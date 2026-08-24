---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T15:03:27.373965'
end_time: '2026-08-05T15:21:36.314167'
duration_seconds: 1088.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy with Myoclonic Absences
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
  - claude-opus-5[1m]
  web_search_requests: 8
  num_turns: 64
  total_cost_usd: 5.091295
  session_id: fcfa66ff-ec04-4158-8cdb-611fc90136b3
  stop_reason: end_turn
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epilepsy with Myoclonic Absences
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Epilepsy with Myoclonic Absences** covering all of the
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

# Epilepsy with Myoclonic Absences — Research Report

*(a.k.a. Tassinari syndrome, EMA. MONDO:0019487)*

sup. Quick framing before the wall of text: this one is a weird little disease. Most absence epilepsies are a brain that briefly *goes quiet* — the lights flicker, the kid stares, it's over. EMA is a brain that goes quiet **and starts drumming** at the same time. Same 3-beats-per-second rhythm you see in ordinary childhood absence, but here that rhythm leaks out into the muscles and you can literally watch it: the arms ratchet upward, jerk by jerk, in lockstep with the brainwave. It's the one absence syndrome where the electrical signature is *visible from across the room*.

That "leak into the motor system" is basically the whole mechanistic story, and it's also the biggest open question in the field.

**One caveat up front, stated plainly:** EMA is rare enough that there is no large prospective cohort anywhere. Everything below rests on case series of 7–12 patients, a handful of single-case genetic reports, and one 2017 imaging study with **two** subjects. I've flagged sample sizes throughout because they matter a lot here. Anything I couldn't verify against a real abstract or ontology lookup, I've marked as unverified rather than smoothing it over.

---

## 1. Disease Information

### What it is

EMA is a rare, childhood-onset **generalized** epilepsy syndrome whose defining seizure is the *myoclonic absence* — an impairment-of-awareness spell with rhythmic bilateral jerking of the shoulders and arms, superimposed on a slowly building tonic pull that ratchets the arms up and outward.

MONDO's definition (sourced from Orphanet:86911), verified via local OAK lookup:

> "A rare childhood-onset epilepsy characterized by sudden onset, short lasting absence associated with rhythmical myoclonia of head and shoulders."

Historically, Tassinari and colleagues described the *seizure type* in 1969–70 (PMID:4985251, Rev Neurol Paris; PMID:4194033, Electroencephalogr Clin Neurophysiol — "Studies on spike and wave discharges in man. II. Clinical and EEG aspects of myoclonic absences"), and Tassinari named the *syndrome* in 1985. Hence "Tassinari syndrome."

The 2025 review by Tang et al. (PMID:40380288) states verbatim:

> "Epilepsy with myoclonic absence (EMA) is a rare childhood-onset generalized epilepsy syndrome characterized by myoclonic absence seizures. First discovered by Tassinari et al. in 1969, EMA has been extensively studied by researchers from all over the world."

### Identifiers (OAK-verified against local `sqlite:obo:mondo`)

| Resource | ID |
|---|---|
| **MONDO** | `MONDO:0019487` — *epilepsy with myoclonic absences* |
| Orphanet | `ORPHA:86911` |
| MedGen | `140741` |
| UMLS | `C0393703` |
| SNOMED CT | `230422001` |
| GARD | `0019087` |
| NANDO | `1200589` |
| ICD-11 foundation | `274380122` |

MONDO parentage: `is_a MONDO:0005395` (movement disorder) **and** `is_a MONDO:0800498` (childhood-onset genetic generalized epilepsy syndrome). That dual parentage is actually a nice bit of curation — it encodes the "absence + movement" hybrid nature.

**Not available / flagged:** there is **no dedicated OMIM entry** for EMA as a syndrome. It's a clinically-defined electroclinical syndrome, not a Mendelian gene-disease pair, so OMIM entries only exist for the individual gene disorders that can *present as* EMA (SYNGAP1, SETD1B, SLC2A1, GLUD1, CREBBP). I could **not** verify a specific ICD-10 code from an authoritative source in this session — do not populate ICD-10 from memory; Orphanet's mapping page was behind a bot check.

### Synonyms

- Epilepsy with myoclonic absences (EMA) — preferred
- Myoclonic absence epilepsy (MAE — **careful**, this abbreviation collides with *myoclonic-astatic epilepsy* / Doose syndrome; a real named-entity-confusion trap)
- Tassinari syndrome
- MONDO records `"EMA" EXACT`

### Data provenance

Aggregated disease-level, entirely. There is no EHR-derived or registry-derived population data for EMA that I could find — the evidence base is single-center retrospective chart reviews plus case reports. No OMOP/OHDSI phenotype algorithm exists for it.

---

## 2. Etiology

### The honest summary

Tang et al. 2025 (PMID:40380288), verbatim:

> "Overall, the etiology of EMA remains unclear and appears to be heterogeneous, categorized into idiopathic, symptomatic and cryptogenic forms."

Think of EMA less as a disease with a cause and more as a **final common pathway** — a particular way a child's thalamocortical circuit can misfire, reachable from many different genetic starting points. Like a fever: lots of upstream causes, one recognizable downstream output.

Roughly **one-third** of cases are idiopathic (myoclonic absences only, normal MRI, normal EEG background, better outcome); **two-thirds** are symptomatic or have additional seizure types (Tang 2025).

### Genetic risk factors

Family history of epilepsy in **20–25%** of EMA patients (Tang 2025). In the Videira 2023 series (PMID:36893512), only 2/7 had a positive family history. Sibling cases exist (Cherian 2014, PMID:24491945, "Epilepsy with myoclonic absences in siblings"), which points at a heritable component without a clean Mendelian pattern.

Single-gene and chromosomal findings reported in EMA — each of these is a **case report or small series**, not an established gene-disease association:

| Lesion | Evidence | PMID |
|---|---|---|
| **SYNGAP1** truncation by de novo balanced translocation t(6;22)(p21.32;q11.21) | Klitten 2011, n=1 | 22050443 |
| **SETD1B** de novo missense c.386T>G p.(Val129Gly) | Hiraide 2019, n=1 (+1 prior) | 31440728 |
| **SLC2A1** (GLUT1DS), R126C hot-spot | Gökben 2011, n=1 | 21546317 |
| **GLUD1** (glutamate dehydrogenase), gain-of-function, HI/HA syndrome | Bahi-Buisson 2008, n=4 family members | 18321734 |
| **CREBBP** pathogenic variant (Rubinstein-Taybi) | Matsubara 2025, n=1 | 40451035 |
| **Trisomy 12p** | Elia 1998, n=1 | 9545186 |
| **2q13 recurrent microdeletion** (BUB1, ACOXL, BCL2L11, ANAPC1, MERTK, TMEM87B, FBLN7, ZC3H8, ZC3H6) | Ogawa 2023, n=1 | 36796225 |
| **15q11.2 microdeletion** (maternal), with Angelman-like notched delta on EEG | Chin 2026 | 42434914 |
| **Inverted duplication chromosome 15** | Elia, cited in Tang 2025 | — (secondary) |
| **FOXP1**, **MBD5** | cited in Tang 2025 via Frydson | — (secondary) |

Key verbatim quotes:

Klitten 2011 (PMID:22050443):
> "the breakpoint at 6p21.32 was found to truncate the N-methyl-d-aspartate (NMDA)-receptor associated gene SYNGAP1... This finding, together with our report, suggests that dysfunction of SYNGAP1 contributes to the development of generalized epilepsy, including EMA."

Hiraide 2019 (PMID:31440728):
> "Therefore, this report supports the indication that SETD1B may be a causative gene for neurodevelopmental disorders and suggests that epilepsy with myoclonic absences may be a characteristic feature of SETD1B-related disorders."

Gökben 2011 (PMID:21546317):
> "Although typical absences are frequent in GLUT1DS, myoclonic absence seizures are rarely reported. Here we describe a novel Turkish patient with a hot-spot mutation (R126C) in the SLC2A1 gene who presented with unusual myoclonic absence epilepsy and paroxysmal shivering."

Bahi-Buisson 2008 (PMID:18321734):
> "The mother, brother and both sisters had myoclonic absence seizures, but only the mother and one sister had the complete HI/HA pattern."

The broader genetic landscape of absence epilepsies (Balestrini et al., *Epilepsia* 2026, doi:10.1111/epi.18655) identifies **SLC2A1, SLC6A1, SYNGAP1, CHD2, SCN1A** as the most frequent monogenic causes across absence-featuring epilepsies, with CACNA1A also implicated. That paper reports hyperventilation as a precipitant across CACNA1A, GABRA2, GABRG2, SETD1B, SLC2A1, SLC6A1, and SYNGAP1 variants, and notes atypical absences were most common with SYNGAP1 (n=9).

### Environmental / acquired risk factors

Tang 2025:
> "Symptomatic EMA is associated with factors including prematurity, perinatal damage, consanguineous marriage, and congenital hemiparesis."

Older literature (via MedLink secondary summary, **unverified against primary source**) puts etiological factors in ~35% of cases: prematurity, perinatal damage, consanguinity, congenital hemiparesis, chromosomal anomalies.

**Sex** is a genuine risk factor: male predominance ~70% (Tang 2025; epilepsydiagnosis.org). Though note the cohorts disagree — Zanzmera 2016 was 50% male, Videira 2023 was 7/7 male, Hu 2025 was 7:4. Small-n noise.

**Seizure precipitants** (not disease-risk factors, but seizure-trigger factors — worth keeping distinct):
- Hyperventilation
- Awakening
- Intermittent photic stimulation: **14%** of myoclonic absences are IPS-inducible (Tang 2025)

### Protective factors

**Not available.** No protective genetic variants or lifestyle protective factors have been reported for EMA. Given the rarity, no GWAS exists.

### Gene–environment interactions

**Largely not available.** The one real example: in GLUT1 deficiency, the *environmental* variable is dietary — fasting and carbohydrate state modulate seizures, and the ketogenic diet is directly therapeutic because it bypasses the broken glucose transporter. That's a genuine G×E axis (SLC2A1 genotype × dietary substrate), and it's actionable.

---

## 3. Phenotypes

### The core seizure — myoclonic absence

**HP:0011150 — Myoclonic absence seizure** (OAK-verified). This is *mandatory* for the diagnosis under ILAE 2022.

What it looks like, per Tang 2025:

> "The severity of impaired consciousness is usually milder than that in childhood absence epilepsy (CAE), however, the seizure duration (ranging from 8–60 s) exceeds that of CAE"

> "The tonic element affecting both shoulders is often present in myoclonus, leading to rigid abduction and elevation of the upper limbs"

> "Rhythmic myoclonic seizures primarily affect the shoulder and limb muscles with rare eyelid involvement"

The mechanical picture: the jerks are the fast beat, the tonic contraction is a slow steady pull underneath, and because the jerks ride on top of a rising tonic baseline, the arms climb upward in a ratcheting staircase over the course of the seizure. Like a socket wrench — each click advances and holds.

Videira 2023 (PMID:36893512, n=7): "All patients had seizures with impairment of awareness accompanied by bilateral rhythmic myoclonus of the proximal segments of the upper limbs, followed by arm abduction," asymmetrical in 4/7, duration 4–60 s, all with ≥2 seizures/day.

Hu 2025 (PMID:40414191, n=11): 4/11 (36.36%) had asymmetrical features.

**Frequency:** multiple daily, "ranging from several to dozens" per day (Tang 2025), abrupt onset and offset.

| Phenotype | HPO term (verified) | Frequency | Onset | Course | Notes |
|---|---|---|---|---|---|
| Myoclonic absence seizure | `HP:0011150` | 100% (definitional) | childhood | recurrent/daily | mandatory for dx |
| Generalized tonic-clonic seizure | `HP:0002069` Bilateral tonic-clonic seizure | ~45% (Bureau 2005); 42% (Zanzmera 2016) | after MA onset | recurrent | **key prognostic marker** |
| Atonic seizure | `HP:0010819` | 40% had atonic component (Carter 2022, n=10) | childhood | recurrent | drives drug resistance |
| Generalized myoclonic seizure | `HP:0002123` | present in subset | childhood | recurrent | Hu 2025 |
| Typical absence seizure | `HP:0011147` | subset | childhood | recurrent | |
| Myoclonic absence status epilepticus | `HP:0032865` | 20% (Carter 2022, n=10) | childhood | episodic | incl. a twin pair |
| Intellectual disability | `HP:0001249` | ~70% eventually (epilepsydiagnosis.org); 20/28 in Tassinari follow-up | variable | progressive in subset | |
| Delayed speech and language development | `HP:0000750` | 3/6 drug-resistant patients (Hu 2025) | pre- or post-onset | | |
| Developmental regression | `HP:0002376` | 7/15 initially-normal patients (Tassinari series) | after onset | progressive | |
| ADHD | `HP:0007018` | subset | childhood | chronic | Tang 2025 |
| Autism | `HP:0000717` | subset (SETD1B, 2q13, SYNGAP1 cases) | childhood | stable | |
| EEG with spike-wave complexes (2.5–3.5 Hz) | `HP:0010848` | ~82% (Zanzmera 2016) | — | — | ictal + interictal |
| EEG with generalized epileptiform discharges | `HP:0011198` | high | — | — | |
| EEG with photoparoxysmal response | `HP:0010852` | 14% IPS-inducible | — | — | Tang 2025 |
| EEG with hyperventilation-induced generalized epileptiform discharges | `HP:0011184` | common | — | — | |
| Childhood onset | `HP:0011463` | — | — | — | onset descriptor |

### Cognitive trajectory — the part that actually hurts

Tang 2025, summarizing Tassinari's follow-up of 28 patients:

> "13 exhibited intellectual impairment before or at MA onset, while 15 initially showed normal intelligence—of these, 8 remained normal throughout the evolution but 7 developed significant mental deterioration during disease progression. Overall, 20 patients (including 13 with pre-existing and 7 with acquired impairment) ultimately exhibited cognitive deficits, presenting a markedly different neurodevelopmental trajectory compared to childhood absence epilepsy."

And the sting in the tail:

> "Although seizures may gradually diminish over time, the accompanying cognitive deficits frequently persist, and complete functional recovery is rarely achieved."

> "In most children with drug-resistant EMA, the severity of cognitive decline is proportional to the duration of intractable epilepsy."

That last one is the clinically actionable claim in the whole report: **time-with-uncontrolled-seizures appears to be the dose**. It argues for aggressive early control. It's also an observational correlation from a small series and could easily be confounded by severity — worth curating as a hypothesis, not a fact.

### Unusual presentations worth knowing

**Complex gestural automatisms** — Myers & Scheffer 2018 (PMID:29325826):
> "complex gestural automatisms were often observed; in one case, a boy undid his seatbelt and attempted to exit a moving vehicle... Complex automatisms have not been described in myoclonic absence seizures. This generalized seizure type can be confused with focal seizures when these ictal behaviours occur."

**Focal seizures** in EMA: Çetin 2016, PMID:27596001, "A rare finding in epilepsy with myoclonic absences: focal seizure."

### Quality of life

**Not available as measured data.** No EQ-5D, SF-36, PROMIS, or QOLCE data specific to EMA exists that I could find. Impact is inferable from the seizure burden (dozens daily) plus the cognitive/behavioral comorbidity load, but nobody has measured it. This is a real gap.

---

## 4. Genetic / Molecular Information

### Causal genes

There is **no single causal gene**. What exists is a set of genes in which individual patients have presented with an EMA phenotype. Curate these as `relationship_type: CAUSATIVE` only for the specific reported cases, and consider `SUSCEPTIBILITY`/`MODIFIER` framing for the syndrome as a whole.

| Gene | HGNC | Protein / function | Variant reported | Mechanism | PMID |
|---|---|---|---|---|---|
| **SYNGAP1** | `hgnc:11497`* | Synaptic Ras-GTPase-activating protein 1; NMDA-receptor-associated postsynaptic regulator | de novo balanced translocation t(6;22)(p21.32;q11.21), truncating | haploinsufficiency / LoF | 22050443 |
| **SETD1B** | `hgnc:29187`* | Histone H3 lysine 4 methyltransferase component | de novo c.386T>G p.(Val129Gly), missense | LoF, epigenetic dysregulation | 31440728 |
| **SLC2A1** | `hgnc:11005`* | GLUT1, blood-brain-barrier glucose transporter | R126C (hot-spot), missense | LoF, impaired brain glucose supply | 21546317 |
| **GLUD1** | `hgnc:4335`* | Glutamate dehydrogenase | dominantly inherited activating variant | **gain of function** | 18321734 |
| **CREBBP** | `hgnc:2348`* | CREB-binding protein, histone acetyltransferase | pathogenic variant (Rubinstein-Taybi) | LoF | 40451035 |

\* **HGNC IDs above are from memory and were NOT verified with OAK in this session.** Verify each with `just validate-terms` before committing any of them to a KB entry. Note this repo uses lowercase `hgnc:`.

### Mechanistic notes per gene

**SYNGAP1** — sits in the postsynaptic density and acts as a brake on Ras signaling downstream of NMDA receptors. Lose one copy and excitatory synapses mature too early and too strong. Relevant GO: `GO:0098989` (NMDA selective glutamate receptor signaling pathway), `GO:0050803` (regulation of synapse structure or activity). Note Klitten's framing that "Two-thirds of the patients described so far also have generalized epilepsy."

**SETD1B** — writes the H3K4 methyl mark, an activating chromatin tag. Relevant GO molecular function: `GO:0042800` (histone H3K4 methyltransferase activity). Careful: `GO:0051568` "histone H3-K4 methylation" is **obsolete** in current GO — don't use it.

**SLC2A1 / GLUT1** — Tang 2025 describes it as "mainly expressed in endothelial cells and astrocytes of the blood-brain barrier, facilitates glucose transport across the blood-brain barrier into astrocytes to provide energy for the brain." Relevant GO: `GO:1904659` (D-glucose transmembrane transport), `GO:0098708` (D-glucose import across plasma membrane), `GO:0006006` (glucose metabolic process). All OAK-verified. Diagnostic corollary: **low CSF glucose / low CSF:blood glucose ratio**, and it's treatable with ketogenic diet — this is the one genotype where finding it changes management immediately.

**GLUD1 / GDH** — a *gain*-of-function, which is unusual in this list. Tang 2025 describes it as "Enhanced glutamate dehydrogenase's function, increasing oxidative deamination of glutamate and elevating levels of α-ketoglutaric acid and ammonia." Chronic hyperammonemia plus recurrent hypoglycemia plus depleted brain glutamate → a plausible triple hit on cortical excitability. Note this family was also **photosensitive**, which is a phenotype marker worth tracking.

### Variant classification / allele frequency / somatic vs germline

- All reported variants are **germline**, mostly **de novo**. GLUD1 was **dominantly inherited** through a family.
- ACMG classification: individually reported as pathogenic/likely pathogenic in their source papers; I did **not** query ClinVar directly this session, so treat per-variant classifications as unverified.
- **Allele frequencies: not available.** These are private/de novo variants; gnomAD frequencies would be zero or absent. Not a meaningful field here.

### Modifier genes

**Not available.** No modifier gene has been identified for EMA.

### Epigenetic information

Indirect but real: **SETD1B** (H3K4 methyltransferase) and **CREBBP** (histone acetyltransferase) are both chromatin writers, and **15q11.2 / inv dup(15)** sits in an imprinted region with maternal-origin effects. So chromatin-level regulation shows up three separate ways in this small gene list, which is suggestive. No direct methylome study of EMA patients exists (no ENCODE/Roadmap/DiseaseMeth data specific to EMA).

### Chromosomal abnormalities

Genuinely a recurring theme — Elia 1998 (PMID:9545186) argued this explicitly:

> "Our patient and other sporadic reports in the literature seem to support the hypothesis that, at least in some cases, myoclonic absences can be a direct or indirect effect of a chromosomopathy."

Reported: trisomy 12p; 2q13 recurrent microdeletion; maternal 15q11.2 microdeletion; inverted duplication of chromosome 15. **Practical implication: chromosomal microarray belongs in the EMA workup**, not just a gene panel.

---

## 5. Environmental Information

- **Environmental toxins / radiation / occupational exposure:** not applicable / not reported.
- **Infectious agents:** not applicable. EMA is not infection-triggered.
- **Perinatal factors:** prematurity and perinatal brain injury are reported as antecedents in symptomatic EMA (Tang 2025). These are the closest thing to an environmental exposure in this disease.
- **Consanguinity:** reported as an associated factor (Tang 2025), which is really a genetic-architecture signal (recessive burden) wearing an environmental costume.
- **Lifestyle:** the only lifestyle variable with mechanistic weight is **diet**, and only in the GLUT1-deficiency subgroup, where carbohydrate/ketone state directly modulates brain fuel supply.
- **Iatrogenic aggravation** — this is environmental in the practical sense and it matters: several antiseizure drugs *worsen* EMA. Tang 2025: "Carbamazepine, phenytoin, vigabatrin, gabapentin, and tiagabine should be avoided due to their potential to exacerbate seizures." Levetiracetam aggravation of absence seizures is also documented (Auvin 2011, PMID:21680209) — which is awkward, because levetiracetam is also listed as a second-line option. Genuine tension in the literature; curate both directions.

---

## 6. Mechanism / Pathophysiology

### The causal chain, as best anyone knows it

Here's the story in plain terms. There's a three-way loop in the brain — cortex talks to thalamus, thalamus talks back to cortex, and a thin shell of inhibitory cells called the thalamic reticular nucleus wraps around the thalamus and gates the whole conversation. Normally that loop does useful rhythmic things (it's the machinery behind sleep spindles). In absence epilepsy it slips into a pathological resonance and starts ringing at 3 cycles per second, and consciousness drops out while it rings.

Tang 2025, verbatim:

> "Previous experimental studies have confirmed that the activation of a neural loop—including the cerebral cortex, thalamic reticular nucleus and thalamus—produces the 3 Hz spike-slow wave in absence seizures."

**Then EMA does the extra thing.** The central unsolved question, stated by Tang 2025:

> "A key unresolved question is why motor symptoms (e.g., myoclonus) are prominent in EMA but absent in typical absence epilepsy."

Their proposed model:

> "Given these observations, it is plausible that in EMA, the 3 Hz spike-waves generated by the thalamocortical loop likely excessively drive the motor cortex, especially the precentral gyrus, leading to simultaneous occurrence of myoclonus."

So: same oscillator, but the motor strip is unusually strongly coupled into it, and each cycle of the oscillation discharges down the corticospinal tract as a jerk. The 3 Hz rhythm stops being purely an internal brain event and becomes a **motor command**.

### The one piece of direct human evidence

Ikeda et al. 2018 (PMID:28823645), ictal SPECT with 99mTc-ECD in **two** patients (ages 4 and 8):

- Patient 1: increased perfusion in "perirolandic areas, thalamus, caudate nucleus, and precuneus"; decreased in frontal and orbitofrontal regions
- Patient 2: increased in "thalamus, putamen, and globus pallidus"; decreased precuneus

Conclusion, verbatim:

> "in addition to the thalamus and basal ganglia, the perirolandic cortical motor area is involved in MAs"

That's the empirical anchor for the motor-cortex-recruitment model. **n=2.** Please curate it with that caveat attached — it is a suggestive finding, not a demonstrated mechanism.

### Proposed causal chain for a pathograph

Upstream → downstream:

1. **Genetic or chromosomal lesion** (MOLECULAR) — SYNGAP1/SETD1B/SLC2A1/GLUD1 LoF or GoF, or a CNV. Sets the excitability baseline.
2. **Altered synaptic excitation/inhibition balance** (MOLECULAR/CELLULAR) — `GO:0007268` chemical synaptic transmission, `GO:0060080` inhibitory postsynaptic potential, `GO:0007214` GABA signaling pathway, `GO:0070588` calcium ion transmembrane transport (T-type Ca²⁺ currents in thalamic relay cells are the classic absence substrate).
3. **Thalamocortical loop enters hypersynchronous 3 Hz resonance** (TISSUE) — cortex `UBERON:0016529`, thalamus `UBERON:0001897`, thalamic reticular nucleus `UBERON:0001903`. Process: `GO:0042391` regulation of membrane potential, `GO:0019228` neuronal action potential.
4. **Impairment of awareness** (ORGANISM) — the classic absence output; note it's *milder* than CAE here.
5. **Cycle-locked recruitment of primary motor cortex** (TISSUE) — `UBERON:0001384` primary motor cortex; the EMA-specific branch.
6. **Rhythmic 3 Hz myoclonus + progressive tonic contraction** (ORGANISM) — the visible seizure.
7. **Chronic high seizure burden → cognitive deterioration** (ORGANISM) — in the drug-resistant subset.

This maps cleanly onto the existing `epilepsy_excitation_inhibition_imbalance` module in this repo. Key conformance target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`. EMA's distinctive contribution — the thing worth *not* pushing into the module — is step 5, the motor-cortex recruitment branch.

### Cell types involved (CL, OAK-verified)

- `CL:0000679` glutamatergic neuron — corticothalamic and thalamocortical projections
- `CL:0000617` GABAergic neuron — thalamic reticular nucleus inhibitory shell
- `CL:0000598` pyramidal neuron — cortical output, including motor cortex
- `CL:4023068` thalamic excitatory neuron — relay cells; T-type Ca²⁺ burst firing
- `CL:4023013` corticothalamic-projecting glutamatergic cortical neuron — the cortical arm of the loop
- `CL:0008031` cortical interneuron
- `CL:0000127` astrocyte — specifically relevant in the GLUT1 subgroup (astrocytes at the BBB are where GLUT1 does its work)

### Anatomy (UBERON, OAK-verified)

`UBERON:0000955` brain · `UBERON:0001897` dorsal plus ventral thalamus · `UBERON:0001903` thalamic reticular nucleus · `UBERON:0001384` primary motor cortex · `UBERON:0016529` cortex of cerebral lobe · `UBERON:0002420` basal ganglion · `UBERON:0001873` caudate nucleus · `UBERON:0001874` putamen · `UBERON:0002435` striatum · `UBERON:0006093` precuneus cortex

### Metabolic changes

Only in specific genetic subgroups:
- **GLUT1DS**: impaired glucose flux across the blood-brain barrier → chronic brain energy deficit → low CSF glucose. `GO:1904659` D-glucose transmembrane transport.
- **GLUD1/HI-HA**: elevated α-ketoglutarate and ammonia, plus episodic hypoglycemia. Chronic hyperammonemia is independently neurotoxic (astrocyte glutamine osmole swelling — same logic as the `metabolic_intoxication_decompensation` module here, though EMA is not an intoxication-type IEM).

### Immune involvement, tissue damage, fibrosis, oxidative stress

**Not applicable.** EMA is a circuit-function disorder, not a tissue-destruction disorder. Brain MRI is normal in idiopathic EMA. There is no inflammatory, autoimmune, or degenerative component described.

### Molecular profiling / advanced technologies

**Not available.** No transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial, or CRISPR-screen data specific to EMA. Nothing in GEO/ArrayExpress/PRIDE/MetaboLights for this syndrome. Genuinely unstudied at the omics level — unsurprising for a syndrome this rare with no reliable animal model.

---

## 7. Anatomical Structures Affected

- **Body system:** nervous system, exclusively. No multi-organ involvement.
- **Primary organ:** brain (`UBERON:0000955`)
- **Primary circuit:** thalamocortical loop — thalamus (`UBERON:0001897`), thalamic reticular nucleus (`UBERON:0001903`), cerebral cortex (`UBERON:0016529`)
- **EMA-distinctive site:** primary motor cortex / perirolandic region (`UBERON:0001384`)
- **Secondary involvement:** basal ganglia (`UBERON:0002420`) — caudate, putamen, globus pallidus; precuneus (`UBERON:0006093`) — per Ikeda 2018 SPECT
- **Effector (not lesioned, just driven):** proximal upper-limb musculature, especially **deltoid**. This is where the polygraphy lands its electrodes. Iyer 2017 (PMID:28366625) titled a paper "Proximal Upper Limb Jerking" precisely as a diagnostic sign.

**Subcellular:** no specific compartment pathology. The action is at the **synapse** and the **plasma membrane** (ion channels, glutamate receptors, GLUT1 transporter) rather than in an organelle. For GLUT1DS the relevant compartment is the plasma membrane of BBB endothelium and astrocytes.

**Lateralization:** classically **bilateral and symmetric** — that's part of the definition. But asymmetry is common enough to be a recognized variant: 4/7 in Videira 2023, 4/11 (36%) in Hu 2025, and Ogawa's 2q13 case presented specifically with **unilateral** jerks (PMID:36796225). Asymmetry should *not* by itself exclude the diagnosis, though it should prompt harder for a structural or chromosomal cause.

---

## 8. Temporal Development

### Onset

- **Range:** 6 months to 12.5 years (Tang 2025); epilepsydiagnosis.org gives 1–12 years
- **Peak:** ~7 years
- **Cohort means:** 3.5 y (Zanzmera 2016, n=12) · 5.2 y, range 3–8 (Videira 2023, n=7) · 7.18 ± 3.72 y (Hu 2025, n=11)
- **Pattern:** subacute — seizures start at multiple-per-day frequency fairly quickly
- Tang 2025: **"No cases of EMA with adult onset have been reported thus far"** — a clean exclusionary criterion
- HPO onset terms: `HP:0011463` Childhood onset (primary); `HP:0003593` Infantile onset (for the earliest cases)

### Course

Tang 2025:
> "patients with EMA may continue experiencing MA attacks for up to 10 years after onset, with seizures typically subsiding after 4 years on average. Notably, EMA can evolve into LGS in some individuals."

Course pattern: **episodic seizures on a chronic background**, with two divergent trajectories:

1. **Idiopathic branch (~1/3):** myoclonic absences only, normal MRI and EEG background, good drug response, eventual remission, cognition preserved.
2. **Symptomatic branch (~2/3):** additional seizure types (especially GTCS), drug resistance, cognitive decline, possible evolution to Lennox-Gastaut syndrome.

The fork is decided early and mostly by **whether GTCS are present**. Tang 2025:
> "The course of EMA mainly depends on the existence of GTCS, regardless of encephalopathic features (such as psychomotor retardation, hemiparesis and behavioral disorders) or treatment timing."

Worth flagging: that last clause — "regardless of... treatment timing" — sits in **direct tension** with the claim elsewhere in the same review that cognitive decline is proportional to duration of intractable epilepsy. That's a real, curatable contradiction in the literature. Recommend a `KNOWLEDGE_GAP` discussion on it.

### Remission

**~40%** remit (epilepsydiagnosis.org; consistent with Hu 2025's 45.45% seizure-free at 15–44 months follow-up). Remission is largely treatment-associated rather than clearly spontaneous, though the natural-history data can't cleanly separate the two.

### Critical periods

The implied intervention window is **early**: if seizure duration drives cognitive outcome, then the first months after onset are the window that matters. This is an inference from observational data, not a tested claim.

---

## 9. Inheritance and Population

### Epidemiology

- **Share of epilepsy:** "EMA accounts for 0.5–1% of total epilepsy patients" (Tang 2025). Note this phrasing is a *proportion of epilepsy patients*, not a population prevalence — don't convert one into the other.
- **Population prevalence / incidence: not available.** No population-based estimate exists. Orphanet lists it as rare (`subset: rare`, `orphanet_rare`) but I could not retrieve a numeric prevalence class this session — the Orphanet page was behind a bot check and there's no `ORPHA_86911.md` in this repo's reference cache.

For a dismech `Prevalence` block, the honest fill is `prevalence_class: NOT_YET_DOCUMENTED` or `UNKNOWN` with the 0.5–1%-of-epilepsy figure in `notes`, **not** converted to a rate.

### Inheritance

- **Not Mendelian at the syndrome level.** Most cases are sporadic.
- Family history of epilepsy in 20–25%, suggesting **polygenic/multifactorial** susceptibility — consistent with the broader genetic generalized epilepsies.
- Individual genetic causes: **de novo autosomal dominant** (SYNGAP1, SETD1B, CREBBP, SLC2A1 usually) or **inherited autosomal dominant** (GLUD1 family in Bahi-Buisson 2008). HPO: `HP:0000006` Autosomal dominant inheritance.
- Sibling recurrence reported (Cherian 2014, PMID:24491945) — consistent with either recessive inheritance in consanguineous families or shared polygenic load. `HP:0000007` Autosomal recessive inheritance may apply in the consanguinity-associated subgroup.
- **Penetrance, expressivity:** the GLUD1 family is instructive on expressivity — all four had myoclonic absences but only two had the full HI/HA metabolic phenotype, and the mother's EEG was normal without photosensitivity. So: variable expressivity, clearly.
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.
- **Founder effects, carrier frequency:** not applicable / not available.

### Demographics

- **Sex ratio:** male-predominant, ~70% male (Tang 2025; epilepsydiagnosis.org gives 7:3). Cohorts vary: 7:4 (Hu 2025), 7:0 (Videira 2023), 1:1 (Zanzmera 2016). The male skew is a consistent enough signal across the literature to record, but the effect size is soft.
- **Ethnic/geographic distribution:** no reported predilection. Cases published from Italy, France, Turkey, Denmark, Japan, India, China, Portugal, USA — i.e. wherever people do video-EEG. Consanguinity as a risk factor implies enrichment in populations with high consanguinity rates, but this hasn't been quantified.
- **Age distribution:** pediatric, by definition.

---

## 10. Diagnostics

### The single most important test: video-EEG with surface EMG polygraphy

This is not optional and it is the whole ballgame. Genton & Bureau 2006 (PMID:17044728) are blunt that diagnosis requires "video documentation of the seizure and/or adequate polygraphy," as it may otherwise be missed.

What you're looking for — the time-locking. From the polygraphy literature: rhythmic bilateral myoclonias have "a strict and constant relation with the spike wave of the discharge; the latency between EEG spikes and EMG myoclonic activity varies between 15 and 40 milliseconds in proximal muscles."

Tang 2025:
> "A strict time-locked relationship exists between EEG and EMG, making the analysis of electro-clinical symptoms with MA crucial for EMA diagnosis"

That 15–40 ms latency is basically corticospinal conduction time. It's the measurement that proves the cortex is driving the muscle rather than the two happening coincidentally. Beautiful piece of clinical neurophysiology.

Aoun 2021 (PMID:33632671) shows why the polygraphy matters even more than you'd think — they demonstrated that in one case "rhythmic upper limb jerking, mimicking positive myoclonus, corresponded to recovery of muscular tone after each negative myoclonus." So the arm going *up* can actually be the arm recovering from a brief drop. Without EMG you'd call it the wrong seizure type entirely. Their conclusion: "video-EEG recording coupled to EMG polygraphy is essential."

**Electrode placement:** bilateral deltoids at minimum.

### EEG findings

**Interictal** (Tang 2025):
> "The background EEG activity of EMA is typically remains normal"
> "Interictal recordings demonstrate generalized spike-wave or polyspike-waves predominance in the frontal area"

Abnormal background = a red flag for symptomatic EMA and a worse prognosis.

**Ictal:**
> "the EEG shows rhythmic 3 Hz generalized spike-wave or polyspike-waves activity"
> "Accompanied by characteristic EMG manifesting as bilateral synchronous and symmetrical rhythmic EMG bursts, superimposed with gradually increasing tonic potential"

Zanzmera 2016 (PMID:27770719): "3- to 3.5-Hz spike-and-wave discharges (82%) and fast recruiting bifrontal rhythm (25%)."

Hu 2025: "In eight patients [of 11], bilateral symmetrically synchronized 3 Hz rhythmic spike-slow wave complex bursts, which showed a lock-in relationship with myoclonic, were recorded."

**Activation procedures:** hyperventilation, awakening, intermittent photic stimulation (positive in 14%).

### Imaging

- **Brain MRI** (`NCIT:C16809` Magnetic Resonance Imaging, OAK-verified): normal in idiopathic EMA; abnormal MRI defines the symptomatic form. Mandatory in the workup.
- **Ictal SPECT:** research tool only (Ikeda 2018). Not clinical practice.
- **EEG-fMRI:** used in childhood absence epilepsy research; Tang 2025 notes it showed involvement of "primary sensory (visual, auditory, somatosensory), motor (Rolandic) areas and frontoparietal association cortex" during absence seizures. Not established for EMA specifically.

### Laboratory tests

- **CSF glucose and CSF:blood glucose ratio** — to screen for GLUT1 deficiency. This is the highest-yield metabolic test because a positive result changes treatment immediately (ketogenic diet).
- **Ammonia and insulin** — if the HI/HA (GLUD1) phenotype is suspected, especially with photosensitivity or episodic hypoglycemia.
- No EMA-specific biomarker exists.

### Genetic testing — recommended approach

Given the etiological picture (single genes *and* recurrent CNVs both well-represented), a two-pronged approach:

1. **Chromosomal microarray (CMA)** — non-negotiable here. Trisomy 12p, 2q13 microdeletion, 15q11.2 microdeletion, and inv dup(15) have all produced EMA phenotypes. A gene panel alone will miss every one of these.
2. **Epilepsy gene panel or whole-exome sequencing** — covering at minimum SLC2A1, SYNGAP1, SETD1B, GLUD1, CREBBP, plus the broader absence-epilepsy genes (SLC6A1, CHD2, SCN1A, CACNA1A, GABRA2, GABRG2). WES has the advantage of catching the long tail; several of the EMA gene associations were WES discoveries (Hiraide 2019 explicitly: "Using whole-exome sequencing, we found a novel de novo variant").
3. **Targeted SLC2A1 testing** if CSF glucose is low — or just test it upfront given how actionable it is.

Karyotype/FISH: historical relevance (Klitten's translocation was mapped by FISH), but superseded by CMA + sequencing for first-line use. Note that a *balanced* translocation like Klitten's is invisible to both CMA and standard WES — so in a patient with EMA + intellectual disability and negative CMA/WES, karyotype still has a role.

**Not applicable:** mtDNA testing, repeat expansion testing, liquid biopsy, methylation arrays (except 15q11.2 imprinting studies if an Angelman-like EEG pattern is seen — see Chin 2026, PMID:42434914).

**Omics diagnostics:** not available / not established for EMA.

### Clinical criteria (ILAE 2022)

EMA is one of three generalized epilepsies with childhood onset in the ILAE 2022 nosology (Specchio et al., *Epilepsia* 2022;63(6):1398-1442, PMID:35503717), alongside childhood absence epilepsy and epilepsy with eyelid myoclonia. ILAE 2022 classifies it as a **hereditary generalized epilepsy syndrome with childhood onset**.

**Mandatory:** myoclonic absence seizures — absences with rhythmic 3 Hz jerks of the upper limbs superimposed on tonic abduction of the arms, with abrupt onset and offset; ictal EEG showing regular 3 Hz generalized spike-wave time-locked to the jerks.

I was **unable to retrieve the full ILAE mandatory/alert/exclusionary criteria table** — both the Wiley full text and the ILAE PDF returned 403 in this session. Do not populate exclusionary criteria from memory; fetch PMID:35503717 properly before curating that section.

### Differential diagnosis

From Tang 2025's comparison table:

| | Idiopathic EMA | Symptomatic EMA | CAE | Jeavons (eyelid myoclonia) |
|---|---|---|---|---|
| Onset | 6 mo–12.5 y | 6 mo–12.5 y | 4–10 y | 2–14 y |
| Sex (M:F) | 7:3 | 7:3 | ~1:2 (female-predominant) | 1:2 |
| Seizure types | MA only | MA + GTCS/clonic/atonic/typical absence | typical absence | eyelid myoclonia ± absence |
| MRI | normal | abnormal | normal | normal |
| EEG background | normal | abnormal | normal | normal |
| Ictal EEG | 3 Hz GSWD time-locked to jerks | same | 3 Hz GSWD | eye-closure/IPS-induced 3 Hz GSWD |
| Prognosis | remits | persistent, drug-resistant, ID common | >90% remit | drug-resistant, lifelong |

Tang 2025: **"In general, symptomatic EMA is often associated with abnormal neurological signs, abnormal background activity of EEG and structural abnormalities on brain MRI."**

Additional differentials to rule out:
- **Childhood absence epilepsy with mild myoclonic features** — Capovilla 2001 (PMID:11431166) describes "A clinical spectrum of the myoclonic manifestations associated with typical absences in childhood absence epilepsy." The boundary is genuinely fuzzy; the discriminator is whether the myoclonus is prominent, rhythmic, proximal, and tonically-augmented, versus incidental.
- **Atypical absence with negative myoclonus / ESES** — Aoun 2021, PMID:33632671. EMG polygraphy is what separates these.
- **Focal seizures with automatisms** — Myers & Scheffer 2018, PMID:29325826.
- **Myoclonic-atonic epilepsy (Doose)** — nomenclature trap, different syndrome. This repo has a separate `Epilepsy_with_Myoclonic_Atonic_Seizures` entry; keep the two entries explicitly cross-referenced as differentials.
- **Lennox-Gastaut syndrome** — both a differential and a possible evolution endpoint.
- **Early-onset absence epilepsy** (<3 years) — Chaix 2003, PMID:12823578, "Absence epilepsy with onset before age three years: a heterogeneous and often severe condition"; Caraballo 2011, PMID:21269284.
- **ATRX syndrome** — myoclonic absences appear in its EEG spectrum (Aiello 2022, PMID:36031702).

### Screening

**Not applicable.** There is no newborn screening, carrier screening, or population screening for EMA. Cascade testing applies only in the rare families with an identified dominant variant (e.g. the GLUD1 family).

---

## 11. Outcome / Prognosis

### Mortality

**No EMA-specific mortality data available.** Not a directly fatal condition. Standard epilepsy mortality considerations (SUDEP risk with uncontrolled GTCS, injury from atonic falls) apply but have not been quantified for EMA specifically. Life expectancy: not reported.

### Seizure outcome

| Series | n | Outcome |
|---|---|---|
| epilepsydiagnosis.org / Tang 2025 | — | remission in ~40% |
| Hu 2025 (PMID:40414191) | 11 | 5 (45.45%) seizure-free with no cognitive impairment; 6 drug-resistant |
| Carter 2022 (PMID:35770757) | 10 | 60% had **incomplete** control at last follow-up |
| Zanzmera 2016 (PMID:27770719) | 12 | 9 responders: 4 seizure-free ≥1 y, 2 with >90% reduction, 3 with >50% reduction |

Zanzmera's conclusion, verbatim-ish from the abstract: "While most patients responded favorably to treatment, prognosis remained guarded, with some patients developing drug-resistant seizures evolving into different patterns."

### Cognitive/functional outcome

The harder outcome. ~70% eventually have learning impairment (epilepsydiagnosis.org). Tassinari's 28-patient follow-up: 20/28 ended with cognitive deficits, of whom 7 had *acquired* the deficit during the disease course. Behavioral morbidity: ADHD, aggression, impulse-control problems, learning disabilities (Tang 2025).

### Prognostic factors — the actionable list

1. **Presence of GTCS** — the strongest predictor. Bureau & Tassinari 2005 (PMID:15737698): treatment "proves most effective when myoclonic absences occur independently. However, prognosis becomes less favorable when combined with other seizure types, potentially progressing toward different epilepsy forms."
2. **Atonic component** — Carter 2022: "Of patients with an atonic component, 75% did not achieve seizure freedom with medication alone."
3. **Pre-onset developmental delay** — Hu 2025's conclusion, verbatim: "developmental delay before disease onset may be associated with a poor prognosis." In their drug-resistant subgroup, 4/6 (66.67%) had developmental delay predating the epilepsy.
4. **Abnormal EEG background / abnormal MRI** — symptomatic form marker.
5. **Duration of uncontrolled seizures** — correlated with cognitive decline severity (Tang 2025), though see the contradiction flagged in §8.

### Complications

- Evolution to **Lennox-Gastaut syndrome**
- **Myoclonic absence status epilepticus** (`HP:0032865`) — 20% in Carter 2022
- Injury from atonic drop attacks
- Progressive cognitive and behavioral deterioration

### Recovery potential

Seizures often diminish over time (average ~4 years, up to 10). Cognition does not follow: "complete functional recovery is rarely achieved" (Tang 2025). That asymmetry — the seizures burn out but the developmental cost is already paid — is the defining tragedy of the symptomatic form.

### Prognostic biomarkers

**Not available.** No molecular prognostic marker exists. The best predictors are clinical (seizure types, EEG background, baseline development).

---

## 12. Treatment

### First-line pharmacotherapy

Tang 2025, verbatim:
> "The first-line ASMs are sodium valproate, ethosuximide, and lamotrigine, which can be used alone or in combination."

Genton & Bureau 2006 (PMID:17044728): treatment typically involves "valproic acid and ethosuximide, or valproic acid and lamotrigine."

Bureau & Tassinari 2005 (PMID:15737698): "Treatment with valproate and ethosuximide proves most effective when myoclonic absences occur independently."

Hu 2025: of the 5 patients who became seizure-free, **4/5 (80%) were on valproic acid alone**. Zanzmera 2016: "Most benefited from valproate monotherapy or valproate-lamotrigine combination therapy."

So the consensus is unusually clean for a rare disease: **valproate is the backbone**, ethosuximide or lamotrigine is the partner.

| Treatment | Drug (CHEBI, OAK-verified) | NCIT action term | Modality |
|---|---|---|---|
| Valproate | `CHEBI:39867` valproic acid | `NCIT:C15986` Pharmacotherapy | SMALL_MOLECULE |
| Ethosuximide | `CHEBI:4887` ethosuximide | `NCIT:C15986` | SMALL_MOLECULE |
| Lamotrigine | `CHEBI:6367` lamotrigine | `NCIT:C15986` | SMALL_MOLECULE |
| Levetiracetam | `CHEBI:6437` levetiracetam | `NCIT:C15986` | SMALL_MOLECULE |
| Topiramate | `CHEBI:63631` topiramate | `NCIT:C15986` | SMALL_MOLECULE |
| Clonazepam | `CHEBI:3756` clonazepam | `NCIT:C15986` | SMALL_MOLECULE |
| Zonisamide | `CHEBI:10127` zonisamide | `NCIT:C15986` | SMALL_MOLECULE |
| Rufinamide | `CHEBI:134966` rufinamide | `NCIT:C15986` | SMALL_MOLECULE |
| Phenobarbital | `CHEBI:8069` phenobarbital | `NCIT:C15986` | SMALL_MOLECULE |
| **Avoid:** carbamazepine | `CHEBI:3387` carbamazepine | — | — |

*(Note per this repo's memory: `therapeutic_agent` validation prefers CHEBI over NCIT drug terms — all of the above are CHEBI and OAK-verified.)*

### Second-line

Tang 2025: "Second-line ASMs include levetiracetam, acetazolamide, zonisamide, topiramate, and lacosamide." *(I did not verify CHEBI IDs for acetazolamide or lacosamide — look those up before curating.)*

### Drugs to avoid — worth curating as an explicit treatment entry

Tang 2025: "Carbamazepine, phenytoin, vigabatrin, gabapentin, and tiagabine should be avoided due to their potential to exacerbate seizures."

The mechanism is well-understood generally: sodium-channel blockers and GABA-transaminase/reuptake drugs enhance thalamic burst firing and make generalized spike-wave *worse*. It's the pharmacological equivalent of trying to quiet a resonating string by pushing on it in rhythm.

Contradiction to preserve: **levetiracetam** appears as second-line in Tang 2025 *and* as an absence-aggravating drug in Auvin 2011 (PMID:21680209, "Aggravation of absence seizure related to levetiracetam"). Curate both; don't resolve it silently.

### Refractory options

**Rufinamide add-on** — Häusler 2011 (PMID:21557146), n=3 boys refractory to conventional therapy:
> "Add-on RUF treatment was initiated in 3 boys with EMA refractory to conventional antiepileptic therapy (primidone + valproic acid, n=1; levetiracetame + ethosuximide, n=2). It resulted in complete cessation of all seizures in 2, and a 50% reduction of the seizure frequency in one child, respectively."

Interesting that rufinamide — licensed for Lennox-Gastaut — works here, given EMA's tendency to evolve toward LGS. Possibly the same circuit vulnerability.

**Low-dose phenobarbital** — Ito 2021 (PMID:33461850), n=1: complete seizure freedom after adding low-dose phenobarbital to valproate + ethosuximide.

**Ketogenic diet** (`NCIT:C173168` Ketogenic Diet, OAK-verified; `NCIT:C15447` Dietary Intervention; modality BEHAVIORAL per this repo's mapping table). Especially indicated in GLUT1 deficiency, where it's not adjunctive but **mechanistically corrective** — ketones cross the blood-brain barrier via MCT1, which is intact, routing around the broken GLUT1 door entirely.

**Vagus nerve stimulation** — listed by Tang 2025. Modality DEVICE. ⚠️ **No suitable NCIT clinical-action term found** in the local NCIT adapter (`NCIT:C203750` is *transcutaneous auricular* VNS, which is a different intervention). Leave `term:` off and keep a free-text `preferred_term`, per this repo's convention.

**Corpus callosotomy** — the most interesting refractory option, and mechanistically elegant: if the seizure depends on bilateral synchrony, cutting the main bridge between the hemispheres should degrade it.

Carter 2022 (PMID:35770757), verbatim:
> "Two patients with epilepsy with myoclonic absences with atonia underwent corpus callosotomy; one patient was seizurefree eight months after surgery and the other had greater than 50% seizure reduction over a five-month period."

And their appropriately cautious conclusion: "the efficacy of this treatment should be further evaluated in a larger study."

Suggested NCIT: `NCIT:C15656` Neurosurgical Procedure (OAK-verified) — NCIT has **no** specific callosotomy term in this build. Modality SURGERY.

### Personalized medicine

Two real genotype-guided decisions exist:
1. **SLC2A1/GLUT1DS → ketogenic diet.** The clearest case.
2. **GLUD1/HI-HA → ** management of hyperinsulinism/hyperammonemia (diazoxide, protein-intake management) alongside seizure control.

Everything else is empirical. **Pharmacogenomics: not available** — no PharmGKB/CPIC guidance specific to EMA beyond the general HLA-B*15:02/carbamazepine and CYP2C9/phenytoin warnings, which are moot since both drugs are contraindicated here anyway.

### Supportive / rehabilitative

Given the ~70% learning-impairment rate: special education support, speech-language therapy (`NCIT:C159273`, *unverified*), occupational therapy, behavioral intervention for ADHD/impulse control. Genetic counseling (`NCIT:C15240` Genetic Counseling, OAK-verified) once a genetic cause is identified.

### Clinical trials

**None found specific to EMA.** No NCT identifiers for EMA-specific trials. Patients would be enrolled, if at all, under broader generalized-epilepsy or LGS protocols. Cannabidiol has been discussed for epilepsies beyond Dravet/LGS (Lattanzi 2021, PMID:33754312) but I found no EMA-specific efficacy data.

---

## 13. Prevention

Short section, because there isn't much, and I'd rather say so than pad it.

- **Primary prevention:** **not available.** Most cases are de novo genetic or idiopathic. The only modifiable upstream factors are the perinatal ones (prematurity, birth injury) associated with symptomatic EMA, which is really just general perinatal care rather than EMA prevention.
- **Immunization:** not applicable.
- **Population screening:** not applicable. Too rare, no presymptomatic marker, no preventive intervention.
- **Genetic screening:** prenatal/preimplantation testing is technically available for families with an identified pathogenic variant (e.g. the GLUD1 kindred), and cascade testing of relatives applies in those rare families. Genetic counseling (`NCIT:C15240`) is appropriate once a molecular cause is found — but for the ~sporadic majority, recurrence risk counseling is essentially "low, empirical, unquantified."
- **Secondary prevention (early detection):** this is where the real leverage is. Because prognosis may track with duration of uncontrolled seizures, **shortening time-to-diagnosis is the closest thing EMA has to a preventive intervention.** The bottleneck is recognition: without video-EEG-plus-EMG, myoclonic absences get miscalled as tics, behavioral episodes, focal seizures, or plain absence. Tang 2025 states the goal of their review is to "reduce the rate of missed diagnosis and misdiagnosis."
- **Tertiary prevention:** seizure control to protect cognition; avoiding the aggravating drug list (a genuinely preventable iatrogenic harm); fall precautions in patients with atonic components.
- **Behavioral / public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

This section has exactly one entry, and it's delightful.

**Dog** — *Canis lupus familiaris*, `NCBITaxon:9615`.

Poma, Ochi & Cortez 2010 (PMID:20483714), *Epileptic Disord*, verbatim:

> "Long-term video-EEG was recorded for an eight-month-old Chihuahua dog with recurrent episodes of altered behaviour associated with head and nose twitching. Each episode lasted one to two seconds, multiple times per day before treatment. Ictal EEG showed generalised bilaterally synchronous 4 Hz spike-and-wave complexes during the 'absence-like' event, along with rhythmically correlated head and nose twitching. We present video documentation of such attacks and discuss their similarities to human epilepsy with myoclonic absences."

That's a **naturally occurring** myoclonic-absence-like phenotype in a companion animal, with the same defining feature — twitching rhythmically correlated with the spike-wave discharge. Different frequency (4 Hz vs 3 Hz), different body part (head/nose vs shoulders/arms), much shorter duration (1–2 s vs 8–60 s), but the same architecture. Evidence source: **MODEL_ORGANISM** per this repo's rules (veterinary observations count as animal, even when observational).

VBO breed term for Chihuahua: exists but **I did not verify the ID** — look it up before curating.

- **OMIA:** not checked this session; worth a look for canine idiopathic generalized epilepsy entries.
- **Zoonotic potential / cross-species transmission:** not applicable, obviously.
- **Comparative biology:** the thalamocortical spike-wave oscillator is deeply conserved across mammals — it's the same machinery in rodents, cats, dogs, and humans, which is why absence models translate reasonably well. The *motor recruitment* branch that makes EMA distinctive is the part that has never been modeled deliberately.

---

## 15. Model Organisms

### The honest headline: there is no EMA model

Nobody has built a mouse that has myoclonic absences. What exists are (a) good absence-epilepsy models that produce the 3 Hz-equivalent oscillation without the motor component, and (b) one model that happens to have *both* absence seizures and a paroxysmal motor phenotype, though they're separate events rather than the fused single seizure that defines EMA.

### Genetic models of the underlying oscillator

**GAERS** (Genetic Absence Epilepsy Rat from Strasbourg) and **WAG/Rij** rat — the two workhorse inbred absence models. Both show spontaneous spike-wave discharges with behavioral arrest and the classic pharmacological profile (suppressed by ethosuximide and valproate, worsened by carbamazepine and vigabatrin). They model **steps 1–4** of the EMA chain and none of step 5. *(Not fetched in this session — verify PMIDs before citing.)*

**tottering (*Cacna1a* mouse)** — the most EMA-adjacent model available. Missense mutation in *Cacna1a*, orthologue of human CACNA1A, in the pore-lining region of the P/Q-type Ca²⁺ channel. Three phenotypes: absence seizures with generalized spike-wave discharges (6–7 Hz in mouse), episodic dystonia, and mild ataxia. Critically, tottering shows "a striking downstream enhancement of α1G-mediated T-type currents in thalamic neurons **before** the onset of absence epilepsy" — i.e. a compensatory change in the thalamic burst-firing machinery precedes the seizures. That's a mechanistically interesting handle on how a channel defect converts into an oscillation.

**Limitation, stated plainly:** tottering's motor phenotype (60–90 minute dystonic attacks progressing along the body axis) is a *separate event* from its absence seizures. In EMA the motor and absence components are the same event, cycle-locked. So tottering models the *ingredients* but not the *fusion*.

Also worth noting: cerebellar neurons act as "powerful regulators of the pathological oscillations in the thalamocortical system" in *Cacna1a* models — an underexplored angle for EMA, where nobody has looked at the cerebellum.

**Genetic α1G/CACNA1G overexpression** — elevating α1G-mediated low-voltage-activated Ca²⁺ current in thalamus induces "pure absence epilepsy" (*J Neurosci* 29(6):1615). Useful as the *negative control* for the EMA question: this manipulation gives you absence **without** motor features, which sharpens the question of what EMA adds on top.

### Models for the EMA-associated genes

- ***Syngap1*** heterozygous mice — extensively characterized (premature excitatory synapse maturation, cognitive deficits, seizures). Good for the SYNGAP1 subgroup; not an EMA model per se.
- ***Slc2a1*** haploinsufficient mice — established GLUT1DS model with spike-wave discharges and motor deficits; responds to ketogenic diet. The most translationally useful model on this list.
- ***Setd1b*, *Glud1*, *Crebbp*** — models exist for all three, none characterized for myoclonic absence phenotypes.

### What's missing

No model recapitulates:
1. The **cycle-by-cycle time-locking** of cortical spike to muscle jerk (15–40 ms latency)
2. The **progressive tonic contraction** superimposed on the myoclonus
3. The **cognitive deterioration proportional to seizure duration**

A model that produced genuine cycle-locked corticospinal output during spike-wave would be the field-advancing tool here. This is a legitimate `HUMAN_MODEL_MISMATCH` discussion for the KB entry — evidence exists in models, but the models specifically lack the feature that defines the disease.

### Resources

MGI (mouse), RGD (rat — GAERS/WAG-Rij strains), IMPC/KOMP (knockouts for SYNGAP1, SETD1B, SLC2A1, GLUD1, CREBBP), Alliance of Genome Resources.

---

## Curation notes for the dismech entry

A few things I'd flag before this gets committed anywhere:

1. **Verify before use.** The HGNC IDs in §4, the CHEBI IDs for acetazolamide/lacosamide, the VBO Chihuahua term, the NCIT speech-therapy term, and any ICD-10 code are **not** OAK-verified in this session. Everything marked "OAK-verified" was checked against the local `sqlite:obo:*` adapters.
2. **NEC risk.** "MAE" is ambiguous between *myoclonic absence epilepsy* and *myoclonic-astatic epilepsy* (Doose). If any deep-research report is generated for this disease, run `just preflight-dr` and check the gene mentions — but note EMA has **no canonical causal gene** in MONDO, so preflight will likely return `SKIP` and you'll need the manual synonym/OMIM checks. The Doose collision is the specific thing to watch for.
3. **Two curatable controversies**, both worth `discussions` blocks:
   - **Why motor?** — the central open mechanistic question, with the Ikeda n=2 SPECT study as the only direct human evidence. `KNOWLEDGE_GAP`.
   - **Does treatment timing matter?** — Tang 2025 says course depends on GTCS "regardless of... treatment timing," while also saying cognitive decline tracks duration of intractable epilepsy. Direct internal tension. `KNOWLEDGE_GAP`.
   - Optionally a third: **levetiracetam** as second-line vs. absence-aggravating.
4. **Module conformance:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` is the natural target. Keep the motor-cortex-recruitment node as EMA-specific — don't push it up into the module.
5. **Evidence source tagging:** Ikeda 2018 (SPECT), all the cohort series, and the genetic case reports are `HUMAN_CLINICAL`. Poma 2010 (Chihuahua) is `MODEL_ORGANISM`. Any tottering/GAERS/α1G citations are `MODEL_ORGANISM`.
6. **Prevalence:** resist the urge to convert "0.5–1% of epilepsy patients" into a `rate_per_100000`. It's a proportion of a clinical population, not a population rate. `prevalence_class: NOT_YET_DOCUMENTED` with the figure in `notes` is the truthful curation.

---

## Sources

**Primary literature (PMIDs verified against PubMed records this session):**

- Tang F, Li M, Liu L, Wang X, Qin B. Research progress on epilepsy with myoclonic absence. *Acta Epileptol*. 2025. doi:10.1186/s42494-025-00218-2. [PMID:40380288](https://pubmed.ncbi.nlm.nih.gov/40380288/) · [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12082880/)
- Hu Q, Luo Y, Hong S, Yuan P, Jiang L. Electroclinical features of myoclonic absence epilepsy: A single-center cohort analysis in Southwest China. *Epilepsy Behav*. 2025 Oct;171:110505. [PMID:40414191](https://pubmed.ncbi.nlm.nih.gov/40414191/)
- Carter EG, Armour EA, Pagano LM, Reddy SB. Epilepsy with myoclonic absences: a case series highlighting clinical heterogeneity and surgical management. *Epileptic Disord*. 2022;24(3):541-547. [PMID:35770757](https://pubmed.ncbi.nlm.nih.gov/35770757/)
- Videira G, Raimundo R, Chorão R. Epilepsy with myoclonic absences: A case series. *Seizure*. 2023;106:162-163. [PMID:36893512](https://pubmed.ncbi.nlm.nih.gov/36893512/)
- Zanzmera P, Menon RN, Karkare K, et al. Epilepsy with myoclonic absences: Electroclinical characteristics in a distinctive pediatric epilepsy phenotype. *Epilepsy Behav*. 2016;64(Pt A):242-247. [PMID:27770719](https://pubmed.ncbi.nlm.nih.gov/27770719/)
- Ikeda H, Imai K, Ikeda H, et al. Ictal single photon emission computed tomographic study of myoclonic absence seizures. *Brain Dev*. 2018;40(2):126-129. [PMID:28823645](https://pubmed.ncbi.nlm.nih.gov/28823645/)
- Bureau M, Tassinari CA. Epilepsy with myoclonic absences. *Brain Dev*. 2005;27(3):178-84. [PMID:15737698](https://pubmed.ncbi.nlm.nih.gov/15737698/)
- Genton P, Bureau M. Epilepsy with myoclonic absences. *CNS Drugs*. 2006;20(11):911-916. [PMID:17044728](https://pubmed.ncbi.nlm.nih.gov/17044728/)
- Klitten LL, Møller RS, Nikanorova M, et al. A balanced translocation disrupts SYNGAP1 in a patient with intellectual disability, speech impairment, and epilepsy with myoclonic absences (EMA). *Epilepsia*. 2011;52(12):e190-3. [PMID:22050443](https://pubmed.ncbi.nlm.nih.gov/22050443/)
- Hiraide T, Hattori A, Ieda D, et al. De novo variants in SETD1B cause intellectual disability, autism spectrum disorder, and epilepsy with myoclonic absences. *Epilepsia Open*. 2019;4(3):476-481. [PMID:31440728](https://pubmed.ncbi.nlm.nih.gov/31440728/)
- Gökben S, Yılmaz S, Klepper J, et al. Video/EEG recording of myoclonic absences in GLUT1 deficiency syndrome with a hot-spot R126C mutation in the SLC2A1 gene. *Epilepsy Behav*. 2011;21(2):200-2. [PMID:21546317](https://pubmed.ncbi.nlm.nih.gov/21546317/)
- Bahi-Buisson N, El Sabbagh S, Soufflet C, et al. Myoclonic absence epilepsy with photosensitivity and a gain of function mutation in glutamate dehydrogenase. *Seizure*. 2008;17(7):658-64. [PMID:18321734](https://pubmed.ncbi.nlm.nih.gov/18321734/)
- Elia M, Musumeci SA, Ferri R, Cammarata M. Trisomy 12p and epilepsy with myoclonic absences. *Brain Dev*. 1998;20(2):127-30. [PMID:9545186](https://pubmed.ncbi.nlm.nih.gov/9545186/)
- Häusler M, Kluger G, Nikanorova M. Epilepsy with myoclonic absences — favourable response to add-on rufinamide treatment in 3 cases. *Neuropediatrics*. 2011;42(1):28-29. [PMID:21557146](https://pubmed.ncbi.nlm.nih.gov/21557146/)
- Myers KA, Scheffer IE. Myoclonic absence seizures with complex gestural automatisms. *Eur J Paediatr Neurol*. 2018;22(3):532-535. [PMID:29325826](https://pubmed.ncbi.nlm.nih.gov/29325826/)
- Aoun MA, Eisermann M, Chemaly N, et al. Jerking during absences: video-EEG and polygraphy of epileptic myoclonus associated with two paediatric epilepsy syndromes. *Epileptic Disord*. 2021;23(1):191-200. [PMID:33632671](https://pubmed.ncbi.nlm.nih.gov/33632671/)
- Poma R, Ochi A, Cortez MA. Absence seizures with myoclonic features in a juvenile Chihuahua dog. *Epileptic Disord*. 2010;12(2):138-41. [PMID:20483714](https://pubmed.ncbi.nlm.nih.gov/20483714/)
- Matsubara K, Yamakawa K, Ishioka R, et al. Epilepsy with myoclonic absences associated with a pathogenic CREBBP variant: A case report of Rubinstein-Taybi syndrome. *Seizure*. 2025;131:1-4. [PMID:40451035](https://pubmed.ncbi.nlm.nih.gov/40451035/)
- Specchio N, Wirrell EC, Scheffer IE, et al. ILAE classification and definition of epilepsy syndromes with onset in childhood. *Epilepsia*. 2022;63(6):1398-1442. [PMID:35503717](https://pubmed.ncbi.nlm.nih.gov/35503717/) · [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/epi.17241)
- Ogawa et al. Epilepsy with myoclonic absence presenting with unilateral jerks: A case of 2q13 microdeletion syndrome. *Seizure*. 2023. [PMID:36796225](https://pubmed.ncbi.nlm.nih.gov/36796225/)
- Chin HL, Chang J, Nordli D 3rd. Refining the electroclinical phenotype of 15q11.2 microdeletion: EEG biomarker overlap with Angelman syndrome. *Epileptic Disord*. 2026. [PMID:42434914](https://onlinelibrary.wiley.com/doi/10.1002/epd2.70328)
- Cherian A, Jabeen SA, Kandadai RM, et al. Epilepsy with myoclonic absences in siblings. *Brain Dev*. 2014. [PMID:24491945](https://pubmed.ncbi.nlm.nih.gov/24491945/)
- Auvin S, Chhun S, et al. Aggravation of absence seizure related to levetiracetam. *Eur J Paediatr Neurol*. 2011. [PMID:21680209](https://pubmed.ncbi.nlm.nih.gov/21680209/)
- Ito S, Nagumo K, et al. Low-dose phenobarbital for epilepsy with myoclonic absences. *Brain Dev*. 2021. [PMID:33461850](https://pubmed.ncbi.nlm.nih.gov/33461850/)
- Tassinari CA, Lyagoubi S, Santos V, et al. Studies on spike and wave discharges in man. II. Clinical and EEG aspects of myoclonic absences. *Electroencephalogr Clin Neurophysiol*. 1970. [PMID:4194033](https://pubmed.ncbi.nlm.nih.gov/4194033/) · original 1969 French paper [PMID:4985251](https://pubmed.ncbi.nlm.nih.gov/4985251/)
- Balestrini S, et al. Clinical and genetic landscape of epilepsies with absence seizures and single-gene etiology. *Epilepsia*. 2026. [doi:10.1111/epi.18655](https://onlinelibrary.wiley.com/doi/10.1111/epi.18655)

**Reference resources:**
- [epilepsydiagnosis.org — Epilepsy with Myoclonic Absences overview](https://www.epilepsydiagnosis.org/syndrome/epilepsy-myoclonic-absences-overview.html)
- [MedLink Neurology — Epilepsy with myoclonic absences](https://www.medlink.com/articles/epilepsy-with-myoclonic-absences) and [Myoclonic absences](https://www.medlink.com/articles/myoclonic-absences)
- [Jasper's Basic Mechanisms of the Epilepsies — The Voltage-Gated Calcium Channel and Absence Epilepsy](https://www.ncbi.nlm.nih.gov/books/NBK98208/)
- [Genetic Enhancement of Thalamocortical Network Activity by Elevating α1G-Mediated LVA Calcium Current Induces Pure Absence Epilepsy, *J Neurosci* 29(6):1615](https://www.jneurosci.org/content/29/6/1615)
- MONDO:0019487 via local OAK `sqlite:obo:mondo`; HPO/GO/CL/UBERON/CHEBI/NCIT terms verified via local OAK adapters