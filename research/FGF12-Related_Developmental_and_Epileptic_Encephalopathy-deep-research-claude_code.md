---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T03:51:50.813643'
end_time: '2026-08-20T03:56:18.201433'
duration_seconds: 267.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FGF12-Related Developmental and Epileptic Encephalopathy
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
  num_turns: 28
  total_cost_usd: 1.9569852000000003
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 3
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:42057324
  - PMID:42185328
  - PMID:37331110
  relevance_assessed: 25
  on_topic: 20
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FGF12-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FGF12-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I now have enough primary-literature material to compile the full report.

# FGF12-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview.** FGF12-related developmental and epileptic encephalopathy (also designated **Developmental and Epileptic Encephalopathy 47, DEE47**, and historically "Early Infantile Epileptic Encephalopathy 47, EIEE47") is a severe, early-onset genetic epilepsy syndrome caused by heterozygous, typically de novo, pathogenic variants in **FGF12** (fibroblast growth factor 12, also called **FHF1**, fibroblast growth factor homologous factor 1). It belongs to the growing family of sodium-channel-regulatory-protein epileptic encephalopathies, alongside SCN1A/SCN2A/SCN8A and FGF13(FHF2)-related disorders. Seizures typically begin in the first days to weeks of life and are intractable, with variable developmental regression ([OMIM #617166](https://omim.org/entry/617166); [Siekierska et al. 2016, Neurology, PMID:27164707](https://www.neurology.org/doi/10.1212/WNL.0000000000002752)).

**Key identifiers:**
- OMIM gene: *601513 (FGF12); OMIM phenotype: **#617166** DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 47 (DEE47)
- HGNC gene symbol: FGF12 (also known as FHF1, FGF12B)
- Chromosomal location: **3q28** (some sources cite 3q28-q29)
- Orphanet: listed under "FGF12-fibroblast growth factor 12" gene page, associated with **non-specific early-onset epileptic encephalopathy** ([Orphanet](https://www.orpha.net/en/disease/gene/FGF12?name=FGF12&mode=gene))
- MONDO: developmental and epileptic encephalopathy, 47 (cross-referenced via NORD/MONDO: [rarediseases.org](https://rarediseases.org/mondo-disease/developmental-and-epileptic-encephalopathy-47/))
- Synonyms: EIEE47; Early Infantile Epileptic Encephalopathy 47; FHF1 epileptic encephalopathy; DEE47

**Evidence source note:** Most published data derive from individual patient case reports and small case series (aggregated into cohorts of up to ~27 patients), supplemented by animal-model (mouse, zebrafish) and cell-based electrophysiological studies — i.e., a mix of individual clinical observation and structured multi-patient cohort synthesis, not large-scale registries.

---

## 2. Etiology

**Disease causal factors — genetic, monogenic.** DEE47 is caused by heterozygous, usually de novo, **gain-of-function** missense variants in FGF12, which encodes an intracellular fibroblast growth factor homologous factor (FHF1) that binds the C-terminal cytoplasmic tail of neuronal voltage-gated sodium channels (Nav1.2/SCN2A, Nav1.6/SCN8A, and cardiac Nav1.5/SCN5A) to modulate channel inactivation ([Siekierska et al. 2016, PMID:27164707](https://www.neurology.org/doi/10.1212/WNL.0000000000002752); [Life Science Alliance 2023, PMID:37286232](https://www.life-science-alliance.org/content/6/8/e202302025)).

**Recurrent causal variants:**
- **p.Arg52His (R52H in the B-isoform; equivalently R114H in the A-isoform)** — the most frequently reported de novo missense variant, at a highly conserved residue that contacts the Nav cytoplasmic tail, disrupting fast-inactivation modulation ([OMIM #617166](https://omim.org/entry/617166); [Siekierska et al. 2016](https://www.neurology.org/doi/10.1212/WNL.0000000000002752); [Villeneuve et al. 2016, Neurol Genet, PMID:27830185](https://www.neurology.org/doi/10.1212/NXG.0000000000000115)).
- **p.Gly50Ser / p.Gly112Ser** — a second recurrent variant, reported to have a distinct, more explosive/later-onset seizure phenotype compared with R52H ([Pierret et al. 2025, Epilepsia, PMID:40488543](https://onlinelibrary.wiley.com/doi/10.1111/epi.18495)).
- **c.334G>A / c.341G>A** and other private missense variants reported in individual case reports (e.g., seizure-free on VPA+topiramate combination therapy; PMID:34020858; iPSC line generation from a c.334G>A patient, PMID:37331110).
- **p.Ser8Pro (S8P)** — a novel variant reported in a patient with autism spectrum disorder and developmental delay **without seizures**, illustrating the phenotypic breadth beyond classic DEE ([modulating effects case series, PMID:36029553](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(22)00416-9/fulltext)).
- **Copy number variants (whole-gene or intragenic duplications)** — de novo intragenic tandem duplications (e.g., exons 1–4) and full-gene duplications produce a phenytoin-responsive epileptic encephalopathy phenotype, including via complex chromosomal rearrangements causing West syndrome ([Neurol Genet 2017, PMC7371371](https://pmc.ncbi.nlm.nih.gov/articles/PMC7371371/); [Uehara et al. 2019, J Hum Genet, PMID:31311986](https://www.nature.com/articles/s10038-019-0641-1); Willemsen et al. 2020, PMID:32524056; long-read sequencing of recurrent duplications, PMID:40838839).
- **Biallelic (recessive) structural/loss-of-function variants** — a 2023 report using long-read sequencing identified the **first biallelic intragenic structural variants** in FGF12, causing DEE via a **loss-of-function** mechanism, contrasting with the dominant gain-of-function paradigm ([PMID:37286232](https://www.life-science-alliance.org/content/6/8/e202302025)).

**Risk factors:**
- **Genetic:** de novo occurrence is the norm; germline mosaicism has been reported in at least one family, carrying recurrence-risk implications for genetic counseling.
- No established environmental, infectious, or lifestyle risk factors — this is a monogenic ion-channel-regulatory disorder.
- **Protective factors:** none specifically documented; early recognition and use of sodium-channel-blocking antiseizure medications appears to modify (improve) outcome rather than prevent disease.

**Gene-environment interactions:** None reported; this is a purely monogenic condition with expression driven by the underlying channelopathy mechanism.

---

## 3. Phenotypes

**Core phenotype — epilepsy (symptom/clinical sign):**
- **Onset:** neonatal to early infantile — "the first days or weeks of life" in the classic severe form ([OMIM #617166](https://omim.org/entry/617166)); all patients in the broadened cohort developed epilepsy before 5 months of age ([Pierret et al. 2025, PMID:40488543](https://onlinelibrary.wiley.com/doi/10.1111/epi.18495)).
- **Seizure types:** tonic seizures are the most common seizure type reported; also focal seizures, migrating focal seizures of infancy (EIMFS phenotype), infantile spasms/hypsarrhythmia, and generalized seizures.
- **Diagnoses spanned:** early infantile epileptic encephalopathy (EIEE/Ohtahara-spectrum), epilepsy of infancy with migrating focal seizures (EIMFS), West syndrome (infantile spasms), and — in the milder/broadened spectrum — drug-responsive focal epilepsy without encephalopathy.
- **Severity/course:** historically described as intractable/refractory with developmental regression; more recent broader ascertainment shows a spectrum from severe DEE to **drug-responsive epilepsy with favorable cognitive outcome** — ~70% of patients in one 10-patient cohort achieved seizure remission within 6 months of antiseizure medication, with favorable long-term neurodevelopmental outcome over median 6.8-year follow-up (PMID:40488543).
- **EEG:** background slowing, multifocal epileptiform spikes; may show hypsarrhythmia.

**Neurodevelopmental/cognitive phenotype:**
- Development is typically normal before seizure onset in the classic form.
- Developmental regression after seizure onset is common in the severe phenotype; persistent intellectual disability and neurologic impairment of variable severity.
- One larger-cohort synthesis: 79.1% of patients showed moderate-to-severe intellectual disability (cohort context: PMID:42057324/related reviews).
- Milder end of spectrum: normal to near-normal cognitive outcome when seizures are well controlled early.
- Autism spectrum disorder has been reported (in a patient with a novel S8P variant, without seizures) (PMID:36029553).

**Neuroimaging phenotype:**
- Mild cerebral and/or cerebellar atrophy reported in a substantial minority (~41.6%) of cases, correlating with more severe phenotype; the original Siekierska et al. report specifically described "cerebellar atrophy" as a feature (PMID:27164707). Patients with favorable outcome/drug-responsive epilepsy show no cerebellar atrophy (PMID:40488543).

**Cardiac phenotype (emerging):**
- Ictal asystole requiring pacemaker implantation has been reported in a 9-year-old with an FGF12 pathogenic variant (PMID:40897676), consistent with the cardiac Nav1.5-modulatory role of FHF1 and the cardiac arrhythmia/SUDEP phenotype demonstrated in mouse models (see Mechanism and Model Organisms below).
- Apnea attacks and partial mitochondrial respiratory chain complex II deficiency were reported in one heterogeneous case (PMID:28506426).

**Suggested HPO terms:**
- HP:0011097 Epileptic spasm
- HP:0002187 Intractable epilepsy
- HP:0032794 Focal-onset seizure
- HP:0011146 Focal seizures with impaired awareness
- HP:0007186 Cerebellar atrophy
- HP:0001263 Global developmental delay
- HP:0001249 Intellectual disability
- HP:0002194 Delayed gross motor development
- HP:0000006 Autosomal dominant inheritance
- HP:0011168 Generalized tonic seizure
- HP:0011177 Multifocal epileptiform discharges
- HP:0011200 EEG with hypsarrhythmia
- HP:0000708 Behavioral abnormality (autism)
- HP:0001645 Sudden cardiac death / HP:0031547 asystole (context-dependent, cardiac arrhythmia)

**Quality of life impact:** Not separately quantified in the literature reviewed; qualitatively, the severe end of the spectrum imposes major burden via intractable seizures, developmental regression, and (rarely) SUDEP risk, whereas the drug-responsive end permits favorable developmental trajectories.

---

## 4. Genetic / Molecular Information

**Gene:** FGF12 (HGNC symbol FGF12; also FHF1, FGF12B); located at **chromosome 3q28** (some sources: 3q28-q29). Gene structure: **4 introns and 5 coding exons**, with alternative splicing producing two isoforms — the shorter **isoform B** and longer **isoform A** ("FGF12: biology and function," PMID:38042708).

**Protein:** Fibroblast growth factor homologous factor 1 (FHF1), a member of the **FGF11 subfamily of intracellular FGFs (iFGFs, FHFs 1–4)**, structurally related to canonical FGFs (β-trefoil fold core domain) but functioning intracellularly rather than as secreted mitogens (though limited non-canonical secretion has recently been reported). FHF1 is highly expressed in excitable cells — neurons (hippocampus, cortex, cerebellum) and cardiomyocytes — where it binds the C-terminal cytoplasmic tail of voltage-gated sodium channel alpha subunits (**Nav1.2/SCN2A, Nav1.5/SCN5A, Nav1.6/SCN8A**) to modulate fast and long-term inactivation gating (PMID:38042708; PMID:37286232).

**Pathogenic variant classes:**
| Variant type | Example | Mechanism | Reference |
|---|---|---|---|
| Recurrent missense (dominant, de novo) | p.Arg52His (=R114H isoform A) | Gain of function — weakened FHF1–Nav tail interaction → depolarizing shift in fast inactivation → enhanced Nav1.6/Nav1.2 currents | PMID:27164707, 27830185 |
| Recurrent missense | p.Gly50Ser / p.Gly112Ser | Gain of function, distinct kinetic profile (later/more explosive onset) | PMID:40488543 |
| Private missense | c.334G>A, c.341G>A, others | Gain of function | PMID:34020858, 37331110 |
| Novel missense (non-epilepsy phenotype) | p.Ser8Pro | Mixed loss-/gain-of-function kinetic effects on Nav1.2/Nav1.6 | PMID:36029553 |
| Whole-gene / intragenic duplication | exon 1–4 tandem duplication; full-gene duplication | Presumed dosage/gain-of-function; phenytoin-responsive | PMID:31311986, 32524056, 40838839, PMC7371371 |
| Biallelic structural variants (recessive) | intragenic SVs, compound state | **Loss of function** | PMID:37286232 |

**Variant classification:** Per ACMG/AMP criteria as captured in ClinVar, recurrent variants such as NM_004113.6(FGF12):c.155G>A (p.Arg52His) are classified **Pathogenic** for "Developmental and epileptic encephalopathy, 47" ([ClinVar RCV000258032](https://www.ncbi.nlm.nih.gov/clinvar/RCV000258032/)).

**Functional consequences — the central mechanism:** In heterologous expression systems (transfected Neuro2A cells), mutant FHF1 (R52H) produces a **strong gain-of-function** effect: enhanced depolarizing shifts in Nav1.6 voltage-dependent fast inactivation, predicted to increase neuronal excitability. The mechanistic basis is a **weaker interaction of mutant FHF1 with the Nav cytoplasmic tail**, paradoxically producing gain-of-function kinetics rather than simple loss of channel modulation ([bioRxiv/eBioMedicine, PMID:36029553](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(22)00416-9/fulltext)). Other variants (G50S/G112S, S8P) produce a "complex kinetic influence... including loss- as well as gain-of-function changes in fast and slow inactivation" on both Nav1.2 and Nav1.6, explaining phenotypic heterogeneity across variants.

**Allele frequency:** Not established in population databases (gnomAD) as these are ultra-rare, largely private de novo pathogenic variants; no population carrier frequency data identified.

**Modifier genes / epigenetics / chromosomal abnormalities:** No modifier genes reported. No specific epigenetic (DNA methylation/histone) studies identified for FGF12-DEE specifically. Chromosomal-level involvement is limited to the described 3q28 duplications/complex rearrangements encompassing FGF12.

**Suggested ontology terms:**
- GO:0005112 Notch binding (not applicable) — more relevant: GO:0044324 regulation of voltage-gated sodium channel activity; GO:0086006 voltage-gated sodium channel activity involved in cardiac muscle cell action potential; GO:0086010 membrane depolarization during action potential
- GO:0007507 heart development / GO:0007399 nervous system development (broad context)
- CHEBI: n/a (not a small-molecule disease)
- UniProt: P61328 (FGF12_HUMAN)

---

## 5. Environmental Information

No environmental toxins, lifestyle factors, or infectious triggers have been identified as causal or modifying for FGF12-DEE — it is a monogenic channelopathy. Antiseizure medication choice (see Treatment) is the dominant modifiable factor affecting clinical course, not an "environmental" exposure in the traditional sense.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular lesion:** De novo heterozygous gain-of-function missense variant (e.g., p.Arg52His) in FGF12/FHF1, or a gene-dosage change (duplication), alters the FHF1 protein's interaction with the intracellular C-terminal tail of neuronal voltage-gated sodium channels.
2. **Channel biophysics:** Mutant FHF1 binds Nav1.2 and Nav1.6 (and, for cardiac phenotypes, Nav1.5) with altered affinity, producing a **depolarizing shift in the voltage-dependence of fast inactivation** and complex effects on slow inactivation and recovery from inactivation — net effect is typically **enhanced (gain-of-function) persistent/window sodium current**.
3. **Cellular electrophysiology:** Increased sodium current availability and delayed fast inactivation **increase intrinsic neuronal excitability**. This has been directly confirmed by patch-clamp recordings showing increased excitability in hippocampal CA3 pyramidal neurons in a mouse model (FGF12^ΔV52H) (ScienceDirect 2024, "Phenotyping of FGF12^ΔV52H mutation in mouse implies a complex FGF12 network").
4. **Network/circuit level:** Hyperexcitable cortical, hippocampal, and cerebellar circuits generate epileptiform activity, demonstrated directly in a zebrafish overexpression/knock-in model showing epileptiform discharges (PMID:27164707).
5. **Cardiac arm:** The same FHF1–Nav interaction occurs in cardiomyocytes via Nav1.5, and mouse knock-in models (Fhf1^R52H/+) show **cardiac arrhythmia and bradycardia** contributing to sudden unexpected death in epilepsy (SUDEP) — paralleling the analogous Scn8a gain-of-function (p.Asn1768Asp) mouse model, supporting a shared **"FHF1/Nav1.6 functional axis"** in brain and heart (PMID:33982289).
6. **Clinical output:** Neonatal/infantile-onset intractable seizures (tonic, focal, migrating focal, spasms), developmental regression/intellectual disability of variable severity, occasional cerebellar/cerebral atrophy on MRI, and — in a subset — cardiac conduction abnormalities/SUDEP risk.

**Divergent (loss-of-function) arm:** Biallelic structural FGF12 variants instead reduce/eliminate FHF1's normal delay of Nav channel fast inactivation, i.e., a **loss-of-function mechanism** also producing DEE — indicating that both increased and decreased FHF1-mediated modulation of the same channels can destabilize network excitability, analogous to other channelopathy genes with bidirectional GOF/LOF disease mechanisms (PMID:37286232).

**Molecular pathway:** Not a classical signaling cascade (Wnt/MAPK/mTOR) — the relevant "pathway" is direct **protein–ion channel modulation** (FHF1–Nav1.2/1.5/1.6 C-terminal tail interaction), distinguishing FHF1 pathophysiology mechanistically from canonical growth-factor-receptor FGF signaling.

**Cell types involved:** Cortical and hippocampal excitatory pyramidal neurons (notably CA3), cerebellar neurons (Purkinje cells, by analogy to paralog FGF14/FHF4 biology), and cardiomyocytes (via Nav1.5).

**Suggested GO terms:** GO:0086010 (membrane depolarization during cardiac muscle cell action potential), GO:1902480 (regulation of the voltage-gated sodium channel), GO:0044309 (neuron spine), GO:0034765 (regulation of ion transmembrane transport)
**Suggested CL terms:** CL:0000598 (pyramidal neuron), CL:0001031 (cerebellar Purkinje cell), CL:0000746 (cardiac muscle cell)

**Advanced/omics data:** iPSC-derived neuronal models have been generated from a patient carrying c.334G>A (PMID:37331110), enabling future electrophysiological and transcriptomic studies; no large-scale transcriptomic/proteomic/metabolomic datasets specific to FGF12-DEE were identified in this search.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system (brain — cerebral cortex, hippocampus, cerebellum). **Secondary:** heart (conduction system), via the shared Nav-channel-modulatory mechanism.
- **Body systems:** Nervous system (primary), cardiovascular system (secondary, arrhythmia/SUDEP risk).
- **Tissue/cell level:** Cerebral and cerebellar cortex (mild atrophy on imaging in ~41.6% of more severely affected patients); excitatory pyramidal neurons; cerebellar Purkinje-cell circuitry (by mechanistic analogy with paralog FHF4/FGF14); cardiomyocytes/conduction tissue.
- **Subcellular level:** FHF1 protein localizes intracellularly — nucleus, nucleolus, and cytoplasm — and acts at the **plasma membrane** at the site of the sodium-channel C-terminal tail (GO Cellular Component: plasma membrane, voltage-gated sodium channel complex).
- **UBERON suggestions:** UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0001954 (Ammon's horn/hippocampus), UBERON:0000948 (heart), UBERON:0002382 (cardiac conduction system).
- **Laterality:** Not applicable (diffuse/bilateral CNS process).

---

## 8. Temporal Development

- **Onset:** Neonatal to early infantile — seizures typically begin within the first days to weeks of life in the classic severe DEE47 phenotype; all patients in the broadened cohort had epilepsy onset before 5 months of age (PMID:40488543). Development is typically normal *before* seizure onset.
- **Onset pattern:** Acute onset of seizures, sometimes explosive (particularly with the G50S/G112S variant) versus a more gradual onset pattern (more typical of R52H) (PMID:40488543).
- **Progression:** Variable — ranges from a **progressive, refractory course with developmental regression** (classic severe DEE47) to **stabilization/remission** with early, effective antiseizure treatment (milder end of spectrum).
- **Disease course pattern:** Can be intractable/refractory (frequent, difficult-to-control seizures with persistent neurologic impairment) or **drug-responsive with seizure remission** (up to 70% achieving remission within 6 months on ASMs in a favorable-outcome cohort).
- **Critical window:** Early, precision-guided initiation of sodium-channel-blocking antiseizure medication appears to be a critical intervention window associated with better long-term cognitive/developmental outcome.
- **Duration:** Chronic, lifelong condition; in a minority of severe cases, mortality can occur early via SUDEP-like mechanisms (supported by mouse model data — see below).

---

## 9. Inheritance and Population

- **Prevalence/Incidence:** No formal population prevalence or incidence estimates are available; this is an ultra-rare Mendelian condition identified through targeted or exome/genome sequencing in patients with epilepsy, with fewer than ~30–40 patients cumulatively reported in the literature to date (aggregated across the ~27-patient and other smaller cohorts identified in this search).
- **Inheritance pattern:** **Autosomal dominant**, almost always **de novo**, for the classic missense gain-of-function and duplication forms. A **recessive (biallelic) form** has now also been described via loss-of-function structural variants (PMID:37286232) — representing an important, newly recognized second inheritance mode.
- **Penetrance:** Appears high/complete for the recurrent de novo missense variants given consistent early-onset phenotypes, though expressivity (severity) is variable.
- **Expressivity:** Markedly variable — from severe intractable DEE with developmental regression and cerebellar atrophy, to drug-responsive epilepsy with normal-to-near-normal cognitive outcome, to seizure-free autism/developmental-delay presentations (S8P variant).
- **Germline mosaicism:** Reported in at least one family, with implications for recurrence risk counseling in ostensibly "de novo" cases.
- **Founder effects / geographic distribution:** No founder populations identified; cases reported worldwide, including cohorts from Japan (PMID for "Two Japanese cases" report), Turkey (129-patient DEE cohort including FGF12 cases, PMID:41153369), Europe, and North America.
- **Sex ratio:** Not specifically reported as skewed; autosomal gene, no clear sex predilection identified in the literature reviewed.
- **Consanguinity:** Relevant specifically to the newly described **biallelic (recessive) form**, where both parental alleles must be transmitted.

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES) / whole genome sequencing (WGS)** — the primary route of discovery for de novo missense and many CNV cases; trio WES/WGS is standard for suspected genetic epilepsy/DEE.
- **Long-read sequencing** — specifically valuable for detecting **intragenic structural variants/duplications** in FGF12 that short-read exome sequencing can miss, as demonstrated in both the biallelic LOF cases (PMID:37286232) and recurrent intragenic duplication cases (PMID:40838839).
- **Chromosomal microarray (CMA)** — can detect larger duplications/complex rearrangements encompassing FGF12 (e.g., West-syndrome-associated 3q28 rearrangement, PMID:31311986).
- **Gene panels for early-onset/DEE** — FGF12 is included in clinical epilepsy gene panels (e.g., Genomics England PanelApp, "Early onset or syndromic epilepsy" panel).
- **Single-gene testing/Sanger confirmation** of recurrent hotspot variants (R52H, G50S/G112S) is reasonable given their recurrence.

**Clinical/EEG/imaging:**
- **EEG:** background slowing, multifocal epileptiform discharges, possible hypsarrhythmia.
- **Brain MRI:** may show mild cerebral and/or cerebellar atrophy in more severely affected patients (~41.6%); typically normal in the drug-responsive/favorable-outcome subgroup.
- **Cardiac evaluation (ECG/Holter)** — increasingly recommended given emerging reports of ictal asystole and the mouse-model cardiac arrhythmia/SUDEP phenotype; a reasonable diagnostic consideration once the genetic diagnosis is established.

**Functional/precision diagnostics:** In-vitro electrophysiological characterization of a patient's specific variant (heterologous Nav1.2/Nav1.6 co-expression assays) can clarify gain- vs loss-of-function status, informing precision antiseizure drug selection (PMID:36029553).

**Differential diagnosis:** Other early-onset DEEs/EIEE genes — SCN1A, SCN2A, SCN8A, KCNQ2, STXBP1, CDKL5, FGF13(FHF2), and syndromes presenting as Ohtahara syndrome, EIMFS, or West syndrome; genetic testing is required to distinguish these clinically overlapping entities.

**Screening:** No population-level newborn or carrier screening program exists for this ultra-rare condition; diagnosis is reactive, triggered by neonatal/infantile-onset refractory epilepsy.

---

## 11. Outcome / Prognosis

- **Mortality:** No formal human mortality statistics are available, but **SUDEP is a plausible and mechanistically supported risk**, based directly on the Fhf1^R52H/+ mouse model, in which mice die of sudden death with cardiac arrhythmia/bradycardia around postnatal day 16–20, and on the human case report of ictal asystole requiring pacemaker implantation (PMID:33982289; PMID:40897676).
- **Morbidity/function:** Ranges from severe, persistent intellectual disability and neurologic impairment (moderate-to-severe ID reported in ~79% of one cohort) to normal/near-normal developmental outcome in the favorable, drug-responsive subgroup.
- **Complications:** Developmental regression, refractory epilepsy, cerebral/cerebellar atrophy, cardiac arrhythmia/ictal asystole (emerging).
- **Recovery potential:** Substantially improved by **early recognition of the genetic diagnosis and prompt initiation of sodium-channel-blocking antiseizure medications** — the single most consistent prognostic modifier identified across the literature. In one cohort, patients started promptly on sodium channel blockers achieved seizure freedom with good developmental outcomes in 8/12 cases, versus DEE in the remainder.
- **Prognostic factors:** Specific variant identity (R52H vs G50S/G112S vs biallelic LOF) correlates with onset pattern and severity; presence of cerebellar/cerebral atrophy on MRI correlates with worse prognosis; timing of ASM initiation is a key modifiable prognostic factor.

---

## 12. Treatment

**Pharmacotherapy — precision, mechanism-guided sodium-channel blockade** is the central treatment strategy, reflecting the gain-of-function Nav-channel mechanism:

- **Phenytoin** — repeatedly reported as effective, including in the original discovery families and multiple subsequent case reports; a hallmark "diagnostic-therapeutic" indicator for FGF12-DEE (PMID:38465135; original Neurology Genetics duplication report, e133).
- **Carbamazepine** — the most commonly used agent among achieving-remission patients in the largest recent cohort (used in 6/10 patients; 4/? achieved remission specifically on carbamazepine) (PMID:40488543).
- **Oxcarbazepine** — used successfully in at least one patient achieving remission (PMID:40488543).
- **High-dose phenobarbital** — effective in some early reports (e.g., epilepsy of infancy with migrating focal seizures phenotype responded to phenytoin and high-dose phenobarbital).
- **Valproic acid (VPA) + topiramate (TPM) combination therapy** — reported as effective (seizure freedom in all three probands with the c.341G>A variant), with two patients showing improved motor/cognitive function; the first documented report of this specific combination's efficacy for an FGF12 variant (PMID:34020858).
- **Lamotrigine** — used successfully in at least one remission case in the broadened cohort.
- **General class:** across cohorts, **sodium channel blockers as a class** are "commonly associated with clinical improvement," and specific FGF12 variants "may be amenable to precision treatment with sodium channel blockers" (PMID:36029553; PMID:42057324/PMID:42185328 review cohorts).

**Pharmacogenomic caution:** Because the biallelic/structural-variant form of FGF12-DEE operates via a **loss-of-function** mechanism, sodium-channel-blocker responsiveness cannot necessarily be assumed for all FGF12 variants — precision therapy selection should ideally be informed by variant-specific functional data (gain- vs loss-of-function) rather than gene identity alone.

**Advanced/experimental therapeutics:** No gene therapy, ASO, or targeted biologic therapies specific to FGF12-DEE were identified in the literature reviewed; the mechanistic/precision approach to date is limited to selection among existing sodium-channel-blocking antiseizure medications.

**Supportive/rehabilitative care:** Physical, occupational, and speech therapy are standard supportive measures for the neurodevelopmental impairment component, though not specifically studied in this population.

**Cardiac monitoring/management:** Given the emerging cardiac-arrhythmia/SUDEP signal, cardiac evaluation and, in select cases, pacemaker implantation (as already reported for ictal asystole) may be part of a comprehensive management strategy (PMID:40897676). Atenolol has been shown in the analogous mouse SUDEP model to reduce cardiac-mediated mortality, suggesting a possible (as-yet unstudied in humans) beta-blocker strategy for cardiac risk mitigation (biorxiv 2023, "Atenolol reduces cardiac-mediated mortality in genetic mouse model of sudden unexpected death in epilepsy").

**Suggested NCIT terms:**
- NCIT:C15986 Pharmacotherapy (parent term)
- Therapeutic agents (CHEBI/NCIT): phenytoin (CHEBI:8107), carbamazepine (CHEBI:3564), oxcarbazepine (CHEBI:7824), phenobarbital (CHEBI:8069), valproic acid (CHEBI:39867), topiramate (CHEBI:9646), lamotrigine (CHEBI:6367)
- NCIT:C15315 Rehabilitation (supportive/rehabilitative care)
- NCIT:C15289 Organ Transplantation / device-related — not applicable; pacemaker implantation would fall under NCIT:C15329 Surgical Procedure / device category

**Treatment algorithm implication:** Because this is a **sodium-channelopathy**, clinicians and guideline literature explicitly caution **against** the use of sodium-channel-blocker-contraindicated regimens typical in some other DEEs, mirroring the precision-medicine logic already established for SCN2A/SCN8A gain-of-function epilepsies.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies specific to FGF12-DEE exist, as it is caused by de novo variants not amenable to population-level prevention. The relevant "prevention" activities identified in the literature are:
- **Genetic counseling** for families with a diagnosed proband, particularly given the documented occurrence of germline mosaicism (recurrence risk counseling) and the newly recognized recessive/biallelic form (carrier-based reproductive risk assessment in consanguineous or carrier-carrier couples).
- **Prenatal/preimplantation genetic testing** could theoretically be offered once a familial variant is identified (mosaicism or biallelic carrier couple), though no specific reports of this were found for FGF12.
- **Secondary prevention** — early genetic diagnosis enabling prompt, mechanism-guided sodium-channel-blocker therapy functions as a de facto "prevention" of the worst neurodevelopmental outcomes, per the outcome data above.
- No immunization, public health, or population screening programs apply to this ultra-rare monogenic disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease attributable to FGF12/FHF1 variants has been reported in the literature reviewed. FGF12 orthologs are broadly conserved across vertebrates (used experimentally in mouse and zebrafish, see below), but no OMIA (Online Mendelian Inheritance in Animals) entries or spontaneous animal disease reports were identified.

---

## 15. Model Organisms

**Mouse models:**
- **Fhf1^R52H/+ knock-in mice** (CRISPR-edited to carry the human-equivalent p.Arg52His mutation) — recapitulate **early-onset epilepsy and SUDEP with cardiac arrhythmia**. EEG at postnatal day 19–20 confirmed severe tonic seizures immediately preceding loss of brain activity and death; mice die around day 16 (spontaneous seizures and SUDEP), with phenytoin only marginally prolonging survival (to ~day 19) (Velíšková et al. 2021, Epilepsia, **PMID:33982289**). This model directly parallels the human phenotype and demonstrates a shared **FHF1/Nav1.6 functional axis** with the analogous Scn8a p.Asn1768Asp gain-of-function mouse model.
- **FGF12^ΔV52H mice** — a related model showing increased excitability in dorsal hippocampal CA3 neurons by patch-clamp recording and seizure susceptibility (without necessarily showing spontaneous seizures), implicating a "complex FGF12 network" (ScienceDirect 2024).
- **Atenolol intervention study** — in the genetic SUDEP mouse model, the beta-blocker atenolol reduced cardiac-mediated mortality, supporting a translatable cardioprotective strategy (bioRxiv 2023).
- **Neuro2A (N2A) transfection studies** — heterologous cell system used to characterize gain-of-function shifts in Nav1.6/Nav1.2 fast-inactivation kinetics induced by mutant FHF1, foundational for establishing the molecular mechanism (PMID:27164707, PMID:36029553).

**Zebrafish models:**
- **Zebrafish overexpression/knock-in of mutant FHF1 (R52H/R114H equivalent)** — showed increased neuronal excitability and **epileptiform activity**, directly supporting the gain-of-function disease mechanism in vivo in a second vertebrate model system (Siekierska et al. 2016, **PMID:27164707**).

**Cellular/iPSC models:**
- **Patient-derived induced pluripotent stem cell (iPSC) line** generated from a patient carrying the FGF12 c.334G>A variant, intended to enable neuronal differentiation and disease modeling of "developmental epileptic encephalopathy" pathogenesis (PMID:37331110).

**Model recapitulation and limitations:** The mouse Fhf1^R52H/+ model recapitulates both the seizure phenotype and, notably, the emerging **cardiac arrhythmia/SUDEP** phenotype now also observed clinically in humans (ictal asystole case, PMID:40897676) — an unusually strong translational correlation. Limitations include the mouse model's very early lethality (~postnatal day 16–20), which may limit study of the milder, drug-responsive, favorable-cognitive-outcome end of the human phenotypic spectrum; and the zebrafish model's inherent differences in nervous system complexity relative to humans.

---

## Summary Table: Key PMIDs Cited

| PMID | Study | Key contribution |
|---|---|---|
| 27164707 | Siekierska et al. 2016, Neurology | Original R52H/R114H discovery; zebrafish + cell GOF model; cerebellar atrophy |
| 27830185 | Villeneuve et al. 2016, Neurol Genet | 3 more R52H patients; infancy-to-adulthood spectrum |
| 33982289 | Velíšková et al. 2021, Epilepsia | Fhf1^R52H/+ mouse: SUDEP, cardiac arrhythmia |
| 34020858 | — | VPA+TPM combination effective for c.341G>A |
| 36029553 | — (eBioMedicine) | Complex GOF/LOF kinetic effects; S8P autism-only variant |
| 37286232 | — (Life Science Alliance) | First biallelic/recessive LOF FGF12-DEE, long-read sequencing |
| 37331110 | — | iPSC line from FGF12 c.334G>A patient |
| 40488543 | Pierret et al. 2025, Epilepsia | 10-patient cohort; G50S/R52H; drug-responsive favorable-outcome phenotype |
| 40838839 | — | Long-read sequencing of recurrent intragenic duplications |
| 40897676 | — | Ictal asystole/pacemaker case |
| 31311986 | Uehara et al. 2019, J Hum Genet | Full FGF12 duplication → West syndrome |
| 38042708 | — | "FGF12: biology and function" review |
| 42057324 / 42185328 | Aldurayhim et al. / related 2026 cohorts | 27- and 12-patient cohorts; sodium channel blocker response rates |

---

## Sources

- [OMIM #617166 — Developmental and Epileptic Encephalopathy 47](https://omim.org/entry/617166)
- [OMIM *601513 — FGF12 gene entry](https://omim.org/entry/601513)
- [Siekierska et al., "Gain-of-function FHF1 mutation causes early-onset epileptic encephalopathy with cerebellar atrophy," Neurology 2016 (PMID:27164707)](https://www.neurology.org/doi/10.1212/WNL.0000000000002752)
- [Villeneuve et al., "FHF1 (FGF12) epileptic encephalopathy," Neurol Genet 2016 (PMID:27830185)](https://www.neurology.org/doi/10.1212/NXG.0000000000000115)
- [Velíšková et al., "Early onset epilepsy and sudden unexpected death in epilepsy with cardiac arrhythmia in mice carrying the... FHF1(FGF12) missense mutation," Epilepsia 2021 (PMID:33982289)](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.16916)
- [Pierret et al., "Broadening the phenotype associated with pathogenic variants in the FGF12 gene," Epilepsia 2025 (PMID:40488543)](https://onlinelibrary.wiley.com/doi/10.1111/epi.18495)
- ["Effective treatments for FGF12-related early-onset epileptic encephalopathies patients" (PMID:34020858)](https://pubmed.ncbi.nlm.nih.gov/34020858/)
- ["Modulating effects of FGF12 variants on NaV1.2 and NaV1.6... A case series," eBioMedicine (PMID:36029553)](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(22)00416-9/fulltext)
- ["Biallelic structural variations within FGF12 detected by long-read sequencing in epilepsy," Life Science Alliance (PMID:37286232)](https://www.life-science-alliance.org/content/6/8/e202302025)
- ["Long-read sequencing of recurrent FGF12 duplications in epilepsy"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12779332/)
- ["Generation of iPSC line from FGF12 mutation patient" (PMID:37331110)](https://pubmed.ncbi.nlm.nih.gov/37331110/)
- [Uehara et al., "Entire FGF12 duplication by complex chromosomal rearrangements associated with West syndrome," J Hum Genet 2019 (PMID:31311986)](https://pubmed.ncbi.nlm.nih.gov/31311986/)
- ["Childhood-onset epileptic encephalopathy due to FGF12 exon 1–4 tandem duplication"](https://pmc.ncbi.nlm.nih.gov/articles/PMC7371371/)
- ["Ictal Asystole in a Patient With DEE due to an FGF12 Pathogenic Variant" (PMID:40897676)](https://pubmed.ncbi.nlm.nih.gov/40897676/)
- ["FGF12: biology and function" review (PMID:38042708)](https://pubmed.ncbi.nlm.nih.gov/38042708/)
- ["FGF12‐Related Early‐Onset Epileptic Encephalopathies: Therapeutic Response to Sodium Channel Blockers," AJMG A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.70182)
- [Orphanet — FGF12-fibroblast growth factor 12](https://www.orpha.net/en/disease/gene/FGF12?name=FGF12&mode=gene)
- [NORD/MONDO — Developmental and epileptic encephalopathy, 47](https://rarediseases.org/mondo-disease/developmental-and-epileptic-encephalopathy-47/)
- [ClinVar — NM_004113.6(FGF12):c.155G>A (p.Arg52His)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000258032/)
- [GeneCards — FGF12 Gene](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FGF12)
- [Genomics England PanelApp — FGF12 (Early onset or syndromic epilepsy)](https://panelapp.genomicsengland.co.uk/panels/402/gene/FGF12/)
- ["Atenolol reduces cardiac-mediated mortality in genetic mouse model of sudden unexpected death in epilepsy," bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.12.10.570964.full.pdf)
- ["Phenotyping of FGF12ΔV52H mutation in mouse implies a complex FGF12 network," ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0969996124002377)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 25 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42057324` *(abstract only)*: "may be amenable to precision treatment with sodium channel blockers"
  - closest text in source: "While treatment responses were heterogeneous, sodium channel blockers were commonly associated with clinical improvement"
- `PMID:42185328` *(abstract only)*: "may be amenable to precision treatment with sodium channel blockers"
  - closest text in source: "8 patients promptly started on sodium channel blockers became seizure-free with good developmental outcomes while 4 developed DEE"
- `PMID:37331110` *(abstract only)*: "Generation of iPSC line from FGF12 mutation patient"
  - closest text in source: "This study used non-insertion Sendai virus transfection to establish the induced pluripotent stem cells(iPSCs)line with FGF12 mutation"