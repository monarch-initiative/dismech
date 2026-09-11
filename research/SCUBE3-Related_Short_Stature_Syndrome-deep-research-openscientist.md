---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T07:08:01.570983'
end_time: '2026-09-05T07:28:23.243503'
duration_seconds: 1221.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SCUBE3-Related Short Stature Syndrome
  mondo_id: MONDO:0030953
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
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 56
  verified: 49
  not_found: 1
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.02
  labels_checked: 28
  labels_matching: 23
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030953
    reported_labels:
    - MONDO
    ontology_label: short stature, facial dysmorphism, and skeletal anomalies with
      or without cardiac anomalies 2
  - term_id: DOID:0112358
    reported_labels:
    - DOID
    ontology_label: short stature, facial dysmorphism, and skeletal anomalies with
      or without cardiac anomalies 2
  labels_variant: 3
  unresolved_terms:
  - UBERON:0002332
  unresolvable_prefixes:
  - NCBIGene
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCUBE3-Related_Short_Stature_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCUBE3-Related_Short_Stature_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCUBE3-Related Short Stature Syndrome
- **MONDO ID:** MONDO:0030953 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SCUBE3-Related Short Stature Syndrome** covering all of the
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

# SCUBE3-Related Short Stature Syndrome (SSFSC2): Comprehensive Disease Characterization

**Disease:** SCUBE3-Related Short Stature Syndrome
**Formal name:** Short stature, facial dysmorphism, and skeletal anomalies with or without cardiac anomalies 2 (SSFSC2)
**MONDO:** MONDO:0030953 · **OMIM:** 619184 · **Category:** Mendelian (autosomal recessive)
**Date compiled:** 2026-09-05

---

## Summary

SCUBE3-Related Short Stature Syndrome (SSFSC2) is an **ultra-rare, autosomal-recessive Mendelian disorder** caused by **biallelic loss-of-function variants in *SCUBE3*** (Signal peptide-CUB-EGF domain-containing protein 3; HGNC:23310, NCBIGene:222663, chromosome 6p21.31, UniProt Q8IX30). The disorder was first defined as a discrete clinical entity by Lin and colleagues in 2021, who described 18 affected individuals from 9 unrelated families sharing a consistent phenotype of reduced growth, skeletal features, a distinctive craniofacial appearance, and dental anomalies ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)). As of 2025, approximately 20 patients from around 10 families have been reported worldwide ([PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)).

Mechanistically, SCUBE3 is a secreted/cell-surface-anchored glycoprotein that functions as a **co-receptor for bone morphogenetic proteins BMP2/BMP4**, recruiting BMP receptor complexes into lipid-raft microdomains and augmenting BMP–BMP type I receptor interactions. It also modulates TGF-β (via SMAD2/3), FGF, and Hedgehog signaling. Biallelic loss-of-function impairs transcript processing, protein secretion, and co-receptor function, dysregulating BMP signaling. Because BMP-mediated chondrogenesis and osteogenesis are essential for endochondral bone formation at the growth plate, SCUBE3 deficiency produces prenatal-onset short stature and skeletal/craniofacial/dental abnormalities. The *Scube3⁻/⁻* knockout mouse faithfully recapitulates the human disorder, exhibiting craniofacial and dental defects, reduced body size, and defective endochondral bone growth due to impaired BMP-mediated chondrogenesis and osteogenesis ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)).

Clinically, the syndrome is **non-lethal with generally normal cognition and normal life expectancy**. Diagnosis is molecular—recognition of the clinical gestalt followed by exome/genome sequencing or a short-stature/skeletal-dysplasia gene panel. There is **no disease-modifying therapy**; management is supportive and multidisciplinary (orthopedic/spinal, dental/orthodontic, cardiac surveillance, growth monitoring). The GH/IGF-1 axis is typically normal, so the growth failure reflects a local growth-plate BMP-signaling defect rather than classic growth-hormone deficiency.

---

## Section 1 — Disease Information

**Overview.** SSFSC2 is a syndromic short-stature disorder of prenatal onset combining growth retardation, a recognizable craniofacial gestalt (long/triangular face, high forehead, long nose, small pointed chin), skeletal anomalies (brachydactyly, short long bones, scoliosis, 11 rib pairs), and dental anomalies (crowding, enamel defects), typically with preserved cognition ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030953 |
| OMIM | 619184 |
| DOID | DOID:0112358 |
| UMLS | C5543057 |
| MedGen | 1782253 |
| Causal gene | *SCUBE3* — HGNC:23310, NCBIGene:222663, Ensembl ENSG00000146197, UniProt Q8IX30 |
| Locus | 6p21.31 |
| Inheritance | Autosomal recessive (HP:0000007) |

**Synonyms / alternative names:** Short stature, facial dysmorphism, and skeletal anomalies with or without cardiac anomalies 2 (SSFSC2); SCUBE3-related short stature syndrome; SCUBE3-related developmental disorder; SCUBE3 deficiency. Gene aliases: *SCUBE3*, *CEGF3*.

**Data source type:** Information is derived from **aggregated disease-level resources** (OMIM, MONDO, HPO annotations) built on **individual-patient case series** from the primary literature; there is no large EHR-derived dataset for this ultra-rare condition. No dedicated Orphanet ORPHA code or MeSH term has been identified; MONDO:0030953 / OMIM:619184 are the canonical entries.

---

## Section 2 — Etiology

**Primary cause:** Purely genetic—**biallelic (homozygous or compound heterozygous) loss-of-function variants in *SCUBE3***. There is **no environmental, infectious, or multifactorial component**; this is a monogenic germline disorder ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)).

> *"bi-allelic inactivating variants in SCUBE3 have pleiotropic consequences on development and cause a previously unrecognized syndromic disorder. Eighteen affected individuals from nine unrelated families showed a consistent phenotype characterized by reduced growth, skeletal features, distinctive craniofacial appearance, and dental anomalies."* — [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)

**Genetic risk factors:** The causal variants are inactivating *SCUBE3* alleles (nonsense, canonical splice-site, exon-skipping deletions, and functionally validated missense variants). **Consanguinity is a major driver**, with homozygous variants reported in Turkish, Iranian, Saudi/Emirati, Indian, Israeli, and Brazilian families. No modifier genes have been established.

**Environmental risk factors / protective factors / gene-environment interactions:** None known or applicable. No lifestyle, occupational, toxic, or dietary factors have been implicated, and no protective alleles or environmental protective factors are reported.

---

## Section 3 — Phenotypes

Phenotype frequencies below are drawn from HPO disease annotations for OMIM:619184, sourced from the founding cohort (~15 evaluable individuals; [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)). The phenotype is prenatal-onset, non-progressive in its core growth deficit, and of variable expressivity.

> *"Eighteen affected individuals from nine unrelated families showed a consistent phenotype characterized by reduced growth, skeletal features, distinctive craniofacial appearance, and dental anomalies."* — Lin et al. 2021

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Postnatal growth retardation / short stature | HP:0008897 | ~100% (15/15) | Physical/growth |
| High forehead | HP:0000348 | ~100% (15/15) | Craniofacial sign |
| Long face | HP:0000276 | ~100% (14/14) | Craniofacial sign |
| Triangular face | HP:0000325 | ~100% (14/14) | Craniofacial sign |
| Short chin | HP:0000331 | ~100% (14/14) | Craniofacial sign |
| Long nose | HP:0003189 | ~87% (13/15) | Craniofacial sign |
| Prominent nasal bridge | HP:0000426 | ~87% (13/15) | Craniofacial sign |
| Pointed chin | HP:0000307 | ~85% (11/13) | Craniofacial sign |
| Dental crowding | HP:0000678 | 80% (12/15) | Dental anomaly |
| Short palm | HP:0004279 | 80% (12/15) | Skeletal |
| Brachydactyly | HP:0001156 | 80% (12/15) | Skeletal |
| Microcephaly | HP:0000252 | ~69% (9/13) | Craniofacial |
| Intrauterine growth retardation | HP:0001511 | ~73% (8/11) | Growth, antenatal |
| Antenatal onset | HP:0030674 | ~73% (8/11) | Temporal |
| Thick vermilion border | HP:0012471 | ~47% (7/15) | Craniofacial |
| Short long bone | HP:0003026 | ~55% (6/11) | Skeletal |
| Scoliosis | HP:0002650 | ~46% (6/13) | Skeletal |
| Enamel hypoplasia | HP:0006297 | ~27% (4/15) | Dental |
| 11 pairs of ribs | HP:0000878 | ~31% (4/13) | Skeletal |
| Oligodontia / hypodontia | HP:0000677 / HP:0000668 | ~13% (2/15 each) | Dental |
| Brittle hair | HP:0002299 | ~13% (2/15) | Ectodermal |
| Pierre-Robin sequence | HP:0000201 | ~14% (2/14) | Craniofacial |
| Atrial septal defect | HP:0001631 | ~14% (2/14) | Cardiac (variable) |
| Global developmental delay | HP:0001263 | ~7% (1/15) | Neurodevelopmental |
| Intellectual disability | HP:0001249 | ~7% (1/15) | Neurodevelopmental |

**Key clinical points:**
- **Cognition is usually normal** (developmental delay/intellectual disability each ~7%), an important distinguishing feature.
- **Cardiac anomalies are variable** (ASD, arrhythmia, patent foramen ovale)—hence "with or without cardiac anomalies" in the disease name.
- Occasional/rare features: joint hypermobility or stiffness, nystagmus/strabismus/astigmatism, hypotonia, cleft palate, hypospadias, tracheobronchomalacia, bicoronal craniosynostosis, oropharyngeal dysphagia. The expanded ocular/skeletal spectrum (high-arched eyebrows, epicanthus, blepharoptosis, hypotelorism, radial bowing, irregular vertebral endplates, narrow iliac wings) was added by [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/).

**Severity/progression:** Short stature is congenital and stable rather than progressive; scoliosis may progress and requires surveillance. **Quality-of-life impact** derives chiefly from short stature, skeletal (spinal) issues, and dental problems; disease-specific QoL instrument data (EQ-5D/SF-36/PROMIS) are not available.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** *SCUBE3* (HGNC:23310, NCBIGene:222663, 6p21.31, transcript **NM_152753.4**).

**Pathogenic variant spectrum.** ClinVar (accessed 2026) lists ~13 Pathogenic + 1 Pathogenic/Likely-pathogenic + 1 Likely-pathogenic *SCUBE3* records among ~184 total (63 VUS, 4 benign/LB). Disease-associated variants converge on **loss of function**:

| Variant (NM_152753.4) | Protein | Class |
|---|---|---|
| c.1557C>A | p.Cys519Ter | Nonsense |
| c.2785C>T | p.Arg929Ter | Nonsense |
| c.1717C>T | p.Arg573Ter | Nonsense (conflicting) |
| c.2599+2T>C | — | Canonical splice |
| c.2239+1G>A | — | Canonical splice |
| c.829+3_952+2del | — | Exon-skipping deletion |
| c.2444T>C | p.Ile815Thr | Missense (Path/LP) |
| c.611G>A | p.Gly204Asp | Missense |
| c.291C>G | p.Cys97Trp | Missense (cysteine) |
| c.908G>C | p.Cys303Ser | Missense (disrupts EGF disulfide) |
| NG_050574.1 delins-inversion | — | Structural |

Contiguous-gene **6p21 CNV deletions** (e.g., chr6:34.4–38.4 Mb) have also been reported (with severe IUGR). All variants are **germline**.

**Functional consequences.** In vitro validation showed variants variably impair transcript processing, protein secretion, and function, dysregulating BMP signaling:

> *"In vitro functional validation studies demonstrated a variable impact of disease-causing variants on transcript processing, protein secretion and function, and their dysregulating effect on bone morphogenetic protein (BMP) signaling."* — [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)

**Population constraint (gnomAD, ENSG00000146197):** pLI = 1.0; LOEUF (oe_lof_upper) = 0.378; oe_lof = 0.283 (33 observed vs 117 expected LoF); missense Z = 3.72. The gene is strongly constrained yet tolerant of heterozygous LoF alleles at low frequency—consistent with rare recessive carriers. No founder mutation established.

**Modifier genes / epigenetics:** No modifier genes or disease-specific epigenetic mechanisms have been reported. **Chromosomal abnormalities:** the contiguous-gene 6p21 microdeletions noted above.

---

## Section 5 — Environmental Information

Not applicable. SSFSC2 is a **monogenic germline disorder with no known environmental, lifestyle, or infectious contributors**. No toxins, radiation, occupational exposures, dietary factors, or pathogens are implicated.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function *SCUBE3* variants** (nonsense, splice, exon-skip, or destabilizing missense) → **reduced/absent functional SCUBE3 protein**, either through nonsense-mediated decay, impaired transcript processing, or defective secretion of misfolded protein. *(Demonstrated in vitro; [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/).)*
2. Destabilizing missense variants (e.g., p.Cys303Ser) → **disruption of a critical disulfide bridge in the 7th EGF-like repeat**, impairing protein stability and reducing secretion. *(AlphaFold3 modeling; [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/).)*
3. Loss of cell-surface SCUBE3 co-receptor → **failure to recruit BMP receptor complexes into lipid-raft microdomains** and reduced augmentation of BMP–BMP type I receptor interactions → **decreased BMP2/BMP4 signaling**. *(Demonstrated; [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/).)*
4. Reduced BMP signaling (and altered TGF-β/SMAD2-3 co-modulation) → **impaired SMAD-mediated transcriptional output** in growth-plate cells. *(BMP branch demonstrated; TGF-β branch inferred from CUB-domain ligand activity, [PMID: 21441952](https://pubmed.ncbi.nlm.nih.gov/21441952/).)*
5. **Impaired chondrogenesis and osteogenesis** at the endochondral growth plate → **defective endochondral bone growth**. *(Demonstrated in Scube3⁻/⁻ mouse; [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/).)*
6. **Branch A:** growth-plate defect → **prenatal-onset short stature, short long bones, brachydactyly, scoliosis, rib anomalies.**
   **Branch B:** cranial neural-crest/dental mesenchyme BMP defect → **distinctive craniofacial gestalt and dental anomalies.**
   **Branch C (variable):** cardiac BMP signaling perturbation → **septal defects / arrhythmia** in a minority.

### Detail

**Molecular pathways.** The core lesion is in the **BMP2/BMP4 signaling pathway** (SMAD1/5/8 branch), with SCUBE3 acting as a positive co-receptor:

> *"We show that SCUBE3 acts as a BMP2/BMP4 co-receptor, recruits the BMP receptor complexes into raft microdomains, and positively modulates signaling possibly by augmenting the specific interactions between BMPs and BMP type I receptors."* — [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)

SCUBE3 additionally acts as an **endogenous TGF-β type II receptor ligand** through its C-terminal CUB domain, inducing SMAD2/3 phosphorylation:

> *"bound to transforming growth factor-β (TGF-β) type II receptor through the C-terminal CUB domain, activated TGF-β signaling and triggered the epithelial-mesenchymal transition (EMT). This process includes the induction of Smad2/3 phosphorylation"* — [PMID: 21441952](https://pubmed.ncbi.nlm.nih.gov/21441952/)

Recombinant SCUBE3 boosts BMP2/TGF-β expression and drives osteogenic differentiation via SMAD phosphorylation in human bone-marrow mesenchymal stem cells, reinforcing its pro-osteogenic role ([PMID: 39250278](https://pubmed.ncbi.nlm.nih.gov/39250278/)). SCUBE family members also participate in **FGF** (zebrafish muscle development) and **Hedgehog** signaling.

**Protein dysfunction.** SCUBE3 (~993 aa) has five modular domains:

> *"organized into five modular domains: (1) an N-terminal signal peptide sequence, (2) nine tandem epidermal growth factor (EGF)-like repeats, (3) a large spacer region, (4) three cysteine-rich (CR) motifs, and (5) a CUB domain at the C-terminus"* — [PMID: 37237303](https://pubmed.ncbi.nlm.nih.gov/37237303/)

The cysteine-rich, disulfide-stabilized EGF-like repeats are essential for folding and secretion; pathogenic missense variants that eliminate cysteines (Cys97Trp, Cys303Ser, Cys519Ter) destabilize the protein and reduce secretion. Structural modeling confirms this:

> *"Protein modeling using AlphaFold3 revealed disruption of a critical disulfide bridge within the seventh epidermal growth factor-like repeat, likely affecting protein stability."* — [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)

**Cellular processes and cell types.** Upstream: chondrocytes and osteoblasts of the endochondral growth plate; cranial neural-crest-derived mesenchyme; odontoblasts/dental mesenchyme. Downstream clinical manifestations follow from impaired proliferation/differentiation in these lineages. Suggested **GO** terms: BMP signaling pathway (GO:0030509), chondrocyte differentiation (GO:0002062), osteoblast differentiation (GO:0001649), endochondral ossification (GO:0001958), SMAD protein signal transduction (GO:0060395). Suggested **CL** terms: chondrocyte (CL:0000138), osteoblast (CL:0000062), odontoblast (CL:0000060), neural crest cell (CL:0000333).

**Metabolic / immune / epigenetic involvement.** No primary metabolic derangement, immune dysregulation, or epigenetic mechanism is part of the core disease; the single interesting metabolic observation is that recombinant SCUBE3 activates mitophagy and ameliorates oxidative stress during osteogenesis in vitro ([PMID: 39250278](https://pubmed.ncbi.nlm.nih.gov/39250278/)), which is peripheral to the germline disease.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level (primary):** Skeletal system—long bones, vertebral column, ribs, hands (brachydactyly), skull/craniofacial skeleton. Endocrine-independent growth failure (GH/IGF-1 axis normal). **Secondary/variable:** cardiovascular system (atrial septal defect, PFO, arrhythmia); dentition; occasionally airway (tracheobronchomalacia), palate, and eyes.

**Suggested UBERON terms:** skeletal system (UBERON:0001434), endochondral bone (UBERON:0002513), epiphyseal growth plate (UBERON:0002332), long bone (UBERON:0002495), vertebral column (UBERON:0001130), rib (UBERON:0002228), skull (UBERON:0003129), tooth (UBERON:0001091), heart (UBERON:0000948), interatrial septum (UBERON:0002085).

**Tissue / cell level:** Connective tissue—cartilage (growth-plate chondrocytes) and bone (osteoblasts); dental mesenchyme/odontoblasts; cranial neural crest derivatives. **CL terms** as above.

**Subcellular level:** Secreted/cell-surface (plasma-membrane-associated) glycoprotein; biosynthetic defects implicate the **endoplasmic reticulum** (folding/secretion, GO:0005783) and **extracellular space / lipid-raft plasma-membrane microdomains** (GO:0045121) where SCUBE3 co-receptor function occurs.

**Localization / lateralization:** Skeletal and craniofacial involvement is **bilateral and largely symmetric**; scoliosis introduces axial asymmetry; cardiac defects are structural (septal).

**Expression sites:** primary osteoblasts, long bones, axial-skeleton cartilage, vascular endothelium, platelets, and mammary ductal epithelium ([PMID: 37237303](https://pubmed.ncbi.nlm.nih.gov/37237303/), [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)).

---

## Section 8 — Temporal Development

- **Onset:** **Congenital / prenatal.** Intrauterine growth retardation and antenatal onset are documented in the majority (8/11 each). Short stature is present from birth.
- **Onset pattern:** Chronic/insidious—a developmental, non-inflammatory process.
- **Progression:** The core growth deficit is **stable (non-progressive)** rather than degenerative; the child remains short-statured. **Scoliosis may progress** through childhood/adolescence and requires monitoring.
- **Disease course:** Lifelong, chronic, non-episodic, non-relapsing.
- **Critical periods:** The prenatal and childhood growth-plate windows are the period of vulnerability; there is no known therapeutic window that reverses the growth-plate signaling defect.
- **Remission:** None (genetic, structural condition).

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive** (HP:0000007), fully penetrant in reported biallelic cases with **variable expressivity** ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/), [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)). Most cases are homozygous; some are compound heterozygous.
- **Epidemiology:** **Ultra-rare.** ~20 patients from ~10 families reported worldwide as of 2025; no prevalence or incidence estimate exists.

> *"is a very rare genetic disorder caused by biallelic pathogenic variants in the SCUBE3 gene and has been reported in approximately 20 patients to date"* — [PMID: 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)

- **Consanguinity:** A major driver—homozygous variants in Turkish, Iranian, Saudi/Emirati, Indian, Israeli, and Brazilian families.
- **Carrier frequency:** Rare; gnomAD shows only 33 heterozygous LoF alleles (LOEUF 0.38). No founder mutation.
- **Penetrance / anticipation / mosaicism:** Complete penetrance for biallelic genotypes; no genetic anticipation (not a repeat-expansion disorder); no germline mosaicism reported.
- **Sex ratio:** No sex bias; both sexes affected.
- **Population demographics:** No population-specific prevalence beyond enrichment in consanguineous populations; no established geographic clustering of specific variants.

---

## Section 10 — Diagnostics

**Diagnostic approach — molecular.** Recognition of the **clinical gestalt** (prenatal-onset short stature + long/triangular face, high forehead, long nose, small pointed chin + brachydactyly + dental crowding/enamel defects with preserved cognition) followed by confirmation of **biallelic *SCUBE3* variants**:
- **Whole-exome sequencing (WES)** — the original discovery method; high yield ([PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)).
- **Whole-genome sequencing (WGS)** — captures splice/structural variants.
- **Multigene short-stature / skeletal-dysplasia panels** including *SCUBE3*; *SCUBE3* now appears on SGA/short-stature panels ([PMID: 41001785](https://pubmed.ncbi.nlm.nih.gov/41001785/)).
- **Single-gene testing** once the phenotype is recognized.
- **Chromosomal microarray (CMA)** — detects contiguous-gene 6p21 deletions.

**Supportive workup:** skeletal survey/radiographs (brachydactyly, short long bones, scoliosis, 11 rib pairs, narrow iliac wings, vertebral endplate irregularities); echocardiography (ASD/PFO); dental/orthodontic evaluation; ophthalmologic exam; hearing assessment. **Endocrine (GH/IGF-1) axis is typically normal**—this is *not* classic GH deficiency, and there is **no specific biomarker**.

**Differential diagnosis:** 3M syndrome, Silver-Russell syndrome, Floating-Harbor syndrome, other primordial/skeletal-dysplasia short-stature disorders, ACAN- and COL2A1-related short stature. Preserved cognition, the specific facial gestalt, and biallelic *SCUBE3* findings distinguish SSFSC2.

**Screening:** Carrier/cascade testing in affected consanguineous families; prenatal/preimplantation genetic testing where the familial variants are known. No population newborn screening exists (ultra-rare).

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality:** **Non-lethal**; life expectancy is generally normal. No disease-specific mortality data reported.
- **Morbidity / function:** Principal morbidity is **short stature**, **skeletal (scoliosis)** and **dental** problems; cognition is generally preserved, so functional/educational outcomes are usually good.
- **Quality of life:** Impacted mainly by stature, orthopedic, and dental issues; no formal QoL instrument data available.
- **Complications:** Scoliosis progression, dental crowding/enamel defects requiring orthodontic care, occasional cardiac defects requiring follow-up, rare airway issues (tracheobronchomalacia).
- **Prognostic factors:** Severity is variable and not strongly predicted by a single factor; no validated prognostic biomarkers exist.

---

## Section 12 — Treatment

**No disease-modifying or targeted therapy exists.** Management is **supportive, multidisciplinary, and symptom-directed:**

| Domain | Intervention | Suggested NCIT concept |
|---|---|---|
| Orthopedic | Spinal/scoliosis monitoring and management; orthopedic surgery as needed | Orthopedic Surgery |
| Dental | Orthodontic care for crowding, enamel defects, oligo/hypodontia | Dental Care |
| Cardiac | Echocardiographic surveillance; management of ASD/arrhythmia | Supportive Care Intervention |
| Growth | Growth monitoring; recombinant human GH has been *tried* with unproven/limited efficacy | Growth Hormone Therapy |
| Genetics | Genetic counseling for families | Genetic Counseling |
| Supportive | Developmental support if needed; ophthalmology/audiology follow-up | Supportive Care Intervention |

**Important caveat:** Because the growth failure reflects a **local growth-plate BMP-signaling defect rather than GH deficiency**, recombinant human growth hormone is of unproven benefit. No pharmacogenomic, gene-therapy, cell-therapy, RNA-based, immunotherapy, or clinical-trial (NCT) interventions are currently available for this indication.

---

## Section 13 — Prevention

Primary prevention of the disease itself is not possible (germline monogenic). Relevant preventive/genetic measures:
- **Genetic counseling** for at-risk consanguineous families (25% recurrence risk per pregnancy for carrier couples).
- **Carrier / cascade screening** of relatives once familial variants are identified.
- **Prenatal diagnosis / preimplantation genetic testing** for known familial variants.
- **Tertiary prevention** (preventing complications): scoliosis surveillance, dental prophylaxis/orthodontics, cardiac follow-up.
No immunization, behavioral, environmental, or public-health interventions are applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Highly conserved across vertebrates ([PMID: 37237303](https://pubmed.ncbi.nlm.nih.gov/37237303/)). Mouse *Scube3* (NCBIGene:268935, chr17), rat *Scube3* (NCBIGene:294297), zebrafish *scube3* (NCBIGene:100000687).
- **Natural disease:** **No naturally occurring SCUBE3 disease reported in companion animals or wildlife** (no OMIA entry). No breed-specific (VBO) associations.
- **Comparative biology:** Disease mechanism (BMP co-receptor function in skeletal development) is evolutionarily conserved, enabling faithful mouse and zebrafish modeling.
- **Transmission:** Not applicable—no zoonotic or infectious component.

---

## Section 15 — Model Organisms

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| *Scube3⁻/⁻* knockout mouse | Mammalian, null | Craniofacial & dental defects, reduced body size, defective endochondral bone growth from impaired BMP-mediated chondrogenesis/osteogenesis—recapitulates the human disorder | [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/) |
| *Scube3^N294K/N294K* ENU missense mouse (German Mouse Clinic) | Mammalian, missense | Skeletal morphology abnormalities, altered bone-metabolism parameters, changed renal function, hearing impairment, plus energy-metabolism/behavioral/neurological alterations; resembles Paget disease of bone (6p21 is a PDB locus) | [PMID: 27815347](https://pubmed.ncbi.nlm.nih.gov/27815347/) |
| Earlier *Scube3*-null mouse | Mammalian, null | Expressed in multiple developing tissues; dispensable for embryonic survival | [PMID: 23383134](https://pubmed.ncbi.nlm.nih.gov/23383134/) |
| Zebrafish *scube3* | Teleost | Modulates FGF signaling during fast-muscle development; SCUBE family shows redundant/novel developmental roles | [PMID: 24849601](https://pubmed.ncbi.nlm.nih.gov/24849601/), [PMID: 40912446](https://pubmed.ncbi.nlm.nih.gov/40912446/) |
| Human BMSC in vitro | Cellular | rhSCUBE3 promotes osteogenic differentiation, mitophagy via BMP2/TGF-β–SMAD | [PMID: 39250278](https://pubmed.ncbi.nlm.nih.gov/39250278/) |

Model characteristics:

> *"Scube3⁻/⁻ mice showed craniofacial and dental defects, reduced body size, and defective endochondral bone growth due to impaired BMP-mediated chondrogenesis and osteogenesis, recapitulating the human disorder."* — [PMID: 33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/)

> *"Scube3N294K/N294K mutants showed morphological abnormalities of the skeleton, alterations of parameters relevant for bone metabolism, changes in renal function, and hearing impairments."* — [PMID: 27815347](https://pubmed.ncbi.nlm.nih.gov/27815347/)

**Applications:** growth-plate BMP signaling, skeletal/craniofacial/dental development, bone metabolism. **Limitations:** the knockout captures core skeletal/craniofacial phenotypes but human variant-specific hypomorphic effects (variable secretion/function) and the human cognitive-sparing may not be fully modeled by null alleles.

---

## Mechanistic Model / Interpretation

```
Biallelic LoF SCUBE3 variants
  (nonsense / splice / exon-skip / destabilizing missense)
        │  NMD, impaired processing, misfolding (disulfide loss in EGF repeats)
        ▼
Reduced / non-functional secreted SCUBE3 co-receptor
        │  fails to recruit BMP receptor complexes to lipid rafts;
        │  loss of BMP–BMPR-I interaction augmentation
        ▼
Decreased BMP2/BMP4 signaling  ── (co-modulation) ── TGF-β/SMAD2/3, FGF, Hedgehog
        │  reduced SMAD1/5/8 transcriptional output
        ▼
Impaired chondrogenesis + osteogenesis at the endochondral growth plate
        │
        ├──► Branch A (skeleton): prenatal short stature, short long bones,
        │                         brachydactyly, scoliosis, 11 rib pairs
        ├──► Branch B (craniofacial/dental): long triangular face, high forehead,
        │                         long nose, pointed chin, dental crowding/enamel defects
        └──► Branch C (variable): cardiac septal defects / arrhythmia
```

**Upstream vs downstream:** the mutation → protein loss → BMP co-receptor failure steps are upstream and directly demonstrated in vitro and in the mouse; the tissue-specific clinical branches are downstream and reflect the developmental requirement for BMP signaling in each lineage. The consistency between the in-vitro co-receptor data, the AlphaFold3 structural modeling, and the faithful *Scube3⁻/⁻* mouse gives this causal chain strong internal coherence.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [33308444](https://pubmed.ncbi.nlm.nih.gov/33308444/) | *SCUBE3 loss-of-function causes a recognizable recessive developmental disorder due to defective BMP signaling* | **Landmark/defining paper.** Cohort of 18 individuals/9 families; establishes recessive inheritance, phenotype, BMP2/BMP4 co-receptor mechanism, in-vitro functional validation, and the recapitulating *Scube3⁻/⁻* mouse. |
| [40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/) | Yeter et al. 2025 case report | Expands phenotype (ocular/skeletal), reports ~20 patients worldwide, AlphaFold3 disulfide-disruption mechanism for p.Cys303Ser. |
| [37237303](https://pubmed.ncbi.nlm.nih.gov/37237303/) | SCUBE3 review | Defines five-domain protein architecture, expression sites, multipathway co-receptor role, vertebrate conservation. |
| [21441952](https://pubmed.ncbi.nlm.nih.gov/21441952/) | *SCUBE3 is an endogenous TGF-β receptor ligand...* | Documents CUB-domain TGF-β binding → SMAD2/3 phosphorylation—the TGF-β arm of SCUBE3 function. |
| [39250278](https://pubmed.ncbi.nlm.nih.gov/39250278/) | *SCUBE3 promotes osteogenic differentiation... in hBMSCs* | In-vitro confirmation of pro-osteogenic BMP2/TGF-β–SMAD role; supports the growth/bone mechanism. |
| [27815347](https://pubmed.ncbi.nlm.nih.gov/27815347/) | *Scube3^N294K* ENU mouse | Independent missense mouse model with skeletal/bone-metabolism phenotype. |
| [24084593](https://pubmed.ncbi.nlm.nih.gov/24084593/) | *Scube regulates synovial angiogenesis-related signaling* | Contextualizes SCUBE family antagonism/agonism across BMP/TGF-β/Hedgehog. |
| [41001785](https://pubmed.ncbi.nlm.nih.gov/41001785/) | Korean SGA-SS exome study | Shows *SCUBE3* appears among genes with likely-pathogenic variants in short-stature diagnostic panels. |

All primary mechanistic and clinical claims here are **human clinical** (cohort/case reports) reinforced by **model-organism** (mouse, zebrafish) and **in-vitro/computational** (functional assays, AlphaFold3) evidence.

---

## Limitations and Knowledge Gaps

- **Small evidence base:** ~20 patients worldwide; phenotype frequencies derive from a single founding cohort (~15 evaluable individuals). Frequencies are precise-looking but statistically fragile.
- **No epidemiology:** no prevalence/incidence estimate; no Orphanet ORPHA or MeSH term.
- **No prognostic biomarkers** and no natural-history/longitudinal cohort data (e.g., adult final height distributions, scoliosis progression rates).
- **Genotype–phenotype correlations** are not yet established (whether hypomorphic missense vs null alleles predict severity).
- **GH therapy efficacy is untested rigorously**—used empirically with unproven benefit.
- **TGF-β/FGF/Hedgehog contributions** to the human phenotype are inferred; only the BMP arm is directly demonstrated for the disease.
- **Cognitive-sparing mechanism** (why SCUBE3 loss largely spares cognition despite CNS expression) is unexplained.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to capture natural history: final adult height, scoliosis progression, cardiac and dental outcomes, and QoL (SF-36/PROMIS).
2. **Genotype–phenotype study** correlating residual SCUBE3 secretion/function (per-variant in-vitro assays) with clinical severity to build a variant-effect map on NM_152753.4.
3. **Controlled evaluation of recombinant GH** (or, mechanistically, growth-plate-directed BMP-pathway modulation) in a small cohort, given the local BMP defect rationale.
4. **Conditional/tissue-specific *Scube3* mouse models** (chondrocyte-, neural-crest-, cardiac-specific) to dissect the phenotype branches and test BMP-augmentation rescue.
5. **Deep phenotyping of the cardiac and ocular spectrum** to refine "with or without cardiac anomalies" penetrance estimates.
6. **Structural/biochemical work** on how missense EGF-repeat disulfide disruptions impair secretion, to identify potentially rescuable (chaperone-amenable) alleles.
7. **Formal ClinGen/ACMG variant curation and gene-disease validity classification** to standardize diagnostic reporting.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations. Evidence sources: human clinical cohorts/case reports, mouse and zebrafish model organisms, in-vitro functional assays, and computational structural modeling.*


## Artifacts

- [OpenScientist final report](SCUBE3-Related_Short_Stature_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCUBE3-Related_Short_Stature_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 28 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030953` (3 mentions) - the report calls it "MONDO"; MONDO calls it **short stature, facial dysmorphism, and skeletal anomalies with or without cardiac anomalies 2**
- `DOID:0112358` (1 mention) - the report calls it "DOID"; DOID calls it **short stature, facial dysmorphism, and skeletal anomalies with or without cardiac anomalies 2**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0002332` (1 mention) - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (2 mentions) - the report calls it "Autosomal recessive", "Inheritance:** **Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `HP:0008897` (1 mention) - the report calls it "Postnatal growth retardation / short stature"; HP calls it **Postnatal growth retardation**
- `GO:0045121` (1 mention) - the report calls it "extracellular space / lipid-raft plasma-membrane microdomains"; GO calls it **membrane raft**, and lists "glycolipid-enriched membrane domain" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Autosomal recessive", "Inheritance:** **Autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBIGene`, `OMIM`.