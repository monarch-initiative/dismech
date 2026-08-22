---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T07:14:16.562489'
end_time: '2026-08-20T07:19:22.493208'
duration_seconds: 305.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral
    Abnormalities
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
  web_search_requests: 20
  num_turns: 33
  total_cost_usd: 2.5482137000000007
  session_id: a2af77d9-bbdc-5701-9764-fc7421450a50
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 6
  verified: 5
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.167
  relevance_assessed: 5
  on_topic: 2
  unresolved_references:
  - DOI:10.1101/2025.04.09.646620](https://www.biorxiv.org/content/10.1101/2025.04.09.646620v2
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities** covering all of the
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

Now let me fetch the full PubMed abstract and GIM article for detailed clinical/mechanistic content.

I now have comprehensive material. Let me compile the full research report.

# Neurodevelopmental Disorder with Absent Speech and Movement and Behavioral Abnormalities (NEDSMB)

## 1. Disease Information

**Overview:** Neurodevelopmental disorder with absent speech and movement and behavioral abnormalities (NEDSMB) is an ultra-rare, autosomal recessive Mendelian disorder characterized by global developmental delay apparent from early infancy, severely impaired intellectual development with absent/mutistic speech, movement abnormalities (tremor, ataxia, limb dystonia), and significant neurobehavioral disturbance (self- and hetero-aggression, autistic features), accompanied by mild dysmorphic features and hypodontia (OMIM #620270; MalaCards, accessed 2026) [1][2]. It was first delineated in 2023 as one of two novel biallelic HECT-domain E3-ubiquitin-ligase disease genes (the other being *HECTD4*) identified in a cohort of patients with syndromic neurodevelopmental, seizure, and movement phenotypes whose presentation overlapped with — but was genetically distinct from — Angelman syndrome [3].

**Key identifiers:**
- **OMIM phenotype:** #620270 (NEDSMB) [1]
- **OMIM gene:** *614454 — UBIQUITIN PROTEIN LIGASE E3C; UBE3C [4]
- **MONDO:** MONDO:0859519 [2]
- **HGNC gene symbol:** UBE3C (chromosome 7q36) [1]
- **Inheritance:** Autosomal recessive (biallelic loss-of-function) [1][3]

**Synonyms:** NEDSMB (OMIM abbreviation) [1]. It belongs to a large, systematically-named family of "Neurodevelopmental disorder with X" OMIM entries generated from large-scale exome/genome sequencing efforts (e.g., the DDD study), and should not be confused with phenotypically similar but genetically distinct entries such as NEDBASH (*NTNG2*, OMIM #618718), NEDHISB (*GNAI1*, OMIM #619854), or NEDPM (*ACBD6*, OMIM #620785) [search results].

**Evidence basis:** All currently published clinical data derive from a small aggregated case series (individual patient-level phenotyping) rather than a population-level disease registry — specifically, sisters from a consanguineous family plus an additional unrelated case, reported in the founding genetics paper [3][1]. No epidemiological registry, GeneReviews chapter, or large natural-history cohort yet exists given the extreme rarity and recency of the gene-disease association (first reported late 2022/2023).

---

## 2. Etiology

**Disease causal factor:** NEDSMB is caused by biallelic (homozygous or compound heterozygous) loss-of-function (LoF) variants in *UBE3C*, encoding a HECT-domain E3 ubiquitin-protein ligase [3][1]. The founding study, Faqeih et al. (2023), *Genetics in Medicine* (PMID: 36401616), used chromosomal analysis and exome sequencing in 10 patients from 7 unrelated families with syndromic neurodevelopmental/seizure/movement/behavioral phenotypes [3]:

> "In 3 patients from 2 families with Angelman-like syndrome, paralog-directed candidate gene approach detected 2 LoF variants in the other candidate E3 ligase gene, UBE3C, a paralog of the Angelman syndrome E3 ligase gene, UBE3A. The RNA studies in 4 patients with LoF variants in HECTD4 and UBE3C provided evidence for the LoF effect." [3]

**Reported variant types:**
- A homozygous frameshift variant in two affected sisters born to consanguineous parents, identified by exome sequencing and confirmed by Sanger sequencing (present heterozygous in each unaffected parent) — patient cells showed markedly reduced UBE3C expression, consistent with nonsense-mediated mRNA decay and a loss-of-function mechanism [3][search result].
- A homozygous ~185-kb genomic deletion spanning the first 17 exons of *UBE3C* (7q36.3) in a 20-year-old man born to consanguineous Turkish parents, identified via GeneMatcher-facilitated data sharing [search result].

**Risk factors:**
- *Genetic:* Biallelic *UBE3C* LoF is necessary and sufficient; parental consanguinity is a strong enabling risk factor observed in all reported families (Saudi and Turkish consanguineous unions) [3][search result]. Carrier (heterozygous) parents are clinically unaffected, consistent with recessive inheritance.
- *Environmental:* None identified or plausible for a monogenic loss-of-function disorder; no environmental modifiers have been reported.
- No modifier genes, protective variants, or gene–environment interaction data have yet been published given the disorder's very recent description.

**Related but mechanistically/gene-distinct spectrum:** Heterozygous de novo missense and LoF *UBE3C* variants have separately been reported as candidate/strong-candidate risk alleles for autism spectrum disorder (ASD) in large de novo variant discovery cohorts (Simons Simplex Collection), distinct from the biallelic NEDSMB mechanism:
> "Two de novo missense variants and an inherited LoF variant that was not transmitted to an unaffected sibling have been observed in ASD probands from the Simons Simplex Collection" [SFARI Gene]

SFARI Gene currently scores *UBE3C* as **Category 2 (Strong Candidate)** for autism risk, citing PMID:22495309, 23160955 (O'Roak et al. 2012), 26401017 (Iossifov et al. 2015, *PNAS*), 27525107 (Yuen et al. 2016), 36401616 (Faqeih et al. 2022/2023), 37506195 (Cirnigliaro et al. 2023), 39769462 (Vijay Gupta et al. 2024), and 40869941 (Repiska et al. 2025) [SFARI Gene database]. This heterozygous-ASD association is genetically and mechanistically distinct from the biallelic recessive NEDSMB phenotype and should be curated as a separate gene–phenotype relationship (relationship_type: SUSCEPTIBILITY, if modeled) rather than conflated with the Mendelian recessive disease.

---

## 3. Phenotypes

Reported phenotypic features (from the two affected sisters and the Turkish index case) [3][search results]:

| Phenotype | Type | Suggested HPO term | Notes |
|---|---|---|---|
| Global developmental delay (from early infancy) | Symptom/sign | HP:0001263 (Global developmental delay) | Onset: infancy |
| Severely impaired intellectual development | Symptom/sign | HP:0010864 (Severe intellectual disability) | |
| Absent speech / mutism | Symptom/sign | HP:0001344 or HP:0002465 (Mutism) / HP:0007344 (Absent speech, if curated) | Core feature per disease name |
| Hypotonia | Symptom/sign | HP:0001252 (Hypotonia) | Reported in original two sisters |
| Tremor | Symptom/sign | HP:0001337 (Tremor) | Movement abnormality |
| Ataxia | Symptom/sign | HP:0001251 (Ataxia) | Movement abnormality |
| Limb dystonia | Symptom/sign | HP:0002451 (Limb dystonia) | Movement abnormality |
| Self-injurious/aggressive behavior | Behavioral | HP:0100716 (Self-injurious behavior) / HP:0000718 (Aggressive behavior) | "self- and hetero-aggression" |
| Autistic features | Behavioral | HP:0000729 (Autistic behavior) | |
| Macrostomia | Physical/dysmorphic | HP:0000154 (Macrostomia) | |
| Large mandible | Physical/dysmorphic | HP:0000303 (Mandibular prognathia) or similar | |
| Open-mouthed expression | Physical/dysmorphic | HP:0410006 or descriptive | |
| Hypodontia | Physical/dysmorphic | HP:0000668 (Hypodontia) | Named in disease title/description |
| Conductive hearing loss | Sensory | HP:0000405 (Conductive hearing impairment) | |
| Myopia | Sensory | HP:0000545 (Myopia) | |
| Transient obesity (1 patient) | Growth | HP:0001513 (Obesity) | Reported in only 1 patient — low frequency |

**Severity/progression:** Described as a static or slowly evolving global developmental encephalopathy rather than a degenerative process; no published longitudinal natural-history data on progression rate or life-course trajectory exist yet given the small case series.

**Frequency:** With only ~3 genetically confirmed cases published to date (2 sisters + 1 unrelated Turkish patient), most phenotype frequencies cannot be meaningfully quantified beyond "reported in the described patients" — curators should avoid fabricating percentage frequencies and instead cite frequency as qualitative/case-based (e.g., "observed in the reported cohort") per dismech's frequency-evidence guidance.

**Quality of life impact:** Severely impaired intellectual development, absent functional speech, and aggressive/self-injurious behavior imply substantial impact on independence, communication, and caregiver burden, consistent with other severe autosomal recessive intellectual disability syndromes; no disease-specific QOL instrument data (EQ-5D, SF-36) have been published.

---

## 4. Genetic/Molecular Information

**Causal gene:** *UBE3C* (HGNC gene symbol UBE3C; OMIM *614454), chromosome 7q36 [1][4].

**Gene product:** UBE3C is a ~126-kDa HECT (Homologous to E6-AP C-Terminus)-domain E3 ubiquitin-protein ligase (UniProt Q5T447; EC 2.3.2.26) [search results]. It is a paralog of *UBE3A*, the gene responsible for Angelman syndrome, which explains the substantial clinical overlap between NEDSMB and Angelman-like presentations [3].

**Variant classification observed:**
- Homozygous frameshift variant (PTC-generating, loss-of-function via nonsense-mediated decay) — 2 affected sisters [3]
- Homozygous ~185-kb structural deletion removing exons 1–17 of *UBE3C* — 1 unrelated patient (Turkish, consanguineous) [search result]
- Compound heterozygous LoF variants also reported among the 3 UBE3C-affected patients from 2 families in the founding paper [3]

**Functional consequence:** Loss of function. RNA/expression studies in patient-derived cells demonstrated markedly reduced UBE3C transcript/protein levels compared to controls, consistent with nonsense-mediated mRNA decay of the mutant allele and haploinsufficiency-in-trans (biallelic null) mechanism [3].

**Allele frequency:** LoF variants in *UBE3C* were reported as rare and "absent from controls as homozygous" in gnomAD-scale population databases [3] — consistent with a severe, fully penetrant recessive disease allele under purifying selection.

**Somatic vs. germline:** All reported variants are germline, inherited in autosomal recessive fashion from unaffected heterozygous consanguineous parents [3].

**Epigenetic/chromatin information:** No disease-specific DNA methylation or histone modification studies have been published for NEDSMB. However, a major 2025 mechanistic paper (see Section 6) implicates UBE3C in **epitranscriptomic** (RNA m6A methylation) — not DNA-epigenetic — regulation during cortical development, a distinct but related layer of gene-expression control [5].

**Chromosomal abnormalities:** The 185-kb deletion spanning *UBE3C* exons 1–17 (7q36.3) constitutes a large structural genomic lesion detectable by chromosomal microarray/exome CNV calling, in addition to the point/frameshift variant class [search result].

---

## 5. Environmental Information

No environmental risk factors, toxin exposures, lifestyle factors, or infectious triggers have been identified or are mechanistically plausible for this monogenic loss-of-function disorder. As a fully genetically determined biallelic recessive condition, disease occurrence is governed by inheritance of two null alleles, most commonly enabled by parental consanguinity rather than by exposure.

---

## 6. Mechanism / Pathophysiology

**Protein function and normal biology:** UBE3C is a HECT-type E3 ubiquitin ligase that forms a covalent thioester intermediate with ubiquitin via a conserved catalytic cysteine in its C-terminal HECT domain (crystallized structure: PDB 6K2C) before transferring ubiquitin to substrate proteins, receiving ubiquitin from E2 conjugating enzymes such as UBE2D1 (and, less efficiently, UBE2L3) [search results]. UBE3C physically associates with the 26S proteasome (interacting with the S2/Rpn1 subunit) and builds Lys-29- and Lys-48-linked polyubiquitin chains on proteasome-engaged, partially-degraded substrates, thereby **enhancing proteasome processivity** — ensuring complete degradation of difficult/stable substrates rather than release of truncated degradation products [PMID:24158444; search results]:

> "In the absence of Hul5p/UBE3C, the proteasome is less able to completely degrade particularly stable proteins, leaving behind a truncated product." [search result]

Suggested GO terms: **GO:0061630** (ubiquitin protein ligase activity), **GO:0004842** (ubiquitin-protein transferase activity), **GO:0043161** (proteasome-mediated ubiquitin-dependent protein catabolic process), **GO:0000209** (protein polyubiquitination).

**Disease mechanism — causal chain (established, human genetic evidence: PMID:36401616):**
1. **Trigger:** Biallelic LoF variant in *UBE3C* (frameshift, structural deletion, or compound heterozygous LoF) [3]
2. **Molecular consequence:** Nonsense-mediated decay of mutant transcript → markedly reduced/absent UBE3C protein → loss of HECT E3 ligase activity [3]
3. **Cellular consequence (established via paralogy with UBE3A/Angelman mechanism, and directly evidenced in the 2025 mechanistic study below):** Disrupted ubiquitin-proteasome-mediated protein turnover / disrupted substrate ubiquitination in neurons
4. **Clinical manifestation:** Global neurodevelopmental impairment, absent speech, movement abnormalities (tremor, ataxia, dystonia), and behavioral disturbance, phenotypically overlapping with Angelman syndrome (caused by loss of the UBE3C paralog UBE3A) [3]

**Emerging mechanistic detail — cortical neurogenesis and the epitranscriptome (model-organism/in-vitro evidence, EMERGING; Borisova, Ambrozkiewicz et al., bioRxiv 2025, DOI:10.1101/2025.04.09.646620, posted April 2025):**
> "The neurodevelopmental disorder-associated ubiquitin ligase UBE3C regulates the cellular composition of the murine cerebral cortex and human brain organoids, with its loss favoring neurogenesis and suppressing glial fate. Disease-associated UBE3C mutations alter its autoubiquitination activity and disrupt cortical lamination. Proteomic profiling of UBE3C-deficient forebrains and organoids identifies Cbll1 as a UBE3C substrate, and the UBE3C-Cbll1 duo drives N6-methyladenosine (m6A) mRNA methylation. Hyperactivation of m6A writers in UBE3C-deficient neural progenitors impairs cell cycle exit, a defect reversible in vivo by the METTL3 inhibitor STM2457." [5]

This establishes a novel causal chain, evidenced in mouse cortex and human brain organoids (IN_VITRO / MODEL_ORGANISM evidence source):
- UBE3C loss/dysfunction → altered autoubiquitination and stabilization of the substrate **Cbll1 (Hakai)** → dysregulated m6A RNA methylation writer activity (implicating METTL3) → impaired neural progenitor cell-cycle exit → **skewed neurogenesis vs. gliogenesis balance** and **disrupted cortical lamination** [5]

This is a genuine, biologically important **HUMAN_MODEL_MISMATCH**-flavored knowledge gap: the mechanistic chain (Cbll1/m6A/METTL3/cortical lamination) is established in mouse forebrain and human organoid model systems but has not yet been directly confirmed in human patient brain tissue — appropriate for a `HUMAN_MODEL_MISMATCH` discussion node if curated into a pathophysiology graph, given that mouse cortical lamination and organoid neurogenesis timing only partially recapitulate human corticogenesis. Pharmacologic rescue with the METTL3 inhibitor STM2457 is a notable translational/drug-target lead (in vivo mouse evidence) [5].

**Cell types involved:** Neural progenitor cells / radial glia (cortical neurogenesis), differentiating cortical neurons, glial precursors (Cell Ontology candidates: CL:0000047 neural stem cell / CL:0002608 radial glial cell, CL:0000031 neuroblast).

**Relationship to Angelman syndrome:** UBE3C is the closest human paralog of UBE3A, and NEDSMB was explicitly identified through a "paralog-directed candidate gene approach" in patients with Angelman-like clinical presentation who lacked a UBE3A/15q11-q13 diagnosis, expanding the differential for "Angelman-negative" suggestive presentations [3]. This makes NEDSMB a strong candidate for `conforms_to` linkage to relevant ubiquitin-proteostasis or Angelman-adjacent mechanism content if/when such a dismech module exists, though the KB does not currently list a dedicated UBE3A/Angelman mechanism module among those enumerated in this project.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Primarily the **central nervous system** (cerebral cortex, cerebellum [ataxia], basal ganglia/motor circuits [dystonia, tremor]); secondarily craniofacial/dental structures (mandible, dentition) and the auditory and visual systems (conductive hearing loss, myopia) [3][search results].
- **Suggested UBERON terms:** UBERON:0000955 (brain), UBERON:0001851 (cortex), UBERON:0002037 (cerebellum), UBERON:0002020 (gray matter/basal ganglia structures), UBERON:0003129 (skull/mandible), UBERON:0001091 (tooth), UBERON:0001846 (middle ear structures — conductive hearing loss), UBERON:0000970 (eye — myopia).
- **Tissue/cell level:** Cortical neural progenitor cells and their neuronal/glial progeny (per the 2025 organoid/mouse mechanistic study) [5]; suggested CL terms: CL:0002608 (radial glial cell), CL:0000540 (neuron), CL:0000127 (astrocyte)/CL:0000128 (oligodendrocyte) as glial lineages suppressed by UBE3C loss.
- **Subcellular level:** UBE3C functions at the **26S proteasome** (GO:0000502 proteasome complex) and in cytosolic/nuclear ubiquitin-proteasome machinery; suggested GO Cellular Component: GO:0000502 (proteasome complex), GO:0005829 (cytosol).
- **Laterality:** Not applicable/not reported — a systemic neurodevelopmental disorder without lateralized findings.

---

## 8. Temporal Development

- **Onset:** Congenital/early infancy — "global developmental delay apparent from early infancy" [search results, citing OMIM #620270].
- **Onset pattern:** Insidious/static neurodevelopmental (not acute), consistent with other biallelic ubiquitin-pathway intellectual disability syndromes.
- **Progression:** No formal staging system exists; published cases (children/young adults, including a 20-year-old patient) suggest the condition is compatible with survival into adulthood with persistent severe intellectual disability, but detailed natural-history/longitudinal progression data have not been published.
- **Course pattern:** Best characterized as a stable/non-degenerative developmental encephalopathy based on available case descriptions, though this has not been formally studied.
- **Critical periods:** The 2025 mechanistic study suggests a developmental critical window during cortical neurogenesis (neural progenitor cell-cycle exit) as the point of vulnerability, with pharmacological rescue (METTL3 inhibition) shown effective specifically during that embryonic/perinatal developmental window in mouse models [5] — an important consideration for any future therapeutic-timing discussion.

---

## 9. Inheritance and Population

- **Epidemiology:** Extremely rare/ultra-rare; fewer than five genetically confirmed patients have been published in the literature to date (2 sisters plus 1 unrelated case in the founding paper, plus possibly additional cases in later series) [3][search result]. No formal prevalence or incidence estimate exists; classify as `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE` per dismech's structured prevalence schema, explicitly avoiding fabricated per-100,000 rates.
- **Inheritance pattern:** Autosomal recessive (biallelic LoF) [1][3] — suggested HPO inheritance term: **HP:0000007** (Autosomal recessive inheritance).
- **Penetrance:** Appears fully penetrant in reported homozygous/compound-heterozygous individuals (all molecularly confirmed cases are clinically affected); no incomplete-penetrance carriers reported (consistent with recessive LoF disease biology).
- **Expressivity:** Some variability is evident even among the founding pair of affected sisters (differing severity of individual dysmorphic/behavioral features, e.g., "transient obesity" reported in only 1 of the patients), suggesting some phenotypic variability, though the n is too small for firm conclusions.
- **Consanguinity:** A major recognized risk factor — all reported families are consanguineous (Saudi Arabian and Turkish kindreds) [3][search result].
- **Carrier frequency:** Not established; given the extreme rarity of reported cases, population carrier frequency for specific *UBE3C* LoF alleles is expected to be very low, and no gnomAD-scale carrier-frequency estimate has been published specifically for NEDSMB-causing alleles.
- **Affected populations/geographic distribution:** Reported cases originate from Saudi Arabian and Turkish consanguineous families [3][search result]; no broader geographic or ethnic distribution data exist. This should not be interpreted as a founder-population-restricted disease — rather, ascertainment reflects clinical genetics referral patterns (consanguinity increases detection of rare recessive conditions) combined with the disorder's overall rarity.
- **Sex ratio:** Insufficient data (2 of 3 index cases are female siblings; 1 is male) to establish a sex ratio; no biological basis (autosomal gene) to expect sex-differential risk.

---

## 10. Diagnostics

- **Molecular/genetic testing (primary diagnostic modality):**
  - **Exome sequencing (WES)** is the modality by which all reported cases were identified, given the disorder's genetic and phenotypic heterogeneity overlap with Angelman syndrome and other recessive ID syndromes [3].
  - **Chromosomal microarray (CMA)** is relevant for detecting large structural deletions, as demonstrated by the 185-kb *UBE3C* exon 1–17 deletion identified in one patient [search result].
  - Given the paralog relationship to *UBE3A*, **UBE3A/15q11-q13 methylation and sequencing testing (standard Angelman syndrome workup)** would typically be performed first and return negative/inconclusive in NEDSMB patients, prompting broader paralog-directed or exome-wide analysis — this "Angelman-negative" diagnostic pathway is explicitly how the gene was discovered [3].
  - No single-gene panel, targeted *UBE3C* Sanger-only test, or standardized clinical diagnostic criteria (DSM/ICD) currently exist for this very recently described condition; it is not yet listed in GeneReviews or major commercial gene-panel curricula as of this writing (2026), reflecting its 2023 initial description.
- **Differential diagnosis:** Angelman syndrome (UBE3A/15q11-q13), other biallelic HECT-ligase disorder *HECTD4*-associated NDD (described in the same founding paper), and other autosomal recessive syndromic intellectual disability disorders presenting with absent speech, ataxia, and behavioral abnormalities (e.g., NEDBASH/*NTNG2*, NEDHISB/*GNAI1*) [3][search results].
- **Screening:** No population or newborn screening program exists (ultra-rare Mendelian disorder); genetic counseling and carrier testing are relevant within consanguineous families with a previously affected child.
- **Omics-based diagnostics:** RNA studies (transcript-level expression analysis in patient fibroblasts/lymphoblasts) were used as functional confirmation of the loss-of-function mechanism in the founding paper, showing reduced UBE3C transcript consistent with nonsense-mediated decay [3] — this remains a research-confirmatory rather than routine clinical diagnostic test.

---

## 11. Outcome/Prognosis

No formal survival, mortality, or standardized quality-of-life outcome data have been published for NEDSMB given its extreme rarity and recent description. Reported patients include individuals who have survived into young adulthood (a 20-year-old man in one report), suggesting the condition is not associated with early lethality, but no systematic natural-history study, life-expectancy estimate, or validated prognostic biomarker exists. Prognosis is expected to be dominated by lifelong severe intellectual disability, absent functional speech, and behavioral/psychiatric comorbidity (aggression, self-injury) requiring long-term supportive/behavioral management, by analogy to other severe biallelic ubiquitin-pathway intellectual disability syndromes, though this inference should be explicitly flagged as extrapolated rather than disease-specific evidence.

---

## 12. Treatment

**Currently no disease-specific, FDA-approved, or trial-validated pharmacotherapy exists for NEDSMB.** Management is expected to be entirely supportive/symptomatic, extrapolated from general practice for severe syndromic neurodevelopmental disorders:

- **Supportive/rehabilitative care:** Physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), speech-language therapy (NCIT:C159273) — despite absent speech, augmentative/alternative communication approaches are standard for nonverbal neurodevelopmental disorders.
- **Behavioral management:** Behavioral counseling/intervention (NCIT:C181743) for aggression and self-injurious behavior; applied behavior analysis approaches used in other severe ID/autism-spectrum conditions may be extrapolated but are not disease-specific evidence.
- **Symptomatic pharmacotherapy:** No published reports of specific drug trials in NEDSMB patients; management of movement abnormalities (tremor, dystonia) and behavioral symptoms would follow general symptomatic pharmacologic approaches used in other genetic intellectual disability syndromes (e.g., antipsychotics or alpha-agonists for aggression, dystonia-directed therapy), but none of this is disease-specific published evidence and should not be curated as NEDSMB-specific treatment without a primary citation.
- **Experimental/preclinical lead (NOT yet a treatment, translational significance only):** The 2025 bioRxiv mechanistic study demonstrated that the **METTL3 inhibitor STM2457** reversed the neural progenitor cell-cycle-exit defect caused by UBE3C deficiency in an in vivo mouse model [5]:
  > "a defect reversible in vivo by the METTL3 inhibitor STM2457" [5]
  This represents an important preclinical/model-organism (MODEL_ORGANISM evidence_source) proof-of-concept for a targeted molecular therapy (small-molecule METTL3/m6A-writer inhibition) addressing the downstream epitranscriptomic consequence of UBE3C loss, but has not been tested in human NEDSMB patients and should be curated as an experimental/preclinical `target_mechanisms` lead rather than an established treatment.
- No gene therapy, cell therapy, or RNA-based (ASO/siRNA) therapeutic approaches have been reported for this disorder.

---

## 13. Prevention

As a fully genetically determined autosomal recessive disorder with no environmental component, prevention is limited to:
- **Genetic counseling** for consanguineous families or those with a previously affected child, given the demonstrated autosomal recessive inheritance pattern (NCIT:C15240, Genetic Counseling) [3].
- **Carrier screening / prenatal or preimplantation genetic testing** would be technically feasible once a familial pathogenic *UBE3C* variant is identified, though this has not been reported as implemented for this specific ultra-rare condition.
- No immunization, primary public-health, or population-based screening measures are applicable.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife cases of *UBE3C*-associated disease have been reported (searched OMIA-type sources without hits). The murine ortholog *Ube3c* (MGI:2140998) has been studied primarily in engineered laboratory mouse models (see Section 15) rather than as a model of spontaneous natural disease.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBITaxon:10090):** The principal model system used to date. Conditional/floxed *Ube3c* alleles exist (e.g., Cyagen Ube3c-flox, C57BL/6JCya-Ube3c^em1flox^) [search result], and the 2025 Borisova/Ambrozkiewicz et al. bioRxiv study used *Ube3c*-deficient murine forebrain/cortex to demonstrate:
  - Altered cellular composition of the cerebral cortex (favoring neurogenesis, suppressing gliogenesis) upon UBE3C loss [5]
  - Disrupted cortical lamination with disease-associated UBE3C mutations (altered autoubiquitination activity) — a strong `RECAPITULATES`/`PARTIALLY_RECAPITULATES` candidate for structured `animal_models.modeled_mechanisms` curation, given it directly models a disease-relevant molecular lesion class (altered autoubiquitination) [5]
  - Rescue of the neural progenitor cell-cycle-exit defect by in vivo METTL3 inhibitor (STM2457) administration [5]
  - **Model fidelity caveat:** murine cortical neurogenesis timing, six-layer lamination proportions, and outer radial glia/OSVZ biology only partially mirror the human cerebral cortex, so translational claims from the mouse cortical-lamination phenotype to the human NEDSMB phenotype should carry a `HUMAN_MODEL_MISMATCH` caveat rather than being treated as directly confirmatory.
- **Human iPSC-derived brain organoids:** Used in parallel with the mouse model in the same 2025 study to confirm that UBE3C loss favors neurogenesis over gliogenesis and drives the same Cbll1/m6A axis in a human cellular system, partially addressing (but not fully resolving) the mouse-to-human translational gap [5].
- **Patient-derived cells (fibroblasts/lymphoblasts):** Used for RNA expression studies confirming nonsense-mediated decay/loss-of-function in the founding 2023 genetics paper — an IN_VITRO evidence source directly from human cells, distinct from the mouse/organoid mechanistic work [3].
- No zebrafish, *Drosophila*, *C. elegans*, or yeast *UBE3C*-specific disease models were identified in this search, though the S. cerevisiae ortholog **Hul5** was referenced as informing the general biochemical understanding of HECT-ligase proteasome-processivity function (not disease modeling per se) [search result].

---

## Sources

- [Neurodevelopmental Disorder with Absent Speech and Movement and Behavioral Abnormalities - MalaCards](https://www.malacards.org/card/neurodevelopmental_disorder_with_absent_speech_and_movement_and_behavioral_abnormalities)
- [Entry - #620270 - OMIM](https://omim.org/entry/620270)
- [Clinical Synopsis - #620270 - OMIM](https://www.omim.org/clinicalSynopsis/620270)
- [Entry - *614454 - UBIQUITIN PROTEIN LIGASE E3C; UBE3C - OMIM](https://www.omim.org/entry/614454)
- Faqeih EA, et al. "Biallelic variants in HECT E3 paralogs, HECTD4 and UBE3C, encoding ubiquitin ligases cause neurodevelopmental disorders that overlap with Angelman syndrome." *Genet Med.* 2023. [PubMed PMID: 36401616](https://pubmed.ncbi.nlm.nih.gov/36401616/) / [Genetics in Medicine full text](https://www.gimjournal.org/article/S1098-3600(22)00987-X/fulltext)
- Borisova E, Cuthill KJ, Dannenberg R, et al. "UBE3C links ubiquitin signaling to epitranscriptomic control of cortical neurogenesis." bioRxiv, April 2025. [DOI:10.1101/2025.04.09.646620](https://www.biorxiv.org/content/10.1101/2025.04.09.646620v2) / [Max Delbrück Center summary](https://www.mdc-berlin.de/research/publications/ube3c-links-ubiquitin-signaling-epitranscriptomic-control-cortical)
- [UBE3C Gene - SFARI Gene Database](https://gene.sfari.org/database/human-gene/UBE3C) (Category 2 – Strong Candidate; citing PMID 22495309, 23160955, 26401017, 27525107, 36401616, 37506195, 39769462, 40869941)
- [The E3 Ubiquitin Ligase UBE3C Enhances Proteasome Processivity by Ubiquitinating Partially Proteolyzed Substrates - PubMed PMID:24158444](https://pubmed.ncbi.nlm.nih.gov/24158444/)
- [UBE3C Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=UBE3C)
- [RCSB PDB 6K2C - Extended HECT domain of UBE3C E3 Ligase](https://www.rcsb.org/structure/6K2C)
- [Ube3c MGI Mouse Gene Detail - MGI:2140998](https://www.informatics.jax.org/marker/MGI:2140998)
- Iossifov I, et al. "Low load for disruptive mutations in autism genes and their biased transmission." *PNAS* 2015. [PubMed PMID: 26401017](https://pubmed.ncbi.nlm.nih.gov/26401017/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1101/2025.04.09.646620](https://www.biorxiv.org/content/10.1101/2025.04.09.646620v2` (1 mention) - Identifier did not resolve to a record