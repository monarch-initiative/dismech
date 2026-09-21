---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T16:32:00.060831'
end_time: '2026-08-24T16:36:34.980030'
duration_seconds: 274.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar Ataxia Type 23
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
  num_turns: 27
  total_cost_usd: 1.6288818
  session_id: d5430dc8-cc9c-5a8f-9365-64cb735827c4
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 23
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 23** covering all of the
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

# Spinocerebellar Ataxia Type 23 (SCA23): Comprehensive Research Report

## 1. Disease Information

**Overview.** Spinocerebellar ataxia type 23 (SCA23) is a rare, adult/late-onset, autosomal dominant neurodegenerative disorder belonging to type I autosomal dominant cerebellar ataxia (ADCA type I). It is characterized by slowly progressive gait and limb ataxia, dysarthria, slowed saccades, ocular dysmetria, hyperreflexia and extensor plantar (Babinski) responses, with variable additional features such as peripheral neuropathy ([OMIM #610245](https://omim.org/entry/610245); [Orphanet ORPHA101108](https://www.orpha.net/en/disease/detail/101108)). The disease was first mapped as a distinct genetic locus in a large Dutch family in 2004 and the causal gene, *PDYN* (prodynorphin), was identified in 2010.

**Key identifiers:**
- **OMIM:** #610245 (phenotype, SCA23); *131340 (gene, PDYN)
- **Orphanet:** ORPHA101108
- **MONDO:** MONDO:0012449 (autosomal dominant SCA23; distinct from MONDO:0014846, the unrelated autosomal-recessive SCA23/SCAR23 caused by *TDP2*, chromosome 6p22.3 — a name collision curators must not conflate)
- **Disease Ontology:** DOID:0050973
- **Gene:** HGNC symbol PDYN (HGNC:8820), chromosome 20p13
- **MeSH/ICD-10/11:** Grouped under hereditary ataxia/spinocerebellar ataxia (ICD-10 G11.1, "Early-onset cerebellar ataxia" category is not precise for this late-onset entity; most registries code SCA23 under the general spinocerebellar ataxia ICD-10 G11 heading, as there is no SCA23-specific ICD code)

**Synonyms:** SCA23; Spinocerebellar Ataxia 23; Prodynorphin-related spinocerebellar ataxia; ADCA type I due to PDYN mutation.

**Data provenance:** Almost all published knowledge on SCA23 derives from aggregated disease-level resources — pedigree/linkage studies, case series, and cohort screening studies — rather than large-scale EHR data, reflecting its rarity (Verbeek et al., 2004, PMID:[15306549](https://pubmed.ncbi.nlm.nih.gov/15306549/); Bakalkin et al., 2010, PMID:[21035104](https://pmc.ncbi.nlm.nih.gov/articles/PMC2978951/)).

---

## 2. Etiology

**Disease causal factor:** SCA23 is caused by heterozygous (autosomal dominant) missense mutations in *PDYN*, which encodes prodynorphin, the precursor of the opioid neuropeptides α-neoendorphin, dynorphin A (Dyn A), and dynorphin B (Dyn B) (Bakalkin et al. 2010, PMID:21035104). The locus was first mapped by genome-wide linkage analysis in a large two-generation Dutch pedigree to chromosome 20p13–12.3 (max LOD score 3.46 at marker D20S199) before the gene itself was identified (Verbeek et al. 2004, PMID:15306549).

**Genetic risk factors:**
- Eight disease-causing PDYN variants have been reported to date (Biomedicines 2021 review, PMC8698333). Six of the eight cluster exclusively within the dynorphin A/B-encoding region (residues ~207–236 of prodynorphin), the peptide segment sometimes called "Big Dynorphin" — establishing this region as a mutational hotspot.
- Named pathogenic variants (protein/cDNA nomenclature from Bakalkin et al. 2010, PMID:21035104):
  - c.414G>T, p.R138S — in the non-opioid domain of prodynorphin (large original Dutch family, 10 affected individuals)
  - c.632T>C, p.L211S (Dyn A position 5, "L5S") — sporadic case, onset age 73
  - c.634C>T, p.R212W (Dyn A position 6, "R6W") — onset age 54; most functionally severe variant
  - c.643C>T, p.R215C (Dyn A position 9, "R9C") — segregated in two affected siblings
  - c.644G>A, p.R215H — novel variant reported in two families with five affected/carrier individuals, likely pathogenic (Cerebellum & Ataxias 2020, PMC7310450)
- Overall variant frequency is very low: PDYN variants account for only ~0.1% of screened ataxia cohorts (UK study of 852 ataxia patients plus 190 MSA-C patients found essentially no convincing pathogenic carriers beyond one novel early-onset case; Chan et al., PMID:[23108490](https://pubmed.ncbi.nlm.nih.gov/23108490/)). PDYN mutations are essentially absent as a cause of multiple system atrophy (PMID:23355175) and were not found among 104 PDYN-negative German ADCA families, indicating population-specific rarity.
- **Inheritance modifier — zygosity effect:** In the Cerebellum & Ataxias 2020 family series, the individual **homozygous** for p.R215H had the most severe phenotype (wheelchair-dependent by age 59), consistent with a gene-dosage effect on disease severity, while heterozygotes showed slower, more variable progression — some remaining asymptomatic into the 9th decade (PMC7310450).

**Environmental/other risk factors:** No environmental, infectious, or lifestyle risk factors have been established; SCA23 is a purely monogenic disorder to date, though modifier loci affecting severity/penetrance have not been systematically studied.

**Protective factors:** None specifically established. Loss of normal κ-opioid receptor (KOR)-mediated neuroprotective dynorphin signaling is part of the proposed mechanism (see Section 6), implying that pharmacological restoration of KOR signaling could theoretically be protective, but this remains untested in humans.

**Gene-environment interaction:** Not established; no CTD/GWAS gene-environment interaction data exist for PDYN and SCA23.

---

## 3. Phenotypes

**Core motor phenotype (progressive, adult-onset):**
- **Gait ataxia** — nearly universal presenting feature (HP:0002066, Gait ataxia)
- **Limb/appendicular ataxia** (HP:0002070, Limb ataxia)
- **Dysarthria** (HP:0001260, Dysarthria) — common, often an early symptom
- **Slowed saccades** (HP:0000514 approximates "Slow saccadic eye movements", more precisely HP:0000605, Ophthalmoparesis is not correct; the specific term is HP:0000514/"Nystagmus" is also distinct — the precise HPO term is **HP:0001344, "Abnormal saccadic eye movements"** or the more specific **HP:0000514** is Nystagmus; slow saccades map best to **HP:0001347** is ataxia-related — recommend **HP:0000640 (Slow saccadic eye movements)** for curation)
- **Ocular dysmetria** (HP:0007874, Ocular dysmetria)
- **Hyperreflexia** (HP:0001347, Hyperreflexia)
- **Extensor plantar response / Babinski sign** (HP:0003487, Babinski sign)
- **Decreased vibratory sense**, typically distal/below the knees, reflecting peripheral sensory neuropathy (HP:0007166, Decreased vibratory sense)
- **Peripheral neuropathy** — variably present (HP:0009830)
- **Tremor** — reported in some cases (HP:0001337)
- **Dysphagia** — reported in later/severe disease (HP:0002015)
- **Parkinsonian features** (bradykinesia, rigidity) — reported in a subset mimicking multiple system atrophy with predominant parkinsonism (MSA-P) (Cerebellum & Ataxias 2020, PMC7310450)

**Phenotype characteristics:**
- **Age of onset:** Classically reported as 43–56 years in the original Dutch family (Verbeek et al. 2004), but subsequent series show a much broader range. The Cerebellum & Ataxias 2020 intrafamilial variation study reports mean onset 37.8 ± 5.5 years (range including one individual asymptomatic at 88). The 2026 Cerebellum case-report review cites a broader literature range of onset **10–73 years**, mean ~43 ± 15 years, underscoring substantial phenotypic and age-of-onset heterogeneity even within the same pedigree/mutation.
- **Severity/progression:** Slowly progressive in most cases; disease course is typically measured over decades. Severity correlates with genotype dosage (homozygotes more severe than heterozygotes in the R215H family) and possibly with specific variant (R212W/R215C show the most severe in vitro neurotoxicity).
- **Frequency (qualitative):** Because SCA23 is exceedingly rare, formal frequency-of-symptom tables (as in HPO annotation) are not well established; gait/limb ataxia and dysarthria are reported in essentially all published cases (i.e., "obligate" features), while peripheral neuropathy, tremor, and parkinsonism are "occasional" in the published literature.
- **Marked intrafamilial and interfamilial variability:** Some mutation carriers remain asymptomatic into advanced age (e.g., an 88-year-old asymptomatic carrier in one family), while others with the identical variant show severe, early progressive disease — indicating incomplete or age-dependent penetrance (PMC7310450).

**Quality of life impact:** Progressive gait and limb ataxia, dysarthria, and (in advanced/homozygous cases) wheelchair dependence and dysphagia substantially impair mobility, communication, nutrition, and independence, consistent with the general burden described for hereditary ataxias; disease-specific QOL instrument data for SCA23 specifically have not been published, but general SCA rehabilitation literature (PMC9648943) applies directly to management goals.

**Suggested HPO terms:** HP:0002066 (Gait ataxia), HP:0002070 (Limb ataxia), HP:0001260 (Dysarthria), HP:0007874 (Ocular dysmetria), HP:0001347 (Hyperreflexia), HP:0003487 (Babinski sign), HP:0007166 (Decreased vibratory sensation), HP:0009830 (Peripheral neuropathy), HP:0001337 (Tremor), HP:0002015 (Dysphagia), HP:0002527 (Falls), HP:0001272 (Cerebellar atrophy — imaging correlate).

---

## 4. Genetic/Molecular Information

**Causal gene:** *PDYN* (prodynorphin), OMIM *131340, chromosome 20p13, encoding the polyprotein precursor of α-neoendorphin, dynorphin A (Dyn A, 17 aa), dynorphin A-(1-8), and dynorphin B (Dyn B, 13 aa) — endogenous opioid peptides that are the primary endogenous ligands for the κ-opioid receptor (KOR, gene *OPRK1*).

**Pathogenic variants (missense, dominant, GAIN/altered-function — see Section 6):**

| Variant (protein) | cDNA | Position in Dyn A | Reference |
|---|---|---|---|
| p.R138S | c.414G>T | Non-opioid domain (upstream of Dyn A) | Bakalkin 2010, PMID:21035104 |
| p.L211S ("L5S") | c.632T>C | Dyn A residue 5 | Bakalkin 2010 |
| p.R212W ("R6W") | c.634C>T | Dyn A residue 6 | Bakalkin 2010 |
| p.R215C ("R9C") | c.643C>T | Dyn A residue 9 | Bakalkin 2010 |
| p.R215H | c.644G>A | Dyn A residue 9 (alternative substitution) | PMC7310450 |
| (additional variants) | — | — | 8 total reported per Biomedicines 2021 review (PMC8698333) |

- **Variant classification:** ClinVar lists multiple PDYN variants for SCA23, including p.R138S (RCV000018094, classified pathogenic/likely pathogenic by submitters) and additional missense/synonymous variants of uncertain significance (e.g., c.456C>T p.Asn152=, RCV001143591; c.405C>T p.Asp135=, RCV000392614).
- **Population frequency:** Critically, a major controversy arose because **7 of 9 originally published SCA23 variants were subsequently found in the ExAC population database**, raising doubt about pathogenicity for some variants and prompting the 2016 *Brain* correspondence "SCA23 and prodynorphin: is it time for gene retraction?" (Sailer et al., PMID:[27190015](https://pubmed.ncbi.nlm.nih.gov/27190015/)). The precipitating case was a 64-year-old Brazilian man carrying a rare PDYN missense variant, and skepticism about ExAC-observed "pathogenic" alleles. Bakalkin and colleagues rebutted (Reply, *Brain* 2016) that segregation in a large Dutch pedigree, identification of the same/related mutations in multiple independent families, and orthogonal functional/cell/mouse-model validation supported causality, and that presence of rare variants in population databases does not by itself exclude pathogenicity for a dominant, incompletely penetrant, late-onset disorder. **Curators should treat PDYN-SCA23 causality as more contested than most monogenic ataxia genes**, and weigh variant-level evidence (segregation + functional data) individually rather than assuming class-wide pathogenicity.
- **Functional consequence:** Missense variants in the Dyn A/B coding region alter processing and stability of the mature dynorphin A peptide (see Mechanism, Section 6) — a mechanism distinct from simple loss-of-function or classical gain-of-function; better classified as **altered/aberrant peptide function** (`functional_impact_category` candidates: `PARTIAL_LOSS_OF_FUNCTION` at the receptor level combined with a **gain of toxic peptide stability/accumulation** — a mixed mechanism).
- **Variant origin:** All reported variants are germline; no somatic PDYN variants have been implicated.
- **Modifier genes:** None formally established; zygosity (homozygous vs. heterozygous R215H) modifies severity within one reported family (PMC7310450).
- **Epigenetics/chromosomal abnormalities:** Not implicated; SCA23 is a point-mutation disorder, not a repeat-expansion or copy-number disorder (distinguishing it from most other numbered SCAs, which are commonly CAG-repeat expansions).

**Suggested gene/ontology annotations:** HGNC:8820 (PDYN); GO:0007218 (neuropeptide signaling pathway); GO:0038193 (thromboxane receptor signaling — not applicable); more precisely **GO:0038047 (opioid receptor activity)** and **GO:0016248 (opioid receptor binding)**; CHEBI compound-level term for dynorphin A is not standard (peptide, not small molecule) — use UniProt P01213 (Proenkephalin-B/Prodynorphin, human) as protein reference.

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, pollutants, or infectious agents have been implicated in SCA23 causation; this is a purely monogenic, autosomal dominant disorder. No lifestyle factor (diet, smoking, alcohol, exercise) has been shown to modify onset or progression in the literature reviewed. This section is essentially not applicable beyond noting the absence of reported gene-environment interaction data.

---

## 6. Mechanism / Pathophysiology

SCA23 pathophysiology centers on **dysregulated processing and toxic accumulation of mutant dynorphin A peptide**, converging on **loss of neuroprotective κ-opioid receptor (KOR) signaling** combined with **NMDA-receptor-mediated excitotoxicity** and **direct membrane-disruptive peptide toxicity**.

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Missense mutation in the PDYN Dyn A/B coding region (e.g., p.R212W, p.L211S, p.R215C) (GO:0006508, proteolysis; the mutations affect proprotein convertase processing sites).
2. **Altered peptide processing/stability:** Two of the mutations (p.L211S, p.R212W) cause **10- to 18-fold elevated Dyn A peptide levels** in a transfected cellular model (RINm-5F cells) compared to wild type — i.e., a "gain" in peptide abundance due to impaired degradation/processing rather than increased transcription (Bakalkin et al. 2010, PMID:21035104).
3. **Altered secondary structure:** Mutant Dyn A peptides show **loss of the N-terminal α-helix**, altered secondary structure, and increased peptide stability/resistance to degradation (Human Molecular Genetics 2016, PMID:[27260403](https://pubmed.ncbi.nlm.nih.gov/27260403/)).
4. **Loss of KOR signaling (loss-of-function at the receptor level):** Mutant Dyn A peptides show markedly **reduced potency at the κ-opioid receptor (KOR)** for both canonical G-protein dissociation and β-arrestin recruitment (EC50 shifts: R6W ~11-fold reduced potency, L5S ~7-fold, R9C ~3-fold) (Biomedicines 2021, PMC8698333). Structural modeling shows the wild-type Arg6 forms a critical ionic interaction with glutamate E297 on the KOR transmembrane helix, which is disrupted by the R6W substitution.
5. **Partial switch to NMDA-receptor-mediated excitotoxicity:** Loss of normal opioid-receptor-mediated neuroprotective signaling is accompanied by a partial shift toward **NMDA receptor-mediated excitotoxic signaling**, contributing to neuronal injury (PMID:27260403).
6. **Direct membrane toxicity:** Enhanced peptide stability of mutant Dyn A enables **plasma membrane poration/bilayer penetration**, causing membrane leakage and cellular dysfunction independent of receptor signaling — a proposed general mechanism for pathological neuropeptide signal transduction (*Cell Death & Disease* 2015).
7. **Cellular consequence — cytotoxicity:** Mutant Dyn A peptides (particularly R212W and R215C) induce marked **neuronal loss in cultured striatal neurons** on time-lapse imaging (Bakalkin 2010) and cause **Purkinje cell loss** in vivo.
8. **Circuit-level consequence — climbing fiber/Purkinje cell pathology and developmental component:** In the PDYN R212W knock-in mouse, **developmental deficits are detectable as early as 2 weeks of age** — a reduced number of GABAergic synapses on Purkinje cell somata and delayed climbing-fiber (CF) elimination between postnatal days 14–21, so that CFs fail to reach their normal terminal dendritic height, leaving proximal Purkinje dendrites available for parallel-fiber (PF) territory takeover (increased vGlut1, a PF-PC synapse marker). This establishes SCA23 as having a **neurodevelopmental component superimposed on later neurodegeneration** (Smeets et al., *Brain Pathology* 2021, PMID:[33043513](https://pubmed.ncbi.nlm.nih.gov/33043513/)).
9. **Progressive degeneration:** PDYN R212W mice show progressive **motor deficits from 3 months of age**, ongoing **climbing-fiber deficits from 3 months**, and overt **Purkinje cell loss by 12 months of age**, reproducing core features of the human disease (Jezierska/Bakalkin group, *Brain* 2015, PMID:[26169942](https://pubmed.ncbi.nlm.nih.gov/26169942/)).
10. **End-organ/clinical manifestation:** Progressive cerebellar (and variably brainstem/spinal cord) degeneration produces the gait/limb ataxia, dysarthria, oculomotor, and reflex abnormalities described in Section 3.

**Cell types involved:** Cerebellar Purkinje cells (CL:0000121), striatal neurons (used as the in vitro toxicity model; CL:0000393 medium spiny neuron), inferior olivary neurons (climbing fiber origin), dentate nucleus neurons, and glial cells (gliosis in affected white matter).

**Molecular functions/processes (suggested GO terms):** GO:0038047 (opioid receptor activity), GO:0007218 (neuropeptide signaling pathway), GO:0007269 (neurotransmitter secretion), GO:0006508 (proteolysis, neuropeptide processing), GO:0043524 (negative regulation of neuron apoptotic process — for the lost neuroprotective KOR arm), GO:0007268 (chemical synaptic transmission), GO:0021702 (cerebellar Purkinje cell differentiation, developmental component), GO:0021688 (cerebellar molecular layer formation).

**Anatomical/cellular localization (suggested UBERON/CL/GO-CC):** UBERON:0002037 (cerebellum), UBERON:0002190 (cerebellar vermis specifically implicated — rostral vermis Purkinje cell loss), UBERON:0002037 dentate nucleus, UBERON:0002037 inferior olivary nucleus, UBERON:0002298 brainstem (basis pontis atrophy), CL:0000121 (Purkinje cell), GO:0005886 (plasma membrane — site of peptide-membrane interaction and KOR signaling).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Central nervous system — predominantly the **cerebellum** (UBERON:0002037), with prominent **rostral vermis** involvement.
- **Secondary/associated regions:** Brainstem (basis pontis atrophy, relatively small cerebellopontine tracts), spinal cord (atrophy reported at autopsy), dentate nuclei, and inferior olivary nuclei (marked neuronal loss). One autopsy case additionally noted frontotemporal cerebral atrophy and ubiquitin-positive intranuclear inclusions in nigral neurons (interpreted as incidental Marinesco bodies, not disease-specific pathology) (Genetic Update review, PMID:[19089525](https://pubmed.ncbi.nlm.nih.gov/19089525/)).
- **Peripheral nervous system:** Variable peripheral sensory neuropathy (decreased vibratory sense) implicates dorsal root ganglia/peripheral sensory axons, though this is less consistently reported than the core cerebellar phenotype.
- **Tissue/cell level:** Purkinje cell layer of the cerebellar cortex (severe loss), surrounding cerebellar white matter (myelin loss and gliosis), climbing fiber–Purkinje cell synapses (developmentally and progressively disrupted), granule cell layer (parallel fiber territory expansion documented in mouse model).
- **Subcellular level:** Plasma membrane (site of peptide-induced poration; GO:0005886), synaptic vesicles/dense-core granules (site of prodynorphin processing and dynorphin storage/release; GO:0030141 secretory granule).
- **Localization/laterality:** Diffuse, bilateral cerebellar and brainstem involvement; no reported lateralization.

**Suggested UBERON/CL terms:** UBERON:0002037 (cerebellum), UBERON:0002190 (cerebellar vermis), UBERON:0002315 (cerebellar cortex), UBERON:0002038 (dentate nucleus), UBERON:0002298 (brainstem), CL:0000121 (Purkinje cell), CL:0000119 (cerebellar granule cell).

---

## 8. Temporal Development

- **Onset:** Adult-onset, with substantial reported range — classic Dutch family: 43–56 years; broader literature range across all reported families/cases: **10–73 years** (mean ~43 ± 15 years per the 2026 case-report review); one large intrafamilial series reports mean onset 37.8 ± 5.5 years. Onset is typically **insidious**, presenting with dysarthria, gait unsteadiness, or speech disturbance.
- **Progression:** Slowly progressive over years to decades in most patients; a subset (notably a homozygous R215H carrier) shows more rapid, severe progression to wheelchair dependence (by age 59 in the reported case).
- **Disease course pattern:** Chronic, progressive, non-remitting; no episodic or relapsing-remitting pattern has been described.
- **Penetrance/critical periods:** Age-dependent, incomplete penetrance is documented — an obligate carrier remained asymptomatic at age 88 in one family, indicating either very-late or absent clinical penetrance is possible. This has direct implications for genetic counseling of at-risk relatives.
- **Neurodevelopmental component:** Mouse model data (Smeets et al. 2021) indicate that **pathological changes at the synaptic/circuit level (climbing fiber elimination delay, reduced GABAergic PC synapses) begin in early postnatal development (~2 weeks in mice)**, long before any measurable motor deficit (3 months) or Purkinje cell loss (12 months) — suggesting SCA23 may have a subclinical developmental substrate decades before human symptom onset, an important consideration for early-biomarker or preventive-intervention strategies.

---

## 9. Inheritance and Population

- **Epidemiology:** SCA23 is exceptionally rare. Population prevalence/incidence figures are not established in standard registries (SEER, GBD) given its rarity; the best available quantitative estimate is that **PDYN variants account for ~0.1% of screened ataxia cohorts** (UK cohort of 852 ataxia patients plus 190 MSA-C patients; Chan et al., PMID:23108490). As of the most recent case reports (2026), SCA23 remains reportable as individual case series — e.g., a 2026 case report describes only the **third reported case in the Americas and second in Brazil**, underscoring how few confirmed cases exist worldwide outside the Netherlands.
- **Geographic distribution:** Originally and predominantly described in **Dutch/Netherlands families** (the founding pedigree and several subsequent Dutch families/sporadic cases); subsequently identified sporadically in the UK, China (Han population, described as an "uncommon SCA subtype"), and most recently South America (Brazil). SCA23 appears to be essentially absent or exceptionally rare in central European (German) ADCA cohorts specifically screened and found negative.
- **Inheritance pattern:** Autosomal dominant (AD); one reported instance of homozygosity for p.R215H associated with more severe disease, suggesting a semi-dominant, gene-dosage effect atop dominant inheritance.
- **Penetrance:** Incomplete and age-dependent — asymptomatic carriers into the 9th decade have been documented.
- **Expressivity:** Highly variable, both between and within families (intrafamilial phenotypic heterogeneity extending to an MSA-parkinsonism-mimicking presentation in one proband).
- **Genetic anticipation:** Not established/reported for SCA23 (unlike CAG-repeat SCAs); SCA23 is a point-mutation disorder, so classical repeat-expansion anticipation is not expected.
- **Founder effects:** The concentration of cases in Dutch families raises the possibility of a founder effect for specific variants (e.g., p.R138S in the original large pedigree), though this has not been formally established via haplotype analysis in the literature reviewed.
- **Consanguinity:** The one reported homozygous case (p.R215H) arose in the context of two related branches of an extended family rather than documented parental consanguinity per se (PMC7310450); consanguinity is not established as a general risk factor.
- **Sex ratio / age distribution:** No specific male:female skew has been reported; case reports include both sexes across a wide adult age range at onset.
- **Carrier frequency:** Not established in large reference population databases beyond the ExAC observations that prompted the 2016 pathogenicity controversy (Section 4).

---

## 10. Diagnostics

**Clinical tests:**
- **Neurological examination:** gait/limb ataxia assessment, saccadic eye movement testing, deep tendon reflex and plantar response testing, vibratory sense testing.
- **Imaging (MRI):** Cerebellar atrophy is a consistent finding across reported cases, generally with vermian and hemispheric involvement; brainstem is relatively preserved in most cases (distinguishing from MSA-C, which characteristically shows pontine "hot cross bun" sign — **absent** in SCA23 per the intrafamilial variation study). One SCA23 case showed an atypical "hyperintense lateral putaminal rim," creating diagnostic overlap with MSA-P and illustrating why SCA23 can mimic MSA clinically and radiologically (PMC7310450).
- **Electrophysiology:** Nerve conduction studies may show peripheral neuropathy in a subset of patients (not systematically characterized).
- **Neuropathology (autopsy, when available):** Marked Purkinje cell loss in the rostral cerebellar vermis, neuronal loss in dentate nuclei and inferior olives, myelin loss/gliosis in adjacent white matter, relatively preserved basis pontis myelination but reduced cerebellopontine tract size, and brain weight reduction reflecting overall atrophy (PMID:19089525).

**Genetic testing:**
- **Recommended approach:** Given extreme rarity (~0.1% of ataxia cohorts), PDYN sequencing is generally **not** first-line in undiagnosed ataxia and is more appropriately pursued after exclusion of the common repeat-expansion SCAs (SCA1, 2, 3, 6, 7) and other more prevalent causes, or via a broad **ataxia gene panel** or exome/genome sequencing, particularly in familial, autosomal-dominant, "pure" cerebellar ataxia cases without another identified cause. The UK screening study explicitly concludes that "front-line diagnostic evaluation... should focus on other known ataxia genes" given PDYN's rarity (PMID:23108490).
- **Single-gene testing:** Direct Sanger sequencing of PDYN coding exons and flanking intronic regions, focused especially on the dynorphin A/B-encoding hotspot region (residues ~207–236), is used once other causes are excluded or when segregation analysis in a family with an existing candidate variant is needed.
- **Whole exome/genome sequencing (WES/WGS):** Increasingly the diagnostic route by which sporadic/small-family SCA23 cases are now identified (e.g., the 2026 Brazilian case, diagnosed via next-generation sequencing).
- **Variant interpretation caution:** Given the ExAC-based controversy over pathogenicity of several PDYN variants (Section 4), genetic counseling for a PDYN variant of uncertain significance should incorporate segregation data, population frequency, and — where possible — functional evidence (e.g., peptide stability/KOR signaling assays), rather than classification alone.
- **Chromosomal microarray/karyotyping/FISH/mitochondrial testing/repeat-expansion testing:** Not applicable — SCA23 is not a copy-number, chromosomal, mitochondrial, or repeat-expansion disorder.

**Differential diagnosis:** Other autosomal dominant SCAs (especially repeat-expansion SCA1/2/3/6/7 and other ADCA type I subtypes), **multiple system atrophy with cerebellar or parkinsonian features (MSA-C/MSA-P)** — a particularly important mimic given overlapping late-onset ataxia/parkinsonism and (in one case) similar putaminal MRI signal change, though brainstem "hot cross bun" sign is typically absent in SCA23. PDYN mutations were specifically shown **not** to be a cause of sporadic MSA in a dedicated screening study (PMID:23355175), reinforcing that PDYN testing should be reserved for familial/dominant-inheritance-pattern cases rather than sporadic MSA-like presentations.

**Screening:** No population-based or newborn screening applies given adult onset and rarity; **predictive/cascade testing** in at-risk relatives of a confirmed proband is the relevant genetic-counseling application, tempered by the documented incomplete, age-dependent penetrance.

**Suggested NCIT/LOINC terms:** NCIT:C16809 (Magnetic Resonance Imaging), NCIT:C15709 (Genetic Testing), NCIT:C158748-type panel testing concepts, LOINC terms for targeted PDYN gene sequencing (locus-specific, no dedicated LOINC panel code identified in this review).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics (5-/10-year survival, life expectancy) have been published for SCA23 specifically, consistent with its rarity and the absence of large natural-history cohorts. The disease is understood as being **slowly progressive but not rapidly fatal** in most reported cases, in contrast to some other SCAs with earlier or more aggressive courses.
- **Morbidity/functional outcomes:** Progressive gait and limb ataxia leading to increasing mobility impairment; the most severe reported outcome (homozygous R215H carrier) was wheelchair dependence by age 59. Dysarthria and (in advanced disease) dysphagia contribute to communication and nutritional morbidity.
- **Complications:** Falls and fall-related injury (implied by progressive gait ataxia, though not separately quantified), aspiration risk with dysphagia in advanced cases, and functional decline requiring rehabilitative support.
- **Prognostic factors:** Genotype dosage (homozygous vs. heterozygous) appears to modify severity; specific variant identity may modify severity given differential in vitro neurotoxicity (R6W/R212W and R9C/R215C show more severe cell-culture neurotoxicity than L5S/L211S). Age of onset varies widely and does not appear tightly predictable from genotype alone given documented intrafamilial variability, including near-complete non-penetrance in at least one elderly carrier.
- **Recovery potential:** As a neurodegenerative disorder, spontaneous recovery is not expected; multidisciplinary rehabilitation (see Section 12) aims to maximize function rather than reverse disease.

---

## 12. Treatment

**No disease-modifying or curative therapy exists for SCA23.** As with other hereditary cerebellar ataxias, management is entirely **symptomatic and supportive**, following the general framework used across the SCA spectrum (PMC9048095 review of current/emerging SCA treatment modalities; PMC9648943 rehabilitation review):

- **Pharmacotherapy (symptomatic, non-SCA23-specific evidence base):**
  - Agents such as riluzole and valproic acid have been trialed for cerebellar ataxia symptoms in SCAs broadly, though evidence quality is limited and none is SCA23-specific (NCIT:C15986, Pharmacotherapy; CHEBI riluzole CHEBI:8804).
  - Antispasmodic agents for spasticity if present.
  - Analgesics/psycholeptics for pain and mood symptoms as needed.
- **Rehabilitative/supportive care (the mainstay of documented SCA23 management):**
  - **Multidisciplinary rehabilitation** — the 2026 Brazilian case report explicitly describes referral to a multidisciplinary rehabilitation team focused on **functional gait rehabilitation and dysphagia management** (NCIT:C15302, Physical Therapy; NCIT:C159273, Speech Therapy; NCIT:C121351, Occupational Therapy).
  - Physical therapy for gait and balance training.
  - Speech and swallowing therapy for dysarthria and dysphagia, critical for aspiration prevention.
  - Occupational therapy to support activities of daily living as disability progresses.
- **Genetic counseling** (NCIT:C15240) is an essential component of care given autosomal dominant inheritance with incomplete, age-dependent penetrance, informing at-risk relatives about predictive testing options and the uncertainty around variant-level pathogenicity.
- **Experimental/investigational directions (mechanism-informed, not yet in human trials for SCA23):** Given the proposed loss of neuroprotective KOR signaling and gain of NMDA-receptor-mediated excitotoxicity, **KOR agonism** or **NMDA receptor modulation** represent plausible but unvalidated therapeutic strategies suggested by the mechanistic literature (PMID:27260403); no clinical trials specifically targeting PDYN/KOR pathway modulation in SCA23 patients were identified in this search (ClinicalTrials.gov search recommended as a follow-up for currency).
- **Surgical/device interventions:** Not applicable; no surgical treatment is described for SCA23.

**Suggested NCIT terms for treatment annotation:** NCIT:C15747 (Supportive Care), NCIT:C15302 (Physical Therapy), NCIT:C159273 (Speech Therapy), NCIT:C121351 (Occupational Therapy), NCIT:C15240 (Genetic Counseling), NCIT:C15986 (Pharmacotherapy, generic, for symptomatic drug trials with therapeutic_agent sub-binding to riluzole/CHEBI:8804 where used).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause); the only "primary prevention" avenue is **reproductive genetic counseling** for known carrier families, including discussion of preimplantation genetic diagnosis (PGD) or prenatal testing where desired, tempered by the challenge that penetrance is incomplete and age-dependent, complicating risk communication.
- **Secondary prevention/early detection:** Predictive genetic testing of at-risk relatives in a family with a confirmed pathogenic PDYN variant allows early identification of carriers, though clinical utility is limited by the absence of any preventive or disease-modifying intervention to offer asymptomatic carriers at present.
- **Tertiary prevention:** Multidisciplinary rehabilitative care (Section 12) functions as tertiary prevention — minimizing fall risk, aspiration, and functional decline complications once disease is manifest.
- **Screening programs:** No population or newborn screening applies (adult-onset, rare, no actionable early intervention).
- **Public health/environmental interventions:** Not applicable — no environmental risk factor has been identified to intervene upon.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease in other species:** No naturally occurring PDYN-associated cerebellar ataxia has been reported in companion animals or wildlife (e.g., no OMIA entry identified for a PDYN-linked ataxia). SCA23 knowledge in non-human species derives exclusively from **engineered/induced genetic mouse models** (Section 15), not naturally occurring veterinary disease.
- **Comparative biology:** Prodynorphin and the opioid peptide system (dynorphins, κ-opioid receptor) are highly conserved across mammals, supporting the translational validity of the mouse knock-in model for studying the human mutation's mechanistic consequences (Purkinje cell loss, climbing fiber pathology).
- **Zoonotic potential:** Not applicable — SCA23 is a purely genetic, non-communicable, non-zoonotic disorder.

---

## 15. Model Organisms

**Genetic mouse model — PDYN R212W knock-in mouse:**
- **Model type:** Genetically engineered mouse expressing human PDYN carrying the SCA23-causing p.R212W (R6W in Dyn A) variant.
- **Phenotype recapitulation:**
  - **Progressive motor deficits** beginning at 3 months of age.
  - **Climbing fiber (CF) synaptic deficits** detectable from 3 months of age, with earlier **developmental** CF elimination delay and reduced Purkinje cell somatic GABAergic synapse number detectable as early as **2 weeks postnatal age** (Smeets et al., *Brain Pathology* 2021, PMID:33043513).
  - **Purkinje cell loss** emerging by **12 months of age**, together with elevated levels of mutant dynorphin A (Jezierska/Bakalkin group, *Brain* 2015, PMID:26169942).
  - Reproduces core disease features: gait deficits, climbing-fiber pathology, and Purkinje cell degeneration — providing strong (though not complete) fidelity to the human phenotype, and directly linking the biochemical mechanism (elevated/toxic mutant Dyn A) to the anatomical and behavioral phenotype.
- **Model limitations:** As with most knock-in models of a late-onset human disease, the mouse model's timeline is compressed relative to the human decades-long course, and it captures only the R212W allele — not the full allelic spectrum (e.g., R138S in the non-opioid domain acts through a potentially distinct mechanism not yet separately modeled). The model's most novel finding — a **neurodevelopmental** synaptic phenotype at 2 weeks — has not yet been confirmed to have a human correlate, representing an open `HUMAN_MODEL_MISMATCH`-type question: whether human PDYN-mutation carriers have subclinical developmental cerebellar circuit abnormalities decades before overt ataxia.
- **Cellular/in vitro models:** Transfected RINm-5F cells (rat insulinoma cell line) used to demonstrate elevated mutant Dyn A peptide production; cultured striatal neurons (primary rodent) used in time-lapse imaging to demonstrate direct neurotoxicity of mutant Dyn A peptides (R212W, R215C) (Bakalkin et al. 2010, PMID:21035104). Receptor pharmacology (KOR G-protein/β-arrestin signaling assays) performed in heterologous expression systems to quantify EC50 shifts for mutant peptides (Biomedicines 2021, PMC8698333).
- **Applications:** The mouse model is used to study the temporal relationship between molecular pathology (mutant peptide accumulation), synaptic/circuit pathology (climbing fiber-Purkinje cell synapse abnormalities), and cell loss/behavioral phenotype — and represents the principal in vivo platform for any future preclinical therapeutic testing (e.g., KOR-targeted or NMDA-modulating compounds).

**Suggested NCBITaxon/model resource terms:** NCBITaxon:10090 (Mus musculus), NCBITaxon:9606 (Homo sapiens, for the knock-in human-mutant transgene context); model resource cross-reference would be to MGI once/if a formal MGI allele record is confirmed (not verified in this search).

---

## Summary of Key Evidence Citations (PMID)

| Topic | Citation | PMID |
|---|---|---|
| Locus mapping, chromosome 20p13-12.3, original Dutch family | Verbeek et al., *Brain* 2004 | 15306549 |
| Identification of PDYN as SCA23 gene, 4 mutations, functional data | Bakalkin et al., *Am J Hum Genet* 2010 | 21035104 |
| Elevated mutant Dyn A, Purkinje cell loss, R212W mouse model | Jezierska et al./Bakalkin group, *Brain* 2015 | 26169942 |
| Altered Dyn A secondary structure, loss of opioid signaling, NMDA excitotoxicity | *Hum Mol Genet* 2016 | 27260403 |
| Pathogenicity controversy ("gene retraction?") | Sailer et al., *Brain* 2016 (letter) | 27190015 |
| UK cohort screening, frequency ~0.1% | Chan et al., *J Neurol* 2012 | 23108490 |
| PDYN not implicated in MSA | *J Neurol* 2013 | 23355175 |
| Genetic update review | *Cerebellum* 2009 | 19089525 |
| Cerebellar developmental deficits, R212W mouse (climbing fiber) | Smeets et al., *Brain Pathol* 2021 | 33043513 |
| Intrafamilial phenotypic variation, R215H variant | *Cerebellum Ataxias* 2020 | (PMC7310450) |
| Functional characterization of Dyn A mutant peptides (KOR EC50 data) | *Biomedicines* 2021 | (PMC8698333) |
| SCA23 review | *J Neurol* 2021 | 33175256 |
| Third case in the Americas (Brazil), NGS diagnosis | *Cerebellum* 2026 | (in press, DOI 10.1007/s12311-026-02001-6) |

**Note on evidence quality:** Given SCA23's rarity, most quantitative claims (frequency ~0.1%, age-of-onset ranges, EC50 shifts) derive from small cohort/case-series/single-family studies rather than large epidemiological databases; the pathogenicity of several individual PDYN variants remains actively debated in the literature (Section 4), which curators should flag explicitly (e.g., via `evidence_source` classification and possibly a `mechanistic_hypotheses`/`KNOWLEDGE_GAP` discussion block) rather than treating PDYN→SCA23 causality as uniformly settled across all eight reported variants.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.
