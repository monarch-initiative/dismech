---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-17T22:49:44.044821'
end_time: '2026-07-17T22:55:00.971954'
duration_seconds: 316.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KCNQ2 Developmental and Epileptic Encephalopathy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 9
  num_turns: 12
  total_cost_usd: 1.68818425
  session_id: 4a2ba45e-f479-471d-8ddd-31ce21930e0a
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KCNQ2 Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KCNQ2 Developmental and Epileptic Encephalopathy** covering all of the
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

Alright, I've got a solid evidence base pulled from GeneReviews, OMIM, Orphanet, and the primary literature. Here's the full report. One housekeeping note up front, in the spirit of this project's anti-hallucination rules: I've marked which PMIDs I verified live against PubMed versus which came from secondary sources (GeneReviews/reviews) and should get a `just fetch-reference` pass before they land in a KB entry.

---

# KCNQ2 Developmental and Epileptic Encephalopathy — Research Report

sup Harry. So this one's a potassium-channel gene that, when it misfires in a newborn's brain, basically turns the volume knob on neuronal firing the wrong way during the most delicate week of a person's life. Here's the whole picture, section by section.

> **PMID verification key:** ✅ = I confirmed the PMID/DOI live this session. 🔶 = citation pulled from a secondary source (GeneReviews, review article) — verify with `just fetch-reference` before curating, per the DR-verification SOP in CLAUDE.md.

---

## 1. Disease Information

**What it is.** KCNQ2 developmental and epileptic encephalopathy (KCNQ2-DEE, historically "KCNQ2 encephalopathy" or Early Infantile Epileptic Encephalopathy type 7 / EIEE7) is the severe end of a spectrum of disorders caused by variants in *KCNQ2*, the gene for the Kv7.2 voltage-gated potassium channel subunit. Think of Kv7.2 as a brake pedal on neurons; when it fails, the neonatal brain seizes in the first days of life and — unlike the benign twin condition — development doesn't recover.

The *KCNQ2* spectrum runs from **self-limited familial neonatal epilepsy (SLFNE**, formerly benign familial neonatal convulsions/seizures) at the mild end, where seizures vanish by 6–12 months and development is normal, to **neonatal-onset DEE** at the severe end, where the same-timed seizures come with lifelong moderate-to-profound intellectual disability. Same gene, wildly different lives, and the difference is mostly *how badly* the channel is broken (GeneReviews, *KCNQ2-Related Disorders*, 2022 update 🔶).

**Key identifiers:**
- **OMIM:** 613720 (Developmental and Epileptic Encephalopathy 7, DEE7); 121200 (Seizures, benign familial neonatal, 1 / BFNS1); 602235 (the *KCNQ2* gene itself)
- **MONDO:** MONDO:0013387 (developmental and epileptic encephalopathy, 7)
- **Orphanet:** ORPHA:439218 (KCNQ2-related developmental and epileptic encephalopathy); the SLFNE end maps to ORPHA:266
- **ICD-11:** 8A62 (Developmental and epileptic encephalopathies); **ICD-10:** G40.4 / roughly the "other generalized epilepsy and epileptic syndromes" bucket
- **MeSH:** covered under "Spasms, Infantile" / "Epilepsy, Benign Neonatal" (D020936) and "Epileptic Syndromes"
- **HGNC gene:** `hgnc:6296` (KCNQ2)

**Synonyms:** KCNQ2 encephalopathy, KCNQ2-DEE, EIEE7, DEE7, neonatal-onset KCNQ2-DEE (NEO-DEE); the mild sibling is BFNC/BFNS/SLFNE.

**Data provenance.** Most knowledge here is **aggregated disease-level** (case series, functional-genetics cohorts, GeneReviews), not EHR-derived. Patient-registry data exist through the KCNQ2 Cure Alliance and the RIKEE (Rational Intervention for KCNQ2/3 Epileptic Encephalopathy) variant database, but the foundational literature is cohort- and family-based.

---

## 2. Etiology

**Primary cause: genetic, monogenic.** Heterozygous variants in *KCNQ2* (chromosome 20q13.33). No environmental or infectious cause — this is a Mendelian channelopathy full stop.

**The clean split by variant mechanism** (this is the load-bearing concept for the whole disease):
- **Dominant-negative loss-of-function → severe neonatal DEE.** A missense variant makes a poison subunit that drags down the wild-type subunits it co-assembles with, cutting M-current by **>50%** rather than the ~25% a simple haploinsufficiency would give. This is the classic KCNQ2-DEE mechanism (Miceli et al., 2013 🔶; Weckhuysen et al., 2012, PMID:22275249 ✅).
- **Simple/partial loss-of-function (haploinsufficiency) → mild SLFNE.** Truncations, whole-gene deletions, ~20–30% M-current reduction. Seizures resolve, development normal.
- **Gain-of-function → a different, non-neonatal-seizure phenotype.** GoF variants (e.g., R201C/R201H, R144, R198Q) hyperpolarize channel activation, silence neurons too *much*, and produce **neonatal encephalopathy with non-epileptic myoclonus, later-onset DEE, autism/ID with language impairment — often WITHOUT neonatal seizures.** The absence of neonatal seizures is the single best clinical tell for GoF (Mulkey et al., 2017 🔶; Miceli et al., 2015 🔶; the R144 GoF paper, *eBioMedicine* 2022 🔶).

**Risk factors.** Essentially none beyond carrying the variant. Because severe KCNQ2-DEE variants are overwhelmingly **de novo**, there's no meaningful "risk factor" story — no maternal exposure, no prematurity link, no infection. Family history matters only for the milder inherited SLFNE end.

**Protective factors.** None genetically established. The most interesting "protective" signal is therapeutic timing, not innate: earlier initiation of sodium-channel-blocker therapy may blunt phenotype severity (see §12).

**Gene–environment interactions.** No established GxE for KCNQ2-DEE. This is about as close to "pure genotype" as neurodevelopmental disease gets.

---

## 3. Phenotypes

The core clinical picture, with suggested HPO terms and frequencies drawn from Weckhuysen 2012 (PMID:22275249 ✅) and GeneReviews 🔶:

| Phenotype | HPO term | Onset | Frequency | Notes |
|---|---|---|---|---|
| Neonatal-onset seizures | Neonatal onset (HP:0003623); Seizure (HP:0001250) | Median **day 1** of life, almost always first week | ~Universal in DEE end | Tonic seizures predominate |
| **Tonic seizures** | Bilateral tonic seizure (HP:0032794) / Tonic seizure (HP:0032792) | Neonatal | Very frequent | Focal-onset tonic stiffening ± clonic, autonomic features |
| **Multiple daily seizures / drug-resistant epilepsy** | Drug-resistant epilepsy (HP:0032794-adjacent; Intractable seizures HP:0032796) | Neonatal | Frequent at onset | Often many per day initially |
| Apnea / cyanosis / autonomic features | Apnea (HP:0002104) | Neonatal | Common ictal accompaniment | |
| **Moderate-to-profound intellectual disability** | Intellectual disability, profound (HP:0002187) / severe (HP:0010864) | Evident in infancy | Defining feature of DEE end | Persists after seizures remit |
| **Global developmental delay** | Global developmental delay (HP:0001263) | Infancy | Very frequent | |
| Axial hypotonia / appendicular hypertonia | Axial hypotonia (HP:0008936); Hypertonia (HP:0001276) | Infancy | Frequent | Mixed tone abnormality is characteristic |
| Absent/impaired speech | Absent speech (HP:0001344) | Childhood | Frequent (severe end) | |
| Cortical visual impairment | Cortical visual impairment (HP:0100704) | Infancy | Occasional–frequent | |
| Movement disorder (dystonia, dyskinesia) | Dystonia (HP:0001332) | Later | Occasional | |
| Non-epileptic myoclonus (GoF variants) | Myoclonus (HP:0001336) | Neonatal | GoF subtype | Distinguishes GoF phenotype |
| Microcephaly (acquired) | Microcephaly (HP:0000252) | Postnatal | Occasional | |

**Severity/progression pattern (this is the important bit):** the *seizures* are episodic and often **remit** by age 9 months–4 years, but the *encephalopathy* is **static-to-slowly-improving and lifelong.** That decoupling is exactly why the field renamed it from "epileptic encephalopathy" to "**developmental AND epileptic** encephalopathy" — there's a developmental component that isn't just a consequence of the seizures (the debate is nicely framed in "KCNQ2-DEE: developmental or epileptic encephalopathy?" *Epilepsia Open* 🔶, PMC7951099).

**Quality-of-life impact:** severe. Most individuals at the DEE end are nonverbal, non-ambulatory or limited, require full care, and have feeding, communication, and mobility support needs across the lifespan. A 2025 qualitative study of lived experience (*Epilepsy & Behavior* 🔶) documents high caregiver burden and the developmental-regression fear tied to medication weaning.

---

## 4. Genetic / Molecular Information

**Causal gene:** *KCNQ2* (potassium voltage-gated channel subfamily Q member 2), **20q13.33**, HGNC:6296, OMIM 602235. Encodes Kv7.2, a 6-transmembrane (S1–S6) voltage-gated K⁺ channel subunit: S1–S4 voltage sensor, S5–S6 pore, and a long intracellular C-terminus with four calmodulin-binding/subunit-assembly helices (A–D).

**Discovery lineage** (for provenance):
- Singh et al., 1998, *Nat Genet* 18:25–29 — *KCNQ2* mutated in BFNC 🔶 (commonly cited PMID:9425895)
- Biervert et al., 1998, *Science* 279:403–406 — potassium channel mutation in neonatal epilepsy 🔶 (PMID:9430337)
- Charlier et al., 1998, *Nat Genet* — *KCNQ3* as the second BFNC gene 🔶 (PMID:9425900)
- Weckhuysen et al., 2012, *Ann Neurol* 71:15–25 — carved out the **severe encephalopathy** phenotype (PMID:22275249 ✅)

**Variant classes (ACMG/AMP-classified in ClinVar):**
- **Missense** dominates the DEE end (dominant-negative). Recurrent hotspot residues cluster in **four high-risk zones**: the **S4 voltage sensor** (e.g., R198, R201, R213, R214), the **pore** (e.g., around residue 281), the **proximal C-terminus**, and the **C-terminal B-helix** (Millichap et al., 2016, *Neurol Genet* 🔶). Recurrent DEE alleles include **R201C/R201H, R213W/R213Q, A294V, and the pore variant G281 series**.
- **Truncating / frameshift / nonsense / whole-gene deletions** → generally the milder SLFNE (haploinsufficiency), though not exclusively.
- **In-frame indels** can behave dominant-negatively.
- **Deletion/duplication** (CNV) accounts for <10% of pathogenic findings; sequence analysis catches >90% 🔶.

**Allele frequency:** DEE-causing variants are **absent from population databases (gnomAD)** — they're de novo and highly penetrant, so they don't persist in the general population. This absence is itself an ACMG PM2 supporting criterion.

**Origin:** **germline, de novo** for the vast majority of DEE cases; germline/gonadal **mosaicism** in an unaffected parent has been reported and is the reason recurrence risk is quoted as low-but-not-zero (~1–2%+).

**Functional consequences:** loss-of-function (haploinsufficiency), **dominant-negative** loss-of-function (the DEE workhorse), and **gain-of-function** (distinct phenotype). A 2025 paper adds a genuinely novel wrinkle — some DEE variants act by introducing **abnormal current inactivation** rather than pure current reduction, a fourth biophysical mechanism ("Potassium current inactivation as a novel pathomechanism," PMC12169393 🔶).

**Modifier genes / epigenetics / chromosomal abnormalities:** no established Mendelian modifier genes, no disease-specific methylation signature (episignature) validated for KCNQ2-DEE as of this writing, and no recurrent large chromosomal rearrangement beyond the 20q13.33 CNVs noted above.

---

## 5. Environmental Information

Short section, and honestly a relief to write: **no environmental, lifestyle, or infectious contribution is established.** KCNQ2-DEE is a de novo monogenic channelopathy. Toxins, radiation, occupational exposure, diet, infection — none are causal or triggering in any documented way. The only "environmental" lever anyone can pull is *treatment choice and timing* (§12).

---

## 6. Mechanism / Pathophysiology

Here's the causal chain, from broken protein to seizing baby. This is the meat for the pathophysiology nodes.

**Upstream — the channel and the M-current.** Kv7.2 (KCNQ2) co-assembles with Kv7.3 (KCNQ3) into heterotetramers that carry the **M-current (I_M / I_Kv7)** — a slowly activating, non-inactivating, sub-threshold K⁺ current. Because it's active *near resting potential and doesn't inactivate*, the M-current is a persistent leak that:
1. sets and stabilizes the resting membrane potential,
2. produces **spike-frequency adaptation** (it clamps down repetitive firing), and
3. dampens overall neuronal excitability.

Crucially, these channels are concentrated at the **axon initial segment (AIS)** and **nodes of Ranvier**, anchored there via **ankyrin-G**-binding motifs — the exact spots where action potentials are born and propagated (Devaux et al., 2004, "KCNQ2 is a nodal K⁺ channel," *J Neurosci*, PMID:14762142 ✅; Pan et al., PNAS 🔶). So Kv7.2 isn't a diffuse background brake — it's a brake bolted right onto the ignition switch.

**GO / CL / UBERON anchors:**
- Biological processes: **regulation of membrane potential** (GO:0042391), **potassium ion transmembrane transport** (GO:0071805), **regulation of neuronal action potential** (GO:0098908), **negative regulation of neuron differentiation/excitability**, **spike-frequency adaptation**.
- Molecular function: **voltage-gated potassium channel activity** (GO:0005249).
- Cellular components: **axon initial segment** (GO:0043194), **node of Ranvier** (GO:0033268), **plasma membrane** (GO:0005886).
- Cell types (CL): **glutamatergic neuron** (CL:0000679), **pyramidal neuron** (CL:0000598), **CNS interneuron / GABAergic interneuron** (CL:0000617) — GoF pathology is thought to preferentially silence excitatory neurons or disrupt interneuron circuits.
- Anatomy (UBERON): **cerebral cortex** (UBERON:0000956), **hippocampus** (UBERON:0002421), **brain** (UBERON:0000955); the basal ganglia show transient neonatal MRI changes.

**Midstream — what the variant does.** A dominant-negative missense subunit incorporates into the tetramer and poisons it, so M-current drops **>50%**. Less brake → the AIS/nodes fire too readily → **neuronal hyperexcitability and hypersynchrony** → neonatal seizures.

**The gain-of-function paradox.** GoF variants do the *opposite* biophysically — too much K⁺ current, neurons over-silenced — yet still cause encephalopathy, likely by disrupting the excitation/inhibition balance at the circuit level (over-silencing excitatory cells, or knocking out interneuron function). This is why the two mechanisms need **opposite drugs** (Kv7 opener helps LoF, harms GoF).

**Downstream — the developmental arm.** Kv7 channels aren't just firing regulators; they shape neuronal maturation. A 2025 iPSC study shows LoF variants cause **early hyperexcitability followed by maladaptive network remodeling** during development (bioRxiv 2025.07.22 🔶), which is the mechanistic candidate for why the *developmental* deficit outlasts the seizures. That's the crux of the "developmental AND epileptic" reframing.

**Conformance note for the KB:** the core of this maps cleanly onto the **`cardiac_ion_channel_repolarization`** module's sibling logic and, more directly, the **`epilepsy_excitation_inhibition_imbalance`** module — KCNQ2-DEE is essentially a textbook conformer of `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` (ion-channel dysfunction → E/I imbalance → hyperexcitability/hypersynchrony → seizures → epileptogenesis). Worth flagging when this entry gets curated.

**Molecular profiling:** most mechanistic data are electrophysiological (patch-clamp of heterologously expressed channels in *Xenopus* oocytes / CHO / HEK cells — **IN_VITRO** evidence) and, increasingly, patient-derived **iPSC neurons** (also IN_VITRO). No robust transcriptomic/proteomic/metabolomic disease signature from patient tissue exists — you can't biopsy a neonatal brain.

---

## 7. Anatomical Structures Affected

- **Organ level:** brain (UBERON:0000955) — primarily. This is a CNS-restricted disorder; no systemic organ involvement. Body system: **nervous system** (central).
- **Regions:** cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421); **basal ganglia** (UBERON:0002420) show transient neonatal T1/T2 or diffusion changes on MRI; later, nonspecific white-matter changes and volume loss.
- **Tissue/cell level:** nervous tissue; **neurons** — pyramidal/glutamatergic (CL:0000598/CL:0000679) and GABAergic interneurons (CL:0000617). The functional lesion sits at the **axon initial segment and nodes of Ranvier**.
- **Subcellular:** **plasma membrane** at the AIS (GO:0043194) and node of Ranvier (GO:0033268).
- **Lateralization:** **bilateral / diffuse** encephalopathy; individual seizures are often focal-onset (can shift sides — multifocal) but the disease burden is bilateral.

---

## 8. Temporal Development

- **Onset:** **neonatal**, median **day 1 of life**, essentially always within the first week (Weckhuysen 2012, PMID:22275249 ✅). Onset pattern is **acute** (dramatic multiple-daily seizures from the start).
- **Course:** seizures are **frequent and drug-resistant at onset**, then typically **improve and remit** between ~9 months and 3–4 years. The **encephalopathy is static-to-lifelong** — developmental impairment persists after seizure remission.
- **Stages:** (1) neonatal explosive-seizure phase with burst-suppression/multifocal EEG; (2) seizure-attenuation phase in infancy/early childhood; (3) chronic static encephalopathy with variable later-life epilepsy relapse.
- **Progression rate:** the neurodevelopmental deficit is **non-progressive** (static encephalopathy) in most — not a neurodegeneration. Severity is set early.
- **Critical window:** the neonatal period is both the window of maximal vulnerability *and* the proposed window of therapeutic opportunity — the "treat early, treat right" hypothesis (Pisano et al., 2015, *Epilepsia*, "Early and effective treatment of KCNQ2 encephalopathy" 🔶).
- **Duration:** chronic, lifelong disability; seizures self-limit but the disorder does not.

---

## 9. Inheritance and Population

**Inheritance:** **autosomal dominant.**
- **KCNQ2-DEE (severe):** overwhelmingly **de novo**; penetrance is **complete**. Reproduction is rare, so vertical transmission is uncommon.
- **SLFNE (mild):** usually **inherited** from an affected parent; penetrance **incomplete (~77–85%)** 🔶.
- **Germline/gonadal mosaicism** occurs and drives the low-but-nonzero sibling recurrence risk.
- **Anticipation:** not a repeat-expansion disorder — no genetic anticipation.
- **Founder effects / consanguinity:** not relevant (dominant, de novo).
- **Carrier frequency:** N/A for the de novo dominant DEE end.

**Epidemiology:**
- *KCNQ2* is one of the **most common genetic causes of neonatal-onset epileptic encephalopathy** — it was found in ~**10% of 80** unexplained neonatal/early-infantile seizure-plus-delay cases in the founding cohort (Weckhuysen 2012, PMID:22275249 ✅).
- **Incidence** of KCNQ2-related neonatal epilepsy estimated at roughly **~5.9 per 100,000 live births** (<6 months) in a Scottish population cohort (Symonds et al., 2019, *Brain* 🔶 — verify PMID before curation).
- **Documented individuals:** on the order of a few hundred reported NEO-DEE cases plus ~200 SLFNE families 🔶; it's a rare disease but not vanishingly so among neonatal epilepsies.
- **Sex ratio:** roughly **1:1** — no sex bias (X-autosomal; gene is autosomal).
- **Geography/ethnicity:** no population clustering; reported worldwide across ancestries.

**Prevalence class for the KB:** qualitatively **RARE**; incidence ~5.9/100,000 live births → `rate_per_100000` ≈ 5.9 (ANNUAL_INCIDENCE / BIRTH_PREVALENCE framing), Orphanet band roughly `BAND_1_9_PER_100000`.

---

## 10. Diagnostics

**Genetic testing is the definitive diagnostic.**
- **Approach:** clinical suspicion (neonatal tonic seizures + burst-suppression/multifocal EEG + encephalopathy) → **next-generation sequencing.** Options: **multigene neonatal-epilepsy/DEE panel** (fastest yield in the NICU), **exome/genome sequencing** (rapid trio WES/WGS increasingly first-line for neonatal seizures), or **single-gene *KCNQ2* sequencing.** Sequence analysis detects >90%; add **deletion/duplication (CMA/MLPA)** for the <10% CNV cases 🔶.
- **Interpretation:** classify per **ACMG/AMP**; DEE variants are typically de novo (PS2), absent from gnomAD (PM2), at known hotspots/recurrent (PS1/PM1/PM5), with functional data (PS3) from patch-clamp — a strong combination that often reaches **pathogenic**.

**Electrophysiology (central to the phenotype):**
- **EEG:** at DEE onset, **burst-suppression** pattern or **multifocal epileptiform activity**; SLFNE shows normal-to-focal discharges that normalize. Serial EEG is used for surveillance.
- Ictal semiology: focal-onset **tonic** seizures with autonomic/apneic features.

**Neuroimaging:**
- **Brain MRI:** often normal early, or transient **basal ganglia and thalamic hyperintensity/restricted diffusion** in the neonatal period; later nonspecific white-matter change or volume loss. MRI helps exclude structural/hypoxic-ischemic mimics rather than confirm KCNQ2-DEE.

**Laboratory / biomarkers:** **no specific blood, CSF, or metabolic biomarker.** Routine metabolic workup (glucose, electrolytes, ammonia, lactate, CSF, acylcarnitines, etc.) is done to exclude treatable metabolic/infectious causes of neonatal seizures — it's a rule-out, not a rule-in. No LOINC-coded diagnostic analyte for the disease itself.

**Differential diagnosis:** other genetic neonatal DEEs — **SCN2A, SCN8A, STXBP1, KCNQ3, ARX, CDKL5, KCNT1**, pyridoxine-dependent epilepsy (ALDH7A1) and other treatable metabolic epilepsies, and hypoxic-ischemic encephalopathy. *KCNQ3* neonatal epilepsy is clinically near-indistinguishable at the mild end.

**Screening:** *KCNQ2* is **not** on standard biochemical newborn screening (it's not a metabolic disease). Cascade/family testing applies mainly to the inherited SLFNE end. Prenatal/PGT is technically possible when a familial variant is known but is rarely relevant for the de novo DEE cases.

---

## 11. Outcome / Prognosis

- **Survival:** most individuals survive into adulthood; there is an elevated risk of **SUDEP** (sudden unexpected death in epilepsy) and mortality from severe-disability complications, but KCNQ2-DEE is not typically early-lethal. Life expectancy is reduced by comorbidity burden, not by a defined disease-specific lethal course.
- **Seizure prognosis:** relatively **good** — seizures usually remit in infancy/early childhood (9 mo–4 yr), though a subset relapse later.
- **Developmental prognosis:** **poor and the dominant driver of outcome** — moderate-to-profound intellectual disability, frequently nonverbal, motor impairment, feeding/communication needs. The encephalopathy persists regardless of seizure control.
- **Prognostic factors:** the strongest predictor is **variant functional severity** — degree of in-vitro M-current reduction correlates with long-term neurodevelopmental outcome (PMC7415140, "Heteromeric Kv7.2 current changes… correlated with long-term neurodevelopmental outcomes" 🔶). Dominant-negative > simple LoF in severity. **Earlier effective therapy** (sodium-channel blockers) may improve outcome (Pisano 2015 🔶).
- **QoL measures:** no KCNQ2-specific validated instrument; generic pediatric DEE/QI-Disability and caregiver-burden tools are used.

---

## 12. Treatment

This is where KCNQ2-DEE gets genuinely interesting as a **precision-medicine** story, because the right drug depends on the biophysics of the variant.

**First-line: sodium channel blockers (the standout for loss-of-function).**
- **Carbamazepine, oxcarbazepine, phenytoin, lacosamide.** Multiple series show these outperform broad-spectrum ASMs in KCNQ2-DEE. Reported seizure-freedom rates: **carbamazepine ~40% within 2 weeks**, phenytoin ~33–42%, **oxcarbazepine ~53%** in one comparison 🔶.
- **Why it works:** Kv7 potassium channels and Naᵥ sodium channels co-localize at the AIS; blocking the sodium channels compensates for the missing potassium brake (down-regulating the excitatory current that the failed K⁺ channel can no longer restrain) 🔶.
- MAXO/CHEBI anchors: **Pharmacotherapy (NCIT:C15986)**; agents — carbamazepine (CHEBI:3387), oxcarbazepine (CHEBI:7824), phenytoin (CHEBI:8107), lacosamide (CHEBI:87517). `therapeutic_modality: SMALL_MOLECULE`.

**Targeted / mechanism-based: Kv7 channel openers (retigabine/ezogabine).**
- **Ezogabine (retigabine, XEN496)** directly opens Kv7.2/7.3 channels — it's the mechanistically "perfect" drug for **loss-of-function** variants. A retrospective series (**Knight et al., 2023, *Epilepsia***, DOI:10.1111/epi.17627 ✅) of 8 KCNQ2-DEE patients found **≥50% seizure reduction in the 5 with daily seizures, developmental improvement in all 8**, and — tellingly — **weaning caused seizure increase, irritability, poor sleep, and developmental regression.**
- **BUT:** retigabine was **withdrawn from market in 2017** for retinal pigmentation and blue skin/mucosal discoloration with chronic use. A reformulated pediatric version (**XEN496/ezogabine**) ran a Phase 3 RCT (**NCT04639310, EPIK**), which was **terminated in May 2023 for a sponsor business decision, not safety** ✅. So the ideal targeted drug currently has no approved pediatric product — a real unmet-need gap.
- **Genotype caveat:** for **gain-of-function** variants a Kv7 *opener* is the wrong direction and **can worsen** the phenotype; those patients theoretically need Kv7 *blockers/negative modulators* 🔶. This LoF-vs-GoF drug divergence is the reason functional variant classification matters clinically, not just academically.
- MAXO anchor for ezogabine: Pharmacotherapy (NCIT:C15986), agent ezogabine/retigabine (CHEBI:78754), `therapeutic_modality: SMALL_MOLECULE`, with a `target_mechanisms` link back to the Kv7/M-current node.

**Supportive / adjunctive:** phenobarbital (common neonatal first agent, though less specific), levetiracetam, topiramate, benzodiazepines; **ketogenic diet** (MAXO:0000088, dietary intervention) in refractory cases; standard DEE supportive care — PT/OT/speech, feeding support, developmental services (MAXO:0000950 supportive care; NCIT:C15315 rehabilitation).

**Experimental horizon:** **antisense oligonucleotide** and other genetic approaches are in preclinical development (allele-selective knockdown for dominant-negative alleles is a conceptually clean strategy; iPSC/mouse work is underway), and small-molecule Kv7 modulators beyond ezogabine are being pursued. Nothing approved yet.

**Pharmacogenomics:** the "pharmacogenomics" here IS the disease genotype — LoF vs GoF classification of the *KCNQ2* variant is the single most important treatment-guiding factor. This is genotype-guided therapy in its purest form.

---

## 13. Prevention

- **Primary prevention:** not possible for de novo variants — you can't prevent a spontaneous germline mutation. No vaccine, no modifiable risk factor.
- **Secondary prevention / early detection:** the meaningful lever is **rapid genetic diagnosis in the NICU** (rapid trio exome/genome for neonatal seizures) so that **variant-appropriate therapy (sodium channel blockers / Kv7 openers) starts early** — the "treat early and right" strategy that may improve developmental outcome (Pisano 2015 🔶). That's secondary prevention of *severity*, not of the disease.
- **Tertiary prevention:** seizure control, SUDEP-risk management, developmental/rehabilitative support to prevent complications.
- **Genetic counseling:** essential. For de novo DEE, recurrence risk is low (~1–2%, driven by possible parental gonadal mosaicism); for inherited SLFNE, standard 50% AD transmission with incomplete penetrance. **PGT/prenatal testing** available when a familial variant is known (MAXO:0000079 genetic counseling; NSGC/ACMG frameworks).
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *KCNQ2* is deeply conserved. Mouse *Kcnq2* (**NCBITaxon:10090**, Mus musculus), rat *Kcnq2* (**NCBITaxon:10116**), zebrafish *kcnq2* (**NCBITaxon:7955**). Human ortholog KCNQ2 (NCBI Gene 3785).
- **Natural disease in animals:** **no well-documented spontaneous naturally-occurring *KCNQ2* neonatal epilepsy in companion animals or wildlife** is catalogued in OMIA the way, say, some canine epilepsies are. The disease knowledge is essentially all human + engineered models.
- **Comparative biology:** the M-current and Kv7.2/7.3 AIS localization are conserved across mammals, which is *why* rodent models recapitulate the human electrophysiology well — the brake pedal is built the same way across species.
- **Zoonosis / transmission:** N/A — genetic, non-transmissible.

---

## 15. Model Organisms

Rodent models are strong here and are the backbone of mechanistic and preclinical-therapeutic work. Evidence source = **MODEL_ORGANISM.**

- **Conditional dominant-negative *Kcnq2* transgenic mice (Peters et al., 2005):** suppress M-current → **spontaneous seizures, hippocampal memory impairment, behavioral hyperactivity** — an early demonstration that M-current loss alone produces the seizure+cognitive phenotype 🔶.
- **Knock-in point-mutant mice reproducing human alleles:**
 - ***Kcnq2* Thr274Met/+ knock-in** — viable, **spontaneous generalized seizures from ~P20–P30 with cognitive impairment** (Milh/Marini group, 2020, *Epilepsia*, **PMID:32239694** ✅). A faithful DEE-like model.
 - ***Kcnq2* A306T and *Kcnq3* G311V knock-ins** — survive into adulthood with **spontaneous lifelong seizures** 🔶.
 - **Calmodulin-binding-domain variant mice** — spontaneous seizure + memory loss (PMC8713762 🔶).
 - **cKcnq2 M547V conditional mice** — early mortality, spontaneous seizures, enhanced seizure susceptibility, memory deficits, repetitive behaviors 🔶.
 - **Tg *Kcnq2* G279S mice** — partial seizures ± secondary generalization 🔶.
- **Conventional *Kcnq2* knockout:** homozygous null is **neonatal-lethal** (pulmonary/dysfunctional), consistent with the channel's essential role — hence the field's reliance on **heterozygous and conditional** models. Good review: **Brun et al., 2022, "Mouse models of *Kcnq2* dysfunction," *Epilepsia*** 🔶.
- **iPSC-derived human neuron models (IN_VITRO):** patient-derived and CRISPR-engineered iPSC neurons now recapitulate variant-specific hyperexcitability and drug responses, including the 2025 machine-learning-phenotyping and maladaptive-remodeling studies (bioRxiv 2025 🔶) — increasingly used for **variant functional classification and drug screening.**
- **Heterologous expression (IN_VITRO):** *Xenopus* oocytes and CHO/HEK cells for patch-clamp are the standard for scoring a new variant as LoF/DN/GoF — the assay that feeds the ACMG PS3 criterion and the treatment decision.

**Model strengths:** rodent knock-ins reproduce spontaneous seizures, cognitive deficits, and the electrophysiology, and respond to Kv7 openers — good for preclinical drug testing. **Limitations:** rodents don't fully model the human *developmental/cognitive* trajectory or the neonatal timing precisely; homozygous KO lethality limits complete-loss modeling; and human-specific circuit biology is only approximated (a candidate `HUMAN_MODEL_MISMATCH` discussion note for the KB where mouse timing/severity diverges from human).

**Resources:** MGI (mouse), RGD (rat), ZFIN (zebrafish), IMPC/KOMP for *Kcnq2* alleles; the **RIKEE database** (rikee.org) as the human variant-function registry.

---

## Curation notes for the dismech entry

A few things worth carrying into the YAML when this gets built:
- **Module conformance:** strong candidate conformer for **`epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`** (ion-channel dysfunction → E/I imbalance → hyperexcitability/hypersynchrony → seizures). The Kv7-opener treatment pattern fits the `target_mechanisms` drug convention.
- **The LoF/DN/GoF split** should be modeled explicitly (probably as subtypes or mechanistic_hypotheses with `hypothesis_group_id`), since it drives both phenotype *and* opposite-direction treatment.
- **Evidence-source discipline:** electrophysiology and iPSC data = IN_VITRO; mouse knock-ins = MODEL_ORGANISM; keep the neonatal-seizure/EEG/outcome claims on HUMAN_CLINICAL sources (Weckhuysen 2012, Knight 2023).
- **Verify before committing:** PMIDs marked �remaining (Singh 9425895, Biervert 9430337, Charlier 9425900, Miceli 2013/2015, Millichap 2016 27353566, Mulkey 2017, Symonds 2019) came from GeneReviews/reviews — run `just fetch-reference` and confirm snippets are exact substrings per the anti-hallucination SOP. The ones I confirmed live this session are Weckhuysen (22275249), Devaux nodal K⁺ (14762142), the Thr274Met mouse (32239694), and the Knight ezogabine paper (DOI 10.1111/epi.17627).

**Sources:**
- [GeneReviews: KCNQ2-Related Disorders (NBK32534)](https://www.ncbi.nlm.nih.gov/books/NBK32534/)
- [OMIM #613720 — DEE7](https://www.omim.org/entry/613720) · [OMIM *602235 — KCNQ2](https://omim.org/entry/602235) · [OMIM #121200 — BFNS1](https://omim.org/entry/121200)
- [Orphanet: KCNQ2-related DEE (439218)](https://www.orpha.net/en/disease/detail/439218) · [NORD: KCNQ2-DEE](https://rarediseases.org/rare-diseases/kcnq2-encephalopathy/)
- [Weckhuysen et al. 2012, Ann Neurol (PMID:22275249)](https://pubmed.ncbi.nlm.nih.gov/22275249/)
- [Devaux et al. 2004, KCNQ2 is a nodal K⁺ channel (PMID:14762142)](https://pubmed.ncbi.nlm.nih.gov/14762142/)
- [Knight et al. 2023, Ezogabine in KCNQ2-DEE, Epilepsia](https://onlinelibrary.wiley.com/doi/10.1111/epi.17627) · [NCT04639310 (XEN496/EPIK)](https://clinicaltrials.gov/study/NCT04639310)
- [Knock-in Kcnq2 Thr274Met mouse (PMID:32239694)](https://pubmed.ncbi.nlm.nih.gov/32239694/) · [Brun et al. 2022, Mouse models of Kcnq2 dysfunction](https://onlinelibrary.wiley.com/doi/10.1111/epi.17405)
- [KCNQ2-DEE: developmental or epileptic encephalopathy? (PMC7951099)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951099/) · [Heteromeric Kv7.2 current & outcomes (PMC7415140)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7415140/)
- [Potassium current inactivation as novel pathomechanism (PMC12169393)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12169393/) · [R144 gain-of-function, eBioMedicine 2022](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(22)00311-5/fulltext)
- [KCNQ2 Cure Alliance — What is KCNQ2 Epilepsy](https://www.kcnq2cure.org/kcnq2-epilepsy/)

That's the whole animal, nose to tail. The one-line version if you're skimming: it's a de novo dominant potassium-channel brake failure that seizes newborns in week one, the seizures fade but the brain stays hurt, and — unusually — knowing whether the channel is *too weak* or *too strong* literally flips which drug you reach for. Want me to go ahead and scaffold the actual `kb/disorders/KCNQ2_Developmental_and_Epileptic_Encephalopathy.yaml` entry from this, or open a curation issue for it?