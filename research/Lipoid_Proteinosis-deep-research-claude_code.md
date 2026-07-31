---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-29T15:55:15.696456'
end_time: '2026-07-29T16:00:18.947568'
duration_seconds: 303.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lipoid Proteinosis
  mondo_id: MONDO:0009530
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
  num_turns: 20
  total_cost_usd: 1.6744369999999997
  session_id: 5dd887df-f66e-565b-8209-dadd5bf74d40
  stop_reason: end_turn
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lipoid Proteinosis
- **MONDO ID:** MONDO:0009530 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lipoid Proteinosis** covering all of the
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

# Lipoid Proteinosis (Urbach-Wiethe Disease): Comprehensive Research Report

## 1. Disease Information

**Overview:** Lipoid proteinosis (LP), also known as Urbach-Wiethe disease, hyalinosis cutis et mucosae, or lipoglycoproteinosis, is a rare autosomal recessive genodermatosis first described by Erich Urbach and Camillo Wiethe in 1929. It is characterized by progressive deposition of amorphous hyaline-like material (a glycoprotein-lipid complex) in the skin, oral and laryngeal mucosa, and — in a subset of patients — the central nervous system, principally the amygdalae and hippocampi bilaterally. The disorder is clinically heterogeneous, chronic, and slowly progressive but generally compatible with a normal lifespan.

**Key identifiers:**
- **OMIM:** #247100 (LIPOID PROTEINOSIS OF URBACH AND WIETHE) [omim.org/entry/247100](https://omim.org/entry/247100)
- **Gene/locus OMIM:** ECM1, *602201*, chromosome 1q21.2
- **MONDO:** MONDO:0009530
- **ORPHA:** ORPHA:530
- **ICD-10:** E78.8 (other disorders of lipoprotein metabolism) — commonly cross-referenced in dermatology coding; Q82.8 is also used in some classification systems for the congenital genodermatosis grouping
- **MeSH:** D008065 (Lipoid Proteinosis of Urbach and Wiethe)
- **HPO:** HP:0001609 (Hoarse voice) is a core associated term; the disorder itself maps as a MONDO/OMIM disease entity
- **Suggested MONDO/HPO cross-reference:** the disease term should be bound to MONDO:0009530, with candidate phenotype terms drawn from HPO as below (Section 3)

**Common synonyms:** Urbach-Wiethe disease/syndrome; Hyalinosis cutis et mucosae; Lipoglycoproteinosis; Lipoidosis cutis et mucosae.

**Data provenance:** Information on LP is derived almost entirely from aggregated case-series and case-report literature (>400 reported cases worldwide as of recent reviews) rather than large-scale disease registries or population-level EHR studies, reflecting its extreme rarity. The largest single cohorts come from a South African (Namaqualand) founder population and more recently pooled Chinese case series (Advances in treatment for lipoid proteinosis: a case report and systematic review, PMID:38308656 — 25 studies/44 histopathologically confirmed patients).

Sources: [GeneReviews: Lipoid Proteinosis](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [OMIM 247100](https://omim.org/entry/247100), [StatPearls: Lipoid Proteinosis](https://www.ncbi.nlm.nih.gov/books/NBK568769/)

---

## 2. Etiology

**Disease causal factors:** LP is a monogenic Mendelian disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function pathogenic variants in **ECM1** (Extracellular Matrix Protein 1), first mapped to chromosome 1q21 and confirmed as the causal gene by Hamada et al., 2002 (PMID:11929856, "Lipoid proteinosis maps to 1q21 and is caused by mutations in the extracellular matrix protein 1 gene (ECM1)"). There is no known environmental, infectious, or purely mechanistic (non-genetic) cause.

**Genetic risk factors:**
- Biallelic ECM1 variants are necessary and sufficient to cause disease (fully penetrant autosomal recessive trait).
- **Consanguinity** substantially raises risk in an at-risk family given the rarity of the allele; multiple reported kindreds (Pakistani, Indian, Middle Eastern, South African) show consanguineous parents.
- **Founder variants** substantially raise local population prevalence:
  - **c.826C>T (p.Gln276Ter / Q276X)** — the founder mutation among South African (Namaqualand) patients, traced to a European (German) settler, Jacob Cloete (arrived Cape Colony 1652), with descendants migrating to Namaqualand by 1742 (Van Hougenhouck-Tulleken et al., "Clinical and molecular characterization of lipoid proteinosis in Namaqualand, South Africa," PMID:15327549).
  - **c.742G>T (p.Glu248Ter)** — reported as a recurrent variant in Pakistani families.
  - **c.658T>G (p.Cys220Gly)** — a major recurrent allele in Chinese patients (Journal of Translational Medicine, "Treatment of lipoid proteinosis due to the p.C220G mutation in ECM1, a major allele in Chinese patients").
- No genotype-phenotype correlation has been established; clinical severity varies substantially even among individuals homozygous for the same variant and within the same family (GeneReviews).

**Environmental risk factors:** None established as causal. LP is not associated with toxin exposure, radiation, occupational exposures, diet, or lifestyle factors — it is a purely genetic disorder of extracellular matrix protein function.

**Protective factors:** No genetic or environmental protective factors or modifier alleles have been described in the literature. Heterozygous carriers are generally asymptomatic, though some case reports note subtle findings (mild hoarseness in cold weather, slightly thickened lingual frenulum, firmer tongue) suggestive of very mild haploinsufficiency effects in obligate carriers — not a "protective" effect, but evidence of a gene-dosage relationship.

**Gene-environment interactions:** None reported; LP behaves as a pure single-gene, fully genetically-determined disorder without documented environmental modulation of expressivity, though secondary environmental triggers (upper respiratory infections, mechanical trauma to affected skin/mucosa) can precipitate acute local complications (parotitis, laryngeal crusting) rather than altering underlying disease risk.

Sources: [Hamada et al. 2002, PubMed](https://pubmed.ncbi.nlm.nih.gov/11929856/), [Namaqualand study, PubMed](https://pubmed.ncbi.nlm.nih.gov/15327549/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/)

---

## 3. Phenotypes

Onset is in **infancy** in nearly all cases, with the first sign almost universally being a **weak or hoarse cry** due to hyaline infiltration of the vocal cords. The disease course is chronic, fluctuating, and slowly progressive, typically stabilizing or partially regressing after adolescence for cutaneous lesions, while CNS calcifications tend to progress with disease duration.

### Mucocutaneous / laryngeal (nearly universal — clinical signs)
| Phenotype | Frequency | Notes | Candidate HPO term |
|---|---|---|---|
| Hoarse voice / dysphonia | Present in essentially all affected individuals; first manifestation in infancy | Due to hyaline deposition in vocal cords | HP:0001609 (Hoarse voice) |
| Vesicles/bullae and hemorrhagic crusting on face and extremities | Common in infancy/early childhood | Heal with "pock-like"/acneiform scarring | HP:0200034 (Vesiculobullous dermatitis) / HP:0100582 (Acneiform eruption, related) |
| Verrucous/keratotic lesions on extensor surfaces (elbows, knees, hands) | Common, appearing in later childhood | Progressive skin thickening, waxy yellow discoloration | HP:0000982 (Hyperkeratosis) |
| Moniliform blepharosis (beaded eyelid-margin papules) | ~50% of patients; considered pathognomonic when present | Along eyelid margins/inner canthi | HP:0000653 (relevant eyelid abnormality term) / consider a more specific descriptor term |
| Cobblestone/nodular oral mucosa, yellow lip nodules | Common | Mucosal hyaline deposition | HP:0000217 (Abnormal oral mucosa) related |
| Shortened, thickened lingual frenulum restricting tongue protrusion | Common | Distinctive clinical sign | HP:0000160 (Ankyloglossia)-adjacent |
| Diffuse skin thickening / infiltration | Progressive over time | Waxy/yellowish | HP:0031391 or general dermal infiltration term |
| Patchy alopecia | Reported subset | — | HP:0002293 (Alopecia) |
| Oligodontia / poor dental health, dental caries | Reported subset | — | HP:0000677 (Oligodontia) |

### Extracutaneous/CNS (variable, subset of patients)
| Phenotype | Frequency | Notes | Candidate HPO term |
|---|---|---|---|
| Bilateral amygdala ± hippocampal/striatal calcification | Considered pathognomonic radiologic finding; more prominent with longer disease duration | Bean/comma-shaped calcifications on CT | HP:0002514 (basal ganglia calcification)-adjacent; no exact amygdala-specific HPO term identified — flag as ontology gap |
| Temporal lobe epilepsy / seizures | Subset of patients | Managed with antiseizure medication (levetiracetam, carbamazepine reported effective) | HP:0002373 (Focal-onset seizure) / HP:0025319 (temporal lobe epilepsy, if extant) |
| Neuropsychiatric disturbance (memory impairment, paranoia, hallucinations, aggressive behavior, absence-of-fear phenotype) | Subset, correlates with amygdala calcification | Includes the well-studied "absence of fear" phenotype (see Patient SM, Section 6) | HP:0002354 (Memory impairment); HP:0000709 (psychosis); consider behavioral-phenotype terms |
| Migraine / headache | Frequently reported | — | HP:0002315 (Headache) |
| Depression / anxiety disorder | Frequently reported | — | HP:0000716 (Depressivity) / HP:0000739 (Anxiety) |
| Spontaneous CNS hemorrhage | Rare but reported | Serious complication | HP:0007256-adjacent (intracranial hemorrhage) |
| Recurrent parotitis | Subset | Due to ductal stenosis from hyaline deposition | HP:0100640 (Parotitis)-adjacent |
| Asymptomatic GI hyaline nodules | Subset (endoscopic finding) | Rarely causes hemorrhage | — |
| Xerostomia, epiphora/dry eyes | Subset | Lacrimal/salivary duct involvement | HP:0000633 (Dry eye) |

**Severity/progression:** Cutaneous manifestations tend to be most active in childhood/adolescence and can partially stabilize in adulthood; CNS calcification and associated neuropsychiatric/epileptic phenotypes tend to accumulate with age and disease duration. Course is described in the literature as "chronic and fluctuating."

**Quality of life impact:** No formal EQ-5D/SF-36 disease-specific studies were identified in the literature searched; qualitative impact is significant via disfigurement (facial/eyelid papules, skin scarring), voice impairment (social/occupational impact of chronic hoarseness), and, in the neuropsychiatric subgroup, cognitive/behavioral impairment affecting daily functioning. This is a documented gap area for structured QoL data.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [Neurology: Lipoid proteinosis with bilateral amygdalae calcifications](https://www.neurology.org/doi/10.1212/WNL.0b013e31829bfe1c), [AJNR case collection](https://www.ajnr.org/ajnr-case-collections-diagnosis/lipoid-proteinosis-bilateral-amygdalae-calcifications), [Brain imaging findings review, PMC12301744](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12301744/)

---

## 4. Genetic/Molecular Information

**Causal gene:** ECM1 (HGNC:3153; OMIM *602201*), chromosome 1q21.2, 10 exons, two major alternatively spliced transcripts (**ECM1a** and **ECM1b**, the latter lacking exon 7), both expressed in skin and upper respiratory tract.

**Variant classification/type:** Reported ECM1 pathogenic variants in LP are predominantly **loss-of-function** — nonsense, frameshift/small deletion, splice-site, and some missense variants distributed across multiple exons (notably exons 6, 7, and 8), consistent with a straightforward loss-of-function/haploinsufficiency-in-trans mechanism rather than a dominant-negative or gain-of-function mechanism. Whole-gene or whole-exon deletions have also been reported (detected by targeted deletion/duplication analysis when sequencing alone is uninformative).

**Notable/recurrent variants (population-specific):**
- **c.826C>T (p.Gln276Ter, "Q276X")** — South African/Namaqualand founder allele (all Namaqualand LP patients are homozygous for this variant per the founder-effect study).
- **c.742G>T (p.Glu248Ter)** — recurrent in Pakistani families.
- **c.658T>G (p.Cys220Gly, "C220G")** — major recurrent allele among Chinese LP patients (~treatment studies specifically target this variant).

**Allele frequency in population databases:** LP is exceedingly rare (>400 cases reported worldwide); ECM1 loss-of-function alleles are correspondingly rare in gnomAD population data (consistent with a fully penetrant recessive lethal-adjacent-severity phenotype maintained at low frequency except where founder effects operate). Specific gnomAD allele-frequency figures were not directly retrieved in this search pass and would need confirmation via direct gnomAD query for a knowledge-base entry.

**Somatic vs. germline:** LP is exclusively a germline/constitutional disorder; no somatic mosaicism or acquired-variant mechanism has been described.

**Functional consequence:** Loss of functional ECM1 protein (an ~85-kDa secreted glycoprotein) disrupts its normal roles as an extracellular matrix scaffolding/binding protein (see Section 6), leading to compensatory/aberrant deposition of hyaline material (thought to reflect altered collagen IV/V metabolism and accumulation of non-collagenous basement-membrane proteins) rather than direct accumulation of ECM1 itself.

**Modifier genes:** None have been identified; the marked intrafamilial phenotypic variability among individuals with identical genotypes (including within the same homozygous founder-variant population) strongly suggests unidentified genetic or stochastic modifiers, but none have been mapped.

**Epigenetic information:** No disease-specific DNA methylation, histone modification, or chromatin studies specific to LP/ECM1 were identified in this search — an open area.

**Chromosomal abnormalities:** LP is not associated with aneuploidy, translocations, or copy-number syndromes beyond the gene-level small deletions noted above; it is a single-gene disorder, not a contiguous gene/microdeletion syndrome.

**Suggested gene/ontology annotations:**
- Gene: ECM1, hgnc:3153
- GO biological process candidates: keratinocyte differentiation (GO:0030216), extracellular matrix organization (GO:0030198), basement membrane organization, angiogenesis regulation, ossification/endochondral bone development
- GO molecular function: structural molecule activity, extracellular matrix structural constituent, protein binding (specifically binding fibulin-1, fibulin-3, laminin-332 β3 chain, perlecan, collagen IV, MMP-9)

Sources: [Hamada et al. 2002](https://pubmed.ncbi.nlm.nih.gov/11929856/), [Chan et al., ECM1 mutations and genotype-phenotype correlation](https://pubmed.ncbi.nlm.nih.gov/12603844/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [ECM1 basement membrane protein of skin, PubMed](https://pubmed.ncbi.nlm.nih.gov/18200062/), [ECM1 interacts with fibulin-3/laminin 332, PubMed](https://pubmed.ncbi.nlm.nih.gov/19275936/)

---

## 5. Environmental Information

LP has **no known environmental, toxic, occupational, dietary, lifestyle, or infectious causal contribution**. It is a fully genetically determined Mendelian disorder. Environmental factors are relevant only as **secondary aggravating triggers** of established lesions rather than disease causes:
- Mechanical trauma/friction can exacerbate skin blistering and scarring in affected infants and children.
- Upper respiratory infections are more frequent in affected individuals (likely secondary to structural mucosal/laryngeal changes) and can precipitate airway compromise.
- Cold weather has been anecdotally reported to worsen hoarseness even in heterozygous carriers.

No infectious agent is implicated in pathogenesis (the disorder is not communicable), and no lifestyle modification is known to alter disease risk or course beyond general supportive/preventive care (see Sections 12–13).

Sources: [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/)

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function ECM1 variants → absent or non-functional ECM1 glycoprotein (85 kDa, secreted).
2. **Protein structure/function loss:** ECM1a comprises an N-terminal α-helical domain (αD1) and three serum albumin subdomain-like domains (SASDL2–4). SASDL2/3 normally bind collagen IV, laminin-332 (β3 chain), fibronectin, perlecan, fibulin-1 (isoforms 1C/1D), fibulin-3, and matrix metalloproteinase-9 (MMP-9) — ECM1 functions as a multifunctional scaffolding/binding hub stabilizing the dermal-epidermal basement membrane and regulating keratinocyte proliferation/differentiation.
3. **Cellular consequence:** Loss of ECM1's basement-membrane scaffolding and MMP-9-regulatory function disrupts normal collagen IV processing and basement-membrane architecture, and alters keratinocyte differentiation programs; there is increased production of collagen type V and altered collagen IV metabolism, and defective ECM1 likely generates aberrant protein binding to basement-membrane macromolecules.
4. **Tissue-level consequence:** Progressive **reduplication of the dermal-epidermal basement membrane** and **hyalinization** — widespread deposition of PAS-positive, diastase-resistant, glycoprotein-lipid hyaline material in the papillary dermis, around dermal blood vessels, and around skin appendages, with loss of the normal capillary loop network.
5. **Organ-level/clinical manifestation:** Hyaline deposition in the vocal cords → hoarseness; in skin → verrucous/keratotic thickening and blistering-then-scarring; in oral/lacrimal/salivary structures → mucosal nodularity, xerostomia, epiphora, recurrent parotitis; in the CNS → bilateral amygdala/hippocampal/striatal calcification (mechanism of CNS calcification specifically is less well characterized biochemically than the dermal hyalinization, representing an area of relative mechanistic uncertainty) → temporal lobe epilepsy, memory impairment, and behavioral/emotional dysregulation, most famously the **"absence of fear"** phenotype described in Patient S.M., a woman with complete bilateral amygdala destruction from LP who fails to show fear responses to live snakes/spiders, horror films, and haunted houses, yet — notably — retains the capacity for CO₂-inhalation-induced panic (Feinstein et al.), demonstrating that externally-triggered fear (amygdala-dependent) and internally-triggered panic (via interoceptive/chemoreceptive pathways) are dissociable.

**Molecular pathways:** No single canonical signaling cascade (e.g., Wnt/MAPK/mTOR) has been implicated; the mechanism is primarily one of **structural extracellular-matrix/basement-membrane protein dysfunction** rather than intracellular signal transduction.

**Cellular processes:** Altered keratinocyte proliferation/differentiation; disrupted basement-membrane assembly; secondary microvascular changes (capillary loop loss, vessel-wall reduplication).

**Protein dysfunction type:** Loss of function (absent/non-functional secreted glycoprotein) — not aggregation/misfolding of the ECM1 protein itself; the "hyaline material" that accumulates is thought to be predominantly composed of excess/misprocessed basement-membrane components (collagen IV, other non-collagenous glycoproteins) rather than aggregated ECM1.

**Biochemical abnormalities:** Altered collagen type IV metabolic processing; increased collagen type V production; disrupted MMP-9 regulation (ECM1 normally inhibits MMP-9 activity, so its loss may dysregulate local matrix turnover).

**Tissue damage mechanisms:** Progressive fibrohyaline deposition and basement-membrane reduplication (not primarily oxidative-stress- or ischemia-driven); mechanical/structural compromise of the vocal cords and skin.

**Immune system involvement:** Not a primary autoimmune or immunodeficiency disorder; recurrent parotitis and respiratory infections are secondary to structural/ductal obstruction rather than primary immune dysfunction.

**Model systems:** No viable mouse knockout model exists — constitutive Ecm1 knockout in mice causes **embryonic lethality**, and the reason for this human-mouse phenotypic discordance is unknown (a notable human-model mismatch relevant to any `HUMAN_MODEL_MISMATCH` knowledge-gap curation). A **zebrafish ECM1 knockdown model** has been used instead and reproduces developmental pathologies, proposed as a more tractable system for future therapeutic testing.

**Suggested ontology terms:**
- GO cellular component: basement membrane, extracellular matrix, extracellular region
- GO biological process: extracellular matrix organization (GO:0030198), keratinocyte differentiation (GO:0030216), basement membrane organization, positive/negative regulation of MMP-9 activity
- CL cell types: keratinocyte (CL:0000312), fibroblast (dermal), vascular endothelial cell
- UBERON: skin epidermis, dermis, basement membrane, larynx/vocal cord, amygdala, hippocampus

Sources: [ECM1 in human skin, PubMed](https://pubmed.ncbi.nlm.nih.gov/14723723/), [ECM1 basement membrane protein of skin, PubMed](https://pubmed.ncbi.nlm.nih.gov/18200062/), [ECM1 interacts with fibulin-3/laminin 332, PubMed](https://pubmed.ncbi.nlm.nih.gov/19275936/), [Ultrastructural aspects of skin in LP, PMC8790196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8790196/), [S.M. patient — Wikipedia summary of Feinstein et al. research](https://en.wikipedia.org/wiki/S.M._(patient)), [Feinstein — Living Without an Amygdala](https://shackmanlab.org/wp-content/uploads/2024/03/Feinstein_PatientSMChapter2016.pdf), [J Neurosci — Panic Anxiety in Humans with Bilateral Amygdala Lesions](https://www.jneurosci.org/content/36/12/3559), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin (epidermis/dermis), oral mucosa, larynx/vocal cords, upper respiratory tract mucosa.
- **Secondary:** Eyelids (moniliform blepharosis), lacrimal apparatus (epiphora/dry eyes), salivary glands/parotid ducts (recurrent parotitis, xerostomia), tongue/lingual frenulum, teeth, gastrointestinal tract (asymptomatic nodules, rare hemorrhage), central nervous system (amygdala, hippocampus, parahippocampal gyrus, striatum/basal ganglia).
- **Body systems involved:** Integumentary, respiratory (upper airway), nervous (CNS), and to a lesser extent gastrointestinal and exocrine glandular systems.

**Tissue and cell level:**
- Epidermal keratinocytes (hyperkeratosis, altered differentiation).
- Dermal fibroblasts and perivascular connective tissue (site of hyaline deposition).
- Dermal microvascular endothelium (basement-membrane reduplication, capillary loop loss).
- Neurons/glia of the amygdala and hippocampus (site of calcification, though the specific cell population driving calcification is not well characterized).

**Subcellular level:** Primarily extracellular (basement membrane, extracellular matrix) rather than intracellular organelle pathology; GO cellular component annotation should emphasize basement membrane / extracellular matrix rather than mitochondria, ER, or lysosome.

**Localization:** Skin lesions favor extensor surfaces (elbows, knees, hands), face, and eyelid margins; typically bilateral/symmetric. CNS calcifications are classically **bilateral and symmetric** in the amygdala/medial temporal lobe — a described pathognomonic radiologic pattern.

Suggested UBERON terms: UBERON:0001003 (skin epidermis), UBERON:0002067 (dermis), UBERON:0001737 (larynx), UBERON:0001876 (amygdala), UBERON:0002421 (hippocampal formation), UBERON:0002435 (striatum).

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [AJNR: Lipoid Proteinosis Bilateral Amygdalae Calcifications](https://www.ajnr.org/ajnr-case-collections-diagnosis/lipoid-proteinosis-bilateral-amygdalae-calcifications), [Radiologic presentation with symmetrical medial temporal lobe calcifications, PMC4921162](https://pmc.ncbi.nlm.nih.gov/articles/PMC4921162/)

---

## 8. Temporal Development

**Onset:** Congenital/early infantile — the hoarse cry is typically noted from birth or the first months of life; skin manifestations (vesicles/bullae) generally appear in infancy to early childhood. Onset pattern is **insidious/chronic** rather than acute.

**Progression:**
- Cutaneous disease tends to be most active during infancy/childhood (recurrent vesiculobullous eruptions with scarring), evolving into more stable verrucous/keratotic thickening by adolescence/adulthood.
- CNS calcification is **progressive with disease duration** — the AJNR/Neurology literature specifically notes amygdala calcification "more prominent with a longer duration of the disease," implying it accumulates across the lifespan rather than being fixed at onset.
- No formal staging system (analogous to AJCC cancer staging) exists for LP; disease description relies on qualitative "early/established/late" clinical pattern in case reports.

**Disease course pattern:** Chronic and fluctuating overall; individual manifestations (skin vesicles, seizures) can be episodic/relapsing, while structural changes (scarring, calcification) are cumulative and largely irreversible.

**Duration:** Chronic, lifelong; disease is generally **compatible with a normal lifespan** except in cases of laryngeal airway obstruction or CNS hemorrhage.

**Remission patterns:** No spontaneous full remission described; some improvement of active cutaneous lesions (blistering) can occur with age or treatment (see Section 12), but structural/scarring and CNS changes do not reverse.

**Critical periods:** Infancy represents a critical period for early recognition (weak cry) and airway monitoring; childhood/adolescence is the critical window for active skin-lesion management before scarring consolidates.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [Neurology 2013](https://www.neurology.org/doi/10.1212/WNL.0b013e31829bfe1c)

---

## 9. Inheritance and Population

**Epidemiology:** Precise incidence/prevalence figures are not established; **more than 400 cases** (ages 6–67 years in early series, since expanded) have been documented worldwide in the literature. This makes LP an ultra-rare disease by any standard classification (well below 1/1,000,000).

**Inheritance pattern:** **Autosomal recessive.** For two heterozygous (carrier) parents: 25% chance of an affected (biallelic) child, 50% chance of an asymptomatic carrier, 25% chance of a non-carrier — standard AR Punnett-square recurrence risk.

**Penetrance:** Complete/full penetrance for the biallelic genotype (all reported biallelic ECM1 variant carriers manifest disease, albeit with variable severity).

**Expressivity:** Markedly **variable expressivity** — clinical heterogeneity is prominent even within families sharing the identical genotype, and no genotype-phenotype correlation has been established.

**Genetic anticipation:** Not reported/applicable (LP is not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed.

**Founder effects:** Well-documented — the South African/Namaqualand population (Q276X, traced to European settler ancestry from the 1650s–1740s) and additional founder-type recurrent alleles in Pakistani (p.Glu248Ter) and Chinese (p.Cys220Gly) populations.

**Consanguinity role:** Substantially elevates risk in affected kindreds; many reported cases (Pakistani, South Asian, Middle Eastern families) arise in consanguineous unions given the rarity of the pathogenic allele in the general population.

**Carrier frequency:** Not precisely quantified in general populations; locally elevated in founder populations (e.g., Namaqualand, South Africa) due to the founder effect and reported consanguinity/community endogamy.

**Population demographics:**
- **Affected populations:** Reported worldwide across many ethnicities; the largest documented cluster is in the **Namaqualand region, Northern Cape Province, South Africa**, in a population of mixed Khoisan and European (Afrikaner) ancestry with a well-characterized founder effect. Substantial case series also exist from China, India/Pakistan, and various European cohorts (disproportionately of Dutch/German ancestry historically).
- **Geographic distribution:** Global, but regionally concentrated in founder populations as above.
- **Sex ratio:** Approximately **equal** — males and females affected equally, consistent with autosomal (non-X-linked) recessive inheritance.
- **Age distribution:** Presents from infancy; documented cases in the literature span roughly ages 6–67+ years, i.e., diagnosed and followed from childhood through late adulthood.

Sources: [Van Hougenhouck-Tulleken et al., PubMed](https://pubmed.ncbi.nlm.nih.gov/15327549/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [NCBI Bookshelf — Genetic Disorders Associated with Founder Variants Common in the Afrikaner Population](https://www.ncbi.nlm.nih.gov/books/NBK583036/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/)

---

## 10. Diagnostics

**Diagnostic criteria:** Diagnosis is established in a proband with characteristic clinical findings **plus either** (a) biallelic ECM1 pathogenic variants on molecular genetic testing, **or** (b) characteristic histologic/immunolabeling findings on skin biopsy.

**Clinical/laboratory tests:**
- **Skin biopsy (histopathology):** Hyperkeratosis; PAS-positive, diastase-resistant, thickened basement membrane around dermal vessels and skin appendages; focal hyaline deposition in the papillary dermis and at the dermal-epidermal junction; microvascular wall reduplication and loss of the normal capillary loop network.
- **Immunolabeling:** Reduced/absent ECM1 protein expression on skin biopsy — particularly useful early in disease when classic histology may be less developed.
- **No specific blood biomarker or enzyme assay** exists for LP (it is not a metabolic/enzymatic disorder in the classical biochemical sense, despite the "lipoid" name referring to the histochemical lipid-staining property of the hyaline deposits rather than a lipid-metabolism defect).

**Imaging studies:**
- **CT/MRI brain:** Bilateral, symmetric, bean/comma-shaped calcifications in the medial temporal lobes (amygdala ± hippocampus, parahippocampal gyrus, striatum) — considered a **pathognomonic radiologic hallmark**, more prominent with longer disease duration. CT is generally more sensitive than MRI for detecting calcification.

**Functional/other tests:** Laryngoscopy for direct visualization of vocal-cord hyaline deposits and airway assessment; EEG for suspected temporal lobe epilepsy; neuropsychiatric/cognitive testing for the CNS-involved subgroup.

**Genetic testing approach:**
- **Single-gene sequencing of ECM1** detects the pathogenic variant in the great majority of cases (GeneReviews cites detection of >99% of variants by combined sequencing/deletion-duplication approaches).
- **Gene-targeted deletion/duplication analysis** for exon-level or whole-gene deletions missed by sequencing alone.
- **Multigene panels** (genodermatosis panels) and **exome/genome sequencing** are alternative comprehensive approaches, particularly when the phenotype is atypical or a single-gene test is uninformative.
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not applicable** — LP is a single-gene point-mutation/small-indel disorder, not a copy-number or repeat-expansion syndrome.

**Omics-based diagnostics:** Not part of routine LP diagnosis; no established transcriptomic, proteomic, metabolomic, or liquid-biopsy diagnostic assay is in clinical use for this disorder.

**Differential diagnosis:**
| Condition | Distinguishing features |
|---|---|
| Pseudoxanthoma elasticum (ABCC6) | Subretinal neovascularization/visual impairment; lacks moniliform blepharosis and infantile hoarseness |
| Erythropoietic protoporphyria (FECH), autosomal recessive form | Hepatic dysfunction common; photosensitivity; no hoarseness/blepharosis |
| Herpes simplex, impetigo (cutaneous lesions) | Infectious course, different histology |
| Epidermolysis bullosa | Different blistering mechanism/histology |
| Systemic amyloidosis / lichen myxedematosus / scleromyxedema | Different deposit composition on special stains |
| Leprosy | Infectious, nerve involvement |
| Fahr disease, calcified glioma, Raine syndrome, prior herpes encephalitis (for CNS calcification) | Different calcification pattern/distribution and clinical context |
| Systemic amyloidosis, hypothyroidism/myxedema, acromegaly (for macroglossia) | Different systemic biochemical findings |

**Screening:** No population-based newborn screening or carrier-screening program exists for LP given its rarity; carrier testing, prenatal testing, and preimplantation genetic testing are available on a **targeted family/at-risk basis** once the familial ECM1 variant(s) are known, rather than as a public-health screening initiative.

Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [AJNR](https://www.ajnr.org/ajnr-case-collections-diagnosis/lipoid-proteinosis-bilateral-amygdalae-calcifications)

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal 5-/10-year survival statistics exist (data are insufficiently powered given rarity), but the consistent qualitative statement across GeneReviews and StatPearls is that LP has a **"benign, slowly progressive course...generally compatible with a normal lifespan."** Mortality risk, when it occurs, relates to specific complications rather than the underlying hyalinosis process itself.

**Morbidity/complications:**
- **Airway obstruction/respiratory compromise** from laryngeal hyaline deposition — the most acutely dangerous complication, occasionally requiring tracheostomy.
- **Seizures** (temporal lobe epilepsy), generally manageable with antiseizure medication.
- **Spontaneous intracranial hemorrhage** — rare but reported, serious.
- **Gastrointestinal hemorrhage** — rare, from mucosal nodules.
- **Neuropsychiatric morbidity** — memory impairment, mood/anxiety disorders, and (in the amygdala-calcification subgroup) behavioral changes including the striking "absence of fear" phenotype; these can meaningfully affect functional/occupational outcomes though they are not directly life-threatening.
- **Cosmetic/psychosocial morbidity** from visible facial/eyelid lesions and chronic voice change.
- **Procedural/surgical complications:** bleeding, infection, and recurrent scarring/granulation tissue after laser or surgical intervention.

**Quality of life:** No disease-specific validated QoL instrument results were identified; morbidity is driven by visible dermatologic disfigurement, voice change, and (in a subset) neuropsychiatric/epileptic burden.

**Prognostic factors:** Presence and duration of CNS (amygdala) calcification correlates with more prominent neuropsychiatric/epileptic manifestations; laryngeal involvement severity predicts airway risk. No validated biomarker-based prognostic score exists.

Sources: [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/)

---

## 12. Treatment

**No curative therapy exists; no FDA-approved treatment; no randomized controlled trials have established a standard of care.** Management is multidisciplinary and manifestation-directed.

**Pharmacotherapy:**
- **Systemic retinoids — acitretin** (~0.5 mg/kg/day), used off-label, is the most frequently reported and comparatively best-evidenced pharmacologic option. Efficacy is **more consistent for mucosal/laryngeal symptoms (voice improvement) than for established cutaneous lesions**, with variable individual response (case reports of major improvement in moniliform blepharosis and skin thickening within 3–6 months in some patients; minimal skin response despite voice improvement in others) (PMC3505959; Luo et al., *J Dermatol* 2016, treating the Chinese C220G founder variant). A 2024 systematic review (PMID:38308656) pooling 25 studies/44 histopathologically confirmed patients supports low-dose oral acitretin as having a favorable risk/benefit profile relative to alternatives.
- **Dimethyl sulfoxide (DMSO)** — historically reported, limited/anecdotal evidence.
- **D-penicillamine** — historically reported (proposed to affect collagen cross-linking), limited evidence.
- **Short-course systemic corticosteroids** — for acute vesiculobullous flares.
- **Antiepileptic medications** — for seizure control (carbamazepine, levetiracetam reported effective in individual cases, e.g., levetiracetam 500 mg BID with good seizure-frequency reduction).
- **Antipsychotics** — for behavioral/psychotic manifestations in the neuropsychiatric subgroup.

**Advanced/molecularly targeted therapeutics:** None specific to ECM1/LP have reached clinical development (no gene therapy, RNA-based therapy, or targeted biologic identified in the literature reviewed); this remains an area of unmet therapeutic need, with the zebrafish knockdown model proposed as a future preclinical testing platform.

**Surgical/interventional:**
- **Microlaryngoscopic excision** of vocal-cord hyaline deposits; **CO₂ laser** ablation for laryngeal lesions.
- **Tracheostomy** for severe/refractory airway obstruction.
- **Cosmetic procedures:** CO₂ laser ablation, dermabrasion, cryotherapy, blepharoplasty for eyelid papules and facial scarring; newer approaches include microwave treatment and plasma exeresis.
- **Risk:** postoperative granulation tissue formation and recurrent fibrosis, sometimes necessitating repeat procedures.

**Supportive/rehabilitative care:** Speech therapy/voice support for chronic hoarseness; dental care for oligodontia/caries; ophthalmologic care for dry eye/epiphora; psychiatric/psychological support and neuropsychological follow-up for the CNS-involved subgroup.

**Treatment outcomes/algorithm:** No formal clinical treatment algorithm or NCCN-style guideline exists; management is individualized and consensus-based, drawing on the interdisciplinary team (dermatology, otolaryngology, neurology, psychiatry, dentistry, medical genetics) recommended by StatPearls and GeneReviews. Suggested **surveillance schedule** per GeneReviews: otolaryngologic (airway/vocal cord) assessment every 6 months, dermatologic exam every 6 months, annual neurologic and neuropsychiatric evaluation.

**Suggested MAXO terms:** MAXO:0000647 (chemotherapy — not applicable here), more relevantly MAXO:0000011 (physical therapy, for speech/rehab support), MAXO:0000004 (surgical procedure, for laryngeal/cosmetic procedures), MAXO:0000079 (genetic counseling), NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI:41879 (acitretin) or the appropriate CHEBI/NCIT identifier.

Sources: [Acitretin Treatment for Lipoid Proteinosis, PMC3505959](https://pmc.ncbi.nlm.nih.gov/articles/PMC3505959/), [Advances in treatment for LP: case report and systematic review, PMID:38308656](https://pubmed.ncbi.nlm.nih.gov/38308656/), [Luo et al. 2016, acitretin in Chinese C220G patients](https://onlinelibrary.wiley.com/doi/abs/10.1111/1346-8138.13261), [Treatment of LP due to p.C220G, Journal of Translational Medicine](https://link.springer.com/article/10.1186/1479-5876-12-85), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/)

---

## 13. Prevention

**Primary prevention:** No population-level primary prevention exists (no vaccination, no modifiable environmental risk factor); the only "primary prevention" concept applicable is **avoidance of consanguineous unions** in populations with known elevated carrier frequency, and **genetic counseling** for at-risk couples (both known heterozygous carriers, or from a founder population/consanguineous background).

**Secondary prevention (early detection):** No formal population screening program; early clinical recognition of the infantile hoarse cry, and prompt genetic/histologic confirmation, allows earlier initiation of surveillance (airway monitoring) before serious complications (airway obstruction) develop.

**Tertiary prevention:** Structured multidisciplinary surveillance (per Section 12 schedule) to catch and manage airway compromise, seizures, and neuropsychiatric decline before they become severe; early treatment of active cutaneous flares may reduce scarring burden.

**Genetic screening/counseling:**
- **Carrier testing** of at-risk relatives once the familial ECM1 variant(s) are known.
- **Prenatal testing** and **preimplantation genetic testing** are available options for at-risk pregnancies in known carrier couples.
- Genetic counseling should specifically address the **25%/50%/25%** recurrence-risk pattern for future pregnancies of two carrier parents, and the elevated a priori risk in founder populations (e.g., Namaqualand) or consanguineous unions.

**Risk stratification:** Not formally validated at a population level beyond family history/consanguinity/founder-population ancestry as risk indicators.

**Public health/environmental interventions:** Not applicable — LP is not modifiable by sanitation, vector control, or environmental-exposure reduction.

**Prophylaxis:** No pharmacologic prophylaxis exists to prevent onset in a genetically affected individual; management is entirely reactive/surveillance-based once the diagnosis is established or anticipated from family history.

Sources: [GeneReviews — Genetic Counseling section](https://www.ncbi.nlm.nih.gov/books/NBK338540/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK568769/)

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring lipoid proteinosis analog in non-human species (companion animals, livestock, or wildlife) was identified in the literature searched — this appears to be a human-specific disease entity as currently documented (NCBITaxon:9606, Homo sapiens, is the only affected taxon reported).

**Breed:** Not applicable (no veterinary VBO breed association identified).

**Orthologous gene:** ECM1 is broadly conserved across vertebrates (mouse *Ecm1*, zebrafish *ecm1* orthologs exist and have been experimentally manipulated — see Section 15), but no spontaneous/natural disease phenotype analogous to human LP has been reported in these species; the mouse ortholog's constitutive loss instead causes **embryonic lethality**, a striking human-mouse phenotypic discordance.

**Comparative biology:** The human-mouse discordance (viable, non-lethal, tissue-restricted hyalinosis phenotype in humans vs. embryonic lethality in mice) is itself a notable comparative-biology finding suggesting either species-specific compensatory mechanisms or differences in ECM1 developmental requirements between mouse and human, and represents an unresolved question in the field.

**Transmission:** Not applicable — LP is a non-communicable, purely genetic disorder with no zoonotic potential or cross-species susceptibility relevant to transmission.

Sources: [Search results on Ecm1 knockout mouse model / zebrafish knockdown](citations above), [OMIA](http://omia.org) not directly queried but no reported entries for this phenotype were surfaced in this search.

---

## 15. Model Organisms

**Model types available:**
- **Mammalian (mouse):** Constitutive *Ecm1* knockout is **embryonic lethal** — there is **no viable mouse model** that recapitulates the human LP phenotype. This is an important and explicit human-model mismatch: the reason for the mouse/human phenotypic disparity is unknown, and no conditional/tissue-specific knockout recapitulating the postnatal skin/CNS phenotype was identified in this search.
- **Zebrafish:** *ecm1* knockdown (morpholino-based, per the searched literature) produces evident developmental pathologies and has been proposed as a **more suitable model system for testing future therapies**, given the failure of the mouse knockout approach. Specific phenotypic recapitulation details (which human LP features are/are not reproduced) were not fully retrievable in this search pass and would benefit from direct primary-literature follow-up (search terms to pursue further: "ecm1 morpholino zebrafish skin phenotype").
- **Cellular/in vitro models:** Patient-derived skin fibroblast and keratinocyte cultures have been used in mechanistic studies of ECM1 protein-protein interactions (e.g., co-immunoprecipitation studies establishing ECM1-fibulin-3 and ECM1-laminin-332 binding), though these are not "disease models" per se but rather protein-interaction/functional-validation systems.
- **Induced models:** No CRISPR-edited iPSC-derived organoid model specific to LP was identified in this search.

**Model characteristics:**
- **Phenotype recapitulation:** Poor in mouse (lethal, non-recapitulating); the zebrafish model recapitulates general developmental pathology from *ecm1* loss but its fidelity to the specific adult human dermal-hyalinosis and CNS-calcification phenotype is not established — flagging this as a candidate `HUMAN_MODEL_MISMATCH` for any dismech curation, since translational validity of the zebrafish findings to human disease biology remains an open question.
- **Model limitations:** No model captures the chronic, slowly progressive, tissue-restricted (skin/mucosa/CNS) adult phenotype seen in humans; the CNS-specific (amygdala/hippocampal calcification) component in particular has no established animal correlate.

**Applications:** Zebrafish knockdown is proposed for future **therapeutic screening** given the absence of a mammalian genetic model; patient fibroblast/keratinocyte culture systems support **mechanistic protein-interaction studies** (ECM1-basement membrane protein binding).

**Resources:** No dedicated LP-specific model-organism database or repository was identified; general resources (MGI for mouse, ZFIN for zebrafish) would be the appropriate starting points for confirming the current state of any deposited *Ecm1*/*ecm1* alleles, though this search did not directly query those databases.

Sources: [Search results on Ecm1 mouse knockout embryonic lethality; ECM1 zebrafish knockdown model](citations above), [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK338540/)

---

## Summary of Key Curation-Relevant Points for dismech

1. **Causal chain for pathophysiology nodes:** ECM1 biallelic LOF variant → loss of ECM1 basement-membrane/ECM scaffolding function (disrupted binding to collagen IV, laminin-332, fibulin-1/3, perlecan, MMP-9) → altered keratinocyte differentiation and collagen IV/V metabolism → basement-membrane reduplication and dermal/mucosal hyaline deposition → clinical mucocutaneous phenotype (hoarseness, skin thickening, blepharosis) and, in a subset, CNS (amygdala/hippocampal) calcification → temporal lobe epilepsy and neuropsychiatric/behavioral phenotype (memory impairment, absence-of-fear).
2. **Notable candidate mechanism module fit:** This causal chain (structural ECM protein loss → basement-membrane/tissue matrix pathology → progressive fibrohyaline deposition) does not map cleanly onto the existing fibrotic_response or amyloidogenesis modules (the deposited material is not classic fibrosis or amyloid) — likely best modeled as a disease-specific pathophysiology chain rather than forced into an existing module, though the "Xogenesis" (pathological-structure-formation: hyaline deposit formation) convention used for amyloidogenesis/granuloma_formation/thrombogenesis/atherogenesis could be a relevant framing to consider for a hyaline-deposit anchor if the project later wants a `Xogenesis`-style module.
3. **Notable human-model mismatch:** mouse *Ecm1* knockout embryonic lethality vs. viable human phenotype — flag with `kind: HUMAN_MODEL_MISMATCH` if curated, since it is a genuine unresolved translational-validity question rather than mere absent evidence.
4. **Digenic/oligogenic:** Not applicable — LP is a straightforward single-locus autosomal recessive disorder with no documented digenic/oligogenic modifiers.
5. **Evidence-source classification reminders:** Hamada 2002 and most genetic-mapping/case-report papers = HUMAN_CLINICAL; the zebrafish knockdown study = MODEL_ORGANISM; ECM1-protein-interaction co-IP studies = IN_VITRO.

**Key PMIDs identified for evidence citation (verify snippets via `just fetch-reference` before use):** 11929856 (Hamada et al., ECM1 mapping/mutation discovery), 15327549 (Namaqualand founder study), 12603844 (Chan et al., genotype-phenotype correlation), 18200062 (ECM1 basement membrane protein of skin), 19275936 (ECM1-fibulin-3/laminin-332 interaction), 14723723 (role of ECM1 in human skin), 38308656 (2024 systematic review of LP treatment), 16225617 (novel ECM1 mutation, Sicily).

---

### Sources (consolidated)
- [OMIM #247100 — Lipoid Proteinosis of Urbach and Wiethe](https://omim.org/entry/247100)
- [GeneReviews: Lipoid Proteinosis](https://www.ncbi.nlm.nih.gov/books/NBK338540/)
- [StatPearls: Lipoid Proteinosis](https://www.ncbi.nlm.nih.gov/books/NBK568769/)
- [Hamada et al. 2002, PubMed 11929856](https://pubmed.ncbi.nlm.nih.gov/11929856/)
- [Van Hougenhouck-Tulleken et al., Namaqualand study, PubMed 15327549](https://pubmed.ncbi.nlm.nih.gov/15327549/)
- [Chan et al., genotype-phenotype correlation, PubMed 12603844](https://pubmed.ncbi.nlm.nih.gov/12603844/)
- [ECM1 basement membrane protein of skin, PubMed 18200062](https://pubmed.ncbi.nlm.nih.gov/18200062/)
- [ECM1 interacts with fibulin-3/laminin 332, PubMed 19275936](https://pubmed.ncbi.nlm.nih.gov/19275936/)
- [Role of ECM1 in human skin, PubMed 14723723](https://pubmed.ncbi.nlm.nih.gov/14723723/)
- [Ultrastructural aspects of skin in LP, PMC8790196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8790196/)
- [A novel ECM1 mutation, Sicily, PubMed 16225617](https://pubmed.ncbi.nlm.nih.gov/16225617/)
- [Treatment of LP due to p.C220G, J Transl Med](https://link.springer.com/article/10.1186/1479-5876-12-85)
- [MalaCards: Lipoid Proteinosis of Urbach and Wiethe](https://www.malacards.org/card/lipoid_proteinosis_of_urbach_and_wiethe)
- [Acitretin Treatment for Lipoid Proteinosis, PMC3505959](https://pmc.ncbi.nlm.nih.gov/articles/PMC3505959/)
- [Advances in treatment for LP: systematic review, PubMed 38308656](https://pubmed.ncbi.nlm.nih.gov/38308656/)
- [Luo et al. 2016, acitretin in Chinese C220G families](https://onlinelibrary.wiley.com/doi/abs/10.1111/1346-8138.13261)
- [AJNR: Lipoid Proteinosis Bilateral Amygdalae Calcifications](https://www.ajnr.org/ajnr-case-collections-diagnosis/lipoid-proteinosis-bilateral-amygdalae-calcifications)
- [Radiologic presentation with symmetrical medial temporal lobe calcifications, PMC4921162](https://pmc.ncbi.nlm.nih.gov/articles/PMC4921162/)
- [Neurology 2013: LP with bilateral amygdalae calcifications, headache, cognitive impairment](https://www.neurology.org/doi/10.1212/WNL.0b013e31829bfe1c)
- [Brain imaging findings in LP, PMC12301744](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12301744/)
- [S.M. (patient) — Wikipedia summary of amygdala/fear research](https://en.wikipedia.org/wiki/S.M._(patient))
- [Feinstein — Living Without an Amygdala (chapter PDF)](https://shackmanlab.org/wp-content/uploads/2024/03/Feinstein_PatientSMChapter2016.pdf)
- [J Neurosci: Panic Anxiety in Humans with Bilateral Amygdala Lesions](https://www.jneurosci.org/content/36/12/3559)
- [NCBI Bookshelf: Genetic Disorders Associated with Founder Variants Common in the Afrikaner Population](https://www.ncbi.nlm.nih.gov/books/NBK583036/)
- [GeneCards: ECM1](https://www.genecards.org/card/ECM1)
- [DermNet NZ: Lipoid Proteinosis](https://dermnetnz.org/topics/lipoid-proteinosis)