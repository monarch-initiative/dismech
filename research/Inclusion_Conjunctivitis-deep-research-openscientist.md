---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T04:15:48.226683'
end_time: '2026-09-30T04:53:17.998367'
duration_seconds: 2249.77
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Inclusion Conjunctivitis
  mondo_id: MONDO:0005808
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42350099
  relevance_assessed: 28
  on_topic: 26
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 18
  verified: 17
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.056
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0005808
    reported_labels:
    - Mondo
    ontology_label: inclusion conjunctivitis
  - term_id: HP:0025421
    reported_labels:
    - Conjunctival hyperemia
    ontology_label: Pneumomediastinum
  - term_id: HP:0000509
    reported_labels:
    - related
    ontology_label: Conjunctivitis
  - term_id: HP:0410019
    reported_labels:
    - regional lymphadenopathy
    ontology_label: Epigastric pain
  - term_id: UBERON:0000964
    reported_labels:
    - Associated structures:** cornea
    ontology_label: cornea
  labels_variant: 2
  unresolved_terms:
  - HP:0200019
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Inclusion_Conjunctivitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Inclusion_Conjunctivitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inclusion Conjunctivitis
- **MONDO ID:** MONDO:0005808 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Inclusion Conjunctivitis** covering all of the
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

# Inclusion Conjunctivitis (MONDO:0005808): A Comprehensive Disease Characteristics Report

**Category:** Infectious Disease
**Causative agent:** *Chlamydia trachomatis* serovars D–K (obligate intracellular bacterium)
**Report basis:** 14 confirmed findings across 37 reviewed papers; human clinical cohorts, case reports, reviews, and a guinea-pig animal model

---

## Summary

**Inclusion conjunctivitis is an infectious follicular conjunctivitis caused by the obligate intracellular bacterium *Chlamydia trachomatis*, specifically the "oculogenital" serovars D–K — the same serovars that cause urogenital chlamydia.** It is fundamentally an infectious, sexually-linked disease with no genetic etiology. The condition presents in two demographic settings: (1) **adult inclusion conjunctivitis (AIC)**, a sexually transmitted disease acquired by transfer of infected genital secretions to the eye (autoinoculation or sexual contact), peaking in young sexually active adults; and (2) **neonatal inclusion conjunctivitis (ophthalmia neonatorum)**, acquired by the newborn passing through an infected birth canal during vaginal delivery. This dual presentation reflects a single reservoir — genital *C. trachomatis* infection in the sexually active population.

Mechanistically, disease follows the hallmark chlamydial **biphasic developmental cycle**: infectious **elementary bodies (EBs)** are inoculated onto conjunctival epithelium, are endocytosed, and differentiate within a membrane-bound **inclusion** into replicative **reticulate bodies (RBs)** that divide by binary fission before re-converting to EBs and lysing the host cell to spread. The intracellular infection and released chlamydial antigens drive a **neutrophil- and lymphocyte-mediated immune response** producing the characteristic **subepithelial follicles (germinal centers)**, papillary hypertrophy, mucopurulent discharge, and preauricular adenopathy. In neonates, infection can extend beyond the conjunctiva to cause **chlamydial (interstitial) pneumonia**.

Inclusion conjunctivitis is clinically and epidemiologically **distinct from trachoma** (serovars A–C), which is a chronic, blinding, cicatricial keratoconjunctivitis of the upper tarsal conjunctiva driven by repeated childhood reinfection in endemic areas. By contrast, inclusion conjunctivitis is sporadic, generally non-blinding, and **curable with systemic antibiotics** — single-dose oral azithromycin 1 g or a doxycycline course in adults; erythromycin or azithromycin in neonates (with amoxicillin/macrolides for the maternal reservoir in pregnancy, since doxycycline is contraindicated). Diagnosis is best made by **nucleic acid amplification testing (NAAT/PCR)** of conjunctival specimens, which outperforms culture and Giemsa inclusion cytology. Prevention rests chiefly on **antenatal maternal screening and treatment**, not neonatal topical prophylaxis, which is inadequate against *Chlamydia*.

---

## 1. Disease Information

**Overview.** Inclusion conjunctivitis is an infectious conjunctivitis caused by *Chlamydia trachomatis*. It is called "inclusion" conjunctivitis because of the pathognomonic intracytoplasmic **inclusion bodies** (chlamydial inclusions) formed in infected conjunctival epithelial cells. The disease sits at one pole of the oculogenital *C. trachomatis* disease spectrum, which — per a review of STI-associated eye infections — "*includes STIs, inclusion conjunctivitis in adults and neonatal ophthalmia*" ([PMID: 35027140](https://pubmed.ncbi.nlm.nih.gov/35027140/)) (F013).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:0005808 |
| Causative organism (NCBI Taxonomy) | *Chlamydia trachomatis* (txid813) |
| MeSH | Conjunctivitis, Inclusion; Chlamydia trachomatis |
| ICD-10 | A74.0 (Chlamydial conjunctivitis); P39.1 (Neonatal conjunctivitis / ophthalmia neonatorum) |
| ICD-11 | 1C22 (Chlamydial infection); neonatal conjunctivitis under KA modules |

**Synonyms / alternative names:** adult inclusion conjunctivitis (AIC); chlamydial conjunctivitis; oculogenital chlamydial conjunctivitis; paratrachoma; swimming-pool conjunctivitis (historical); neonatal chlamydial conjunctivitis / chlamydial ophthalmia neonatorum (neonatal form); inclusion blennorrhea (historical neonatal term).

**Information source:** The evidence base is drawn from **aggregated disease-level resources** — clinical cohorts, case series, reviews, and one animal model — rather than individual EHR records, although some cohorts (e.g., a Cosmos EHR study of neonatal conjunctivitis, [PMID: 39749988](https://pubmed.ncbi.nlm.nih.gov/39749988/)) draw on de-identified patient data.

---

## 2. Etiology

**Primary cause — infectious.** Inclusion conjunctivitis is caused entirely by infection with *C. trachomatis* serovars D–K. There is **no genetic etiology**; this is not a Mendelian or complex genetic disease. As stated for the adult form, "*Inclusion conjunctivitis caused by the serovars D-K of Chlamydia trachomatis also affects the sexually active population*" ([PMID: 23692878](https://pubmed.ncbi.nlm.nih.gov/23692878/)) (F001).

**Risk factors (environmental/behavioral):**

- **Adults:** sexual activity and genital *C. trachomatis* infection; young adult age (peak 16–20 years); autoinoculation from infected genital secretions; sexual/orogenital contact. Adult chlamydial conjunctivitis "*is a complication of sexually transmitted genital infection by C trachomatis and it indicates a large reservoir of such infections*" ([PMID: 7427689](https://pubmed.ncbi.nlm.nih.gov/7427689/)) (F014).
- **Neonates:** maternal genital chlamydial infection and **vaginal delivery**. In a 10-year cohort of 797 neonates with suspected ophthalmia neonatorum, vaginal delivery was among the strongest predictors of chlamydial infection (OR = 17.63, 95% CI 5.59–55.51, p < 0.001), alongside bloody discharge (OR = 20.99, 95% CI 6.09–72.29) ([PMID: 41062949](https://pubmed.ncbi.nlm.nih.gov/41062949/)) (F002).

**Genetic risk / protective factors:** Not applicable — no causal or susceptibility loci; no protective alleles. Host genetic modifiers of chlamydial immunopathology are relevant to blinding trachoma but not established for inclusion conjunctivitis.

**Gene–environment interactions:** Not applicable for this infectious disease.

---

## 3. Phenotypes

Inclusion conjunctivitis presents as a **subacute-to-chronic follicular conjunctivitis**. In a clinical/molecular AIC cohort, it presented with "*variable hyperaemia, follicular reaction, papillary hypertrophy and mucopurulent discharge*" ([PMID: 42350099](https://pubmed.ncbi.nlm.nih.gov/42350099/)) (F004).

| Phenotype | Type | HPO suggestion | Characteristics / Frequency |
|---|---|---|---|
| Follicular conjunctivitis (subepithelial follicles) | Clinical sign | HP:0200019 (related) | **Most common sign**; earliest to regress after treatment ([PMID: 24047438](https://pubmed.ncbi.nlm.nih.gov/24047438/)) (F004) |
| Conjunctival hyperemia / redness | Clinical sign | HP:0025421 (Conjunctival hyperemia) | Variable; common |
| Mucopurulent discharge | Symptom/sign | HP:0000509 (related) | Common |
| Papillary hypertrophy | Clinical sign | — | Common |
| Preauricular lymphadenopathy | Clinical sign | HP:0410019 (regional lymphadenopathy) | Characteristic of follicular chlamydial conjunctivitis |
| Pseudoptosis | Clinical sign | HP:0000508 (Ptosis, related) | Conspicuous in some adult cases ([PMID: 3838901](https://pubmed.ncbi.nlm.nih.gov/3838901/)) (F014) |
| Foreign-body sensation / irritation | Symptom | — | Common |
| Chronic, therapy-resistant course | Course feature | — | Frequently misdiagnosed ([PMID: 28443807](https://pubmed.ncbi.nlm.nih.gov/28443807/)) (F004) |

**Onset & severity:** Adult form typically presents in young adults; neonatal form within days to weeks of birth. Severity is mild-to-moderate and generally non-blinding, but the course can be **prolonged if unrecognized/untreated** ("*a prolonged course is expected if unrecognized/untreated*," F014). Laterality is characteristically **unilateral** in adults: "*In patients with proved chlamydial conjunctivitis unilateral symptoms were the rule*" ([PMID: 3838901](https://pubmed.ncbi.nlm.nih.gov/3838901/)) (F014).

**Quality of life:** Chronic irritation, discharge, and diagnostic delay (with unnecessary workups for orbital or thyroid eye disease, [PMID: 35623592](https://pubmed.ncbi.nlm.nih.gov/35623592/)) impose morbidity, but the disease is not sight-threatening in the great majority of cases and resolves with appropriate therapy.

---

## 4. Genetic/Molecular Information

**Not applicable — this is an infectious, non-genetic disease.** There are no human causal genes, pathogenic variants, modifier genes, epigenetic lesions, or chromosomal abnormalities.

The relevant molecular biology is that of the **pathogen**: the *C. trachomatis* **ompA** gene (encoding the major outer membrane protein, MOMP) defines serovars/genotypes D–K and is used for molecular typing. An AIC cohort "*provides a clinical and molecular profile of AIC and highlights variability across ompA serotypes*" ([PMID: 42350099](https://pubmed.ncbi.nlm.nih.gov/42350099/)) (F001). In the pathogen, azithromycin resistance can arise from single point mutations in **23S rRNA (A2058/A2059)**, demonstrated in the related *C. caviae* (F011, [PMID: 20065052](https://pubmed.ncbi.nlm.nih.gov/20065052/)).

---

## 5. Environmental Information

**Infectious agent (organism):** *Chlamydia trachomatis*, an obligate intracellular Gram-negative bacterium. Ocular disease is divided by serovar: serovars **A, B, C** cause trachoma; serovars **D–K** cause inclusion conjunctivitis and urogenital infection (F006, F001).

**Environmental/behavioral factors:** sexual transmission of genital chlamydia; transfer of infected secretions to the eye; passage through an infected birth canal. Historically, contaminated swimming-pool water was implicated ("swimming-pool conjunctivitis"). No toxin, radiation, pollution, occupational-exposure, or lifestyle (smoking/diet/alcohol) factor is causally established beyond sexual behavior as the route to genital infection.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating infection → clinical manifestation)

1. **Inoculation.** Infectious **elementary bodies (EBs)** are deposited on the conjunctival epithelium — from infected genital secretions (adult autoinoculation/sexual contact) or from the birth canal during vaginal delivery (neonate). *(Demonstrated route; F001, F002.)*
2. **Attachment and entry** — EBs attach to and are endocytosed by conjunctival epithelial cells, entering a membrane-bound compartment, the **chlamydial inclusion**. *"Chlamydia are obligate intracellular bacteria that reside within a membrane-bound compartment called the chlamydial inclusion inside a eukaryotic host cell"* ([PMID: 35703434](https://pubmed.ncbi.nlm.nih.gov/35703434/)) (F009).
3. **EB → RB differentiation and replication** — inside the inclusion, EBs convert to replicative **reticulate bodies (RBs)** that divide by binary fission. *"Chlamydia undergo a biphasic developmental cycle alternating between the infectious elementary body (EB) and the replicative reticulate body (RB)"* ([PMID: 36385643](https://pubmed.ncbi.nlm.nih.gov/36385643/)) (F009).
4. **RB → EB re-conversion and release** — *"RBs replicate by binary fission within an infected host cell, but there is a delay before RBs convert into EBs for spread to a new host cell"* ([PMID: 33594486](https://pubmed.ncbi.nlm.nih.gov/33594486/)); host-cell lysis/extrusion releases progeny EBs that infect neighboring epithelium (F009).
5. **Innate immune activation** — infection and released chlamydial antigens trigger innate responses; **neutrophils** infiltrate and drive tissue pathology (established causally in the animal model: neutrophil depletion "*dramatically decreased ocular pathology, both clinically and histologically*," [PMID: 21402767](https://pubmed.ncbi.nlm.nih.gov/21402767/)) (F011).
6. **Adaptive immune response** — lymphocytic (CD4+/CD8+ T-cell) infiltration and B-cell responses form **subepithelial follicles (germinal centers)** and papillary hypertrophy (F009, F011).
7. **Clinical disease** — chronic follicular mucopurulent conjunctivitis, hyperemia, preauricular adenopathy (F004).
8. **Branch (neonate):** the same organism can spread to the respiratory tract, causing **chlamydial interstitial pneumonia** (F007, F013).
9. **Branch (chronic/repeated infection):** prolonged immunopathology can cause conjunctival scarring — **demonstrated for trachoma** (serovars A–C, [PMID: 26424969](https://pubmed.ncbi.nlm.nih.gov/26424969/)); *inferred to be milder and usually non-cicatricial* in inclusion conjunctivitis (F006, F009).

```
 EB inoculation ──▶ epithelial endocytosis ──▶ inclusion forms
        │                                          │
        │                              EB → RB (replication, binary fission)
        │                                          │
        │                              RB → EB ──▶ host-cell lysis ──▶ spread
        ▼                                          ▼
  genital reservoir                    chlamydial antigen release
  (adult STI / maternal)                         │
                                     ┌────────────┴────────────┐
                              neutrophil influx          T/B-cell response
                              (tissue damage)          (follicles/germinal ctrs)
                                     └────────────┬────────────┘
                                                  ▼
                            chronic follicular mucopurulent conjunctivitis
                                                  │
                           ┌──────────────────────┴───────────────────────┐
                    (neonate) spread to lung           (chronic) conjunctival
                    → interstitial pneumonia            scarring [trachoma-proven;
                                                        inferred mild here]
```

**Molecular pathways / cellular processes (GO suggestions):** intracellular bacterial infection/entry into host (GO:0044409); host innate immune response (GO:0045087); inflammatory response (GO:0006954); adaptive immune response / germinal center formation (GO:0002250, GO:0002467). **Cell types (CL):** conjunctival epithelial cell (CL:0000066 epithelial cell), neutrophil (CL:0000775), CD4+ T cell (CL:0000624), CD8+ T cell (CL:0000625), B cell/plasma cell. In the animal model, neutrophil depletion also raised *C. caviae*-specific tear/serum IgA and altered IL-5, TGF-β, and CCL5/RANTES, showing neutrophils shape both innate damage and the adaptive response (F011).

---

## 7. Anatomical Structures Affected

- **Primary organ/tissue:** the **conjunctiva** (UBERON:0001811), specifically the **conjunctival epithelium** (epithelial tissue). Palpebral/tarsal and bulbar conjunctiva are involved; follicles predominate in the inferior fornix/tarsal conjunctiva.
- **Associated structures:** cornea (UBERON:0000964) may show punctate epithelial keratitis or micropannus in some cases; regional **preauricular lymph nodes** enlarge.
- **Secondary organ involvement (neonate):** **lung** (UBERON:0002048) — chlamydial interstitial pneumonia (F007).
- **Subcellular (GO Cellular Component):** the pathogen occupies the **chlamydial inclusion**, a modified host membrane-bound vacuole in the cytoplasm; host cytoplasm and endomembrane system are co-opted (F009).
- **Body systems:** ocular/visual system; reproductive/genitourinary system (reservoir); respiratory system (neonatal complication).
- **Lateralization:** characteristically **unilateral** in adults (F014); neonatal disease is often bilateral.

---

## 8. Temporal Development

- **Onset:** Adult form — subacute to insidious, in sexually active young adults (peak 16–20 years, F014). Neonatal form — within the first days to ~2 weeks of life following delivery.
- **Onset pattern:** subacute/chronic; frequently indolent and therapy-resistant if treated only with topical agents (F004).
- **Course:** untreated disease can be **prolonged/chronic** (F014). Follicles are the earliest sign to regress with successful systemic treatment, though **complete relief may take ~1 month** ([PMID: 24047438](https://pubmed.ncbi.nlm.nih.gov/24047438/)) (F003, F004).
- **Resolution:** treatment-induced remission with systemic antibiotics; prompt therapy "*can eradicate the microorganism at least in uncomplicated infections, preventing the sequelae of the disease*" ([PMID: 2247702](https://pubmed.ncbi.nlm.nih.gov/2247702/)) (F013).
- **Critical period:** the perinatal window (maternal screening/treatment before delivery) is the key opportunity to prevent neonatal disease (F005).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable.

**Epidemiology.** The disease tracks the burden of genital chlamydia. A review estimates global *C. trachomatis* prevalence at **~2.8% in men and ~3.8% in women** ([PMID: 35027140](https://pubmed.ncbi.nlm.nih.gov/35027140/)) (F013).

| Setting | Finding | Source |
|---|---|---|
| Eye-clinic conjunctivitis patients | Chlamydia in 28/983 (~2.8%); peak >9% at ages 16–20 | [PMID: 3838901](https://pubmed.ncbi.nlm.nih.gov/3838901/) (F14) |
| Neonatal ophthalmia (Singapore, n=797) | *C. trachomatis* leading cause: 140 (17.5%) | [PMID: 41062949](https://pubmed.ncbi.nlm.nih.gov/41062949/) (F02) |
| Symptomatic neonatal conjunctivitis (Hungary, n=76) | *C. trachomatis* in 30 (39.5%) | [PMID: 28693667](https://pubmed.ncbi.nlm.nih.gov/28693667/) (F12) |
| Perinatal transmission (preterm cohort) | maternal carriage ~10%; mother-to-infant transmission 75% | [PMID: 22568356](https://pubmed.ncbi.nlm.nih.gov/22568356/) (F07) |

**Serovar/genotype distribution:** oculogenital serovars **E and G predominate**, mirroring urogenital chlamydia. In the Hungarian neonatal series: genotype **E 48%** (14/29), **G 24%** (7/29), J 10%, K and F 6.9% each, H 3.4% ([PMID: 28693667](https://pubmed.ncbi.nlm.nih.gov/28693667/)) (F12).

**Demographics:** adults — young, sexually active; neonates — infants of infected mothers, especially after vaginal delivery. **Age peak 16–20 years** in adults; not seen in ages 1–15 (F14). Geographic distribution is worldwide and sporadic (non-endemic), unlike trachoma.

---

## 10. Diagnostics

**NAAT/PCR is the most sensitive test.** In 241 neonates, *C. trachomatis* was detected by PCR in 16.6%, culture in 12.9%, and Giemsa staining in only 7.5%; PCR showed "*High sensitivity (100%) and specificity (95.7%)... as compared to culture*" ([PMID: 22369307](https://pubmed.ncbi.nlm.nih.gov/22369307/)) (F10).

| Modality | Role | Relative yield |
|---|---|---|
| **NAAT / PCR** (e.g., transcription-mediated amplification, Aptima Combo 2) | **Test of choice**; confirms atypical cases | Highest (100% sens vs culture) |
| Cell culture | Historical gold standard | Intermediate (12.9%) |
| Giemsa cytology (intracytoplasmic inclusions) | Rapid, low-cost | Lowest (7.5%) |
| Conjunctival cytology + NAAT + culture combined | Comprehensive AIC workup | — |

Contemporary AIC cohorts combine cytology, NAAT, and culture ([PMID: 42350099](https://pubmed.ncbi.nlm.nih.gov/42350099/)); atypical adult presentations were confirmed by TMA ([PMID: 35623592](https://pubmed.ncbi.nlm.nih.gov/35623592/)) (F10).

**Clinical clue / differential:** Persistent, therapy-resistant follicular conjunctivitis should prompt chlamydial testing — "*when a patient presents with persistent, therapy-resistant conjunctivitis, particularly if conjunctival follicles are present, chlamydial conjunctivitis should be considered*" ([PMID: 28443807](https://pubmed.ncbi.nlm.nih.gov/28443807/)) (F04). Differential diagnosis includes viral (adenoviral) follicular conjunctivitis, other bacterial conjunctivitis, allergic conjunctivitis, keratoconjunctivitis sicca, and — critically — **trachoma** in endemic settings. Adult diagnosis should trigger full genital/serological STI investigation (F14).

---

## 11. Outcome / Prognosis

**Excellent with prompt antibiotics.** Prompt treatment eradicates the organism in uncomplicated infection and prevents sequelae ([PMID: 2247702](https://pubmed.ncbi.nlm.nih.gov/2247702/)) (F13). Unlike blinding trachoma, inclusion conjunctivitis is **generally non-blinding** (F06).

- **Mortality:** essentially nil for the ocular disease itself.
- **Morbidity:** chronic ocular irritation, misdiagnosis/diagnostic delay; complete symptom relief may take ~1 month even after appropriate therapy (F03).
- **Neonatal complications:** spread of infection to cause **chlamydial pneumonia** (all infected infants in one preterm cohort developed respiratory disorders/pneumonia, some requiring nCPAP or ventilation, [PMID: 22568356](https://pubmed.ncbi.nlm.nih.gov/22568356/)); maternal chlamydia is associated with low birth weight and preterm birth (F07, [PMID: 27144177](https://pubmed.ncbi.nlm.nih.gov/27144177/), [PMID: 27164464](https://pubmed.ncbi.nlm.nih.gov/27164464/)).
- **Prognostic factors:** promptness of systemic (not merely topical) therapy; recognition of the diagnosis; treatment of the genital reservoir and partners.

---

## 12. Treatment

**Systemic antibiotics are required** — chlamydial conjunctivitis "*warrant[s] systemic antibiotics due to their potential for severe complications*," unlike routine bacterial conjunctivitis ([PMID: 37977204](https://pubmed.ncbi.nlm.nih.gov/37977204/)) (F03).

| Population | Regimen | Evidence |
|---|---|---|
| **Adults** | **Single-dose oral azithromycin 1 g** (NCIT: Azithromycin) — equivalent to prolonged azithromycin and 21-day doxycycline for retreatment rate | RCT, n=83: "*All treatment groups provided statistically equivalent results of retreatment rate*" ([PMID: 24047438](https://pubmed.ncbi.nlm.nih.gov/24047438/)) (F03) |
| Adults (alternative) | Doxycycline course; oral azithromycin 1 g resolved atypical cases | [PMID: 35623592](https://pubmed.ncbi.nlm.nih.gov/35623592/) (F03) |
| **Neonates** | Systemic erythromycin or azithromycin | F05, F13 |
| **Pregnant women (reservoir)** | **Amoxicillin 7-day course** or erythromycin; **doxycycline & fluoroquinolones contraindicated** | "*Amoxicillin (a 7-day course) is the antibiotic of choice for pregnant women...*"; "*Doxycycline and fluoroquinolones are contraindicated during pregnancy*" ([PMID: 22216551](https://pubmed.ncbi.nlm.nih.gov/22216551/)) (F08) |

**Adjuncts / strategy:** partner treatment and full STI evaluation in adults; treat the maternal genital infection to protect the neonate (F08, F14). **NCIT suggestions:** Azithromycin (C551), Doxycycline (C459), Erythromycin (C576), Amoxicillin (C398). **Pharmacogenomics / resistance:** azithromycin resistance can arise from single 23S rRNA A2058/A2059 mutations (shown in *C. caviae*; attenuates virulence) (F11).

---

## 13. Prevention

**Antenatal maternal screening and treatment is the most effective prevention.** "*Prenatal screening and treatment of pregnant women is the most effective way to prevent ophthalmia neonatorum*" ([PMID: 36691840](https://pubmed.ncbi.nlm.nih.gov/36691840/)) (F05).

- **Neonatal topical prophylaxis is inadequate against chlamydia.** "*Administration of erythromycin ophthalmic ointment for the prevention of neonatal conjunctivitis is not literature-supported*" ([PMID: 36691840](https://pubmed.ncbi.nlm.nih.gov/36691840/)); a Botswana series found most infants who developed chlamydial ophthalmia had received ocular tetracycline prophylaxis — "*current prophylaxis and treatment modalities... are inadequate*" ([PMID: 37338101](https://pubmed.ncbi.nlm.nih.gov/37338101/)) (F05).
- **Primary prevention:** safe-sex practices; STI screening in sexually active adults.
- **Secondary prevention:** early detection/treatment of genital chlamydia; partner notification and treatment.
- **Public health:** treating the "large reservoir" of genital infection reduces both adult and neonatal ocular disease (F14).
- **Immunization:** no licensed chlamydia vaccine (research ongoing).

---

## 14. Other Species / Natural Disease

- **Guinea pig (*Cavia porcellus*):** natural host of ***Chlamydia caviae***, which causes **guinea-pig inclusion conjunctivitis (GPIC)** — "*Chlamydia caviae, which is a natural pathogen of guinea pigs*" ([PMID: 20065052](https://pubmed.ncbi.nlm.nih.gov/20065052/)) (F11). This is a naturally occurring analog of human inclusion conjunctivitis and the principal animal model.
- **Cross-species relevance:** the EB→RB developmental cycle and inclusion biology are conserved across the *Chlamydiaceae*, underpinning the model's validity.
- **Zoonotic note:** *C. caviae* has occasionally caused human respiratory disease, but ocular inclusion conjunctivitis in humans is caused by *C. trachomatis*, not *C. caviae*.

---

## 15. Model Organisms

**Guinea pig *C. caviae* ocular infection (GPIC)** is the principal animal model of inclusion conjunctivitis. It recapitulates ocular follicular immunopathology and enables mechanistic and antibiotic studies:

- **Neutrophil role:** neutrophil depletion "*dramatically decreased ocular pathology, both clinically and histologically*," and shifted adaptive immunity (higher *C. caviae*-specific IgA in tears/serum; fewer conjunctival CD4+/CD8+ T cells; altered IL-5, TGF-β, CCL5/RANTES) — establishing neutrophils as drivers of tissue damage ([PMID: 21402767](https://pubmed.ncbi.nlm.nih.gov/21402767/)) (F11).
- **Antibiotic pharmacology:** spontaneous azithromycin resistance maps to single 23S rRNA mutations (A2058/A2059) and attenuates virulence in vivo ([PMID: 20065052](https://pubmed.ncbi.nlm.nih.gov/20065052/)) (F11).

**Cell-based systems:** *C. trachomatis* is routinely studied in cultured epithelial cell lines for the developmental cycle, inclusion kinetics, and drug inhibition ([PMID: 35703434](https://pubmed.ncbi.nlm.nih.gov/35703434/), [PMID: 33051378](https://pubmed.ncbi.nlm.nih.gov/33051378/)).

**Limitations:** the guinea-pig model uses a different species (*C. caviae*, not *C. trachomatis*) and does not fully replicate human sexual/perinatal transmission dynamics; cell culture omits the intact ocular immune microenvironment.

---

## Mechanistic Model / Interpretation

Inclusion conjunctivitis is best understood as **one clinical face of a single genital-chlamydia reservoir**. The identical serovars D–K that colonize the urogenital tract reach the eye by two routes — adult autoinoculation/sexual contact, and neonatal passage through the birth canal — and there execute the universal chlamydial developmental program. The **EB→RB→EB cycle inside conjunctival epithelial inclusions** is the mechanistic engine; the **host neutrophil-then-lymphocyte response** converts intracellular infection into the visible follicular disease. This explains the key clinical facts: the chronic, therapy-resistant nature (intracellular persistence), the follicular morphology (germinal-center immunopathology), the requirement for **systemic** antibiotics (topical agents cannot reliably clear an intracellular, genitally-seeded infection), and the neonatal pneumonia branch (same organism, different mucosa).

The **trachoma vs. inclusion conjunctivitis** distinction is central and is defined by serovar, site, transmission, and outcome:

| Feature | Inclusion conjunctivitis | Trachoma |
|---|---|---|
| Serovars | **D–K** (oculogenital) | **A, B, C** |
| Transmission | Sexual/perinatal, sporadic | Eye-to-eye, endemic, repeated childhood reinfection |
| Primary site | Conjunctiva (fornix/tarsal) | Upper tarsal conjunctiva |
| Course | Acute–chronic, usually **non-blinding** | Chronic cicatricial, **blinding** |
| Prognosis | Curable with systemic antibiotics | Leading infectious cause of blindness |

Source: [PMID: 26424969](https://pubmed.ncbi.nlm.nih.gov/26424969/), [PMID: 35027140](https://pubmed.ncbi.nlm.nih.gov/35027140/) (F06, F13).

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [23692878](https://pubmed.ncbi.nlm.nih.gov/23692878/) | Serovars D–K cause adult inclusion conjunctivitis in sexually active population | F01 |
| [42350099](https://pubmed.ncbi.nlm.nih.gov/42350099/) | Clinical/molecular AIC profile; ompA serotype variability; presentation features | F01, F04, F10 |
| [41062949](https://pubmed.ncbi.nlm.nih.gov/41062949/) | *C. trachomatis* leading cause of ophthalmia neonatorum (17.5%); vaginal delivery OR 17.63 | F02 |
| [24047438](https://pubmed.ncbi.nlm.nih.gov/24047438/) | RCT: single-dose azithromycin equivalent to longer regimens; follicles most common sign | F03, F04 |
| [37977204](https://pubmed.ncbi.nlm.nih.gov/37977204/) | Chlamydial conjunctivitis requires systemic antibiotics | F03 |
| [35623592](https://pubmed.ncbi.nlm.nih.gov/35623592/) | Atypical adult cases; oral azithromycin 1 g resolution; TMA diagnosis | F03, F04, F10 |
| [28443807](https://pubmed.ncbi.nlm.nih.gov/28443807/) | Persistent therapy-resistant follicular conjunctivitis → suspect chlamydia | F04 |
| [36691840](https://pubmed.ncbi.nlm.nih.gov/36691840/) | Prenatal screening/treatment most effective; topical prophylaxis not supported | F05 |
| [37338101](https://pubmed.ncbi.nlm.nih.gov/37338101/) | Field evidence topical prophylaxis fails against chlamydia | F05 |
| [26424969](https://pubmed.ncbi.nlm.nih.gov/26424969/) | Trachoma (A,B,C) distinct blinding disease | F06 |
| [22568356](https://pubmed.ncbi.nlm.nih.gov/22568356/) | 75% perinatal transmission; all infected infants developed pneumonia | F07 |
| [22216551](https://pubmed.ncbi.nlm.nih.gov/22216551/) | Amoxicillin in pregnancy; doxycycline/fluoroquinolones contraindicated | F08 |
| [35703434](https://pubmed.ncbi.nlm.nih.gov/35703434/) | Obligate intracellular niche; chlamydial inclusion | F09 |
| [36385643](https://pubmed.ncbi.nlm.nih.gov/36385643/) | Biphasic EB–RB developmental cycle | F09 |
| [33594486](https://pubmed.ncbi.nlm.nih.gov/33594486/) | RB binary fission and RB→EB conversion for spread | F09 |
| [22369307](https://pubmed.ncbi.nlm.nih.gov/22369307/) | PCR 100% sens/95.7% spec vs culture; PCR>culture>Giemsa | F10 |
| [21402767](https://pubmed.ncbi.nlm.nih.gov/21402767/) | Guinea pig GPIC model; neutrophils drive pathology | F11 |
| [20065052](https://pubmed.ncbi.nlm.nih.gov/20065052/) | *C. caviae* natural guinea-pig pathogen; 23S rRNA azithromycin resistance | F11 |
| [28693667](https://pubmed.ncbi.nlm.nih.gov/28693667/) | Genotype E (48%) and G (24%) predominance; 39.5% positivity | F12 |
| [35027140](https://pubmed.ncbi.nlm.nih.gov/35027140/) | Oculogenital spectrum incl. inclusion conjunctivitis; prevalence ~2.8%/3.8% | F13 |
| [2247702](https://pubmed.ncbi.nlm.nih.gov/2247702/) | Vertical transmission → inclusion conjunctivitis/interstitial pneumonia; prompt antibiotics eradicate | F13 |
| [3838901](https://pubmed.ncbi.nlm.nih.gov/3838901/) | Age peak 16–20 y (>9%); unilateral presentation | F14 |
| [7427689](https://pubmed.ncbi.nlm.nih.gov/7427689/) | Adult/neonatal chlamydial conjunctivitis marks large genital reservoir | F14 |

---

## Limitations and Knowledge Gaps

- **No omics/molecular-profiling data specific to human ocular inclusion conjunctivitis** (transcriptomics, proteomics, metabolomics, single-cell) were identified; mechanistic immunology relies on the guinea-pig *C. caviae* model and general chlamydial cell biology.
- **Quantitative human immunopathology** (cytokine profiles, follicle histology grading) in inclusion conjunctivitis specifically is sparse; neutrophil causal data come from the animal model.
- **Frequency percentages for individual phenotypes** in adults are not precisely quantified across large cohorts; several estimates are qualitative.
- **Precise incidence/prevalence of the ocular disease** (as opposed to genital chlamydia) is not well defined; figures are inferred from conjunctivitis cohorts and STI prevalence.
- **Scarring risk in inclusion conjunctivitis** is inferred (by analogy to trachoma) to be mild/uncommon rather than directly quantified.
- Some cited abstracts (e.g., [PMID: 42350099](https://pubmed.ncbi.nlm.nih.gov/42350099/), [PMID: 31753423](https://pubmed.ncbi.nlm.nih.gov/31753423/)) had limited or unavailable full text.

---

## Proposed Follow-up Experiments / Actions

1. **Human ocular immunoprofiling:** single-cell RNA-seq / cytokine profiling of conjunctival specimens from confirmed AIC patients to directly test the neutrophil→lymphocyte follicle model in humans (currently only guinea-pig evidence).
2. **Serovar–phenotype correlation:** larger ompA-genotyped AIC cohorts to test whether serovars E/G differ in severity, chronicity, or treatment response.
3. **Antimicrobial resistance surveillance:** monitor 23S rRNA (A2058/A2059) and other resistance markers in ocular *C. trachomatis* isolates given single-dose azithromycin use.
4. **Prevention policy evidence:** prospective evaluation of universal antenatal chlamydia screening vs. neonatal topical prophylaxis for preventing neonatal ocular and pulmonary disease.
5. **Diagnostic pathways:** embed reflex NAAT for persistent/therapy-resistant follicular conjunctivitis to reduce the well-documented diagnostic delay and unnecessary orbital/thyroid workups.
6. **Epidemiologic quantification:** registry-based estimation of true incidence/prevalence of ocular (vs. genital) chlamydial disease, and of neonatal pneumonia progression rates.

---

*Report compiled from 14 confirmed findings and 37 reviewed papers. Evidence types: human clinical cohorts and case series, narrative reviews, and a guinea-pig (*C. caviae*) animal model plus in vitro chlamydial cell biology. Inclusion conjunctivitis is an infectious, non-genetic disease; genetic/genomic sections are annotated "not applicable" where appropriate.*


## Artifacts

- [OpenScientist final report](Inclusion_Conjunctivitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Inclusion_Conjunctivitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 28 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42350099` *(abstract only)*: "*variable hyperaemia, follicular reaction, papillary hypertrophy and mucopurulent discharge*"
  - closest text in source: "RESULTS: Patients presented with subacute or chronic conjunctivitis with variable conjunctival hyperaemia, follicular reaction, papillary hypertrophy and discharge"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005808` (2 mentions) - the report calls it "Mondo"; MONDO calls it **inclusion conjunctivitis**
- `HP:0025421` (1 mention) - the report calls it "Conjunctival hyperemia"; HP calls it **Pneumomediastinum**
- `HP:0000509` (1 mention) - the report calls it "related"; HP calls it **Conjunctivitis**
- `HP:0410019` (1 mention) - the report calls it "regional lymphadenopathy"; HP calls it **Epigastric pain**
- `UBERON:0000964` (1 mention) - the report calls it "Associated structures:** cornea"; UBERON calls it **cornea**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0200019` (1 mention), reported as "related" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000508` (1 mention) - the report calls it "Ptosis, related"; HP calls it **Ptosis**
- `UBERON:0001811` (1 mention) - the report calls it "conjunctiva", "Primary organ/tissue:** the **conjunctiva"; UBERON calls it **conjunctiva**, and lists "tunica conjunctiva" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001811` - called "conjunctiva", "Primary organ/tissue:** the **conjunctiva"
