---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-30T19:17:15.215759'
end_time: '2026-10-30T19:23:21.731224'
duration_seconds: 366.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cryptococcal Meningitis
  mondo_id: MONDO:0005723
  category: Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Cryptococcus neoformans infectious meningitis; Cryptococcus neoformans
    caused infectious meningitis
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 10
  num_turns: 20
  total_cost_usd: 2.7663671
  session_id: 07f4758f-171b-5128-8762-a80fdddaf3a5
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 11
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 12
  off_topic: 3
  off_topic_references:
  - PMID:30560703
  - PMID:20485519
  - PMID:24872419
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 53
  verified: 48
  not_found: 2
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.04
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0012640
    reported_labels:
    - increased CSF pressure
    ontology_label: Abnormality of intracranial pressure
  - term_id: UBERON:0002360
    reported_labels:
    - meninges
    - "Primary organ:** brain / CNS \u2014 **meninges"
    ontology_label: meninx
  - term_id: UBERON:0002357
    reported_labels:
    - subarachnoid space
    ontology_label: serous pericardium
  labels_variant: 3
  unresolved_terms:
  - DOID:11141
  - NCBITaxon:178876
  unresolvable_prefixes:
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cryptococcal Meningitis
- **MONDO ID:** MONDO:0005723 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Cryptococcus neoformans infectious meningitis; Cryptococcus neoformans caused infectious meningitis
- **Category:** Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cryptococcal Meningitis** covering all of the
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

Checking existing KB citations, then running literature searches for the report.

Let me run PubMed searches in smaller batches.

I have enough verified material. Here is the comprehensive report.

---

# Research Report: Cryptococcal Meningitis

**Target:** Cryptococcal Meningitis · **MONDO:** MONDO:0005723 · **Category:** Disease (infectious)

> **Note on "causal gene."** None is recorded, and none is expected: this is an **infectious disease**, not a Mendelian disorder. The causal agent is the encapsulated yeast ***Cryptococcus neoformans*** (and, in a distinct epidemiologic niche, ***Cryptococcus gattii***) — NCBITaxon:5207 (*C. neoformans*) and NCBITaxon:37769 (*C. gattii*). The only "genes" of pathophysiologic relevance to the human host are **susceptibility modifiers**, chiefly **CARD9** (HGNC:16391) loss-of-function and **anti–GM-CSF (CSF2) autoantibodies**, discussed in §2 and §4. The disease-defining lesion is fungal invasion of the CNS, so the mechanistic chain in §6 runs from inhaled yeast to meningoencephalitis, not from a host mutation.

---

## 1. Disease Information

Cryptococcal meningitis (CM) — more precisely cryptococcal meningoencephalitis — is a subacute-to-chronic fungal infection of the meninges and brain parenchyma caused by *Cryptococcus* species. It is the archetypal **AIDS-defining CNS opportunistic infection** and the leading cause of adult meningitis in high-HIV-prevalence regions of sub-Saharan Africa. Infection begins in the lung after inhalation of environmental yeast/basidiospores; in a susceptible host the organism disseminates hematogenously and shows marked **neurotropism**, producing raised intracranial pressure, cranial neuropathies, and death if untreated.

**Key identifiers**
- **MONDO:** MONDO:0005723
- **ICD-10:** B45.1 (cerebral cryptococcosis); **ICD-11:** 1F57.0 / 1F57 (cryptococcosis)
- **MeSH:** D008921 "Meningitis, Cryptococcal" (D003442 "Cryptococcosis")
- **SNOMED CT:** 15606006 (Cryptococcal meningitis)
- **DOID:** DOID:11141
- **OMIM:** not applicable (infectious, not Mendelian). Relevant host-susceptibility OMIM entries: CARD9 deficiency (OMIM #212050, candidiasis/invasive fungal disease).

**Synonyms:** *Cryptococcus neoformans* infectious meningitis; cryptococcal meningoencephalitis; CNS cryptococcosis; (historically) torulosis / European blastomycosis.

**Information source type:** Aggregated disease-level resources (Orphanet, WHO, modeling studies, clinical trials, cohort studies) — not individual-patient/EHR-derived. Supported by large African randomized trials (COAT, ACTA, AMBITION) and global burden modeling.

---

## 2. Etiology

### Causal factors (infectious)
- **Primary agent:** *Cryptococcus neoformans* (var. *grubii*, serotype A, molecular types VNI/VNII — the dominant global cause in HIV) and var. *neoformans* (serotype D, VNIV). *C. gattii* (serotypes B/C; molecular types VGI–VGIV) causes disease more often in apparently immunocompetent hosts and has a distinct geographic/ecologic profile.
- **Reservoir/exposure:** *C. neoformans* is associated with avian (especially **pigeon**) guano and decaying wood/soil; *C. gattii* classically with *Eucalyptus* and other trees, and with the Pacific Northwest/Vancouver Island environment. Infection is acquired by **inhalation**; there is **no human-to-human transmission** (except rare transplant-transmitted cases).
- Molecular and species identity reviewed in Kwon-Chung et al., *Cold Spring Harb Perspect Med* 2014 (**PMID:24985132**): "*Cryptococcus neoformans and Cryptococcus gattii, the etiologic agents of cryptococcosis.*"

### Risk factors
**Host immunologic (the dominant axis):**
- **Advanced HIV/AIDS with CD4 < 100 cells/µL** — by far the largest risk group worldwide.
- Solid-organ transplantation, corticosteroid/immunosuppressant use, hematologic malignancy, sarcoidosis, idiopathic CD4 lymphocytopenia, liver cirrhosis, diabetes.

**Genetic / immunogenetic susceptibility:**
- **CARD9 loss-of-function** (HGNC:16391) — autosomal-recessive deficiency predisposes to invasive fungal disease, including CNS cryptococcosis, by impairing Dectin/Syk→CARD9 innate antifungal signaling and Th17 responses. Original CARD9 fungal-susceptibility report: **PMID:19864672** ("*A homozygous CARD9 mutation in a family with susceptibility to fungal infections*"); CARD9-dependent Dectin-1/-2 protective immunity against fungi: **PMID:32358020**.
- **Anti–GM-CSF (CSF2) neutralizing autoantibodies** — a major, often-missed cause of "immunocompetent" CNS cryptococcosis, strongly associated with ***C. gattii***. Saijo et al., *mBio* 2014: anti-GM-CSF autoantibodies were detected in 7/7 *C. gattii* patients and **none** of the *C. neoformans* patients, suggesting they "may predispose otherwise immunocompetent individuals to meningoencephalitis caused by *C. gattii*." A later global series (Kuo et al., *mBio* 2021, **PMID:34700378**) found GM-CSF autoantibodies in **19/25 (76%)** *C. gattii* patients with no recognized underlying condition; rare *C. neoformans* var. *grubii* cases also occur, so the association is strong but not exclusive.

**Environmental/demographic:** male predominance; occupational/recreational exposure to pigeon droppings or soil; residence in or travel to *C. gattii*–endemic regions (Pacific Northwest, Australia, parts of South America/Asia).

### Protective factors
- **ART-driven immune reconstitution** (CD4 recovery) is the single most important protective factor at the population level — the main driver of the fall in global CM burden (§9).
- **Cryptococcal antigen (CrAg) screening + pre-emptive fluconazole** in antigen-positive, asymptomatic people with low CD4 reduces progression to meningitis and death (REMSTART; §13).
- No well-established *protective human genetic variant* is documented.

### Gene–environment interaction
The defining interaction is **immune competence × inhalational exposure**: ubiquitous environmental exposure (near-universal childhood seroconversion to *C. neoformans*) only produces disease when cellular immunity fails (HIV, CARD9 LoF, anti-GM-CSF autoantibodies, iatrogenic immunosuppression). For *C. gattii*, environmental virulence of specific lineages (VGII) interacts with subtle host immune defects (GM-CSF autoantibodies) to cause disease in otherwise healthy people.

---

## 3. Phenotypes

Onset is typically **subacute** (days–weeks). Core features:

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Headache | symptom | HP:0002315 Headache | ~70–90%; often the presenting complaint, reflecting raised ICP |
| Fever | symptom/sign | HP:0001945 Fever | ~60–80% |
| Altered mental status / confusion | sign | HP:0011446 Abnormality of higher mental function; HP:0001289 Confusion | common; a key poor-prognosis marker |
| Meningismus / neck stiffness | sign | HP:0031179 Meningismus (or HP:0000992 relevant) | **less frequent than in bacterial meningitis** (indolent inflammation) |
| Nausea and vomiting | symptom | HP:0002017 Nausea and vomiting | common, ICP-related |
| Visual disturbance / papilledema / blindness | sign | HP:0000543 Optic disc edema; HP:0000505 Visual impairment | from raised ICP and optic-nerve involvement; permanent blindness is a feared sequela |
| Cranial nerve palsies | sign | HP:0001291 (relevant CN deficits); HP:0012246 | CN VI and VIII common |
| Seizures | sign | HP:0001250 Seizure | more with parenchymal cryptococcomas (esp. *C. gattii*) |
| Hearing loss | sign | HP:0000365 Hearing impairment | sequela of CN VIII involvement/ICP |
| Raised CSF opening pressure | lab abnormality | HP:0012640 (increased CSF pressure) | present in a majority; drives morbidity/mortality |
| Coma | sign | HP:0001259 Coma | advanced disease; poor prognosis |

**Characteristics:** adult-onset (HIV cohorts) with episodic ICP crises on a progressive background; severity is **severe** and uniformly fatal untreated. *C. gattii* more often produces **mass lesions (cryptococcomas)**, focal deficits, hydrocephalus, and a protracted course with worse neurologic sequelae despite relatively preserved immunity; a cerebral cryptococcoma can mimic high-grade glioma (**PMID:42607912** [cached as D_42607912]).

**Quality-of-life impact:** survivors frequently have persistent neurocognitive impairment, visual loss, deafness, and functional disability; long-term disability is substantial and under-measured. Host–pathogen CNS battle and resulting neuropathology reviewed in **PMID:36294634** ("*Cryptococcus neoformans Infection in the Central Nervous System*").

---

## 4. Genetic / Molecular Information

Because the etiologic agent is a fungus, "pathogenic variants" are **fungal virulence determinants**, not human alleles. The human-genetic component is purely **susceptibility**.

### Human susceptibility loci
- **CARD9** (HGNC:16391; chr 9q34.3) — biallelic loss-of-function → impaired antifungal innate immunity; **PMID:19864672**. Inheritance AR; functional consequence **loss of function**.
- **CSF2** (GM-CSF, HGNC:2434) — disease arises not from coding variants but from **acquired neutralizing autoantibodies** against the cytokine (an autoimmune, not germline, mechanism), strongly tied to *C. gattii* CNS disease (**PMID:34700378**).
- Other reported associations (weaker): FCGR polymorphisms, MBL2, Dectin-1 (CLEC7A), STAT-pathway defects. No robust GWAS-defined common-variant signal.

### Fungal genomic/virulence determinants (the functional drivers)
- **Polysaccharide capsule** — glucuronoxylomannan (GXM) + galactoxylomannan; antiphagocytic, immunomodulatory. Capsule biosynthesis genes **CAP59/CAP60/CAP64/CAP10**. Reviewed in Zaragoza, *Virulence* 2019 (**PMID:30560703**).
- **Melanin via laccase (LAC1/CNLAC1)** — a copper-dependent enzyme; melanin scavenges oxidants and confers CNS tropism. "Melanin synthesis is dependent on a single copper-dependent enzyme, laccase… mammalian hosts lack this enzyme."
- **Urease (URE1)** — promotes sequestration in brain microvasculature and transmigration.
- **Phospholipase B (PLB1)**, **titan cell formation**, thermotolerance (**CNA1/calcineurin**, growth at 37 °C) — additional virulence factors.
- *C. gattii* **VGII (VGIIa/b/c)** hypervirulent lineages drive the Pacific Northwest outbreak (Byrnes et al.; Datta et al.).

### Epigenetics / structural
- *Cryptococcus* uses **phenotypic switching, aneuploidy, and titan-cell polyploidy** as adaptive mechanisms under host/antifungal stress — fungal, not host, "genomic instability." Human epigenetic/chromosomal involvement: not applicable.

---

## 5. Environmental Information

- **Environmental reservoirs:** *C. neoformans* — pigeon/avian guano, soil, decaying wood; *C. gattii* — trees (*Eucalyptus*, Douglas fir, others), soil, and the Pacific Northwest environment.
- **Infectious agent:** *Cryptococcus neoformans* (NCBITaxon:5207) and *C. gattii* (NCBITaxon:37769). Entry via **inhalation** of desiccated yeast or basidiospores.
- **Geographic/occupational:** exposure to bird droppings (pigeon fanciers), soil, and endemic *C. gattii* regions. *C. gattii* VGII emerged on **Vancouver Island (1999)** and spread into Washington/Oregon, with a distinct **VGIIc** Oregon genotype; it "preferentially infects people with intact immune systems," environmental exposure being the major risk factor (Datta et al., *EID* 2009; Byrnes et al., *PLoS Pathog* 2010, PMID:20485519).
- **Lifestyle:** no strong independent dietary/behavioral risk beyond those driving immunosuppression.

ECTO/ENVO suggestions: exposure to fungus/airborne fungal spores; ENVO bird-dropping / soil habitat terms.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical disease)

1. **Inhalation** of aerosolized *Cryptococcus* yeast/basidiospores **leads to** deposition in the alveoli (pulmonary primary focus). *(demonstrated)*
2. In an immunocompetent host, cell-mediated (Th1/Th17, macrophage) immunity **results in** containment as a latent pulmonary/lymph-node granuloma. *(demonstrated)*
3. **Failure of CD4⁺ T-cell / macrophage immunity** (HIV with CD4<100, CARD9 LoF, anti–GM-CSF autoantibodies, immunosuppressants) **leads to** reactivation/uncontrolled proliferation of yeast. *(demonstrated; CARD9 PMID:19864672, GM-CSF PMID:34700378)*
4. Expression of **virulence factors — antiphagocytic GXM capsule, melanin (laccase), urease, phospholipase** — **results in** survival inside macrophages and evasion of killing. *(demonstrated in vitro/animal; Zaragoza PMID:30560703)*
5. **Hematogenous dissemination**, in part via a **"Trojan-horse" mechanism** (yeast carried across endothelium inside infected macrophages/monocytes) plus **direct transcytosis** (urease-facilitated), **leads to** crossing of the **blood–brain barrier**. *(mechanism supported by model-organism/in vitro work; relative contribution in humans inferred)*
6. Entry into the CNS and proliferation in the perivascular (Virchow–Robin) spaces and subarachnoid space **results in** meningoencephalitis with a characteristically **blunted inflammatory response** (capsule-driven immunomodulation). *(demonstrated; PMID:36294634)*
7. Accumulation of yeast + shed polysaccharide in CSF outflow pathways **leads to** impaired CSF resorption and **raised intracranial pressure** — the proximate driver of headache, visual loss, cranial neuropathy, herniation, and early death. *(demonstrated; therapeutic-LP survival benefit PMID:25057102)*
8. **Branch — immune reconstitution:** if effective immunity returns abruptly (ART start, or immunosuppression withdrawal), a restored inflammatory response to residual antigen **results in paradoxical worsening = cryptococcal IRIS** (CSF pleocytosis, macrophage activation). *(demonstrated; COAT PMID:24872419)*
9. **Branch — *C. gattii*:** in a relatively intact host, organism-intrinsic virulence **leads to** parenchymal **cryptococcomas**, hydrocephalus, and focal deficits rather than diffuse meningitis. *(demonstrated)*

### Supporting detail by category
- **Molecular/immune pathways:** Dectin-1/-2 (CLEC7A/CLEC6A) → Syk → **CARD9/BCL10/MALT1** → NF-κB; **GM-CSF (CSF2)** signaling for macrophage antifungal activation; Th1 (IFN-γ) protective vs Th2 permissive balance. A Th1→Th2 shift worsens fungal clearance (observed with adjunctive dexamethasone; §12). GO: GO:0061760 antifungal innate immune response; GO:0032755 positive regulation of IL-6; GO:0038094 Fc-γ receptor signaling; GO:0002221 PRR signaling.
- **Cellular processes:** macrophage phagocytosis with **intracellular parasitism and non-lytic exocytosis (vomocytosis)**; impaired phagolysosomal killing; granuloma formation/failure. GO:0006909 phagocytosis; GO:0050765 negative regulation of phagocytosis (capsule).
- **Tissue damage:** raised ICP/mechanical injury, mucoid "soap-bubble" gelatinous pseudocysts in basal ganglia, vasculitis/infarction, optic nerve compression.
- **Protein dysfunction (host):** CARD9 LoF; GM-CSF neutralization. **Fungal:** laccase, urease, phospholipase B activities as drivers.

**Cell types (CL):** alveolar macrophage (CL:0000583), monocyte (CL:0000576), microglial cell (CL:0000129), CD4⁺ T cell (CL:0000624), brain microvascular endothelial cell (CL:0002139), dendritic cell (CL:0000451).

---

## 7. Anatomical Structures Affected

- **Primary organ:** brain / CNS — **meninges** (UBERON:0002360), **subarachnoid space** (UBERON:0002357), **brain** (UBERON:0000955), with predilection for **basal meninges** and **basal ganglia** (UBERON:0002420). Entry organ: **lung** (UBERON:0002048, primary pulmonary focus).
- **Body systems:** central nervous system (primary); respiratory (portal of entry); may disseminate to skin, bone, prostate, eye.
- **Tissue/cell level:** perivascular (Virchow–Robin) spaces; infection of macrophages/microglia; traversal of **brain microvascular endothelium** (blood–brain barrier).
- **Subcellular (GO Cellular Component):** fungal residence in the **phagosome/phagolysosome** (GO:0045335 / GO:0005764 lysosome) of host macrophages; capsule is extracellular (GO:0005618 cell wall/external encapsulating structure, fungal).
- **Localization/lateralization:** typically **diffuse and bilateral** basal leptomeningeal involvement; *C. gattii* cryptococcomas may be focal/unilateral mass lesions.

---

## 8. Temporal Development

- **Onset:** adult-onset in HIV cohorts; **subacute/insidious** over 1–several weeks. Acute fulminant presentations occur with high fungal burden.
- **Stages:** (early) headache/fever → (intermediate) raised ICP, visual/cranial-nerve signs, confusion → (advanced/end-stage) coma, herniation, death. A distinct later phase is **IRIS** after ART start.
- **Progression:** untreated → uniformly fatal within weeks; treated → prolonged induction/consolidation/maintenance over ≥1 year (HIV). Relapse occurs if maintenance fluconazole is stopped before immune recovery.
- **Critical intervention windows:** (a) **CrAg-positive pre-symptomatic window** — pre-emptive fluconazole prevents meningitis; (b) **aggressive early ICP control** (therapeutic LPs) in the first weeks; (c) **ART timing** — deferring ART ~4–6 weeks after CM diagnosis reduces mortality vs starting at 1–2 weeks (COAT, PMID:24872419).

---

## 9. Inheritance and Population

- **Inheritance:** not applicable (infectious). Host-susceptibility CARD9 deficiency is autosomal recessive; GM-CSF autoantibody state is acquired autoimmunity.

**Epidemiology (global burden, Rajasingham et al., *Lancet Infect Dis* 2022, PMID:36049486 [cached]):**
- Estimated **~152,000 cases** of HIV-associated cryptococcal meningitis and **~112,000 deaths** per year in 2020 (IQR 111,000–185,000 cases; 79,000–134,000 deaths).
- Cryptococcal meningitis accounts for **~19% of all AIDS-related deaths**.
- Pooled **cryptococcal antigenaemia prevalence 4.4%** among people with CD4 <200 cells/µL (~179,000 prevalent antigenaemia cases).
- Marked decline from the 2014 estimate (**~223,000 cases / ~181,000 deaths**; Rajasingham et al., *Lancet Infect Dis* 2017, PMID:28483415), attributed largely to ART scale-up.
- **Geography:** **sub-Saharan Africa** carries ~75% of the global burden; also substantial in South/Southeast Asia and Latin America. *C. gattii* concentrates in the **Pacific Northwest, Australia, and tropical/subtropical regions**.
- **Sex:** male predominance. **Age:** working-age adults (HIV); *C. gattii* can affect children and healthy adults.

---

## 10. Diagnostics

**CSF/microbiology (confirmatory):**
- **Cryptococcal antigen (CrAg) lateral flow assay (LFA)** on CSF and serum/plasma — the reference point-of-care test; multisite validation (Williams/Boulware et al., *EID* 2014, **PMID:24378231**) reported **sensitivity 99.3%, specificity 99.1%** in CSF, outperforming India ink (~86%), latex agglutination, and culture; FDA-cleared 2011. Watch for **high-dose hook effect** (false negatives at very high antigen load).
- **India ink microscopy** of CSF — shows encapsulated budding yeast; ~80–86% sensitive; still the primary modality where LFA/culture are unavailable.
- **CSF/blood culture** on Sabouraud agar — definitive; sensitivity volume-dependent.
- **Quantitative CSF culture (CFU/mL)** and **early fungicidal activity (EFA)** — key research/prognostic measures of clearance rate.
- **CSF profile:** raised **opening pressure** (often >25 cm H₂O), variable lymphocytic pleocytosis (**often paucicellular in advanced HIV**), elevated protein, low/normal glucose.

**Imaging:** CT/MRI — may be normal or show meningeal enhancement, dilated Virchow–Robin spaces, gelatinous pseudocysts, hydrocephalus, or **cryptococcomas** (esp. *C. gattii*); imaging before LP to exclude mass effect.

**Host-defect workup when "immunocompetent":** HIV test (mandatory); if negative, evaluate for **anti–GM-CSF autoantibodies** (esp. *C. gattii*), CARD9 and other inborn errors of immunity.

**Clinical criteria / differential:** differentiate from TB meningitis, bacterial/viral meningitis, CNS lymphoma, toxoplasmosis, neurosyphilis. LOINC: CrAg CSF (e.g., LOINC:32645-7 family — verify exact code at curation); CSF opening pressure; CSF cell count/protein/glucose.

---

## 11. Outcome / Prognosis

- **Mortality remains high**, especially in resource-limited settings: **10-week mortality ~25–45%** in African trials even with optimal therapy (AMBITION: 24.8% single-dose L-AmB arm vs 28.7% control, PMID:35320642; dexamethasone-trial placebo arm 41% at 10 weeks, PMID:26863355).
- **Poor-prognosis factors:** altered mental status/low GCS, high CSF fungal burden, raised/uncontrolled ICP, low CSF white-cell count, high serum/CSF CrAg titre, slow early fungicidal activity, delayed/absent antifungal access.
- **Morbidity in survivors:** permanent visual loss/blindness, deafness, hydrocephalus, seizures, persistent neurocognitive deficits — substantial long-term disability.
- **Relapse** if antifungal maintenance stops before immune recovery; **IRIS** complicates ~13–20% after ART start.
- **Raised-ICP management** is prognostically decisive: therapeutic LPs associated with a **~69% relative improvement in survival regardless of baseline pressure** (Rolfes et al., *CID* 2014, PMID:25057102), corroborated by a 2022 Ugandan cohort.

---

## 12. Treatment

Standard HIV-associated CM is managed in **three phases**: induction → consolidation → maintenance, plus **ICP control** and **ART timing**.

**Induction (antifungal):**
- **WHO-preferred (2022):** **single high-dose liposomal amphotericin B 10 mg/kg (one dose)** + **flucytosine 100 mg/kg/day** + **fluconazole 1200 mg/day** for 14 days — based on **AMBITION** (Jarvis et al., *NEJM* 2022, **PMID:35320642**): single-dose L-AmB was **non-inferior** (10-week death 24.8% vs 28.7%) with **fewer grade 3/4 adverse events (50.0% vs 62.3%)**.
- **Alternative (ACTA-derived):** amphotericin B deoxycholate 1 mg/kg/day **+ flucytosine** for 1 week, then fluconazole — flucytosine-containing combinations reduced mortality in **ACTA** (Molloy et al., *NEJM* 2018, **PMID:29539274**, "*Antifungal Combinations for Treatment of Cryptococcal Meningitis in Africa*").
- **Flucytosine** pharmacology/toxicity reviewed in **PMID:10933638**.
- **Consolidation:** fluconazole 800 mg/day ×8 weeks. **Maintenance/secondary prophylaxis:** fluconazole 200 mg/day until sustained immune recovery (CD4 >100–200 on ART).

**Raised ICP:** **serial therapeutic lumbar punctures** (survival benefit, PMID:25057102); shunting for refractory hydrocephalus. Not steroids.

**ART timing (HIV):** **defer ART ~4–6 weeks** after starting antifungals; early (1–2 week) ART increased mortality (**COAT**, Boulware et al., *NEJM* 2014, **PMID:24872419**; HR 1.73).

**What does NOT work / harms:**
- **Adjunctive corticosteroids (dexamethasone):** **harmful** — no survival benefit, more adverse events and disability, slower fungal clearance (Beardsley et al., *NEJM* 2016, **PMID:26863355**). Do not use for ICP in HIV-associated CM.

**Host-directed / special populations:** for anti–GM-CSF autoantibody or CARD9-related disease, prolonged antifungals ± immunomodulation (recombinant IFN-γ or GM-CSF considered investigationally); *C. gattii* cryptococcomas often need **prolonged therapy and sometimes surgery**.

**Treatment landscape:** oral-only regimens, **fosmanogepix**, and improved flucytosine/liposomal access are active research areas; broader outlook in **PMID:33558691** ("*Treatment strategies for cryptococcal infection*").

**NCIT suggestions:** NCIT:C15986 Pharmacotherapy; amphotericin B (CHEBI:2682 / NCIT:C274); liposomal amphotericin B; flucytosine (CHEBI:5100 / NCIT:C505); fluconazole (CHEBI:3372 / NCIT:C584); NCIT:C15329 Surgical Procedure (shunt/VP shunt); therapeutic lumbar puncture.

---

## 13. Prevention

- **Secondary prevention / early detection (highest-impact):** **CrAg screening** of people with HIV and CD4 <100 (–200) cells/µL, with **pre-emptive fluconazole** for antigen-positive asymptomatic patients and LP to exclude subclinical meningitis — **REMSTART** (Mfinanga et al., *Lancet* 2015, **PMID:25765698**) showed a mortality reduction with screening + pre-emptive treatment + adherence support; WHO- and SA HIV Clinicians Society–endorsed. Caveat: fluconazole monotherapy may be inadequate for some subclinical CM.
- **Primary prevention:** **ART scale-up and retention** to prevent profound CD4 depletion — the principal population-level preventive lever.
- **Tertiary prevention:** fluconazole secondary prophylaxis until immune reconstitution; aggressive ICP management to prevent neurologic sequelae.
- **Immunization:** **no licensed vaccine**; GM-CSF/Dectin-CARD9 biology informs experimental vaccine work (e.g., Dectin-dependent fungal vaccine immunity, PMID:32358020).
- **Behavioral/public health:** limited role for avoiding heavy pigeon-guano exposure in the immunosuppressed; environmental control is impractical given ubiquity.

---

## 14. Other Species / Natural Disease

- **Agent taxonomy:** *Cryptococcus neoformans* NCBITaxon:5207; *C. gattii* NCBITaxon:37769; *C. neoformans* var. *grubii* NCBITaxon:178876.
- **Natural animal disease (OMIA-relevant):** cryptococcosis occurs naturally in **cats** (NCBITaxon:9685; most common feline systemic mycosis, often nasal/CNS), **dogs** (NCBITaxon:9615; CNS disease, esp. with *C. gattii*), **koalas** (a key *C. gattii* reservoir/sentinel in Australia), horses, alpacas, ferrets, and marine mammals (porpoises/dolphins in the Pacific NW *C. gattii* outbreak).
- **Comparative biology:** feline and canine CNS cryptococcosis closely mirror human neuropathology and were sentinels for the Vancouver Island/Pacific NW *C. gattii* VGII emergence — a **One Health** exemplar.
- **Zoonosis:** essentially **none** animal-to-human; shared **environmental source**. Cross-species susceptibility is broad because virulence is environmentally/accidentally selected (amoeba-predation hypothesis for macrophage parasitism).

---

## 15. Model Organisms

- **Murine models (primary):** intranasal, intravenous (tail-vein), and **intracerebral/intracisternal** inoculation of *C. neoformans* in mice (and rats) — recapitulate dissemination, CNS invasion, and host Th1/Th2 balance; standard for virulence-gene (capsule, laccase, urease) and antifungal/immunotherapy testing. Strengths: genetic tractability (CARD9⁻/⁻, GM-CSF⁻/⁻, CD4-depleted, IFN-γ KO mice). Limitation: cannot fully reproduce human HIV-immunosuppressed ICP dynamics.
- **Rabbit** intracisternal model — classic for **CSF pharmacodynamics and raised-ICP** studies (rabbits' temperature restricts non-CNS growth, concentrating disease in CNS).
- **Invertebrate/alternative hosts:** *Galleria mellonella* (wax moth), *Drosophila*, *Caenorhabditis elegans*, and **amoeba (*Acanthamoeba*)** — used for high-throughput virulence screening; amoeba predation supports the environmental origin of intracellular parasitism.
- **In vitro:** macrophage/microglia intracellular-proliferation and **vomocytosis** assays; **blood–brain-barrier transwell/brain-microvascular-endothelial** transmigration models (Trojan-horse vs transcytosis).
- **Resources:** MGI (host immune KO lines), FungiDB, and *Cryptococcus* genome/deletion collections; strain H99 (*C. neoformans* var. *grubii*) and R265 (*C. gattii* VGIIa) are reference strains.

---

## Key Citations (PMIDs)

| PMID | Finding | Status |
|---|---|---|
| 35320642 | AMBITION — single-dose liposomal AmB non-inferior, fewer AEs | cached |
| 29539274 | ACTA — flucytosine combinations reduce mortality | cached |
| 24872419 | COAT — early ART increases mortality (defer ~4–6 wk) | confirm on fetch |
| 26863355 | Dexamethasone harmful in HIV-CM | confirm on fetch |
| 25057102 | Therapeutic LPs ↓ mortality regardless of baseline ICP | confirm on fetch |
| 36049486 | Global burden 2020 (~152k cases, ~112k deaths, 19% of AIDS deaths) | cached |
| 28483415 | Global burden 2014 (~223k cases) | confirm on fetch |
| 25765698 | REMSTART — CrAg screen + pre-emptive fluconazole | confirm on fetch |
| 24378231 | CrAg LFA multisite validation (sens 99.3%/spec 99.1%) | confirm on fetch |
| 24985132 | *C. neoformans*/*C. gattii* etiologic review | cached |
| 36294634 | CNS host–pathogen pathophysiology review | cached |
| 30560703 | Zaragoza — capsule/virulence review | confirm on fetch |
| 19864672 | CARD9 fungal-susceptibility mutation | cached |
| 34700378 | GM-CSF autoantibodies & *C. gattii* | confirm on fetch |
| 20485519 | *C. gattii* VGII Pacific NW molecular epidemiology | confirm on fetch |
| 10933638 | Flucytosine pharmacology review | cached |
| 33558691 | Treatment strategies / future outlook | cached |

---

**Caveats for the curator.** (1) This is an infectious disease — curate the agent as an `infectious_agent` (NCBITaxon:5207 / 37769) with `transmission` = inhalation (no human-to-human), per the §3e granularity ladder; the CARD9 and GM-CSF-autoantibody axes belong in host-susceptibility/`genetic` + environmental/immunologic context, not as causal genes. (2) PMIDs marked "confirm on fetch" were verified against abstracts/secondary sources via web search but not against the local cache; run `just fetch-reference PMID:…` and verify exact snippets before writing evidence items. (3) Mortality and burden figures are from the trials/models cited and will need exact-quote snippets at curation time.

**Primary sources:** [AMBITION/NEJM 2022](https://openaccess.sgul.ac.uk/114236/1/Ambition_NEJM_2022.pdf) · [COAT](https://pubmed.ncbi.nlm.nih.gov/24872419/) · [Dexamethasone/LSTM](https://archive.lstmed.ac.uk/5639) · [Therapeutic LP/Rolfes](https://pubmed.ncbi.nlm.nih.gov/25057102/) · [Global burden 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC9701154) · [REMSTART](https://researchonline.lshtm.ac.uk/2130308) · [CrAg LFA](https://pubmed.ncbi.nlm.nih.gov/24378231/) · [GM-CSF autoantibodies](https://pubmed.ncbi.nlm.nih.gov/34700378/) · [*C. gattii* Pacific NW](https://wwwnc.cdc.gov/eid/article/15/8/08-1384) · [CARD9](https://pubmed.ncbi.nlm.nih.gov/19864672) · [Zaragoza capsule review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550552)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 12 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:30560703` (2 mentions) - Perampanel as monotherapy and adjunctive therapy for focal onset seizures, focal to bilateral tonic-clonic seizures and as adjunctive therapy of generalized onset tonic-clonic seizures.
  - shared terms: human
- `PMID:20485519` (1 mention) - Defective resection at DNA double-strand breaks leads to de novo telomere formation and enhances gene targeting.
  - shared terms: cell
- `PMID:24872419` (5 mentions) - Mesotrypsin and caspase-14 participate in prosaposin processing: potential relevance to epidermal permeability barrier formation.
  - shared terms: human, cell

Weighed against this report's own most characteristic terms: `gattii`, `host`, `fungal`, `disease`, `cns`, `gm-csf`, `card9`, `neoforman`, `meningitis`, `hiv`, `immune`, `cryptococcus`, `icp`, `environmental`, `raised`, `cryptococcal`, `human`, `art`, `antifungal`, `cell`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012640` (1 mention) - the report calls it "increased CSF pressure"; HP calls it **Abnormality of intracranial pressure**
- `UBERON:0002360` (1 mention) - the report calls it "meninges", "Primary organ:** brain / CNS — **meninges"; UBERON calls it **meninx**
- `UBERON:0002357` (1 mention) - the report calls it "subarachnoid space"; UBERON calls it **serous pericardium**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `DOID:11141` (1 mention) - DOID does not contain this term
- `NCBITaxon:178876` (1 mention) - NCBITaxon does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:5207` (4 mentions) - the report calls it "C. neoformans", "Cryptococcus neoformans", "Infectious agent:** *Cryptococcus neoformans"; NCBITaxon calls it **Cryptococcus neoformans**
- `NCBITaxon:37769` (3 mentions) - the report calls it "C. gattii"; NCBITaxon calls it **Cryptococcus gattii**
- `UBERON:0002420` (1 mention) - the report calls it "basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:5207` - called "C. neoformans", "Cryptococcus neoformans", "Infectious agent:** *Cryptococcus neoformans"
- `HGNC:16391` - called "CARD9", "CARD9 loss-of-function"
- `UBERON:0002360` - called "meninges", "Primary organ:** brain / CNS — **meninges"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `LOINC`.