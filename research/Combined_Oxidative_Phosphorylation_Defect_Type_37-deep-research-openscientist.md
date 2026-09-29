---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T23:05:08.922628'
end_time: '2026-09-11T23:18:55.246418'
duration_seconds: 826.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 37
  mondo_id: MONDO:0032679
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 4
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002151
    reported_labels:
    - Increased serum lactate
    - lactate elevation
    ontology_label: Increased circulating lactate concentration
  - term_id: CHEBI:1993
    reported_labels:
    - 3-methylglutaconic acid
    ontology_label: CHEBI_1993
  - term_id: GO:0016021
    reported_labels:
    - integral component of membrane
    ontology_label: GO_0016021
  labels_variant: 5
  obsolete_terms:
  - term_id: CHEBI:1993
    ontology_label: CHEBI_1993
    replaced_by: CHEBI:28126
  - term_id: GO:0016021
    ontology_label: GO_0016021
    replaced_by: GO:0016020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Defect_Type_37-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Defect_Type_37-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 37
- **MONDO ID:** MONDO:0032679 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 37** covering all of the
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

# Combined Oxidative Phosphorylation Defect Type 37 (COXPD37): A Comprehensive Disease Characterization

**MONDO ID:** MONDO:0032679 | **OMIM:** #618329 | **Gene:** *MICOS13* (MIC13 / QIL1 / C19orf70) | **Inheritance:** Autosomal recessive | **Category:** Mendelian mitochondrial disorder

---

## Summary

**Combined Oxidative Phosphorylation Deficiency 37 (COXPD37)** is an ultra-rare, autosomal-recessive, early-onset mitochondrial disorder caused by **biallelic loss-of-function variants in *MICOS13*** (also known as *MIC13*, *QIL1*, or *C19orf70*). *MICOS13* encodes a small (~113-amino-acid) inner-mitochondrial-membrane protein that serves as the essential structural "bridge" between the two subcomplexes of the **Mitochondrial Contact site and Cristae Organizing System (MICOS)**. When MIC13 is absent, the MIC10–MIC26–MIC27 subcomplex fails to assemble, cristae junctions collapse, and the inner mitochondrial membrane loses its normal folded architecture. Because cristae junctions are the structural scaffold on which the oxidative phosphorylation (OXPHOS) machinery is organized, this architectural collapse produces a **combined respiratory-chain deficiency**, most prominently affecting Complex IV (cytochrome *c* oxidase).

Clinically, COXPD37 presents in infancy as a **severe, frequently fatal mitochondrial hepato-encephalopathy**. Affected children exhibit liver dysfunction (hepatopathy, cholestasis), profound neurodevelopmental impairment, cerebellar and vermian atrophy, and often optic atrophy, sensorineural hearing loss, and microcephaly. The two consistent biochemical hallmarks are **lactic acidosis** and **3-methylglutaconic aciduria (3-MGA)** — the latter being a diagnostic signature of disorders affecting mitochondrial membrane architecture. The disorder is caused by truncating variants (frameshift, splice-site) that remove the C-terminal functional motifs of MIC13, and it segregates in an autosomal-recessive manner, frequently in consanguineous families.

There is **no disease-specific or genotype-directed therapy**. Management is entirely supportive, typically comprising empirical mitochondrial "cofactor cocktails" (coenzyme Q10, carnitine, riboflavin, biotin, thiamine), metabolic stabilization, and organ-specific support, alongside genetic counseling for at-risk families. **Prognosis is poor**, with high early mortality reflecting the fatal infantile encephalo-hepatopathy phenotype. This report synthesizes eight confirmed findings drawn from the primary literature on MIC13 biology and MICOS13-associated disease.

---

## Key Findings

### Finding 1 — COXPD37 is caused by biallelic loss-of-function variants in *MICOS13*

COXPD37 is a monogenic Mendelian disorder resulting from **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *MICOS13***. Every reported family carries truncating variants — frameshift, nonsense, or splice-site — that introduce a premature termination codon and abolish functional MIC13 protein.

| Variant (protein) | Variant type | Family / study | PMID |
|---|---|---|---|
| QIL1 null alleles | Loss-of-function | Guarani et al., 2016 (2 siblings) | 27623147 |
| p.(Gly15Glufs*75) | Frameshift (homozygous) | Zeharia et al., 2016 (consanguineous) | 27485409 |
| Splice-site variant | Splicing loss-of-function | Gödiker et al., 2018 | 29618761 |
| c.209dupT (p.A73Rfs*32) | Frameshift (homozygous) | Ammar et al., 2026 (consanguineous) | 42033541 |

The causal role is well established. Guarani et al. reported that "*we identify QIL1 null alleles in two siblings displaying multiple clinical symptoms of early-onset fatal mitochondrial encephalopathy with liver disease*" ([PMID: 27623147](https://pubmed.ncbi.nlm.nih.gov/27623147/)). Zeharia et al. confirmed that "*the patients were found to be homozygous for the p.(Gly15Glufs*75) variant in the QIL1/MIC13 (C19orf70) gene*" ([PMID: 27485409](https://pubmed.ncbi.nlm.nih.gov/27485409/)). Most recently, Ammar et al. "*identified a homozygous pathogenic novel c.209dupT (p. A73Rfs*32) variant in the MICOS13 gene inherited from his heterozygous parents*" ([PMID: 42033541](https://pubmed.ncbi.nlm.nih.gov/42033541/)), confirming autosomal-recessive inheritance with unaffected heterozygous carriers.

**Ontology suggestions:** Gene — *MICOS13* (HGNC:28182); Disease — MONDO:0032679; Inheritance — HP:0000007 (Autosomal recessive inheritance).

### Finding 2 — Loss of MIC13 causes MICOS disassembly, loss of cristae junctions, and OXPHOS deficiency

MIC13 is the **structural linchpin of the MICOS complex**. MICOS is organized into two subcomplexes: the MIC60/MIC19/MIC25 subcomplex and the MIC10/MIC26/MIC27 subcomplex; MIC13 bridges the two. In CRISPR/Cas9 MIC13-knockout human cells, Anand et al. demonstrated that "*these knockout cells show a complete loss of crista junctions demonstrating that MIC13 is strictly required for the formation of crista junctions. MIC13 is required for the assembly of MIC10, MIC26, and MIC27 into the MICOS complex*" ([PMID: 27479602](https://pubmed.ncbi.nlm.nih.gov/27479602/)).

This cellular phenotype is faithfully recapitulated in patient tissue. Guarani et al. showed that "*QIL1 absence in patients' fibroblasts was associated with MICOS disassembly, abnormal cristae, mild cytochrome c oxidase defect*" ([PMID: 27623147](https://pubmed.ncbi.nlm.nih.gov/27623147/)). The selectivity of the defect is striking: Zeharia et al. found that "*in patient fibroblasts both MICOS subunits QIL1/MIC13 and MIC10 were absent whereas MIC60 was present in a comparable abundance to that of the control*" ([PMID: 27485409](https://pubmed.ncbi.nlm.nih.gov/27485409/)). Thus, loss of MIC13 selectively destroys the MIC10 subcomplex while sparing the MIC60 subcomplex, and the loss of cristae junctions translates into a measurable respiratory-chain (OXPHOS) deficiency in patient liver and muscle.

**Ontology suggestions:** GO:0042407 (cristae formation); GO:0061617 (MICOS complex assembly); GO:0006119 (oxidative phosphorylation).

### Finding 3 — Clinical phenotype: early-onset mitochondrial hepato-encephalopathy with 3-MGA and lactic acidosis

Across all reported families, COXPD37 presents as a **multisystem infantile mitochondrial disorder centered on the liver and central nervous system**. The core clinical picture combines encephalopathy/neurodegeneration, hepatopathy, and the biochemical signatures of lactic acidosis and 3-methylglutaconic aciduria.

Zeharia et al. described patients who "*presented with a neurodegenerative disorder accompanied by hyperlactatemia, 3-methylglutaconic aciduria, disturbed hepatocellular function with abnormal cristae morphology in liver and cerebellar and vermis atrophy*" ([PMID: 27485409](https://pubmed.ncbi.nlm.nih.gov/27485409/)). Gödiker et al. reported that the QIL1/MIC13 defect "*induces severe mitochondrial encephalopathy, hepatopathy and lactate acidosis consistent with psychomotor retardation. In addition, bilateral kidney stones were observed*" ([PMID: 29618761](https://pubmed.ncbi.nlm.nih.gov/29618761/)), extending the phenotype to include renal involvement. The most recent report broadened the spectrum further: Ammar et al. described a patient "*presenting with cholestatic hepatopathy, profound developmental delay, optic atrophy, sensorineural hearing loss, microcephaly, and cerebellar atrophy*" along with mtDNA depletion ([PMID: 42033541](https://pubmed.ncbi.nlm.nih.gov/42033541/)).

**Phenotype table with suggested HPO terms:**

| Phenotype | HPO term | Onset | Frequency (qualitative) |
|---|---|---|---|
| Hepatopathy / cholestasis | HP:0001392; HP:0001396 (Cholestasis) | Neonatal/infantile | Very frequent |
| Global developmental delay / psychomotor retardation | HP:0001263 | Infantile | Very frequent |
| Elevated lactate / lactic acidosis | HP:0002151 (Increased serum lactate) | Infantile | Very frequent |
| 3-Methylglutaconic aciduria | HP:0003535 | Infantile | Very frequent (hallmark) |
| Cerebellar / vermian atrophy | HP:0001272 (Cerebellar atrophy) | Infantile | Frequent |
| Optic atrophy | HP:0000648 | Infantile | Reported |
| Sensorineural hearing loss | HP:0000407 | Infantile | Reported |
| Microcephaly | HP:0000252 | Congenital/infantile | Reported |
| Nephrolithiasis (kidney stones) | HP:0000787 | Variable | Reported (single family) |
| mtDNA depletion | molecular | Infantile | Reported |

### Finding 4 — MICOS supports cardiolipin-dependent cristae curvature and modular assembly of Complex IV

The mechanistic link between architectural collapse and biochemical OXPHOS failure operates at two levels. **First**, the MIC10 subcomplex physically shapes the inner membrane by organizing cardiolipin. Simulation and biophysical work by Brown et al. showed that "*the MIC10 proteins Mic10, Mic26, and Mic27 strongly recruit cardiolipin at conserved positive loop motifs, driving oligomerization of these subunits and resulting in the stabilization of curvature in model membranes*" ([PMID: 42647630](https://pubmed.ncbi.nlm.nih.gov/42647630/)). Because MIC13 is required to build this exact subcomplex (Finding 2), its loss removes the machinery that generates cristae-junction curvature.

**Second**, MICOS directly facilitates assembly of the respiratory chain. Colina-Tenorio et al. demonstrated that "*MICOS facilitates specific assembly steps of CIV and associates with intermediates of the Cox1 and Cox3 modules*" ([PMID: 41420863](https://pubmed.ncbi.nlm.nih.gov/41420863/)). This explains why the cytochrome *c* oxidase (Complex IV) defect is the most consistently observed respiratory-chain abnormality in MIC13-deficient patients — Guarani et al. observed "*abnormal cristae, mild cytochrome c oxidase defect*" in patient fibroblasts ([PMID: 27623147](https://pubmed.ncbi.nlm.nih.gov/27623147/)). Thus MIC13 loss impairs OXPHOS by two convergent routes: (i) loss of cristae-junction curvature that concentrates respiratory complexes, and (ii) loss of a direct MICOS scaffolding function during Complex IV biogenesis.

**Ontology suggestions:** GO:0033617 (mitochondrial cytochrome c oxidase assembly); CHEBI:28494 (cardiolipin); GO:0097250 (mitochondrial respiratory chain complex IV assembly).

### Finding 5 — 3-Methylglutaconic aciduria is a "secondary" mitochondrial-membrane-type marker and key diagnostic biomarker

3-Methylglutaconic aciduria (3-MGA) is one of the most useful diagnostic clues in COXPD37. It belongs to the class of "secondary" 3-MGA associated with **disrupted mitochondrial membrane architecture**, rather than a primary defect in leucine catabolism. Wortmann et al., in a landmark analysis of 50 genes and 977 patients, established that 3-MGA "*was more frequently seen in ATPase related disorders, with mitochondrial DNA depletion or deletion, but not in patients with single respiratory chain complex deficiencies*" ([PMID: 23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/)). This pattern places MICOS13 disease firmly in the "membrane-associated" 3-MGA category alongside TAZ (Barth syndrome), SERAC1 (MEGDEL), OPA3 (Costeff), DNAJC19 (DCMA), and TMEM70 disorders.

The diagnostic value is emphasized by the nomenclature review of Wortmann et al., which noted that "*there is, however, a group of disorders with significantly and consistently increased 3-methylglutaconic acid excretion, where the 3-methylglutaconic aciduria is a hallmark of the phenotype and the key to diagnosis*" ([PMID: 23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/)). In practice, the finding of 3-MGA on urine organic acid analysis in an infant with hepato-encephalopathy and lactic acidosis should prompt consideration of MICOS/inner-membrane disorders including COXPD37.

**Ontology suggestions:** HP:0003535 (3-Methylglutaconic aciduria); CHEBI:1993 (3-methylglutaconic acid).

### Finding 6 — MIC13 protein domain organization, functional motifs, and cellular disease models

MIC13 (UniProt Q5XKP0; ~113 amino acids) is an inner-membrane protein whose function depends on two conserved motifs: an **N-terminal GxxxG motif** within its transmembrane segment and an **internal WN (RDSWN) motif**. Urbach et al. demonstrated that "*a GxxxG motif in the N-terminal transmembrane segment and an internal WN motif are essential for stability of MIC13, formation of the MIC10-subcomplex, interaction with MIC10- and MIC60-subcomplexes and maintenance of cristae morphology. The GxxxG motif is required for membrane insertion of MIC13*" ([PMID: 34271005](https://pubmed.ncbi.nlm.nih.gov/34271005/)). This structural insight directly rationalizes pathogenesis: the reported disease-causing truncating variants (e.g., p.Gly15Glufs*75, p.A73Rfs*32) remove or disrupt these C-terminal functional motifs, abolishing MIC13's bridging function.

The primary experimental disease model is the **CRISPR/Cas9 MIC13-knockout human cell line**. Anand et al. reported that "*using the CRISPR/Cas method we generated the first cell line deleted for MIC13. These knockout cells show a complete loss of crista junctions*" ([PMID: 27479602](https://pubmed.ncbi.nlm.nih.gov/27479602/)), providing a tractable, faithful cellular model of the human architectural defect.

**Ontology suggestions:** Protein — UniProt Q5XKP0; GO:0016021 (integral component of membrane); GO:0005743 (mitochondrial inner membrane).

### Finding 7 — No disease-specific therapy; supportive management with empirical cofactors; poor prognosis

There is **no approved, genotype-directed therapy** for MICOS13 deficiency. Management follows the general paradigm for primary mitochondrial disease: empirical vitamin/cofactor supplementation plus organ-specific supportive care. In a cohort of genetically confirmed primary mitochondrial disease (n=62), Akyüzlüer Güneş et al. found that "*Coenzyme Q10 (62.9%), carnitine (53.2%), riboflavin (48.4%), biotin (37.1%) and thiamine (35.5%) were the most frequently prescribed agents*" ([PMID: 42697122](https://pubmed.ncbi.nlm.nih.gov/42697122/)), with ~71% of patients receiving at least one cofactor supplement and only ~21% having established targeted therapies — underscoring the largely empirical nature of treatment.

Prognosis is **poor**. Guarani et al. characterized the disorder as "*early-onset fatal mitochondrial encephalopathy with liver disease*" ([PMID: 27623147](https://pubmed.ncbi.nlm.nih.gov/27623147/)), and the broader literature describes lethal infantile hepato-encephalopathy, indicating high early mortality. Some patients with milder or later-recognized presentations survive longer, reflecting variable expressivity.

**Ontology suggestions:** NCIT — Coenzyme Q10 (C1099), Levocarnitine (C61815), Riboflavin (C716), Biotin (C287), Thiamine (C1109); Supportive care (NCIT:C133387).

### Finding 8 — Ultra-rare autosomal-recessive disorder with complete penetrance, variable expressivity, and consanguinity association

COXPD37 is **ultra-rare**, with only a small number of families reported worldwide since its first description in 2016. All show autosomal-recessive segregation of biallelic *MICOS13* truncating variants, and several arise in **consanguineous families**. Zeharia et al. described "*a brother and sister from a consanguineous family*" ([PMID: 27485409](https://pubmed.ncbi.nlm.nih.gov/27485409/)), and Ammar et al. documented "*a homozygous pathogenic novel c.209dupT (p. A73Rfs*32) variant in the MICOS13 gene inherited from his heterozygous parents*" ([PMID: 42033541](https://pubmed.ncbi.nlm.nih.gov/42033541/)) — confirming recessive inheritance with unaffected heterozygous carriers.

Because the gene is autosomal, both sexes are affected equally. Penetrance in biallelic-variant individuals appears complete, while expressivity is variable (from lethal infantile disease to somewhat longer-surviving milder cases). No formal prevalence, incidence, founder-mutation, or carrier-frequency estimates currently exist for this disorder.

**Ontology suggestions:** HP:0000007 (Autosomal recessive inheritance); consanguinity — HP:0032316.

---

## Mechanistic Model / Interpretation

The pathophysiology of COXPD37 flows in an ordered causal chain from a single genetic lesion to a fatal multisystem phenotype:

```
1. Biallelic truncating MICOS13 variant (e.g., p.Gly15Glufs*75, p.A73Rfs*32)
        │  removes GxxxG / WN functional motifs
        ▼  results in
2. Absence / instability of MIC13 protein
        │  (loss of the "bridge" between MICOS subcomplexes)
        ▼  leads to
3. Failure to assemble the MIC10–MIC26–MIC27 subcomplex
        │  (MIC60 subcomplex preserved — selective defect)
        ▼  leads to
4. Loss of cardiolipin-organized membrane curvature at cristae junctions
        │
        ▼  results in
5. Complete loss of cristae junctions → abnormal inner-membrane architecture
        │
        ├──────────────────────────────┐
        ▼ (branch A)                    ▼ (branch B)
6a. Loss of MICOS scaffolding of    6b. Disorganized cristae fail to
    Complex IV (Cox1/Cox3 module        concentrate/stabilize OXPHOS
    assembly)                            complexes; mtDNA depletion in
        │                                some cases
        ▼                                    │
7. Combined OXPHOS deficiency (prominent Complex IV / COX defect)
        │
        ▼  results in
8. Impaired ATP production + secondary metabolic derangement
        │  (lactic acidosis; 3-methylglutaconic aciduria)
        ▼  leads to
9. Energy failure in high-demand tissues (liver, brain, cochlea, retina, kidney)
        │
        ▼  manifests as
10. Infantile hepato-encephalopathy: hepatopathy/cholestasis, developmental
    delay, cerebellar/vermian atrophy, optic atrophy, hearing loss, microcephaly
        │
        ▼  frequently
11. Early death (fatal infantile course)
```

**Upstream vs downstream:** Steps 1–3 (genetic and MICOS-assembly defects) are the *upstream, demonstrated* causal core, established both in patient fibroblasts and in CRISPR knockout cells. Steps 4–6 integrate biophysical and biochemical evidence from MIC10-complex and MICOS-CIV assembly studies. Steps 8–11 (the clinical phenotype) are consistently observed across all reported families, though the precise tissue-selectivity of energy failure (why liver and cerebellum are especially vulnerable) is *inferred* from the general biology of mitochondrial disease rather than mechanistically proven for MIC13 specifically.

**Cell types and compartments involved:** The defect is intrinsic to the **mitochondrial inner membrane** (GO:0005743) and its **cristae** (crista junction, GO:0030061). High-energy-demand cell types are most affected: hepatocytes (CL:0000182), neurons/cerebellar Purkinje cells (CL:0000121), retinal ganglion cells (CL:0000740; optic atrophy), and cochlear hair cells (sensorineural hearing loss). Affected organs (UBERON): liver (UBERON:0002107), cerebellum (UBERON:0002037), brain (UBERON:0000955), optic nerve (UBERON:0000941), inner ear (UBERON:0001846), kidney (UBERON:0002113).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports finding(s) |
|---|---|---|---|
| [27623147](https://pubmed.ncbi.nlm.nih.gov/27623147/) | *QIL1 mutation causes MICOS disassembly and early onset fatal mitochondrial encephalopathy with liver disease* | Human clinical + cell | F001, F002, F003, F004, F007 |
| [27485409](https://pubmed.ncbi.nlm.nih.gov/27485409/) | *Mitochondrial hepato-encephalopathy due to deficiency of QIL1/MIC13 (C19orf70)* | Human clinical + cell | F001, F002, F003, F008 |
| [29618761](https://pubmed.ncbi.nlm.nih.gov/29618761/) | *QIL1-dependent assembly of MICOS complex — lethal mutation in C19ORF70* | Human clinical | F001, F003 |
| [42033541](https://pubmed.ncbi.nlm.nih.gov/42033541/) | *Novel homozygous MICOS13 frameshift → hepatoencephalopathy & mtDNA depletion* | Human clinical + computational | F001, F003, F008 |
| [27479602](https://pubmed.ncbi.nlm.nih.gov/27479602/) | *Mic13 Is Essential for Formation of Crista Junctions in Mammalian Cells* | In vitro (CRISPR KO) | F002, F006 |
| [34271005](https://pubmed.ncbi.nlm.nih.gov/34271005/) | *Conserved GxxxG and WN motifs of MIC13 are essential for bridging two MICOS subcomplexes* | In vitro / structure-function | F006 |
| [42647630](https://pubmed.ncbi.nlm.nih.gov/42647630/) | *The molecular basis of mitochondrial crista formation by the MIC10 complex* | Computational / biophysical | F004 |
| [41420863](https://pubmed.ncbi.nlm.nih.gov/41420863/) | *MICOS promotes modular assembly of cytochrome c oxidase* | In vitro / biochemical | F004 |
| [23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/) | *3-Methylglutaconic aciduria — lessons from 50 genes and 977 patients* | Human cohort | F005 |
| [23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/) | *Inborn errors of metabolism with 3-MGA as discriminative feature* | Review / nomenclature | F005 |
| [42697122](https://pubmed.ncbi.nlm.nih.gov/42697122/) | *Prescribing patterns of vitamin/cofactor therapies in primary mitochondrial disease* | Human cohort (n=62) | F007 |
| [42178653](https://pubmed.ncbi.nlm.nih.gov/42178653/) | *MICOS and MIMAS — multifunctional assemblies linking mitochondrial biogenesis, architecture, and function* | Review | F002, F004 (background) |

**How the evidence coheres:** The genetic causality (F001) is triangulated across four independent families spanning 2016–2026, all with truncating *MICOS13* variants. The cellular mechanism (F002, F006) is anchored by CRISPR knockout experiments that directly demonstrate crista-junction loss and MIC10-subcomplex assembly failure, and this is mirrored in patient fibroblasts. The biochemical bridge to OXPHOS failure (F004) is supported by recent biophysical (cardiolipin/curvature) and biochemical (MICOS–Complex IV assembly) studies. The 3-MGA biomarker (F005) is contextualized by large cohort data placing it in the "membrane-architecture" 3-MGA class. Together these constitute a mechanistically complete, internally consistent model.

**Note on cross-domain references:** Two papers reviewed during the investigation (*TACO1 in hypertensive heart failure*, PMID 42147162; and a heart-specific conditional deletion study, PMID 41892295) concern Complex IV/MICOS biology in cardiac remodeling and are not COXPD37-specific; they provide supporting background on MICOS–Complex IV interdependence but were not used as primary evidence for disease claims.

---

## Section-by-Section Consolidated Data

### 1. Disease Information
COXPD37 is one of a numbered series of "Combined Oxidative Phosphorylation Deficiency" disorders (OMIM #618329). **Synonyms/alternative names:** MIC13 deficiency; QIL1 deficiency; MICOS13 deficiency; C19orf70-related mitochondrial hepato-encephalopathy. Identifiers: MONDO:0032679, OMIM #618329, gene *MICOS13* (HGNC:28182). Information is derived from **aggregated disease-level resources and individual case reports/series** (not large EHR datasets), reflecting its ultra-rarity.

### 2. Etiology
**Primary cause:** genetic — biallelic loss-of-function variants in *MICOS13*. **Genetic risk factor:** consanguinity (increases homozygosity risk). No environmental, infectious, lifestyle, or occupational causal factors are known or implicated. No protective factors, modifier genes, or gene–environment interactions have been characterized. This is a fully penetrant Mendelian disorder, not a multifactorial one.

### 3. Phenotypes
See Finding 3 table. The phenotype spectrum is dominated by hepatopathy/cholestasis and neurodegeneration (developmental delay, cerebellar/vermian atrophy) with the biochemical hallmarks of lactic acidosis and 3-MGA. Additional reported features: optic atrophy, sensorineural hearing loss, microcephaly, nephrolithiasis, and mtDNA depletion. Onset is neonatal/infantile; severity ranges from lethal to severe; course is progressive. Quality of life is profoundly impaired given the severe multisystem, often fatal, infantile presentation.

### 4. Genetic / Molecular Information
**Causal gene:** *MICOS13* (chromosome 19). **Variant classes reported:** frameshift (p.Gly15Glufs*75; p.A73Rfs*32), splice-site, and null alleles — all **loss-of-function**. **Functional consequence:** loss of function (protein absence/instability). **Somatic vs germline:** germline. Population allele frequencies are extremely low (variants are private/family-specific); no recurrent founder allele is established. No epigenetic mechanisms or gross chromosomal abnormalities are implicated. Secondary **mtDNA depletion** has been reported in at least one case (Ammar 2026).

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known. Disease is entirely genetically determined.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and Mechanistic Model above. Key molecular elements: MICOS complex assembly (MIC10 subcomplex), cardiolipin-dependent inner-membrane curvature, cristae-junction formation, and MICOS-assisted Complex IV assembly. Cellular processes: disrupted OXPHOS/energy metabolism, secondary metabolic derangement (lactic acidosis, 3-MGA). No autoimmune/inflammatory or infectious component.

### 7. Anatomical Structures Affected
**Primary organs:** liver (UBERON:0002107) and brain (UBERON:0000955), especially cerebellum/vermis (UBERON:0002037). **Secondary/associated:** optic nerve (UBERON:0000941), inner ear/cochlea (UBERON:0001846), kidney (UBERON:0002113; nephrolithiasis in one family). **Body systems:** hepatic, central and peripheral nervous, sensory (visual, auditory), renal. **Subcellular:** mitochondrial inner membrane and cristae (GO:0005743). **Lateralization:** bilateral/symmetric (e.g., bilateral optic atrophy, bilateral kidney stones).

### 8. Temporal Development
**Onset:** neonatal to infantile (congenital/early pediatric). **Onset pattern:** subacute to progressive. **Course:** progressive neurodegeneration with hepatic dysfunction; frequently fatal in infancy/early childhood. **Duration:** typically short due to high early mortality; milder survivors have chronic lifelong disease. Critical intervention window (if therapy existed) would be neonatal/early infancy.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (HP:0000007). **Penetrance:** complete in biallelic carriers. **Expressivity:** variable. **Sex ratio:** 1:1 (autosomal). **Consanguinity:** associated. **Prevalence/incidence:** unknown — ultra-rare; only a handful of families reported worldwide. No established founder effect, genetic anticipation, or carrier-frequency estimate.

### 10. Diagnostics
**Biochemical screening:** urine organic acids showing **3-methylglutaconic aciduria** (HP:0003535) and blood/CSF **lactate elevation** (HP:0002151) are the key first-line clues. **Enzymology:** respiratory-chain assays in muscle/liver show combined OXPHOS deficiency with prominent Complex IV (COX) reduction. **Histology/EM:** liver and muscle show abnormal cristae morphology. **Imaging:** brain MRI shows cerebellar/vermian atrophy. **Definitive diagnosis:** molecular genetic testing — whole-exome/whole-genome sequencing or mitochondrial-disease gene panels including *MICOS13*; single-gene testing confirms familial variants; mtDNA testing may show secondary depletion. **Differential diagnosis:** other MICOS/inner-membrane and membrane-associated 3-MGA disorders — TAZ (Barth), SERAC1 (MEGDEL), OPA3 (Costeff), DNAJC19 (DCMA), TMEM70, and other combined-OXPHOS-deficiency subtypes.

### 11. Outcome / Prognosis
**Prognosis is poor**, with frequent early death from fatal infantile mitochondrial encephalopathy with liver disease. Survivors experience severe neurodevelopmental disability, sensory impairment (vision, hearing), and chronic hepatic and metabolic compromise. No validated prognostic biomarkers exist, though severity broadly tracks with residual mitochondrial function and hepatic involvement.

### 12. Treatment
**No disease-specific therapy.** Supportive management includes empirical mitochondrial cofactor supplementation (coenzyme Q10, L-carnitine, riboflavin, biotin, thiamine), management of lactic acidosis, nutritional/hepatic support, treatment of complications (e.g., seizures, kidney stones), and sensory support. No gene, cell, RNA-based, or targeted therapies are approved or in trials specific to COXPD37. NCIT terms: Coenzyme Q10 (C1099), Levocarnitine (C61815), Riboflavin (C716), Biotin (C287), Thiamine (C1109).

### 13. Prevention
**Primary prevention** is genetic: carrier identification, genetic counseling for consanguineous or affected families, and reproductive options including prenatal diagnosis and preimplantation genetic testing once the familial variant is known. **Cascade testing** of at-risk relatives is appropriate. No behavioral, immunization, or public-health prevention applies.

### 14. Other Species / Natural Disease
MICOS is deeply evolutionarily conserved from yeast to humans, so cross-species cellular models inform the mechanism. *MICOS13* orthologs exist across vertebrates and invertebrates. Naturally occurring MICOS13 disease in other species (OMIA) is not established, and no zoonotic or cross-species transmission applies (this is a genetic disorder).

### 15. Model Organisms
The principal validated model is the **CRISPR/Cas9 MIC13-knockout human cell line** (Anand 2016, [PMID: 27479602](https://pubmed.ncbi.nlm.nih.gov/27479602/)), which fully recapitulates crista-junction loss and MIC10-subcomplex assembly failure. **Patient-derived fibroblasts** serve as a primary human in-vitro model, faithfully reproducing MICOS disassembly and the COX defect. Yeast MICOS systems inform conserved mechanism. No dedicated mouse/zebrafish MIC13-disease model is prominent in the reviewed literature — a recognized gap.

---

## Limitations and Knowledge Gaps

1. **Very small patient base.** Fewer than a dozen families have been reported, precluding formal epidemiology (prevalence, incidence, carrier frequency) and robust genotype–phenotype correlation. Reported allelic spectrum is limited to truncating variants; the pathogenicity spectrum of missense/hypomorphic variants is essentially unknown.
2. **Tissue-selectivity unexplained.** Why the liver and cerebellum are disproportionately affected, while MICOS is ubiquitous, is inferred from general mitochondrial-disease biology rather than demonstrated for MIC13.
3. **Complex IV emphasis vs "combined" defect.** The literature consistently notes a Complex IV/COX defect ("mild" in some fibroblast assays), but the full quantitative profile of the *combined* OXPHOS deficiency across complexes and tissues is incompletely characterized.
4. **mtDNA depletion mechanism.** Secondary mtDNA depletion was reported recently (Ammar 2026); whether this is a consistent feature and how MIC13 loss causes it mechanistically is unresolved.
5. **No animal model reviewed.** Absence of an in-vivo (mouse/zebrafish) COXPD37 model in the reviewed literature limits study of organ-level pathogenesis and preclinical therapeutics.
6. **No therapeutic evidence.** Cofactor use is extrapolated from general mitochondrial-disease cohorts, not from COXPD37-specific trials; efficacy in this disorder is unproven.
7. **Biomarker specificity.** 3-MGA and lactate are sensitive clues but non-specific across membrane-architecture mitochondrial disorders, so molecular confirmation is essential.

---

## Proposed Follow-up Experiments / Actions

1. **Build a patient registry / natural-history study** to aggregate all reported and unreported MICOS13 cases, enabling genotype–phenotype correlation, survival estimates, and biomarker validation.
2. **Generate an in-vivo model** — conditional (liver- and neuron-specific) *Micos13* knockout mouse or zebrafish — to dissect tissue-selectivity, mtDNA depletion, and to serve as a preclinical therapeutic platform.
3. **Quantitative multi-complex OXPHOS profiling** across patient tissues (liver, muscle, brain where available) and iPSC-derived hepatocytes/neurons to define the full "combined" deficiency signature and confirm the Complex IV emphasis.
4. **Structure-guided variant interpretation.** Use the defined GxxxG/WN motif map (Urbach 2021) plus AlphaFold modeling to build an ACMG-aligned functional-classification framework for future missense/VUS *MICOS13* variants; complement with a cell-based rescue assay (crista-junction restoration in MIC13-KO cells).
5. **Cardiolipin and membrane-lipidomics analysis** in patient/knockout cells to test whether MIC13 loss perturbs cardiolipin organization as predicted by the MIC10-complex biophysics (PMID 42647630).
6. **Investigate the mtDNA-depletion axis** — measure mtDNA copy number and nucleoid distribution in additional cases to determine whether depletion is a recurrent, mechanistically informative feature.
7. **Preclinical therapeutic screening** — test whether cofactor cocktails, cardiolipin-targeting agents (e.g., elamipretide-class peptides), or gene-replacement approaches restore cristae architecture and OXPHOS in MIC13-KO models, given the small protein size favorable for AAV gene therapy.
8. **Refine diagnostic pathways** — advocate for early WES/WGS in infants presenting with the 3-MGA + lactic acidosis + hepato-encephalopathy triad to shorten diagnostic odyssey and enable cascade testing.

---

*Report compiled from an autonomous multi-iteration investigation (8 confirmed findings, 14 papers reviewed). Evidence types span human clinical case series, in-vitro CRISPR knockout and structure-function studies, biophysical/computational simulations, and large biochemical cohorts. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_37-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_37-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002151` (2 mentions) - the report calls it "Increased serum lactate", "lactate elevation"; HP calls it **Increased circulating lactate concentration**
- `CHEBI:1993` (1 mention) - the report calls it "3-methylglutaconic acid"; CHEBI calls it **CHEBI_1993**
- `GO:0016021` (1 mention) - the report calls it "integral component of membrane"; GO calls it **GO_0016021**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CHEBI:1993` (CHEBI_1993) (1 mention) - replaced by `CHEBI:28126`
- `GO:0016021` (GO_0016021) (1 mention) - replaced by `GO:0016020`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0061617` (1 mention) - the report calls it "MICOS complex assembly"; GO calls it **MICOS complex**
- `HP:0001263` (1 mention) - the report calls it "Global developmental delay / psychomotor retardation"; HP calls it **Global developmental delay**
- `HP:0000787` (1 mention) - the report calls it "Nephrolithiasis (kidney stones)"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names
- `GO:0033617` (1 mention) - the report calls it "mitochondrial cytochrome c oxidase assembly"; GO calls it **mitochondrial respiratory chain complex IV assembly**, and lists "mitochondrial cytochrome c oxidase assembly" among its other names
- `GO:0097250` (1 mention) - the report calls it "mitochondrial respiratory chain complex IV assembly"; GO calls it **mitochondrial respirasome assembly**, and lists "mitochondrial respiratory chain supercomplex assembly" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002151` - called "Increased serum lactate", "lactate elevation"
- `HP:0003535` - called "3-Methylglutaconic aciduria", "3-methylglutaconic aciduria"