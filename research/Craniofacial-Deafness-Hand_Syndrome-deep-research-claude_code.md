---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T23:40:27.864459'
end_time: '2026-07-31T23:46:09.676853'
duration_seconds: 341.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Craniofacial-Deafness-Hand Syndrome
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
  num_turns: 33
  total_cost_usd: 2.0894524
  session_id: 8b1fb180-501a-5f87-8315-d35146c73dee
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniofacial-Deafness-Hand Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Craniofacial-Deafness-Hand Syndrome** covering all of the
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

# Craniofacial-Deafness-Hand Syndrome (CDHS): Comprehensive Research Report

*Note on ontology terms: HPO/GO/CL/UBERON/CHEBI/NCIT IDs below are provided as curatorial leads. Per this project's anti-hallucination policy, every term ID and label should be independently confirmed with OAK (`runoak -i sqlite:obo:<ont> info <ID>`) before being written into a KB entry — several are marked "verify" because I could not directly confirm the canonical label text against the ontology in this session.*

---

## 1. Disease Information

**Overview:** Craniofacial-deafness-hand syndrome (CDHS) is an extremely rare autosomal dominant multiple-congenital-anomaly disorder combining (1) a distinctive craniofacial dysmorphism, (2) profound congenital sensorineural hearing loss, and (3) hand/wrist anomalies (ulnar deviation, camptodactyly/flexion contractures of digits 3–5). It is caused by heterozygous mutation of **PAX3** (2q36.1) and is now understood as a severe allelic variant at the same locus responsible for Waardenburg syndrome types 1 and 3 (WS1/WS3) — "Constitutional mutations of PAX3 lead to Waardenburg syndrome (WS) or Craniofacial-deafness-hand (CFDS) syndrome" (per OMIM/PAX3 literature synthesis).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | **#122880** — CRANIOFACIAL-DEAFNESS-HAND SYNDROME; CDHS |
| OMIM (gene) | **\*606597** — PAX3 |
| Orphanet | **ORPHA:1529** |
| MedGen (NCBI) | **C1852510** |
| ICD-10 | Q87.0 (congenital malformation syndromes predominantly affecting facial appearance) — reported value, confirm against your ICD-10 coding source |
| ICD-11 | LD2H.Y (reported) |
| MONDO | Not confirmed in this session — a mapping likely exists (searchable via the OMIM/Orphanet xref); verify with `runoak -i sqlite:obo:mondo` before use |
| HGNC (PAX3) | HGNC:8617 |
| Gene location | 2q36.1 |

**Synonyms:** CDHS; craniofacial–deafness–hand syndrome; Sommer syndrome (informal, after the describing author). Note: MedGen groups PAX3-related concepts (CDHS, WS1, WS3) under a shared gene record — CDHS itself does not carry "WS1/WS3" as true clinical synonyms; it is a **distinct, allelic phenotype**, not a subtype label.

**Evidence base:** This is one of the rarest disorders in the medical literature — derived almost entirely from a handful of individual case/family reports (aggregated disease-level synthesis in OMIM/Orphanet/GeneReviews-adjacent resources is built directly from these same primary reports, not from registries or large cohorts).

---

## 2. Etiology

**Disease causal factor:** CDHS is a monogenic disorder. All confirmed and candidate cases are attributable to heterozygous, typically de novo or dominantly inherited, disruption of **PAX3** — either a missense variant in the paired-domain DNA-binding region, or a genomic deletion encompassing the gene.

**Genetic risk factors:**
- **PAX3 missense mutation, paired domain, N47K (Asn47Lys):** the founding CDHS family (PMID:8664898, Asher et al. 1996, *Human Mutation*). Quote: *"a missense mutation (Asn47Lys) in the paired domain of PAX3"* was found in "a family of three affected individuals with this syndrome, a mother and two children." The authors specifically noted that *"substitution of a basic amino acid for asparagine at residue 47, conserved in all known murine Pax and human PAX genes, appears to have a more drastic effect on the phenotype than missense, frameshift and deletion mutations of PAX3 that cause Waardenburg syndrome type 1"* — i.e., this particular paired-domain lesion is proposed as mechanistically more severe than typical WS1-causing alleles.
- **PAX3 missense variant, paired domain, T31P (p.Thr31Pro; c.A91C):** a novel variant reported in a 2024/2025 case (PMID:39850491, Saenz Hinojosa et al., *Frontiers in Genetics*), also within the conserved paired-box (PB) domain, meeting ACMG pathogenic criteria (PS2, PM1, PM2, PM4, PP3, PP4).
- **~862 kb de novo 2q36.1 deletion encompassing PAX3** (plus CCSC140 and part of SGPP2): reported in a 16-year-old girl with an intermediate WS1/CDHS phenotype (PMID:24839464, Drozniewska et al. 2014, *Molecular Cytogenetics*). This supports haploinsufficiency (loss-of-function/dosage) as a viable CDHS mechanism, not only missense gain-of-severity.
- **Negative-finding case:** a 37-year-old woman with a partially overlapping phenotype (hearing loss + some craniofacial features, but normal hand films/nasal bones and a Mondini cochlear malformation) had **no PAX3 coding mutation** found on full gene sequencing (PMID:18553554, PMC2533638) — heterozygosity for a PAX3 SNP excluded whole-gene deletion, but a partial/regulatory deletion could not be ruled out. This case is best framed as an unresolved WS-spectrum variant rather than confirmed CDHS.

**Environmental / infectious risk factors:** None established or reported. CDHS is a purely monogenic, developmental (neural-crest patterning) disorder with no known environmental, occupational, dietary, or infectious contribution.

**Protective factors:** None reported (genetic or environmental) — expected for an ultra-rare fully penetrant dominant disorder with no population-scale data available.

**Gene–environment interaction:** Not applicable / not studied given the extreme rarity and small number of reported cases.

---

## 3. Phenotypes

CDHS phenotypes cluster into three domains — craniofacial, otologic, and hand/limb — with an emerging fourth (cardiovascular) domain from the most recent case report.

### Craniofacial features
- Flat/depressed facial profile with a **normal calvarium** (distinguishing radiologically from other craniofacial syndromes)
- **Hypertelorism** — suggested term: HP:0000316 Hypertelorism (verify)
- Small, **downslanting palpebral fissures** with an "antimongoloid" slant — suggested term: HP:0000494 Downslanted palpebral fissures (verify)
- **Depressed/absent nasal bridge**, "button tip," slit-like nares, hypoplastic/absent nasal bones (radiographically absent or small nasal bones) — suggested terms: HP:0005280 Depressed nasal bridge; HP:0000463 (verify label) for anteverted/slit nares
- Small, "pursed" mouth
- Maxillary hypoplasia, malar flattening
- Frontal bossing (variably reported)
- Microcephaly (reported in the 2024 case; head circumference 50 cm at age 21 — not part of the original description, so may reflect phenotypic variability or an independent finding)

### Otologic / auditory
- **Profound (or severe) bilateral sensorineural hearing loss**, congenital/present from birth in the classic family; onset at age 8 in the 2024 case (moderate–severe right, profound left) — suggested term: HP:0000407 Sensorineural hearing impairment (verify)
- Frequency: reported in **100% of confirmed cases** to date (small N, so this is a qualitative "always present" observation, not a population-derived percentage)
- Associated inner-ear structural anomaly reported in a WS-spectrum case: Mondini cochlear deformity (1.5 vs normal 2.5 turns) (PMID:18553554) — not established as core CDHS pathology, but illustrative of the PAX3/otic-capsule connection

### Hand / limb
- **Ulnar deviation of the fingers/hand**
- **Camptodactyly / flexion contractures of digits 3, 4, and 5**
- Limited wrist movement; hypoplastic ulnar styloid (radiographic)
- Clinodactyly of the 5th finger; in the 2024 case, additional findings of nail clubbing, increased DIP-joint prominence of digit 5, and increased PIP-joint prominence of digits 2–3 bilaterally
- Suggested terms: HP:0009465 (verify) Ulnar deviation of the hand/fingers; HP:0012385 Camptodactyly

### Other reported (variable / emerging)
- Short stature (158 cm at 21 y in the 2024 case)
- Thoracic asymmetry, shoulder-girdle hypoplasia, kyphoscoliosis, pectus carinatum, bilateral cubitus valgus
- Iris pigmentary anomaly (hypopigmented iris lesion) — note this overlaps with the WS pigmentary spectrum even though CDHS is nominally distinguished from WS by lacking classic pigmentary stigmata (white forelock, heterochromia) in the founding family
- **Patent ductus arteriosus, cardiomegaly, severe pulmonary hypertension, valvular insufficiency** — first reported cardiovascular phenotype in CDHS (PMID:39850491); authors note PAX3's known role in cardiac neural crest and cite the Splotch mouse's persistent-truncus-arteriosus/outflow-tract phenotypes as mechanistic precedent
- Undernutrition (secondary, reported once)

**Age of onset:** Congenital for the craniofacial and hand features; hearing loss present from birth in the original family, but documented as later-onset (age 8) in the 2024 case — suggesting a broader age range than initially appreciated.

**Severity/progression:** Described as **stable** across a 20-year longitudinal follow-up of the original family (PMID:14556253) — "the extended follow-up period allowed observation of phenotype stability across childhood into adulthood." No degenerative/progressive component is described for the core triad; the cardiovascular complication in the 2024 case reflects a previously undiagnosed structural cardiac lesion (PDA) that became symptomatic with age, not a progressive dysplasia.

**Quality of life impact:** Profound congenital deafness is the dominant driver of QoL impact (communication/speech/social development), compounded in the 2024 case by delayed diagnosis, fragmented specialty care, and untreated PDA/pulmonary hypertension leading to significant cardiopulmonary morbidity by young adulthood. No formal EQ-5D/SF-36/PROMIS data exist for this disorder given its rarity.

---

## 4. Genetic / Molecular Information

**Causal gene:** **PAX3** (paired box 3), HGNC:8617, OMIM \*606597, chromosome 2q36.1.

**Variants identified in CDHS to date:**
| Variant | Type | Domain | Case | PMID |
|---|---|---|---|---|
| c.141T>A / N47K (Asn47Lys) | Missense | Paired domain (exon 2) | Founding family (mother + 2 children), 1983/1996/2003 | 8664898, 14556253, 6859126 |
| c.A91C / p.T31P (Thr31Pro) | Missense | Paired box (PB) domain, exon 2 | 21-year-old Ecuadorian male, 2024 | 39850491 |
| ~862 kb deletion at 2q36.1 (whole-gene) | Deletion (de novo, CNV) | Whole gene + CCSC140 + partial SGPP2 | 16-year-old girl, intermediate WS1/CDHS phenotype | 24839464 |
| Full PAX3 coding sequence — no mutation found | N/A (negative) | — | 37-year-old woman, partial phenotype | 18553554 |

**Variant classification (ACMG/AMP, 2024 case, PMID:39850491):** Pathogenic — criteria met: PS2 (de novo, no family history), PM1 (well-established functional domain), PM2 (absent from gnomAD/population databases), PM4 (evolutionarily conserved residue), PP3 (concordant in-silico damage predictions — SIFT 0.015 damaging, PolyPhen-2 1.0 deleterious, MutationTaster 1 disease-causing, PROVEAN −3.13 deleterious, FATHMM −3.43 deleterious), PP4 (phenotype specificity).

**Allele frequency:** Absent from gnomAD / population databases for both missense variants (expected given the extreme rarity and severity of the phenotype).

**Somatic vs. germline:** All reported variants are **germline** — either transmitted (autosomal dominant, the founding family) or de novo (2024 case; 2014 deletion case).

**Functional consequence / mechanism:** PAX3 encodes a paired-box/homeodomain transcription factor with:
- An N-terminal **paired domain (PD)** — two subdomains, PAI and RED, each with helix-turn-helix motifs for sequence-specific DNA binding
- A central **homeodomain (HD)** — three helix-turn-helix subdomains, helix III mediating DNA recognition
- A linker octapeptide motif (HSIDGILS) that recruits transcriptional corepressors
- A C-terminal proline/serine-rich **transactivation domain (TAD)**
- An N-terminal transcriptional repression domain (TRD), function less well characterized

Both confirmed CDHS missense variants (N47K, T31P) map to the **paired domain**, the primary DNA-recognition module — consistent with a model in which specific, severe disruption of paired-domain DNA binding produces a **more drastic phenotype** than the broader spectrum of PAX3 lesions (missense/frameshift/deletion, including whole-gene loss) that typically produce the milder WS1/WS3 phenotype. The 2014 whole-gene-deletion case, however, shows that simple haploinsufficiency can also produce an intermediate/CDHS-leaning phenotype, so the genotype–phenotype correlation is not absolute (as also concluded broadly for PAX3: "little correlation between genotype and phenotype; deletions of the entire PAX3 gene result in phenotypes indistinguishable from those associated with single-base substitutions").

**Modifier genes:** None identified specific to CDHS. (In the 2024 cardiovascular case, extensive sequencing of >100 congenital-heart-disease genes found no additional variant explaining the cardiac phenotype, implicating PAX3 itself in the cardiac finding.)

**Epigenetics / chromosomal abnormalities:** No CDHS-specific epigenetic studies exist. The 2q36.1 deletion case is the only chromosomal-scale lesion reported; standard karyotype is otherwise normal in described cases.

---

## 5. Environmental Information

No environmental, lifestyle, occupational, dietary, or infectious contributing factors have been identified or proposed for CDHS in the literature — consistent with its status as a fully penetrant, single-gene developmental disorder.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed):**
1. **Trigger:** Heterozygous PAX3 lesion disrupting paired-domain DNA binding (missense) or reducing gene dosage (deletion)
2. **Molecular:** Impaired/altered PAX3 transcription-factor activity — loss of normal cooperative transactivation of downstream targets (MITF with SOX10; WNT1, CXCR4, c-RET in neural crest; MYOD/MYF5/DMRT2 in myogenic precursors)
3. **Cellular:** Defective **neural crest cell** induction, survival, migration, and differentiation — PAX3 "orchestrates neural crest-specific gene expression" and promotes neural-crest-cell survival/stress resistance
4. **Tissue:** Disrupted derivatives of the cranial and cardiac neural crest — craniofacial skeleton (absent/hypoplastic nasal bones, midface hypoplasia), inner ear/cochlear melanocytes and structure (sensorineural deafness — PAX3 loss "causes reduction of melanocytes in the developing mouse cochlea," PMC/Nature 2024), limb/hand mesenchyme patterning (ulnar deviation, camptodactyly), and cardiac outflow-tract neural crest (PDA, in the 2024 case)
5. **Organism:** The clinical triad (craniofacial dysmorphism + deafness + hand anomalies), with cardiovascular involvement as an emerging, possibly underrecognized, fourth domain

**Molecular pathways:** PAX3–SOX10–MITF axis (melanocyte specification/melanogenesis); PAX3-driven WNT1/CXCR4/c-RET (neural crest migration); PAX3–MYOD/MYF5 (myogenic specification, less relevant to CDHS's core phenotype but part of PAX3 biology generally).

**Cell types involved:** Cranial neural crest cells, otic/cochlear melanocytes (intermediate cell population of the stria vascularis), craniofacial mesenchyme/osteogenic precursors, cardiac neural crest cells (outflow tract). Suggested CL terms (verify with OAK): CL:0000333 (neural crest cell), CL:0000148 (melanocyte).

**Biological processes:** Neural crest cell migration, craniofacial skeletal morphogenesis, inner ear development, cochlear melanocyte differentiation, cardiac outflow tract morphogenesis. Suggested GO terms (verify): GO:0014032 (neural crest cell development), GO:0042475 (odontogenesis of dentin-containing tooth — not relevant, omit), GO:0060384 (innervation — not directly relevant); more precisely GO:0001755 (neural crest cell migration), GO:0043010 (camera-type eye development — not relevant). Given the specificity needed, curators should search GO directly for "neural crest cell migration," "inner ear morphogenesis," and "cardiac neural crest cell migration."

**Protein dysfunction:** Altered DNA-binding specificity/affinity of the paired domain (missense variants) or simple loss of one functional gene copy (deletion) — both converge on reduced/altered PAX3 transcriptional output during a narrow embryonic window of neural crest patterning.

**Model-system evidence supporting mechanism (not confirmed in CDHS patients directly — flag as model-organism-derived):**
- **Splotch (Sp) mouse** — Pax3 loss-of-function model: dorsal neural tube closure defects (spina bifida, exencephaly), and (per the 2024 CDHS case report's discussion) cardiac neural crest phenotypes including myocardial dysfunction, persistent truncus arteriosus, and outflow-tract malalignment — cited as mechanistic precedent for the patient's PDA/pulmonary hypertension, though the Splotch mouse itself reportedly has **no facial phenotype** (PMID:8421686 and related Pax3/vertebrate-development literature), a notable **human-model mismatch**: PAX3 loss clearly produces craniofacial dysmorphism in humans (WS1/WS3/CDHS) but not in the mouse facial skeleton, indicating species-specific roles for Pax3 in facial neural crest patterning.
- **Mouse cochlea:** Pax3 loss reduces melanocytes in the developing cochlea, supporting the deafness mechanism (Nature Scientific Reports, 2024).

**Molecular profiling (transcriptomics/proteomics/etc.):** No disease-specific -omics datasets exist for CDHS patients; all mechanistic inference is extrapolated from general PAX3 developmental biology and mouse models, not primary human multi-omics data on CDHS cases.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- Craniofacial skeleton (nasal bones, maxilla, malar bones) — primary
- Inner ear / cochlea (sensorineural hearing apparatus) — primary
- Hand/wrist skeleton and soft tissue (ulna, carpal region, digits 3–5) — primary
- Cardiovascular system (ductus arteriosus, pulmonary vasculature) — secondary/emerging, reported in one case
- Ocular (iris pigmentation) — secondary, variably reported
- Axial skeleton (kyphoscoliosis, pectus carinatum) — secondary, reported in one case

**Tissue/cell level:** Craniofacial neural-crest-derived bone and connective tissue; cochlear melanocytes/stria vascularis; limb mesenchyme; cardiac neural crest-derived outflow tract tissue.

**Subcellular level:** Nuclear (PAX3 is a nuclear transcription factor; its dysfunction is a nuclear/transcriptional-regulation defect, not an organelle-level pathology). Suggested GO Cellular Component term: GO:0005634 (nucleus).

**Localization / laterality:** Bilateral and generally symmetric involvement of ears, hands, and facial midline structures; no lateralization pattern reported. Suggested UBERON terms (verify): UBERON:0001691 (nasal bone/nose), UBERON:0001846 (cochlea), UBERON:0002389 (hand), UBERON:0001091 (ulna).

---

## 8. Temporal Development

- **Onset:** Congenital for craniofacial and hand features; hearing loss present from birth in the founding family (later-recognized at age 8 in the 2024 case, possibly reflecting ascertainment/diagnostic delay rather than true later biological onset).
- **Onset pattern:** Present at birth (structural anomalies); the cardiovascular complication in the 2024 case became clinically apparent (dyspnea) only in young adulthood (age 19), following an unaddressed infantile heart murmur — an important "critical period" lesson: early cardiac evaluation in infancy might have altered the outcome.
- **Progression:** Craniofacial/hand phenotype is **stable, non-progressive** over a documented 20-year follow-up. The cardiac lesion (PDA + pulmonary hypertension), left untreated, followed the natural progressive course typical of uncorrected left-to-right shunts (Eisenmenger-type physiology by adulthood).
- **Disease course:** Chronic, lifelong for the core triad; the cardiovascular complication in the one reported case became an unresectable/inoperable chronic condition due to delayed diagnosis.
- **Remission:** Not applicable — structural/developmental anomalies do not remit.
- **Critical periods:** Embryonic neural crest migration (roughly the first trimester) is the presumed critical window for the craniofacial/otic/cardiac neural crest anomalies; infancy is a critical window for hearing-loss detection/intervention and for cardiac murmur follow-up (as the 2024 case explicitly illustrates by its negative example).

---

## 9. Inheritance and Population

**Epidemiology:** Prevalence is reported as **<1 in 1,000,000** (ultra-rare). The disorder has been "described in one family to date" in canonical references (the founding Sommer family), with subsequent isolated case reports (2008, 2014, 2024/2025) expanding the total documented cases to a handful worldwide. This is one of the rarest named Mendelian syndromes in the literature.

**Inheritance pattern:** Autosomal dominant. The founding family showed vertical transmission across two generations (affected mother → affected daughter and, two years later, an affected son — "identical manifestations across three family members spanning two generations"). Other reported cases (2014 deletion, 2024 missense) arose **de novo**.

**Penetrance:** Appears complete in the reported pedigree (all three affected family members show the full triad), though the total pedigree size is too small to estimate penetrance rigorously.

**Expressivity:** Some variability is evident across cases (e.g., presence/absence of cardiovascular involvement, variable craniofacial severity, variable hearing-loss onset age), consistent with variable expressivity typical of PAX3-spectrum disorders.

**Genetic anticipation, germline mosaicism, founder effects, consanguinity:** None reported/applicable — the very small number of families precludes meaningful assessment, and no consanguinity was noted in any reported case (parents in the 2024 case were unaffected and non-consanguineous; same for the 2014 and 2008 cases).

**Carrier frequency:** Not applicable (fully penetrant dominant disorder, not a recessive carrier state).

**Population demographics:** Reported cases span diverse ancestries (the founding family's ancestry is not emphasized in available sources; more recent cases include an Ecuadorian male). No geographic clustering, sex predilection or age-distribution pattern can be established from the very small case series (2 affected females and 2 affected males across all fully described cases, i.e., no clear sex bias but N is far too small to be meaningful).

---

## 10. Diagnostics

**Clinical recognition:** Diagnosis is currently based on the **clinical triad** (distinctive facial dysmorphism + congenital/early sensorineural deafness + hand anomalies), supported by radiographic findings (absent/hypoplastic nasal bones, normal calvarium, hypoplastic ulnar styloid, ulnar deviation of the hand) and then confirmed molecularly.

**Laboratory/imaging tests:**
- Skull/facial radiography — absent or small nasal bones, normal calvarium, small maxilla
- Hand/wrist radiography — ulnar deviation, hypoplastic ulnar styloid, flexion contractures
- Audiometry / ABR — confirms severe-to-profound bilateral sensorineural hearing loss
- Temporal bone CT — can reveal associated inner-ear structural anomalies (e.g., Mondini deformity, sinus hypoplasia in the related WS-spectrum case)
- Echocardiography — recommended given the newly reported PDA/pulmonary hypertension association; the 2024 case authors explicitly argue for **routine cardiac screening** in CDHS given the neural-crest-cardiac link

**Genetic testing:**
- **First-line:** PAX3 single-gene sequencing (all coding exons + flanking intron/exon boundaries) — the approach used in essentially every reported case
- **Deletion/duplication analysis** (chromosomal microarray / CMA) — necessary given the 2014 case's whole-gene deletion mechanism; sequencing alone would have missed this
- **Whole-exome sequencing (WES)** — used in the 2024 case (Illumina NextSeq, GRCh37 reference, GATK4.3 variant calling, ANNOVAR annotation), confirmed by Sanger sequencing; also useful to exclude phenocopies (e.g., the 2024 authors screened >100 congenital heart disease genes to rule out an alternative cardiac explanation)
- NCBI GTR lists PAX3 as the associated gene with **141 available clinical tests** (sequencing, deletion/duplication, targeted variant analysis)

**Clinical criteria / differential diagnosis:** Key differential is **Waardenburg syndrome types 1 and 3** (also PAX3-caused) — CDHS is distinguished by its imaging findings (absent nasal bones, normal calvarium) and distinct facial gestalt, and notably by the **absence of the classic WS pigmentary stigmata** (white forelock, heterochromia iridis, synophrys/dystopia canthorum) in the founding description, although some overlap (e.g., an iris pigmentary lesion) has since been reported. Other differentials include other PAX3-spectrum/2q36.1 microdeletion phenotypes and other craniofacial-limb syndromes (e.g., Nager, Treacher Collins — distinguished by absence of hand ulnar-deviation pattern and different inheritance/gene).

**Screening:** No population screening program exists (ultra-rare disorder); universal newborn hearing screening (as recommended broadly for congenital deafness, including WS-spectrum disorders) would be the relevant entry point for early detection, given deafness is often the most immediately actionable finding.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No mortality data specific to CDHS exist; life expectancy for the core triad (craniofacial + deafness + hand) appears normal absent complications. The one reported cardiovascular case illustrates that **undiagnosed/untreated cardiac involvement can be life-threatening** — by young adulthood the patient had developed severe, inoperable pulmonary hypertension from an unrepaired PDA, a course associated with significant morbidity/mortality risk if untreated in classic PDA natural history.

**Morbidity/function:** Profound deafness is the dominant lifelong functional impact (communication, speech-language development, education, social integration) if not addressed early with hearing aids/cochlear implantation and habilitation. Hand contractures may impair fine-motor function, though the degree of functional hand impairment is not quantified in available reports.

**Complications:** Cardiovascular complications (PDA, pulmonary hypertension, cardiomegaly, valvular insufficiency) — newly recognized, possibly underascertained in earlier cases because cardiac screening was not systematically performed; kyphoscoliosis/thoracic deformity; undernutrition (secondary, one case).

**Prognostic factors:** Timeliness of diagnosis and multidisciplinary care appears to be the dominant modifiable prognostic factor illustrated by the literature — the 2024 case authors explicitly frame their patient's poor cardiovascular outcome as a consequence of **fragmented, non-holistic care** and delayed genetics referral (14+ years from murmur detection to genetic diagnosis), not an inevitable disease course.

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for CDHS — management is entirely supportive/symptomatic, directed at each phenotypic domain.

**Hearing loss management:**
- Hearing aids / cochlear implantation (standard of care for congenital severe-profound SNHL; not explicitly documented as performed in the reported CDHS cases, but standard practice for the WS/PAX3-spectrum)
- Speech-language therapy
- NCIT suggestion: NCIT:C15315 (Rehabilitation), NCIT:C159273 (Speech Therapy) — verify against your NCIT adapter

**Hand anomaly management:**
- Occupational/physical therapy for contractures; surgical release considered case-by-case (not specifically documented in reported CDHS cases)
- NCIT: NCIT:C15302 (Physical Therapy), NCIT:C121351 (Occupational Therapy)

**Cardiovascular management (2024 case, symptomatic/palliative given inoperability from established pulmonary hypertension):**
- **Furosemide** (loop diuretic) — CHEBI: furosemide, CHEBI:47426
- **Bosentan** (dual endothelin-receptor antagonist) — CHEBI:3181 (verify)
- **Enalapril** (ACE inhibitor) — CHEBI:4784 (verify)
- **Sildenafil** (phosphodiesterase-5 inhibitor) — CHEBI:9139 (verify)
- Treatment term: NCIT:C15986 (Pharmacotherapy) for all four; therapeutic_agent bound to the respective CHEBI terms
- The authors explicitly frame this regimen as **not curative** — "aim to manage symptoms rather than provide curative treatment" — because surgical PDA closure was contraindicated by the degree of established pulmonary hypertension (irreversible Eisenmenger-type physiology)

**Surgical:** PDA closure would be first-line **if performed early** (standard congenital cardiology practice), but was deemed unsuitable in the one reported CDHS case due to delayed diagnosis and established severe pulmonary hypertension — an argument for early echocardiographic screening in future CDHS diagnoses.

**Genetic counseling:** Recommended given autosomal dominant inheritance with a 50% transmission risk to offspring of an affected individual; molecular confirmation in a family enables predictive testing of at-risk relatives (extrapolated from general PAX3/WS management guidance, e.g., GeneReviews' Waardenburg Syndrome Type I chapter, PMID/NBK1531).

**Experimental / clinical trials:** None identified — no ClinicalTrials.gov entries specific to CDHS were located; the extreme rarity precludes trial-based development.

**Treatment strategy / personalized medicine:** The clearest actionable lesson from the literature is procedural rather than pharmacological: **early, coordinated multidisciplinary evaluation** (genetics, audiology, cardiology, orthopedics) at diagnosis, rather than isolated single-specialty management — explicitly the central argument of the most recent (2024) case report.

---

## 13. Prevention

- **Primary prevention:** Not applicable — CDHS arises from de novo or inherited single-gene mutation; there is no known modifiable risk factor to prevent occurrence.
- **Secondary prevention:** Early recognition of the craniofacial-hand phenotype should prompt (a) immediate audiologic evaluation/newborn hearing screening and (b) — based on the 2024 case's central lesson — **routine echocardiographic screening**, given the emerging cardiac neural-crest association, even though this is based on a single case to date.
- **Genetic counseling / reproductive options:** Standard autosomal dominant counseling (50% recurrence risk per pregnancy for an affected parent); prenatal or preimplantation genetic testing would be technically feasible once a familial PAX3 variant is identified, though not documented as having been used in any reported CDHS family.
- **Screening programs:** No CDHS-specific screening program exists; universal newborn hearing screening (a general public-health measure, not CDHS-specific) is the most relevant existing infrastructure that would flag an affected infant.

---

## 14. Other Species / Natural Disease

No naturally occurring CDHS-equivalent disease has been reported in any non-human species. PAX3 orthologs are highly conserved (mouse *Pax3*, and Pax3 orthologs across vertebrates), and **Waardenburg-like pigmentary/deafness phenotypes are well documented in animals with PAX3-pathway disruption** (e.g., naturally occurring white-spotting/deafness phenotypes in some mammals are linked to MITF-pathway genes, of which PAX3 is an upstream regulator), but no natural veterinary case has been specifically characterized as a CDHS analog (i.e., with the combined craniofacial + deafness + hand/limb triad). This is an evidence gap, not a documented negative finding — it likely reflects the extreme rarity and specificity of the human phenotype rather than true absence of comparable biology in other species.

---

## 15. Model Organisms

**Mouse — Splotch (Sp) mutant, Pax3 loss-of-function:**
- Classic neural tube defect model: exencephaly and spina bifida from failure of dorsal neural tube closure, with severity increasing along the rostrocaudal axis (PMID:8421686 and related Pax3/vertebrate development literature)
- Splotch mice additionally show **cardiac neural crest phenotypes** — myocardial dysfunction, persistent truncus arteriosus, and cardiac outflow-tract malalignment — cited by the 2024 CDHS case-report authors as the mechanistic precedent for their patient's PDA/pulmonary hypertension
- **Important human-model mismatch:** Splotch mice reportedly have **no facial phenotype**, whereas human PAX3 loss-of-function clearly causes craniofacial dysmorphism (WS1/WS3/CDHS) — indicating the facial neural-crest role of Pax3 is not fully recapitulated in this mouse model, and caution is warranted before extrapolating mouse craniofacial findings (or their absence) to human CDHS.
- Persistent Pax3 expression (gain-of-function) in neural crest causes cleft palate and defective osteogenesis in mice (JCI, PMID referenced above) — relevant to understanding dosage sensitivity of PAX3 in craniofacial development, though this is the opposite direction of the presumed CDHS mechanism.

**Mouse — cochlear melanocyte studies:** Pax3 loss reduces melanocytes in the developing mouse cochlea (Scientific Reports, 2024), supporting a melanocyte-dependent mechanism for the sensorineural hearing loss common to PAX3-spectrum disorders including CDHS.

**Zebrafish/medaka:** Pax3 and Pax7 function combinatorially with Mitf to generate melanophores/xanthophores (bioRxiv 2023) — general PAX3-pathway biology, not CDHS-specific.

**Applications/limitations:** No mouse or other model has been engineered to carry the specific CDHS-associated paired-domain alleles (N47K, T31P) or has recapitulated the full human CDHS triad (craniofacial + deafness + hand). All model-organism evidence cited in CDHS discussions is **extrapolated from general Pax3 loss-of-function biology**, not validated against the specific human CDHS variants — this represents a genuine translational/model-fidelity gap worth flagging explicitly (a `HUMAN_MODEL_MISMATCH`-type gap, in dismech schema terms) rather than treating mouse Pax3 data as direct confirmation of CDHS mechanism.

---

## Summary of Key Evidence Gaps

1. **No MONDO ID confirmed** in this session — needs direct OAK/MONDO lookup.
2. **No dedicated GeneReviews chapter** for CDHS exists (only for Waardenburg Syndrome Type I) — CDHS content must be synthesized from OMIM/Orphanet/primary case reports, as done here.
3. **Extremely small evidence base** (≈4–5 total published cases/families across >40 years) — essentially every quantitative claim (prevalence, penetrance, sex ratio) is a qualitative impression from a handful of individuals, not a population statistic.
4. **Cardiovascular association is single-case evidence** (PMID:39850491) — real but not yet independently replicated; should be curated as an emerging/tentative association, not an established core phenotype.
5. **No confirmed CDHS-specific animal model** — all mechanistic model-organism support is inferential from general Pax3 biology, with an explicit facial-phenotype mismatch between mouse (Splotch, no facial phenotype) and human (craniofacial-dominant phenotype) PAX3 loss-of-function.

---

### Primary Citations (PMID)
- 6859126 — Sommer, 1983, original description
- 8664898 — Asher et al., 1996, N47K PAX3 missense mutation
- 14556253 — Sommer et al., 2003, 20-year follow-up ("revisited")
- 18553554 — Gad et al./PMC2533638, 2008, WS-spectrum case, no PAX3 mutation found
- 24839464 — Drozniewska et al., 2014, 862 kb 2q36.1 deletion case
- 39850491 — Saenz Hinojosa et al., 2024/2025, PAX3 T31P + PDA/pulmonary hypertension case
- 8421686 — Splotch mouse Pax3 intron-3 splicing mutation

Sources:
- [OMIM #122880 — CRANIOFACIAL-DEAFNESS-HAND SYNDROME; CDHS](https://omim.org/entry/122880)
- [OMIM *606597 — PAX3](https://www.omim.org/entry/606597)
- [Orphanet: Craniofacial-deafness-hand syndrome (ORPHA:1529)](https://www.orpha.net/en/disease/detail/1529)
- [PubMed 8664898 — Missense mutation in the paired domain of PAX3 causes craniofacial-deafness-hand syndrome](https://pubmed.ncbi.nlm.nih.gov/8664898/)
- [PubMed 14556253 — Craniofacial-deafness-hand syndrome revisited](https://pubmed.ncbi.nlm.nih.gov/14556253/)
- [PubMed 6859126 — Previously undescribed syndrome of craniofacial, hand anomalies, and sensorineural deafness](https://pubmed.ncbi.nlm.nih.gov/6859126/)
- [PMC11754966 / Frontiers in Genetics — Case Report: Craniofacial deafness hand syndrome with unusual cardiovascular symptoms](https://pmc.ncbi.nlm.nih.gov/articles/PMC11754966/)
- [PMC2533638 — Sensorineural Deafness, Distinctive Facial Features and Abnormal Cranial Bones: a New Variant of Waardenburg Syndrome?](https://pmc.ncbi.nlm.nih.gov/articles/PMC2533638/)
- [PMC4023700 — PAX3 gene deletion detected by microarray analysis in a girl with hearing loss](https://pmc.ncbi.nlm.nih.gov/articles/PMC4023700/)
- [PAX3: A Driver of Normal Development and Disease (PMC13024339)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13024339/)
- [NCBI GTR — Craniofacial-deafness-hand syndrome (C1852510)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1852510/)
- [GARD/NIH — Craniofacial-deafness-hand syndrome](https://rarediseases.info.nih.gov/diseases/1571/craniofacial-deafness-hand-syndrome)
- [NORD — craniofacial-deafness-hand syndrome](https://rarediseases.org/mondo-disease/craniofacial-deafness-hand-syndrome/)
- [Waardenburg Syndrome Type I — GeneReviews (NBK1531)](https://www.ncbi.nlm.nih.gov/books/NBK1531/)
- [Cellular mechanisms underlying Pax3-related neural tube defects and their prevention by folic acid (PMC6899032)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6899032/)
- [Loss of Pax3 causes reduction of melanocytes in the developing mouse cochlea (Scientific Reports)](https://www.nature.com/articles/s41598-024-52629-9)