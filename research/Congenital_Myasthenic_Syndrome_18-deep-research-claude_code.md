---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T23:47:51.045751'
end_time: '2026-07-31T23:53:45.444045'
duration_seconds: 354.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Myasthenic Syndrome 18
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
  web_search_requests: 21
  num_turns: 31
  total_cost_usd: 2.2080154999999992
  session_id: aed4af82-a86a-5a40-97ca-88599f828e94
  stop_reason: end_turn
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myasthenic Syndrome 18
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myasthenic Syndrome 18** covering all of the
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

I now have sufficient information to compile the comprehensive research report.

---

# Congenital Myasthenic Syndrome 18 (CMS18) — Comprehensive Research Report

## Important Nomenclature Note (Read First)

Searches for "Congenital Myasthenic Syndrome 18/CMS18" frequently surface material on **COL13A1**, but that gene causes a *different, higher-numbered* entity — **Congenital Myasthenic Syndrome 19 (CMS19, OMIM #616720)** — not CMS18. This is a common confusion because the numbering is easy to mistransc­ribe and because COL13A1-CMS dominates recent CMS literature volume.

**CMS18 is the SNAP25-related disorder, OMIM #616330**, originally named "Myasthenic syndrome, congenital, 18, with intellectual disability and ataxia" and gene symbol **SNAP25** (synaptosome-associated protein 25, 20p12.2). OMIM's clinical synopsis for this entry has since been folded into/relabeled **"Developmental and Epileptic Encephalopathy 117" (DEE117)** as the phenotypic spectrum of SNAP25 heterozygous variants was found to extend beyond myasthenia into a broader neurodevelopmental/epileptic encephalopathy continuum. MedGen (Concept ID **C4225364**) still lists "Congenital myasthenic syndrome 18" as a synonym/legacy label for the same OMIM #616330 entity, and the disease is also cataloged under HGNC gene aliases RIC-4, SEC9, SUP, SNAP for the SNAP25 protein. This report treats **CMS18 = SNAP25-related presynaptic CMS/DEE (OMIM #616330)** throughout, and flags where source material blends into the wider DEE117 phenotype.

---

## 1. Disease Information

**Overview:** CMS18 is a rare, autosomal-dominant **presynaptic** congenital myasthenic syndrome caused by heterozygous (typically de novo) missense or truncating variants in **SNAP25**, a core SNARE-complex protein required for calcium-triggered synaptic vesicle exocytosis. Unlike the majority of CMS subtypes — which are autosomal recessive and confined to the neuromuscular junction (NMJ) — CMS18 is dominant and produces a **combined phenotype of fatigable myasthenic weakness plus CNS dysfunction** (cortical hyperexcitability/epilepsy, cerebellar ataxia, and intellectual disability), reflecting SNAP25's essential role in exocytosis at both the NMJ and central synapses.

**Key identifiers:**
- **OMIM #616330** — "Myasthenic syndrome, congenital, 18, with intellectual disability and ataxia" / "Developmental and epileptic encephalopathy 117; DEE117"
- **OMIM gene entry *600322** — SNAP25 (Synaptosomal-Associated Protein, 25-KD)
- **MedGen:** C4225364 ("Congenital myasthenic syndrome 18")
- **HGNC:** SNAP25, HGNC:11132; cytogenetic location 20p12.2
- **NCBI Gene ID:** 6616
- **Gene aliases:** SNAP-25, RIC-4, RIC4, SEC9, SUP
- **Orphanet:** listed under the broader "Congenital myasthenic syndrome" grouping (ORPHA:590); a dedicated presynaptic-CMS/SNAP25 stub is cross-referenced under the mechanistic Orphanet grouping for defective synaptic vesicle cycling
- Frequency in the CMS spectrum: **<1% of all genetically solved CMS cases** — among the rarest presynaptic CMS subtypes (GeneReviews *Congenital Myasthenic Syndromes Overview*, NBK1168)

**Synonyms:** CMS18; SNAP25-related congenital myasthenic syndrome; Myasthenic syndrome, congenital 18, with intellectual disability and ataxia; Developmental and epileptic encephalopathy-117 (DEE117); SNAP25 encephalopathy

**Data provenance:** Knowledge is derived almost entirely from **individual published case reports/series** (fewer than 10-15 molecularly confirmed patients described to date across the founding 2014 report, subsequent DEE-focused cohorts, and isolated case reports) plus mechanistic biophysical/cell-biology studies of the specific mutant alleles — not from large aggregated disease registries. This is characteristic of an ultra-rare, recently delineated Mendelian disorder.

---

## 2. Etiology

**Primary cause:** Heterozygous, almost always **de novo**, missense or nonsense variants in **SNAP25**, encoding a t-SNARE protein essential for synaptic vesicle docking, priming, and calcium-triggered fusion at both the presynaptic motor nerve terminal and central synapses.

**Genetic risk factors / mechanism of pathogenicity:**
- **Dominant-negative mechanism** is well established for the founding mutation (I67N): mutant SNAP25B protein incorporates into SNARE complexes and destabilizes/poisons them even in the presence of wild-type protein, rather than simply reducing gene dosage (haploinsufficiency).
- SNAP25 is under strong **evolutionary and population constraint** consistent with the dominant, de novo disease mechanism — gnomAD-type constraint metrics for genes causing severe dominant neurodevelopmental disease from de novo variants typically show high missense and loss-of-function intolerance (elevated missense Z-score / pLI), consistent with SNAP25 being depleted of both truncating and disruptive missense variation in the general population (per general gnomAD constraint methodology; Wilfert et al., gene-constraint/genotype-phenotype correlation studies, PMC10340126).
- No recessive/biallelic SNAP25 CMS has been reported — inheritance is monogenic autosomal dominant with each reported case arising as a **de novo** event in an otherwise unaffected family (no vertical transmission reported to date, consistent with the severity of the phenotype limiting reproductive fitness).

**Environmental/other risk factors:** None identified — this is a monogenic disorder with no known environmental, infectious, or lifestyle contribution to disease occurrence. No consanguinity signal (dominant de novo mechanism).

**Protective factors:** None specifically described. No modifier alleles have been reported; phenotypic variability across the small number of known cases appears driven by **variant-specific biophysical mechanism** (see Section 6) rather than by identified genetic modifiers.

**Gene-environment interactions:** Not applicable/not described — no evidence of environmental triggers modifying expressivity has been reported in the literature.

---

## 3. Phenotypes

CMS18/SNAP25-CMS phenotypes span **neuromuscular (myasthenic)**, **central neurological (epileptic encephalopathy, ataxia)**, and **neurodevelopmental** domains, distinguishing it from isolated CMS subtypes.

### Core neuromuscular (myasthenic) phenotypes
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Fatigable/fluctuating muscle weakness | HP:0003473 (Fatigable weakness) | Hallmark CMS feature; partial improvement with neostigmine reported in the index case |
| Ptosis (fluctuating eyelid) | HP:0000508 | Present in the founding I67N case |
| Neonatal respiratory distress / respiratory failure requiring intubation | HP:0002878 / HP:0004879 | Life-threatening in the severe nonsense (Gln177Ter) neonatal case; cause of death in that patient |
| Hypotonia | HP:0001252 | Present across reported cases, often neonatal |
| Feeding difficulty | HP:0011968 | Reported in severe neonatal-onset cases |
| Arthrogryposis / congenital joint contractures | HP:0002804 | Documented in the neonatal nonsense-variant case (multiple upper-extremity contractures, clubfeet) — reflects reduced fetal movement from impaired NMJ transmission in utero |
| Decreased fetal movement | HP:0001558 | Consistent with arthrogrypotic presentation |
| Knee flexion contractures | HP:0006380 | Present in the index (I67N) patient, worsening gait |

### Central/CNS phenotypes
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Seizures / epilepsy (generalized, polyspike-wave) | HP:0002133 / HP:0011097 | Founding patient: onset ~age 5, valproate partially/ineffective initially; later cohorts (V48F, D166Y, I67N-DEE presentations) show early-onset seizures as a presenting/dominant feature |
| Cortical hyperexcitability | HP:0031547 (Abnormal cortical excitability, if modeled) | Explicit descriptor used by the original 2014 report title |
| Cerebellar ataxia | HP:0001251 | Present in essentially all reported cases; ataxic dysarthria and paretic/ataxic gait |
| Dysarthria | HP:0001260 | Documented in the index patient |
| Intellectual disability / developmental delay | HP:0001249 (ID) / HP:0001263 (Global developmental delay) | Ranges from mild-moderate (V48F, D166Y cases) to severe with poor/absent speech; index patient had a developmental level of 3-4 years at chronological age 11 |
| Echolalia / speech abnormality | HP:0010529 (echolalia, if applicable) / HP:0002167 | Present in the index patient |
| Movement abnormalities: spasticity, dystonia | HP:0001257 / HP:0001332 | Variable, per OMIM DEE117 synopsis |
| Areflexia | HP:0001284 | Listed among neurological manifestations |
| Gait disturbance | HP:0001288 | Overlaps with ataxia |
| Brain atrophy / cortical atrophy | HP:0012443 / mild diffuse cortical atrophy on MRI | Seen on MRI in the D166Y adult case |
| Delayed myelination | HP:0012448 | Seen on MRI in the V48F case |
| Ocular anomalies | HP:0000478 (nonspecific) | Listed as a variable DEE117 feature |
| Mild dysmorphic features | — | Listed as variable in the DEE117/CMS18 synopsis; the neonatal nonsense case additionally had micrognathia, cleft palate, diffuse skin thickening |
| Clubfeet | HP:0001762 | Variable feature; present in the neonatal severe case |

### Phenotype characteristics
- **Age of onset:** Ranges from **prenatal/neonatal** (severe cases — decreased fetal movement, arthrogryposis, birth respiratory failure) to **infancy/early childhood** (typical presenting age for the myasthenia-ataxia-ID triad) to later childhood-onset seizures (index patient, seizure onset ~age 5).
- **Severity:** Highly variable — from a **lethal neonatal presentation** (the Gln177Ter nonsense-variant patient died on day 6 of life from respiratory failure) to a **moderate, largely stable phenotype** persisting into the third decade (D166Y patient, 23 years old at report).
- **Progression:** Neurological features (ataxia, ID) are generally **static/developmental** rather than progressive once established, though epilepsy course is variable (the index patient's seizures were described across a multi-year follow-up with variable anticonvulsant response).
- **Frequency among affected individuals:** Given the very small number of published cases (literature currently comprises roughly the I67N index case, the Q177Ter neonatal case, and the V48F/D166Y encephalopathy-predominant cases characterized functionally in the 2024 eLife paper, plus additional unpublished/registry cases alluded to in reviews), formal phenotype-frequency percentages analogous to HPO annotation frequencies are **not established** — most features are reported as present/absent per-case rather than as population frequencies.

**Quality-of-life impact:** Not formally measured with QOL instruments (no EQ-5D/SF-36/PROMIS data identified); qualitatively, the combination of motor weakness, ataxia, and intellectual disability in surviving patients produces substantial functional impairment (non-ambulation or impaired gait, poor/absent speech, dependence for activities of daily living reported in the more severely affected cases per the DEE117 OMIM synopsis).

---

## 4. Genetic/Molecular Information

**Causal gene:** **SNAP25** (Synaptosomal-Associated Protein, 25kDa), OMIM *600322, chromosome 20p12.2, HGNC:11132, NCBI Gene ID 6616. Two alternatively spliced isoforms exist — **SNAP25a** and **SNAP25b** — differing in a short internal segment; SNAP25b is the predominant adult neuronal isoform and is the isoform in which the founding I67N mutation was characterized.

**Reported pathogenic variants (heterozygous, all reported as de novo):**

| Variant (protein) | Variant (cDNA) | Domain/location | Classification | Isoform affected | Reporting study |
|---|---|---|---|---|---|
| p.Ile67Asn (I67N) | c.200T>A | Core SNARE four-helix bundle (C-terminal SNARE motif region) | Pathogenic; dominant-negative | SNAP25b | Shen, Selcen, Brengman, Engel 2014, *Neurology* 83:2247-2255, PMID: 25381298 |
| p.Gln177Ter (Q177Ter) | c.529C>T | C-terminal truncation | Pathogenic (nonsense/truncating), de novo | — | Cold Spring Harb Mol Case Stud 2022;8:a006242 (rapid genome sequencing case), PMID reported in PMC9808558 |
| p.Val48Phe (V48F) | — | N-terminal t-SNARE coiled-coil domain / synaptotagmin-1 (Syt1)-binding interface | Pathogenic; "neomorph" (combined loss- and gain-of-function) | Both SNAP25a and SNAP25b | Rohena et al. 2013 (originally reported as an epileptic encephalopathy variant); mechanistically characterized in Wu et al./eLife 2024, PMID 38411501 |
| p.Asp166Tyr (D166Y) | — | Synaptotagmin-1 (Syt1)-binding interface | Pathogenic; "neomorph" (combined loss- and gain-of-function), stronger effect than V48F | — | Hamdan et al. 2017; mechanistically characterized in eLife 2024, PMID 38411501 |
| p.Gly86Arg (G86Arg) | c.256G>A | — | Reported in ClinVar under "Congenital myasthenic syndrome 18" (RCV000689120) | — | ClinVar submission |

**Variant type/class:** Missense (I67N, V48F, D166Y, G86R) and nonsense/truncating (Q177Ter) — no large structural rearrangements or splice-site variants reported for CMS18/SNAP25-CMS to date.

**Allele frequency in population databases:** Given the extreme rarity and de novo, severe-phenotype dominant mechanism, these specific pathogenic variants are **absent or present only as extremely rare singletons** in gnomAD/population databases — consistent with strong negative selection against SNAP25 coding variation in the general population (SNAP25 shows population-level constraint against both loss-of-function and disruptive missense variation, per gnomAD gene-constraint conventions).

**Somatic vs. germline origin:** All molecularly reported cases are **germline, de novo, heterozygous** variants (not somatic mosaicism in the parents; though *within* the patient, the index I67N case's electrophysiology showed non-normally distributed quantal-content values that the authors interpreted as possibly reflecting somatic mosaicism at the neuromuscular junction level — an intriguing but not independently confirmed observation).

**Functional consequences by variant (loss-of-function vs. gain-of-function vs. dominant-negative):**
- **I67N** — classic **dominant-negative**: destabilizes the SNARE four-helix bundle via loss of a critical hydrophobic packing interaction (replacing hydrophobic Ile [hydropathy +4.5] with hydrophilic Asn [-3.5]); in reconstituted membrane-fusion assays, mutant SNAP25B blocked calcium-triggered v-SNARE/t-SNARE liposome fusion, and cotransfection of mutant with wild-type in chromaffin cells reduced catecholamine release to 11% of wild-type levels, confirming a poisoning/dominant-negative effect on the assembled complex rather than simple haploinsufficiency.
- **V48F and D166Y** — mechanistically distinct **"neomorphic" mutations** combining loss-of-function (impaired synaptotagmin-1 interaction, reduced Ca²⁺-stimulated fusion, reduced readily-releasable-pool priming) with gain-of-function features (paradoxically enhanced SNARE-partner binding, increased spontaneous release, lowered energy barrier for fusion, and evasion of complexin-mediated fusion clamping) — as characterized in detailed reconstituted-fusion biophysics (eLife 2024, PMID 38411501).
- **Q177Ter** — C-terminal truncation predicted to disrupt the SNARE motif and membrane-proximal region required for complex assembly/stability; associated with the most severe reported phenotype (neonatal lethality).

**Modifier genes:** None identified/reported.

**Epigenetic information:** Not reported for this disorder.

**Chromosomal abnormalities:** Not applicable — CMS18 arises from single-nucleotide/small coding variants in SNAP25, not from copy-number or structural chromosomal changes. (Note: SNAP25 also lies within a chromosomal region relevant to unrelated 20p microdeletion contexts, but that is mechanistically distinct from the point-mutation CMS18/DEE117 disease model and outside this report's scope.)

**Suggested ontology bindings:** Gene — `hgnc:11132` (SNAP25); Molecular function — GO:0005484 (SNARE binding), GO:0061789 (SNARE complex disassembly, if relevant to disassembly-cycle mechanism), GO:0016081 (synaptic vesicle docking); relevant GO Cellular Component — GO:0031201 (SNARE complex), GO:0042734 (presynaptic membrane), GO:0008021 (synaptic vesicle).

---

## 5. Environmental Information

Not applicable — no environmental toxins, occupational exposures, radiation, pollution, lifestyle, or infectious triggers are implicated in CMS18 causation. This is a purely genetic (de novo monogenic) disorder. No gene-environment interaction data exist.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger (upstream):** Heterozygous de novo SNAP25 variant produces a structurally altered t-SNARE protein (I67N: destabilized coiled-coil; V48F/D166Y: altered synaptotagmin-1-binding interface; Q177Ter: truncated protein).
2. **SNARE complex assembly/stability defect:** Mutant SNAP25 protein incorporates into the ternary SNARE complex (with syntaxin-1 and VAMP2/synaptobrevin-2) alongside wild-type SNAP25, producing either (a) a destabilized, dominant-negative complex with an increased energy barrier to membrane fusion (I67N), or (b) an aberrantly hyperstable/miswired complex with disrupted synaptotagmin-1 coupling and dysregulated calcium sensing (V48F, D166Y).
3. **Impaired calcium-triggered synaptic vesicle exocytosis:** Across all characterized variants, calcium-stimulated, synchronous vesicle fusion is compromised — manifesting as reduced evoked quantal release (reduced miniature endplate potential frequency and quantal content at the NMJ) and, in reconstituted central-synapse systems, altered readily-releasable-pool size, altered spontaneous (miniature) release, and altered fusion kinetics.
4. **Presynaptic neuromuscular transmission failure:** At the motor endplate, this produces the electrophysiological signature of a **presynaptic CMS** — reduced quantal release with normal postsynaptic acetylcholine receptor density/distribution and normal synaptic vesicle docking morphology (docked vesicles are present but fail to fuse efficiently) — yielding fatigable muscle weakness, ptosis, and (in severe cases) neonatal respiratory failure and arthrogryposis from reduced fetal muscle activity.
5. **Central synaptic transmission failure:** The same SNARE-complex defect operating in CNS neurons (cortical, cerebellar) produces network-level dysfunction: cortical hyperexcitability/epileptogenesis (paradoxically, impaired inhibitory/excitatory balance from dysregulated vesicle release can manifest as seizures), cerebellar Purkinje/granule-cell circuit dysfunction (ataxia), and impaired synaptic plasticity/circuit maturation underlying intellectual disability and developmental delay.
6. **Downstream systemic consequences:** Chronic impaired neuromuscular and CNS synaptic function drives the multisystem phenotype — feeding difficulty, hypotonia, contractures/arthrogryposis (reduced in utero movement), and the neurodevelopmental/epilepsy phenotype.

**Which mechanisms are upstream vs. downstream:** The single unifying upstream lesion is **impaired SNARE-complex-mediated, calcium-triggered vesicle fusion**; everything else (myasthenic weakness, ataxia, seizures, ID) is a downstream tissue-specific consequence of this one presynaptic mechanism operating in different neuronal populations (motor nerve terminal vs. cortex vs. cerebellum).

**Cell types involved (CL terms):**
- Motor neuron / neuromuscular junction presynaptic terminal — CL:0000100 (motor neuron)
- Cortical excitatory/inhibitory neurons — CL:0000598 (pyramidal neuron), CL:0000617 (GABAergic interneuron, if inhibitory dysfunction contributes to hyperexcitability)
- Cerebellar Purkinje cells — CL:0000121 (Purkinje cell)
- Skeletal muscle fiber (postsynaptic target, secondarily affected) — CL:0000188/CL:0008002

**Biological processes (GO terms):**
- GO:0016079 — synaptic vesicle exocytosis
- GO:0031629 — synaptic vesicle fusion to presynaptic active zone membrane
- GO:0007269 — neurotransmitter secretion
- GO:0099525 — presynaptic dense core vesicle exocytosis (relevant given SNAP25's dual role in synaptic and dense-core-vesicle release)
- GO:0060079 — excitatory postsynaptic potential (downstream circuit effect)

**Protein dysfunction:** Predominantly **dominant-negative destabilization** (I67N) or **neomorphic gain/loss-of-function combination** (V48F, D166Y) rather than simple loss-of-function/haploinsufficiency — an important mechanistic nuance versus most recessive LOF-driven CMS genes.

**Biochemical abnormalities:** Core defect is in the **SNARE (soluble NSF-attachment protein receptor) fusion machinery** — SNAP25 is the t-SNARE partner of syntaxin-1 (plasma membrane) and VAMP2/synaptobrevin (vesicle membrane); disease variants disrupt either the coiled-coil zippering of the four-helix SNARE bundle or the calcium-sensor (synaptotagmin-1) coupling interface required to convert calcium influx into fast, synchronous fusion.

**Molecular/omics profiling:** No transcriptomic, proteomic, or metabolomic disease-tissue profiling has been published for human CMS18 patients (tissue inaccessibility in a rare pediatric neuromuscular/CNS disorder); mechanistic insight instead comes from **reconstituted biochemical fusion assays** (liposome fusion, single-vesicle content-mixing assays), **chromaffin-cell exocytosis assays**, and **electrophysiological recordings from patient intercostal-muscle endplates** (microelectrode studies).

**Advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR screen data specific to human CMS18 tissue have been published. Functional dissection has instead relied on classic single-molecule/reconstitution biophysics (eLife 2024 study) and expression-system electrophysiology (PC12/chromaffin cells, cultured neurons).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Peripheral nervous system — the neuromuscular junction (motor nerve terminal) and skeletal muscle (secondarily, via impaired innervation); central nervous system — cerebral cortex (epileptogenesis), cerebellum (ataxia).
- **Secondary:** Respiratory system (via bulbar/respiratory muscle weakness — the most life-threatening secondary organ involvement, causing neonatal respiratory failure in the severe case); musculoskeletal system (contractures/arthrogryposis, clubfeet from reduced fetal movement); orofacial structures (cleft palate, micrognathia reported in the severe neonatal case, likely also secondary to reduced fetal orofacial muscle activity/deformation).
- **Body systems involved:** Neuromuscular, nervous (central and peripheral), musculoskeletal, and (secondarily, in severe neonatal cases) respiratory.

**Tissue and cell level:**
- Presynaptic nerve terminal (motor and central neurons) — UBERON:0000102 (motor neuron / axon terminal, general presynaptic terminal concept)
- Skeletal muscle motor endplate — UBERON:0031594 (neuromuscular junction) if using an anatomical descriptor
- Cerebral cortex — UBERON:0000956
- Cerebellum — UBERON:0002037
- Cell populations: motor neurons, cortical pyramidal/interneurons, cerebellar Purkinje and granule cells (see CL terms above)

**Subcellular level:**
- Synaptic vesicle membrane — GO:0008021 (synaptic vesicle)
- Presynaptic plasma membrane — GO:0042734
- SNARE complex assembly — GO:0031201 (SNARE complex)

**Localization:**
- Site of primary pathology: **presynaptic nerve terminal** at both the neuromuscular junction and central synapses (UBERON:0031594 NMJ; cortex/cerebellum for CNS involvement).
- **Lateralization:** Not applicable/no lateralized pattern reported — disease is a diffuse/generalized presynaptic transmission defect (bilateral ptosis, generalized weakness, diffuse cortical/cerebellar dysfunction), not a focal or unilateral process.

---

## 8. Temporal Development

**Onset:**
- **Typical age of onset:** Congenital/neonatal to early childhood. The most severe reported case (Q177Ter) presented **prenatally** (polyhydramnios, decreased fetal movement) with birth at 35 weeks and immediate respiratory failure. The founding index case (I67N) had an earlier developmental/myasthenic presentation with seizure onset around age 5. The V48F and D166Y cases were characterized as adolescent/young-adult at time of report (15 and 23 years old respectively) with seizure onset in infancy (5 months) for V48F.
- **Onset pattern:** Predominantly **congenital/insidious** for the myasthenic/hypotonic component (present from birth), with **acute-onset** possible for the most severe respiratory presentations, and a more **subacute/progressive** unmasking of the epileptic-encephalopathy component over the first years of life.

**Progression:**
- **Disease stages:** Not formally staged (no consensus staging system exists for this ultra-rare disorder).
- **Progression rate/course pattern:** Variable and **not uniformly progressive** — the neurodevelopmental/ataxic component appears largely static once established (a developmental disorder rather than a neurodegenerative one), while epilepsy course fluctuates (index patient's seizures were treatment-resistant for a period, then apparently better controlled). The disease course is best described as **"static-to-fluctuating"** rather than classically progressive or classically episodic.
- **Disease duration:** Chronic, lifelong in survivors; the most severely affected neonatal patient died on day 6 of life (respiratory failure) — indicating the phenotype spans from neonatal-lethal to a chronic, non-degenerative lifelong neurodevelopmental/myasthenic disorder.

**Patterns:**
- **Remission:** No spontaneous remission reported; myasthenic component may show **partial pharmacologic improvement** (index case: neostigmine partially reduced EMG decrement).
- **Critical periods:** The **perinatal/neonatal period** represents the highest-risk critical window (respiratory failure risk in severe truncating variants); early childhood is the critical window for seizure onset and developmental-trajectory determination.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence/incidence:** Not formally estimated — CMS18/SNAP25-CMS is one of the rarest genetically defined CMS subtypes, representing **<1% of all molecularly solved CMS** cases (GeneReviews CMS Overview, NBK1168). Given that CMS overall has an estimated prevalence on the order of 1-9 per 1,000,000 (typical Orphanet-class range for the broader CMS group), SNAP25-CMS/CMS18 itself is almost certainly in the **ultra-rare (<1 in 1,000,000)** Orphanet prevalence band, with the world literature comprising a handful of published, molecularly confirmed cases.

**Inheritance pattern:**
- **Autosomal dominant (AD)** — a notable exception among CMS genes, most of which are autosomal recessive. All reported cases have arisen as **de novo** heterozygous variants (suggested HP inheritance term: HP:0000006 Autosomal dominant, or more specifically HP:0025352 De novo — should be modeled with an `Inheritance` block bound to the relevant HPO mode-of-inheritance term, `HP:0000006`, with `description` noting the de novo pattern per case).

**Penetrance:** Presumed **complete/high** given that every reported carrier of a pathogenic SNAP25 variant manifests disease (consistent with the severe, dominant-negative/gain-of-function mechanism), though the very small case number precludes a formal penetrance estimate.

**Expressivity:** **Highly variable** — ranging from a mild-to-moderate ataxia/ID/epilepsy phenotype with long-term survival (D166Y, V48F, I67N cases) to a lethal neonatal arthrogrypotic/respiratory-failure phenotype (Q177Ter). This variability appears to track with the **specific biophysical mechanism of each variant** (dominant-negative destabilization vs. neomorphic gain/loss-of-function vs. truncation) rather than with any identified modifier.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not formally documented in unaffected parents of reported cases (all cases described as apparently de novo with unaffected, non-mosaic-tested or presumed non-carrier parents); the index I67N patient's own quantal-release data showed a statistical pattern the authors speculated might reflect **somatic mosaicism within the patient** at the neuromuscular junction, though this remains an unconfirmed hypothesis specific to that case rather than a general germline-mosaicism finding.

**Founder effects:** None reported — each case has a distinct, apparently independently arising variant.

**Consanguinity:** Not relevant — dominant de novo mechanism, consistent with reported cases arising in non-consanguineous families (explicitly noted for the neonatal Q177Ter case).

**Carrier frequency:** Not applicable (not a recessive carrier-screening-relevant disorder; each case is an independent de novo dominant event, not inherited from a carrier parent).

**Population demographics:** No specific ethnic, geographic, or sex-ratio pattern has been established given the very small number of published cases (a mix of male and female patients reported: the index case was female, the neonatal lethal case was male). No geographic clustering reported.

---

## 10. Diagnostics

**Clinical tests:**
- **Electrophysiology (key diagnostic modality for presynaptic CMS):** Repetitive nerve stimulation showing a decremental response; **in vitro microelectrode studies** of intercostal-muscle endplates in the index case demonstrated reduced miniature endplate potential (MEPP) frequency (31% of normal) and reduced quantal release probability (63% of normal) with preserved acetylcholine receptor density — the classic **presynaptic quantal-release-defect signature** distinguishing this CMS category from postsynaptic (e.g., AChR-deficiency) or synaptic-basal-lamina (e.g., COL13A1, COLQ) CMS subtypes.
- **EMG:** Partial reduction of decrement with neostigmine reported in the index case, consistent with a component of neuromuscular junction dysfunction responsive to acetylcholinesterase inhibition, though the primary defect (presynaptic release) is not fully correctable by AChE inhibition.
- **EEG:** Generalized polyspike-wave discharges documented in the index/seizure-affected cases; essential for characterizing the epileptic-encephalopathy component.
- **Brain MRI:** Findings variably include mild diffuse cortical atrophy (D166Y case) and delayed myelination (V48F case); MRI can also be normal.
- **Muscle biopsy/ultrastructure:** Electron microscopy in the index case showed abundant synaptic vesicles normally docked at active zones (i.e., a **functional fusion defect, not a structural/vesicle-number defect** — vesicles dock but fail to fuse efficiently), an important diagnostic/mechanistic distinguishing feature.

**Genetic testing:**
- **Recommended approach:** Given the CMS phenotype-gene heterogeneity (>30 genes implicated in CMS) plus the possibility of a broader DEE, **CMS gene-panel or exome/genome sequencing** is the recommended diagnostic strategy rather than single-gene testing, given SNAP25's atypical (dominant, de novo, CNS-plus-NMJ) presentation that might not immediately suggest "classic CMS" to a clinician expecting recessive, NMJ-limited disease.
- **Rapid genome sequencing (rWGS):** Explicitly demonstrated as diagnostically decisive in the critically ill neonatal case — a 7-day-turnaround rWGS identified the de novo SNAP25 c.529C>T (p.Gln177Ter) variant, illustrating the clinical utility of rapid sequencing in acutely ill neonates with an undifferentiated arthrogryposis/respiratory-failure presentation.
- **Single-gene testing:** Available via clinical laboratories (e.g., NIH GTR lists dedicated SNAP25 sequence-analysis clinical tests for "Myasthenic syndrome, congenital, 18" — GTR test ID 581717) once the phenotype is suspected.
- **Chromosomal microarray/karyotype/FISH:** Not primarily indicated (disease is due to point mutation, not structural rearrangement), though may be part of a standard undiagnosed-arthrogryposis or DEE diagnostic workup to exclude other etiologies.
- **Variant classification:** Reported variants are classified pathogenic per functional/segregation evidence (de novo occurrence, absence from population databases, concordant electrophysiological/biochemical functional data) — consistent with ACMG/AMP criteria PS2 (de novo), PM2 (absent from population databases), PS3 (functional studies), and (for I67N) PM1/PM5-type structural-domain evidence.

**Omics-based diagnostics:** Not part of routine diagnostic workup; RNA-seq, proteomics, metabolomics not used clinically for this disorder.

**Clinical criteria:** No formal consensus diagnostic-criteria document specific to SNAP25-CMS exists; diagnosis rests on the combination of (1) fatigable myasthenic weakness with presynaptic electrophysiology, (2) epilepsy/cortical hyperexcitability, (3) ataxia, and (4) intellectual disability/developmental delay, confirmed by molecular identification of a heterozygous de novo pathogenic SNAP25 variant.

**Differential diagnosis:** Other presynaptic CMS genes (CHAT, SYT2, MUNC13-1/UNC13A, SLC5A7/choline transporter, VAMP1); other genetic causes of developmental and epileptic encephalopathy with ataxia (e.g., STXBP1-DEE, given STXBP1's mechanistic overlap as another SNARE-machinery regulator); other arthrogryposis-associated neuromuscular disorders in the severe neonatal presentation.

**Screening:** No population newborn-screening or carrier-screening program exists (ultra-rare, de novo dominant disorder not amenable to carrier screening); prenatal diagnosis could theoretically be offered in a family with a previously affected child (recurrence risk driven primarily by the low background rate of germline mosaicism rather than standard Mendelian recurrence risk, though this has not been specifically quantified for SNAP25).

---

## 11. Outcome/Prognosis

**Survival and mortality:** Highly variant-dependent. The **Q177Ter truncating variant** was associated with **neonatal death on day 6 of life** from respiratory failure following compassionate extubation. In contrast, patients with the I67N, V48F, and D166Y missense variants have survived into **the second and third decades** of life (ages 11, 15, and 23 years reported, respectively), indicating that **survival is not uniformly poor** and depends heavily on the specific variant's severity and the degree of respiratory/bulbar involvement.

**Morbidity and function:** Surviving patients experience chronic, non-fatal but substantial morbidity — non-fatigable ptosis in adulthood, ataxic gait (sometimes limited by contractures), dysarthria, and intellectual disability ranging from mild to severe with poor or absent speech in more affected individuals. No formal disability-outcome or QOL instrument data available.

**Disease course/complications:** Chronic contractures (knee flexion), recurrent/treatment-resistant seizures in a subset, and (in the index case) gradual improvement of muscle strength over time is notably **not** the typical CMS pattern reported for SNAP25 — data here are limited to case-level narrative rather than systematic follow-up. (Contrast: the *COL13A1/CMS19* literature, not CMS18, specifically documents strength improvement into adulthood — care should be taken not to conflate the two entities' natural histories.)

**Prognostic factors:** The clearest identified prognostic determinant in the literature is **variant-specific mechanism/severity** — truncating/null-like variants (Q177Ter) associated with the most severe, neonatal-lethal phenotype; missense dominant-negative or neomorphic variants (I67N, V48F, D166Y) associated with survival and a chronic but non-degenerative course. No molecular biomarker-based prognostic model exists.

---

## 12. Treatment

**Pharmacotherapy:**
- **Acetylcholinesterase inhibitors (e.g., pyridostigmine, neostigmine):** Standard first-line CMS therapy; in the index (I67N) patient, **neostigmine partially reduced the EMG decremental response**, indicating some benefit, though — as is typical for presynaptic CMS where the primary defect is release probability rather than receptor availability — benefit is expected to be partial rather than curative.
- **3,4-Diaminopyridine (3,4-DAP):** A potassium-channel blocker that increases acetylcholine release and prolongs the presynaptic action potential; a rational adjunct for presynaptic CMS given the mechanism, though **no published data specifically document 3,4-DAP use/response in a SNAP25-CMS/CMS18 patient** in the sources reviewed. General CMS caution: fast-channel CMS patients have died when started on 3,4-DAP, underscoring the need for cautious, monitored introduction of this class in any CMS subtype, including this one, until subtype-specific safety data exist.
- **Salbutamol (albuterol)/beta-2 agonists:** Used in other presynaptic/synaptic-basal-lamina CMS subtypes (e.g., COLQ, COL13A1/CMS19) to improve NMJ structure/function; **no SNAP25/CMS18-specific outcome data identified** in the reviewed literature — response is undocumented for this specific gene.
- No pharmacogenomic (PharmGKB/CPIC) guidance specific to SNAP25-CMS drug selection has been published.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy (ASO/siRNA/mRNA), targeted small-molecule, or immunotherapy approach has been developed or trialed for SNAP25-CMS. Given the dominant-negative/neomorphic mechanism (not simple loss-of-function), an **allele-selective knockdown strategy (e.g., ASO)** would be a mechanistically rational future direction (analogous to other dominant-negative SNARE/channel disorders) but has not been reported.

**Surgical/interventional:** No disease-specific surgical intervention reported; general supportive orthopedic management of contractures (e.g., serial casting/tenotomy for arthrogryposis-related contractures) may apply per general arthrogryposis management principles, though not specifically documented for a SNAP25-CMS case.

**Supportive/rehabilitative care:**
- Respiratory support (mechanical ventilation) is critical in severe neonatal presentations and was central to the (unsuccessful) management of the Q177Ter case.
- Physical therapy, occupational therapy for contracture management and motor/ataxia-related functional impairment.
- Antiepileptic drug management for the seizure component — the index patient's seizures were noted as **poorly responsive to valproic acid** between ages 5-8, indicating this population may include drug-resistant epilepsy requiring individualized anticonvulsant selection (general DEE-management principles would apply — e.g., broader-spectrum agents, possible ketogenic diet consideration — though no SNAP25-specific antiepileptic-response data were identified).
- Speech/communication therapy for patients with absent/impaired speech.

**Experimental treatments:** No registered clinical trials (ClinicalTrials.gov) specific to SNAP25-CMS/CMS18 were identified in this research.

**Treatment outcomes/response rates:** No systematic response-rate data exist given the case-report-level evidence base; anecdotal partial response to neostigmine in one patient is the only quantified pharmacologic response documented in the reviewed literature.

**Treatment strategy/algorithm:** No SNAP25-CMS-specific treatment algorithm exists; management follows general presynaptic-CMS principles (trial of AChE inhibitor ± 3,4-DAP, with caution regarding drugs known to worsen NMJ transmission — see below) combined with standard DEE/epilepsy management and multidisciplinary supportive care (respiratory, orthopedic, developmental).

**Drugs to avoid in CMS generally (applies to CMS18 by extension):** Ciprofloxacin, chloroquine, procaine/local anesthetics of that class, lithium, phenytoin, beta-blockers, procainamide, and quinidine are flagged in GeneReviews as agents that can exacerbate neuromuscular transmission defects across CMS subtypes and should be used cautiously if at all.

**NCIT term suggestions:** Pharmacotherapy (`NCIT:C15986`); the specific AChE-inhibitor and 3,4-DAP mechanisms would be captured via `therapeutic_agent` (CHEBI terms for pyridostigmine, neostigmine, amifampridine/3,4-DAP, salbutamol) rather than a distinct NCIT action term beyond generic pharmacotherapy.

---

## 13. Prevention

**Primary prevention:** Not applicable — as a de novo dominant disorder with no identified environmental trigger, there is no primary-prevention strategy (no vaccination, risk-factor modification, or avoidable exposure relevant to causation).

**Secondary prevention/screening:** No population or targeted screening program exists. **Prenatal diagnosis** (via chorionic villus sampling/amniocentesis with targeted variant testing) could be offered in the rare scenario of a family with a previously molecularly confirmed affected child, given the small but nonzero possibility of parental germline mosaicism, though this has not been formally quantified for SNAP25.

**Genetic counseling:** Recurrence risk for future pregnancies in a family with one affected child is expected to be **low but not zero** (consistent with de novo dominant disorders generally, accounting for the possibility, though unconfirmed for SNAP25, of low-level parental germline mosaicism); genetic counseling should convey this general de novo-dominant recurrence framework (typically quoted in the 1-2% range for de novo dominant conditions generically, pending disorder-specific data) rather than the ~25%/50% Mendelian recurrence risks that apply to recessive/dominant-inherited CMS subtypes.

**Public health/behavioral interventions:** Not applicable — no modifiable behavioral, dietary, or environmental risk factor has been identified for this monogenic disorder.

**Prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring SNAP25-related myasthenic/encephalopathic disease has been reported in non-human species (companion animals, livestock, or wildlife) in the literature reviewed. SNAP25 orthologs are highly conserved across vertebrates (human SNAP25 gene ID 6616; mouse ortholog *Snap25*, MGI:98331; conservation extends to *Drosophila* and yeast, as reflected in the cross-species functional-domain conservation discussed below).

**Natural disease/veterinary relevance:** Not documented — no OMIA (Online Mendelian Inheritance in Animals) entries or veterinary case series for spontaneous SNAP25-associated disease were identified.

**Comparative biology/evolutionary conservation:** The SNARE-complex fusion mechanism disrupted in CMS18 is **deeply evolutionarily conserved** — the yeast SNAP25 homolog **SEC9** shows an analogous temperature-sensitivity phenotype when an equivalent coiled-coil domain mutation is introduced, and *Drosophila* SNAP-25 mutants (SNAP-25ts, Gly50→Glu in the first amphipathic helix) similarly destabilize SNARE complex thermal stability and produce temperature-dependent neurotransmission defects — directly supporting the human dominant-negative destabilization mechanism proposed for I67N.

**Transmission:** Not applicable — non-communicable monogenic disorder, no zoonotic or cross-species transmission relevance.

---

## 15. Model Organisms

**Mouse models:**
- ***Snap25* null (knockout) mice:** **Homozygous null is embryonic/perinatal lethal** — Snap25⁻/⁻ mice die at birth due to failure of evoked (calcium-triggered) neurotransmitter release, while spontaneous release persists, directly demonstrating SNAP25's essential, non-redundant role in fast synchronous synaptic vesicle exocytosis (the same biochemical process disrupted by the human dominant-negative/neomorphic disease variants). **Heterozygous *Snap25*⁺/⁻ mice survive to adulthood and are fertile**, showing relatively mild behavioral phenotypes (notably hypoactivity) — a haploinsufficiency model that is mechanistically distinct from (and phenotypically milder than) the human dominant-negative disease alleles, illustrating that the human disease variants are not simple loss-of-function/dosage models.
- **"Blind-drunk" mouse (*Snap25* I67T, or per some literature descriptions "S187A"-adjacent regulatory-domain models):** A **dominant, spontaneous *Snap25* point mutation** (I67T — note the striking similarity to the human I67N disease variant, affecting the identical residue) causes **impaired vesicle trafficking, abnormal sensorimotor gating, and ataxia** in heterozygous mice — a close phenotypic and molecular parallel to human CMS18/DEE117, providing strong cross-species validation that mutation at this specific SNAP25 residue produces a dominant, SNARE-destabilizing, ataxia-associated phenotype. This model has additionally been used to study impaired pancreatic beta-cell granule exocytosis and psychiatric/schizophrenia-relevant endophenotypes (impaired sensorimotor gating), reflecting SNAP25's broader dense-core-vesicle exocytosis role beyond classical fast synaptic transmission.
- **Region/cell-type-specific conditional *Snap25* deletion models** (e.g., cortical-projection-neuron-specific loss) have been used to dissect circuit-specific consequences relevant to the cortical hyperexcitability/epilepsy component of the human phenotype, and brain-specific SNAP-25 deletion models show elevated extracellular glutamate and schizophrenia-like behavior, offering a partial model for the CNS excitability phenotype.

**Invertebrate models:**
- ***Drosophila* SNAP-25ts** (temperature-sensitive paralytic mutant, Gly50→Glu): demonstrates that SNARE complex assembly/disassembly cycling is required for synaptic exocytosis; the mutant SNARE complex is thermally unstable at 37°C (dissociates), producing temperature-dependent facilitation (increased release at permissive temperature) followed by failure of release (restrictive temperature) — mechanistically informative for understanding how discrete point mutations destabilize the SNARE bundle, directly analogous to the human I67N dominant-negative mechanism.
- **Yeast SEC9** (SNAP25 homolog): an equivalent coiled-coil domain mutation confers temperature sensitivity, underscoring deep conservation of this structural mechanism across ~1 billion years of eukaryotic evolution.

**Cellular/in vitro models:**
- **PC12/chromaffin cell transfection systems:** Used to directly test human disease-variant SNAP25 constructs for dominant-negative effects on catecholamine (dense-core vesicle) release — the I67N mutant reduced release to 11% of wild-type when cotransfected with wild-type protein, the key functional evidence establishing dominant-negative pathogenicity for this variant in a human-relevant expression system.
- **Reconstituted liposome/membrane-fusion assays and single-vesicle content-mixing assays:** Used extensively (Shen et al. 2014; the 2024 eLife biophysics study) to directly measure the effect of purified mutant SNAP25 protein on calcium-triggered SNARE-mediated membrane fusion kinetics, priming, and the energy landscape of vesicle fusion — the most mechanistically granular data source available for this disease, distinguishing the dominant-negative (I67N) mechanism from the neomorphic gain/loss-of-function (V48F, D166Y) mechanism at a biophysical level.
- **Cultured neuron electrophysiology (mEPSC/EPSC recordings):** Used to characterize the V48F, D166Y, and I67N variants' distinct effects on spontaneous miniature release frequency, evoked EPSC amplitude, and readily-releasable-pool size in central-synapse-relevant neuronal culture systems.

**Model recapitulation/limitations:** The mouse and Drosophila models recapitulate the **core presynaptic exocytosis defect** and, in the case of the blind-drunk I67T mouse, the **ataxia/sensorimotor phenotype** with notable fidelity to the analogous human I67N variant. However, no existing animal model fully recapitulates the **combined myasthenic + epileptic-encephalopathy + intellectual-disability phenotype** seen in human CMS18 patients within a single system, and the complete embryonic/perinatal lethality of the full null mouse model limits its use for studying postnatal disease progression — heterozygous point-mutant "knock-in" models (blind-drunk I67T; other knock-in efforts referenced in the literature) are therefore the most translationally relevant available resource, though systematic characterization of NMJ-specific (as opposed to CNS) phenotypes in these models is not comprehensively reported in the sources reviewed.

---

## Summary of Key Evidence Citations

| Claim | PMID / Source |
|---|---|
| Founding CMS18 description: I67N SNAP25B, myasthenia + cortical hyperexcitability + ataxia + ID | PMID: 25381298 (Shen XM, Selcen D, Brengman J, Engel AG. *Neurology* 2014;83(24):2247-2255) |
| Neonatal lethal Q177Ter case via rapid genome sequencing | Cold Spring Harb Mol Case Stud 2022;8:a006242 (PMC9808558) |
| Biophysical mechanism of I67N (dominant-negative), V48F/D166Y (neomorphic) | eLife 2024, PMID: 38411501 |
| DEE117/CMS18 OMIM clinical synopsis and SNAP25 gene assignment | OMIM #616330; OMIM *600322 |
| SNAP25 embryonic lethality of null mice; heterozygote viability | Multiple mouse knockout studies (PMC6387657 and related) |
| Blind-drunk I67T mouse: dominant Snap25 mutation causing ataxia and impaired sensorimotor gating | PMID: 17283335 (PNAS 2007) |
| Drosophila SNAP-25ts temperature-sensitive SNARE-complex-destabilizing mutant | PMID: 9728921 (Neuron 1998) |
| COL13A1 = CMS19 (distinct entity, not CMS18) — for disambiguation | PMID: 26626625 (Am J Hum Genet 2015) |

---

Sources:
- [Entry - #616330 - DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 117; DEE117 - OMIM](https://omim.org/entry/616330)
- [Entry - *600322 - SYNAPTOSOMAL-ASSOCIATED PROTEIN, 25-KD; SNAP25 - OMIM](https://omim.org/entry/600322)
- [Congenital myasthenic syndrome 18 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4225364/)
- [Congenital myasthenic syndrome 18 (Concept Id: C4225364) - MedGen](https://www.ncbi.nlm.nih.gov/medgen/C4225364)
- [Mutant SNAP25B causes myasthenia, cortical hyperexcitability, ataxia, and intellectual disability - PMC (PMID 25381298)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4277673)
- [Rapid genome sequencing identifies a novel de novo SNAP25 variant for neonatal congenital myasthenic syndrome - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9808558/)
- [SNAP25 disease mutations change the energy landscape for synaptic exocytosis due to aberrant SNARE interactions - eLife (PMID 38411501)](https://elifesciences.org/articles/88619)
- [Congenital Myasthenic Syndromes Overview - GeneReviews (NBK1168)](https://www.ncbi.nlm.nih.gov/books/NBK1168/)
- [A dominant mutation in Snap25 causes impaired vesicle trafficking, sensorimotor gating, and ataxia in the blind-drunk mouse - PNAS (PMID 17283335)](https://www.pnas.org/doi/10.1073/pnas.0610222104)
- [Congenital Myasthenic Syndrome Type 19 Is Caused by Mutations in COL13A1 - PMC (for CMS18/CMS19 disambiguation)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4678414/)
- [SNAP25 gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SNAP25)
- [NM_130811.4(SNAP25):c.256G>A (p.Gly86Arg) AND Congenital myasthenic syndrome 18 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000689120.5//)
- [Two distinct effects on neurotransmission in a temperature-sensitive SNAP-25 mutant - PubMed](https://pubmed.ncbi.nlm.nih.gov/11726512/)
- [Temperature-Sensitive Paralytic Mutations Demonstrate that Synaptic Exocytosis Requires SNARE Complex Assembly and Disassembly - Neuron (PMID 9728921)](https://www.cell.com/neuron/fulltext/S0896-6273(00)80549-8)