---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-04T12:35:46.061308'
end_time: '2026-10-04T12:36:44.799968'
duration_seconds: 58.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: GYG1-Related Disorder of Glycogen Metabolism
  mondo_id: MONDO:0100314
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8112782000000001
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 3
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GYG1-Related Disorder of Glycogen Metabolism
- **MONDO ID:** MONDO:0100314 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GYG1-Related Disorder of Glycogen Metabolism** covering all of the
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

# GYG1-Related Disorder of Glycogen Metabolism (Glycogen Storage Disease XV, glycogenin-1 deficiency): research report

**Method and limits.** I ran three web searches only, so this is not an exhaustive review. Items marked **[verified]** were seen in those results. Items marked **[unverified]** come from my background knowledge. Check those, especially PMIDs, MONDO and HPO IDs, and all numeric frequencies, with `just fetch-reference` and `just validate-terms` before using them in the KB. Per the repo rules, none of the CURIEs below were looked up in a cache, so treat them as leads and not as bindings.

**Searches that returned too little or nothing.** Prevalence and incidence, newborn screening, treatment trials and NCT numbers, and OMIA/VBO veterinary data were not searched. Population-specific data, such as the Sardinian cluster, rest on one search snippet.

---

## 1. Disease information

- **Overview [verified].** Glycogenin-1 deficiency is a rare glycogen storage disorder. Biallelic (homozygous or compound heterozygous) deleterious variants in *GYG1* cause either a slowly progressive adult-onset myopathy with polyglucosan storage in muscle fibres, or a cardiomyopathy with little or no skeletal muscle weakness. ([Hedberg-Oldfors review/cohort, PMC7046021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7046021/); [PubMed 31628455](https://pubmed.ncbi.nlm.nih.gov/31628455/))
- **Identifiers.**
  - Gene OMIM 603942 (GYG1) **[verified]**. The OMIM disease entry is "Glycogen storage disease XV" (GSD15); I recall 613507 for the disease entry **[unverified]**.
  - MONDO:0100314 is as given in the template and was not checked. KEGG Medicus H01955 appeared in results **[verified]**.
  - Orphanet, ICD-10 (E74.0x) and MeSH IDs were not retrieved.
- **Synonyms.**
  - Glycogenin-1 deficiency.
  - GSD XV / GSD15.
  - Polyglucosan body myopathy type 2 (PGBM2) **[unverified]**.
  - Muscle glycogen storage disease associated with glycogenin-1 deficiency.
- **Data provenance.** The literature is case reports and small cohorts of individual patients. Disease-level resources such as OMIM and Orphanet aggregate these reports. No EHR-derived source was found.

## 2. Etiology

- **Cause.** Biallelic loss-of-function or hypomorphic *GYG1* variants. Variants that are compatible with expressed protein can nonetheless be harmful, as the p.Asp102His cardiac cases show (see section 4).
- **Genetic risk factors.** Biallelic *GYG1* variants are the only established cause. No modifier genes were identified in the sources I saw.
- **Environmental and protective factors, gene-environment interactions.** None known.

## 3. Phenotypes

| Phenotype | Suggested HPO (to verify) | Notes |
|---|---|---|
| Proximal/limb-girdle muscle weakness | HP:0003701 (Proximal muscle weakness) | Slowly progressive, adult onset (5th–6th decade in the Sardinian patients) **[verified]** |
| Vacuolar myopathy with PAS-positive polyglucosan deposits | HP:0003803 (Type 1 muscle fibre predominance) and HP:0003713 (muscle fibre necrosis) are not the right terms. Look up a polyglucosan or glycogen-storage-in-muscle term instead. | Subsarcolemmal and intermyofibrillar vacuoles, partly α-amylase-resistant **[verified]** |
| Cardiomyopathy | HP:0001638 (Cardiomyopathy) | Seen in the p.Asp102His men aged 34–52 **[verified]**. Can present with severe cardiac failure and little or no skeletal muscle weakness |
| Cardiac arrhythmia | HP:0011675 (Arrhythmia) | In the first reported patient (Moslemi 2010) **[verified]** |
| Exercise intolerance / myalgia | HP:0003546 | Reported in some patients **[unverified]** |

- **Frequency and severity.** Frequencies per phenotype were not retrieved. Do not assign percentages without a source.
- **Quality of life.** No data found.

## 4. Genetic and molecular information

- **Gene.** *GYG1* (glycogenin-1; HGNC ID not looked up, so verify against `cache/hgnc` before using the lowercase `hgnc:` form).
- **Index case.** Moslemi et al. described a 27-year-old man with muscle weakness and cardiac arrhythmia who was compound heterozygous for a nonsense variant and the missense variant p.Thr83Met. The missense variant abolished glycogenin-1 autoglucosylation, which primes glycogen synthesis ([N Engl J Med 2010, PMID:20357282](https://pubmed.ncbi.nlm.nih.gov/20357282/)) **[verified]**.
- **Cohort.** Malfatti and colleagues (Ann Neurol 2014, PMID not confirmed) described 7 unrelated adults with homozygous or compound heterozygous deleterious variants **[verified]**. Most had no detectable glycogenin-1 in muscle. One had a protein lacking the C-terminus, which normally binds glycogen synthase. The authors concluded that either depletion of glycogenin-1 or impaired interaction with glycogen synthase underlies the disease.
- **Cardiac variant.** Three unrelated men with cardiomyopathy were homozygous for p.Asp102His. The mutant protein expressed in heart had lost autoglucosylation ([Hedberg-Oldfors et al., PMC4724519](https://pmc.ncbi.nlm.nih.gov/articles/PMC4724519) is a likely source; confirm) **[verified for the finding; unverified for the citation]**.
- **Variant class.** Nonsense, missense, splice and null alleles. Functional consequence is loss of function, or loss of autoglucosylation or glycogen synthase binding.
- **Epigenetic and chromosomal data.** None.

## 5. Environmental information

No environmental, lifestyle or infectious factors are known.

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic *GYG1* variants lead to absent, truncated or catalytically inactive glycogenin-1.
2. Without functional glycogenin-1, the autoglucosylation (self-priming) step of glycogen synthesis is lost. This is demonstrated for p.Thr83Met and p.Asp102His in vitro.
3. Branch point A, skeletal muscle with glycogenin-1 absent: muscle can still make glycogen, because glycogenin-2 or other priming routes compensate. This is inferred from the finding that glycogen synthesis proceeds without glycogenin ([PubMed 31628455](https://pubmed.ncbi.nlm.nih.gov/31628455/), "dispensable for glycogen synthesis in human muscle"). The result is focal accumulation of glycogen and polyglucosan, vacuolar myopathy and progressive weakness.
4. Branch point B, heart with a mutant protein that is expressed but inactive: abnormal glycogen is stored, which leads to cardiomyopathy. The proposed explanation is that the expressed mutant protein is deleterious in cardiac tissue, whereas complete absence is better tolerated **[verified in the search summary; mechanism is the authors' interpretation]**.
5. Polyglucosan storage disrupts myofibre architecture and cardiac contractility, leading to the clinical phenotype. This step is inferred.

**Suggested terms (to verify)**
- GO: glycogen biosynthetic process (GO:0005978), glycogenin glucosyltransferase activity (GO:0008466), glycogen metabolic process (GO:0005977).
- CL: skeletal muscle fibre (CL:0008002), cardiac muscle cell (CL:0000746).
- UBERON: skeletal muscle tissue, heart.
- Subcellular: sarcoplasm, subsarcolemmal and intermyofibrillar regions.
- Molecular profiling, advanced technologies and immune involvement: nothing found.

## 7. Anatomical structures affected

- **Primary:** skeletal muscle, mainly proximal and limb-girdle, and heart.
- **Tissue:** muscle fibres with vacuoles containing polyglucosan.
- **Laterality:** presumably bilateral and symmetric. This was not documented in the sources I saw.

## 8. Temporal development

- **Onset:** mostly adult onset (5th–6th decade in the Sardinian patients), but cardiac presentations occurred in the 3rd to 6th decade (ages 34–52 in the p.Asp102His men) **[verified]**.
- **Progression:** slowly progressive myopathy. Cardiac course is variable and can reach severe heart failure **[verified]**.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Founder effects:** a cluster of five Sardinian patients was reported **[verified; variant not retrieved]**. The p.Asp102His recurrence in unrelated men suggests a recurrent or founder allele **[inferred]**.
- **Prevalence, incidence, carrier frequency, sex ratio:** not found.

## 10. Diagnostics

- **Muscle biopsy:** vacuoles with PAS-positive, partly diastase-resistant polyglucosan. Immunohistochemistry or Western blot shows absent or reduced glycogenin-1 in most patients **[verified]**.
- **Genetic testing:** *GYG1* sequencing, or a neuromuscular or cardiomyopathy gene panel or exome.
- **Other tests:** CK, EMG, cardiac MRI, echocardiography and ECG are reasonable. I did not retrieve specific findings.
- **Differential diagnosis:** other polyglucosan storage diseases (*GBE1*-related disease, Pompe disease and other glycogenoses).
- **Screening:** none established.

## 11. Outcome and prognosis

Not retrieved. Prognosis is driven by cardiac involvement, which can cause severe cardiac failure **[verified]**. No survival data found.

## 12. Treatment

No disease-specific therapy found. Management is supportive: cardiac surveillance and standard heart-failure or arrhythmia care, and physical therapy. No clinical trials were identified, and I did not search ClinicalTrials.gov. Suggested NCIT terms (verify): Supportive Care (NCIT:C15747), Physical Therapy (NCIT:C15302), Pharmacotherapy (NCIT:C15986).

## 13. Prevention

Genetic counselling for autosomal recessive risk (NCIT:C15240). Cascade testing of relatives and cardiac surveillance of carriers of cardiomyopathy-associated genotypes are reasonable but unsourced here.

## 14. Other species and natural disease

Not searched. OMIA and VBO have not been checked.

## 15. Model organisms

- **Mouse:** a constitutive Gyg knockout (gene-trap) mouse has been reported **[verified in search summary; the primary citation was not seen]**. About 90% of embryos were lost, but survivors still synthesised glycogen and accumulated high levels of it, especially in skeletal and cardiac muscle. This parallels the human finding that glycogen synthesis continues without glycogenin-1.
- **Limits:** the high lethality and the glycogen accumulation phenotype are not clearly the same as the adult human myopathy. Other models were not searched.
- **Evidence-source tagging:** the mouse work should be tagged `MODEL_ORGANISM`, and the human biopsy and genetic data `HUMAN_CLINICAL`.

---

## Priority follow-ups before curation

1. Fetch and quote the primary papers: PMID:20357282 (Moslemi 2010), the Malfatti 2014 Ann Neurol paper (find its PMID), PMID:31628455, PMC4724519 and PMC7046021.
2. Check for a GeneReviews chapter with `just check-genereviews`, and check ClinGen validity with `just list-gene-validity`.
3. Search for Orphanet prevalence and the HPO annotations for GSD XV.
4. Verify every HPO, GO and CL CURIE above, and replace the phenotype row where I did not give a confident term.

Sources:
- [PubMed 31628455](https://pubmed.ncbi.nlm.nih.gov/31628455/)
- [PMC7046021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7046021/)
- [PMC4724519](https://pmc.ncbi.nlm.nih.gov/articles/PMC4724519)
- [OMIM *603942 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/603942)
- [Institut de Myologie](https://www.institut-myologie.org/en/?p=17297)
- [Reactome R-HSA-3814838](https://reactome.org/content/detail/R-HSA-3814838)
- [Malfatti cohort and mouse model (UB repository)](https://diposit.ub.edu/dspace/handle/2445/100100)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003546` (1 mention) - the report calls it "Exercise intolerance / myalgia"; HP calls it **Exercise intolerance**
- `GO:0005978` (1 mention) - the report calls it "GO: glycogen biosynthetic process"; GO calls it **glycogen biosynthetic process**
- `CL:0008002` (1 mention) - the report calls it "CL: skeletal muscle fibre"; CL calls it **skeletal muscle fiber**

Every term resolved, and every label the report gave matched.