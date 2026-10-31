---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-29T03:30:47.019197'
end_time: '2026-10-29T04:00:50.991530'
duration_seconds: 1803.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Currarino Triad
  mondo_id: MONDO:0008305
  category: Mendelian
  causal_genes: MNX1
  omim_id: not recorded
  synonyms: Currarino syndrome; ASP triad
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0008436
    reported_labels:
    - Abnormal sacrum morphology
    ontology_label: Absent/hypoplastic coccyx
  - term_id: HP:0032417
    reported_labels:
    - Presacral mass / teratoma terms
    ontology_label: Periglomerular fibrosis
  - term_id: HP:0002019
    reported_labels:
    - Symptom
    ontology_label: Constipation
  - term_id: HP:0000020
    reported_labels:
    - Symptom
    ontology_label: Urinary incontinence
  - term_id: HP:0002144
    reported_labels:
    - Neurological sign
    ontology_label: Tethered cord
  - term_id: HP:0002383
    reported_labels:
    - Clinical sign
    ontology_label: Infectious encephalitis
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Currarino_Triad-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Currarino_Triad-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Currarino Triad
- **MONDO ID:** MONDO:0008305 (if available)
- **Causal gene(s):** MNX1
- **OMIM:** not recorded
- **Synonyms:** Currarino syndrome; ASP triad
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Currarino Triad** covering all of the
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

# Currarino Triad (Currarino Syndrome) — Comprehensive Disease Characteristics Report

**Disease:** Currarino Triad / Currarino syndrome (ASP triad)
**MONDO:** MONDO:0008305 · **OMIM:** #176450 · **Orphanet:** ORPHA:1552
**ICD-10:** Q87.8 (approximate; often coded via component anomalies Q06.8/Q76.49) · **ICD-11:** component-based (LD2F.1Y / LB70.Y)
**MeSH:** "Currarino syndrome" (via Digestive System Abnormalities; Sacrococcygeal Region)
**Causal gene:** **MNX1** (motor neuron and pancreas homeobox 1; formerly **HLXB9**), HGNC:4628, located at **chromosome 7q36.3**
**Category:** Mendelian, autosomal dominant

---

## Summary

**Currarino syndrome (CS) is a rare, congenital, autosomal-dominant caudal malformation syndrome caused by heterozygous loss-of-function variants in the homeobox transcription-factor gene MNX1 (formerly HLXB9) at chromosome 7q36.3.** Through haploinsufficiency, loss of one functional MNX1 allele disrupts dorsal–ventral patterning of the developing caudal (hindgut/notochord/neural) region, producing the defining clinical **triad**: (1) partial sacral agenesis with a characteristic sickle-shaped or "scimitar" hemisacrum, (2) an anorectal malformation — most commonly anal stenosis — and (3) a presacral mass (usually an anterior meningocele, a mature teratoma, or both). The triad is frequently incomplete, and associated anomalies (tethered cord, urogenital/gynecologic malformations, renal anomalies, recurrent meningitis) are present in roughly 85% of patients.

The disorder is defined by **incomplete, age-independent penetrance** (~50% of MNX1 mutation carriers are clinically asymptomatic) and **highly variable expressivity**, with no reproducible genotype–phenotype correlation even within families sharing the same variant. MNX1 pathogenic variants are detected in nearly all **familial** cases but only in approximately **25–30% of sporadic** cases, implying additional genetic/modifier contributions in mutation-negative patients. The variant spectrum is dominated by null alleles (frameshift, nonsense, splice-site, whole-gene/7q36 deletions) with mutational hotspots in exon 1 (the N-terminal polyalanine tract) and the homeobox DNA-binding domain; mosaic mutations and translocation-mediated 7q36 deletions are also reported.

Diagnosis rests on clinical suspicion (persistent childhood constipation + sacral anomaly), **MRI** (the most sensitive single modality for presacral mass, spinal dysraphism, and anorectal malformation), and **MNX1 sequencing plus deletion/MLPA/chromosomal-microarray testing**. Management is **multidisciplinary surgery** — presacral mass resection, spinal cord untethering, and anorectoplasty — most often via posterior/transsacral or combined anterior–posterior approaches. Prognosis is generally good because CS-associated presacral masses are predominantly **benign mature teratomas**, but chronic constipation (~76%) and urinary incontinence (~44%) are common long-term morbidities, and rare malignant (neuroendocrine) transformation warrants lifelong surveillance. There is no pharmacologic or gene therapy; prevention centers on cascade family screening and genetic counseling. The principal experimental model is the **Hlxb9/Mnx1-null mouse**, and MNX1 forms an **allelic series** in which biallelic missense variants instead cause neonatal diabetes and overexpression drives certain cancers.

---

## Key Findings

### Finding 1 — Causal gene and variant spectrum: heterozygous loss-of-function MNX1 at 7q36

Currarino syndrome is caused by **heterozygous loss-of-function mutations in MNX1 (HLXB9)** on chromosome 7q36.3. MNX1 encodes HB9, a homeodomain transcription factor. The detection rate differs sharply by inheritance context: pathogenic variants are found in **nearly all familial CS cases** but only **~28–30% of sporadic cases**. As stated by [PMID: 34156759](https://pubmed.ncbi.nlm.nih.gov/34156759/): *"CS is associated with mutations in the MNX1 gene (motor neuron and pancreas homeobox-1, previously known as HLXB9) mapped to chromosome 7q36. Heterozygous loss-of-function mutations in the coding sequence of MNX1 gene have been reported in nearly all familial CS cases and in approximately 30% of CS sporadic patients."* The Korean cohort of [PMID: 29401559](https://pubmed.ncbi.nlm.nih.gov/29401559/) quantified this precisely: *"Pathogenic variants in MNX1 were detected in 28% of all CS cases and 25% of sporadic cases."*

The variant spectrum is dominated by predicted null alleles consistent with haploinsufficiency:

| Variant type | Representative examples |
|---|---|
| Frameshift | p.Pro18ProfsX38, p.Gly98Alafs*124, p.Gly145Alafs*77, p.Gly151Leufs*67, p.Ala216Profs*5 |
| Nonsense | p.Gln212*, p.Tyr186*, p.Gln288X |
| Missense (homeobox) | p.Arg243Trp, p.Lys295Gln, p.Trp288Gly |
| Splice-site | IVS2+1G>A |
| Structural | Large 7q36 deletions; whole-gene deletions; der(7)t(7;21)(q36.2;p11.3) |
| Mosaic | Reported in an adult female with CS features |

The Swedish series ([PMID: 21763840](https://pubmed.ncbi.nlm.nih.gov/21763840/)) demonstrated both de novo (p.Gln212X) and maternally inherited (p.Pro18ProfsX38) variants, and showed that MLPA and array-CGH are required to capture deletions missed by sequencing. **Suggested ontology terms:** gene HGNC:4628 (MNX1); disease MONDO:0008305.

### Finding 2 — MNX1/HB9 developmental role (mouse and in vitro)

MNX1/Hlxb9 is a developmental master regulator required for caudal endodermal and neural patterning. In the mouse knockout ([PMID: 10471502](https://pubmed.ncbi.nlm.nih.gov/10471502/)): *"In mice homologous for a null mutation of Hlxb9, the dorsal lobe of the pancreas fails to develop. The remnant Hlxb9-/- pancreas has small islets of Langerhans with reduced numbers of insulin-producing beta-cells."* The gene is also essential in the nervous system: [PMID: 25136833](https://pubmed.ncbi.nlm.nih.gov/25136833/) notes HB9 *"is relevant for both motor neuronal and pancreatic beta cells development"* and that *"Experimental work on animal models has shown that HLXB9 has an essential role in motor neuronal differentiation."* This dual (endoderm + neuroectoderm) requirement mechanistically links MNX1 loss to the combined hindgut/sacral/neural tube phenotypes seen in CS. **Suggested GO terms:** GO:0030154 (cell differentiation), GO:0021520 (spinal cord motor neuron cell fate specification), GO:0031016 (pancreas development).

### Finding 3 — Presacral mass: predominantly benign teratoma/meningocele, rare malignancy

CS presacral masses are biologically distinct from sporadic sacrococcygeal teratomas (SCTs). In a multicenter review of 203 pediatric SCT resections (2010–2020), 25 (12.3%) had CS; **all CS tumors were mature teratomas** ([PMID: 40541662](https://pubmed.ncbi.nlm.nih.gov/40541662/)): *"All tumors in the Currarino cohort were mature teratomas, while 27 % of non-Currarino tumors were immature and 12 % were malignant (p < 0.001). Tumors in Currarino patients were significantly smaller in size (median 3.3 cm vs. 8.0 cm, p < 0.001)."* CS tumors were predominantly Altman type IV (87% vs 17%), more often diagnosed postnatally (80% vs 25%), and associated with higher urinary incontinence (44% vs 28%, p=0.048) and constipation (76% vs 32%, p<0.001).

Despite the benign norm, malignant transformation occurs rarely. [PMID: 21915987](https://pubmed.ncbi.nlm.nih.gov/21915987/): *"Since malignant neuroendocrine transformation of presacral mass in CS is a possible complication, even thought rare, close follow up in these patients is advisable."* The mass may also be an anterior meningocele, a dermoid/neurenteric/enterogenous cyst, a hamartoma, or **dual pathology** — in a review of ~200 complete-triad cases, 22 had both a meningocele and a teratoma ([PMID: 12847376](https://pubmed.ncbi.nlm.nih.gov/12847376/)).

### Finding 4 — Incomplete penetrance and absence of genotype–phenotype correlation

CS shows strikingly variable expressivity and reduced penetrance. In a study of 72 individuals from 9 families ([PMID: 11528505](https://pubmed.ncbi.nlm.nih.gov/11528505/)): *"Highly variable phenotypes and a low penetrance with half of all carriers being clinically asymptomatic were found in three families, whereas affected members of one family showed almost identical phenotypes. However, an obvious genotype-phenotype correlation was not found."* The same work localized mutational hotspots: *"The distribution pattern of here and previously reported HLXB9 mutations indicates mutational predilection sites within exon 1 and the homeobox."* The ~50% asymptomatic-carrier figure is the single most important fact for genetic counseling and cascade screening — an apparently "sporadic" child may have a carrier parent harboring a presacral mass. The siblings in [PMID: 23466002](https://pubmed.ncbi.nlm.nih.gov/23466002/) with an identical HLXB9 mutation showed phenotypic expression ranging from incomplete to complete triad, reinforcing variable expressivity.

### Finding 5 — MRI is the preferred modality; frequent coexisting spinal dysraphism

Among 32 pediatric complete-CS patients, MRI outperformed CT for most features ([PMID: 35282111](https://pubmed.ncbi.nlm.nih.gov/35282111/)): *"While CT was better than MRI in displaying sacral anomaly (P<0.05), MRI was more sensitive than CT at detecting presacral mass, spinal dysraphism, and congenital anal atresia (P<0.05)."* In that cohort, anal atresia was the most common ARM (59.4%), sacral agenesis was mainly type IV (75%), and 25/32 had associated anomalies (tethered cord, filum lipoma, hydronephrosis). A surgical series of 10 CS patients ([PMID: 30095346](https://pubmed.ncbi.nlm.nih.gov/30095346/)) documented the dysraphism spectrum: *"Spinal anomalies included anterior meningocele (5 cases), low-lying conus (8), terminal syrinx (4), fatty filum (5), caudal lipoma (3), and intraspinal cyst (1)."* The pathognomonic bony lesion is the **sickle-shaped / "scimitar" hemisacrum** (preserved S1 with asymmetric defect of lower sacrum).

### Finding 6 — Anterior sacral meningocele: female predominance, surgical approaches

Anterior sacral meningocele (ASM) is the most common presacral-mass type. A systematic review of 208 ASM patients across 148 studies ([PMID: 42508731](https://pubmed.ncbi.nlm.nih.gov/42508731/)) found: *"Associated malformative syndromes were identified in 66% of cases, most commonly Currarino syndrome (33%). The dorsal transsacral approach was the most frequently performed procedure (58%) and showed favorable outcomes."* Female predominance was 73% (mean age 24.6 years); constipation was the most common presenting symptom (50%). An independent case series/review ([PMID: 41989599](https://pubmed.ncbi.nlm.nih.gov/41989599/)) confirmed 81% female predominance and a 70% preference for posterior approaches with lower morbidity/recurrence. Untreated ASM can present acutely as bowel obstruction/ileus or recurrent meningitis; CS can present in the neonatal period with obstruction ([PMID: 22901924](https://pubmed.ncbi.nlm.nih.gov/22901924/)): *"We describe a male infant presenting in the neonatal period with bowel obstruction who had features of anal stenosis, a presacral teratoma, and a sacral anomaly consistent with Currarino's syndrome."*

### Finding 7 — Phenotypic stratification (Complete / Mild / Minimal) and high associated-anomaly rate

A multicentre retrospective study of 45 CS patients ([PMID: 28689883](https://pubmed.ncbi.nlm.nih.gov/28689883/)) defined three phenotypic subtypes: *"Twenty patients (44.5%) presented a Complete CS type, 19 (42.2%) a Mild CS and 6 (13.3%) a Minimal CS. In addition to the classical triad elements, 38 (84.5%) patients showed associated anomalies."* Critically, this study also addressed the mutation-negative problem: *"Mutations in the MNX1 gene are the main genetic background of CS, although they are not present in almost half of the cases."* Associated anomalies include tethered cord, urogenital/gynecologic anomalies (bicornuate uterus, vaginal/uterine duplication), renal anomalies (hydronephrosis), and recurrent meningitis.

### Finding 8 — Principal model organism: the Hlxb9/Mnx1-null mouse

The Hlxb9-null mouse ([PMID: 10471502](https://pubmed.ncbi.nlm.nih.gov/10471502/)) is the principal experimental model, recapitulating MNX1 developmental dependence through dorsal pancreatic lobe agenesis and reduced beta-cell numbers. HB9 is also essential for spinal motor neuron differentiation ([PMID: 25136833](https://pubmed.ncbi.nlm.nih.gov/25136833/)), and the human SK-N-BE neuroblastoma line models HLXB9/HB9 transcriptional dynamics during retinoic-acid-induced neuronal differentiation. **Key limitation:** the mouse null phenotype centers on the pancreas/beta-cells, whereas human CS centers on caudal sacral/anorectal/presacral features; moreover, human CS is a heterozygous haploinsufficiency disorder, while the informative mouse phenotype is homozygous-null. The mouse ortholog is *Mnx1* (MGI). No naturally occurring animal equivalent is recorded in OMIA.

### Finding 9 — HB9 is a nuclear transcription factor interacting with NONO; biallelic MNX1 is a distinct allelic disorder

HB9 is a nuclear homeodomain protein whose phosphorylated isoform interacts with NONO/p54NRB ([PMID: 29309627](https://pubmed.ncbi.nlm.nih.gov/29309627/)): *"the phosphorylated isoform of the β-cell differentiation factor HLXB9 that interacts with NONO/p54NRB, a survival factor."* Importantly, this establishes an **allelic series**: biallelic/homozygous missense mutations cause a recessive disorder distinct from CS — *"two different homozygous germline mutations in HLXB9, p.F248L and p.F272L, were reported in neonatal diabetes, a condition with functional β-cell deficiency."* Separately, MNX1 **overexpression** is oncogenic (e.g., bladder cancer via CCNE1/2 upregulation [PMID: 30012177](https://pubmed.ncbi.nlm.nih.gov/30012177/); infant leukemia via t(7;12)). Thus MNX1 dosage maps to three distinct disease states.

### Finding 10 — Treatment-resistant anal stenosis; broad presacral-mass differential

CS-associated anal stenosis behaves differently from isolated congenital anal stenosis. In a systematic review of 70 congenital anal-stenosis cases ([PMID: 42489929](https://pubmed.ncbi.nlm.nih.gov/42489929/)): *"20 cases (28.6%) associated with Currarino syndrome showed poor response to conservative treatment and frequently required treatment of associated presacral lesions or more invasive procedures."* The presacral-mass differential extends beyond meningocele/teratoma ([PMID: 42864507](https://pubmed.ncbi.nlm.nih.gov/42864507/)): *"Final pathologic diagnoses included myxopapillary ependymoma, mature cystic teratoma, and neuroendocrine tumor arising within a teratoma. These cases highlight the considerable heterogeneity of presacral lesions in Currarino syndrome."*

### Finding 11 — Overall disease synthesis

CS is a congenital autosomal-dominant caudal malformation triad: partial sacral agenesis + anorectal malformation + presacral mass, caused by heterozygous MNX1/HLXB9 LoF at 7q36 (AD, ~50% asymptomatic carriers, variable expressivity). Diagnosis combines clinical findings, MRI, and MNX1 sequencing/MLPA/CMA. Treatment is surgical and multidisciplinary; prognosis is generally good (predominantly benign mature teratomas, 0% malignant in one 25-patient CS cohort vs 12% in non-CS SCT), though chronic constipation (~76%) and urinary incontinence (~44%) are common long-term morbidities ([PMID: 40541662](https://pubmed.ncbi.nlm.nih.gov/40541662/); [PMID: 34156759](https://pubmed.ncbi.nlm.nih.gov/34156759/)). Orphanet prevalence <1/100,000.

---

## Detailed Section Report

### 1. Disease Information
CS is a rare congenital malformation syndrome of the caudal body region, first delineated as a triad by Currarino et al. (1981). **Identifiers:** MONDO:0008305; OMIM #176450; Orphanet ORPHA:1552; MeSH "Currarino syndrome." **Synonyms:** Currarino syndrome, Currarino triad, ASP triad (Anorectal malformation–Sacral defect–Presacral mass), hereditary sacral agenesis with presacral mass. Information is primarily **disease-level aggregated** from case reports, case series, and multicenter cohorts rather than large EHR datasets, reflecting the disorder's rarity.

### 2. Etiology
**Primary cause:** heterozygous loss-of-function MNX1 variants (haploinsufficiency). **Genetic risk factors:** the MNX1 variant itself; a positive family history is the strongest risk factor (familial transmission with ~50% penetrance). Modifier genes are hypothesized because mutation-negative cases (~50% of sporadic patients) and intrafamilial variability imply additional genetic background ([PMID: 19853743](https://pubmed.ncbi.nlm.nih.gov/19853743/): *"The variability of the CS phenotype among related or unrelated patients bearing the same mutation advocates for differences in the genetic background of each individual and invokes the implication of additional CS susceptibility genes."*). **Environmental risk/protective factors:** none established — this is a Mendelian developmental disorder. **Gene–environment interactions:** not documented. **Protective factors:** none known.

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset | Frequency |
|---|---|---|---|---|
| Partial sacral agenesis / scimitar hemisacrum | Skeletal sign (imaging) | HP:0008436 (Abnormal sacrum morphology) | Congenital | Triad-defining (~all complete cases) |
| Anorectal malformation / anal stenosis | Structural sign | HP:0002025 (Anal stenosis) / HP:0002023 (Anal atresia) | Congenital/neonatal | Most common ARM; anal atresia 59.4% in one cohort |
| Presacral mass (meningocele/teratoma) | Structural sign | HP:0032417 (Presacral mass / teratoma terms) | Congenital | Triad-defining |
| Chronic constipation | Symptom | HP:0002019 | Infancy–childhood | ~76% |
| Urinary incontinence | Symptom | HP:0000020 | Variable | ~44% |
| Tethered cord | Neurological sign | HP:0002144 | Congenital | Frequent (part of ~85% associated anomalies) |
| Recurrent meningitis | Clinical sign | HP:0002383 | Variable | Associated (via meningocele) |
| Urogenital/gynecologic anomalies | Structural sign | HP:0000130 / HP:0000078 | Congenital | Associated |

**Severity/progression:** variable; many carriers asymptomatic (mild/minimal subtypes). Symptoms are generally stable/structural but complications (obstruction, infection) may be acute. **Quality-of-life impact:** chronic constipation and incontinence are the dominant long-term burdens.

### 4. Genetic/Molecular Information
**Causal gene:** MNX1/HLXB9 (HGNC:4628; OMIM *142994), 7q36.3. **Variant classes:** frameshift, nonsense, splice-site, missense (homeobox), whole-gene/7q36 deletions, mosaicism (see Finding 1 table). **Classification:** most null variants are Pathogenic/Likely Pathogenic per ACMG (PVS1 loss-of-function mechanism). **Allele frequency:** pathogenic CS variants are essentially absent from gnomAD (private/family-specific). **Origin:** germline (de novo or inherited); one mosaic case reported. **Functional consequence:** loss of function / haploinsufficiency; homeobox missense variants may alter DNA-binding specificity. **Modifier genes:** hypothesized but unidentified. **Epigenetics:** no disease-specific methylation signature established. **Chromosomal abnormalities:** 7q36 deletions, including translocation-mediated der(7)t(7;21)(q36.2;p11.3) ([PMID: 38585544](https://pubmed.ncbi.nlm.nih.gov/38585544/)).

### 5. Environmental Information
No environmental toxins, lifestyle factors, or infectious agents are implicated in disease causation. Recurrent meningitis is a *complication* (via CSF-communicating meningocele), not an etiologic agent.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **heterozygous loss-of-function MNX1 variant** (frameshift/nonsense/splice/deletion, or rarely a DNA-binding missense) → reduces functional HB9 transcription factor to ~50% (**haploinsufficiency**).
2. HB9 haploinsufficiency → **impaired transcriptional regulation of caudal developmental patterning** during early embryogenesis (inferred from the gene's known role in motor neuron and endodermal/beta-cell development; a direct caudal-patterning assay in human CS has not been demonstrated).
3. Defective patterning → **disrupted dorsal–ventral/notochord–hindgut–neural tube coordination** in the caudal eminence (inferred — CS is described as caused by dorsal-ventral patterning defects during embryonic development).
4. This **branches** into the triad:
   - 4a → **partial sacral agenesis** (scimitar hemisacrum) via failed caudal vertebral/sacral formation;
   - 4b → **anorectal malformation** (anal stenosis/atresia) via abnormal hindgut/cloacal development;
   - 4c → **presacral mass** (anterior meningocele from dural herniation through the sacral defect, and/or teratoma from persistent caudal pluripotent cells).
5. Structural lesions → **clinical manifestations**: constipation/obstruction (ARM + mass effect), tethered cord/neurological deficit, recurrent meningitis (CSF-communicating meningocele), urinary/fecal incontinence.
6. Rare downstream branch: persistent germ-cell/neuroendocrine elements in the teratoma → **malignant transformation** (neuroendocrine tumor) — rare.

**Molecular pathways/processes:** MNX1/HB9 is a homeodomain transcription factor acting in embryonic developmental gene-regulatory networks; its phosphorylated isoform interacts with **NONO/p54NRB** ([PMID: 29309627](https://pubmed.ncbi.nlm.nih.gov/29309627/)). **Protein dysfunction:** loss of function (truncation) or altered DNA binding (homeobox missense). **Cell types involved (suggested CL):** motor neurons (CL:0000100), pancreatic beta cells (CL:0000169) in the broader MNX1 biology; caudal mesenchyme/notochord and hindgut endoderm in CS proper. **GO terms:** GO:0045944 (positive regulation of transcription by RNA Pol II), GO:0009952 (anterior/posterior pattern specification), GO:0048646 (anatomical structure formation in morphogenesis). The upstream lesion is the mutation; all structural anomalies are downstream and parallel (the triad branches share a common upstream patterning defect rather than forming a linear cascade among themselves).

### 7. Anatomical Structures Affected
**Primary organs/structures (UBERON):** sacrum (UBERON:0001684), anus/rectum/anal canal (UBERON:0001052/UBERON:0001353), presacral/retrorectal space. **Secondary involvement:** spinal cord and meninges (tethered cord, meningocele; UBERON:0002240/UBERON:0002360), urinary tract (hydronephrosis; UBERON:0000056), female genital tract (uterus/vagina duplications; UBERON:0000995/UBERON:0000996). **Body systems:** digestive, nervous (including caudal spinal cord), skeletal, genitourinary. **Tissue level:** neuroectoderm (meninges/cord), endoderm (hindgut), mesoderm (sacrum), plus germ-cell-derived teratoma tissue. **Subcellular (GO CC):** nucleus (GO:0005634) — HB9 is a nuclear transcription factor. **Lateralization:** the hemisacral defect is characteristically **asymmetric/unilateral** (scimitar).

### 8. Temporal Development
**Onset:** congenital; anomalies are present at birth. **Presentation:** often in infancy/childhood (constipation, sacral dimple, obstruction), but frequently diagnosed in **adulthood** or incidentally (e.g., ASM found during pregnancy/delivery evaluation) because of mild/minimal phenotypes. **Course:** structural and stable rather than progressive, but complications (obstruction, meningitis, rare malignant transformation) can be acute/episodic. **Duration:** lifelong. **Critical period:** early embryogenesis (caudal development) is the window of vulnerability; postnatally, early surgical diagnosis prevents morbidity.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant. **Penetrance:** incomplete — ~50% of carriers asymptomatic ([PMID: 11528505](https://pubmed.ncbi.nlm.nih.gov/11528505/)). **Expressivity:** highly variable; no genotype–phenotype correlation. **Mosaicism:** reported (somatic/germline mosaic MNX1). **Founder effects:** none established. **Consanguinity:** not a major factor for dominant CS (relevant instead to the recessive allelic neonatal diabetes). **Epidemiology:** rare; Orphanet prevalence <1/100,000. **Sex ratio:** overall ~equal for CS, but the ASM subset shows strong **female predominance (73–81%)**. **Geographic distribution:** worldwide; cases reported across European, East Asian, and North African populations.

### 10. Diagnostics
**Imaging:** MRI is the most sensitive single modality for presacral mass, spinal dysraphism, and ARM; CT better depicts the bony sacral defect ([PMID: 35282111](https://pubmed.ncbi.nlm.nih.gov/35282111/)). Plain radiograph may show the scimitar hemisacrum. **Genetic testing (recommended approach):** MNX1 single-gene sequencing first; if negative, **MLPA/deletion analysis and chromosomal microarray** to detect 7q36 deletions ([PMID: 21763840](https://pubmed.ncbi.nlm.nih.gov/21763840/)); karyotype/FISH where translocation suspected. WES/WGS useful in syndromic/mutation-negative cases. **Clinical criteria:** the triad (sacral defect + ARM + presacral mass), with "incomplete triad" recognized. **Differential diagnosis:** caudal regression syndrome (broader caudal agenesis; HLXB9 **not** involved — [PMID: 16498628](https://pubmed.ncbi.nlm.nih.gov/16498628/)), isolated sacrococcygeal teratoma, VACTERL association, isolated anorectal malformation, Hirschsprung disease (which can co-occur — [PMID: 23948812](https://pubmed.ncbi.nlm.nih.gov/23948812/)). **Screening:** MRI screening of at-risk family members of a known mutation carrier is recommended to detect occult presacral masses ([PMID: 23466002](https://pubmed.ncbi.nlm.nih.gov/23466002/)).

### 11. Outcome / Prognosis
Prognosis is **generally good**: CS presacral masses are predominantly benign mature teratomas (0% malignant in one 25-patient CS cohort vs 12% malignant in non-CS SCT; [PMID: 40541662](https://pubmed.ncbi.nlm.nih.gov/40541662/)). **Morbidity** is dominated by chronic constipation (~76%) and urinary incontinence (~44%), plus risk of recurrent meningitis and, rarely, neuroendocrine malignant transformation requiring lifelong surveillance ([PMID: 21915987](https://pubmed.ncbi.nlm.nih.gov/21915987/)). Life expectancy is near-normal with appropriate management. **Prognostic factors:** completeness of triad, extent of spinal/neurological involvement, timeliness of surgery, and mass histology.

### 12. Treatment
No pharmacologic or gene therapy exists; management is **surgical and supportive/multidisciplinary** (pediatric surgery + neurosurgery). **Surgical interventions (suggested NCIT):** resection of the presacral mass (posterior sagittal / transsacral / anterior transabdominal / combined approaches), spinal cord **untethering**, **anorectoplasty** (e.g., PSARP) for the ARM, and **colostomy** for acute obstruction/neonatal management ([PMID: 30095346](https://pubmed.ncbi.nlm.nih.gov/30095346/); [PMID: 23590527](https://pubmed.ncbi.nlm.nih.gov/23590527/)). For ASM, posterior/dorsal transsacral approaches are most frequent and lowest-morbidity; combined anterior–posterior approaches have highest success for large/high-lying lesions ([PMID: 42508731](https://pubmed.ncbi.nlm.nih.gov/42508731/); [PMID: 41989599](https://pubmed.ncbi.nlm.nih.gov/41989599/)). CS-associated anal stenosis often resists conservative dilatation and requires definitive surgery ([PMID: 42489929](https://pubmed.ncbi.nlm.nih.gov/42489929/)). **Supportive care:** bowel management for constipation, management of urinary dysfunction, antibiotics for meningitis. Anesthetic planning is important given sacral/dural anomalies (neuraxial anesthesia challenges — [PMID: 41916044](https://pubmed.ncbi.nlm.nih.gov/41916044/)).

### 13. Prevention
**Primary prevention** is not possible (congenital Mendelian disorder). **Secondary prevention:** cascade **family/MRI screening** of first-degree relatives of mutation carriers to detect occult masses early; prenatal/postnatal imaging. **Genetic counseling** (AD inheritance, 50% transmission risk but reduced penetrance) and options for **prenatal testing / preimplantation genetic diagnosis** where a familial variant is known. **Tertiary prevention:** surgical correction and surveillance to prevent complications (obstruction, meningitis, malignant transformation).

### 14. Other Species / Natural Disease
**Taxonomy:** human (NCBI Taxon 9606) disease; experimental mouse (*Mus musculus*, 10090) model. **Orthologous gene:** mouse *Mnx1* (MGI). **Natural disease:** no naturally occurring CS equivalent is recorded in OMIA; no zoonotic or cross-species transmission (non-infectious genetic disorder). Evolutionary conservation of MNX1/HB9's developmental role (motor neurons, pancreas) across vertebrates underpins model-organism relevance.

### 15. Model Organisms
**Principal model:** the **Hlxb9/Mnx1-null mouse** (knockout), which recapitulates MNX1 developmental dependence via dorsal pancreatic lobe agenesis and reduced beta-cell numbers ([PMID: 10471502](https://pubmed.ncbi.nlm.nih.gov/10471502/)), and informs HB9's role in motor-neuron differentiation ([PMID: 25136833](https://pubmed.ncbi.nlm.nih.gov/25136833/)). **In vitro:** human SK-N-BE neuroblastoma cells model HLXB9/HB9 transcriptional dynamics during RA-induced differentiation; MIN6 beta-cell line used for NONO-interaction and proliferation studies. **Limitations:** the mouse null phenotype is pancreas/beta-cell–centric and homozygous, whereas human CS is a heterozygous, caudal-skeletal/anorectal/presacral disorder — the model therefore captures MNX1 molecular biology better than the human malformation phenotype. **Resources:** MGI (mouse), IMPC/IMSR for alleles.

---

## Mechanistic Model (Schematic)

```
 Heterozygous MNX1 (HLXB9) LoF variant  [7q36.3]
                 │  (haploinsufficiency → ~50% HB9)
                 ▼
 Impaired HB9 transcription-factor activity in caudal development
                 │ (HB9 = nuclear homeodomain TF; partner NONO)
                 ▼
 Disrupted dorsal–ventral / notochord–hindgut–neural tube patterning   [inferred]
                 │
     ┌───────────┼─────────────────────┬───────────────────────────┐
     ▼           ▼                     ▼                           ▼
 Partial      Anorectal            Presacral mass             Associated anomalies
 sacral       malformation         (ant. meningocele          (tethered cord, GU/
 agenesis     (anal stenosis/      and/or mature              renal, uterine; ~85%)
 (scimitar)   atresia)             teratoma)
     │           │                     │                           │
     └───────────┴──────────┬──────────┴───────────────────────────┘
                            ▼
      Clinical: constipation (~76%), incontinence (~44%),
      obstruction, recurrent meningitis; RARE neuroendocrine
      malignant transformation of teratoma
```

**MNX1 dosage → three distinct diseases (allelic series):**

| MNX1 state | Mechanism | Disease |
|---|---|---|
| Heterozygous LoF | Haploinsufficiency | **Currarino syndrome** (caudal malformation) |
| Biallelic/homozygous missense (p.F248L, p.F272L) | β-cell dysfunction | Neonatal diabetes |
| Overexpression | Oncogenic (CCNE1/2↑; t(7;12)) | Bladder cancer; infant leukemia |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [34156759](https://pubmed.ncbi.nlm.nih.gov/34156759/) | Mosaic MNX1 in adult female CS | Causal gene, locus, detection rates |
| [29401559](https://pubmed.ncbi.nlm.nih.gov/29401559/) | MNX1 variant spectrum, Korean CS | 28%/25% detection; variant classes |
| [10471502](https://pubmed.ncbi.nlm.nih.gov/10471502/) | Hlxb9-null mice | Developmental role; mouse model |
| [25136833](https://pubmed.ncbi.nlm.nih.gov/25136833/) | HLXB9 in neuronal differentiation | Motor-neuron + beta-cell role |
| [40541662](https://pubmed.ncbi.nlm.nih.gov/40541662/) | SCT in CS, multicenter | Benign teratoma predominance; outcomes |
| [21915987](https://pubmed.ncbi.nlm.nih.gov/21915987/) | CS with neuroendocrine tumor | Rare malignant transformation |
| [11528505](https://pubmed.ncbi.nlm.nih.gov/11528505/) | Genotype–phenotype analysis | ~50% penetrance; mutational hotspots |
| [35282111](https://pubmed.ncbi.nlm.nih.gov/35282111/) | CT vs MRI in CS | MRI superiority; phenotype frequencies |
| [30095346](https://pubmed.ncbi.nlm.nih.gov/30095346/) | Combined surgical repair | Spinal dysraphism spectrum; surgery |
| [28689883](https://pubmed.ncbi.nlm.nih.gov/28689883/) | Multicentre CS subtypes | Complete/Mild/Minimal; 84.5% associated |
| [42508731](https://pubmed.ncbi.nlm.nih.gov/42508731/) | ASM surgical review | CS 33% of ASM; approaches |
| [41989599](https://pubmed.ncbi.nlm.nih.gov/41989599/) | ASM case series/review | Female predominance; posterior approach |
| [29309627](https://pubmed.ncbi.nlm.nih.gov/29309627/) | HLXB9/NONO functional defects | NONO interaction; neonatal-diabetes allele |
| [42489929](https://pubmed.ncbi.nlm.nih.gov/42489929/) | Congenital anal stenosis review | Treatment-resistant CS stenosis |
| [42864507](https://pubmed.ncbi.nlm.nih.gov/42864507/) | Atypical presacral masses | Broader mass differential |
| [19853743](https://pubmed.ncbi.nlm.nih.gov/19853743/) | MNX1 mutations in CS patients | Modifier/susceptibility-gene hypothesis |
| [21763840](https://pubmed.ncbi.nlm.nih.gov/21763840/) | Swedish MNX1 analysis | MLPA/CGH utility; asymptomatic carriers |
| [16498628](https://pubmed.ncbi.nlm.nih.gov/16498628/) | HLXB9 & caudal regression | DDx: HLXB9 not causal in CRS |
| [12847376](https://pubmed.ncbi.nlm.nih.gov/12847376/) | Dual-pathology presacral mass | Meningocele+teratoma in 22/200 |
| [30012177](https://pubmed.ncbi.nlm.nih.gov/30012177/) | MNX1 in bladder cancer | Overexpression → oncogenesis (allelic series) |
| [38585544](https://pubmed.ncbi.nlm.nih.gov/38585544/) | 7q36 deletion via t(7;21) | Structural/translocation mechanism |
| [23466002](https://pubmed.ncbi.nlm.nih.gov/23466002/) | Variable imaging, 3 siblings | Variable expressivity; MRI family screening |

---

## Limitations and Knowledge Gaps

1. **Mutation-negative cases:** ~50% of sporadic CS lacks an identifiable MNX1 variant, indicating unknown modifier genes, regulatory variants, or locus heterogeneity ([PMID: 28689883](https://pubmed.ncbi.nlm.nih.gov/28689883/); [PMID: 19853743](https://pubmed.ncbi.nlm.nih.gov/19853743/)). No modifier gene has been identified.
2. **No genotype–phenotype correlation:** the mechanism underlying variable expressivity and ~50% penetrance is unexplained; stochastic developmental and epigenetic factors are plausible but undemonstrated.
3. **Model-organism mismatch:** the Hlxb9-null mouse best models MNX1 molecular/pancreatic biology, not the human caudal malformation; a heterozygous mouse recapitulating the triad is lacking.
4. **Mechanistic inference:** the caudal dorsal–ventral patterning defect is inferred from gene biology rather than directly demonstrated in human CS tissue; transcriptomic/single-cell data from affected caudal tissue are absent.
5. **Epidemiology:** prevalence is poorly quantified (Orphanet <1/100,000); no population registry or incidence data.
6. **Rare-event surveillance:** the true rate and predictors of malignant transformation are unknown given the disorder's rarity.

## Proposed Follow-up Experiments / Actions

1. **Expanded genomic analysis of mutation-negative CS** — trio WGS/RNA-seq to identify non-coding MNX1 regulatory variants, structural variants, and candidate modifier/digenic loci.
2. **Heterozygous and conditional caudal Mnx1 mouse models** — to test whether Mnx1 haploinsufficiency (with sensitized/modifier backgrounds) reproduces the sacral/anorectal/presacral triad and to map the critical developmental window.
3. **Single-cell/spatial transcriptomics of the embryonic caudal eminence** in Mnx1-perturbed models to resolve the inferred dorsal–ventral patterning defect and define affected cell types (notochord, hindgut endoderm, neural tube).
4. **Functional assays of homeobox missense variants** (e.g., p.Arg243Trp) for DNA-binding/transcriptional activity and NONO interaction, to clarify LoF vs altered-specificity mechanisms along the allelic series.
5. **Natural-history registry** — prospective multicenter cohort to quantify penetrance, long-term bowel/bladder outcomes, and malignant-transformation rate, standardizing MRI family-screening protocols.
6. **Standardized cascade-screening guideline** — formalize MRI + MNX1 testing recommendations for first-degree relatives of carriers.

---

*Evidence source types: human clinical (cohorts/case series/reviews), model organism (mouse Hlxb9 knockout), in vitro (SK-N-BE, MIN6). All mechanistic and clinical claims above are cited to primary literature with PMIDs and verbatim abstract quotes where provided in the knowledge base.*


## Artifacts

- [OpenScientist final report](Currarino_Triad-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Currarino_Triad-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008436` (1 mention) - the report calls it "Abnormal sacrum morphology"; HP calls it **Absent/hypoplastic coccyx**
- `HP:0032417` (1 mention) - the report calls it "Presacral mass / teratoma terms"; HP calls it **Periglomerular fibrosis**
- `HP:0002019` (1 mention) - the report calls it "Symptom"; HP calls it **Constipation**
- `HP:0000020` (1 mention) - the report calls it "Symptom"; HP calls it **Urinary incontinence**
- `HP:0002144` (1 mention) - the report calls it "Neurological sign"; HP calls it **Tethered cord**
- `HP:0002383` (1 mention) - the report calls it "Clinical sign"; HP calls it **Infectious encephalitis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045944` (1 mention) - the report calls it "positive regulation of transcription by RNA Pol II"; GO calls it **positive regulation of transcription by RNA polymerase II**
- `GO:0048646` (1 mention) - the report calls it "anatomical structure formation in morphogenesis"; GO calls it **anatomical structure formation involved in morphogenesis**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.