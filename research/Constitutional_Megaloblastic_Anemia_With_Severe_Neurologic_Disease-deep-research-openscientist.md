---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-16T20:45:06.829346'
end_time: '2026-09-16T21:11:37.260137'
duration_seconds: 1590.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Constitutional Megaloblastic Anemia With Severe Neurologic Disease
  mondo_id: MONDO:0013456
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
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 10
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 21
  labels_variant: 11
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
  path: Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Constitutional Megaloblastic Anemia With Severe Neurologic Disease
- **MONDO ID:** MONDO:0013456 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Constitutional Megaloblastic Anemia With Severe Neurologic Disease** covering all of the
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

# Constitutional Megaloblastic Anemia With Severe Neurologic Disease (DHFR Deficiency)

**Disease knowledge-base research report**
**MONDO:0013456 · OMIM #613839 · Orphanet ORPHA:319651 · Gene: DHFR**
Date: 2026-09-16

---

## Summary (Answer to the Research Question)

Constitutional Megaloblastic Anemia With Severe Neurologic Disease is an ultra-rare **autosomal recessive inborn error of folate metabolism caused by biallelic loss-of-function missense mutations in *DHFR*** (dihydrofolate reductase; chromosome 5q14.1). Profound DHFR enzyme deficiency prevents regeneration of tetrahydrofolate (THF) from dihydrofolate and the reduction of dietary folate, collapsing the reduced-folate pool. The result is a dual hematologic + neurologic disease: **megaloblastic anemia/pancytopenia** (impaired thymidylate and purine synthesis) plus **severe cerebral folate deficiency** (low CSF 5‑methyltetrahydrofolate) and **cerebral tetrahydrobiopterin (BH4) deficiency**, manifesting as developmental delay, seizures (notably atypical childhood absence epilepsy), and other neurologic abnormalities. The disease is **treatable with folinic acid (calcium leucovorin, a pre-reduced folate that bypasses the DHFR block)**, which corrects the anemia, normalizes CSF folate, and improves neurologic symptoms — while folic acid is ineffective because it still requires DHFR for activation.

The disease was defined by two simultaneous 2011 reports (Cario et al., PMID 21310277; Banka et al., PMID 21310276) in a total of 6 patients from 4 consanguineous/related families. Because reported cases are very few, much of the clinical detail below derives from these primary reports and a subsequent folate-disorder review (Watkins & Rosenblatt, PMID 22108709). *Evidence source types are flagged throughout: [HUMAN clinical], [in vitro], [structural/biochemical], [review].*

---

## 1. Disease Information

- **Overview:** A recessive inborn error of intracellular folate metabolism combining bone-marrow failure (megaloblastic anemia/pancytopenia) with a severe central-nervous-system phenotype driven by cerebral folate and BH4 deficiency. It is a **treatable metabolic encephalopathy** when recognized early. [HUMAN clinical; PMID 21310277, 21310276]
- **Key identifiers:**
  - **MONDO:** MONDO:0013456
  - **OMIM (phenotype):** #613839 "Megaloblastic anemia due to dihydrofolate reductase deficiency"
  - **OMIM (gene):** *126060 (DHFR)
  - **Orphanet:** ORPHA:319651 (Megaloblastic anemia due to dihydrofolate reductase deficiency)
  - **Gene / HGNC:** DHFR (HGNC:2861); NCBI Gene 1719; Ensembl ENSG00000228716; UniProt P00374
  - **ICD-10:** D53.1 (Other megaloblastic anemias, not elsewhere classified); **ICD-11:** 3A01.0 area / 5C50 (inborn errors of metabolism) — no unique code
  - **MeSH:** Folic Acid Deficiency (D005494); Anemia, Megaloblastic (D000749); Tetrahydrofolate Dehydrogenase (D013894)
- **Synonyms / alternative names:** DHFR deficiency; Dihydrofolate reductase deficiency; Megaloblastic anemia due to dihydrofolate reductase deficiency; Constitutional megaloblastic anemia with severe neurologic disease; Cerebral folate deficiency due to DHFR deficiency.
- **Information source type:** Aggregated disease-level (OMIM/Orphanet/MONDO) plus **individual-patient** case series (EHR-derived clinical descriptions of ~6 patients). Not derived from large population EHR datasets.

---

## 2. Etiology

- **Primary cause (genetic):** Biallelic (homozygous) germline **missense mutations in *DHFR*** producing a stable but catalytically deficient enzyme. Cario et al. identified **c.458A>T (p.Asp153Val)**; Banka et al. identified a homozygous *DHFR* missense mutation resulting in profound enzyme deficiency. [HUMAN clinical; PMID 21310277, 21310276]
  > "DHFR sequencing revealed a homozygous DHFR mutation, c.458A>T (p.Asp153Val), in all siblings." (PMID 21310277)
- **Genetic risk factors:** Homozygous DHFR pathogenic variants are causal (Mendelian, not susceptibility loci). **Consanguinity / relatedness** is a major risk factor — reported families were consanguineous or distantly related, consistent with a rare recessive founder-type allele.
- **Environmental risk factors:** None are causal. However, **low dietary folate intake would be expected to worsen the phenotype**, and **exposure to antifolate drugs** (methotrexate, trimethoprim, pyrimethamine) that further inhibit residual DHFR could exacerbate disease (mechanistic inference).
- **Protective factors:** **Dietary folate as reduced folates (folinic acid / 5-formyl-THF, 5-MTHF)** bypasses the block and is protective/therapeutic. Common population *DHFR* polymorphisms (e.g., the 19-bp intron-1 deletion, c.594+59del19; p.Leu80Phe) modulate folate handling/antifolate response in the general population but are **not** causes of this monogenic disease.
- **Gene–environment interactions:** Folate/antifolate status interacts strongly with residual DHFR activity — the phenotype is a genetic enzyme deficiency whose severity is modifiable by folate form and dose (folinic acid rescue is the clearest example). [HUMAN clinical; PMID 21310277, 21310276]

---

## 3. Phenotypes

Frequencies are qualitative given the very small case number (n≈6). Onset is typically **neonatal to infancy/early childhood**; course is **progressive if untreated, largely reversible/stabilizable with folinic acid**.

**Hematologic (laboratory abnormalities / clinical signs):**
- **Megaloblastic anemia** — core feature, most/all patients. HPO: **HP:0001889** (Megaloblastic anemia). Onset infancy; severe; treatment-responsive.
- **Pancytopenia** — reported in some patients. HP:0001876 (Pancytopenia); HP:0001873 (Thrombocytopenia), HP:0001882 (Leukopenia).
- **Macrocytosis / elevated MCV**, megaloblastic bone marrow, hypersegmented neutrophils. HP:0001972 (Macrocytic anemia).
  > "characterized by megaloblastic anemia and/or pancytopenia" (PMID 21310276)

**Neurologic (symptoms / signs):**
- **Seizures / epilepsy**, characteristically **atypical childhood absence epilepsy**. HP:0002121 (Absence seizure), HP:0001250 (Seizure). [HUMAN clinical; PMID 21310277]
  > "megaloblastic anemia and cerebral folate deficiency causing neurologic disease with atypical childhood absence epilepsy." (PMID 21310277)
- **Global developmental delay / intellectual disability.** HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability).
- **Microcephaly** (reported in cerebral folate deficiency states). HP:0000252.
- **Cerebral folate deficiency features** — variable neurologic findings including hypotonia, movement/motor abnormalities, and, mechanistically expected from BH4/monoamine deficiency, potential extrapyramidal or mood/behavioral changes. HP:0002376 (Developmental regression) variably.
- **Neuroimaging abnormalities** consistent with folate-deficient leukoencephalopathy in some patients. HP:0002352 (Leukoencephalopathy).

**Severity / progression / QoL:** Severe, potentially life-threatening in the neonatal/infantile period (anemia) with substantial neurodisability risk. **Quality-of-life impact is high if untreated** (epilepsy + developmental impairment); **early folinic acid markedly improves hematologic status and neurologic trajectory**, though pre-treatment CNS injury may persist. [HUMAN clinical; PMID 21310277, 21310276]

---

## 4. Genetic / Molecular Information

- **Causal gene:** **DHFR** (dihydrofolate reductase), 5q14.1; OMIM *126060; HGNC:2861; UniProt P00374 (187 aa cytosolic enzyme). EC 1.5.1.3.
- **Pathogenic variants (germline, autosomal recessive):**
  - **c.458A>T; p.Asp153Val (p.D153V)** — homozygous; 3 affected siblings (Cario et al.). Missense; classified pathogenic; drastically reduced enzyme activity and reduced methotrexate (FMTX) binding; **normal mRNA but reduced protein → destabilizing missense / loss of function.** [HUMAN clinical + in vitro; PMID 21310277]
    > "RT-PCR of DHFR mRNA revealed no differences between wild-type and DHFR mutation-carrying cells, whereas protein expression was reduced in cells with the DHFR mutation." (PMID 21310277)
  - **Homozygous DHFR missense mutation** in 3 individuals from 2 families (Banka et al.) → profound enzyme deficiency (reported as p.Leu80Phe in that cohort). [HUMAN clinical; PMID 21310276]
  - **Variant type/class:** missense (loss-of-function via reduced protein stability/activity). No nonsense/frameshift/structural variants reported as causal to date.
  - **ACMG/AMP:** Pathogenic (functional enzyme assays + segregation + rarity).
- **Allele frequency:** Causal alleles are private/ultra-rare (essentially absent in gnomAD as homozygotes). Note the **common benign** *DHFR* 19-bp intron-1 deletion and p.Leu80Phe polymorphism exist in general populations and affect folate/antifolate pharmacology but are not disease-causing here.
- **Somatic vs germline:** **Germline** only.
- **Functional consequence:** **Loss of function** (reduced catalytic activity + reduced protein). Heterozygotes show **intermediate** DHFR activity and FMTX binding but are clinically unaffected (recessive). [in vitro; PMID 21310277]
- **Modifier genes:** Not formally established; folate-pathway genes (MTHFR, folate transporters SLC46A1/FOLR1, MTHFD1) and dietary folate plausibly modify severity (inference).
- **Epigenetic / chromosomal abnormalities:** None implicated; no aneuploidy/translocation. Global one-carbon/methylation supply is indirectly reduced (methionine/SAM), a downstream metabolic — not primary epigenetic — effect.

---

## 5. Environmental Information

- **Environmental factors:** No environmental cause. **Antifolate drug exposure** (methotrexate, trimethoprim–sulfamethoxazole, pyrimethamine) is mechanistically contraindicated/aggravating because it further inhibits DHFR (inference).
- **Lifestyle / diet:** **Folate nutrition** is the dominant modifiable factor; adequacy of *reduced* folate (folinic acid) is protective. Ordinary folic acid supplementation does not rescue the defect. [HUMAN clinical; PMID 21310276]
- **Infectious agents:** Not applicable (not an infectious disease).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *DHFR* missense mutation** (e.g., p.Asp153Val) → **destabilized DHFR protein with severely reduced catalytic activity** ([in vitro] reduced enzyme activity + FMTX binding; normal mRNA, low protein). *Demonstrated.*
2. Reduced DHFR activity → **failure to reduce 7,8-dihydrofolate (DHF) to tetrahydrofolate (THF)** and failure to reduce dietary folic acid → **depletion of the reduced-folate (THF) pool**. *Demonstrated by patient folate profiling.*
3. THF depletion **branches** into three arms:
   - **3a. Hematologic arm:** low THF → impaired **thymidylate synthase cycle** (dUMP→dTMP) and de novo purine synthesis → **uracil misincorporation / imbalanced dNTPs → ineffective DNA synthesis in erythroid precursors** → nuclear–cytoplasmic asynchrony → **megaloblastic anemia and pancytopenia**. *Inferred from folate biochemistry; demonstrated hematologic phenotype.*
   - **3b. Cerebral folate arm:** impaired regeneration/transport of reduced folate → **low CSF 5‑methyltetrahydrofolate (cerebral folate deficiency)** → impaired CNS one-carbon metabolism, methylation, and neurotransmitter precursor supply → **seizures (atypical absence epilepsy), developmental delay**. *Demonstrated (low CSF folate).*
   - **3c. Neurotransmitter/BH4 arm:** DHFR also **regenerates tetrahydrobiopterin (BH4) from dihydrobiopterin (BH2)** (the salvage arm of BH4 metabolism). Loss → **cerebral BH4 deficiency** → reduced activity of tyrosine/tryptophan/phenylalanine hydroxylases → **reduced dopamine, serotonin, norepinephrine** → neurologic/neuropsychiatric manifestations. *Demonstrated (cerebral BH4 deficiency; PMID 21310276).*
4. Convergent CNS effects of 3b + 3c → **severe, potentially progressive encephalopathy**.
5. **Therapeutic branch (reversal):** administration of **folinic acid (5‑formyl‑THF)**, a folate already reduced beyond the DHFR block → restores THF pool → **corrects anemia, normalizes CSF folate, improves neurologic symptoms**. *Demonstrated.*

### Detail by category
- **Molecular pathways:** Folate one-carbon metabolism (KEGG hsa00670 one-carbon pool by folate; Reactome "Metabolism of folate and pterines"); pterine/BH4 salvage; methionine cycle (SAM methylation).
- **Cellular processes:** DNA replication in rapidly dividing cells (erythroblasts) → ineffective erythropoiesis/apoptosis of precursors; neuronal signaling via monoamines.
- **Protein dysfunction:** Destabilizing missense → **loss of function** with reduced protein abundance (not simply catalytic-site abolition); heterozygous intermediate activity. DHFR is a small (~21 kDa, 187 aa) NADPH-dependent oxidoreductase (Rossmann-like fold) whose catalysis involves hydride transfer from NADPH and protonation of the folate N5 — mechanistic basis for why point mutations near substrate/cofactor contacts abolish activity. [structural; PMID 25453083]. Human DHFR crystal structures (e.g., PDB via Cody et al., PMID 21931219, 26057816) define an active-site pocket with a conserved substrate-anchoring **Arg70**, and pteridine-binding residues **Phe31, Gln35, Val115** (Val115 vs Ile in microbial DHFR underlies antifolate selectivity). The disease missense residues (e.g., Asp153, Leu80) map to this compact fold; substitutions destabilize the protein and/or perturb cofactor/substrate binding, consistent with the observed loss of activity and reduced protein level. UniProt P00374; AlphaFold model AF-P00374.
- **Metabolic changes:** ↓THF, ↑DHF (relative), ↓5‑MTHF (esp. CSF), ↓BH4, impaired dTMP/purine synthesis, impaired homocysteine remethylation (variable). CHEBI: 7,8-dihydrofolate (CHEBI:20506), tetrahydrofolate (CHEBI:26907), 5‑methyltetrahydrofolate (CHEBI:15641), folinic acid (CHEBI:63606), tetrahydrobiopterin (CHEBI:15372).
- **Immune involvement:** Not a primary feature (contrast MTHFD1 deficiency, which adds SCID).
- **Tissue damage mechanisms:** Ineffective hematopoiesis (marrow); neuronal dysfunction from substrate/neurotransmitter insufficiency (largely functional, potentially structural leukoencephalopathy).
- **Biochemical abnormality:** Enzyme deficiency — dihydrofolate reductase (EC 1.5.1.3).
- **Suggested GO terms:** GO:0046452 (dihydrofolate metabolic process), GO:0006545 (glycine biosynthetic process), GO:0046655 (folic acid metabolic process), GO:0009394 (2'-deoxyribonucleotide metabolic process), GO:0006760 (folic acid-containing compound metabolic process), GO:0034355 (NAD salvage n/a) ; molecular function GO:0004146 (dihydrofolate reductase activity); GO:0006559 (l-phenylalanine catabolic process, via BH4).
- **Suggested CL terms:** erythroid progenitor cell (CL:0000038), megakaryocyte-erythroid progenitor, neuron (CL:0000540), dopaminergic neuron (CL:0000700), serotonergic neuron (CL:0000850).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Bone marrow / hematopoietic system** (UBERON:0002371 bone marrow) and **brain / central nervous system** (UBERON:0000955 brain).
- **Secondary/system involvement:** Peripheral blood (all lineages — anemia, leukopenia, thrombocytopenia); potentially cerebrospinal fluid compartment (UBERON:0001359 CSF) showing low 5-MTHF.
- **Body systems:** Hematologic/immune (blood) and nervous system; digestive absorption of folate is intact (the defect is intracellular reduction, distinguishing it from hereditary folate malabsorption).
- **Tissue/cell level:** Erythroid and other hematopoietic precursors (megaloblastic marrow); CNS neurons dependent on monoamine neurotransmitters. CL: erythroid progenitor (CL:0000038), neuron (CL:0000540).
- **Subcellular level:** **Cytosol** (DHFR is cytosolic; GO:0005829) with folate-dependent one-carbon reactions in cytosol and nucleus; downstream **nuclear** de novo thymidylate synthesis affected.
- **Localization / lateralization:** Systemic/bilateral; CNS involvement is diffuse/bilateral (e.g., diffuse white-matter changes), not focal.

---

## 8. Temporal Development

- **Onset:** Congenital enzyme defect; clinical presentation typically **neonatal to early infancy/childhood** (megaloblastic anemia early; seizures/absence epilepsy in early childhood). [HUMAN clinical; PMID 21310277]
- **Onset pattern:** Subacute/chronic, insidious neurologic decline with intercurrent anemia.
- **Progression:** **Progressive if untreated**; neurologic damage may accrue during the untreated window. With folinic acid, hematologic and biochemical parameters normalize and neurologic symptoms improve/stabilize. [HUMAN clinical; PMID 21310276]
- **Course pattern:** Chronic, lifelong (requires lifelong folinic acid). Seizures may be episodic.
- **Remission:** **Treatment-induced** biochemical/hematologic remission with folinic acid; not spontaneous.
- **Critical period:** **Early infancy/childhood is the critical intervention window** — earlier treatment better preserves neurodevelopment (rationale for newborn/early metabolic detection).

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare** — only a handful of patients (≈6 from 4 families) reported worldwide; prevalence <1/1,000,000 (Orphanet "unknown/ultra-rare"). Incidence not quantifiable.
- **Inheritance:** **Autosomal recessive.** Heterozygous carriers are asymptomatic with intermediate enzyme activity. [in vitro; PMID 21310277]
- **Penetrance:** Complete in biallelic individuals reported; **expressivity variable** (neurologic severity varies — "variable neurological findings," PMID 22108709).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects / consanguinity:** Reported families were **consanguineous or distantly related**; private homozygous alleles — consistent with founder/consanguinity mechanism.
- **Carrier frequency:** Unknown; expected very low given rarity.
- **Demographics:** No established ethnic predilection given tiny sample; both sexes affected (autosomal). No sex bias expected. Age distribution: pediatric onset.

---

## 10. Diagnostics

- **Laboratory tests:**
  - CBC + smear: **macrocytic/megaloblastic anemia**, possible pancytopenia, hypersegmented neutrophils. LOINC: MCV 30428-7, Hemoglobin 718-7.
  - Bone marrow: megaloblastic changes.
  - **Serum/RBC folate, vitamin B12, homocysteine** to position within folate disorders (B12 normal; distinguishes from B12 deficiency).
  - **CSF 5‑methyltetrahydrofolate (low)** — hallmark of cerebral folate deficiency. [HUMAN clinical; PMID 21310277]
  - **CSF neurotransmitter metabolites / biopterins** (low BH4, altered HVA/5-HIAA) reflecting BH4/monoamine deficiency. [HUMAN clinical; PMID 21310276]
  - LC-MS/MS folate profiling of RBC, plasma, CSF (as used diagnostically). [PMID 21310277]
- **Functional/enzyme assay:** **DHFR enzyme activity** and **fluorescein-methotrexate (FMTX) binding** in lymphoblastoid cells/fibroblasts — severely reduced in patients, intermediate in carriers. [in vitro; PMID 21310277]
- **Imaging:** Brain MRI — may show leukoencephalopathy/white-matter changes; used to characterize CNS involvement.
- **Electrophysiology:** EEG for absence/atypical absence epilepsy characterization.
- **Genetic testing:** **Definitive test = *DHFR* sequencing** (single-gene, or as part of a megaloblastic-anemia / inborn-errors-of-folate / epilepsy-metabolic gene panel; WES/WGS in undiagnosed cases). Homozygosity mapping was pivotal in gene discovery. [PMID 21310277]. GTR panels for "megaloblastic anemia" and "cerebral folate deficiency" include DHFR.
- **Clinical criteria / differential diagnosis:** Combination of megaloblastic anemia + low CSF folate + folinic-acid responsiveness + biallelic DHFR variants. **Differentiate from:** vitamin B12 deficiency; folate malabsorption (SLC46A1); FOLR1 cerebral folate deficiency (no anemia); MTHFR deficiency (homocystinuria, no megaloblastic anemia); **MTHFD1 deficiency (adds SCID/immunodeficiency; impaired nuclear dTMP synthesis with elevated uracil in DNA, PMID 25548164)**; thiamine-responsive megaloblastic anemia (SLC19A2); orotic aciduria.
- **Screening:** No routine newborn screen currently; consider **cascade/carrier testing** in affected families and prenatal/preimplantation testing where the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Untreated severe megaloblastic anemia/pancytopenia is potentially fatal in infancy; **prognosis is substantially improved with early folinic acid.** No formal survival statistics exist (too few cases).
- **Morbidity/function:** Neurodevelopmental disability and epilepsy are the main morbidities; degree depends on timing of treatment. Hematologic parameters are fully correctable.
- **Recovery potential:** **Hematologic and biochemical abnormalities are reversible with folinic acid; neurologic recovery is partial** — pre-treatment CNS injury may be irreversible, underscoring early diagnosis. [HUMAN clinical; PMID 21310276, 21310277]. The analogous FOLR1 cerebral folate deficiency literature reinforces a **critical treatment window**: folinic acid begun after >15 years of illness produced no meaningful clinical/neurophysiological improvement in three siblings (PMID 34008900), whereas timely initiation improved outcome (PMID 41132636).
- **Prognostic factors:** Age at diagnosis/treatment initiation, extent of pre-treatment neurologic damage, adherence to lifelong folinic acid, avoidance of antifolate drugs.

---

## 12. Treatment

- **First-line pharmacotherapy:** **Folinic acid (calcium leucovorin / 5‑formyltetrahydrofolate)** — a pre-reduced folate that bypasses the DHFR block; corrects anemia/pancytopenia, normalizes CSF folate, improves neurologic symptoms. Lifelong. **NCIT: Leucovorin Calcium (C1035) / Folinic Acid.** [HUMAN clinical; PMID 21310277, 21310276]
  > "Treatment with folinic acid resulted in the resolution of hematological abnormalities, normalization of CSF folate levels, and improvement of neurological symptoms." (PMID 21310277)
- **Ineffective/avoid:** **Folic acid** (requires DHFR to become active — does not rescue). Beyond needing DHFR, **unmetabolized folic acid actively inhibits 5-MTHF transport across the blood–CSF barrier**, worsening cerebral folate deficiency: in two CFD cases high-dose folic acid failed to normalize CSF 5-MTHF, and stopping folic acid normalized it — so folinic acid or 5-MTHF is preferred (PMID 36341171). Avoid **antifolate drugs** (methotrexate, trimethoprim, pyrimethamine).
  > "In the treatment of CFD, supplementation of folinic acid or 5MTHF (in cases of impaired 5MTHF synthesis) is preferred over the use of FA." (PMID 36341171)
- **Adjunctive:** Dose titration to normalize CSF 5-MTHF; consider that some cerebral folate deficiency benefits from higher folinic acid doses to cross the blood–brain barrier. Antiepileptic therapy for seizures as needed; monitor since folate status interacts with some AEDs.
- **Potential neurotransmitter support:** Because of **BH4/monoamine deficiency**, consideration of BH4 (sapropterin) or neurotransmitter precursor supplementation (e.g., L-dopa/carbidopa, 5-hydroxytryptophan) is biologically rational in select patients (inference; not established as standard for DHFR deficiency). Management principles for BH4/monoamine-deficiency disorders are summarized in an international consensus guideline (PMID 32456656).
- **Advanced/experimental therapeutics:** No gene, cell, or RNA therapy in clinical use; the disorder is largely managed by metabolite replacement. Gene replacement is conceptually feasible but unstudied.
- **Supportive care:** Transfusion for severe anemia acutely; developmental/rehabilitative therapies for neurodisability.
- **Treatment strategy / personalized medicine:** Genotype-confirmed diagnosis → lifelong folinic acid + monitoring of CBC, plasma and CSF folate; family cascade testing. NCIT terms: Leucovorin Calcium (C1035); Sapropterin Dihydrochloride (C61815) [experimental rationale].

---

## 13. Prevention

- **Primary prevention:** Not preventable in an affected homozygote (germline). **Genetic counseling** for at-risk families; **carrier/cascade testing**; **prenatal or preimplantation genetic testing** where the familial DHFR variant is known.
- **Secondary prevention (early detection):** High index of suspicion in infants with megaloblastic anemia + neurologic signs + low CSF folate → early DHFR testing and prompt folinic acid to prevent CNS damage. No population newborn screen exists yet, but the treatable nature makes early metabolic detection valuable.
- **Tertiary prevention:** Lifelong folinic acid, avoidance of antifolates, seizure control, developmental support to prevent complications and progression.
- **Counseling:** Autosomal recessive recurrence risk 25% per pregnancy for carrier couples; offer NSGC/ACMG-guided counseling.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** DHFR is universally conserved (essential enzyme) across bacteria, fungi, plants, and animals (NCBI Taxon relevance broad). Human host: *Homo sapiens* (NCBI:txid9606).
- **Orthologous genes:** Mouse *Dhfr* (NCBI Gene 13361); rat *Dhfr* (NCBI Gene 24312); zebrafish *dhfr*. High evolutionary conservation of catalytic function.
- **Natural disease in animals:** No well-characterized spontaneous DHFR-deficiency disease reported in companion animals/wildlife (OMIA — none established). DHFR is a classic antimicrobial/antineoplastic drug target across species.
- **Comparative biology:** Complete DHFR loss is embryonic-lethal in model organisms (essential gene), which is why human disease arises only from **hypomorphic missense** alleles retaining partial activity — a key comparative insight.
- **Transmission:** Not applicable (non-infectious, monogenic).

---

## 15. Model Organisms

- **Model status:** No published dedicated mouse/zebrafish model that recapitulates the *human hypomorphic DHFR-deficiency disease* was identified in this search; complete *Dhfr* knockouts are expected to be embryonic-lethal (essential enzyme), a key limitation.
- **Cellular/in vitro models (used in the defining studies):** **Patient-derived EBV-immortalized lymphoblastoid cell lines and fibroblasts** demonstrating reduced DHFR activity, reduced FMTX binding, and reduced protein — the primary functional models to date. [in vitro; PMID 21310277]
- **Model types feasible:** Knock-in of patient missense alleles (e.g., p.Asp153Val, p.Leu80Phe) in mouse/human iPSC or cell lines; conditional/hypomorphic alleles; iPSC-derived neurons/erythroid cultures to model the dual phenotype; humanized DHFR yeast/bacterial complementation assays for variant functional testing.
- **Applications:** Variant functional classification (enzyme activity, antifolate binding), folate-flux studies, testing folinic acid / BH4 rescue.
- **Resources:** MGI (Dhfr), Cellosaurus (patient lines), ClinVar (DHFR variants).

---

## Ontology Term Quick-Reference

- **Disease:** MONDO:0013456; OMIM #613839; ORPHA:319651
- **Gene/Protein:** DHFR (HGNC:2861; NCBI 1719; UniProt P00374); GO:0004146 (DHFR activity)
- **HPO:** HP:0001889 (megaloblastic anemia), HP:0001876 (pancytopenia), HP:0002121 (absence seizure), HP:0001250 (seizure), HP:0001263 (global developmental delay), HP:0001249 (intellectual disability), HP:0000252 (microcephaly), HP:0002352 (leukoencephalopathy)
- **GO (BP/CC):** GO:0046655 (folic acid metabolic process), GO:0046452 (dihydrofolate metabolic process), GO:0006760 (folic acid-containing compound metabolic process), GO:0005829 (cytosol)
- **CL:** CL:0000038 (erythroid progenitor), CL:0000540 (neuron), CL:0000700 (dopaminergic neuron)
- **UBERON:** UBERON:0002371 (bone marrow), UBERON:0000955 (brain), UBERON:0001359 (CSF)
- **CHEBI:** CHEBI:20506 (7,8-dihydrofolate), CHEBI:26907 (tetrahydrofolate), CHEBI:15641 (5-MTHF), CHEBI:63606 (folinic acid), CHEBI:15372 (tetrahydrobiopterin)
- **NCIT:** Leucovorin Calcium (C1035); Sapropterin (C61815)

---

## Supported vs. Refuted Hypotheses

**Supported:**
- H1 (Supported): Biallelic *DHFR* missense mutations cause the disease via profound enzyme loss of function. [PMID 21310277, 21310276]
- H2 (Supported): The mechanism is THF-pool depletion producing megaloblastic anemia + cerebral folate deficiency + cerebral BH4 deficiency. [PMID 21310276, 21310277]
- H3 (Supported): Folinic acid (not folic acid) is corrective because it bypasses the DHFR block. [PMID 21310277, 21310276]
- H4 (Supported): The disorder is distinguishable within inborn errors of folate metabolism; MTHFD1 deficiency adds immunodeficiency. [PMID 22108709, 25548164]

**Refuted / Not supported:**
- Environmental or infectious primary etiology — refuted (Mendelian recessive enzyme defect).
- Dominant inheritance — refuted (heterozygotes asymptomatic with intermediate activity).

---

## Limitations and Future Directions

- **Evidence base is very small** (~6 patients from 4 families); frequencies, prognosis, and genotype–phenotype correlations are qualitative. Numbers such as prevalence are order-of-magnitude estimates from Orphanet-class sources.
- The curated literature accessible here is limited; additional post-2012 case reports and any dedicated animal models were not retrievable in this environment and should be sought in OMIM/GeneReviews/HGMD/ClinVar and full PubMed.
- **Future directions:** systematic natural-history and treatment-timing studies; standardized CSF 5-MTHF/BH4/neurotransmitter panels; functional assays for variant classification; evaluation of BH4/neurotransmitter-precursor adjuncts; and consideration of DHFR in metabolic/epilepsy newborn or early-childhood screening given treatability.

---

### Primary References (PMID)
- **21310277** — Cario H, et al. *Dihydrofolate reductase deficiency due to a homozygous DHFR mutation causes megaloblastic anemia and cerebral folate deficiency leading to severe neurologic disease.* Am J Hum Genet, 2011. [HUMAN clinical + in vitro]
- **21310276** — Banka S, et al. *Identification and characterization of an inborn error of metabolism caused by dihydrofolate reductase deficiency.* Am J Hum Genet, 2011. [HUMAN clinical + in vitro]
- **22108709** — Watkins D, Rosenblatt DS. *Update and new concepts in vitamin responsive disorders of folate transport and metabolism.* J Inherit Metab Dis, 2012. [review]
- **25548164** — Field MS, et al. *Human mutations in MTHFD1 impair nuclear de novo thymidylate biosynthesis.* (differential) [HUMAN + in vitro]
- **25453083** — Wan Q, et al. *Toward resolving the catalytic mechanism of dihydrofolate reductase using neutron and ultrahigh-resolution X-ray crystallography.* [structural — DHFR enzymology]
- **36341171** — Akiyama T, et al. *Folic acid inhibits 5-methyltetrahydrofolate transport across the blood-cerebrospinal fluid barrier: Clinical biochemical data from two cases.* 2022. [HUMAN clinical — treatment rationale; provides pediatric CSF 5-MTHF reference values from 600 cases]
- **34008900** — Brunetti V, et al. *Cerebral folate transporter deficiency syndrome in three siblings...* 2021. [HUMAN clinical — FOLR1 differential; supports critical treatment window / irreversibility of delayed therapy]
- **41132636** — Ahmadabadi F, et al. *A Case of Cerebral Folate Deficiency due to FOLR1 Mutation in a 10-Year-Old Girl.* 2025. [HUMAN clinical — FOLR1 differential; timely folinic acid improves outcome]
- **32456656** — Opladen T, et al. *Consensus guideline for the diagnosis and treatment of tetrahydrobiopterin (BH4) deficiencies.* 2020. [guideline — BH4/monoamine management framework]
- **21931219 / 26057816** — Cody V, et al. *Structural analyses of human dihydrofolate reductase.* 2011/2015. [structural — hDHFR active-site residues Arg70, Phe31, Gln35, Val115]


## Artifacts

- [OpenScientist final report](Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 32 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 11 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `CHEBI:20506` (2 mentions) - the report calls it "7,8-dihydrofolate"; CHEBI calls it **5,6,7,8-tetrahydrofolic acid**, and lists "5,6,7,8-Tetrahydrofolate" among its other names
- `CHEBI:26907` (2 mentions) - the report calls it "tetrahydrofolate"; CHEBI calls it **tetrahydrofolic acid**, and lists "tetrahydrofolate" among its other names
- `CHEBI:15641` (2 mentions) - the report calls it "5-MTHF"; CHEBI calls it **5-methyltetrahydrofolic acid**, and lists "5-methyl-THF" among its other names
- `CHEBI:63606` (2 mentions) - the report calls it "folinic acid"; CHEBI calls it **(6S)-5-formyltetrahydrofolic acid**, and lists "L-Folinic acid" among its other names
- `CHEBI:15372` (2 mentions) - the report calls it "tetrahydrobiopterin"; CHEBI calls it **5,6,7,8-tetrahydrobiopterin**, and lists "Tetrahydrobiopterin" among its other names
- `GO:0034355` (1 mention) - the report calls it "NAD salvage n/a"; GO calls it **NAD+ biosynthetic process via the salvage pathway**, and lists "NAD salvage" among its other names
- `GO:0004146` (2 mentions) - the report calls it "dihydrofolate reductase activity", "DHFR activity"; GO calls it **dihydrofolate reductase activity**, and lists "dihydrofolic reductase activity" among its other names
- `GO:0006559` (1 mention) - the report calls it "l-phenylalanine catabolic process, via BH4"; GO calls it **L-phenylalanine catabolic process**
- `CL:0000038` (3 mentions) - the report calls it "Suggested CL terms:** erythroid progenitor cell", "erythroid progenitor"; CL calls it **erythroid progenitor cell**
- `UBERON:0001359` (2 mentions) - the report calls it "CSF"; UBERON calls it **cerebrospinal fluid**, and lists "CSF" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001876` - called "Pancytopenia", "pancytopenia"
- `HP:0002121` - called "Absence seizure", "absence seizure"
- `HP:0001250` - called "Seizure", "seizure"
- `HP:0001263` - called "Global developmental delay", "global developmental delay"
- `HP:0001249` - called "Intellectual disability", "intellectual disability"
- `HP:0002352` - called "Leukoencephalopathy", "leukoencephalopathy"
- `GO:0004146` - called "dihydrofolate reductase activity", "DHFR activity"
- `CL:0000038` - called "Suggested CL terms:** erythroid progenitor cell", "erythroid progenitor"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

34 of 36 terms resolved to a current term; the rest could not be looked up either way.