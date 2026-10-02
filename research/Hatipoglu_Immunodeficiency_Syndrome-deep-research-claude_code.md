---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T19:41:39.093748'
end_time: '2026-09-23T19:46:54.984620'
duration_seconds: 315.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hatipoglu Immunodeficiency Syndrome
  mondo_id: MONDO:0957229
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
  web_search_requests: 13
  num_turns: 29
  total_cost_usd: 1.5665656
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hatipoglu Immunodeficiency Syndrome
- **MONDO ID:** MONDO:0957229 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hatipoglu Immunodeficiency Syndrome** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research this condition using web search tools. Let me first load the necessary search capabilities.

# Hatipoglu Immunodeficiency Syndrome (HATIS) — Comprehensive Research Report

## Executive Summary

Hatipoglu Immunodeficiency Syndrome (HATIS; OMIM #620331; MONDO:0957229; MedGen C5830439; also designated "Immunodeficiency 111," IMD111) is a recently delineated (2022) autosomal recessive inborn error of immunity caused by biallelic loss-of-function/hypomorphic variants in **DPP9** (dipeptidyl peptidase 9; OMIM *608258; 19p13.3). It is a monogenic **inflammasomopathy**: loss of DPP9's restraint on the NLRP1 (and, as shown mechanistically in 2026, CARD8) inflammasomes causes constitutive caspase-1 activation, IL-1β release, and pyroptotic cell death — most consequentially in hematopoietic stem/progenitor cells (HSPCs) and keratinocytes. Clinically the disease presents in early childhood with failure to thrive, short stature, pancytopenia/bone-marrow failure, recurrent bacterial and herpesviral infections, and a distinctive skin phenotype (eczema, dyspigmentation, petechiae), with variable neurodevelopmental features. It is disease-defining, ultra-rare (four patients from three families in the founding report, plus a fourth family reported in 2025), and severe — three of the first four reported patients required hematopoietic stem cell transplantation (HSCT).

---

## 1. Disease Information

**Overview.** HATIS is an autosomal recessive immunologic/autoinflammatory disorder of childhood onset characterized by failure to thrive, skin manifestations, pancytopenia, and susceptibility to recurrent infections, caused by biallelic (homozygous or compound heterozygous) DPP9 variants (Harapas et al., *Sci Immunol* 2022, PMID:36112693). It was named for the discovering clinician/family series (Hatipoğlu N., a co-author on the founding paper) following the OMIM naming convention for newly described monogenic disorders.

**Key identifiers:**
- **OMIM (phenotype):** #620331 — HATIPOGLU IMMUNODEFICIENCY SYNDROME; HATIS
- **OMIM (gene):** *608258 — DIPEPTIDYL PEPTIDASE IX; DPP9 (19p13.3)
- **MONDO:** 0957229
- **MedGen:** C5830439 (UID 1841075)
- **Synonym:** Immunodeficiency 111 (IMD111)
- **Gene:** DPP9 (HGNC symbol DPP9; chr19:4,675,224–4,724,673, GRCh38)
- No dedicated **Orphanet**, **ICD-10/ICD-11**, or **GeneReviews** entry currently exists — this is expected given the disease was first described in 2022 with only a handful of published families; standard nosology resources have not yet caught up. (Source class: structured database absence, checked directly against MedGen/OMIM/Orphanet gene pages, September 2026.)

**Synonyms/alternate names:** HATIS; Immunodeficiency 111 (IMD111); "DPP9 deficiency" (mechanistic/functional name used interchangeably in the primary literature, e.g., Harapas et al. title "DPP9 deficiency: An inflammasomopathy that can be rescued by lowering NLRP1/IL-1 signaling").

**Data provenance.** All clinical characterization to date derives from **aggregated case series and individual case reports** (n=4 in the founding cohort, plus subsequent single-family/twin case reports) rather than large aggregated disease-level registries — this is a disease-level knowledge base built from primary literature synthesis, not from an EHR/claims aggregation resource, given its rarity and recency.

---

## 2. Etiology

**Primary cause — genetic, monogenic.** HATIS is caused by biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in **DPP9**, encoding dipeptidyl peptidase 9, a serine protease that is a direct negative regulator of the NLRP1 (and CARD8) inflammasomes (PMID:36112693).

**Genetic risk factors:**
- **Consanguinity** is a documented risk factor in at least 2 of the 3 founding families: Family 2 (14-year-old boy, homozygous c.2551C>T, p.Gln851Ter, consanguineous Turkish parents) and Family 3 (2 male patients, homozygous c.331C>T, p.Arg111Ter, consanguineous Bedouin family, Israel). Family 1's proband was **compound heterozygous** (paternal p.Gly167Ser [c.499G>A]; maternal p.Ser214Ter), consistent with a non-consanguineous mating (PMID:36112693; ClinVar RCV003224652 for c.499G>A/p.Gly167Ser).
- A 2025 case report (PMID:41082409) describes 8-month-old **dizygotic/monozygotic twins** from a **non-consanguineous** marriage with biallelic DPP9 mutation, expanding the mutational/ancestral spectrum beyond the original consanguineous founder families.
- No modifier genes have yet been reported for HATIS specifically, though the mouse genetic-rescue data (below) implicate the entire NLRP1→ASC→caspase-1→GSDMD→IL-1R axis as a mechanistic "modifier pathway" whose dosage determines severity.

**Environmental risk factors:** None established; this is a fully penetrant monogenic disease with no reported environmental gene–disease interaction data. Infections (herpesviruses, bacterial otitis/bronchitis pathogens) are a **consequence** of the immunodeficiency rather than a cause, though they may act as **triggers/exacerbants** of inflammasome flares in a susceptibility background (analogous to the de novo dominant-negative DPP9 disorder below, where infection precipitated HLH-like hyperinflammation).

**Protective factors:** None reported. There is no described protective allele or environmental protective factor.

**Gene–environment interactions:** Not established for biallelic HATIS. However, the mechanistically related **monoallelic, dominant-negative DPP9 disorder** (see below) shows that inflammasome-priming stimuli (e.g., infection) can precipitate acute HLH-like crises on a sensitized inflammasome-regulatory background — a plausible but unproven gene–environment interaction template for HATIS flares as well.

**Important nosological distinction — do not conflate two DPP9-related conditions:**

| Feature | HATIS (biallelic) | De novo dominant-negative DPP9 disorder |
|---|---|---|
| Inheritance | Autosomal recessive, biallelic LOF/hypomorphic | Heterozygous, de novo, dominant-negative |
| Variant | e.g., p.Gln851Ter, p.Arg111Ter, p.Gly167Ser/p.Ser214Ter | c.755G>C, p.Arg252Pro |
| Mechanism | Complete/near-complete loss of DPP9 restraint | Destabilized DPP9 (26–52% WT levels) still fails to restrain NLRP1/CARD8 |
| Phenotype | Pancytopenia, failure to thrive, skin disease, recurrent infection (chronic) | HLH-like hyperinflammation, massive IL-1β/IL-18, hepatosplenomegaly, fever (acute/severe infantile) |
| Reference | Harapas et al. 2022, PMID:36112693 | Wolf et al. 2023, *J Allergy Clin Immunol* 152(5):1336–1344.e5, PMID:37544411 |

This distinction should be preserved in curation — the dominant-negative disorder is a **distinct clinical entity sharing the same gene and inflammasome mechanism**, not a HATIS subtype, per the design-decision on keeping germline mechanism-sharing entities separate unless explicitly lumped by the field.

---

## 3. Phenotypes

Phenotype data below are drawn from the MedGen/OMIM clinical synopsis for #620331 and the Harapas et al. 2022 primary cohort (4 patients, ages 6–14 at description) plus the 2025 twin case report (PMID:41082409). **Frequencies among only 4–6 published patients should be read as small-n case-series proportions, not population-level penetrance estimates** — a caveat that should be preserved in any curated frequency field.

### Symptoms / Clinical Signs

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Failure to thrive | HP:0001508 | Reported in essentially all patients (defining feature) |
| Fetal growth restriction | HP:0001511 | Prenatal onset in some patients |
| Proportionate short stature | HP:0003508 | |
| Feeding difficulties | HP:0011968 | |
| Recurrent infections | HP:0002719 | Defining feature |
| Recurrent otitis media | HP:0000403 | |
| Recurrent bronchitis | HP:0002837 | |
| Recurrent herpes | HP:0100819 (herpetic infection context) / herpes simplex/zoster reactivation | Reported in 2 of 4 founding patients |
| Recurrent fever | HP:0001954 | |
| Febrile seizures | HP:0002373 | |
| Pancytopenia | HP:0001876 | Core hematologic feature; drove HSCT decision in 3/4 patients |
| Anemia | HP:0001903 | |
| Petechiae | HP:0000967 | |
| Infantile eczema / atopic dermatitis | HP:0001047 (Atopic dermatitis) | In 2/4 patients |
| Eczematoid dermatitis | related to HP:0000964 (Eczema) | |
| Dry skin | HP:0000958 | |
| Thickened skin | HP:0008065 | |
| Anhidrosis | HP:0000970 | |
| Hyper-/hypopigmented macules | HP:0007440 (Hyperpigmented skin macules) / HP:0001053 (Hypopigmented skin patches) | Distinctive dyspigmentation reported in all founding patients |
| Premature graying / fair hair | HP:0002216 (Premature graying of hair) | |
| Poor wound healing | HP:0001058 | |
| Learning disability / speech delay | HP:0002194 (Delayed speech and language development), HP:0001328 (Specific learning disability) | 3 of 4 patients |
| Autism spectrum / autistic behavior | HP:0000717 | 2 of 4 patients |
| Slurred speech | HP:0001350 | |
| Downslanting palpebral fissures | HP:0000494 | 2 of 4 patients |
| Broad forehead | HP:0000337 | |
| Hemivertebrae | HP:0002937 | 2 of 4 patients |
| Cryptorchidism | HP:0000028 | |
| Hypospadias | HP:0000047 | |
| Inguinal hernia | HP:0000023 | |
| Asthma/allergy | HP:0002099 (Asthma) | |

### Phenotype characteristics
- **Age of onset:** Childhood, often with prenatal (fetal growth restriction) or infantile onset of failure to thrive; the 2025 case report describes presentation at 8 months of age (twins) with severe anemia and infections.
- **Severity:** Variable but often severe — 3 of the 4 founding-cohort patients ultimately required HSCT for bone marrow failure/pancytopenia.
- **Progression:** Chronic and progressive marrow failure with episodic infectious/inflammatory flares; not classically relapsing-remitting but punctuated by acute infectious or inflammatory episodes.
- **Frequency (case-series, not population level):** Neurodevelopmental features (learning disability/speech delay) in 3/4; autism spectrum features in 2/4; craniofacial dysmorphism (downslanting palpebral fissures) in 2/4; hemivertebrae in 2/4 — small numbers, interpret cautiously.
- **Quality of life impact:** Not formally measured with validated instruments (EQ-5D, SF-36) in the literature to date; qualitatively, recurrent hospitalization for infection/transfusion (documented explicitly in the 2025 twin case, PMID:41082409: "recurrent sino-pulmonary infections requiring multiple hospitalizations and blood transfusions") and HSCT burden indicate substantial disease impact, but no formal QoL instrument data exist — **this is a genuine evidence gap**, not merely unreported.

---

## 4. Genetic/Molecular Information

**Causal gene:** DPP9 (dipeptidyl peptidase 9), HGNC symbol DPP9, OMIM *608258, chromosome 19p13.3 (GRCh38 chr19:4,675,224–4,724,673). Ubiquitously expressed with highest levels in liver, heart, and muscle, lowest in brain (per GeneCards/OMIM gene summary).

**Protein:** 863 amino acids, ~98 kDa, containing an active-site serine protease motif (GWSYG, post-proline dipeptidyl aminopeptidase activity cleaving Xaa-Pro dipeptides from protein N-termini) and 2 N-glycosylation sites. DPP9 is cytosolic (unlike its membrane-bound relative DPP4/CD26) and is a member of the S9B prolyl oligopeptidase family together with DPP8.

**Reported pathogenic variants (biallelic HATIS):**

| Family | Genotype | Variant(s) | Consequence | Consanguinity |
|---|---|---|---|---|
| 1 | Compound heterozygous | c.499G>A (p.Gly167Ser, paternal) / p.Ser214Ter (maternal) | Missense (hypomorphic) / nonsense | Not stated as consanguineous |
| 2 | Homozygous | c.2551C>T (p.Gln851Ter) | Nonsense, exon 21; absent DPP9 protein on patient fibroblast Western blot, consistent with nonsense-mediated decay → complete loss of function | Consanguineous (Turkish) |
| 3 (2 affected males) | Homozygous | c.331C>T (p.Arg111Ter) | Nonsense, exon 5 | Consanguineous (Bedouin, Israel) |
| 2025 twin case | Biallelic (specific alleles not extracted from abstract) | Not detailed in available abstract | — | Non-consanguineous |

Source: Harapas et al., *Sci Immunol* 2022 (PMID:36112693); ClinVar RCV003224652 for p.Gly167Ser; Singh et al. 2025 (PMID:41082409).

**Variant classification / functional impact:** The Harapas et al. paper functionally characterized these variants as **hypomorphic or loss-of-function alleles that fail to repress NLRP1** — i.e., `FunctionalImpactEnum` = `LOSS_OF_FUNCTION` (nonsense alleles p.Gln851Ter, p.Arg111Ter, p.Ser214Ter) or `PARTIAL_LOSS_OF_FUNCTION`/hypomorphic (missense p.Gly167Ser). ACMG/AMP classification per ClinVar for p.Gly167Ser should be checked directly in ClinVar at curation time rather than assumed.

**Allele frequency:** Not reported in the primary literature abstracts retrieved; given the extreme rarity (four families worldwide as of the founding report, one additional twin case since), these variants are expected to be private/family-specific or extremely rare in gnomAD — **this should be verified directly against gnomAD at curation time** rather than asserted from memory (per this repository's Ontology Term Contract, the same "never write from memory" discipline extends to any quantitative claim not directly sourced).

**Somatic vs. germline:** All reported HATIS variants are **germline**.

**Contrast — the dominant-negative variant:** c.755G>C (p.Arg252Pro), heterozygous, de novo, in the distinct HLH-like hyperinflammatory disorder (PMID:37544411). This variant destabilizes the DPP9 protein (reducing expression to ~26–52% of wild-type in transfected cells) such that the mutant protein "failed to restrain the NLRP1 and CARD8 inflammasomes, resulting in constitutive inflammasome activation" — a **dominant-negative** mechanism, mechanistically and clinically distinct from the biallelic loss-of-function/hypomorphic HATIS variants.

**Modifier genes:** None specifically implicated in HATIS patients, but functional/genetic-rescue data in animal models (see Mechanism, below) show that Nlrp1a/b/c, Asc (Pycard), Gsdmd, Il-1r, and — in the humanized mouse — CARD8/CASP1 are all dosage-sensitive modifiers of the phenotype, making them plausible candidate modifier loci for human disease severity, though this is inferred from model systems and not yet demonstrated in patients.

**Epigenetic information:** None reported for HATIS.

**Chromosomal abnormalities:** None; this is a point-mutation/small-indel disorder, not a copy-number or structural disorder.

---

## 5. Environmental Information

HATIS is a monogenic disorder with no established primary environmental etiologic factor. The clinically relevant "environmental" contributors are **infectious triggers of disease flares/complications** rather than causes of the underlying disease:
- **Infectious agents** documented in patients: herpesviruses (recurrent herpetic infections), otitis-media pathogens, and bronchitis-associated respiratory pathogens — these represent the **consequence** of impaired immune competence (recurrent infection susceptibility) but, per the mechanistically related dominant-negative DPP9 disorder, infection may also act as a **trigger** that precipitates acute inflammasome-driven hyperinflammatory flares on top of chronic immunodeficiency. No specific pathogen has been identified as a required precipitant for HATIS-specific inflammasome flares (as distinct from the HLH-like disorder).
- **Lifestyle/toxin/occupational factors:** None reported; disease onset is in infancy/early childhood, prior to occupational exposure windows.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function or hypomorphic variants in DPP9** (e.g., p.Gln851Ter, p.Arg111Ter, p.Gly167Ser/p.Ser214Ter) → **loss (or severe reduction) of DPP9 dipeptidyl peptidase/scaffolding activity** in patient cells (demonstrated directly: patient fibroblasts from Family 2 showed absent DPP9 protein by Western blot, PMID:36112693).
2. Loss of DPP9 → **failure to form the inhibitory DPP9–NLRP1(FIIND)–NLRP1(C-terminal UPA-CARD fragment) ternary complex** that normally sequesters the autoproteolytically-generated NLRP1 C-terminal fragment in an inactive state (mechanism established in Nature 2021, PMID for "DPP9 sequesters the C terminus of NLRP1 to repress inflammasome activation," and corroborating structural/biochemical studies of the FIIND ZU5-UPA autoproteolysis and "functional degradation"/N-end-rule model of NLRP1 activation).
3. Loss of ternary-complex sequestration → **the NLRP1 C-terminal UPA-CARD fragment is liberated from autoinhibition and free to oligomerize**, and — as shown by direct reverse-genetics evidence in a 2026 humanized-mouse study — **the CARD8 inflammasome is analogously de-repressed** in human hematopoietic cells (PMID:42427515/JCI 10.1172/JCI207530). This is the key **human-specific branch point**: mouse Dpp9 loss activates NLRP1 but (because mice lack a functional CARD8) does not recapitulate the CARD8-driven hematopoietic phenotype, explaining why constitutive Dpp9-knockout mice have grossly normal hematopoiesis despite recapitulating other aspects of disease.
4. Liberated NLRP1 (skin, epithelial tissue) and CARD8 (human hematopoietic stem/progenitor cells, HSPCs — CARD8 is "absent from the mouse genome yet highly enriched in human hematopoietic cell populations," per the 2026 JCI study) **assemble into an active inflammasome complex** recruiting ASC (in the NLRP1 branch) and activating **caspase-1**.
5. Caspase-1 activation → (a) **cleavage and activation of gasdermin D (GSDMD)**, driving **pyroptotic cell death**, and (b) **proteolytic maturation and release of IL-1β** (and, to a lesser/dispensable extent based on murine rescue data, IL-18).
6. In **HSPCs**, CARD8-inflammasome-driven pyroptosis (demonstrated by CASP1/CARD8 genetic deletion rescuing cytopenia and HSPC survival in the humanized mouse model, while NLRP1 deletion did not) causes **direct destruction of the hematopoietic stem/progenitor pool** → **bone marrow failure, pancytopenia, and anemia** — the dominant, treatment-defining clinical feature requiring HSCT in most reported patients.
7. In **keratinocytes and skin**, spontaneous NLRP1 inflammasome activation (directly demonstrated ex vivo in patient keratinocytes, PMID:36112693) drives **IL-1β-mediated cutaneous inflammation**, manifesting as eczema/dermatitis, petechiae (from combined thrombocytopenia and vascular inflammation), and pigmentary change.
8. Chronic systemic low-grade inflammasome activation plus loss of the immune cell compartments that depend on intact hematopoiesis (neutrophils, lymphocytes) together produce **failure to thrive/growth restriction** and **immunodeficiency with recurrent bacterial and herpesviral infection** — the latter reflecting depletion of both innate (neutrophil) and adaptive (T/B/NK) effector populations secondary to marrow failure, compounding any cell-intrinsic lymphocyte inflammasome dysregulation.
9. **Neurodevelopmental and skeletal features** (learning disability, autism-spectrum features, hemivertebrae, craniofacial dysmorphism) are reported in a subset of patients; a direct causal inflammasome mechanism for these specific features has not been mechanistically demonstrated in the literature reviewed and should be treated as an **associated but mechanistically unresolved** part of the phenotype (a candidate `HUMAN_MODEL_MISMATCH`/knowledge-gap discussion point for curation, since animal models do not obviously recapitulate this branch).

### Molecular pathways
- **NLRP1 inflammasome pathway** (canonical activation via FIIND autoproteolysis + N-end-rule/functional degradation model): GO:0140639 (NLRP1 inflammasome complex) / relevant GO biological process terms for "positive regulation of NLRP1 inflammasome complex assembly."
- **CARD8 inflammasome pathway** (human-specific, hematopoietic-restricted) — mechanistically analogous FIIND-domain regulation by DPP9.
- **Pyroptosis** — GO:0070269 (pyroptotic cell death; gasdermin D pore formation).
- **IL-1β maturation/signaling** — caspase-1-dependent pro-IL-1β cleavage; IL-1R signaling.

### Cellular processes
- Pyroptosis (GSDMD-mediated), inflammatory cytokine release (IL-1β predominant; IL-18 dispensable per murine genetic-rescue data), keratinocyte-intrinsic inflammasome activation, hematopoietic stem/progenitor cell death.

### Protein dysfunction
- DPP9 loss of scaffolding/enzymatic function → derepression (not "gain of function" of a pathway per se, but qualitative loss of restraint) of NLRP1/CARD8 — this is the canonical **LOSS_OF_FUNCTION** variant-level annotation on `GeneticContext`, with the downstream pathway node itself appropriately annotated `GAIN_OF_FUNCTION`/`INCREASED` (inflammasome activity) as a pathway-state modifier, since the pathway activation is qualitatively unconstrained rather than merely quantitatively elevated above a normally-regulated baseline.

### Tissue damage mechanisms
- Direct pyroptotic destruction of HSPCs (bone marrow failure) and likely of keratinocytes/skin-resident cells (dermatitis, petechiae via vascular/platelet involvement).

### Cell types involved (suggested CL terms)
- Hematopoietic stem cell (CL:0000037)
- Hematopoietic multipotent progenitor cell (CL:0000048)
- Keratinocyte (CL:0000312)
- Neutrophil (CL:0000775) — secondarily depleted
- T cell (CL:0000084), B cell (CL:0000236), NK cell (CL:0000623) — secondarily depleted, per patient immunophenotyping showing "markedly reduced neutrophils and T/B/NK cells" in the related dominant-negative disorder (PMID:37544411) and pancytopenia in HATIS itself.

### Molecular profiling / advanced technologies
- The 2026 JCI reverse-genetics study (PMID:42427515) used a **humanized mouse model (MISTRG6)** engrafted with human HSPCs to demonstrate that "DPP9 deletion led to little transcriptional changes, suggesting post-transcriptional regulation in human HSPCs" — i.e., **transcriptomic profiling was performed and was uninformative/negative**, with the causal mechanism instead resolved by targeted genetic epistasis (CARD8/CASP1 knockout rescue) rather than by expression-based discovery. This is a useful `analyses` provenance note: transcriptomics was attempted (`SUCCEEDED` as an assay, but essentially a negative/non-explanatory result) and the definitive mechanistic claim rests on CRISPR-based reverse genetics in the humanized model, not on omics.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Bone marrow/hematopoietic system (pancytopenia, marrow failure), skin/integument (eczema, dyspigmentation, petechiae, anhidrosis), immune system broadly (recurrent infection).
- **Secondary/complication-driven:** Respiratory system (recurrent bronchitis, sino-pulmonary infection in the twin case), ENT (recurrent otitis media), reproductive/genitourinary (cryptorchidism, hypospadias — reported in a subset), musculoskeletal (hemivertebrae), CNS/neurodevelopmental (learning disability, speech delay, autism-spectrum features).
- **Body systems:** Hematologic/immune (primary), integumentary (primary), musculoskeletal, genitourinary, nervous system (secondary/associated).

**Tissue/cell level:** Bone marrow stroma and hematopoietic stem/progenitor compartment (CL:0000037); epidermal keratinocytes (CL:0000312); circulating leukocyte lineages (neutrophils, T/B/NK cells) reduced secondary to marrow failure.

**Subcellular level:** Cytosolic — DPP9 is a cytosolic serine protease (unlike membrane-bound DPP4); the NLRP1/CARD8 inflammasome complex it regulates assembles in the cytoplasm (GO cellular component: cytosol, GO:0005829; inflammasome complex, GO:0061702).

**Localization:** Bilateral/systemic — no lateralization reported; skin findings and marrow failure are systemic/diffuse rather than focal.

**Suggested UBERON terms:** bone marrow (UBERON:0002371), skin epidermis (UBERON:0001003), hematopoietic system (UBERON:0002390).

---

## 8. Temporal Development

- **Onset:** Childhood, with evidence of onset as early as the **prenatal period** (fetal growth restriction reported) and presentation in **infancy** (the 2025 twin case presented at 8 months of age). The founding cohort patients were characterized at ages 6–14 years, reflecting diagnostic delay typical of an ultra-rare, only-recently-molecularly-defined disease rather than true late onset.
- **Onset pattern:** Insidious/chronic (failure to thrive, growth restriction, progressive cytopenia) punctuated by **acute** infectious/febrile episodes.
- **Progression:** Progressive bone marrow failure culminating in need for HSCT in the majority of reported patients (3 of 4 founding-cohort patients); disease course otherwise chronic with recurrent infectious and dermatologic flares rather than a discrete staged progression model (no formal staging system exists, as expected for an ultra-rare monogenic disorder).
- **Disease course pattern:** Chronic with superimposed acute infectious/inflammatory episodes; not classically relapsing-remitting in the autoimmune sense, though marrow failure severity and infection frequency vary over time.
- **Duration:** Chronic, lifelong absent curative intervention (HSCT); no reports of spontaneous resolution.
- **Remission:** No spontaneous remission reported; HSCT is reported as a disease-modifying/curative intervention for the hematologic phenotype in the patients who received it (specific post-HSCT outcome/survival data were not extracted in full from the abstracts reviewed and should be verified against full text at curation time).
- **Critical periods:** Early recognition and consideration of HSCT before life-threatening cytopenia/infection appears to be the key intervention window, based on the pattern of eventual bone marrow transplantation in most reported cases (inference from case pattern, not a formally stated "critical period" in the literature).

---

## 9. Inheritance and Population

**Epidemiology:** HATIS is **ultra-rare** — the founding description (2022) reported only **4 patients from 3 unrelated families**; a subsequent 2025 case report added twin siblings from a fourth, non-consanguineous family. No formal prevalence or incidence estimate exists in Orphanet, GBD, or national registries (expected/appropriate given fewer than 10 published cases as of this report). Any curated `Prevalence` record should use `measure_type: CASES_IN_LITERATURE` and `prevalence_class: NOT_YET_DOCUMENTED` rather than inventing a numeric estimate.

**Inheritance pattern:** Autosomal recessive (biallelic DPP9 variants required for HATIS). The mechanistically related but clinically distinct hyperinflammatory disorder is **autosomal dominant/de novo** (heterozygous dominant-negative) — see the nosological distinction table in Section 2. Do not conflate the two inheritance patterns under one entry.

**Penetrance:** Appears fully penetrant among biallelic carriers in the reported families (all reported biallelic individuals were symptomatic), though the numerator (n≈6 published cases) is far too small to formally estimate penetrance with confidence.

**Expressivity:** Variable — e.g., neurodevelopmental features (autism-spectrum, learning disability), skeletal anomalies (hemivertebrae), and facial dysmorphism were present in some but not all founding-cohort patients despite presumably similarly severe loss-of-function genotypes, indicating variable expressivity of the extra-hematologic/extra-cutaneous phenotype.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported.

**Founder effects:** Not established; the four founding families are geographically/ethnically diverse (unspecified/Australian-ascertained Family 1, Turkish consanguineous Family 2, Bedouin-Israeli consanguineous Family 3), arguing against a single founder allele, though each family's specific variant may be a local founder allele within its population — this has not been formally tested.

**Consanguinity role:** Documented in 2 of the first 3 families (Families 2 and 3), consistent with the expected enrichment of rare autosomal recessive disease in consanguineous unions; however, the twin case (2025) and Family 1 (compound heterozygous) demonstrate the disease also occurs in non-consanguineous settings.

**Carrier frequency:** Not established/reported; given the extreme rarity and apparent allelic heterogeneity (distinct private variants in each family), no meaningful population carrier frequency can currently be stated — verify directly against gnomAD allele counts for each specific variant at curation time rather than inferring a population-level carrier rate.

**Population demographics:** Reported cases span Australian (ascertainment center), Turkish, Bedouin-Israeli, and unspecified additional (2025 twin case) ancestries — no single ethnic group appears preferentially affected based on current (extremely limited) case numbers.

**Sex ratio:** Of the founding cohort, at least 3 of 4 reported patients are described as male (Family 2's single patient and Family 3's two patients are explicitly male); Family 1's proband's sex was not specified in the sources reviewed. This is too small a sample to establish a true sex ratio, and no biological (e.g., X-linked modifier) basis for male predominance has been proposed — treat as an observation, not an established epidemiological sex ratio.

**Age distribution:** All reported patients are pediatric at diagnosis (infancy through mid-adolescence); no adult-onset or adult-diagnosed cases have been reported, consistent with the severity of the hematologic phenotype necessitating early clinical attention.

---

## 10. Diagnostics

**Laboratory tests:**
- Complete blood count showing pancytopenia/anemia (core finding).
- Inflammatory marker elevation (in the mechanistically related dominant-negative disorder: elevated LDH, ferritin, soluble IL-2 receptor, triglycerides, and "massively increased" serum IL-1β and IL-18 — PMID:37544411; analogous but generally less extreme inflammatory marker elevation is expected in classic biallelic HATIS, though this should be confirmed per-patient rather than assumed to be identical to the dominant-negative phenotype).
- Immunophenotyping showing reduced neutrophils and T/B/NK lymphocyte populations.
- Dihydrorhodamine (DHR) test: in the 2025 twin case, DHR testing was **positive**, initially suggestive of chronic granulomatous disease, until whole-exome sequencing redirected the diagnosis to DPP9 mutation — an important **differential-diagnosis pitfall** worth noting for diagnostic-criteria curation (DHR abnormalities are not specific to CGD and can occur in other neutrophil-affecting immunodeficiencies).

**Genetic testing:** **Whole-exome sequencing (WES)** was the diagnostic modality in all reported cases (founding cohort and 2025 twin case). No dedicated commercial gene panel or GTR-listed single-gene test was identified in the sources reviewed; given the disease's recent molecular delineation (2022), it is most likely to be diagnosed via WES/WGS with subsequent identification of biallelic DPP9 variants, rather than via a targeted panel — clinicians should ensure DPP9 is included in relevant primary immunodeficiency/bone-marrow-failure/autoinflammatory gene panels going forward.

**Functional/research-level confirmation used in the literature (not yet routine clinical tests):**
- Western blot for DPP9 protein in patient fibroblasts (confirmed absent protein in the Gln851Ter homozygote, supporting nonsense-mediated decay/complete loss of function).
- Ex vivo keratinocyte inflammasome activation assays (spontaneous NLRP1 activation demonstrated in patient keratinocytes).
- Serum IL-1β/IL-18 measurement as a research-level functional readout of inflammasome activity.

**Imaging/other:** No disease-specific imaging protocol reported; skeletal imaging may reveal hemivertebrae as an incidental/associated finding.

**Differential diagnosis:** Other inborn errors of immunity presenting with bone marrow failure and recurrent infection (e.g., Fanconi anemia, dyskeratosis congenita, GATA2 deficiency, severe combined immunodeficiency variants), other monogenic autoinflammatory/inflammasomopathy disorders (NLRP1-associated autoinflammation with arthritis and dyskeratosis [NAIAD], CARD8-related disease), and — critically, per the 2025 case — **chronic granulomatous disease** (given a false-suggestive positive DHR test in at least one reported case).

**Screening:** No newborn screening or population carrier-screening program exists for this ultra-rare, only-recently-described disorder.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No formal survival statistics (5-year/10-year survival rates) exist given the extremely small published cohort; outcome data are anecdotal/case-level. Three of the four founding-cohort patients required HSCT for bone marrow failure, implying that without transplantation the hematologic phenotype is life-threatening; specific post-HSCT survival/engraftment outcomes were not fully extracted from the abstracts reviewed here and should be confirmed against full text before use in a curated `Outcome`/`Prognosis` field — do not assert a specific survival percentage without direct verification.

**Morbidity:** Substantial — recurrent infection requiring hospitalization, recurrent transfusion dependence (explicitly described in the 2025 twin case: "recurrent sino-pulmonary infections requiring multiple hospitalizations and blood transfusions," PMID:41082409), chronic skin disease, and in a subset, neurodevelopmental impairment (learning disability, autism-spectrum features) with associated long-term functional impact.

**Quality of life:** No validated QoL instrument data reported — genuine gap, not merely unreported detail.

**Complications:** Bone marrow failure/pancytopenia (primary complication driving HSCT), recurrent/severe infections (bacterial, herpesviral), transfusion-related complications (implied by transfusion dependence), and potential HSCT-related morbidity (not itself disease-specific but a consequence of the required intervention).

**Recovery potential:** HSCT is reported as the definitive intervention for the hematologic phenotype in patients who progress to bone marrow failure; whether HSCT also modifies the extra-hematologic (skin, neurodevelopmental) phenotype is not established in the sources reviewed.

**Prognostic factors:** Not formally modeled; qualitatively, severity of pancytopenia appears to be the key driver of need for HSCT.

---

## 12. Treatment

**Pharmacotherapy:**
- **IL-1 blockade (anakinra)** has been attempted clinically. In one reported case, anakinra (2–4 mg/kg/day) over one week was **ineffective**, and following a subsequent inflammatory flare with elevated proinflammatory cytokines, the clinical team proceeded to allogeneic HSCT (source: search synthesis of case-report literature; this specific dosing/outcome detail should be re-verified against the primary full-text source before being entered as a curated evidence snippet, since it was obtained via a secondary AI-generated search summary rather than direct abstract text in this session — flagged here explicitly per this repository's attribution discipline).
- Suggested NCIT term for anakinra as a therapeutic agent: NCIT (IL-1 receptor antagonist) — CHEBI term for anakinra itself should be looked up directly (CHEBI ID not verified in this session).
- Preclinically, **genetic (not yet pharmacologic) lowering of NLRP1/IL-1 signaling rescues murine and zebrafish phenotypes** (Harapas et al. 2022): removal of a single copy of Nlrp1a/b/c, Asc, Gsdmd, or Il-1r — but notably **not Il-18** — rescued the lethal/pathologic phenotype in the Dpp9 catalytically-inactive (S729A) mouse model, and asc knockout rescued survival of dpp9-knockout zebrafish. This provides strong preclinical rationale for **IL-1-pathway-targeted therapy** (anakinra, canakinumab, or NLRP1-inflammasome-directed agents as they become available) as a rational, mechanism-matched treatment strategy, even though clinical experience so far (single reported case) suggests anakinra alone may be insufficient once the hematologic phenotype has manifested — possibly because the dominant hematopoietic pathology in humans is **CARD8**-driven (IL-1-independent at the level of pyroptotic HSPC death) rather than purely NLRP1/IL-1-driven, per the 2026 mechanistic study. This is an important treatment-rationale nuance: **CARD8/caspase-1-targeted strategies, not only IL-1 blockade, may be needed to address the marrow-failure component**, since genetic CASP1 or CARD8 (but not NLRP1) deletion rescued HSPC survival in the human-relevant humanized mouse model (PMID:42427515).

**Advanced therapeutics:**
- **Hematopoietic stem cell transplantation (allogeneic HSCT):** the primary disease-modifying intervention reported to date, used in 3 of the first 4 published patients and in at least one additional reported case following anakinra failure. NCIT term: NCIT:C15431 (Hematopoietic Cell Transplantation).
- No gene therapy, gene editing, RNA-based therapy, or targeted small-molecule NLRP1/CARD8 inhibitor has been reported in HATIS patients to date (research-stage NLRP1/CARD8/caspase-1 inhibitors exist in the broader inflammasome field but are not reported as used in this specific disease).

**Supportive care:** Transfusion support (red cell/platelet, per the twin case report), management of recurrent infections (antimicrobial therapy for bacterial otitis/bronchitis, antiviral therapy for herpetic infections), and dermatologic management of eczema/atopic dermatitis (standard topical/systemic eczema management, not disease-specific).

**Experimental/clinical trials:** No disease-specific registered clinical trial (ClinicalTrials.gov NCT) was identified for HATIS in the searches performed in this session — expected given the extreme rarity of the condition; this should be explicitly re-checked at curation time via `just fetch-reference`/ClinicalTrials.gov search rather than assumed absent purely on the basis of this session's search results.

**Treatment outcomes:** Insufficient published data to characterize formal response rates; anakinra failure and progression to HSCT is described in at least one case.

**Treatment strategy / personalized medicine:** The emerging mechanistic distinction between NLRP1-driven skin/epithelial pathology (rescuable by IL-1 blockade in principle) and CARD8-driven, IL-1-independent HSPC pyroptosis (rescuable by CASP1/CARD8 inhibition, not by IL-1 blockade) suggests that future genotype- and mechanism-guided therapy may need to combine IL-1-pathway blockade (for cutaneous/systemic inflammation) with CARD8/caspase-1-targeted strategies or early HSCT (for marrow failure) — this is a reasoned mechanistic inference from the 2026 JCI paper's genetic-rescue data, not yet a clinically validated treatment algorithm, and should be labeled as such in any curated `mechanistic_hypotheses` block.

---

## 13. Prevention

**Primary prevention:** None available — this is a fully penetrant monogenic recessive disorder; primary prevention is limited to **genetic counseling and reproductive options** (carrier testing of parents/relatives in known-affected families, prenatal diagnosis, preimplantation genetic diagnosis) once a family's causal variant is known — standard practice for any newly delineated autosomal recessive Mendelian disorder, though not specifically reported as implemented for HATIS in the literature reviewed.

**Secondary prevention:** Early recognition (WES-based diagnosis) to enable timely consideration of HSCT before life-threatening cytopenia/infection develops appears to be the de facto secondary-prevention strategy emerging from the case pattern, though no formal screening program exists.

**Tertiary prevention:** Infection prophylaxis (e.g., antimicrobial prophylaxis, IVIG if indicated by humoral immune status) in patients with established pancytopenia/immunodeficiency — standard supportive practice for immunodeficient patients generally, not specifically validated for HATIS.

**Immunization:** Not specifically addressed in the literature reviewed; live vaccines would be expected to be contraindicated in the context of significant lymphopenia/immunodeficiency, following general primary-immunodeficiency vaccination principles, though this is an inference rather than a disease-specific published recommendation.

**Genetic counseling:** Recommended given autosomal recessive inheritance with 25% recurrence risk per pregnancy for parents of an affected child; consanguinity counseling relevant in at least 2 of the 3 founding families.

**Public health/environmental interventions:** Not applicable (not an environmentally modifiable disease).

---

## 14. Other Species / Natural Disease

**Naturally occurring disease in other species:** **None reported.** No spontaneous/naturally occurring DPP9-deficiency disease has been described in companion animals, livestock, or wildlife in the sources reviewed (no OMIA entry identified). All non-human DPP9-deficiency phenotypes described in the literature are **induced/engineered models** (see Section 15), not naturally occurring veterinary disease — this should be recorded as an explicit "no natural animal disease identified" rather than left silently blank.

**Orthologous gene:** Mouse *Dpp9* (MGI ortholog of human DPP9) is well characterized functionally; no OMIA or comparable veterinary-disease cross-reference exists.

**Zoonotic potential / cross-species susceptibility:** Not applicable — this is a monogenic host-genetic disorder, not an infectious/transmissible disease.

---

## 15. Model Organisms

**Mouse models (genetic, induced):**
- ***Dpp9* constitutive knockout mice:** Neonatal lethal due to a suckling defect related to migratory tongue muscle progenitor survival (PMID:24223149/PMC3819388 lineage of work; ScienceDirect developmental-biology paper on DPP9 enzyme activity and tongue muscle progenitors) — this model demonstrates an essential non-hematopoietic developmental role for DPP9 enzymatic activity distinct from the human hematologic phenotype, and **notably does not recapitulate human pancytopenia** ("Dpp9 mutant mice have normal hematopoiesis," per PMID:42427515), making this an instructive **human–model mismatch** for the bone-marrow-failure phenotype specifically.
- ***Dpp9*-S729A knock-in mice** (catalytically inactive DPP9, serine-to-alanine active-site point mutation): Homozygotes are born alive but die within 8–24 hours of birth (no weaned homozygotes recovered), modeling the catalytic-loss aspect of human disease. Genetic rescue experiments in this model directly established the NLRP1-dependence of lethality: **removal of a single copy of Nlrp1a/b/c, Asc, Gsdmd, or Il-1r (but not Il-18) rescued the lethal phenotype**, providing the foundational genetic evidence that NLRP1-inflammasome/IL-1 (not IL-18) signaling drives DPP9-deficiency pathology in this model (PMID:36112693).
- ***MISTRG6 humanized mice engrafted with human HSPCs*** (Xiao et al., PMID:42427515/JCI 10.1172/JCI207530, 2026): A **reverse-genetics human-relevant model** specifically constructed to address the mouse–human discrepancy in hematopoietic phenotype. In this model, DPP9 deletion in human HSPCs activated the **CARD8** inflammasome (a gene absent from the mouse genome), causing HSPC pyroptosis; **NLRP1 was dispensable for this cell death**, and **CARD8 or CASP1 deletion rescued cytopenia and HSPC survival, whereas NLRP1 deficiency did not**. This is the most direct and translationally important model to date, explaining why prior mouse models failed to recapitulate the defining human hematologic phenotype and providing a validated system for future therapeutic testing (e.g., of CARD8/caspase-1-directed agents).

**Zebrafish models:**
- ***dpp9* knockout zebrafish:** Recapitulate lethality; genetic knockout of ***asc*** (the inflammasome adaptor) rescues survival, corroborating the NLRP1(ASC)-dependence of pathology across two independent model systems (mouse and zebrafish) (PMID:36112693).

**Cellular/in vitro models:**
- **Patient-derived fibroblasts** (Western blot confirming absent DPP9 protein in the Gln851Ter homozygote — direct human cellular evidence of complete loss of function).
- **Patient-derived keratinocytes** (ex vivo demonstration of spontaneous NLRP1 inflammasome activation, directly linking the cutaneous phenotype to the proposed mechanism in human cells, not merely inferred from mouse skin).
- **Transfection-based studies** of the dominant-negative p.Arg252Pro variant (distinct disorder) quantifying reduced DPP9 protein stability (26–52% of wild-type).

**Model recapitulation summary (fidelity assessment for curation):**

| Model | Recapitulates | Fails to recapitulate / limitation |
|---|---|---|
| Constitutive *Dpp9*-KO mouse | Neonatal lethality (via tongue-muscle mechanism) | Normal hematopoiesis — does NOT model human pancytopenia (species-specific CARD8 absence) |
| *Dpp9*-S729A knock-in mouse | NLRP1/ASC/GSDMD/IL-1R-dependent lethality; genetic rescue logic | Still does not model human marrow-failure mechanism (no CARD8) |
| Zebrafish *dpp9*-KO | ASC-dependent lethality | Distant species; hematopoietic-specificity not the focus |
| MISTRG6 humanized mouse + human HSPCs | **CARD8-dependent human HSPC pyroptosis — the defining human hematologic mechanism** | Newest model (2026); long-term/whole-organism phenotype (skin, neurodevelopmental features) not addressed by this HSPC-focused system |
| Patient fibroblasts/keratinocytes | Direct human-cell confirmation of loss of function and NLRP1 activation | Ex vivo; does not model whole-organism disease course |

This table itself illustrates a textbook **HUMAN_MODEL_MISMATCH** knowledge-gap pattern (per this repository's curation conventions): standard mouse knockout/knock-in models systematically failed to explain the defining human hematologic phenotype for several years (2013 tongue-muscle paper through the 2022 Science Immunology paper) until species-specific CARD8 biology was directly tested in a humanized reverse-genetics system in 2026 — a prompt, explicit, and well-documented case of a mechanism resolved specifically because a model-organism limitation (mouse CARD8 absence) was identified and worked around, rather than silently extrapolated across species.

---

## Key Primary Sources (PMID-cited)

1. **Harapas CR, Robinson KS, Lay K, et al.** DPP9 deficiency: An inflammasomopathy that can be rescued by lowering NLRP1/IL-1 signaling. *Sci Immunol.* 2022 Sep 16;7(75):eabi4611. **PMID:36112693** — disease-defining founding paper (3 families, 4 patients; DPP9 variant characterization; mouse and zebrafish genetic rescue).
2. **Wolf C, Fischer H, Kühl JS, et al.** Hemophagocytic lymphohistiocytosis–like hyperinflammation due to a de novo mutation in DPP9. *J Allergy Clin Immunol.* 2023 Nov;152(5):1336–1344.e5. **PMID:37544411** — distinct dominant-negative monoallelic DPP9 disorder; important nosological contrast.
3. **Xiao T, Brewer JR, Carlino M, et al.** Reverse genetics in humanized mice reveals CARD8-mediated pyroptosis causing pancytopenia in human DPP9 deficiency. *J Clin Invest.* 2026;136(18). DOI:10.1172/JCI207530. **PMID:42427515** — mechanistic resolution of the human-specific CARD8/HSPC pyroptosis pathway; most recent and most directly mechanistic source.
4. **Singh S, Garg A, Mandal P.** Recurrent Transfusions and Severe Infections: Unmasking Hatipoglu Immunodeficiency Syndrome: Case Report and Review of Literature. *J Pediatr Hematol Oncol.* **PMID:41082409** — 2025 twin case report expanding the clinical/ancestral spectrum; DHR-test differential-diagnosis pitfall.
5. Structural/mechanistic background (NLRP1-FIIND-DPP9 ternary complex): "DPP9 sequesters the C terminus of NLRP1 to repress inflammasome activation," *Nature* 2021 — cite and verify exact PMID directly from Nature/PubMed at curation time before use as an evidence snippet, since this session identified the paper by title/journal via search but did not independently confirm its PMID through a direct abstract fetch.
6. OMIM #620331 (HATIS phenotype) and OMIM *608258 (DPP9 gene) — structured database entries for identifiers, clinical synopsis, and molecular genetics summary (content in this report was obtained via MedGen/search-engine mirrors of the OMIM clinical synopsis, since a direct OMIM.org fetch returned HTTP 403 in this session; **re-verify directly against OMIM at curation time**, as this report's OMIM-sourced content is a secondary reconstruction, not a direct-fetch primary read).

---

## Explicit Gaps and Caveats for Curation

- **No Orphanet, GeneReviews, or ICD-10/11 entry exists** — confirmed by direct search, not merely unfound.
- **Quantitative treatment-outcome and dosing details** (e.g., the anakinra 2–4 mg/kg/day figure) were obtained via AI-generated search-engine summaries rather than a direct primary-source fetch in this session and **must be re-verified against full-text primary literature** before being entered as a cited/quoted evidence item.
- **gnomAD allele frequencies** for the specific reported DPP9 variants were not independently verified in this session and should be looked up directly (per this repository's "never write an identifier/statistic from memory" discipline) before populating a `ClinVar`/`gnomAD`-sourced field.
- **No validated quality-of-life data** exist for this disease.
- **No population-level prevalence/incidence estimate** exists (fewer than 10 published patients); any curated `Prevalence` record should reflect `CASES_IN_LITERATURE`/`NOT_YET_DOCUMENTED`, not an invented number.
- The **exact PMID for the 2021 Nature DPP9–NLRP1 ternary-complex structural paper** was not independently confirmed via direct PubMed fetch in this session (only via secondary search-result titles) and should be confirmed before citation.
- The **neurodevelopmental/skeletal phenotype's mechanistic link to inflammasome dysregulation is unestablished** — flagged above as a candidate knowledge gap rather than asserted as inflammasome-driven.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
