---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T07:51:20.461479'
end_time: '2026-10-30T08:26:32.177707'
duration_seconds: 2111.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autoimmune Disease Multisystem Infantile-onset 3
  mondo_id: MONDO:0957388
  category: Mendelian
  causal_genes: CBLB
  omim_id: OMIM:620430
  synonyms: not recorded
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 17
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.033
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0005829
    reported_labels:
    - GO cellular component:** cytosol
    ontology_label: cytosol
  labels_variant: 2
  unresolved_terms:
  - HP:0001078
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autoimmune_Disease_Multisystem_Infantile-onset_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autoimmune_Disease_Multisystem_Infantile-onset_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Disease Multisystem Infantile-onset 3
- **MONDO ID:** MONDO:0957388 (if available)
- **Causal gene(s):** CBLB
- **OMIM:** OMIM:620430
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Disease Multisystem Infantile-onset 3** covering all of the
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

# Autoimmune Disease, Multisystem, Infantile-Onset, 3 (ADMIO3): A Comprehensive Disease Report

**MONDO:0957388 · OMIM:620430 · Causal gene: _CBLB_ (HGNC:1542)**

---

## Summary

**Autoimmune disease, multisystem, infantile-onset, 3 (ADMIO3)** is a rare, autosomal-recessive inborn error of immunity caused by **biallelic loss-of-function variants in _CBLB_**, the gene on chromosome 3q13.11 encoding the E3 ubiquitin ligase **CBL-B (Casitas B-lineage lymphoma proto-oncogene-b)**. The disease name is a serial number and does not itself name the gene; per the identifiers supplied, the correct causal gene is **_CBLB_**, and this report addresses that gene throughout. The disease was defined as a distinct Mendelian entity by Janssen and colleagues in 2022, who described three unrelated children with early-onset multisystem autoimmunity carrying distinct homozygous _CBLB_ mutations ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/)).

CBL-B is the central intracellular negative checkpoint of antigen-receptor signaling. By catalyzing ubiquitination of proximal signaling components (TCR-ζ, Vav1, PI3K, PKCθ/PLCγ1, CARMA1) it raises the activation threshold of lymphocytes, uncouples T-cell activation from the normal CD28 costimulation requirement, enforces T-cell anergy, and maintains sensitivity of effector T cells to regulatory-T-cell (Treg) suppression. When CBL-B catalytic (E3 ligase) function is lost on both alleles, this brake is removed: T cells hyperproliferate, resist Treg suppression, escape anergy, and B cells, NK cells and mast cells become hyperactivated — producing infantile-onset multisystem autoimmunity, sometimes with allergic features such as chronic urticaria and a predisposition to anaphylaxis.

The mechanism is strongly corroborated across species and model systems. The _Cblb_-knockout mouse spontaneously develops multi-organ autoimmunity with autoantibodies, lymphocytic tissue infiltration, IL-2 hyperproduction and high susceptibility to experimental autoimmune encephalomyelitis (EAE); a knock-in mouse bearing the orthologue of the patient p.H285L allele reproduces the human cellular phenotype; and the naturally occurring _Cblb_-nonsense-mutant Komeda diabetes-prone (KDP) rat develops autoimmune diabetes, thyroiditis and alopecia. Common hypomorphic _CBLB_ variants are, in turn, established susceptibility alleles for polygenic autoimmune diseases (multiple sclerosis, type 1 diabetes, systemic lupus erythematosus), placing ADMIO3 at the severe, monogenic pole of a CBL-B "tolerance rheostat" whose opposite pole is deliberate pharmacologic CBL-B inhibition to boost anti-tumour immunity.

---

## Key Findings

### Finding 1 — ADMIO3 is caused by biallelic loss-of-function _CBLB_ variants and presents as infantile-onset multisystem autoimmunity

The gene-defining study (Janssen et al., 2022) identified distinct homozygous _CBLB_ mutations in **3 unrelated children** with early-onset autoimmunity, one of whom also had chronic urticaria. The paper states: *"Distinct homozygous mutations in CBLB were identified in 3 unrelated children with early-onset autoimmunity, one of whom also had chronic urticaria"* and concludes that *"This study establishes CBL-B deficiency as a cause of immune dysregulation."* The three index alleles were **p.R496X** (nonsense; abolishes CBL-B expression), **p.C464W** (RING-finger; protein preserved but catalytically non-functional) and **p.H285L** (SH2/TKB domain; protein expressed at approximately half-normal level). Patient T cells hyperproliferated in response to anti-CD3 cross-linking, consistent with loss of the inhibitory brake. Inheritance is autosomal recessive. This is the primary human evidence establishing ADMIO3 ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/)).

### Finding 2 — CBL-B is an E3 ubiquitin ligase acting as the central negative checkpoint of antigen-receptor signaling; its loss drives T-cell hyperactivation and failure of anergy

CBL-B was the first E3 ubiquitin ligase directly implicated in peripheral T-cell activation and tolerance. Selective inactivation of its catalytic E3 activity causes *"T cell hyperactivation, spontaneous autoimmunity, and impaired induction of T cell anergy in vivo"* ([PMID: 21248250](https://pubmed.ncbi.nlm.nih.gov/21248250/)). CBL-B is expressed across all leukocyte subsets, and *"cblb-deficient immune cells display lower activation thresholds and cblb knockout mice spontaneously develop autoimmunity and are highly susceptible to experimental autoimmunity"* ([PMID: 25815272](https://pubmed.ncbi.nlm.nih.gov/25815272/)). Mechanistically, CBL-B normally couples T-cell-receptor (TCR) signaling to the requirement for CD28 costimulation; its loss *"frees antigen receptor-triggered receptor clustering, lipid raft aggregation, and sustained tyrosine phosphorylation from the requirement for CD28 costimulation"* ([PMID: 11070165](https://pubmed.ncbi.nlm.nih.gov/11070165/)). At the substrate level, CBL-B mediates **K33-linked polyubiquitination of TCR-ζ**, which *"affected its phosphorylation and association with the zeta chain-associated protein kinase Zap-70"* — a proteolysis-independent signaling control ([PMID: 20637659](https://pubmed.ncbi.nlm.nih.gov/20637659/)).

### Finding 3 — Patient effector T cells and a matched knock-in mouse show Treg-resistance and mast-cell hyperactivation, explaining autoimmunity plus urticaria/anaphylaxis

In Janssen 2022, a **CblbH257L knock-in mouse** (orthologous to the patient p.H285L allele) showed T- and B-cell hyperproliferation to antigen-receptor cross-linking. Although Tregs were *increased* in percentage and retained normal in-vitro suppressive function, the effector T cells were intrinsically resistant to suppression: *"T effector cells from the patient with the p.H285L mutation and CblbH257L mice were resistant to suppression by WT Tregs."* The same model linked CBL-B loss to allergic disease: *"Bone marrow-derived mast cells from CblbH257L mice were hyperactivated after FcεRI cross-linking, and CblbH257L mice demonstrated exaggerated IgE-mediated passive anaphylaxis"* ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/)). Independent work confirms the Teff-intrinsic defect: *"Cbl-b(-/-) Teffs are resistant to suppression by Tregs in vivo"* ([PMID: 20624942](https://pubmed.ncbi.nlm.nih.gov/20624942/)). This dual mechanism — Treg-resistant effector T cells plus hyperactive mast cells — accounts for both the autoimmune and the allergic (urticaria/anaphylaxis) components of the clinical picture.

### Finding 4 — Common _CBLB_ variants are established autoimmunity susceptibility alleles, situating the Mendelian disease on an allelic series

A Sardinian genome-wide association study (GWAS) linked the common _CBLB_ variant **rs9657904** to multiple sclerosis (MS) at genome-wide significance (*"rs9657904, overall P = 1.60 x 10(-10), OR = 1.40"*) ([PMID: 20453840](https://pubmed.ncbi.nlm.nih.gov/20453840/)). This was replicated in the Italian mainland (rs9657904 OR 1.31, 95% CI 1.14–1.52; [PMID: 21037273](https://pubmed.ncbi.nlm.nih.gov/21037273/)) and in a pooled Spanish cohort (rs9657904 OR 0.89; [PMID: 22194214](https://pubmed.ncbi.nlm.nih.gov/22194214/)). Mechanistically, the MS-risk SNP **rs12487066** lowers CBL-B expression: *"The MS risk-related single nucleotide polymorphism of CBLB rs12487066 is associated with diminished CBL-B expression levels and alters the effects of type I IFNs on human CD4(+) T cell proliferation"* ([PMID: 25261476](https://pubmed.ncbi.nlm.nih.gov/25261476/)). Thus common hypomorphic variants cause polygenic autoimmune risk, while biallelic null variants cause the monogenic ADMIO3 — one continuous allelic series.

### Finding 5 — _Cblb_-null mice recapitulate the human disease: spontaneous multi-organ autoimmunity

Two landmark 2000 _Nature_ papers established the mouse model. Bachmaier et al. showed that *"gene-targeted mice lacking the adaptor Cbl-b develop spontaneous autoimmunity characterized by auto-antibody production, infiltration of activated T and B lymphocytes into multiple organs, and parenchymal damage,"* and that *"Mutation of Cbl-b uncouples T-cell proliferation, interleukin-2 production and phosphorylation of the GDP/GTP exchange factor Vav1 from the requirement for CD28 co-stimulation"* ([PMID: 10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/)). Chiang et al. showed CBL-B-deficient T cells no longer need CD28 for IL-2 production, that Vav activation is enhanced, and that *"Mice deficient in Cbl-b are highly susceptible to experimental autoimmune encephalomyelitis, suggesting that the dysregulation of signalling pathways modulated by Cbl-b may also contribute to human autoimmune diseases such as multiple sclerosis"* ([PMID: 10646609](https://pubmed.ncbi.nlm.nih.gov/10646609/)).

### Finding 6 — CBL-B is a multi-lineage immune checkpoint with substrates across T, NK, NKT, B and myeloid cells

CBL-B's regulatory reach extends well beyond the TCR. Confirmed substrates and nodes include TCR-ζ (K33 polyubiquitination; [PMID: 20637659](https://pubmed.ncbi.nlm.nih.gov/20637659/)), Vav1 ([PMID: 10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/)), PKCθ and PLCγ1 ([PMID: 25000980](https://pubmed.ncbi.nlm.nih.gov/25000980/)), CARMA1 (*"Cbl-b binds and promotes monoubiquitination to CARMA1, a critical signaling molecule in NFkappaB activation"* in NKT anergy; [PMID: 19815501](https://pubmed.ncbi.nlm.nih.gov/19815501/)), and the TAM receptors in NK cells (*"The TAM tyrosine kinase receptors Tyro3, Axl and Mer... were identified as ubiquitylation substrates for Cbl-b"*; [PMID: 24553136](https://pubmed.ncbi.nlm.nih.gov/24553136/)). Because *"Cbl-b is expressed in all leukocyte subsets and regulates several signaling pathways in T cells, NK cells, B cells, and different types of myeloid cells"* ([PMID: 25815272](https://pubmed.ncbi.nlm.nih.gov/25815272/)), its loss produces genuinely multisystem disease, not just a T-cell disorder.

### Finding 7 — The Komeda diabetes-prone (KDP) rat is a naturally occurring _Cblb_-nonsense-mutant disease model

Positional cloning identified a nonsense mutation in the rat _Cblb_ gene (Iddm/kdp1) as one of two major susceptibility genes (with the MHC RT1u haplotype) for autoimmune type 1 diabetes in the KDP rat ([PMID: 15897618](https://pubmed.ncbi.nlm.nih.gov/15897618/)). Congenic transfer reconstitutes insulitis and thyroiditis ([PMID: 17259398](https://pubmed.ncbi.nlm.nih.gov/17259398/)); on a PVG.R23 background, *"The congenic rats with homozygous Cblb mutation showed autoimmune thyroiditis without T1D and slight to severe alopecia"* ([PMID: 21918539](https://pubmed.ncbi.nlm.nih.gov/21918539/)). Human _CBLB_ is likewise a T1D susceptibility locus: *"One SNP in exon 12 of the CBLB gene was significantly demonstrated to be associated to T1D in a large Danish T1D family material of 480 families"* ([PMID: 15629882](https://pubmed.ncbi.nlm.nih.gov/15629882/)).

### Finding 8 — Patient mutations map onto CBL-B's functional domains, all converging on loss of E3 ligase function

Cbl-family proteins share an N-terminal tyrosine-kinase-binding (TKB/phosphotyrosine-binding) domain, a linker helix, a zinc-coordinating RING-finger domain that carries E3 activity, and proline-rich/leucine-zipper regions; CBL-B *"retains the conserved phosphotyrosine binding domain (PTB) in the N-terminal and the zinc finger"* ([PMID: 10362357](https://pubmed.ncbi.nlm.nih.gov/10362357/)). E3 activity is autoinhibited by the TKB and linker-helix domains and relieved by tyrosine phosphorylation: *"the E3 activity of c-Cbl is negatively regulated by other domains present in the amino-terminal half of the protein (the TKB and linker helix domains) and that this negative regulation is removed when the protein is phosphorylated on tyrosine residues"* ([PMID: 15117950](https://pubmed.ncbi.nlm.nih.gov/15117950/)). The three ADMIO3 alleles thus hit three different structural modules — p.H285L (SH2/TKB), p.C464W (RING), p.R496X (truncation) — but all converge on **loss of catalytic E3 ligase function**.

### Finding 9 — ADMIO3 is the loss-of-function mirror image of a validated druggable immune checkpoint

CBL-B loss-of-function in humans causes infantile multisystem autoimmunity, whereas *pharmacologic or genetic inactivation* of CBL-B is being developed to **enhance** anti-tumour immunity: *"genetic deletion of the E3 ubiquitin ligase Cbl-b... or targeted inactivation of its E3 ligase activity licenses natural killer (NK) cells to spontaneously reject metastatic tumours"* ([PMID: 24553136](https://pubmed.ncbi.nlm.nih.gov/24553136/)), and *"the increased activation potential of cblb-deficient cells renders them more potent to fight against malignancies or infections"* ([PMID: 25815272](https://pubmed.ncbi.nlm.nih.gov/25815272/)). ADMIO3 therefore sits at one extreme of a dose/function rheostat, which has direct therapeutic implications (see §Treatment).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in _CBLB_** (nonsense p.R496X, RING-finger p.C464W, or TKB p.H285L) → **loss or catalytic inactivation of the CBL-B E3 ubiquitin ligase** in lymphocytes and myeloid cells. *(demonstrated — human; [PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/))*
2. Loss of CBL-B catalytic activity → **failure to ubiquitinate proximal antigen-receptor signaling substrates** (TCR-ζ via K33 chains, Vav1, PI3K, PKCθ, PLCγ1, CARMA1). *(demonstrated — in vitro/mouse; [PMID: 20637659](https://pubmed.ncbi.nlm.nih.gov/20637659/), [PMID: 25000980](https://pubmed.ncbi.nlm.nih.gov/25000980/), [PMID: 19815501](https://pubmed.ncbi.nlm.nih.gov/19815501/))*
3. Failure of substrate ubiquitination → **TCR signaling is uncoupled from the CD28 costimulation requirement; receptor clustering, lipid-raft aggregation and sustained tyrosine phosphorylation proceed unchecked** → lowered activation threshold. *(demonstrated — mouse; [PMID: 11070165](https://pubmed.ncbi.nlm.nih.gov/11070165/), [PMID: 10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/))*
4. Lowered activation threshold → **impaired induction/maintenance of T-cell anergy and effector T cells become resistant to Treg-mediated suppression** (despite numerically normal/increased Tregs). *(demonstrated — human + mouse; [PMID: 21248250](https://pubmed.ncbi.nlm.nih.gov/21248250/), [PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/), [PMID: 20624942](https://pubmed.ncbi.nlm.nih.gov/20624942/))*
5. **Branch A (T/B cells):** Treg-resistant, anergy-escaping lymphocytes hyperproliferate, hyperproduce IL-2, generate autoantibodies and infiltrate multiple organs → **multisystem autoimmunity**. *(demonstrated — mouse; [PMID: 10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/))*
6. **Branch B (mast cells/myeloid):** CBL-B loss hyperactivates mast cells after FcεRI cross-linking → **chronic urticaria and exaggerated IgE-mediated anaphylaxis**. *(demonstrated — mouse model of patient allele; [PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/))*
7. **Branch C (NK cells):** loss of TAM-receptor (Tyro3/Axl/Mer) ubiquitination raises NK activation — the same axis exploited therapeutically in cancer — contributing to immune dysregulation. *(inferred for human disease; demonstrated mechanism in mouse; [PMID: 24553136](https://pubmed.ncbi.nlm.nih.gov/24553136/))*
8. Convergent organ damage → **infantile-onset clinical autoimmune/inflammatory disease** (ADMIO3). *(demonstrated — human; [PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/))*

### Schematic

```
  CBLB biallelic LoF (p.R496X / p.C464W / p.H285L)
                 │
                 ▼
     Loss of CBL-B E3 ligase activity  ── upstream ──
                 │
                 ▼
  No ubiquitination of TCR-ζ, Vav1, PI3K, PKCθ, PLCγ1, CARMA1
                 │
                 ▼
  TCR signaling uncoupled from CD28; activation threshold ↓
                 │
                 ▼
  Anergy fails + effector T cells resist Treg suppression
        │               │               │
        ▼               ▼               ▼
   T/B autoimmunity   Mast-cell       NK hyperactivity
   autoantibodies,    hyperactivation  (TAM axis)
   organ infiltration (urticaria,
                      anaphylaxis)
        └───────────────┴───────────────┘
                 │  downstream
                 ▼
     Infantile-onset multisystem autoimmunity (ADMIO3)
```

### Upstream vs downstream
- **Upstream (initiating):** _CBLB_ mutation → loss of E3 ligase activity → failed substrate ubiquitination.
- **Midstream (amplifying):** lowered activation threshold, CD28-independence, anergy failure, Treg resistance.
- **Downstream (effector/clinical):** autoantibody production, multi-organ lymphocytic infiltration, mast-cell-driven allergy, tissue damage.

### Suggested ontology terms
- **Gene/protein:** _CBLB_ (HGNC:1542); CBL-B E3 ubiquitin-protein ligase (UniProt Q13191).
- **GO biological process:** protein polyubiquitination (GO:0000209); negative regulation of T cell activation (GO:0050868); T cell anergy (GO:0002870); regulation of immune response (GO:0050776); negative regulation of T cell receptor signaling pathway (GO:0050860).
- **GO cellular component:** cytosol (GO:0005829); plasma membrane (GO:0005886).
- **CL cell types:** T cell (CL:0000084), CD4-positive alpha-beta T cell (CL:0000624), regulatory T cell (CL:0000815), B cell (CL:0000236), natural killer cell (CL:0000623), mast cell (CL:0000097), dendritic cell (CL:0000451).
- **Disease:** MONDO:0957388; autoimmune disease (MONDO:0005952, parent).

---

## Anatomical Structures, Phenotypes and Temporal Profile

**Phenotypes (from the defining cohort and model systems).** The disease is a **multisystem** autoimmune/immune-dysregulation syndrome with **infantile onset** (HPO: Infantile onset, HP:0003593; Autoimmunity, HP:0002960). Reported/model-supported features include: early-onset autoimmunity (HP:0002960), chronic urticaria (HP:0001078) in at least one patient, and — by extrapolation from the _Cblb_-mutant rat and knockout mouse — organ-specific autoimmune targets such as autoimmune thyroiditis (HP:0100646), type 1 diabetes/insulitis (HP:0100651), and alopecia (HP:0001596). Laboratory hallmarks include autoantibody production (HP:0030057), lymphocyte hyperproliferation to antigen-receptor stimulation, and (in the matched mouse model) exaggerated IgE-mediated anaphylaxis and elevated Tregs with intact intrinsic suppressive function but Treg-resistant effector T cells. Because only three index patients are published, precise per-phenotype frequencies, severity grading and quality-of-life data are **not yet available** for the human disease.

**Anatomy / organ systems (UBERON).** Primary target is the **immune system** (UBERON:0002405) — peripheral lymphoid organs including spleen (UBERON:0002106) and lymph nodes (UBERON:0000029). Secondary organ involvement is inferred from model data and the multisystem designation: thyroid gland (UBERON:0002046), pancreatic islets (UBERON:0000006), skin (UBERON:0002097; urticaria, alopecia), and potentially central nervous system/white matter in the MS-analogous EAE susceptibility seen in mice (UBERON:0002316). **Subcellular:** CBL-B acts in the cytosol and at the inner plasma membrane of leukocytes; its substrates reside in the proximal antigen-receptor signalosome.

**Temporal development.** Onset is **infantile/early childhood** by definition. The limited human data describe a chronic course; model data suggest a progressive, multi-organ autoimmune evolution rather than a self-limited one. Exact progression rate, relapsing-remitting vs. progressive pattern, remission behaviour and critical intervention windows are **not established** in humans given the cohort size.

---

## Genetics, Inheritance and Population

- **Causal gene:** _CBLB_ (HGNC:1542; NCBI Gene 868; Ensembl ENSG00000114423; chromosome 3q13.11), encoding the **E3 ubiquitin-protein ligase CBL-B** (UniProt Q13191; OMIM gene 604491). Disease OMIM **620430**.
- **Index pathogenic variants (all germline, homozygous, autosomal recessive):**

| Variant (protein) | Type | Domain | Effect on CBL-B | Classification |
|---|---|---|---|---|
| p.R496X | Nonsense / truncating | Downstream of RING | Abolishes protein expression | Pathogenic (LoF) |
| p.C464W | Missense | RING finger (Zn-coordinating) | Protein preserved, E3 activity lost | Pathogenic (LoF) |
| p.H285L | Missense | SH2 / TKB (PTB) | ~50% protein, hypomorphic | Pathogenic (LoF) |

- **Functional consequence:** uniformly **loss of function** of the E3 ligase; no gain-of-function or dominant-negative mechanism described. ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/), [PMID: 15117950](https://pubmed.ncbi.nlm.nih.gov/15117950/))
- **Inheritance:** autosomal recessive; heterozygous carriers are healthy. Penetrance in biallelic carriers appears high but cannot be quantified from n = 3.
- **Allelic series / modifier context:** common hypomorphic regulatory variants (rs9657904, rs12487066, exon-12 SNP) are susceptibility alleles for MS, T1D and SLE ([PMID: 20453840](https://pubmed.ncbi.nlm.nih.gov/20453840/), [PMID: 25261476](https://pubmed.ncbi.nlm.nih.gov/25261476/), [PMID: 15629882](https://pubmed.ncbi.nlm.nih.gov/15629882/)); human CBLB genetically interacts with CTLA4 in T1D ([PMID: 15629882](https://pubmed.ncbi.nlm.nih.gov/15629882/)).
- **Epidemiology:** ADMIO3 is **ultra-rare** — only three published families to date. Prevalence/incidence, founder effects, carrier frequency, sex ratio and geographic distribution are **not established**. Consanguinity is a plausible contributor given homozygosity but was not systematically reported.

---

## Diagnostics

- **Genetic testing is the definitive diagnostic modality:** whole-exome or whole-genome sequencing, or a comprehensive inborn-errors-of-immunity (IEI) gene panel that includes _CBLB_, with confirmation of **biallelic** pathogenic variants. Single-gene _CBLB_ sequencing is appropriate when the phenotype is highly suggestive or a familial variant is known.
- **Supportive immunologic workup:** autoantibody panels (autoimmunity screen), total/specific IgE (given urticaria/anaphylaxis risk), and functional assays showing **T-cell hyperproliferation to anti-CD3/anti-CD28 cross-linking** and **effector-T-cell resistance to Treg suppression** — the laboratory signatures demonstrated in patients and the matched mouse ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/)).
- **Differential diagnosis:** other monogenic immune-dysregulation/IPEX-like disorders (FOXP3, CTLA4 haploinsufficiency, LRBA deficiency, STAT1/STAT3 GOF), and the other "autoimmune disease, multisystem, infantile-onset" entities (types 1 and 2, different genes). The _CBLB_ genotype distinguishes ADMIO3.

---

## Treatment and Prevention

No ADMIO3-specific approved therapy or clinical trial exists; management is extrapolated from immune-dysregulation principles and the mechanism.

- **Mechanism-guided rationale:** because the lesion removes the inhibitory brake and renders effector T cells **CD28-costimulation-independent** and **Treg-resistant**, rational therapy aims to **restore inhibitory tone**. Candidate approaches include **CTLA4-Ig / abatacept** (NCIT: Abatacept, C47384) to re-impose the costimulation brake, and **mTOR inhibition (sirolimus/rapamycin; NCIT: Sirolimus, C1212)** — supported indirectly by SLE studies where rapamycin plus vitamin D restored Treg-related anergy factors ([PMID: 25351606](https://pubmed.ncbi.nlm.nih.gov/25351606/)). Standard immunosuppression (corticosteroids, calcineurin inhibitors) and allergy management (antihistamines, anti-IgE for mast-cell features) are reasonable symptomatic measures. ([PMID: 36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/))
- **Therapeutic inversion / caution:** ADMIO3 is the **loss-of-function mirror** of oncology CBL-B **inhibitors** developed to boost anti-tumour T/NK immunity ([PMID: 24553136](https://pubmed.ncbi.nlm.nih.gov/24553136/), [PMID: 25815272](https://pubmed.ncbi.nlm.nih.gov/25815272/)); CBL-B agonism/restoration is the conceptual therapeutic direction for the disease, and CBL-B inhibitors are strictly contraindicated.
- **Prevention/counseling:** autosomal-recessive genetic counseling, carrier testing of relatives, and prenatal/preimplantation options where a familial variant is known. No primary prevention beyond reproductive counseling is applicable to a monogenic disorder.

---

## Model Organisms and Comparative Biology

| Model | Lesion | Key phenotype | PMID |
|---|---|---|---|
| _Cblb_−/− mouse (knockout) | Full null | Spontaneous multi-organ autoimmunity, autoantibodies, IL-2 hyperproduction, CD28-independence, EAE susceptibility | [10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/), [10646609](https://pubmed.ncbi.nlm.nih.gov/10646609/) |
| _CblbH257L_ knock-in mouse | Orthologue of patient p.H285L | T/B hyperproliferation; Treg-resistant effector T cells; mast-cell hyperactivation; exaggerated IgE anaphylaxis | [36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/) |
| Catalytic-dead (E3-inactive) mouse | RING inactivation | T-cell hyperactivation, spontaneous autoimmunity, impaired anergy | [21248250](https://pubmed.ncbi.nlm.nih.gov/21248250/) |
| Komeda diabetes-prone (KDP) rat | Natural _Cblb_ nonsense | Autoimmune T1D, thyroiditis, alopecia (with MHC RT1u) | [15897618](https://pubmed.ncbi.nlm.nih.gov/15897618/), [21918539](https://pubmed.ncbi.nlm.nih.gov/21918539/) |

**Orthologues:** mouse _Cblb_ (NCBI Gene 208650), rat _Cblb_ (NCBI Gene 171109). Disease mechanisms are **evolutionarily conserved** across human, mouse and rat, and the KDP rat represents a **naturally occurring** animal disease of veterinary/comparative interest (OMIA relevance). Phenotype recapitulation is strong for the core immune-dysregulation and multi-organ autoimmunity; model limitations include species differences in which organs are preferentially targeted and the small human dataset against which to benchmark.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [36006710](https://pubmed.ncbi.nlm.nih.gov/36006710/) | *Immune dysregulation caused by homozygous mutations in CBLB* | Human clinical + matched mouse | **Gene-defining** study; variants, Treg-resistance, mast-cell phenotype |
| [21248250](https://pubmed.ncbi.nlm.nih.gov/21248250/) | *Essential role of E3 ligase activity in Cbl-b-regulated T cell functions* | Mouse | E3 activity required to prevent autoimmunity/anergy failure |
| [11070165](https://pubmed.ncbi.nlm.nih.gov/11070165/) | *Cbl-b is a negative regulator of receptor clustering...* | Mouse/in vitro | CD28-independence mechanism |
| [20637659](https://pubmed.ncbi.nlm.nih.gov/20637659/) | *K33-linked polyubiquitination of TCR-ζ...* | In vitro | Molecular substrate (TCR-ζ) |
| [20624942](https://pubmed.ncbi.nlm.nih.gov/20624942/) | *Cbl-b(-/-) T cells resistant to Tregs...* | Mouse | Independent confirmation of Treg resistance |
| [10646608](https://pubmed.ncbi.nlm.nih.gov/10646608/) | *Negative regulation of lymphocyte activation... Cbl-b* | Mouse | Knockout multisystem autoimmunity; Vav1/CD28 |
| [10646609](https://pubmed.ncbi.nlm.nih.gov/10646609/) | *Cbl-b regulates the CD28 dependence of T-cell activation* | Mouse | EAE susceptibility; MS relevance |
| [25815272](https://pubmed.ncbi.nlm.nih.gov/25815272/) | *Modulation of Immune Cell Functions by the E3 Ligase Cbl-b* | Review | Multi-lineage expression; rheostat framing |
| [24553136](https://pubmed.ncbi.nlm.nih.gov/24553136/) | *Cbl-b and TAM receptors regulate cancer metastasis via NK cells* | Mouse | NK substrates; therapeutic inverse |
| [19815501](https://pubmed.ncbi.nlm.nih.gov/19815501/) | *Cbl-b monoubiquitination of CARMA1 in NKT anergy* | Mouse/in vitro | CARMA1/NF-κB node |
| [25000980](https://pubmed.ncbi.nlm.nih.gov/25000980/) | *Deltex1 / PKCθ / Cbl-b in anergy* | In vitro | PKCθ, PLCγ1 substrates |
| [20453840](https://pubmed.ncbi.nlm.nih.gov/20453840/) | *CBLB variants associated with MS* | Human GWAS | Common-variant autoimmunity risk |
| [21037273](https://pubmed.ncbi.nlm.nih.gov/21037273/) | *CBLB–MS replication (Italy)* | Human | Replication |
| [22194214](https://pubmed.ncbi.nlm.nih.gov/22194214/) | *CBLB–MS replication (Spain)* | Human | Replication |
| [25261476](https://pubmed.ncbi.nlm.nih.gov/25261476/) | *MS-associated CBLB variant links to type I IFN* | Human/in vitro | Mechanism of risk allele |
| [15897618](https://pubmed.ncbi.nlm.nih.gov/15897618/) | *Major gene for T1D in KDP rat* | Rat | Natural Cblb-mutant model |
| [21918539](https://pubmed.ncbi.nlm.nih.gov/21918539/) | *MHC II in rat autoimmune diabetes/thyroiditis* | Rat | Organ-specific autoimmunity |
| [17259398](https://pubmed.ncbi.nlm.nih.gov/17259398/) | *Genetic reconstitution of T1D in rat* | Rat | Two-gene model confirmation |
| [15629882](https://pubmed.ncbi.nlm.nih.gov/15629882/) | *CBLB variants in T1D; interaction with CTLA4* | Human | Human T1D susceptibility |
| [15117950](https://pubmed.ncbi.nlm.nih.gov/15117950/) | *Regulation of c-Cbl ligase activity* | In vitro/structural | Domain autoinhibition relevant to variants |
| [10362357](https://pubmed.ncbi.nlm.nih.gov/10362357/) | *cbl-3: a new mammalian cbl family protein* | In vitro | Domain architecture (TKB/RING) |

A consistent caveat: much of the mechanistic literature uses the common gene synonym **_Cbl-b_/Casitas B-lineage lymphoma-b** rather than the formal symbol **_CBLB_**, and several SLE/MS papers describe *common-variant* or *acquired* CBL-B reduction rather than the biallelic null of ADMIO3. These support the mechanism but are not direct observations of the Mendelian disease.

---

## Limitations and Knowledge Gaps

1. **Tiny human cohort (n = 3).** All firm human clinical claims rest on a single 2022 report. Penetrance, expressivity, full phenotypic spectrum, per-phenotype frequencies, severity distribution, natural history, prognosis and quality-of-life metrics are **unknown**.
2. **Epidemiology is unquantified.** No prevalence, incidence, carrier frequency, founder-effect, geographic or sex-ratio data exist for ADMIO3.
3. **No disease-specific treatment evidence.** Therapeutic suggestions (abatacept/CTLA4-Ig, mTOR inhibition) are mechanistic extrapolations, not trial-tested in ADMIO3.
4. **Organ-specificity extrapolation.** Thyroiditis, diabetes and alopecia are prominent in rat/mouse models; the exact organ distribution in human ADMIO3 is not yet mapped.
5. **Human NK/mast-cell contribution.** The mast-cell and NK/TAM branches are demonstrated in mice; their precise contribution to human clinical disease is inferred.
6. **Nomenclature hazard.** The serial-number disease name does not encode the gene; literature mixes _CBLB_, _Cbl-b_, and common-variant studies — care is needed to avoid conflating hypomorphic-risk-allele biology with the biallelic-null Mendelian disease.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry** via GeneMatcher/collaborative IEI networks to define phenotype frequencies, penetrance, natural history and genotype–phenotype correlations across the three index-allele classes (null vs. RING vs. TKB hypomorph).
2. **Deep immunophenotyping** of patients: standardized Treg-suppression assays, TCR-signaling thresholds, FcεRI-driven mast-cell/basophil activation tests, NK-cell TAM-axis function — to confirm which mouse-derived branches operate in humans.
3. **Variant functional characterization** in patient iPSC-derived or primary T cells with isogenic correction, quantifying E3 ligase activity and substrate (TCR-ζ, Vav1, CARMA1) ubiquitination per allele.
4. **Therapeutic proof-of-concept**: test abatacept/CTLA4-Ig and mTOR inhibition in the _CblbH257L_ knock-in mouse for autoimmunity and anaphylaxis endpoints, as the preclinical bridge to compassionate-use human trials.
5. **Prognostic biomarker discovery**: longitudinal autoantibody, cytokine (IL-2) and Treg-resistance profiling to predict organ-specific flares.
6. **Carrier/population screening analysis** of gnomAD for biallelic-compatible _CBLB_ LoF burden to estimate disease frequency and inform counseling.

---

## Consensus Answer

Autoimmune disease, multisystem, infantile-onset, 3 (ADMIO3; OMIM 620430; MONDO:0957388) is a rare autosomal-recessive inborn error of immunity caused by **biallelic loss-of-function variants in _CBLB_**, encoding the E3 ubiquitin ligase CBL-B — the central negative checkpoint that ubiquitinates proximal antigen-receptor signaling components to raise lymphocyte activation thresholds and enforce peripheral tolerance. Loss of CBL-B catalytic activity lowers the activation threshold, uncouples T-cell activation from CD28 costimulation, impairs anergy, and renders effector T cells resistant to Treg suppression while hyperactivating B, NK and mast cells, producing infantile-onset multisystem autoimmunity (including allergic features such as chronic urticaria); the mechanism is corroborated by _Cblb_-knockout/knock-in mice and the naturally _Cblb_-mutant Komeda diabetes-prone rat.


## Artifacts

- [OpenScientist final report](Autoimmune_Disease_Multisystem_Infantile-onset_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autoimmune_Disease_Multisystem_Infantile-onset_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005829` (1 mention) - the report calls it "GO cellular component:** cytosol"; GO calls it **cytosol**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001078` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0000209` (1 mention) - the report calls it "GO biological process:** protein polyubiquitination"; GO calls it **protein polyubiquitination**
- `CL:0000084` (1 mention) - the report calls it "CL cell types:** T cell"; CL calls it **T cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.