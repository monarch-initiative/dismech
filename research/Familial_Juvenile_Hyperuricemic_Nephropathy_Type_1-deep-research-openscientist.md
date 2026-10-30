---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T17:19:07.688136'
end_time: '2026-10-28T17:33:56.966039'
duration_seconds: 889.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Familial Juvenile Hyperuricemic Nephropathy Type 1
  mondo_id: MONDO:0008073
  category: Mendelian
  causal_genes: UMOD
  omim_id: not recorded
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
citation_count: 20
reference_validation:
  total_references: 25
  verified: 24
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.04
  relevance_assessed: 24
  on_topic: 22
  unresolved_references:
  - PMID:34593962
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 11
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0008073
    reported_labels:
    - MONDO
    ontology_label: familial juvenile hyperuricemic nephropathy type 1
  - term_id: HP:0003642
    reported_labels:
    - Isosthenuria
    ontology_label: Type I transferrin isoform profile
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Juvenile_Hyperuricemic_Nephropathy_Type_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Juvenile_Hyperuricemic_Nephropathy_Type_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Juvenile Hyperuricemic Nephropathy Type 1
- **MONDO ID:** MONDO:0008073 (if available)
- **Causal gene(s):** UMOD
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Familial Juvenile Hyperuricemic Nephropathy Type 1** covering all of the
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

# Familial Juvenile Hyperuricemic Nephropathy Type 1 (ADTKD-UMOD): A Comprehensive Disease Characteristics Report

**Disease:** Familial Juvenile Hyperuricemic Nephropathy Type 1
**MONDO ID:** MONDO:0008073 · **OMIM:** 162000 · **Causal gene:** **UMOD** (uromodulin / Tamm-Horsfall protein)
**Current classification:** Autosomal Dominant Tubulointerstitial Kidney Disease, UMOD subtype (**ADTKD-UMOD**)

---

## Summary

**Familial Juvenile Hyperuricemic Nephropathy Type 1 (FJHN1; MONDO:0008073; OMIM 162000) is caused by heterozygous, mostly missense, gain-of-toxic-function mutations in *UMOD*, the gene on chromosome 16p12.3 encoding uromodulin (Tamm-Horsfall protein).** The causal gene is **UMOD** — it is important to state this explicitly because the historical name "familial juvenile hyperuricemic nephropathy" was once linked in older literature to a putative *SLC8A1* locus by linkage analysis, but the established molecular cause of Type 1 disease is UMOD. Under the 2015 KDIGO consensus, FJHN1, medullary cystic kidney disease type 2 (MCKD2), uromodulin-associated kidney disease (UAKD), and glomerulocystic kidney disease with UMOD mutation were unified into a single entity: **ADTKD-UMOD**. This disease is distinct from similarly named entities caused by other genes (*MUC1*, *REN*, *HNF1B*, *SEC61A1*, *DNAJB11*); the identifiers above anchor this report.

Mechanistically, pathogenic UMOD variants — predominantly affecting conserved cysteine residues in the N-terminal EGF-like and cysteine-rich/D8C domains — cause misfolding and retention of mutant uromodulin in the endoplasmic reticulum (ER) of thick ascending limb (TAL) epithelial cells. ER retention triggers the unfolded protein response (specifically the IRE1/XBP1 branch), ER stress, disrupted proteostasis and mitochondrial dynamics, defective autophagy, and progressive tubular cell death with interstitial fibrosis. This produces slowly progressive chronic kidney disease (CKD) that reaches end-stage kidney disease (ESKD) typically between the third and seventh decades. In parallel, TAL dysfunction impairs NKCC2-mediated salt handling, triggering compensatory proximal-tubule sodium-coupled urate reabsorption (URAT1/SLC22A12, SLC5A8), which reduces fractional excretion of uric acid and produces the characteristic **early-onset hyperuricemia and gout** (often in the teenage years).

ADTKD-UMOD is one of the more common monogenic causes of CKD (ADTKD collectively ~5% of monogenic CKD; UMOD the most prevalent ADTKD gene), yet it remains substantially under-diagnosed because it presents with bland urine (little/no proteinuria or hematuria) and non-specific CKD. Diagnosis rests on autosomal-dominant family history, hyperuricemia/gout disproportionate to kidney function, and confirmatory *UMOD* sequencing; characteristic histology shows tubulointerstitial fibrosis with intracytoplasmic uromodulin aggregates. There is **no proven disease-modifying therapy**: management is supportive (xanthine oxidase inhibitors such as allopurinol/febuxostat for gout, nephroprotection, and curative kidney transplantation without graft recurrence). Autophagy-enhancing proteostasis strategies (e.g., calorie restriction) show promise in mouse models and represent the leading experimental therapeutic direction.

---

## Key Findings

### Finding 1 — FJHN Type 1 is ADTKD-UMOD, caused by gain-of-toxic-function *UMOD* mutations

Familial juvenile hyperuricemic nephropathy type 1 (MONDO:0008073) is caused by heterozygous mutations in **UMOD** (chromosome 16p12.3), encoding uromodulin/Tamm-Horsfall protein. The 2015 KDIGO consensus report reclassified FJHN, MCKD type 2, and uromodulin-associated kidney disease (UAKD) into one entity, **ADTKD-UMOD**. The disease is defined by a classic clinical triad: autosomal-dominant inheritance, progressive renal failure beginning in the third to fifth decade, and early-onset gout/hyperuricemia. Most pathogenic UMOD variants are missense substitutions affecting cysteine residues in the N-terminal cysteine-rich, EGF-like, and D8C domains (e.g., Arg185His, Cys223Gly, Cys255Tyr, Trp258Gly, Cys147Trp). The unifying molecular consequence is a **gain-of-toxic-function** caused by retention of misfolded uromodulin in the ER.

> *"Rare autosomal dominant tubulointerstitial kidney disease is caused by mutations in the genes encoding uromodulin (UMOD), hepatocyte nuclear factor-1β (HNF1B), renin (REN), and mucin-1 (MUC1)"* — KDIGO consensus [PMID: 25738250](https://pubmed.ncbi.nlm.nih.gov/25738250/)

> *"The mutation has been traced to the UMOD gene in chromosome 16. The disease is characterised by the classic triad of autosomal dominant inheritance, progressive renal failure beginning in the third to fifth decade of life and gout."* [PMID: 26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/)

### Finding 2 — Mutant uromodulin ER retention triggers the unfolded protein response and ER stress

In immortalized mouse TAL cells expressing a mutant GFP-uromodulin, 109 genes were differentially expressed relative to wild type, with up-regulation of ER-resident chaperones and protein disulfide isomerases. Mutant uromodulin induced the **unfolded protein response (UPR)**, specifically the IRE1 branch, evidenced by increased splicing of XBP1. The common primary effect of UMOD mutations is ER retention; downstream consequences include ER stress, altered protein and mitochondrial homeostasis, defective autophagy, and increased cell death.

> *"mutant uromodulin expression induces the Unfolded Protein Response (UPR), and specifically the IRE1 branch, as shown by an increased splicing of XBP1"* [PMID: 28437467](https://pubmed.ncbi.nlm.nih.gov/28437467/)

> *"UMOD mutations have a common gain-of-toxic-function effect, causing mutant uromodulin retention in the endoplasmic reticulum (ER). This leads to ER stress, alteration of protein homeostasis and mitochondrial dynamics, defective autophagy, and increased cell death."* [PMID: 41632531](https://pubmed.ncbi.nlm.nih.gov/41632531/)

### Finding 3 — Hyperuricemia arises from impaired TAL salt handling driving compensatory urate retention

Uromodulin is produced exclusively in the TAL and regulates the NKCC2 cotransporter. Tamm-Horsfall protein/uromodulin-knockout mice display salt and water wasting via decreased luminal NKCC2 translocation, with **compensatory up-regulation of proximal-tubule sodium-coupled urate transporters SLC5A8 and SLC22A12 (URAT1)** and NHE3, elevated renin, hypertension, and elevated serum uric acid and allantoin. In Umod knock-in mouse models (C93F, A227T), the uromodulin maturation defect reduces fractional excretion of uric acid and impairs urinary concentrating ability — the direct mechanistic basis of hyperuricemia.

> *"they had significant upregulation of Na-coupled urate transporters Slc5a8 and Slc22a12 as well as sodium-hydrogen exchanger 3 (NHE3) in the proximal tubule and elevated serum uric acid and allantoin"* [PMID: 29357410](https://pubmed.ncbi.nlm.nih.gov/29357410/)

> *"reduced fractional excretion of uric acid and nephropathological alterations including uromodulin retention in TALH cells, interstitial fibrosis and inflammatory cell infiltrations"* [PMID: 23748428](https://pubmed.ncbi.nlm.nih.gov/23748428/)

### Finding 4 — Diagnostic histopathology and emerging proteostasis therapy

Renal histology shows chronic tubulointerstitial nephropathy with fibrillar/intracytoplasmic uromodulin inclusions in distal tubule cells; electron microscopy reveals bundled and cystic ER; immunohistochemistry confirms intracytoplasmic uromodulin aggregates. Genetic analysis (UMOD sequencing) is the diagnostic gold standard. Historically, allopurinol has been used for hyperuricemia and gout, but its efficacy for slowing renal progression rests only on small uncontrolled studies. In Tg-Umod^C147W mice, **30% calorie restriction stimulated autophagy and degradation of mutant uromodulin**, reverting the ADTKD-UMOD phenotype at an early stage and delaying progression at an advanced stage.

> *"Immunohistological analysis confirmed intracytoplasmic aggregates of uromodulin in the distal tubules"* [PMID: 31422399](https://pubmed.ncbi.nlm.nih.gov/31422399/)

> *"calorie restriction largely reverted autosomal dominant tubulointerstitial kidney disease (ADTKD)-UMOD phenotype, preventing inflammation, fibrosis, and kidney function decline"* [PMID: 41632531](https://pubmed.ncbi.nlm.nih.gov/41632531/)

### Finding 5 — Epidemiology: a leading but under-recognized monogenic cause of CKD

ADTKD collectively accounts for **~5% of monogenic disorders causing CKD**, making it one of the most common monogenic kidney diseases after autosomal dominant polycystic kidney disease (ADPKD); UMOD is the most prevalent ADTKD gene. Among adults with CKD, diagnostic variants are found in roughly 22% across studies, and UMOD ranks among the 8 genes accounting for more than 60% of such variants. No precise population prevalence is established and the disease is considered under-diagnosed. Inheritance is autosomal dominant with high but age-dependent penetrance; males and females are affected equally.

> *"recent data suggesting that ADTKD is one of the more common monogenic kidney diseases after autosomal dominant polycystic kidney disease, accounting for ~5% of monogenic disorders causing chronic kidney disease"* [PMID: 31488840](https://pubmed.ncbi.nlm.nih.gov/31488840/)

> *"More than 60% of these variants affected 8 genes (PKD1, PKD2, COL4A3, COL4A4, COL4A5, UMOD, MUC1, HNF1B)"* [PMID: 38958599](https://pubmed.ncbi.nlm.nih.gov/38958599/)

### Finding 6 — Clinical phenotype spectrum: hyperuricemia/gout, bland urine, progressive CKD to ESKD

ADTKD-UMOD presents with early-onset hyperuricemia (sometimes in childhood) due to profound renal uric-acid under-excretion, gout often in the teenage years, bland urine sediment (no or minimal proteinuria/hematuria), normal or small kidneys, impaired urinary concentrating ability, and slowly progressive CKD reaching ESKD between the third and seventh decades. UMOD mutations cause a marked decrease in uromodulin synthesis plus accumulation of abnormal uromodulin leading to tubular cell death. In a Chinese case series, median age of symptom onset was ~26.5 years and median ESKD age ~41.9 years (without renal replacement). Renal cysts (especially corticomedullary) may occur. Overlapping historical entities include MCKD type 2, FJHN, and glomerulocystic kidney disease.

> *"UMOD gene mutations are responsible for the autosomal dominant inheritance of chronic interstitial disease, leading to the need for renal replacement in the third through seventh decades of life. Individuals with UMOD mutations also suffer from hyperuricemia in childhood, and often suffer from gout in their teenage years."* [PMID: 21071970](https://pubmed.ncbi.nlm.nih.gov/21071970/)

> *"hyperuricemia secondary to profound renal uric acid underexcretion, gout, and chronic renal disease"* [PMID: 25417683](https://pubmed.ncbi.nlm.nih.gov/25417683/)

### Finding 7 — Uromodulin structure: a GPI-anchored ZP-module polymer; most mutations disrupt conserved cysteines

Uromodulin (UniProt **P07911**; HGNC:12559; 640-aa precursor) is a glycosylphosphatidylinositol (GPI)-anchored glycoprotein of the TAL apical membrane, built from EGF-like domains (including a calcium-binding EGF), a cysteine-rich/D8C domain, and a bipartite zona pellucida (ZP) module (ZPN+ZPC) that drives polymerization. Cryo-EM shows uromodulin forms a one-start helical homopolymer with ~180° twist between subunits; assembly is triggered by proteolytic release of a C-terminal propeptide that otherwise anchors assembly-incompetent precursors to the membrane. Most pathogenic ADTKD-UMOD variants are missense substitutions affecting conserved cysteines (e.g., C147W, C223G, C255Y), disrupting disulfide bonds and causing a maturation/folding defect. These variants are germline, near-absent in gnomAD, and classified **pathogenic/likely pathogenic** under ACMG/AMP.

> *"The unique filament architecture suggests an assembly mechanism in which subunit incorporation could be synchronized with proteolytic cleavage of the C-terminal pro-peptide that anchors assembly-incompetent UMOD precursors to the membrane."* [PMID: 32815518](https://pubmed.ncbi.nlm.nih.gov/32815518/)

> *"UMOD forms a one-start helix with an unprecedented 180-degree twist between subunits enfolded by interdomain linkers that have completely reorganized as a result of propeptide dissociation."* [PMID: 33196145](https://pubmed.ncbi.nlm.nih.gov/33196145/)

### Finding 8 — Management: xanthine-oxidase inhibitors, renal replacement therapy, and experimental autophagy enhancers

No disease-modifying therapy is proven to slow renal decline. Management is supportive: xanthine oxidase inhibitors — allopurinol (CHEBI:40279; NCIT C614) and febuxostat — control hyperuricemia and prevent gout, alongside anti-inflammatory prophylaxis (colchicine). Evidence that urate-lowering slows CKD progression is weak (small uncontrolled studies). ESKD is treated with dialysis and kidney transplantation; because the defect is intrinsic to native TAL cells, the disease **does not recur in the allograft**, making transplantation highly effective. Precipitating/nephrotoxic agents (e.g., fenofibrate, volume depletion, NSAIDs) should be used cautiously. Experimental mechanism-based approaches aim to enhance clearance of misfolded uromodulin — e.g., autophagy induction via calorie restriction.

> *"Her gout had been successfully controlled with varying doses of daily allopurinol"* [PMID: 25417683](https://pubmed.ncbi.nlm.nih.gov/25417683/)

> *"Allopurinol has been suggested as a therapeutic agent, but unfortunately this was based on non-randomised uncontrolled trials with small patient numbers."* [PMID: 26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/)

### Finding 9 — Model organisms and genotype-phenotype correlation

Multiple mouse models reproduce the human disease. Umod^C93F and Umod^A227T knock-in lines (C3H background) show gain-of-toxic-function from a uromodulin maturation defect, with ER accumulation/hyperplasia in TAL cells, elevated plasma urea/cystatin, impaired urinary concentration, reduced fractional excretion of uric acid, interstitial fibrosis, inflammation, and tubular atrophy; mutation type and allelic status (homozygous worse) modulate onset and severity. A missense Umod mouse models inherited renal fibrosis with ER stress. Transgenic Tg-Umod^C147W mice are used for therapy testing. Umod/THP knockout mice recapitulate the TAL salt-wasting → hyperuricemia/hypertension axis. Genotype-phenotype correlation is evident in a Galician cohort (37 patients, 15 families): hyperuricemia occurred in 76% of p.C255Y versus 50% of p.Q316P carriers, indicating variant-dependent expressivity. UMOD residues are highly conserved across species.

> *"the Umod mutations cause a gain-of-toxic function due to a maturation defect of the mutant uromodulin leading to a dysfunction of thick ascending limb of Henle's loop (TALH) cells of the kidney"* [PMID: 23748428](https://pubmed.ncbi.nlm.nih.gov/23748428/)

> *"Hyperuricemia was observed in 76% of p.C255Y carriers and 50% of p.Q316P carriers"* [PMID: 40300987](https://pubmed.ncbi.nlm.nih.gov/40300987/)

### Finding 10 — Common *UMOD* promoter variants modulate kidney function (distinct from Mendelian disease)

Distinct from the rare coding mutations that cause ADTKD-UMOD, common non-coding UMOD variants (e.g., promoter rs4293393/rs13333226) are among the top GWAS signals for kidney function and blood pressure. The G allele of rs4293393 associates with higher eGFR and lower CKD risk; rs13333226 associates with ESRD, diastolic blood pressure, and is protective against type 2 diabetic nephropathy. These common variants act by altering uromodulin production and renal sodium reabsorption in the TAL — mechanistically connected to, but epidemiologically separate from, the Mendelian disease.

> *"G-allele carriers at UMOD rs4293393 exhibited significantly higher eGFR values compared to non-carriers"* [PMID: 34593962](https://pubmed.ncbi.nlm.nih.gov/34593962/)

> *"The G allele of rs13333226 was associated with a decreased risk of nephropathy"* [PMID: 21738052](https://pubmed.ncbi.nlm.nih.gov/21738052/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** FJHN Type 1 is a rare, autosomal-dominant, slowly progressive tubulointerstitial kidney disease caused by mutations in **UMOD** (uromodulin / Tamm-Horsfall protein). It is characterized by a triad of dominant inheritance, early-onset hyperuricemia/gout, and progressive CKD leading to ESKD in adulthood. Under current nomenclature it is the UMOD subtype of **autosomal dominant tubulointerstitial kidney disease (ADTKD-UMOD)**.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008073 |
| OMIM | 162000 |
| Gene (HGNC) | UMOD, HGNC:12559 |
| UniProt | P07911 |
| Locus | 16p12.3 |
| Classification | ADTKD-UMOD (KDIGO 2015) |

**Synonyms / alternative names:** Familial juvenile hyperuricemic nephropathy (FJHN); uromodulin-associated kidney disease (UAKD); medullary cystic kidney disease type 2 (MCKD2); glomerulocystic kidney disease (UMOD-related); UMOD-related ADTKD.

**Data source type:** Information is derived from aggregated disease-level resources (OMIM, Orphanet, KDIGO consensus) and from individual-patient case reports and family cohorts in the primary literature, rather than from a single EHR dataset.

### 2. Etiology

**Causal factors:** Primarily **genetic** — heterozygous gain-of-toxic-function mutations in *UMOD*. There is no infectious or primary environmental cause. The disease is fully Mendelian.

**Genetic risk factors:** The causal variants are germline UMOD coding mutations (predominantly missense affecting conserved cysteines in EGF-like/cysteine-rich/D8C domains). An ultra-rare *SLC8A1* nonsense variant co-segregating with a UMOD deletion was associated with **earlier onset** in one Portuguese family, reviving an old (unconfirmed) FJHN–SLC8A1 linkage hypothesis as a possible modifier [PMID: 39216982](https://pubmed.ncbi.nlm.nih.gov/39216982/). Common UMOD promoter variants modulate general-population kidney function but do not cause the Mendelian disease (Finding 10).

**Environmental/lifestyle risk factors:** No established environmental cause. Precipitating factors that accelerate renal decline or gout include volume depletion, NSAIDs, and fenofibrate (which abruptly raised serum creatinine in an FJHN patient) [PMID: 24940667](https://pubmed.ncbi.nlm.nih.gov/24940667/). Dietary purine load and alcohol may aggravate gout non-specifically.

**Protective factors:** No specific genetic or environmental protective factor is established for the Mendelian disease. In the general population, the UMOD rs4293393 G allele and rs13333226 G allele associate with better kidney outcomes (Finding 10).

**Gene–environment interactions:** Limited data. The SLC8A1 modifier and precipitant sensitivity (fenofibrate, volume depletion) represent the main documented interactions.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency / severity | Suggested HPO |
|---|---|---|---|---|
| Hyperuricemia | Lab abnormality | Childhood–adolescence | Common; variant-dependent (76% in p.C255Y vs 50% in p.Q316P) | HP:0002149 (Hyperuricemia) |
| Gout | Clinical sign/symptom | Teenage years–adulthood | Frequent | HP:0001997 (Gout) |
| Progressive CKD / renal insufficiency | Clinical + lab | 3rd–5th decade (variable) | Near-universal, progressive | HP:0012622 (Chronic kidney disease) |
| End-stage kidney disease | Clinical | 3rd–7th decade (median ~42 y in one cohort) | Eventual in most | HP:0003774 (Stage 5 chronic kidney disease) |
| Impaired urinary concentrating ability | Lab/physiologic | Early | Common | HP:0003642 (Isosthenuria) |
| Bland urine sediment (minimal proteinuria/hematuria) | Lab | Throughout | Characteristic (notably minimal) | HP:0000093 (Proteinuria) — minimal/absent |
| Renal cysts (corticomedullary) | Imaging/physical | Variable | Inconstant | HP:0000107 (Renal cyst) |
| Normal/small kidneys | Imaging | Throughout | Common | HP:0000085-area |
| Hypertension | Clinical sign | Variable | Occurs | HP:0000822 (Hypertension) |

**Quality-of-life impact:** Progressive CKD imposes dialysis dependency or transplantation, with associated morbidity; recurrent gout attacks cause acute pain and disability. Disease-specific QoL instrument data (EQ-5D/SF-36) specific to ADTKD-UMOD are not available; impact is inferred from the general CKD/ESKD and gout literature.

### 4. Genetic / Molecular Information

**Causal gene:** *UMOD* (uromodulin), 16p12.3; HGNC:12559; UniProt P07911.

**Pathogenic variants:** Predominantly **missense** substitutions, with strong clustering at conserved **cysteine** residues in the EGF-like and cysteine-rich/D8C domains (e.g., C147W, R185H, C223G, C255Y, W258G). Rarer classes include in-frame deletions and a reported large terminal-exon deletion. Variants are **germline**, near-absent in gnomAD, and classified **pathogenic/likely pathogenic** per ACMG/AMP. Functional consequence is a **gain-of-toxic-function** (ER retention of misfolded protein) rather than simple haploinsufficiency, though uromodulin synthesis is also markedly reduced. A dominant-negative component exists: some mutant isoforms escape the ER, reach the plasma membrane, and form extracellular aggregates that impair co-expressed wild-type protein [PMID: 22237754](https://pubmed.ncbi.nlm.nih.gov/22237754/).

**Modifier genes:** A candidate SLC8A1 modifier associated with earlier onset in one family (PMID 39216982); allelic status (homozygous vs heterozygous) modulates severity in mice.

**Epigenetic / chromosomal abnormalities:** No disease-specific epigenetic signature or recurrent chromosomal abnormality is established; one large intragenic UMOD deletion is reported.

### 5. Environmental Information

No environmental toxin, infectious agent, or occupational exposure causes this Mendelian disease. Relevant lifestyle/iatrogenic modifiers: avoid volume depletion, NSAIDs, and fenofibrate (associated with acute renal function decline) [PMID: 24940667](https://pubmed.ncbi.nlm.nih.gov/24940667/). Infectious agents: not applicable.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous **UMOD missense mutation** (usually altering a conserved cysteine) **results in** a misfolded uromodulin protein with disrupted disulfide bonding / maturation defect.
2. Misfolded uromodulin **leads to** retention in the **endoplasmic reticulum** of TAL epithelial cells (instead of normal trafficking to the apical membrane).
3. ER accumulation **triggers** the **unfolded protein response (IRE1/XBP1 branch)** and **ER stress** (demonstrated: XBP1 splicing, chaperone/PDI up-regulation).
4. Sustained ER stress **results in** altered protein and mitochondrial homeostasis, **defective autophagy**, and (branch A) progressive **tubular epithelial cell death** → interstitial inflammation → **fibrosis** → **progressive CKD → ESKD** (3rd–7th decade).
5. In parallel (branch B), reduced functional uromodulin at the apical membrane **impairs NKCC2-mediated salt reabsorption** in the TAL → salt/water wasting and reduced urinary concentrating ability.
6. TAL salt wasting **leads to** compensatory **up-regulation of proximal-tubule Na-coupled urate transporters** (URAT1/SLC22A12, SLC5A8) and NHE3 (demonstrated in Umod-knockout mice) → increased urate reabsorption.
7. Increased reabsorption **results in** reduced **fractional excretion of uric acid** → **hyperuricemia** → **gout** (early onset).
8. (Minor branch, inferred) Some mutant isoforms escape the ER and form extracellular aggregates exerting a dominant-negative effect on wild-type uromodulin.

**Molecular pathways / cellular processes:** UPR/ER-stress signaling (IRE1–XBP1), proteostasis/chaperone network, autophagy (impaired; a therapeutic target), apoptosis/cell death, mitochondrial dynamics, interstitial inflammation and fibrosis. **GO term suggestions:** GO:0030968 (endoplasmic reticulum unfolded protein response), GO:0036498 (IRE1-mediated UPR), GO:0034976 (response to ER stress), GO:0006914 (autophagy), GO:0006915 (apoptotic process), GO:0008217 (regulation of blood pressure), ion transport terms for TAL salt handling.

**Cell types / anatomy:** The thick ascending limb epithelial cell is the primary target. **CL suggestions:** kidney loop of Henle thick ascending limb epithelial cell; proximal tubule epithelial cell (secondary, urate handling). **Subcellular:** endoplasmic reticulum (GO:0005783) is the central compartment; mitochondria (GO:0005739), autophagosome (GO:0005776).

**Biochemical abnormalities:** Reduced fractional uric-acid excretion; impaired urinary concentration; elevated serum uric acid; in models, elevated renin and allantoin.

### 7. Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113), specifically the **thick ascending limb of the loop of Henle** (nephron loop) and distal tubule where inclusions are seen.
- **Secondary/proximal involvement:** Proximal tubule (compensatory urate transport); renal interstitium (fibrosis, inflammatory infiltrate).
- **Body systems:** Renal/urinary system; secondary cardiovascular involvement (hypertension); musculoskeletal (gouty arthritis — first metatarsophalangeal joint classically).
- **Tissue/cell level:** Renal tubular epithelium (epithelial tissue); TAL epithelial cells; interstitial fibroblasts.
- **Subcellular:** Endoplasmic reticulum (bundled/cystic ER on EM), intracytoplasmic uromodulin aggregates.
- **Lateralization:** Bilateral (systemic genetic disease affecting both kidneys).

### 8. Temporal Development

- **Onset:** Hyperuricemia can appear in childhood; gout commonly in teenage years; CKD becomes clinically apparent in the 3rd–5th decade. Onset pattern is **insidious/chronic**.
- **Progression:** Slowly progressive to ESKD, typically between the 3rd and 7th decades (median ESKD ~41.9 years in one Chinese cohort; variable across variants/families).
- **Course:** Progressive and chronic/lifelong; not relapsing-remitting (gout attacks episodic, superimposed).
- **Critical periods:** Early disease (pre-fibrotic) is the proposed window for proteostasis-based intervention, supported by mouse calorie-restriction data showing greater benefit at an early stage.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant; high but **age-dependent penetrance**; **variable expressivity** (variant-dependent, e.g., C255Y vs Q316P).
- **Sex ratio:** ~1:1 (autosomal).
- **Epidemiology:** No precise prevalence/incidence established; under-diagnosed. ADTKD overall ≈5% of monogenic CKD; UMOD is the most common ADTKD gene; UMOD among the top 8 genes covering >60% of monogenic CKD variants in adults.
- **Founder effects / consanguinity:** Not a prominent feature (dominant disease); recurrent variants (e.g., C255Y, Q316P) reported in regional cohorts (Galicia). De novo mutations occur.
- **Genetic anticipation / germline mosaicism:** Not characteristic.

### 10. Diagnostics

- **Laboratory:** Serum uric acid (elevated, with low fractional excretion of uric acid — a key discriminator), serum creatinine/eGFR (declining), bland urinalysis (minimal proteinuria/hematuria). Reduced urinary and serum uromodulin correlate with disease severity [PMID: 37835820](https://pubmed.ncbi.nlm.nih.gov/37835820/).
- **Imaging:** Renal ultrasound — normal or small kidneys, occasional corticomedullary cysts.
- **Histopathology (biopsy):** Chronic tubulointerstitial fibrosis, tubular atrophy, intracytoplasmic uromodulin aggregates in distal tubule cells; EM shows bundled/cystic ER; IHC confirms uromodulin aggregates.
- **Genetic testing (gold standard):** *UMOD* single-gene sequencing or ADTKD/CKD gene panels (UMOD, MUC1, REN, HNF1B, SEC61A1); WES/WGS useful when panels are negative. Chromosomal microarray can detect large UMOD deletions.
- **Clinical criteria / differential diagnosis:** ADTKD criteria require a pathogenic variant in a defined gene. Differentials: other ADTKD subtypes (MUC1, REN, HNF1B, SEC61A1), ADPKD, nephronophthisis, FSGS (UMOD can mimic), and other causes of juvenile gout (e.g., methylmalonic acidemia, HGPRT deficiency, glycogen storage disease). Low fractional excretion of uric acid plus dominant family history points to UMOD.
- **Screening:** Cascade genetic screening of at-risk relatives once a familial variant is identified.

### 11. Outcome / Prognosis

- **Natural history:** Progressive CKD to ESKD requiring renal replacement therapy, typically 3rd–7th decade; substantial inter-individual and inter-family variability.
- **Mortality:** Driven by ESKD and cardiovascular comorbidity if untreated; dialysis/transplant markedly improve survival. Disease-specific mortality statistics are sparse.
- **Prognostic factors:** Variant type and domain affected (D8C-domain variants associated with more severe phenotype than GPI-area in one cohort), allelic status, modifier alleles (e.g., SLC8A1), and degree of fibrosis at biopsy.
- **Recovery:** Kidney function loss is not reversible; transplantation is curative for the renal phenotype (no graft recurrence).

### 12. Treatment

- **Pharmacotherapy (supportive):** Xanthine oxidase inhibitors — **allopurinol** (CHEBI:40279; NCIT C614) and **febuxostat** — for hyperuricemia/gout; colchicine for gout prophylaxis/flares. Urate-lowering benefit on renal progression is unproven (weak, uncontrolled evidence). Standard nephroprotection (BP control; caution with RAAS agents given salt-wasting tendency).
- **Advanced/experimental:** Autophagy-enhancing proteostasis strategies (calorie restriction in Tg-Umod^C147W mice degrade mutant uromodulin and ameliorate fibrosis). No approved gene, cell, or RNA therapy; these remain conceptual.
- **Surgical/interventional:** Kidney transplantation for ESKD — highly effective, **no disease recurrence** in the graft. Dialysis as needed.
- **Agents to avoid:** Fenofibrate (associated with acute creatinine rise), NSAIDs, volume depletion.
- **NCIT suggestions:** Allopurinol (C614), Febuxostat, Colchicine, Kidney Transplantation, Dialysis.

### 13. Prevention

- **Primary prevention:** Not possible for the Mendelian genotype; genetic counseling and reproductive options (prenatal/preimplantation genetic testing) can prevent transmission.
- **Secondary prevention:** Cascade genetic screening of relatives; early detection enables early urate control and nephroprotection.
- **Tertiary prevention:** Gout prophylaxis, BP management, avoidance of nephrotoxins, timely transplant planning.
- **Counseling:** Autosomal-dominant counseling (50% transmission risk; variable expressivity and age-dependent penetrance).

### 14. Other Species / Natural Disease

- **Orthologs/taxonomy:** *UMOD* is conserved; mouse *Umod* (NCBI Gene) is the principal ortholog used in modeling. UMOD residues (e.g., V550) are highly conserved across species.
- **Natural disease in other species:** No well-characterized spontaneous animal disease analogue is documented in the reviewed literature; models are engineered (below).

### 15. Model Organisms

| Model | Type | Key phenotype recapitulation | PMID |
|---|---|---|---|
| Umod^C93F, Umod^A227T knock-in (C3H) | Mouse knock-in | ER accumulation in TAL, impaired concentration, reduced FE uric acid, fibrosis, inflammation; severity depends on mutation/allelic status | [23748428](https://pubmed.ncbi.nlm.nih.gov/23748428/) |
| Missense Umod mouse | Mouse | Inherited renal fibrosis with ER stress | [28325753](https://pubmed.ncbi.nlm.nih.gov/28325753/) |
| Tg-Umod^C147W | Transgenic mouse | Used for therapy testing; calorie restriction reverts/delays phenotype | [41632531](https://pubmed.ncbi.nlm.nih.gov/41632531/) |
| Umod/THP knockout | Mouse KO | TAL salt-wasting → compensatory proximal urate reabsorption → hyperuricemia, hypertension | [29357410](https://pubmed.ncbi.nlm.nih.gov/29357410/) |
| Immortalized mTAL cells (mutant GFP-UMOD) | Cellular/in vitro | UPR/IRE1 activation, XBP1 splicing, chaperone up-regulation | [28437467](https://pubmed.ncbi.nlm.nih.gov/28437467/) |

**Limitations of models:** Knockout models capture the salt-handling/urate axis but not the gain-of-toxic-function ER proteinopathy; knock-in/transgenic models better capture ER retention but disease tempo and hyperuricemia penetrance differ from humans.

---

## Mechanistic Model / Interpretation

```
   UMOD missense mutation (conserved cysteine, EGF/D8C domain)
                    │  (disrupts disulfide bonds → misfolding)
                    ▼
       Misfolded uromodulin maturation defect
                    │
                    ▼
     ER retention in thick ascending limb (TAL) cells
                    │
      ┌─────────────┴─────────────────────────────┐
      ▼ (Branch A: toxic proteinopathy)            ▼ (Branch B: lost function)
 UPR / IRE1–XBP1 activation, ER stress       ↓ apical uromodulin
 defective autophagy, ↓ proteostasis          → impaired NKCC2 salt handling
      │                                            │
      ▼                                            ▼
 tubular cell death                          TAL salt/water wasting
      │                                       ↓ urinary concentration
      ▼                                            │
 interstitial inflammation + FIBROSIS             ▼
      │                                  compensatory ↑ proximal URAT1/SLC5A8/NHE3
      ▼                                            │
 PROGRESSIVE CKD → ESKD (3rd–7th decade)          ▼
                                          ↓ fractional excretion of uric acid
                                                   │
                                                   ▼
                                       HYPERURICEMIA → GOUT (early onset)

   (Minor branch) escaped mutant isoforms → extracellular aggregates
                  → dominant-negative on wild-type uromodulin
```

The two arms converge on the clinical phenotype: the **proteinopathy arm** (Branch A) drives the fibrotic CKD trajectory, while the **loss-of-function/salt-handling arm** (Branch B) drives the hyperuricemia. Upstream, the single rate-limiting lesion is ER retention of misfolded uromodulin; this is why **proteostasis-directed therapy (autophagy enhancement)** is mechanistically attractive — it targets the shared upstream node. The common-variant GWAS biology (Finding 10) is a mechanistically adjacent but epidemiologically separate phenomenon: non-coding variants tune uromodulin *dosage* and TAL sodium reabsorption across the general population, whereas the Mendelian coding mutations produce a toxic misfolded species.

---

## Evidence Base

| PMID | Role in report |
|---|---|
| [25738250](https://pubmed.ncbi.nlm.nih.gov/25738250/) | KDIGO consensus establishing ADTKD classification and UMOD as cause |
| [26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/) | Causal gene/locus, clinical triad; weak allopurinol evidence |
| [28437467](https://pubmed.ncbi.nlm.nih.gov/28437467/) | UPR/IRE1–XBP1 activation by mutant uromodulin (in vitro) |
| [41632531](https://pubmed.ncbi.nlm.nih.gov/41632531/) | Gain-of-toxic-function summary; calorie-restriction therapy in mice |
| [29357410](https://pubmed.ncbi.nlm.nih.gov/29357410/) | TAL salt-wasting → compensatory urate reabsorption (KO mouse) |
| [23748428](https://pubmed.ncbi.nlm.nih.gov/23748428/) | Knock-in mouse models; reduced FE uric acid; genotype effects |
| [31422399](https://pubmed.ncbi.nlm.nih.gov/31422399/) | Diagnostic histopathology (intracytoplasmic uromodulin aggregates) |
| [31488840](https://pubmed.ncbi.nlm.nih.gov/31488840/) | Epidemiology: ADTKD ~5% of monogenic CKD |
| [38958599](https://pubmed.ncbi.nlm.nih.gov/38958599/) | UMOD among top monogenic CKD genes in adults |
| [21071970](https://pubmed.ncbi.nlm.nih.gov/21071970/) | Age of ESKD, early hyperuricemia/gout |
| [25417683](https://pubmed.ncbi.nlm.nih.gov/25417683/) | Renal under-excretion basis of hyperuricemia; allopurinol use |
| [32815518](https://pubmed.ncbi.nlm.nih.gov/32815518/) / [33196145](https://pubmed.ncbi.nlm.nih.gov/33196145/) | Cryo-EM uromodulin filament / ZP-module assembly |
| [40300987](https://pubmed.ncbi.nlm.nih.gov/40300987/) | Variant-dependent expressivity (C255Y vs Q316P) |
| [29569962](https://pubmed.ncbi.nlm.nih.gov/29569962/) | Chinese cohort; median onset ~26.5 y, ESKD ~41.9 y; D8C vs GPI severity |
| [22237754](https://pubmed.ncbi.nlm.nih.gov/22237754/) | Dominant-negative extracellular aggregates (escaped mutant isoforms) |
| [24940667](https://pubmed.ncbi.nlm.nih.gov/24940667/) | Fenofibrate-associated acute renal decline (agent to avoid) |
| [39216982](https://pubmed.ncbi.nlm.nih.gov/39216982/) | Large UMOD deletion; SLC8A1 candidate modifier (earlier onset) |
| [34593962](https://pubmed.ncbi.nlm.nih.gov/34593962/) / [21738052](https://pubmed.ncbi.nlm.nih.gov/21738052/) / [27938332](https://pubmed.ncbi.nlm.nih.gov/27938332/) / [22592667](https://pubmed.ncbi.nlm.nih.gov/22592667/) | Common UMOD variant GWAS biology (distinct from Mendelian disease) |
| [28325753](https://pubmed.ncbi.nlm.nih.gov/28325753/) | Missense Umod mouse — inherited fibrosis with ER stress |
| [30099615](https://pubmed.ncbi.nlm.nih.gov/30099615/) | ER stress in monogenic kidney disease; MANF/CRELD2 biomarkers |
| [37835820](https://pubmed.ncbi.nlm.nih.gov/37835820/) | Uromodulin as kidney-disease biomarker |

**Evidence-type mix:** Human clinical (cohorts, case reports, KDIGO consensus), model organism (knock-in/KO/transgenic mice), in vitro (mTAL cells), and computational/structural (cryo-EM, AlphaFold). Convergent across all four source types for the central ER-retention mechanism.

---

## Limitations and Knowledge Gaps

- **Epidemiology:** No precise population prevalence/incidence; the disease is under-diagnosed. Reported figures are relative (fraction of monogenic CKD) rather than absolute.
- **Therapeutics:** No disease-modifying therapy is proven in humans. Allopurinol's effect on renal progression rests on small, uncontrolled studies. Calorie-restriction/autophagy data are preclinical (mouse only).
- **Genotype–phenotype:** Variant-dependent expressivity is documented but incompletely predictive; modifiers (e.g., SLC8A1) are hypothesis-generating from single families and unconfirmed.
- **Mechanistic uncertainty:** The relative contributions of the toxic-gain (fibrosis) arm versus loss-of-function (urate) arm to the final clinical trajectory are not precisely quantified in humans. The pathogenicity mechanism of the large terminal-exon UMOD deletion (which spares core domains) is unexplained.
- **QoL / outcomes:** No disease-specific quality-of-life, survival, or natural-history registry data (EQ-5D/SF-36) are available; prognosis is extrapolated from the general CKD/ESKD literature.
- **Human proteostasis therapy:** Whether autophagy enhancement translates to humans, and at what disease stage, is untested.

## Proposed Follow-up Experiments / Actions

1. **Clinical translation of proteostasis therapy:** Design early-phase trials or dietary/pharmacologic autophagy-induction studies (e.g., intermittent fasting, mTOR modulation) in genetically confirmed early-stage ADTKD-UMOD patients, using serum/urinary uromodulin and eGFR slope as endpoints.
2. **Natural-history registry:** Establish a multinational ADTKD-UMOD registry capturing variant, age of gout/CKD onset, ESKD age, and QoL to define prevalence, penetrance curves, and genotype-stratified prognosis.
3. **Validate the SLC8A1 modifier:** Test SLC8A1 co-segregation and onset effect in additional UMOD families and model it functionally.
4. **Mechanism quantification:** Use TAL organoids / iPSC-derived tubular cells carrying patient cysteine variants to quantify ER-stress magnitude, autophagic flux, and dominant-negative extracellular aggregation across variants.
5. **Biomarker development:** Validate ER-stress biomarkers (MANF, CRELD2) and serum/urinary uromodulin as non-invasive diagnostic/progression markers specific to ADTKD-UMOD.
6. **Deletion pathogenicity:** Functionally dissect the large terminal-exon UMOD deletion to clarify how a variant sparing core domains causes disease.

---

*Report compiled from 10 confirmed findings and 37 reviewed papers over 5 investigation iterations. Causal gene: **UMOD** (uromodulin). Disease: FJHN Type 1 = ADTKD-UMOD (MONDO:0008073; OMIM 162000).*


## Artifacts

- [OpenScientist final report](Familial_Juvenile_Hyperuricemic_Nephropathy_Type_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Juvenile_Hyperuricemic_Nephropathy_Type_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 22 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:34593962` (4 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008073` (5 mentions) - the report calls it "MONDO"; MONDO calls it **familial juvenile hyperuricemic nephropathy type 1**
- `HP:0003642` (1 mention) - the report calls it "Isosthenuria"; HP calls it **Type I transferrin isoform profile**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0036498` (1 mention) - the report calls it "IRE1-mediated UPR"; GO calls it **IRE1-mediated unfolded protein response**
- `GO:0034976` (1 mention) - the report calls it "response to ER stress"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names