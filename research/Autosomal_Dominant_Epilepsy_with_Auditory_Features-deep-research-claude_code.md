---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T00:48:40.656734'
end_time: '2026-08-05T01:03:55.566310'
duration_seconds: 914.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Epilepsy with Auditory Features
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 11
  num_turns: 63
  total_cost_usd: 6.2663445
  session_id: 4dc9ceb2-9356-4fb8-818e-99b907393b6a
  stop_reason: end_turn
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Epilepsy with Auditory Features
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Epilepsy with Auditory Features** covering all of the
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

# Autosomal Dominant Epilepsy with Auditory Features (ADEAF) — Research Report

**Prepared:** 2026-08-05 · **Target MONDO:** `MONDO:0010898` · **Category:** Mendelian (focal epilepsy syndrome)

A note before diving in: the evidence base here is unusually clean-edged for a rare disease. One syndrome, one very characteristic aura, three genes that all converge — from three quite different directions — on the same secreted-protein-holds-the-synapse-together story. Where a claim comes from a GeneReviews table rather than a PubMed abstract, I flag it, because those sentences will *not* survive `just validate-references` and need re-quoting from the primary paper.

---

## 1. Disease Information

### Overview

ADEAF is a familial focal (lateral temporal lobe) epilepsy in which the defining ictal event is a sound that isn't there — a buzz, a ring, a voice, a song — sometimes accompanied or replaced by a sudden inability to *understand* speech while the person is otherwise fully alert. Brains are structurally normal, development is normal, and most people do well on standard antiseizure medication. Onset is typically adolescence/early adulthood.

GeneReviews defines it as a focal epilepsy syndrome characterized by auditory symptoms and/or receptive aphasia as "prominent ictal manifestations," with normal brain development (Michelucci R, Pasini E, Nobile C, Ottman R. *Autosomal Dominant Epilepsy with Auditory Features*. GeneReviews®, NCBI Bookshelf NBK1537, PMID:20301709).

The 2022 ILAE nosology retains ADEAF as a named syndrome under "epilepsy syndromes with onset at a variable age" (Riney K et al., *Epilepsia* 2022;63:1443–1474, doi:10.1111/epi.17240). Recent literature increasingly uses the etiology-agnostic term **epilepsy with auditory features (EAF)** to cover sporadic and non-Mendelian cases: the name shift happened "to acknowledge this entity also in a non-familial context/pattern" (Furia A et al., *Front Neurol* 2022;12:807939, PMID:35153984).

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | `MONDO:0010898` — autosomal dominant epilepsy with auditory features |
| Orphanet | `ORPHA:101046` |
| OMIM (LGI1) | **600512** — EPILEPSY, FAMILIAL TEMPORAL LOBE, 1 (ETL1) |
| OMIM (RELN) | **616436** — EPILEPSY, FAMILIAL TEMPORAL LOBE, 7 (ETL7) |
| OMIM (MICAL1) | gene MIM **607129**; *no separate ETL phenotype number assigned* — note ETL8 (616461) is **GAL**-related, not MICAL1 (verified via MedGen). Do not mis-map this. |
| MeSH | `C537297` |
| MedGen | `325326` |
| UMLS | `C1838062` |
| GARD | `0002257` |
| ICD-11 | foundation id `832717248` (MONDO xref); classified under focal epilepsies (8A61.x) |
| ICD-10 | no dedicated code; typically coded G40.2 / G40.1 (localization-related epilepsy) — **approximation, verify before curating** |

MONDO parents: `MONDO:0017704` familial partial epilepsy; `MONDO:0800496` epilepsy with auditory features.

### Synonyms (verbatim from the MONDO record)

ADEAF · ADLTE · ADPEAF · "autosomal dominant lateral temporal lobe epilepsy" · "autosomal dominant partial epilepsy with auditory features" · "partial epilepsy with auditory aura" · "partial epilepsy with auditory features" · "adolescent/adult onset autosomal dominant epilepsy with auditory features."

### Level of evidence

Everything below is **disease-level aggregated** (family series, multi-center cohorts, registries, GeneReviews) plus mechanistic work in mice/cells. There is no EHR-derived individual-patient resource for ADEAF; the largest clinical series (Bisulli 2018, n=123) is a single-center tertiary referral cohort, which biases toward more severe/refractory cases.

---

## 2. Etiology

### Causal factors

Monoallelic (heterozygous) pathogenic variants in one of three genes, all encoding **secreted or secretion-dependent proteins** rather than ion channels — which was the surprise in 2002:

> "Most inherited forms of epilepsy result from mutations in ion channels. However, one form of epilepsy, autosomal dominant partial epilepsy with auditory features…" (Fukata Y et al., *Science* 2006;313:1792–5, PMID:16990550)

| Gene | HGNC | Locus | Protein | Share of ADEAF families | Mechanism |
|---|---|---|---|---|---|
| **LGI1** | `hgnc:6572` | 10q23.33 | Leucine-rich glioma inactivated 1 (epitempin) | ~30% (Italian series); ~50% of large multigenerational pedigrees | Loss of function / haploinsufficiency |
| **RELN** | `hgnc:9957` | 7q22.1 | Reelin | 7/40 = **17.5%** | Loss of function via impaired secretion |
| **MICAL1** | `hgnc:20619` | 6q21 | MICAL-1 monooxygenase | 2 families (~5–7%) | **Gain of function** (↑ oxidoreductase activity) |
| Unsolved | — | — | — | ~50% | Unknown |

Verbatim (Dazzo E et al., *Am J Hum Genet* 2015;96:992–1000, PMID:26046367):
> "Overall, RELN mutations occurred in 7/40 (17.5%) ADLTE-affected families."
> "ADLTE is genetically heterogeneous, and mutations in LGI1 account for fewer than 50% of affected families."

**Critical caveat on yield.** Those family-based percentages are *not* the diagnostic yield in an unselected clinic population. In the largest genotyped EAF cohort (Bisulli F et al., *Seizure* 2021;85:115–118, PMID:33453592; 112 unrelated probands, 29.5% familial):
> "We identified a genetic diagnosis for 8% of our cohort, including pathogenic/likely pathogenic variants (4/8 novel) in LGI1 (2.7%, CI: 0.6-7.6); RELN (1.8%; CI: 0.2-6.3); SCN1A (2.7%; CI: 0.6-7.6) and DEPDC5 (0.9%; CI 0-4.9)."
> "This study shows that the contribution of each of the known genes to the overall disorder is limited and that the genetic background of EAF is still largely unknown."

**Secondary / emerging genes in EAF pedigrees** (not classical ADEAF genes; phenotypically heterogeneous families): *DEPDC5* (`hgnc:18423`), *SCN1A* (`hgnc:10585`), *CNTNAP2* (`hgnc:13830`) — Pippucci T et al., *Neurol Genet* 2015;1:e5, PMID:27066544. And newly, *KCNQ2* (`hgnc:6296`): a family segregating c.2251T>G presented with "epilepsy with auditory features (EAFs), focal epilepsy, and generalized epilepsy, and none of them suffered from neonatal seizures," leading the authors to "unveil… the prospect of its inclusion in screening panels for EAFs" (Talarico M et al., *Int J Mol Sci* 2024;26:295, PMID:39796146).

### Risk factors

- **Genetic:** carrying a heterozygous pathogenic *LGI1*/*RELN*/*MICAL1* variant. Family history of epilepsy is the dominant risk descriptor. No validated common-variant susceptibility loci specific to ADEAF (no dedicated GWAS; the syndrome is too rare).
- **Environmental:** none established as causing the disease. **Sound is a seizure *trigger*, not a cause** — reflex seizures precipitated by sudden noises (telephone, doorbell) in 8–13% of affected individuals (GeneReviews Table 2); "seizures were precipitated by environmental noises in 8% of patients" in RELN families (Michelucci R et al., *Epilepsy Behav* 2017;68:103–107, PMID:28142128).
- **Age/sex:** no sex effect on penetrance — "Penetrance did not differ by gender" (Rosanoff MJ, Ottman R, *Neurology* 2008;71:567–71, PMID:18711109). Sex ratio in the largest EAF series was 58 M / 65 F (Bisulli 2018, PMID:29464704).

### Protective factors

No genetic or environmental protective factors are documented. **Not available for this disease.** (Speculatively, residual protein secretion level is protective — see §4 dose-response — but that's a modifier of severity, not a population protective factor.)

### Gene–environment interactions

The only well-described G×E is **sound-triggered reflex seizure susceptibility** in mutation carriers — an environmental stimulus (auditory input to a genetically hyperexcitable lateral temporal cortex) precipitating events. Sleep is a second permissive state: seizures "frequently occur during sleep" (Furia 2022, PMID:35153984). Beyond that: **no data.**

---

## 3. Phenotypes

Frequencies below are from GeneReviews Table 2 (ranges reflect different published series) unless a primary PMID is given. **Note for curation:** GeneReviews prose is not a PubMed abstract and will fail snippet validation — re-source each frequency from Ottman 2004 / Michelucci 2017 / Bisulli 2018 / Ho 2012 before writing evidence blocks.

| Phenotype | Frequency | HPO term (all verified against local `sqlite:obo:hp`) |
|---|---|---|
| Focal sensory seizure with auditory features (aura) | 57–71% overall; 80% in LRR-domain / missense carriers; **71%** in RELN families (PMID:28142128) | `HP:0011158` Focal sensory seizure with auditory features |
| — aware variant | — | `HP:0032864` Focal aware sensory seizure with auditory features |
| — with impaired awareness | — | `HP:0032880` Focal impaired awareness sensory seizure with auditory features |
| Ictal receptive aphasia | 17–20%; ~⅓ of RELN patients had aphasia among associated symptoms | `HP:0032696` Focal cognitive seizure with receptive dysphasia/aphasia; `HP:0032710` (aware variant); `HP:0033848` Receptive aphasia |
| Focal to bilateral tonic-clonic seizures | 88–92%; **88%** in RELN families, preceded by aura in 67% | `HP:0007334` Bilateral tonic-clonic seizure with focal onset |
| Focal aware / focal impaired awareness seizures | near-universal accompaniment | `HP:0002349`, `HP:0002384` |
| Reflex seizures triggered by sudden sound | 8–13% (8% in RELN families) | `HP:0020207` Reflex seizure — **ontology gap:** HPO has `HP:0020214` Startle-induced and `HP:0032896` Music-induced, but **no generic sound-induced seizure term**. Worth an HPO term request. |
| Visual ictal symptoms | minority | `HP:0011165` Focal sensory seizure with visual features |
| Olfactory ictal symptoms | minority | `HP:0011161` |
| Vertiginous symptoms | minority | `HP:0002321` Vertigo |
| Déjà vu / psychic symptoms | less common (helps separate from mesial TLE) | `HP:0032704` Focal aware cognitive seizure with illusion (**verify fit**) |
| Autonomic symptoms | *less* frequent in mutation-positive families (PMID:15079011) | `HP:0011154` Focal autonomic seizure |
| Interictal epileptiform EEG abnormality | 57–80%; **80%** in RELN families, temporal, left-predominant | `HP:0011182` Interictal epileptiform activity; `HP:0002353` EEG abnormality |
| Normal brain MRI | typical/mandatory | no HP term (absence of finding) — record as a diagnostic criterion, not a phenotype |

Winawer's phenotype-defining paper is the cleanest primary quote for the aura spectrum (Winawer MR et al., *Neurology* 2000;54:2173–6, PMID:10851389):
> "Auditory hallucinations were most common, but other sensory symptoms (visual, olfactory, vertiginous, and cephalic) were also reported. Autonomic, psychic, and motor symptoms were less common. The clinical semiology points to a lateral temporal seizure origin."

Auditory quality (Ottman R et al., *Neurology* 2004;62:1120–6, PMID:15079011):
> "In families with mutations, the most common auditory symptom type was simple, unformed sounds (e.g., buzzing and ringing)."

Simple (humming/buzzing/ringing, tinnitus-like) vs complex (voices, music, specific songs) vs **distortions** (volume change) vs **negative** (sudden disappearance of ambient sound) — the simple/complex/distortion split matters prognostically (§11).

### Phenotype characteristics

- **Onset:** adolescence/early adulthood, "age 10–30 years" typical, reported range 4–50 years (GeneReviews). Mean onset **20 years** in RELN families (PMID:28142128).
- **Severity:** mild-to-moderate in most; a minority is refractory. Highly variable even within a family.
- **Progression:** episodic/non-progressive. No neurodegeneration, no intellectual decline (moderate/severe ID is an ILAE *exclusion* criterion).
- **Frequency of events:** FBTCS often only once or twice a year; auras can be much more frequent.
- **Quality of life:** no ADEAF-specific EQ-5D/SF-36/PROMIS study exists. **Not available.** Real-world impact is driven by driving restrictions, FBTCS unpredictability, and the socially isolating weirdness of auditory auras (often misread as psychiatric). Behavioral problems, depression with suicide attempts, and migraine have been reported in isolated pedigrees, but systematic study attributed depression to epilepsy/medication rather than shared genetic susceptibility (GeneReviews).

---

## 4. Genetic / Molecular Information

### LGI1 (`hgnc:6572`, 10q23.33; protein O95970, "epitempin")

Discovery (Kalachikov S et al., *Nat Genet* 2002;30:335–41, PMID:11810107):
> "Here we describe identification of the causative gene in autosomal-dominant partial epilepsy with auditory features (ADPEAF, MIM 600512), a rare form of idiopathic lateral temporal lobe epilepsy characterized by partial seizures with auditory disturbances."
> "…identifying presumptive mutations in one copy of the leucine-rich, glioma-inactivated 1 gene (LGI1) in each of five families with ADPEAF."

Prior linkage: 10q22-24 / 10q24 (Winawer MR et al., *Epilepsia* 2002;43:60–7, PMID:11879388 — "maximum multipoint LOD score of 2.93").

- **Variant types:** >40 reported pathogenic variants; roughly ⅓ truncating (nonsense/frameshift/splice → NMD), the rest missense. Sequence analysis detects ~95%; exon-level del/dup ~5% (GeneReviews).
- **Domain architecture & clustering:** N-terminal leucine-rich repeat (LRR) domain + C-terminal EPTP/epitempin seven-bladed β-propeller. Mutations cluster in the LRR (Ho YY, Ionita-Laza I, Ottman R, *Neurology* 2012;78:563–8, PMID:22323750): "ADPEAF-causing mutations clustered significantly in the LRR domain (exons 3-5) of LGI1 (p = 0.026)."
- **Functional consequence:** loss of function. Two flavors — **secretion-defective** (majority; misfolded protein retained and degraded by ER quality control) and **secretion-positive but binding-defective** (e.g. S473L, R474Q, E383A) which reach the extracellular space but fail to engage ADAM22/23.
- **Constraint (gnomAD API, GRCh38):** pLI ≈ **1.000**, observed/expected LoF = **0.190** (11 observed vs 57.7 expected), LOEUF = **0.315**, missense Z = 3.98. Textbook haploinsufficiency signature.
- **Somatic vs germline:** germline. (Biallelic *somatic* LGI1 loss is a glioma phenomenon — "loss of both copies of LGI1 promotes glial tumor progression," PMID:11810107 — but that is a separate, tumor-suppressor context and should not be conflated with ADEAF.)
- **De novo:** ~1% of ADEAF (GeneReviews); a de novo LGI1 variant was found in a Turkish LTLE-with-auditory-aura cohort (PMID:26773249).

**Allelic spectrum extension (2025, important and new).** Biallelic LGI1 variants cause a far more severe disease (Hirano Y et al., *Brain* 2025;148:3514–3522, PMID:40455867, doi:10.1093/brain/awaf202):
> "Monoallelic pathogenic variants in LGI1 cause autosomal dominant epilepsy with auditory features with onset in childhood/adolescence."
> "Affected individuals presented DEE with neonatal/infantile-onset epilepsy (n = 6/6), global developmental delay/intellectual disability (n = 6/6) and infant/premature death (n = 5/6)."
> "Functional analyses revealed that all LGI1 variants result in reduced secretion and ADAM22-binding. Residual LGI1 function levels correlated with clinical severity, ranging from infantile lethality to intermediate phenotypes."

That paper establishes a clean **dose–response allelic series**: ~50% LGI1 (heterozygous ADEAF) → focal epilepsy, normal cognition; residual function ~6.7–40% (biallelic hypomorph) → DEE of graded severity; null → infantile lethality. A prior mouse study likewise found "approximately 50% of LGI1 and approximately 10% of ADAM22 protein levels are sufficient to prevent lethal epilepsy."

### RELN (`hgnc:9957`, 7q22.1; protein P78509, Reelin)

From PMID:26046367 (verbatim abstract):
> "We show that ADLTE-related mutations significantly decrease serum levels of Reelin, suggesting an inhibitory effect of mutations on protein secretion."
> "We also show that Reelin and LGI1 co-localize in a subset of rat brain neurons, supporting an involvement of both proteins in a common molecular pathway underlying ADLTE."
> "Homozygous RELN mutations are known to cause lissencephaly with cerebellar hypoplasia."

- Seven heterozygous **missense** variants across seven families; 3D modeling predicted structural effects on domain folding.
- **Penetrance in RELN families: 60% (20/33 carriers affected)** (GeneReviews).
- **Constraint:** pLI = 1, o/e LoF = 0.253 (108 obs / 428 exp), LOEUF = 0.296. Note the paradox worth flagging in curation: RELN is LoF-constrained, yet ADEAF alleles are missense secretion-impairing, while *biallelic* RELN LoF gives Norman-Roberts lissencephaly — a second allelic series with a dosage/mechanism split.

### MICAL1 (`hgnc:20619`, 6q21; protein Q8TDZ2)

The odd one out — **gain of function** (Dazzo E et al., *Ann Neurol* 2018;83:483–493, PMID:29394500):
> "We identified two ADLTE-causing variants in the MICAL-1 gene: a p.Gly150Ser substitution occurring in the enzymatically active monooxygenase (MO) domain and a p.Ala1065fs frameshift indel in the C-terminal domain, which inhibits the oxidoreductase activity of the MO domain."
> "In cell-based assays, both variants significantly increased MICAL-1 oxidoreductase activity and induced cell contraction in COS7 cells, which likely resulted from deregulation of F-actin dynamics."
> "This suggests that dysregulation of the actin cytoskeleton dynamics is a likely mechanism by which MICAL-1 pathogenic variants lead to ADLTE."

**Constraint:** pLI ≈ 0, LOEUF = 0.855 — i.e. MICAL1 is *not* LoF-constrained, which is exactly what you'd predict for a gain-of-function disease gene. Nice internal consistency check.

### Variant classification, allele frequency, modifiers, epigenetics

- **ACMG/AMP classification:** ADEAF variants in ClinVar are typically P/LP for recurrent LGI1 alleles; many novel missense land as VUS pending functional data. The secretion/ADAM22-binding assays (HiBiT split-nanoluciferase, cell-surface binding) are the field's de facto PS3-grade functional evidence.
- **Population frequency:** pathogenic alleles are private/family-specific; absent or ultra-rare in gnomAD. No recurrent founder allele is established.
- **Modifier genes:** none validated. Reduced penetrance (54–85%) implies modifiers exist but they are uncharacterized — a genuine knowledge gap worth a `KNOWLEDGE_GAP` discussion in the KB entry.
- **Epigenetics:** no ADEAF-specific methylation/chromatin data. **Not available.**
- **Chromosomal abnormalities:** an intragenic *CNTNAP2* deletion was found in one EAF family (PMID:27066544); LGI1 exon-level deletions account for ~5% of LGI1-positive cases. No recurrent cytogenetic syndrome.

---

## 5. Environmental Information

- **Environmental factors:** none causal. Auditory stimuli act as acute precipitants only (§2).
- **Lifestyle:** standard epilepsy precipitants (sleep deprivation, alcohol, medication non-adherence) apply by extrapolation; no ADEAF-specific study. Explicitly flag as extrapolated, not measured.
- **Infectious agents:** none. **Not applicable.**
- **One genuinely relevant "acquired environment":** anti-LGI1 **autoimmune** encephalitis targets the same protein. "Antibodies against epitempin disrupting the LGI1-ADAM22 complex cause a rare form of autoimmune encephalitis, characterized in some cases by peculiar faciobrachial dystonic seizures (FBDS)" (PMID:35153984). Same molecular node, different insult — a beautiful natural experiment, and a mandatory differential in adult-onset cases.

---

## 6. Mechanism / Pathophysiology

### The core causal chain (LGI1 arm)

**LGI1 loss of function → failure of the trans-synaptic LGI1–ADAM22/ADAM23 bridge → reduced AMPA-receptor-mediated transmission + loss of Kv1.1 at the axon initial segment and presynaptic terminals → intrinsic and synaptic hyperexcitability of lateral-temporal/hippocampal glutamatergic neurons → focal epileptiform discharge in auditory association cortex → auditory aura → propagation → focal impaired awareness / bilateral tonic-clonic seizure.**

Step by step, with citations:

**(1) Ligand–receptor assembly.** ADAM22 is the receptor (PMID:16990550):
> "ADAM22, a transmembrane protein that when mutated itself causes seizure, serves as a receptor for LGI1. LGI1 enhances AMPA receptor-mediated synaptic transmission in hippocampal slices. The mutated form of LGI1 fails to bind to ADAM22. ADAM22 is anchored to the postsynaptic density by cytoskeletal scaffolds containing stargazin."

**(2) Trans-synaptic complex.** (Fukata Y et al., *PNAS* 2010;107:3799–804, PMID:20133599):
> "Extracellularly secreted LGI1 links two epilepsy-related receptors, ADAM22 and ADAM23, in the brain and organizes a transsynaptic protein complex that includes presynaptic potassium channels and postsynaptic AMPA receptor scaffolds. A lack of LGI1 disrupts this synaptic protein connection and selectively reduces AMPA receptor-mediated synaptic transmission in the hippocampus."
> "Thus, LGI1 may serve as a major determinant of brain excitation."

**(3) Structure.** (Yamagata A, Fukai S, *Cell Mol Life Sci* 2019, PMID:31432233 — review):
> "LGI1 consists of the N-terminal LRR domain and the C-terminal epitempin-repeat (EPTP; also known as EAR) domain."
> "The crystal structure of the full-length LGI1 in complex with ADAM22 exhibits a 2:2 heterotetramer in a dimer-of-dimer assembly."
> "transsynaptic linkage through the tripartite complex of ADAM22–(LGI1)2–ADAM23 in synapses"
> "Through this synaptic protein network, LGI1 modulates AMPA receptor-mediated synaptic transmission."
> "LGI1 is enriched at the axon initial segment and colocalized with ADAM22/23 and the voltage-gated potassium (Kv1) channels."

**(4) Two mutational routes into the same failure:**
> "Among them, 19 mutations result in secretion-defective proteins presumably due to the failure of protein folding." / "The E383A mutation disrupts the Ca2+ coordination inside of the β-propeller structure." / "The S473L mutation substantially reduces the binding to ADAM22." / "The R474Q mutation disables the assembly of the tripartite complex of ADAM22, ADAM23, and LGI1." (PMID:31432233)

**(5) Kv1.1 and intrinsic excitability — and it's reversible** (Extrémet J et al., *J Neurosci* 2023;43:8596–8606, PMID:37863654):
> "We previously showed that LGI1 deficiency in a mouse model (i.e., knock-out for LGI1 or KO-Lgi1) decreased Kv1.1 channel density at the axon initial segment (AIS) and at presynaptic terminals, thus enhancing both intrinsic excitability and glutamate release."
> "…the selective expression of LGI1 in KO-Lgi1 neurons from mice of both sexes, using single-cell electroporation, reduces intrinsic excitability and restores both the Kv1.1-mediated D-type current and Kv1.1 channels at the AIS."

**(6) Developmental arm — synaptic pruning** (Zhou YD et al., *Nat Med* 2009;15:1208–14, PMID:19701204):
> "We discovered that the normal postnatal maturation of presynaptic and postsynaptic functions was arrested by the 835delC mutant LGI1, and contrastingly, was magnified by excess wild-type LGI1. Concurrently, mutant LGI1 inhibited dendritic pruning and increased the spine density to markedly increase excitatory synaptic transmission. Inhibitory transmission, by contrast, was unaffected."

**(7) Cell-type specificity — it's the excitatory neurons** (Boillot M et al., *Brain* 2014;137:2984–96, PMID:25234641):
> "Emx1-Lgi1cKO mice displayed early-onset and lethal seizures, whereas CaMKIIα-Lgi1cKO mice presented late-onset occasional seizures associated with variable reduced lifespan. In contrast, neither spontaneous seizures nor increased seizure susceptibility to convulsant were observed when Lgi1 was deleted in parvalbumin interneurons."
> "We suggest that LGI1 secreted from excitatory neurons, but not parvalbumin inhibitory neurons, makes a major contribution to the pathogenesis of LGI1-related epilepsies. Our data further indicate that LGI1 is required from embryogenesis to adulthood to achieve proper circuit functioning."

**(8) Anatomical origin of discharge** (PMID:40455867): "we observed epileptic discharges from the isolated whole hippocampus of Lgi1-/- knockout mice, experimentally modelling the hippocampal origin of LGI1-related epilepsy." Note the tension worth curating explicitly: the *human* syndrome is lateral-temporal/neocortical by semiology, while the mouse models discharge from hippocampus — a legitimate `HUMAN_MODEL_MISMATCH` candidate.

### The RELN arm

Reelin is a large secreted glycoprotein signaling through VLDLR/ApoER2–DAB1; mutant alleles reduce serum reelin, i.e. **loss of secreted ligand** — the same *category* of failure as LGI1, in a partly overlapping cell population ("Reelin and LGI1 co-localize in a subset of rat brain neurons," PMID:26046367). Reelin has "important functions in both the developing and adult brain," so the plausible chain is impaired neuronal positioning/plasticity in temporal cortex → altered excitability. The precise adult-brain mechanism is **not resolved** — this is an honest knowledge gap, not something to over-narrate.

### The MICAL1 arm

MICAL-1 is an actin-disassembling monooxygenase (it oxidizes methionine residues on F-actin). Gain of oxidoreductase activity → excess actin filament disassembly → deranged cytoskeletal dynamics in developing/adult neurons → circuit-level hyperexcitability (PMID:29394500). This is the least mechanistically nailed-down of the three arms, and MICAL1's low constraint plus only two families means it should be curated with appropriate epistemic hedging (see also Nobile & Dazzo, *Genes* 2022;13:715, PMC9141472).

### Suggested ontology terms for pathophysiology nodes (all verified via local OAK)

**Biological processes (GO):**
- `GO:0098990` AMPA selective glutamate receptor signaling pathway
- `GO:0097113` AMPA glutamate receptor clustering
- `GO:0050804` modulation of chemical synaptic transmission
- `GO:0007268` chemical synaptic transmission
- `GO:0060291` long-term synaptic potentiation
- `GO:1905805` excitatory synapse pruning · `GO:0098883` synapse pruning
- `GO:0005249` voltage-gated potassium channel activity (MF)
- `GO:0038026` reelin-mediated signaling pathway
- `GO:0030042` actin filament depolymerization (MICAL1 arm; `modifier: INCREASED`)

**Cellular components:** `GO:0043194` axon initial segment; `GO:0032281` AMPA glutamate receptor complex; `GO:0110157` reelin complex.

**Cell types (CL):** `CL:0000679` glutamatergic neuron; `CL:0000598` pyramidal neuron; `CL:1001571` hippocampal pyramidal neuron; `CL:0000617` GABAergic neuron (for the *negative* result — PV interneuron deletion does **not** cause seizures); `CL:0000127` astrocyte (LGI1 is also secreted by astrocytes).

**Suggested module conformance:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` — ADEAF is close to a textbook conformer (channel/synaptic dysfunction → E/I imbalance → hyperexcitability/hypersynchrony → seizures). Substitute the disorder-specific trigger (LGI1–ADAM22/23 trans-synaptic complex failure) at the top node.

### Molecular profiling / advanced technologies

Transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial, and CRISPR-screen data specific to ADEAF: **not available**. Mouse *Lgi1* expression is "predominantly neuronal and is consistent with the anatomic regions involved in temporal lobe epilepsy" (PMID:11810107). Human protein-level reference: UniProt O95970 (LGI1), Q9P0K1 (ADAM22), P78509 (RELN), Q8TDZ2 (MICAL1); complex structures in the PDB from the Yamagata/Fukai work.

---

## 7. Anatomical Structures Affected

- **Primary organ / system:** brain; nervous system. `UBERON:0000955` brain, `UBERON:0000956` cerebral cortex.
- **Lobe/region:** lateral **temporal lobe** neocortex — "Seizures originate in the lateral temporal neocortex, distinguishing EAF from mesial temporal lobe epilepsy" (PMID:35153984). `UBERON:0001871` temporal lobe.
- **Auditory cortex:** `UBERON:0001393` auditory cortex; primary auditory cortex `UBERON:0034751` (Heschl's gyrus ≈ `UBERON:0002773` anterior transverse temporal gyrus); auditory association cortex ≈ `UBERON:0034752` secondary auditory cortex; `UBERON:0002769` superior temporal gyrus.
- **Language cortex:** posterior superior temporal (Wernicke) region for ictal receptive aphasia — no clean UBERON term; use `UBERON:0002769` plus `HP:0033848`.
- **Hippocampal formation** (`UBERON:0002421`): the discharge origin in mouse models and in the biallelic human DEE phenotype; **not** the primary site in classic human ADEAF.
- **Cell/tissue level:** glutamatergic pyramidal neurons of neocortex and hippocampus; excitatory synapses; PV interneurons spared as a *source* of LGI1.
- **Subcellular:** axon initial segment (`GO:0043194`), presynaptic terminal, postsynaptic density, endoplasmic reticulum (site of misfolded-LGI1 retention/degradation — `GO:0005783`, verify before use).
- **Lateralization:** notable **left predominance** of EEG abnormalities, "with marked left predominance" in RELN families (PMID:28142128); GeneReviews notes left predominance in some series and a DTI finding of "increased fractional anisotropy in the left temporal lobe" in LGI1-positive families. Seizures themselves may be bilateral-independent across a pedigree.

---

## 8. Temporal Development

- **Onset:** adolescence/early adulthood; typical 10–30 years; range 4–50 (GeneReviews). RELN families mean 20 years (PMID:28142128). Onset <10 years is a bad-prognosis marker (PMID:29464704).
- **Onset pattern:** episodic from the start — first event is usually an aura or an FBTCS; no prodrome, no insidious decline.
- **Stages:** none formally defined. Practically: (i) isolated auras, often unrecognized for years; (ii) auras + intermittent FBTCS (usual presentation to care); (iii) either long-term remission or, in a minority, drug-resistant focal epilepsy considered for surgery.
- **Course:** non-progressive, chronic, lifelong susceptibility. FBTCS "occurred only once or twice per year" in one 34-person series (GeneReviews).
- **Remission:** both treatment-induced and spontaneous remission occur; withdrawal relapse is a real hazard — "Drug withdrawal often leads to clinical relapses, not always responding to reinitiation of treatment" (PMID:35153984). Cumulative terminal-remission rates 26.6% / 35.7% / 51.6% at 10 / 20 / 30 years (PMID:29464704).
- **Critical periods:** the mouse data argue LGI1 "is required from embryogenesis to adulthood" (PMID:25234641), and that embryonic-onset loss is catastrophic while late-postnatal loss is mild — relevant to any future gene-replacement timing question.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: unknown.** GeneReviews: "The prevalence of ADEAF is unknown but likely very low." Orphanet lists it among rare disorders (<1/2,000) without a numeric class.
- Among Mendelian focal epilepsies it's not marginal: "9/48 (19%) of families…met criteria for ADEAF" (GeneReviews); ~3% of people with epilepsy have a significant family history, of whom a fraction meets ADEAF criteria.
- **Incidence:** not estimable — "a precise estimate of the incidence of EAF is currently not available" (PMID:35153984), largely because isolated auditory auras go unreported.
- **Suggested dismech encoding:** `measure_type: POINT_PREVALENCE`, `prevalence_class: UNKNOWN` (or `ULTRA_RARE` with a note), no `rate_per_100000`. Do **not** invent a number.

### Genetic parameters

- **Inheritance:** autosomal dominant with **reduced penetrance** (`HP:0000006` Autosomal dominant inheritance; `HP:0003829` Incomplete penetrance).
- **Penetrance:** 54% across eight LGI1 families (PMID:15079011); best pooled estimate **67% (95% CI 55–77%)** across all 24 published LGI1 families (PMID:18711109) —
  > "Overall penetrance was 67% (95% CI 55-77%), and did not vary according to mutation type or location within the gene."
  > "Our results suggest that about two-thirds of individuals who inherit a mutation in LGI1 will develop epilepsy. This probably overestimates the true penetrance in the population because it is based on data from families containing multiple affected individuals."
  RELN: 60% (20/33 carriers). GeneReviews quotes an overall 54–85% range for counseling.
- **Expressivity:** variable — auditory aura vs aphasic seizures vs FBTCS-only within the same pedigree; some LGI1 families even contain individuals with idiopathic generalized epilepsies (PMID:15079011).
- **Anticipation:** not a repeat-expansion disorder; apparent generational increase in penetrance in the Rosanoff analysis was attributed to ascertainment ("probably because of limited information about early generations").
- **Germline mosaicism:** not reported. **De novo:** ~1%.
- **Founder effects / consanguinity:** none for classic AD ADEAF. Consanguinity is relevant only for the new **biallelic** LGI1 DEE phenotype — all four families in PMID:40455867 were consanguineous.
- **Carrier frequency:** not applicable (dominant); pathogenic alleles are essentially absent from gnomAD.

### Demographics

- **Populations:** described worldwide; the deepest family series are Italian (Nobile/Michelucci, 40 families) and North American (Ottman/Columbia). Reports from Turkey, Korea, China, Brazil. No population enrichment established.
- **Sex ratio:** ~1:1 (58 M / 65 F, PMID:29464704); penetrance sex-independent.
- **Geographic variant distribution:** private family variants; no geographic clustering.

---

## 10. Diagnostics

### Clinical criteria (ILAE 2022, via GeneReviews summary)

**Mandatory:** focal sensory auditory seizures and/or focal cognitive seizures with receptive aphasia; **normal brain MRI**.
**Exclusionary/alerts:** generalized-onset seizures or other focal-onset seizure types; moderate/severe intellectual disability; generalized epileptiform discharges; focal abnormalities on neurologic exam.

### Electrophysiology (the workhorse)

EEG (`LOINC` — routine EEG `24708-6`, **verify**): interictal EEG normal in a substantial minority; focal temporal sharp waves/spikes in 57–80%, often left-predominant. Sleep-deprived and prolonged video-EEG increase yield. **Prognostically loaded:** unremarkable EEG predicts remission (HR 3.5, PMID:29464704).

### Imaging

MRI brain (3T, epilepsy protocol) — expected **normal**; its main job is excluding hippocampal sclerosis, focal cortical dysplasia (think *DEPDC5*), and tumor. Research-level findings: left temporal FA increase on DTI; one Brazilian family with a left lateral temporal malformation that did not fully co-segregate (GeneReviews). A completed NIH imaging study exists: **NCT00072813** — "MRI in Autosomal Dominant Partial Epilepsy With Auditory Features" (status: Completed).

### Laboratory / biomarkers

- No routine biochemical marker. **Serum Reelin is reduced** by ADLTE RELN mutations (PMID:26046367) — a research biomarker, not a validated clinical assay.
- **Anti-LGI1 antibodies (serum + CSF)** are the essential rule-out in adult-onset cases — a negative-defining test rather than a positive one.
- Biopsy/histopathology: not indicated; no characteristic pathology.

### Genetic testing (the actual diagnostic)

Recommended approach: multigene **epilepsy panel** including at minimum *LGI1*, *RELN*, *MICAL1*, plus *DEPDC5*, *SCN1A*, *CNTNAP2*, and (emerging) *KCNQ2*; escalate to **exome/genome** if the panel is negative — which it will be most of the time (92% of unselected EAF probands, PMID:33453592). Single-gene *LGI1* testing is reasonable only in a classic large AD pedigree. Include **exon-level del/dup analysis** (~5% of LGI1 findings). CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are **not indicated** unless the phenotype is atypical.

### Differential diagnosis (with distinguishing features)

| Condition | How to tell it apart |
|---|---|
| **Anti-LGI1 autoimmune encephalitis** | subacute onset, faciobrachial dystonic seizures, amnesia, hyponatremia, LGI1 antibodies, often older adult, MRI mesial temporal signal change |
| **Mesial temporal lobe epilepsy (familial or with HS)** | epigastric/psychic/autonomic auras dominate; auditory symptoms <10%; hippocampal sclerosis on MRI |
| **Familial focal epilepsy with variable foci (DEPDC5 etc.)** | seizure focus differs *between* family members; auditory symptoms/aphasia not the family-wide signature |
| **Autosomal dominant sleep-related hypermotor epilepsy** | nocturnal hyperkinetic frontal seizures |
| **Tinnitus** | continuous/durable rather than brief and stereotyped; "far more durable than the seizure of EAF" (PMID:35153984) |
| **Schizophrenia / primary psychotic auditory hallucination** | complex, sustained, with other psychotic features; not brief, stereotyped, self-limited |
| **Structural lateral temporal lesion** | MRI |

### Screening

No population or newborn screening (adult-onset, non-treatable-by-early-detection, moderate penetrance). **Cascade predictive testing** of at-risk relatives is available once the familial variant is known, but must be counseled around the 54–85% penetrance and the absence of any preventive intervention. Prenatal and preimplantation genetic testing are technically available (GeneReviews) — and are exactly the kind of decision that belongs with a genetic counselor, not a panel default.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** no excess mortality documented for classic heterozygous ADEAF beyond the general epilepsy SUDEP risk; **not quantified for this syndrome.** (Contrast: biallelic LGI1 DEE, where 5/6 died between 9 months and 24 years — PMID:40455867.)
- **Seizure outcome — the single most important recent number** (Bisulli F et al., *Epilepsia* 2018;59:834–843, PMID:29464704, n=123, median follow-up 11 years):
  > "At last assessment, 42 patients had achieved TR (34.1%)."
  > "The cumulative rates of TR were 26.6%, 35.7%, and 51.6% at 10, 20, and 30 years from inclusion."
  > "Our data show a wide prognostic spectrum of EAF, ranging from mild forms with spontaneous remission, to severely refractory epilepsy addressed to surgery. The outcome, less favorable than expected from previous studies, appears to be primarily a function of 3 prognostic negative risk factors: age at onset < 10 years, auditory aura characterized by complex auditory hallucinations, and focal epileptiform abnormalities on scalp EEG."

  Positive predictors on multivariate analysis: age at onset >10 years (HR 3.2, p=.028); distortion-only auras vs simple/complex hallucinations (HR 2.9, p=.041); unremarkable EEG (HR 3.5, p=.041).

  **This directly contradicts the older "benign syndrome" framing** ("The clinical course of ADEAF is usually benign," GeneReviews). Curate both, with the tension made explicit — the discrepancy is partly referral-center ascertainment (Bologna tertiary cohort) vs family-study ascertainment. Worth a `DISCREPANCY`/`KNOWLEDGE_GAP` discussion node.
- **Morbidity/disability:** cognition and neurologic exam are normal by definition. Disability is seizure-driven (driving, employment, injury from FBTCS).
- **Quality-of-life instruments:** no ADEAF-specific QOLIE-31/EQ-5D data. **Not available.**
- **Complications:** status epilepticus is rare; aphasic status epilepticus (`HP:0032849`) is conceptually possible but not established as characteristic.
- **Prognostic biomarkers:** none molecular. Genotype does **not** predict outcome — "no significant clinical differences were observed between families with an LGI1 pathogenic variant and families without an identified pathogenic variant," and RELN vs LGI1 families are clinically "indistinguishable" (PMID:28142128). The only genotype–phenotype signal is domain-level: "Auditory symptoms were less frequent in individuals with truncation mutations in the EPTP domain than in those with other mutation type/domain combinations (58% vs 80%, p = 0.018)" (PMID:22323750).

---

## 12. Treatment

**There are no ADEAF-specific randomized trials.** Everything below is standard focal-epilepsy practice applied to this syndrome, plus small-series experience. Say so plainly in the KB entry.

### Pharmacotherapy

- **First line: sodium-channel-blocking ASMs, carbamazepine as the prototype, usually as monotherapy and often at low dose.** GeneReviews: "Seizure control is usually readily achieved with standard anti-seizure medications (ASM)" and "Traditionally sodium channel blockers such as carbamazepine have been more frequently used with clear benefit," while noting no formal trials. Furia 2022: "EAF is considered a syndrome with a good response to anti-seizure medications used for focal epilepsy, such as carbamazepine in monotherapy."
- **Reasonable alternatives** (focal-epilepsy standard): oxcarbazepine, lamotrigine, levetiracetam, lacosamide.
- **Avoid the classic misstep:** "When misdiagnosed as idiopathic generalized epilepsy, EAF might be treated with drugs that are not optimal (i.e., phenobarbital or valproate), leading to poor response" (PMID:35153984).
- **Withdrawal caution:** relapse after withdrawal may not re-respond (PMID:35153984) — argues for conservative, counseled taper decisions.
- **Response:** "completely or almost completely controlled by antiepileptic treatment in the vast majority of cases (96%)" in RELN families (PMID:28142128) — but note this is *seizure control at last visit*, not the stricter 5-year terminal remission of Bisulli 2018 (34.1%). Two different endpoints; don't blend them.

### Pharmacogenomics

Not ADEAF-specific, but clinically mandatory for the first-line drug: **HLA-B\*15:02 screening before carbamazepine in Southeast Asian ancestry** (SJS/TEN risk) and HLA-A\*31:01 as a risk allele for carbamazepine hypersensitivity in European/Japanese populations — see CPIC carbamazepine guideline / FDA labeling. This is a real and actionable pharmacogenomic link for this syndrome's first-line agent.

### Advanced / experimental therapeutics

- **Chemical chaperone (preclinical, promising):** 4-phenylbutyrate rescues secretion-defective LGI1 — "The 4PBA treatment significantly improved the secretion of LGI1 mutants and their binding to ADAM22" and "small molecules serving as chemical correctors might be new therapeutic options for LGI1-mediated epilepsy" (PMID:31432233). In 2025, 4PBA "selectively enhanced Cys48Phe secretion" (PMID:40455867). Mutation-class-specific: only helps *foldable-but-retained* alleles, useless for nulls. CHEBI:41500 (4-phenylbutyric acid).
- **Gene/protein restoration (preclinical):** single-neuron LGI1 re-expression normalizes excitability (PMID:37863654); Thy1-LGI1 transgene rescues the lethal Lgi1−/− phenotype. No AAV-LGI1 clinical program exists as of this writing. Given the ~50%-protein-sufficiency threshold, dose control would matter.
- **Gene therapy / ASO / cell therapy / immunotherapy:** none in trials for ADEAF. **Not available.** (Immunotherapy is for the *autoimmune* LGI1 disease, a different entity — don't cross-wire them in the KB.)

### Surgical / interventional

Resective surgery is reserved for the drug-resistant minority — "Surgery might be employed instead in resistant cases" (PMID:35153984); the Bologna cohort included patients "addressed to surgery" (PMID:29464704). Outcome data for surgery specifically in ADEAF are **not published** in any systematic form; note that a genetic, potentially bilateral-network epilepsy is a less favorable surgical substrate than unilateral hippocampal sclerosis.

### Supportive

Standard epilepsy self-management, sleep hygiene, driving counseling, seizure-safety education, and — specific to this syndrome — counseling that unexplained sounds are seizures, not psychosis. Genetic counseling is a core deliverable (§13).

### Suggested NCIT annotations (verified via local `sqlite:obo:ncit` unless noted)

| Treatment | `treatment_term` | `therapeutic_agent` (CHEBI, all verified) | `therapeutic_modality` |
|---|---|---|---|
| Carbamazepine monotherapy | `NCIT:C15986` Pharmacotherapy | `CHEBI:3387` carbamazepine | SMALL_MOLECULE |
| Oxcarbazepine | `NCIT:C15986` | `CHEBI:7824` oxcarbazepine | SMALL_MOLECULE |
| Lamotrigine | `NCIT:C15986` | `CHEBI:6367` lamotrigine | SMALL_MOLECULE |
| Levetiracetam | `NCIT:C15986` | `CHEBI:6437` levetiracetam | SMALL_MOLECULE |
| Lacosamide | `NCIT:C15986` | `CHEBI:135939` lacosamide | SMALL_MOLECULE |
| Generic ASM therapy | `NCIT:C64172` Anticonvulsant Therapy (**check reachability from `NCIT:C25218` before use**) | — | SMALL_MOLECULE |
| Resective temporal surgery | `NCIT:C15329` Surgical Procedure, or `NCIT:C52004` Brain Lobectomy | — | SURGERY |
| Genetic counseling | `NCIT:C15240` Genetic Counseling | — | BEHAVIORAL |
| Supportive care | `NCIT:C15747` Supportive Care | — | OTHER |

### Clinical trials

`NCT00072813` — *MRI in Autosomal Dominant Partial Epilepsy With Auditory Features* (observational imaging; **Completed**). No interventional ADEAF trial found on ClinicalTrials.gov as of 2026-08-05.

---

## 13. Prevention

- **Primary prevention:** none — the disease is germline. The only "primary prevention" lever is reproductive: genetic counseling, prenatal diagnosis, or PGT once the familial variant is known (GeneReviews), each carrying the heavy caveat of 54–85% penetrance and a generally treatable, non-degenerative phenotype.
- **Secondary prevention:** early recognition of auditory auras in known families → earlier diagnosis and treatment. Whether earlier treatment changes long-term remission is **unstudied**.
- **Tertiary prevention:** adherence, avoidance of sleep deprivation and (for the reflex-sensitive minority) unpredictable loud stimuli; correct drug selection (avoid valproate/phenobarbital chosen on a mistaken IGE diagnosis); cautious ASM withdrawal given relapse risk; driving/occupational safety.
- **Immunization / public health / environmental interventions:** **not applicable.**
- **Prophylaxis:** no pre-symptomatic ASM prophylaxis is indicated or studied in unaffected carriers. Given ~⅓ of carriers never develop seizures, treating carriers would be net harm.
- **Counseling specifics:** offspring of an affected individual have a 50% chance of inheriting the variant, of whom 54–85% will manifest (GeneReviews); siblings' risk depends on parental carrier status, and a clinically unaffected parent may still be a carrier because of reduced penetrance.

---

## 14. Other Species / Natural Disease

This is one of the better comparative stories in epilepsy genetics — dogs got there partly first.

- **Taxonomy:** *Homo sapiens* `NCBITaxon:9606`; *Mus musculus* `NCBITaxon:10090`; *Rattus norvegicus* `NCBITaxon:10116`; *Canis lupus familiaris* `NCBITaxon:9615`.
- **Naturally occurring canine disease — LGI2 in Lagotto Romagnolo** (Seppälä EH et al., *PLoS Genet* 2011;7:e1002194, PMID:21829378):
  > "Using genome-wide association in 11 discordant sib-pairs from this pedigree, we mapped the disease locus to a 1.7 Mb region of homozygosity in chromosome 3 where we identified a protein-truncating mutation in the Lgi2 gene, a homologue of the human epilepsy gene LGI1."
  > "We show that LGI2, like LGI1, is neuronally secreted and acts on metalloproteinase-lacking members of the ADAM family of neuronal receptors, which function in synapse remodeling, and that LGI2 truncation, like LGI1 truncations, prevents secretion and ADAM interaction."
  > "LGI2 acts at least in part through the same ADAM receptors as LGI1, but earlier, ensuring electrical stability (absence of epilepsy) during pruning years, preceding this same function performed by LGI1 in later years."

  Onset ~7 weeks, remitting by ~4 months — a *developmentally shifted* version of the same pathway, and a proposed model for remitting childhood epilepsy. Breed: Lagotto Romagnolo (VBO term available — **look up before curating**). Note this is **autosomal recessive** in dogs and involves the paralog *LGI2* (`hgnc:18710`), so it is a pathway homolog, not a direct ADEAF ortholog model.
- **Canine ADAM23 risk haplotype** (Koskinen LL et al., *BMC Genomics* 2015;16:465, PMID:26084559): a 28-kb ADAM23 risk haplotype replicated across Belgian Shepherd, Schipperke, Finnish Spitz, and Beagle (p_raw = 2.76e-15), frequency 0.49–0.70 — "ADAM23 plays a role in synaptic transmission and interacts with known epilepsy genes, LGI1 and LGI2, and should be considered as a candidate gene for human epilepsies." Low-penetrance risk gene, causative variant still unidentified. This is real **veterinary relevance**: idiopathic epilepsy is a common canine neurological disease and a DNA test exists for the Lagotto LGI2 allele.
- **Orthologs:** mouse *Lgi1* (MGI), *Reln* (the classic **reeler** mouse), *Adam22*, *Adam23*, *Mical1*; dog *LGI2*, *ADAM23*. Register in OMIA for the canine entries.
- **Evolutionary conservation:** the LGI–ADAM synaptic module is conserved across mammals, with paralog subfunctionalization by developmental window (LGI2 early, LGI1 later — PMID:21829378). Genuinely elegant.
- **Zoonotic potential / cross-species transmission:** **not applicable.**

---

## 15. Model Organisms

| Model | Type | Phenotype | Recapitulation | Key citation |
|---|---|---|---|---|
| ***Lgi1*−/− mouse** | germline KO | early-onset spontaneous seizures, **lethal at 2–3 weeks**; reduced AMPAR transmission; ↓Kv1.1 at AIS/terminals; hippocampal epileptic discharges in isolated whole hippocampus | Models the *pathway*, not the human heterozygous syndrome; far more severe. Now recognized as a model of the **biallelic human DEE** | PMID:20133599; PMID:25234641; PMID:40455867 |
| ***Lgi1*+/− mouse** | germline het | **lowered seizure thresholds**, no spontaneous lethal epilepsy | Closest genotype match to human ADEAF; phenotype is subthreshold (no spontaneous auditory-aura equivalent — mice can't report auras anyway) | PMID:20133599 |
| **Emx1-Cre *Lgi1* cKO** | conditional (embryonic, glutamatergic) | early-onset lethal seizures | Localizes requirement to excitatory neurons + early development | PMID:25234641 |
| **CaMKIIα-Cre *Lgi1* cKO** | conditional (late postnatal, excitatory) | late-onset occasional seizures, variable lifespan reduction | Best temporal analog of adolescent-onset human disease | PMID:25234641 |
| **PV-Cre *Lgi1* cKO** | conditional (PV interneurons) | **no seizures, no threshold change** — informative negative | Establishes cell-type specificity | PMID:25234641 |
| **LGI1-835delC transgenic mouse** | human truncating allele, transgenic | arrested postnatal synapse maturation, inhibited dendritic pruning, ↑spine density, ↑excitatory transmission, epileptiform discharge + facilitated kindling; inhibitory transmission unaffected | Models the *developmental* arm of a real human ADEAF allele | PMID:19701204 |
| **LGI1 D51G knock-in mouse** | precise patient-allele KI | confirms pathogenicity of a novel Chinese-family ADLTE variant | Highest-fidelity allele model class | PMC8739050 (2021) |
| ***Adam22*−/− mouse** | KO | epileptic phenotype similar to Lgi1 loss; ~10% ADAM22 protein suffices to prevent lethal epilepsy | Receptor-side validation | PMID:16990550; PMID:40455867 |
| ***Adam22*ΔC5/ΔC5 mouse** | KI (PDZ-binding motif deleted) | hyperactivity, impaired behavioral flexibility, complex-learning deficits (IntelliCage) | Models cognitive dimension of ADAM22-related DEE | PMID:40455867 |
| ***Adam23*−/− / +/− mouse** | KO / het | spontaneous seizures (−/−); decreased seizure threshold (+/−); reduced CA1 dendritic arborization | Third leg of the tripartite complex | PMID:19796686 |
| ***reeler* mouse (*Reln* null)** | spontaneous mutant | ataxia, inverted cortical lamination | Models **biallelic** RELN lissencephaly, **not** heterozygous ADEAF — the ADEAF-relevant heterozygous-missense mouse is a gap | (classic literature) |
| **Cultured neurons + single-cell electroporation** | in vitro rescue | LGI1 re-expression restores D-type current, Kv1.1 at AIS, prevents homeostatic AIS shortening | Proof-of-principle for reversibility | PMID:37863654 |
| **COS7 / HEK cell assays** | in vitro | secretion (Western, HiBiT split-nanoluciferase), cell-surface ADAM22 binding, MICAL1 oxidoreductase + cell-contraction assay | The functional-evidence backbone for variant classification | PMID:29394500; PMID:40455867 |

**Model limitations to record explicitly:**
1. **No model reproduces the defining human feature** — the auditory aura and ictal receptive aphasia are subjective, language/percept-dependent phenomena with no rodent readout. Any mouse-derived phenotype claim must be tagged `MODEL_ORGANISM` and must not be the sole support for a human phenotype.
2. **Dosage mismatch:** mouse *homozygous* nulls are lethal-epileptic while human *heterozygotes* have a mild focal epilepsy; the human-equivalent het mouse shows only threshold changes.
3. **Anatomical mismatch:** mouse discharges originate in hippocampus; human ADEAF is lateral-temporal neocortical. Strong candidate for a `HUMAN_MODEL_MISMATCH` discussion with a proposed experiment (region-restricted lateral-temporal *Lgi1* deletion; auditory-cortex-targeted recordings).
4. **RELN and MICAL1 arms are under-modeled** — no published heterozygous-missense Reln ADLTE mouse, no Mical1 GoF knock-in.

**Resources:** MGI (mouse alleles for *Lgi1*, *Adam22*, *Adam23*, *Reln*), Alliance of Genome Resources, IMPC/KOMP, IMSR/MMRRC for strain requests, OMIA for the canine LGI2/ADAM23 entries, Cellosaurus for cell lines.

---

## Appendix A — Suggested dismech pathophysiology skeleton

A causal chain that stays honest about scale and evidence:

1. **LGI1 Loss of Function** — `biological_scale: MOLECULAR`; gene `hgnc:6572`; secretion-defective vs binding-defective as two `mechanistic_hypotheses`-free *routes* (both established, so model as two upstream nodes converging, not competing hypotheses) → downstream to (2)
2. **Failure of the LGI1–ADAM22/ADAM23 Trans-Synaptic Complex** — `MOLECULAR`; `GO:0050804`; cell types `CL:0000679` → (3a) and (3b)
3. **a. Reduced AMPA Receptor-Mediated Synaptic Transmission** — `CELLULAR`; `GO:0098990`, `GO:0097113`, modifier DECREASED
   **b. Loss of Kv1.1 at the Axon Initial Segment** — `CELLULAR`; `GO:0005249` + `GO:0043194`, modifier DECREASED
4. **Glutamatergic Neuron Hyperexcitability** — `CELLULAR`; `CL:0000598` / `CL:1001571`
5. **Excitation-Inhibition Imbalance** — `CELLULAR`; `conforms_to: epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`
6. **Lateral Temporal Neocortical Epileptogenesis** — `TISSUE`; `UBERON:0001393` / `UBERON:0002769` / `UBERON:0002773`
7. **Focal Sensory Auditory Seizure ± Receptive Aphasia → Focal to Bilateral Tonic-Clonic Seizure** — `ORGANISM`; `HP:0011158`, `HP:0032696`, `HP:0007334`

Parallel entry nodes: **RELN Secretion Deficiency** (`GO:0038026`, gene `hgnc:9957`) and **MICAL1 Oxidoreductase Gain of Function** (`GO:0030042`, modifier INCREASED, gene `hgnc:20619`), both feeding node (5). A separate **Developmental Arm: Arrested Excitatory Synapse Pruning** (`GO:1905805`, modifier DECREASED, PMID:19701204) feeding node (4) captures the Zhou/Anderson mechanism without overwriting the acute-excitability chain.

**Suggested `discussions` entries:**
- `KNOWLEDGE_GAP` — ~50% of ADEAF families and 92% of unselected EAF probands remain genetically unsolved (PMID:33453592).
- `KNOWLEDGE_GAP` — modifiers explaining 54–85% penetrance are entirely uncharacterized.
- `KNOWLEDGE_GAP` — "benign" (GeneReviews) vs 34.1% terminal remission (PMID:29464704); ascertainment-driven discrepancy, unresolved.
- `HUMAN_MODEL_MISMATCH` — mouse discharges are hippocampal; human semiology is lateral-temporal neocortical; and no model can express an auditory aura.

## Appendix B — Curation warnings

1. **GeneReviews quotes will fail `just validate-references`.** Every frequency I sourced to GeneReviews Table 2 (57–71% auditory, 17–20% aphasic, 88–92% FBTCS, 8–13% sound-triggered) needs re-sourcing to a PubMed-indexed primary paper before it becomes an evidence `snippet`. The RELN paper (PMID:28142128) supplies verifiable substitutes: 71% auditory, 88% FBTCS, 8% noise-precipitated, 80% EEG abnormalities, 96% controlled.
2. **Do not map MICAL1-ADLTE to OMIM ETL8 (616461)** — that entry is GAL-related. Verified via MedGen this session.
3. **ADEAF ≠ anti-LGI1 encephalitis.** Same protein, opposite direction of arrival (germline LoF vs acquired autoantibody), different age, different treatment. Keep them as distinct entries with a cross-reference.
4. **Seed the MONDO caches** for `MONDO:0010898` in both `cache/enums/*.csv` and `cache/mondo/terms.csv` before pushing, and remember the term must be seeded from the worktree, not just the primary checkout.
5. Every mouse-derived claim gets `evidence_source: MODEL_ORGANISM`; every COS7/HEK/neuron-culture claim gets `IN_VITRO`; family series and cohorts get `HUMAN_CLINICAL`.

## Sources

- [GeneReviews: Autosomal Dominant Epilepsy with Auditory Features (NBK1537, PMID:20301709)](https://www.ncbi.nlm.nih.gov/books/NBK1537/)
- [Kalachikov et al., Nat Genet 2002, PMID:11810107](https://pubmed.ncbi.nlm.nih.gov/11810107/)
- [Winawer et al., Neurology 2000, PMID:10851389](https://pubmed.ncbi.nlm.nih.gov/10851389/) · [Winawer et al., Epilepsia 2002, PMID:11879388](https://pubmed.ncbi.nlm.nih.gov/11879388/)
- [Ottman et al., Neurology 2004, PMID:15079011](https://pubmed.ncbi.nlm.nih.gov/15079011/) · [Rosanoff & Ottman, Neurology 2008, PMID:18711109](https://pubmed.ncbi.nlm.nih.gov/18711109/) · [Ho et al., Neurology 2012, PMID:22323750](https://www.neurology.org/doi/10.1212/WNL.0b013e318247ccbf)
- [Dazzo et al., Am J Hum Genet 2015, PMID:26046367](https://pubmed.ncbi.nlm.nih.gov/26046367/) · [Michelucci et al., Epilepsy Behav 2017, PMID:28142128](https://pubmed.ncbi.nlm.nih.gov/28142128/) · [Dazzo et al., Ann Neurol 2018, PMID:29394500](https://pubmed.ncbi.nlm.nih.gov/29394500/) · [Nobile & Dazzo, Genes 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9141472/)
- [Pippucci et al., Neurol Genet 2015, PMID:27066544](https://pmc.ncbi.nlm.nih.gov/articles/PMC4821078/) · [Bisulli et al., Seizure 2021, PMID:33453592](https://www.seizure-journal.com/article/S1059-1311(20)30412-X/fulltext) · [Talarico et al., Int J Mol Sci 2024, PMID:39796146](https://pmc.ncbi.nlm.nih.gov/articles/PMC11719710/)
- [Bisulli et al., Epilepsia 2018, PMID:29464704](https://pubmed.ncbi.nlm.nih.gov/29464704/) · [Furia et al., Front Neurol 2022, PMID:35153984](https://pmc.ncbi.nlm.nih.gov/articles/PMC8829259/) · [Riney et al., Epilepsia 2022](https://onlinelibrary.wiley.com/doi/10.1111/epi.17240)
- [Fukata et al., Science 2006, PMID:16990550](https://pubmed.ncbi.nlm.nih.gov/16990550/) · [Fukata et al., PNAS 2010, PMID:20133599](https://www.pnas.org/doi/10.1073/pnas.0914537107) · [Zhou et al., Nat Med 2009, PMID:19701204](https://pubmed.ncbi.nlm.nih.gov/19701204/) · [Boillot et al., Brain 2014, PMID:25234641](https://academic.oup.com/brain/article/137/11/2984/2391905) · [Yamagata & Fukai, CMLS 2019, PMID:31432233](https://pmc.ncbi.nlm.nih.gov/articles/PMC11104983/) · [Extrémet et al., J Neurosci 2023, PMID:37863654](https://www.jneurosci.org/content/43/50/8596) · [Hirano et al., Brain 2025, PMID:40455867](https://academic.oup.com/brain/article/148/10/3514/8155328)
- [Seppälä et al., PLoS Genet 2011, PMID:21829378](https://pubmed.ncbi.nlm.nih.gov/21829378/) · [Koskinen et al., BMC Genomics 2015, PMID:26084559](https://pubmed.ncbi.nlm.nih.gov/26084559/)
- [gnomAD (constraint metrics via API)](https://gnomad.broadinstitute.org/gene/ENSG00000108231) · [OMIM 616436 / ETL7](https://omim.org/entry/616436) · [ClinicalTrials.gov NCT00072813](https://clinicaltrials.gov/study/NCT00072813)