---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T02:21:47.220752'
end_time: '2026-10-25T02:36:36.911424'
duration_seconds: 889.69
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Optic Atrophy 15
  mondo_id: MONDO:0957935
  category: Mendelian
  causal_genes: MCAT
  omim_id: not recorded
  synonyms: OPA15; MCAT-related optic neuropathy; MCAT-related nuclear LHON-like optic
    neuropathy; autosomal recessive optic neuropathy, MCAT-related
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 3
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Optic_Atrophy_15-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Optic_Atrophy_15-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Optic Atrophy 15
- **MONDO ID:** MONDO:0957935 (if available)
- **Causal gene(s):** MCAT
- **OMIM:** not recorded
- **Synonyms:** OPA15; MCAT-related optic neuropathy; MCAT-related nuclear LHON-like optic neuropathy; autosomal recessive optic neuropathy, MCAT-related
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Optic Atrophy 15** covering all of the
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

# Optic Atrophy 15 (OPA15): A Comprehensive Disease Characteristics Report

**Disease:** Optic Atrophy 15 (OPA15)
**Causal gene:** **MCAT** (malonyl-CoA–acyl carrier protein transacylase, mitochondrial)
**MONDO ID:** MONDO:0957935 · **OMIM:** #620583 · **Orphanet:** ORPHA:98676 (autosomal recessive isolated optic atrophy)
**Synonyms:** OPA15; MCAT-related optic neuropathy; MCAT-related nuclear LHON-like optic neuropathy; autosomal recessive optic neuropathy, MCAT-related
**Category:** Mendelian (autosomal recessive)

---

## Summary

**Optic Atrophy 15 (OPA15) is an ultra-rare autosomal recessive mitochondrial optic neuropathy caused by biallelic loss-of-function variants in the nuclear gene *MCAT*** (malonyl-CoA–acyl carrier protein transacylase), the enzyme that performs the second (malonyl-transfer) step of **mitochondrial fatty-acid synthesis (mtFAS / type II FAS; EC 2.3.1.39)**. It is one of a small group of nuclear genes — alongside *DNAJC30*, *NDUFS2*, *NDUFA12*, and *MECR* — that cause an **autosomal recessive Leber-hereditary-optic-neuropathy-like (arLHON, OMIM 619382)** phenotype that clinically mimics classic mtDNA-driven LHON. The gene is named explicitly here because the serial disease name "Optic Atrophy 15" does not by itself indicate the causal gene; the subject of this report is strictly the **MCAT**-driven disorder defined by MONDO:0957935 / OMIM #620583, not the distinct gene-specific optic atrophies (e.g., OPA1, MECR/MEPAN).

Mechanistically, reduced MCAT enzyme lowers mtFAS flux, which starves two downstream branches: (1) **octanoyl-ACP → lipoic acid synthesis / protein lipoylation** of key mitochondrial enzymes (PDH, OGDH, BCKDH, glycine cleavage system), and (2) **long-chain acyl-ACP supply to the NFS1–ISD11(LYRM4)–ACP complex** required for **iron–sulfur (Fe-S) cluster biogenesis** and for assembly/stability of the **electron-transport-chain (ETC) complexes and supercomplexes**. The net result is **combined OXPHOS deficiency**. Because **retinal ganglion cells (RGCs)** — especially the small-caliber fibers of the papillomacular bundle — are exquisitely dependent on efficient oxidative phosphorylation, they selectively degenerate, producing optic nerve atrophy and vision loss. Functional-rescue data point to the **respiratory-chain assembly branch, not lipoylation, as the actionable driver** of the optic phenotype.

Clinically, OPA15 spans a spectrum: an **insidious childhood optic atrophy** (nystagmus, progressive bilateral vision loss, blindness within the first decade), an **adult acute/subacute LHON-like central vision loss**, and, in its most severe form, an **infantile multisystem mitochondrial disease** with hypotonia, failure to thrive, and abnormal brain MRI. Diagnosis is molecular (whole-exome/whole-genome sequencing or broad optic-atrophy nuclear gene panels after exclusion of primary mtDNA LHON and *OPA1*). There is **no approved disease-specific therapy**; management relies on empirical idebenone (by analogy to LHON), low-vision rehabilitation, avoidance of mitochondrial toxins, and genetic counseling. This report consolidates **9 confirmed findings** drawn from the three primary case reports (Li 2020, Gerber 2021, Webb 2023) and two mechanistic/review papers on arLHON and mtFAS.

---

## Key Findings

### Finding 1 — OPA15 is caused by biallelic *MCAT* variants that disrupt mitochondrial fatty-acid synthesis

OPA15 (OMIM #620583; MONDO:0957935) is an autosomal recessive optic neuropathy caused by homozygous or compound-heterozygous pathogenic variants in **MCAT** (malonyl-CoA–acyl carrier protein transacylase; OMIM 614479; HGNC:29622; NCBI Gene 27349; Ensembl ENSG00000100294; UniProt Q8IVS2; chromosome **22q13.2**). The condition was first described by **Li et al. 2020** (*Hum Mol Genet* 29:444–458) in two Chinese siblings from a consanguineous family who carried **double homozygous missense variants p.Leu81Arg (c.242T>G) and p.Arg212Trp (c.634C>T)**. HEK293 expression studies showed that these variants produce **structurally unstable MCAT with markedly reduced intracellular protein**, establishing a loss-of-function mechanism. **Gerber et al. 2021** (*Genes* 12:521) subsequently reported a compound-heterozygous genotype — **c.424-2A>G (a canonical splice-acceptor variant causing exon-2 skipping) plus c.824G>A (p.Glu275Lys)**. MCAT catalyzes the second step of **mitochondrial fatty-acid synthesis (mtFAS/FASII)**, transferring the malonyl moiety from malonyl-CoA onto the mitochondrial acyl-carrier protein (NDUFAB1).

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"biallelic mutations in the NDUFS2, DNAJC30, MCAT and NDUFA12 nuclear genes have been identified in unresolved LHON cases, identifying an autosomal recessive LHON (arLHON, OMIM:619382)."* This confirms MCAT as one of the nuclear genes causing autosomal recessive LHON-like optic neuropathy.

### Finding 2 — OPA15 presents along a spectrum from childhood insidious optic atrophy to adult acute LHON-like vision loss

Two principal presentations are documented, plus a severe syndromic form:

1. **Childhood insidious form** (Li 2020, [PMID: 31915829](https://pubmed.ncbi.nlm.nih.gov/31915829/)): two siblings with gradual vision loss, **nystagmus**, and optic atrophy diagnosed at age 8; examination showed **diffuse optic nerve pallor, attenuated disc capillaries, severely reduced retinal nerve fiber layer (RNFL) on OCT, and optic nerve thinning on brain MRI**, progressing to blindness within the first decade.
2. **Adult acute LHON-like form** (Gerber 2021, [PMID: 33918393](https://pubmed.ncbi.nlm.nih.gov/33918393/)): a woman with sudden **bilateral, asymmetric central vision loss at age 20**, headaches, **central scotoma**, abnormal visual evoked potentials, and optic nerve signal abnormality on MRI; at 10-year follow-up she had a persistent central scotoma with preserved peripheral vision, **photophobia, and blue-yellow dyschromatopsia** with generalized optic nerve fiber reduction.
3. **Severe multisystem form** (Webb 2023, [PMID: 36881526](https://pubmed.ncbi.nlm.nih.gov/36881526/)): expanded the phenotype to include **hypotonia, failure to thrive, nystagmus, and abnormal brain MRI**, with reduced complex I/II/IV subunits and decreased ETC activity.

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"The clinical presentation of arLHON copies that of typical LHON due to mtDNA mutations (mtLHON), with an acute phase of sudden and severe vision loss, telangiectatic and tortuous vessels around the optic nerve and swelling of the retinal nerve fibre layer."*

**Suggested HPO terms:** HP:0000648 Optic atrophy; HP:0000543 Optic disc pallor; HP:0000639 Nystagmus; HP:0030532 Central scotoma; HP:0000551 Abnormality of color vision; HP:0000496 Abnormal eye movement; HP:0001290 Hypotonia (syndromic); HP:0001508 Failure to thrive (syndromic); HP:0000007 Autosomal recessive inheritance.

### Finding 3 — Mechanism: MCAT deficiency impairs mtFAS-dependent lipoylation and Fe-S/ETC supercomplex assembly in retinal ganglion cells

The causal chain runs: biallelic *MCAT* LoF variants → unstable, reduced MCAT protein (Li 2020) → reduced malonyl transfer from malonyl-CoA to mitochondrial ACP → **decreased mtFAS flux** (GO:0006633 fatty-acid biosynthesis; EC 2.3.1.39). Lower acyl-ACP then starves two branches: (a) reduced octanoyl-ACP → **impaired lipoic-acid synthesis and protein lipoylation** of PDH, OGDH, BCKDH, and the glycine cleavage system; and (b) reduced long-chain acyl-ACP binding to the LYRM/ISD11 (LYRM4) factor → **impaired Fe-S cluster biogenesis** (NFS1–ISD11–ACP complex) and defective **ETC complex/supercomplex assembly**. **Webb 2023** demonstrated combined OXPHOS deficiency with reduced NDUFB8 (CI), COXII (CIV), and SDHB (CII) and decreased ETC enzyme activities in patient fibroblasts and lymphoblasts. Mitochondria-rich RGCs, which depend on efficient OXPHOS, degenerate, producing optic nerve atrophy and vision loss. **Mouse evidence:** RGC-specific *Mcat* knockdown attenuated the retinal nerve fiber layer, phenocopying the human optic neuropathy (Li 2020). Importantly, some MCAT patients lacked systemic lipoylation defects or lactic acidosis, implicating the **Fe-S/supercomplex branch rather than lipoate deficiency** as the RGC driver.

> Supporting quote — [PMID: 37734847](https://pubmed.ncbi.nlm.nih.gov/37734847/): *"reinforcing the impairment of mtFAS as novel pathogenic mechanism in LHON."*

**Suggested terms:** GO:0006633 (fatty-acid biosynthesis), GO:0009249 (protein lipoylation), GO:0016226 (iron-sulfur cluster assembly), GO:0010257 (NADH dehydrogenase complex assembly); CL:0000740 retinal ganglion cell; UBERON:0000941 optic nerve; GO:0005759 mitochondrial matrix.

### Finding 4 — Epidemiology: ultra-rare, consanguinity-associated; the LHON-like subset shows male predominance and incomplete penetrance

OPA15 is ultra-rare, with only a handful of families reported worldwide: two Chinese consanguineous siblings (Li 2020), one French woman plus separate cases (Gerber 2021), and one proband with multisystem disease (Webb 2023). **No prevalence or incidence estimates exist.** Orphanet classifies MCAT under autosomal recessive isolated optic atrophy (ORPHA:98676). Inheritance is **autosomal recessive (HP:0000007)**; consanguinity contributed to the index family (homozygous L81R + R212W). As a recessive disease gene, *MCAT* is expected to have a low pLI (not haploinsufficient). As part of the broader arLHON group (DNAJC30, NDUFS2, NDUFA12, MCAT, MECR), the LHON-like presentations share classic LHON features — **strong male predominance (~8.5:1 male:female across arLHON) and incomplete, sex-biased penetrance** — although MCAT-specific sex and penetrance figures are not established given the few cases. **No founder variant** is described for MCAT, unlike *DNAJC30* p.Tyr51Cys in Eastern Europeans.

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"As for mtLHON, arLHON predominantly affected male compared with female carriers."*

### Finding 5 — Treatment and prognosis: no approved therapy; empirical idebenone; supportive care

No disease-specific or approved therapy exists for OPA15. Management is extrapolated from LHON/arLHON. **Idebenone** (a short-chain benzoquinone antioxidant; approved as Raxone in the EU for LHON) bypasses complex I to restore ATP synthesis in RGCs. In the arLHON cohort, **DNAJC30 patients showed high idebenone-responsive visual recovery (up to ~81%)**, whereas the reported MCAT patient did not recover with corticosteroid boluses; **MCAT-specific idebenone efficacy is not established**. AAV gene-replacement therapies in clinical use (**lenadogene nolparvovec, rAAV2/2-ND4; REFLECT trial**) target the mitochondrial *MT-ND4* m.11778G>A form and are **NOT applicable** to nuclear MCAT disease. Prognosis: the childhood-onset form (Li 2020) is severe and progressive, reaching blindness within the first decade; the adult LHON-like form (Gerber 2021) shows subacute severe central vision loss with persistent central scotoma. A key mechanistic insight for therapy comes from **Webb 2023**: the T271I MCAT variant **rescued protein lipoylation but not respiration** in MCAT-deficient C2C12 cells, indicating that the **OXPHOS/respiration branch, not lipoylation, is the actionable disease driver**.

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"Idebenone treatment significantly improved vision recovery in DNAJC30-associated patients."*

**Suggested NCIT term:** idebenone (therapeutic antioxidant / neuroprotective agent).

### Finding 6 — Molecular identifiers, protein function, and model organisms

**Gene/protein:** MCAT (malonyl-CoA–ACP transacylase, mitochondrial); HGNC:29622; NCBI Gene 27349; Ensembl ENSG00000100294; UniProt Q8IVS2; EC 2.3.1.39; chr22q13.2. It catalyzes malonyl transfer from malonyl-CoA to mitochondrial ACP (NDUFAB1) — step 2 of mtFAS (type II FAS). **Subcellular localization:** mitochondrial matrix (GO:0005759). **CHEBI entities:** malonyl-CoA (CHEBI:15531), acyl carrier protein, octanoate/lipoic acid (CHEBI:30314). **Pathogenic variants (all germline, recessive):** missense p.Leu81Arg (c.242T>G) and p.Arg212Trp (c.634C>T) (Li 2020); splice c.424-2A>G + missense p.Glu275Lys (c.824G>A) (Gerber 2021); missense p.Thr271Ile plus a second allele (Webb 2023). The functional consequence is **loss of function via protein destabilization / reduced expression**, confirmed in HEK293 and C2C12 systems.

**Model organisms:** (1) Mouse *Mcat* (NCBI Gene 223722; MGI:2388651; UniProt Q8R3F5) — RGC-specific knockdown attenuated the RNFL, recapitulating optic neuropathy (Li 2020, in vivo). (2) Cellular models — MCAT-deficient mouse C2C12 myoblasts rescued with WT vs mutant human MCAT to assay lipoylation and respiration (Webb 2023, in vitro), and HEK293 overexpression stability assays (Li 2020). (3) Broader mtFAS loss-of-function models (*Mcat*/*Mecr*) in mouse myoblasts show severe loss of ETC complexes. mtFAS/FASII is highly conserved from bacteria to humans, enabling yeast complementation studies.

> Supporting quote — [PMID: 37734847](https://pubmed.ncbi.nlm.nih.gov/37734847/): *"We modelled the candidate variant in yeast and studied mitochondrial dysfunction in yeast and fibroblasts."* This illustrates the yeast/fibroblast modeling approach used for mtFAS genes (here MECR, paralleling MCAT).

### Finding 7 — Diagnostics: molecular diagnosis by WES/WGS or optic-atrophy gene panels after exclusion of mimics

OPA15 has **no specific biochemical biomarker**; diagnosis is molecular. The recommended workup for inherited optic neuropathy includes: history, best-corrected visual acuity, color-vision testing (dyschromatopsia, often blue-yellow in MCAT), fundus exam (optic disc pallor, attenuated disc capillaries), automated perimetry (central/cecocentral scotoma), **OCT** (peripapillary RNFL and macular ganglion-cell-layer thinning, global and temporal-predominant), and **electrophysiology** (abnormal VEP; reduced PERG N95 reflecting RGC dysfunction). **Brain/orbit MRI** shows optic nerve thinning/signal change and helps exclude compressive, demyelinating, toxic, nutritional, and metabolic mimics. **Genetic strategy:** first exclude primary mtDNA LHON variants (m.11778G>A, m.14484T>C, m.3460G>A) and *OPA1*, then perform whole-exome/whole-genome sequencing or a broad optic-atrophy nuclear gene panel (MCAT is included among ~50 nuclear HON genes). Diagnostic yield of exome sequencing for nuclear hereditary optic neuropathy is ~31.5% (149/473) in a large 2024/2025 cohort ([PMID: 39423307](https://pubmed.ncbi.nlm.nih.gov/39423307/)); MCAT is a very rare cause — the "LHON-like optic atrophy" fundus category accounted for only ~3.64% of nuclear HON. Variant interpretation follows ACMG/AMP; reported MCAT alleles (missense and canonical splice) are classified pathogenic/likely pathogenic.

**Differential diagnosis:** mitochondrial LHON (MT-ND1/4/6), dominant optic atrophy (OPA1), WFS1/Wolfram, FDXR, ACO2, AFG3L2, NR2F1 (BBSOAS), MECR/MEPAN, toxic/nutritional optic neuropathy, optic neuritis, and compressive lesions.

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"NDUFS2, DNAJC30, MCAT and NDUFA12 should be investigated in these individuals, knowing that other arLHON genes might exist."*

### Finding 8 — Anatomical and temporal profile: bilateral RGC–optic nerve degeneration; childhood-to-young-adult onset, chronic progressive

**Primary affected structures:** retina and optic nerve of the central visual system. **Cell type:** retinal ganglion cells (CL:0000740), with preferential loss of the **papillomacular bundle** (small-caliber fibers), as in other mitochondrial optic neuropathies. **Tissue:** retinal nerve fiber layer (UBERON:0001789 retina; UBERON:0000941 optic nerve; UBERON:0004327 retinal nerve fiber layer). **Subcellular compartment:** mitochondrion/mitochondrial matrix (GO:0005759). **Secondary/syndromic involvement** in the severe multisystem presentation (Webb 2023): CNS (abnormal brain MRI), skeletal muscle (hypotonia), and growth (failure to thrive), reflecting systemic combined OXPHOS deficiency. **Lateralization:** bilateral, may be asymmetric (Gerber 2021 patient worse in the left eye). **Temporal profile:** onset ranges from early childhood (Li 2020, diagnosed age 8, insidious/chronic progressive to blindness in the first decade) to young adulthood (Gerber 2021, acute/subacute at age 20, LHON-like); the multisystem form presents in infancy. The course is chronic and progressive with variable, usually poor, visual recovery; the LHON-like form shows an acute phase followed by a chronic atrophic phase. No remission/relapsing pattern is established.

> Supporting quote — [PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/): *"This is followed by a chronic phase of retinal nerve fibre layer loss, but eventually affected individuals recover partial or full visual acuity"* — describing the acute-then-chronic course of the LHON-like presentation.

### Finding 9 — Etiology is purely genetic; prevention rests on toxin avoidance and genetic counseling

OPA15 is a **monogenic (Mendelian, autosomal recessive)** disorder caused solely by biallelic MCAT loss-of-function variants; there is no infectious, autoimmune, or primary environmental cause. **No susceptibility loci, GWAS associations, modifier genes, or epigenetic mechanisms** have been reported for MCAT disease (data not available). No environmental or lifestyle factors are proven. By analogy to LHON — where tobacco smoking and heavy alcohol are recognized precipitants/aggravators of RGC bioenergetic failure — avoidance of mitochondrial toxins and of drugs impairing oxidative phosphorylation is prudent, though unproven for MCAT (inferred, not demonstrated). The variable penetrance/expressivity of the broader arLHON group suggests gene–environment or gene–sex interactions as in LHON, but this is not established for MCAT specifically. **Prevention:** no primary prevention or vaccine applies; secondary/tertiary prevention equals early molecular diagnosis, ophthalmologic monitoring (OCT, perimetry), low-vision rehabilitation, and empirical neuroprotection (idebenone) in LHON-like cases. **Genetic counseling:** autosomal recessive 25% sibling recurrence risk; carrier testing of relatives/partners, cascade testing, and prenatal diagnosis or preimplantation genetic testing are appropriate for families with known biallelic MCAT variants — particularly relevant in consanguineous unions. No newborn or population carrier screening programs exist for this ultra-rare gene.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *MCAT* loss-of-function variants** (missense destabilizing, or canonical splice) → **reduced, structurally unstable MCAT protein** (demonstrated in HEK293 and C2C12 — Li 2020, Webb 2023).
2. Reduced MCAT **leads to** decreased malonyl transfer from malonyl-CoA to mitochondrial ACP (NDUFAB1) → **decreased mitochondrial fatty-acid synthesis (mtFAS) flux** (EC 2.3.1.39).
3. Lower acyl-ACP pools **result in** a branch point:
   - **Branch A (lipoylation):** reduced octanoyl-ACP → impaired lipoic-acid synthesis → **reduced protein lipoylation** of PDH, OGDH, BCKDH, glycine cleavage system. *(Present biochemically but apparently NOT the primary optic driver — some patients lack systemic lipoylation/lactic-acidosis signs; T271I rescued lipoylation yet not respiration.)*
   - **Branch B (Fe-S / ETC assembly):** reduced long-chain acyl-ACP binding to LYRM4(ISD11) → **impaired Fe-S cluster biogenesis** (NFS1–ISD11–ACP) → **defective assembly/stability of ETC complexes and supercomplexes**. *(Inferred to be the actionable driver.)*
4. Branch B **leads to** **combined OXPHOS deficiency** — reduced CI (NDUFB8), CII (SDHB), CIV (COXII) subunits and lowered ETC enzyme activities (demonstrated in patient fibroblasts/lymphoblasts — Webb 2023).
5. OXPHOS deficiency **results in** bioenergetic failure selectively in **mitochondria-rich retinal ganglion cells**, preferentially the small-caliber papillomacular bundle fibers.
6. RGC degeneration **leads to** **retinal nerve fiber layer thinning and optic nerve atrophy** (demonstrated on OCT/MRI; phenocopied by RGC-specific *Mcat* knockdown in mouse — Li 2020).
7. This **results in** the clinical manifestation: **bilateral progressive or acute central vision loss, optic disc pallor, dyschromatopsia, central scotoma** — and, in severe infantile cases, systemic multisystem mitochondrial disease.

```
 MCAT biallelic LoF
        │ (reduced/unstable protein)
        ▼
 ↓ malonyl transfer → ↓ mtFAS flux (acyl-ACP)
        │
        ├────────────── Branch A ──────────────┐
        │  ↓ octanoyl-ACP → ↓ lipoic acid      │  (lipoylation defect —
        │  → ↓ protein lipoylation (PDH/OGDH)  │   NOT primary optic driver)
        │                                       │
        └────────────── Branch B ──────────────┘
           ↓ long-chain acyl-ACP → LYRM4/ISD11
           → ↓ Fe-S cluster biogenesis
           → ↓ ETC complex/supercomplex assembly   ◄── ACTIONABLE DRIVER
                        │
                        ▼
              Combined OXPHOS deficiency
                        │
                        ▼
        RGC bioenergetic failure (papillomacular bundle)
                        │
                        ▼
        RNFL thinning / optic nerve atrophy  →  vision loss
```

### Comparison of reported genotypes and phenotypes

| Study | PMID | Genotype (MCAT) | Variant type | Phenotype | Onset |
|---|---|---|---|---|---|
| Li et al. 2020 | [31915829](https://pubmed.ncbi.nlm.nih.gov/31915829/) | p.Leu81Arg (c.242T>G) + p.Arg212Trp (c.634C>T), homozygous (consanguineous) | Missense (destabilizing) | Insidious optic atrophy, nystagmus, blindness in 1st decade | Childhood (~age 8) |
| Gerber et al. 2021 | [33918393](https://pubmed.ncbi.nlm.nih.gov/33918393/) | c.424-2A>G (splice) + p.Glu275Lys (c.824G>A) | Splice + missense | Acute/subacute LHON-like central vision loss, scotoma, dyschromatopsia | Young adult (age 20) |
| Webb et al. 2023 | [36881526](https://pubmed.ncbi.nlm.nih.gov/36881526/) | p.Thr271Ile + second allele | Missense | Multisystem: hypotonia, failure to thrive, nystagmus, abnormal MRI; combined OXPHOS deficiency | Infancy |

### MCAT within the arLHON gene group

| Gene | Pathway role | Idebenone response | Notes |
|---|---|---|---|
| **MCAT** | mtFAS step 2 (malonyl transfer) | Not established (one patient no recovery) | OXPHOS-assembly branch is driver |
| MECR | mtFAS (enoyl reductase) | Not established | Paralogous mtFAS mechanism |
| DNAJC30 | Complex V assembly/turnover | High (~81% recovery) | Founder p.Tyr51Cys in Eastern Europe |
| NDUFS2 | Complex I subunit | Variable | Core CI gene |
| NDUFA12 | Complex I assembly | Variable | CI accessory factor |

---

## Evidence Base

| PMID | Title / focus | Role in this report |
|---|---|---|
| [31915829](https://pubmed.ncbi.nlm.nih.gov/31915829/) | Li et al. 2020, *Hum Mol Genet* — first OPA15/MCAT description | Primary source: index consanguineous family, variants, protein-stability assay, mouse RGC knockdown |
| [33918393](https://pubmed.ncbi.nlm.nih.gov/33918393/) | Gerber et al. 2021, *Genes* — adult LHON-like MCAT case | Primary source: compound-het splice+missense genotype, acute phenotype, 10-year follow-up |
| [36881526](https://pubmed.ncbi.nlm.nih.gov/36881526/) | Webb et al. 2023 — combined OXPHOS deficiency / MCAT | Primary source: multisystem phenotype, combined OXPHOS deficiency, C2C12 rescue (lipoylation vs respiration) |
| [37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/) | *Autosomal recessive LHON, a new neuro-ophthalmo-genetic paradigm* | Framework for arLHON: MCAT as an arLHON gene, clinical course, male predominance, idebenone, diagnostic approach |
| [37734847](https://pubmed.ncbi.nlm.nih.gov/37734847/) | Recessive mtFAS (MECR) optic neuropathy | Supports mtFAS impairment as a shared pathogenic mechanism; yeast/fibroblast modeling approach |
| [39423307](https://pubmed.ncbi.nlm.nih.gov/39423307/) | Nuclear HON exome cohort (Brain 2024/2025) | Diagnostic yield context (~31.5%); MCAT rarity within nuclear HON |

**How the evidence converges:** The three primary case reports independently establish *MCAT* causality across distinct genotypes and ancestries, supporting genuine disease causation rather than chance association. The arLHON review ([PMID: 37071596](https://pubmed.ncbi.nlm.nih.gov/37071596/)) situates MCAT within a coherent clinical and therapeutic framework, and the MECR mtFAS paper ([PMID: 37734847](https://pubmed.ncbi.nlm.nih.gov/37734847/)) provides convergent mechanistic validation that disrupting mtFAS causes LHON-like optic neuropathy. The Webb 2023 C2C12 rescue experiment is the pivotal mechanistic result distinguishing the two downstream branches, redirecting therapeutic attention from lipoylation toward respiratory-chain assembly.

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** Fewer than ~5 families/probands are reported worldwide. All clinical, penetrance, and prognostic statements rest on single-digit case numbers, so frequencies, severity distributions, and natural history are provisional.
- **No epidemiology:** Prevalence, incidence, carrier frequency, and sex ratio specific to MCAT are unknown; male-predominance and penetrance figures are borrowed from the broader arLHON group.
- **MCAT-specific therapy data absent:** Idebenone efficacy in MCAT disease is unproven; the one reported attempt (corticosteroids) failed. No clinical trials target nuclear mtFAS optic neuropathy.
- **Mechanistic branch resolution:** While functional data favor the Fe-S/ETC-assembly branch as the driver, the precise contribution of lipoylation loss to the systemic/syndromic phenotype versus the isolated optic phenotype is not fully resolved.
- **Genotype–phenotype correlation:** It remains unclear why some alleles yield isolated childhood optic atrophy, others adult LHON-like disease, and others infantile multisystem disease. Residual enzyme activity and modifier effects are plausible but untested.
- **No modifier genes, epigenetics, or environmental triggers** have been formally studied; all such statements are inferred from LHON analogy.
- **No animal model fully recapitulates the human disease;** available data are RGC-specific knockdown (mouse) and myoblast rescue (C2C12) rather than a constitutive or knock-in disease model.

---

## Proposed Follow-up Experiments / Actions

1. **Build a knock-in mouse** carrying a human pathogenic allele (e.g., p.Leu81Arg or a splice equivalent) to establish a constitutive, physiologically faithful OPA15 model and track RGC loss, OCT RNFL, and OXPHOS assembly over time.
2. **Patient-derived iPSC-RGCs / retinal organoids** from MCAT patients to quantify supercomplex assembly, Fe-S enzyme activity, and respiration, and to screen candidate neuroprotectants.
3. **Targeted rescue experiments** distinguishing the branches: selectively restore lipoylation (lipoate supplementation) vs respiratory assembly (e.g., AAV-MCAT, or supercomplex-stabilizing interventions) in patient cells to confirm which branch rescues the RGC phenotype.
4. **AAV-MCAT gene replacement** proof-of-concept in the mouse model — a rational nuclear-gene analogue to lenadogene nolparvovec, since mtDNA-targeted AAV therapies do not apply.
5. **International registry / GeneMatcher recruitment** to aggregate additional MCAT cases, enabling genotype–phenotype correlation, penetrance estimation, and natural-history definition.
6. **Formal idebenone (and alternative electron carriers) evaluation** in MCAT cases, given the ambiguous LHON-group evidence and the OXPHOS-centric mechanism.
7. **Deep-phenotyping and gnomAD interrogation** of MCAT variant frequencies to estimate carrier frequency and to refine ACMG classification of novel alleles.

---

*Evidence source types distinguished throughout: human clinical (Li 2020, Gerber 2021, Webb 2023; exome cohort PMID 39423307), review/synthesis (PMID 37071596), model organism / in vitro (mouse RGC knockdown, C2C12 and HEK293 assays, yeast complementation for the paralogous mtFAS gene MECR, PMID 37734847).*


## Artifacts

- [OpenScientist final report](Optic_Atrophy_15-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Optic_Atrophy_15-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 4 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006633` (2 mentions) - the report calls it "fatty-acid biosynthesis"; GO calls it **fatty acid biosynthetic process**, and lists "fatty acid biosynthesis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `MGI`.

21 of 25 terms resolved to a current term; the rest could not be looked up either way.