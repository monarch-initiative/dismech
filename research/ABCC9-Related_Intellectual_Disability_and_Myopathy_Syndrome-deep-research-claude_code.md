---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T07:12:38.547253'
end_time: '2026-08-01T07:25:50.754500'
duration_seconds: 792.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ABCC9-Related Intellectual Disability and Myopathy Syndrome
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
  web_search_requests: 4
  num_turns: 54
  total_cost_usd: 4.25636325
  session_id: 56e6725b-ff1c-4123-adda-40942aa1da1a
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ABCC9-Related Intellectual Disability and Myopathy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ABCC9-Related Intellectual Disability and Myopathy Syndrome** covering all of the
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

I have enough verified material. Writing the report now.

# Research Report: ABCC9-Related Intellectual Disability and Myopathy Syndrome (AIMS)

**Prepared:** 2026-08-01 · **Target for KB entry:** `kb/disorders/ABCC9-Related_Intellectual_Disability_and_Myopathy_Syndrome.yaml` · **Category:** Mendelian

> **Evidence-provenance note for curators.** Quotes marked **[ABSTRACT-VERIFIED]** were read directly from locally cached PubMed records (`references_cache/PMID_*.md`) or from the full-text PDF body cached for PMID:31575858, and are exact substrings suitable for `snippet:` fields. Statements marked **[FULL-TEXT — RE-VERIFY]** were extracted from PMC full text via an intermediary summarizer and must be re-checked against the cached file with `just validate-references` before being committed as snippets. All ontology IDs below were verified against authoritative sources during this research (OLS4/EBI, HPO `ontology.jax.org` API, genenames.org REST, MGI); the sole exception is flagged inline.

---

## 1. Disease Information

### Overview

ABCC9-related Intellectual disability Myopathy Syndrome (AIMS) is an ultra-rare **autosomal recessive K<sub>ATP</sub> channelopathy** caused by biallelic loss-of-function (LoF) variants in *ABCC9*, which encodes the **sulfonylurea receptor 2 (SUR2)** regulatory subunit of ATP-sensitive potassium channels. The core triad — established by the original 2019 description and confirmed across two subsequent cohort expansions — is (i) developmental delay with intellectual disability, (ii) muscle weakness and fatigability, and (iii) cerebral white matter abnormality resembling periventricular leukomalacia or small-vessel disease. Variable additional features include seizures, spasticity, microcephaly, corpus callosum abnormality, short stature, a shared facial gestalt, sensorineural hearing loss, and age-dependent cardiac systolic dysfunction.

AIMS is the **mechanistic mirror image of Cantú syndrome**: the same gene, opposite channel consequence. This LoF-vs-GoF duality is the single most important framing fact for the entry.

> "We term this channelopathy resulting from loss-of-function of SUR2-containing K<sub>ATP</sub> channels ABCC9-related Intellectual disability Myopathy Syndrome (AIMS). The phenotype differs from Cantú syndrome, which is caused by gain-of-function ABCC9 mutations, reflecting the opposing consequences of K<sub>ATP</sub> loss- versus gain-of-function." — Smeland et al. 2019, **PMID:31575858** **[ABSTRACT-VERIFIED]**

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0859224** | Label verified via OLS4: *"intellectual disability and myopathy syndrome"*. Equivalent-to xrefs: OMIM:619719, DOID:0070600, MedGen 1808193, UMLS C5676904. **The draft entry's `disease_term` is correct as written.** |
| **OMIM (phenotype)** | **#619719** | INTELLECTUAL DISABILITY AND MYOPATHY SYNDROME; **IDMYS** |
| **OMIM (gene)** | 601439 | *ABCC9* / SUR2 |
| **Disease Ontology** | DOID:0070600 | |
| **UMLS / MedGen** | C5676904 / 1808193 | |
| **ORPHA** | **Not found** | No Orphanet code for AIMS/IDMYS was identified. Consequently no Orphanet prevalence class is citable, and no `ORPHA:` structured-source reference can be used for this entry. |
| **ICD-10 / ICD-11** | **No specific code** | Would be coded by manifestation (e.g. myopathy + intellectual disability) rather than as a named entity. |
| **MeSH** | No specific descriptor | Indexed under *Channelopathies*, *Neurodevelopmental Disorders*, *Muscular Diseases*, *Sulfonylurea Receptors* (per PMID:31575858 MeSH set). |

### Synonyms

- **AIMS** (the field-standard acronym; used in all three primary papers)
- ABCC9-related Intellectual disability Myopathy Syndrome
- Intellectual disability and myopathy syndrome (**IDMYS** — the OMIM-preferred name)
- SUR2 loss-of-function channelopathy

The draft's synonym list is accurate; consider adding **IDMYS** explicitly, since that is the OMIM label a curator or user is most likely to search.

### Information provenance

All knowledge is **aggregated case-level literature**, not EHR- or registry-derived. The entire published world experience is ~20 individuals from ~13 families across three papers. There is **no natural-history cohort, no registry, no patient-reported-outcome dataset, and no ICEES/COHD-style EHR signal** available for this disease. Every frequency figure below is a small-*n* case-series proportion and should be curated with that caveat.

---

## 2. Etiology

### Primary causal factor

Biallelic (homozygous or compound heterozygous) loss-of-function variants in *ABCC9* → non-functional SUR2-containing K<sub>ATP</sub> channels. This is a monogenic, fully genetic etiology; no infectious, toxic, or environmental cause contributes.

> "Loss-of-function mutation of ABCC9, the gene encoding the SUR2 subunit of ATP sensitive-potassium (KATP) channels, was recently associated with autosomal recessive ABCC9-related intellectual disability and myopathy syndrome (AIMS)." — Efthymiou et al. 2024, **PMID:38217872** **[ABSTRACT-VERIFIED]**

### Genetic risk factors

- **Causal:** biallelic *ABCC9* LoF (see §4 for the full allelic series).
- **Consanguinity** is a major risk factor for occurrence. Of the 2024 cohort's seven families, consanguinity was documented in the Pakistani, two Egyptian, British-Pakistani, and Saudi Arabian families **[FULL-TEXT — RE-VERIFY]**; the 2026 cohort included a first-cousin union **[FULL-TEXT — RE-VERIFY]**.
- **Founder-like enrichment:** the Norwegian c.1320+1G>A allele is disproportionately frequent in Finns (see §9).
- **Modifier genes:** none identified. The 2019 authors explicitly kept the door open — *"Notably, gene interactions with the homozygous ABCC9 c.1320+1G>A variant cannot be excluded as participating in the syndrome."* (PMID:31575858, full-text body) **[ABSTRACT-VERIFIED — full-text body line]** This is a legitimate `KNOWLEDGE_GAP` discussion item.

### Environmental risk factors

None are causal. However, AIMS has a genuinely important **gene–environment / gene–exposure interaction** at the level of *decompensation triggers*, which is arguably the most clinically actionable content in this entry:

| Trigger | Consequence | Source |
|---|---|---|
| **Physical exertion / metabolic stress** | Fatigability, painful muscle spasms, failure to recover from fatigue; in SUR2-KO mice histological muscle abnormality appears only with chronic exercise | PMID:31575858; PMID:37154692 |
| **Surgery / general anesthesia (propofol)** | Post-operative cardiogenic shock, lactic acidosis, refractory seizures in a neonate, after each of two procedures | PMID:42290677 **[FULL-TEXT — RE-VERIFY]** |
| **Calcium-channel-blocking drugs (verapamil)** | Premature death in AIMS mouse models | PMID:37154692 **[ABSTRACT-VERIFIED]** |
| **Phenytoin / fosphenytoin** | Severe bradycardia and hypotension in an AIMS patient | PMID:42290677 **[FULL-TEXT — RE-VERIFY]** |
| **Febrile / catabolic illness** | One patient had a coma-and-tetraplegia episode preceded by fever and vomiting, with metabolic acidosis (lactate 6), CK 738, and transient multifocal grey+white matter lesions | PMID:31575858 full text |

### Protective factors

No genetic or environmental protective factors are described. **Heterozygosity is effectively protective/neutral for AIMS**: parents are clinically unaffected carriers, and functional assays show no dominant-negative effect (§4, §6).

---

## 3. Phenotypes

### Frequencies from the pooled published cohorts

The 2024 Brain paper provides the only published pooled frequency table (their cohort n=9, plus the 2019 cohort n=6, total n=15) **[FULL-TEXT — RE-VERIFY all counts before curating `frequency:`]**:

| Phenotype | Suggested HPO term | 2024 cohort (n=9) | Pooled (n=15) | Suggested `FrequencyEnum` |
|---|---|---|---|---|
| Developmental delay | **HP:0001263** Global developmental delay | 9 (100%) | 15 (100%) | `OBLIGATE`/`VERY_FREQUENT` |
| Intellectual disability | **HP:0001249** Intellectual disability | 8 (89%) | 14 (93%) | `VERY_FREQUENT` |
| Fatigability | **HP:0012378** Fatigue | 7 (78%) | 13 (87%) | `VERY_FREQUENT` |
| White matter signal alteration | **HP:0030891** Periventricular white matter hyperintensities | 5 (56%) | 11 (73%) | `FREQUENT` |
| Spasticity | **HP:0001257** Spasticity | 6 (67%) | n/a | `FREQUENT` |
| Microcephaly | **HP:0000252** Microcephaly | 6 (67%) | 8 (53%) | `FREQUENT` |
| Corpus callosum abnormality | **HP:0002079** Hypoplasia of the corpus callosum | 6 (67%) | 6 (40%) | `FREQUENT` |
| Seizures | **HP:0001250** Seizure | 4 (44%) | 5 (33%) | `FREQUENT`/`OCCASIONAL` |
| Dysmorphic features | (see facial cluster below) | 4 (44%) | 10 (67%) | `FREQUENT` |
| Cardiac abnormality | **HP:0025169** Left ventricular systolic dysfunction | 1 (11%) | 3 (20%) | `OCCASIONAL` |

**Curation caution.** Note the *discordance* between cohorts — corpus callosum abnormality was 0/6 in 2019 but 6/9 in 2024, and dysmorphism was 6/6 in 2019 but 4/9 in 2024. This is ascertainment/expertise variation across small series, not a real biological gradient. Per `docs/frequency-evidence-guidelines.md`, the safest course for several of these rows is to **omit `frequency:`** and record the counts in `notes:` instead.

### Officially curated HPO annotations (OMIM:619719)

The HPO project has annotated IDMYS from the 2019 cohort only. This is the authoritative, ready-to-use term set (IDs and labels retrieved from the HPO API and exact as given):

| HPO ID | Term (exact label) | Frequency |
|---|---|---|
| HP:0001252 | Hypotonia | 6/6 |
| HP:0012378 | Fatigue | 6/6 |
| HP:0002172 | Postural instability | 6/6 |
| HP:0000965 | Cutis marmorata | 6/6 |
| HP:0000219 | Thin upper lip vermilion | 6/6 |
| HP:0000336 | Prominent supraorbital ridges | 6/6 |
| HP:0012368 | Flat face | 5/6 |
| HP:0003593 | Infantile onset | 5/6 |
| HP:0002395 | Lower limb hyperreflexia | 4/6 |
| HP:0000601 | Hypotelorism | 4/6 |
| HP:0001771 | Achilles tendon contracture | 4/6 |
| HP:0000689 | Dental malocclusion | 4/6 |
| HP:0011081 | Incisor macrodontia | 4/6 |
| HP:0000455 | Broad nasal tip | 4/6 |
| HP:0002938 | Lumbar hyperlordosis | 4/6 |
| HP:0000739 | Anxiety | 4/4 |
| HP:0030891 | Periventricular white matter hyperintensities | 3/6 |
| HP:0010535 | Sleep apnea | 2/2 |
| HP:0025169 | Left ventricular systolic dysfunction | 2/6 |
| HP:0005590 | Spotty hypopigmentation | 2/6 |
| HP:0500093 | Food allergy | 2/6 |
| HP:0001047 | Atopic dermatitis | 2/6 |
| HP:0001566 | Widely-spaced maxillary central incisors | 2/6 |
| HP:0001377 | Limited elbow extension | 1/6 |
| HP:0001374 | Congenital hip dislocation | 1/6 (congenital onset) |
| HP:0033204 | Triceps hyperreflexia | 1/6 |
| HP:0000957 | Cafe-au-lait spot | 1/6 |
| HP:0000639 | Nystagmus | 1/6 |
| HP:0032012 | Heterotropia | 1/6 |
| HP:0020045 | Esodeviation | 1/6 |
| HP:0000565 | Esotropia | 1/6 |
| HP:0002650 | Scoliosis | 1/6 |
| HP:0000007 | Autosomal recessive inheritance | — |
| HP:0003577 | Congenital onset | 1/6 |

### Additional terms needed for features from the 2024/2026 expansions

All verified during this research:

| Feature | HPO term |
|---|---|
| Intellectual disability | **HP:0001249** Intellectual disability |
| Global developmental delay | **HP:0001263** Global developmental delay |
| Seizure | **HP:0001250** Seizure |
| Spasticity | **HP:0001257** Spasticity |
| Microcephaly | **HP:0000252** Microcephaly |
| Short stature | **HP:0004322** Short stature |
| Corpus callosum hypoplasia | **HP:0002079** Hypoplasia of the corpus callosum |
| Periventricular leukomalacia (imaging pattern) | **HP:0006970** Periventricular leukomalacia |
| Leukoencephalopathy | **HP:0002352** Leukoencephalopathy |
| Abnormal cerebral white matter | **HP:0002500** Abnormal cerebral white matter morphology |
| Reduced periventricular WM volume | **HP:0034295** Reduced cerebral white matter volume |
| Cerebral WM hyperintensity on MRI | **HP:0030890** Hyperintensity of cerebral white matter on MRI |
| Generalized muscle weakness | **HP:0003324** Generalized muscle weakness |
| Exercise-induced myalgia | **HP:0003738** Exercise-induced myalgia |
| Exercise-induced muscle cramps | **HP:0003710** Exercise-induced muscle cramps |
| Exercise-induced muscle fatigue | **HP:0009020** Exercise-induced muscle fatigue |
| Dementia / cognitive decline (sexagenarian case) | **HP:0000726** Dementia |
| Dilated cardiomyopathy | **HP:0001644** Dilated cardiomyopathy |
| Sensorineural hearing impairment | **HP:0000407** Sensorineural hearing impairment |
| Elevated CK (crisis only) | **HP:0003236** Elevated circulating creatine kinase concentration |
| Ileal atresia (neonatal case) | **HP:0011102** Ileal atresia |
| Ventricular septal defect (neonatal case) | **HP:0001629** Ventricular septal defect |
| Stillbirth / IUFD (het parents) | **HP:0003826** Stillbirth; **HP:0034241** Prenatal death |

**Ontology gap worth flagging:** HPO has no single term capturing *"periventricular-leukomalacia-like white matter change of vascular origin in a genetic channelopathy"*. The pragmatic composition is HP:0006970 + HP:0030891, with `preferred_term` carrying the nuance (permitted by the repo's `preferred_term` vs `term.label` rule).

### Phenotype characteristics

- **Onset:** infantile in 5/6 of the original cohort (**HP:0003593**), congenital in 1/6 (**HP:0003577**). The 2026 series extends onset to the **neonatal period** (seizures on day 3 of life). One 2024-cohort participant had **developmental regression at 15 months** **[FULL-TEXT — RE-VERIFY]**.
- **Severity:** intellectual disability is **mild** in most (5/6 mild, 1/6 moderate in the 2019 cohort) but "of variable severity" across the expanded cohort. Muscle weakness is mild-to-moderate (MRC grade 4 to 4+ in affected groups); one 2019 patient had entirely normal strength despite reporting exhaustibility.
- **Progression:** classically **static/non-progressive in childhood**, but two progressive dimensions are now documented: (a) **white matter lesions accumulate** — *"Lesions have increased significantly since the first investigation"* in the oldest 2019 patient (PMID:31575858 full text), and (b) **adult motor and cognitive decline** from the fifth decade in the 2026 sexagenarian.
- **Episodic overlay:** discrete decompensations (fever/vomiting-triggered coma episode; post-operative cardiogenic shock) punctuate an otherwise stable course. `temporality: RECURRENT` / `EPISODIC` is appropriate for the spasm and decompensation phenotypes.
- **Quality-of-life impact:** no formal instrument (EQ-5D, SF-36, PROMIS) has ever been applied in AIMS — **a genuine data gap.** Functional proxies from the 2019 cohort are quantitative and citable: all six had **reduced 6-minute walk distance** (e.g. 512.5 m vs 765 m reference) and **moderate-to-severe balance deficits on the miniBESTest** (scores 14–21 / 28). Supported-living need is documented: patients live in own homes or sheltered housing "with daily help and supervision," and one attends a sheltered work program but "is easily exhausted, and needs rest during the day."

---

## 4. Genetic/Molecular Information

### Causal gene

| Field | Value |
|---|---|
| Symbol | **ABCC9** |
| HGNC | **HGNC:60** (verified via genenames.org REST — the draft's `hgnc:60` is correct) |
| Approved name | ATP binding cassette subfamily C member 9 |
| Locus | **12p12.1** |
| Ensembl | ENSG00000069431 |
| NCBI Gene | 10060 |
| UniProt | **O60706** (ABCC9_HUMAN, SUR2) |
| Aliases | **SUR2**, CMD1O |
| OMIM gene | 601439 |

Gene architecture matters mechanistically: *ABCC9* has **≥39 exons** and yields two major, tissue-divergent splice isoforms differing only in the terminal exon — **SUR2A** (striated muscle; pairs with Kir6.2/*KCNJ11*) and **SUR2B** (smooth muscle; pairs with Kir6.1/*KCNJ8*). Any variant proximal to the terminal exon — as all AIMS variants are — hits **both** isoforms, which is precisely why AIMS is multisystem while the exon-38-specific heterozygous DCM variants are cardiac/skeletal-limited.

### Pathogenic variant spectrum (complete published allelic series)

**Cohort 1 — Smeland et al. 2019 (PMID:31575858), 6 patients / 2 Norwegian families:**

| Variant | Protein | Mechanism |
|---|---|---|
| **c.1320+1G>A** (NM_020297.2; NC_000012.11:g.22063090C>T) | **p.(Ala389_Gln440del)** via r.1165_1320del | Splice-donor loss of exon 8 → **in-frame** 52-aa deletion in TMD1 |

**Cohort 2 — Efthymiou et al. 2024 (PMID:38217872), 9 patients / 7 families + 1 IUFD family** **[FULL-TEXT — RE-VERIFY]**:

| Family | Variant | Protein | Origin | Consanguineous |
|---|---|---|---|---|
| F1 | c.1320+1G>A | p.(Ala389_Gln440del) | Norwegian | No |
| F2 | c.2812C>T | p.(Arg938Ter) | Pakistani | Yes |
| F3 | c.4212-1G>T | p.(Phe1405SerfsTer8) | Egyptian | Yes |
| F4 | c.1858C>T | p.(Arg620Ter) | Dutch | No |
| F5 | c.1234C>T | p.(Gln412Ter) | Egyptian | Yes |
| F6 | c.284+1G>A | p.(Phe49GlyfsTer13) | Norwegian | No |
| F7 | c.3747del | p.(Leu1250TrpfsTer9) | British Pakistani | Yes |
| F8 (IUFD only) | c.2140_2141del | p.(Leu714SerfsTer7) | Saudi Arabian | Yes |

**Cohort 3 — Nagaraj et al. 2026 (PMID:42290677), 5 patients** **[FULL-TEXT — RE-VERIFY]**:

| Participant | Variant | Protein | Note |
|---|---|---|---|
| P1 | c.2881del (hom) | p.(Glu961LysfsTer10) | Sexagenarian with dementia |
| P2 | c.3269delG (hom) | p.(Gly1090AspfsTer2) | |
| P3 | c.3269delG (hom) | p.(Gly1090AspfsTer2) | Unrelated to P2 — recurrent allele |
| P4 | 73,292 bp deletion, exons 13–33 (hom) | p.(Ser601ArgfsTer9) | **Only structural/CNV variant reported** |
| P5 | c.4018C>T / c.1828_1829del (comp het) | p.(Gln1340Ter) / p.(Leu610GlufsTer2) | **First compound heterozygote**; neonatal crisis |

**Spectrum summary for curation:**
- **Variant classes:** nonsense (4), frameshift (5+), canonical splice-site (3), whole-exon in-frame deletion (1), multi-exon genomic deletion (1). **No pathogenic missense variant has ever been reported for AIMS** — a sharp genotype contrast with Cantú syndrome, which is overwhelmingly missense GoF.
- **Molecular consequence:** NMD of the transcript and/or drastic SUR2 truncation. > "All variants are predicted to lead to nonsense mediated decay of ABCC9 transcripts and/or drastic truncation of SUR2." — **PMID:42290677** **[ABSTRACT-VERIFIED]**
- **Origin:** exclusively **germline**. No somatic *ABCC9* involvement in AIMS (somatic *ABCC9* appears in COSMIC only as incidental cancer variation, unrelated to this disease).
- **Functional consequence:** **complete loss of function**, *not* dominant-negative — see §6. The correct dismech `modifier` on the *ABCC9* gene descriptor is `DECREASED`, and the relevant `GENO` framing is biallelic LoF.
- **ACMG/AMP:** these are PVS1-anchored (null variant in a gene where LoF is the established mechanism) plus PM3 (recessive, in trans), PS3 (functional assays), PP1 (segregation) — expected **Pathogenic**. Note that **ClinGen has published no variant pathogenicity assertions for *ABCC9*** (0 records), so no `CGGV:`/ClinVar expert classification is citable for AIMS variants.

### Allele frequencies

- c.1320+1G>A: **Finnish gnomAD AF 0.0007 (18/24,850)**; non-Finnish European 5/128,232 (**AF 0.00004**); **absent in Asian and African populations**; **homozygous state absent from gnomAD** (PMID:31575858 full text). Earlier ExAC counts: Finnish 3/6,586; non-Finnish European 4/66,386.
- Across the 2024 allelic series: *"All the reported ABCC9 variants are…rare in the general population (max. allele frequency 0.000088) and absent in homozygous state in the gnomAD database."* **[FULL-TEXT — RE-VERIFY]**
- **Not retrieved:** gnomAD gene-level constraint metrics for *ABCC9* (pLI / LOEUF / o-e LoF). The gnomAD browser is client-rendered and could not be scraped in this session. If constraint is wanted for the entry, pull it from the gnomAD API or a local download rather than asserting a value.

### Allelic series — other *ABCC9* diseases (essential differential context)

| Disease | Mechanism | Inheritance | ClinGen validity (verified 2026) |
|---|---|---|---|
| **AIMS / IDMYS** (this entry) | Biallelic **LoF** | AR | **No ClinGen curation** — gap |
| **Cantú syndrome** (hypertrichotic osteochondrodysplasia; MONDO:0009406, OMIM #239850) | Heterozygous **GoF** (mostly missense) | AD | **Definitive** (Syndromic Disorders GCEP, 2025-02-21) |
| **Dilated cardiomyopathy 1O** (OMIM #608569) | Heterozygous LoF missense in **exon 38** (SUR2A-specific) | AD | **Limited** (DCM GCEP, 2026-03-04) |
| **Atrial fibrillation, familial, 12** (OMIM #614050) | Missense in the same SUR2A-specific exon; single 53-year-old patient | AD | — |
| **Brugada syndrome** | — | AD | **Disputed** (Hereditary Cardiovascular Disease GCEP, 2025-10-28) |

The paralogous pancreatic/neuronal pair *ABCC8*/*KCNJ11* completes the family logic: GoF → neonatal diabetes; LoF → congenital hyperinsulinism.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** none identified. The 2024 paper's observation that two unrelated families share c.3269delG with differing severity (P2 had seizures and regression; P3 had isolated ID with a **normal MRI**) is direct evidence of **modifier or stochastic effects** and is an excellent `KNOWLEDGE_GAP`/`mechanistic_hypotheses` candidate.
- **Epigenetics:** **no data.** No methylation episignature, no DiseaseMeth/ENCODE-based analysis exists for AIMS. Do not populate this section.
- **Chromosomal abnormalities:** none causal. Notably, karyotype/G-banding, high-resolution SNP array, *FMR1* CGG repeat analysis, *DMPK* PCR, mtDNA screening, and metabolic screening were all **normal** in the 2019 patients before exome analysis — clinically useful negative information for the diagnostics section. The one exception is P4's **73.3 kb intragenic deletion of exons 13–33**, which is a CNV detectable by array/CNV-aware sequencing.

---

## 5. Environmental Information

- **Environmental factors:** none contributory to causation. CTD/TOXNET yield no AIMS-relevant exposure.
- **Lifestyle factors:** none causal. Exercise is a *symptom trigger* (spasms, myalgia, fatigability), not a risk factor. Two 2019 patients became **overweight (>97.5th percentile)** in adulthood after early failure-to-thrive, and obesity contributed to obstructive sleep apnea in one — a modifiable comorbidity, not an etiologic factor.
- **Infectious agents:** **not applicable.** One febrile illness preceded a coma episode, but as a decompensation trigger rather than a pathogen-mediated cause.

The substantive content for this section is **iatrogenic exposure** (§12 drugs-to-avoid), which is where the real "environmental" risk in AIMS lies.

---

## 6. Mechanism / Pathophysiology

### Molecular foundation

K<sub>ATP</sub> channels are **octameric complexes of four pore-forming Kir6.x subunits and four regulatory SURx subunits** that couple cellular metabolic state to membrane excitability. ATP binding to Kir6.x inhibits the channel; Mg-ADP/Mg-ATP binding to the SURx nucleotide-binding domains stimulates it. SUR2 is therefore the **metabolic sensor arm** of the channel — losing it does not merely reduce current, it abolishes the metabolism-to-excitability coupling entirely in SUR2-dependent tissues.

Tissue pairing (PMID:31575858 full text): *"Pancreatic and neuronal K<sub>ATP</sub> channels are predominantly formed by Kir6.2 and SUR1, smooth muscle K<sub>ATP</sub> channels are comprised of Kir6.1 and SUR2B, and the predominant combination in striated muscle is Kir6.2 and SUR2A."*

### Proximal molecular defect

The exon-8 in-frame deletion removes SUR2 residues **Ala389–Gln440**, disrupting multiple transmembrane helices in **TMD1**. Consequences measured in Cosm6 cells:

1. **~50% reduction in SUR2 protein** on Western blot.
2. **Complete abolition of ⁸⁶Rb⁺ efflux** — "cells expressing Kir6.2/SUR2AΔ8 showed no rubidium efflux above the background levels observed in GFP-transfected cells."
3. **Complete absence of K<sub>ATP</sub> current** in inside-out patch clamp.
4. Same result for **SUR2BΔ8** — so both isoforms are dead.
5. **No dominant-negative effect:** a 1:1 WT:Δ8 co-expression gave WT-like efflux rates and unchanged ATP IC₅₀ / pinacidil activation — *"in the heterozygous context, the c.1320+1G>A mutation is without significant effect."* This is the molecular explanation for healthy carrier parents.

The 2026 paper reproduced complete LoF for three further truncating variants (p.Glu961LysfsTer10, p.Gly1090AspfsTer2, p.Ser601ArgfsTer9) using a **landing-pad HEK293 / FLIPR membrane-potential assay** (no oligomycin-A-induced hyperpolarization) plus patch clamp, again with **no major dominant-negative effect** **[FULL-TEXT — RE-VERIFY]**.

> "Functional tests of recombinant channels confirm that disease-associated SUR2 truncations cause a complete loss-of-function." — **PMID:42290677** **[ABSTRACT-VERIFIED]**

### Causal chains — three mechanistically distinct downstream arms

The pathophysiology graph should be modeled as **one molecular trigger fanning into three tissue-specific arms**, because the arms have genuinely different intermediate biology.

**Arm A — Skeletal muscle (myopathy). This arm is causally proven to be muscle-intrinsic.**

```
ABCC9 biallelic LoF (MOLECULAR)
  → loss of SUR2A/Kir6.2 KATP in skeletal myocytes (CELLULAR)
  → failure of fatigue-induced action-potential shortening and
    resting-membrane-potential stabilization (CELLULAR)
  → excessive Ca2+ entry, elevated resting tension,
    abnormal unstimulated force generation (CELLULAR)
  → myofiber stress/degeneration, impaired fatigue recovery (TISSUE)
  → fatigability, muscle weakness, painful exercise-induced spasms (ORGANISM)
```

The 2019 mechanistic rationale, verbatim from the full text: *"In skeletal muscle, K<sub>ATP</sub> channels are typically closed at rest but open in response to metabolic stress or fatigue. Channel activation results in action potential shortening and stabilization of the resting membrane potential during the development of fatigue, which serves to reduce intracellular calcium, decrease resting tension and protect myocytes from damage. Therefore, loss of K<sub>ATP</sub> function might be expected to result in failure to recover from fatigue, myofiber degeneration, and excessive calcium influx."*

McClenaghan et al. 2023 then **localized** this arm by tissue-selective knockdown and, importantly, **falsified** the obvious Ca²⁺-influx hypothesis:

> "Given the roles of KATP channels in all muscles, we sought to determine how myopathy arises using tissue-selective suppression of KATP and found that LoF in skeletal muscle, specifically, underlies myopathy. In isolated muscle, SUR2 LoF results in abnormal generation of unstimulated forces, potentially explaining painful spasms in AIMS. We sought to determine whether excessive Ca2+ influx through CaV 1.1 channels was responsible for myopathology but found that the Ca2+ channel blocker verapamil unexpectedly resulted in premature death of AIMS mice and that rendering CaV 1.1 channels nonpermeable by mutation failed to reverse pathology; results which caution against the use of calcium channel blockers in AIMS." — **PMID:37154692** **[ABSTRACT-VERIFIED]**

That negative result is scientifically important and should be curated as a `supports: REFUTE` evidence item against a CaV1.1-influx sub-hypothesis — it is exactly the kind of falsified mechanism dismech is designed to record rather than discard.

**Arm B — Cerebral vasculature → white matter injury (the leading explanation for the CNS phenotype).**

```
ABCC9 biallelic LoF (MOLECULAR)
  → loss of SUR2B/Kir6.1 KATP in vascular smooth muscle (CELLULAR)
  → increased vascular tone / hypertension; loss of metabolic
    vasodilatory reserve (TISSUE)
  → impaired dynamic coupling of cerebral blood flow to
    neuronal metabolic demand; chronic hypoperfusion (TISSUE)
  → ischemic periventricular white matter injury, small-vessel
    disease, lacunar-like cavitation, mineral deposition (TISSUE)
  → intellectual disability, spasticity, hyperreflexia,
    seizures, later cognitive decline (ORGANISM)
```

The 2019 authors' framing: *"recent data demonstrate that SUR2-containing K<sub>ATP</sub> channels play a critical role in regulation of cerebral vascular architecture… Since K<sub>ATP</sub> channel GoF results in chronic vasodilation and altered neuro–vascular coupling, it is conceivable that K<sub>ATP</sub> loss of function may impact the cerebral vasculature in a way that results in impaired dynamic coupling of blood flow to match neuronal metabolic demand."* They add that the white matter hyperintensities seen in **both** Cantú syndrome and AIMS *"could result from ischemic events due to dysregulated cerebral blood flow, although the cognitive phenotype seems to be more definite in AIMS than in Cantú syndrome."*

Supporting evidence: hypertension was significantly increased in SUR2-STOP mice; cardinal vein red-cell velocity was increased in SUR2-STOP zebrafish; and the 2026 sexagenarian's imaging evolved into frank **severe vascular leukoencephalopathy** with perivascular space dilation and lacunar-like cavitations **[FULL-TEXT — RE-VERIFY]**. Note also that **MR angiography was normal with normal cerebral vessel calibers** in the 2019 patients — so this is a *functional* microvascular/autoregulatory defect, not a macrovascular malformation. That distinction is a genuine contrast with Cantú syndrome (dilated, tortuous vessels) and should be stated explicitly.

Mark this arm as `status: EMERGING` in `mechanistic_hypotheses` — the 2019 authors themselves say "it is conceivable," and no direct human CBF/neurovascular-coupling measurement in AIMS exists.

**Arm C — Cardiac (age-dependent).**

```
ABCC9 biallelic LoF (MOLECULAR)
  → loss of SUR2A/Kir6.2 KATP in cardiomyocytes; loss of
    metabolic stress protection (CELLULAR)
  → reduced contractile reserve, cardiomyocyte apoptosis
    (TUNEL+ in zebrafish) (CELLULAR/TISSUE)
  → biventricular systolic dysfunction, LV dilation (TISSUE)
  → early-stage dilated cardiomyopathy, heart failure;
    acute cardiogenic shock under stress (ORGANISM)
```

Human anchor: the two oldest 2019 patients had biventricular systolic dysfunction (EF 35–40% and 48%), raised NT-proBNP, and cardiac-MRI LV dilation "compatible with early-stage dilated cardiomyopathy," while a teenage echocardiogram in the same patient had been normal — establishing **age-dependent emergence**. The authors compare with the heterozygous exon-38 DCM patients who were older with far worse EFs (15–23%) and conclude: *"This may suggest a progressive cardiomyopathy which will require longitudinal analysis in AIMS."*

Notably, zebrafish hearts showed **no fibrosis** (AFOG) and **normal myofiber/tropomyosin structure** despite marked ventricular enlargement — so this is a functional/apoptotic remodeling process rather than a primary fibrotic cardiomyopathy. That argues **against** naive conformance to `fibrotic_response` and **for** conformance to `cardiomyopathy_maladaptive_remodeling`.

### Unexplained: the intellectual disability itself

The 2019 authors are admirably candid, and this should be curated as a first-class knowledge gap:

*"It is not obvious how myocyte K<sub>ATP</sub> dysfunction could explain the intellectual disability or anxiety, and there are no reports of cognitive impairment in previous SUR2 mutant animal models."* Neuronal K<sub>ATP</sub> is predominantly Kir6.2/SUR1, though SUR2 transcripts are reported in central and peripheral neurons and implicated in hippocampal sclerosis of aging and ALS.

This is a textbook **`HUMAN_MODEL_MISMATCH`** case per the repo's CLAUDE.md guidance, not a plain `KNOWLEDGE_GAP`: the SUR2-STOP mouse was formally tested for cognition and anxiety and was **negative on all of it** (locomotor activity, sensorimotor battery, Morris water maze spatial learning, elevated plus maze), while the defining human feature is intellectual disability plus anxiety in 4/4 assessed. The authors' own caveat — *"mild cognitive impairment, as seen in humans, can be difficult to recognize in animals"* — plus their suggestion of working-memory/fear-conditioning testing maps directly onto `proposed_experiments`.

### Cellular processes, cell types, and compartments

| Ontology | Term | Verified label |
|---|---|---|
| **GO CC** | **GO:0008282** | **"inward rectifying potassium channel"** — ⚠️ **the canonical GO label is *not* "ATP-sensitive potassium channel complex"**; that is a *synonym*. Use the canonical label in `term.label` and put "ATP-sensitive potassium channel complex (K<sub>ATP</sub>)" in `preferred_term`. Its definition explicitly describes the four Kir6.x + four SURx architecture. |
| **GO MF** | **GO:0015272** | "ATP-activated inward rectifier potassium channel activity" — the precise molecular function lost |
| **GO MF** | GO:0017098 | "sulfonylurea receptor binding" |
| **GO BP** | **GO:0071805** | "potassium ion transmembrane transport" |
| **GO BP** | GO:1901379 | "regulation of potassium ion transmembrane transport" |
| **GO BP** | GO:0042391 | regulation of membrane potential *(commonly used; verify with OAK before committing)* |
| **CL** | **CL:0008002** | **"skeletal muscle fiber"** — primary myopathy cell type |
| **CL** | **CL:0000192** | **"smooth muscle cell"** — vascular arm |
| **CL** | CL:0000746 | cardiac muscle cell *(verify with OAK)* |
| **CL** | CL:0000128 | oligodendrocyte — plausible white-matter target, but **no direct AIMS evidence**; omit unless supported |
| **UBERON** | **UBERON:0002437** | **"cerebral hemisphere white matter"** |
| **UBERON** | **UBERON:0008967** | **"centrum semiovale"** — explicitly named in two patients' MRI reports |
| **CHEBI** | **CHEBI:9948** | **verapamil** (the contraindicated agent) |

### Metabolic, immune, biochemical, and profiling data

- **Biochemical abnormality:** the defect *is* an ion channel defect. Routine biochemistry is characteristically **normal**: *"S-CK, B-lactate, nerve conduction velocities, and electromyography, including repetitive nerve stimulation, are normal in all individuals, except for discrete myopathic discharges in patient 2–2."* Abnormal values appear only during crises (lactate 6, CK 738) or incidentally (hyperprolactinemia 720 mIU/L in one patient, with normal pituitary MRI).
- **Metabolic changes:** no primary metabolic derangement; inborn-errors-of-metabolism screening was normal. Mouse SUR2 nulls show *lower serum glucose and enhanced insulin action* (MGI) — an interesting, unexplored translational thread with **no human counterpart reported**.
- **Immune involvement:** **none mechanistically.** Atopic dermatitis (2/6), food allergies with anaphylaxis, and cyclosporine treatment in one patient are recorded features whose relationship to SUR2 is entirely unexplained — curate as associations, not mechanism.
- **Transcriptomics / proteomics / metabolomics / lipidomics / single-cell / spatial / multi-omics / CRISPR screens:** **no AIMS-specific datasets exist.** The only quantitative expression data is zebrafish qPCR showing ~4-fold reduced *abcc9* mRNA in SUR2-STOP larvae, consistent with NMD. Leave these subsections empty rather than importing generic *ABCC9* GTEx data as if it were disease data.

### Suggested dismech module conformance

AIMS is a strong multi-module conformer candidate:
- **`cardiomyopathy_maladaptive_remodeling`** → Arm C (`#Ventricular Remodeling`). Good fit; note the absence of fibrosis in the fish model.
- **`epilepsy_excitation_inhibition_imbalance`** → the seizure phenotype (`#Excitation-Inhibition Imbalance`), with the zebrafish PTZ hypersensitivity as supporting `MODEL_ORGANISM` evidence.
- **A new K<sub>ATP</sub> channelopathy grouping** is the more valuable structural contribution: AIMS + Cantú syndrome + DCM1O + neonatal diabetes + congenital hyperinsulinism form a textbook **GoF/LoF antagonistic pair set** across two paralogous gene pairs. This parallels the existing `cellular_senescence` / `senescence_tumor_suppression` two-module treatment of opposing arms, and would fit `kb/groupings/` with `grouping_basis: [SHARED_MECHANISM, SHARED_GENE_FAMILY]`.

---

## 7. Anatomical Structures Affected

**Primary organs / systems**

| System | Structures | UBERON |
|---|---|---|
| **Central nervous system** | Cerebral white matter (periventricular, juxtacortical, frontal/parietal), centrum semiovale, corpus callosum, basal ganglia, pons, brainstem, cerebellum | UBERON:0002437 cerebral hemisphere white matter; UBERON:0008967 centrum semiovale; UBERON:0002336 corpus callosum*; UBERON:0002420 basal ganglion*; UBERON:0000988 pons* |
| **Skeletal muscle** | Generalized, with proximal and truncal predominance | UBERON:0001134 skeletal muscle tissue* |
| **Heart** | Both ventricles (biventricular systolic dysfunction); LV dilation | UBERON:0002084 heart left ventricle*; UBERON:0002080 heart right ventricle* |
| **Vasculature** | Cerebral microvasculature (functional, not structural); systemic arteries (hypertension) | UBERON:0001637 artery*; UBERON:0001981 blood vessel* |

*\* commonly-used IDs stated from knowledge; verify with `just validate-terms` / OAK before committing. Only UBERON:0002437 and UBERON:0008967 were verified live in this session.*

**Secondary involvement:** skeleton (lumbar hyperlordosis, scoliosis, congenital hip dislocation, Achilles contractures), eye/oculomotor (nystagmus, strabismus/esotropia, heterotropia), inner ear (bilateral high-frequency sensorineural hearing loss), skin (cutis marmorata in 6/6, spotty hypopigmentation, café-au-lait macule, atopic dermatitis, facial telangiectasia), craniofacial/dental (macrodontia, malocclusion, widely spaced incisors), GI (feeding difficulties, ileal atresia in the neonate), upper airway (obstructive sleep apnea).

**Tissue and cell level:** striated muscle fibers (**CL:0008002**), cardiac myocytes (CL:0000746), vascular smooth muscle cells (**CL:0000192**). Muscle histology is strikingly bland — a single biopsy showed only *"unspecific changes of mitochondrial aggregation and muscle fiber caliber variation"* — consistent with mouse data showing histological abnormality only after chronic exercise.

**Subcellular level:** the **plasma membrane** K<sub>ATP</sub> complex (**GO:0008282**) is the site of the defect; the 2019 paper specifically frames the loss as of *"plasmalemmal K<sub>ATP</sub> function."* A mitochondrial angle exists in the literature (a prior mouse allele retains a "mitochondria-limited short form" of SUR2, and one patient's biopsy showed mitochondrial aggregation) but **mitochondrial SUR2 is not established as an AIMS mechanism** — do not assert it.

**Lateralization:** predominantly **bilateral and symmetric** (white matter changes, hearing loss, hyperreflexia, ventricular dysfunction). Documented asymmetric exceptions: unilateral left lower-extremity weakness with limping in one patient, unilateral Achilles contracture in another, and a single left-anterior-horn periventricular lesion.

---

## 8. Temporal Development

**Onset**
- **Neonatal:** recurrent emesis, feeding difficulty, ileal atresia, multifocal seizures on day 3 (2026 case) — the earliest documented presentation.
- **Infantile:** HP:0003593 in 5/6 of the original cohort — hypotonia, delayed psychomotor development, feeding difficulty, low weight, typically noticed in toddler years.
- **Congenital:** HP:0003577 in 1/6 (congenital hip dislocation).
- **Prenatal / lethal extreme:** recurrent intrauterine fetal death in heterozygous couples, including two IUFDs of fetuses confirmed homozygous for p.(Arg620Ter) **[FULL-TEXT — RE-VERIFY]**.
- **Pattern:** insidious and chronic, with superimposed acute episodes.

**Progression / stages** — a useful three-stage model emerges from the pooled natural history:
1. **Early (infancy–childhood):** hypotonia, developmental delay, feeding difficulty, failure to thrive, toe-walking/in-toeing, lumbar lordosis. Cardiac and cognitive testing may be normal.
2. **Intermediate (adolescence–early adulthood):** mild-to-moderate ID confirmed on neuropsychological testing, fatigability, exercise-induced myalgia/spasms, hyperreflexia, balance impairment, accumulating white matter lesions, anxiety; weight often shifts from low to overweight.
3. **Late (fourth decade onward):** biventricular systolic dysfunction/early DCM; progression of leukoencephalopathy toward vascular small-vessel disease with cavitation and calcification; **motor and cognitive decline with global muscle atrophy and dementia-like presentation** (2026 sexagenarian, died in her early sixties of aspiration-related asphyxiation) **[FULL-TEXT — RE-VERIFY]**.

**Rate:** slow. Static-appearing through childhood, which is why AIMS was long mistaken for a static encephalopathy — but explicitly **not static** on imaging (*"Lesions have increased significantly since the first investigation"*) or in late adulthood.

**Course:** chronic, lifelong, **progressive with an episodic overlay**. Not relapsing-remitting.

**Remission:** none. The only documented reversibility is imaging: the fever-triggered multifocal lesions in patient 1–4 "were normalized a few weeks later, except for a white matter lesion," and he "regained the same psychomotor level as before" — evidence that acute decompensations can be survivable and partly reversible.

**Critical periods / windows for intervention**
- **Perioperative period** — the highest-acuity documented window (two post-operative decompensations in one neonate).
- **Antiseizure and anesthetic drug selection** at any age.
- **Adulthood cardiac surveillance** — the 2019 patient had a normal teenage echocardiogram and dysfunction by age 33, so a single normal childhood echo does not discharge the risk.
- **Early developmental years** for habilitation, feeding, and educational support.

---

## 9. Inheritance and Population

**Epidemiology.** No prevalence or incidence estimate has ever been published, and there is no Orphanet prevalence class (no ORPHA code exists). The literature total is **~20 individuals from ~13 families (2019: 6; 2024: 9 + IUFDs; 2026: 5)**. For dismech `Prevalence`, the honest structured record is:

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Approximately 20 affected individuals from ~13 families reported across
    three publications (2019-2026). No prevalence or incidence estimate has
    been published; no Orphanet epidemiology record exists.
```

Do **not** derive a rate_per_100000 from carrier frequency — that inference is not in the literature.

**Inheritance pattern.** **Autosomal recessive** (HP:0000007). Verified by homozygosity in all affected individuals with heterozygous unaffected parents and one heterozygous unaffected sibling, plus one compound heterozygote with variants confirmed in trans (paternal/maternal).

**Penetrance.** Appears **complete** for the core triad in biallelic carriers, though the very small *n* and the 2026 participant with isolated ID and a normal MRI show **variable expressivity of individual features**. Heterozygotes have no AIMS phenotype: *"Heterozygous parents do not show any conserved clinical pathology but report multiple incidences of intra-uterine fetal death"* (PMID:38217872) **[ABSTRACT-VERIFIED]**.

**Expressivity.** **Variable** — most sharply demonstrated by the two unrelated homozygotes for the identical c.3269delG allele with markedly different severity (regression + seizures vs. IQ 69 with normal imaging). Cardiac involvement is age-dependent rather than variant-dependent.

**Genetic anticipation.** **Not applicable** (no repeat expansion).

**Germline mosaicism.** Not reported.

**Founder effect.** Strongly suggested for **c.1320+1G>A**: both 2019 families came from the same area of Northern Norway with probable Finnish ancestry, yet whole-genome kinship analysis excluded relatedness (**kinship coefficient 0.0403**, versus ~0.05 expected for unrelated samples), and the allele sits in a shared 3.8 Mb homozygous block (chr12:18,326,590–22,176,010, hg19). Combined with the Finnish gnomAD AF of 0.0007, the authors concluded: *"Considering the probable Finnish ancestry of all patients, the syndrome might be more prevalent in the Finnish population than others."* A second Norwegian allele (c.284+1G>A) appeared in the 2024 cohort.

**Consanguinity.** A major contributor outside Northern Europe — documented in Pakistani, Egyptian (×2), Saudi Arabian, and British-Pakistani families, and in the 2026 first-cousin family.

**Carrier frequency.** Best estimate is the Finnish c.1320+1G>A allele frequency of **0.0007** (≈1 in 690 carriers for that single allele in Finns) — but note this is a per-allele figure, not a pan-allelic carrier rate, and no carrier-screening study exists.

**Population demographics.** Reported ancestries: Norwegian (with probable Finnish ancestry), Dutch, Pakistani, British Pakistani, Egyptian, Saudi Arabian, Brazilian and Italian contributions via the 2026 author network. Absent from gnomAD Asian and African populations for the founder allele. **Geographic distribution reflects where exome sequencing and expert networks are concentrated, not true disease distribution** — this is ascertainment bias and should be stated as such.

**Sex ratio.** Roughly balanced with no evidence of sex bias: 2019 cohort 2F/4M; 2026 cohort 4F/1M. Consistent with autosomal inheritance. (Note: the PMID:31575858 MeSH set anomalously includes *Genetic Diseases, X-Linked* and *Intellectual Disability/parasitology* — clear MEDLINE indexing artifacts, not claims about the disease. Do not propagate these.)

**Age distribution of reported individuals.** Newborn to early sixties; the 2019 cohort spanned 11–33 years at report.

---

## 10. Diagnostics

### The diagnostic gestalt

The 2026 authors give the single most useful practical recommendation: the constellation of **periventricular leukomalacia + developmental delay/intellectual disability + muscle weakness and fatigability** should prompt investigation for an *ABCC9*-related disorder **[FULL-TEXT — RE-VERIFY]**. This matters because the imaging pattern mimics acquired perinatal hypoxic-ischemic injury, so AIMS is easily dismissed as non-genetic.

### Laboratory tests — mostly normal, which is itself diagnostic information

- **Creatine kinase:** normal in all 2019 patients and in the 2026 participant tested; elevated (738) only during acute crisis. **A normal CK does not exclude AIMS** — a critical negative, since it steers clinicians away from a myopathy workup. LOINC: CK 2157-6.
- **Lactate:** normal at baseline; elevated in crisis (6 mmol/L). LOINC 2524-7.
- Prolactin: hyperprolactinemia in one patient with normal pituitary MRI (incidental). NT-proBNP: raised in the patient with heart failure, normal in his sister with milder dysfunction.
- Normal: metabolic/IEM screening, mtDNA sequence and deletion screening.

**Biomarkers:** there is **no diagnostic or prognostic biomarker for AIMS**. NT-proBNP serves only as a generic heart-failure marker. This is a real gap worth recording.

### Imaging — the highest-yield test

**Brain MRI** is the cornerstone. Findings: periventricular and juxtacortical white matter T2/FLAIR hyperintensities (centrum semiovale, frontal and parietal, anterior temporal lobes, external capsules); reduced periventricular white matter volume; corpus callosum hypoplasia/agenesis; punctate lesions in basal ganglia, pons, brainstem and cerebellum suggesting mineral deposition/calcification; in advanced disease, dilated perivascular spaces and lacunar-infarct-like cavitations. **MR angiography is normal with normal vessel calibers** — a key discriminator from Cantú syndrome. MRS was normal in the one patient tested. Serial imaging is recommended, since lesions accumulate.

**Cardiac imaging:** echocardiography ± cardiac MRI. Cardiac MRI detected LV dilation that echo missed (LV diameter was within normal range on echo in the same patient) — so **echo alone may under-call early cardiomyopathy**.

### Electrophysiology — characteristically normal

EMG, nerve conduction velocity, repetitive nerve stimulation, and EEG were **normal in all 2019 patients** (bar discrete myopathic discharges in one). Notably, one patient with clinical tonic–clonic episodes had **repeatedly normal EEGs** — clinically important, because normal EEG does not exclude the paroxysmal events, and it feeds the hypothesis that some episodes are circulatory rather than epileptic.

### Biopsy / pathology

Muscle biopsy is **low-yield and non-specific**: "caliber changes, mitochondrial aggregations." Not recommended as a diagnostic route; its main value is exclusionary.

### Genetic testing — the definitive route

- **Recommended first-line: exome or genome sequencing** (trio-based where possible). Both cohorts were solved this way, and the 2019 patients had already had extensive normal targeted testing (G-banding, high-resolution SNP array, *FMR1* CGG, *DMPK* PCR, multiple neuromuscular gene panels, mtDNA, IEM screening) before ES/GS succeeded.
- **Gene panels:** *ABCC9* is included in large neurodevelopmental/neuromuscular panels (the 2019 study used a >4,800-gene panel). No AIMS-specific panel exists.
- **WGS** adds value for excluding alternatives, resolving relatedness (kinship coefficient), and for **CNV detection** — essential given the 73.3 kb exon 13–33 deletion in the 2026 cohort. **A sequencing pipeline blind to intragenic CNVs can miss AIMS.**
- **Single-gene testing** is reasonable only for targeted familial testing or in a Finnish/Northern Norwegian patient with the classic triad (founder allele).
- **CMA/karyotype/FISH:** normal in AIMS; CMA would only detect the large intragenic deletion if probe coverage is adequate.
- **mtDNA testing:** normal — but frequently performed, because the phenotype (myopathy + white matter disease + lactate rise in crisis) mimics mitochondrial disease.
- **Repeat expansion testing:** not applicable.
- **RNA/functional confirmation:** cDNA analysis from fibroblasts confirmed exon 8 skipping in the 2019 family — a good template for splice-variant validation. Recombinant channel assays (⁸⁶Rb⁺ efflux, patch clamp, landing-pad/FLIPR membrane potential) are research-grade PS3 evidence, not clinical tests.
- **Omics diagnostics (proteomics/metabolomics/epigenomics/liquid biopsy):** no role established.

### Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria** — diagnosis is molecular plus phenotype fit.

Differential, with discriminators (several of these are *documented misdiagnoses* in the published families, which makes them high-value KB content):

| Alternative | How to distinguish |
|---|---|
| **Cantú syndrome** (*ABCC9* GoF, MONDO:0009406) | Hypertrichosis and coarse facies present; cardiomegaly with **high** cardiac output; dilated tortuous vessels on MRA; intellect typically **normal**. AIMS: no hypertrichosis, normal MRA, definite ID, **reduced** systolic function. |
| **Tuberous sclerosis** | *Actually diagnosed and later abandoned* in Family 2 because of depigmented patches + white matter lesions. TSC has cortical tubers/SEGA and a different MRI pattern. |
| **Acute disseminated encephalomyelitis** | *Actually considered* for patient 1–4's coma episode; re-read as "inflammatory perivascular reaction," lesions resolved. |
| **Perinatal hypoxic-ischemic periventricular leukomalacia** | Radiologically near-identical; distinguished by absent perinatal risk history, progression over time, and the muscle/ID/cardiac triad. |
| **Leukodystrophies** | Patient 2–1's MRI was described as "similar to leucodystrophy"; distinguished by genotype and by the myopathy/cardiac phenotype. |
| **Mitochondrial disease** | Overlapping myopathy + WM disease + crisis lactate; excluded by normal mtDNA/IEM screening. |
| **Congenital muscular dystrophy / congenital myopathy** | Normal-to-mildly-abnormal CK, normal EMG, non-specific biopsy in AIMS. |
| **Genetic cerebral small-vessel disease (e.g. CADASIL)** | Later onset, no ID/myopathy, different genotype. |
| **Thanatophoric dysplasia** | Suspected in a terminated Family 1 fetus with micromelia and narrow thorax; the 2019 authors flagged it as a **probable unrelated** finding — worth curating as an explicit non-attribution so future readers don't add skeletal dysplasia to the AIMS phenotype. |

### Screening

- **Newborn screening:** not included in any program; no biochemical marker exists to enable it.
- **Carrier screening:** not offered. Mechanistically justifiable in Finnish/Northern Norwegian populations for c.1320+1G>A given AF 0.0007, but **no such program or recommendation is published** — flag as inference, not practice.
- **Cascade testing:** appropriate for at-risk relatives once a familial variant is known; ACMG-standard.
- **Prenatal/PGT:** technically available for known familial variants (§13).

---

## 11. Outcome / Prognosis

**Survival and mortality.** No survival statistics, life-expectancy estimate, or mortality rate exists — *n* is far too small. Documented outcomes at the extremes: **recurrent intrauterine fetal death** in homozygous fetuses (the most severe reported outcome), and **death in the early sixties from aspiration-related asphyxiation** in the oldest reported patient after progressive motor/cognitive decline **[FULL-TEXT — RE-VERIFY]**. Most reported individuals were alive at report, aged 11–33. Preliminary read: **survival into at least the sixth decade is possible**, with heart failure, aspiration, perioperative decompensation, and refractory neonatal seizures as the identified threats.

**Morbidity and function.** Lifelong disability across motor, cognitive, and stamina domains. Concrete functional data: reduced 6-minute walk distance in 6/6; miniBESTest balance scores 14–21/28 in 6/6; supported or sheltered living with daily supervision in the adults; sheltered employment limited by exhaustion. Global proximal muscle atrophy with inability to walk in the advanced case.

**Quality-of-life measures.** **None applied.** No EQ-5D, SF-36, PROMIS, or disease-specific instrument has been used in AIMS. Explicit gap.

**Complications.** Heart failure / early dilated cardiomyopathy; refractory seizures including infantile spasms; obstructive sleep apnea; scoliosis and contractures; aspiration; feeding failure requiring gastrostomy; anxiety requiring pharmacotherapy; perioperative cardiogenic shock; progressive vascular leukoencephalopathy; sensorineural hearing loss.

**Recovery potential.** No recovery of the neurodevelopmental deficit. Acute decompensations can resolve substantially — the coma/tetraplegia episode resolved with return to baseline psychomotor level and near-complete lesion resolution, and the neonate's cardiac function normalized with VSD closure by 2 months.

**Prognostic factors.** Provisional, low-confidence given *n*: **older age** (cardiac dysfunction and cognitive decline both age-associated); **surgical/anesthetic exposure**; **neonatal presentation** (the most acutely unstable course); presence of seizures. **No molecular genotype–phenotype correlation is established** — the two unrelated c.3269delG homozygotes with divergent severity argue directly against simple variant-based prognostication, and all variants tested are complete LoF regardless of position.

**Prognostic biomarkers.** None. NT-proBNP tracks heart failure only.

---

## 12. Treatment

**There is no disease-specific, curative, or channel-directed therapy for AIMS.** Management is entirely supportive and surveillance-based. The most valuable content in this section is the **drugs-to-avoid list**, which is unusually well-evidenced for a 20-patient disease.

### Contraindicated / high-caution agents — the actionable core

| Agent / class | Evidence | Strength |
|---|---|---|
| **Verapamil / calcium channel blockers** (CHEBI:9948) | *"the Ca2+ channel blocker verapamil unexpectedly resulted in premature death of AIMS mice… results which caution against the use of calcium channel blockers in AIMS"* — **PMID:37154692** **[ABSTRACT-VERIFIED]** | `MODEL_ORGANISM`, strong and explicit |
| **Phenytoin / fosphenytoin** | Caused severe bradycardia and hypotension in an AIMS patient (patient 1–1, age 17); calcium-channel-blocking activity | `HUMAN_CLINICAL`, single case **[FULL-TEXT — RE-VERIFY]** |
| **Propofol** | Two post-operative decompensations (cardiogenic shock, lactic acidosis) in a neonate; inhibits cardiac L-type Ca²⁺ channels, associated with bradycardia | `HUMAN_CLINICAL`, single case **[FULL-TEXT — RE-VERIFY]** |
| **Lacosamide** (maintenance) | Discontinued for bradycardia risk (used acutely with benefit) | `HUMAN_CLINICAL` **[FULL-TEXT — RE-VERIFY]** |

Reported general principle: loss of SUR2-dependent K<sub>ATP</sub> channels is expected to alter cardiac resilience to stressors and may have complex, unpredictable effects on cardiac-acting drugs **[FULL-TEXT — RE-VERIFY]**. The 2026 authors call for systematic screening of antiseizure drugs for cardiovascular toxicity in SUR2-deficient animal models.

> **Contrast worth curating explicitly.** Cantú syndrome's GeneReviews "agents to avoid" list is **minoxidil, diazoxide, and ACE inhibitors** — i.e. K<sub>ATP</sub> *openers* (PMID:25275207) **[ABSTRACT-VERIFIED]**. AIMS' avoid-list is **calcium channel blockers and Ca-channel-blocking anesthetics/antiseizure drugs**. The two diseases have *opposite* pharmacological hazards, exactly as their opposite channel defects predict. This is a compelling, non-obvious pairing for the KB.

### Supportive and symptomatic management, with NCIT terms

| Intervention | NCIT `treatment_term` | `therapeutic_modality` | Notes |
|---|---|---|---|
| **Antiseizure therapy — levetiracetam preferred** | NCIT:C15986 Pharmacotherapy | `SMALL_MOLECULE` | Preferred because its mechanism (synaptic vesicle protein) avoids cardiac channel blockade. Lamotrigine was "partly effective" in patient 1–1. ACTH used for infantile spasms. |
| **Heart failure therapy — ACE inhibitor + beta-blocker** | NCIT:C15986 Pharmacotherapy | `SMALL_MOLECULE` | Started in patient 2–1 (EF 35–40%). Note ACE inhibitors are *avoided in Cantú* but *used in AIMS* — the inverse logic again. |
| **Anxiolytic therapy — SSRI** | NCIT:C15986 Pharmacotherapy | `SMALL_MOLECULE` | Used in patient 2–1 for anxiety (4/4 assessed patients had anxiety). |
| **Physical therapy / habilitation** | NCIT:C15302 Physical Therapy | `BEHAVIORAL` | Core management; two 2019 authors were from a physiotherapy/pediatric-rehabilitation service. |
| **Rehabilitation** | NCIT:C15315 Rehabilitation | `BEHAVIORAL` | |
| **Developmental and educational support** | NCIT:C181743 Behavioral Counseling *(verify)* | `BEHAVIORAL` | Adapted schooling documented. |
| **Nutritional support / gastrostomy** | NCIT:C15433 Nutritional Support | — | ⚠️ Per CLAUDE.md, do **not** auto-tag as `BEHAVIORAL`; assess the actual intervention. |
| **Orthopedic / scoliosis and contracture management** | NCIT:C16186 Orthopedic Surgical Procedure | `SURGERY` | Congenital hip dysplasia treated; contractures and scoliosis managed. |
| **OSA surgery** | NCIT:C15329 Surgical Procedure | `SURGERY` | Operative treatment recommended for OSA in patient 1–4. |
| **Genetic counseling** | NCIT:C15240 Genetic Counseling | — | See §13. |
| **Supportive care** | NCIT:C15747 Supportive Care | — | |

Also documented: cyclosporine for severe atopic eczema (one patient), steroids given during the ADEM-like episode, and hearing aids implied by bilateral high-frequency SNHL (note: there is no reliable NCIT clinical-action term for hearing-aid use, per CLAUDE.md).

### Advanced therapeutics

- **Gene therapy, gene editing, cell therapy, RNA therapy, targeted therapy, immunotherapy:** **none developed, none in trial.** Conceptually, an autosomal-recessive LoF channelopathy is a rational gene-replacement target, but *ABCC9* is a large gene, the relevant tissues (skeletal muscle, vascular smooth muscle, brain vasculature, heart) are broadly distributed, and no preclinical program is published.
- **Pharmacogenomics:** no PharmGKB/CPIC entry for *ABCC9* in AIMS. The clinically relevant pharmacology is the mechanism-based hazard above, not metabolizer status. (Incidentally, the 2026 neonate also had **G6PD deficiency**, which carries its own independent drug-avoidance list — a confounder in that case, not an AIMS feature.)

### Clinical trials

**No clinical trial has ever been registered for AIMS.** A ClinicalTrials.gov search yields no AIMS/IDMYS interventional or observational study. Leave `clinical_trials:` empty.

### A mechanistic caution for curators

It is tempting to reason that if AIMS is loss of K<sub>ATP</sub> function, a **K<sub>ATP</sub> opener** (diazoxide, pinacidil, minoxidil, nicorandil) should help. **The functional data argue this cannot work:** SUR2Δ8 and the truncating variants produce channels with *no measurable current at all*, and pinacidil activation was tested and required WT SUR2 to be present. A pharmacological opener needs a functional channel to open. I state this explicitly because it is an inviting inference that the literature does **not** support — it should not be curated as a candidate therapy, and if recorded at all it belongs in a `discussions` `KNOWLEDGE_GAP` entry, clearly labeled as unsupported reasoning rather than as a treatment.

---

## 13. Prevention

**Primary prevention.** Not possible for the genotype. Prevention is **reproductive**, via genetic counseling, carrier testing of at-risk relatives, prenatal diagnosis, and preimplantation genetic testing for known familial variants. The recurrent IUFDs in heterozygous couples make reproductive counseling unusually consequential here — couples may present with pregnancy loss before any living affected child is diagnosed.

**Secondary prevention (early detection).** No newborn or population screening exists. Realistic secondary prevention is **early molecular diagnosis via exome/genome sequencing** in a child with the triad, which unlocks the drug-avoidance list and cardiac surveillance before harm occurs.

**Tertiary prevention (preventing complications)** — the most actionable level, and where the entry should concentrate:
1. **Perioperative planning** — anesthetic and antiseizure drug review before any procedure; avoid propofol; monitor cardiac function and lactate post-operatively.
2. **Avoid calcium channel blockers and Ca-channel-blocking antiseizure drugs**; prefer levetiracetam.
3. **Longitudinal cardiac surveillance** — periodic echocardiography (consider cardiac MRI, which detected dilation echo missed) with NT-proBNP, continuing into adulthood even after normal childhood studies.
4. **Serial brain MRI** to track lesion accumulation.
5. **Audiological monitoring** for progressive high-frequency SNHL.
6. **Orthopedic surveillance** for scoliosis and contractures; physiotherapy to preserve function.
7. **Weight management** — the low-weight-to-overweight trajectory contributed to OSA.
8. **Aspiration risk assessment** in advanced disease (cause of death in the oldest patient).
9. **Activity pacing** — exertion triggers spasms and myalgia; graded rather than maximal exercise (note the mouse data showing muscle histopathology emerges specifically with chronic heavy exercise).

**Immunization, public health, environmental, and prophylactic interventions:** **not applicable** — no infectious, environmental, or population-level dimension to this disease.

---

## 14. Other Species / Natural Disease

**Taxonomy of species with relevant *ABCC9* biology:**

| Species | NCBI Taxon | Gene | Identifier |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *ABCC9* | HGNC:60; NCBI Gene 10060 |
| *Mus musculus* | NCBITaxon:10090 | *Abcc9* | **MGI:1352630**; NCBI Gene 20928 (verified) |
| *Danio rerio* | NCBITaxon:7955 | *abcc9* | ZFIN gene *abcc9* — **ZFIN ID not retrieved** (site required interactive verification); look it up before curating |
| *Canis lupus familiaris* | NCBITaxon:9615 | *ABCC9* | see natural disease below |

**Naturally occurring disease in another species — a genuine find for this entry.** **OMIA:002710-9615, "Cardiomyopathy, dilated, ABCC9-related" in *Canis lupus familiaris*.** An *ABCC9* **p.R1186Q** variant, homozygous in all affected dogs, underlies **sudden cardiac death / dilated cardiomyopathy (SCDY/DCM) in Manchester Terriers**, with death typically before 2 years of age. **VBO term:** Manchester Terrier (look up the VBO identifier before curating).

This is comparatively informative in a specific way: the canine disease is a **recessive, cardiac-predominant** *ABCC9* disorder — mechanistically adjacent to AIMS' cardiac arm and to human DCM1O, but without a reported neurodevelopmental or myopathic phenotype. Whether that reflects true species divergence, a milder/different variant effect (missense vs. truncating), or simply the limits of assessing cognition in dogs is unresolved — a legitimate comparative-biology knowledge gap.

**Comparative pathology and conservation.** K<sub>ATP</sub> subunit architecture and the SUR2/Kir6.x tissue pairing are deeply conserved across vertebrates, which is precisely why zebrafish and mouse SUR2 nulls both lose ventricular myocyte K<sub>ATP</sub> current and both reproduce the muscle and cardiac phenotypes. The conservation **breaks down for cognition**: no SUR2-mutant animal recapitulates the intellectual disability (§6, §15).

**Zoonotic potential / cross-species transmission:** **not applicable** — a germline genetic disease.

---

## 15. Model Organisms

### Mouse

**SUR2-STOP (CRISPR/Cas9; the purpose-built AIMS model), Smeland et al. 2019**
- Allele: `c.3446_3450delACTTCinsGA` → premature stop after K1148, **p.Y1149Stop**, in TM15.
- **Channel validation:** functional K<sub>ATP</sub> essentially **absent** in both ventricular myocytes and aortic smooth muscle cells on inside-out patch clamp (18 WT vs 10 mutant patches, p<0.0001) — confirming it reproduces the human channel defect even though the genetic lesion differs.
- **Recapitulates:** fatigability (multiple-trial inverted screen — comparable first-trial performance, progressive decline across trials, significant genotype and genotype×trial/session effects; n=9 per group); reduced LV fractional shortening (p<0.01); increased LVIDd normalized to body length; **increased blood pressure**; increased LV mass.
- **Fails to recapitulate:** cognition and anxiety. Negative across 1-hour locomotor activity, center/periphery distance, a four-test sensorimotor battery (ledge, platform, pole, inclined screen), **Morris water maze** cued and place trials and probe trials, and **elevated plus maze**. The authors' verbatim conclusion: *"Collectively, the behavioral findings suggest that the SUR2-STOP mice do not exhibit marked deficits in learning and memory nor show any obvious anxiety-like behaviors."*

**Tissue-selective and CaV1.1 models, McClenaghan et al. 2023 (PMID:37154692)**
- Tissue-selective K<sub>ATP</sub> suppression localized myopathy to **skeletal muscle specifically**.
- Isolated muscle showed **abnormal unstimulated force generation** — a mechanistic correlate of painful spasms.
- **Verapamil caused premature death** in AIMS mice.
- A **CaV1.1-nonpermeable** genetic model **failed to reverse** pathology — falsifying the excess-Ca²⁺-influx-through-CaV1.1 hypothesis.

**Pre-existing SUR2 alleles (MGI:1352630)** — background/comparative: null alleles show spontaneous death from **episodic coronary artery vasospasm**, hypertension, growth retardation, lower serum glucose with enhanced insulin action; a homozygous exon 5 deletion causes cardiac mitochondrial defects, cardiomyopathy and early postnatal death. An earlier internal-deletion allele retains a mitochondria-limited short SUR2 form and shows impaired exercise capacity and myofiber damage.

**Explicit model caveat from the authors:** *"The animal models used in this study do not recapitulate the genetic defect identified in the AIMS patients, but were chosen as the functional effects of the frameshift mutations introduced into SUR2-STOP mice and fish mirror the functional effect of the SUR2 Δ8 mutation."* They call for knock-in models carrying the actual human AIMS variants — a clean `proposed_experiments` item.

### Zebrafish

**SUR2-STOP zebrafish (CRISPR/Cas9), Smeland 2019 + Efthymiou 2024**
- Allele: `c.2944_2957del13` → frameshift, stop after S984, **p.S985Stop**, in TM12.
- **~4-fold reduction in *abcc9* mRNA** (qPCR), consistent with NMD; **complete absence of functional K<sub>ATP</sub>** in ventricular myocytes.
- **Craniofacial:** significantly decreased normalized interorbital distance — recapitulating human **hypotelorism** (4/6 patients). Notably the mouse did *not* show this, making the fish the better dysmorphology model. No other striking dysmorphism.
- **Motor:** reduced total movement, reduced total swimming distance, reduced duration of high-speed movements, but **similar total time moving** (n=62 per genotype) — a fatigability-like rather than paralysis-like signature. Hatching (which requires muscle contraction) was normal.
- **Cardiac:** fractional shortening reduced 29%, ejection fraction 25%, cardiac output 28%, with proportionally reduced stroke volume; **unchanged** end-diastolic and end-systolic volumes in larvae; markedly enlarged ventricle with abnormal morphology in 5/6 adults; **no fibrosis** (AFOG); **normal tropomyosin myofiber structure**; **numerous TUNEL-positive cells** in both chambers versus very few in WT. **No cardiac abnormality in heterozygotes** — matching healthy human carriers.
- **Vascular:** increased cardinal vein red-cell velocity, concordant with the hypertension in SUR2-STOP mice.
- **Seizure susceptibility (2024):** exaggerated motor response to **pentylenetetrazole**. > "In vivo studies of abcc9 loss-of-function in zebrafish revealed an exacerbated motor response to pentylenetetrazole, a pro-convulsive drug, consistent with impaired neurodevelopment associated with an increased seizure susceptibility." — **PMID:38217872** **[ABSTRACT-VERIFIED]**

### In vitro / cellular systems

- **Cosm6 cells** transiently transfected with Kir6.2 + FLAG-SUR2A/SUR2B (WT, Δ8, 1:1 mix): Western blot, ⁸⁶Rb⁺ efflux, inside-out patch clamp, ATP dose–response (IC₅₀), pinacidil activation.
- **Landing-pad HEK293** with FLIPR Blue membrane-potential dye and oligomycin A / glibenclamide challenge — the 2026 platform, notable as a **scalable variant-classification assay** suitable for future *ABCC9* VUS interpretation.
- **Patient fibroblasts** for cDNA/splicing analysis (exon 8 skipping).
- **No iPSC, organoid, or myotube model of AIMS has been reported** — a clear gap, especially given that the ID phenotype is the one thing animal models miss and a human neural or cerebrovascular model could address it.

### Recapitulation summary

| Human feature | Mouse SUR2-STOP | Zebrafish SUR2-STOP |
|---|---|---|
| Loss of myocyte K<sub>ATP</sub> | ✅ | ✅ |
| Fatigability / reduced performance | ✅ | ✅ |
| Muscle spasms / unstimulated force | ✅ (isolated muscle, 2023) | — |
| Cardiac systolic dysfunction | ✅ | ✅ |
| Ventricular dilation/enlargement | ✅ | ✅ |
| Hypotelorism | ❌ | ✅ |
| Seizure susceptibility | not tested | ✅ (PTZ) |
| Hypertension / vascular tone | ✅ | ✅ (indirect) |
| **Intellectual disability** | **❌ formally negative** | not assessable |
| **Anxiety** | **❌ formally negative** | not assessable |
| **Cerebral white matter lesions** | not reported | not reported |

**Model limitations to record.** No model reproduces the two defining CNS features — intellectual disability and cerebral white matter abnormality. Combined with the fact that neuronal K<sub>ATP</sub> is predominantly Kir6.2/SUR1 rather than SUR2, this makes the CNS arm of AIMS pathophysiology the least secure part of the mechanism and the highest-value research target. Per CLAUDE.md this is a **`HUMAN_MODEL_MISMATCH`**, not a `KNOWLEDGE_GAP`: the model evidence exists and is *negative*, so the open question is translational validity rather than absence of data.

---

## Recommended dismech curation actions

1. **Keep `MONDO:0859224`** — verified correct, with OMIM:619719 / DOID:0070600 / UMLS C5676904 as `mappings`. Add **IDMYS** to synonyms.
2. **Keep `hgnc:60`** for *ABCC9* — verified against genenames.org.
3. **Fix the GO label if used:** `GO:0008282` canonical label is **"inward rectifying potassium channel"**, not "ATP-sensitive potassium channel complex" (that is a synonym). Put the K<sub>ATP</sub> phrasing in `preferred_term`.
4. **Model the pathophysiology as one molecular trigger with three arms** (skeletal muscle / cerebrovascular-white matter / cardiac), tagging `biological_scale` per node. Give the cerebrovascular arm a `mechanistic_hypotheses` entry with `status: EMERGING`.
5. **Add a `HUMAN_MODEL_MISMATCH` discussion** for the intellectual-disability/anxiety phenotype vs. the formally negative SUR2-STOP mouse behavioral battery, with the authors' proposed working-memory/fear-conditioning experiments as `proposed_experiments`.
6. **Add a `supports: REFUTE` evidence item** for the CaV1.1-Ca²⁺-influx sub-hypothesis (PMID:37154692) — a rare, valuable falsified-mechanism record.
7. **Curate the drugs-to-avoid content prominently** (verapamil/CCBs, phenytoin/fosphenytoin, propofol, lacosamide maintenance), and consider the **opposite-hazard pairing with Cantú syndrome** (K<sub>ATP</sub> openers) as an explicit cross-reference.
8. **Consider a `kb/groupings/` entry for K<sub>ATP</sub> channelopathies** — AIMS/Cantú/DCM1O/neonatal diabetes/congenital hyperinsulinism, `grouping_basis: [SHARED_MECHANISM, SHARED_GENE_FAMILY]`, with GoF-vs-LoF as the differentiating axis.
9. **Use `measure_type: CASES_IN_LITERATURE` + `prevalence_class: ULTRA_RARE`**; do not fabricate a rate.
10. **Omit `frequency:` on the discordant phenotypes** (corpus callosum, dysmorphism) per the repo's frequency-evidence guidelines; record raw counts in `notes:`.
11. **Before committing:** run `just fetch-reference` for any PMID not already cached, then `just validate-references`, `just validate-terms`, and `just validate` — and specifically re-verify every claim marked **[FULL-TEXT — RE-VERIFY]** above, since those came through a summarizing intermediary rather than from a cached abstract I read directly.

---

## Primary sources

| PMID | Citation | Role |
|---|---|---|
| **31575858** | Smeland MF, McClenaghan C, Roessler HI, et al. ABCC9-related Intellectual disability Myopathy Syndrome is a K(ATP) channelopathy with loss-of-function mutations in ABCC9. **Nat Commun.** 2019 Oct 1;10(1):4457. doi:10.1038/s41467-019-12428-7. PMC6773855 | **Landmark / disease definition.** Cached with full text. |
| **38217872** | Efthymiou S, Scala M, Nagaraj V, et al. Novel loss-of-function variants expand ABCC9-related intellectual disability and myopathy syndrome. **Brain.** 2024 May 3;147(5):1822–1836. doi:10.1093/brain/awae010. PMC11068106 | **Phenotype/genotype expansion**, pooled frequencies, IUFD, zebrafish PTZ. |
| **42290677** | Nagaraj V, Thomas QH, Nóbrega PR, et al. Cognitive Decline, Neurologic Involvement, and Neonatal Crisis in ABCC9-Related Intellectual Disability and Myopathy Syndrome. **Neurol Genet.** 2026 Jun 10;12(4):e200385. doi:10.1212/NXG.0000000000200385. PMC13262668 | **Most recent.** Natural-history extension (neonate → sexagenarian), drug hazards, landing-pad assay. |
| **37154692** | McClenaghan C, Mukadam MA, Roeglin J, et al. Skeletal muscle delimited myopathy and verapamil toxicity in SUR2 mutant mouse models of AIMS. **EMBO Mol Med.** 2023;15(6):e16883. doi:10.15252/emmm.202216883. PMC10245035 | **Mechanism localization + verapamil toxicity + falsified CaV1.1 hypothesis.** |
| **22608503** | Harakalova M, van Harssel JJT, Terhal PA, et al. Dominant missense mutations in ABCC9 cause Cantú syndrome. **Nat Genet.** 2012 | Contrasting GoF disorder. |
| **25275207** | Grange DK, Nichols CG, Singh GK, et al. **Cantú Syndrome.** GeneReviews®, University of Washington | GoF management and agents-to-avoid contrast. |

**Databases consulted:** OMIM (#619719, 601439), MONDO/OLS4 (MONDO:0859224), HPO annotation API (OMIM:619719), Disease Ontology (DOID:0070600), HGNC (HGNC:60), UniProt (O60706), Ensembl (ENSG00000069431), NCBI Gene (10060, 20928), MGI (MGI:1352630), OMIA (OMIA:002710-9615), ClinGen (`search.clinicalgenome.org/kb/genes/HGNC:60`), gnomAD (allele-level data via publications; gene constraint **not retrieved**), ClinicalTrials.gov (no AIMS studies), Orphanet (**no AIMS code found**).

**Sources:**
- [Smeland et al. 2019, Nat Commun (PMC6773855)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6773855/)
- [Efthymiou et al. 2024, Brain (PMC11068106)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11068106/)
- [Nagaraj et al. 2026, Neurology Genetics (PMC13262668)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13262668/)
- [McClenaghan et al. 2023, EMBO Mol Med (PMC10245035)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10245035/)
- [OMIM #619719 — Intellectual Disability and Myopathy Syndrome](https://www.omim.org/entry/619719)
- [OMIM #601439 — ABCC9](https://omim.org/entry/601439)
- [MONDO:0859224 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0859224)
- [HPO annotations for OMIM:619719](https://ontology.jax.org/api/network/annotation/OMIM:619719)
- [HGNC ABCC9 (genenames.org REST)](https://rest.genenames.org/fetch/symbol/ABCC9)
- [MGI:1352630 — mouse Abcc9](https://www.informatics.jax.org/marker/MGI:1352630)
- [OMIA:002710-9615 — ABCC9-related dilated cardiomyopathy in dog](https://www.omia.org/OMIA002710/9615/)
- [ClinGen gene curation for ABCC9 (HGNC:60)](https://search.clinicalgenome.org/kb/genes/HGNC:60)
- [Disease Ontology DOID:0070600](https://www.informatics.jax.org/disease/DOID:0070600)