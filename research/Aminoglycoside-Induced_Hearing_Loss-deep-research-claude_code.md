---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:20:10.556963'
end_time: '2026-08-27T14:24:25.412309'
duration_seconds: 254.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aminoglycoside-Induced Hearing Loss
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 15
  total_cost_usd: 1.0307156000000002
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 42
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 17
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aminoglycoside-Induced Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Aminoglycoside-Induced Hearing Loss** covering all of the
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

# Aminoglycoside-Induced Hearing Loss (AIHL) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Aminoglycoside-induced hearing loss (AIHL) is a form of ototoxic, mitochondrially-mediated sensorineural hearing loss (SNHL) that occurs when a person carrying a pathogenic variant in the mitochondrial 12S rRNA gene **MT-RNR1** is exposed to aminoglycoside antibiotics (gentamicin, tobramycin, amikacin, streptomycin, kanamycin, neomycin). In susceptible individuals the hearing loss can be triggered by even a single, therapeutic-dose exposure and is typically bilateral, severe-to-profound, and irreversible. A separate, dose/duration-dependent form of ototoxicity also occurs in the general population (without a known MT-RNR1 variant) after cumulative or prolonged aminoglycoside courses, e.g., in cystic fibrosis (CF) or multidrug-resistant tuberculosis (MDR-TB) treatment.

**Key identifiers:**
- **OMIM:** #580000 — *DEAFNESS, AMINOGLYCOSIDE-INDUCED* ([OMIM.org](https://omim.org/entry/580000))
- **Gene:** MT-RNR1 (mitochondrial 12S rRNA), maternally inherited
- **GeneReviews:** "Nonsyndromic Hearing Loss and Deafness, Mitochondrial" (PMID: [20301595](https://pubmed.ncbi.nlm.nih.gov/20301595/))
- **ClinVar:** RCV000010254/RCV000010255 (m.1555A>G); RCV001449811/RCV000010263 (m.1494C>T)
- **MeSH/ICD:** classified under drug-induced/toxic sensorineural hearing loss (ICD-10 H91.0 Ototoxic hearing loss); MONDO term to be confirmed against the local MONDO release
- **Suggested MONDO search terms:** "aminoglycoside-induced hearing loss," "aminoglycoside otototoxicity," "maternally inherited nonsyndromic hearing loss and deafness"

**Synonyms:** Aminoglycoside-induced deafness; maternally inherited aminoglycoside ototoxicity; MT-RNR1-related susceptibility to aminoglycoside ototoxicity; nonsyndromic mitochondrial deafness with aminoglycoside sensitivity.

**Evidence base:** Predominantly aggregated disease-level literature — pedigree studies of maternally-transmitted deafness (Prezant et al. 1993; Hutchin et al. 1993, foundational reports establishing MT-RNR1 m.1555A>G), population cohort studies (UK Biobank-linked cohort, PMID: [22223843](https://pubmed.ncbi.nlm.nih.gov/22223843/)), systematic reviews of ototoxicity in TB/CF populations, and structured pharmacogenomic guidance (CPIC). Individual EHR-level data exist mainly through CF and TB ototoxicity cohort studies.

---

## 2. Etiology

### Disease Causal Factors
AIHL has two overlapping causal mechanisms:
1. **Genetic (Mendelian/mitochondrial) susceptibility:** A maternally inherited, usually homoplasmic, pathogenic variant in **MT-RNR1** (12S rRNA) that structurally mimics bacterial 16S rRNA, allowing aminoglycosides to bind and disrupt mitochondrial ribosomal protein synthesis in cochlear hair cells upon drug exposure ("two-hit" gene-environment model). This is the classic Mendelian entry represented by OMIM #580000.
2. **Non-genetic/dose-dependent ototoxicity:** Cumulative aminoglycoside exposure (total dose, duration, peak/trough serum levels, concurrent nephrotoxicity) causes ototoxicity in genetically unselected patients, especially with repeated courses (CF, MDR-TB).

### Genetic Risk Factors
- **MT-RNR1 m.1555A>G** — the most common and best-characterized variant; population prevalence ~1 in 500 (UK) to 0.19–1.8% globally, with marked founder-effect enrichment in some populations (e.g., 20.2% in Buryat individuals of the Baikal Lake region, PMID pending; PMC: [11222474](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11222474/)). Penetrance of hearing loss with aminoglycoside exposure is considered near-100% for homoplasmic carriers.
- **MT-RNR1 m.1494C>T** — second most common variant, homoplasmic, reported in >20 Asian and 2 Spanish probands; average penetrance ~18% (range 0–77%) in the absence of documented aminoglycoside exposure, rising sharply with exposure.
- **MT-RNR1 m.1095T>C** — third variant flagged by CPIC as high-risk.
- Rarer variants at **position 961** (961delT+Cn insertion, 961T>C) are also associated with nonsyndromic hearing loss with and without aminoglycoside exposure.
- **Nuclear modifier genes:** **TRMU** (mitochondrial tRNA-modifying enzyme; A10S missense variant) modulates penetrance of m.1555A>G/m.1494C>T-associated deafness in Arab-Israeli, European, and Chinese pedigrees. Secondary mitochondrial variants (e.g., m.4394C>T tRNA-Gln, m.1584A m62A rRNA methylation site) have also been proposed as penetrance modifiers (PMC: [9602358](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9602358/); HMG: [617880](https://academic.oup.com/hmg/article/24/4/1036/617880)).

### Environmental/Clinical Risk Factors
- Aminoglycoside class, dose, duration, and route (systemic vs. topical/otic) — cumulative dose is the dominant driver of non-genetic ototoxicity (CF cohorts: 4.5× higher odds of hearing loss with higher cumulative dosing).
- Renal impairment (reduced clearance → higher serum trough levels).
- Concurrent ototoxic drugs (loop diuretics, cisplatin/platinum chemotherapy, vancomycin).
- Advanced age, pre-existing renal or hepatic dysfunction, prolonged treatment duration (TB regimens of 6–12 months show near-universal hearing loss in some series).
- Noise exposure may synergize in genetically susceptible carriers even without drug exposure.

### Protective Factors
- Absence of the MT-RNR1 risk variant (genotype-guided antibiotic selection).
- Use of alternative, non-ototoxic antimicrobials when genotype-positive.
- Emerging "designer aminoglycosides" engineered to spare the mitochondrial ribosome (see Treatment/Prevention, §12–13).
- Investigational otoprotectants (see below) — evidence base currently strongest for cisplatin, not aminoglycosides.

### Gene-Environment Interaction
This is the defining feature of AIHL: the MT-RNR1 variant alone is often clinically silent (or produces only mild, late-onset, non-progressive/age-related hearing loss); the drug exposure is the "second hit" that converts genetic susceptibility into acute, severe, irreversible deafness. CPIC (2021, updated 2023) formalizes this as a pharmacogenomic gene-drug interaction (see §12).

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Bilateral sensorineural hearing loss | Clinical sign | Acute (hours–days) to subacute after exposure; can occur after a single dose in genotype-positive individuals | Near 100% penetrance in homoplasmic m.1555A>G + exposure; ~18% baseline for m.1494C>T without exposure | HP:0000407 (Sensorineural hearing impairment) |
| High-frequency-predominant hearing loss | Clinical sign / audiometric finding | Earliest detectable change (as soon as 4h post-treatment by high-frequency audiometry), progressing base-to-apex to affect speech frequencies | Common; a base-to-apex cochlear damage gradient is well documented | HP:0008625 (High-frequency sensorineural hearing impairment) |
| Progressive, severe-to-profound deafness | Clinical course | Progressive over days–weeks; permanent | Majority of homoplasmic-variant + exposure cases | HP:0008625; HP:0001730 (Progressive hearing impairment) |
| Tinnitus | Symptom | Subacute/chronic, often precedes or accompanies threshold shift | Frequently reported in cochleotoxicity monitoring | HP:0000360 (Tinnitus) |
| Vestibulotoxicity — gait ataxia, oscillopsia, dizziness, nystagmus | Clinical sign | Subacute bilateral vestibulopathy, may develop in parallel with cochleotoxicity | Variable, drug- and dose-dependent (higher with streptomycin/gentamicin) | HP:0002066 (Gait ataxia); HP:0000615 (Oscillopsia); HP:0002321 (Vertigo) |
| Multiorgan mitochondrial features (rare) | Systemic | Variable | Reported in some m.1555A>G carriers with syndromic presentations (PMC: [7015579](https://pmc.ncbi.nlm.nih.gov/articles/PMC7015579/)) | context-dependent |

**Quality of life impact:** Profound bilateral SNHL in infancy/early childhood (the population most likely to receive gentamicin for suspected sepsis) has major, well-documented effects on language acquisition, education, and social development; adult-onset cases affect communication, employment, and mental health, consistent with general SNHL QoL literature (EQ-5D/SF-36 not disease-specific for AIHL).

---

## 4. Genetic/Molecular Information

**Causal gene:** MT-RNR1 (mitochondrially encoded 12S rRNA), OMIM *561000; the deafness phenotype is OMIM #580000.

**Key pathogenic variants (all mitochondrial, maternally inherited):**
| Variant | Classification | Notes |
|---|---|---|
| m.1555A>G | Pathogenic (ClinVar RCV000010254/255) | Most common; homoplasmic; near-complete penetrance with aminoglycoside exposure; population frequency ~0.1–1.8% depending on cohort/region |
| m.1494C>T | Pathogenic (ClinVar RCV001449811/RCV000010263) | Second most common; incomplete penetrance (avg. ~18%, up to 77% in some pedigrees) |
| m.1095T>C | Pathogenic, CPIC-flagged | Rarer |
| m.961delT+Cn / m.961T>C | Associated, variable evidence | Reported with and without aminoglycoside exposure |
| m.7444G>A (MT-CO1) | Co-segregating secondary variant | Reported alongside m.1555A>G in a 3-generation Chinese family, may modify phenotype |

**Zygosity/heteroplasmy:** These variants are typically found in the **homoplasmic** state in affected pedigrees; CPIC (2021) explicitly states there is not yet sufficient evidence to define a heteroplasmy threshold below which aminoglycoside use is safe, so any detectable variant is treated per the homoplasmic guidance.

**Functional consequence:** Gain-of-susceptibility, not a classic loss-of-function — the base substitution creates a new base pair at the terminus of the penultimate stem of the 12S rRNA decoding site, structurally converting it toward the ancestral bacterial-type 16S rRNA conformation. This increases the aminoglycoside-binding pocket, permitting aminoglycoside binding to the mitochondrial ribosome much as it would bind a bacterial ribosome, inhibiting mitochondrial protein synthesis in cochlear tissue.

**Modifier genes:**
- **TRMU** (mitochondrial tRNA 5-methylaminomethyl-2-thiouridylate methyltransferase) — nuclear-encoded modifier; the A10S variant increases penetrance of MT-RNR1-associated deafness.
- Secondary mtDNA variants (m.4394C>T tRNA-Gln, m.1584 12S rRNA methylation site) proposed as additional modifiers of clinical expressivity.

**Population/allele frequency resources:** gnomAD (mitochondrial variant server) and MITOMAP catalog m.1555A>G and m.1494C>T frequencies across populations; GeneReviews Table 2 provides population-stratified prevalence of m.1555A>G ([NCBI Bookshelf NBK1422](https://www.ncbi.nlm.nih.gov/books/NBK1422/table/mt-deafness.T.prevalence_of_mtrnr1_patho/)).

**Suggested gene/molecular ontology bindings:** HGNC gene symbol MT-RNR1 (mitochondrial, note standard HGNC/NCBI Gene entry applies; dismech convention uses lowercase `hgnc:` CURIEs for nuclear genes — MT-RNR1 is mitochondrially encoded and may require special handling per dismech's mitochondrial-gene conventions).

---

## 5. Environmental Information

- **Primary environmental/pharmacologic trigger:** Systemic aminoglycoside antibiotic exposure — gentamicin, tobramycin, amikacin, streptomycin, kanamycin, neomycin, and (in TB regimens) capreomycin/viomycin (technically cyclic peptides with similar ribosomal mechanism).
- **Clinical contexts of exposure:** Neonatal suspected sepsis (empiric gentamicin), CF pulmonary exacerbations (inhaled/IV tobramycin prophylaxis every 3–4 months), MDR-TB intensive-phase injectable regimens (kanamycin, amikacin, capreomycin), and historically streptomycin for various infections.
- **Non-infectious environmental modifiers:** Concurrent noise exposure may act synergistically with genetic susceptibility (reported in some m.1555A>G pedigrees even absent drug exposure) — supports possible G×E beyond drug exposure alone.
- **No infectious-agent etiology** — this is a drug-toxicity disorder, though the underlying illness prompting aminoglycoside use (sepsis, TB, CF pulmonary infection) is itself infectious in most cases; the ontology `ECTO` "aminoglycoside antibiotic exposure" or an equivalent drug-exposure term is the appropriate environmental/exposure binding, not a pathogen taxon.

---

## 6. Mechanism / Pathophysiology

**Causal chain (genotype-positive form):**
1. **Trigger:** Systemic aminoglycoside administration in a carrier of a pathogenic MT-RNR1 variant (m.1555A>G most common).
2. **Molecular lesion:** The variant reconfigures the 12S rRNA decoding-site conformation to resemble bacterial 16S rRNA, permitting high-affinity aminoglycoside binding within the mitochondrial ribosome's small subunit.
3. **Mitochondrial protein synthesis inhibition:** Aminoglycoside binding at the decoding site causes mistranslation/inhibition of mitochondrially-encoded OXPHOS subunit synthesis, analogous to bacterial ribosome inhibition.
4. **Mitochondrial dysfunction in cochlear hair cells:** Disrupted protein synthesis leads to impaired oxidative phosphorylation, mitochondrial membrane potential collapse, and generation of reactive oxygen species (ROS).
5. **Downstream cell-death signaling:** ROS and stress-kinase activation (notably c-Jun N-terminal kinase, JNK) amplify mitochondrial injury; cytochrome c release triggers caspase-9 → caspase-3 activation (intrinsic apoptotic pathway). Calcium flux from the endoplasmic reticulum via IP3 receptors into mitochondria is a key acute step (documented in zebrafish lateral-line hair cells).
6. **Distinct temporal/mechanistic pathways by drug:** Neomycin exposure causes rapid (within ~1h) hair cell death associated with acute mitochondrial calcium flux (attenuated by the mitochondria-targeted antioxidant mitoTEMPO); gentamicin causes delayed (up to 24h) hair cell death via calcium-independent pathways (PMC: [11602426](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11602426/)).
7. **Cell death mechanisms beyond classical apoptosis:** Necroptosis has also been implicated alongside apoptosis in aminoglycoside- and cisplatin-induced ototoxicity; RIPOR2 translocation and phosphatidylserine externalization occur via mechanistically distinct pathways from canonical apoptosis (PMC: [12364911](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12364911/)).
8. **Anatomical gradient:** Cochlear damage follows a **base-to-apex** gradient — basal-turn (high-frequency-encoding) outer hair cells are damaged first and are most vulnerable, explaining the characteristic high-frequency-first audiometric pattern; inner hair cells appear especially vulnerable at low, non-antibacterial concentrations relevant to hidden hearing loss.
9. **Clinical manifestation:** Irreversible bilateral sensorineural hearing loss, high-frequency-predominant progressing to lower frequencies, ± tinnitus and vestibulotoxicity.

**Cellular processes involved:** Mitochondrial protein synthesis inhibition (GO:0032543, mitochondrial translation), oxidative stress response (GO:0006979/0034599), intrinsic apoptotic signaling (GO:0097193), regulated necrosis/necroptosis, calcium-mediated signaling between ER and mitochondria.

**Protein/molecular target:** MT-RNR1 12S rRNA decoding site of the mitochondrial small ribosomal subunit (28S) — a structural/RNA target rather than a protein per se.

**Cell types involved:** Cochlear outer hair cells (basal turn preferentially) and inner hair cells, spiral ganglion neurons (secondary degeneration), vestibular hair cells (type I/II) for the vestibulotoxic phenotype.

**Suggested ontology terms:**
- GO: GO:0032543 (mitochondrial translation), GO:0006915 (apoptotic process), GO:0070997 (neuron death), GO:0055074 (calcium ion homeostasis), GO:0034599 (cellular response to oxidative stress)
- CL: CL:0000601 (outer hair cell), CL:0000598 (inner hair cell), CL:0000101 (sensory neuron; for spiral ganglion neurons), CL:0000211 (vestibular hair cell where applicable)
- CHEBI: CHEBI:41000 (aminoglycoside antibiotic) or specific drugs — CHEBI:17833 (gentamicin), CHEBI:28864 (tobramycin), CHEBI:2637 (amikacin), CHEBI:9334 (streptomycin)

**Molecular profiling data:** Direct disease-specific transcriptomic/proteomic/metabolomic datasets in humans are limited (ototoxicity research relies heavily on animal/organoid models); zebrafish lateral-line and mouse cochlear explant transcriptomic studies of aminoglycoside exposure are available in GEO but are model-system, not human-tissue, datasets.

---

## 7. Anatomical Structures Affected

- **Organ level:** Inner ear (cochlea — primary; vestibular labyrinth — secondary/vestibulotoxicity). Systemic aminoglycoside toxicity also affects the kidney (nephrotoxicity) as a parallel, mechanistically related but anatomically distinct toxicity — relevant as a comorbid risk marker (nephrotoxicity often co-occurs and can indicate cumulative exposure).
- **Tissue/cell level:** Organ of Corti sensory epithelium — outer hair cells (basal turn first), inner hair cells, supporting cells (Deiters', pillar cells), spiral ganglion neurons (stria vascularis less directly implicated than in some other ototoxic mechanisms); vestibular sensory epithelium (crista ampullaris, maculae) hair cells for the vestibular phenotype.
- **Subcellular level:** Mitochondria (site of 12S rRNA target and ROS generation), endoplasmic reticulum (calcium release via IP3 receptors), cytosol (caspase cascade execution).
- **Localization/laterality:** Bilateral and typically symmetric.

**Suggested UBERON terms:** UBERON:0001846 (cochlea), UBERON:0005988 (organ of Corti), UBERON:0009663 (spiral ganglion), UBERON:0001824 (vestibular organ), UBERON:0000362 (mitochondrion is GO cellular component, not UBERON — use GO:0005739 for mitochondrion instead).

---

## 8. Temporal Development

- **Onset:** Can occur at any age when aminoglycoside is administered; clinically most consequential in neonates (empiric gentamicin for suspected sepsis) and in patients receiving prolonged/repeated courses (CF, MDR-TB). Onset relative to drug exposure is acute-to-subacute: earliest detectable ultra-high-frequency threshold shifts within hours (as early as 4h post-treatment in monitoring studies); clinically apparent hearing loss can appear within days to a few weeks of exposure.
- **Progression:** Once triggered, hearing loss is typically progressive over days to weeks, following a base-to-apex cochlear gradient (high frequencies affected first, then progressively lower/speech frequencies). It then stabilizes as permanent, non-progressive residual deafness once the ototoxic insult resolves (unlike some other genetic SNHL that continues to progress with age).
- **Disease course pattern:** Not relapsing-remitting — a single triggering exposure produces a step-wise, largely irreversible threshold shift. Genetically susceptible carriers not exposed to aminoglycosides may still show mild, later-onset, more gradual hearing decline in some pedigrees (independent low-penetrance expression), distinct from the acute triggered form.
- **Critical windows for intervention:** The period between first aminoglycoside dose and onset of measurable ototoxicity (hours to days) is the key window for early detection (serial high-frequency/ultra-high-frequency audiometry, otoacoustic emissions) and for genotype-based pre-exposure avoidance (point-of-care testing before/at time of first dose, see §10, §13).

---

## 9. Inheritance and Population

**Inheritance pattern:** Maternal (mitochondrial) inheritance — MT-RNR1 variants are transmitted exclusively through the maternal line; male carriers do not transmit the variant to offspring.

**Penetrance:**
- m.1555A>G: near-complete (approaching 100%) for hearing loss when a homoplasmic carrier receives aminoglycosides; lower baseline penetrance without exposure, historically reported 28%, 20%, 15% across different pedigree analyses when aminoglycoside-induced cases are included/excluded.
- m.1494C>T: average penetrance ~18% (range 0–77%) across families, strongly modified by aminoglycoside exposure history and by nuclear modifier genes (e.g., TRMU).

**Expressivity:** Variable — ranges from no detectable hearing loss (silent carriers without exposure) to profound congenital-onset deafness, influenced by modifier genes, heteroplasmy (where present), and environmental co-factors (noise, drug exposure).

**Genetic anticipation:** Not a recognized feature (this is not a repeat-expansion disorder).

**Founder effects:** Strong founder effect documented in the Buryat population of the Baikal Lake region of Russia (m.1555A>G prevalence 20.2% vs. 1.3% in surrounding Russian population) — PMC: [11222474](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11222474/) / Sci Rep [s41598-024-66254-z](https://www.nature.com/articles/s41598-024-66254-z). Founder enrichment also reported in some Spanish, Chinese, and Arab-Israeli pedigrees.

**Carrier/population frequency:**
- UK general population: ~0.26% (~1 in 385–500) for m.1555A>G.
- European general population: ~0.19%.
- Global pooled estimate (enriched cohorts, hearing-loss-ascertained): ~1.8% (863/47,328) — likely an overestimate of true general-population frequency due to ascertainment bias.
- Wide regional variation, up to 20%+ in isolated founder populations.

**Population demographics:**
- No strong sex bias in mitochondrial transmission itself (both sexes can be affected equally since inheritance is maternal but penetrance is independent of the child's sex); clinical exposure risk (e.g., neonatal sepsis treatment) is population-wide.
- Geographic/ethnic enrichment as above (Han Chinese, Spanish, Arab-Israeli, Buryat/Siberian populations disproportionately represented in the literature for specific variants).
- Age distribution of clinical presentation skews toward populations with high aminoglycoside exposure: neonates (NICU sepsis treatment), children/young adults with CF, and TB patients of any age receiving injectable second-line regimens.

**Epidemiology of ototoxicity in exposed populations (non-genotype-specific dose-dependent toxicity):**
- CF: prevalence of SNHL 0–57% depending on cohort/definition; 3–24% with <10 IV aminoglycoside doses, rising to 40–44% with >10 doses (recurrent exposure); cumulative dose associated with 4.5× higher odds of hearing loss; adult CF prevalence up to 59%.
- TB: incidence ranges from 3.2% in early-phase standard therapy up to near-universal with prolonged (6–12 month) treatment; MDR-TB incidence of ototoxicity ~22.9% in one cohort; a meta-analysis found pooled prevalence of ototoxic hearing loss of ~40.6% across drugs, with kanamycin highest at ~49.65% (J Infect systematic review, PMID: [34015383](https://pubmed.ncbi.nlm.nih.gov/34015383/)).

---

## 10. Diagnostics

**Clinical/audiologic tests:**
- Pure-tone audiometry (standard + extended high-frequency/ultra-high-frequency audiometry, which detects the earliest threshold shifts before speech-frequency involvement).
- Otoacoustic emissions (OAEs, especially distortion-product OAEs) for early, pre-symptomatic monitoring, particularly in infants and non-verbal patients.
- Serial audiometric monitoring protocols are standard of care during prolonged aminoglycoside courses (CF, TB) to detect ototoxicity early and allow dose adjustment/discontinuation.
- Newborn hearing screening (universal newborn hearing screening programs) — m.1555A>G has been specifically studied as a risk factor for failed newborn hearing screening in preterm infant cohorts (PMC: [4236616](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4236616/)).

**Genetic testing:**
- Targeted MT-RNR1 variant testing (m.1555A>G, m.1494C>T, m.1095T>C at minimum, per CPIC) — via standard clinical mtDNA sequencing/genotyping panels or dedicated hearing-loss gene panels.
- **Rapid point-of-care genotyping:** The Genedrive MT-RNR1 ID Kit provides m.1555A>G genotyping in ~26 minutes with reported 100% sensitivity/specificity in preclinical validation, enabling real-time avoidance of gentamicin in NICU settings before first dose (the **PALOH trial**, PMC: [8211036](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8211036/) and PMC: [8938898](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8938898/)). Deployed at Manchester University NHS Foundation Trust and now expanding to 14 NHS neonatal units across England, Scotland, Wales, and Northern Ireland (2024–2025 rollout).
- Non-invasive prenatal MT-RNR1 pharmacogenetic testing is under active investigation (2026 medRxiv preprint) as a means of identifying at-risk neonates before birth.
- Whole mitochondrial genome sequencing can identify rarer/novel MT-RNR1 variants and co-segregating secondary mtDNA variants (e.g., m.7444G>A, m.4394C>T) beyond the three CPIC-actionable variants.

**Clinical criteria / differential diagnosis:** Diagnosis relies on temporal association between aminoglycoside exposure and new-onset bilateral high-frequency-predominant SNHL, ideally confirmed by pre/post-exposure audiometric comparison; differential diagnosis includes other causes of SNHL (congenital, noise-induced, presbycusis, other syndromic/nonsyndromic genetic deafness, autoimmune inner ear disease) which the genetic test and exposure history help exclude/confirm.

**Screening:** CPIC and NHS guidance effectively function as a pharmacogenomic screening recommendation — genotype before first aminoglycoside exposure wherever feasible (especially neonatal/NICU and CF/TB populations with anticipated repeated courses).

---

## 11. Outcome/Prognosis

- **Reversibility:** Hearing loss from AIHL, once established, is generally **permanent and irreversible** — this is a defining clinical feature distinguishing it from some other forms of drug ototoxicity.
- **Severity spectrum:** Ranges from mild high-frequency threshold shifts (often subclinical, detected only by extended high-frequency audiometry) to bilateral profound deafness.
- **Functional/QoL impact:** Congenital or early-childhood-onset profound deafness (as in genotype-positive neonates exposed to gentamicin) carries major lifelong implications for language development, education, and psychosocial functioning unless mitigated by early intervention (hearing aids, cochlear implantation, sign language/communication support).
- **Complications:** Concurrent vestibulotoxicity contributes to falls risk, gait instability, and oscillopsia, compounding functional impact, especially in adults.
- **Mortality:** Not directly disease-related; mortality risk in this population is driven by the underlying infection requiring aminoglycoside therapy (sepsis, MDR-TB), not by the ototoxicity itself.
- **Prognostic factors:** Genotype (homoplasmic MT-RNR1 pathogenic variant = near-certain severe outcome with exposure), cumulative dose, concurrent nephrotoxicity/renal impairment (reduces drug clearance, raising exposure), and early detection/discontinuation of the ototoxic agent.

---

## 12. Treatment

There is **no reversal treatment** for established AIHL; management is preventive (avoidance, monitoring, dose optimization) and rehabilitative once hearing loss has occurred.

**Pharmacogenomics (CPIC):** The Clinical Pharmacogenetics Implementation Consortium (CPIC) published a formal guideline in 2021 (updated March 2023) — [cpicpgx.org/guidelines/cpic-guideline-for-aminoglycosides-and-mt-rnr1](https://cpicpgx.org/guidelines/cpic-guideline-for-aminoglycosides-and-mt-rnr1/):
> Any individual carrying the m.1555A>G, m.1494C>T, or m.1095T>C variant should **avoid aminoglycoside antibiotics** unless the risk of permanent hearing loss is outweighed by the severity of the infection and lack of suitable alternatives. No heteroplasmy threshold has been established as "safe," so any detectable variant is managed as if homoplasmic. The 2023 update also addressed whether variant carriers should avoid vaccines manufactured using aminoglycosides (residual amounts are not considered clinically significant for this indication).

**Rehabilitative/supportive care (NCIT terms suggested):**
- Hearing aids — NCIT:C50384 (Hearing Aid) or device-category equivalent.
- Cochlear implantation — NCIT term for cochlear implant procedure (surgical intervention; suggest NCIT:C61509 Cochlear Implant or closest available surgical-device term).
- Speech-language therapy — NCIT:C15302 (Physical Therapy)-adjacent; NCIT speech therapy term if available.
- Genetic counseling — NCIT:C15240 (Genetic Counseling), critical given maternal transmission implications for family planning.
- Audiologic monitoring/surveillance — NCIT:C25218 category (Clinical Intervention or Procedure), specific monitoring/audiometry term.

**Avoidance/substitution strategy** (primary "treatment" for genotype-positive individuals): substitution of non-aminoglycoside antimicrobials for suspected sepsis/infection when clinically appropriate — NCIT:C15986 (Pharmacotherapy) with a different `therapeutic_agent`.

**Experimental/otoprotective strategies (evidence base still developing for aminoglycosides specifically):**
- **Sodium thiosulfate** — FDA-, EMA-, and MHRA-approved (2022–2023) as an otoprotectant, but specifically for **cisplatin**-induced ototoxicity in pediatric localized non-metastatic solid tumors (SIOPEL6 and COG ACCL0431 trials showed reduced hearing-loss incidence: 39% vs 68%, and 44% vs 58%, respectively). **Not yet an approved indication for aminoglycoside ototoxicity**, though mechanistic overlap (oxidative stress, ROS scavenging) makes it of research interest.
- **Mitochondria-targeted antioxidants** (e.g., mitoTEMPO) — shown in zebrafish models to attenuate acute neomycin-induced hair cell death via mitigation of mitochondrial calcium flux; not yet in human trials for AIHL.
- **N-acetylcysteine and related antioxidants** — investigated in CF and other cohorts as adjunctive otoprotection during aminoglycoside courses; evidence remains preliminary/mixed.

**Designer aminoglycosides in development (address root cause by decoupling antibacterial activity from mitochondrial ribosome binding):**
- **Apramycin** — a 4-monosubstituted 2-deoxystreptamine aminoglycoside shown in guinea pig and cochlear explant models to have substantially lower ototoxicity than gentamicin while retaining potent activity against MDR pathogens including *Mycobacterium tuberculosis*; structural studies (3.5 Å resolution apramycin-ribosome complexes) provide a framework for further reduced-toxicity aminoglycoside design (PNAS: [10.1073/pnas.1204073109](https://www.pnas.org/doi/10.1073/pnas.1204073109); PMC: [3390888](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3390888/), [6382871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382871/)).
- **Gentamicin C1a** — a specific gentamicin congener also identified as having lower ototoxicity and no evidence of "hidden hearing loss" in guinea pig round-window application studies.
- **ELX-02** — a synthetic, eukaryotic-ribosome-selective aminoglycoside-class "read-through" agent developed primarily for nonsense-mutation genetic diseases (e.g., CF); engineered to eliminate antibacterial activity and reduce nephro-/ototoxicity. Phase 1 trials showed no severe ototoxicity or nephrotoxicity signals across dose range 0.3–7.5 mg/kg.

**Experimental clinical trials:** Multiple registered trials on ClinicalTrials.gov address sodium thiosulfate otoprotection (mostly cisplatin-focused; e.g., NCT05129748, NCT04541355) and ELX-02 pharmacokinetics/safety (NCT03776539, NCT03309605). No large registered trial currently targets otoprotection specifically for genotype-positive AIHL beyond the genotyping-avoidance strategy itself (PALOH and related implementation trials).

---

## 13. Prevention

AIHL is one of the clearest examples of a **primary-prevention-focused pharmacogenomic disorder** — because the hearing loss is irreversible once triggered, prevention (avoiding the triggering exposure in genetically susceptible individuals) is the dominant clinical strategy, more so than treatment.

- **Primary prevention — genotype-guided prescribing:** Pre-emptive or point-of-care MT-RNR1 genotyping before first aminoglycoside dose, especially in neonatal intensive care (NICU) settings where empiric gentamicin is common for suspected sepsis. The Manchester/NHS **PALOH implementation trial** demonstrated feasibility: 424/526 (80.6%) of eligible infants tested within the clinically actionable window using the Genedrive MT-RNR1 ID Kit (~26 min turnaround, 100% sensitivity/specificity in validation); identified variant carriers avoided aminoglycoside exposure entirely. This program is expanding to 14 NHS neonatal units UK-wide (2024–2025).
- **Screening — high-risk/repeated-exposure populations:** Consider MT-RNR1 genotyping before starting long-term/repeated aminoglycoside regimens in CF and MDR-TB patients, in addition to serial audiometric monitoring throughout treatment.
- **Secondary prevention — early detection during ongoing therapy:** Extended high-frequency/ultra-high-frequency audiometry and OAE monitoring at baseline and serially during aminoglycoside courses to detect subclinical threshold shifts before they progress into speech-frequency-affecting, functionally significant hearing loss; allows early drug discontinuation/dose adjustment.
- **Tertiary prevention:** Once hearing loss occurs, prompt referral to audiology/otolaryngology for hearing aid fitting or cochlear implant evaluation, and early educational/communication intervention in pediatric cases to mitigate developmental impact.
- **Genetic counseling:** Because inheritance is maternal, identification of an affected/carrier proband should prompt counseling and (ideally) cascade testing of maternal relatives, since all maternal-line relatives share the same variant and risk.
- **Non-invasive prenatal testing (emerging, 2026):** Under active investigation as a way to identify at-risk MT-RNR1-carrier neonates before birth, allowing avoidance planning before any postnatal antibiotic exposure decision is needed.
- **Prescribing/stewardship policy:** Clinical guideline bodies (CPIC; UK Genomics Education programs) now explicitly recommend genotype-informed antibiotic stewardship as formal policy, moving beyond individual clinician awareness to systematized point-of-care testing pathways.

---

## 14. Other Species / Natural Disease

- No well-established naturally-occurring veterinary counterpart of MT-RNR1-mediated AIHL has been prominently reported in the literature surveyed (OMIA search recommended for confirmation); aminoglycoside ototoxicity itself is a recognized general veterinary drug-toxicity concern (e.g., in companion animals receiving aminoglycosides), but genotype-linked susceptibility analogous to human MT-RNR1 variants is not established as a common veterinary syndrome in the sources reviewed here.
- The mitochondrial 12S rRNA target is deeply evolutionarily conserved (relationship to the bacterial 16S rRNA target is the entire basis of the mechanism), so cross-species susceptibility to aminoglycoside ototoxicity is a general pharmacological property of the drug class rather than being confined to genetically susceptible human carriers — this is why "designer aminoglycoside" research uses standard rodent (mouse, guinea pig) ototoxicity models even without introducing the human risk variant.
- **Note:** This report did not identify strong evidence of natural (spontaneous) veterinary MT-RNR1-variant disease; recommend an OMIA database check during KB curation to confirm absence/presence before asserting a definitive negative.

---

## 15. Model Organisms

- **Zebrafish (lateral-line hair cells):** Extensively used to dissect distinct temporal/mechanistic pathways of aminoglycoside-induced hair cell death — neomycin (rapid, ~1h, calcium-dependent via ER→mitochondria IP3-mediated calcium flux, rescued by mitoTEMPO) vs. gentamicin (delayed, up to 24h, calcium-independent) (PMC: [11602426](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11602426/), bioRxiv: [2024.05.30.596537](https://www.biorxiv.org/content/10.1101/2024.05.30.596537.full.pdf)). This model does not carry the human MT-RNR1 variant but demonstrates the general aminoglycoside-mitochondrial hair cell death mechanism and is used for mechanistic dissection and drug (designer-aminoglycoside/otoprotectant) screening.
- **Guinea pig (cochlear explant / in vivo chronic ototoxicity model):** Used to compare ototoxicity profiles across aminoglycoside congeners — demonstrated gentamicin C1a and apramycin as substantially less ototoxic than standard gentamicin via round-window drug application and compound action potential/outer hair cell survival assays (PMC: [6382871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382871/)).
- **Mouse (cochlear explants, in vivo dosing comparisons):** Used to refine ototoxicity study protocols and compare different aminoglycoside dosing regimens in adult mice (Murillo-Cuesta et al., *Lab Animals* 2010).
- **Genotype-specific (MT-RNR1 variant knock-in) models:** This search did not surface a well-established, widely-cited mouse or zebrafish knock-in line carrying the human m.1555A>G or m.1494C>T variant that recapitulates genotype-specific hypersensitivity; most mechanistic model-organism work uses wild-type animals to study general aminoglycoside ototoxicity pathways rather than modeling the specific human genetic susceptibility variant. This is a **notable gap** worth flagging in a knowledge-gap/discussion entry — direct modeling of the human-specific MT-RNR1 gain-of-susceptibility mutation in an animal ribosome is complicated by sequence divergence between species' mitochondrial rRNA.
- **Model limitations:** Because the causal lesion is a single-nucleotide change in human mitochondrial 12S rRNA altering aminoglycoside binding affinity, and because most current animal ototoxicity models use wild-type (non-variant) rRNA, these models capture the general aminoglycoside-mitochondrial-ribosome-hair-cell-death mechanism well but do **not** directly recapitulate the human genotype-specific hypersusceptibility — this is a translational (human-model mismatch) gap appropriate for a `HUMAN_MODEL_MISMATCH` discussion entry in dismech curation, pending confirmation of whether a knock-in model has since been published.

---

## Summary of Suggested Ontology Bindings for Curation

| Category | Suggested term(s) |
|---|---|
| MONDO | (verify local release for exact ID; candidate labels: "aminoglycoside-induced hearing loss," "maternally-inherited nonsyndromic hearing loss and deafness") |
| OMIM | #580000 |
| HPO | HP:0000407, HP:0008625, HP:0001730, HP:0000360, HP:0002066, HP:0000615, HP:0002321 |
| GO (BP) | GO:0032543, GO:0006915, GO:0070997, GO:0034599, GO:0055074 |
| CL | CL:0000601 (outer hair cell), CL:0000598 (inner hair cell), CL:0000211, CL:0000101 |
| UBERON | UBERON:0001846 (cochlea), UBERON:0005988 (organ of Corti), UBERON:0009663 (spiral ganglion), UBERON:0001824 (vestibular organ) |
| CHEBI | CHEBI:17833 (gentamicin), CHEBI:28864 (tobramycin), CHEBI:2637 (amikacin), CHEBI:9334 (streptomycin), CHEBI:41000 (aminoglycoside antibiotic class) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15240 (Genetic Counseling), NCIT:C15747 (Supportive Care) + device/procedure terms for hearing aid/cochlear implant |
| Gene | MT-RNR1 (mitochondrial 12S rRNA) |

---

## Key Caveats for Curators

1. **Snippet/quote verification required:** This report synthesizes web-search summaries and secondary source excerpts; per dismech's evidence policy, every claim used in a KB entry must be re-verified with an exact quoted substring from the actual cached reference (PMID/OMIM/GeneReviews/CPIC) via `just fetch-reference`, not from this report's paraphrased summaries.
2. **CPIC guideline citation:** Cite the primary CPIC publication (2021, PMID needed — search PubMed directly for the exact PMID of "Clinical Pharmacogenetics Implementation Consortium Guideline for the Use of Aminoglycosides Based on MT-RNR1 Genotype") plus its March 2023 update supplement.
3. **MONDO ID and precise HPO/GO term matches** should be confirmed against the locally cached ontology versions before binding, per dismech's anti-hallucination term-validation workflow.
4. **Founder-effect prevalence figures** (Buryat 20.2%, etc.) and global pooled prevalence (1.8%) should be sourced to their specific primary publications (Scientific Reports 2024, PMC:11222474) rather than cited from this summary.

Sources:
- [NC_012920.1(MT-RNR1):m.1555A>G AND Mitochondrial non-syndromic sensorineural hearing loss - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000010255/)
- [NC_012920.1(MT-RNR1):m.1555A>G AND Aminoglycoside-induced deafness - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000010254/)
- [Clinical Pharmacogenomic MT-RNR1 Screening for Aminoglycoside-Induced Ototoxicity and the Post-Test Counseling Conundrum - PubMed](https://pubmed.ncbi.nlm.nih.gov/37314952/)
- [Gentamicin Therapy and MT-RNR1 Genotype - Medical Genetics Summaries - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK285956/)
- [Non-invasive Prenatal MT-RNR1 Pharmacogenetic Testing for the Prevention of Aminoglycoside-Induced Profound Hearing Loss - medRxiv](https://www.medrxiv.org/content/10.64898/2026.01.02.25343256v1.full)
- [Mechanisms of aminoglycoside ototoxicity and targets of hair cell protection - PubMed](https://www.ncbi.nlm.nih.gov/pubmed/22121370)
- [Multiple mechanisms of aminoglycoside ototoxicity are distinguished by subcellular localization of action - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11602426/)
- [Towards the Prevention of Aminoglycoside-Related Hearing Loss - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5651232/)
- [Mechanisms of Aminoglycoside- and Cisplatin-Induced Ototoxicity - American Journal of Audiology](https://pubs.asha.org/doi/10.1044/2021_AJA-21-00006)
- [Aminoglycoside induces RIPOR2 translocation and phosphatidylserine externalization via distinct mechanisms - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12364911/)
- [Entry - #580000 - DEAFNESS, AMINOGLYCOSIDE-INDUCED - OMIM](https://omim.org/entry/580000)
- [Maternally inherited aminoglycoside-induced and nonsyndromic hearing loss is associated with the 12S rRNA C1494T mutation - PubMed](https://pubmed.ncbi.nlm.nih.gov/17698299/)
- [CPIC® Guideline for Aminoglycosides and MT-RNR1](https://cpicpgx.org/guidelines/cpic-guideline-for-aminoglycosides-and-mt-rnr1/)
- [MT-RNR1 CPIC Guidelines](https://cpicpgx.org/gene/mt-rnr1/)
- [Aminoglycoside antibiotics — Genomics Education Knowledge Hub](https://www.genomicseducation.hee.nhs.uk/genotes/knowledge-hub/aminoglycoside-antibiotics/)
- [New developments in aminoglycoside therapy and ototoxicity - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3169717/)
- [Aminoglycoside- and glycopeptide-induced ototoxicity in children: a systematic review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8669239/)
- [Prevalence of aminoglycoside-induced hearing loss in drug-resistant tuberculosis patients: A systematic review - PubMed](https://pubmed.ncbi.nlm.nih.gov/34015383/)
- [Nonsyndromic Hearing Loss and Deafness, Mitochondrial - PubMed (GeneReviews)](https://pubmed.ncbi.nlm.nih.gov/20301595/)
- [Mitochondrial tRNAGln 4394C>T Mutation May Contribute to the Clinical Expression of 1555A>G-Induced Deafness - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9602358/)
- [Results: Patient with a known MT-RNR1 genotype requiring aminoglycoside antibiotics — In the Clinic](https://www.genomicseducation.hee.nhs.uk/genotes/in-the-clinic/results-patient-with-a-known-mt-rnr1-genotype-requiring-aminoglycoside-antibiotics/)
- [Use of Sodium Thiosulfate as an Otoprotectant in Patients With Cancer Treated With Platinum Compounds - JCO](https://ascopubs.org/doi/10.1200/JCO.23.02353)
- [FDA Approves Sodium Thiosulfate to Decrease Cisplatin-Associated Ototoxicity - CancerNetwork](https://www.cancernetwork.com/view/fda-approves-sodium-thiosulfate-to-decrease-cisplatin-associated-ototoxicity-in-pediatric-localized-non-metastatic-solid-malignancies)
- [Sodium Thiosulfate for Protection from Cisplatin-Induced Hearing Loss - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1801109)
- [New Rapid genomic testing at Manchester University NHS Foundation Trust prevents at-risk neonates from potential lifelong hearing loss - BioSpace](https://www.biospace.com/new-rapid-genomic-testing-at-manchester-university-nhs-foundation-trust-hospitals-prevents-at-risk-neonates-from-potential-lifelong-hearing-loss)
- [Rapid Point-of-Care Genotyping to Avoid Aminoglycoside-Induced Ototoxicity in Neonatal Intensive Care - PubMed](https://pubmed.ncbi.nlm.nih.gov/35311942/)
- [Pharmacogenetics to Avoid Loss of Hearing (PALOH) trial protocol - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8211036/)
- [Rapid Point-of-Care Genotyping to Avoid Aminoglycoside-Induced Ototoxicity in Neonatal Intensive Care - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8938898/)
- [Genotype testing to guide antibiotic use and prevent hearing loss - Scottish Health Technologies Group](https://shtg.scot/media/2500/20241030-gentamicin-genotype-testing-assessment-v10.pdf)
- [Genetic test developed by Manchester researchers to prevent newborn babies going deaf, to be trialled across the UK - MFT NHS](https://mft.nhs.uk/2024/11/21/genetic-test-developed-by-manchester-researchers-to-prevent-newborn-babies-going-deaf-to-be-trialled-across-the-uk/)
- [Variant m.1555A>G in MT-RNR1 causes hearing loss and multiorgan mitochondrial disorder - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7015579/)
- [High prevalence of m.1555A>G in patients with hearing loss in the Baikal Lake region of Russia as a result of founder effect - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11222474/) / [Scientific Reports](https://www.nature.com/articles/s41598-024-66254-z)
- [Lower ototoxicity and absence of hidden hearing loss point to gentamicin C1a and apramycin as promising antibiotics for clinical use - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382871/)
- [Dissociation of antibacterial activity and aminoglycoside ototoxicity in the 4-monosubstituted 2-deoxystreptamine apramycin - PNAS](https://www.pnas.org/doi/10.1073/pnas.1204073109)
- [ELX-02: an investigational read-through agent for the treatment of nonsense mutation-related genetic disease](https://www.tandfonline.com/doi/full/10.1080/13543784.2020.1828862)
- [Hearing in 44-45 year olds with m.1555A>G, a genetic mutation predisposing to aminoglycoside-induced deafness: a population based cohort study - PubMed](https://pubmed.ncbi.nlm.nih.gov/22223843/)
- [Table 2. Prevalence of MT-RNR1 Pathogenic Variant m.1555A>G by Population - GeneReviews, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1422/table/mt-deafness.T.prevalence_of_mtrnr1_patho/)
- [Mitochondrial mutation m.1555A>G as a risk factor for failed newborn hearing screening in a large cohort of preterm infants - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4236616/)
- [Mitochondrial m.1584A 12S rRNA methylation in families with m.1555A>G associated hearing loss - Human Molecular Genetics](https://academic.oup.com/hmg/article/24/4/1036/617880)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.