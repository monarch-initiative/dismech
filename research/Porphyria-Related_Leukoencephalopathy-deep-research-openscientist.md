---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:35:23.090032'
end_time: '2026-09-01T23:12:50.585416'
duration_seconds: 2247.5
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Porphyria-Related Leukoencephalopathy
  mondo_id: ''
  category: Mendelian
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
citation_count: 31
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 15
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:30987916
  - PMID:11478735
  relevance_assessed: 32
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - PMID:31952692
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002571
    reported_labels:
    - Autonomic dysfunction (tachycardia, hypertension)
    ontology_label: Achalasia
  - term_id: CHEBI:17549
    reported_labels:
    - Metabolic changes:** Accumulation of ALA
    ontology_label: 5-aminolevulinic acid
  - term_id: UBERON:0000955
    reported_labels:
    - "Organ level:** Primary \u2014 brain/CNS"
    ontology_label: brain
  labels_variant: 8
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
  path: Porphyria-Related_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Porphyria-Related_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Porphyria-Related Leukoencephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Porphyria-Related Leukoencephalopathy** covering all of the
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

# Porphyria-Related Leukoencephalopathy — Comprehensive Disease Report

*Category: Mendelian (with an overlapping acquired/reversible phenocopy)*
*Suggested MONDO context: the biallelic-HMBS Mendelian entity is closest to "acute intermittent porphyria-related leukoencephalopathy" (Kevelam et al. 2016); the reversible entity maps to porphyria + posterior reversible encephalopathy syndrome (PRES).*

---

## Summary

**"Porphyria-Related Leukoencephalopathy" is not a single disease but an umbrella covering two mechanistically distinct white-matter conditions that share a common biochemical root — deficient hydroxymethylbilane synthase (HMBS, also called porphobilinogen deaminase, PBGD) and neurotoxic accumulation of the heme precursor 5-aminolevulinic acid (ALA).** The first entity (A) is a **reversible posterior reversible encephalopathy syndrome (PRES)** occurring during acute neurovisceral attacks of monoallelic autosomal-dominant acute intermittent porphyria (AIP). The second entity (B) is a **true Mendelian, autosomal-recessive, childhood-onset progressive leukodystrophy** caused by **biallelic pathogenic HMBS variants** — the eponymous "acute intermittent porphyria-related leukoencephalopathy" first defined by Kevelam et al. in 2016 ([PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/)).

The distinction is clinically decisive. Entity A is an acute, largely reversible vasogenic-edema syndrome that resolves with attack management (avoidance of triggers, IV dextrose, IV hemin) and can be prevented with the liver-directed siRNA givosiran. Entity B is a slowly (or, in infantile forms, rapidly) progressive neurodegenerative leukodystrophy in which porphyrin precursors are **constitutively elevated in cerebrospinal fluid** and are **not corrected by hepatically directed therapies** — liver transplantation and haem arginate do not change the CSF biochemical phenotype nor halt progression ([PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)). This means the two entities require fundamentally different management framing, and a knowledge-base entry must keep them separate while acknowledging their shared enzyme and shared neurotoxic metabolite.

Across five iterations, seven findings were confirmed and 65 papers reviewed. The unifying causal chain is: **HMBS loss of function → hepatic (or systemic) de-repression of ALAS1 → overproduction of ALA and porphobilinogen (PBG) → ALA neurotoxicity (GABA-A receptor interference) and endothelial/blood-brain-barrier dysfunction → white-matter edema (reversible PRES) or progressive demyelination/cystic leukoencephalopathy (Mendelian form).** The report below organizes the evidence across the requested template sections.

---

## Key Findings

### Finding 1 — Two distinct entities under one name

Porphyria-related leukoencephalopathy comprises (A) reversible PRES during acute hepatic porphyria attacks and (B) a progressive biallelic-HMBS leukodystrophy. A systematic review of 46 patients with acute hepatic porphyria (AHP) complicated by PRES found a strong female predominance (84.8% women), young median age (24 ± 13.8 years), AIP as the most common subtype (41.3%), and a posterior-predominant lesion distribution — occipital (81.4%), parietal (65.1%), frontal (60.5%), subcortical (40%), and cortical (32.5%) ([PMID: 31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/)). Cerebral vasoconstriction was demonstrated in 41.7% of patients who underwent angiography, 19.6% had ischemic lesions, and only 4.3% developed long-term sequelae — underscoring the generally reversible nature of entity A.

> "The most common distributions of brain lesions were occipital (81.4%), parietal (65.1%), frontal (60.5%), subcortical (40%), and cortical (32.5%). Cerebral vasoconstriction was demonstrated in 41.7% of the patients who underwent angiography. 19.6% of the patients had ischemic lesions, and 4.3% developed long-term sequelae" — [PMID: 31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/)

By contrast, the Mendelian entity is a categorically different disease. As stated in the definitive natural-history/therapy report:

> "Leukodystrophy due to biallelic HMBS variants is a rare condition distinct from acute intermittent porphyria (AIP). It is characterised by progressive leukoencephalopathy rather than acute attacks of neurovisceral symptoms." — [PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)

### Finding 2 — HMBS is the causal gene; allele dosage determines phenotype

**HMBS** (hydroxymethylbilane synthase; HGNC:4982; chromosome 11q23.3; OMIM *609806) encodes the third enzyme of heme biosynthesis, porphobilinogen deaminase. More than 400 (some databases list >1000) pathogenic HMBS variants have been reported. **Heterozygous (monoallelic) loss of function → autosomal-dominant AIP** with very low penetrance. **Biallelic loss of function → autosomal-recessive leukodystrophy.** Both conditions arise from the same molecular defect — loss of HMBS protein function — with allele dosage governing severity:

> "deficiency of HMBS is associated with both autosomal dominant acute intermittent porphyria (AIP) and autosomal recessive homozygous dominant AIP (HD-AIP). Yet, both conditions result from loss-of-function of the HMBS protein" — [PMID: 42107342](https://pubmed.ncbi.nlm.nih.gov/42107342/)

The population genetics reveal a striking penetrance gap: the minimal estimated prevalence of pathogenic HMBS carriers is ~1/1299, yet symptomatic disease is far rarer (general-population penetrance 0.5–1%, versus ~22.9% in AIP families) ([PMID: 29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/)). In silico and in vitro analyses estimate that only ~1% of carriers of likely-pathogenic mutations ever develop acute attacks — highlighting the essential role of modifier genes and environmental triggers ([PMID: 27539938](https://pubmed.ncbi.nlm.nih.gov/27539938/)).

> "The minimal estimated prevalence of AIP in the general population was 1/1299" — [PMID: 29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/)

Biallelic pathogenic HMBS variants documented in leukodystrophy include **c.251C>A (p.Ala84Asp)**, **c.674G>A**, and **c.517C>T (p.Arg173Trp)**. A recent case documented biallelic HMBS causing progressive cystic leukoencephalopathy with elevated ALA/PBG in urine and PBG in CSF:

> "progressive cystic leukoencephalopathy and neurological decay. In his urine, 5-aminolevulinic acid and porphobilinogen were markedly elevated, but in cerebrospinal fluid just porphobilinogen" — [PMID: 41731635](https://pubmed.ncbi.nlm.nih.gov/41731635/)

### Finding 3 — Mechanism: hepatic ALA overproduction drives neurotoxicity and BBB dysfunction

HMBS deficiency in hepatocytes reduces heme output, which de-represses **ALAS1** (5-aminolevulinic acid synthase-1), the rate-limiting enzyme of heme synthesis, causing marked hepatic overproduction of ALA and PBG:

> "This deficiency leads to de-repression of the first and normally rate-controlling enzyme of the heme synthetic pathway, delta- or 5-aminolevulinic acid [ALA] synthase-1, and thus to marked up-regulation of this key enzyme and to marked hepatic overproduction of ALA" — [PMID: 30987916](https://pubmed.ncbi.nlm.nih.gov/30987916/)

ALA is directly neurotoxic. It interferes with GABAergic neurotransmission by inhibiting muscimol binding at GABA-A receptors in both rat and human brain synaptic membranes with comparable potency (IC50 199 vs 228 µM), a proposed basis for the seizures and encephalopathy:

> "ALA (0.1-10 mM) significantly inhibited the binding of [3H]muscimol (12 nM), with a similar potency in rat and human membranes (IC50 = 199 vs. 228 microM, respectively)" — [PMID: 11478735](https://pubmed.ncbi.nlm.nih.gov/11478735/)

Clinically, acute encephalopathy in AHP manifests as a triad of seizures, confusion, and/or blurred vision, with PRES detected in 42% of attacks and severe hyponatremia in 88% — pointing to acute endothelial dysfunction and blood-brain-barrier breakdown ([PMID: 36757574](https://pubmed.ncbi.nlm.nih.gov/36757574/)). The PRES lesions are typically reversible vasogenic edema — T2/FLAIR hyperintensity without diffusion restriction — reflecting transient BBB compromise ([PMID: 31649773](https://pubmed.ncbi.nlm.nih.gov/31649773/)).

### Finding 4 — Mouse models recapitulate porphyric motor axonal neuropathy

The **Pbgd-deficient (Pbgd−/−) mouse** faithfully models the biochemistry of human AIP: decreased hepatic Pbgd activity, increased ALA synthase activity, and massively increased urinary ALA after phenobarbital induction ([PMID: 8563760](https://pubmed.ncbi.nlm.nih.gov/8563760/)). Functionally, these mice develop impaired motor coordination, muscle weakness, and primary motor-axon degeneration:

> "femoral nerves of PBGD-/- mice exhibit a marked decrease in large-caliber (>8 microm) axons and ultrastructural changes consistent with primary motor axon degeneration, secondary Schwann cell reactions, and axonal regeneration" — [PMID: 10207164](https://pubmed.ncbi.nlm.nih.gov/10207164/)

> "These mice exhibit the typical biochemical characteristics of human AIP, notably, decreased hepatic Pbgd activity, increased delta-aminolevulinic acid synthase activity and massively increased urinary excretion of the heme precursor, delta-aminolevulinic acid after treatment with drugs such as phenobarbital" — [PMID: 8563760](https://pubmed.ncbi.nlm.nih.gov/8563760/)

Hepatocyte transplantation of wild-type cells reduced plasma ALA/PBG by ~50% with only 2.7% engraftment — providing proof of concept that even partial hepatic correction lowers systemic precursors ([PMID: 23582197](https://pubmed.ncbi.nlm.nih.gov/23582197/)). Notably, these models capture the peripheral axonal neuropathy of AIP but do not, to date, reproduce the central biallelic leukodystrophy — a key model-organism gap.

### Finding 5 — Diagnosis and the distinct Mendelian phenotype/MRI pattern; NfL biomarker

Acute attacks are diagnosed by markedly elevated urinary PBG and ALA, screened with rapid bedside tests (Hoesch/Watson-Schwartz) and confirmed quantitatively ([PMID: 41704990](https://pubmed.ncbi.nlm.nih.gov/41704990/), [PMID: 41069899](https://pubmed.ncbi.nlm.nih.gov/41069899/)). **Serum neurofilament light chain (NfL)** is an emerging biomarker of axonal damage, elevated ~68-fold during acute attacks and correlating strongly with ALA/PBG:

> "During acute attacks, serum NfL levels were 68 times higher compared to normal controls and disclosed a strong correlation with ALA and PBG levels" — [PMID: 38715693](https://pubmed.ncbi.nlm.nih.gov/38715693/)

The Mendelian biallelic-HMBS leukodystrophy has a recognizable clinical and radiological signature. In a series of 6 adults:

> "All six affected individuals presented with slowly progressive spasticity, ataxia, peripheral neuropathy, with or without mild cognitive impairment, and/or ocular disease with onset in childhood or adolescence. Their brain MRIs show mainly confluent signal abnormalities in the periventricular and deep white matter and bilateral thalami" — [PMID: 34089223](https://pubmed.ncbi.nlm.nih.gov/34089223/)

Severe infantile biallelic cases present even earlier — with ataxia, hypotonia, and seizures from ~3 months of age, and substantial irreversible injury already present at diagnosis ([PMID: 42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/)).

### Finding 6 — Treatment: hepatic-directed therapies help attacks but NOT the Mendelian leukodystrophy

For acute attacks (entity A), the AGA Clinical Practice Update lists the cornerstones of management:

> "The cornerstones of management include discontinuation of porphyrinogenic drugs and chemicals, administration of oral or intravenous dextrose and intravenous hemin, and use of analgesics and antiemetics" — [PMID: 36642627](https://pubmed.ncbi.nlm.nih.gov/36642627/)

**Givosiran (Givlaari)**, an FDA-approved liver-directed siRNA targeting ALAS1, produces durable normalization of ALA and significantly reduces attack rates and hemin need; approved for adults and adolescents ≥12 years:

> "Givosiran is a novel siRNA-based therapy targeted specifically to hepatocytes to inhibit ALA synthase 1, the first and rate-limiting step in heme biosynthesis. Patients with frequent recurrent attacks treated with givosiran had durable normalization of ALA and significantly reduced numbers of acute attacks" — [PMID: 33769375](https://pubmed.ncbi.nlm.nih.gov/33769375/)

Liver transplantation remains the only curative option for refractory AIP ([PMID: 41287633](https://pubmed.ncbi.nlm.nih.gov/41287633/)). **Critically, none of these hepatic-directed strategies works for the biallelic leukodystrophy**, because the CSF precursor accumulation is generated behind/within the blood-brain barrier and is constitutively elevated:

> "porphyrin precursor levels are constitutively elevated in the cerebrospinal fluid and are not reduced by haem arginate therapy. Liver transplantation and hepatically directed therapies are not likely to be effective for leukodystrophy due to biallelic" — [PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)

Givosiran improved a biallelic case biochemically, but neurological injury was largely irreversible ([PMID: 41731635](https://pubmed.ncbi.nlm.nih.gov/41731635/), [PMID: 42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/)). Seizures during attacks require **non-porphyrinogenic anticonvulsants — levetiracetam is preferred**; enzyme-inducing agents (phenytoin, valproate, carbamazepine, barbiturates) can precipitate attacks ([PMID: 31649773](https://pubmed.ncbi.nlm.nih.gov/31649773/)).

### Finding 7 — The eponymous entity was defined by Kevelam et al. 2016

The named disease "AIP-related leukoencephalopathy" was established in a single family with 3 affected members sharing a distinct MRI pattern:

> "We identified 3 family members with a similar MRI pattern characterized by symmetrical signal abnormalities in the periventricular and deep cerebral white matter, thalami, and central part of the pons. Cerebellar atrophy was noted in advanced disease stages." — [PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/)

Its inheritance is autosomal recessive by biallelic HMBS variants:

> "Whole-exome sequencing revealed compound heterozygous missense variants in the HMBS gene, both associated with the autosomal dominant disorder acute intermittent porphyria. Sanger sequencing of 6 healthy siblings confirmed the bi-allelic location of the variants and segregation with the disease." — [PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/)

And its biochemistry is distinctively mild relative to florid AIP, with only slight-to-moderate precursor elevation and 50–66% residual enzyme activity:

> "Patients had a slight and moderate increase in urinary and plasma porphobilinogen and 5'-aminolevulinic acid, respectively, and a 50% to 66% decrease in hydroxymethylbilane synthase enzyme activity compared to normal." — [PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/)

---

## Section-by-Section Report

### 1. Disease Information

- **Overview:** Two entities. **(A)** Porphyria-associated PRES — a reversible posterior-predominant vasogenic-edema encephalopathy occurring during acute hepatic porphyria attacks (most often AIP). **(B)** Biallelic-HMBS leukodystrophy — a Mendelian, autosomal-recessive, childhood/adolescent-onset progressive white-matter disease (the eponymous "acute intermittent porphyria-related leukoencephalopathy," Kevelam 2016).
- **Key identifiers:** Gene **HMBS** (OMIM *609806). AIP: OMIM #176000; Orphanet ORPHA:79276; ICD-10 E80.21; ICD-11 5C58.10; MeSH D017118 (Porphyria, Acute Intermittent). PRES: MeSH D054038 (Posterior Leukoencephalopathy Syndrome); ICD-11 8D43. The biallelic leukodystrophy does not yet have a widely adopted standalone OMIM number and is described under HMBS-related disease. Suggested MONDO: map entity B to the biallelic HMBS leukodystrophy concept; entity A to porphyria + PRES.
- **Synonyms/alternatives:** AIP-related leukoencephalopathy; HMBS-related leukoencephalopathy/leukodystrophy; biallelic HMBS leukodystrophy; homozygous-dominant AIP (HD-AIP) with CNS disease; porphyria-associated PRES; reversible posterior leukoencephalopathy in porphyria.
- **Information source:** Predominantly aggregated disease-level resources plus individual case reports and small case series (the Mendelian form is described in <20 individuals worldwide); the PRES association derives from a 46-patient systematic review and numerous single-patient reports.

### 2. Etiology

- **Causal factors:** Genetic — loss-of-function variants in **HMBS**. Monoallelic → dominant AIP (entity A substrate); biallelic → recessive leukodystrophy (entity B). Entity A additionally requires an **environmental/physiological trigger** to precipitate an attack.
- **Genetic risk factors:** Pathogenic HMBS variants (>400 reported). Modifier genes influence penetrance — **CYP2D6*4 and *5 defective alleles may be protective** against attacks (CYP2D6 as a penetrance-modifying gene) ([PMID: 30808393](https://pubmed.ncbi.nlm.nih.gov/30808393/)); oligogenic/environmental modifiers shift inheritance from a purely dominant to an oligogenic model ([PMID: 29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/)).
- **Environmental/trigger risk factors:** Porphyrinogenic drugs (barbiturates, sulfonamides, enzyme-inducing anticonvulsants, some hormonal agents e.g., levonorgestrel), fasting/low-carbohydrate states, alcohol, endocrine/hormonal fluctuations (premenstrual), stress, infection (including COVID-19), and surgery/anesthesia. Female sex and reproductive age are strong demographic risk factors for attacks.
- **Protective factors:** Adequate carbohydrate intake; avoidance of porphyrinogenic drugs; possibly CYP2D6 loss-of-function alleles (genetic).
- **Gene–environment interactions:** The ~1% penetrance of likely-pathogenic HMBS variants shows attacks are contingent on interactions between the causal allele, modifier genotypes (CYP2D6), and environmental triggers that induce ALAS1 ([PMID: 27539938](https://pubmed.ncbi.nlm.nih.gov/27539938/)).

### 3. Phenotypes

**Entity A (porphyria/PRES attack):**
| Phenotype | HPO term (suggested) | Frequency / notes |
|---|---|---|
| Seizures | HP:0001250 | Common in AE; PRES in 42% of AE attacks |
| Encephalopathy/confusion | HP:0001298 | Part of AE triad |
| Visual disturbance/cortical blindness | HP:0000618 | Occipital-predominant edema |
| Abdominal pain (neurovisceral) | HP:0002027 | Hallmark of attacks |
| Hyponatremia (SIADH) | HP:0002902 | 88% of severe AE attacks |
| Peripheral motor neuropathy | HP:0007141 | Axonal, can cause paralysis |
| Autonomic dysfunction (tachycardia, hypertension) | HP:0002571 | Frequent |

**Entity B (biallelic leukodystrophy):**
| Phenotype | HPO term (suggested) | Onset/course |
|---|---|---|
| Spastic paraparesis | HP:0002061 | Childhood/adolescent, slowly progressive |
| Cerebellar ataxia | HP:0001251 | Progressive |
| Peripheral neuropathy | HP:0009830 | Progressive |
| Cognitive impairment (mild) | HP:0100543 | Variable |
| Optic atrophy | HP:0000648 | In subset |
| Nystagmus / gaze palsy | HP:0000639 / HP:0000496 | In subset |
| Leukoencephalopathy | HP:0002352 | Defining feature |
| Infantile hypotonia/seizures | HP:0001290 / HP:0001250 | Severe infantile form (~3 months) |

- **QoL impact:** Entity A attacks are severely disabling acutely but usually reversible (4.3% long-term sequelae; [PMID: 31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/)); rare severe cases lead to lasting disability ([PMID: 38274883](https://pubmed.ncbi.nlm.nih.gov/38274883/)). Entity B causes chronic, accruing disability (mobility, vision, cognition), lifelong.

### 4. Genetic / Molecular Information

- **Causal gene:** **HMBS** (HGNC:4982), OMIM *609806, chromosome 11q23.3. Encodes porphobilinogen deaminase (EC 2.5.1.61), the 3rd enzyme of heme biosynthesis; substrate porphobilinogen (CHEBI:17381) → hydroxymethylbilane.
- **Variant classification/types:** >400 reported pathogenic/likely-pathogenic variants — missense, nonsense, frameshift, splice-site, and small indels. Documented leukodystrophy variants: **c.251C>A (p.Ala84Asp)**, **c.674G>A**, **c.517C>T (p.Arg173Trp)**; example AIP variants include c.669_698del30 (Spanish founder), c.1005dupC, c.405_406delAA. Functional consequence: **loss of function** in both dominant and recessive forms ([PMID: 42107342](https://pubmed.ncbi.nlm.nih.gov/42107342/)).
- **Allele frequency:** Combined likely-pathogenic HMBS allele frequency in Caucasians ~0.00056; carrier prevalence ~1/1299 ([PMID: 27539938](https://pubmed.ncbi.nlm.nih.gov/27539938/), [PMID: 29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/)).
- **Origin:** Germline (both entities).
- **Modifier genes:** CYP2D6 (penetrance modifier; *4/*5 possibly protective) ([PMID: 30808393](https://pubmed.ncbi.nlm.nih.gov/30808393/)); additional oligogenic modifiers proposed ([PMID: 29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/)).
- **Epigenetics / chromosomal abnormalities:** Not established as contributors; no recurrent large-scale rearrangements described for these entities.

### 5. Environmental Information

- **Environmental factors / toxins:** Porphyrinogenic drugs and chemicals that induce hepatic ALAS1 (barbiturates, sulfonamides, rifampin, many anticonvulsants, certain steroids).
- **Lifestyle factors:** Caloric restriction/fasting, alcohol, smoking; hormonal contraceptives can trigger attacks.
- **Infectious agents:** No causal pathogen; however, infections (including COVID-19) can trigger/unmask attacks and precipitate PRES ([PMID: 40186107](https://pubmed.ncbi.nlm.nih.gov/40186107/)). Entity B (Mendelian leukodystrophy) is not trigger-dependent.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **HMBS loss-of-function variant** (monoallelic or biallelic) *leads to* reduced porphobilinogen deaminase activity (50–66% residual in biallelic leukodystrophy; more severe deficits or trigger-dependent decompensation in AIP).
2. Reduced HMBS activity *results in* diminished heme output in hepatocytes (and, inferred, in CNS-resident cells for the biallelic form).
3. Low heme *de-represses* **ALAS1**, the rate-limiting enzyme (demonstrated hepatic mechanism; [PMID: 30987916](https://pubmed.ncbi.nlm.nih.gov/30987916/)).
4. ALAS1 up-regulation *causes* overproduction and accumulation of **ALA** and **PBG** (systemic in AIP; constitutively elevated in CSF in biallelic leukodystrophy — [PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)).
5. **Branch A (attack/PRES):** Circulating ALA *leads to* (i) GABA-A receptor interference (demonstrated in vitro; [PMID: 11478735](https://pubmed.ncbi.nlm.nih.gov/11478735/)) and neuronal hyperexcitability, and (ii) endothelial/blood-brain-barrier dysfunction (inferred) *causing* reversible vasogenic edema in posterior white matter (PRES), often with cerebral vasoconstriction and hyponatremia.
6. **Branch A resolution:** Removal of trigger + lowering hepatic ALA (dextrose, hemin, givosiran) *results in* normalization and radiological/clinical reversal (4.3% sequelae).
7. **Branch B (Mendelian leukodystrophy):** Chronic CNS precursor accumulation *leads to* progressive oligodendrocyte/white-matter injury, demyelination, and (in some) cystic change and thalamic/pontine involvement — largely irreversible; hepatic-directed therapy does not correct CSF precursors (demonstrated; [PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)).
8. In both branches, ALA/PBG neurotoxicity *causes* axonal degeneration (peripheral motor axonopathy; modeled in Pbgd−/− mice — [PMID: 10207164](https://pubmed.ncbi.nlm.nih.gov/10207164/); reflected by ~68-fold NfL rise — [PMID: 38715693](https://pubmed.ncbi.nlm.nih.gov/38715693/)).

- **Molecular pathway:** Heme biosynthesis (KEGG hsa00860; Reactome R-HSA-189451). Suggested GO: heme biosynthetic process (GO:0006783); porphyrin-containing compound metabolic process (GO:0006778).
- **Cellular processes:** Neuronal excitotoxicity, endothelial dysfunction, demyelination, axonal degeneration, oxidative stress (ALA autoxidation generates reactive oxygen species — inferred contributor).
- **Protein dysfunction:** PBGD is a morpheein — an equilibrium of octamer/hexamer/dimer assemblies; destabilizing variants reduce active-octamer function ([PMID: 31952692](https://pubmed.ncbi.nlm.nih.gov/31952692/)). UniProt P08397.
- **Metabolic changes:** Accumulation of ALA (CHEBI:17549) and PBG (CHEBI:17381); relative heme deficiency.
- **Cell types (suggested CL):** neuron (CL:0000540), oligodendrocyte (CL:0000128), brain microvascular endothelial cell (CL:1001568/CL:0002139), hepatocyte (CL:0000182), motor neuron/Schwann cell (CL:0002573).
- **Subcellular (GO CC):** mitochondrion (GO:0005739; ALAS1/ALA synthesis), cytosol (GO:0005829; HMBS reaction).

### 7. Anatomical Structures Affected

- **Organ level:** Primary — brain/CNS (UBERON:0000955), particularly cerebral white matter (UBERON:0002316), and peripheral nerves (UBERON:0001021). Secondary/systemic — liver (UBERON:0002107; source of precursors), autonomic nervous system.
- **Regional (entity A / PRES):** Posterior-predominant — occipital (UBERON:0002021, 81.4%), parietal (65.1%), frontal (60.5%) cortex/subcortex; bilateral, often symmetric ([PMID: 31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/)).
- **Regional (entity B):** Periventricular and deep cerebral white matter, bilateral thalami (UBERON:0001897), central pons (UBERON:0000988), with cerebellar atrophy in advanced disease; bilateral/symmetric ([PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/), [PMID: 34089223](https://pubmed.ncbi.nlm.nih.gov/34089223/)).
- **Tissue/cell:** White matter (myelin/oligodendrocytes), large-caliber motor axons, cerebral microvascular endothelium.

### 8. Temporal Development

- **Entity A onset:** Acute/subacute during attacks; typically young adults (median 24 y), 84.8% female. Course: episodic, reversible; recurrent PRES possible ([PMID: 31153599](https://pubmed.ncbi.nlm.nih.gov/31153599/)).
- **Entity B onset:** Childhood/adolescent (slowly progressive form) or infantile (~3 months, severe form). Course: chronic, progressive, largely irreversible; critical window for intervention is likely very early, before fixed white-matter injury ([PMID: 42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/)).
- **Remission:** Entity A remits with treatment/trigger removal; pregnancy can transiently remit AHP with postpartum escalation ([PMID: 42367478](https://pubmed.ncbi.nlm.nih.gov/42367478/)). Entity B does not remit.

### 9. Inheritance and Population

- **Epidemiology:** AIP minimal prevalence ~1/1299 carriers; symptomatic AIP far rarer (~5.4/million symptomatic Europeans; regional founder populations higher, e.g., 17.7/million in Murcia, Spain). Biallelic leukodystrophy is ultra-rare (<20 reported individuals).
- **Inheritance:** Entity A — autosomal dominant, markedly reduced penetrance (~1% of likely-pathogenic carriers; ~22.9% in AIP families). Entity B — autosomal recessive (biallelic HMBS).
- **Penetrance/expressivity:** Incomplete, modifier- and trigger-dependent (A); more consistent but variable severity (B).
- **Founder effects/consanguinity:** Spanish founder mutation c.669_698del30 ([PMID: 30808393](https://pubmed.ncbi.nlm.nih.gov/30808393/)); recessive entity B favored by consanguinity/compound heterozygosity.
- **Sex ratio:** Attacks strongly female-predominant (~85% women); entity B without strong sex bias.
- **Anticipation/mosaicism:** Not characteristic (no repeat expansion).

### 10. Diagnostics

- **Biochemistry (first-line):** Markedly elevated urinary **PBG** and **ALA** during attacks; rapid screening with Hoesch/Watson-Schwartz tests ([PMID: 41704990](https://pubmed.ncbi.nlm.nih.gov/41704990/), [PMID: 41069899](https://pubmed.ncbi.nlm.nih.gov/41069899/)). In biallelic leukodystrophy, precursor elevations may be mild but CSF PBG/ALA are constitutively elevated ([PMID: 41731635](https://pubmed.ncbi.nlm.nih.gov/41731635/), [PMID: 41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/)).
- **Biomarkers:** Serum NfL (axonal damage; ~68-fold in attacks) ([PMID: 38715693](https://pubmed.ncbi.nlm.nih.gov/38715693/)); hyponatremia and elevated CK as clues; transaminase elevation common.
- **Imaging:** MRI — entity A shows T2/FLAIR posterior hyperintensity without diffusion restriction (reversible vasogenic edema/PRES) ([PMID: 31649773](https://pubmed.ncbi.nlm.nih.gov/31649773/)); entity B shows confluent periventricular/deep white matter + bilateral thalamic ± pontine signal change, cerebellar atrophy late ([PMID: 27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/)).
- **Genetic testing:** HMBS single-gene sequencing or 4-gene AHP panel; zygosity determination is essential (mono- vs biallelic). WES/WGS useful for the leukodystrophy (compound heterozygosity often found on reanalysis; note WGS can be negative when the clinicobiochemical phenotype is compelling — [PMID: 42367478](https://pubmed.ncbi.nlm.nih.gov/42367478/)). Enzyme assay: erythrocyte/leukocyte HMBS activity (50–66% residual in biallelic leukodystrophy).
- **Differential diagnosis:** Hypertensive/eclamptic PRES, other leukodystrophies, Guillain-Barré (peripheral neuropathy mimicry), cyclic vomiting syndrome, POTS (screening generally low-yield — [PMID: 40856938](https://pubmed.ncbi.nlm.nih.gov/40856938/)), heavy-metal toxicity, mitochondrial disease.

### 11. Outcome / Prognosis

- **Entity A:** Generally favorable — 4.3% long-term sequelae, 19.6% ischemic lesions in the PRES cohort ([PMID: 31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/)); mortality low with prompt treatment, but severe attacks can cause lasting disability or death. Chronic AHP complications include hepatocellular carcinoma, chronic kidney disease, and hypertension ([PMID: 41287633](https://pubmed.ncbi.nlm.nih.gov/41287633/)).
- **Entity B:** Poor — progressive disability; infantile form leaves irreversible injury by diagnosis with no effective disease-modifying therapy ([PMID: 42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/)).
- **Prognostic markers:** NfL for axonal damage; ALA/PBG burden; residual HMBS activity; age of onset (earlier = worse in entity B).

### 12. Treatment

| Intervention | Entity A (attacks/PRES) | Entity B (leukodystrophy) | NCIT (suggested) |
|---|---|---|---|
| Trigger removal + IV/oral dextrose | First-line, effective | Not applicable | C1948 (glucose) |
| IV hemin / haem arginate | Effective for attacks | Ineffective (no CSF change) | C29027 (hemin) |
| Givosiran (siRNA vs ALAS1) | Prophylaxis; reduces attacks | Biochemical improvement only; injury irreversible | — |
| Liver transplantation | Curative for refractory AIP | Ineffective | C15329 |
| Levetiracetam (seizures) | Preferred (non-porphyrinogenic) | Symptomatic | C61814 |
| Analgesics/antiemetics, Na+ correction | Supportive | Supportive | — |

Avoid enzyme-inducing anticonvulsants (phenytoin, valproate, carbamazepine, barbiturates) — they can precipitate attacks ([PMID: 31649773](https://pubmed.ncbi.nlm.nih.gov/31649773/)). Rehabilitation (PT/OT) for chronic deficits. **No disease-modifying therapy currently exists for biallelic HMBS deficiency** ([PMID: 42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/)). Pharmacogenomics: CYP2D6 genotype may inform attack risk ([PMID: 30808393](https://pubmed.ncbi.nlm.nih.gov/30808393/)).

### 13. Prevention

- **Primary:** Avoid porphyrinogenic drugs, fasting, and alcohol; maintain carbohydrate intake; trigger education (entity A). Not applicable to genetically determined onset of entity B.
- **Secondary/prophylaxis:** Givosiran or off-label prophylactic hemin for recurrent attackers; hormone suppression for menstrual-cycle-linked attacks ([PMID: 39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/)).
- **Tertiary:** Monitor chronic AHP complications (HCC, CKD, hypertension) ([PMID: 41287633](https://pubmed.ncbi.nlm.nih.gov/41287633/)).
- **Genetic counseling / screening:** Cascade family testing; carrier screening; determine zygosity for recessive-risk counseling. No routine newborn screening.

### 14. Other Species / Natural Disease

- **Orthology:** Hmbs is conserved (mouse *Hmbs*, NCBI Gene 15288; rat ortholog present). No well-documented naturally occurring porphyria-related leukoencephalopathy in companion animals/wildlife identified in this investigation. Comparative relevance derives chiefly from engineered rodent models (below).

### 15. Model Organisms

- **Primary model:** **Pbgd/Hmbs-deficient (Pbgd−/−) mouse** — biochemically faithful to human AIP (↓hepatic Pbgd, ↑ALAS activity, massive urinary ALA after phenobarbital) and reproduces **porphyric motor axonal neuropathy** (loss of large-caliber femoral-nerve axons, primary motor axon degeneration) ([PMID: 8563760](https://pubmed.ncbi.nlm.nih.gov/8563760/), [PMID: 10207164](https://pubmed.ncbi.nlm.nih.gov/10207164/)).
- **Therapeutic-model applications:** Hepatocyte transplantation lowered plasma ALA/PBG ~50% with 2.7% engraftment ([PMID: 23582197](https://pubmed.ncbi.nlm.nih.gov/23582197/)); non-viral PBGD gene delivery tested with limited hepatic expression ([PMID: 15110317](https://pubmed.ncbi.nlm.nih.gov/15110317/)).
- **Limitations:** Existing models capture peripheral neuropathy and hepatic biochemistry but **do not reproduce the biallelic central leukodystrophy** — a major gap. Resources: MGI for murine alleles.

---

## Mechanistic Model / Interpretation

```
            HMBS loss-of-function variant
                        │
          (monoallelic) │ (biallelic, ~34–66% residual activity)
        ┌───────────────┴────────────────────┐
        ▼                                     ▼
   Latent AIP carrier                Constitutive CNS + systemic
   (needs a trigger)                 precursor accumulation
        │                                     │
   + trigger (drug/fast/                       │
     hormone/infection)                        │
        ▼                                     ▼
  ↓ hepatic heme → ALAS1 de-repression   ↑ CSF ALA/PBG (behind BBB;
        │                                 hepatic therapy cannot correct)
        ▼                                     │
  ↑↑ ALA / PBG (systemic)                      │
        │                                     │
   ┌────┴─────┐                                │
   ▼          ▼                                ▼
GABA-A     endothelial/BBB              chronic oligodendrocyte /
inhibition dysfunction                 white-matter injury
   │          │                                │
   ▼          ▼                                ▼
seizures,  vasogenic edema             progressive spasticity,
encephalop. (posterior → PRES)         ataxia, neuropathy,
   │          │                        cystic leukoencephalopathy
   └────┬─────┘                                │
        ▼                                     ▼
  REVERSIBLE (Entity A)              LARGELY IRREVERSIBLE (Entity B)
  responds to dextrose/hemin/        no disease-modifying therapy;
  givosiran/trigger removal          hepatic-directed Rx ineffective
```

The two entities are best understood as **the same biochemical lesion expressed at two doses and two timescales**. Monoallelic disease produces intermittent, trigger-dependent, systemic precursor surges that transiently poison the posterior cerebral vasculature and GABAergic neurons — reversible if caught. Biallelic disease produces a lower-grade but *constant, compartmentalized* precursor excess within the CNS that the liver-centric therapeutic toolkit cannot reach, yielding cumulative, fixed white-matter damage.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [27558376](https://pubmed.ncbi.nlm.nih.gov/27558376/) | Founding | Defines the eponymous biallelic-HMBS leukodystrophy, MRI signature, AR inheritance, mild biochemistry |
| [34089223](https://pubmed.ncbi.nlm.nih.gov/34089223/) | Confirmatory | Expands phenotype/MRI in 6 adults |
| [41377573](https://pubmed.ncbi.nlm.nih.gov/41377573/) | Pivotal | Shows hepatic-directed therapy fails to correct CSF precursors or halt progression |
| [41731635](https://pubmed.ncbi.nlm.nih.gov/41731635/) | Case | Biallelic cystic leukoencephalopathy; CSF precursor accumulation |
| [42396593](https://pubmed.ncbi.nlm.nih.gov/42396593/) | Case | Severe infantile form; irreversible injury; liver transplant of limited benefit |
| [31706631](https://pubmed.ncbi.nlm.nih.gov/31706631/) | Systematic review | PRES lesion distribution, vasoconstriction, outcomes (n=46) |
| [42107342](https://pubmed.ncbi.nlm.nih.gov/42107342/) | Genetics | HMBS LOF underlies both dominant and recessive disease |
| [29360981](https://pubmed.ncbi.nlm.nih.gov/29360981/) | Epidemiology | Prevalence/penetrance; oligogenic model |
| [27539938](https://pubmed.ncbi.nlm.nih.gov/27539938/) | Genetics | ~1% penetrance of likely-pathogenic variants |
| [30987916](https://pubmed.ncbi.nlm.nih.gov/30987916/) | Mechanism | ALAS1 de-repression / hepatic ALA overproduction |
| [11478735](https://pubmed.ncbi.nlm.nih.gov/11478735/) | Mechanism | ALA inhibits GABA-A receptor binding |
| [36757574](https://pubmed.ncbi.nlm.nih.gov/36757574/) | Clinical | AE triad; PRES 42%, hyponatremia 88% |
| [8563760](https://pubmed.ncbi.nlm.nih.gov/8563760/) / [10207164](https://pubmed.ncbi.nlm.nih.gov/10207164/) | Model | Pbgd−/− mouse biochemistry and motor axonopathy |
| [38715693](https://pubmed.ncbi.nlm.nih.gov/38715693/) | Biomarker | NfL ~68× in attacks, correlates with ALA/PBG |
| [36642627](https://pubmed.ncbi.nlm.nih.gov/36642627/) | Guideline | AGA acute management |
| [33769375](https://pubmed.ncbi.nlm.nih.gov/33769375/) / [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | Therapy | Givosiran mechanism/efficacy |
| [30808393](https://pubmed.ncbi.nlm.nih.gov/30808393/) | Modifier | CYP2D6 as penetrance modifier / protective alleles |
| [31649773](https://pubmed.ncbi.nlm.nih.gov/31649773/) | Clinical | Reversible vasogenic edema; anticonvulsant choice |

---

## Limitations and Knowledge Gaps

1. **Small sample size for the Mendelian entity.** The biallelic-HMBS leukodystrophy is described in fewer than ~20 individuals worldwide; phenotype frequencies, natural history, and genotype–phenotype correlations are provisional.
2. **Nosological ambiguity.** "Porphyria-related leukoencephalopathy" conflates a reversible acquired phenocopy (PRES during attacks) with a true Mendelian disease. Knowledge-base curation must keep them separate to avoid propagating errors in prognosis and treatment.
3. **Mechanism partly inferred.** The endothelial/BBB-dysfunction step of PRES and the exact CNS cell-type target of biallelic precursor toxicity are not fully demonstrated; direct human tissue and single-cell data are lacking.
4. **Model gap.** No animal model reproduces the central biallelic leukodystrophy, limiting mechanistic and therapeutic study of entity B.
5. **No CNS-penetrant therapy.** Because hepatic-directed drugs do not reach CNS precursor pools, there is currently no disease-modifying option for entity B.
6. **Genetic testing pitfalls.** WGS can be negative when the clinicobiochemical phenotype is compelling; zygosity interpretation and reanalysis are critical.

## Proposed Follow-up Experiments / Actions

1. **Develop a biallelic-Hmbs CNS model** (e.g., conditional/neural-restricted Hmbs knockout or humanized knock-in of leukodystrophy variants) to test whether constitutive CNS ALA/PBG drives demyelination and to serve as a therapeutic platform.
2. **Test CNS-penetrant precursor-lowering strategies** — CNS-directed ALAS1 knockdown (intrathecal siRNA/ASO), AAV-mediated HMBS gene replacement to CNS, or small molecules that stabilize the PBGD octamer — since liver-directed therapy is proven ineffective for entity B.
3. **Prospective natural-history registry** for biallelic-HMBS individuals with serial MRI, CSF ALA/PBG, and serum NfL to define progression rate and identify a treatment window.
4. **Validate NfL and CSF precursor ratios** as prognostic/monitoring biomarkers across both entities.
5. **Characterize the CNS cell-type target** via single-cell/spatial transcriptomics of affected white matter (postmortem or organoid), testing oligodendrocyte and microvascular-endothelial vulnerability.
6. **Curation action:** create/align MONDO entries that explicitly separate (A) porphyria-associated PRES from (B) biallelic-HMBS leukodystrophy, cross-referencing HMBS (HGNC:4982), OMIM *609806, and the Kevelam 2016 definition.

---

*Report compiled from 5 discovery iterations, 7 confirmed findings, and 65 reviewed papers. Evidence types span human clinical case series/systematic reviews, mouse models, and in vitro biochemistry, as annotated above.*


## Artifacts

- [OpenScientist final report](Porphyria-Related_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Porphyria-Related_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 32 |
| On topic | 13 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30987916` *(abstract only)*: "This deficiency leads to de-repression of the first and normally rate-controlling enzyme of the heme synthetic pathway, delta- or 5-aminolevulinic acid [ALA] synthase-1, and thus to marked up-regulation of this key enzyme and to marked hepatic overproduction of ALA"
  - closest text in source: "This deficiency leads to de-repression of the first and normally rate-controlling enzyme of the heme synthetic pathway, delta- or 5-aminolevulinic acid [ALA] synthase-1, and thus to marked up-regulation of this key enzyme and to marked hepatic overproduction of ALA"
- `PMID:11478735` *(abstract only)*: "ALA (0.1-10 mM) significantly inhibited the binding of [3H]muscimol (12 nM), with a similar potency in rat and human membranes (IC50 = 199 vs. 228 microM, respectively)"
  - closest text in source: "ALA (0.1-10 mM) significantly inhibited the binding of [3H]muscimol (12 nM), with a similar potency in rat and human membranes (IC50 = 199 vs. 228 microM, respectively)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31952692` (3 mentions) - Porphobilinogen synthase: An equilibrium of different assemblies in human health.
  - shared terms: variant, hepatic

Weighed against this report's own most characteristic terms: `attack`, `leukodystrophy`, `entity`, `biallelic`, `hmbs`, `pres`, `disease`, `aip`, `ala`, `reversible`, `acute`, `pbg`, `precursor`, `leukoencephalopathy`, `variant`, `hepatic`, `progressive`, `mendelian`, `gene`, `alas1`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002571` (1 mention) - the report calls it "Autonomic dysfunction (tachycardia, hypertension)"; HP calls it **Achalasia**
- `CHEBI:17549` (1 mention) - the report calls it "Metabolic changes:** Accumulation of ALA"; CHEBI calls it **5-aminolevulinic acid**
- `UBERON:0000955` (1 mention) - the report calls it "Organ level:** Primary — brain/CNS"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001298` (1 mention) - the report calls it "Encephalopathy/confusion"; HP calls it **Encephalopathy**
- `HP:0000618` (1 mention) - the report calls it "Visual disturbance/cortical blindness"; HP calls it **Blindness**, and lists "Legal blindness" among its other names
- `HP:0002027` (1 mention) - the report calls it "Abdominal pain (neurovisceral)"; HP calls it **Abdominal pain**
- `HP:0002902` (1 mention) - the report calls it "Hyponatremia (SIADH)"; HP calls it **Hyponatremia**
- `HP:0007141` (1 mention) - the report calls it "Peripheral motor neuropathy"; HP calls it **Sensorimotor neuropathy**
- `HP:0002061` (1 mention) - the report calls it "Spastic paraparesis"; HP calls it **Lower limb spasticity**, and lists "Spastic lower extremity" among its other names
- `HP:0001251` (1 mention) - the report calls it "Cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0100543` (1 mention) - the report calls it "Cognitive impairment (mild)"; HP calls it **Cognitive impairment**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:4982` - called "HMBS", "Causal gene:** **HMBS"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
