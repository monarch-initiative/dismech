---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-10T12:59:16.328870'
end_time: '2026-07-10T13:04:15.595269'
duration_seconds: 299.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Organophosphate Poisoning
  mondo_id: ''
  category: Environmental
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
  num_turns: 13
  total_cost_usd: 2.373729
  session_id: ce5f8433-0ca0-4f69-9e01-54a7232dce5e
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Organophosphate Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Organophosphate Poisoning** covering all of the
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

I have enough well-sourced material to write the report. Compiling it now.

---

# Comprehensive Research Report: Organophosphate Poisoning

**Prepared:** 2026-07-10 · **Category:** Environmental (toxic exposure) · **Knowledge-base target entry**

A note on scope: Organophosphate (OP) poisoning is an acquired **toxic/environmental** syndrome, not a heritable Mendelian disease. Accordingly, several template sections built for genetic disorders (causal genes, inheritance, chromosomal abnormalities, gene panels) are **not applicable in the disease-causing sense** — the only genetics that matter here are *host-susceptibility modifiers* (chiefly *PON1*). I flag these explicitly where they arise rather than forcing genetic content that does not exist.

---

## 1. Disease Information

**Overview.** Organophosphate poisoning is the clinical syndrome resulting from exposure to organophosphorus (OP) compounds — insecticides (parathion, malathion, chlorpyrifos, dimethoate, fenthion, diazinon, monocrotophos) and chemical warfare nerve agents (sarin, soman, tabun, VX). The unifying mechanism is inhibition of **acetylcholinesterase (AChE)**, causing accumulation of acetylcholine at cholinergic synapses and an acute cholinergic crisis affecting muscarinic, nicotinic, and central nervous system receptors. As the flagship 2023 mechanistic review states, "The OP binds to and phosphorylates a nucleophilic serine at the catalytic site of the enzyme" (Naughton & Terry, *Toxics* 2023; **PMID:37888716**), and acetylcholinesterase inhibition "results in accumulation of acetylcholine and overstimulation of acetylcholine receptors" (Eddleston et al., *Lancet* 2008; **PMID:17706760**).

**Key identifiers.**
- **ICD-10:** T60.0 (Toxic effect of organophosphate and carbamate insecticides); X48 / T60.0 for accidental/intentional pesticide exposure.
- **ICD-11:** NE61 (Harmful effects of drugs, medicaments and biological substances) / exposure codes; poisoning by insecticides.
- **MeSH:** "Organophosphate Poisoning" (D062025); related: "Organophosphorus Compounds," "Cholinesterase Inhibitors."
- **MONDO:** No specific well-established MONDO term for the acute toxic syndrome (this is a toxic exposure, not a disease entity in the OMIM/Mendelian sense). Candidate mapping is to a poisoning/intoxication class; **do not assert a MONDO ID without verification via OAK** (`runoak -i sqlite:obo:mondo search "organophosphate poisoning"`).
- **OMIM / Orphanet:** Not applicable (acquired toxic condition; no Orphanet rare-disease code).

**Common synonyms / alternative names.** Organophosphorus poisoning; OP poisoning; organophosphate insecticide poisoning; anticholinesterase poisoning; cholinergic toxidrome; nerve agent poisoning (for warfare agents). "Organophosphate-induced cholinergic crisis" refers to the acute phase.

**Data derivation.** Information is **aggregated disease-level** (toxicology reviews, clinical cohorts, RCTs, poison-center registries) rather than individual EHR-derived — though large single-center Asian cohorts (Sri Lanka, India, Pakistan, Bangladesh) supply much of the clinical evidence.

---

## 2. Etiology

**Primary cause.** Exposure — dermal, inhalational, or (most lethally) oral ingestion — to an organophosphorus compound. The dominant global context is **intentional self-poisoning (suicide)** by ingestion of agricultural insecticides in low- and middle-income countries; secondary causes are occupational/agricultural exposure and accidental (often pediatric) exposure. Chemical warfare/terrorism (e.g., Tokyo sarin 1995; Syria) is a distinct high-acuity setting.

**Risk factors (environmental/behavioral):**
- Residence in rural agricultural regions of South Asia, Southeast Asia, sub-Saharan Africa, Central/South America.
- Occupational: farm workers, pesticide applicators/handlers, sheep-dip workers (chronic low-dose exposure).
- Ready domestic availability of highly hazardous WHO Class I OP pesticides.
- Psychiatric distress / acute interpersonal crisis (impulsive self-harm — the reason means-restriction works so well).
- Male sex and working age predominate in fatal self-poisoning cohorts.

**Genetic susceptibility modifiers (not causal genes).** **PON1 (paraoxonase-1)** is the principal host determinant. PON1 is "an A-esterase capable of hydrolyzing the active metabolites (oxons) of a number of organophosphorus insecticides such as parathion, diazinon and chlorpyrifos" (Costa et al.; **PMC3516631**). The **Q192R (rs662)** and **L55M** coding polymorphisms and the **−108 C/T** promoter variant (governing expression level) modulate detoxification efficiency in a substrate-specific manner — "The PON1R192 alloform hydrolyzes chlorpyrifos oxon and paraoxon more rapidly than PON1Q192." A meta-analysis found "PON1 192Q and 55LM polymorphisms may increase the risk of organophosphate toxicity, especially among Caucasian populations" (**PMID:23590198**). See §4 and §9.

**Protective factors.**
- **Environmental/public-health:** national bans of highly hazardous pesticides (Sri Lanka's staged bans are the landmark example — see §9/§13), safe storage, dilution/formulation changes. These are the single most effective interventions for population mortality.
- **Genetic:** high-activity PON1 alloforms/high plasma PON1 status confer relative protection against specific oxons; there is no universally protective allele (protection is compound-dependent).

**Gene–environment interaction.** The canonical GxE here is **PON1 genotype × specific OP compound**: "The extent to which PON1 protects against a given OP is determined by its catalytic efficiency" toward that compound's oxon. Groups with high-dose exposure (sheep-dip workers, first Gulf War veterans) reported poorer health if carrying the 192R allele (**PMC3516631**). CTD (Comparative Toxicogenomics Database) catalogs OP compound → gene interactions for curation cross-reference.

---

## 3. Phenotypes

Clinical features derive from cholinergic excess at three receptor populations. Onset is **acute** (minutes to hours after ingestion; sometimes delayed with lipophilic agents like fenthion).

**Muscarinic effects (mnemonics SLUDGE / DUMBELS):** salivation, lacrimation, urination, defecation/diarrhea, gastrointestinal cramping, emesis; plus miosis, bronchorrhea, bronchospasm, bradycardia, sweating. Bronchorrhea + bronchospasm ("the killer B's") drive early respiratory failure.

| Phenotype | Type | HPO suggestion | Frequency (qualitative) |
|---|---|---|---|
| Miosis (pinpoint pupils) | Sign | HP:0000616 (Anisocoria/miosis — nearest: HP:0025616 Miosis) | Very frequent |
| Hypersalivation | Sign | HP:0002307 (Drooling) / HP:0000048 | Frequent |
| Excessive lacrimation | Sign | HP:0009926 (Increased lacrimation) | Frequent |
| Diarrhea | Symptom | HP:0002014 (Diarrhea) | Frequent |
| Vomiting | Symptom | HP:0002013 (Vomiting) | Frequent |
| Bronchorrhea / excessive airway secretions | Sign | HP:0002486 (nearest: Abnormal bronchus morphology); use HP:0033109/secretion terms | Frequent, life-threatening |
| Bronchospasm / wheezing | Sign | HP:0030828 (Wheezing) | Frequent |
| Bradycardia | Sign | HP:0001662 (Bradycardia) | Common (tachycardia also possible) |
| Sweating | Sign | HP:0000975 (Hyperhidrosis) | Frequent |
| Muscle fasciculations | Sign (nicotinic) | HP:0002380 (Fasciculations) | Frequent |
| Muscle weakness / flaccid paralysis | Sign (nicotinic) | HP:0001324 (Muscle weakness) | Common, severe cases |
| Respiratory failure | Sign | HP:0002878 (Respiratory failure) | Leading cause of death |
| Seizures / status epilepticus | Sign (CNS) | HP:0001250 (Seizure); HP:0002133 (Status epilepticus) | Severe cases, esp. nerve agents |
| Altered consciousness / coma | Sign (CNS) | HP:0001259 (Coma) / HP:0002493 | Severe cases |
| Confusion, anxiety, agitation | Behavioral (CNS) | HP:0001289 (Confusion) | Common |

**Nicotinic effects:** fasciculations, muscle weakness, cramps, tachycardia, hypertension, mydriasis (variable) — reflecting neuromuscular junction and sympathetic ganglion stimulation. "Overstimulation of nicotinic acetylcholine receptors in the CNS results in anxiety, headache, convulsions, ataxia, depression of respiration and circulation, tremor, general weakness, and potentially coma" (mechanism reviews).

**CNS effects:** anxiety, restlessness, confusion, tremor, seizures, and status epilepticus. Per the 2023 review, "brain damage from acute OP exposure is a direct result of status epilepticus," and "muscarinic but not nicotinic receptor antagonists prevent seizure induction if administered before OP exposure" (**PMID:37888716**).

**Later/secondary phenotypes (see §8 for timing):**
- **Intermediate syndrome (IMS):** proximal muscle and neck-flexor weakness, cranial nerve palsies, and **respiratory failure 24–96 h** after cholinergic crisis, "not responsive to atropine or oxime therapy" (**PMC5548687**). HPO: HP:0002878, HP:0003324 (Generalized muscle weakness).
- **OP-induced delayed polyneuropathy (OPIDN):** distal sensorimotor peripheral neuropathy 1–3 weeks post-exposure. HPO: HP:0009830 (Peripheral neuropathy), HP:0007015 (Sensorimotor neuropathy).
- **Chronic OP-induced neuropsychiatric disorder (COPIND):** cognitive/affective sequelae after chronic or severe acute exposure.

**Severity & progression.** Severity graded clinically by the **Peradeniya Organophosphorus Poisoning (POP) scale** (miosis, fasciculations, respiration, bradycardia, consciousness, seizures); "Higher POP scale scores are associated with increased mortality, need for ventilatory support, and atropine dosages" (**PMC10336367**). Course is acute and often episodic across the three phases; QoL impact is dominated by ICU-level respiratory failure, prolonged ventilation, and (in survivors) persistent neuropsychiatric and peripheral-nerve deficits.

---

## 4. Genetic / Molecular Information

**Causal genes: NOT APPLICABLE** — OP poisoning is toxin-induced; there is no disease-causing germline mutation.

**Host-susceptibility gene (modifier): PON1**
- **HGNC:** *PON1* (paraoxonase 1), HGNC:9204; chromosome 7q21.3.
- **Function:** calcium-dependent A-esterase that hydrolyzes OP oxons (the toxic activated metabolites); "PON1 activity is highest in liver and in plasma" (**PMC3516631**).
- **Key variants (germline polymorphisms, not pathogenic mutations):**
  - **Q192R (rs662):** substrate-specific catalytic difference; R192 hydrolyzes chlorpyrifos-oxon/paraoxon faster, Q192 hydrolyzes some others (e.g., soman/sarin analogs) better. Both hydrolyze diazoxon equally.
  - **L55M (rs854560):** affects protein stability/level.
  - **−108 C/T (promoter):** "the major contributor of differences in the levels of PON1 expression."
  - Allele frequencies vary widely by ancestry (e.g., 192R more common in some Asian/African populations); consult **gnomAD** for population-specific frequencies.
- **Functional consequence:** modifies *detoxification capacity* — effectively a pharmacokinetic protective/risk gradient, not loss/gain-of-function disease biology.

**Other modifier candidates:** **BCHE** (butyrylcholinesterase) genotype affects plasma pseudocholinesterase scavenging capacity; carboxylesterase (CES1/CES2) contributes to OP scavenging in some species (large in rodents, minor in humans — relevant to model translation, §15). These are secondary.

**Epigenetics / chromosomal abnormalities:** Not applicable to the acute syndrome. Some experimental and epidemiological work links chronic/developmental OP exposure to DNA-methylation changes (neurodevelopmental cohorts), but this is not part of the acute poisoning entity.

---

## 5. Environmental Information

**Environmental / chemical agents (the etiology itself).** Representative OP insecticides — with CHEBI suggestions for curation:
- Parathion (CHEBI:27928), methyl-parathion, chlorpyrifos (CHEBI:34631), malathion (CHEBI:6651), diazinon (CHEBI:34682), dimethoate (CHEBI:34706), monocrotophos, fenthion, dichlorvos (CHEBI:4498).
- Nerve agents: sarin (CHEBI:75701), soman, tabun, VX.
- Detoxification/therapeutic chemicals: atropine (CHEBI:16684), pralidoxime (CHEBI:8354), obidoxime, diazepam (CHEBI:49575).

WHO hazard classification (Class Ia/Ib "extremely/highly hazardous") predicts case fatality — the basis for regulatory bans.

**Lifestyle factors.** Alcohol co-ingestion at the time of self-poisoning worsens outcome; occupational non-use of personal protective equipment increases dermal/inhalational absorption in agricultural workers.

**Infectious agents:** Not applicable (aspiration pneumonia is a *complication*, not a cause).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **OP absorption and bioactivation.** Parent thion OPs (P=S) are metabolized by hepatic cytochrome P450 to the active **oxon (P=O)** form; PON1 competes by hydrolyzing oxons (detoxification branch). Pathways: KEGG "Metabolism of xenobiotics by cytochrome P450."
2. **AChE inhibition (primary lesion).** The oxon phosphorylates the catalytic serine of **acetylcholinesterase (AChE, ACHES/ACHE; EC 3.1.1.7)**: "The OP binds to and phosphorylates a nucleophilic serine at the catalytic site of the enzyme" (**PMID:37888716**). GO terms: **GO:0003990** (acetylcholinesterase activity), **GO:0004104** (cholinesterase activity), **GO:0042135** (neurotransmitter catabolic process).
3. **"Aging."** The phosphorylated enzyme can undergo dealkylation ("aging"), after which it becomes **irreversibly** inhibited and no longer reactivatable by oximes — the pharmacological rationale for giving oximes *early*. Aging half-time is compound-specific (minutes for soman; hours–days for many insecticides).
4. **Acetylcholine accumulation → receptor overstimulation.** Acetylcholine (CHEBI:15355) accumulates at synapses; overstimulation of muscarinic (CHRM1-5) and nicotinic (CHRNA/CHRNB) acetylcholine receptors. GO: **GO:0007271** (synaptic transmission, cholinergic), **GO:0007213** (G-protein-coupled acetylcholine receptor signaling). Clinical cholinergic toxidrome results (§3).
5. **CNS excitotoxicity.** Cholinergic overactivity triggers seizures/status epilepticus; downstream, "the amygdala displays a rapid increase in extracellular glutamate after exposure to soman" — a **glutamatergic secondary phase** that sustains seizures and neuronal injury even after cholinergic control (**PMID:37888716**).
6. **Calcium overload, mitochondrial dysfunction, oxidative stress.** "Excess Ca++ disrupts the function of mitochondria, leading to ATP depletion and oxidative stress"; "oxidative stress and inflammation play an important role in neuronal damage caused by chronic OP exposure." GO: GO:0006954 (inflammatory response), GO:0006979 (response to oxidative stress), GO:0006915 (apoptotic process). This drives neuronal necrosis/apoptosis and long-term brain damage.
7. **Respiratory failure (the proximate cause of death).** Convergence of bronchorrhea/bronchospasm (muscarinic), diaphragmatic/intercostal weakness (nicotinic neuromuscular block), and central respiratory depression (CNS).

**Distinct secondary mechanisms:**
- **Intermediate syndrome (IMS):** post-synaptic neuromuscular dysfunction and receptor downregulation from prolonged ACh excess; correlates with sustained AChE inhibition and specific agents (dimethoate, fenthion, monocrotophos).
- **OPIDN:** mechanistically separate — covalent inhibition and "aging" of **neuropathy target esterase (NTE / PNPLA6)**, "localised to the cytoplasmic face of the endoplasmic reticulum," which normally deacylates ER phosphatidylcholine; its inhibition "may perturb the metabolism of important membrane phospholipids," causing distal axonopathy (**PMC5548687**). Newer work implicates **TRPA1 channel** activation: "a variety of organophosphates, exemplified by malathion, activates TRPA1 but not other neuronal TRP channels" (*Cell Discovery* 2017, celldisc201724). GO: GO:0004622-type phospholipase activity; NTE = **PNPLA6** (HGNC:16268).

**Molecular profiling.** Candidate severity biomarkers beyond cholinesterase include serum **S100B and amyloid-β** (**PMC10579114**) and **creatine phosphokinase (CPK)** for muscle involvement (**PMC9662705**); these are prognostic, not diagnostic.

---

## 7. Anatomical Structures Affected

**Organ / system level:**
- **Nervous system** (primary): central (UBERON:0001017 CNS — brain seizures/excitotoxicity), peripheral/autonomic, neuromuscular junction.
- **Respiratory system** (UBERON:0001004): bronchi (bronchorrhea/bronchospasm), diaphragm (UBERON:0001103) — respiratory failure.
- **Cardiovascular** (UBERON:0004535): brady-/tachyarrhythmia, QT prolongation.
- **Gastrointestinal** (UBERON:0005409): hypersalivation, cramping, diarrhea.
- **Eye** (UBERON:0000970): pupil (miosis via iris sphincter), lacrimal gland (UBERON:0001817).
- **Exocrine glands:** salivary (UBERON:0001044), sweat glands.
- **Skeletal muscle** (UBERON:0001134): fasciculation, weakness, rhabdomyolysis.

**Cell types (CL suggestions):**
- Cholinergic neurons (CL:0000108 cholinergic neuron).
- Skeletal muscle fibers / motor endplate (CL:0000188 cell of skeletal muscle).
- Peripheral neurons and Schwann cells (CL:0002573) — OPIDN axonopathy.
- Bronchial smooth muscle and secretory (goblet) cells; cardiac pacemaker cells.

**Subcellular (GO cellular component):** synaptic cleft (GO:0043083), neuromuscular junction (GO:0031594), endoplasmic reticulum (GO:0005783 — NTE localization), mitochondria (GO:0005739 — Ca²⁺/oxidative injury).

**Localization / lateralization:** systemic and **bilateral/symmetric**; miosis is bilateral; OPIDN is length-dependent and symmetric distal.

---

## 8. Temporal Development

Three temporally distinct phases (a hallmark of OP toxicology):

1. **Acute cholinergic crisis** — onset minutes to a few hours (delayed/prolonged with lipophilic agents like fenthion, which can relapse over days). Duration ~24–72 h; the phase in which most deaths occur.
2. **Intermediate syndrome (IMS)** — "occurs 24–96 hours after exposure," after apparent recovery from cholinergic signs; proximal/respiratory muscle weakness; "the patient usually recovers within 2 or 3 weeks"; atropine/oxime-unresponsive (**PMC5548687**). A critical window because respiratory arrest can occur in a conscious, seemingly recovering patient ("type II respiratory failure," Eddleston 2008).
3. **OPIDN** — delayed, 1–3 weeks (typically ~2 weeks) after exposure; progressive distal sensorimotor neuropathy; recovery partial and slow over months, often incomplete.

**Onset pattern:** acute for the syndrome overall; subacute/delayed for IMS and OPIDN. **Course:** episodic/multiphasic rather than continuously progressive. **Critical intervention window:** the first minutes–hours (decontamination, atropine, early oxime before "aging"); and vigilant monitoring across the 1–4 day IMS window.

---

## 9. Inheritance and Population (Epidemiology)

**Global burden.** OP self-poisoning is a major global health problem. Pesticide self-poisoning overall causes roughly **110,000–168,000 deaths per year**; a systematic review estimated "around one in seven of global suicides were due to pesticide self-poisoning" (~110,000/year, 2010–2014). Eddleston et al. attribute "around two-thirds of these deaths — a total of 200,000 a year" to **organophosphorus** pesticides specifically (**PMID:17706760**; earlier BJPsych global-response analysis, Gunnell & Eddleston, **PMID:16946353 / PMC2493385**).

**Case fatality.** "Medical management is difficult, with case fatality generally more than 15%" and reported ranges of **15–30%** in Asian hospital cohorts (Eddleston 2008). Fatality is compound-dependent (dimethoate, fenthion, parathion far more lethal than malathion/chlorpyrifos).

**Geographic distribution.** Concentrated in **rural low- and middle-income countries** — South Asia (Sri Lanka, India, Bangladesh), Southeast Asia, China, sub-Saharan Africa, and parts of Central/South America — where highly hazardous OP insecticides are agriculturally available. The **Sri Lankan pesticide-ban natural experiment** is the landmark demonstration that means restriction cuts population suicide rates (Lancet Global Health, 2017).

**Demographics.** Male predominance and working-age (roughly 15–45 y) predominance in fatal self-poisoning; a separate pediatric accidental-exposure population exists. Occupational chronic exposure affects agricultural workers of both sexes.

**Genetics (host):** No inheritance pattern for the *disease* (it is acquired). *PON1* susceptibility alleles follow ordinary Mendelian codominant polymorphism inheritance with ancestry-dependent allele frequencies (see §4). Penetrance/expressivity concepts do not apply to a toxic exposure.

---

## 10. Diagnostics

**Diagnosis is primarily clinical** (exposure history + cholinergic toxidrome), supported by:

**Laboratory / biomarkers (LOINC-codable):**
- **Red-cell (erythrocyte) acetylcholinesterase (RBC AChE)** — best surrogate for synaptic AChE; "direct measurement of red blood cell acetylcholinesterase activity indicates the degree of toxicity, and sequential measurement could be used to assess treatment response" (**PMID:17913691**). LOINC ~ "Acetylcholinesterase [Enzymatic activity/volume] in RBC."
- **Plasma butyrylcholinesterase (BChE / pseudocholinesterase)** — "more easily available but may not correlate with severity of poisoning and cannot be used to guide treatment," though useful as an exposure biomarker; "serum cholinesterase can fall to about 40% before any symptoms occur and up to 70–80% before symptoms become severe" (**PMID:25189163 / PMC4224972**; **PMID:17913691**).
- **CPK** (muscle injury / severity prediction; **PMC9662705**); amylase; arterial blood gas (respiratory failure); electrolytes; lactate.
- Emerging: **S100B, amyloid-β** as severity biomarkers (**PMC10579114**).

**Functional / electrophysiology:** ECG (bradycardia, QT prolongation, arrhythmia — prognostic); **repetitive nerve stimulation / EMG** shows decrement-increment and can predict/confirm intermediate syndrome; nerve conduction studies for OPIDN.

**Imaging:** chest X-ray for aspiration pneumonia/ARDS (a complication, not diagnostic).

**Clinical severity criteria:** **Peradeniya Organophosphorus Poisoning (POP) scale** (**PMC10336367**); POP correlates with mortality, ventilation need, and atropine requirement.

**Genetic testing:** Not diagnostic. *PON1* genotyping is a **research/exposure-susceptibility tool**, not a clinical diagnostic (GTR lists PON1 assays for research contexts).

**Differential diagnosis:** carbamate poisoning (same toxidrome, **spontaneously reversible** carbamylation, oximes usually unnecessary/controversial), nerve-agent exposure, muscarine-containing mushroom poisoning, nicotine toxicity, cholinergic drugs, and non-toxic causes of miosis/coma (opioids — miosis but no SLUDGE, no bronchorrhea).

---

## 11. Outcome / Prognosis

**Mortality.** Case fatality **15–30%** in resource-limited cohorts, dominated by early respiratory failure and later IMS-related respiratory arrest, aspiration pneumonia, and ARDS (§9). Death is driven by agent lethality, ingested dose, time-to-treatment, and access to ICU ventilation.

**Prognostic factors:** ingested compound (dimethoate/fenthion/parathion worst), POP severity score, depth/duration of cholinesterase inhibition, GCS/coma at presentation, need for intubation, hypotension, and time to atropinization. Elevated CPK and persistent low RBC AChE predict complicated courses.

**Morbidity in survivors:**
- **Intermediate syndrome** — prolonged ventilation, ICU complications; usually recovers over 2–3 weeks.
- **OPIDN** — distal weakness/sensory loss with slow, often incomplete recovery; long-term disability.
- **COPIND / neuropsychiatric sequelae** — persistent cognitive impairment, depression, anxiety, EEG changes after severe/repeated exposure.
- Anoxic brain injury from prolonged seizures/respiratory failure.

**Recovery potential:** with prompt aggressive supportive care (early intubation, adequate atropinization) survival is good for many insecticides; nerve agents and the most lethal insecticides carry high mortality despite treatment.

---

## 12. Treatment

Management rests on **decontamination + resuscitation + antidotes (atropine, oxime, benzodiazepine)** — MAXO suggestions noted.

**Immediate / supportive (MAXO:0000950 supportive care):** airway protection and **early intubation/mechanical ventilation** for respiratory failure/secretions (MAXO for mechanical ventilation / oxygen administration); IV access, fluids; skin/GI decontamination (remove clothing, wash skin; activated charcoal if early and airway protected). Staff PPE to prevent secondary contamination.

**Antidotes (pharmacotherapy — MAXO:0000058 / administration of drug):**

1. **Atropine (CHEBI:16684)** — competitive muscarinic antagonist; the mainstay, benefit well established. Give by **doubling-dose titration**: "a regimen of doubling doses, with the aim of raising the pulse above 80 beats per minute and systolic blood pressure above 80 mm Hg," continuing "until the heart rate is more than 80 bpm, the systolic BP is more than 80 mm Hg, and the chest is clear" (Eddleston 2008, **PMID:17706760**; doubling-dose vs ad hoc comparison **PMID:18784205**). Does **not** treat nicotinic (muscle weakness) effects. Watch for atropine toxicity (agitation, hyperthermia, ileus).
2. **Oximes — pralidoxime (CHEBI:8354) / obidoxime** — reactivate phosphorylated AChE *before aging*. WHO regimen: "pralidoxime chloride 2 g IV over 20–30 min, follow with an infusion of pralidoxime 0.5–1 g/h" (Eddleston 2008). **Efficacy is genuinely uncertain:** a Cochrane review concluded current evidence is insufficient to show benefit or harm and does not support the WHO regimen; a 2020 meta-analysis of RCTs found "the risk of mortality and the need for ventilator support were not significantly different," with "a significant increase in the incidence of intermediate syndrome in the pralidoxime group" — "pralidoxime was not shown to be beneficial" (**PMID:32257715 / PMC7117609**; earlier systematic review **PMID:11978898**). Curate this as a genuine evidence controversy (SUPPORT vs REFUTE evidence items).
3. **Benzodiazepine — diazepam (CHEBI:49575)** — for seizures/agitation and neuroprotection: "Acutely agitated patients will benefit from treatment with diazepam" (Eddleston 2008); first-line for OP/nerve-agent seizures (with midazolam increasingly preferred pre-hospital).

**Pharmacogenomics:** *PON1* status influences endogenous detoxification (§4) but is not yet used to guide antidote dosing.

**Experimental / investigational therapies:** novel reactivators (e.g., experimental oxime **K027** vs pralidoxime/obidoxime, **PMC6547910**), CNS-penetrant oxime prodrugs, bioscavengers (recombinant/plasma-derived butyrylcholinesterase as a stoichiometric scavenger), magnesium sulfate and clonidine as adjuncts, lipid emulsion, and — for nerve-agent neuroprotection — the Src-kinase inhibitor **saracatinib** (soman model, **PMC12270223**). Search ClinicalTrials.gov for active adjunct trials (magnesium, sodium bicarbonate, fresh frozen plasma/BChE).

**Treatment algorithm summary:** decontaminate → secure airway/ventilate → atropine titrated to secretions/HR/BP → oxime early (per local protocol, acknowledging weak evidence) → benzodiazepine for seizures → ICU monitoring for intermediate syndrome across days 1–4 → rehabilitation for OPIDN.

---

## 13. Prevention

**Primary prevention (the highest-impact lever):**
- **Regulatory bans of highly hazardous OP pesticides** — WHO-endorsed; Sri Lanka's staged bans produced large national declines in suicide with negligible agricultural cost (Lancet Global Health 2017). This population-level **means restriction** is the single most effective intervention.
- Safer formulations, dilution, and secure household/community storage (lockboxes).
- Occupational: PPE, closed application systems, worker training, exposure limits (EPA/WHO).

**Secondary prevention:** occupational **cholinesterase surveillance** of pesticide handlers (baseline + periodic RBC AChE/BChE; remove from exposure at defined depression thresholds — "cholinesterase depression among pesticide handlers," **PMID:25189163**); early recognition and rapid treatment of exposures.

**Tertiary prevention:** ICU monitoring to preempt IMS respiratory arrest; rehabilitation for OPIDN; psychiatric follow-up and safety planning for self-poisoning survivors to prevent repetition.

**Public-health / behavioral:** integrated suicide-prevention (means restriction remains dominant over individual counseling given impulsivity), agricultural extension education, and poison-center infrastructure. **Immunization/prophylaxis:** for anticipated nerve-agent exposure only, military pretreatment with **pyridostigmine** (reversible carbamate that shields a fraction of AChE) plus auto-injector atropine/oxime kits — not applicable to civilian insecticide poisoning.

---

## 14. Other Species / Natural Disease

- **Taxonomy affected:** OPs are toxic across vertebrates and invertebrates (the insecticidal target is homologous insect AChE). Mammals studied include mouse (NCBITaxon:10090), rat (NCBITaxon:10116), guinea pig (NCBITaxon:10141), and non-human primates; birds and fish are ecotoxicologically important.
- **Veterinary relevance:** OP/carbamate toxicosis is a common **companion-animal and livestock** poisoning (dogs, cats, cattle, horses) from flea/tick products, dips, and agricultural exposure — same cholinergic toxidrome, treated with atropine ± pralidoxime. OMIA is not the relevant resource (no Mendelian trait); veterinary toxicology literature and VetCompass cover incidence.
- **Comparative biology:** the AChE mechanism is **deeply evolutionarily conserved** (single active-site serine across taxa), which is why OPs are broad-spectrum. A key **cross-species caveat:** rodents express high **plasma carboxylesterase** that scavenges OPs, conferring protection humans lack — a major translational confounder (§15).
- **Cross-species susceptibility differences** track carboxylesterase levels, PON1 orthologs, and body-size/dosing; guinea pigs (low carboxylesterase) better model human nerve-agent responses than rats/mice.
- **Zoonotic/transmission:** Not applicable (non-communicable toxic exposure).

---

## 15. Model Organisms

- **Guinea pig (NCBITaxon:10141):** historically preferred for nerve-agent/OP work because low plasma carboxylesterase mimics human pharmacokinetics; toxicity is "sex- and age-dependent and cannot be solely accounted for by acetylcholinesterase inhibition" (**PMC2630363**).
- **Rat (NCBITaxon:10116):** widely used for seizure/EEG, respiratory, and countermeasure studies (anesthetized-rat EEG/respiratory assays); confounded by high carboxylesterase.
- **Genetically humanized mice (KIKO):** a modern model — "a novel genetically modified mouse strain (KIKO) with nonfunctional serum carboxylesterase (Es1 KO) and an altered AChE gene expressing the human form (AChE KI)" — engineered to remove the rodent carboxylesterase scavenging confounder and express human-sequence AChE, improving translation for soman/nerve-agent countermeasure testing (**PMC7918218**; MALDI-MSI characterization **PMC11172367**).
- **Model types available:** knock-in (human AChE), knockout (Es1/serum carboxylesterase), and induced (agent-dosed) models. Resources: MGI, IMPC, IMSR.
- **Phenotype recapitulation:** models reproduce cholinergic crisis, seizures/status epilepticus, and respiratory failure, and support antidote/neuroprotectant screening (e.g., saracatinib in soman-poisoned models, **PMC12270223**; physostigmine adjunct in soman guinea pig, **PMC3043258**).
- **Limitations:** rodent carboxylesterase overprotection; species differences in oxime pharmacokinetics and in the human-specific chronicity of IMS/COPIND; nerve-agent models may not fully capture insecticide self-poisoning kinetics (huge ingested doses, slow absorption, prolonged redistribution of lipophilic agents).

---

## Curation Notes & Ontology Cross-Reference Summary

- **Nature of entry:** environmental/toxic exposure syndrome — populate `pathophysiology` around AChE inhibition; treat *PON1* as a `SUSCEPTIBILITY`/`MODIFIER` gene, **not** a causal gene; do not add inheritance blocks for the disease itself.
- **Key genes:** ACHE (HGNC:108), BCHE (HGNC:983), PON1 (HGNC:9204), PNPLA6/NTE (HGNC:16268).
- **Key GO:** GO:0003990 (acetylcholinesterase activity), GO:0007271 (cholinergic synaptic transmission), GO:0007213 (GPCR ACh receptor signaling), GO:0006979 (oxidative stress response), GO:0006954 (inflammation).
- **Key CHEBI:** acetylcholine (CHEBI:15355), atropine (CHEBI:16684), pralidoxime (CHEBI:8354), diazepam (CHEBI:49575), chlorpyrifos (CHEBI:34631), parathion (CHEBI:27928), sarin (CHEBI:75701).
- **Key MAXO:** supportive care (MAXO:0000950), pharmacotherapy/drug administration, mechanical ventilation, dietary/GI decontamination.
- **Evidence controversy to encode explicitly:** oxime/pralidoxime efficacy — pair a SUPPORT item (mechanistic reactivation rationale) with REFUTE/PARTIAL items from the 2020 RCT meta-analysis (**PMID:32257715**) and Cochrane review.

---

## Primary Sources (verify each PMID with `just fetch-reference` before quoting in YAML)

| Topic | Citation | ID |
|---|---|---|
| Mechanism / AChE inhibition review (2023) | Naughton SX, Terry AV. *Toxics* 2023 — Mechanisms of Organophosphate Toxicity and the Role of Acetylcholinesterase Inhibition | **PMID:37888716** / PMC10611379 |
| Clinical management (landmark) | Eddleston M et al. Management of acute organophosphorus pesticide poisoning. *Lancet* 2008 | **PMID:17706760** / PMC2493390 |
| Pralidoxime efficacy meta-analysis | Efficacy of Pralidoxime in OP Poisoning: Systematic Review & Meta-analysis of RCTs, 2020 | **PMID:32257715** / PMC7117609 |
| Oximes systematic review | Eddleston M et al. Oximes in acute OP pesticide poisoning: systematic review of clinical trials, 2002 | **PMID:11978898** |
| Global burden / prevention | Gunnell D, Eddleston M. Deaths from pesticide poisoning: a global response. *Br J Psychiatry* 2006 | **PMID:16946353** / PMC2493385 |
| Novel toxicology/pharmacology review | Eddleston M. Novel Clinical Toxicology and Pharmacology of OP Insecticide Self-Poisoning. *Annu Rev Pharmacol Toxicol* 2019 | (Annu Rev; DOI 10.1146/annurev-pharmtox-010818-021842) |
| PON1 susceptibility | Costa LG et al. Paraoxonase 1 (PON1) as a genetic determinant of susceptibility to OP toxicity | PMC3516631 |
| PON1 meta-analysis | PON1 Q192R and L55M polymorphisms and OP toxicity risk: a meta-analysis, 2013 | **PMID:23590198** |
| Cholinesterase biomarkers | Blood AChE and BChE as biomarkers of cholinesterase depression among pesticide handlers, 2014 | **PMID:25189163** / PMC4224972 |
| RBC AChE / BChE clinical use | RBC acetylcholinesterase and plasma butyrylcholinesterase status, 2007 | **PMID:17913691** |
| Delayed neuropathy (OPIDN) | Delayed Polyneuropathy Induced by Organophosphate Poisoning | PMC5548687 |
| TRPA1 in OPIDN | TRPA1 channel mediates organophosphate-induced delayed neuropathy. *Cell Discovery* 2017 | (celldisc.2017.24) |
| Severity scale | Assessment of the Peradeniya OP Poisoning Scale | PMC10336367 |
| Atropine regimen comparison | Doubling doses vs ad hoc atropinization, prospective study, 2008 | **PMID:18784205** |
| Humanized (KIKO) mouse model | Novel Genetically Modified Mouse Model to Assess Soman Toxicity (KIKO) | PMC7918218 |
| Guinea pig model | Acute Toxicity of OP Compounds in Guinea Pigs is Sex- and Age-Dependent | PMC2630363 |
| Overview reference | Organophosphate Toxicity, StatPearls (NCBI) | NBK470430 |

**Verification reminder for KB ingestion:** every snippet above is drawn from search-surfaced abstracts/reviews; before committing any of these as evidence items, run `just fetch-reference PMID:XXXX` and confirm each snippet is an **exact substring** of the fetched abstract (per the dismech anti-hallucination SOP), and validate all HP/GO/CL/CHEBI/UBERON/MAXO term IDs and labels with `just validate-terms-file`. The oxime-efficacy claim in particular should be curated as a genuine SUPPORT-vs-REFUTE controversy, not a settled recommendation.

**Sources:**
- [Mechanisms of Organophosphate Toxicity and the Role of Acetylcholinesterase Inhibition (Toxics 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10611379/) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37888716/)
- [Management of acute organophosphorus pesticide poisoning (Lancet 2008 / PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2493390/) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/17706760/)
- [Efficacy of Pralidoxime: Systematic Review & Meta-analysis (2020)](https://pubmed.ncbi.nlm.nih.gov/32257715/)
- [Oximes in acute OP pesticide poisoning: systematic review (2002)](https://pubmed.ncbi.nlm.nih.gov/11978898/)
- [Deaths from pesticide poisoning: a global response (BJPsych 2006)](https://pubmed.ncbi.nlm.nih.gov/16946353/)
- [Novel Clinical Toxicology and Pharmacology of OP Insecticide Self-Poisoning (Annu Rev)](https://www.annualreviews.org/content/journals/10.1146/annurev-pharmtox-010818-021842)
- [PON1 as a genetic determinant of susceptibility to OP toxicity](https://pmc.ncbi.nlm.nih.gov/articles/PMC3516631/) · [PON1 Q192R/L55M meta-analysis](https://pubmed.ncbi.nlm.nih.gov/23590198/)
- [Blood AChE and BChE as biomarkers among pesticide handlers](https://pubmed.ncbi.nlm.nih.gov/25189163/) · [RBC AChE and plasma BChE status](https://pubmed.ncbi.nlm.nih.gov/17913691/)
- [Delayed Polyneuropathy Induced by OP Poisoning (OPIDN)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5548687/) · [TRPA1 mediates OPIDN (Cell Discovery)](https://www.nature.com/articles/celldisc201724)
- [Peradeniya OP Poisoning Scale assessment](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10336367/)
- [Doubling doses vs ad hoc atropinization (2008)](https://pubmed.ncbi.nlm.nih.gov/18784205/)
- [KIKO humanized mouse model of soman toxicity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7918218/) · [Guinea pig OP toxicity model](https://pmc.ncbi.nlm.nih.gov/articles/PMC2630363/)
- [Organophosphate Toxicity — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK470430/)

This report is ready to seed a dismech `Organophosphate_Poisoning.yaml` entry. The two most important curation cautions: treat it as a **toxic-exposure** entry (PON1 = susceptibility modifier, no causal gene/inheritance), and encode the **oxime efficacy uncertainty** as competing evidence rather than a recommendation.