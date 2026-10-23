---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-04T03:20:51.913451'
end_time: '2026-10-04T03:21:49.984047'
duration_seconds: 58.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Opioid Poisoning
  mondo_id: MONDO:0018173
  category: Toxic Exposure Disorder
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8212122
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Opioid Poisoning
- **MONDO ID:** MONDO:0018173 (if available)
- **Category:** Toxic Exposure Disorder

## Research Objectives

Please provide a comprehensive research report on **Acute Opioid Poisoning** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# Acute Opioid Poisoning (MONDO:0018173): Research Report

**Verification status.** I ran three web searches in this session. Only these sources were actually retrieved:
- PMID:35965031 (OIRD pathophysiology review, from its PubMed URL)
- PMC8997313 and PMC8424565 (titles not shown in the results)
- Frontiers in Neuroscience 2023, doi:10.3389/fnins.2023.1134842
- CDC provisional overdose figures, as relayed by news outlets
- The intranasal naloxone and nalmefene results

Everything else is background knowledge, labelled **[unverified]**. It has no PMID and no snippet. Do not use any claim in this report as an evidence item until the reference is fetched with `just fetch-reference`. Ontology term names are given without CURIEs on purpose. Each needs a lookup (`runoak` or the term caches) before binding. The MONDO ID is as supplied in the template, and I did not check it.

## 1. Disease Information

Acute opioid poisoning is a toxic exposure disorder. An excess dose of an opioid agonist, or a dose that exceeds the person's tolerance, suppresses central respiratory drive and consciousness. The result is hypoventilation, hypoxia, and death if untreated. Opioids involved include heroin, illicit fentanyl and its analogues, methadone, oxycodone, morphine, and others.

- **Proximal cause of death:** the review "The pathophysiology of opioid-induced respiratory depression" ([PMID:35965031](https://pubmed.ncbi.nlm.nih.gov/35965031/)) and related results describe respiratory depression as the proximal cause of death in opioid overdose.
- **Identifiers:** ICD-10 T40.0–T40.4 and T40.6 (poisoning), with X/Y intent codes **[unverified]**. MeSH "Opiate Overdose" **[unverified]**. No OMIM or Orphanet entry is expected.
- **Synonyms:** opioid overdose, narcotic overdose, opiate intoxication, opioid toxidrome.
- **Data level:** this is an aggregate, disease-level concept. Surveillance data come from death certificates and ED visits.

## 2. Etiology

- **Causal factor:** an exposure to an opioid agonist that exceeds the patient's tolerance.
  - Illicit fentanyl is the dominant driver in the US. Synthetic-opioid deaths rose to about 76,282 in 2023 ([CDC data via news summary](https://www.yahoo.com/news/us-drug-overdose-deaths-fell-143131058.html)).
  - Other routes are prescription misuse, therapeutic error, pediatric accidental ingestion, and polysubstance use.
- **Risk factors [unverified]:**
  - Loss of tolerance after abstinence, for example after release from prison or detox.
  - Concurrent benzodiazepine, alcohol, or other CNS-depressant use.
  - Using alone, injection use, high prescribed dose, and respiratory or hepatic disease.
  - Contamination of the drug supply.
- **Genetic factors:** none are causal. Pharmacogenomic variation in CYP2D6, CYP3A4, and OPRM1 may modulate individual risk **[unverified]**.
- **Tolerance:** tolerance to respiratory depression is less than complete and may develop more slowly than tolerance to euphoria. This is one reason experienced users are at relatively high overdose risk ([search result summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8997313)).
- **Protective factors:**
  - Take-home naloxone and bystander presence.
  - Medication for opioid use disorder (buprenorphine, methadone).
  - Supervised consumption sites **[unverified]**.

## 3. Phenotypes

The classic opioid toxidrome is:
- Depressed consciousness.
- Respiratory depression (bradypnea or apnea).
- Miosis (pinpoint pupils).
- Hypoxemia and cyanosis.

Candidate phenotype terms to look up in HPO: coma/stupor, hypoventilation, apnea, bradypnea, miosis, cyanosis, bradycardia, hypotension, hypothermia, hypercapnia, respiratory acidosis, seizures (e.g. with tramadol or meperidine), muscle rigidity (e.g. fentanyl chest-wall rigidity), pulmonary edema, aspiration, rhabdomyolysis, anoxic brain injury.

- **Onset:** acute, within minutes after IV or inhaled use and within hours after oral use **[unverified]**.
- **Course:** episodic. Severity is dose-dependent and the course is fluctuating, with possible recurrence of toxicity after naloxone wears off.
- **Frequencies:** not reliably available. Fetch authoritative case-series data before assigning any percentages.
- **Quality of life:** survivors may have hypoxic brain injury, but I found no sourced data.

## 4. Genetic/Molecular Information

- No causal genes.
- **Pharmacological targets:** OPRM1 (hgnc-bound, lowercase `hgnc:` form; look up the ID), with additional OPRD1 and OPRK1 activity.
- **Metabolizing enzymes:** CYP3A4 (fentanyl), CYP2D6 (codeine, oxycodone), UGT2B7 (morphine).
- **Epigenetic and chromosomal findings:** none relevant.

## 5. Environmental Information

- **Exposures:** heroin, illicit fentanyl and its analogues, nitazenes, diverted prescription opioids.
- **Lifestyle factors:** injection drug use and polysubstance use. Alcohol and benzodiazepines are potentiators.
- **Infectious agents:** none are causal. Injection use carries secondary infection risk.
- **ECTO exposure terms:** search ECTO for opioid, heroin, and fentanyl exposure terms. Do not assume a term exists or doesn't. Re-run the searches before writing any note.

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. Opioid exposure at a dose above tolerance leads to high receptor occupancy of the mu-opioid receptor (MOR). Opioids produce inhibition at the chemoreceptors via mu opioid receptors and in the medulla via mu and delta receptors ([search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8997313)).
2. MOR is a Gi/o-coupled GPCR. Activation reduces cAMP and opens GIRK channels, causing hyperpolarization. It also closes voltage-gated Ca²⁺ channels, reducing neurotransmitter release **[unverified]**.
3. Neurons in the preBötzinger complex and in the parabrachial/Kölliker-Fuse pontine respiratory groups are inhibited **[unverified]**. Normal breathing requires the integration of rhythmogenic, modulatory, and sensory feedback mechanisms, and overdose can suppress all of them ([search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8997313)).
4. Chemoreflex responses to hypercapnia and hypoxia are blunted, so rate and tidal volume fall and the airway may be obstructed by loss of tone.
5. Hypoventilation causes hypercapnia, respiratory acidosis, and hypoxemia.
6. Hypoxemia leads to hypoxic-ischemic injury (brain, heart), arrhythmia, and cardiac arrest. This step is inferred from general physiology and not demonstrated in a retrieved source.
7. Branches:
   - Fentanyl-induced chest-wall rigidity may impair ventilation **[unverified]**.
   - Aspiration and non-cardiogenic pulmonary edema are described complications **[unverified]**.
   - Co-ingested sedatives add GABA-A potentiation, which is synergistic.

Candidate GO processes to look up: G protein-coupled opioid receptor signaling, regulation of respiratory rhythm / control of breathing, adenylate cyclase inhibition, regulation of membrane potential. Candidate cell types in CL: neurons of the preBötzinger complex (likely best bound as a generic neuron or respiratory-center neuron term), and carotid body glomus cells.

Omics and model-system sections (transcriptomics, proteomics, single-cell, etc.): none were found or searched. They are not applicable at this point.

## 7. Anatomical Structures Affected

- **Primary:** brainstem respiratory centres (medulla, pons), cerebral cortex (sedation), and peripheral chemoreceptors (carotid body).
- **Secondary:**
  - Lungs (aspiration, edema).
  - Heart (hypoxic arrhythmia).
  - Brain (anoxic injury).
  - Kidney (rhabdomyolysis).
  - GI tract (reduced motility).
- **Laterality:** bilateral and systemic.
- **Subcellular localization:** plasma membrane (receptor).

## 8. Temporal Development

- Onset is acute, from minutes to hours.
- It is self-limited if the person survives. Duration tracks opioid pharmacokinetics. Naloxone's duration is roughly 30–120 minutes ([search summary](https://www.2minutemedicine.com/?p=17080)), which can be shorter than a long-acting opioid's effect and allow re-sedation.
- Critical period: the minutes after apnea begins, when reversal is most effective. Brain injury accumulates with hypoxia time.

## 9. Inheritance and Population

- **Inheritance:** not applicable (non-genetic).
- **Epidemiology (US, CDC provisional data via news reports; the primary CDC pages were not fetched):**
  - All drug overdose deaths fell from 110,037 in 2023 to 80,391 in 2024, a 26.9% decline ([source](https://www.yahoo.com/news/us-drug-overdose-deaths-fell-143131058.html)).
  - Synthetic-opioid deaths fell from 76,282 to 48,422 over the same period.
  - In 2025, deaths fell a further ~14% to about 69,973. Opioid-involved deaths were about 44,564, down from 55,296 ([source](https://www.marketscreener.com/news/us-drug-overdose-deaths-dropped-for-third-straight-year-in-2025-cdc-data-shows-ce7f5bdcdb80ff24)).
  - CDC attributes the decline in part to naloxone distribution and treatment access.
- **Demographics:** the sex ratio is male-predominant (about 2:1) **[unverified]**. Peak ages are 25–54 **[unverified]**. Geography and ethnicity vary; check CDC WONDER.
- **Encoding for the KB:** use `measure_type: ANNUAL_INCIDENCE` with a `rate_denominator`, and avoid a qualitative prevalence tier. Convert only from the primary CDC source.

## 10. Diagnostics

- **Clinical diagnosis:** the toxidrome of coma, respiratory depression, and miosis, with response to naloxone as a diagnostic aid.
- **Labs:** blood gas (hypercapnia, acidosis), glucose, CK, ECG, co-ingestant screens. Urine immunoassays often miss fentanyl and nitazenes, so use specific confirmation **[unverified]**.
- **Imaging:** CXR for aspiration or edema; CT/MRI if anoxic injury is suspected.
- **Differential:** other sedative-hypnotic and alpha-2 agonist toxicity, hypoglycemia, stroke, postictal state, sepsis, hypothermia.
- Genetic testing and screening are not applicable.

## 11. Outcome/Prognosis

- Prognosis depends on speed of reversal and the duration of hypoxia.
- Complications: anoxic brain injury, aspiration pneumonia, rhabdomyolysis, compartment syndrome, post-reversal pulmonary edema. All are **[unverified]**.
- Nonfatal overdose strongly predicts later overdose death **[unverified]**.
- Fatality is dominated by synthetic opioids, as in the CDC figures above.
- Quantitative survival and prognostic-factor data were not retrieved.

## 12. Treatment

- **Airway and ventilation** (bag-mask ventilation, oxygen) are first-line. This is an established principle, but no source was fetched. Candidate NCIT clinical-intervention terms: supportive care (look up) and artificial or mechanical ventilation.
- **Naloxone** is the competitive MOR antagonist.
  - Higher-concentration (2 mg/mL) intranasal naloxone has similar efficacy to IM naloxone. The odds of needing a rescue dose were 2.17 times higher with intranasal than IM/IV ([search result](https://www.drugsandalcohol.ie/32293/)).
  - Encode as pharmacotherapy (NCIT:C15986, from the repo guidance) with a therapeutic agent. Look up naloxone in CHEBI.
- **Nalmefene:** intranasal nalmefene (Opvee) was FDA-approved in May 2023. It has a longer duration of action than naloxone ([UIC summary](https://dig.pharmacy.uic.edu/faqs/2024-2/may-2024-faqs/what-are-the-differences-in-efficacy-and-safety-of-intranasal-naloxone-versus-nalmefene)).
- **Risks:** naloxone can precipitate withdrawal in dependent patients. Observation is needed for re-sedation, especially with long-acting opioids **[unverified]**.
- **Experimental:** none retrieved. A ClinicalTrials.gov search is pending.
- **Long-term treatment:** medication for opioid use disorder (buprenorphine, methadone, naltrexone) is a secondary-prevention measure **[unverified]**.

## 13. Prevention

- **Primary:** safe opioid prescribing and the reduction of illicit supply.
- **Secondary:** take-home naloxone, MOUD initiation, and fentanyl test strips and drug checking **[unverified]**.
- **Tertiary:** post-overdose outreach and linkage to care.
- **Public health:** naloxone distribution is credited by CDC, in part, for the decline in deaths ([source](https://www.marketscreener.com/news/us-drug-overdose-deaths-dropped-for-third-straight-year-in-2025-cdc-data-shows-ce7f5bdcdb80ff24)).
- Immunization (e.g. fentanyl vaccines) is investigational. I did not find a source.

## 14. Other Species / Natural Disease

- Opioid toxicosis occurs in dogs, cats, and horses, most often through accidental ingestion **[unverified]**. Naloxone is used in veterinary practice **[unverified]**.
- Not zoonotic.
- Look up NCBITaxon IDs for dog (*Canis lupus familiaris*) and others at curation time.
- Comparative physiology: respiratory depression is conserved across mammals. Mu-opioid receptor pharmacology is broadly conserved. No source was retrieved.

## 15. Model Organisms

- **Rodent (mouse, rat):**
  - Opioid-induced respiratory depression is measured by plethysmography and blood-gas analysis. Genetic models include MOR knockout, which is protected from OIRD **[unverified]**.
  - Brainstem-slice preparations are used to study the preBötzinger complex **[unverified]**.
- **Limitations:** rodents differ from humans in dose, tolerance, and polysubstance patterns. Fidelity and divergences should be recorded per link (`modeled_mechanisms`) when curated.
- **Resources:** MGI, IMPC. Not searched.
- A review of OIRD pathophysiology is available at the [Frontiers in Neuroscience 2023 article](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1134842/full), which I found but did not read.

## Curation Next Steps

1. Run `just fetch-reference` for PMID:35965031 and any other primary papers you intend to cite.
2. Take exact snippets from the cached files only.
3. Look up every ontology term (HPO, GO, CL, UBERON, CHEBI, NCIT, ECTO) with `runoak` or the term caches.
4. Get the primary CDC pages (WONDER, NCHS VSRR) for epidemiology.
5. Search for sourced frequencies, prognosis, and mortality data, which are currently missing.

## Sources

- [PubMed: pathophysiology of opioid-induced respiratory depression (PMID:35965031)](https://pubmed.ncbi.nlm.nih.gov/35965031/)
- [PMC8997313](https://pmc.ncbi.nlm.nih.gov/articles/PMC8997313)
- [PMC8424565](https://pmc.ncbi.nlm.nih.gov/articles/PMC8424565)
- [Frontiers in Neuroscience 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1134842/full)
- [CDC 2024 overdose data, news summary](https://www.yahoo.com/news/us-drug-overdose-deaths-fell-143131058.html)
- [CDC 2025 overdose data, news summary](https://www.marketscreener.com/news/us-drug-overdose-deaths-dropped-for-third-straight-year-in-2025-cdc-data-shows-ce7f5bdcdb80ff24)
- [Intranasal vs IM/IV naloxone summary](https://www.drugsandalcohol.ie/32293/)
- [Intranasal naloxone vs nalmefene (UIC)](https://dig.pharmacy.uic.edu/faqs/2024-2/may-2024-faqs/what-are-the-differences-in-efficacy-and-safety-of-intranasal-naloxone-versus-nalmefene)
- [2 Minute Medicine](https://www.2minutemedicine.com/?p=17080)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.