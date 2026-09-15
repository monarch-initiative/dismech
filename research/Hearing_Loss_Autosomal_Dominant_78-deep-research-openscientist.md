---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T18:52:51.398625'
end_time: '2026-09-03T19:06:39.707112'
duration_seconds: 828.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing loss, autosomal dominant 78 (DFNA78, SLC12A2-related)
  mondo_id: MONDO:0033665
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
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 10
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001270
    reported_labels:
    - Occasional
    ontology_label: Motor delay
  - term_id: HP:0000360
    reported_labels:
    - Not systematically reported
    ontology_label: Tinnitus
  - term_id: UBERON:0002429
    reported_labels:
    - Tissue/cell level:** cochlear **lateral wall / stria vascularis
    ontology_label: cervical lymph node
  labels_variant: 1
  unresolvable_prefixes:
  - Orphanet
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hearing_Loss_Autosomal_Dominant_78-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hearing_Loss_Autosomal_Dominant_78-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing loss, autosomal dominant 78 (DFNA78, SLC12A2-related)
- **MONDO ID:** MONDO:0033665 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing loss, autosomal dominant 78 (DFNA78, SLC12A2-related)** covering all of the
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

# Autosomal Dominant Hearing Loss 78 (DFNA78, SLC12A2-related) — Comprehensive Disease Report

*Prepared as a disease knowledge-base entry. Evidence types are flagged as [human clinical], [model organism], [in vitro], or [computational]. Primary citations are given as PMIDs.*

---

## Summary / Consensus Answer

DFNA78 is a rare, autosomal dominant, non-syndromic sensorineural hearing loss (frequently accompanied by bilateral vestibular areflexia) caused by heterozygous variants in **SLC12A2**, the gene encoding the secretory Na⁺-K⁺-2Cl⁻ cotransporter **NKCC1**. The pathogenic variants cluster in **exon 21 (or its 3′ splice site)**, a region present almost exclusively in the cochlea-specific NKCC1 isoform that is required to maintain the K⁺-rich endolymph and endocochlear potential that drive hair-cell mechanotransduction. Reduced/dysfunctional cotransport disrupts endolymph homeostasis, leading to hair-cell dysfunction and hearing/vestibular loss. Management is supportive (hearing aids, cochlear implantation, vestibular rehabilitation); no disease-specific pharmacotherapy exists.

---

## 1. Disease Information

**Overview.** DFNA78 ("Deafness, autosomal dominant 78") is a Mendelian sensorineural hearing loss (SNHL) caused by heterozygous *SLC12A2* variants. It was first delineated in 2020 [human clinical; PMID 32294086; 32658972]. The phenotype is congenital-to-early-onset, bilateral SNHL, often severe-to-profound, and frequently with **bilateral vestibular areflexia** (hence sometimes described as a cochleovestibular defect) [PMID 32658972; 40503591].

> "In 2020, heterozygous variants in SLC12A2 were identified as a cause of non-syndromic deafness associated with vestibular areflexia (DFNA78; MIM 619081)." — PMID 40503591

**Key identifiers** (verified via OLS4/MONDO, 2026-09-03).
- **OMIM:** #619081 (Deafness, autosomal dominant 78)
- **Gene OMIM:** SLC12A2 *600840*
- **MONDO:** **MONDO:0033665** ("hearing loss, autosomal dominant 78")
- **DOID:** DOID:0112159; **GARD:** 0018156; **MedGen:** C5436768 (CUI 1777362); **UMLS:** C5436768
- **Orphanet:** *No dedicated DFNA78 ORPHAcode* (MONDO records no Orphanet xref); clinically grouped under autosomal dominant non-syndromic sensorineural hearing loss.
- **ICD-11:** AB52 Sensorineural hearing impairment (bilateral, AB52.0); **ICD-10:** H90.3/H90.5
- **MeSH:** "Hearing Loss, Sensorineural" (D006319); "Hearing Loss, Bilateral"
- **HGNC gene:** HGNC:10911 (SLC12A2); **NCBI Gene:** 6558; **Ensembl:** ENSG00000064651; **UniProt:** P55011 (NKCC1)

**Synonyms / alternative names:** DFNA78; deafness, autosomal dominant 78; SLC12A2-related autosomal dominant deafness; NKCC1-related hearing loss; non-syndromic sensorineural hearing loss with vestibular areflexia. **Distinct allelic disorders** (same gene, different phenotype/inheritance): **Delpire-McNeill syndrome** — neurodevelopmental disorder, MONDO:0033667, OMIM #619083, Orphanet:633024 [PMID 32658972]; **Kilquist syndrome** — autosomal recessive multisystem disorder, MONDO:0033664, OMIM #619080, Orphanet:633021 [PMID 30740830].

**Data source type:** Aggregated disease-level knowledge derived from a small number of published case reports/families and functional studies (not EHR-derived at scale). Fewer than ~20 unrelated affected individuals/families are described to date.

---

## 2. Etiology

**Primary cause — genetic.** DFNA78 is a monogenic disorder caused by heterozygous, usually dominantly-inherited or de novo, variants in *SLC12A2* [human clinical; PMID 32294086; 32658972]. There is **no environmental or infectious cause**; environmental agents are irrelevant to the primary etiology.

**Genetic risk factors.**
- Causal variants: missense and splice-site variants restricted to **exon 21 / its 3′ splice site** of the cochlea-specific NKCC1 isoform [PMID 32294086]. ClinVar additionally lists DFNA78-annotated truncating alleles **c.2977G>T (p.Glu993Ter)** [Pathogenic] and **c.869dup (p.Val291fs)** [Likely pathogenic] [computational; ClinVar 2026].
- No known common susceptibility loci or modifier genes have been established for DFNA78 (the disorder is monogenic and ultra-rare).

**Environmental risk / protective factors.** None established as causal or modifying for DFNA78. General SNHL aggravators (noise, ototoxic aminoglycosides, loop diuretics) are theoretical concerns because loop diuretics (bumetanide/furosemide) inhibit NKCC1; avoidance is prudent but not evidence-based for this specific disease.

**Gene–environment interactions.** Not characterized. Given the ion-transport mechanism, ototoxic drugs that further impair endolymph homeostasis (loop diuretics, aminoglycosides, cisplatin) could plausibly worsen hearing, but no formal GxE data exist.

---

## 3. Phenotypes

Core phenotype = **bilateral sensorineural hearing loss ± bilateral vestibular areflexia**, non-syndromic.

| Phenotype | Type | Onset | Severity | Progression | Frequency | HPO term |
|---|---|---|---|---|---|---|
| Sensorineural hearing loss | Clinical sign / lab (audiometry) | Congenital–early childhood (some later/progressive) | Moderate → profound | Stable or slowly progressive | ~100% (defining) | **HP:0000407** Sensorineural hearing impairment; **HP:0008619** Bilateral SNHL; **HP:0008527** Congenital SNHL; **HP:0000408** Progressive SNHL |
| Vestibular areflexia / dysfunction | Clinical sign (caloric/vHIT) | Congenital–early | Variable | Stable | Frequent (subset; reported in the cochleovestibular families) | **HP:0410057** Vestibular areflexia; **HP:0002321** Vertigo; **HP:0001336** (imbalance) |
| Delayed motor milestones (2° to vestibular loss) | Physical | Infancy | Mild | Non-progressive | Occasional | HP:0001270 |
| Tinnitus | Symptom | Variable | Mild-moderate | Variable | Not systematically reported | HP:0000360 |

**Explicitly NOT part of DFNA78** (these distinguish it from the recessive/de-novo allelic disorders): intellectual disability, developmental delay, gastrointestinal dysmotility, absent salivation/lacrimation, respiratory abnormalities, microcephaly — these occur in **Kilquist syndrome** (biallelic LoF) and **Delpire-McNeill** (de novo NDD) [PMID 30740830; 32658972; 33500540].

**Quality-of-life impact.** SNHL impairs speech/language acquisition, education, and communication; vestibular areflexia impairs balance, gaze stabilization (oscillopsia), and delays motor development. No DFNA78-specific EQ-5D/SF-36 data; QoL burden inferred from congenital bilateral SNHL literature generally.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SLC12A2* (Solute carrier family 12 member 2), encoding **NKCC1** (Na⁺-K⁺-2Cl⁻ cotransporter 1). HGNC:10911; NCBI Gene 6558; Ensembl ENSG00000064651; UniProt **P55011** (1212 aa); locus **5q23.3** (GRCh38 chr5:128,083,766–128,189,677); canonical transcript ENST00000262461 / NM_001046.3 [computational; gnomAD/UniProt].

**Pathogenic variants.**
- **Type/class:** predominantly **missense** and **splice-site** variants in exon 21 / its 3′ splice acceptor (cochlear isoform) [PMID 32294086]; ClinVar also records truncating (nonsense/frameshift) DFNA78 alleles (p.Glu993Ter; p.Val291fs) [ClinVar].
- **Classification (ACMG/AMP):** the two established DFNA78 alleles are Pathogenic / Likely pathogenic; most other *SLC12A2* variants are VUS [ClinVar 2026].
- **Allele frequency:** private/ultra-rare; absent or singleton in gnomAD (consistent with de novo or small-family dominant transmission).
- **Origin:** **germline** — inherited (dominant families) or **de novo** (sporadic cases) [PMID 32294086; 32658972]. No somatic involvement.
- **Functional consequence:** reduced cotransporter activity — "Cl⁻ influx was significantly decreased in all SLC12A2 variants studied" [in vitro Xenopus oocytes; PMID 32294086]. Because NKCC1 is an obligate **dimer** and heterozygous LoF carriers have normal hearing, DFNA78 missense alleles likely act via **dominant-negative / isoform-specific** loss of endolymph-secreting function rather than simple haploinsufficiency (partly inferred) [PMID 40503591].

> "SLC12A2 functions as a dimer and has several isoforms; only one isoform contains exon 21, and this isoform is almost exclusively expressed in the inner ear/cochlea." — PMID 40503591

**Constraint (gnomAD).** LOEUF 0.60, LoF o/e 0.49 (obs 67/exp 136), lof_z 5.04, **pLI ≈ 0**, missense o/e 0.86 (mis_z 2.32) — i.e., *SLC12A2* is only moderately LoF-constrained and **not classically haploinsufficient**, supporting the non-haploinsufficiency mechanism [computational; gnomAD].

**Modifier genes / epigenetics / chromosomal abnormalities.** None established for DFNA78. (In Kilquist syndrome the causal lesion was a homozygous 22-kb deletion arising via **uniparental isodisomy of chromosome 5** — a large-scale mechanism relevant to the recessive allelic disorder, not DFNA78 [PMID 30740830].)

---

## 5. Environmental Information

Not applicable to disease causation. No environmental toxins, lifestyle factors, or infectious agents are implicated in DFNA78. Theoretical aggravators of any SNHL — noise exposure, aminoglycosides, cisplatin, and **loop diuretics (NKCC1 inhibitors)** — should be minimized as general otoprotective practice, but there is no disease-specific evidence.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous *SLC12A2* variant in the cochlea-specific **exon-21 region** (missense/splice/truncating) **alters NKCC1 in the exon-21 (inner-ear) isoform** [PMID 32294086].
2. The mutant subunit **incorporates into the obligate NKCC1 dimer**, and (inferred) **exerts a dominant-negative / isoform-specific reduction** of cotransport in cochlear secretory epithelium — demonstrated as decreased Cl⁻ influx in vitro [PMID 32294086; dimer/mechanism partly inferred, PMID 40503591].
3. Reduced NKCC1 activity in **stria vascularis marginal cells** (and other lateral-wall cells) **decreases basolateral uptake of Na⁺/K⁺/Cl⁻**, which **results in reduced K⁺ secretion into the endolymph** [model organism; PMID 10369265].
4. Impaired K⁺ secretion **leads to failure of endolymph homeostasis and reduction of the endocochlear potential (EP)** — the driving force for hair-cell transduction currents [PMID 32294086; 17674100].
5. Loss of the K⁺ gradient/EP **results in failure of hair-cell mechano-electrical transduction** ("K⁺ transport is required for the mechano-transduction of auditory stimuli") [PMID 40503591].
6. Chronic endolymph disturbance **leads to structural damage / collapse of the endolymphatic compartment and hair-cell dysfunction** (shown in Slc12a2⁻/⁻ mice) [model organism; PMID 10369265].
7. → **Sensorineural hearing loss**; in parallel, the same defect in **vestibular dark cells** of the labyrinth **results in vestibular hypofunction/areflexia** [PMID 32658972].

**Molecular pathways / biochemistry.** The core defect is an **ion-transport (ion-homeostasis) defect**, not a classical signaling cascade. NKCC1 mediates electroneutral, bumetanide-sensitive Na⁺:K⁺:2Cl⁻ symport (MF **GO:0008511** sodium:potassium:chloride symporter activity). Relevant GO biological processes (UniProt P55011): potassium ion transmembrane transport (**GO:0071805**), chloride transmembrane transport (**GO:1902476**), potassium ion import across plasma membrane (GO:1990573), intracellular potassium ion homeostasis (GO:0030007), cell volume homeostasis (GO:0006884), sensory perception of sound (**GO:0007605**), inner ear morphogenesis (GO:0042472). CHEBI entities: potassium(1+) **CHEBI:29103**, chloride **CHEBI:17996**, sodium(1+) CHEBI:29101; inhibitors bumetanide **CHEBI:3213**, furosemide CHEBI:47426.

**Protein dysfunction.** NKCC1 is a 12-TM cation-chloride cotransporter that assembles as a homodimer; cryo-EM structures reveal ion-binding sites and the dimer interface [in vitro/structural; PMID 36239040; 32081947; 37545407]. Exon-21 variants perturb the C-terminal cytoplasmic domain critical for transport/regulation; recessive alleles also cluster in the C-terminal domain [PMID 33500540]. Consequence = loss/reduction of transport function (± dominant-negative on the dimer).

**Cell types / processes (upstream→downstream).** Upstream: dysfunction of **strial marginal cells (CL:0002516)** and vestibular dark cells (epithelial K⁺ secretion). Downstream: secondary dysfunction/degeneration of **cochlear hair cells (inner CL:0000589; outer CL:0000601)**, vestibular hair cells (CL:0000633), and (later) spiral ganglion neurons (CL:0002253). No inflammation/autoimmunity, apoptosis-driven primary mechanism, or metabolic disorder is implicated in DFNA78.

**Molecular profiling.** NKCC1 immunolocalizes to the basolateral membrane of strial marginal cells; in hereditary-deaf animal cochleae, spatiotemporal loss of SLC12A2 accompanies strial malformation and endolymph collapse [PMID 18093167; 24713161]. No DFNA78-specific transcriptomic/proteomic/metabolomic datasets exist.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **inner ear / cochlea** (UBERON:0001846 inner ear; **UBERON:0001844 cochlea**); vestibular apparatus (semicircular canals UBERON:0001840, otolith organs).
- **Body systems:** special sense (auditory/vestibular) organ of the **nervous/sensory system**. No cardiovascular, GI, renal, or respiratory involvement in DFNA78 (unlike the multisystem recessive disorder).
- **Tissue/cell level:** cochlear **lateral wall / stria vascularis (UBERON:0002429)** secretory epithelium — **strial marginal cells (CL:0002516)**; **organ of Corti (UBERON:0002227)** — inner/outer hair cells (CL:0000589 / CL:0000601); vestibular dark cells and vestibular hair cells (CL:0000633); endolymph compartment (UBERON:0011078).
- **Subcellular level:** **basolateral plasma membrane (GO:0016323)** of secretory epithelial cells (NKCC1 also at apical membrane GO:0016324 in some epithelia); integral membrane transporter.
- **Localization / laterality:** **bilateral** (typically symmetric) cochleovestibular involvement.

---

## 8. Temporal Development

- **Onset:** congenital or early-childhood in most reported cases; some heterozygous families show later-onset/progressive SNHL [PMID 32294086; 32658972]. Pattern is **chronic/insidious** rather than acute.
- **Progression:** ranges from **stable** to **slowly progressive**; severity moderate-to-profound. Vestibular areflexia is generally stable/non-progressive.
- **Course/duration:** **lifelong, non-remitting.** No spontaneous remission; no relapsing-remitting pattern.
- **Critical period:** early identification (newborn hearing screening) and early amplification/cochlear implantation within the first years of life are the key windows for language outcomes.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (DFNA78), including **de novo** occurrences in sporadic cases [PMID 32294086; 32658972].
- **Penetrance:** appears high in reported dominant families (5/5 affected members in the index family) but formal penetrance estimates are unavailable given few families; treat as **likely high but incompletely quantified**.
- **Expressivity:** **variable** (severity and presence of vestibular involvement differ across individuals).
- **Anticipation / germline mosaicism / founder effects:** none reported. Founder alleles not described.
- **Carrier frequency:** not applicable (dominant); *SLC12A2* LoF alleles exist in gnomAD but do not cause DFNA78.
- **Epidemiology:** **ultra-rare**; exact prevalence/incidence unknown. DFNA (autosomal dominant non-syndromic) deafness collectively is a minority of hereditary hearing loss; DFNA78 is among the rarer subtypes with <20 reported families/individuals. No prevalence per 100,000 can be reliably stated.
- **Demographics:** reported across multiple populations (Japanese index families [PMID 32294086]; European/other cohorts [PMID 32658972; 40503591]). **No sex predilection** expected (autosomal). No specific geographic/ethnic clustering established.

---

## 10. Diagnostics

**Clinical/functional tests.**
- **Audiometry** (pure-tone, ABR/auditory brainstem response, OAE, tympanometry): documents bilateral SNHL; OAEs typically absent. LOINC panels for audiometry.
- **Vestibular testing**: video head-impulse test (vHIT), caloric testing, VEMP, rotational chair — reveal vestibular areflexia/hypofunction.
- **Imaging**: MRI/CT of temporal bones — usually **normal inner-ear anatomy** (helps exclude structural/EVA causes); no pathognomonic finding.
- **No blood/urine biomarker** exists; diagnosis is not made by chemistry.

**Genetic testing (diagnostic gold standard).**
- Recommended approach: **hereditary-hearing-loss gene panel** or **whole-exome sequencing (WES)**, with attention to *SLC12A2* including **exon 21 and splice sites** (which may be under-covered/mis-annotated because the pathogenic cochlear isoform differs from the canonical transcript) [PMID 32294086]. WES/WGS with trio analysis is especially useful to detect **de novo** variants [PMID 32658972].
- Single-gene *SLC12A2* testing is appropriate when the phenotype (congenital SNHL + vestibular areflexia, dominant/de novo) is suggestive.
- CMA/karyotype/FISH generally not indicated (point-variant disorder); mtDNA and repeat-expansion testing not relevant.
- **Variant-interpretation caveat:** confirm variant is in the exon-21 cochlear isoform and, ideally, functional confirmation (reduced Cl⁻/transport) supports pathogenicity [PMID 32294086].

**Clinical criteria / differential diagnosis.** No formal diagnostic criteria. Differential includes other non-syndromic SNHL genes (GJB2, SLC26A4/Pendred, MYO7A, TMC1, etc.), and syndromic causes with vestibular involvement (Usher syndrome). The **combination of non-syndromic congenital SNHL with bilateral vestibular areflexia and dominant/de novo inheritance** points toward *SLC12A2*. Distinguish from the allelic **Kilquist** (recessive, multisystem) and **Delpire-McNeill** (NDD) disorders.

**Screening.** Detected via **universal newborn hearing screening** (phenotype), then genetic confirmation; **cascade testing** of at-risk relatives in dominant families.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** DFNA78 is **not life-limiting**; normal life expectancy. Mortality not attributable to the disease. (Contrast with severe multisystem Kilquist syndrome.)
- **Morbidity/disability:** principal morbidity is **communication disability** from bilateral SNHL and **balance impairment/oscillopsia** from vestibular areflexia; motor milestone delay possible in infancy.
- **Disease course:** chronic, lifelong; hearing stable-to-progressive.
- **Recovery potential:** no spontaneous recovery; **functional hearing is recoverable with amplification/cochlear implantation**, and balance improves with vestibular rehabilitation/compensation.
- **Prognostic factors:** degree/onset of hearing loss, timing of intervention (early implantation → better language outcomes), and residual hearing. No molecular prognostic biomarker established.
- **QoL measures:** no DFNA78-specific instruments; general pediatric SNHL QoL tools apply.

---

## 12. Treatment

*No disease-modifying/curative pharmacotherapy exists.* Management is **supportive/rehabilitative**.

- **Amplification / devices:** **hearing aids** for milder loss; **cochlear implantation** for severe-to-profound loss (NCIT: Cochlear Implant C99286; Hearing Aid C99285). Cochlear implants bypass the failed endolymph-dependent transduction by directly stimulating the auditory nerve and are expected to be effective (spiral ganglion typically preserved early).
- **Vestibular rehabilitation** / physical therapy for balance; **speech-language therapy** and early-intervention/educational support.
- **Pharmacotherapy:** none specific. Note NKCC1 is the target of **loop diuretics (bumetanide CHEBI:3213, furosemide)** — these *inhibit* NKCC1 and are potentially ototoxic, so they are **not therapeutic** and are best avoided. Bumetanide is being studied in NKCC1-related neurodevelopmental/GABA-polarity contexts [PMID 26955005; 38950809], but this is **not applicable to restoring cochlear NKCC1 function** in DFNA78.
- **Advanced/experimental:** No approved gene therapy, ASO, or cell therapy for DFNA78. Given the dominant/likely dominant-negative mechanism, allele-selective silencing (siRNA/ASO) or gene editing are conceptually attractive future strategies but remain **preclinical/theoretical**. No registered clinical trials (ClinicalTrials.gov) target DFNA78 specifically as of this report.
- **Pharmacogenomics:** avoid concomitant ototoxic drugs (aminoglycosides, cisplatin, loop diuretics).

---

## 13. Prevention

- **Primary prevention:** not possible (genetic). **Genetic counseling** for dominant families (50% transmission risk); options include **prenatal testing** and **preimplantation genetic testing (PGT)** for known familial variants.
- **Secondary prevention / early detection:** **universal newborn hearing screening** enables early diagnosis and intervention; **cascade genetic testing** of relatives.
- **Tertiary prevention:** early amplification/cochlear implantation and vestibular rehabilitation to prevent language/developmental sequelae; avoidance of ototoxic exposures and noise to preserve residual hearing.
- **Immunization / public-health / environmental measures:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Slc12a2* is highly conserved. Mouse **Slc12a2** (NCBI Gene 20496; MGI:101924; NCBI Taxon 10090); rat *Slc12a2* (Taxon 10116); zebrafish *slc12a2* (Taxon 7955). Human ortholog UniProt P55011.
- **Natural disease in animals:** Deafness/inner-ear dysfunction from *Slc12a2* disruption is a **model-organism phenomenon** (targeted mutants); no well-known spontaneous companion-animal DFNA78 equivalent is catalogued (OMIA lists NKCC1/SLC12A2 biology but no established dominant deafness breed disorder).
- **Comparative biology:** NKCC1's role in endolymph/K⁺ cycling is conserved across mammals (mouse, gerbil, rat, guinea pig) and underlies the shared deafness phenotype [PMID 10369265; 18093167]. Evolutionary conservation of the endolymph-secretion mechanism is strong.
- **Transmission:** none (non-infectious, non-zoonotic).

---

## 15. Model Organisms

- **Mouse — *Slc12a2* (NKCC1) knockout** [model organism; PMID 10369265]: constitutive KO mice are **deaf**, display classic **shaker/waltzer** circling/head-bobbing (vestibular dysfunction), and show **collapse of the endolymphatic compartment** and strial/inner-ear structural damage from reduced endolymph secretion. This recapitulates the core DFNA78 mechanism (endolymph/EP failure) and the cochleovestibular phenotype.
  > "absence of functional co-transporter leads to structural damages in the inner ear consistent with a decrease in endol[ymph]" — PMID 10369265
- **Allelic mouse models / EP studies:** heterozygous *Nkcc1* deletion causes **progressive, age-dependent hearing loss** with EP decline; combined manipulation with Na,K-ATPase isoforms modulates EP and hearing, underscoring NKCC1's role in EP generation [PMID 17674100].
- **Other species:** guinea-pig hereditary-deafness models show spatiotemporal loss of strial K⁺-transport proteins including SLC12A2 with endolymph collapse [PMID 18093167].
- **Model types available:** constitutive knockout; heterozygous; the biology also supports conditional/knock-in and humanized approaches (MGI/IMPC resources for *Slc12a2*).
- **Recapitulation & limitations:** KO models faithfully reproduce **deafness + vestibular dysfunction + endolymph collapse**, but represent **complete loss of function/biallelic** biology (closer to Kilquist) rather than the human **heterozygous, isoform-/exon-21-specific dominant** mechanism; a precise DFNA78 exon-21 knock-in would better model the dominant-negative disease. No DFNA78 iPSC/organoid model is yet published.
- **Databases:** MGI (Slc12a2), IMPC/IMSR, Alliance of Genome Resources, ZFIN (slc12a2), RGD.

---

## Supported vs Refuted Hypotheses

**Supported:**
- DFNA78 is caused by heterozygous *SLC12A2* variants clustered in the cochlea-specific exon-21 region [PMID 32294086].
- Mechanism = impaired NKCC1-mediated K⁺ secretion → endolymph/EP failure → hair-cell transduction failure → SNHL + vestibular areflexia [PMID 10369265; 32294086; 40503591].
- *SLC12A2* is an allelic series (dominant DFNA78 vs recessive Kilquist vs de novo Delpire-McNeill NDD) [PMID 30740830; 32658972; 33500540].

**Refuted / disfavored:**
- **Haploinsufficiency as the DFNA78 mechanism** — disfavored: gnomAD shows *SLC12A2* is not classically haploinsufficient (pLI≈0) and heterozygous LoF carriers/patients have normal hearing; DFNA78 arises from isoform-specific missense/splice (dominant-negative) alleles [PMID 40503591; gnomAD].
- Environmental/infectious causation — not applicable.

## Limitations & Future Directions

- Very small number of reported families → penetrance, expressivity, prevalence, natural-history, and audiometric-progression data are limited.
- The dominant-negative mechanism is **inferred** from the dimeric structure and genotype–phenotype correlation; direct in-vivo proof (exon-21 knock-in models) is lacking.
- No DFNA78-specific omics, iPSC/organoid, or therapeutic-trial data. Future work: exon-21 knock-in mouse, patient iPSC-derived otic organoids, and allele-selective RNA/gene-editing therapeutics.

---

### Key References (PMIDs)
- 32294086 — Mutai et al. 2020: exon-21 SLC12A2 variants cause hereditary hearing loss (foundational DFNA78).
- 32658972 — McNeill et al. 2020: SLC12A2 variants cause NDD or cochleovestibular defect (vestibular areflexia).
- 40503591 — Ludin et al. 2025: de novo SLC12A2 variant, congenital HL + vestibular areflexia; isoform/exon-21 review.
- 30740830 — Macnamara et al. 2019: Kilquist syndrome (biallelic SLC12A2 deletion).
- 33500540 — Bilal Shamsi et al. 2021: autosomal recessive SLC12A2 disease; C-terminal clustering.
- 10369265 — Delpire et al. 1999: Slc12a2-KO mouse deafness/imbalance, endolymph collapse.
- 17674100 — Diaz et al. 2007: NKCC1/Na,K-ATPase, endocochlear potential and hearing.
- 18093167 — Jin et al. 2008: loss of strial K⁺-transport proteins (incl. SLC12A2) in hereditary deafness.
- 36239040 / 32081947 / 37545407 — human NKCC1 cryo-EM structures.
- 33345190 / 37399495 — reviews: NKCC1 as a human disease-causing ion transporter.
- 26955005 / 38950809 — SLC12A2/NKCC1 GABA-polarity and bumetanide (neuro contexts; not DFNA78 therapy).


## Artifacts

- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_78-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_78-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001270` (1 mention) - the report calls it "Occasional"; HP calls it **Motor delay**
- `HP:0000360` (1 mention) - the report calls it "Not systematically reported"; HP calls it **Tinnitus**
- `UBERON:0002429` (1 mention) - the report calls it "Tissue/cell level:** cochlear **lateral wall / stria vascularis"; UBERON calls it **cervical lymph node**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016323` (1 mention) - the report calls it "Subcellular level:** **basolateral plasma membrane"; GO calls it **basolateral plasma membrane**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `MGI`.