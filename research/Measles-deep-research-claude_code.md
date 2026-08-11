---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-03T04:14:26.796004'
end_time: '2026-07-03T04:19:08.777919'
duration_seconds: 281.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Measles
  mondo_id: ''
  category: Infectious Disease
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
  - claude-sonnet-5
  web_search_requests: 22
  num_turns: 26
  total_cost_usd: 2.2934185
  session_id: 520ca325-e58e-5587-b817-abe96e2a26c5
  stop_reason: end_turn
citation_count: 57
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Measles
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Measles** covering all of the
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

# Measles: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Measles (rubeola) is a highly contagious, vaccine-preventable acute viral illness caused by *Measles morbillivirus* (measles virus, MeV), a member of genus *Morbillivirus*, family *Paramyxoviridae*. It is transmitted by respiratory droplets and airborne aerosols, and is characterized by a prodrome of high fever, cough, coryza, and conjunctivitis ("the three C's"), followed by pathognomonic Koplik spots and a cephalocaudally spreading maculopapular rash (CDC Clinical Overview; Mayo Clinic).

**Key identifiers:**
- **MeSH**: D008457 (Measles)
- **MONDO**: MONDO:0004619 (measles) — note: MONDO:0005453 is a distinct, unrelated entity; do not conflate
- **ICD-11**: 1F03 (Measles)
- **ICD-10**: B05 (Measles)
- **Wikidata**: Q79793
- Related distinct entity: subacute sclerosing panencephalitis (SSPE) has its own Wikidata/MONDO entry (Q2475919), reflecting its status as a delayed complication rather than the acute disease itself

**Synonyms:** rubeola, morbilli, 9-day measles (to distinguish from rubella/"3-day measles").

**Evidence base:** Measles is unusual among rare/infectious disease KB entries in that most curative literature is aggregated epidemiological, clinical-cohort, and experimental (NHP) data rather than individual EHR-level case data, though outbreak investigations (e.g., CDC MMWR, Ethiopia outbreak reports) report patient-level line-lists.

Sources: [Measles - MalaCards](https://www.malacards.org/card/measles), [Mondo Disease Ontology](https://mondo.monarchinitiative.org/), [1F03 Measles - ICD-11 MMS](https://www.findacode.com/icd-11/code-1826431497.html), [IGVF — MONDO:0005453](https://data.igvf.org/phenotype-terms/MONDO_0005453/)

---

## 2. Etiology

**Causal agent.** Measles is caused exclusively by infection with measles virus (MeV), a non-segmented negative-sense single-stranded RNA virus of genus *Morbillivirus*. There is no genetic (Mendelian) cause — measles is a purely infectious disease, though host genetics modulates susceptibility and vaccine response (see below).

**Risk factors:**
- **Lack of immunity / unvaccinated status**: the dominant risk factor. In the 2025 US outbreaks, 93% of confirmed cases occurred in unvaccinated individuals and 3% in under-vaccinated individuals (CDC MMWR 2025; ASTHO 2026).
- **Age**: infants too young for vaccination (<12 months) and adults >20 years are at higher risk of complications (CDC Clinical Overview).
- **Malnutrition and vitamin A deficiency**: strongly associated with severe/fatal disease. "Serum retinol is typically low in measles infection and is inversely related to the severity of the disease" (PMID:1285727 — Vitamin A levels and severity of measles, New York City). Vitamin A deficiency and malnutrition are recognized risk factors for severe measles even in adults in high-income settings (PMID:3437709 — Roma community Europe).
- **Immunodeficiency**: HIV infection, hematologic malignancy, and other immunocompromising conditions predispose to atypical, prolonged, and severe disease including measles inclusion body encephalitis (MIBE).
- **Pregnancy**: increases risk of severe maternal illness and adverse pregnancy outcomes (fetal loss, preterm birth) (Mayo Clinic).
- **Genetic/host factors** (modulating vaccine response and possibly susceptibility, not causal): polymorphisms in RARA/RARB/RARG (vitamin A receptor genes) and VDR (vitamin D receptor) are associated with variation in measles-vaccine antibody titers and cytokine responses (PMID:22082653 — "The RARB haplotype was significantly associated with variations in both measles antibody levels and cytokine secretion, including interleukin (IL)-10 and interferon (IFN)-α"); additional associations reported for cytokine receptor, toll-like receptor, and viral receptor gene variants (PMC3941984).

**Protective factors:**
- Two-dose MMR vaccination (see Prevention).
- Maternal antibody transfer confers passive protection in early infancy (waning by ~6-12 months, a key determinant of vaccine-schedule timing).
- Adequate vitamin A status.
- Prior natural infection (though this carries substantial morbidity/mortality risk itself and induces "immune amnesia" — see Mechanism).

**Gene-environment interactions:** Vitamin A/D receptor genotype interacts with nutritional vitamin A status to determine antibody response magnitude and durability after vaccination or natural infection — a clear gene-environment interaction relevant to global vitamin-A-deficient populations.

Sources: [Vitamin A levels and severity of measles - PubMed](https://pubmed.ncbi.nlm.nih.gov/1285727/), [Severe Measles, Vitamin A Deficiency, and the Roma Community](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3437709/), [Effects of Vitamin A and D Receptor Gene Polymorphisms on Immune Responses to Measles Vaccine - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3237827/), [Genetic polymorphisms in host antiviral genes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3941984/)

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HP term |
|---|---|---|---|---|
| Fever (stepwise, up to 104-105°F) | Sign | Prodromal, days 1-4 | Nearly universal | HP:0001945 (Fever) |
| Cough | Symptom | Prodromal | Very frequent | HP:0012735 (Cough) |
| Coryza (rhinorrhea) | Symptom | Prodromal | Very frequent | HP:0031417 (Rhinorrhea) |
| Conjunctivitis | Sign | Prodromal | Very frequent | HP:0000509 (Conjunctivitis) |
| Koplik spots (white/bluish-white spots on buccal mucosa) | Sign, pathognomonic | 1-2 days pre-rash, resolve 1-2 days after rash onset | 60-70% (PMC2645467; PMC4435874) | HP:0031398 (Koplik spots) if available, else HP:0100773 (oral mucosal lesion) — verify via OAK |
| Maculopapular rash | Sign | Cephalocaudal spread (face/hairline → trunk → extremities), days 3-5 of illness, fades in order of appearance over 5-7 days | Universal in classic disease | HP:0001060 (Maculopapular rash) |
| Otitis media | Complication | Acute | 7-9% | HP:0000388 (Otitis media) |
| Pneumonia | Complication | Acute, most common cause of death | 1-6% (up to 56-86% of measles deaths) | HP:0002090 (Pneumonia) |
| Diarrhea | Complication | Acute | ~8% | HP:0002014 (Diarrhea) |
| Post-infectious (acute) encephalitis | Complication | ~1 week after rash onset | 1 per 1,000-2,000 cases; 10% mortality, frequent permanent brain damage | HP:0002383 (Encephalitis) |
| Subacute sclerosing panencephalitis (SSPE) | Delayed complication | Latency 4-10 years (range 1 month-27 years) post-infection | ~1 per 100,000 cases overall; much higher (~1 in 600-1400) if infected <2 years of age | HP:0002535 (SSPE) — has its own MONDO/HP dual coding |
| Measles inclusion body encephalitis (MIBE) | Delayed complication (immunocompromised) | 1-9 months post-infection | Rare, near-uniformly fatal | HP:0002383 / consider specific descriptor |
| Thrombocytopenia | Rare complication | Acute | Rare | HP:0001873 (Thrombocytopenia) |
| Hepatitis (transient transaminitis) | Rare complication | Acute | Rare | HP:0001392 (Abnormality of the liver) / HP:0002240 (Hepatomegaly) as applicable |
| Myocarditis | Rare complication | Acute | Very rare; ~25% of reported cases progress to heart failure | HP:0001636 (Myocarditis) |
| Immune amnesia (loss of pre-existing antibody repertoire) | Immunological sequela | Weeks-months post-infection | Documented depletion of 11-73% of pre-existing antibody repertoire (PMID:31672891) | Consider HP term for acquired immunodeficiency/hypogammaglobulinemia as proxy; no precise HPO term for "immune amnesia" specifically |

**Quality of life impact:** Acute measles causes several days to weeks of debilitating febrile illness with school/work absence; complications (pneumonia, encephalitis) can cause lasting disability (neurological sequelae in ~25% of encephalitis survivors per general pediatric ID literature). SSPE and MIBE are uniformly fatal, progressive neurodegenerative conditions with severe QoL impact (progressive cognitive decline, myoclonus, coma). Immune amnesia is associated with elevated all-cause childhood mortality for 2-3 years post-measles due to loss of protection against unrelated pathogens (broader epidemiological literature, e.g., Mina et al. context).

Sources: [Koplik spots in early measles - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2645467/), [Koplik spots revisited - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435874/), [CDC Clinical Overview](https://www.cdc.gov/measles/hcp/clinical-overview/index.html), [ECDC Disease information on measles](https://www.ecdc.europa.eu/en/measles/facts), [Measles associated with numerous complications, death - AAP](https://publications.aap.org/aapnews/news/11910/Measles-associated-with-numerous-complications), [Measles Encephalitis: Towards New Therapeutics - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6893791/)

---

## 4. Genetic/Molecular Information

Measles is not a Mendelian genetic disease; "genetic/molecular" information centers on the **viral genome** rather than host pathogenic variants.

**Viral genome and gene products:** MeV is a non-segmented negative-strand RNA virus (~16 kb genome) encoding six structural proteins from the 3'→5' gene order N-P/V/C-M-F-H-L:
- **N (nucleoprotein)**: encapsidates genomic RNA, forms nucleocapsid with P and L
- **P (phosphoprotein)**: polymerase cofactor; the P gene also encodes two nonstructural accessory proteins via RNA editing/alternative ORFs — **V** and **C** proteins, both key interferon antagonists
- **M (matrix)**: links nucleocapsid to envelope during assembly; mutations in M are central to SSPE pathogenesis (below)
- **F (fusion)**: mediates membrane fusion/cell-cell fusion (syncytia)
- **H (hemagglutinin)**: receptor-binding envelope glycoprotein; determinant of tropism, binds CD46, SLAM/CD150, and nectin-4
- **L (large protein)**: RNA-dependent RNA polymerase (transcription/replication, capping, polyadenylation, methylation)

Sources: [Measles Virus - ScienceDirect Topics](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/measles-virus), [Frontiers - Measles Virus Hemagglutinin](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2011.00247/full)

**Receptors (functional "variant" analog — receptor tropism):**
- **CD150/SLAM** (signaling lymphocytic activation molecule): the receptor for wild-type MeV on immune cells; "expressed on activated B, T, monocyte, and dendritic cells" (PMC4997572). HGNC: SLAMF1.
- **Nectin-4 (PVRL4)**: the epithelial-cell receptor mediating virus egress via the airway epithelium — "Tumor Cell Marker PVRL4 (Nectin 4) Is an Epithelial Cell Receptor for Measles Virus" (PMC3161989). HGNC: NECTIN4.
- **CD46**: a complement-regulatory protein expressed on all human nucleated cells; used specifically by vaccine and some laboratory-adapted MeV strains, not wild-type virus (PMID:20010840, structural study of MV-H bound to CD46; RCSB 3INB).

**Genotypes/molecular epidemiology:** WHO recognizes measles genotypes based on N and H gene sequence divergence thresholds (2.5% and 2.0% nucleotide divergence respectively define a new genotype). Of 24 recognized genotypes, only genotypes **B3** and **D8** have caused the great majority of outbreaks globally in the elimination era (PMC7352894); B3 has further diverged into sub-genotypes 3.1 and 3.2, with 3.2/400V the dominant global clade of the past decade (PMC8540759).

**SSPE-associated viral mutations:** SSPE virus accumulates extensive hypermutation during chronic CNS persistence, notably **clustered mutations in the matrix (M) protein gene** that suppress productive budding/infectious particle release and favor cell-to-cell spread by fusion, plus **hyperfusogenic mutations in F** that facilitate CNS propagation via syncytium formation rather than free virion release (PMC8604190 — "M protein of subacute sclerosing panencephalitis virus, synergistically with the F protein, plays a crucial role in viral neuropathogenicity").

**Host genetic modifiers:** RARA/RARB/RARG (vitamin A receptor) and VDR (vitamin D receptor) polymorphisms modulate the magnitude of humoral/cellular vaccine response (see Etiology). No host pathogenic-variant classification (ACMG/ClinVar) applies since this is not a genetic disease; there is no somatic/germline distinction relevant here except in the sense of viral quasispecies evolution within a host (SSPE).

**Epigenetics:** No well-characterized disease-defining host epigenetic signature is established in the literature reviewed; MeV infection does induce host transcriptional reprogramming (interferon-stimulated gene suppression via STAT1/STAT2 antagonism — see Mechanism) but this is a functional/immunological rather than an epigenetic (chromatin) mechanism per se.

Suggested identifiers: HGNC:SLAMF1, HGNC:NECTIN4, HGNC:CD46; GO terms below.

---

## 5. Environmental Information

- **Infectious agent**: Measles morbillivirus (NCBI Taxon:11234), genus *Morbillivirus*, family *Paramyxoviridae*. Transmission is via respiratory droplet, aerosol (airborne), and direct contact with infected secretions; the virus remains viable and infectious in airspace/on surfaces for up to 2 hours after an infected person leaves an area (well-established CDC/WHO characterization).
- **Environmental/structural factors**: crowding, low vaccination coverage in a community (e.g., religious/philosophical exemption clusters — the Dutch Orthodox Protestant outbreak studied in PMC6251901; US 2025 outbreaks concentrated in under-vaccinated communities), healthcare-associated transmission, and international travel-importation into susceptible pockets are the dominant environmental drivers of outbreaks in the current elimination era.
- **Lifestyle factors**: vaccine hesitancy/refusal is the principal modifiable behavioral determinant of outbreak risk in high-income countries; nutritional status (vitamin A intake) is the principal modifiable factor for severity in low-resource settings.
- No toxin, radiation, or occupational-exposure etiology is applicable — measles is a directly infectious, not environmentally-triggered, disease.

Sources: [Studies into the mechanism of measles-associated immune suppression - Nature Communications](https://www.nature.com/articles/s41467-018-07515-0), [MMWR Measles Update 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7414a1.htm), [US measles outbreak: causes, consequences - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12046242/)

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Respiratory entry & innate immune cell infection**: MeV aerosol/droplet exposure infects **alveolar macrophages and dendritic cells** of the airway, which act as the initial portal (PMC4997572 — "MV infection starts in alveolar macrophages and dendritic cells of the airways, which transport the virus to the lymphoid organs").
2. **Lymphatic dissemination**: Infected APCs traffic the virus to **local lymph nodes and primary/secondary lymphoid organs**, where the virus undergoes explosive replication in **SLAM/CD150-high activated lymphocytes** (memory B and T cells preferentially, due to higher CD150 expression than naive cells) (PMID:33332470; PMC7994291).
3. **Systemic viremia and epithelial re-infection**: Infected immune cells recirculate systemically and transmit virus back to the **respiratory epithelium via the basolateral nectin-4 receptor**, enabling apical shedding into airway secretions for onward transmission (PMC3161989; PMC3571369).
4. **Innate immune evasion**: The **P-gene-derived V and C accessory proteins** block type I/III interferon signaling — V protein binds JAK1/TYK2 and forms a complex with STAT1/STAT2/IRF9, blocking STAT1-STAT2 heterodimerization and ISG transcription; C protein independently interferes with IFN-β transcription in the nucleus (PMC9781438; JVI.00831-08; JVI.00108-08). This transient global interferon blockade permits systemic viral spread before adaptive clearance.
5. **Immune amnesia (the signature downstream immunological lesion)**: MeV's tropism for **CD150-high memory lymphocytes** causes **selective depletion of pre-existing immunological memory** — both memory B cells (loss of IgG+/IgA+ class-switched memory B cells) and memory T cells are preferentially infected and eliminated, while a compensatory rise in naive/transitional B cells reconstitutes a "immunologically naive" repertoire (PMC6251901, Nature Communications 2018, PMID:30470742). The landmark VirScan serological study (Mina et al., *Science* 2019, PMID:31672891) quantified this directly: "Measles caused elimination of 11 to 73% of the antibody repertoire across individuals," with recovery only via re-exposure, and the effect was **absent in MMR-vaccinated children** — establishing that natural infection, not vaccination, causes this immunosuppressive erasure.
6. **Clinical rash and mucocutaneous manifestation**: The maculopapular rash and Koplik spots reflect a **cell-mediated immune (T-cell) response** attacking virus-infected vascular endothelial and epithelial cells, not direct cytopathic viral effect — rash onset coincides with the appearance of MeV-specific T cells and roughly with viral clearance from blood.
7. **Complications as downstream branches**:
   - Transient global immunosuppression (steps 4-5) → secondary bacterial/opportunistic infections (otitis media, pneumonia) which cause most deaths.
   - Acute post-infectious encephalitis (~1/1000-2000): thought to be immune-mediated (autoimmune, ADEM-like) rather than direct CNS viral invasion in most cases.
   - **SSPE**: rare (~1/10,000-100,000, but much higher if infection occurs before age 2) persistent, defective, non-productive CNS infection by a hypermutated MeV variant. Accumulated **M-protein mutations** suppress virion budding (limiting immune-detectable free virus) while **hyperfusogenic F-protein mutations** enable cell-to-cell spread within the CNS via syncytia, producing progressive neurodegeneration over years (PMC8604190).
   - **MIBE**: in severely immunocompromised hosts (HIV, hematologic malignancy, transplant), inadequate T-cell control allows productive-but-contained CNS infection with a fulminant, rapidly fatal course within months.

**Cellular processes involved:** apoptosis of infected lymphocytes, cell-cell membrane fusion (syncytium formation — GO:0140253 cell-cell fusion), suppression of type I/III interferon signaling (GO:0060337 type I interferon signaling pathway), immune memory cell depletion, bystander immunosuppression, complement regulation interference (via CD46 binding).

**Cell types involved (suggested CL terms):**
- CL:0000235 macrophage (alveolar macrophage entry)
- CL:0000451 dendritic cell
- CL:0000236 B cell / CL:0000787 memory B cell
- CL:0000084 T cell / CL:0000897 CD4-positive, alpha-beta memory T cell
- CL:0000066 epithelial cell (respiratory epithelium, nectin-4-bearing)
- CL:0000127 astrocyte / CL:0000540 neuron (CNS spread in SSPE/MIBE)

**Biological process GO terms:**
- GO:0019064 fusion of virus membrane with host plasma membrane
- GO:0039502 suppression by virus of host type I interferon-mediated signaling pathway
- GO:0002250 adaptive immune response (disrupted)
- GO:0006915 apoptotic process (infected lymphocyte death)

**Molecular profiling:** VirScan/phage-immunoprecipitation sequencing (PhIP-seq) has been the key "omics" technology demonstrating repertoire-wide antibody loss (Mina et al. 2019). Immunosequencing (Adaptive Biotechnologies/immunoSEQ-style B/T-cell receptor repertoire sequencing) was used in PMC6251901 to demonstrate reduced memory B-cell receptor diversity post-infection. No large-scale single-cell or spatial transcriptomic atlas specific to measles was identified in this search, though NHP and cotton-rat transcriptomic studies of lymphoid tissue exist in the broader literature.

Sources: [Measles Virus Host Invasion and Pathogenesis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4997572/), [On invariant T cells and measles - PLOS Pathogens/PubMed](https://pubmed.ncbi.nlm.nih.gov/33332470/), [Measles immunity and immunosuppression - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7994291/), [Measles Virus-Induced Host Immunity and Mechanisms of Viral Evasion - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9781438/), [STAT2 Is a Primary Target for Measles Virus V Protein - J Virol](https://journals.asm.org/doi/10.1128/jvi.00831-08), [Measles Virus Circumvents Host Interferon Response by C and V Proteins - J Virol](https://journals.asm.org/doi/10.1128/jvi.00108-08), [Studies into the mechanism of measles-associated immune suppression - Nature Comm](https://www.nature.com/articles/s41467-018-07515-0), Mina et al. *Science* 2019;366(6465):599-606, PMID:31672891, [M protein of SSPE virus - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8604190/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: respiratory tract (nasopharynx, trachea, bronchi) — site of entry and shedding
- Secondary/systemic: lymphoid organs (lymph nodes, spleen, thymus, tonsils — primary sites of viral amplification); skin/mucous membranes (rash, Koplik spots); eyes (conjunctivitis); in complications — lungs (pneumonia), middle ear, GI tract (diarrhea), liver (rare hepatitis), heart (rare myocarditis), CNS (encephalitis, SSPE, MIBE)
- Body systems: respiratory, immune/lymphatic, integumentary, and (in complications) nervous, cardiovascular, hepatic, hematologic (thrombocytopenia) systems

**Tissue/cell level:**
- Respiratory pseudostratified columnar epithelium (nectin-4+ basolateral entry/apical egress)
- Lymphoid tissue: germinal center B cells, memory T cells, follicular dendritic cells
- Vascular endothelium (implicated in rash pathogenesis)
- CNS: neurons and astrocytes (SSPE/MIBE; CDV comparative data show SLAM/nectin-4-independent noncytolytic astrocyte spread in the related canine distemper virus, PMC4442543, informative for morbillivirus CNS tropism generally)

**Subcellular level (GO Cellular Component):**
- Plasma membrane (H/F envelope glycoprotein fusion machinery, GO:0005886)
- Cytoplasm (nucleocapsid assembly, ribonucleoprotein complex, GO:0019013 viral nucleocapsid)
- Nucleus (C protein interferes with IFN-β transcription in the nucleus — JVI.86.2.796)

**Localization / laterality:** Rash is typically bilateral/symmetric, beginning at the hairline/behind the ears and spreading centrifugally and caudally — no lateralization is expected as this is a systemic, hematogenously/lymphatically disseminated infection.

Suggested UBERON terms: UBERON:0001004 (respiratory system), UBERON:0002370 (thymus), UBERON:0002100 (lymph node), UBERON:0002097 (skin of body), UBERON:0000955 (brain).

---

## 8. Temporal Development

**Onset:** Acute onset, incubation period ~10-14 days (range 7-21) from exposure to first symptoms; prodrome (fever, cough, coryza, conjunctivitis) begins 2-4 days before rash; Koplik spots appear 1-2 days before rash and fade 1-2 days after rash onset. Any unvaccinated/non-immune individual of any age can be affected; classically a childhood disease but adult and neonatal (congenital, via transplacental infection near delivery) cases occur.

**Progression/stages:**
1. Incubation (asymptomatic, ~10-14 days)
2. Prodromal ("catarrhal") stage (2-4 days): fever, cough, coryza, conjunctivitis, Koplik spots
3. Exanthem stage: maculopapular rash spreads face→trunk→extremities over ~3 days, with fever peaking at rash onset
4. Recovery: rash fades in order of appearance over 5-7 days, with fine desquamation; cough may persist 1-2 weeks
5. Delayed complications: acute post-infectious encephalitis (days-weeks post-rash), MIBE (1-9 months, immunocompromised only), SSPE (4-10 years, range 1 month-27 years)

**Course pattern:** Self-limited acute monophasic illness in the immunocompetent host; complications represent distinct temporal branches rather than a relapsing-remitting pattern. SSPE itself, once initiated, is relentlessly progressive (stages from behavioral/cognitive decline through myoclonus to akinetic mutism and death, classically over 1-3 years, though acute fulminant and very protracted forms occur).

**Critical periods:** Age at primary infection strongly determines SSPE risk — infection before age 2 confers markedly higher SSPE risk than infection later in childhood (well-established in the SSPE literature, e.g., PMC12145622 case series on SSPE re-emergence with low vaccination coverage). The maternal-antibody window (birth to ~12 months) is the critical period determining first MMR dose timing.

**Remission:** No spontaneous remission pattern applies to acute measles (self-limited by adaptive immunity) or SSPE (uniformly progressive, no spontaneous remission; rare prolonged plateau phases reported but not true remission).

Sources: [Subacute sclerosing panencephalitis as a re-emerging condition - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145622/), [MedlinePlus - SSPE](https://medlineplus.gov/ency/article/001419.htm), [Subacute sclerosing panencephalitis (SSPE) associated with congenital measles infection - PubMed](https://pubmed.ncbi.nlm.nih.gov/15884631/)

---

## 9. Inheritance and Population

Measles is an infectious, not inherited, disease — no Mendelian inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, or carrier-frequency concepts apply in the genetic sense. Population genetics is relevant only insofar as host genotype (vitamin A/D receptor variants) modulates vaccine response (see Etiology).

**Epidemiology:**
- **Global burden**: an estimated **11 million measles infections in 2024** — nearly 800,000 more than pre-pandemic 2019 levels (WHO/PAHO, Nov 2025). Measles deaths have fallen **88% since 2000**, but cases are surging due to declining vaccination coverage.
- **Vaccine impact**: nearly 59 million lives saved by the measles vaccine since 2000 (WHO 2025).
- **Elimination status**: 96 countries have achieved measles elimination; Canada officially **lost its elimination status** following prolonged 2024-2025 transmission — the only country in the Americas to do so.
- **US 2025 outbreak**: the worst year for US measles in over three decades — **2,144 confirmed cases**, 49 outbreaks, 88% of cases outbreak-associated, 3 deaths confirmed; 93% of cases in unvaccinated individuals.
- **Global vaccination coverage**: first-dose (MCV1) coverage ~83%, second-dose (MCV2) ~74% — both below the 95% threshold needed for herd immunity.
- **Case fatality rate**: 1-3 per 1,000 cases in general, but ranges from 0.1% in industrialized countries to as high as 15% in some developing-country settings, highest in children <5 years and immunocompromised individuals (ECDC).
- **R0 (basic reproduction number)**: widely cited as **12-18** (some estimates 6-19+), among the highest of any human pathogen, driving the very high (~92-95%) herd immunity threshold required for elimination.

**Population demographics:** No strong ethnic/genetic-susceptibility pattern is described (unlike genetic diseases); disparities in incidence instead track vaccination coverage gaps — geographically concentrated in under-immunized communities (religious/philosophical exemption clusters, conflict-affected regions with disrupted health systems, and low-income countries with weaker routine immunization infrastructure). Age distribution has shifted in some outbreak settings toward older unvaccinated cohorts and infants too young for vaccination.

Sources: [Measles deaths down 88% since 2000 - WHO](https://www.who.int/news/item/28-11-2025-measles-deaths-down-88--since-2000--but-cases-surge), [Measles deaths down 88% since 2000 - PAHO](https://www.paho.org/en/news/28-11-2025-measles-deaths-down-88-2000-cases-surge), [Understanding Current U.S. Measles Outbreaks - ASTHO](https://www.astho.org/communications/blog/2026/understanding-current-us-measles-outbreaks-elimination-status/), [Measles Update MMWR](https://www.cdc.gov/mmwr/volumes/74/wr/mm7414a1.htm), [The basic reproduction number (R0) of measles: systematic review - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1473309917303079), [Are the Objectives Proposed by WHO Sufficient to Achieve Measles Elimination - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349949/)

---

## 10. Diagnostics

**Clinical criteria:** Classic triad (fever + cough/coryza/conjunctivitis) plus generalized maculopapular rash plus Koplik spots is highly suggestive; case definitions (WHO/CDC) require laboratory confirmation for surveillance purposes given resurgence of other rash-fever illnesses.

**Laboratory tests:**
- **RT-PCR** (real-time reverse transcription PCR): highest diagnostic sensitivity when specimens (nasopharyngeal swab, throat swab, urine, or oral fluid) are collected from first contact through ~3 days after rash onset, with detection possible up to 10-14 days after rash onset. Available at state public health labs and the APHL/CDC Vaccine Preventable Disease Reference Centers.
- **IgM serology**: capture IgM EIA using recombinant nucleocapsid protein antigen; presumptive evidence of current/recent infection from serum collected within the first few days of rash.
- **Combined approach**: CDC recommends performing RT-PCR and serology together for all suspect cases.
- **Genotyping**: N/H gene sequencing for molecular epidemiology and outbreak-source tracing (WHO genotype nomenclature, e.g., distinguishing B3/D8).
- **High-avidity IgG / neutralizing antibody titers**: used to distinguish primary infection from reinfection in previously immune individuals (PMC4979181).

**Differential diagnosis:** rubella, roseola, parvovirus B19 (fifth disease), scarlet fever, Kawasaki disease, drug reactions, other viral exanthems — distinguished by Koplik spots, rash progression pattern, and epidemiologic exposure history.

**Screening:** No population genetic screening applies (non-genetic disease); public health "screening" takes the form of vaccination-status verification, contact tracing, and outbreak surveillance rather than individual diagnostic screening of asymptomatic persons.

**Suggested LOINC/ontology terms:** LOINC codes exist for measles IgM/IgG serology and measles RNA PCR panels (specific LOINC codes should be verified via LOINC search at curation time).

Sources: [Laboratory Testing for Measles - CDC](https://www.cdc.gov/measles/php/laboratories/index.html), [Measles Serology Testing - CDC](https://www.cdc.gov/measles/php/laboratories/serology.html), [High Concentrations of Measles Neutralizing Antibodies... Identify Measles Reinfection - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4979181/), [Importance of real-time RT-PCR in measles elimination program - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6267958/)

---

## 11. Outcome / Prognosis

**Mortality:** Case fatality rate 1-3/1000 in general populations; 0.1% in industrialized settings up to 15% in some developing-country outbreak settings; highest in children under 5 and immunocompromised patients. Pneumonia accounts for **56-86% of measles-related deaths** (varies by source; one estimate states "six out of ten measles associated deaths"). Encephalitis carries ~10% mortality among those who develop it. SSPE and MIBE are essentially uniformly fatal once established, over a course of months (MIBE) to typically 1-3 years (SSPE, with variable pace).

**Morbidity/functional outcomes:** Acute encephalitis survivors frequently have permanent neurological sequelae. Immune amnesia produces a period (empirically estimated at up to 2-3 years in broader epidemiological literature, though not itself directly measured in the PMIDs retrieved here) of elevated susceptibility to unrelated infections, contributing to excess non-measles mortality in the months-years following infection — the core translational implication of the Mina et al. 2019 findings.

**Recovery potential:** Uncomplicated measles is self-limited with full recovery in a large majority of immunocompetent patients; vitamin A supplementation reduces morbidity/mortality in deficient populations (Cochrane review, PMID:16235283 — "Vitamin A for treating measles in children"). Antibody-repertoire loss from immune amnesia is gradually reconstituted upon natural re-exposure to pathogens over time (Mina et al. 2019).

**Prognostic factors:** age (<5 or >20), nutritional/vitamin A status, immune status (HIV, malignancy, transplant), and vaccination status of the community (affecting secondary attack rates and access to post-exposure prophylaxis) are the dominant prognosis-modifying variables identified in this literature set.

Sources: [Vitamin A for treating measles in children - PubMed/Cochrane](https://pubmed.ncbi.nlm.nih.gov/16235283/), [Attack rate, case fatality rate and determinants of measles infection - Ethiopia systematic review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10623867/), [Measles 2025 - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMra2504516)

---

## 12. Treatment

**Pharmacotherapy:** There is **no FDA-approved specific antiviral therapy** for measles. Ribavirin has in vitro activity and has been used off-label/experimentally in severely immunocompromised patients or severe pneumonia/encephalitis, but is not FDA-approved for this indication and such use is considered experimental (Medscape Treatment).

**Vitamin A therapy** (MAXO consideration — supportive/nutritional intervention): WHO recommends **oral vitamin A, 200,000 IU (100,000 IU for infants) once daily for 2 days**, for children with measles, particularly in vitamin-A-deficient settings; the American Academy of Pediatrics extends this recommendation to US children under medical supervision. Cochrane review supports reduced morbidity/mortality with this regimen (PMID:16235283).

**Supportive care:** the mainstay of management — bed rest, hydration (especially with diarrhea), antipyretics, and prompt treatment of secondary bacterial complications (otitis media, pneumonia) with appropriate antibiotics when indicated.

**Passive immunization / post-exposure prophylaxis:** immunoglobulin (IG) can be given to high-risk exposed contacts (infants, pregnant women, immunocompromised persons) within 6 days of exposure to prevent or attenuate disease; MMR vaccine can be given within 72 hours of exposure to eligible contacts.

**Experimental/emerging approaches:**
- Fusion-inhibitory peptides delivered by nebulization have protected cynomolgus macaques from measles virus infection in a proof-of-concept animal study ("Nebulized fusion inhibitory peptide protects cynomolgus macaques from measles virus infection," *Nature Communications*, PMC/DOI referenced above) — a potential future post-exposure antiviral strategy, not yet in human trials per the sources reviewed.
- Small-molecule measles virus RNA polymerase inhibitors have been explored in preclinical/early studies as a strategy to blunt severe disease (PMC2728049 — "Measles control – Can measles virus inhibitors make a difference?").
- Probenecid was recently reported to inhibit Edmonston strain MeV replication in Vero cells in vitro (preprint/early study; requires further validation before clinical relevance can be assessed).

**MAXO term suggestions:**
- MAXO:0000950 (supportive care) — general supportive management
- MAXO:0000088 (dietary intervention) — for vitamin A supplementation (or NCIT:C15986 Pharmacotherapy + therapeutic_agent CHEBI vitamin A term if modeled as a drug)
- MAXO:0001017 (vaccination) — for MMR post-exposure prophylaxis
- Passive immunoglobulin prophylaxis would use NCIT:C15986 Pharmacotherapy with an appropriate immunoglobulin therapeutic_agent term

Sources: [Measles Treatment & Management - Medscape](https://emedicine.medscape.com/article/966220-treatment), [CDC Measles Prevention and Treatment Overview](https://www.cdc.gov/measles/media/pdfs/2026/05/measles-prevention-and-treatment-overview.pdf), [Vitamin A for treating measles in children - PMC (Cochrane)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7076287/), [Nebulized fusion inhibitory peptide protects cynomolgus macaques - Nature Communications](https://www.nature.com/articles/s41467-022-33832-6), [Measles control – Can measles virus inhibitors make a difference? - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2728049/)

---

## 13. Prevention

**Primary prevention — vaccination:** The **MMR vaccine** (live-attenuated measles, mumps, rubella) is the cornerstone of prevention. Two doses are **97% effective** (range 67-100%) at preventing measles; one dose is **93% effective** (range 39-100%). The live-attenuated vaccine strain uses **CD46** (not SLAM/nectin-4) as its primary receptor, contributing to its attenuated, non-immunosuppressive phenotype relative to wild-type virus — mechanistically consistent with the finding that immune amnesia is **not observed in MMR-vaccinated children** (Mina et al. 2019).

**Herd immunity:** Given R0 of ~12-18, elimination requires population immunity of roughly **92-95%**, translating to a need for ≥95% two-dose MMR coverage — a threshold current global coverage (83% dose 1 / 74% dose 2) falls well short of, explaining ongoing resurgence.

**Secondary prevention:** Post-exposure prophylaxis with MMR vaccine (within 72 hours) or immunoglobulin (within 6 days) for high-risk contacts; rapid outbreak-response vaccination campaigns.

**Tertiary prevention:** Prompt recognition and treatment of complications (antibiotics for secondary bacterial pneumonia/otitis media, vitamin A supplementation, supportive neurological/critical care for encephalitis) to limit sequelae.

**Public health interventions:** case isolation, contact tracing, outbreak-response immunization, maintenance of high routine MMR coverage, and surveillance/genotyping to track chains of transmission and importation sources.

**Screening/risk stratification:** verification of vaccination/immunity status (serology) in healthcare workers, international travelers, and outbreak-exposed populations; no genetic carrier or prenatal screening applies.

**Counseling:** patient/parent education addressing vaccine hesitancy is a major public-health-level "counseling" intervention specific to this disease's current epidemiology, distinct from genetic counseling paradigms used for inherited disease.

Sources: [MMR Vaccine - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554450/), [Measles Vaccine Recommendations - CDC](https://www.cdc.gov/measles/hcp/vaccine-considerations/index.html), [Herd Immunity Threshold Calculator context](https://metricgate.com/docs/herd-immunity-threshold/), [Are the Objectives Proposed by WHO Sufficient - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7349949/)

---

## 14. Other Species / Natural Disease

**Taxonomy:** Measles morbillivirus is essentially host-restricted to humans and non-human primates under natural conditions (NCBI Taxon:11234, humans NCBITaxon:9606).

**Related morbilliviruses in other species** (comparative biology, not measles itself, but mechanistically homologous):
- **Canine distemper virus (CDV)**: broad host range among carnivores — wild canids, procyonids (raccoons), ailurids (red pandas), ursids (bears, giant pandas), mustelids (ferrets, minks), viverrids (civets), hyaenids, and large felids (lions, tigers); a major cause of endangered-species mortality (PMC9862170).
- **Phocine distemper virus (PDV)**: affects marine mammals (seals); thought to have evolved from CDV via terrestrial-carnivore-to-seal contact.
- **Cetacean morbillivirus**: dolphins/whales.
- **Peste-des-petits-ruminants virus (small ruminant morbillivirus)**: sheep and goats.
- **Rinderpest morbillivirus**: historically devastated cattle populations; formally declared eradicated (the second infectious disease, after smallpox, eradicated globally) — a notable "natural experiment" precedent relevant to measles-eradication feasibility discussions.

Morbilliviruses generally are considered among the most infectious viruses known, with morbidity/mortality rates of 90-95% reported in immunologically naive host populations upon introduction (PMC6833027).

**Veterinary relevance:** CDV is of major veterinary and wildlife-conservation importance (species-jump events into endangered carnivore populations); it is also the most widely used **comparative animal-pathogenesis model** for measles virus biology given the close genetic and receptor-usage homology (both use SLAM/CD150 and nectin-4 orthologs), described as "Morbillivirus Experimental Animal Models: Measles Virus Pathogenesis Insights from Canine Distemper Virus" (PMC5086610).

**Cross-species/zoonotic potential:** Measles virus itself is not zoonotic in the classical sense (evolved from rinderpest virus historically, and does not currently circulate in animal reservoirs back to humans); CDV, by contrast, demonstrates ongoing cross-species jumps into diverse carnivore hosts.

Sources: [Canine Distemper Virus in Endangered Species - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9862170/), [Canine and Phocine Distemper Viruses: Global Spread and Genetic Basis of Jumping Species Barriers - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6833027/), [Cross-species transmission of canine distemper virus - PubMed](https://pubmed.ncbi.nlm.nih.gov/28616465/), [Morbillivirus Experimental Animal Models - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5086610/)

---

## 15. Model Organisms

**Non-human primate models:** Cynomolgus macaques experimentally infected with wild-type MeV show "marked leukopenia associated with a steady reduction in CD4+ T cell numbers for 18 days post-inoculation," making NHPs the model that "best reflect the pathogenesis of measles" among available systems, particularly for immune amnesia/immunosuppression studies. NHP models were also used to test the nebulized fusion-inhibitory-peptide prophylaxis strategy.

**Cotton rat (*Sigmodon hispidus*):** A semipermissive small-animal model; cotton rat CD150 was confirmed to function as an entry receptor for MeV with tissue expression patterns similar to mouse and human ("Cotton Rat Signaling Lymphocyte Activation Molecule (CD150) Is an Entry Receptor for Measles Virus," PMC4190324). Wild-type versus vaccine-strain MeV differ in extent of viral spread and immune suppression in this model (PMC140581), making it useful for comparative pathogenicity/attenuation studies, including maternal-antibody interference experiments relevant to vaccine timing.

**Transgenic mouse models:** Mice engineered to express human **CD46** (vaccine-strain receptor) or human **CD150/SLAM** (wild-type and vaccine-strain receptor) have been developed to "humanize" susceptibility and study MV pathogenicity, since wild-type mice lack functional receptor expression and are naturally non-permissive.

**Model limitations:** Rodent models (mouse, cotton rat) do not naturally reproduce the full clinical syndrome (rash, Koplik spots) seen in humans/NHPs and generally require receptor-humanization or are only semipermissive; NHP models are the most translationally faithful but are costly and lower-throughput. No single small-animal model fully recapitulates SSPE-type CNS persistence, immune amnesia at full scale, or the characteristic exanthem — a **human-model-mismatch-relevant gap** worth flagging for a dismech entry (e.g., rodent models chiefly validate receptor biology and short-term immunosuppression, not the complete clinical phenotype).

**Research applications:** receptor/tropism biology (transgenic mice), immune amnesia/immunosuppression mechanisms (NHP, cotton rat), vaccine/maternal-antibody interaction studies (cotton rat), and antiviral/prophylactic countermeasure testing (NHP nebulized-peptide study).

**Comparative model system:** Canine distemper virus infection of its natural host (dogs, ferrets) serves as a second-tier "natural disease" comparative model for morbillivirus CNS persistence and pathogenesis given close mechanistic homology (SLAM/nectin-4 receptor usage, similar accessory-protein IFN antagonism strategy) (PMC5086610).

Sources: [Immune responses against measles virus in cynomolgus monkeys - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0147957107000288), [Cotton Rat CD150 Is an Entry Receptor for Measles Virus - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4190324/), [Extent of Measles Virus Spread and Immune Suppression Differentiates Wild-Type and Vaccine Strains in Cotton Rat Model - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC140581/), [Current animal models: transgenic animal models for measles pathogenesis - PubMed](https://pubmed.ncbi.nlm.nih.gov/19203107/), [Morbillivirus Experimental Animal Models - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5086610/)

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms (verify via OAK before use) |
|---|---|
| Disease | MONDO:0004619 (measles); SSPE has separate MONDO coding |
| Causal organism | NCBITaxon:11234 (Measles morbillivirus) |
| Genes/receptors | hgnc:SLAMF1 (CD150/SLAM), hgnc:NECTIN4, hgnc:CD46 |
| Phenotypes (HP) | HP:0001945 Fever, HP:0012735 Cough, HP:0031417 Rhinorrhea, HP:0000509 Conjunctivitis, HP:0001060 Maculopapular rash, HP:0000388 Otitis media, HP:0002090 Pneumonia, HP:0002014 Diarrhea, HP:0002383 Encephalitis, HP:0002535 SSPE, HP:0001873 Thrombocytopenia, HP:0001636 Myocarditis |
| Cell types (CL) | CL:0000235 macrophage, CL:0000451 dendritic cell, CL:0000787 memory B cell, CL:0000897 memory T cell, CL:0000066 epithelial cell |
| GO biological processes | GO:0019064 virus membrane fusion, GO:0039502 suppression of host type I IFN signaling, GO:0002250 adaptive immune response |
| Anatomy (UBERON) | UBERON:0001004 respiratory system, UBERON:0002100 lymph node, UBERON:0002370 thymus, UBERON:0000955 brain |
| Treatments (MAXO/NCIT) | MAXO:0000950 supportive care, MAXO:0000088 dietary intervention (vitamin A), MAXO:0001017 vaccination |

**Note on evidence classification for dismech curation:** Human clinical evidence (outbreak cohorts, case series) should be tagged HUMAN_CLINICAL; NHP/cotton rat/transgenic mouse studies MODEL_ORGANISM; VirScan/immunosequencing repertoire analyses on human samples remain HUMAN_CLINICAL (in vivo human sampling, ex vivo assay) rather than IN_VITRO. All PMIDs above should be independently re-verified with `just fetch-reference` and snippet-matched before use in any KB entry, per the project's anti-hallucination SOP.