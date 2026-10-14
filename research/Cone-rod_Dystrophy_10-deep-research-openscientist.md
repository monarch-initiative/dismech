---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T12:24:14.879362'
end_time: '2026-10-14T12:38:57.785547'
duration_seconds: 882.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cone-rod dystrophy 10
  mondo_id: MONDO:0012464
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
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 11
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0012464
    reported_labels:
    - MONDO
    ontology_label: cone-rod dystrophy 10
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: HP:0000551
    reported_labels:
    - Symptom/sign
    ontology_label: Color vision defect
  - term_id: HP:0000662
    reported_labels:
    - Symptom
    ontology_label: Nyctalopia
  - term_id: HP:0000512
    reported_labels:
    - Lab/functional
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0007843
    reported_labels:
    - Sign
    ontology_label: Attenuation of retinal blood vessels
  - term_id: UBERON:0002423
    reported_labels:
    - macula
    ontology_label: hepatobiliary system
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
  path: Cone-rod_Dystrophy_10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cone-rod_Dystrophy_10-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cone-rod dystrophy 10
- **MONDO ID:** MONDO:0012464 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cone-rod dystrophy 10** covering all of the
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

# Cone-Rod Dystrophy 10 (CORD10): Comprehensive Disease Characterization Report

**Disease:** Cone-rod dystrophy 10 (CORD10)
**MONDO ID:** MONDO:0012464 | **OMIM:** #610283 | **Causal gene:** *SEMA4A* (semaphorin 4A, chromosome 1q22)
**Category:** Mendelian inherited retinal dystrophy
**Report date:** 2026-10-14

---

## Summary

Cone-rod dystrophy 10 (CORD10) is a rare, bilateral, progressive non-syndromic **inherited retinal dystrophy (IRD)** caused by germline missense mutations in the gene *SEMA4A*, which encodes the transmembrane protein **semaphorin 4A**. The disease belongs to the clinically and genetically heterogeneous cone-rod dystrophy (CRD) group, in which cone photoreceptors degenerate first or concurrently with rods, producing early loss of central visual acuity, photophobia, impaired color vision, and later night blindness and peripheral visual-field constriction. The disease-causing variants (notably **p.D345H** and **p.F350C**) cluster in the conserved extracellular **Sema domain** of the protein and were originally identified in retinal-degeneration families, establishing *SEMA4A* as the causal gene for CORD10 ([PMID: 16199541](https://pubmed.ncbi.nlm.nih.gov/16199541/)).

Mechanistically, CORD10 is a **loss-of-function disorder of retinal pigment epithelium (RPE) endosomal sorting**. SEMA4A normally mediates **Rab11/FIP2-dependent endosomal sorting** in the RPE, which (1) under oxidative/light stress diverts the anti-apoptotic lysosomal precursor **prosaposin** from lysosomal degradation to exosomal secretion, protecting photoreceptors from light-induced apoptosis, and (2) under baseline conditions sorts retinoid-binding proteins to regenerate **11-cis-retinal**, the chromophore for phototransduction. The Sema-domain missense mutation (e.g., p.F350C) alters protein conformation and causes abnormal subcellular localization, crippling this sorting machinery. Photoreceptors consequently lose both anti-apoptotic support and chromophore supply, and undergo progressive apoptosis — cones first, then rods ([PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/); [PMID: 22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/)).

This causal chain is validated in animal models: *Sema4A* knockout mice develop severe early retinal degeneration affecting both rods and cones, and knock-in mice carrying the F350C allele reproduce the degeneration, which is **rescued by AAV-mediated *Sema4A* gene transfer** ([PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/); [PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/)). There is currently **no approved disease-specific therapy** for CORD10; management is supportive (low-vision rehabilitation, genetic counseling). Gene augmentation for loss-of-function alleles and CRISPR editing for any dominant allele are the leading, preclinically-validated therapeutic strategies for the cone-rod dystrophy class.

---

## 1. Disease Information

**Overview.** CORD10 is a monogenic, non-syndromic cone-rod dystrophy — a form of inherited retinal degeneration in which cone photoreceptors (responsible for central, high-acuity, daylight, and color vision) are affected first or together with rod photoreceptors (responsible for peripheral and night vision). This "cone-led" pattern distinguishes CRD from rod-cone dystrophy / retinitis pigmentosa, where rods fail first. CORD10 specifically denotes the subtype caused by variants in *SEMA4A*.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #610283 (CONE-ROD DYSTROPHY 10; CORD10) |
| MONDO | MONDO:0012464 |
| Gene | *SEMA4A* (HGNC: 10730); OMIM gene #607292 |
| Chromosomal locus | 1q22 |
| Orphanet | Cone-rod dystrophy (parent group ORPHA:1872; no separate CORD10 ORPHA generally assigned) |
| ICD-10 | H35.54 (dystrophies primarily involving the sensory retina) |
| ICD-11 | 9B70.0 / 9B70 (hereditary retinal dystrophy) |
| MeSH | Cone-Rod Dystrophies; Retinal Dystrophies |

**Synonyms / alternative names:** CORD10; CRD10; cone-rod dystrophy 10; SEMA4A-related cone-rod dystrophy; SEMA4A-associated retinal degeneration. (*SEMA4A* variants are also reported in association with retinitis pigmentosa, reflecting phenotypic overlap.)

**Information source.** The CORD10 knowledge base is derived from **aggregated disease-level resources** (OMIM, gene/variant databases) plus **primary literature from individual patients and families** (the original Pakistani retinal-dystrophy families) and **model-organism experiments** (mouse knockout/knock-in). It is not EHR-derived population data.

---

## 2. Etiology

**Primary cause — genetic.** CORD10 is a **Mendelian, monogenic disorder** caused by pathogenic missense variants in *SEMA4A*. The founding report screened 190 unrelated retinal-disease patients (135 retinitis pigmentosa, 25 CRD, 30 Leber congenital amaurosis) and identified heterozygous *SEMA4A* missense mutations exclusively in affected individuals and absent from 100 controls ([PMID: 16199541](https://pubmed.ncbi.nlm.nih.gov/16199541/)):

> "We report the first observation of the involvement of SEMA4A gene mutations causing retinitis pigmentosa (RP) and cone rod dystrophy (CRD)."

> "Two mutations, p.D345H and p.F350C, were observed only in affected patients; they were not observed in any of the normal members or the 100 control subjects. Both mutations identified occur in the conserved semaphorin domain."

**Genetic risk factors.** The causal variants are the *SEMA4A* Sema-domain missense changes themselves (p.D345H, p.F350C, and other reported alleles such as p.R713Q in the cytoplasmic domain). **Consanguinity** is a major contextual risk factor: *SEMA4A*-linked disease was first described in Pakistani families, and recessive IRDs generally are strongly enriched in consanguineous Middle Eastern/North African and South Asian populations, where founder mutations recur ([PMID: 35551639](https://pubmed.ncbi.nlm.nih.gov/35551639/)).

**Environmental risk factors.** No established environmental cause. However, the mechanism implicates **light exposure and oxidative stress** as modulators of photoreceptor survival: SEMA4A's protective prosaposin-sorting function is specifically engaged "in response to oxidative stress" to prevent "light-induced photoreceptor apoptosis," so cumulative light/oxidative burden plausibly influences the rate of degeneration ([PMID: 22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/)). This is mechanistically inferred, not clinically demonstrated for CORD10.

**Protective factors.** None genetically defined for CORD10. By mechanistic inference, measures reducing oxidative/photic stress (UV/blue-light protection, antioxidant support) are plausible but unproven disease modifiers.

**Gene-environment interactions.** The core interaction is **genotype × photo-oxidative stress**: a hypomorphic/mislocalized SEMA4A cannot mount the stress-induced prosaposin-sorting response, so the same light/oxidative load that is tolerated in healthy RPE becomes injurious. This is a plausible but not formally tested GxE model.

---

## 3. Phenotypes

CORD10 produces the characteristic cone-rod dystrophy symptom complex. Because CORD10 is rare, per-phenotype frequencies are extrapolated from the CRD class and from *SEMA4A* model data rather than from large CORD10 cohorts.

| Phenotype | Type | HPO term | Onset | Severity / course | Notes |
|---|---|---|---|---|---|
| Reduced visual acuity | Symptom/sign | HP:0000572 / HP:0000505 | Childhood–early adult | Moderate→severe, progressive | Central/macular, cone-driven |
| Photophobia | Symptom | HP:0000613 | Early | Variable, often prominent | Classic cone-dysfunction feature |
| Dyschromatopsia (color-vision defect) | Symptom/sign | HP:0000551 | Early | Progressive | Cone loss |
| Reduced/constricted visual field | Sign | HP:0001123 / HP:0007994 | Later | Progressive | Rod involvement |
| Nyctalopia (night blindness) | Symptom | HP:0000662 | Later | Progressive | Appears as rods degenerate |
| Abnormal electroretinogram (cone > rod) | Lab/functional | HP:0000512 | Detectable early | Progressive | Diagnostic hallmark |
| Macular degeneration / RPE changes | Sign (imaging) | HP:0000608 / HP:0007754 | Variable | Progressive | Central atrophy, bull's-eye possible |
| Attenuated retinal vessels | Sign | HP:0007843 | Later | Progressive | Seen in *Sema4A*-null mice |
| Abnormal fundus pigmentation/depigmentation | Sign | HP:0008046 / HP:0030506 | Variable | Progressive | RPE depigmentation (mouse) |

**Characteristic pattern.** In cone-rod dystrophies, degeneration begins in the cone-rich central macula before spreading peripherally — hence early loss of acuity/color and late night-blindness/field loss. The *SEMA4A* mouse phenotype confirms that "disruption of Sema4A also compromised the physiological function of both rod and cone photoreceptors," consistent with pan-photoreceptor disease ([PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/)).

**Quality-of-life impact.** CORD10 is a cause of **progressive low vision and eventual legal blindness**, with major impact on reading, driving, face recognition, mobility, education, and employment. Photophobia adds daily discomfort in ordinary lighting. No CORD10-specific EQ-5D/SF-36 data exist; impact is inferred from the severe-visual-impairment trajectory common to CRDs.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SEMA4A*** (semaphorin 4A), HGNC:10730, OMIM *607292, chromosome **1q22**. It encodes a **760-amino-acid type-I transmembrane protein** of the semaphorin family, with an extracellular **Sema domain**, immunoglobulin-like domain, transmembrane segment, and short cytoplasmic tail ([PMID: 16199541](https://pubmed.ncbi.nlm.nih.gov/16199541/)).

**Pathogenic variants.**

| Variant | Domain | Type | Classification | Evidence |
|---|---|---|---|---|
| p.D345H (c.1033G>C) | Sema domain | Missense | Pathogenic/likely pathogenic (segregating; absent in 100 controls) | PMID 16199541 |
| p.F350C (c.1049T>G) | Sema domain | Missense | Pathogenic — functionally validated in mouse | PMID 16199541; 23360997 |
| p.R713Q | Cytoplasmic | Missense | Reported; **not** degeneration-causing in knock-in mice | PMID 23360997 |

**Variant type/class.** All reported CORD10 alleles are **missense** point mutations; no structural/CNV causes are established. The disease-relevant variants concentrate in the **conserved extracellular Sema domain**, where residue 350 is structurally critical: structural modeling shows the 350th side chain is critical for proper protein conformation ([PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/)).

**Allele frequency.** The pathogenic Sema-domain alleles are **absent/ultra-rare** in population databases (absent from 100 ethnically matched controls in the founding study; rare in gnomAD), consistent with pathogenicity.

**Somatic vs germline.** **Germline** only. No somatic/mosaic mechanism is implicated.

**Functional consequence.** **Loss of function via mislocalization.** The critical functional readout is that F350C "results in abnormal localization of the Sema4A protein, leading to impaired endosomal sorting of molecules indispensable for photoreceptor survival," and reintroducing functional Sema4A rescues the phenotype — the hallmark of loss of function ([PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/)). Human reports include heterozygous (dominant) and recessive presentations, and the phenotypic overlap between CORD10 and RP indicates allele- and dose-dependent expressivity.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic marks, or cytogenetic abnormalities are established for CORD10. Given SEMA4A's pleiotropy and receptor network (below), modifier effects are biologically plausible but unstudied.

**Receptor / interaction network.** SEMA4A is a dual neuro-immune "immune semaphorin" that signals through **Tim-2** and **CD72** on leukocytes and **PlexinB1 (PLXNB1)** and **PlexinD1 (PLXND1)** on non-immune cells ([PMID: 21595947](https://pubmed.ncbi.nlm.nih.gov/21595947/)):

> "Sema4A and Sema4D were the first semaphorins found to be expressed on immune cells and were termed 'immune semaphorins'. It is known that Sema4A and Sema4D bind Tim-2 and CD72 expressed on leukocytes and PlexinD1 and B1 present on non-immune cells."

Ontology suggestions: gene HGNC:10730; GO:0007411 (axon guidance), GO:0016192 (vesicle-mediated transport), GO:0032456 (endocytic recycling).

---

## 5. Environmental Information

CORD10 is a **monogenic disease with no established environmental cause.** No toxins, radiation, pollutants, occupational exposures, infectious agents, or specific lifestyle factors are documented as causal or triggering. The only mechanistically relevant environmental variables are **ambient light and oxidative stress**, which the SEMA4A-dependent prosaposin-sorting pathway normally buffers to prevent "light-induced photoreceptor apoptosis" ([PMID: 22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/)). **No infectious agents** are implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline missense mutation** in the conserved extracellular **Sema domain** of *SEMA4A* (e.g., p.F350C; p.D345H) **alters the amino-acid side chain critical for protein folding**, which *leads to* an abnormal protein conformation. *(Demonstrated by structural modeling; PMID 23360997.)*
2. The misfolded SEMA4A **is abnormally (mis)localized** within the cell rather than reaching its functional membrane/endosomal compartment. *(Demonstrated; PMID 23360997.)*
3. Mislocalized SEMA4A **can no longer drive Rab11/FIP2-dependent endosomal sorting** in the **retinal pigment epithelium (RPE)**, which *results in* failure of two downstream cargo-sorting functions. *(Demonstrated in RPE cells; PMID 22465952.)*

   **Branch A (stress response):** Under oxidative/light stress, SEMA4A normally **switches sorting of the lysosomal precursor prosaposin from lysosomal degradation to exosomal release**; loss of this switch *results in* failure to deliver anti-apoptotic prosaposin, so photoreceptors lose protection against **light-induced apoptosis**.

   **Branch B (visual cycle):** Under baseline conditions, SEMA4A normally **sorts retinoid-binding proteins to regenerate 11-cis-retinal**; loss *results in* impaired chromophore supply to photoreceptors.
4. Combined loss of anti-apoptotic support (Branch A) and chromophore supply (Branch B) *leads to* **photoreceptor dysfunction and progressive apoptosis**. *(Inferred synthesis of A+B; each arm demonstrated.)*
5. Because the cone-rich central macula is affected first, this *leads to* **early cone loss (reduced acuity, photophobia, dyschromatopsia), followed by rod loss (night blindness, peripheral field constriction)** — the clinical cone-rod dystrophy phenotype. *(Clinical pattern; model data show both rod and cone compromise, PMID 15277503.)*

### Causal-chain diagram

```
SEMA4A Sema-domain missense (F350C / D345H)
        │  (altered side chain → misfolding)
        ▼
Abnormal SEMA4A protein conformation
        │
        ▼
Mislocalization of SEMA4A protein
        │
        ▼
Failure of Rab11/FIP2 endosomal sorting in RPE
        ├───────────────────────────┐
        ▼                            ▼
Branch A: no stress-induced     Branch B: no retinoid-protein
prosaposin → exosome switch     sorting → ↓ 11-cis-retinal
        │                            │
        ▼                            ▼
Loss of anti-apoptotic          Impaired chromophore
protection (light stress)       supply / phototransduction
        └───────────────┬────────────┘
                        ▼
        Progressive photoreceptor apoptosis
                        ▼
      Cone loss first → then rod loss (bilateral)
                        ▼
   CORD10: ↓acuity, photophobia, dyschromatopsia,
           later nyctalopia & field constriction
```

### Detail by category

- **Molecular pathways / cellular processes:** Rab11/FIP2 endocytic recycling and endosomal cargo sorting (GO:0032456 endocytic recycling; GO:0016192 vesicle-mediated transport); regulated exosome biogenesis/secretion; apoptosis (GO:0006915) as the terminal photoreceptor-death process; the visual cycle / retinoid metabolism (11-cis-retinal regeneration).
- **Protein dysfunction:** Conformational destabilization of the Sema β-propeller domain → aberrant trafficking/localization (a trafficking-type loss of function rather than a simple null). CHEBI entities: 11-cis-retinal (CHEBI:16066), retinoid (CHEBI:26537).
- **Tissue-damage mechanism:** Photo-oxidative stress unbuffered by prosaposin exosomal delivery → light-induced photoreceptor apoptosis.
- **Immune involvement:** SEMA4A is an "immune semaphorin," but immune dysfunction is **not** the operative mechanism in CORD10; the retinal phenotype is driven by the RPE sorting defect. SEMA4A pleiotropy (immune, neuronal, cardiovascular, renal) explains why variant class/location determines which phenotype emerges.
- **Molecular profiling:** No CORD10-specific transcriptomic/proteomic/metabolomic datasets identified. SEMA4A expression in RPE can be up-regulated by neural-cell–derived PACAP ([PMID: 25515530](https://pubmed.ncbi.nlm.nih.gov/25515530/)), indicating physiological regulation of the pathway in the retina.

**Upstream vs downstream:** The *SEMA4A* mutation and RPE sorting failure are **upstream/initiating**; photoreceptor apoptosis and the clinical cone-then-rod phenotype are **downstream**. The RPE is the primary site of molecular defect even though photoreceptors are the dying cells (a non-cell-autonomous mechanism).

**Suggested GO/CL terms:** Biological processes — GO:0032456 (endocytic recycling), GO:0006915 (apoptotic process), GO:0007601 (visual perception); cell types — RPE cell (CL:0002586), cone photoreceptor (CL:0000573), rod photoreceptor (CL:0000604).

---

## 7. Anatomical Structures Affected

**Organ level.** The **eye** (UBERON:0000970), specifically the **neural retina** (UBERON:0003902) and the **retinal pigment epithelium** (UBERON:0001782). Disease is **bilateral**. No primary involvement of other organ systems in CORD10 (though SEMA4A is systemically expressed).

**Tissue/cell level.** Primary molecular lesion is in the **RPE** (CL:0002586), which non-cell-autonomously supports the overlying **photoreceptor layer** — both **cone photoreceptors** (CL:0000573) and **rod photoreceptors** (CL:0000604). In *Sema4A*-null mice: "the outer nuclear layer was reduced to a single row of photoreceptor cells, and the outer plexiform layer was thin and disorganized," with RPE depigmentation and attenuated vessels ([PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/)). Mechanistic localization to RPE: Sema4A "plays a role in Rab11/FIP2-mediated endosomal sorting in retinal pigment epithelial cells to support photoreceptor function" ([PMID: 22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/)).

**Subcellular level.** **Endosomes / recycling endosomes** (GO:0005768 endosome; GO:0055037 recycling endosome), **exosomes/multivesicular bodies** (GO:0070062 extracellular exosome), **lysosome** (GO:0005764), and the **plasma membrane** (GO:0005886). The trafficking defect centers on the Rab11/FIP2 recycling-endosome machinery.

**Localization.** Bilateral; disease begins in the **macula** (UBERON:0002423) / central retina and spreads peripherally in the cone-rod pattern.

---

## 8. Temporal Development

**Onset.** Typically **childhood to early adulthood** (consistent with the CRD class), with insidious, chronic onset. CORD10 is not congenital in the LCA sense, but early cone dysfunction (photophobia, acuity/color problems) is often the first complaint.

**Progression.** **Chronic, progressive, lifelong.** Stages: early cone-dominated central dysfunction → intermediate combined cone-rod loss → advanced widespread photoreceptor degeneration with legal blindness. Progression rate is variable (characteristic of IRDs). In the mouse null, "fundus photography performed at 14 weeks of age revealed severe retinal degeneration, attenuated retinal vessels, and depigmentation," indicating a relatively rapid course in the complete-loss-of-function model ([PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/)).

**Patterns.** No spontaneous remission; the disease does not relapse-remit — it is steadily progressive. The **critical intervention window** is before substantial photoreceptor loss: gene-augmentation rescue in mice is most effective while photoreceptors remain viable, defining a therapeutic time window analogous to other IRD gene therapies.

---

## 9. Inheritance and Population

**Epidemiology.** CORD10 is a **rare subtype of a rare disease group.** Cone-rod dystrophies collectively account for a minority of IRDs — e.g., **8.0% of 325 patients** in a Southeastern US IRD cohort ([PMID: 36011402](https://pubmed.ncbi.nlm.nih.gov/36011402/)):

> "The most prevalent dystrophies identified clinically were non-syndromic retinitis pigmentosa (29.8%), Stargardt disease (8.3%), Usher syndrome (8.3%), cone-rod dystrophy (8.0%), cone dystrophy (4.9%), and Leber congenital amaurosis (4.3%)."

CRD overall prevalence is on the order of ~1 in 40,000. IRDs collectively involve **>340 genes**, and *SEMA4A* is an **uncommon** CRD cause. No separate prevalence/incidence figures exist for the *SEMA4A* subtype specifically.

**Inheritance.** Reported as both **autosomal dominant** (heterozygous Sema-domain missense in the founding families) and **autosomal recessive** (depending on allele); *SEMA4A* variants cause a spectrum spanning CRD and RP. The dual reporting reflects allele-specific functional consequences and incomplete characterization.

**Penetrance / expressivity.** Variable expressivity is evident from the CRD↔RP phenotypic overlap for *SEMA4A*. Penetrance of the classic Sema-domain alleles appears high given tight segregation with disease in the original families, but precise estimates are unavailable.

**Anticipation / mosaicism.** No genetic anticipation (not a repeat-expansion disorder). No germline mosaicism documented.

**Founder effects / consanguinity.** The founding *SEMA4A* families were **Pakistani**, and recessive IRDs are strongly enriched in **consanguineous** Middle Eastern, North African, and South Asian populations with founder mutations. In a North African IRD/ION review, "76.1% of IRD ... investigated families were consanguineous," underscoring the population context in which recessive *SEMA4A* disease is most likely to surface ([PMID: 35551639](https://pubmed.ncbi.nlm.nih.gov/35551639/)).

**Population demographics / sex ratio / geographic distribution.** No sex predilection expected for an autosomal gene. Higher detection likelihood in consanguineous South Asian / Middle Eastern / North African communities. No endemic geographic clustering beyond founder/consanguinity effects.

---

## 10. Diagnostics

**Clinical/functional tests.**
- **Electroretinography (ERG)** — the functional hallmark: reduced/abnormal cone responses, with rod involvement developing over time (abnormal ERG, HP:0000512). Mouse data confirm both rod and cone functional compromise ([PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/)).
- **Multimodal retinal imaging** — fundus photography (RPE changes, vessel attenuation, macular atrophy/bull's-eye), **fundus autofluorescence** (RPE/outer-retinal disturbance), and **spectral-domain OCT** (outer-retinal/photoreceptor layer thinning). These are standard CRD workup tools.
- **Color-vision testing** and **visual-field perimetry** document dyschromatopsia and progressive field loss.
- No specific **blood/urine biomarker**, enzyme assay, or biopsy is diagnostic; diagnosis is clinical + genetic.

**Genetic testing (the definitive diagnostic).**
- **Targeted NGS IRD gene panels** including *SEMA4A* are the recommended first-line molecular test; CRD panels routinely cover dozens-to-hundreds of IRD genes.
- **Whole-exome sequencing (WES)** and **whole-genome sequencing (WGS)** are valuable when panels are negative. Diagnostic yield for CRD is lower than for distinctive phenotypes (e.g., LCA, Bietti dystrophy) because CRD is common and heterogeneous ([PMID: 40114034](https://pubmed.ncbi.nlm.nih.gov/40114034/)).
- **Single-gene testing** of *SEMA4A* is appropriate for cascade testing within known families.
- CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable** (CORD10 is a point-mutation disorder).

**Clinical criteria / differential diagnosis.** Diagnosis rests on the cone-rod ERG pattern plus imaging and confirmatory genetics. Key differentials to exclude include other CRD genes (**ABCA4, GUCY2D, CRX, PROM1, CDHR1, RPGR**), achromatopsia (**CNGA3/CNGB3**), cone dystrophy with supernormal rod responses (**KCNV2**; [PMID: 33706576](https://pubmed.ncbi.nlm.nih.gov/33706576/)), and **syndromic** mimics — e.g., ACBD5 deficiency (retinal dystrophy + leukodystrophy; [PMID: 42343915](https://pubmed.ncbi.nlm.nih.gov/42343915/)) and Alström syndrome (infantile cone-rod dystrophy with cardiomyopathy/obesity; [PMID: 9663233](https://pubmed.ncbi.nlm.nih.gov/9663233/)). Note that *SEMA4A* was flagged as a candidate novel genotype-phenotype correlation in a large macular/cone-rod cohort ([PMID: 29555955](https://pubmed.ncbi.nlm.nih.gov/29555955/)).

**Screening.** No newborn screening. **Cascade/carrier testing** of relatives once the familial *SEMA4A* variant is known; preconception/prenatal options via genetic counseling.

---

## 11. Outcome / Prognosis

**Survival/mortality.** CORD10 is **not life-limiting**; life expectancy is normal. The burden is **visual morbidity**, not mortality.

**Morbidity/function.** The natural history is **progressive loss of vision to legal blindness**, with major disability in reading, driving, mobility, and independence. Early central (cone) loss is particularly disabling for daily high-acuity tasks; later rod loss adds night blindness and field constriction. No CORD10-specific EQ-5D/SF-36/PROMIS data exist.

**Disease course/complications.** Complications are those of severe low vision (falls, dependency, reduced quality of life). There is no spontaneous recovery; photoreceptor loss is irreversible once cells die.

**Prognostic factors.** Residual photoreceptor viability (OCT outer-retinal integrity), age at onset, and rate of ERG decline are the practical prognostic indicators; earlier/more complete loss of function (as in the null mouse) predicts faster, more severe degeneration. Genotype (allele severity/location in the Sema domain) is a biologically-grounded prognostic factor.

---

## 12. Treatment

**Current standard: supportive.** There is **no FDA/EMA-approved disease-specific therapy** for *SEMA4A*-related CORD10. Management is **low-vision rehabilitation** (magnifiers, high-contrast aids, lighting/glare management for photophobia — tinted/UV-blocking lenses), **occupational support**, orientation/mobility training, and **genetic counseling**. NCIT suggestions: supportive care (NCIT:C19054), genetic counseling (NCIT:C15516), low-vision rehabilitation.

**Advanced therapeutics (preclinical / class-level).**
- **Gene augmentation (AAV).** Directly validated for *SEMA4A*: "Sema4A gene transfer successfully prevents photoreceptor degeneration in Sema4A(F350C/F350C) and Sema4A(-/-) mice" — strong rationale for AAV *SEMA4A* augmentation in loss-of-function CORD10 ([PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/)). AAV subretinal gene augmentation is the leading, field-proven IRD strategy (cf. voretigene neparvovec for *RPE65*).
- **Gene editing (CRISPR/Cas9).** For any autosomal-dominant gain-of-function/dominant-negative *SEMA4A* allele, mutation-specific correction or allele ablation ("ablate-and-replace") is the emerging approach; CRISPR "offers the potential for one-time, mutation-specific gene correction or allele ablation" for CRD and achromatopsia, addressing the limitations of AAV augmentation in dominant disease ([PMID: 42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/)).
- **Gene-independent neuroprotection.** AAV-delivered rod-derived cone viability factors (RdCVF/RdCVFL from *NXNL1*) preserve cones and reduce lipid peroxidation in RP models and are in clinical trial (PRODYGY, NCT05748873) — a mutation-agnostic strategy potentially relevant to CRD cone rescue ([PMID: 41769936](https://pubmed.ncbi.nlm.nih.gov/41769936/)).

**Pharmacotherapy / pharmacogenomics / immunotherapy / surgery.** No disease-specific drugs, pharmacogenomic guidance, immunotherapies, or surgical interventions are established for CORD10. Standard ophthalmic care may be needed for incidental comorbidities.

**Personalized medicine.** Treatment is inherently **genotype-guided**: loss-of-function alleles → augmentation; dominant alleles → editing/ablation. Confirming the precise *SEMA4A* variant and its functional class is prerequisite to any future targeted therapy.

---

## 13. Prevention

**Primary prevention.** No way to prevent a germline mutation. The main lever is **reproductive risk reduction** via genetic counseling, carrier/cascade testing, and reproductive options (preimplantation genetic testing, prenatal diagnosis) in families with a known *SEMA4A* variant.

**Secondary prevention.** **Cascade genetic screening** of at-risk relatives enables earlier diagnosis and candidacy for emerging therapies while photoreceptors remain viable (the key intervention window).

**Tertiary prevention.** Low-vision rehabilitation and photoprotection (glare/UV control) to maximize residual function and daily safety. Photoprotection is mechanistically rational given the light/oxidative-stress component, though unproven for CORD10 specifically.

**Immunization / public-health / environmental interventions.** Not applicable (non-infectious, non-environmental Mendelian disease).

**Counseling.** Genetic counseling is central — discussing inheritance (AD vs AR per allele), recurrence risk, variable expressivity, and reproductive options. In consanguineous communities, consanguinity education and carrier screening are especially relevant ([PMID: 35551639](https://pubmed.ncbi.nlm.nih.gov/35551639/)).

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** *SEMA4A* is conserved across mammals. Mouse *Sema4a* (NCBI Gene ID 20352) is the principal disease-modeling ortholog; orthologs exist in rat, zebrafish, and other vertebrates (NCBI Taxonomy: *Mus musculus* txid10090; *Homo sapiens* txid9606).

**Natural disease in other species.** No well-characterized naturally-occurring *SEMA4A* cone-rod dystrophy is documented in companion animals or wildlife (no OMIA entry identified for *SEMA4A* CRD). The disease is studied via engineered models rather than spontaneous animal disease.

**Comparative biology.** The RPE endosomal-sorting / photoreceptor-support function of SEMA4A appears evolutionarily conserved, since mouse knockout and knock-in faithfully reproduce human retinal degeneration — evidence that the disease mechanism is conserved across mammals.

**Transmission.** Not applicable — non-communicable, non-zoonotic genetic disease.

---

## 15. Model Organisms

**Mammalian (mouse) — the principal and best-validated models.**

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| *Sema4A*−/− knockout | Null | Severe retinal degeneration by 14 wk; ONL reduced to a single photoreceptor row; thin/disorganized OPL; RPE depigmentation; attenuated vessels; both rod & cone ERG compromised | [PMID: 15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/) |
| *Sema4A* F350C knock-in | Patient-allele knock-in | Reproduces retinal degeneration; protein mislocalization; impaired endosomal sorting | [PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/) |
| *Sema4A* D345H knock-in | Patient-allele knock-in | **No** retinal degeneration (allele-specific) | [PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/) |
| *Sema4A* R713Q knock-in | Patient-allele knock-in | **No** retinal degeneration | [PMID: 23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/) |

**In vitro / cellular.** **RPE cell systems** (e.g., ARPE-19) were used to define the Rab11/FIP2 endosomal-sorting function and prosaposin/retinoid-sorting switch, and to show PACAP-induced SEMA4A up-regulation ([PMID: 22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/); [PMID: 25515530](https://pubmed.ncbi.nlm.nih.gov/25515530/)). Patient-derived iPSC-RPE is an emerging platform (demonstrated for other IRD genes, e.g., RLBP1; [PMID: 39385467](https://pubmed.ncbi.nlm.nih.gov/39385467/)).

**Phenotype recapitulation.** The mouse models recapitulate the core human disease — **progressive degeneration of both cone and rod photoreceptors** with RPE involvement — and critically demonstrate **allele specificity** (only F350C, not D345H or R713Q, caused degeneration in mice), a caveat for interpreting human genotype-phenotype correlations.

**Applications.** These models established the loss-of-function mechanism (RPE endosomal sorting), enabled structural modeling of the pathogenic residue, and provided **proof-of-concept gene-therapy rescue** (AAV *Sema4A*), directly informing therapeutic strategy.

**Limitations.** Mouse retinas lack a macula/fovea (the cone-rich region central to human CRD), so the central-vision aspects of CORD10 are not modeled. Allele discordance (D345H pathogenic in humans but not in the mouse knock-in) highlights species/genetic-background differences.

**Resources:** MGI (*Sema4a*), IMPC/IMSR for alleles; Cellosaurus/ATCC for ARPE-19.

---

## Mechanistic Model / Interpretation

CORD10 is best understood as a **non-cell-autonomous, trafficking-based loss-of-function retinopathy**: the gene defect acts in the **RPE**, but the cells that die are the **photoreceptors** the RPE is supposed to sustain. SEMA4A is a molecular "switch operator" on the RPE's Rab11/FIP2 recycling-endosome platform, toggling cargo between two survival-critical destinations depending on cellular stress — exosomal prosaposin secretion (anti-apoptotic, under oxidative/light stress) versus retinoid-protein sorting for 11-cis-retinal regeneration (visual cycle, at baseline). A Sema-domain missense mutation misfolds and mislocalizes the protein, disabling the switch. The retina thus suffers a **double hit**: chronic chromophore shortfall plus loss of stress-protection, converging on photoreceptor apoptosis. Cones, concentrated in the metabolically demanding central macula, decompensate first, giving the cone-rod clinical sequence.

The therapeutic corollary is clean: because the defect is loss of function and the pathway is restorable, **replacing functional SEMA4A rescues the phenotype** — proven in two independent mouse genotypes. This makes CORD10 a strong candidate for AAV gene augmentation, with CRISPR editing reserved for any dominant allele.

---

## Evidence Base

| PMID | Study (abbrev.) | Role in this report |
|---|---|---|
| [16199541](https://pubmed.ncbi.nlm.nih.gov/16199541/) | Novel SEMA4A mutations in retinal degeneration | **Establishes *SEMA4A* as causal gene**; identifies p.D345H, p.F350C in Sema domain |
| [23360997](https://pubmed.ncbi.nlm.nih.gov/23360997/) | Point mutation in Semaphorin 4A; defective endosomal sorting | **Mechanism + gene-therapy rescue**; F350C mislocalization; allele specificity |
| [22465952](https://pubmed.ncbi.nlm.nih.gov/22465952/) | Endosomal sorting by Sema4A in RPE supports photoreceptor survival | **Defines RPE Rab11/FIP2 sorting**, prosaposin switch, 11-cis-retinal regeneration |
| [15277503](https://pubmed.ncbi.nlm.nih.gov/15277503/) | Severe retinal degeneration with disruption of Sema4A | **Knockout phenotype**; rod+cone compromise; retinal histology |
| [21595947](https://pubmed.ncbi.nlm.nih.gov/21595947/) | Neuroimmune semaphorins 4A and 4D | SEMA4A receptor network (Tim-2, CD72, PlexinB1/D1); pleiotropy |
| [25515530](https://pubmed.ncbi.nlm.nih.gov/25515530/) | Up-regulation of SEMA4A in RPE by PACAP | SEMA4A expression/regulation in human RPE |
| [42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/) | CRISPR strategies for cone-rod dystrophy and achromatopsia | Therapeutic landscape; editing for dominant alleles |
| [36011402](https://pubmed.ncbi.nlm.nih.gov/36011402/) | IRD in Southeastern US | Epidemiology: CRD ~8% of IRDs |
| [35551639](https://pubmed.ncbi.nlm.nih.gov/35551639/) | North African IRD/ION families | Consanguinity (76.1%) and founder effects |
| [29555955](https://pubmed.ncbi.nlm.nih.gov/29555955/) | 251 macular/cone-rod dystrophy patients | *SEMA4A* as candidate genotype-phenotype correlation |
| [41769936](https://pubmed.ncbi.nlm.nih.gov/41769936/) | AAV RdCVF/RdCVFL for RP | Gene-independent cone-protection strategy (PRODYGY trial) |
| [40114034](https://pubmed.ncbi.nlm.nih.gov/40114034/) | Asian IRD diagnostic yield | CRD harder to diagnose (heterogeneous) |
| [33706576](https://pubmed.ncbi.nlm.nih.gov/33706576/); [42343915](https://pubmed.ncbi.nlm.nih.gov/42343915/); [9663233](https://pubmed.ncbi.nlm.nih.gov/9663233/) | KCNV2 CDSRR; ACBD5; Alström | Differential diagnosis |

**Evidence-type summary:** Human clinical/genetic (16199541, 29555955, epidemiology papers); model organism (23360997, 15277503); in vitro/cellular (22465952, 25515530); computational/structural modeling (23360997). The causal gene, mechanism, and gene-therapy rescue are supported by **direct, convergent human-genetic + model-organism + cell-biology evidence**.

---

## Limitations and Knowledge Gaps

1. **Small human evidence base.** *SEMA4A* CORD10 rests largely on the original family report plus candidate findings; there is no large CORD10 patient cohort, so **penetrance, expressivity, natural-history rate, and per-phenotype frequencies are not precisely quantified**.
2. **Allele discordance.** p.D345H is pathogenic in humans but did **not** cause degeneration in the mouse knock-in, while F350C did — leaving uncertainty about the pathogenic mechanism of non-F350C alleles and about human-mouse translatability.
3. **Inheritance ambiguity.** Both dominant and recessive reports exist; the dose-dependence and dominant-vs-recessive behavior of specific alleles are not fully resolved, which directly affects therapeutic choice (augmentation vs editing).
4. **No CORD10-specific omics.** No transcriptomic/proteomic/metabolomic/single-cell datasets specific to CORD10 patients were identified.
5. **No CORD10-specific clinical imaging/ERG series or QoL data** — phenotype characteristics are extrapolated from the CRD class and mouse data.
6. **Therapeutics are preclinical.** Gene-augmentation rescue is mouse-only; no human trial for *SEMA4A*.

---

## Proposed Follow-up Experiments / Actions

1. **Variant functional classification.** Systematically test each reported *SEMA4A* allele (D345H, F350C, R713Q, and any new variants) in human iPSC-RPE for trafficking/localization and prosaposin/retinoid-sorting phenotypes to resolve dominant-vs-recessive and loss-vs-dominant-negative behavior — the key branch point for therapy selection.
2. **Patient registry & natural-history study.** Aggregate *SEMA4A* cases via GeneMatcher/IRD consortia to quantify onset, progression rate, penetrance, expressivity, and genotype-phenotype correlation with longitudinal OCT/ERG.
3. **AAV-*SEMA4A* dose-ranging & window study.** Define the therapeutic time window and vector/promoter (RPE-specific) for augmentation in F350C knock-in mice, as IND-enabling work toward a first-in-human trial.
4. **CRISPR allele-ablation proof-of-concept** for any confirmed dominant *SEMA4A* allele, benchmarking editing efficiency and off-target profile.
5. **Mechanistic completion.** Directly test, in RPE models and in vivo, whether prosaposin supplementation or antioxidant/photoprotective interventions slow degeneration — validating the oxidative-stress branch as a druggable, mutation-agnostic target.
6. **Structural biology.** Solve/model the SEMA4A Sema-domain structure with pathogenic residues to explain allele-specific severity and guide variant interpretation.

---

*Report compiled from 9 confirmed findings and 22 reviewed papers over a 5-iteration autonomous investigation. Primary evidence anchors: PMID 16199541 (causal gene), PMID 23360997 (mechanism + rescue), PMID 22465952 (RPE sorting pathway), PMID 15277503 (knockout phenotype).*


## Artifacts

- [OpenScientist final report](Cone-rod_Dystrophy_10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cone-rod_Dystrophy_10-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012464` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cone-rod dystrophy 10**
- `HP:0000613` (1 mention) - the report calls it "Symptom"; HP calls it **Photophobia**
- `HP:0000551` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Color vision defect**
- `HP:0000662` (1 mention) - the report calls it "Symptom"; HP calls it **Nyctalopia**
- `HP:0000512` (2 mentions) - the report calls it "Lab/functional"; HP calls it **Abnormal electroretinogram**
- `HP:0007843` (1 mention) - the report calls it "Sign"; HP calls it **Attenuation of retinal blood vessels**
- `UBERON:0002423` (1 mention) - the report calls it "macula"; UBERON calls it **hepatobiliary system**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000573` (2 mentions) - the report calls it "cone photoreceptors"; CL calls it **retinal cone cell**, and lists "cone" among its other names
- `CL:0000604` (2 mentions) - the report calls it "rod photoreceptors"; CL calls it **retinal rod cell**, and lists "rod" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.