---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-21T17:02:51.844825'
end_time: '2026-07-21T17:09:29.584173'
duration_seconds: 397.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Erythropoietic Protoporphyria
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
  - claude-opus-4-8
  web_search_requests: 9
  num_turns: 12
  total_cost_usd: 1.7720552499999997
  session_id: aa61b676-b239-41d1-aca2-54a24b193ebc
  stop_reason: end_turn
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Erythropoietic Protoporphyria
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Erythropoietic Protoporphyria** covering all of the
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

Alright, I've got what I need — genetics (FECH loss-of-function + the IVS3-48C low-expression allele, ALAS2 gain-of-function for XLP, CLPX for EPP2), the afamelanotide long-term data, the two oral pipeline drugs (dersimelagon and bitopertin), and the liver story all confirmed against current sources. Writing the full report now.

One housekeeping note up top since this is headed for the KB: I've marked every PMID with how I sourced it. The ones I pulled straight from PubMed/PMC search results are solid; a couple I've flagged **⚠verify** because I'm citing them from memory or a secondary mention — run `just fetch-reference` on those before you paste a snippet into an evidence block.

---

# Erythropoietic Protoporphyria (EPP) — Comprehensive Research Report

*sup — quick orientation before the deep dive. EPP is the one where sunlight isn't a slow tan-and-burn thing but an immediate "my skin is on fire" alarm, sometimes within minutes and with almost nothing to see on the surface. The whole disease is basically one broken step at the very end of the heme assembly line: the enzyme that's supposed to tuck an iron atom into a porphyrin ring quits early, so the ring — protoporphyrin IX — piles up. That ring happens to be a tiny solar panel that turns light into cellular shrapnel. Everything else downstream flows from that one traffic jam.*

---

## 1. Disease Information

**What it is.** Erythropoietic protoporphyria is an inherited disorder of heme biosynthesis caused by partial deficiency of **ferrochelatase (FECH; EC 4.98.1.1)**, the terminal enzyme of the heme pathway, which inserts ferrous iron (Fe²⁺) into protoporphyrin IX (PPIX) to make heme. Reduced FECH activity → accumulation of **metal-free, photoreactive PPIX** in erythroid cells, plasma, skin, and liver. It is the **most common cutaneous porphyria of childhood** and the third most common porphyria overall. A phenotypically identical variant, **X-linked protoporphyria (XLP / XLPP)**, arises from *gain-of-function* mutations in erythroid **ALAS2** that overdrive substrate flux into the same pathway.

**Key identifiers** (MONDO verified locally via `sqlite:obo:mondo`):
- **MONDO:** `MONDO:0001676` (erythropoietic protoporphyria); `MONDO:0008319` (protoporphyria, erythropoietic, 1) — both confirmed present in local MONDO.
- **OMIM:** `#177000` EPP1 (FECH); `#618015` EPP2 (CLPX); `#300752` X-linked protoporphyria (ALAS2). Gene entries: FECH `*612386`, ALAS2 `*301300`, CLPX `*615611`.
- **Orphanet:** ORPHA:79278 (autosomal EPP); a distinct X-linked entry exists for XLP. ⚠verify exact XLP ORPHA code via `just fetch-reference ORPHA:79278` and Orphanet lookup.
- **ICD-10:** E80.0 (hereditary erythropoietic porphyria). **ICD-11:** 5C58.10.
- **MeSH:** D046351 "Protoporphyria, Erythropoietic."
- **HGNC genes:** FECH `hgnc:3647`, ALAS2 `hgnc:397`, CLPX `hgnc:17820`. *(Confirm the numeric HGNC IDs with OAK before committing — repo uses lowercase `hgnc:` prefix.)*

**Synonyms / alternative names:** EPP; protoporphyria; erythrohepatic protoporphyria (older term reflecting liver involvement); ferrochelatase deficiency. For the variant: X-linked dominant protoporphyria, XLPP, XLP.

**Data provenance.** Almost everything here is from **aggregated disease-level resources** — OMIM, Orphanet, GeneReviews, consensus guidelines, and cohort studies from specialist porphyria centers (Mass General, Erasmus MC Rotterdam, UCSF, Mount Sinai). The recent **UK Biobank** analysis is the notable population-genomic (EHR-adjacent) dataset showing systematic underdiagnosis.

---

## 2. Etiology

### Disease causal factors (genetic — three molecular routes to one phenotype)

**Route 1 — FECH loss-of-function (EPP1, ~90% of cases).** The dominant paradigm is genetically counterintuitive and worth stating precisely: most clinically overt patients are **compound heterozygous** for a *rare pathogenic FECH null/missense allele* on one chromosome and a **common hypomorphic low-expression allele, `c.315-48T>C` (IVS3-48C)**, on the other. The IVS3-48C polymorphism strengthens use of a cryptic aberrant splice acceptor, so ~40% of transcripts are aberrantly spliced and degraded by nonsense-mediated decay, lowering steady-state FECH mRNA.

> "For 96% of patients, EPP results from coinheriting a rare pathogenic variant in *trans* of a common hypomorphic variant c.315-48T>C" (minor allele frequency ~0.05). — UK Biobank underdiagnosis study, *Genetics in Medicine* 2021 (PMC7796935; **PMID likely 33257847 ⚠verify**).

> "the IVS3-48C minigene gave rise to 40% aberrantly spliced mRNA, and the IVS3-48T minigene to only 20%." — **PMID:21132468**, *low-expression allele leads to low enzyme activity*.

Residual FECH activity in symptomatic patients is roughly **10–35% of normal**. A minority carry **two loss-of-function FECH alleles** (true autosomal recessive) — this subgroup carries a **higher risk of severe liver disease and palmar keratoderma**.

**Route 2 — ALAS2 gain-of-function (X-linked protoporphyria, ~2–10% overall, up to ~40% in some North American cohorts).** C-terminal frameshift deletions in **exon 11 of ALAS2** — canonically `c.1699_1700delAT` (p.Met567GlufsTer2) and `c.1706_1709delAGTG` (p.Glu569GlyfsTer24) — truncate an autoinhibitory C-terminal region, **increasing ALAS2 activity/stability**. This pushes more 5-aminolevulinic acid into the pathway, so PPIX accumulates *despite normal FECH*.

> "deletions in ALAS2 cause a … X-linked protoporphyria that, in contrast to autosomal dominant porphyrias, has close to 100% penetrance." — Whatley et al., *Am J Hum Genet* 2008 (**PMID:18760763 ⚠verify**).

**Route 3 — CLPX dominant mutation (EPP2, very rare).** A heterozygous **CLPX p.Gly298Asp** mutation in the mitochondrial AAA+ unfoldase CLPX impairs its normal turnover of ALAS, stabilizing ALAS and raising PPIX — an indirect gain-of-function on the same node.

> "Cells with the mutant protein showed … increased posttranslational stability of ALAS and pathologic accumulation of PPIX." — Yien et al., *PNAS* 2017 (**PMID:28874591**).

### Risk / modifying factors
- **Iron status:** iron deficiency tends to *worsen* EPP (limits FECH substrate/activity and de-represses ALAS2); iron repletion may help XLP but effects are variable and sometimes worsen classic EPP — a genuinely unresolved clinical knob.
- **Sunlight** is the phenotype **trigger**, not a cause. Even visible violet light (~400–410 nm) transmitted through window glass provokes symptoms.
- **Hepatotoxic stressors** (alcohol, fasting, drugs that induce ALAS/CYP, intercurrent illness) can precipitate hepatic decompensation once liver disease exists.
- **Genetic ancestry:** IVS3-48C allele frequency is markedly higher in East/Southeast Asian and Japanese populations than in Northern Europeans, shaping regional penetrance patterns.
- **Consanguinity** matters for the rare biallelic-LOF autosomal recessive form.

### Protective factors
- **Homozygosity for the high-expression IVS3-48T allele** in *trans* to a pathogenic FECH mutation → subclinical/latent carriers (higher residual FECH). This is the single strongest protective genetic factor.
- **Constitutive skin melanin** (darker pigmentation) is modestly photoprotective — the mechanistic basis for the afamelanotide/dersimelagon therapeutic strategy.

### Gene–environment interaction
The defining GxE story is **genotype (FECH residual activity) × light dose × iron availability**. The trans-allele expression level sets a PPIX ceiling; ambient light converts that latent chemistry into phenotype; iron status tunes flux at both FECH and ALAS2.

---

## 3. Phenotypes

Suggested HPO anchors in brackets.

**Acute cutaneous phototoxicity (near-universal, ~99%; onset infancy–early childhood).**
- **Painful, burning/stinging/prickling photosensitivity** within minutes of sun exposure, often with little visible sign at first — a hallmark that causes years of diagnostic delay. `[HP:0000992 Cutaneous photosensitivity]`, pain `[HP:0012531]`.
- Erythema `[HP:0000988 skin rash / HP:0010783 erythema]`, edema, pruritus. Blistering is *uncommon* (distinguishes EPP from other cutaneous porphyrias like PCT).
- Severity **moderate–severe and highly disabling**; course **episodic/acute-on-chronic** (each light exposure is a discrete event), lifelong.

**Chronic skin changes (frequent with cumulative exposure).**
- Waxy thickening/lichenification over the knuckles and dorsal hands, shallow linear/pitted scars on the nose and cheeks, leathery hyperkeratosis. `[HP:0000962 Hyperkeratosis]`, scarring `[HP:0100699]`.

**Hepatobiliary.**
- **Cholelithiasis** — PPIX-rich pigment gallstones, often at a young age `[HP:0001081 Cholelithiasis]`. Common.
- **Protoporphyric hepatopathy** — mild transaminase elevation in up to ~20% of LOF-FECH patients; **severe cholestatic liver disease / acute liver failure in ~2–5%**. `[HP:0001394 Cirrhosis]`, cholestasis `[HP:0001396]`, hepatic failure `[HP:0001399]`.

> "Liver involvement is observed in 5%–20% of patients harbouring loss-of-function FECH variants and its manifestations are heterogeneous, ranging from mildly elevated liver transaminases, cholelithiasis to severe acute cholestatic hepatitis/liver failure." — *Erythropoietic protoporphyrias: Pathogenesis, diagnosis and management* (PMC11669082).

**Hematologic.**
- **Mild microcytic, hypochromic anemia** with low ferritin/iron stores in a substantial fraction `[HP:0001935 Microcytic anemia]`. Usually mild and non-hemolytic.

**Secondary / systemic.**
- **Vitamin D deficiency** and reduced bone mineral density from lifelong sun avoidance `[HP:0100512 Decreased vitamin D level]`, osteopenia `[HP:0000938]`.
- **Motor polyneuropathy** — a rare, dramatic complication seen in acute protoporphyric liver failure.

**Quality of life.** Impact is large and under-appreciated: patients organize life around darkness, curtail schooling/work/socializing, and report anxiety and depression. QoL instruments respond strongly to treatment — in an Austrian afamelanotide cohort the EPP-QoL score rose from a median of **11.11 to 79.17** and phototoxic burn-tolerance time from **15 to 250 minutes** (*JDDG* 2023, Seidl-Philipp et al.).

---

## 4. Genetic / Molecular Information

**Causal genes.**
| Gene | Locus | Mechanism | Disorder | OMIM |
|---|---|---|---|---|
| **FECH** | 18q21.31 | Loss of function | EPP1 (~90%) | #177000 |
| **ALAS2** | Xp11.21 | Gain of function | XLP | #300752 |
| **CLPX** | 15q22.31 | Dominant, stabilizes ALAS | EPP2 (rare) | #618015 |

**Pathogenic variants.**
- **FECH:** >180 reported alleles — missense, nonsense, splice-site, small indels, and **large multi-exon/whole-gene deletions**. Most are private/family-specific null alleles. The recurring functional partner is the common **IVS3-48C hypomorph** (gnomAD MAF ~0.05 in Europeans; considerably higher in East Asians). ClinVar RCV000000592 covers the c.315-48T>C allele.
- **ALAS2:** recurrent C-terminal exon-11 frameshifts (`c.1699_1700delAT`, `c.1706_1709delAGTG`); additional deletions reported (e.g., a four-base ALAS2 deletion in a Chinese pedigree, PMC7186625).
- **CLPX:** single dominant `p.Gly298Asp` to date.

**Variant classification / origin.** Germline. FECH nulls → **loss of function**; ALAS2 C-terminal deletions → **gain of function**; CLPX → dominant with a gain-of-function-*like* effect on ALAS stability. No somatic involvement (this is not a neoplastic process).

**Modifier genes.** The FECH IVS3-48C allele is the canonical modifier/permissive locus. Iron-regulatory genes and **ALAS2** iron-responsive-element biology modulate flux. Zygosity for LOF FECH modifies liver-disease risk.

**Epigenetics / chromosomal abnormalities.** No established disease-driving epigenetic marks; the IVS3-48C effect is a *splicing* phenomenon, not methylation. Large FECH deletions are the relevant structural lesions (detectable by MLPA/CMA when sequencing is negative). No aneuploidy association.

---

## 5. Environmental Information

- **Environmental factor (defining):** **visible light, ~400–410 nm (violet/Soret band)** — the phenotype's obligatory trigger. Passes through window glass; even fluorescent/operating-room lighting can burn.
- **Lifestyle:** alcohol and fasting stress the liver; smoking and hepatotoxins accelerate hepatopathy in susceptible patients. Sun-avoidance lifestyle itself causes secondary vitamin D deficiency.
- **Occupational:** outdoor work is often untenable; even phototherapy lamps and surgical lights are hazards (surgical-light phototoxic burns are a documented intra-operative risk in EPP patients).
- **Infectious agents:** none causal. (Hepatitis A/B are relevant only as *avoidable* liver insults — hence vaccination is recommended.)

---

## 6. Mechanism / Pathophysiology

**Core causal chain (upstream → downstream):**

1. **Enzymatic block at the terminal heme step.** FECH deficiency (or ALAS2/CLPX overdrive) → the metal-insertion step fails or is outrun. `[GO:0004325 ferrochelatase activity; GO:0006783 heme biosynthetic process]`. FECH is an **inner-mitochondrial-membrane** enzyme `[GO:0005743]`.
2. **PPIX accumulation in erythroid cells.** The bone-marrow **reticulocyte/erythroblast** is the dominant source of excess **metal-free protoporphyrin IX** `[CHEBI:15430 protoporphyrin IX]`; in XLP, **zinc-protoporphyrin** rises too. Cell types: `[CL:0000765 erythroblast; CL:0000558 reticulocyte]`.
3. **Systemic distribution.** Lipophilic PPIX loads into erythrocytes and plasma, deposits in skin, and is excreted into bile — the only elimination route (not renal).
4. **Cutaneous phototoxicity (the acute arm).** PPIX absorbs violet light → excited **triplet state** → **type I/II photochemistry generating singlet oxygen and other reactive oxygen species** `[GO:0006979 response to oxidative stress]` → oxidative injury to dermal microvascular **endothelium** `[CL:0000115]`, **mast-cell** degranulation `[CL:0000097]`, and complement activation → immediate neurogenic/inflammatory **pain and edema**. `[GO:0009416 response to light stimulus]`.
5. **Protoporphyric hepatopathy (the chronic/severe arm).** PPIX is cholestatic and directly hepatotoxic: it precipitates as crystalline deposits in **hepatocytes** `[CL:0000182]` and bile canaliculi, injuring **cholangiocytes** `[CL:0002326]` and Kupffer cells → **cholestasis** → reduced biliary PPIX clearance → *further* hepatic PPIX retention. This **feed-forward vicious cycle** is what converts stable disease into fulminant liver failure.

> "Protoporphyric hepatopathy results from the accumulation of protoporphyrin in hepatocytes and bile canaliculi, with toxic effects on cholangiocytes and Kupffer cells leading to cholestasis." — liver-management consensus guidelines (PMC10818013).

**Protein dysfunction.** FECH is a homodimeric `[2Fe-2S]`-cluster mitochondrial enzyme; pathogenic variants reduce catalytic activity or destabilize the protein. ALAS2 C-terminal deletions remove an autoinhibitory element (structural gain of function). CLPX G298D disrupts unfoldase-mediated ALAS turnover.

**Metabolic changes.** The lesion is confined to the **heme biosynthetic pathway** (KEGG map00860); the phenotype is a substrate-accumulation disease — no broad energy-metabolism derangement, though secondary anemia reflects constrained heme output.

**Immune involvement.** Innate/inflammatory rather than autoimmune — ROS-driven mast cell and complement activation in skin; sterile inflammatory hepatic injury.

**Molecular profiling.** The bitopertin mechanistic work used **CD34⁺-derived and iPSC-derived erythroid cultures** to show that limiting glycine (via GlyT1) reduces PPIX — an *in vitro* substrate-limitation demonstration (PMC12435829 / PMC12435834). Erythroid-specific transcriptional control of ALAS2 (GATA1, iron-responsive element) is the relevant expression biology.

---

## 7. Anatomical Structures Affected

- **Skin** `[UBERON:0002097 skin of body]`, specifically **sun-exposed sites** — face, dorsal hands, ears, nose (bilateral, symmetric, light-distribution).
- **Liver** `[UBERON:0002107]` and **biliary tract / gallbladder** `[UBERON:0002110 gallbladder; UBERON:0002394 bile duct]`.
- **Bone marrow** `[UBERON:0002371]` — the erythroid production source of excess PPIX.
- **Blood / erythrocytes** `[UBERON:0000178 blood]`.
- **Subcellular:** **mitochondrion** `[GO:0005739]` (site of FECH, ALAS2, and terminal heme synthesis); mitochondrial inner membrane `[GO:0005743]`.
- **Secondary:** bone `[UBERON:0002481]` (low BMD from vitamin D deficiency); peripheral nerves (post-liver-failure neuropathy).

---

## 8. Temporal Development

- **Onset:** typically **infancy to early childhood** — often the first prolonged sun exposures. Screaming/crying with sun in a nonverbal infant is a classic (and easily missed) presentation.
- **Onset pattern of episodes:** **acute** (minutes) with each light exposure; underlying disease is **chronic and lifelong**.
- **Progression:** skin phenotype is generally **stable in severity** across life (not progressive neurodegeneration-style). The dangerous variable is **hepatic**: usually absent/mild, but can convert to **rapid, life-threatening acute liver failure**, sometimes precipitated by an intercurrent stressor.
- **Course:** non-remitting baseline; phototoxic events are **episodic/provoked**. Symptom-free periods require darkness, not spontaneous remission.
- **Critical windows:** liver-function surveillance is the key intervention window — catching rising PPIX/LFTs before decompensation is what changes outcomes.

---

## 9. Inheritance and Population

**Inheritance patterns.**
- **EPP1:** operationally behaves as **autosomal recessive / pseudodominant** — clinical disease usually requires a rare LOF FECH allele *in trans* to the common IVS3-48C hypomorph (a "one severe hit + one weak hit" model). Rare biallelic-LOF families are frankly recessive. HPO inheritance: `[HP:0000007 Autosomal recessive]` for the two-hit model; some pedigrees historically labeled autosomal dominant with low penetrance.
- **XLP:** **X-linked** `[HP:0001417]`; near-100% penetrance in hemizygous males, variable in heterozygous females depending on **X-inactivation** (skewed lyonization can make carrier females symptomatic — PMID:25615817).
- **EPP2 (CLPX):** autosomal dominant `[HP:0000006]`.

**Penetrance / expressivity.** Penetrance of the FECH mutation is *gated by the trans-allele expression level* — the reason many obligate carriers are asymptomatic. Expressivity is **variable** (mild latent to severe with hepatopathy).

**Epidemiology.**
- **Prevalence:** commonly cited **1:75,000 (Netherlands) to 1:200,000 (Wales)**; worldwide range ~1:17,000–1:100,000. Europe-wide diagnosed prevalence ≈ **0.00092%**.
- **Underdiagnosis:** UK Biobank genetics suggest true prevalence is **~2.3× higher** than clinically estimated (corrected ≈ **0.0059%**); diagnosis is frequently delayed >10 years.

> "the prevalence of erythropoietic protoporphyria is 2.3 times higher than previously estimated in Europe" — UK Biobank underdiagnosis analysis (*Genetics in Medicine* 2021).

- **Sex ratio:** roughly equal for EPP1; male predominance among symptomatic XLP.
- **Ancestry:** higher IVS3-48C frequency in East/Southeast Asian populations; XLP proportion notably higher in North American cohorts (~40% in one Mount Sinai series, PMC3646094).
- **Age distribution:** overwhelmingly diagnosed in children once symptomatic; carriers span all ages.

---

## 10. Diagnostics

**The decisive biochemical test:** markedly **elevated total erythrocyte protoporphyrin with a predominance of metal-free (non-zinc) PPIX**. `[LOINC candidates for erythrocyte protoporphyrin; confirm exact LOINC codes]`.

- **Fractionation** is critical and distinguishes entities:
  - **EPP1:** mostly **metal-free PPIX** (zinc-PP fraction typically <15%).
  - **XLP:** substantially higher **zinc-protoporphyrin** fraction (~15–50%).
  - **Iron deficiency / lead poisoning:** predominantly **zinc-protoporphyrin** (helps exclude mimics).
- **Plasma fluorescence scan:** emission peak at **~634 nm** — a rapid confirmatory screen.
- **Biochemistry pattern:** urinary porphyrins are typically **normal** (PPIX is not water-soluble) — a useful negative that separates EPP from acute hepatic porphyrias.

**Genetic testing.**
- **FECH:** sequencing for the rare pathogenic allele **plus targeted IVS3-48C genotyping** (essential — the common allele won't be flagged as pathogenic on its own). **MLPA/deletion analysis** when sequencing finds only one or no variant (large FECH deletions).
- **ALAS2:** targeted **exon 11** analysis for C-terminal frameshifts when biochemistry suggests XLP.
- **CLPX:** consider in FECH/ALAS2-negative dominant pedigrees.
- Gene panels (porphyria panels) and WES are reasonable when the phenotype is atypical.

**Monitoring labs.** LFTs (surveillance for hepatopathy), ferritin/iron studies, **25-OH vitamin D**, CBC.

**Imaging / pathology.** Not required for diagnosis. Liver biopsy in hepatopathy shows **birefringent, Maltese-cross PPIX deposits** under polarized light; abdominal imaging for gallstones.

**Differential diagnosis.** Other cutaneous porphyrias (PCT, variegate, hereditary coproporphyria — but those blister and have abnormal urinary porphyrins), solar urticaria, polymorphous light eruption, phototoxic drug reactions, hydroa vacciniforme. The **immediate painful, largely non-blistering** photosensitivity with **normal urinary porphyrins** is the discriminating fingerprint.

**Screening.** No newborn screening. **Cascade genetic testing** of first-degree relatives (for both the LOF allele and IVS3-48C) is appropriate for counseling.

---

## 11. Outcome / Prognosis

- **Life expectancy:** **normal for the great majority**; the disease's weight is on quality of life, not survival — *except* for the small subset with progressive liver disease.
- **Principal mortality driver:** **protoporphyric liver failure** (~2–5%). Rare but potentially fatal, and can be abrupt.
- **Morbidity:** chronic pain, profound activity restriction, social/occupational limitation, secondary vitamin D deficiency/low BMD, and cholelithiasis. QoL scores are low at baseline and highly treatment-responsive.
- **Prognostic factors:** **biallelic LOF FECH genotype**, very high/rising erythrocyte PPIX, and abnormal LFTs flag higher hepatic risk. Erythrocyte PPIX level tracks disease burden and is the practical biomarker.
- **Recovery:** phototoxic symptoms are fully reversible with light avoidance/therapy; liver failure is not reversible without transplant ± marrow replacement.

---

## 12. Treatment

*The therapeutic logic splits cleanly: (a) shield the solar panel or darken the skin over it, (b) turn down PPIX production at the source, and (c) rescue the liver when the feed-forward cycle runs away.*

**Photoprotection & supportive care (foundation).**
- Strict sunlight avoidance, protective clothing, and **opaque physical sunscreens with visible-light reflectants** (zinc oxide, titanium dioxide, **iron-oxide-tinted** formulations — chemical UV filters alone are useless here because the culprit is *visible* light). `[MAXO:0000950 supportive care]`.
- **Vitamin D supplementation**; **hepatitis A/B vaccination** to protect the vulnerable liver.

**Melanocortin-1-receptor agonists (approved / advanced pipeline).**
- **Afamelanotide (Scenesse)** — α-MSH analog **MC1R agonist**, subcutaneous controlled-release implant every ~60 days; stimulates eumelanin to raise the phototoxic threshold. **EMA-approved 2014, FDA-approved 2019.** Randomized and long-term real-world data show longer pain-free sun exposure and large QoL gains. `[MAXO/NCIT:C15986 Pharmacotherapy; therapeutic_agent: afamelanotide]`.

> "Afamelanotide … increased duration of sun exposure without pain and improved quality of life." — Langendonk et al., *N Engl J Med* 2015 (**PMID:26132941**).

- **Dersimelagon (MT-7117)** — **oral, non-peptide selective MC1R agonist**; phase 2 (ENDEAVOR) met its primary endpoint (increased pain-free sun-exposure time), with phase 3 in EPP/XLP (NCT extension NCT05005975). A genuinely convenient oral alternative to implants if approved. `[therapeutic_modality: SMALL_MOLECULE]`.

**Substrate-limiting / disease-modifying (investigational).**
- **Bitopertin** — **oral glycine transporter-1 (GlyT1) inhibitor** that starves the very first heme step of glycine, lowering PPIX at the source (potentially *disease-modifying* rather than just photoprotective). The randomized **AURORA** phase 2 (75 patients, 20/60 mg vs placebo, 17 weeks) showed **dose-dependent whole-blood PPIX reductions of −21.6% (20 mg) and −40.7% (60 mg)**; sunlight-tolerance improvements did not reach significance against a strong placebo response.

> "Bitopertin shows efficacy in patients with erythropoietic protoporphyria: Results from the randomized, double-blind, placebo-controlled AURORA trial." — **PMID:41390126** ⚠verify (recent; fetch before quoting).

**Older adjuncts (limited evidence):** oral **β-carotene** (historical, modest at best), cysteine, N-acetylcysteine, antioxidants, narrowband UVB skin-hardening.

**Liver disease management (escalating).**
- Suppress erythroid PPIX output and promote elimination: **cholestyramine / activated charcoal** (interrupt enterohepatic PPIX recycling), **ursodeoxycholic acid**, **IV hemin/heme arginate** (represses erythroid ALAS), **RBC exchange transfusion / plasmapheresis**, iron optimization.
- **Liver transplantation** for acute protoporphyric liver failure — *life-saving but NOT curative*, because the marrow keeps overproducing PPIX and can damage the graft. `[MAXO:0010039 organ transplantation]`.
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the **only curative therapy**, as it replaces the erythroid PPIX source; performed after liver transplant in the combined strategy for severe cases.

> "The strategy of hematopoietic stem cell transplantation after liver transplantation cures erythropoietic protoporphyria and prevents recurrent erythropoietic protoporphyria from damaging the allograft." — liver-disease consensus guidelines (PMC10818013).

**Pharmacogenomics.** No routine PGx gating, but genotype *is* the therapeutic map: XLP (ALAS2) is the strongest rationale for source-reduction approaches (bitopertin, hemin), while FECH-EPP with hepatopathy anchors the transplant/HSCT pathway.

---

## 13. Prevention

- **Primary prevention:** none (inherited) — but **genetic counseling and cascade family testing** identify at-risk relatives, and **prenatal testing / preimplantation genetic diagnosis** are available for known familial variants. `[MAXO:0000079 genetic counseling]`.
- **Secondary prevention:** photoprotection to prevent phototoxic injury; **annual LFT/PPIX surveillance** to catch hepatopathy early; **vitamin D** repletion; **hepatitis A/B vaccination**; avoidance of alcohol and hepatotoxins.
- **Tertiary prevention:** aggressive early management of rising PPIX/abnormal LFTs to head off liver failure; timely referral to a specialist porphyria center with transplant capability.
- **Public-health angle:** raising clinician awareness is itself a prevention lever — the >10-year diagnostic delay is the biggest modifiable failure point.

---

## 14. Other Species / Natural Disease

- **Taxonomy of natural/model disease:** mouse `[NCBITaxon:10090]`, cattle `[NCBITaxon:9913]`, zebrafish `[NCBITaxon:7955]`.
- **Bovine protoporphyria** — a naturally occurring FECH-deficiency disease documented in cattle (notably **Limousin**), with photosensitivity paralleling human EPP; catalogued in **OMIA**. `[VBO breed term for Limousin — verify]`.
- **Orthologous genes:** Fech, Alas2, Clpx are conserved across mammals and in zebrafish; the pathway is deeply conserved (heme synthesis is ancient), making cross-species mechanism transfer strong.
- **Comparative biology:** natural bovine and induced rodent/fish models reproduce both the photosensitivity and, in FECH-null rodents, the hepatopathy — a nice illustration of evolutionary conservation of the PPIX-phototoxicity mechanism.
- **Zoonosis:** not applicable (non-infectious, non-transmissible).

---

## 15. Model Organisms

- **Fech^m1Pas mouse** (BALB/c background; a chemically induced *Fech* point mutation, Tutois et al.) — the workhorse model; homozygotes recapitulate **cutaneous photosensitivity + cholestatic liver disease + biliary PPIX deposits**, capturing both arms of human disease. `[evidence_source: MODEL_ORGANISM]`. **⚠verify PMID** (Tutois 1991, *J Clin Invest*).
- **Ferrochelatase c.315-48C modifier mouse** — engineered to model the human low-expression splice modifier (PMC5374324), directly testing the IVS3-48C mechanism *in vivo*.
- **CLPX mouse models** — probe the ALAS-stabilization mechanism of EPP2.
- **Zebrafish *dracula* (fech mutant)** — classic vertebrate heme-synthesis model showing porphyrin accumulation and light-dependent hemolysis/phenotype.
- **Chemically induced protoporphyria** — griseofulvin or **DDC (3,5-diethoxycarbonyl-1,4-dihydrocollidine)** feeding induces PPIX accumulation and protoporphyric hepatopathy in rodents; a standard tool for studying the liver arm.
- **Cellular / in vitro models** — **CD34⁺-derived and iPSC-derived erythroid cultures** used to demonstrate GlyT1/glycine-limitation reduction of PPIX (the bitopertin mechanism; PMC12435829/PMC12435834). `[evidence_source: IN_VITRO]`.
- **Model resources:** MGI (*Fech*, *Alas2*, *Clpx*), ZFIN (*fech*), OMIA (bovine protoporphyria), IMPC/IMSR for allele availability.
- **Recapitulation vs limitations:** rodent Fech models capture skin + liver disease well; the **compound-heterozygous IVS3-48C human genetics** (a splicing hypomorph) is *not* naturally reproduced by simple null alleles — the engineered c.315-48C mouse exists specifically to close that human-model gap. Consider a `HUMAN_MODEL_MISMATCH` discussion note if you're modeling the splice-modifier arm.

---

## Priority citation set for the KB entry

Verified via PubMed/PMC search this session (safe to fetch and quote):
- **PMID:26132941** — Langendonk et al., afamelanotide RCT, *NEJM* 2015.
- **PMID:28874591** — Yien et al., CLPX/EPP2, *PNAS* 2017.
- **PMID:21132468** — FECH IVS3-48C low-expression allele → low enzyme activity.
- **PMID:30704898** — Balwani, EPP & XLP pathophysiology/genetics/management review.
- **PMID:25615817** — X-inactivation and XLP phenotype in females.
- *Blood* 2023;141:2921–2931 — Karp Leaf & Dickey, "How I treat EPP and XLP" (**fetch for PMID**).
- PMC10818013 — consensus guidelines, protoporphyria-related liver dysfunction.
- PMC7796935 — UK Biobank underdiagnosis (*Genet Med* 2021).

**⚠verify before quoting** (cited from memory or secondary mention): **PMID:18760763** (Whatley ALAS2 2008), the AURORA bitopertin primary paper (**PMID:41390126**), the dersimelagon phase 2 primary paper, and the Fech^m1Pas mouse origin paper. Run `just fetch-reference PMID:XXXX` and confirm the snippet is an exact abstract substring before any of these lands in an evidence block — standard DR-hallucination hygiene per the repo SOP.

---

### Sources
- [OMIM #177000 EPP1](https://omim.org/entry/177000) · [OMIM #618015 EPP2/CLPX](https://www.omim.org/entry/618015) · [OMIM #300752 XLP](https://omim.org/entry/300752) · [OMIM ALAS2 *301300](https://omim.org/entry/301300)
- [Orphanet: Autosomal erythropoietic protoporphyria](https://www.orpha.net/en/disease/detail/79278) · [StatPearls EPP](https://www.ncbi.nlm.nih.gov/books/NBK563141/) · [MSD Manual: EPP & XLP](https://www.msdmanuals.com/professional/hematology-and-oncology/the-porphyrias/erythropoietic-protoporphyria-and-x-linked-protoporphyria) · [NORD: EPP](https://rarediseases.org/rare-diseases/erythropoietic-protoporphyria/)
- [IVS3-48C low-expression allele (PMID:21132468)](https://pubmed.ncbi.nlm.nih.gov/21132468/) · [c.315-48C modifier mouse (PMC5374324)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5374324/) · [ClinVar c.315-48T>C](https://www.ncbi.nlm.nih.gov/clinvar/RCV000000592.6/)
- [Whatley ALAS2 C-terminal deletions 2008 (PDF)](https://codene.porphyrie.net/2015/07/Whatley_2008.pdf) · [ALAS2 GOF characterization (PMID:23348515)](https://pubmed.ncbi.nlm.nih.gov/23348515/) · [X-inactivation in XLP (PMID:25615817)](https://pubmed.ncbi.nlm.nih.gov/25615817/) · [North American FECH/ALAS2 cohort (PMC3646094)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3646094/)
- [Yien CLPX/PPIX (PMID:28874591 / PNAS)](https://www.pnas.org/doi/10.1073/pnas.1700632114) · [Role of ClpX in EPP (PMC6001922)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6001922/)
- [Balwani EPP/XLP review (PMID:30704898)](https://pubmed.ncbi.nlm.nih.gov/30704898/) · [Erythropoietic protoporphyrias: pathogenesis/diagnosis/management (PMC11669082)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669082/) · [How I treat EPP/XLP, Blood 2023](https://ashpublications.org/blood/article/141/24/2921/494865/How-I-treat-erythropoietic-protoporphyria-and-X)
- [Liver-dysfunction consensus guidelines (PMC10818013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10818013/) · [Cholestatic liver disease case report](https://www.sciencedirect.com/science/article/pii/S2214426923000642)
- [Afamelanotide NEJM 2015 (PMID:26132941)](https://pubmed.ncbi.nlm.nih.gov/26132941/) · [Austrian afamelanotide QoL cohort (JDDG 2023)](https://onlinelibrary.wiley.com/doi/10.1111/ddg.15996) · [US afamelanotide cohort (PMC11204624)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11204624/) · [3-year afamelanotide observational study (PMID:32811524)](https://pubmed.ncbi.nlm.nih.gov/32811524/)
- [Dersimelagon MT-7117 extension NCT05005975](https://clinicaltrials.gov/study/NCT05005975) · [Bitopertin meets phase 2 endpoint (HCPLive)](https://www.hcplive.com/view/bitopertin-meets-primary-phase-2-endpoint-erythropoietic-protoporphyria) · [AURORA bitopertin RCT (PMID:41390126)](https://pubmed.ncbi.nlm.nih.gov/41390126/) · [GlyT1/glycine-uptake mechanism (PMC12435829)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12435829/)
- [UK Biobank underdiagnosis (Genet Med 2021, PMC7796935)](https://ncbi.nlm.nih.gov/pmc/articles/PMC7796935) · [Mass General: prevalence underestimated](https://advances.massgeneral.org/pulmonary/journal.aspx?id=1762) · [GeneReviews: EPP, autosomal recessive](https://www.ncbi.nlm.nih.gov/books/NBK100826/)

**Bottom line for curation:** EPP is a clean, well-understood substrate-accumulation disease that maps neatly onto the dismech pathograph — one enzymatic block (FECH↓, or ALAS2↑ / CLPX for the variants), PPIX buildup, then a *forking* downstream into an **acute photochemical skin arm** (light → singlet oxygen → dermal injury) and a **chronic hepatic arm** (PPIX cholestasis → feed-forward liver failure). The genetics deserve special care in the entry: model the **two-hit FECH-null + IVS3-48C hypomorph** genotype explicitly (it's the whole reason penetrance is weird), and give **X-linked protoporphyria** its own subtype block with the ALAS2 gain-of-function mechanism rather than folding it in silently.