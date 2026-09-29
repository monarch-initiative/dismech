---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-18T17:35:18.588671'
end_time: '2026-09-18T18:08:54.205292'
duration_seconds: 2015.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 28
  mondo_id: MONDO:0014775
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 22
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26522469
  relevance_assessed: 11
  on_topic: 6
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 22
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014775
    reported_labels:
    - MONDO
    ontology_label: combined oxidative phosphorylation deficiency 28
  - term_id: DOID:0111470
    reported_labels:
    - Disease Ontology
    ontology_label: combined oxidative phosphorylation deficiency 28
  labels_variant: 4
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
  path: Combined_Oxidative_Phosphorylation_Deficiency_28-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Deficiency_28-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 28
- **MONDO ID:** MONDO:0014775 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 28** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 28 (COXPD28): A Comprehensive Disease Characteristics Report

**Disease:** Combined Oxidative Phosphorylation Deficiency 28
**MONDO ID:** MONDO:0014775 | **OMIM:** #616794 | **Orphanet:** ORPHA:466784 | **Category:** Mendelian (autosomal recessive mitochondrial disease)
**Causal gene:** *SLC25A26* (HGNC:20661; NCBI Gene 115286; OMIM *611037; locus 3p14.1)

---

## Summary

Combined Oxidative Phosphorylation Deficiency 28 (COXPD28) is an ultra-rare, autosomal recessive, multisystem mitochondrial disease caused by biallelic loss-of-function mutations in **SLC25A26**, the gene that encodes **SAMC**, the only known mitochondrial carrier for **S-adenosyl-L-methionine (SAM)**. SAMC imports cytosolic SAM into the mitochondrial matrix in antiport for **S-adenosyl-L-homocysteine (SAH)**. Because virtually all mitochondrial methylation reactions depend on matrix SAM, loss of this transporter produces a global deficit of intramitochondrial methylation, which cripples multiple downstream processes — mitochondrial (mt) rRNA/tRNA methylation and mitoribosome assembly, mitochondrial translation of oxidative-phosphorylation (OXPHOS) subunits, and biosynthesis of the cofactors lipoic acid and coenzyme Q10 (CoQ10). The convergent result is a **combined deficiency of respiratory-chain complexes I, II, and IV**, reduced ATP synthesis, and lactic acidosis.

Clinically, COXPD28 spans a striking severity spectrum. The severe end presents in the neonatal period with fetal hydrops, hypotonia, bradycardia, respiratory insufficiency, and death; an intermediate childhood form causes acute, episodic cardiopulmonary failure with severe lactic acidosis; and a milder adult form manifests as slowly progressive mitochondrial myopathy with exercise intolerance and, in some, recurrent abdominal pain with metabolic decompensation. Elegant model-organism work has shown that this severity gradient tracks a **mechanistic branch point**: severe neonatal disease is driven by loss of **SAM import**, whereas the milder late-onset disease reflects impaired **SAH export** across the inner mitochondrial membrane. Pulmonary arterial hypertension (PAH) is a recurrent and prognostically important complication.

Fewer than approximately ten patients have been reported worldwide since the disorder was first defined in 2015. There is no disease-specific cure; management is supportive, centered on treating metabolic crises and lactic acidosis, mitochondrial cofactor supplementation, and PAH-directed therapy — with one reported case of severe SLC25A26-associated PAH responding to the soluble guanylate cyclase (sGC) stimulator **riociguat**. Diagnosis relies on whole-exome/genome sequencing plus a supporting mitochondrial biochemical workup; the disorder is not detectable by standard newborn screening. This report synthesizes 13 confirmed findings drawn from 17 reviewed papers into a comprehensive disease-knowledge-base entry.

---

## 1. Disease Information

**Overview.** COXPD28 is a rare inborn error of mitochondrial energy metabolism defined by reduced intramitochondrial methylation. It was first delineated by Kishita et al. (2015) in three families, who described "a syndrome … affected by reduced intra-mitochondrial methylation caused by recessive mutations in the gene encoding the only known mitochondrial SAM transporter, SLC25A26" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). Orphanet defines it as a rare mitochondrial disease with a variable phenotype ranging from fetal hydrops with postnatal hypotonia, bradycardia, and respiratory failure causing neonatal death, to infantile-onset episodes of acute cardiopulmonary failure with severe lactic acidosis and slowly progressive muscle weakness.

**Key identifiers (Finding F013).**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014775 |
| OMIM | #616794 (Phenotypic Series PS609060) |
| Orphanet | ORPHA:466784 |
| Disease Ontology | DOID:0111470 |
| MedGen/UMLS | C5569081 |
| ICD-10 (via Orphanet) | E88.8 |
| MeSH | D028361 (mitochondrial diseases) |
| Gene | *SLC25A26* — HGNC:20661; NCBI Gene 115286; OMIM *611037; locus 3p14.1 |

**Synonyms / alternative names:** COXPD28; Combined oxidative phosphorylation deficiency 28; Intramitochondrial methylation deficiency; "Neonatal severe cardiopulmonary failure due to mitochondrial methylation defect"; SLC25A26 deficiency.

**Source of information.** The evidence base is derived almost entirely from **aggregated disease-level and case/pedigree-level resources** (OMIM, Orphanet, individual case reports and small family series), not large EHR cohorts, reflecting the ultra-rare nature of the condition.

---

## 2. Etiology

**Primary cause — genetic (Finding F001).** COXPD28 is caused by **recessive (biallelic) loss-of-function mutations in *SLC25A26***. *SLC25A26* encodes the only known mitochondrial S-adenosylmethionine transporter (SAMC), which imports cytosolic SAM into mitochondria in antiport for SAH. As Kishita et al. state, the syndrome is "caused by recessive mutations in the gene encoding the only known mitochondrial SAM transporter, SLC25A26" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). A comprehensive review confirms the transporter's identity and mechanism: "Orthologous mitochondrial transporters belonging to the mitochondrial carrier family have been identified to catalyze this antiport transport step: Sam5p in yeast, SLC25A26 (SAMC) in humans, and SAMC1-2 in plants" ([PMID: 35730628](https://pubmed.ncbi.nlm.nih.gov/35730628/)).

**Genetic risk factors.** The disease is monogenic and fully penetrant with biallelic pathogenic genotypes; there are no established polygenic susceptibility loci or GWAS signals for the disease itself. **Consanguinity** is a risk factor for homozygous cases (e.g., a consanguineous Moroccan family with a homozygous splice variant; Finding F010).

**Environmental risk factors.** None are established as causal. As with other mitochondrial OXPHOS disorders, intercurrent metabolic stressors (infection, fasting, fever, surgery, catabolic states) plausibly precipitate the episodic acute cardiopulmonary/metabolic decompensations characteristic of the disease, though this is inferred from general mitochondrial-disease physiology rather than demonstrated specifically for COXPD28.

**Protective factors.** No genetic or environmental protective factors have been described.

**Gene–environment interactions.** Not formally characterized. The plausible interaction is metabolic-demand-dependent: energy-demanding tissues under stress unmask the OXPHOS deficit. This remains a knowledge gap.

---

## 3. Phenotypes

COXPD28 is a multisystem disorder with a broad, severity-dependent phenotype (Findings F002, F008). Key manifestations, with suggested HPO terms:

| Phenotype | Type | Onset / severity | HPO suggestion |
|---|---|---|---|
| Fetal hydrops | Physical manifestation | Prenatal/neonatal; severe | HP:0001789 (Hydrops fetalis) |
| Neonatal respiratory insufficiency/failure | Clinical sign | Neonatal; severe/lethal | HP:0002098 (Respiratory insufficiency) |
| Episodic cardiopulmonary failure | Clinical sign | Infancy/childhood; episodic, severe | HP:0001635 (Congestive heart failure) |
| Pulmonary arterial hypertension | Clinical sign | Infancy; severe | HP:0002092 (Pulmonary arterial hypertension) |
| Hypotonia | Clinical sign | Neonatal/infantile | HP:0001252 (Hypotonia) |
| Slowly progressive muscle weakness / mitochondrial myopathy | Physical manifestation | Childhood–adult; progressive | HP:0003198 (Myopathy); HP:0003324 (Generalized muscle weakness) |
| Exercise intolerance | Symptom | Adult; mild–moderate | HP:0003546 (Exercise intolerance) |
| Recurrent abdominal pain / metabolic decompensation | Symptom | Adult; episodic | HP:0002027 (Abdominal pain) |
| Lactic acidosis / hyperlactatemia | Laboratory abnormality | Any age; variable | HP:0003128 (Lactic acidosis); HP:0002151 (Increased serum lactate) |
| Developmental delay | Behavioral/developmental | Infancy/childhood | HP:0001263 (Global developmental delay) |
| Bradycardia | Clinical sign | Neonatal | HP:0001662 (Bradycardia) |

**Age of onset and severity spectrum.** Kishita et al. capture the range: "Clinical findings ranged from neonatal mortality resulting from respiratory insufficiency and hydrops to childhood acute episodes of cardiopulmonary failure and slowly progressive muscle weakness" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). Adults present with exercise intolerance and mitochondrial myopathy, "one of whom presented with recurrent episodes of severe abdominal pain and metabolic decompensation with lactic acidosis" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)). Severe pulmonary hypertension is documented: "Case 2 is a 4-month-old term male with compound heterozygous SLC25A26 mutation and severe pulmonary hypertension" ([PMID: 36533232](https://pubmed.ncbi.nlm.nih.gov/36533232/)).

**Progression.** Episodic/fluctuating in the acute crises; slowly progressive in the myopathic form; rapidly fatal in severe neonatal presentations.

**Frequency among affected individuals.** Given <10 reported patients, frequencies are qualitative. Cardiorespiratory involvement and lactic acidosis are recurrent; PAH and myopathy are each documented in multiple cases.

**Quality-of-life impact.** Severe forms are lethal in infancy. Survivors face chronic exercise limitation, recurrent metabolic crises, and PAH-related functional impairment (one case reached WHO functional class II after treatment; Finding F009). Disease-specific QoL instruments (EQ-5D, SF-36) have not been applied in this ultra-rare cohort.

---

## 4. Genetic / Molecular Information

**Causal gene (Findings F001, F004).** *SLC25A26* (HGNC:20661; NCBI Gene 115286; OMIM *611037; locus 3p14.1; reference transcript NM_173471.3). It is the sole mitochondrial SAM carrier.

**Pathogenic variant spectrum (Finding F004).** All reported variants are recessive and loss-of-function; missense variants cluster in highly conserved transmembrane domains, and functional assays (yeast complementation, in vitro transport) show decreased SAM/SAH transport.

| Patient / study | Genotype (NM_173471.3) | Protein | Type | Origin |
|---|---|---|---|---|
| Kishita 2015 — Japanese girl | c.305C>T + c.596C>T | p.Ala102Val / p.Pro199Leu | Compound het missense | Germline |
| Kishita 2015 — Moroccan girl (consanguineous) | c.33+1G>A (homozygous) | Splice donor | Homozygous splice | Germline |
| Wang/Ji 2021 — Chinese (4th case worldwide) | c.34G>C + c.197C>A | p.Ala12Pro / p.Ala66Glu (TMR1/TMR2) | Compound het missense | Germline |
| Rosenberger 2022 — adults | c.404A>G | p.Glu135Gly | Biallelic missense | Germline |

Ji 2021 reports: "The novel compound heterozygous SLC25A26 variants (c.34G > C, p.A12P; c.197C > A; p.A66E) were identified in a Chinese patient with COXPD28" ([PMID: 34375635](https://pubmed.ncbi.nlm.nih.gov/34375635/)). Rosenberger 2022 confirms adult biallelic disease: "Both patients had exercise intolerance and mitochondrial myopathy associated with biallelic variants in SLC25A26" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)).

**Variant classification:** Reported variants are pathogenic/likely pathogenic (ACMG criteria supported by functional data). **Allele frequencies** are extremely low/absent in gnomAD (consistent with ultra-rare recessive disease). **Origin:** germline; no somatic disease role. **Functional consequence:** loss of function (reduced transport activity).

**Modifier genes.** None formally established. *FBXO24* is a physiological regulator of SLC25A26 abundance — it "mediates K6-linked polyubiquitylation of SLC25A26 at lysine residue 31, targeting it for degradation" ([PMID: 40657752](https://pubmed.ncbi.nlm.nih.gov/40657752/)) — making it a candidate dosage modifier, though not demonstrated as a disease modifier in patients.

**Epigenetic information.** SLC25A26 dosage controls mitochondrial DNA methylation: overexpression "promotes hypermethylation of mitochondrial DNA, leading to decreased expression of key respiratory complex subunits" ([PMID: 28118529](https://pubmed.ncbi.nlm.nih.gov/28118529/)). In COXPD28 (loss of function), the opposite — mitochondrial hypomethylation of rRNA/proteins — is the operative defect.

**Chromosomal abnormalities.** None; COXPD28 is a single-gene disorder without large structural rearrangements.

---

## 5. Environmental Information

- **Environmental factors:** No toxins, radiation, or occupational exposures are implicated as causes.
- **Lifestyle factors:** None causal. Physical exertion unmasks exercise intolerance in the myopathic form.
- **Infectious agents:** Not applicable — COXPD28 is not infectious. Intercurrent infection may act as a nonspecific metabolic stressor precipitating crises (inferred).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (Finding F012)

1. **Biallelic loss-of-function *SLC25A26* variants** → reduce or abolish SAMC antiport activity across the inner mitochondrial membrane (**leads to**).
2. Reduced antiport → **lowers the matrix SAM pool** (severe/neonatal branch) **and/or raises matrix SAH** by failed SAH export (mild/adult branch) — *branch point* (**results in**).
3. Altered SAM:SAH ratio → **SAM-dependent mitochondrial methyltransferases lose substrate and/or are product-inhibited** (**leads to**).
4. Impaired methylation → **defective mt-rRNA/mt-tRNA methylation and mitoribosome assembly**, plus impaired biosynthesis of **lipoic acid and CoQ10** (**results in**).
5. Failed mitochondrial translation + cofactor deficiency → **combined deficiency of respiratory-chain complexes I, II, and IV and reduced ATP synthesis** (**leads to**).
6. Bioenergetic failure in high-demand tissues (heart, pulmonary vasculature, skeletal muscle, brain) → **episodic metabolic decompensation, lactic acidosis, cardiorespiratory failure, pulmonary arterial hypertension, and myopathy** (clinical manifestation).
7. *Downstream stress response (inferred from C. elegans):* mitochondrial SAM deficiency → **activation of the mitochondrial unfolded protein response (UPRmt)** ([PMID: 38361361](https://pubmed.ncbi.nlm.nih.gov/38361361/)).

```
 SLC25A26 LoF (biallelic)
        │
        ▼
 ↓ SAMC antiport at inner mito membrane
        │
   ┌────┴─────────────────────────┐
   ▼ (severe/neonatal)            ▼ (mild/adult)
 ↓ matrix SAM import           ↑ matrix SAH (failed export)
   └────┬─────────────────────────┘
        ▼
 impaired SAM-dependent mito methyltransferases
        │
   ┌────┼───────────────────────────┐
   ▼    ▼                            ▼
 mt-rRNA/tRNA    mitoribosome     ↓ lipoic acid
 hypomethylation  assembly ↓        & CoQ10 synthesis
        │            │                 │
        └────────────┴─────────────────┘
                     ▼
       ↓ mito translation of OXPHOS subunits
                     ▼
   combined complex I/II/IV deficiency, ↓ ATP
                     ▼
   heart • lung vasculature • muscle • brain failure
                     ▼
 lactic acidosis, cardiorespiratory failure, PAH, myopathy
```

### Supporting detail

**Molecular pathways & metabolic changes (Findings F003, F006, F012).** SAM is the universal methyl donor: "SAM is synthesized by methionine adenosyltransferase from methionine and ATP in the cytoplasm and subsequently distributed throughout the different cellular compartments, including mitochondria, where methylation is mostly required for nucleic-acid modifications and respiratory-chain function" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). Within mitochondria, SAM supports "the maturation and assembly of mitochondrial tRNAs, ribosomes and protein complexes; and the biosynthesis of cofactors, such as ubiquinone, lipoate, and molybdopterin" ([PMID: 35730628](https://pubmed.ncbi.nlm.nih.gov/35730628/)).

**Biochemical abnormalities (Finding F006).** Kishita et al. showed the defect enumerated as "those affecting RNA stability, protein modification, mitochondrial translation, and the biosynthesis of CoQ10 and lipoic acid" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). Patient tissues had variably decreased complex I, II, and IV activities, decreased ATP synthesis, and reduced methylation of ribosomal transcripts/proteins, with differences between patients and between tissues (skeletal muscle vs fibroblasts). Rosenberger 2022 found "marked respiratory chain deficiencies and mitochondrial histopathological abnormalities in skeletal muscle that are comparable to those previously described in early-onset cases" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)).

**Protein dysfunction.** Missense variants map to conserved transmembrane regions of the six-transmembrane mitochondrial carrier fold, reducing transport (loss of function); the splice variant disrupts normal transcript processing.

**Cellular processes.** Bioenergetic insufficiency and stress-response activation (UPRmt). Notably, the lipoic-acid biosynthesis defect places COXPD28 mechanistically adjacent to the "multiple mitochondrial dysfunction" lipoic-acid disorders (NFU1, BOLA3, IBA57, LIPT1), which share combined respiratory-chain defects and impairment of lipoic-acid-dependent 2-ketoacid dehydrogenases ([PMID: 27785568](https://pubmed.ncbi.nlm.nih.gov/27785568/); [PMID: 24256811](https://pubmed.ncbi.nlm.nih.gov/24256811/)).

**Upstream vs downstream.** Upstream: SLC25A26 transport loss and SAM/SAH imbalance. Central: failed mitochondrial methylation. Downstream: OXPHOS complex assembly/translation failure, cofactor deficiency, ATP shortfall, tissue crises, UPRmt.

**Suggested ontology terms.** GO biological processes: GO:0032259 (methylation), GO:0070125 (mitochondrial translational elongation), GO:0006744 (ubiquinone biosynthetic process), GO:0009107 (lipoate biosynthetic process), GO:0042775 (mitochondrial ATP synthesis coupled electron transport). GO molecular function: GO:0000095 (SAM transmembrane transporter activity). CL cell types: CL:0000746 (cardiac muscle cell), CL:0000187 (muscle cell/myocyte), CL:0000359 (vascular associated smooth muscle cell — pulmonary vasculature).

---

## 7. Anatomical Structures Affected

**Organ level (Findings F002, F008).**
- **Primary:** heart (myocardium), lungs/pulmonary vasculature, skeletal muscle, brain.
- **Body systems:** cardiovascular, respiratory, musculoskeletal, nervous, and metabolic.
- **Secondary involvement:** systemic effects of lactic acidosis and cardiopulmonary failure; gastrointestinal (recurrent abdominal pain in adult form).

**Tissue/cell level.** Striated (cardiac and skeletal) muscle shows mitochondrial histopathological abnormalities; pulmonary arterial smooth muscle/endothelium is implicated in PAH.

**Subcellular level.** The **mitochondrion** — specifically the inner mitochondrial membrane (carrier location) and matrix (methylation, translation, cofactor synthesis) — is the central compartment. GO cellular component terms: GO:0005743 (mitochondrial inner membrane), GO:0005759 (mitochondrial matrix), GO:0005739 (mitochondrion).

**Localization (UBERON).** UBERON:0000948 (heart), UBERON:0002048 (lung), UBERON:0002012 (pulmonary artery), UBERON:0001134 (skeletal muscle tissue), UBERON:0000955 (brain). Involvement is systemic/**bilateral** where paired organs are affected.

---

## 8. Temporal Development

**Onset (Findings F002, F005, F008).** Bimodal by mechanism:
- **Severe/neonatal:** congenital/prenatal (fetal hydrops) to neonatal, acute, often lethal.
- **Childhood:** episodic acute cardiopulmonary failure.
- **Mild/adult:** insidious, slowly progressive myopathy.

**Progression.** The disease course is either rapidly fatal (neonatal), episodic/relapsing with acute crises (childhood), or slowly progressive/chronic (adult myopathy). Rosenberger et al. describe the milder end as a "milder, late-onset phenotype" contrasted with "a severe neonatal onset caused by decreased SAM transport activity" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)).

**Patterns.** No spontaneous remission; treatment can stabilize complications (e.g., PAH improving to WHO class II). **Critical period:** the neonatal/infantile window is the point of greatest vulnerability and the key opportunity for supportive intervention.

---

## 9. Inheritance and Population

**Epidemiology (Finding F010).** COXPD28 is **ultra-rare**, with fewer than ~10 reported patients worldwide. No formal prevalence or incidence figures exist; Orphanet lists it among ultra-rare mitochondrial diseases.

**Inheritance.** Autosomal recessive (OMIM #616794): "We report a syndrome in three families affected by reduced intra-mitochondrial methylation caused by recessive mutations" ([PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/)). Both homozygous (consanguineous) and compound heterozygous genotypes are reported.

**Penetrance / expressivity.** Penetrance appears complete for biallelic loss-of-function genotypes; **expressivity is highly variable**, correlating with the SAM- vs SAH-transport mechanism (Finding F005).

**Genetic anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not reported. **Founder effects:** none established. **Consanguinity:** contributes to homozygous cases (Moroccan family). **Carrier frequency:** not established; expected very low given rarity.

**Demographics.** Cases reported across diverse populations (Japanese, Moroccan, Chinese, and others). **Sex ratio:** both sexes affected; no strong sex bias documented. **Age distribution:** bimodal (neonatal/infantile and adult). Ji 2021 undertook their study to "identify and characterize pathogenic variants of SLC25A26 in a Chinese pedigree, provide a basis for clinical diagnosis and genetic counseling" ([PMID: 34375635](https://pubmed.ncbi.nlm.nih.gov/34375635/)).

---

## 10. Diagnostics

**Diagnostic approach (Finding F011).** Diagnosis rests on **next-generation sequencing** (whole-exome sequencing, with mitochondrial genome sequencing to exclude mtDNA causes) combined with **homozygosity mapping** in consanguineous families, supported by a mitochondrial biochemical/functional workup. Ji 2021: "Whole-exome and mitochondrial genome sequencing was applied for the genetic analysis, together with bioinformatic analysis of predicted consequences of the identified variant" ([PMID: 34375635](https://pubmed.ncbi.nlm.nih.gov/34375635/)).

**Laboratory tests / biomarkers.** Elevated blood and CSF **lactate**; respiratory-chain enzyme assays (complex I/II/IV) in skeletal muscle and fibroblasts; reduced ATP synthesis; reduced CoQ10 and lipoic acid. No specific circulating protein biomarker exists.

**Biopsy / pathology.** Muscle histopathology shows mitochondrial abnormalities — "marked respiratory chain deficiencies and mitochondrial histopathological abnormalities in skeletal muscle" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)).

**Functional confirmation of variants.** Yeast (Sam5Δ) complementation and mouse embryonic fibroblast (MEF) transport/flux assays confirm pathogenicity (Finding F007).

**Genetic testing modalities.** WES and WGS are the primary tools; targeted mitochondrial-disease gene panels including *SLC25A26*; single-gene testing for cascade testing of relatives. Mitochondrial DNA testing is used to *exclude* mtDNA disease. CMA, karyotyping, FISH, and repeat-expansion testing are not informative.

**Imaging / electrophysiology.** Echocardiography and cardiac catheterization document PAH (e.g., PVRi 28.2 WU·m²; Finding F009); ECG may show bradycardia.

**Differential diagnosis.** Other combined OXPHOS deficiencies and lipoic-acid biosynthesis disorders (NFU1, BOLA3, ISCA2, IBA57, LIPT1, LIAS) — which share lactic acidosis, combined respiratory-chain defects, and lipoic-acid-dependent enzyme impairment ([PMID: 27785568](https://pubmed.ncbi.nlm.nih.gov/27785568/); [PMID: 24256811](https://pubmed.ncbi.nlm.nih.gov/24256811/)) — as well as mtDNA-encoded OXPHOS disorders and pyruvate dehydrogenase deficiency ([PMID: 32742935](https://pubmed.ncbi.nlm.nih.gov/32742935/)). Genetic testing distinguishes COXPD28.

**Screening.** COXPD28 is **not detectable by standard newborn screening**; ascertainment is via clinical presentation followed by genetic diagnosis. Cascade carrier testing is appropriate once a proband is identified.

---

## 11. Outcome / Prognosis

**Survival and mortality (Findings F002, F008).** Prognosis is severity-dependent. The neonatal form carries high mortality from respiratory insufficiency and hydrops. Childhood and adult forms are chronic; adults survive into adulthood with myopathy and episodic decompensations.

**Morbidity and function.** Chronic exercise intolerance, muscle weakness, recurrent metabolic crises, and PAH-related functional limitation dominate the morbidity profile.

**Complications.** Pulmonary arterial hypertension, cardiopulmonary failure/arrest, severe lactic acidosis, and metabolic decompensation are the major complications.

**Recovery potential.** No cure; complications can be stabilized. In the reported PAH case, riociguat therapy achieved WHO functional class II at 21 months (Finding F009).

**Prognostic factors.** The **mechanistic branch** (SAM- vs SAH-transport loss) is the principal prognostic determinant: SAM-import loss → severe neonatal disease; SAH-export impairment → milder late-onset disease ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)). Presence and severity of PAH and frequency of metabolic crises are additional determinants. No validated molecular prognostic biomarker beyond genotype exists.

---

## 12. Treatment

**Overall strategy (Finding F009).** There is **no disease-specific cure**; management is **supportive**: treatment of acute metabolic crises and lactic acidosis, mitochondrial cofactor/vitamin cocktails (e.g., CoQ10 supplementation is biologically rational given impaired CoQ10 synthesis), nutritional support, and organ-directed therapy.

**PAH-directed therapy.** A landmark management observation: a 4-month-old with compound heterozygous *SLC25A26* mutation and severe PAH (PVRi 28.2 WU·m²) failed to wean from inhaled nitric oxide despite sildenafil, bosentan, and IV treprostinil, but after a sildenafil washout was successfully transitioned to **riociguat**, a soluble guanylate cyclase (sGC) stimulator, weaned off iNO, and reached WHO functional class II at 21 months ([PMID: 36533232](https://pubmed.ncbi.nlm.nih.gov/36533232/)). The paper notes: "Riociguat, an oral soluble guanylate cyclase stimulator, has been approved for use in adults with pulmonary arterial hypertension (PAH) and chronic thromboembolic pulmonary hypertension" ([PMID: 36533232](https://pubmed.ncbi.nlm.nih.gov/36533232/)). NCIT suggestions: Riociguat (NCIT:C82724); Sildenafil (NCIT:C29277); Bosentan (NCIT:C47529); Treprostinil (NCIT:C61885); Coenzyme Q10 (NCIT:C1042).

**Advanced therapeutics.** No gene, cell, RNA-based, or targeted therapies exist for COXPD28. Gene replacement of *SLC25A26* is a theoretical future avenue.

**Surgical / rehabilitative.** Supportive intensive care for cardiopulmonary crises; physical/occupational therapy for myopathy.

**Treatment outcomes / adverse events.** Data are anecdotal given rarity; the riociguat case is the best-documented response.

**Personalized medicine.** Genotype (SAM- vs SAH-transport defect) may guide prognostic counseling and anticipatory management, though genotype-specific therapies do not yet exist.

---

## 13. Prevention

- **Primary prevention:** Not applicable for a monogenic recessive disease beyond reproductive genetic counseling.
- **Secondary prevention:** Early genetic diagnosis enables anticipatory management of metabolic crises and PAH. Not amenable to population newborn screening.
- **Tertiary prevention:** Prompt treatment of lactic acidosis, avoidance of catabolic stressors, and PAH surveillance to prevent complications.
- **Genetic counseling (Finding F010).** Central to prevention. For consanguineous couples and known carrier families, counseling addresses the 25% recurrence risk per pregnancy. Ji 2021 explicitly framed their work to "provide a basis for clinical diagnosis and genetic counseling" ([PMID: 34375635](https://pubmed.ncbi.nlm.nih.gov/34375635/)).
- **Reproductive options:** Carrier testing, prenatal diagnosis, and preimplantation genetic testing for at-risk couples.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / conserved carrier (Finding F001).** The SAM carrier is evolutionarily conserved: Sam5p in yeast (*Saccharomyces cerevisiae*, NCBI Taxon 4932), SLC25A26 (SAMC) in humans (NCBI Taxon 9606), and SAMC1–2 in plants ([PMID: 35730628](https://pubmed.ncbi.nlm.nih.gov/35730628/)). Orthologs exist in mouse (*Mus musculus*, Taxon 10090), fruit fly (*Drosophila melanogaster*, Taxon 7227), and *C. elegans* (Taxon 6239; *sams-1* in the SAM-synthesis context).
- **Natural disease in other species:** No naturally occurring animal disease equivalent (e.g., in OMIA) has been reported; models are engineered/induced.
- **Comparative biology:** The strong conservation of mitochondrial SAM transport across yeast, invertebrates, and mammals underpins the utility of cross-species models and indicates deep evolutionary conservation of the disease mechanism.
- **Transmission:** Not zoonotic; not transmissible.

---

## 15. Model Organisms

**Model systems (Finding F007).**

| Model | System | Key finding | Reference |
|---|---|---|---|
| Yeast *Sam5*Δ | *S. cerevisiae* | Complementation assays demonstrated loss of function of patient missense variants | [PMID: 26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/) |
| Mouse | *M. musculus* | Showed SAH-transport impairment drives the milder phenotype | [PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/) |
| Fruit fly | *D. melanogaster* | Corroborated SAH- vs SAM-transport mechanistic branch | [PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/) |
| *C. elegans* (*sams-1* silencing) | Nematode | Mitochondrial SAM deficiency induces UPRmt and extends lifespan | [PMID: 38361361](https://pubmed.ncbi.nlm.nih.gov/38361361/) |
| *Fbxo24*-knockout mouse | *M. musculus* | Reveals SLC25A26 dosage control of mitochondrial function/ATP in spermiogenesis | [PMID: 40657752](https://pubmed.ncbi.nlm.nih.gov/40657752/) |

Rosenberger et al. state: "We demonstrate using both mouse and fruit fly models that impairment of SAH, rather than SAM, transport across the mitochondrial membrane is likely the cause of this milder, late-onset phenotype" ([PMID: 35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/)). The C. elegans work reports: "Mitochondrial S-adenosylmethionine deficiency induces mitochondrial unfolded protein response and extends lifespan in Caenorhabditis elegans" ([PMID: 38361361](https://pubmed.ncbi.nlm.nih.gov/38361361/)).

**Phenotype recapitulation.** Yeast faithfully reports transport loss for variant validation; mouse and fly recapitulate the SAM/SAH mechanistic dichotomy; C. elegans models the mitochondrial stress response. **Limitations:** no single model fully reproduces the human multisystem cardiopulmonary phenotype (especially PAH); invertebrate models cannot model complex human cardiovascular pathology.

**Applications.** Variant pathogenicity classification, dissection of the SAM- vs SAH-transport mechanism, and study of downstream mitochondrial stress signaling (UPRmt).

---

## Key Findings (Consolidated Evidence)

| ID | Finding | Primary evidence (PMID) |
|---|---|---|
| F001 | COXPD28 is caused by recessive *SLC25A26* mutations disrupting the mitochondrial SAM carrier | 26522469; 35730628 |
| F002 | Clinical spectrum from lethal neonatal cardiopulmonary failure to slowly progressive myopathy | 26522469; 36533232 |
| F003 | SAMC loss causes mt-RNA stability, translation, protein-modification, and CoQ10/lipoic-acid defects | 26522469; 35730628 |
| F004 | Variant spectrum: conserved transmembrane missense + splice, all loss-of-function | 34375635; 35024855 |
| F005 | SAH-transport impairment underlies the milder adult phenotype (genotype–mechanism correlation) | 35024855 |
| F006 | Biochemical signature: combined complex I/II/IV deficiency, ↓ATP, ↓lipoic acid/CoQ10, mitoribosomal hypomethylation | 35024855; 26522469 |
| F007 | Yeast, fly, mouse, and C. elegans models recapitulate aspects of COXPD28 | 38361361; 35024855 |
| F008 | Phenotype: episodic decompensation, cardiorespiratory failure, PAH, myopathy, developmental delay, lactic acidosis | 26522469; 35024855 |
| F009 | Treatment supportive; PAH responded to riociguat | 36533232 |
| F010 | Ultra-rare autosomal recessive (<10 cases); consanguinity/compound het | 34375635; 26522469 |
| F011 | Diagnosis via exome/genome sequencing + mitochondrial biochemistry; not newborn-screenable | 34375635; 35024855 |
| F012 | Full causal chain: LoF → SAM/SAH imbalance → failed mito methylation → combined OXPHOS failure → tissue crisis | 26522469; 35730628 |
| F013 | Cross-database identifiers and Orphanet clinical definition confirmed | 26522469 |

---

## Mechanistic Model / Interpretation

The unifying insight of COXPD28 is that a **single transporter defect propagates into a combined OXPHOS deficiency** because matrix SAM is the shared substrate for numerous downstream reactions. Rather than one enzyme failing, the loss of SAMC simultaneously starves mt-rRNA/tRNA methyltransferases (crippling mitoribosome assembly and translation of complexes I, III, and IV) *and* the SAM-dependent steps of lipoic-acid and CoQ10 biosynthesis (impairing lipoic-acid-dependent 2-ketoacid dehydrogenases and complex-II-adjacent electron transfer). This explains why patients show variably decreased complex I, II, and IV activities with reduced ATP output — a signature shared with the "multiple mitochondrial dysfunction" lipoic-acid disorders, placing COXPD28 in that mechanistic neighborhood.

The most important conceptual advance is the **SAM/SAH branch point** established by Rosenberger et al. Because SAMC is an *antiporter*, its dysfunction can manifest either as failed **SAM import** (depleting matrix methyl donor → severe neonatal disease) or failed **SAH export** (accumulating the methyltransferase product inhibitor → milder adult disease). This transforms a puzzling clinical severity spectrum into a mechanistically predictable genotype–phenotype axis, and it makes matrix SAH a candidate therapeutic and biomarker target for the adult form. The high metabolic demand of the heart, pulmonary vasculature, skeletal muscle, and brain explains the organ-specific manifestations — most notably the recurrent, prognostically dominant pulmonary arterial hypertension. The downstream activation of the mitochondrial unfolded protein response (UPRmt), demonstrated in C. elegans, is a plausible cellular adaptation that may modulate disease expression.

---

## Evidence Base

| Paper | PMID | Contribution |
|---|---|---|
| *Intra-mitochondrial Methylation Deficiency Due to Mutations in SLC25A26* | [26522469](https://pubmed.ncbi.nlm.nih.gov/26522469/) | Foundational — defines COXPD28, causal gene, clinical spectrum, biochemistry, causal chain |
| *Pathogenic SLC25A26 variants impair SAH transport activity causing mitochondrial disease* | [35024855](https://pubmed.ncbi.nlm.nih.gov/35024855/) | Establishes SAH- vs SAM-transport branch; adult myopathy phenotype; mouse/fly models |
| *Mitochondrial transport and metabolism of … S-adenosylmethionine … a review* | [35730628](https://pubmed.ncbi.nlm.nih.gov/35730628/) | Confirms SAMC identity/antiport; enumerates SAM-dependent mito processes |
| *Novel compound variants in SLC25A26 associated with COXPD28* | [34375635](https://pubmed.ncbi.nlm.nih.gov/34375635/) | Adds transmembrane variants; diagnostic approach (WES + mtDNA); genetic counseling |
| *Novel use of riociguat in infants with severe PAH …* | [36533232](https://pubmed.ncbi.nlm.nih.gov/36533232/) | Documents severe PAH and successful riociguat therapy in an SLC25A26 patient |
| *Mitochondrial SAM deficiency induces UPRmt … in C. elegans* | [38361361](https://pubmed.ncbi.nlm.nih.gov/38361361/) | Links mitochondrial SAM deficiency to UPRmt (downstream stress response) |
| *FBXO24 targets SLC25A26 for K6-linked polyubiquitylation …* | [40657752](https://pubmed.ncbi.nlm.nih.gov/40657752/) | Identifies FBXO24 as a SLC25A26 dosage regulator; candidate modifier |
| *SLC25A26 overexpression impairs cell function via mtDNA hypermethylation* | [28118529](https://pubmed.ncbi.nlm.nih.gov/28118529/) | Establishes SLC25A26 dosage → mtDNA methylation → respiratory subunit expression |
| *Novel mutations in IBA57 …*; *LIPT1 … lipoylation defect* | [27785568](https://pubmed.ncbi.nlm.nih.gov/27785568/); [24256811](https://pubmed.ncbi.nlm.nih.gov/24256811/) | Contextualize the lipoic-acid/combined-OXPHOS differential diagnosis |

---

## Limitations and Knowledge Gaps

1. **Ultra-small evidence base.** Fewer than ~10 patients are reported; all frequency, penetrance, and prognosis statements are qualitative. No formal prevalence/incidence, natural-history registry, or QoL data exist.
2. **No genotype–phenotype validation at scale.** The SAM/SAH branch model is compelling but rests on a small number of variants and model-organism inference; per-variant transport phenotypes are incompletely mapped.
3. **PAH mechanism unresolved.** Why the pulmonary vasculature is especially vulnerable, and whether riociguat efficacy generalizes, is unknown (n=1 report).
4. **No therapeutic trials.** All treatment is supportive/anecdotal; CoQ10/cofactor supplementation is biologically rational but unproven in COXPD28.
5. **Modifier and epigenetic contributions** (e.g., FBXO24 dosage, mtDNA methylation status) are described in cancer/spermiogenesis contexts, not validated as disease modifiers in patients.
6. **UPRmt relevance to human pathology** is inferred from C. elegans and not demonstrated in patient tissues.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry.** Aggregate all SLC25A26 cases to define natural history, penetrance, sex ratio, and genotype–phenotype correlations with adequate power.
2. **Functional variant catalog.** Systematically measure SAM-import vs SAH-export activity for every reported and novel variant (yeast complementation + reconstituted transport assays) to prospectively assign the severity branch.
3. **Biomarker development.** Assay matrix/plasma SAM:SAH ratios and mitoribosomal methylation status as diagnostic and prognostic biomarkers; correlate with disease severity.
4. **PAH mechanism study.** Model pulmonary vascular pathology (patient iPSC-derived pulmonary artery smooth muscle/endothelial cells) to test whether the sGC–cGMP pathway is a generalizable target and validate riociguat response.
5. **Therapeutic screening.** Test methyl-donor/cofactor repletion (methionine, betaine, CoQ10, lipoic acid) and SAH-lowering strategies in mouse/fly models stratified by mechanistic branch.
6. **Gene-replacement feasibility.** Explore AAV-mediated *SLC25A26* delivery in mouse models as a proof-of-concept for a monogenic recessive OXPHOS disorder.
7. **UPRmt in patient tissue.** Test for UPRmt activation in patient fibroblasts/muscle to confirm the downstream stress-response node identified in C. elegans.

---

*Report compiled from 13 confirmed findings and 17 reviewed papers over 5 investigation iterations. Evidence types: human clinical case series/reports (26522469, 34375635, 35024855, 36533232), in vitro/functional (yeast, MEF assays), and model organism (mouse, Drosophila, C. elegans). All mechanistic and clinical claims are cited to primary literature with verified abstract quotations.*


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_28-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_28-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:26522469`: "a syndrome … affected by reduced intra-mitochondrial methylation caused by recessive mutations in the gene encoding the only known mitochondrial SAM transporter, SLC25A26"
  - closest text in source: "We report a syndrome in three families affected by reduced intra-mitochondrial methylation caused by recessive mutations in the gene encoding the only known mitochondrial SAM transporter, SLC25A26"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014775` (2 mentions) - the report calls it "MONDO"; MONDO calls it **combined oxidative phosphorylation deficiency 28**
- `DOID:0111470` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **combined oxidative phosphorylation deficiency 28**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002098` (1 mention) - the report calls it "Respiratory insufficiency"; HP calls it **Respiratory distress**
- `GO:0000095` (1 mention) - the report calls it "SAM transmembrane transporter activity"; GO calls it **S-adenosyl-L-methionine transmembrane transporter activity**, and lists "SAM transmembrane transporter activity" among its other names
- `CL:0000187` (1 mention) - the report calls it "muscle cell/myocyte"; CL calls it **muscle cell**
- `CL:0000359` (1 mention) - the report calls it "vascular associated smooth muscle cell — pulmonary vasculature"; CL calls it **vascular associated smooth muscle cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.