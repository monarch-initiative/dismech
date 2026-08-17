---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-17T15:42:04.720131'
end_time: '2026-08-17T15:46:55.217769'
duration_seconds: 290.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Embryonal Carcinoma
  mondo_id: ''
  category: ''
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
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.9481344999999999
  session_id: c8dd5cfe-f073-50fe-bd25-fe890bfcd83c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 56
reference_validation:
  total_references: 26
  verified: 25
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.038
  quotes_checked: 1
  quotes_valid: 0
  unresolved_references:
  - DOI:10.3390/ijms222111774](https://doi.org/10.3390/ijms222111774
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Embryonal Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Embryonal Carcinoma** covering all of the
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

# Embryonal Carcinoma: Comprehensive Research Report

## 1. Disease Information

**Overview.** Embryonal carcinoma (EC) is a highly malignant, primitive/pluripotent germ cell tumor composed of large, undifferentiated cells that morphologically and biologically recapitulate the epiblast/inner cell mass of the pre-implantation embryo. It is classified as a **type II ("malignant") germ cell tumor (GCT)** and is the prototypical, most aggressive component of **nonseminomatous germ cell tumors (NSGCTs)**. EC most commonly arises in the testis (young to middle-aged men, peak incidence ~25 years), but can also occur in the ovary and at extragonadal midline sites (mediastinum, retroperitoneum, sacrococcygeal region, pineal/suprasellar CNS). EC is characterized histologically by large germ cells with abundant cytoplasm resembling primitive epithelial cells, geographic necrosis, high mitotic activity, and pseudoglandular/pseudopapillary architecture ([Malacards](https://www.malacards.org/card/embryonal_carcinoma); [NORD/MONDO](https://rarediseases.org/mondo-disease/embryonal-carcinoma/)). It most often develops in young/middle-aged men, grows rapidly, and tends to metastasize outside the testis before diagnosis, more so than pure seminoma ([GARD](https://rarediseases.info.nih.gov/diseases/5140/embryonal-carcinoma)).

**Key identifiers:**
- **MONDO:** MONDO:0005440 (embryonal carcinoma); related umbrella term **testicular germ cell tumor** OMIM #273300 / MONDO:0010108 ([OMIM](https://www.omim.org/entry/273300))
- **Orphanet:** ORPHA:180226 (embryonal carcinoma, testis-specific); related codes ORPHA:363483, 363494 (non-seminomatous GCT of testis), 363504, 842, 876, 99865 ([Orphanet](https://www.orpha.net/en/disease/detail/180226))
- **ICD-O-3 morphology:** 9070/3 (Embryonal carcinoma, NOS)
- **ICD-10-CM:** C62.- (Malignant neoplasm of testis), site-modified (C62.0 undescended, C62.1 descended, C62.9 unspecified)
- **MeSH:** Carcinoma, Embryonal (D018236)
- Synonyms: Embryonal cell carcinoma; malignant teratoma, undifferentiated; adult-type teratocarcinoma component

**Data source type:** Overwhelmingly aggregated disease-level literature (case series, cohort/registry studies such as SEER and national cancer registries, molecular-pathology reviews, GWAS) rather than individual EHR records, reflecting the disease's rarity and its predominant characterization through oncology registries and pathology consortia.

---

## 2. Etiology

**Primary causal mechanism.** EC arises from a common precursor lesion, **germ cell neoplasia in situ (GCNIS)**, an intratubular malignant transformation of fetal-type gonocytes that fail to differentiate into mature spermatogonia due to a functional insufficiency of the somatic testicular niche during fetal development ([Fichtner et al. 2024, Histopathology](https://onlinelibrary.wiley.com/doi/full/10.1111/his.15249)). GCNIS is the shared precursor for all "type II" GCTs (seminoma, embryonal carcinoma, choriocarcinoma, yolk-sac tumor, postpubertal-type teratoma). If untreated, GCNIS progresses to invasive GCT with a **~70% risk at 7 years**. GCNIS is found adjacent to invasive tumor in 72–98% of cases and in the contralateral testis in 4.9–6.6% of cases.

**Disease causal factors** — genetic, mechanistic:
- **Isochromosome 12p [i(12p)]** or gain of 12p material is the hallmark, near-universal chromosomal alteration of invasive type II GCTs, present in >80% of cases across histologic subtypes, and its acquisition marks the transition from in-situ GCNIS to invasive tumor ([Atlas Genetics Oncology](https://atlasgeneticsoncology.org/solid-tumor/5005/testis-germ-cell-tumors); [Fichtner et al. 2021, Histopathology](https://onlinelibrary.wiley.com/doi/10.1111/his.14258)).
- **KIT/KITLG pathway activation**: driver mutations affecting the KIT receptor tyrosine kinase and downstream signaling are important, though somatic KIT mutations are enriched in the seminoma component (~22% of seminoma-containing samples) more than pure embryonal carcinoma.
- **TP53** is generally wild-type in treatment-naive GCTs (mutated in only ~11.2% of NSGCT samples), which is mechanistically linked to chemosensitivity (see Section 6). TP53 mutation/MDM2 amplification is instead associated with **somatic-type malignant transformation** and acquired cisplatin resistance.
- **PTEN loss** is common specifically in the embryonal carcinoma component (loss of expression in ~86% of EC), and **loss of 3q27–q28** is consistently detected in EC components ([Atlas Genetics Oncology, PMC12700052](https://pmc.ncbi.nlm.nih.gov/articles/PMC12700052/)).

**Genetic risk factors:**
- **GWAS-identified common susceptibility loci** (all TGCT, not EC-specific): **KITLG** (12p22) — the strongest known common TGCT risk locus, conferring up to ~3-fold risk per allele at rs3782179/rs4474514 (Kanetsky et al. 2009, *Nat Genet* 41:811–815, [PMID cited via Nature Genetics](https://www.nature.com/articles/ng.393)); **SPRY4** (5q31.3, rs4324715/rs6897876, ~1.4-fold risk per allele); **BAK1**, **DMRT1**, **GAB2**, and at least 22 additional susceptibility loci identified in expanded GWAS meta-analyses ([Nature Communications 2021](https://www.nature.com/articles/s41467-021-24334-y)). These genes converge on **KIT/KITLG signaling**, which is essential for primordial germ cell (PGC) migration and survival.
- **CHEK2** is the only moderate-penetrance gene with pathogenic variants associated with TGCT risk identified to date; overall heritability of TGCT is estimated at **37–49%** based on twin/family studies, with an **8–10-fold increased risk in siblings** and **4–6-fold in father-son** relationships — among the highest familial relative risks of any solid tumor ([PMC Frontiers Endocrinology 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6626920/); [PMC4815881](https://pmc.ncbi.nlm.nih.gov/articles/PMC4815881/)).
- **Klinefelter syndrome (47,XXY)** is a well-established, strong risk factor specifically for **extragonadal mediastinal** NSGCT/embryonal carcinoma — reported in up to 20% of mediastinal NSGCT series ([PMC7526209](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7526209/)).

**Environmental/non-genetic risk factors:**
- **Cryptorchidism (undescended testis)** — one of the strongest and most consistent risk factors, thought to share a common developmental etiology with TGCT under the **Testicular Dysgenesis Syndrome (TDS)** hypothesis, which links cryptorchidism, hypospadias, impaired spermatogenesis, and TGCT to a common in-utero origin ([PMC7822361](https://pmc.ncbi.nlm.nih.gov/articles/PMC7822361/); [PMC1892638](https://pmc.ncbi.nlm.nih.gov/articles/PMC1892638/)).
- In-utero exposure to **estrogenic or anti-androgenic environmental disruptors**, disorders of androgen receptor expression, and placental abnormalities have been proposed as contributing environmental exposures during fetal gonadal development ([PMC12841294](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12841294/)).
- Age (peak 15–35 years), personal history of contralateral GCT/GCNIS, and family history of TGCT.

**Protective factors:** No well-established genetic or environmental protective factors are documented in the literature specific to embryonal carcinoma; this remains a data gap.

**Gene-environment interactions:** The prevailing model (TDS hypothesis) posits that environmental endocrine-disrupting exposures act during a critical fetal developmental window in genetically predisposed individuals (carrying KITLG/SPRY4/BAK1/DMRT1 risk alleles) to impair gonocyte-to-spermatogonium differentiation, producing the GCNIS precursor.

**Suggested ontology terms:** MONDO:0005440 (embryonal carcinoma); HP:0100615 (Male germ cell neoplasia — for cryptorchidism-associated risk, see HP:0000028 Cryptorchidism); GENO/HGNC: KITLG (HGNC:6343), SPRY4 (HGNC:15533), BAK1 (HGNC:949), DMRT1 (HGNC:2933), CHEK2 (HGNC:16627), KIT (HGNC:6342), TP53 (HGNC:11998), PTEN (HGNC:9588).

---

## 3. Phenotypes

**Primary presenting phenotype (clinical sign):** A **painless testicular mass/swelling** is the classic presentation. HPO: **HP:0100615** (Neoplasm of the testis) or more specifically a testicular mass finding; ~10–20% of patients report acute testicular pain from hemorrhage/infarction within the tumor, and embryonal carcinoma in particular is prone to intratumoral hemorrhage.

- **Onset:** Age of onset for pure embryonal carcinoma peaks in young adulthood; it is the predominant histology up to age ~35, after which pure seminoma becomes more common (up to age 75). In very young boys (0–4 years, SEER 1973-2004 data), only 17% of nonseminomas were embryonal carcinoma (yolk sac tumor, 67%, predominates in this age group; teratoma, 13%) ([PMC3694153](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3694153/); [NCBI Bookshelf NBK585983](https://www.ncbi.nlm.nih.gov/books/NBK585983/)).
- **Severity/progression:** EC is the most aggressive NSGCT histologic component. Embryonal carcinoma predominance (>50% of tumor volume) and lymphovascular invasion in the orchiectomy specimen are independent predictors of occult metastatic (retroperitoneal) disease and of relapse on surveillance, and drive the use of adjuvant chemotherapy in clinical stage I disease.
- **Metastatic phenotypes** at presentation may include: back/flank pain (retroperitoneal lymphadenopathy), dyspnea/cough/hemoptysis (pulmonary metastases), neurologic symptoms (rare CNS metastases), gynecomastia (from hCG-driven estrogen production).

**Laboratory abnormalities (biomarker phenotypes):**
- **Elevated serum AFP (alpha-fetoprotein)** — produced by the yolk-sac component when present; pure EC alone can show modest AFP elevation (immunohistochemically demonstrated within mononuclear EC cells), typically lower magnitude than yolk sac tumor.
- **Elevated serum β-hCG (human chorionic gonadotropin)** — EC (like choriocarcinoma) can produce β-hCG via syncytiotrophoblastic giant cells; <10% of pure seminomas also produce low-level hCG. Half-life of β-hCG ≈ 24 hours; AFP half-life ≈ 4–6 days — clinically used to monitor treatment response ([ScienceDirect – Tumor markers review](https://www.sciencedirect.com/science/article/abs/pii/S1040842821000123)).
- **LDH (lactate dehydrogenase)** elevation is a nonspecific marker of tumor burden used in IGCCCG risk stratification.

**Quality of life impact:** Beyond the acute oncologic burden, survivors face long-term QoL issues from treatment: infertility (orchiectomy + retroperitoneal lymph node dissection risking retrograde ejaculation; cisplatin gonadotoxicity), cisplatin-related peripheral neuropathy, ototoxicity, nephrotoxicity, cardiovascular risk elevation, hypogonadism, and psychosocial distress related to young-adult cancer diagnosis and fertility preservation needs.

**Suggested HPO terms:** HP:0100615 (Neoplasm of the testis — proxy), HP:0000028 (Cryptorchidism, as an associated/risk phenotype), HP:0011014 (Abnormal blood glucose — not typical), HP:0031264 (Elevated alpha-fetoprotein — check HP mapping), general oncology phenotype terms for retroperitoneal lymphadenopathy and pulmonary nodules as metastatic sequelae.

---

## 4. Genetic/Molecular Information

**Causal/driver alterations (somatic, not classically "germline Mendelian"):**
- **Isochromosome 12p [i(12p)]**: present in >80% of type II GCTs including EC; considered the molecular signature separating invasive GCT from GCNIS. Extra copies of 12p (containing genes such as **CCND2**, **NANOG**, **KRAS**) are thought to drive proliferation and pluripotency maintenance ([ScienceDirect - Chromosome 12p overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/chromosome-12p)).
- **KIT** somatic activating mutations (exon 17, D816 hotspot) — more frequent in the seminoma component (~22%) than pure EC.
- **TP53**: predominantly wild-type in treatment-naive EC (mutated in ~11.2% of NSGCT overall); TP53 mutation and MDM2 amplification are associated with **somatic-type malignant transformation** and **cisplatin resistance** ([IJMS 2021, PMID cited via DOI 10.3390/ijms222111774](https://doi.org/10.3390/ijms222111774)).
- **PTEN**: loss of expression in ~86% of EC components — the highest among GCT histotypes — implicating PI3K/AKT pathway dysregulation.
- **Loss of chromosome 3q27–q28** consistently found in the EC component specifically.

**Functional consequences:** These alterations converge on sustaining a pluripotent, undifferentiated cell state (elevated 12p pluripotency genes), enhanced proliferative/survival signaling (KIT, PI3K/PTEN axis), and — importantly — an **intact, hypersensitized p53-apoptotic pathway** that underlies clinical cisplatin sensitivity (see Section 6).

**Epigenetic information:** EC genome-wide **DNA hypomethylation** relative to somatic tissue is a defining epigenetic feature, contrasting with seminoma. Human EC cells show extreme sensitivity to low-dose 5-aza-2′-deoxycytidine (a DNA methyltransferase inhibitor), which induces global/gene-specific promoter hypomethylation, downregulation of pluripotency genes (**NANOG, SOX2, GDF3**) and Myc target genes, DNA damage, and p53 activation — highlighting a mechanistic link between the pluripotent epigenome and drug hypersensitivity ([PMC3531428](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3531428/)). Conversely, specific tumor-suppressor gene promoters can be **hypermethylated** in testicular EC ([*Br J Cancer*, Nature](https://www.nature.com/articles/bjc2015408)).

**Molecular/transcriptional drivers of the EC phenotype:**
- **OCT4 (POU5F1)**, **NANOG**, and **SOX2** — core pluripotency transcription factor network; OCT4-SOX2 heterodimers activate the NANOG promoter, and this triad is essential to maintaining the EC stem-like state, directly paralleling embryonic stem cell (ESC) biology. OCT4 and NANOG are highly specific immunohistochemical/diagnostic markers for EC (and seminoma), distinguishing them from other GCT histotypes ([PMC3506717](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3506717/); [PMC7408284](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7408284/)).
- SOX2 in particular is implicated as an etiologic differentiator between EC and its seminoma-like precursor state, based on NCCIT/NT2 cell line studies (Gjerstorff et al., [PMC3880257](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880257/)).

**Chromosomal abnormalities:** Beyond i(12p), aneuploidy is a general feature of TGCTs; near-triploid/tetraploid karyotypes are common. In Klinefelter-associated extragonadal (mediastinal) GCT, the constitutional 47,XXY karyotype is itself the predisposing chromosomal abnormality.

**Suggested ontology terms:** HGNC genes — POU5F1/OCT4 (HGNC:9221), NANOG (HGNC:19349), SOX2 (HGNC:11195), KIT (HGNC:6342), KITLG (HGNC:6343), TP53 (HGNC:11998), PTEN (HGNC:9588), MDM2 (HGNC:6973); GO terms — GO:0019827 (stem cell population maintenance), GO:0060333 (interferon-gamma-mediated signaling — n/a), GO:0006974 (DNA damage response), GO:0006306 (DNA methylation).

---

## 5. Environmental Information

- **Endocrine disruptors**: in-utero exposure to estrogenic/anti-androgenic environmental chemicals is hypothesized as a contributor to the TDS spectrum (cryptorchidism → GCNIS → TGCT), though direct causal human data for embryonal carcinoma specifically are limited to indirect epidemiologic association ([PMC12841294](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12841294/)).
- **Occupational/lifestyle exposures**: some epidemiologic studies implicate occupational exposures (e.g., certain agricultural/industrial chemical exposures) and maternal factors (e.g., diethylstilbestrol historically), though robust prospective evidence specific to EC is lacking; TGCT etiology literature (Trabert et al., [PMC3000220](https://ncbi.nlm.nih.gov/pmc/articles/PMC3000220)) reviews these broadly.
- **Infectious agents**: No established infectious causal agent for embryonal carcinoma (distinguishing it from virally-associated malignancies).
- **Radiation**: no strong evidence implicating ionizing radiation in EC etiology (unlike some other cancers), though scrotal/testicular trauma has been historically but inconsistently proposed and is not well supported.

**ECTO/exposure term suggestions:** general "exposure to endocrine-disrupting chemical" terms (not disease-specific validated associations); this remains an area with more hypothesis than confirmed causal environmental exposure data for EC specifically.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:**

1. **Fetal gonocyte developmental arrest** (in a genetically susceptible individual, e.g., carrying KITLG/SPRY4/BAK1 risk alleles) → failure of normal gonocyte-to-spermatogonium transition, often in the context of testicular dysgenesis (cryptorchidism).
2. **Germ Cell Neoplasia In Situ (GCNIS)** formation — an intratubular population of malignant, arrested primordial-germ-cell-like cells retaining a pluripotency gene expression program (OCT4/NANOG/SOX2 positive) but confined by the basement membrane.
3. **Acquisition of isochromosome 12p / 12p gain** (a "second hit" during puberty/post-puberty, hormonally influenced) → drives invasive transformation, breaching the basement membrane.
4. **Divergence along GCT lineages**: retained pluripotent, undifferentiated cells give rise to **embryonal carcinoma** (the "stem cell" of NSGCT), which can then differentiate along embryonic somatic lineages (→ teratoma) or extraembryonic lineages (→ yolk sac tumor, choriocarcinoma) — recapitulating normal early embryogenesis in a malignant context.
5. **Local growth/invasion and lymphovascular spread** — embryonal carcinoma predominance and lymphovascular invasion in the primary tumor mechanistically drive early hematogenous/lymphatic metastasis to retroperitoneal nodes, lungs, and other viscera.
6. **Clinical hypersensitivity to cisplatin-based chemotherapy** — a mechanistically distinctive downstream vulnerability: EC cells retain **wild-type TP53** with low MDM2-bound p53, producing a "hyperactive" apoptotic p53 response upon DNA damage. siRNA knockdown of TP53 abrogates cisplatin hypersensitivity, and the pro-apoptotic p53 target gene **NOXA (PMAIP1)** is central to this apoptotic response; EC cells show an inefficient/attenuated DNA damage repair response relative to somatic tumors, favoring apoptosis over repair-mediated survival (Kerst & Timmer-Bosscha review; [PMC3080918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3080918/); [Cambridge Core review](https://www.cambridge.org/core/journals/expert-reviews-in-molecular-medicine/article/unravelling-mechanisms-of-cisplatin-sensitivity-and-resistance-in-testicular-cancer/6C142D267335E17E701C0417949DB17D)). This explains both the excellent curability of EC-predominant NSGCT with BEP chemotherapy and the ominous significance of acquired TP53 mutation as a resistance mechanism at relapse.

**Molecular pathways involved:**
- **Core pluripotency network**: OCT4–SOX2–NANOG transcriptional circuit (analogous to normal ESC self-renewal machinery) — KEGG/Reactome "signaling pathways regulating pluripotency of stem cells."
- **KIT/KITLG receptor tyrosine kinase signaling** — normally governs PGC migration/survival; dysregulated in TGCT susceptibility and (in the seminoma component) via activating mutation.
- **PI3K-AKT-mTOR** — activated via frequent PTEN loss in EC.
- **p53/NOXA apoptotic axis** — central to chemosensitivity.
- **BMP/NODAL signaling** — implicated in reprogramming of seminoma-like cells toward an embryonal-carcinoma-like pluripotent state (BMP inhibition initiates NODAL-driven acquisition of pluripotency; [PMC4520454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4520454/)), illustrating within-tumor plasticity between GCT histotypes.
- **DNA methylation machinery (DNMT1/3A/3B)** — genome-wide hypomethylation maintains the pluripotent, ESC-like epigenetic state and confers unique sensitivity to demethylating agents.

**Cellular processes:** self-renewal/pluripotency maintenance, aberrant re-entry into an embryonic-like developmental program, apoptosis (p53/NOXA-driven, both constitutively and in response to genotoxic stress), cellular senescence (increasingly recognized in GCNIS and other TGCT histotypes as a barrier/facilitator of progression — [PMC11278860](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11278860/)), epithelial-like pseudoglandular differentiation.

**Cell types involved:** malignant primitive germ cells / GCNIS cells (arrested gonocyte-like cells), embryonal carcinoma tumor cells (pluripotent stem-cell-like), syncytiotrophoblast-like giant cells (hCG-producing), and — in mixed tumors — yolk sac, trophoblastic, and somatic (teratomatous) differentiated lineages.

**Suggested GO terms:** GO:0019827 (stem cell population maintenance), GO:0097191 (extrinsic apoptotic signaling pathway), GO:0006915 (apoptotic process), GO:0007283 (spermatogenesis — as the disrupted normal process), GO:0006306 (DNA methylation), GO:0007169 (transmembrane receptor protein tyrosine kinase signaling pathway — KIT).

**Suggested CL terms:** primordial germ cell, embryonal carcinoma stem cell (disease-associated), syncytiotrophoblast cell, spermatogonium (as the normal comparator lineage).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary site**: testis (most common, UBERON:0000473) — arising within the seminiferous tubules.
- **Extragonadal primary sites**: mediastinum (anterior, most common extragonadal site, 50–70% of extragonadal cases), retroperitoneum, sacrococcygeal region, pineal gland/suprasellar region (CNS germ cell tumors) — reflecting the migratory path of primordial germ cells during embryogenesis and their occasional mislocalization at midline sites.
- **Secondary/metastatic organ involvement**: retroperitoneal (para-aortic/paracaval) lymph nodes (most common first metastatic site for testicular primaries), lungs, liver, brain, bone (less common), supraclavicular/mediastinal nodes in advanced disease.
- **Body systems involved**: reproductive system (primary), lymphatic system (nodal spread), respiratory system (pulmonary metastasis), hepatic system, CNS (metastasis or primary extragonadal site).

**Tissue and cell level:**
- Seminiferous tubule epithelium / germinal epithelium (site of GCNIS and tumor origin).
- Tumor architecture: solid sheets, pseudoglandular, and pseudopapillary structures of large epithelioid cells with vesicular nuclei, prominent nucleoli, indistinct cell borders, geographic necrosis, and high mitotic index.

**Subcellular level:**
- Nuclear pluripotency transcription factor localization (OCT4, NANOG, SOX2 — nuclear staining pattern used diagnostically).
- Cytoplasmic AFP in mononuclear EC cells (when yolk-sac differentiation present); hCG in syncytiotrophoblastic elements.

**Localization:** Testicular EC is typically unilateral; bilateral synchronous or metachronous GCT (including EC) occurs in a small minority, often associated with cryptorchidism or contralateral GCNIS.

**Suggested UBERON terms:** UBERON:0000473 (testis), UBERON:0000341 (mediastinum), UBERON:0002367 (prostate — n/a), UBERON:0002435 (striatum — n/a), UBERON:0001350 (coccygeal region), UBERON:0002037 (cerebellum — n/a; use UBERON:0002020 pineal gland for CNS primaries), UBERON:0002391 (retroperitoneal space).

---

## 8. Temporal Development

**Onset:** Testicular EC typically presents in the **15–35 year age range** (peak ~25 years for nonseminoma overall), earlier on average than pure seminoma (peak ~35 years). Pure EC in prepubertal children is rare — yolk sac tumor dominates the 0–4 year nonseminoma group. Onset is generally **subacute**, presenting as a gradually enlarging, painless testicular mass over weeks to a few months, though acute presentation with pain from intratumoral hemorrhage/infarction can occur given EC's propensity for necrosis and hemorrhage.

**Progression:**
- **Disease course**: EC-predominant tumors are biologically aggressive, with high rates of lymphovascular invasion and early micrometastatic spread even in "clinical stage I" (testis-confined) disease — a key reason embryonal-carcinoma-predominance and lymphovascular invasion are used as risk stratifiers for occult metastatic disease and for choosing surveillance versus adjuvant therapy.
- **Staging (AJCC/TNM/S)**: Testicular cancer staging uniquely incorporates serum tumor markers into a combined **TNMS** system (no formal Stage IV). Stage I = testis-confined; Stage II = retroperitoneal/para-aortic nodal spread; Stage III = spread beyond retroperitoneal nodes (visceral/distant) — IIIC being the most advanced substage ([Merck Manual Professional](https://www.merckmanuals.com/professional/multimedia/table/ajcctnm-staging-of-testicular-cancer); [CAP protocol](https://documents.cap.org/protocols/cp-testis-17protocol-4010.pdf)).
- **Progression rate**: rapid without treatment; with modern platinum-based chemotherapy the disease is often curable even at advanced stage, contrasting sharply with most other rapidly progressive solid tumors.
- **Growing Teratoma Syndrome (GTS)**: a distinctive post-chemotherapy pattern in which residual/metastatic masses enlarge on treatment despite normalizing tumor markers, due to selective survival/growth of chemoresistant mature teratoma elements — requiring surgical resection rather than further chemotherapy.
- **Somatic-type malignant transformation**: rare (2.7–8.6% of GCTs with residual teratoma) but clinically important late event in which a teratoma component (which may have arisen from a totipotent EC cell) transforms into a non-germ-cell malignancy (most often sarcoma, especially rhabdomyosarcoma; also adenocarcinoma, PNET/Ewing sarcoma, or leukemia) — this transformed component is characteristically **chemoresistant** and requires surgical excision ([ScienceDirect review](https://www.sciencedirect.com/science/article/abs/pii/S030228380601311X)).

**Critical periods:** Fetal gonadal development (window of TDS-related susceptibility) and puberty (hormonal trigger for GCNIS-to-invasive transformation) represent the two key developmental windows implicated in pathogenesis.

**Remission/relapse patterns:** The great majority of relapses occur within the first 2 years post-treatment; "late relapse" (>2 years, sometimes decades later) is uncommon but recognized, often associated with teratomatous or somatically transformed elements that are relatively chemoresistant, and carries a worse prognosis, typically requiring surgical salvage.

---

## 9. Inheritance and Population

**Epidemiology:**
- Testicular GCT overall: major incidence peak ages 15–35; ~84% of TGCTs occur in men 15–44 years; ~15% in men ≥45; ~1% in boys <15 years ([NCBI Bookshelf NBK585983](https://www.ncbi.nlm.nih.gov/books/NBK585983/)).
- Histologic composition: ~55% classic seminoma, ~44% nonseminoma (embryonal carcinoma, yolk sac tumor, choriocarcinoma, teratoma, often mixed), ~1% spermatocytic tumor.
- Embryonal carcinoma is the **predominant histology up to age 35**; seminoma predominates thereafter.
- Incidence of testicular cancer (and by extension EC as a major component) has been rising in many Western countries over recent decades, with marked geographic variation — highest incidence rates in Northern Europe (notably Scandinavia) and lowest in Asia and Africa.

**Inheritance pattern:** TGCT (including EC) is **not** a classic Mendelian disease but shows **multifactorial/polygenic inheritance** with substantial heritability (37–49%) driven by common low-penetrance risk alleles (KITLG, SPRY4, BAK1, DMRT1, and ~20+ additional GWAS loci) plus rare moderate-penetrance variants (CHEK2) and environmental/developmental factors (TDS). Familial relative risk: 8–10× in brothers, 4–6× in fathers of affected men.

**Penetrance/expressivity:** Individual risk alleles are low-penetrance; disease results from cumulative polygenic risk-score burden plus environmental/developmental exposure — expressivity (histologic subtype: seminoma vs. embryonal carcinoma vs. mixed) is variable and not tightly genotype-determined.

**Population demographics:**
- **Ethnic/geographic variation**: Highest incidence in white/Caucasian populations of Northern European descent; substantially lower incidence in Black and Asian populations, a disparity only partially explained by known genetic risk loci.
- **Sex ratio**: essentially exclusive to males for testicular EC (with rare ovarian and extragonadal counterparts in both sexes).
- **Age distribution**: as above — young to middle-aged adult predominance, distinctly bimodal-adjacent to the older-predominant seminoma distribution.
- **Klinefelter syndrome (47,XXY)** confers markedly elevated risk specifically for extragonadal (especially mediastinal) NSGCT/EC — up to 20% of mediastinal NSGCT series have Klinefelter syndrome ([PMC7526209](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7526209/)).

**Prevalence/incidence:** Testicular cancer overall has an annual incidence of roughly 5–10 per 100,000 males in high-incidence countries (Northern Europe) with embryonal carcinoma as a component of a substantial fraction of the nonseminoma (~44%) cases; exact age-standardized incidence for "pure" embryonal carcinoma specifically is not separately tabulated in most registries (usually reported within the NSGCT category).

---

## 10. Diagnostics

**Clinical tests:**
- **Scrotal ultrasound** — first-line imaging for a palpable testicular mass; EC typically appears as a heterogeneous, hypoechoic intratesticular mass with irregular margins, often with hemorrhage/necrosis (unlike the more homogeneous appearance of seminoma).
- **Serum tumor markers**: AFP, β-hCG, and LDH are drawn at diagnosis (pre-orchiectomy) and monitored serially post-treatment per their respective half-lives (AFP 4–6 days; β-hCG 24 hours) to assess response and detect relapse ([ScienceDirect tumor marker review](https://www.sciencedirect.com/science/article/abs/pii/S1040842821000123)).
- **CT chest/abdomen/pelvis** — for staging (retroperitoneal nodal and visceral metastasis assessment); MRI or CT brain if CNS symptoms or high-risk marker elevations (e.g., very high hCG) suggest brain metastasis.
- **Histopathology / immunohistochemistry** (definitive diagnosis, post-orchiectomy or biopsy):
  - EC is **OCT3/4 positive, SALL4 positive (diffuse nuclear), SOX2 positive, CD30 positive (membranous)**, and typically **CD117/KIT negative** — the converse pattern (CD117+/CD30–) is seen in seminoma, making the **CD30/CD117 combination diagnostically discriminating** ([ResearchGate](https://www.researchgate.net/publication/11560082_CD30_and_CD117_c-kit_Used_in_Combination_Are_Useful_for_Distinguishing_Embryonal_Carcinoma_from_Seminoma)).
  - Caveat: **CD30 expression can be lost in metastatic/post-chemotherapy foci**, making **OCT3/4** the more reliable marker in that setting ([ResearchGate — OCT4 superior to CD30 post-chemo](https://www.researchgate.net/publication/7050060_OCT4_is_superior_to_CD30_in_the_diagnosis_of_metastatic_embryonal_carcinomas_after_chemotherapy)).
  - Standard diagnostic IHC panel for GCT subtyping: OCT3/4, PLAP, D2-40, SALL4, CD117, CD30 ("the core four" plus PLAP/D2-40 for seminoma).

**Genetic testing:** Not part of routine diagnostic workup for sporadic EC (no clinically actionable germline single-gene test); i(12p) FISH/cytogenetics can support diagnosis in ambiguous or metastatic-site-only presentations (e.g., confirming GCT origin of an unknown primary). Klinefelter karyotype/genetic testing (47,XXY) should be considered in males presenting with **extragonadal (mediastinal) NSGCT**, given the strong association.

**Omics-based diagnostics:** Not yet standard of care; research-level transcriptomic/epigenomic profiling (e.g., miRNA panels such as miR-371a-3p) is an emerging **liquid biopsy biomarker** for GCT (increasingly used in place of/alongside classical AFP/hCG/LDH, especially for marker-negative disease), though this is more validated for GCT broadly than for EC specifically.

**Clinical/staging criteria:** AJCC/UICC TNM(S) staging (see Section 8); College of American Pathologists (CAP) synoptic reporting protocol for testis specifies percentage of embryonal carcinoma and presence/absence of lymphovascular invasion as required, prognostically significant data elements.

**Differential diagnosis:** Seminoma, yolk sac tumor, choriocarcinoma, teratoma (each may coexist as components of a mixed GCT — over 50% of NSGCTs are histologically mixed), Sertoli/Leydig cell tumors, lymphoma (in older men), and — for extragonadal/mediastinal presentations — thymoma, lymphoma, and other mediastinal masses.

**Screening:** No population-level screening program exists for testicular cancer (including EC); self-examination is sometimes recommended for high-risk individuals (history of cryptorchidism, contralateral GCT, family history), though formal screening guideline endorsement is limited given overall low absolute incidence and excellent treatability.

**Suggested ontology terms:** LOINC panels for AFP/hCG/LDH; NCIT:C15200 (Immunohistochemistry) diagnostic procedure term.

---

## 11. Outcome/Prognosis

**Survival:** Testicular cancer overall has one of the best prognoses of any solid malignancy — **SEER 5-year overall survival ≈95.0%** across all stages, and **99.2%** for localized (testis-confined) disease ([SEER data via search summary](https://ncbi.nlm.nih.gov/pmc/articles/PMC3694153/)). Pure embryonal carcinoma, when treated, carries a slightly less favorable prognosis than mixed or teratoma-predominant NSGCT but still generally excellent outcomes, especially with modern cisplatin-based combination chemotherapy; comparative survival studies show differences by stage between pure EC and mixed GCT populations ([PMC10056449 — Survival of testicular pure embryonal carcinoma vs mixed GCT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056449/)).

**Prognostic risk stratification (IGCCCG):** The International Germ Cell Cancer Collaborative Group classification stratifies metastatic NSGCT into **good, intermediate, and poor** risk groups based on primary tumor site, presence/absence of non-pulmonary visceral metastases, and degree of AFP/hCG/LDH elevation — this remains the standard prognostic and treatment-selection tool.

**Prognostic factors specific to EC:**
- **Percentage of embryonal carcinoma** and **lymphovascular invasion** in the orchiectomy specimen are the two most important histopathologic predictors of occult (microscopic) retroperitoneal metastasis in clinical stage I NSGCT — driving risk-adapted management (surveillance vs. one cycle of adjuvant BEP vs. primary RPLND).
- **Embryonal carcinoma predominance (ECP)** is associated with higher risk of retroperitoneal/systemic relapse.
- Persistent **CD30 expression through treatment** has been proposed as having prognostic significance and as a potential therapeutic target (anti-CD30 antibody-drug conjugate strategies, e.g., brentuximab vedotin, have been explored) ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022534713041128)).

**Morbidity/complications:** Retroperitoneal/pulmonary metastasis, growing teratoma syndrome after chemotherapy, somatic-type malignant transformation of residual teratoma (2.7–8.6% of GCTs with teratoma; prognosis for the transformed component depends on resectability and histologic type), late relapse (rare, poor-prognosis subset), treatment-related morbidity (infertility, secondary malignancy risk from platinum/etoposide, cardiovascular and metabolic late effects, neuropathy, ototoxicity, nephrotoxicity).

**Quality of life / functional outcomes:** Long-term testicular cancer survivors (a large population given young age at diagnosis and high cure rates) show elevated rates of cardiovascular disease, metabolic syndrome, secondary malignancy, hypogonadism, and infertility compared to age-matched controls — an active area of survivorship research.

---

## 12. Treatment

**Surgical:**
- **Radical inguinal orchiectomy** — first-line diagnostic and therapeutic step for testicular primaries (NCIT:C15329, Surgical Procedure; more specifically orchiectomy).
- **Retroperitoneal lymph node dissection (RPLND)** — for clinical stage II disease (nodal metastasis) or for residual masses post-chemotherapy (especially to resect residual teratoma, which is chemoresistant, or viable residual EC).

**Pharmacotherapy — cytotoxic chemotherapy:**
- **BEP regimen** (Bleomycin, Etoposide, Cisplatin) — standard-of-care combination chemotherapy; 3–4 cycles for metastatic disease depending on IGCCCG risk group; **one cycle of adjuvant BEP** is used for high-risk clinical stage I NSGCT (embryonal-carcinoma-predominant and/or lymphovascular invasion positive) — shown to reduce relapse rate to ~3.2% versus ~41.7% on surveillance alone in some series ([Annals of Oncology, 15-year outcomes](https://www.annalsofoncology.org/article/S0923-7534(19)31372-9/fulltext)).
- **Intensified regimens for intermediate/poor-risk disease** (per IGCCCG): C-BOP/BEP (dose-intense alternating regimen), BOP/BEP-VIP combinations — studied in randomized trials (MRC TE23/CRUK 05/014; EORTC 30948) with modest survival benefit in poor-risk patients ([PMC2361516](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2361516/); [PMC4410298](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4410298/)).
- Salvage regimens for relapsed/refractory disease: TIP (paclitaxel, ifosfamide, cisplatin), high-dose chemotherapy with autologous stem cell rescue.

**Therapeutic agent classes:** Platinum agents (cisplatin — CHEBI:27899), topoisomerase II inhibitors (etoposide — CHEBI:4917), glycopeptide antibiotic/anti-tumor agent (bleomycin — CHEBI:22907).

**Targeted/experimental therapies:** No FDA-approved molecularly targeted therapy specific to EC exists; investigational approaches include anti-CD30 antibody-drug conjugates (brentuximab vedotin) given EC's characteristic CD30 expression, and DNA methyltransferase inhibitors (5-aza-2′-deoxycytidine/decitabine) leveraging EC's unique epigenetic hypersensitivity, though these remain preclinical/early-phase.

**Radiation therapy:** Generally **not** used for embryonal carcinoma/NSGCT (unlike pure seminoma, which is radiosensitive) due to relative radioresistance of nonseminomatous elements; chemotherapy and surgery are preferred.

**Supportive/fertility care:** Sperm banking prior to treatment (given gonadotoxic chemotherapy and potential RPLND-related ejaculatory dysfunction) is a standard component of care; nerve-sparing RPLND techniques aim to preserve antegrade ejaculation.

**Treatment algorithm summary:** Orchiectomy → risk stratification by histology (% EC, lymphovascular invasion) and stage/markers (IGCCCG) → surveillance vs. adjuvant BEP vs. RPLND for stage I; BEP chemotherapy (risk-adapted cycle number/intensity) ± post-chemo RPLND for residual masses in metastatic disease.

**Suggested NCIT terms:** NCIT:C15329 (Surgical Procedure — orchiectomy/RPLND), NCIT:C15632 (Chemotherapy), NCIT:C1613 (Cisplatin), NCIT:C1580 (Etoposide), NCIT:C450 (Bleomycin).

---

## 13. Prevention

**Primary prevention:** No established primary prevention strategy exists (etiology not modifiable in a validated way); early orchiopexy for cryptorchidism (ideally before 12–18 months of age) is recommended for its general urologic/fertility benefits and is associated with some reduction in subsequent TGCT risk, though it does not eliminate risk entirely.

**Secondary prevention (early detection):** Testicular self-examination is commonly recommended, particularly for men with known risk factors (cryptorchidism history, contralateral GCT, family history), though formal population screening is not endorsed by major guideline bodies (e.g., USPSTF) given the overall favorable prognosis even at later-stage diagnosis and low absolute population incidence.

**Genetic counseling:** Relevant primarily in the context of a strong family history (multiple affected first-degree relatives) or known CHEK2 pathogenic variant carriage, to inform surveillance intensity; not a Mendelian single-gene counseling scenario for the great majority of cases.

**Klinefelter syndrome surveillance:** Given the strong association with mediastinal extragonadal GCT, some authors advocate for awareness/vigilance (not formal screening protocols) in known Klinefelter patients.

**Public health/behavioral:** No specific validated public-health-level intervention (e.g., dietary, lifestyle) has been shown to meaningfully reduce EC/TGCT risk; general reduction of exposure to suspected endocrine-disrupting chemicals during pregnancy is a hypothesis-driven, not evidence-proven, recommendation.

---

## 14. Other Species / Natural Disease

Embryonal carcinoma as a discrete testicular malignancy entity is a predominantly **human** oncologic diagnosis; it is not commonly described as a naturally occurring spontaneous disease entity in veterinary species in the same taxonomic framework (dogs, for instance, more commonly develop Sertoli cell tumors, seminomas, and Leydig cell tumors as testicular neoplasms, with embryonal-carcinoma-type histology being rare). No OMIA (Online Mendelian Inheritance in Animals) entry specific to naturally occurring canine/feline "embryonal carcinoma" was identified in this search; this represents a genuine gap/limitation rather than a confirmed absence, and would require dedicated OMIA/veterinary pathology database review beyond the scope of this search pass.

**Comparative biology:** The pluripotency network (Oct4/Pou5f1, Nanog, Sox2) driving human EC is deeply evolutionarily conserved and is the same network exploited to generate murine and human embryonic stem cells and induced pluripotent stem cells — making EC biology historically foundational to stem cell science (see Section 15).

---

## 15. Model Organisms

**Cell line models (in vitro, human-derived):**
- **NTERA-2 clone D1 (NT2/D1)** — a pluripotent human embryonal carcinoma cell line established from a nude-mouse xenograft of the parental TERA-2 line, itself derived from a lung metastasis of a 22-year-old man's primary testicular EC. NT2/D1 differentiates into neuronal and other lineages in response to retinoic acid or hexamethylene bisacetamide (HMBA), making it a long-standing model for studying both EC biology and normal human neurodevelopment/differentiation ([ATCC CRL-1973](https://www.atcc.org/products/crl-1973); [PMC6496632](https://ncbi.nlm.nih.gov/pmc/articles/PMC6496632)).
- **NCCIT** — another widely used pluripotent human EC cell line; retains SOX2 expression even upon loss of OCT3/4 expression during differentiation in xenograft (N-NCCIT/N2-NCCIT) models, useful for dissecting the individual roles of core pluripotency factors ([search summary, xenograft literature](https://altogenlabs.com/xenograft-models/other-bladder-cervical/nt2-ntera-2-xenograft-model/)).
- **TCam-2** — a seminoma-derived cell line used comparatively; BMP-inhibition/NODAL-signaling experiments in TCam-2 demonstrate reprogramming toward an EC-like pluripotent state, informing lineage-plasticity models of GCT histogenesis ([PMC4520454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4520454/)).

**Xenograft models:** Nude mouse xenografts of NT2/NTERA-2 and NCCIT cell lines are standard in vivo models for studying EC tumor growth, differentiation induction, and drug response (e.g., chemosensitivity/epigenetic-therapy studies).

**Genetic/induced models:** No widely used germline knockout mouse model recapitulates spontaneous human testicular embryonal carcinoma directly (unlike, e.g., the classical **129/Sv mouse strain**, which has a well-known predisposition to spontaneous testicular teratomas/teratocarcinomas arising from primordial germ cells — a related but distinct historical model system foundational to GCT and embryonic stem cell research). Murine embryonal carcinoma cells (historically derived from 129-strain teratocarcinomas) were the original source material used to derive **embryonic stem (ES) cells** and remain used comparatively in reprogramming/pluripotency research (e.g., "linking incomplete reprogramming to improved pluripotency of murine EC-cell-derived pluripotent stem cells," [PMC2859941](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2859941/)).

**Model characteristics/limitations:** Human EC cell line xenografts recapitulate the pluripotent, undifferentiated phenotype and differentiation capacity (into neuronal, epithelial, and other lineages) reasonably well, and are highly informative for pluripotency-network biology and for epigenetic/cisplatin-sensitivity mechanism studies. They less well recapitulate the tumor microenvironment, immune interactions, and the full multi-lineage mixed-histology architecture (EC + yolk sac + choriocarcinoma + teratoma) typical of clinical NSGCT, and the classic 129/Sv spontaneous teratoma mouse model, while mechanistically informative for germ-cell tumorigenesis broadly, does not specifically model the human i(12p)/OCT4-NANOG-driven EC molecular signature.

**Research applications:** Differentiation biology and neurodevelopmental modeling (NT2/D1 retinoic-acid-induced neuronal differentiation is a classic human neurogenesis model), pluripotency transcription factor network dissection, DNA methylation/epigenetic-therapy mechanism studies, and cisplatin sensitivity/resistance mechanism studies (p53/NOXA apoptotic axis).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Term |
|---|---|
| MONDO | MONDO:0005440 (embryonal carcinoma); MONDO:0010108 (testicular germ cell tumor, umbrella) |
| Genes (HGNC) | POU5F1/OCT4, NANOG, SOX2, KIT, KITLG, TP53, PTEN, MDM2, CHEK2, SALL4, PMAIP1/NOXA |
| GO (biological process) | stem cell population maintenance (GO:0019827); apoptotic process (GO:0006915); DNA methylation (GO:0006306); spermatogenesis (GO:0007283, as disrupted process) |
| CL | primordial germ cell; spermatogonium; syncytiotrophoblast cell |
| UBERON | testis (UBERON:0000473); mediastinum (UBERON:0000341); retroperitoneal space (UBERON:0002391) |
| HP | Cryptorchidism (HP:0000028); Testicular neoplasm (proxy term) |
| CHEBI | cisplatin, etoposide, bleomycin, 5-aza-2′-deoxycytidine (decitabine) |
| NCIT | Surgical Procedure, Chemotherapy, Orchiectomy-related terms |

---

### Sources

- [Embryonal carcinoma | GARD](https://rarediseases.info.nih.gov/diseases/5140/embryonal-carcinoma)
- [Testicular germ cell tumor | NORD/MONDO](https://rarediseases.org/mondo-disease/testicular-germ-cell-tumor/)
- [OMIM #273300 Testicular Germ Cell Tumor](https://www.omim.org/entry/273300)
- [Embryonal Carcinoma | MalaCards](https://www.malacards.org/card/embryonal_carcinoma)
- [Orphanet: Embryonal carcinoma (ORPHA:180226)](https://www.orpha.net/en/disease/detail/180226)
- [Orphanet: Non-seminomatous germ cell tumor of testis](https://www.orpha.net/en/disease/detail/363494)
- [embryonal carcinoma | NORD/MONDO](https://rarediseases.org/mondo-disease/embryonal-carcinoma/)
- [Testis: Germ cell tumors | Atlas Genetics Oncology](https://atlasgeneticsoncology.org/solid-tumor/5005/testis-germ-cell-tumors)
- [Molecular pathology of testicular germ cell tumours (PMC12700052)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12700052/)
- [Detection of isochromosome i(12p) by qRT-PCR, Histopathology 2021](https://onlinelibrary.wiley.com/doi/10.1111/his.14258)
- [SOX2, OCT4, Nanog and EMT correlations, PMC3570418](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570418/)
- [Pluripotency markers in breast cancer cell lines, PMC3506717](https://pmc.ncbi.nlm.nih.gov/articles/PMC3506717/)
- [NANOG/SOX2/OCT4 in HNSCC prognosis, PMC7408284](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7408284/)
- [Pathogenesis and pathobiology of TGCT, Histopathology 2024](https://onlinelibrary.wiley.com/doi/full/10.1111/his.15249)
- [Germ cell neoplasia in situ | Pathology Outlines](https://www.pathologyoutlines.com/topic/testisitgcn.html)
- [Cellular Senescence in GCNIS, PMC11278860](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11278860/)
- [Embryonal Carcinoma: Symptoms & Prognosis | Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/embryonal-carcinoma)
- [Serum tumour markers in germ cell tumours | ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1040842821000123)
- [Long-term outcome, one adjuvant BEP cycle, Annals of Oncology](https://www.annalsofoncology.org/article/S0923-7534(19)31372-9/fulltext)
- [Intensive induction chemotherapy C-BOP/BEP, PMC2361516](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2361516/)
- [Randomised phase 2 CBOP/BEP trial, PMC4410298](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4410298/)
- [Survival of pure EC vs mixed GCT, PMC10056449](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056449/)
- [Similarities in age-specific incidence of colon/testicular cancer, PMC3694153](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3694153/)
- [Epidemiology of Testicular Cancer, NCBI Bookshelf NBK585983](https://www.ncbi.nlm.nih.gov/books/NBK585983/)
- [CD30/CD117 combination for EC vs seminoma](https://www.researchgate.net/publication/11560082_CD30_and_CD117_c-kit_Used_in_Combination_Are_Useful_for_Distinguishing_Embryonal_Carcinoma_from_Seminoma)
- [OCT4 superior to CD30 post-chemotherapy](https://www.researchgate.net/publication/7050060_OCT4_is_superior_to_CD30_in_the_diagnosis_of_metastatic_embryonal_carcinomas_after_chemotherapy)
- [Persistent CD30 expression, prognostic significance](https://www.sciencedirect.com/science/article/abs/pii/S0022534713041128)
- [Risk factors for cryptorchidism, PMC1892638](https://pmc.ncbi.nlm.nih.gov/articles/PMC1892638/)
- [TDS components and TGCT prognosis, PMC7822361](https://pmc.ncbi.nlm.nih.gov/articles/PMC7822361/)
- [Genetic/epigenetic/non-genetic factors in TDS, PMC12841294](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12841294/)
- [NTERA-2 pluripotency and differentiation, PMC6496632](https://ncbi.nlm.nih.gov/pmc/articles/PMC6496632)
- [Role of SOX2 in EC etiology (NCCIT/NT2), PMC3880257](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880257/)
- [NT2/NTERA-2 Xenograft Model, Altogen Labs](https://altogenlabs.com/xenograft-models/other-bladder-cervical/nt2-ntera-2-xenograft-model/)
- [5-Aza hypersensitivity in EC, PMC3531428](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3531428/)
- [Hypermethylation of genes in testicular EC, Br J Cancer](https://www.nature.com/articles/bjc2015408)
- [Linking incomplete reprogramming to pluripotency, PMC2859941](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2859941/)
- [BMP inhibition/NODAL reprogramming seminoma to EC, PMC4520454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4520454/)
- [Common variation in KITLG and 5q31.3, Nature Genetics](https://www.nature.com/articles/ng.393)
- [TGCT predisposition genes review, Nature Reviews Cancer](https://www.nature.com/articles/nrc3021)
- [Identification of 22 susceptibility loci for TGCT, Nature Communications](https://www.nature.com/articles/s41467-021-24334-y)
- [Polygenic susceptibility to testicular cancer, PMC4815881](https://pmc.ncbi.nlm.nih.gov/articles/PMC4815881/)
- [Testicular Cancer: Genes, Environment, Hormones, PMC6626920](https://pmc.ncbi.nlm.nih.gov/articles/PMC6626920/)
- [Mediastinal Germ Cell Tumors, StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK563232/)
- [Klinefelter syndrome and germ cell tumors, PMC7526209](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7526209/)
- [p53 Hypersensitivity in TGCT cisplatin response, PMC3080918](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3080918/)
- [Unravelling cisplatin sensitivity/resistance mechanisms, Cambridge Core](https://www.cambridge.org/core/journals/expert-reviews-in-molecular-medicine/article/unravelling-mechanisms-of-cisplatin-sensitivity-and-resistance-in-testicular-cancer/6C142D267335E17E701C0417949DB17D)
- [Role of TP53 in cisplatin resistance, IJMS 2021](https://doi.org/10.3390/ijms222111774)
- [AJCC/TNM staging of testicular cancer, Merck Manual](https://www.merckmanuals.com/professional/multimedia/table/ajcctnm-staging-of-testicular-cancer)
- [CAP Cancer Protocol Testis](https://documents.cap.org/protocols/cp-testis-17protocol-4010.pdf)
- [Chemotherapy in teratoma with malignant transformation, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S030228380601311X)
- [Embryonal carcinoma, Wikidata](https://www.wikidata.org/wiki/Q1451877)
- [embryonal carcinoma, NORD/MONDO ICD-O/ICD listing](https://rarediseases.org/mondo-disease/embryonal-carcinoma/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/ijms222111774](https://doi.org/10.3390/ijms222111774` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC2859941`: "linking incomplete reprogramming to improved pluripotency of murine EC-cell-derived pluripotent stem cells,"
  - closest text in source: "To our knowledge, for the first time, we linked incomplete reprogramming to the improved pluripotency of EC cell-derived pluripotent stem cells"