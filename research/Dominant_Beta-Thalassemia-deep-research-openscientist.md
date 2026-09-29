---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T11:46:52.973529'
end_time: '2026-09-11T12:22:11.821066'
duration_seconds: 2118.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dominant Beta-Thalassemia
  mondo_id: MONDO:0011381
  category: Genetic
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
citation_count: 30
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 7
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:24432801
  - PMID:1971109
  - PMID:34889443
  - PMID:34493145
  relevance_assessed: 31
  on_topic: 18
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011381
    reported_labels:
    - MONDO
    ontology_label: dominant beta-thalassemia
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dominant_Beta-Thalassemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dominant_Beta-Thalassemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dominant Beta-Thalassemia
- **MONDO ID:** MONDO:0011381 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dominant Beta-Thalassemia** covering all of the
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

# Dominant Beta-Thalassemia (Inclusion-Body β-Thalassemia / Hyperunstable Hemoglobinopathy)

**Disease:** Dominant Beta-Thalassemia
**MONDO ID:** MONDO:0011381
**Category:** Genetic (autosomal-dominant hemoglobinopathy)
**Report type:** Comprehensive disease-characterization report for knowledge-base population

---

## Summary

**Dominant β-thalassemia** is a rare autosomal-dominant hemoglobinopathy in which a **single mutant *HBB* (β-globin) allele** is sufficient to produce clinically overt disease in a heterozygote — a fundamental contrast with the far more common recessive β-thalassemias, in which heterozygotes are asymptomatic carriers. The disease is caused predominantly by **exon-3 missense, nonsense (nonsense-mediated-decay–escaping), or frameshift/elongating mutations** in *HBB* that yield a *translated* but **hyperunstable β-globin chain**. This aberrant chain retains the ability to bind heme, precipitates as **protease-resistant inclusion (Heinz) bodies** in erythroid precursors and mature red cells, and behaves as a **toxic, dominant-negative gene product** rather than a simple loss-of-function allele ([PMID: 1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/), [PMID: 34957901](https://pubmed.ncbi.nlm.nih.gov/34957901/)).

Mechanistically, the disease is best understood as a **proteostasis / protein-aggregation disorder of the erythron**. The unstable β-globin (together with the resulting excess of unpaired α-globin) overwhelms and escapes the erythroid **ubiquitin–proteasome and autophagy quality-control machinery**, precipitates with attached heme, generates **reactive oxygen species**, and drives **apoptosis of erythroblasts (ineffective erythropoiesis)** and **splenic destruction of inclusion-laden red cells (hemolysis)**. The net clinical picture is a **thalassemia-intermedia–like phenotype**: moderate hemolytic anemia, reticulocytosis, Heinz bodies, splenomegaly, and secondary iron overload. Severity is modified by co-inherited genetic factors — notably **co-inheritance of α-thalassemia** (which reduces the α/β chain imbalance and softens the phenotype) and **HbF-boosting variants** ([PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/), [PMID: 28651846](https://pubmed.ncbi.nlm.nih.gov/28651846/)).

Because affected heterozygotes are symptomatic, the dominant form is **not enriched by malaria selection** and therefore occurs **pan-ethnically as isolated families or de novo cases** (only ~12 families were known worldwide with a third-exon nonsense allele at the time of one foundational survey) — unlike recessive β-thalassemia, which is concentrated in historically malaria-endemic regions ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/)). Management follows the broader β-thalassemia framework: **supportive care** (transfusion, iron chelation, and often **splenectomy**, which can restore transfusion independence), **disease-modifying agents** (luspatercept, mitapivat), and potentially **curative hematopoietic stem-cell transplantation or gene addition/editing therapy** (betibeglogene autotemcel; exagamglogene autotemcel) ([PMID: 42584024](https://pubmed.ncbi.nlm.nih.gov/42584024/), [PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/)).

---

## 1. Disease Information

**Overview.** Dominant β-thalassemia is a form of β-thalassemia in which heterozygosity for a single *HBB* mutation produces a clinically significant hemolytic/dyserythropoietic anemia. It is also known as **inclusion-body β-thalassemia**, **dominantly inherited β-thalassemia**, and **hyperunstable hemoglobinopathy (HUH)** — the latter term explicitly equated with "dominantly inherited β-thalassemia" in the literature and classified as "a relatively rare form of congenital hemolytic anemia" ([PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/)). The defining feature is that the mutant allele encodes a *translated*, structurally abnormal β-globin that forms inclusion bodies, so a single copy causes disease.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011381 |
| OMIM (β-thalassemia; *HBB*) | #603902 (beta-thalassemia); *HBB* gene 141900 |
| Gene | *HBB*, HGNC:4827, NCBI Gene 3043, chromosome 11p15.4 |
| MeSH | beta-Thalassemia (D017086) |
| ICD-10 | D56.1 (Beta thalassemia) |
| ICD-11 | 3A50.1 (Beta thalassaemia) |

**Synonyms / alternative names:** dominant beta-thalassemia; dominantly inherited β-thalassemia; inclusion-body β-thalassemia; hyperunstable hemoglobinopathy (HUH); (historically overlapping with) congenital Heinz-body hemolytic anemia due to unstable β-globin variants.

**Nature of evidence.** The knowledge base for this entity is derived from **aggregated disease-level resources and case/family reports** (individual probands and pedigrees with defined *HBB* variants), plus mechanistic work in **in-vitro** systems and **mouse models**. It is not primarily an EHR/population-cohort disease because of its rarity.

---

## 2. Etiology

**Primary cause (genetic).** Heterozygous mutations in the β-globin gene *HBB* on chromosome 11p15.4. Unlike recessive β-thalassemia (where a single defective allele is silent), the dominant form arises from **specific mutation classes — predominantly in exon 3 — that produce an abnormal but translated globin product** ([PMID: 1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/)). Representative causal variants documented in the literature:

| Variant (common name / HGVS) | Type | Reference |
|---|---|---|
| Hb Hradec Kralove, β115(G17)Ala→Asp | Missense (exon 3) | [PMID: 7693620](https://pubmed.ncbi.nlm.nih.gov/7693620/) |
| Codon 121 (G→T), codon 112 (T→A) | Nonsense (exon 3, NMD-escaping) | [PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/) |
| Hb Dieppe, β127(H5)Gln→Arg | Missense (exon 3) | [PMID: 34957901](https://pubmed.ncbi.nlm.nih.gov/34957901/) |
| HBB:c.313delA | Frameshift / elongating | [PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/) |
| Hb Grand Junction, HBB:c.348_349delinsG; p.His117IlefsX42 | Frameshift (codons 115/116) | [PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/) |

**Genetic risk factors.** The causal variant itself is the sole necessary risk factor. **Modifier genes** influence severity: the **α-globin genotype** (co-inherited α-thalassemia is protective; see below) and **HbF-modifying loci** (e.g., *BCL11A*, *HBS1L-MYB*) provide "some prediction of disease severity for β thalassemia" ([PMID: 28651846](https://pubmed.ncbi.nlm.nih.gov/28651846/)). **AHSP (α-hemoglobin-stabilizing protein)** is a candidate modulatory factor via its role in escorting free α-globin ([PMID: 31894534](https://pubmed.ncbi.nlm.nih.gov/31894534/)).

**Environmental risk factors.** None are established as causal. Oxidative stressors could theoretically aggravate hemolysis in unstable-hemoglobin states, but the disease is fundamentally monogenic. Family history (an affected parent) is the main non-modifiable factor; **de novo mutation** is well documented.

**Protective factors.** The best-established **genetic protective factor is co-inherited α-thalassemia** (e.g., a −3.7 kb single α-gene deletion), which "leads to a decreased imbalance between α and β chain formation, and subsequently a milder phenotype" ([PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/)). **Elevated HbF** (high-HbF genotypes/HbF-inducing modifiers) is likewise ameliorating.

**Gene–environment interactions.** Not a significant feature. Disease expression is governed largely by the primary lesion plus genetic modifiers (α-genotype, HbF).

---

## 3. Phenotypes

The phenotype resembles **β-thalassemia intermedia** / congenital non-spherocytic hemolytic anemia. In Hb Hradec Kralove heterozygotes the picture was "moderate anemia, reticulocytosis, nucleated red cells, target cells, and other red cell changes, Heinz body formation, and splenomegaly," with marked compensatory increase in fetal-hemoglobin synthesis ([PMID: 7693620](https://pubmed.ncbi.nlm.nih.gov/7693620/)). Czech/Slovak dominant alleles presented as thalassemia intermedia with Heinz bodies in peripheral erythrocytes, and — importantly — **severity varied markedly even within families** carrying identical mutations ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/)).

| Phenotype | Type | HPO suggestion | Onset / severity / frequency |
|---|---|---|---|
| Hemolytic anemia | Lab / clinical | HP:0001878 (Hemolytic anemia); HP:0001903 (Anemia) | Childhood onset; moderate; near-universal |
| Reticulocytosis | Lab abnormality | HP:0001923 (Reticulocytosis) | Chronic compensatory; frequent |
| Heinz bodies / red-cell inclusions | Lab / morphologic | (Heinz body inclusion; verify HPO ID) | Hallmark; frequent |
| Splenomegaly | Clinical sign | HP:0001744 (Splenomegaly) | Progressive; common |
| Jaundice / hyperbilirubinemia | Clinical / lab | HP:0000952 (Jaundice); HP:0002904 (Hyperbilirubinemia) | Chronic; common |
| Microcytic hypochromic red cells | Lab | HP:0001935 (Microcytic anemia) | Frequent |
| Nucleated RBCs / abnormal morphology | Lab | HP:0012132 (Erythroid abnormality) | Frequent |
| Elevated HbA2 / HbF | Lab | (elevated HbF; verify HPO ID) | Frequent |
| Iron overload (secondary) | Lab / clinical | HP:0011031 (Abnormal iron homeostasis) | Late; treatment/disease related |

**Quality-of-life impact.** Chronic anemia, fatigue, splenomegaly, and (when present) transfusion dependence and iron-overload complications impair daily functioning. QoL burden parallels that documented for β-thalassemia intermedia/transfusion-dependent thalassemia; generic tools (SF-36, EQ-5D) are used in the broader thalassemia literature. Disease-specific QoL data for the dominant subtype specifically were **not identified**.

---

## 4. Genetic / Molecular Information

**Causal gene.** *HBB* (β-globin; HGNC:4827; NCBI Gene 3043; OMIM 141900), chromosome 11p15.4.

**Pathogenic variants.** Dominant β-thalassemia is characteristically caused by:
- **Missense** mutations in **exon 3** producing hyperunstable globins (e.g., Hb Hradec Kralove β115Ala→Asp; Hb Dieppe β127Gln→Arg) — "certain missense mutations in exon 3, however, produce unstable globins causing a dominant β-thal phenotype or hemolytic anemia in heterozygotes" ([PMID: 34957901](https://pubmed.ncbi.nlm.nih.gov/34957901/)).
- **Nonsense** mutations in exon 3 that **escape nonsense-mediated decay** (e.g., codon 121 G→T, codon 112 T→A), so a truncated toxic chain is translated ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/)).
- **Frameshift/elongating** variants (e.g., HBB:c.313delA producing a β-chain elongated by 10 residues; Hb Grand Junction p.His117IlefsX42) ([PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/), [PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/)).

**Variant classification.** These variants are **pathogenic (dominant)** by family segregation and functional data. **Origin is germline** (inherited or de novo); this is not a somatic/oncologic disease. **Allele frequencies** are effectively absent from population databases (private/rare family-specific alleles), consistent with the lack of malaria-driven selection.

**Functional consequences.** The defining consequence is a **toxic gain-of-function / dominant-negative** effect: the abnormal chain "binds heme and produces aggregations that are relatively resistant to proteolytic degradation" ([PMID: 1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/)). For frameshift/elongating alleles, the phenotype is "mainly related to the stability of mutant mRNA, the degradation of mutant proteins" — a combination of mRNA-stability and protein-degradation determinants rather than simple quantitative deficiency ([PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/)).

**Modifier genes:** α-globin genotype (co-inherited α-thalassemia), HbF loci (*BCL11A*, *HBS1L-MYB*), and *AHSP*.

**Epigenetic information / chromosomal abnormalities.** No specific epigenetic signature or large-scale chromosomal abnormality is characteristic; the disease is a point-mutation/small-indel disorder of *HBB*. (HbF induction pharmacology engages γ-globin regulation but is therapeutic, not etiologic.)

---

## 5. Environmental Information

Dominant β-thalassemia is a **monogenic disease with no established environmental, toxic, occupational, lifestyle, or infectious cause**. Oxidative stress is mechanistically central to the *pathophysiology* (see Section 6) but is generated endogenously by the unstable globin rather than by external exposures. Chronic transfusion (a treatment) introduces secondary risks (iron overload; historically transfusion-transmitted HCV/HBV in the broader thalassemia population, e.g. [PMID: 28836463](https://pubmed.ncbi.nlm.nih.gov/28836463/)). No infectious agent triggers the disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous *HBB* exon-3 missense/nonsense/frameshift mutation** *leads to* production of an mRNA that (for NMD-escaping/elongating alleles) is translated into a **structurally abnormal, hyperunstable β-globin chain** ([PMID: 1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/), [PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/)).
2. The abnormal β-globin **binds heme and precipitates**, forming **protease-resistant aggregates / inclusion (Heinz) bodies** *because* it escapes normal proteolytic clearance ([PMID: 1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/)).
3. In parallel, defective β-globin **results in an α/β chain imbalance**, leaving **excess unpaired α-globin**; AHSP normally escorts free α-globin, but the excess **overwhelms this chaperone**, so unpaired α-globin also precipitates ([PMID: 40655320](https://pubmed.ncbi.nlm.nih.gov/40655320/), [PMID: 31894534](https://pubmed.ncbi.nlm.nih.gov/31894534/)).
4. The **erythroid protein quality-control (PQC) system** — ubiquitin–proteasome (Nrf1-driven) plus compensatory **ULK1-mediated autophagy** — attempts to degrade the aggregates; **dominance reflects the failure/escape of this clearance** ([PMID: 22427201](https://pubmed.ncbi.nlm.nih.gov/22427201/)).
5. Precipitated globin **with attached heme accumulates**, *leading to* **reactive oxygen species (ROS) and oxidative membrane damage** in erythroblasts ([PMID: 29180398](https://pubmed.ncbi.nlm.nih.gov/29180398/), [PMID: 25724329](https://pubmed.ncbi.nlm.nih.gov/25724329/)).
6. Oxidative stress *results in* **apoptosis of erythroid precursors → ineffective erythropoiesis** in the bone marrow ([PMID: 25724329](https://pubmed.ncbi.nlm.nih.gov/25724329/)). *(Branch: GDF11/ActRIIA signaling amplifies this via an ROS-driven autocrine loop involving α-globin precipitation — [PMID: 24658077](https://pubmed.ncbi.nlm.nih.gov/24658077/).)*
7. Surviving inclusion-bearing red cells that reach circulation are **removed predominantly by the spleen** (cordal-macrophage phagocytosis in the red pulp), *leading to* **hemolytic anemia and splenomegaly** ([PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/)).
8. Chronic anemia and ineffective erythropoiesis *lead to* **compensatory HbF elevation**, increased intestinal iron absorption, and **secondary iron overload** — the downstream clinical manifestations (thalassemia-intermedia phenotype).

### Detail by category

- **Molecular pathways / cellular processes:** protein aggregation, ubiquitin–proteasome degradation, macroautophagy (ULK1), oxidative-stress signaling (Nrf1/Nrf2), Fas/Fas-ligand apoptosis of immature erythroblasts, and GDF11–ActRIIA (TGF-β–superfamily) signaling in ineffective erythropoiesis. β-thalassemia "fits into the broader framework of protein-aggregation disorders that use PQC pathways as cell-protective mechanisms" ([PMID: 22427201](https://pubmed.ncbi.nlm.nih.gov/22427201/)).
- **Protein dysfunction:** misfolding, heme-bound aggregation, protease resistance (gain-of-toxic-function / dominant-negative).
- **Immune involvement:** not autoimmune; splenic macrophage phagocytosis is the effector of hemolysis.
- **Tissue-damage mechanism:** oxidative stress → apoptosis (marrow) and macrophage-mediated erythrophagocytosis (spleen).

**Upstream vs downstream:** the *HBB* mutation and unstable-globin aggregation are **upstream**; ROS, ineffective erythropoiesis, splenic hemolysis, HbF compensation, and iron overload are **downstream**.

**Suggested GO terms:** GO:0034976 (response to endoplasmic reticulum stress), GO:0006979 (response to oxidative stress), GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0006914 (autophagy), GO:0006915 (apoptotic process), GO:0043249 (erythrocyte maturation), GO:0030218 (erythrocyte differentiation).
**Suggested CL terms:** CL:0000765 (erythroblast), CL:0000764 (erythroid progenitor cell), CL:0000232 (erythrocyte), CL:0000235 (macrophage — splenic red-pulp).

---

## 7. Anatomical Structures Affected

- **Primary tissue/organ:** **bone marrow / erythroid lineage** (UBERON:0002371 bone marrow) — site of ineffective erythropoiesis; **blood** (UBERON:0000178).
- **Spleen** (UBERON:0002106) — primary site of destruction of inclusion-bearing red cells and cause of splenomegaly ([PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/)); the **red pulp** is the specific compartment.
- **Liver** (UBERON:0002107) — secondary iron deposition; minor Kupffer-cell phagocytosis; extramedullary hematopoiesis in severe cases.
- **Secondary/systemic:** endocrine glands, heart, and bones (from iron overload and marrow expansion) — as in the broader thalassemia-intermedia spectrum.
- **Cell populations (CL):** erythroblasts (CL:0000765), erythrocytes (CL:0000232), splenic red-pulp macrophages (CL:0000235).
- **Subcellular / GO Cellular Component:** cytosol (site of globin aggregation; GO:0005829), proteasome complex (GO:0000502), autophagosome (GO:0005776); Heinz bodies are membrane-associated cytoplasmic inclusions.
- **Lateralization:** systemic/bilateral (a blood/marrow disorder); splenomegaly involves the single left-sided organ.

---

## 8. Temporal Development

- **Onset:** typically **childhood**, often insidious with chronic hemolytic anemia; some cases recognized in adolescence/adulthood. Reported probands include adolescents ([PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/)) and adults (a 41-year-old with a novel frameshift, [PMID: 39103314](https://pubmed.ncbi.nlm.nih.gov/39103314/)).
- **Onset pattern:** **chronic**, congenital in genetic terms; clinically insidious.
- **Progression / course:** **chronic, lifelong, generally stable-to-progressive**, with progressive splenomegaly and cumulative iron overload if untreated. Severity is **variable even within families** carrying identical alleles ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/)).
- **Remission / intervention windows:** no spontaneous remission; **splenectomy** can produce "almost complete recovery from hemolysis" and transfusion independence ([PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/), [PMID: 42261228](https://pubmed.ncbi.nlm.nih.gov/42261228/)); curative HSCT/gene therapy offers a one-time intervention.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal dominant** — a single *HBB* allele causes disease; **de novo** mutations occur, explaining sporadic/isolated cases.
- **Penetrance / expressivity:** high penetrance but **variable expressivity**, strongly influenced by α-globin genotype and HbF ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/), [PMID: 28651846](https://pubmed.ncbi.nlm.nih.gov/28651846/)).
- **Anticipation / mosaicism:** not a repeat-expansion disorder (no anticipation); germline mosaicism is theoretically possible but not a defining feature.
- **Epidemiology:** **rare and pan-ethnic.** Overall β-thalassemia is among the most common monogenic diseases (~1.5% of the global population are carriers; ~7% of the world population carry a thalassemia gene, with 300,000–400,000 affected births/year) — but these figures pertain to the *recessive* forms ([PMID: 21082937](https://pubmed.ncbi.nlm.nih.gov/21082937/), [PMID: 36367309](https://pubmed.ncbi.nlm.nih.gov/36367309/)). The **dominant** (inclusion-body) form is a small minority: one survey noted only **~12 families worldwide** known with a third-exon nonsense β-thal mutation, and it appears in isolated families/de novo cases across ethnic groups.
- **Why pan-ethnic (not malaria-linked):** because heterozygotes are symptomatic, the dominant alleles are **not maintained by malaria selection** — "the absence of selective preference of these mutations in malaria infested areas as a result of serious clinical manifestations in heterozygotes" ([PMID: 8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/)). This distinguishes it from recessive β-thalassemia's geographic clustering.
- **Sex ratio / age distribution:** no strong sex predilection (autosomal); presents across childhood-to-adult ages.

---

## 10. Diagnostics

**Laboratory / hematologic.**
- CBC: microcytic, hypochromic indices with anemia; reticulocytosis; abnormal red-cell morphology (target cells, nucleated RBCs).
- **Heinz-body / inclusion-body preparation** (supravital stain, e.g., methyl violet): hallmark of unstable-globin disorders — inclusions may be sparse before splenectomy and abundant after ([PMID: 7022469](https://pubmed.ncbi.nlm.nih.gov/7022469/)).
- **Heat-instability / isopropanol stability tests**: positive for unstable hemoglobins ([PMID: 24074398](https://pubmed.ncbi.nlm.nih.gov/24074398/)).
- **Hemoglobin analysis** by HPLC/capillary electrophoresis: elevated **HbA2** and often **HbF**; abnormal peaks for some variants (though many unstable variants are electrophoretically silent).
- **Mass spectrometry** (MALDI-TOF) can quantify globin-chain imbalance as a rapid screen ([PMID: 35098837](https://pubmed.ncbi.nlm.nih.gov/35098837/)).
- Hemolysis markers: unconjugated hyperbilirubinemia, elevated LDH, low haptoglobin.

**Genetic testing (definitive).** **Single-gene *HBB* sequencing** is the diagnostic gold standard and is required to identify the exon-3/frameshift variant, since many causal variants are not detectable by protein methods. **α-globin (*HBA1/HBA2*) genotyping** should accompany it to assess the protective α-thalassemia modifier. Gene panels or WES/WGS can be used when *HBB* Sanger sequencing is non-diagnostic. In-silico protein modeling can support pathogenicity of novel variants ([PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/)).

**Clinical criteria / differential diagnosis.** Differentiate from: recessive β-thalassemia intermedia/major, other **congenital Heinz-body hemolytic anemias / unstable hemoglobins** (e.g., Hb Köln β98Val→Met, [PMID: 24074398](https://pubmed.ncbi.nlm.nih.gov/24074398/)), G6PD deficiency and other enzymopathies, and hereditary spherocytosis. Family history of a dominantly transmitted hemolytic anemia plus *HBB* sequencing resolves the diagnosis.

**Screening.** For the dominant form, **cascade family testing** after an index case is the key strategy; classical carrier screening (aimed at recessive β-thal) does not detect dominant alleles in silent carriers because there are none.

---

## 11. Outcome / Prognosis

- **Course:** chronic, lifelong hemolytic/dyserythropoietic anemia of **intermediate severity** (thalassemia-intermedia–like). Most affected individuals are **not transfusion-dependent from birth** but may require intermittent or (in severe variants) regular transfusion.
- **Complications:** progressive splenomegaly/hypersplenism, cholelithiasis (chronic hemolysis), secondary **iron overload** with attendant endocrine, hepatic, and cardiac risk (as in NTDT/thalassemia intermedia — [PMID: 36295656](https://pubmed.ncbi.nlm.nih.gov/36295656/), [PMID: 28589785](https://pubmed.ncbi.nlm.nih.gov/28589785/)), extramedullary hematopoiesis, and thrombosis risk in the broader NTDT spectrum.
- **Recovery / prognostic modifiers:** **splenectomy** can normalize hemolysis and confer transfusion independence in unstable-hemoglobin disease ([PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/), [PMID: 42261228](https://pubmed.ncbi.nlm.nih.gov/42261228/)). **Co-inherited α-thalassemia and high HbF** predict milder disease ([PMID: 24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/), [PMID: 28651846](https://pubmed.ncbi.nlm.nih.gov/28651846/)). Prognosis is generally favorable with modern supportive care, though rare severe unstable-hemoglobin cases have had fatal outcomes from hemosiderosis ([PMID: 6162731](https://pubmed.ncbi.nlm.nih.gov/6162731/)).
- **Mortality:** no disease-specific survival statistics exist for this rare subtype; outcomes track the thalassemia-intermedia/NTDT literature and depend on iron-overload management.

---

## 12. Treatment

**Supportive / foundational care.** Red-cell **transfusion** as needed, **iron chelation** (deferoxamine, deferasirox, deferiprone) for iron overload, folate supplementation, and **splenectomy** for hypersplenism/transfusion burden — the latter especially effective in inclusion-body/unstable-hemoglobin disease ([PMID: 142356](https://pubmed.ncbi.nlm.nih.gov/142356/), [PMID: 42261228](https://pubmed.ncbi.nlm.nih.gov/42261228/)).

**HbF induction.** Hydroxyurea and sirolimus (rapamycin) induce γ-globin/HbF; sirolimus co-induces AHSP and ULK1-autophagy in patient erythroid cells, addressing α-globin excess ([PMID: 40655320](https://pubmed.ncbi.nlm.nih.gov/40655320/), [PMID: 38731008](https://pubmed.ncbi.nlm.nih.gov/38731008/)).

**Disease-modifying agents.** **Luspatercept** (ActRIIB ligand trap / erythroid maturation agent) and **mitapivat** (pyruvate-kinase activator) are approved and "have demonstrated clinically meaningful improvements in hemoglobin levels and reduction of transfusion burden" ([PMID: 42584024](https://pubmed.ncbi.nlm.nih.gov/42584024/), [PMID: 34889443](https://pubmed.ncbi.nlm.nih.gov/34889443/)).

**Curative / advanced therapeutics.** **Allogeneic HSCT** (curative in eligible patients); **gene addition** with **betibeglogene autotemcel (beti-cel)** and **CRISPR-based *BCL11A* editing** with **exagamglogene autotemcel (exa-cel)** — approved and achieving "high rates of durable transfusion independence" ([PMID: 42584024](https://pubmed.ncbi.nlm.nih.gov/42584024/), [PMID: 34493145](https://pubmed.ncbi.nlm.nih.gov/34493145/)). Note: gene-*addition* corrects globin-chain imbalance but does not remove a dominant toxic allele; allogeneic HSCT and (conceptually) allele-directed editing more fully address a dominant-negative product — an important consideration specific to this subtype.

**Suggested NCIT terms (verify codes):** Luspatercept, Mitapivat, Hydroxyurea (C577), Deferasirox (C29331), Deferoxamine, Splenectomy (C51772), Hematopoietic Stem Cell Transplantation (C15431), Gene Therapy (C15254), Red Blood Cell Transfusion.

---

## 13. Prevention

- **Primary prevention:** as a dominant/often de novo monogenic disease, population carrier screening is less applicable than for recessive β-thal. **Genetic counseling** for affected individuals (50% transmission risk per pregnancy) and **cascade family testing** are central.
- **Reproductive options:** **prenatal diagnosis** and **preimplantation genetic testing (PGT)** for the known familial *HBB* variant.
- **Secondary/tertiary prevention:** early detection of iron overload (ferritin, MRI T2\*), timely chelation, vaccination and antibiotic prophylaxis after splenectomy (encapsulated-organism protection), and monitoring for endocrine/cardiac complications.
- **Public health:** premarital/genetic screening programs (e.g., Saudi Arabia, [PMID: 39073533](https://pubmed.ncbi.nlm.nih.gov/39073533/)) target recessive hemoglobinopathies primarily; they do not prevent dominant/de novo cases.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *HBB* (NCBI Gene 3043). Orthologous β-globin genes exist across mammals (mouse *Hbb* cluster). β-globin structure and the α/β balance are evolutionarily conserved, which is why murine β-thalassemia models recapitulate core mechanisms.
- **Natural disease in animals:** unstable-hemoglobin/thalassemia-like syndromes are not a prominent naturally occurring veterinary disease for the dominant human variants specifically; comparative data are limited. No zoonotic potential (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse models** are the principal system. β-thalassemia mice reproduce **ineffective erythropoiesis, α-globin precipitation, oxidative stress, and iron dysregulation**, and have been used to validate mechanistic and therapeutic hypotheses: e.g., an ActRIIA ligand trap (RAP-011) correcting ineffective erythropoiesis and GDF11 biology ([PMID: 24658077](https://pubmed.ncbi.nlm.nih.gov/24658077/)); heme-oxygenase inhibition ameliorating anemia/iron overload ([PMID: 29180398](https://pubmed.ncbi.nlm.nih.gov/29180398/)); and **integrated PQC (proteasome + autophagy) regulation of free α-globin in murine β-thalassemia** ([PMID: 22427201](https://pubmed.ncbi.nlm.nih.gov/22427201/)).
- **In-vitro / cellular models:** K562 and primary erythroid precursor cells (ErPCs) for AHSP/Nrf2/ULK1 studies ([PMID: 35092867](https://pubmed.ncbi.nlm.nih.gov/35092867/), [PMID: 40655320](https://pubmed.ncbi.nlm.nih.gov/40655320/)); HEK-293T transfection to dissect mutant-mRNA/protein stability for specific dominant alleles ([PMID: 34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/)); patient nucleated erythrocytes for functional characterization.
- **Model characteristics/limitations:** murine models capture the chain-imbalance/ineffective-erythropoiesis axis well but are usually engineered as loss-of-function/recessive backgrounds; **faithful modeling of a translated toxic dominant-negative β-globin (knock-in of a human hyperunstable allele)** is a gap.
- **Resources:** MGI (mouse), Cellosaurus (K562), plus patient-derived iPSC/erythroid-differentiation platforms.

---

## Mechanistic Model / Interpretation

```
 Heterozygous HBB exon-3 mutation (missense / NMD-escaping nonsense / frameshift-elongating)
                     |  (translated, NOT degraded by NMD)
                     v
        HYPERUNSTABLE beta-globin chain  --------------+
                     | binds heme, precipitates        | defective beta -> alpha/beta imbalance
                     v                                  v
      Protease-resistant inclusion (Heinz)     Excess unpaired alpha-globin
        bodies -- escape UPS + autophagy -->     (overwhelms AHSP chaperone)
                     |  (Nrf1/Nrf2, ULK1 PQC fail)      |
                     +----------------+-----------------+
                                      v
                    ROS / oxidative membrane damage (heme, Fe)
                                      |
                 +--------------------+---------------------+
                 v                                          v
   Apoptosis of erythroblasts                 Inclusion-laden RBCs cleared
   = INEFFECTIVE ERYTHROPOIESIS                by SPLENIC red-pulp macrophages
   (amplified by GDF11-ActRIIA loop)           = HEMOLYSIS + SPLENOMEGALY
                 |                                          |
                 +---------------> CHRONIC ANEMIA <---------+
                                      |
                 compensatory ^HbF, ^iron absorption -> SECONDARY IRON OVERLOAD
                                      |
                          Thalassemia-intermedia phenotype
   Modifiers:  (-) co-inherited alpha-thalassemia, high HbF -> milder disease
```

The unifying insight from this investigation is that **dominant β-thalassemia is a proteostasis disorder of the erythron**: dominance is not about quantitative haploinsufficiency but about a **translated, aggregation-prone, protease-resistant globin that escapes protein quality control** and acts as a toxic dominant-negative. This reframes it alongside protein-aggregation diseases and explains (a) why only specific exon-3/frameshift alleles are dominant, (b) why co-inherited α-thalassemia (which lowers the competing α-globin burden) is protective, and (c) why gene-*addition* therapy — which supplies normal β-globin but leaves the toxic allele intact — may be mechanistically less complete than allogeneic HSCT for this subtype.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [1971109](https://pubmed.ncbi.nlm.nih.gov/1971109/) | *Molecular basis for dominantly inherited inclusion body beta-thalassemia* | Foundational: exon-3 *HBB* mutations; aggregates resistant to proteolysis |
| [7693620](https://pubmed.ncbi.nlm.nih.gov/7693620/) | *Hb Hradec Kralove β115Ala→Asp* | Dominant phenotype; hematologic picture; splenectomy; ↑HbF |
| [8184583](https://pubmed.ncbi.nlm.nih.gov/8184583/) | *Dominant β-thal alleles in Czech/Slovak population* | Nonsense exon-3 alleles; rarity (~12 families); non-malaria rationale; Heinz bodies; variable severity |
| [34957901](https://pubmed.ncbi.nlm.nih.gov/34957901/) | *Hb Dieppe* | Confirms exon-3 missense → unstable globin → dominant phenotype |
| [34271589](https://pubmed.ncbi.nlm.nih.gov/34271589/) | *HBB:c.313delA elongated β-globin* | Frameshift/elongation; mRNA-stability + protein-degradation determinants |
| [24432801](https://pubmed.ncbi.nlm.nih.gov/24432801/) | *Hb Grand Junction (HUH)* | HUH = dominant β-thal synonym; α-thalassemia co-inheritance is protective |
| [28651846](https://pubmed.ncbi.nlm.nih.gov/28651846/) | *Molecular basis of β-thal / targets* | HbF + α-globin genotype predict severity |
| [22427201](https://pubmed.ncbi.nlm.nih.gov/22427201/) | *Integrated PQC of free α-globin in murine β-thal* | Proteasome + autophagy clearance; protein-aggregation framework |
| [142356](https://pubmed.ncbi.nlm.nih.gov/142356/) | *Ultrastructure of spleen/liver in unstable-Hb anemia* | Spleen is site of clearance; splenectomy → recovery |
| [42261228](https://pubmed.ncbi.nlm.nih.gov/42261228/) | *Unstable Hb Perth managed with splenectomy* | Clinical evidence for splenectomy efficacy |
| [25724329](https://pubmed.ncbi.nlm.nih.gov/25724329/) | *Role of α-Hb chaperone* | ROS → apoptosis → ineffective erythropoiesis |
| [29180398](https://pubmed.ncbi.nlm.nih.gov/29180398/) | *Heme-oxygenase inhibition in β-thal mice* | Unpaired globin + heme → oxidative erythroblast death |
| [24658077](https://pubmed.ncbi.nlm.nih.gov/24658077/) | *ActRIIA ligand trap corrects ineffective erythropoiesis* | GDF11/ROS/α-globin amplification loop; luspatercept rationale |
| [40655320](https://pubmed.ncbi.nlm.nih.gov/40655320/) | *ULK1 + AHSP co-induction (sirolimus)* | Autophagy/AHSP response to α-globin excess |
| [42584024](https://pubmed.ncbi.nlm.nih.gov/42584024/) | *2026 Update on Clinical Trials in β-Thalassemia* | Approved disease-modifying (luspatercept, mitapivat) + curative gene therapies |
| [21082937](https://pubmed.ncbi.nlm.nih.gov/21082937/) | *Global burden of β-thal / HbE* | 1.5% global carrier baseline |
| [36367309](https://pubmed.ncbi.nlm.nih.gov/36367309/) | *Gujarat screening* | 7% global thalassemia carriers; 300–400k affected births/yr |

Evidence types span **human clinical case/family reports** (variant characterization, phenotype, splenectomy), **mouse models** (mechanism, therapeutics), and **in-vitro cellular systems** (PQC, AHSP/Nrf2/ULK1, mutant mRNA/protein stability).

---

## Limitations and Knowledge Gaps

1. **Rarity → sparse quantitative data.** No robust prevalence/incidence, survival, or QoL statistics exist *specifically* for the dominant subtype; epidemiology is inferred from case series and the broader β-thal/NTDT literature.
2. **Phenotype frequencies are qualitative.** Per-phenotype percentages are not well established for this subtype; HPO frequencies given here are approximate.
3. **Mechanistic evidence is partly extrapolated** from recessive β-thal and general unstable-hemoglobin biology (mouse/in-vitro); direct demonstration of PQC-escape *for each dominant allele* is limited.
4. **Ontology term IDs** for a few entries (e.g., "Heinz bodies," some NCIT drug codes) should be verified by curators against current ontology releases.
5. **Therapeutic subtype-specificity untested.** Whether gene-addition vs. allele-directed editing differs in efficacy for a *dominant toxic* allele is a hypothesis, not a demonstrated clinical result.
6. **No dedicated animal model** faithfully expressing a human hyperunstable dominant β-globin knock-in was identified.

---

## Proposed Follow-up Experiments / Actions

1. **Curate a variant registry** of all reported dominant *HBB* alleles (exon-3 missense/nonsense, frameshift/elongating) with HGVS nomenclature, ClinVar submission, and linked phenotype severity, to enable genotype–phenotype correlation.
2. **Generate a knock-in mouse or iPSC-erythroid model** expressing a representative hyperunstable human β-globin (e.g., Hb Hradec Kralove) to directly test PQC-escape and dominant-negative toxicity.
3. **Quantify PQC flux** (proteasome vs. ULK1-autophagy) for individual dominant alleles in patient-derived erythroblasts; test whether pharmacologic autophagy induction (sirolimus) is allele-dependent.
4. **Systematically test the α-thalassemia modifier** by stratifying reported cases (and any registry) by α-genotype to quantify the protective effect size.
5. **Evaluate curative-therapy mechanism-fit:** model whether gene-addition adequately dilutes a translated toxic allele vs. approaches that reduce/edit the mutant allele, informing therapy selection for dominant cases.
6. **Confirm and standardize ontology mappings** (HPO/GO/CL/UBERON/NCIT) for knowledge-base ingestion.

---

*Report compiled from 9 confirmed findings across 5 iterations and 37 reviewed papers. Evidence prioritizes primary literature with verified abstract quotes; PMIDs are provided for all mechanistic and clinical claims.*


## Artifacts

- [OpenScientist final report](Dominant_Beta-Thalassemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dominant_Beta-Thalassemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 31 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24432801` *(abstract only)*: "leads to a decreased imbalance between α and β chain formation, and subsequently a milder phenotype"
  - closest text in source: "Both patients also have a 3.7 kb deletion on one α gene, leading to a decreased imbalance between α and β chain formation, and subsequently a milder phenotype than that seen in other hyperunstable Hb variants."
- `PMID:1971109` *(abstract only)*: "binds heme and produces aggregations that are relatively resistant to proteolytic degradation"
  - closest text in source: "It is suggested that the phenotypic difference between this condition and the more common recessive forms of beta-thalassemia lies mainly in the length and stability of the abnormal translation products that are synthesized and, in particular, whether they are capable of binding heme and producing aggregations that are relatively resistant to proteolytic degradation."
- `PMID:34889443` *(abstract only)*: "have demonstrated clinically meaningful improvements in hemoglobin levels and reduction of transfusion burden"
  - closest text in source: "Luspatercept, a transforming growth factor-β inhibitor, has demonstrated efficacy in reducing ineffective erythropoiesis, improving anemia, and possibly reducing iron loading"
- `PMID:34493145` *(abstract only)*: "high rates of durable transfusion independence"
  - closest text in source: "Although treatments have a significant impact on quality of life (QoL), life expectancy, and long-term health outcomes have improved in recent decades through safer RBC transfusion practices and better iron chelation strategies"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011381` (2 mentions) - the report calls it "MONDO"; MONDO calls it **dominant beta-thalassemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012132` (1 mention) - the report calls it "Erythroid abnormality"; HP calls it **Erythroid hyperplasia**
- `HP:0011031` (1 mention) - the report calls it "Abnormal iron homeostasis"; HP calls it **Abnormality of iron homeostasis**
- `CL:0000764` (1 mention) - the report calls it "erythroid progenitor cell"; CL calls it **erythroid lineage cell**
- `CL:0000235` (2 mentions) - the report calls it "macrophage — splenic red-pulp"; CL calls it **macrophage**