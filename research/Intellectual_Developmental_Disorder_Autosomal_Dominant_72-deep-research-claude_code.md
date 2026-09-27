---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T08:38:01.381292'
end_time: '2026-08-19T08:43:10.132475'
duration_seconds: 308.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Developmental Disorder, Autosomal Dominant 72
  mondo_id: ''
  category: Genetic
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
  num_turns: 31
  total_cost_usd: 2.3627932000000005
  session_id: 97f41810-e806-56ab-ba28-3afc344c20f9
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 9
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, Autosomal Dominant 72
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, Autosomal Dominant 72** covering all of the
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

I now have comprehensive data across genetics, molecular mechanism, clinical phenotype, animal models, and structural variant literature. Compiling the full research report.

---

# Intellectual Developmental Disorder, Autosomal Dominant 72 (MRD72 / SRRM2-Related Neurodevelopmental Disorder)

## 1. Disease Information

**Overview.** Intellectual Developmental Disorder, Autosomal Dominant 72 (MRD72), also referred to as SRRM2-related neurodevelopmental disorder, is a recently delineated genetic condition caused by heterozygous, predominantly de novo, loss-of-function (LoF) variants in **SRRM2** (Serine/Arginine Repetitive Matrix Protein 2), a core nuclear-speckle scaffold protein and pre-mRNA splicing factor. It was first formally characterized as a distinct clinical entity by Cuinat et al. (2022, *Genetics in Medicine*, PMID: [35567594](https://pubmed.ncbi.nlm.nih.gov/35567594/)), who described 22 unrelated individuals ascertained through GeneMatcher, following earlier statistical implication of *SRRM2* as a developmental-disorder gene by the Deciphering Developmental Disorders (DDD) study (Kaplanis et al. 2020, *Nature*, PMID: [33057194](https://pubmed.ncbi.nlm.nih.gov/33057194/)), which identified *SRRM2* as one of 28 genes newly and robustly associated with developmental disorders via statistical enrichment of de novo mutations across 31,058 parent-offspring trios.

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM Phenotype | [#620439](https://omim.org/entry/620439) — INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 72; MRD72 |
| OMIM Gene | [*606032](https://omim.org/entry/606032) — SRRM2 |
| HGNC | HGNC:16639 |
| NCBI Gene ID | 23524 |
| Cytogenetic location | 16p13.3 |
| GRCh38 coordinates | chr16:2,752,626–2,772,538 (+) |
| ClinGen Dosage (CCID:007940) | Sufficient Evidence for Haploinsufficiency (score 3); No Evidence for Triplosensitivity (0) |
| Inheritance | Autosomal dominant (nearly always de novo) |

**Synonyms/alternative names:** SRRM2-related neurodevelopmental disorder; SRRM2 haploinsufficiency syndrome; MRD72; the gene product is historically known as SRm300 (300-kD splicing factor) with aliases CWF21, Cwc21, SRL300.

**Evidence basis.** Nearly all published knowledge derives from **aggregated disease-level case series** compiled through international gene-matching platforms (GeneMatcher), large-scale trio-exome cohorts (DDD/GeneDx), and structural-variant registries (Genomics England 100,000 Genomes Project), rather than single-patient case reports alone (though several individual case reports have since expanded the phenotypic spectrum). No dedicated patient registry or natural-history study yet exists.

---

## 2. Etiology

**Disease causal factor:** Heterozygous loss-of-function of *SRRM2* — frameshift, nonsense, canonical splice-site variants, or contiguous gene deletions spanning the locus — is the sole established cause. The mechanism is **haploinsufficiency**, not dominant-negative or gain-of-function, based on:
- ClinGen curation assigning "Sufficient Evidence for Haploinsufficiency" (score 3)
- gnomAD constraint metrics: **pLI = 1.0**, **LOEUF = 0.18** (well within the top haploinsufficiency decile, threshold <0.35), observed/expected LoF ratio ≈0.06 — indicating extreme intolerance to LoF variation in the general population
- In parallel, SRRM2 shows *tolerance* to missense variation (missense Z ≈ −6.28, o/e ≈1.43), consistent with LoF (not missense-driven dominant-negative) as the principal pathomechanism, though rare pathogenic missense variants in the intrinsically disordered region (IDR) have since been reported (see below)
- Mouse data: *Srrm2*-null (homozygous) mice are embryonic lethal (preweaning lethality, IMPC), while *Srrm2+/−* heterozygotes are viable but show molecular and behavioral phenotypes — directly modeling human haploinsufficiency

**Genetic risk factors:**
- De novo heterozygous frameshift or nonsense SNVs/indels in *SRRM2* (majority of cases)
- De novo microdeletions of the 16p13.3 locus spanning *SRRM2* (66–482 kb reported), several arising via a recombination-prone **~144 kb palindrome-like structure** located ~75 kb upstream of *SRRM2* (GRCh38 chr16:2,534,000–2,678,000), which predisposes to complex structural rearrangements including deletions with internal inversions (Pagnamenta et al. 2023, *Human Mutation*, PMC11918891)
- Rare de novo missense variants within the SRRM2 intrinsically disordered region, associated with an expanding/atypical phenotype (see Phenotypes)
- No recurrent/founder variant has been identified; nearly all reported variants are private (patient-specific)

**Environmental risk factors:** None established; this is a purely monogenic disorder with no known environmental, infectious, toxin, or lifestyle contributors to primary disease causation.

**Protective factors:** None identified at the genetic or environmental level. No modifier genes or protective alleles have been reported to date, reflecting the rarity and recency of the condition's description.

**Gene-environment interactions:** None reported; insufficient case numbers and no systematic epidemiological studies exist to assess G×E effects.

**Suggested ontology terms:** MONDO term for SRRM2-related neurodevelopmental disorder (mapped to OMIM 620439); HGNC:16639 (SRRM2); NCBITaxon:9606 (Homo sapiens).

---

## 3. Phenotypes

Data drawn primarily from the Cuinat et al. 2022 cohort (n=22), the Pagnamenta et al. 2023 100,000 Genomes Project structural-variant cohort (n=4–6), and individual case reports (tics/PMC12488763; hyperphagia-obesity/Frontiers 2025).

### Core neurodevelopmental phenotypes (Cuinat cohort, LoF variants — typically milder end of spectrum)
| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Developmental delay | 22/22 (100%) | HP:0001263 Global developmental delay |
| Predominant speech/language delay | 16/19 (84%) | HP:0000750 Delayed speech and language development |
| Gross motor developmental delay | 8/22 (36%) | HP:0002194 Delayed gross motor development |
| Mild intellectual disability | 16/22 (73%) | HP:0001256 Mild intellectual disability |
| Borderline intellectual disability | 4/22 (18%) | HP:0006889 Borderline intellectual functioning |
| Autism spectrum / ASD features | present in subset | HP:0000729 Autistic behavior |
| ADHD features | present in subset (6/22 in one tabulation) | HP:0007018 Attention deficit hyperactivity disorder |
| Overfriendliness / sociable personality | frequent, characteristic | HP:0000750-adjacent behavioral descriptor (no precise HP term; often coded as HP:0000722 Sociable/gregarious personality if used) |
| Generalized hypotonia | common | HP:0001290 Generalized hypotonia |
| Overweight/obesity | 12/22 (~55%) | HP:0001513 Obesity |

### Dysmorphic facial features (Cuinat cohort)
| Feature | Frequency | Suggested HPO term |
|---|---|---|
| Epicanthus | 3/22 | HP:0000286 Epicanthus |
| Deep-set eyes | 10/22 | HP:0000490 Deeply set eye |
| Large ears | 7/22 | HP:0000400 Macrotia |
| Low-set, posteriorly rotated ears | 4/22 | HP:0000369 Low-set ears / HP:0000368 Posteriorly rotated ears |
| Broad/bulbous nasal tip | 9/22 | HP:0000414 Bulbous nose |
| Smooth philtrum | 6/22 | HP:0000319 Smooth philtrum |
| Thin upper lip | 7/22 | HP:0000219 Thin upper lip vermilion |
| Broad chin | 6/22 | HP:0000324 Broad chin |

### More severe structural-variant phenotype (100,000 Genomes Project deletion cohort, n=4–6)
This subgroup — carrying larger contiguous deletions rather than point LoF variants — shows a **more severe phenotype** than the Cuinat SNV cohort:
- Moderate-to-severe intellectual disability (vs. typically mild in the LoF-SNV cohort)
- Microcephaly in 3/6 (50%) vs. ~5% in the SNV cohort — HP:0000252 Microcephaly
- Seizures in 2/6 — HP:0001250 Seizure
- Dystonia in 2/6 — HP:0001332 Dystonia
- Autistic features 4/6, ADHD traits 5/6
- Additional dysmorphism: geographic tongue, large ears, tapering fingers, prominent halluces (HP:0001155 Broad hallux phalanx / tapering finger descriptors)

*This genotype-phenotype gradient (SNV/frameshift → milder; large contiguous deletion → more severe) suggests dosage or contiguous-gene effects and is an important curation nuance.*

### Expanding phenotype — missense/IDR variants
A 2025 case report (Frontiers in Medicine, PMC11880253) of a de novo missense variant (p.Q1554L) in the SRRM2 intrinsically disordered region described a novel, more metabolically severe presentation:
- Hyperphagia driving rapid-onset severe obesity (BMI 44.6 by age 17) — HP:0002591 Polyphagia / HP:0001513 Obesity
- Macrocephaly (contrasting with microcephaly in the deletion cohort) — HP:0000256 Macrocephaly
- Short hands and feet — HP:0001217 Small hand / HP:0001773 Short foot
- Secondary complications: stage IV cardiogenic insufficiency, hypertension, hyperlipidemia, obstructive sleep apnea
- UK Biobank association data cited supporting SRRM2 missense variants correlating with increased body weight in the general population

### Additional reported feature — tics/movement disorder
A single case report (2025, PMC12488763) of a 16p13.3 microdeletion presented atypically with **late-onset (age 25) simple motor and vocal tics progressing to catatonic-type tics** (Yale Global Tic Severity Scale 55/100), notably *without* the hypotonia, dysmorphism, or obesity typical of the syndrome — expanding the phenotypic spectrum to include movement disorder/tic phenomenology (HP:0100033 Tics).

**Quality of life impact:** No formal QoL instrument (EQ-5D, SF-36) data have been published for this rare, recently described condition. Qualitatively, developmental delay/intellectual disability, obesity-related cardiometabolic complications (in a subset), and speech delay are the dominant drivers of functional impact reported in case series.

---

## 4. Genetic/Molecular Information

**Causal gene:** SRRM2 (HGNC:16639; OMIM *606032), encoding a large (~2,752 amino acid) intrinsically-disordered-region-rich splicing factor (SRm300 protein).

**Pathogenic variant spectrum (Cuinat et al. 2022, n=22 unrelated probands):**
- 12 frameshift variants
- 8 nonsense variants
- 2 microdeletions (66 kb and 270 kb)
- 19/20 confirmed de novo (essentially all cases where parental testing was performed)

**Structural variant spectrum (Pagnamenta et al. 2023, 100,000 Genomes Project):**
- 4 unrelated individuals with de novo whole-gene deletions, 248–482 kb
- All distal breakpoints cluster within the upstream 16p13.3 palindrome-like structure
- 3/4 deletions show internal inverted segments (45–94 kb) — complex structural variant architecture, likely arising via replication-based or hairpin/cruciform-mediated recombination mechanisms during DNA repair/replication

**Emerging missense/IDR variant:**
- p.Q1554L (NM_016333.4: c.4661A>T), de novo, classified Likely Pathogenic (ACMG PS2, PM2, PP3), located in the SRRM2 IDR, predicted to disrupt local hydrophilicity and liquid-liquid phase separation properties

**Variant classification (ClinVar):** Predominantly Pathogenic/Likely Pathogenic per ACMG/AMP; example variant NM_016333.4(SRRM2):c.7748_7758del (p.Thr2583fs) classified pathogenic for "Intellectual developmental disorder, autosomal dominant 72" (ClinVar RCV004763624).

**Population frequency / constraint (gnomAD):**
- pLI = 1.0; LOEUF = 0.18 (strong LoF intolerance)
- Missense Z ≈ −6.28, o/e(missense) ≈1.43 (missense tolerant — supports haploinsufficiency, not dominant-negative, as principal mechanism for truncating variants)
- Estimated population prevalence of pathogenic de novo LoF: ~1/1,827 among DDD-ascertained developmental-disorder trios (17/31,058; likely an underestimate, as exome sequencing under-captures structural variants); broader unexplained-ID cohort estimates cited around 1/1,300; general-population prevalence estimated in the range of 1/11,000–1/50,000 (early, imprecise estimates given the condition's recent description)

**Functional consequence:** Loss of one functional SRRM2 allele → haploinsufficiency of SRm300 → disrupted nuclear speckle organization and impaired pre-mRNA splicing (see Mechanism, below). No dominant-negative or gain-of-function mechanism has been established for truncating variants; the missense IDR variant is hypothesized to act via altered phase-separation biophysics rather than classical LOF/GOF dichotomy.

**Modifier genes:** None identified.

**Epigenetic information:** Not specifically studied in this disorder to date.

**Chromosomal abnormalities:** Beyond the palindrome-associated microdeletions above, no recurrent translocations, aneuploidies, or larger syndromic contiguous-gene deletions (beyond *SRRM2* itself) have been robustly linked to a distinct phenotype.

**Suggested ontology terms:** HGNC:16639 (SRRM2); GO:0000398 (mRNA splicing, via spliceosome); GO:0016607 (nuclear speck); GO:0003729 (mRNA binding); UniProt Q9UQ35 (SRRM2_HUMAN, SRm300/SRRM2).

---

## 5. Environmental Information

No environmental factors, lifestyle exposures, or infectious agents have been implicated in causing or triggering MRD72. This is a purely genetically determined, predominantly de novo condition. Environmental/lifestyle factors (diet, activity) are relevant only as **secondary modifiers of the obesity/metabolic complications** seen in a subset of patients, not as disease-causal agents.

---

## 6. Mechanism / Pathophysiology

**Molecular function of SRRM2 / SRm300:**
SRRM2 encodes an RS-domain-containing, intrinsically-disordered-region-rich splicing coactivator (SRm300) that:
- Docks directly onto core U5 snRNP proteins Prp8 and Snu114 at the spliceosome catalytic center (identified by cryo-EM in spliceosomal structures)
- Promotes physical interaction between pre-mRNA and the spliceosome catalytic machinery, supporting both constitutive splicing and exonic splicing enhancer (ESE)-dependent alternative splicing
- Together with SON, acts as a principal molecular scaffold that organizes **nuclear speckles** — membraneless nuclear bodies enriched in splicing factors — via **liquid-liquid phase separation** driven by the intrinsically disordered regions of SRRM2 and SON (Ilik et al. 2020, PMID: 33095160; SRRM2 condensate biology, PMC9410892)

**Causal chain (haploinsufficiency → disease):**
1. Heterozygous LoF variant/deletion → ~50% reduction in functional SRRM2 protein (GO:0003729 mRNA binding; GO:0000398 mRNA splicing via spliceosome)
2. Disrupted nuclear speckle architecture/organization (GO:0016607 nuclear speck) — impaired phase-separation-driven condensate assembly
3. Genome-wide **alternative splicing dysregulation** — preferentially affecting cassette exons with short introns and weak splice sites, with a tendency to alter large protein domains
4. Downstream transcriptomic and proteomic perturbation of neurodevelopmentally important genes
5. Impaired neuronal/glial development and synaptic protein regulation → clinical neurodevelopmental phenotype

**Cellular/developmental model evidence:**
- **Mouse embryonic stem cells** (Srrm2+/− heterozygous knockout): reduced colony formation, dispersed clustering, reduced alkaline phosphatase (pluripotency marker) activity; loss of stemness with intermediate pluripotency states; altered splicing of *Dtx3* (NOTCH pathway) and *Pcyt2* (phospholipid synthesis, itself embryonic-lethal when fully knocked out) precedes broader transcriptional changes; upregulation of SRF-controlled mesoderm/cardiac differentiation genes (PMC11070786, *Biology Open* 2024) — establishes SRRM2 dosage as critical for stemness/cell-identity maintenance in early development
- **Mouse (Srrm2+/−) brain model** (Cell Reports, 2026; bioRxiv PMID pending, preprint 2024.10.10.617460): large-scale gene-expression changes across neuronal and glial populations affecting DNA-binding, synapse, translation, and mitochondria-related pathways; **reduction of the gamma isoform of SynGAP** (a key postsynaptic Ras/Rap GAP regulating synaptic plasticity) and reciprocal elevation of its interactor **AGAP3**; reduced oligodendrocyte proportions (particularly striatal) with decreased myelin-related mRNA/protein expression; behaviorally, reduced locomotor activity and impaired acoustic startle response; **EEG shows reduced sleep spindles**, a finding paralleling human schizophrenia electrophysiology. Human iPSC-derived neurons with SRRM2 deficiency show conserved AGAP3 mis-splicing, directly bridging the mouse mechanism to human neurobiology. This positions SRRM2 haploinsufficiency as a shared mechanistic node between neurodevelopmental disorder and schizophrenia risk.
- **Homozygous Srrm2-null mice**: preweaning embryonic lethal (IMPC data), confirming SRRM2 is essential for viability and that only the heterozygous (haploinsufficient) state is compatible with life — directly mirroring the human autosomal dominant/de novo heterozygous disease model.

**Cell types and biological processes involved:**
- Neurons and glial cells (oligodendrocytes specifically implicated) — suggested CL terms: CL:0000540 (neuron), CL:0000128 (oligodendrocyte)
- Pluripotent stem/progenitor cells during early embryonic development
- Core biological processes: GO:0000398 mRNA splicing via spliceosome; GO:0000381 regulation of alternative mRNA splicing, via spliceosome; GO:0016607 nuclear speck organization; GO:0007399 nervous system development; GO:0022010 central nervous system myelination

**Metabolic changes:** In the hyperphagia/obesity-associated missense case, downstream metabolic dysregulation (hyperphagia → severe obesity → cardiometabolic complications) represents a secondary, phenotype-specific consequence rather than a core molecular pathway finding; mechanistic basis for the hyperphagia is not yet established but is hypothesized to relate to hypothalamic splicing dysregulation.

**Immune system involvement:** Not implicated; no autoimmune or immunodeficiency features reported.

**Advanced/omics technologies applied:**
- Single-cell transcriptomic analysis of Srrm2+/− mouse ES cells (four distinct cellular states identified)
- Bulk and cell-type-resolved transcriptomics/splicing analysis in Srrm2+/− mouse brain (multiple regions) and human iPSC-derived neurons
- No published proteomics, metabolomics, or spatial transcriptomics specific to this disorder to date

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Central nervous system (brain) — developmental delay, intellectual disability, hypotonia, (in severe subgroup) seizures, dystonia, microcephaly
- Secondary: Adipose tissue/metabolic system (obesity, hyperphagia in subset); cardiovascular system (hypertension, cardiogenic insufficiency secondary to severe obesity); craniofacial skeleton and soft tissue (dysmorphic facial features)
- Body systems: Nervous system, endocrine/metabolic system, musculoskeletal system (short hands/feet in one report), integumentary/craniofacial

**Suggested UBERON terms:** UBERON:0000955 (brain); UBERON:0001013 (adipose tissue); UBERON:0000948 (heart); UBERON:0001456 (face)

**Tissue and cell level:**
- Neurons (CL:0000540) and oligodendrocytes (CL:0000128) — from the mouse Srrm2+/− brain model
- Embryonic/pluripotent stem cells (CL:0002322) — from the mESC model
- Adipose tissue cells — implicated in obesity phenotype but not specifically characterized at cellular resolution

**Subcellular level:**
- Nuclear speckles (GO:0016607) — the primary subcellular structure directly disrupted by SRRM2 haploinsufficiency
- Spliceosome (GO:0005681) — catalytic center where SRRM2/SRm300 docks (Prp8, Snu114 interaction)
- Nucleus generally (GO:0005634)

**Localization/lateralization:** No lateralization pattern reported; phenotypes are bilateral/systemic (developmental, craniofacial, metabolic) as expected for a germline splicing-factor disorder.

---

## 8. Temporal Development

**Onset:** Congenital/early childhood onset. Developmental delay is typically first recognized in infancy/early childhood (failure to meet motor milestones — e.g., not sitting independently by 12 months, not walking by 18 months — and speech delay — not using two-word phrases by 24 months, per the tic case report's developmental history).

**Onset pattern:** Insidious/developmental rather than acute; a chronic, non-episodic neurodevelopmental trajectory.

**Progression:**
- Developmental delay/intellectual disability is generally **stable-to-mildly progressive** in cognitive terms, consistent with a static encephalopathy-type neurodevelopmental disorder rather than a degenerative one, though long-term natural history data are extremely limited given how recently the condition was described (2020–2022 for gene discovery/first cohort)
- **Obesity is progressive** in the subset of patients who develop it, worsening from childhood-onset hyperphagia to severe adult obesity with escalating cardiometabolic complications (documented longitudinally in the age 7→17 case report)
- **Tics**, in the one reported case, had an atypically late onset (age 25, well past the typical ~age 6 onset for neurodevelopmental tic disorders) and were progressive in severity (simple motor/vocal → complex catatonic-type tics)

**Disease course pattern:** Chronic, lifelong; no spontaneous remission reported for the core neurodevelopmental phenotype. No defined discrete "stages" (early/intermediate/advanced) have been established in the literature, reflecting the condition's recency and small case numbers.

**Critical periods:** Embryonic/early postnatal neurodevelopment is the presumed critical window, based on mouse ESC data showing SRRM2 dosage is critical for stemness maintenance and early lineage specification, and homozygous-null embryonic lethality in mice.

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence/incidence study exists. Estimates (indirect, derived from cohort ascertainment):
- ~1/1,827 among DDD-ascertained developmental-disorder trios (de novo pLoF only; likely underestimated as structural variants are under-captured by exome sequencing)
- ~1/1,300 cited in cohorts of individuals with unexplained intellectual disability
- Broader population prevalence estimates in the range of 1/11,000–1/50,000 have been cited but should be treated as provisional given the small evidence base

**Inheritance pattern:** Autosomal dominant (per OMIM #620439 designation); however, essentially all confirmed cases are **de novo** (19/20 in Cuinat cohort with parental testing; all four 100kGP deletion cases de novo). No multi-generational transmission has been documented in the literature reviewed, though the condition is formally classified as AD (implying that transmission from an affected, reproductively fit parent would in principle occur with 50% recurrence risk).

**Penetrance:** Appears to be high/complete for the core developmental delay phenotype based on cases identified to date, though this is based on small numbers, and germline/somatic mosaicism has not been systematically assessed.

**Expressivity:** Markedly **variable** — ranging from mild intellectual disability with characteristic facial gestalt (typical LoF/SNV phenotype) to moderate-severe ID with microcephaly and seizures (large-deletion phenotype) to an atypical late-onset tic-predominant presentation without the classic dysmorphism/obesity, to a hyperphagia/severe-obesity-predominant presentation (missense/IDR variant). This genotype-phenotype heterogeneity is one of the most clinically important features of the disorder.

**Genetic anticipation:** Not applicable/not reported (this is not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented but theoretically possible given the de novo mechanism; not systematically studied.

**Founder effects:** None identified; variants are private/patient-specific with no recurrent pathogenic allele.

**Consanguinity:** Not relevant, given the autosomal dominant/de novo mechanism (not a recessive disorder).

**Carrier frequency:** Not applicable in the traditional sense (AD, not AR); population allele frequency of pathogenic LoF variants is expected to be near zero in unaffected populations given the severe negative selection reflected by pLI=1.0/LOEUF=0.18.

**Population demographics:** No specific ethnic or geographic enrichment reported; cases have been identified across multiple international cohorts (France/Cuinat et al., UK Genomics England 100,000 Genomes Project, and additional individual case reports from various countries), consistent with a pan-ethnic de novo disorder without founder population bias.

**Sex ratio:** Not explicitly reported as skewed in the literature reviewed; no clear male:female bias has been established.

**Age distribution:** Reported patients range from early childhood through adulthood (oldest reported case, the tic patient, was 30 years old at report), reflecting ascertainment across pediatric and adult genetics clinics.

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES)** or **whole genome sequencing (WGS)**, typically as trio analysis (proband + both parents) to establish de novo status — this is how essentially all reported cases have been ascertained (GeneMatcher-facilitated case matching, DDD/100,000 Genomes Project cohorts)
- **Chromosomal microarray (CMA)** — necessary to detect the microdeletion subset (66 kb–482 kb), which would be missed by exome sequencing alone; WGS with structural-variant calling is increasingly important given the palindrome-associated complex rearrangements described by Pagnamenta et al.
- Single-gene *SRRM2* sequencing is not a standard first-tier approach given the absence of a recognizable, specific enough clinical gestalt to prompt targeted testing; it is typically identified via exome-wide or panel-based ID/developmental-disorder gene panels (e.g., Genomics England PanelApp "Intellectual disability" panel includes SRRM2)
- No specific biomarkers, laboratory tests, imaging findings, or electrophysiologic signatures are diagnostic; EEG abnormalities (reduced sleep spindles) are so far only described in the mouse model, not systematically in human patients (though the 100kGP cohort did include seizure patients, presumably with abnormal EEGs, not detailed further)

**Clinical criteria:** No formal consensus diagnostic criteria exist (condition too recently described). Diagnosis is genetic-confirmation-based: identification of a de novo (or presumed pathogenic) heterozygous LoF variant or deletion in SRRM2 in the context of compatible developmental delay/ID, ideally with supportive dysmorphology.

**Differential diagnosis:** Other genetic causes of syndromic intellectual disability with overlapping features (hypotonia, obesity, ASD/ADHD traits, dysmorphism) — e.g., other chromatin/splicing-factor-related neurodevelopmental disorders, and Prader-Willi-like syndromes when hyperphagia/obesity dominate the presentation (relevant to the missense-variant case). Given the phenotypic overlap with hyperphagic obesity syndromes, differentiation typically requires exome/genome sequencing rather than clinical gestalt alone.

**Screening:** No population, carrier, or newborn screening applies, given the de novo, non-recurrent nature of the disorder.

---

## 11. Outcome/Prognosis

No formal survival, mortality, or long-term outcome studies exist. Based on available case reports:
- The disorder is not associated with reduced lifespan intrinsically, though **secondary cardiometabolic complications from severe obesity** (in the subset who develop hyperphagia-driven obesity) — including stage IV cardiac insufficiency, hypertension, hyperlipidemia, and obstructive sleep apnea documented in one adolescent case — represent a significant, potentially life-limiting morbidity pathway if unmanaged
- Cognitive outcome ranges from mild intellectual disability/borderline functioning (most common, per the Cuinat LoF cohort) to moderate-severe intellectual disability (in the larger-deletion subgroup)
- No natural history data on adult functional independence, employment, or long-term psychiatric outcomes (though the mouse model's schizophrenia-relevant EEG/behavioral findings raise a hypothesis-generating question about long-term psychiatric risk in human carriers that has not yet been clinically studied)
- Prognostic factors identified so far are primarily **genotypic**: variant/deletion size and type appear to correlate with severity (SNV/frameshift → milder; large contiguous deletion → more severe with microcephaly/seizures; IDR missense → distinct hyperphagia-obesity-predominant course)

---

## 12. Treatment

There is **no disease-specific or targeted therapy** for MRD72; management is entirely symptomatic/supportive, individualized to the phenotypic subtype:

- **Developmental/behavioral therapies:** Early intervention services, speech-language therapy (for the predominant speech delay), physical/occupational therapy, and special education support — suggested NCIT terms: NCIT:C15302 (Physical Therapy), NCIT:C159273 (Speech Therapy), NCIT:C121351 (Occupational Therapy)
- **Behavioral/psychiatric management:** For ASD/ADHD features — behavioral counseling and, where indicated, standard ADHD pharmacotherapy (not SRRM2-specific) — NCIT:C181743 (Behavioral Counseling), NCIT:C15986 (Pharmacotherapy)
- **Movement disorder management:** In the tic-predominant case, alpha-2 agonist **clonidine** was recommended for tic management — NCIT:C15986 (Pharmacotherapy) with therapeutic_agent CHEBI (clonidine)
- **Metabolic/obesity management:** Dietary intervention was attempted (with limited success against uncontrolled hyperphagia) in the obesity case; standard multidisciplinary obesity management (nutrition, weight management, cardiometabolic risk-factor treatment for hypertension/hyperlipidemia/sleep apnea) — NCIT:C15447 (Dietary Intervention), NCIT:C15747 (Supportive Care)
- **Genetic counseling:** Recommended for all families given the de novo autosomal dominant mechanism, to discuss recurrence risk (low, but non-zero due to potential germline mosaicism) — NCIT:C15240 (Genetic Counseling)
- **Experimental/targeted therapies:** None in development or clinical trials specific to SRRM2-related disorder as of this writing; no NCT-registered trials identified. The mechanistic convergence with schizophrenia biology (SynGAP-γ, AGAP3, oligodendrocyte/myelination pathways) identified in the 2026 mouse model study represents a potential future avenue for mechanism-informed therapeutic exploration, but this is preclinical only.

**Treatment outcomes/response rates:** Not systematically studied; case-by-case symptomatic management only.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies exist for the underlying de novo genetic event, as with most sporadic monogenic developmental disorders.

- **Prenatal/reproductive counseling:** For families with a previously affected child, genetic counseling regarding low (but non-zero, due to potential parental germline mosaicism) recurrence risk, and availability of prenatal diagnosis (chorionic villus sampling/amniocentesis with targeted variant testing) or preimplantation genetic testing (PGT-M) if the familial variant is known
- **Secondary prevention:** Early developmental screening and early intervention referral upon recognition of developmental delay can improve functional outcomes generally (standard developmental-pediatrics practice, not SRRM2-specific)
- **Tertiary prevention:** Proactive metabolic/cardiovascular monitoring (weight, blood pressure, lipids, sleep study) in patients showing early hyperphagia, to prevent/mitigate the severe obesity-related cardiometabolic complications documented in case reports
- No vaccination, public health, or environmental intervention is relevant, as there is no infectious or environmental disease-causal component

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease analog has been reported (NCBITaxon:9606, human, is the only species with described clinical disease)
- **Orthologous gene:** Mouse *Srrm2* (MGI:1923206, chromosome 17) is the primary ortholog used experimentally; no OMIA (naturally occurring animal disease) entries exist for SRRM2
- **Comparative biology:** The mouse gene shows the same essential/dosage-sensitive biology as the human gene (homozygous-null embryonic lethal; heterozygous viable with molecular/behavioral phenotype), supporting deep evolutionary conservation of SRRM2's role in nuclear speckle organization and splicing regulation across mammals
- **Zoonotic potential:** Not applicable (monogenic disorder, not infectious)

---

## 15. Model Organisms

| Model | Type | Key findings | Source |
|---|---|---|---|
| **Mouse embryonic stem cells** (E14tg2a.4 line), *Srrm2+/−* heterozygous knockout | Cellular/genetic model | Impaired colony formation, reduced pluripotency (alkaline phosphatase) markers, loss of stemness with intermediate pluripotent states, altered splicing of *Dtx3*/*Pcyt2* preceding transcriptional changes | Biology Open 2024, PMC11070786 |
| **Mouse**, *Srrm2* homozygous knockout | Whole-organism genetic model | Embryonic/preweaning lethal (IMPC data) — establishes essential gene status | IMPC; cited in multiple SRRM2 papers |
| **Mouse**, *Srrm2+/−* heterozygous (brain-focused) | Whole-organism genetic model of schizophrenia/NDD | Neuronal/glial transcriptomic changes (synapse, mitochondria, translation pathways); reduced SynGAP-γ; elevated AGAP3; reduced striatal oligodendrocyte proportion and myelin gene/protein expression; reduced locomotor activity; impaired acoustic startle; reduced EEG sleep spindles (parallels human schizophrenia electrophysiology) | Cell Reports 2026 (preprint bioRxiv 2024.10.10.617460) |
| **Human iPSC-derived neurons**, SRRM2-deficient | Cellular (isogenic) human model | Conserved AGAP3 mis-splicing recapitulating the mouse finding — bridges mouse mechanism to human neuronal biology | Same Cell Reports 2026 study |

**Model characteristics/limitations:** The mouse Srrm2+/− brain model shows strong construct validity (same haploinsufficiency mechanism as human disease) and notable face validity for neurophysiological (EEG spindle) and behavioral (locomotor, startle) endpoints relevant to neurodevelopmental/psychiatric phenotypes, but does not model the craniofacial dysmorphism, obesity/hyperphagia, or human-specific cognitive/speech phenotypes seen clinically — this is best flagged as a `HUMAN_MODEL_MISMATCH`-type caveat for curation: the mouse model captures neuronal/synaptic/myelination and schizophrenia-relevant electrophysiological biology well, but does not recapitulate the full human syndromic (dysmorphic, metabolic, speech-delay) phenotype, and its relevance to the milder, more common LoF-SNV human phenotype (vs. the more severe deletion phenotype) is not yet established.

**Research applications:** The mESC model is suited to studying SRRM2's role in pluripotency/early lineage decisions; the Srrm2+/− mouse brain model is suited to studying synaptic protein regulation, oligodendrocyte/myelination biology, and neurophysiological correlates (with direct relevance to the emerging schizophrenia connection); human iPSC-neuron models allow direct validation of mouse-derived splicing findings (e.g., AGAP3) in a human cellular context.

---

## Summary for Knowledge-Base Curation

**Suggested pathophysiology causal chain:**
SRRM2 heterozygous LoF variant/deletion (MOLECULAR: GO:0003729 mRNA binding, GO:0004930-adjacent) → SRRM2/SRm300 haploinsufficiency (MOLECULAR) → disrupted nuclear speckle assembly via impaired liquid-liquid phase separation (CELLULAR: GO:0016607 nuclear speck) → genome-wide alternative pre-mRNA mis-splicing (CELLULAR: GO:0000398, e.g., AGAP3, SynGAP-γ isoform, DTX3, PCYT2) → impaired neuronal/glial (oligodendrocyte) differentiation and synaptic protein regulation (CELLULAR/TISSUE) → neurodevelopmental phenotype (developmental delay, intellectual disability, ASD/ADHD features, hypotonia) ± dysmorphic features ± obesity/hyperphagia (ORGANISM).

**Key genes/terms for curation:** hgnc:16639 (SRRM2); GO:0000398, GO:0016607, GO:0000381; CL:0000540 (neuron), CL:0000128 (oligodendrocyte); HP:0001263, HP:0000750, HP:0001256, HP:0001290, HP:0001513, HP:0000729, HP:0007018; UBERON:0000955 (brain); MONDO mapping to OMIM 620439.

**Primary citations:** Kaplanis et al. 2020 (Nature, PMID: 33057194) — gene discovery; Cuinat et al. 2022 (Genet Med, PMID: 35567594) — clinical delineation (n=22); Pagnamenta et al. 2023 (Hum Mutat, PMC11918891) — structural-variant mechanism and severe phenotype subgroup; case reports PMC12488763 (tics) and PMC11880253/Frontiers 2025 (hyperphagia-obesity, missense variant); Cell Reports 2026 (mouse Srrm2+/− brain model, schizophrenia-relevant mechanism).

---

### Sources

- [Entry - #620439 - INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 72; MRD72 - OMIM](https://omim.org/entry/620439)
- [Entry - *606032 - SERINE/ARGININE REPETITIVE MATRIX PROTEIN 2; SRRM2 - OMIM](https://omim.org/entry/606032)
- [Loss-of-function variants in SRRM2 cause a neurodevelopmental disorder - PubMed (PMID: 35567594)](https://pubmed.ncbi.nlm.nih.gov/35567594/)
- [BRIEF REPORT: Loss-of-function variants in SRRM2 cause a neurodevelopmental disorder - Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(22)00740-7/pdf)
- [Correspondence on "Loss-of-function variants in SRRM2 cause a neurodevelopmental disorder" - Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(23)00891-2/fulltext)
- [A Palindrome-Like Structure on 16p13.3 Is Associated with the Formation of Complex Structural Variations and SRRM2 Haploinsufficiency - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11918891/)
- [Neurodevelopmental disorder and juvenile-onset tics associated with microdeletion of the SRRM2 gene - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12488763/)
- [Rare SRRM2 mutation in neurodevelopmental disorders involving hyperphagia triggering severe obesity and other complications - Frontiers in Medicine](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1492851/full)
- [SRRM2 splicing factor modulates cell fate in early development - PMC (Biology Open)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11070786/)
- [Reduction of SynGAP-γ, disrupted splicing of Agap3, and oligodendrocyte deficits in Srrm2 mice, a genetic model of schizophrenia and neurodevelopmental disorder - bioRxiv](https://www.biorxiv.org/content/10.1101/2024.10.10.617460v1)
- [Srrm2 haploinsufficiency drives SynGAP-γ reduction, Agap3 mis-splicing, and oligodendrocyte deficits in a genetic mouse model of schizophrenia - Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(26)00514-0)
- [SRRM2 curation results for Dosage Sensitivity - ClinGen](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:16639)
- [SRRM2 (Intellectual disability) - Gene - PanelApp, Genomics England](https://panelapp.genomicsengland.co.uk/panels/285/gene/SRRM2/)
- [Evidence for 28 genetic disorders discovered by combining healthcare and research data - Nature (Kaplanis et al. 2020, PMID: 33057194)](https://www.nature.com/articles/s41586-020-2832-5)
- [NM_016333.4(SRRM2):c.7748_7758del (p.Thr2583fs) AND Intellectual developmental disorder, autosomal dominant 72 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV004763624/)
- [SRRM2 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SRRM2)
- [Srrm2 MGI Mouse Gene Detail - MGI:1923206](https://www.informatics.jax.org/marker/MGI:1923206)
- [Gene: SRRM2 - SFARI Gene](https://gene.sfari.org/database/human-gene/SRRM2)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.