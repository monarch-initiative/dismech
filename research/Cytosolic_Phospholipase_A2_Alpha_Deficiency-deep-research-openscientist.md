---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T02:48:14.507107'
end_time: '2026-10-15T03:10:07.829185'
duration_seconds: 1313.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cytosolic Phospholipase A2 Alpha Deficiency
  mondo_id: MONDO:0018794
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 12
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0018794
    reported_labels:
    - MONDO
    ontology_label: cytosolic phospholipase-A2 alpha deficiency associated bleeding
      disorder
  - term_id: HP:0005263
    reported_labels:
    - gastrointestinal ulceration
    ontology_label: Gastritis
  - term_id: HP:0005208
    reported_labels:
    - enteric fistula
    ontology_label: Secretory diarrhea
  - term_id: HP:0001891
    reported_labels:
    - Frequent
    ontology_label: Iron deficiency anemia
  - term_id: HP:0002027
    reported_labels:
    - Frequent
    ontology_label: Abdominal pain
  - term_id: CL:0000066
    reported_labels:
    - epithelial cell; intestinal/uterine luminal epithelium
    - luminal epithelium
    - Tissue/cell level:** intestinal **luminal epithelium
    ontology_label: epithelial cell
  - term_id: NCIT:C62042
    reported_labels:
    - Misoprostol
    ontology_label: Leuprolide
  - term_id: NCIT:C29059
    reported_labels:
    - Iron
    ontology_label: Fluoxamine
  labels_variant: 7
  obsolete_terms:
  - term_id: NCIT:C29059
    ontology_label: Fluoxamine
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cytosolic_Phospholipase_A2_Alpha_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cytosolic_Phospholipase_A2_Alpha_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cytosolic Phospholipase A2 Alpha Deficiency
- **MONDO ID:** MONDO:0018794 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cytosolic Phospholipase A2 Alpha Deficiency** covering all of the
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

# Cytosolic Phospholipase A2 Alpha (cPLA2α) Deficiency — Comprehensive Disease Report

**Disease:** Cytosolic Phospholipase A2 Alpha Deficiency
**MONDO ID:** MONDO:0018794
**Gene:** *PLA2G4A* (cytosolic phospholipase A2 group IVA; HGNC:9035)
**Category:** Mendelian (ultra-rare autosomal recessive inborn error of eicosanoid biosynthesis)

---

## Summary

Cytosolic phospholipase A2 alpha (cPLA2α) deficiency is an **ultra-rare autosomal-recessive inborn error of lipid-mediator metabolism** caused by biallelic loss-of-function variants in *PLA2G4A*. cPLA2α is the rate-limiting enzyme that selectively liberates **arachidonic acid (AA)** from the *sn*-2 position of membrane glycerophospholipids; the released AA is the obligate substrate for cyclooxygenases (COX-1/COX-2) and lipoxygenases (5-LOX, 12-LOX) that make **prostaglandins, thromboxanes, prostacyclin, and leukotrienes**. When both alleles of *PLA2G4A* are inactivated, the cell can no longer provide AA on demand, and the entire downstream eicosanoid cascade is starved of substrate. The clinical consequence is a distinctive **two-part phenotype**: (1) a prostaglandin-deficiency "NSAID-like" **ulcerating, stenosing, and fistulating small-intestinal enteropathy** with iron-deficiency anemia, recurrent GI bleeding, and protein-losing enteropathy; and (2) a thromboxane-dependent **platelet-function bleeding diathesis**.

The disease has been described in only a handful of unrelated families worldwide (fewer than ~5 published probands as of this review), making it one of the rarest known Mendelian eicosanoid disorders. The molecular diagnosis is anchored by a biochemical signature — **markedly reduced platelet thromboxane B2 (TxB2) and 12-HETE, reduced calcium-ionophore–induced leukotriene B4, and depressed urinary prostanoid metabolites** — followed by confirmatory *PLA2G4A* sequencing. The defect is upstream of COX: platelet aggregation to ADP and collagen is blunted but is **restored by exogenous arachidonic acid**, localizing the lesion to AA release rather than to the COX/synthase machinery itself.

There is **no approved disease-specific therapy**. Management is supportive and mechanism-based: strict NSAID avoidance, **prostaglandin replacement (misoprostol, a PGE1 analog)**, mucosal protection, iron and nutritional support, and bleeding management. Importantly, the inherited human deficiency essentially recapitulates the **predicted on-target toxicity** of pharmacologic cPLA2α inhibition — a drug class long pursued for asthma, rheumatoid arthritis, inflammatory bowel disease, and psoriasis — and the mouse and human data together serve as a cautionary natural experiment about the consequences of complete cPLA2α blockade.

---

## 1. Disease Information

**Overview.** cPLA2α deficiency is a monogenic disorder of eicosanoid biosynthesis. Loss of the group IVA cytosolic phospholipase A2 abolishes the regulated, stimulus-coupled release of arachidonic acid, producing a systemic shortage of prostaglandins, thromboxanes, prostacyclin, and leukotrienes. The two cardinal clinical domains are chronic small-bowel ulceration/stenosis and a platelet-type bleeding tendency.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018794 |
| Gene | *PLA2G4A*, HGNC:9035, NCBI Gene 5321, UniProt P47712 |
| Chromosomal locus | 1q31.1 |
| Protein | 85-kDa cytosolic phospholipase A2, group IVA (cPLA2α) |

**Synonyms / alternative names.** cPLA2-alpha deficiency; cytosolic phospholipase A2 group IVA deficiency; PLA2G4A deficiency; "enteropathy of prostaglandin deficiency"; inherited human cPLA2α deficiency. Clinically overlapping descriptive term: a "prostaglandin-related enteropathy."

**Information source.** Evidence is derived almost entirely from **individual-patient reports and small kindreds** (human clinical case studies) complemented by **mouse knockout models** and **in vitro enzymology**, rather than from aggregated EHR or population-disease registries. This reflects the extreme rarity of the condition.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *PLA2G4A***. No environmental or infectious cause is implicated as the primary driver.

**Genetic risk / causal variants.**
- Compound heterozygous **p.Ser111Pro + [p.Arg485His; p.Lys651Arg]** (Adler et al., 2008; [PMID: 18451993](https://pubmed.ncbi.nlm.nih.gov/18451993/)).
- Homozygous **c.1723G>C, p.Asp575His** (Faioni et al., 2014; [PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/)).
- p.Lys651Arg is a common polymorphism, essentially neutral for catalysis (functional data below).

**Modifier genes.** Co-inherited **mild factor XI deficiency** was observed in one family (proband, sister, mother) and is a plausible modifier of the bleeding phenotype (Faioni et al., 2014; [PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/)).

**Environmental risk factors / triggers.** NSAIDs (COX inhibitors) are expected to **aggravate** the enteropathy because they act downstream of the already-starved pathway; occult NSAID use is a key confounder in differential diagnosis.

**Protective factors.** None established genetically. Mechanistically, **prostaglandin replacement** (misoprostol, PGE2/prostacyclin analogs) is protective in models (see §6, §12).

**Gene–environment interactions.** The defining interaction is **NSAID exposure on a prostaglandin-deficient background** — pharmacologic COX inhibition in a patient who already cannot supply AA would be expected to compound mucosal injury. Urinary prostanoid-metabolite screening can distinguish inherited deficiency from occult NSAID enteropathy.

---

## 3. Phenotypes

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Recurrent small-intestinal ulcers | Clinical sign / structural | Childhood–young adult | Severe, recurrent/progressive | Core feature (all probands) | HP:0005263 (gastrointestinal ulceration) |
| Intestinal strictures / stenosis / subocclusion | Structural | Young adult | Moderate–severe, progressive | Frequent | HP:0005214 (intestinal stricture) |
| Intestinal fistula / perforation | Structural | Variable | Severe | Reported | HP:0005208 (enteric fistula) / intestinal perforation |
| Iron-deficiency anemia | Lab abnormality | Childhood–adult | Moderate, chronic | Frequent | HP:0001891 |
| GI blood loss / occult bleeding | Clinical sign | Childhood–adult | Chronic | Frequent | HP:0002239 (GI hemorrhage) |
| Protein-losing enteropathy / edema | Lab + sign | Adult | Moderate | Reported | HP:0000969 (edema) / protein-losing enteropathy |
| Platelet-type bleeding diathesis | Clinical sign / lab | Early (childhood) | Mild–moderate | In recessive homozygotes | HP:0011869 (abnormal platelet function); HP:0001892 (abnormal bleeding) |
| Recurrent abdominal pain | Symptom | Childhood–adult | Moderate, episodic | Frequent | HP:0002027 |

**Onset and progression.** Symptoms typically begin in **childhood to young adulthood**; the course is **chronic, recurrent, and progressive** for the enteropathy (ulcers → strictures → subocclusion/fistula), while the bleeding tendency is lifelong but generally **mild-to-moderate**.

**Quality-of-life impact.** Recurrent ulceration, strictures, chronic anemia, and protein-losing enteropathy impose substantial GI morbidity, risk of repeated surgery, nutritional compromise, and transfusion dependence. No disease-specific EQ-5D/SF-36 data exist given rarity.

Supporting evidence: Adler et al., 2008/2009 ([PMID: 18451993](https://pubmed.ncbi.nlm.nih.gov/18451993/); [PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/)); Faioni et al., 2014 ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/)); Guisado Vasco et al., 2014 ([PMID: 24035666](https://pubmed.ncbi.nlm.nih.gov/24035666/)); McAlindon, 2022 ([PMID: 35275899](https://pubmed.ncbi.nlm.nih.gov/35275899/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** *PLA2G4A* (HGNC:9035; NCBI Gene 5321; UniProt P47712), 1q31.1, encoding the 85-kDa group IVA cytosolic phospholipase A2 (cPLA2α).

**Protein architecture.** cPLA2α comprises an **N-terminal Ca²⁺-dependent C2 domain** (membrane targeting/translocation) and a **catalytic domain with an unusual Ser-Asp catalytic dyad** located in a hydrophobic funnel with a flexible lid governing interfacial activation; it **selectively cleaves arachidonyl phospholipids** (Dessen et al., 1999; [PMID: 10319815](https://pubmed.ncbi.nlm.nih.gov/10319815/)).

> "An unusual Ser-Asp dyad located in a deep cleft at the center of a predominantly hydrophobic funnel selectively cleaves arachidonyl phospholipids." — Dessen et al., 1999 ([PMID: 10319815](https://pubmed.ncbi.nlm.nih.gov/10319815/))

**Pathogenic variants and functional consequences.**

| Variant (protein) | Nucleotide | Type | Functional effect | Evidence |
|---|---|---|---|---|
| p.Ser111Pro | — | Missense | Impairs **Ca²⁺ binding & Golgi/membrane translocation**; catalysis intact | Reed et al., 2011 ([PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/)) |
| p.Arg485His | — | Missense | **Nearly devoid of catalytic activity** | Reed et al., 2011 ([PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/)) |
| p.Lys651Arg | — | Missense | Common polymorphism; activity slightly > wild type (neutral) | Reed et al., 2011 ([PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/)) |
| p.Asp575His | c.1723G>C | Missense | **Protein instability** — transcribed but not stably translated; undetectable protein | Faioni 2014 ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/)); Zulueta 2015 ([PMID: 25904158](https://pubmed.ncbi.nlm.nih.gov/25904158/)) |

> "the R485H mutant was nearly devoid of any catalytic activity, that the S111P mutation did not affect the enzyme activity" — Reed et al., 2011 ([PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/))

The **compound-heterozygous** Adler patient thus carries one allele that cannot catalyze (R485H) and one allele that cannot translocate to membranes (S111P) — a two-hit convergence that abolishes effective enzyme function. The **homozygous** Faioni/Zulueta mechanism is **protein instability**: the mRNA is present but protein is undetectable on Western blot.

> "suggesting that the variant is transcribed, but not translated or translated into an unstable protein" — Faioni et al., 2014 ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/))

**Variant classification.** All reported disease alleles behave as **loss-of-function** (ACMG: pathogenic/likely pathogenic on functional + segregation grounds). **Allele frequency:** disease alleles are private/ultra-rare; p.Lys651Arg is a common benign polymorphism.

**Somatic vs germline.** All reported disease variants are **germline**. (Of note, somatic/expression-level *PLA2G4A* changes appear in cancer contexts — e.g., colorectal cancer ferroptosis regulation, [PMID: 41400081](https://pubmed.ncbi.nlm.nih.gov/41400081/) — but these are unrelated to the Mendelian deficiency.)

**Modifier genes / epigenetics / chromosomal abnormalities.** Co-inherited factor XI deficiency modifies bleeding (above). No disease-specific epigenetic signature or chromosomal abnormality is described.

---

## 5. Environmental Information

- **Environmental factors:** No environmental agent causes the disease. **NSAIDs/COX inhibitors** are expected to exacerbate the enteropathy and should be avoided.
- **Lifestyle factors:** None established.
- **Infectious agents:** Not applicable; the disorder is not infectious. (Secondary bacterial complications of ulceration/perforation are possible, as with any severe enteropathy.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LoF variants in *PLA2G4A*** (catalytic-dead p.Arg485His, translocation-dead p.Ser111Pro, or unstable p.Asp575His) **lead to** absent or non-functional cPLA2α protein.
2. Loss of functional cPLA2α **results in** failure to release **arachidonic acid** from the *sn*-2 position of membrane phospholipids upon cell stimulation (the rate-limiting step).
3. AA substrate starvation **leads to** collapse of downstream **COX** (prostaglandins, thromboxane, prostacyclin) and **LOX** (leukotrienes, HETEs) product formation across cell types.
4. **Branch A — Platelets:** Near-absent **thromboxane A2/B2 and 12-HETE** **results in** defective platelet activation/aggregation and degranulation to ADP and collagen → **bleeding diathesis**. (The defect is upstream of COX — exogenous AA restores aggregation.)
5. **Branch B — GI mucosa:** Deficient **cytoprotective prostaglandins (PGE2, prostacyclin)** in the small-bowel mucosa **results in** loss of mucosal defense → recurrent **ulceration → stenosis/strictures → fistula/perforation**, with **GI bleeding, iron-deficiency anemia, and protein-losing enteropathy** (an "endogenous NSAID-enteropathy" phenotype). *Inferred* from the mechanistic parallel to NSAID enteropathy plus depressed urinary prostanoids.
6. **Branch C — Endothelium/leukocytes:** Reduced (but not absent) endothelial **prostacyclin** and near-absent leukocyte **PGE2/LTB4** **lead to** a pro-inflammatory, "primed" endothelial/leukocyte state.
7. **Branch D — Reproduction (model-demonstrated):** Loss of uterine epithelial cPLA2α-derived prostaglandins **results in** deferred implantation, delayed parturition, and small litters (mouse).

> "These findings suggested deficient AA release from membrane phospholipids by cytosolic phospholipase A2-alpha (cPLA2-alpha), which regulates cyclooxygenase- and lipoxygenase-mediated eicosanoid production by catalyzing the release of their substrate, AA." — Adler et al., 2009 ([PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/))

### Pathway, cell, and compartment diagram

```
 PLA2G4A (LoF)                     [upstream / initiating]
      │
      ▼
 cPLA2α absent/nonfunctional ── C2-domain Ca2+-dependent translocation to Golgi/perinuclear ER fails
      │
      ▼
 No arachidonic acid (AA) released from membrane phospholipids   (GO:0019369 AA metabolism)
      │
      ├───────────────┬───────────────┬──────────────┐
      ▼               ▼               ▼              ▼
   COX-1/COX-2     5-LOX / 12-LOX   (platelets)   (uterine epi)
   PGE2, PGI2,     LTB4, LTE4,      TxA2, 12-HETE  PGE2/PGF2α
   TxA2 ↓↓         HETEs ↓↓         ↓↓↓            ↓↓
      │               │               │              │
      ▼               ▼               ▼              ▼
  GI mucosal      inflammation     platelet       implantation/
  cytoprotection  dysregulation    dysfunction    parturition
  lost → ulcers   (endothelium     → bleeding      defects (mouse)
  /strictures     "primed")        diathesis
                                   [downstream / clinical]
```

**Molecular pathways:** arachidonic acid metabolism; eicosanoid (prostaglandin/thromboxane/leukotriene) biosynthesis (KEGG hsa00590; Reactome AA metabolism).
**Cellular processes:** inflammation, platelet activation/degranulation, mucosal cytoprotection.
**Subcellular compartments:** cytosol → **Golgi/perinuclear ER/nuclear envelope** (site of Ca²⁺-triggered cPLA2α translocation and AA release). GO CC: GO:0005829 (cytosol), GO:0005794 (Golgi apparatus), GO:0005635 (nuclear envelope).
**Suggested GO BP:** GO:0019369 (arachidonic acid metabolic process), GO:0001516 (prostaglandin biosynthetic process), GO:0006954 (inflammatory response), GO:0030168 (platelet activation).
**Suggested CL:** CL:0000233 (platelet/thrombocyte), CL:0000235 (macrophage), CL:0000066 (epithelial cell; intestinal/uterine luminal epithelium), CL:0002139 (endothelial cell).
**CHEBI:** CHEBI:15843 (arachidonic acid), CHEBI:26333 (prostaglandin), CHEBI:26347 (prostanoid/thromboxane), CHEBI:25029 (leukotriene).

### Quantitative biochemical signature (human)

| Analyte | Control | Patient | Source |
|---|---|---|---|
| Serum TxB2 production | 100% | **4.6%** (P<0.006) | [PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/) |
| Serum 12-HETE | 100% | **1.3%** (P<0.005) | [PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/) |
| Leukocyte LTB4 biosynthesis | 100% | **~3%** | [PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/) |
| Platelet TxA2 | 20.5 ± 1.4 ng/ml | **0.1 ng/ml** | [PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) |
| Leukocyte PGE2 | 21.9 ± 7.4 ng/ml | **1.9 ng/ml** | [PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) |
| Endothelial prostacyclin (PGI2) | 956 ± 422 pg/ml | **196 pg/ml** (reduced, not absent) | [PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) |
| Urinary prostacyclin metabolites | 100% | **18.4%** | [PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) |
| Urinary PGE2 metabolites | 100% | **~77.8%** | [PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) |

A key nuance: the deficiency is **near-complete in platelets and leukocytes** but only **partial in endothelium** (residual prostacyclin), implying cell-type-specific compensation by other phospholipases, and leaving the endothelium "primed for inflammation."

> "cPLA2α-deficient endothelial cells showed reduced, but not absent, formation of prostaglandin I2 (prostacyclin; control 956 ± 422 pg/ml vs. patient 196 pg/ml) and were primed for inflammation." — Kirkby et al., 2015 ([PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/))

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Small intestine** (UBERON:0002108) — recurrent ulceration, stenosis, fistula. Body system: **digestive system** (UBERON:0001007).
- **Hematologic involvement:** **Platelets/blood** (platelet dysfunction, bleeding diathesis).
- **Secondary/complication organs:** systemic effects of chronic GI blood loss (anemia) and protein loss (edema). Endothelium/vasculature shows a pro-inflammatory state.
- **Model-demonstrated additional organs (mouse):** **uterus** (UBERON:0000995, reproductive failure), **kidney** (UBERON:0002113, concentration defect), **heart** (exaggerated ischemia–reperfusion injury), **lung/airway** (reduced bronchial reactivity), **brain** (altered injury susceptibility).
- **Tissue/cell level:** intestinal **luminal epithelium** (CL:0000066), **platelets** (CL:0000233), **macrophages/leukocytes** (CL:0000235), **endothelial cells** (CL:0002139); uterine luminal epithelium in mouse.
- **Subcellular:** cytosol, Golgi apparatus, nuclear envelope/perinuclear ER (site of AA release).
- **Lateralization:** Not applicable (systemic/bilateral by nature).

---

## 8. Temporal Development

- **Onset:** childhood to young adulthood; **chronic/insidious** onset of GI symptoms; bleeding tendency apparent early.
- **Progression:** the enteropathy is **progressive** (ulcers → strictures/stenosis → subocclusion → fistula/perforation), punctuated by **episodic** flares of pain and bleeding.
- **Disease course / duration:** **chronic, lifelong.** No spontaneous remission is described; remission of mucosal injury is treatment-related (prostaglandin replacement, NSAID avoidance).
- **Critical periods / windows for intervention:** prevention of NSAID exposure throughout life; early prostaglandin replacement to protect mucosa and manage bleeding.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive.** Homozygous (p.Asp575His) and compound-heterozygous (p.Ser111Pro/p.Arg485His) genotypes described.
- **Penetrance/expressivity:** The severe recessive phenotype requires biallelic LoF. **Heterozygotes show partial penetrance for the GI phenotype**: in the Faioni kindred, **GI ulcers affected 5/14 heterozygous members under 40 years** vs **1/16 wild-type members over 60 years**; crucially, **no heterozygote had a bleeding diathesis** (bleeding is strictly recessive).

> "Platelet aggregation and degranulation induced by adenosine diphosphate or collagen were diminished but were normal in response to arachidonic acid." — Adler et al., 2008 ([PMID: 18451993](https://pubmed.ncbi.nlm.nih.gov/18451993/))

- **Epidemiology:** **Ultra-rare** — fewer than ~5 published probands across 2–3 unrelated families; no reliable prevalence/incidence figures exist. Orphanet/OMIM-level aggregation is limited by rarity.
- **Founder effects / consanguinity / carrier frequency:** The homozygous p.Asp575His family is consistent with identity-by-descent; no established founder population or carrier-frequency estimate. Disease alleles are private/ultra-rare in gnomAD.
- **Sex ratio / demographics:** Both sexes affected (reported male proband + twin sister; siblings). No sex predilection established. No defined geographic/ethnic clustering.

---

## 10. Diagnostics

**Biochemical (first-line, disease-defining):**
- **Platelet TxB2 / 12-HETE** — markedly reduced.
- **Calcium-ionophore–induced leukocyte LTB4** — markedly reduced; urinary LTE4 may be undetectable.
- **Urinary prostanoid metabolites** (e.g., **11-dehydro-TxB2**, PGE2/PGI2 metabolites) — depressed. Also useful to **exclude occult NSAID use**.
- **Platelet aggregometry:** blunted response to ADP/collagen that is **normalized by exogenous arachidonic acid** — the pathognomonic "upstream of COX" signature.
- **Western blot:** platelet cPLA2α **undetectable** (p.Asp575His homozygotes).

> "platelet cPLA2a was undetectable by Western Blotting in the proband and his sister" — Faioni et al., 2014 ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/))

**Genetic testing:** **Single-gene *PLA2G4A* sequencing** confirms the diagnosis; WES/WGS or a GI/platelet-disorder gene panel is reasonable in undiagnosed cases. Functional confirmation (enzyme assay, translocation, protein stability) supports VUS interpretation.

**Imaging/endoscopy:** capsule endoscopy, enterography (CT/MR), and small-bowel studies reveal multifocal ulcers, short strictures, and subocclusion; biopsy shows superficial submucosal ulceration with edema.

**Clinical criteria / differential diagnosis:** There are no formal consensus criteria. Diagnosis rests on the **tetrad of small-bowel ulcerating/stenosing disease + platelet-type bleeding + global eicosanoid deficiency + biallelic *PLA2G4A* variants**. Key differentials:
- **SLCO2A1-related chronic enteropathy (CEAS/CMUSE)** — prostaglandin **transporter** defect, phenotypically overlapping.
- **NSAID enteropathy** — excluded by urinary metabolite screen (occult NSAID use).
- Crohn's disease, cryptogenic multifocal ulcerating stenosing enteritis (CMUSE), other platelet secretion/aggregation disorders.

> "Mutations in the PLA2G4A gene result in cytosolic phospholipase A2α deficiency and reduced arachidonic acid for prostaglandin synthesis leading to a severe ulcerating, stenosing and fistulating small bowel disease." — McAlindon, 2022 ([PMID: 35275899](https://pubmed.ncbi.nlm.nih.gov/35275899/))

**Screening:** No population or newborn screening exists. Cascade genetic testing of relatives is appropriate once a family variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival data; the disorder is not typically rapidly lethal but carries morbidity from recurrent surgery, perforation risk, chronic anemia, and protein loss. Life expectancy data are unavailable given rarity.
- **Morbidity/function:** Substantial — recurrent small-bowel obstruction/strictures, fistula/perforation, iron-deficiency anemia, protein-losing enteropathy with edema, and a lifelong bleeding tendency.
- **Complications:** bowel stenosis/subocclusion, fistulae, perforation, chronic GI hemorrhage, transfusion dependence, nutritional deficiency.
- **Prognostic factors:** degree of residual eicosanoid production (cell-type dependent), NSAID avoidance, access to prostaglandin replacement, surgical burden.
- **Recovery:** chronic disease; mucosal protection and NSAID avoidance can reduce flares, but the underlying enzymatic defect is permanent.

---

## 12. Treatment

**No approved disease-specific (curative) therapy exists.** Management is **supportive and mechanism-based**:

| Intervention | Rationale / evidence | Suggested NCIT |
|---|---|---|
| **Misoprostol (PGE1 analog)** — prostaglandin replacement | Replaces deficient cytoprotective prostaglandin; misoprostol ameliorated eicosanoid-deficiency injury in cPLA2α-null hearts ([PMID: 21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/)) | NCIT:C62042 (Misoprostol) |
| **NSAID avoidance** | Patients cannot buffer further COX inhibition | — |
| Iron supplementation / transfusion | Chronic GI blood loss, iron-deficiency anemia | NCIT:C29059 (Iron) |
| Nutritional support (protein-losing enteropathy) | Edema, hypoproteinemia | — |
| Mucosal protection / ulcer management | Symptomatic ulcer/stricture control | — |
| Surgical resection / stricturoplasty | Obstructing strictures, fistula, perforation | NCIT (bowel resection) |
| Bleeding management (platelet support, antifibrinolytics) | Platelet-function defect | — |

> "the enhanced injury is ameliorated by treatment with the PGE analog, misoprostol" — Kerkelä et al., 2011 ([PMID: 21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/))

Preclinical proof-of-concept for **prostaglandin replacement** also comes from the reproductive rescue in Pla2g4a-null mice:

> "Pla2g4a-null females that received PGE2 + carbaprostacyclin at the time of implantation delivered earlier (20.5 +/- 0.2 days vs. 21.6 +/- 0.2 days, P < 0.01)" — Brown et al., 2009 ([PMID: 19684335](https://pubmed.ncbi.nlm.nih.gov/19684335/))

**Advanced/experimental therapeutics:** No gene therapy, RNA therapy, or targeted therapy is in clinical use for this indication. Conceptually, **enzyme/gene replacement** of *PLA2G4A* or **downstream eicosanoid-analog supplementation** are rational future directions. No registered NCT trials are specific to this ultra-rare disease.

**Personalized medicine:** Treatment is inherently genotype-driven (confirmed biallelic LoF); cell-type-specific residual activity may influence response.

---

## 13. Prevention

- **Primary prevention:** Not applicable to disease occurrence (Mendelian). **Preconception/prenatal genetic counseling and carrier testing** in affected families; options include prenatal diagnosis and preimplantation genetic testing for known family variants.
- **Secondary prevention:** Cascade genetic testing of at-risk relatives; early biochemical screening (eicosanoid profiling) in symptomatic kin.
- **Tertiary prevention (preventing complications):** **strict NSAID avoidance**, prostaglandin replacement (misoprostol), iron repletion, and surveillance for strictures/bleeding to prevent perforation and obstruction.
- **Counseling:** Autosomal-recessive recurrence risk (25% for carrier couples); heterozygotes may have a milder GI predisposition but no bleeding risk — relevant genetic-counseling nuance.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Pla2g4a* is conserved; mouse *Pla2g4a* (NCBI Gene 18783) is the principal model ortholog. Human NCBI Gene 5321.
- **Natural disease in other species:** No well-characterized naturally occurring companion-animal or wildlife disease is documented; knowledge derives from engineered mouse knockouts.
- **Comparative biology:** The mouse knockout **recapitulates core human features** (intestinal ulceration; near-absent eicosanoid production) while revealing **additional organ roles** (renal concentration defect, reproductive failure, context-dependent cardioprotection/neuroprotection) — demonstrating strong evolutionary conservation of the AA-release → eicosanoid axis.
- **Zoonotic potential:** None (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) *Pla2g4a* knockout** is the definitive model.

| Model / study | Key phenotypes | Relevance |
|---|---|---|
| **Uozumi et al., 1997, Nature** ([PMID: 9403692](https://pubmed.ncbi.nlm.nih.gov/9403692/)) | ↓ eicosanoids & PAF in peritoneal macrophages; reduced ovalbumin anaphylaxis and bronchial reactivity; females fail to deliver (rescuable by progesterone-receptor antagonist) | First KO; non-redundant role in allergy & reproduction |
| **Uozumi & Shimizu, 2002 (review)** ([PMID: 12432909](https://pubmed.ncbi.nlm.nih.gov/12432909/)) | Normal growth but **renal concentration defect + intestinal ulcerative lesions**; small litters; milder anaphylaxis, lung injury, I/R, MPTP, polyposis | Recapitulates hallmark **intestinal ulceration** |
| **Brown et al., 2009** ([PMID: 19684335](https://pubmed.ncbi.nlm.nih.gov/19684335/)) | ↓ uterine PGE2/PGF2α/6-keto-PGF1α/TxB2; delayed implantation/parturition; **rescued by PGE2 + carbaprostacyclin** | Pharmacologic prostaglandin rescue |
| **Kerkelä et al., 2011** ([PMID: 21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/)) | **Exaggerated cardiac ischemia–reperfusion injury**; ↓PGE2; ameliorated by misoprostol | cPLA2α is **cardioprotective**; caution for inhibition |
| **Sapirstein & Bonventre, 2000** ([PMID: 10905638](https://pubmed.ncbi.nlm.nih.gov/10905638/)) | **Protected** against neuronal injury in ischemia/reperfusion & MPTP | Context-dependent (protective in brain) |

> "Their ovalbumin-induced anaphylactic responses were significantly reduced, as was their bronchial reactivity to methacholine." — Uozumi et al., 1997 ([PMID: 9403692](https://pubmed.ncbi.nlm.nih.gov/9403692/))

> "Close examinations have revealed a renal concentration defect and intestinal ulcerative lesions." — Uozumi & Shimizu, 2002 ([PMID: 12432909](https://pubmed.ncbi.nlm.nih.gov/12432909/))

> "In each model cPLA2 deficient mice are protected against neuronal injury when compared to their wild type littermate controls." — Sapirstein & Bonventre, 2000 ([PMID: 10905638](https://pubmed.ncbi.nlm.nih.gov/10905638/))

**Model limitations:** Mouse knockouts reveal additional organ phenotypes (renal, reproductive, cardiac) that are not prominent clinical features in the few described human patients — partly reflecting the small human sample and possible species-specific phospholipase redundancy. The **direction of effect is context-dependent** (protective in brain, deleterious in heart/intestine), complicating extrapolation.

**In vitro / structural models:** Recombinant cPLA2α enzymology (Reed et al., 2011, [PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/)); crystal structure (Dessen et al., 1999, [PMID: 10319815](https://pubmed.ncbi.nlm.nih.gov/10319815/)); cellular expression/stability assays (Zulueta et al., 2015, [PMID: 25904158](https://pubmed.ncbi.nlm.nih.gov/25904158/)).

---

## Key Findings (with statistical evidence)

**F001 — cPLA2α deficiency is an autosomal-recessive *PLA2G4A* disorder causing eicosanoid-deficiency enteropathy with platelet dysfunction.** Two unrelated families anchor the entity. The Adler proband (compound heterozygous p.Ser111Pro + [p.Arg485His; p.Lys651Arg]) had multiple small-intestinal ulcers, markedly reduced platelet TxB2/12-HETE and ionophore-induced LTB4, and diminished aggregation/degranulation to ADP/collagen that **normalized with arachidonic acid** — proving the lesion is upstream of COX ([PMID: 18451993](https://pubmed.ncbi.nlm.nih.gov/18451993/)). The Faioni family (homozygous p.Asp575His, a 27-year-old man and his twin sister) showed early bleeding diathesis, recurrent GI ulcers, undetectable platelet cPLA2α on Western blot, and extremely low serum TxB2/12-HETE and urinary 11-dehydro-TxB2 ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/)).

**F002 — Prostaglandin deficiency mechanistically links cPLA2α loss to an NSAID-like enteropathy.** Adler's "enteropathy of prostaglandin deficiency" patient had chronic recurrent small-intestinal ulcers, small-bowel perforations, and GI blood loss **despite no COX-inhibitor use**, with serum TxB2 at 4.6% (P<0.006) and 12-HETE at 1.3% (P<0.005) of controls, leukocyte LTB4 at ~3%, and undetectable urinary LTE4 ([PMID: 19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/)).

**F003 / F006 / F009 — Mouse knockouts validate causality and reveal multi-organ roles.** Pla2g4a-null mice show significantly decreased uterine PGE2/PGF2α/6-keto-PGF1α/TxB2 with delayed implantation and parturition, pharmacologically rescued by PGE2 + carbaprostacyclin (20.5±0.2 vs 21.6±0.2 days, P<0.01) ([PMID: 19684335](https://pubmed.ncbi.nlm.nih.gov/19684335/)). Broader knockout data show intestinal ulceration plus a renal concentration defect ([PMID: 12432909](https://pubmed.ncbi.nlm.nih.gov/12432909/)) and the landmark non-redundant role in allergy and reproduction ([PMID: 9403692](https://pubmed.ncbi.nlm.nih.gov/9403692/)). Context-dependence is notable — protective in brain injury ([PMID: 10905638](https://pubmed.ncbi.nlm.nih.gov/10905638/)) but deleterious in cardiac I/R ([PMID: 21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/)).

**F004 — Structure–function maps each variant to a distinct defect.** cPLA2α uses a Ser-Asp catalytic dyad selective for arachidonyl phospholipids ([PMID: 10319815](https://pubmed.ncbi.nlm.nih.gov/10319815/)); p.Arg485His abolishes catalysis, p.Ser111Pro abolishes Ca²⁺-dependent membrane translocation without affecting catalysis, and p.Lys651Arg is neutral ([PMID: 21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/)). Compound heterozygosity therefore combines two separable loss-of-function mechanisms.

**F005 — Cell-type-specific eicosanoid loss.** Platelet TxA2 (20.5±1.4 → 0.1 ng/ml) and leukocyte PGE2 (21.9±7.4 → 1.9 ng/ml) are nearly abolished, whereas endothelial prostacyclin is reduced but not absent (956±422 → 196 pg/ml), leaving endothelium "primed for inflammation"; urinary prostacyclin metabolites fell to 18.4% while PGE2 metabolites remained ~77.8% of control ([PMID: 26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/)).

**F007 — A prostaglandin-related ulcerating/stenosing/fistulating small-bowel disease.** The full phenotype (ulcers, strictures, fistulae, iron-deficiency anemia, protein-losing enteropathy) sits in a differential with SLCO2A1-CMUSE and NSAID enteropathy; a urinary-metabolite screen reveals occult NSAID use ([PMID: 35275899](https://pubmed.ncbi.nlm.nih.gov/35275899/); [PMID: 24035666](https://pubmed.ncbi.nlm.nih.gov/24035666/)).

**F008 — p.Asp575His acts via protein instability; heterozygotes show partial GI penetrance.** The variant is transcribed but yields unstable/undetectable protein ([PMID: 25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/); [PMID: 25904158](https://pubmed.ncbi.nlm.nih.gov/25904158/)); GI ulcers affected 5/14 heterozygotes (<40 y) vs 1/16 wild-type (>60 y), while bleeding was strictly recessive, and co-inherited mild factor XI deficiency may modify bleeding.

**F010 — Management is supportive prostaglandin replacement; the human deficiency is the on-target toxicity of cPLA2α inhibition.** cPLA2α is a long-standing anti-inflammatory/anti-asthma drug target ([PMID: 16712837](https://pubmed.ncbi.nlm.nih.gov/16712837/)); the inherited human deficiency therefore defines the predicted toxicity (GI ulceration + bleeding) of complete pharmacologic blockade, with misoprostol-based replacement supported by model rescue ([PMID: 21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/); [PMID: 19684335](https://pubmed.ncbi.nlm.nih.gov/19684335/)).

---

## Mechanistic Model / Interpretation

The disease is best understood as a **single enzymatic "choke point" failure** with pleiotropic downstream consequences. cPLA2α sits at the apex of eicosanoid signaling as the only PLA2 that selectively and efficiently releases arachidonate on cell activation. Because every prostaglandin, thromboxane, prostacyclin, and leukotriene depends on this released AA, a complete loss collapses the whole lipid-mediator network simultaneously — but **not uniformly across cell types**. Platelets and leukocytes, which rely heavily on cPLA2α-derived AA, lose ~99% of their thromboxane/HETE/leukotriene output, explaining the bleeding and inflammatory-regulation defects. The small-intestinal mucosa loses cytoprotective prostaglandins, producing an "endogenous NSAID enteropathy." The endothelium retains partial prostacyclin production (residual/compensatory phospholipases), yet is pushed toward a pro-inflammatory state.

```
Supported hypotheses:                       Refuted / excluded:
• AR LoF of PLA2G4A is causal       ✔       • Primary environmental/infectious cause   ✘
• Global eicosanoid deficiency      ✔       • COX/synthase-level defect (AA rescues)    ✘
• Upstream-of-COX platelet lesion   ✔       • Dominant bleeding in heterozygotes        ✘
• Prostaglandin-deficiency enteropathy ✔
• Misoprostol/PG-analog rescue (model) ✔
```

This mechanistic model also unifies the **human deficiency and the pharmacology**: cPLA2α has been pursued as an anti-inflammatory drug target, and the inherited human loss-of-function phenotype is effectively the toxicology readout of maximal target engagement — a point reinforced by mouse data showing cPLA2α is cardioprotective and its loss worsens cardiac ischemia–reperfusion injury.

---

## Evidence Base

| PMID | Study | Source type | Contribution |
|---|---|---|---|
| [18451993](https://pubmed.ncbi.nlm.nih.gov/18451993/) | Adler 2008 | Human clinical | First human case; compound-het genotype; platelet/eicosanoid defect upstream of AA |
| [19148786](https://pubmed.ncbi.nlm.nih.gov/19148786/) | Adler 2009 | Human clinical | "Enteropathy of prostaglandin deficiency"; quantified global eicosanoid loss |
| [25102815](https://pubmed.ncbi.nlm.nih.gov/25102815/) | Faioni 2014 | Human clinical | Homozygous p.Asp575His; undetectable protein; heterozygote penetrance; factor XI |
| [25904158](https://pubmed.ncbi.nlm.nih.gov/25904158/) | Zulueta 2015 | In vitro | Protein instability mechanism for p.Asp575His |
| [21247147](https://pubmed.ncbi.nlm.nih.gov/21247147/) | Reed 2011 | In vitro | Functional mapping of patient variants (catalysis vs translocation) |
| [10319815](https://pubmed.ncbi.nlm.nih.gov/10319815/) | Dessen 1999 | Structural | Crystal structure; Ser-Asp dyad; arachidonyl selectivity |
| [26183771](https://pubmed.ncbi.nlm.nih.gov/26183771/) | Kirkby 2015 | Human clinical | Cell-type-specific eicosanoid loss; endothelium primed for inflammation |
| [19684335](https://pubmed.ncbi.nlm.nih.gov/19684335/) | Brown 2009 | Model organism | KO reproductive phenotype; prostaglandin rescue |
| [12432909](https://pubmed.ncbi.nlm.nih.gov/12432909/) | Uozumi 2002 | Model organism | KO review; intestinal ulceration + renal defect |
| [9403692](https://pubmed.ncbi.nlm.nih.gov/9403692/) | Uozumi 1997 | Model organism | First KO; allergy + parturition roles |
| [21884509](https://pubmed.ncbi.nlm.nih.gov/21884509/) | Kerkelä 2011 | Model organism | Cardioprotective role; misoprostol rescue; inhibition caution |
| [10905638](https://pubmed.ncbi.nlm.nih.gov/10905638/) | Sapirstein 2000 | Model organism | Neuroprotection from cPLA2α loss (context dependence) |
| [35275899](https://pubmed.ncbi.nlm.nih.gov/35275899/) | McAlindon 2022 | Review | Prostaglandin-related enteropathy framework; differentials |
| [24035666](https://pubmed.ncbi.nlm.nih.gov/24035666/) | Guisado Vasco 2014 | Human clinical | CMUSE-type presentation; anemia, protein-losing enteropathy |
| [16712837](https://pubmed.ncbi.nlm.nih.gov/16712837/) | Malaviya 2006 | Model organism | cPLA2α as anti-inflammatory drug target (toxicity context) |

---

## Limitations and Knowledge Gaps

1. **Extremely small human sample.** Fewer than ~5 published probands; no prevalence, incidence, survival, or validated quality-of-life data. Phenotype spectrum and natural history are incompletely defined.
2. **No formal diagnostic criteria or guidelines.** Diagnosis is ad hoc (biochemical + genetic).
3. **Variant-level data are sparse.** Only a few alleles are characterized; no comprehensive ClinVar landscape or founder analysis.
4. **Mouse–human discordance.** Knockouts show renal, reproductive, cardiac, and neurologic phenotypes not clearly prominent in patients, and the effect direction is context-dependent — complicating extrapolation.
5. **Therapy is unproven in humans.** Misoprostol/prostaglandin replacement is supported only by model rescue and mechanistic reasoning, not controlled human trials.
6. **Modifier biology underexplored.** Cell-type-specific residual eicosanoid production (e.g., endothelial prostacyclin) and modifiers like factor XI are only beginning to be understood.
7. **No epigenetic, single-cell, or multi-omic patient datasets** exist for this disease.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry / GeneMatcher outreach** to aggregate additional probands and define natural history, penetrance, and genotype–phenotype correlations.
2. **Standardize a diagnostic biochemical panel** (platelet TxB2/12-HETE, ionophore-induced LTB4, urinary 11-dehydro-TxB2 and PGI2/PGE2 metabolites, AA-rescue aggregometry) as a reproducible workup, with urinary-metabolite screening to exclude occult NSAID use.
3. **Functionally characterize all reported and novel variants** (catalysis, Ca²⁺ binding/translocation, protein stability) to build an ACMG-grade functional-evidence database.
4. **Conduct n-of-1 or small controlled studies of misoprostol/prostaglandin-analog replacement** for enteropathy and bleeding, with eicosanoid-metabolite and mucosal-healing endpoints.
5. **Develop patient iPSC-derived intestinal organoids and megakaryocytes/platelets** to model mucosal cytoprotection and platelet dysfunction and to test eicosanoid-replacement and gene-correction strategies.
6. **Build conditional, tissue-specific mouse models** (intestinal epithelium, platelet) to dissect the enteropathy and bleeding mechanisms separately and test prostaglandin rescue.
7. **Formalize a differential-diagnosis protocol** distinguishing cPLA2α deficiency from SLCO2A1-CEAS/CMUSE and occult NSAID enteropathy using urinary metabolite screening plus targeted gene panels.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 46 reviewed papers. Evidence integrates human clinical case series, in vitro enzymology and structural biology, and mouse genetic models.*


## Artifacts

- [OpenScientist final report](Cytosolic_Phospholipase_A2_Alpha_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cytosolic_Phospholipase_A2_Alpha_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018794` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cytosolic phospholipase-A2 alpha deficiency associated bleeding disorder**
- `HP:0005263` (1 mention) - the report calls it "gastrointestinal ulceration"; HP calls it **Gastritis**
- `HP:0005208` (1 mention) - the report calls it "enteric fistula"; HP calls it **Secretory diarrhea**
- `HP:0001891` (1 mention) - the report calls it "Frequent"; HP calls it **Iron deficiency anemia**
- `HP:0002027` (1 mention) - the report calls it "Frequent"; HP calls it **Abdominal pain**
- `CL:0000066` (2 mentions) - the report calls it "epithelial cell; intestinal/uterine luminal epithelium", "luminal epithelium", "Tissue/cell level:** intestinal **luminal epithelium"; CL calls it **epithelial cell**
- `NCIT:C62042` (1 mention) - the report calls it "Misoprostol"; NCIT calls it **Leuprolide**
- `NCIT:C29059` (1 mention) - the report calls it "Iron"; NCIT calls it **Fluoxamine**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29059` (Fluoxamine) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005214` (1 mention) - the report calls it "intestinal stricture"; HP calls it **Intestinal obstruction**
- `GO:0019369` (2 mentions) - the report calls it "arachidonic acid metabolic process"; GO calls it **arachidonate metabolic process**, and lists "arachidonic acid metabolic process" among its other names
- `CL:0000233` (2 mentions) - the report calls it "platelet/thrombocyte", "platelets"; CL calls it **platelet**, and lists "anucleate thrombocyte" among its other names
- `CL:0000235` (2 mentions) - the report calls it "macrophage", "macrophages/leukocytes"; CL calls it **macrophage**
- `CL:0002139` (2 mentions) - the report calls it "endothelial cell", "endothelial cells"; CL calls it **endothelial cell of vascular tree**, and lists "vascular endothelial cell" among its other names
- `CHEBI:26347` (1 mention) - the report calls it "prostanoid/thromboxane"; CHEBI calls it **prostanoid**
- `UBERON:0002108` (1 mention) - the report calls it "Small intestine", "Primary organ:** **Small intestine"; UBERON calls it **small intestine**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000233` - called "platelet/thrombocyte", "platelets"
- `CL:0000235` - called "macrophage", "macrophages/leukocytes"
- `CL:0000066` - called "epithelial cell; intestinal/uterine luminal epithelium", "luminal epithelium", "Tissue/cell level:** intestinal **luminal epithelium"
- `CL:0002139` - called "endothelial cell", "endothelial cells"
- `UBERON:0002108` - called "Small intestine", "Primary organ:** **Small intestine"