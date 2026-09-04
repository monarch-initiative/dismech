---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T18:56:03.645846'
end_time: '2026-08-24T19:01:07.949334'
duration_seconds: 304.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 6
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
  num_turns: 19
  total_cost_usd: 1.4557434
  session_id: 5f967ed8-4b7d-5ed5-b009-2720effe579b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 39
reference_validation:
  total_references: 24
  verified: 15
  not_found: 0
  unverifiable: 9
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:32595021
  relevance_assessed: 15
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:11828475
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelinating Leukodystrophy 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 6** covering all of the
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

I have sufficient sourced material now. Compiling the full report.

# Hypomyelinating Leukodystrophy 6 (HLD6) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Hypomyelinating leukodystrophy 6 (HLD6) is an autosomal dominant, gene-defined leukodystrophy caused by heterozygous pathogenic variants in *TUBB4A* (β-tubulin 4A). HLD6 sits at the severe end of a continuous **TUBB4A-related neurologic disorder spectrum** that also includes an isolated-hypomyelination phenotype at the mild end and, at a mechanistically distinct pole, an inherited dystonia (DYT-TUBB4A, formerly DYT4/"whispering dysphonia") with normal or near-normal myelination. The classic HLD6 presentation is often referred to by its MRI-defined name, **H-ABC — Hypomyelination with Atrophy of the Basal Ganglia and Cerebellum** — first delineated as a distinct clinico-radiological entity by van der Knaap and colleagues (PMID:11828475, 2002 Ann Neurol) and subsequently shown to be caused by a recurrent de novo *TUBB4A* variant by Simons et al. (PMID:23746550, *Am J Hum Genet* 2013): *"All eleven H-ABC-diagnosed individuals were found to carry the same de novo, single-nucleotide substitution in TUBB4A"* (p.Asp249Asn).

**Key identifiers:**
- **OMIM disease entry:** #612438 — *Leukodystrophy, Hypomyelinating, 6 (HLD6)*
- **OMIM gene entry:** *602662 — TUBULIN, BETA-4A; TUBB4A* (chromosome 19p13.3)
- **NCBI MedGen / GTR concept:** C2676244 ("Hypomyelinating leukodystrophy 6")
- **GeneReviews:** *TUBB4A-Related Neurologic Disorders* (NBK395611), Simons, Wolf, van der Knaap (updated periodically)
- **Related dystonia OMIM entry:** #128101 — *Dystonia 4, Torsion, Autosomal Dominant (DYT4)*, now reclassified as DYT-TUBB4A
- **ICD-10:** falls under E75.29 / G31.9 (leukodystrophy, unspecified) — no disease-specific ICD-10/11 code exists
- **Mondo:** rare-disease aggregators (e.g., NORD/Mondo disease pages) list a dedicated "hypomyelinating leukodystrophy 6" Mondo term paired with OMIM:612438 (the exact numeric MONDO CURIE could not be independently confirmed from an authoritative fetch in this session — verify against the local `sqlite:obo:mondo` adapter before curating)

**Synonyms / alternative names:**
- H-ABC (Hypomyelination with Atrophy of Basal Ganglia and Cerebellum)
- TUBB4A-related hypomyelinating leukodystrophy
- Leukoencephalopathy, hypomyelinating, with atrophy of basal ganglia and cerebellum
- Hypomyelination with basal ganglia and cerebellar atrophy

**Evidence source:** This entry is derived almost entirely from **aggregated disease-level resources** (OMIM, GeneReviews, cohort/case-series publications) rather than individual EHR-level data, consistent with the rarity of the disorder (see §9, prevalence).

---

## 2. Etiology

**Disease causal factor:** HLD6/H-ABC is a **monogenic, autosomal dominant** disorder. Essentially all cases result from a **heterozygous, typically de novo, missense variant in *TUBB4A***, the gene encoding the β-tubulin isotype β-4A. There is no known environmental, infectious, or multifactorial contribution — this is a pure Mendelian tubulinopathy.

**Genetic risk factors — the recurrent hotspot variant:**
- The overwhelming majority of classic H-ABC cases carry the identical recurrent missense variant **c.745G>A, p.(Asp249Asn) [D249N]**, first reported by Simons et al. 2013 (PMID:23746550) in 11 unrelated individuals, all with the same substitution, one of which arose on a maternally mosaic allele: *"one family quartet showed maternal mosaicism for the mutation, suggesting that rare de novo mutations that are initially phenotypically neutral in a mosaic individual can be disease causing in the subsequent generation."*
- Additional pathogenic variants causing H-ABC or milder points on the spectrum have since been reported across the gene, including p.Arg2Gly, p.Arg2Trp, p.Gly96Arg (adolescent/adult-onset milder disease; PMID reported via *Human Genome Variation* 2017), p.Met363Thr (hypomyelination without atrophy of the basal ganglia; PMC9166743), p.Gly244Asp/Ser, p.Cys354Tyr, p.Asn165Asp, and others cataloged in ClinVar under "Hypomyelinating leukodystrophy 6."
- Genotype–phenotype correlation is imperfect but partially predictable by variant location: variants in the **autoregulatory 3′ domain/C-terminal region** tend to associate with the dystonia (DYT-TUBB4A) phenotype with normal myelination, whereas variants affecting **GTP-binding, longitudinal, or lateral tubulin-tubulin interfaces** (including D249N, which lies near the taxane-binding pocket/M-loop region) more often produce hypomyelination and the H-ABC phenotype (Hersheson et al. 2013, *Ann Neurol*, on the autoregulatory domain; Curiel et al. 2017, PMID:28973395, *Hum Mol Genet*: *"TUBB4A mutations result in specific neuronal and oligodendrocytic defects that closely match clinically distinct phenotypes"*).

**Risk factors — none established beyond genetic:**
- No environmental, occupational, dietary, or infectious risk factor is described.
- **Sex:** no clear sex predilection is reported.
- **Family history:** classic H-ABC is almost always simplex (sporadic, de novo); recurrence risk to sibs is low but non-zero due to possible germline/somatic parental mosaicism (documented in the founding cohort). DYT-TUBB4A, by contrast, shows multi-generational autosomal dominant transmission with reduced penetrance.

**Protective factors:** None identified — this is a rare highly penetrant de novo Mendelian disorder; no protective genetic or environmental modifiers have been reported in the literature.

**Gene-environment interactions:** None described; disease expression is not known to be modulated by environmental exposures. (CTD/PheGenI searches return no gene-environment interaction records for TUBB4A/HLD6.)

**Suggested ontology terms:** GENO:0000147 (heterozygous), HP:0025352 (de novo variant status, if modeling as a genetic context slot), MONDO term for TUBB4A-related leukodystrophy spectrum.

---

## 3. Phenotypes

TUBB4A/HLD6 produces a recognizable triad of **clinical signs, developmental/behavioral features, and characteristic MRI-defined "laboratory" (imaging) abnormalities**. Below, phenotypes are grouped by type, with onset, severity, course, frequency, and suggested HPO terms.

### Symptoms / Clinical Signs (progressive extrapyramidal-pyramidal-cerebellar syndrome)

| Phenotype | Onset | Course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Delayed motor development / gait instability | Infancy–early childhood (median ~6 months; range 2 months–4.5 years per cohort data) | Progressive | Very frequent | HP:0001270 (Motor delay), HP:0002540 (Inability to walk) |
| Extrapyramidal movement disorder — dystonia, choreoathetosis, rigidity | Infancy–childhood | Progressive | Very frequent | HP:0001332 (Dystonia), HP:0002072 (Chorea), HP:0002063 (Rigidity) |
| Opisthotonus / oculogyric crises | Infancy–childhood | Episodic/progressive | Frequent | HP:0002179 (Oculogyric crisis) |
| Progressive spastic tetraplegia | Childhood | Progressive | Very frequent | HP:0002510 (Spastic tetraplegia) |
| Ataxia / cerebellar signs | Infancy onward | Progressive | Very frequent | HP:0001251 (Ataxia) |
| Dysarthria / speech delay / loss of communication | Childhood | Progressive | Very frequent | HP:0000750 (Delayed speech), HP:0001260 (Dysarthria) |
| Cognitive decline / intellectual disability | Variable | Progressive in classic H-ABC; can be preserved in mild spectrum | Frequent (per GeneReviews, "some can function normally") | HP:0001249 (Intellectual disability) |
| Seizures | Variable, later feature | Can be intractable in severe cases | Occasional–frequent (more common in early-infantile/encephalopathic variant end) | HP:0001250 (Seizure) |
| Feeding difficulties/dysphagia | Childhood, as disease progresses | Progressive | Frequent | HP:0011968 (Feeding difficulties) |
| Loss of ambulation | Before end of first decade in classic D249N H-ABC | Progressive, often permanent | Very frequent in severe form | HP:0002505 (Loss of ambulation) |
| Laryngeal/spasmodic dysphonia, craniocervical dystonia (DYT-TUBB4A end of spectrum) | Early childhood to third decade | Progressive; may generalize to limbs | Characteristic of the milder dystonia-predominant phenotype rather than classic H-ABC | HP:0025268 (Spasmodic dysphonia) |

### Laboratory / Imaging Abnormalities (the disease's defining "phenotype")

MRI is essentially diagnostic and constitutes the disease's hallmark quantitative phenotype:
- **Diffuse cerebral hypomyelination** (T2 hyperintensity/T1 hypointensity of white matter without the expected myelin signal maturation) — HP:0002188 (Delayed CNS myelination) / HP:0012448 (Diffuse white matter abnormalities)
- **Atrophy or near-complete disappearance of the putamen**, with sparing/relative preservation of the caudate and globus pallidus in many cases — HP:0002062 (Atrophy/Degeneration affecting the brain and spinal cord); specifically putaminal atrophy is a defining radiological sign
- **Cerebellar atrophy**, particularly of the vermis — HP:0001272 (Cerebellar atrophy)
- **Corpus callosum thinning/atrophy** in some cohorts
- Progressive nature on serial imaging: Duncan/Simons cohort work (Brain 2014, PMID for "further delineation of the phenotype and genotype-phenotype correlation") documented radiological progression paralleling clinical decline.

**Phenotype characteristics summary:**
- **Age of onset:** classic H-ABC/D249N — infancy (median 6 months; range 2 months to 4.5 years). The broader TUBB4A spectrum ranges from neonatal/early-infantile encephalopathic presentations to adult-onset isolated dystonia (DYT-TUBB4A, onset 2nd–3rd decade) or adult-onset spastic paraplegia with isolated hypomyelination.
- **Severity:** highly variable across the spectrum — from severe early-infantile encephalopathy with intractable seizures to mild, slowly progressive isolated dystonia with normal myelination.
- **Progression:** typically progressive in classic H-ABC — feeding difficulties, loss of communication, and loss of ambulation accrue "before the end of the first decade of life" in the D249N-associated phenotype (per natural-history literature summarized above).
- **Frequency among affected individuals:** the core triad (hypomyelination + putaminal atrophy + cerebellar atrophy) is present in essentially all classic H-ABC cases by definition/ascertainment; extrapyramidal and pyramidal signs are "very frequent"; seizures are less universal and more associated with the severe/encephalopathic end.

### Quality of Life Impact
Progressive loss of independent ambulation, communication, and feeding capacity in the classic form imposes major functional impact requiring wheelchair use, augmentative communication, and often gastrostomy feeding; no disease-specific EQ-5D/SF-36 data were identified in the literature (expected for an ultra-rare pediatric neurodegenerative disease — QoL is typically captured via caregiver-reported functional scales in natural history studies rather than standardized generic instruments).

---

## 4. Genetic / Molecular Information

**Causal gene:** ***TUBB4A*** (HGNC:20773; OMIM *602662), chromosome 19p13.3, encoding **β-tubulin isotype 4A**, a major constituent of neuronal and oligodendroglial microtubules.

**Pathogenic variant landscape:**
- **Recurrent hotspot:** c.745G>A, p.(Asp249Asn) — the dominant variant in classic H-ABC, arising recurrently as an independent de novo mutation at a mutable site (subsequently shown to also recur in a Chinese cohort at a **CpG hotspot**, in the TMEM106B modifier-gene paper's companion literature — note: the CpG-hotspot recurrence finding specifically concerns *TMEM106B* p.Asp252Asn in HLD16, a distinct but molecularly parallel story; the *TUBB4A* D249N recurrence in H-ABC is independently well-documented across multiple ethnic cohorts).
- **Variant classification:** per ACMG/AMP criteria as applied in ClinVar, D249N and related H-ABC variants are classified **Pathogenic/Likely Pathogenic**, generally supported by de novo occurrence (PS2), absence from population databases (PM2), and functional/structural evidence (PS3/PM1 — see mechanism below).
- **Variant type:** missense, clustering in functionally critical domains (GTP-binding pocket, lateral/longitudinal tubulin dimer interface region, autoregulatory C-terminal domain).
- **Population frequency:** the D249N and other H-ABC-causing variants are essentially **absent from gnomAD/ExAC/1000 Genomes** (consistent with de novo, highly penetrant, severe pediatric disease under strong purifying selection).
- **Origin:** predominantly **de novo germline**; rare parental somatic/germline mosaicism documented (Simons et al. 2013).
- **Functional consequence:** the D249N substitution is classified in structural/functional studies as an **antimorphic (dominant-negative-like) mutation** — *"the p.D249N variant is classified as an antimorphic mutation that affects microtubule polymerization as a steric block. In silico simulations revealed that the straight conformation is less likely adopted, possibly leading to steric hindrances during microtubule polymerization"* (per structural work summarized in Science Advances 2022, PMID:35275727, "H-ABC– and dystonia-causing TUBB4A mutations show distinct pathogenic effects"). H-ABC-causing mutants show **reduced incorporation into microtubules and slower polymerization growth**, accumulating in the free-tubulin pool, distinct from the DYT-TUBB4A autoregulatory-domain mutants, which act through disrupted autoregulation of β-tubulin's own mRNA stability rather than direct polymerization defects — this mechanistic split is the molecular basis for the phenotypic divergence between H-ABC and DYT-TUBB4A.

**Modifier genes:** No confirmed modifier genes for TUBB4A/HLD6 severity are established in the human literature (contrast with the mechanistically analogous HLD16/*TMEM106B* disorder, where *TMEM106B* itself is independently a well-known **modifier locus for FTLD-TDP/GRN-related neurodegeneration** — an interesting but distinct biology not directly bearing on TUBB4A HLD6 pathogenesis).

**Epigenetic information:** No disease-specific DNA methylation or chromatin-level studies of *TUBB4A*/HLD6 were identified; not a primary mechanism in this disorder.

**Chromosomal abnormalities:** HLD6 is caused by point mutations, not large structural/copy-number chromosomal rearrangements; no aneuploidy or translocation etiology is described.

**Suggested ontology/annotation terms:** hgnc:20773 (TUBB4A gene), GO:0005874 (microtubule), GO:0007017 (microtubule-based process), GO:0005525 (GTP binding), FunctionalImpactCategory: consider `DOMINANT_NEGATIVE` for the D249N polymerization-poisoning mechanism.

---

## 5. Environmental Information

No environmental toxins, radiation, pollutant, or occupational exposures are implicated in HLD6 causation. No lifestyle factor (diet, smoking, alcohol, exercise) modifies risk or course. No infectious trigger or agent is described. This is consistent with HLD6's status as a purely monogenic, highly penetrant, de novo disorder — CTD, TOXNET, and CDC/WHO searches return no gene-environment or exposure associations for TUBB4A-related leukodystrophy.

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **De novo heterozygous missense variant in *TUBB4A*** (e.g., D249N) →
2. **Production of mutant β-tubulin-4A protein** that is incorporated into the cellular tubulin pool alongside wild-type β-tubulin →
3. **Antimorphic/dominant-negative disruption of microtubule assembly dynamics**: mutant tubulin heterodimers show reduced incorporation efficiency and, once incorporated, sterically impair normal microtubule polymerization/depolymerization dynamics, and mutant protein accumulates abnormally in the free (unpolymerized) tubulin pool rather than the polymer →
4. **Cell-type-specific consequences** differing by lineage:
   - In **oligodendrocyte lineage cells**, disrupted microtubule dynamics impair oligodendrocyte precursor cell (OPC) differentiation/maturation and myelin sheath elaboration, producing a **dramatic decrease in mature oligodendrocytes and their progenitors** (demonstrated directly in *Tubb4a*^D249N/D249N knock-in mice) →
   - In **striatal medium spiny neurons and cerebellar neurons**, cytoskeletal dysfunction from mutant tubulin incorporation drives **neuronal degeneration**, independent of and in parallel to the oligodendroglial defect (eLife 2020, PMID:32463361/PMC7255805: *"TUBB4A mutations result in both glial and neuronal degeneration in an H-ABC leukodystrophy mouse model"*) →
5. **Convergent tissue-level pathology**: failure of normal developmental myelination (**hypomyelination**, rather than a normally myelinated brain undergoing demyelination) combined with **selective, progressive neurodegeneration of the putamen and cerebellum** →
6. **Structural brain atrophy** visible on MRI (putaminal disappearance, cerebellar atrophy, diffuse hypomyelination) →
7. **Clinical phenotype**: progressive extrapyramidal (dystonia, choreoathetosis), pyramidal (spasticity), and cerebellar (ataxia) dysfunction, with developmental stagnation, seizures in a subset, and eventual loss of ambulation/communication.

**Upstream vs. downstream distinctions:** The primary molecular lesion (mutant tubulin incorporation/polymerization poisoning) is upstream and common to all cell types expressing TUBB4A; the *bifurcation* into oligodendroglial-predominant (hypomyelination) versus neuronal-predominant (dystonia without hypomyelination, i.e., DYT-TUBB4A) phenotypes is thought to be downstream and variant-dependent — mutations disrupting the tubulin **autoregulatory 3′ mRNA domain** preferentially derange neuronal tubulin autoregulation (favoring the dystonia phenotype with spared myelination), whereas mutations directly poisoning the **microtubule polymerization interface** (like D249N) preferentially compromise the oligodendrocyte's heavy microtubule-dependent process-extension/myelin-wrapping machinery (favoring H-ABC).

**Cell types involved (Cell Ontology candidates):**
- CL:0000128 (oligodendrocyte) / CL:0000130 (oligodendrocyte precursor cell) — myelination failure
- CL:0000617 (GABAergic neuron) / medium spiny neuron of striatum (CL:1001474) — putaminal neurodegeneration
- CL:0000121 (Purkinje cell) and other cerebellar neuron populations — cerebellar atrophy

**Biological processes involved (GO term candidates):**
- GO:0007017 (microtubule-based process) — modifier: perturbed/dysregulated
- GO:0022010 (central nervous system myelination) — modifier: DECREASED
- GO:0042552 (myelination)
- GO:0031122 (cytoplasmic microtubule organization)
- GO:0006916 / GO:0097194 (apoptotic process / execution phase of apoptosis) for the neurodegeneration arm

**Protein dysfunction:** classified functionally as a partial loss-of-normal-function combined with **dominant-negative/antimorphic gain-of-abnormal-function** — the mutant subunit does not merely fail to work but actively impairs polymer assembly of the mixed wild-type/mutant tubulin pool (steric-block mechanism per the Science Advances 2022 structural study).

**Metabolic changes:** No primary metabolic derangement is described; this is a structural cytoskeletal disorder rather than an enzymopathy.

**Immune system involvement:** Not a primary feature; H-ABC is not classified among the immune-mediated or inflammatory leukodystrophies (contrast with e.g. Aicardi-Goutières or vanishing white matter's secondary immune activation) — no substantial neuroinflammatory literature specific to TUBB4A pathogenesis was identified, though secondary reactive gliosis accompanies neurodegeneration as in most progressive leukodystrophies.

**Tissue damage mechanisms:** progressive **neurodegeneration** (loss of striatal and cerebellar neurons) combined with **developmental hypomyelination/failure of oligodendrocyte maturation** — a dual glial-and-neuronal mechanism, distinguishing HLD6 from purely "failure to myelinate" disorders and from purely neurodegenerative ones.

**Biochemical abnormalities:** aberrant microtubule polymerization kinetics (reduced growth rate, altered dynamic instability parameters) demonstrated by in vitro tubulin polymerization assays and cell-based imaging in the cited structural/functional papers.

**Molecular profiling / advanced technologies:** Model-system transcriptomic and imaging studies (second-harmonic-generation microscopy of myelin ultrastructure, PMC9402540; MRI-based quantitative phenotyping in rat and mouse models) have been used, but comprehensive human single-cell/spatial transcriptomic or multi-omic profiling of HLD6 brain tissue has not been reported (expected given tissue inaccessibility in a pediatric neurodegenerative disease) — most molecular characterization derives from **model organism (mouse, rat) and in vitro biochemical/structural studies**, not from human tissue omics.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** central nervous system (CNS) — cerebral white matter, basal ganglia (putamen specifically), cerebellum.
- **Secondary:** musculoskeletal system (contractures from spasticity/dystonia), gastrointestinal/nutritional systems (dysphagia-related complications), respiratory system (aspiration risk from bulbar dysfunction).
- **Body system:** primarily **nervous system**; secondarily **musculoskeletal**.

**Tissue/cell level:**
- White matter tracts — hypomyelinated oligodendrocyte-myelin units (CL:0000128 oligodendrocyte)
- Putamen — striatal projection/medium spiny neurons
- Cerebellar cortex/vermis — Purkinje and granule cell populations
- UBERON candidates: UBERON:0002420 (basal ganglia), UBERON:0001873 (putamen), UBERON:0002037 (cerebellum), UBERON:0002316 (white matter of CNS), UBERON:0001890 (forebrain)

**Subcellular level:**
- Cytoskeletal microtubules (GO:0005874 microtubule; GO Cellular Component)
- Myelin sheath (GO:0043209 myelin sheath) — as the structural endpoint of oligodendrocyte process extension failure

**Localization/lateralization:** Involvement is **bilateral and relatively symmetric** (typical of a cell-autonomous, systemically expressed structural gene defect) rather than lateralized or focal; putaminal atrophy is classically **bilateral**.

---

## 8. Temporal Development

- **Onset:** Classic H-ABC/D249N — infancy, median ~6 months (range 2 months–4.5 years). Broader spectrum: neonatal-onset severe encephalopathy at one extreme to adult-onset isolated dystonia (DYT-TUBB4A, 2nd–3rd decade) or adult-onset spastic paraplegia/isolated hypomyelination at the other.
- **Onset pattern:** generally **insidious/subacute** developmental stagnation and regression rather than acute presentation, though seizures can present more acutely when they occur.
- **Progression:** **Progressive** in the classic phenotype — accrual of motor, communicative, and feeding disability across the first decade; MRI findings (atrophy) also progress longitudinally, as documented in serial-imaging natural history work (e.g., the taiep rat and human longitudinal cerebellar-sign studies, PMC8317997).
- **Disease course pattern:** progressive/neurodegenerative rather than episodic or relapsing-remitting, though extrapyramidal crises (oculogyric crises, dystonic storms) can punctuate the course episodically against a background of steady decline.
- **Disease duration:** chronic, lifelong; no spontaneous remission is described. Severe cases are associated with reduced life expectancy (feeding/respiratory complications of advanced neurodegeneration), though comprehensive population-level survival statistics are not established given the disease's rarity and recent (2013) molecular delineation.
- **Critical periods:** the developmental window of active CNS myelination (infancy through early childhood) is the period of greatest vulnerability to the oligodendroglial arm of pathology, making early infancy the presumptive therapeutic window for any disease-modifying intervention (relevant to the ASO therapy discussion in §12).

---

## 9. Inheritance and Population

**Epidemiology:**
- HLD6/TUBB4A-related disorders are **ultra-rare**; exact incidence/prevalence figures are not established. Patient-advocacy and clinical sources report **"just over 200 individuals worldwide"** confirmed with a TUBB4A mutation as of the mid-2020s, most identified as young children, with likely underascertainment. H-ABC specifically is reported to constitute roughly **9% of a group of ~30 rare leukodystrophies** studied in aggregate cohorts (per H-ABC/TUBB4A patient-foundation summary).
- No population-based incidence/prevalence rate (cases per 100,000) has been published; this should be curated as `prevalence_class: ULTRA_RARE` / `NOT_YET_DOCUMENTED` in structured terms, citing the qualitative "~200 reported cases" figure with `measure_type: CASES_IN_LITERATURE`.

**Inheritance pattern:** **Autosomal dominant** (HP:0000006). Classic H-ABC (HLD6 proper) is overwhelmingly **de novo** — "most probands represent a simplex case," per GeneReviews. DYT-TUBB4A, by contrast, shows classic multi-generational autosomal dominant transmission with **reduced penetrance**.

**Penetrance:** High/complete for classic de novo H-ABC variants (essentially fully penetrant given consistent phenotype across unrelated de novo cases); **reduced penetrance** is specifically documented for DYT-TUBB4A dystonia variants.

**Expressivity:** **Highly variable** — this is a defining feature of TUBB4A biology: the same gene, and even overlapping variant positions, can produce phenotypes ranging from lethal early-infantile encephalopathy to mild adult-onset isolated dystonia with normal myelination, to intermediate phenotypes (e.g., "Adult-Onset Dystonia with Late-Onset Epilepsy in TUBB4A-Related Hypomyelinating Leukodystrophy—A New Intermediate Phenotype," PMC9350765).

**Genetic anticipation:** Not described/expected — this is not a repeat-expansion disorder.

**Germline mosaicism:** Documented and clinically important — the founding Simons et al. 2013 cohort included a family with **maternal mosaicism** for D249N, explaining the rare instance of sib recurrence despite the variant's otherwise de novo occurrence; this underlies the (low but non-zero) sibling recurrence risk counseling point.

**Founder effects:** No specific population founder effect is described; the D249N hotspot's recurrence across genetically unrelated families from multiple populations (including confirmed independent recurrence in Chinese cohorts) is best explained by mutational hotspot biology (a highly mutable nucleotide context) rather than a shared ancestral founder haplotype.

**Consanguinity:** Not a relevant risk factor — autosomal dominant de novo disease, not recessive.

**Carrier frequency:** Not applicable in the classic sense (dominant de novo disorder, not a recessive carrier state); population database (gnomAD) representation of pathogenic TUBB4A variants is effectively absent.

**Population demographics:**
- **Affected populations:** reported across diverse ethnic/geographic populations (European, Middle Eastern including a Saudi case report [PMC10027483], East Asian/Chinese cohorts) — no clear ethnic predilection; this is consistent with a de novo mutational mechanism rather than population-specific allele enrichment.
- **Geographic distribution:** worldwide, reflecting ascertainment via clinical genetic testing rather than any endemic pattern.
- **Sex ratio:** no strong sex bias reported in the literature reviewed.
- **Age distribution:** skewed toward pediatric ascertainment for classic H-ABC (given infantile onset), with a smaller adult-ascertained subset corresponding to the milder end of the spectrum (isolated hypomyelination, DYT-TUBB4A).

---

## 10. Diagnostics

**Clinical/imaging tests:**
- **Brain MRI** is the central diagnostic modality: the combination of diffuse hypomyelination + putaminal atrophy/disappearance + cerebellar (vermian) atrophy is considered near-pathognomonic for the H-ABC end of the spectrum and is what originally defined the entity (van der Knaap et al. 2002/2007) before its molecular basis was known.
- Serial/longitudinal MRI documents progression of atrophy and is used in natural-history characterization.
- No specific diagnostic laboratory biomarker (blood/CSF metabolite, enzyme assay) exists — unlike metabolic leukodystrophies (e.g., MLD, Krabbe), HLD6 is a structural/cytoskeletal disorder with no biochemical screening analyte.
- Electrophysiology (EEG) is used when seizures are part of the presentation but is not diagnostic of the underlying disorder itself.
- Neuropathology (on rare autopsy/biopsy) has demonstrated combined oligodendroglial loss and neuronal degeneration with microtubule accumulation, corroborating the mouse/rat model findings (e.g., "Severe TUBB4A-Related H-ABC: Novel Neuropathological Findings," PMID:30476126).

**Genetic testing:**
- **Recommended approach (per GeneReviews):** given the phenotype's overlap with other hypomyelinating leukodystrophies, testing typically proceeds via a **leukodystrophy/hypomyelination gene panel** or **exome/genome sequencing**, given genetic heterogeneity among the hypomyelinating leukodystrophies (HLD1–HLD20+, including PLP1, GJC2, POLR3A/B, TUBB4A, and others — see GeneReviews Table 3, "Genetic Differential Diagnosis").
- **Targeted single-gene testing** for the recurrent D249N variant can serve as a **rapid diagnostic assay** when the classic H-ABC MRI phenotype is present — this is explicitly described in "A recurrent TUBB4A mutation in hypomyelinating leukodystrophy: A rapid diagnostic assay" (PMID:32595021), which developed a targeted assay given how frequently the same hotspot variant recurs.
- **Whole-exome/whole-genome sequencing**, often as trio analysis, is the primary route by which most cases (including the founding cohort and subsequent isolated case reports, e.g., the Saudi child, PMC10027483) have been diagnosed, given the phenotypic overlap with other leukodystrophies and lack of an a priori candidate gene in unselected referrals ("Genetic analysis of 20 patients with hypomyelinating leukodystrophy by trio-based whole-exome sequencing," *J Hum Genet* 2020).
- **Chromosomal microarray/karyotype:** not diagnostic (point-mutation disorder), but often performed as part of the standard leukodystrophy diagnostic workup to exclude other etiologies before/alongside sequencing.
- **Mitochondrial DNA testing, repeat-expansion testing:** not applicable to this disorder's mechanism but frequently part of the differential-diagnosis workup for hypomyelinating leukodystrophy in general.

**Clinical diagnostic criteria:** No formal consensus diagnostic scoring system exists; diagnosis rests on the combination of (1) characteristic MRI pattern, (2) compatible clinical course, and (3) confirmatory molecular genetic testing.

**Differential diagnosis:** Other hypomyelinating leukodystrophies (Pelizaeus-Merzbacher disease/HLD1-*PLP1*, HLD2-*GJC2*, POLR3-related leukodystrophy/HLD7-8, *TMEM106B*-related HLD16, *FAM126A*-related HLD5), and disorders producing basal ganglia + cerebellar atrophy on MRI more broadly. GeneReviews Table 3 provides the structured genetic differential diagnosis list.

**Screening:** No population newborn-screening or carrier-screening program exists for this ultra-rare, predominantly de novo disorder; prenatal diagnosis is offered on a case-by-case basis in families with a known familial variant (relevant chiefly to DYT-TUBB4A families or documented parental mosaicism).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No population-level survival statistics (5-year/10-year rates) are published, consistent with the disorder's rarity and recent characterization; severe classic H-ABC cases are associated with substantial morbidity and presumed reduced life expectancy from complications of advanced neurodegeneration (aspiration, respiratory compromise), though quantitative mortality data were not identified in the literature reviewed.
- **Disease course:** progressive functional decline — feeding difficulties, loss of communication ability, and loss of ambulation typically occur "before the end of the first decade of life" in the classic D249N-associated phenotype.
- **Morbidity/function:** major motor disability (loss of independent ambulation), communication impairment, and in many, cognitive decline; a subset of patients on the milder end of the spectrum can retain near-normal cognitive function.
- **Complications:** contractures, dystonic crises/storms, aspiration pneumonia risk from bulbar dysfunction, seizures (a subset), nutritional compromise requiring gastrostomy in advanced cases.
- **Recovery potential:** the disease is neurodegenerative and progressive; spontaneous recovery is not described. No disease-modifying therapy is currently approved (see §12), so "recovery" in the classic sense is not part of the natural history; symptomatic interventions (e.g., botulinum toxin, deep brain stimulation for the dystonia component) can improve specific symptoms without altering the underlying trajectory.
- **Prognostic factors:** phenotype severity correlates with variant location/mechanism (polymerization-interface variants → more severe H-ABC-type courses; autoregulatory-domain variants → milder, dystonia-predominant courses with preserved myelination) and, in mouse allelic-series studies, with the **relative dose of mutant versus wild-type Tubb4a expression** — "disease severity correlates with the expression of mutant Tubb4a and relative preservation of wild-type tubulin" (bioRxiv/Molecular Therapy ASO paper, 2024–2026).
- **Prognostic biomarkers:** none validated in humans; MRI-based longitudinal atrophy metrics are used as natural-history/therapeutic outcome measures in research settings rather than as formal prognostic biomarkers.

---

## 12. Treatment

**Current standard of care is entirely supportive/symptomatic; there is no approved disease-modifying or curative therapy for HLD6/H-ABC.**

**Pharmacotherapy (symptomatic):**
- **Botulinum toxin injections** for severe focal/segmental dystonia — reported as periodic (e.g., twice yearly) symptomatic management (NCIT:C1332 Botulinum Toxin, under NCIT:C15986 Pharmacotherapy).
- **Levodopa/carbidopa** trialed for abnormal movements in individual case reports with reported responsiveness (Neurology abstract, "A case of TUBB4A-related hypomyelinating leukodystrophy with abnormal movements responsive to levodopa/carbidopa").
- Anti-seizure medications for the subset with epilepsy (standard antiepileptic pharmacotherapy, not disease-specific).
- General spasticity management (e.g., baclofen, tizanidine) as used in other spastic leukodystrophies, though not specifically studied in controlled HLD6 trials.

**Device/interventional:**
- **Bipallidal deep brain stimulation (DBS)** has been reported effective for medically refractory dystonia/whispering dysphonia in TUBB4A-related disorders (PMID:33084096, "Whispering dysphonia in TUBB4A-related disorders responsive to bipallidal deep brain stimulation") — NCIT term candidate: Deep Brain Stimulation procedure, under `therapeutic_modality: DEVICE`.

**Rehabilitative/supportive:**
- Physical therapy, occupational therapy, speech/communication therapy (augmentative and alternative communication), and nutritional support (including gastrostomy feeding when dysphagia is significant) — standard supportive-care measures for progressive pediatric neurodegenerative leukodystrophy (NCIT:C15302 Physical Therapy; NCIT:C15747 Supportive Care).

**Experimental / disease-modifying (preclinical):**
- **Antisense oligonucleotide (ASO) gene-suppression therapy** targeting *Tubb4a* transcript reduction is the most advanced disease-modifying approach in development, reported in "Therapeutic suppression of *Tubb4a* rescues H-ABC leukodystrophy" (PMID:41566774, *Molecular Therapy*, 2026; preprint bioRxiv 2024.08.27.609903): *"a well-tolerated Tubb4a-targeted antisense oligonucleotide (ASO) candidate that selectively reduces Tubb4a"* was identified, and *"single intracerebroventricular administration of ASO in postnatal Tubb4a^D249N/KO mice drastically extends lifespan, improves motor phenotypes, and reduces seizures."* This is a `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`, `aso_mechanism: RNASE_H_KNOCKDOWN`-type approach (allele-nonselective transcript suppression rather than splice modulation), directly analogous in strategy to nusinersen for SMA but not yet in human trials — this represents the module `target_mechanisms` candidate: an ASO `INHIBITS`/reduces the "Mutant TUBB4A Incorporation into Microtubules" trigger node.
- **4-Aminopyridine** improved evoked potentials and ambulation in the taiep rat model (a potassium-channel blocker strategy analogous to its use in multiple sclerosis for conduction improvement) — preclinical only (PMC10906851).

**Clinical trials:** No disease-specific interventional trial (NCT) for a TUBB4A-targeted disease-modifying therapy was identified as currently registered/recruiting in the sources reviewed; the ASO work remains preclinical (mouse model stage) as of the 2026 publication. A **Natural History Study** infrastructure exists for the broader leukodystrophy/tubulinopathy space (e.g., adjacent tubulinopathy natural-history protocols referenced via ClinicalTrials.gov, though not TUBB4A-specific in the sources found) — natural history data collection (e.g., via the H-ABC/TUBB4A patient foundation) is a precursor to future interventional trial readiness.

**Treatment strategy:** No formal treatment algorithm exists; management follows general symptomatic/palliative principles for progressive pediatric leukodystrophy, individualized to the dominant symptom domain (dystonia vs. spasticity vs. seizures vs. nutritional/respiratory complications), coordinated through multidisciplinary neurology, physiatry, genetics, and palliative-care teams.

---

## 13. Prevention

There is **no primary prevention** strategy for HLD6, as it arises overwhelmingly from de novo germline mutation with no known environmental or modifiable risk factor.

- **Genetic counseling:** the principal "preventive" intervention available is **genetic counseling** regarding recurrence risk — low but non-zero due to possible parental germline/somatic mosaicism, as documented in the founding cohort. Prenatal diagnosis or preimplantation genetic testing can be offered to families with an identified pathogenic variant, particularly where parental mosaicism is suspected or confirmed, or in DYT-TUBB4A families with dominant transmission.
- **Secondary prevention:** early diagnosis via MRI pattern recognition and confirmatory genetic testing allows earlier initiation of supportive therapies (PT/OT/speech, nutritional planning, seizure management) to mitigate secondary complications, though this does not alter the underlying neurodegenerative trajectory absent a disease-modifying therapy.
- **Tertiary prevention:** proactive management of aspiration risk (dysphagia screening, gastrostomy planning), contracture prevention (physical therapy, orthotics, botulinum toxin), and seizure control aims to reduce disease-related complications and improve quality of life.
- No immunization, screening program, public-health, or environmental-intervention strategy is applicable to this disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy of relevant model species:** *Mus musculus* (NCBITaxon:10090), *Rattus norvegicus* (NCBITaxon:10116).
- **Naturally occurring disease — the *taiep* rat:** A **spontaneously arising, naturally occurring recessive *Tubb4a* mutant rat model** (the "*taiep*" rat — named for its sequential phenotype of Tremor, Ataxia, Immobility, Epilepsy, Paralysis) carries a homozygous **p.Ala302Thr** *Tubb4a* mutation, arising spontaneously during inbreeding of a Sprague-Dawley subline. This is described as *"the first animal model of TUBB4 mutations in humans"* and *"shows clinical, radiological, and pathological signs like those of the human leukodystrophy hypomyelination with atrophy of the basal ganglia and cerebellum (H-ABC)"* — with initial hypomyelination followed by progressive demyelination and microtubule accumulation in oligodendrocytes (Duncan lab work, PMID:28393430). This is a genuine **naturally occurring veterinary-relevant tubulinopathy** rather than an engineered model, giving it particular translational value.
- **Orthologous gene:** rat *Tubb4a* (RGD gene ID applicable), mouse *Tubb4a* (MGI gene ID applicable) — both highly conserved orthologs of human *TUBB4A*.
- **Comparative pathology:** the *taiep* rat and engineered mouse knock-in models recapitulate the core dual pathology of human H-ABC — oligodendrocyte/myelination failure plus neuronal microtubule dysfunction — supporting strong evolutionary conservation of the disease mechanism across mammals.
- **Zoonotic potential / cross-species transmission:** not applicable — this is a non-infectious, genetic structural disorder.

---

## 15. Model Organisms

**Rodent genetic models (the dominant model system for this disease):**

1. ***Tubb4a*^D249N knock-in mouse allelic series** — the most disease-relevant engineered model, comprising *Tubb4a*^KO/KO (null), *Tubb4a*^D249N/+ (heterozygous, modeling the human dosage), *Tubb4a*^D249N/KO (hemizygous mutant, no wild-type allele), and *Tubb4a*^D249N/D249N (homozygous mutant) genotypes, used to dissect **dose-dependency between mutant expression and wild-type tubulin preservation** as the key determinant of severity (eLife 2020, PMID:32463361; used again as the therapeutic model in the 2024–2026 ASO rescue study).
   - **Phenotype recapitulation:** demonstrates both glial (oligodendrocyte loss, hypomyelination) and neuronal degeneration, closely mirroring the dual human pathology; the D249N/KO genotype (short life expectancy, myelination deficits, motor phenotypes, seizures) is used as the "severe" therapeutic-testing model.
   - **Model limitations:** as with most mouse leukodystrophy models, developmental/behavioral timelines and CNS myelination kinetics differ from humans, and full recapitulation of human cognitive/communicative decline is not directly assessable in rodents.
2. ***taiep* rat** (spontaneous p.Ala302Thr homozygous mutant) — see §14. Used for MRI natural-history characterization (PMC7284052, "MRI Features in a Rat Model of H-ABC Tubulinopathy"), longitudinal cerebellar-sign correlation with the human disease (PMC8317997), ultrastructural myelin imaging (PMC9402540, second-harmonic-generation microscopy), and pharmacological testing (4-aminopyridine, PMC10906851).
   - **Applications:** natural history modeling, imaging biomarker development, and small-molecule/electrophysiological intervention testing.

**Induced/other models:** No major non-rodent model system (zebrafish, *Drosophila*, *C. elegans*, iPSC-derived organoid) for TUBB4A/HLD6 specifically was identified in this search, though iPSC-derived oligodendrocyte differentiation assays would be a plausible and valuable future in vitro system given the emphasis on oligodendrocyte-lineage-specific dysfunction in the mechanistic literature.

**Model databases relevant to follow-up:** MGI (mouse *Tubb4a* allele records), RGD (rat *Tubb4a*/*taiep* strain records), IMSR (strain repository lookup for *Tubb4a* knock-in lines).

---

## Summary Table of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | OMIM:612438; MedGen:C2676244 |
| Gene | hgnc:20773 (TUBB4A) |
| Causal variant | c.745G>A p.(Asp249Asn), ClinVar-classified Pathogenic |
| Inheritance | HP:0000006 (Autosomal dominant) |
| Key phenotypes | HP:0002188 (Delayed CNS myelination), HP:0002062 (basal ganglia/putaminal atrophy), HP:0001272 (Cerebellar atrophy), HP:0001332 (Dystonia), HP:0002510 (Spastic tetraplegia), HP:0001251 (Ataxia), HP:0001250 (Seizure), HP:0002505 (Loss of ambulation) |
| Cell types | CL:0000128 (oligodendrocyte), CL:0000130 (OPC), medium spiny neuron, Purkinje cell |
| Biological process | GO:0007017 (microtubule-based process), GO:0022010 (CNS myelination) |
| Anatomy | UBERON:0001873 (putamen), UBERON:0002037 (cerebellum), UBERON:0002316 (CNS white matter) |
| Treatment (symptomatic) | NCIT:C15986 (Pharmacotherapy) + botulinum toxin agent; Deep Brain Stimulation device procedure |
| Treatment (experimental) | ANTISENSE_OLIGONUCLEOTIDE modality, RNase-H knockdown mechanism, target_gene TUBB4A |

---

## Key Primary Citations

- Simons C, et al. "A de novo mutation in the β-tubulin gene TUBB4A results in the leukoencephalopathy hypomyelination with atrophy of the basal ganglia and cerebellum." *Am J Hum Genet.* 2013;92:767–773. **PMID:23746550**
- Duncan ID, et al. / Simons et al. "Hypomyelination with atrophy of the basal ganglia and cerebellum: further delineation of the phenotype and genotype–phenotype correlation." *Brain.* 2014;137:1921–1930.
- Hersheson J, et al. "Mutations in the autoregulatory domain of β-tubulin 4a cause hereditary dystonia." *Ann Neurol.* 2013.
- Lohmann K, et al. "Whispering dysphonia (DYT4 dystonia) is caused by a mutation in the TUBB4 gene." *Ann Neurol.* 2013. **PMID:23595291**
- Curiel J, et al. "TUBB4A mutations result in specific neuronal and oligodendrocytic defects that closely match clinically distinct phenotypes." *Hum Mol Genet.* 2017. **PMID:28973395**
- Duncan ID, et al. "A mutation in the Tubb4a gene leads to microtubule accumulation with hypomyelination and demyelination." (*taiep* rat) 2017. **PMID:28393430**
- "TUBB4A mutations result in both glial and neuronal degeneration in an H-ABC leukodystrophy mouse model." *eLife.* 2020. **PMID:32463361**
- "H-ABC– and dystonia-causing TUBB4A mutations show distinct pathogenic effects." *Science Advances.* 2022. **PMID:35275727**
- "A recurrent TUBB4A mutation in hypomyelinating leukodystrophy: A rapid diagnostic assay." 2020. **PMID:32595021**
- "Therapeutic suppression of *Tubb4a* rescues H-ABC leukodystrophy." *Molecular Therapy.* 2026. **PMID:41566774**
- Simons C, Wolf NI, van der Knaap MS. "TUBB4A-Related Neurologic Disorders." *GeneReviews®* [Internet]. NCBI Bookshelf NBK395611.
- "Whispering dysphonia in TUBB4A-related disorders responsive to bipallidal deep brain stimulation." **PMID:33084096**

Sources:
- [Entry - #617964 - LEUKODYSTROPHY, HYPOMYELINATING, 16; HLD16 - OMIM](https://omim.org/entry/617964)
- [612438 - LEUKODYSTROPHY, HYPOMYELINATING, 6 - OMIM](https://omim.org/entry/612438)
- [A recurrent de novo mutation in TMEM106B causes hypomyelinating leukodystrophy | Brain](https://academic.oup.com/brain/article/140/12/3105/4654492)
- [TMEM106B and myelination: rare leukodystrophy families reveal unexpected connections - PubMed](https://pubmed.ncbi.nlm.nih.gov/29194508/)
- [Entry - *602662 - TUBULIN, BETA-4A; TUBB4A - OMIM](https://omim.org/entry/602662)
- [Data on the effect of hypomyelinating leukodystrophy 6 (HLD6)-associated mutations on the TUBB4A properties - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5328720/)
- [TUBB4A mutations result in both glial and neuronal degeneration in an H-ABC leukodystrophy mouse model - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7255805/)
- [Hypomyelination with atrophy of the basal ganglia and cerebellum: further delineation of the phenotype and genotype–phenotype correlation | Brain](https://academic.oup.com/brain/article-abstract/137/7/1921/2847795)
- [Severe TUBB4A-Related Hypomyelination With Atrophy of the Basal Ganglia and Cerebellum: Novel Neuropathological Findings - PubMed](https://pubmed.ncbi.nlm.nih.gov/30476126/)
- [TUBB4A-related hypomyelinating leukodystrophy: New insights from a series of 12 patients - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1090379815001890)
- [A De Novo Mutation in the β-Tubulin Gene TUBB4A Results in the Leukoencephalopathy H-ABC - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002929713001262)
- [TUBB4A-Related Leukodystrophy - GeneReviews - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/sites/books/NBK395611/)
- [TUBB4A mutations result in specific neuronal and oligodendrocytic defects that closely match clinically distinct phenotypes - PubMed](https://pubmed.ncbi.nlm.nih.gov/28973395/)
- [Expanding the phenotypic spectrum of TUBB4A-associated hypomyelinating leukoencephalopathies | Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000000535)
- [The natural history of variable subtypes in pediatric-onset TUBB4A-related leukodystrophy - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1096719225000393)
- [H-ABC– and dystonia-causing TUBB4A mutations show distinct pathogenic effects | Science Advances](https://www.science.org/doi/10.1126/sciadv.abj9229)
- [A mutation in the Tubb4a gene leads to microtubule accumulation with hypomyelination and demyelination - PubMed](https://pubmed.ncbi.nlm.nih.gov/28393430/)
- [Therapeutic suppression of Tubb4a rescues H-ABC leukodystrophy - PubMed](https://pubmed.ncbi.nlm.nih.gov/41566774/)
- [Therapeutic suppression of Tubb4a rescues H-ABC leukodystrophy | bioRxiv](https://www.biorxiv.org/content/10.1101/2024.08.27.609903v1)
- [Physician's Corner - Foundation to Fight H-ABC / TUBB4A](https://www.h-abc.org/physicians)
- [TUBB4A de novo mutations cause isolated hypomyelination - PubMed](https://pubmed.ncbi.nlm.nih.gov/25085639/)
- [Genetic analysis of 20 patients with hypomyelinating leukodystrophy by trio-based whole-exome sequencing | Journal of Human Genetics](https://www.nature.com/articles/s10038-020-00896-5)
- [TUBB4A-related leukodystrophy - MedlinePlus](https://medlineplus.gov/download/genetics/condition/tubb4a-related-leukodystrophy.pdf)
- [Cross-sectional quantitative analysis of the natural history of TUBA1A and TUBB2B tubulinopathies | Genetics in Medicine](https://www.nature.com/articles/s41436-020-01001-z)
- [H-ABC tubulinopathy revealed by label-free second harmonic generation microscopy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9402540/)
- [Whispering dysphonia (DYT4 dystonia) is caused by a mutation in the TUBB4 gene - PubMed](https://pubmed.ncbi.nlm.nih.gov/23595291/)
- [DYSTONIA 4, TORSION, AUTOSOMAL DOMINANT; DYT4 - OMIM](https://omim.org/entry/128101)
- [Whispering dysphonia in TUBB4A-related disorders responsive to bipallidal deep brain stimulation - PubMed](https://pubmed.ncbi.nlm.nih.gov/33084096/)
- [Adult-Onset Dystonia with Late-Onset Epilepsy in TUBB4A-Related Hypomyelinating Leukodystrophy—A New Intermediate Phenotype - PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC9350765)
- [The myelin mutant taiep rat as a model for developmental brain disorders - ScienceDirect](https://www.sciencedirect.com/science/article/pii/B978012817988800049X)
- [MRI Features in a Rat Model of H-ABC Tubulinopathy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7284052/)
- [4-aminopyridine improves evoked potentials and ambulation in the taiep rat - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10906851/)
- [Longitudinal Evaluation of Cerebellar Signs of H-ABC Tubulinopathy in a Patient and in the taiep Model - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8317997/)
- [Hypomyelinating leukodystrophy 6 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2676244/)
- [Hypomyelinating leukodystrophy 6 (Concept Id: C2676244) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/436642)
- [TUBB4A-associated leukodystrophy - Open Access Government](https://www.openaccessgovernment.org/leukodystrophy/124977/)
- [What is H-ABC/TUBB4A Leukodystrophy? | H-ABC/TUBB4A](https://www.h-abc.org/habc-tubb4a)
- [A TUBB4A Met363Thr variant in pediatric hypomyelination without atrophy of the basal ganglia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9166743/)
- [hypomyelinating leukodystrophy 6 - National Organization for Rare Disorders](https://rarediseases.org/mondo-disease/hypomyelinating-leukodystrophy-6/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 9 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 7 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32595021` *(abstract only)*: "A recurrent TUBB4A mutation in hypomyelinating leukodystrophy: A rapid diagnostic assay"
  - closest text in source: "Recently, a recurrent de novo mutation in TMEM106B was identified to be responsible for five cases of HLD"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11828475` (1 mention) - Dynamic deconvolution of a pre-equilibrated dynamic combinatorial library of acetylcholinesterase inhibitors.
  - shared terms: none

Weighed against this report's own most characteristic terms: `tubb4a`, `phenotype`, `h-abc`, `disease`, `disorder`, `hld6`, `leukodystrophy`, `dystonia`, `variant`, `atrophy`, `myelination`, `hypomyelination`, `d249n`, `classic`, `dyt-tubb4a`, `novo`, `seizure`, `severe`, `genetic`, `gene`.
