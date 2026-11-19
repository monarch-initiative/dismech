---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T04:15:48.924777'
end_time: '2026-09-30T04:52:47.615654'
duration_seconds: 2218.69
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ureaplasma Urethritis
  mondo_id: MONDO:0007007
  category: Infectious Disease
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
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 14
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40247169
  relevance_assessed: 31
  on_topic: 23
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 9
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0025401
    reported_labels:
    - abnormal urethral discharge
    ontology_label: Staring gaze
  - term_id: HP:0032263
    reported_labels:
    - abnormal inflammatory marker
    ontology_label: Increased blood pressure
  - term_id: NCIT:C692
    reported_labels:
    - Doxycycline
    ontology_label: Nimodipine
  - term_id: NCIT:C1662
    reported_labels:
    - Azithromycin
    ontology_label: Indinavir Sulfate
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ureaplasma_Urethritis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ureaplasma_Urethritis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ureaplasma Urethritis
- **MONDO ID:** MONDO:0007007 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Ureaplasma Urethritis** covering all of the
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

# Ureaplasma Urethritis — Comprehensive Disease Characteristics Report

**Disease:** Ureaplasma Urethritis
**MONDO ID:** MONDO:0007007
**Category:** Infectious Disease (sexually transmitted, non-gonococcal urethritis)
**Investigation:** 5 iterations · 11 confirmed findings · 53 papers reviewed
**Evidence base:** Literature synthesis (PubMed) — predominantly human clinical/epidemiological studies, plus in vitro biochemistry, comparative genomics, and veterinary/natural-disease reports. No patient-level dataset was provided; this is an aggregated disease-level report.

---

## Summary

**Ureaplasma urethritis** is a form of **non-gonococcal urethritis (NGU)** caused by *Ureaplasma* species — cell-wall-less bacteria (class Mollicutes) that colonize the human urogenital tract. The disease is best understood as an **infectious, non-genetic, behaviorally acquired sexually transmitted infection (STI)** of predominantly young adult men. Crucially, of the two human *Ureaplasma* species, it is **_Ureaplasma urealyticum_ (biovar 2)** — not the more common commensal *U. parvum* (biovar 1) — that carries the urethritis-associated pathogenic potential, and this pathogenicity is **load-dependent**: the organism behaves as a **conditional pathogen** that can also be carried asymptomatically. In a large Chinese cohort of 1,249 NGU patients, single *U. urealyticum* infection was the single most common identifiable cause at **40.59%**, exceeding *Chlamydia trachomatis* and *Mycoplasma genitalium* ([PMID: 40497611](https://pubmed.ncbi.nlm.nih.gov/40497611/)).

Mechanistically, *Ureaplasma* adheres to the urethral epithelium and deploys a conserved triad of virulence factors: its hallmark **urease** hydrolyzes urea to generate ATP and cytotoxic **ammonia**; a secreted, species-specific **IgA1 protease** cleaves human IgA1 at the hinge region (Pro235–Thr236), disabling the dominant mucosal antibody; and the phase-variable **Multiple Banded Antigen (MBA)** enables antigenic variation and immune evasion. Together these provoke a **neutrophilic (polymorphonuclear) inflammatory response** that manifests as mild-to-moderate urethral discharge, dysuria, and urethral discomfort — often scant/mucoid and frequently asymptomatic. The clinical phenotype is non-specific and cannot be distinguished from other NGU causes without laboratory testing.

Diagnosis is a **two-step process**: syndromic confirmation of urethritis (≥5 PMN/high-power field on urethral smear, with exclusion of *N. gonorrhoeae*) plus **species-specific molecular detection** by multiplex NAAT/real-time PCR on first-void urine or urethral swab. Prognosis is **excellent**: first-line doxycycline or azithromycin achieves ~76–81% clinical cure, though cure rates are moderate and declining, and regional fluoroquinolone/tetracycline resistance is rising. Untreated or persistent infection can cause epididymitis, prostatitis, and reduced semen quality/male-factor infertility. A conserved natural analog disease exists in cattle (*Ureaplasma diversum* granular vulvovaginitis), underscoring the evolutionary conservation of the urease/IgA-protease pathogenic mechanism. No human causal genes, inheritance pattern, vaccine, or genetic screening apply to this disease.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Ureaplasma urethritis is inflammation of the male (and, less commonly female) urethra attributable to *Ureaplasma* species within the broader clinical syndrome of non-gonococcal urethritis. NGU "is characterized by discharge, dysuria and/or urethral discomfort but may be asymptomatic," and diagnosis "is confirmed by demonstrating an excess of polymorpho-nuclear leucocytes (PMNLs) in a stained smear" ([PMID: 26220178](https://pubmed.ncbi.nlm.nih.gov/26220178/)).

**Key identifiers.**
- **MONDO:** MONDO:0007007 (Ureaplasma urethritis)
- **MeSH:** Ureaplasma Infections; Urethritis
- **ICD-10:** A63.8 / N34.1 (nonspecific urethritis); **ICD-11:** 1A9Y / GC02
- **Causative organism (NCBI Taxonomy):** *Ureaplasma urealyticum* txid2130; genus *Ureaplasma* txid2129
- **OMIM / Orphanet:** Not applicable — an acquired infectious disease with no Mendelian genetic basis.

**Synonyms / alternative names.** Ureaplasma-associated non-gonococcal urethritis; ureaplasmal urethritis; nonspecific urethritis (in part); a subtype of NGU. Historically part of "T-strain mycoplasma" infection.

**Information source.** Derived from **aggregated disease-level resources** — case-control studies, quantitative PCR cohorts, clinical trials, and microbiological surveillance — rather than individual EHR/patient-level records.

---

### 2. Etiology

**Causal factor — infectious.** The primary cause is infection with *Ureaplasma urealyticum* (biovar 2). A defining finding of this investigation is the **species distinction**: *U. urealyticum* biovar 2, not *U. parvum* biovar 1, is the urethritis-associated species, and its pathogenicity is **load-dependent**.

- Povlsen et al. (2002, n=340): "*Ureaplasma urealyticum* biovar 2 was detected more often among patients with NGU than among those without (P=0.012)" ([PMID: 11939406](https://pubmed.ncbi.nlm.nih.gov/11939406/)).
- Yoshida/Deguchi et al. (2007): "*U. urealyticum* (biovar 2) loads in 23 men with NMNCNGU were significantly higher than those in 14 men without urethritis. However, *U. parvum* (biovar 1) loads did not differ significantly" ([PMID: 17522569](https://pubmed.ncbi.nlm.nih.gov/17522569/)).
- Counterpoint (conditional pathogen): Jordan et al. (2020): "UU monoinfection was not associated with NGU and was almost twice as prevalent in controls" ([PMID: 31515293](https://pubmed.ncbi.nlm.nih.gov/31515293/)).

**Genetic risk factors.** **None established.** The human host is immunologically normal; there is no known causal variant, susceptibility locus, or modifier gene. This is an environmentally/behaviorally acquired infection.

**Environmental / behavioral risk factors.** Risk mirrors other STIs: young age, multiple or new sexual partners, unprotected intercourse, higher coital frequency, and prior STI. In 2,668 men, *U. urealyticum* positivity (24.7%) was independently associated with **smoking (OR 1.23, 95% CI 1.02–1.49, P=0.03)** and **sexual frequency >2×/week (OR 1.41, 95% CI 1.04–1.91, P=0.03)** ([PMID: 41665055](https://pubmed.ncbi.nlm.nih.gov/41665055/)). Unprotected sexual contact was reported by 67.0% of a symptomatic urogenital series ([PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)).

**Protective factors.** Barrier contraception (condoms), sexual-partner reduction, and partner treatment. No genetic protective variant is described.

**Gene–environment interactions.** Not applicable — no host genetic component is implicated.

---

### 3. Phenotypes

The clinical phenotype is that of urethritis and is **mild and non-specific**.

| Phenotype | Type | HPO suggestion | Frequency | Characteristics |
|-----------|------|----------------|-----------|-----------------|
| Urethral discharge (often scant/mucoid) | Clinical sign | HP:0025401 (abnormal urethral discharge) | ~86% of symptomatic men | Adult-onset; mild–moderate |
| Dysuria | Symptom | HP:0100518 (dysuria) | ~88% | Adult-onset; mild–moderate; may fluctuate |
| Urethral discomfort/itch | Symptom | — | Common | Mild |
| Asymptomatic carriage | — | — | Substantial fraction | Load-dependent |
| Urethral PMN excess (≥5/HPF) | Laboratory abnormality | HP:0032263 (abnormal inflammatory marker) | Diagnostic criterion | Objective sign |

- Symptom frequencies: "Dysuria was reported in 88% cases" and urethral discharge in ~86% of symptomatic men ([PMID: 33423450](https://pubmed.ncbi.nlm.nih.gov/33423450/); median age ~33 years).
- Definition/diagnosis: "Urethritis is characterized by discharge, dysuria and/or urethral discomfort but may be asymptomatic... confirmed by demonstrating an excess of polymorpho-nuclear leucocytes (PMNLs)" ([PMID: 26220178](https://pubmed.ncbi.nlm.nih.gov/26220178/)).
- Non-specificity: "No individual sign or symptom accurately predicted the infectious etiology" ([PMID: 32149960](https://pubmed.ncbi.nlm.nih.gov/32149960/)) — Ureaplasma urethritis cannot be clinically distinguished from chlamydial, mycoplasmal, or other NGU.

**Onset/severity/progression.** Adult-onset (sexually active adults); mild-to-moderate severity; discharge tends to be scant/mucoid rather than the copious purulence of gonorrhea; course is often episodic and typically self-limited with treatment.

**Quality-of-life impact.** Generally modest — discomfort, anxiety, and interference with sexual activity during symptomatic periods; larger QoL impact stems from complications (infertility concerns, chronic prostatitis/pain).

---

### 4. Genetic/Molecular Information

**No human causal genes, pathogenic variants, modifier genes, epigenetic changes, or chromosomal abnormalities apply** — this is an infectious, not a Mendelian/genomic, disease. Molecular information instead concerns the **pathogen genome**:

- Genomes are small: *U. parvum* 0.75–0.78 Mbp; *U. urealyticum* 0.84–0.95 Mbp; 14 serovars total (10 *U. urealyticum* [UUR], 4 *U. parvum* [UPA]) ([PMID: 22646228](https://pubmed.ncbi.nlm.nih.gov/22646228/)).
- Key pathogen virulence loci: **urease gene cluster**; **IgA1 protease gene** (species-specific serine protease); **mba (Multiple Banded Antigen) gene superfamily** — "the mba gene was part of a large superfamily, which is a phase variable gene system" ([PMID: 22646228](https://pubmed.ncbi.nlm.nih.gov/22646228/)).
- Antibiotic-resistance determinants (pathogen): **tet(M)** ribosomal-protection element (tetracycline resistance); **23S rRNA / L4 ribosomal protein** changes (macrolide resistance, e.g., R66/Q67 deletion in L4); **ParC D82N** (fluoroquinolone resistance) ([PMID: 19273669](https://pubmed.ncbi.nlm.nih.gov/19273669/)).

---

### 5. Environmental Information

- **Environmental/occupational toxins:** None causally implicated.
- **Lifestyle factors:** Smoking and high sexual frequency are statistically associated risk factors ([PMID: 41665055](https://pubmed.ncbi.nlm.nih.gov/41665055/)); unprotected sexual contact is the dominant exposure ([PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)).
- **Infectious agent:** *Ureaplasma urealyticum* (biovar 2), NCBI txid2130 — a cell-wall-less mollicute. *U. parvum* (biovar 1) is generally a commensal in this context. Coinfection with *Chlamydia trachomatis* and *Mycoplasma genitalium* is common and can amplify disease (e.g., 3.64-fold increased postgonococcal urethritis risk with UU biovar 2 coinfection, [PMID: 17806051](https://pubmed.ncbi.nlm.nih.gov/17806051/)).

---

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical manifestation):**

1. Sexual transmission delivers *U. urealyticum* biovar 2 to the male urethral mucosa **→ leads to** attachment.
2. Surface adhesins mediate **adhesion to urethral epithelial cells** **→ results in** stable colonization (load-dependent; below a threshold, asymptomatic carriage).
3. Colonized organisms express **urease**, which **hydrolyzes urea → generates ATP + releases ammonia (NH₃)** **→ leads to** local cytotoxic/irritant injury of the mucosal epithelium (*inferred* from the organism's metabolic dependence on urea and ammonia toxicity).
4. In parallel, the organism secretes a **species-specific IgA1 protease** that **cleaves human IgA1 at the hinge (Pro235–Thr236) into intact Fab/Fc fragments** **→ results in** degradation of the dominant mucosal antibody and **immune evasion** ([PMID: 1587621](https://pubmed.ncbi.nlm.nih.gov/1587621/)).
5. Concurrently, the **phase-variable MBA gene superfamily** varies the immunodominant surface antigen **→ results in** evasion of adaptive immunity and persistence ([PMID: 22646228](https://pubmed.ncbi.nlm.nih.gov/22646228/)).
6. Epithelial irritation + immune evasion **→ leads to** recruitment and activation of **neutrophils (polymorphonuclear leukocytes)** into the urethral mucosa (branch: seminal leukocytosis, elevated IL-6 and elastase in genital-tract infection).
7. Neutrophilic inflammation **→ results in** the clinical urethritis phenotype: discharge, dysuria, PMN excess.
8. **Branch (complications):** ascending or persistent infection **→ leads to** epididymitis, prostatitis, reactive arthritis (rare), and, via seminal inflammation/oxidative injury, **impaired semen quality and sperm DNA damage**.

**Supporting molecular detail.**
- **IgA1 protease:** "*Ureaplasma urealyticum* strains of all serotypes express a specific human immunoglobulin A1 protease that cleaves immunoglobulin A1 to produce intact Fab and Fc fragments"; "the enzyme cleaves between the proline and threonine residues 235 and 236 in the hinge region of the heavy chain" ([PMID: 1587621](https://pubmed.ncbi.nlm.nih.gov/1587621/)). This activity is host-IgA-specific and, among mycoplasmas, exclusive to *U. urealyticum* ([PMID: 6392177](https://pubmed.ncbi.nlm.nih.gov/6392177/)); "IgA proteases produced by pathogenic bacteria are considered potential virulence factors for organisms that cause disease or gain entry at mucous membranes" ([PMID: 3882564](https://pubmed.ncbi.nlm.nih.gov/3882564/)).
- **Seminal inflammation (mechanistic):** UU-positive men had increased seminal plasma **elastase (p=0.0006)**, increased sperm morphology abnormality (p<0.0001), and higher DNA fragmentation ([PMID: 41217668](https://pubmed.ncbi.nlm.nih.gov/41217668/)).

**GO / CL / CHEBI term suggestions:**
- Biological processes: GO:0006508 (proteolysis, IgA1 cleavage); GO:0043419 (urea catabolic process); GO:0006954 (inflammatory response); GO:0009405 (pathogenesis).
- Cell types: CL:0000775 (neutrophil); CL:0000066 (epithelial cell); CL:0002251 (epithelial cell of urethra, approx.).
- Chemical entities: CHEBI:16134 (ammonia); CHEBI:16199 (urea); CHEBI:15422 (ATP).

**Molecular pathways.** Host — innate NF-κB / inflammatory cytokine signaling (IL-6, IL-8-driven neutrophil chemotaxis). Pathogen — urease/nitrogen metabolism generating ATP and ammonia. No canonical Wnt/MAPK/mTOR oncogenic pathway is involved.

---

### 7. Anatomical Structures Affected

**Organ level (primary):** Male **urethra** (UBERON:0000057). **Secondary/complication:** epididymis (UBERON:0001301), prostate gland (UBERON:0002367); in reactive arthritis, joints. Body system: **genitourinary / reproductive system** (UBERON:0000990).

**Tissue and cell level:** Urethral **epithelium** (epithelial tissue); infiltrating **neutrophils/PMNs** (CL:0000775). Seminal leukocytes in genital-tract involvement.

**Subcellular level:** Ureaplasma is a cell-wall-less mollicute residing extracellularly at the epithelial surface; host injury involves the plasma membrane and, via ammonia and inflammatory mediators, cytoplasmic stress. No specific organelle target (mitochondria/ER) is defined for host cells.

**Localization / lateralization:** Anterior urethra; a single midline organ, so laterality is not applicable. Complications such as epididymitis may be unilateral or bilateral.

---

### 8. Temporal Development

- **Onset:** Adult-onset in sexually active individuals; **acute to subacute** following exposure. Incubation is variable and often longer/more insidious than gonorrhea.
- **Progression:** Usually **self-limited or episodic**; mild and non-progressive in most. Can become **persistent/recurrent**, particularly with coinfection or inadequate treatment/adherence.
- **Disease course pattern:** Episodic; responds to therapy. Chronic sequelae (prostatitis, infertility) represent a downstream branch.
- **Remission:** Treatment-induced remission is the norm (~76–81% cure); spontaneous clearance of carriage also occurs.
- **Critical period for intervention:** Prompt syndromic treatment plus partner treatment during the symptomatic window prevents complications and reinfection.

---

### 9. Inheritance and Population

**Epidemiology.** Ureaplasma is a **leading identifiable cause of NGU**. In a large Chinese cohort (n=1,249 NGU): "Among the patients with NGU, UU was the most common cause (40.59%; 507/1,249)"; "81.67% (1,020/1,249) of patients with NGU were men... Coinfections... mainly comprised UU and CT" (13.05%); idiopathic NGU 28.26%; mean age 31 years ([PMID: 40497611](https://pubmed.ncbi.nlm.nih.gov/40497611/)). In a Turkish series of symptomatic urogenital patients, "*Ureaplasma* spp. were detected in 92.6% of [mollicute-positive] cases... median age was 29 years," 69% male ([PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)).

**Inheritance / penetrance / genetics.** **Not applicable** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency, because there is no host genetic etiology.

**Population demographics.** Predominantly **young adult men** (male predominance ~70–82%); global distribution with high prevalence reported in China and elsewhere. No ethnic-specific genetic predisposition. Sex ratio skews male in the urethritis presentation (women more often have cervicitis/asymptomatic carriage). Geographic variation is driven by sexual-behavior epidemiology and by regional antimicrobial-resistance patterns, not by pathogen genetics.

---

### 10. Diagnostics

**Two-step diagnostic approach:**

1. **Confirm urethritis:** ≥5 PMN/high-power field on Gram-stained urethral smear (or ≥10 PMN/HPF on first-void urine sediment), and **exclude *N. gonorrhoeae*** ([PMID: 26220178](https://pubmed.ncbi.nlm.nih.gov/26220178/)).
2. **Identify *Ureaplasma*** by nucleic acid amplification (NAAT):
   - Modern **high-throughput multiplex real-time PCR** detects *M. hominis* and *Ureaplasma* (parvum and urealyticum) in urine/genital swab with rapid turnaround: "Current culture-based methods... turnaround time between 1 and 2 weeks. We developed a high-throughput, real-time multiplex PCR assay for the rapid detection of *M. hominis* and *Ureaplasma* species" ([PMID: 37683891](https://pubmed.ncbi.nlm.nih.gov/37683891/)) — ~4–5 h and ~96% agreement vs culture.
   - **Multiplex STI panels** detect *U. urealyticum* alongside CT/NG/MG/TV/HSV with high sensitivity: 98% for genital Ureaplasma ([PMID: 21392925](https://pubmed.ncbi.nlm.nih.gov/21392925/)); a FilmArray panel detected "*U. urealyticum* in 36 (12%)" among differential-diagnosis pathogens ([PMID: 26538551](https://pubmed.ncbi.nlm.nih.gov/26538551/)).
   - **Quantitative real-time PCR** distinguishing *U. urealyticum* biovar 2 from *U. parvum* and estimating organism **load** improves clinical relevance, given load-dependent pathogenicity ([PMID: 17522569](https://pubmed.ncbi.nlm.nih.gov/17522569/)).

**Biomarkers:** Urethral/seminal PMN excess; seminal elastase and IL-6 in genital-tract involvement ([PMID: 41217668](https://pubmed.ncbi.nlm.nih.gov/41217668/)). **Imaging/electrophysiology/biopsy:** Not routinely applicable. **Genetic testing / karyotyping / CMA / omics diagnostics:** Not applicable (infectious disease). **Differential diagnosis:** *C. trachomatis*, *M. genitalium*, *N. gonorrhoeae*, *T. vaginalis*, HSV, and adenovirus.

---

### 11. Outcome/Prognosis

**Excellent prognosis.** Ureaplasma urethritis is not life-threatening; **mortality is essentially nil** and there is no impact on life expectancy. Morbidity relates to symptoms and, in a minority, complications.

**Treatment response (cure surrogate):** Randomized double-blind trial (Manhart 2013, n=606): clinical cure **80% (95% CI 74–85) azithromycin** vs **76% (95% CI 70–82) doxycycline** (P=0.40) ([PMID: 23223595](https://pubmed.ncbi.nlm.nih.gov/23223595/)); Stamm 1995 cumulative cure 81% for the NGU syndrome ([PMID: 7629982](https://pubmed.ncbi.nlm.nih.gov/7629982/)). Toh 2022: clinical cure was **100% for UU** with azithromycin, and clinical cure accurately predicted microbiological cure for UU (unlike *M. genitalium*) ([PMID: 34618416](https://pubmed.ncbi.nlm.nih.gov/34618416/)).

**Complications (morbidity branch):** epididymitis, chronic prostatitis ([PMID: 16340190](https://pubmed.ncbi.nlm.nih.gov/16340190/)), rare reactive arthritis, and **reduced semen quality/male-factor infertility**. Meta-analysis: "*U. urealyticum* significantly reduced ejaculate volume (SMD 0.33 [95% CI: 0.15, 0.52] p = 0.0004), sperm concentration (SMD 0.47 [95% CI: 0.31, 0.64] p < 0.00001), total sperm motility (SMD 0.73 [95% CI: 0.43, 1.02] p < 0.00001)" ([PMID: 40247169](https://pubmed.ncbi.nlm.nih.gov/40247169/)); WHO attributes ~15% of male infertility to genital-tract infection, with UU among the most frequent seminal-tract pathogens ([PMID: 41500460](https://pubmed.ncbi.nlm.nih.gov/41500460/)). Notably, IVF outcomes appear largely unaffected despite elevated anti-sperm antibodies ([PMID: 39629051](https://pubmed.ncbi.nlm.nih.gov/39629051/)).

**Prognostic factors:** treatment adherence (imperfect doxycycline adherence → microbiologic failure for UU-2, aRR 3.08, 95% CI 1.31–7.26; [PMID: 24106340](https://pubmed.ncbi.nlm.nih.gov/24106340/)), organism load, coinfection, and local antimicrobial resistance.

---

### 12. Treatment

**First-line pharmacotherapy** (NCIT suggestions in brackets):
- **Doxycycline** 100 mg PO BID ×7 days [NCIT:C692 — Doxycycline] — tetracycline class.
- **Azithromycin** 1 g PO single dose [NCIT:C1662 — Azithromycin] — macrolide.
- Both achieve ~76–81% clinical cure with no significant difference ([PMID: 23223595](https://pubmed.ncbi.nlm.nih.gov/23223595/)); azithromycin achieved 100% UU clinical cure in one cohort ([PMID: 34618416](https://pubmed.ncbi.nlm.nih.gov/34618416/)).

**Susceptibility profile.** *Ureaplasma* is susceptible to **tetracyclines, macrolides, and fluoroquinolones**; being cell-wall-deficient, it is **intrinsically resistant to beta-lactams, glycopeptides, sulfonamides, and trimethoprim** ([PMID: 19273669](https://pubmed.ncbi.nlm.nih.gov/19273669/)). Alternative/second-line: **fluoroquinolones** (e.g., moxifloxacin, levofloxacin) where susceptible; **josamycin** (96.1% susceptibility regionally, [PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)).

**Resistance considerations.** Currently uncommon overall — Beeton 2009: "one (1.6%) was resistant to erythromycin (MIC, >64 mg/liter) and clarithromycin (MIC, 4 mg/liter), one to ciprofloxacin (1.6%), and one to tetracycline/doxycycline (1.6%)"; "the tetM genetic element was detected in the tetracycline-resistant clinical isolate" ([PMID: 19273669](https://pubmed.ncbi.nlm.nih.gov/19273669/)) — but **rising regionally**: ciprofloxacin resistance 79.3% in one Turkish surveillance ([PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)). tet(M) can be silent in phenotypically susceptible isolates.

**Combination/strategy.** Concurrent **partner treatment** to prevent reinfection; adherence support; retreatment for persistent symptoms. **Advanced therapeutics** (gene, cell, RNA, targeted, immuno-therapies): Not applicable. **Surgical/rehabilitative:** Not applicable except for managing complications. **Pharmacogenomics:** Not applicable.

---

### 13. Prevention

- **Primary prevention:** Barrier protection (condoms), partner reduction, and behavioral counseling. Condom use-effectiveness against NGU is limited by pre-application exposure ([PMID: 2554516](https://pubmed.ncbi.nlm.nih.gov/2554516/)) — proper/consistent use is emphasized.
- **Secondary prevention:** Prompt syndromic diagnosis and treatment; **partner notification and concurrent partner treatment** to prevent reinfection.
- **Tertiary prevention:** Treating persistent infection to prevent epididymitis/prostatitis/infertility.
- **Antimicrobial stewardship:** Increasingly central given rising fluoroquinolone resistance ([PMID: 42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/)) — avoid unnecessary empiric antibiotics; guide therapy by local susceptibility.
- **Immunization:** **No vaccine exists.**
- **Genetic screening / counseling:** Not applicable (no heritable component).

---

### 14. Other Species / Natural Disease

A **conserved natural analog disease** exists in cattle. *Ureaplasma diversum* (NCBI Taxon 42094) causes bovine genital disease: "*Ureaplasma diversum* has been associated with various reproductive problems in cattle, including granular vulvovaginitis, endometritis, salpingitis, early embryonic death, weak calves, decreased conception rates, balanoprosthitis, impaired spermatozoids and seminal vesiculitis in bulls" ([PMID: 22731950](https://pubmed.ncbi.nlm.nih.gov/22731950/)).

- **Prevalence (bovine):** e.g., "Mollicutes and U. diversum were detected in 45.4% (178/392) and 21.7% (85/392) of the samples, respectively, with a herd-level prevalence of 88.8%" ([PMID: 42113363](https://pubmed.ncbi.nlm.nih.gov/42113363/)).
- **Conserved mechanism:** Histopathology of naturally infected Nellore heifers "showed leukocytes infiltration and destruction and/or necrosis of epithelium" ([PMID: 29236848](https://pubmed.ncbi.nlm.nih.gov/29236848/)) — the same neutrophilic epithelial-injury mechanism seen in humans. *U. diversum* expresses an even more potent, broadly-degrading IgA protease than human ureaplasmas ([PMID: 6392177](https://pubmed.ncbi.nlm.nih.gov/6392177/)).
- **Veterinary relevance:** Significant reproductive/economic impact in cattle; part of a Mollicutes differential (with *M. bovis*, *M. bovigenitalium*).
- **Zoonotic potential:** Not established — human and bovine Ureaplasma species are host-adapted and distinct.

**NCBI Taxon suggestions:** *Ureaplasma urealyticum* txid2130 (human); *Ureaplasma diversum* txid42094 (cattle); *Bos taurus* txid9913.

---

### 15. Model Organisms

- **Natural/large-animal model:** **Cattle** infected with *U. diversum* provide a naturally occurring model of ureaplasmal genital disease with documented histopathology ([PMID: 22731950](https://pubmed.ncbi.nlm.nih.gov/22731950/); [PMID: 29236848](https://pubmed.ncbi.nlm.nih.gov/29236848/)).
- **In vitro:** Clinical isolates and 14 reference serovars are cultured for pathogenicity, antibiotic-susceptibility (MIC), and comparative-genomics studies ([PMID: 19273669](https://pubmed.ncbi.nlm.nih.gov/19273669/); [PMID: 22646228](https://pubmed.ncbi.nlm.nih.gov/22646228/)).
- **Genetic/rodent knockouts:** No standard mouse/rat/zebrafish transgenic disease model is established for Ureaplasma urethritis (the pathogen, not the host, carries the relevant genetics).
- **Phenotype recapitulation:** The bovine natural model faithfully recapitulates neutrophilic epithelial injury and IgA-protease-mediated mucosal virulence; **limitation** — it models female genital/reproductive disease more than male urethritis, and host immune context differs.
- **Applications:** Virulence-factor characterization (urease, IgA1 protease, MBA phase variation), antimicrobial susceptibility, and vaccine-target discovery.

---

## Mechanistic Model / Interpretation

```
   Sexual transmission of U. urealyticum biovar 2 (load-dependent)
                              │
                              ▼
        Adhesion to urethral epithelium (surface adhesins)
                              │
        ┌─────────────────────┼─────────────────────────┐
        ▼                     ▼                           ▼
   UREASE →              IgA1 PROTEASE →            MBA phase variation
   urea → NH3 + ATP      cleaves IgA1 hinge         (antigenic variation)
   (epithelial           (Pro235–Thr236)            → adaptive immune
    cytotoxicity)        → mucosal antibody           evasion, persistence
        │                  degradation, evasion              │
        └─────────────────────┬───────────────────────────┘
                              ▼
            Neutrophil (PMN) recruitment & activation
                              │
                              ▼
         URETHRITIS: discharge, dysuria, PMN excess (≥5/HPF)
                              │
                              ▼ (persistent / ascending — branch)
     Epididymitis · Prostatitis · Reduced semen quality / infertility
```

**Upstream vs downstream.** Adhesion and the virulence triad (urease, IgA1 protease, MBA) are **upstream** initiating/persistence factors; neutrophilic inflammation is the **proximate cause** of symptoms; complications are **downstream** sequelae of persistence and seminal inflammation. The **load-dependent, conditional** nature explains why UU is detected in asymptomatic controls yet drives urethritis at higher burden — reconciling the positive association ([PMID: 11939406](https://pubmed.ncbi.nlm.nih.gov/11939406/); [PMID: 17522569](https://pubmed.ncbi.nlm.nih.gov/17522569/)) with the null/reverse association in monoinfection ([PMID: 31515293](https://pubmed.ncbi.nlm.nih.gov/31515293/)).

---

## Evidence Base

| PMID | Study / type | Supports finding |
|------|-------------|------------------|
| [11939406](https://pubmed.ncbi.nlm.nih.gov/11939406/) | Case-control, n=340 (human clinical) | UU biovar 2 associated with NGU (P=0.012) |
| [17522569](https://pubmed.ncbi.nlm.nih.gov/17522569/) | qPCR load study (human clinical) | Load-dependent pathogenicity; U. parvum non-pathogenic |
| [31515293](https://pubmed.ncbi.nlm.nih.gov/31515293/) | Case-control, n=155/103 (human clinical) | Counter-evidence: UU monoinfection = conditional/colonizer |
| [40497611](https://pubmed.ncbi.nlm.nih.gov/40497611/) | Cohort, n=1,249 NGU (human clinical) | UU leading NGU cause (40.59%); male predominance |
| [17806051](https://pubmed.ncbi.nlm.nih.gov/17806051/) | Cohort (human clinical) | UU biovar 2 → 3.64× postgonococcal urethritis risk |
| [23223595](https://pubmed.ncbi.nlm.nih.gov/23223595/) | RCT, n=606 (human clinical) | Azithromycin 80% vs doxycycline 76% cure |
| [24106340](https://pubmed.ncbi.nlm.nih.gov/24106340/) | Prospective cohort (human clinical) | Adherence → UU-2 microbiologic cure (aRR 3.08) |
| [34618416](https://pubmed.ncbi.nlm.nih.gov/34618416/) | Cohort (human clinical) | 100% UU clinical cure with azithromycin |
| [1587621](https://pubmed.ncbi.nlm.nih.gov/1587621/) | Biochemical (in vitro) | IgA1 protease cleaves Pro235–Thr236 |
| [6392177](https://pubmed.ncbi.nlm.nih.gov/6392177/) | Comparative (in vitro) | IgA1 protease exclusive to U. urealyticum; U. diversum most potent |
| [3882564](https://pubmed.ncbi.nlm.nih.gov/3882564/) | Comparative (in vitro) | IgA protease as mucosal virulence factor |
| [22646228](https://pubmed.ncbi.nlm.nih.gov/22646228/) | Comparative genomics (19 strains) | MBA phase-variable gene superfamily; genome sizes |
| [40247169](https://pubmed.ncbi.nlm.nih.gov/40247169/) | Meta-analysis (human clinical) | UU reduces semen quality (SMDs) |
| [41217668](https://pubmed.ncbi.nlm.nih.gov/41217668/) | Case-control (human clinical) | ↑seminal elastase, ↑DNA fragmentation |
| [41500460](https://pubmed.ncbi.nlm.nih.gov/41500460/) | Review (human clinical) | UU leading seminal-tract pathogen; ~15% male infertility |
| [19273669](https://pubmed.ncbi.nlm.nih.gov/19273669/) | Susceptibility/genotyping (in vitro) | tetM; low baseline resistance; L4/ParC mutations |
| [26220178](https://pubmed.ncbi.nlm.nih.gov/26220178/) | Guideline/review (human clinical) | NGU definition; PMN diagnostic criterion |
| [33423450](https://pubmed.ncbi.nlm.nih.gov/33423450/) | Clinical profile (human clinical) | Dysuria 88%, discharge ~86% |
| [32149960](https://pubmed.ncbi.nlm.nih.gov/32149960/) | Cohort (human clinical) | No sign/symptom predicts etiology |
| [37683891](https://pubmed.ncbi.nlm.nih.gov/37683891/) | Assay development (diagnostic) | Rapid multiplex real-time PCR vs slow culture |
| [26538551](https://pubmed.ncbi.nlm.nih.gov/26538551/) | Multiplex panel (diagnostic) | UU within 9-pathogen STI NAAT |
| [21392925](https://pubmed.ncbi.nlm.nih.gov/21392925/) | Multiplex PCR (diagnostic) | 98% sensitivity for genital Ureaplasma |
| [41665055](https://pubmed.ncbi.nlm.nih.gov/41665055/) | Cross-sectional, n=2,668 (human clinical) | Smoking & sexual frequency risk factors |
| [42163127](https://pubmed.ncbi.nlm.nih.gov/42163127/) | 6-yr retrospective (human clinical) | Detection distribution; rising fluoroquinolone resistance |
| [22731950](https://pubmed.ncbi.nlm.nih.gov/22731950/) | Veterinary (animal) | U. diversum bovine genital disease spectrum |
| [29236848](https://pubmed.ncbi.nlm.nih.gov/29236848/) | Histopathology (animal) | Conserved neutrophilic epithelial injury |
| [42113363](https://pubmed.ncbi.nlm.nih.gov/42113363/) | Prevalence (animal) | Bovine U. diversum prevalence |
| [16340190](https://pubmed.ncbi.nlm.nih.gov/16340190/) | Pilot RCT (human clinical) | UU chronic prostatitis; azithromycin/doxycycline |
| [7629982](https://pubmed.ncbi.nlm.nih.gov/7629982/) | RCT, n=452 (human clinical) | 81% cumulative NGU cure |
| [39629051](https://pubmed.ncbi.nlm.nih.gov/39629051/) | Retrospective (human clinical) | ↑anti-sperm antibodies; IVF outcomes unaffected |

---

## Limitations and Knowledge Gaps

1. **Conditional-pathogen ambiguity.** The single greatest interpretive challenge is that *U. urealyticum* is frequently detected in asymptomatic controls ([PMID: 31515293](https://pubmed.ncbi.nlm.nih.gov/31515293/)). Association is load- and biovar-dependent, but **clinically validated load thresholds** distinguishing disease from carriage are not standardized.
2. **Mechanism largely inferred.** The urease→ammonia cytotoxicity step and the integration of MBA phase variation into urethral disease are supported by in vitro and genomic data but have **limited direct in vivo demonstration in the human male urethra**.
3. **No primary data analysis.** This report synthesizes observational and trial literature; no dataset was provided. Findings rest on published effect sizes.
4. **Resistance heterogeneity.** Resistance data range from very low (Beeton 2009) to very high regional fluoroquinolone resistance (Turkey), limiting generalizable treatment guidance.
5. **Female urethritis under-characterized.** Most data concern men; Ureaplasma's role in female urethritis vs cervicitis/carriage is less defined.
6. **No human host-genetic dimension** was found — sections on causal genes, inheritance, penetrance, and genetic screening are not applicable, as expected for an acquired STI.

---

## Proposed Follow-up Experiments / Actions

1. **Establish quantitative diagnostic cutoffs:** Prospective qPCR study correlating *U. urealyticum* biovar 2 **load** with PMN counts and symptoms to define a clinically actionable threshold separating disease from carriage.
2. **Mechanistic validation in an epithelial model:** Human urethral epithelial organoids/air-liquid cultures ± urease-deficient and IgA1-protease-deficient *U. urealyticum* mutants to directly test the ammonia and immune-evasion steps.
3. **Resistance surveillance & stewardship:** Multi-region tet(M), 23S rRNA/L4, and parC genotyping linked to MIC and clinical outcomes to build a resistance-guided treatment algorithm.
4. **Randomized adherence/partner-treatment trial:** Test whether directly-observed therapy and universal partner treatment improve UU-2 microbiologic cure and reduce recurrence.
5. **Fertility outcomes:** Longitudinal study of whether treating UU-positive men improves semen parameters (elastase, DNA fragmentation) and time-to-conception.
6. **Comparative-genomics of virulence:** Contrast human *U. urealyticum* and bovine *U. diversum* IgA-protease/urease loci to identify conserved vaccine/therapeutic targets.

---

## Conclusion

Ureaplasma urethritis is an infectious, behaviorally acquired, non-genetic STI in which *Ureaplasma urealyticum* biovar 2 acts as a **load-dependent conditional pathogen** of the male urethral epithelium, driving mild neutrophilic urethritis through urease-generated ammonia, a secreted IgA1 protease, and phase-variable MBA immune evasion. It is diagnosed by urethral PMN excess plus multiplex NAAT, carries an excellent prognosis under doxycycline or azithromycin (~76–81% cure), and its principal harms are persistence-related complications (epididymitis, prostatitis, reduced fertility) amid a backdrop of rising regional antimicrobial resistance.


## Artifacts

- [OpenScientist final report](Ureaplasma_Urethritis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ureaplasma_Urethritis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 31 |
| On topic | 23 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40247169` *(abstract only)*: "*U. urealyticum* significantly reduced ejaculate volume (SMD 0.33 [95% CI: 0.15, 0.52] p = 0.0004), sperm concentration (SMD 0.47 [95% CI: 0.31, 0.64] p < 0.00001), total sperm motility (SMD 0.73 [95% CI: 0.43, 1.02] p < 0.00001)"
  - closest text in source: "urealyticum significantly reduced ejaculate volume (SMD 0.33 [95% CI: 0.15, 0.52] p = 0.0004), sperm concentration (SMD 0.47 [95% CI: 0.31, 0.64] p < 0.00001), total sperm motility (SMD 0.73 [95% CI: 0.43, 1.02] p < 0.00001), total motile sperm count (SMD 0.21 [95% CI: 0.17, 0.26] p < 0.00001), normal sperm morphology (SMD 0.88 [95% CI: 0.42, 1.35] p = 0.0002), but increased seminal fluid leukocyte count (SMD -0.82 [95% CI: -1.61, -0.02] p = 0.04)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025401` (1 mention) - the report calls it "abnormal urethral discharge"; HP calls it **Staring gaze**
- `HP:0032263` (1 mention) - the report calls it "abnormal inflammatory marker"; HP calls it **Increased blood pressure**
- `NCIT:C692` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Nimodipine**
- `NCIT:C1662` (1 mention) - the report calls it "Azithromycin"; NCIT calls it **Indinavir Sulfate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006508` (1 mention) - the report calls it "proteolysis, IgA1 cleavage"; GO calls it **proteolysis**
- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `CL:0000775` (2 mentions) - the report calls it "neutrophil", "neutrophils/PMNs"; CL calls it **neutrophil**
- `CL:0002251` (1 mention) - the report calls it "epithelial cell of urethra, approx"; CL calls it **epithelial cell of alimentary canal**
- `UBERON:0000990` (1 mention) - the report calls it "genitourinary / reproductive system"; UBERON calls it **reproductive system**, and lists "animal reproductive system" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000775` - called "neutrophil", "neutrophils/PMNs"