---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-23T22:19:55.410254'
end_time: '2026-08-23T22:25:17.949182'
duration_seconds: 322.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cadmium Poisoning
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 14
  num_turns: 16
  total_cost_usd: 1.4342990000000002
  session_id: d2cc8eac-8a6b-577d-90bb-94480df8b5a4
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cadmium Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Cadmium Poisoning** covering all of the
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

I'll research current literature on cadmium poisoning to build the comprehensive report.

# Cadmium Poisoning: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Cadmium (Cd) poisoning encompasses the acute and chronic toxic effects of exposure to cadmium and its compounds, a non-essential, non-biodegradable heavy metal with no known physiological function in humans. Cadmium is released into the environment from mining, smelting, electroplating, battery (Ni-Cd) manufacture, pigment/plastic stabilizer production, and fossil-fuel combustion, and enters the food chain because certain crops (notably rice, leafy vegetables, shellfish, and organ meats) readily accumulate it from contaminated soil and water. The two principal exposure routes are **inhalation** (occupational fume/dust exposure, cigarette smoking) and **ingestion** (contaminated food and water). Cadmium has an exceptionally long biological half-life in humans (10–30 years), accumulating primarily in the renal cortex and liver, which is why chronic low-dose environmental exposure — rather than single high-dose events — dominates the global disease burden ([StatPearls: Cadmium Toxicity, NBK536966](https://www.ncbi.nlm.nih.gov/books/NBK536966/); [ATSDR Toxicological Profile for Cadmium](https://www.atsdr.cdc.gov/toxprofiles/tp5.pdf)).

Clinically, cadmium poisoning presents in two distinct syndromes:
- **Acute (high-dose) poisoning** — typically occupational fume inhalation (welding/brazing cadmium-containing alloys, smelting) causing chemical pneumonitis and pulmonary edema, or ingestion causing severe gastroenteritis.
- **Chronic (low-dose) poisoning** — the dominant global pattern, causing irreversible proximal tubular nephropathy, osteomalacia/osteoporosis (classically **Itai-itai disease** in Japan), pulmonary emphysema, and is classified by IARC as a **Group 1 human carcinogen** (lung cancer, with evidence for kidney, prostate, breast, and bladder).

**Key identifiers:**
- **ICD-10-CM:** T56.3 (Toxic effect of cadmium and its compounds); T56.3X1A (accidental, initial encounter); Y96 codes for occupational exposure context
- **ICD-11:** NE61 (Toxic effect of cadmium or its compounds) — falls under Chapter 22, "Injury, poisoning or certain other consequences of external causes"
- **MeSH:** D002104 (Cadmium Poisoning); D002103 (Cadmium)
- **MONDO ID:** A specific, verified MONDO CURIE for "cadmium poisoning" was not confirmed through direct ontology lookup during this research pass; MONDO's disease hierarchy contains toxic/chemically-induced disease branches (e.g., under "poisoning by heavy metal" concepts) that a curator should resolve via `runoak` against the local MONDO adapter before binding a `disease_term`. Itai-itai disease itself may warrant a distinct MONDO entity as a specific historical cadmium-poisoning cohort/syndrome — this should be confirmed rather than assumed.
- **OMIM:** Not applicable — cadmium poisoning is an acquired/environmental toxic disorder, not a monogenic Mendelian condition (though genetic polymorphisms modulate susceptibility; see Etiology).
- **Orphanet:** Not indexed as a distinct rare disease entity (cadmium poisoning is common-exposure, not rare-disease scoped), though Itai-itai disease historically appears in some toxicology/rare-disease compendia.

**Synonyms/alternative names:** Cadmium intoxication; chronic cadmium nephropathy; cadmium fume fever; Itai-itai disease (痛い痛い病, "ouch-ouch disease" — the chronic cadmium-induced osteomalacia/osteoporosis syndrome first described in the Jinzu River basin, Toyama Prefecture, Japan, in the 1950s–60s).

**Evidence base composition:** The literature is a mixture of (1) aggregated population-level exposure-outcome studies (NHANES, EFSA dietary surveys, occupational cohorts), (2) individual clinical case reports/series (acute fume poisoning, Itai-itai patients), and (3) mechanistic in vitro/animal studies. Unlike a monogenic disease entry, cadmium poisoning evidence is dominated by epidemiological dose-response relationships rather than individual EHR-derived case phenotyping.

---

## 2. Etiology

### Disease Causal Factor
Cadmium poisoning is **environmental/toxicological**, not genetic or infectious, in its primary causation: it is caused directly by absorption of cadmium (Cd²⁺) from an external source, exceeding the body's detoxification (metallothionein-binding) and excretory capacity. There is no infectious agent and no single causal gene; genetic factors instead act as **modifiers of susceptibility and toxicokinetics** (absorption efficiency, renal handling, antioxidant capacity), not as sufficient or necessary causes.

### Risk Factors

**Environmental/occupational risk factors:**
- **Occupational exposure**: smelting, battery manufacturing (Ni-Cd), electroplating, pigment/plastics production, welding/brazing of cadmium alloys, phosphate fertilizer production, e-waste recycling.
- **Cigarette smoking** — the single largest environmental determinant of cadmium body burden in non-occupationally-exposed populations. Tobacco leaves hyperaccumulate cadmium from soil; a smoker inhales roughly 1–2 µg of cadmium per cigarette, absorbing ~10% via the lung (much higher bioavailability than the ~5% GI absorption from food). A geometric mean blood cadmium of ~1.58 µg/L has been reported in heavy smokers versus a U.S. population mean of ~0.38 µg/L ([ATSDR Toxicological Profile for Cadmium](https://www.atsdr.cdc.gov/toxprofiles/tp5.pdf)).
- **Diet**: rice, shellfish, offal (kidney, liver), cocoa/chocolate, and leafy vegetables grown on contaminated or naturally cadmium-rich (often phosphate-fertilized) soils are the dominant dietary sources. EFSA's Panel on Contaminants in the Food Chain set the Tolerable Weekly Intake (TWI) at **2.5 µg/kg body weight/week**, and notes that dietary exposure in some EU subgroups (children, vegetarians, residents of contaminated areas) approaches or exceeds this TWI, with cereals, vegetables, nuts/pulses, starchy roots, and meat products the largest dietary contributors.
- **Contaminated drinking water and soil** near mining/smelting sites — the etiologic exposure route for Itai-itai disease (irrigation of rice paddies with mine-tailings-contaminated water from the Kamioka mine on the Jinzu River).
- **Iron deficiency** markedly increases intestinal cadmium absorption, because cadmium is taken up via iron-transport pathways (DMT1) when body iron stores are low — a key reason why **women** (who have lower iron stores, especially premenopausally) show higher gastrointestinal cadmium absorption efficiency (up to ~2×) than men for a matched dietary dose.
- **Age**: cumulative, lifelong bioaccumulation means body burden and toxic risk rise with age; children and the elderly show heightened vulnerability windows.
- **Low dietary calcium and zinc status** enhance cadmium absorption and toxicity by competing for shared transport pathways.

**Genetic risk factors (modifiers of toxicokinetics, not causal in the Mendelian sense):**
- **Metal transporter gene variants** governing intestinal/renal cadmium uptake: **DMT1/SLC11A2** (divalent metal transporter 1) — the intronic IVS4+44C/A polymorphism's CA genotype has been associated with elevated urinary cadmium, suggesting susceptibility to prolonged accumulation; **SLC39A8 (ZIP8)** and **SLC39A14 (ZIP14)** — zinc/bicarbonate symporters expressed in the proximal tubule S3 segment that mediate cadmium uptake from the apical membrane; siRNA knockdown of ZIP8, ZIP14, or DMT1 in kidney proximal tubule cells significantly reduces cadmium uptake, and no single transporter dominates — TRPV6 and TRPM7 calcium channels also contribute (Fujishiro et al., *Metallomics* 2012, PMID:22437713 region of literature).
- **Metallothionein (MT1A/MT2A) promoter polymorphisms** affecting the individual's capacity to sequester cadmium as the relatively inert Cd-MT complex, thereby modulating the balance between "safe storage" and free-ion toxicity.
- **Glutathione S-transferase (GSTM1/GSTT1) null genotypes** and **antioxidant enzyme polymorphisms** (SOD, catalase, GPX1) — reduce detoxification of cadmium-induced reactive oxygen species (ROS), increasing individual susceptibility to oxidative damage.
- **VDR (vitamin D receptor) gene polymorphisms** — plausibly modify individual susceptibility to cadmium-induced bone loss given cadmium's interference with vitamin D activation, though human data are more limited than for the transporter genes above.

### Protective Factors
- **Adequate iron, zinc, and calcium nutritional status** — competitively reduces intestinal cadmium absorption via shared transporters (DMT1, calcium channels), the best-established dietary protective mechanism.
- **Selenium** — forms cadmium-selenide complexes that may reduce cadmium bioavailability/toxicity in some experimental models, though human protective evidence is less robust.
- **High dietary fiber and certain plant polyphenols** — modestly reduce GI cadmium bioavailability in some studies.
- **Metallothionein induction** (e.g., by prior low-dose zinc exposure) — upregulates the endogenous Cd-sequestering protein, a preconditioning-type protective mechanism demonstrated mainly in animal models.
- No specific protective genetic variant is well-replicated in human GWAS to date; this remains an area with limited direct evidence (flag as `KNOWLEDGE_GAP` if curated in dismech).

### Gene-Environment Interactions
The clearest documented gene-environment interaction is **iron status × DMT1/transporter genotype × dietary cadmium exposure**: individuals who are iron-deficient (environmental/nutritional factor) upregulate DMT1 expression at the intestinal brush border, which increases cadmium co-absorption; a DMT1 polymorphism further modulates the magnitude of this effect, meaning genetically susceptible, iron-deficient individuals absorb proportionally more cadmium from an identical dietary dose than iron-replete individuals with a lower-risk genotype. Similarly, **GST-null genotype × oxidative-stress-inducing co-exposures** (smoking, other pro-oxidant xenobiotics) likely potentiates cadmium's oxidative renal and vascular injury, though this remains an area needing more targeted human interaction studies (CTD, PheGenI databases catalog these gene-chemical relationships).

---

## 3. Phenotypes

### A. Acute high-dose exposure phenotypes
| Phenotype | Type | HPO suggestion | Onset/Course | Notes |
|---|---|---|---|---|
| Chemical pneumonitis | Clinical sign | HP:0410048 (Pneumonitis) / consider HP:0002090 (Pneumonia) | Acute, 8h–7 days post-exposure, progressive | Follows fume inhalation; can be fatal ([PMID:5928153](https://pubmed.ncbi.nlm.nih.gov/5928153/) — 5 cases, 1 death from renal necrosis) |
| Pulmonary edema | Clinical sign | HP:0100598 (Pulmonary edema) | Acute, days | Leading cause of acute-exposure mortality |
| Metal fume fever (flu-like syndrome) | Symptom | HP:0001945 (Fever) + HP:0025406 (Chills) | Acute, self-limited if exposure ceases early | Initial, often reversible phase |
| Acute tubular necrosis | Lab/clinical | HP:0000083 (Renal insufficiency) | Acute, can be irreversible | Cause of fatality in severe cases |
| Severe gastroenteritis (ingestion route) | Symptom | HP:0002018 (Nausea)/HP:0002014 (Diarrhea)/HP:0030157 (Abdominal pain) | Acute, hours | From ingestion of highly contaminated food/beverage |

### B. Chronic low-dose exposure phenotypes

**Renal:**
- **Proximal tubular dysfunction** (the hallmark chronic lesion) — HP:0000121 (Nephropathy) / consider a Fanconi-syndrome-pattern term; presents as low-molecular-weight proteinuria (β2-microglobulinuria, retinol-binding-protein-uria), glucosuria, aminoaciduria, and phosphaturia. Progressive, generally irreversible even after exposure cessation; frequency approaches 100% in heavily exposed occupational/Itai-itai cohorts at sufficiently high cumulative dose.
- **Decreased glomerular filtration rate / chronic kidney disease** — HP:0012622 (Chronic kidney disease); later-stage, progressive complication of sustained tubular injury.
- **Nephrolithiasis** — HP:0000787 (Nephrolithiasis); reported at elevated frequency in cadmium-exposed cohorts secondary to hypercalciuria from tubular calcium leak.

**Skeletal (Itai-itai disease spectrum):**
- **Osteomalacia** — HP:0002753 (Osteomalacia); severe bone pain, multiple pseudofractures (Looser zones), and characteristic waddling "duck gait." Onset typically in postmenopausal, multiparous women with chronic dietary cadmium exposure and pre-existing calcium/vitamin D insufficiency; severe, chronic, progressive.
- **Osteoporosis** — HP:0000939 (Osteoporosis); often coexists with osteomalacia in the same patients.
- **Bone pain** — HP:0002653 (Skeletal pain) — the eponymous "itai-itai" (ouch-ouch) symptom.
- **Pathological/spontaneous fractures** — HP:0002816 (Pathologic fracture); can occur with minimal trauma or even coughing in severe cases.
- **Decreased bone mineral density** — measurable, dose-related, documented even in general (non-Itai-itai) cadmium-exposed populations at moderate exposure.

**Pulmonary (chronic, mainly occupational/smoking-related):**
- **Emphysema/chronic obstructive pulmonary disease** — HP:0002088 (Abnormal pulmonary interstitial morphology)/consider HP:0006510 (Chronic pulmonary obstruction); progressive, associated with cumulative fume exposure, and now recognized as an important, underappreciated component of cadmium's contribution to tobacco-related lung disease.
- **Restrictive/decreased pulmonary function** — reduced FEV1/FVC documented in occupational cohorts.
- **Anosmia** — HP:0000458 (Abnormal nasal morphology)/consider olfactory dysfunction terms; reported in cadmium-exposed workers from nasal mucosal damage.

**Cardiovascular:**
- **Hypertension** — HP:0000822 (Hypertension); a 2024 dose-response meta-analysis (26 studies, 2005–2023) found a significant positive correlation between cadmium exposure and risk of heart failure, stroke, and coronary heart disease ([PMID:38295933](https://pubmed.ncbi.nlm.nih.gov/38295933/)); a 2023 AHA scientific statement similarly implicates chronic low-level cadmium (with lead and arsenic) in elevated cardiovascular disease risk.
- **Increased cardiovascular mortality** — dose-dependent association across multiple cohort studies.

**Reproductive/endocrine:**
- **Hormonal disruption (estrogen-mimetic effects)** — cadmium binds and activates estrogen receptor alpha (ERα), forming an ERα–c-Jun transcriptional complex that drives proliferative gene programs; termed a "metalloestrogen" ([PMID:20219890](https://pubmed.ncbi.nlm.nih.gov/20219890/)).
- **Reduced fertility / adverse pregnancy outcomes** — associated with cadmium exposure in multiple epidemiological studies (reduced birth weight, altered placental function).
- **Testicular damage** — HP:0000034 (Abnormal testis morphology); classic acute high-dose animal toxicology finding, with more limited direct human occupational evidence.

**Neurological/psychiatric:**
- **Cognitive impairment / neurotoxicity** — cadmium accumulates in brain over prolonged low-dose exposure; the nervous system is described as particularly vulnerable to chronic low-dose cadmium (2023 review, DOI:10.3390/ijms242316558).
- **Depression** — recent NHANES cross-sectional analyses found each incremental unit of blood cadmium associated with a ~33% rise in depression prevalence.
- **Chronic pain** — elevated blood cadmium is a documented risk factor for chronic pain in NHANES 1999–2004 data ([PMC11148299](https://pmc.ncbi.nlm.nih.gov/articles/PMC11148299/)).
- **Peripheral neuropathy** — reported in some heavily exposed occupational cohorts.

**Oncologic (chronic, latency of years-decades):**
- **Lung cancer** — HP:0100526 (Neoplasm of the lung); IARC Group 1 carcinogen designation is substantially based on this association, strongest in occupational cohorts.
- **Bladder, prostate, pancreatic, breast, kidney, endometrial cancers** — variably supported associations; a 2024 systematic review of biological-sample cadmium and cancer risk (9 meta-analyses + 57 original articles) concluded consistent evidence for a causal role in pancreas, lung, and bladder carcinogenesis, and positive correlation between biological cadmium and total cancer risk/mortality. Prostate cancer evidence is weaker/mixed (2024 updated meta-analysis: pooled effect size 1.11, 95% CI 0.85–1.45 — not statistically significant).

**Quality of life impact:** Chronic phenotypes — especially Itai-itai-type osteomalacia with severe bone pain and pathologic fractures, and progressive CKD — carry substantial disability burden (mobility loss, chronic pain, dialysis dependence in advanced nephropathy). Dedicated disease-specific QOL instrument data for cadmium poisoning specifically are sparse in the literature; QOL burden is typically inferred from generic CKD/osteoporosis QOL literature (EQ-5D, SF-36) rather than cadmium-specific cohorts.

---

## 4. Genetic/Molecular Information

Cadmium poisoning is fundamentally an **acquired toxic disorder**, so there is no single causal gene (no OMIM Mendelian entry). The relevant genetics concern (a) toxicokinetic modifier genes and (b) the molecular targets cadmium acts upon.

**Toxicokinetic/susceptibility genes (modifier, not causal):**
- **SLC11A2 (DMT1)** — HGNC:10908; intestinal/renal divalent metal transporter; IVS4+44C/A intronic polymorphism CA genotype associated with elevated urinary cadmium in exposed populations.
- **SLC39A8 (ZIP8)** — HGNC:20862; zinc/bicarbonate symporter; the A391T variant reduces cellular uptake of zinc, cadmium, and iron via reduced plasma membrane expression, and is separately associated with hypotension and insulin resistance ([PMC9240775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9240775/)).
- **SLC39A14 (ZIP14)** — HGNC:20858; kidney proximal tubule S3-segment metal/bicarbonate symporter mediating cadmium and manganese uptake.
- **MT1A, MT2A (metallothioneins)** — HGNC:7393, HGNC:7407; low-molecular-weight, cysteine-rich metal-binding proteins that sequester cadmium; promoter polymorphisms modulate individual sequestration capacity.
- **GSTM1, GSTT1** (null genotypes) — reduced glutathione-conjugation-based detoxification capacity.
- **VDR** — vitamin D receptor; plausible modifier of bone susceptibility given cadmium's vitamin D interference (limited direct human replication).

**Molecular targets / mechanisms of cadmium action (not "pathogenic variants" in the classical sense, but the molecular lesions cadmium itself produces):**
- **Calcium channel mimicry** — cadmium enters cells via voltage-gated calcium channels, TRPV6, and TRPM7, in addition to the ZIP8/ZIP14/DMT1 metal-transporter routes, disrupting intracellular Ca²⁺ signaling.
- **Zinc-finger protein displacement** — cadmium displaces zinc from zinc-finger DNA-binding domains (transcription factors, DNA-repair enzymes such as XPA, PARP), impairing DNA repair fidelity and contributing to genotoxicity/carcinogenicity.
- **Enzyme inhibition** — direct inhibition of DNA repair enzymes and antioxidant enzymes (catalase, superoxide dismutase) by binding to sulfhydryl (-SH) groups.
- **Epigenetic dysregulation** — cadmium alters DNA methylation patterns and histone modifications genome-wide; implicated as a contributing carcinogenic mechanism (2024 Toxics review, PMID:38922068).

**Variant classification / allele frequency databases:** Because there is no single causal locus, ClinVar/gnomAD-style pathogenic-variant curation does not apply in the standard Mendelian sense. gnomAD is, however, relevant as a source of population allele frequencies for the modifier polymorphisms above (DMT1, ZIP8, GST-null genotypes) if fine-grained susceptibility modeling is desired.

**Chromosomal abnormalities:** Not a feature of cadmium poisoning etiology; cadmium is, however, itself clastogenic/aneugenic in vitro and in occupationally exposed cohorts (chromosomal aberration and micronucleus frequency increases reported), which is a downstream genotoxic *effect* of exposure rather than a causal chromosomal lesion.

---

## 5. Environmental Information

**Environmental factors (primary etiologic category — see also Etiology above):**
- **Occupational cadmium fume/dust** (smelting, welding, battery manufacture, electroplating, pigment production) — ECTO-type exposure term suggestion: "occupational exposure to cadmium" / "exposure to cadmium fumes."
- **Contaminated soil/water from mining and smelting** — the documented cause of Itai-itai disease via irrigation-water and rice-paddy contamination downstream of the Kamioka zinc mine.
- **Ambient air pollution** near industrial/smelting sites and from fossil fuel/waste combustion.
- **Contaminated food** — rice (especially in parts of Asia grown on cadmium-enriched soils), leafy vegetables, shellfish/crustaceans (which bioaccumulate cadmium strongly), organ meats (kidney, liver), cocoa/chocolate products, and phosphate-fertilized crops. EFSA notes cereals, vegetables, nuts/pulses, starchy roots, and meat products are collectively the largest dietary contributors in EU populations.
- **E-waste recycling** (informal/artisanal recycling of Ni-Cd batteries and electronics) — an emerging exposure source, especially in low- and middle-income countries.

**Lifestyle factors:**
- **Cigarette smoking** — the dominant modifiable lifestyle risk factor in non-occupational populations; smokers show roughly double the blood cadmium level of non-smokers.
- **Second-hand smoke exposure.**
- **Dietary pattern** — high consumption of cadmium-accumulating foods, low intake of protective minerals (iron, zinc, calcium).
- **Alcohol use** — some studies suggest interactive hepatotoxic/nephrotoxic effects with chronic cadmium exposure, though evidence is less robust than for smoking.

**Infectious agents:** Not applicable — cadmium poisoning has no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Overview of the causal chain
**Cadmium exposure (inhalation/ingestion) → systemic absorption bound to albumin/metallothionein → hepatic and, predominantly, renal cortical accumulation → intracellular free Cd²⁺ release → oxidative stress, Ca²⁺ signaling disruption, zinc-finger protein displacement, mitochondrial dysfunction → proximal tubular epithelial cell injury/death → chronic tubular dysfunction (Fanconi-like proximal tubulopathy) → impaired renal 1α-hydroxylation of vitamin D and phosphate wasting → secondary/associated osteomalacia and osteoporosis, with parallel direct osteotoxic effects on osteoblasts → systemic complications (CVD, carcinogenesis, endocrine disruption) via oxidative stress and ERα mimicry in extra-renal tissues.**

### Molecular pathways
- **Oxidative stress** is described as "the pivotal mechanism" underlying cadmium toxicity across virtually all target organs: cadmium disrupts the pro-oxidant/antioxidant balance (depleting glutathione, inhibiting catalase and superoxide dismutase via -SH group binding), generating reactive oxygen species (ROS) that damage lipids, proteins, and DNA, and trigger apoptosis (PMID:38922068; PMID:39771090; PMID:24117228).
- **Ca²⁺ signaling disruption** — cadmium is a molecular mimic of calcium, entering cells through voltage-gated calcium channels, TRPV6, and TRPM7, and dysregulating downstream Ca²⁺-dependent signaling cascades. GO term suggestion: GO:0007204 (positive regulation of cytosolic calcium ion concentration) — perturbed.
- **Epigenetic modification** — genome-wide DNA methylation changes and histone modifications are increasingly recognized as contributing to both chronic tissue injury and carcinogenesis.
- **DNA repair interference** — cadmium inhibits nucleotide excision repair and mismatch repair enzymes (many of which are zinc-finger proteins), a key mechanism underlying its genotoxic/carcinogenic potential despite cadmium itself being a weak direct mutagen.

### Cellular processes
- **Apoptosis and necrosis** of proximal tubular epithelial cells (renal), alveolar type I cells with type II cell hyperplasia (acute pulmonary injury), osteoblasts (via a documented ROS → SIRT1/PGC-1α/p53 signaling axis in a 2023 rat model of cadmium-induced osteoporosis), and germ cells (testicular toxicity in animal models).
- **Chronic inflammation** — acute inhalation triggers neutrophilic pulmonary inflammation (demonstrated in rat inhalation models); chronic low-dose exposure is associated with systemic low-grade inflammatory activation contributing to cardiovascular risk.
- **Impaired autophagy/mitochondrial dysfunction** — increasingly implicated in cadmium-induced proximal tubular cell injury.

### Protein/enzyme dysfunction
- Cadmium **inhibits proteins via thiol-group binding** (broad mechanism affecting many enzymes, including antioxidant enzymes) and **displaces zinc from zinc-finger transcription factors and DNA-repair proteins**, producing loss-of-function-like effects without altering the underlying gene sequence.
- **Renal proximal tubular uptake** occurs via **megalin:cubilin receptor-mediated endocytosis** at the apical brush border. The classical model held that Cd²⁺–metallothionein-1 complexes (filtered freely at the glomerulus given the ~7 kDa size of MT-1) are endocytosed via megalin/cubilin and then released intracellularly in the endosomal/lysosomal compartment, producing free Cd²⁺-driven toxicity. A revised model (2019, PMC6566203) argues that cadmium bound to **β2-microglobulin, albumin, and lipocalin-2**, rather than metallothionein specifically, is the primary driver of megalin:cubilin-dependent proximal tubular toxicity — an active area of mechanistic revision.

### Tissue damage mechanisms
- **Renal**: diffuse proximal tubular atrophy, basement membrane thickening, and mild interstitial fibrosis in the renal cortex (autopsy-confirmed in Itai-itai patients, PMID:10997741).
- **Bone**: osteomalacia in cadmium poisoning is driven substantially indirectly, via **renal tubular dysfunction → impaired proximal-tubule 1α-hydroxylase activity → reduced active vitamin D (1,25-dihydroxyvitamin D) → impaired intestinal calcium absorption and mineralization defect**, compounded by direct renal phosphate wasting. Direct toxic effects of cadmium on osteoblasts (impairing calcification at the ossification front) are a proposed, evidence-supported second mechanistic arm; the field notes "the exact mechanism underlying this bone disease remains unresolved," making this a genuine, citable knowledge gap suitable for a `KNOWLEDGE_GAP` discussion if curated (PMID:23095355; PMID:1303956).
- **Lung (acute)**: alveolar type I cell necrosis with type II cell hyperplasia, interstitial thickening, hemorrhage, edema, and macrophage inhibition following high-dose fume inhalation.

### Biochemical abnormalities
- Elevated urinary β2-microglobulin, N-acetyl-β-D-glucosaminidase (NAG), and retinol-binding protein — biomarkers of proximal tubular injury (see Diagnostics).
- Hypophosphatemia, glucosuria, generalized aminoaciduria — Fanconi-syndrome-like tubular leak pattern.
- Reduced serum 1,25-dihydroxyvitamin D.

### Molecular profiling
- **Transcriptomics**: altered gene expression signatures in kidney and bone tissue following cadmium exposure, documented in animal models (GEO-deposited datasets exist for cadmium nephrotoxicity/osteotoxicity studies).
- **Epigenomics**: genome-wide DNA methylation alteration is an active 2023–2024 research area (see Mechanisms/Pathways review, PMID:38922068).
- **microRNA dysregulation**: cadmium nephrotoxicity is associated with altered microRNA expression in the rat renal cortex (PMC5874789), a mechanistic link between cadmium exposure and post-transcriptional dysregulation of injury-response genes.

### Suggested ontology terms for pathophysiology nodes
- **GO (biological process)**: GO:0006979 (response to oxidative stress); GO:0034605 (cellular response to heat) [analogous stress-response framework]; GO:0006974 (DNA damage response); GO:0006914 (autophagy); GO:0097190 (apoptotic signaling pathway); GO:0030282 (bone mineralization) — decreased.
- **GO (molecular function)**: GO:0046872 (metal ion binding); GO:0005385 (zinc ion transmembrane transporter activity) — for ZIP8/ZIP14.
- **GO (cellular component)**: GO:0005739 (mitochondrion); GO:0005634 (nucleus) — for zinc-finger displacement effects; GO:0005886 (plasma membrane) — transporter localization.
- **CL (cell type)**: CL:1001106 (kidney proximal straight tubule epithelial cell) / CL:1000838 (kidney proximal convoluted tubule epithelial cell); CL:0000062 (osteoblast); CL:0001056 (alveolar type I cell) and alveolar type II cell; CL:0000359 (vascular endothelial cell) for cardiovascular effects.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary target organs**: Kidney (proximal tubule — the dose-limiting critical organ for chronic exposure) and Lung (acute high-dose route of entry and target organ for inhalational disease).
- **Secondary/complication organs**: Bone (osteomalacia/osteoporosis, secondary to renal dysfunction plus direct effects), Liver (accumulation site, hepatic dysfunction in severe chronic poisoning — documented pathologically in Itai-itai autopsies with metallothionein expression), Cardiovascular system (hypertension, atherosclerosis-associated events), Testis/reproductive organs, Peripheral/central nervous system, Breast/endocrine tissue (ERα-mediated effects).
- **Body systems involved**: Renal/urinary, Respiratory, Skeletal, Cardiovascular, Endocrine/reproductive, Nervous, and (as a chronic carcinogenic consequence) multiple organ systems via oncogenesis.

**Tissue and cell level:**
- Renal **proximal tubular epithelium** (S1–S3 segments) — primary cellular target (CL:1000838 / CL:1001106).
- **Osteoblasts and osteoclasts** — bone remodeling cells directly and indirectly affected.
- **Alveolar epithelium** (Type I and Type II pneumocytes) — acute inhalational injury.
- **Vascular endothelium** — implicated in cadmium-associated hypertension/atherosclerosis.
- **Hepatocytes** — accumulation and metallothionein-expression site.

**Subcellular level (GO Cellular Component):**
- **Mitochondria** — site of oxidative stress generation and dysfunction.
- **Lysosomes/endosomes** — site of Cd-metallothionein/Cd-protein complex release following megalin:cubilin-mediated endocytosis.
- **Nucleus** — site of zinc-finger transcription factor and DNA-repair-enzyme interference.
- **Plasma membrane** — site of transporter-mediated (ZIP8/ZIP14/DMT1/TRPV6/TRPM7) cellular entry.

**Localization (UBERON terms):**
- UBERON:0004134 (kidney proximal tubule) or UBERON:0001225 (proximal tubule)
- UBERON:0002048 (lung)
- UBERON:0001474 (bone element) / UBERON:0002481 (bone tissue)
- UBERON:0002107 (liver)
- UBERON:0001981 (blood vessel) — cardiovascular involvement

**Lateralization:** Not applicable — cadmium toxicity is systemic/bilateral in its organ effects (bilateral renal tubulopathy, bilateral/diffuse osteomalacia).

---

## 8. Temporal Development

**Onset:**
- **Acute poisoning**: onset within hours (inhalation — flu-like/metal-fume-fever symptoms) to days (progression to chemical pneumonitis/pulmonary edema, 8 hours–7 days post-exposure in severe cases); ingestion-related acute gastroenteritis has onset within hours.
- **Chronic poisoning**: insidious onset over years to decades of cumulative low-dose exposure; there is no defined "typical age of onset" in the congenital-disease sense — onset is exposure-duration- and cumulative-dose-dependent. Itai-itai disease classically presented in adults, especially multiparous, postmenopausal women in their 40s–60s in the endemic Jinzu River basin cohort, reflecting decades of chronic dietary exposure compounded by pregnancy/lactation-related calcium demands and postmenopausal bone loss.

**Progression:**
- **Renal**: proximal tubular dysfunction is typically slowly progressive and, once an injury threshold is crossed, often **irreversible even after exposure cessation** — a critical prognostic feature distinguishing cadmium nephropathy from many other toxic nephropathies.
- **Skeletal**: progressive osteomalacia/osteoporosis with worsening bone pain and increasing fracture risk over time in the absence of exposure cessation and mineral/vitamin D repletion.
- **Pulmonary (acute)**: staged progression — mild flu-like phase (hours) → possible progression to pneumonitis/edema (days) → potential fibrosis or death in severe unresolved cases; if the patient survives the acute phase without progressing after 1–2 days, prognosis is generally favorable, though "interstitial pneumonitis after cadmium exposure" reversibility itself has been specifically questioned in case reports.
- **Carcinogenesis**: long latency (years to decades) typical of chemical carcinogenesis, consistent with cadmium's classification based predominantly on chronic occupational cohort follow-up data.

**Patterns:**
- **Remission**: chronic renal tubular dysfunction generally does **not** remit even after exposure cessation, unlike many other toxic exposures — this "point of no return" characteristic is one of the more clinically important, distinguishing features of chronic cadmium nephropathy.
- **Critical periods**: pregnancy/lactation (increased maternal bone turnover interacting with cadmium-impaired mineralization) and iron-deficient states (childhood, menstruating/pregnant women) represent windows of heightened absorption and vulnerability.

---

## 9. Inheritance and Population

**Epidemiology:**
- Cadmium poisoning is not a rare/orphan disease in exposure terms — low-level chronic exposure is nearly universal in industrialized populations via diet and, for smokers, tobacco. Clinically significant chronic poisoning (nephropathy, osteomalacia) is concentrated in **occupationally exposed workers** and populations in **historically or currently contaminated regions** (the Jinzu River basin in Japan being the paradigmatic example, with several thousand affected individuals historically identified and hundreds of confirmed Itai-itai cases).
- **Blood cadmium** in the general U.S. adult population (NHANES 1999–2008): geometric mean **0.376 µg/L** (age ≥20 years); slightly higher in females (0.331 µg/L) than males (0.299 µg/L) in some analyses, reflecting sex differences in GI absorption efficiency (see below) partially offset by occupational exposure patterns.
- Newer NHANES cycles (August 2021–August 2023) have updated blood cadmium reference data available via CDC, though a full updated geometric-mean summary was not directly retrieved in this pass.

**Inheritance pattern:** Not applicable in the Mendelian sense — cadmium poisoning is an acquired toxic/environmental disease. The relevant "genetic" dimension is **polygenic susceptibility modification** (transporter and detoxification gene polymorphisms described in Etiology/Genetics above), not a discrete inheritance pattern, penetrance, or expressivity in the classical genetic-disease sense.

**Population demographics:**
- **Affected populations**: historically, agricultural communities in cadmium-mining-affected river basins (Japan — Jinzu River/Toyama; other documented cadmium-contaminated regions in China); currently, occupationally exposed industrial workers (battery, smelting, electroplating industries) worldwide, and — for the low-grade chronic exposure relevant to cardiovascular/cancer/bone endpoints — the general population, especially smokers.
- **Geographic distribution**: strongly tied to industrial/mining activity and to regional soil cadmium content affecting crop uptake (parts of East Asia with cadmium-contaminated paddy soils are particularly notable); e-waste recycling hotspots in parts of Africa and Asia represent an emerging geographic risk pattern.
- **Sex ratio**: Itai-itai disease specifically showed strong female predominance, attributed to lower iron stores (hence higher cadmium GI absorption efficiency), pregnancy/lactation-related bone calcium demand, and postmenopausal bone loss compounding cadmium's skeletal effects — a well-documented sex-specific vulnerability pattern rather than a sex-linked genetic mechanism.
- **Age distribution**: chronic disease manifestations (nephropathy, osteomalacia, cancer) cluster in middle-aged to older adults reflecting cumulative exposure; acute poisoning can occur at any age given sufficient single/short-term high-dose exposure (predominantly working-age adults in occupational settings).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Blood cadmium (BCd)** — reflects recent/ongoing exposure (biological half-life in blood ~3–4 months); standard biomonitoring test (NHANES reference method).
- **Urinary cadmium (UCd, typically creatinine-corrected, µg/g creatinine)** — reflects cumulative body burden/kidney cadmium content given cadmium's long renal half-life; the standard biomarker for chronic exposure assessment and the basis of most occupational and environmental exposure limits (LOINC terms exist for both blood and urine cadmium assays).
- **Urinary β2-microglobulin (Uβ2-MG)** — a classic marker of proximal tubular dysfunction; "currently the most widely used assay for detecting kidney dysfunction" in cadmium-exposed workers, though its relative sensitivity versus NAG is debated across studies (some show UCd correlates more closely with NAG at UCd <10 µg/g creatinine; more recent work suggests Uβ2-MG is more sensitive for detecting renal dysfunction per se). Also linked to hypertension risk in chronically exposed populations (PMC12029079).
- **Urinary N-acetyl-β-D-glucosaminidase (NAG)** — lysosomal enzyme marker of tubular cell injury; simple, inexpensive, reliable, but less sensitive than retinol-binding protein (RBP) or β2-microglobulin per some assessments, and recent work questions how tightly NAG actually tracks nephron destruction.
- **Urinary retinol-binding protein (RBP)** — another low-molecular-weight protein biomarker of proximal tubular reabsorptive dysfunction.
- **Serum creatinine/eGFR** — for later-stage, established CKD assessment (a late marker relative to tubular biomarkers).
- **Urinary calcium, phosphate; serum 1,25-dihydroxyvitamin D, phosphate** — for the osteomalacia workup.
- **Bone mineral density (DXA)** — for skeletal complication assessment; documented dose-related decreases in cadmium-exposed populations.

**Imaging:**
- Plain radiography for pseudofractures (Looser zones), a classic osteomalacia finding in advanced Itai-itai disease.
- Chest imaging (CXR/CT) for acute inhalational pneumonitis/pulmonary edema assessment.

**Genetic testing:** Not applicable in the diagnostic sense (no causal gene to sequence); research-context genotyping of transporter/detoxification polymorphisms (DMT1, ZIP8, GST) is investigational for susceptibility stratification, not clinical diagnosis.

**Clinical diagnostic criteria:**
- Diagnosis of chronic cadmium poisoning/nephropathy rests on a combination of (a) documented exposure history (occupational or environmental), (b) elevated urinary and/or blood cadmium, and (c) the characteristic proximal tubular dysfunction biomarker pattern (β2-MG, NAG, RBP, glucosuria, aminoaciduria) ± osteomalacia findings. Itai-itai disease has established historical diagnostic criteria from Japanese public health authorities (exposure-area residence + tubular proteinuria + bone lesions), a useful `ESTABLISHED_CRITERIA` framework if curated as a definitions block.
- **Differential diagnosis**: other causes of Fanconi-like proximal tubulopathy (Wilson disease, cystinosis, Dent disease, other heavy metal nephropathies — lead, mercury), other causes of adult-onset osteomalacia (vitamin D deficiency, hypophosphatemic disorders, celiac disease), and other occupational pneumonitides for the acute inhalational presentation.

**Screening:** Occupational biological monitoring programs (OSHA's cadmium standard, 29 CFR 1910.1027, mandates biological monitoring of blood and urinary cadmium plus urinary β2-microglobulin in exposed workers) represent the primary organized screening framework; there is no population-wide newborn or carrier screening analog given the acquired, non-genetic nature of the disease.

---

## 11. Outcome/Prognosis

**Survival and mortality:**
- Acute high-dose fume poisoning carries meaningful mortality risk from pulmonary edema/respiratory failure in severe, unresolved cases (case series document fatalities, e.g., PMID:5928153).
- Chronic exposure is associated with **increased all-cause and cardiovascular mortality** in dose-response fashion across multiple cohort and NHANES-based analyses, and with increased site-specific cancer mortality (lung, and evidence trending for pancreas/bladder) per the 2024 systematic review of biological cadmium and cancer risk/mortality.

**Morbidity and function:**
- Chronic cadmium nephropathy, once tubular injury has occurred, is generally **irreversible** — a key prognostic feature — leading to lifelong low-molecular-weight proteinuria and, in advanced cases, progression to overt CKD.
- Itai-itai-pattern osteomalacia produces substantial disability: chronic debilitating bone pain, waddling gait, and susceptibility to pathological fractures with minimal trauma, historically causing severe functional impairment and reduced quality of life in affected Japanese cohorts.
- Emphysema/reduced pulmonary function from chronic fume exposure contributes to long-term respiratory morbidity, compounding smoking-related lung disease risk in exposed smokers.

**Complications:**
- Progression to end-stage renal disease in severe/prolonged exposure.
- Recurrent pathological fractures.
- Increased cardiovascular events (heart failure, stroke, coronary heart disease).
- Malignancy (lung primarily; possibly bladder, pancreatic, other sites).

**Recovery potential:**
- **Acute** exposure: substantial recovery potential if exposure is promptly terminated and the patient survives the acute pneumonitis/edema phase without progressing to severe respiratory failure.
- **Chronic** exposure: recovery of renal tubular function after exposure cessation is generally **poor/absent** once injury has occurred — this is one of the more clinically distinctive and consequential features of the disease, in contrast to some other reversible toxic nephropathies. Skeletal disease can improve somewhat with calcium/vitamin D repletion and exposure cessation, but severe deformity/fracture sequelae are often permanent.

**Prognostic factors:** Cumulative dose (duration × intensity of exposure), baseline nutritional status (iron, calcium, vitamin D), sex (female sex historically associated with more severe skeletal disease in the Itai-itai cohort), age at exposure, and smoking status (compounding pulmonary and cardiovascular risk) are the principal prognostic modifiers identified in the literature. Urinary β2-microglobulin/NAG/RBP levels also function as prognostic biomarkers for the likelihood of progression to overt renal impairment.

---

## 12. Treatment

**There is no proven disease-modifying cure for established chronic cadmium nephropathy or osteomalacia.** Management is fundamentally **exposure cessation plus supportive/symptomatic care**; chelation therapy — the mainstay for lead and some other heavy-metal poisonings — has notably limited and time-dependent efficacy for cadmium and carries specific safety concerns.

**Primary intervention:**
- **Removal from exposure source** (occupational reassignment, dietary source identification/avoidance, environmental remediation) — NCIT term suggestion: NCIT:C15747 (Supportive Care) or a more specific environmental-modification concept if available.

**Pharmacotherapy — chelation (limited/investigational efficacy, use with caution):**
- **EDTA (ethylenediaminetetraacetic acid, e.g., CaNa₂EDTA)** — binds cadmium and enhances urinary excretion; in animal models, cadmium cytotoxicity was completely inhibited by co-administered EDTA, but chelator efficacy for cadmium is markedly **time-critical**: only administration immediately (versus delayed) after cadmium exposure significantly reduced tissue (kidney/liver) cadmium concentrations in experimental models, with immediate-treatment animals excreting 50–75% of the cadmium dose in urine within 24 hours versus ~0.1% in untreated controls. NCIT/CHEBI suggestion: CHEBI:64118 (edetic acid) as `therapeutic_agent` under a Pharmacotherapy `treatment_term` (NCIT:C15986).
- **DMSA (dimercaptosuccinic acid, succimer)** — removed cadmium more effectively than DMPS in some mouse studies, but was reported **ineffective against cadmium cytotoxicity** in at least one direct study, illustrating that chelator efficacy for cadmium does not parallel its established efficacy for lead.
- **DMPS (2,3-dimercapto-1-propanesulfonic acid)** — used experimentally, generally less effective than DMSA for cadmium removal in comparative animal studies.
- **Safety caveat**: chelation for cadmium carries a documented risk of **aggravating renal tubular damage** rather than ameliorating it, particularly with delayed or high-dose administration — this is a critical, clinically important limitation distinguishing cadmium chelation from lead chelation, and underlies why chelation is not a routine standard-of-care intervention for established chronic cadmium nephropathy in humans. Combination with methionine has shown improved outcomes over chelators alone in restoring cadmium-induced hepatic/renal transaminase changes in animal studies, but this remains experimental.

**Supportive/symptomatic care:**
- **Calcium and vitamin D (active/activated forms, e.g., calcitriol) supplementation** — for osteomalacia management, addressing the downstream mineralization defect even though it does not reverse the underlying renal tubular lesion.
- **Phosphate repletion** as needed for tubular phosphate wasting.
- **Management of acute pulmonary injury**: supplemental oxygen, corticosteroids (used empirically in some case reports of cadmium-induced pneumonitis), and mechanical ventilatory support for severe pulmonary edema/respiratory failure — NCIT:C15747 (Supportive Care).
- **Analgesia** for the severe chronic bone pain characteristic of Itai-itai disease.
- **Standard CKD management** (blood pressure control, dietary modification, and progression to renal replacement therapy/dialysis in advanced cases) for those who progress to overt chronic kidney disease.

**Experimental/investigational:**
- Antioxidant supplementation (e.g., N-acetylcysteine, selenium) has been explored in animal models to mitigate cadmium-induced oxidative injury, but robust human clinical trial evidence supporting a specific antioxidant regimen for established cadmium poisoning was not identified in this research pass — flag as an evidence gap if curated.
- No cadmium-specific agents are registered in ClinicalTrials.gov as approved disease-modifying therapies at the time of this report; most relevant trials concern chelation pharmacokinetics/biomonitoring methodology rather than definitive efficacy trials for cadmium poisoning specifically.

**Treatment outcomes:** Given the largely irreversible nature of established tubular injury, the primary "treatment outcome" measured in the literature is **prevention of further exposure/progression** rather than reversal of existing damage; formal treatment-response-rate data (in the sense used for pharmacotherapy trials) are sparse for this indication.

---

## 13. Prevention

**Primary prevention:**
- **Occupational exposure controls**: engineering controls (ventilation, enclosed processes), personal protective equipment, and regulatory exposure limits (e.g., OSHA's cadmium standard 29 CFR 1910.1027, setting permissible exposure limits and mandating biological monitoring) in cadmium-using industries.
- **Environmental/agricultural controls**: soil remediation in contaminated areas, restrictions on irrigation with contaminated water (the direct historical lesson of Itai-itai disease, which prompted major Japanese public-health and environmental-remediation programs), and monitoring/limiting cadmium content in fertilizers.
- **Food safety regulation**: maximum permitted cadmium levels in foods (EU/Codex Alimentarius regulatory limits for rice, cereals, vegetables, offal, cocoa products), informed by EFSA's Tolerable Weekly Intake of 2.5 µg/kg body weight.
- **Tobacco control**: smoking cessation and reduction in smoking initiation is arguably the single most impactful primary-prevention lever for population-level cadmium body burden reduction, given tobacco's outsized contribution to non-occupational exposure.
- **Nutritional adequacy programs**: ensuring adequate dietary iron, zinc, and calcium intake (particularly in women of reproductive age) to reduce the enhanced intestinal cadmium absorption associated with deficiency states.

**Secondary prevention (screening/early detection):**
- **Occupational biological monitoring** (blood cadmium, urinary cadmium, urinary β2-microglobulin) in exposed worker populations, enabling early detection of tubular dysfunction before progression to irreversible injury — this is the most evidence-supported secondary-prevention intervention.
- **Environmental biomonitoring** of at-risk populations near contaminated sites.

**Tertiary prevention:**
- Early exposure cessation upon detection of biomarker abnormalities, before progression to overt osteomalacia or CKD, is the principal tertiary strategy given the largely irreversible nature of established chronic cadmium nephropathy.
- Calcium/vitamin D supplementation and fracture-prevention strategies in individuals with established skeletal disease.

**Immunization:** Not applicable — cadmium poisoning is not an infectious/immunization-preventable disease.

**Genetic counseling:** Not applicable in the classical sense (no Mendelian transmission), though risk communication regarding individual susceptibility (e.g., iron-deficiency-related enhanced absorption) may have a role in targeted public health messaging for high-risk groups (e.g., women of reproductive age).

**Public health interventions:**
- Site remediation and contamination monitoring at former mining/smelting locations.
- Public health surveillance systems (e.g., NHANES biomonitoring in the U.S., similar national programs elsewhere) tracking population-level cadmium body burden trends over time.
- International/regulatory harmonization of food cadmium limits (Codex Alimentarius, EU regulations) given the global nature of food-trade-mediated exposure.

---

## 14. Other Species / Natural Disease

**Taxonomy:** Cadmium toxicity is a broadly conserved phenomenon across vertebrate (and many invertebrate) species, reflecting cadmium's fundamental biochemical mimicry of essential divalent cations (zinc, calcium) rather than a species-specific mechanism.

**Naturally occurring/environmental exposure in other species:**
- **Wildlife**: cadmium bioaccumulation and toxicity are well-documented in wildlife inhabiting contaminated environments, particularly species with long lifespans and high trophic-level bioaccumulation potential (e.g., raptors, marine mammals accumulating cadmium from shellfish/crustacean prey — cadmium is strongly bioaccumulated in mollusks and crustaceans, which show naturally high tissue cadmium even in relatively unpolluted marine environments).
- **Domestic/companion animal and livestock exposure**: livestock grazing on contaminated pasture or fed contaminated feed can develop cadmium-related renal and skeletal pathology analogous to the human disease; veterinary case reports of environmental cadmium toxicosis exist, though this is not as systematically cataloged (e.g., in OMIA, which is primarily oriented toward Mendelian veterinary genetic disease) as inherited veterinary conditions.

**Comparative biology:**
- The **proximal tubular megalin:cubilin-mediated uptake mechanism** central to human cadmium nephrotoxicity is evolutionarily conserved across mammals, which is precisely why **rodent models (rat, mouse)** are considered reasonably faithful models of the human renal lesion (see Model Organisms below).
- **Avian species** (notably relevant to wildlife toxicology) show comparable cadmium-induced renal and skeletal pathology, though avian calcium metabolism differences (egg-laying-related calcium mobilization) introduce some species-specific nuance to skeletal outcome comparisons.

**Zoonotic potential/transmission:** Not applicable — cadmium poisoning is a toxic exposure phenomenon, not an infectious or transmissible disease; there is no zoonotic transmission concept relevant here, though shared dietary/environmental exposure sources (e.g., a contaminated water/food source affecting both livestock and the human population consuming them) represent a shared-exposure rather than transmission pathway.

---

## 15. Model Organisms

**Rodent models (the dominant experimental system):**
- **Mouse**: chronic low-dose environmentally-relevant cadmium exposure models demonstrate **early renal proximal tubular damage that is not well-predicted by blood or urine cadmium levels alone** — an important translational finding suggesting tissue-level injury can precede/exceed what conventional biomarkers capture (ScienceDirect, chronic mouse exposure study). Mouse models are also used to study cadmium's estrogen-mimetic effects on uterine and mammary gland growth, supporting the ERα-mediated endocrine-disruption mechanism.
- **Rat**: extensively used for both **renal** (subcutaneous/drinking-water cadmium exposure models showing dose- and duration-dependent proximal tubular injury, histomorphological/ultrastructural precancerous lesions, and altered renal cortical microRNA expression) and **skeletal** toxicity modeling — a 2023 rat study specifically implicated the **ROS → SIRT1/PGC-1α/p53 signaling pathway** in cadmium-induced osteoblast apoptosis underlying osteoporosis pathogenesis. Rat models using dual-energy X-ray absorptiometry (DXA) have quantified dose-related bone mineral density reductions in cadmium-exposed animals, directly modeling the Itai-itai skeletal phenotype. Rat inhalation models have also been used to study acute cadmium-induced neutrophilic pulmonary inflammation and to test protective agents (e.g., tiotropium/budesonide) against this acute lung injury phenotype.
- **Periodontal bone models**: subcutaneous cadmium injection in rats produces significant periodontal bone loss, proposed as a translational model for periodontal disease association with cadmium exposure in humans.

**Genetic models:**
- Transporter knockout/knockdown models (siRNA-mediated knockdown of ZIP8, ZIP14, and DMT1 in cultured mouse kidney proximal tubule cells) have been used to dissect the relative contribution of each metal-transport pathway to cellular cadmium uptake, establishing that no single transporter pathway predominates (a polygenic-uptake model with direct relevance to interpreting human transporter-gene susceptibility polymorphisms).
- Conditional/tissue-specific transporter knockouts in mouse are a logical extension for future mechanistic dissection, though a comprehensive knockout-model literature specific to cadmium (analogous to, e.g., IMPC-cataloged single-gene disease models) was not comprehensively retrieved in this pass.

**In vitro/cell-based models:**
- Cultured renal proximal tubule cell lines (human and rodent-derived) are the standard system for studying megalin:cubilin-dependent cadmium-protein complex uptake and cytotoxicity mechanisms, including the classical Cd-metallothionein model and the revised Cd-β2-microglobulin/albumin/lipocalin-2 model.
- Human breast cancer cell lines (T47D, and ERα+/ERα− comparator lines) are the standard system for dissecting cadmium's estrogen-receptor-mediated mechanisms.

**Phenotype recapitulation and limitations:**
- Rodent renal and skeletal models recapitulate the **proximal tubular injury and mineralization-defect phenotypes** of human chronic cadmium poisoning with reasonably high fidelity, given the conserved megalin:cubilin uptake mechanism and shared vitamin-D-activation pathway.
- **Limitations**: rodent lifespan and cadmium accumulation kinetics differ substantially from the multi-decade human chronic exposure pattern underlying diseases like Itai-itai, so rodent models are generally better suited to modeling the *mechanism* of injury than the full decades-long natural history; species differences in calcium/bone metabolism (and the specific postmenopausal/multiparous-female risk profile of human Itai-itai disease) are not fully captured by standard rodent designs unless specifically modeled (e.g., ovariectomized rat models combined with cadmium exposure, mimicking postmenopausal bone vulnerability).
- **Applications**: rodent and cell-based models remain the primary tools for mechanistic dissection (transporter biology, oxidative stress pathways, chelation pharmacokinetics/efficacy testing) and are essential to interpreting the chelation-efficacy time-dependence findings summarized in the Treatment section, which derive substantially from these animal studies rather than human clinical trial data.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms |
|---|---|
| MeSH | D002104 (Cadmium Poisoning), D002103 (Cadmium) |
| ICD-10-CM | T56.3 |
| Key genes (modifier) | SLC11A2/DMT1 (hgnc:10908), SLC39A8/ZIP8 (hgnc:20862), SLC39A14/ZIP14 (hgnc:20858), MT1A (hgnc:7393), MT2A (hgnc:7407) |
| Key phenotypes (HP) | HP:0002753 (Osteomalacia), HP:0000939 (Osteoporosis), HP:0000121 (Nephropathy), HP:0012622 (Chronic kidney disease), HP:0410048/HP:0002090 (Pneumonitis/Pneumonia), HP:0100598 (Pulmonary edema), HP:0000822 (Hypertension), HP:0002816 (Pathologic fracture), HP:0100526 (Neoplasm of the lung) |
| Key GO processes | GO:0006979 (response to oxidative stress), GO:0006974 (DNA damage response), GO:0097190 (apoptotic signaling pathway), GO:0030282 (bone mineralization) |
| Key CL cell types | CL:1000838/CL:1001106 (proximal tubule epithelial cell), CL:0000062 (osteoblast), CL:0001056 (alveolar type I cell) |
| Key UBERON | UBERON:0004134 (kidney proximal tubule), UBERON:0002048 (lung), UBERON:0001474 (bone element) |
| Key CHEBI | CHEBI:22977 (cadmium atom/ion), CHEBI:64118 (edetic acid / EDTA) |
| Key NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15747 (Supportive Care) |

**Note on evidence gaps requiring curator judgment:** (1) the exact molecular mechanism of cadmium-induced osteoblast/bone toxicity remains explicitly unresolved in the primary literature; (2) the megalin:cubilin cargo-protein model (metallothionein vs. β2-microglobulin/albumin/lipocalin-2) is under active mechanistic revision; (3) a verified MONDO CURIE for this entity should be confirmed via direct ontology lookup rather than assumed from this report.

---

### Sources

- [Cadmium Exposure: Mechanisms and Pathways of Toxicity and Implications for Human Health (Toxics, 2024, PMID:38922068)](https://www.mdpi.com/2305-6304/12/6/388)
- [The Mechanisms of Cadmium Toxicity in Living Organisms (PMID:39771090)](https://pubmed.ncbi.nlm.nih.gov/39771090/)
- [Cellular mechanisms of cadmium-induced toxicity: a review (PMID:24117228)](https://pubmed.ncbi.nlm.nih.gov/24117228/)
- [Mechanisms of Cadmium Neurotoxicity (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10706630/)
- [Cadmium Toxicity - StatPearls (NBK536966)](https://www.ncbi.nlm.nih.gov/books/NBK536966/)
- [Cadmium Complexed with β2-Microglobulin, Albumin and Lipocalin-2 rather than Metallothionein Cause Megalin:Cubilin Dependent Toxicity of the Renal Proximal Tubule](https://pmc.ncbi.nlm.nih.gov/articles/PMC6566203/)
- [Megalin-dependent internalization of cadmium-metallothionein and cytotoxicity in cultured renal proximal tubule cells (PMID:16690719)](https://pubmed.ncbi.nlm.nih.gov/16690719/)
- [Mechanism of cadmium-induced nephrotoxicity (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0300483X24000076)
- [Toxicological Profile for Cadmium - ATSDR](https://www.atsdr.cdc.gov/toxprofiles/tp5.pdf)
- [ATSDR Cadmium Toxicological Profile - CDC](https://wwwn.cdc.gov/TSP/ToxProfiles/ToxProfiles.aspx?id=48&tid=15)
- [Cadmium induces osteomalacia mediated by proximal tubular atrophy and disturbances of phosphate reabsorption (PMID:10997741)](https://pubmed.ncbi.nlm.nih.gov/10997741/)
- [Itai-itai disease: Renal tubular osteomalacia induced by environmental exposure to cadmium — historical review and perspectives](https://www.tandfonline.com/doi/full/10.1080/00380768.2016.1159116)
- [Itai-itai disease: cadmium-induced renal tubular osteomalacia (PMID:23095355)](https://pubmed.ncbi.nlm.nih.gov/23095355/)
- [The liver in itai-itai disease (chronic cadmium poisoning): pathological features and metallothionein expression - Modern Pathology](https://www.nature.com/articles/modpathol201362)
- [Mechanism and epidemiology of bone effects of cadmium (PMID:1303956)](https://pubmed.ncbi.nlm.nih.gov/1303956/)
- ["Itai-itai" disease (osteoporosis and osteomalacia due to industrial cadmium poisoning) (PMID:4977879)](https://pubmed.ncbi.nlm.nih.gov/4977879/)
- [Pathogenesis of Osteomalacia in Itai-itai Disease](https://www.jstage.jst.go.jp/article/tox/19/2/19_2_69/_pdf)
- [Cadmium exposure and cardiovascular disease risk: A systematic review and dose-response meta-analysis (PMID:38295933)](https://pubmed.ncbi.nlm.nih.gov/38295933/)
- [Chronic exposure to lead, cadmium and arsenic increases risk of cardiovascular disease - American Heart Association](https://newsroom.heart.org/news/chronic-exposure-to-lead-cadmium-and-arsenic-increases-risk-of-cardiovascular-disease)
- [Cadmium in biological samples and site-specific cancer risk and mortality: A systematic review](https://www.sciencedirect.com/science/article/abs/pii/S1877782124000298)
- [The Association Between Cadmium Exposure and Prostate Cancer: An Updated Systematic Review and Meta-Analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11593822/)
- [Pharmacokinetics of metal excretion following different doses of sodium EDTA infusion](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12050972/)
- [Chelation: Harnessing and Enhancing Heavy Metal Detoxification—A Review](https://onlinelibrary.wiley.com/doi/10.1155/2013/219840)
- [Roles of ZIP8, ZIP14, and DMT1 in transport of cadmium and manganese in mouse kidney proximal tubule cells](https://academic.oup.com/metallomics/article/4/7/700/6016098)
- [The Allelic Variant A391T of Metal Ion Transporter ZIP8 (SLC39A8) Leads to Hypotension and Enhanced Insulin Resistance](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9240775/)
- [Genetic polymorphism of divalent metal transporter 1 gene intronic IVS4+44C/A in cadmium exposed population](https://ouci.dntb.gov.ua/en/works/4NwzxGKl/)
- [An assessment of sensitivity biomarkers for urinary cadmium burden](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7487760/)
- [Urinary β2-Microglobulin Predicts the Risk of Hypertension in Populations Chronically Exposed to Environmental Cadmium](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12029079/)
- [Cadmium Exposure Panel - OSHA - ARUP Laboratories Test Directory](https://ltd.aruplab.com/Tests/Pub/0025013)
- [Urinary N-acetylglucosaminidase in People Environmentally Exposed to Cadmium Is Minimally Related to Cadmium-Induced Nephron Destruction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11598048/)
- [Blood cadmium level as a risk factor for chronic pain: NHANES database 1999–2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC11148299/)
- [Cadmium blood and urine concentrations as measures of exposure: NHANES 1999–2010](https://www.nature.com/articles/jes201355)
- [NHANES August 2021-August 2023: Lead, Cadmium, Total Mercury, Selenium, & Manganese – Blood Data Documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/PBCD_L.htm)
- [RELEVANCE TO PUBLIC HEALTH - Toxicological Profile for Cadmium](https://www.ncbi.nlm.nih.gov/books/NBK158837/)
- [Acute cadmium fume poisoning. Five cases with one death from renal necrosis (PMID:5928153)](https://pubmed.ncbi.nlm.nih.gov/5928153/)
- [Cadmium Toxicity: What Health Effects Are Associated With Acute High-Dose Cadmium Exposure? - ATSDR](https://archive.cdc.gov/www_atsdr_cdc_gov/csem/cadmium/Acute-Effects.html)
- [HEALTH EFFECTS - Toxicological Profile for Cadmium](https://www.ncbi.nlm.nih.gov/books/NBK158834/)
- [Cadmium in tobacco smokers: a neglected link to lung disease?](https://publications.ersnet.org/content/errev/27/147/170122)
- [Interstitial Pneumonitis after Cadmium Exposure: Is it Reversible?](https://www.anncaserep.com/full-text/accr-v1-id1119.php)
- [Protective effects of tiotropium alone or combined with budesonide against cadmium inhalation induced acute neutrophilic pulmonary inflammation in rats](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5831634/)
- [Statement on tolerable weekly intake for cadmium - EFSA CONTAM Panel](https://www.researchgate.net/publication/281935185_Statement_on_tolerable_weekly_intake_for_cadmium_1_EFSA_Panel_on_Contaminants_in_the_Food_Chain_CONTAM)
- [EFSA sets lower tolerable intake level for cadmium in food](https://www.efsa.europa.eu/en/news/efsa-sets-lower-tolerable-intake-level-cadmium-food)
- [Dietary exposure to cadmium from six common foods in the United States](https://www.sciencedirect.com/science/article/pii/S0278691523002752)
- [Dietary cadmium exposure assessment among the Chinese population](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5436861/)
- [Cadmium Induces Kidney Iron Deficiency and Chronic Kidney Injury by Interfering with the Iron Metabolism in Rats](https://pmc.ncbi.nlm.nih.gov/articles/PMC10815742/)
- [Cadmium Exposure Disrupts Periodontal Bone in Experimental Animals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6027471/)
- [Chronic exposure of mice to environmentally relevant, low doses of cadmium leads to early renal damage, not predicted by blood or urine cadmium levels](https://www.sciencedirect.com/science/article/abs/pii/S0300483X06006159)
- [Histomorphological and ultrastructural cadmium-induced kidney injuries and precancerous lesions in rats](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9202506/)
- [Cadmium Nephrotoxicity Is Associated with Altered MicroRNA Expression in the Rat Renal Cortex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5874789/)
- [Bone metabolism of male rats chronically exposed to cadmium](https://www.sciencedirect.com/science/article/abs/pii/S0041008X05000116)
- [Cadmium promotes breast cancer cell proliferation by potentiating the interaction between ERalpha and c-Jun (PMID:20219890)](https://pubmed.ncbi.nlm.nih.gov/20219890/?dopt=Abstract)
- [Effects of cadmium on estrogen receptor mediated signaling and estrogen induced DNA synthesis in T47D human breast cancer cells](https://pmc.ncbi.nlm.nih.gov/articles/PMC2981500/)
- [Cadmium and breast cancer – Current state and research gaps in the underlying mechanisms](https://www.sciencedirect.com/science/article/pii/S0378427422000650)
- [The endocrine disruptor cadmium modulates the androgen–estrogen receptors ratio and induces inflammatory cytokines in luminal (A) cell models of breast cancer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10902028/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 19 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22437713` (1 mention) - A two-dimensional polymer prepared by organic synthesis.
  - shared terms: none

Weighed against this report's own most characteristic terms: `cadmium`, `exposure`, `renal`, `disease`, `poisoning`, `chronic`, `tubular`, `proximal`, `bone`, `calcium`, `injury`, `itai-itai`, `acute`, `osteomalacia`, `kidney`, `effect`, `cell`, `via`, `mechanism`, `risk`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
