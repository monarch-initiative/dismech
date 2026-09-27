---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T13:02:56.755312'
end_time: '2026-09-22T13:49:51.437495'
duration_seconds: 2814.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 102
  mondo_id: MONDO:0014428
  category: Disease
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
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 9
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0014428
    reported_labels:
    - MONDO
    ontology_label: autosomal recessive nonsyndromic hearing loss 102
  - term_id: HP:0008619
    reported_labels:
    - Bilateral SNHL
    - Localization / lateralization:** **Bilateral**, symmetric cochlear involvement
    ontology_label: Bilateral sensorineural hearing impairment
  - term_id: NCIT:C15694
    reported_labels:
    - Cochlear Implant
    ontology_label: Phase II/III Trial
  - term_id: NCIT:C99936
    reported_labels:
    - Hearing Aid
    ontology_label: Catecholaminergic Polymorphic Ventricular Tachycardia by ECG Finding
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_102-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_102-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 102
- **MONDO ID:** MONDO:0014428 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 102** covering all of the
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

# Autosomal Recessive Nonsyndromic Hearing Loss 102 (DFNB102): A Comprehensive Disease Report

**Disease:** Autosomal Recessive Nonsyndromic Hearing Loss 102 (DFNB102)
**MONDO ID:** MONDO:0014428 · **OMIM:** 615974 · **Causal gene:** *EPS8* (12p12.3)
**Report type:** Aggregated disease-level synthesis of primary literature and ontology resources

---

## Summary

**Autosomal Recessive Nonsyndromic Hearing Loss 102 (DFNB102)** is an ultrarare Mendelian sensorineural deafness caused by biallelic loss-of-function variants in *EPS8*, the gene encoding Epidermal Growth Factor Receptor Pathway Substrate 8, an 822-amino-acid F-actin capping and bundling protein. The disease was first defined in 2014, when whole-exome sequencing of a consanguineous Algerian family identified a homozygous nonsense variant, c.88C>T (p.Gln30*), segregating with isolated profound congenital deafness ([PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)). DFNB102 is genetically and clinically homogeneous within its small case series: affected individuals present with **prelingual/congenital, bilateral, symmetric, severe-to-profound, nonsyndromic sensorineural hearing loss** with no consistent vestibular, syndromic, or extra-auditory features. As of 2023, only about five pathogenic *EPS8* variants/families had been reported worldwide (Algerian, Chinese, Iranian), underscoring its rarity.

The mechanism is well delineated at the molecular and cellular level thanks to concordant human genetics and mouse models. EPS8 localizes to the tips of cochlear hair-cell stereocilia, where its C-terminal effector domain caps actin filament barbed ends and bundles the actin core. This activity is required for stereocilia to elongate to their correct staircase heights and for inner hair cells (IHCs) to mature into functional mechanoelectrical transducers. When *EPS8* is truncated or deleted, this domain is lost; stereocilia remain abnormally short, IHCs fail to mature, mechano-electrical transduction is abolished, and profound deafness results. The *Eps8*-knockout mouse faithfully recapitulates the human phenotype — it is profoundly deaf with short stereocilia — and the paralog *Eps8L2* divides labor with EPS8, handling stereocilia **maintenance** while EPS8 handles initial **elongation**.

Because EPS8 is broadly expressed and multifunctional (EGFR signaling, Rac regulation via the EPS8–ABI1–SOS1 complex, intestinal microvillus formation), one might expect a syndromic phenotype; however, human EPS8-null individuals present with **isolated deafness only**, indicating functional redundancy of EPS8 outside the cochlea (the paralogs EPS8L1/L2/L3 compensate) but a **non-redundant role at stereocilia tips**. Notably, the *Eps8*-knockout mouse displays intestinal microvillus shortening and a favorable calorie-restriction-like metabolic phenotype that is **absent from human patients**, an instructive species divergence. There is no disease-specific pharmacologic or gene therapy; diagnosis relies on exome/genome sequencing with copy-number analysis, and management is **cochlear implantation**, the standard of care for congenital severe-to-profound sensorineural hearing loss.

---

## 1. Disease Information

**Overview.** DFNB102 is a form of autosomal recessive nonsyndromic sensorineural hearing loss (SNHL). "Nonsyndromic" means hearing loss occurs in isolation, without associated malformations or dysfunction of other organ systems. "DFNB" designates a recessive (B) locus for deafness (DFN); "102" is its sequential locus number.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014428 |
| OMIM (phenotype) | 615974 (DEAFNESS, AUTOSOMAL RECESSIVE 102; DFNB102) |
| Gene | *EPS8*, OMIM 600206, HGNC:3555, NCBI Gene 2059, Ensembl ENSG00000151491, UniProt Q12929 |
| Cytoband | 12p12.3 |
| ICD-10 | H90.3 (sensorineural hearing loss, bilateral) — non-specific |
| ICD-11 | AB52.0 / bilateral sensorineural hearing impairment stem — non-specific |
| MeSH | Closest: "Hearing Loss, Sensorineural" (D006319); no DFNB102-specific MeSH term |

**Synonyms / alternative names.** DFNB102; Deafness, autosomal recessive 102; EPS8-related nonsyndromic hearing loss; autosomal recessive nonsyndromic sensorineural deafness type DFNB102.

**Information source.** This entry is derived from **aggregated disease-level resources** (OMIM, ontology databases) and **individual published case reports/families** (Algerian, Chinese, Iranian), not from a large EHR cohort. The literature base is small (a handful of families).

---

## 2. Etiology

**Primary cause — genetic.** DFNB102 is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *EPS8***. It is not caused by environmental, infectious, or acquired factors. The founding evidence: Behlouli et al. 2014 identified a homozygous nonsense variant c.88C>T (p.Gln30*) in two siblings from a consanguineous Algerian family with isolated profound congenital deafness; the variant segregated recessively (heterozygous in unaffected parents and one sib, absent from two unaffected sibs) and was absent from 120 Algerian controls and the Exome Variant Server ([PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)).

> *"A biallelic nonsense mutation, c.88C > T (p.Gln30*), was identified in EPS8 that encodes epidermal growth factor receptor pathway substrate 8, a 822 amino-acid protein involved in actin dynamics."* — [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)

**Genetic risk factors.** The causal factor is possession of two loss-of-function *EPS8* alleles. **Consanguinity** is a major risk-elevating context (the index family was consanguineous, and homozygous LoF alleles are far more likely in consanguineous unions). Carriers (heterozygotes) are unaffected.

**Environmental / lifestyle risk factors.** None established for the primary (genetic) disease. General SNHL aggravators (noise, ototoxic drugs, aging) are not documented as modifiers of DFNB102 specifically.

**Protective factors.** No genetic or environmental protective factors are described. In principle, the paralogs **EPS8L1/EPS8L2/EPS8L3** provide functional redundancy in non-cochlear tissues, explaining why the phenotype is confined to hearing (see §4, §6).

**Gene–environment interactions.** None documented. DFNB102 is a fully penetrant monogenic condition; environmental modulation has not been reported.

---

## 3. Phenotypes

The DFNB102 phenotype is dominated by a single, highly consistent manifestation.

| Phenotype | Type | Onset | Severity | Progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|---|
| Sensorineural hearing loss | Clinical sign / audiometric | Congenital / prelingual | Severe-to-profound | Non-progressive (congenitally profound) | ~100% of affected | HP:0000407 (SNHL); HP:0008527 (Congenital SNHL); HP:0000365 (Hearing impairment) |
| Bilateral involvement | Clinical sign | Congenital | — | Stable | ~100% | HP:0008619 (Bilateral SNHL) |
| Profound degree | Audiometric | Congenital | Profound (>90 dB HL) | Stable | Majority | HP:0011476 (Bilateral profound SNHL); HP:0000364 |
| Absence of syndromic features | — | — | — | — | — | (Nonsyndromic) |

**Characteristics.** Onset is **congenital/prelingual** (present at or before language acquisition). Severity is **severe-to-profound**; the Chinese case was congenital profound, the Algerian siblings profound. The loss is **bilateral and symmetric**. Because it is congenitally profound, it is best described as **stable/non-progressive** in patients (contrast with *EPS8L2* disease, which is late-onset progressive — see §4/§15). No consistent **vestibular dysfunction** or balance phenotype has been reported, and no extra-auditory (syndromic) features are documented.

> *"an 11-month-old male infant presented with congenital profound non-syndromic hearing loss"* — [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)

**Quality-of-life impact.** Congenital profound hearing loss, if unaddressed in the critical period, severely impairs spoken-language acquisition, literacy, educational attainment, and social participation. Early cochlear implantation substantially mitigates these outcomes (see §11–12). Formal EQ-5D/SF-36 data specific to DFNB102 are **not available** given the tiny cohort.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***EPS8*** (Epidermal Growth Factor Receptor Pathway Substrate 8), 12p12.3; HGNC:3555; OMIM 600206; UniProt Q12929; protein length 822 aa. EPS8 is an **F-actin capping and bundling protein**.

> *"EPS8 is an F-actin capping and bundling protein."* — [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)

**Reported pathogenic variants.** As of 2023, only ~5 pathogenic *EPS8* variants had been described ([PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/)).

| Variant (cDNA / protein) | Type | Zygosity / family | Population | Reference |
|---|---|---|---|---|
| c.88C>T (p.Gln30*) | Nonsense (LoF) | Homozygous, consanguineous | Algerian | [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/) |
| c.1435-2A>T (p.His479Cysfs*14) | Splice-site (LoF) | Compound het with CNV | Chinese | [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/) |
| ~65.9 kb intragenic deletion | Structural / CNV (LoF) | Compound het (maternal) | Chinese | [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/) |
| Fifth reported pathogenic variant | (per report) | — | Iranian | [PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/) |

> *"Thus far, only four pathogenic variations in EPS8 have been described. In this study, we report the fifth pathogenic variant in the EPS8 gene in an Iranian patient with DFNB102."* — [PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/)

**Variant classification & type.** All reported disease alleles are **pathogenic loss-of-function**: nonsense, splice-site/frameshift, and a large intragenic deletion. No pathogenic missense variant establishing DFNB102 has been reported; the mechanism requires **biallelic** loss.

**Allele frequency.** Reported variants are absent or ultrarare in population databases (c.88C>T absent from 120 Algerian controls and the Exome Variant Server; [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)). No common susceptibility allele exists.

**Somatic vs germline.** All variants are **germline**.

**Functional consequence.** **Loss of function.** Truncating and deletion alleles remove the C-terminal effector domain that carries capping/bundling activity (see §6). In the Chinese case, in vitro splicing and allele-specific expression assays confirmed near-total loss of functional transcript (0-fold WT; 0.25–0.27-fold mutant; P<0.05) ([PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)).

> *"further CNVs analysis identified a novel 65.9 kb intragenic deletion and was inherited from his mother"* — [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)

**Modifier genes.** The paralog ***EPS8L2*** is functionally relevant: it complements EPS8 at stereocilia tips and its own loss causes progressive hearing loss ([PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/)). EPS8L1/L2/L3 collectively provide redundancy outside the cochlea. No formal disease-severity modifier has been mapped for DFNB102.

**Epigenetic / chromosomal.** No epigenetic mechanism is implicated. The only "structural" lesion is the intragenic *EPS8* deletion; no aneuploidy or translocation is associated.

---

## 5. Environmental Information

**Environmental factors:** None causal or contributory — DFNB102 is monogenic.
**Lifestyle factors:** None established.
**Infectious agents:** None — DFNB102 is not an infectious or acquired deafness (contrast with congenital CMV, rubella, ototoxic exposure). Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LoF variant in *EPS8*** (nonsense / splice / deletion) **leads to** absence of functional full-length EPS8 protein, specifically deleting the C-terminal effector domain that carries capping and bundling activity. *(Demonstrated: human genetics + transcript assays, [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/), [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/).)*
2. **Loss of EPS8 at stereocilia tips** **results in** failure of barbed-end actin capping and actin-core bundling within hair-cell stereocilia. *(Demonstrated in vitro/structurally: [PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/), [PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/).)*
3. **Dysregulated stereocilia actin assembly** **leads to** abnormally short stereocilia and a decayed staircase hair-bundle architecture. *(Demonstrated in mouse: [PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/), [PMID: 21236676](https://pubmed.ncbi.nlm.nih.gov/21236676/).)*
4. **Short/disorganized hair bundles** **result in** failure of inner hair cells (IHCs) to mature into fully functional sensory receptors (OHCs comparatively spared). *(Demonstrated: [PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/).)*
5. **Immature IHCs with defective bundles** **abolish** mechano-electrical transduction (inferred at the human level; demonstrated functionally in mouse IHC recordings).
6. **Loss of transduction** **results in** profound congenital bilateral sensorineural hearing loss — the clinical phenotype. *(Human: [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/), [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/).)*

**Branch (developmental vs maintenance):** EPS8 drives **initial elongation** (step 3); its paralog **EPS8L2** independently drives **maintenance** of stereocilia in adult cells. Loss of EPS8 → short bundles from the outset (DFNB102, congenital). Loss of EPS8L2 → normal build-up then decay → **late-onset progressive** loss ([PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/)).

### Molecular and structural detail

**Actin capping vs bundling — separable activities.** Disanza et al. 2004 showed EPS8 caps actin barbed ends with nanomolar affinity through its conserved C-terminal effector domain, with full-length EPS8 auto-inhibited in vitro and de-repressed by Abi1 ([PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/)).

> *"proteins of another family, the Eps8 family, also show barbed-end capping activity, which resides in their conserved carboxy-terminal effector domain"* — [PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/)

Hertzog et al. 2010 resolved the structural basis: **bundling** is mediated by a compact four-helix bundle contacting three actin subunits along the filament, whereas **capping** is mediated by an amphipathic helix inserting into the hydrophobic pocket at the barbed end, blocking monomer addition; point mutations can dissociate the two activities ([PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/)).

> *"The capping activity is mainly mediated by a amphipathic helix that binds within the hydrophobic pocket at the barbed ends of actin blocking further addition of actin monomers."* — [PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/)

Because DFNB102 truncating/deletion alleles remove this **C-terminal effector domain**, both capping and bundling are lost — the mechanistic crux linking genotype to stereocilia failure.

**Tip complex context.** EPS8 is a central actin-regulatory element within the stereocilia **tip complex** together with **MyosinXVa (MYO15A)** and **whirlin (WHRN)**; Eps8-null bundles are shorter than MyoXVa- or whirlin-deficient bundles, placing EPS8 at the heart of elongation control ([PMID: 21236676](https://pubmed.ncbi.nlm.nih.gov/21236676/)).

> *"MyoXVa, whirlin, and Eps8 are integral components of the stereocilia tip complex, where Eps8 is a central actin-regulatory element for elongation of the stereocilia actin core."* — [PMID: 21236676](https://pubmed.ncbi.nlm.nih.gov/21236676/)

Krey et al. 2023 showed EPS8 protein accumulation at row-1 tips peaks at the end of developmental stage III, coinciding with row-1 lengthening, and that mechanotransduction normally restricts EPS8 to the tallest row ([PMID: 37011103](https://pubmed.ncbi.nlm.nih.gov/37011103/)).

**Broader signaling role (redundant in cochlea).** Outside hair cells, EPS8 regulates Rac-dependent actin remodeling and cell motility via the trimeric **EPS8–ABI1–SOS1** complex, participates in EGFR signaling, and can undergo chaperone-mediated autophagy in cancer cells ([PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/), [PMID: 20184880](https://pubmed.ncbi.nlm.nih.gov/20184880/), [PMID: 41974702](https://pubmed.ncbi.nlm.nih.gov/41974702/)). These functions are **not manifest as disease in humans** because paralogs compensate — hence isolated deafness.

**Molecular pathways / GO terms.** GO:0030041 (actin filament polymerization), GO:0051016 (barbed-end actin filament capping), GO:0051017 (actin filament bundle assembly), GO:0060088 (auditory receptor cell stereocilium organization), GO:0032420 (stereocilium), GO:0007605 (sensory perception of sound). Cell types (CL): CL:0000589 (cochlear inner hair cell), CL:0000601 (cochlear outer hair cell).

### ASCII mechanistic model

```
 EPS8 biallelic LoF (nonsense/splice/deletion)
        │  removes C-terminal effector domain
        ▼
 Loss of barbed-end CAPPING + actin BUNDLING at stereocilia tips
        │
        ▼
 Failed stereocilia ELONGATION → short bundles, decayed staircase
        │                                   ┌───────────────────────────┐
        ▼                                   │ Paralog division of labor: │
 IHCs fail functional MATURATION            │ EPS8  = elongation (DFNB102│
 (OHCs comparatively spared)                │ EPS8L2= maintenance →      │
        │                                   │        progressive HL)     │
        ▼                                   └───────────────────────────┘
 Loss of mechano-electrical transduction (inferred in human)
        ▼
 PROFOUND CONGENITAL BILATERAL SENSORINEURAL HEARING LOSS
```

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Inner ear — cochlea. UBERON:0001844 (cochlea), UBERON:0001846 (internal ear), UBERON:0002227 (organ of Corti / spiral organ).
- **Body system:** Auditory / sensory nervous system. No secondary organ involvement in humans (nonsyndromic).
- **Tissue / cell level:** Sensory neuroepithelium of the organ of Corti; specifically **cochlear inner hair cells** (CL:0000589) are functionally most affected, with outer hair cells (CL:0000601) comparatively spared in the knockout model ([PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/)).
- **Subcellular level:** The **stereocilium** (GO:0032420) and its **actin filament core / stereocilia tip** (GO:0032426 stereocilium tip). The defect is in the actin cytoskeleton (GO:0015629, actin cytoskeleton).
- **Localization / lateralization:** **Bilateral**, symmetric cochlear involvement (HP:0008619).

---

## 8. Temporal Development

- **Onset:** Congenital / prelingual; hearing loss is present from birth. Onset pattern is **congenital-static** rather than acquired.
- **Progression:** In DFNB102 patients the loss is congenitally profound and therefore essentially **stable/non-progressive** (there is little residual hearing to lose). This contrasts with *EPS8L2*-related deafness, which is **late-onset and progressive** because EPS8L2 governs stereocilia maintenance rather than initial construction ([PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/)).
- **Disease course / duration:** Chronic, lifelong.
- **Remission:** None spontaneously; functional hearing is restored only by intervention (cochlear implant).
- **Critical period:** The developmental window for stereocilia elongation (in mouse, up to ~postnatal day 8, stage III–IV transition; [PMID: 37011103](https://pubmed.ncbi.nlm.nih.gov/37011103/)) is when EPS8 acts. Clinically, the critical period for intervention is early infancy — early cochlear implantation optimizes language outcomes.

---

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; requires biallelic *EPS8* LoF. Carriers unaffected.
- **Penetrance:** Appears **complete** in reported biallelic individuals.
- **Expressivity:** Consistent (uniformly severe-to-profound congenital SNHL) within the small cohort.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Consanguinity:** A major contributing context — the founding family was consanguineous (Algerian); homozygous LoF alleles are enriched in consanguineous populations.
- **Founder effects:** None established; the reported variants are private to individual families across different populations.
- **Carrier frequency:** Unknown / presumed extremely low given ultrararity.

**Epidemiology.** DFNB102 is **ultrarare**: only ~5 pathogenic variants/families reported worldwide as of 2023 ([PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/), [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)). For context, nonsyndromic hearing loss overall affects ~1 in 1000 newborns and is hereditary in 60–70% of cases, with *GJB2* the most common cause ([PMID: 19939467](https://pubmed.ncbi.nlm.nih.gov/19939467/); [PMID: 10376574](https://pubmed.ncbi.nlm.nih.gov/10376574/)); *EPS8*/DFNB102 accounts for a vanishingly small fraction.

> *"Nonsyndromic hearing loss is one of the most abundant human sensory disorders, and can be found in 1 out of 1000 newborns. In 60-70% of the cases this disorder is hereditary."* — [PMID: 19939467](https://pubmed.ncbi.nlm.nih.gov/19939467/)

- **Affected populations:** Reported in Algerian, Chinese, and Iranian families — no single ethnic predilection beyond enrichment in consanguineous unions.
- **Geographic distribution:** No endemic focus; sporadic across populations.
- **Sex ratio:** No sex bias expected (autosomal); reported cases include males; sample too small for a meaningful ratio.
- **Age distribution:** Congenital onset; affects all ages once present.

---

## 10. Diagnostics

**Recommended approach.** Diagnosis is **molecular**, integrated with audiometric confirmation.

- **Audiometry / physiologic testing:** Newborn hearing screening (OAE/ABR), diagnostic ABR and behavioral audiometry confirm bilateral severe-to-profound SNHL.
- **Genetic testing (primary):**
  - **Whole-exome sequencing (WES)** identified the founding variant and is the workhorse for gene discovery/diagnosis in nonsyndromic HL ([PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)).
  - **Whole-genome sequencing (WGS)** and, critically, **copy-number/CNV analysis** are needed because **intragenic deletions can masquerade as homozygosity** — the Chinese case required CNV detection of a 65.9 kb deletion to resolve the genotype ([PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)).
  - **Hearing-loss gene panels** including *EPS8* are appropriate first-tier tests.
  - **Functional confirmation** (in vitro splicing assays, allele-specific expression) can validate splice/structural variants ([PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/)).
- **Imaging:** Temporal-bone CT/MRI is used to exclude inner-ear malformations and assess candidacy for cochlear implantation; no DFNB102-specific radiologic signature.
- **Biopsy/pathology:** Not applicable (cochlea is not biopsied clinically).

**Clinical criteria / differential diagnosis.** DFNB102 is diagnosed by the combination of nonsyndromic congenital profound SNHL and biallelic *EPS8* LoF. Differentials include the far more common *GJB2*/*GJB6* deafness ([PMID: 10376574](https://pubmed.ncbi.nlm.nih.gov/10376574/)), *SLC26A4* (Pendred/EVA), *MYO15A*, *TMC1*, *OTOF* (auditory neuropathy), and syndromic causes (Usher, Pendred, Waardenburg) — distinguished by absence of syndromic features and gene-specific findings. *EPS8L2* should be considered in **progressive** postlingual loss.

**Screening.** Newborn hearing screening detects the phenotype; **cascade/carrier testing** of relatives is appropriate once the familial variants are known. There is no population carrier-screening program specific to *EPS8*.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** DFNB102 is **not life-threatening**; life expectancy is normal. No disease-specific mortality.
- **Morbidity / function:** The principal morbidity is **communication disability** from congenital profound deafness — impaired spoken-language development, education, and social participation if untreated.
- **Disease course:** Chronic, stable (congenitally profound). No spontaneous recovery.
- **Recovery potential:** Auditory function is not restored biologically but can be substantially rehabilitated with **cochlear implantation**, particularly when performed early.
- **Prognostic factors:** Age at implantation, duration of auditory deprivation, and consistency of device use are the key determinants of language outcome after pediatric cochlear implantation ([PMID: 41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/)). Because the lesion is peripheral (hair cell/stereocilia) with an intact auditory nerve, implant candidacy and expected benefit are favorable.
- **QoL measures:** No DFNB102-specific PROMIS/EQ-5D data; general pediatric cochlear-implant literature applies.

---

## 12. Treatment

There is **no disease-specific pharmacologic or gene therapy** for DFNB102. Management is habilitative.

| Modality | Detail | NCIT suggestion |
|---|---|---|
| **Cochlear implantation** (standard of care) | For congenital bilateral severe-to-profound SNHL with limited hearing-aid benefit; effective; best outcomes with early implantation ([PMID: 41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/)) | NCIT:C15694 (Cochlear Implant) |
| **Hearing aids** | Trialed first; typically insufficient for profound loss | NCIT:C99936 (Hearing Aid) |
| **Auditory-verbal / speech-language therapy** | Rehabilitation to develop spoken language post-implant | NCIT:C15195 (Rehabilitation Therapy) |
| **Educational/communication support** | Sign language, assistive listening, early intervention services | — |

> *"Pediatric cochlear implantation is the standard of care for infants and young children with congenital bilateral severe-to-profound sensorineural hearing loss who receive limited benefits from optimally fitted hearing aids."* — [PMID: 41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/)

**Pharmacotherapy / pharmacogenomics:** None specific. **Gene therapy / RNA therapy / cell therapy:** None approved or in DFNB102-specific trials; inner-ear gene therapy is an active field for other deafness genes (e.g., *OTOF*) but not yet for *EPS8*. **Surgical:** Cochlear implant surgery as above. **Experimental:** No DFNB102-specific NCT-registered trials identified.

---

## 13. Prevention

- **Primary prevention:** Not preventable in an affected fetus (monogenic, congenital). At the family level, **genetic counseling** for consanguineous or carrier couples informs reproductive options.
- **Secondary prevention (early detection):** **Universal newborn hearing screening** enables early diagnosis and timely intervention within the critical language-development window.
- **Tertiary prevention:** Early cochlear implantation and structured auditory-verbal rehabilitation prevent the developmental complications (language/educational delay) of untreated profound deafness.
- **Genetic screening / reproductive options:** Carrier testing of at-risk relatives once familial variants are identified; prenatal testing and preimplantation genetic testing (PGT-M) are options for known-carrier couples.
- **Counseling:** Autosomal recessive recurrence risk is 25% per pregnancy for two carrier parents — a core counseling message.
- **Immunization / public health / environmental:** Not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *EPS8* is conserved across vertebrates. Mouse *Eps8* (NCBI Gene 13860; taxon *Mus musculus*, NCBI:txid10090) is the principal ortholog studied. Paralogs *Eps8l1/l2/l3* exist in mouse and human.
- **Natural disease in animals:** No well-characterized naturally occurring *EPS8* deafness is documented in companion animals or wildlife (OMIA). The animal evidence comes from **engineered** models, not spontaneous disease.
- **Comparative biology:** EPS8's actin capping/bundling role is conserved and pleiotropic across species — e.g., it contributes to intestinal microvillus morphogenesis in mouse ([PMID: 20209148](https://pubmed.ncbi.nlm.nih.gov/20209148/)) and to actin-based structures in invertebrates such as *Eriocheir sinensis* spermatogenesis ([PMID: 36709695](https://pubmed.ncbi.nlm.nih.gov/36709695/)). **Species divergence is important:** mouse *Eps8* knockouts show intestinal/metabolic phenotypes that human EPS8-null patients do not (see below).
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

The mouse is the definitive model and faithfully recapitulates the human cochlear phenotype, while also revealing species-specific pleiotropy.

| Model | Type | Key phenotype | Human relevance | Reference |
|---|---|---|---|---|
| ***Eps8*-knockout mouse** | Constitutive KO (mammalian) | Profoundly deaf; abnormally **short stereocilia**; IHCs (not OHCs) fail to mature | Faithful DFNB102 model | [PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/), [PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/) |
| ***Eps8L2*-knockout mouse** | Constitutive KO | **Late-onset progressive** hearing loss; gradual hair-bundle deterioration | Models maintenance role / progressive HL branch | [PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/) |
| ***Eps8/Eps8L2* double-null** | Combined KO | Decay of ordered staircase hair-bundle structure | Demonstrates complementary roles | [PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/) |
| ***Eps8*-KO (systemic phenotypes)** | Constitutive KO | ~25% shorter intestinal microvilli; reduced fat absorption; resistance to diet-induced obesity; improved metabolism; increased lifespan | **Not seen in human patients** — species divergence | [PMID: 20209148](https://pubmed.ncbi.nlm.nih.gov/20209148/) |

> *"whereas Eps8 is essential for the initial elongation of stereocilia, Eps8L2 is required for their maintenance in adult hair cells. In the absence of both proteins, the ordered staircase structure of the hair bundle in the cochlea decays."* — [PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/)

> *"Eps8 knockout mice are profoundly deaf and that IHCs, but not OHCs, fail to mature into fully functional sensory receptors"* — [PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/)

**Phenotype recapitulation.** Excellent for the auditory phenotype — the *Eps8*-KO mouse independently established EPS8 as an essential stereocilia elongation factor before the human gene was implicated, providing strong cross-species validation.

**Model limitations.** The mouse KO exhibits **extra-cochlear phenotypes** (intestinal microvillus shortening, favorable metabolic status, longevity) absent from human isolated deafness — likely reflecting differences in paralog compensation between species. This makes the mouse imperfect for modeling the *isolated* human presentation but valuable for dissecting EPS8's broader actin biology.

> *"knockout mice for Eps8, a regulator of actin dynamics, display reduced body weight, partial resistance to age- or diet-induced obesity, and overall improved metabolic status"* — [PMID: 20209148](https://pubmed.ncbi.nlm.nih.gov/20209148/)

**Resources:** MGI (mouse *Eps8*), IMPC; in vitro biochemistry and structural biology of EPS8 capping/bundling ([PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/), [PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/)).

---

## Key Findings (with statistical evidence)

**F1 — DFNB102 is caused by biallelic loss-of-function *EPS8* variants (12p12.3).** WES of a consanguineous Algerian family found homozygous c.88C>T (p.Gln30*) segregating recessively, absent from 120 controls and the Exome Variant Server ([PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/)); only ~5 pathogenic variants known by 2023 ([PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/)).

**F2 — EPS8 controls stereocilia elongation and IHC maturation.** *Eps8*-KO mice are profoundly deaf with short stereocilia; IHCs (not OHCs) fail to mature ([PMID: 21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/)); EPS8 sits in the MYO15A–whirlin tip complex as the central elongation regulator ([PMID: 21236676](https://pubmed.ncbi.nlm.nih.gov/21236676/)).

**F3 — Consistent clinical phenotype:** prelingual, bilateral, symmetric, severe-to-profound nonsyndromic SNHL across Algerian, Chinese (compound splice + 65.9 kb deletion; transcript loss P<0.05), and Iranian cases ([PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/), [PMID: 36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/)).

**F4 — Faithful mouse models; EPS8 vs EPS8L2 divide developmental vs maintenance roles** ([PMID: 23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/), [PMID: 37011103](https://pubmed.ncbi.nlm.nih.gov/37011103/)).

**F5 — EPS8 is a multifunctional EGFR-pathway actin regulator with a non-redundant cochlear role** — broad expression yet isolated deafness implies paralog redundancy elsewhere ([PMID: 24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/), [PMID: 41974702](https://pubmed.ncbi.nlm.nih.gov/41974702/)).

**F6 — Ultrarare; diagnosed by WES/WGS + CNV analysis; managed by cochlear implantation** ([PMID: 19939467](https://pubmed.ncbi.nlm.nih.gov/19939467/), [PMID: 41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/)).

**F7 — Mouse-specific intestinal/metabolic phenotype absent in humans** (~25% shorter microvilli, improved metabolism; [PMID: 20209148](https://pubmed.ncbi.nlm.nih.gov/20209148/)).

**F8 — Separable capping and bundling encoded by the C-terminal effector domain, both required and both lost by truncating alleles** ([PMID: 15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/), [PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/)).

---

## Evidence Base

| PMID | How it supports the findings |
|---|---|
| [24741995](https://pubmed.ncbi.nlm.nih.gov/24741995/) | Founding paper: EPS8 = DFNB102 gene; c.88C>T; defines EPS8 as F-actin capping/bundling protein |
| [34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/) | Compound splice variant + 65.9 kb intragenic deletion; congenital profound nonsyndromic HL; CNV diagnostics |
| [36635257](https://pubmed.ncbi.nlm.nih.gov/36635257/) | Fifth pathogenic variant (Iranian); confirms rarity |
| [21526224](https://pubmed.ncbi.nlm.nih.gov/21526224/) | *Eps8*-KO mouse: profound deafness, short stereocilia, IHC maturation failure |
| [21236676](https://pubmed.ncbi.nlm.nih.gov/21236676/) | EPS8 central in MYO15A–whirlin tip complex for actin-core elongation |
| [23918390](https://pubmed.ncbi.nlm.nih.gov/23918390/) | EPS8L2 maintenance role; double-null staircase decay; progressive HL branch |
| [37011103](https://pubmed.ncbi.nlm.nih.gov/37011103/) | EPS8 timing at stereocilia tips; transduction restricts EPS8 to tallest row |
| [15558031](https://pubmed.ncbi.nlm.nih.gov/15558031/) | Barbed-end capping resides in C-terminal effector domain; Abi1 de-repression; Rac via EPS8–Abi1–Sos1 |
| [20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/) | Structural basis: helix-bundle bundling vs amphipathic-helix capping; separable activities |
| [20209148](https://pubmed.ncbi.nlm.nih.gov/20209148/) | Mouse intestinal/metabolic phenotype (species divergence) |
| [41974702](https://pubmed.ncbi.nlm.nih.gov/41974702/) | EPS8–ABI1 complexes in non-cochlear actin remodeling |
| [41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/) | Cochlear implantation as standard of care |
| [19939467](https://pubmed.ncbi.nlm.nih.gov/19939467/), [10376574](https://pubmed.ncbi.nlm.nih.gov/10376574/) | Epidemiologic context for nonsyndromic HL and *GJB2* differential |

**Evidence-type mix:** Human clinical genetics (24741995, 34637946, 36635257); model organism (21526224, 21236676, 23918390, 37011103, 20209148); in vitro/structural biochemistry (15558031, 20532239); clinical management (41895171).

---

## Limitations and Knowledge Gaps

1. **Tiny cohort.** Fewer than ~5 families worldwide. Estimates of penetrance, expressivity, sex ratio, and full phenotypic range (e.g., subtle vestibular involvement) are consequently uncertain.
2. **No human histopathology.** The stereocilia/IHC mechanism is proven in mouse; the human cellular lesion is inferred, not directly demonstrated.
3. **No missense-variant genotype–phenotype data.** All reported alleles are truncating/deletion; whether hypomorphic missense alleles could cause milder or progressive loss is unknown.
4. **Species divergence.** Mouse KO extra-cochlear phenotypes (intestinal, metabolic, longevity) complicate translation and are unexplained in terms of human paralog compensation.
5. **No natural animal disease** and **no DFNB102-specific therapeutics** (no gene/RNA therapy trials).
6. **No population carrier-frequency data** for *EPS8* LoF alleles.
7. **Non-specific ICD/MeSH coding** limits registry-based epidemiology.

---

## Proposed Follow-up Experiments / Actions

1. **International case aggregation** (e.g., GeneMatcher, deafness gene registries) to expand the DFNB102 cohort, refine phenotype (including vestibular testing), and estimate penetrance/expressivity.
2. **gnomAD LoF audit** of *EPS8* to estimate carrier frequency and predicted disease incidence, and to check for any biallelic LoF individuals without reported deafness (redundancy test).
3. **Functional classification pipeline** for candidate *EPS8* missense/splice VUS (minigene splicing assays, allele-specific expression) to enable confident clinical reporting — extending the approach validated in [PMID: 34637946](https://pubmed.ncbi.nlm.nih.gov/34637946/).
4. **Human iPSC-derived inner-ear organoids** carrying DFNB102 alleles to directly test stereocilia elongation and transduction in a human cellular context, closing the human-histopathology gap.
5. **Structure-guided rescue experiments** using capping-only vs bundling-only EPS8 constructs ([PMID: 20532239](https://pubmed.ncbi.nlm.nih.gov/20532239/)) in *Eps8*-null hair cells to determine which activity is limiting for stereocilia elongation — informing future gene-therapy payload design.
6. **Cochlear-targeted gene-replacement proof-of-concept** (AAV-*EPS8*) in the *Eps8*-KO mouse during the neonatal critical window ([PMID: 37011103](https://pubmed.ncbi.nlm.nih.gov/37011103/)) to test biological rescue.
7. **Cochlear-implant outcome tracking** specifically in genetically confirmed DFNB102 patients, contributing to etiology-driven implant management ([PMID: 41895171](https://pubmed.ncbi.nlm.nih.gov/41895171/)).

---

*Report compiled from 8 confirmed findings and 27 reviewed papers across a 5-iteration autonomous investigation. Evidence sources are labeled by type (human clinical, model organism, in vitro/structural, clinical management). Ontology suggestions: MONDO:0014428; HGNC:3555 (EPS8); UBERON:0001844 (cochlea), UBERON:0002227 (organ of Corti); CL:0000589 (cochlear inner hair cell), CL:0000601 (cochlear outer hair cell); GO:0051016 (barbed-end actin filament capping), GO:0051017 (actin filament bundle assembly), GO:0060088 (auditory receptor cell stereocilium organization), GO:0032420 (stereocilium); NCIT:C15694 (Cochlear Implant).*


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_102-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_102-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
| Terms checked | 24 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014428` (3 mentions) - the report calls it "MONDO"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 102**
- `HP:0008619` (2 mentions) - the report calls it "Bilateral SNHL", "Localization / lateralization:** **Bilateral**, symmetric cochlear involvement"; HP calls it **Bilateral sensorineural hearing impairment**
- `NCIT:C15694` (2 mentions) - the report calls it "Cochlear Implant"; NCIT calls it **Phase II/III Trial**
- `NCIT:C99936` (1 mention) - the report calls it "Hearing Aid"; NCIT calls it **Catecholaminergic Polymorphic Ventricular Tachycardia by ECG Finding**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032420` (3 mentions) - the report calls it "stereocilium", "Subcellular level:** The **stereocilium"; GO calls it **stereocilium**
- `UBERON:0002227` (2 mentions) - the report calls it "organ of Corti / spiral organ", "organ of Corti"; UBERON calls it **spiral organ of cochlea**, and lists "spiral organ of Corti" among its other names
- `NCIT:C15195` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Brachytherapy**, and lists "Radiation Brachytherapy" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0008619` - called "Bilateral SNHL", "Localization / lateralization:** **Bilateral**, symmetric cochlear involvement"
- `GO:0032420` - called "stereocilium", "Subcellular level:** The **stereocilium"
- `CL:0000589` - called "cochlear inner hair cell", "cochlear inner hair cells"
- `UBERON:0002227` - called "organ of Corti / spiral organ", "organ of Corti"