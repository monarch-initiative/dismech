---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T08:42:40.299789'
end_time: '2026-09-06T09:05:01.422741'
duration_seconds: 1341.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Paraneoplastic Cerebellar Degeneration
  mondo_id: MONDO:0044877
  category: Complex
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
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 21
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:27606347
  - PMID:35871640
  - PMID:7788964
  relevance_assessed: 36
  on_topic: 25
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 10
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0012310
    reported_labels:
    - CSF lymphocytic pleocytosis
    ontology_label: Abnormal monocyte count
  - term_id: HP:0032101
    reported_labels:
    - Oligoclonal bands / elevated IgG index
    ontology_label: Unusual infection
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Paraneoplastic_Cerebellar_Degeneration-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Paraneoplastic_Cerebellar_Degeneration-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paraneoplastic Cerebellar Degeneration
- **MONDO ID:** MONDO:0044877 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Paraneoplastic Cerebellar Degeneration** covering all of the
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

# Paraneoplastic Cerebellar Degeneration (PCD): A Comprehensive Disease Characteristics Report

**MONDO ID:** MONDO:0044877 · **Category:** Complex (immune-mediated, non-Mendelian)
**Report type:** Disease knowledge-base synthesis from literature (69 papers reviewed; 12 confirmed findings)
**Evidence base:** Human clinical cohorts and case series, model-organism studies, in vitro immunology

---

## Summary

Paraneoplastic cerebellar degeneration (PCD) is a rare, immune-mediated, subacute pancerebellar syndrome that arises as a remote effect of cancer. It is **not** a genetic disease in the Mendelian sense; instead, the initiating lesion is a malignancy that **ectopically expresses a neuronal ("onconeural") antigen** normally restricted to cerebellar Purkinje cells. This aberrant expression breaks immune tolerance in genetically predisposed (HLA Class II) hosts, triggering an anti-tumor immune response that cross-reacts with the cerebellum. The dominant effector mechanism is **cytotoxic CD8+ T-cell-mediated destruction of Purkinje cells**, with autoantibodies serving primarily as diagnostic biomarkers rather than the direct cause of neuronal death (for the intracellular-antigen subtypes). The clinical result is subacute (weeks-to-months) progressive gait and limb ataxia, dysarthria, nystagmus, and dizziness, typically plateauing within ~6 months, often leaving patients severely and irreversibly disabled.

The single most important organizing principle to emerge from this investigation is the **antigen-location prognosis rule**: antibodies against *intracellular* antigens (anti-Yo/CDR2, anti-Hu/ANNA-1, Ma2) mark a T-cell-driven, largely irreversible process with poor neurological outcomes, whereas antibodies against *cell-surface* antigens (anti-DNER/Tr, anti-mGluR1) mark a more antibody-mediated, treatment-responsive process. Anti-Yo (PCA-1), directed against CDR2/CDR2L, is the most common variant, occurring almost exclusively in women with gynecologic or breast cancer, and carries a dismal prognosis (≈84% of survivors unable to walk unassisted). Anti-Tr/DNER PCD, by contrast, occurs mostly in middle-aged men with Hodgkin lymphoma and is more treatable.

Management rests on two pillars applied urgently: **prompt tumor detection and treatment** (antibody-guided screening, with FDG-PET/CT central when conventional imaging is negative) and **immunotherapy** (corticosteroids, IVIG, plasma exchange, cyclophosphamide, rituximab). Good outcomes correlate with early diagnosis, low disability at presentation (mRS <3), absence of metastasis, and combined immunotherapy plus tumor-directed therapy. An emerging iatrogenic trigger is the class of **immune checkpoint inhibitors (ICIs)**, which can unmask or amplify pre-existing onconeural immunity. Population data indicate PCD is the second most common paraneoplastic neurological syndrome (≈28% of PNS), against an overall PNS incidence of ~0.89/100,000 person-years.

---

## Section 1 — Disease Information

**Overview.** PCD is an autoimmune cerebellar syndrome triggered by an underlying (often occult) malignancy. It belongs to the broader family of paraneoplastic neurological syndromes (PNS) and immune-mediated cerebellar ataxias (IMCAs). The typical presentation is "the subacute development of pancerebellar deficits with a clinical plateau within 6 months" ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)).

**Key identifiers.**
- **MONDO:** MONDO:0044877
- **MeSH:** Paraneoplastic Cerebellar Degeneration
- **ICD-10:** G13.1 (Systemic atrophy primarily affecting central nervous system in neoplastic disease) / D48.9 with paraneoplastic manifestation
- **Orphanet:** Paraneoplastic cerebellar degeneration (rare neurological PNS)
- **OMIM:** Not applicable — PCD is not a heritable Mendelian disorder; no OMIM disease entry (relevant onconeural genes have Gene OMIM entries, e.g., *CDR2*).

**Synonyms / alternative names.** Paraneoplastic cerebellar degeneration; subacute cerebellar degeneration (paraneoplastic); anti-Yo/PCA-1 cerebellar ataxia (for that subtype); paraneoplastic cerebellar ataxia; onconeural cerebellar syndrome. Antibody-defined subtypes: PCA-1 (anti-Yo), PCA-Tr (anti-Tr/DNER), ANNA-1 (anti-Hu), ANNA-2 (anti-Ri), PCA-2 (anti-MAP1B).

**Information source type.** This report is derived from **aggregated disease-level resources** — systematic reviews, laboratory serology cohorts (Mayo Clinic, Barcelona), population-based epidemiology, and case series — rather than from individual EHR patient records.

---

## Section 2 — Etiology

**Primary cause.** The causal factor is an **underlying malignancy** that ectopically expresses a neuronal antigen. In anti-Yo disease, "the Yo autoantibodies are directed against the Yo antigens, aberrantly overexpressed by tumor cells with frequent somatic mutations and gene amplifications" ([PMID: 38494293](https://pubmed.ncbi.nlm.nih.gov/38494293/)). The disease is therefore fundamentally a **cancer-triggered autoimmune** process, not genetic, environmental (toxic), or infectious in origin.

**Tumor-type risk factors (antibody-dependent).**
- Anti-Yo → gynecologic (ovarian, endometrial) and breast carcinoma; 96% female, 82% gynecologic cancer ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)).
- Anti-Tr/DNER → Hodgkin lymphoma, middle-aged males ([PMID: 34817790](https://pubmed.ncbi.nlm.nih.gov/34817790/)).
- Anti-Hu, CV2/CRMP5, PCA-2/MAP1B, ZIC4 → small-cell lung cancer (SCLC), often in smokers.
- Anti-Ma2 → testicular germ-cell tumors (young men <50), also lung/breast.

**Genetic risk factors.** Host susceptibility is conferred by **HLA Class II** haplotypes rather than causal coding mutations. High-resolution typing of 40 anti-Yo cases identified protective haplotypes (DPA1\*01:03~DPB1\*04:01, OR=0, p=0.0008) and an ovarian-cancer-specific susceptibility haplotype (DRB1\*13:01~DQA1\*01:03~DQB1\*06:03, OR=5.4, p=0.0016), indicating "differential genetic susceptibility to anti-Yo per cancer and with a primary HLA Class II involvement" ([PMID: 29306402](https://pubmed.ncbi.nlm.nih.gov/29306402/)).

**Environmental / lifestyle risk factors.** Tobacco smoking is a strong indirect risk factor via SCLC-associated subtypes (anti-Hu, CRMP5). No direct toxic, occupational, or infectious cause of PCD itself is established.

**Iatrogenic trigger.** Immune checkpoint inhibitors (anti-PD-1/PD-L1/CTLA-4) are an emerging cause; they can "amplify pre-existing onconeural immunity" ([PMID: 42442848](https://pubmed.ncbi.nlm.nih.gov/42442848/)).

**Protective factors.** The only clearly documented protective factors are the HLA Class II protective haplotypes above. No dietary or lifestyle protective factors are established.

**Gene–environment interaction.** The model is: a tumor (environmental/somatic event) expressing an onconeural antigen, in a host carrying a permissive/susceptible HLA Class II genotype, produces tolerance breakdown. Molecular mimicry directs the specificity, and co-signaling molecules (checkpoint pathways) modulate the strength — a concept reinforced by the ICI-triggered cases ([PMID: 39052041](https://pubmed.ncbi.nlm.nih.gov/39052041/)).

---

## Section 3 — Phenotypes

The core phenotype is a **subacute, progressive pancerebellar syndrome** (HPO: HP:0001251 Ataxia; HP:0002070 Limb ataxia; HP:0002066 Gait ataxia).

| Phenotype | HPO term | Type | Frequency / notes |
|---|---|---|---|
| Gait ataxia | HP:0002066 | Clinical sign | Near-universal; often presenting feature |
| Limb ataxia / dysmetria | HP:0002070 / HP:0001310 | Clinical sign | Very common |
| Dysarthria | HP:0001260 | Clinical sign | Common |
| Nystagmus (incl. downbeat) | HP:0000639 | Clinical sign | Common; downbeat characteristic |
| Vertigo / dizziness | HP:0002321 | Symptom | Prodromal in ~two-thirds of anti-Yo patients ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)) |
| Diplopia / oscillopsia | HP:0000651 / HP:0011495 | Symptom | Frequent |
| Truncal instability | HP:0002078 | Clinical sign | Common |
| CSF lymphocytic pleocytosis | HP:0012310 | Lab abnormality | Frequent, inflammatory CSF |
| Oligoclonal bands / elevated IgG index | HP:0032101 | Lab abnormality | Frequent |

**Characteristics.** Onset is **adult/late-adult** (median age ~60 for anti-Yo, ~68 in the population PNS cohort). Course is **subacute and progressive** over weeks to months, with "a clinical plateau within 6 months" ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)). Severity is typically **severe** for intracellular-antigen subtypes: despite treatment, 84% of anti-Yo survivors are unable to walk unassisted at follow-up ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)). "Vertigo and imbalance can be present early in the disease course in about two thirds of patients, as a prodromal phase" ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)).

**Quality-of-life impact.** Profound — most patients with intracellular-antigen PCD become wheelchair-dependent, non-ambulatory, and dependent for activities of daily living, with dysarthria impairing communication. Surface-antigen subtypes may recover substantially.

**Extracerebellar features.** Rare in isolated anti-Tr/DNER PCD (8%) ([PMID: 34817790](https://pubmed.ncbi.nlm.nih.gov/34817790/)); anti-Hu and anti-Ma2 more often present with multifocal encephalomyelitis, limbic/brainstem involvement, and peripheral neuropathy.

---

## Section 4 — Genetic / Molecular Information

PCD has **no causal germline disease gene**. The relevant molecules are the **onconeural target antigens** and the **host HLA Class II** susceptibility loci.

**Onconeural antigens (target autoantigens).**

| Antibody (alias) | Target antigen / gene | Antigen location | Typical tumor |
|---|---|---|---|
| Anti-Yo (PCA-1) | CDR2 / CDR2L | Intracellular (cytoplasm) | Ovarian, breast |
| Anti-Tr (PCA-Tr) | DNER (Delta/Notch-like EGF-related receptor) | **Cell surface** | Hodgkin lymphoma |
| Anti-Hu (ANNA-1) | HuD / ELAVL family | Intracellular (nuclear) | SCLC |
| Anti-Ri (ANNA-2) | NOVA1/2 | Intracellular (nuclear) | Breast, lung |
| Anti-Ma2 | PNMA2 (Ma2) | Intracellular | Testicular germ-cell |
| Anti-CV2/CRMP5 | CRMP5/DPYSL5 | Intracellular | SCLC, thymoma |
| Anti-PCA-2 | MAP1B | Intracellular | SCLC |
| Anti-mGluR1 | GRM1 (metabotropic glutamate receptor 1) | **Cell surface** | Often non-paraneoplastic / lymphoma |
| Anti-Homer-3 | HOMER3 | Intracellular/postsynaptic | Breast adenocarcinoma |
| Anti-ZIC4 | ZIC4 | Intracellular | SCLC |

The anti-Yo antigen designation and target are established: anti-Yo is "directed against cerebellar degeneration-related protein 2 (CDR2) and CDR2L" and is "the most common variant of paraneoplastic cerebellar degeneration" ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)). Anti-Tr binds "the extracellular domain of DNER" ([PMID: 25745634](https://pubmed.ncbi.nlm.nih.gov/25745634/)).

**Somatic vs germline.** The genetic aberrations are **somatic in the tumor** — "aberrantly overexpressed by tumor cells with frequent somatic mutations and gene amplifications" of the Yo antigen genes ([PMID: 38494293](https://pubmed.ncbi.nlm.nih.gov/38494293/)). There is no germline pathogenic variant driving PCD.

**Modifier genes / functional consequences.** HLA Class II haplotypes modify susceptibility per cancer type ([PMID: 29306402](https://pubmed.ncbi.nlm.nih.gov/29306402/)). Epigenetic and chromosomal abnormality data specific to PCD are not established beyond tumor-level somatic changes.

**HGNC / Gene identifiers:** CDR2 (HGNC:1802), CDR2L (HGNC:14002), ELAVL4/HuD, PNMA2, DPYSL5/CRMP5, MAP1B, GRM1, DNER, HOMER3, ZIC4.

---

## Section 5 — Environmental Information

- **Environmental/toxic factors:** No direct environmental toxin causes PCD. The relevant "environmental" exposure is **tobacco smoke**, acting indirectly by causing SCLC (the tumor substrate for anti-Hu, CRMP5, PCA-2, ZIC4 subtypes).
- **Lifestyle factors:** Smoking (via SCLC). No dietary triggers established.
- **Infectious agents:** None causative. PCD is a paraneoplastic (tumor-driven) autoimmune process, though molecular mimicry conceptually parallels post-infectious immune cerebellar ataxias in the broader IMCA family ([PMID: 39052041](https://pubmed.ncbi.nlm.nih.gov/39052041/)).
- **Iatrogenic:** Immune checkpoint inhibitor therapy (see Sections 2, 6, 12).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **malignancy arises** (e.g., ovarian/breast carcinoma, SCLC, Hodgkin lymphoma) and, through somatic mutation/gene amplification, **ectopically expresses an onconeural antigen** (CDR2/CDR2L, HuD, DNER, Ma2) normally restricted to neurons → *results in* presentation of a neural self-antigen to the immune system in an immunogenic (tumor) context ([PMID: 38494293](https://pubmed.ncbi.nlm.nih.gov/38494293/)).
2. In a **host carrying permissive HLA Class II haplotypes**, this ectopic antigen presentation *leads to* **breakdown of immune self-tolerance** ([PMID: 29306402](https://pubmed.ncbi.nlm.nih.gov/29306402/)).
3. Tolerance breakdown *results in* an **anti-tumor adaptive immune response**: generation of onconeural autoantibodies AND antigen-specific T cells. (For surface antigens, the branch is antibody-dominant; for intracellular antigens, the branch is T-cell-dominant — see branch below.)
4. **Intracellular-antigen branch (Yo, Hu, Ma2):** cross-reactive **cytotoxic CD8+ T lymphocytes (CTLs)** traffic across the blood–brain barrier into the CSF/cerebellum → *leads to* antigen recognition of Purkinje cells → *results in* **CTL-mediated Purkinje cell apoptosis/death** ([PMID: 10632096](https://pubmed.ncbi.nlm.nih.gov/10632096/); [PMID: 9879687](https://pubmed.ncbi.nlm.nih.gov/9879687/)). Antibody alone is **insufficient** to cause degeneration (inferred from failed passive-transfer/immunization models) ([PMID: 7707074](https://pubmed.ncbi.nlm.nih.gov/7707074/); [PMID: 7788981](https://pubmed.ncbi.nlm.nih.gov/7788981/)).
5. **Surface-antigen branch (DNER, mGluR1):** autoantibodies bind the extracellular domain of the target → *results in* receptor dysfunction/internalization that is potentially reversible → more treatment-responsive disease ([PMID: 25745634](https://pubmed.ncbi.nlm.nih.gov/25745634/); [PMID: 41197574](https://pubmed.ncbi.nlm.nih.gov/41197574/)).
6. Purkinje cell loss *leads to* **loss of the sole output neuron of the cerebellar cortex** → *results in* **pancerebellar dysfunction** (gait/limb ataxia, dysarthria, nystagmus).
7. Progressive Purkinje depletion *leads to* **cerebellar atrophy** (radiographically visible late) and, for intracellular subtypes, **irreversible clinical disability** ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)).

```
 Tumor (ectopic onconeural antigen: CDR2/CDR2L, HuD, DNER, Ma2)
            │  (somatic mutation/amplification)
            ▼
 HLA Class II–permissive host  ──►  Tolerance breakdown
            │
   ┌────────┴─────────┐
   ▼                  ▼
 INTRACELLULAR Ag    SURFACE Ag
 (Yo, Hu, Ma2)       (DNER, mGluR1)
   │                  │
 CD8+ CTL response   Antibody binds
 (dominant)          extracellular domain
   │                  │
 Purkinje-cell        Receptor dysfunction
 cytotoxic killing    (± reversible)
   │                  │
 IRREVERSIBLE  ◄──── vs ────►  TREATMENT-RESPONSIVE
 disability                    recovery
   │
   ▼
 Purkinje cell loss → pancerebellar syndrome → cerebellar atrophy
```

**Molecular pathways / cellular processes.** Adaptive immunity: MHC Class I/II antigen presentation, T-cell receptor engagement, CTL granule-mediated cytotoxicity, apoptosis (GO:0006915), and antigen-specific B-cell/plasma-cell antibody production. In active PCD CSF, ">75% of cells were CD3+ alphabeta T cells and 20–40% were activated T cells," and "activated cdr2-specific CTLs in the CSF contribute to Purkinje degeneration in PCD" ([PMID: 10632096](https://pubmed.ncbi.nlm.nih.gov/10632096/)). CASPR2-associated cerebellar ataxia similarly shows combined CD8+ T-cell and CD138+ plasma-cell CSF infiltration ([PMID: 22759321](https://pubmed.ncbi.nlm.nih.gov/22759321/)).

**Protein dysfunction.** For intracellular antigens the antigen is a normal neuronal protein (loss of Purkinje cells eliminates its function); for surface antigens (DNER, a Notch-pathway EGF-repeat receptor; mGluR1, essential for motor coordination/learning), antibody binding impairs signaling. Notably Homer-3's partner mGluR1A "is predominantly expressed in Purkinje cells where its function is essential for motor coordination and motor learning" ([PMID: 35871640](https://pubmed.ncbi.nlm.nih.gov/35871640/)).

**Immune system involvement.** Central and defining — a cell-mediated (CTL) plus humoral autoimmune attack. Autoantibodies of multiple immunoglobulin classes bind Purkinje cytoplasm across species ([PMID: 3346369](https://pubmed.ncbi.nlm.nih.gov/3346369/)).

**Suggested GO / CL terms.** GO:0006915 (apoptotic process), GO:0002456 (T cell mediated immunity), GO:0001913 (T cell mediated cytotoxicity), GO:0002376 (immune system process), GO:0019882 (antigen processing and presentation). **CL:** CL:0000121 (Purkinje cell — primary target), CL:0000794 (CD8-positive, alpha-beta cytotoxic T cell — effector), CL:0000786 (plasma cell), CL:0000909 (CD8-positive alpha-beta memory T cell).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ / system:** Central nervous system — the **cerebellum** (UBERON:0002037), specifically the cerebellar cortex (UBERON:0002129).
- **Primary cell target:** **Purkinje cells** (CL:0000121; UBERON: Purkinje cell layer UBERON:0002974). Purkinje-cell loss is the pathological hallmark; molecular-layer interneurons are also stained by autoantibodies ([PMID: 3346369](https://pubmed.ncbi.nlm.nih.gov/3346369/)).
- **Secondary involvement:** Brainstem, limbic system, diencephalon, and peripheral nerves in overlap syndromes (anti-Hu encephalomyelitis, anti-Ma2 limbic/diencephalic/brainstem encephalitis, anti-Ri brainstem syndrome).
- **Tissue type:** Nervous tissue.
- **Subcellular compartments:** Depends on antigen — cytoplasm (CDR2/CDR2L; GO:0005737), nucleus (HuD, Ri; GO:0005634), plasma membrane / cell surface (DNER, mGluR1; GO:0005886), postsynaptic density (Homer-3; GO:0014069).
- **Localization / lateralization:** Bilateral, symmetric cerebellar involvement is typical (pancerebellar). FDG-PET may show bilateral cerebellar hypometabolism (early) or hyperperfusion in some inflammatory cases.

---

## Section 8 — Temporal Development

- **Onset:** Adult to older-adult (median ~60–68 years). Onset pattern is **subacute** — evolving over weeks to a few months.
- **Prodrome:** Vertigo/imbalance precedes the full syndrome in ~two-thirds of anti-Yo patients ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)).
- **Progression:** Rapidly progressive during the active phase, then **plateaus within ~6 months** ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)), after which deficits are usually fixed (intracellular subtypes). Cerebellar atrophy appears late on MRI.
- **Course pattern:** Monophasic progressive-then-plateau for classic onconeural PCD; surface-antigen cases may relapse or remit with immunotherapy.
- **Duration:** Chronic/lifelong disability once the plateau is reached in intracellular-antigen disease.
- **Critical window:** There is a narrow therapeutic window **before irreversible Purkinje loss**; "early tumor detection, diagnosis, and PCD treatment are essential because any delay can result in the progression of the disorder and irreversible neurological damage" ([PMID: 35501715](https://pubmed.ncbi.nlm.nih.gov/35501715/)).
- **Tumor timing:** The neurological syndrome usually **precedes** cancer diagnosis; screening should be repeated over time (tumors may surface years later) ([PMID: 22157026](https://pubmed.ncbi.nlm.nih.gov/22157026/)).

---

## Section 9 — Inheritance and Population

- **Epidemiology:** In a population-based 9-year Italian study (983,190 people), overall PNS incidence was **0.89/100,000 person-years** and prevalence **4.37/100,000**; "PNS developed in 1 in every 334 cancers" ([PMID: 31552550](https://pubmed.ncbi.nlm.nih.gov/31552550/)). Cerebellar degeneration was the **second most common PNS at 28%** (after limbic encephalitis 31%): "Most common PNS were limbic encephalitis (31%), cerebellar degeneration (28%) and encephalomyelitis (20%)" ([PMID: 31552550](https://pubmed.ncbi.nlm.nih.gov/31552550/)). Antibody specificities in that cohort: Yo 30%, Hu 26%, Ma2 22%; associated tumors lung 17%, breast 16%, lymphoma 12%.
- **Inheritance:** **Not heritable** — PCD is acquired/autoimmune. The only genetic contribution is HLA Class II susceptibility (polygenic/multifactorial predisposition), not a Mendelian inheritance pattern.
- **Penetrance / expressivity / anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** Not applicable (no causal germline mutation).
- **Sex ratio:** Strongly subtype-dependent. Anti-Yo: 96% female ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)). Anti-Tr/DNER: predominantly middle-aged males ([PMID: 34817790](https://pubmed.ncbi.nlm.nih.gov/34817790/)). Anti-Ma2: predominantly young males (testicular tumors). Overall PNS cohort ~52% female, median age 68 ([PMID: 31552550](https://pubmed.ncbi.nlm.nih.gov/31552550/)).
- **Age distribution:** Adult/older adult, tracking the age of the underlying cancers.

---

## Section 10 — Diagnostics

**Clinical / CSF.** CSF is frequently inflammatory: "lymphocytic pleocytosis, elevated protein, elevated IgG index, and oligoclonal bands" ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/); [PMID: 35871640](https://pubmed.ncbi.nlm.nih.gov/35871640/)).

**Antibody testing (the diagnostic cornerstone).** Serum and CSF onconeural antibody panels: anti-Yo/CDR2/CDR2L, anti-Hu, anti-Ri, anti-Tr/DNER, anti-Ma2, anti-CV2/CRMP5, anti-PCA-2/MAP1B, anti-mGluR1, anti-Homer-3, anti-ZIC4. The anti-Tr/DNER recombinant cell-based assay reaches 100% sensitivity/specificity ([PMID: 25745634](https://pubmed.ncbi.nlm.nih.gov/25745634/)). Rodent cerebellar tissue reliably reproduces the diagnostic Purkinje-cytoplasm immunostaining ([PMID: 3346369](https://pubmed.ncbi.nlm.nih.gov/3346369/)).

**Imaging.** "Magnetic resonance imaging of the brain is often normal in the early stages, with cerebellar atrophy seen later" ([PMID: 27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/)). FDG-PET can show cerebellar hypometabolism.

**Tumor screening (antibody-guided, time-critical).** Per the EFNS task force, "the nature of antibody, and to a lesser extent the clinical syndrome, determines the risk and type of an underlying malignancy," and "for screening of the thoracic region, a CT-thorax is recommended, which if negative is followed by fluorodeoxyglucose-positron emission tomography (FDG-PET)" ([PMID: 20880069](https://pubmed.ncbi.nlm.nih.gov/20880069/)). FDG-PET/CT detected malignancy in ~19% of suspected PNS patients and is recommended regardless of antibody status ([PMID: 22157026](https://pubmed.ncbi.nlm.nih.gov/22157026/)). Screening should be **repeated** if initially negative, because the tumor usually postdates neurological onset.

**Diagnostic criteria.** The 2021 updated PNS diagnostic criteria replaced "classical syndromes" with "high-risk phenotypes," reclassified antibodies as high-risk (>70% cancer association) vs intermediate-risk (30–70%), and introduced the **PNS-Care Score** combining phenotype, antibody, cancer presence, and follow-up to grade diagnoses as definite/probable/possible ([PMID: 34006622](https://pubmed.ncbi.nlm.nih.gov/34006622/)).

**Differential diagnosis.** Hereditary/degenerative ataxias, multiple system atrophy (cerebellar type), toxic/metabolic cerebellar injury, gluten ataxia, anti-GAD ataxia, post-infectious cerebellitis, primary autoimmune cerebellar ataxia (PACA), and metastatic/leptomeningeal disease ([PMID: 39052041](https://pubmed.ncbi.nlm.nih.gov/39052041/); [PMID: 35618871](https://pubmed.ncbi.nlm.nih.gov/35618871/)).

---

## Section 11 — Outcome / Prognosis

**Antigen-location prognosis rule (central finding).** Intracellular-antigen antibodies (Yo, Hu) predict irreversible disability; surface-antigen antibodies (DNER, mGluR1) predict a treatable course. In anti-Yo disease, despite treatment, **84% of survivors are unable to walk unassisted** at follow-up ([PMID: 36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/)). In anti-mGluR1 cerebellar syndrome, "the majority of patients showed clinical improvement (n = 31)" of 42 ([PMID: 41197574](https://pubmed.ncbi.nlm.nih.gov/41197574/)).

**Predictors of good outcome.** In a 97-patient PNS cohort with good outcome in 54.6%, "factors associated with good outcome were: early diagnosis, mRS <3 at presentation, absence of metastatic disease, and adjuvant immunotherapy" ([PMID: 33911377](https://pubmed.ncbi.nlm.nih.gov/33911377/)).

**Oncologic paradox.** PNS can prompt earlier cancer detection, conferring a survival advantage despite neurological morbidity: ANNA1/Hu-IgG PNS + SCLC patients had "a 41% lower hazard of death" than SCLC-only patients (HR=0.59, 95% CI 0.37–0.96) ([PMID: 42233990](https://pubmed.ncbi.nlm.nih.gov/42233990/)).

**Subtype-specific prognosis.** Anti-Ma2-only patients fare significantly better than anti-Ma (Ma1+Ma2) patients — "the clinical outcome was significantly better in the anti-Ma2 group" ([PMID: 27460184](https://pubmed.ncbi.nlm.nih.gov/27460184/)). ICI-related cerebellar ataxia: 46% improved but with residual disability ([PMID: 39153058](https://pubmed.ncbi.nlm.nih.gov/39153058/)). In ICI-related PNS more broadly, risk-antibody positivity carried 29% mortality vs 10% in antibody-negative patients (P=0.012) ([PMID: 41488641](https://pubmed.ncbi.nlm.nih.gov/41488641/)).

**Morbidity / QoL.** High disability burden: wheelchair dependence, dysarthria, and loss of independence dominate the intracellular-antigen subtypes.

---

## Section 12 — Treatment

Treatment rests on **two urgent pillars**: (1) prompt tumor removal/therapy and (2) immunotherapy.

**Tumor-directed therapy.** Surgery, chemotherapy, or radiotherapy of the underlying malignancy is the mainstay and can stabilize or improve neurological symptoms.

**Immunotherapy (NCIT: Immunotherapy).**
- Corticosteroids / IV methylprednisolone pulses (NCIT: Methylprednisolone)
- Intravenous immunoglobulin (NCIT: Intravenous Immunoglobulin Therapy)
- Plasma exchange (NCIT: Plasmapheresis) — can give repeated benefit in some cases ([PMID: 31142706](https://pubmed.ncbi.nlm.nih.gov/31142706/))
- Cyclophosphamide (NCIT: Cyclophosphamide)
- Rituximab / anti-CD20 (NCIT: Rituximab); ofatumumab reported in refractory anti-Yo ([PMID: 39737186](https://pubmed.ncbi.nlm.nih.gov/39737186/))

**Response by subtype.** "Patients with surface receptor autoimmunity … usually show a good response to treatment," in contrast to classical (intracellular) onconeural PNS ([PMID: 29327271](https://pubmed.ncbi.nlm.nih.gov/29327271/)). Anti-Yo/intracellular cases often deteriorate despite aggressive therapy ([PMID: 35501715](https://pubmed.ncbi.nlm.nih.gov/35501715/)). Early rituximab benefited non-tumor anti-DNER ([PMID: 37991702](https://pubmed.ncbi.nlm.nih.gov/37991702/)) and anti-mGluR1 ([PMID: 40760473](https://pubmed.ncbi.nlm.nih.gov/40760473/)) cases.

**ICI-related PCD management.** Discontinue the checkpoint inhibitor and start immunosuppression; outcomes are variable, and rechallenge can provoke relapse ([PMID: 37151179](https://pubmed.ncbi.nlm.nih.gov/37151179/)).

**Supportive / rehabilitative.** Symptomatic agents (e.g., 4-aminopyridine for downbeat nystagmus/oscillopsia) plus physical, occupational, and speech therapy.

**Overall.** Good outcome in ~55% when combined immunotherapy + tumor treatment is applied early ([PMID: 33911377](https://pubmed.ncbi.nlm.nih.gov/33911377/)).

---

## Section 13 — Prevention

- **Primary prevention:** Reducing cancer risk (e.g., smoking cessation to reduce SCLC-associated subtypes) is the only meaningful primary preventive lever; there is no vaccine or specific prophylaxis.
- **Secondary prevention (most actionable):** Early recognition of a subacute cerebellar syndrome, prompt antibody testing, and **antibody-guided tumor screening with FDG-PET** to detect and treat the malignancy before irreversible Purkinje loss ([PMID: 20880069](https://pubmed.ncbi.nlm.nih.gov/20880069/); [PMID: 22157026](https://pubmed.ncbi.nlm.nih.gov/22157026/)). In known cancer survivors, PCD can herald relapse (e.g., Hodgkin lymphoma) — vigilance enables early re-treatment.
- **Tertiary prevention:** Immunotherapy plus rehabilitation to limit disability once disease is established.
- **Pre-ICI risk stratification:** Pre-treatment screening for onconeural antibodies before checkpoint-inhibitor therapy may identify high-risk patients ([PMID: 41488641](https://pubmed.ncbi.nlm.nih.gov/41488641/)).
- **Genetic counseling / carrier screening / immunization:** Not applicable (non-heritable, non-infectious).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Naturally occurring PCD is essentially a **human (Homo sapiens, NCBI:txid9606) disease**. No well-characterized spontaneous paraneoplastic cerebellar degeneration is documented in companion animals as a defined entity.
- **Related veterinary autoimmune cerebellar/encephalitic disease:** Neuronal-autoantibody encephalitis is increasingly recognized in cats — including a reported case of anti-mGluR1 antibodies in a cat ([PMID: 42656301](https://pubmed.ncbi.nlm.nih.gov/42656301/)) — but this was not clearly paraneoplastic.
- **Orthologous genes:** CDR2/CDR2L, ELAVL4/HuD, Grm1, Dner, Pnma2, Homer3 have rodent orthologs (mouse *Cdr2*, *Grm1*, *Dner*), enabling model work.
- **Comparative pathology:** Autoantibodies from human PCD sera bind Purkinje-cell cytoplasm in human, rat, and mouse cerebellum, indicating cross-species antigen conservation ([PMID: 3346369](https://pubmed.ncbi.nlm.nih.gov/3346369/)).
- **Zoonotic potential:** None (autoimmune, non-transmissible).

---

## Section 15 — Model Organisms

Attempts to build a faithful animal model have repeatedly **failed to reproduce degeneration by antibody alone**, which is itself the key mechanistic evidence for T-cell causation.

| Model approach | Result | Interpretation |
|---|---|---|
| Active immunization of mice (BALB/c, C3H, C57BL/6, SJL/J) with recombinant Yo | "All the strains produced high anti-Yo antibody titer but none developed cerebellar ataxia or showed Purkinje cell loss" ([PMID: 7788981](https://pubmed.ncbi.nlm.nih.gov/7788981/)) | Antibody insufficient |
| Passive transfer of PCD patient IgG ± complement/macrophages into rodent brain | IgG taken up by Purkinje cells >36 h without cell loss; "could not be the sole cause of Purkinje cell loss" ([PMID: 7707074](https://pubmed.ncbi.nlm.nih.gov/7707074/), [PMID: 7788964](https://pubmed.ncbi.nlm.nih.gov/7788964/)) | Antibody insufficient |
| DNA immunization against pcd17/cdr2 | Induced antibodies AND CTLs, but "neither clinical nor pathological changes consistent with significant cerebellar degeneration" ([PMID: 11771954](https://pubmed.ncbi.nlm.nih.gov/11771954/)) | Immunity inducible; degeneration not recapitulated — model limitation |
| In vitro human CTLs (HLA-A24) + recombinant Yo on autologous dendritic cells | CTLs reacted with Yo; "cytotoxic T cells are involved in Purkinje cell loss in PCD" ([PMID: 9879687](https://pubmed.ncbi.nlm.nih.gov/9879687/)) | Positive evidence for CTL effector |

**Model type:** Mammalian (mouse, rat, SCID mouse) and in vitro human cellular immunology. **Genetic models:** immunization/transgene (DNA immunization) rather than knockout disease models. **Phenotype recapitulation:** Poor — antibodies and even antigen-specific CTLs can be generated without overt cerebellar degeneration, a major limitation likely reflecting incomplete CNS T-cell trafficking or additional required signals. **Applications:** Established that antibody is not the sole effector and pointed to CTLs; useful for diagnostic reagent validation (rodent cerebellum for immunostaining).

---

## Mechanistic Model / Interpretation

PCD is best understood as **collateral autoimmune damage from an anti-tumor immune response**. The unifying model is antigenic: a tumor ectopically expresses a neuronal protein → tolerance breaks in an HLA-Class-II-permissive host → adaptive immunity attacks both tumor and cerebellum. The **antigen's subcellular location dictates the effector mechanism and therefore the prognosis**:

- **Intracellular antigens** (CDR2/CDR2L, HuD, Ma2) can only be seen by the immune system as MHC-presented peptides → **CD8+ CTL cytotoxicity** → Purkinje-cell death that is rapid, irreversible, and poorly antibody-treatable. The antibodies are bystander biomarkers.
- **Surface antigens** (DNER, mGluR1) are directly accessible to antibodies → **antibody-mediated receptor dysfunction** that is often reversible → treatment-responsive disease.

This single axis explains the epidemiology (tumor associations by antibody), the diagnostics (antibody-guided screening), the treatment response gradient, and the prognosis. The failed animal models are not a gap but positive evidence: they demonstrate that circulating antibody, complement, and macrophages cannot kill Purkinje cells, forcing the conclusion that the effector is the cytotoxic T cell.

---

## Evidence Base (key literature)

| PMID | Contribution | Type |
|---|---|---|
| [27606347](https://pubmed.ncbi.nlm.nih.gov/27606347/) | Anti-Yo most common PCD variant; CDR2/CDR2L; subacute pancerebellar course, MRI evolution | Human review |
| [36334195](https://pubmed.ncbi.nlm.nih.gov/36334195/) | 379-patient anti-Yo systematic review: 96% female, 82% gynecologic, 84% non-ambulatory | Human systematic review |
| [38494293](https://pubmed.ncbi.nlm.nih.gov/38494293/) | Ectopic tumor overexpression of Yo antigens with somatic mutations/amplifications | Human review |
| [34817790](https://pubmed.ncbi.nlm.nih.gov/34817790/) | 85-patient anti-Tr/DNER review: middle-aged males, 91% tumor, Hodgkin lymphoma | Human systematic review |
| [25745634](https://pubmed.ncbi.nlm.nih.gov/25745634/) | Anti-Tr binds extracellular DNER; 100% sensitive/specific CBA | Human/in vitro |
| [10632096](https://pubmed.ncbi.nlm.nih.gov/10632096/) | Activated cdr2-specific CTLs in CSF drive degeneration | Human immunology |
| [9879687](https://pubmed.ncbi.nlm.nih.gov/9879687/) | Patient CTLs react with recombinant Yo — CTL effector role | In vitro |
| [11771954](https://pubmed.ncbi.nlm.nih.gov/11771954/) | DNA immunization induces antibody+CTL but no degeneration | Mouse model |
| [7788981](https://pubmed.ncbi.nlm.nih.gov/7788981/) / [7707074](https://pubmed.ncbi.nlm.nih.gov/7707074/) / [7788964](https://pubmed.ncbi.nlm.nih.gov/7788964/) | Antibody alone insufficient for Purkinje loss | Mouse/rat model |
| [29306402](https://pubmed.ncbi.nlm.nih.gov/29306402/) | HLA Class II susceptibility/protective haplotypes in anti-Yo | Human genetics |
| [31552550](https://pubmed.ncbi.nlm.nih.gov/31552550/) | Population-based PNS incidence 0.89/100k; PCD = 28% of PNS | Human epidemiology |
| [42233990](https://pubmed.ncbi.nlm.nih.gov/42233990/) | Anti-Hu survival paradox (41% lower death hazard w/ SCLC) | Human cohort |
| [41197574](https://pubmed.ncbi.nlm.nih.gov/41197574/) | Anti-mGluR1: majority improve with immunotherapy | Human systematic review |
| [33911377](https://pubmed.ncbi.nlm.nih.gov/33911377/) | Predictors of good outcome; 54.6% good outcome | Human cohort |
| [20880069](https://pubmed.ncbi.nlm.nih.gov/20880069/) / [22157026](https://pubmed.ncbi.nlm.nih.gov/22157026/) | Antibody-guided FDG-PET tumor screening | Guideline/human |
| [34006622](https://pubmed.ncbi.nlm.nih.gov/34006622/) | 2021 PNS diagnostic criteria & PNS-Care Score | Consensus guideline |
| [27460184](https://pubmed.ncbi.nlm.nih.gov/27460184/) | Anti-Ma2 testicular tumors 40%; Ma2-only better outcome | Human series |
| [39153058](https://pubmed.ncbi.nlm.nih.gov/39153058/) / [42442848](https://pubmed.ncbi.nlm.nih.gov/42442848/) | ICI-related cerebellar ataxia; amplification of onconeural immunity | Human cohort/case |
| [3346369](https://pubmed.ncbi.nlm.nih.gov/3346369/) | Cross-species Purkinje-cytoplasm antibody binding; diagnostic substrate | Human/animal |

---

## Limitations and Knowledge Gaps

1. **No faithful animal model** of the degeneration exists; the CTL effector mechanism is inferred from failed antibody-transfer experiments plus in vitro human CTL reactivity, not from a reproducible in vivo lesion.
2. **Rarity and heterogeneity** limit prospective, controlled treatment data; most evidence is from case series, retrospective cohorts, and systematic reviews of case reports — susceptible to publication and referral bias (serology-lab cohorts over-represent antibody-positive cases).
3. **Molecular detail of tolerance breakdown** (why specific tumors over-express onconeural antigens, and the exact epitope-spreading/mimicry events) is incompletely defined.
4. **Prognostic biomarkers** beyond antibody class/antigen location are lacking; no validated molecular predictor of immunotherapy response.
5. **Epigenetic, transcriptomic, proteomic, and single-cell profiling** of PCD cerebellum are largely absent from the literature reviewed — a genuine data gap.
6. **HLA association data** derive from a single modest cohort (n=40); replication across ancestries is needed.

---

## Proposed Follow-up Experiments / Actions

1. **Single-cell / spatial profiling** of PCD-affected cerebellum and matched CSF (CITE-seq, TCR sequencing) to define the clonality and antigen-specificity of infiltrating CD8+ T cells and confirm the CTL model in situ.
2. **Humanized HLA-transgenic mouse models** expressing onconeural antigens in a tumor context, with adoptive transfer of antigen-specific CD8+ T cells, to finally recapitulate Purkinje-cell loss.
3. **Multi-center prospective registry** with standardized PNS-Care scoring, antibody subtyping, and mRS trajectories to quantify outcomes and treatment effects by antigen location.
4. **Replication of HLA Class II associations** in larger, ancestrally diverse cohorts, extended to non-Yo subtypes.
5. **Trials of T-cell-directed immunotherapy** (e.g., agents targeting CD8+ CTLs or trafficking) for intracellular-antigen PCD, where B-cell-directed therapy underperforms.
6. **Pre-ICI onconeural antibody screening protocols** with prospective evaluation of whether screening plus surveillance reduces severe checkpoint-inhibitor cerebellar toxicity.
7. **Biomarker discovery** (CSF proteomics/neurofilament light) to identify early, treatable-window markers before irreversible atrophy.

---

*Report compiled from 69 reviewed publications and 12 confirmed findings across 5 investigative iterations. Evidence types are labeled per claim; PMIDs link to primary sources.*


## Artifacts

- [OpenScientist final report](Paraneoplastic_Cerebellar_Degeneration-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Paraneoplastic_Cerebellar_Degeneration-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 36 |
| On topic | 25 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27606347` *(abstract only)*: "lymphocytic pleocytosis, elevated protein, elevated IgG index, and oligoclonal bands"
  - closest text in source: "Cerebrospinal fluid abnormalities, primarily elevated protein, lymphocytic pleocytosis, and oligoclonal bands, are common in the early stages"
- `PMID:35871640` *(abstract only)*: "lymphocytic pleocytosis, elevated protein, elevated IgG index, and oligoclonal bands"
  - closest text in source: "Examination of CSF showed a lymphocytic pleocytosis of 11 cells/µl and an intrathecal IgG synthesis of 26%"
- `PMID:7788964` *(abstract only)*: "could not be the sole cause of Purkinje cell loss"
  - closest text in source: "We conclude that the anti-Yo antibody, either in combination with or without complement or activated mononuclear cells, cannot be the sole cause of Purkinje cell loss."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012310` (1 mention) - the report calls it "CSF lymphocytic pleocytosis"; HP calls it **Abnormal monocyte count**
- `HP:0032101` (1 mention) - the report calls it "Oligoclonal bands / elevated IgG index"; HP calls it **Unusual infection**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000639` (1 mention) - the report calls it "Nystagmus (incl. downbeat)"; HP calls it **Nystagmus**
- `HP:0002321` (1 mention) - the report calls it "Vertigo / dizziness"; HP calls it **Vertigo**, and lists "Dizziness" among its other names
- `HP:0002078` (1 mention) - the report calls it "Truncal instability"; HP calls it **Truncal ataxia**
- `CL:0000121` (2 mentions) - the report calls it "Purkinje cell — primary target"; CL calls it **Purkinje cell**
- `CL:0000794` (1 mention) - the report calls it "CD8-positive, alpha-beta cytotoxic T cell — effector"; CL calls it **CD8-positive, alpha-beta cytotoxic T cell**