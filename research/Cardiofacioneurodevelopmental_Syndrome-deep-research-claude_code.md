---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T09:35:31.586194'
end_time: '2026-08-01T09:53:10.150078'
duration_seconds: 1058.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cardiofacioneurodevelopmental Syndrome
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
  web_search_requests: 10
  num_turns: 70
  total_cost_usd: 5.277999499999998
  session_id: dbcd44e7-7d9a-4b56-b6c1-bff8340e1fac
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiofacioneurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiofacioneurodevelopmental Syndrome** covering all of the
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

# Comprehensive Research Report: Cardiofacioneurodevelopmental Syndrome (CFNDS)

**Prepared:** 2026-08-01 · **Target entity:** Cardiofacioneurodevelopmental syndrome · **MONDO:0030873** · **Gene: CCDC32**

---

## ⚠️ Named Entity Confusion (NEC) Preflight — READ FIRST

This disease name is a **high NEC risk**. During the very first literature sweep, search engines returned **cardiofacio*cutaneous* syndrome (CFC)** results for "cardiofacio*neuro*developmental syndrome." These are entirely different entities:

| | **Cardiofacioneurodevelopmental syndrome (CFNDS)** — the target | **Cardiofaciocutaneous syndrome (CFC)** — NOT the target |
|---|---|---|
| OMIM | 619123 | 115150 / 615278 / 615279 / 615280 |
| MONDO | MONDO:0030873 | MONDO:0015280 (and type-specific) |
| Gene(s) | **CCDC32** (15q15.1) | BRAF, MAP2K1, MAP2K2, KRAS |
| Inheritance | **Autosomal recessive** | Autosomal dominant (de novo) |
| Mechanism | AP-2 adaptor assembly / clathrin-mediated endocytosis (± ciliogenesis) | RAS-MAPK hyperactivation (RASopathy) |
| Hallmark | Bilateral cleft lip and palate + DD | Ectodermal/cutaneous findings, HCM, pulmonic stenosis |

**Identity anchors verified for this report** (all three concordant, per the CLAUDE.md NEC preflight):
- **Gene check:** MedGen/MONDO/ClinGen all name **CCDC32** as the sole causal gene; every primary paper retrieved reports CCDC32.
- **OMIM check:** MONDO:0030873 carries xref `OMIM:619123`, matching the OMIM entry title "CARDIOFACIONEURODEVELOPMENTAL SYNDROME; CFNDS."
- **Synonym check:** MONDO:0030873 exact synonym = "CFNDS" only. No competing entity claims this acronym.

**Also do not confuse with:** cardioacrofacial dysplasia 1 (CAFD1, OMIM 619142), MRFACD (OMIM 616789), or craniofrontonasal syndrome — all surfaced as near-neighbours in searches.

---

## ⚠️ Evidence-Base Caveat (critical for curation scope)

**CFNDS is an ultra-rare, recently delineated disorder with a total published cohort of approximately six living individuals plus one terminated fetus, from five families.** Nearly every quantitative statement in this report rests on n ≤ 6. Section-level "not available" markers below are frequent and are **real absences of data**, not search failures.

The Human Phenotype Ontology annotation set for OMIM:619123 is derived from a **single publication (PMID:32307552) describing two individuals** — so every HPO frequency below is `n/2`. Treat these as presence/absence observations, not population frequencies.

**Snippet-verification note:** Full abstracts for PMID:32307552 and PMID:35451546 below are verbatim from the Europe PMC REST API and are safe candidates for evidence snippets. Quotes drawn from PMC **full text** (marked *[full text]*) were extracted through a summarizing fetch layer and **must be re-verified with `just fetch-reference` + `just validate-references` before being committed as evidence snippets.**

---

## 1. Disease Information

### Overview

Cardiofacioneurodevelopmental syndrome (CFNDS) is an autosomal recessive multiple-congenital-anomaly syndrome caused by biallelic loss-of-function variants in *CCDC32*. Its recognized core is **global developmental delay plus bilateral cleft lip and palate**, with a variable constellation of craniofacial dysmorphism, congenital heart disease, hindbrain (cerebellar vermian) hypoplasia, microcephaly, digital/nail anomalies, postnatal growth restriction, and — in one individual — laterality disturbance (abdominal situs inversus with asplenia).

The MedGen/OMIM clinical definition:

> "Characterized by microcephaly, midline facial defects, developmental delay, and cerebellar hypoplasia. Variable cardiac defects may be present, including atrioventricular canal and ventricular septal defects. Heterotaxy has also been reported."
> — MedGen UID 1721861

Abdalla et al. proposed the two-feature core:

> "We describe a core phenotype comprising developmental delay and bilateral cleft lip and palate in the three individuals with CFNDS."
> — PMID:35451546 (verbatim, abstract)

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0030873** (label: "Cardiofacioneurodevelopmental syndrome"; exact synonym "CFNDS") |
| **OMIM (phenotype)** | **619123** |
| **OMIM (gene)** | **618941** (*CCDC32*) |
| **MedGen** | UID 1721861 |
| **UMLS** | C5436852 |
| **Orphanet** | **No ORPHA code identified.** Direct Orphanet query returned no matching entry; MONDO:0030873 carries no Orphanet xref. Flag as an ontology-coverage gap. |
| **ICD-10** | No specific code. Best fits **Q87.8** (other specified congenital malformation syndromes NEC). No dedicated code assigned. |
| **ICD-11** | No specific code. Best fits **LD2F.1Y** / LD2F (other specified syndromes with multiple structural anomalies). Not formally assigned. |
| **MeSH** | No dedicated descriptor. Indexed under MeSH terms of the source papers: *Craniofacial Abnormalities*, *Heart Defects, Congenital*, *Neurodevelopmental Disorders*, *Ciliopathies*, *Cleft Lip*, *Cleft Palate*, *Loss of Function Mutation*. |
| **GARD** | Not identified. |
| **ClinGen** | Gene-disease validity curated (see §4). |

### Synonyms / alternative names

- CFNDS (standard abbreviation)
- CCDC32-related cardiofacioneurodevelopmental syndrome (usage in Albuainain et al. 2026, PMID:41639596)
- CCDC32 deficiency / CCDC32-related syndrome (informal)
- Historical gene alias in older literature: **C15orf57**-related syndrome

### Provenance of information

**Entirely aggregated disease-level and case-level literature.** All data derive from individual published case reports and one review; there is **no EHR-derived cohort, no patient registry, no natural-history study, and no biobank cohort** for CFNDS. No ICEES/COHD-style co-occurrence data exist for this entity (it has no ICD code to key on).

---

## 2. Etiology

### Disease causal factors

**Purely monogenic and germline.** CFNDS is caused by **biallelic (homozygous, in all published families) loss-of-function variants in *CCDC32***. No environmental, infectious, or acquired etiology is known or plausible.

> "Using whole exome sequencing, we identified homozygous frameshift *CCDC32* variants in three affected individuals."
> — PMID:32307552 (verbatim, abstract)

All reported probands to date are **homozygous**, arising in the context of **parental consanguinity** in at least two of the founding families. Compound heterozygosity is theoretically expected but has not yet been reported.

### Risk factors

**Genetic (causal):**
- Biallelic *CCDC32* LoF variants (frameshift, whole-gene/multi-exon deletion, nonsense) — see §4.
- **Carrier parents** (obligate heterozygotes are unaffected; no heterozygous phenotype reported).

**Non-genetic modifier of risk:**
- **Consanguinity** is the dominant epidemiological risk factor, as for essentially all ultra-rare AR disorders. Family A was a consanguineous **Arab Muslim** pedigree (first cousins once removed); Family B a consanguineous **Iranian (Isfahan)** pedigree *[PMC7268788, full text]*.
- **Founder/population endogamy** may explain the apparently recurrent large deletion allele (§4).

**Environmental risk factors: none identified.** No toxin, teratogen, maternal exposure, occupational, dietary, or lifestyle risk factor has been implicated. Given complete genetic determinism at the causal level, none is expected.

**Age / sex / family history:** Disease is congenital; sex distribution is unremarkable in the tiny cohort (roughly balanced). Family history of consanguinity or an affected sib is the actionable risk signal.

### Protective factors

**None identified.** No protective allele, modifier allele, or environmental protective factor has been reported. gnomAD contains no reported homozygous LoF individuals that would suggest incomplete penetrance or a protective background.

### Gene–environment interactions

**None identified.** No GxE data exist for CFNDS. CTD contains no CCDC32–chemical–disease interaction of relevance to this phenotype.

**Curation note / open question:** Harel et al. explicitly raised **genetic modifiers** as a candidate explanation for the incomplete ciliopathy phenotype (absence of cystic kidney disease and polydactyly), citing possible "cis/trans genetic interactions" *[PMC7268788, full text]*. This is an appropriate `KNOWLEDGE_GAP` discussion item.

---

## 3. Phenotypes

### 3.1 HPO annotation set (authoritative, from HPOA)

Retrieved from the HPO API for OMIM:619123. **Sole annotation source: PMID:32307552** (2 individuals). Frequencies are literal patient counts.

| HP ID | Label | Freq | HPO organ system |
|---|---|---|---|
| HP:0001263 | Global developmental delay | 2/2 | Nervous system |
| HP:0000252 | Microcephaly | 2/2 | Head and neck |
| HP:0410030 | Cleft lip | 2/2 | Head and neck |
| HP:0000175 | Cleft palate | 2/2 | Head and neck |
| HP:0000411 | Protruding ear | 2/2 | Ear |
| HP:0004209 | Clinodactyly of the 5th finger | 2/2 | Limbs |
| HP:0008872 | Feeding difficulties in infancy | 2/2 | Digestive |
| HP:0003577 | Congenital onset | 2/2 | Clinical course |
| HP:0001320 | Cerebellar vermis hypoplasia | 1/1 | Nervous system |
| HP:0000028 | Cryptorchidism | 1/1 | Male-specific |
| HP:0006695 | Atrioventricular canal defect | 1/2 | Cardiovascular |
| HP:0001629 | Ventricular septal defect | 1/2 | Cardiovascular |
| HP:0001642 | Pulmonic stenosis | 1/2 | Cardiovascular |
| HP:0001746 | Asplenia | 1/2 | Cardiovascular |
| HP:0003363 | Abdominal situs inversus | 1/2 | Digestive |
| HP:0000316 | Hypertelorism | 1/2 | Eye |
| HP:0000601 | Hypotelorism | 1/2 | Eye |
| HP:0000582 | Upslanted palpebral fissure | 1/2 | Head and neck |
| HP:0000347 | Micrognathia | 1/2 | Head and neck |
| HP:0001156 | Brachydactyly | 1/2 | Limbs |
| HP:0012385 | Camptodactyly | 1/2 | Connective tissue |
| HP:0008386 | Aplasia/Hypoplasia of the nails | 1/2 | Skin, hair, nails |
| HP:0007477 | Abnormal dermatoglyphics | 1/2 | Skin, hair, nails |
| HP:0002808 | Kyphosis | 1/2 | Skeletal |
| HP:0000007 | Autosomal recessive inheritance | — | Inheritance |

**Note the hypertelorism/hypotelorism split (1/2 each)** — this is genuine phenotypic discordance between the two index patients, not an annotation error: Individual A-II-1 had **hypotelorism**, Individual B-II-1 had **hypertelorism** *[PMC7268788, full text]*. This is mechanistically interesting (both are midline-patterning readouts in opposite directions) and worth a curation note.

### 3.2 Additional phenotypes from later reports (not yet in HPOA)

Suggested HPO terms below were **verified against OLS**:

| HP ID | Label | Source | Notes |
|---|---|---|---|
| HP:0001249 | Intellectual disability | PMID:35451546 | 9-y-o girl, Abdalla patient |
| HP:0002079 | Hypoplasia of the corpus callosum | PMID:35451546 | "Brain imaging disclosed hypoplastic corpus callosum" |
| HP:0000405 | Conductive hearing impairment | PMID:35451546 | Bilateral |
| HP:0004322 | Short stature | PMID:35451546 | |
| HP:0012110 | Hypoplasia of the pons | PMID:32307552 (fetus A-II-2) | *[full text]* |
| HP:0001321 | Cerebellar hypoplasia | PMID:41639596 | Review-level phenotype statement |
| HP:0000286 | Epicanthus | PMID:32307552 | Individual B-II-1 *[full text]* |
| HP:0000752 | Hyperactivity | PMID:32307552 | Individual B-II-1 *[full text]* |

Additional descriptive features from full text, without a crisply matching specific HP term, best captured as free-text `preferred_term` on a broader parent: *stiff upper lip*, *vaulted palate*, *underdeveloped helices*, *broad nasal root*, *prominent large nose*, *nail clubbing*, *small hands and feet*, *abnormal cisterna magna*, *missing teeth* (HP:0000670 Carious teeth / HP:0000668 Hypodontia — **verify against the exact clinical description before assigning**).

### 3.3 Phenotype characteristics

**Type distribution:** Predominantly **congenital structural malformations** (craniofacial, cardiac, CNS, limb) plus **neurodevelopmental/behavioral** features. There are **no reported disease-specific laboratory abnormalities** — no biomarker, no metabolic derangement, no characteristic biochemical signature. This is important: CFNDS has **no biochemical diagnostic handle**.

**Age of onset:** **Congenital (HP:0003577), 2/2.** Structural anomalies are present prenatally — the terminated fetus A-II-2 was ascertained on prenatal imaging with bilateral cleft lip, vermian hypoplasia, hypoplastic pons, and abnormal cisterna magna *[PMC7268788, full text]*. Developmental delay declares itself in infancy; feeding difficulties are an early-infancy presentation (2/2).

**Severity:** **Variable.** Structural anomalies range from lethal-in-utero-decision severity (fetus) through moderate (VSD + pulmonic stenosis, moderate motor/language delay) to comparatively mild growth findings (one patient at 80th centile height). Neurodevelopmental severity spans "moderately delayed motor and language development" to frank intellectual disability.

**Progression:** The **malformations are static** (non-progressive congenital structural defects). The neurodevelopmental phenotype is **developmental, not neurodegenerative** — no regression, no progressive neurological decline has been reported in any patient. Cerebellar and callosal hypoplasia are developmental (hypoplasia), not atrophic.

**Frequency:** See table. **All frequencies are n/2 or n/6 and are not generalizable.** Only DD and bilateral cleft lip/palate approach "obligate" status, and even that is a proposal from a three-patient series.

### 3.4 Quality-of-life impact

**No CFNDS-specific QoL data exist.** No EQ-5D, SF-36, PROMIS, or disease-specific PROM has been administered. The following are **reasoned extrapolations from the constituent phenotypes** and should be curated as such (not as CFNDS evidence):

- **Bilateral cleft lip/palate (2/2 → likely near-obligate):** feeding difficulty in infancy, speech/resonance impairment, recurrent otitis media and conductive hearing loss, multiple staged surgeries through childhood, facial-appearance psychosocial burden. Highest-burden single feature.
- **Global developmental delay / ID:** dominant long-term determinant of independence and caregiver burden.
- **Congenital heart disease (AVSD/VSD/PS):** surgical morbidity; AVSD in particular carries meaningful operative and long-term valve-function burden.
- **Conductive hearing loss:** compounds the speech impact of cleft palate.
- **Feeding difficulties (2/2):** early-infancy nutritional and caregiver burden.
- **Asplenia (with heterotaxy):** lifelong invasive-infection risk requiring prophylaxis — see §12/§13.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Field | Value |
|---|---|
| **Symbol** | **CCDC32** |
| **HGNC** | **HGNC:28295** → CURIE `hgnc:28295` (lowercase prefix per dismech convention) |
| **Approved name** | "coiled-coil domain containing 32" |
| **Previous symbol** | **C15orf57** (appears in older literature and in Abdalla 2022) |
| **Alias** | MGC20481 |
| **Locus** | **15q15.1** |
| **Ensembl** | ENSG00000128891 |
| **NCBI Gene** | 90416 |
| **UniProt** | **Q9BV29** |
| **OMIM (gene)** | 618941 |
| **RefSeq** | NM_052849 (HGNC canonical); **NM_001080791.2** used by Harel 2020; **NM_001080792.4** used by ClinVar |
| **Locus type** | gene with protein product |
| **Protein** | 194-amino-acid polypeptide (isoform reported by Harel et al.); multiple transcript variants exist |

⚠️ **Transcript-nomenclature hazard.** Published HGVS for the two founding frameshifts is on **NM_001080791.2**, but ClinVar reports the same alleles on **NM_001080792.4** with different numbering. Curate both and note the transcript explicitly:

| Family | Published (NM_001080791.2) | ClinVar (NM_001080792.4) |
|---|---|---|
| A | c.54dupT, p.(Thr19Tyrfs*12) | c.27dup, p.(Thr10fs) |
| B | c.189_190dupGG, p.(Glu64Glyfs*12) | c.162_163dup, p.(Glu55fs) |

### 4.2 Pathogenic variants reported

| # | Variant | Type | HGVS / coordinates | Zygosity | Family / origin | Reference |
|---|---|---|---|---|---|---|
| 1 | c.54dupT | Frameshift (1-bp dup) | NM_001080791.2:c.54dupT, p.(Thr19Tyrfs*12); chr15:g.40855188dupA (hg19) | Homozygous | Family A, consanguineous Arab Muslim | PMID:32307552 |
| 2 | c.189_190dupGG | Frameshift (2-bp dup) | NM_001080791.2:c.189_190dupGG, p.(Glu64Glyfs*12); chr15:g.40855052dupCC | Homozygous | Family B, consanguineous Iranian (Isfahan) | PMID:32307552 |
| 3 | ~32.6-kb deletion | Multi-exon/whole-gene deletion | NC_000015.10:g.40529942_40562524del (ClinVar VCV001690313, **Pathogenic**, condition = CFNDS) | Homozygous | Abdalla patient (9-y-o female) | PMID:35451546 |
| 4 | ~32.6-kb deletion | Deletion | NC_000015.10:g.(40529939_40562522)del (ClinVar VCV002431643, **Pathogenic**, condition = CFNDS) | Homozygous | Fernandes da Rocha patient (Portugal) | PMID:38818818 |
| 5 | Deletion of exons 3–4 | Intragenic multi-exon deletion, detected as exon skipping on RNA-seq | Exons 3 and 4 of *CCDC32* | Biallelic | Two siblings, Rotterdam | PMID:41639596 |
| 6 | p.Tyr157Ter | Nonsense | ClinVar VCV002580223, **VUS**, condition = CFNDS | Not stated | ClinVar submission | ClinVar |

**Verbatim support for variant 3:**
> "We report a 9-year-old female patient with CFNDS caused by a homozygous 32,583-bp deletion affecting CCDC32. Independent of the affected CCDC32 transcript variant this deletion likely leads to loss of the encoded protein."
> — PMID:35451546 (verbatim, abstract)

🔬 **Novel observation worth flagging (hypothesis, needs verification):** ClinVar records VCV001690313 and VCV002431643 have **near-identical breakpoints** (g.40529942_40562524 vs g.40529939_40562522) yet correspond to patients reported independently from different centres (Abdalla et al., Egypt/Hamburg; Fernandes da Rocha et al., Porto). This is consistent with a **recurrent, likely repeat-mediated (NAHR) deletion allele at 15q15.1**, or possibly a founder allele. I could not confirm the Fernandes da Rocha breakpoints directly — that paper has **no abstract in PubMed** and the full text is paywalled. **Curate this as a `KNOWLEDGE_GAP`/hypothesis, not as an established fact.**

**Variant classification (ACMG/AMP):** ClinVar carries **4 Pathogenic** CFNDS-associated *CCDC32* alleles (two frameshift dups, two large deletions), all with the criteria-provided or no-assertion review status — **none are expert-panel reviewed**. One nonsense VUS exists. There are **no ClinGen variant-curation assertions** for *CCDC32*.

**Variant class distribution:** exclusively **loss-of-function** — frameshift duplications, whole-gene/multi-exon deletions, and (VUS) nonsense. **No pathogenic missense variant has been reported.** This matters mechanistically: the disease is a pure LoF/hypomorph disorder, not a gain-of-function or dominant-negative one.

**Allele frequency:** Both founding frameshifts were:
> "Absent from gnomAD, TOPMed, Geno2MP, and GME Variome" *[PMC7268788, full text]*

**Gene-level constraint (gnomAD v4.0):** **pLI = 0.19**, **LOEUF = 0.76**. Both indicate *CCDC32* is **tolerant of heterozygous LoF** — exactly the expected signature for a recessive disease gene, and a useful reassurance that carriers are unaffected. (LOEUF 0.76 sits above the conventional <0.6 Mendelian-dominant threshold.)

**Somatic vs germline:** **Germline only.** No somatic role. COSMIC/TCGA report no recurrent driver role for *CCDC32*.

**Functional consequence:** **Loss of function.** Mechanistic work (§6) shows the disease-associated truncations remove the α-helical AP-2-binding region:
> "Disease-causing mutations…lack the α-helix encoded by residues 78–98…defective in AP2 binding" *[PMC12768407, eLife, full text]*
> "The CCDC32 mutant was defective in binding AP2 α and σ2 when expressed at similar levels as WT" *[PMC11348294, PNAS, full text]*
> "The AP2-regulating function of CCDC32 is disrupted by a disease-causing mutation" *[PMC11348294, full text]*

### 4.3 ClinGen gene–disease validity

| Field | Value |
|---|---|
| Gene | CCDC32 (HGNC:28295) |
| Disease | Cardiofacioneurodevelopmental syndrome (MONDO:0030873) |
| MOI | **Autosomal recessive (AR)** |
| **Classification** | **MODERATE** |
| Expert panel | Syndromic Disorders GCEP |
| Date | 2024-10-18 |

This is a **CGGV**-citable structured assertion for dismech evidence. Note it is **Moderate**, not Definitive — appropriate epistemic humility for a 5-family disease. (Structured-source citation would take the form `CGGV:<assertion_id>`; the assertion ID must be resolved from the ClinGen CSV via `just clingen-rebuild` before citing.)

**ClinGen dosage sensitivity:** **no curation exists** (0 classifications) — so no CGDS citation is available.

### 4.4 Modifier genes

**None identified.** Harel et al. invoke unspecified modifiers to explain absent classical ciliopathy features, but no modifier locus has been mapped.

### 4.5 Epigenetic information

**No data.** No methylation episignature has been described for CFNDS. (This is a plausible future study — episignatures now exist for many Mendelian NDDs — and is a reasonable `KNOWLEDGE_GAP`.)

### 4.6 Chromosomal abnormalities

The pathogenic alleles include **intragenic and whole-gene deletions at 15q15.1**, i.e. CNVs rather than SNVs, in **3 of 5 families**. Critically:

> "This deletion was not detected in previous SNP array analyses and trio exome sequencing" *[PMID:41639596]*

No CFNDS case has been attributed to aneuploidy, translocation, inversion, or a contiguous-gene 15q15 microdeletion syndrome. Larger 15q duplications/gains overlapping *CCDC32* appear in ClinVar but are unrelated pathogenic CNVs of other phenotypes.

---

## 5. Environmental Information

- **Environmental factors:** **Not applicable.** No toxin, radiation, pollutant, or occupational exposure is implicated. CTD contains no relevant CCDC32–chemical–disease axis for this phenotype.
- **Lifestyle factors:** **Not applicable.** No smoking, diet, exercise, or alcohol association. (Note: general periconceptional folate status modifies non-syndromic orofacial clefting risk in the population — this is **not** established as relevant to the syndromic, monogenic clefting in CFNDS and should not be curated as a CFNDS factor.)
- **Infectious agents:** **Not applicable.** No infectious etiology or trigger.

The only non-genetic factor with real epidemiological traction is **consanguinity** (§2, §9), which is a population-structure variable rather than an environmental exposure.

---

## 6. Mechanism / Pathophysiology

CFNDS has a **genuinely contested and rapidly evolving mechanism**, which is the most scientifically interesting aspect of this entry. Two models exist; the second has largely overtaken the first in molecular support, but the first carries the developmental-phenotype evidence.

### 6.1 Model A — Ciliopathy (Harel et al. 2020; the original proposal)

The founding paper framed CFNDS as a ciliopathy on the basis of phenotype overlap (laterality defect, cerebellar hypoplasia, craniofacial anomalies) plus direct functional data.

**Full verbatim abstract (PMID:32307552) — safe for evidence snippets:**

> "Despite the wide use of genomics to investigate the molecular basis of rare congenital malformations, a significant fraction of patients remains bereft of diagnosis. As part of our continuous effort to recruit and perform genomic and functional studies on such cohorts, we investigated the genetic and mechanistic cause of disease in two independent consanguineous families affected by overlapping craniofacial, cardiac, laterality and neurodevelopmental anomalies. Using whole exome sequencing, we identified homozygous frameshift CCDC32 variants in three affected individuals. Functional analysis in a zebrafish model revealed that ccdc32 depletion recapitulates the human phenotypes. Because some of the patient phenotypes overlap defects common to ciliopathies, we asked if loss of CCDC32 might contribute to the dysfunction of this organelle. Consistent with this hypothesis, we show that ccdc32 is required for normal cilia formation in zebrafish embryos and mammalian cell culture, arguing that ciliary defects are at least partially involved in the pathomechanism of this disorder."

**Supporting evidence:**
- Kupffer's vesicle (the zebrafish left-right organizer) cilia **reduced in both number (P<0.001) and length (P<0.05)** in `ccdc32` crispants *[MODEL_ORGANISM]*
- Ciliogenesis impaired in mouse **IMCD3** cells on siRNA knockdown: reduced % ciliated cells (P<0.01) and reduced cilium length *[IN_VITRO]*
- Human Protein Atlas independently localizes CCDC32 to the **primary cilium, centrosome, and basal body** (as well as plasma membrane and microtubules)
- CCDC-family precedent: CCDC39, CCDC40, CCDC103, CCDC114 all cause primary ciliary dyskinesia

**Authors' own caveats (important for balanced curation):**
> "Some of the hallmark ciliopathy pathologies were absent from the described individuals, such as cystic renal disease and polydactyly" *[full text]*
> "Whether this molecule also performs non-ciliary roles relevant to the human pathology remain unclear" *[full text]*

### 6.2 Model B — AP-2 adaptor assembly chaperone / clathrin-mediated endocytosis (2024–2026; now the dominant molecular model)

Three independent structural/cell-biological studies since 2024 have assigned CCDC32 a **precise, non-ciliary molecular function**: it is a dedicated **assembly chaperone for the AP-2 clathrin adaptor complex**.

**The assembly pathway (PNAS 2024, PMID:39145939):**

1. AAGAB binds the AP-2 **α** subunit, then recruits **σ2** → AAGAB:α:σ2 ternary complex
2. **CCDC32 recognizes AAGAB:α:σ2**, displacing AAGAB → **α:σ2:CCDC32 template complex**
3. The template **sequentially recruits μ2, then β2**
4. **β2 binding completes AP-2 and releases CCDC32**

> "AP2 assembly is controlled by a handover mechanism, switching from AAGAB-based initiation complexes to CCDC32-based template complexes" *[PMC11348294, full text]*
> "In mammalian cells deficient in AAGAB or CCDC32, all AP2 subunits are degraded" *[full text]*
> "CCDC32 is a general regulator of CME" *[full text]*

CCDC32 directly binds **α, σ2, and μ2 — but not β2** (β2 binding is what evicts it). It is **selective for AP-2** and does not regulate AP-1/AP-3/AP-4 assembly.

**Cellular consequences of CCDC32 loss:** AP-2 subunit degradation; loss of plasma-membrane AP-2 puncta; **strongly reduced transferrin-receptor endocytosis with elevated surface TfR**; impaired GLUT4 internalization.

**Coated-pit dynamics (eLife 2026, PMID:41489497 / PMC12768407):**
> "siRNA-mediated knockdown of CCDC32 leads to the accumulation of unstable flat clathrin assemblies" *[full text]*
> "CCDC32 knockdown strongly inhibited CCP invagination" *[full text]*
> "CCDC32 interacts with AP2 via the α-AD [appendage domain]" *[full text]*

Notably, in this system knockdown **"does not affect AP2 expression level"** *[full text]* — an apparent tension with the PNAS degradation result, likely reflecting knockdown vs knockout depth. Worth curating as a `hypothesis_groups` distinction rather than smoothing over.

**Structural mechanism and the membrane switch (Science Advances 2026, PMID:42234739):**
> "CCDC32 binds to α/σ2 in a multivalent manner, using at least three (extended FxDxF, dileucine, and AH1)" *[full text]*
> "CCDC32 uses a noncanonical WAPL (Wxxϕ) motif to bind in the same location as other tyrosine-containing cargo" *[full text]*
> "In solution, CCDC32 prevents complex assembly and actively disassembles AP-2 tetramers" *[full text]*
> "The presence of PIP2–containing membrane stabilizes the final stages of assembly" *[full text]*
> "Loss of CCDC32 significantly decreases the steady-state level of all four AP-2 subunits in HeLa cells" *[full text]*

So CCDC32 is a **cargo-mimicking, membrane-gated chaperone**: it occupies the cargo-binding sites of α/σ2 and μ2 to hold AP-2 in an assembly-competent but inactive state, and **PI(4,5)P₂-containing membrane acts as the molecular switch** that licenses final assembly at the plasma membrane. This elegantly couples AP-2 biogenesis to its site of action.

### 6.3 Reconciling the two models

These are **not mutually exclusive**, and the most defensible curated position is that **AP-2/CME dysfunction is the primary molecular lesion, with ciliary phenotypes as a plausible downstream consequence**:

- Clathrin-mediated endocytosis governs surface-receptor turnover, including receptors that traffic through the ciliary pocket and regulate Hedgehog/Wnt signalling — so CME failure can secondarily impair ciliogenesis and cilium-dependent signalling.
- The **absence of classical ciliopathy features** (no cystic kidney disease, no polydactyly, no retinal degeneration reported) argues against a primary, canonical ciliopathy.
- Independent genetic support for AP-2 hypofunction as a cause of *exactly this phenotype spectrum*: **Ap2b1 (β2) null mice "survive until birth but then die shortly afterwards, the only obvious abnormality being that they have a cleft palate"** *[JCS review, full text]*. Abdalla et al. made precisely this argument:
  > "Cleft palate and cardiac defects observed in mice deficient of different AP2 subunits support a CCDC32 function in the AP2 complex." — PMID:35451546 (verbatim, abstract)
- AP2σ (σ2) and AP2μ (μ2) nulls are **early embryonic lethal**; complete AP-2 loss is embryonic lethal. CCDC32 loss is compatible with birth — consistent with CFNDS being a **partial/hypomorphic AP-2 deficiency**, i.e. residual AP-2 assembly persists (AAGAB-dependent, CCDC32-independent). The Sci Adv authors make this point:
  > "Mutation of CCDC32 does not prevent embryonic development but results in patients with craniofacial malformations" *[full text]*

**Another reported interaction:** CCDC32 binds the **C-terminus of annexin A2**, itself a membrane–cytoskeleton and endocytosis protein *[PMC7268788, full text]* — consistent with the trafficking model.

### 6.4 Proposed causal chain (for a dismech pathograph)

```
Biallelic CCDC32 LoF (frameshift / multi-exon deletion)          [MOLECULAR]
  → Loss of CCDC32 α-helix aa78–98; failure to bind AP-2 α/σ2     [MOLECULAR]
    → Failure of the AAGAB→CCDC32 handover; no α:σ2:CCDC32 template [MOLECULAR]
      → Impaired AP-2 heterotetramer assembly; AP-2 subunit degradation [MOLECULAR]
        → Destabilized, flat, non-invaginating clathrin-coated pits [CELLULAR]
          → Reduced clathrin-mediated endocytosis / receptor internalization [CELLULAR]
            ├→ Impaired ciliogenesis (reduced cilium number and length)  [CELLULAR]  (hypothesis group: ciliary)
            │    → Defective left-right organizer (Kupffer's vesicle) function [TISSUE]
            │      → Aberrant southpaw/NODAL laterality signalling
            │        → Situs inversus, asplenia, cardiac looping defect  [ORGANISM]
            ├→ Impaired cranial neural crest / facial primordium morphogenesis [TISSUE]
            │    → Failure of lip and palatal shelf fusion
            │      → Bilateral cleft lip and palate; midline facial defects [ORGANISM]
            ├→ Impaired cardiac morphogenesis (septation / AV canal)     [TISSUE]
            │    → AVSD, VSD, pulmonic stenosis                          [ORGANISM]
            └→ Impaired cerebral/cerebellar growth and midline patterning [TISSUE]
                 → Microcephaly, cerebellar vermis hypoplasia, hypoplastic
                   corpus callosum, hypoplastic pons
                     → Global developmental delay / intellectual disability [ORGANISM]
```

**Upstream vs downstream:** The AP-2 assembly failure is unambiguously upstream. The ciliary branch is **contested** in its position — Harel's model places cilia upstream of laterality/cerebellar defects directly; the newer model places cilia *downstream of* CME failure. Curate as **two `hypothesis_groups`** on the relevant edges (e.g. `ciliary_primary` vs `cme_primary`), with the AP-2 chain as the canonical/emerging model.

### 6.5 Ontology term suggestions for mechanism

**GO biological process / cellular component (all verified via OLS):**

| GO ID | Label | Use |
|---|---|---|
| GO:0072583 | clathrin-dependent endocytosis | Core process, DECREASED |
| GO:0030122 | AP-2 adaptor complex | CC — the assembled target |
| GO:0030131 | clathrin adaptor complex | CC — parent |
| GO:0035612 | AP-2 adaptor complex binding | MF — CCDC32's molecular function |
| GO:0030119 | AP-type membrane coat adaptor complex | CC — parent |
| GO:0030136 | clathrin-coated vesicle | CC |
| GO:0060271 | cilium assembly | Ciliary branch, DECREASED |
| GO:0007368 | determination of left/right symmetry | Laterality branch, DECREASED |

Additional GO candidates to verify before use: protein-containing complex assembly (GO:0065003), chaperone-mediated protein complex assembly, phosphatidylinositol-4,5-bisphosphate binding, palate development, heart looping, cerebellum development.

**CL cell types (verified):**

| CL ID | Label | Relevance |
|---|---|---|
| CL:0000008 | migratory cranial neural crest cell | Craniofacial/cleft branch |
| CL:2000073 | migratory cardiac neural crest cell | Cardiac outflow branch |
| CL:0011012 | neural crest cell | Parent |

Additional candidates (verify): ciliated epithelial cell, kidney collecting duct epithelial cell (the IMCD3 in-vitro model), cardiac myocyte, Purkinje cell, neuroepithelial cell.

**UBERON (verified):** UBERON:0004720 cerebellar vermis. Additional candidates to verify: secondary palate, upper lip, interventricular septum, atrioventricular canal, pulmonary valve, spleen, corpus callosum, pons, Kupffer's vesicle (zebrafish-specific).

**CHEBI:** phosphatidylinositol 4,5-bisphosphate (the membrane switch lipid) — verify the exact CHEBI ID before use.

### 6.6 Other mechanism dimensions

- **Metabolic changes:** **None reported.** No metabolic phenotype. (Note the GLUT4 internalization defect in CCDC32-deficient cells is a *cell-biological* observation, not a reported clinical metabolic phenotype in patients — do not over-read it into a diabetes claim.)
- **Immune involvement:** No primary immune mechanism. However, **asplenia** (1/2 in HPOA) produces functional hyposplenism with encapsulated-organism susceptibility — a **secondary, anatomically-mediated immunodeficiency**, clinically important (§12/§13).
- **Tissue damage mechanisms:** **Not applicable in the classical sense** — CFNDS is a **developmental morphogenesis disorder**, not a tissue-injury disorder. There is no oxidative stress, ischemia, fibrosis, or necrosis mechanism.
- **Biochemical abnormalities:** No enzyme deficiency, no channelopathy, no receptor defect measurable in patient fluids. The defect is a **protein-complex assembly failure**.
- **Molecular profiling:** No CFNDS transcriptomic, proteomic, metabolomic, or lipidomic patient study exists. The **one transcriptomic application is diagnostic, not mechanistic** — clinical RNA-seq of patient cells detecting exon 3–4 skipping (PMID:41639596).
- **Single-cell / spatial / multi-omics:** **None for CFNDS.** CCDC32 shows "low tissue specificity" and "low cell type specificity" in Human Protein Atlas, with mass-spec enhancement in lymphoid tissue and single-cell enhancement in fallopian tube — **none of which maps onto the disease phenotype**, reinforcing that the phenotype specificity comes from developmental context, not expression restriction.
- **Functional genomics screens:** No published CRISPR/RNAi screen result specific to CFNDS. *CCDC32* is not a common-essential gene in DepMap-style screens (consistent with LOEUF 0.76 and viability of KO cell lines used in the mechanism papers).

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (directly malformed):**
| System | Structures | HPO/UBERON anchor |
|---|---|---|
| Craniofacial | Upper lip, primary and secondary palate, mandible, external ear, orbits/interorbital distance, nose | HP:0410030, HP:0000175, HP:0000347, HP:0000411 |
| Central nervous | Cerebellum (vermis), pons, corpus callosum, cerebral cortex (volume — microcephaly) | HP:0001320, HP:0012110, HP:0002079, HP:0000252; UBERON:0004720 |
| Cardiovascular | Atrioventricular canal, interventricular septum, pulmonary valve | HP:0006695, HP:0001629, HP:0001642 |
| Skeletal / limb | Digits (5th finger, phalanges), nails, spine (kyphosis), hands/feet size | HP:0004209, HP:0001156, HP:0012385, HP:0008386, HP:0002808 |
| Genitourinary | Testis (descent) | HP:0000028 |

**Secondary / complication-driven:**
- **Spleen** — asplenia (HP:0001746), in the context of the laterality defect
- **Abdominal viscera** — situs inversus (HP:0003363)
- **Middle ear** — conductive hearing loss, mechanistically secondary to cleft palate/eustachian dysfunction (HP:0000405)
- **Upper GI / feeding apparatus** — feeding difficulties (HP:0008872), largely secondary to cleft and neurological status
- **Growth axis** — postnatal growth restriction / short stature (HP:0004322)

**Notably spared:** **Kidneys** (normal renal ultrasound in both index patients), **eyes/retina** (normal ophthalmology in both), **EEG normal** in individual B-II-1 *[PMC7268788, full text]*. The renal and retinal sparing is the key argument against classical ciliopathy.

**Body systems involved:** cardiovascular, nervous, musculoskeletal, digestive, integumentary (nails/dermatoglyphics), reproductive, immune (via asplenia), sensory (auditory).

### Tissue and cell level

- **Cranial neural crest–derived mesenchyme** of the frontonasal and maxillary/mandibular prominences — the presumptive lesion site for cleft lip/palate and the facial/ear/jaw dysmorphism (CL:0000008)
- **Cardiac neural crest** and second-heart-field derivatives — outflow/septation defects (CL:2000073)
- **Left-right organizer ciliated epithelium** (Kupffer's vesicle in fish; embryonic node in mammals) — laterality
- **Cerebellar and pontine neuroepithelium / rhombic lip derivatives** — vermian and pontine hypoplasia
- **Palatal shelf epithelium and mesenchyme** — fusion failure
- **Epithelial tissue** broadly, given CME is a general epithelial/all-cell process

### Subcellular level (GO cellular component)

CCDC32 and its pathway localize to:
- **Plasma membrane** and **clathrin-coated pit / clathrin-coated vesicle** (GO:0030136) — the principal site of action
- **AP-2 adaptor complex** (GO:0030122) itself
- **Primary cilium, centrosome, basal body** — per Human Protein Atlas
- **Microtubules**
- **Cytosol** (site of the AAGAB/CCDC32 pre-assembly intermediates)

### Localization / lateralization

- **Facial clefting is bilateral** in the reported patients ("bilateral cleft lip and palate" is the emphasized core feature) — a midline/bilateral pattern, not unilateral.
- **Digital anomalies are bilateral** (bilateral camptodactyly and clinodactyly of fifth fingers).
- **The laterality defect is, by definition, an asymmetry disorder**: abdominal situs inversus with asplenia, plus abnormal cardiac looping in the zebrafish model with **"bilateral or right-sided"** *southpaw* expression replacing normal left-sided expression.

This combination — **bilateral/midline structural defects plus a stochastic laterality defect** — is characteristic and diagnostically useful.

---

## 8. Temporal Development

### Onset

- **Congenital (HP:0003577), 2/2.** All structural anomalies are established in embryogenesis.
- **Detectable prenatally:** the terminated fetus (A-II-2) was identified antenatally with bilateral cleft lip, vermian hypoplasia, hypoplastic pons, and abnormal cisterna magna — establishing that CFNDS can be **recognized on second-trimester ultrasound/fetal MRI** in an at-risk family.
- **Onset pattern:** **chronic/static from birth.** Not acute, not subacute, not insidious.
- **Sequence of clinical declaration:** prenatal structural findings (if imaged) → neonatal cleft and cardiac diagnosis → infantile feeding difficulty (2/2) → toddler-age developmental delay → school-age intellectual disability, hearing, and growth concerns.

### Progression

- **Disease stages:** **No staging system exists** and none is applicable — CFNDS is not a staged/progressive disease.
- **Progression rate:** **Non-progressive.** The malformations are fixed. Developmental delay evolves into a stable intellectual disability profile rather than deteriorating.
- **Course pattern:** **Static/stable** with age-dependent emergence of developmental phenotypes. **No episodic, relapsing-remitting, or degenerative course** has been reported in any patient.
- **Duration:** **Lifelong, chronic.** Not self-limited.

### Patterns

- **Remission:** Not applicable — no spontaneous remission; "treatment-induced improvement" refers only to surgical correction of individual anomalies (cleft repair, cardiac repair), not disease remission.
- **Critical periods:**
  - **Weeks 4–7 post-conception** — lip fusion; **weeks 6–12** — secondary palate fusion. These windows are already passed at diagnosis; **no prenatal intervention is possible.**
  - **Weeks 3–4** — left-right axis determination and cardiac looping.
  - **Postnatal intervention windows are the actionable ones:** cleft lip repair ~3–6 months, palate repair ~9–18 months (speech-outcome critical period), cardiac repair timed to lesion (AVSD typically 3–6 months), **early intervention/speech therapy from infancy**, and **hearing surveillance from the neonatal period** because unrecognized conductive loss compounds the cleft-related speech deficit.

**Longitudinal data:** **No natural-history study, no registry, no longitudinal cohort exists.** The oldest reported patient is 9 years old. **Adult outcomes for CFNDS are entirely unknown.** This is arguably the single largest knowledge gap.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** **Not established.** With ~6 living individuals reported worldwide from 5 families since 2020, the observed prevalence is far **below 1 in 1,000,000**.
  - For structured curation: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: BELOW_1_IN_1000000` (or `ULTRA_RARE`), `population: Worldwide`. **Do not assign a `rate_per_100000`** — no denominator-based estimate exists.
  - Supporting statement: *"CFNDS has only been described in four living individuals and one terminated fetus from four families"* (PMID:41639596) — that count precedes the two siblings in the same report.
- **Incidence:** **Not established.** No birth-prevalence estimate exists.
- **Ascertainment caveat:** True prevalence is almost certainly higher than reported. Three of five families' variants are **deletions**, and one was **missed by both SNP array and trio exome sequencing** — meaning conventional diagnostic pipelines systematically under-ascertain this disease (§10).

### Genetic epidemiology

| Parameter | Status |
|---|---|
| **Inheritance pattern** | **Autosomal recessive** (HP:0000007). ClinGen AR, MODERATE. All published probands **homozygous**. |
| **Penetrance** | Appears **complete** in biallelic LoF homozygotes (all reported homozygotes are affected), but **n is far too small to exclude reduced penetrance.** Heterozygous carriers (parents) are **unaffected**. |
| **Expressivity** | **Variable** — clearly so. Compare: one patient with AVSD + situs inversus + asplenia; another with VSD + pulmonic stenosis and normal situs; the fetus with no cardiac defect at all. Hypertelorism vs hypotelorism between the two index patients. **Intrafamilial** variability is untested except in the sibling pair. |
| **Genetic anticipation** | **Not applicable** — no repeat expansion mechanism. |
| **Germline mosaicism** | **Not reported.** Standard AR recurrence counselling applies; no mosaicism-specific caveat documented. |
| **Founder effects** | **Suspected but unproven.** The near-identical ~32.6-kb deletion in two independently reported patients (§4.2) raises either a **recurrent (repeat-mediated) deletion** or a **founder allele**. Requires breakpoint-level and haplotype confirmation. |
| **Consanguinity** | **Central.** Both founding families were consanguineous (Arab Muslim first cousins once removed; Iranian). Homozygosity mapping was the discovery route: **~9.06 Mb ROH** in Family A, **5.23 Mb ROH** in Family B *[full text]*. |
| **Carrier frequency** | **Not established.** No pathogenic *CCDC32* allele is reported at appreciable frequency in gnomAD; the two founding frameshifts were **absent from gnomAD, TOPMed, Geno2MP, and GME Variome**. Carrier frequency is presumptively <1/1,000 in unselected populations, potentially higher in specific endogamous groups. |

### Population demographics

- **Reported ancestries:** Arab Muslim (Israel/Palestine region), Iranian (Isfahan), Egyptian (Abdalla cohort context), Portuguese, Dutch (Rotterdam sibling pair). This is a **broad, non-clustered geographic spread** — no single ethnic predilection can be claimed, though ascertainment is biased toward centres with consanguineous referral populations and toward European tertiary genetics services.
- **Geographic distribution:** No endemic region. Cases from the Middle East, North Africa, Southern Europe, and Northwestern Europe.
- **Variant geography:** The two founding frameshifts are each private to one Middle Eastern family. The ~32.6-kb deletion allele appears in at least two unrelated Southern-European/North-African-context patients — the only candidate for a geographically structured allele.
- **Sex ratio:** Approximately balanced in a cohort far too small to estimate (reported: female, male, female, plus the 2024 patient and sibling pair). **No sex bias is expected** for an autosomal recessive disorder; do not curate a sex ratio.
- **Age distribution of affected individuals:** All reported living patients were children at the time of report (ages 3, 6, 9 years, plus the sibling pair). **No adult patient has been described.** This reflects the disease's recent delineation, not necessarily a survival ceiling — but it means **adult phenotype and survival are unknown**.

---

## 10. Diagnostics

### Clinical tests

- **Laboratory tests:** **No disease-specific laboratory test exists.** There is no enzyme assay, no metabolite, no biochemical marker for CFNDS. Standard labs are non-diagnostic.
  - The one lab investigation with real value is **functional asplenia screening** in patients with laterality defects: peripheral smear for **Howell-Jolly bodies**, correlated with abdominal imaging.
- **Biomarkers:** **None.** No FDA-listed or research biomarker. Neither diagnostic, prognostic, nor monitoring biomarkers exist. (Speculatively, surface transferrin receptor levels or AP-2 subunit abundance in patient fibroblasts could serve as a **functional assay** — this has been demonstrated in engineered cells but **never applied to a patient sample**. This is a concrete, actionable research gap.)
- **Imaging studies (essential, high-yield):**
  - **Brain MRI** — required. Detects cerebellar vermis hypoplasia (HP:0001320), hypoplastic corpus callosum (HP:0002079), hypoplastic pons (HP:0012110), abnormal cisterna magna. This is the highest-yield single imaging study.
  - **Echocardiography** — required in all patients. Detects AVSD, VSD, pulmonic stenosis, and cardiac looping/positional abnormality.
  - **Abdominal ultrasound / cross-sectional imaging** — for situs and **spleen presence**. Given asplenia carries life-threatening infection risk, this is not optional in a patient with any laterality clue.
  - **Renal ultrasound** — normal in reported patients, but reasonable to exclude the ciliopathy differential.
  - **Skeletal survey / hand radiographs** — brachydactyly, clinodactyly, phalangeal anomalies, kyphosis.
  - **Fetal ultrasound / fetal MRI** — for prenatal detection in at-risk pregnancies (proven effective: the A-II-2 fetus).
- **Functional tests:** **Audiometry / tympanometry** — mandatory and repeated, given bilateral conductive hearing loss and cleft palate. Feeding/swallow evaluation (videofluoroscopy) for the 2/2 infantile feeding difficulty.
- **Electrophysiology:** **EEG was normal** in individual B-II-1. **Seizures are not a reported CFNDS feature** — a useful negative that distinguishes CFNDS from the AP2M1-related developmental and epileptic encephalopathy (see differential below). ECG accompanies echocardiography.
- **Biopsy / pathology:** **No characteristic histopathology.** No diagnostic biopsy exists. Nasal brush biopsy for ciliary ultrastructure/beat frequency (the PCD workup) has **not** been reported in CFNDS and there is no evidence of a motile-ciliary/PCD-type respiratory phenotype — **do not curate a PCD-style workup as indicated**.

### Genetic testing — the only definitive diagnostic modality

**Recommended approach, in order of yield:**

1. **Trio exome sequencing (ES) with explicit CNV calling**, or preferably
2. **Genome sequencing (GS)** — better structural-variant resolution, and
3. **RNA sequencing (RNA-seq) as a complementary second-tier test** when DNA testing is negative.

**The single most important practical lesson from the literature is that conventional testing fails in this disease:**

> "This deletion was not detected in previous SNP array analyses and trio exome sequencing" — PMID:41639596
> "highlighting the complementary value of RNA-seq" — PMID:41639596

- **WES utility:** Established — it discovered the gene ("Using whole exome sequencing, we identified homozygous frameshift CCDC32 variants," PMID:32307552). But **ES alone missed a causal intragenic deletion** in one family. ES must be paired with CNV analysis, and a negative ES does not exclude CFNDS.
- **WGS utility:** Superior for the deletion alleles that constitute the majority of reported pathogenic variation (3/5 families). Preferred first-line where available.
- **RNA-seq:** **Proven diagnostic in CFNDS** — exon 3–4 skipping revealed the biallelic deletion the DNA tests missed. This makes CFNDS a genuine exemplar of RNA-seq's complementary diagnostic value.
- **Gene panels:** *CCDC32* should be included on **orofacial clefting**, **syndromic congenital heart disease**, **heterotaxy/laterality**, **cerebellar hypoplasia/pontocerebellar**, and **intellectual disability/multiple congenital anomaly** panels. **Verify inclusion before relying on a panel** — as a 2020 gene with Moderate ClinGen validity, panel coverage is inconsistent.
- **Single-gene testing:** Reasonable only for **targeted familial-variant testing** (carrier testing of relatives, prenatal diagnosis) once the family's variant is known. Not appropriate as a primary diagnostic given phenotypic nonspecificity.
- **Chromosomal microarray (CMA)/SNP array:** **Documented to fail** — the exon 3–4 deletion escaped SNP array. CMA remains a reasonable first-tier test for MCA/DD generally, but a **normal CMA does not exclude CFNDS.**
- **Homozygosity mapping:** **High value in consanguineous families** — it was the discovery route (9.06 Mb and 5.23 Mb ROH). Should be run alongside ES/GS in consanguineous pedigrees.
- **Karyotyping / FISH:** No role. No CFNDS case involves a visible chromosomal rearrangement.
- **Mitochondrial DNA testing:** **Not applicable.**
- **Repeat expansion testing:** **Not applicable.**

### Omics-based diagnostics

- **RNA sequencing:** the one validated omics diagnostic (above).
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** **No established role.** No episignature. No metabolomic signature.

### Clinical criteria

- **No standardized diagnostic criteria, no consensus guideline, no society statement exists** for CFNDS. Diagnosis is **molecular**: biallelic pathogenic *CCDC32* variants in a compatible phenotype.
- **Proposed clinical gestalt prompting testing (from Abdalla's core phenotype):** developmental delay + bilateral cleft lip and palate, with any of — microcephaly, cerebellar vermis hypoplasia, congenital heart defect, digital/nail anomalies, laterality anomaly, postnatal growth restriction. **Consanguinity substantially raises prior probability.**

### Differential diagnosis

| Condition | Gene(s) | Distinguishing features |
|---|---|---|
| **Cardiofaciocutaneous syndrome (CFC)** | BRAF, MAP2K1/2, KRAS | **AD/de novo**, RASopathy; ectodermal/hair/skin findings, HCM; **cleft lip/palate not typical**. The critical name-confusion pitfall. |
| **Kabuki syndrome** | KMT2D, KDM6A | AD/XL; long palpebral fissures with lower-lid eversion, persistent fetal fingerpads, CHD; cleft palate common but cleft **lip** less so |
| **CHARGE syndrome** | CHD7 | AD; coloboma, choanal atresia, semicircular canal hypoplasia, hypogonadotropic hypogonadism |
| **22q11.2 deletion** | TBX1 region | Conotruncal CHD, palatal insufficiency/cleft palate, hypocalcemia, immune deficiency; **CMA-detectable** |
| **Primary ciliary dyskinesia / heterotaxy syndromes** | DNAH5, DNAI1, CCDC39, CCDC40, ZIC3, etc. | Chronic sinopulmonary disease, neonatal respiratory distress, bronchiectasis — **absent in CFNDS**; clefting atypical |
| **Joubert syndrome / other cerebellar-vermis ciliopathies** | AHI1, CEP290, TMEM67, etc. | Molar tooth sign, oculomotor apraxia, retinal dystrophy, nephronophthisis — **renal and retinal disease absent in CFNDS** |
| **Pontocerebellar hypoplasias** | TSEN54, EXOSC3, etc. | **Progressive** microcephaly and neurodegeneration; CFNDS is static |
| **AP2M1-related DEE** | AP2M1 | Same molecular pathway (AP-2/CME) but **AD de novo p.Arg170Trp**, dominated by **epilepsy (myoclonic-atonic)**; **no clefting, no CHD**. EEG normal in CFNDS. |
| **Oral-facial-digital syndromes** | OFD1 et al. | Oral frenula, lingual hamartomas, polydactyly (absent in CFNDS) |
| **Non-syndromic bilateral CL/P** | multifactorial | Absence of DD, CHD, cerebellar anomaly, microcephaly |

### Screening

- **Newborn screening:** **Not applicable** and not feasible — no biochemical marker. CFNDS is not on any NBS panel.
- **Carrier screening:** *CCDC32* is **not on standard expanded carrier screening panels.** Given the ultra-rare status, population carrier screening is not indicated. **Targeted carrier testing of relatives is indicated once a family variant is known.**
- **Cascade screening:** Appropriate for at-risk relatives in a known family (siblings of probands; extended family in consanguineous pedigrees).

---

## 11. Outcome / Prognosis

**Global caveat: there is no natural-history study, no survival analysis, and no adult patient reported. Everything below is either directly observed in ≤6 children or explicitly labelled as extrapolation.**

### Survival and mortality

- **5-year / 10-year survival:** **Not established.** No survival data.
- **Life expectancy:** **Unknown.** All reported living patients were alive at last report at ages 3, 6, and 9 years, plus the sibling pair. **No death of a liveborn CFNDS patient has been reported.**
- **Mortality rate / disease-specific mortality:** **Not established.**
- **One pregnancy was electively terminated** following prenatal detection of anomalies (fetus A-II-2) — this is a **reproductive decision, not a measure of intrinsic lethality**, and should not be curated as a mortality statistic.
- **Reasoned prognostic drivers of mortality risk** (extrapolated, not CFNDS-observed): severity of the congenital heart defect (AVSD carries the greatest operative burden), and **overwhelming post-splenectomy-type sepsis risk in asplenic patients** — the latter is a preventable cause of death and the single most important actionable prognostic factor.

### Morbidity and function

- **Morbidity:** Substantial and multi-domain — cognitive, speech, hearing, feeding, cardiac, and surgical.
- **Disability outcomes:** **Global developmental delay in 2/2 and frank intellectual disability in the oldest reported patient (age 9).** Long-term functional independence is unknown but likely to require support. No ICF-coded outcome data exist.
- **Quality of life:** **No measured QoL data.** No EQ-5D/SF-36/PROMIS administration reported.

### Disease course and complications

Observed and anticipated complications:
- **Cleft-related:** feeding failure in infancy (observed 2/2, "severe feeding difficulties" in one), velopharyngeal insufficiency, speech disorder, recurrent otitis media, **bilateral conductive hearing loss** (observed), dental anomalies (missing teeth observed)
- **Cardiac:** heart failure from unrepaired AVSD/VSD, right-ventricular consequences of pulmonic stenosis, operative and post-operative morbidity
- **Neurological:** developmental delay → intellectual disability; cerebellar signs (ataxia/coordination) plausible from vermian hypoplasia but **not explicitly reported**; **seizures not reported**
- **Infectious:** **encapsulated-organism sepsis in the asplenic patient** — the highest-acuity preventable complication
- **Growth:** postnatal growth restriction/short stature in some, but **not universal** (one patient at 80th centile height, another at 97th)
- **Behavioral:** hyperactivity reported in one patient

### Recovery potential

- **Structural anomalies are surgically correctable, not spontaneously recoverable.** Cleft repair and cardiac repair yield good anatomical outcomes by general paediatric standards.
- **Neurodevelopmental impairment is not recoverable** — it is amenable to habilitation/early intervention but not to reversal.
- **No disease-modifying therapy exists**, so there is no "with vs without treatment" survival comparison to report.

### Prediction

- **Prognostic factors:** **No validated prognostic model, no prognostic biomarker, no clinical calculator exists.** Reasoned (unvalidated) determinants: severity of CHD; presence of asplenia; degree of microcephaly and hindbrain hypoplasia; adequacy/timing of cleft and hearing management.
- **Genotype–phenotype correlation:** **None established.** All reported variants are complete LoF (frameshift or deletion) yet produce a variable phenotype — arguing that **modifiers or stochastic developmental variation**, not allele severity, drive expressivity. This is a well-posed research question.

---

## 12. Treatment

**There is no disease-specific, disease-modifying, or targeted therapy for CFNDS.** Management is entirely **symptomatic, anatomical, and habilitative**, delivered by a multidisciplinary craniofacial/genetics/cardiology team. No treatment guideline exists for CFNDS specifically; care follows the guidelines for each constituent anomaly.

### Pharmacotherapy

- **No disease-specific pharmacotherapy.**
- **Antibiotic prophylaxis in asplenia** is the one pharmacological intervention with a strong, specific indication in the subset with asplenia/heterotaxy: penicillin prophylaxis plus a low threshold for empiric treatment of febrile illness (standard asplenia protocols).
- Peri-operative and heart-failure medications as dictated by the specific cardiac lesion (diuretics, afterload reduction) — lesion-directed, not disease-directed.
- **Pharmacogenomics:** No CPIC or PharmGKB guidance applies to *CCDC32*. **No PGx relevance identified.**

**Suggested NCIT annotation:**
```yaml
- name: Antimicrobial Prophylaxis for Asplenia
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
  therapeutic_modality: SMALL_MOLECULE
```

### Advanced therapeutics

- **Gene therapy:** **None. Not in development.** No preclinical program exists. (Conceptually challenged: the pathology is established during embryogenesis and is structural — postnatal gene replacement could not correct a cleft palate or a septal defect.)
- **Cell therapy:** None.
- **RNA-based therapies (ASO/siRNA/mRNA):** **None.** Note that despite the exon 3–4 deletion, **exon-skipping/splice-modulating ASO strategies are not applicable** — the lesion is a genomic deletion producing loss of protein, not a correctable splice defect, and the therapeutic window is prenatal.
- **Targeted therapy:** **None.** No druggable node has been proposed. (The AP-2 assembly pathway is not currently a therapeutic target for any indication.)
- **Immunotherapy:** Not applicable.

### Surgical and interventional (the principal therapeutic modality)

| Intervention | Typical timing | Purpose |
|---|---|---|
| **Cleft lip repair (cheiloplasty)** | ~3–6 months | Lip closure, feeding, appearance |
| **Cleft palate repair (palatoplasty)** | ~9–18 months | Palatal closure; **timed to speech development** |
| **Alveolar bone grafting** | ~8–11 years | Alveolar continuity, dental eruption |
| **Secondary speech surgery (pharyngoplasty)** | as needed | Velopharyngeal insufficiency |
| **Cardiac surgical repair** — AVSD repair, VSD closure, pulmonary valvotomy/valvuloplasty | lesion-dependent; AVSD typically 3–6 months | Hemodynamic correction |
| **Tympanostomy tube placement** | as needed, often at cleft repair | Middle-ear effusion, conductive hearing loss |
| **Orchidopexy** | 6–18 months | Cryptorchidism |
| **Gastrostomy** | if feeding failure severe | Nutrition |
| **Orthopedic/spinal management** | as needed | Kyphosis |

**Suggested NCIT annotations (verified via OLS unless noted):**
```yaml
- name: Cleft Palate Repair
  treatment_term:
    preferred_term: palatorrhaphy
    term: {id: NCIT:C168380, label: Palatorrhaphy}
  therapeutic_modality: SURGERY

- name: Congenital Heart Defect Surgical Repair
  treatment_term:
    preferred_term: surgical procedure
    term: {id: NCIT:C15329, label: Surgical Procedure}   # safe, reachable from NCIT:C25218
  therapeutic_modality: SURGERY
```
⚠️ NCIT:C157806 "Cardiac Surgery" also exists but may sit outside the `NCIT:C25218` (Clinical Intervention or Procedure) subtree used by the dismech `TreatmentTerm` dynamic enum — **validate with `just validate-terms` before using it**; `NCIT:C15329` is the safe fallback.

### Supportive and rehabilitative

| Intervention | NCIT | Modality |
|---|---|---|
| Speech and language therapy — **high priority** (cleft + DD + hearing) | NCIT:C159273 | BEHAVIORAL |
| Physical therapy | NCIT:C15302 | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Nutritional/feeding support | NCIT:C15433 (Nutritional Support) — see CLAUDE.md caution on modality tagging | — |
| Supportive care (general) | NCIT:C15747 | — |
| Genetic counseling | NCIT:C15240 | — |
| Hearing amplification / hearing aids | **No suitable NCIT clinical-action term** — omit `term:`, keep free-text `preferred_term`; `therapeutic_modality: DEVICE` | DEVICE |
| Developmental early intervention / special education | NCIT:C15315 (Rehabilitation) | BEHAVIORAL |

### Experimental treatments

**No clinical trials exist for CFNDS.** A ClinicalTrials.gov search yields **no interventional or observational study** recruiting CFNDS or *CCDC32* patients. **No NCT identifiers to report.** Do not curate a `clinical_trials:` block for this entry.

### Treatment outcomes

- **Response rates:** **No CFNDS-specific outcome data.** Outcomes of cleft repair and CHD repair in CFNDS patients have not been separately reported.
- **Side effects / adverse events:** No disease-specific pharmacovigilance signal (no disease-specific drug). Surgical risks are the standard risks of the respective procedures.

### Treatment strategy

- **Algorithm:** No CFNDS-specific pathway. Practical approach: (1) confirm molecular diagnosis; (2) complete the baseline evaluation — echocardiogram, brain MRI, abdominal imaging for situs/spleen, audiology, ophthalmology, renal ultrasound, feeding assessment, developmental assessment; (3) refer to a multidisciplinary craniofacial team; (4) stage cleft and cardiac surgery per standard protocols; (5) institute early intervention and hearing surveillance; (6) **if asplenic, start antibiotic prophylaxis and asplenia vaccination immediately**; (7) genetic counselling for the family.
- **Combination therapies:** Not applicable in the pharmacological sense; management is inherently multimodal/multidisciplinary.
- **Personalized/genotype-guided treatment:** **None available.** No genotype-guided management stratification exists — and with all reported alleles being complete LoF, none is currently plausible.

---

## 13. Prevention

### Prevention levels

- **Primary prevention (preventing occurrence):** **The only effective primary prevention is reproductive** — genetic counselling, carrier testing, and reproductive options in at-risk (typically consanguineous) families. There is **no modifiable exposure** to target. Population-level consanguinity counselling programs reduce the aggregate burden of AR disease but are not CFNDS-specific.
- **Secondary prevention (early detection):** **Prenatal ultrasound/fetal MRI in at-risk pregnancies** is proven to detect the phenotype (fetus A-II-2). **Targeted prenatal molecular testing** (CVS/amniocentesis for the known familial variant) is definitive. Postnatally, **early molecular diagnosis** enables timely baseline evaluation.
- **Tertiary prevention (preventing complications in affected individuals)** — this is where the highest-value, concrete actions lie:
  - **Asplenia protocol**: lifelong antibiotic prophylaxis + immunization + fever action plan. Prevents the most likely preventable death.
  - **Audiology surveillance** from birth: prevents hearing loss compounding speech/language deficit.
  - **Timely palatoplasty within the speech-critical window**: prevents durable velopharyngeal speech impairment.
  - **Cardiac surveillance and timely repair**: prevents pulmonary vascular disease and heart failure.
  - **Feeding/nutrition management**: prevents failure to thrive.
  - **Early developmental intervention**: optimizes attainable function.

### Immunization

**Highly relevant in the asplenic subset.** Standard functional-asplenia immunization: **pneumococcal (conjugate + polysaccharide), meningococcal (ACWY and B), and Haemophilus influenzae type b**, plus annual influenza. Otherwise, routine childhood immunization per national schedule.

**Suggested annotation:** `treatment_term: NCIT:C15346` (Vaccination), `therapeutic_modality: VACCINE`.

### Screening and early detection

- **Population screening programs:** **None applicable.** Not newborn-screenable (no biochemical marker); too rare for population carrier screening.
- **Genetic screening in families:** Carrier testing of at-risk relatives; **preimplantation genetic testing for monogenic disease (PGT-M)** and **prenatal diagnosis (CVS/amniocentesis)** are both technically available once the familial variant is characterized. For families whose variant is a **deletion**, ensure the prenatal assay is deletion-capable (targeted MLPA/ddPCR or breakpoint-spanning PCR — a standard variant-specific Sanger assay will fail).
- **Risk stratification:** Prior risk is driven by consanguinity and by an affected sibling (1 in 4 recurrence).

### Behavioral interventions

**Not applicable** to disease occurrence. Standard periconceptional care (folic acid, avoidance of teratogens) is appropriate general practice but has **no established effect on CFNDS risk** and should not be curated as a CFNDS protective factor.

### Counseling

**Genetic counselling is the cornerstone of prevention.** Content should include:
- **Autosomal recessive inheritance; 25% recurrence risk** for each pregnancy of carrier parents
- **Carrier parents are unaffected** (supported by gnomAD constraint: pLI 0.19, LOEUF 0.76)
- **Extended-family carrier risk** in consanguineous pedigrees; offer cascade testing
- **Availability of PGT-M and prenatal diagnosis**
- **Honest communication of prognostic uncertainty** — with ~6 published patients and no adult data, families must be told that long-term outcome is genuinely unknown
- Consanguinity counselling for the wider kindred where culturally appropriate

**NCIT:** `NCIT:C15240` Genetic Counseling.

### Public health / environmental interventions

**Not applicable.** No environmental determinant. The only population-level lever is consanguinity-related genetic services and premarital/preconception carrier screening programs in high-consanguinity populations — a general AR-disease intervention, not CFNDS-specific.

### Prophylaxis

- **Antibiotic prophylaxis for asplenia** — the one strongly indicated prophylactic medication (see above).
- **Endocarditis prophylaxis** per standard cardiology guidelines for the specific repaired/unrepaired cardiac lesion.

---

## 14. Other Species / Natural Disease

### Taxonomy of species with relevant biology

| Species | NCBI Taxon | Relevance |
|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | The only species with naturally occurring CFNDS |
| *Danio rerio* (zebrafish) | NCBITaxon:7955 | Principal experimental model (§15) |
| *Mus musculus* (mouse) | NCBITaxon:10090 | Cell-line source (IMCD3); no published whole-animal *Ccdc32* model |

### Breed

**Not applicable.** No breed-associated CFNDS-equivalent disorder has been described. **No VBO identifiers apply.**

### Orthologous genes

- **Zebrafish *ccdc32*:** a **single ortholog**, with **46% amino-acid identity and 64% similarity** to human CCDC32 *[PMC7268788, full text]*. Modest conservation, but functionally sufficient — depletion recapitulates the human phenotype.
- **Mouse *Ccdc32*:** ortholog exists (used for the IMCD3 siRNA experiments, targeted via si*Ccdc32*). MGI record exists; I could not retrieve an IMPC phenotype page (404), and **no IMPC null-allele phenotype data were located.**
- Human NCBI Gene ID 90416 is the anchor for ortholog lookup (Alliance of Genome Resources / HomoloGene).

### Natural disease in other species

**None known.** **No OMIA entry, no veterinary case series, no spontaneous animal disorder** corresponding to CFNDS has been reported. There is no companion-animal or wildlife counterpart, and no veterinary health importance.

### Comparative biology

- **Evolutionary conservation of mechanism:** Strong. Harel et al. concluded that **"CCDC32 plays an evolutionarily conserved role in cilia formation in the vertebrate left/right organizing center"** *[full text]*. The AP-2 adaptor complex and its assembly chaperones (AAGAB, CCDC32) are deeply conserved across eukaryotes, and the AP-2 assembly mechanism described in human cells is expected to be broadly conserved.
- **Comparative pathology — concordances:** zebrafish `ccdc32` crispants reproduce reduced head size (≈ microcephaly), altered facial cartilage morphology (≈ craniofacial dysmorphism/clefting), cerebellar hypoplasia, disrupted cardiac looping, and laterality randomization (≈ situs inversus).
- **Comparative pathology — divergences:** the zebrafish model shows **no global developmental delay (normal body length)**, and clefting per se cannot be modelled in fish (no secondary palate) — only the homologous pharyngeal cartilage patterning.

### Transmission

**Not applicable.** CFNDS is a germline monogenic disorder. **No zoonotic potential, no cross-species transmission, no infectious component.**

---

## 15. Model Organisms

### 15.1 Zebrafish (*Danio rerio*, NCBITaxon:7955) — the primary and best-characterized model

**Model type:** vertebrate, mammalian-adjacent developmental model; **F0 CRISPR crispant** (mosaic knockout).

**Construction:** Two distinct sgRNAs (sgRNA1, sgRNA2) targeting **non-overlapping regions of exon 2**, injected with Cas9 protein at the one-cell stage. **Editing efficiency: 85% (sgRNA1) and 70% (sgRNA2)** mosaic alterations in F0 crispants *[PMC7268788, full text]*. Two independent guides is good practice and substantially strengthens the specificity of the result.

**Expression pattern in zebrafish:** *ccdc32* detected as early as **1 hour post-fertilization**; localized to the **developing head and neural tube** throughout embryogenesis, and **particularly concentrated in the Kupffer's vesicle region** — a spatial pattern that closely prefigures the human phenotype (head, CNS, laterality).

**Phenotypes observed** *[all MODEL_ORGANISM evidence]*:

| Zebrafish phenotype | Human counterpart | Statistics |
|---|---|---|
| Significant reduction in **head size** at 3 dpf | Microcephaly (HP:0000252) | Significant vs uninjected and sgRNA-only controls |
| Altered **facial cartilage morphology** (ceratohyal angle) | Craniofacial dysmorphism / clefting | P < 0.05 |
| **Hypoplastic cerebellum** (anti-α-acetylated tubulin) | Cerebellar vermis hypoplasia (HP:0001320) | Qualitative + morphometric |
| Disrupted **cardiac looping** at 2 dpf (normal/midline/reversed) | Cardiac malformation, looping abnormality | Both sgRNAs |
| Aberrant ***southpaw (spaw)*** expression at 18-somite stage — bilateral or right-sided instead of left | Situs inversus, asplenia (HP:0003363, HP:0001746) | Qualitative scoring |
| **Kupffer's vesicle cilia reduced in number and length** at 10-somite stage | Ciliary mechanism hypothesis | Number P<0.001; length P<0.05; one-way ANOVA + Tukey |
| **Normal body length** | — | Explicitly noted: no global developmental delay |

> "ccdc32 depletion recapitulates the human phenotypes" — PMID:32307552 (verbatim, abstract)

**Phenotype recapitulation quality:** **Good for craniofacial, cerebellar, cardiac-looping, and laterality domains.** This is a genuinely convergent model — four independent human phenotype domains reproduced.

**Limitations:**
- **F0 crispants are mosaic**, not stable germline nulls — a **stable mutant line has not been reported** and is an obvious next step.
- **Cleft lip/palate cannot be modelled** — zebrafish have no secondary palate; only homologous pharyngeal cartilage patterning is assessable.
- **Intellectual disability/global developmental delay cannot be modelled**; body length was explicitly normal.
- **Situs inversus and asplenia** are assessed indirectly (spaw expression, cardiac looping) rather than as terminal organ situs.
- Crispant phenotypes can carry p53-dependent off-target/toxicity artefacts; the two-independent-guide design mitigates but does not eliminate this.
- Modest human–fish protein identity (46%) limits inference about specific residues/motifs.

**Resource:** ZFIN (the ZFIN publication record ZDB-PUB-220423-8 exists for the Abdalla paper; I was unable to retrieve the *ccdc32* gene record — ZFIN returned a CAPTCHA/traffic page — so **the ZFIN gene ID should be looked up before curation**).

### 15.2 Mammalian cell models

**mIMCD3 5-HT6-GFP (mouse inner medullary collecting duct, ciliated reporter line)** *[IN_VITRO]*
- siRNA against *Ccdc32* (5 nM) vs non-targeting control; 24 h serum starvation to induce ciliogenesis; knockdown validated by qRT-PCR with three primer sets
- **Result: significantly reduced % ciliated cells (P<0.01) and reduced cilium length (P<0.05 to P<0.001)**
- Rigor: >500 cells per replicate, 4 replicates, >1000 cilia measured, **imaging blinded to condition** — a well-controlled experiment
> "Cilia formation is similarly impaired in ciliated mouse inner medullary collecting duct cells" *[full text]*

**HeLa and other human cell lines (2024–2026 mechanism studies)** *[IN_VITRO]*
- ***CCDC32* knockout HeLa cells:** loss of all four AP-2 subunits at steady state; loss of plasma-membrane AP-2 puncta; strongly reduced transferrin-receptor endocytosis with elevated surface TfR; impaired GLUT4 internalization
- **siRNA knockdown:** accumulation of unstable flat clathrin assemblies; inhibited CCP invagination; reduced TfnR uptake
- **Structure–function:** deletion constructs (e.g. CCDC32(1-54), mimicking the patient truncations) fail to rescue CCP stabilization; **patient-mutant CCDC32 is defective in binding AP-2 α and σ2** — this is the closest thing to a **direct functional validation of patient alleles**
- **In vitro reconstitution with PIP2-containing liposomes** — the membrane-switch experiments (Sci Adv 2026)

**Patient-derived cells:** **None reported** beyond the RNA-seq performed on patient material for diagnosis (PMID:41639596). **No patient fibroblast, iPSC, organoid, or neuronal model of CFNDS exists.** This is a major and readily addressable gap.

### 15.3 Mouse (*Mus musculus*, NCBITaxon:10090)

- **No published *Ccdc32* whole-animal knockout or knock-in mouse model exists.** I found no IMPC phenotype data (the queried IMPC gene page returned 404) and no MGI-recorded allele phenotype for a *Ccdc32* null.
- **A commercially available conditional (flox) allele exists** — a *Ccdc32*-flox C57BL/6 line (Cyagen `Ccdc32em1flox`) is catalogued — but **no phenotype has been published from it.** Curate as "resource available, phenotype unpublished," not as a characterized model.
- **Highly informative surrogate models — the AP-2 subunit knockouts:**
  - ***Ap2b1* (β2) null:** *"mice lacking the single-copy AP-2 β subunit gene AP2B1 survive until birth but then die shortly afterwards, the only obvious abnormality being that they have a cleft palate"* *[JCS review, full text]* — **strikingly convergent with the CFNDS core phenotype.** Survival is attributed to partial redundancy with the AP-1 β paralog.
  - ***Ap2s1* (σ2) null:** early embryonic lethal (~E3.5–E9.5).
  - ***Ap2m1* (μ2) null:** early embryonic lethal.
  - **Complete AP-2 loss:** *"Complete loss of AP-2 is early embryonic lethal"* *[JCS review, full text]*
  - **Interpretive value:** these establish a **dosage/severity gradient** in which CFNDS sits at the mild, viable end — consistent with CCDC32 loss producing **partial** rather than complete AP-2 deficiency, and directly supporting the cleft palate and cardiac phenotypes as AP-2-attributable.
  ⚠️ **Do not conflate** the **AP-2 adaptor complex α subunit (AP2A1/AP2A2)** with the **AP-2α transcription factor (TFAP2A)** — searches readily mix them, and TFAP2A knockouts also produce cleft palate and cardiovascular defects for entirely unrelated reasons.

### 15.4 Applications and gaps

**What current models support:** ciliogenesis assays; left-right patterning; craniofacial cartilage morphometry; cardiac looping; AP-2 assembly biochemistry and structural biology; CCP dynamics by TIRF; transferrin-uptake functional readouts; **direct testing of patient alleles in rescue assays**.

**What no current model supports:** the neurodevelopmental/cognitive phenotype; cleft lip and palate morphogenesis in a mammal; longitudinal/adult natural history; therapeutic testing.

**Highest-value next models:** (1) a **stable germline zebrafish *ccdc32* mutant line**; (2) a **constitutive or neural-crest-conditional mouse *Ccdc32* knockout** using the existing flox allele — with explicit assessment of palate, cardiac septation, situs, and brain; (3) **patient-derived iPSC neural crest cells and cerebral/cardiac organoids**; (4) **patient fibroblast AP-2 abundance and transferrin-uptake assays** as a candidate functional diagnostic for VUS resolution.

**Model databases:** ZFIN (zebrafish), MGI / IMPC / IMSR / KOMP (mouse), Alliance of Genome Resources (ortholog integration), Cellosaurus (HeLa, mIMCD3 lines).

---

## Appendix A — Consolidated Reference List

| PMID | Citation | Type | Role |
|---|---|---|---|
| **32307552** | Harel T, Griffin JN, Arbogast T, Monroe TO, Palombo F, Martinelli M, Seri M, Pippucci T, Elpeleg O, Katsanis N. *Loss of function mutations in CCDC32 cause a congenital syndrome characterized by craniofacial, cardiac and neurodevelopmental anomalies.* Hum Mol Genet. 2020;29(9):1489-1497. DOI 10.1093/hmg/ddaa073. PMC7268788 | HUMAN_CLINICAL + MODEL_ORGANISM + IN_VITRO | **Founding paper.** Gene discovery, 2 families/3 individuals, zebrafish, ciliary model. Sole HPOA annotation source. |
| **35451546** | Abdalla E, Alawi M, Meinecke P, Kutsche K, Harms FL. *Cardiofacioneurodevelopmental syndrome: Report of a novel patient and expansion of the phenotype.* Am J Med Genet A. 2022;188(8):2448-2453. DOI 10.1002/ajmg.a.62762 | HUMAN_CLINICAL | 3rd patient; **defines the core phenotype**; first to propose the AP-2 link. |
| **38818818** | Fernandes da Rocha D, Quental R, Grangeia A, Pinto Moura C. *A novel homozygous deletion in CCDC32 gene causing cardiofacioneurodevelopmental syndrome: the fourth patient reported.* Clin Dysmorphol. 2024;33(3):114-117. DOI 10.1097/MCD.0000000000000501 | HUMAN_CLINICAL | 4th patient. ⚠️ **No abstract in PubMed; full text paywalled — no quotable snippet obtainable.** |
| **41639596** | Albuainain F, Venema M, Schot R, Huigen G, Mancini GMS, van Ham TJ, Barakat TS. *Two siblings with CCDC32-related cardiofacioneurodevelopmental syndrome diagnosed by clinical RNA-sequencing and review of literature.* Eur J Hum Genet. 2026. DOI 10.1038/s41431-026-02023-y. PMC13046869 | HUMAN_CLINICAL | **Most recent + only review.** Sibling pair; RNA-seq diagnosis; literature synthesis. ⚠️ Full text not retrievable (403/paywall) — the feature-by-feature review table could not be extracted. |
| **39145939** | Wan C, Puscher H, Ouyang Y, Wu J, Tian Y, Li S, Yin Q, Shen J. *An AAGAB-to-CCDC32 handover mechanism controls the assembly of the AP2 adaptor complex.* PNAS. 2024. PMC11348294 | IN_VITRO | **Defines CCDC32's molecular function.** Tests a CFNDS patient mutant. |
| **41489497** | Yang Z, Yang C, Huang Z, Xu P, Li Y, Han L, Peng L, Wei X, Pak JE, Svitkina T, Schmid SL, Chen Z. *CCDC32 stabilizes clathrin-coated pits and drives their invagination.* eLife. 2026. PMC12768407 (preprint: PMID 38979322) | IN_VITRO | CCP dynamics; maps the aa78-98 α-helix removed by disease alleles. |
| **42234739** | Sloan DE, Matthews AE, Yanagisawa H, Tedamrongwanish T, Cannon K, Simmons J, Chappell G, Nicely NI, Berlow R, Kikkawa M, Baker RW. *CCDC32 collaborates with the membrane to assemble the AP-2 clathrin adaptor complex.* Sci Adv. 2026. PMC13267310 (preprint: PMID 40799577) | IN_VITRO / structural | Structural mechanism; PIP2 membrane as molecular switch. |
| **39250673** | *Stepwise assembly of the AP2 endocytic clathrin adaptor complex.* PNAS. 2024. PMC11420168 | Commentary | Contextual commentary on the assembly pathway. |
| — | Sanger JM et al. *Adaptor protein complexes and disease at a glance.* J Cell Sci. 2019;132(20):jcs222992 | Review | AP-2 subunit KO phenotypes; AP2S1/AP2M1 human disease. |

**Structured / database sources:** MONDO:0030873 (OLS/EBI); MedGen UID 1721861; HPO API annotations for OMIM:619123; HGNC:28295; ClinGen gene-disease validity (Syndromic Disorders GCEP, 2024-10-18, MODERATE); ClinVar (VCV001690313, VCV002431643, VCV000988600, VCV000988601, VCV002580223); gnomAD v4.0 constraint; Human Protein Atlas ENSG00000128891.

---

## Appendix B — Explicit "No Data" Register

For honest curation, these are **confirmed absences**, not unsearched areas:

| Domain | Status |
|---|---|
| Orphanet entry / ORPHA code | **Not found** — ontology coverage gap |
| ICD-10 / ICD-11 specific code | **None assigned** |
| Dedicated MeSH descriptor | **None** |
| GARD entry | Not identified |
| Prevalence / incidence estimate | **None** — literature case count only |
| Natural history study, registry, longitudinal cohort | **None** |
| Adult patient reported | **None** — oldest is 9 years |
| Survival / mortality data | **None** |
| QoL instrument data (EQ-5D/SF-36/PROMIS) | **None** |
| Diagnostic criteria / consensus guideline / society statement | **None** |
| Biomarker (diagnostic, prognostic, monitoring) | **None** |
| Prognostic model or genotype-phenotype correlation | **None** |
| Clinical trials (ClinicalTrials.gov) | **None** |
| Disease-modifying / targeted / gene / RNA therapy | **None; none in development** |
| Pharmacogenomics (CPIC/PharmGKB) | **Not applicable** |
| Methylation episignature | **None** |
| Patient transcriptomics/proteomics/metabolomics (mechanistic) | **None** (RNA-seq used diagnostically only) |
| Patient-derived fibroblast / iPSC / organoid model | **None** |
| Published mouse model phenotype | **None** (flox allele commercially available, unpublished) |
| IMPC data for *Ccdc32* | **Not found** |
| Naturally occurring disease in other species / OMIA entry | **None** |
| Environmental, infectious, lifestyle, or GxE factor | **None; not applicable** |
| ClinGen dosage sensitivity / variant / actionability curation | **None** (validity curation only) |
| Newborn or population carrier screening | **Not applicable / not indicated** |

---

## Appendix C — Suggested High-Priority `discussions` Entries for the KB Record

1. **`kind: KNOWLEDGE_GAP`** — Adult phenotype, survival, and natural history are entirely unknown (oldest reported patient age 9).
2. **`kind: KNOWLEDGE_GAP`** — Are the two ~32.6-kb deletions (ClinVar VCV001690313 / VCV002431643) the same recurrent, repeat-mediated allele? Breakpoint and haplotype analysis needed. *Proposed experiment: breakpoint-junction sequencing and SNP-haplotype comparison across reported deletion carriers.*
3. **`kind: HUMAN_MODEL_MISMATCH`** — The zebrafish `ccdc32` crispant supports a **primary ciliary** mechanism, but the 2024–2026 human-cell structural/biochemical work assigns CCDC32 a **primary AP-2 assembly** function, and patients lack the cardinal ciliopathy features (cystic kidney disease, polydactyly, retinal dystrophy). Whether the ciliary defect is primary or secondary to CME failure is unresolved. *Proposed experiments: test ciliogenesis in CCDC32-KO human cells with AP-2 rescue; assay ciliary receptor trafficking; characterize a stable zebrafish mutant line and a neural-crest-conditional mouse KO.*
4. **`kind: KNOWLEDGE_GAP`** — All reported alleles are complete LoF yet expressivity is markedly variable (hypertelorism vs hypotelorism; AVSD+heterotaxy vs isolated VSD; fetus with no cardiac defect). Modifiers, stochastic developmental variation, or both?
5. **`kind: KNOWLEDGE_GAP`** — No functional assay exists to classify *CCDC32* VUS (e.g. the p.Tyr157Ter ClinVar VUS). *Proposed experiment: validate patient-fibroblast AP-2 subunit abundance and transferrin-uptake as a clinical-grade functional readout.*

**Suggested `conforms_to` candidates:** none of the existing dismech modules is a clean fit. `pharyngeal_arch_patterning_serial_homology` is a *partial* conceptual neighbour (cranial-neural-crest-derived multi-element craniofacial malformation) but CFNDS's lesion is a trafficking/assembly chaperone rather than an arch-patterning or ribosome/spliceosome lesion, and the CFNDS bundle is not confined to arch derivatives — **do not force conformance.** If a module is created, the natural one is a new **"AP-2 adaptor assembly / clathrin-mediated endocytosis deficiency"** module, which would already have three worked conformers across the pathway (CCDC32→CFNDS, AP2M1→DEE, AP2S1→FHH3, AAGAB→punctate PPK type 1) — a genuinely reusable conserved mechanism.

---

**Sources:**
- [OMIM #619123 — CARDIOFACIONEURODEVELOPMENTAL SYNDROME; CFNDS](https://omim.org/entry/619123)
- [OMIM *618941 — CCDC32](https://www.omim.org/entry/618941)
- [Harel et al. 2020, Hum Mol Genet (PMID:32307552)](https://pubmed.ncbi.nlm.nih.gov/32307552/) · [full text PMC7268788](https://pmc.ncbi.nlm.nih.gov/articles/PMC7268788/) · [publisher](https://academic.oup.com/hmg/article/29/9/1489/5822585)
- [Abdalla et al. 2022, Am J Med Genet A (PMID:35451546)](https://pubmed.ncbi.nlm.nih.gov/35451546/) · [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.62762)
- [Fernandes da Rocha et al. 2024, Clin Dysmorphol (PMID:38818818)](https://pubmed.ncbi.nlm.nih.gov/38818818/) · [journal](https://journals.lww.com/clindysmorphol/citation/2024/07000/a_novel_homozygous_deletion_in_ccdc32_gene_causing.3.aspx)
- [Albuainain et al. 2026, Eur J Hum Genet (PMID:41639596)](https://www.nature.com/articles/s41431-026-02023-y)
- [Wan et al. 2024, PNAS — AAGAB-to-CCDC32 handover (PMC11348294)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11348294/)
- [Yang et al. 2026, eLife — CCDC32 stabilizes clathrin-coated pits (PMC12768407)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768407/)
- [Sloan et al. 2026, Sci Adv — CCDC32 collaborates with the membrane (PMC13267310)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13267310/)
- [Stepwise assembly of the AP2 endocytic clathrin adaptor complex, PNAS 2024 (PMC11420168)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11420168/)
- [Adaptor protein complexes and disease at a glance, J Cell Sci 2019](https://journals.biologists.com/jcs/article/132/20/jcs222992/224736/Adaptor-protein-complexes-and-disease-at-a-glance)
- [MedGen UID 1721861 — CFNDS](https://www.ncbi.nlm.nih.gov/medgen/1721861)
- [HPO annotations for OMIM:619123](https://ontology.jax.org/api/network/annotation/OMIM:619123)
- [MONDO:0030873 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http://purl.obolibrary.org/obo/MONDO_0030873)
- [HGNC:28295 — CCDC32](https://rest.genenames.org/fetch/symbol/CCDC32)
- [ClinGen curation results for CCDC32 (HGNC:28295)](https://search.clinicalgenome.org/kb/genes/HGNC:28295)
- [ClinVar — CCDC32 variants](https://www.ncbi.nlm.nih.gov/clinvar/?term=CCDC32%5Bgene%5D)
- [gnomAD v4.0 gene constraint](https://gnomad.broadinstitute.org/news/2024-03-gnomad-v4-0-gene-constraint/)
- [Human Protein Atlas — CCDC32 (ENSG00000128891)](https://www.proteinatlas.org/ENSG00000128891-CCDC32)
- [GeneCards — CCDC32](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CCDC32)
- [Cyagen Ccdc32-flox mouse model](https://www.cyagen.com/mouseatlas/S-CKO-09782)
- [AAGAB mutations in punctate palmoplantar keratoderma (PMC4282079)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4282079/)
- [Mutations in AP2S1 cause familial hypocalciuric hypercalcemia type 3, Nat Genet](https://www.nature.com/articles/ng.2492)
- [Modeling AP2M1 developmental and epileptic encephalopathy in Drosophila, DMM](https://journals.biologists.com/dmm/article/18/11/dmm052419/369896/Modeling-AP2M1-developmental-and-epileptic)