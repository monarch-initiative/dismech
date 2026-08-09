---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T00:45:49.729651'
end_time: '2026-07-31T00:51:12.380767'
duration_seconds: 322.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holoprosencephaly 12 With or Without Pancreatic Agenesis
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
  web_search_requests: 16
  num_turns: 27
  total_cost_usd: 1.9498761999999996
  session_id: 960620ec-c302-557f-8b90-97540b6164dc
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Holoprosencephaly 12 With or Without Pancreatic Agenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Holoprosencephaly 12 With or Without Pancreatic Agenesis** covering all of the
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

# Research Report: Holoprosencephaly 12 With or Without Pancreatic Agenesis (HPE12)

## 1. Disease Information

**Overview.** Holoprosencephaly 12 with or without pancreatic agenesis (HPE12) is a rare, genetically defined developmental disorder in which failure of the embryonic forebrain (prosencephalon) to cleave into two cerebral hemispheres (holoprosencephaly, HPE) co-occurs — in most but not all reported individuals — with congenital absence of the pancreas, producing neonatal/early-infancy insulin-dependent diabetes and exocrine pancreatic insufficiency. It is caused by a specific, recurrent heterozygous *CNOT1* missense variant. OMIM summarizes it as "a developmental disorder characterized by abnormal separation of the embryonic forebrain (HPE) resulting in dysmorphic facial features and, often but not always, impaired neurologic development. Most patients with this form of HPE also have congenital absence of the pancreas, resulting in early-onset type 1 diabetes mellitus and requiring pancreatic enzyme replacement" (OMIM #618500).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | **#618500** — HOLOPROSENCEPHALY 12 WITH OR WITHOUT PANCREATIC AGENESIS; HPE12 |
| OMIM (gene) | *604917* — CCR4-NOT TRANSCRIPTION COMPLEX, SUBUNIT 1; CNOT1 |
| MONDO | **MONDO:0032787** |
| Orphanet | **ORPHA:556955** — Pancreatic agenesis-holoprosencephaly syndrome |
| Gene | **CNOT1**, HGNC:7877, chromosome 16q21 |
| HGNC gene xref (dismech-style, lowercase) | `hgnc:7877` |
| Inheritance | Autosomal dominant (all reported cases de novo) |
| ICD-10 (closest, non-specific) | Q04.3 (Other reduction deformities of brain, incl. holoprosencephaly) |
| MeSH | Holoprosencephaly D019586; Pancreatic Agenesis is not separately indexed (indexed under congenital pancreatic anomalies) |

**Synonyms:** Pancreatic Agenesis and Holoprosencephaly Syndrome; PAHS; CNOT1-related holoprosencephaly; HPE with pancreatic agenesis (CNOT1-associated).

**Evidence basis of the disease description:** The disease description is derived almost entirely from **aggregated, individually reported patient/family case series** rather than a large aggregated registry — currently 6 reported individuals across 3 primary literature sources (a discovery cohort study, a fetal autopsy case report, and a later phenotypic-expansion case report), plus a mouse knock-in model. This is a very small, still-emerging n, so phenotypic frequencies should be treated as provisional (Sources: [PMC6506862](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6506862/), [PubMed 35481434](https://pubmed.ncbi.nlm.nih.gov/35481434/), [PubMed 39149840](https://pubmed.ncbi.nlm.nih.gov/39149840/)).

---

## 2. Etiology

**Disease causal factor — genetic, single recurrent variant.** HPE12 is caused by a **heterozygous, de novo, recurrent missense variant** in *CNOT1*:
> GenBank NM_016284.4; **c.1603C>T (p.Arg535Cys)**, exon 14 — De Franco et al. 2019 (PMID:31006513), OMIM #618500.

This is unusual among monogenic disease genes in that essentially **all reported disease-causing alleles are the identical single amino-acid substitution** — a strong "mutation-specific" (rather than simple loss-of-function/haploinsufficiency) genotype-phenotype signature (see Mechanism, §6).

**Genetic risk factors:**
- The causal variant arises **de novo** in essentially all reported cases (confirmed de novo in the original 3 probands where parental samples were available, and in the subsequent fetal case; PMID:31006513, PMID:35481434).
- *CNOT1* is under strong purifying selection in the general population: gnomAD reports **pLI = 1.0** and **LOEUF ≈ 0.06**, indicating extreme intolerance to loss-of-function variation — consistent with a scaffold gene essential for the CCR4-NOT complex and explaining why *only* a specific hypomorphic/altered-function missense change (not truncating LOF alleles) is compatible with live birth.
- Notably, three unrelated *CNOT1* de novo variants identified through the Deciphering Developmental Disorders (DDD) study cause developmental delay **without** the structural pancreatic/HPE malformation, implying that variant location/type — not simple haploinsufficiency — determines phenotype (PMC6506862).

**Environmental/other risk factors:** None specifically established for the CNOT1-driven form. General HPE risk factors (maternal diabetes, retinoic acid exposure, cholesterol-synthesis inhibitors, twinning) are documented for HPE broadly but have not been implicated in the CNOT1-specific syndrome, which is monogenic and de novo.

**Protective factors:** None reported/established.

**Gene-environment interaction:** Not established for this specific gene; general HPE literature documents maternal diabetes and other teratogens as modifiers of SHH-pathway HPE penetrance/severity, but no CNOT1-specific G×E data exist.

---

## 3. Phenotypes

Phenotype data are drawn from the 6 reported individuals (3 in De Franco et al. 2019, PMID:31006513; 1 fetal case in Cospain et al. 2022, PMID:35481434, who state the p.Arg535Cys variant "was previously reported in 5 unrelated children" — i.e., cumulative reporting across sources; 1 additional postnatal case without pancreatic agenesis in Queiroz Júnior et al. 2024, PMID:39149840).

| Phenotype | HPO suggestion | Frequency (reported cohort) | Onset | Notes |
|---|---|---|---|---|
| Holoprosencephaly (semilobar/lobar) | HP:0002507 (Semilobar holoprosencephaly) / HP:0001360 (Holoprosencephaly) | Present in all/most reported cases (2/3 confirmed in original cohort as definite; 1 possible; the fetal case had confirmed semi-lobar HPE) | Prenatal/congenital | Range from possible mild features to confirmed semilobar HPE; "absence of the anterior interhemispheric fissure, fusion of the frontal lobes, absence of frontal horns, absence of the sylvian fissures" documented by MRI in one patient (PMC6506862) |
| Pancreatic agenesis (complete or partial) | HP:0006443 (Pancreatic agenesis) | 4/5 (per Cospain et al. cumulative reporting) — "not always" present per OMIM | Congenital, present at birth | Total pancreas agenesis confirmed at fetal autopsy in one case (PMID:35481434); can be absent even when the variant is present (PMID:39149840) |
| Neonatal/early-infancy insulin-dependent diabetes mellitus | HP:0008270 (Neonatal insulin-dependent diabetes mellitus) | Present when pancreatic agenesis occurs; 2/3 original patients diagnosed day 1 of life, one at 13 weeks | Neonatal to early infancy (or adolescent-onset in the variant case without pancreatic agenesis) | All three original patients required both insulin and pancreatic enzyme replacement within the first 6 months of life |
| Exocrine pancreatic insufficiency | HP:0001738 (Exocrine pancreatic insufficiency) | Co-occurs with pancreatic agenesis | Congenital | Requires pancreatic enzyme replacement therapy |
| Late-onset (adolescent) diabetes mellitus without pancreatic agenesis | HP:0000819 (Diabetes mellitus) | 1 reported case | Adolescence | Demonstrates that pancreatic phenotype spectrum is broader than isolated agenesis — authors recommend diabetes surveillance even when no structural pancreas anomaly is seen at birth (PMID:39149840) |
| Gallbladder agenesis | HP:0011773 (Gallbladder agenesis) | Present in 2/3 original patients (P01, P02) | Congenital | |
| Sensorineural/hearing loss | HP:0000365 (Hearing impairment) | Reported as an associated feature (OMIM) | Variable | |
| Global developmental delay / intellectual disability | HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) | Variable — "common but not universal" (OMIM); neurologic impairment not seen in all patients | Infancy/childhood | Phenotype is variable — some patients neurologically normal |
| Very low birth weight (IUGR) | HP:0001518 (Decreased body weight) / HP:0001511 (Intrauterine growth retardation) | 3/3 original patients (birth-weight Z-score < −2) | Congenital | |
| Dysmorphic facial features | — | Present, variable | Congenital | One patient: "prominent central incisors and occiput, highly arched palate, and low-set ears" (HP:0000218 highly arched palate; HP:0000369 low-set ears; HP:0000269 prominent occiput) |

**Quality-of-life impact:** Not formally studied with standardized instruments (EQ-5D/SF-36) in this ultra-rare condition; qualitatively, affected children face lifelong insulin dependence, pancreatic enzyme replacement, and — in those with structural HPE and neurodevelopmental impairment — variable degrees of developmental support needs. No dedicated natural-history or QoL cohort study exists.

---

## 4. Genetic/Molecular Information

**Causal gene:** *CNOT1* (CCR4-NOT Transcription Complex Subunit 1), HGNC:7877, OMIM *604917, chromosome 16q21.

**Pathogenic variant:**
- **Variant:** c.1603C>T, p.(Arg535Cys), exon 14, NM_016284.4
- **Classification:** Pathogenic (ACMG) — recurrent de novo missense, absent from population databases, highly conserved residue ("highly conserved from humans to *C. elegans*," PMC6506862), functionally validated in a knock-in mouse model
- **Variant type:** Missense (single recurrent substitution — arginine to cysteine at residue 535)
- **Allele frequency:** Not present in gnomAD/population databases (consistent with de novo occurrence and severe/lethal-in-homozygous-state biology)
- **Origin:** Germline, de novo in every genotyped case
- **Functional consequence:** Not simple loss-of-function; proposed to be a specific gain/alteration-of-function or dominant-interfering change that preserves (rather than abolishes) CNOT1's transcriptional-repressor activity on early differentiation factors, thereby failing to repress *SHH* appropriately (see Mechanism).
- **Gene constraint:** gnomAD pLI = 1.0, LOEUF ≈ 0.06 — among the most loss-of-function-intolerant genes in the genome, explaining why only this specific missense change (not truncating alleles) produces a live-born phenotype.

**Modifier genes:** None established; phenotypic variability (e.g., presence/absence of pancreatic agenesis in carriers of the identical p.Arg535Cys allele) is documented but unexplained (PMID:39149840).

**Epigenetic information:** Not specifically studied in human HPE12; broadly, CNOT1/CCR4-NOT complex has documented roles in post-transcriptional gene silencing (miRNA-mediated, via TNRC6 interaction) that could plausibly intersect with epigenetic regulatory networks, but no CNOT1-HPE12-specific epigenomic data exist.

**Chromosomal abnormalities:** None — this is a single-nucleotide missense disorder, distinct from the many chromosomal (e.g., trisomy 13, 18p−, 13q−) causes of holoprosencephaly captured under separate HPE nosology.

**Gene function (CNOT1/CCR4-NOT complex):** CNOT1 encodes the core scaffolding subunit of the CCR4-NOT deadenylase complex, which coordinates mRNA deadenylation/decay, translational repression, and transcriptional regulation. The L-shaped complex has a nuclease/deadenylase module (CNOT6/6L, CNOT7/8) and a NOT module (CNOT2, CNOT3, CNOT9, CNOT10, CNOT11), all binding to different domains of the CNOT1 scaffold from N- to C-terminus. CNOT1 has been proposed as critical for maintaining embryonic stem cells in a pluripotent state (PMC6506862; GeneCards). A recently characterized HEAT-repeat domain (residues ~800–999) mediates interaction with tristetraprolin (TTP)/ZFP36 for AU-rich-element mRNA decay (PMC11939966) — the p.Arg535Cys variant lies N-terminal to this characterized HEAT domain, in a distinct, also highly conserved region.

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious contributing factors have been identified for HPE12; the disorder is fully explained (in all reported cases) by the de novo *CNOT1* p.Arg535Cys variant. General HPE-associated environmental risk factors (maternal pregestational diabetes, retinoids, cholesterol-synthesis-inhibiting drugs such as statins/AY9944-class teratogens, alcohol) are documented in the broader HPE literature but have not been specifically linked to CNOT1-associated cases.

---

## 6. Mechanism / Pathophysiology

**Causal chain (from De Franco et al. 2019, PMC6506862):**

1. **Trigger:** De novo *CNOT1* c.1603C>T (p.Arg535Cys) missense variant.
2. **Molecular/protein level:** The variant is proposed to alter — rather than abolish — CNOT1's repressor function. The authors state the mutant "results in CNOT1 maintaining its inhibition activity on the GATA and other early differentiation factors and, as a consequence, SHH expression is not repressed."
3. **Cellular level:** Persistent CNOT1-mediated repression of early endodermal/neural differentiation factors keeps multipotent/embryonic progenitor cells in an undifferentiated (stem-like) state longer than normal, coupled with **increased Shh expression** (confirmed in mouse pancreatic tissue, p = 0.0107) that further blocks differentiation ("a model in which the CNOT1 p.Arg535Cys mutation results in embryonic stem cells being maintained in an undifferentiated state through SHH-mediated inhibition of differentiation," PMC6506862).
4. **Tissue level, pancreas:** In homozygous mutant mouse embryos (E14.5), pancreatic (especially dorsal pancreas) progenitors fail to properly express the pancreatic differentiation program: significantly **decreased Pdx1** (p = 0.0189), **Ins** (p = 7.03×10⁻⁶), **Hnf1b** (p = 0.0294), and **Ptf1a** (p = 0.00781), with **Gata6/Rxra unchanged** — i.e., a selective failure of the endocrine/exocrine differentiation cascade downstream of persistent Shh signaling, and dramatically reduced dorsal pancreas volume (p < 10⁻¹⁰ by high-resolution episcopic microscopy).
5. **Tissue level, forebrain:** Impaired ventral forebrain patterning consistent with dysregulated SHH signaling produces failure of prosencephalic cleavage — the classic final common pathway of essentially all monogenic HPE (SHH pathway disruption is "the main pathophysiologic mechanism underlying HPE" broadly; MDPI review PMC10137117/StatPearls NBK560861).
6. **Organism/clinical level:** Structural HPE (semilobar/lobar) + congenital pancreatic agenesis → neonatal diabetes + exocrine pancreatic insufficiency + variable neurodevelopmental impairment, hearing loss, and gallbladder agenesis.

**Upstream vs. downstream:** CNOT1 dysfunction (upstream) → SHH pathway dysregulation (a shared convergence point with essentially all other monogenic HPE genes: SHH, ZIC2, SIX3, GLI2, FGF8, FGFR1, DISP1, DLL1) → failure of ventral midline patterning in both forebrain and pancreatic primordia (downstream, shared organogenesis defect). This makes HPE12 mechanistically a member of the same "SHH-pathway HPE" convergence class as the classical HPE genes, but with an unusual second organ (pancreas) affected because CNOT1, unlike SHH itself, acts further upstream in a stem/progenitor-maintenance role shared by both organ primordia.

**Cell types involved:** Embryonic/pluripotent stem-like progenitor cells (general), pancreatic multipotent progenitor cells, neuroepithelial cells of the ventral forebrain/prosencephalon.

**Suggested ontology terms:**
- **GO (biological process):** GO:0007224 (smoothened signaling pathway) / GO:0021979 (hypothalamus cell differentiation) is less precise — more directly: **GO:0007224** is SMO-specific; better to use **"Sonic hedgehog signaling pathway"** — note dismech curators should verify exact GO ID via OAK, but candidate terms include GO:0060831 (Hedgehog signaling); GO:0031016 (pancreas development); GO:0021983 (pituitary gland development, N/A); GO:0021983 not relevant; **GO:0030900** (forebrain development); GO:0021978 (telencephalon regionalization); GO:0000289 (mRNA deadenylation, for CNOT1's baseline molecular function); GO:0019827 (stem cell population maintenance); GO:0017148 (negative regulation of translation).
- **CL (cell types):** CL:0002322 (embryonic stem cell) or CL:0000723 (somatic stem cell); pancreatic multipotent progenitor cell (CL:0005020 or similar — verify via OAK); CL:0000030 (neuroepithelial cell).
- **UBERON (anatomy):** UBERON:0001264 (pancreas); UBERON:0001890 (forebrain) / UBERON:0002037 (prosencephalon, verify exact term); UBERON:0001211 (dorsal pancreas — verify).
- **HGNC gene:** hgnc:7877 (CNOT1); comparator/pathway genes: hgnc:10848 (SHH), hgnc:12873 (GATA6), hgnc:9490 (PDX1), hgnc:9484 (PTF1A).

**Molecular profiling/omics:** The primary functional dataset is bulk RNA expression from E14.5 mouse pancreatic tissue (qPCR-based, not genome-wide RNA-seq) in the De Franco et al. 2019 study; no human transcriptomic, proteomic, or single-cell data have been published for this specific syndrome as of this search. No CRISPR/RNAi functional genomic screens specific to this variant have been reported.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (forebrain/prosencephalon — failure of hemispheric cleavage) and pancreas (agenesis/hypoplasia, predominantly dorsal pancreas in the mouse model).
- **Secondary:** Gallbladder (agenesis in a subset), inner ear/cochlea (hearing loss in a subset), craniofacial skeleton (dysmorphic facial features).
- **Body systems:** Nervous system (CNS structural malformation ± neurodevelopmental impairment), endocrine system (pancreatic islet failure → diabetes), digestive system (exocrine pancreas, gallbladder), auditory system.

**Tissue/cell level:** Neuroepithelium of the ventral prosencephalon; pancreatic epithelial progenitors (both endocrine and exocrine lineages, based on decreased Pdx1/Ins/Ptf1a/Hnf1b); cochlear sensory epithelium (for the hearing-loss feature, mechanism not specifically studied).

**Subcellular level:** CNOT1 itself functions predominantly in the cytoplasm (mRNA deadenylation/decay machinery, P-bodies) and has nuclear transcriptional-repressor activity; GO Cellular Component candidates: GO:0030014 (CCR4-NOT complex), GO:0005634 (nucleus), GO:0000932 (P-body).

**Localization/lateralization:** The forebrain malformation is a midline defect (failure of interhemispheric separation) rather than lateralized; imaging in one patient documented "absence of the anterior interhemispheric fissure, fusion of the frontal lobes, absence of frontal horns, absence of the sylvian fissures" (bilateral, midline-symmetric). Mouse data show the dorsal pancreas is preferentially affected relative to the ventral pancreas.

---

## 8. Temporal Development

**Onset:** Congenital — both the brain malformation and (when present) pancreatic agenesis are present from early embryonic/fetal life; diabetes typically manifests neonatally (day 1 of life in 2/3 original patients) to early infancy (13 weeks in the third), though one reported individual with the identical variant but without structural pancreatic agenesis presented with diabetes only in **adolescence** (PMID:39149840) — indicating a variable "critical window" for clinical pancreatic-endocrine failure even when the underlying molecular lesion is identical.

**Progression:** The structural brain and pancreatic anomalies are fixed/static congenital malformations (not progressive structural lesions), but the functional consequences (diabetes, exocrine insufficiency, hearing loss, developmental impairment) are lifelong and require ongoing management. Disease course is chronic/lifelong, not self-limited.

**Patterns:** No spontaneous remission described (structural malformations are permanent; diabetes requires lifelong insulin). The "critical period" for the causal insult is early embryogenesis (pancreatic and forebrain organogenesis, roughly analogous to human 4th–8th post-conceptional week for HPE and early pancreatic budding), well before any postnatal intervention window — i.e., this is a primary prevention-only critical period (there is no known way to rescue the developmental defect after conception; management is entirely supportive/replacement-based postnatally).

---

## 9. Inheritance and Population

**Epidemiology:** HPE12 is **ultra-rare** — as of current literature, only ~6 individuals (from 2 core reports plus 1 phenotype-expansion case) have been published with a confirmed *CNOT1* p.Arg535Cys genotype (PMC6506862; PMID:35481434; PMID:39149840). No formal population prevalence/incidence estimate exists for this specific molecular subtype. For context, broader holoprosencephaly (all causes) has a live-birth prevalence generally cited as **<1 per 10,000** but far higher in early embryonic/first-trimester loss and terminations of pregnancy (up to 40–50 per 10,000 in aborted-embryo series), reflecting very high embryonic/fetal lethality; a large China national birth-defects surveillance study (2007–2014) reported an overall live-birth HPE prevalence of **0.92 per 10,000 births** (PubMed 20104599; PMC6553724). For pancreatic agenesis specifically, *CNOT1* is one of only ~8 known causative genes (PDX1, PTF1A, RFX6, GATA6, GATA4, CNOT1, ONECUT1, ZNF808), among which it accounts for a small minority of a rare disease's genetic causes (originally 3/107 individuals with pancreatic agenesis and definite/possible HPE screened in the discovery cohort; De Franco et al. 2019).

**Inheritance pattern:** Autosomal dominant; **all reported cases have arisen de novo** — no vertical transmission (parent-to-child) has been documented, likely reflecting either severe reduction in reproductive fitness of affected individuals or (per the mouse model) reduced viability of the variant allele in some genetic contexts.

**Penetrance:** Appears high for the pancreatic-agenesis/HPE phenotype overall, but individual features are variably expressed — one identical-genotype case lacked structural pancreatic agenesis entirely and only developed diabetes in adolescence (PMID:39149840), demonstrating incomplete/variable penetrance for specific organ phenotypes despite an identical causal variant.

**Expressivity:** Markedly variable — from possible/mild HPE features with normal neurodevelopment to confirmed semilobar HPE with global developmental delay; from complete pancreatic agenesis with neonatal diabetes to no structural pancreatic defect with adolescent-onset diabetes.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented, though as a purely de novo AD disorder, standard recurrence-risk counseling should still account for possible parental germline mosaicism (empiric ~1% background risk, as for other de novo AD conditions), even though no case has yet been reported.

**Founder effects:** None described — the recurrent p.Arg535Cys variant occurring independently in multiple unrelated families across different countries (UK/US discovery cohort, French fetal case, Brazilian case) is best explained by mutational hotspot/CpG-type recurrence rather than a shared founder haplotype, though haplotype analysis has not been explicitly reported in the sources reviewed.

**Consanguinity:** Not relevant (autosomal dominant, de novo).

**Carrier frequency:** Not applicable (not a recessive carrier-screening condition); variant absent from gnomAD population databases.

**Population demographics:** Reported cases span multiple ancestries/countries (UK, France, Brazil) with no described ethnic clustering; sex ratio and detailed demographic patterns cannot be meaningfully assessed given the very small published case count.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Blood glucose/HbA1c and insulin/C-peptide levels to establish neonatal (or later-onset) insulin-dependent diabetes.
- Fecal elastase or other exocrine pancreatic function testing for exocrine insufficiency.
- Abdominal ultrasound/MRI/CT to assess pancreatic and gallbladder presence/morphology.

**Imaging:**
- Prenatal ultrasound can detect semilobar HPE (as in the fetal case, PMID:35481434) and, less reliably, pancreatic agenesis.
- Postnatal brain MRI is the primary tool for HPE subtype classification (alobar/semilobar/lobar/middle interhemispheric variant), documenting findings such as absent interhemispheric fissure, fused frontal lobes, absent septum pellucidum, absent frontal horns, absent sylvian fissures.
- Abdominal imaging (ultrasound/MRI) to confirm pancreatic agenesis/hypoplasia and gallbladder agenesis.

**Biopsy/pathology:** Fetal/perinatal autopsy with neuropathological and whole-body (including pancreatic) examination has been diagnostically pivotal in at least one case, revealing total pancreatic agenesis not otherwise apparent, which then guided targeted genetic testing (PMID:35481434: "The fetal autopsy that revealed the pancreas agenesis was crucial in guiding the genetic diagnosis").

**Genetic testing:**
- **Recommended approach:** Given the extreme genetic heterogeneity of both HPE (SHH, ZIC2, SIX3, GLI2, FGF8, FGFR1, DISP1, DLL1, CNOT1, and others) and syndromic pancreatic agenesis (PDX1, PTF1A, RFX6, GATA6, GATA4, CNOT1, ONECUT1, ZNF808), **whole exome sequencing (WES)** is the diagnostic approach that has identified all reported HPE12 cases to date (all cases in the reviewed literature were solved via WES, not single-gene or panel testing).
- **Targeted single-gene testing** for the recurrent c.1603C>T (p.Arg535Cys) variant is feasible once WES/panel testing establishes the diagnosis in a family, useful for prenatal testing of subsequent pregnancies (recurrence risk primarily from potential parental gonadal mosaicism).
- **Chromosomal microarray/karyotype:** Recommended as first-tier/parallel testing to exclude the many chromosomal causes of HPE (e.g., trisomy 13, 18p deletion), since CNOT1-HPE12 is clinically indistinguishable from other monogenic/chromosomal HPE forms without genetic confirmation.
- **Gene panels:** HPE-focused or neonatal-diabetes-focused NGS panels that include CNOT1 (e.g., Genomics England PanelApp "Holoprosencephaly – NOT chromosomal" and "Neonatal diabetes" panels both list CNOT1).

**Clinical criteria:** No formal consensus diagnostic criteria specific to HPE12 exist; diagnosis rests on the combination of (1) HPE on neuroimaging/pathology and (2) molecular confirmation of the CNOT1 c.1603C>T variant, with pancreatic agenesis/neonatal diabetes as a strongly supportive but not obligate additional feature.

**Differential diagnosis:**
- Other monogenic HPE (SHH, ZIC2, SIX3, GLI2 — account for >15% of all HPE combined) and chromosomal HPE.
- Other syndromic pancreatic agenesis genes: **PDX1** and **PTF1A** (biallelic, recessive; complete pancreatic agenesis without HPE), **GATA6** (heterozygous; most common single-gene cause of pancreatic agenesis, broad phenotypic spectrum including cardiac and hepatobiliary defects but not HPE), **GATA4**, **RFX6**, **ONECUT1**, **ZNF808** (Mitchell-Riley syndrome — pancreatic/intestinal atresia, gallbladder anomalies, but distinct from HPE).
- Mitchell-Riley syndrome (ZNF808) can mimic overlapping gallbladder/pancreatic features but lacks the HPE component.

**Screening:** No population-level screening program exists (ultra-rare, non-founder condition). Given the Queiroz Júnior et al. 2024 finding, the authors specifically recommend that individuals confirmed to carry the p.Arg535Cys variant **without** pancreatic agenesis at birth undergo ongoing diabetes surveillance through childhood/adolescence.

---

## 11. Outcome/Prognosis

**Survival and mortality:** Formal survival statistics are not available given the extremely small published cohort. Broader HPE literature documents very high embryonic/fetal lethality for HPE overall (explaining the much higher prevalence in aborted/stillborn cohorts than live births), and one reported HPE12 pregnancy in the literature reviewed here ended in medical termination following prenatal diagnosis of semilobar HPE and (at autopsy) pancreatic agenesis (PMID:35481434) — reflecting both the severity some families face and an ascertainment bias toward the most severe end of the phenotypic spectrum in autopsy-based case identification.

**Morbidity/function:** Surviving individuals face lifelong insulin dependence and pancreatic enzyme replacement (universal need in those with pancreatic agenesis), variable neurodevelopmental impairment/intellectual disability correlating with HPE severity, and possible sensorineural hearing loss. No formal disability/QoL outcome instruments have been applied.

**Disease course:** Chronic, lifelong management is required for the endocrine (diabetes) and exocrine (malabsorption) pancreatic insufficiency; the structural brain anomaly is static but its neurodevelopmental sequelae persist throughout life.

**Complications:** Diabetic complications (as for any insulin-dependent diabetes, with the added challenge of very early/neonatal onset management), malnutrition/growth failure from unrecognized exocrine insufficiency, and standard HPE-associated complications (seizures, hypothalamic-pituitary dysfunction, feeding difficulties) are plausible by analogy to other HPE causes, though not specifically quantified for CNOT1-HPE12 in the literature reviewed.

**Prognostic factors:** Presence/severity of HPE (alobar > semilobar > lobar in terms of typical severity in HPE generally) is the strongest predictor of neurodevelopmental outcome; presence of pancreatic agenesis versus preserved-but-eventually-failing pancreatic function (the adolescent-onset case) predicts timing of diabetes onset and management complexity.

---

## 12. Treatment

There is no disease-modifying or curative therapy; management is **entirely supportive/replacement-based**, directed at the organ-specific consequences.

**Pharmacotherapy:**
- **Insulin therapy** for neonatal/early-onset (or later adolescent-onset) insulin-dependent diabetes mellitus — required from diagnosis (day 1 of life in most reported cases) and lifelong.
  - Suggested MAXO/NCIT: treatment_term NCIT:C15986 (Pharmacotherapy) + therapeutic_agent CHEBI (insulin, e.g., CHEBI:145810 or a specific insulin analog CHEBI term).
- **Pancreatic enzyme replacement therapy (PERT)** for exocrine pancreatic insufficiency — required from diagnosis, lifelong, for those with pancreatic agenesis/severe hypoplasia.
  - Suggested treatment_term: NCIT:C15986 (Pharmacotherapy) or a specific "pancreatic enzyme replacement" NCIT/MAXO term if available.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy has been developed or trialed for CNOT1-HPE12 — the underlying molecular lesion (a scaffold-protein missense variant altering transcriptional repression) is not currently druggable.

**Surgical/interventional:** Not typically indicated for the core lesion; management is medical. Cholecystectomy is not applicable (gallbladder is congenitally absent, not diseased).

**Supportive/rehabilitative care:**
- Nutritional support/monitoring given IUGR/low birth weight and malabsorption risk (MAXO:0000088, dietary intervention).
- Developmental/early intervention services, physical/occupational/speech therapy as indicated by neurodevelopmental impairment (MAXO:0000011 physical therapy; MAXO:0001351 occupational therapy; MAXO:0000930 speech therapy).
- Hearing aid/audiologic management for documented hearing loss (MAXO:0009030 hearing aid usage; MAXO:0000950 supportive care).
- Genetic counseling for families (MAXO:0000079 genetic counseling), given the AD inheritance pattern with (empirically low but non-zero) recurrence risk from potential parental germline mosaicism.

**Experimental treatments:** None identified in ClinicalTrials.gov specific to this ultra-rare molecular diagnosis.

**Treatment outcomes:** No systematic treatment-response data exist beyond standard-of-care diabetes and exocrine-insufficiency management outcomes seen in other causes of neonatal diabetes/pancreatic agenesis.

**Treatment strategy:** Multidisciplinary — pediatric endocrinology (diabetes management), gastroenterology/nutrition (exocrine insufficiency), neurology/developmental pediatrics (HPE-related neurodevelopmental care), audiology, clinical genetics, and (prenatally) maternal-fetal medicine for counseling around a prenatally suspected diagnosis.

---

## 13. Prevention

**Primary prevention:** None possible for the de novo genetic lesion itself; there are no known modifiable risk factors.

**Secondary prevention/early detection:**
- Prenatal ultrasound detection of HPE (as demonstrated in the fetal case) can prompt targeted prenatal genetic testing (chromosomal microarray + WES) if a familial variant is not already known, or targeted variant testing if a parent is a known (rare, since virtually all cases are de novo) carrier.
- Newborn screening for neonatal diabetes (via clinical presentation/hyperglycemia rather than a dedicated screening assay) leads to early diagnosis and insulin initiation, critical given onset as early as day 1 of life.

**Genetic counseling:** Recurrence risk counseling for families of an affected child should reflect the de novo, non-recurring nature of virtually all reported cases, while still acknowledging a small residual empiric recurrence risk from possible parental germline mosaicism (as for other de novo AD disorders) — prenatal testing (chorionic villus sampling/amniocentesis) for the specific familial variant can be offered in a subsequent pregnancy.

**Prenatal diagnosis/family planning:** Once a familial CNOT1 p.Arg535Cys variant is confirmed, targeted prenatal testing is feasible for future pregnancies; preimplantation genetic testing (PGT-M) is theoretically applicable though not specifically reported in the literature reviewed.

**Public health/prophylaxis:** Not applicable — this is a private, sporadically occurring monogenic disorder, not a population-level public-health target.

---

## 14. Other Species / Natural Disease

**Taxonomy:** Studied in **house mouse (*Mus musculus*, NCBITaxon:10090)**. No naturally occurring veterinary disease or spontaneous animal model of CNOT1-HPE12 has been reported; the only animal data are from an engineered (CRISPR-generated) knock-in mouse model.

**Breed:** Not applicable (no companion-animal disease reported).

**Orthologous gene:** Mouse *Cnot1* (MGI:2442402); the p.Arg535Cys-equivalent knock-in was engineered directly in mouse using CRISPR to model the human variant (PMC6506862).

**Natural disease in other species:** None documented (no OMIA entry or veterinary case reports identified).

**Comparative biology:** The residue affected by the human pathogenic variant is described as conserved "from humans to *C. elegans*," indicating deep evolutionary conservation of this region of CNOT1, consistent with its core scaffolding role in the CCR4-NOT complex across metazoans.

**Transmission:** Not applicable (non-infectious, non-zoonotic genetic disorder).

---

## 15. Model Organisms

**Primary model — CRISPR knock-in mouse (*Cnot1* p.Arg535Cys):**
- **Model type:** Mammalian, genetic knock-in (point mutation engineered by CRISPR to recapitulate the exact human variant), MGI:2442402 (*Cnot1* gene page).
- **Heterozygous mice:** Born at lower-than-expected Mendelian frequency but with **no obvious overt phenotype** — mirroring the viability of heterozygous human carriers.
- **Homozygous mice:** **Embryonic lethal after E14.5.** Phenotypes at E14.5 included:
  - Neurological: exencephaly (p = 3.2×10⁻⁹), spina bifida (p = 0.027)
  - Ocular: eye defects including coloboma (p = 5.5×10⁻⁸)
  - Systemic: edema (p = 2.6×10⁻⁷)
  - Pancreatic: significantly reduced pancreatic size, predominantly affecting the dorsal pancreas (High-Resolution Episcopic Microscopy volumetric analysis, p < 10⁻¹⁰), with altered gene expression (increased *Shh*; decreased *Pdx1*, *Ins*, *Hnf1b*, *Ptf1a*; unchanged *Gata6*, *Rxra*).
- **Phenotype recapitulation:** The homozygous mouse model recapitulates the **pancreatic hypoplasia/agenesis and neural-tube/forebrain-relevant malformation spectrum** of the human disease, though the mouse phenotype (exencephaly, spina bifida, coloboma) is broader than classic holoprosencephaly per se and is only seen in the biallelic (homozygous) state, whereas humans are affected as heterozygotes — an important **species-dosage discrepancy**: human disease is dominant/heterozygous, but the mouse model shows overt structural phenotype only in the homozygous state, with heterozygous mice appearing grossly normal apart from sub-Mendelian survival. This is a candidate `HUMAN_MODEL_MISMATCH` consideration for dismech curation — the mouse heterozygote does not reproduce the human heterozygous phenotype, and the homozygous mouse phenotype (exencephaly/spina bifida/coloboma) is not a precise phenocopy of human semilobar/lobar HPE.
- **Model limitations:** No mouse model exists for the human heterozygous state's structural HPE; the pancreatic and gene-expression data are the most directly translatable finding. No single-cell, spatial transcriptomic, or organoid model of this specific variant has been published. No zebrafish, *Drosophila*, *C. elegans*, or iPSC/organoid model specific to this CNOT1 variant was identified in this search (despite deep evolutionary conservation of the affected residue).

**Applications:** The mouse model has been used to establish causality (confirming the human variant is sufficient to produce a pancreatic/neural developmental phenotype), to define the affected developmental window (embryonic lethality after E14.5), and to generate the mechanistic hypothesis of SHH-pathway dysregulation via altered pancreatic gene expression.

**Resources:** MGI:2442402 (*Cnot1* mouse gene page, informatics.jax.org).

---

## Summary for Knowledge-Base Curation

This is an ultra-rare (n≈6 published individuals), fully monogenic, autosomal dominant, always-de-novo disorder caused by a single recurrent *CNOT1* missense variant (p.Arg535Cys) that converges mechanistically on **SHH pathway dysregulation** — placing it naturally alongside the classical SHH/ZIC2/SIX3/GLI2 monogenic HPE genes for pathophysiology modeling, while its **dual-organ (forebrain + pancreas)** phenotype and proposed **stem-cell-differentiation-maintenance mechanism** (rather than direct SHH pathway membership) make it mechanistically distinctive. Key curation cautions: (1) very small evidence base — treat phenotype frequencies as provisional; (2) strong mouse/human genotype-phenotype dosage mismatch (heterozygous human disease vs. homozygous-lethal/heterozygous-silent mouse) warrants a `HUMAN_MODEL_MISMATCH` discussion node rather than treating the mouse data as a clean phenocopy; (3) documented incomplete penetrance for the pancreatic-agenesis component specifically (PMID:39149840) is an important nuance for phenotype `frequency:` qualifiers.

**Primary citations:**
- De Franco E, et al. *Am J Hum Genet.* 2019;104(5):985-989. PMID:31006513. DOI:10.1016/j.ajhg.2019.03.018
- Cospain A, et al. *Pediatr Dev Pathol.* 2022;25(5):548-552. PMID:35481434
- Queiroz Júnior AF, et al. *Am J Med Genet A.* 2024. PMID:39149840

Sources:
- [OMIM #618500 — HOLOPROSENCEPHALY 12](https://omim.org/entry/618500)
- [OMIM Clinical Synopsis #618500](https://omim.org/clinicalSynopsis/618500)
- [OMIM *604917 — CNOT1](https://www.omim.org/entry/604917)
- [PMC6506862 — De Franco et al. 2019, full text](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6506862/)
- [PubMed 31006513](https://pubmed.ncbi.nlm.nih.gov/31006513/)
- [PubMed 35481434 — Cospain et al. 2022](https://pubmed.ncbi.nlm.nih.gov/35481434/)
- [PubMed 39149840 — Queiroz Júnior et al. 2024](https://pubmed.ncbi.nlm.nih.gov/39149840/)
- [Orphanet ORPHA:556955 — Pancreatic agenesis-holoprosencephaly syndrome](https://www.orpha.net/en/disease/detail/556955)
- [Orphanet CNOT1 gene page](https://www.orpha.net/en/disease/gene/CNOT1)
- [MalaCards — Holoprosencephaly 12](https://www.malacards.org/card/holoprosencephaly_12_with_or_without_pancreatic_agenesis)
- [ClinicalGenome MONDO:0032787 curation](https://search.clinicalgenome.org/kb/conditions/MONDO:0032787/by-gene)
- [PanelApp Genomics England — CNOT1 (Holoprosencephaly)](https://panelapp.genomicsengland.co.uk/panels/78/gene/CNOT1/)
- [PanelApp Genomics England — CNOT1 (Neonatal diabetes)](https://panelapp.genomicsengland.co.uk/panels/293/gene/CNOT1/)
- [GeneCards — CNOT1](https://www.genecards.org/card/CNOT1)
- [MGI — Cnot1 gene detail](https://www.informatics.jax.org/marker/MGI:2442402)
- [Orioli & Castilla, Epidemiology of holoprosencephaly, PubMed 20104599](https://pubmed.ncbi.nlm.nih.gov/20104599/)
- [PMC6553724 — HPE epidemiology China 2007-2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6553724/)
- [Holoprosencephaly review, MDPI PMC10137117](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137117/)
- [Holoprosencephaly — StatPearls NCBI Bookshelf NBK560861](https://www.ncbi.nlm.nih.gov/books/NBK560861/)
- [GATA6 mutations and pancreatic agenesis spectrum, PMC3581234](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3581234/)
- [CNOT1(800–999) HEAT domain / TTP interaction, PMC11939966](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11939966/)