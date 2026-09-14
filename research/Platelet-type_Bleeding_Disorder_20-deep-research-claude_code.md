---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-26T16:14:55.173131'
end_time: '2026-08-26T16:19:28.421668'
duration_seconds: 273.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Platelet-type Bleeding Disorder 20
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
  web_search_requests: 11
  num_turns: 24
  total_cost_usd: 1.2587878000000001
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 31
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 2
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:37041648
  - PMID:29678925
  - PMID:42213791
  relevance_assessed: 17
  on_topic: 15
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-type Bleeding Disorder 20
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Platelet-type Bleeding Disorder 20** covering all of the
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

I now have comprehensive data to compile the report.

I have sufficient data. Now compiling the comprehensive research report.

# Platelet-type Bleeding Disorder 20 (BDPLT20) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Platelet-type Bleeding Disorder 20 (BDPLT20), also known as SLFN14-related thrombocytopenia, is a rare autosomal dominant inherited platelet disorder characterized by moderate thrombocytopenia (often with macrothrombocytes/enlarged platelets), impaired platelet secretion (particularly ATP release from dense granules), and a lifelong mucocutaneous bleeding tendency. It was first delineated as a distinct clinical entity by Fletcher et al. in 2015, who identified heterozygous missense mutations in the *SLFN14* (Schlafen family member 14) gene as the molecular cause ([JCI, PMID: 26280575](https://pubmed.ncbi.nlm.nih.gov/26280575/)).

**Key Identifiers:**
- **OMIM:** #616913 — BLEEDING DISORDER, PLATELET-TYPE, 20; BDPLT20 ([OMIM entry](https://omim.org/entry/616913))
- **Gene locus (OMIM):** *614958 — SCHLAFEN FAMILY, MEMBER 14; SLFN14 ([OMIM entry](https://www.omim.org/entry/614958))
- **HGNC:** SLFN14, HGNC:32689
- **MONDO:** MONDO:0014830 ([ClinGen curation page](https://search.clinicalgenome.org/kb/conditions/MONDO:0014830))
- **MedGen:** C4310797 ([NCBI MedGen](https://ncbi.nlm.nih.gov/medgen/C4310797))
- **Orphanet:** ORPHA:466806 — SLFN14-related thrombocytopenia ([Orphanet gene page](https://www.orpha.net/en/disease/gene/SLFN14))
- **NCBI GTR:** [Genetic Testing Registry entry](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4310797/)
- Chromosomal location: 17q12

**Synonyms:** SLFN14-related thrombocytopenia; SLFN14-related macrothrombocytopenia; Inherited thrombocytopenia due to SLFN14 mutation.

**Evidence basis:** Nearly all published knowledge derives from individual patient/family case series and case reports (aggregated across roughly a dozen kindreds worldwide identified via next-generation sequencing in bleeding-disorder cohorts such as the UK GAPP [Genotyping and Phenotyping of Platelets] study), supplemented by mechanistic cell-line and mouse-model studies. There is no large-scale disease registry or population-level epidemiological dataset — this is characteristic of an ultra-rare monogenic platelet disorder.

---

## 2. Etiology

**Disease Causal Factor:** BDPLT20 is caused by heterozygous, dominantly acting missense (and at least one frameshift) mutations in *SLFN14*, which encodes an RNA endoribonuclease. This is a purely genetic/monogenic disorder — no environmental or infectious causal factors are described.

**Genetic Risk Factors:**
- Fletcher et al. (2015) identified three heterozygous missense mutations — **p.K218E, p.K219N, p.V220D** — clustered within an ATPase-associated-with-diverse-cellular-activities (AAA) GTP/ATP-binding domain, in 12 patients from 3 unrelated families ([PMID: 26280575](https://pubmed.ncbi.nlm.nih.gov/26280575/)).
- Marconi et al. (2016) reported an additional heterozygous missense mutation in an Italian family — **Thromb Haemost. 2016;115(5):1076-9** ([PMID: 26769223](https://pubmed.ncbi.nlm.nih.gov/26769223/)).
- A **p.R223W** substitution in the AAA domain, near previously reported residues, has also been described.
- A novel **c.1766T>C (p.L589S)** variant in the *helicase* domain was reported in 2025 in twin brothers with severe thrombocytopenia and abnormal megakaryocyte maturation — notably, the variant showed **incomplete penetrance**: "the mother and maternal grandmother showed no abnormal phenotypes" despite carrying the variant ([EJHaem 2025, PMID: 40521396](https://pubmed.ncbi.nlm.nih.gov/40521396/)).
- A frameshift variant, **T853fs**, was identified in the helicase domain in patients with inherited macrothrombocytopenia, distinct in mechanism from the AAA-domain missense variants ([Mol Ther Nucleic Acids 2025, PMID: 40510593](https://pubmed.ncbi.nlm.nih.gov/40510593/)).
- A novel variant was reported in a 17-year-old female with severe macrothrombocytopenia and giant platelets (>10 μm) ([Orphanet J Rare Dis 2023, PMID: 37041648](https://pubmed.ncbi.nlm.nih.gov/37041648/)).
- Maternal gonosomal (germline) mosaicism has been documented as a mechanism of transmission in at least one family, relevant to genetic counseling and recurrence-risk estimation ([Br J Haematol 2022, PMID: 36237120](https://pubmed.ncbi.nlm.nih.gov/36237120/)).
- Across the literature, **five heterozygous single-nucleotide substitutions have been reported, producing four distinct amino-acid changes (p.K218E, p.K219N, p.V220D, p.R223W)**, plus the more recently identified helicase-domain missense and frameshift variants.

**Risk Factor Databases:** Because this is a single-gene autosomal dominant disorder with no described modifier genes, environmental risk factors, or GWAS-identified susceptibility loci, the standard PheGenI/GWAS Catalog/CTD resources return no relevant hits — risk is essentially binary (carrying a pathogenic *SLFN14* variant vs. not), modulated somewhat by variant location (AAA-ATPase domain vs. helicase domain) and possibly by mosaicism/penetrance effects.

**Protective Factors:** None reported in the literature; there are no known protective genetic variants or environmental protective factors specific to BDPLT20.

**Gene-Environment Interactions:** Not described; this is a purely cell-intrinsic, monogenic disorder of megakaryocyte/platelet biology.

---

## 3. Phenotypes

### Clinical/hemorrhagic phenotypes (symptoms and signs)
Based on the original description of a 9-member, 3-generation family (proband: 31-year-old woman) and subsequent case series:

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Easy/frequent bruising | HP:0000978 (Bruising susceptibility) | Common presenting feature |
| Prolonged bleeding from minor wounds | HP:0031093 (Post-traumatic bleeding) / HP:0025153 | |
| Menorrhagia / heavy menstrual bleeding | HP:0000132 (Menorrhagia) | Frequently reported in adult females; managed with tranexamic acid in at least one reported case |
| Postpartum hemorrhage | HP:0011024 (Abnormality of the gastrointestinal tract) — more precisely, no exact HPO term for PPH exists; often noted as free text | |
| Spontaneous muscle hematoma | HP:0031364 (Muscle hemorrhage) | |
| Epistaxis (spontaneous) | HP:0000421 (Epistaxis) | |
| Gum bleeding | HP:0000225 (Gingival bleeding) | |
| Bleeding after tooth extraction | HP:0031093 | |
| Severe hemorrhagic syndrome (in some patients) | — | One 17-year-old patient had severe bleeding requiring intervention |

### Laboratory/hematologic abnormalities
- **Thrombocytopenia** (HP:0001873) — typically "moderate" (platelet counts variably reduced, not typically in the severe <20×10⁹/L range in most reported families, though severe cases have been described in twin patients with the L589S variant)
- **Macrothrombocytes / enlarged platelets** (HP:0011877, Abnormal platelet volume) — a hallmark feature; one case report described "heterogeneity in cell size, including giant forms over 10 μm (normal size 1–5 μm) in diameter, with vacuolization" ([PMID: 37041648](https://pubmed.ncbi.nlm.nih.gov/37041648/))
- **Reduced platelet dense granules** — electron microscopy shows decreased dense-granule number
- **Impaired ATP secretion** on lumiaggregometry
- **Reduced platelet aggregation** in response to ADP, collagen, and PAR1 (thrombin-receptor peptide), with **normal response to arachidonic acid**
- **Impaired calcium mobilization and thrombus formation** in functional assays ([PMID: 37041648](https://pubmed.ncbi.nlm.nih.gov/37041648/))
- Abnormal megakaryocyte maturation/accumulation in bone marrow in severe pediatric cases ([PMID: 40521396](https://pubmed.ncbi.nlm.nih.gov/40521396/))

### Phenotype characteristics
- **Onset:** Lifelong/congenital — bleeding tendency present from an early age; some cases identified in childhood/adolescence (e.g., the 17-year-old proband), others diagnosed in adulthood after gynecologic or surgical bleeding.
- **Severity:** Variable — ranges from mild bruising/heavy menses to severe hemorrhagic syndromes in some patients (notably those with helicase-domain variants).
- **Progression:** Generally stable/chronic rather than progressive, though bleeding episodes are episodic (triggered by trauma, surgery, menstruation, childbirth).
- **Penetrance:** Incomplete in at least one reported kindred (asymptomatic carriers of the p.L589S variant), indicating that BDPLT20, unlike the classic AAA-domain-mutation families, may show variable expressivity/incomplete penetrance depending on variant location.

### Quality of life impact
No disease-specific QOL instrument data were identified in the literature (no EQ-5D/SF-36 studies specific to BDPLT20 were found); qualitatively, recurrent menorrhagia, easy bruising, and bleeding after minor trauma or dental/surgical procedures are described as impacting daily life and requiring proactive hemostatic management (e.g., prophylactic interventions before procedures).

---

## 4. Genetic/Molecular Information

**Causal Gene:** *SLFN14* (Schlafen family member 14), HGNC:32689, chromosome 17q12, OMIM *614958.

**Variant spectrum (reported to date):**

| Variant (protein) | Domain | Source |
|---|---|---|
| p.K218E | AAA-ATPase | Fletcher et al. 2015 (PMID: 26280575) |
| p.K219N | AAA-ATPase | Fletcher et al. 2015 (PMID: 26280575); modeled in mice as K208N |
| p.V220D | AAA-ATPase | Fletcher et al. 2015 (PMID: 26280575) |
| p.R223W | AAA-ATPase | Later report, near the K218/K219/V220 cluster |
| Marconi variant (missense) | — | Marconi et al. 2016 (PMID: 26769223), Italian family |
| p.L589S (c.1766T>C) | Helicase domain | 2025 case report, twin brothers (PMID: 40521396) |
| T853fs (frameshift) | Helicase domain | 2025 (PMID: 40510593) |
| Novel variant (unspecified) | — | 2023 Orphanet J Rare Dis case (PMID: 37041648) |

**Variant classification:** Reported variants are generally classified as pathogenic/likely pathogenic under ACMG/AMP criteria based on segregation with disease in affected families, absence/rarity in population databases (gnomAD), and functional evidence of protein dysfunction. ClinVar and ClinVar Miner catalog reported *SLFN14* variants associated with this condition ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-condition/Platelet-type%20bleeding%20disorder%2020)).

**Inheritance/transmission:** Autosomal dominant, with three original families showing clear dominant segregation. Reduced/incomplete penetrance has since been documented in at least one family (helicase-domain variant), and maternal germline/gonosomal mosaicism has been reported as an unusual transmission mechanism (PMID: 36237120), which is clinically important for recurrence-risk counseling of "de novo"-appearing cases.

**Functional consequences — gain vs. loss of function:** The mechanism is complex and domain-dependent:
- AAA-domain missense mutants (K218E, K219N, V220D) show **dramatically reduced protein expression due to post-translational degradation from protein misfolding**, and functional studies "propose a dominant-negative mechanism explaining heterozygous mutations in patients" ([RNA 2018, PMID: 29678925](https://pubmed.ncbi.nlm.nih.gov/29678925/)).
- A 2026 mechanistic study found that inherited-thrombocytopenia (IT)-linked mutations **alter SLFN14 RNA substrate specificity** rather than simply abolishing function: "IT-linked mutations alter SLFN14 RNA substrate specificity, enhancing depletion of type II tRNAs while reducing rRNA cleavage," triggering "ribosome stalling at codons decoded by type II tRNAs, stress signaling, and cell death" ([PLoS Biol 2026, PMID: 42213791](https://pubmed.ncbi.nlm.nih.gov/42213791/)) — i.e., a **neomorphic/altered-specificity** mechanism rather than simple loss-of-function.
- The T853fs helicase-domain frameshift shows **markedly reduced SLFN14 protein expression in patient platelets**, and — unlike AAA-domain mutants — "did not affect mitochondrial translation," instead disrupting "ion channels and dense granule" pathways ([PMID: 40510593](https://pubmed.ncbi.nlm.nih.gov/40510593/)), indicating locus/domain-specific mechanistic heterogeneity.

**Modifier genes:** None specifically established; genetic background (species-specific, per mouse-model data below) appears to strongly modulate phenotype expression.

**Somatic vs. germline:** All reported cases are germline; no somatic *SLFN14* thrombocytopenia has been reported (contrast with *SLFN14*'s described antiviral/RNase roles in other contexts).

**Allele frequency:** Population database (gnomAD) frequency data specific to the pathogenic variants were not detailed in available search results; given the ultra-rare disease status and dominant-negative/gain-of-function-like mechanism, pathogenic alleles are expected to be essentially absent or present only as extreme rarities in gnomAD.

---

## 5. Environmental Information

No environmental risk factors, lifestyle factors, or infectious triggers are described as causal for BDPLT20 — it is a purely monogenic disorder. (Note: *SLFN14* itself has been separately implicated in **antiviral RNase activity against double-stranded RNA** in unrelated contexts — "Human Schlafen 14 Cleavage of Short Double-Stranded RNAs Underpins its Antiviral Activity" — but this is a distinct biological role of the wild-type protein, not an environmental disease trigger for BDPLT20.)

---

## 6. Mechanism / Pathophysiology

### Molecular function of SLFN14
SLFN14 is an **RNA endoribonuclease** that colocalizes with ribosomes and cleaves RNA — preferentially rRNA and ribosome-associated mRNA — leading to endoribonucleolytically mediated RNA degradation ([RNA 2018, PMID: 29678925](https://pubmed.ncbi.nlm.nih.gov/29678925/)). A high-resolution cryo-EM structure (2025) revealed the SLFN14•RNA complex has "a medallion-like architecture" and that "metal-dependent acceptor stem cleavage requires the SLFN14 E-EhK motif," and structurally characterized "the environment of the SLFN14 disease hotspot at the RNA cleft entrance" ([Nat Commun 2025, PMID: 40592880](https://pubmed.ncbi.nlm.nih.gov/40592880/)).

### Causal chain (upstream → downstream)
1. **Trigger:** Heterozygous pathogenic *SLFN14* variant (AAA-ATPase or helicase domain).
2. **Molecular consequence:** Altered/aberrant endoribonuclease substrate specificity and/or dominant-negative protein misfolding and degradation.
3. **RNA-processing defect:** In megakaryocytes and mature platelets, mutant SLFN14 drives **rRNA and type II tRNA degradation**, with disease variants showing enhanced tRNA cleavage and reduced rRNA cleavage relative to wild type ([PMID: 42213791](https://pubmed.ncbi.nlm.nih.gov/42213791/)).
4. **Ribosome/translation dysfunction:** "SLFN14-defective platelets and mature MK showed signs of rRNA degradation; however, this was absent in undifferentiated imMKCL cells and granulocytes" — i.e., the defect manifests specifically during **megakaryocyte maturation**, not in progenitor/undifferentiated states ([Blood 2023, PMID: 36790527](https://pubmed.ncbi.nlm.nih.gov/36790527/)). Ribosome stalling at codons decoded by depleted type II tRNAs triggers cellular stress signaling and cell death pathways.
5. **Transcriptional dysregulation:** Gene-expression analysis found "upregulated genes were enriched in pathways involved in (mitochondrial) translation and transcription," pointing to **dysregulated mTORC1-coordinated ribosomal biogenesis** as a downstream driver ([PMID: 36790527](https://pubmed.ncbi.nlm.nih.gov/36790527/)).
6. **Megakaryocyte-level consequences:** Reduced megakaryocyte numbers in bone marrow (mouse model), abnormal mitochondria in megakaryocytes, dysregulated genes involved in ubiquitination, ATP activity, and cytoskeletal function ([J Clin Invest 2025, PMID: 40794453](https://pubmed.ncbi.nlm.nih.gov/40794453/)).
7. **Platelet-level consequences:** Enlarged platelets (macrothrombocytes) with vacuolization, reduced number of dense granules, decreased ATP secretion, impaired aggregation to ADP/collagen/PAR1 (but preserved arachidonic acid response), impaired calcium mobilization, reduced platelet signaling to thrombin, and delayed thrombus formation.
8. **Clinical outcome:** Moderate-to-severe thrombocytopenia plus qualitative platelet secretion defect together produce the mucocutaneous bleeding phenotype.

### Relevant ontology term suggestions
- **GO (biological process):** GO:0006364 (rRNA processing); GO:0034661 (ncRNA catabolic process); GO:0007596 (blood coagulation); GO:0030220 (platelet formation); GO:0007599 (hemostasis); GO:0032262 (positive regulation of ATP secretion, if bound)
- **GO (molecular function):** GO:0004521 (endoribonuclease activity); GO:0003924 (GTPase activity)/ATP-binding AAA domain function
- **GO (cellular component):** GO:0005840 (ribosome); GO:0031091 (platelet alpha granule); GO:0042629 (mast cell granule — analogous dense-granule terms); GO:0022626 (cytosolic ribosome)
- **CL (cell types):** CL:0000556 (megakaryocyte); CL:0000233 (platelet/thrombocyte)
- **HP terms:** listed in Section 3 above.

### Cellular processes involved
Ribosome biogenesis/degradation, mitochondrial translation, megakaryocyte maturation and proliferation, platelet dense-granule biogenesis, ATP secretion, thrombus formation, and (in the mouse model) erythroid lineage commitment.

### Molecular profiling data
- **Transcriptomics:** RNA-seq of patient platelets/megakaryocyte-like cells and mouse platelets/megakaryocytes show altered expression in translation, transcription, ubiquitination, ATP-activity, and cytoskeletal pathways (PMID: 36790527, PMID: 40794453).
- No dedicated proteomics, metabolomics, lipidomics, single-cell, or spatial transcriptomics datasets specific to BDPLT20 were identified in this search.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Primarily the hematopoietic/hemostatic system — bone marrow (megakaryopoiesis) and peripheral blood (platelets). Secondary manifestations occur wherever bleeding presents clinically: skin/subcutaneous tissue (bruising, hematoma), oral mucosa (gum bleeding), nasal mucosa (epistaxis), female reproductive tract (menorrhagia, postpartum hemorrhage), and skeletal muscle (spontaneous hematoma).
- **Tissue/cell level:** Megakaryocytes (bone marrow) and platelets (peripheral blood) — CL:0000556 and CL:0000233 respectively.
- **Subcellular level:** Ribosomes (GO:0005840), platelet dense granules (delta granules), mitochondria (abnormal mitochondrial morphology reported in mouse megakaryocytes).
- **Localization/laterality:** Systemic hemostatic disorder — not lateralized; bleeding can occur at any anatomic site subjected to trauma or physiologic stress (menstruation, delivery, surgery).

---

## 8. Temporal Development

- **Onset:** Congenital/lifelong — the underlying platelet defect is present from birth, though clinical bleeding may first become apparent in childhood, adolescence, or adulthood depending on exposure to hemostatic challenges (menarche, dental extraction, surgery, childbirth).
- **Onset pattern:** Chronic, with episodic (rather than acute single-event) bleeding manifestations.
- **Progression:** The underlying thrombocytopenia/platelet dysfunction is generally stable over time (not classically progressive), though bleeding episodes are triggered situationally.
- **Disease course:** Chronic, lifelong; no remission is described, as this is a structural/genetic platelet defect rather than an acquired, immune-mediated, or reversible process.
- **Critical periods:** Hemostatic challenge windows (surgery, dental procedures, menstruation, pregnancy/delivery) represent periods of elevated bleeding risk requiring proactive management.

---

## 9. Inheritance and Population

- **Epidemiology:** BDPLT20 is an ultra-rare disorder; no formal prevalence or incidence estimates (per 100,000) have been published. It has been identified in a modest number of families worldwide (originally 3 families/12 patients in the founding 2015 report, with additional single-family/single-patient reports subsequently from Italy, and other case reports through 2025), consistent with an inherited-thrombocytopenia subtype identified predominantly through next-generation sequencing referral cohorts (e.g., UK GAPP study, whole-exome-sequencing bleeding-diathesis diagnostic pipelines).
- **Inheritance pattern:** Autosomal dominant (OMIM: heterozygous mutation).
- **Penetrance:** Historically considered high/complete in the originally described AAA-domain-mutation families, but **incomplete penetrance** has since been reported for at least one helicase-domain variant (asymptomatic carrier mother and grandmother) (PMID: 40521396).
- **Expressivity:** Variable — bleeding severity ranges from mild bruising/menorrhagia to severe hemorrhagic syndrome; platelet count reduction and macrothrocytopenia severity also vary.
- **Germline mosaicism:** Documented in at least one family as "maternal gonosomal mosaicism" (PMID: 36237120) — clinically relevant since it can produce apparently sporadic/de novo cases with recurrence risk in future offspring.
- **Founder effects / consanguinity:** Not reported; families described span multiple ancestries (original US-derived and UK GAPP-ascertained families, an Italian family, and others), without an identified founder mutation or consanguinity requirement (consistent with autosomal dominant, not recessive, inheritance).
- **Carrier frequency:** Not established given the small number of known families and pathogenic-variant heterogeneity.
- **Population demographics:** No specific ethnic or geographic clustering has been reported; cases have been described in North American, European (UK, Italian), and other cohorts. Both males and females are affected, consistent with autosomal (non-X-linked) transmission, though several described probands are female (likely partly ascertainment bias via menorrhagia presentation).
- **Age distribution:** Diagnosed across a wide age range — from pediatric/adolescent (e.g., 17-year-old proband, pediatric twin brothers) to adult (31-year-old original proband and other adult family members across 3 generations in the founding family).

---

## 10. Diagnostics

**Laboratory tests:**
- Complete blood count with peripheral smear — reveals thrombocytopenia and macrothrombocytes (enlarged platelets, occasionally giant forms).
- Platelet aggregometry — reduced response to ADP, collagen, and PAR1 (thrombin-receptor-activating peptide); normal response to arachidonic acid.
- Lumiaggregometry — decreased ATP secretion (dense-granule release defect).
- Electron microscopy of platelets — reduced number of dense granules; vacuolization in some cases.
- Bone marrow examination — may show megakaryocyte accumulation with arrested maturation in severe pediatric cases.
- Flow cytometry-based "activation index" functional platelet assessment has been proposed as a newer diagnostic approach for inherited thrombocytopenias including macrothrombocytopenias (PMID: 40314328).

**Genetic testing:**
- **Recommended approach:** Given the phenotypic overlap among inherited thrombocytopenias (>40 causal genes known), whole-exome sequencing (WES) is the diagnostic modality that has identified nearly all reported BDPLT20 cases, typically applied "at the end of the diagnostic trajectory" after standard hematologic workup fails to establish a diagnosis (PMID: 30431218). Targeted *SLFN14* single-gene sequencing or an inherited-thrombocytopenia gene panel would also be appropriate once BDPLT20 is clinically suspected (thrombocytopenia + macrothrombocytes + secretion defect + dominant family history).
- WGS, chromosomal microarray, karyotyping, and FISH are not first-line for this single-gene disorder but may be used to exclude syndromic/chromosomal causes of thrombocytopenia in the differential.

**Clinical criteria / differential diagnosis:** BDPLT20 should be distinguished from other inherited macrothrombocytopenias (e.g., MYH9-related disorders, Bernard-Soulier syndrome, ACTN1-related BDPLT15, gray platelet syndrome) and from other dense-granule secretion defects (e.g., Hermansky-Pudlak syndrome). The combination of dominant inheritance, moderate thrombocytopenia with macrothrombocytes, and a selective secretion defect with normal arachidonic-acid response is characteristic, but definitive diagnosis requires *SLFN14* sequencing.

**Screening:** No population or newborn screening program exists given the disorder's rarity; diagnosis occurs via clinical ascertainment (bleeding history) followed by genetic confirmation, with cascade testing of at-risk relatives once a family-specific variant is identified.

---

## 11. Outcome/Prognosis

- No mortality data specific to BDPLT20 were identified; the disorder is not associated with a described reduction in life expectancy, and bleeding episodes, while sometimes severe, are generally manageable with hemostatic support.
- **Morbidity:** Chronic bleeding tendency affecting quality of life via recurrent bruising, menorrhagia, and bleeding after minor trauma or procedures; severe hemorrhagic syndrome has been reported in at least one adolescent case.
- **Complications:** Iron-deficiency anemia secondary to chronic menorrhagia is a plausible (though not explicitly quantified in available sources) complication; postpartum hemorrhage represents an important obstetric risk.
- **Prognostic factors:** Variant domain/location (AAA-ATPase vs. helicase) and degree of penetrance appear to modulate severity, though formal genotype-phenotype correlation studies with prognostic biomarkers have not been established.

---

## 12. Treatment

There is no disease-modifying or curative therapy for BDPLT20; management is supportive/symptomatic, following general principles for inherited platelet function disorders and thrombocytopenias:

- **Antifibrinolytic therapy:** Oral **tranexamic acid** has been used successfully for menorrhagia management in at least one adolescent patient (NCIT:C61129 Tranexamic Acid; treatment category: Pharmacotherapy, NCIT:C15986).
- **Platelet transfusion:** Prophylactic platelet transfusion is used to reduce spontaneous bleeding risk, generally following standard thresholds used for thrombocytopenia (e.g., ≤10×10⁹/L) or peri-procedurally to cover surgical/dental bleeding risk (NCIT term: Platelet Transfusion, NCIT:C15343 or similar transfusion-therapy term).
- **DDAVP (desmopressin):** Commonly used empirically in inherited platelet function disorders generally, though no BDPLT20-specific published trial or case data confirming efficacy were identified in this search — this should be considered plausible but unconfirmed for this specific gene defect.
- **Supportive/procedural management:** Peri-operative and peri-partum planning with hematology involvement, avoidance of antiplatelet/anticoagulant medications, and individualized bleeding-risk assessment.
- **Experimental/investigational therapies:** None specific to BDPLT20 are in clinical trials per available ClinicalTrials.gov search results; management remains empirical/symptomatic, consistent with the broader category of inherited platelet secretion disorders.

No gene therapy, cell therapy, or targeted molecular therapy has been developed or trialed for this condition to date.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense — genetic counseling and cascade testing of at-risk relatives (given autosomal dominant inheritance and documented germline mosaicism risk) is the principal preventive strategy for identifying at-risk family members before bleeding complications occur.
- **Secondary prevention:** Early genetic diagnosis in a proband enables surveillance and pre-emptive management (e.g., planning for menarche, surgery, pregnancy) in relatives found to carry the familial variant.
- **Reproductive counseling:** Given autosomal dominant transmission (50% risk to offspring of an affected individual) and at least one report of germline mosaicism (recurrence risk even when parental testing is negative), genetic counseling is important for family planning; prenatal or preimplantation genetic testing could theoretically be offered once a familial variant is known, though no specific literature on this practice for BDPLT20 was found.
- **Behavioral/prophylactic measures:** Avoidance of antiplatelet medications (aspirin, NSAIDs) and proactive hemostatic planning before invasive procedures.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Mus musculus* (NCBITaxon:10090) is the principal model species used experimentally; no naturally occurring veterinary *SLFN14*-associated bleeding disorder has been reported (this is an experimentally engineered rather than naturally occurring animal disease).
- **Orthologous gene:** Mouse *Slfn14* (murine ortholog of human SLFN14); the human p.K219N mutation corresponds to mouse p.K208N.
- **Comparative biology — important species-specific divergence:** Mouse and human phenotypes diverge substantially. The heterozygous K208N knock-in mouse shows "microcytic erythrocytosis, hemolytic anemia, splenomegaly, and abnormal thrombus formation," but notably "platelet function and morphology remain unchanged" in mice — contrasting sharply with the platelet-centric defects seen in human patients ([Blood Adv 2021, PMID: 33496736](https://pubmed.ncbi.nlm.nih.gov/33496736/)). The homozygous K208N mutation is **embryonic lethal** in mice. This represents an important **human-model mismatch**: the global knock-in model better recapitulates an erythroid phenotype not classically described in human BDPLT20, while a separate **platelet/megakaryocyte-specific conditional knockout** (PF4-Cre-mediated deletion of *Slfn14* exons 2–3) more faithfully reproduces the human platelet phenotype — "reduced platelet signaling to thrombin, reduced thrombin formation, increased bleeding tendency, and delayed thrombus formation," with reduced bone-marrow megakaryocyte numbers ([J Clin Invest 2025, PMID: 40794453](https://pubmed.ncbi.nlm.nih.gov/40794453/)).
- **Zoonotic potential:** Not applicable; this is a non-infectious, purely genetic disorder.

---

## 15. Model Organisms

| Model | Type | Key findings | Source |
|---|---|---|---|
| Global CRISPR knock-in mouse, K208N (heterozygous) | Genetic, germline knock-in | Microcytic erythrocytosis, hemolytic anemia, splenomegaly, abnormal thrombus formation; **no platelet functional/morphological defect** (species-specific divergence from human phenotype); homozygous state embryonic lethal | Stapley/Blood Adv 2021, PMID: 33496736 |
| Platelet/megakaryocyte-specific conditional knockout mouse (PF4-Cre; *Slfn14* exon 2-3 deletion) | Genetic, conditional/tissue-specific knockout | Reduced platelet signaling to thrombin, reduced thrombin generation, increased bleeding tendency, delayed thrombus formation, reduced marrow megakaryocyte numbers, dysregulated ubiquitination/ATP/cytoskeletal gene expression — closely recapitulates human platelet phenotype | J Clin Invest 2025, PMID: 40794453 |
| Immortalized megakaryocyte cell line (imMKCL) with SLFN14 disease-mutant modeling | Cellular/in vitro | rRNA degradation phenotype present in mature megakaryocyte-like cells but absent in undifferentiated progenitor cells, indicating a maturation-stage-specific defect; supports mTORC1-linked ribosomal biogenesis dysregulation | Blood 2023, PMID: 36790527 |
| Patient-derived platelets (primary human cells) | Primary human ex vivo | Direct evidence of reduced dense granules, ATP secretion defect, impaired aggregation | Fletcher et al. 2015 (PMID: 26280575) and multiple subsequent case reports |
| Recombinant SLFN14 protein / biochemical & structural studies (cryo-EM) | In vitro/computational structural biology | Defined RNA-cleavage mechanism, disease-hotspot mapping at the RNA cleft entrance, E-EhK catalytic motif requirement | Nat Commun 2025, PMID: 40592880; PLoS Biol 2026, PMID: 42213791 |

**Model limitations:** The global heterozygous knock-in mouse notably **fails to recapitulate the platelet phenotype** seen in humans (a clear human-model mismatch), while showing an erythroid phenotype not prominently described in human patients — underscoring that megakaryocyte/platelet-lineage-restricted conditional models are needed to faithfully model the human disease, and that cross-species extrapolation of SLFN14 biology must be done cautiously.

**Applications:** These models have been used to establish the RNA endoribonuclease mechanism, the megakaryocyte-maturation-stage specificity of the ribosomal/rRNA degradation defect, the dominant-negative/altered-substrate-specificity mechanism of disease variants, and thrombus-formation/bleeding phenotypes relevant to the human disorder.

---

## Summary of Key Evidence-Anchored Claims

| Claim | PMID | Evidence type |
|---|---|---|
| SLFN14 mutations identified in 12 patients/3 families; moderate thrombocytopenia, enlarged platelets, decreased ATP secretion, dominant inheritance | 26280575 | Human clinical |
| Additional Italian family with SLFN14 missense mutation | 26769223 | Human clinical |
| Disease mutants show dramatically reduced expression via post-translational degradation; proposed dominant-negative mechanism | 29678925 | In vitro |
| rRNA degradation specific to mature megakaryocytes/platelets, not progenitors; mTORC1-linked mechanism | 36790527 | In vitro/human clinical (patient transcriptomes) |
| Novel variant, giant platelets >10 μm, impaired calcium mobilization/thrombus formation | 37041648 | Human clinical |
| Maternal gonosomal mosaicism | 36237120 | Human clinical |
| Helicase-domain L589S variant, incomplete penetrance | 40521396 | Human clinical |
| T853fs frameshift, distinct mechanism (ion channel/dense granule vs. mitochondrial translation) | 40510593 | Human clinical + in vitro |
| CryoEM structure of SLFN14-RNA complex, disease hotspot mapping | 40592880 | Computational/structural |
| IT-linked mutations alter RNA substrate specificity (tRNA vs rRNA cleavage balance) | 42213791 | In vitro/computational |
| Heterozygous K208N mouse: erythroid phenotype, no platelet defect; homozygous embryonic lethal | 33496736 | Model organism (mouse) |
| Platelet-specific Slfn14 knockout mouse recapitulates human platelet/bleeding phenotype | 40794453 | Model organism (mouse) |

---

**Sources:**
- [OMIM #616913 — BLEEDING DISORDER, PLATELET-TYPE, 20; BDPLT20](https://omim.org/entry/616913)
- [OMIM *614958 — SCHLAFEN FAMILY, MEMBER 14; SLFN14](https://www.omim.org/entry/614958)
- [NCBI GTR: Platelet-type bleeding disorder 20](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4310797/)
- [MedGen C4310797](https://ncbi.nlm.nih.gov/medgen/C4310797)
- [ClinGen MONDO:0014830 curation](https://search.clinicalgenome.org/kb/conditions/MONDO:0014830)
- [Orphanet: SLFN14-related thrombocytopenia](https://www.orpha.net/en/disease/gene/SLFN14)
- [ClinVar Miner variants for Platelet-type bleeding disorder 20](https://clinvarminer.genetics.utah.edu/variants-by-condition/Platelet-type%20bleeding%20disorder%2020)
- [SLFN14 mutations underlie thrombocytopenia with excessive bleeding and platelet secretion defects (JCI 2015, PMID 26280575)](https://pubmed.ncbi.nlm.nih.gov/26280575/)
- [SLFN14-related thrombocytopenia: identification within a large series (Thromb Haemost 2016, PMID 26769223)](https://pubmed.ncbi.nlm.nih.gov/26769223/)
- [Role of the novel endoribonuclease SLFN14 in ribosomal degradation (RNA 2018, PMID 29678925)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6004054/)
- [Ribosome dysfunction underlies SLFN14-related thrombocytopenia (Blood 2023, PMID 36790527)](https://ashpublications.org/blood/article/141/18/2261/494489/Ribosome-dysfunction-underlies-SLFN14-related)
- [Novel SLFN14 mutation associated with macrothrombocytopenia (Orphanet J Rare Dis 2023, PMID 37041648)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10091655/)
- [Maternal gonosomal mosaicism in rare autosomal dominant SLFN14-related thrombocytopenia (Br J Haematol 2022, PMID 36237120)](https://pubmed.ncbi.nlm.nih.gov/36237120/)
- [Whole exome sequencing in the diagnostic workup of patients with a bleeding diathesis (Haemophilia 2019, PMID 30431218)](https://pubmed.ncbi.nlm.nih.gov/30431218/)
- [Molecular basis of inherited thrombocytopenias: an update (Curr Opin Hematol 2016, PMID 27438527)](https://pubmed.ncbi.nlm.nih.gov/27438527/)
- [Severe Thrombocytopenia Associated with a Genetic Variant in the Helicase Domain of SLFN14 (EJHaem 2025, PMID 40521396)](https://pubmed.ncbi.nlm.nih.gov/40521396/)
- [Novel mutation SLFN14 T853fs associated with inherited macrothrombocytopenia (Mol Ther Nucleic Acids 2025, PMID 40510593)](https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(25)00108-8)
- [CryoEM structure of the SLFN14 endoribonuclease (Nat Commun 2025, PMID 40592880)](https://www.nature.com/articles/s41467-025-XXXXX)
- [Type II tRNA cleavage by SLFN14 endoribonuclease variants drives global translational repression (PLoS Biol 2026, PMID 42213791)](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3003830)
- [Heterozygous mutation SLFN14 K208N in mice mediates species-specific differences (Blood Adv 2021, PMID 33496736)](https://ashpublications.org/bloodadvances/article/5/2/377/474925/Heterozygous-mutation-SLFN14-K208N-in-mice)
- [Platelet-specific SLFN14 deletion causes macrothrombocytopenia and platelet dysfunction (J Clin Invest 2025, PMID 40794453)](https://www.jci.org/articles/view/189100)
- [A new approach to personalized assessment of functional platelet disorders in children (Blood Coagul Fibrinolysis 2025, PMID 40314328)](https://pubmed.ncbi.nlm.nih.gov/40314328/)
- [SLFN14 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLFN14)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 17 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:37041648`: "heterogeneity in cell size, including giant forms over 10 μm (normal size 1–5 μm) in diameter, with vacuolization"
  - closest text in source: "Immunofluorescence and brightfield examination of platelets in the smear showed heterogeneity in cells size, including giant forms over 10 μm (normal size 1-5) in diameter, with vacuolization and diffuse distribution of β1-tubulin and CD63"
- `PMID:29678925` *(abstract only)*: "propose a dominant-negative mechanism explaining heterozygous mutations in patients"
  - closest text in source: "These findings could explain the dominant negative effect of heterozygous mutation on SLFN14 expression in patients' platelets"
- `PMID:42213791`: "ribosome stalling at codons decoded by type II tRNAs, stress signaling, and cell death"
  - closest text in source: "This shift promotes ribosome stalling at codons decoded by type II tRNAs, triggering global translational arrest, stress signaling, and cell death"