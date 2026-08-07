---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T11:33:22.253029'
end_time: '2026-07-18T11:38:39.413426'
duration_seconds: 317.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy with Myoclonic-Atonic Seizures
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
  - claude-opus-4-8
  web_search_requests: 10
  num_turns: 16
  total_cost_usd: 1.6706177500000003
  session_id: 6dd2fa47-2273-4036-8a6e-fed0f3159678
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epilepsy with Myoclonic-Atonic Seizures
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Epilepsy with Myoclonic-Atonic Seizures** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

Alright, I've got a solid haul of real, verifiable sources with PMIDs and the ontology IDs. Here's the full write-up.

---

# Research Report: Epilepsy with Myoclonic-Atonic Seizures (Doose Syndrome)

sup Harry — so this is one of those diseases where the name has been through more costume changes than a stage actor. "Myoclonic-astatic epilepsy," "myoclonic-atonic epilepsy (MAE)," "Doose syndrome," and now the ILAE-blessed **epilepsy with myoclonic-atonic seizures (EMAtS / EMAS)**. Same kid falling down, different label decade. The thread that ties the whole thing together is a very specific seizure — the *myoclonic-atonic* — a little muscle jerk immediately followed by the floor dropping out from under all your muscle tone, so the child pitches forward or collapses. Think of a marionette where someone yanks a string and then, in the same breath, cuts all of them.

A quick honesty note up front, since this feeds a curation entry: everything below is anchored to real papers I pulled and verified titles/PMIDs for. But per your own SOP, **every snippet needs to be checked as an exact substring against the fetched abstract before it goes in an evidence block** — I'm giving you the quotes I saw in fetched content, but treat the paraphrased bits as leads, not gospel. I've flagged the ontology IDs that need an OAK pass too.

---

## 1. Disease Information

EMAtS is a **childhood-onset generalized epilepsy syndrome** defined by the presence of myoclonic-atonic (and often pure atonic, myoclonic, absence, and generalized tonic-clonic) seizures, arising in a previously typically-developing young child. It sits in that fascinating middle zone between the "self-limited" epilepsies (kid grows out of it, no scars) and the "developmental and epileptic encephalopathies" (the seizures themselves chew up development) — and which side a given child lands on is genuinely hard to call at onset. The 2025 Lancet Neurology review put it plainly:

> "Although two-thirds of children attain remission from seizures without cognitive or behavioural sequelae, some continue to have drug-resistant seizures, intellectual disability, and behavioural problems." — Guerrini, Scheffer & Balestrini, *Lancet Neurol* 2025;24:348–360, **PMID:40120618**

**Key identifiers:**
- **Orphanet:** ORPHA:1942 (solid)
- **OMIM:** 616421 (MYOCLONIC-ATONIC EPILEPSY; MAE — the *GABRG2*-associated molecular entry). Note OMIM treats this as a molecularly-defined slot, not the whole clinical syndrome.
- **MONDO:** search surfaced `MONDO:0014633` (MalaCards) but I could **not** verify this against OAK — ⚠️ **run `runoak -i sqlite:obo:mondo` before trusting it.** The classic "myoclonic-astatic epilepsy" MONDO node may differ; verify before setting `disease_term`.
- **ICD-10:** G40.4 (other generalized epilepsy and epileptic syndromes); **ICD-11:** 8A61.x (generalized epilepsies)
- **MeSH:** "Myoclonic-Astatic Epilepsy" / Doose syndrome (Epilepsies, Myoclonic subtree)

**Synonyms:** Doose syndrome; myoclonic-astatic epilepsy (MAE); myoclonic astatic epilepsy of early childhood; epilepsy with myoclonic-atonic seizures (EMAtS/EMAS). "Astatic" and "atonic" are used interchangeably in the drop-attack sense.

**Data derivation:** Almost entirely **disease-level aggregated** — small-to-medium retrospective clinical cohorts and case series, not EHR-mined patient records. The largest recent evidence base is multicenter retrospective cohorts (dozens to a few hundred children).

---

## 2. Etiology

Here's the honest headline: **most cases are still "genetic, cause unknown."** Doose himself pegged it as idiopathic/genetic generalized epilepsy, and that framing has held up — a substantial fraction of kids have a family history of epilepsy or febrile seizures, consistent with a **complex/polygenic** background rather than one broken gene. Layered on top of that polygenic soup is a growing list of **monogenic** causes that produce an EMAtS-like picture.

**Primary causal factors:**
- **Genetic (monogenic subset):** *SLC6A1* is the standout MAE gene — loss of function in the GABA transporter GAT-1. *GABRG2*, *SCN1A*, *SCN1B*, *SLC2A1* (GLUT1), *STX1B*, *CHD2*, *SYNGAP1*, *KCNA2*, and others show up across cohorts. The 2015 discovery paper:
  > "Targeting resequencing of 644 individuals... six SLC6A1 mutations in seven individuals, all of whom have epilepsy with myoclonic-atonic seizures (MAE)... pathogenic mutations occurred in 6/160 individuals with MAE, accounting for ∼4% of unsolved MAE cases." — Carvill et al, *Am J Hum Genet* 2015, **PMID:25865495**
- **Genetic (polygenic):** the majority — inferred from twin/family aggregation, no single Mendelian locus.
- **Metabolic:** ~5% are **GLUT1 deficiency (SLC2A1)** — this one *matters clinically* because it's treatable with the ketogenic diet, so it must be actively excluded.
- **Environmental/infectious:** none established as causal. This is not an acquired or structural epilepsy — normal MRI is part of the definition.

**Risk factors:** young age (2–5 yr window), male sex, and prior febrile seizures (~25% of kids). Family history of epilepsy is a susceptibility signal.

**Protective factors / gene-environment interactions:** not well characterized. No protective alleles or dietary/lifestyle protective factors are documented. GLUT1's ketogenic-diet responsiveness is the closest thing to a gene-treatment interaction, but that's therapeutic, not preventive.

---

## 3. Phenotypes

The defining move is the **myoclonic-atonic seizure** — a symmetric myoclonic jerk (often trunk/shoulders/arms) immediately followed by loss of tone, producing a **drop attack** (falls, head nods, buckling knees). But EMAtS is a *seizure buffet*, and different types dominate at different points. From the Japanese Doose cohort (Nickels-style breakdown), **PMID:32913952**:

**At onset:** generalized tonic-clonic 41%, tonic seizures 38%, myoclonic 24%, myoclonic-atonic 14%.
**During course:** myoclonic 48%, absence 45%, atonic 24%, nonconvulsive status epilepticus 14%.

| Phenotype | Type | HPO suggestion (⚠️ verify w/ OAK) | Frequency | Onset |
|---|---|---|---|---|
| Myoclonic-atonic seizure (drop attack) | Clinical sign | HP:0032792 "Myoclonic-atonic seizure" (verify) | Mandatory / defining | 2–5 yr |
| Atonic seizure | Clinical sign | HP:0010819 Atonic seizure | Frequent (~24%) | early childhood |
| Myoclonic seizure | Clinical sign | HP:0032794 Myoclonic seizure | Frequent (48%) | early childhood |
| Absence seizures (typical/atypical) | Clinical sign | HP:0002121 Absence seizure / HP:0011153 | Frequent (~45%) | early childhood |
| Generalized tonic-clonic seizure | Clinical sign | HP:0002069 Bilateral tonic-clonic seizure | Common (often first sign, 41%) | early childhood |
| Nonconvulsive status epilepticus | Clinical sign | HP:0011153/HP:0002133 (verify) | Occasional (~14%) | course |
| Febrile seizures (preceding) | Clinical sign | HP:0002373 Febrile seizure | ~25% | infancy |
| Intellectual disability / cognitive impairment | Lab/functional | HP:0001249 Intellectual disability | ~40–58% (variable) | after onset |
| Global developmental delay | Behavioral | HP:0001263 Global developmental delay | subset; key prognostic | at/after onset |
| Developmental regression/stagnation | Behavioral | HP:0002376 Developmental regression | during active phase | active phase |
| Ataxia | Clinical sign | HP:0001251 Ataxia | subset | active phase |
| ADHD | Behavioral | HP:0007018 ADHD | ~40% (most common comorbidity) | course |

**Characteristics:** onset **6 months–6 (some say 8) years, peaking 2–4 yr**; development typically **normal before onset in ~two-thirds**; severity **highly variable** (self-limited → drug-resistant DEE); course **episodic/fluctuating**, sometimes with "stormy" onset periods of near-continuous drops. From epilepsydiagnosis.org: *"Developmental stagnation or regression is typically seen during the phase of active seizures."*

**Quality of life:** driven by drop attacks (injury risk, helmet use), cognitive/behavioral load, and drug resistance in the unlucky third. No EMAtS-specific EQ-5D/SF-36 data surfaced — flag as **not available**.

---

## 4. Genetic / Molecular Information

The molecular story is a "many roads into the same town" situation, and the roads mostly run through **GABAergic inhibition** and **ion channels**.

**Marquee gene — *SLC6A1* (GAT-1, HGNC verify `hgnc:11042`):**
- Encodes the sodium/chloride-dependent GABA transporter type 1, which vacuums GABA back out of the synaptic and extrasynaptic space.
- Variant classes: **missense (most), nonsense, frameshift, splice, and whole-gene/translocation** — converging on **loss of function** (reduced GABA reuptake, but also protein misfolding/destabilization and ER retention for some missense alleles).
- ~4% of unsolved MAE (Carvill 2015); most common single-gene MAE cause. De novo dominant, mostly.

**Other genes across cohorts:**
- ***GABRG2*** (GABA-A receptor γ2 subunit) — OMIM 616421's assigned gene; GABAergic again.
- ***SCN1A / SCN1B*** (sodium channels) — overlap with the Dravet spectrum; a caution flag for named-entity confusion.
- ***SLC2A1* (GLUT1)** — ~4–5%; loss of function → CNS glucose-transport failure; **the treatable one**.
- ***STX1B*** — syntaxin-1B, presynaptic vesicle fusion; haploinsufficiency causes MAE-like epilepsy.
- ***CHD2, SYNGAP1, KCNA2, HNRNPU*** and, in the newest cohort (**PMID:41523187**), a widened net: *ANKRD11, CSNK2B, NEXMIF, POLR3B*, plus novel associations *KMT2E, POGZ, SHANK3, YWHAG*. That cohort's yield:
  > "15/39 patients (38.5%) who underwent next-generation sequencing had pathogenic variants."

So NGS yield in a well-selected modern cohort is roughly **a third to 40%**, but the classic candidate-gene panels (SCN1A/GABRG2/SLC2A1) are individually **low-yield**.

**Chromosomal:** microdeletions (e.g., involving *SCN1A*, *STS*) and a reported 4q21.22-q21.23 microduplication; balanced translocations disrupting *SLC6A1*.

**Epigenetics / modifiers:** no established EMAtS-specific methylation signature or modifier gene — **not available**. The polygenic background *is* effectively the modifier layer, but it's uncharacterized at the locus level.

**Ontology anchors:** GO:0015812 (GABA transport), GO:0051932 (GABAergic synaptic transmission), GO:0007214 (GABA signaling pathway), GO:0005328 (neurotransmitter:sodium symporter activity).

---

## 5. Environmental Information

Short section, and that's the finding: **EMAtS has no established environmental, lifestyle, toxic, or infectious cause.** Febrile seizures precede it in ~25%, but fever is a trigger/marker of susceptibility, not an environmental etiology. No occupational, dietary, or pollution links. Normal neuroimaging and no acquired insult are baked into the diagnostic definition. Mark **§5 = not applicable / not available**.

---

## 6. Mechanism / Pathophysiology

The through-line is **failure of GABAergic inhibition in the thalamocortical circuitry**, tipping the cortex toward generalized hypersynchronous discharge.

**Causal chain (canonical, SLC6A1 exemplar):**
1. **Trigger:** loss-of-function variant in GAT-1 (*SLC6A1*) → GABA not efficiently cleared from synaptic/extrasynaptic space. (Counterintuitively, *more* ambient GABA can be pro-seizure here because tonic GABA-A currents and receptor desensitization dysregulate thalamocortical rhythms — the same paradox seen in absence epilepsy.)
2. **Cellular:** GAT-1 lives mainly on **astrocytes and GABAergic nerve terminals**, so the defect degrades the astrocyte-neuron GABA homeostasis loop. From the mechanism literature: *"GAT-1... is expressed mainly in astrocytes and the terminals of GABAergic neurons, where it regulates GABA levels in the synaptic and extrasynaptic compartments."*
3. **Circuit:** dysregulated tonic inhibition → abnormal **thalamocortical oscillation** → generalized **2–4 Hz spike-and-slow-wave / polyspike-wave discharges** (the EEG hallmark). *Gat1*-null mice recapitulate spontaneous spike-wave discharges — a nice cross-species anchor (**PMID:25865495**).
4. **Clinical output:** the spike drives the **myoclonic jerk**, the trailing slow wave drives the **atonic drop**. Absence and GTC seizures emerge from the same generalized-network instability.

**GLUT1 branch:** *SLC2A1* LOF → impaired glucose flux across the blood-brain barrier → chronic cerebral energy deficit → seizures + movement/cognitive features. Mechanistically distinct (an **energy-metabolism** failure, not a channel/transporter-of-GABA failure), which is exactly why the ketogenic diet — supplying ketone bodies as an alternate brain fuel — works so well for it.

**Involved cell types / regions:** CL:0000617 (GABAergic neuron), CL:0000127 (astrocyte), CL:0000498 (inhibitory interneuron); UBERON:0000956 (cerebral cortex), UBERON:0001897 (thalamus), UBERON:0002037 (cerebellum, for the ataxia thread). No immune, fibrotic, or neurodegenerative mechanism — this is a **channelopathy/synaptopathy of inhibition**, a good conformance candidate for your `epilepsy_excitation_inhibition_imbalance` module (`#Excitation-Inhibition Imbalance`).

---

## 7. Anatomical Structures Affected

- **Organ/system:** central nervous system, generalized — no focal lesion. Primary structure is the **thalamocortical network** (cortex + thalamus). Secondary: cerebellar circuits (ataxia).
- **Tissue/cell:** cortical and thalamic **neurons**, **GABAergic interneurons**, and **astrocytes** (GAT-1 expression site).
- **Subcellular (GO Cellular Component):** GO:0045202 (synapse), GO:0043195 (terminal bouton / presynaptic terminal), GO:0005886 (plasma membrane — where GAT-1/channels sit), GO:0098982 (GABA-ergic synapse). For GLUT1: GO:0005886 at the BBB endothelium.
- **Localization/laterality:** **bilateral, symmetric, generalized** by definition — the EEG discharges are bisynchronous. Persistent focal spikes argue *against* the diagnosis.

---

## 8. Temporal Development

- **Onset:** early childhood, **6 mo–6 yr, peak 2–4 yr**; typically **abrupt/subacute** ("usually begins abruptly, with frequent generalized seizures... between 2–6 years of age"), sometimes heralded by febrile or afebrile GTC seizures.
- **Active phase:** often a "stormy" 1–3 year period of frequent daily drops, sometimes with episodes of nonconvulsive status ("minor epileptic status") that dents cognition transiently.
- **Course pattern:** episodic/fluctuating during the active phase, then commonly **self-limited** — the "two-thirds remit" figure. From the outcomes cohort (**PMID:41523187**): *"61.7% achieved seizure freedom after mean 5.1 years."* From epilepsydiagnosis.org: *"Two thirds of children achieve epilepsy remission, usually within 3 years of epilepsy onset."*
- **Critical window:** the active-seizure phase is the intervention window — controlling drops and status early (right drug/diet, avoiding aggravators) appears to protect development. Interestingly, the outcomes cohort found *"'Stormy' onset did not predict worse prognosis"* — it's the **baseline developmental delay**, not the seizure intensity, that flags trouble.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** ~**16.4 per 100,000 children** (one population estimate).
- **Share of childhood epilepsy:** **1–2.2%** of childhood-onset epilepsies; ~5.5% of generalized epilepsies in 1–9 year olds.
- **Prevalence:** not precisely known (rare disease; Orphanet lists it as rare).
- Normalized for your `Prevalence` slots: `ANNUAL_INCIDENCE`, `rate_per_100000: 16.4`, population "children," prevalence_class ~`BAND_1_5_PER_10000` if reasoning from incidence + short active duration (⚠️ but incidence ≠ prevalence — keep them in separate records; don't cross the streams).

**Sex ratio:** male predominant, **~2:1 to 3:1 (M:F)**; Orphanet cites 2.7–3.1:1. The Japanese cohort was 21:8 (~2.6:1); the outcomes cohort was 26.7% female (~2.75:1 M).

**Inheritance (genetic subset):**
- Pattern: mostly **complex/polygenic**; monogenic cases are usually **autosomal dominant, de novo** (*SLC6A1*, *GABRG2*, *STX1B*, *SLC2A1*, *SCN1A*).
- **Penetrance/expressivity:** highly variable expressivity even within a gene — *SLC6A1* alone spans MAE, milder GGE, and focal epilepsy with intellectual disability.
- Anticipation / germline mosaicism / founder effects / carrier frequency: not established for EMAtS specifically — **not available** (de novo dominant biology makes classic carrier-screening framing largely N/A).
- **Consanguinity:** not a notable feature (dominant/de novo, not recessive).

**Demographics:** no strong ethnic enrichment reported; described across European, North American, and Asian cohorts.

---

## 10. Diagnostics

EMAtS is a **clinical-electroencephalographic diagnosis of inclusion + exclusion** — there's no single confirmatory test, and genetics is confirmatory only in the monogenic subset.

**Core clinical + EEG criteria (Ren et al 2021 modification, PMID:34883415; per ILAE 2022 nosology):**
1. Normal development/cognition before onset;
2. Onset ~6 mo–6 yr (peak 2–4);
3. **Myoclonic-atonic seizures mandatory** (plus atonic/myoclonic drop attacks);
4. **Generalized 2–3 Hz (up to ~4 Hz) spike-wave / polyspike-wave** on EEG, **without persistent focal spikes**;
5. **Exclusion** of other myoclonic epilepsies (Dravet, LGS, epileptic spasms, progressive myoclonic epilepsies).

**Tests:**
- **EEG** (the workhorse): normal or theta-rich background early; generalized 2–4 Hz spike/polyspike-wave; characteristic **biparietal/central theta rhythm** (seen in ~69% of the Japanese cohort). ⚠️ Predictors of *poor* outcome: *"slow (<2.5Hz) spike wave or generalized paroxysmal fast activity on EEG"* (the latter smells more like LGS).
- **MRI:** normal (part of the definition; abnormal imaging → reconsider).
- **Genetic testing:** **gene panel or exome/genome sequencing** is now recommended, given ~⅓–40% yield and management implications (SLC6A1, GLUT1). Single-gene testing is low-yield except targeted GLUT1 workup.
- **CSF glucose / CSF:blood glucose ratio** (± *SLC2A1* sequencing): to catch **GLUT1 deficiency** — cheap, high-stakes, don't skip it.
- Metabolic/lactate workup if a progressive myoclonic epilepsy or mitochondrial mimic is on the table.

**Differential diagnosis (the "rule these out" list):** Dravet syndrome (SCN1A, but febrile/hemiclonic, worse trajectory), **Lennox-Gastaut syndrome** (tonic seizures in sleep, slow <2.5 Hz spike-wave, GPFA), epilepsy with eyelid myoclonia, myoclonic epilepsy in infancy, and progressive myoclonic epilepsies.

**LOINC/ontology:** EEG → the electrophysiology bucket; MAXO diagnostic terms exist for EEG (verify). No validated blood biomarker.

---

## 11. Outcome / Prognosis

The prognosis is genuinely **bimodal**, and that bimodality is the most clinically important thing about this disease.

- **Seizure remission:** ~**two-thirds** remit, often within ~3 years of onset; **61.7% seizure-free after mean 5.1 yr** in the outcomes cohort (**PMID:41523187**).
- **Cognition:** roughly **40–44% keep normal cognition**; the outcomes cohort reported *"58.3% had intellectual disability; 43.7% had normal cognition,"* and *"38.3%"* drug-resistant. The Japanese cohort was a bit rosier (41% normal IQ).
- **Mortality:** low; not a classically high-mortality epilepsy, though drug-resistant DEE carries the usual SUDEP and injury risks. No EMAtS-specific mortality rate surfaced — **flag as limited data**.
- **Morbidity:** drop-attack injuries (helmets), behavioral comorbidity (**ADHD ~40%**, the most common), learning problems.

**Prognostic indicators (from PMID:41523187):**
> "Global developmental delay at epilepsy onset was associated with drug resistance and with intellectual disability."
- Early **dual-domain (motor + language) delay** → worse outcome.
- **Identified monogenic aetiology** correlated with higher ID rates (i.e., a positive genetic finding tends to flag the harder-course kids).
- **"Stormy" onset did NOT predict worse prognosis** — counterintuitive but repeatedly noted.
- Tonic seizures, GPFA, and slow (<2.5 Hz) spike-wave lean toward the LGS-like, worse-outcome end.

---

## 12. Treatment

Treatment is **broad-spectrum antiseizure meds + ketogenic diet**, with a hard rule about which drugs to *avoid* because they make generalized epilepsies worse.

**First-line pharmacotherapy:**
- **Valproate / valproic acid** — the consensus first-line (CHEBI:39867). Japanese cohort: *"[valproate] was efficacious in 23 patients (79%)."* An international Delphi consensus endorsed **valproate + clobazam** first-line.
- **Clobazam** (benzodiazepine; CHEBI:31413 verify) — first-line partner.
- **Ethosuximide** (CHEBI:4887 verify) — good for the absence component.
- **Levetiracetam, lamotrigine, topiramate, zonisamide, clonazepam** — common add-ons (clonazepam for myoclonus).

**Ketogenic diet** — the star **second-line** (and arguably should be earlier), MAXO:0000088 (dietary intervention) / consider a ketogenic-diet-specific MAXO term (verify). International consensus: *"the ketogenic diet identified as the optimal second-line treatment."* **Mandatory and curative-ish** if GLUT1 is the cause. Case data show seizure freedom at ~2.5:1 ratio with BHB 4–7 mmol/L.

**⚠️ Contraindicated / aggravating (drop-attack worseners):**
- **Carbamazepine, oxcarbazepine, phenytoin, vigabatrin** (and often gabapentin) — these can worsen myoclonic/atonic/absence seizures in generalized epilepsy. This is a genuine "first, do no harm" curation point.

**Precision / emerging:**
- **GLUT1 (SLC2A1):** ketogenic diet is targeted therapy.
- **SLC6A1:** antisense oligonucleotide and gene-based programs are in preclinical/early development (a real "personalised treatment" frontier the Lancet review flags).
- **Supportive:** injury prevention (helmets), developmental/behavioral support, ADHD management.

MAXO anchors: pharmacotherapy (NCIT:C15986 for the therapeutic-agent pattern), MAXO:0000088 dietary intervention, MAXO:0000950 supportive care.

---

## 13. Prevention

Not a preventable disease in the classic sense — **no primary prevention** (no vaccine, no modifiable exposure). What exists:
- **Secondary prevention:** early recognition + prompt broad-spectrum treatment and **early GLUT1 exclusion** to start the ketogenic diet before energy-deficit damage accrues — this is the highest-value "prevention" lever.
- **Tertiary prevention:** avoiding aggravating drugs, controlling nonconvulsive status, injury protection, developmental/behavioral support to limit encephalopathic sequelae.
- **Genetic counseling:** relevant for the monogenic subset (mostly de novo → low sibling recurrence, but reproductive counseling still warranted); NSGC/ACMG framing.
- Population screening / immunization / public-health interventions: **not applicable**.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** the meaningful non-human data is the **mouse** (*Mus musculus*, NCBITaxon:10090) — specifically the ***Gat1* (Slc6a1)-null mouse**, which shows spontaneous spike-wave discharges and shared electrophysiology with human MAE (Carvill 2015). More recent patient-derived *SLC6A1* knock-in mice (e.g., S295L) model the electrobehavioral phenotype and drug sensitivity.
- **Orthologs:** *Slc6a1*, *Gabrg2*, *Scn1a*, *Slc2a1* are all conserved in mouse/rat/zebrafish.
- **Natural disease in animals:** no recognized spontaneous "Doose syndrome" in companion animals or wildlife (OMIA search: nothing specific) — **not applicable**. Zoonosis: N/A.

---

## 15. Model Organisms

- **Primary model:** **mouse** — *Slc6a1/Gat1* knockout and patient-variant knock-in lines are the workhorses for the GABA-transporter mechanism (spontaneous SWDs, tremor, behavioral phenotypes). Evidence source = **MODEL_ORGANISM** for any of this.
- **GABRG2 mouse models** (e.g., R43Q knock-in) reproduce generalized spike-wave/absence-type activity.
- **Zebrafish** (*Danio rerio*, ZFIN) and iPSC-derived neurons are emerging for *SLC6A1* functional screening (trafficking/surface-expression assays) — good IN_VITRO evidence for the misfolding/LOF mechanism.
- **Recapitulation vs limitations:** mice capture the EEG SWD signature and some behavior well, but the human myoclonic-atonic *drop attack* and the developmental-cognitive trajectory don't map cleanly onto rodents — a `HUMAN_MODEL_MISMATCH` flag is apt if you curate model evidence for the cognitive phenotype.
- **Resources:** MGI, IMPC/KOMP for the knockout lines; Cellosaurus/ATCC for patient iPSC lines.

---

## Curation notes & flags for you

A few things worth doing before this lands in `kb/disorders/`:
- ⚠️ **Verify the MONDO ID with OAK** — `MONDO:0014633` came from MalaCards and I couldn't confirm it. The seed-cache-in-both-checkouts dance from your memory ([new-mondo-term-ols-cache-miss]) probably applies.
- ⚠️ **Every HPO/CHEBI/GO/CL term above is a *suggestion*** — run `just validate-terms-file` before trusting labels (the myoclonic-atonic HP term especially).
- ⚠️ **NEC watch:** this disease is *exactly* the high-risk profile — shared genes with **Dravet (SCN1A)** and phenotype overlap with **LGS**. When you pull DR content, confirm the report is about EMAtS and not a *SCN1A*-Dravet paper wearing a trenchcoat.
- This is a clean conformer for your `epilepsy_excitation_inhibition_imbalance` module (`#Excitation-Inhibition Imbalance`), with the GABAergic-inhibition-failure arm as the disease-specific substitution.
- The **avoid-carbamazepine/phenytoin/vigabatrin** point is a "side-effect-as-mechanism" nugget worth encoding as a treatment caution, not just prose.

**Best single anchor references (all real, PMIDs verified by title):**
- Guerrini, Scheffer, Balestrini. *Lancet Neurol* 2025 — **PMID:40120618** (the current authoritative review)
- Genetic aetiologies/outcomes cohort, *Brain Commun* 2025/2026 — **PMID:41523187**
- Carvill et al, *Am J Hum Genet* 2015 (SLC6A1 discovery) — **PMID:25865495**
- Ren et al, *Eur J Paediatr Neurol* 2021 (diagnostic criteria) — **PMID:34883415**
- Doose clinical/genetic cohort, 2020 — **PMID:32913952**
- Zuberi et al, ILAE nosology, *Epilepsia* 2022 — **PMID:35503712** (neonate/infant; the childhood-onset companion by Specchio et al covers EMAtS formally — pull that PMID when you cite the exact ILAE definition)

**Sources:**
- [Lancet Neurology 2025 review](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(25)00032-8/abstract)
- [Genetic aetiologies/outcomes cohort (PMC12782104)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12782104/)
- [Carvill et al, SLC6A1 (PMC4570550)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4570550/)
- [Clinical & genetic characteristics of Doose syndrome (PMC7469791)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7469791/)
- [Ren 2021 diagnostic criteria modification](https://www.ejpn-journal.com/article/S1090-3798(21)00202-6/abstract)
- [ILAE 2022 nosology (Zuberi et al)](https://pubmed.ncbi.nlm.nih.gov/35503712/)
- [epilepsydiagnosis.org — EMAtS overview](https://www.epilepsydiagnosis.org/syndrome/epilepsy-myoclonic-atonic-overview.html)
- [Orphanet ORPHA:1942](https://www.orpha.net/en/disease/detail/1942)
- [OMIM 616421 — MAE](https://omim.org/entry/616421)
- [SLC6A1 — Epilepsiome/Beyond the Ion Channel](https://epilepsygenetics.blog/the-epilepsiome/slc6a1-this-is-what-you-need-to-know/)
- [Treatment effectiveness review — NCBI Bookshelf NBK581164](https://www.ncbi.nlm.nih.gov/books/NBK581164/)
- [Astrocytic GAT-1 deficit mechanism (PMC9472560)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9472560/)

That's the whole organism, dissected. Want me to kick off the actual `/curate` run for this one on the `curate/doose-mae` branch, or turn this into a first-pass disorder YAML skeleton so you can start filling evidence blocks?