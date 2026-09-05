---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T02:30:39.727859'
end_time: '2026-08-09T02:36:15.309346'
duration_seconds: 335.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy with Generalized Tonic-Clonic Seizures Alone
  mondo_id: ''
  category: Complex
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 28
  total_cost_usd: 2.0610037
  session_id: 7b1f73c8-4253-5247-a1ab-17fb2dce44ff
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epilepsy with Generalized Tonic-Clonic Seizures Alone
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Epilepsy with Generalized Tonic-Clonic Seizures Alone** covering all of the
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

# Epilepsy with Generalized Tonic-Clonic Seizures Alone (EGTCSA) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Epilepsy with generalized tonic-clonic seizures alone (EGTCSA) — historically termed "epilepsy with grand mal on awakening" (Aufwach-Epilepsie, described by Janz in 1953) — is one of the four canonical **idiopathic generalized epilepsy (IGE)** syndromes, alongside childhood absence epilepsy (CAE), juvenile absence epilepsy (JAE), and juvenile myoclonic epilepsy (JME). It is defined by the occurrence of generalized tonic-clonic seizures (GTCS) as the *sole* seizure type, in a patient with a generalized EEG trait and no structural brain lesion, distinguishing it from JME/JAE where GTCS occur together with myoclonic jerks or absences (Hirsch et al., *Epilepsia* 2022, PMID for ILAE position statement, doi:10.1111/epi.17236) ([Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/epi.17236)).

**Key identifiers:**
- **MONDO:** MONDO:0005754 ("Epilepsy with generalized tonic-clonic seizures," the current MONDO umbrella term used for this entity) ([BioPortal](https://bioportal.bioontology.org/ontologies/MONDO?p=classes&conceptid=MONDO:0005579))
- **Orphanet:** ORPHA:698005 ("Epilepsy with generalized tonic-clonic seizures alone") ([Orphanet](https://www.orpha.net/en/disease/detail/698005))
- **ICD-10:** G40.3 (Generalized idiopathic epilepsy and epileptic syndromes)
- **MeSH:** Epilepsy, Generalized (D004829) / Epilepsy, Tonic-Clonic (D004832)
- **ILAE classification:** One of the four Idiopathic Generalized Epilepsy Syndromes (2022 ILAE Nosology Task Force) ([ILAE](https://www.ilae.org/guidelines/definition-and-classification/proposed-classification-and-definition-of-epilepsy-syndromes/proposed-classification-idiopathic-generalized-epilepsies))

**Synonyms:** Epilepsy with grand mal on awakening; Aufwach-Epilepsie (Janz); Awakening epilepsy; Generalized tonic-clonic seizures on awakening; Pure grand mal epilepsy; formerly abbreviated GMA or EGMA; also loosely "primary generalized tonic-clonic epilepsy."

**Data provenance:** Information on this syndrome is derived from a mix of individual-patient clinical/EEG cohorts (e.g., Beydoun et al. 2024 prospective cohort, PMC11296088; Asadi-Pooya & Homayoun 2020 retrospective cohort, PMID:32030724) and aggregated syndrome-level nosologic resources (ILAE, Orphanet, epilepsydiagnosis.org/Epilepsy Diagnosis.org "EpilepsyDiagnosis" curated syndrome pages, and MedLink Neurology).

---

## 2. Etiology

**Disease causal factors:** EGTCSA is classified as a **genetic/idiopathic generalized epilepsy** — presumed genetic etiology without an identifiable structural, metabolic, or acquired cause in the great majority of patients. Genetic architecture is **complex/polygenic**, not monogenic: "As the genetic etiology is complex/polygenic, pathogenic single gene disorders are not expected and genetic testing is not part of routine clinical evaluation" (epilepsydiagnosis.org, EGTCSA genetics page).

**Genetic risk factors:**
- **Polygenic risk / common-variant architecture:** GWAS meta-analyses by the ILAE Consortium on Complex Epilepsies identified genome-wide significant loci for genetic generalized epilepsy (GGE) as a class. The 2018 mega-analysis (*Nat Commun* 2018, PMID for International League Against Epilepsy Consortium GWAS) identified 16 genome-wide loci across common epilepsies with strongest signal in genetic generalized epilepsy ([Nature Communications 2018](https://www.nature.com/articles/s41467-018-07524-z)); a larger 2023 meta-analysis (29,944 cases, 52,538 controls) identified 26 risk loci, 19 of which were specific to GGE, implicating 29 likely causal genes (*Nat Genet* 2023) ([Nature Genetics 2023](https://www.nature.com/articles/s41588-023-01485-w)).
- **Twin studies:** Monozygotic twin concordance for IGE substantially exceeds dizygotic concordance (76% vs 33% cited in one review, PMID:9546323), supporting strong heritability (PMC11097769, "Idiopathic Generalized Epilepsy: Misunderstandings, Challenges, and Opportunities," PMID:38165295).
- **Candidate/rare-variant genes reported across the IGE spectrum** (not EGTCSA-specific, but implicated in the broader syndrome group EGTCSA belongs to):
  - **CLCN2** (voltage-gated chloride channel ClC-2, hgnc gene) — variants reported in IGE families including EGTCSA/GTCS phenotypes, though causality remains **controversial**: Saint-Martin et al. 2009 (*Hum Mutat*, PMID:19191339) identified two novel CLCN2 missense mutations (p.Arg235Gln, p.Arg577Gln) with accelerated channel deactivation kinetics in IGE families; Niemeyer et al. (PMID:15252188) performed functional characterization of ClC-2 IGE-associated mutants; but Saint-Martin et al. 2007 (PMID:16932951) concluded CLCN2 mutations are only a rare cause, and a subsequent study found "no evidence for a role of CLCN2 variants in idiopathic generalized epilepsy" (*Nat Genet* 2010) — an earlier 2003 CLCN2 paper was later **retracted**.
  - **CACNB4** (calcium channel beta-4 subunit), **CACNA1A/CACNA1G/CACNA1H** (calcium channel alpha subunits/T-type channels), **GABRA1, GABRB3, GABRG2, GABRD** (GABA-A receptor subunits), **EFHC1** (myoclonin-1) — all reported across the IGE/JME spectrum (PMC11097769); no single gene is established as causal specifically for EGTCSA.
  - **BRD2** (6p21.3) and **connexin-36/GJD2** — reported associations with JME.
- **Copy number variants:** Recurrent microdeletions **15q11.2, 15q13.3, and 16p13.11** are recommended for screening via chromosomal microarray specifically when EGTCSA is drug-resistant or accompanied by intellectual disability (epilepsydiagnosis.org genetics page).
- **Family history:** A first-degree family history of epilepsy is present in roughly 2 in 10 patients ("in keeping with complex inheritance"), with affected relatives typically having other IGE/genetic generalized epilepsy phenotypes rather than EGTCSA specifically. Family history of febrile seizures is reported in ~1 in 10 patients (epilepsydiagnosis.org overview page).

**Environmental risk factors / precipitants (function as seizure triggers/provocateurs rather than root causes in a genetically susceptible individual):**
- **Sleep deprivation** — the dominant and best-documented trigger.
- **Fatigue.**
- **Alcohol use/withdrawal.**
- **Sleep-wake transitions** — seizures cluster in the 1–2 hours after awakening (hence the historical name), and to a lesser extent in a second peak during evening relaxation ("at leisure time").
- **Photic stimulation** — a photoparoxysmal EEG response is documented on repeat EEG testing in up to 35% of EGTCSA patients (Beydoun et al. 2024, PMC11296088), and clinical photosensitivity is a recognized precipitant in the broader IGE group.

**Protective factors:** No specific genetic or environmental protective factors are documented for EGTCSA in the literature surveyed; general seizure-threshold-raising behaviors (regular sleep, alcohol avoidance) are protective against triggering seizures in a susceptible individual but do not alter underlying genetic risk.

**Gene-environment interactions:** The prevailing model is a **polygenic susceptibility threshold** modulated by environmental state-dependent factors (sleep deprivation, circadian phase, alcohol) that transiently lower seizure threshold in genetically predisposed thalamocortical networks — consistent with the "system epilepsy" framework in which seizure timing (awakening) reflects an interaction between genetic network hyperexcitability and the sleep-wake cycle rather than a discrete lesion (Janz 2000, *Clin Neurophysiol* 111 Suppl 2:S103-10, PMID:10996562).

---

## 3. Phenotypes

**Core phenotype — Generalized Tonic-Clonic Seizure (the defining and, by definition, only seizure type):**
- **HPO term suggestion:** HP:0002069 (Generalized tonic-clonic seizures); broader parent HP:0032661 (Generalized-onset seizure) / HP:0001250 (Seizure).
- **Type:** Clinical sign/seizure semiology.
- **Onset:** Peak in the second decade; overall range 5–40 years, with ~80% starting between ages 11–23 (typically cited as 10–25 years) (epilepsydiagnosis.org overview; epilepsy.com syndrome page). In the Beydoun 2024 cohort (n=89), median age at onset was **16 years**.
- **Severity:** Seizures are typically infrequent (in contrast to the more frequent seizures of JME or CAE) but are, by definition, convulsive and carry injury/SUDEP risk.
- **Timing pattern:** Predominantly **diurnal, shortly after awakening** (within 1–2 hours of waking, independent of clock time) or during relaxation/"leisure time" in the evening. In the Beydoun cohort, 59.6% had exclusively diurnal seizures, 28.1% had a mixed diurnal/nocturnal pattern, and a mixed circadian pattern was itself an independent predictor of relapse after medication withdrawal.
- **Progression:** Typically stable/non-progressive in cognitive terms; seizure frequency is usually low and episodic, often triggered rather than spontaneous.
- **Frequency among affected individuals:** By definition 100% (this is the defining/only phenotype), though the diagnosis requires exclusion of absence and myoclonic seizures.

**Associated/secondary features:**
- **Normal neurological examination and head circumference** (epilepsydiagnosis.org).
- **Normal antecedent/birth history**; possible prior febrile seizures.
- **Cognitive profile:** Typically normal global development and intelligence, though subtle deficits in **executive function and attention** may be present in a subset — consistent with the broader IGE literature showing a distinct neuropsychological profile of impaired executive function and reduced psychomotor speed with preserved memory across IGE syndromes (NBK546611).
- **Psychiatric comorbidity (extrapolated from IGE-wide data, not EGTCSA-specific):** Psychiatric comorbidities affect an estimated ~75% of people with epilepsy broadly, with depression (~55%) and anxiety (~25–50%) most common; comorbidity contributes to premature mortality in epilepsy independent of seizure control (Lancet 2013 population study; PMC9433706).

**Quality of life impact:** Not separately quantified for EGTCSA in the sources reviewed; IGE-wide data show reduced quality of life associated with poor seizure control, psychiatric comorbidity, and unemployment (PMC11097769). Recurrent GTCS carry a documented 40–60% risk of seizure-related bodily injury (burns, fractures, concussion) at 12-month follow-up in generalized epilepsy cohorts (NBK546611).

**HPO term summary for KB curation:**
| Phenotype | Suggested HPO term |
|---|---|
| Generalized tonic-clonic seizure | HP:0002069 |
| Seizures related to sleep-wake cycle / on awakening | (no precise HPO term; capture via `temporality`/description) |
| Photoparoxysmal EEG response | HP:0010819 (Photoparoxysmal response) |
| Executive dysfunction | HP:0031331 (Impaired executive functioning) — verify exact label via OAK |
| Generalized spike-wave discharges | HP:0011182 (Generalized non-motor seizure with impairment of consciousness — not exact; better modeled as an EEG/laboratory finding, e.g., HP:0002353 EEG abnormality) |

---

## 4. Genetic/Molecular Information

- **Causal genes:** None established as monogenic causes specific to EGTCSA. The syndrome is explicitly modeled as **polygenic/complex**, and "pathogenic single gene disorders are not expected" (epilepsydiagnosis.org). This distinguishes EGTCSA from monogenic epilepsy syndromes and from GEFS+ (Genetic Epilepsy with Febrile Seizures Plus), a related but phenotypically and often genetically distinct spectrum (SCN1A, SCN1B, GABRG2 etc.) that includes febrile seizures as a defining feature.
- **Candidate genes reported in the broader IGE/GTCS literature** (association-level evidence, not disease-causing in the Mendelian sense):
  - **CLCN2** (chloride channel 2) — see Etiology section; controversial, retracted early report, later studies show inconsistent replication.
  - **CACNB4, CACNA1A, CACNA1G, CACNA1H** — calcium channel subunits, implicated in T-type calcium current dysregulation central to thalamocortical hypersynchronization models.
  - **GABRA1, GABRB3, GABRG2, GABRD** — GABA-A receptor subunit genes.
  - **EFHC1** (myoclonin-1) — primarily JME-associated.
  - **BRD2** — JME-associated polymorphism.
- **Variant classification/pathogenicity:** Not routinely applicable — genetic testing (single-gene, panel) is **not part of routine clinical evaluation** for EGTCSA given the polygenic model; ClinVar/ACMG-AMP classification frameworks are relevant mainly for the rare monogenic look-alikes that must be excluded (e.g., SCN1A-related disorders) rather than for EGTCSA itself.
- **Allele frequency in population databases:** Not meaningfully defined for a polygenic trait; individual candidate-gene rare variants (e.g., CLCN2 missense variants) have been reported at low frequency in family-based cohorts, not systematically characterized in gnomAD for this specific phenotype.
- **Somatic vs germline:** Germline (heritable) susceptibility model; no somatic mosaicism mechanism reported.
- **Functional consequences:** For CLCN2 candidate variants, functional electrophysiology (whole-cell patch clamp in heterologous expression systems) showed **accelerated channel deactivation kinetics** (gain-of-function-like altered gating) as the proposed mechanism (Saint-Martin 2009, PMID:19191339; Niemeyer, PMID:15252188).
- **Copy number variants / chromosomal abnormalities:** Recurrent CNVs **15q11.2, 15q13.3, 16p13.11 microdeletions** are recommended targets for chromosomal microarray testing in drug-resistant or cognitively-impaired EGTCSA presentations — these are well-established generalized-epilepsy risk CNVs across the IGE spectrum, not EGTCSA-specific.
- **Epigenetic information:** No EGTCSA-specific epigenetic (DNA methylation/histone) data were identified in the sources reviewed.
- **GWAS/polygenic architecture:** The ILAE Consortium on Complex Epilepsies' 2018 (16 loci, *Nat Commun*, PMID for study cohort 14,534 cases/24,218 controls) and 2023 (26 loci, 19 GGE-specific, 29 candidate genes, *Nat Genet* 2023) meta-analyses are the principal genome-wide resources; these studies pool across the four IGE syndromes rather than isolating EGTCSA as a distinct GWAS stratum.

**Suggested gene/ontology annotations for KB curation** (candidate-association tier, not causal):
- hgnc:2020 (CLCN2), hgnc:1402 (CACNB4), hgnc:4075 (GABRA1), hgnc:4088 (GABRD), hgnc:4093 (GABRG2), hgnc:4086 (GABRB3) — verify exact HGNC IDs via lookup before use.
- GO terms: "chloride channel activity" (GO:0005254), "voltage-gated calcium channel activity" (GO:0005245), "GABA-A receptor complex" (GO:1902711).

---

## 5. Environmental Information

- **Environmental factors:** No toxin, chemical, occupational, or infectious cause is implicated in EGTCSA pathogenesis; it is not an acquired/symptomatic epilepsy.
- **Lifestyle factors (functioning as seizure precipitants, not causal agents):**
  - Sleep deprivation (best-established trigger; central to historical nosology "epilepsy with grand mal *on awakening*").
  - Alcohol consumption/withdrawal.
  - Fatigue/physical or psychological stress.
  - Irregular sleep-wake schedules (shift work, jet lag).
- **Infectious agents:** Not applicable — EGTCSA is not an infection-triggered or post-infectious epilepsy syndrome.

---

## 6. Mechanism / Pathophysiology

**Causal chain (thalamocortical network model, shared across IGE syndromes; EGTCSA-specific granularity is limited in the literature):**

1. **Trigger/molecular substrate:** Polygenic dysregulation of ion channels controlling thalamocortical excitability — particularly **T-type calcium channels** (CACNA1G/H), **GABA-A receptor subunits**, and candidate chloride channel (CLCN2) function — sets a lowered seizure threshold.
2. **Cellular process:** Altered **tonic and phasic GABA-A-mediated inhibition** in thalamocortical relay neurons and **T-type calcium current dynamics** in thalamic reticular/relay neurons promote pathological oscillatory burst-firing.
3. **Circuit-level process:** **Cortico-thalamo-cortical hypersynchronization** generates generalized spike-wave discharges (GSWD); in animal absence-epilepsy models (GAERS rats, stargazer mice, Gria4/AMPA-receptor-deficient models), spike-wave discharges originate in layer 5/6 somatosensory cortical neurons and propagate to thalamus via reciprocal cortico-thalamic loops (multiple PMC sources on GAERS/stargazer pathophysiology).
4. **State-dependent modulation:** Sleep-wake transition physiology (changing thalamocortical arousal state, altered GABAergic tone during drowsiness/sleep) interacts with this hyperexcitable network to concentrate seizure occurrence around awakening — the mechanistic basis of the "on awakening" phenotype.
5. **Clinical manifestation:** When network hypersynchronization crosses a threshold sufficient to recruit motor cortex and brainstem tonic/clonic generators (rather than remaining confined to a "typical absence" oscillation), the clinical output is a **generalized tonic-clonic seizure** rather than absence or myoclonus — the phenotypic differentiator that defines EGTCSA within the IGE spectrum is presumably a difference in network engagement/propagation rather than a wholly distinct etiology.

**Molecular pathways:** No disease-specific KEGG/Reactome pathway is curated for EGTCSA; relevant general pathways include GABAergic synapse signaling, voltage-gated calcium channel signaling, and glutamatergic (AMPA/mGluR4) signaling within cortico-thalamic circuits.

**Cellular processes:** Altered neuronal excitability/burst-firing; augmented tonic GABA-A inhibition via astroglial GABA transporter (GAT-1) dysfunction has been demonstrated in GAERS rats and stargazer mice (absence models), raising thalamic ambient GABA and altering tonic inhibition of thalamocortical relay neurons.

**Protein dysfunction:** Where candidate variants are implicated (e.g., CLCN2), the proposed mechanism is **altered channel gating kinetics** (faster deactivation) rather than frank loss-of-function or aggregation.

**Tissue-level:** Neuroimaging in IGE broadly shows subtle structural changes — atrophy in bilateral precentral cortex and thalamus has been reported (PMC11097769); abnormal baseline cerebral blood flow involving basal ganglia/cerebellum circuits has also been described (NBK546611). No gross structural lesion is expected in EGTCSA by definition (idiopathic/genetic, non-lesional).

**Immune system involvement:** Not implicated; EGTCSA is not classified as an autoimmune or neuroinflammatory epilepsy.

**Molecular profiling:** No disease-specific transcriptomic, proteomic, or metabolomic signature has been established for EGTCSA in the literature surveyed; GWAS-nominated candidate genes from the 2023 ILAE meta-analysis (29 genes across GGE loci) represent the current state of pathway-level insight (*Nat Genet* 2023).

**Suggested GO terms:**
- Biological process: "regulation of neuronal synaptic plasticity," "chemical synaptic transmission, GABAergic" (GO:0051932), "regulation of ion transmembrane transport."
- Cellular component: thalamocortical relay neuron, thalamic reticular nucleus interneuron (Cell Ontology terms — verify with OAK).

**Suggested CL terms:** thalamocortical relay neuron, GABAergic interneuron of thalamic reticular nucleus, layer 5/6 pyramidal neuron of somatosensory cortex (from animal-model absence-epilepsy literature; extrapolated to EGTCSA given shared IGE mechanism class — flag as MODEL_ORGANISM-sourced, not directly demonstrated in human EGTCSA tissue).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Central nervous system — specifically the **thalamocortical network** (cerebral cortex + thalamus), rather than a focal lesion.
- **Body system:** Nervous system (UBERON:0001016).
- **Secondary/complication-related systems:** Musculoskeletal (seizure-related fracture/injury), cardiovascular/respiratory (peri-ictal risk relevant to SUDEP — see Outcome section).

**Tissue/cell level:**
- Cerebral cortex (particularly frontal regions — EEG discharges are noted to have "frontal prominence" in generalized IGE, NBK546611) and thalamus (thalamic reticular nucleus, thalamocortical relay nuclei).
- Cell types implicated (from mechanistic/animal-model literature, extrapolated): thalamocortical relay neurons, GABAergic reticular thalamic neurons, cortical pyramidal neurons (layers 5/6).

**Subcellular level:**
- Plasma membrane ion channel complexes: voltage-gated T-type calcium channels, GABA-A receptor complex (synaptic and extrasynaptic/tonic), voltage-gated chloride channel (ClC-2).
- Suggested GO Cellular Component terms: "GABA-A receptor complex" (GO:1902711), "T-type voltage-gated calcium channel complex," "voltage-gated chloride channel complex."

**Localization:** Bilateral, diffuse/generalized network involvement (not lateralized) — consistent with the "generalized" designation; EEG and imaging support bilateral, largely symmetric network engagement, though the ILAE 2022 statement and IGE reviews note that "generalized" does not mean uniform involvement of all neurons — specific thalamocortical networks are engaged with sparing of others (PMC11097769).

**Suggested UBERON terms:** UBERON:0001890 (thalamus), UBERON:0000956 (cerebral cortex), UBERON:0002771 (frontal cortex), UBERON:0001872 (thalamic reticular nucleus, verify exact UBERON ID).

---

## 8. Temporal Development

**Onset:**
- Typical age of onset: **10–25 years**, with 80% beginning in the second decade of life; overall reported range 5–40 years (epilepsydiagnosis.org; epilepsy.com).
- Median age of onset in a prospective cohort (Beydoun 2024, n=89): **16 years**.
- Onset pattern: Not acute/sudden in the sense of an inciting event — seizures typically begin without an identifiable precipitating illness, though the first seizure is often associated with sleep deprivation (e.g., after an all-nighter, exam period, or party involving alcohol and sleep loss).
- A distinct **childhood-onset subtype** ("childhood-only epilepsy with generalized tonic-clonic seizures") has been described as a well-defined variant with different remission characteristics (Sciencedirect 2019 report, S0920121119300142) — full text was not accessible during this research, but its existence indicates age-of-onset heterogeneity within the broader EGTCSA phenotype.

**Progression:**
- Disease course is generally **stable/non-progressive** rather than a staged/degenerative process typical of neurodegenerative disorders.
- Seizure frequency is typically **low** (infrequent GTCS) rather than the high-frequency pattern seen in CAE (daily absences) or JME (frequent myoclonus).
- Course pattern: **Episodic**, strongly modulated by state factors (sleep-wake cycle, sleep deprivation, alcohol) rather than continuously active; can be **drug-responsive** with long stretches of seizure freedom on treatment.
- Duration: For many patients the disorder is not lifelong — a substantial fraction achieve durable remission and can discontinue medication (see Outcome section), though relapse after withdrawal is common enough that timing and method of withdrawal materially affect outcome.

**Patterns:**
- **Remission:** Treatment-associated remission is common; in the Beydoun 2024 cohort, 56% who attempted ASM discontinuation after a median 3 years of treatment maintained seizure freedom, while 44% relapsed.
- **Critical periods:** Adolescence/early adulthood represents the principal period of both seizure onset and diagnostic ascertainment; the "on awakening" chronotype identifies a specific circadian vulnerability window (the 1–2 hours following waking) as a within-day critical period for seizure occurrence.

---

## 9. Inheritance and Population

**Epidemiology:**
- IGE as a whole accounts for **~20% of all epilepsies** but receives disproportionately little research attention ("less than 1% of scientific literature," PMC11097769/PMID:38165295).
- Global epilepsy prevalence (all types): ~65 million people worldwide; active epilepsy prevalence ~6.38 per 1,000 persons; US incidence of generalized epilepsies ~7.7 per 100,000 person-years (NBK546611).
- **EGTCSA-specific proportions** (substantial variability by cohort and diagnostic era):
  - Classic Janz series: "pure" GTCS-on-awakening epilepsy in **~10%** of 4,816 epilepsy patients, with a mixed GTCS + absence/myoclonus phenotype in a further 17%.
  - Reported range across studies: **0–17%** of patients with epileptic seizures.
  - Among IGE-diagnosed cohorts specifically: **12%** of 253 IGE patients in one series; **31%** of IGE patients in the Beydoun 2024 prospective cohort (n=89/287 approx.); **65.4%** was reported as the most common syndrome in one adult-onset IGE cohort; **5.8%** (40/692) in a population-based cohort.
  - Among a general IGE cohort of 601 patients (Asadi-Pooya & Homayoun 2020, PMID:32030724), **86% (516/601)** had GTCS as part of their presentation (not restricted to "alone").

**Inheritance pattern:** **Complex/polygenic** — not Mendelian (autosomal dominant/recessive/X-linked/mitochondrial). Genetic counseling is framed around empiric recurrence risk in relatives rather than single-gene transmission probability.

**Penetrance/expressivity:** Not meaningfully quantifiable under the polygenic model in the way it would be for a monogenic disorder; family members with a positive family history typically manifest **other IGE phenotypes** (absence, myoclonic, or mixed GTCS syndromes) rather than EGTCSA specifically, consistent with a shared underlying genetic generalized epilepsy liability rather than syndrome-specific inheritance.

**Genetic anticipation, germline mosaicism, founder effects:** Not established/applicable for this polygenic syndrome; these concepts are more relevant to the rare monogenic mimics that must be excluded.

**Consanguinity:** Not specifically implicated (consistent with the polygenic, non-Mendelian model — contrasts with recessive monogenic epilepsies where consanguinity is a recognized risk factor).

**Population demographics:**
- **Sex ratio:** Both sexes equally affected (epilepsydiagnosis.org, epilepsy.com); no strong sex skew reported, unlike some other IGE subtypes.
- **Geographic distribution:** No specific endemic pattern reported; EGTCSA is described across multiple international cohorts (Lebanon/Beydoun, Iran/Asadi-Pooya, European series underlying the ILAE classification), consistent with a globally distributed genetic generalized epilepsy without strong geographic restriction (in contrast to some infection-associated epilepsies).
- **Age distribution:** Concentrated in adolescence/young adulthood at onset (see Temporal Development); a childhood-onset variant is separately described.

---

## 10. Diagnostics

**Clinical tests / EEG (the primary diagnostic modality):**
- **Interictal EEG:** Generalized spike-wave or polyspike-wave discharges at **3–5.5 Hz**, seen in about half of patients — often only apparent during sleep. Focal spike-wave can occur but persistent, consistent focal findings should prompt evaluation for a structural lesion. Slow spike-wave activity **below 2.5 Hz is absent** and its presence suggests an alternative diagnosis (e.g., Lennox-Gastaut spectrum) (epilepsydiagnosis.org EEG page).
- **Activation procedures:** EEG abnormality is enhanced by **sleep deprivation**, drowsiness, and sleep; generalized spike-wave becomes fragmented (and can spuriously appear focal) under these conditions. An intermittent **photoparoxysmal response** to photic stimulation may be seen.
- **Ictal EEG:** Often obscured by movement artifact; shows generalized fast rhythmic spikes during the tonic phase, spike bursts time-locked to clonic jerks, followed by post-ictal slow-wave activity.
- **Diagnostic yield over serial studies (Beydoun 2024):** Generalized spike-wave discharges present on the **initial** EEG in 88% of patients; photoparoxysmal response present in 20% initially, rising to 35% on follow-up EEGs; repeat EEG increased overall diagnostic yield to **96.6%** by the second recording — underscoring the value of serial/repeat EEG (including sleep-deprived recordings) when the first study is non-diagnostic.
- **Background EEG:** Normal background with no generalized slowing expected; focal slowing should raise suspicion of a structural abnormality and prompt neuroimaging.

**Neuroimaging:** **MRI/MRA** is the standard initial imaging study, primarily to **exclude structural lesions** — by definition, EGTCSA/IGE shows no lesion on conventional imaging. Research-grade quantitative imaging in the broader IGE literature has described bilateral precentral cortex and thalamic atrophy and altered resting cerebral blood flow (basal ganglia/cerebellar circuits), but these are not part of routine clinical diagnosis.

**Genetic testing:** **Not part of routine clinical evaluation** given the polygenic model. **Chromosomal microarray** is reserved for atypical presentations — specifically **drug-resistant** EGTCSA or cases with **intellectual disability** — to screen for recurrent pathogenic CNVs (15q11.2, 15q13.3, 16p13.11 microdeletions).

**Clinical diagnostic criteria:** Per the ILAE 2022 position statement (Hirsch et al., *Epilepsia* 2022;63:1475–1499, doi:10.1111/epi.17236), EGTCSA is one of four defined IGE syndromes, diagnosed on the combination of: (1) generalized tonic-clonic seizures as the sole seizure type, (2) EEG showing generalized spike-wave/polyspike-wave activity, (3) age-appropriate onset window, and (4) exclusion of absence and myoclonic seizure types (which would instead point to JAE, JME, or a mixed IGE phenotype).

**Differential diagnosis** (drawing on general IGE differential, NBK546611):
- **Focal (impaired-awareness) epilepsy with secondarily generalized tonic-clonic seizures** — distinguished by focal EEG onset, longer seizure duration with aura, and (if present) an MRI lesion.
- **Syncope** (cardiac arrhythmia, vasovagal, orthostatic) causing convulsive syncope — ECG and cardiac workup required to exclude.
- **Psychogenic non-epileptic seizures (PNES)** — no EEG correlate; important because 5–40% of PNES patients also have true epilepsy.
- **GEFS+ spectrum disorders** — distinguished by a history of febrile seizures and often (though not always) an identifiable sodium-channel-gene variant.
- **Other IGE syndromes (JME, JAE)** — distinguished by co-occurrence of myoclonic jerks or absence seizures, which by definition exclude "alone" GTCS classification.
- **De novo absence status epilepticus of late onset** — an elderly-onset IGE-spectrum presentation, distinct from EGTCSA's adolescent-onset pattern.

**Screening:** No population-based or newborn screening program applies (not detectable pre-symptomatically via a defined biomarker); clinical vigilance for a first unprovoked GTCS in the setting of sleep deprivation in an adolescent/young adult is the practical "screening" trigger for EEG referral.

---

## 11. Outcome/Prognosis

**Treatment response and remission (Beydoun et al. 2024, *Epilepsia Open*, prospective cohort, n=89):**
- Seizure **recurrence with treatment: 13.5%**, versus **73.3% recurrence without treatment** (p<0.00001) — demonstrating strong ASM efficacy in this syndrome.
- Of 50 patients who attempted ASM discontinuation after a median **3 years** of treatment: **56% maintained seizure freedom**, **44% experienced recurrence**.
- **Predictors of relapse after withdrawal:** patient-initiated (vs physician-directed) tapering, and a **mixed circadian seizure pattern** (both diurnal and nocturnal seizures) independently predicted higher recurrence risk.
- **Predictors of successful withdrawal:** physician-directed tapering, absence of generalized spike-wave discharges on EEG at the time of withdrawal decision, and a purely diurnal or purely nocturnal (non-mixed) seizure pattern.
- One review cites a broader estimate that **~60% of EGTCSA patients recur** after medication withdrawal, in a similar range to JME (where recurrence after withdrawal exceeds 75%) but generally less relapse-prone than JME (PMC11097769).

**Mortality / SUDEP:**
- SUDEP (Sudden Unexpected Death in Epilepsy) risk in IGE overall is reported to be broadly **similar to focal epilepsy cohorts**, although focal epilepsy is more often drug-resistant; **uncontrolled GTCS is the single leading SUDEP risk factor**, yet notably most SUDEP deaths occur in patients with relatively **infrequent** GTCS — an important nuance for risk communication (search synthesis from SUDEP literature). Some sources (NBK546611) describe SUDEP risk as **lower in IGE** compared to other epilepsy categories overall, and lower in females.

**Morbidity/complications:**
- Seizure-related injury risk (fractures, burns, concussion) of **40–60%** at 12-month follow-up is reported for recurrent generalized seizures broadly (NBK546611) — directly relevant given EGTCSA seizures are convulsive by definition.
- **Psychiatric comorbidity** contributes to reduced quality of life and (in the broader epilepsy population) to premature mortality, though one large cohort found that after adjustment, only self-harm and substance use disorders (not psychiatric comorbidity broadly) were independently associated with elevated all-cause mortality (PMC9433706).
- **Drug-resistant course:** A subset of IGE patients (up to ~30% cited for JME; comparable figures not isolated for EGTCSA specifically) fail to achieve seizure freedom and require polytherapy or neuromodulation.

**Prognostic factors:** EEG pattern (presence/absence of GSWD), circadian seizure pattern (pure vs mixed diurnal/nocturnal), and method of ASM withdrawal (physician-directed vs patient-initiated) are the best-documented prognostic modifiers specific to this syndrome (Beydoun 2024).

---

## 12. Treatment

**Pharmacotherapy — first-line and alternatives:**
- **Valproate (sodium valproate/valproic acid)** is the most effective and most commonly prescribed agent for EGTCSA/GTCS-predominant IGE — used in **68.2%** of patients in the Beydoun 2024 cohort; broader IGE literature cites ~75% seizure freedom on valproate monotherapy (NBK546611). Valproate additionally prevents absence status epilepticus and is effective in photosensitive patients, but carries significant **teratogenicity** (7–10% major malformation risk overall; **25.2%** risk reported at doses >1,450 mg/day) and is generally avoided in women of childbearing potential when alternatives are viable.
- **Levetiracetam** — second most-used agent in the Beydoun cohort (21.2%); preferred in women of reproductive age due to low teratogenic risk (~1–3%), and generally well-tolerated.
- **Lamotrigine** — effective for GTCS, better-tolerated than valproate, low teratogenic risk; requires slow titration due to Stevens-Johnson syndrome risk, and its metabolism is inhibited by co-administered valproate (requiring dose adjustment).
- **Topiramate** — cited specifically as effective for "tonic-clonic seizures alone" in the IGE spectrum (NBK546611 subtype table).
- **Phenytoin** — used in a small minority (<5%) in the Beydoun cohort, though generally regarded with caution/relative avoidance in IGE broadly.
- **Perampanel** (AMPA receptor antagonist) — used for GTCS, including drug-resistant cases.
- **Cenobamate** (FDA-approved 2019) and **brivaracetam** — cited as options for drug-resistant IGE/generalized seizures.

**Drugs to avoid:**
- **Carbamazepine and oxcarbazepine** — documented to worsen myoclonic and absence seizures in the IGE spectrum; may be used cautiously specifically for GTCS-alone presentations in refractory cases but are not first-line.
- **Phenytoin and vigabatrin** — generally contraindicated across IGE.

**Non-pharmacological/procedural:**
- **Vagus nerve stimulation (VNS)** — well-tolerated option for medically intractable IGE.
- **Deep brain stimulation** (e.g., centromedian thalamic nucleus), **responsive neurostimulation**, **transcranial magnetic stimulation** — emerging/investigational neuromodulation approaches for drug-resistant generalized epilepsy.
- **Ketogenic diet** — established since 1921 for refractory epilepsy broadly; in one cited IGE cohort, 48% (41/86 adults) achieved >50% seizure reduction on ketogenic diet.

**Supportive/behavioral:**
- **Sleep hygiene counseling** (regular sleep schedule, avoidance of sleep deprivation) is a cornerstone of management given the syndrome's defining sensitivity to sleep-wake state.
- **Alcohol avoidance** and general lifestyle counseling regarding seizure precipitants.
- Safety counseling: avoidance of unsupervised swimming, heights, and heavy machinery; jurisdiction-specific driving restrictions.

**Treatment strategy/withdrawal:** Given the recurrence data above, **physician-directed (not patient-initiated) tapering**, ideally after documented normalization of EEG (loss of GSWD) and a pure (non-mixed) circadian seizure pattern, is the evidence-based approach to attempting ASM discontinuation after a period (median ~3 years in the cited cohort) of seizure freedom.

**Suggested NCIT terms for KB curation:** NCIT:C15986 (Pharmacotherapy) as the generic treatment_term, with therapeutic_agent bound to CHEBI terms for valproate (CHEBI:39867 valproic acid or its salt form), levetiracetam (CHEBI:6437), lamotrigine (CHEBI:6367), topiramate (CHEBI:9698), perampanel (verify CHEBI ID) — confirm exact CHEBI IDs/labels via OAK before curating. NCIT:C15238 (Gene Therapy) is not applicable; NCIT device/neuromodulation term would apply to VNS (no strong NCIT clinical-action term readily available — verify).

---

## 13. Prevention

- **Primary prevention:** No disease-modifying primary prevention exists for the underlying polygenic susceptibility. The practical "primary prevention" applicable to this syndrome is **avoidance of known precipitants** (sleep deprivation, alcohol, fatigue) in individuals with a known genetic generalized epilepsy predisposition or family history, to reduce the likelihood of triggering a first or subsequent seizure.
- **Secondary prevention:** Early recognition and EEG-based diagnosis after a first unprovoked GTCS (especially in an adolescent following sleep deprivation) allows prompt initiation of ASM therapy, which the Beydoun 2024 data show reduces recurrence from 73.3% (untreated) to 13.5% (treated).
- **Tertiary prevention:** Structured medication management (physician-directed withdrawal timing, EEG-guided decision-making) reduces relapse risk after a period of seizure freedom, as detailed in Outcome/Prognosis above.
- **Immunization:** Not applicable (non-infectious).
- **Genetic counseling:** Given the polygenic/complex inheritance model, counseling for at-risk relatives focuses on empiric recurrence risk rather than single-gene predictive testing; targeted chromosomal microarray is reserved for atypical (drug-resistant or intellectually-impaired) presentations rather than population screening.
- **Behavioral interventions:** Sleep hygiene and alcohol moderation counseling are the most directly evidence-supported prevention measures specific to this syndrome's sleep-wake-triggered phenotype.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal disease specifically corresponding to "epilepsy with generalized tonic-clonic seizures alone" as an ILAE-defined human syndrome was identified in this research. Idiopathic/genetic generalized epilepsy is recognized in domestic dogs (e.g., certain breeds with heritable idiopathic epilepsy showing generalized seizures), but breed-specific correspondence to this exact human syndromic entity was not established in the sources reviewed and should be independently verified (e.g., via OMIA) before curation.

---

## 15. Model Organisms

No mouse or other animal model was identified in the literature reviewed that specifically and selectively recapitulates "EGTCSA" as a discrete syndromic entity (i.e., a model producing generalized tonic-clonic seizures as the *sole* phenotype, on an awakening-linked circadian pattern, without absence or myoclonic seizures). Instead, the field relies on **shared thalamocortical/absence-epilepsy models** that illuminate the broader IGE mechanism class from which EGTCSA is drawn:

- **GAERS rats (Genetic Absence Epilepsy Rats from Strasbourg)** — genetic model showing spontaneous spike-wave discharges; astroglial GAT-1 dysfunction raises thalamic ambient GABA, altering tonic GABA-A inhibition of thalamocortical relay neurons.
- **Stargazer mice** — stargazin (Cacng2) deficiency causing loss of AMPA receptors at excitatory synapses onto parvalbumin-positive interneurons, implicating glutamatergic feed-forward inhibition failure in spike-wave generation; also show altered GAT-1-mediated thalamic GABA tone (same mechanism family as GAERS).
- **GABA-A receptor γ2(R43Q) knock-in mice** — model absence epilepsy and febrile seizures with abolished tonic inhibition, relevant to the broader GABA-A receptor gene family (GABRG2) implicated across IGE.
- **Succinic semialdehyde dehydrogenase (SSADH)-deficient mice** — show aberrant GABA-A-receptor-mediated inhibition in cortico-thalamic networks, a metabolic-genetic model informative for GABAergic dysfunction mechanisms.

**Model limitations relevant to EGTCSA specifically:** All of the above are principally **absence-seizure models** (spike-wave discharge with behavioral arrest), not generalized-tonic-clonic-seizure-predominant models, and none incorporate the sleep-wake/circadian "on-awakening" triggering pattern that clinically defines EGTCSA. This represents a **notable translational gap**: the mechanistic literature for thalamocortical hypersynchronization is well developed for absence seizures but has not been specifically extended to model the awakening-triggered GTCS-alone phenotype. Any curation connecting these rodent models to EGTCSA pathophysiology should be flagged as **MODEL_ORGANISM evidence for the shared IGE/thalamocortical mechanism class**, not as direct recapitulation of the EGTCSA clinical syndrome, and a `HUMAN_MODEL_MISMATCH`-style caveat is warranted given the mismatch between absence-predominant rodent phenotypes and the GTCS-alone human phenotype.

---

## Summary of Key Evidence Gaps for Curation

1. **No monogenic cause** — this is a genuinely polygenic syndrome; curators should not force a single causal-gene model.
2. **CLCN2's role is contested** (retracted early paper, inconsistent replication) — cite with appropriate hedging/PARTIAL support classification if used.
3. **EGTCSA-specific GWAS/pathway data are sparse** — most genomic evidence is at the IGE/GGE class level, not syndrome-specific.
4. **No animal model directly recapitulates the "alone" + "on-awakening" phenotype** — available models are absence-epilepsy-focused; use with explicit HUMAN_MODEL_MISMATCH framing.
5. **MONDO ID** should be double-checked (MONDO:0005754 vs. a potentially more specific term) and **Orphanet ORPHA:698005** confirmed against the live Orphanet record before finalizing identifiers in the KB entry.

---

## Sources

- [ILAE definition of the Idiopathic Generalized Epilepsy Syndromes: Position statement (Hirsch et al., Epilepsia 2022)](https://onlinelibrary.wiley.com/doi/full/10.1111/epi.17236)
- [ILAE Proposed Classification of Idiopathic Generalized Epilepsies](https://www.ilae.org/guidelines/definition-and-classification/proposed-classification-and-definition-of-epilepsy-syndromes/proposed-classification-idiopathic-generalized-epilepsies)
- [EpilepsyDiagnosis.org: EGTCSA Overview](https://www.epilepsydiagnosis.org/syndrome/egtcsa-overview.html)
- [EpilepsyDiagnosis.org: EGTCSA Genetics](https://www.epilepsydiagnosis.org/syndrome/egtcsa-genetics.html)
- [Prospective study of epilepsy with generalized tonic–clonic seizures alone (Beydoun et al., Epilepsia Open 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11296088/)
- [Orphanet: Epilepsy with generalized tonic-clonic seizures alone (ORPHA:698005)](https://www.orpha.net/en/disease/detail/698005)
- [Epilepsy with generalized tonic-clonic seizures alone — MedLink Neurology](https://www.medlink.com/articles/epilepsy-with-generalized-tonic-clonic-seizures-alone)
- [Idiopathic Generalized Epilepsy: Misunderstandings, Challenges, and Opportunities (PMC11097769, PMID:38165295)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11097769/)
- [Idiopathic (Genetic) Generalized Epilepsy — StatPearls (NBK546611)](https://www.ncbi.nlm.nih.gov/books/NBK546611/)
- [Two novel CLCN2 mutations accelerating chloride channel deactivation are associated with idiopathic generalized epilepsy (Saint-Martin et al., Hum Mutat 2009, PMID:19191339)](https://pubmed.ncbi.nlm.nih.gov/19191339/)
- [Mutations in the CLCN2 gene are a rare cause of idiopathic generalized epilepsy syndromes (PMID:16932951)](https://pubmed.ncbi.nlm.nih.gov/16932951/)
- [No evidence for a role of CLCN2 variants in idiopathic generalized epilepsy (Nature Genetics)](https://www.nature.com/articles/ng0110-3)
- [Genome-wide mega-analysis identifies 16 loci in the common epilepsies (Nat Commun 2018)](https://www.nature.com/articles/s41467-018-07524-z)
- [GWAS meta-analysis of over 29,000 people with epilepsy identifies 26 risk loci (Nat Genet 2023)](https://www.nature.com/articles/s41588-023-01485-w)
- [Epilepsy with grand mal on awakening and sleep-waking cycle (Janz, Clin Neurophysiol 2000, PMID:10996562)](https://pubmed.ncbi.nlm.nih.gov/10996562/)
- [Tonic-clonic seizures in idiopathic generalized epilepsies: Prevalence, risk factors, and outcome (Asadi-Pooya & Homayoun, Acta Neurol Scand 2020, PMID:32030724)](https://pubmed.ncbi.nlm.nih.gov/32030724/)
- [Childhood-only epilepsy with generalized tonic-clonic seizures — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0920121119300142)
- [Premature mortality in epilepsy and the role of psychiatric comorbidity — The Lancet 2013](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(13)60899-5/fulltext)
- [Psychiatric comorbidities and all-cause mortality in epilepsy: nationwide cohort study (PMC9433706)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9433706/)
- [Mondo Disease Ontology — idiopathic generalized epilepsy (BioPortal, MONDO:0005579)](https://bioportal.bioontology.org/ontologies/MONDO?p=classes&conceptid=MONDO:0005579)
- [Epilepsy disease classification: a community effort to enhance the Mondo Disease Ontology (Database, 2023)](https://academic.oup.com/database/article/doi/10.1093/database/baag004/8487729)