---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:47:04.650977'
end_time: '2026-07-30T23:52:36.480911'
duration_seconds: 331.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holoprosencephaly 9
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
  web_search_requests: 18
  num_turns: 27
  total_cost_usd: 1.9880150000000003
  session_id: 93c49f8d-8819-5fa4-9933-c530cfae996c
  stop_reason: end_turn
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Holoprosencephaly 9
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Holoprosencephaly 9** covering all of the
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

# Holoprosencephaly 9 (HPE9, GLI2-Related Holoprosencephaly): Comprehensive Research Report

## 1. Disease Information

**Overview:** Holoprosencephaly 9 (HPE9) is one of the numbered genetic subtypes of holoprosencephaly (HPE), the most common structural malformation of the developing forebrain in humans, caused by heterozygous mutations in **GLI2** (GLI-Kruppel family member 2), a zinc-finger transcription factor that mediates Sonic Hedgehog (SHH) signaling. HPE9 is defined by a **wide phenotypic spectrum** — from frank forebrain non-cleavage (classic HPE) at the severe end, to an entirely distinct, more common presentation of **pituitary anomalies, postaxial polydactyly, and subtle midfacial features without any brain cleavage defect** at the milder end [OMIM #610829](https://omim.org/entry/610829); [PMID:14581620](https://pubmed.ncbi.nlm.nih.gov/14581620/). Because of this, the field has moved toward viewing GLI2 pathogenic variants as causing a **phenotype distinct from classic HPE** rather than "true" holoprosencephaly in most patients — GeneReviews notes GLI2 variants more often produce "pituitary anomalies, polydactyly, and subtle facial features (sometimes similar to HPE facial features)" than overt HPE ([GeneReviews: Holoprosencephaly Overview, NBK1530](https://www.ncbi.nlm.nih.gov/books/NBK1530/)). The milder, non-HPE end of the spectrum is now separately cataloged as **Culler-Jones syndrome (CJS; OMIM #615849)** — postaxial polydactyly–anterior pituitary anomalies–facial dysmorphism syndrome — caused by the same gene.

**Key identifiers:**
- **OMIM:** #610829 (HPE9, phenotype); *165230 (GLI2, gene)
- **Related OMIM phenotype:** #615849 (Culler-Jones syndrome, allelic disorder)
- **Gene:** GLI2, HGNC:4318, chromosome 2q14.2, NCBI Gene ID 2735/2736 region
- **MONDO:** A MONDO term for "holoprosencephaly 9" exists (indexed by NORD's Mondo-disease pages and ClinVar cross-references) but the exact MONDO CURIE could not be independently confirmed via the search tools used in this session — verify locally with an OAK lookup (e.g., `runoak -i sqlite:obo:mondo search "holoprosencephaly 9"`) before use in curation.
- **Orphanet:** HPE is cataloged generally as ORPHA:2162 (Holoprosencephaly); GLI2-specific HPE9 subtype entries exist in Orphanet's gene-disease association tables.
- **ICD-10:** Q04.2 (Holoprosencephaly, general code; no HPE9-specific ICD-10/11 code exists)
- **Inheritance database cross-refs:** ClinVar aggregates GLI2 variants under "Holoprosencephaly 9" (e.g., [RCV000030728](https://www.ncbi.nlm.nih.gov/clinvar/RCV000030728/)).

**Synonyms:** HPE9; GLI2-related holoprosencephaly; Holoprosencephaly, GLI2-associated; (allelic, milder disorder) Culler-Jones syndrome; postaxial polydactyly–anterior pituitary anomalies–facial dysmorphism syndrome.

**Evidence basis:** Information is derived predominantly from **aggregated case-series/cohort resources** (OMIM, Orphanet, GeneReviews, ClinVar) built from published human case reports and cohort studies (not raw EHR data). The largest primary literature sources are multi-family cohort papers (e.g., Roessler et al. 2003, Bertolacini et al. 2012, Corder et al. 2022) rather than large-scale registries, reflecting HPE9's rarity.

---

## 2. Etiology

**Disease causal factors — genetic:** HPE9 is caused by **heterozygous, typically loss-of-function, mutations in GLI2** (chromosome 2q14.2), a primary transcriptional effector of SHH signaling in the developing forebrain, face, and pituitary. Roessler et al. (2003) first established the disease-gene link, reporting "loss-of-function mutations in the human GLI2 gene are associated with a distinctive phenotype (within the HPE spectrum)... characterized by defective anterior pituitary formation and pan-hypopituitarism, with or without overt forebrain cleavage abnormalities, and HPE-like midfacial hypoplasia" [PMID:14581620](https://pubmed.ncbi.nlm.nih.gov/14581620/), PNAS 100(23):13424-13429, 2003.

Mutation spectrum includes nonsense, frameshift, splice-site, and missense variants, as well as **contiguous gene deletions** encompassing GLI2 (e.g., a 1.3 Mb 2q14 deletion producing a mild HPE-spectrum phenotype with heterotaxy, [PMID:22106008](https://pubmed.ncbi.nlm.nih.gov/22106008/)). Truncating variants that remove the C-terminal transcriptional activator domain are the best-characterized loss-of-function class and are more strongly associated with pituitary anomalies and polydactyly than missense/zinc-finger variants ([Corder et al. 2022, AJMG-A](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62611), "Truncating and zinc-finger variants in GLI2 are associated with hypopituitarism").

**Relative contribution among HPE genes:** The four major HPE genes (SHH, ZIC2, SIX3, TGIF1) together account for point mutations/microrearrangements in ~27% of isolated HPE cases (SHH ~12%, ZIC2 ~9%, SIX3 ~5%, TGIF1 ~1%). GLI2 and PTCH1 are "minor" genes, individually contributing <1% of classic HPE, though GLI2 is disproportionately represented among patients ascertained for the **pituitary-anomaly/polydactyly phenotype** rather than classic HPE — in one screened cohort of ~400 individuals with HPE-spectrum features, roughly 28% carried a GLI2 variant of some kind (most benign/uncertain significance; a minority pathogenic) ([Bertolacini et al. 2012, PMID:21204792](https://pubmed.ncbi.nlm.nih.gov/21204792/)).

**Genetic risk factors:**
- Heterozygous pathogenic/likely pathogenic GLI2 variants (nonsense, frameshift, splice, deletion; some missense in zinc-finger or activator domains)
- De novo occurrence in many probands, but **familial transmission with incomplete penetrance is common** — a hallmark of GLI2-HPE
- No established polygenic/susceptibility-locus modifiers specific to GLI2-HPE beyond the general HPE genetic-modifier literature (e.g., variants in other SHH-pathway genes can act as "second hits" in digenic-like models, per the broader HPE genotype-phenotype literature)

**Environmental risk factors (relevant to the broader HPE spectrum, and shown experimentally to interact with Gli2 dosage):**
- **Maternal pregestational diabetes** — the single most robust environmental HPE risk factor, conferring >10-fold increased risk, with HPE occurring in ~1–2% of diabetic pregnancies; proposed mechanism involves oxidative stress and disrupted neural crest migration.
- **Retinoic acid excess** — teratogenic in animal models via SHH pathway gene misregulation.
- **Cholesterol biosynthesis inhibitors** (e.g., statins) and metabolic disorders of cholesterol synthesis (Smith-Lemli-Opitz syndrome, DHCR7) — cholesterol is required for SHH ligand post-translational modification and pathway activity.
- **Maternal alcohol exposure** — a mouse study specifically demonstrates **Gli2 gene-dosage × ethanol interaction**: "The Teratogenic Effects of Prenatal Ethanol Exposure Are Exacerbated by Sonic Hedgehog or Gli2 Haploinsufficiency in the Mouse" ([PMC3929747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3929747/)), directly demonstrating a gene-environment interaction relevant to GLI2 haploinsufficiency in humans.

**Protective factors:** No specific protective genetic or environmental factors for GLI2-HPE are established in the literature reviewed; general HPE literature does not identify protective alleles analogous to those in other Mendelian disorders.

**Gene-environment interactions:** The mouse Gli2 haploinsufficiency/ethanol model (above) and a separate mouse study on "Gli2 gene-environment interactions contribute to the etiological complexity of holoprosencephaly" ([PMID:27585885](https://pubmed.ncbi.nlm.nih.gov/27585885/); [PMC5117230](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5117230/)) provide the strongest direct mechanistic evidence: mice heterozygous for a Gli2 null allele are phenotypically normal at baseline but show markedly increased penetrance and severity of HPE-spectrum defects when exposed to low-dose teratogens — a model for the incomplete penetrance seen in human GLI2-mutation carriers and consistent with a genetic "second hit"/environmental modifier framework broadly invoked in HPE etiology.

---

## 3. Phenotypes

Because most human GLI2 mutation carriers present with the **pituitary/polydactyly/facial phenotype rather than classic HPE**, the phenotype list below spans that full spectrum, with HPO terms suggested.

| Phenotype | Type | Frequency (approx., from cohort data) | Onset | Suggested HPO term |
|---|---|---|---|---|
| Postaxial polydactyly (hands and/or feet) | Physical/clinical sign | Frequent — reported in ~4/6 in one cohort, and the defining "polydactyly" arm of Culler-Jones syndrome | Congenital | HP:0100259 (Postaxial polydactyly) / HP:0001162 |
| Panhypopituitarism / multiple pituitary hormone deficiency (MPHD) | Endocrine/laboratory | Frequent among GLI2-mutation carriers ascertained via endocrine clinics | Neonatal–childhood | HP:0004926 (Panhypopituitarism) |
| Growth hormone deficiency | Endocrine | Common component of MPHD | Infancy–childhood | HP:0000824 |
| Ectopic posterior pituitary lobe / pituitary stalk interruption, hypoplastic anterior pituitary | Imaging/structural | Common on MRI in GLI2-hypopituitarism cases, "without HPE" | Congenital | HP:0011750 / HP:0002591 (Hypoplasia of the pituitary gland) |
| Diabetes insipidus | Endocrine | Reported in a subset | Infancy–childhood | HP:0000873 |
| Midfacial hypoplasia | Craniofacial | Common, part of the shared "truncating-mutation facial phenotype" | Congenital | HP:0000308 |
| Hypotelorism | Craniofacial | Common | Congenital | HP:0000601 |
| Cleft lip/cleft palate | Craniofacial | Present in a substantial minority; ranges to isolated cleft lip/palate + polydactyly as sole presentation | Congenital | HP:0410030 / HP:0000175 |
| First branchial-arch anomalies (mandibular hypoplasia, abnormal/malformed ears, pre-auricular tags) | Craniofacial | Reported, including a "novel" TMJ (temporomandibular joint) anomaly finding | Congenital | HP:0009925 (Abnormal external ear morphology) |
| Semilobar holoprosencephaly (brain non-cleavage) | Structural CNS | Uncommon among GLI2 carriers — only 1/43 truncating-variant carriers in one review had frank HPE | Prenatal/congenital | HP:0030082 (Holoprosencephaly) / HP:0002573 (Semilobar holoprosencephaly, per HPO hierarchy) |
| Seizures | Neurological | Reported, part of Culler-Jones syndrome core features | Variable | HP:0001250 |
| Intellectual disability | Neurological/behavioral | Reported, variable severity | Childhood | HP:0001249 |
| Growth impairment / short stature | Systemic | Secondary to GH deficiency | Childhood | HP:0004322 |
| Micropenis, cryptorchidism | Genital | Reported, secondary to hypogonadotropic hypogonadism component of MPHD | Congenital/infancy | HP:0000054, HP:0000028 |
| Hearing loss/deafness (in at least one reported Culler-Jones case) | Sensory | Case-report level | Variable | HP:0000365 |

**Characteristics:**
- **Age of onset:** Congenital (structural/craniofacial and polydactyly features present at birth); pituitary hormone deficiencies often manifest neonatally (hypoglycemia, prolonged jaundice) or emerge through childhood as growth failure.
- **Severity/progression:** Highly variable — from isolated cleft lip/palate with polydactyly at the mild end to semilobar HPE at the severe end. Endocrine deficits are typically **stable but require lifelong hormone replacement**; they are not degenerative.
- **Frequency among carriers — the defining feature is incomplete penetrance:** In one key family study, of 11 parents carrying the same pathogenic GLI2 mutation as an affected proband, "only two had hypopituitarism and three had only polydactyly, while six were apparently completely normal," demonstrating that even severe loss-of-function alleles show markedly incomplete penetrance [Roessler et al. 2003](https://pubmed.ncbi.nlm.nih.gov/14581620/); summarized in [Journal of Molecular Endocrinology 54(3):R141](https://journals.bioscientifica.com/jme/article/54/3/R141/11554/).
- **Quality of life impact:** Untreated panhypopituitarism carries risk of adrenal crisis, severe hypoglycemia, and growth failure; with hormone replacement, endocrine outcomes are generally good. Craniofacial/limb anomalies may require surgical correction (cleft repair, polydactyly excision). Neurodevelopmental outcome tracks with brain structural involvement — normal-to-mild in isolated pituitary/polydactyly presentations, more impaired when frank HPE or seizures are present (Culler-Jones syndrome cohort).

---

## 4. Genetic/Molecular Information

**Causal gene:** GLI2 (GLI-Kruppel family member 2), OMIM *165230, HGNC:4318, located at chromosome 2q14.2. Human GLI2 protein contains an **N-terminal transcriptional repressor domain** and a **C-terminal transcriptional activator domain**; it binds DNA via **C2H2 zinc-finger motifs** ([ScienceDirect Topics: GLI2](https://www.sciencedirect.com/topics/neuroscience/gli2); [PMID:10433919](https://pubmed.ncbi.nlm.nih.gov/10433919/)).

**Variant classification and type:**
- **Truncating variants** (nonsense, frameshift, splice-site) that eliminate the C-terminal activator domain — the best-established pathogenic class, associated with pituitary anomalies, polydactyly, and the characteristic facial gestalt (midface hypoplasia, cleft lip/palate, hypotelorism) [Corder et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62611).
- **Zinc-finger (DNA-binding domain) missense variants** — also implicated in hypopituitarism per the same 2022 study title ("Truncating and zinc-finger variants in GLI2 are associated with hypopituitarism").
- **Contiguous deletions** spanning GLI2 at 2q14 — reported to produce milder HPE-spectrum phenotypes, occasionally with additional features (e.g., heterotaxy) attributable to deletion of neighboring genes [PMID:22106008](https://pubmed.ncbi.nlm.nih.gov/22106008/).
- **Synonymous and other missense variants** are frequently identified but often classified benign/VUS — in the Bertolacini et al. 2012 cohort of 110 craniofacial-anomaly patients, 14 GLI2 variants were found (1 deletion, 1 insertion, 9 nonsynonymous, 3 synonymous), with only a subset (6 patients) judged possibly pathogenic [PMID:21204792](https://pubmed.ncbi.nlm.nih.gov/21204792/).

**Functional consequence:** Predominantly **loss of function / haploinsufficiency**. Roessler et al. functionally demonstrated that identified mutant alleles "lack GLI2 activity," establishing a functional link between GLI2 loss and the human phenotype [PMID:14581620](https://pubmed.ncbi.nlm.nih.gov/14581620/).

**Somatic vs. germline:** All reported HPE9/Culler-Jones variants are **germline** (constitutional), consistent with a developmental malformation syndrome; GLI2 is separately implicated in **somatic** oncogenic activation in some cancers (e.g., medulloblastoma, via Hedgehog pathway dysregulation), but that is mechanistically and clinically distinct from HPE9 and outside its scope.

**Allele frequency:** No population carrier-frequency data specific to pathogenic GLI2 HPE9 alleles were found in gnomAD-level detail in this search; given autosomal dominant inheritance with reduced penetrance and case-level/small-family reporting, pathogenic variants are expected to be **very rare/private** (population allele frequency approaching zero in large reference databases), consistent with ultra-rare disease status.

**Modifier genes:** No specific human modifier genes are validated for GLI2-HPE beyond the broader HPE "multiple-hit" model (interaction with other SHH-pathway gene variants, e.g., SHH, PTCH1, ZIC2, in trans, has been proposed in the general HPE genetics literature as contributing to phenotypic variability, though not GLI2-specific confirmed digenic cases in the sources reviewed here).

**Epigenetic information:** No GLI2-HPE9-specific DNA methylation or chromatin-modification data were identified in this search; GLI2 activity is regulated post-translationally (proteolytic processing/degradation is suppressed by active SHH signaling — [PMID: PMC1447407](https://pmc.ncbi.nlm.nih.gov/articles/PMC1447407/), "Sonic hedgehog Signaling Regulates Gli2 Transcriptional Activity by Suppressing Its Processing and Degradation") rather than primarily by epigenetic mechanisms.

**Chromosomal abnormalities:** 2q14 microdeletions encompassing GLI2 are a recognized structural-variant cause, producing a phenotype continuous with point-mutation HPE9 (mild HPE-spectrum features, occasionally with contiguous-gene effects) [PMID:22106008](https://pubmed.ncbi.nlm.nih.gov/22106008/).

**Suggested gene/ontology annotations:** HGNC:4318 (GLI2); GO:0007224 (Smoothened signaling pathway); GO:0008589 (regulation of Smoothened signaling pathway); GO:0003700 (DNA-binding transcription factor activity); GO:0008270 (zinc ion binding, for the C2H2 zinc-finger domains).

---

## 5. Environmental Information

- **Environmental factors:** No GLI2-HPE9-specific toxin/pollutant exposure data identified; the general HPE environmental risk-factor literature (maternal diabetes, retinoic acid, cholesterol-synthesis-inhibiting drugs, alcohol) is the best proxy, and the mouse Gli2-haploinsufficiency/ethanol interaction study provides direct mechanistic support for gene-dose-dependent teratogen sensitivity relevant to GLI2 carriers specifically [PMC3929747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3929747/).
- **Lifestyle factors:** Maternal glycemic control in pregnancy is the most actionable modifiable factor relevant to the broader HPE spectrum, given the strong maternal-diabetes association.
- **Infectious agents:** None established for HPE or HPE9 specifically.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway:** GLI2 acts as the principal transcriptional effector of the **Sonic Hedgehog (SHH) signaling pathway** (KEGG hsa04340; GO:0007224) in the ventral forebrain, craniofacial mesenchyme/first branchial arch, limb bud, and developing pituitary (Rathke's pouch). Canonical pathway logic:

1. **Ligand-receptor step:** In the absence of SHH ligand, the 12-pass transmembrane receptor **PTCH1** inhibits accumulation and activity of **SMO** (Smoothened) in the primary cilium.
2. **Ligand engagement:** SHH binding to PTCH1 relieves this inhibition, allowing SMO to translocate into/accumulate within the primary cilium (a step also dependent on membrane cholesterol, which both modifies the SHH ligand post-translationally and licenses SMO activation) [ScienceDirect: Patched, Smoothened and cholesterol](https://www.sciencedirect.com/science/article/abs/pii/S0955067418301832).
3. **GLI2 liberation:** Active ciliary SMO drives dissociation of the **SUFU–GLI2** repressive complex (with assistance from EVC/EVC2 at the ciliary base), releasing full-length GLI2 to enter the nucleus as a **transcriptional activator** of target genes including GLI1, PTCH1, and HHIP (a negative-feedback loop gene) [PMID:20956384](https://pubmed.ncbi.nlm.nih.gov/20956384/).
4. **Bifunctional GLI2 processing:** In the absence of SHH signal, GLI2 is partially proteolyzed into a **truncated repressor** form; SHH signaling suppresses this processing/degradation, tipping the balance toward the activator form [PMC1447407](https://pmc.ncbi.nlm.nih.gov/articles/PMC1447407/).

**Causal chain — genotype to phenotype:**
- Heterozygous truncating/loss-of-function GLI2 variant → **GLI2 haploinsufficiency** → reduced SHH-pathway transcriptional output in ventral forebrain midline, first branchial arch/craniofacial mesenchyme, limb bud (zone of polarizing activity-adjacent tissue), and Rathke's pouch/pituitary primordium → **variably penetrant developmental field defects**:
  - Ventral forebrain/midline: failure of prosencephalic cleavage in the most severe cases (classic HPE structural spectrum: alobar > semilobar > lobar > middle interhemispheric variant) — but in most GLI2 carriers, midline signaling is sufficient for cleavage and only subtler midfacial hypoplasia results.
  - Rathke's pouch/anterior pituitary: defective organogenesis → hypoplastic anterior pituitary, ectopic posterior pituitary lobe, panhypopituitarism.
  - Limb bud (postaxial zone): postaxial polydactyly, reflecting a role for GLI2/SHH signaling in anteroposterior limb patterning distinct from (and postaxial rather than the SHH/GLI3-ZRS preaxial pattern typical of ZRS-associated syndromes).
  - First branchial arch derivatives: mandibular hypoplasia, ear anomalies, cleft lip/palate, TMJ anomalies.
- **Incomplete penetrance** is best explained mechanistically by the mouse gene-environment model: a single functional GLI2 allele provides sufficient pathway output for normal development under baseline conditions, but reduced buffering capacity renders development vulnerable to additional genetic or environmental "second hits" (teratogen exposure, stochastic developmental variation, possible modifier alleles in other pathway genes) [PMID:27585885](https://pubmed.ncbi.nlm.nih.gov/27585885/).

**Cellular processes:** Neural progenitor patterning/ventralization in the neural tube and forebrain (GO:0021871, "morphogenesis of embryonic epithelium," and GO:0021854, "hypothalamus development," among relevant GO terms); craniofacial neural crest cell patterning; anterior pituitary progenitor (Rathke's pouch) proliferation and differentiation; limb bud mesenchymal patterning.

**Protein dysfunction:** Predominantly **loss-of-function/haploinsufficiency** — truncated proteins lacking the C-terminal activator domain fail to drive SHH target-gene transcription; some act with residual repressor activity, potentially producing partial dominant-negative effects, though most literature frames the mechanism as simple haploinsufficiency.

**Tissue damage mechanism:** Not applicable in the classic "tissue injury" sense — this is a **developmental patterning defect**, not a degenerative or destructive process; the pathology is one of failed morphogenesis rather than secondary tissue injury (with the caveat that untreated endocrine deficiency can secondarily cause metabolic tissue stress, e.g., hypoglycemic injury).

**Suggested GO/CL/UBERON terms for pathophysiology modeling:**
- GO:0007224 Smoothened signaling pathway
- GO:0021871 forebrain regionalization / GO:0021983 pituitary gland development
- GO:0060173 limb development / GO:0060174 limb bud formation
- CL:0002573 Schwann cell (not directly relevant) — more relevant: CL:0000710 neurectodermal cell / CL:0002028 basal cell of epithelium of Rathke's pouch (if available) / generic "neural progenitor cell" CL:0011020
- UBERON:0002298 brainstem / UBERON:0001891 midbrain (less relevant); most relevant: UBERON:0002264 pars distalis of adenohypophysis, UBERON:0002037 cerebellum (not affected); primary sites: UBERON:0000955 brain (forebrain/prosencephalon), UBERON:0000007 pituitary gland, UBERON:0002544 pharyngeal arch (first branchial arch), UBERON:0002544 limb bud/UBERON:0004357 hand

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (forebrain/prosencephalon — in the minority with true HPE); pituitary gland (anterior and posterior lobes); craniofacial skeleton (midface, mandible, maxilla); limbs (hands/feet — postaxial polydactyly).
- **Secondary/complication-related:** Endocrine organs downstream of pituitary hormone axes (thyroid, adrenal glands, gonads) secondary to central hormone deficiency; eyes (hypotelorism, occasionally more severe ocular anomalies in classic HPE); ears (external ear malformations, pre-auricular tags); oral cavity (cleft lip/palate).
- **Body systems:** Nervous system (CNS structural, and secondary seizures/intellectual disability), endocrine system (primary target of the pituitary-anomaly arm), musculoskeletal system (craniofacial, limb).

**Tissue/cell level:**
- Ventral forebrain neuroepithelium and midline glial structures (in classic HPE cases)
- Rathke's pouch epithelium / anterior pituitary hormone-secreting cell lineages (somatotropes, corticotropes, thyrotropes, gonadotropes — reflecting the multi-hormone deficiency pattern)
- Cranial neural crest-derived craniofacial mesenchyme
- Limb bud mesenchyme (postaxial zone)
- Temporomandibular joint condylar/coronoid cartilage (a specifically noted GLI2-associated finding)

**Subcellular level:** Primary cilium (site of SMO/SUFU/GLI2 pathway transduction — GO:0005929 cilium; GO:0060170 ciliary membrane); nucleus (site of GLI2 transcriptional activity); cytoplasm (site of GLI2 proteolytic processing).

**Localization/laterality:** HPE-spectrum brain and facial anomalies are typically **midline** defects (bilateral, symmetric, affecting the axis of embryonic cleavage) rather than lateralized; postaxial polydactyly may be unilateral or bilateral and can affect hands, feet, or both.

---

## 8. Temporal Development

- **Onset:** Congenital for all structural (craniofacial, limb, brain) features; pituitary hormone deficiencies may be apparent at birth (neonatal hypoglycemia, cholestatic jaundice from cortisol/GH deficiency, micropenis) or emerge over infancy/childhood as growth failure or delayed puberty becomes evident.
- **Onset pattern:** Structural anomalies are fixed at birth (non-progressive congenital malformations); endocrine deficits, while congenital in origin (structural pituitary maldevelopment), may have an **insidious, delayed-recognition** clinical onset if hormone deficiency is partial or evolves.
- **Disease stages:** Not applicable in the sense of a staged progressive disease — HPE9/Culler-Jones syndrome is a static congenital malformation/endocrinopathy rather than a degenerative condition.
- **Progression rate/course:** Structural features are stable (non-progressive) from birth; hormone deficiencies, once established, are generally **lifelong and stable** with replacement therapy, though evolving multi-hormone deficiency over childhood (e.g., isolated GH deficiency progressing to panhypopituitarism) has been described in the broader hypopituitarism literature and is plausible in GLI2 cases.
- **Duration:** Chronic, lifelong (endocrine and structural sequelae persist; surgical corrections of cleft/polydactyly are one-time interventions).
- **Remission:** Not applicable — this is a structural/developmental condition, not a relapsing-remitting disease.
- **Critical periods:** The relevant "critical period" is prenatal — first-trimester forebrain, craniofacial, pituitary (Rathke's pouch), and limb bud patterning windows, during which GLI2 haploinsufficiency (potentially compounded by environmental "second hits" such as maternal hyperglycemia, retinoic acid, or alcohol exposure) determines phenotypic severity.

---

## 9. Inheritance and Population

**Epidemiology:**
- Holoprosencephaly overall occurs in **~1 in 250 conceptuses** but only **~1 in 8,000–16,000 live births** (most affected conceptuses are lost to spontaneous abortion); reported live-birth prevalence ranges 0.48–1.70 per 10,000 across international birth-defect surveillance systems, with a large Chinese national study finding 0.92 per 10,000 (1,222 cases / 13,284,142 births) ([PMC6553724](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6553724/); StatPearls [NBK560861](https://www.ncbi.nlm.nih.gov/books/NBK560861/)).
- **GLI2 is a minor contributor** to this overall HPE burden (<1% of classic HPE cases attributable to GLI2 point mutations), but is disproportionately represented among patients specifically ascertained for **congenital hypopituitarism with polydactyly** — making HPE9/Culler-Jones syndrome an important, likely underdiagnosed cause of syndromic congenital hypopituitarism.
- Exact prevalence/incidence figures specific to HPE9 (as opposed to HPE overall) are not separately tabulated in Orphanet/OMIM; it should be treated as an **ultra-rare** disorder (likely well under 1:1,000,000, per case-series-level reporting to date).

**Inheritance pattern:** **Autosomal dominant**, with the defining features of **incomplete penetrance and variable expressivity**. GeneReviews explicitly notes that "[b]ecause incomplete penetrance is a feature of dominantly inherited HPE, relatively normal facial appearance can be seen in individuals who have causative gene variants and affected first degree relatives" ([NBK1530](https://www.ncbi.nlm.nih.gov/books/NBK1530/)).

**Penetrance:** Markedly incomplete — in the Roessler et al. family study, only 2/11 mutation-carrying parents had hypopituitarism, 3/11 had isolated polydactyly, and 6/11 were phenotypically normal despite carrying the identical pathogenic variant as their affected child. This is among the most striking documented penetrance figures in the monogenic HPE literature and is a key curation point.

**Expressivity:** Highly variable, spanning isolated polydactyly → isolated pituitary anomaly → combined craniofacial/pituitary/limb phenotype (Culler-Jones syndrome) → rare semilobar HPE.

**Germline mosaicism:** Not specifically documented for GLI2 in the sources reviewed, though plausible given the general dominant-inheritance, incomplete-penetrance pattern typical of HPE genes; a documented mother-and-two-daughters case series with a GLI2 deletion explicitly demonstrates "variable expressivity and incomplete penetrance" across generations ([PMC7669391](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7669391/)), consistent with vertical transmission through a mildly/subclinically affected parent.

**Founder effects / consanguinity:** No founder mutations or consanguinity-driven recessive component identified — consistent with autosomal dominant, not recessive, inheritance.

**Carrier frequency:** Not established/reported; expected to be very low given rarity and predominance of de novo or small-family case reporting.

**Population demographics:** No specific ethnic or geographic enrichment reported for GLI2-HPE9 itself; broader HPE literature notes higher reported (ascertainment-influenced) prevalence in some populations (African-American, Hispanic, Pakistani communities in the US) attributable to differential rates of prenatal diagnosis/termination rather than true differential incidence. Sex ratio and age-distribution data specific to HPE9 were not identified in this search.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Endocrine hormone panels:** GH, IGF-1, cortisol/ACTH, TSH/free T4, gonadotropins (LH/FSH), prolactin — to characterize the pattern and completeness of multiple pituitary hormone deficiency (MPHD).
- **Electrolytes/urine osmolality/water-deprivation testing** — for suspected diabetes insipidus (posterior pituitary/ADH axis).

**Imaging:**
- **Brain/pituitary MRI is the key diagnostic imaging modality.** Characteristic findings in GLI2-mutation carriers with hypopituitarism: **hypoplastic anterior pituitary** with an **ectopic posterior pituitary lobe** (pituitary stalk interruption-like pattern), often **without any HPE brain malformation** — this pattern was specifically demonstrated in 4 evaluated patients with GLI2 mutations [PMID:20685856](https://pubmed.ncbi.nlm.nih.gov/20685856/); a further case report describes "Ectopic Posterior Pituitary, Polydactyly, Midfacial Hypoplasia and Multiple Pituitary Hormone Deficiency due to a Novel Heterozygous... Mutation in the GLI2 Gene" ([PMC7499131](https://pmc.ncbi.nlm.nih.gov/articles/PMC7499131/)).
- In more severely affected individuals: MRI may show semilobar or lobar HPE (fused thalami, absent septum pellucidum, monoventricle, absent/hypoplastic corpus callosum, absent olfactory bulbs).
- **Skeletal imaging** for polydactyly characterization prior to surgical planning.

**Genetic testing:**
- **Single-gene GLI2 sequencing** (all coding exons) is commercially available (e.g., [GTR test 583574](https://www.ncbi.nlm.nih.gov/gtr/tests/583574/); PreventionGenetics HPE9/GLI2 panel).
- **HPE gene panels** (typically including SHH, ZIC2, SIX3, TGIF1, PTCH1, GLI2, and others) are the standard first-tier approach given genetic heterogeneity of HPE.
- **Whole-exome/genome sequencing** is increasingly used, especially for atypical/expanded phenotypes ("Exome sequencing improves genetic diagnosis of congenital orofacial clefts" [PMC10512413](https://pmc.ncbi.nlm.nih.gov/articles/PMC10512413/); a 2025 case report describes a de novo GLI2 missense variant identified via exome sequencing in isolated hypopituitarism with craniofacial anomalies).
- **Chromosomal microarray (CMA)** is indicated when a contiguous 2q14 deletion is suspected (larger phenotype, additional features beyond the classic GLI2 point-mutation presentation).
- **Familial cascade testing** is important given documented incomplete penetrance — apparently unaffected parents of a proband may carry the variant and should be counseled that normal phenotype does not exclude carrier status.

**Clinical diagnostic criteria:** No formal consensus diagnostic criteria specific to HPE9 exist; diagnosis rests on the combination of (a) characteristic phenotype (pituitary anomaly ± polydactyly ± midfacial hypoplasia ± cleft lip/palate, with or without HPE), and (b) confirmatory GLI2 molecular finding. **Differential diagnosis** includes other HPE-spectrum genes (SHH, ZIC2, SIX3, TGIF1, PTCH1), other syndromic causes of congenital hypopituitarism with polydactyly (e.g., Pallister-Hall syndrome, GLI3-related — a related GLI-family gene with an analogous polydactyly/hypothalamic hamartoma phenotype and important genetic differential), and Smith-Lemli-Opitz syndrome (cholesterol synthesis defect that phenocopies SHH-pathway disruption).

**Screening:** No population-based newborn screening program targets HPE9 specifically; prenatal ultrasound may detect structural HPE brain findings and polydactyly, prompting targeted prenatal genetic testing in known-carrier families.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Prognosis is highly dependent on phenotypic severity. Isolated polydactyly or isolated mild pituitary anomaly carries an excellent prognosis with normal life expectancy. Severe (semilobar/alobar) HPE carries the poor prognosis characteristic of classic HPE generally (high perinatal/infant mortality in severe forms), but this is uncommon among GLI2 carriers specifically (only ~1/43 truncating-variant carriers had frank HPE in the reviewed literature).
- **Morbidity:** Untreated panhypopituitarism carries risk of life-threatening adrenal crisis and hypoglycemia, particularly in the neonatal period; with recognition and hormone replacement, morbidity is substantially reduced and outcomes approach those of other causes of congenital hypopituitarism.
- **Complications:** Adrenal crisis, severe hypoglycemia (especially neonatal), growth failure if GH deficiency undiagnosed, hypogonadism/delayed puberty, feeding/speech difficulties from cleft palate, functional limb impairment from polydactyly (usually correctable surgically).
- **Recovery potential:** Structural anomalies are permanent (surgical correction, not cure); endocrine deficiencies are fully manageable (not curable) with lifelong hormone replacement — patients on adequate replacement generally achieve normal growth and pubertal development.
- **Prognostic factors:** Presence and severity of brain structural HPE is the dominant prognostic determinant; truncating (vs. missense) GLI2 variants correlate with more complete/severe pituitary and polydactyly phenotypes per the Corder et al. 2022 genotype-phenotype analysis.

---

## 12. Treatment

There is no disease-modifying or curative treatment for the underlying GLI2 developmental defect; management is **multidisciplinary and supportive/replacement-based**.

**Pharmacotherapy (hormone replacement — the mainstay of management):**
- **Growth hormone (recombinant human GH)** for GH deficiency — MAXO term: consider MAXO:0000950 (supportive care) or a specific pharmacotherapy term paired with `therapeutic_agent` (somatropin; NCIT term for recombinant human growth hormone).
- **Hydrocortisone** replacement for ACTH/cortisol deficiency (critical for preventing adrenal crisis).
- **Levothyroxine** for central hypothyroidism (TSH deficiency).
- **Desmopressin (DDAVP)** for central diabetes insipidus.
- **Sex hormone replacement** (testosterone or estrogen/progesterone) at puberty for hypogonadotropic hypogonadism.

**Surgical/interventional:**
- **Polydactyly excision/reconstructive surgery** — MAXO:0000004 (surgical procedure) / NCIT:C15329 (Surgical Procedure), often orthopedic (NCIT:C16186, Orthopedic Surgical Procedure).
- **Cleft lip/palate repair** — standard craniofacial surgical protocol.
- **Craniofacial reconstructive surgery** as needed for midfacial hypoplasia/TMJ anomalies.

**Supportive/rehabilitative care:**
- Early developmental intervention, physical/occupational/speech therapy as indicated by neurodevelopmental status (MAXO:0000011 physical therapy; MAXO:0000930 speech therapy).
- Nutritional support in infancy, particularly for feeding difficulty related to cleft palate or hypoglycemia risk.

**Genetic counseling:** MAXO:0000079 (genetic counseling) is essential given autosomal dominant inheritance with incomplete penetrance — counseling must explicitly address the possibility of a phenotypically normal or minimally affected (isolated polydactyly) parent carrying the causal variant, given the well-documented penetrance data above.

**Experimental/targeted therapies:** No GLI2-pathway-targeted or gene therapy approaches were identified as being in clinical development for HPE9 specifically. (Hedgehog-pathway small-molecule inhibitors such as SMO inhibitors exist for cancer indications — e.g., basal cell carcinoma, medulloblastoma — but these target pathway *hyperactivation* and are not relevant to this loss-of-function developmental disorder; no gain-of-function/agonist strategy for GLI2 haploinsufficiency was found reported.)

**Treatment strategy:** Management follows a **standard congenital hypopituitarism algorithm** (endocrinology-led, with hormone deficiencies identified and replaced sequentially/simultaneously as diagnosed) combined with **craniofacial/orthopedic surgical planning** for structural anomalies — essentially the same clinical pathway used for other genetic causes of congenital hypopituitarism with polydactyly (e.g., Pallister-Hall syndrome).

---

## 13. Prevention

- **Primary prevention:** No primary prevention exists for the germline GLI2 mutation itself. For the environmentally-modulated component of the broader HPE spectrum, optimizing maternal glycemic control in diabetic pregnancies is the most evidence-supported modifiable primary-prevention measure; avoidance of retinoic acid excess and cholesterol-synthesis-inhibiting medications in pregnancy is also generally advised in the broader HPE prevention literature.
- **Secondary prevention (early detection):** Newborn screening for hypoglycemia/jaundice in infants with any suggestive dysmorphic features (polydactyly + midfacial hypoplasia) should prompt early endocrine evaluation to prevent adrenal-crisis morbidity — this is the single most impactful secondary-prevention measure for GLI2-HPE9, given that endocrine complications (not structural anomalies) drive acute morbidity/mortality risk.
- **Genetic screening:** Prenatal diagnosis via targeted GLI2 testing is available in families with a known pathogenic variant; given incomplete penetrance, genetic counseling must clarify that a negative family history in parents does not reduce recurrence risk if a parent is an unrecognized (subclinical) carrier.
- **Tertiary prevention:** Lifelong monitoring and hormone-replacement adjustment to prevent complications of under- or over-replacement (e.g., adrenal crisis prevention via stress-dosing education, growth monitoring on GH therapy).
- **Public health/behavioral:** No population-level public health intervention specific to HPE9 exists; general periconceptional counseling regarding diabetes control and teratogen avoidance applies to the broader HPE risk-reduction framework.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Mouse (*Mus musculus*, NCBITaxon:10090) is the dominant model species; Gli2 is also studied in zebrafish (*Danio rerio*, NCBITaxon:7955) in the broader Hedgehog-signaling/craniofacial development literature, though HPE9-specific zebrafish models were not identified in this search.
- **Orthologous gene:** Mouse *Gli2* (MGI:95728), NCBI Gene ID 14633 (mouse); highly conserved zinc-finger transcription factor with essentially identical domain architecture and pathway role as human GLI2.
- **Natural disease in other species:** No naturally occurring GLI2-mutant HPE has been reported in companion animals or wildlife in the sources reviewed (this is a modeled/engineered-mutation disease in animals, not a spontaneously occurring veterinary condition, unlike some other Mendelian disorders with OMIA entries).
- **Comparative pathology:** Mouse *Gli2* null homozygotes show floor-plate absence, foregut/lung/anorectal defects, skeletal malformations, and altered commissural neuron guidance, with most dying before E18.5 ([MGI:95728](https://www.informatics.jax.org/marker/MGI:95728)). Background-strain-dependent HPE recapitulation is a key comparative-biology point (see Model Organisms below).

---

## 15. Model Organisms

- **Mouse Gli2 knockout (constitutive null):** Homozygous *Gli2*-null mice are embryonic lethal (most die before E18.5) with **absence of the neural tube floor plate**, foregut/lung/anorectal defects, skeletal malformations, and altered commissural neuron axon guidance ([MGI:95728](https://www.informatics.jax.org/marker/MGI:95728)).
- **Genetic-background dependence — a key model insight:** On the **C57BL/6J background**, homozygous Gli2 loss-of-function recapitulates the characteristic brain and facial features of **severe human HPE**, including midfacial hypoplasia, hypotelorism, and medial forebrain deficiency with loss of ventral neurospecification. In contrast, Gli2-null mice on an **outbred CD-1 background do not recapitulate the forebrain/facial HPE phenotype** — directly demonstrating background-dependent modifier effects on HPE penetrance/expressivity, a strong parallel to the incomplete penetrance seen in human GLI2 carriers.
- **Heterozygous (haploinsufficient) mice as the more clinically relevant model:** *Gli2*+/− heterozygous mice are phenotypically **normal at baseline**, closely mirroring the incompletely penetrant human carrier state, but show **increased penetrance and severity of HPE-spectrum defects upon low-dose teratogen exposure** — the key gene-environment interaction model for this disease ([PMID:27585885](https://pubmed.ncbi.nlm.nih.gov/27585885/); [PMC5117230](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5117230/)).
- **Ethanol-exposure model:** *Gli2* (and *Shh*) haploinsufficient mice show exacerbated teratogenic response to prenatal ethanol exposure, directly modeling a gene × alcohol-exposure interaction relevant to the "second hit" hypothesis for incomplete penetrance in human carriers ([PMC3929747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3929747/)).
- **Model limitations:** Because complete phenotype recapitulation (forebrain/facial HPE) requires both homozygous loss and a permissive (C57BL/6J) genetic background, no single mouse model directly represents the typical human HPE9 situation (heterozygous variant, phenotype ranging from normal to severe). The heterozygous + teratogen-challenge paradigm is the best available proxy for the human clinical reality of incomplete penetrance and gene-environment-dependent expressivity.
- **Applications:** These models are used to study SHH-pathway dosage sensitivity in forebrain/craniofacial/pituitary/limb patterning, to dissect genetic-background modifier effects on penetrance, and to test specific environmental teratogen interactions (diabetes-like hyperglycemia models, retinoic acid, ethanol, cholesterol-pathway inhibitors) relevant to human risk-factor counseling.
- **Resources:** MGI (Mouse Genome Informatics) — Gli2 gene page [MGI:95728](https://www.informatics.jax.org/marker/MGI:95728); specific targeted allele [MGI:2158720](https://www.informatics.jax.org/allele/MGI:2158720).

---

## Summary of Key Curation Points for a Dismech Entry

1. **Two-tier phenotype framing is essential**: HPE9 nominally denotes GLI2-caused HPE, but the dominant, best-evidenced human phenotype is the **pituitary anomaly + postaxial polydactyly + subtle facial features** presentation (formally split out as Culler-Jones syndrome, OMIM #615849) — true brain-cleavage HPE is a minority presentation in GLI2 carriers (~1/43 truncating-variant carriers). A dismech entry should model this spectrum explicitly, likely with `has_subtypes` distinguishing the classic-HPE-with-forebrain-cleavage presentation from the pituitary/polydactyly-predominant presentation, and should consider cross-referencing/coordinating with a separate Culler-Jones syndrome entry if one exists or is planned (grouping candidate).
2. **Incomplete penetrance is the single most citable, well-quantified fact** (Roessler 2003: 2/11 hypopituitarism, 3/11 isolated polydactyly, 6/11 unaffected among mutation-carrying parents) — ideal for the `Inheritance` block and for genetic-counseling notes.
3. **Mechanism module fit:** This disease is a strong candidate for `conforms_to` a Sonic Hedgehog / GLI2-pathway–anchored pathophysiology node (SUFU-GLI2 dissociation → nuclear GLI2 activator function → target-gene transcription in forebrain/pituitary/limb/craniofacial primordia), and pairs naturally with the mouse gene-environment (Gli2 haploinsufficiency × teratogen) model as `HUMAN_MODEL_MISMATCH`/mechanistic-hypothesis material explaining penetrance variability.
4. **Primary citable sources:** Roessler et al. 2003 (PMID:14581620, founding paper), Bertolacini et al. 2012 (PMID:21204792, phenotypic variability cohort), Corder et al. 2022 (AJMG-A, genotype-phenotype truncating vs. zinc-finger), and the 2010 PubMed:20685856 imaging paper are the core human-clinical evidence base; PMID:27585885 and PMC3929747 are the core model-organism (MODEL_ORGANISM evidence_source) sources for the gene-environment mechanism.

---

**Sources:**
- [Entry - #610829 - HOLOPROSENCEPHALY 9; HPE9 - OMIM](https://omim.org/entry/610829)
- [Entry - *165230 - GLI-KRUPPEL FAMILY MEMBER 2; GLI2 - OMIM](https://omim.org/entry/165230)
- [Entry - #615849 - CULLER-JONES SYNDROME; CJS - OMIM](https://omim.org/entry/615849)
- [Holoprosencephaly Overview - GeneReviews - NCBI Bookshelf (NBK1530)](https://www.ncbi.nlm.nih.gov/books/NBK1530/)
- [Loss-of-function mutations in the human GLI2 gene are associated with pituitary anomalies and holoprosencephaly-like features - PubMed (PMID:14581620)](https://pubmed.ncbi.nlm.nih.gov/14581620/)
- [Clinical findings in patients with GLI2 mutations – phenotypic variability - PMC (PMID:21204792)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135662/)
- [Truncating and zinc‐finger variants in GLI2 are associated with hypopituitarism - Corder et al. 2022 - AJMG-A](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62611)
- [Novel heterozygous nonsense GLI2 mutations in patients with hypopituitarism and ectopic posterior pituitary lobe without holoprosencephaly - PubMed (PMID:20685856)](https://pubmed.ncbi.nlm.nih.gov/20685856/)
- [Ectopic Posterior Pituitary, Polydactyly, Midfacial Hypoplasia and MPHD due to a Novel GLI2 Mutation - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7499131/)
- [A patient with a mild holoprosencephaly spectrum phenotype and heterotaxy and a 1.3 Mb deletion encompassing GLI2 - PubMed (PMID:22106008)](https://pubmed.ncbi.nlm.nih.gov/22106008/)
- [Role of GLI2 in hypopituitarism phenotype - Journal of Molecular Endocrinology](https://journals.bioscientifica.com/jme/article/54/3/R141/11554/)
- [Case Report: A case of Culler-Jones syndrome caused by GLI2 gene mutation - Frontiers/PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12757346/)
- [A case series of a mother and two daughters with a GLI2 gene deletion demonstrating variable expressivity and incomplete penetrance - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7669391/)
- [Gli2 gene-environment interactions contribute to the etiological complexity of holoprosencephaly: evidence from a mouse model - PMC (PMID:27585885)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5117230/)
- [The Teratogenic Effects of Prenatal Ethanol Exposure Are Exacerbated by Sonic Hedgehog or Gli2 Haploinsufficiency in the Mouse - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3929747/)
- [Gli2 MGI Mouse Gene Detail - MGI:95728](https://www.informatics.jax.org/marker/MGI:95728)
- [Sonic hedgehog Signaling Regulates Gli2 Transcriptional Activity by Suppressing Its Processing and Degradation - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1447407/)
- [A mechanism for vertebrate Hedgehog signaling: recruitment to cilia and dissociation of SuFu-Gli protein complexes - PubMed](https://pubmed.ncbi.nlm.nih.gov/20956384/)
- [The interplay of Patched, Smoothened and cholesterol in Hedgehog signaling - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0955067418301832)
- [Regulation of Gli2 and Gli3 activities by an amino-terminal repression domain - PubMed (PMID:10433919)](https://pubmed.ncbi.nlm.nih.gov/10433919/)
- [Epidemiological characteristics of holoprosencephaly in China, 2007-2014 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6553724/)
- [Holoprosencephaly - StatPearls - NCBI Bookshelf (NBK560861)](https://www.ncbi.nlm.nih.gov/books/NBK560861/)
- [Holoprosencephaly: Review of Embryology, Clinical Phenotypes, Etiology and Management - MDPI Children](https://www.mdpi.com/2227-9067/10/4/647)
- [The unfolding clinical spectrum of holoprosencephaly due to mutations in SHH, ZIC2, SIX3 and TGIF genes - EJHG](https://www.nature.com/articles/ejhg201070)
- [Holoprosencephaly 9 - MalaCards](https://www.malacards.org/card/holoprosencephaly_9_2)
- [NM_001374353.1(GLI2):c.4612T>C (p.Ser1538Pro) AND Holoprosencephaly 9 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000030728/)