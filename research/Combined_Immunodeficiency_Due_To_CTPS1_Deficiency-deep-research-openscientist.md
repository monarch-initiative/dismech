---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T08:11:09.479858'
end_time: '2026-09-06T08:25:55.964191'
duration_seconds: 886.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due to CTPS1 Deficiency
  mondo_id: MONDO:0014391
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
citation_count: 15
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 14
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 11
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0014391
    reported_labels:
    - MONDO
    ontology_label: combined immunodeficiency due to CTPS1 deficiency
  - term_id: HP:0002850
    reported_labels:
    - Laboratory
    ontology_label: Decreased circulating IgM concentration
  - term_id: HP:0003261
    reported_labels:
    - Clinical
    ontology_label: Increased circulating IgA concentration
  - term_id: HP:0002841
    reported_labels:
    - Infectious sign
    ontology_label: Recurrent fungal infections
  - term_id: CL:0000625
    reported_labels:
    - "CD8\u207A T"
    ontology_label: CD8-positive, alpha-beta T cell
  - term_id: CL:0000624
    reported_labels:
    - "CD4\u207A T"
    ontology_label: CD4-positive, alpha-beta T cell
  - term_id: CL:0000921
    reported_labels:
    - iNKT
    ontology_label: type I NK T cell
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_CTPS1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_CTPS1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due to CTPS1 Deficiency
- **MONDO ID:** MONDO:0014391 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due to CTPS1 Deficiency** covering all of the
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

# Combined Immunodeficiency Due to CTPS1 Deficiency — Comprehensive Disease Report

**Disease:** Combined Immunodeficiency Due to CTPS1 Deficiency
**MONDO:** MONDO:0014391 · **OMIM:** #615897 (Immunodeficiency 24) · **Orphanet:** ORPHA:319391 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *CTPS1* (HGNC:2519; NCBI Gene 1503; UniProt P17812), chromosome 1p34.2

---

## Summary

Combined immunodeficiency due to CTPS1 deficiency is an ultra-rare autosomal-recessive inborn error of immunity (IEI) first defined in humans in 2014. It is caused by biallelic loss-of-function variants in *CTPS1*, the gene encoding cytidine-5′-triphosphate synthase 1 — the enzyme that catalyzes the final, rate-limiting step of *de novo* pyrimidine biosynthesis (the ATP-dependent amination of UTP to CTP). Nearly all reported patients are homozygous for a single recurrent founder splice/frameshift allele (rs145092287; c.1692-1G>C, p.Thr566AspfsTer26), which behaves as a **hypomorph** that reduces CTPS1 protein and enzymatic activity by 80–90% owing to protein instability rather than loss of intrinsic catalytic function ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/); [PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).

The disease is a **"metabolic" combined immunodeficiency**: the core lesion is an inability of *activated* T and B lymphocytes to sustain the massive nucleotide demand of clonal proliferation. Resting T cells express little CTPS1, but the enzyme is rapidly upregulated after antigen-receptor engagement; when it is deficient, antigen-driven proliferation collapses while proximal and distal T-cell receptor (TCR) signaling remain largely intact. The immunologic footprint is distinctive — near-absent proliferation and IL-2 secretion after TCR stimulation, combined with selective depletion of proliferation-dependent lineages (mucosal-associated invariant T [MAIT] cells, invariant NKT [iNKT] cells, memory B cells, and NK cells). Clinically, patients present in early childhood with severe, chronic, recurrent herpesvirus infections — especially Epstein–Barr virus (EBV) — recurrent encapsulated-bacterial infections, occasional invasive fungal disease, and a strong predisposition to EBV-driven B-cell lymphoproliferation and lymphoma ([PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/); [PMID: 35983265](https://pubmed.ncbi.nlm.nih.gov/35983265/)).

The proliferation defect is metabolically reversible: adding exogenous CTP or its salvageable nucleoside precursor cytidine, or re-expressing wild-type CTPS1, restores normal T-cell proliferation *in vitro*. Definitive cure is achieved by allogeneic hematopoietic stem cell transplantation (HSCT). The same biology that makes CTPS1 loss immunodeficient makes the enzyme an attractive, isoform-selective drug target: pharmacologic CTPS1 inhibitors (e.g., STP938) are in clinical trials for relapsed/refractory lymphomas, and genetic or chemical CTPS1 inactivation rescues fatal autoimmunity in mouse models — the therapeutic mirror image of the human disease ([PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/); [PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/); [PMID: 34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/)).

---

## Key Findings

### Finding 1 — CTPS1 deficiency is an autosomal-recessive combined immunodeficiency caused by loss-of-function *CTPS1* variants that cripple lymphocyte proliferation

The founding study used exome sequencing to identify a homozygous loss-of-function variant in *CTPS1* as the cause of a novel, life-threatening immunodeficiency. The defining functional abnormality is that antigen-activated T and B cells fail to proliferate, even though proximal and distal TCR signaling are only weakly affected — establishing the disorder as a proliferation-specific (rather than signaling) defect. The causal gene is *CTPS1* (HGNC:2519) on chromosome 1p34.2, and the disease is catalogued as OMIM #615897. As stated in the landmark paper, *"we report the identification of a loss-of-function homozygous mutation (rs145092287) in CTPS1 in humans that causes a novel and life-threatening immunodeficiency, characterized by an impaired capacity of activated T and B cells to proliferate in response to antigen receptor-mediated activation"* ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).

### Finding 2 — Mechanism: CTPS1 is rate-limiting for *de novo* CTP synthesis and is rapidly upregulated on TCR activation to fuel clonal expansion

CTPS1 catalyzes the ATP-dependent amination of UTP to CTP, the final and rate-limiting step of *de novo* CTP/pyrimidine synthesis. Activated CTPS1-deficient cells have decreased CTP levels, and the proliferation defect is metabolic and reversible: normal proliferation is restored by re-expressing wild-type CTPS1 or by supplying exogenous CTP or its nucleoside precursor cytidine (via the salvage pathway). Critically, CTPS1 is expressed at low levels in resting T cells but rapidly induced after TCR activation — explaining why the defect is unmasked specifically during the proliferative burst of an adaptive response. The paper reports: *"Activated CTPS1-deficient cells had decreased levels of CTP. Normal T-cell proliferation was restored in CTPS1-deficient cells by expressing wild-type CTPS1 or by addition of exogenous CTP or its nucleoside precursor, cytidine. CTPS1 expression was found to be low in resting T cells, but rapidly upregulated following TCR activation"* ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).

### Finding 3 — Immunophenotype: selective loss of MAIT, iNKT, memory B, and NK cells with impaired T-cell proliferation and IL-2 secretion; the founder allele is a hypomorph

Immunophenotyping of a cohort of 7 patients (all homozygous for c.1692-1G>C, p.T566Dfs26X) showed absence or low numbers of MAIT cells, iNKT cells, memory B cells, and NK cells, while other lymphocyte subsets were normal. Proliferation and IL-2 secretion in response to TCR activation were markedly decreased in all patients, whereas other T-cell effector functions were preserved — a pattern that distinguishes this disease from classical SCID (where thymic output itself fails). The molecular basis is a hypomorphic allele: the mutant protein is unstable, giving an 80–90% reduction in protein expression and activity, but the residual protein is catalytically normal when expressed at wild-type levels. Two verbatim statements anchor this: *"Immune phenotyping performed in 7 patients showed absence or low numbers of mucosal-associated T cells, invariant NKT cells, memory B cells, and NK cells, whereas other subsets were normal. Proliferation and IL-2 secretion by T cells in response to TCR activation were markedly decreased in all patients, while other T cell effector functions were preserved"*; and *"The CTPS1T566Dfs26X mutant protein was found to be hypomorphic, resulting in 80%-90% reduction of protein expression and CTPS activity in cells of patients"* ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).

### Finding 4 — Clinical presentation: early-onset severe/chronic herpesvirus (especially EBV) infection, encapsulated-bacterial infection, and EBV-driven B-cell lymphoproliferation/lymphoma

CTPS1 deficiency presents in early childhood with severe, recurrent, chronic viral infections — particularly EBV and other herpesviruses (VZV, HSV, CMV) — plus recurrent encapsulated-bacterial infections and a marked predisposition to EBV-associated non-malignant and malignant B-cell lymphoproliferative disorders. CTPS1 is repeatedly listed among the IEIs in which defective antigen-driven T-cell expansion impairs elimination of proliferating EBV-infected B cells. A review of EBV-susceptibility genetics places it precisely: *"the defective expansion of EBV-specific CD8 T cells results from mutations in genes involved in T-cell activation (such as RASGRP1, MAGT1, and ITK), DNA metabolism (CTPS1) or co-stimulatory pathways (CD70, CD27, and TNFSFR9)"* ([PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/)). The infectious spectrum also extends to invasive fungal disease: the first reported case presenting *"with coccidioidomycosis"* documents *"the first case of cytidine nucleotide triphosphate synthetase 1 (CTPS1) deficiency, a combined immunodeficiency impairing lymphocyte proliferation, presenting with coccidioidomycosis"* ([PMID: 35983265](https://pubmed.ncbi.nlm.nih.gov/35983265/)).

### Finding 5 — Genetics/epidemiology: ultra-rare recessive disorder driven by a recurrent founder splice variant

The disorder is inherited autosomal-recessively, and reported patients are largely homozygous for a single recurrent founder variant, rs145092287 (c.1692-1G>C, p.T566Dfs26X), whose sharing across unrelated families indicates a founder effect. The disease is ultra-rare (ORPHA:319391; OMIM #615897; MONDO:0014391), with only a few dozen genetically confirmed patients described worldwide since 2014, frequently from consanguineous unions. Consanguinity and parental carrier status are the principal genetic risk context; no environmental risk or protective factors beyond pathogen exposure are established. The founder allele is documented in the discovery paper — *"we report the identification of a loss-of-function homozygous mutation (rs145092287) in CTPS1 in humans"* ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)) — and its precise nomenclature is confirmed in the cohort study as *"a unique homozygous frameshift splice mutation (c.1692-1G>C, p.T566Dfs26X)"* ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).

### Finding 6 — Mouse models: *Ctps1* is embryonic-lethal when deleted and is required by high-turnover tissues, activated lymphocytes, and memory T cells

Conditional/inducible mouse studies show that deletion of *Ctps1* (but not its paralog *Ctps2*) is embryonic-lethal, and that high-proliferation/renewal tissues — intestinal epithelium, erythroid and thymic lineages, activated B and T lymphocytes, and memory T cells — strongly depend on CTPS1. Both CTPS1 and CTPS2 are required for TCR-driven T-cell proliferation. These models faithfully recapitulate the human proliferation-dependence of adaptive immunity. As reported: *"deletion of Ctps1, but not Ctps2, is embryonic-lethal. Tissue and cells with high proliferation and renewal rates, such as intestinal epithelium, erythroid and thymic lineages, activated B and T lymphocytes, and memory T cells strongly rely on CTPS1 for their maintenance and growth. However, both CTPS1 and CTPS2 are required for T cell proliferation following TCR stimulation"* ([PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)).

### Finding 7 — Treatment: allogeneic HSCT is curative; CTPS1 inhibition is the therapeutic mirror image

Allogeneic HSCT has been used successfully as definitive, curative treatment by replacing the CTPS1-deficient hematopoietic compartment ([PMID: 29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/)). Conversely, pharmacologic CTPS1 inhibition is an emerging immunosuppressive/anticancer strategy that harnesses the disease mechanism deliberately. In mice, *"Deletion of Ctps1 in T cells or treatment with a CTPS1 inhibitor rescued Foxp3-deficient mice from fatal systemic autoimmunity and reduced the severity of experimental autoimmune encephalomyelitis. These findings support that CTPS1 may represent a target for immune suppression"* ([PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)). A clinical-stage selective inhibitor is documented: *"de novo CTP synthesis pathway enzyme CTPS1 whose inhibitor (STP938) is already in clinical trials for relapsed/refractory lymphomas (NCT05463263)"* ([PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/)).

### Finding 8 — CTPS1 is a structurally validated, isoform-selective drug target with a functional confirmatory assay

Cryo-EM structural studies establish the structural basis for isoform-specific (CTPS1 vs CTPS2) small-molecule inhibition ([PMID: 34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/)), and CTPS activity in patient lymphocytes can be quantified by LC-MS/MS measurement of CTP, providing a functional confirmatory diagnostic assay ([PMID: 31524312](https://pubmed.ncbi.nlm.nih.gov/31524312/)). Together with the clinical-stage inhibitor STP938 ([PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/)) and mouse rescue-of-autoimmunity data ([PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)), these establish CTPS1 as a validated, druggable, isoform-selective target — the reverse-translation counterpart of the deficiency.

---

## Detailed Report by Template Section

### 1. Disease Information

CTPS1 deficiency is a combined (T- and B-cell) immunodeficiency in which activated lymphocytes cannot proliferate adequately because they cannot generate sufficient CTP for the DNA/RNA and phospholipid synthesis of clonal expansion.

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014391 |
| OMIM | #615897 (Immunodeficiency 24; IMD24) |
| Orphanet | ORPHA:319391 |
| ICD-10 / ICD-11 | D81.8 (other combined immunodeficiencies) / 4A00.1Y |
| MeSH | closest: "Immunologic Deficiency Syndromes"/"Severe Combined Immunodeficiency" (no dedicated term) |
| Gene | *CTPS1*, HGNC:2519; NCBI Gene 1503; Ensembl ENSG00000171793; UniProt P17812; 1p34.2 |

**Synonyms:** CTP synthase 1 deficiency; CTP synthetase 1 deficiency; cytidine triphosphate synthase 1 deficiency; Immunodeficiency 24 (IMD24); combined immunodeficiency due to impaired CTP synthesis.

**Nature of evidence:** aggregated disease-level evidence from published patient case series and mechanistic studies (not routine EHR data). Pivotal cohorts are small individual-patient series (~8 patients in [PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/); 7 immunophenotyped patients in [PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).

### 2. Etiology

- **Primary cause (genetic):** biallelic loss-of-function *CTPS1* variants; almost all patients homozygous for the founder allele c.1692-1G>C (p.T566Dfs26X).
- **Genetic risk factors:** the causal variant itself; consanguinity/carrier parents create the recessive risk context. No GWAS/susceptibility loci (monogenic).
- **Modifier gene (candidate):** *CTPS2* (paralog); residual CTPS2 activity plausibly contributes to survival and to the hypomorphic phenotype (inferred from mouse redundancy; [PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)).
- **Environmental risk factors:** none causal. Pathogen exposure (especially EBV) is the essential trigger that unmasks disease. Sex is not a risk factor (autosomal).
- **Protective factors:** intact salvage pathway (cytidine→CTP) and CTPS2 are compensatory (inferred; salvage rescues the cellular defect in vitro, [PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).
- **Gene–environment interaction:** the CTPS1 lesion is clinically silent until a proliferation-demanding challenge occurs; EBV is paradigmatic because it drives B-cell proliferation and requires vigorous CD8⁺ T-cell expansion to control ([PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/)).

### 3. Phenotypes

Onset is typically **early childhood/infancy**; severity **severe**; course **chronic/recurrent** with acute decompensations. Frequencies are qualitative given small cohorts.

| Phenotype | Type | Suggested HPO | Onset | Frequency |
|---|---|---|---|---|
| Recurrent/chronic viral infection (esp. EBV; also VZV, HSV, CMV) | Infectious sign | HP:0004429; HP:0006515 | Infancy–early childhood | Very frequent |
| Recurrent encapsulated-bacterial infection | Infectious sign | HP:0002718; HP:0002783 | Early childhood | Frequent |
| EBV-driven B-cell lymphoproliferation / lymphoma | Neoplasm | HP:0005523; HP:0002665 | Childhood | Frequent predisposition |
| Impaired T-cell proliferation & ↓IL-2 on TCR stimulation | Laboratory | HP:0002850 | Congenital (functional) | Obligate |
| Low/absent MAIT, iNKT, memory B, NK cells | Laboratory | HP:0011840; HP:0040218 | Congenital | Characteristic |
| Hemophagocytic lymphohistiocytosis (HLH) | Clinical | HP:0003261 | Childhood | Occasional |
| Invasive fungal infection (e.g., coccidioidomycosis) | Infectious sign | HP:0002841 | Childhood | Rare/atypical |
| Failure to thrive / recurrent fever | Symptom/sign | HP:0001508; HP:0011947 | Infancy | Frequent |

Distinctively, **naïve T-cell output/thymic function and proximal TCR signaling are largely preserved**, separating this disease from classical SCID ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/); [PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)). **Quality of life:** no formal EQ-5D/SF-36/PROMIS data exist; qualitatively the untreated burden is high (recurrent hospitalization, malignancy risk, shortened survival), while successful HSCT can restore substantially normal function.

### 4. Genetic / Molecular Information

- **Causal gene:** *CTPS1* (EC 6.3.4.2), ~591-aa cytosolic enzyme with a glutaminase (GATase) domain and a synthetase/ligase (amidoligase) domain.
- **Principal variant:** NM_001905.4:c.1692-1G>C, p.(Thr566AspfsTer26), rs145092287. **Type:** splice-acceptor → frameshift → premature stop. **Classification:** Pathogenic. **Consequence:** loss of function via protein instability (80–90% ↓ protein/activity), residual protein catalytically normal ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).
- **Allele frequency:** very rare in gnomAD/dbSNP; no healthy homozygotes.
- **Origin:** germline, autosomal recessive (not somatic).
- **Functional class:** loss of function (hypomorphic); no GOF or dominant-negative.
- **Modifier genes:** *CTPS2* (partial redundancy). **Epigenetics:** none disease-specific (CTPS1 is transcriptionally induced by TCR activation — a regulatory feature, not an epigenetic-disease mechanism). **Chromosomal abnormalities:** none.

### 5. Environmental Information

No causal toxic/lifestyle factors. Infectious agents central to clinical expression: **EBV/HHV-4** (dominant), other herpesviruses (VZV, HSV, CMV, HHV-6), encapsulated bacteria, and fungi (*Coccidioides*; [PMID: 35983265](https://pubmed.ncbi.nlm.nih.gov/35983265/)). These are triggers/opportunists, not the disease cause.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic *CTPS1* LOF variant (c.1692-1G>C, p.T566Dfs26X) **leads to** a frameshifted, unstable protein.
2. Protein instability **results in** 80–90% reduced CTPS1 protein/activity (residual protein catalytically normal) ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).
3. Reduced activity **impairs** the rate-limiting *de novo* step UTP→CTP, **causing** decreased CTP when demand is high ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).
4. Antigen-receptor activation normally **triggers** rapid CTPS1 upregulation; in deficiency this surge fails, so **CTP becomes limiting** for DNA/RNA/phospholipid synthesis during clonal expansion ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).
5. CTP limitation **blocks** proliferation of activated T and B cells and reduces IL-2, while proximal/distal signaling and non-proliferative effector functions are preserved *(branch: signaling intact, proliferation lost)* ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)).
6. The proliferation block **preferentially depletes** proliferation-dependent lineages — MAIT, iNKT, memory B, NK cells ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)) *(inferred link)*.
7. Impaired clonal expansion **results in** failure to expand EBV-specific CD8⁺ T cells, **leading to** uncontrolled herpesvirus infection and failure to eliminate EBV-infected proliferating B cells → EBV-driven B-cell lymphoproliferation/lymphoma ([PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/)).
8. **Reversal branch:** exogenous CTP/cytidine (salvage) or wild-type CTPS1 rescues proliferation *in vitro*, and HSCT cures *in vivo*; pharmacologic CTPS1 inhibition reproduces the block therapeutically ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/); [PMID: 29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/); [PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)).

**Detail by category:** Pathway — *de novo* pyrimidine/CTP biosynthesis (KEGG map00240; Reactome nucleotide metabolism), downstream of TCR→PI3K/AKT/mTOR and MYC-driven metabolic reprogramming (MYC positively regulates CTPS1; [PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/)). Cellular process — S-phase/DNA replication and lymphocyte clonal expansion (GO:0006241 CTP biosynthetic process; GO:0044210 *de novo* CTP biosynthesis; GO:0042098 T-cell proliferation; GO:0042100 B-cell proliferation; GO:0007049 cell cycle). Protein dysfunction — LOF via instability; CTPS tetramerizes/polymerizes into filaments ("cytoophidia"), and an isoform-specific inhibitor pocket has been resolved by cryo-EM ([PMID: 34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/)). Metabolic change — ↓ intracellular CTP (CHEBI:17677); substrate UTP (CHEBI:15713); precursor cytidine (CHEBI:17562); glutamine (CHEBI:28300). Biochemical assay — reduced CTPS activity by LC-MS/MS CTP quantification ([PMID: 31524312](https://pubmed.ncbi.nlm.nih.gov/31524312/)). **Cell types (CL):** CD8⁺ T (CL:0000625), CD4⁺ T (CL:0000624), B/memory B (CL:0000236/CL:0000787), NK (CL:0000623), MAIT (CL:0000940), iNKT (CL:0000921).

### 7. Anatomical Structures Affected

- **Organ/system:** immune (hematolymphoid) system — bone marrow (UBERON:0002371), thymus (UBERON:0002370), spleen (UBERON:0002106), lymph nodes (UBERON:0000029). Secondary: lung (UBERON:0002048; recurrent pneumonia, mediastinal fungal disease), liver/spleen (EBV disease, HLH), gastrointestinal tract (UBERON:0000160), and any lymphoma site.
- **Tissue/cell:** lymphoid tissue and circulating activated/proliferating lymphocytes; mouse data implicate high-renewal intestinal epithelium and erythroid/thymic lineages ([PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)).
- **Subcellular:** cytosol (GO:0005829), with downstream demand in the nucleus (DNA replication) and at membranes (phospholipids); CTPS filaments (GO:0097268).
- **Lateralization:** systemic/generalized (not lateralized).

### 8. Temporal Development

Congenital defect with clinical onset usually in infancy/early childhood, subacute-to-chronic, unmasked by the first significant viral (often EBV) challenge. Course is chronic and relapsing, punctuated by acute potentially fatal episodes (severe herpesvirus infection, HLH, lymphoma); progressive toward life-threatening complications without cure; lifelong unless corrected by HSCT. No formal staging; no spontaneous remission of the underlying defect, but treatment-induced immune reconstitution follows successful HSCT. **Critical window:** early diagnosis and HSCT before refractory infection/malignancy; uncontrolled pre-transplant infection worsens outcome ([PMID: 33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/)).

### 9. Inheritance and Population

Autosomal recessive (OMIM #615897). Ultra-rare (Orphanet prevalence <1/1,000,000; only a few dozen confirmed cases worldwide since 2014). Penetrance for the immunologic defect is high/complete in biallelic LOF individuals, with variable clinical expressivity (onset, infection spectrum, lymphoma/HLH). Founder effect for c.1692-1G>C (rs145092287) across unrelated families ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/); [PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)); consanguinity frequently contributory. Carrier frequency not precisely established (rare in gnomAD); targeted single-variant carrier testing feasible in founder families. Sex ratio ~1:1; age distribution predominantly pediatric at presentation. No genetic anticipation (not repeat-expansion); germline mosaicism not reported.

### 10. Diagnostics

- **Immunology/labs:** immunophenotyping shows low/absent MAIT, iNKT, memory B, NK cells with otherwise near-normal subsets; lymphocyte proliferation assays show markedly reduced proliferation and IL-2 on TCR/anti-CD3 stimulation with preserved proximal signaling ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/)); CTPS activity assay (LC-MS/MS CTP quantification) is a functional confirmatory biomarker ([PMID: 31524312](https://pubmed.ncbi.nlm.nih.gov/31524312/)); EBV viral load typically high/persistent.
- **Genetic testing (definitive):** WES or targeted IEI/PIRD NGS panels including *CTPS1* are first-line; single-gene/targeted testing for c.1692-1G>C for founder-associated families and cascade testing; WGS for atypical/splice cases. CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are not applicable. *CTPS1* is included on international IEI/PIRD panels ([PMID: 38644452](https://pubmed.ncbi.nlm.nih.gov/38644452/)).
- **Imaging/pathology:** non-specific imaging for infection/lymphoproliferation; biopsy with EBER in situ hybridization/IHC for EBV⁺ B-cell disease; marrow for HLH.
- **Differential diagnosis:** other EBV-susceptibility/CID IEIs — CD27, CD70, RASGRP1, MAGT1 (XMEN), ITK, SH2D1A (XLP1), XIAP, PIK3CD/PIK3R1, CORO1A, STK4, and SCID ([PMID: 26424649](https://pubmed.ncbi.nlm.nih.gov/26424649/); [PMID: 31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/); [PMID: 36209991](https://pubmed.ncbi.nlm.nih.gov/36209991/)).
- **Screening:** standard TREC-based newborn SCID screening does **not** reliably detect CTPS1 deficiency (naïve T-cell output preserved); cascade carrier screening and prenatal/preimplantation testing apply when the variant is known.

### 11. Outcome / Prognosis

Without curative treatment, prognosis is poor with high risk of death from overwhelming viral infection, HLH, or lymphoma in childhood/adolescence; uncontrolled pre-transplant infection is associated with mortality (5 of 9 IEI children in a pre-HSCT VST series, including CTPS1 patients, died before transplant; [PMID: 33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/)). **Allogeneic HSCT is curative** and can restore normal immune function ([PMID: 29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/)). Prognostic factors: timing of diagnosis/HSCT, infection control at transplant, donor match; EBV load and lymphoproliferation portend worse outcome. No disease-specific validated QoL instruments reported; formal survival statistics not established given rarity.

### 12. Treatment

| Modality | Detail | NCIT |
|---|---|---|
| **Allogeneic HSCT (curative)** | Replaces the CTPS1-deficient hematopoietic compartment; best before refractory infection/malignancy ([PMID: 29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/)) | C15431 (HSCT); C107137 (allogeneic HSCT) |
| **Supportive pharmacotherapy** | Antiviral/antibacterial/antifungal prophylaxis & treatment; immunoglobulin replacement | C578 (IVIG) |
| **EBV-LPD/lymphoma management** | Rituximab for EBV⁺ B-cell lymphoproliferation; chemotherapy for lymphoma | C1702 (rituximab) |
| **Adoptive cellular therapy** | EBV/virus-specific T cells (VST) as pre-HSCT bridge — limited efficacy once infection prolonged ([PMID: 33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/)) | — |
| **Metabolic-rationale (experimental)** | Cytidine/CTP supplementation rescues proliferation in vitro (proof of concept, not standard) ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)) | — |
| **Reverse-translation** | Selective CTPS1 inhibitors (STP938; NCT05463263) treat lymphoma/autoimmunity — not a treatment for the deficiency ([PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/); [PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)) | — |

**Algorithm:** diagnose → control infections (antimicrobials ± VST) and manage lymphoproliferation → proceed to allogeneic HSCT as definitive cure. Pharmacogenomics: not applicable.

### 13. Prevention

- **Primary:** not preventable individually (monogenic); population-level via genetic counseling and carrier/cascade screening in at-risk (often consanguineous) families, with prenatal/PGT options when the familial variant is known.
- **Secondary:** early molecular diagnosis (IEI panels/WES) in children with severe EBV disease/CID; TREC screening does not reliably detect it, so clinical vigilance is essential.
- **Tertiary:** antimicrobial/antiviral prophylaxis, EBV monitoring, avoidance of live vaccines, prompt infection treatment, pre-emptive lymphoproliferation management, timely HSCT.
- **Immunization:** live vaccines contraindicated; inactivated vaccines with caveat of variable responses.
- **Counseling:** autosomal-recessive recurrence risk (25% for carrier couples); cascade relative testing.

### 14. Other Species / Natural Disease

*CTPS1* is evolutionarily conserved. Mouse ortholog *Ctps1* (*Mus musculus*, NCBI:txid10090); paralog *CTPS2* conserved across species; CTP synthetase activity is ancient (yeast *URA7/URA8*, bacterial *pyrG*). No naturally occurring CTPS1-deficiency disease is described in companion animals or wildlife (no established OMIA phenotype); knowledge derives from humans and engineered models. Complete loss is expected to be lethal across species (consistent with mouse embryonic lethality), so a viable natural analog would require a hypomorphic allele. Not zoonotic (non-infectious genetic disorder).

### 15. Model Organisms

- **Mouse (principal model; [PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/)):** conditional/inducible *Ctps1* (and *Ctps2*) knockouts and lineage-specific (e.g., T-cell) deletions plus pharmacologic-inhibition models. *Ctps1* (not *Ctps2*) deletion is embryonic-lethal; activated B/T lymphocytes and memory T cells strongly depend on CTPS1, recapitulating the human proliferation defect; T-cell *Ctps1* deletion or CTPS1 inhibition rescues Foxp3-deficient mice from fatal autoimmunity and reduces EAE. **Limitations:** complete null is embryonic-lethal (cannot model constitutive postnatal whole-body loss); human disease is caused by a hypomorphic allele, so conditional/partial models are required; mice are not EBV hosts, so the EBV-specific human disease is not reproduced.
- **Cellular/in vitro:** patient primary lymphocytes; CRISPR *CTPS1* knockout in T-cell leukemia/lymphoma lines abolishes proliferation and causes DNA damage ([PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/); [PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/)); reconstitution and cytidine/CTP-rescue assays; recombinant enzyme for cryo-EM/inhibitor design ([PMID: 34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/)); engineered *Ctps1/Ctps2*-knockout CHO auxotroph lines as bioproduction tools ([PMID: 35249214](https://pubmed.ncbi.nlm.nih.gov/35249214/)).
- **Resources:** MGI (*Ctps1*), IMPC/IMSR for engineered alleles.

---

## Mechanistic Model / Interpretation

```
 CTPS1 LoF variant (c.1692-1G>C, p.T566Dfs26X)
            │  (protein instability)
            ▼
 80–90% ↓ CTPS1 protein & activity  ─────────►  residual protein catalytically NORMAL
            │                                     (defect = amount, not intrinsic function)
            ▼
 ↓ de novo CTP synthesis (UTP ─X─► CTP), rate-limiting
            │
   [TCR/BCR activation demands rapid CTPS1 upregulation — cannot occur]
            ▼
 CTP becomes LIMITING during clonal expansion
            │
     ┌──────┴───────────────────────────────┐
     ▼                                        ▼
 Proliferation & IL-2 BLOCKED        Proximal/distal signaling &
 in activated T & B cells            non-proliferative effectors PRESERVED
     │
     ├──► Selective depletion: MAIT, iNKT, memory B, NK cells
     │
     └──► Failure to expand EBV-specific CD8+ T cells
                 │
                 ▼
      Uncontrolled EBV/herpesviruses ──► EBV-driven B-cell
      + recurrent bacterial/fungal        lymphoproliferation / lymphoma
      infection
                 │
         [Metabolic bypass: exogenous cytidine/CTP or WT CTPS1
          RESCUES proliferation in vitro → HSCT cures in vivo;
          CTPS1 inhibitors reproduce the block therapeutically]
```

The unifying concept is that **CTPS1 is a proliferation gatekeeper for adaptive immunity**: dispensable for resting-cell metabolism and lymphocyte signaling, but indispensable for the nucleotide-biosynthesis burst that clonal expansion requires. This explains the paradoxical phenotype — near-normal lymphocyte numbers and signaling, but functional collapse of antigen-driven immunity, with the sharpest clinical consequence against EBV, the pathogen whose control most depends on massive CD8⁺ T-cell expansion.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/) | *CTP synthase 1 deficiency reveals central role in lymphocyte proliferation* | Human + in vitro | **Foundational:** causal gene/variant, proliferation defect, CTP↓, cytidine/CTP rescue, TCR-induced upregulation |
| [32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/) | *Impaired lymphocyte function… hypomorphic homozygous mutation* | Human cohort (n=7) + in vitro | Immunophenotype (MAIT/iNKT/memory B/NK loss); hypomorph 80–90% ↓; founder allele nomenclature |
| [38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/) | *Inactivation of CTPS1 prevents fatal autoimmunity in mice* | Mouse | Embryonic lethality; high-turnover tissue dependence; CTPS1/CTPS2 roles; inhibitor rescues autoimmunity |
| [31402499](https://pubmed.ncbi.nlm.nih.gov/31402499/) | *Signaling pathways in T-cell immunity against EBV* | Review | Places CTPS1 among EBV-susceptibility IEIs via defective T-cell expansion |
| [35983265](https://pubmed.ncbi.nlm.nih.gov/35983265/) | *Seronegative mediastinal coccidioidomycosis in CTPS1 CID* | Case report | Expands infectious spectrum to invasive fungal disease |
| [37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/) | *MYC-induced cytidine metabolism… cGAS-STING in MCL* | In vitro/translational | Clinical-stage selective inhibitor STP938 (NCT05463263); MYC→CTPS1 |
| [34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/) | *Structural basis for isoform-specific inhibition of CTPS1* | Structural (cryo-EM) | Validates CTPS1 as druggable, isoform-selective target |
| [31524312](https://pubmed.ncbi.nlm.nih.gov/31524312/) | *CTPS activity assay by LC-MS/MS* | Methods | Functional confirmatory assay measuring CTP |
| [29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/) | *HSCT for CTPS1 deficiency* | Clinical | Definitive curative therapy |
| [33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/) | *Failure of VST pre-HSCT in IEIs* | Clinical series | Bridging VST has limited efficacy once infection prolonged |
| [29176466](https://pubmed.ncbi.nlm.nih.gov/29176466/) | *NGS in a boy with EBV lymphoma — CTPS2 VUS* | Case report | Raises CTPS2 as candidate phenocopy |
| [39380841](https://pubmed.ncbi.nlm.nih.gov/39380841/) | *CTPS1 + ATR inhibition in p53-deficient myeloma* | In vitro | Reinforces CTPS1 metabolic-vulnerability biology |
| [25956014](https://pubmed.ncbi.nlm.nih.gov/25956014/) | *Advances in immunology 2014* | Review | Contextualizes CTPS1 among new IEI genes |
| [38644452](https://pubmed.ncbi.nlm.nih.gov/38644452/) | *PIRD mutation spectrum in Turkey* | Cohort/panel | *CTPS1* on international IEI/PIRD panels |
| [26424649](https://pubmed.ncbi.nlm.nih.gov/26424649/), [29942301](https://pubmed.ncbi.nlm.nih.gov/29942301/), [36209991](https://pubmed.ncbi.nlm.nih.gov/36209991/) | *PIDs associated with EBV disease* (reviews) | Review | CTPS1 among EBV-LPD-predisposing IEIs |

All papers are mutually consistent; none challenges the core model. The clearest independent replications are the founder-allele identity and hypomorphic mechanism across [PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/) and [PMID: 32161190](https://pubmed.ncbi.nlm.nih.gov/32161190/), and the mouse-model corroboration of proliferation-dependence in [PMID: 38438357](https://pubmed.ncbi.nlm.nih.gov/38438357/).

---

## Supported vs Refuted Hypotheses

**Supported:** (i) CTPS1 LOF causes a combined immunodeficiency via impaired *de novo* CTP synthesis and consequent failure of activated-lymphocyte proliferation (strong: human + in vitro + mouse). (ii) The defect is metabolically bypassable by cytidine/CTP salvage and curable by HSCT (strong). (iii) A single founder splice allele underlies most cases (strong). (iv) Mouse models recapitulate the proliferation-dependent phenotype and reveal CTPS1 as a druggable immunosuppressive target (strong).

**Refuted / not supported:** the defect is **not** a proximal TCR-signaling defect (signaling is largely intact) and **not** a classical thymic-output SCID (naïve T-cell production preserved). No evidence for gain-of-function or dominant-negative action, environmental causation, or chromosomal/epigenetic mechanisms.

---

## Limitations and Knowledge Gaps

1. **Small cohorts / limited allelic diversity.** Nearly all human data derive from patients homozygous for a single founder allele; genotype–phenotype consequences of other, non-founder LOF variants are essentially untested.
2. **Epidemiology.** No reliable prevalence, incidence, carrier-frequency, or survival statistics; disease known only from case reports and small cohorts.
3. **Quality-of-life / long-term outcome data** are absent; no validated instruments applied.
4. **CTPS2 as modifier/phenocopy** remains unresolved (the reported CTPS2 VUS is unproven; [PMID: 29176466](https://pubmed.ncbi.nlm.nih.gov/29176466/)).
5. **Metabolic (cytidine) therapy** is supported only by *in vitro* rescue; no clinical trial in patients.
6. **Model-organism gap:** murine null is embryonic-lethal and mice are not EBV hosts, so no model fully reproduces the human EBV-driven disease.
7. **Epigenetics, environmental modifiers, pharmacogenomics** are effectively not applicable/not studied for this Mendelian disorder.
8. **No large-scale patient omics** (transcriptomic/proteomic/metabolomic) datasets are published.

---

## Proposed Follow-up Experiments / Actions

1. **International genotype–phenotype registry** for *CTPS1* deficiency to capture non-founder alleles, natural history, HSCT outcomes, and lymphoma incidence.
2. **Functionally characterize additional *CTPS1* variants** (stability, catalytic activity, CTP rescue) using the LC-MS/MS CTP assay ([PMID: 31524312](https://pubmed.ncbi.nlm.nih.gov/31524312/)) and cryo-EM-informed structure–function analysis ([PMID: 34583994](https://pubmed.ncbi.nlm.nih.gov/34583994/)).
3. **Test cytidine/uridine-nucleoside supplementation** as adjunctive/bridging therapy in patient cells and, if promising, compassionate-use, building on *in vitro* rescue ([PMID: 24870241](https://pubmed.ncbi.nlm.nih.gov/24870241/)).
4. **Optimize HSCT timing/conditioning** and define pre-transplant EBV/lymphoma control (including improved VST protocols delivered before prolonged infection) ([PMID: 29884857](https://pubmed.ncbi.nlm.nih.gov/29884857/); [PMID: 33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/)).
5. **Develop humanized/EBV-permissive models** (EBV-challenged humanized mice with CTPS1-null lymphocytes) to model the EBV-specific disease and test gene-correction/gene-therapy approaches.
6. **Resolve CTPS2 candidacy** through segregation, functional assays, and cohort screening ([PMID: 29176466](https://pubmed.ncbi.nlm.nih.gov/29176466/)).
7. **Leverage the reverse-translation link:** use CTPS1-inhibitor programs (STP938; [PMID: 37226519](https://pubmed.ncbi.nlm.nih.gov/37226519/)) to refine understanding of on-target immunosuppression, informing drug-safety (drug-induced phenocopy of the deficiency) and precision-immunosuppression opportunities.

---

## Ontology Term Quick-Reference

- **Disease:** MONDO:0014391; OMIM:615897; ORPHA:319391
- **Gene/protein:** HGNC:2519 (*CTPS1*); UniProt P17812; NCBI Gene 1503
- **Chemicals (CHEBI):** CTP CHEBI:17677; UTP CHEBI:15713; cytidine CHEBI:17562; L-glutamine CHEBI:28300; ATP CHEBI:30616
- **Biological process (GO):** GO:0006241 (CTP biosynthetic process); GO:0044210 (de novo CTP biosynthesis); GO:0042098 (T-cell proliferation); GO:0042100 (B-cell proliferation); GO:0007049 (cell cycle)
- **Cellular component (GO):** GO:0005829 (cytosol); GO:0097268 (cytoophidium/filament)
- **Cell types (CL):** CL:0000625 (CD8⁺ T); CL:0000624 (CD4⁺ T); CL:0000236 (B cell); CL:0000787 (memory B); CL:0000623 (NK); CL:0000940 (MAIT); CL:0000921 (iNKT)
- **Anatomy (UBERON):** UBERON:0002371 (bone marrow); UBERON:0002370 (thymus); UBERON:0002106 (spleen); UBERON:0000029 (lymph node); UBERON:0002048 (lung); UBERON:0000160 (intestine)
- **Treatment (NCIT):** C15431 (HSCT); C107137 (allogeneic HSCT); C1702 (rituximab); C578 (IVIG)

---

*Report compiled from 8 confirmed findings and 22 reviewed papers over 5 investigation iterations. Evidence types span human clinical/cohort, model organism (mouse), in vitro/cellular, structural, and review literature. Key PMIDs cited inline.*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_CTPS1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_CTPS1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 24 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014391` (4 mentions) - the report calls it "MONDO"; MONDO calls it **combined immunodeficiency due to CTPS1 deficiency**
- `HP:0002850` (1 mention) - the report calls it "Laboratory"; HP calls it **Decreased circulating IgM concentration**
- `HP:0003261` (1 mention) - the report calls it "Clinical"; HP calls it **Increased circulating IgA concentration**
- `HP:0002841` (1 mention) - the report calls it "Infectious sign"; HP calls it **Recurrent fungal infections**
- `CL:0000625` (2 mentions) - the report calls it "CD8⁺ T"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000624` (2 mentions) - the report calls it "CD4⁺ T"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000921` (2 mentions) - the report calls it "iNKT"; CL calls it **type I NK T cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0044210` (2 mentions) - the report calls it "de novo CTP biosynthesis"; GO calls it **'de novo' CTP biosynthetic process**
- `CL:0000787` (2 mentions) - the report calls it "memory B"; CL calls it **memory B cell**
- `CL:0000623` (2 mentions) - the report calls it "NK"; CL calls it **natural killer cell**, and lists "NK cell" among its other names
- `CL:0000940` (2 mentions) - the report calls it "MAIT"; CL calls it **mucosal-associated invariant T cell**, and lists "MAIT" among its other names
- `GO:0005829` (2 mentions) - the report calls it "Subcellular:** cytosol", "cytosol"; GO calls it **cytosol**
- `GO:0097268` (2 mentions) - the report calls it "cytoophidium/filament"; GO calls it **cytoophidium**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005829` - called "Subcellular:** cytosol", "cytosol"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.