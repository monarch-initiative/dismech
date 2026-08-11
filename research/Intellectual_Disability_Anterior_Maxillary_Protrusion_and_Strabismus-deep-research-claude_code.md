---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T20:17:45.851430'
end_time: '2026-07-31T20:22:14.132070'
duration_seconds: 268.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus
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
  - claude-sonnet-5
  web_search_requests: 14
  num_turns: 25
  total_cost_usd: 1.770607
  session_id: e4efd2b7-e9f4-5db9-9b8f-985a8acac525
  stop_reason: end_turn
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus** covering all of the
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

# Comprehensive Research Report: Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus (MRAMS Syndrome)

## Executive Summary

**MRAMS syndrome** — Impaired Intellectual Development, Anterior Maxillary Protrusion, and Strabismus — is an ultra-rare autosomal recessive Mendelian disorder caused by biallelic loss-of-function mutation in **SOBP** (Sine Oculis-Binding Protein homolog, HGNC:29256), a nuclear zinc-finger transcriptional co-factor on chromosome 6q21. It was described in a single large consanguineous Israeli-Arab kindred and is characterized by severe intellectual disability, a distinctive dentofacial phenotype (anterior/vertical maxillary excess, open bite, crowded teeth), strabismus, and mild sensorineural hearing loss. Mouse orthologs (*Sobp*/*Jxc1*) recapitulate deafness and vestibular circling behavior, and SOBP's biochemical role as a Six1/Eya1 transcriptional modulator links it mechanistically to the broader branchio-oto-renal (BOR) developmental gene network.

---

## 1. Disease Information

**Overview:** MRAMS syndrome is a rare genetic multiple-congenital-anomaly/dysmorphic syndrome combining severe intellectual disability with a specific craniofacial (dentomaxillary) anomaly and ocular misalignment. It was first delineated as a distinct nosologic entity by Basel-Vanagaite et al. (2007), who could find "no similar disorder in the literature" and proposed the acronym **MRAMS** (Mental Retardation, Anterior Maxillary protrusion, and Strabismus) (PMID: [17618476](https://pubmed.ncbi.nlm.nih.gov/17618476/)).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | [#613671](https://www.omim.org/entry/613671) — "Impaired Intellectual Development, Anterior Maxillary Protrusion, and Strabismus; MRAMS" |
| OMIM (gene) | [*613667](https://www.omim.org/entry/613667) — SOBP |
| MONDO | MONDO:0013353 |
| Orphanet | [ORPHA:562559](https://www.orpha.net/en/disease/detail/562559) — "Anterior maxillary protrusion-strabismus-intellectual disability syndrome" |
| MedGen | UID 462274, Concept ID **C3150924** |
| HGNC (gene) | HGNC:29256 (SOBP) |
| ICD-10/ICD-11 | No disease-specific code identified in the sources reviewed; as an ultra-rare congenital dysmorphic syndrome it would most likely be captured generically (e.g., under "other specified congenital malformation syndromes" categories) rather than by a dedicated rare-disease code — this is an inference, not a sourced code, and should be verified against the current ICD-11 rare-disease linearization before use. |

**Synonyms:** MRAMS syndrome; Mental retardation, anterior maxillary protrusion, and strabismus syndrome; Anterior maxillary protrusion, strabismus, intellectual disability syndrome.

**Evidence basis:** All clinical data derive from a single published aggregated case series (7 affected siblings within one extended consanguineous family), not from EHR-scale or population registries — this is a disease-level literature report, not an aggregated epidemiological resource.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. MRAMS is caused by **homozygous truncating mutation in SOBP** (Sine Oculis-Binding Protein homolog), identified by Birk et al. (2010): a c.1981C>T transition in exon 6, producing a premature stop codon at arginine residue 661 (**p.Arg661Ter / R661X**), truncating the last 212 amino acids of the 873-residue protein (PMID: [21035105](https://pubmed.ncbi.nlm.nih.gov/21035105/)).

> "We report on the identification of a truncating mutation in the SOBP that is responsible for causing both syndromic and nonsyndromic ID in the same family." — Birk et al., 2010

**Genetic risk factors:**
- **Causal variant:** SOBP c.1981C>T (p.R661X), homozygous, autosomal recessive.
- **Consanguinity** is the dominant risk factor identified: the proband family's parents were first cousins of Israeli-Arab descent; 7 of 11 children were affected.
- No modifier genes have been reported. Linkage analysis by Birk et al. (2010) **excluded** the SOBP locus in 22 additional unrelated families with syndromic intellectual disability, indicating SOBP mutations are not a common cause of similar phenotypes — this strongly implies extreme allelic/locus rarity rather than a recurrent mutational hotspot.

**Environmental risk factors:** None identified or applicable — MRAMS is a monogenic Mendelian disorder with no reported environmental or exposure-related contribution.

**Protective factors:** None reported (not applicable to a fully penetrant recessive truncating-null genotype in this pedigree).

**Gene-environment interactions:** None described; no evidence of environmental modulation of expressivity in the literature reviewed.

---

## 3. Phenotypes

Data are drawn from the original description of 7 affected siblings (Basel-Vanagaite et al., 2007) plus later re-analysis of the same kindred (Birk et al., 2010).

| Phenotype | Type | Frequency in reported cohort | Suggested ontology term |
|---|---|---|---|
| Severe intellectual disability | Cognitive | 7/7 (100%) | HP:0010864 (Severe intellectual disability) / HP:0001249 (Intellectual disability, general) |
| Anterior maxillary protrusion with vertical maxillary excess | Craniofacial/skeletal | 6/7 (86%) | No exact-match HP term confirmed in this research pass — candidates include HP:0000303-adjacent maxillary-prominence terms; **verify exact HP ID via OAK before curating** rather than assume |
| Open bite | Dental | 6/7 | HP:0010938 (Open bite) — verify label |
| Dental crowding / prominent teeth | Dental | 6/7 | HP:0000678 (Dental crowding) — verify label |
| Strabismus | Ophthalmologic | 7/7 (100%) | HP:0000486 (Strabismus) |
| Esotropia (reported form of strabismus) | Ophthalmologic | subset | HP:0000565 (Esotropia) |
| Mild cochlear/sensorineural hearing loss | Auditory | Reported in "addition" in a subset | HP:0000407 (Sensorineural hearing loss) |
| Global developmental delay | Cognitive/behavioral | Presumed universal | HP:0001263 (Global developmental delay) |
| Speech/language delay | Behavioral | Reported | HP:0000750 (Delayed speech and language development) |
| Temporal lobe epilepsy | Neurological | 1/7 — in the single sib **without** the dentofacial phenotype | HP:0007334 (Temporal lobe epileptic focus) — verify |
| Psychosis | Behavioral/psychiatric | 1/7, described as "severe psychosis" developing in adolescence, in the same non-dysmorphic sib | HP:0000709 (Psychosis) |

**Onset/course:** Congenital/early-childhood onset of intellectual disability and craniofacial features; the psychosis/epilepsy in the atypical sib was reported to emerge in **adolescence**, suggesting a distinct temporal trajectory possibly reflecting non-allelic or modified expression.

**Important phenotypic heterogeneity noted by the authors:**
> "The child with MR but without a jaw anomaly was somewhat less severely retarded, had seizures and severe psychosis, which may point to his having a separate disorder." — Basel-Vanagaite et al., 2007

Birk et al. (2010) later showed this same individual **does** carry the SOBP truncating mutation, reframing this presentation as an allelic **nonsyndromic** ID phenotype rather than a separate disorder — i.e., SOBP mutation in this family produces both a syndromic (dysmorphic) and a nonsyndromic (epilepsy/psychosis, no dysmorphism) presentation.

**Diagnostic exclusions performed in the original workup** (informative negatives): normal brain MRI, normal standard karyotype, fragile X excluded, no subtelomeric rearrangements detected, random X-inactivation in the carrier mother (arguing against an X-linked mechanism before the AR/SOBP etiology was established).

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36 data identified); qualitatively, severe ID plus visual (strabismus/amblyopia risk) and mild hearing impairment would be expected to substantially affect adaptive functioning, communication, and educational needs, consistent with general severe-ID QoL literature, though disease-specific QoL data do not exist.

---

## 4. Genetic/Molecular Information

**Causal gene:** **SOBP** (OMIM *613667; HGNC:29256), chromosome **6q21**, ~171 kb genomic span (hg-coordinates approx. 107,490,106–107,661,306). Alias: **JXC1** (Jackson circler protein 1, from its original identification via the mouse *jc* mutant).

**Gene structure:** 7 exons in human (first 6 comprise the coding sequence); mRNA of 2,622 nt encodes an **873-amino-acid** nuclear protein.

**Protein domain architecture (from GeneCards/Wikipedia synthesis and Birk et al. 2010):**
- N-terminal nuclear localization signal (NLS)
- Two **FCS-type (MYM-type) zinc-finger** motifs
- A proline-rich region (PR1)
- A putative RNA-binding motif region
- A C-terminal NLS embedded within a second proline-rich motif (PR2)
- GeneCards additionally notes reported SUMO1/SUMO2 interaction ("SUMO polymer binding" GO annotation)

**Pathogenic variant identified:**
- **c.1981C>T, p.R661X** — homozygous nonsense/truncating variant, exon 6, removing the C-terminal ~212 residues (including part of the C-terminal NLS/PR2 region). Classification consistent with pathogenic per loss-of-function mechanism in an autosomal recessive disorder (formal ACMG/ClinVar classification not located in sources reviewed — recommend independent ClinVar/VarSome lookup before final curation).
- **Variant type:** Nonsense (stop-gain).
- **Origin:** Germline, homozygous, segregating with disease in a consanguineous pedigree.
- **Functional consequence:** Loss-of-function via C-terminal truncation; per Tavares et al. (2021), the truncated R661X protein **retains** Six1-binding capacity, suggesting the pathogenic mechanism may be partial/hypomorphic rather than complete null, and may specifically disrupt only C-terminal-dependent functions (PMID: [34414417](https://pubmed.ncbi.nlm.nih.gov/34414417/)).
- **Allele frequency:** Not reported in population databases (gnomAD/ExAC) in the sources reviewed — consistent with a private/founder variant in a single consanguineous kindred rather than a recurrent population variant; should be checked directly in gnomAD for completeness.

**Modifier genes:** None identified.

**Epigenetic information:** No DNA methylation/histone modification data specific to SOBP-related disease were identified in this search.

**Chromosomal abnormalities:** None — standard karyotype was normal in the original family; this is a single-gene sequence-variant disorder, not a copy-number/structural disorder.

---

## 5. Environmental Information

No environmental, toxin, lifestyle, or infectious contributory factors have been reported for MRAMS syndrome; it is described exclusively as a Mendelian autosomal recessive disorder arising from a single-gene defect. Not applicable.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway / protein function:**
SOBP functions as a **nuclear transcriptional co-factor** that modulates the **SIX1–EYA1** transcriptional complex, a core regulatory node of the pre-placodal ectoderm/otic-vesicle developmental network (the same network implicated in branchio-oto-renal, BOR, spectrum disorders). Tavares et al. (2021) demonstrated:

> "Sobp binds to and colocalizes with Six1 in the cell nucleus" and "significantly interferes with transcriptional activation of Six1+Eya1 target genes through competitive binding mechanisms," acting as "a transcriptional co-repressor that competes with Eya1 for Six1 binding in a dose-dependent manner." (PMID: [34414417](https://pubmed.ncbi.nlm.nih.gov/34414417/))

**Causal chain (proposed, integrating human and mouse data):**
1. **Trigger:** Biallelic SOBP loss-of-function/truncating mutation (molecular scale)
2. **Molecular dysregulation:** Altered SOBP-mediated modulation of SIX1/EYA1 transcriptional output in developing neuroectodermal and otic/craniofacial tissues (molecular scale)
3. **Cellular consequence — CNS:** Disrupted gene expression programs during **synaptogenesis** in limbic-system neurons (cellular scale)
4. **Cellular consequence — craniofacial:** Disrupted patterning of neural-crest-derived cranial cartilage elements (Meckel's/ceratohyal cartilages, branchial arch cartilages) in the zebrafish/mouse craniofacial model (cellular/tissue scale)
5. **Cellular consequence — inner ear:** Disrupted cochlear growth, hair-cell fate specification, and patterning of the organ of Corti (tissue scale)
6. **Organism-level phenotype:** Severe intellectual disability, anterior maxillary protrusion/dentofacial anomaly, strabismus, mild sensorineural hearing loss (organism scale)

**Cellular processes / brain expression:** In situ studies in postnatal mouse brain show:
> "Strong expression in the cortex, especially in layer V, the hippocampus, the piriform cortex, the mediodorsal nucleus of the thalamus, the anterior olfactory nucleus, and the mitral cell layer in the olfactory bulb" — i.e., **limbic system** structures — "at the time interval of active synaptogenesis" (Birk et al., 2010, PMID: 21035105).

This expression pattern is the proposed mechanistic link between SOBP disruption and cognitive/behavioral phenotypes (intellectual disability, and in the nonsyndromic sib, temporal lobe epilepsy and psychosis — both classically limbic-system-associated).

**Inner ear mechanism (mouse model data, Kikkawa et al.):** The vertebrate *Sobp*/*Jxc1* ortholog was originally identified via positional cloning of the spontaneous mouse *Jackson circler (jc)* mutation:
> "Jxc1/Sobp, Encoding a Nuclear Zinc Finger Protein, Is Critical for Cochlear Growth, Cell Fate, and Patterning of the Organ of Corti" — cellular patterning of the organ of Corti is severely disrupted in *jc* mutants, with supernumerary hair cells, mirror-image duplications of the tunnel of Corti and inner hair cells, and ectopic vestibular-like hair cells in Kölliker's organ (PMC2556235, *Journal of Neuroscience* 2008).

**Craniofacial mechanism:** Tavares et al. (2021) showed loss or overexpression of *Sobp* in model systems caused:
> "severe cranial cartilage defects" including "deformed Meckel's and ceratohyal cartilages, hypoplastic branchial arch cartilages, and absent otic capsules" — providing a direct mechanistic bridge to the human dentofacial (maxillary) phenotype via disrupted neural-crest/pre-placodal patterning.

**Suggested GO terms:**
- GO:0007605 (sensory perception of sound)
- GO:0009952 (anterior/posterior pattern specification) / craniofacial developmental process terms
- GO:0007416 (synapse assembly) / GO:0050808 (synapse organization) — relevant to the synaptogenesis-timed limbic expression
- GO:0003713 (transcription coactivator activity) / GO:0003714 (transcription corepressor activity) — for the Six1/Eya1 modulatory role

**Suggested CL terms:**
- CL:0000101 / specific inner-ear hair cell types (organ of Corti hair cells)
- CL:0000540 (neuron) — cortical layer V pyramidal neurons, hippocampal neurons
- Neural crest cell (CL:0000333) — for the craniofacial mechanism

**Protein dysfunction:** C-terminal truncation (loss of ~212 residues including part of the C-terminal NLS/proline-rich region) — a partial loss-of-function/hypomorphic mechanism, since Six1-binding is retained per Tavares et al.

**Immune system involvement:** None reported/applicable.

**Metabolic changes, transcriptomics/proteomics/single-cell data:** No disease-specific human -omics datasets were located; the available molecular data derive from candidate-gene Sanger sequencing (Birk et al., 2010) and mouse/zebrafish developmental-biology studies (Kikkawa et al.; Tavares et al.), not from large-scale human profiling.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (limbic system — cortex, hippocampus, piriform cortex, thalamus, olfactory system); craniofacial skeleton (maxilla); eyes (extraocular muscle balance); inner ear (cochlea, vestibular apparatus)
- **Body systems:** Nervous system, musculoskeletal/craniofacial system, ophthalmologic/visual system, auditory-vestibular system

**Tissue/cell level:**
- Neural crest-derived craniofacial cartilage and bone (maxilla)
- Cortical layer V neurons, hippocampal neurons, piriform cortical neurons (CNS)
- Cochlear hair cells and supporting cells, spiral ganglion neurons, vestibular sensory epithelium (inner ear)
- Extraocular muscles/oculomotor control circuitry (strabismus)

**Subcellular level:** Nucleus (SOBP is a nuclear protein; GO Cellular Component: nucleus, nuclear body) — consistent with its role as a transcriptional modulator.

**Suggested UBERON terms:**
- UBERON:0002240 (spinal cord) — not directly relevant; more relevant:
- UBERON:0002316 (hippocampal formation)
- UBERON:0002012 (piriform cortex)
- UBERON:0002420 (maxilla)
- UBERON:0000982 (organ of Corti) / UBERON:0001846 (cochlea)
- UBERON:0000970 (eye) / extraocular muscle structures

**Lateralization:** Not specifically reported; craniofacial and cochlear findings described as generally bilateral/symmetric in the mouse models; strabismus type not consistently specified as unilateral vs. bilateral in the human report.

---

## 8. Temporal Development

- **Onset:** Congenital/early childhood — intellectual disability and dentofacial features are apparent from early development; the atypical sib's seizures and psychosis emerged specifically in **adolescence**.
- **Onset pattern:** Insidious/developmental for the core ID and craniofacial phenotype; the psychiatric/seizure presentation in the one sib appears more subacute-onset in adolescence.
- **Progression:** Static/stable intellectual disability is typical of this class of Mendelian neurodevelopmental disorder (as opposed to a progressive neurodegenerative course) — this is inferred from the general "syndromic ID" framing rather than explicitly stated longitudinal follow-up data, since no long-term natural history study was located.
- **Disease course/duration:** Chronic, lifelong (both the ID and the craniofacial anomaly are structural/developmental, not remitting).
- **Remission:** Not applicable — no evidence for spontaneous remission of the core phenotype; psychosis/seizures in the atypical individual would follow standard chronic psychiatric/epilepsy management courses, but disease-specific outcome data were not located.
- **Critical periods:** The proposed mechanistic critical window is **active synaptogenesis** in postnatal limbic circuitry (per the mouse expression-timing data), suggesting this developmental window is mechanistically central to the neurocognitive phenotype, though this has not been translated into a defined human intervention window.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal recessive**, confirmed via consanguinity, homozygosity for the R661X SOBP variant, and segregation in the pedigree.
- **Penetrance:** Appears complete/high in the reported homozygotes, though only one family has ever been reported, limiting generalizability.
- **Expressivity:** **Variable** — the same homozygous genotype produced both the "syndromic" (dysmorphic, dentofacial + strabismus) phenotype in 6 sibs and a distinct "nonsyndromic" (no dysmorphism, but epilepsy + psychosis) phenotype in the 7th sib, a striking example of intrafamilial phenotypic variability at a single locus.
- **Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effect:** The single reported family is of **Israeli-Arab** descent with parental consanguinity (first-cousin marriage); whether R661X represents a population founder allele beyond this kindred is unknown — no other families have been reported, and Birk et al. explicitly excluded the SOBP locus in 22 other syndromic-ID families, arguing against broad recurrence.
- **Consanguinity:** Central to the disease's emergence in this pedigree — first-cousin parents.
- **Carrier frequency:** Not established in any population database.

**Epidemiology:**
- **Prevalence:** Extremely rare — to date, the disease has been described in **only one extended family** (7 affected individuals among 11 siblings). No prevalence estimate (cases per 100,000) exists; this is an ultra-rare/"cases in literature" tier disorder.
- **Incidence:** Not calculable from available data.
- **Affected populations:** Only the original Israeli-Arab consanguineous kindred has been reported.
- **Geographic distribution:** Israel (single reported kindred); no other geographic clusters reported.
- **Sex ratio:** Of the 7 affected sibs, **5 were female, 2 were male** — though with such a small n, this is not interpretable as a true population sex-ratio signal, and autosomal recessive inheritance predicts equal sex distribution in principle.

---

## 10. Diagnostics

**Clinical tests performed in the index family (all with normal/negative results, used to exclude alternative diagnoses):**
- Brain MRI — normal
- Standard cytogenetic karyotyping — normal
- Fragile X testing — excluded
- Subtelomeric rearrangement screening — negative
- X-inactivation studies in the carrier mother — random (arguing against skewed X-inactivation/X-linked mechanisms)
- Biochemical/metabolic workup — normal (specific assays not detailed in sources reviewed)

**Genetic testing:**
- **Diagnostic confirmation** is via identification of biallelic (homozygous or compound heterozygous) loss-of-function variants in **SOBP** — originally by Sanger sequencing/candidate-gene approach following linkage mapping; today this would be expected via **exome sequencing (WES)** or a **targeted ID gene panel** including SOBP.
- **Chromosomal microarray (CMA)/karyotype:** Useful for excluding chromosomal etiologies (as done in the original workup) but not diagnostic for this single-gene disorder.
- No SOBP-specific commercial single-gene test information beyond general genetic-testing-registry style listings was identified as authoritative in this pass (a "SOBP Gene ... NGS Genetic Test" listing appeared in search results from a commercial diagnostics lab site, but this is a vendor listing rather than a primary clinical-validity source and should not be cited as an evidence-based recommendation).

**Clinical criteria:** No formal consensus diagnostic criteria (DSM/ICD-style) exist; diagnosis rests on the combination of (a) severe ID, (b) anterior maxillary protrusion/dentofacial anomaly, (c) strabismus ± mild hearing loss, in the context of consanguinity, confirmed by SOBP molecular testing.

**Differential diagnosis:** Given the overlapping SOBP–SIX1/EYA1 mechanistic link, **branchio-oto-renal (BOR) spectrum disorders** (caused by SIX1/EYA1 mutations) are a biologically relevant differential/related mechanism to consider (per Tavares et al. 2021), though BOR's renal and branchial-cleft features are not part of the MRAMS clinical description. Other syndromic intellectual disability disorders with maxillary/dental anomalies and strabismus should also be considered and excluded by the workup pattern used in the index family (chromosomal, fragile X, subtelomeric, metabolic).

**Screening:** No population or newborn screening program exists for this ultra-rare disorder; in consanguineous families with a known SOBP variant, **carrier testing and prenatal/preimplantation genetic testing** would be the applicable reproductive-risk-reduction approach, though this is inferred from general practice for AR single-gene disorders rather than sourced to a MRAMS-specific guideline.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality data reported; the disorder does not appear to be associated with reduced lifespan based on available reports (a chronic neurodevelopmental/dysmorphic syndrome rather than a progressive or lethal condition).
- **Morbidity/function:** Defined by severe intellectual disability (lifelong significant adaptive-functioning impairment), visual morbidity from strabismus (risk of amblyopia if untreated), and mild hearing impairment. The atypical sib's temporal lobe epilepsy and psychosis represent additional, potentially more impairing morbidity in that specific allelic presentation.
- **Complications:** Amblyopia risk from untreated strabismus; malocclusion-related dental/functional complications from the maxillary anomaly; psychiatric/seizure complications in the nonsyndromic presentation.
- **Recovery potential:** The core ID and craniofacial anomaly are structural/developmental and not expected to remit; symptomatic interventions (orthodontic/surgical, strabismus surgery, hearing amplification, seizure control, psychiatric treatment) can improve function but do not reverse the underlying condition.
- **Prognostic factors:** The presence vs. absence of the dentofacial dysmorphism appears to correlate with a different clinical trajectory within the same family (dysmorphic sibs had more severe ID without epilepsy/psychosis; the non-dysmorphic sib had somewhat less severe ID but developed epilepsy and severe adolescent-onset psychosis) — suggesting phenotypic heterogeneity may itself carry prognostic information, though this is based on an n of 1 for the atypical presentation and cannot be generalized.

---

## 12. Treatment

No disease-specific curative or targeted pharmacotherapy exists for MRAMS syndrome; management is **symptomatic and multidisciplinary**, inferred from standard management of the component phenotypes (no MRAMS-specific treatment trial or guideline was identified):

| Intervention | Target phenotype | Suggested NCIT term |
|---|---|---|
| Orthodontic/orthognathic surgical correction | Anterior maxillary protrusion, open bite | NCIT:C15329 (Surgical Procedure) / NCIT:C16186 (Orthopedic Surgical Procedure, if applicable) |
| Strabismus surgery / vision therapy | Strabismus, amblyopia prevention | NCIT:C15329 (Surgical Procedure) |
| Hearing amplification (hearing aids) | Mild sensorineural hearing loss | No exact NCIT device-usage term available (per the dismech project's own documented gap — device usage lacks a clean NCIT clinical-action term) |
| Special education / early intervention / rehabilitative therapy | Intellectual disability, developmental delay | NCIT:C15315 (Rehabilitation) |
| Speech-language therapy | Speech/language delay | NCIT:C159273 (Speech Therapy) |
| Antiepileptic pharmacotherapy | Temporal lobe epilepsy (atypical sib) | NCIT:C15986 (Pharmacotherapy) |
| Antipsychotic pharmacotherapy | Psychosis (atypical sib) | NCIT:C15986 (Pharmacotherapy) |
| Genetic counseling | Family planning / recurrence risk | NCIT:C15240 (Genetic Counseling) |

**Experimental treatments:** None identified; no MRAMS-specific clinical trials were found on searches of the available literature.

**Pharmacogenomics:** Not applicable/no data.

**Treatment outcomes:** No systematic outcome data (response rates, adverse events) specific to MRAMS management were identified — all inferred from general standard-of-care for the component phenotypes.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (a fully genetic AR disorder); the only actionable "primary prevention" lever is **genetic/reproductive counseling** in consanguineous families with a known carrier status, informing reproductive decision-making (carrier testing, prenatal diagnosis, preimplantation genetic testing) — standard practice for AR disorders, not MRAMS-specific literature.
- **Secondary prevention:** Early ophthalmologic screening/intervention for strabismus to prevent amblyopia; early audiologic screening for hearing loss; early developmental screening to initiate ID-related early intervention services.
- **Tertiary prevention:** Ongoing multidisciplinary management (dental/orthodontic, ophthalmologic, audiologic, neurodevelopmental, psychiatric as needed) to minimize functional complications.
- **Genetic counseling:** Directly relevant given the autosomal recessive inheritance and consanguinity in the index family — 25% recurrence risk per pregnancy for carrier couples.
- **Immunization, public health, prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

No naturally occurring MRAMS-like disease has been reported in non-human species. However, the causal gene has well-characterized **induced/spontaneous laboratory mouse models** (see Section 15) rather than natural veterinary disease. No OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case series was identified for SOBP-associated disease.

**Orthologous gene:** Mouse *Sobp* (a.k.a. *Jxc1*), MGI:1924427, chromosome 10 (cytogenetic band 10qB2), ~172 kb, 864-amino-acid protein — high conservation of domain structure (NLS, FCS-zinc fingers, proline-rich regions) with human SOBP.

**Comparative pathology:** The mouse cochlear/vestibular phenotype (see below) is considered a reasonable model for the human mild hearing-loss component but does **not** recapitulate the craniofacial (maxillary) or cognitive/behavioral phenotype in a directly comparable way — this represents a **human-model mismatch** worth flagging for any curated entry (i.e., mouse data strongly support the auditory-vestibular mechanism but translational fidelity to the human dentofacial and cognitive phenotype is comparatively less direct, since it is the zebrafish/mouse craniofacial-cartilage work of Tavares et al., not the *jc*/*jc2J* mouse itself, that addresses the craniofacial mechanism).

**Zoonotic potential/transmission:** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

**Mouse models (genetic, spontaneous):**

1. **Jackson circler (*jc*) mouse** — spontaneous recessive mutation, **10-bp deletion in exon 6** of *Sobp*, causing a frameshift and premature stop codon at residue 490. Phenotype: profound deafness, erratic circling (vestibular) behavior, and severe disruption of organ of Corti patterning — supernumerary outer hair cells, duplicated tunnel of Corti, ectopic vestibular-like hair cells in Kölliker's organ, and smaller/thicker vestibular end organs (Kikkawa et al., *Journal of Neuroscience* 2008, PMC2556235; related earlier positional-cloning work in *Human Molecular Genetics*/associated cochlear-development literature). Strain resource: Jackson Laboratory strain [000563](https://www.jax.org/strain/000563).
   > "Jxc1/Sobp, Encoding a Nuclear Zinc Finger Protein, Is Critical for Cochlear Growth, Cell Fate, and Patterning of the Organ of Corti"

2. **jc2J allele** — independent spontaneous nonsense mutation, **c.1894G>T**, creating a premature stop codon at residue 632 — phenotypically similar deafness/circling.

**Model characteristics:**
- **Phenotype recapitulation:** Excellent for the auditory-vestibular component (deafness, cochlear/organ-of-Corti dysmorphogenesis) — directly informative for the human "mild cochlear hearing loss" feature, though the mouse phenotype (profound deafness) is considerably more severe than the human "mild" hearing loss, an important severity mismatch to note.
- **Model limitations:** Does not, by itself, model the human intellectual disability, craniofacial (maxillary), or ocular (strabismus) phenotypes; those are informed instead by expression-pattern data (limbic system in postnatal mouse brain) and by separate craniofacial-development models (zebrafish/mouse *Sobp*-Six1 work by Tavares et al., 2021) rather than by the *jc*/*jc2J* deafness-circling model directly.

**Applications:** The *jc*/*jc2J* models are used to study cochlear developmental biology and hair-cell fate specification; the Tavares et al. craniofacial model system is used to study Six1/Eya1-dependent neural crest and pre-placodal ectoderm patterning relevant to both BOR spectrum disorders and the MRAMS dentofacial phenotype.

**Resources:** MGI:1924427 (mouse *Sobp* gene page); JAX strain 000563 (Jackson circler).

---

## Summary of Key Citations

1. Basel-Vanagaite L, Rainshtein L, Inbar D, Gothelf D, Hennekam R, Straussberg R. "Autosomal recessive mental retardation syndrome with anterior maxillary protrusion and strabismus: MRAMS syndrome." *Am J Med Genet A.* 2007;143A(15):1687-91. PMID: [17618476](https://pubmed.ncbi.nlm.nih.gov/17618476/).
2. Birk E, et al. "SOBP is mutated in syndromic and nonsyndromic intellectual disability and is highly expressed in the brain limbic system." *Am J Hum Genet.* 2010;87(5):694-700. PMID: [21035105](https://pubmed.ncbi.nlm.nih.gov/21035105/). DOI: 10.1016/j.ajhg.2010.10.005.
3. Kikkawa Y, et al. "Jxc1/Sobp, Encoding a Nuclear Zinc Finger Protein, Is Critical for Cochlear Growth, Cell Fate, and Patterning of the Organ of Corti." *J Neurosci.* 2008;28(26):6633. PMC2556235.
4. Tavares ALP, et al. "Sobp modulates the transcriptional activation of Six1 target genes and is required during craniofacial development." *Development.* 2021;148(17):dev199684. PMID: [34414417](https://pubmed.ncbi.nlm.nih.gov/34414417/).
5. OMIM #613671 — [Impaired Intellectual Development, Anterior Maxillary Protrusion, and Strabismus; MRAMS](https://www.omim.org/entry/613671).
6. OMIM *613667 — [Sine Oculis-Binding Protein Homolog; SOBP](https://www.omim.org/entry/613667).
7. [MedGen C3150924](https://www.ncbi.nlm.nih.gov/medgen/?term=OMIM:613671).
8. [Orphanet ORPHA:562559](https://www.orpha.net/en/disease/detail/562559).
9. [GARD/GeneReviews summary — Intellectual disability, anterior maxillary protrusion, and strabismus](https://rarediseases.info.nih.gov/diseases/17997/intellectual-disability-anterior-maxillary-protrusion-and-strabismus).
10. [SOBP — Wikipedia](https://en.wikipedia.org/wiki/SOBP).

**Notes on evidence gaps (explicit, per curation discipline):** This is a single-family, single-publication-lineage disorder. No independent replication family has been reported; no population prevalence, gnomAD allele frequency, natural-history/longitudinal study, disease-specific QoL instrument, clinical trial, or ICD-11 code was located. Several candidate ontology term IDs above (particularly for "anterior maxillary protrusion," "open bite," "dental crowding," and "temporal lobe epilepsy") could not be confirmed with certainty via the searches performed in this pass and **must be verified against the authoritative HPO/OAK lookup** before being committed to any curated knowledge base entry, consistent with this project's anti-hallucination review standard.