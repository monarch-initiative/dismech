---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T11:33:19.620089'
end_time: '2026-11-07T12:09:57.233744'
duration_seconds: 2197.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Interstitial Lung Disease 2
  mondo_id: MONDO:0800497
  category: Mendelian
  causal_genes: SFTPA2
  omim_id: OMIM:178500
  synonyms: fibrocystic pulmonary dysplasia; fibrosing alveolitis, cryptogenic; idiopathic
    pulmonary fibrosis, familial; interstitial pneumonitis, usual; pulmonary fibrosis,
    idiopathic
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
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 18
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 11
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0800497
    reported_labels:
    - MONDO
    ontology_label: interstitial lung disease 2
  - term_id: DOID:0060971
    reported_labels:
    - DOID
    ontology_label: interstitial lung disease 2
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Interstitial_Lung_Disease_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Interstitial_Lung_Disease_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Interstitial Lung Disease 2
- **MONDO ID:** MONDO:0800497 (if available)
- **Causal gene(s):** SFTPA2
- **OMIM:** OMIM:178500
- **Synonyms:** fibrocystic pulmonary dysplasia; fibrosing alveolitis, cryptogenic; idiopathic pulmonary fibrosis, familial; interstitial pneumonitis, usual; pulmonary fibrosis, idiopathic
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Interstitial Lung Disease 2** covering all of the
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

# Interstitial Lung Disease 2 (ILD2, SFTPA2): Comprehensive Disease Report

**Disease:** Interstitial Lung Disease 2 (ILD2)
**Causal gene:** **SFTPA2** (surfactant protein A2; HGNC:10799; UniProt Q8IWL1; chr10q22.3)
**MONDO:** MONDO:0800497 · **OMIM:** 178500 · **DOID:** 0060971 · **GARD:** 0028066 · **MedGen/UMLS:** C5561926

---

## Summary

Interstitial Lung Disease 2 (ILD2) is a rare, **autosomal-dominant, adult-onset form of familial pulmonary fibrosis caused by heterozygous missense mutations in SFTPA2**, the gene encoding surfactant protein A2 (SP-A2). It must not be confused with similarly named interstitial lung diseases driven by other genes (e.g., SFTPB-, SFTPC-, ABCA3-, NKX2-1-, or telomere-gene–related fibrosis); the defining lesion of ILD2 is a coding mutation in **SFTPA2**, most characteristically in the C-terminal **carbohydrate-recognition domain (CRD)** of the protein (canonical variants p.Gly231Val and p.Phe198Ser). The disease was originally defined by linkage in a large kindred co-segregating usual interstitial pneumonia (UIP)–pattern pulmonary fibrosis with lung adenocarcinoma, establishing ILD2 as a fibrosis syndrome with a strong cancer predisposition.

The core pathophysiology is a **toxic gain-of-function / proteostasis mechanism** rather than simple haploinsufficiency. Mutant SP-A2 misfolds, is retained in the endoplasmic reticulum (ER) of alveolar type II (AT2) epithelial cells, and fails to be secreted. ER retention activates the **unfolded protein response (UPR)**, which in turn drives secretion of **latent TGF-β1**, autocrine/paracrine TGF-β signaling, **epithelial–mesenchymal transition (EMT)** and epithelial cell death. This cascade produces progressive fibrotic remodeling of the lung with a UIP histologic pattern. The same secretory failure is shared across pathogenic SFTPA1/SFTPA2 variants, and the accompanying bronchiolar metaplasia and epithelial dysregulation are thought to underlie the elevated lung-cancer risk in variant carriers.

Clinically, ILD2 presents earlier than sporadic IPF (familial pulmonary fibrosis median diagnosis ~61 years vs ~67 years, with cases reported from the late teens to 90s), with exertional dyspnea, cough, reduced diffusing capacity, ground-glass opacities and cysts on CT, and a UIP pattern. Prognosis is poor — surfactant-related-gene (SRG) carriers have low transplant-free survival (median ~44 months in one cohort). There is **no SFTPA2-specific therapy**; management relies on antifibrotics (pirfenidone, nintedanib), selective immunomodulation in some surfactant-gene cases, lung-cancer CT surveillance, genetic counseling, and lung transplantation. This report synthesizes nine confirmed findings drawn from 27 reviewed papers and authoritative database annotations (OMIM, ClinVar, UniProt/InterPro, Monarch/HPO).

---

## 1. Disease Information

**Overview.** ILD2 is a Mendelian interstitial lung disease defined by Monarch as *"An interstitial lung disease in which the cause of the disease is a variation in the SFTPA2 gene."* It manifests as adult-onset familial pulmonary fibrosis, usually with a **usual interstitial pneumonia (UIP)** histologic pattern, and carries a predisposition to **lung adenocarcinoma**. It falls within the broader clinical category of familial pulmonary fibrosis / familial interstitial pneumonia and is one of the "surfactant-related gene" (SRG) forms of pulmonary fibrosis (distinct from telomere-related gene forms).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 178500 |
| MONDO | MONDO:0800497 |
| DOID | DOID:0060971 |
| GARD | 0028066 |
| MedGen / UMLS | C5561926 |
| Gene (HGNC) | SFTPA2 (HGNC:10799) |
| UniProt | Q8IWL1 (SFPA2_HUMAN) |

**Synonyms / alternative names.** Interstitial lung disease 2; fibrocystic pulmonary dysplasia; cryptogenic fibrosing alveolitis; familial idiopathic pulmonary fibrosis; usual interstitial pneumonitis; idiopathic pulmonary fibrosis (when caused by SFTPA2). Note that several of these synonyms are generic IPF terms; the ILD2 label specifically denotes the SFTPA2-caused subtype.

**Nature of the information.** The knowledge base here is derived predominantly from **aggregated, disease-level resources** (OMIM, ClinVar, UniProt, Monarch/HPO) and from **published family/cohort studies** rather than from individual EHR records. Evidence sources span human clinical cohorts, in vitro functional assays, and database curation.

---

## 2. Etiology

**Primary cause (genetic).** ILD2 is caused by **heterozygous germline missense mutations in SFTPA2**, inherited in an autosomal-dominant manner. The original disease-defining study mapped linkage in a large IPF/lung-adenocarcinoma family to chromosome 10 (a 15.7-Mb interval) and identified rare missense mutations **G231V** and **F198S** in SFTPA2, both affecting invariant residues of the highly conserved CRD ([PMID: 19100526](https://pubmed.ncbi.nlm.nih.gov/19100526/)). The authors reported: *"Both mutations involve invariant residues in the highly conserved carbohydrate-recognition domain of the protein and are predicted to disrupt protein structure. Recombinant proteins carrying these mutations are retained in the endoplasmic reticulum and are not secreted."*

**Genetic risk factors.**
- *Causal variants:* CRD missense variants in SFTPA2 (p.Gly231Val, p.Phe198Ser, and additional ClinVar pathogenic variants such as p.Asn171Ile, p.Tyr186Cys, p.Trp233Arg, and the in-frame p.Tyr240del).
- *Shared pathway genes:* Pathogenic variants in the paralog **SFTPA1** cause an essentially indistinguishable SP-A–disorder phenotype, and other surfactant genes (SFTPC, ABCA3, NKX2-1) and telomere-related genes (TERT, TERC, RTEL1, PARN, TINF2, DKC1) cause overlapping familial pulmonary fibrosis.
- *Common modifier/susceptibility loci in broader IPF:* the **MUC5B promoter polymorphism** and SNPs in TERT, FAM13A, and surfactant genes are established IPF risk alleles, though these are general IPF modifiers rather than ILD2-specific ([PMID: 35795226](https://pubmed.ncbi.nlm.nih.gov/35795226/)).

**Environmental risk factors.** For SFTPA2-caused disease itself, the mutation is the dominant driver, with incomplete/age-dependent penetrance implying additional modifiers. In the broader IPF context relevant to disease expression, recognized environmental/host risk factors include **aging, male sex, cigarette smoking, and occupational/inhalational exposures**. Smoking is particularly relevant given the lung-cancer predisposition in carriers.

**Protective factors.** No specific genetic or environmental protective alleles have been established for ILD2. Longer telomere length relative to typical IPF has been noted as a *distinguishing feature* (not necessarily protective) of SFTPA2-variant carriers ([PMID: 36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/)).

**Gene–environment interactions.** The incomplete penetrance and variable expressivity of SFTPA2 mutations strongly imply gene–environment and gene–gene interaction (e.g., smoking, aging, and modifier loci shaping whether and when fibrosis or cancer develops), although specific GxE mechanisms have not been formally quantified for ILD2.

---

## 3. Phenotypes

The Monarch Initiative provides an authoritative set of 12 HPO annotations for ILD2 (MONDO:0800497 / OMIM 178500):

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Pulmonary fibrosis | HP:0002206 | Clinical/imaging/pathology | Core feature; progressive |
| Usual interstitial pneumonia | HP:0031950 | Histopathology pattern | Predominant pattern in familial PF |
| Dyspnea | HP:0002094 | Symptom | Progressive |
| Exertional dyspnea | HP:0002875 | Symptom | Early, common |
| Cough | HP:0012735 | Symptom | Typically dry/chronic |
| Clubbing of fingers | HP:0100759 | Clinical sign | Sign of chronic hypoxemia/fibrosis |
| Decreased DLCO | HP:0045051 | Lab/functional | Hallmark of impaired gas transfer |
| Pulmonary arterial hypertension | HP:0002092 | Complication | Secondary to fibrosis/hypoxia |
| Alveolar cell carcinoma | HP:0006519 | Neoplasm | Lung adenocarcinoma predisposition |
| Elevated BAL neutrophil proportion | HP:0032977 | Lab abnormality | BAL finding |
| Increased circulating immunoglobulin | HP:0010702 | Lab abnormality | |
| Cirrhosis | HP:0001394 | Extrapulmonary | More typical of telomere forms; listed in annotation set |

**Phenotype characteristics.**
- *Age of onset:* Adult/late-onset; familial pulmonary fibrosis is diagnosed younger than sporadic (mean 61.4 vs 66.6 years, p=0.012), with a wide reported range (19–92 years) ([PMID: 22853774](https://pubmed.ncbi.nlm.nih.gov/22853774/)). SFTPA2-variant carriers are often younger than typical IPF patients.
- *Severity:* Variable but frequently severe; carriers can present with substantially reduced lung function (FVC ~72% predicted, DLCO ~46% predicted in an SRG cohort) ([PMID: 36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/)).
- *Progression:* Progressive and frequently fatal, with low transplant-free survival.
- *Frequency:* ILD and/or lung adenocarcinoma was reported in 13/14 families (93%) in a French SP-A disorder cohort ([PMID: 32855221](https://pubmed.ncbi.nlm.nih.gov/32855221/)).

**Quality-of-life impact.** Progressive dyspnea, cough, exercise limitation, oxygen dependence, and the psychological burden of a hereditary, cancer-predisposing, often-fatal disease substantially impair daily functioning. Disease-specific QoL instrument values were not resolved in this investigation; this is a knowledge gap.

---

## 4. Genetic / Molecular Information

**Causal gene.** **SFTPA2** (surfactant protein A2), chromosome 10q22.3; encodes SP-A2, an innate-immune collectin of pulmonary surfactant (UniProt Q8IWL1).

**Pathogenic variants.** Pathogenic/likely-pathogenic variants are predominantly **missense or small in-frame changes clustered in the C-type lectin carbohydrate-recognition domain (CRD)**. ClinVar (queried November 2026) held **137 SFTPA2 records**; among the first 100 reviewed, 5 Pathogenic, 2 Likely pathogenic, 2 Conflicting, ~55 VUS, and ~35 benign/likely benign. Confirmed pathogenic/likely-pathogenic SNVs include (NM_001098668.4):

| cDNA | Protein | Type | Domain |
|---|---|---|---|
| c.512A>T | p.Asn171Ile | missense | CRD |
| c.557A>G | p.Tyr186Cys | missense | CRD |
| c.697T>A | p.Trp233Arg | missense | CRD |
| c.719_721del | p.Tyr240del | in-frame del | CRD |
| (literature) | p.Gly231Val | missense | CRD |
| (literature) | p.Phe198Ser | missense | CRD |

**Variant classification/type.** Per ACMG/AMP interpretation in ClinVar, the pathogenic set is enriched for missense/in-frame variants in a functionally critical domain; many remaining SFTPA2 records are VUS, reflecting the gene's high natural polymorphism.

**Allele frequency.** Pathogenic CRD variants are **rare** (private/family-level), consistent with high-penetrance Mendelian disease; functional studies report that deleterious SFTPA2 variants were found at ~1.3% prevalence in an unselected IPF whole-genome cohort ([PMID: 36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/)).

**Somatic vs germline.** The disease-causing variants are **germline**. Large 10q duplications classified pathogenic in ClinVar are incidental CNVs, not SFTPA2-specific.

**Functional consequence.** A **toxic gain-of-function / proteostasis defect**: recombinant mutant SP-A2 proteins are **retained in the ER and not secreted** ([PMID: 19100526](https://pubmed.ncbi.nlm.nih.gov/19100526/)). Across 11 pathogenic SFTPA1/SFTPA2 mutations, *"protein production was preserved but secretion was abolished"* ([PMID: 32855221](https://pubmed.ncbi.nlm.nih.gov/32855221/)) — i.e., the lesion is secretory/misfolding rather than loss of expression.

**Modifier genes / epigenetics / chromosomal abnormalities.** No ILD2-specific modifier genes are firmly established; broader IPF modifiers (MUC5B, TERT, FAM13A) and epigenetic drivers (specific microRNAs/lncRNAs, transposon dysregulation affecting TGF-β/sirtuin/telomere axes) have been proposed for IPF in general ([PMID: 35795226](https://pubmed.ncbi.nlm.nih.gov/35795226/)). No recurrent chromosomal abnormality defines ILD2.

**UniProt/InterPro annotation (Q8IWL1).** SP-A2 is a collectin with an N-terminal collagen-like region and a C-terminal C-type lectin CRD (InterPro IPR033990 Collectin_CTLD, IPR001304 C-type lectin; Pfam PF00059 Lectin_C). In the presence of calcium ions it binds surfactant phospholipids and lowers surface tension at the alveolar air–liquid interface, essential for normal respiration. Localization: secreted/surface film, plus lamellar body (GO:0042599), ER membrane (GO:0005789), multivesicular body (GO:0005771), clathrin-coated endocytic vesicle (GO:0045334).

---

## 5. Environmental Information

Environmental contributors to ILD2 are those of pulmonary fibrosis generally — **cigarette smoke, inhaled/occupational particulates, and aging** — acting on a genetically primed epithelium. Smoking is doubly relevant given the lung-cancer predisposition. No infectious agent causes ILD2; however, SP-A2's innate-immune role means surfactant dysfunction may alter host defense. There are no established dietary/lifestyle protective exposures specific to ILD2.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **germline missense mutation in SFTPA2** (e.g., p.Gly231Val, p.Phe198Ser) alters an invariant residue of the CRD → **leads to** a misfolded SP-A2 protein (demonstrated: predicted structural disruption; recombinant proteins misfold).
2. Misfolded SP-A2 **is retained in the endoplasmic reticulum** of alveolar type II (AT2) cells and **is not secreted** → protein production is preserved but secretion abolished (demonstrated in recombinant and patient-derived systems).
3. ER accumulation of misfolded protein **results in ER stress and activation of the unfolded protein response (UPR)** (demonstrated; UPR activation required for maximal downstream effect).
4. UPR activation **leads to secretion of latent TGF-β1**, coordinately upregulating TGF-β1, LTBP-1 and LTBP-4 (demonstrated in lung epithelial cells; mutant-specific — not seen with common SP-A2 variants or other misfolded proteins).
5. Latent/active TGF-β1 **drives autocrine and paracrine TGF-β signaling** in the alveolar epithelium (demonstrated).
6. TGF-β signaling **causes epithelial–mesenchymal transition (EMT) and epithelial cell death** (demonstrated; reversed by pan-TGF-β antibody, TGF-β receptor antagonist, or LTBP silencing).
7. Repeated AT2 injury, EMT, and aberrant fibroblast/myofibroblast activation **result in progressive extracellular-matrix deposition and UIP-pattern pulmonary fibrosis** (inferred from integration of steps 1–6 with UIP histology in patients).
8. **Branch:** The same epithelial dysregulation / bronchiolar metaplasia **predisposes to lung adenocarcinoma** (inferred/epidemiologically supported; original families co-segregated fibrosis and adenocarcinoma, and SRG carriers show high cancer risk).
9. Advancing fibrosis **leads to impaired gas exchange (decreased DLCO), exertional dyspnea, hypoxemia, pulmonary arterial hypertension, respiratory failure, and death** (clinically demonstrated).

```
SFTPA2 CRD mutation
        │ misfolding
        ▼
ER retention / no secretion ──► ER stress ──► UPR activation
        │                                           │
        │                                           ▼
        │                                  latent TGF-β1 secretion
        │                                  (↑TGF-β1, LTBP-1/4)
        │                                           │
        │                                           ▼
        │                              autocrine/paracrine TGF-β signaling
        │                                           │
        │                             ┌─────────────┴─────────────┐
        │                             ▼                           ▼
        │                      EMT + epithelial            bronchiolar metaplasia /
        │                      cell death                  epithelial dysregulation
        │                             │                           │
        ▼                             ▼                           ▼
 surfactant dysfunction     progressive UIP fibrosis      lung adenocarcinoma
        └──────────────► impaired gas exchange, PAH, respiratory failure
```

### Detail by category

- **Molecular pathways:** Core driver is **TGF-β1 signaling**, activated via the **UPR/ER-stress** axis; downstream IPF-associated pathways include Wnt/β-catenin and PI3K/Akt ([PMID: 42510961](https://pubmed.ncbi.nlm.nih.gov/42510961/)).
- **Cellular processes:** Protein misfolding, impaired proteostasis, ER stress, apoptosis/cell death, EMT, and fibroblast-to-myofibroblast differentiation.
- **Protein dysfunction:** Misfolding of the C-type lectin CRD → ER retention → gain-of-function proteotoxicity (not haploinsufficiency).
- **Immune involvement:** SP-A2 is an **innate host-defense collectin** that interacts with the alveolar macrophage and modulates surfactant structure/function ([PMID: 34484180](https://pubmed.ncbi.nlm.nih.gov/34484180/)); BAL neutrophilia and increased circulating immunoglobulin are observed.
- **Tissue damage mechanism:** Chronic fibrosis with ECM accumulation, driven by repetitive epithelial injury.
- **GO/CL suggestions:** biological processes — response to ER stress (GO:0034976), UPR (GO:0030968), TGF-β receptor signaling (GO:0007179), EMT (GO:0001837), surfactant homeostasis (GO:0043129); cell types — alveolar type II cell (CL:0002063), alveolar macrophage (CL:0000583), (myo)fibroblast (CL:0000057 / CL:0000186).

---

## 7. Anatomical Structures Affected

- **Organ level:** **Lung** (primary; UBERON:0002048), respiratory system (UBERON:0001004). Secondary: pulmonary vasculature → **pulmonary arterial hypertension**; right heart strain (cor pulmonale) as a downstream complication.
- **Tissue/cell level:** Alveolar epithelium (**alveolar type II cells**, CL:0002063) is the primary injured cell; **alveolar macrophages** (CL:0000583) interact with SP-A2; **fibroblasts/myofibroblasts** mediate matrix deposition. Fibrosis predominates in the **alveolar interstitium**; bronchiolar metaplasia is noted.
- **Subcellular level:** **Endoplasmic reticulum** (GO:0005789, site of mutant retention) is central; normal SP-A2 trafficking involves the **lamellar body** (GO:0042599), multivesicular body (GO:0005771), clathrin-coated endocytic vesicle (GO:0045334), and the secreted **surface film** at the air–liquid interface.
- **Localization / lateralization:** **Bilateral**, typically basal/subpleural-predominant fibrosis consistent with a UIP distribution.

---

## 8. Temporal Development

- **Onset:** Adult/late-onset, **insidious and chronic**; familial cases present earlier than sporadic (mean ~61 vs ~67 years; range 19–92) ([PMID: 22853774](https://pubmed.ncbi.nlm.nih.gov/22853774/)). SFTPA2 carriers skew younger than typical IPF.
- **Progression:** Chronic and **progressive**, often to respiratory failure. SRG-mutation ILD shows low transplant-free survival (**median ~44 months**) ([PMID: 36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/)); familial IPF shows faster physiological decline in some cohorts (e.g., FVC −2.36%/yr, DLCO −4.44%/yr) ([PMID: 41618408](https://pubmed.ncbi.nlm.nih.gov/41618408/)).
- **Disease course:** Progressive, lifelong; no spontaneous remission. Partial, temporary stabilization may occur with immunomodulation in some surfactant-gene cases.
- **Critical periods:** Early diagnosis (genetic ascertainment of at-risk relatives) opens a window for surveillance and timely transplant referral.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (OMIM 178500).
- **Penetrance/expressivity:** **Incomplete, likely age-dependent penetrance** and **variable expressivity** — some carriers develop fibrosis, some lung cancer, some both, and importantly some SFTPA2 carriers present with IPF **without** a personal/family history of lung cancer ([PMID: 36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/)).
- **Epidemiology:** ILD2 is rare. Surfactant biology mutations account for roughly **1–3% of IPF**, and functionally deleterious SFTPA2 variants were found in ~1.3% of an unselected IPF genome cohort ([PMID: 36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/)). Overall IPF prevalence is ~2–29 per 100,000 ([PMID: 35795226](https://pubmed.ncbi.nlm.nih.gov/35795226/)); ILD2 is a small genetic subset of this.
- **Carrier frequency / founder effects:** Pathogenic variants are rare and often family-private; no established founder variant for SFTPA2 specifically.
- **Demographics:** No strong ethnic predilection established for SFTPA2; Western IPF cohorts show surfactant-gene–driven architecture more than some Asian cohorts ([PMID: 41618408](https://pubmed.ncbi.nlm.nih.gov/41618408/)). IPF overall is more common in older males and smokers; SRG carriers are younger and less often male than typical IPF ([PMID: 36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/)).

---

## 10. Diagnostics

**Imaging.** High-resolution CT is central. Surfactant-gene ILD is characteristically associated with **ground-glass opacities and cysts** (in addition to UIP features): *"Surfactant genes mutations are usually associated with ground-glass opacities and cysts on CT scan..."* ([PMID: 32437840](https://pubmed.ncbi.nlm.nih.gov/32437840/)).

**Functional tests.** Pulmonary function testing shows a **restrictive pattern with decreased DLCO** (HP:0045051); carriers may present with markedly reduced FVC (~72% predicted) and DLCO (~46% predicted) ([PMID: 36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/)).

**BAL / labs.** Elevated BAL neutrophil proportion (HP:0032977) and increased circulating immunoglobulin (HP:0010702) have been annotated.

**Histopathology.** **UIP pattern** predominates in familial pulmonary fibrosis; bronchiolar metaplasia is noted on biopsy/explant in SFTPA2 carriers. Altered lung SP-A expression pattern was observed in 6/28 patients in a functional cohort ([PMID: 32855221](https://pubmed.ncbi.nlm.nih.gov/32855221/)).

**Genetic testing.** The definitive diagnostic. Recommended approaches: **NGS gene panels** for familial ILD covering surfactant genes (SFTPA1, SFTPA2, SFTPC, ABCA3, NKX2-1) and telomere genes (TERT, TERC, RTEL1, PARN), **whole-exome/whole-genome sequencing**, or **targeted single-gene testing** of SFTPA2. NGS has uncovered surfactant- and telomere-gene determinants and improves classification of overlapping ILD phenotypes ([PMID: 42510961](https://pubmed.ncbi.nlm.nih.gov/42510961/); [PMID: 36833253](https://pubmed.ncbi.nlm.nih.gov/36833253/)). Karyotyping, FISH, CMA, mtDNA, and repeat-expansion testing are **not applicable**.

**Clinical criteria / differential.** Diagnosis follows ATS/ERS IPF/ILD frameworks (clinical–radiologic–pathologic integration) plus family history and genetics. Differential includes sporadic IPF, telomere-related PF, SFTPC/ABCA3 disease, hypersensitivity pneumonitis, and connective-tissue-disease ILD. Distinguishing features favoring SFTPA2: younger onset, **longer telomeres** than typical IPF, cysts/ground-glass on CT, and strong family history of fibrosis ± lung adenocarcinoma ([PMID: 36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/)).

**Screening.** **Cascade genetic testing** of first-degree relatives and **lung-cancer CT surveillance** in variant carriers are recommended ([PMID: 38575158](https://pubmed.ncbi.nlm.nih.gov/38575158/)).

---

## 11. Outcome / Prognosis

**Survival.** Poor. SRG-mutation ILD carries **median transplant-free survival ~44 months**, with lower baseline FVC and DLCO ([PMID: 36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/)). Familial IPF can show faster physiological decline than sporadic disease.

**Morbidity.** Progressive dyspnea, oxygen dependence, exercise limitation, pulmonary arterial hypertension, and the burden of malignancy risk.

**Complications.** Respiratory failure, PAH/cor pulmonale, acute exacerbations, and **lung adenocarcinoma** (a defining complication of this subtype).

**Prognostic factors.** Baseline and rate-of-decline in FVC/DLCO, extent of fibrosis, PAH, and development of lung cancer. Lung transplantation can be a valid option with reportedly good post-transplant outcomes in surfactant-disorder patients, though lung-cancer screening before and after transplant is essential ([PMID: 38020562](https://pubmed.ncbi.nlm.nih.gov/38020562/)).

---

## 12. Treatment

There is **no SFTPA2-specific or curative therapy.** Management is supportive and disease-modifying:

- **Antifibrotics (standard of care for IPF-pattern disease):** **pirfenidone** and **nintedanib** (NCIT: Pirfenidone, Nintedanib) slow lung-function decline but do not reverse fibrosis ([PMID: 38263193](https://pubmed.ncbi.nlm.nih.gov/38263193/); [PMID: 38805909](https://pubmed.ncbi.nlm.nih.gov/38805909/)).
- **Immunomodulation (surfactant-gene–specific consideration):** Surfactant-gene ILD *"may improve with steroids, hydroxychloroquine or azithromycin"* ([PMID: 32437840](https://pubmed.ncbi.nlm.nih.gov/32437840/)) — a notable contrast to sporadic IPF, where immunosuppression is generally avoided.
- **Lung transplantation:** A valid option in adults with surfactant-disorder ILD, with good reported prognosis; immunosuppressive protocol was unchanged but close lung-cancer screening is required before and after ([PMID: 38020562](https://pubmed.ncbi.nlm.nih.gov/38020562/)).
- **Lung-cancer management/surveillance:** CT screening given high cancer risk in SRG carriers ([PMID: 38575158](https://pubmed.ncbi.nlm.nih.gov/38575158/)).
- **Supportive care:** Supplemental oxygen, pulmonary rehabilitation, vaccination, treatment of PAH and GERD.
- **Experimental / mechanistically rational agents (preclinical IPF):** Selective **Src-kinase inhibition** (saracatinib) ([PMID: 35998281](https://pubmed.ncbi.nlm.nih.gov/35998281/)), selective **PDE4 inhibitors** ([PMID: 38805909](https://pubmed.ncbi.nlm.nih.gov/38805909/)), **PD-1/PD-L1 checkpoint** modulation ([PMID: 38263193](https://pubmed.ncbi.nlm.nih.gov/38263193/)), proton-pump-inhibitor/pirfenidone combinations ([PMID: 36450789](https://pubmed.ncbi.nlm.nih.gov/36450789/)), and anti–miR-21 strategies ([PMID: 33394826](https://pubmed.ncbi.nlm.nih.gov/33394826/)) — none validated specifically for ILD2.

**Mechanistically, the UPR→TGF-β1→EMT axis** suggests TGF-β pathway inhibition and proteostasis/ER-stress modulation as rational targets; in vitro, pan-TGF-β antibody, TGF-β receptor antagonist, and LTBP silencing reversed mutant-SP-A2–induced EMT and cell death ([PMID: 23223528](https://pubmed.ncbi.nlm.nih.gov/23223528/)).

---

## 13. Prevention

- **Primary prevention:** No means to prevent the inherited mutation; **smoking cessation** and avoidance of fibrogenic/carcinogenic inhalational exposures are prudent in carriers.
- **Secondary prevention:** **Cascade genetic screening** of relatives, longitudinal PFT/HRCT monitoring of carriers, and **CT lung-cancer surveillance**.
- **Tertiary prevention:** Antifibrotics, pulmonary rehabilitation, oxygen, PAH management, timely transplant referral.
- **Genetic counseling:** Essential for autosomal-dominant, incompletely penetrant, cancer-predisposing disease; includes reproductive options (prenatal/preimplantation testing) and family planning guidance.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human SP-A is encoded by **two genes, SFTPA1 and SFTPA2**, whereas **rodents have a single Sftpa gene** ([PMID: 34484180](https://pubmed.ncbi.nlm.nih.gov/34484180/)). This architectural difference complicates direct modeling of SFTPA2-specific disease.
- **Natural disease in animals:** No well-established naturally occurring SFTPA2 orthologous Mendelian ILD is documented here; this is a knowledge gap for OMIA/veterinary resources.
- **Comparative biology:** SP-A's innate-immune/alveolar-macrophage function is conserved, but the two-gene human system means human SP-A1/SP-A2 variant biology is not fully recapitulated by single-gene rodents.

---

## 15. Model Organisms

- **In vitro / cellular models (primary evidence base):** Human **lung epithelial cell lines** expressing mutant SP-A2 reproduce ER retention, UPR activation, latent TGF-β1 secretion, EMT and cell death ([PMID: 23223528](https://pubmed.ncbi.nlm.nih.gov/23223528/)); recombinant-protein secretion assays demonstrate abolished secretion ([PMID: 19100526](https://pubmed.ncbi.nlm.nih.gov/19100526/); [PMID: 32855221](https://pubmed.ncbi.nlm.nih.gov/32855221/)).
- **Mouse models:** Humanized SP-A1/SP-A2 variant mice have been used to study differential effects on alveolar macrophages, surfactant structure/function, and survival after infection/oxidative stress ([PMID: 34484180](https://pubmed.ncbi.nlm.nih.gov/34484180/); [PMID: 32670284](https://pubmed.ncbi.nlm.nih.gov/32670284/)).
- **Limitations:** Single rodent Sftpa gene; models emphasize innate-immune/surfactant function rather than full UIP fibrosis + lung-cancer phenotype. No model fully recapitulates the complete human ILD2 syndrome.

---

## Mechanistic Model / Interpretation

ILD2 is best understood as a **proteostasis/gain-of-function disease of the alveolar type II cell**. A single CRD missense change in SFTPA2 is sufficient, in a dominant fashion, to misfold SP-A2 and trap it in the ER. Crucially, this is **not haploinsufficiency**: protein is made but not secreted, and it is the *retained, misfolded protein* that is pathogenic. The retained protein's ER burden triggers the UPR, and the UPR — in a manner specific to these mutants, not to generic misfolded proteins — licenses secretion of latent TGF-β1 together with its latency-binding proteins LTBP-1/4. TGF-β1 then acts as the central fibrogenic effector, driving EMT and epithelial death, which through repetitive injury and myofibroblast activation yields UIP-pattern fibrosis. A parallel branch — epithelial dysregulation and bronchiolar metaplasia — explains the signature lung-adenocarcinoma predisposition. This model is strongly supported because each step was experimentally demonstrated and the downstream EMT/death was *reversible* by blocking TGF-β or LTBPs.

| Upstream → Downstream | Evidence strength |
|---|---|
| SFTPA2 CRD mutation → misfolding | Strong (structural prediction + recombinant assays) |
| Misfolding → ER retention / no secretion | Strong (recombinant + 11-variant cohort) |
| ER retention → UPR | Strong (required for maximal TGF-β1 output) |
| UPR → latent TGF-β1 (+LTBP-1/4) | Strong, mutant-specific |
| TGF-β1 → EMT + cell death | Strong (reversible by blockade) |
| EMT/injury → UIP fibrosis | Inferred (integration + patient histology) |
| Epithelial dysregulation → lung adenocarcinoma | Epidemiologic/clinical |

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [19100526](https://pubmed.ncbi.nlm.nih.gov/19100526/) | **Foundational** — links SFTPA2 CRD missense (G231V, F198S) to familial fibrosis + lung cancer; ER retention, no secretion |
| [23223528](https://pubmed.ncbi.nlm.nih.gov/23223528/) | **Mechanism** — mutant SP-A2 → UPR → latent TGF-β1 → EMT; reversible by TGF-β/LTBP blockade |
| [32855221](https://pubmed.ncbi.nlm.nih.gov/32855221/) | 11 SFTPA1/SFTPA2 mutations: production preserved, secretion abolished; 93% family ILD/adenocarcinoma |
| [32437840](https://pubmed.ncbi.nlm.nih.gov/32437840/) | Imaging (ground-glass + cysts) and immunomodulatory treatment response |
| [36370864](https://pubmed.ncbi.nlm.nih.gov/36370864/) | SRG-mutation ILD: younger, lower FVC/DLCO, median survival ~44 months |
| [38575158](https://pubmed.ncbi.nlm.nih.gov/38575158/) | High lung-cancer risk in SRG carriers → CT screening |
| [36135709](https://pubmed.ncbi.nlm.nih.gov/36135709/) | SFTPA2 variants ~1.3% of IPF; may occur without cancer/family history; longer telomeres |
| [34484180](https://pubmed.ncbi.nlm.nih.gov/34484180/) | SP-A2 innate-immune/alveolar-macrophage role; human two-gene architecture |
| [22853774](https://pubmed.ncbi.nlm.nih.gov/22853774/) | Familial vs sporadic PF: younger onset (61.4 vs 66.6 y), UIP histology |
| [38020562](https://pubmed.ncbi.nlm.nih.gov/38020562/) | Lung transplant outcomes in surfactant-disorder ILD; cancer screening |
| [42510961](https://pubmed.ncbi.nlm.nih.gov/42510961/) | NGS in PF; TGF-β/Wnt/PI3K-Akt pathways |
| [35795226](https://pubmed.ncbi.nlm.nih.gov/35795226/) | IPF molecular genetics, prevalence, epigenetics |
| [41618408](https://pubmed.ncbi.nlm.nih.gov/41618408/) | Korean cohort; population-specific architecture; familial faster decline |
| [36833253](https://pubmed.ncbi.nlm.nih.gov/36833253/) | NGS supports diagnosis of familial interstitial pneumonia |

**Database annotations:** OMIM 178500; Monarch/HPO (12 ILD2 phenotype annotations); ClinVar (137 SFTPA2 records; pathogenic cluster in CRD); UniProt Q8IWL1 / InterPro IPR033990, IPR001304 / Pfam PF00059 (collectin C-type lectin CRD; secreted + lamellar body localization).

---

## Limitations and Knowledge Gaps

1. **Final fibrosis step is inferential.** The jump from demonstrated epithelial EMT/death to full UIP tissue remodeling integrates cell-based data with patient histology rather than a single demonstrated in vivo chain.
2. **Cancer-mechanism gap.** The link between SFTPA2 mutation and lung adenocarcinoma is epidemiologic/clinical; the molecular route (via bronchiolar metaplasia/epithelial dysregulation) is not mechanistically resolved.
3. **No faithful whole-animal model.** The human two-gene SP-A system is not recapitulated by single-Sftpa rodents; no model reproduces the complete fibrosis + cancer phenotype.
4. **Penetrance/modifiers unquantified.** Incomplete, age-dependent penetrance implies modifiers and GxE effects that remain uncharacterized for SFTPA2 specifically.
5. **Epidemiology is coarse.** ILD2-specific prevalence/incidence, sex ratio, and QoL metrics are not precisely established; figures are extrapolated from broader IPF/SRG cohorts.
6. **VUS burden.** A large fraction of ClinVar SFTPA2 records are VUS, complicating clinical interpretation.

---

## Proposed Follow-up Experiments / Actions

1. **AT2-specific / organoid models:** Generate patient-iPSC–derived AT2 organoids or humanized SFTPA1/SFTPA2 knock-in mice carrying p.Gly231Val/p.Phe198Ser to test whether the UPR→TGF-β1→EMT axis produces bona fide progressive fibrosis in vivo.
2. **Therapeutic proof-of-concept:** Test ER-stress/UPR modulators (e.g., chemical chaperones, PERK/IRE1 modulators) and TGF-β pathway inhibitors in these models, building on the demonstrated reversibility of EMT by TGF-β/LTBP blockade.
3. **Cancer-mechanism studies:** Lineage-trace bronchiolar metaplastic cells in carriers to dissect the fibrosis-to-adenocarcinoma transition and identify early biomarkers.
4. **Variant curation:** Apply functional secretion assays systematically to reclassify SFTPA2 VUS, building a ClinGen-style evidence framework.
5. **Natural-history registry:** Assemble an SFTPA2-specific cohort to quantify penetrance, decline rates, sex distribution, QoL, and transplant/cancer outcomes.
6. **Clinical protocol:** Formalize carrier management — cascade testing, antifibrotic timing, trial of immunomodulation in surfactant-gene cases, and structured CT lung-cancer surveillance.


## Artifacts

- [OpenScientist final report](Interstitial_Lung_Disease_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Interstitial_Lung_Disease_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800497` (3 mentions) - the report calls it "MONDO"; MONDO calls it **interstitial lung disease 2**
- `DOID:0060971` (1 mention) - the report calls it "DOID"; DOID calls it **interstitial lung disease 2**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0045051` (2 mentions) - the report calls it "Decreased DLCO", "restrictive pattern with decreased DLCO"; HP calls it **Decreased DLCO**
- `HP:0032977` (2 mentions) - the report calls it "Elevated BAL neutrophil proportion"; HP calls it **Elevated bronchoalveolar lavage fluid neutrophil proportion**
- `HP:0010702` (2 mentions) - the report calls it "Increased circulating immunoglobulin"; HP calls it **Increased circulating immunoglobulin concentration**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0045051` - called "Decreased DLCO", "restrictive pattern with decreased DLCO"