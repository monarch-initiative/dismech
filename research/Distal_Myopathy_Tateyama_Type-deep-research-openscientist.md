---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T01:26:31.792809'
end_time: '2026-10-24T01:40:48.067015'
duration_seconds: 856.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Distal Myopathy, Tateyama Type
  mondo_id: MONDO:0013686
  category: Mendelian
  causal_genes: CAV3
  omim_id: not recorded
  synonyms: Tateyama distal myopathy; CAV3-related distal myopathy; caveolin-3-related
    distal myopathy
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
citation_count: 29
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 22
  validator_version: 0.3.0
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 6
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0003552
    reported_labels:
    - Symptom
    ontology_label: Muscle stiffness
  - term_id: HP:0003750
    reported_labels:
    - rippling muscle disease
    ontology_label: Increased muscle fatiguability
  - term_id: HP:0100284
    reported_labels:
    - Lab/EMG
    ontology_label: 'EMG: myotonic discharges'
  - term_id: GO:0005901
    reported_labels:
    - Subcellular:** sarcolemmal caveolae
    ontology_label: caveola
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Distal_Myopathy_Tateyama_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Distal_Myopathy_Tateyama_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Myopathy, Tateyama Type
- **MONDO ID:** MONDO:0013686 (if available)
- **Causal gene(s):** CAV3
- **OMIM:** not recorded
- **Synonyms:** Tateyama distal myopathy; CAV3-related distal myopathy; caveolin-3-related distal myopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Distal Myopathy, Tateyama Type** covering all of the
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

# Distal Myopathy, Tateyama Type (MONDO:0013686) — Comprehensive Disease Report

**Causal gene: _CAV3_ (caveolin-3), HGNC:1529, NCBI Gene 859, gene OMIM 601253, chromosome 3p25.3 · Category: Mendelian (autosomal dominant)**

> **Causal gene statement (per instructions):** Distal Myopathy, Tateyama type is caused by a heterozygous mutation in **_CAV3_**, the gene encoding **caveolin-3**, the muscle-specific structural protein of sarcolemmal caveolae. It is one of several allelic "caveolinopathy" phenotypes and is defined by the identifiers above (MONDO:0013686 / CAV3), not by any serial-number disease name.

---

## Summary

**Distal Myopathy, Tateyama type (MONDO:0013686) is a rare, benign, autosomal-dominant skeletal-muscle disorder caused by heterozygous missense mutation in _CAV3_, the gene encoding caveolin-3** — the muscle-specific structural protein of sarcolemmal caveolae. The condition was first delineated by Tateyama and colleagues in 2002 in a sporadic patient whose muscle atrophy was uniquely restricted to the small muscles of the hands and feet, in whom muscle caveolin-3 was reduced and a heterozygous _CAV3_ c.80G>A substitution was identified — the identical allele previously reported in idiopathic hyperCKemia ([PMID: 11805270](https://pubmed.ncbi.nlm.nih.gov/11805270/)). Tateyama distal myopathy is **not a standalone genetic entity but one phenotype within the allelic "caveolinopathy" spectrum**, which also encompasses limb-girdle muscular dystrophy type 1C (LGMD1C), rippling muscle disease (RMD), isolated/familial hyperCKemia, and cardiac phenotypes. The same _CAV3_ mutation can produce different phenotypes in different individuals, and asymptomatic carriers exist into old age — hallmarks of variable expressivity and incomplete penetrance.

**Mechanistically**, the pathogenic caveolin-3 protein acts in a **dominant-negative** manner: mutant protein is retained in the Golgi apparatus, drags down wild-type caveolin-3, and reduces the amount of caveolin-3 reaching the sarcolemma by >50%. This abolishes caveolae formation at the muscle cell surface and disorganizes the T-tubule system. Two downstream consequences drive the clinical picture: (1) impairment of the **MG53–dysferlin–caveolin-3 membrane-repair complex**, producing membrane fragility, creatine-kinase (CK) leak and exertional symptoms; and (2) **de-repression of myostatin/Smad2 signaling**, which caveolin-3 normally suppresses, driving the muscle atrophy — a mechanism directly demonstrated and pharmacologically rescued in mutant mice. A metabolic branch (mislocalization of muscle phosphofructokinase, PFK-M) may contribute to exercise intolerance.

**Clinically**, the disease is characterized by adult-onset, slowly progressive or stable distal (hand/foot) muscle atrophy and weakness, often accompanied by percussion-induced muscle phenomena, myalgia, muscle stiffness and elevated serum CK. Diagnosis rests on reduced sarcolemmal caveolin-3 by immunohistochemistry/immunoblot plus _CAV3_ gene sequencing. The prognosis is benign with normal life expectancy; management is supportive with genetic counseling. No disease-specific therapy exists, although myostatin inhibition is a mechanistically rational experimental avenue validated in mouse models.

---

## Key Findings

### Finding 1 — Tateyama distal myopathy is a CAV3 caveolinopathy with hand/foot-restricted atrophy

The original description by Tateyama et al. (*Neurology* 2002) established the entity: a sporadic patient with distal myopathy, **reduced caveolin-3 in muscle fibers**, and muscle atrophy **restricted to the small muscles of the hands and feet**. The abstract states: *"The authors describe a patient with sporadic distal myopathy associated with reduced caveolin-3 in muscle fibers in which the muscle atrophy was restricted to the small muscles of the hands and feet"* and *"Gene analysis disclosed a heterozygous 80 G-->A substitution in the caveolin-3 gene that was identical to that of reported cases of elevated serum creatine kinase"* ([PMID: 11805270](https://pubmed.ncbi.nlm.nih.gov/11805270/)). This fixes both the distinctive distal (small-muscle) distribution and the molecular link to reduced caveolin-3. Identifiers: MONDO:0013686; causal gene _CAV3_ (HGNC:1529; gene OMIM 601253); locus 3p25.3.

### Finding 2 — CAV3 mutations cause an autosomal-dominant phenotypic spectrum of which distal myopathy is a rare subtype

Caveolin-3 deficiency is a *"rare, autosomal dominant, muscle disorder caused by caveolin-3 gene (CAV3) mutations"* consisting of multiple clinical phenotypes: *"limb-girdle muscular dystrophy type 1C (LGMD-1C), rippling muscle disease, distal myopathy, and familial hyperCKemia"* ([PMID: 15564037](https://pubmed.ncbi.nlm.nih.gov/15564037/)). A separate cohort confirmed: *"Mutations in CAV3 lead to various neuromuscular phenotypes with partial overlap, including limb girdle muscular dystrophy type 1C (LGMD1C), rippling muscle disease, distal myopathy and isolated hyperCKemia"*, and documented the molecular signature — *"immunoblotting showed more than 50% reduction of caveolin-3 in five patients compared with controls"* ([PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)). Distal myopathy (Tateyama type) is explicitly described as *"a relatively rare subtype of caveolinopathy"* ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)).

### Finding 3 — The index allele is CAV3 c.80G>A (p.Arg27Gln; historically "R26Q"), classified pathogenic per ACMG

The original Tateyama substitution ("80 G→A") corresponds to **NM_033337.2:c.80G>A**, annotated **p.(Arg27Gln)** (historically "R26Q"). Whole-exome sequencing in a family with elevated CK confirmed: *"WES revealed a missense CAV3 mutation (NM_033337.2:c.80G>A) in the proband"* and *"The c.80G>A mutation was considered pathogenic according to ACMG guidelines"* ([PMID: 30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/)). A 2025 study of two large Chinese families with rippling muscle disease found the identical allele in all affected members: *"A heterozygous variant c.80G>A (p.Arg27Gln) in the CAV3 gene was identified in all patients with RMD"* ([PMID: 40695747](https://pubmed.ncbi.nlm.nih.gov/40695747/)). This same allele therefore recurs across distal myopathy (Tateyama), rippling muscle disease, and idiopathic hyperCKemia. Variant class: **missense**, N-terminal (pre-scaffolding domain); **germline**; functional consequence **dominant-negative / loss of sarcolemmal caveolin-3**. It is absent/ultra-rare in gnomAD, consistent with a dominant pathogenic allele.

### Finding 4 — Dominant-negative Golgi retention impairs the MG53–dysferlin–caveolin-3 membrane-repair complex

Cai et al. (2009) demonstrated that *"a molecular complex formed by MG53, dysferlin, and Cav3 is essential for repair of muscle membrane damage"* and that *"Mutations in Cav3 (P104L, R26Q) that cause retention of Cav3 in Golgi apparatus result in aberrant localization of MG53 and dysferlin in a dominant-negative fashion, leading to defective membrane repair"* ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/)). The R26Q mutation here corresponds to the recurrent Tateyama/hyperCKemia N-terminal arginine allele. This directly establishes both the dominant-negative mechanism (via Golgi retention) and the defect in sarcolemmal membrane repair that underlies CK leakage and exertional symptoms.

### Finding 5 — Caveolin-3 normally suppresses myostatin/Smad2 signaling; its loss drives atrophy (rescuable)

Ohsawa et al. (2006) showed that *"caveolin-3 inhibited myostatin signaling by suppressing activation of its type I receptor; this was followed by hypophosphorylation of an intracellular effector, Mad homolog 2 (Smad2), and decreased downstream transcriptional activity"*. In the disease model, *"Loss of caveolin-3 in P104L mutant caveolin-3 transgenic mice caused muscular atrophy with increase in phosphorylated Smad2 (p-Smad2) as well as p21"*, and critically, *"intraperitoneal administration of the soluble type II myostatin receptor, another inhibitor, ameliorated muscular atrophy of the mutant caveolin-3 transgenic mice"* ([PMID: 17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/)). This provides the mechanistic link from caveolin-3 loss → unopposed myostatin/Smad2/p21 → atrophy, and a proof-of-concept rescue.

### Finding 6 — Caveolin-3 deficiency abolishes caveolae and disorganizes the T-tubule system

Ultrastructural study of human caveolin-3-deficient muscle (Minetti et al. 2002) found *"a severe impairment of caveolae formation at the muscle cell surface, demonstrating that caveolin-3 is essential for the formation and organization of caveolae in muscle fibers"* and *"a striking disorganization of the T-system openings at the sub-sarcolemmal level"* ([PMID: 11786420](https://pubmed.ncbi.nlm.nih.gov/11786420/)). A metabolic branch exists: caveolin-3 recruits muscle phosphofructokinase (PFK-M) to the sarcolemma, and *"recombinant expression of PFK-M with three Cav-3 mutants [DeltaTFT (63 to 65), P104L, and R26Q]... causes a substantial reduction in PFK-M expression levels, and impedes the membrane recruitment of PFK-M"* ([PMID: 14633633](https://pubmed.ncbi.nlm.nih.gov/14633633/)), linking the R26Q allele to mislocalization of a key glycolytic enzyme.

### Finding 7 — The same mutation gives variable phenotypes: modifier genes, incomplete penetrance

Reviews note that among ~30 identified _CAV3_ mutations, *"Many patients show an overlap of these symptoms and the same mutation can be linked to different clinical phenotypes. This variability can be related to additional genetic or environmental factors"* ([PMID: 19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/)). A family study of the Arg26Gln allele found a spectrum from RMD to LGMD1C, and strikingly that *"one mutation carrier was asymptomatic at age 86 years"* ([PMID: 15318349](https://pubmed.ncbi.nlm.nih.gov/15318349/)) — direct evidence of incomplete penetrance/variable expressivity and the existence of modifier loci.

### Finding 8 — Diagnosis rests on reduced sarcolemmal caveolin-3 plus CAV3 sequencing

*"Muscle caveolin-3 immunoreactivity is often absent or diffusely reduced in CAV3-RMD"* ([PMID: 39370631](https://pubmed.ncbi.nlm.nih.gov/39370631/)), and *"immunoblotting was a more sensitive method to detect reduced caveolin-3 levels than immunohistochemistry in skeletal muscle"* ([PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)). The chief differential is immune-mediated RMD, which *"is often accompanied by other autoimmune disorders, including myasthenia gravis. Anti-cavin-4 antibodies are the serological marker"* ([PMID: 39370631](https://pubmed.ncbi.nlm.nih.gov/39370631/)) and is frequently associated with thymoma ([PMID: 36522170](https://pubmed.ncbi.nlm.nih.gov/36522170/)). Secondary caveolin-3 deficiency from _CAVIN1/PTRF_ mutations (congenital generalized lipodystrophy type 4) is another mimic. Dual diagnoses can co-occur, e.g. a _CAV3_ mutation together with a _DMD_ deletion in one family ([PMID: 30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/)).

### Finding 9 — Caveolin-3 dosage is critical: both loss and overexpression cause dystrophy

Mouse models bracket the mechanism. Loss-of-function: Cav3-null mice show mild LGMD1C-like dystrophy with sarcolemmal/T-tubule abnormalities, and *"Caveolin-3 (Cav-3) is a protein that has been implicated in t-tubule formation and function"* with cardiac KO disrupting T-tubule structure ([PMID: 30028203](https://pubmed.ncbi.nlm.nih.gov/30028203/)). Overexpression: transgenic *"overexpressing wild-type caveolin-3 as a transgene in mice"* produces a Duchenne-like dystrophy with *"down-regulation of dystrophin and beta-dystroglycan protein expression"* ([PMID: 10931944](https://pubmed.ncbi.nlm.nih.gov/10931944/)); cardiac overexpression induces cardiomyopathy ([PMID: 12966035](https://pubmed.ncbi.nlm.nih.gov/12966035/)). Tight dosage regulation is therefore essential for normal muscle.

### Finding 10 — CAV3 is pleiotropic: a cardiac channelopathy branch exists, but Tateyama distal myopathy is a skeletal-muscle disorder

Distinct from distal myopathy, certain _CAV3_ alleles (F97C, T78M, V14L, L79R) cause **type-9 long-QT syndrome (LQT9)** and SIDS by a gain-of-function increase in late cardiac sodium current: *"all three CAV3 mutations caused a significant fivefold increase in late sodium current compared with controls"* ([PMID: 17275750](https://pubmed.ncbi.nlm.nih.gov/17275750/)), via *"nNOS dependent direct S-nitrosylation of SCN5A"* ([PMID: 23541953](https://pubmed.ncbi.nlm.nih.gov/23541953/)). Cardiac penetrance of skeletal-muscle alleles is low: *"caveolin-3:p.T78M did not exhibit a LQTS phenotype"* ([PMID: 24021552](https://pubmed.ncbi.nlm.nih.gov/24021552/)). For the Tateyama allele p.Arg27Gln, cardiac involvement is **not** a consistent feature; distal myopathy is predominantly a skeletal-muscle phenotype.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Distal Myopathy, Tateyama type is a rare, benign, adult-onset, autosomal-dominant skeletal myopathy caused by heterozygous mutation in _CAV3_ (caveolin-3). It is distinguished within the caveolinopathy family by muscle atrophy and weakness that is **restricted to the small (distal) muscles of the hands and feet** ([PMID: 11805270](https://pubmed.ncbi.nlm.nih.gov/11805270/)). A later report emphasized an asymmetrical distal distribution ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)).

**Key identifiers.** MONDO:0013686; causal gene _CAV3_ (HGNC:1529; NCBI Gene 859; gene OMIM 601253; 3p25.3; UniProt P56539). OMIM phenotype number: not separately recorded (the distal myopathy is catalogued within the _CAV3_ allelic series; related caveolinopathy phenotypes include LGMD1C OMIM 607801 and RMD OMIM 606072). Orphanet/ICD-11/MeSH: no disease-specific code; subsumed under distal myopathies/caveolinopathies.

**Synonyms.** Tateyama distal myopathy; CAV3-related distal myopathy; caveolin-3-related distal myopathy.

**Information source.** Aggregated from disease-level resources (OMIM, reviews) and individual-patient case reports/small cohorts — the entity rests largely on single-patient and small-family reports.

### 2. Etiology

**Causal factor.** Purely genetic — a heterozygous dominant-negative missense mutation in _CAV3_. The index/canonical allele is **c.80G>A, p.(Arg27Gln)** (historically "R26Q") ([PMID: 11805270](https://pubmed.ncbi.nlm.nih.gov/11805270/); [PMID: 30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/)). Another reported distal-myopathy allele is c.136G>A, p.(Ala46Thr), apparently de novo ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)).

**Genetic risk factors.** The _CAV3_ pathogenic variant is the sole established cause; modifier genes are inferred but unidentified (see Finding 7). **Environmental/lifestyle risk factors:** none established; exercise may provoke myalgia, CK elevation and rarely rhabdomyolysis in some caveolinopathy patients ([PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)). **Protective factors:** none identified. **Gene–environment interactions:** phenotypic variability is attributed to *"additional genetic or environmental factors"* ([PMID: 19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/)) but specific interactions are not characterized.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset / Severity / Progression | Frequency |
|---|---|---|---|---|
| Distal muscle atrophy (hands & feet) | Clinical sign | HP:0003693 (distal amyotrophy) | Adult; mild–moderate; slow/stable | Defining feature |
| Distal muscle weakness | Symptom | HP:0002460 (distal muscle weakness) | Adult | Defining |
| Elevated serum creatine kinase | Lab abnormality | HP:0003236 (elevated CK) | Any age; may precede weakness | Very common |
| Myalgia | Symptom | HP:0003326 (myalgia) | Variable | Common |
| Muscle stiffness | Symptom | HP:0003552 | Variable | Common |
| Percussion-induced muscle mounding / rapid contraction (rippling) | Clinical sign | HP:0003750 (rippling muscle disease) | Childhood–adult | Frequent in spectrum |
| Exercise intolerance / rhabdomyolysis | Symptom | HP:0003546 / HP:0003201 | Exertion-triggered | Reported subset |
| Electrical myotonia (occasional) | Lab/EMG | HP:0100284 | Variable | Rare |

Severity is generally **mild**; quality-of-life impact is driven chiefly by myalgia and, where present, rippling/stiffness rather than by weakness ([PMID: 18583131](https://pubmed.ncbi.nlm.nih.gov/18583131/)). Progression is typically slow or stable; life expectancy is normal.

### 4. Genetic / Molecular Information

**Causal gene.** _CAV3_ (caveolin-3), HGNC:1529, NCBI Gene 859, gene OMIM 601253, 3p25.3; UniProt P56539. Encodes the muscle-specific caveolin isoform, the structural organizer of sarcolemmal caveolae.

**Pathogenic variants.** Canonical Tateyama allele **NM_033337.2:c.80G>A, p.(Arg27Gln)** ("R26Q"), **missense**, N-terminal (pre-scaffolding) domain, **germline**, **pathogenic** per ACMG ([PMID: 30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/)). Also reported in distal myopathy: c.136G>A, p.(Ala46Thr) ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)). Functional consequence: **dominant-negative** — mutant retained in Golgi, reduces sarcolemmal caveolin-3 by >50% ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/); [PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)). **Allele frequency:** absent/ultra-rare in gnomAD. **Somatic vs germline:** germline.

**Modifier genes.** Inferred but unidentified; same mutation → different phenotypes and an asymptomatic 86-year-old carrier ([PMID: 15318349](https://pubmed.ncbi.nlm.nih.gov/15318349/); [PMID: 19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/)).

**Epigenetic / chromosomal abnormalities:** none reported.

### 5. Environmental Information

No environmental, toxic, or infectious cause. Lifestyle: exertion may trigger myalgia/CK elevation/rhabdomyolysis in susceptible caveolinopathy patients ([PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)). No infectious agents involved.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. Heterozygous _CAV3_ missense mutation (e.g., c.80G>A, p.Arg27Gln) **produces** a misfolded caveolin-3 monomer.
2. The mutant monomer **is retained in the Golgi apparatus** and oligomerizes with wild-type caveolin-3, **acting dominant-negatively** to prevent wild-type protein reaching the plasma membrane → **>50% reduction of sarcolemmal caveolin-3** ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/); [PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)).
3. Loss of sarcolemmal caveolin-3 **abolishes caveolae formation** and **disorganizes the T-tubule system** ([PMID: 11786420](https://pubmed.ncbi.nlm.nih.gov/11786420/)).
4. **Branch A (membrane fragility):** mislocalization of MG53 and dysferlin **disrupts the MG53–dysferlin–caveolin-3 membrane-repair complex** → defective sarcolemmal repair → **CK leak, myalgia, exercise intolerance, rhabdomyolysis** ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/)).
5. **Branch B (atrophy):** loss of caveolin-3's inhibition of the myostatin type-I receptor **de-represses myostatin → Smad2 phosphorylation → p21 induction → muscle atrophy** (the distal hand/foot wasting) ([PMID: 17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/)).
6. **Branch C (metabolic, inferred):** failure to recruit PFK-M to the sarcolemma **may impair glycolytic flux**, contributing to exercise intolerance ([PMID: 14633633](https://pubmed.ncbi.nlm.nih.gov/14633633/)).
7. **Modifier step (inferred):** unidentified genetic/environmental modifiers determine which phenotype (distal myopathy vs RMD vs LGMD1C vs hyperCKemia vs asymptomatic) emerges ([PMID: 19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/)).

Upstream events (steps 1–3) are shared across all caveolinopathy phenotypes; the downstream branches and modifier background determine the specific presentation.

**Molecular pathways:** myostatin/activin–Smad2/3 (TGF-β superfamily); caveolae-dependent signaling. **Cellular processes:** sarcolemmal membrane repair, caveolae biogenesis, T-tubule organization. **Protein dysfunction:** loss of function at the sarcolemma via dominant-negative Golgi retention. **Cell types/tissue:** skeletal muscle fiber (CL:0000188); **subcellular:** plasma membrane caveola (GO:0005901), T-tubule (GO:0030315), Golgi apparatus (GO:0005794). **GO biological processes:** GO:0001778 (plasma membrane repair), GO:0070836 (caveola assembly), GO:0048741 (skeletal muscle fiber development). **Immune involvement:** none in the hereditary form (contrast immune-mediated RMD, Finding 8).

### 7. Anatomical Structures Affected

- **Organ/system:** skeletal muscle; musculoskeletal/neuromuscular system. **Primary:** intrinsic small muscles of hands and feet (distal limbs). MRI in caveolinopathies shows preferential rectus femoris/semitendinosus changes in RMD; distal and proximal signal abnormalities reported in distal myopathy ([PMID: 30174172](https://pubmed.ncbi.nlm.nih.gov/30174172/); [PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)).
- **Tissue/cell:** striated skeletal muscle; cell type = skeletal muscle fiber (CL:0000188); satellite cell dysfunction has been proposed across neuromuscular disorders ([PMID: 35302338](https://pubmed.ncbi.nlm.nih.gov/35302338/)).
- **Subcellular:** sarcolemmal caveolae (GO:0005901), T-tubule (GO:0030315), Golgi (GO:0005794).
- **UBERON:** skeletal muscle tissue (UBERON:0001134); muscle of hand (UBERON:0001497); muscle of foot. **Lateralization:** bilateral, may be asymmetric ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)).
- **Secondary:** cardiac involvement is generally absent for the Tateyama allele (Finding 10).

### 8. Temporal Development

**Onset:** typically adult-onset, insidious; rippling signs in the broader spectrum may appear in childhood. **Progression:** slow or stable; benign course. **Disease course:** chronic, lifelong but non-life-limiting. **Remission:** not applicable (hereditary). **Critical periods:** none defined.

### 9. Inheritance and Population

**Inheritance:** autosomal dominant ([PMID: 15564037](https://pubmed.ncbi.nlm.nih.gov/15564037/)); rare recessive caveolinopathy exists for other alleles ([PMID: 16730439](https://pubmed.ncbi.nlm.nih.gov/16730439/)). **Penetrance:** incomplete/age-dependent (asymptomatic carrier at age 86; [PMID: 15318349](https://pubmed.ncbi.nlm.nih.gov/15318349/)). **Expressivity:** highly variable; same allele → distal myopathy, RMD, hyperCKemia ([PMID: 19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/)). **De novo** events occur ([PMID: 26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/)). **Anticipation / mosaicism / founder effects:** not established. **Epidemiology:** caveolinopathy overall is rare (orphan); the distal-myopathy subtype is especially rare (individual case reports), so prevalence/incidence are not quantified. Reported across Japanese, Chinese, and European (UK, Italy, Greece) populations ([PMID: 15564037](https://pubmed.ncbi.nlm.nih.gov/15564037/); [PMID: 40695747](https://pubmed.ncbi.nlm.nih.gov/40695747/); [PMID: 18583131](https://pubmed.ncbi.nlm.nih.gov/18583131/); [PMID: 26185955](https://pubmed.ncbi.nlm.nih.gov/26185955/)). No sex predilection established.

### 10. Diagnostics

- **Muscle biopsy / IHC:** reduced or absent sarcolemmal caveolin-3 ([PMID: 39370631](https://pubmed.ncbi.nlm.nih.gov/39370631/)); nonspecific myopathic/dystrophic changes.
- **Immunoblot:** >50% reduction of caveolin-3 — more sensitive than IHC ([PMID: 27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/)).
- **Serum CK:** elevated (HP:0003236).
- **EMG:** myogenic changes; occasionally electrical myotonia ([PMID: 22581547](https://pubmed.ncbi.nlm.nih.gov/22581547/)) or electrical silence of ripples.
- **Clinical signs:** percussion-induced muscle mounding (PIMM) / rapid contraction (PIRC).
- **Muscle MRI:** characteristic patterns aid recognition ([PMID: 30174172](https://pubmed.ncbi.nlm.nih.gov/30174172/)).
- **Genetic testing:** _CAV3_ single-gene sequencing is definitive; WES/panel useful and can reveal dual diagnoses ([PMID: 30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/)). WGS, CMA, karyotyping, mtDNA and repeat-expansion testing are not indicated for this single-gene disorder.
- **Differential diagnosis:** immune-mediated RMD (anti-cavin-4/MURC antibodies, thymoma, myasthenia; [PMID: 36522170](https://pubmed.ncbi.nlm.nih.gov/36522170/), [PMID: 39819455](https://pubmed.ncbi.nlm.nih.gov/39819455/)); _CAVIN1/PTRF_-related RMD with CGL4 lipodystrophy ([PMID: 20300641](https://pubmed.ncbi.nlm.nih.gov/20300641/)); other distal myopathies and dysferlinopathies.

### 11. Outcome / Prognosis

Benign: normal life expectancy; morbidity dominated by myalgia, stiffness, mild distal weakness. No disease-specific mortality for the skeletal phenotype. (A cardiac-arrhythmia/LQT risk applies only to specific gain-of-function _CAV3_ alleles, not the Tateyama distal-myopathy allele — Finding 10.) Prognostic factors and biomarkers beyond CK and caveolin-3 levels are not established.

### 12. Treatment

No disease-specific or approved therapy. Management is **supportive/rehabilitative**: physiotherapy, symptom control for myalgia/stiffness, avoidance of rhabdomyolysis triggers, and genetic counseling. **Experimental/mechanistic rationale:** myostatin inhibition (soluble type-II receptor) rescued atrophy in mutant mice ([PMID: 17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/)) — a rational but unproven human avenue (NCIT: myostatin inhibitor therapy; NCIT: supportive care; NCIT: physical therapy). No pharmacogenomic, gene-therapy, or targeted therapy exists for this indication.

### 13. Prevention

No primary prevention (genetic disease). **Secondary/tertiary:** genetic counseling, cascade testing of relatives, and cardiac screening where an allele with known arrhythmogenic risk is found (not required for Arg27Gln). Prenatal/preimplantation testing is theoretically possible given a known familial variant but rarely pursued for this benign condition. No immunization or public-health measure is applicable.

### 14. Other Species / Natural Disease

Orthologous gene: mouse _Cav3_ (NCBI Gene 12391). No naturally occurring companion-animal caveolinopathy is well documented in OMIA; the evidence base is engineered mouse models (Section 15). Mechanisms (caveolae biology, T-tubule role) are evolutionarily conserved across mammals. No zoonotic/transmission relevance (non-infectious genetic disease).

### 15. Model Organisms

- **Cav3-null (KO) mouse** (mammalian, genetic): mild LGMD1C-like dystrophy; sarcolemmal/T-tubule abnormalities; cardiac KO disrupts T-tubule structure and reduces L-type Ca²⁺ current ([PMID: 30028203](https://pubmed.ncbi.nlm.nih.gov/30028203/)).
- **P104L mutant CAV3 transgenic mouse** (dominant-negative, loss of caveolin-3): muscular atrophy via myostatin/Smad2/p21; rescued by myostatin inhibition — the best disease-mechanism model ([PMID: 17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/)).
- **Wild-type caveolin-3 overexpression transgenic mouse:** Duchenne-like dystrophy with dystrophin/β-dystroglycan down-regulation ([PMID: 10931944](https://pubmed.ncbi.nlm.nih.gov/10931944/)); cardiac overexpression → cardiomyopathy ([PMID: 12966035](https://pubmed.ncbi.nlm.nih.gov/12966035/)).
- **In vitro:** C2C12 myotubes model dysferlin–caveolin-3 interactions ([PMID: 14749532](https://pubmed.ncbi.nlm.nih.gov/14749532/)); PFK-M recruitment assays with mutant Cav3 ([PMID: 14633633](https://pubmed.ncbi.nlm.nih.gov/14633633/)).

**Phenotype recapitulation / limitations:** models reproduce reduced caveolae, membrane-repair defects, and atrophy, but **do not reproduce the specific distal (hand/foot) distribution** that defines Tateyama myopathy. Resources: MGI, IMPC/KOMP, Cellosaurus (C2C12).

---

## Mechanistic Model (Synthesis)

```
 CAV3 missense mutation (c.80G>A, p.Arg27Gln / "R26Q")
                │  misfolded caveolin-3 monomer
                ▼
   Golgi retention + dominant-negative drag on WT caveolin-3
                │  >50% loss of sarcolemmal caveolin-3
                ▼
   Loss of caveolae  +  T-tubule disorganization
        │                         │                         │
  Branch A                   Branch B                   Branch C (inferred)
  MG53/dysferlin           myostatin type-I          PFK-M fails to
  mislocalized →           receptor de-repressed →   reach sarcolemma →
  membrane-repair          Smad2-P ↑ → p21 ↑ →       impaired glycolysis
  defect                   MUSCLE ATROPHY            → exercise intolerance
        │                         │
  CK leak, myalgia,        distal (hand/foot)
  exercise intolerance,    wasting & weakness
  rhabdomyolysis
                │
     [ MODIFIER genes / environment — unidentified ]
                ▼
  Phenotype selection: distal myopathy ⇆ RMD ⇆ LGMD1C ⇆ hyperCKemia ⇆ asymptomatic
```

Upstream steps (mutation → Golgi retention → caveolae/T-tubule loss) are **shared** across the caveolinopathy spectrum; the **downstream branches plus genetic background** determine the specific clinical presentation, explaining why the identical c.80G>A allele yields distal myopathy in one person, rippling muscle disease in another, and no symptoms at all in an 86-year-old carrier.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [11805270](https://pubmed.ncbi.nlm.nih.gov/11805270/) | Defining | Original Tateyama description; distal hand/foot atrophy; c.80G>A; reduced caveolin-3 |
| [15564037](https://pubmed.ncbi.nlm.nih.gov/15564037/) | Supporting | Establishes AD inheritance and 4-phenotype spectrum |
| [27312022](https://pubmed.ncbi.nlm.nih.gov/27312022/) | Supporting | >50% caveolin-3 reduction; immunoblot > IHC; exertional phenotypes |
| [26947586](https://pubmed.ncbi.nlm.nih.gov/26947586/) | Supporting | Distal myopathy = "rare subtype"; de novo A46T; asymmetry |
| [30723005](https://pubmed.ncbi.nlm.nih.gov/30723005/) | Supporting | HGVS c.80G>A, ACMG pathogenic; dual CAV3+DMD diagnosis |
| [40695747](https://pubmed.ncbi.nlm.nih.gov/40695747/) | Supporting | Same c.80G>A/p.Arg27Gln allele in RMD families (allelic overlap) |
| [19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/) | Mechanism | Golgi retention, dominant-negative, MG53–dysferlin–Cav3 repair defect |
| [17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/) | Mechanism | Myostatin/Smad2/p21 atrophy; rescued by myostatin inhibition |
| [11786420](https://pubmed.ncbi.nlm.nih.gov/11786420/) | Mechanism | Caveolae loss + T-tubule disorganization in human muscle |
| [14633633](https://pubmed.ncbi.nlm.nih.gov/14633633/) | Mechanism | R26Q impairs PFK-M membrane recruitment (metabolic branch) |
| [15318349](https://pubmed.ncbi.nlm.nih.gov/15318349/) | Supporting | Incomplete penetrance (asymptomatic at 86); variable expressivity |
| [19584897](https://pubmed.ncbi.nlm.nih.gov/19584897/) | Supporting | Same mutation → different phenotypes (modifiers/environment) |
| [39370631](https://pubmed.ncbi.nlm.nih.gov/39370631/) | Diagnostic | Reduced caveolin-3 IHC; differential with immune-mediated RMD |
| [30028203](https://pubmed.ncbi.nlm.nih.gov/30028203/) | Model | Cav3 KO disrupts T-tubules |
| [10931944](https://pubmed.ncbi.nlm.nih.gov/10931944/) | Model | Overexpression → Duchenne-like dystrophy; dosage sensitivity |
| [17275750](https://pubmed.ncbi.nlm.nih.gov/17275750/) | Pleiotropy | Gain-of-function late INa → LQT9/SIDS (other alleles) |
| [23541953](https://pubmed.ncbi.nlm.nih.gov/23541953/) | Pleiotropy | Cav3–nNOS–SCN5A S-nitrosylation mechanism |
| [24021552](https://pubmed.ncbi.nlm.nih.gov/24021552/) | Pleiotropy | Low cardiac penetrance of skeletal alleles (T78M no LQTS) |

---

## Limitations and Knowledge Gaps

1. **Thin phenotype-specific evidence base.** The Tateyama distal-myopathy subtype rests on a handful of case reports; no natural-history cohort, prevalence estimate, or quality-of-life study exists specifically for it.
2. **Genotype–phenotype gap.** Why the identical c.80G>A allele produces distal myopathy vs RMD vs hyperCKemia vs asymptomatic status is unexplained; **modifier genes remain unidentified**.
3. **Distribution not modeled.** No animal/cell model reproduces the distinctive hand/foot-restricted atrophy; the mechanistic link between generalized caveolin-3 loss and this focal distribution is unknown.
4. **Metabolic branch inferred.** The PFK-M/glycolysis contribution ([PMID: 14633633](https://pubmed.ncbi.nlm.nih.gov/14633633/)) is in vitro and its clinical weight is uncertain.
5. **No human therapeutic data.** Myostatin inhibition is validated only in mice.
6. **Diagnostic overlap** with immune-mediated and _CAVIN1/PTRF_-related RMD can cause misclassification if serology/second-gene testing is omitted.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype modifier study:** WGS/transcriptomic comparison of c.80G>A carriers across phenotypes (distal myopathy vs RMD vs asymptomatic) to map modifier loci.
2. **Patient-derived iPSC myotubes** carrying p.Arg27Gln to quantify caveolae loss, membrane-repair kinetics (laser-wounding assay), and myostatin/Smad2 activation, and to test myostatin-pathway inhibitors in vitro.
3. **Natural-history registry** for CAV3 distal myopathy capturing MRI progression, CK trajectory, and PROMIS/SF-36 quality-of-life metrics.
4. **Myostatin-inhibition translational rationale** building on the mouse rescue ([PMID: 17039257](https://pubmed.ncbi.nlm.nih.gov/17039257/)).
5. **Systematic serology** (anti-cavin-4/MURC) and _CAVIN1/PTRF_ sequencing in all reduced-caveolin-3 cases to exclude acquired and secondary mimics.
6. **Cardiac screening protocol** stratified by specific _CAV3_ allele (reassurance for Arg27Gln; ECG/Holter for gain-of-function alleles).

---

*Report compiled from a 5-iteration autonomous investigation: 10 confirmed findings, 34 papers reviewed. Evidence types span human clinical case reports/cohorts, mouse models (knockout, dominant-negative transgenic, overexpression), and in vitro cell studies.*


## Artifacts

- [OpenScientist final report](Distal_Myopathy_Tateyama_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Distal_Myopathy_Tateyama_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 22 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003552` (1 mention) - the report calls it "Symptom"; HP calls it **Muscle stiffness**
- `HP:0003750` (1 mention) - the report calls it "rippling muscle disease"; HP calls it **Increased muscle fatiguability**
- `HP:0100284` (1 mention) - the report calls it "Lab/EMG"; HP calls it **EMG: myotonic discharges**
- `GO:0005901` (2 mentions) - the report calls it "Subcellular:** sarcolemmal caveolae"; GO calls it **caveola**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003236` (2 mentions) - the report calls it "elevated CK", "Serum CK:** elevated"; HP calls it **Elevated circulating creatine kinase activity**, and lists "High serum creatine kinase" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "UBERON:** skeletal muscle tissue"; UBERON calls it **skeletal muscle tissue**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003236` - called "elevated CK", "Serum CK:** elevated"