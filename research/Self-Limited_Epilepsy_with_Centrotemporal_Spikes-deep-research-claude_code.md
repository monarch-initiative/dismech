---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T09:15:56.329597'
end_time: '2026-07-18T09:22:25.756859'
duration_seconds: 389.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Self-Limited Epilepsy with Centrotemporal Spikes
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
  - claude-opus-4-8
  web_search_requests: 6
  num_turns: 11
  total_cost_usd: 1.6438912500000002
  session_id: 6985c7f6-b250-4507-988d-ca87686e6aca
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Self-Limited Epilepsy with Centrotemporal Spikes
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Self-Limited Epilepsy with Centrotemporal Spikes** covering all of the
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

Alright, I've got the identifiers and the key citations pinned down. Here's the full report.

---

# Research Report: Self-Limited Epilepsy with Centrotemporal Spikes (SeLECTS)

> **A note on how to read this, Harry:** this is the disease that spent decades wearing the name tag "benign," until the field realized it was more like a mostly-friendly dog that occasionally nips — most kids sail through and grow out of it, but a minority pick up real language and attention problems along the way. The ILAE finally retired "benign" in 2022 and renamed it **SeLECTS**. I've kept the body citation-heavy and precise since this is headed for the KB. Every PMID here should still get run through `just fetch-reference` before it lands in YAML — I verified the load-bearing ones by search, but a few (flagged) are from memory and need the usual anti-hallucination pass.

---

## 1. Disease Information

**Overview.** Self-Limited Epilepsy with Centrotemporal Spikes (SeLECTS) is the most common focal epilepsy syndrome of childhood — an age-dependent, genetically-influenced epilepsy that begins in a neurologically and cognitively normal school-age child, produces characteristic brief focal seizures arising from the lower (rolandic/perisylvian) sensorimotor cortex, shows a signature EEG pattern of high-amplitude centrotemporal spikes activated by drowsiness and sleep, and then reliably remits by mid-adolescence. It is the mild, self-limiting anchor of a broader continuum — the **epilepsy-aphasia spectrum (EAS)** — that at its severe end includes atypical benign focal epilepsy, epileptic encephalopathy with spike-and-wave activation in sleep (EE-SWAS / formerly CSWS/ESES), and Landau-Kleffner syndrome.

**Key identifiers** (verified against the local MONDO ontology, MONDO:0007295):

| Resource | ID |
|---|---|
| **MONDO** | MONDO:0007295 |
| **OMIM** | 117100 (listed as "CENTRALOPATHIC EPILEPSY" / centrotemporal epilepsy) |
| **Orphanet** | ORPHA:1945 |
| **DOID** | DOID:3329 |
| **ICD-9** | 345.80 |
| **ICD-11 (foundation)** | 1046279423 |
| **NCIT** | C116538 |
| **UMLS** | C0376532 |
| **MedGen** | 138210 |
| **GARD** | 0010287 |
| **MeSH** | "Epilepsy, Rolandic" (D019305) |
| **SNOMED CT** | 44145005 |

Related MONDO entities worth distinguishing (NEC risk — see below): MONDO:0100020 *atypical childhood epilepsy with centrotemporal spikes*, MONDO:1060142 *GRIN2A-related self-limited epilepsy with centrotemporal spikes*, MONDO:0015587 *rolandic epilepsy-speech dyspraxia syndrome*, and MONDO:0010388 *X-linked rolandic epilepsy, intellectual disability, and speech dyspraxia*.

**Synonyms / historical names:** Benign Epilepsy with CentroTemporal Spikes (BECTS), Benign Childhood Epilepsy with CentroTemporal Spikes (BCECTS), Benign Rolandic Epilepsy (BRE), Benign Rolandic Epilepsy of Childhood (BREC), Rolandic epilepsy, centrotemporal epilepsy, centralopathic epilepsy, temporal-central focal epilepsy. **The term "benign" is now deprecated** by the ILAE 2022 nosology because it undersells the neurocognitive comorbidities in a subset of children (Specchio et al., *Epilepsia* 2022;63:1398–1442, doi:10.1111/epi.17241).

**Data derivation:** Disease-level aggregated resource. The knowledge here comes from clinical case series, natural-history cohorts, EEG phenotyping studies, and family-based linkage/genetics — not from individual EHR-derived patient records.

> ⚠️ **NEC caution for the curator:** "Rolandic epilepsy" is a genuine named-entity-confusion minefield. MONDO carries at least *four* distinct rolandic-epilepsy entities, and OMIM 117100 is intertwined with the ELP4/GRIN2A monogenic syndromes. The intended entry is the **common, complex-inheritance, self-limited** syndrome (MONDO:0007295) — not the rare Mendelian rolandic-epilepsy-plus-dyspraxia syndromes. Anchor DR content on MONDO:0007295 / OMIM:117100 and treat the GRIN2A monogenic disorder (MONDO:1060142) as a separate, severe-end entity.

---

## 2. Etiology

**Causal factors — complex/multifactorial genetics, not Mendelian.** SeLECTS is best understood as a **complex genetic trait with strong developmental/age dependence**, not a single-gene disorder. The classic view held that the *EEG trait* (centrotemporal sharp waves, CTS) was inherited as an autosomal dominant trait with age-dependent, incomplete penetrance, while the *clinical epilepsy* was a separate, multifactorial layer on top of it — most CTS carriers never seize. This "trait vs. syndrome" dissociation is the central etiologic idea (Bali et al.; Vears et al.).

**Genetic risk factors:**
- **ELP4 (11p13) — the centrotemporal sharp-wave EEG trait.** Genome-wide linkage of the CTS EEG endophenotype mapped to 11p13, with fine-mapping implicating **Elongator Protein Complex 4 (ELP4)**; the strongest signal was intron-9 variant rs986527 (Strug et al., *Eur J Hum Genet* 2009;17:1171–1181, **PMID:19172991**). *"genome-wide linkage of CTS to 11p13 (HLOD 4.30)… the strongest evidence was with rs986527 in intron 9 of ELP4."* The same 11p13 locus shows pleiotropy with developmental verbal dyspraxia (Pal et al., **PMID:20825490**), tying the EEG trait to the speech/language phenotype.
- **GRIN2A (16p13.2) — the epilepsy-aphasia spectrum, severe end.** *De novo* and inherited pathogenic variants in **GRIN2A** (encoding the GluN2A subunit of the NMDA glutamate receptor) cause EAS disorders (Lesca et al., *Nat Genet* 2013;45:1061–1066, doi:10.1038/ng.2726/2727; Lemke et al., *Nat Genet* 2013;45:1067; Carvill et al., *Nat Genet* 2013;45:1073 — trio of 2013 papers, PMIDs ~23933818/23933819/23933820, *verify before use*). Crucially, GRIN2A variants concentrate at the **atypical/severe end** (atypical BECTS, EE-SWAS, LKS) and were **not** found in classic, uncomplicated SeLECTS probands: *"pathogenic variants in GRIN2A were not detected in probands with benign childhood epilepsy with centrotemporal spikes (n = 81)"* (review, **PMID:29056244**). So GRIN2A is a risk gene for the spectrum, not a cause of typical SeLECTS.
- **Other candidate/associated genes (weaker, mostly rare-variant or spectrum-associated):** GRIN2B, RBFOX1/RBFOX3 (splicing regulators), DEPDC5, KCNQ2/KCNQ3, BDNF pathway. None is an established cause of common SeLECTS.

**Environmental / demographic risk factors:**
- **Age** — the dominant "risk factor"; the window of vulnerability is early-mid childhood (see §8).
- **Male sex** — modest male predominance (see §9).
- **Family history** — of epilepsy, febrile seizures, or the CTS EEG trait; ~5–15% have a personal history of febrile seizures.
- **Genetic loading**, not classical toxins/infections. No established environmental, infectious, or occupational trigger.

**Protective factors:** None established. Uniquely, the disease is *intrinsically self-limiting* — remission is programmed by brain maturation rather than by any modifiable protective exposure. No protective allele is characterized.

**Gene–environment interactions:** Not well characterized beyond the age/maturation dependence. The prevailing model is that a heritable cortical-excitability trait (CTS) is expressed clinically only within a developmental window, with maturation of the perisylvian/rolandic network driving both onset and spontaneous offset.

---

## 3. Phenotypes

The seizure semiology is stereotyped and is the diagnostic core. Suggested HPO terms in brackets.

**Seizure phenotypes (clinical signs):**
- **Focal aware seizures with unilateral facial (hemifacial) sensorimotor features** — twitching/clonic movements of one side of the face, lips, tongue [Focal motor seizure / HP:0002384 Focal seizure; HP:0007359 Focal-onset seizure]. Frequency: near-defining; the majority of seizures.
- **Oropharyngeal / bulbar symptoms** — guttural/gurgling sounds, a sensation in the throat, tonic/clonic contraction of oropharyngeal muscles.
- **Hypersalivation / drooling** [HP:0002307 Drooling] — very frequent, a hallmark; the child cannot swallow saliva during the event.
- **Speech arrest / anarthria** — inability to speak with preserved consciousness/comprehension [HP:0002499 Anarthria; HP:0001260 Dysarthria]. Very frequent.
- **Unilateral perioral/tongue paresthesia** — numbness/tingling of cheek, lips, tongue, gums [HP:0003401 Paresthesia]. Frequent.
- **Preserved consciousness** during typical events (the child is aware but cannot speak), a strongly characteristic feature.
- **Focal to bilateral tonic-clonic seizures** — secondary generalization, especially from sleep [HP:0032794 Bilateral tonic-clonic seizure with focal onset; HP:0002069 Generalized tonic-clonic seizures]. Occurs in a substantial minority; often the presenting event that brings the child to attention.
- **Strong nocturnal / sleep-related predominance** — ~70–80% of seizures occur during sleep, especially at sleep onset or shortly before waking [Nocturnal seizures]. Very frequent.
- **Todd's paresis** (transient post-ictal hemiparesis/facial weakness) — occasional.

**Seizure characteristics:**
- **Age of onset:** childhood, 3–14 yr, peak 7–9 yr (see §8).
- **Severity:** typically mild; seizures are brief (usually 1–3 min).
- **Frequency:** highly variable — many children have very few lifetime seizures (a single seizure in ~10–20%; overall low seizure burden). Course is episodic/infrequent.
- **Progression:** self-limited; remits (see §8).

**Neurocognitive / behavioral phenotypes (the "not-so-benign" tail):**
- **Language impairment** — expressive/receptive language, phonological processing, reading [HP:0002463 Language impairment; HP:0001328 Specific learning disability].
- **Speech dyspraxia / apraxia** — at the EAS end and in the ELP4-linked trait [HP:0011098 Speech apraxia].
- **Attention deficit / ADHD-type problems** [HP:0007018 Attention deficit hyperactivity disorder].
- **Executive-function and working-memory deficits, and mild global cognitive underperformance** [HP:0100543 Cognitive impairment].
- **Fine/gross motor and visuomotor difficulties.**

These deficits are typically **mild, state-dependent, and largely reversible** — MONDO's own definition captures it: *"During the course of the active epilepsy, behavioral and neuropsychological deficits may be found, particularly in language and executive functioning. These deficits improve when seizures remit."* They correlate with spike burden (spike-wave index) and worsen sharply if the child evolves toward EE-SWAS.

**Quality-of-life impact:** In typical SeLECTS, long-term QoL is good and near-normal after remission. During the active phase, the burden falls on **school performance, language/reading, and attention** rather than on physical disability; nocturnal seizures and parental anxiety also affect family QoL. Children who evolve to EE-SWAS/atypical forms can have significant, sometimes lasting, cognitive-linguistic impairment. Standardized QoL instrument data specific to SeLECTS are limited; most literature uses neuropsychological batteries rather than EQ-5D/SF-36.

---

## 4. Genetic / Molecular Information

**Causal genes / architecture:** SeLECTS is **not monogenic**. The best-supported molecular contributors:
- **ELP4** (HGNC:1171; 11p13) — associated with the **centrotemporal sharp-wave EEG endophenotype** (Strug 2009, **PMID:19172991**). ELP4 is a subunit of the **Elongator complex**, which modifies wobble-position uridines in tRNAs (translational/post-transcriptional regulation) and has roles in neuronal migration and paladin/cytoskeletal function. The associated variants are largely **non-coding / intronic** (e.g., rs986527), consistent with a regulatory rather than protein-coding effect.
- **GRIN2A** (HGNC:4585; 16p13.2, encodes NMDA receptor subunit GluN2A) — causal at the **severe/atypical end** of the EAS (LKS, EE-SWAS, atypical BECTS), *not* in typical SeLECTS (Lesca/Lemke/Carvill *Nat Genet* 2013; review **PMID:29056244**).

**Pathogenic variants (GRIN2A, EAS end):**
- **Genes/HGNC:** GRIN2A (HGNC:4585).
- **Variant classes:** missense (often altering channel gating/agonist potency), nonsense/frameshift (loss of function/haploinsufficiency), splice-site, and **structural/microdeletions** spanning GRIN2A.
- **ACMG classification:** pathogenic / likely pathogenic for the EAS phenotypes; many remain VUS. Curated in ClinVar and reviewed in GeneReviews (*GRIN2A-Related Disorders*, NCBI Bookshelf NBK385627).
- **Functional consequence — bidirectional:** *"GRIN2A pathogenic variants cause gain or loss of function of NMDA receptor… Gain of function can be targeted with uncompetitive NMDAR antagonists, while loss of function variants can be treated using NMDAR co-agonist serine"* (**PMID:29056244**). Some epilepsy-associated variants reduce NMDAR trafficking and agonist potency (*Sci Rep* 2017, doi:10.1038/s41598-017-00115-w).
- **Origin:** both germline inherited and *de novo*.
- **Allele frequency:** pathogenic GRIN2A variants are rare in gnomAD; the CTS-associated ELP4 variants are common polymorphisms (consistent with a common-variant susceptibility trait).

**Modifier genes:** Poorly defined. The clinical expression (whether a CTS carrier develops seizures, and whether they stay mild or evolve to EE-SWAS) is thought to be modified by additional loci and developmental factors; RBFOX1/3, GRIN2B and others have been proposed as modifiers of severity/spectrum position.

**Epigenetic information:** No robust disease-specific methylation/chromatin signature is established. The ELP4/Elongator mechanism is itself a form of post-transcriptional (translational) regulation via tRNA modification, which is epigenetic-adjacent but not classic DNA methylation.

**Chromosomal abnormalities:** No recurrent aneuploidy. **16p13.2 microdeletions** encompassing GRIN2A occur at the EAS end; these are detectable by chromosomal microarray.

*Suggested gene descriptors:* ELP4 (hgnc:1171), GRIN2A (hgnc:4585), GRIN2B (hgnc:4586), RBFOX1 (hgnc:21205).

---

## 5. Environmental Information

- **Environmental factors:** None established as causal. No toxin, radiation, or pollutant is implicated.
- **Lifestyle factors:** Sleep is the key *state* modulator — seizures and epileptiform discharges are dramatically activated by drowsiness and NREM sleep. Sleep deprivation can precipitate seizures/discharges (also exploited diagnostically). No dietary or activity risk factor is established.
- **Infectious agents:** None. SeLECTS is not infectious/post-infectious; there is no pathogen trigger.

---

## 6. Mechanism / Pathophysiology

**Core concept.** SeLECTS is a disorder of the **maturing perisylvian/rolandic cortical network** — a transient, developmentally-timed hyperexcitability of the lower sensorimotor (rolandic) and adjacent perisylvian language cortex. The network's maturation both *opens* the window (onset in childhood) and *closes* it (spontaneous remission at puberty). It's the textbook example of an **excitation–inhibition imbalance epilepsy** that is genetically primed but developmentally gated.

**Causal chain (upstream → downstream):**
1. **Genetic susceptibility** — heritable cortical hyperexcitability trait (CTS EEG endophenotype linked to ELP4/11p13; at the severe end, NMDAR dysfunction from GRIN2A). *[upstream trigger]*
2. **Perisylvian/rolandic cortical excitability imbalance** — altered glutamatergic (NMDA-mediated) signaling and/or GABAergic interneuron regulation in a specific cortical territory, expressed within a developmental window [GO:0035249 excitatory chemical synaptic transmission, glutamatergic; GO:0007268 chemical synaptic transmission].
3. **Sleep-state amplification** — NREM sleep and thalamocortical synchronization potentiate the epileptiform discharges (why seizures are nocturnal and the EEG "lights up" in sleep) → high-amplitude centrotemporal spikes with a characteristic **horizontal dipole** (negative centrotemporal / positive frontal).
4. **Focal seizure generation** — hypersynchronous discharge in the lower rolandic sensorimotor strip → hemifacial motor, oropharyngeal, salivatory, and speech-arrest semiology; occasional spread → focal-to-bilateral tonic-clonic. *[clinical manifestation]*
5. **Spike-burden spillover to cognition** — heavy interictal discharge (high spike-wave index), especially if it becomes near-continuous in sleep, disrupts sleep-dependent memory consolidation and language networks → the reversible language/attention/executive deficits; at the extreme, evolution to **EE-SWAS/CSWS** with more durable impairment. *[downstream consequence]*
6. **Developmental resolution** — network maturation normalizes excitability → seizures and CTS remit, deficits improve. *[self-limitation]*

**Molecular pathways:** Glutamatergic NMDA-receptor signaling (GRIN2A/GluN2A) is the best-defined molecular node; Elongator-complex tRNA wobble-uridine modification (GO:0002098) is the ELP4 mechanism, plausibly affecting translation of neurodevelopmental proteins and neuronal migration during corticogenesis (GO:0007420 brain development; GO:0001764 neuron migration).

**Cellular processes / cell types:** Cortical **glutamatergic pyramidal neurons** [CL:0000598 pyramidal neuron; CL:0000679 glutamatergic neuron] and **GABAergic interneurons** [CL:0000617 GABAergic neuron] of the rolandic/perisylvian cortex; E/I imbalance rather than cell death. This is a *functional/excitability* disorder — there is **no neurodegeneration, gliosis, or structural lesion** (imaging is normal by definition).

**Protein dysfunction:** GluN2A (GRIN2A) — altered NMDA receptor channel gating, reduced receptor trafficking, and altered agonist potency (both GoF and LoF variants) [UniProt Q12879].

**Metabolic / immune involvement:** No primary metabolic defect; no autoimmune mechanism in typical SeLECTS (contrast with the small subset of atypical/EE-SWAS cases where immune-mediated hypotheses are explored). No systemic biochemical abnormality.

**Tissue-damage mechanisms:** None — the "damage" is functional/electrophysiological (disrupted network function during the active period), fully reversible in typical cases.

**Molecular profiling / advanced tech:** Limited. No established transcriptomic, proteomic, metabolomic, or single-cell signature; genetics rests on family-based linkage (ELP4) and cohort sequencing (GRIN2A). FDG-PET case reports show focal rolandic metabolic changes but are not diagnostic (PMC10010858).

---

## 7. Anatomical Structures Affected

- **Organ / system level:** Central nervous system — specifically the **cerebral cortex** [UBERON:0000956]. No other organ system is primarily involved.
- **Regional localization (the defining anatomy):** The **lower rolandic (peri-Rolandic) sensorimotor cortex** around the **central sulcus** [UBERON:0002930], i.e., the lower **precentral gyrus** [UBERON:0002810] and **postcentral gyrus** [UBERON:0002811], within the broader **perisylvian / opercular region** adjacent to the **lateral (Sylvian) sulcus** [UBERON:0002721]. The "centrotemporal" EEG label reflects the C3/C4–T3/T4 electrode territory over this cortex.
- **Tissue / cell level:** Cortical gray matter neurons — glutamatergic pyramidal neurons and GABAergic interneurons (CL terms in §6). Nervous tissue only.
- **Subcellular level:** Postsynaptic density / glutamatergic synapse (NMDA receptors) [GO:0014069 postsynaptic density; GO:0045211 postsynaptic membrane]; cytoplasmic Elongator complex [GO:0033588 Elongator holoenzyme complex] for the ELP4 mechanism.
- **Lateralization:** Individual seizures and their EEG discharges are **unilateral/focal**, but the trait is frequently **bilateral or shifting** on EEG (independent bilateral centrotemporal spikes are common). Clinically, the hemifacial semiology is unilateral, contralateral to the discharging hemisphere.

---

## 8. Temporal Development

- **Onset:** Childhood, ages **3–14 years**, with a **peak at 7–9 years** (~90% between 5 and 10). Onset pattern is essentially **abrupt at the level of the first seizure** but the underlying trait is present subclinically before that. Congenital/neonatal and adult onset do **not** occur (adult onset excludes the diagnosis).
- **Progression / course:** **Episodic and infrequent.** Most children have few seizures over the active period; some have only a single lifetime seizure. Seizure burden is generally low; the "active" epilepsy phase lasts a few years.
- **Duration / remission:** **Self-limited** — this is the defining temporal feature. Seizures remit spontaneously, usually by age **13**, occasionally up to **16–18**, essentially always by adulthood. Per MONDO: *"onset of seizures between 3 and 14 years (peak 8-9 years) that usually resolve by age 13 years, but can occasionally occur up to age 18 years."* Remission is **spontaneous** (maturational), not treatment-dependent — antiseizure medication controls seizures but does not change the age of remission.
- **Critical periods:** The active-epilepsy childhood window is also the window of neurocognitive vulnerability (and the window in which heavy spike burden can, in a minority, evolve toward EE-SWAS). This makes the active period the target for monitoring language/attention and for intervention if atypical evolution appears. Recent work builds quantitative-EEG prediction models to flag children at risk of evolving to EE-SWAS (PMC11915340).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Share of childhood epilepsy:** the **most common** focal/idiopathic epilepsy of childhood; accounts for roughly **6–7% of all childhood epilepsy** overall, rising to **~15–25% of epilepsies diagnosed between ages 5–15** (and ~15% of children aged 1–15 with non-febrile seizures).
- **Incidence:** approximately **7–21 per 100,000 per year in children <15 years** (reported range for seizures with centrotemporal spikes ~10.7–21/100,000; a UK birth-cohort study reported a lower crude annual incidence of ~5.3/100,000 across all ages, reflecting methodological differences). *Orphanet epidemiology class: it is a rare-listed but relatively common childhood condition.* (Birth-cohort/incidence data: PMC7285789.)
- **Prevalence:** best expressed as incidence in the pediatric window given the self-limiting course; point prevalence in the general population is low because it clears by adulthood.

**Genetic epidemiology:**
- **Inheritance pattern:** **Complex / multifactorial.** The *EEG trait* (CTS) shows autosomal-dominant-like segregation with **age-dependent, incomplete penetrance**; the *clinical syndrome* is multifactorial/polygenic. It is **not** a classic Mendelian disorder (the monogenic GRIN2A/ELP4 forms are separate, rarer entities). *[Suggested inheritance term: HP:0010982 Polygenic inheritance / complex; the CTS trait historically HP:0000006 Autosomal dominant with incomplete penetrance.]*
- **Penetrance:** incomplete and age-dependent — most CTS-trait carriers never develop clinical seizures.
- **Expressivity:** highly variable (single seizure → typical course → atypical/EAS evolution).
- **Anticipation / mosaicism / founder effects:** not features of this disorder.
- **Consanguinity:** not a recognized risk factor (complex, not recessive).
- **Carrier frequency:** the CTS EEG trait is detectable in a notable fraction of first-degree relatives and in a small percentage of the general pediatric population who never seize.

**Demographics:**
- **Sex ratio:** modest **male predominance** (~1.5:1; boy:girl roughly 6:4).
- **Geographic / ethnic distribution:** worldwide, no strong geographic or ethnic clustering established.
- **Age distribution:** confined to childhood (see §8).

---

## 10. Diagnostics

**Diagnosis is clinical + EEG** — a characteristic history plus the signature EEG in a normal child, with normal imaging.

- **EEG (the diagnostic centerpiece):** normal background with **high-amplitude, biphasic (di/triphasic) centrotemporal spikes/sharp waves**, often with a **horizontal dipole** (surface-negative centrotemporal, surface-positive frontal), **markedly activated by drowsiness and NREM sleep**, frequently **bilateral/independent or shifting**. A **sleep EEG** greatly increases yield. ILAE 2022 criteria for typical SeLECTS require **spike-wave index (SWI) <50%** during NREM sleep with normal cognition/development; **SWI ≥50%** flags evolution toward EE-SWAS. [MAXO/LOINC: electroencephalography]
- **Neuroimaging (MRI):** **normal by definition** — MRI is done largely to exclude a structural lesion when features are atypical; a lesion argues against the diagnosis. FDG-PET is not routine (case-level focal findings only).
- **Laboratory tests / biomarkers:** none diagnostic; there is no blood, CSF, or metabolic biomarker. Labs serve only to exclude mimics.
- **Genetic testing:** **not required** for typical SeLECTS (yield is low; it's a complex trait). Genetic testing (targeted **GRIN2A** sequencing, epilepsy gene panels, or chromosomal microarray for 16p13.2) is reserved for **atypical presentations** — early/regressive language loss, EE-SWAS/CSWS, atypical semiology, developmental concerns — i.e., the EAS end. GeneReviews *GRIN2A-Related Disorders* (NBK385627) covers testing.
- **Clinical diagnostic criteria:** ILAE 2022 syndrome definitions (Specchio et al., doi:10.1111/epi.17241; epilepsydiagnosis.org SeLECTS overview) — mandatory features (normal development, typical semiology, characteristic sleep-activated centrotemporal EEG, onset 3–14 yr) and exclusionary features (structural lesion, developmental encephalopathy, SWI ≥50% with regression).
- **Differential diagnosis:**
  - **Self-limited epilepsy with autonomic seizures (Panayiotopoulos syndrome)** — autonomic/vomiting semiology, younger, occipital-predominant.
  - **Childhood occipital visual epilepsy (Gastaut type)** — visual seizures.
  - **Atypical BECTS / EE-SWAS (CSWS) / Landau-Kleffner** — the severe EAS end; distinguished by high SWI, language regression, atypical/negative-myoclonic features.
  - **Structural focal epilepsy** (e.g., low-grade tumor, focal cortical dysplasia) — MRI abnormal.
  - **Sleep parasomnias / benign sleep phenomena** — no epileptiform EEG.
- **Screening:** No population screening. Cascade/relative EEG screening is not indicated clinically (many trait carriers never seize).

---

## 11. Outcome / Prognosis

- **Survival / mortality:** **Excellent — essentially normal life expectancy.** SeLECTS is not associated with increased mortality; SUDEP risk is negligible in typical cases. No disease-specific mortality.
- **Seizure outcome:** **Remission by mid-adolescence is the rule** (see §8), independent of whether the child was treated. The great majority become seizure-free adults with normal neurological exams.
- **Neurocognitive outcome:** Generally good. **Language, attention, and executive deficits during the active phase are usually mild and largely reverse with remission.** A minority carry residual, subtler cognitive/academic effects into later life, particularly those who had heavy spike burden or evolved toward atypical/EE-SWAS forms.
- **Morbidity / complications:** the main "complications" are (a) neurocognitive/academic difficulty during the active years, and (b) rare **atypical evolution** to atypical BECTS, EE-SWAS/CSWS, or Landau-Kleffner — the outcomes that make "benign" a misnomer and that can leave lasting language impairment.
- **Prognostic factors:** high **spike-wave index / near-continuous sleep discharges**, very early onset, atypical semiology (negative myoclonus, atonic/absence features), and language regression predict a more complicated course and possible EE-SWAS evolution; QEEG-based prediction models are emerging (PMC11915340).

---

## 12. Treatment

**Overarching principle: many children need no antiseizure medication at all.** Because seizures are typically infrequent, nocturnal, brief, and self-limiting, **watchful waiting** is a legitimate first choice — treatment is often reserved for frequent seizures, daytime or focal-to-bilateral tonic-clonic seizures, or significant family/child distress. [MAXO: watchful waiting / active surveillance; NCIT:C15986 Pharmacotherapy when drugs are used.]

**Pharmacotherapy (when indicated) — generally monotherapy, low dose, short duration:**
- **Levetiracetam** [CHEBI:6437] — commonly used first-line; favorable tolerability. Evidence supports EEG normalization.
- **Sulthiame (sultiame)** — an established, evidence-based option specifically studied in this syndrome. A 6-month randomized, double-blind, placebo-controlled monotherapy trial (Rating et al./Sulthiame Study Group, *Epilepsia* 2000, **PMID:11051123**) found *"Twenty-five of the 31 STM-treated patients (81%) and 10 of the 35 placebo-treated patients (29%) completed the trial without any treatment failure"* — a clear benefit. (Note a cautionary report of cognitive deterioration in some sulthiame-treated children, **PMID:18184938** — dose/individual dependent.)
- **Carbamazepine** [CHEBI:3387] / **oxcarbazepine** [CHEBI:7824] — historically standard and effective for the focal seizures, **but with an important caveat**: sodium-channel blockers can **aggravate** atypical forms and precipitate/worsen EE-SWAS/CSWS and negative myoclonus. Use cautiously; avoid if atypical features are present.
- **Valproate** [CHEBI:39867] — broad-spectrum alternative, useful when generalization or atypical features are a concern.
- **Others:** clobazam [CHEBI:31413], gabapentin, lacosamide, lamotrigine as alternatives; a comparative effectiveness study assessed antiseizure medications by spike-wave-index response (ScienceDirect S0887899423004551; NCBI Bookshelf NBK581163).

**Atypical / EE-SWAS end (severe spectrum, escalated therapy):** high-dose benzodiazepines (e.g., nocturnal clobazam/diazepam), **corticosteroids / ACTH**, and for confirmed **GRIN2A** cases, **mechanism-targeted precision approaches** — NMDAR antagonists (e.g., **memantine** [CHEBI:64312]) for gain-of-function variants and the NMDAR co-agonist **L-serine** for loss-of-function variants (rationale per **PMID:29056244**; still investigational). Sodium-channel blockers should generally be **avoided** in this group.

**Non-pharmacological:** neuropsychological/**educational support**, speech-language therapy for language/dyspraxia difficulties, and family counseling/reassurance about the benign natural history. [MAXO: speech therapy; educational intervention.]

**Advanced/experimental therapeutics:** gene- or receptor-targeted GRIN2A therapy remains research-stage; no gene therapy is approved for this syndrome. Surgery has **no role** in typical SeLECTS.

**Treatment outcomes / adverse events:** seizure control on monotherapy is generally good; the key safety issues are (1) drug-specific cognitive/behavioral side effects (levetiracetam irritability; topiramate/sulthiame cognitive effects) and (2) **paradoxical aggravation** by carbamazepine/oxcarbazepine in atypical cases. Because remission is age-programmed, medication can usually be **withdrawn after a seizure-free interval** without recurrence.

---

## 13. Prevention

- **Primary prevention:** none — the disorder is genetically/developmentally determined and not preventable. No vaccine, no modifiable exposure.
- **Secondary prevention (early detection / intervention):** the meaningful "prevention" target is **atypical evolution** — early recognition of rising spike-wave index, language regression, or atypical semiology so that aggressive treatment (and avoidance of aggravating sodium-channel blockers) can protect cognition. Serial sleep EEG and neuropsychological monitoring in at-risk children is the practical strategy.
- **Tertiary prevention:** neurocognitive/educational and speech-language support to limit academic and language impact during the active phase; careful drug selection to avoid iatrogenic aggravation.
- **Genetic counseling:** appropriate for families, but framed around **complex inheritance / low recurrence risk** for typical SeLECTS (with the caveat that the CTS EEG trait is more heritable than the clinical epilepsy). Targeted counseling applies for confirmed monogenic GRIN2A families (see GeneReviews NBK385627).
- **Immunization / public health / prophylaxis:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human-specific syndrome [NCBITaxon:9606 *Homo sapiens*]. There is **no recognized naturally-occurring animal analog** of SeLECTS — the syndrome is defined by a human developmental cortical trait and a human EEG signature.
- **Breed / veterinary (OMIA):** No established veterinary counterpart. (Idiopathic/genetic epilepsies exist in dogs, but no direct SeLECTS homolog is described.)
- **Orthologous genes:** ELP4 and GRIN2A are deeply conserved across vertebrates — orthologs exist in mouse (*Elp4*, *Grin2a*), rat, and zebrafish — enabling mechanistic (not syndrome-recapitulating) modeling. [Use Alliance of Genome Resources / MGI for ortholog IDs.]
- **Comparative biology / transmission:** not applicable; non-infectious, non-zoonotic, no cross-species susceptibility.

---

## 15. Model Organisms

- **Overall caveat (flag as a `HUMAN_MODEL_MISMATCH` candidate for the KB):** there is **no faithful animal model of the SeLECTS *syndrome*** — no model reproduces the age-dependent centrotemporal EEG trait plus spontaneous pubertal remission. Models capture the **molecular** contributors, not the clinical entity.
- **Mouse (*Mus musculus*):**
  - ***Grin2a* knockout / point-mutant mice** — model NMDA-receptor GluN2A dysfunction; show altered synaptic plasticity, cognition, and seizure susceptibility. Useful for the EAS/GRIN2A end, not typical SeLECTS. [MGI]
  - ***Elp4* / Elongator-complex mouse models** — probe tRNA-modification and neurodevelopmental roles; relevant to the CTS EEG trait mechanism.
  - Applications: NMDAR pharmacology (memantine/serine rationale), synaptic E/I studies, neurodevelopmental corticogenesis.
- **Zebrafish / *in vitro* / iPSC:** *grin2a* zebrafish and patient-derived iPSC neurons with GRIN2A variants are used for electrophysiological/functional characterization and variant classification (GoF vs LoF), which directly informs the precision-therapy split. [ZFIN; Cellosaurus]
- **Limitations:** no model shows the disorder's signature — **self-limitation** — so questions about *why the human perisylvian network remits at puberty* remain a genuine knowledge gap best captured in the entry as a `KNOWLEDGE_GAP`/`HUMAN_MODEL_MISMATCH` discussion.

---

## Citation summary (verify each before committing to YAML)

| Claim | Reference | Status |
|---|---|---|
| ILAE 2022 nosology; "benign" deprecated; SeLECTS definition | Specchio et al., *Epilepsia* 2022;63:1398–1442, **doi:10.1111/epi.17241** | ✅ verified via search |
| CTS EEG trait maps to ELP4 (11p13), rs986527 | Strug et al., *Eur J Hum Genet* 2009;17:1171–81, **PMID:19172991** | ✅ verified |
| 11p13 pleiotropy with verbal dyspraxia | Pal et al., **PMID:20825490** | ✅ verified |
| GRIN2A at EAS end; not in typical SeLECTS; GoF/LoF precision therapy | Review, **PMID:29056244** | ✅ verified |
| GRIN2A causes EAS (foundational trio) | Lesca/Lemke/Carvill, *Nat Genet* 2013 (PMIDs ~23933818/819/820) | ⚠️ from memory — verify |
| Sulthiame monotherapy RCT (81% vs 29%) | Rating/Sulthiame Study Group, *Epilepsia* 2000, **PMID:11051123** | ✅ verified |
| Sulthiame cognitive-deterioration caution | **PMID:18184938** | ✅ verified via search listing |
| Incidence/epidemiology (birth cohort) | UK birth-cohort study, PMC7285789 | ✅ verified via search |
| GRIN2A-Related Disorders (testing, counseling) | GeneReviews **NBK385627** | ✅ verified via search |
| MONDO/OMIM/Orphanet identifiers | local `sqlite:obo:mondo` MONDO:0007295 | ✅ verified locally |

**Sources:**
- [ILAE 2022 childhood syndromes position paper (Specchio et al.)](https://onlinelibrary.wiley.com/doi/10.1111/epi.17241)
- [epilepsydiagnosis.org — SeLECTS overview](https://www.epilepsydiagnosis.org/syndrome/ects-overview.html)
- [Strug et al. — ELP4 / centrotemporal sharp waves (PMID 19172991)](https://pubmed.ncbi.nlm.nih.gov/19172991/)
- [Pal et al. — 11p13 pleiotropy, verbal dyspraxia (PMID 20825490)](https://pubmed.ncbi.nlm.nih.gov/20825490/)
- [GRIN2A mutations in epilepsy-aphasia spectrum — review (PMID 29056244)](https://pubmed.ncbi.nlm.nih.gov/29056244/)
- [GRIN2A mutations cause epilepsy-aphasia spectrum disorders — Nature Genetics](https://www.nature.com/articles/ng.2727)
- [GRIN2A-Related Disorders — GeneReviews (NBK385627)](https://www.ncbi.nlm.nih.gov/books/NBK385627/)
- [Sulthiame monotherapy RCT (PMID 11051123)](https://pubmed.ncbi.nlm.nih.gov/11051123/)
- [Cognitive deterioration with sulthiame (PMID 18184938)](https://pubmed.ncbi.nlm.nih.gov/18184938/)
- [Temporal trends in Rolandic epilepsy incidence — birth cohort (PMC7285789)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7285789/)
- [OMIM 117100](https://omim.org/entry/117100)
- [MedLink Neurology — SeLECTS](https://www.medlink.com/articles/self-limited-epilepsy-with-centrotemporal-spikes)
- [Effectiveness of antiseizure medications for SeLECTS (NBK581163)](https://www.ncbi.nlm.nih.gov/books/NBK581163/)
- [QEEG prediction of evolution to EE-SWAS (PMC11915340)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11915340/)
- [Rolandic epilepsy — IntechOpen chapter](https://www.intechopen.com/chapters/75338)

---

**Bottom line, Harry:** SeLECTS is the friendly-mostly-but-watch-it face of an excitation/inhibition imbalance in the maturing rolandic cortex — genetically primed (ELP4 for the EEG trait, GRIN2A for the severe end), developmentally gated to switch on around 7–9 and switch off by puberty, and for most kids it needs little more than reassurance and maybe low-dose levetiracetam or sulthiame. The one thing the entry should really lean on is the **spectrum** framing: the same machinery, cranked harder, becomes EE-SWAS/Landau-Kleffner, and *that* tail is where the cognition gets hurt. Two natural KB hooks jump out — a `conforms_to` link to the `epilepsy_excitation_inhibition_imbalance` module, and a `HUMAN_MODEL_MISMATCH` discussion around the unmodeled mystery of *why it remits*. Want me to go ahead and draft the actual `kb/disorders/` YAML on this `curate/selects-rolandic` branch, running the terms and references through validation as I go?