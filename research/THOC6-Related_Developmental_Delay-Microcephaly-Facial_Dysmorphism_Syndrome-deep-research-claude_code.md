---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:50:31.620057'
end_time: '2026-07-30T23:55:12.427626'
duration_seconds: 280.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: THOC6-Related Developmental Delay-Microcephaly-Facial Dysmorphism
    Syndrome
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
  web_search_requests: 12
  num_turns: 20
  total_cost_usd: 1.6913635
  session_id: fce2c191-78f6-554d-bb4c-6fb4218f2aec
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** THOC6-Related Developmental Delay-Microcephaly-Facial Dysmorphism Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **THOC6-Related Developmental Delay-Microcephaly-Facial Dysmorphism Syndrome** covering all of the
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

I have gathered sufficient primary literature. Here is the comprehensive research report.

---

# THOC6-Related Developmental Delay-Microcephaly-Facial Dysmorphism Syndrome (Beaulieu-Boycott-Innes Syndrome)

## 1. Disease Information

**Overview:** THOC6-related developmental delay-microcephaly-facial dysmorphism syndrome, universally referred to in the literature as **Beaulieu-Boycott-Innes syndrome (BBIS)** or **THOC6 Intellectual Disability Syndrome (TIDS)**, is a rare autosomal recessive neurodevelopmental disorder first delineated in 2013 in a Hutterite kindred. It is caused by biallelic pathogenic variants in *THOC6*, which encodes a subunit of the THO/TREX (transcription-export) mRNA processing and nuclear export complex. The syndrome is characterized by global developmental delay, moderate-to-severe intellectual disability, microcephaly, characteristic but nonspecific facial dysmorphism, and variable multi-organ malformations (cardiac, renal, dental, genitourinary, and corpus callosum anomalies) (Beaulieu et al. 2013, PMID:23621916; Lemire, Innes, Boycott, GeneReviews NBK560442).

**Key Identifiers:**
- **OMIM:** #613680 (Beaulieu-Boycott-Innes syndrome, phenotype); *615403 (THOC6 gene)
- **Gene:** THOC6 (HGNC), chromosome 16p13.3 (per GeneReviews) / 16p13.11–13.3 region
- **MedGen CUI:** C3150939 ("THOC6-related developmental delay-microcephaly-facial dysmorphism syndrome")
- **GTR condition:** C3150939
- **Inheritance:** Autosomal recessive
- **MONDO/Orphanet:** Specific MONDO and ORPHA numeric IDs were not confidently retrievable via web search in this session and should be independently verified directly against the MONDO Ontology Lookup Service and Orphanet before use in a knowledge base (the disease is indexed in Orphanet's rare-disease nomenclature as "Beaulieu-Boycott-Innes syndrome," cross-referenced to OMIM:613680, but the exact ORPHA code was not confirmed here).

**Synonyms:** Beaulieu-Boycott-Innes syndrome (BBIS); THOC6 Intellectual Disability Syndrome (TIDS); THOC6-related intellectual disability; intellectual disability, autosomal recessive, with THOC6 defect.

**Source of information:** Data is derived almost entirely from aggregated case-series/case-report literature (GeneReviews synthesis of ~19–20+ published individuals across ~15+ families as of 2020, with additional case reports through 2024–2025) rather than large-scale EHR/registry data, reflecting the extreme rarity of the condition (Lemire et al., GeneReviews NBK560442; multiple case reports below).

---

## 2. Etiology

**Disease Causal Factors:** BBIS is a purely monogenic, Mendelian disorder. It is caused by biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic missense variants in *THOC6* that impair THO/TREX complex assembly and function (Beaulieu et al. 2013, PMID:23621916; Mattioli et al. 2019, HMG 28(6):952-960, PMID via DOI 10.1093/hmg/ddy391).

**Genetic Risk Factors:**
- **Founder variant:** The original mutation identified, c.136G>A (p.Gly46Arg), is a founder variant in the Hutterite Dariusleut and Lehrerleut populations, with reported carrier frequencies of 3% in Dariusleut controls and 2% in Lehrerleut controls — implying meaningfully elevated recurrence risk in these endogamous communities (Beaulieu et al. 2013, PMID:23621916).
- **Other pathogenic variants reported:** compound heterozygous stop + missense combinations; homozygous missense variants (e.g., a haplotype bearing three amino-acid changes p.Trp100Arg, p.Val234Leu, p.Gly275Asp; p.Gly190Glu); homozygous splice-site variants (e.g., c.155+1G>T, a novel splice-donor variant reported in a Palestinian infant with disorders of sexual development) (Mattioli et al. 2019; PMC12324036, 2024/2025 case report).
- **Consanguinity:** Given autosomal recessive inheritance and multiple reports from consanguineous families (e.g., Palestinian and Indian sibling cases), parental consanguinity is a recognized risk factor for biallelic variant co-occurrence.
- THOC6 itself, unlike other THO complex subunits (THOC1, THOC3, THOC5, THOC7 — all of which show high pLI/loss-of-function intolerance in gnomAD and have no known associated developmental disorder, likely because complete loss is embryonic lethal), appears to tolerate partial loss-of-function in humans, which is thought to explain why *THOC6*, and not the other THO subunits, is the one component in which biallelic hypomorphic variants are compatible with live birth (PMC10884030 / Nature Communications 2024).

**Environmental Risk Factors:** None identified; this is a purely genetic disorder with no known environmental, infectious, or toxin-mediated contribution to primary causation.

**Protective Factors:** No specific genetic modifiers or protective variants have been described. Notably, human cells/embryos appear more tolerant of biallelic THOC6 loss-of-function than mouse embryos (which are embryonic lethal by E9.5–E11.5), suggesting an unidentified human-specific compensatory mechanism for the resulting lncRNA dysregulation and intron-retention burden — an active area of investigation rather than an established protective factor (PMC10884030).

**Gene-Environment Interactions:** None reported; no CTD/PheGenI gene-environment interaction data exists for THOC6-related disease given its recessive Mendelian architecture.

---

## 3. Phenotypes

Phenotype data are drawn primarily from GeneReviews (NBK560442, summarizing published cohorts) and individual case reports.

### Neurodevelopmental
- **Global developmental delay / intellectual disability** — moderate to severe, affecting essentially all reported individuals; present from infancy, stable-to-slowly-progressive course, lifelong. HPO: HP:0001263 (Developmental delay), HP:0002342 (Intellectual disability, moderate/severe forms HP:0002342 family), HP:0001263.
- **Microcephaly** — congenital, typically **2–3 SD below the mean**; the defining "microcephaly" element of the syndrome name. HPO: HP:0000252 (Microcephaly).
- **Corpus callosum dysgenesis** — variably reported (hypoplasia/agenesis). HPO: HP:0007370 (Aplasia/Hypoplasia of the corpus callosum).
- **Ventriculomegaly/hydrocephalus** — reported in multiple cases. HPO: HP:0002119 (Ventriculomegaly), HP:0000238 (Hydrocephalus).
- **Seizures** — rare, documented in only two affected individuals in the literature to date. HPO: HP:0001250 (Seizure).
- **Language delay** — a core, frequently emphasized feature. HPO: HP:0002463 (language delay)/HP:0000750.

### Craniofacial dysmorphism (nonspecific but recurrent gestalt)
- Tall/prominent forehead, deep-set eyes, short and upslanting palpebral fissures, epicanthal folds, long nose with low-hanging columella, triangular face, posteriorly rotated ears, long philtrum, microretrognathia. HPO terms: HP:0000341 (Prominent forehead), HP:0000490 (Deep set eye), HP:0012843 (Upslanted palpebral fissure) / HP:0000582, HP:0000286 (Epicanthus), HP:0000426 (Prominent nasal bridge)/HP:0012810 (long nose), HP:0000308 (Microretrognathia), HP:0000343 (Long philtrum), HP:0000358 (Posteriorly rotated ears).
- These features "are often recognized as consistent with this diagnosis after confirmation" rather than being independently diagnostic (GeneReviews NBK560442).

### Cardiac
- Atrial and/or ventricular septal defects are the most common cardiac anomaly, present in **~47%** of reported cases. HPO: HP:0001631 (Atrial septal defect), HP:0001629 (Ventricular septal defect).
- Peripheral pulmonary stenosis, patent foramen ovale also reported (PMC12324036).

### Renal/Genitourinary
- Unilateral renal agenesis (most common), ectopic kidney, horseshoe kidney. HPO: HP:0000122 (Unilateral renal agenesis), HP:0000085 (Horseshoe kidney).
- Cryptorchidism in males. HPO: HP:0000028 (Cryptorchidism).
- Hypergonadotropic hypogonadism in adolescent/adult individuals (management guidance includes assessing secondary sexual characteristics and offering hormone replacement).
- **Novel expansion (2024/2025):** ambiguous genitalia, hypospadias, fused labioscrotal folds, and anorectal malformation (anal atresia with perineal fistula) reported for the first time in a Palestinian infant with a homozygous splice variant — the authors propose the mechanism may extend to disruption of hypothalamic-pituitary-gonadal axis signaling secondary to impaired THO complex function (PMC12324036, 2024–2025 case report). HPO: HP:0000062 (Ambiguous genitalia), HP:0000047 (Hypospadias), HP:0002251 (Anal atresia).

### Dental
- Multiple dental caries, malocclusion, supernumerary teeth — reported in approximately half of affected individuals. HPO: HP:0000670 (Carious teeth), HP:0000689 (Dental malocclusion), HP:0000660 (Supernumerary teeth).

### Growth
- Low birth weight, postnatal growth failure/short stature — frequent/common. HPO: HP:0001518 (Small for gestational age), HP:0004322 (Short stature).
- Feeding difficulties, occasionally requiring gastrostomy. HPO: HP:0011968 (Feeding difficulties).

### Sensory
- Hearing loss (sensorineural, warranting annual audiology). HPO: HP:0000365 (Hearing impairment).
- Myopia. HPO: HP:0000545 (Myopia).

### Skeletal
- Vertebral segmentation defects. HPO: HP:0003422 (Vertebral segmentation defect).

**Frequency/severity:** Given the very small published cohort (≈19–20+ individuals as of 2020, with sporadic additional single case reports through 2024–2025), most frequency estimates are qualitative or based on small denominators (e.g., "47%" for cardiac defects, "approximately half" for dental issues) rather than robust population-level statistics; frequency qualifiers should be curated conservatively.

**Quality of life impact:** Not formally studied with standardized instruments (no EQ-5D/SF-36 data identified); clinical narrative indicates lifelong cognitive and functional impairment requiring coordinated multidisciplinary care, special education, and in some cases assistive devices (hearing aids, feeding support).

---

## 4. Genetic/Molecular Information

**Causal Gene:** THOC6 (THO complex subunit 6), OMIM *615403, chromosome 16p13.3.

**Pathogenic Variant Spectrum:**
- **c.136G>A (p.Gly46Arg)** — founder missense variant, homozygous in the original Hutterite families (Beaulieu et al. 2013, PMID:23621916).
- **Triple-amino-acid-change haplotype** — p.Trp100Arg, p.Val234Leu, p.Gly275Asp (in cis), and **p.Gly190Glu** — characterized functionally by Mattioli et al. 2019 (HMG 28(6):952-960), shown to relocalize THOC6 protein from nucleus to cytoplasm and disrupt THOC1/THOC5 interaction.
- **c.155+1G>T** — homozygous canonical splice-donor variant (intron 3), classified likely pathogenic, reported in a consanguineous Palestinian family (PMC12324036).
- Compound heterozygous stop + missense combinations reported in multiple families (e.g., Chinese infant, PMC7220430; Indian siblings, PMID:31421288).
- **Variant classification (ACMG/ClinVar):** Multiple THOC6 variants are catalogued in ClinVar (e.g., VCV000561208, VCV000521349) as pathogenic/likely pathogenic.
- **Variant types:** missense, nonsense (stop-gain), splice-site — no large structural/CNV mechanism reported to date; standard first-tier testing (chromosomal microarray) is recommended primarily to exclude alternative diagnoses rather than because THOC6-associated CNVs are common.
- **Population frequency:** Aside from the Hutterite founder allele (2–3% carrier frequency in specific subpopulations), THOC6 pathogenic variants are otherwise very rare/private in gnomAD; variants with population MAF >3.3% are excluded as non-causal in functional studies (PMC10884030/PMC10503840).
- **Somatic vs. germline:** All reported variants are germline; no somatic/mosaic mechanism described.
- **Functional consequence:** Predominantly **loss-of-function / hypomorphic** — reduced or mislocalized THOC6 protein disrupts THO complex tetramer assembly; no gain-of-function or dominant-negative mechanism has been described (biallelic/recessive throughout).

**Modifier Genes:** None established; other THO/TREX components (THOC1, THOC2, THOC3, THOC5, THOC7) are mechanistic pathway partners but are not documented modifiers of THOC6 disease severity in humans. Related but genetically distinct: THOC2 causes an X-linked syndromic intellectual disability via R-loop accumulation/DNA damage (a related mechanistic paradigm) (Nature Communications 2024, PMID:38388532-adjacent article "THOC2...").

**Epigenetic Information:** No specific DNA methylation, histone modification, or chromatin-level abnormality has been reported as a primary driver; however, the disease mechanism itself converges on RNA processing (splicing) rather than classical epigenetic dysregulation.

**Chromosomal Abnormalities:** No recurrent CNV/translocation mechanism identified; disease is due to sequence-level (point/splice) variants.

**HGNC gene symbol:** THOC6 (HGNC ID should be confirmed locally; use lowercase `hgnc:` CURIE per dismech convention).

---

## 5. Environmental Information

No environmental, toxin, occupational, radiation, or lifestyle contributing factors have been described for THOC6-related disease — it is a fully penetrant, purely monogenic autosomal recessive disorder. No infectious trigger or agent is implicated.

---

## 6. Mechanism / Pathophysiology

This is the best-characterized and most recently elucidated aspect of the disease, driven by two 2024 studies (Nature Communications, PMC10884030; and the related PMC10503840/bioRxiv precursor).

**Molecular function of THOC6:** THOC6 is a core subunit of the THO complex, which together with additional factors (UAP56/DDX39B, ALYREF, etc.) forms the larger **TREX (TRanscription-EXport) complex**, classically understood to couple transcription, mRNA processing, and nuclear export of mature mRNAs (Beaulieu et al. 2013; GeneReviews NBK560442).

**Causal chain (established primarily via human iPSC-derived cortical organoids and Thoc6 mutant mouse embryos):**

1. **Trigger:** Biallelic THOC6 loss-of-function/hypomorphic variants → loss or mislocalization of THOC6 protein (cytoplasmic mislocalization for missense alleles; near-absent protein for nonsense alleles).
2. **Proximal molecular lesion:** THOC6 sits at the TREX-tetramer interface, interacting with THOC5 to enable **tetramerization of the TREX complex** (four hexameric THO monomers). Loss of THOC6 abolishes THOC5–THOC6 interaction and tetramer formation while the smaller **TREX dimer is preserved** — meaning bulk nuclear mRNA export is *not* the primary defect (contrary to the originally assumed mechanism).
3. **Downstream molecular consequence:** Instead, TREX tetramer loss causes widespread **alternative pre-mRNA splicing defects** — in one dataset, 3,796 significantly enriched aberrant splicing events, dominated by exon skipping (56%) and intron retention (21%), preferentially affecting long genes with weak splice sites and long introns. Auxiliary export factor ALYREF binding (tetramer-dependent) is also reduced.
4. **Cellular consequence (human cortical organoids / neural progenitor cells, NPCs):** Reduced NPC proliferative capacity, elevated apoptosis (cleaved caspase-3+), retained pluripotency/multipotency marker expression (OCT4 upregulation) with delayed differentiation into doublecortin+ migrating neurons; organoids show thinner pseudostratified neuroepithelium and smaller neural rosettes, with prolonged KI67+/EdU+ co-labeling indicating extended (dysregulated) proliferation before eventual apoptotic loss.
5. **Pathway-level dysregulation:** Splicing/lncRNA disruption cascades into altered signaling required for the proliferative-to-neurogenic transition in corticogenesis — PI3K-AKT/mTOR pathway genes downregulated (>30 genes), TGF-β pathway genes reduced (HAPLN1, INHBA, TGFB2), and paradoxical WNT pathway upregulation mediated through dysregulated lncRNAs (notably MEG3 and MEG8 upregulation).
6. **Tissue/organism-level outcome:** Impaired corticogenesis → microcephaly and global neurodevelopmental impairment; the mechanism plausibly extends to renal, cardiac, and genitourinary organogenesis given the multi-organ phenotype spectrum, though these non-neural manifestations are mechanistically less well studied at the cellular level.

**Species divergence:** *Thoc6*-null/hypomorphic mouse embryos are **embryonic lethal by E9.5–E11.5** (thinner neuroepithelium, increased mitosis and apoptosis at E9.5, developmental delay from E9.5, smaller embryo size), in contrast to humans, who survive to adulthood (oldest reported individuals in their 40s) despite biallelic loss. This suggests **human-specific tolerance/compensation** for the resulting intron-retention and lncRNA dysregulation burden — an open mechanistic question and a strong candidate for a `HUMAN_MODEL_MISMATCH` discussion in a dismech-style entry, since the mouse model does not recapitulate survivability and the translational fidelity of murine apoptotic/proliferative severity to the milder human phenotype is unresolved.

**Suggested ontology terms:**
- **GO (biological process):** GO:0006406 (mRNA export from nucleus), GO:0000398 (mRNA splicing, via spliceosome), GO:0008380 (RNA splicing), GO:0007420 (brain development), GO:0021987 (cerebral cortex development), GO:0043065 (positive regulation of apoptotic process), GO:0008283 (cell population proliferation).
- **GO (cellular component):** GO:0000445 (THO complex part of transcription export complex) / GO:0000346 (transcription export complex), GO:0005634 (nucleus).
- **GO (molecular function):** possible RNA-binding-complex scaffolding activity (specific THOC6 MF term should be verified via UniProt/QuickGO before curation).
- **CL (cell types):** CL:0011020 (neural progenitor cell) / CL:0002608 (embryonic stem cell related) — more precisely CL:0000047 (neural stem cell) / radial glial cell CL:0000681; CL:0000540 (neuron), CL:0000679 (glutamatergic neuron) for migrating cortical neurons.
- **UBERON:** UBERON:0001890 (forebrain), UBERON:0000955 (brain), UBERON:0002021 (neural tube/neuroepithelium - approximate).

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Central nervous system** — brain (microcephaly, corpus callosum dysgenesis, ventriculomegaly/hydrocephalus). UBERON:0000955 (brain), UBERON:0002336 (corpus callosum, if precise UBERON needed verify), UBERON:0002264 (lateral ventricle).
- **Craniofacial skeleton/soft tissue** — dysmorphic facial features. UBERON:0001456 (face).
- **Cardiovascular system** — heart (septal defects). UBERON:0000948 (heart).
- **Renal/urinary system** — kidney (agenesis, ectopia, horseshoe kidney). UBERON:0002113 (kidney).
- **Genitourinary/reproductive system** — gonads, external genitalia (cryptorchidism, ambiguous genitalia, hypogonadism). UBERON:0000992 (gonad), UBERON:0004818 (external genitalia).
- **Dentition** — teeth (caries, malocclusion, supernumerary teeth). UBERON:0001091 (tooth).
- **Gastrointestinal/anorectal** — anorectal malformation in at least one case. UBERON:0000160 (intestine)/UBERON:0004908 (anus, approximate).
- **Skeletal system** — vertebrae (segmentation defects). UBERON:0001068 (vertebra).
- **Auditory system** — inner/middle ear (sensorineural hearing loss). UBERON:0001846 (ear).
- **Ocular system** — eyes (myopia; deep-set eyes, palpebral fissure anomalies as dysmorphic features). UBERON:0000970 (eye).

**Body systems involved:** Nervous, cardiovascular, renal/urinary, reproductive, skeletal, digestive (dental/anorectal), auditory, ophthalmologic — i.e., a genuinely multisystem developmental disorder, consistent with THOC6's broadly required role in mRNA processing across many developing tissues, though the brain (and specifically corticogenesis) is the best-mechanistically-characterized target organ.

**Tissue/cell level:**
- Cerebral cortex neuroepithelium/ventricular zone — pseudostratified neuroepithelium, neural rosettes (organoid correlate).
- Neural progenitor cells / radial glia (proliferation and apoptosis defects). CL:0000047 (neural stem cell) — more specific radial glial cell term CL:0000681 if desired.
- Migrating/differentiating cortical neurons (doublecortin+ population, reduced fraction). CL:0000540 (neuron) / DCX+ immature neuron.

**Subcellular level:**
- Nucleus — normal THOC6 localization site; site of TREX complex assembly and pre-mRNA splicing/processing. GO:0005634 (nucleus), GO:0016607 (nuclear speck, as a candidate TREX/splicing-associated compartment — verify).
- Cytoplasm — site of pathogenic THOC6 mislocalization for certain missense variants (loss of nuclear function).

**Lateralization:** No consistent lateral asymmetry pattern reported; renal agenesis has been unilateral in described cases but laterality (left vs right) is not consistently documented; overall dysmorphism/malformations are typically bilateral/symmetric (e.g., bilateral epicanthal folds, bilateral inguinal gonads in the genitourinary case).

---

## 8. Temporal Development

**Onset:**
- **Congenital/prenatal onset** for microcephaly, growth restriction, and structural anomalies (corpus callosum dysgenesis, cardiac/renal malformations) — detectable prenatally or at birth in several reported cases (see Ruaud et al. 2022, Birth Defects Research, "Biallelic THOC6 pathogenic variants: Prenatal phenotype and review of the literature," documenting prenatal ultrasound findings).
- **Neonatal/early infancy** recognition of low birth weight, feeding difficulties, and dysmorphic features.
- **Early childhood** manifestation of developmental delay and evolving intellectual disability as milestones are missed.

**Onset pattern:** Insidious/congenital rather than acute; anomalies are present from birth, with developmental delay becoming apparent over the first months to years of life.

**Progression:**
- Neurodevelopmental impairment: **stable to slowly evolving** — described as a static encephalopathy-type course rather than progressive neurodegeneration; no evidence of regression.
- Growth: postnatal growth failure/short stature persists but is not reported as progressively worsening.
- No formal disease-staging system exists (this is a static congenital malformation/neurodevelopmental syndrome, not a progressive degenerative disease).

**Disease course pattern:** Chronic, lifelong, non-progressive (congenital/static) — individuals require lifelong developmental, medical, and educational support but do not experience described periods of clinical regression, exacerbation-remission cycling, or episodic crises specific to the syndrome itself (beyond standard co-morbidity management, e.g., seizures in the rare individuals affected).

**Patterns / critical periods:** Early intervention (ages 0–3) is explicitly recommended in GeneReviews management guidance, reflecting the developmental-window importance of early therapy access, though this is a general early-childhood-intervention principle rather than a THOC6-specific critical period discovery.

**Longevity:** Survival into adulthood is documented; oldest reported affected individuals are in their **early 40s**. Whether life expectancy is shortened relative to the general population is currently **unknown** (small cohort size precludes formal survival analysis).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Extremely rare; estimated point prevalence **<1/1,000,000 worldwide** (per aggregated rare-disease database sourcing). As of GeneReviews (2020), approximately **19 affected individuals from 15 families** had been published; sporadic additional case reports (China, India, Turkey [Kiraz et al. 2022, AJMG], Palestine/2024–2025) have incrementally expanded this since, but the total published cohort remains well under 50 individuals.
- **Incidence:** Not formally calculated given rarity; no national/registry-level incidence figures exist.

**Inheritance pattern:** **Autosomal recessive.** Each sib of an affected individual has, at conception: 25% chance affected, 50% chance unaffected carrier, 25% chance unaffected non-carrier (standard AR Mendelian recurrence risk, per GeneReviews).

**Penetrance:** Appears to be complete/high for biallelic pathogenic variants (no clear unaffected biallelic carriers reported), though the very small cohort limits confidence in this assessment.

**Expressivity:** **Markedly variable** — phenotypic spectrum ranges from "classic" BBIS (microcephaly, ID, characteristic facies, cardiac/renal defects) to recently expanded presentations including ambiguous genitalia/disorders of sexual development and anorectal malformation, indicating substantial variable expressivity even among individuals with loss-of-function alleles.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed, though theoretically possible for any AR condition; genetic counseling for future pregnancies in a family with one affected child conventionally still assumes standard 25% recurrence risk given confirmed biallelic status in parents (both carriers).

**Founder effects:** Yes — the p.Gly46Arg (c.136G>A) variant is a well-documented **founder mutation in the Hutterite population** (Dariusleut and Lehrerleut Anabaptist communities), with carrier frequencies of 2–3%, substantially higher than expected for a private disease allele, reflecting the known founder-effect genetic architecture of this endogamous population.

**Consanguinity role:** Multiple non-Hutterite reported families are consanguineous (e.g., Palestinian, Indian sibling cases), consistent with the expected pattern for a rare AR disorder — biallelic variant co-occurrence is facilitated by shared ancestry.

**Carrier frequency:** Outside the Hutterite founder population, carrier frequency for any single THOC6 pathogenic variant is expected to be very low (private/rare variants); gnomAD-based estimates were not independently retrieved with precision in this session and should be checked directly in gnomAD for specific variants.

**Population Demographics:**
- **Affected populations:** Originally described in the Hutterite population (North American Anabaptist founder population); subsequently reported worldwide, including Chinese, Indian, Turkish, and Palestinian/Middle Eastern families — indicating no strict ethnic restriction outside the founder-effect enrichment in Hutterites.
- **Geographic distribution:** Global, reflecting panethnic distribution of private pathogenic variants, with the notable exception of Hutterite founder-variant enrichment in specific North American communities.
- **Sex ratio:** No skewed sex ratio reported (autosomal recessive, not X-linked); however, cryptorchidism, hypogonadism, and the reported ambiguous-genitalia case specifically highlight male genitourinary vulnerability, without implying differential overall prevalence by sex.
- **Age distribution:** Reported cases span from prenatal diagnosis/neonates through adults in their 40s.

---

## 10. Diagnostics

**Genetic Testing (primary diagnostic modality):**
- **First-tier:** Chromosomal microarray analysis (CMA) — to exclude large deletions/duplications and alternative diagnoses (though THOC6 disease itself is not typically caused by CNVs).
- **If CMA non-diagnostic:** Multigene intellectual-disability panel or exome sequencing (or genome sequencing) — sequence analysis of THOC6 detects essentially all reported pathogenic variant types (missense, nonsense, splice-site); GeneReviews states sequence analysis detects the pathogenic variant in essentially 100% of confirmed cases when the gene is adequately covered.
- **Population-specific approach:** In individuals of Hutterite ancestry, targeted testing for the founder variant c.136G>A (p.Gly46Arg) may be considered as a rapid first step before broader panel/exome testing.
- **Confirmatory:** Biallelic pathogenic/likely pathogenic THOC6 variants (homozygous or compound heterozygous) establish the molecular diagnosis.

**Clinical/Imaging Tests:**
- **Neuroimaging (brain MRI):** to assess corpus callosum dysgenesis, ventriculomegaly/hydrocephalus, and microcephaly-associated structural findings.
- **Echocardiography:** to detect septal defects and other structural cardiac anomalies.
- **Renal ultrasound:** to detect agenesis, ectopia, horseshoe kidney.
- **Dental evaluation:** for caries, malocclusion, supernumerary teeth.
- **Audiology:** for sensorineural hearing loss.
- **Ophthalmologic exam:** for myopia and strabismus/alignment issues.
- **Endocrine workup:** hypothalamic-pituitary-gonadal axis assessment (LH/FSH, testosterone/estradiol) in cases with genitourinary anomalies or delayed puberty, given documented hypergonadotropic hypogonadism.

**Prenatal diagnostics:** Prenatal ultrasound has detected findings consistent with BBIS (e.g., ventriculomegaly, growth restriction, structural anomalies) in at-risk pregnancies, as reviewed by Ruaud et al. 2022 (Birth Defects Research); prenatal molecular testing is available once familial pathogenic variants are known.

**Differential Diagnosis (per GeneReviews):**
- **Seckel syndrome** — overlapping microcephaly and dental malocclusion, distinguished by severe primordial growth restriction.
- **Rubinstein-Taybi syndrome** — overlapping microcephaly/dysmorphism, distinguished by characteristic broad thumbs/halluces.
- **Mowat-Wilson syndrome** — overlapping corpus callosum dysgenesis and genitourinary anomalies, distinguished by Hirschsprung disease and its own distinctive facial gestalt.
- Broader differential includes other syndromic autosomal recessive intellectual disability disorders with microcephaly and multi-organ involvement (e.g., other TREX/spliceosomopathy-related disorders such as THOC2-related ID).

**Screening:** No population-based newborn screening program exists (disease too rare, no biochemical screening marker); carrier screening could theoretically be offered in the Hutterite community given the known founder variant and elevated carrier frequency, though this was not explicitly documented as an implemented program in the sources reviewed.

**Omics-based diagnostics:** Not part of routine clinical diagnosis; RNA-seq-based splicing analysis (as used in the Nature Communications 2024 mechanistic study) is a research tool rather than an established clinical diagnostic, though it may have future utility for functional variant classification in ambiguous cases (VUS resolution).

---

## 11. Outcome/Prognosis

**Survival and Mortality:** No formal survival statistics or life-expectancy data exist given the small published cohort. The oldest reported affected individuals are documented into their **early 40s**, indicating survival well into adulthood is possible; whether overall life expectancy is shortened relative to the general population remains **unknown** and unquantified in the literature.

**Morbidity and Function:**
- Lifelong moderate-to-severe intellectual disability with associated functional impairment in adaptive skills, communication, and independence.
- Multi-organ morbidity depends on the specific malformation burden present (cardiac defect severity, renal function, hearing/vision impairment).
- No standardized quality-of-life instrument data (EQ-5D, SF-36, PROMIS) identified in the literature for this specific condition.

**Disease Course/Complications:**
- Recognized complications include: renal impairment (in those with structural renal anomalies, warranting annual renal function monitoring), dental complications (caries/malocclusion requiring ongoing dental care), hearing loss progression (warranting annual audiology), seizures (rare), and endocrine complications (hypergonadotropic hypogonadism potentially requiring hormone replacement in adolescence/adulthood).
- No described "recovery" — the neurodevelopmental component is a static, non-regressive congenital impairment; supportive/rehabilitative interventions aim to maximize functional potential rather than reverse an active degenerative process.

**Prognostic factors:** No validated prognostic biomarkers or clinical scoring system exists. Anecdotally, prognosis for cognitive/functional outcome likely correlates with the severity of the specific malformation burden (e.g., presence/severity of cardiac defects, degree of corpus callosum dysgenesis) and access to early intervention services, though this has not been formally studied.

---

## 12. Treatment

There is no disease-modifying or curative therapy for THOC6-related disease; management is entirely **supportive, symptomatic, and surveillance-based**, per the GeneReviews "Management" chapter (NBK560442, Table 5: Treatment of Manifestations).

**Developmental/Educational Support:**
- Early intervention programs (ages 0–3), developmental preschool, individualized education plans (IEPs), involvement of developmental pediatrics. MAXO candidate: MAXO:0000011 (physical therapy), and general early-intervention/education support terms (may not have a precise MAXO code; consider `MAXO:0000950` supportive care as a general anchor, or NCIT:C15747 Supportive Care).

**Surveillance/Monitoring (not treatment per se, but standard of care):**
- Annual/each-visit developmental, mobility, and behavioral assessment.
- Growth parameter and nutritional status monitoring.
- Annual (or each-visit, if renal anomaly present) renal function testing.
- Annual audiology evaluation.
- Ophthalmologic assessment.
- Dental evaluation.
- Assessment of secondary sexual characteristics in adolescent/adult females (and by extension males, given documented cryptorchidism/hypogonadism).

**Specific Interventions:**
- **Feeding therapy**, with possible **gastrostomy tube placement** for significant feeding/swallowing difficulties. MAXO candidate: feeding therapy under supportive care; gastrostomy under MAXO:0000004 (surgical procedure) or a more specific NCIT gastrostomy code.
- **Hearing aids** for documented sensorineural hearing loss. MAXO:0009030 (hearing aid usage).
- **Standard cardiac management** (per pediatric cardiology; surgical repair of septal defects as clinically indicated) — MAXO:0000004 (surgical procedure) / NCIT:C15329 (Surgical Procedure).
- **Standard urologic management**, including orchiopexy for cryptorchidism and reconstructive surgery for anorectal malformation/ambiguous genitalia as clinically indicated. MAXO:0000004 (surgical procedure), NCIT:C16186 (Orthopedic Surgical Procedure, not applicable here — better to use general surgical procedure or a specific urologic procedure NCIT term).
- **Standard orthopedic management** for skeletal anomalies (e.g., vertebral segmentation defects) as clinically indicated.
- **Anti-seizure medication** for the rare individuals with documented seizures. Treatment term: NCIT:C15986 (Pharmacotherapy) + `therapeutic_agent` per specific anticonvulsant used (not individually specified in the literature reviewed).
- **Hormone replacement therapy** for documented hypergonadotropic hypogonadism. Treatment term: NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (e.g., sex-hormone replacement, not individually specified).
- **Genetic counseling** for families, given 25% recurrence risk. MAXO:0000079 (genetic counseling).

**Experimental/Advanced Therapeutics:** None identified — no gene therapy, RNA-based therapy (ASO/siRNA), cell therapy, or targeted molecular therapy has been developed or is in clinical trials for THOC6-related disease specifically (searched clinicaltrials.gov context not separately verified in this session but no such trials were surfaced in any search). Given the mechanistic finding that disease arises from **splicing dysregulation** rather than bulk export failure, antisense-oligonucleotide splice-modulation approaches are a plausible future research direction (by analogy to other spliceosomopathies) but are **not** an established or trialed treatment as of this report.

**Treatment Outcomes:** No systematic treatment-response data exists; management is individualized symptomatic care per standard specialty guidelines for each organ-system manifestation, not disease-specific clinical trial evidence.

**Treatment Strategy:** Multidisciplinary care coordination (genetics, developmental pediatrics, cardiology, nephrology/urology, audiology, ophthalmology, dentistry, endocrinology) is the explicit GeneReviews-recommended strategy; no algorithmic/staged treatment pathway exists beyond this coordinated-surveillance model.

---

## 13. Prevention

**Primary Prevention:** Not applicable in the traditional sense (no modifiable risk factor); the only "primary prevention" avenue is **reproductive genetic counseling and carrier screening** in at-risk families/populations (notably the Hutterite community, given the known founder variant), enabling informed reproductive decision-making (e.g., IVF with preimplantation genetic testing, prenatal diagnosis, or informed conception planning).

**Secondary Prevention:** Prenatal diagnosis (via chorionic villus sampling/amniocentesis molecular testing once familial variants are known, or prenatal ultrasound surveillance for structural anomalies as reviewed by Ruaud et al. 2022) allows early identification, which does not prevent the condition but enables anticipatory perinatal/neonatal management planning.

**Tertiary Prevention:** The entire GeneReviews management program (surveillance schedule, early intervention, organ-specific monitoring) functions as tertiary prevention — aiming to minimize complications (renal deterioration, uncorrected hearing loss, dental disease, untreated hypogonadism) in individuals already diagnosed.

**Immunization:** No disease-specific vaccine strategy; standard immunization schedules apply.

**Genetic Counseling:** Central to prevention strategy — informing carrier parents of the 25% recurrence risk per pregnancy, offering prenatal/preimplantation testing options, and (in the Hutterite community specifically) potentially offering targeted carrier screening for the founder c.136G>A variant.

**Public Health/Behavioral/Prophylaxis:** Not applicable — this is not a condition amenable to public-health-level intervention, sanitation, vector control, or prophylactic medication strategies.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally-occurring THOC6-deficient disease has been reported in non-human species (no OMIA entry identified in searches conducted). The gene is broadly conserved (THO complex is conserved from yeast through mammals), but no spontaneous veterinary/companion-animal or wildlife disease phenotype has been documented.

**Comparative biology:** The THO/TREX complex mRNA-export/splicing-coupling function is evolutionarily conserved from *Saccharomyces cerevisiae* through humans, underscoring the fundamental cellular importance of this pathway; however, no comparative natural-disease models exist — all model data derives from **engineered** (not naturally occurring) animal models (see Section 15).

**Zoonotic potential/transmission:** Not applicable (non-infectious monogenic disorder).

---

## 15. Model Organisms

**Mouse (engineered, not natural disease):**
- ***Thoc6* loss-of-function mouse model** (described as *Thoc6^fs/fs* in the 2024 Nature Communications mechanistic study): biallelic loss is **embryonic lethal by E9.5–E11.5**. Embryos show developmental delay evident from E9.5, are smaller than littermates, and display **thinner neuroepithelium in the telencephalic vesicles**, with increased mitosis and increased apoptosis at E9.5. This is notably **more severe than the human phenotype** (humans survive with biallelic loss-of-function into adulthood), representing an important **human-model mismatch**: the mouse model demonstrates the embryonic requirement for Thoc6 in neuroepithelial development but does not recapitulate human survivability, implying species-specific compensatory mechanisms not yet identified. Splicing-defect signatures (weak splice sites, altered events) were broadly similar in direction to human findings but the mouse showed a "broader apoptotic response" than human iPSC-derived models (PMC10884030 / Nature Communications 2024, PMID:38388531).
- Available via MGI (Thoc6, MGI:2677480), which curates mouse genetic/phenotype data for this locus, though the specific engineered allele used in the corticogenesis study should be cross-referenced directly with the primary publication for exact allele nomenclature.

**Human iPSC-derived cortical organoid model:**
- Patient-derived and CRISPR-engineered iPSC lines carrying THOC6 pathogenic variants (nonsense W100* and missense E188K alleles referenced) differentiated into **dorsal forebrain-fated cortical organoids**, recapitulating aspects of in vivo ventricular-zone neurogenesis (neural rosette formation, NPC proliferation, and differentiation to cortical neuron fates). This model reproduced **reduced NPC proliferation, elevated apoptosis, delayed neuronal differentiation, thinner pseudostratified neuroepithelium, and smaller neural rosettes** — closely mirroring the human microcephaly phenotype, making this the most disease-relevant available model system (PMC10884030/PMC10503840, Nature Communications 2024 and its bioRxiv precursor).
- **Model characteristics:** Human iPSC-derived organoids showed **milder** apoptotic response than the mouse model, better recapitulating the survivable human phenotype — an important point favoring the organoid model's translational fidelity over the (embryonic lethal) mouse model for phenotype severity, though the organoid model cannot capture the full multi-organ (cardiac/renal/genitourinary) phenotype spectrum, which remains a **model limitation** (organoids model cortical/neural pathology only).

**Applications:** These models have been used specifically to establish the **TREX-tetramer-disruption / alternative-splicing** mechanism (rather than the originally hypothesized bulk mRNA nuclear export defect), and to identify downstream PI3K-AKT/mTOR, TGF-β, and WNT/lncRNA pathway dysregulation as mediators of the proliferation/apoptosis/differentiation phenotype in corticogenesis.

**Resources:** MGI (Thoc6 mouse gene record, MGI:2677480) for mouse genetic/allele data; no dedicated ZFIN/FlyBase/WormBase THOC6 disease model was identified in this search (searches for zebrafish THOC6-specific models did not return a dedicated published zebrafish thoc6 disease model, unlike the related THOC2 gene, for which a zebrafish model exists).

---

## Summary of Key Primary Citations

| Citation | Contribution |
|---|---|
| Beaulieu et al. 2013, *Orphanet J Rare Dis* 8:62, PMID:23621916 | Original description; Hutterite founder variant p.Gly46Arg |
| Kumar et al. 2016 / "Autosomal recessive mutations in THOC6..." PMID:27102954 | Syndrome delineation, forward/reverse phenotyping, expanded cohort |
| Mattioli et al. 2019, *Hum Mol Genet* 28(6):952-960, DOI:10.1093/hmg/ddy391 | Functional characterization of recurrent missense variants; mislocalization and THOC1/THOC5 interaction loss |
| Lemire, Innes, Boycott — GeneReviews NBK560442 (2020) | Comprehensive clinical synthesis, diagnostic/management guidelines, ~19 individuals/15 families |
| Ruaud et al. 2022, *Birth Defects Research*, DOI:10.1002/bdr2.2011 | Prenatal phenotype and literature review |
| Kiraz et al. 2022, *Am J Med Genet A*, DOI:10.1002/ajmg.a.62667 | Truncating variant, new phenotypic findings |
| PMC10503840 / bioRxiv 2022.09.06.506502 | Mechanisms of mRNA processing defects — precursor mechanistic study |
| Nature Communications 2024, PMID:38388531, PMC10884030 | Definitive TREX-tetramer/splicing mechanism; mouse and human organoid models |
| PMC12324036 (2024–2025 case report) | Novel splice variant (c.155+1G>T); first report of ambiguous genitalia/DSD phenotype |

**Note for dismech curation:** MONDO and Orphanet numeric identifiers for this entry should be independently confirmed against the live MONDO Ontology Lookup Service and Orphanet database before entry (not reliably retrievable via general web search in this session); OMIM #613680 (phenotype) and *615403 (gene) are confirmed. All PMIDs above should be run through `just fetch-reference` and snippet-verified per the standard dismech evidence SOP before being committed to a knowledge-base YAML entry — several claims here (e.g., "47% cardiac defects," "approximately half" dental anomalies) originate from aggregated GeneReviews narrative text rather than a single quotable primary-source sentence, so curators should locate the specific primary cohort paper (likely Kumar et al. 2016 or the GeneReviews-cited case series) for an exact quotable snippet rather than citing the GeneReviews synthesis itself as the evidence source where a primary paper exists.