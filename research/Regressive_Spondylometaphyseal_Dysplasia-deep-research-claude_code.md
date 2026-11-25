---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T16:13:07.745425'
end_time: '2026-11-24T16:18:12.842685'
duration_seconds: 305.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Regressive Spondylometaphyseal Dysplasia
  mondo_id: MONDO:0018663
  category: Mendelian
  causal_genes: LBR
  omim_id: OMIM:618019
  synonyms: Pelger-Huet anomaly with mild skeletal anomalies
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 10
  total_cost_usd: 0.986548735
  session_id: b82a2a05-002a-42d8-bb84-83df2f98b194
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 26
  retrieval_calls: 23
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 48
  verified: 48
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 4
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:19940018
  relevance_assessed: 48
  on_topic: 42
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0018663
    reported_labels:
    - MONDO
    ontology_label: regressive spondylometaphyseal dysplasia
  - term_id: HP:0011870
    reported_labels:
    - term to verify
    ontology_label: Impaired arachidonic acid-induced platelet aggregation
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Regressive Spondylometaphyseal Dysplasia
- **MONDO ID:** MONDO:0018663 (if available)
- **Causal gene(s):** LBR
- **OMIM:** OMIM:618019
- **Synonyms:** Pelger-Huet anomaly with mild skeletal anomalies
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Regressive Spondylometaphyseal Dysplasia** covering all of the
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

Searching for sources now; next I'm fetching the key PubMed abstracts.

All four efetch calls returned complete records with no truncation, so every quote below is verbatim from the efetch output. Where I shortened a sentence, I cut it and marked the cut with "...". Quotes are kept under 125 characters because the source is not preapproved.

Final URLs read:
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=32827848,33846535,36400164,35650273,35707587,32304187&rettype=abstract&retmode=text`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30448303,30052598,29068549,28858257,27830109,27336722,26489030,25348816,23100253,22338047&rettype=abstract&retmode=text`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22140257,21327094,21327084,21327079,21326950,21103616,19940018,18621876,18550262,18495328&rettype=abstract&retmode=text`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18382993,17403717,17245605,16784888,16046620,15773746,15724491,14617022,12490533,9949197&rettype=abstract&retmode=text`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=ichthyosis+AND+lamin+B+receptor+AND+mice`

## (a) Requested batch of six

**PMID 32827848.** "A homozygous variant in the Lamin B receptor gene LBR results in a non-lethal skeletal dysplasia without Pelger-Huët anomaly." Collins M. *Bone*. 2020 Dec;141:115601.
- Variant: "We identified a homozygous LBR missense mutation (NM_002296.4: c.1366C > G, p.(Leu456Val))"
- Phenotype: "Individual 1 has short stature with short limbs (mostly rhizomelic for the upper extremities..."
- Radiology and skeletal: "Individual 2 has similar skeletal features, but also has bowed femurs, osteopenia..."
- Severity: "a skeletal dysplasia milder than Greenberg Dysplasia"
- Sterol: "demonstrate the effect of this variant on sterol C14-reductase activity."
- The abstract does not state the inheritance pattern in words.

**PMID 33846535.** "Deletion of LBR N-terminal domains recapitulates Pelger-Huet anomaly phenotypes in mouse without disrupting X chromosome inactivation." Young AN. *Commun Biol*. 2021 Apr 12;4(1):478.
- Mouse model: "a 236bp N-terminal deletion in the mouse Lbr gene, generating a protein missing the N-terminal domains of LBR"
- Model comparison: "Existing PHA mouse models do not fully recapitulate the human phenotypes..."
- Phenotype: "presents a superior model of human PHA."
- X inactivation: "displays minor X chromosome inactivation defects that do not lead to any overt phenotypes in vivo."
- Sterol: "LBR), a nuclear-membrane protein with sterol reductase activity"
- This is a CRISPR/Cas-9 N-terminal deletion model. It is not the ichthyosis (ic) mouse.

**PMID 36400164.** "Natural history and genetic spectrum of the Turkish metaphyseal dysplasia cohort, including rare types caused by biallelic COL10A1, COL2A1, and LBR variants." Tüysüz B. *Bone*. 2023 Feb;167:116614 (Epub 2022 Nov 15).
- Phenotype: "Biallelic mutation in LBR was described in a patient with prenatal onset short stature, short and curved limb..."
- "Unlike previously reported patients, this patient had ectodermal findings, similar to CHH."
- No HGVS variant is given in the abstract.
- This corrects my earlier report. The verbatim header gives *Bone* 2023 (Epub 2022), not 2022, and the title is now confirmed.

**PMID 35650273.** "Genetic architecture of band neutrophil fraction in Iceland." Oskarsson GR. *Commun Biol*. 2022 Jun 1;5(1):525.
- GWAS: "Five of the variants are at the Lamin B receptor (LBR) locus, encoding an inner nuclear membrane protein."
- PHA: "Mutations in LBR are linked to Pelger-Huët anomaly."
- Cosegregation: "we identify cosegregation of a rare stop-gain sequence variant in LBR and Pelger Huët anomaly..."
- Stop-gain variant not named in the abstract.

**PMID 35707587.** "Blended Phenotype of Pelger-Huet Anomaly with Osteochondroma and Autosomal Recessive Deafness with Enlarged Vestibular Aqueduct." Cinleti T. *Mol Syndromol*. 2022 May;13(3):200-205.
- Phenotype: "We report a case with SNHL, multiple skeletal anomalies including osteochondroma, developmental delay..."
- Variant: "Molecular studies revealed a heterozygous pathogenic variant in the LBR gene..."
- Second diagnosis: "a homozygous likely pathogenic variant in the SLC26A4 gene"
- PHA: "PHA may be accompanied by multiple skeletal abnormalities."

**PMID 32304187.** "A new case of Greenberg dysplasia and literature review suggest that Greenberg dysplasia, dappled diaphyseal dysplasia, and Astley-Kendall dysplasia are allelic disorders." Gregersen PA. *Mol Genet Genomic Med*. 2020 Jun;8(6):e1173.
- Inheritance: "Greenberg dysplasia is a rare, autosomal recessive, prenatal lethal bone dysplasia..."
- Genetics: "Genetic testing confirmed the diagnosis Greenberg dysplasia: homozygosity for a pathogenic variant in LBR."
- Conclusion: "we suggest that these are allelic disorders."
- No HGVS variant is given in the abstract.

## Ichthyosis esearch (6 hits, all fetched)

The query `ichthyosis AND lamin B receptor AND mice` returned Count 6: 22140257, 18621876, 18550262, 18495328, 17403717, 12490533. All six are in the batch (b) list below.

## (b) Requested unfetched batch: relevant records

**PMID 30448303.** "Lamin B receptor-related disorder is associated with a spectrum of skeletal dysplasia phenotypes." Thompson E. *Bone*. 2019 Mar;120:354-363.
- Variants: "Exome sequencing revealed two novel variants in LBR, c.1504C > G (p.Arg502Gly) in exon 12..."
- Patient 2: "Patient 2 is homozygous for a pathogenic variant c.1534C > T (p.Arg512Trp) in exon 12 of LBR..."
- Inheritance: "which were inherited from her unaffected father and mother, respectively."
- Radiology: "Patient 1 exhibited frontal bossing, mid-face hypoplasia, short stature with rhizomelic limb shortening..."
- Sterol: "Sterol analysis revealed an increased level of cholesta-8,14-dien-3beta-ol to 2.9% of total sterols..."

**PMID 29068549.** "Expanding the genetic architecture and phenotypic spectrum in the skeletal ciliopathies." Zhang W. *Hum Mutat*. 2018 Jan;39(1):152-166.
- "LBR, which encodes a nuclear membrane protein with sterol reductase activity."
- "Causal variants were discovered in 14 genes in 120 families..."
- This is a large skeletal ciliopathy cohort. The abstract does not describe individual LBR variants.

**PMID 28858257.** "Lamin B Receptor: Interplay between Structure, Function and Localization." Nikolakaki E. *Cells*. 2017 Aug 31;6(3):28. (Review)
- "its transmembrane domains exhibit sterol reductase activity"
- "Mutations within the transmembrane segments result in defects in cholesterol synthesis..."

**PMID 27830109.** "Pelger-Huët anomaly and Greenberg skeletal dysplasia: LBR-associated diseases of cholesterol metabolism." Turner EM. *Rare Dis*. 2016 Sep 27;4(1):e1241363.
- This record is an erratum/commentary on Tsai PL et al. (eLife 2016).
- Sterol: "a defect in cholesterol synthesis due to loss of LBR-associated sterol C14 reductase activity"
- Mechanism: "disease-associated LBR point mutations reduce sterol C14 reductase activity by decreasing the affinity of LBR..."

**PMID 27336722.** "The Lamin B receptor is essential for cholesterol synthesis and perturbed by disease-causing mutations." Tsai PL. *eLife*. 2016 Jun 23;5:e16011.
- "We demonstrate that human LBR is essential for cholesterol synthesis."
- "LBR mutant derivatives implicated in Greenberg skeletal dysplasia or Pelger-Huët anomaly fail to rescue..."
- "point mutations in the sterol reductase domain perturb enzymatic activity by reducing the affinity..."
- "LBR truncations render the mutant protein metabolically unstable..."

**PMID 25348816.** "An anadysplasia-like, spontaneously remitting spondylometaphyseal dysplasia secondary to lamin B receptor (LBR) gene mutations..." Sobreira N. *Am J Med Genet A*. 2015 Jan;167A(1):159-63.
- "By whole exome sequencing he was shown to have compound heterozygous mutations of LBR..."
- "homozygosity or compound heterozygosity of mutations in LBR can result in a mild, spontaneously regressing bone dysplasia."

**PMID 22338047.** "Understanding and recognizing the Pelger-Huët anomaly." Colella R. *Am J Clin Pathol*. 2012 Mar;137(3):358-66. (Review)
- "PHA is caused by a decreased amount of the lamin B receptor (LBR)."
- "Recognition of PHA morphologic features serves as a marker for mutations in the LBR gene."

**PMID 22140257.** "Lamin B receptor regulates the growth and maturation of myeloid progenitors via its sterol reductase domain..." Subramanian G. *J Immunol*. 2012 Jan 1;188(1):85-102.
- Mouse model: "a myeloid model of ichthyosis (ic) bone marrow that lacks Lbr expression"
- Sterol: "the sterol Δ(14) reductase domain of LBR plays a critical role in cholesterol biosynthesis"
- Rescue: "Ectopic expression of a full-length Lbr in EML-ic/ic cells rescued both nuclear lobulation and growth arrest..."

**PMID 21327094.** "An in vitro model for Pelger-Huët anomaly: stable knockdown of lamin B receptor in HL-60 cells." Olins AL. *Nucleus*. 2010 Nov-Dec;1(6):506-12. (Human cell model, not a mouse.)
- "the LBR knockdown cells retain an ovoid shaped nucleus with reduced levels of lamin A/C..."

**PMID 21327084.** "Mutations causing Greenberg dysplasia but not Pelger anomaly uncouple enzymatic from structural functions of a nuclear membrane protein." Clayton P. *Nucleus*. 2010 Jul-Aug;1(4):354-66.
- Sterol: "LBR missense mutations can abolish sterol reductase activity, causing lethal Greenberg dysplasia but not Pelger anomaly."
- Yeast: "both mutations failed to rescue C14 sterol reductase deficient yeast..."
- Mouse: "We studied Lbr in mouse embryos and demonstrate expression in skin and the developing skeletal system..."

**PMID 21327079.** "The danger of 'multi-tasking': LBR out of control." Herrmann H. *Nucleus*. 2010 Jul-Aug;1(4):319-24. (Commentary.)
- "a less well characterized functional role as a sterol reductase"

**PMID 21326950.** "Dosage effect of zero to three functional LBR-genes in vivo and in vitro." Gravemann S. *Nucleus*. 2010 Mar-Apr;1(2):179-89.
- Dosage: "there is a highly significant gene-dosage effect between the gene copy number and the nuclear segmentation index..."

**PMID 19940018.** "Induction of a massive endoplasmic reticulum and perinuclear space expansion by expression of lamin B receptor mutants and the related sterol reductases TM7SF2 and DHCR7." Zwerger M. *Mol Biol Cell*. 2010 Jan 15;21(2):354-68.
- "Mutations in the LBR gene cause two different human diseases: Pelger-Huët anomaly and Greenberg skeletal dysplasia..."
- "forced expression of the two structurally related sterol reductases transmembrane 7 superfamily member 2..."

**PMID 18621876.** "The lamin B receptor under transcriptional control of C/EBPepsilon is required for morphological but not functional maturation of neutrophils." Cohen TV. *Hum Mol Genet*. 2008 Oct 1;17(19):2921-33.
- Mouse model: "we derived a novel mouse model with a gene-trap insertion into the Lbr locus (Lbr(GT/GT))"
- "Phenotypically, the Lbr(GT/GT) mice are similar to ichthyosis mice."
- "Our findings indicate that the Lbr(GT/GT) mice are a model for Pelger-Huët anomaly..."

**PMID 18550262.** "Mouse neutrophils lacking lamin B-receptor expression exhibit aberrant development and lack critical functional responses." Gaines P. *Exp Hematol*. 2008 Aug;36(8):965-76.
- "Neutrophils derived from EML-ic/ic cells exhibited nuclear hypolobulation identical to that observed in ichthyosis mice."
- "produced a deficient respiratory burst upon terminal maturation."

**PMID 18495328.** "Granulocytic nuclear differentiation of lamin B receptor-deficient mouse EPRO cells." Zwerger M. *Exp Hematol*. 2008 Aug;36(8):977-87.
- "ic/ic granulocytes exhibited smaller ovoid nuclei devoid of LBR."
- "Lamin A/C, which is normally not present in mature granulocytes, was significantly elevated in LBR-deficient EPRO cells."

**PMID 18382993.** "Pathologic, radiographic and molecular findings in three fetuses diagnosed with HEM/Greenberg skeletal dysplasia." Konstantinidou A. *Prenat Diagn*. 2008 Apr;28(4):309-12.
- Variant: "a homozygous, N547D amino acid substitution in the LBR gene in the third affected fetus"
- Radiology: "The characteristic 'moth-eaten' radiographic appearance is already seen at 13 weeks' gestational age."

**PMID 17403717.** "HEM dysplasia and ichthyosis are likely laminopathies and not due to 3beta-hydroxysterol Delta14-reductase deficiency." Wassif CA. *Hum Mol Genet*. 2007 May 15;16(10):1176-87.
- Knockout mouse: "we obtained ichthyosis mice (Lbr(-/-)) and disrupted Dhcr14."
- Sterol: "no sterol abnormalities were detected in either liver or kidney tissue."
- Brain: "relatively small transient elevations of Delta(14)-sterols were observed in Lbr(-/-) and Dhcr14 brain tissue"
- Redundancy: "LBR and DHCR14 provide substantial enzymatic redundancy with respect to cholesterol synthesis..."
- "Neither of these mutants resembles the ichthyosis mouse..."

**PMID 17245605.** "The granulocyte nucleus and lamin B receptor: avoiding the ovoid." Hoffmann K. *Chromosoma*. 2007 Jun;116(3):227-35. (Review.)
- "A single dominant mutation in humans leads to neutrophils with hypolobulated nuclei"
- "Homozygosity for null mutations is frequently lethal and associated with severe skeletal deformities."

**PMID 16784888.** "Sterol dependent regulation of human TM7SF2 gene expression: role of the encoded 3beta-hydroxysterol Delta14-reductase in human cholesterol biosynthesis." Bennati AM. *Biochim Biophys Acta*. 2006 Jul;1761(7):677-85.
- "Both human C14SR and LBR expressed in COS-1 cells exhibit 3beta-hydroxysterol Delta(14)-reductase activity in vitro."
- "a primary role of C14SR in human cholesterol biosynthesis, whereas LBR role in the pathway remains unclear."

**PMID 15773746.** "Components of the nuclear envelope and their role in human disease." Worman HJ. *Novartis Found Symp*. 2005;264:35-42. (Review.)
- "homozygous mutations cause HEM/Greenberg skeletal dysplasia, characterized by developmental abnormalities..."

**PMID 15724491.** "[Nuclear abnormalities in Pelger-Huet anomaly; progress in blood cell morphology]." Tomonaga M. *Rinsho Byori*. 2005 Jan;53(1):54-60. (Japanese article; English abstract quoted.)
- "Lack of LBR protein in familial Pelger-Huet anomaly results in hypolobulation and chromatin-hypercondensation in neutrophils..."

**PMID 14617022.** "Lamin B-receptor mutations in Pelger-Huët anomaly." Best S. *Br J Haematol*. 2003 Nov;123(3):542-4.
- "Following linkage studies in two families, the lamin B-receptor (LBR) was sequenced and mutations found..."
- "CCG-->CTG causing proline-->leucine in codon 119 of exon 3, and IVS11-9 A-->G, disrupting the splice acceptor site"
- "a heterozygous C-->G mutation was found in codon 569 of exon 14, predicted to cause a proline-->arginine"

**PMID 12490533.** "Mutations at the mouse ichthyosis locus are within the lamin B receptor gene: a single gene model for human Pelger-Huët anomaly." Shultz LD. *Hum Mol Genet*. 2003 Jan 1;12(1):61-9.
- Knockout alleles: "we identified one nonsense (815ins) and two frameshift mutations (1088insCC and 1884insGGAA) within the Lbr gene..."
- Complete loss: "Our studies of mice homozygous for the ic(J) mutation revealed a complete loss of LBR protein..."
- Phenotype: "Mice homozygous for deleterious alleles at the ichthyosis (ic) locus present with a blood phenotype similar to PHA..."
- "develop other phenotypic abnormalities, including alopecia, variable expression of syndactyly and hydrocephalus."

## Tangential (not in the requested categories; titles only)

- PMID 23100253: "Lamin B receptor recognizes specific modifications of histone H4 in heterochromatin formation." Hirano Y. *J Biol Chem*. 2012. Heterochromatin function only.
- PMID 16046620: "Alterations of nuclear envelope and chromatin organization in mandibuloacral dysplasia, a rare form of laminopathy." Filesi I. *Physiol Genomics*. 2005. LBR is delocalized in a LMNA disorder.
- PMID 26489030: "Genetic Predictors of Depressive Symptoms in the Look AHEAD Trial." McCaffery JM. *Psychosom Med*. 2015. LBR SNPs only.
- PMID 21103616: "Nuclear shape in papillary thyroid carcinoma: a role for lamin B receptor?" Recupero D. *Rom J Morphol Embryol*. 2010. LBR expression in thyroid cancer.

## Unrelated (excluded)

- PMID 30052598: "Mixed Session Periodization..." (LBR here is an author name.)
- PMID 9949197: "Distribution of emerin and lamins in the heart..." (LBR only as a family member.)

No record in these results describes an ichthyosis mouse phenotype beyond the ic/ic and Lbr(GT/GT) and Lbr(-/-) models above. The lamin B receptor sterol-reductase data in this batch come from the Tsai, Clayton, Wassif, Bennati, Turner, and Thompson records.

**Assumptions and limits of this report.** I took the disease to be the **LBR‑related, autosomal recessive, non‑lethal skeletal dysplasia with partial spontaneous regression**, as defined by the identifiers MONDO:0018663 and OMIM:618019, with **LBR (lamin B receptor)** as the causal gene. This disorder has been published under several names: "Pelger‑Huët anomaly with mild skeletal anomalies" (Borovik 2013), "anadysplasia‑like spontaneously remitting SMD" (Sobreira 2015) and "LBR‑related regressive SMD" (Turgut 2022). KEGG H02732 and MedGen use the newer name "Rhizomelic skeletal dysplasia with or without Pelger‑Huët anomaly (SKPHA)" ([KEGG H02732](https://www.kegg.jp/entry/H02732); [MedGen](https://https.ncbi.nlm.nih.gov/medgen/1648288)).

I could not open OMIM, Orphanet, PubMed web pages or PMC; each returned a bot check or a 403. All PMIDs and quotes below come from NCBI E‑utilities abstract text retrieved in this session. Fields that would need full texts or databases I could not reach (ClinVar, gnomAD, HPO annotation frequencies, Orphanet prevalence and codes) are marked **not retrieved**. Suggested ontology IDs are my own suggestions and should be checked against the ontologies before use.

---

## 1. Disease information

**Overview.** This is a rare autosomal recessive skeletal dysplasia caused by biallelic (homozygous or compound heterozygous) **LBR** variants. It sits at the mild, survivable end of the LBR spectrum, between heterozygous Pelger‑Huët anomaly (PHA, a harmless blood finding) and homozygous, lethal Greenberg (HEM) dysplasia.
- Typical features: prenatal or infantile short stature, rhizomelic (proximal) limb shortening, bowed long bones, and spondylometaphyseal changes on X‑ray that improve over time.
- PHA (hyposegmented, "pince‑nez" or ovoid neutrophil nuclei) is usually present, but not always.

Key evidence:
- Borovik et al. 2013 (PMID 23824842) described the first case: a girl with bilobed neutrophils and a mild skeletal dysplasia who was compound heterozygous for "c.651_653 delinsTGATGAGAAA (p.Ile218Aspfs*19) and c.1757G > A (p.Arg586His)". They wrote: "These mutations were found to be in trans, and, thus, she is a compound heterozygote."
- Sobreira et al. 2015 (PMID 25348816) concluded that "homozygosity or compound heterozygosity of mutations in LBR can result in a mild, spontaneously regressing bone dysplasia."

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0018663 | given in brief |
| OMIM | 618019 (current label appears to be "Rhizomelic skeletal dysplasia with or without Pelger‑Huët anomaly", SKPHA) | page blocked; label from KEGG/MedGen |
| KEGG Disease | H02732 | retrieved via search |
| MedGen | 1648288 | retrieved via search |
| Orphanet | "Regressive spondylometaphyseal dysplasia", probably ORPHA:93357 | **unverified** (bot check) |
| ICD‑10 / ICD‑11 / MeSH | not retrieved; likely a generic osteochondrodysplasia code (ICD‑10 Q77.8) | **unverified** |

**Synonyms:** regressive spondylometaphyseal dysplasia (SMD); LBR‑related regressive SMD (LBR‑R‑SMD); Pelger‑Huët anomaly with mild skeletal anomalies; rhizomelic skeletal dysplasia with or without Pelger‑Huët anomaly (SKPHA); anadysplasia‑like spontaneously remitting SMD.

**Evidence base:** fewer than about 15 published individual patients and fetuses in case reports. There are no registries or EHR cohorts.

## 2. Etiology

- **Causal factor:** biallelic pathogenic LBR variants, which reduce the protein's 3β‑hydroxysterol Δ14‑reductase (sterol C14 reductase) activity and/or its structural role at the nuclear envelope. Thompson et al. 2019 (PMID 30448303) summarised this as "Lamin B receptor‑related disorder is associated with a spectrum of skeletal dysplasia phenotypes."
- **Genetic risk:**
  - Carrier parents, each heterozygous; heterozygotes often show PHA themselves.
  - Consanguinity: one Turkish pedigree had a homozygous p.Arg512Trp variant with apparent pseudodominant transmission (Turgut 2022, PMID 34467646).
  - Severity appears to depend on genotype. Giorgio et al. 2019 (PMID 30561119) proposed it depends on "the functional domain affected, the heterozygous or homozygous state of the variants."
- **Environmental risk, protective factors, gene–environment interaction:** none reported. A plausible but untested idea is that dietary or maternal cholesterol supply could modify the phenotype; no human data exist.
- **Modifier genes:** none reported in humans. The paralogous sterol reductase **TM7SF2 (DHCR14)** gives partial enzymatic redundancy in mice. Wassif 2007 (PMID 17403717): "LBR and DHCR14 provide substantial enzymatic redundancy with respect to cholesterol synthesis". In human cells, Bennati 2006 (PMID 16784888) found "a primary role of C14SR in human cholesterol biosynthesis". This redundancy is a candidate modifier, inferred rather than demonstrated in patients.

## 3. Phenotypes

Frequencies are qualitative because the case series are very small.

| Phenotype | Suggested HPO | Onset / course | Frequency | Source |
|---|---|---|---|---|
| Short stature, prenatal onset | HP:0004322 short stature; HP:0003561 birth length less than 3rd percentile | prenatal; partial catch‑up | most | 36400164 ("prenatal onset short stature, short and curved limb"); 32827848 |
| Rhizomelic limb shortening | HP:0008905 rhizomelia | prenatal or infancy; improves | most | 30448303 ("short stature with rhizomelic limb shortening"); 32827848 |
| Bowed long bones (femora) | HP:0002980 femoral bowing; HP:0006487 bowing of the long bones | prenatal; regresses | frequent | 34467646 ("short and bowed tubular bones"); 32827848 ("bowed femurs") |
| Spondylometaphyseal changes that regress | HP:0003300 ovoid vertebral bodies / HP:0003016 metaphyseal widening (approximate terms) | infancy; spontaneous radiological improvement | defining | 25348816 |
| Narrow thorax (fetal) | HP:0000774 | prenatal | occasional | 34467646 |
| Frontal bossing, midface hypoplasia | HP:0002007, HP:0011800 | infancy | occasional | 30448303 |
| Osteopenia | HP:0000938 | childhood | occasional | 32827848 |
| Hyposegmented neutrophils (Pelger‑Huët anomaly) | HP:0011870 (term to verify) | lifelong, harmless | usual; absent in the p.Leu456Val family | 23824842; 34467646; 32827848 |
| Ectodermal findings resembling cartilage‑hair hypoplasia (CHH) | HP:0008070 sparse hair (approximate) | childhood | single case | 36400164 |
| Hemivertebrae / scoliosis | HP:0002937, HP:0002650 | childhood | single heterozygous case, uncertain | 40980134 |
| Trace cholesta‑8,14‑dien‑3β‑ol (laboratory) | HP:0003107 abnormal cholesterol metabolism (approximate) | n/a | when measured | 23824842 ("trace amounts of cholesta-8,14-dien-3beta-ol"); 30448303 ("2.9% of total sterols") |

**Quality of life:** no EQ‑5D, SF‑36 or other formal data were found. The impact is mainly short stature and orthopaedic problems in childhood, which lessen with regression. PHA itself does not impair neutrophil function in humans.

## 4. Genetic and molecular information

**Gene:** LBR, lamin B receptor, on 1q42.12. Gene MIM *600024 (not retrieved this session); HGNC:6518 (verify). Transcripts NM_002296.4 / NP_002287.2. The protein has a nucleoplasmic N‑terminal domain that binds lamin B, chromatin and HP1, plus 8 transmembrane domains with a sterol‑reductase (ERG24 family) domain. Nikolakaki 2017 (PMID 28858257): "its transmembrane domains exhibit sterol reductase activity."

**Reported variants in the non‑lethal recessive phenotype**

| Variant (NM_002296.4 unless noted) | Type | Zygosity | Phenotype | PMID |
|---|---|---|---|---|
| c.651_653delinsTGATGAGAAA p.(Ile218Aspfs*19) + c.1757G>A p.(Arg586His) | frameshift + missense | compound heterozygous | PHA + mild skeletal | 23824842 |
| compound heterozygous LBR variants (not named in abstract) | — | compound heterozygous | spontaneously remitting SMD | 25348816 |
| c.1504C>G p.(Arg502Gly) + second novel variant | missense | compound heterozygous | rhizomelic dysplasia | 30448303 |
| c.1534C>T p.(Arg512Trp) | missense | homozygous | SMD; PHA allele | 30448303; 34467646 |
| c.1366C>G p.(Leu456Val) | missense | homozygous | non‑lethal dysplasia **without** PHA | 32827848 |
| c.1757G>A p.(Arg586His) | missense | homozygous | moderate recurrent fetal dysplasia | 36712868 |
| c.1687+1G>A + c.1757G>A p.(Arg586His) | splice + missense | compound heterozygous | fetal rhizomelic dysplasia | 38946370 |
| c.43C>T p.(Arg15*) + c.1640A>G p.(Asn547Ser) | nonsense + missense | compound heterozygous | rhizomelic dysplasia + PHA (mother also affected) | 41059452 |
| c.1011T>G p.(Cys337Trp) + LBR deletion | missense + deletion | compound heterozygous | skeletal dysplasia | 40355051 |

**Genotype–phenotype pattern** (inferred from the reports above):
- Homozygous null or catalytically dead alleles in the sterol‑reductase domain cause lethal Greenberg dysplasia. Examples: the homozygous 1599‑1605 substitution (Waterham 2003, PMID 12618959); N547D (PMID 18382993); D460R (PMID 30561119).
- Hypomorphic missense alleles, or one hypomorphic allele combined with a null allele, give the regressive SMD phenotype.
- Heterozygous loss of function gives PHA only. Hoffmann 2002 (PMID 12118250) "identified four splice-site, two frameshift and two nonsense mutations in LBR".
- A homozygous p.Val482Gly allele gives PHA **without** skeletal dysplasia and "has no direct influence on the LBR sterol reductase activity" (Hoffmann 2026, PMID 42622427).

**Other molecular fields**
- **ACMG classification, ClinVar entries, gnomAD frequencies:** not retrieved.
- **Origin:** germline only.
- **Functional consequence:** loss of function, either partial or complete, of the sterol C14 reductase and/or the structural lamina‑binding role.
- **Modifier genes:** see section 2.
- **Epigenetics:** LBR tethers heterochromatin to the nuclear envelope. Hirano 2012 (PMID 23100253) showed it "recognizes specific modifications of histone H4". No disease‑specific epigenomic data exist.
- **Chromosomal abnormalities:** one intragenic or whole‑gene LBR deletion has been reported as the second allele (PMID 40355051). No other structural abnormalities are known.

## 5. Environmental information

No environmental, lifestyle or infectious factors have been reported. Not applicable.

## 6. Mechanism and pathophysiology

**Causal chain**
1. Biallelic hypomorphic LBR variants (germline) lead to reduced sterol C14 reductase activity. Point mutations lower substrate affinity, and truncations destabilise the protein. *Demonstrated in vitro:* Tsai 2016 (PMID 27336722) found that "point mutations in the sterol reductase domain perturb enzymatic activity by reducing the affinity..." and that "LBR truncations render the mutant protein metabolically unstable".
2. Reduced C14 reductase activity leads to accumulation of the Δ14 intermediate cholesta‑8,14‑dien‑3β‑ol and to impaired cell‑autonomous cholesterol synthesis. *Shown in patients and cells* (PMID 23824842; 30448303; 12618959). Tsai 2016: "human LBR is essential for cholesterol synthesis."
3. Impaired cholesterol supply in growth‑plate chondrocytes and developing bone leads to disturbed endochondral ossification. *Partly inferred.* Lbr is expressed "in skin and the developing skeletal system" in mouse embryos (Clayton 2010, PMID 21327084). One study proposes that cholesterol deficit impairs canonical **Wnt/β‑catenin** signalling in skeletal cells: "disruption of cholesterol synthesis by LBR impairs Wnt pathway" (Chen 2025, PMID 40355051). That study also reports that LBR is an FBW7 substrate.
4. Disturbed endochondral ossification results in short, bowed long bones and spondylometaphyseal dysplasia in utero and infancy.
5. With residual enzyme activity, plus redundancy from TM7SF2/DHCR14 and/or dietary cholesterol after birth (*hypothesis*), growth‑plate function partly recovers, which results in the **radiological regression** (PMID 25348816). The mechanism of regression has not been demonstrated.
6. **Haematological branch:** a reduced amount of the structural LBR protein (dosage‑dependent) leads to failure of neutrophil nuclear lobulation, i.e. the Pelger‑Huët anomaly.
   - Gravemann 2010 (PMID 21326950): "a highly significant gene-dosage effect between the gene copy number and the nuclear segmentation index".
   - Colella 2012 (PMID 22338047): "PHA is caused by a decreased amount of the lamin B receptor (LBR)."
   - The two branches can be uncoupled. Clayton 2010 (PMID 21327084): "LBR missense mutations can abolish sterol reductase activity, causing lethal Greenberg dysplasia but not Pelger anomaly." Conversely, p.Leu456Val gives skeletal disease without PHA (PMID 32827848), and p.Val482Gly gives PHA without skeletal disease (PMID 42622427).

**Caveat on the mechanism.** In Lbr‑/‑ (ichthyosis) mice, "no sterol abnormalities were detected in either liver or kidney tissue". The authors argued that HEM and ichthyosis "are likely laminopathies" rather than primary sterol disorders (Wassif 2007, PMID 17403717). The relative weight of the sterol and structural roles is therefore still debated.

**Mutant‑protein cell stress:** expressing LBR mutants induces "a massive endoplasmic reticulum and perinuclear space expansion" (Zwerger 2010, PMID 19940018). Whether this happens in patients is unknown.

**Suggested GO terms:** GO:0006695 cholesterol biosynthetic process; GO:0050613 Δ14‑sterol reductase activity; GO:0001958 endochondral ossification; GO:0060070 canonical Wnt signaling pathway; GO:0006998 nuclear envelope organization; GO:0030223 neutrophil differentiation.

**Suggested CL terms:** CL:0000138 chondrocyte; CL:0000062 osteoblast; CL:0000775 neutrophil; CL:0000057 fibroblast (cell type used for sterol assays).

**Omics, single‑cell, spatial and CRISPR data:** none disease‑specific found.

## 7. Anatomical structures affected

- **Organs and tissues:**
  - Primary: skeleton, especially the long bones of the limbs (UBERON:0002495), femur (UBERON:0000981), vertebral column (UBERON:0001130) and metaphyses/growth plates (UBERON:0004378 epiphyseal plate, to verify), plus cartilage.
  - Secondary: thorax (narrow in fetuses), blood (neutrophils), and occasionally skin or hair (PMID 36400164).
- **Body systems:** musculoskeletal and haematopoietic.
- **Cells:** chondrocytes, osteoblasts and neutrophils.
- **Subcellular location:**
  - Nuclear inner membrane (GO:0005637) and endoplasmic reticulum membrane (GO:0005789).
  - Nuclear lamina (GO:0005652); heterochromatin (GO:0000792).
- **Laterality:** bilateral and symmetric.

## 8. Temporal development

- **Onset:** prenatal. Fetal ultrasound shows short, bowed bones and a narrow thorax; Turgut 2022 reported "the first case with radiological manifestations of LBR-R-SMD in the fetal period" (PMID 34467646).
- **Course:** the skeletal changes partly improve over infancy and childhood ("spontaneously remitting"; PMID 25348816). Short stature can persist into adulthood; an affected mother had milder findings (PMID 41059452).
- **Pattern and duration:** spontaneous partial remission of the bone changes; PHA is lifelong.
- **Stages:** none defined.
- **Critical period:** prenatal diagnosis, where this mild disorder must be distinguished from lethal Greenberg dysplasia. Turgut 2022 calls this an "antenatal diagnostic dilemma".

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Heterozygous carriers often show PHA, so carrier status behaves as co‑dominant at the haematological level. Waterham 2003 (PMID 12618959): "classic Pelger-Huët anomaly represents the heterozygous state of 3beta-hydroxysterol delta(14)-reductase deficiency."
- **Pseudodominance:** described in a consanguineous family (PMID 34467646) and in a family where mother and son were both compound heterozygous (PMID 41059452).
- **Prevalence:** fewer than 1 in 1,000,000 (Orphanet figure not retrieved); about 10 or more families have been published.
- **PHA carrier frequency:** often quoted as about 1 in 1,000–10,000. This figure was not retrieved this session.
- **Penetrance:** apparently complete for biallelic hypomorphic genotypes.
- **Expressivity:** variable, ranging from moderate fetal dysplasia (PMID 36712868) to mild disease.
- **Anticipation:** none reported.
- **Founder effects:** none established. p.Arg586His recurs in American (PMID 23824842) and Chinese (PMID 36712868; 38946370) cases.
- **Populations reported:** Turkish, Chinese, American and other families.
- **Sex ratio:** both sexes affected.

## 10. Diagnostics

- **Peripheral blood smear:** look for hyposegmented, bilobed "pince‑nez" neutrophils in the patient and in both parents. This is a cheap pointer to LBR (Colella 2012, PMID 22338047), and examining parents' smears has been suggested for prenatal work‑up (PMID 34467646). A normal smear does not exclude the disease (PMID 32827848).
- **Sterol analysis:** GC‑MS of plasma or cultured fibroblasts for cholesta‑8,14‑dien‑3β‑ol (PMID 23824842; 30448303; 12618959).
- **Imaging:**
  - Skeletal survey: rhizomelia, bowed femora, metaphyseal and vertebral changes.
  - Serial radiographs to document regression.
  - Prenatal ultrasound.
  - Greenberg dysplasia, by contrast, shows a "moth-eaten" pattern already at 13 weeks (PMID 18382993).
- **Genetic testing:** skeletal dysplasia gene panels that include LBR, or exome/genome sequencing, which is the most common route in the reports (PMID 25348816; 30448303; 32360156). Copy‑number analysis is worthwhile because a whole‑gene deletion has been reported (PMID 40355051).
- **Not relevant:** karyotype, FISH, mtDNA and repeat expansion testing.
- **Differential diagnosis:**
  - Greenberg/HEM dysplasia: lethal, with hydrops and moth‑eaten bones.
  - Dappled diaphyseal and Astley‑Kendall dysplasia, now considered allelic (PMID 32304187).
  - Metaphyseal chondrodysplasias: Schmid type (COL10A1) and CHH (RMRP); see PMID 36400164.
  - Anadysplasia (MMP13).
  - Spondylometaphyseal dysplasias, Kozlowski type (TRPV4) and COL2A1‑related.
  - Rhizomelic chondrodysplasia punctata.
  - Pseudo‑Pelger‑Huët anomaly: acquired, or due to TMEM147 variants.
- **Formal diagnostic criteria and newborn screening:** none exist.

## 11. Outcome and prognosis

- **Survival:** survival into adulthood is expected; the cases are non‑lethal by definition. No mortality data exist.
- **Morbidity:** short stature and limb bowing, which may need orthopaedic care. PHA has no effect on immunity in humans.
  - Mouse caveat: Lbr‑deficient mouse neutrophils "produced a deficient respiratory burst" (Gaines 2008, PMID 18550262). This has not been shown in humans.
- **Prognostic factors:**
  - Genotype: homozygous null or catalytically dead alleles in the reductase domain predict lethality, while hypomorphic alleles predict regression (PMID 30561119).
  - Residual sterol reductase activity measured in vitro may help predict severity (inferred).
- **Quality‑of‑life studies:** none.

## 12. Treatment

- **No disease‑specific therapy and no registered trials** (ClinicalTrials.gov was not searched this session).
- **Supportive care:**
  - Growth monitoring.
  - Orthopaedic follow‑up, including guided growth or osteotomy for persistent bowing (NCIT C15329 "Surgical Procedure").
  - Physiotherapy (NCIT C15300 "Physical Therapy").
  - Genetic counselling (NCIT C15418 "Genetic Counseling").
- **Experimental idea:** cholesterol supplementation. It is plausible from the mechanism but untested, and the ichthyosis‑mouse data question whether sterol deficit is the main driver.
- **Gene, cell and RNA therapies, and pharmacogenomics:** none applicable.

## 13. Prevention

- **Primary prevention:** carrier detection. Parents' blood smears showing PHA, plus cascade testing of LBR.
- **Reproductive options:** prenatal diagnosis or preimplantation genetic testing for known familial variants.
- **Recurrence risk:** 25% per pregnancy for carrier couples. Pseudodominant families carry a 50% risk (PMID 34467646; 41059452).
- **Secondary and tertiary prevention:** early orthopaedic surveillance.
- **Vaccines, prophylaxis, public‑health or behavioural measures:** not applicable.

## 14. Other species and natural disease

- **Rabbit (*Oryctolagus cuniculus*, NCBI Taxon 9986):** Hoffmann 2002 (PMID 12118250): "Homozygous offspring in an extinct rabbit lineage showed severe chondrodystrophy". This is a natural "Pelger" phenotype in rabbits.
- **Dogs:** Pelger anomaly is known in some breeds (OMIA not retrieved). In Australian Shepherds, "Linkage analysis excluded LBR" for a stillbirth phenotype (PMID 37347778).
- **Orthologues:** mouse *Lbr*; Drosophila LBR, which has a role in circadian PER foci (PMID 38185834). NCBI Gene IDs were not retrieved.
- **Zoonotic potential:** none.

## 15. Model organisms

| Model | Type | Recapitulation | PMID |
|---|---|---|---|
| Ichthyosis (*ic*, *ic^J*) mouse, Lbr null | spontaneous null alleles | PHA‑like neutrophils, "alopecia, variable expression of syndactyly and hydrocephalus". Lacks the human skeletal regression and has no tissue sterol defect. | 12490533; 17403717 |
| Lbr^GT/GT gene‑trap mouse | gene trap | "similar to ichthyosis mice"; neutrophil morphology affected but not function | 18621876 |
| Lbr N‑terminal 236 bp deletion (CRISPR) | knock‑in | "a superior model of human PHA"; no skeletal phenotype reported | 33846535 |
| Dhcr14 (Tm7sf2) knockout mouse | knockout | no disease; shows enzymatic redundancy | 17403717 |
| EML‑ic/ic and EPRO ic/ic myeloid lines | murine cell lines | hypolobulated neutrophils; rescue experiments | 22140257; 18550262; 18495328 |
| HL‑60 LBR knockdown | human cell line | ovoid nuclei (PHA) | 21327094 |
| C14 sterol reductase–deficient yeast (*erg24*) | complementation assay | tests the catalytic activity of variants | 21327084; 27336722 |

**Model limitations:** no animal model shows the hypomorphic, regressive skeletal phenotype. Mouse sterol redundancy through Tm7sf2 limits how well mouse sterol findings translate to humans.

**Resources:** MGI (*Lbr* alleles *ic*, *ic^J*, gene trap) and IMPC; not queried this session.

---

### Sources
- Web searches: [KEGG H02732](https://www.kegg.jp/entry/H02732), [MedGen 1648288](https://https.ncbi.nlm.nih.gov/medgen/1648288), [GARD 17782](https://rarediseases.info.nih.gov/assets/singles/17782.json), [PubMed 30561119](https://pubmed.ncbi.nlm.nih.gov/30561119/), [Front Pediatr 2025 (PMC12443853)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12443853/), [Karger Mol Syndromol](https://karger.com/msy/article/13/3/200/825172).
- Abstracts via NCBI E‑utilities efetch (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi): PMIDs 12118250, 12490533, 12618959, 14617022, 16784888, 17245605, 17403717, 18382993, 18495328, 18550262, 18621876, 19940018, 21326950, 21327084, 21327094, 22140257, 22338047, 23824842, 25348816, 27336722, 28858257, 30448303, 30561119, 32304187, 32360156, 32827848, 33846535, 34467646, 35650273, 35707587, 36400164, 36712868, 37347778, 38185834, 38946370, 40355051, 40980134, 41059452, 42622427.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 48 |
| On topic | 42 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19940018` *(abstract only)*: "a massive endoplasmic reticulum and perinuclear space expansion"
  - closest text in source: "Hence, LBR mutant variants and sterol reductases can severely interfere with the regular organization of the nuclear envelope and the endoplasmic reticulum."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018663` (2 mentions) - the report calls it "MONDO"; MONDO calls it **regressive spondylometaphyseal dysplasia**
- `HP:0011870` (1 mention) - the report calls it "term to verify"; HP calls it **Impaired arachidonic acid-induced platelet aggregation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000774` (1 mention) - the report calls it "Narrow thorax (fetal)"; HP calls it **Narrow chest**, and lists "Narrow thorax" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.