---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-21T16:25:01.872941'
end_time: '2026-08-21T16:29:54.030501'
duration_seconds: 292.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SOCS1 Haploinsufficiency
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
  web_search_requests: 12
  num_turns: 30
  total_cost_usd: 2.0117368
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
reference_validation:
  total_references: 17
  verified: 16
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.059
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC11070515
  quotes_not_checkable: 1
  relevance_assessed: 16
  on_topic: 11
  unresolved_references:
  - DOI:10.1371/journal.pone.0162111](https://journals.plos.org
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SOCS1 Haploinsufficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SOCS1 Haploinsufficiency** covering all of the
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

# SOCS1 Haploinsufficiency — Comprehensive Research Report

## 1. Disease Information

**Overview.** SOCS1 (suppressor of cytokine signaling 1) haploinsufficiency (SOCS1-HI) is a recently delineated, autosomal dominant **inborn error of immunity (IEI)** caused by heterozygous loss-of-function variants in *SOCS1*, encoding a key intracellular negative regulator of JAK/STAT cytokine signaling. Loss of one functional *SOCS1* allele produces cytokine hypersensitivity (especially to IFN-γ, IL-2, IL-4, IL-6) and a strikingly pleiotropic clinical picture spanning early-onset autoimmunity, autoinflammation, lymphoproliferation, atopy, and increased infection susceptibility. It was first formally described as a Mendelian disease entity in 2020 ([Hadjadj et al., *Nat Commun* 2020](https://www.nature.com/articles/s41467-020-18925-4); PMC copy: [PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)), although the underlying biology had been predicted by SOCS1-knockout mouse work two decades earlier (Naka et al. and Starr et al., 1998; Alexander et al. 1999, PMID:10490099; Marine et al. 1999, PMID:10490100).

**Key identifiers:**
- **Gene:** SOCS1, HGNC:19383, chromosome **16p13.13** (chr16:11,249,101–11,256,556, GRCh38) ([GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SOCS1); [ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:19383))
- **Orphanet:** ORPHA "Early-onset autoimmunity-autoinflammation-immunodeficiency syndrome due to SOCS1 haploinsufficiency" ([Orphanet detail page 619948](https://www.orpha.net/en/disease/detail/619948))
- **OMIM gene entry:** *SOCS1, 603597 ([OMIM 603597](https://omim.org/entry/603597)) — a distinct phenotype MIM number for the haploinsufficiency syndrome has not been broadly confirmed in the sources searched
- **ClinGen:** SOCS1 has 1 Gene-Disease Validity classification but, as of the current search, 0 Dosage Sensitivity classification on file ([ClinGen SOCS1](https://search.clinicalgenome.org/kb/genes/HGNC:19383))
- Falls under the broader IEI category of **autoimmune lymphoproliferative immunodeficiencies (ALPID)** ([PMC10499775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10499775/))

**Common synonyms/alternative names:** SOCS1 insufficiency; SOCS1 deficiency (heterozygous); SOCS-1 haploinsufficiency; JAK/STAT gain-of-function-like syndrome due to SOCS1; early-onset autoimmunity–autoinflammation–immunodeficiency syndrome due to SOCS1 haploinsufficiency (Orphanet name).

**Data source type.** The evidence base is almost entirely **individual patient-level case reports and small case series** (5–10 patients per report), aggregated across international collaborative registries (a European ESID-affiliated SOCS1 study group and a US SOCS1 study group), culminating in a **registry-based, population-level systematic review of 33 patients across 9 publications** ([Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext)). There is no large aggregated disease-level registry comparable to those for common autoimmune diseases; essentially all quantitative statistics below derive from this pooled literature review of the (currently) small known patient population.

---

## 2. Etiology

**Disease causal factor:** SOCS1-HI is a **monogenic, autosomal dominant** condition. It is caused directly by **heterozygous loss-of-function (LOF) germline variants in *SOCS1*** — frameshift, nonsense, missense (particularly in the SH2 and SOCS-box domains), and complete gene deletions (including microdeletions/CNVs removing one copy of 16p13.13) — that reduce functional SOCS1 protein dosage by ~50%, sufficient to disturb the stoichiometric balance of JAK/STAT negative feedback ("haploinsufficiency" model) ([Nat Commun 2020](https://www.nature.com/articles/s41467-020-18925-4); [PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/)).

**Genetic risk factors:**
- Reported pathogenic variants include: **p.P123R (c.368C>G)**, SH2 domain missense; **p.A9Pfs\*76 (c.24delA)**, frameshift in the 5′ KIR region; **p.M161Afs\*46 (c.476_480dupGCCGC)**, frameshift in the SOCS box; **p.R22W (c.64C>T)**, missense in the KIR region; **p.Y154H (c.460T>C)**, SH2 domain missense — all with high CADD scores (>11.63) ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/))
- A **p.(Ala70Pro) [c.208G>C]** variant segregating with a multi-generational family with neurological disease ([PMC12628480](https://pmc.ncbi.nlm.nih.gov/articles/PMC12628480/))
- **Complete heterozygous chromosomal deletions** of 16p13.13 encompassing *SOCS1* (e.g., unmasked by SARS-CoV-2 infection in a pediatric patient) — interestingly, reports note complete gene deletions may produce a **less severe** phenotype than certain heterozygous C-terminal point variants, possibly reflecting dominant-negative effects of some missense/truncating alleles beyond simple dosage loss ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/); [Springer 2022 case report](https://link.springer.com/article/10.1007/s10875-022-01346-x))
- **Population tolerance:** gnomAD v4.0 reports SOCS1 pLI = 0.12 and LOEUF = 1.47 ([search results](https://genebe.net/gene/hg38/SOCS1)) — a relatively "tolerant" score in the general population metric, which sits in tension with the clinical LOF disease association and likely reflects incomplete penetrance plus the population database's limited power for a gene of this size/constraint profile.
- Family segregation studies show **identical variants produce markedly different phenotypes** even within the same pedigree, indicating additional genetic/epigenetic modifiers are likely at play, though none have yet been formally identified.

**Environmental risk factors / triggers:**
- **Infection as a disease-unmasking trigger** is a recurring and clinically important theme: SARS-CoV-2 infection precipitating immune thrombocytopenia, arthralgia/enthesitis, and **multisystem inflammatory syndrome in children (MIS-C)**-like presentations in carriers ([PubMed 32853638](https://pubmed.ncbi.nlm.nih.gov/32853638/); [PMC11746893, two case reports](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11746893/))
- Acute infections generally appear able to "unmask" underlying cytokine hypersensitivity, precipitating first presentation with cytopenia or autoinflammatory flares.

**Protective factors:** No specific genetic or environmental protective factors have been characterized in the literature searched; ~33% of identified mutation carriers remain **clinically asymptomatic** despite carrying the pathogenic variant and displaying immunological abnormalities on functional testing, implying unidentified modifying/protective factors ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)).

**Gene-environment interaction:** The clearest documented interaction is infection (particularly SARS-CoV-2) acting as a "second hit" precipitant of overt autoimmune/autoinflammatory disease in genetically susceptible (SOCS1+/-) individuals, consistent with a two-hit model in which baseline cytokine hypersensitivity is clinically silent until an inflammatory trigger occurs.

---

## 3. Phenotypes

SOCS1-HI shows **extreme pleiotropy**, involving essentially every major organ system. Onset is typically pediatric (median 7.5 years) but ranges into adulthood.

### Hematologic / autoimmune cytopenias (most common presenting feature)
- **Immune thrombocytopenia (ITP)** — HP:0001873 (Thrombocytopenia)
- **Autoimmune hemolytic anemia** — HP:0001878 (Hemolytic anemia)
- **Evans syndrome** (combined ITP + AIHA)
- 5/10 index patients in the founding cohort had autoimmune cytopenia ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/))

### Systemic/organ-specific autoimmunity
- **Systemic lupus erythematosus (SLE)-like disease** — HP:0002960 (Autoimmunity), often with glomerulonephritis and discoid skin lesions; described as the single most common overall manifestation in the pooled registry review ([Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext))
- **Autoimmune thyroiditis** — HP:0100646
- **Coeliac disease** — HP:0002608
- **Psoriasis / psoriasis-like lesions** — HP:0100750
- **Spondyloarthritis / severe enthesitis** — HP:0011729-adjacent; a pediatric case presented with severe enthesitis and bone marrow hypocellularity ([Springer 2022](https://link.springer.com/article/10.1007/s10875-022-01346-x))
- **Autoimmune hepatitis** — HP:0001394; **autoimmune pancreatitis**

### Autoinflammatory / granulomatous manifestations
- **Atopic disease**: asthma, allergic rhinoconjunctivitis, atopic dermatitis (SOCS1-HI is distinguished from other genetic ALPS-like disorders by frequent atopic manifestations) ([Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext))
- **Granulomatous-lymphocytic interstitial lung disease (GLILD)**, organizing pneumonia, granulomatous uveitis
- **Severe oral and upper gastrointestinal ulcerations**, recurrent stomatitis (ACR abstract findings)

### Gastrointestinal
- Coeliac disease, **Crohn's-like disease**, **chronic intestinal pseudo-obstruction**, and a specifically described **lymphocytic leiomyositis** with CD8+ T-cell muscular infiltration causing intestinal obstructive symptoms, responsive to ruxolitinib ([Springer 2023 intestinal spectrum paper](https://link.springer.com/article/10.1007/s10875-023-01495-7))

### Lymphoproliferative / neoplastic
- **Lymphadenopathy mimicking ALPS** (autoimmune lymphoproliferative syndrome)
- One documented case of **Hodgkin lymphoma** at age 34 evolving from chronic lymphoproliferation ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/))

### Neurological (newly expanding phenotype, 2025)
- **Multiple sclerosis** (relapsing-remitting, adult-onset, diagnosed age 35)
- **Autoimmune (limbic) encephalitis** with anti-GAD antibodies and seizures (onset age 10)
- **Complex regional pain syndrome (CRPS)** with reduced intraepidermal nerve fiber density (4.02/mm vs. normal cutoff of 8.4/mm), suggesting peripheral small-fiber neuropathy
([PMC12628480](https://pmc.ncbi.nlm.nih.gov/articles/PMC12628480/))

### Infectious susceptibility
- Predominantly localized infections; severe bacterial infections reported in some patients ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))
- **MIS-C-like** presentation following SARS-CoV-2 in carriers ([PubMed 32853638](https://pubmed.ncbi.nlm.nih.gov/32853638/))

### Phenotype characteristics
- **Age of onset:** median 7.5 years (range 2–44 years) in the founding cohort ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)); some patients (e.g., MS) present in adulthood
- **Severity/progression:** highly variable — ranges from asymptomatic carriers (33% of gene carriers) to severe multi-organ, treatment-refractory disease
- **Sex bias:** autoimmune manifestations predominate in **females**, mirroring the female bias of SLE, and consistent with heterozygous mouse model data ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))
- **Penetrance:** incomplete — approximately two-thirds of variant carriers are symptomatic; penetrance is higher in females than males ([Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext))

### Quality of life
No dedicated QoL instrument studies (EQ-5D/SF-36) were identified for this rare, newly described condition; qualitative case reports describe substantial disease burden from chronic cytopenia, refractory arthralgia/enthesitis, and neurological complications (e.g., CRPS causing debilitating pain episodes).

---

## 4. Genetic/Molecular Information

**Causal gene:** *SOCS1* (HGNC:19383; OMIM *603597*), 16p13.13.

**Variant spectrum and classification:**
| Variant | Type | Domain | 
|---|---|---|
| p.P123R (c.368C>G) | Missense | SH2 domain |
| p.A9Pfs\*76 (c.24delA) | Frameshift | 5′ KIR region |
| p.M161Afs\*46 (c.476_480dupGCCGC) | Frameshift | SOCS box |
| p.R22W (c.64C>T) | Missense | 5′ KIR region |
| p.Y154H (c.460T>C) | Missense | SH2 domain |
| p.(Ala70Pro) (c.208G>C) | Missense | (functional domain, family with neurological phenotype) |
| Chromosomal microdeletion (16p13.13) | Full-gene deletion | N/A |

All reported coding variants carry high CADD scores (>11.63), consistent with predicted deleteriousness ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)).

**Functional consequence:** **Loss of function / haploinsufficiency.** SOCS1 protein has three key functional domains:
1. A **kinase inhibitory region (KIR)** acting as a pseudosubstrate for JAK kinases
2. An **SH2 domain** that binds the JAK activation loop, directly inhibiting JAK catalytic activity
3. A **SOCS box** that recruits an Elongin B/C–Cullin5 E3 ubiquitin ligase complex, targeting bound substrates (including JAKs) for proteasomal degradation
4. A **nuclear localization signal**, enabling additional intranuclear regulatory roles (e.g., interaction with p53, modulation of NF-κB) ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))

LOF variants disrupt one or more of these functions, producing reduced negative feedback on JAK1/JAK2/TYK2-STAT1/3/5/6 signaling downstream of type I/II interferons, IL-2, IL-4, IL-6, and leukemia inhibitory factor (LIF).

**Origin:** Germline, typically inherited in an autosomal dominant pattern with incomplete penetrance and variable expressivity; de novo occurrence has not been systematically characterized in the sources reviewed but is plausible given the pedigree data available.

**Population frequency:** gnomAD v4.0 pLI = 0.12; LOEUF = 1.47 (ENST00000332029) — indicating the gene is not under classical severe constraint against LOF variation in the general population, in apparent tension with (but not necessarily contradicting) its role in a highly penetrant-in-symptomatic-carriers monogenic disease, given incomplete penetrance ([search result via genebe.net](https://genebe.net/gene/hg38/SOCS1)).

**Epigenetic note (biologically related, distinct from the germline disease):** *SOCS1* promoter hypermethylation and transcriptional silencing is a well-documented **somatic** epigenetic event in several cancers (hepatocellular carcinoma, multiple myeloma), functioning as a tumor-suppressor-like mechanism distinct from germline haploinsufficiency (PMID:11326271; PMID:12456503) — relevant context for understanding SOCS1's dual role in cancer biology versus the germline immune dysregulation syndrome, though not itself part of the SOCS1-HI disease mechanism.

**Modifier genes:** None formally established; phenotypic discordance among carriers of identical variants strongly suggests unidentified genetic or epigenetic modifiers.

---

## 5. Environmental Information

- **Infectious triggers:** SARS-CoV-2 is the most concretely documented environmental/infectious trigger, precipitating both cytopenia/enthesitis presentations and MIS-C-like multisystem inflammation in SOCS1+/- individuals ([PubMed 32853638](https://pubmed.ncbi.nlm.nih.gov/32853638/); [Springer 2022](https://link.springer.com/article/10.1007/s10875-022-01346-x); [PMC11746893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11746893/)).
- No specific toxin, occupational, or lifestyle risk factors have been reported for this rare monogenic condition in the literature surveyed.
- Given the disease's cytokine-hypersensitivity mechanism, any acute inflammatory/infectious insult is mechanistically plausible as a trigger of clinical flares, though systematic study of this is limited to the COVID-19 examples above.

---

## 6. Mechanism / Pathophysiology

**Core causal chain:** Heterozygous *SOCS1* LOF variant → reduced functional SOCS1 protein dosage → impaired negative feedback on JAK1/JAK2/TYK2 → **exaggerated and prolonged STAT1 phosphorylation** upon IFN-γ (and IFN-α/β) stimulation, comparable in magnitude to STAT1 gain-of-function disease → concurrently **increased STAT5 phosphorylation** (IL-2) and **increased STAT6 phosphorylation** (IL-4), with **reduced STAT3 phosphorylation** (IL-6) → downstream transcriptional dysregulation (upregulated CXCL9, CXCL10, CISH, PIM1) → cellular immune dysregulation (reduced Tregs, reduced Th17, expanded Th1 responses, monocyte/macrophage hyperactivation) → clinical autoimmunity, autoinflammation, and lymphoproliferation ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/); [PMC8375263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8375263/)).

**Molecular pathways (KEGG/Reactome-relevant):**
- **JAK-STAT signaling pathway** (KEGG hsa04630) — central pathway
- Downstream **PI3K-AKT-mTOR** pathway component: loss of SOCS1 E3 ligase activity is associated with **increased FAK1** and **enhanced phosphorylated AKT and p70 ribosomal S6 kinase (RPS6K)** in patient immune cells, indicating cross-talk beyond canonical JAK-STAT ([PMC8375263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8375263/))
- NF-κB pathway modulation via nuclear SOCS1

**Cellular processes:**
- Impaired **regulatory T-cell (Treg)** development/function: reduced CD4+CD25+FOXP3+ Tregs, lower FOXP3/HELIOS/CD25 expression, and moderately reduced suppressive activity — distinguishes SOCS1-HI from STAT1 gain-of-function disease, where Tregs are typically preserved ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/); [PMC8375263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8375263/))
- **Reduced Th17 cells** (CD3+CD4+CXCR3-CCR6+) secondary to reduced STAT3 phosphorylation following IL-6 stimulation, phenocopying an aspect of STAT3 loss-of-function disease despite the opposite direction of the primary genetic lesion
- **Cytokine hypersensitivity** of T and B lymphocytes to IFN-γ, IL-2, and IL-4
- B-cell abnormalities including hypogammaglobulinemia and B-cell maturation deficiency reported in a subset of patients
- Monocyte/macrophage hyperinflammatory phenotype (relevant to the GLILD/granulomatous manifestations)

**Protein dysfunction:** Loss-of-function of SOCS1's SH2-domain JAK-binding, KIR pseudosubstrate inhibition, and/or SOCS-box-mediated E3 ubiquitin ligase activity, leading to failure of JAK degradation and prolonged kinase activity.

**Immune system involvement:** This is fundamentally an immune dysregulation disease — combining features of **autoimmunity** (SLE-like disease, cytopenias, organ-specific autoimmunity), **autoinflammation** (granulomatous disease, GLILD, enthesitis), and mild **immunodeficiency** (infection susceptibility, hypogammaglobulinemia in some), consistent with its classification among the ALPID (autoimmune lymphoproliferative immunodeficiency) spectrum of IEIs ([PMC10499775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10499775/)).

**Tissue damage mechanisms:** In the intestinal phenotype, **CD8+ T-lymphocyte infiltration of the muscularis (lymphocytic leiomyositis)** drives obstructive GI symptoms; ruxolitinib treatment produced "significant decrease of the CD8+ T lymphocyte muscular infiltrate, and normalization of serum and intestinal cytokines" ([PMC10354128](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10354128/)). In neurological disease, reduced intraepidermal nerve fiber density suggests inflammatory small-fiber neuropathy; SOCS1 is proposed to "act as a regulator of the inflammatory response in perineural tissues, thus preventing nerve damage" when intact ([PMC12628480](https://pmc.ncbi.nlm.nih.gov/articles/PMC12628480/)).

**Genotype-severity correlation:** Complete heterozygous gene deletions may produce milder phenotypes than certain heterozygous C-terminal point variants, suggesting some missense/truncating alleles may act partly through dominant-negative mechanisms rather than pure dosage loss.

**Suggested ontology terms:**
- **GO:0004860** (protein kinase inhibitor activity, relevant to KIR function); **GO:0007259** (JAK-STAT cascade); **GO:0060333** (interferon-gamma-mediated signaling pathway); **GO:0031398** (positive regulation of protein ubiquitination)
- **CL:0000815** (regulatory T cell); **CL:0000899** (Th17 cell); **CL:0000236** (B cell); **CL:0000576** (monocyte)
- Molecular function: ubiquitin-protein transferase activity (SOCS-box/Elongin BC/Cullin5 E3 ligase complex)

**Molecular profiling data:** No large-scale transcriptomic/proteomic/metabolomic dataset specific to SOCS1-HI was identified in the sources reviewed; most functional characterization derives from targeted phospho-flow cytometry (pSTAT1/3/5/6) and flow immunophenotyping of patient PBMCs rather than unbiased omics.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Hematologic/lymphoid system** — bone marrow (hypocellularity reported), spleen, lymph nodes (lymphoproliferation)
- **Skin** — psoriasis, discoid lupus, atopic dermatitis
- **Joints/entheses** — spondyloarthritis, severe enthesitis
- **Kidney** — lupus glomerulonephritis
- **Liver** — autoimmune hepatitis
- **Pancreas** — autoimmune pancreatitis
- **Gastrointestinal tract** — Crohn's-like disease, coeliac disease, intestinal pseudo-obstruction, lymphocytic leiomyositis of intestinal muscularis
- **Lung** — GLILD, organizing pneumonia
- **Eye** — granulomatous uveitis
- **Thyroid** — autoimmune thyroiditis
- **Central and peripheral nervous system** — MS (CNS demyelination), limbic encephalitis, small-fiber peripheral neuropathy (CRPS)

**Body systems involved:** Hematologic/immune, musculoskeletal, dermatologic, gastrointestinal, hepatic, endocrine, respiratory, ophthalmologic, nervous, renal — essentially multisystem.

**Tissue/cell level:**
- Epithelial and connective tissue involvement in autoimmune organ disease
- Smooth muscle (intestinal muscularis) infiltration by CD8+ T cells in the intestinal phenotype
- Peripheral nerve fibers (reduced intraepidermal nerve fiber density)
- Key immune cell populations: CD4+ T cells (Treg, Th1, Th17 subsets), CD8+ T cells, B cells, monocytes/macrophages

**Suggested UBERON/CL terms:** UBERON:0002370 (thymus), UBERON:0002371 (bone marrow), UBERON:0000178 (blood), UBERON:0001155 (colon), UBERON:0001987 (placenta N/A), UBERON:0000955 (brain), UBERON:0001021 (nerve); CL:0000815 (Treg), CL:0000899 (Th17), CL:0000625 (CD8+ T cell), CL:0000236 (B cell).

**Subcellular level:** Cytoplasmic JAK-STAT signaling complexes at the plasma membrane/cytoplasm (GO:0005737 cytoplasm); nuclear translocation of phosphorylated STATs and of SOCS1 itself via its nuclear localization signal (GO:0005634 nucleus).

**Laterality:** Not applicable/not systematically reported (systemic, bilateral/multisystem disease).

---

## 8. Temporal Development

**Onset:**
- **Median age of onset: 7.5 years** (range 2–44 years) across the founding cohort; several patients present in early childhood (as young as 2 years) with cytopenia or enthesitis, while others (e.g., MS, adult SLE) present in adulthood up to age 44 ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/))
- Onset pattern is variable — can be **acute** (e.g., infection-triggered thrombocytopenia) or **insidious** (e.g., slowly progressive organ-specific autoimmunity)

**Progression:**
- No formal staging system exists for this condition.
- Disease course is **highly variable**: some patients have a single self-limited autoimmune episode (e.g., transient ITP), others develop **chronic, relapsing, or progressive multi-organ disease** (e.g., relapsing-remitting MS, recurrent CRPS episodes — 8 debilitating episodes documented in one patient, refractory thrombocytopenia)
- Lymphoproliferation can be chronic/benign or evolve into malignancy (one Hodgkin lymphoma case at age 34, following prior chronic lymphoproliferation)

**Patterns:**
- **Remission:** Some cytopenias remit spontaneously or with treatment; JAK inhibitor therapy has induced sustained clinical and laboratory remission in several reported cases.
- **Critical periods:** Acute infection appears to represent a critical "unmasking" window in which previously asymptomatic carriers develop overt disease (documented for SARS-CoV-2).
- **Asymptomatic carrier state:** ~33% of genetically confirmed carriers remain clinically silent, sometimes for decades (asymptomatic carriers reported aged 10–62 years), indicating the disease can remain latent indefinitely in some individuals.

---

## 9. Inheritance and Population

**Epidemiology:**
- SOCS1-HI is an **ultra-rare** disease. As of the most recent systematic review (Sept 2024), the entire published literature comprised **9 publications describing 33 patients** ([Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext)); an earlier estimate cited "over 10 families" reported since 2020 ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/)). No formal population prevalence or incidence estimate (cases per 100,000) exists; the condition is considered likely **underdiagnosed**, given its recent description (2020) and pleiotropic, easily-misattributed clinical presentations.

**Inheritance pattern:** **Autosomal dominant** with **incomplete penetrance** and **variable expressivity**.

**Penetrance:**
- Incomplete — approximately **~67% of genetically confirmed carriers are symptomatic** (5/15 asymptomatic in the founding cohort); the Lancet Rheumatology 2024 registry study confirms penetrance is incomplete and **higher in females than males**.

**Expressivity:** Markedly variable, even within families carrying an identical variant — ranging from asymptomatic status to severe multi-organ disease (e.g., the multi-generational family with the p.(Ala70Pro) variant showing a spectrum from CRPS/encephalitis in a child to adult-onset MS in the father).

**Genetic anticipation:** Not reported/established in the literature reviewed.

**Germline mosaicism:** Not specifically reported.

**Founder effects:** Not established; variants identified to date appear to be distinct across unrelated families (no recurrent founder allele described in the sources reviewed).

**Consanguinity:** Not implicated — this is a dominant, not recessive, disease mechanism.

**Carrier frequency:** Not established in general population screening databases; gnomAD constraint metrics (pLI 0.12) suggest rare LOF variants in SOCS1 do occur in the general population without necessarily causing recognized disease, consistent with incomplete penetrance.

**Population demographics:**
- **Sex ratio:** Female predominance in autoimmune manifestation expression (though the genetic variant itself is autosomal, not sex-linked) — mirrors the female bias seen in SLE and confirmed in heterozygous SOCS1+/- mouse models.
- **Geographic/ethnic distribution:** No specific ethnic or geographic clustering has been reported; cases have been described across European and US cohorts (reflecting the ESID-affiliated European SOCS1 study group and a parallel US SOCS1 study group).
- **Age distribution:** Spans pediatric to late adulthood (documented cases from age 2 to 62).

---

## 10. Diagnostics

**No formal consensus diagnostic criteria exist** for SOCS1-HI given its recent characterization (2020) and rarity. Diagnosis is established through a combination of:

**Genetic testing:**
- **Targeted gene sequencing / IEI gene panels** including *SOCS1* — the primary diagnostic modality
- **Whole exome sequencing (WES)** — used in essentially all reported index cases to identify the causal variant, often in the context of a broader IEI/autoimmunity gene panel workup
- **Chromosomal microarray (CMA)** — relevant for detecting 16p13.13 microdeletions encompassing *SOCS1* (as in the pediatric enthesitis/thrombocytopenia case)
- Variant interpretation follows standard **ACMG/AMP guidelines**; functional/in vitro validation (phospho-flow STAT assays) is recommended to support pathogenicity given the gene's relative population tolerance (pLI 0.12) and to distinguish disease-causing from benign heterozygous variants

**Functional/immunological studies (supportive, not yet standardized as formal diagnostic criteria):**
- **Phospho-flow cytometry** measuring STAT1, STAT5, STAT6 phosphorylation in response to IFN-γ, IL-2, IL-4 stimulation (elevated/prolonged in patients) and STAT3 phosphorylation in response to IL-6 (reduced)
- Flow immunophenotyping: reduced Treg frequency/function, reduced Th17 cells
- Elevated STAT-responsive gene transcripts (CXCL9, CXCL10, CISH, PIM1)
- Ex vivo ruxolitinib "correction" assays — demonstrating that JAK inhibition normalizes the hyperphosphorylation phenotype, both supporting diagnosis and predicting therapeutic response

**Laboratory/clinical tests supporting individual manifestations:**
- CBC with differential (cytopenias), Coombs test (AIHA), anti-DNA/ANA/anti-GAD antibodies (autoimmunity workup), immunoglobulin levels (hypogammaglobulinemia in some), bone marrow biopsy (hypocellularity), skin/lung/GI biopsy with histopathology (e.g., CD8+ lymphocytic leiomyositis on intestinal biopsy, granulomatous change in GLILD)
- Imaging: MRI (enthesitis, CNS demyelination in MS/encephalitis), radiologic assessment of joints

**Differential diagnosis:** STAT1 gain-of-function disease (shares STAT1 hyperactivation but typically preserves Tregs, unlike SOCS1-HI); STAT3 loss-of-function disease (shares reduced Th17/STAT3 signaling); other ALPS-like/ALPID conditions; primary SLE; idiopathic ITP/AIHA when presenting in isolation without recognized syndromic features.

**Screening:** No established population or newborn screening program exists (disease too rare/recently characterized); cascade genetic testing of relatives of an index case (as performed in the reported families) is the practical equivalent of targeted "screening" currently used.

---

## 11. Outcome/Prognosis

- No formal survival statistics (5-year/10-year survival), life-expectancy data, or population mortality rate have been established for this ultra-rare, recently described condition.
- **Disease course is highly variable** — from asymptomatic lifelong carriage to severe treatment-refractory multi-organ autoimmune/autoinflammatory disease.
- **Malignancy risk:** at least one documented progression from chronic lymphoproliferation to Hodgkin lymphoma (age 34), suggesting a potential (not yet quantified) elevated lymphoma risk analogous to other ALPS-spectrum disorders.
- **Complications:** bone marrow hypocellularity/refractory thrombocytopenia, glomerulonephritis (lupus nephritis), intestinal obstruction (lymphocytic leiomyositis), CNS demyelination/seizures, debilitating recurrent CRPS pain episodes, hypogammaglobulinemia with associated infection risk.
- **Prognostic factors:** Female sex is associated with higher penetrance and more frequent autoimmune manifestation; specific variant type/location (missense in functional domains vs. complete deletion) may correlate with severity, though this is based on limited case numbers rather than a validated prognostic model.
- **Treatment-modifying prognosis:** JAK inhibitor therapy has produced meaningful clinical and immunological remission in multiple reported cases (normalized cytokine profiles, resolved obstructive GI symptoms, reduced autoantibody titers, improved cytopenia), suggesting that with recognition and targeted treatment, disease course can be substantially favorably altered — though long-term outcome data with JAK inhibition are not yet mature given the recency of the disease's description.

---

## 12. Treatment

**Pharmacotherapy — JAK inhibitors (primary targeted therapeutic strategy):**
- **Ruxolitinib** (JAK1/JAK2 inhibitor) — demonstrated in vitro reduction of IFN-γ-induced STAT1 phosphorylation and IL-2-induced STAT5 phosphorylation, and suppression of IL-2-driven T-cell proliferation without affecting TCR-mediated responses ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)); clinically, ruxolitinib induced "rapid resolution of ... obstructive symptoms, significant decrease of the CD8+ T lymphocyte muscular infiltrate, and normalization of serum and intestinal cytokines" in a patient with lymphocytic leiomyositis ([PMC10354128](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10354128/))
- **Baricitinib** (JAK1/JAK2 inhibitor) — used in an SLE-phenotype patient (patient E1), starting at 2 mg once daily and escalated to 2 mg twice daily; produced decreased anti-DNA autoantibodies at 3 months and dose-correlated reduction in monocyte STAT1 phosphorylation ([PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/))
- **Tofacitinib** (pan-JAK inhibitor) — used successfully in a pediatric patient with severe enthesitis, bone marrow hypocellularity, and refractory thrombocytopenia, with "excellent clinical and functional laboratory response" ([Springer 2022](https://link.springer.com/article/10.1007/s10875-022-01346-x))
- Suggested NCIT term: **NCIT:C15986** (Pharmacotherapy); therapeutic agent CHEBI terms: ruxolitinib CHEBI:71196; baricitinib CHEBI:90932; tofacitinib CHEBI:75236

**Targeted cytokine blockade:**
- **Emapalumab** (anti-IFN-γ monoclonal antibody) — proposed/discussed as a promising option for highly IFN-γ-driven disease presentations, consistent with mouse-model data showing that anti-IFN-γ antibody administration rescues the lethal SOCS1-/- phenotype ([Cell, PMID:10490099](https://www.cell.com/fulltext/S0092-8674(00)80047-1); [PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))
- **IL-4Rα blockade** (e.g., dupilumab-class mechanism) and **IL-17A blockade** — shown in murine SOCS1 haploinsufficiency models to rescue autoinflammation, supporting these as candidate targeted biologic strategies (PMID:38157076, "IL4Rα and IL17A Blockade Rescue Autoinflammation in SOCS1 Haploinsufficiency")

**Experimental/emerging:**
- **SOCS1-mimetic peptides** — small peptides designed to replicate SOCS1's KIR pseudosubstrate function; still experimental, limited by "high costs, low permeability, difficulties of intracellular delivery, proteolytic instability" ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))
- **Hematopoietic stem cell transplantation (HSCT) and gene therapy** — proposed as potentially curative approaches by analogy to other severe monogenic IEIs, but not yet applied in reported SOCS1-HI patients

**Supportive/organ-specific care:**
- Standard immunosuppressive/anti-inflammatory agents for individual manifestations prior to/alongside JAK inhibition (e.g., corticosteroids, conventional cytopenia management) — used in earlier case reports before the JAK-inhibitor mechanism was recognized

**Treatment strategy:** Given the mechanistic homogeneity (JAK/STAT hyperactivation) underlying phenotypically diverse presentations, **JAK inhibition represents a rational, mechanism-based, "precision medicine" approach** applicable across the phenotypic spectrum (autoimmune, autoinflammatory, and lymphoproliferative manifestations alike), representing a genotype-informed treatment algorithm rather than organ-by-organ symptomatic management.

**Adverse events:** Not systematically reported for this population; general JAK-inhibitor class safety profile (infection risk, cytopenia, thrombosis risk) would be expected to apply, warranting caution given baseline cytopenia risk in this population.

---

## 13. Prevention

No disease-specific primary, secondary, or tertiary prevention programs, immunization strategies, or population screening programs exist for this ultra-rare, recently described monogenic condition.

- **Secondary prevention (practical, in current use):** Cascade genetic testing of first-degree relatives of an identified proband, enabling early recognition of asymptomatic/pre-symptomatic carriers who could be monitored for the onset of autoimmune/autoinflammatory manifestations, and potentially treated pre-emptively or promptly upon symptom onset.
- **Genetic counseling:** Recommended given autosomal dominant inheritance with ~50% transmission risk to offspring, tempered by counseling regarding incomplete penetrance (documented asymptomatic carriers into the 6th decade of life) and variable expressivity.
- **Infection-avoidance counseling:** Given the documented role of infection (notably SARS-CoV-2) as a disease-unmasking trigger, heightened vigilance for new autoimmune/autoinflammatory symptoms following acute infections in known carriers is a reasonable, though not formally validated, clinical practice.
- **Prophylaxis:** No specific prophylactic medication regimen has been established or studied.

---

## 14. Other Species / Natural Disease

- **Naturally occurring SOCS1 haploinsufficiency in non-human species has not been reported** in the literature surveyed. The primary cross-species data come from **engineered mouse models** (below) rather than spontaneous veterinary disease.
- No OMIA (Online Mendelian Inheritance in Animals) entries or veterinary case series for spontaneous *Socs1* haploinsufficiency were identified.
- **Comparative biology / evolutionary conservation:** The SOCS gene family (SOCS1–SOCS7, CISH) is evolutionarily conserved across vertebrates, with core JAK-inhibitory domain architecture maintained; a phylogenetic study of SOCS gene family evolution across vertebrates exists (*Mol Biol Evol* 2019, [academic.oup.com/mbe](https://academic.oup.com/mbe/article/36/2/393/5231869)), underscoring deep conservation of this negative-feedback mechanism.
- **Mouse ortholog:** *Socs1*, MGI:1354910 ([MGI SOCS1](https://www.informatics.jax.org/marker/MGI:1354910)).

---

## 15. Model Organisms

**Complete SOCS1 knockout mice (Socs1-/-):**
- Foundational studies: **Naka et al. 1998, Starr et al. 1998; Alexander et al. 1999 (Cell 98:597–608, PMID:10490099)** and **Marine et al. 1999 (Cell 98:609–616, PMID:10490100)**
- Phenotype: **perinatal lethality (~3 weeks after birth)** due to fulminant IFN-γ-driven multi-organ inflammation — monocytic infiltration of organs, fatty liver degeneration, thymic atrophy, progressive loss of B-lymphocyte maturation, and elevated baseline IFN-γ
- **Rescue experiments** were mechanistically definitive: lethality was **prevented by anti-IFN-γ neutralizing antibody administration** and **did not occur in Socs1-/-Ifng-/- double knockouts**, directly establishing IFN-γ as the principal lethal mediator ([Cell PMID:10490099](https://www.cell.com/fulltext/S0092-8674(00)80047-1))
- Also rescued by concomitant **Rag2 knockout** (removing lymphocytes), demonstrating the fatal inflammatory phenotype is **lymphocyte-dependent** ([Cell PMID:10490100](https://www.cell.com/fulltext/S0092-8674(00)80048-3))

**Heterozygous mice (Socs1+/-)** — the closer model of human haploinsufficiency:
- Normal at birth
- Develop **progressive autoimmune manifestations** with age: anti-dsDNA autoantibodies, inflammatory infiltration of lungs, salivary glands, and kidneys
- Show **female-predominant disease severity**, closely mirroring the human female bias in SLE-like manifestations
- Exhibit **reduced Treg function**
- This heterozygous model provided the foundational prediction — years before human cases were identified — that partial SOCS1 loss would produce a lupus-like autoimmune phenotype, later confirmed by the 2020 human genetic discovery ([PMC11070515](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/))

**Combined SOCS1/SOCS3 hematopoietic-specific knockouts:** Show rapid, accelerated inflammation, further underscoring the non-redundant, critical negative-feedback role of this gene family in hematopoietic cells ([PLOS ONE, journals.plos.org/plosone/article?id=10.1371/journal.pone.0162111](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0162111)).

**Model applications:** These mouse models have been used to (1) establish IFN-γ as the central pathogenic cytokine, informing the rationale for **emapalumab** as a candidate therapy; (2) demonstrate the JAK/STAT hyperactivation mechanism that underlies the rationale for **JAK inhibitor** therapy; and (3) test candidate biologic therapies — **IL-4Rα and IL-17A blockade rescued autoinflammation** in the Socs1 haploinsufficient mouse model (PMID:38157076), directly nominating these as translational therapeutic candidates for human SOCS1-HI.

**Model limitations:** The complete knockout is not a faithful haploinsufficiency model (it is uniformly lethal and represents complete rather than partial loss); the heterozygous mouse, while a better dosage match, does not fully recapitulate the extreme phenotypic breadth seen in humans (e.g., neurological manifestations such as MS/CRPS have not been reported as a feature of the mouse heterozygous model in the sources reviewed), and no mouse model to date has reproduced the lymphoproliferative-to-lymphoma progression seen in at least one human patient.

**Resources:** MGI:1354910 (Socs1 mouse gene record, [informatics.jax.org](https://www.informatics.jax.org/marker/MGI:1354910)).

---

## Summary of Key Evidence Gaps

- No formal population prevalence/incidence estimate exists (disease too rare/recently described)
- No dedicated GeneReviews chapter or standardized diagnostic criteria identified
- No large omics dataset (transcriptomic/proteomic) specific to patient cohorts identified
- ClinGen Dosage Sensitivity curation for SOCS1 is not yet completed
- Long-term outcome data on JAK-inhibitor-treated patients are not yet mature
- Quality-of-life instrument data (EQ-5D/SF-36 or disease-specific) are absent from the literature reviewed

---

## Sources

- [One Gene, Many Facets: Multiple Immune Pathway Dysregulation in SOCS1 Haploinsufficiency (PMC8375263)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8375263/)
- [Immune dysregulation and multisystem inflammatory syndrome in children (MIS-C) in individuals with haploinsufficiency of SOCS1 - PubMed](https://pubmed.ncbi.nlm.nih.gov/32853638/)
- [OMIM 603597 - SOCS1](https://omim.org/entry/603597)
- [Early-onset autoimmunity associated with SOCS1 haploinsufficiency | Nature Communications](https://www.nature.com/articles/s41467-020-18925-4)
- [Early-onset autoimmunity associated with SOCS1 haploinsufficiency - PMC7578789](https://pmc.ncbi.nlm.nih.gov/articles/PMC7578789/)
- [One gene to rule them all – clinical perspectives of a potent suppressor of cytokine signaling – SOCS1 (Frontiers/PMC11070515)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070515/)
- [Clinical manifestations, disease penetrance, and treatment in individuals with SOCS1 insufficiency - Lancet Rheumatology 2024](https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(24)00348-5/fulltext)
- [Autoimmune lymphoproliferative immunodeficiencies (ALPID) in childhood (PMC10499775)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10499775/)
- [SOCS1 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SOCS1)
- [SOCS1 curation results - ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:19383)
- [SOCS1 gene details - Genebe](https://genebe.net/gene/hg38/SOCS1)
- [Neurological Phenotypes of SOCS1 Haploinsufficiency (PMC12628480)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12628480/)
- [SOCS1 Haploinsufficiency Presenting as Severe Enthesitis, Bone Marrow Hypocellularity, and Refractory Thrombocytopenia... - Springer](https://link.springer.com/article/10.1007/s10875-022-01346-x)
- [Insights into the expanding intestinal phenotypic spectrum of SOCS1 haploinsufficiency and therapeutic options (PMC10354128)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10354128/)
- [IL4Rα and IL17A Blockade Rescue Autoinflammation in SOCS1 Haploinsufficiency - PubMed](https://pubmed.ncbi.nlm.nih.gov/38157076/)
- [SOCS1 deficiency—crossroads of autoimmunity and autoinflammation—two case reports (PMC11746893)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11746893/)
- [SOCS1 Is a Critical Inhibitor of Interferon γ Signaling... - Cell (PMID:10490099)](https://www.cell.com/fulltext/S0092-8674(00)80047-1)
- [SOCS1 Deficiency Causes a Lymphocyte-Dependent Perinatal Lethality - Cell (PMID:10490100)](https://www.cell.com/fulltext/S0092-8674(00)80048-3)
- [Rapid Inflammation in Mice Lacking Both SOCS1 and SOCS3 in Hematopoietic Cells - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0162111)
- [Insights into the Evolution of the SOCS Gene Family in Vertebrates - Mol Biol Evol](https://academic.oup.com/mbe/article/36/2/393/5231869)
- [Socs1 MGI Mouse Gene Detail - MGI:1354910](https://www.informatics.jax.org/marker/MGI:1354910)
- [Orphanet: Early-onset autoimmunity-autoinflammation-immunodeficiency syndrome due to SOCS1 haploinsufficiency](https://www.orpha.net/en/disease/detail/619948)
- [Phenotypic Variability of SOCS1 Haploinsufficiency - PubMed](https://pubmed.ncbi.nlm.nih.gov/36890397/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1371/journal.pone.0162111](https://journals.plos.org` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11070515` *(abstract only)*: "high costs, low permeability, difficulties of intracellular delivery, proteolytic instability"
  - Text part not found as substring: 'high costs, low permeability, difficulties of intracellular delivery, proteolytic instability' (note: only abstract available for PMID:38711523, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1007/s10875-022-01346-x`: "excellent clinical and functional laboratory response"
  - Reference resolved but exposes no abstract or full text to search