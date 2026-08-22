---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T21:03:04.500225'
end_time: '2026-08-22T21:08:16.353349'
duration_seconds: 311.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paraquat Poisoning
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 13
  num_turns: 15
  total_cost_usd: 1.3477161999999998
  session_id: dbeb19c7-f0c3-5dc5-b8bb-7894f948fb0c
  stop_reason: end_turn
  assistant_text_blocks: 2
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 14
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paraquat Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Paraquat Poisoning** covering all of the
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

I'll research paraquat poisoning across multiple databases and recent literature now.

# Paraquat Poisoning — Comprehensive Research Report

## 1. Disease Information

**Overview.** Paraquat poisoning is acute (and occasionally chronic/occupational) toxicity caused by exposure to paraquat (1,1′-dimethyl-4,4′-bipyridinium dichloride), a fast-acting, non-selective bipyridyl contact herbicide. The overwhelming majority of severe, fatal poisonings result from deliberate ingestion (self-harm) of concentrated commercial formulations (typically 20% w/v solutions), though occupational dermal/inhalational exposure and rare accidental ingestions also occur. Ingested paraquat is corrosive to mucosa, is concentrated in the lung by an active pulmonary uptake system, undergoes redox cycling that generates reactive oxygen species (ROS), and causes multi-organ toxicity — acute kidney injury, hepatic injury, and (in survivors of the acute phase) progressive, often fatal pulmonary fibrosis. There is no specific antidote, and case-fatality remains among the highest of any acute poisoning.

**Key identifiers:**
- **MeSH:** Paraquat (D010297)
- **ICD-10-CM:** T60.3 (Toxic effect of herbicides and fungicides), with 5th/7th character for intent (accidental T60.3X1A, intentional self-harm T60.3X2A, assault T60.3X3A) and Y-code E-codes historically (ICD-9 E863.5)
- **ICD-11:** NE61 / PJ21 (Toxic effect of pesticides) — herbicide-specific subcode under the poisoning chapter
- **CAS Registry Number:** 1910-42-5 (paraquat dichloride); 4685-14-7 (paraquat cation)
- **CHEBI:** CHEBI:34905 (paraquat dichloride); CHEBI:34922 (paraquat) — verify canonical labels via OAK before binding
- **MONDO:** No dedicated, well-populated MONDO term for "paraquat poisoning" specifically was identified in this pass; poisoning-by-substance concepts in MONDO are generally sparse compared to genetic disease — this should be confirmed directly against the MONDO release before curation (candidate parent: a general "poisoning by pesticide/herbicide" grouping term).
- **Synonyms:** Methyl viologen; PQ; Gramoxone (trade name); N,N′-dimethyl-4,4′-bipyridinium dichloride; 1,1′-dimethyl-4,4′-bipyridylium dichloride.

**Evidence source note:** Information below is drawn from aggregated disease-level literature (toxicology reviews, case series, cohort/registry studies, national mortality statistics) rather than individual patient-level EHR data, with individual case reports cited where they illustrate a specific clinical course (e.g., lung transplantation).

---

## 2. Etiology

**Disease causal factor:** Direct chemical/toxicological — absorption of a threshold dose of paraquat (principally by ingestion; also possible by inhalation of concentrated spray/mist or extensive dermal contact through broken skin) initiates redox-cycling oxidative injury. This is not a genetic or infectious disease; it is a single-agent environmental/toxicological exposure disorder.

**Risk factors:**
- **Dose:** The single strongest determinant of outcome. Ingestion of >40–50 mg/kg body weight (of paraquat ion; roughly >20–40 mL of 20% solution) is usually fatal within hours to days; 20–40 mg/kg causes a subacute, often-fatal multi-organ/pulmonary-fibrotic course over days-to-weeks; <20 mg/kg is frequently survivable with supportive care (Dinis-Oliveira et al., *Crit Rev Toxicol* 2008, PMID:18161502).
- **Occupational exposure:** Agricultural workers/applicators in countries where paraquat remains registered, particularly with inadequate protective equipment, backpack sprayer leaks, or contaminated storage containers (accidental ingestion from re-used drink bottles is a well-documented accidental-poisoning pattern).
- **Access to concentrated formulations / means availability:** In agrarian, low- and middle-income settings, ready household access to concentrated paraquat is the dominant modifiable risk factor for suicidal ingestion (Gunnell & Eddleston, *PLOS Medicine*/related pesticide-suicide literature).
- **Delayed presentation:** Delayed hospital arrival (rural distance, stigma, lack of recognition of severity) worsens prognosis because early gastrointestinal decontamination and hemoperfusion lose efficacy after paraquat has distributed into tissue (within ~12–24 h).
- **Psychiatric comorbidity:** Documented as an important covariate of mortality among intentional-ingestion cohorts (e.g., psychiatric comorbidity and mortality analysis, *PMC4227688*).
- **Renal impairment at presentation:** Pre-existing or evolving acute kidney injury (AKI) — since renal clearance is the principal excretory route and its failure both raises systemic exposure and independently predicts death (mortality 70.1% with AKI vs 40.0% without; *Oncotarget*, PMC5584253/PMC5584253).

**Protective factors:**
- **Regulatory restriction / means restriction:** Withdrawal or reformulation (e.g., addition of an emetic, stenching agent, dye, and reduced concentration) of paraquat products, and outright bans, have measurably reduced pesticide-suicide mortality without simple substitution to other lethal methods in several national studies (South Korea ban analysis, Cha et al., *PLOS ONE* 2015; Sri Lanka pesticide-restriction natural experiments).
- **Early, repeated hemoperfusion** (within 12 h of ingestion) is associated with reduced 90-day mortality in some cohort analyses, though evidence quality is limited (retrospective multicenter study, PMC7711471).
- **Combined immunosuppressive therapy** (methylprednisolone + cyclophosphamide ± dexamethasone) added to hemoperfusion was associated with improved survival (48% vs comparator) in a nationwide Taiwanese registry study (Lin et al., *PLOS ONE* 2014, PMID:24475310), and case series report favorable outcomes (Afzali & Gholyaf; PMC3348234) — though the overall evidence base remains weak and randomized-trial confirmation is lacking.
- **Genetic/molecular:** No validated human protective genetic variant has been established; efflux-transporter (e.g., MDR1/P-glycoprotein) activity has been shown in vitro to reduce paraquat cytotoxicity in proximal tubule cells (Toxicol Sci, "MDR1 Transporter Protects Against Paraquat-Induced Toxicity in Human and Mouse Proximal Tubule Cells"), suggesting a plausible but unproven modifier locus.

**Gene-environment interactions:** The best-characterized gene-environment axis for paraquat is not the acute-poisoning phenotype but paraquat as an environmental risk modifier for **idiopathic Parkinson's disease** — where genetic background (e.g., variants affecting dopaminergic handling, mitochondrial quality control, or xenobiotic transport) is hypothesized to modulate individual susceptibility to paraquat-induced dopaminergic neurodegeneration (see Section 6/Section 2 crosslink below); this is an epidemiological association layer distinct from acute toxicity.

---

## 3. Phenotypes

Paraquat poisoning presents as a dose- and time-dependent, multi-organ symptom complex. Three broadly recognized clinical syndromes are described by ingested dose:

| Syndrome | Approx. ingested dose | Course |
|---|---|---|
| Mild-moderate | <20 mg/kg | GI symptoms only; usually full recovery, occasional mild transient renal/hepatic changes |
| Moderate-severe | 20–40 mg/kg | Multi-organ (renal, hepatic, cardiac) injury over days, followed by progressive pulmonary fibrosis over 1–4 weeks; often fatal |
| Fulminant | >40 mg/kg | Rapid multi-organ failure, refractory shock, death within 24–72 h ("hyperacute" form) |

**Symptoms / clinical signs (local, corrosive — onset minutes to hours):**
- Oropharyngeal, esophageal, and gastric ulceration and burning pain (HP:0000164 mouth ulcer / esophageal ulceration is not separately coded in HPO but is captured under "gastrointestinal ulceration")
- Vomiting (HP:0002013 Vomiting), abdominal pain (HP:0002027 Abdominal pain), diarrhea (HP:0002014 Diarrhea) — frequent, near-universal after significant ingestion
- Dysphagia/odynophagia from caustic esophagitis; rare esophageal perforation and mediastinitis with very concentrated/large ingestions

**Systemic/organ-specific manifestations:**
- **Renal:** Acute kidney injury (HP:0001919 Acute kidney injury) from proximal tubular necrosis — often the earliest laboratory abnormality (creatinine rise within 24 h), and the single strongest early predictor of mortality
- **Hepatic:** Elevated transaminases, hepatocellular injury, occasionally jaundice/liver failure (HP:0001392-type hepatic dysfunction)
- **Cardiovascular:** Myocarditis, arrhythmia, and refractory hypotension/circulatory shock in severe poisoning (cardiogenic/circulatory collapse is the dominant fatal mechanism in the fulminant form) — HP:0001635 Congestive heart failure / cardiogenic shock phenotype
- **Pulmonary — the defining and most characteristic feature:**
  - Early: hypoxemia, tachypnea
  - Delayed (days to weeks): progressive, often irreversible pulmonary fibrosis (HP:0002206 Pulmonary fibrosis) driven by alveolar epithelial injury, epithelial-mesenchymal transition-like fibrogenesis, and impaired reepithelialization ("paraquat lung"). Paradoxically, **supplemental oxygen can worsen pulmonary injury** in the acute phase by fueling further ROS generation via redox cycling, so oxygen is withheld unless the patient is significantly hypoxemic — an important, counter-intuitive clinical management point.
  - Radiographic pattern: initially patchy alveolar infiltrates progressing to diffuse ground-glass/honeycombing consistent with acute respiratory distress syndrome (ARDS)-like injury evolving into fibrosis
- **Metabolic:** Metabolic acidosis (HP:0001942 Metabolic acidosis), hypoxemia (HP:0012418 Hypoxemia)
- **Neurological (rare, less characterized):** Peripheral neuropathy and case reports of CNS demyelination following paraquat self-poisoning (systematic review, PMC11590890) — an emerging, still limited literature.
- **Cutaneous/local (occupational exposure):** Contact dermatitis, chemical burns, nail changes with repeated dermal contact; corneal injury with ocular splash.

**Age of onset / progression / frequency:** Onset is acute (minutes–hours for local GI effects; hours–days for renal/hepatic failure; days–weeks for pulmonary fibrosis). Course is progressive in survivors of the acute phase who go on to develop fibrosis, and pulmonary fibrosis is the dominant determinant of subacute/delayed mortality in the moderate-severe group. GI symptoms are near-universal (approaching 100% after a substantial ingestion); AKI incidence is high in moderate-to-severe poisoning (studies report roughly one-third to over half of hospitalized cases, varying by cohort); pulmonary fibrosis develops in a substantial proportion of patients who survive the first several days after moderate-to-large ingestions.

**Quality of life impact:** Survivors with established pulmonary fibrosis face chronic dyspnea, oxygen dependence, and in the most severe cases require lung transplantation — itself associated with a complex, high-morbidity post-transplant course (see Section 12).

**Suggested HPO terms:** HP:0002013 (Vomiting), HP:0002027 (Abdominal pain), HP:0002014 (Diarrhea), HP:0001919 (Acute kidney injury), HP:0002206 (Pulmonary fibrosis), HP:0002094 (Dyspnea), HP:0012418 (Hypoxemia), HP:0001942 (Metabolic acidosis), HP:0001635 (Congestive heart failure / circulatory collapse phenotype), HP:0001392 (Abnormality of liver physiology).

---

## 4. Genetic/Molecular Information

Paraquat poisoning is **not a Mendelian genetic disease** — it is an acute toxicological exposure. There is no causal gene, pathogenic variant, or chromosomal abnormality that produces the disease; instead, "genetic/molecular information" for this entry is best modeled as **host susceptibility/transporter genes** that modulate uptake, distribution, and excretion, and (separately) the **molecular targets of paraquat's toxic mechanism** (covered fully in Section 6).

**Transporter genes implicated in tissue uptake/handling (host susceptibility, not causal mutations):**
- **SLC22A2 (OCT2, hgnc:11005):** The principal transporter mediating renal tubular secretion/uptake of paraquat; overexpression of human OCT2 (but not OCT1 or OCT3) in HEK-293 cells markedly enhanced paraquat accumulation and cytotoxicity (Chen et al., "Transport of paraquat by human organic cation transporters and multidrug and toxic compound extrusion family," PMID:17495125). At toxic plasma concentrations, OCT2-mediated proximal tubular secretion itself becomes a route of self-injury: the transporter concentrates paraquat inside tubular cells, which then poisons the very secretory mechanism, and ultimately destroys the cells (renal AKI mechanism reviews, PMC4376530 / PMC5584253).
- **SLC22A3 (OCT3, hgnc:11043):** Transports the monovalent paraquat radical cation and contributes to distribution into brain and other extra-renal tissues; implicated together with the dopamine transporter (SLC6A3/DAT) in paraquat neurotoxicity to dopaminergic neurons (Rappold et al., *PNAS*, "Paraquat neurotoxicity is mediated by the dopamine transporter and organic cation transporter-3," PMC3251116).
- **ABCB1 (MDR1/P-glycoprotein, hgnc:40):** An efflux transporter shown in vitro to be protective against paraquat-induced cytotoxicity in human and mouse proximal tubule cells (*Toxicological Sciences* 2014), suggesting reduced MDR1 activity/expression could be a modifier of individual susceptibility to nephrotoxicity — not established in human epidemiology.
- **Pulmonary "polyamine uptake system":** The lung's active, saturable uptake of paraquat (yielding 6–10× plasma concentration in lung tissue) has classically been attributed to a polyamine-transport-like carrier system; the precise molecular transporter(s) responsible for this pulmonary-selective concentration are still incompletely characterized at the single-gene level in the literature reviewed here and would need targeted confirmation before ontology binding.

**Somatic vs. germline:** Not applicable — no somatic mutational driver is implicated; this is a pharmacokinetic/toxicodynamic host-modifier question, not a mutation-driven disease.

**Epigenetics:** No paraquat-poisoning-specific human epigenetic signature was identified in this pass; epigenetic mechanisms (histone modification, DNA methylation) are, however, an active research area in the *separate* paraquat–Parkinson's-disease epidemiological literature (e.g., "Linking environmental risk factors with epigenetic mechanisms in Parkinson's disease," *npj Parkinson's Disease* 2023, PMC10457362), which is a distinct chronic-exposure/neurodegeneration question rather than the acute-poisoning phenotype.

**Chromosomal abnormalities:** Not applicable.

---

## 5. Environmental Information

**Environmental/chemical factor (the disease-defining exposure):** Paraquat dichloride, a quaternary-nitrogen bipyridyl herbicide formulated commercially (e.g., as Gramoxone) typically at 20% w/v concentration. Suggested exposure-term binding: ECTO term for "exposure to paraquat" (verify exact CURIE via OAK against ECTO; a general herbicide-exposure ECTO branch exists and should be searched for the paraquat-specific leaf term).

**Routes of exposure:**
- **Ingestion** (dominant route for severe/fatal poisoning; deliberate self-poisoning is responsible for the great majority — cited as ~93% of fatalities in some series — of deaths)
- **Inhalation** of spray mist during agricultural application (low systemic absorption via this route under normal use conditions, but relevant with heavy/prolonged occupational exposure or misuse)
- **Dermal absorption** (minimal through intact skin; significant through abraded/broken skin or prolonged saturated-clothing contact)
- **Ocular** splash exposure (local corneal/conjunctival injury)

**Occupational/lifestyle factors:** Agricultural work involving herbicide application without adequate personal protective equipment; storage/transfer of concentrated paraquat in unlabeled beverage containers (a recurrent, well-documented cause of accidental fatal ingestion, especially of children); rural/agrarian residence in regions where paraquat remains legally available.

**Infectious agents:** Not applicable — paraquat poisoning is a purely chemical/toxicological disease with no infectious component (though secondary infection, e.g., ventilator-associated pneumonia or catheter-related sepsis, is a recognized complication of prolonged critical illness in survivors).

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:** ingestion → mucosal/GI corrosive injury → systemic absorption (variable, generally poor oral bioavailability, ~5–10% but sufficient at high doses to be lethal) → selective, active, saturable pulmonary and renal tissue concentration → intracellular redox cycling and reactive-oxygen-species generation → lipid peroxidation, NADPH depletion, mitochondrial dysfunction, and direct cytotoxicity → acute organ injury (kidney, liver, heart) in the near term and progressive fibrogenic remodeling (lung) in the medium term → multi-organ failure and/or respiratory failure as terminal common pathways.

**Molecular mechanism — redox cycling (the central, defining mechanism):**
Paraquat is a redox-active dication (PQ²⁺). Intracellularly it is reduced by one electron — chiefly via **mitochondrial Complex I** (NADH:ubiquinone oxidoreductase) — to the paraquat radical monocation (PQ•⁺), which then reacts non-enzymatically with molecular oxygen to regenerate PQ²⁺ while producing superoxide anion (O₂•⁻). This cycle repeats catalytically, consuming NADPH/NADH and continuously generating ROS. Complex I was identified as the major site of mitochondrial superoxide production by paraquat (Cochemé & Murphy, *J Biol Chem*; "Complex I Is the Major Site of Mitochondrial Superoxide Production by Paraquat"). **NADPH oxidase (NOX)** is a second major site of redox cycling, particularly in phagocytic/microglial cells, generating extracellular superoxide (search results on NADPH-oxidase–mediated paraquat/maneb oxidative stress). Superoxide is dismutated to hydrogen peroxide and, via Fenton-type chemistry, to the highly reactive hydroxyl radical, which attacks polyunsaturated fatty acids in membrane phospholipids, initiating lipid peroxidation and membrane destruction. This ROS burden also depletes cellular NADPH reserves needed for glutathione regeneration, compounding oxidative injury (GO:0006979 response to oxidative stress; GO:0055114 oxidation-reduction process; GO:0006749 glutathione metabolic process).

**Structural analogy to MPP+/Parkinsonian toxins:** Paraquat (PQ²⁺) is structurally similar to 1-methyl-4-phenylpyridinium (MPP⁺), the active dopaminergic neurotoxic metabolite of MPTP; both are taken up via cation transporters (dopamine transporter, OCT3) into dopaminergic neurons, generate ROS, and have been used experimentally to model nigrostriatal degeneration in Parkinson's disease research (PMC5082881; PNAS PMC3251116). This mechanistic parallel underlies the long-standing epidemiological hypothesis linking chronic low-dose paraquat exposure to Parkinson's disease risk (Section 2).

**Ferroptosis and Nrf2/Keap1 signaling:** Recent mechanistic work implicates **ferroptosis** — iron-dependent lipid peroxidative cell death — as a specific contributor to paraquat-induced pulmonary fibrosis, mediated through Keap1/Nrf2 signaling dysregulation ("Molecular mechanism of paraquat-induced ferroptosis leading to pulmonary fibrosis mediated by Keap1/Nrf2 signaling pathway," PMC10635988). GO:0097707 (ferroptosis) is a candidate process term.

**Fibrogenic cascade in the lung (the disease-defining subacute mechanism):**
1. Selective, active pulmonary uptake concentrates paraquat 6–10-fold above plasma in alveolar type I and type II epithelial cells and Clara (club) cells (via the classical "polyamine uptake system").
2. Redox-cycling ROS generation causes diffuse alveolar epithelial injury and death, producing an early alveolitis/ARDS-like picture.
3. Surviving/regenerating alveolar epithelial cells undergo an **epithelial-mesenchymal transition (EMT)-like fibrogenic response**, with resistance to apoptosis and acquisition of a pro-fibrotic phenotype (PMC4370722, "Paraquat Induces Epithelial-Mesenchymal Transition-Like Cellular Response...").
4. NF-κB and JNK/p38 MAPK signaling pathways are activated, driving pro-inflammatory and pro-fibrotic gene programs (PMC5396433, liver X receptor agonist attenuation study).
5. Excess extracellular matrix deposition (GO:0030198 extracellular matrix organization) by activated (myo)fibroblasts (CL:0000186) produces progressive interstitial fibrosis, culminating in restrictive lung physiology and, in the most severe cases, respiratory failure over 1–4 weeks — the classical "delayed progressive pulmonary fibrosis" of subacute paraquat poisoning.

**Renal mechanism:** Active tubular secretion of paraquat by OCT2 concentrates the compound within proximal tubular epithelial cells (CL:0002306/CL candidate: proximal tubule epithelial cell), where redox cycling drives tubular necrosis; this is compounded by systemic oxidative stress from other organs. Early creatinine rise reflects both true tubular injury and a component of systemic oxidative-stress-driven renal dysfunction (PLOS ONE, "Mechanisms Underlying Early Rapid Increases in Creatinine in Paraquat Poisoning," PMC4376530). AKI is a strong independent mortality predictor.

**Cardiac and hepatic injury:** Direct oxidative myocardial and hepatocellular injury via the same redox-cycling mechanism, contributing to circulatory collapse (dominant fatal mechanism in fulminant, high-dose poisoning) and hepatic dysfunction/failure in severe cases.

**Cell types involved (candidate CL terms):** CL:0002063 (type I pneumocyte), CL:0002062 (type II pneumocyte), CL:0000158 (Clara/club cell), CL:0000186 (myofibroblast), proximal tubule epithelial cell (CL candidate), CL:0000700 (dopaminergic neuron, relevant to the PD-association literature), CL:0000129 (microglial cell, implicated in NOX-mediated CNS oxidative injury).

**Candidate GO biological process terms:** GO:0006979 (response to oxidative stress), GO:0034599 (cellular response to oxidative stress), GO:0055114 (oxidation-reduction process), GO:0006749 (glutathione metabolic process), GO:0097707 (ferroptosis), GO:0030198 (extracellular matrix organization), GO:0097237 (cellular response to toxic substance), GO:0006915 (apoptotic process).

**Molecular profiling:** An iTRAQ quantitative proteomic study has identified candidate serum biomarkers of acute paraquat poisoning in humans (PMC9078879), an early step toward systems-level (proteomic) characterization; comprehensive transcriptomic/metabolomic paraquat-poisoning-specific human datasets were not identified in this pass (much of the -omics literature instead concerns paraquat as an experimental oxidative-stress or Parkinson's-model tool rather than clinical poisoning cohorts).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary target organs:** Lung (the organ most characteristically and often fatally affected — UBERON:0002048), kidney (UBERON:0002113, especially the proximal tubule), and the gastrointestinal tract (oropharynx, esophagus, stomach — direct corrosive contact site; UBERON:0001043 esophagus)
- **Secondary/complication organs:** Liver (UBERON:0002107, hepatocellular injury), heart (UBERON:0000948, myocarditis/circulatory collapse), and less consistently the central and peripheral nervous system (rare demyelination/neuropathy reports)
- **Body systems involved:** Respiratory, renal, gastrointestinal, hepatic, cardiovascular, and (uncommonly) nervous systems — i.e., a multi-system toxidrome.

**Tissue and cell level:**
- Respiratory epithelium — alveolar type I/II pneumocytes and club (Clara) cells (the selective site of pulmonary paraquat concentration)
- Renal proximal tubular epithelium (the selective site of tubular secretion/reabsorption-mediated concentration)
- Gastrointestinal squamous/columnar mucosa (direct corrosive contact injury)
- Hepatocytes
- Cardiac myocytes
- In the chronic/PD-association literature: nigrostriatal dopaminergic neurons of the substantia nigra pars compacta (UBERON:0002038) and associated microglia

**Subcellular level:** Mitochondria (Complex I as the principal intracellular site of paraquat-driven superoxide generation; GO Cellular Component: GO:0005743 mitochondrial inner membrane), plasma membrane/lipid bilayer (site of lipid peroxidation), and — via NADPH oxidase — the cell membrane-associated NOX complex.

**Localization:** Bilateral, diffuse pulmonary involvement (not focal/unilateral); bilateral renal involvement; systemic (not lateralized) disease overall.

---

## 8. Temporal Development

**Onset:** Acute, occurring within minutes to hours of ingestion for local corrosive/GI effects, within 24–72 hours for renal/hepatic/cardiac injury, and over days to 1–4 weeks for the defining delayed pulmonary fibrosis.

**Progression / disease course pattern (dose-stratified, as in Section 3):**
- **Mild-moderate poisoning:** Self-limited, typically resolving GI symptoms with supportive care; may have transient, reversible organ dysfunction.
- **Moderate-severe poisoning:** A biphasic/triphasic course — initial GI/corrosive phase, followed by an organ-failure phase (renal/hepatic/cardiac, days 1–4), followed by a progressive pulmonary-fibrotic phase (days–weeks) that is frequently the ultimate cause of death.
- **Fulminant (massive-dose) poisoning:** Rapid, unremitting multi-organ failure and refractory circulatory shock, typically fatal within 24–72 hours, often before pulmonary fibrosis has time to develop.

**Critical period for intervention:** The first ~12–24 hours after ingestion is the critical window for gastrointestinal decontamination and hemoperfusion, since paraquat distributes irreversibly into tissue compartments after this window, sharply reducing the efficacy of extracorporeal removal.

**Disease duration:** Ranges from self-limited (days, in mild ingestions) to a protracted, weeks-to-months critical illness culminating in death or, in a minority of survivors, chronic pulmonary fibrosis requiring long-term oxygen support or lung transplantation.

**Remission:** Full recovery is possible after low-dose ingestion; there is no described spontaneous remission pattern once significant pulmonary fibrosis is established — the mechanism is progressive rather than fluctuating.

---

## 9. Inheritance and Population

Paraquat poisoning is **not a heritable genetic disease**; inheritance-pattern fields (AD/AR/X-linked, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, carrier frequency) are **not applicable**.

**Epidemiology:**
- Pesticide self-poisoning as a whole is estimated to account for a substantial share of global suicide deaths, disproportionately concentrated in rural areas of low- and middle-income countries in Asia and the Pacific.
- Paraquat specifically has historically been one of the most lethal agents used, with an estimated **~20 deaths per million persons worldwide** attributable to paraquat as a suicide method in earlier global estimates, and it has been described as the most frequently used self-poisoning agent in some national settings (e.g., historically in South Korea and Trinidad).
- **~93% of fatalities from paraquat intoxication are reported as suicides**, occurring predominantly in developing/agrarian countries (search-derived synthesis of pesticide-suicide epidemiology literature; see also "Suicide by intentional ingestion of pesticides: A continuing tragedy in developing countries").

**Mortality:** Global case-fatality estimates are consistently high, generally cited in the **35–70%+ range** across cohorts, with some sources citing an overall mortality around 60% and others up to 70–90% depending on dose distribution and access to care; mortality is strongly right-shifted toward the lethal end because ingestion is so often deliberate and at high concentration.

**Geographic distribution:** Historically concentrated in agrarian regions of East/Southeast Asia (China, South Korea historically before its ban, other parts of Asia-Pacific), parts of Latin America and the Caribbean (e.g., Trinidad), and Sub-Saharan Africa where paraquat has remained available; incidence has fallen sharply in jurisdictions that banned or restricted paraquat sale (see Section 13 and regulatory notes below).

**Age/sex distribution:** Case series generally show a predominance of working-age adults with agricultural access; sex distribution varies by setting/study, reflecting local patterns of self-harm method choice rather than a biological sex-specific susceptibility.

**Regulatory/geographic status as of 2024–2026 (relevant population-exposure context):** Paraquat is banned or severely restricted in more than 70 countries, including the European Union, China, Brazil, Canada, and — as of 2024 — Nigeria. It remains registered and in agricultural use in the United States (subject to restricted-use/certified-applicator rules tightened in 2016 after fatal accidental exposures), with U.S. EPA regulatory review ongoing (the EPA removed a 2021 interim risk-mitigation decision in January 2025) and state-level actions underway (e.g., a 2026 voluntary registration cancellation by Syngenta in California, and California legislative proposals to phase out paraquat by end of 2025). It also remains registered in India, Japan, and Australia among other countries.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Urine dithionite (sodium hydrosulfite) colorimetric test:** A rapid, low-cost bedside qualitative screening test — a blue/blue-green color change on adding alkaline sodium dithionite to urine indicates the presence of paraquat and roughly correlates with severity (used widely in resource-limited settings for triage).
- **Plasma/serum paraquat concentration** (measured by spectrophotometry historically, and by LC-MS/MS in modern laboratories) — the single most validated quantitative prognostic test, plotted against time-since-ingestion on validated nomograms (see below).
- Routine chemistry: serum creatinine (early rise is a key marker of renal injury and independent mortality predictor), liver enzymes, arterial blood gas/lactate, and inflammatory markers.
- Novel/investigational biomarkers: urinary NGAL (neutrophil gelatinase-associated lipocalin, elevated in AKI but not independently predictive of death), urinary cystatin C (reflecting altered proximal-tubular reuptake/degradation and confirming tubular injury), and serum proteomic panels under investigation (PMC9078879).

**Prognostic/severity scoring tools:**
- **Proudfoot nomogram (1979):** Relates outcome to plasma paraquat concentration at a given time post-ingestion (valid for samples drawn 4–24 h post-ingestion).
- **Scherrmann extension (1987):** Extends the nomogram's applicability beyond 24 hours post-ingestion.
- **Severity Index for Paraquat Poisoning (SIPP), Sawada et al.:** SIPP = elapsed time from ingestion to arrival (hours) × serum paraquat concentration (µg/mL). SIPP <10 → good prognosis; SIPP 10–50 → high risk of death from progressive pulmonary fibrosis/organ failure; SIPP >50 → typically rapid death from circulatory collapse.
- APACHE II score and serum lactate have also been evaluated (sometimes in combination with SIPP) as prognostic tools in Chinese cohorts.
- More recent prognostic nomograms integrating multiple clinical variables for predicting in-hospital mortality have been developed and validated (*Scientific Reports* 2023, doi:10.1038/s41598-023-50722-z).

**Imaging:** Chest radiography/CT showing progression from patchy alveolar infiltrates (early) to diffuse ground-glass and honeycomb fibrotic change (late) tracks the pulmonary phase.

**Differential diagnosis:** Other causes of acute corrosive ingestion (other herbicides/pesticides, especially diquat — a related bipyridyl compound with a similar corrosive/multi-organ-failure profile but without paraquat's selective pulmonary accumulation and characteristic fibrosis), ARDS from other etiologies, and other causes of rapidly progressive interstitial lung disease in a patient without a clear ingestion history.

**Genetic testing:** Not applicable/not indicated — this is not a heritable disease and there is no clinically validated genetic test for paraquat susceptibility.

**Screening:** No population screening program exists; the principal "screening" intervention at the population level is public-health means restriction (regulatory withdrawal, reformulation with deterrents, or licensing controls) rather than individual biomarker screening.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Case-fatality is high across the literature, commonly cited in the range of ~35–70%, with some series (particularly those enriched for intentional, high-dose ingestion) reporting up to 70–90% mortality. Death from progressive pulmonary fibrosis typically occurs over 1–4 weeks after ingestion in the moderate-dose group; death from circulatory collapse/multi-organ failure typically occurs within 24 hours to a few days in the high-dose group.

**Key prognostic factors:** Ingested dose/plasma paraquat concentration (the dominant factor, formalized in the Proudfoot/Scherrmann nomograms and SIPP), time from ingestion to treatment (earlier decontamination/hemoperfusion improves outcome), development of AKI (strongly associated with mortality — 70.1% vs 40.0% in AKI vs non-AKI patients), and age (younger patients, e.g., <45 years, have shown better survival in some immunosuppressive-therapy cohorts).

**Morbidity in survivors:** The principal long-term morbidity is chronic restrictive lung disease from established pulmonary fibrosis, which can progress to end-stage respiratory failure requiring long-term oxygen or lung transplantation. Renal recovery is variable; some patients develop chronic kidney disease after severe AKI. Case reports also describe delayed neurological sequelae (demyelination, peripheral neuropathy) though this is not well quantified epidemiologically.

**Complications:** Esophageal stricture/perforation and mediastinitis (from corrosive injury), secondary nosocomial infection during prolonged critical illness, and — in the small subset undergoing lung transplantation — the full range of transplant-related complications (graft dysfunction, rejection, infection, weaning failure from mechanical ventilation) (case-based reviews, PMC12868150; PMC10387547).

**Recovery potential:** Full recovery is achievable after low-dose ingestion with prompt supportive care; recovery after moderate-severe poisoning is possible but guarded and dependent on whether pulmonary fibrosis becomes established; recovery after fulminant, massive-dose poisoning is exceedingly rare.

---

## 12. Treatment

There is **no specific antidote** for paraquat poisoning; management is supportive, decontamination-focused, and — for the fibrotic/organ-failure phase — largely investigational, with a generally weak evidence base for any single intervention.

**Gastrointestinal decontamination (early, time-critical):**
- Activated charcoal or Fuller's earth/bentonite clay administered as soon as possible after ingestion to adsorb unabsorbed paraquat and limit systemic exposure — NCIT candidate term: NCIT:C1445 (Activated Charcoal) as a therapeutic agent under a general decontamination/pharmacotherapy treatment_term.
- Gastric lavage may be considered very early after ingestion in some protocols, though evidence and practice vary.

**Extracorporeal removal:**
- **Hemoperfusion** (charcoal or resin cartridge) — theoretically attractive because it removes paraquat directly from blood, but overall trial evidence for a survival benefit is weak/mixed; some retrospective analyses suggest benefit only when performed early (within ~12 h) and repeatedly (PMC7711471), reflecting the narrow window before tissue redistribution.
- **Hemodialysis** — similarly limited by rapid tissue distribution and reduced efficacy after the first ~24 hours, further diminished once tubular necrosis reduces renal clearance.
- **Continuous renal replacement therapy (CRRT)** for established AKI, primarily as supportive renal-failure management rather than a paraquat-elimination strategy per se.

**Immunosuppressive therapy** (targeting the inflammatory/fibrogenic cascade):
- Combination pulse **methylprednisolone + cyclophosphamide ± dexamethasone** is the most widely studied regimen; a nationwide Taiwanese registry analysis found immunosuppressive therapy added to hemoperfusion associated with improved survival (48% vs lower in comparator groups, p<0.001), with the greatest benefit in patients under 45 (Lin et al., *PLOS ONE* 2014, PMID:24475310). A small case series (n=9) using pulse cyclophosphamide/methylprednisolone reported 100% survival, though this is a very small, likely selected sample. Overall the evidence remains "very weak" per multiple reviews, and randomized controlled trial data are lacking. NCIT candidate terms: NCIT:C15632 (Chemotherapy) treatment_term with therapeutic_agent cyclophosphamide (CHEBI candidate) and corticosteroids.

**Antioxidant therapy (adjunctive, mechanistically motivated but weakly evidenced):**
- N-acetylcysteine (NAC), vitamin C, and vitamin E have been used to scavenge ROS and support glutathione regeneration, consistent with the redox-cycling mechanism, though clinical efficacy data are limited and mostly derived from small studies/case series.

**Oxygen therapy — a critical caveat, not a straightforward supportive measure:**
- Supplemental oxygen is generally **withheld unless the patient is significantly hypoxemic**, because hyperoxia can potentiate paraquat's redox-cycling ROS generation and worsen pulmonary injury — a distinctive, mechanism-driven deviation from standard critical-care oxygen practice.

**Definitive/last-resort therapy:**
- **Lung transplantation** has been performed in selected survivors with progressive, irreversible pulmonary fibrosis after systemic paraquat clearance, sometimes bridged with ECMO. Case reports and small reviews (8 reports/11 patients; a more recent review of 15 cases) describe generally encouraging but heterogeneous outcomes, with careful timing (waiting for hepatorenal recovery), infection prevention, and multidisciplinary perioperative management identified as key to success (PMID:36626514; PMC10387547; PMC12868150; PMC8660696). NCIT candidate term: NCIT:C15289 (Organ Transplantation).

**Experimental/investigational directions:** Preclinical work targeting Nrf2/Keap1 signaling, ferroptosis inhibition, NF-κB/JNK–p38 MAPK pathway modulation (e.g., liver X receptor agonist TO901317 in mouse models, PMC5396433), and pirfenidone (an antifibrotic approved for idiopathic pulmonary fibrosis) has shown protective effects against paraquat-induced lung injury/fibrosis in animal models, representing candidate translational targets not yet established in human treatment guidelines.

**Treatment algorithm summary:** (1) Immediate GI decontamination if within the window; (2) supportive/organ-support care (fluid resuscitation, renal replacement as needed, cautious oxygen use); (3) consider early, repeated hemoperfusion if very early presentation; (4) consider pulse immunosuppressive therapy in moderate-severe poisoning, weighing infection risk; (5) antioxidant adjuncts; (6) evaluate for lung transplantation in survivors with established, progressive, irreversible fibrosis once systemic toxicity has cleared.

---

## 13. Prevention

**Primary prevention — means restriction (the dominant, best-evidenced strategy):**
Because the great majority of severe/fatal paraquat poisoning is intentional self-poisoning enabled by ready access to a highly lethal concentrated agent, **regulatory restriction of paraquat availability** is the single most impactful and best-documented prevention strategy at a population level:
- National **bans or severe restrictions** (now covering 70+ countries, including the EU, China, Brazil, Canada, and — as of 2024 — Nigeria) have been followed by measurable declines in pesticide-suicide mortality in several jurisdictions, without simple full substitution to other lethal methods (South Korea paraquat-prohibition analysis, Cha et al., *PLOS ONE* 2015).
- **Reformulation strategies** short of outright bans — reduced concentration, addition of an emetic, a stenching/warning agent, and a blue dye to discourage confusion with beverages — have also been used to reduce lethality of accidental/impulsive ingestions.
- U.S. regulatory status remains under active review (restricted-use/certified-applicator requirements since 2016; EPA's 2025 removal of a 2021 interim decision; ongoing state-level legislative and voluntary-registrant actions such as California's 2026 cancellation).

**Occupational/behavioral prevention:**
- Personal protective equipment, restricted/certified-applicator licensing, and safe storage/labeling practices (never storing paraquat in unlabeled drink bottles) to reduce accidental occupational and household exposure.

**Secondary prevention:**
- Rapid recognition and immediate decontamination (activated charcoal/Fuller's earth) at first medical contact is the most time-critical secondary-prevention measure, given the narrow window before irreversible tissue distribution.
- Rural health-worker and community education to shorten time-to-presentation after ingestion.

**Public health / suicide-prevention framing:**
- Paraquat restriction is a widely cited exemplar of the "means restriction" approach to suicide prevention (paralleling the broader evidence base from Sri Lanka's WHO Class I/II pesticide restrictions), on the rationale that highly lethal, impulsively accessible methods disproportionately convert a suicide attempt into a death, and restricting access reduces population suicide mortality even without addressing underlying psychiatric drivers directly.

**Prophylaxis:** No pharmacological prophylaxis exists; prevention is exposure-control based, not medication-based.

---

## 14. Other Species / Natural Disease

Paraquat poisoning is not a naturally occurring disease of non-human species in the sense of a spontaneous veterinary condition, but accidental and occasionally deliberate paraquat poisoning is a recognized veterinary and wildlife toxicology entity:

- **Companion and farm animals** (dogs, cats, livestock — NCBITaxon:9615 *Canis lupus familiaris*, NCBITaxon:9685 *Felis catus*, NCBITaxon:9913 *Bos taurus*, etc.) can be accidentally poisoned via contaminated feed, water, or direct ingestion of herbicide, presenting with the same core toxidrome (GI corrosive injury, renal injury, and progressive pulmonary fibrosis), and this is documented in the veterinary toxicology literature (search for veterinary paraquat case reports/OMIA was not exhaustively pursued in this pass; recommend a targeted OMIA/veterinary-toxicology literature search if this section needs deeper sourcing).
- **Wildlife** exposure (birds, in particular) via contaminated agricultural runoff or direct ingestion of treated vegetation is documented in environmental-toxicology literature, though this is an ecotoxicology question distinct from clinical veterinary poisoning.
- **Comparative pathology:** The core mechanism — selective pulmonary uptake, redox cycling, and progressive fibrosis — appears broadly conserved across mammalian species, which is precisely what underlies the extensive use of rodent models (Section 15).
- **Zoonotic potential:** Not applicable — paraquat poisoning is a toxicological, not infectious, condition, so there is no zoonotic transmission dimension; however, cross-species susceptibility to the same chemical mechanism is expected wherever the relevant transporters (OCT-family) and mitochondrial Complex I are conserved.

---

## 15. Model Organisms

Paraquat is one of the most widely used experimental toxicants precisely because it reliably reproduces two distinct human disease phenotypes in model systems: **pulmonary fibrosis** and **dopaminergic neurodegeneration (Parkinsonian) phenotypes**.

**Rodent models (pulmonary fibrosis):**
- **Mouse (*Mus musculus*, NCBITaxon:10090):** Intraperitoneal injection (a commonly used protocol reports paraquat 40 mg/kg IP producing optimal pulmonary fibrosis by 2 weeks post-injection, with diffuse alveolar thickening and interstitial fibrosis on histology) and intratracheal aerosolized delivery (e.g., 0.02 mg/mouse) are both used, with intratracheal delivery cited as producing more homogeneous lesion distribution across the lung. There is no single standardized dosing protocol across the field — gastric gavage, intraperitoneal injection, and intratracheal instillation are all used, with intraperitoneal injection most common (search synthesis of multiple mouse-model papers, including PMC9011139/"Paraquat Induces Lung Injury via miR-199-Mediated SET in a Mouse Model").
- **Rat (*Rattus norvegicus*, NCBITaxon:10116):** Also used for paraquat-induced lung-injury/fibrosis modeling, often compared against the bleomycin model (the other classical chemical-induction model for pulmonary fibrosis).
- **Fidelity/limitations:** These models recapitulate the redox-cycling, alveolar-epithelial-injury, and fibrogenic-remodeling cascade reasonably well and are used to test antifibrotic/antioxidant candidate therapies (e.g., pirfenidone, LXR agonists), but do not fully reproduce the human multi-organ (renal/hepatic/cardiac) failure syndrome seen after oral ingestion, since dosing routes differ from the human ingestion route and dose selection is optimized for the pulmonary endpoint specifically.

**Rodent and invertebrate models (Parkinsonian/dopaminergic neurodegeneration):**
- **Mouse:** Systemic paraquat administration (often combined with the fungicide maneb for synergistic effect) is a standard chemical model of nigrostriatal dopaminergic neuron loss and microglial activation in the substantia nigra pars compacta, used to probe Parkinson's-disease-relevant mechanisms (PMC5082881, "Assessment of the Effects of MPTP and Paraquat on Dopaminergic Neurons and Microglia in the Substantia Nigra Pars Compacta of C57BL/6 Mice").
- **Drosophila melanogaster (NCBITaxon:7227):** Paraquat feeding is a classical oxidative-stress/Parkinsonian-phenotype assay in flies; a 2025 genome-wide screen identified genes mediating resistance to paraquat-induced neurodegeneration in *Drosophila*, offering candidate modifier loci for translational follow-up (bioRxiv preprint, 2025.04.02.646829).
- **C. elegans:** Also used as a rapid, genetically tractable oxidative-stress/paraquat-exposure model system, though not detailed in the sources retrieved here.

**Model limitations (general):** No single model captures the full human clinical picture (GI corrosive injury + renal + hepatic + cardiac + delayed pulmonary fibrosis, in a dose- and time-dependent cascade following oral ingestion). Pulmonary-fibrosis rodent models typically bypass the GI/systemic-absorption step (via IP or intratracheal dosing) and so are best understood as models of the *downstream* fibrogenic mechanism rather than the complete ingestion-poisoning syndrome; Parkinsonian models use chronic low-dose systemic exposure distinct from the acute high-dose ingestion scenario that defines clinical "paraquat poisoning."

**Applications:** Rodent lung models are used to test candidate antifibrotic/antioxidant therapeutics and to dissect the Nrf2/Keap1-ferroptosis and NF-κB/MAPK signaling pathways; Drosophila/mouse Parkinsonian models are used to study gene-environment interaction and neurodegeneration mechanism, informing (but not proving) the human paraquat-Parkinson's-disease epidemiological association.

---

## Ontology Term Suggestions Summary (for curator verification via OAK)

| Category | Candidate terms (verify before binding) |
|---|---|
| HPO | HP:0002013 Vomiting; HP:0002027 Abdominal pain; HP:0002014 Diarrhea; HP:0001919 Acute kidney injury; HP:0002206 Pulmonary fibrosis; HP:0002094 Dyspnea; HP:0012418 Hypoxemia; HP:0001942 Metabolic acidosis |
| GO (biological process) | GO:0006979 response to oxidative stress; GO:0034599 cellular response to oxidative stress; GO:0055114 oxidation-reduction process; GO:0006749 glutathione metabolic process; GO:0097707 ferroptosis; GO:0030198 extracellular matrix organization; GO:0006915 apoptotic process |
| CL | type I pneumocyte; type II pneumocyte; club (Clara) cell; myofibroblast; proximal tubule epithelial cell; dopaminergic neuron; microglial cell |
| UBERON | UBERON:0002048 lung; UBERON:0002113 kidney; UBERON:0002107 liver; UBERON:0000948 heart; UBERON:0001043 esophagus; UBERON:0002038 substantia nigra |
| CHEBI | CHEBI:34905 paraquat dichloride (verify canonical form) |
| NCIT (treatment) | NCIT:C1445 Activated Charcoal; NCIT:C15632 Chemotherapy (cyclophosphamide regimen); NCIT:C15289 Organ Transplantation; NCIT:C15986 Pharmacotherapy |
| HGNC (transporter genes) | SLC22A2 (OCT2, hgnc:11005); SLC22A3 (OCT3, hgnc:11043); ABCB1 (MDR1, hgnc:40) |

---

## Key Citations

- Dinis-Oliveira RJ et al. Paraquat poisonings: mechanisms of lung toxicity, clinical features, and treatment. *Crit Rev Toxicol.* 2008. PMID:18161502
- Paraquat poisoning: an overview of the current status. PMID:2198050
- Chen Y et al. Transport of paraquat by human organic cation transporters and multidrug and toxic compound extrusion family. PMID:17495125
- Lin JL et al. Addition of immunosuppressive treatment to hemoperfusion is associated with improved survival after paraquat poisoning: a nationwide study. *PLOS ONE.* 2014. PMID:24475310
- Cochemé HM, Murphy MP. Complex I is the major site of mitochondrial superoxide production by paraquat. *J Biol Chem.*
- Rappold PM et al. Paraquat neurotoxicity is mediated by the dopamine transporter and organic cation transporter-3. *PNAS.* PMC3251116
- Molecular mechanism of paraquat-induced ferroptosis leading to pulmonary fibrosis mediated by Keap1/Nrf2 signaling pathway. PMC10635988
- Paraquat Induces Epithelial-Mesenchymal Transition-Like Cellular Response Resulting in Fibrogenesis... PMC4370722
- Predictors of acute kidney injury after paraquat intoxication. *Oncotarget.* PMC5584253
- Mechanisms Underlying Early Rapid Increases in Creatinine in Paraquat Poisoning. *PLOS ONE.* PMC4376530
- Development and validation of a prognostic nomogram for predicting in-hospital mortality of patients with acute paraquat poisoning. *Sci Rep.* 2023. doi:10.1038/s41598-023-50722-z
- Cha ES et al. Paraquat Prohibition and Change in the Suicide Rate and Methods in South Korea. *PLOS ONE.* 2015.
- Lung transplantation in a woman with paraquat poisoning that led to pulmonary fibrosis: A case report. PMID:36626514
- Case Report: Multifactorial weaning failure after lung transplantation in paraquat-induced pulmonary fibrosis. PMC12868150
- The Link Between Paraquat and Demyelination: A Review of Current Evidence. PMC11590890
- Van Maele-Fabry G, meta-analysis of pesticide exposure and Parkinson's disease risk (summary risk ratio ~1.6, referenced via secondary sources)
- Genome-wide analysis reveals genes mediating resistance to paraquat neurodegeneration in *Drosophila*. bioRxiv 2025.04.02.646829

**Note on evidence completeness:** This report synthesizes disease-level literature (toxicology reviews, cohort/registry studies, case reports, mechanistic and animal-model papers, and regulatory-status sources) retrieved via targeted web/PubMed-indexed searches conducted August 2026. Several sections (precise MONDO ID, exhaustive gene-frequency/variant data — not applicable given the non-genetic etiology, and comprehensive veterinary/wildlife case literature) would benefit from direct database queries (MONDO release browser, OMIA, PubMed full-text search) beyond what a search-engine-mediated pass can confirm, and all PMIDs and ontology term candidates listed above should be independently re-verified (e.g., via OAK `runoak info` lookups) before being bound into a curated knowledge-base entry, consistent with standard anti-hallucination practice for AI-assisted curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.