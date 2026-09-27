---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T19:06:01.071504'
end_time: '2026-08-08T19:12:44.534676'
duration_seconds: 403.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: AA Amyloidosis
  mondo_id: ''
  category: Complex
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
  web_search_requests: 22
  num_turns: 30
  total_cost_usd: 2.3409681
  session_id: dd1e0d74-d236-5ea2-a472-23fc42f509bd
  stop_reason: end_turn
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AA Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **AA Amyloidosis** covering all of the
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

# AA Amyloidosis: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** AA amyloidosis (amyloid A amyloidosis; historically "secondary" or "reactive" systemic amyloidosis) is an acquired, potentially fatal complication of chronic inflammatory, infectious, or autoinflammatory disease in which the acute-phase reactant **serum amyloid A (SAA)** is proteolytically cleaved, misfolds, and deposits extracellularly as insoluble cross-β-sheet **AA amyloid fibrils** in multiple organs, most severely the kidney. It is one of the ~40 recognized human systemic amyloidoses classified by fibril precursor protein, and clinically it is dominated by progressive proteinuria and renal failure (PMC11219434, "AA Amyloidosis: A Contemporary View," Mirioglu et al., *Curr Rheumatol Rep* 2024;26:248-259, PMID:38568326).

**Key identifiers:**
- **MONDO:** MONDO:0019439
- **Orphanet:** ORPHA:85445 (also grouped under ORPHA:69, Amyloidosis)
- **ICD-10-CM:** E85.3 (Secondary systemic amyloidosis)
- **OMIM (related/hereditary form):** A rare autosomal-dominant hereditary form driven by an SAA1 promoter mutation has been described (Kidney International 2021; distinct from the acquired/reactive form that dominates clinical practice) — see Section 4/9. The classic acute-phase-reactant gene entry is OMIM *104750 (SAA1).
- **MeSH:** Amyloidosis (D000686); the AA-specific concept is indexed under "Amyloidosis" with SAA protein subheading.
- **UniProt:** P0DJI8 (SAA1_HUMAN), P0DJI9 (SAA2_HUMAN)

**Synonyms:** Secondary amyloidosis; reactive systemic amyloidosis; inflammatory amyloidosis; amyloid A (AA) amyloidosis; SAA amyloidosis.

**Data provenance.** Most quantitative disease-level knowledge (incidence, organ-involvement frequencies, survival statistics) derives from **aggregated multicenter cohort studies and national amyloidosis referral centers** (e.g., the UK National Amyloidosis Centre, French multicenter renal-transplant cohorts, and large FMF registries) rather than individual EHR mining — this is a rare disease with concentrated expert-center case ascertainment (PMID:38568326; French AJKD/AJT transplant cohort studies below).

---

## 2. Etiology

### 2a. Disease Causal Factors

AA amyloidosis is fundamentally a **disease of sustained inflammation**: any condition producing chronically or recurrently elevated SAA for a sufficient duration and concentration can, in a susceptible host, trigger fibrillogenesis. Recognized etiologic categories (PMID:38568326; PMC11219434):

- **Chronic inflammatory arthritides** (~60-70% of cases in industrialized nations): rheumatoid arthritis (historically the single largest cause), ankylosing spondylitis, psoriatic arthritis, juvenile idiopathic arthritis.
- **Autoinflammatory (periodic fever) syndromes**: familial Mediterranean fever (FMF, *MEFV*), TNF receptor-associated periodic syndrome (TRAPS, *TNFRSF1A*), cryopyrin-associated periodic syndromes/CAPS (*NLRP3*, includes Muckle-Wells syndrome), mevalonate kinase deficiency/hyper-IgD syndrome (*MVK*).
- **Chronic infections**: tuberculosis, leprosy, chronic osteomyelitis, bronchiectasis, chronic pyelonephritis, decubitus ulcers, IV drug use with recurrent skin/soft-tissue infection — the dominant cause in low/middle-income countries.
- **Inflammatory bowel disease**: Crohn's disease (more than ulcerative colitis).
- **Vasculitides**: giant cell arteritis, Takayasu arteritis, polyarteritis nodosa, granulomatosis with polyangiitis.
- **Primary immunodeficiencies**: common variable immunodeficiency, hypo/agammaglobulinemia (recurrent infection as the proximate driver).
- **Malignancy** (uncommon): renal cell carcinoma, Hodgkin lymphoma, Castleman disease.
- **Idiopathic**: up to ~20-25% of cases have no identifiable overt inflammatory trigger.

**Direct quote (mechanistic causal statement):** "the exact mechanisms remain incompletely understood" but "inflammatory cytokines—particularly interleukin-6—stimulate hepatic production of serum amyloid A (SAA). Sustained elevation of plasma SAA concentrations leads to aggregation into fibrillar deposits" (Westermark GT, Fändrich M, Westermark P. *Annu Rev Pathol* 2015;10:321-44, PMID:25387054).

### 2b. Risk Factors

**Genetic risk factors:**
- ***SAA1* allelic variation** — the single strongest documented genetic modifier. Human SAA1 has five common coding-region alleles (SAA1.1–SAA1.5, differing at codons 52 and 57: alpha=Val52, beta=Val57, gamma=Ala52/Ala57). SAA1.1 predominates in European populations and its homozygosity is associated with increased amyloidosis risk in RA and FMF; SAA1.3 homozygosity confers elevated risk in Japanese populations. Population allele-frequency differences (SAA1.1-dominant in Caucasians vs. near-equal SAA1.1/1.3/1.5 distribution in Japanese cohorts) partly explain geographic variation in amyloidosis penetrance (GeneCards SAA1; PMID:12687559, PMID:15018633, PMC3577815, PMC11535276).
- ***MEFV* genotype in FMF** — homozygosity for the p.Met694Val (M694V) missense variant is the strongest single MEFV risk allele for renal AA amyloidosis, particularly documented in North African Jewish FMF cohorts; combined SAA1α/α + M694V/M694V homozygosity substantially compounds risk (PMID:12687559).
- **Country/ethnicity of residence** — identified in FMF cohorts as a risk factor for amyloidosis independent of MEFV genotype and disease duration, implicating additional genetic-background or environmental modifiers (PMC11219434).
- **Rare autosomal-dominant hereditary SAA1 promoter mutation** — a single-nucleotide promoter variant (chr11:18287683 T>C, hg19) linked to the amyloidogenic SAA1.1 haplotype doubles basal SAA1 promoter activity, producing chronically elevated baseline SAA (without other acute-phase protein elevation) and autosomal-dominant AA amyloidosis in the absence of an inflammatory trigger (LOD score >5 across 12 affected/6 unaffected relatives) (*Kidney Int* 2021, PMID pending indexing — ScienceDirect S0085-2538(21)00867-X).

**Environmental / demographic risk factors:**
- **Obesity** — an independently identified susceptibility factor for *idiopathic* AA amyloidosis; obese/idiopathic-AA patients are older and more obese than FMF- or RA-associated AA cases (Amyloid 2018, PMID:29364741). Adipose tissue itself expresses SAA1/SAA2 (as an "adipokine"), correlating with BMI and contributing to chronic low-grade systemic inflammation independent of hepatic SAA (PLOS Medicine 2006, PMID:16737350).
- **Older age at disease onset/diagnosis** (median historically ~50 years, more recent cohorts report up to 70), reflecting cumulative inflammatory burden and improved recognition of idiopathic/obesity-associated cases (PMID:38568326).
- **Male sex** — slightly increased representation in most cohorts.
- **Duration and control of the underlying inflammatory disease** — untreated/undertreated chronic inflammation (e.g., colchicine-noncompliant FMF) is the dominant modifiable environmental/behavioral risk factor.
- **Socioeconomic/geographic setting** — infection-driven AA amyloidosis predominates where chronic infections (TB, leprosy, osteomyelitis) are more prevalent (developing regions); rheumatic-disease-driven AA predominates in industrialized nations with better infection control.

### 2c. Protective Factors

- **Colchicine compliance in FMF** is the best-documented protective intervention: in a cohort of 960 FMF patients, the cumulative rate of proteinuria at 11 years was 1.7% in colchicine-compliant patients vs. 48.9% in non-compliant patients (PMC11219434, citing FMF colchicine outcome studies).
- **Effective suppression of the underlying inflammatory disease** by any modality (biologics, DMARDs, anti-infective therapy) that durably normalizes SAA is protective against amyloid progression and, when applied early, can permit amyloid regression.
- No specific protective genetic variants (e.g., an SAA1 "resistant" allele analogous to APOE2 in Alzheimer disease) are firmly established, though non-SAA1.1/1.3 genotypes appear less amyloidogenic in the populations studied.

### 2d. Gene-Environment Interactions

The clearest documented gene-environment interaction is the **combination of amyloidogenic SAA1 genotype (SAA1α/α or SAA1.3 homozygosity) with a chronic inflammatory driver** (FMF genotype severity, RA disease duration, or obesity-associated adipose inflammation): neither the SAA1 risk allele alone nor inflammation alone reliably produces amyloidosis — sustained elevation of SAA to a critical, prolonged concentration in a host carrying an amyloidogenic SAA1 haplotype is required (PMC11219434; PMID:29364741 for the obesity+SAA1 interaction specifically). Ethnic/geographic background further modulates this interaction beyond MEFV genotype alone in FMF cohorts, suggesting unidentified additional genetic or environmental modifiers (PMC11219434).

---

## 3. Phenotypes

AA amyloidosis phenotypes are best organized by organ system; renal disease dominates the clinical picture in >90% of patients at presentation.

### Renal (most frequent; ~90% at presentation)
- **Proteinuria** — HP:0000093 (Proteinuria); often nephrotic-range.
- **Nephrotic syndrome** — HP:0000100 (Nephrotic syndrome); reported in >50-63% of patients (PMC11219434; PMID:17714761 reports 63.1%).
- **Progressive chronic kidney disease / renal insufficiency** — HP:0012622 (Chronic kidney disease); ~75% of patients show renal insufficiency at some point (PMID:17714761).
- **Acute kidney injury** — HP:0001919 (Acute kidney injury), seen in the rare "amyloid storm" presentation.
- **Renal failure / end-stage kidney disease** — HP:0000083 (Renal insufficiency) progressing to ESKD; ~10% present already in kidney failure.
- **Nephrogenic diabetes insipidus** — HP:0009806, reported with tubulointerstitial-predominant deposition patterns.
- Onset: variable, typically adult-onset, insidious over months-to-years except the acute "amyloid storm" variant in FMF (days-to-weeks).
- Severity/progression: progressive without treatment; a landmark large study found untreated 5-year renal survival poor.

### Systemic/Constitutional
- **Weight loss** — HP:0001824.
- **Fatigue/weakness** — HP:0025406 / HP:0001324 (Muscle weakness) — reported as one of the most common overall manifestations.
- **Peripheral edema** — HP:0000969, secondary to nephrotic-range proteinuria and hypoalbuminemia.
- **Orthostatic hypotension** — HP:0001278.

### Hepatosplenic
- **Hepatomegaly** — HP:0002240.
- **Splenomegaly** — HP:0001744.
- Clinically these are frequent radiographic/pathologic findings but usually functionally silent; elevated alkaline phosphatase (HP:0003155, Elevated alkaline phosphatase) is a marker of hepatic amyloid activity rather than hepatic failure.

### Gastrointestinal (~30%)
- **Chronic diarrhea** — HP:0002014 (Diarrhea), often refractory to standard antidiarrheal treatment; the predominant GI symptom.
- **Malabsorption** — HP:0002024.
- **Gastrointestinal hemorrhage** — HP:0002239.
- **Macroglossia** — HP:0000158 (occurs, but far less frequent than in AL amyloidosis — an important differentiating feature).
- Rarely: intestinal pseudo-obstruction.

### Cardiac (relatively uncommon compared with AL amyloidosis)
- **Cardiomyopathy / increased left ventricular wall thickness** — HP:0001635 (Congestive heart failure), HP:0001712 (Cardiomyopathy); left ventricular wall thickness >12 mm (absent hypertension) suggests amyloid infiltration, but overt heart failure is uncommon relative to AL/ATTR amyloidosis (PMC11219434) — an important differential-diagnosis clue.

### Neurologic
- **Peripheral neuropathy** — HP:0009830 — infrequent (contrasts with AL amyloidosis, where it is common).
- **Carpal tunnel syndrome** — HP:0100039 — infrequent in AA compared with AL/ATTR forms.

### Endocrine
- Adrenal insufficiency, hypothyroidism (secondary to amyloid infiltration of endocrine glands) — reported but uncommon.

### Laboratory abnormalities
- Elevated **serum amyloid A (SAA)** and **C-reactive protein (CRP)** — the central biomarkers, tracked longitudinally as surrogates of disease activity and amyloid regression risk.
- Hypoalbuminemia, dyslipidemia (secondary to nephrotic syndrome).
- Elevated alkaline phosphatase as above.

### The "Amyloid Storm" phenotype (FMF-specific, rare)
A distinct acute presentation: "acute illness, marked by substantial proteinuria, elevated inflammatory markers, and rapid progression to kidney failure within weeks," typically triggered by an infection or other acute inflammatory insult in FMF patients (PMC11219434). Age of onset: any age in established FMF; onset pattern: acute/subacute (days-weeks) — distinct from the otherwise chronic, insidious natural history.

### Quality-of-life impact
No AA-amyloidosis-specific validated QoL instrument was identified in this search; QoL burden is dominated by the consequences of nephrotic syndrome (fatigue, edema, dietary restriction), chronic diarrhea, and progression to dialysis-dependence, each independently associated with substantial functional impairment per general CKD/dialysis QoL literature (not amyloid-specific; general inference, flagged as such).

---

## 4. Genetic/Molecular Information

### Causal/Contributory Genes
AA amyloidosis is **not a single-gene Mendelian disease** in its usual (acquired/reactive) form — it is a complex trait arising from an inflammatory disease acting on a genetically variable SAA/inflammasome background. The relevant genes are:

- **SAA1** (HGNC:10513; Gene ID 6288; chr11p15.1; OMIM *104750) — encodes serum amyloid A1, the dominant fibril-forming precursor isoform in AA deposits.
- **SAA2** (HGNC:10514; chr11p15.1) — a closely related, ~95%-homologous acute-phase isoform; N-terminal SAA2-derived peptide (SAA2-15) has been localized specifically within Congo red-positive amyloid regions by imaging mass spectrometry, implicating it directly in fibril nucleation (PMC9565386).
- **MEFV** (HGNC:6998; chr16p13.3; encodes pyrin) — the causal gene of familial Mediterranean fever, the single most important monogenic *upstream trigger* disease for AA amyloidosis worldwide. Pyrin is a component of the pyrin inflammasome, driving caspase-1 activation and IL-1β production upon dysregulation.
- **TNFRSF1A** (TRAPS), **NLRP3** (CAPS/Muckle-Wells), **MVK** (hyper-IgD/mevalonate kinase deficiency) — the other major monogenic autoinflammatory "upstream trigger" genes, each conferring variable AA amyloidosis risk (see Section 9).

### Pathogenic Variants
- **SAA1 alleles (not classically "pathogenic variants" in the ACMG sense, but disease-modifying common polymorphisms):** SAA1.1 (Val52/Val57, "alpha"), SAA1.2, SAA1.3 (predominant in Japanese populations), SAA1.4, SAA1.5 (Ala52/Ala57, "gamma") — differ by 1-2 amino acids at codons 52/57. Functional consequence of the amyloidogenic alleles: SAA1.1 shows "increased susceptibility of serum amyloid A 1.1 to degradation by MMP-1," generating the amyloidogenic 76-residue AA fragment more readily (PMC11219434).
- **MEFV p.Met694Val (M694V)** — classified pathogenic/high-penetrance for severe FMF phenotype and amyloidosis risk (ClinVar); homozygosity is the key genotype-amyloidosis association. Other MEFV variants (p.M680I, p.M694I) are more common in some Arab populations and associated with lower amyloidosis risk.
- **SAA1 promoter regulatory variant** chr11:18287683 T>C (hg19), on the amyloidogenic SAA1.1 haplotype background — a gain-of-expression (not missense) mechanism causing autosomal-dominant hereditary AA amyloidosis via chronically doubled basal SAA1 transcription (Kidney Int 2021).
- **Somatic vs. germline:** All AA-amyloidosis-relevant variants (SAA1 allelic variants, MEFV, TNFRSF1A, NLRP3, MVK) are **germline**; there is no recognized somatic/clonal component (this is the key biological distinction from AL amyloidosis, which arises from a somatic clonal plasma-cell/B-cell disorder).
- **Allele frequency:** SAA1.1 is the majority allele in European-ancestry populations (gnomAD/1000 Genomes frequency data were not independently re-derived in this search but are cited as dominant in Caucasian cohorts per GeneCards/PMC3577815); MEFV carrier frequency is high (up to 1 in 5-7) in Mediterranean-basin populations (Sephardic/North African Jews, Armenians, Turks, Arabs) consistent with FMF's status as one of the most common autosomal recessive diseases in those groups (general FMF epidemiology, not independently re-verified here).

### Functional Consequences / Molecular Mechanism of Misfolding
The 122-amino-acid, ~12 kDa SAA1/SAA2 apolipoprotein precursor undergoes **proteolytic cleavage by matrix metalloproteinases (MMPs)** to a ~76-amino-acid AA fragment. This cleavage, combined with local physicochemical factors (acidic pH, elevated temperature, heparin/heparan sulfate proteoglycans), increases resistance to further proteolysis and promotes conformational conversion to a **cross-β-sheet amyloidogenic state**. Fibril formation is **nucleation-dependent**: once a fibrillar nucleus forms, it "recruits and catalyzes the conversion of native molecules" in a self-propagating cascade (PMID:25387054). Cofactors implicated in fibril stabilization/deposition include serum amyloid P component (SAP), heparan sulfate, and apolipoproteins (PMC11219434). Cryo-EM has resolved AA fibril core structures directly from patient tissue, showing "species complementarity" of the pathological fold (PMC6405766).

### Modifier Genes
- **SAA1** itself functions as the principal modifier of amyloidosis risk in patients with an inflammatory trigger disease (FMF, RA) — i.e., it modifies penetrance/severity rather than causing disease alone.
- **MICA polymorphisms** have also been reported as a modifying factor for amyloidosis risk in FMF alongside MEFV and SAA1 (PMID:15018633).

### Epigenetic Information
No AA-amyloidosis-specific epigenetic (DNA methylation/histone) studies were identified in this search; SAA transcriptional induction is primarily driven by classical cytokine-responsive transcription factor activation (NF-κB, C/EBP) downstream of IL-1β/IL-6/TNF-α signaling rather than a documented disease-specific epigenetic mechanism. Flagged as **not available/not established** for this disease.

### Chromosomal Abnormalities
None recognized; AA amyloidosis is not associated with aneuploidy, translocations, or copy-number disorders. **Not applicable.**

---

## 5. Environmental Information

- **Environmental/occupational factors:** No specific toxin, radiation, or occupational chemical exposure is established as a direct AA amyloidosis trigger; risk operates indirectly through chronic inflammatory or infectious disease (e.g., occupational exposures causing chronic osteomyelitis or silicosis-associated inflammation) rather than a direct toxic mechanism. **ECTO term candidate:** exposure to chronic infection/inflammatory stimulus (general, disease-mediated rather than a discrete chemical exposure).
- **Lifestyle factors:** **Obesity** is the best-documented lifestyle-adjacent risk factor (Section 2b), acting through adipose-tissue SAA production and chronic low-grade systemic inflammation (PMID:16737350, PMID:29364741). Poor **medication adherence** (e.g., colchicine non-compliance in FMF) is the principal modifiable behavioral risk factor for progression (PMC11219434).
- **Infectious agents:** Chronic bacterial infections are direct etiologic triggers rather than "risk factors" per se — most importantly **Mycobacterium tuberculosis** (chronic pulmonary/extrapulmonary TB), **Mycobacterium leprae** (leprosy), and pyogenic osteomyelitis pathogens (commonly *Staphylococcus aureus*). These remain the dominant AA amyloidosis triggers in resource-limited settings where chronic untreated infection is more prevalent (PMC11219434). NCBI Taxonomy: *Mycobacterium tuberculosis* (NCBITaxon:1773); *Mycobacterium leprae* (NCBITaxon:1769); *Staphylococcus aureus* (NCBITaxon:1280).

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Trigger → Clinical Manifestation)

1. **Trigger:** Chronic inflammatory, infectious, or autoinflammatory disease (Section 2a) produces sustained elevation of pro-inflammatory cytokines.
2. **Cytokine-driven hepatic SAA overproduction:** IL-6 (primary driver), IL-1β, and TNF-α stimulate hepatocyte transcription and secretion of SAA1/SAA2 as acute-phase apolipoproteins, normally associated with HDL. GO term: **GO:0006953** (acute-phase response); **GO:0070669** (response to interleukin-6); molecular players: IL6 (HGNC:6018), IL1B (HGNC:5992), TNF (HGNC:11892).
3. **Sustained pathologic SAA elevation:** Prolonged (not merely transient acute-phase) elevation to critical plasma concentrations is required — this is the rate-limiting upstream lesion distinguishing amyloidogenic from ordinary acute-phase physiology.
4. **Proteolytic cleavage / misfolding:** Extracellular/tissue proteases (notably MMPs, e.g., MMP-1) cleave the 122-aa SAA precursor to a ~76-aa AA fragment; the amyloidogenic SAA1.1/SAA1.3 alleles are preferentially susceptible to this cleavage. GO: **GO:0006508** (proteolysis); cellular process: **GO:0034629** (cellular protein-containing complex localization) is less specific — better: **GO:1990830** or general "amyloid fibril formation" **GO:1990000** (amyloid fibril formation).
5. **Nucleation-dependent fibrillogenesis:** Misfolded AA fragments adopt a cross-β-sheet conformation; nucleation seeds recruit and convert additional native/cleaved SAA molecules in a self-propagating cascade, stabilized by cofactors (serum amyloid P component, heparan sulfate proteoglycans, apolipoproteins).
6. **Tissue deposition:** Extracellular AA fibril deposits accumulate first in perivascular/mesangial spaces, especially in kidney (glomerular mesangium and capillary walls), spleen (red/white pulp), liver (space of Disse/portal areas), and adrenal glands.
7. **Organ dysfunction:** Glomerular amyloid deposition disrupts the filtration barrier → proteinuria/nephrotic syndrome → progressive nephron loss → CKD/ESKD. Analogous architectural disruption underlies hepatosplenic and GI dysfunction.

### Cellular Processes and Cell Types Involved
- **Hepatocytes** (CL:0000182) — primary site of SAA biosynthesis under cytokine stimulation.
- **Macrophages** (CL:0000235) — implicated in local AA fibril processing/propagation; notably, AA amyloidosis has been experimentally shown transferable via peripheral blood monocytes in animal models, supporting a monocyte/macrophage role in disease transmission of the amyloid-enhancing seed (PLOS ONE, PMC3308).
- **Glomerular mesangial cells** (CL:0000650) and **glomerular endothelial cells** (CL:0002144) — sites of amyloid deposition and secondary injury in the kidney.
- **Adipocytes** (CL:0000136) — a peripheral, non-hepatic source of SAA in obesity-associated idiopathic AA amyloidosis.

### Protein Dysfunction
SAA/AA amyloid pathology is a **gain-of-toxic-aggregation** process rather than loss-of-function: native SAA retains its lipid-transport/immune-signaling roles, but a fraction of the chronically elevated, proteolytically processed pool undergoes conformational conversion to insoluble, protease-resistant β-sheet fibrils that are cytotoxic and architecturally disruptive to tissue. UniProt: P0DJI8/P0DJI9 (SAA1/SAA2); structural fold: cross-β amyloid, resolved by cryo-EM directly from ex vivo patient fibrils (PMC6405766).

### Metabolic Changes
SAA functions physiologically as a component of HDL particles influencing lipid transport; chronic overproduction and diversion into amyloid fibrils is associated with dyslipidemia (secondary largely to nephrotic syndrome rather than a primary SAA lipid-metabolism defect). SAA is now also recognized as an obesity-associated **adipokine**, directly linking adipose tissue inflammation, lipid metabolism, and systemic SAA elevation (PMID:16737350).

### Immune System Involvement
Central and causal: SAA is itself an acute-phase innate-immune protein with roles in leukocyte chemotaxis and antibacterial defense; its pathologic overproduction is a direct consequence of dysregulated innate immune/inflammasome signaling (IL-1β/pyrin axis in FMF; NLRP3 inflammasome in CAPS). The disease is thus best framed as a **maladaptive consequence of chronic innate immune activation**, not autoimmunity in the classical adaptive-immune sense, though it frequently complicates autoimmune/rheumatic disease (RA).

### Tissue Damage Mechanisms
Amyloid deposits cause tissue injury through **direct structural/architectural disruption** (glomerular filtration barrier, hepatic sinusoidal architecture, splenic parenchyma) and possible direct cytotoxicity of prefibrillar oligomeric SAA species (analogous to other amyloidoses), rather than through oxidative stress or classical ischemic mechanisms as the primary driver.

### Molecular Profiling / Advanced Technologies
- **Proteomics:** Laser-microdissection/mass spectrometry (LMD-MS) of Congo-red-positive tissue is now the diagnostic and mechanistic gold standard for confirming AA (vs. AL, ATTR, or other) fibril composition, identifying the AA-specific 76-residue N-terminal fragment signature; achieves >99% subtype-identification accuracy where available (PMC11219434).
- **Imaging mass spectrometry:** Localized the N-terminal SAA2-derived peptide SAA2-15 specifically within Congo-red-positive amyloid regions, directly implicating this fragment in fibril core formation (PMC9565386).
- **Cryo-EM:** Solved ex vivo AA fibril core structures directly from patient-derived tissue, revealing species-specific structural polymorphism ("species complementarity") (PMC6405766).
- Single-cell/spatial transcriptomic and multi-omic human AA amyloidosis-specific datasets were **not identified** in this search (contrast with the feline model, Section 14/15, where multi-omic data do exist) — flagged as a **gap**, likely reflecting AA amyloidosis's rarity and tissue-biopsy-based (rather than fresh-tissue -omics) diagnostic workflow in humans.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Kidney (UBERON:0002113) — nearly universal involvement, clinically dominant.
- **Secondary:** Liver (UBERON:0002107), spleen (UBERON:0002106), adrenal gland (UBERON:0002369) — "readily accessible" sites classically demonstrated by SAP scintigraphy; gastrointestinal tract (UBERON:0005409/intestine) — clinically significant in ~30%; heart (UBERON:0000948) — infrequent but prognostically important when present; thyroid gland (UBERON:0002046) — occasionally involved.
- **Body systems:** renal/urinary system, gastrointestinal system, hepatobiliary system, endocrine system, and (less often) cardiovascular and peripheral nervous systems.

### Tissue and cell level
- **Kidney:** glomerular mesangium and capillary basement membrane (mesangial and subendothelial amyloid), with a distinct tubulointerstitial-predominant deposition pattern seen in some cases producing milder proteinuria but nephrogenic diabetes insipidus.
- **Liver:** perisinusoidal (space of Disse) deposition.
- **Spleen:** deposition in both red and white pulp regions.
- **Blood vessel walls** — perivascular amyloid deposition is a common early feature across organs.

### Subcellular level
Amyloid is an **extracellular** deposit (GO Cellular Component: **GO:0005576**, extracellular region), not an intracellular/organellar pathology — distinguishing it mechanistically from intracellular proteinopathies. Electron microscopy shows "rigid, randomly oriented, unbranched fibrils with a thickness of 8-12 nm," distinguishing AA (and other systemic) amyloid from fibrillary glomerulonephritis (15-20 nm fibrils) and immunotactoid glomerulonephritis (30-60 nm microtubules) (PMC11219434).

### Localization
Deposition is typically **bilateral/systemic** rather than lateralized, consistent with a circulating precursor protein depositing wherever local tissue conditions (vascularity, extracellular matrix composition) favor fibril nucleation and growth.

---

## 8. Temporal Development

### Onset
- Adult-onset in the great majority of acquired/reactive cases; **median diagnosis age historically ~50 years**, with more recent cohorts reporting up to age 70, reflecting an aging population with better-controlled acute inflammatory disease but cumulative burden and rising idiopathic/obesity-associated cases (PMC11219434).
- Onset in **childhood/adolescence** occurs specifically in the context of pediatric-onset autoinflammatory disease (FMF, CAPS, TRAPS, hyper-IgD syndrome) — e.g., pediatric renal AA amyloidosis reported in children with hyper-IgD syndrome/MVK deficiency (PMC4044039).
- Onset pattern: typically **insidious/chronic** (progressive proteinuria over months to years); the **"amyloid storm"** variant in FMF is a distinct **acute** presentation evolving over days-to-weeks.

### Progression
- **Disease course:** progressive and cumulative without effective control of the underlying inflammatory driver; amyloid deposits are not spontaneously resorbed under ongoing inflammatory stimulation.
- **Rate:** variable, dependent on the degree and duration of SAA elevation; the eprodisate RCT quantified a "mean rate of decline in creatinine clearance" of 15.6 mL/min/1.73m²/year in untreated (placebo) progression vs. 10.9 with eprodisate (PMID:17554116/NEJM 2007), giving a concrete natural-history progression benchmark.
- **Stages:** proteinuria → nephrotic syndrome → progressive CKD → end-stage kidney disease requiring renal replacement therapy; this renal staging sequence is the disease's principal natural-history framework (no formal AJCC-style staging system exists for AA amyloidosis specifically).

### Patterns
- **Remission/regression:** Amyloid deposit *regression* (documented histologically and by SAP scintigraphy) is achievable when SAA is durably suppressed to near-normal levels by treatment of the underlying disease — "decreased [SAA] levels have been consistently associated with the regression of amyloid deposition, improved organ function, and reduced mortality" (PMC11219434). This is a critically important and clinically actionable natural-history feature.
- **Critical treatment window:** Treatment is explicitly **time-sensitive** — "delayed control of the inflammation cannot prevent the development of amyloid fibril deposits" (PMC11219434), i.e., once substantial fibril deposition and organ damage has occurred, later cytokine suppression halts but does not reliably reverse structural damage (though biochemical/histologic regression is possible for still-active deposits).

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence:** ~1-2 cases per million person-years in European cohorts (likely underestimated in resource-limited settings with less biopsy access) (PMC11219434).
- **Autopsy-based incidence:** 0.50-0.86% in Western autopsy series (higher than clinically diagnosed rates, implying substantial underdiagnosis).
- **Relative frequency among amyloidoses:** AA amyloidosis now represents only **2.9% of all amyloidosis cases** in contemporary Western referral cohorts, a marked decline from historical rates, attributed to improved control of RA and other chronic inflammatory disease with modern biologics (PMC11219434).
- **Renal amyloidosis composition:** AA amyloidosis accounts for ~7% of biopsy-proven renal amyloidosis cases in some series (vs. AL amyloidosis as the dominant renal amyloid type in industrialized settings).

### Inheritance pattern (for the genetic-trigger diseases)
AA amyloidosis itself is not inherited as a single Mendelian trait in its usual form, but its principal monogenic upstream triggers are:
- **FMF (*MEFV*):** autosomal recessive (HP:0000007) — the classic and most important genetic driver of AA amyloidosis worldwide.
- **TRAPS (*TNFRSF1A*):** autosomal dominant (HP:0000006).
- **CAPS (*NLRP3*):** autosomal dominant.
- **Hyper-IgD/mevalonate kinase deficiency (*MVK*):** autosomal recessive.
- **Rare hereditary SAA1-promoter-driven AA amyloidosis (Kidney Int 2021):** autosomal dominant, LOD score >5, full segregation in 12 affected/6 unaffected relatives — a novel, non-MEFV route to hereditary AA amyloidosis via constitutive SAA1 overexpression rather than an inflammasome defect.

### Penetrance / Expressivity by trigger disease
- **TRAPS and CAPS:** amyloidosis incidence ~25% of affected individuals.
- **Muckle-Wells syndrome (CAPS subtype) specifically:** >25% of patients show elevated serum amyloid and at least 25% develop overt amyloidosis.
- **Hyper-IgD syndrome/MKD:** <5% develop amyloidosis, "perhaps because the disease often ameliorates spontaneously in early adulthood" (search result summary of PMC4707170 and related literature).
- **FMF:** amyloidosis penetrance is strongly genotype- and geography-dependent (M694V homozygosity + SAA1α/α + country of residence), and is dramatically reduced by colchicine compliance (1.7% vs. 48.9% cumulative proteinuria at 11 years, compliant vs. non-compliant) — a striking real-world demonstration of environmentally-modifiable penetrance.
- **Founder effects / population-specific mutations:** MEFV M694V shows population-specific enrichment (e.g., North African Jewish FMF cohorts); FMF carrier frequency is markedly elevated in Mediterranean-basin populations (Sephardic and North African Jews, Armenians, Turks, Arabs) consistent with founder-effect population genetics of FMF generally.
- **Consanguinity:** relevant to FMF (autosomal recessive) penetrance in high-consanguinity Mediterranean-basin populations, though not independently re-verified with primary data in this search.

### Population Demographics
- **Affected populations:** Highest FMF-associated AA amyloidosis burden in Mediterranean-basin/Sephardic Jewish, Armenian, Turkish, and Arab populations owing to high MEFV carrier frequency; broader RA/infection-driven AA amyloidosis occurs across all populations, weighted toward regions with higher chronic infectious disease burden (tuberculosis, leprosy, osteomyelitis) in developing countries.
- **Geographic distribution:** Global, but etiologic mix varies strongly by region as above (infection-dominant in low/middle-income countries vs. rheumatic-disease-dominant in high-income countries).
- **Sex ratio:** slight male predominance reported in several cohorts.
- **Age distribution:** predominantly older adults in acquired/idiopathic and RA-associated disease; pediatric and young-adult cases cluster in the monogenic autoinflammatory-syndrome-driven subset.

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Serum amyloid A (SAA)** and **C-reactive protein (CRP)** — key biomarkers for both diagnosis-adjacent risk stratification and (critically) longitudinal monitoring of treatment response and amyloid regression/progression risk. LOINC codes for SAA and CRP exist in standard laboratory ontologies (not individually re-verified here).
- **24-hour urine protein / urine protein-creatinine ratio** — quantifies nephrotic-range proteinuria.
- **Serum creatinine / estimated GFR** — tracks renal function decline (the primary outcome measure in the pivotal eprodisate trial).
- **Serum albumin** — reflects nephrotic-syndrome severity.

### Tissue diagnosis (gold standard)
- **Biopsy with Congo red staining**, showing **apple-green birefringence under polarized light**, is the definitive diagnostic method for amyloid of any type. **Immunohistochemistry with anti-AA antibody** is then required to subtype the fibril as AA (vs. AL, ATTR, etc.) — "in AA amyloidosis, only the AA [antibody] is positive."
- **Less invasive biopsy sites:** abdominal/periumbilical subcutaneous fat pad aspiration and minor salivary gland biopsy — combined sensitivity 77-89%, allowing avoidance of organ biopsy in many cases.
- **Renal biopsy** remains definitive when renal involvement dominates, with electron microscopy showing the characteristic 8-12 nm randomly oriented fibrils.
- **Laser microdissection + mass spectrometry (LMD-MS)** — the modern proteomic gold standard for unambiguous fibril-protein subtyping (>99% accuracy where available, though costly and limited in global availability).
- **Immunoelectron microscopy** — high sensitivity/specificity, limited by expertise availability.

### Imaging
- **123I-labeled serum amyloid P (SAP) component scintigraphy** — historically the premier whole-body amyloid-burden imaging modality, "most useful in AA amyloidosis because the major sites of deposition (liver, kidneys, spleen, and adrenal glands) are readily accessible to the imaging agent," with sensitivity up to 90%; performed at specialized centers (London, Paris) but **unavailable in the United States** because the reagent (human-derived SAP) cannot undergo the required viral inactivation for US regulatory approval.
- **Echocardiography** and **cardiac MRI** — assess for (uncommon but prognostically important) cardiac involvement; late/diffuse subendocardial gadolinium enhancement on CMR is a hallmark of amyloid cardiac infiltration generally (not AA-specific).

### Genetic testing
- **MEFV sequencing** — indicated in any patient with a Mediterranean-basin ancestry background or clinical FMF phenotype, particularly to confirm M694V zygosity given its strong amyloidosis-risk association.
- **TNFRSF1A, NLRP3, MVK sequencing** — indicated when clinical features suggest TRAPS, CAPS, or hyper-IgD syndrome respectively.
- **SAA1 genotyping** (research/specialized use) — informative for amyloidosis-risk stratification in known FMF/RA patients, though not yet standard-of-care clinical testing.
- No standard clinical **gene panel** specific to "AA amyloidosis risk" as a discrete product was identified; genetic testing in practice is organized around the **autoinflammatory-disease gene panels** (periodic fever syndrome panels covering *MEFV*, *TNFRSF1A*, *NLRP3*, *MVK*, and related genes).

### Differential diagnosis
Must be distinguished from **AL (light-chain) amyloidosis** (the other major systemic amyloidosis, more likely to show cardiac involvement, peripheral neuropathy, macroglossia, and carpal tunnel syndrome — features relatively uncommon in AA amyloidosis), **hereditary ATTR amyloidosis**, and other renal-biopsy differentials including fibrillary glomerulonephritis and immunotactoid glomerulonephritis (distinguished by fibril diameter on EM as above).

### Screening
No population-level newborn or carrier screening program exists for AA amyloidosis itself; the relevant screening paradigm is **surveillance of known high-risk populations** — i.e., periodic proteinuria/SAA monitoring in patients with established FMF, TRAPS, CAPS, MKD, or long-standing RA, to detect amyloid nephropathy early enough for effective intervention.

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Historical/untreated natural history:** progression to renal failure and early death without effective control of the underlying inflammatory driver (PMC11219434).
- **Dialysis-dependent AA amyloidosis:** poor survival — reported ranges from as low as **15% survival at 31.8 months** up to **51% at 5 years**, reflecting historically poor outcomes on dialysis alone, worsened by cardiovascular comorbidity and hypotension-prone dialysis tolerance.
- **Historical kidney transplant outcomes:** 10-year patient and graft survival as low as **62.3% and 56.4%**, respectively (older cohorts).
- **Contemporary kidney transplant outcomes** (French multicenter cohort, AJKD 2023, PMID:37741608): substantially improved — **94.0% patient survival at 1 year, 85.5% at 5 years**; **overall graft survival 75.8% at 5 years** — now comparable to outcomes for diabetic nephropathy transplant recipients. **CRP level at time of transplantation** was independently associated with both patient and graft survival, underscoring the importance of inflammatory control at the time of transplant.
- **Post-transplant amyloid recurrence:** histologically confirmed recurrence in AA amyloid grafts occurs in **5.8%** at a median 23.5 months, associated with elevated SAA but (in this cohort) not independently associated with worse outcomes.
- **Mortality after transplant** remains elevated primarily due to **cardiovascular involvement**, underscoring the importance of pre-transplant cardiac assessment.

### Morbidity and Function
Principal morbidity burden derives from progressive CKD/nephrotic syndrome (edema, malnutrition from proteinuria, dyslipidemia, hypercoagulability) and — where present — chronic refractory diarrhea causing malabsorption and weight loss. No AA-amyloidosis-specific validated disability/QoL outcome measure was identified (general CKD/dialysis QoL literature applies but is not amyloid-specific).

### Prognostic Factors
- **Baseline renal function at diagnosis/treatment initiation** — earlier intervention (creatinine <1.5 mg/dL) improves renal prognosis with anti-TNF therapy specifically.
- **Degree and durability of SAA suppression achieved by treatment** — the single most consistently reported prognostic biomarker; sustained near-normalization of SAA correlates with amyloid regression, organ function stabilization/improvement, and reduced mortality.
- **CRP at time of kidney transplantation** — independently prognostic for both patient and graft survival.
- **Cardiovascular comorbidity** — the dominant driver of excess mortality among successfully transplanted patients.

---

## 12. Treatment

### General Principle
"The mainstay of treatment is targeted at managing the underlying pathogenic mechanisms by suppressing the cytokine-induced production of SAA protein by the liver" (PMC11219434) — i.e., AA amyloidosis treatment is fundamentally **treatment of the causal inflammatory disease**, not a disease-specific anti-amyloid drug (with the partial exception of the investigational agents below). Treatment is explicitly time-sensitive: delayed control cannot prevent deposition that has already occurred, though it can halt further deposition and, when SAA is durably suppressed, permit measurable regression.

### Pharmacotherapy — Anti-Inflammatory/Immunomodulatory (the primary treatment class)
- **Colchicine** (CHEBI:3532) — NCIT:C743 (Colchicine) — first-line, foundational therapy for FMF; suppresses inflammasome activation and IL-1β production; long-term compliance data (1.7% vs. 48.9% proteinuria at 11 years) constitute the strongest available prevention evidence in this disease area. NCIT treatment term: NCIT:C15986 (Pharmacotherapy) with therapeutic_agent CHEBI:3532.
- **Anti-TNF-α agents** (e.g., etanercept, infliximab, adalimumab) — retrospective series show variable results: amyloidosis progressed in 46.7%, stabilized in 33.3%, and proteinuria regressed in 20% of a 15-patient cohort over 10 months; a larger prospective 36-patient, 5-year study found >50% proteinuria reduction in more than half of patients. NCIT class term: NCIT:C20401 (Monoclonal Antibody) or specific agent terms (e.g., NCIT:C1873 Infliximab, NCIT:C1656 Etanercept, NCIT:C1420 Adalimumab).
- **Anti-IL-6 (tocilizumab)** (CHEBI/NCIT:C82595 Tocilizumab) — shown in a 42-patient retrospective analysis to be **superior to anti-TNF agents** for decreasing SAA, improving kidney function, and suppressing disease activity; "whole-cohort median pre-treatment SAA fell from 70 to 4 mg/L within 10 days of the first dose," sustained over 23 months of follow-up (PMID:26120866). Also effective in the rare autosomal-dominant SAA1-promoter-mutation hereditary form.
- **IL-1 inhibitors — anakinra (NCIT:C1857), canakinumab (NCIT:C74003), rilonacept** — effective in monogenic autoinflammatory disease (FMF, CAPS/NLRP3-AID, TRAPS, MKD) and in colchicine-resistant/-intolerant FMF; an 11-patient anakinra series and additional canakinumab data showed benefit, including regression of proteinuria with daily anakinra in some patients; IL-1 blockade is specifically recommended for colchicine-resistant FMF-associated amyloidosis.
- Combination/sequencing strategy: colchicine remains first-line for FMF; biologics (anti-IL-1, anti-IL-6, or occasionally anti-TNF) are reserved for colchicine-resistant/intolerant FMF or for the primary rheumatic/inflammatory diseases (RA, JIA, vasculitis) driving non-FMF AA amyloidosis.

### Experimental / Investigational (targeting amyloid deposition directly)
- **Eprodisate (Fibrillex)** (NCIT — investigational small molecule, glycosaminoglycan mimetic) — a Phase II/III RCT (183 patients, 27 centers, 24 months, NEJM 2007, PMID:17554116) found the composite renal-progression/death endpoint occurred in 27% (eprodisate) vs. 40% (placebo), hazard ratio 0.58 (95% CI 0.37-0.93), and creatinine clearance decline was slower (10.9 vs. 15.6 mL/min/1.73m²/year); however, the drug **did not receive regulatory approval**, and subsequent evaluation did not confirm sufficient benefit for approval — "the trial failed to reach primary endpoints [in some analyses] and the substance has not been approved."
- **Miridesap (CPHPC)** + **anti-SAP monoclonal antibody (dezamizumab)** — a two-step approach to deplete circulating serum amyloid P component and then clear residual tissue-bound SAP-amyloid complexes with a therapeutic antibody; "safely triggered clearance of amyloid deposits from the liver and some other tissues" in early trials (NEJM 2015, PMID for the anti-SAP antibody paper: 26221758), but development was **discontinued** after fatal cardiac arrhythmia adverse events in a later oral-formulation study.
- **Antisense oligonucleotides (ASOs) targeting SAA** — reduced amyloid deposition in animal models; **not yet studied in humans** for AA amyloidosis specifically (an analogous strategy to the ASO approach used clinically in ATTR amyloidosis — see the `antisense_oligonucleotide_therapy` mechanism-module pattern in the dismech schema, RNase H knockdown mechanism class).

### Surgical/Interventional and Supportive Care
- **Renal replacement therapy** — hemodialysis or peritoneal dialysis for ESKD; historically poor survival, particularly with cardiac involvement (hypotension-prone).
- **Kidney transplantation** — the optimal treatment for AA-amyloidosis-related kidney failure in appropriately selected patients (see Section 11 for outcome data); requires pre-transplant cardiac evaluation given the cardiovascular mortality signal.
- **Supportive nephroprotective measures:** ACE inhibitors/ARBs for proteinuria reduction, dietary sodium restriction (<2 g/day), loop diuretics for volume overload, and management of nephrotic-syndrome-associated hyperlipidemia and hypercoagulability.
- **Splenectomy** is not a standard treatment (unlike in some historical amyloidosis contexts) — not identified as recommended in current literature reviewed.

### Treatment Outcomes / Adverse Events
- Anti-TNF agents in transplant recipients: better inflammation control but increased infection risk.
- IL-1 inhibitors in FMF kidney-transplant recipients: longer graft survival and lower rejection rates but a paradoxically increased death rate in one 36-patient evaluation, possibly reflecting infection risk or progressive cardiovascular amyloid deposition rather than the drug itself.
- Miridesap/anti-SAP antibody program: discontinued for **fatal arrhythmia** adverse events — an important cautionary data point for amyloid-clearance strategies generally.

### Treatment Strategy / Personalized Medicine
Treatment selection is fundamentally **etiology-directed** (treat the causal disease) and **biomarker-guided** (titrate therapy to SAA/CRP normalization rather than a fixed regimen), representing a pragmatic form of "personalized medicine" already embedded in standard AA amyloidosis management, albeit driven by a conventional biomarker rather than genomic stratification.

---

## 13. Prevention

### Primary Prevention
- **Aggressive, sustained control of the underlying chronic inflammatory/infectious disease** is the principal primary-prevention strategy — most concretely demonstrated by colchicine prophylaxis in FMF, which reduces 11-year cumulative proteinuria incidence roughly 25-fold in compliant vs. non-compliant patients.
- **Early, effective biologic therapy for RA and other inflammatory arthritides** is credited with the observed decline in AA amyloidosis incidence/relative frequency in Western cohorts over recent decades (from a historically larger share of amyloidosis cases to ~2.9% currently).
- **Prompt and adequate treatment of chronic infections** (tuberculosis, osteomyelitis, leprosy) — the principal primary-prevention lever in regions where infection remains the dominant AA trigger.
- **Weight management** — plausible but not rigorously trial-proven primary prevention measure given the obesity-idiopathic AA amyloidosis association.

### Secondary Prevention (early detection in at-risk patients)
- **Routine proteinuria/urinalysis surveillance** in patients with established FMF, other periodic fever syndromes, or long-standing chronic inflammatory arthritis, allowing detection of amyloid nephropathy at a subclinical/early stage when treatment intensification (colchicine dose optimization, biologic escalation) can still prevent progression.
- **Periodic SAA/CRP monitoring** as a surrogate for cumulative amyloidogenic risk in high-risk populations.

### Tertiary Prevention
- Once amyloid nephropathy is established, **aggressive suppression of SAA production** (biologics as above) plus **nephroprotective supportive care** (ACE-I/ARB, sodium restriction) to slow progression to ESKD and preserve residual renal function as long as possible.

### Genetic Counseling / Screening
- **Genetic counseling and cascade family testing** are well-established for FMF and the other autosomal-dominant/recessive autoinflammatory trigger diseases (MEFV, TNFRSF1A, NLRP3, MVK), enabling early identification of at-risk relatives who can then be started on prophylactic colchicine (for FMF) before amyloid complications develop — this is arguably the single most effective genetics-driven prevention pathway in this disease area.
- No population-level newborn or general-population carrier screening program specific to AA amyloidosis exists; screening operates through **targeted family/ethnicity-based cascade testing** in populations with elevated FMF carrier frequency.

### Public Health
Reduction of the global burden of chronic infectious diseases (TB control programs, osteomyelitis prevention/early treatment) constitutes an indirect but real public-health-level AA amyloidosis prevention strategy in lower-resource settings.

---

## 14. Other Species / Natural Disease

AA amyloidosis is **not unique to humans** — it is one of the best-characterized examples of naturally occurring, spontaneous amyloid disease across vertebrate species, making it an unusually rich source of comparative/veterinary disease models.

- **Domestic dog — Chinese Shar-Pei breed** (VBO term applicable): a well-documented **familial predisposition** to renal AA amyloidosis, with medullary interstitial deposition pattern predominating (distinct from the glomerular pattern typical in humans and Abyssinian cats); often associated with recurrent "Shar-Pei fever" episodes analogous conceptually to periodic fever syndromes. Comparative study: 91-case retrospective comparing Shar-Pei vs. non-Shar-Pei dogs (*J Vet Intern Med* 2012, PMID for Segev et al. study referenced above).
- **Domestic cat — Abyssinian and Siamese breeds**: familial AA amyloidosis with breed-specific deposition patterns — predominantly **glomerular** in Abyssinian cats and **hepatic** in Siamese cats. Notably, domestic cats can develop spontaneous amyloidosis at a young age **without evidence of a preceding overt inflammatory condition**, an intriguing parallel to human idiopathic AA amyloidosis. A recent **multi-omic** study characterized Abyssinian cat renal amyloid deposits (*Sci Rep* 2021, PMID for Almeida-Souza/Littlewood et al. — Nature/PMC8052419), and a separate paper characterized proteinuria and candidate urinary biomarkers in feline AA amyloidosis (PMC10800178) — this is the species with the most extensive AA-amyloidosis-specific -omics dataset identified in this research, exceeding what is currently available for human AA amyloidosis.
- **Captive wild felids**: cheetahs and black-footed cats show genetic predisposition to AA amyloidosis in captivity, an important captive-wildlife veterinary health issue.
- **Endangered island fox** (*Urocyon littoralis*): a proteomic study found AA amyloidosis to be **highly prevalent** in this endangered species, of direct conservation-biology relevance (PMC4245998).
- **Cattle, mink, waterfowl, and other domestic/farmed species**: AA amyloidosis is a recognized entity across additional mammalian and avian species per the Merck Veterinary Manual overview, though with less detailed molecular characterization identified in this search.
- **Comparative pathology / evolutionary conservation**: The fundamental SAA→cleavage→misfolding→cross-β-fibril mechanism is conserved from mice through cats, dogs, and humans, though fibril structural details show species-specific "complementarity" (per the cryo-EM comparative structural work, PMC6405766) — i.e., the amyloid fold is not identical across species despite shared precursor biology.
- **Zoonotic potential**: AA amyloidosis is **not an infectious/transmissible disease in the conventional zoonotic sense** — it is a protein-misfolding disorder secondary to each host's own chronic inflammatory state, not a transmissible pathogen (though the amyloid-enhancing-factor phenomenon described in Section 15 shows experimental cross-tissue and cross-individual "seeding" transferability within a species under laboratory conditions, a prion-like propagation property distinct from classical zoonosis).

---

## 15. Model Organisms

AA amyloidosis is unusual among systemic amyloidoses in having a **long-established, highly efficient, and mechanistically informative rodent induction model**, because SAA overexpression and amyloid deposition can be reliably triggered pharmacologically rather than requiring a transgenic construct.

### Model Types and Genetics
- **Mouse (*Mus musculus*)** — the dominant model species. Relevant mouse orthologs (MGI): **Saa1** (MGI:98221), **Saa2** (MGI:98222), **Saa3** (MGI:98223) — mice, like humans, carry multiple SAA paralogs with overlapping but non-identical acute-phase/inflammatory roles.
- **Induced (non-genetic) models — the classical and still most widely used approach:**
  - **Casein-injection model:** repeated subcutaneous/intraperitoneal injection of casein over an extended period chronically elevates SAA and induces amyloid deposition — the original and still-used chronic-inflammation-mimicking model.
  - **Silver nitrate + AEF (amyloid-enhancing factor) model:** administration of an inflammatory stimulus (e.g., silver nitrate, AgNO₃) together with intravenous **AEF** — a protein extract from amyloid-laden spleen or liver of a previously affected animal — produces extensive, rapid amyloid deposits within 3-5 days. AEF dramatically shortens the induction "lag phase" by providing a preformed fibrillar nucleation seed, directly demonstrating the **nucleation-dependent, prion-like seeding mechanism** of AA amyloidogenesis. In the standard protocol, 8-12-week-old mice receive 10 µg AEF intravenously, with deposition proceeding spleen (24-48h) → liver (3-4 days) → kidney (5-7 days), closely recapitulating the organ-involvement sequence seen clinically.
  - **AA amyloidosis is experimentally transferable via peripheral blood monocytes** between animals, further supporting a cellular (macrophage/monocyte)-mediated component of fibril seeding/propagation (PLOS ONE, referenced above).
- **Genetic models:**
  - **IL-1 receptor antagonist knockout (Il1rn⁻/⁻) mice** — spontaneously develop AA amyloid deposition reflecting unopposed IL-1 signaling, and have been used to study deposition, clearance, and re-induction dynamics of AA amyloid (*Vet Pathol* 2017, Watanabe et al.).
  - **H2/IL-6 transgenic mice** — used alongside standard strains in the AEF induction protocol, providing an IL-6-overexpression genetic background that sensitizes to amyloid induction, directly modeling the human IL-6-driven SAA induction axis.
  - Standard **Saa1/Saa2 double-knockout mice** exist and have been used to probe baseline SAA physiology (e.g., altered cholesterol handling under LPS challenge) rather than as an amyloidosis model per se (loss-of-function, as expected, does not produce amyloid disease since SAA itself, not its absence, is pathogenic).
- **Mink (*Neovison vison*)**: AEF-based rapid induction of experimental AA amyloidosis by intravenous AEF injection has also been established in mink as an alternative model species (PMID:18266118), useful for comparative fibril-structure studies.

### Phenotype Recapitulation
The induced mouse models recapitulate the **key organ-deposition sequence** (spleen → liver → kidney) and the **cross-β amyloid fibril ultrastructure** of human disease with high fidelity, and have been essential for elucidating the nucleation-dependent seeding mechanism, testing candidate anti-amyloid therapeutics (including early proof-of-concept for antisense-oligonucleotide SAA knockdown), and generating the cryo-EM fibril structures referenced in Section 6.

### Model Limitations
Induced models depend on **exogenous inflammatory stimuli and/or AEF seeding** rather than spontaneous chronic autoimmune/autoinflammatory disease, so they may not fully capture the decades-long, genetically-modulated (SAA1 allele-dependent) human natural history, nor the specific contribution of individual human trigger diseases (RA, FMF) to the inflammatory milieu. The **naturally occurring feline and canine breed-specific familial forms** (Section 14) may in some respects better model the genetically-predisposed, spontaneously-arising human idiopathic/familial AA amyloidosis phenotype than the pharmacologically-induced mouse models, and — notably — the feline model currently has more extensive multi-omic characterization publicly available than human AA amyloidosis itself.

### Applications
Mouse/mink induction models remain the principal tool for: (1) dissecting the nucleation-seeding mechanism of amyloidogenesis; (2) testing anti-amyloid and anti-SAA therapeutics (including the ASO strategy noted in Section 12) prior to human trials; (3) generating sufficient homogeneous amyloid tissue for structural (cryo-EM) and proteomic studies not readily obtainable from limited human biopsy material.

### Resources
MGI (Saa1: MGI:98221; Saa2: MGI:98222; Saa3: MGI:98223) for mouse genetic/allele resources; no dedicated AA-amyloidosis-specific IMPC/KOMP high-throughput phenotyping line was identified in this search (SAA genes are not primary IMPC amyloidosis-phenotyping targets, consistent with the field's reliance on induced rather than constitutive-knockout models).

---

## Summary of Suggested Ontology Terms for Knowledge-Base Curation

| Category | Suggested terms |
|---|---|
| **MONDO** | MONDO:0019439 (AA amyloidosis) |
| **HPO (phenotypes)** | HP:0000093 Proteinuria; HP:0000100 Nephrotic syndrome; HP:0012622 Chronic kidney disease; HP:0001919 Acute kidney injury; HP:0000083 Renal insufficiency; HP:0002240 Hepatomegaly; HP:0001744 Splenomegaly; HP:0002014 Diarrhea; HP:0002024 Malabsorption; HP:0001635 Congestive heart failure; HP:0009830 Peripheral neuropathy; HP:0000158 Macroglossia; HP:0100039 Carpal tunnel syndrome; HP:0001824 Weight loss; HP:0000969 Edema; HP:0011034 Amyloidosis (general) |
| **GO (biological process)** | GO:0006953 acute-phase response; GO:0006508 proteolysis; GO:1990000 amyloid fibril formation |
| **GO (cellular component)** | GO:0005576 extracellular region |
| **CL (cell types)** | CL:0000182 hepatocyte; CL:0000235 macrophage; CL:0000650 mesangial cell; CL:0002144 glomerular endothelial cell; CL:0000136 adipocyte |
| **UBERON** | UBERON:0002113 kidney; UBERON:0002107 liver; UBERON:0002106 spleen; UBERON:0002369 adrenal gland; UBERON:0000948 heart |
| **HGNC/genes** | SAA1 (HGNC:10513); SAA2 (HGNC:10514); MEFV (HGNC:6998); TNFRSF1A; NLRP3; MVK; IL6; IL1B; TNF |
| **CHEBI** | CHEBI:3532 colchicine |
| **NCIT (treatments)** | NCIT:C15986 Pharmacotherapy; NCIT:C743 Colchicine; NCIT:C82595 Tocilizumab; NCIT:C1857 Anakinra; NCIT:C74003 Canakinumab; NCIT:C1873 Infliximab; NCIT:C15329 Surgical Procedure (transplant context: NCIT:C15289 Organ Transplantation) |

---

## Sources

- [AA amyloidosis - GARD](https://rarediseases.info.nih.gov/diseases/10560/aa-amyloidosis)
- [Orphanet: AA amyloidosis](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=85445)
- [AA amyloidosis - NORD](https://rarediseases.org/mondo-disease/aa-amyloidosis/)
- [AA Amyloidosis: A Contemporary View - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11219434/) (PMID:38568326)
- [AA amyloidosis: pathogenesis and targeted therapy - PubMed](https://pubmed.ncbi.nlm.nih.gov/25387054/)
- [Cryo-EM fibril structures from systemic AA amyloidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6405766/)
- [N-terminal peptide fragment constitutes core of amyloid deposition of serum amyloid A - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9565386/)
- [Amyloidosis in familial Mediterranean fever patients: MEFV genotype and SAA1/MICA polymorphisms - PubMed](https://pubmed.ncbi.nlm.nih.gov/15018633/)
- [Contribution of genotypes at MEFV and SAA1 loci to amyloidosis in FMF - PubMed](https://pubmed.ncbi.nlm.nih.gov/12687559/)
- [SAA1 Gene Polymorphisms on Renal Involvement in Jordanian FMF - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11535276/)
- [SAA1 Polymorphisms Contribution to FMF Susceptibility Japanese - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3577815/)
- [Serum Amyloid A Protein–Associated Kidney Disease - Kidney Medicine](https://www.kidneymedicinejournal.org/article/S2590-0595(22)00125-X/fulltext)
- [AA (Inflammatory) Amyloidosis - Medscape](https://emedicine.medscape.com/article/335559-overview)
- [AA amyloidosis of unknown aetiology: response to IL-1 inhibitors - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10229276/)
- [Tocilizumab in ankylosing spondylitis AA amyloidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8107218/)
- [Therapeutic blockade of IL-6 by tocilizumab in AA amyloidosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/26120866/)
- [AA amyloidosis – Benefits and prospects of IL-6 inhibitors](https://www.tandfonline.com/doi/full/10.1080/14397595.2018.1515145)
- [Kidney Transplantation in Patients With AA Amyloidosis - AJKD](https://www.ajkd.org/article/S0272-6386(23)00834-X/fulltext) (PMID:37741608)
- [Renal Transplantation in AA Amyloidosis Nephropathy - French Multicenter Study - AJT](https://www.amjtransplant.org/article/S1600-6135(22)28159-3/fulltext)
- [A mouse model for serum amyloid A amyloidosis - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0076687999090461)
- [Rapid induction of experimental AA amyloidosis in mink by AEF - PubMed](https://pubmed.ncbi.nlm.nih.gov/18266118/)
- [AA-Amyloidosis Can Be Transferred by Peripheral Blood Monocytes - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0003308)
- [Deposition, Clearance, and Reinduction of AA Amyloid in IL-1Ra Knockout Mice](https://journals.sagepub.com/doi/full/10.1177/0300985816658772)
- [Eprodisate for the Treatment of Renal Disease in AA Amyloidosis - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa065644)
- [Eprodisate in AA amyloidosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/17554116/)
- [A mutation in the SAA1 promoter causes hereditary amyloid A amyloidosis - Kidney International](https://www.kidney-international.org/article/S0085-2538(21)00867-X/fulltext)
- [Familial Mediterranean Fever - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK560754/)
- [Update on management of colchicine resistant FMF - Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-019-1201-7)
- [Secondary amyloidosis in autoinflammatory diseases - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4707170/)
- [TRAPS with renal AA amyloidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7865531/)
- [Renal AA amyloidosis in a child with hyper-IgD syndrome - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4044039/)
- [Obesity is a significant susceptibility factor for idiopathic AA amyloidosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/29364741/)
- [Acute-phase serum amyloid A: an inflammatory adipokine - PLOS Medicine](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.0030287)
- [SAA1 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAA1)
- [SAA1 (104750) - OMIM](https://omim.org/entry/104750)
- [Multi-omic analyses in Abyssinian cats with primary renal amyloid deposits - Scientific Reports](https://www.nature.com/articles/s41598-021-87168-0)
- [Renal Amyloidosis in Dogs: Shar-Pei vs Non-Shar-Pei - J Vet Intern Med](https://academic.oup.com/jvim/article/26/2/259/8451539)
- [Amyloidosis in Animals - Merck Veterinary Manual](https://www.merckvetmanual.com/immune-system/amyloidosis/amyloidosis-in-animals)
- [Proteomic Analysis of AA Amyloidosis in Endangered Island Foxes - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4245998/)
- [Saa1 MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:98221)
- [Saa2 MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:98222)
- [Saa3 MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:98223)
- [Diversity and Complexity of the Mouse Saa1 and Saa2 genes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4160927/)
- [2026 ICD-10-CM Diagnosis Code E85.3](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E85-/E85.3)
- [Mondo Disease Ontology - Monarch Initiative](https://mondo.monarchinitiative.org/)