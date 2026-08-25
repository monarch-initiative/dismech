---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-15T08:51:22.357403'
end_time: '2026-08-15T09:09:38.870806'
duration_seconds: 1096.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: GNE Myopathy
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
  - claude-opus-5[1m]
  web_search_requests: 6
  num_turns: 64
  total_cost_usd: 8.6453605
  session_id: 503bcb97-2421-472d-82c6-26c48db010a0
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
citation_count: 44
reference_validation:
  total_references: 41
  verified: 41
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GNE Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GNE Myopathy** covering all of the
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

# GNE Myopathy — Comprehensive Disease Characteristics Report

*Prepared 2026-08-15 for dismech knowledge-base curation. Everything below is anchored to a PMID, a database record I pulled live, or a registry entry; where I couldn't verify something I say so out loud rather than smoothing it over. Quotes marked with `>` are verbatim from the cited abstract (pulled from PubMed via eutils this session) and are safe to use as evidence snippets. Anything I flag as **UNVERIFIED** should be re-checked before it lands in YAML.*

---

## 1. Disease Information

### Overview

GNE myopathy is an ultra-rare, adult-onset, autosomal recessive skeletal muscle disease caused by biallelic pathogenic variants in *GNE*, the gene encoding the bifunctional enzyme that runs the first two committed steps of sialic acid biosynthesis. Think of it as a factory whose front-end sugar line is throttled: the cell can still make some sialic acid, but not enough, and the tissue that turns out to be least forgiving of the shortfall is skeletal muscle. Patients typically present in their twenties or thirties with bilateral foot drop, then decline distally-to-proximally over decades — with the striking and diagnostically load-bearing quirk that the quadriceps is spared until very late.

> "GNE myopathy is a rare, adult-onset, autosomal recessive muscle disorder caused by biallelic pathogenic variants in the GNE gene, which encodes a key enzyme in the biosynthesis of sialic acid. Deficient GNE enzyme activity results in decreased production of sialic acid and subsequent hyposialylation of muscle glycoproteins, ultimately leading to progressive muscle degeneration and characteristic histopathological changes." — Yoshioka, Noguchi & Nishino 2025, *Ann Indian Acad Neurol* (**PMID:41082181**)

> "The typical presentation is bilateral foot drop caused by weakness of the anterior tibialis muscles with onset in early adulthood. The disease slowly progresses over the next decades to involve skeletal muscles throughout the body, with relative sparing of the quadriceps until late stages of the disease." — Carrillo, Malicdan & Huizing 2018, *Neurotherapeutics* (**PMID:30338442**)

### Key identifiers (all verified live this session unless noted)

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0011603** (GNE myopathy) |
| OMIM (disease) | **605820** (Nonaka myopathy) |
| OMIM (gene) | **603824** (*GNE*) |
| Orphanet | **ORPHA:602** |
| DOID | DOID:0080718 |
| MedGen | 381298 |
| UMLS | C1853926 |
| SNOMED CT | 702382000 |
| GARD | 0009493 |
| NORD | 2011 |
| NANDO (Japan) | NANDO:1200218 |
| ICD-10 | G71.0 — **UNVERIFIED** (Orphanet was behind a bot-check; confirm) |
| ICD-11 | 8C70.x distal myopathy range — **UNVERIFIED**, confirm before curating |
| MeSH | Indexed as the supplementary concept "Distal myopathy, Nonaka type" (this is what PubMed's query translator maps "GNE myopathy" onto) |

**Allied but distinct MONDO entity:** **MONDO:0958325** — *thrombocytopenia 12 with or without myopathy* (THC12), also *GNE*-caused. This matters for dismech scoping: the platelet phenotype is curated as a separate MONDO entity, so a decision is needed on whether to model it as a subtype, a linked entry, or an extramuscular manifestation of MONDO:0011603. See §3 and §9.

### Synonyms (verbatim from MONDO:0011603)

`inclusion body myopathy autosomal recessive` · `DMRV` · `HIBM2` · `IBM2` · `NM` · `Nonaka myopathy` · `QSM` · `distal myopathy with rimmed vacuoles` · `distal myopathy, Nonaka type` · `hereditary inclusion body myopathy type 2` · `inclusion body myopathy 2, autosomal recessive` · `inclusion body myopathy type 2` · `inclusion body myopathy, autosomal recessive` · `inclusion body myopathy, quadriceps-sparing` · `quadriceps sparing myopathy` · `quadriceps-sparing myopathy` · `rimmed vacuole myopathy`

**The naming history is a real curation hazard.** Two independently described diseases — Nonaka distal myopathy (Japan) and quadriceps-sparing hereditary inclusion body myopathy / IBM2 (Iranian Jewish families) — turned out to be one entity. The unified name "GNE myopathy" was formalized in 2014 (Huizing et al., *Neuromuscul Disord*, **PMID:24685570**). **Do not** confuse this with sporadic inclusion body myositis (sIBM), an inflammatory, late-onset, non-Mendelian disease with a completely different mechanism — the shared "inclusion body" phrase is one of the more expensive naming collisions in neuromuscular medicine.

### Evidence provenance

The information base is **aggregated disease-level**, not EHR-derived: clinical cohorts, two prospective natural-history programs (Japan NCNP; the international GNEM-DMP), national patient registries in Japan and Europe (NCT04009226, NCT01784679), and randomized trials. There is no population-scale EHR phenotype for GNE myopathy that I could find — a real gap given how much of the phenotype frequency data rests on small single-country cohorts.

---

## 2. Etiology

### Primary cause — monogenic

Biallelic (homozygous or compound heterozygous) pathogenic variants in ***GNE*** (HGNC:23657; NCBI Gene 10020; Ensembl ENSG00000159921; UniProt Q9Y223; **9p13.3**). The gene encodes UDP-*N*-acetylglucosamine 2-epimerase / *N*-acetylmannosamine kinase — one polypeptide, two enzyme activities, both required for sialic acid synthesis.

> "Hereditary inclusion body myopathy (HIBM; OMIM 600737) is a unique group of neuromuscular disorders characterized by adult onset, slowly progressive distal and proximal weakness and a typical muscle pathology including rimmed vacuoles and filamentous inclusions… we eventually identified mutations in the UDP-N-acetylglucosamine-2-epimerase/N-acetylmannosamine kinase (GNE) gene in the HIBM families: all patients from Middle Eastern descent shared a single homozygous missense mutation, whereas distinct compound heterozygotes were identified in affected individuals of families of other ethnic origins. Our findings indicate that GNE is the gene responsible for recessive HIBM." — Eisenberg et al. 2001, *Nat Genet* (**PMID:11528398**)

### Genetic risk factors

- **Causal variants:** predominantly missense; see §4 for the full spectrum.
- **Founder alleles** are the dominant epidemiological driver (see §9). Being of Persian/Middle Eastern Jewish, Japanese, Korean, Bulgarian Roma, or certain Indian ancestries substantially raises prior probability.
- **Consanguinity** raises risk in the usual autosomal-recessive way; the Indian and Middle Eastern cohorts show enrichment of homozygotes.
- **Modifier genes:** none established. This is a genuine open question — see §4.

### Environmental risk factors

**No established environmental cause, trigger, or exposure.** There is no toxin, infection, occupational exposure, or dietary factor with credible evidence of causing or precipitating GNE myopathy. Age is a proxy for cumulative disease duration rather than an independent risk factor. Sex is not a strong determinant of susceptibility (see §9 for the sex-ratio nuance in the Japanese registry). **Curation note: leave `environmental:` sparse and honest rather than inventing plausible-sounding exposures.**

### Protective factors

- **Genetic:** none established. Interestingly, the *strongest* candidate for a protective/attenuating allele is a hypomorphic-but-non-catalytic *GNE* variant — Chinese cohort data suggest c.620A>T (p.Asp207Val) is associated with milder disease (§4).
- **Environmental/dietary:** dietary sialic acid intake is the obvious hypothesis, and the one thing tested head-on in a model system came out **negative**:

> "We found that a diet enriched in Neu5Gc-containing glycoproteins had no impact on Neu5Gc immunostaining in muscles of GNEM model mice." — Crowe et al. 2022, *J Neuromuscul Dis* (**PMID:34511508**), MODEL_ORGANISM

  So ordinary dietary sialoglycoprotein loading is *not* protective; only pharmacological monosaccharide dosing moved the needle in that model.

### Gene–environment interactions

None established. The one mechanistically motivated candidate — that muscle contraction generates reactive oxygen species that sialic acid normally buffers, so activity level might modulate damage — is a hypothesis carried in the therapeutic literature, not a demonstrated GxE interaction:

> "Sialic acid acts as a buffer against reactive oxygen species generated during muscle contraction. Increased oxidative stress may relate to muscle atrophy involving patients with GNE myopathy." — Jay et al. 2026, *J Gene Med* (**PMID:42186366**)

Practically, management guidance advises avoiding repetitive/eccentric overexertion and myotoxic drugs (GeneReviews, NBK1262), which is a *clinical* precaution rather than an evidenced interaction.

---

## 3. Phenotypes

### Core muscle phenotype

| Phenotype | Suggested HPO | Onset / course | Frequency | Notes |
|---|---|---|---|---|
| Foot dorsiflexor weakness (bilateral foot drop) — the presenting sign | **HP:0009027** Foot dorsiflexor weakness | Adult, 20–40 y | Near-universal as presentation | Tibialis anterior first |
| Distal lower-limb muscle weakness | **HP:0009053** Distal lower limb muscle weakness | Adult onset (HP:0003581) | 6/9 in the HPO-annotated source cohort (**PMID:12177386**) | HPO's own annotation frequency |
| Distal muscle weakness (general) | **HP:0002460** Distal muscle weakness | Adult, progressive | Very frequent | |
| Distal amyotrophy | **HP:0003693** Distal amyotrophy | Progressive | Frequent | |
| Steppage gait / gait disturbance | **HP:0003376** Steppage gait; **HP:0001288** Gait disturbance | Early | Frequent | Consequence of foot drop |
| Proximal muscle weakness (hip girdle, later) | **HP:0003701** Proximal muscle weakness | 5–20 y after onset | Frequent, later | |
| **Relative quadriceps sparing** | *No dedicated HP term found* — model as an explicit negative/pattern statement | Persists until advanced disease | Highly characteristic | The single most useful diagnostic discriminator |
| Neck muscle weakness | **HP:0000467** Neck muscle weakness | Advanced | Occasional | |
| Scapular winging / shoulder-girdle weakness | **HP:0003691** Scapular winging | Variable | Occasional | UE pattern is variable |
| Loss of ambulation | **HP:0002505** Loss of ambulation | ~10–20 y after onset | Frequent | Wheelchair dependence |
| Respiratory insufficiency due to muscle weakness | **HP:0002747** | Late | Rare/occasional | %FVC declines measurably even at 1 y in non-ambulant patients (**PMID:24656604**) |

### Laboratory / histopathological phenotypes

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Elevated circulating creatine kinase | **HP:0003236** | Normal to mildly/moderately elevated; helps separate from dysferlinopathy where CK is very high |
| Rimmed vacuoles on biopsy | **HP:0003805** Rimmed vacuoles | Definitional; actually autophagic vacuoles |
| Deposits immunoreactive to β-amyloid protein | **HP:0003791** | Congophilic inclusions; also ubiquitin, tau, lysosomal proteins |
| Increased variability in muscle fiber diameter | **HP:0003557** | With atrophic and angular fibers |
| EMG: myopathic abnormalities | **HP:0003458** | |
| Absence of inflammation | *(model as negative finding)* | Key contrast with sporadic IBM |

### Extramuscular phenotypes (registry-derived, Japan)

The best frequency data here comes from a nationwide Japanese registry questionnaire (Yoshioka et al. 2022, *Clin Neurol Neurosurg*, **PMID:34871992**; response rate 62.4%, n=126):

> "Of the participants, 4.1% (5/123) had a diagnosis of idiopathic thrombocytopenia, and 16.3% (8/49) of males and 6.6% of females (5/76) had a diagnosis of SAS. In total, 0.8% (1/126) of participants had pervasive developmental disabilities and 14.7% (16/109) had a psychiatric disease."

> "The frequencies of idiopathic thrombocytopenia and SAS among Japanese GNE myopathy patients were higher than those observed in the general Japanese population. Routine blood tests and evaluation of sleep-disordered breathing should be considered in order to better manage GNE myopathy patients."

| Extramuscular phenotype | Suggested HPO | Frequency (Japanese registry) |
|---|---|---|
| Thrombocytopenia | **HP:0001873** Thrombocytopenia | 4.1% ("idiopathic thrombocytopenia" diagnosis) |
| Obstructive sleep apnea / SAS | **HP:0002870** Obstructive sleep apnea | 16.3% males, 6.6% females |
| Psychiatric disease | *(non-specific; needs a decision)* | 14.7% — **caution:** a self-reported "psychiatric disease" diagnosis in a chronic disabling myopathy is heavily confounded by reactive depression. Do not curate this as a mechanistic phenotype. |

**Thrombocytopenia is the extramuscular finding with a real mechanistic story.** Some individuals with biallelic *GNE* variants have congenital macrothrombocytopenia with or without myopathy, driven by a *platelet* sialylation defect and accelerated platelet clearance:

> "ES revealed two suspicious variants, one likely pathogenic and one a variant of uncertain significance, in the UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase (GNE) gene, and flow cytometry showed diminished expression of surface platelet sialic acid (about 5%) but normal red cell sialic acid." — Montcrieff et al. 2023, *Transfusion* (**PMID:36941763**)

That paper's second half is clinically actionable and worth an evidence item: the patient's thrombopoietin level was low and they responded to TPO-mimetic treatment, so **platelet transfusion may be avoidable** in these cases.

### Severity, progression, variability

Severity is variable and progression is slow. Two structured quantifications:

- **1-year Japanese natural history** (Mori-Yoshimura et al. 2014, **PMID:24656604**, n=24): *"Summed manual muscle testing of 17 muscles, grip power, and percent force vital capacity (%FVC) were significantly reduced (p<0.05)… The decrement in %FVC was significant among non-ambulant patients, whereas the decrement in grip power tended to be greater among ambulant patients."*
- **3-year international GNEM-DMP** (Lochmüller et al. 2021, **PMID:33459658**, 101 enrolled / 60 completing 36 months): *"Mean (SD) HHD UE composite score decreased from 34.3 kg (32.0) at baseline to 29.4 kg (32.6) kg at month 36 (LS mean change [95%CI]: -3.8 kg [-5.9, -1.7]; P = 0.0005). Mean (SD) HHD LE composite score decreased from 32.0 kg (34.1) at baseline to 25.5 kg (31.2) at month 36 (LS mean change [95%CI]: -4.9 [-7.7, -2.2]; P = 0.0005)."*

**Phenotypic outliers exist.** At least one family broke the canonical pattern with severe *posterior* calf involvement and a spared anterior compartment (Papadimas et al. 2016, *J Neuromuscul Dis*, **PMID:27854221**): *"in contrast to the typical pattern of muscle involvement, one of them showed severe involvement of posterior calf muscles with spared anterior compartment of the lower leg muscles."* Worth curating as a documented atypical presentation so the entry doesn't over-promise the quadriceps-sparing rule.

### Quality-of-life impact

The disease-specific instrument is the **GNE myopathy–Functional Activity Scale (GNEM-FAS)**, with mobility, upper-extremity, and self-care domains — used as a key secondary endpoint in the phase 3 trial and tracked in the DMP:

> "GNEM-FAS scores were more severe at baseline in subjects who walked <200 meters versus ≥200 meters in 6 minutes; in both groups, GNEM-FAS total, mobility, UE, and self-care scores decreased from baseline through month 36." (**PMID:33459658**)

I found **no** published EQ-5D, SF-36, or PROMIS study specific to GNE myopathy in this search. That's a real gap — flag it rather than substituting generic myopathy QoL data.

---

## 4. Genetic / Molecular Information

### The gene

| Field | Value |
|---|---|
| Symbol | *GNE* |
| Name | glucosamine (UDP-*N*-acetyl)-2-epimerase / *N*-acetylmannosamine kinase |
| HGNC | **hgnc:23657** (lowercase prefix per dismech convention) |
| Location | 9p13.3 |
| NCBI Gene | 10020 |
| Ensembl | ENSG00000159921 |
| UniProt | Q9Y223 |
| OMIM | 603824 |
| Previous symbol | IBM2 |

### ⚠ The two-numbering-system trap — read this before curating any variant

*GNE* has two commonly cited transcripts, and the older literature uses the shorter one. Every variant in the pre-2014 literature is offset by 31 residues.

> "Note that we use a new mutation nomenclature based on the longest transcript (GenBank: NM_001128227), which encodes a 31-amino acid longer protein than the originally described one (GenBank: NM_005476), which has been used previously in most papers." — Nishino, Carrillo-Carrasco & Argov 2015, *JNNP* (**PMID:25002140**)

| Old (NM_005476) | Current (NM_001128227) | cDNA | Population |
|---|---|---|---|
| p.Met712Thr | **p.Met743Thr** | c.2228T>C | Middle Eastern / Persian Jewish founder |
| p.Val572Leu | **p.Val603Leu** | c.1807G>C | Japanese founder |
| p.Asp176Val | **p.Asp207Val** | c.620A>T | Japanese founder |

Curate in current (NM_001128227) nomenclature and record the legacy name as a note — otherwise the mouse-model literature (which uses `GneM712T`, `hGNE D176V`) will look like it's about different alleles.

### Pathogenic variant spectrum

- **>255 variants** reported across **>1,000 affected individuals** (GeneReviews NBK1262).
- **Predominantly missense**, distributed across both catalytic domains: *"Missense variants predominantly located in the epimerase/kinase domain coding region, indicating the impairment of catalytic function as a key pathogenic consequence."* — Jiao et al. 2024, *J Med Genet* (**PMID:39332896**)
- **Functional consequence: loss of function (hypomorphic).** Complete biallelic null is not compatible with the human phenotype — *Gne* knockout is embryonic lethal in mouse (**PMID:17704511**), so surviving human genotypes retain residual enzyme activity. Curate `functional_impact_category: PARTIAL_LOSS_OF_FUNCTION` where the literature supports it, `LOSS_OF_FUNCTION` otherwise. **Do not curate GAIN_OF_FUNCTION for myopathy alleles** — that's the *sialuria* mechanism (below).
- **Non-coding and structural variants are under-ascertained.** The Chinese multicentre study found deep intronic variants (c.862+870C>T, c.52-8924G>T, c.1505-12G>A) and a 639 bp insertion at chr9:36249241 only via WGS and Nanopore long-read sequencing: *"Comprehensive techniques such as WGS and Nanopore LRS warrants the identifying of GNE variants."* (**PMID:39332896**). Practical implication: a single-negative-panel result does not exclude the diagnosis.
- **Somatic vs germline:** germline exclusively. No somatic/mosaic disease mechanism reported.

### Genotype–phenotype correlation

Historically described as weak, but two concrete signals have emerged:

1. **Non-catalytic-domain alleles are milder.** *"The high allele frequency of the non-catalytic GNE variant, c.620A>T, might underlie the milder phenotype of Chinese patients… Patients with the non-catalytic GNE variant, c.620A>T, had a milder disease progression and later wheelchair use."* (**PMID:39332896**). The same cohort showed onset ~2 years later than Japanese, Korean, and Jewish cohorts.
2. **A weak MRI–genotype link:** *"a weak genotype-muscle MRI association was found in which tibialis posterior was more involved in patients with the most frequent mutation, i.e., C.2228T > C (p.M743T) mutation; however, this finding may be related to longer disease duration."* — Fatehi et al. 2021, *J Neuromuscul Dis* (**PMID:34334416**). Note the authors' own confounding caveat — carry it into any curated claim.

### Allelic disorders — two, and they are mechanistically opposite

1. **Sialuria (OMIM 269921)** — *autosomal dominant*, caused by missense changes in the **allosteric CMP-sialic-acid feedback site** of GNE, producing **overproduction** of free sialic acid. This is the same gene doing the opposite thing:
 > "Sialuria is a dominant disorder caused by missense mutations in the allosteric site of GNE… The resultant loss of feedback inhibition of GNE-epimerase activity by CMP-sialic acid causes excessive production of free sialic acid." — Klootwijk et al. 2008, *FASEB J* (**PMID:18653764**)

 The structural basis is resolved: *"the CMP-Neu5Ac binding mode clearly elucidates why mutations in Arg263 and Arg266 can cause sialuria."* — Chen et al. 2016, *Sci Rep* (**PMID:26980148**)
2. **Thrombocytopenia 12 with or without myopathy (MONDO:0958325)** — biallelic *GNE*, platelet-restricted or platelet-predominant expression.

Curation implication: *GNE* is a **one-gene, three-phenotype** locus with dominant-GOF and recessive-LOF arms. That's worth an explicit `mechanistic_hypotheses` or notes treatment in the entry.

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none established. Candidate territory only.
- **Epigenetics:** no DNA-methylation or histone-modification findings specific to GNE myopathy found in this search. **Not available.**
- **Chromosomal abnormalities:** not a mechanism in this disease. Aneuploidy, translocations, CMA/karyotype/FISH findings — **not applicable** (see §10 for the diagnostic corollary).

### Population allele frequency

The comprehensive gnomAD-based variant compilation is Derksen et al. 2024, *Hum Mutat* (**PMID:40225917**) — see §9 for the prevalence figures it derives. GeneReviews estimates a worldwide *GNE* pathogenic-variant carrier rate of **~1:203**.

---

## 5. Environmental Information

**Environmental factors:** none established. **Lifestyle factors:** none established as causal; exercise prescription is a management question (§12), not an etiological one. **Infectious agents:** not applicable — this is a Mendelian metabolic myopathy with no infectious component.

The only environment-adjacent finding worth recording is the negative dietary result in the Neu5Gc-visualizable mouse model (**PMID:34511508**, quoted in §2): dietary sialoglycoprotein loading does not raise muscle sialic acid. Curate that as a *refuted* protective hypothesis rather than omitting it — negative results are load-bearing here because "just eat more sialic acid" is an intuition patients and clinicians both reach for.

---

## 6. Mechanism / Pathophysiology

### The causal chain, upstream → downstream

**Step 1 — enzymatic block (MOLECULAR).** Biallelic hypomorphic *GNE* variants reduce UDP-GlcNAc 2-epimerase and/or ManNAc kinase activity. GNE catalyses the first committed and rate-limiting steps of the Neu5Ac pathway: UDP-GlcNAc → ManNAc (epimerase) → ManNAc-6-P (kinase) → … → Neu5Ac → CMP-Neu5Ac. The pathway is feedback-inhibited at the epimerase domain by the end product CMP-Neu5Ac (**PMID:26980148**).

- GO: **GO:0008761** UDP-N-acetylglucosamine 2-epimerase activity (`modifier: DECREASED`)
- GO: **GO:0009384** N-acylmannosamine kinase activity (`modifier: DECREASED`)
- GO: **GO:0046380** N-acetylneuraminate biosynthetic process (`modifier: DECREASED`)
- CHEBI: **CHEBI:16264** UDP-N-acetyl-α-D-glucosamine → **CHEBI:63153** N-acetyl-D-mannosamine → **CHEBI:17012** N-acetylneuraminic acid → **CHEBI:16556** CMP-N-acetyl-β-neuraminic acid

**Step 2 — free sialic acid depletion (MOLECULAR).** The single best-quantified node, and the one that also explains quadriceps sparing:

> "Mean serum free SA level was 0.166 μg/mL in patients and 18% lower (p<0.001) than that of age-matched control samples (0.203 μg/mL). In biopsies obtained from patients, mean free SA levels of different muscles ranged from 0.046-0.075 μg/μmol Cr and were markedly lower by 72-85% (p<0.001) than free SA from normal controls." — Chan et al. 2017, *PLoS One* (**PMID:28267778**)

> "Normal quadriceps had significantly lower levels of free SA (reduced by 39%) and total SA (reduced by 53%) compared to normal gastrocnemius. A lower SA requirement for quadriceps may be linked to the reported quadriceps sparing in GNEM." (same)

That second quote is the mechanistic explanation for the disease's most distinctive clinical sign, and it's an unusually clean claim to curate. The same paper also raises the possibility that the pathogenic target set is narrow: *"Differences in mean total SA levels in muscle from patients compared with normal controls were less distinct and more variable between different muscles, suggesting a small subset of sialylation targets could be responsible for the pathogenesis of GNEM."*

**Step 3 — hyposialylation of muscle glycoproteins (MOLECULAR/CELLULAR).** GO: **GO:1990743** protein sialylation (`modifier: DECREASED`). The specific glycoprotein target(s) whose hyposialylation is pathogenic are **not definitively identified** — this is the field's central open question. (α-dystroglycan and NCAM have been examined over the years; I did not verify a definitive result in this session, so don't curate a named target without a fresh citation.)

**Step 4 — proteostasis failure and autophagic block (CELLULAR).** Rimmed vacuoles are not vacuoles in the naive sense; they are accumulated autophagic material. The newest mechanistic work gives an actual signalling chain:

> "Mechanistically, our data reveal that aberrant activation of the noncanonical AKT-mTORC1 pathway-driven by excessive extracellular matrix production-induces inhibitory phosphorylation of ULK1, thereby suppressing autophagy initiation." — Kim et al. 2026, *Exp Mol Med* (**PMID:41963465**), IN_VITRO (hPSC-derived myoblasts, Gne-KO C2C12, neuromuscular organoids)

- GO: **GO:0016236** macroautophagy (`modifier: DECREASED`)

**Step 5 — β-amyloid and misfolded protein accumulation (CELLULAR).** The mouse model established the *temporal ordering*, which is the mechanistically interesting part — amyloid comes first:

> "A compelling finding is the development of beta-amyloid deposition in myofibers by 32 weeks, which clearly precedes RV formation at 42 weeks." — Malicdan et al. 2007, *Hum Mol Genet* (**PMID:17704511**), MODEL_ORGANISM

The inclusions are immunoreactive to *"beta-amyloid, lysosomal proteins, ubiquitin and tau proteins"* (same paper). A dedicated review argues amyloid-β is mechanistically upstream of the atrophy rather than an epiphenomenon (Zhang, Shang & Miao 2022, *Neurol Sci*, **PMID:35904705**), though it is explicit that *"the cause and process of the formation of amyloid β in the pathological process of GNE myopathy are unclear"* — curate as an open hypothesis, not settled fact.

**Step 6 — myofiber atrophy, degeneration, weakness (TISSUE → ORGANISM).**

### The pivotal causality proof

Whether hyposialylation is *the* cause (versus GNE having other essential jobs) was resolved by rescue in the mouse — this is the highest-value single evidence item in the whole entry:

> "By showing that muscle atrophy and weakness are completely prevented in a mouse model of DMRV-hIBM after treatment with sialic acid metabolites orally, we provide evidence that hyposialylation is indeed one of the key factors in the pathomechanism of DMRV-hIBM." — Malicdan et al. 2009, *Nat Med* (**PMID:19448634**), MODEL_ORGANISM

Note the authors' own hedge — *"one of the key factors"* — and preserve it. The human trials (§12) are precisely why that hedge matters.

### Metabolic changes beyond sialic acid

Glycosphingolipids are secondarily deranged, and correctably so:

> "Not only neutral GSLs, but also sialylated GSLs, were significantly increased compared to controls in all tested models of GNE myopathy. Treatment of GNE myopathy fibroblasts with N-acetylmannosamine (ManNAc), a sialic acid precursor downstream of GNE epimerase activity, ameliorated the increased total GSL concentrations." — Patzel et al. 2014, *J Inherit Metab Dis* (**PMID:24136589**), IN_VITRO + MODEL_ORGANISM

### Immune system involvement

**Essentially none — and the absence is diagnostic.** Muscle biopsy shows *"lack of inflammation"* (**PMID:30338442**). This is the key histological separator from sporadic IBM. One caveat: a case series of *GNE*-thrombocytopenia reported "moderate complement activation" (PMC8630651) — I did not verify that abstract directly, so treat as **UNVERIFIED**.

### Tissue damage mechanisms

Oxidative stress (sialic acid as a ROS buffer during contraction — **PMID:42186366**), impaired autophagic clearance (**PMID:41963465**), and protein aggregation. Fibrosis and fatty replacement are the end-stage tissue outcomes visible on MRI (§10). Notably **not** ischemia, necrosis-predominant injury, or inflammation.

### Other proposed GNE functions (mechanistically unsettled)

Beyond sialic acid synthesis, GNE has been proposed to participate in protein aggregation handling, apoptosis, ER stress, cell migration, HSP70 chaperone activity, autophagy, muscle atrophy signalling, and myogenesis. The 2025 review frames the pathophysiology as still incompletely resolved: the exact mechanism linking hyposialylation to *muscle-restricted* pathology remains *"poorly understood"* despite sialic acid reduction being systemic (**PMID:34511508**). That tissue-restriction paradox — the enzyme defect is everywhere, the disease is in muscle — deserves an explicit `KNOWLEDGE_GAP` discussion in the entry.

### Molecular profiling

- **Transcriptomics:** Kim et al. 2026 (**PMID:41963465**) performed transcriptome analysis on two independent hPSC-derived GNE myoblast models and *"identified multiple autophagy-related gene sets as pathogenic signatures of GNE myopathy."* They then ran a **transcriptome-based drug screen using gene-signature reversal**, which nominated copanlisib (an FDA-approved PI3K inhibitor) — a nice example of computational repurposing feeding back into a mechanism claim.
- **Metabolomics/glycomics:** LC/MS/MS free and total sialic acid quantification in serum and muscle (**PMID:28267778**); HPLC glycosphingolipid profiling (**PMID:24136589**).
- **Proteomics:** no dedicated GNE myopathy proteomics dataset surfaced in this search. **Gap.**
- **Single-cell / spatial transcriptomics:** none found specific to GNE myopathy. **Gap.**
- **Functional genomics screens (CRISPR/RNAi):** no disease-specific screen found; the allele-specific siRNA work (**PMID:18653764**) is a therapeutic proof-of-concept for *sialuria*, not a screen.

---

## 7. Anatomical Structures Affected

### Organ / system level

- **Primary:** skeletal muscle — **UBERON:0001134** skeletal muscle tissue. Musculoskeletal system.
- **Secondary:** respiratory system (via diaphragm/accessory muscle weakness, HP:0002747); hematological system (megakaryocyte/platelet lineage in the thrombocytopenia arm).
- **Notably spared:** cardiac muscle. The Japanese 1-year natural history study reported *"No cardiac events were observed."* (**PMID:24656604**). Baseline echocardiography is nonetheless recommended surveillance (GeneReviews).
- **Not affected:** CNS/peripheral nerve (this is a pure myopathy — no neuropathy, no cognitive phenotype).

### Specific muscles — the MRI-derived involvement hierarchy

From Fatehi et al. 2021 (**PMID:34334416**), n=18, cluster analysis of fat infiltration:

> "The four muscles with the highest fat infiltration were adductor magnus, tibialis anterior, semitendinosus, and semimembranosus."

> "cluster 3, atypical muscle involvement with low-fat infiltration: rectus femoris, sartorius, vastus intermedius, vastus medialis, and vastus lateralis."

That second cluster *is* the quadriceps — imaged confirmation of the sparing rule. Note that adductor magnus topping the list is a useful, under-appreciated early marker.

| Muscle | UBERON | Involvement |
|---|---|---|
| Tibialis anterior | **UBERON:0001385** | Earliest and most severe |
| Semitendinosus | *(hamstring; verify specific ID)* | High fat infiltration |
| Semimembranosus | **UBERON:0001381** | High fat infiltration |
| Biceps femoris | **UBERON:0001374** | High (cluster 1) |
| Gastrocnemius | **UBERON:0001388** | Involved (cluster 1) |
| Quadriceps femoris | **UBERON:0001377** | **Spared until advanced disease** |

### Tissue and cell level

- **CL:0008002** skeletal muscle fiber — the primary affected cell type
- **CL:0000594** skeletal muscle satellite cell — regenerative compartment; involvement plausible via impaired myogenesis but **not firmly established**
- **CL:0000056** myoblast — the workhorse of the in vitro models (C2C12, hPSC-derived)
- **CL:0000556** megakaryocyte — the thrombocytopenia arm; MONDO:0958325 explicitly describes *"abnormal megakaryocyte maturation and a defect in platelet surface sialylation"*
- **CL:0000653** podocyte — **model-organism only.** The `Gne M712T/M712T` knockin mouse develops podocytopathy and proteinuria, *not* myopathy (**PMID:17549255**). Curate carefully as a HUMAN_MODEL_MISMATCH: humans with GNE myopathy do not characteristically have glomerular disease.

### Subcellular level

- Autophagosome / autolysosome — the rimmed vacuole itself (GO cellular component; **verify specific CC ID before curating**)
- Golgi apparatus and ER — site of sialyltransferase-mediated glycan capping; where the sialylation deficit becomes structural
- Sarcolemma — sarcolemmal sialylation is the pharmacodynamic readout used in the ManNAc trial (**PMID:34257421**)
- Cytosol — GNE's own localization
- Mitochondria — mitochondrial process impairment has been reported in HIBM (**PMID:18723858**, abstract not verified this session — **UNVERIFIED**)

### Localization / lateralization

**Bilateral and broadly symmetric**, with a **length-dependent, distal-to-proximal** gradient in the lower limbs. Upper-extremity involvement is more variable in pattern (shoulder abduction can precede hand weakness). Asymmetry is not characteristic; marked asymmetry should prompt reconsideration of the diagnosis.

---

## 8. Temporal Development

### Onset

- **Typical age:** 20–40 years; GeneReviews gives the presentation as *"bilateral foot drop caused by anterior tibialis weakness"* in that window. HPO annotation: **HP:0003581** Adult onset.
- **Onset pattern:** insidious and chronic. Not acute, not episodic, not relapsing.
- **Ancestry-linked shift:** the Chinese cohort showed *"later onset ages by 2 years"* than Japanese, Korean, and Jewish cohorts (**PMID:39332896**).

### Progression timeline (GeneReviews NBK1262)

| Time from onset | Milestone |
|---|---|
| ~5 years | Complete loss of ankle dorsiflexion; ankle-foot orthoses required |
| 5–10 years | Loss of knee flexion; assistive walking devices |
| 10–20 years | Wheelchair may be needed; quadriceps may finally become involved |
| Advanced | Respiratory muscle involvement (rare) |

### Course

- **Pattern:** chronically progressive, lifelong. No remission — spontaneous or treatment-induced — has been described. No relapsing-remitting component. No episodic decompensation.
- **Rate:** slow, and slow enough that it broke conventional trial design. The Bayesian disease-progression model was built precisely because *"The GNE Myopathy Progression Model provides an understanding of disease progression that would have otherwise required a natural history of unfeasible duration."* — Quintana et al. 2019, *Stat Med* (**PMID:30511500**)
- **Duration:** lifelong from onset.
- **Genotype-linked rate:** c.620A>T (p.D207V) carriers show *"milder disease progression and later wheelchair use"* (**PMID:39332896**).

### Critical intervention windows

The mouse data argue strongly for early intervention: sialic acid metabolites given **prophylactically** *"completely prevented"* atrophy and weakness (**PMID:19448634**), whereas human trials in established disease have at best slowed decline. This asymmetry — prevention works, rescue barely does — is the most important translational lesson in the field and should be curated as such.

---

## 9. Inheritance and Population

### Epidemiology

Two eras of estimate, and they disagree by an order of magnitude:

**Classic (registry/clinical ascertainment):**
> "It has an estimated prevalence of 1 to 9:1,000,000." — Carrillo et al. 2018 (**PMID:30338442**); the same 1–9 per million band appears in GeneReviews (Orphanet-derived).

**Genomic (carrier-frequency-derived):**
> "Our most conservative estimate suggested a prevalence of 18.46 cases per million, while our most liberal estimate places the prevalence at 95.42 cases per million. When accounting for variant severity, this range drops to 11.00-87.68 cases per million. Our findings indicate that the true global prevalence of GNEM is greater than previous predictions underscoring that this condition is considerably more widespread than previously believed." — Derksen et al. 2024, *Hum Mutat* (**PMID:40225917**)

The authors are explicit about why the old numbers are low: *"the accuracy of these estimates is limited by underdiagnosis, misdiagnosis, and bias introduced by founder allele frequencies."*

**Curation guidance for the `prevalence:` block:** record **both**, with distinct `population`/`measure_type`/`notes`. Suggested structure:
- Orphanet/clinical: `prevalence_class: BAND_1_9_PER_1000000`, `rate_per_100000: 0.1–0.9`, `measure_type: POINT_PREVALENCE`
- gnomAD-derived: `rate_per_100000: 1.1–8.8` (severity-adjusted 11.00–87.68 per million), `measure_type: POINT_PREVALENCE`, notes recording the Hardy-Weinberg modelling assumption
- Carrier frequency: **~1:203 worldwide** (GeneReviews), `measure_type: CARRIER_FREQUENCY`

**Incidence:** no incidence figure found. **Gap.**

### Inheritance

- **Autosomal recessive** — **HP:0000007**. Verified in HPO annotation of OMIM:605820 (source PMID:12177386).
- **Penetrance:** appears high/complete for biallelic pathogenic genotypes, but *age-dependent* — a 25-year-old biallelic carrier may be presymptomatic. I found no formal penetrance estimate. **Gap — do not assert "complete penetrance" without a source.**
- **Expressivity:** variable, in onset age, muscle pattern (**PMID:27854221**), and whether thrombocytopenia occurs.
- **Anticipation:** not applicable — no repeat expansion.
- **Germline mosaicism:** not reported.
- **Consanguinity:** relevant, especially in Middle Eastern and South Asian populations.

### Founder effects and geography

Founder alleles dominate the epidemiology, and the Eisenberg 2001 haplotype analysis is the classic demonstration:

> "Haplotype analysis around the HIBM gene region of 104 affected people from 47 Middle Eastern families indicates one unique ancestral founder chromosome in this community. By contrast, single non-Jewish families from India, Georgia (USA) and the Bahamas, with QSM and linkage to the same 9p12-13 region, show three distinct haplotypes." (**PMID:11528398**)

| Founder variant | Population | Approx. reported cases (GeneReviews) |
|---|---|---|
| p.Met743Thr (c.2228T>C) | Middle Eastern / Persian Jewish | ~200 |
| p.Val603Leu (c.1807G>C) | Japanese | ~300 |
| p.Asp207Val (c.620A>T) | Japanese | ~230 |

**Geographic distribution:** worldwide but clustered.
> "Although universal and ubiquitous, GNE myopathy prevails in the Jewish community of Persian origin, living in Iran, Israel or in the United States. This condition has also been reported in great number in populations of far-East Asia (Japan and neighboring countries) and, closer to France, in Bulgaria." — Urtizberea & Béhin 2015, *Med Sci (Paris)* (**PMID:26546927**)

**India deserves special mention.** In a 207-patient clinical exome study of the Indian subcontinent, *GNE* was the single largest contributor among solved myopathy cases:
> "Clinical-correlation driven definitive molecular diagnosis was established in 49% (101 cases; 95% CI, 42-56%) of patients with the major contributing pathogenicity in either of three genes, GNE (28%; GNE-myopathy), DYSF (25%; Dysferlinopathy), and CAPN3 (19%; Calpainopathy)." — Chakravorty et al. 2020, *Front Neurol* (**PMID:33250842**)

**China:** 113-patient multicentre cohort, 97 distinct variants of which 36.08% novel (**PMID:39332896**).

### Sex ratio and age distribution

The Japanese registry survey enrolled *"51 male and 75 female participants"* (**PMID:34871992**) — a 1:1.47 M:F ratio in that registry, which is more plausibly ascertainment/response bias than a true sex effect for an autosomal recessive disease. **Do not curate a sex predilection.** Sleep apnea, by contrast, *did* differ by sex (16.3% M vs 6.6% F), consistent with general OSA epidemiology.

Age distribution of prevalent cases: adults, with the bulk in the 3rd–6th decades given adult onset plus decades-long survival.

---

## 10. Diagnostics

### Diagnostic triad (GeneReviews NBK1262)

Diagnosis requires: **(1)** suggestive clinical findings, **(2)** muscle histopathology showing *"rimmed vacuoles, no inflammation,"* and **(3)** *"biallelic pathogenic variants in GNE identified by molecular genetic testing."*

### Laboratory tests

- **Serum creatine kinase** — normal to mildly/moderately elevated (**HP:0003236**). LOINC: CK, total, serum/plasma (**verify exact LOINC before curating**). Modest CK is itself discriminating: very high CK points toward dysferlinopathy instead.
- **Complete blood count with platelet count** — now explicitly recommended: *"Routine blood tests and evaluation of sleep-disordered breathing should be considered in order to better manage GNE myopathy patients."* (**PMID:34871992**)
- **Free sialic acid (serum)** — reduced ~18% vs age-matched controls; measurable by LC/MS/MS (**PMID:28267778**). **Important caveat: an 18% mean reduction with overlapping distributions is a group-level biochemical signature, not a diagnostic test.** Do not curate this as a clinical diagnostic assay.

### Biomarkers

There is no validated diagnostic or prognostic biomarker. The 2022 review states plainly that *"Sensitive and reliable biomarkers, and a disease-specific functional activity scale, have also been investigated"* (**PMID:35959526**) — i.e., still under investigation. Candidates:
- Plasma free Neu5Ac (pharmacodynamic, used as trial endpoint)
- Sarcolemmal sialylation on biopsy (pharmacodynamic; **PMID:34257421**)
- Total glycosphingolipid concentration — proposed: *"These data advocate for further exploring GSL concentrations as an informative biomarker, not only for GNE myopathy, but also for other disorders of sialic acid metabolism."* (**PMID:24136589**)
- Muscle MRI fat fraction — the most trial-sensitive measure currently (§12)

### Imaging

**Muscle MRI** is the workhorse. Pattern: high fat infiltration in adductor magnus, tibialis anterior, semitendinosus, semimembranosus; low in the quadriceps group (**PMID:34334416**). Quantitative **fat fraction** is emerging as the most sensitive progression measure — in the 6'-sialyllactose pilot it was the only endpoint reaching significance (§12).

### Functional and electrophysiological tests

- **EMG:** myopathic pattern (**HP:0003458**); no neurogenic features
- **Nerve conduction studies:** normal (useful for excluding neuropathic foot drop)
- **Pulmonary function (%FVC):** declines measurably, significantly so in non-ambulant patients over 1 year (**PMID:24656604**)
- **6-minute walk test:** only *"eight (33.3%) completed a standard 6-min walk test without assistance"* in a 24-patient cohort (**PMID:24656604**) — a floor-effect warning for anyone designing outcome measures
- **Hand-held dynamometry (UEC/LEC composites)** and **manual muscle testing** — the primary trial endpoints
- **ECG / echocardiography:** baseline recommended for surveillance, though cardiac involvement is not characteristic

### Biopsy / pathology

Rimmed vacuoles on modified Gomori trichome; fiber size variation; atrophic and angular fibers; **absence of inflammatory infiltrate**; congophilic inclusions immunoreactive to β-amyloid, ubiquitin, tau, and lysosomal proteins.

> "Histopathologic findings on muscle biopsies include fiber size variation, atrophic fibers, lack of inflammation, and the characteristic 'rimmed' vacuoles on modified Gomori trichome staining." (**PMID:30338442**)

Important qualifier — biopsy can be falsely reassuring: rimmed vacuoles are *"fairly typical in a suggestive context, but non-specific and inconsistent from one muscle to another."* (**PMID:26546927**)

### Genetic testing

- **Recommended approach:** targeted *GNE* sequencing when the clinical picture is classic (especially in a founder population); a neuromuscular/myopathy gene panel or WES otherwise; **WGS + long-read** when a panel returns single-heterozygous or negative results.
- **WGS/long-read is not optional in unsolved cases** — deep intronic variants and a 639 bp insertion were only found this way (**PMID:39332896**).
- **Single-gene testing:** high yield in founder populations.
- **Not applicable:** chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, repeat expansion testing. Curate these explicitly as N/A rather than omitting.
- **Deletion/duplication analysis:** warranted — a large *GNE* deletion has been reported (**PMID:12811782**, abstract not verified this session).

### Omics-based diagnostics

- **RNA-seq:** useful specifically for functional interpretation of the intronic/splice variants above (mechanistically indicated; no validated diagnostic protocol found)
- **Proteomics / epigenomics / liquid biopsy:** **not applicable / no evidence**

### Differential diagnosis

From GeneReviews (NBK1262), distinguished on CK level, inheritance pattern, and biopsy:

| Differential | Gene | Key discriminator |
|---|---|---|
| Miyoshi muscular dystrophy | *ANO5* | Posterior calf onset, very high CK |
| Dysferlinopathy / Miyoshi | *DYSF* | Very high CK, dysferlin absent on IHC |
| LGMD1D | *DNAJB6* | Autosomal dominant |
| Myotilinopathy | *MYOT* | Dominant; myofibrillar pathology |
| IBMPFD | *VCP* | Dominant; Paget disease + frontotemporal dementia |
| **Sporadic inclusion body myositis** | — | Late onset, *inflammation present*, quadriceps *involved* (the mirror image), no Mendelian inheritance |
| Charcot-Marie-Tooth (foot drop) | various | Neurogenic EMG/NCS |

### Screening

- **Carrier screening:** justified in founder populations (Persian/Middle Eastern Jewish, Japanese). Estimated worldwide carrier rate ~1:203 (GeneReviews).
- **Cascade testing:** standard for at-risk siblings of a proband. Note this identifies presymptomatic adults, which raises the usual counselling issues in a disease with no approved therapy in most jurisdictions.
- **Newborn screening:** **not applicable** — adult onset, no neonatal intervention.
- **Prenatal / PGT:** technically available for known biallelic genotypes.

---

## 11. Outcome / Prognosis

### Survival and mortality

**This is the most poorly documented domain.** I found **no** published 5-/10-year survival rate, life-expectancy estimate, or disease-specific mortality rate for GNE myopathy. GeneReviews describes advanced respiratory muscle involvement as *rare*, and cardiac involvement is not characteristic (no cardiac events in the 1-year Japanese cohort, **PMID:24656604**). The general clinical understanding is that life expectancy is not markedly shortened in most patients, but **this should be curated as an explicit knowledge gap, not asserted.** Do not import mortality figures from other distal myopathies.

### Morbidity and function

This is where the burden sits. Progressive loss of ambulation is the defining outcome:
> "GNE myopathy is an ultra-rare autosomal recessive disease, which starts as a distal muscle weakness and ultimately leads to a wheelchair bound state." — Pogoryelova et al. 2018, *Orphanet J Rare Dis* (**PMID:29720219**)

Wheelchair dependence typically 10–20 years after onset (GeneReviews). Quantified decline: −3.8 kg UE and −4.9 kg LE composite over 36 months (**PMID:33459658**).

### Complications

Loss of ambulation and its downstream sequelae; falls from foot drop; respiratory insufficiency in advanced disease; obstructive sleep apnea (16.3% M / 6.6% F); thrombocytopenia with bleeding tendency in the subset with the platelet phenotype.

### Recovery potential

**None.** No spontaneous or treatment-induced recovery has been described. The best any intervention has shown in humans is *slowed decline* (§12). Curate this honestly — the therapeutic literature's optimistic framing can mislead.

### Prognostic factors

- **Genotype:** c.620A>T (p.D207V) non-catalytic variant → milder course, later wheelchair use (**PMID:39332896**)
- **Ambulatory status at baseline:** stratifies both function and rate of change; GNEM-FAS scores were *"more severe at baseline in subjects who walked <200 meters versus ≥200 meters in 6 minutes"* (**PMID:33459658**)
- **Baseline "disease age"** from the Bayesian model: *"'Disease age,' the model-generated measure of disease progression, highly correlates with a variety of clinical, functional and patient-reported outcomes."* (**PMID:30511500**)
- **Prognostic biomarkers:** none validated.

---

## 12. Treatment

### Approved therapy — and the geography matters

**Japan, March 2024:** aceneuramic acid extended-release tablets (**Acenobel® ER 500 mg**, Nobelpharma) received manufacturing and marketing approval from the Japanese MHLW — **the first drug approved anywhere for GNE myopathy**. Confirmed by the 2025 review:

> "Several clinical trials targeting sialic acid biosynthetic pathways, such as oral N-acetylneuraminic acid, ManNAc, and 6'-sialyllactose, have advanced to late-stage development, culminating in the approval of the N-acetyl-neuraminic acid extended-release tablet in Japan in 2024." (**PMID:41082181**)

*(Brand name and specific March-2024 date come from the Tohoku University press release, not a peer-reviewed source — cite the review for the approval fact and treat the trade name as **UNVERIFIED** for evidence purposes.)*

**Everywhere else: no approved disease-modifying therapy.** Management is supportive.

### ⚠ The central pharmacological tension — curate this carefully

Sialic acid replacement **failed** its pivotal Western phase 3 and **succeeded, narrowly, in Japan**. Both results are real; do not present only one.

**Negative — Class I evidence (Ace-ER, international, n=89, NCT02377921):**
> "Change from baseline to week 48 for UEC score between treatments did not differ (least square mean [LSM] Ace-ER -2.25 kg vs placebo -2.99 kg; LSM difference confidence interval [CI] 0.74 [-1.61 to 3.09]; p = 0.5387)."

> "Ace-ER was not superior to placebo in improving muscle strength and function in patients with GNE myopathy."

> "CLASSIFICATION OF EVIDENCE: This study provides Class I evidence that for patients with GNE myopathy, Ace-ER does not improve muscle strength compared to placebo." — Lochmüller et al. 2019, *Neurology* (**PMID:31036580**)

**Positive-ish — Japanese phase II/III (SA-ER, n=20, 16:4 randomization):**
> "The mean value of change in UEC score (95% confidence interval [CI]) at 48 weeks was -0.1 kg (-2.1 to 2.0) in the SA-ER group and -5.1 kg (-10.4 to 0.3) in the placebo group. The least squares mean difference (95% CI) between the groups in the covariance analysis was 4.8 kg (-0.3 to 9.9; P = 0.0635). The change in UEC score at 48 weeks was significantly higher in the SA-ER group compared with the placebo group (P = 0.0013) in the generalized estimating equation test repeated measurement analysis." — Suzuki et al. 2023, *J Neuromuscul Dis* (**PMID:37125562**)

Note: the primary ANCOVA analysis was **p = 0.0635 — not significant**; significance came from a repeated-measures GEE analysis. A curator should record both numbers.

**Confirmatory Japanese phase III (NCT04671472, n=14):**
> "Decrease in least square mean (LSM) change in UEC score at Week 48 with SA-ER (- 0.115 kg) was numerically smaller as compared with placebo (- 2.625 kg), with LSM difference (95% confidence interval) of 2.510 (- 1.720 to 6.740) kg."

> "The present study reproducibly showed a trend towards slowing of loss of muscle strength and function with orally administered SA-ER, indicating supplementation with sialic acid might be a promising replacement therapy for GNE myopathy." — Mori-Yoshimura et al. 2023, *Orphanet J Rare Dis* (**PMID:37568154**)

The confidence interval crosses zero. "Trend" is the authors' own word — preserve it. An open-label extension followed (Suzuki et al. 2024, *JNNP*, **PMID:38839274**; 19 patients, 72 weeks, no major adverse effects — abstract is a short-format research letter with no structured abstract in PubMed, so quote from the full text if you need a snippet).

**Safety note worth curating:** one SA-ER-group patient found to be pregnant 2 weeks after starting drug had *"fetal death with tangled umbilical cord… at 13 weeks after the discontinuation of treatment"* (**PMID:37125562**). The authors report no other serious adverse events. Record it factually without implying causation.

### ManNAc (N-acetyl-D-mannosamine) — the upstream precursor

**CHEBI:63153.** Rationale: ManNAc enters the pathway *downstream* of the defective epimerase step, so it bypasses the block — and importantly it works even for kinase-domain mutants.

**Phase 1** (Xu et al. 2017, *Mol Genet Metab*, **PMID:28641925**):
> "Single doses of 3 and 6g of oral ManNAc were safe and well tolerated; 10g was associated with diarrhea likely due to unabsorbed ManNAc… Given that Neu5Ac is known to have a short half-life, the prolonged elevation of Neu5Ac after a single dose of ManNAc suggests that intracellular biosynthesis of sialic acid was restored in subjects with GNE myopathy, including those homozygous for mutations in the kinase domain."

**Phase 2 open-label** (Carrillo et al. 2021, *Genet Med*, **PMID:34257421**, NCT02346461, n=12):
> "Increased plasma Neu5Ac (+2,159 nmol/L, p < 0.0001) and sarcolemmal sialylation (p = 0.0090) were observed at day 90 compared to baseline. A slower rate of decline was observed for upper extremity strength (p = 0.0139), lower extremity strength (p = 0.0006), and the Adult Myopathy Assessment Tool (p = 0.0453), compared to natural history."

> "ManNAc showed long-term safety, biochemical efficacy consistent with the intended mechanism of action, and preliminary evidence clinical efficacy in patients with GNE myopathy."

The comparator was historical natural history, not placebo — a real limitation. **NCT04231266** (multi-centre, placebo-controlled phase 2) is **ACTIVE_NOT_RECRUITING** as of this session's ClinicalTrials.gov query.

### 6'-Sialyllactose (6SL) — South Korea

A milk oligosaccharide serving as a sialic acid source.

**Pilot PK + efficacy** (Park et al. 2023, *Biomed Pharmacother*, **PMID:37852099**, n=10 PK + 20 trial): *"6SL was well tolerated, except for self-limited gastrointestinal discomfort… In the high-dose group, proximal limb powers improved with daily 6SL."*

**Placebo-controlled pilot** (Park et al. 2025, *Mol Genet Metab*, **PMID:39644669**, n=11):
> "The fat fraction measured by MRI showed the most significant results in the posterior thigh. The increase in fat fraction, indicating muscle degeneration, was statistically significant between the two groups (p = 0.0004)."

> "Muscle strength, excluding hand grip power, did not show a significant difference between the two groups, which is attributed to the lack of pronounced muscle strength decline in both groups."

Also demonstrated target engagement: *"Resialylation of cell surface glycoconjugate was demonstrated in 6SL group by measuring lectin bindings on peripheral blood monocytes."* Note the pattern — **imaging endpoints are outperforming strength endpoints** in these small studies.

### Emerging / experimental

| Intervention | Stage | Identifier / citation |
|---|---|---|
| **UX016** — sialic acid-C16 prodrug, oral tablets | Phase 1/2 first-in-human, **NOT_YET_RECRUITING** | **NCT07511556** — *"A Phase 1/2, First-in-human, Double-blind, Placebo-controlled Study to Assess Dose, Safety, and Efficacy of UX016 (Sialic Acid-C16 Prodrug) in Adults With GNE Myopathy"* |
| **dbDNA GNE(wt)/bi-shRNA-GNE(M743T) lipoplex** — simultaneous WT replacement + mutant knockdown, IV, DOTAP-cholesterol delivery | Preclinical (mouse, rat) | Jay et al. 2026, *J Gene Med* (**PMID:42186366**): *"These results support further preclinical investigation to justify product IND development towards Phase 1 trial involving patients with GNE myopathy."* |
| **rAAV GNE gene therapy** (liver- or muscle-specific promoter) | Preclinical | Crowe et al. 2022 (**PMID:34511508**): *"Delivery of a single dose of GNE gene therapy using a recombinant Adeno Associated Virus (rAAV) vector with a liver-specific or a muscle-specific promoter both caused increased muscle Neu5Gc immunostaining that exceeded that seen with single dose monosaccharide therapy."* — plus the intriguing suggestion that *"liver expression of GNE may contribute overall muscle SA content"* |
| **Copanlisib** (FDA-approved PI3K inhibitor) — autophagy restoration via ULK1 | Preclinical, in vitro / organoid | Kim et al. 2026 (**PMID:41963465**): *"Functional validation in human pluripotent stem cell-derived neuromuscular organoids demonstrated that copanlisib reactivates autophagy via restoration of ULK1 activity."* |
| **Antioxidant therapy** | Under investigation | Named as an active strategy in **PMID:41082181** |
| **IVIG** (as an exogenous sialic acid source) | Historical phase 1 | **NCT00195637** (completed) |

### Supportive and rehabilitative care (the actual standard of care)

Per GeneReviews (NBK1262):
- **Ankle-foot orthoses** for foot drop; walking aids; wheelchair
- **Physical therapy** and **occupational therapy**
- **Baseline echocardiography and pulmonary function testing**, with annual multidisciplinary surveillance
- **Avoid myotoxic medications** and repetitive/overexertive activity
- **Screen for thrombocytopenia and sleep-disordered breathing** (**PMID:34871992**)
- **Genetic counselling** for the family

### Suggested NCIT terms (all verified against NCIT this session)

| Treatment | `treatment_term` | `therapeutic_agent` / notes |
|---|---|---|
| Aceneuramic acid ER (sialic acid) | **NCIT:C15986** Pharmacotherapy | **CHEBI:17012** N-acetylneuraminic acid (NCIT:C28188 "Sialic Acid" also exists but CHEBI is preferred per dismech convention); `therapeutic_modality: SMALL_MOLECULE` |
| ManNAc | **NCIT:C15986** Pharmacotherapy | **CHEBI:63153** N-acetyl-D-mannosamine; `SMALL_MOLECULE` |
| 6'-Sialyllactose | **NCIT:C15986** Pharmacotherapy | CHEBI ID for 6'-SL specifically **not confirmed** this session — look it up rather than guessing; `SMALL_MOLECULE` |
| GNE gene therapy (rAAV / lipoplex) | **NCIT:C15238** Gene Therapy | `therapeutic_modality: GENE_THERAPY` |
| Physical therapy | **NCIT:C15302** Physical Therapy | `BEHAVIORAL` |
| Occupational therapy | **NCIT:C121351** Occupational Therapy | `BEHAVIORAL` |
| Ankle-foot orthosis | *no reliable NCIT clinical-action term* — use free-text `preferred_term` | `therapeutic_modality: DEVICE` |
| Supportive care | **NCIT:C15747** Supportive Care | |
| Genetic counselling | **NCIT:C15240** Genetic Counseling | |

### Pharmacogenomics, surgery, immunotherapy, combination therapy, personalized medicine

- **Pharmacogenomics:** none established.
- **Surgery:** no disease-specific surgical intervention. Orthopaedic procedures (e.g. tendon transfer for foot drop) are conceivable but I found no GNE-specific evidence. **Do not curate speculatively.**
- **Immunotherapy:** not applicable — no immune mechanism.
- **Combination therapy:** none studied.
- **Genotype-guided treatment:** the one real signal is mechanistic — ManNAc bypasses the epimerase step and so should work for kinase-domain mutants, and the phase 1 data support this *"including those homozygous for mutations in the kinase domain"* (**PMID:28641925**). That's a genuine genotype-mechanism-therapy link worth curating.

---

## 13. Prevention

### Primary prevention

**Not available for the disease itself** — it is congenital in genotype. Prevention operates at the reproductive level:
- **Carrier screening** in founder populations (Persian/Middle Eastern Jewish, Japanese); worldwide carrier rate ~1:203 (GeneReviews)
- **Genetic counselling** (**NCIT:C15240**) — 25% recurrence risk per pregnancy for carrier couples
- **Preimplantation genetic testing** and **prenatal diagnosis** for known biallelic genotypes

There is a serious open question here: the mouse data show sialic acid metabolites given **prophylactically** *"completely prevented"* the myopathic phenotype (**PMID:19448634**), which raises the possibility of *presymptomatic* pharmacological prevention in identified biallelic carriers. That has not been tested in humans, and it's the single most interesting untried clinical question in the field. Curate as a `KNOWLEDGE_GAP` with proposed experiments.

### Secondary prevention

- **Cascade genetic testing** of at-risk relatives of probands
- Early diagnosis to avoid the diagnostic odyssey — the field's stated motivation: *"Now that therapies are under investigation, it is critical that a timely and accurate diagnosis is made in patients with GNE myopathy."* (**PMID:25002140**)

### Tertiary prevention (preventing complications)

- Falls prevention via AFOs and walking aids
- Respiratory surveillance (PFTs) and sleep-study evaluation for SAS
- CBC monitoring for thrombocytopenia; in the *GNE*-thrombocytopenia subgroup, **TPO-mimetic treatment may allow platelet transfusion to be avoided** (**PMID:36941763**)
- Avoidance of myotoxic drugs and overexertion
- Contracture prevention through PT

### Not applicable

**Immunization** (no infectious component), **public health / environmental interventions** (no environmental etiology), **population-based screening programs** beyond targeted carrier screening, and **prophylactic medication** (none exists).

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBITaxon | Gene | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *GNE* | 10020 |
| *Mus musculus* | NCBITaxon:10090 | *Gne* | 50798 |
| *Danio rerio* | NCBITaxon:7955 | *gne* | 393857 |
| *Rattus norvegicus* | NCBITaxon:10116 | *Gne* | present (ID not verified this session) |

### Naturally occurring disease in other species

**None found.** I searched and found no OMIA-registered naturally occurring GNE myopathy in companion animals, livestock, or wildlife. Unlike, say, ALS (which has a naturally occurring canine SOD1 model) or muscular dystrophy (golden retriever MD), GNE myopathy has **no natural animal counterpart** — every animal model is engineered (§15). Curate this as an explicit absence.

- **Breed (VBO):** not applicable
- **Veterinary relevance:** none
- **Zoonotic potential / cross-species transmission:** not applicable (genetic, non-transmissible)

### Comparative biology

The sialic acid pathway is deeply conserved, and one comparative difference is *methodologically* important: humans cannot synthesize **Neu5Gc** (N-glycolylneuraminic acid) because *CMAH* is inactivated in the human lineage, while mice can. Crowe et al. exploited exactly this by crossing onto a `Cmah-/-` background so that orally delivered Neu5Gc could be visualized as a tracer (**PMID:34511508**) — a clever bit of comparative-genomics-as-assay, and a reminder that mouse sialic acid biology is not identical to human.

*Gne* is essential in mouse — knockout is embryonic lethal (**PMID:17704511**) — establishing deep functional conservation of the pathway's necessity.

---

## 15. Model Organisms

### Mouse models — the workhorses, each with a distinct limitation

| Model | Genotype | Phenotype recapitulation | Key limitation | Citation |
|---|---|---|---|---|
| ***Gne* null** | `Gne-/-` | — | **Embryonic lethal**; no disease modelling possible | **PMID:17704511** |
| **DMRV-hIBM mouse** ⭐ | `Gne(-/-)hGNE D176V-Tg` (= p.D207V current nomenclature) | **Best overall.** Hyposialylation in serum, muscle, other organs; motor decline from 30 wk; β-amyloid deposition by 32 wk; rimmed vacuoles by 42 wk | Human transgene on null background (not a knock-in); long latency | **PMID:17704511** |
| **M712T knock-in** | `Gne(M712T/M712T)` | **FAILS_TO_RECAPITULATE the myopathy.** Dies by P3 with glomerular hematuria, proteinuria, podocytopathy — *"no myopathic features were apparent"* | Models a *renal* hyposialylation phenotype humans don't have. Genuine HUMAN_MODEL_MISMATCH | **PMID:17549255** |
| **M743T mouse** | `GneM743T/M743T` | Sialic acid biochemistry corroborates human findings | Used as a biochemical, not behavioural, model in the cited work | **PMID:28267778** |
| **Neu5Gc-tracer model** | `Cmah-/- GNED207VTgGne-/-` | Enables visualization of orally delivered Neu5Gc in muscle | Requires *Cmah* deletion, i.e. a humanized-sialic-acid background layered on the disease model | **PMID:34511508** |

The DMRV-hIBM mouse is the model that carried the field, and its authors say why:
> "These results show that the Gne(-/-)hGNED176V-Tg mouse mimics the clinical, histopathological and biochemical features of DMRV/hIBM, making it useful for understanding the pathomechanism of this myopathy and for employing different strategies for therapy." (**PMID:17704511**)

The M712T knock-in is the model that should be curated with a `FAILS_TO_RECAPITULATE` relationship against the myopathy nodes — it's a textbook case where the same human allele produces a completely different organ phenotype in mouse:
> "Homozygous mutant (Gne(M712T/M712T)) mice did not survive beyond P3. At P2, significantly decreased Gne-epimerase activity was observed in Gne(M712T/M712T) muscle, but no myopathic features were apparent. Rather, homozygous mutant mice had glomerular hematuria, proteinuria, and podocytopathy." (**PMID:17549255**)

That same paper delivers a `RESCUES` readout worth curating: *"ManNAc administration yielded survival beyond P3 in 43% of the Gne(M712T/M712T) pups. Survivors exhibited improved renal histology, increased sialylation of podocalyxin, and increased Gne/Mnk protein expression and Gne-epimerase activities."*

### Non-animal / cellular models (`experimental_models:`)

| Model | Type | Application | Citation |
|---|---|---|---|
| **hPSC-derived GNE myoblasts** (two independent lines) | iPSC-derived | Transcriptomic pathogenic signature; autophagy gene sets | **PMID:41963465** |
| **hPSC-derived neuromuscular organoids** | Organoid | Functional validation of copanlisib autophagy rescue | **PMID:41963465** |
| ***Gne*-knockout C2C12 myoblasts** | Immortalized cell line | Biochemical validation of AKT-mTORC1-ULK1 axis | **PMID:41963465** |
| **Patient fibroblasts** | Primary culture | Glycosphingolipid profiling; ManNAc rescue *in vitro* | **PMID:24136589** |
| **Control fibroblasts + iminosugar GNE-epimerase inhibitor** | Chemically induced | Phenocopy of GNE deficiency | **PMID:24136589** |
| **Sialuria patient fibroblasts + allele-specific siRNA** | Primary culture | Proof-of-concept for allele-specific silencing | **PMID:18653764** |

### Computational models

The **GNE Myopathy Disease Progression Model (GNE-DPM)** — a Bayesian latent-variable repeated-measures model built on prospective natural-history strength data (**PMID:30511500**), later used as a formal efficacy-analysis method in the ManNAc phase 2 (**PMID:34257421**, decreased progression γ = 0.61 at 12 months, γ = 0.55 at 18 months). Its stated value:
> "With the incorporation of a treatment effect parameter to the GNE Disease Progression Model, we describe a novel GNE Myopathy Disease Modification Analysis that significantly increases power and reduces the number of subjects required to test the effectiveness of novel therapies when compared to more traditional analysis methods."

That's a genuinely reusable pattern for any ultra-rare slowly-progressive disease and worth flagging in the dismech entry as a `computational_models:` record.

### Model limitations across the board

- **Long latency** — the DMRV-hIBM mouse takes 30–42 weeks to show phenotype, making preclinical screening slow and expensive
- **Species divergence in sialic acid biology** (Neu5Gc/*CMAH*)
- **No natural animal model** (§14)
- **Limited preclinical models** is named explicitly as a therapy-development bottleneck: *"developing therapies for GNE myopathy is complicated by several factors, including the rare incidence of disease, limited preclinical models, lack of reliable biomarkers, and slow disease progression."* (**PMID:30338442**)

### Resources

MGI (mouse), RGD (rat), ZFIN (zebrafish), Alliance of Genome Resources, IMSR, Cellosaurus (for C2C12 and patient-derived lines). No GNE-myopathy-specific model repository exists.

---

## Curation notes and flagged gaps

Things a curator should treat carefully when this becomes `kb/disorders/GNE_Myopathy.yaml`:

1. **Variant nomenclature.** Every pre-2014 paper uses NM_005476 numbering (−31 residues). Curate current numbering; note legacy names. The mouse literature will read as inconsistent otherwise.
2. **Two prevalence eras.** Clinical (1–9/million) and genomic (11–88/million) — record both as separate `Prevalence` records with distinct `notes`, not a blended average.
3. **The Ace-ER contradiction.** Class I negative internationally, marginal positive in Japan, approved in Japan. Model as competing evidence with honest `supports:` values, not as a settled efficacy claim.
4. **The M712T knock-in mouse** deserves `relationship: FAILS_TO_RECAPITULATE` with `limitations` and evidence — it is a substantive negative claim and the schema requires both.
5. **`MONDO:0958325` (thrombocytopenia 12 with or without myopathy)** overlaps this entity. Decide the modelling relationship explicitly rather than silently folding the platelet phenotype in.
6. **Quadriceps sparing** has no dedicated HP term. It needs a modelling decision — a `distinguishing_features` entry, a negated phenotype, or free text.
7. **Verified gaps** (record as `KNOWLEDGE_GAP` discussions, don't paper over): survival/mortality data; formal penetrance estimate; incidence; validated biomarker; the identity of the pathogenic hyposialylated target glycoprotein(s); why the pathology is muscle-restricted when the enzyme defect is systemic; whether presymptomatic sialic acid supplementation would prevent disease in humans; disease-specific QoL instrument data beyond GNEM-FAS.
8. **UNVERIFIED items** to re-check before curating: ICD-10/ICD-11 codes; the Acenobel® trade name and exact approval date; PMID:18723858 (mitochondrial processes) and PMID:12811782 (large deletion) abstracts; the complement-activation claim in *GNE*-thrombocytopenia; specific LOINC codes; a 6'-sialyllactose CHEBI ID; the rat *Gne* NCBI Gene ID.
9. **DR-hallucination discipline still applies.** Every PMID and quote above came from a live eutils fetch this session, but `just fetch-reference` + `just count-verified-snippets` are still required before any of it becomes an evidence item — my having read an abstract is not the same as the cache having it.

---

## Sources

**Primary literature (PubMed, verbatim abstracts retrieved this session):**
- [PMID:11528398](https://pubmed.ncbi.nlm.nih.gov/11528398/) — Eisenberg et al. 2001, *Nat Genet* — *GNE* identified
- [PMID:12177386](https://pubmed.ncbi.nlm.nih.gov/12177386/) — Tomimitsu et al. 2002, *Neurology* — DMRV novel mutations
- [PMID:17549255](https://pubmed.ncbi.nlm.nih.gov/17549255/) — Galeano et al. 2007, *J Clin Invest* — M712T knock-in mouse
- [PMID:17704511](https://pubmed.ncbi.nlm.nih.gov/17704511/) — Malicdan et al. 2007, *Hum Mol Genet* — DMRV-hIBM mouse
- [PMID:18653764](https://pubmed.ncbi.nlm.nih.gov/18653764/) — Klootwijk et al. 2008, *FASEB J* — sialuria allele-specific silencing
- [PMID:19448634](https://pubmed.ncbi.nlm.nih.gov/19448634/) — Malicdan et al. 2009, *Nat Med* — prophylactic sialic acid rescue
- [PMID:24136589](https://pubmed.ncbi.nlm.nih.gov/24136589/) — Patzel et al. 2014, *J Inherit Metab Dis* — glycosphingolipids
- [PMID:24656604](https://pubmed.ncbi.nlm.nih.gov/24656604/) — Mori-Yoshimura et al. 2014, *Neuromuscul Disord* — prospective natural history
- [PMID:24685570](https://pubmed.ncbi.nlm.nih.gov/24685570/) — Huizing et al. 2014, *Neuromuscul Disord* — nomenclature
- [PMID:25002140](https://pubmed.ncbi.nlm.nih.gov/25002140/) — Nishino, Carrillo-Carrasco & Argov 2015, *JNNP* — review
- [PMID:26546927](https://pubmed.ncbi.nlm.nih.gov/26546927/) — Urtizberea & Béhin 2015, *Med Sci (Paris)*
- [PMID:26980148](https://pubmed.ncbi.nlm.nih.gov/26980148/) — Chen et al. 2016, *Sci Rep* — GNE epimerase structure
- [PMID:27854221](https://pubmed.ncbi.nlm.nih.gov/27854221/) — Papadimas et al. 2016, *J Neuromuscul Dis* — atypical calf phenotype
- [PMID:28267778](https://pubmed.ncbi.nlm.nih.gov/28267778/) — Chan et al. 2017, *PLoS One* — free sialic acid quantification
- [PMID:28641925](https://pubmed.ncbi.nlm.nih.gov/28641925/) — Xu et al. 2017, *Mol Genet Metab* — ManNAc phase 1
- [PMID:29720219](https://pubmed.ncbi.nlm.nih.gov/29720219/) — Pogoryelova et al. 2018, *Orphanet J Rare Dis*
- [PMID:30338442](https://pubmed.ncbi.nlm.nih.gov/30338442/) — Carrillo, Malicdan & Huizing 2018, *Neurotherapeutics*
- [PMID:30511500](https://pubmed.ncbi.nlm.nih.gov/30511500/) — Quintana et al. 2019, *Stat Med* — Bayesian progression model
- [PMID:31036580](https://pubmed.ncbi.nlm.nih.gov/31036580/) — Lochmüller et al. 2019, *Neurology* — phase 3 Ace-ER
- [PMID:33250842](https://pubmed.ncbi.nlm.nih.gov/33250842/) — Chakravorty et al. 2020, *Front Neurol* — Indian cohort
- [PMID:33459658](https://pubmed.ncbi.nlm.nih.gov/33459658/) — Lochmüller et al. 2021, *J Neuromuscul Dis* — GNEM-DMP
- [PMID:34257421](https://pubmed.ncbi.nlm.nih.gov/34257421/) — Carrillo et al. 2021, *Genet Med* — ManNAc phase 2
- [PMID:34334416](https://pubmed.ncbi.nlm.nih.gov/34334416/) — Fatehi et al. 2021, *J Neuromuscul Dis* — muscle MRI
- [PMID:34511508](https://pubmed.ncbi.nlm.nih.gov/34511508/) — Crowe et al. 2022, *J Neuromuscul Dis* — dietary vs gene therapy
- [PMID:34871992](https://pubmed.ncbi.nlm.nih.gov/34871992/) — Yoshioka et al. 2022, *Clin Neurol Neurosurg* — extramuscular survey
- [PMID:35904705](https://pubmed.ncbi.nlm.nih.gov/35904705/) — Zhang, Shang & Miao 2022, *Neurol Sci* — amyloid β
- [PMID:35959526](https://pubmed.ncbi.nlm.nih.gov/35959526/) — Yoshioka, Nishino & Noguchi 2022, *Curr Opin Neurol*
- [PMID:36941763](https://pubmed.ncbi.nlm.nih.gov/36941763/) — Montcrieff et al. 2023, *Transfusion* — GNE thrombocytopenia
- [PMID:37125562](https://pubmed.ncbi.nlm.nih.gov/37125562/) — Suzuki et al. 2023, *J Neuromuscul Dis* — Japanese phase II/III
- [PMID:37568154](https://pubmed.ncbi.nlm.nih.gov/37568154/) — Mori-Yoshimura et al. 2023, *Orphanet J Rare Dis* — efficacy confirmation
- [PMID:37852099](https://pubmed.ncbi.nlm.nih.gov/37852099/) — Park et al. 2023, *Biomed Pharmacother* — 6SL pilot
- [PMID:38839274](https://pubmed.ncbi.nlm.nih.gov/38839274/) — Suzuki et al. 2024, *JNNP* — open-label extension
- [PMID:39332896](https://pubmed.ncbi.nlm.nih.gov/39332896/) — Jiao et al. 2024, *J Med Genet* — Chinese cohort
- [PMID:39644669](https://pubmed.ncbi.nlm.nih.gov/39644669/) — Park et al. 2025, *Mol Genet Metab* — 6SL placebo-controlled
- [PMID:40225917](https://pubmed.ncbi.nlm.nih.gov/40225917/) — Derksen et al. 2024, *Hum Mutat* — gnomAD prevalence
- [PMID:41082181](https://pubmed.ncbi.nlm.nih.gov/41082181/) — Yoshioka, Noguchi & Nishino 2025, *Ann Indian Acad Neurol*
- [PMID:41963465](https://pubmed.ncbi.nlm.nih.gov/41963465/) — Kim et al. 2026, *Exp Mol Med* — autophagy/AKT-mTORC1
- [PMID:42186366](https://pubmed.ncbi.nlm.nih.gov/42186366/) — Jay et al. 2026, *J Gene Med* — dbDNA lipoplex

**Databases and registries (queried live):**
- [GeneReviews: GNE Myopathy (NBK1262)](https://www.ncbi.nlm.nih.gov/books/NBK1262/)
- [MONDO:0011603 via EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0011603)
- [HPO annotations for OMIM:605820](https://ontology.jax.org/api/network/annotation/OMIM:605820)
- [HGNC:23657 (*GNE*)](https://rest.genenames.org/fetch/symbol/GNE)
- [ClinicalTrials.gov — GNE myopathy studies](https://clinicaltrials.gov/search?cond=GNE%20myopathy) (NCT02377921, NCT04671472, NCT02346461, NCT04231266, NCT07511556, NCT01784679, NCT04009226, NCT00195637)
- [Tohoku University press release — first approved drug for GNE myopathy (Aug 2024)](https://www.tohoku.ac.jp/en/press/aceneuramic_acid_is_the_first_approved_drug_for_gne_myopathy.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |

All extracted references resolved successfully.