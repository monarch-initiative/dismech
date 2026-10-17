---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T14:59:46.872859'
end_time: '2026-10-15T15:00:58.629002'
duration_seconds: 71.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: AKT3-Related Overgrowth Spectrum
  mondo_id: MONDO:0800485
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7136863999999999
  session_id: 64590904-699d-5a87-8944-0af839afc103
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 5
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AKT3-Related Overgrowth Spectrum
- **MONDO ID:** MONDO:0800485 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **AKT3-Related Overgrowth Spectrum** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# AKT3-Related Overgrowth Spectrum: Research Report

**Scope and evidence caveat.** This report draws on three web searches run in this session. Items marked **[verified]** appeared in those search results (OMIM, MedlinePlus, abstracts). Items marked **[recall]** come from background knowledge and were not re-checked here. Every **[recall]** PMID, and every MONDO, HPO, GO, CL, UBERON and NCIT identifier, must be looked up before it goes into the KB, as the repository's CURIE rule requires. I did not verify MONDO:0800485 or any other ontology ID. Where the literature gives no figure, I say so instead of estimating one.

---

## 1. Disease Information

**Overview.** AKT3-related overgrowth spectrum is a group of brain-overgrowth and cortical-malformation disorders caused by activating variants in *AKT3*. The AKT3 protein is a PI3K-AKT-mTOR pathway kinase. The resulting phenotype depends on whether the variant is germline or somatic and on the mosaic fraction. The spectrum runs from:
- diffuse, constitutional megalencephaly, including megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome (MPPH2), to
- unilateral hemimegalencephaly or focal cortical dysplasia from post-zygotic variants, to
- milder segmental overgrowth.

A cohort study found that "all mutations increased kinase activity, and pleckstrin homology domain mutants exhibited enhanced phospholipid binding" ([Mutations of AKT3 … extreme megalencephaly](https://nemours.elsevierpure.com/en/publications/mutations-of-akt3-are-associated-with-a-wide-spectrum-of-developm/)) **[verified]**.

**Identifiers.**
- *AKT3*: OMIM *611223 **[verified]** ([OMIM](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/611223)).
- MPPH2: OMIM #615937 **[verified]** ([OMIM](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/615937)).
- MONDO:0800485: as given in the request, unverified.
- Orphanet, ICD-10/11 and MeSH: not retrieved. Curators should check them. The nearby ORPHA entries for MPPH and hemimegalencephaly are likely relevant. Hemimegalencephaly is also covered by the MTOR-pathway disorder term that Pharos lists ([Pharos](https://pharos.nih.gov/diseases/overgrowth%20syndrome%20and%2For%20cerebral%20malformations%20due%20to%20abnormalities%20in%20MTOR%20pathway%20genes)).

**Synonyms.**
- MPPH2 / MPPH syndrome.
- AKT3-related megalencephaly.
- AKT3-associated hemimegalencephaly.
- Part of the PIK3CA-related overgrowth spectrum / MTOR-pathway "megalencephaly-capillary malformation" family.

**Data level.** The sources are aggregated, disease-level literature and databases built from patient cohorts and case reports. No EHR-derived data were used.

**Lump/split note for curation.** The spectrum includes:
- constitutional (germline) MPPH2,
- somatic E17K hemimegalencephaly, and
- 1q43q44 deletion/loss-of-function microcephaly (the opposite direction of effect).

The 1q43q44 deletion/loss-of-function microcephaly is probably a separate entry, or a contrasting note. Under the repository's somatic-mosaicism rules, this entry should carry an `HP:0001442` inheritance block for the post-zygotic arm and `variant_origin: SOMATIC` on the relevant gene rows. Check the `somatic-mosaicism` skill and the `Somatic_Mosaic_Disorders` grouping.

---

## 2. Etiology

- **Primary cause.** Activating (gain-of-function) *AKT3* variants. MedlinePlus states: "Each of the known mutations changes a single protein building block… These changes are described as 'gain-of-function' because they increase the activity of the protein" ([MedlinePlus AKT3](https://medlineplus.gov/genetics/gene/akt3)) **[verified]**.
- **Germline arm.** The variants causing MPPH are de novo germline changes **[verified]**. Rivière et al. 2012 reported de novo *AKT3*, *PIK3R2* and *CCND2* mutations in MPPH, PMID 22729224 **[recall]**.
- **Somatic arm.**
  - Isolated hemimegalencephaly arises from somatic mosaic variants. The recurrent one is c.49G>A, p.E17K, in the PH domain.
  - Lee et al. 2012 (PMID 22729223) and Poduri et al. 2012 (PMID 22500628) found somatic *AKT3* variants or duplications in hemimegalencephaly brain tissue **[verified as cited in search summaries]**.
  - A resected hemimegalencephaly sample carried the activating c.49G>A (p.E17K) variant **[verified]** ([PMC3460551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3460551)).
- **Risk and protective factors.** No environmental or lifestyle risk factors are described. No protective alleles or modifier genes are established.
- **Gene-environment interaction.** None documented.
- **Contrasting direction of effect.** Loss of *AKT3* through 1q43q44 deletion is linked to microcephaly. MedlinePlus says that reduced AKT3 activity "likely decreases signaling through the PI3K-AKT-mTOR pathway and restricts cell growth" **[verified]**.

---

## 3. Phenotypes

No quantitative frequencies were retrieved. The qualitative picture below is from the cited cohort and review summaries. The frequency column is deliberately blank where I have no source. Terms are HPO name suggestions that need CURIE lookup.

| Phenotype (suggested HPO term name) | Setting | Notes |
|---|---|---|
| Megalencephaly | Germline, constitutional | Can be extreme, often with polymicrogyria **[verified]** |
| Hemimegalencephaly | Somatic, usually E17K | Highly asymmetric cortical dysplasia **[verified]** |
| Polymicrogyria | Germline/constitutional | Bilateral cortical malformations **[verified]** |
| Focal cortical dysplasia | Somatic | |
| Hydrocephalus | MPPH | Defining feature of the MPPH name |
| Postaxial polydactyly | MPPH | Defining feature of the MPPH name |
| Seizures / epilepsy | Hemimegalencephaly | Often severe and drug-resistant **[recall]** |
| Developmental delay / intellectual disability | All | Variable severity **[recall]** |
| Segmental overgrowth; capillary malformation | Somatic p.T81dup | Milder phenotype; uncommon in AKT3 cases ([2023 case report summary](https://iris.unito.it/handle/2318/1963332)) **[verified]** |

- **Onset.** Prenatal or neonatal macrocephaly and epilepsy in infancy are typical **[recall]**.
- **Severity.** It varies with variant type and mosaic level. The cohort paper describes "several phenotypes dependent on the type of mutation and level of mosaicism" **[verified]**.
- **Quality of life.** No instrument-based data were retrieved.

---

## 4. Genetic/Molecular Information

- **Gene.** *AKT3* (1q44; HGNC symbol AKT3, use the lowercase `hgnc:` CURIE after lookup). AKT3 is a serine/threonine kinase.
- **Variants.**
  - p.E17K: recurrent, somatic, PH domain **[verified]**.
  - p.N229S: reported in a boy with MCAP-overlapping features (Nakamura et al. 2014, PMID 23745724, per the search summary) **[verified as cited]**.
  - p.T81dup: somatic, milder **[verified]**.
  - Other constitutional missense variants are reported. All known variants are single-amino-acid changes **[verified]**.
- **Functional consequence.** Gain of function, with increased kinase activity and enhanced phospholipid binding for PH-domain mutants **[verified]**.
- **Somatic vs germline.** Both occur, as described above.
- **Modifier genes and epigenetics.** None established.
- **Chromosomal abnormalities.** 1q43q44 deletions including *AKT3* cause microcephaly and corpus callosum agenesis (Boland et al. 2007, PMID 17668387 **[recall]**). 1q duplications involving *AKT3* have been linked to megalencephaly **[verified, MedlinePlus: duplication/loss linked to brain size differences]**.
- **Population frequencies.** gnomAD and ClinVar were not queried. The pathogenic variants are expected to be absent from population databases, but this was not checked.
- **Gene-disease validity.** ClinGen was not searched. Per repository policy, copy a tier from a `CGGV:` record. Do not assign one.

---

## 5. Environmental Information

No environmental, lifestyle or infectious factors are known. Leave `environmental:` empty, or add a "searched, none found" note.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. A gain-of-function *AKT3* variant arises, either germline (de novo) or post-zygotic (mosaic). A PH-domain variant such as E17K is an example.
2. This leads to increased membrane (phospholipid) binding and kinase activity **[verified, cohort paper]**.
3. That in turn increases PI3K-AKT-mTOR signaling **[verified, MedlinePlus]**.
4. Excess signaling results in excessive cell growth and division in the developing brain **[verified, MedlinePlus]**.
5. Neural progenitor overproliferation and altered cortical organization are inferred from this. The exact cell-lineage steps are not demonstrated in this search.
6. These produce megalencephaly, polymicrogyria or cortical dysplasia.
   - *Branch, germline:* every cell carries the variant, so the brain is diffusely enlarged (MPPH).
   - *Branch, somatic:* only the mutant clone is affected, so one hemisphere or a region is involved (hemimegalencephaly).
7. The structural lesions lead to seizures and developmental impairment. This step is clinically well established but was not quoted here.

**Detail**
- **Molecular pathway.** PI3K-AKT-mTOR (GO suggestions: positive regulation of protein kinase B signaling; TOR signaling). Look up CURIEs.
- **Protein dysfunction.** Release of PH-domain autoinhibition and enhanced lipid binding.
- **Cell types.** Neural progenitors / radial glia; cortical neurons. Suggest CL terms after lookup.
- **Contrast from knockout.** Akt3−/− mice show "a selective 20% decrease in brain size" with "smaller and fewer cells," and attenuated mTOR signaling in brain ([Easton et al. 2005, PMID 15713641](https://https.ncbi.nlm.nih.gov/pubmed/15713641), via the search summary) **[verified]**. This is consistent with a dosage-sensitive growth role for AKT3 in the brain.
- **Omics, single-cell, spatial and CRISPR data.** None retrieved.

---

## 7. Anatomical Structures Affected

- **Primary.** Cerebral cortex and cerebral hemispheres, with unilateral asymmetry in the somatic arm and bilateral involvement in the germline arm.
- **Other.** The cerebral ventricular system (hydrocephalus) and the digits (polydactyly in MPPH). Skin vasculature (capillary malformation) in some somatic cases.
- **Subcellular.** Plasma membrane (PH-domain lipid binding) and the cytosolic kinase compartment.
- **Suggested UBERON terms.** cerebral cortex, cerebral hemisphere, lateral ventricle. Look up CURIEs.

---

## 8. Temporal Development

- **Onset.** Congenital or prenatal. Macrocephaly is often evident at birth or on prenatal imaging **[recall]**.
- **Progression.** Structural malformations are fixed, while seizure burden and neurodevelopmental impact evolve. Natural-history studies were not retrieved.
- **Remission.** No spontaneous remission is documented. Surgical outcomes after hemispherotomy vary **[recall]**.

---

## 9. Inheritance and Population

- **Inheritance.** MPPH2 variants are de novo, sporadic, heterozygous **[verified]**. The somatic arm is not inherited.
- **Penetrance and expressivity.** Expressivity is highly variable, driven by mosaic fraction and variant **[verified]**. Germline mosaicism was not researched.
- **Prevalence and incidence.** No figures were found. Orphanet may have a prevalence class, so check it. Do not write a rate without a source.
- **Sex ratio, ethnicity, founder effects.** None established.

---

## 10. Diagnostics

- **Imaging.** MRI shows megalencephaly, hemimegalencephaly, polymicrogyria and hydrocephalus. Suggested RadLex/NCIT terms need lookup.
- **Genetic testing.**
  - Germline: multigene panel or exome covering *AKT3*, *PIK3R2*, *PIK3CA* and *CCND2* **[recall]**.
  - Somatic: deep sequencing of resected brain tissue, because blood often misses low-level mosaicism. The hemimegalencephaly studies relied on brain tissue **[verified]**.
  - Chromosomal microarray detects 1q copy-number changes.
- **Histopathology.** Dysmorphic neurons and cortical dyslamination are expected in resected tissue **[recall]**.
- **Differential diagnosis.** MCAP (*PIK3CA*), MPPH1 (*PIK3R2*), *MTOR*-related disease, *PTEN*-related macrocephaly, and *CCND2*-related MPPH. The cohort paper notes overlap with MCAP **[verified]**.
- **Screening.** No newborn or population screening exists.

---

## 11. Outcome/Prognosis

No survival, life-expectancy or quality-of-life figures were retrieved. Prognosis follows seizure control and the extent of malformation. Do not assert numbers in the KB without sources.

---

## 12. Treatment

- **Established.** Antiseizure medication, hydrocephalus shunting, and epilepsy surgery (hemispherotomy for hemimegalencephaly), plus rehabilitation and developmental support. These are standard care **[recall]**. NCIT terms to look up: Surgical Procedure (NCIT:C15329 appears in the repository guidance), Pharmacotherapy (NCIT:C15986), Rehabilitation (NCIT:C15315).
- **Targeted therapy.**
  - AKT or PI3K inhibitors (miransertib, alpelisib) have been used or trialled in PIK3CA- and AKT1-related overgrowth.
  - My search returned no data on these drugs for *AKT3* disease or MPPH.
  - Mark these only as a `KNOWLEDGE_GAP`/hypothesis, and cite nothing until evidence is found.
  - mTOR inhibitors (sirolimus, everolimus) are the usual rationale for pathway-directed therapy. Evidence specific to *AKT3* was not retrieved.
- **Trials.** ClinicalTrials.gov was not searched. Search it for AKT3, MPPH and hemimegalencephaly before adding any `clinical_trials:` entry.
- **Pharmacogenomics.** None known.

---

## 13. Prevention

- No primary prevention exists.
- Genetic counseling applies. Recurrence risk for de novo germline or somatic variants is low, but germline mosaicism cannot be excluded **[recall]**.
- Prenatal diagnosis is possible by ultrasound or MRI and by sequencing when a variant is known.

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease or OMIA entry was found. *Akt3* orthologs are conserved in mouse and rat.

---

## 15. Model Organisms

- **Mouse knockout.** Akt3−/− mice show a selective ~20% reduction in brain size, with smaller and fewer cells and attenuated mTOR signaling, unlike Akt1−/− mice, which shrink all organs ([Easton et al. 2005](https://https.ncbi.nlm.nih.gov/pubmed/15713641), and see also [PMC549378](https://pmc.ncbi.nlm.nih.gov/articles/PMC549378)) **[verified]**. This models the loss-of-function direction, not human overgrowth. A `HUMAN_MODEL_MISMATCH` discussion may fit.
- **Rat gain-of-function model.** Cortical injection of AAV2 carrying constitutively active AKT3 produced larger hemispheres, larger cell bodies, inflammatory cell activation and severe behavioral seizures ([AES abstract](https://aesnet.org/abstractslisting/characterization-of-a-novel-model-of-akt3-associated-hemimegencephaly)) **[verified]**. This is a conference abstract and a viral overexpression model, not a knock-in. Its fidelity is limited by supraphysiological expression.
- **No mouse E17K model** turned up in my search.
- **Other.** iPSC/organoid models were not found. Check MGI, IMPC and Alliance databases.

---

## Priority Verification Checklist for Curators

1. Look up every ontology CURIE and label.
2. Fetch each cited paper with `just fetch-reference PMID:<n>` before quoting. All **[recall]** PMIDs need this, including 22729224, 17668387, and the cohort paper (Alcantara et al., Brain 2017 — PMID not confirmed).
3. Retrieve the Orphanet, ClinGen, GeneReviews and ClinVar records.
4. Search ClinicalTrials.gov, and literature on alpelisib, miransertib and sirolimus in *AKT3* disease.
5. Decide the entry's scope relative to MPPH1/*PIK3R2* and 1q43q44 deletion microcephaly.

**Sources:** [MedlinePlus AKT3](https://medlineplus.gov/genetics/gene/akt3) · [OMIM MPPH2 #615937](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/615937) · [OMIM AKT3 *611223](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/611223) · [AKT3 cohort paper](https://nemours.elsevierpure.com/en/publications/mutations-of-akt3-are-associated-with-a-wide-spectrum-of-developm/) · [PMC3460551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3460551) · [2023 T81dup case (Univ. Torino)](https://iris.unito.it/handle/2318/1963332) · [Easton 2005, PMID 15713641](https://https.ncbi.nlm.nih.gov/pubmed/15713641) · [PMC549378](https://pmc.ncbi.nlm.nih.gov/articles/PMC549378) · [AES rat model abstract](https://aesnet.org/abstractslisting/characterization-of-a-novel-model-of-akt3-associated-hemimegencephaly) · [Pharos](https://pharos.nih.gov/diseases/overgrowth%20syndrome%20and%2For%20cerebral%20malformations%20due%20to%20abnormalities%20in%20MTOR%20pathway%20genes)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.