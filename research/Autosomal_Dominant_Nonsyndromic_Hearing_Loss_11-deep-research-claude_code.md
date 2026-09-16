---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T15:16:37.725868'
end_time: '2026-08-27T15:20:41.275261'
duration_seconds: 243.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 11
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
  num_turns: 30
  total_cost_usd: 1.1702818000000004
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 2
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:32097363
  relevance_assessed: 10
  on_topic: 7
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 11
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 11** covering all of the
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

# Autosomal Dominant Nonsyndromic Hearing Loss 11 (DFNA11): Comprehensive Research Report

## 1. Disease Information

**Overview:** Autosomal Dominant Nonsyndromic Hearing Loss 11 (DFNA11; also written "Deafness, Autosomal Dominant 11") is a form of progressive, postlingual sensorineural hearing loss caused by heterozygous (dominant) pathogenic variants in *MYO7A*, the gene encoding unconventional myosin VIIa. It is one of three distinct clinical phenotypes produced by *MYO7A* mutations, situated at the mild end of the *MYO7A* disease spectrum: DFNA11 (dominant, nonsyndromic) < DFNB2 (recessive, nonsyndromic) < Usher syndrome type 1B (USH1B; recessive, syndromic — deafness plus retinitis pigmentosa and vestibular areflexia) ([OMIM #601317](https://omim.org/entry/601317); [NIH GTR C1832475](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1832475/)).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | #601317 |
| OMIM (gene, *MYO7A*) | *276903 |
| Allelic OMIM phenotypes | DFNB2 #600060; Usher syndrome 1B #276900 |
| MONDO | MONDO:0011032 |
| MedGen | C1832475 |
| HGNC (gene) | HGNC:7606 (*MYO7A*) |
| UniProt | Q13402 (MYO7A_HUMAN) |
| Gene location | 11q13.5 |

**Synonyms:** Deafness, autosomal dominant 11; DFNA11; MYO7A-related nonsyndromic hearing loss (dominant form); myosin VIIA-associated deafness.

**Evidence basis:** Data on DFNA11 derive almost entirely from aggregated multi-generational pedigrees and clinical case series (audiometric cohort studies, family linkage studies) rather than large EHR-based population datasets, reflecting its rarity — it is described as "the rarest consequence of *MYO7A* variants" relative to DFNB2 and USH1B (Joo et al. 2022, PMID: 35453549).

---

## 2. Etiology

**Disease causal factors:** DFNA11 is purely genetic/monogenic — caused by heterozygous, typically missense or in-frame deletion, pathogenic variants in *MYO7A* acting via a dominant mechanism (see Mechanism, below). No environmental or infectious causal factors are described for this specific dominant condition (as opposed to acquired/environmental sensorineural hearing loss more broadly).

**Genetic risk factors:**
- Causal variants: heterozygous missense and small in-frame deletion variants in *MYO7A*, clustering predominantly in the **motor domain** (aa 65–741) and, less commonly, the **MyTH4** (aa 1017–1253, 1747–1895) and **IQ motif/coiled-coil** regions. In a Korean cohort, motor-domain variants accounted for 66.7% (12/18) of DFNA11 variants identified (Joo et al. 2022, PMID: 35453549).
- All reported autosomal dominant *MYO7A* variants in this cohort were missense or in-frame deletions — no truncating/nonsense variants were dominant-acting, consistent with a gain-of-function/dominant-activation mechanism rather than simple haploinsufficiency (see Mechanism).
- Representative pathogenic variants: p.Arg853His (Kubota et al. 2020, PMID: 32097363); p.Arg244Pro-adjacent motor-domain variants; p.Thr1234Ser and p.Pro1244Arg in MyTH4 (associated with earlier-onset, more severe phenotypes) (PMID: 35453549); a missense variant in the motor head domain reported in a separate DFNA11 family (PMC3558421).

**Environmental risk factors:** Not specifically implicated in DFNA11; as with other progressive sensorineural hearing losses, noise exposure is generically counseled against to avoid accelerating any residual hearing decline, though this is extrapolated from general ADNSHL management guidance rather than DFNA11-specific data.

**Protective factors:** No genetic or environmental protective factors specific to DFNA11 have been identified in the literature reviewed.

**Gene-environment interactions:** None specifically documented for DFNA11.

---

## 3. Phenotypes

**Primary phenotype — Sensorineural hearing loss (symptom/clinical sign):**
- **Onset:** Postlingual — after complete speech acquisition, "often in the first decade of life" per OMIM, though other cohorts describe onset in the second decade or later (second–fifth decade for motor-domain variants) (Joo et al. 2022, PMID: 35453549; malacards/OMIM #601317).
- **Severity:** Mild to moderate at onset in most families; can progress to severe (Kubota 2002, PMID: 11889386, describes "moderate cochlear hearing loss beginning in the second decade"). MyTH4-domain variants are associated with more severe/profound loss (PMID: 35453549).
- **Progression:** Gradual, progressive, affecting all frequencies over time. A detailed multi-generational study (Kim et al. 2020, PMID: 32097363) found audiometric configuration evolves with age: a "gently sloping configuration" in early childhood transitioning to a "flat configuration" after age 30; high-frequency thresholds deteriorate slowly while low-frequency thresholds, though affected later, "progressed more rapidly" once involved. Abnormal distortion product otoacoustic emissions (DPOAEs) were detectable **before** standard pure-tone threshold elevation in some subjects, suggesting DPOAE as a potential early/preclinical biomarker.
- **Laterality:** Bilateral.
- Suggested HP term: **HP:0000407** (Sensorineural hearing impairment) or more specific **HP:0000408** (Progressive sensorineural hearing impairment); **HP:0000360** (Hearing impairment, general).

**Vestibular dysfunction (secondary/variable phenotype):**
- Variably present; described as "mild" or "asymptomatic" vestibular dysfunction in some series (OMIM #601317) while a separate large-pedigree study found vestibular function "remained normal across all tested subjects" (PMID: 32097363) — indicating inter-family variability. When present, severity of vestibular impairment appears to parallel severity of the auditory phenotype within a family.
- Suggested HP term: **HP:0000762** (Vestibular hypofunction) or **HP:0000740**/HP:0002321 (Vertigo).

**Absent phenotypes (distinguishing DFNA11 from allelic conditions):** No retinal degeneration/retinitis pigmentosa — this is the key clinical distinguishing feature versus USH1B (OMIM #601317; PMID: 11889386). Suggested negated term: absence of **HP:0000510** (Rod-cone dystrophy).

**Quality of life impact:** Not separately quantified for DFNA11 in the literature surveyed; general ADNSHL guidance notes progressive postlingual hearing loss affects communication, education (if pediatric onset), and social functioning, with hearing aids/cochlear implants indicated for functional impact management (PMC10296186).

**Frequency among affected individuals:** As an autosomal dominant condition, all variant carriers are expected to develop hearing loss (segregation in described pedigrees is consistent with high penetrance), though age of onset and severity are variable even within families.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MYO7A* (HGNC:7606; OMIM *276903), chromosome 11q13.5, spans ~87 kb genomic sequence, 49 exons (48 coding). Encodes myosin VIIa, a 254 kDa, 2,215-amino-acid unconventional myosin motor protein (UniProt Q13402) (PMID: 35453549 domain data).

**Protein domain architecture** (from Joo et al. 2022, PMID: 35453549):
- **Motor domain** (aa 65–741): ATP- and actin-binding; site of majority of DFNA11 variants
- **Neck domain** (aa 745–857): five IQ motifs (calmodulin-binding lever arm)
- **SAH domain** (aa 858–935): single alpha-helix, lever-arm extension
- **Coiled-coil region**: between SAH and tail
- **Tail domain**: two MyTH4 domains (aa 1017–1253; 1747–1895), two FERM domains (aa 1258–1602; 1900–2205), one SH3 domain (aa 1603–1672)
- MYO7A functions as a monomer (unlike many conventional myosins), with the tail folding back onto the head-neck region in an autoinhibited state.

**Variant classification and type:** DFNA11 variants are exclusively missense or small in-frame deletions (never truncating) — consistent with the requirement for a stably folded, dominantly acting mutant protein (PMID: 35453549). By contrast, DFNB2 (recessive) alleles retain partial function and localize correctly to stereocilia, while USH1B alleles are typically more severely disruptive (often null/truncating) and fail to localize properly — "DFNB2 and USH1B are different ends of the same disease spectrum" (search synthesis referencing GeneReviews/PreventionGenetics data).

**Allele frequency:** Population-level allele frequency data specific to DFNA11-causing variants were not identified in gnomAD searches during this review; as private/family-specific dominant missense variants, they are expected to be rare/absent in gnomAD population databases, consistent with pathogenicity assessment under ACMG/AMP criteria (PM2).

**Functional consequence — dominant mechanism:** A 2024–2025 mechanistic study (bioRxiv 10.1101/2024.09.17.613491; PubMed: 39345484, "Select autosomal dominant DFNA11 deafness mutations activate Myo7A targeting in epithelial cells") reports that **many DFNA11-patient mutations activate Myo7A targeting/trafficking** in epithelial cell assays — i.e., these variants relieve the normal autoinhibited (folded-back) conformation of the myosin, causing constitutive activation/mistargeting of the motor protein. This provides a mechanistic explanation for dominant inheritance: rather than simple haploinsufficiency, mutant Myo7A is hyperactive/mistargeted, which is proposed to interfere with normal mechanotransduction complex assembly or tip-link tensioning in a dominant-negative or gain-of-function manner. A companion structure-function study found that specific IQ motifs within the myosin's lever arm regulate this targeting, at least partly independent of tail sequence.

**Modifier genes:** A genetic modifier of DFNA11 audiometric phenotype (affecting low- and mid-frequency thresholds) has been sought in linkage studies (Naz et al., PMID: 18667942, "In search of the DFNA11 myosin VIIA low- and mid-frequency auditory genetic modifier"), indicating intrafamilial phenotypic variability may be partly modifier-gene-driven, though the specific modifier locus was not conclusively identified in the search results retrieved.

**Epigenetic information:** No DFNA11-specific epigenetic (DNA methylation/histone) data were identified.

**Chromosomal abnormalities:** DFNA11 is caused by point/small indel variants, not large chromosomal rearrangements; no aneuploidy/translocation mechanism is described.

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious causal or exacerbating factors for DFNA11 were identified in the literature surveyed — it is a purely monogenic dominant condition. General noise-avoidance counseling applies as standard practice for progressive sensorineural hearing loss but is not DFNA11-specific evidence.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Molecular trigger:** Heterozygous missense/in-frame-deletion variant in *MYO7A*, predominantly in the motor domain, alters normal myosin VIIa autoregulation.
2. **Molecular dysfunction:** Mutant Myo7A protein shows **activated/constitutive targeting** rather than normal regulated (autoinhibited) trafficking, per epithelial-cell reporter assays (bioRxiv 2024.09.17.613491 / PubMed 39345484). This is distinct from the loss-of-targeting seen in USH1B-causing alleles.
3. **Cellular/subcellular dysfunction:** Myosin VIIa normally functions at the **stereocilia upper tip-link density (UTLD)** of cochlear hair cells, where a cluster of ~8+ Myo7A molecules maintains **tip-link tension** at rest and is required for hair-cell mechanoelectrical transduction (MET) — specifically for maintaining resting open probability of MET channels and enabling proper onset kinetics of MET currents (Nature Communications 2020, PMID: 32350269; PNAS 2024, "MYO7A is required for the functional integrity of the mechanoelectrical transduction complex in hair cells of the adult cochlea"). MYO7A also participates in **ankle-link positioning** in the stereocilia bundle and co-localizes with PDZD7 at the ankle-link region (eLife 2016, PMC5005036).
4. **Consequence in DFNA11:** Dysregulated/dominantly acting mutant myosin disrupts normal tip-link tensioning and MET complex integrity in a dose-dependent, progressive manner — producing progressive loss of MET current and progressive threshold elevation, without the profound congenital dysfunction and stereocilia disorganization seen in USH1B (where myosin VIIa is essentially non-functional/mislocalized).
5. **Tissue-level consequence:** Progressive cochlear hair cell (particularly stereocilia bundle) dysfunction across the cochlear frequency map, manifesting audiometrically as the age-dependent shift from sloping to flat threshold configuration described clinically (PMID: 32097363).
6. **Organism-level consequence:** Progressive, postlingual, bilateral sensorineural hearing loss, with variable, generally milder vestibular involvement than in USH1B (reflecting that the vestibular hair cell MET/tip-link apparatus is less severely affected by the "activating" dominant variants than by the loss-of-function USH1B alleles).

**Cell types involved:** Cochlear inner and outer hair cells (auditory); vestibular hair cells (variably, for the vestibular component). Suggested CL term: **CL:0000855** (sensory hair cell) / **CL:0002620** (skeletal muscle satellite — N/A) — more precisely **CL:0000201** (auditory hair cell) if available in the ontology used, or UBERON-anchored hair cell terms.

**Biological processes:** Suggested GO terms:
- **GO:0007605** (sensory perception of sound)
- **GO:0060088** (auditory receptor cell stereocilium organization)
- **GO:0036158** (outer dynein arm assembly — N/A, not relevant) — more appropriately **GO:0032420** (stereocilium) as a cellular component and **GO:0060113** (inner ear receptor cell differentiation)
- Molecular function: **GO:0003774** (cytoskeletal motor activity) / **GO:0000146** (microfilament motor activity, actin-based motor)

**Protein dysfunction category:** Altered regulation/autoinhibition (a form of activating/gain-of-function dysregulation) rather than classic loss-of-function or aggregation-based misfolding — distinguishing DFNA11's mechanism from typical dominant-negative structural-protein diseases.

**Subcellular localization (GO Cellular Component):** Stereocilia (**GO:0032420**, stereocilium; specifically the upper tip-link density region of the stereocilium tip).

**Not applicable/not identified in this review:** No specific immune-system involvement, no described metabolic pathway alterations, and no transcriptomic/proteomic/metabolomic/lipidomic profiling datasets specific to DFNA11 human hair cells were identified (human inner-ear tissue is inherently difficult to biopsy, so most molecular profiling in this field derives from animal/organoid models rather than human patients).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary organ: **Inner ear** — specifically the **cochlea** (organ of Corti) for the hearing phenotype, and the **vestibular labyrinth** (semicircular canals, utricle, saccule) for the variable vestibular phenotype.
- Body system: Auditory/vestibular sensory system (special senses).
- No other organ systems are affected — this distinguishes nonsyndromic DFNA11 from syndromic USH1B (which additionally involves the retina).
- Suggested UBERON terms: **UBERON:0001846** (cochlea), **UBERON:0002105** (vestibular organ) / **UBERON:0009038** (vestibular labyrinth), **UBERON:0000030** (sensory system, general).

**Tissue/cell level:**
- Sensory epithelium of the organ of Corti — inner hair cells and outer hair cells and their stereociliary bundles.
- Suggested Cell Ontology term: cochlear hair cell (best available CL term for auditory hair cells; e.g., **CL:0000201**, "auditory hair cell").

**Subcellular level:**
- **Stereocilia** (actin-based mechanosensory protrusions on the hair-cell apical surface) — the principal subcellular site of Myo7A dysfunction.
- The **tip link** and **upper tip-link density (UTLD)**, a specialized subdomain at the stereocilium tip.
- Suggested GO Cellular Component terms: **GO:0032420** (stereocilium), **GO:0032421** (stereocilium bundle), **GO:0002131** (stereocilium tip [if present in ontology]).

**Localization:** Bilateral, symmetric involvement of both cochleae (and both vestibular labyrinths when vestibular dysfunction is present) — no lateralization pattern is described.

---

## 8. Temporal Development

**Onset:** Postlingual — after speech has been acquired. Reports vary: OMIM describes onset "often in the first decade of life"; other cohort/pedigree studies describe onset in the second decade (Kubota et al., PMID: 11889386) through the second-to-fifth decade depending on the specific variant/domain affected (motor-domain variants: later onset, second–fifth decade; MyTH4-domain variants: earlier onset, teens–20s) (Joo et al. 2022, PMID: 35453549).

**Onset pattern:** Insidious/gradual rather than acute or episodic.

**Progression:** Slowly progressive at high frequencies initially; low frequencies become involved later but then progress more rapidly once affected (PMID: 32097363). Audiometric configuration evolves over decades from sloping (childhood) to flat (after age ~30).

**Disease course pattern:** Progressive, not relapsing-remitting or episodic. No spontaneous remission is described.

**Disease duration:** Chronic and lifelong/progressive — hearing loss does not resolve and is expected to continue worsening with age.

**Critical periods / early biomarker window:** Abnormal DPOAEs can be detected before conventional audiometric threshold shifts, suggesting a preclinical detection window that could inform earlier monitoring or intervention timing (PMID: 32097363).

---

## 9. Inheritance and Population

**Epidemiology:**
- Hearing loss overall affects approximately **1–3 per 1,000 live births**, with more than half attributable to genetic causes.
- Non-syndromic hearing loss is predominantly autosomal recessive (75–80% of Mendelian cases); autosomal dominant nonsyndromic hearing loss (ADNSHL, the DFNA category) accounts for roughly **20%** of nonsyndromic hereditary hearing loss cases; X-linked accounts for 2–5%, mitochondrial ~1%.
- Within ADNSHL specifically, **46 causative genes** have been identified to date, of which *MYO7A* (DFNA11) is one.
- DFNA11 is explicitly characterized as "the rarest consequence of the *MYO7A* gene variant" relative to DFNB2 and USH1B — i.e., among the three *MYO7A*-associated phenotypes, dominant DFNA11 is the least frequently observed clinically (Joo et al. 2022, PMID: 35453549, synthesis).
- In a large post-lingual ADNSHL diagnostic cohort (Korea), *MYO7A*/DFNA11 variants were identified in 2.0% (6/300) of families overall and 4.1% (6/148) of multiplex families (PMID: 35453549).

**Inheritance pattern:** Autosomal dominant.

**Penetrance:** Appears high/complete within described pedigrees (all variant carriers develop hearing loss), though formal penetrance estimates were not located in this review.

**Expressivity:** Variable — age of onset, severity, audiometric configuration, and presence/absence of vestibular involvement vary between and within families, correlating in part with which protein domain is affected (motor vs. MyTH4 vs. IQ/coiled-coil) (PMID: 35453549).

**Genetic anticipation:** Not described for DFNA11 (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for DFNA11 in this review.

**Founder effects:** Not specifically documented for DFNA11 variants in the sources reviewed (contrast with some *MYO7A*-DFNB2/USH1B populations where founder alleles are described in specific ethnic groups, e.g., South African and Chinese cohorts).

**Carrier frequency:** As an autosomal dominant condition with (presumably) private family-specific variants, a general population "carrier frequency" concept (as used for recessive disease) is not applicable in the same way; rather, prevalence reflects de novo occurrence plus transmission within affected pedigrees.

**Consanguinity role:** Not relevant to this dominant condition (relevant instead to the recessive DFNB2/USH1B end of the *MYO7A* spectrum).

**Population demographics:** DFNA11 has been reported in diverse populations including Dutch, Japanese, Korean, and Chinese pedigrees, without an established predominant ethnic enrichment specific to the dominant (as opposed to recessive) phenotype, based on the geographic spread of cited cohort studies.

**Sex ratio:** No sex-specific skewing is described — consistent with autosomal (non-X-linked) inheritance.

---

## 10. Diagnostics

**Clinical tests:**
- **Pure-tone audiometry:** primary diagnostic tool; characteristic evolving configuration (sloping → flat) with age, as described above.
- **Distortion product otoacoustic emissions (DPOAE):** identified as potentially useful for **early/preclinical detection**, showing abnormalities before conventional threshold elevation in some DFNA11 subjects (PMID: 32097363).
- **Vestibular function testing** (e.g., caloric testing, vestibular-evoked myogenic potentials/VEMP, video head-impulse testing): used to characterize the variable vestibular component; results are family-specific (normal in some pedigrees, abnormal in others).
- **Ophthalmologic examination (including electroretinography):** important to formally exclude retinitis pigmentosa/USH1B, given allelism at the *MYO7A* locus — a normal ERG supports the nonsyndromic DFNA11 diagnosis over USH1B.

**Genetic testing:**
- Diagnosis is established by identifying a heterozygous pathogenic/likely pathogenic *MYO7A* variant, typically via **next-generation sequencing (NGS) hearing-loss gene panels**, **whole-exome sequencing**, or **single-gene *MYO7A* sequence analysis**, in the context of a family history consistent with autosomal dominant inheritance and a characteristic audioprofile.
- GTR (Genetic Testing Registry) lists 37 clinical tests for this condition, including 31 sequence-analysis tests of the entire coding region, 23 deletion/duplication analyses, 4 targeted variant analyses, and 1 select-exon sequence analysis (NIH GTR C1832475).
- Chromosomal microarray, karyotyping, and mitochondrial DNA testing are not primary diagnostic modalities for this single-gene point-variant disorder.

**Differential diagnosis:** Other ADNSHL genes (e.g., *COCH*/DFNA9, *WFS1*, *MYO6*, *MYO15A*, *NCOA3*), age-related hearing loss, noise-induced hearing loss, and — critically — USH1B (must be excluded via ophthalmologic/ERG evaluation given allelic overlap at *MYO7A*) and DFNB2 (excluded by dominant vs. recessive family segregation pattern).

**Screening:** Newborn hearing screening (universal, non-gene-specific) would detect congenital/early hearing loss but DFNA11's typically postlingual onset means it is more often identified through childhood/young-adult audiometric surveillance in known-affected families plus cascade genetic testing once a familial variant is identified. At-risk relatives can be tested to guide early monitoring (annual audiograms are recommended for progression tracking in ADNSHL generally).

---

## 11. Outcome/Prognosis

**Survival/mortality:** DFNA11 is not associated with increased mortality — it is an isolated sensory (auditory ± vestibular) disorder with no systemic organ involvement.

**Morbidity/function:** Progressive bilateral sensorineural hearing loss leading, over decades, to moderate-to-severe (and potentially profound in some MyTH4-variant cases) hearing impairment; functional impact centers on communication and, if vestibular involvement is present, balance/gait.

**Disease course/complications:** No systemic complications are described. The main "complication" is progression to a degree of hearing loss requiring amplification or cochlear implantation.

**Recovery potential:** Hearing loss is not reversible without intervention (hearing aids/cochlear implant); there is no evidence of spontaneous recovery.

**Prognostic factors:** Domain of the causative variant appears prognostic — motor-domain variants are associated with later onset, milder severity, and slower progression, while MyTH4-domain variants are associated with earlier onset, greater severity, and more rapid progression (PMID: 35453549). Abnormal DPOAE prior to threshold shift may serve as an early prognostic/monitoring biomarker (PMID: 32097363).

---

## 12. Treatment

DFNA11 has no gene-specific or disease-modifying pharmacotherapy; management is supportive/rehabilitative, following general ADNSHL practice:

- **Hearing aids** — for mild-to-moderate hearing loss (amplification). Suggested NCIT term: consider a general audiologic rehabilitation/hearing-aid-fitting procedure term if present in NCIT (no MAXO/NCIT-specific "hearing aid" clinical-action term is confirmed to exist per this repository's own documented gap — see CLAUDE.md note on lack of an NCIT equivalent for hearing-aid usage).
- **Cochlear implantation** — considered when hearing loss progresses to severe-to-profound levels; NCIT candidate: **NCIT:C15329** (Surgical Procedure) as the closest general clinical-action term, or a more specific cochlear-implantation term if available in NCIT.
- **Hybrid (electro-acoustic) devices** — combining acoustic amplification for residual low-frequency hearing with electrical stimulation for high-frequency loss, relevant given DFNA11's sloping-then-flat audiometric evolution.
- **Genetic counseling** — NCIT:C15240 (Genetic Counseling); important for informing at-risk relatives, given autosomal dominant transmission (~50% risk to offspring of an affected individual) and variable expressivity.
- **Audiologic surveillance** — at least annual audiograms recommended to track progression; DPOAE monitoring may allow earlier detection of decline (PMID: 32097363).
- **Noise avoidance counseling** — to minimize any additional/superimposed noise-induced component to the progressive genetic loss (general ADNSHL guidance, PMC10296186).

**Experimental/advanced therapeutics:** No DFNA11-specific gene therapy trials were identified. However, the allelic and mechanistically related USH1B (severe *MYO7A* loss-of-function) has active preclinical and early clinical gene-therapy development that is instructive for the broader *MYO7A* therapeutic landscape:
- **Dual-AAV8(Y733F) vector delivery of full-length *MYO7A* cDNA** (split into 5′/3′ halves due to the ~6.7 kb cDNA exceeding single-AAV packaging capacity) has shown improved vestibular hair-cell stereocilium morphology and vestibular function in the shaker-1 (USH1B) mouse model, though cochlear stereocilia organization and auditory function were not similarly rescued (Molecular Therapy Methods & Clinical Development, 2023).
- A Phase 1/2 human trial of dual-AAV *MYO7A* delivery to the retina in USH1B patients ("UshTher") was designed but was placed on hold after Sanofi withdrew from the program in December 2018; the sponsor sought an out-licensing partner as of February 2019.
- Third-generation lentiviral gene therapy (UshStat, EIAV-based) has also been studied preclinically in the shaker-1 mouse model.
- These approaches target loss-of-function USH1B alleles and are not directly applicable to DFNA11's proposed dominant-activation mechanism, which would more likely require an allele-specific knockdown or gene-silencing (rather than gene-replacement) strategy if a targeted therapy were pursued — though no such DFNA11-specific therapeutic program was identified in this review.

**Personalized medicine:** Not currently applicable beyond domain-based prognostic counseling (motor vs. MyTH4 variant location informing expected course, per PMID: 35453549).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the sense of preventing occurrence of a germline dominant variant; genetic counseling and reproductive options (e.g., preimplantation genetic testing) can be discussed with affected families who wish to reduce transmission risk, though this is standard ADNSHL counseling rather than DFNA11-specific literature.
- **Secondary prevention:** Early identification via audiometric (and potentially DPOAE) surveillance in known-affected families/genetically confirmed carriers, enabling earlier fitting of amplification devices and earlier educational/communication support.
- **Tertiary prevention:** Avoidance of additional noise exposure to prevent superimposed noise-induced threshold shifts; prompt escalation from hearing aids to cochlear implantation as thresholds decline, to minimize functional/communicative morbidity.
- **Genetic/carrier screening:** Cascade testing of at-risk relatives once a familial *MYO7A* variant is identified; prenatal/preimplantation genetic testing is an option for informed families given the well-defined dominant Mendelian pattern.
- **Public health/behavioral/immunization/prophylaxis:** Not applicable — DFNA11 is not preventable by vaccination, environmental intervention, or prophylactic medication.

---

## 14. Other Species / Natural Disease

**Taxonomy:** Mouse (*Mus musculus*, NCBITaxon:10090) and zebrafish (*Danio rerio*, NCBITaxon:7955) are the principal model species; no naturally occurring companion-animal or wildlife DFNA11-equivalent disease was identified in this review (note: some veterinary myosin-related deafness models exist for other myosin genes, but not specifically an autosomal dominant *Myo7a* condition analogous to DFNA11).

**Orthologous gene:** Mouse *Myo7a* (MGI ortholog of human *MYO7A*); zebrafish *myo7aa* (and paralog *myo7ab*).

**Comparative biology:** The mouse and zebrafish *Myo7a*-null/loss-of-function models (below) primarily recapitulate the **USH1B/DFNB2 end** of the phenotypic spectrum (profound congenital deafness plus vestibular dysfunction, with only mild/attenuated retinal phenotypes in mouse and zebrafish compared to human USH1B). A model specifically representing the **dominant, activating DFNA11 mechanism** (as opposed to loss-of-function) was not identified in the literature surveyed — this is a modeling gap, since the shaker-1 and mariner models are loss-of-function (recessive-equivalent), not dominant-activating alleles.

**Transmission/zoonotic potential:** Not applicable — this is a non-infectious, monogenic disorder.

---

## 15. Model Organisms

**Mouse — Shaker-1 (sh1):**
- The first identified USH locus model (1995); a spontaneous nonsense mutation in *Myo7a*.
- Phenotype: profound, lifelong deafness; vestibular dysfunction manifesting as head-tossing and circling behavior; disorganized cochlear hair-cell stereocilia; only minor/mild retinal defects are observed despite the human USH1B phenotype including significant retinitis pigmentosa — a notable **human-model translational mismatch** for the retinal component.
- Represents the **severe loss-of-function end** of the *Myo7a* spectrum (USH1B-like), not the dominant-activating DFNA11 mechanism.
- AAV-mediated *Myo7a* rescue (dual-AAV8(Y733F)) in shaker-1 mice improves vestibular hair-cell stereocilium morphology and vestibular function (reduced circling, improved VsEP thresholds) but does not similarly rescue cochlear stereocilia organization or auditory function — indicating differential rescuability of vestibular versus auditory hair cells.

**Zebrafish — *myo7aa* mariner mutant:**
- Ernest et al. (2000) described a *myo7aa* premature-stop-codon zebrafish model of USH1B; homozygous mutants show circular swimming, defective balance, morphological/functional inner-ear hair-cell defects, and absence of the acoustic startle response.
- *myo7aa⁻/⁻* zebrafish also show mild photoreceptor degeneration and reduced electroretinographic responses (PMID: 24698764), again modeling USH1B rather than DFNA11 specifically.
- A more recent study (Frontiers in Molecular Neuroscience, 2024) implicates zebrafish *myo7aa* in congenital hearing via Rho-GTPase signaling regulation, adding a signaling-pathway dimension to the mechanistic picture.

**Cell-based/epithelial models:** Heterologous expression systems (e.g., kidney epithelial cell lines such as MDCK-type cells) have been used to directly test **DFNA11 patient-derived missense variants** for their effect on Myo7A subcellular targeting/trafficking, providing the closest available model to the dominant DFNA11 mechanism itself (bioRxiv 2024.09.17.613491 / PubMed 39345484) — these assays found that DFNA11 mutations activate (rather than abolish) Myo7A targeting, distinguishing the cellular mechanism from the USH1B mistargeting phenotype.

**Model limitations:** No available animal model directly and specifically recapitulates the dominant, gain-of-function/activating DFNA11 mechanism in vivo (as opposed to the standard loss-of-function shaker-1/mariner alleles) — an important **human-model mismatch** to flag for any DFNA11 knowledge-base entry: existing *Myo7a* animal models are informative for general hair-cell MET biology and for the USH1B/DFNB2 severe end of the spectrum, but their applicability to DFNA11's proposed dominant-activation mechanism and its comparatively mild, slowly progressive phenotype is not established.

**Resources:** MGI (Mouse Genome Informatics) for shaker-1 allele records; ZFIN for zebrafish *myo7aa* mariner allele records; IMSR/EMMA for repository access to *Myo7a* mouse strains.

---

## Summary of Key Primary Citations

| Citation | Topic |
|---|---|
| Liu et al., *Nat Genet* 1997;17:268–269 (PMID: 9354784) | Original identification of *MYO7A* mutation causing autosomal dominant nonsyndromic deafness (DFNA11) |
| Weil et al., *Nat Genet* 1997;16:191–193 | *MYO7A* as allelic cause of DFNB2/USH1B |
| Kubota et al. 2002 (PMID: 11889386) | Phenotype of DFNA11: moderate cochlear hearing loss from second decade, variable vestibular dysfunction, no retinal degeneration |
| Naz et al. 2008 (PMID: 18667942) | Search for DFNA11 low/mid-frequency genetic modifier |
| Kim et al. 2020 (PMID: 32097363) | Clinical profile across ages in a large DFNA11 family; DPOAE as early marker; p.Arg853His variant |
| Joo et al., *Biomedicines* 2022;10(4):798 (PMID: 35453549) | Domain-specific genotype-phenotype correlations (motor vs. MyTH4 vs. IQ/coiled-coil) across DFNA11/DFNB2/USH1B |
| bioRxiv 10.1101/2024.09.17.613491 (PubMed: 39345484) | Mechanistic study: DFNA11 mutations activate Myo7A targeting in epithelial cells |
| Nature Communications 2020 (PMID: 32350269) | Myosin-VIIa tensions the hair-cell mechanotransduction complex |
| eLife 2016 (PMC5005036) | PDZD7–MYO7A complex at stereocilia ankle-link region |
| PNAS 2024/2025 | MYO7A required for MET complex integrity in adult cochlear hair cells |

---

## Notes on Information Gaps

- Direct OMIM #601317 full-text clinical synopsis and the primary GeneReviews *MYO7A* chapter could not be fetched directly (403/cookie-wall errors); content above synthesizes OMIM/GTR summaries obtained via search snippets and secondary sources, and should be cross-checked against the primary OMIM clinical synopsis and GeneReviews "MYO7A-Related Hearing Loss and Retinitis Pigmentosa" chapter when curating a formal knowledge-base entry.
- No gnomAD constraint metrics (pLI/LOEUF/missense Z) specific to *MYO7A* were retrieved in this pass; these should be pulled directly from gnomAD for the knowledge-base entry.
- No dedicated DFNA11 prevalence/incidence rate (cases per 100,000) was located; only the general ADNSHL proportion (~20% of nonsyndromic hereditary hearing loss) and MYO7A's cohort-level diagnostic yield (2.0–4.1% of postlingual ADNSHL families in one Korean cohort) are available as proxies.
- The mechanistic bioRxiv paper (39345484) appears to have been a preprint at the time of search; verify final peer-reviewed publication status/PMID before final curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32097363` *(abstract only)*: "remained normal across all tested subjects"
  - closest text in source: "Vestibular function was within the normal range in all the subjects tested"