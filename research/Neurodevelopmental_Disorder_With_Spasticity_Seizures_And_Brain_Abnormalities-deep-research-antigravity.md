---
provider: antigravity
model: gemini-4-carbon-medium
cached: false
start_time: '2026-11-20T10:19:57.022890'
end_time: '2026-11-20T10:39:59.065985'
duration_seconds: 1202.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Spasticity, Seizures, And Brain Abnormalities
  mondo_id: MONDO:0859275
  category: Mendelian
  causal_genes: NSRP1
  omim_id: OMIM:620001
  synonyms: NEDSSBA
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agy_executable: agy
    skip_permissions: false
    disable_slash_commands: true
    add_dirs: []
    timeout: 1800
    health_probe_timeout: 30
    min_report_chars: 200
    extra_args: []
run_metadata:
  model: gemini-4-carbon-medium
  status: SUCCESS
  num_turns: 1
  duration_seconds: 1198.138689775
  conversation_id: 4d3ce879-84c9-402e-8655-7fe6ec34f00c
  usage:
    input_tokens: 127142
    output_tokens: 36202
    thinking_tokens: 7748
    cache_read_tokens: 650292
    total_tokens: 163344
  tool_calls: 72
  retrieval_calls: 72
citation_count: 15
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - PMID:22342930
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 75
  verified: 65
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 10
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - Gene
  - MGI
  service_unreachable: 1
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Spasticity, Seizures, And Brain Abnormalities
- **MONDO ID:** MONDO:0859275 (if available)
- **Causal gene(s):** NSRP1
- **OMIM:** OMIM:620001
- **Synonyms:** NEDSSBA
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Spasticity, Seizures, And Brain Abnormalities** covering all of the
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

# Comprehensive Research Report: Neurodevelopmental Disorder With Spasticity, Seizures, And Brain Abnormalities (NEDSSBA; MONDO:0859275)

---

## 1. Disease Information

### Disease Overview
**Neurodevelopmental Disorder With Spasticity, Seizures, And Brain Abnormalities** (**NEDSSBA**; `MONDO:0859275`, `OMIM:620001`) is an ultra-rare, autosomal recessive Mendelian disorder caused by biallelic pathogenic loss-of-function or hypomorphic variants in the ***NSRP1*** gene (*Nuclear Speckle Splicing Regulatory Protein 1*, `HGNC:25305`, `OMIM:616173`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). *NSRP1* (formerly designated *CCDC55* or *NSrp70*) encodes an RNA-binding splicing factor localized to nuclear speckles that counteracts serine/arginine-rich (SR) proteins such as SRSF1 and SRSF2 to regulate alternative pre-mRNA splicing ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/)).

First delineated as a human Mendelian entity by Calame et al. in 2021 in six affected individuals from three unrelated consanguineous families ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)), NEDSSBA classically manifests in early infancy as a severe developmental and epileptic encephalopathy (`HP:0001263`, `HP:0001250`) accompanied by axial hypotonia (`HP:0008936`), appendicular spasticity mimicking spastic cerebral palsy (`HP:0001257`, `HP:0002510`), variable microcephaly (`HP:0000252`), and structural neuroimaging malformations including simplified cortical gyral patterns (`HP:0009879`), incomplete opercularization, corpus callosum hypoplasia/dysgenesis (`HP:0002079`), thin brainstem (`HP:0002365`), and cerebellar vermis hypoplasia (`HP:0001320`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Recent literature from 2024 expanded the clinical continuum: Neuens et al. (2024) reported a 14-year-old female with compound heterozygous *NSRP1* variants—including a missense variant (`p.Val532Glu`) within the C-terminal nuclear localization signal (NLS)—who exhibited intellectual disability (`HP:0001249`), motor/language delay, and gait ataxia (`HP:0002066`), yet achieved unassisted ambulation and conversational speech in short sentences ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

> **Direct Abstract Support:**
> *"We identified six patients from three unrelated families with homozygous loss-of-function variants in NSRP1. Clinical features include developmental delay, epilepsy, variable microcephaly (Z-scores −0.95 to −5.60), hypotonia, and spastic cerebral palsy. Brain abnormalities included simplified gyral pattern, under-opercularization, and/or vermian hypoplasia."* — Calame et al., *Genetics in Medicine*, 2021 ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) `[Human clinical]`

### Key Identifiers
- **MONDO Disease Ontology:** [`MONDO:0859275`](https://monarchinitiative.org/MONDO:0859275)
- **OMIM (Phenotype):** [`OMIM:620001`](https://omim.org/entry/620001)
- **OMIM (Causal Gene — *NSRP1*):** [`OMIM:616173`](https://omim.org/entry/616173)
- **HGNC (Causal Gene):** [`HGNC:25305`](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25305) (`NSRP1`)
- **NCBI Gene ID:** [`84081`](https://www.ncbi.nlm.nih.gov/gene/84081)
- **Ensembl Gene ID:** `ENSG00000126653`
- **UniProtKB:** [`Q9H0G5`](https://www.uniprot.org/uniprotkb/Q9H0G5)
- **Orphanet (`ORPHA`), ICD-10, ICD-11, and MeSH:** Dedicated disease-specific identifiers for NEDSSBA (`OMIM:620001` / `MONDO:0859275`) were not retrieved in public ontology cross-references during this session, reflecting its recent (2021–2024) molecular delineation `[Database / computational]`. Clinically, affected individuals have historically received broad phenotypic classifications such as spastic cerebral palsy or developmental and epileptic encephalopathy prior to genomic sequencing ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Common Synonyms and Alternative Names
- **NEDSSBA** (official OMIM acronym) ([OMIM:620001](https://omim.org/entry/620001))
- **Neurodevelopmental disorder with spasticity, seizures, and brain abnormalities** ([OMIM:620001](https://omim.org/entry/620001))
- ***NSRP1*-related neurodevelopmental disorder** / ***NSRP1*-associated neurodevelopmental disorder** ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/))

### Provenance of Disease Evidence
Current knowledge of NEDSSBA is derived directly from **individual patient-level genomic and clinical characterizations** across research and diagnostic cohorts (7 molecularly confirmed patients across 4 unrelated families in peer-reviewed primary literature, plus 1 ungenotyped similarly affected deceased sibling), supplemented by aggregated rare-disease curations (`OMIM:620001`, `MONDO:0859275`, ClinVar) and mechanistic studies in mammalian cell lines and animal models ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/); [PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)). Large-scale electronic health record (EHR) or population registry datasets do not yet exist for this ultra-rare disorder.

---

## 2. Etiology

### Disease Causal Factors
NEDSSBA has a strictly **monogenic genetic etiology** caused by biallelic (homozygous or compound heterozygous) loss-of-function or partial loss-of-function (hypomorphic) variants in *NSRP1* on chromosome 17q11.2 ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`. Mechanistically, pathogenic variants either:
1. Introduce premature termination codons in early exons (`c.52C>T`, `p.Gln18Ter`) or disrupt canonical splice donor sites (`c.114+2T>G`), depleting functional transcript/protein levels ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)); or
2. Truncate the final exon (`c.1359_1362delAAAG`, `p.Glu455AlafsTer20`; `c.1272dupG`, `p.Lys425GlufsTer5`) or substitute conserved residues (`c.1595T>A`, `p.Val532Glu`) within the C-terminal nuclear localization signal (NLS, residues 531–540), preventing nuclear import into nuclear speckles (`GO:0016607`), causing cytosolic mislocalization (`GO:0005829`), and abolishing or attenuating alternative pre-mRNA splicing regulation (`GO:0000380`) during neurodevelopment ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

No infectious, teratogenic, toxic, or autoimmune causes of NEDSSBA have been identified.

### Risk Factors
- **Genetic Risk Factors:**
  - **Parental Heterozygous Carrier Status:** Inheritance of one pathogenic *NSRP1* allele from each biological parent confers a 25% recurrence risk per pregnancy under autosomal recessive Mendelian transmission ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`.
  - **Susceptibility Loci / Modifier Genes:** None identified to date for NEDSSBA `[Human clinical]`.
- **Demographic / Familial Risk Factors:**
  - **Parental Consanguinity and Family History:** Parental consanguinity substantially increases the probability of autozygosity (regions of homozygosity) for ultra-rare private loss-of-function alleles in *NSRP1*; all three families in the initial discovery cohort (originating from Egypt, Iran, and Pakistan) harbored homozygous variants ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). However, compound heterozygosity also occurs in non-consanguineous settings, as demonstrated in the 2024 Belgian report ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`.
- **Environmental Risk Factors:** No environmental toxins, lifestyle exposures, occupational hazards, or maternal age effects are known to cause or increase the risk of *NSRP1* pathogenic variants `[Human clinical]`.

### Protective Factors
- **Genetic Protective Factors:** Retaining at least one wild-type *NSRP1* allele completely protects against clinical disease, as heterozygous carrier parents are clinically unaffected ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) `[Human clinical]`. Among biallelic individuals, hypomorphic missense alleles that retain partial nuclear function (`p.Val532Glu`) or early nonsense variants potentially permitting leaky translation re-initiation/residual activity (`p.Gln18Ter`) are associated with attenuated clinical severity compared with C-terminal frameshift alleles that abolish the NLS ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). No external genetic modifier alleles have been reported.
- **Environmental Protective Factors:** None known to prevent disease manifestation in biallelic *NSRP1* variant homozygotes or compound heterozygotes.

### Gene-Environment Interactions
No gene-environment ($G \times E$) interactions involving *NSRP1* have been established in NEDSSBA in PubMed, PheGenI, or Comparative Toxicogenomics Database (CTD) records retrieved during this session.

---

## 3. Phenotypes

Phenotypic characterization is synthesized from the 7 molecularly confirmed patients reported across the two peer-reviewed clinical studies: 6 severe homozygous patients from 3 families in Calame et al. (2021) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) and 1 milder compound heterozygous patient in Neuens et al. (2024) ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

> **Direct Abstract Support:**
> *"Bi-allelic loss-of-function variants in NSRP1 have recently been identified in patients suffering from a severe neurodevelopmental disorder, presenting with neurodevelopmental delay, epilepsy, microcephaly, hypotonia, and spastic cerebral palsy. Described patients acquired neither independent walking nor speech and often showed anomalies on cerebral MRI. Here we describe the case of a 14-year-old girl with motor and language delay as well as intellectual disability, who presents an ataxic gait but walks without assistance and speaks in short sentences."* — Neuens et al., *American Journal of Medical Genetics Part A*, 2024 ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`

### Summary Table of Phenotypes and HPO Annotations

| Phenotype | HPO Term | Phenotype Type | Onset | Severity | Progression | Reported Frequency |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Global developmental delay** | `HP:0001263` | Clinical sign / Neurodevelopmental | Neonatal to early infancy | Moderate to profound (variable by genotype) | Static to slowly evolving | **100% (7/7)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Intellectual disability** | `HP:0001249` | Cognitive / Behavioral manifestation | Childhood (assessable after infancy) | Mild-moderate (1/7) to severe/profound (6/7) | Static lifelong | **100% of evaluable older children** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Seizure (Epilepsy)** | `HP:0001250` | Clinical symptom / Neurological sign | Early infancy | Variable; drug-resistant in 3/6 severe cases | Episodic / chronic refractory in ~50% of classic cohort | **86% (6/7 overall; 6/6 in classic cohort, 0/1 in mild case)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Axial hypotonia / Hypotonia** | `HP:0008936` / `HP:0001252` | Clinical sign / Physical manifestation | Neonatal / Early infancy | Severe in classic cohort | Persistent truncal hypotonia coexisting with limb hypertonia | **86% (6/6 in classic cohort)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Spasticity / Spastic tetraplegia** | `HP:0001257` / `HP:0002510` | Clinical sign / Motor manifestation | Infancy | Severe in classic cohort (spastic cerebral palsy mimic) | Chronic; evolves from neonatal hypotonia to limb spasticity | **86% (6/6 in classic cohort; absent in mild case)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Inability to walk** | `HP:0002540` | Functional motor sign | Infancy / Childhood | Profound | Non-ambulatory lifelong in severe cases | **86% (6/7; 6/6 in classic cohort)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Gait ataxia** | `HP:0002066` | Clinical sign / Motor coordination | Childhood | Mild to moderate | Stable | **14% (1/7; observed in ambulatory mild patient)** ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Absent speech** | `HP:0001344` | Neurodevelopmental / Communication sign | Childhood | Profound in classic cases (short sentences in mild case) | Static | **86% (6/7; 6/6 in classic cohort)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) |
| **Microcephaly** | `HP:0000252` | Physical manifestation | Congenital to postnatal infancy | Variable ($Z$-scores $-0.95$ to $-5.60$ in classic cohort) | Static or progressive postnatal head growth deceleration | **83% in classic cohort (5/6)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **EEG abnormality** | `HP:0002353` | Electrophysiological abnormality | Infancy | Moderate to severe (background slowing, epileptiform discharges) | Persistent in epileptic patients | **83% of tested classic cohort (5/6)** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Simplified gyral pattern** | `HP:0009879` | Neuroimaging / Structural sign | Congenital / Infantile MRI | Mild to moderate | Appears most pronounced in early infancy; sulcation partially matures with age | **Frequent in infant MRI scans in classic cohort** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Incomplete / under-opercularization** | *(Descriptive neuroimaging sign; no dedicated HPO ID)* | Neuroimaging / Structural sign | Congenital / Infantile MRI | Mild to moderate | Most conspicuous in infant scans | **Frequent in classic cohort** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Cerebellar vermis hypoplasia / Cerebellar atrophy** | `HP:0001320` / `HP:0001272` | Neuroimaging / Structural sign | Congenital / Infantile MRI | Mild to moderate | Non-progressive hypoplasia or mild atrophy | **Frequent in classic cohort** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Hypoplasia / Aplasia of the corpus callosum** | `HP:0002079` / `HP:0007370` | Neuroimaging / Structural sign | Congenital / Infantile MRI | Mild to moderate thinning/dysgenesis | Static congenital malformation | **Observed in classic cohort subset** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Hypoplasia of the brainstem** | `HP:0002365` | Neuroimaging / Structural sign | Congenital / Infantile MRI | Mild to moderate thinning | Static | **Observed in classic cohort subset** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |
| **Feeding difficulties / Dysphagia** | `HP:0011968` / `HP:0002015` | Clinical symptom / Bulbar dysfunction | Neonatal / Infancy | Moderate to severe | Chronic | **Observed in severe classic cases** ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) |

### Routine Laboratory Abnormalities
No disease-specific blood, urine, or cerebrospinal fluid biochemical abnormalities (LOINC-indexed metabolic markers) have been linked to NEDSSBA; routine metabolic screenings performed during diagnostic workups are characteristically unremarkable, prompting genomic sequencing ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Quality of Life (QoL) Impact
No formal standardized patient-reported or caregiver-reported quality-of-life instruments (such as EQ-5D, SF-36, or WHOQOL) have been published specifically for NEDSSBA cohorts `[Human clinical]`. However, clinical functional descriptions demonstrate profound per-phenotype impacts on daily living:
- **Motor and Mobility (`HP:0001257`, `HP:0008936`, `HP:0002540`):** In the classic biallelic loss-of-function phenotype (6/6 patients in Calame et al.), combined axial hypotonia and appendicular spasticity prevent independent sitting or walking, necessitating full-time caregiver dependence for transfers, positioning, and activities of daily living ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Even in the attenuated presentation (`p.Val532Glu`), gait ataxia (`HP:0002066`) impairs fine balance and motor coordination ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Communication and Cognition (`HP:0001263`, `HP:0001249`, `HP:0001344`):** Complete absence of verbal speech in classic patients severely limits autonomous expression, whereas milder cases experience educational and social limitations requiring specialized schooling ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Refractory Seizures (`HP:0001250`) and Dysphagia (`HP:0002015`):** Drug-resistant epilepsy (3/6 patients in Calame et al.) drives recurrent hospitalizations, polypharmacy side effects, and heightened caregiver burden, while dysphagia impairs safe oral nutrition and increases aspiration risk ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

---

## 4. Genetic/Molecular Information

### Causal Gene
- **Gene Symbol:** *NSRP1* (*Nuclear speckle splicing regulatory protein 1*) ([HGNC:25305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25305))
- **Previous Symbols / Aliases:** *CCDC55* (*Coiled-coil domain-containing protein 55*), *NSrp70*, *HSPC095* ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/))
- **Identifiers:** `HGNC:25305`, `OMIM:616173`, `NCBI Gene:84081`, `Ensembl:ENSG00000126653`, `RefSeq:NM_032141`, `UniProtKB:Q9H0G5`
- **Genomic Locus:** Human chromosome `17q11.2` (approx. chr17:30,115,521–30,186,475, GRCh38/hg38), encoding a canonical 558-amino-acid nuclear protein ([UniProtKB:Q9H0G5](https://www.uniprot.org/uniprotkb/Q9H0G5)).

### Pathogenic Variants Reported in Literature

| Nucleotide Change (`NM_032141`) | Predicted Protein Change | Variant Type / Class | Zygosity & Origin | ACMG/AMP Classification | Population Frequency (gnomAD) | Functional Consequence | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `c.1359_1362delAAAG` | `p.Glu455AlafsTer20` | Frameshift deletion (final exon) | Homozygous, germline (Family 1, Egypt) | Pathogenic | Absent / ultra-rare; 0 homozygotes | Escapes NMD; truncates C-terminal RS-like domain & NLS (aa 531–540), causing cytoplasmic mislocalization & LoF | [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/) |
| `c.1272dupG` | `p.Lys425GlufsTer5` | Frameshift duplication (final exon) | Homozygous, germline (Family 2, Iran) | Pathogenic | Absent / ultra-rare; 0 homozygotes | Escapes NMD; truncates C-terminal RS-like domain & NLS (aa 531–540), causing cytoplasmic mislocalization & LoF | [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/) |
| `c.52C>T` | `p.Gln18Ter` | Nonsense / stop-gain (exon 2) | Homozygous, germline (Family 3, Pakistan) | Pathogenic | Ultra-rare; 0 homozygotes | Premature termination codon; subject to NMD or potential leaky downstream translation (severe LoF / hypomorph) | [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/) |
| `c.114+2T>G` | `p.?` (splice-donor disruption) | Canonical splice-site | Compound heterozygous (*in trans* with `c.1595T>A`), germline | Pathogenic / Likely pathogenic | Absent / ultra-rare; 0 homozygotes | Disrupts canonical 5' splice donor site, causing aberrant splicing / LoF | [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/) |
| `c.1595T>A` | `p.Val532Glu` | Missense (within NLS) | Compound heterozygous (*in trans* with `c.114+2T>G`), germline | Likely pathogenic / Pathogenic (functionally validated) | Absent / ultra-rare; 0 homozygotes | Substitutes conserved residue inside C-terminal NLS (aa 531–540), causing cytosolic mislocalization in HEK293T cells (hypomorphic LoF) | [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/) |

#### Population Database & Variant Curation Context
- **gnomAD Constraint & Allele Frequencies:** Consistent with an autosomal recessive mechanism, heterozygous loss-of-function variants occur at very low allele frequencies in healthy adult reference populations in gnomAD, whereas **homozygous predicted loss-of-function variants are absent**, reflecting strong purifying selection against biallelic null genotypes ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) `[Database / computational]`.
- **Missense Variants of Uncertain Significance (VUS):** Outside of functionally validated NLS variants such as `p.Val532Glu` ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)), uncharacterized rare missense variants in *NSRP1* submitted to ClinVar routinely remain classified as VUS under ACMG/AMP criteria unless supported by segregation and nuclear-speckle localization or splicing reporter assays `[Database / computational]`.
- **Somatic vs. Germline Origin:** All disease-causing NEDSSBA variants are **germline** inherited alleles ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). Somatic *NSRP1* alterations are not implicated in NEDSSBA.

### Modifier Genes
No modifier genes influencing NEDSSBA expressivity have been identified in human cohorts or genetic screens to date `[Human clinical]`. Observed phenotypic variability correlates primarily with allelic class (complete C-terminal NLS truncation vs. early nonsense `p.Gln18Ter` vs. NLS missense `p.Val532Glu`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

### Epigenetic Information
No primary DNA methylation, histone modification, or chromatin accessibility defects at the *NSRP1* locus have been reported as causal or modifying mechanisms in NEDSSBA in ENCODE, Roadmap Epigenomics, or PubMed literature retrieved in this session. Note that while nuclear speckles (`GO:0016607`) associate spatially with transcriptionally active chromatin domains ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)), disease-specific epigenomic profiling (e.g., episignature arrays) has not yet been published for NEDSSBA.

### Chromosomal Abnormalities
NEDSSBA is caused by intragenic sequence-level variants in *NSRP1* (`17q11.2`). Note that chromosome `17q11.2` also harbors *NF1*, and large contiguous 17q11.2 microdeletions cause the distinct autosomal dominant *NF1* microdeletion syndrome; however, biallelic chromosomal rearrangements or aneuploidies specifically causing NEDSSBA have not been reported in DECIPHER or PubMed literature retrieved in this session `[Database / computational]`.

---

## 5. Environmental Information

- **Environmental Factors:** None identified. No chemical toxins, ionizing radiation, environmental pollutants, or occupational exposures have been associated with NEDSSBA in PubMed or CTD searches conducted in this session.
- **Lifestyle Factors:** Not applicable. Maternal or patient lifestyle factors (diet, smoking, exercise, alcohol) do not cause NEDSSBA, though nutritional support is clinically relevant for secondary dysphagia management ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Infectious Agents:** Not applicable. NEDSSBA is a non-infectious Mendelian disorder, though secondary respiratory infections can complicate severe bulbar dysfunction and immobility in profound neurodevelopmental encephalopathies.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (Initiating Lesion to Clinical Manifestation)

1. **Biallelic germline pathogenic variants in *NSRP1* (`HGNC:25305`)** (`c.52C>T`, `c.114+2T>G`, `c.1272dupG`, `c.1359_1362delAAAG`, or `c.1595T>A`) **lead to** either nonsense-mediated mRNA decay / canonical splice-site disruption with quantitative protein depletion, **or** loss/perturbation of the C-terminal nuclear localization signal (NLS, amino acids 531–540) `[Demonstrated in human genetics & HEK293T cellular assays: PMID: 34385670; PMID: 38808951]`.
2. **Disruption of the C-terminal NLS or transcript depletion results in** failure of NSRP1 nuclear import and mislocalization of mutant NSRP1 protein from nuclear speckles (`GO:0016607`) in the nucleus (`GO:0005634`) into the cytosol (`GO:0005829`) `[Demonstrated in vitro in HEK293T cells: PMID: 34385670; PMID: 38808951]`.
3. **Depletion of functional NSRP1 within nuclear speckles leads to** loss of physical binding and functional antagonism toward serine/arginine-rich (SR) splicing factors **SRSF1** and **SRSF2** via NSRP1's arginine/serine-like (RS-like) and coiled-coil oligomerization domains `[Demonstrated biochemically & in vivo in mammalian cells: PMID: 21296756; PMID: 26797131]`.
4. **Unchecked SRSF1/SRSF2 activity and loss of NSRP1 RNA-binding (`GO:0003723`) result in** widespread dysregulation of spliceosome-mediated alternative pre-mRNA splicing (`GO:0000380`, `GO:0043484`), including aberrant isoform ratios of RNA processing factors, cell-cycle/survival transcripts, and cell-adhesion/migration regulators `[Demonstrated in mammalian splicing reporters & mouse conditional knockouts: PMID: 21296756; PMID: 26797131; PMID: 34033671; inferred in human neural progenitors: PMID: 34385670]`.
5. **Dysregulated alternative pre-mRNA splicing in neural stem/progenitor cells (`CL:0000047`) and differentiating neurons (`CL:0000540`) during embryonic brain development (`GO:0007420`) leads to** impaired neurogenesis (`GO:0022008`), defective neuronal migration, altered cortical lamination, and impaired axonal/synaptic maturation `[Inferred from human neuroimaging malformations, mouse embryonic lethality, and C. elegans migration defects: PMID: 34385670; PMID: 21296756; PMID: 22342930]`, **where the mechanism branches into three anatomical-clinical pathways:**
   - **Branch 5A (Supratentorial Cortical & Commissural Malformation):** Defective cortical neurogenesis, lamination, and interhemispheric axon tract formation **result in** microcephaly (`HP:0000252`), simplified gyral patterns (`HP:0009879`), incomplete opercularization, and corpus callosum hypoplasia (`HP:0002079`) `[Demonstrated on human brain MRI: PMID: 34385670]`, **which in turn lead to**:
     - **5A-i:** Cortical network hyperexcitability and epileptiform discharges (`HP:0002353`), **resulting in** early-onset, often drug-resistant seizures (`HP:0001250`) `[Demonstrated clinically: PMID: 34385670]`.
     - **5A-ii:** Severe disruption of integrative association and language networks, **resulting in** global developmental delay (`HP:0001263`), intellectual disability (`HP:0001249`), and absent or delayed speech (`HP:0001344`) `[Demonstrated clinically: PMID: 34385670; PMID: 38808951]`.
   - **Branch 5B (Corticospinal & Brainstem Motor Pathway Dysfunction):** Impaired maturation and upper motor neuron integrity across cortical pyramidal neurons (`CL:0000598`) and descending brainstem (`UBERON:0002298`) / spinal cord (`UBERON:0002240`) tracts (`HP:0002365`) **lead to** loss of descending inhibitory modulation over spinal stretch reflexes `[Inferred from clinical upper motor neuron signs & MRI brainstem thinning: PMID: 34385670]`, **resulting in** axial hypotonia (`HP:0008936`), appendicular spasticity / spastic tetraplegia (`HP:0001257`, `HP:0002510`), dysphagia (`HP:0002015`), and inability to walk (`HP:0002540`) `[Demonstrated clinically: PMID: 34385670]`.
   - **Branch 5C (Infratentorial Cerebellar Dysfunction):** Impaired cerebellar cortical and Purkinje cell (`CL:0000121`) / vermian morphogenesis **results in** cerebellar vermis hypoplasia (`HP:0001320`) or cerebellar atrophy (`HP:0001272`) `[Demonstrated on human brain MRI: PMID: 34385670]`, **which leads to** impaired sensorimotor coordination manifesting as gait ataxia (`HP:0002066`) in ambulatory patients with partial residual NSRP1 function `[Demonstrated clinically in milder genotype: PMID: 38808951]`.

---

### Detailed Mechanistic Breakdown

#### Protein Structure and Dysfunction
Canonical human NSRP1 (`UniProtKB:Q9H0G5`, 558 amino acids, apparent molecular weight ~70 kDa on SDS-PAGE, hence *NSrp70*) contains four critical functional modules ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/); [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)):
1. **Two putative RNA Recognition Motifs (RRMs):** Mediate RNA binding (`GO:0003723`).
2. **Arginine/Serine-like (RS-like) Domain:** Mediates direct physical interaction with spliceosomal SR proteins SRSF1 (ASF/SF2) and SRSF2 (SC35) ([PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/)).
3. **Two Coiled-Coil Domains:** Mediate NSRP1 self-oligomerization, which is required for speckle targeting and splicing modulation ([PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/)).
4. **C-terminal Nuclear Localization Signal (NLS, residues 531–540):** Embedded within the C-terminal RS-like region and indispensable for nuclear import ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

> **Direct Abstract Support:**
> *"Functional validation using HEK293T cells transfected with either wild-type or mutated GFP-tagged Nsrp1 suggests that the Val532Glu variant interferes with the function of the nuclear localization signal, and leads to mislocalization of NSRP1 in the cytosol, thus confirming the pathogenicity of the observed variant."* — Neuens et al., *American Journal of Medical Genetics Part A*, 2024 ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[In vitro / cellular]`

Both C-terminal frameshift variants (`p.Lys425GlufsTer5`, `p.Glu455AlafsTer20`)—which reside in the final exon and escape nonsense-mediated mRNA decay—and the `p.Val532Glu` missense substitution disrupt this NLS, sequestering NSRP1 in the cytosol (`GO:0005829`) and causing a functional **loss of nuclear splicing activity** rather than toxic gain-of-function aggregation ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

#### Molecular Pathways and Biochemical Abnormalities
- **Spliceosome / Alternative Pre-mRNA Splicing Pathway (`GO:0008380`, `GO:0000380`, `GO:0043484`):** Rather than acting in canonical cytoplasmic kinase cascades (e.g., Wnt, MAPK, or mTOR), NSRP1 operates directly within **nuclear speckles** (`GO:0016607`) as a stoichiometric regulator of splice-site selection ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)). Kim et al. (2011, 2016) demonstrated that NSRP1 co-localizes with SC35 (SRSF2) and SRSF1, binds them through its RS-like region, and **counteracts SRSF1- and SRSF2-driven exon inclusion/exclusion** on alternative splicing targets (such as *CD44*, *FAS*, and *TRA2B* minigene reporters *in vivo*) ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/)) `[In vitro / cellular]`.

> **Direct Abstract Support:**
> *"Nuclear speckles are known to be the storage sites of mRNA splicing regulators. We report here the identification and characterization of a novel speckle protein, referred to as NSrp70 (nuclear speckle-related protein 70; originally designated as CCDC55), based on its subcellular localization and apparent molecular weight."* — Kim et al., *Nucleic Acids Research*, 2011 ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)) `[In vitro / cellular]`

#### Cellular Processes and Tissue Damage Mechanisms
- **Neurogenesis, Cell Cycle Control, Cell Survival, and Cell Migration:** During mammalian brain development (`GO:0007420`), precise alternative splicing transitions govern neural progenitor (`CL:0000047`) proliferation, neurogenesis (`GO:0022008`), cortical radial/tangential migration, cortical lamination, and synaptogenesis ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Complete loss of *Nsrp1* in mice causes early pre-/peri-implantation embryonic lethality ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)), while conditional deletion in mouse thymocytes (`CL:0000893`) causes aberrant splicing of *Srsf1* and other spliceosomal/cell-cycle genes, triggering dysregulated cell-cycle progression and cell death ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)) `[Model organism]`. In *C. elegans*, loss of the ortholog *ccdc-55* disrupts temporal cell migration stopping cues in distal tip cells ([PMID: 22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/)) `[Model organism]`. In human fetuses and infants with biallelic *NSRP1* variants, the primary tissue abnormality is **developmental hypoplasia and malformation of cortical development** (simplified gyration, under-opercularization, callosal and vermian hypoplasia) rather than ischemia, fibrosis, or primary necrosis ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) `[Human clinical]`.

#### Metabolic Changes & Immune System Involvement
- **Metabolic Changes:** No primary defects in energy, amino acid, or lipid metabolism have been demonstrated in human NEDSSBA patients `[Human clinical]`.
- **Immune System Involvement:** Although conditional *Nsrp1* knockout in mouse T cells (`CD4-Cre`) causes severe thymocyte maturation arrest and peripheral lymphopenia ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)) `[Model organism]`, clinically overt primary immunodeficiency or autoimmunity has **not** been reported as a defining clinical feature in published human NEDSSBA patients ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`. Whether subclinical T-cell repertoire or lymphocyte splicing alterations exist in human *NSRP1* patients remains uninvestigated.

> **Direct Abstract Support:**
> *"Global splicing and transcriptional profiling revealed that NSrp70 regulates the cell cycle and survival of thymocytes by controlling the alternative processing of various RNA splicing factors, including the oncogenic splicing factor SRSF1."* — Kim et al., *Nucleic Acids Research*, 2021 ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)) `[Model organism]`

#### Molecular Profiling & Advanced Technologies
- **Transcriptomics / Splicing Profiling:** Global RNA-seq and alternative splicing profiling in *Nsrp1*-deficient murine thymocytes demonstrated broad intron retention and exon-skipping defects across RNA-processing factors (*Srsf1*, *Son*, *Sf3b1*) and cell-cycle regulators ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)) `[Model organism]`. However, patient-derived neural transcriptomics, brain proteomics, metabolomics, lipidomics, single-cell RNA-seq, spatial transcriptomics, and human neural organoid CRISPR screens specific to NEDSSBA have **not yet been published** in literature retrieved during this session.

---

## 7. Anatomical Structures Affected

### Organ and System Level
- **Primary Body System Involved:** Nervous system (`UBERON:0001016`) — specifically the central nervous system ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Primary Organ Directly Affected:** Brain (`UBERON:0000955`) and descending corticospinal pathways through the brainstem (`UBERON:0002298`) and spinal cord (`UBERON:0002240`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Secondary Organ / Musculoskeletal Involvement:** Skeletal muscle (`UBERON:0001134`) and pharyngeal/oromotor musculature are secondarily affected via upper motor neuron spasticity (`HP:0001257`), axial hypotonia (`HP:0008936`), and neurogenic dysphagia (`HP:0002015`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Primary cardiac, hepatic, renal, or endocrine organ malformations are not established features of NEDSSBA.

### Specific Anatomical Localization & Lateralization
Neuroimaging in affected individuals demonstrates **bilateral, symmetric** involvement across supratentorial and infratentorial brain structures ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)):
- **Cerebral hemispheres (`UBERON:0001870`) & Cerebral cortex (`UBERON:0000956`):** Microcephaly (`HP:0000252`), simplified gyral pattern (`HP:0009879`), and bilateral incomplete opercularization over the Sylvian fissures/insula ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Corpus callosum (`UBERON:0002336`):** Midline corpus callosum hypoplasia/dysgenesis (`HP:0002079`, `HP:0007370`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Cerebellum (`UBERON:0002037`) & Cerebellar vermis (`UBERON:0004720`):** Midline superior/inferior cerebellar vermis hypoplasia (`HP:0001320`) and cerebellar atrophy (`HP:0001272`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Brainstem (`UBERON:0002298`):** Thin/hypoplastic brainstem (`HP:0002365`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Tissue and Cell Level
- **Primary Tissue Type:** Nervous tissue (developing neuroepithelium, cortical gray matter, commissural white matter tracts, and cerebellar cortex) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Target Cell Populations (Inferred from human clinicoradiological phenotype & model organisms):**
  - **Neuronal stem / neural progenitor cells (`CL:0000047`):** Implicated upstream in microcephaly and simplified cortical gyration ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  - **Neurons (`CL:0000540`), including cortical pyramidal neurons (`CL:0000598`):** Implicated in cortical epileptogenesis (`HP:0001250`), callosal projection hypoplasia, and corticospinal upper motor neuron spasticity (`HP:0001257`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  - **Cerebellar Purkinje cells (`CL:0000121`) and cerebellar granule/vermian neurons:** Implicated in vermian hypoplasia (`HP:0001320`) and gait ataxia (`HP:0002066`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
  - **Thymocytes (`CL:0000893`):** Demonstrated target in murine conditional *Nsrp1* knockout models ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)).

### Subcellular Level
- **Nuclear speck / nuclear speckle (`GO:0016607`) within the Nucleus (`GO:0005634`):** Physiological site of NSRP1 enrichment and pre-mRNA splicing regulation ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)).
- **Cytosol (`GO:0005829`):** Pathological site of mutant NSRP1 accumulation when variants truncate or disrupt the C-terminal NLS (`p.Lys425GlufsTer5`, `p.Glu455AlafsTer20`, `p.Val532Glu`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

---

## 8. Temporal Development

### Onset
- **Typical Age of Onset:** **Congenital to early infantile** (neonatal period through the first months of life) in classic severe NEDSSBA ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Structural brain malformations arise prenatally during fetal cortical folding, callosal formation, and posterior fossa development, while hypotonia, developmental delay, and seizures present in early infancy ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). In milder hypomorphic presentations (`p.Val532Glu`), onset is recognized in **infancy to early childhood** via delayed motor and language milestones without infantile epilepsy ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Onset Pattern:** Insidious developmental failure to acquire milestones, frequently punctuated by acute onset of infantile epileptic seizures ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Progression
- **Disease Stages:** Formal clinical staging systems (such as AJCC or WHO classifications) do not exist for NEDSSBA. Clinically, the classic trajectory comprises:
  1. *Fetal / Neonatal phase:* Congenital structural brain anomalies, variable microcephaly, and neonatal axial hypotonia ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  2. *Infantile phase:* Emergence of epileptic seizures (often refractory) and evolution of peripheral tone into appendicular spasticity / spastic tetraplegia ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  3. *Childhood / Adolescent phase:* Static profound neurodevelopmental impairment (or stable mild-moderate intellectual disability and ataxia in attenuated cases), with neuroimaging showing partial postnatal maturation of cortical sulcation making simplified gyral patterns appear less striking in older children than in early infancy ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Progression Rate & Course Pattern:** Primarily a **static to slowly evolving congenital neurodevelopmental encephalopathy** (rather than a rapid late-onset neurodegenerative storage disease), superimposed with **episodic/chronic seizures** that may aggravate epileptic encephalopathy and early-life mortality risk ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Disease Duration:** **Chronic lifelong** condition, with premature mortality reported in a subset of severely affected children ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Patterns
- **Remission Patterns:** Spontaneous remission of the underlying neurodevelopmental disorder does not occur. Seizures achieved pharmacological control in 3 of 6 epileptic patients in the Calame et al. cohort, whereas 3 of 6 remained drug-resistant ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Critical Periods:** Embryonic and fetal neurodevelopment (neurogenesis, cortical migration, opercularization, and synaptogenesis) represents the primary developmental window of vulnerability to NSRP1 deficiency ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)). Postnatally, early infancy represents a critical window for aggressive seizure control and early physical/occupational rehabilitation.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence and Incidence:** **Ultra-rare (<1 per 1,000,000)**. Exact population-based point prevalence and annual incidence per 100,000 have not been established in Orphanet, CDC, WHO, or Global Burden of Disease (GBD) registries. Across peer-reviewed literature retrieved in this session, **7 molecularly confirmed individuals** (plus 1 ungenotyped affected deceased sibling) from **4 unrelated families** have been published between 2021 and 2024 ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)) `[Human clinical]`.

### Genetic Inheritance Characteristics
- **Inheritance Pattern:** **Autosomal recessive (AR)** ([OMIM:620001](https://omim.org/entry/620001); [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Penetrance:** **Complete (100%)** among reported individuals carrying biallelic pathogenic *NSRP1* variants ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). Heterozygous carriers are clinically unaffected (0% penetrance in heterozygotes).
- **Expressivity:** **Variable**, correlating with allele severity:
  - *Severe end:* Final-exon frameshift variants (`p.Glu455AlafsTer20`, `p.Lys425GlufsTer5`) cause profound non-verbal, non-ambulatory spastic tetraplegia, microcephaly ($Z$-scores down to $-5.60$), and infantile epilepsy ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  - *Intermediate:* Early exon 2 nonsense variant (`p.Gln18Ter`) was associated with somewhat less severe epilepsy and acquisition of slightly more developmental milestones within the initial cohort ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  - *Milder end:* Compound heterozygosity for `c.114+2T>G` and the NLS missense variant `p.Val532Glu` caused intellectual disability and ataxic gait with preserved independent ambulation, short-sentence speech, and absence of severe spastic tetraplegia ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Genetic Anticipation:** Not applicable (not a nucleotide repeat expansion disorder).
- **Germline Mosaicism:** Not reported to date; all evaluated parents of affected probands were obligate heterozygous germline carriers ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Founder Effects:** None established. Each of the 4 reported families harbored distinct private *NSRP1* variant alleles (`c.1359_1362delAAAG`, `c.1272dupG`, `c.52C>T`, and `c.114+2T>G` / `c.1595T>A`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Consanguinity Role:** High in homozygous families—3 of 4 reported families originated from regions with elevated consanguinity practices (Egypt, Iran, and Pakistan) and carried homozygous variants within regions of autozygosity ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Carrier Frequency:** Ultra-low globally; exact pan-ethnic carrier frequency has not been formally tabulated in GeneReviews or ACMG carrier screening panels, though individual LoF alleles are exceedingly rare in gnomAD ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Population Demographics
- **Geographic & Ancestral Distribution:** Reported families originate from **Egypt** (`c.1359_1362delAAAG`), **Iran** (`c.1272dupG`), **Pakistan** (`c.52C>T`), and **Europe / Belgium** (`c.114+2T>G` and `c.1595T>A`), indicating pan-ethnic susceptibility without geographic endemism ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Sex Ratio:** Both males and females are affected as expected for an autosomal recessive disorder (mixed-sex sibships in Calame et al. plus 1 female in Neuens et al.; sample size $n=7$ is too small for formal sex-ratio statistics) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Age Distribution:** All reported molecularly diagnosed patients have been **infants, children, and adolescents** (ranging from 3 months to 14 years at clinical evaluation) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). Adult cohorts have not yet been described.

---

## 10. Diagnostics

### Clinical Tests
- **Laboratory Tests & Circulating Biomarkers:** No blood, urine, or CSF biochemical test orFDA/BEST-validated circulating biomarker diagnoses NEDSSBA. Routine metabolic tests (plasma amino acids, urine organic acids, acylcarnitines, lactate/pyruvate) are utilized only to exclude neurometabolic mimics.
- **Neuroimaging Studies (Brain MRI — Primary Structural Modality):** Cranial magnetic resonance imaging (MRI) is essential in diagnostic evaluation. Characteristic findings, particularly prominent on infantile scans, include ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)):
  - Simplified cortical gyral pattern (`HP:0009879`)
  - Bilateral incomplete / under-opercularization (widened Sylvian fissures)
  - Cerebellar vermis hypoplasia (`HP:0001320`) or cerebellar atrophy (`HP:0001272`)
  - Corpus callosum dysgenesis/thinning (`HP:0002079`)
  - Thin/hypoplastic brainstem (`HP:0002365`) and generous extra-axial CSF spaces
  - *Diagnostic caveat:* Cortical sulcation matures postnatally, so simplified gyral patterns may appear subtle or absent if MRI is first performed later in childhood, and milder hypomorphic cases may lack gross structural brain malformations ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Electrophysiology (EEG):** Routine and video electroencephalography (EEG) demonstrates diffuse background slowing and focal or multifocal epileptiform discharges (`HP:0002353`, documented in 5/6 patients in the Calame et al. cohort) to characterize seizure semiology and monitor antiseizure treatment ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Functional Tests & Biopsy/Pathology Findings:** Formal videofluoroscopic swallow studies may be used clinically to evaluate dysphagia (`HP:0002015`). Brain or muscle biopsy histopathology is **not indicated** and no human neuropathological autopsy series of NEDSSBA has been published in literature retrieved in this session.

### Genetic Testing
Molecular confirmation of **biallelic pathogenic or likely pathogenic variants in *NSRP1*** is required to establish a definitive diagnosis of NEDSSBA ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Whole Exome Sequencing (WES) & Whole Genome Sequencing (WGS) — Recommended First-Tier Approaches:** Family-based (trio) WES or WGS is the diagnostic modality of choice. All 6 initial patients were identified via family-based WES ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)), and the 2024 compound heterozygous case (`c.114+2T>G` / `c.1595T>A`) was diagnosed via WGS ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). WGS provides additional sensitivity for non-coding intronic splice variants and small structural deletions.
- **Multigene Panels:** Comprehensive neurodevelopmental disorder, epilepsy, cerebral palsy mimic, or microcephaly NGS panels can detect *NSRP1* variants **only if updated post-2021** to include *NSRP1*; older panels omit this gene.
- **Single-Gene Testing (Sanger Sequencing):** Indicated primarily for targeted familial carrier testing, cascade testing of at-risk relatives, or prenatal/preimplantation testing once familial *NSRP1* variants are known.
- **Chromosomal Microarray (CMA), Karyotyping, FISH, Mitochondrial DNA Testing, & Repeat Expansion Testing:** Low primary diagnostic yield for NEDSSBA, as all reported pathogenic *NSRP1* alleles are single-nucleotide variants or small indels (`1–4 bp`) invisible to karyotyping, FISH, and standard CMA ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). CMA may be considered only if an unphased apparent homozygote in a non-consanguineous family requires exclusion of a multi-exon/whole-gene deletion *in trans*.

### Omics-Based Diagnostics
- **RNA Sequencing (Transcriptomics):** Clinical blood- or fibroblast-derived RNA-seq has high potential utility as a reflex diagnostic assay to validate intronic or splice-site variants (such as `c.114+2T>G`) in *NSRP1*, as *NSRP1* is ubiquitously expressed across tissues ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Functional Cellular Assays (Research-Level Validation):** Transfection of GFP-tagged mutant *NSRP1* cDNA into HEK293T cells to evaluate nuclear speckle (`GO:0016607`) vs. cytosolic (`GO:0005829`) localization is an established experimental assay to reclassify VUS in the NLS domain (demonstrated for `p.Val532Glu` in [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)). Proteomics, metabolomics, epigenomic episignatures, and liquid biopsy are not applicable.

### Clinical Criteria & Differential Diagnosis
- **Standardized Clinical Criteria:** No formal consensus clinical diagnostic criteria exist due to the ultra-rare nature of NEDSSBA; diagnosis relies on integrating clinical neuroimaging/neurological phenotypes with biallelic *NSRP1* molecular findings.
- **Differential Diagnosis:**
  1. **Acquired Perinatal Spastic Cerebral Palsy:** Distinguished by perinatal hypoxic-ischemic history/lesions on MRI, absence of congenital simplified gyration/under-opercularization, and absence of biallelic *NSRP1* variants ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  2. **Monogenic Cerebral Palsy Mimics & Complex Hereditary Spastic Paraplegias (e.g., *AP4B1*, *AP4M1*, *AP4E1*, *SPAST*):** Share axial hypotonia evolving to spastic tetraplegia, microcephaly, thin corpus callosum, and absent speech; distinguished via WES/WGS.
  3. **Pontocerebellar Hypoplasias (PCH) and Spliceosomopathies / Ribosomopathies:** Share microcephaly, vermian/brainstem hypoplasia, spasticity, and early-onset seizures; distinguished by progressive pontocerebellar atrophy on serial MRI and multigene/exome sequencing.
  4. **Tubulinopathies (*TUBA1A*, *TUBB2B*, *TUBB3*) and Lissencephaly Spectrum Disorders:** Share simplified gyration, incomplete opercularization, callosal dysgenesis, and cerebellar hypoplasia, typically accompanied by characteristic basal ganglia dysmorphism; distinguished by WES/WGS.

### Screening
- **Newborn & Population Screening:** *NSRP1* is **not** included on state/national newborn dried-blood-spot screening panels or standard ACMG population carrier-screening tiers `[Database / computational]`.
- **Cascade Carrier Screening:** Targeted *NSRP1* variant testing is indicated for biological parents and extended family members of a diagnosed proband, particularly in consanguineous kindreds ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Mortality Rate & Early-Life Survival:** Formal actuarial 5-year and 10-year survival curves do not exist due to small sample size ($n=7$ confirmed patients). However, in the initial severe cohort of Calame et al. (2021), **2 of 6 molecularly confirmed patients (33%)**—along with **1 additional similarly affected ungenotyped sibling**—died in early childhood, demonstrating substantial early-life mortality in severe biallelic loss-of-function genotypes ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)) `[Human clinical]`. Conversely, other patients in the cohort were alive at ages 3 and 9 years ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)), and the milder compound heterozygous patient was alive and medically stable at age 14 years ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Life Expectancy:** Reduced in severe classic NEDSSBA with refractory epilepsy and profound bulbar/motor impairment; potentially near-normal into adolescence/adulthood in attenuated hypomorphic cases, though long-term adult natural history remains unknown ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

### Morbidity and Function
- **Long-Term Disability Outcomes:**
  - *Classic severe genotype (6/7 patients):* Profound lifelong neurodevelopmental disability; 100% of patients in Calame et al. failed to acquire independent ambulation (`HP:0002540`) or functional speech (`HP:0001344`) and required full custodial care ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
  - *Attenuated hypomorphic genotype (1/7 patients):* Milder intellectual disability, independent walking with gait ataxia (`HP:0002066`), and verbal communication in short sentences at age 14 years ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Quality of Life Measures:** No quantitative EQ-5D, SF-36, or PROMIS scores have been published for NEDSSBA.

### Disease Course
- **Complications:** Medically refractory epilepsy / status epilepticus (drug-resistant in 3/6 severe patients), feeding difficulties and neurogenic dysphagia (`HP:0002015`) predisposing to malnutrition and aspiration pneumonia, joint contractures/orthopedic deformities secondary to chronic spastic tetraplegia (`HP:0002510`), and premature childhood death ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Recovery Potential:** Structural congenital brain malformations and genetic splicing deficiency are irreversible with current therapies; complete neurological recovery does not occur, though rehabilitative therapy and antiseizure medications improve functional comfort and milestone attainment within genetic limits ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

### Prediction
- **Prognostic Factors:**
  1. **Genotype / Residual Nuclear Localization:** Frameshift variants truncating the C-terminal NLS (`p.Glu455AlafsTer20`, `p.Lys425GlufsTer5`) predict the most severe neurological outcome, early exon 2 nonsense (`p.Gln18Ter`) was associated with modestly milder epilepsy/milestone attainment, and partial-function missense substitution in the NLS (`p.Val532Glu`) predicts an ambulatory, verbal phenotype without severe spasticity ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
  2. **Refractory Infantile Epilepsy & Structural MRI Burden:** Early drug-resistant seizures and severe infantile cortical/brainstem hypoplasia correlate with higher morbidity and early mortality ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Prognostic Biomarkers:** No validated molecular blood or CSF prognostic biomarkers exist beyond the *NSRP1* genotype itself.

---

## 12. Treatment

There is currently **no curative or disease-modifying therapy** for NEDSSBA. Clinical management is supportive, symptomatic, and multidisciplinary, adapted from standard neurological guidelines for developmental and epileptic encephalopathies and spastic cerebral palsy ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).

### Pharmacotherapy
- **Antiseizure Medications (for Epilepsy, `HP:0001250`):** Standard broad-spectrum and focal antiseizure medications are utilized empirically to control infantile-onset seizures, including:
  - **Levetiracetam** (`NCIT:C61884`, `CHEBI:6437`) — synaptic vesicle glycoprotein 2A (SV2A) modulator.
  - **Valproic acid / Valproate** (`NCIT:C62329` / `NCIT:C71156`, `CHEBI:39867`) — broad-spectrum sodium-channel and GABAergic modulator.
  - **Phenobarbital** (`NCIT:C76956`, `CHEBI:8069`) — $\text{GABA}_\text{A}$ receptor agonist frequently used for neonatal/early-infantile seizures.
  - Other standard agents such as **Topiramate** (`NCIT:C821`) or **Carbamazepine** (`NCIT:C341`) depending on electroclinical seizure type.
- **Anti-Spasticity Pharmacotherapy (for Appendicular Spasticity, `HP:0001257`):**
  - **Baclofen** (`NCIT:C90890`, `CHEBI:2972`) — $\text{GABA}_\text{B}$ receptor agonist skeletal muscle relaxant used to reduce painful limb hypertonia and clonus.
- **Pharmacogenomics:** No *NSRP1*-specific pharmacogenomic drug-metabolism interactions or CPIC/PharmGKB guidelines exist. Standard HLA screening applies if aromatic anticonvulsants (such as carbamazepine, `NCIT:C341`) are prescribed in relevant ancestral populations.

### Advanced Therapeutics
- **Gene Therapy, Cell Therapy, RNA-Based Therapies (ASOs/siRNA/mRNA), Targeted Therapies, & Immunotherapies:** **None available or in clinical development.** No viral-vector gene replacement, CRISPR base/prime editing, antisense oligonucleotide (e.g., splice-switching ASO for `c.114+2T>G`), stem-cell therapy, or molecularly targeted small molecule has been developed or tested for *NSRP1*-related NEDSSBA in PubMed or ClinicalTrials.gov records retrieved during this session.

### Surgical and Interventional
- No disease-specific neurosurgical cure exists. Standard supportive surgical interventions in severe spastic quadriplegic and dysphagic encephalopathies—such as gastrostomy tube placement for severe dysphagia (`HP:0002015`) or orthopedic tendon/contracture procedures—are guided by individual clinical need rather than NEDSSBA-specific surgical trials.

### Supportive and Rehabilitative Care
Multidisciplinary allied health rehabilitation forms the cornerstone of longitudinal care across both severe and milder NEDSSBA phenotypes ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)):
- **Physical Therapy (`NCIT:C51581`):** Targeted at optimizing postural trunk control (`HP:0008936`), preventing spastic contractures (`HP:0001257`), providing seating/orthotic support in non-ambulatory patients, and improving balance/ataxic gait (`HP:0002066`) in ambulatory patients.
- **Occupational Therapy (`NCIT:C121351`):** Focused on adaptive equipment, fine motor skills, and activities of daily living.
- **Speech Therapy (`NCIT:C92562`):** Addresses augmentative and alternative communication (AAC) in non-verbal patients (`HP:0001344`), language expansion in verbal patients ([PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)), and safe swallowing strategies for dysphagia (`HP:0002015`).
- **Nutritional & Palliative Support:** Caloric optimization, aspiration precautions, and family psychosocial support.

### Experimental Treatments
- **Clinical Trials:** A search of ClinicalTrials.gov records retrieved **0 active or completed interventional clinical trials (no NCT identifiers)** specifically targeting *NSRP1* or NEDSSBA `[Database / computational]`.

### Treatment Outcomes & Strategy
- **Treatment Response Rates:** In the Calame et al. cohort, **50% (3/6)** of patients had seizures responsive to antiseizure medications, while **50% (3/6)** exhibited drug-resistant epilepsy requiring combination polypharmacy ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Side Effects & Adverse Events:** Antiseizure polypharmacy and baclofen (`NCIT:C90890`) carry risk of sedation, worsening of baseline axial hypotonia (`HP:0008936`), drooling, and hepatotoxicity (with valproic acid, `CHEBI:39867`), requiring careful titration in hypotonic infants.
- **Treatment Strategy & Personalized Medicine:** No genotype-specific precision drug exists yet; however, molecular diagnosis of *NSRP1* ends the diagnostic odyssey, prevents futile empirical metabolic or immunomodulatory trials, distinguishes genetic spastic tetraplegia from acquired perinatal cerebral palsy, and tailors developmental prognosis (e.g., recognizing ambulatory/verbal potential in hypomorphic NLS missense alleles such as `p.Val532Glu`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).

---

## 13. Prevention

### Prevention Levels
- **Primary Prevention:** Because NEDSSBA arises from inherited germline variants, primary prevention is achievable only in families with known carrier status through reproductive genetic options—specifically **preimplantation genetic testing for monogenic disorders (PGT-M)** or donor gametes—guided by **Genetic Counseling** (`NCIT:C17178`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Secondary Prevention:** Early molecular diagnosis via rapid infant WES/WGS, targeted **prenatal genetic testing** (chorionic villus sampling or amniocentesis) in known carrier couples, prompt initiation of antiseizure therapy (`NCIT:C61884`, `NCIT:C62329`, `NCIT:C76956`) upon first seizure/EEG abnormality, and early developmental rehabilitation (`NCIT:C51581`, `NCIT:C121351`, `NCIT:C92562`) to mitigate epileptic encephalopathy burden.
- **Tertiary Prevention:** Prevention of secondary medical complications in established disease, including anti-spasticity management (`NCIT:C90890`) and orthotics to prevent fixed joint contractures and hip subluxation, swallowing interventions to prevent aspiration pneumonia, and seizure rescue protocols to prevent status epilepticus.

### Immunization, Screening, Counseling, Behavioral, Public Health, & Prophylaxis
- **Immunization:** No vaccine prevents NEDSSBA; affected children should receive routine age-appropriate pediatric immunizations (including influenza and pneumococcal vaccines) as tertiary prevention against respiratory infections that can trigger seizure decompensation or complicate bulbar dysfunction.
- **Genetic Screening & Risk Stratification:** Cascade carrier testing of at-risk biological relatives in extended or consanguineous kindreds stratifies couples at a **25% per-pregnancy risk** of having an affected child ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Genetic Counseling (`NCIT:C17178`):** Essential upon diagnosis to explain autosomal recessive inheritance, 25% recurrence risk, asymptomatic carrier status (50% chance in unaffected siblings), and prenatal/preimplantation testing options ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Behavioral, Public Health, Environmental Interventions, & Preventive Prophylaxis:** Lifestyle/environmental interventions and pharmacological prophylaxis do not prevent disease occurrence. Culturally sensitive community education regarding carrier screening in consanguineous marriages represents a general public health measure for autosomal recessive neurodevelopmental disorders.

---

## 14. Other Species / Natural Disease

### Taxonomy and Orthologous Genes
*NSRP1* is evolutionarily conserved across metazoans, with well-annotated orthologs across vertebrate and invertebrate species `[Database / computational; Model organism]`:
- **Human (*Homo sapiens*, `NCBITaxon:9606`):** *NSRP1* (`NCBI Gene:84081`, `HGNC:25305`)
- **House mouse (*Mus musculus*, `NCBITaxon:10090`):** *Nsrp1* (`NCBI Gene:237859`, `MGI:2144305`) ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/))
- **Norway rat (*Rattus norvegicus*, `NCBITaxon:10116`):** *Nsrp1* (`NCBI Gene:303346`)
- **Zebrafish (*Danio rerio*, `NCBITaxon:7955`):** *nsrp1*
- **Fruit fly (*Drosophila melanogaster*, `NCBITaxon:7227`):** *CG15747* (`NCBI Gene:38150`) ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/))
- **Nematode (*Caenorhabditis elegans*, `NCBITaxon:6239`):** *ccdc-55* (`NCBI Gene:180459`, `WormBase:WBGene00016100`) ([PMID: 22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/); [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/))

### Natural Disease & Veterinary Relevance
- **Naturally Occurring Animal Disease & Breed Associations:** **None reported.** Searches of Online Mendelian Inheritance in Animals (OMIA) and PubMed retrieved no spontaneous Mendelian neurological or developmental disorder caused by *NSRP1* mutations in companion animals, livestock, or wildlife, and no Vertebrate Breed Ontology (`VBO`) breed-specific predisposition exists `[Database / computational]`. (In agricultural transcriptomics, porcine *NSRP1* has been noted only in benign quantitative trait locus/splicing studies of adipose traits rather than natural clinical disease.)

### Comparative Biology & Transmission
- **Comparative Pathology & Evolutionary Conservation:** Across mouse (*Nsrp1*), fruit fly (*CG15747*), and nematode (*ccdc-55*), complete loss of function consistently impairs early embryonic or larval viability and cell migration/proliferation, underscoring deep evolutionary conservation of NSRP1/CCDC55 in metazoan developmental RNA processing ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/); [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
- **Transmission / Zoonotic Potential:** **Not applicable.** NEDSSBA is a non-transmissible genetic disorder with zero zoonotic potential.

---

## 15. Model Organisms

### Overview of Experimental Model Systems

| Model System | Species & Taxon ID | Gene / Construct | Model Type | Key Phenotype Observed | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Constitutive Mouse Knockout / Gene-Trap** | *Mus musculus* (`NCBITaxon:10090`) | *Nsrp1* (`MGI:2144305`, `NCBI Gene:237859`) | Mammalian genetic null (gene-trap / KO) | **Early embryonic lethality** in homozygotes; broad wild-type expression in oocytes, morulae, and mid-gestation E11.5 embryos | [PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/) |
| **Conditional Lineage Mouse Knockout (`NSrp70-cKO`)** | *Mus musculus* (`NCBITaxon:10090`) | *Nsrp1* floxed $\times$ `CD4-Cre` | Mammalian conditional genetic KO (T-lymphocyte lineage) | Arrested double-positive to single-positive thymocyte maturation (`CL:0000893`), aberrant splicing of *Srsf1*/*Son*/*Sf3b1*, uncontrolled cell-cycle/cell-death dysregulation, severe peripheral lymphopenia | [PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/) |
| **Nematode Mutant & RNAi Knockdown** | *Caenorhabditis elegans* (`NCBITaxon:6239`) | *ccdc-55* (`WBGene00016100`, `NCBI Gene:180459`) | Invertebrate genetic mutant & RNAi knockdown | Larval developmental arrest/lethality and **distal tip cell (DTC) migration overshoot**, demonstrating defective temporal stopping of cell migration | [PMID: 22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/) |
| **Fruit Fly Ortholog Loss-of-Function** | *Drosophila melanogaster* (`NCBITaxon:7227`) | *CG15747* (`NCBI Gene:38150`) | Invertebrate genetic / knockdown context | Developmental lethality upon complete disruption, supporting essential conserved developmental role | [PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/) |
| **Human Cellular Mislocalization & Splicing Reporter Models** | *Homo sapiens* (`NCBITaxon:9606`) — HEK293T cell line | Wild-type vs. mutant GFP-tagged *NSRP1*/*Nsrp1* (e.g., `p.Val532Glu`, NLS-truncated mutants) & *CD44*/*FAS*/*TRA2B* minigenes | *In vitro* human cellular / biochemical | Demonstrates loss of nuclear speckle (`GO:0016607`) localization, **cytosolic mislocalization** (`GO:0005829`), loss of SRSF1/SRSF2 antagonism, and loss of alternative splicing regulation | [PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/) |

*Note on Induced Models and Patient iPSCs/Organoids:* No drug-induced, surgical, or patient-derived induced pluripotent stem cell (iPSC) / cerebral organoid models of NEDSSBA were identified in literature retrieved during this session.

### Model Characteristics: Phenotype Recapitulation and Limitations
- **Phenotype Recapitulation:**
  - *Cellular HEK293T models* accurately recapitulate the **subcellular pathology** of human C-terminal frameshift and NLS missense (`p.Val532Glu`) variants—specifically nuclear import failure and cytoplasmic mislocalization away from nuclear speckles—and directly quantify loss of alternative splicing activity against SRSF1/SRSF2 ([PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
  - *Invertebrate (*C. elegans* `ccdc-55`) and constitutive mouse (*Nsrp1*) models* recapitulate the **essential developmental requirement** of NSRP1 and reveal conserved roles in cell-cycle survival and Guided cell migration ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/); [PMID: 22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/); [PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)).
- **Model Limitations:**
  - **Embryonic Lethality in Constitutive Null Mice:** Because constitutive *Nsrp1* knockout mice die early in embryogenesis ([PMID: 21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/)), global null mice **cannot model postnatal human neurological phenotypes** such as infantile epilepsy (`HP:0001250`), appendicular spasticity (`HP:0001257`), microcephaly (`HP:0000252`), simplified gyration (`HP:0009879`), or incomplete opercularization (which is specific to gyrencephalic primate brains and absent in lissencephalic rodent cortices). This indicates either that surviving human patients retain low-level hypomorphic/residual NSRP1 activity or that human vs. murine pre-implantation embryos differ in maternal/splicing compensation ([PMID: 34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/)).
  - **Lack of Brain-Specific Conditional Knockouts:** Published murine conditional knockouts (`CD4-Cre`) targeted T lymphocytes (`CL:0000893`) ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)); neural-specific conditional knockouts (e.g., *Nestin-Cre* or *Emx1-Cre* crossing with floxed *Nsrp1* mice) or humanized knock-in mice (`p.Glu455AlafsTer20`, `p.Val532Glu`) are needed to model cortical malformation and epileptogenesis *in vivo*.

### Research Applications and Model Databases
- **Applications:** Existing floxed *Nsrp1* mouse alleles provide an immediate genetic resource to generate forebrain- and cerebellum-specific conditional knockouts for transcriptomic mapping of neuronal splicing targets, seizure threshold testing, and preclinical evaluation of AAV gene replacement or splice-modulating therapies ([PMID: 34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/)). HEK293T GFP-NSRP1 localization and minigene splicing assays provide rapid functional validation of clinical VUS ([PMID: 26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/); [PMID: 38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/)).
- **Key Model Organism Databases:**
  - **Mouse Genome Informatics (MGI):** `MGI:2144305` (*Nsrp1*)
  - **Rat Genome Database (RGD) / NCBI Gene:** `NCBI Gene:303346` (*Nsrp1*)
  - **WormBase:** `WBGene00016100` (*ccdc-55*)
  - **FlyBase / NCBI Gene:** *CG15747* (`NCBI Gene:38150`)
  - **Zebrafish Information Network (ZFIN):** *nsrp1*
  - **Alliance of Genome Resources:** Integrates cross-species *NSRP1* orthology and phenotype annotations (`HGNC:25305`).

---

## References

1. **Calame DG, Bakhtiari S, Logan R, et al.** Biallelic loss-of-function variants in the splicing regulator *NSRP1* cause a severe neurodevelopmental disorder with spastic cerebral palsy and epilepsy. *Genetics in Medicine*. 2021 Dec (epub Aug 2021);23(12):2455–2460. PMID: [34385670](https://pubmed.ncbi.nlm.nih.gov/34385670/).
2. **Neuens S, Kausar M, Kang SK, Soblet J, Van Dooren S, Olsen C, Janssen T, Caljon B, Jun CD, Smits G, Coppens S, Vilain C.** A milder form of NSRP1-associated neurodevelopmental disorder, caused by a missense variant in the nuclear localization signal. *American Journal of Medical Genetics Part A*. 2024 (epub May 2024). DOI: [10.1002/ajmg.a.63727](https://doi.org/10.1002/ajmg.a.63727). PMID: [38808951](https://pubmed.ncbi.nlm.nih.gov/38808951/).
3. **Kim YD, Lee JY, Oh KM, Araki M, Araki K, Yamamura K, Jun CD.** NSrp70 is a novel nuclear speckle-related protein that modulates alternative pre-mRNA splicing in vivo. *Nucleic Acids Research*. 2011 May;39(10):4300–4314. PMID: [21296756](https://pubmed.ncbi.nlm.nih.gov/21296756/).
4. **Kim CH, Kim YD, Choi EK, Kim HR, Na BR, Im SH, Jun CD.** Nuclear Speckle-related Protein 70 Binds to Serine/Arginine-rich Splicing Factors 1 and 2 via an Arginine/Serine-like Region and Counteracts Their Alternative Splicing Activity. *Journal of Biological Chemistry*. 2016 Mar;291(12):6169–6181. PMID: [26797131](https://pubmed.ncbi.nlm.nih.gov/26797131/).
5. **Kim CH, Park SM, Lee S, Kim YD, Jang SH, Woo SM, et al.** NSrp70 is a lymphocyte-essential splicing factor that controls thymocyte development. *Nucleic Acids Research*. 2021 Jun;49(10):5760–5778. DOI: [10.1093/nar/gkab389](https://doi.org/10.1093/nar/gkab389). PMID: [34033671](https://pubmed.ncbi.nlm.nih.gov/34033671/); PMCID: PMC8186196.
6. **Kovacevic I, Ho R, Cram EJ.** CCDC-55 is required for larval development and distal tip cell migration in *Caenorhabditis elegans*. *Mechanisms of Development*. 2012 Jan–Feb;128(11–12):548–559. DOI: [10.1016/j.mod.2012.01.003](https://doi.org/10.1016/j.mod.2012.01.003). PMID: [22342930](https://pubmed.ncbi.nlm.nih.gov/22342930/).
7. **Online Mendelian Inheritance in Man (OMIM).** #620001: Neurodevelopmental disorder with spasticity, seizures, and brain abnormalities (NEDSSBA) & *616173: Nuclear Speckle Splicing Regulatory Protein 1 (*NSRP1*). URL: [https://omim.org/entry/620001](https://omim.org/entry/620001) and [https://omim.org/entry/616173](https://omim.org/entry/616173).
8. **Monarch Initiative / Mondo Disease Ontology.** MONDO:0859275 — neurodevelopmental disorder with spasticity, seizures, and brain abnormalities. URL: [https://monarchinitiative.org/MONDO:0859275](https://monarchinitiative.org/MONDO:0859275).
9. **HUGO Gene Nomenclature Committee (HGNC) & UniProtKB.** *NSRP1* (`HGNC:25305`; [https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25305)) and UniProtKB `Q9H0G5` ([https://www.uniprot.org/uniprotkb/Q9H0G5](https://www.uniprot.org/uniprotkb/Q9H0G5)).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22342930` (13 mentions) - The role of hydration in protein stability: comparison of the cold and heat unfolded states of Yfh1.
  - shared terms: none

Weighed against this report's own most characteristic terms: `nsrp1`, `nedssba`, `variant`, `patient`, `clinical`, `splicing`, `genetic`, `seizure`, `severe`, `disorder`, `nuclear`, `developmental`, `nls`, `disease`, `spastic`, `brain`, `cell`, `spasticity`, `epilepsy`, `biallelic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 75 |
| Resolved | 65 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |
| Terms whose name was checked | 11 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001250` (7 mentions) - the report calls it "Seizure (Epilepsy)"; HP calls it **Seizure**, and lists "Seizures" among its other names

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `UBERON:0004720` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `UBERON:0002037` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `MGI`.

65 of 75 terms resolved to a current term; the rest could not be looked up either way.