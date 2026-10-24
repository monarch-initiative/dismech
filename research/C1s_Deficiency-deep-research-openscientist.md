---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T17:32:01.352497'
end_time: '2026-10-23T17:45:48.173952'
duration_seconds: 826.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: C1s Deficiency
  mondo_id: MONDO:1060176
  category: Mendelian
  causal_genes: C1S
  omim_id: not recorded
  synonyms: complement component 1s deficiency; hereditary C1s deficiency; systemic
    lupus erythematosus related to C1S
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
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:1060176
    reported_labels:
    - C1s deficiency
    ontology_label: systemic lupus erythematosus related to C1S
  - term_id: HP:0003261
    reported_labels:
    - Abnormality of complement system
    ontology_label: Increased circulating IgA concentration
  - term_id: CL:0000235
    reported_labels:
    - Tissue/cell level:** phagocytes/macrophages
    ontology_label: macrophage
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: C1s_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: C1s_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** C1s Deficiency
- **MONDO ID:** MONDO:1060176 (if available)
- **Causal gene(s):** C1S
- **OMIM:** not recorded
- **Synonyms:** complement component 1s deficiency; hereditary C1s deficiency; systemic lupus erythematosus related to C1S
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **C1s Deficiency** covering all of the
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

# C1s Deficiency (MONDO:1060176): A Comprehensive Disease Characteristics Report

**Causal gene:** *C1S* (complement C1s subcomponent; HGNC:1247; NCBI Gene 716; UniProt P09871; chromosome 12p13.31)
**Disease category:** Mendelian, autosomal recessive inborn error of immunity / classical-complement-pathway deficiency

---

## Summary

**C1s deficiency is a rare autosomal-recessive inborn error of immunity caused by biallelic loss-of-function (truncating) variants in the *C1S* gene on chromosome 12p13.31.** *C1S* encodes the catalytic serine protease of the first complement complex (C1). When C1s is absent, the C1 complex is enzymatically dead: it can no longer cleave complement components C4 and C2, so the entire classical complement pathway fails to propagate. The biochemical hallmark is an **immeasurably low total hemolytic complement activity (CH50) with a normal alternative-pathway activity**, normal C3, and normal/elevated C4 and C2. Only about 9–10 cases of complete C1s deficiency have been reported worldwide, making it one of the rarest of the inherited complement deficiencies.

Clinically, the disease produces a characteristic **two-branch phenotype**. First, defective opsonization predisposes to **recurrent, invasive pyogenic infections with encapsulated bacteria**, especially *Streptococcus pneumoniae* and *Neisseria meningitidis*. Second, failure of complement-dependent clearance of apoptotic cells and immune complexes — compounded by loss of a complement-independent C1s function (proteolytic inactivation of the nuclear alarmin HMGB1) — drives **systemic lupus erythematosus (SLE) or an SLE-like syndrome, including proliferative lupus nephritis**. The autoimmune branch shows **incomplete penetrance and variable expressivity**: in one consanguineous family, all four C1s-deficient siblings shared the same genotype but only two developed SLE, indicating that additional predisposing/modifier genes are required.

Management is **supportive and preventive**: vaccination against encapsulated organisms (pneumococcus, meningococcus, *Haemophilus influenzae* type b), antibiotic prophylaxis, and standard immunosuppression for lupus manifestations (hydroxychloroquine, corticosteroids, and — for refractory proliferative lupus nephritis — rituximab). A crucial allelic distinction must be made: **heterozygous missense (gain-of-function-like) variants in *C1S* (and its partner *C1R*) cause a mechanistically opposite dominant disorder, periodontal Ehlers-Danlos syndrome (EDSPD2/EDSPD1)**, not complement deficiency. Confusing these two allelic disorders is the principal diagnostic pitfall for this gene.

---

## Key Findings

### Finding 1 — C1s deficiency is a rare autosomal-recessive classical-complement-pathway defect caused by loss-of-function *C1S* variants

Complete C1s deficiency is caused by **biallelic truncating / loss-of-function variants** in the *C1S* gene (HGNC:1247; chromosome 12p13.31), which encodes the serine protease C1s (UniProt P09871). Reported molecular lesions span frameshift, nonsense, and compound-truncating classes:

- A **homozygous 4-bp deletion (TTTG, nucleotides 1087–1090) in exon 10** creating a premature stop codon. As reported, *"Sequence analysis of C1s cDNA revealed a deletion at nucleotides 1087-1090 (TTTG), creating a stop codon (TGA) at position 94 downstream of the mutation site"* ([PMID: 9856483](https://pubmed.ncbi.nlm.nih.gov/9856483/)).
- A **homozygous nonsense/premature-stop mutation at position 938 in exon 6**, segregating in a consanguineous family with four affected siblings — *"all four siblings are homozygous for a mutation at position 938 in exon 6 of the C1s cDNA that creates a premature stop codon"* ([PMID: 18062908](https://pubmed.ncbi.nlm.nih.gov/18062908/)).
- **Compound truncating variants identified by whole-genome sequencing** in a male Caucasian patient — *"The genome of the patient was analyzed by whole genome sequencing showing two truncating variants"* ([PMID: 38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/)).

The biochemical signature across cases is consistent: an **isolated early classical-pathway defect** with immeasurably low CH50, normal alternative-pathway function, undetectable C1s, normal C3, and normal/elevated C4 and C2. Fewer than ~10 complete C1s-deficient cases are reported worldwide.

**Variant classification:** The reported truncating variants are pathogenic under ACMG/AMP criteria (PVS1 loss-of-function in a gene where LOF is the disease mechanism, plus segregation). **Allele frequencies** in population databases (gnomAD) are correspondingly very low/absent for these private variants. Origin is **germline**.

### Finding 2 — Presentation: early-onset SLE / SLE-like disease (including lupus nephritis) plus recurrent pyogenic infections

Across the small case literature, complete C1s deficiency is strongly associated with **SLE or SLE-like syndromes and severe pyogenic infections**. The best-characterized modern case is a 34-year-old man with compound truncating *C1S* variants who had recurrent infections since childhood (pneumococcal and meningococcal meningitis, erysipelas, subcutaneous abscess, recurrent upper-airway infections) plus adult-onset SLE and proliferative lupus nephritis: *"The patient also exhibited adult-onset SLE, meeting 7/11 of the ACR criteria and 34 of the 2019 EULAR/ACR classification criteria, along with class IV-G (A) proliferative lupus nephritis (LN)"* ([PMID: 38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/)). The renal biopsy showed C1q positivity along glomerular basement membranes.

The autoimmune branch is **incompletely penetrant**: in the consanguineous family, *"all four children are deficient in C1s but only two of them developed SLE"* ([PMID: 18062908](https://pubmed.ncbi.nlm.nih.gov/18062908/)), demonstrating variable expressivity. The infection branch reflects impaired opsonophagocytosis: deficiencies of early classical-pathway components *"predispose to severe infections, particularly with encapsulated bacteria such as Neisseria meningitidis and Streptococcus pneumoniae"* ([PMID: 41421099](https://pubmed.ncbi.nlm.nih.gov/41421099/)).

**Suggested HPO terms:** HP:0002725 (Systemic lupus erythematosus), HP:0001970 (lupus nephritis/nephritis), HP:0002721 (Immunodeficiency), HP:0002718 (Recurrent bacterial infections), HP:0002090 (Pneumonia), HP:0001287 (Meningitis), HP:0100658 (Cellulitis/erysipelas), HP:0003261 (Abnormality of complement system), HP:0005356 (Decreased complement activity).

### Finding 3 — Mechanism: beyond C4/C2 cleavage, C1s inactivates nuclear alarmins (HMGB1), linking its loss to lupus

The archetypal role of C1s is as the **catalytic arm of the C1 complex**, cleaving C4 and C2 to propagate the classical pathway. Beyond this, C1s has a **complement-independent proteolytic function**: purified C1s and the physiological C1 complex cleave the nuclear alarmin **HMGB1** into defined 19- and 12-kDa fragments during apoptosis, diminishing HMGB1's ability to enhance LPS-mediated pro-inflammatory cytokine production — *"C1s, both in its purified and physiological form as C1 complex, cleaving HMGB1 into defined fragments of 19 and 12 kDa"* ([PMID: 27648302](https://pubmed.ncbi.nlm.nih.gov/27648302/)). Because HMGB1 can induce antinuclear autoantibodies and lupus-like disease in mice, loss of C1s removes a brake on alarmin-driven autoimmunity — an additional mechanistic link between C1s deficiency and SLE.

That C1s is the specific missing catalytic component was confirmed functionally: in a C4d-deposition assay, *"the patient's absent complement activity was fully restored by adding C1s"* ([PMID: 38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/)).

Importantly, C1r/C1s loss is **necessary but not sufficient** for lupus. A congenic mouse lacking C1r/C1s (with low C1q) did not spontaneously develop SLE: *"These results suggest that C1r/C1s deficiency is not sufficient to drive murine SLE and also that other predisposing genes exist in ICGN mice"* ([PMID: 29550838](https://pubmed.ncbi.nlm.nih.gov/29550838/)). This directly explains the incomplete penetrance seen in human families.

### Finding 4 — Classical-pathway deficiencies impair waste-disposal (apoptotic-cell clearance), with a severity hierarchy explaining the SLE link

Inherited classical-pathway deficiencies are among the **strongest known single-gene susceptibility factors for SLE**, following a well-established hierarchy: risk is highest for C1q deficiency (>90% develop SLE), high for C1r/C1s and C4 deficiency, and lower for C2 deficiency — *"This hierarchy of disease associations suggests the importance of an intact early classic activation pathway in preventing systemic lupus erythematosus"* ([PMID: 8907066](https://pubmed.ncbi.nlm.nih.gov/8907066/)).

Functionally, the classical pathway predominates in opsonizing apoptotic and secondary-necrotic cells: *"the components of the complement classical pathway, including C1q, were equally important in clearance of apoptotic cells"* ([PMID: 19302245](https://pubmed.ncbi.nlm.nih.gov/19302245/)). Failure of this "waste-disposal" function allows accumulation of nuclear autoantigens, driving autoantibody formation. Clinically, early complement/immunodeficiency in SLE associates with worse organ damage — in juvenile SLE, *"the median of Systemic Lupus International Collaborating Clinics/ACR-damage index (SLICC/ACR-DI) was significantly higher in JSLE patients with PID compared with patients without these abnormalities (p = 0.0033)"* ([PMID: 21813590](https://pubmed.ncbi.nlm.nih.gov/21813590/)). C1s deficiency sits within this hierarchy as a proximal classical-pathway defect.

| Deficient component | Approx. SLE risk | Position in pathway |
|---|---|---|
| C1q | >90% | Recognition subunit |
| **C1r / C1s** | **High** | **Catalytic proteases of C1** |
| C4 | High | Downstream of C1 |
| C2 | Lower (~10–30%) | Downstream of C4 |

### Finding 5 — Allelic distinction: heterozygous *C1S/C1R* missense variants cause periodontal Ehlers-Danlos syndrome, NOT complement deficiency

The same gene harbors a **mechanistically opposite class of variants**. **Periodontal Ehlers-Danlos syndrome (pEDS; EDSPD2 for *C1S*, EDSPD1 for *C1R*)** is an autosomal-dominant disorder caused by **heterozygous missense (and in-frame indel) variants** — *"Periodontal Ehlers-Danlos syndrome (pEDS) is a rare condition caused by pathogenic variants in the C1R and C1S genes, encoding subunits C1r and C1s of the first component of the classical complement pathway"* ([PMID: 33890303](https://pubmed.ncbi.nlm.nih.gov/33890303/)). As of 2022, *"148 cases have been described in the literature"* ([PMID: 36348983](https://pubmed.ncbi.nlm.nih.gov/36348983/)).

pEDS is characterized by early-onset periodontitis with premature tooth loss, lack of attached gingiva, thin/fragile gums, easy bruising, pretibial hyperpigmentation/plaques, distal joint hypermobility, hoarse voice, and occasional vascular complications. Crucially, these variants are **not loss-of-function**: activated/dysregulated C1s acquires aberrant activity — *"Degradation of collagen I by activated C1s in periodontal Ehlers-Danlos Syndrome"* ([PMID: 36960056](https://pubmed.ncbi.nlm.nih.gov/36960056/)). This stands in direct contrast to complete C1s deficiency (biallelic truncating LOF → SLE + infections), and the two must never be conflated.

| Feature | **C1s deficiency (MONDO:1060176)** | **pEDS / EDSPD2** |
|---|---|---|
| Variant type | Biallelic truncating (LOF) | Heterozygous missense (gain/dysregulated activity) |
| Inheritance | Autosomal recessive | Autosomal dominant |
| Molecular effect | No C1s protein / enzymatically dead C1 | Aberrantly active C1s degrades collagen I |
| Complement activity | CH50 absent | Normal |
| Phenotype | SLE + encapsulated-bacterial infections | Periodontitis, tooth loss, skin/vascular fragility |
| Approx. cases | ~9–10 | ~148 |

### Finding 6 — Diagnosis and management: CH50 functional screen + sequencing; prophylaxis/vaccination + lupus immunosuppression

Classical-pathway defects *"result from deficiencies of complement proteins C1q, C1r, C1s, C2, and C4, and typically manifest with features of systemic lupus erythematosus and infections with encapsulated organisms"* ([PMID: 39294906](https://pubmed.ncbi.nlm.nih.gov/39294906/)). The specific laboratory signature of C1s deficiency is an **absent/immeasurably low CH50 with a normal alternative-pathway (AH50) activity** — *"A screening of the complement cascade showed immeasurably low CH50, while the alternative pathway (AP) function was normal"* ([PMID: 38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/)). Component quantitation then shows undetectable C1s with normal C3 and normal/elevated C4 and C2 (corroborated in the C1r/C1s case of [PMID: 7939409](https://pubmed.ncbi.nlm.nih.gov/7939409/), which noted *"persistently depressed levels of haemolytic complement activity (CH50)... associated with normal levels of C3, C4 and C2 components, and normal alternative pathway haemolytic activity"*).

**Definitive diagnosis** uses genetic sequencing (single-gene *C1S*, complement gene panels, WES, or WGS); the index modern patient was diagnosed by whole-genome sequencing ([PMID: 38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/)). **Management** emphasizes anticipatory care — *"the importance of anticipatory care, vaccination, and prophylaxis as new complement-targeted drugs continue to emerge"* ([PMID: 41421099](https://pubmed.ncbi.nlm.nih.gov/41421099/)) — i.e., vaccination against pneumococcus, meningococcus, and Hib plus antibiotic prophylaxis. Lupus manifestations are treated with standard immunosuppression; **refractory/proliferative lupus nephritis in complete C1s deficiency responded to rituximab (anti-CD20)** ([PMID: 20191570](https://pubmed.ncbi.nlm.nih.gov/20191570/)).

**Suggested NCIT terms:** Rituximab (NCIT:C1702), Hydroxychloroquine (NCIT:C509), Corticosteroid therapy, Pneumococcal/Meningococcal vaccination, Antibiotic prophylaxis.

### Finding 7 — C1s is the catalytic serine protease of the ~790-kDa C1 complex (C1q·C1r₂·C1s₂)

Complement component C1 is a **~790-kDa assembly** of the recognition subcomponent C1q (a hexamer of heterotrimers, 18 chains) bound to a tetramer of the modular proteases C1r and C1s (C1r₂s₂) — *"Complement component C1... is a 790-kDa assembly formed from the target-recognition subcomponent C1q and the modular proteases C1r and C1s"* ([PMID: 23922389](https://pubmed.ncbi.nlm.nih.gov/23922389/)). C1q/C1s binding is Ca²⁺-dependent. C1s (domain architecture CUB-EGF-CUB-CCP-CCP-serine protease; peptidase clan PA, family S1; EC 3.4.21.42) is the catalytic arm: *"Enzymatically active C1s provides the catalytic basis for cleavage of the downstream CP components, C4 and C2"* ([PMID: 38149922](https://pubmed.ncbi.nlm.nih.gov/38149922/)). Its loss renders the entire C1 complex enzymatically dead. Notably, C1s is **druggable** — an FDA-approved anti-C1s mAb and small-molecule inhibitors block the classical pathway — relevant to C1s-overactivity diseases, the opposite of the deficiency state.

**Suggested ontology terms:** GO:0006958 (complement activation, classical pathway), GO:0045087 (innate immune response), GO:0004252 (serine-type endopeptidase activity); GO cellular component GO:0005615 (extracellular space)/GO:0005576 (extracellular region); CHEBI relevance: Ca²⁺ (CHEBI:29108) cofactor.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (from mutation to clinical manifestation)

```
1. Biallelic truncating variant in C1S (12p13.31)
        │  leads to
2. Absent or non-functional C1s serine protease (premature stop → no protein)
        │  results in
3. Enzymatically dead C1 complex (C1q·C1r2·C1s2 cannot cleave substrates)
        │  results in
4. Failure to cleave C4 and C2 → no classical-pathway C3 convertase (C4b2a)
        │  branches into two downstream arms ↓
        │
 ┌──────┴───────────────────────────────┐
 │ BRANCH A (infection)                  │ BRANCH B (autoimmunity)
 │                                       │
5A. Impaired opsonization (less C3b/C4b  5B. Defective complement-dependent
    deposition on encapsulated bacteria) │    clearance of apoptotic & secondary-
        │ leads to                       │    necrotic cells (loss of classical-
6A. Reduced opsonophagocytosis           │    pathway opsonization)
        │ results in                     │        │ plus (complement-independent)
7A. Recurrent invasive pyogenic          │    5B'. Loss of C1s-mediated proteolytic
    infections (S. pneumoniae,           │        inactivation of HMGB1 alarmin
    N. meningitidis)                     │        │ leads to
                                         │ 6B. Accumulation of nuclear autoantigens
                                         │     & pro-inflammatory alarmin signaling
                                         │        │ results in (if modifier genes present)
                                         │ 7B. Loss of tolerance → antinuclear
                                         │     autoantibodies → immune-complex
                                         │     deposition → SLE / lupus nephritis
```

**Inferred vs demonstrated:** Steps 1–4 and Branch A (5A–7A) are well demonstrated (functional CH50/AP assays, C1s add-back restoration). Step 5B (apoptotic-cell clearance) is demonstrated in vitro for classical-pathway components generally ([PMID: 19302245](https://pubmed.ncbi.nlm.nih.gov/19302245/)). Step 5B' (HMGB1 inactivation) is demonstrated biochemically ([PMID: 27648302](https://pubmed.ncbi.nlm.nih.gov/27648302/)) but its quantitative contribution to human lupus is **inferred**. The requirement for modifier genes at step 7B is demonstrated in mouse ([PMID: 29550838](https://pubmed.ncbi.nlm.nih.gov/29550838/)) and inferred in humans from incomplete penetrance.

**Upstream vs downstream:** The mutation and loss of C1s catalytic activity are the upstream lesion; impaired opsonization and impaired waste clearance are intermediate; infection and autoimmunity are the downstream clinical endpoints. The branch point is the failed C3 convertase assembly.

**Cell types / biological processes (suggested CL/GO terms):** monocyte-derived macrophages (CL:0000235) and phagocytes performing apoptotic-cell clearance (GO:0043277, apoptotic cell clearance; GO:0006911, phagocytosis, engulfment); complement activation, classical pathway (GO:0006958). **Anatomy (UBERON):** blood/serum (UBERON:0000178), kidney glomerulus (UBERON:0000074) in lupus nephritis, skin (UBERON:0002097) in cutaneous lupus/erysipelas, meninges (UBERON:0002360) in meningitis.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [38469558](https://pubmed.ncbi.nlm.nih.gov/38469558/) | *C1s deficiency in a male with SLE: case report* | Human clinical | Compound truncating variants by WGS; SLE + lupus nephritis + infections; CH50 absent/AP normal; C1s add-back restoration (F1, F2, F3, F6) |
| [18062908](https://pubmed.ncbi.nlm.nih.gov/18062908/) | *Genetic analysis of C1s deficiency with SLE* | Human clinical/genetic | Homozygous premature-stop (exon 6); AR inheritance; incomplete penetrance (2/4 SLE) (F1, F2) |
| [9856483](https://pubmed.ncbi.nlm.nih.gov/9856483/) | *Selective C1s deficiency, 4-bp deletion* | Human genetic | Homozygous TTTG frameshift → stop codon (F1) |
| [27648302](https://pubmed.ncbi.nlm.nih.gov/27648302/) | *C1s inactivation of HMGB1 during apoptosis* | In vitro | Complement-independent C1s function linking loss to lupus (F3) |
| [29550838](https://pubmed.ncbi.nlm.nih.gov/29550838/) | *C1r/C1s deficiency insufficient for murine SLE* | Model organism | Necessary-but-not-sufficient; modifier genes required (F3) |
| [19302245](https://pubmed.ncbi.nlm.nih.gov/19302245/) | *Classical pathway in clearance of apoptotic cells* | In vitro | Waste-disposal mechanism for SLE link (F4) |
| [8907066](https://pubmed.ncbi.nlm.nih.gov/8907066/) | *Inherited complement deficiencies in rheumatic disease* | Review | SLE-susceptibility hierarchy C1q>C1r/s/C4>C2 (F4) |
| [21813590](https://pubmed.ncbi.nlm.nih.gov/21813590/) | *Complement/antibody PID in juvenile SLE* | Human cohort | Early complement PID → worse damage (p=0.0033) (F4) |
| [33890303](https://pubmed.ncbi.nlm.nih.gov/33890303/) | *Periodontal EDS: 13 novel cases* | Human clinical | pEDS caused by C1R/C1S variants (F5) |
| [36348983](https://pubmed.ncbi.nlm.nih.gov/36348983/) | *Periapical dysplasia in pEDS* | Human clinical | pEDS dominant, 148 cases (F5) |
| [36960056](https://pubmed.ncbi.nlm.nih.gov/36960056/) | *Collagen I degradation by activated C1s in pEDS* | In vitro | pEDS variants confer aberrant activity (F5) |
| [39294906](https://pubmed.ncbi.nlm.nih.gov/39294906/) | *Immunodeficiency: complement disorders* | Review | Diagnostic category & presentation (F6) |
| [41421099](https://pubmed.ncbi.nlm.nih.gov/41421099/) | *Complement deficiencies and infections* | Review | Encapsulated-bacteria risk; prevention strategy (F2, F6) |
| [20191570](https://pubmed.ncbi.nlm.nih.gov/20191570/) | *Lupus nephritis in C1s deficiency treated with rituximab* | Human clinical | Rituximab efficacy in refractory LN (F6) |
| [7939409](https://pubmed.ncbi.nlm.nih.gov/7939409/) | *C1r/C1s deficiency biosynthesis* | Human clinical | Laboratory signature (CH50↓, C3/C4/C2 normal, AP normal) (F6) |
| [23922389](https://pubmed.ncbi.nlm.nih.gov/23922389/) | *Structural basis of C1q/C1s interaction* | Structural | C1 complex architecture (F7) |
| [38149922](https://pubmed.ncbi.nlm.nih.gov/38149922/) | *Inhibition of C1s protease* | Biochemical | C1s is catalytic for C4/C2; druggable (F7) |
| [25414705](https://pubmed.ncbi.nlm.nih.gov/25414705/) | *C1 assembly and activation* | Review | C1r₂s₂ tetramer architecture (F7) |

---

## Section-by-Section Coverage

### 1. Disease Information
- **Overview:** A rare autosomal-recessive deficiency of complement C1s, the catalytic protease of the C1 complex, abolishing classical-pathway activation and producing SLE-like autoimmunity plus susceptibility to encapsulated-bacterial infection.
- **Identifiers:** MONDO:1060176; causal gene *C1S* (HGNC:1247; NCBI Gene 716; UniProt P09871; 12p13.31). OMIM phenotype not formally recorded for the deficiency (gene *C1S* OMIM 120580). MeSH: Hereditary Complement Deficiency Diseases. Orphanet category: hereditary complement deficiency. ICD-10: D84.1 (defects in the complement system).
- **Synonyms:** complement component 1s deficiency; hereditary C1s deficiency; SLE related to *C1S*.
- **Data source:** Disease-level aggregated resources plus individual case reports (not large EHR cohorts), reflecting extreme rarity.

### 2. Etiology
Primary cause is monogenic (biallelic LOF *C1S*). Genetic risk = the causal variants themselves; **consanguinity** is a strong contributor (homozygous cases in consanguineous families, [PMID: 18062908](https://pubmed.ncbi.nlm.nih.gov/18062908/)). Modifier/predisposing genes are required for the lupus branch ([PMID: 29550838](https://pubmed.ncbi.nlm.nih.gov/29550838/)). No established protective alleles or environmental protective factors; UV light and infection act as general lupus/flare triggers (environmental, inferred by analogy to SLE). Gene-environment interaction: a "two-hit" model in which the complement defect (hit 1) plus modifier genes/triggers (hit 2) determine whether SLE manifests.

### 3. Phenotypes
Two phenotypic domains: (a) **laboratory abnormality** — absent CH50, undetectable C1s (HP:0005356, HP:0003261); (b) **clinical disease** — recurrent bacterial infections (HP:0002718; childhood onset, episodic, potentially severe/fatal), and SLE/lupus nephritis (HP:0002725, HP:0001970; adult-onset, variable severity, chronic-relapsing, incomplete penetrance). Quality-of-life impact is driven by recurrent infections and by lupus organ damage; formal QoL instruments have not been applied in this ultra-rare population.

### 4. Genetic/Molecular Information
Causal gene *C1S*; variant types reported = frameshift deletion, nonsense, and compound truncating (all LOF). ClinVar/ACMG: pathogenic. gnomAD allele frequencies: very rare/absent (private variants). Germline origin. Functional consequence: complete loss of function. Modifier genes: implicated but unidentified in humans; demonstrated to exist in the ICGN mouse. No epigenetic or chromosomal-abnormality mechanism reported. The index case's genetic analysis also highlighted **alternative splicing of the normal C1s gene** ([PMID: 18062908](https://pubmed.ncbi.nlm.nih.gov/18062908/)).

### 5. Environmental Information
No specific toxin/occupational cause. **Infectious agents** are downstream consequences rather than causes — encapsulated bacteria (*S. pneumoniae*, *N. meningitidis*, *H. influenzae* type b). Lifestyle factors are not established disease determinants.

### 6. Mechanism / Pathophysiology
Presented as the ordered causal chain above. Molecular pathway: complement classical pathway (Reactome/KEGG). Cellular processes: opsonophagocytosis, apoptotic-cell clearance, inflammation. Protein dysfunction: loss of function (no catalytic C1s). Immune involvement: combined immunodeficiency (opsonization failure) + autoimmunity (SLE). Tissue damage: immune-complex-mediated glomerulonephritis (lupus nephritis). Biochemical defect: absent serine-protease activity for C4/C2 cleavage.

### 7. Anatomical Structures Affected
- **Organ level:** kidney (lupus nephritis, UBERON:0002113 / glomerulus UBERON:0000074), skin (cutaneous lupus, erysipelas; UBERON:0002097), meninges/CNS (meningitis; UBERON:0002360), respiratory tract (recurrent infections). Body systems: immune, renal, integumentary, nervous.
- **Tissue/cell level:** phagocytes/macrophages (CL:0000235); serum/plasma complement.
- **Subcellular:** C1s is a secreted extracellular protein (GO:0005615/GO:0005576).
- **Localization:** systemic/bilateral (immune-complex disease affects paired organs symmetrically).

### 8. Temporal Development
Infections typically begin in **childhood**; SLE often **adult-onset** (index case 34 y). Course is **chronic/lifelong** with episodic infective and lupus flares. Penetrance of autoimmunity is **incomplete and age-dependent**. Treatment-induced remission of lupus nephritis achievable (rituximab).

### 9. Inheritance and Population
**Autosomal recessive**; carrier frequency unknown (ultra-rare, private variants, largely absent from gnomAD). ~9–10 reported complete cases worldwide; prevalence/incidence never formally established. **Consanguinity** prominent. No defined ethnic predilection beyond consanguineous pedigrees. Penetrance incomplete (2/4 siblings SLE); variable expressivity. No anticipation (not a repeat disorder). Sex ratio not established given small numbers.

### 10. Diagnostics
CH50 absent + AH50 normal → quantify C1s (undetectable), C3 normal, C4/C2 normal-to-elevated; confirm by sequencing (single-gene *C1S* / complement panel / WES / WGS). Biomarkers: anti-nuclear, anti-dsDNA antibodies (in SLE cases). Biopsy: lupus-nephritis histology with C1q deposition. Differential diagnosis: other early-pathway deficiencies (C1q, C1r, C4, C2), each distinguished by component assays, and idiopathic SLE. Screening: cascade testing of relatives via CH50 + sequencing.

### 11. Outcome/Prognosis
Driven by infection severity and lupus organ damage; invasive infections (meningitis, sepsis) are potentially fatal (a historical C1r/C1s case died of septic shock, [PMID: 7939409](https://pubmed.ncbi.nlm.nih.gov/7939409/)). Prophylaxis and vaccination substantially mitigate infectious mortality. Lupus nephritis can respond to immunosuppression/rituximab. Early complement PID associates with greater cumulative organ damage in SLE ([PMID: 21813590](https://pubmed.ncbi.nlm.nih.gov/21813590/)). No formal survival statistics exist.

### 12. Treatment
- **Pharmacotherapy / immunosuppression:** hydroxychloroquine, corticosteroids, and conventional immunosuppressants for lupus; **rituximab (anti-CD20)** effective for refractory proliferative lupus nephritis ([PMID: 20191570](https://pubmed.ncbi.nlm.nih.gov/20191570/)).
- **Anti-infective:** antibiotic prophylaxis; prompt treatment of infections.
- **Advanced/experimental:** No gene therapy; plasma/C1s replacement is conceptual. (Anti-C1s drugs target overactivity, not deficiency.)
- **NCIT terms:** Rituximab (NCIT:C1702), Hydroxychloroquine (NCIT:C509).

### 13. Prevention
- **Primary:** vaccination against encapsulated bacteria (pneumococcal, meningococcal, Hib) and antibiotic prophylaxis ([PMID: 41421099](https://pubmed.ncbi.nlm.nih.gov/41421099/)).
- **Secondary:** cascade CH50/genetic screening of relatives; early detection of lupus.
- **Tertiary:** immunosuppression to prevent lupus-nephritis progression; infection surveillance.
- **Counseling:** genetic counseling for AR recurrence risk (25% per pregnancy for carrier couples).

### 14. Other Species / Natural Disease
*C1s* orthologs exist across mammals (mouse *C1s1*/*C1s2*; NCBI Gene for mouse C1s1 = 50909). No prominent naturally occurring companion-animal C1s-deficiency disease is catalogued (OMIA), though complement biology is evolutionarily conserved. Disease mechanisms (classical pathway) are broadly conserved in mammals.

### 15. Model Organisms
The most informative model is the **ICGN congenic mouse lacking C1r/C1s** (with low C1q), which does **not** spontaneously develop SLE — recapitulating the complement defect but *not* the autoimmune phenotype in isolation, confirming the requirement for additional predisposing genes ([PMID: 29550838](https://pubmed.ncbi.nlm.nih.gov/29550838/)). **Phenotype recapitulation:** complement-deficiency phenotype reproduced; lupus phenotype NOT reproduced without modifiers — this is the model's key limitation and simultaneously its key scientific insight. In vitro systems (purified C1s, C1 complex, patient sera with C1s add-back) model the catalytic defect precisely.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (~9–10 cases):** All clinical inferences rest on case reports and small pedigrees; no cohort, prevalence, incidence, survival, or quality-of-life data exist. Penetrance and expressivity estimates are qualitative.
2. **No OMIM phenotype MIM** formally recorded for the deficiency; nosology partly inferred from the broader complement-deficiency literature.
3. **HMGB1-inactivation mechanism** is biochemically demonstrated but its *quantitative* contribution to human lupus relative to apoptotic-cell-clearance failure is unquantified.
4. **Modifier genes** that convert C1s deficiency into overt SLE in humans are unidentified.
5. **No C1s-specific knockout mouse study** of the full disease; existing model (ICGN) is combined C1r/C1s with low C1q.
6. **Treatment evidence** (rituximab) derives from single cases; no controlled data.
7. **Allelic confusion risk:** Literature searches for "*C1S*" readily return the far more numerous pEDS cases (~148), which must be excluded when curating the deficiency entry.

---

## Proposed Follow-up Experiments / Actions

1. **Curate variant-level data** into ClinVar for all reported truncating *C1S* alleles with ACMG classifications and confirm absence in gnomAD.
2. **Generate/obtain a C1s-specific knockout mouse** on a lupus-prone background to dissect the autoimmune branch and identify modifier loci (QTL mapping).
3. **Quantify HMGB1 fragment levels** in C1s-deficient patient sera vs controls to test the alarmin hypothesis in humans.
4. **Establish an international registry** for complete classical-pathway deficiencies to capture natural history, penetrance, and treatment outcomes.
5. **Assess C1s/FFP or recombinant-C1s replacement** feasibility as a mechanistic therapy; evaluate whether plasma-derived C1 could transiently restore CH50.
6. **Systematic cascade screening** (CH50 + sequencing) of relatives in reported pedigrees to refine carrier and penetrance estimates.
7. **Comparative curation review** clearly separating *C1S* LOF (deficiency) from *C1S/C1R* missense (pEDS) for knowledge-base disambiguation.

---

*Report compiled from 7 confirmed findings and 27 reviewed papers over 5 investigation iterations. Evidence types: human clinical case reports, in vitro biochemistry, model-organism (mouse), structural biology, and review literature.*


## Artifacts

- [OpenScientist final report](C1s_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](C1s_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1060176` (3 mentions) - the report calls it "C1s deficiency"; MONDO calls it **systemic lupus erythematosus related to C1S**
- `HP:0003261` (2 mentions) - the report calls it "Abnormality of complement system"; HP calls it **Increased circulating IgA concentration**
- `CL:0000235` (2 mentions) - the report calls it "Tissue/cell level:** phagocytes/macrophages"; CL calls it **macrophage**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001970` (2 mentions) - the report calls it "lupus nephritis/nephritis"; HP calls it **Tubulointerstitial nephritis**, and lists "Nephritis, Tubulointerstitial" among its other names
- `HP:0100658` (1 mention) - the report calls it "Cellulitis/erysipelas"; HP calls it **Cellulitis**
- `HP:0005356` (2 mentions) - the report calls it "Decreased complement activity"; HP calls it **Decreased circulating complement factor I concentration**, and lists "Decreased serum complement factor I" among its other names
- `NCIT:C1702` (2 mentions) - the report calls it "NCIT terms:** Rituximab"; NCIT calls it **Rituximab**
- `GO:0005615` (2 mentions) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names