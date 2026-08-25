---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T03:51:02.109641'
end_time: '2026-08-20T03:56:56.347830'
duration_seconds: 354.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CYFIP2-Related Developmental and Epileptic Encephalopathy
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
  num_turns: 30
  total_cost_usd: 2.3263049
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 21
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 9
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CYFIP2-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CYFIP2-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research this using web search and fetch tools to gather accurate, citable information before writing the report.

I now have sufficient material to compile a comprehensive report. Let me write it up.

I have sufficient primary-source material now. Compiling the comprehensive report.

I now have comprehensive, well-sourced material. Here is the full research report.

---

# CYFIP2-Related Developmental and Epileptic Encephalopathy — Research Report

## 1. Disease Information

**Overview.** CYFIP2-related developmental and epileptic encephalopathy (DEE) is an autosomal dominant neurodevelopmental disorder caused by heterozygous, almost always *de novo*, missense (rarely in-frame deletion or splice-site) variants in **CYFIP2** (Cytoplasmic FMR1-Interacting Protein 2), a core structural component of the WAVE regulatory complex (WRC) that governs Arp2/3-mediated actin polymerization. It presents with early-onset, typically drug-resistant seizures (often infantile spasms/West syndrome), severe to profound global developmental delay/intellectual disability, hypotonia, and — in a subset — hyperkinetic/dyskinetic movements and microcephaly ([OMIM #618008](https://omim.org/entry/618008); [Nakashima et al. 2018, PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/)).

**Key identifiers:**
- **OMIM disease:** #618008 — *Developmental and Epileptic Encephalopathy 65 (DEE65)*
- **OMIM gene:** *606323 — CYFIP2 (Cytoplasmic FMRP-Interacting Protein 2)*
- **Gene location:** 5q33.3
- **HGNC:** HGNC:13760 (CYFIP2)
- **MONDO:** MONDO:0033374 (per Monarch/MalaCards cross-reference)
- **Orphanet (broader umbrella):** ORPHA:442835 — *Non-specific early-onset epileptic encephalopathy* (CYFIP2 is listed as a causal gene under this umbrella; there is not yet a CYFIP2-specific ORPHA disease code distinct from this umbrella term as of current Orphanet indexing)
- **NCBI Gene:** CYFIP2 (Gene ID 26999)
- **UniProt:** Q96F07
- **Synonyms for the disease:** DEE65; CYFIP2-related neurodevelopmental disorder; CYFIP2 encephalopathy; (historically reported under) "early infantile epileptic encephalopathy" (EIEE)-spectrum, West syndrome with CYFIP2 mutation
- **Gene synonyms:** PIR121; p140Sra-1 (protein); the gene family member CYFIP1 (5q33 as well, MIM 606322) is distinct and causes a different phenotype spectrum

**Nature of the evidence base.** Essentially all published information is **aggregated case-series / cohort data** from clinical exome and genome sequencing referral cohorts (not registry- or claims-based epidemiology), supplemented by mechanistic functional studies (patient fibroblasts, heterologous cell expression, *Xenopus* tadpole and mouse knock-in models). There is no large population-based EHR cohort for this ultra-rare disorder.

Sources: [OMIM #618008](https://omim.org/entry/618008), [OMIM *606323](https://omim.org/entry/606323), [GeneCards CYFIP2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CYFIP2), [Orphanet CYFIP2](https://www.orpha.net/en/disease/gene/CYFIP2)

---

## 2. Etiology

**Disease causal factor.** DEE65 is a purely monogenic disorder — heterozygous, predominantly *de novo* pathogenic variation in *CYFIP2* is both necessary and sufficient to cause disease in essentially all reported cases. There is no established environmental, infectious, or multifactorial contribution to primary causation.

**Genetic risk factors:**
- **Mutational hotspot at Arg87 (p.Arg87Cys/Leu/Pro):** the dominant recurrent hotspot, identified in ~29–35% of published cases across cohorts ([Nakashima et al. 2018, PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/); [Zweier et al. 2019, PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/); [Begemann/Zweier et al. 2021, PMID:33149277, *Genet Med*](https://pubmed.ncbi.nlm.nih.gov/33149277/)). All reported Arg87 substitutions produce a **consistently severe** DEE phenotype.
- **Second hotspot at Asp724:** reported in 4/19 newly ascertained individuals in the 2021 cohort expansion, with a more variable/milder phenotype than Arg87 ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)): *"We report p.Asp724 as second mutational hotspot (4/19 cases). Genotype-phenotype correlation confirms a consistently severe phenotype in p.Arg87 patients but a more variable phenotype in p.Asp724 and other substitutions."*
- **Other missense variants** are distributed at additional interface residues within the CYFIP2–WAVE1/NCKAP1 tertiary structure — spatially clustered despite being scattered across the primary sequence ([Zweier et al. 2019, PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/)).
- **Putative loss-of-function variants** (truncating/frameshift) are rarer, reported in a small number of individuals with a **milder** phenotype, and their pathogenicity/mechanism remains less certain (haploinsufficiency vs. incidental finding) ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)).
- **Somatic/germline mosaicism** has not been systematically characterized but is plausible given the *de novo* origin pattern typical of DEE genes; no confirmed parental mosaicism case has been prominently reported in the literature surveyed.

**Environmental/lifestyle risk factors:** None established. This is a primary monogenic channelopathy/cytoskeletal disorder with no known toxin, infectious, or lifestyle contributor.

**Protective factors:** None specifically documented for CYFIP2 variants. No modifier alleles have been described in the literature to date.

**Gene-environment interactions:** Not applicable/not reported; the disorder's severity appears driven by variant type/location (genotype) rather than environmental modulation.

Sources: [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)

---

## 3. Phenotypes

### Core/near-universal features
| Phenotype | HPO suggestion | Onset | Frequency (reported cohorts) |
|---|---|---|---|
| Intellectual disability / global developmental delay | HP:0001249 (Intellectual disability) / HP:0001263 (Global developmental delay) | Apparent after seizure onset in most; normal development often reported before seizure onset | ~100% (universal across cohorts) |
| Seizures, drug-resistant, various types | HP:0001250 (Seizure) / HP:0031375 (Drug-resistant epilepsy) | First months–years of life, commonly <6 months | ~100% |
| Infantile spasms / West syndrome | HP:0011097 (Epileptic spasm) | Typically <12 months | Reported in a substantial subset, especially Arg87 carriers |
| Muscular hypotonia (generalized/truncal) | HP:0001252 (Hypotonia) | Neonatal/infantile | ~100% of the original 12-patient series had generalized/truncal hypotonia; 4/12 also had appendicular hypertonia ([PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/)) |
| Microcephaly | HP:0000252 (Microcephaly) | Postnatal, progressive in some | 8/12 in the original hotspot cohort ([PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/)) |
| Mild facial dysmorphism | HP:0001999 (Abnormal facial shape) | Congenital | Reported as "mild" in OMIM clinical description |

### Additional/variable features
- **Hyperkinetic/dyskinetic movements:** present in a meaningful minority — one recent case-series/literature review reports hyperkinetic movements in **17%** of pooled CYFIP2 patients ([Squire et al. 2025, *Ann Child Neurol Soc*](https://onlinelibrary.wiley.com/doi/10.1002/cns3.70036)).
- **Spasm-like/paroxysmal dystonic movements**, particularly around seizure onset (mirrored closely in the *Cyfip2^R87C^* mouse model).
- **EEG abnormalities:** hypsarrhythmia (in infantile-spasm presentations), multifocal epileptiform discharges.
- **Brain MRI:** frequently **normal or nonspecific** despite severe clinical phenotype — noted explicitly in a codon-87 case report: *"MRI findings showed no relevant changes despite severe clinical presentation"* ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)).
- **Impaired social communication / autistic features:** documented in patients and recapitulated in the *Cyfip2^R87C^* mouse (impaired ultrasonic vocalization, social interaction deficits) ([Kang et al. 2023, PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/)).
- **Poor visual fixation/pursuit, hyperreflexia, feeding difficulties (swallowing/tongue protrusion)** in severely affected infants ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)).
- **Developmental regression** after an initial period of relatively preserved development in some patients.

### Phenotype severity/progression pattern
- **Age of onset:** neonatal to early infantile (majority <6 months); OMIM states onset "usually within the first months or years of life."
- **Severity:** severe to profound in Arg87-hotspot carriers; more variable (mild–moderate to severe) in Asp724 and other missense/putative LOF carriers.
- **Course:** progressive/static mixture — seizures often intractable from onset; the mouse model shows a triphasic course (neonatal spasms → seizure-free interval → adult-onset spontaneous recurrent seizures), which may parallel an underrecognized human trajectory ([PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)).

### Quality of life impact
Severe global developmental impairment, drug-resistant epilepsy, and motor/communication deficits imply substantial lifelong caregiver burden and functional impairment; no disease-specific validated QOL instrument data were identified in the literature surveyed — QOL impact is inferred from the severe DEE clinical picture rather than directly measured (EQ-5D/SF-36/PedsQL data not located for this specific gene).

Sources: [OMIM #618008](https://omim.org/entry/618008), [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/), [Squire et al. 2025](https://onlinelibrary.wiley.com/doi/10.1002/cns3.70036)

---

## 4. Genetic/Molecular Information

**Causal gene:** *CYFIP2* (HGNC:13760; OMIM *606323; NCBI Gene 26999; UniProt Q96F07), chromosome 5q33.3. Transcript reference commonly used in ClinVar: NM_001037333.3.

**Pathogenic variant classes:**
- **Missense, gain-of-function (GOF)** — the dominant mechanism. Concentrated at two hotspots:
  - **p.Arg87Cys/Leu/Pro** (c.259C>T, c.260G>T, c.260G>C) — the most severe, most recurrent hotspot.
  - **p.Asp724** substitutions — second hotspot, milder/variable phenotype.
  - Additional scattered missense variants (e.g., in the original 12-patient EJHG cohort: 7 missense + 1 splice-donor variant) that cluster spatially at the CYFIP2–WAVE1/NCKAP1 interface in 3D structure despite linear sequence dispersion ([PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/)).
- **In-frame deletion:** e.g., c.258_266del; p.(Trp86_Ser88del), eliminating the Arg87 hotspot codon entirely ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)).
- **Putative loss-of-function (truncating) variants:** rare, associated with a comparatively milder phenotype; pathogenic significance still described as of "unclear pathogenicity" in the largest cohort study ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)).

**Variant classification (ACMG/AMP):** Missense hotspot variants (Arg87, Asp724) are classified Pathogenic/Likely Pathogenic in ClinVar (e.g., NM_001037333.3(CYFIP2):c.259C>T (p.Arg87Cys), [ClinVar RCV000656389](https://www.ncbi.nlm.nih.gov/clinvar/RCV000656389/)) based on de novo occurrence, absence from population databases, and concordant functional evidence.

**Allele frequency:** Pathogenic CYFIP2 variants are essentially **absent from gnomAD/population databases** — consistent with de novo occurrence and embryonic-lethal-adjacent severity of complete loss-of-function in model systems (see below).

**Origin:** Overwhelmingly **de novo germline**; no confirmed inherited transmission from an affected parent has been widely reported (consistent with reduced reproductive fitness in a severe pediatric-onset DEE).

**Functional consequences — mechanistic characterization:**
- CYFIP2 is an obligate structural subunit of the **WAVE regulatory complex (WRC)** (CYFIP1/2–NCKAP1–WASF/WAVE–ABI–BRK1), which in the resting state sequesters the VCA domain of WASF to keep the complex autoinhibited. **RAC1-GTP binding to CYFIP releases VCA**, triggering **Arp2/3-mediated actin polymerization** at the membrane.
- Disease variants — especially Arg87 — **weaken the CYFIP2–WAVE1 interface interaction**, releasing autoinhibition and driving **constitutive/enhanced WRC activation** — a **gain-of-function** mechanism at the level of actin regulation:
  > *"The structural analysis showed this residue is positioned at the interface between CYFIP2 and WAVE1, and the variants may disrupt hydrogen bonding, leading to structural instability... Mutant CYFIP2 demonstrated weaker binding to the VCA domain and caused increased actin accumulation in transfected cells, suggesting gain-of-function effects on WAVE signaling."* ([Nakashima et al. 2018, PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/))
- Patient fibroblast studies substantiate **aberrant regulation of the actin cytoskeleton**, confirming the cellular pathomechanism in primary patient-derived cells, not just heterologous overexpression systems ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)).
- A **second, independent mechanism** was identified for the Arg87Cys variant: it **enhances ubiquitination and proteasomal degradation of CYFIP2 protein**, reducing steady-state CYFIP2 levels in the brain — described in mouse and cellular models ([Kang et al. 2023, PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/); note a published exchange debating "reduced CYFIP2 stability" vs. gain-of-function interpretation exists in the literature — [ResearchGate summary of the reply](https://www.researchgate.net/publication/335768036_Reply_to_Reduced_CYFIP2_Stability_by_Arg87_Variants_Causing_Human_Neurological_Disorders)). A review notes: *"Almost all CYFIP2-derived mutations (7 out of 8) promoted WRC activation, but to variable extent and with at least two independent mechanisms"* — i.e., both interface-destabilization-driven WRC hyperactivation and reduced-protein-stability/increased-turnover mechanisms are represented across the mutational spectrum.
- **Not classical loss-of-function haploinsufficiency** for the hotspot variants — this is an important curatorial distinction from most other severe DEE genes, since the dominant disease mechanism is toxic gain-of-function/dysregulation rather than simple dosage reduction (contrast with the rarer, milder truncating-variant subset, which may act via haploinsufficiency).

**Modifier genes:** None specifically established.

**Epigenetics:** No CYFIP2-specific DNA methylation/chromatin signature has been reported in the literature surveyed. A related RNA-level regulatory mechanism (A-to-I RNA editing of CYFIP2 transcripts affecting actin regulation, axon growth, and spinogenesis) has been described as a separate area of investigation, distinct from the DEE-causing coding variants ([bioRxiv, RNA editing paper](https://www.biorxiv.org/content/10.1101/2025.03.04.641430.full.pdf)) — relevant to normal CYFIP2 biology rather than to DEE65 pathogenic variants specifically.

**Chromosomal abnormalities:** DEE65 is caused by single-nucleotide/small-indel variants, not large chromosomal rearrangements; no recurrent CNV mechanism has been described for this locus in the DEE65 literature (contrast: CYFIP1 sits within the 15q11.2 microdeletion region relevant to a *different* neurodevelopmental syndrome — not to be conflated with CYFIP2/5q33.3).

Ontology suggestions: **HGNC:13760** (CYFIP2); **GO:0071203** (WASP-family verprolin-homologous protein regulatory complex localization) / **GO:0034314** (Arp2/3 complex-mediated actin nucleation) / **GO:0030041** (actin filament polymerization); **CHEBI** not directly applicable to the protein itself.

Sources: [OMIM *606323](https://omim.org/entry/606323), [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/), [ClinVar RCV000656389](https://www.ncbi.nlm.nih.gov/clinvar/RCV000656389/)

---

## 5. Environmental Information

No environmental toxin, occupational exposure, radiation, or pollutant exposure has been implicated in CYFIP2-related DEE causation — it is a purely monogenic disorder. No lifestyle factors (maternal or infant) have been linked to onset or severity. No infectious trigger or agent is described in the literature; seizure precipitants in already-affected individuals (fever, illness) are not specifically documented for this gene in the sources reviewed (contrast with genes like SCN1A/CACNA1C where fever-triggered exacerbation is well characterized — no equivalent CYFIP2-specific finding was located).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** *De novo* heterozygous missense variant in *CYFIP2* (most commonly Arg87Cys/Leu/Pro) destabilizes the CYFIP2–WAVE1 (WASF1) interface within the pentameric WAVE Regulatory Complex, OR (Arg87Cys specifically) promotes CYFIP2 ubiquitination/proteasomal degradation.
2. **Molecular consequence:** Loss of normal autoinhibitory sequestration of the WASF VCA domain → **constitutive/enhanced release of VCA** → **aberrant, excessive activation of the Arp2/3 complex**.
3. **Cellular consequence:** **Dysregulated actin cytoskeleton dynamics** — increased/aberrant F-actin polymerization demonstrated directly in transfected cells and in patient-derived fibroblasts ([PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/); [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)). In neurons, CYFIP2/WRC signaling is essential for normal **dendritic spine morphogenesis, synaptic actin remodeling, axon growth, and BDNF-TrkB (NTRK2) endosomal trafficking/signaling** (per GeneCards functional annotation).
4. **Circuit-level consequence:** Disrupted synaptic actin dynamics and spine architecture are hypothesized to produce **neuronal hyperexcitability and aberrant network connectivity**, providing a plausible mechanistic bridge to the epilepsy phenotype; this is directly modeled functionally in the *Xenopus* tadpole system, where transient expression of GOF *cyfip2* mRNA (encoding pathogenic variants) is sufficient to cause **spontaneous epileptiform brain activity and seizure-associated behaviors** (rapid darting, circling swimming) — a direct causal (not merely correlative) demonstration that the GOF variant alone drives network hyperexcitability in vivo ([bioRxiv, DEE65 Xenopus model](https://www.biorxiv.org/content/10.1101/2022.12.07.519540v2)).
5. **Organismal/clinical consequence:** Seizures (often infantile spasms/West syndrome pattern), profound developmental delay, hypotonia progressing in some to hyperkinetic movement abnormalities, and microcephaly — the last plausibly reflecting a role for CYFIP2/actin dynamics in neural progenitor proliferation and cortical growth (supported by the Cyfip2-null mouse embryonic phenotype below).

**Cell types and biological processes involved:**
- **Cortical/hippocampal excitatory neurons** — actin-dependent dendritic spine and synapse remodeling (documented cytoarchitectural disorganization and gliosis in hippocampus of the *Cyfip2^R87C^* mouse — [PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/)).
- **Glial cells (astrocytes/microglia):** sequential/temporally staged glial activation (gliosis) accompanies seizure evolution in the mouse model, with **lipid droplet accumulation in astrocytes** and broad proteomic/lipidomic remodeling over the disease course ([PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)).
- **Neural progenitor cells / developing cortex:** Cyfip2-null mouse embryos show smaller body size, early postnatal lethality, and **cortical extracellular-matrix (ECM)-related gene expression changes**, though gross E18.5 brain size/cytoarchitecture were comparable to wild-type at that stage — implicating CYFIP2 in ECM-dependent aspects of cortical development ([PMC6338024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6338024/)).
- **Non-neuronal role (secondary):** CYFIP2/WRC has broader roles in membraneless organelle (stress granule, P-body, nucleolus) regulation and eIF2α phosphorylation/translational control, identified via CYFIP2-knockout forebrain proteomics — a newly characterized, actin-cytoskeleton-linked mechanism for translational regulation whose disease relevance is still emerging ([Cho et al. 2024, PMID:38981622](https://pubmed.ncbi.nlm.nih.gov/38981622/)).

**Molecular pathways:** WAVE regulatory complex / Arp2/3 actin nucleation pathway (Reactome: "RHO GTPase Effectors"; KEGG: regulation of actin cytoskeleton); RAC1-GTPase signaling upstream of WRC activation.

**Protein dysfunction category:** Predominantly **toxic gain-of-function / dysregulated activity** (constitutive WRC hyperactivation) rather than simple loss-of-function, distinguishing DEE65 mechanistically from many other DEE genes that act via straightforward haploinsufficiency; a minority of putative truncating variants may act via classical loss-of-function/haploinsufficiency with a correspondingly milder phenotype.

**Suggested ontology terms:**
- **GO (biological process):** GO:0030036 (actin cytoskeleton organization), GO:0034314 (Arp2/3 complex-mediated actin nucleation), GO:0051893 (regulation of focal adhesion assembly), GO:0007015 (actin filament organization)
- **GO (molecular function):** GO:0003779 (actin binding)
- **GO (cellular component):** GO:0071203 (WASP-family verprolin-homologous protein regulatory complex), GO:0030426 (growth cone), GO:0043197 (dendritic spine)
- **CL (cell types):** CL:0000679 (glutamatergic neuron) / CL:0000128 (oligodendrocyte, if relevant to white matter findings) / CL:0000127 (astrocyte)

Sources: [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/), [PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/), [PMC6338024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6338024/), [PMID:38981622](https://pubmed.ncbi.nlm.nih.gov/38981622/), [bioRxiv Xenopus model](https://www.biorxiv.org/content/10.1101/2022.12.07.519540v2)

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Primary:** Central nervous system (brain) — cerebral cortex, hippocampus.
- **Secondary:** Musculoskeletal system (hypotonia-related), craniofacial structures (mild dysmorphism, microcephaly reflecting reduced brain/skull growth).
- **Body systems involved:** Nervous system (primary); musculoskeletal (hypotonia); growth/development (microcephaly, failure to thrive in severe cases).

**Tissue/cell level:**
- Cerebral cortical neurons and hippocampal pyramidal neurons (cytoarchitectural disorganization documented in mouse model).
- Glial populations (astrocytes, microglia) showing reactive gliosis over disease course.
- Peripheral patient fibroblasts (used as an accessible surrogate tissue for demonstrating actin dysregulation in functional studies — not itself clinically affected, but mechanistically informative).

**Subcellular level:**
- Actin cytoskeleton / cortical actin network (GO:0015629 actin cytoskeleton).
- Dendritic spines / postsynaptic density (site of WRC-dependent spine actin remodeling).
- Growth cone (axon guidance/pathfinding, WRC-dependent).
- Proteasome (site of enhanced Arg87Cys protein degradation).

**Localization / laterality:** Diffuse, bilateral cerebral involvement (no lateralization reported); MRI is frequently structurally unremarkable despite severe functional/electrical involvement.

**UBERON suggestions:** UBERON:0000955 (brain), UBERON:0001954 (Ammon's horn/hippocampus), UBERON:0001851 (cortex).

Sources: [OMIM #618008](https://omim.org/entry/618008), [PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/), [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)

---

## 8. Temporal Development

- **Onset:** Congenital predisposition with clinical onset in the **neonatal-to-early-infantile period**; seizures most commonly begin within the **first 6 months of life** (OMIM), sometimes as early as the neonatal period. Development is often described as apparently normal *before* seizure onset in milder cases, with delay/regression becoming evident afterward.
- **Onset pattern:** Acute/subacute onset of seizures, often abrupt (spasms clusters), against a background of insidious developmental impairment.
- **Progression:** Predominantly **static-to-progressive** — seizures are frequently intractable from onset (refractory to multiple antiseizure medications, as documented in case reports trying levetiracetam, phenobarbital, vigabatrin, zonisamide, valproic acid, and ketogenic diet without seizure control — [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)). The mouse model reveals a more complex, **triphasic natural history**: neonatal spasm-like events → a seizure-free interval → adult-onset spontaneous recurrent seizures with progressive synaptic remodeling, gliosis, and premature death ([PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)) — raising the possibility of an analogous, currently underrecognized, evolving human natural history.
- **Disease duration:** Chronic, lifelong; DEE65 is not known to remit.
- **Remission:** No spontaneous remission pattern documented; some symptomatic improvement possible with combination antiseizure regimens in individual cases, but sustained pharmacoresistance is the norm.
- **Critical periods:** Early infancy appears to be a critical window for both seizure emergence and the steepest developmental impact, paralleling the well-established DEE/West-syndrome paradigm of early intervention urgency, though CYFIP2-specific intervention-timing data are not established.

Sources: [OMIM #618008](https://omim.org/entry/618008), [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/), [PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)

---

## 9. Inheritance and Population

**Epidemiology:** DEE65 is an **ultra-rare** disorder. As of the original 2018 discovery, only 4 individuals were reported; by the 2019 EJHG cohort, 12 patients; by the 2021 Genetics in Medicine cohort expansion, a cumulative total of **37 individuals** (19 newly reported + 18 previously published) ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)); a 2024–2025 systematic literature review/case report identified substantially more — **~41 additional patients**, with the Arg87Cys variant present in **12/42 (29%)** of one pooled analysis, and at least 27 additional distinct variants described across roughly 30 more patients ([Squire et al. 2025](https://onlinelibrary.wiley.com/doi/10.1002/cns3.70036)). No formal population-based incidence/prevalence rate (cases per 100,000) has been established — case counts reflect literature ascertainment via clinical exome/genome sequencing referral, not population screening.

**Inheritance pattern:** **Autosomal dominant**, virtually always due to a ***de novo*** variant.

**Penetrance:** Appears to be **complete** for the well-characterized hotspot variants (Arg87), based on the absence of reported unaffected carrier parents; penetrance/expressivity for milder putative loss-of-function variants is less certain.

**Expressivity:** **Variable**, correlated with variant identity — Arg87 substitutions show consistently severe expressivity; Asp724 and other missense variants show more heterogeneous, sometimes milder expressivity; putative LOF variants associate with the mildest reported phenotypes.

**Genetic anticipation:** Not applicable — this is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically documented as a recurrence mechanism in this gene's literature to date, though theoretically possible for any de novo dominant disorder (genetic counseling should still consider low recurrence risk from potential parental gonadal mosaicism, per general DEE counseling practice).

**Founder effects:** None reported — cases described in the literature span diverse ethnic/geographic backgrounds (original hotspot cohort included Japanese, Israeli, and Malaysian families; subsequent cohort recruited from Germany, France, UK, and elsewhere), consistent with recurrent independent de novo mutation at a true mutational hotspot rather than a single ancestral founder allele.

**Consanguinity:** Not a relevant risk factor given the dominant de novo mechanism.

**Carrier frequency:** Not applicable (dominant de novo disorder, not a recessive carrier state); population database allele frequency for pathogenic variants is essentially zero.

**Sex ratio:** No skewed sex ratio has been specifically reported; both male and female patients are represented in all major cohorts, and the *Cyfip2^R87C^* mouse model shows phenotypes in both sexes.

**Geographic distribution:** No endemic or regionally restricted distribution; cases have been reported globally (East Asia, Middle East, Southeast Asia, Western Europe).

Sources: [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [Squire et al. 2025](https://onlinelibrary.wiley.com/doi/10.1002/cns3.70036)

---

## 10. Diagnostics

**Clinical/laboratory tests:** No CYFIP2-specific biomarker or biochemical assay exists; routine metabolic/biochemical workup in suspected DEE is typically used to exclude alternative etiologies rather than to positively diagnose CYFIP2-DEE.

**Electrophysiology:** **EEG** is central to diagnosis and phenotyping — documenting hypsarrhythmia (in spasms presentations), multifocal epileptiform discharges, and background abnormalities consistent with an encephalopathic process. LOINC-coded EEG procedures apply generically (no CYFIP2-specific EEG signature established).

**Imaging:** **Brain MRI** is typically performed to exclude structural lesions; findings are frequently **normal or nonspecific** even in severely affected patients ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)) — an important diagnostic point (a normal MRI does not exclude CYFIP2-DEE).

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES)** or **whole genome sequencing (WGS)**, typically as trio (proband + parents) analysis, is the standard diagnostic approach, since CYFIP2-DEE was itself discovered via de novo variant discovery in WES cohorts of unexplained early-onset epileptic encephalopathy ([PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/); [PMID:30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/)).
- **Gene panels** for epileptic encephalopathy / early-infantile epilepsy (e.g., commercial DEE panels, the Genomics England PanelApp "Epileptic encephalopathy" panel, which lists CYFIP2 — [PanelApp CYFIP2](https://panelapp.genomicsengland.co.uk/panels/67/gene/CYFIP2/)) include CYFIP2 and are a reasonable first-tier test given the recognizable phenotype.
- **Single-gene (Sanger) testing** is appropriate for targeted confirmation once a candidate variant is identified by broader sequencing, or for recurrence-risk testing in future pregnancies (to exclude/confirm rare parental mosaicism).
- Chromosomal microarray (CMA) and karyotyping are **not** primary diagnostic tools for this disorder (single-nucleotide variant mechanism, not CNV-based), though they are often performed as part of standard first-tier DEE/ID workup to exclude other etiologies.
- **Mitochondrial DNA testing / repeat-expansion testing:** not relevant to this specific gene.

**Clinical diagnostic criteria:** No formal consensus clinical diagnostic criteria specific to CYFIP2-DEE exist; diagnosis follows the general DEE/ILAE framework (early-onset seizures + developmental impairment disproportionate to seizures alone, when applicable) combined with molecular confirmation, since the phenotype alone is not sufficiently distinctive to establish diagnosis without genetic testing.

**Differential diagnosis:** Other genetic DEEs presenting with infantile spasms/West syndrome and severe ID (e.g., *STXBP1*, *KCNQ2*, *SCN2A*, *CDKL5*, *ARX* [causing OMIM DEE1, a distinct entity from CYFIP2's DEE65 despite similar naming], and other WAVE-complex-adjacent genes such as *NCKAP1*, *ACTB/ACTG1*) should be considered and are typically distinguished only by molecular testing given phenotypic overlap.

**Screening:** No population-based newborn or carrier screening applies (ultra-rare, de novo dominant disorder); prenatal testing is possible in a family with a previously identified pathogenic variant (targeted testing for future pregnancies), though the near-universal de novo mechanism limits its practical yield outside of confirmed parental mosaicism.

Sources: [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/), [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/), [PanelApp CYFIP2](https://panelapp.genomicsengland.co.uk/panels/67/gene/CYFIP2/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics (5-/10-year survival) have been published for the human disorder; the condition is not classically described as directly life-limiting in early reports, though severe DEEs of this type carry recognized SUDEP (sudden unexpected death in epilepsy) risk in general, and the mouse model shows **premature death** associated with progressive adult-onset seizures and neuroinflammation — a signal that warrants clinical vigilance even though it has not yet been formally quantified in human cohorts ([PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)).

**Morbidity/function:** Severe to profound intellectual disability and motor impairment are the norm in Arg87-hotspot carriers; more variable functional outcomes (mild–moderate ID) occur with Asp724/other missense or putative LOF variants. No standardized disability outcome measure (e.g., ICF-based) has been systematically applied across cohorts in the literature reviewed.

**Complications:** Drug-resistant epilepsy with attendant risks (injury, aspiration in severe cases, medication side effects from polytherapy); failure to thrive/growth impairment in the most severely affected; secondary orthopedic complications from chronic hypotonia/hypertonia are plausible but not specifically quantified in the sources reviewed.

**Recovery potential:** Given the drug-resistant nature of seizures across nearly all reported cases (multiple standard and dietary therapies failing in individual case reports), and the fixed neurodevelopmental impairment pattern, recovery to a mild phenotype is not typical for hotspot (Arg87) variant carriers; the milder end of the spectrum (Asp724, other missense, putative LOF variants) offers somewhat better functional prognosis.

**Prognostic factors:** **Variant identity is the strongest known prognostic factor** — Arg87 substitutions predict a consistently severe DEE course; Asp724 and other substitutions predict a more variable course; putative loss-of-function variants predict the mildest reported phenotypes ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)). No independent biomarker-based prognostic tool exists.

Sources: [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/), [PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/)

---

## 12. Treatment

**Pharmacotherapy (symptomatic/standard-of-care only — no CYFIP2-targeted approved drug exists):**
- Standard antiseizure medications have been trialed empirically and are frequently **ineffective** individually: levetiracetam, phenobarbital, vigabatrin (a first-line agent for infantile spasms generally), zonisamide, valproic acid — documented as failing to control seizures in a codon-87 case report despite combination use ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)). ACTH/corticosteroid therapy (standard for infantile spasms broadly) is presumably trialed in spasms-presenting cases per general West syndrome practice, though CYFIP2-specific response data were not located in the sources reviewed.
- **Ketogenic diet** has been tried as an adjunct in at least one reported case without achieving seizure freedom ([PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/)).
- **NCIT suggestion:** NCIT:C15986 (Pharmacotherapy) as the generic treatment_term, with specific agents captured via `therapeutic_agent` (e.g., CHEBI terms for levetiracetam, valproic acid, vigabatrin, phenobarbital, zonisamide).
- **Dietary intervention:** NCIT:C15447 (Dietary Intervention) for the ketogenic diet.

**Precision/targeted therapy:** No CYFIP2-specific precision therapeutic has been developed or trialed to date. Because the dominant mechanism is **toxic gain-of-function WRC hyperactivation** (analogous conceptually to other GOF-driven DEEs where targeted pharmacology has succeeded, e.g., quinidine for *KCNT1*-GOF epilepsy, memantine for *GRIN2D*-GOF epilepsy), CYFIP2-DEE is a plausible future candidate for genotype-informed precision approaches (e.g., agents modulating Rac1/WRC/Arp2/3 signaling), but this remains **speculative/preclinical** — no clinical trial or case report of a targeted small molecule was identified. A general review of precision epilepsy therapeutics frames this class of gene (defined mechanism, amenable pathway) as a priority area for future targeted drug development ([Byrne et al. 2021, PMID:34089185](https://pubmed.ncbi.nlm.nih.gov/34089185/)).

**Gene/RNA-based therapy:** No CYFIP2-specific gene therapy, ASO, or siRNA approach has reached even preclinical proof-of-concept publication in the literature surveyed, though the *Xenopus* GOF model system provides a tractable platform on which future suppression/knockdown strategies (e.g., allele-specific ASO knockdown of the mutant transcript, analogous to strategies used for other dominant GOF DEE genes) could in principle be tested.

**Surgical/interventional:** Not applicable as a primary treatment (no known epileptogenic focal lesion amenable to resection; this is a diffuse genetic encephalopathy).

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, and speech/communication therapy are standard supportive measures for the hypotonia, motor impairment, and communication deficits characteristic of severe DEE, per general DEE management practice (NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation).

**Experimental/clinical trials:** No CYFIP2-DEE-specific registered clinical trial was identified via the sources reviewed (searches did not surface an NCT-registered CYFIP2-targeted trial).

**Treatment outcomes:** As above, existing case reports document **refractory epilepsy** despite multi-drug and dietary intervention — the treatment picture at present is one of largely unmet need for a mechanism-based therapy.

Sources: [PMC10038648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10038648/), [Byrne et al. 2021, PMID:34089185](https://pubmed.ncbi.nlm.nih.gov/34089185/)

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy exists for CYFIP2-DEE, given its near-universal *de novo* origin (not preventable through risk-factor modification, vaccination, or population screening). The applicable preventive interventions are:

- **Genetic counseling:** for parents of an affected child, to communicate the generally low (but not zero, due to possible germline mosaicism) empiric recurrence risk for future pregnancies, and to discuss options such as targeted prenatal or preimplantation genetic testing once the familial variant is known (NCIT:C15240 Genetic Counseling).
- **Prenatal diagnosis:** feasible only in a family with an already-identified pathogenic variant (e.g., via amniocentesis/CVS with targeted variant testing), not as population-level screening.
- **Early intervention services:** while not preventing the underlying disorder, early developmental/rehabilitative intervention following diagnosis is standard practice to optimize functional outcomes in severe pediatric DEEs generally.

No public-health-level, environmental, or behavioral prevention measures apply, consistent with the disorder's purely monogenic de novo etiology.

---

## 14. Other Species / Natural Disease

**Taxonomy of models used:** *Mus musculus* (NCBITaxon:10090); *Xenopus laevis* (NCBITaxon:8355).

**Orthologous gene:** Mouse *Cyfip2* (MGI ortholog of human CYFIP2); highly conserved across vertebrates given the essential, ancient function of the WAVE regulatory complex in actin regulation.

**Naturally occurring disease in other species:** No naturally occurring (spontaneous) CYFIP2-associated disease has been reported in companion animals or wildlife in the sources reviewed (no OMIA entry surfaced) — all non-human disease models identified are **engineered** (knock-in/knockout or induced mRNA overexpression), not naturally arising veterinary conditions.

**Comparative biology:** The WAVE regulatory complex and its Arp2/3-actin-nucleation function are deeply conserved from *Xenopus* through mammals, which is precisely why the transient mRNA-overexpression *Xenopus* tadpole system and the mouse knock-in system both successfully recapitulate core aspects of the human phenotype (seizures, developmental/behavioral abnormalities) — supporting strong evolutionary conservation of the underlying disease mechanism.

**Zoonotic/transmission relevance:** Not applicable — this is a non-communicable monogenic disorder.

Sources: [Kang et al. 2023, PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/), [bioRxiv Xenopus model](https://www.biorxiv.org/content/10.1101/2022.12.07.519540v2)

---

## 15. Model Organisms

### Mouse models
1. **`Cyfip2^+/R87C^` knock-in mouse (heterozygous, patient-matched hotspot variant)** — the flagship disease model.
   - *Recapitulation:* *"Cyfip2+/R87C mice recapitulated many neurological and neurobehavioral phenotypes of the patients, including spasmlike movements, microcephaly, and impaired social communication."* Specific findings: neonatal spasm-like behavior, developmental regression, muscular hypotonia, microcephaly in early life; adult mice show **hyperlocomotion**, impaired social interaction, and defective ultrasonic vocalization ([Kang et al. 2023, PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/)).
   - *Molecular mechanism confirmed in vivo:* enhanced ubiquitination/proteasomal degradation of CYFIP2 protein, reducing brain CYFIP2 levels.
   - *Neuropathology:* age-progressive hippocampal cytoarchitectural disorganization and gliosis.
   - *Longitudinal natural history (follow-on study):* triphasic seizure evolution (neonatal spasms → seizure-free interval → adult spontaneous recurrent seizures → premature death), with time-dependent synapse remodeling, sequential glial activation, astrocytic lipid droplet accumulation, and significant proteomic/lipidomic brain changes across the disease course ([PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/); related preprint: [bioRxiv longitudinal deep phenotyping](https://www.biorxiv.org/content/10.1101/2025.05.06.652352.full.pdf)).
   - *Fidelity:* High for spasm-like movements, microcephaly, and social/behavioral deficits; the mouse additionally reveals an adult-onset seizure phase not yet systematically documented in humans, raising a **HUMAN_MODEL_MISMATCH**-type open question about whether the human natural history includes an analogous later-life seizure evolution that is currently underrecognized due to limited longitudinal follow-up of patients.

2. **`Cyfip2^-/-^` (null/knockout) mouse** — models complete loss of function (distinct from the disease-causing GOF hotspot alleles; useful for understanding baseline CYFIP2 developmental biology).
   - *Phenotype:* Smaller embryonic body size; embryos survive to E18.5 with grossly comparable brain size/cortical cytoarchitecture to wild-type/heterozygous littermates at that stage, but **all Cyfip2−/− pups are found dead at postnatal day 0** (early postnatal, not embryonic, lethality). Cortical extracellular-matrix (ECM)-related gene expression changes are identified in the null embryonic cortex ([PMC6338024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6338024/)).
   - *Relevance:* Establishes that **complete biallelic loss of CYFIP2 is not viable postnatally**, reinforcing that the milder human phenotypes associated with putative (heterozygous) loss-of-function variants reflect partial haploinsufficiency rather than complete pathway loss, and underscoring that the disease-causing mechanism for the severe human phenotype (Arg87 etc.) is mechanistically distinct from simple loss-of-function.

### Non-mammalian model
3. **`Xenopus laevis` tadpole, transient mRNA overexpression of GOF *cyfip2* variants** — a rapid, tractable in vivo system.
   - *Approach:* Ectopic expression of pathogenic-variant-encoding mRNA (including an Arg87Cys-equivalent variant) directly in tadpoles.
   - *Findings:* Sufficient on its own to cause **spontaneous epileptiform brain electrical activity** and seizure-associated behaviors (rapid darting, circular swimming, increased agitation) — providing strong causal (not just correlative) evidence that the GOF mutant protein, expressed transiently and ectopically, is sufficient to generate a seizure phenotype ([bioRxiv, DEE65 Xenopus model](https://www.biorxiv.org/content/10.1101/2022.12.07.519540v2)).
   - *Fidelity/limitations:* High construct-validity for demonstrating GOF sufficiency and rapid electrophysiological/behavioral seizure readouts; lower face-validity for modeling the full chronic developmental/cognitive phenotype given the amphibian system and transient (non-genomic, mosaic) expression paradigm — a **HUMAN_MODEL_MISMATCH** consideration for any curated entry using this model.

### Cellular/in vitro models
4. **Patient-derived dermal fibroblasts** — used to demonstrate aberrant actin cytoskeleton regulation directly in human cells carrying the endogenous heterozygous variant, substantiating that the WRC-dysregulation mechanism operates in patient tissue, not only in heterologous overexpression systems ([PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/)).
5. **Heterologous transfected cell lines** (e.g., COS/HEK-type systems) — used in the original discovery study to demonstrate weakened CYFIP2–VCA/WAVE1 binding and increased aberrant F-actin accumulation for the Arg87 hotspot variants ([PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/)).
6. **iPSC-derived human neuronal model (R87C)** — a more recent addition assessing the R87C variant's impact in a human neuronal context in vitro ([Impact of the CYFIP2 R87C variant in a human neuronal model in vitro, *Sci Rep*](https://www.nature.com/articles/s41598-026-44176-2)) — relevant for MorPhiC-style cellular phenotype curation if applicable.

**Model databases:** MGI (mouse *Cyfip2* allele records), Xenbase (for *Xenopus* Cyfip2), IMPC (if a systematic *Cyfip2* knockout line has been phenotyped — not confirmed in sources reviewed).

Sources: [PMID:36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/), [PMC12520403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12520403/), [PMC6338024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6338024/), [bioRxiv Xenopus model](https://www.biorxiv.org/content/10.1101/2022.12.07.519540v2), [PMID:33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/), [PMID:29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/)

---

## Summary of Key Primary Literature for Curation

| PMID/ID | First author, Year, Journal | Contribution |
|---|---|---|
| [29534297](https://pubmed.ncbi.nlm.nih.gov/29534297/) | Nakashima et al., 2018, *Ann Neurol* | First description of CYFIP2 Arg87 de novo hotspot in 4 patients; establishes GOF mechanism |
| [30664714](https://pubmed.ncbi.nlm.nih.gov/30664714/) | Zweier et al., 2019, *Eur J Hum Genet* | 12-patient cohort; spatial clustering of variants at WRC interface |
| [33149277](https://pubmed.ncbi.nlm.nih.gov/33149277/) | Begemann/Zweier et al., 2021, *Genet Med* | 37-patient cumulative cohort; identifies Asp724 second hotspot; fibroblast functional data; genotype-phenotype correlation; LOF-variant subset |
| [36251395](https://pubmed.ncbi.nlm.nih.gov/36251395/) | Kang et al., 2023, *Ann Neurol* | Cyfip2+/R87C mouse knock-in model; degradation mechanism |
| PMC12520403 | Guo et al. (longitudinal follow-up) | Mouse model natural history: triphasic seizure evolution, gliosis, lipidomics |
| PMC6338024 | 2018, *Front Mol Neurosci* | Cyfip2-null mouse: postnatal lethality, ECM gene expression |
| bioRxiv 2022.12.07.519540 | — | Xenopus GOF model: sufficiency for spontaneous seizures |
| [38981622](https://pubmed.ncbi.nlm.nih.gov/38981622/) | Cho et al., 2024 | CYFIP2 role in membraneless organelles/eIF2α regulation |
| PMC10038648 | Cureus case report | Codon-87 in-frame deletion case; treatment-refractory course; normal MRI |
| Squire et al. 2025, [Ann Child Neurol Soc](https://onlinelibrary.wiley.com/doi/10.1002/cns3.70036) | — | Most recent systematic literature review expanding phenotype spectrum |
| [34089185](https://pubmed.ncbi.nlm.nih.gov/34089185/) | Byrne et al., 2021, *Dev Med Child Neurol* | General precision-therapy framework relevant to future CYFIP2-targeted treatment |

**Note on evidence-quality caveats for curation:** Several full-text sources (OMIM clinical synopsis, Nature/Genetics in Medicine, and one bioRxiv PDF) returned HTTP 403/429/cookie-wall errors during this research session and could not be directly fetched verbatim; the corresponding content above was reconstructed from search-engine-indexed summaries and abstract text retrieved via PubMed/NCBI eutils, cross-checked across multiple independent sources where possible. **Before using any PMID/snippet pair from this report in a dismech KB entry, run `just fetch-reference` and `just count-verified-snippets` per the standard SOP** to confirm exact-quote fidelity against the authoritative cached abstract, since some quoted fragments above were extracted via an intermediary summarization step rather than direct verbatim page retrieval.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.