---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T03:51:03.504918'
end_time: '2026-08-20T03:55:11.691845'
duration_seconds: 248.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: UBA5-Related Developmental and Epileptic Encephalopathy
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
  web_search_requests: 16
  num_turns: 24
  total_cost_usd: 1.9186447999999996
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC8208045
  relevance_assessed: 12
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** UBA5-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **UBA5-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I have enough to compile a comprehensive report now.

I now have sufficient material to compile the full report.

# UBA5-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

### Overview

UBA5-related developmental and epileptic encephalopathy — formally **Developmental and Epileptic Encephalopathy 44 (DEE44)**, and historically termed "Early Infantile Epileptic Encephalopathy-44 (EIEE44)" — is an ultra-rare, autosomal recessive neurodevelopmental disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in **UBA5**, which encodes the E1-like activating enzyme of the UFMylation post-translational modification pathway. The disorder was first described in 2016 in three back-to-back reports (Colin et al., Duan et al., Muona et al., all *Am J Hum Genet* 99(3)), making UBA5 "the first gene from the ufmylation pathway... linked to disease" ([PMC8208045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208045/)). It is characterized by early-onset (typically first weeks to months of life) refractory epilepsy/infantile spasms, severe global developmental delay/intellectual disability, hypotonia with limb hypertonia, dystonia, microcephaly, failure to thrive, and progressive white-matter/cerebellar abnormalities on MRI ([OMIM #617132](https://www.omim.org/entry/617132); [eLife 89891](https://elifesciences.org/articles/89891)).

Biallelic UBA5 variants produce a **phenotypic spectrum along a severity continuum** rather than a single discrete disease, spanning three overlapping presentations:
1. **DEE44** — severe infantile-onset encephalopathy with/without seizures (the majority phenotype)
2. **Autosomal recessive spinocerebellar ataxia 24 (SCAR24, OMIM #617133)** — milder, childhood-onset progressive gait/limb ataxia with normal-to-preserved cognition
3. **Severe congenital neuropathy** — profound sensorimotor peripheral neuropathy, sometimes fatal in infancy, with or without CNS involvement

([Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/846/gene/UBA5/); [PMC10691876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691876))

### Key Identifiers
- **OMIM disease**: #617132 (DEE44); related #617133 (SCAR24)
- **OMIM gene**: *610552 (UBA5)
- **Gene**: UBA5 — HGNC:23230, chromosome 3q22.1
- **UniProt**: Q9GZZ9
- **Inheritance**: Autosomal recessive
- **Synonyms**: Early infantile epileptic encephalopathy 44 (EIEE44, older nomenclature); UBA5-related encephalopathy; UBA5-associated encephalopathy; UBA5 deficiency

### Data Source Type
Nearly all clinical knowledge derives from **aggregated case reports and small case series** (individual patients and sibships) rather than large EHR-based cohorts, reflecting the extreme rarity of the condition — as of the most comprehensive published review, **24 individuals from ~17–19 families** had been reported ([PMC8208045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208045/); [eLife 89891](https://elifesciences.org/articles/89891), reporting "21/25" analyzed individuals).

---

## 2. Etiology

### Disease Causal Factor
Purely monogenic/genetic: biallelic pathogenic variants in **UBA5** causing partial-to-severe loss of UFM1-activating (E1) enzymatic function. There is no known environmental, infectious, or purely acquired cause.

### Genetic Risk Factors
- **Compound heterozygosity is the dominant genotype**: most reported patients carry one severe/null allele in *trans* with a hypomorphic (partial-function) allele — a pattern essential to viability, since complete biallelic null UBA5 is likely embryonic/perinatally lethal (consistent with murine data below).
- **Recurrent hypomorphic allele p.Ala371Thr (c.1111G>A)**: found in ~65–70% of DEE44 alleles reported (12/17 families in one series), functioning as a weak/mild hypomorphic variant that preserves partial E1 activity. Population database carrier frequencies are estimated at **1 in 84 in Finnish populations** and **1 in 200 in non-Finnish Europeans**, and homozygosity for p.A371T alone is reported in **asymptomatic adults** in population databases — establishing it as a "very weak allele" below a pathogenic threshold on its own ([PMC8208045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208045/); [eLife 89891](https://elifesciences.org/articles/89891)).
- **Founder homozygous variant p.Arg11Trp (c.31C>T)** identified in a consanguineous multigenerational family, associated with a fatal congenital neuropathy phenotype ([ResearchGate/J Med Genet](https://www.researchgate.net/publication/339959720)).
- No modifier genes have yet been formally established, though allelic strength (see §4) is itself the principal determinant of phenotype severity.

### Risk Factors
- **Consanguinity** increases risk of biallelic pathogenic combinations, particularly for the severe congenital-neuropathy phenotype.
- No age, sex, lifestyle, or occupational risk factors are known (Mendelian recessive disease).

### Protective Factors
- Genetically, inheriting **two mild/hypomorphic alleles** (e.g., homozygous p.A371T) appears protective/asymptomatic — a genotype–phenotype threshold effect rather than a distinct "protective variant."
- No environmental or lifestyle protective factors identified.

### Gene-Environment Interactions
None established; this is considered a purely monogenic disorder with no reported environmental modifiers of penetrance or expressivity.

---

## 3. Phenotypes

### Core Clinical Features (with suggested HPO terms)

| Phenotype | Frequency (from reviewed cohorts) | Suggested HPO term |
|---|---|---|
| Global developmental delay / intellectual disability (severe–profound) | ~95% | HP:0001263 / HP:0001249 |
| Axial hypotonia with appendicular hypertonia | Majority | HP:0008936 / HP:0002540 |
| Dystonia / movement disorder | 20/24 (83%) | HP:0001332 |
| Failure to thrive (despite adequate caloric intake) | 75% | HP:0001508 |
| Seizures/epilepsy (infantile spasms most common) | Majority; infantile spasms ~54% | HP:0001250; infantile spasms HP:0011097 |
| Microcephaly (often acquired/progressive) | Common | HP:0000252 |
| Drug-resistant/refractory epilepsy | Common | HP:0011451 |
| Visual impairment | Reported | HP:0000505 |
| Delayed myelination on MRI | ~100% of imaged cases | HP:0012448 |
| Thin/abnormal corpus callosum | Common | HP:0033725 |
| Cerebellar/cerebral atrophy | Common | HP:0001272 / HP:0002059 |
| White matter hyperintensities | Common | HP:0030890 |
| Peripheral sensorimotor neuropathy (in neuropathy-predominant subtype) | Subtype-specific | HP:0007141 |
| Gait/limb ataxia, dysarthria, nystagmus, cataracts (SCAR24 phenotype) | SCAR24 subtype | HP:0001288/HP:0001260/HP:0000639/HP:0000518 |

### Phenotype Characteristics
- **Onset**: Most cases present in early infancy — "refractory infantile spasms or myoclonus usually in the first weeks or months of life, up to about 12 months of age" ([OMIM](https://www.omim.org/entry/617132)). The most severe reported genotype caused burst-suppression encephalopathy within hours of birth, with death at 16 days. Conversely, seizure onset was delayed to childhood in some patients, and the milder SCAR24 phenotype presents with ataxia onset at 5–8 years of age.
- **Severity**: Highly variable, ranging from neonatal-lethal encephalopathy to milder ataxia-predominant disease with preserved cognition in adulthood — directly correlating with residual UFM1-activating enzymatic activity (allelic strength; see §4/§6).
- **Progression**: Generally progressive for both the encephalopathy (worsening motor/cognitive trajectory, evolving MRI abnormalities — "imaging was normal in the first months of life but later showed abnormalities" in many patients) and the SCAR24 ataxia phenotype (one adult sibling lost ambulation by age 39).
- **Frequency among affected individuals**: See table above; based on small aggregated cohorts (n≈24–25), so percentages should be interpreted cautiously.

### Quality of Life Impact
Severely affected individuals experience profound lifelong disability: non-ambulation, minimal-to-absent verbal communication, inability to hold the head upright, and dependence on caregivers for all activities of daily living. Refractory dystonia/status dystonicus can be life-threatening and has required emergency deep brain stimulation ([PMID:37130202](https://pubmed.ncbi.nlm.nih.gov/37130202/)). Failure to thrive despite adequate nutrition adds additional medical burden; the pituitary gland is notably the highest UBA5-expressing tissue in GTEx, raising a hypothesized but unconfirmed growth-hormone-axis contribution.

---

## 4. Genetic/Molecular Information

### Causal Gene
- **UBA5** (OMIM *610552), chromosome 3q22.1, encodes an E1-like ubiquitin-activating enzyme (EC 6.2.1.45) that is the sole known activator of UFM1 (ubiquitin-fold modifier 1).

### Pathogenic Variants
- **Gene**: UBA5, HGNC:23230
- **Variant classification**: Missense (majority — affecting the adenylation/catalytic domain), nonsense (e.g., p.Arg188*), frameshift, and rare intronic/splice variants, all loss-of-function to varying degrees.
- **Variant type/class and functional impact**: Systematic biochemical and in vivo (humanized *Drosophila*) characterization of 13+ missense variants stratified them into four allelic-strength classes — **Group IA/IB** (mild hypomorphs; full or near-full lethality rescue in flies but progressive phenotypes), **Group II** (partial rescue; developmental delay, seizure-like behavior), and **Group III** (severe loss-of-function; failed rescue, insoluble/misfolded protein), plus **Group IV** null/frameshift alleles ([eLife 89891](https://elifesciences.org/articles/89891)). "There is a strong correlation between in vivo and in vitro phenotypes, establishing a classification of LoF variants into mild, intermediate, and severe allelic strengths."
- **Key recurrent variants**:
  - **p.Ala371Thr (c.1111G>A)** — recurrent hypomorphic allele in ~65–70% of DEE44 alleles, always found in *trans* with a more severe variant in symptomatic individuals; homozygous in some asymptomatic adults; shows temperature-dependent loss of UFM1 transthiolation activity at 22°C but not 37°C in vitro.
  - **p.Tyr53Phe (c.158A>T)** (homozygous) — associated with the most severe reported phenotype (death from status epilepticus); E1 activity reduced to 3.4% and E2 (transthiolation) activity to 6.8% of wild type.
  - **p.Arg11Trp (c.31C>T)** (homozygous, founder in a consanguineous family) — fatal congenital neuropathy.
  - **p.Cys303Arg, p.Leu254Pro** — novel variants causing significant functional impairment, each identified in two unrelated families/sibships.
  - Catalytic residue: **Cys250** forms the active-site thioester bond with UFM1's C-terminal glycine after ATP-dependent adenylation; the engineered enzyme-dead control p.Cys250Ala is used as a null reference in functional assays.
- **Allele frequency**: p.A371T carrier frequency ~1/84 (Finnish) and ~1/200 (non-Finnish European) in population databases (gnomAD-derived), consistent with a founder/recurrent hypomorphic allele rather than a fully deleterious one.
- **Somatic vs. germline**: Exclusively germline; no somatic mosaicism reported.
- **Functional consequence**: Loss of function (partial to near-complete) of UBA5's E1-activating enzymatic activity — reduced ATP binding, reduced UFM1 adenylation, reduced thioester (transthiolation) formation, and/or reduced protein stability/solubility, depending on variant location (buried structural residues → misfolding/insolubility; ATP-pocket residues → reduced catalysis without stability loss).

### Modifier Genes
None formally established; allelic strength of the two UBA5 alleles themselves is the principal known modifier of phenotype.

### Epigenetic Information
Not established for this disease specifically (UFMylation itself is increasingly recognized as intersecting broadly with chromatin/DNA-damage-response biology, but disease-specific epigenetic data are not reported).

### Chromosomal Abnormalities
None reported; this is a single-gene point-mutation/small-indel disorder, not a copy-number or structural chromosomal condition.

---

## 5. Environmental Information

No environmental toxins, occupational exposures, lifestyle factors, or infectious triggers have been implicated in UBA5-DEE44 — it is a purely monogenic disease. No infectious agents are associated.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway: UFMylation Cascade
UBA5 is the **E1-activating enzyme** of UFMylation, a ubiquitin-like post-translational modification (PTM) system parallel to but distinct from canonical ubiquitination. The cascade proceeds:

**UBA5 (E1) → UFC1 (E2, UFM1-conjugating enzyme) → UFL1/UFBP1/CDK5RAP3 (E3 ligase complex) → substrate conjugation with UFM1**

Mechanistically, UBA5 forms a **homodimer** that enables a *trans*-binding mechanism: UFM1 binds one subunit while the active site resides in the partner subunit. UBA5 first **adenylates** the C-terminal glycine of UFM1 (ATP-dependent), then forms a **thioester bond via active-site Cys250**, and finally transfers activated UFM1 to UFC1 (transthiolation) ([BRENDA EC 6.2.1.45](https://www.brenda-enzymes.org/enzyme.php?ecno=6.2.1.45); [PMC5428781](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428781/)).

### Causal Chain (Trigger → Manifestation)
1. **Biallelic UBA5 hypomorphic/null variants** → reduced UBA5 protein stability, ATP binding, or catalytic (adenylation/thioester) activity
2. → **Reduced global UFMylation flux** (reduced UBA5–UFM1 and downstream substrate–UFM1 conjugates; zebrafish models show Ufm1-conjugates reduced to ~30% of wild type)
3. → **Perturbed endoplasmic reticulum (ER) homeostasis and exacerbated unfolded protein response (UPR)** — elevated phospho-PERK and phospho-eIF2α, increased nuclear ATF6 translocation and CHOP expression, decreased IRE1α stability and reduced spliced XBP1, ER expansion (calnexin staining), and increased PARP cleavage (apoptosis) in patient-derived organoid/cell models ([Science Translational Medicine 2024/2025, PMID:38328212 preprint / PMID:40333994 published](https://www.science.org/doi/10.1126/scitranslmed.adn8417))
4. → **Mitochondrial dysfunction**: widespread mitochondrial pathology (abnormal cristae, vacuolated/"onion-ring" degenerating mitochondria, elevated full-length PINK1 indicating mitophagy activation) in zebrafish CNS, PNS, and skeletal muscle ([Brain Communications 2023, PMC10691876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691876))
5. → **Neurodevelopmental disruption**, most strikingly a **severe GABAergic interneuron deficit** in patient-derived cortical organoids (~15% GABAergic interneuron population vs. ~40% in controls, with reduced GAD1/GAD2/CALB2/SCGN expression) and **microcephaly** (patient organoids ~25% smaller than controls)
6. → **Aberrant network electrophysiology**: increased weighted mean firing rate and burst frequency, but paradoxically decreased *network* burst frequency, indicating impaired coordinated neuronal activity → clinical **epileptogenesis and encephalopathy**
7. → Downstream **peripheral neurodegeneration** (axonal/mitochondrial pathology in peripheral nerves) explains the neuropathy-predominant phenotypic pole, while cerebellar Purkinje/neuronal degeneration explains the ataxia-predominant pole (SCAR24)

### Cell Types and Biological Processes Involved
- **GABAergic interneurons** (loss/reduced differentiation) — candidate CL term: CL:0000617 (GABAergic neuron)
- **Cortical excitatory neurons** (aberrant firing)
- **Cerebellar neurons/Purkinje cells** (degeneration in SCAR24-type phenotype and in zebrafish cerebellar pathology at 14 dpf)
- **Peripheral sensorimotor neurons** (axonal degeneration in neuropathy-predominant phenotype)
- **Skeletal muscle** (mitochondrial pathology in zebrafish)
- Suggested GO terms: GO:0071569 (protein UFmylation), GO:0006986 (response to unfolded protein / UPR), GO:0034976 (response to ER stress), GO:0007005 (mitochondrion organization), GO:0000422 (mitophagy)

### Protein Dysfunction
Depending on variant location: **loss of catalytic (adenylation/thioester) function** at the active site, **loss of ATP-binding capacity**, or **structural misfolding/insolubility** for variants affecting buried hydrophobic residues (e.g., Gly168, Cys303) — demonstrated via thermal shift assays and purification studies in the eLife allelic-series paper.

### Advanced/Omics Technologies Applied
- **Patient-derived iPSC-cortical organoids** with single-cell/marker-based transcriptomic characterization (GABAergic marker panel) and multi-electrode-array electrophysiology
- **CRISPR-engineered isogenic cell lines** (U-87 MG) modeling specific compound-heterozygous genotypes (UBA5^A371T/R55H, UBA5^A371T/F292*)
- **CRISPRa (dCas9-VP64-p65-Rta) gene-activation** and **SINEUP synthetic lncRNA** approaches to therapeutically upregulate UBA5 translation

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: Central nervous system (brain — cortex, cerebellum, white matter, corpus callosum, thalami, hippocampus); in a subset of patients, the peripheral nervous system (peripheral nerves)
- **Secondary/systemic**: Growth failure/failure to thrive (possible pituitary/growth-hormone axis involvement, speculative); in SCAR24, eyes (cataracts) are also affected
- **Body systems**: Nervous system (primary); endocrine/growth axis (secondary, unconfirmed mechanism); musculoskeletal (secondary to hypertonia/dystonia)
- **Tissue/cell level**: Cerebral cortical neurons and GABAergic interneurons; cerebellar neurons; peripheral sensorimotor axons; skeletal muscle (mitochondrial pathology in models)
- **Subcellular level**: Endoplasmic reticulum (UPR activation, ER expansion), mitochondria (structural/functional pathology, mitophagy activation) — candidate GO Cellular Component terms: GO:0005783 (endoplasmic reticulum), GO:0005739 (mitochondrion)
- **Localization (UBERON)**: UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002336 (corpus callosum white matter), UBERON:0001017 (central nervous system), UBERON:0000010 (peripheral nervous system)
- **Laterality**: Bilateral/diffuse — not a lateralized process

---

## 8. Temporal Development

- **Onset**: Typically neonatal-to-early-infantile (first weeks to ~12 months) for DEE44; childhood (5–8 years) for the SCAR24 ataxia phenotype; congenital (in utero, reduced fetal movements) for the severe neuropathy phenotype.
- **Onset pattern**: Acute-to-subacute for the most severe neonatal encephalopathy (burst suppression within hours of birth in the most severe case); insidious/progressive for ataxia and developmental phenotypes.
- **Progression**: Generally progressive — worsening motor/developmental trajectory, evolving neuroimaging abnormalities (many patients have normal early imaging that becomes abnormal over time), and in SCAR24, progressive loss of ambulation over decades (one sibling lost independent ambulation at age 39).
- **Disease course pattern**: Chronic-progressive rather than relapsing-remitting; punctuated by episodes of status epilepticus or status dystonicus that can themselves be acutely life-threatening.
- **Disease duration**: Chronic, lifelong in survivors; the most severe genotypes are neonatally or infantile lethal (e.g., death at 16 days in one report; the congenital neuropathy phenotype causes "early death in infancy" in a consanguineous family).
- **Critical periods**: Early infancy appears to be a critical window for both diagnosis (before irreversible neurodevelopmental injury) and, per model-system data, for potential UBA5-upregulation therapeutics (organoid electrophysiology correction was only transient, suggesting narrow/ongoing dosing windows may matter).

---

## 9. Inheritance and Population

- **Epidemiology**: Ultra-rare — approximately 24–25 individuals from ~17–19 families reported in the literature as of the most recent comprehensive reviews (2021 review; 2023 eLife series). True population prevalence/incidence is not established (likely underdiagnosed given phenotypic overlap with other genetic epilepsies/encephalopathies).
- **Inheritance pattern**: Autosomal recessive.
- **Penetrance**: Complete for the disease-causing genotype combinations reported, but with a documented **threshold effect** — biallelic combinations of very mild hypomorphic alleles (e.g., homozygous p.A371T) are reported as **asymptomatic** in population databases, indicating incomplete penetrance is possible for the mildest allelic combinations depending on residual enzymatic activity.
- **Expressivity**: Highly variable — spanning fatal neonatal encephalopathy/congenital neuropathy to adult-onset ataxia with normal cognition, driven largely by the combined "allelic strength" of the two inherited variants.
- **Genetic anticipation**: Not reported/not applicable (not a repeat-expansion disorder).
- **Germline mosaicism**: Not specifically documented in the literature reviewed.
- **Founder effects**: p.Ala371Thr shows an elevated carrier frequency consistent with a founder/recurrent allele in Finnish (1/84) and other European (1/200) populations; p.Arg11Trp is a founder variant in a specific consanguineous family lineage.
- **Consanguinity**: A recognized contributor, particularly for the homozygous severe congenital-neuropathy phenotype (large consanguineous multigenerational family reported).
- **Carrier frequency**: See p.A371T figures above; overall UBA5 pathogenic-variant carrier frequency in the general population is not separately quantified.
- **Population demographics**: Reported cases span diverse ancestries; SCAR24 was first reported in Chinese siblings; DEE44 cases span European, Finnish, and other backgrounds. No clear geographic endemicity beyond the Finnish/European founder-allele signal.
- **Sex ratio**: No sex predilection reported (autosomal recessive).
- **Age distribution**: Reported individuals span neonates to adults in their late 30s (the oldest reported SCAR24 patient).

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- No specific disease biomarker exists; diagnosis relies on **genetic confirmation** in the context of a compatible clinical/EEG/MRI phenotype.
- **EEG**: Near-universal abnormality — spikes/polyspikes with background slowing and disorganization; hypsarrhythmia in infantile-spasms presentations; burst suppression in the most severe neonatal cases.
- **Brain MRI**: Delayed myelination, thin/dysmorphic corpus callosum, cerebral/cerebellar atrophy, white matter hyperintensities, diminutive thalami, abnormal hippocampal orientation, and altered U-fiber pattern; often normal in early infancy with abnormalities emerging over time — serial imaging is informative.
- **Nerve conduction studies/EMG**: Relevant in the neuropathy-predominant phenotype to document severe sensorimotor peripheral neuropathy.

### Genetic Testing
- **Whole exome sequencing (WES) or whole genome sequencing (WGS)** is the primary diagnostic approach given the phenotypic overlap of DEE44 with dozens of other genetic developmental and epileptic encephalopathies; UBA5 is included on epilepsy/DEE gene panels.
- **Targeted gene panels** for early infantile epileptic encephalopathy / developmental and epileptic encephalopathy routinely include UBA5.
- **Single-gene/Sanger confirmation** of variants identified by panel/exome sequencing, and segregation testing in parents to confirm compound heterozygosity (trans configuration).
- Functional/biochemical variant classification (as developed in the eLife allelic-series study) is emerging as a research-grade tool to help interpret novel missense VUS by comparison to characterized allelic-strength groups.

### Clinical Diagnostic Criteria
No formal consensus diagnostic criteria exist (ultra-rare disease); diagnosis is genotype-driven (biallelic UBA5 pathogenic/likely pathogenic variants) combined with compatible phenotype per OMIM clinical synopsis and case-series-derived phenotype descriptions.

### Differential Diagnosis
Other genetic developmental and epileptic encephalopathies (e.g., CDKL5 deficiency disorder, STXBP1-DEE, other early infantile epileptic encephalopathies), other UFMylation-pathway disorders (UFM1, UFC1, UFSP2, UFBP1/DDRGK1, CDK5RAP3 — all now linked to overlapping hypomyelinating leukodystrophy/encephalopathy phenotypes), and other causes of hypotonia/failure-to-thrive with epilepsy.

### Screening
No population-based newborn or carrier screening program specifically targets UBA5 given its rarity; carrier screening could theoretically be offered in populations with elevated p.A371T-type founder frequencies, but this is not standard practice.

---

## 11. Outcome/Prognosis

- **Survival/mortality**: Ranges from neonatal/infantile death (most severe genotypes — e.g., death at 16 days from a homozygous severely hypomorphic variant; early infant death in the fatal congenital neuropathy family) to survival into adulthood with milder genotypes (SCAR24 patients surviving into their 30s–40s with progressive but non-lethal disease course).
- **Morbidity/function**: Severely affected individuals have profound, lifelong intellectual disability, non-ambulation, and dependence on caregivers; refractory epilepsy and dystonia (including life-threatening status dystonicus) are major sources of morbidity.
- **Complications**: Status epilepticus (a reported cause of death), status dystonicus requiring emergency intervention, failure to thrive/malnutrition, aspiration risk from severe motor impairment.
- **Recovery potential**: No cure exists; supportive/symptomatic management is the current standard. Investigational UBA5-upregulation approaches (see below) show preclinical proof-of-concept for partial phenotype correction.
- **Prognostic factors**: Genotype (allelic strength of both variants) is the dominant known prognostic determinant — severe/severe or severe/null combinations are neonatally lethal or profoundly disabling, while mild/mild combinations may be asymptomatic-to-mildly affected (SCAR24-type or subclinical).

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is entirely supportive/symptomatic.

### Pharmacotherapy
- **Antiepileptic drugs (AEDs)**: Multiple AEDs are typically required given drug-resistant seizures; specific agent selection is individualized and not standardized for this ultra-rare disease. NCIT term: NCIT:C15632/NCIT:C15986 categories apply generically (Pharmacotherapy/anticonvulsant therapy).
- **Levodopa**: Reported to provide "moderate improvement" in the movement disorder for at least one patient.
- **Prophylactic antiepileptic treatment**: Used in some patients based on EEG abnormalities even before clinical seizures manifest.

### Advanced/Interventional
- **Deep brain stimulation (globus pallidus internus, GPi-DBS)**: Used for medically refractory dystonia/status dystonicus in UBA5-related disorder, with one report describing "dramatic improvement in dystonia" and a dedicated case report of DBS for medically refractory status dystonicus ([PMID:37130202](https://pubmed.ncbi.nlm.nih.gov/37130202/), *Movement Disorders* 2023). NCIT candidate term: device/procedural intervention (DBS has no precise NCIT clinical-action term identified; would require DEVICE modality classification).

### Dietary/Supportive
- **Ketogenic diet**: A generic option for drug-resistant epilepsy broadly (not UBA5-specific evidence identified, but plausible extrapolated management given refractory-epilepsy phenotype); NCIT:C15447 (Dietary Intervention).
- **Nutritional support** for failure to thrive (feeding tube support commonly needed in severe developmental and epileptic encephalopathies generally).
- **Physical, occupational, and speech therapy**: Standard supportive rehabilitative care (NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation).

### Experimental/Investigational
No registered UBA5-specific clinical trials were identified (ClinicalTrials.gov search did not surface an active interventional trial). Preclinical therapeutic strategies under active research development, targeting the core mechanism (increasing residual UBA5 protein/activity), include:
- **SINEUP synthetic long non-coding RNA** — increased UBA5 translation ~1.5-fold in patient organoids, transiently normalizing aberrant electrophysiology (effect lasted 2–4 days) ([Science Translational Medicine, PMID:40333994](https://www.science.org/doi/10.1126/scitranslmed.adn8417))
- **CRISPRa (dCas9-VP64-p65-Rta) gene activation** — achieved ~2-fold UBA5 protein increase, restoring ER-homeostasis/UPR markers
- Rationale: because the common p.A371T hypomorphic allele is compatible with an asymptomatic state when both alleles are equally mild, **modest (not excessive — overexpression is itself detrimental) upregulation** of UBA5 expression is hypothesized as a therapeutic strategy for patients carrying at least one A371T-class allele.

### Treatment Outcomes
Given the small numbers, no systematic response-rate or adverse-event data exist beyond individual case reports; drug-resistant epilepsy is the norm, and DBS/levodopa responses are anecdotal.

### Treatment Strategy
No formal treatment algorithm exists; management follows general refractory-DEE/movement-disorder principles (stepwise AED trials → ketogenic diet consideration → DBS for refractory dystonia) individualized by clinical team, informed by emerging genotype-function data as a potential future guide to prognosis counseling.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the traditional sense (monogenic recessive disease); **genetic/carrier counseling** for at-risk families (especially those with known founder alleles or consanguinity) is the main preventive lever, alongside **prenatal diagnosis or preimplantation genetic testing (PGT)** for families with a previously affected child and known biallelic variants.
- **Secondary prevention**: Early genetic diagnosis via WES/WGS in infants presenting with unexplained early-onset encephalopathy/refractory seizures allows earlier supportive intervention (though no disease-modifying treatment currently changes the trajectory).
- **Tertiary prevention**: Aggressive seizure and dystonia management (including DBS) to reduce morbidity/mortality from status epilepticus or status dystonicus; nutritional support to prevent complications of failure to thrive.
- **Genetic counseling**: Recommended for parents of an affected child (25% recurrence risk per pregnancy) and for extended family members in consanguineous or founder-allele-enriched populations (NCIT:C15240 Genetic Counseling).
- **Carrier screening**: Not part of standard population carrier screening panels currently, but could be considered in populations with elevated p.A371T carrier frequency (e.g., Finnish population) as awareness grows.

---

## 14. Other Species / Natural Disease

- No spontaneously occurring UBA5-related disease has been reported in domestic animals, companion animals, or wildlife (OMIA search did not surface a natural veterinary UBA5 disease). This section is not applicable beyond engineered laboratory models (see §15).
- **Orthologous gene**: UBA5 orthologs are highly conserved; the *Drosophila melanogaster* ortholog (Uba5) shares 64% amino acid identity / 75% similarity with human UBA5, sufficient for successful "humanization" (replacement with human UBA5 cDNA) in fly disease models.

---

## 15. Model Organisms

### Mouse
- **Germline Uba5 knockout mice are embryonic lethal at E12.5**, caused by hematopoietic defects — this precludes direct study of the neurological phenotype and demonstrates that complete loss of UBA5 function is incompatible with development, consistent with the human observation that all reported patients carry at least one partial-function (hypomorphic) allele ([MGI:1913913](https://www.informatics.jax.org/marker/MGI:1913913)).
- Conditional/hypomorphic mouse alleles that better model human disease were not identified as established in the sources reviewed here — this is a **noted gap** (relevant to a `HUMAN_MODEL_MISMATCH` framing: the null mouse model fails to recapitulate the human neurological phenotype and instead demonstrates a distinct hematopoietic-lethal mechanism).

### Zebrafish (the leading in vivo model)
- Two independent CRISPR-Cas9-engineered *uba5* mutant zebrafish lines: **uba5ex1s** (exon 1 nonsense/frameshift, p.E5Ffs*1, truncated non-functional protein) and **uba5ex3d** (exon 3 in-frame deletion of the ATP-binding domain, p.A73_V80del) ([Brain Communications 2023, PMC10691876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691876)).
- **Phenotype recapitulation (RECAPITULATES)**: 41–45% reduced swimming distance at 6 dpf; 40–50% reduced body length from 14 dpf; severely reduced survival (only 4% surviving past 39 dpf, max lifespan 70 dpf) — closely mirroring human motor impairment, growth failure, and reduced life expectancy.
- **CNS findings**: cerebellar neuronal degeneration at 14 dpf (abnormal membranous swirls, degenerating mitochondria); no gross brain/cerebellar volume change at 6 dpf.
- **PNS findings**: peripheral nerve abnormalities at 6 dpf (autophagic structures, large vesicles, elongated/degenerating mitochondria in nerve terminals) — directly modeling the human neuropathy-predominant phenotypic pole.
- **Mitochondrial pathology**: widespread abnormal cristae, vacuolated/"onion-ring" mitochondria, elevated full-length PINK1 (mitophagy activation), and reduced Ufm1-conjugates to ~30% of wild type — providing the strongest evidence to date for mitochondrial dysfunction as a downstream consequence of UFMylation loss.
- **Applications**: motor function assays (high-throughput swimming/locomotor tracking), survival/lifespan assays, ultrastructural (EM) study of CNS/PNS/muscle mitochondrial pathology, and validation of variant pathogenicity.

### Drosophila melanogaster
- "Humanized" fly models expressing human UBA5 variants under the control of the endogenous *Uba5* promoter (replacing/complementing the fly ortholog, 64% identity/75% similarity to human) were used to systematically test **13+ patient missense variants plus synthetic controls** (e.g., enzyme-dead p.Cys250Ala) across **viability, developmental timing, lifespan, locomotor activity, and bang-sensitivity (seizure-like) assays** ([eLife 89891](https://elifesciences.org/articles/89891)).
- Variants stratified into **Groups IA/IB/II/III/IV** by degree of phenotype rescue, which **strongly correlated with in vitro biochemical severity** (thermal stability, ATP binding, UbiReal fluorescence-polarization transthiolation assays) — establishing the fly platform as a validated variant-classification tool bridging genotype to phenotype severity, directly informative for VUS interpretation in newly identified patients.
- Clinical correlation: 21/25 analyzed affected individuals carried one Group IA/IB (mild) allele in *trans* with one Group III/IV (severe) allele, mechanistically explaining why "mild + severe" combinations are viable and symptomatic while "severe + severe" combinations are presumed embryonic/perinatally lethal (paralleling the mouse null-lethality finding).

### Patient-Derived Cellular/Organoid Models
- **iPSC-derived cortical organoids** from two probands (compound heterozygous UBA5 variants) plus isogenic parental controls, and **CRISPR-engineered U-87 MG glioma cell lines** carrying specific patient genotypes (UBA5^A371T/R55H; UBA5^A371T/F292*) and a benign control (UBA5^A371T/A371T homozygous) ([Science Translational Medicine, PMID:40333994](https://www.science.org/doi/10.1126/scitranslmed.adn8417); preprint PMID:38328212).
- **Fidelity**: High construct validity for modeling human-specific neurodevelopmental features (GABAergic interneuron specification, cortical organoid electrophysiology) not accessible in mouse/fish; **RECAPITULATES** microcephaly (~25% organoid size reduction), GABAergic interneuron deficit (~15% vs ~40% in controls), ER stress/UPR activation, and network-level electrophysiological abnormality.
- **Limitations**: Organoids model early corticogenesis and lack mature circuit-level, in vivo behavioral correlates (seizures, motor phenotype); therapeutic rescue (SINEUP) was only transient (2–4 days), an unresolved translational gap.
- **Research applications**: Mechanistic dissection of ER/UPR and GABAergic-lineage pathology; platform for testing UBA5-upregulation therapeutic strategies (SINEUP RNA, CRISPRa) prior to any in vivo/clinical translation.

---

## Summary Table: Key Evidence Citations

| Claim | PMID / Source |
|---|---|
| First disease description (2016) | Colin et al. *AJHG* 99(3):695-703; Muona et al. *AJHG* 99(3):683-694 (PMID:27545675 region); Duan et al. 2016 (SCAR24) |
| Compound heterozygous mutations, two sisters | [PMID:28965491](https://pubmed.ncbi.nlm.nih.gov/28965491/) |
| Novel variants / phenotypic spectrum review (24 individuals, 19 families) | [PMC8208045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208045/) |
| OMIM DEE44 clinical synopsis | [OMIM #617132](https://www.omim.org/entry/617132) |
| OMIM SCAR24 | [OMIM #617133](https://omim.org/entry/617133) |
| Allelic strength classification, Drosophila + biochemistry | [eLife 89891](https://elifesciences.org/articles/89891) / [PMC10371176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10371176) |
| Zebrafish model, mitochondrial abnormalities | [Brain Communications, PMC10691876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10691876) |
| Patient-derived organoid model & therapeutic strategies | [Science Translational Medicine, PMID:40333994](https://www.science.org/doi/10.1126/scitranslmed.adn8417); preprint [PMID:38328212](https://pubmed.ncbi.nlm.nih.gov/38328212/) |
| Fatal congenital neuropathy, p.Arg11Trp | [J Med Genet, ResearchGate summary](https://www.researchgate.net/publication/339959720) |
| DBS for status dystonicus | [PMID:37130202](https://pubmed.ncbi.nlm.nih.gov/37130202/) |
| Case report, compound heterozygous DEE44 | [PMC11960287](https://pmc.ncbi.nlm.nih.gov/articles/PMC11960287/) / [PMID:40217280](https://pubmed.ncbi.nlm.nih.gov/40217280/) |

**Note on gaps**: No formal GeneReviews chapter, no MONDO ID, and no large systematic natural-history study (>25 patients) were identified in this search — these represent genuine literature gaps rather than omissions, consistent with UBA5-DEE44's status as an ultra-rare, recently-described (2016) condition. No active registered clinical trial was found. Mouse knockout data reflect a `HUMAN_MODEL_MISMATCH`-type limitation (embryonic lethality via a hematopoietic, not neurological, mechanism) rather than a validated CNS/PNS disease model, in contrast to the zebrafish and Drosophila platforms.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC8208045` *(abstract only)*: "the first gene from the ufmylation pathway... linked to disease"
  - closest text in source: "Early infantile epileptic encephalopathy-44 (EIEE44, MIM: 617132) is a previously described condition resulting from biallelic variants in UBA5, a gene involved in a ubiquitin-like post-translational modification system called UFMylation"