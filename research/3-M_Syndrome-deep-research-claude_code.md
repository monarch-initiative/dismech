---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T01:41:25.028660'
end_time: '2026-08-27T01:45:22.080316'
duration_seconds: 237.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 3-M Syndrome
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
  num_turns: 17
  total_cost_usd: 1.13946
  session_id: a1f65bb8-1b49-516c-9197-25fb2b9c84dd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 20
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-M Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-M Syndrome** covering all of the
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

I now have enough sourced material to compile the full report.

I have comprehensive, well-sourced material across all required domains. Here is the complete research report.

# 3-M Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview.** 3-M syndrome (also written "3M syndrome," "Miller-McKusick-Malvaux syndrome," "Le Merrer syndrome," or "Gloomy face syndrome") is a rare autosomal recessive **primordial growth disorder** — meaning growth restriction begins prenatally and persists throughout life without a "catch-up" phase — characterized by severe pre- and postnatal growth deficiency, a distinctive facial gestalt, characteristic skeletal/radiographic findings, and normal intelligence. The name derives from the surnames of the three physicians (Miller, McKusick, Malvaux) who first described it in 1975.

**Key identifiers:**
- **OMIM:** 3M syndrome 1 (#273750, *CUL7*), 3M syndrome 2 (#612921, *OBSL1*), 3M syndrome 3 (#614205, *CCDC8*) [OMIM #273750](https://omim.org/entry/273750); [OMIM #612921](https://omim.org/entry/612921); [OMIM #614205](https://omim.org/entry/614205)
- **Orphanet:** ORPHA2616 ([Orphanet: 3M syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=2616))
- **MONDO:** MONDO:0007477 (3M syndrome 1); related MONDO terms exist per subtype
- **Disease Ontology:** DOID:0060241
- **GeneReviews:** [NBK1481](https://www.ncbi.nlm.nih.gov/books/NBK1481/) (Cormier-Daire, Huber, et al., updated periodically)
- **GTR/MeSH/ICD:** Listed under primordial dwarfism / short stature syndromes; no dedicated ICD-10-CM code beyond the general short-stature syndrome category

**Synonyms:** 3M syndrome; Miller-McKusick-Malvaux syndrome; Le Merrer syndrome; Gloomy face syndrome (historical, now discouraged); Dolichospondylic dysplasia; Yakut short stature syndrome (population-specific CUL7 founder-variant form).

**Data derivation:** Information is drawn predominantly from **aggregated case-series/cohort literature** (fewer than ~250 molecularly confirmed cases reported worldwide as of 2025) rather than large-scale EHR/registry data, reflecting the disorder's rarity. GeneReviews and the recent 2025 natural-history literature review (217 pooled cases from 36 publications) are the most authoritative aggregate sources.

---

## 2. Etiology

**Disease causal factors — genetic.** 3-M syndrome is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants** in one of three genes encoding components of a single molecular complex:

| Subtype | OMIM | Gene | Locus | Approx. proportion of cases |
|---|---|---|---|---|
| 3M1 | #273750 | *CUL7* (Cullin-7) | 6p21.1 | ~65–75% |
| 3M2 | #612921 | *OBSL1* (Obscurin-like 1) | 2q35 | ~28–34% |
| 3M3 | #614205 | *CCDC8* (Coiled-coil domain containing 8) | 19q13.32 | ~1–5% |

Approximately 1% of clinically diagnosed cases remain molecularly unresolved, suggesting additional causative genes or loci may exist ([GeneReviews NBK1481](https://www.ncbi.nlm.nih.gov/books/NBK1481/)).

- **CUL7** variants: predominance of null variants (nonsense, splice-site; missense also frequent); ~50% of pathogenic variants localize to the cullin domain critical for ROC1 anchoring.
- **OBSL1** variants: most pathogenic variants occur within the first 8 exons, affecting all known isoforms, predominantly loss-of-function.
- **CCDC8**: a single-exon gene; pathogenic variants lead to truncation and loss of function.

**Founder variants (population-specific risk factors):**
- **Yakut population (Siberia):** *CUL7* c.4581dupT (also reported as 4582_4583insT), described by Maksimova et al. 2007, associated with a distinctive phenotype of high neonatal respiratory distress but comparatively few bone abnormalities ([PMC2652813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2652813/)).
- **Maghrebian/Tunisian population:** *CUL7* c.4451_4452delTG.
- **Turkish population:** *OBSL1* c.1273dupA (emerging founder variant).

**Risk factors:**
- **Genetic:** Consanguinity substantially raises risk given the autosomal recessive inheritance and regional founder alleles; carrier parents (heterozygotes) are asymptomatic.
- **Environmental:** No environmental, toxin, infectious, or lifestyle risk factors have been identified — this is a purely monogenic Mendelian disorder.
- **Modifier genes:** None formally established, though phenotypic variability (e.g., milder stature in CCDC8-related disease vs. more severe in CUL7-related disease) suggests gene-specific and possibly allele-specific modulation of severity.

**Protective factors:** None described; this is a fully penetrant recessive disorder once biallelic pathogenic variants are present.

**Gene-environment interactions:** Not applicable/not reported — no environmental modifiers of penetrance or expressivity have been documented in the literature.

---

## 3. Phenotypes

### Growth phenotype
- **Severe pre- and postnatal growth deficiency**: final adult height typically ~5 SD below the mean (range roughly 115–150 cm in adults). Birth length typically 40–42 cm with **normal head circumference for gestational age** (giving the appearance of relative macrocephaly).
- No catch-up growth occurs; short stature is proportionate. HPO: **HP:0004322** (Short stature), **HP:0001511** (Intrauterine growth retardation).

### Craniofacial features
Characteristic facies including: relative macrocephaly (HP:0004482 / HP:0000256 macrocephaly-adjacent terms), dolichocephaly (HP:0000268), triangular face (HP:0000325), midface retrusion (HP:0011800), thick eyebrows (HP:0000574), fleshy/bulbous nasal tip (HP:0000455-adjacent), long philtrum (HP:0000343), thick vermilion of upper and lower lips (HP:0012471), pointed chin (HP:0000307). Infants may show facial nevus simplex and infraorbital fullness that fade with age. Facial appearance is most diagnostic in **infancy** and becomes progressively subtler through childhood into adolescence, per a 2025 natural-history review of 217 cases (Ital J Pediatr, PMID 41437277, DOI 10.1186/s13052-025-02172-8).

### Musculoskeletal features
Short broad neck, prominent trapezii, pectus carinatum/excavatum (HP:0000768/HP:0000767), short thorax, square shoulders, winged scapulae, thoracic kyphoscoliosis (HP:0002751), **hyperlordosis** (HP:0002938), spina bifida occulta, clinodactyly of the fifth finger (HP:0004209), **joint hypermobility** (HP:0001382), hip dislocation, prominent heels, pes planus (HP:0001763).

### Radiographic (skeletal) hallmark features
- **Slender long bones** with diaphyseal constriction and flared metaphyses — the primary distinguishing radiologic sign.
- **Tall vertebral bodies** with reduced anteroposterior and transverse diameters, especially lumbar.
- Elevated metacarpal and vertebral indices.
- Small pelvic bones.
These become "increasingly vague" with age, per the 2025 natural-history review, so radiographic diagnosis is most reliable in infancy.

### Neurodevelopmental
**Normal intelligence** is a defining and diagnostically important feature that distinguishes 3-M syndrome from many other severe short-stature/primordial-dwarfism syndromes (e.g., Seckel syndrome, microcephalic primordial dwarfism).

### Endocrine/reproductive
Males may have **hypogonadism** and occasionally **hypospadias** (HP:0000047); a 2024 JCEM Case Reports paper documented a CUL7-variant male with bifid scrotum and perineal hypospadias at birth, spontaneous but incomplete pubertal maturation, and progressive **gonadal failure** in adolescence (declining testicular volume, rising gonadotropins, low-normal testosterone) (PMID 38847008, [PMC11154130](https://pmc.ncbi.nlm.nih.gov/articles/PMC11154130/)). Female gonadal function appears normal. Endocrine (thyroid, adrenal) function is otherwise generally normal.

### Cardiac
Aortic root dilatation reported in some individuals — a rationale for periodic echocardiographic surveillance.

### Respiratory
Some neonates, particularly in the Yakut founder-variant population, experience significant **neonatal respiratory distress** (~41% in that population), sometimes requiring NICU care.

### Quality of life
Not formally quantified with standardized instruments (EQ-5D/SF-36) in the literature reviewed; qualitatively, impact centers on short-stature-related psychosocial and functional issues (adaptive equipment needs, orthopedic complications) rather than cognitive/behavioral burden, since intelligence and daily function are largely preserved.

---

## 4. Genetic/Molecular Information

**Causal genes:** *CUL7* (HGNC:16290, OMIM *609577), *OBSL1* (HGNC:15738, OMIM *610991), *CCDC8* (HGNC:17086, OMIM *614145).

**Pathogenic variant classification:** Per ACMG/AMP framework, disease-causing alleles are classified as **pathogenic/likely pathogenic** biallelic loss-of-function or damaging missense variants; heterozygous carriers are unaffected. ClinVar/ClinGen entries exist for known recurrent and founder variants.

**Variant types:**
- Nonsense, frameshift, and canonical splice-site variants predominate for *CUL7* and *OBSL1* (loss-of-function mechanism).
- Missense variants also occur in *CUL7*, frequently clustering in the cullin domain required for ROC1 (RBX1) anchoring within the SCF-like complex.
- *CCDC8*, being single-exon, is disrupted almost exclusively by truncating variants causing loss of function.

**Allele frequency:** No individual pathogenic variant reaches appreciable frequency in general population databases (gnomAD) outside specific founder populations (Yakut, Maghrebian/Tunisian, Turkish), consistent with an ultra-rare recessive disorder.

**Origin:** Germline, biallelic — not somatic; both alleles inherited from heterozygous, unaffected parents (or occasionally uniparental disomy/de novo events, though these are not prominently reported for this condition).

**Functional consequence — molecular mechanism:**
CUL7 is a member of the Cullin family and forms the scaffold of an **SCF-like (Skp1–Cullin–F-box) E3 ubiquitin ligase complex** localized to the Golgi apparatus. This complex:
- Physically interacts with **OBSL1** and **CCDC8** to form the "**3-M E3 complex**," which regulates microtubule dynamics and ubiquitinates the membrane-associated protein **LL5β**, impacting cell migration and cytoskeletal regulation (Hanson et al. 2009, *Am J Hum Genet*, [PMC2694976](https://ncbi.nlm.nih.gov/pmc/articles/PMC2694976); PMID 19481195).
- Is implicated in proteasomal degradation of **IRS-1** (insulin receptor substrate-1) and **cyclin D1**. CUL7 interacts with IRS-1, a downstream signaling node shared by insulin, IGF-1, and GH receptor pathways. Loss of CUL7 function leads to IRS-1 accumulation (impaired proteasomal turnover), and downstream **reduced IGF-1-mediated activation of Akt** and reduced cell proliferation ([Endocrine Abstracts EA0021P232](https://www.endocrine-abstracts.org/ea/0021/ea0021p232)).
- Loss of CUL7 also reduces *OBSL1* transcription, tying the three genes into a single interdependent pathway — consistent with all three genes producing a convergent, largely indistinguishable phenotype (CUL7- and OBSL1-related disease are "clinically and radiographically indistinguishable," per GeneReviews, though CUL7-related disease tends to produce shorter final stature).
- A separate mechanistic axis: 3-M fibroblasts show an epigenetic gene-expression signature of **reduced IGF2 expression and increased H19 expression**, resembling the imprinting profile of Silver-Russell syndrome, with markedly reduced IGF-II secretion in conditioned culture medium (10.2±2.9 ng/mL control vs. 0.6±0.9 ng/mL 3-M fibroblasts, P<0.01) — implicating **IGF2 silencing** as a contributing, gene-network-level (not primary genetic-imprinting) mechanism (Meyer et al. 2013, *Endocr Connect*, PMID 24148222, [PMC3847915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3847915/)).

**Modifier genes:** None formally established; phenotype-genotype correlation is largely gene-specific (CUL7 > OBSL1 > CCDC8 severity gradient) rather than driven by known secondary modifiers.

**Epigenetic information:** The IGF2/H19 imprinting-like expression signature above is the principal epigenetic finding; it appears to be a downstream transcriptional consequence of E3-complex disruption rather than a primary imprinting defect.

**Chromosomal abnormalities:** 3-M syndrome is not caused by large structural chromosomal rearrangements; it is a single-gene (biallelic small-variant) disorder. No characteristic CNV/translocation etiology has been reported.

---

## 5. Environmental Information

3-M syndrome is a monogenic Mendelian disorder with **no identified environmental, toxin, infectious, or lifestyle contributing factors**. It is not associated with teratogen exposure, maternal illness, or infectious triggers. The only population-level "risk factor" beyond genetics is **consanguinity**, which increases the probability of biallelic inheritance of a rare recessive allele, and geographic/ethnic founder-variant enrichment (Yakut, Maghrebian, Turkish populations).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function variant in *CUL7*, *OBSL1*, or *CCDC8* → loss of function of one component of the Golgi-localized 3-M E3 ubiquitin ligase complex.
2. **Complex disruption:** CUL7, OBSL1, and CCDC8 normally physically interact to form the joint 3-M E3 complex, which is critical for **microtubule regulation** and ubiquitination of the membrane-associated protein **LL5β** (cell migration regulator). Loss of any one component destabilizes the complex.
3. **Impaired proteostasis of growth-signaling intermediates:** Failure of ubiquitin-mediated proteasomal degradation of **IRS-1** (and cyclin D1) → IRS-1 accumulation.
4. **Blunted IGF-1/insulin/GH signal transduction:** Because IRS-1 is a shared downstream node of insulin, IGF-1, and GH receptor pathways, its dysregulated turnover produces **reduced IGF-1-mediated Akt activation** and reduced cellular proliferative response to growth-factor stimulation.
5. **Cell-cycle/cytoskeletal defects:** Mitotic and cytokinesis abnormalities from loss of CUL7 function are proposed contributors to short stature; reduced *OBSL1* transcription follows loss of CUL7, reinforcing pathway interdependence.
6. **Epigenetic-level convergence:** A gene-expression signature of reduced IGF2 and elevated H19 (Silver-Russell-like) further suppresses IGF-II bioavailability, compounding the growth-signaling deficit.
7. **Tissue-level consequence — growth plate dysfunction:** Cartilage-specific *Cul7* knockout mice show abnormally short/deformed limbs, thickened growth plates, disorganized chondrocyte columns, decreased proliferative-zone cell numbers, and disordered trabecular bone at the metaphysis — implicating both **chondrocyte proliferation defects** and disrupted **endochondral ossification** as the proximate tissue mechanism of skeletal growth failure (Longitudinal skeletal growth study, PMID 38367951, *ScienceDirect*).
8. **Organism-level phenotype:** Severe proportionate pre-/postnatal growth restriction, characteristic facial dysmorphism, skeletal (long-bone/vertebral) abnormalities, and (in a subset) gonadal, cardiac, and respiratory involvement, with sparing of cognitive development.

**Molecular pathways involved:** Ubiquitin-proteasome system (SCF/Cullin-RING E3 ligase pathway); insulin/IGF-1/GH-IRS1-Akt signaling axis; microtubule/cytoskeletal regulation via LL5β.

**Cellular processes:** Impaired cell proliferation, disrupted mitosis/cytokinesis, altered cell migration (cytoskeletal), disrupted chondrocyte proliferation and endochondral ossification.

**Protein dysfunction:** Loss-of-function of CUL7 (scaffold protein of Golgi-localized E3 ligase), OBSL1 (cytoskeletal adaptor), CCDC8 (coiled-coil complex partner); consequent failure of substrate (IRS-1, cyclin D1, LL5β) ubiquitination/degradation.

**Suggested ontology terms:**
- **GO (biological process):** GO:0016567 (protein ubiquitination), GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0043410 (positive regulation of MAPK cascade)/IGF signaling-related terms, GO:0001501 (skeletal system development), GO:0060350 (endochondral bone morphogenesis)
- **GO (molecular function):** GO:0031625 (ubiquitin protein ligase binding), GO:0004842 (ubiquitin-protein transferase activity)
- **CL (cell types):** CL:0000138 (chondrocyte), CL:0000057 (fibroblast, used in in vitro studies)
- **UBERON:** UBERON:0002102 (growth plate cartilage), UBERON:0001474 (bone element)

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Skeletal system** (primary): long bones, vertebral column, pelvis, ribs, hands/feet — UBERON:0001434 (skeletal system)
- **Craniofacial skeleton and soft tissue**: skull shape, facial structure — UBERON:0000033 (head)
- **Reproductive system** (males): testes, scrotum, penile/urethral development (hypospadias) — UBERON:0000473 (testis)
- **Cardiovascular system**: aortic root — UBERON:0002049 (aorta)
- **Respiratory system**: neonatal lung maturation/distress in some populations — UBERON:0002048 (lung)
- **CNS**: spared (normal intelligence)

**Tissue/cell level:** Growth plate chondrocytes (proliferative zone), cortical/trabecular bone, dermal fibroblasts (used for functional IGF2/H19 studies), Golgi-associated cellular machinery broadly (since CUL7 localizes to the Golgi apparatus).

**Subcellular level:** Golgi apparatus (site of the 3-M E3 ligase complex) — GO:0005794 (Golgi apparatus); microtubule cytoskeleton — GO:0005874 (microtubule); ubiquitin-proteasome machinery — GO:0000502 (proteasome complex).

**Localization/laterality:** Findings are generally **bilateral and symmetric** (proportionate short stature, symmetric limb involvement) — this symmetry is a key differentiator from Silver-Russell syndrome, which classically shows limb-length asymmetry.

---

## 8. Temporal Development

**Onset:** Prenatal — intrauterine growth restriction is evident before birth (low birth weight/length with normal-for-age head circumference), making this a **primordial** (prenatal-onset) growth disorder rather than a postnatal-onset condition.

**Progression:** Persistent, non-progressive, lifelong short stature without catch-up growth. The disorder is generally **stable** rather than degenerative — final adult height is reached without further mechanistic deterioration, though secondary orthopedic (kyphoscoliosis, joint laxity) and endocrine (pubertal, gonadal) complications can evolve over time.

**Phenotype evolution with age** (per the 2025 natural-history review of 217 cases, PMID 41437277):
- **Infancy** is the period of clearest diagnostic signal — short length/thorax, protuberant abdomen, prominent heels, bulbous/fleshy nasal tip, and the most distinct radiographic long-bone/vertebral findings.
- **Childhood through adolescence**: most dysmorphic and radiographic features progressively attenuate/become "increasingly vague"; short stature and the characteristic nasal appearance persist as the most durable diagnostic clues.
- **Puberty/adulthood**: some males show initially normal pubertal onset followed by **secondary (progressive) gonadal failure** in adolescence/young adulthood (declining testicular volume, rising gonadotropins) — a later-emerging, evolving feature rather than a static congenital one.

**Critical periods:** Infancy/early childhood is the critical window for clinical/radiographic diagnosis and for initiating growth hormone trials, given diminishing diagnostic specificity of physical signs with age.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Not formally established; **fewer than ~250 molecularly confirmed cases** reported in the literature worldwide since the first description in 1975 ([GeneReviews NBK1481](https://www.ncbi.nlm.nih.gov/books/NBK1481/)); Orphanet lists it as "very rare" with prevalence unknown/<1/1,000,000.
- **Incidence:** Not reported at a population level (too rare for standard surveillance-based incidence estimation).

**Inheritance pattern:** **Autosomal recessive** for all three subtypes (3M1/*CUL7*, 3M2/*OBSL1*, 3M3/*CCDC8*). Sibling recurrence risk when both parents are carriers: 25% affected, 50% carrier, 25% unaffected/non-carrier.

**Penetrance:** Complete (biallelic pathogenic variants are consistently associated with the phenotype).

**Expressivity:** Variable — facial/skeletal severity and final height vary by gene (CUL7 generally associated with the shortest stature; CCDC8-related disease tends to be milder with relatively higher final height) and to some extent by specific allele (e.g., the Yakut *CUL7* founder variant produces a distinct sub-phenotype with high neonatal respiratory distress but comparatively fewer bone abnormalities).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the reviewed literature, though standard recessive-disorder recurrence counseling applies.

**Founder effects:**
- **Yakut (Sakha) population, Siberia:** *CUL7* c.4581dupT — described in 43 affected individuals (Maksimova et al. 2007, [PMC2652813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2652813/)); associated with high neonatal respiratory distress (~41%) and fewer skeletal anomalies than typical CUL7-related disease.
- **Maghrebian/Tunisian population:** *CUL7* c.4451_4452delTG.
- **Turkish population:** *OBSL1* c.1273dupA (emerging founder allele).

**Consanguinity role:** Strongly associated with increased case frequency, as expected for an ultra-rare autosomal recessive disorder; many reported cohorts (e.g., recent Chinese and Middle Eastern case series) note parental consanguinity.

**Carrier frequency:** Not established at a population level outside founder populations.

**Population demographics:** Reported cases span diverse ethnic groups (European, Middle Eastern/Maghrebian, East Asian [Chinese, Japanese], Siberian/Yakut, Turkish), consistent with panethnic occurrence with regional founder-variant clustering. No formal sex-ratio skew is reported (autosomal recessive, so no inherent sex bias, aside from male-specific gonadal manifestations being clinically more apparent in males).

---

## 10. Diagnostics

**Diagnostic criteria (GeneReviews):** Diagnosis established in a proband with **prenatal-onset persistent growth deficiency** plus characteristic clinical and radiographic features, **and/or** identification of biallelic pathogenic variants in *CCDC8*, *CUL7*, or *OBSL1* by molecular genetic testing. No formally published consensus clinical scoring criteria exist.

**Clinical tests:**
- **Imaging:** Skeletal radiographic survey — long bones (slender diaphyses, flared metaphyses), spine (tall vertebral bodies), pelvis (small pelvic bones); echocardiography for aortic root assessment.
- **Laboratory:** IGF-1 levels (monitored during GH trials); gonadotropin/testosterone panel in pubertal/adult males for hypogonadism surveillance.
- **Prenatal ultrasound:** Short long bones and other skeletal findings can be detected as early as 24 weeks' gestation, though findings are not pathognomonic on their own.

**Genetic testing:**
- Recommended approach: **multigene panel** covering *CUL7*, *OBSL1*, *CCDC8* (and relevant differential-diagnosis genes), or **exome/genome sequencing** given phenotypic overlap with other growth-restriction syndromes.
- Single-gene sequential testing (starting with *CUL7*, the most frequently implicated gene) is an alternative in resource-limited settings or when a founder variant is suspected by ancestry.
- Prenatal and **preimplantation genetic testing** are available once familial pathogenic variants are identified (demonstrated in a 2023 Chinese family case, [PMC10767403](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767403/)).

**Clinical criteria / differential diagnosis** (per GeneReviews):
- **Silver-Russell syndrome:** often shows limb-length asymmetry and relative macrocephaly at birth; lacks the classic 3-M long-bone/vertebral radiologic signature; notably, 3-M syndrome shares an IGF2/H19 expression signature with SRS at the molecular level despite distinct genetic causes.
- **Mulibrey nanism:** less severe IUGR; distinct facial gestalt (high forehead, "pseudohydrocephalic" skull).
- **IGF1R haploinsufficiency/deficiency:** microcephaly and intellectual disability common in severe cases (contrasts with normal head size/intelligence in 3-M).
- **Dubowitz syndrome:** microcephaly, eczema, intellectual disability.
- **Fetal alcohol syndrome:** acquired, with microcephaly and nail hypoplasia — important to exclude given overlapping growth restriction/facial features.

**Screening:** No population-based newborn screening program exists (disorder too rare and non-treatable via early biochemical intervention); diagnosis is clinically/radiographically or genetically triggered rather than screened.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** **Life expectancy is generally normal.** No characteristic disease-specific mortality has been documented outside of population-specific neonatal respiratory distress risk (e.g., Yakut founder variant) and rare complete-knockout-lethal equivalents in constitutive animal models (not applicable to human heterozygous-viable genotypes, since humans with the disease are, by definition, live-born survivors of hypomorphic/partial-loss-of-function alleles).
- **Morbidity:** Primarily orthopedic (kyphoscoliosis, hip dysplasia/dislocation, joint hypermobility-related complications, potential early arthritis), endocrine (progressive gonadal failure in some males), and cardiovascular (aortic root dilatation) morbidity, layered onto lifelong short stature.
- **Cognitive/functional outcome:** **Normal intelligence** and generally preserved functional independence, distinguishing 3-M syndrome prognostically from many other severe growth-restriction syndromes.
- **Complications:** Neonatal respiratory distress (population-dependent), hip dislocation, scoliosis, joint laxity/early arthritis risk, hypospadias (surgical correction), progressive hypogonadism in some males, aortic root dilation.
- **Prognostic factors:** Causal gene (CUL7 > OBSL1 > CCDC8 in terms of severity/short stature), specific founder variant (e.g., Yakut variant → higher respiratory risk), and timing/response to growth hormone trial.
- **Recovery potential:** Height deficit is not "recovered" — it is a fixed, non-progressive trait once adult stature is reached; management is supportive/adaptive rather than curative.

---

## 12. Treatment

**Pharmacotherapy — Growth hormone (GH):**
- Standard of care approach: **referral to pediatric endocrinology for a trial of recombinant human growth hormone**, particularly in prepubertal children, with close monitoring of growth velocity and IGF-1 levels.
- Response is **variable**: some children show meaningful improvement in growth velocity; others show poor response. A well-documented case (novel CUL7 mutation, associated with neonatal respiratory distress) showed a **good response to GH therapy** (PMID from [PMC4418346](https://pmc.ncbi.nlm.nih.gov/articles/PMC4418346/), *Endocrinol Diabetes Metab Case Rep*); another 18-year follow-up case documented 3-M syndrome co-occurring with **growth hormone deficiency** responding to treatment ([PMC3608257](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3608257/), *Ital J Pediatr* 2013).
- One reported individual with CUL7-related disease treated with **recombinant human IGF-1** showed a poor response and significant side effects — IGF-1 therapy is not generally favored.
- NCIT term: `NCIT:C15986` (Pharmacotherapy) as the general treatment_term, with growth hormone as `therapeutic_agent` (e.g., somatropin, CHEBI-bindable).

**Surgical/interventional:**
- **Orthopedic surgery** for hip dysplasia/dislocation and progressive kyphoscoliosis (NCIT:C16186, Orthopedic Surgical Procedure).
- **Surgical limb lengthening** is an option for selected patients seeking increased stature (NCIT:C15329, Surgical Procedure).
- **Urological surgery** for hypospadias correction in affected males (NCIT:C15329).

**Supportive/rehabilitative:**
- **Physical therapy** (NCIT:C15302) and **occupational therapy** to maximize function and address joint hypermobility/adaptive needs.
- Environmental/community adaptations (adaptive equipment, community child-health services) for short stature.

**Endocrine management:** Monitoring and, where indicated, hormone replacement for males with progressive hypogonadism (testosterone/gonadotropin-guided management by endocrinology).

**Surveillance/monitoring protocol** (from GeneReviews):

| System | Evaluation | Suggested frequency |
|---|---|---|
| Growth | Growth chart/velocity | Every 6–12 months |
| Musculoskeletal | Joint hypermobility, kyphoscoliosis assessment | Annually |
| Hip | Dislocation screening | Each visit in infancy, especially if walking delayed |
| Cardiac | Echocardiogram (aortic root) | Consider in adolescence |

**Experimental/investigational:** No gene therapy, RNA-based therapy, or targeted molecular therapy has been developed or trialed for 3-M syndrome; management remains supportive/symptomatic rather than mechanism-targeted, reflecting the structural (ubiquitin-ligase complex assembly) nature of the defect, which is not straightforwardly druggable. No relevant ClinicalTrials.gov interventional trials specific to 3-M syndrome were identified in this search.

**Treatment outcomes / adverse events:** GH therapy is generally well tolerated in the reported cases with variable efficacy; IGF-1 therapy in the one reported case caused significant side effects with poor efficacy.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause); the only "primary prevention" lever is **reproductive/genetic counseling** for known carrier couples, particularly in consanguineous unions or founder-variant populations (Yakut, Maghrebian, Turkish).
- **Secondary prevention (early detection):** Prenatal ultrasound surveillance (skeletal findings detectable from ~24 weeks in at-risk pregnancies) and, where familial variants are known, **prenatal diagnosis and preimplantation genetic testing (PGT)** — demonstrated in a 2023 Chinese family case using novel biallelic *CUL7* variants ([PMC10767403](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767403/)).
- **Genetic counseling:** Central to prevention/family planning — carrier detection in relatives once the familial variant(s) are known; counseling on the 25% recurrence risk for future pregnancies of carrier couples; sibling evaluation for undiagnosed short stature.
- **Screening programs:** No population-based newborn or carrier screening program exists given extreme rarity, though targeted carrier screening is reasonable in founder populations with known high local carrier frequency.
- **Tertiary prevention:** Surveillance protocol above (orthopedic, cardiac, endocrine) aims to prevent/mitigate secondary complications (scoliosis progression, hip damage, aortic complications, missed hypogonadism) rather than the primary disease process.

---

## 14. Other Species / Natural Disease

**Naturally occurring veterinary disease:**
- **Sheep (Ovis aries):** A recessively inherited disorder in Australian Poll Merino/Merino sheep called **Brachygnathia, Cardiomegaly and Renal Hypoplasia Syndrome (BCRHS)** was found to be caused by a frameshift variant in **OBSL1** (p.(Val573Trpfs*119)), representing a naturally occurring **ovine model of human 3M syndrome-2**. Identification enabled improved breeding management of the affected flock via carrier detection ([BMC Genomic Data 2020](https://link.springer.com/article/10.1186/s12863-020-00913-8); OMIA:001595-9940, "Growth disorder, syndromic, OBSL1-related," in *Ovis aries*).

**Comparative biology / model organisms:**
- **Mouse (*Mus musculus*), Cul7 knockout:** Constitutive *Cul7−/−* mice are **perinatal lethal** — severe growth retardation in late gestation and respiratory distress after birth; some models show abnormal bone mineralization, decreased body weight, and reduced bone mineral density; others show severe fetal growth restriction and perinatal death (multiple studies cited in PMC10423707 background). To circumvent lethality, a **cartilage-specific conditional knockout** (*Cul7^fl/fl;Col2a1-CreERT2*) was generated: these mice show short/deformed limbs, thickened growth plates, disorganized proliferative-zone chondrocyte columns, and disordered metaphyseal trabecular bone — implicating defective chondrocyte proliferation and endochondral ossification (PMID 38367951, *ScienceDirect*, "Longitudinal skeletal growth and growth plate morphological characteristics of chondro-tissue specific CUL7 knockout mice").
- **Mouse, CCDC8 knockout:** A 2023 study (Molecular Biomedicine, PMID 37574524, [PMC10423707](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423707/)) established a *Ccdc8−/−* mouse model; knockout was **highly lethal** (only 4 live-born knockouts from 410 mice bred, <1% success rate), with placental developmental disorder, intrauterine growth retardation, intrauterine death, and perinatal death closely paralleling *Cul7* knockout embryo phenotypes — supporting the shared-pathway model of CUL7/OBSL1/CCDC8 function.
- **OBSL1 knockout studies** (Hanson et al. 2009, [PMC2694976](https://ncbi.nlm.nih.gov/pmc/articles/PMC2694976)) established the direct physical and functional link between OBSL1 and the CUL7-containing E3 ligase complex, foundational to the current mechanistic model.

**Cross-species relevance:** These animal models (sheep OBSL1, mouse Cul7/Ccdc8) confirm cross-species conservation of the 3-M E3 complex's essential role in fetal/perinatal growth and support their use for mechanistic and (potentially) therapeutic research, though the severe perinatal lethality of constitutive knockouts limits their use to conditional/tissue-specific systems for postnatal phenotyping.

**Zoonotic potential:** None — this is a purely genetic (non-infectious) disorder; no transmission risk.

---

## 15. Model Organisms

| Model | Type | Key features | Reference |
|---|---|---|---|
| *Cul7−/−* mouse (constitutive) | Genetic knockout, mammalian | Perinatal lethal; late-gestation growth retardation, respiratory distress at birth; some lines show abnormal bone mineralization and reduced BMD | Cited in PMC10423707 background |
| *Cul7^fl/fl;Col2a1-CreERT2* mouse | Conditional/tissue-specific (cartilage) knockout | Short/deformed limbs, thickened growth plate, disorganized proliferative chondrocytes, disordered metaphyseal trabecular bone; viable, enabling postnatal skeletal phenotyping | PMID 38367951 |
| *Ccdc8−/−* mouse | Constitutive knockout | Highly lethal (<1% live-birth rate of homozygotes); placental defects, IUGR, intrauterine/perinatal death mirroring Cul7 knockouts | PMID 37574524 / [PMC10423707](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423707/) |
| Merino/Poll Merino sheep, OBSL1 frameshift | Naturally occurring animal model | BCRHS: brachygnathia, cardiomegaly, renal hypoplasia; ovine model of human 3M syndrome-2; enabled breeding-based carrier management | [BMC Genomic Data 2020](https://link.springer.com/article/10.1186/s12863-020-00913-8) / OMIA:001595-9940 |
| Human dermal fibroblasts (patient-derived) | Cellular/in vitro | Reduced IGF2 expression, increased H19 expression, reduced IGF-II secretion vs. controls; used to demonstrate the IGF2-silencing mechanism | PMID 24148222 |

**Applications:** These models collectively support study of (a) the shared CUL7-OBSL1-CCDC8 E3-ligase-complex biology, (b) chondrocyte/growth-plate-specific consequences of complex loss, (c) placental/perinatal growth-restriction mechanisms, and (d) potential future therapeutic-target validation (e.g., IGF-1/Akt pathway modulation), though no model has yet been used for interventional (drug) testing specific to 3-M syndrome in the literature surveyed.

**Model limitations:** Constitutive knockouts in mouse (*Cul7*, *Ccdc8*) are embryonic/perinatal lethal and thus **do not recapitulate the live-born, postnatal phenotype** seen in humans (who carry hypomorphic/partial-loss-of-function alleles rather than complete null states compatible only with lethality) — a clear **human-model mismatch**: conditional/tissue-specific knockouts were required to generate a viable, phenotypically informative postnatal model. The sheep OBSL1 model, by contrast, is a naturally occurring, viable (in appropriate genotype/zygosity) large-animal model that may better approximate the human postnatal skeletal phenotype, though comparative fidelity has not been formally characterized against the human 3-M radiographic signature.

---

## Summary Table: Suggested Ontology Bindings

| Category | Term |
|---|---|
| Disease | MONDO:0007477 (3M syndrome 1); OMIM #273750/#612921/#614205; ORPHA:2616 |
| Genes | hgnc CUL7, hgnc OBSL1, hgnc CCDC8 (verify current HGNC IDs before curation) |
| Phenotypes (HP) | HP:0004322 Short stature; HP:0001511 IUGR; HP:0002938 Hyperlordosis; HP:0001382 Joint hypermobility; HP:0002751 Kyphoscoliosis; HP:0000047 Hypospadias; HP:0000268 Dolichocephaly; HP:0011800 Midface retrusion |
| GO (BP) | GO:0016567 protein ubiquitination; GO:0060350 endochondral bone morphogenesis |
| GO (CC) | GO:0005794 Golgi apparatus |
| CL | CL:0000138 chondrocyte |
| UBERON | UBERON:0002102 growth plate cartilage |
| NCIT (treatment) | NCIT:C15986 Pharmacotherapy (GH); NCIT:C16186 Orthopedic Surgical Procedure; NCIT:C15302 Physical Therapy |

---

## Sources

- [3-M Syndrome – GeneReviews (NBK1481)](https://www.ncbi.nlm.nih.gov/books/NBK1481/)
- [OMIM #273750 – THREE M SYNDROME 1](https://omim.org/entry/273750)
- [OMIM #612921 – THREE M SYNDROME 2](https://omim.org/entry/612921)
- [OMIM #614205 – THREE M SYNDROME 3](https://omim.org/entry/614205)
- [Orphanet: 3M syndrome (ORPHA2616)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=2616)
- [NORD: Three M Syndrome](https://rarediseases.org/rare-diseases/three-m-syndrome/)
- Hanson D et al., "The Primordial Growth Disorder 3-M Syndrome Connects Ubiquitination to the Cytoskeletal Adaptor OBSL1," Am J Hum Genet 2009, PMID 19481195 — [PMC2694976](https://ncbi.nlm.nih.gov/pmc/articles/PMC2694976)
- Meyer R et al., "3-M syndrome: a growth disorder associated with IGF2 silencing," Endocr Connect 2013, PMID 24148222 — [PMC3847915](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3847915/)
- Maksimova N et al., "Clinical, molecular and histopathological features of short stature syndrome with novel CUL7 mutation in Yakuts," 2007 — [PMC2652813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2652813/)
- "3-M syndrome: evolution of the phenotype over time," Ital J Pediatr, Dec 2025, PMID 41437277, DOI 10.1186/s13052-025-02172-8 — [PMC12838503](https://pmc.ncbi.nlm.nih.gov/articles/PMC12838503/)
- "Establishment of the 3M syndrome animal model in CCDC8 knockout mice," Mol Biomed 2023, PMID 37574524 — [PMC10423707](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423707/)
- "Longitudinal skeletal growth and growth plate morphological characteristics of chondro-tissue specific CUL7 knockout mice," PMID 38367951 — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0940960224000165)
- "Molecular basis of a new ovine model for human 3M syndrome-2," BMC Genomic Data 2020 — [Springer](https://link.springer.com/article/10.1186/s12863-020-00913-8); [PMC7493961](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7493961/)
- Aldhoon-Hainerová I et al., "Gonadal Failure in a Male With 3-M Syndrome," JCEM Case Rep 2024, PMID 38847008 — [PMC11154130](https://pmc.ncbi.nlm.nih.gov/articles/PMC11154130/)
- "Chinese patients with 3M syndrome: clinical manifestations and two novel pathogenic variants," Front Genet 2023 — [Frontiers](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1164936/full)
- "3-M syndrome: a novel CUL7 mutation associated with respiratory distress and a good response to GH therapy" — [PMC4418346](https://pmc.ncbi.nlm.nih.gov/articles/PMC4418346/)
- "3-M syndrome associated with growth hormone deficiency: 18 year follow-up of a patient," Ital J Pediatr 2013 — [PMC3608257](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3608257/)
- "Prenatal diagnosis and preimplantation genetics testing of 3M syndrome in a Chinese family with novel biallelic variants of CUL7" — [PMC10767403](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767403/)
- Society for Endocrinology, "Loss of the Golgi localised E3 ubiquitin ligase containing Cullin 7 in 3-M syndrome leads to reduced cell proliferation and reduced IGF1 mediated activation of Akt" — [Endocrine Abstracts](https://www.endocrine-abstracts.org/ea/0021/ea0021p232)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.
