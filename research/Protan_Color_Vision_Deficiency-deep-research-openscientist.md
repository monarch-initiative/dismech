---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T12:38:15.651015'
end_time: '2026-10-14T13:21:06.849877'
duration_seconds: 2571.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Protan Color Vision Deficiency
  mondo_id: MONDO:0010565
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
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 20
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40769301
  relevance_assessed: 19
  on_topic: 12
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 13
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000573
    reported_labels:
    - L-cone photoreceptors
    ontology_label: retinal cone cell
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Protan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Protan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Protan Color Vision Deficiency
- **MONDO ID:** MONDO:0010565 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Protan Color Vision Deficiency** covering all of the
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

# Protan Color Vision Deficiency: A Comprehensive Disease Characterization

**Disease:** Protan Color Vision Deficiency (Protanopia / Protanomaly)
**MONDO ID:** MONDO:0010565
**Category:** Mendelian (X-linked recessive)
**OMIM:** 303900 ("Colorblindness, partial, protan series"); gene *OPN1LW* 300822
**ICD-10:** H53.54 ("Deficiencies of colour vision"); **ICD-11:** 9D47 Colour vision deficiencies
**MeSH:** Color Vision Defects (D003117); **Orphanet:** Colour blindness (grouping)
**HGNC:** *OPN1LW* HGNC:4206
**Report type:** Literature-synthesis, disease-level (no individual EHR data). Evidence labeled [human clinical], [model organism], [in vitro], or [computational/comparative].

---

## Summary

Protan color vision deficiency (CVD) is a congenital, lifelong, non-progressive, X-linked recessive disorder of red–green color discrimination caused by loss or spectral alteration of the **long-wavelength–sensitive (L) cone photopigment** encoded by *OPN1LW* within the *OPN1LW/OPN1MW* opsin gene tandem array at chromosome **Xq28**. The disorder exists in two forms: **protanopia**, the dichromatic form in which no functional L-pigment is present, and **protanomaly**, the anomalous-trichromatic form in which the L-pigment is replaced by an M-shifted 5′L–3′M hybrid photopigment. A hallmark distinguishing protan from deutan defects is the **reduced luminous sensitivity to long-wavelength (red) light**, which carries real-world safety implications (e.g., perceiving red traffic signals and brake lights as dimmer).

The molecular basis is exceptionally well understood. The L and M opsin genes are >96% identical and arranged head-to-tail in a tandem array flanked by a **locus control region (LCR)**. This high sequence similarity predisposes the array to **unequal homologous recombination**, which generates **gene deletions** and **5′L–3′M hybrid (chimeric) genes** — the predominant mechanism of protan and deutan defects, rather than point mutations. Phenotype type and severity are determined by the amino-acid identity at a small number of **spectral-tuning residues** (notably sites 180, 277, and 285), which set the pigment's wavelength of peak absorption (λmax). Rare, specific exon-3 L-opsin haplotypes (e.g., LIAVA, LVAVA) or the Cys203Arg substitution destabilize the opsin protein and produce a severe allelic branch — **Bornholm Eye Disease** — combining dichromacy with cone dystrophy and high myopia.

Epidemiologically, congenital CVD affects **~2.6% of people globally** with strong male predominance consistent with X-linkage; among European-ancestry men red-green CVD reaches ~8%, with protan defects comprising a minority (~8% of CVD cases vs ~92% deutan). The condition is diagnosed with pseudoisochromatic plates (Ishihara) and confirmed/typed by Nagel anomaloscopy and opsin-gene molecular analysis. Prognosis is benign — there is no systemic morbidity or mortality, and morbidity is confined to color-dependent daily and occupational tasks. **No curative treatment exists**: tinted filters (e.g., ChromaGen) alter but do not reduce deficiency severity, and AAV-mediated opsin gene augmentation remains proof-of-concept in animal models.

---

## Key Findings

### 1. Molecular etiology: altered copy number or sequence of X-linked cone opsin genes [human clinical/molecular]

The core etiology of protan CVD is firmly established. Causative mutations change the **copy number or sequence of the L, M, or S cone opsin genes**; for protan defects, the lesion specifically affects the L-cone opsin gene (*OPN1LW*). Davidoff, Neitz & Neitz (2016) performed direct sequencing and MassArray SNP genotyping of 1,872 subjects (1,074 with psychophysical testing) and correctly classified all protan/deutan red-green defects, with SNPs controlling spectral tuning correlating with Nagel anomaloscopy severity.

> "The genetics underlying inherited color vision deficiencies is well understood: causative mutations change the copy number or sequence of the long (L), middle (M), or short (S) wavelength sensitive cone opsin genes." — [PMID: 27622081](https://pubmed.ncbi.nlm.nih.gov/27622081/)

> "Estimates of defect severity based on SNPs that control photopigment spectral tuning correlated with estimates derived from Nagel anomaloscopy." — [PMID: 27622081](https://pubmed.ncbi.nlm.nih.gov/27622081/)

This finding (F001) anchors the entire disease model: protan CVD is a **Mendelian photopigment disorder**, not a neural or acquired condition, and its severity tracks directly with the molecular spectral-tuning state of the surviving opsin gene(s).

### 2. Mechanism — deletions and L/M hybrid genes from unequal recombination at Xq28 [human clinical/molecular]

Protan deficiency maps to the *OPN1LW* gene (HGNC:4206; OMIM gene 300822) at the **proximal (5′) end** of the *OPN1LW/OPN1MW* tandem array on Xq28; the phenotype "Colorblindness, partial, protan series" is OMIM 303900. The lesions are produced by **intergenic and intragenic unequal homologous recombination** between the highly similar L and M genes, yielding **5′L–3′M hybrid genes** (encoding M-like pigments, causing protanomaly or protanopia depending on the crossover point) and **gene deletions** (removing the L gene entirely). Single-gene dichromats carry only a single X-linked pigment gene, the structural signature of recombination-mediated loss of the L gene (Sharpe et al. 1998).

> "causative mutations change the copy number or sequence of the long (L), middle (M), or short (S) wavelength sensitive cone opsin genes" — [PMID: 27622081](https://pubmed.ncbi.nlm.nih.gov/27622081/)

Molecular analysis of Japanese men by Deeb et al. (1995) identified exon 3 as a **recombination/gene-conversion hotspot** and found abnormal array patterns (deletions, hybrids) in ~5% of men, matching the phenotypic frequency of CVD (F009, F011).

### 3. Phenotype determination by spectral-tuning residues (sites 180, 277, 285) [human psychophysics / in vitro]

The protan phenotype and its severity are set by the **amino-acid identity at key spectral-tuning sites** of the surviving opsin. Sharpe et al. (1998) studied 41 single-gene male dichromats and showed the deduced opsin amino-acid sequence correlated directly with psychophysically measured cone spectral sensitivity and Rayleigh matches.

> "allows for a straightforward correlation between each observer's spectral sensitivity measured at the cornea and the amino acid sequence of his visual pigment" — [PMID: 9822760](https://pubmed.ncbi.nlm.nih.gov/9822760/)

The LWS pigment λmax (~525–560 nm) is tuned by substitutions at a small set of sites — notably **180, 197, 277, 285, and 308** (the "five-site rule") (Davies et al. 2012). The L and M opsins differ by ~15–19 residues, with sites 277 and 285 producing the largest (red↔green) spectral shifts and site **180 (Ser↔Ala)** causing a ~2–5 nm polymorphism that modulates the exact λmax and thus the severity of anomalous trichromacy.

> "amino acid substitutions at five sites (180, 197, 277, 285 and 308) are useful in predicting the λ(max) values of the LWS pigment class" — [PMID: 22349213](https://pubmed.ncbi.nlm.nih.gov/22349213/)

Importantly, the normal L:M cone ratio varies widely (28–93% L; mean ~65% L) among color-normal males (Carroll et al. 2002, [PMID: 12678637](https://pubmed.ncbi.nlm.nih.gov/12678637/)), so the *separation* between the two surviving pigments' λmax — not the cone ratio per se — determines whether color discrimination is normal, anomalous, or absent (F008).

### 4. Severe allelic branch — Bornholm Eye Disease (dichromacy + cone dystrophy + myopia) [human families / in vitro]

A rare but clinically important branch arises when specific L-opsin exon-3 haplotypes destabilize the opsin protein. McClements et al. (2013) studied 7 Bornholm Eye Disease (BED) families and found affected L opsin genes carried a rare exon-3 haplotype (e.g., **LIAVA / LVAVA**) in the first array position. In vitro, the variant opsins trafficked to membranes but were **less stable and produced in reduced amounts**, with defective exon-3 splicing implicated. One family instead carried the deleterious **Cys203Arg** substitution.

> "The variant opsins were, however, less stable than wild type." — [PMID: 23322568](https://pubmed.ncbi.nlm.nih.gov/23322568/)

> "Both mechanisms explain the presence of dichromacy and cone dystrophy." — [PMID: 23322568](https://pubmed.ncbi.nlm.nih.gov/23322568/)

This establishes a mechanistic bridge from simple color deficiency (benign) to a **progressive, sight-threatening cone dystrophy with high myopia** (F010, F012). It is the single exception to the otherwise benign prognosis of protan CVD.

### 5. Epidemiology — ~2.6% global prevalence with strong male predominance [meta-analysis / cross-sectional]

A meta-analysis of 1,703,619 participants across 56 studies in 21 countries estimated global congenital CVD prevalence at **2.59% (95% CI 2.20–3.03%)** (Jeong et al. 2025).

> "The global prevalence of CVD was estimated at 2.59% (95% confidence interval [CI], 2.20-3.03" — [PMID: 40769301](https://pubmed.ncbi.nlm.nih.gov/40769301/)

Male predominance is consistent across cohorts. In a Chinese children's study, prevalence was **2.81% in boys vs 0.16% in girls**, with deutan comprising 91.6% and protan only 8.3% of color-deficient cases.

> "The prevalence of color vision deficiency was 1.68%, with 2.81% in boys and 0.16% in girls. Color-deficient cases consisted of 91.6% deutan and 8.3% protan." — [PMID: 35103751](https://pubmed.ncbi.nlm.nih.gov/35103751/)

### 6. Ancestry variation driven by founder effects/genetic drift [review / cross-sectional]

Red-green CVD prevalence varies substantially by ancestry. Birch's review reported ~8% of European Caucasian men and ~0.4% of women affected, and 4–6.5% of Chinese and Japanese men, attributing differences to **founder events and genetic drift rather than natural selection**.

> "the prevalence of deficiency in European Caucasians is about 8% in men and about 0.4% in women and between 4% and 6.5% in men of Chinese and Japanese ethnicity" — [PMID: 22472762](https://pubmed.ncbi.nlm.nih.gov/22472762/)

> "founder events and genetic drift, rather than natural selection, are the cause of these differences" — [PMID: 22472762](https://pubmed.ncbi.nlm.nih.gov/22472762/)

The Multi-Ethnic Pediatric Eye Disease Study (4,177 children) confirmed ancestry- and sex-specific patterns:

> "The prevalence of CVD among boys was 1.4% for black, 3.1% for Asian, 2.6% for Hispanic, and 5.6% for non-Hispanic white children; the prevalence in girls was 0.0% to 0.5%" — [PMID: 24702753](https://pubmed.ncbi.nlm.nih.gov/24702753/)

(F002, F011)

### 7. Diagnosis — pseudoisochromatic plates with anomaloscopy as gold standard [diagnostic validation]

Protan CVD is diagnosed clinically by **Ishihara pseudoisochromatic plates** (screening), with the **Nagel anomaloscope** (Rayleigh red-green match) as the gold standard for distinguishing dichromacy from anomalous trichromacy and protan from deutan. Digital tests (e.g., DIVE) show excellent agreement with Ishihara and quantify severity along the protan axis.

> "The DIVE and Ishihara tests exhibited excellent agreement in identifying participants with color deficiency (Cohen's kappa = 1.00)" — [PMID: 38396435](https://pubmed.ncbi.nlm.nih.gov/38396435/)

Molecular opsin-gene analysis (MassArray/sequencing) provides definitive confirmation of type and severity (Davidoff-Neitz 2016, [PMID: 27622081](https://pubmed.ncbi.nlm.nih.gov/27622081/)) (F005).

### 8. Quality-of-life impact — functional, not medical [review / cross-sectional]

An integrative review (PRISMA, 20 studies) categorized CVD impacts into daily routine, occupational, product choice, emotional, education, and self-care domains, with work activities most affected.

> "people with some degree of color vision loss face challenges in different aspects of their daily life, especially in their work activities" — [PMID: 30443703](https://pubmed.ncbi.nlm.nih.gov/30443703/)

In 1,426 Egyptian students, those with CVD had significantly higher odds of difficulties in daily and study/work color tasks.

> "Students with colour vision defects had significantly higher odds ratios for difficulties in daily activities and study/work tasks related to colour perception." — [PMID: 33955536](https://pubmed.ncbi.nlm.nih.gov/33955536/)

Protan individuals additionally have reduced luminous sensitivity to long-wavelength light, a distinguishing feature with safety implications (F004).

### 9. No curative treatment; filters do not reduce severity [interventional]

In 80 CVD males (5 protanopes, 18 protanomalous), ChromaGen filters altered the nature of the deficiency without correcting it; no protanope passed any test with any lens.

> "ChromaGen filters may influence the nature of CVD without reducing its severity" — [PMID: 41806157](https://pubmed.ncbi.nlm.nih.gov/41806157/)

> "none of the participants with protanopia passing any of the tests using any ChromaGen lens" — [PMID: 41806157](https://pubmed.ncbi.nlm.nih.gov/41806157/)

(F006)

### 10. Gene therapy — proof-of-concept in preclinical models [model organism]

AAV-mediated opsin gene augmentation has restored L/M-cone function in animal models, establishing proof-of-concept relevant to protan correction. AAV5 vectors expressing human *OPN1LW/OPN1MW* regenerated cone outer segments and rescued M-cone function in M-opsin knockout mice (Deng et al. 2018); AAV8-Y733F expressing human L-opsin rescued cone function for ≥5 months in a C198R all-cone mouse model (Cahill et al. 2026). Optimized primate L-opsin promoters (PR1.7) drive strong cone-specific expression in nonhuman primates.

> "Exogenously expressed human opsins can regenerate cone outer segments and rescue M-cone function in" — [PMID: 29386880](https://pubmed.ncbi.nlm.nih.gov/29386880/)

> "subretinal injection of an AAV-GFP vector containing a 1.7-kb L-opsin promoter (PR1.7) achieved strong and specific GFP expression in all cone photoreceptors" — [PMID: 26603570](https://pubmed.ncbi.nlm.nih.gov/26603570/)

(F003)

### 11. Comparative/evolutionary context [computational/comparative]

The human L/M opsin tandem array arose by **gene duplication**. Old World primates (including humans) have separate X-linked MW/LW genes in a head-to-tail array flanked by an LCR; most New World monkeys have a single polymorphic X-linked opsin gene, so all males are dichromats and trichromacy occurs only in heterozygous females — a natural model of X-linked polymorphic color vision. Howler monkeys independently evolved routine trichromacy via opsin duplication.

> "most New World primates have only a single polymorphic X-linked opsin gene; all males are dichromats and trichromacy is achieved only in those females that possess a different form of this gene on each X chromosome" — [PMID: 10413401](https://pubmed.ncbi.nlm.nih.gov/10413401/)

> "organized into a head-to-tail tandem array flanked on the upstream side by a locus control region (LCR)" — [PMID: 10413401](https://pubmed.ncbi.nlm.nih.gov/10413401/)

(F007)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Unequal homologous recombination** (or gene conversion) occurs within the highly homologous *OPN1LW/OPN1MW* tandem array at Xq28, favored by the >96% sequence identity between the L and M genes and the exon-3 recombination hotspot. *(demonstrated — Deeb 1995, Sharpe 1998)*
   → **leads to** one of two structural outcomes (the mechanism branches here):

   **Branch A — Deletion of the L gene** → only M-type gene(s) remain expressed in the "L" position → **no functional L photopigment** → **protanopia (dichromacy)**.

   **Branch B — 5′L–3′M hybrid (chimeric) gene** in the first array position → encodes a photopigment with an **M-shifted λmax** → the two expressed pigments (hybrid + M) have λmax separated by only a few nm → **protanomaly (anomalous trichromacy)**; the smaller the λmax separation, the more severe the anomaly.

2. The surviving opsin's **amino-acid identity at spectral-tuning sites 180, 277, 285** (and 197, 308) sets the exact λmax of the L-position pigment. *(demonstrated — Sharpe 1998, Davies 2012)*
   → **results in** a shift or collapse of the long-wavelength spectral sensitivity function measured at the cornea.

3. Loss/shift of L-cone spectral sensitivity → **reduced or absent red-green chromatic signal** at the L-vs-M cone-opponent pathway, plus **reduced luminous sensitivity to long-wavelength (red) light** (L cones dominate the luminance channel).
   → **results in** the perceptual phenotype: confusion of reds/greens/browns and dimming of red stimuli. *(demonstrated — psychophysics)*

4. **Clinical manifestation:** congenital, bilateral, non-progressive red-green color confusion with the protan signature (red appears dim), present from birth and stable for life. *(demonstrated)*

**Severe sub-branch (Bornholm Eye Disease):** If the first-array L gene carries a destabilizing exon-3 haplotype (**LIAVA/LVAVA**) or **Cys203Arg**, the opsin protein is **less stable / produced in reduced amounts / mis-spliced** → cone outer-segment dysfunction → **cone dystrophy + high myopia** superimposed on dichromacy. *(demonstrated in vitro — McClements 2013; the splicing contribution is partly inferred)*

### Schematic

```
   Xq28 OPN1LW/OPN1MW tandem array (head-to-tail, LCR upstream)
   LCR --[ L gene (5') ]--[ M gene(s) (3') ]-->
                 |
      unequal recombination / gene conversion (exon-3 hotspot)
         /                                    \
   DELETION of L                        5'L-3'M HYBRID gene
         |                                     |
   no L pigment                        M-shifted pigment (small Δλmax)
         |                                     |
   PROTANOPIA                           PROTANOMALY
  (dichromacy)                     (anomalous trichromacy)
         \                                    /
          --> loss/shift of L-cone spectral sensitivity
          --> reduced red-green opponency + dim red (luminance)
          --> congenital, bilateral, stable red-green CVD
                               |
             (if destabilizing exon-3 haplotype / C203R)
                               v
             Bornholm Eye Disease: + cone dystrophy + myopia
```

### Ontology mapping

| Entity | Term |
|---|---|
| Disease | MONDO:0010565 (protan defect) |
| Gene | *OPN1LW* HGNC:4206, OMIM 300822 |
| Phenotype | HP:0000551 Abnormality of color vision; HP:0011519 Protanomaly / protan defect |
| Cell type | CL:0000573 retinal cone cell (L cone) |
| Anatomy | UBERON:0000966 retina; UBERON:0000970 eye |
| Biological process | GO:0007601 visual perception; GO:0007602 phototransduction; GO:0050908 detection of light stimulus involved in visual perception |
| Cellular component | GO:0001750 photoreceptor outer segment; GO:0016020 membrane (opsin) |
| Chemical | CHEBI:17201 11-cis-retinal (chromophore) |

---

## Anatomical, Temporal, and Population Summary (consolidated)

- **Anatomy:** Retina (UBERON:0000966), specifically **L-cone photoreceptors** (CL:0000573) of both eyes; the defect is **bilateral and symmetric**. The opsin is a membrane protein of the cone outer segment (GO:0001750). No other organ system is involved.
- **Onset/temporal course:** **Congenital** (fixed at conception, germline X-linked); **non-progressive** and **lifelong/stable**. The only progressive presentation is the rare Bornholm Eye Disease branch.
- **Inheritance:** **X-linked recessive**; males (hemizygous) affected, females affected only when homozygous/compound (rare) — explaining the strong male predominance. Carrier females may show subtle anomalies and, by Lyonization and heterozygosity for two pigment alleles, can occasionally be tetrachromatic.
- **Prognosis:** Benign — **no systemic morbidity or mortality**; morbidity is functional/occupational (color-dependent tasks, certain career restrictions such as aviation, electrical work, some military/transport roles).
- **Prevention/counseling:** No primary prevention exists for a germline X-linked trait; genetic counseling can inform carrier risk. There is no newborn screening mandate; school-age pseudoisochromatic screening enables early awareness and career guidance.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [27622081](https://pubmed.ncbi.nlm.nih.gov/27622081/) | Genetic testing as new standard for CVD diagnosis | Human clinical/molecular (n=1,872) | F001, F005, F009 — copy-number/sequence etiology; molecular diagnosis |
| [9822760](https://pubmed.ncbi.nlm.nih.gov/9822760/) | Red/green/hybrid pigments; sequence↔spectral sensitivity | Human psychophysics/molecular (n=41) | F008, F009 — sequence determines spectral sensitivity; single-gene dichromats |
| [22349213](https://pubmed.ncbi.nlm.nih.gov/22349213/) | Spectral tuning of MWS/LWS pigments | In vitro / comparative | F008 — five-site tuning rule (180,197,277,285,308) |
| [12678637](https://pubmed.ncbi.nlm.nih.gov/12678637/) | L:M cone ratio from ERG + genetics | Human (n=62) | F008 — wide normal L:M ratio (28–93% L) |
| [23322568](https://pubmed.ncbi.nlm.nih.gov/23322568/) | Opsin coding variants → cone dysfunction + myopia | Human families + in vitro (7 families) | F010, F012 — Bornholm Eye Disease mechanism |
| [7759069](https://pubmed.ncbi.nlm.nih.gov/7759069/) | Molecular patterns in Japanese men | Human population molecular (n=203) | F009, F011 — hybrids/deletions ~5%; exon-3 hotspot |
| [40769301](https://pubmed.ncbi.nlm.nih.gov/40769301/) | Global prevalence of congenital CVD | Meta-analysis (n=1.7M) | F002 — 2.59% global prevalence |
| [35103751](https://pubmed.ncbi.nlm.nih.gov/35103751/) | CVD & myopia in Chinese children | Cross-sectional | F002 — male predominance; deutan 91.6% vs protan 8.3% |
| [22472762](https://pubmed.ncbi.nlm.nih.gov/22472762/) | Worldwide prevalence of red-green deficiency | Review | F011 — ancestry variation; founder/drift |
| [24702753](https://pubmed.ncbi.nlm.nih.gov/24702753/) | Multi-ethnic pediatric eye disease study | Cross-sectional (n=4,177) | F011 — sex/ancestry-specific prevalence |
| [38396435](https://pubmed.ncbi.nlm.nih.gov/38396435/) | Validation of digital color test (DIVE) | Diagnostic validation | F005 — plate/digital screening, kappa=1.00 |
| [30443703](https://pubmed.ncbi.nlm.nih.gov/30443703/) | Impacts of abnormal color vision (integrative review) | Review (20 studies) | F004, F012 — QoL/occupational impact |
| [33955536](https://pubmed.ncbi.nlm.nih.gov/33955536/) | CVD prevalence/predictors, Egyptian students | Cross-sectional (n=1,426) | F004 — functional difficulty |
| [41806157](https://pubmed.ncbi.nlm.nih.gov/41806157/) | ChromaGen lenses on CVD test performance | Interventional (n=80) | F006 — filters do not reduce severity |
| [29386880](https://pubmed.ncbi.nlm.nih.gov/29386880/) | Human L/M opsins restore M-cone function (mouse) | Model organism | F003 — gene therapy proof-of-concept |
| [26603570](https://pubmed.ncbi.nlm.nih.gov/26603570/) | Cone-specific promoters for gene therapy | Model organism / NHP | F003 — PR1.7 L-opsin promoter |
| [42275379](https://pubmed.ncbi.nlm.nih.gov/42275379/) | Gene therapy in all-cone C203R mouse | Model organism | F003 — AAV L-opsin rescue ≥5 months |
| [10413401](https://pubmed.ncbi.nlm.nih.gov/10413401/) | Evolution of trichromacy by opsin duplication | Comparative genetics | F007 — array origin; NW monkey model |
| [14963105](https://pubmed.ncbi.nlm.nih.gov/14963105/) | Trichromacy + pheromones in howler monkeys | Comparative genetics | F007 — independent opsin duplication |

**Model-organism note:** The mouse is the principal model. Wild-type mice lack an L-opsin (only S and M), so human protan biology is studied via **humanized/knock-in opsin mice** and **all-cone (Nrl−/−) backgrounds**. These recapitulate cone opsin loss and gene-therapy rescue (outer-segment regeneration, ERG restoration) but cannot fully model human **trichromatic perception** or the foveal cone architecture. New World monkeys serve as a natural genetic model of single-locus X-linked polymorphic dichromacy/trichromacy (OPN1LW/MW orthologs; NCBI Taxonomy under Platyrrhini).

---

## Limitations and Knowledge Gaps

1. **Protan-specific vs red-green-combined data.** Most epidemiologic and QoL studies report red-green CVD as a whole; protan-only figures are scarcer. Protan is consistently the minority (~8% of CVD cases), so protan-specific prevalence is roughly ~1% of European-ancestry men — but precise protanope-vs-protanomal breakdowns across ancestries are incompletely characterized.
2. **No human gene-therapy trials for isolated protan CVD.** All restorative evidence is preclinical (mouse, NHP promoter work). The benign, non-degenerative nature of common protan CVD makes a surgical subretinal AAV intervention a difficult risk/benefit proposition; clinical translation is more plausible for the degenerative Bornholm/BCM branch.
3. **Genotype–phenotype fine mapping.** While the five-site rule predicts λmax, individual-level prediction of *anomaloscope matching range* from genotype still carries uncertainty, particularly for intermediate hybrids and the effect of site-180 polymorphism.
4. **Carrier (heterozygous female) phenotypes** — including possible tetrachromacy and subclinical anomalies — are under-quantified in the retrieved literature.
5. **Epigenetic/environmental modifiers.** No strong evidence implicates epigenetic regulation or environmental exposure in *congenital* protan CVD; acquired red-green changes (e.g., in multiple sclerosis, optic neuropathy, diabetes) are a distinct differential, not the Mendelian entity.
6. **Splicing mechanism in BED** is partly inferred; the relative contribution of reduced protein stability vs defective exon-3 splicing to the LIAVA/LVAVA phenotype is not fully resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Protan-stratified meta-analysis:** Re-analyze existing large cohorts to extract protanopia vs protanomaly frequencies by ancestry and sex, improving knowledge-base epidemiology fields.
2. **Genotype→anomaloscope predictive model:** Build and validate a quantitative model mapping opsin array structure + spectral-tuning SNPs to Nagel matching midpoint/range, extending Davidoff-Neitz 2016.
3. **Natural-history registry for exon-3 haplotype carriers (LIAVA/LVAVA/C203R):** Prospectively track myopia and cone-dystrophy progression to define the benign-vs-BED boundary and intervention windows.
4. **Preclinical→clinical gene-therapy pathway for the degenerative branch:** Prioritize AAV L-opsin augmentation (PR1.7/PR2.1 promoters, AAV8-Y733F capsids) for BED/BCM where there is a clear degenerative target, building on the C198R all-cone mouse rescue.
5. **Carrier-female phenotyping study:** Quantify subtle discrimination deficits and potential tetrachromacy in obligate carriers using modern digital tests (DIVE) plus opsin genotyping.
6. **Assistive-technology benchmarking:** Rigorously compare digital aids/apps against filters (which do not reduce severity) for task-specific performance (e.g., signal recognition), given the confirmed null result for ChromaGen.

---

## Conclusion

Protan color vision deficiency is a paradigmatic, molecularly resolved Mendelian photopigment disorder: X-linked recessive loss or spectral alteration of the L-cone opsin (*OPN1LW*, Xq28), arising predominantly through unequal recombination–generated deletions and 5′L–3′M hybrid genes, with phenotype severity set by amino-acid spectral-tuning residues (180/277/285). It is common (~1% of European-ancestry men; ~2.6% CVD overall), benign and non-progressive, diagnosed by pseudoisochromatic plates and anomaloscopy/opsin genotyping, and currently untreatable (filters do not reduce severity; gene therapy is preclinical). A rare destabilizing exon-3 allelic branch (LIAVA/LVAVA; C203R) crosses into sight-threatening Bornholm Eye Disease, the one context where restorative gene therapy has a compelling rationale.


## Artifacts

- [OpenScientist final report](Protan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Protan_Color_Vision_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40769301` *(abstract only)*: "The global prevalence of CVD was estimated at 2.59% (95% confidence interval [CI], 2.20-3.03"
  - closest text in source: "The global prevalence of CVD was estimated at 2.59% (95% confidence interval [CI], 2.20-3.03"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000573` (2 mentions) - the report calls it "L-cone photoreceptors"; CL calls it **retinal cone cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000966` (2 mentions) - the report calls it "Anatomy:** Retina"; UBERON calls it **retina**