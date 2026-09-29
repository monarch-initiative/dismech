---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T10:33:10.918243'
end_time: '2026-09-07T10:48:31.411994'
duration_seconds: 920.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Frontotemporal Dementia And/Or Amyotrophic Lateral Sclerosis 2
  mondo_id: MONDO:0014395
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 13
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0001638
    reported_labels:
    - Spectrum-dependent
    ontology_label: Cardiomyopathy
  - term_id: HP:0009830
    reported_labels:
    - Allele-dependent
    ontology_label: Peripheral neuropathy
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Frontotemporal_Dementia_And_Or_Amyotrophic_Lateral_Sclerosis_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Frontotemporal_Dementia_And_Or_Amyotrophic_Lateral_Sclerosis_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Frontotemporal Dementia And/Or Amyotrophic Lateral Sclerosis 2
- **MONDO ID:** MONDO:0014395 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frontotemporal Dementia And/Or Amyotrophic Lateral Sclerosis 2** covering all of the
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

# Frontotemporal Dementia And/Or Amyotrophic Lateral Sclerosis 2 (FTDALS2): Comprehensive Disease Characteristics Report

**Disease:** Frontotemporal Dementia And/Or Amyotrophic Lateral Sclerosis 2 (FTDALS2)
**MONDO ID:** MONDO:0014395 · **OMIM:** #615911 · **Causal gene:** *CHCHD10* (HGNC:15559)
**Category:** Mendelian (autosomal dominant)

---

## Summary

Frontotemporal Dementia and/or Amyotrophic Lateral Sclerosis 2 (FTDALS2; OMIM #615911, MONDO:0014395) is a rare, adult/late-onset, autosomal dominant neurodegenerative disorder caused by heterozygous gain-of-function missense mutations in *CHCHD10*, a gene encoding a small mitochondrial intermembrane-space protein. It was defined by the discovery of the founding p.Ser59Leu (c.176C>T) mutation in a large French family exhibiting a strikingly multisystem "mitochondrial" phenotype that combined motor neuron disease, frontotemporal-dementia–like cognitive decline, cerebellar ataxia, and mitochondrial myopathy with ragged-red/COX-negative fibres and multiple mitochondrial DNA (mtDNA) deletions [PMID: 24934289]. FTDALS2 sits within a broader **CHCHD10 spectrum** that spans classical ALS, FTD-ALS, isolated mitochondrial myopathy/cardiomyopathy, late-onset spinal motor neuronopathy (SMAJ, Spinal Muscular Atrophy Jokela type), and Charcot-Marie-Tooth disease type 2, with a strong allele-specific genotype–phenotype correlation [PMID: 37021679; PMID: 25428574].

Mechanistically, mutant CHCHD10 misfolds and aggregates, disassembles the MICOS (mitochondrial contact site and cristae organizing system) complex, collapses cristae junctions, and destabilizes the mitochondrial genome — explaining the accumulation of deleted mtDNA in patient muscle [PMID: 26666268]. Downstream, mutant protein activates the OMA1 peptidase, which cleaves the long form of the fusion protein OPA1 (L-OPA1), triggers the mitochondrial integrated stress response (mtISR), impairs mitochondrial axonal transport, and drives cytoplasmic accumulation of TDP-43, the pathological hallmark shared with sporadic ALS/FTLD-TDP [PMID: 32338760; PMID: 30877432; PMID: 28585542]. The mechanism is best described as a **toxic gain-of-function / dominant-negative**, not simple haploinsufficiency; the degree of MICOS disruption tracks clinical severity [PMID: 30092269].

CHCHD10 mutations are an **ultra-rare** cause of ALS/FTD (~0.4% of cohorts), and careful population-genetics work is essential to separate genuinely pathogenic ultra-rare alleles (p.Ser59Leu, p.Arg15Leu) from historically-reported benign polymorphisms such as p.Pro34Ser (gnomAD allele frequency ~0.4%, far too common to be causal) [PMID: 27056076; PMID: 28318595]. There is **no disease-specific therapy**; management follows ALS/FTD symptomatic standards (riluzole, edaravone, multidisciplinary supportive care) [PMID: 42113599; PMID: 42666355]. Experimental precision strategies targeting the MICOS/mitochondrial-transport axis (e.g., nifuroxazide), the integrated stress response, and metabolic/creatine buffering are under active investigation in yeast, knock-in mouse, and patient iPSC-derived motor neuron models [PMID: 39478664; PMID: 40400037].

---

## Key Findings

### Finding 1 — *CHCHD10* is the causal gene (autosomal dominant)

FTDALS2 is caused by heterozygous mutations in **CHCHD10** (coiled-coil-helix-coiled-coil-helix domain containing 10, chromosome 22q11.23, HGNC:15559), encoding a mitochondrial intermembrane-space protein. The founding p.Ser59Leu mutation was identified in a large French family with mitochondrial myopathy associated with motor neuron disease: *"We reported patients, carrying the p.Ser59Leu heterozygous mutation in CHCHD10, from a large family with a mitochondrial myopathy associated with motor neuron disease (MND)"* [PMID: 30874923]. The allelic spectrum was subsequently extended across ALS, FTD-ALS, and milder syndromes; for example, a distinct milder allele defines a lower motor neuron syndrome: *"Mutation c.197G>T p.G66V in CHCHD10 is the cause of the lower motor neuron syndrome LOSMoN/SMAJ"* [PMID: 25428574]. Inheritance is autosomal dominant.

### Finding 2 — Core lesion: MICOS disassembly, cristae collapse, mtDNA instability

CHCHD10 resides within the MICOS complex together with mitofilin (MIC60), CHCHD3, and CHCHD6. Mutant CHCHD10 disassembles MICOS and collapses cristae junctions: *"CHCHD10 resides with mitofilin, CHCHD3 and CHCHD6 within the 'mitochondrial contact site and cristae organizing system' (MICOS) complex. CHCHD10 mutations lead to MICOS complex disassembly and loss of mitochondrial cristae with a decrease in nucleoid number and nucleoid disorganization"* [PMID: 26666268]. This links directly to mtDNA instability: *"Repair of the mitochondrial genome after oxidative stress is impaired in CHCHD10 mutant fibroblasts and this likely explains the accumulation of deleted mtDNA molecules in patient muscle"* [PMID: 26666268]. Importantly, the **degree of MICOS disruption correlates with disease severity**: *"Loss of MICOS complex integrity and mitochondrial damage, but not TDP-43 mitochondrial localisation, are likely associated with severity of CHCHD10-related diseases"* [PMID: 30092269].

### Finding 3 — Toxic gain-of-function → OMA1/OPA1 cleavage → mtISR → cytoplasmic TDP-43

The pathogenic mechanism is a tissue-specific toxic gain-of-function with dominant-negative activity, not haploinsufficiency. A knock-in mouse bearing the mouse-equivalent S59L (S55L) mutation was generated *"to investigate the pathogenic mechanisms of CHCHD10 … harboring the mouse-equivalent of a disease-associated human S59L mutation, S55L in the endogenous mouse gene,"* demonstrating a tissue-specific toxic gain-of-function and mitochondrial stress response [PMID: 30877432]. The downstream cristae-shaping mechanism is OMA1-mediated: *"C2/C10 DKO mice have disrupted mitochondrial cristae, because of cleavage of the mitochondrial-shaping protein long form of OPA1 (L-OPA1) by the stress-induced peptidase OMA1,"* and these mice *"partially phenocopied mutant C10 KI mice with the development of cardiomyopathy and activation of the integrated mitochondrial integrated stress response in affected tissues"* [PMID: 32338760]. The link to TDP-43 pathology is direct: *"FTD/ALS-associated mutations (R15L and S59L) exhibit loss of function phenotypes in C. elegans genetic complementation assays and dominant negative activities in mammalian systems, resulting in mitochondrial/synaptic damage and cytoplasmic TDP-43 accumulation"* [PMID: 28585542]. Insoluble CHCHD10 co-aggregates with phospho-TDP-43 and correlates with insoluble TDP-43 in FTLD-TDP brains [PMID: 35787294].

### Finding 4 — Multisystem late-onset clinical phenotype

In the founding p.Ser59Leu (c.176C>T) family, *"We report a large family with a late-onset phenotype including motor neuron disease, cognitive decline resembling frontotemporal dementia, cerebellar ataxia and myopathy"* [PMID: 24934289]. Muscle biopsy findings were characteristically mitochondrial: *"In all patients, muscle biopsy showed ragged-red and cytochrome c oxidase-negative fibres with combined respiratory chain deficiency and abnormal assembly of complex V,"* and *"The multiple mitochondrial DNA deletions found in skeletal muscle revealed a mitochondrial DNA instability disorder"* [PMID: 24934289]. Patient fibroblasts showed respiratory chain deficiency, mitochondrial ultrastructural alterations, and fragmentation of the mitochondrial network; overexpression of mutant CHCHD10 in HeLa cells caused loss, disorganization, and dilatation of cristae.

### Finding 5 — Rarity, severity gradient, and pathology staging

CHCHD10 mutations are a rare cause of ALS/FTD-ALS. Screening of 499 Chinese ALS patients found *"The mutation frequency of CHCHD10 (0.4 %, 2/487) in a Chinese SALS population"* [PMID: 27056076], and some variants have a *"controversial role in ALS"* [PMID: 28318595]. Variant-dependent severity is well established: p.Ser59Leu causes severe FTD-ALS with mtDNA instability, whereas the SMAJ phenotype is mild — *"patients presenting with SMAJ phenotype have neither mitochondrial myopathy nor mtDNA instability"* [PMID: 30092269; PMID: 25428574]. In knock-in mice, *"Mitochondrial defect in muscle precedes neuromuscular junction degeneration and motor neuron death in CHCHD10"* [PMID: 30874923], establishing a muscle → NMJ → motor neuron staging.

### Finding 6 — Population genetics separates pathogenic from benign variants

A direct gnomAD v4 query (CHCHD10, ENSG00000250479, chr22:23,765,834–23,767,972, GRCh38) confirmed that pathogenic FTD-ALS alleles are ultra-rare: **p.Ser59Leu** allele frequency (AF) = 6.9×10⁻⁷ (1 of 1,446,818 exome alleles); **p.Arg15Leu** AF = 0 (0 of 949,590); **p.Ala35Asp** AF = 6.1×10⁻⁶; the Finnish SMAJ founder **p.Gly66Val** AF = 2.1×10⁻⁶ (3 alleles). By stark contrast, **p.Pro34Ser**, reported in early ALS/FTD studies, has AF = 0.0043 (5,542 exome alleles; ~0.23% in genomes) — far above any plausible disease-allele frequency, indicating it is a benign/likely-benign common polymorphism (ACMG BA1/BS1). This population evidence explains the literature's caution that CHCHD10 has *"a controversial role in ALS"* [PMID: 28318595] — the controversy largely reflects benign common variants being conflated with true ultra-rare pathogenic alleles.

### Finding 7 — Strong allele-specific genotype–phenotype correlation

Distinct CHCHD10 alleles map to distinct clinical syndromes: *"dominant mutations in the mitochondrial protein CHCHD10 (p.R15L and p.S59L) and its paralog CHCHD2 (p.T61I) were shown to cause familial amyotrophic lateral sclerosis (ALS) and Parkinson's disease (PD), respectively"* [PMID: 37021679]. Further: *"Different mutations in CHCHD10 cause additional neuromuscular disorders, including the lower motor neuron disease Spinal Muscular Atrophy Jokela type (SMAJ) (p.G66V) and autosomal dominant isolated mitochondrial myopathy (IMMD) (p.G58R)"* [PMID: 37021679]. The unifying mechanism is toxic misfolding: *"mitochondrial dysfunction may drive ALS and PD pathogenesis by a gain of function mechanism, driven by protein misfolding of CHCHD2 and CHCHD10 into toxic species"* [PMID: 37021679]. CHCHD10 is an intrinsically disordered/low-complexity protein that heterodimerizes with its paralog CHCHD2 [PMID: 35791387; PMID: 36158221].

### Finding 8 — No disease-specific therapy; emerging precision strategies

No approved CHCHD10-specific therapy exists; management follows ALS/FTD symptomatic standards (riluzole — modest survival benefit; edaravone — narrow eligibility; multidisciplinary care) [PMID: 42113599; PMID: 42666355]. Experimental precision approaches are emerging. A yeast-based repurposing screen identified nifuroxazide: *"nifuroxazide rescues mitochondrial network fragmentation and cristae abnormalities in CHCHD10^S59L/+ patient fibroblasts. This molecule also decreases caspase-dependent death of human CHCHD10^S59L/+ induced pluripotent stem cell-derived motor neurons,"* and *"Its benefits involve KIF5B-mediated mitochondrial transport enhancement, evidenced by increased axonal movement and syntaphilin degradation in patient-derived motor neurons"* [PMID: 39478664]. Metabolic dysregulation is a downstream feature and potential biomarker/target: *"CHCHD10 p.G66V dysregulates energy metabolism, leading to altered redox balance and energy buffering by creatine metabolism,"* and *"we report the first homozygous CHCHD10 patient, and show that the variant dosage dictates the severity of the motor neuron disease in SMAJ"* [PMID: 40400037].

---

## Report by Section

### 1. Disease Information

FTDALS2 is a Mendelian, autosomal dominant, adult/late-onset neurodegenerative disorder within the ALS–FTD spectrum, caused by *CHCHD10* mutations and distinguished by prominent mitochondrial features (myopathy with ragged-red/COX-negative fibres, mtDNA instability) alongside motor neuron disease, FTD-like cognitive decline, and cerebellar ataxia [PMID: 24934289].

- **Key identifiers:** OMIM #615911; MONDO:0014395; gene *CHCHD10* (HGNC:15559; NCBI Gene 400916; Ensembl ENSG00000250479); chromosome 22q11.23. ICD-10 mapping is via G31.0 (frontotemporal dementia) and G12.21 (ALS); ICD-11 in the 8B60/8B00 range. MeSH: Frontotemporal Dementia; Amyotrophic Lateral Sclerosis.
- **Synonyms / alternative names:** FTDALS2; "FTD-ALS type 2"; part of the "CHCHD10 spectrum" / "CHCHD10-related disease"; historically described as "mitochondrial myopathy with motor neuron disease." Related spectrum entities include SMAJ (Jokela-type spinal muscular atrophy), isolated mitochondrial myopathy (IMMD), and CMT2.
- **Data source type:** Information is derived from aggregated disease-level resources (OMIM, Orphanet, ClinVar, gnomAD) and primary literature (family pedigrees, cohort screens, model organisms), not from EHR-level individual patient records.

### 2. Etiology

- **Causal factors:** Genetic. Heterozygous gain-of-function missense mutations in *CHCHD10* [PMID: 24934289; PMID: 37021679]. No infectious or purely environmental cause.
- **Genetic risk factors:** The causal variants are ultra-rare dominant missense alleles — principally **p.Ser59Leu (c.176C>T)** and **p.Arg15Leu** for the ALS/FTD-ALS phenotype [PMID: 37021679]. Allele-specific: p.G66V → SMAJ; p.G58R → isolated mitochondrial myopathy. The paralog *CHCHD2* (p.T61I) causes Parkinson's disease, and CHCHD2/CHCHD10 heterodimerize [PMID: 37021679; PMID: 36158221].
- **Genetic pseudo-risk / benign confounders:** p.Pro34Ser is a common benign polymorphism (gnomAD AF ~0.4%) historically misattributed as a risk allele (ACMG BA1/BS1) — a key caution for variant interpretation (Finding 6) [PMID: 28318595].
- **Environmental / lifestyle risk factors:** Age (late-onset) is the dominant non-genetic factor; no established toxin, occupational, or lifestyle risk factor is specific to FTDALS2.
- **Protective factors:** No validated genetic or environmental protective factors are established for FTDALS2. (Not available.)
- **Gene–environment interactions:** Not characterized for FTDALS2 specifically. Oxidative stress exacerbates the mtDNA-repair defect in mutant cells, suggesting an inferred (not demonstrated) sensitization to oxidative-stress environments [PMID: 26666268].

### 3. Phenotypes

| Phenotype | Type | Onset / severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Motor neuron disease (upper + lower) / ALS | Clinical sign | Adult/late-onset; progressive | Core, in founding family | HP:0007354 (ALS); HP:0002355; HP:0007289 |
| Frontotemporal-dementia–like cognitive decline | Behavioral/cognitive | Late-onset; progressive | Core | HP:0002145 (Frontotemporal dementia); HP:0100543 |
| Cerebellar ataxia | Clinical sign | Late-onset; progressive | Present in founding family | HP:0001251 (Ataxia); HP:0002070 |
| Mitochondrial myopathy (ragged-red, COX-negative fibres) | Lab/histopathology | Adult; progressive | Core in FTDALS2 | HP:0003198 (Myopathy); HP:0003200; HP:0008314 |
| Respiratory chain deficiency / abnormal complex V assembly | Laboratory abnormality | — | Core | HP:0011922; HP:0003287 |
| Multiple mtDNA deletions in muscle | Laboratory abnormality | — | Core (S59L) | HP:0003689 (Multiple mitochondrial DNA deletions) |
| Cardiomyopathy | Clinical sign | Variable | Spectrum-dependent | HP:0001638 |
| Peripheral neuropathy (CMT2-like) | Clinical sign | Spectrum-dependent | Allele-dependent | HP:0009830 |

Evidence: *"late-onset phenotype including motor neuron disease, cognitive decline resembling frontotemporal dementia, cerebellar ataxia and myopathy"* and *"ragged-red and cytochrome c oxidase-negative fibres with combined respiratory chain deficiency and abnormal assembly of complex V"* [PMID: 24934289]. Severity is genotype-driven; SMAJ (p.G66V) is a mild lower motor neuron syndrome with normal life expectancy and no mtDNA instability [PMID: 30092269; PMID: 25428574].

**Quality of life:** Per-phenotype QOL instruments specific to FTDALS2 are not available; by extension from ALS/FTD, motor neuron degeneration and cognitive/behavioral decline cause severe progressive loss of daily functioning, with respiratory failure as the terminal event [PMID: 42113599].

### 4. Genetic / Molecular Information

- **Causal gene:** *CHCHD10* (HGNC:15559; OMIM *615903), chr22q11.23. Small (~14 kDa) mitochondrial intermembrane-space protein with a CHCH domain; intrinsically disordered/low-complexity; heterodimerizes with CHCHD2 [PMID: 35791387; PMID: 36158221].
- **Pathogenic variants (representative):**

| Variant | cDNA | Class | Phenotype | gnomAD AF | Significance |
|---|---|---|---|---|---|
| p.Ser59Leu | c.176C>T | Missense | FTD-ALS (FTDALS2), severe | 6.9×10⁻⁷ | Pathogenic |
| p.Arg15Leu | — | Missense | Familial ALS/FTD-ALS | 0 | Pathogenic |
| p.Gly66Val | c.197G>T | Missense | SMAJ (mild LMN) | 2.1×10⁻⁶ | Pathogenic (Finnish founder) |
| p.Gly58Arg | — | Missense | Isolated mitochondrial myopathy | — | Pathogenic |
| p.Ala35Asp | — | Missense | ALS spectrum | 6.1×10⁻⁶ | Likely pathogenic (rare) |
| p.Pro34Ser | c.100C>T | Missense | (historically ALS) | 0.0043 | **Benign polymorphism (BA1/BS1)** |

- **Variant type/class:** Predominantly **missense** (dominant). The gene is intolerant to true loss-of-function, but the pathogenic mechanism is dominant missense (Finding 6).
- **Functional consequence:** **Gain-of-function** via toxic protein misfolding, with dominant-negative activity in mammalian systems [PMID: 37021679; PMID: 28585542].
- **Origin:** Germline (autosomal dominant). No somatic/tumor role.
- **Modifier genes:** The paralog *CHCHD2* modifies mitochondrial function; combined CHCHD2/CHCHD10 loss phenocopies patient mutations, implicating the heterodimer as a functional unit [PMID: 32338760; PMID: 30496485]. OMA1 and OPA1 are functional effectors/modifiers of the cristae phenotype [PMID: 32338760].
- **Epigenetics / chromosomal abnormalities:** No disease-specific DNA-methylation, histone, or chromosomal (aneuploidy/translocation) findings are established for FTDALS2. mtDNA instability (multiple deletions) is the key acquired genomic lesion [PMID: 24934289].

### 5. Environmental Information

No specific environmental toxin, radiation, pollutant, occupational exposure, lifestyle factor, or infectious agent has been established as a cause or trigger of FTDALS2. The disorder is monogenic. Oxidative stress worsens the intrinsic mtDNA-repair defect in mutant cells, an inferred sensitizer rather than a primary environmental cause [PMID: 26666268].

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous dominant missense mutation in *CHCHD10* (e.g., p.Ser59Leu, p.Arg15Leu) **leads to** production of a misfolding-prone, aggregation-prone mutant protein in the mitochondrial intermembrane space [PMID: 37021679].
2. Mutant CHCHD10 **results in** disassembly of the MICOS complex (MIC60/mitofilin, CHCHD3, CHCHD6) **and thereby** loss of cristae junctions and collapse/dilatation of cristae [PMID: 26666268].
3. MICOS/cristae disruption **leads to** nucleoid disorganization and impaired repair of the mitochondrial genome after oxidative stress, **which causes** accumulation of deleted mtDNA in muscle (mtDNA instability) [PMID: 26666268; PMID: 24934289].
4. In parallel (branch), mutant CHCHD10 (with loss of the CHCHD2/CHCHD10 functional unit) **activates** the stress peptidase OMA1, **which cleaves** long-form OPA1 (L-OPA1), **further disrupting** cristae architecture [PMID: 32338760].
5. These stresses **induce** the mitochondrial integrated stress response (mtISR) in affected tissues **and result in** respiratory-chain deficiency and abnormal complex V assembly [PMID: 30877432; PMID: 32338760; PMID: 24934289].
6. Mitochondrial damage **impairs** KIF5B-mediated mitochondrial axonal transport (with syntaphilin dysregulation), **contributing to** synaptic/neuromuscular-junction failure [PMID: 39478664; PMID: 28585542].
7. Mitochondrial/synaptic damage **drives** cytoplasmic accumulation and aggregation of TDP-43 (co-aggregating with insoluble CHCHD10) — the shared pathological endpoint of ALS/FTLD-TDP [PMID: 28585542; PMID: 35787294]. *(The precise CHCHD10→TDP-43 link is partly inferred.)*
8. Progressive degeneration proceeds from muscle mitochondrial defect → NMJ degeneration → motor neuron death (demonstrated staging in knock-in mice), together with frontotemporal and cerebellar neuronal loss, **producing** the clinical phenotype of ALS, FTD-like decline, ataxia, and myopathy [PMID: 30874923; PMID: 24934289].

**Branch note:** Severity scales with the degree of MICOS disruption/mitochondrial damage rather than with TDP-43 mitochondrial localization [PMID: 30092269]; mild alleles (SMAJ/p.G66V) cause metabolic/creatine-buffering dysregulation without frank mitochondrial myopathy or mtDNA instability [PMID: 40400037; PMID: 30092269].

- **Molecular pathways / cellular processes:** Cristae/MICOS organization; mitochondrial fusion (OPA1) and quality control (OMA1); integrated stress response; apoptosis regulation (mutant fibroblasts inhibit cytochrome c release) [PMID: 26666268]; mitophagy (enhanced in S59L cardiomyopathy) [PMID: 38583639]; mitochondrial axonal transport [PMID: 39478664].
- **Protein dysfunction:** Misfolding/aggregation of an intrinsically disordered protein; dominant-negative disruption of the CHCHD2/CHCHD10 heterodimer [PMID: 35791387; PMID: 37021679].
- **Metabolic changes:** Dysregulated energy metabolism, altered redox balance, and creatine-based energy buffering [PMID: 40400037].
- **Suggested GO / CL terms:** GO:0042407 (cristae formation); GO:0007007 (inner mitochondrial membrane organization); GO:0140053 (mitochondrial gene expression); GO:0006915 (apoptotic process); GO:0034976 (response to endoplasmic-reticulum/mitochondrial stress) / integrated stress response; GO:0047497 (mitochondrion transport along microtubule). Cell types: CL:0000100 (motor neuron), CL:0000540 (neuron), CL:0000188 (skeletal muscle cell).

### 7. Anatomical Structures Affected

- **Organ level (primary):** Central and peripheral nervous system — motor cortex, brainstem/spinal motor neurons (UBERON:0001017 CNS; UBERON:0001021 nerve), frontotemporal cerebral cortex (UBERON:0016525 frontal lobe / UBERON:0001871 temporal lobe), cerebellum (UBERON:0002037). Skeletal muscle (UBERON:0001134). Secondary: heart/myocardium in cardiomyopathy-prominent spectrum members (UBERON:0002349) [PMID: 24934289; PMID: 38583639].
- **Body systems:** Nervous (central + peripheral, motor), musculoskeletal, and cardiovascular (spectrum-dependent).
- **Tissue / cell level:** Nervous tissue (upper and lower motor neurons; frontotemporal cortical neurons; cerebellar neurons) and striated skeletal muscle fibres (ragged-red, COX-negative). Cell Ontology: CL:0000100 (motor neuron), CL:0000188 (skeletal muscle cell), CL:0000540 (neuron). The neuromuscular junction is an early failure site [PMID: 30874923].
- **Subcellular level:** Mitochondrion — inner mitochondrial membrane, cristae/cristae junctions, intermembrane space, and nucleoids. GO cellular component: GO:0005743 (inner mitochondrial membrane), GO:0044284 (mitochondrial crista junction), GO:0005758 (mitochondrial intermembrane space), GO:0042645 (mitochondrial nucleoid), GO:0061617 (MICOS complex).
- **Localization / lateralization:** Typically bilateral; may begin focally/asymmetrically as in ALS generally; brain involvement predominantly frontotemporal + cerebellar.

### 8. Temporal Development

- **Onset:** Adult / late-onset; insidious and chronic. The founding family showed a *"late-onset phenotype"* [PMID: 24934289]. SMAJ presents in mid-adulthood.
- **Progression:** Progressive and neurodegenerative. Rate is genotype-dependent — severe/rapid for FTD-ALS (p.Ser59Leu) versus slow with normal life expectancy for SMAJ (p.G66V) [PMID: 30092269; PMID: 40400037]. Staging (from models): muscle mitochondrial defect → NMJ degeneration → motor neuron death [PMID: 30874923].
- **Disease course:** Chronic, lifelong, progressive; no relapsing-remitting pattern and no spontaneous remission. Duration ranges from a few years (ALS-like) to decades (SMAJ). Critical intervention windows are inferred to be early (pre-NMJ-degeneration), supported by the muscle-first staging in knock-in mice [PMID: 30874923].

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant [PMID: 24934289; PMID: 25428574].
- **Penetrance / expressivity:** Age-dependent penetrance with variable expressivity; strong allele-specific genotype–phenotype correlation (Finding 7) [PMID: 37021679]. Variant **dosage** modulates severity — the first reported homozygous CHCHD10 (SMAJ) patient had more severe disease, indicating a dose effect [PMID: 40400037].
- **Epidemiology:** FTDALS2 is very rare. CHCHD10 mutations account for ~0.4% of ALS cohorts (2/487 sporadic Chinese ALS) and are a minor contributor to familial ALS/FTD [PMID: 27056076; PMID: 28318595]. Precise prevalence/incidence figures for FTDALS2 are not established (ultra-rare); by comparison, ALS overall affects ~25,000 individuals in the US [PMID: 42113599].
- **Founder effects:** p.Gly66Val (SMAJ) is a Finnish founder allele (gnomAD AF 2.1×10⁻⁶) [PMID: 25428574; Finding 6].
- **Population / demographics:** Reported across European (French founding family; Finnish SMAJ) and Asian (Chinese) cohorts. No strong sex bias specific to FTDALS2 is established. Carrier frequency is extremely low given ultra-rare pathogenic allele frequencies (Finding 6).
- **Genetic anticipation / germline mosaicism / consanguinity:** Not features of this dominant missense disorder (not a repeat-expansion disease; not recessive).

### 10. Diagnostics

- **Clinical / electrophysiology:** EMG and nerve conduction studies to document lower motor neuron involvement (ALS pattern); clinical exam for upper motor neuron signs, cognitive/behavioral (FTD) assessment, and cerebellar signs [PMID: 24934289; PMID: 42113599].
- **Muscle biopsy / histopathology (characteristic):** Ragged-red fibres and COX-negative fibres with combined respiratory-chain deficiency and abnormal complex V assembly — a hallmark distinguishing FTDALS2 from most other ALS/FTD [PMID: 24934289].
- **Laboratory / molecular:** Detection of **multiple mtDNA deletions** in skeletal muscle (mtDNA instability) [PMID: 24934289]; respiratory chain enzymology; metabolomic evidence of altered energy/redox/creatine metabolism (research-stage biomarker) [PMID: 40400037].
- **Imaging:** MRI showing frontotemporal ± cerebellar atrophy (extrapolated from phenotype); no CHCHD10-specific imaging signature established.
- **Genetic testing (definitive):** Single-gene *CHCHD10* sequencing, ALS/FTD gene panels, WES, or WGS. **Variant interpretation is critical** — classify per ACMG/AMP, treating ultra-rare missense (S59L, R15L, G66V) as pathogenic and common variants like p.Pro34Ser (gnomAD AF ~0.4%) as benign (BA1/BS1) (Finding 6) [PMID: 28318595]. Repeat-expansion, karyotype, CMA, FISH, and mtDNA-primary testing are not the diagnostic route (the mtDNA deletions here are secondary to the nuclear CHCHD10 defect).
- **Differential diagnosis:** Other genetic ALS/FTD (C9orf72, SOD1, TARDBP, FUS), primary mitochondrial myopathies with mtDNA-maintenance defects (POLG, TWNK), and SMA. Distinguishing feature: combination of MND/FTD with mitochondrial myopathy + mtDNA instability points to CHCHD10.

### 11. Outcome / Prognosis

- **Survival / mortality:** Highly genotype-dependent. Severe FTD-ALS (p.Ser59Leu) carries an ALS-like poor prognosis (progressive to respiratory failure), whereas SMAJ (p.G66V) has a normal life expectancy [PMID: 30092269; PMID: 40400037]. FTDALS2-specific survival curves are not established; general ALS survival is ~3–5 years from diagnosis [PMID: 42113599].
- **Morbidity / function:** Progressive motor disability, cognitive/behavioral decline, and myopathy with high burden on daily functioning; respiratory failure is the usual terminal event in ALS-predominant cases.
- **Prognostic factors:** Genotype (specific allele and dosage) is the dominant prognostic factor; degree of MICOS disruption/mitochondrial damage tracks severity [PMID: 30092269; PMID: 40400037]. Metabolic/creatine dysregulation is a candidate prognostic biomarker [PMID: 40400037].
- **Recovery:** None; the disease is progressive and neurodegenerative.

### 12. Treatment

- **Disease-specific therapy:** **None approved.** Management follows ALS/FTD symptomatic standards [PMID: 42113599; PMID: 42666355].
- **Pharmacotherapy (symptomatic, ALS-standard; NCIT terms):** Riluzole (NCIT:C1215; glutamate-release inhibitor; modest ~2–4 month benefit); Edaravone (NCIT:C65358; free-radical scavenger; narrow eligibility). Tofersen is SOD1-specific and **not** applicable to CHCHD10 disease [PMID: 42113599].
- **Supportive / rehabilitative:** Multidisciplinary care (neurology, respiratory support/NIV, nutrition/PEG, physical/occupational/speech therapy) improves survival (~4–7 months) and QOL [PMID: 42113599].
- **Experimental / precision (research-stage):**
  - **Nifuroxazide** — repurposed compound rescuing cristae/network abnormalities in S59L patient fibroblasts and reducing caspase-dependent death of S59L iPSC motor neurons via KIF5B-mediated mitochondrial transport enhancement and syntaphilin degradation [PMID: 39478664].
  - **Elamipretide/MTP-131** — mitochondria-targeted peptide that enhanced MICOS/OXPHOS in CHCHD2-mutant NPCs (paralog data; candidate for CHCHD10) [PMID: 30496485].
  - **Integrated-stress-response** modulation and **metabolic/creatine** support (rationale from mtISR activation and creatine-buffering dysregulation) [PMID: 32338760; PMID: 40400037].
  - Broader ALS trials (e.g., trehalose/autophagy in the HEALEY platform) have been negative, underscoring difficulty [PMID: 40409314].
- **Pharmacogenomics / gene / cell / RNA therapy:** No CHCHD10-directed ASO/gene therapy is approved; these are conceptual future directions.

### 13. Prevention

- **Primary prevention:** Not applicable for a monogenic dominant disorder beyond reproductive options. No vaccine or modifiable risk-factor program exists.
- **Genetic counseling / reproductive prevention:** Autosomal dominant inheritance implies 50% transmission risk; cascade testing of at-risk relatives, prenatal diagnosis, and preimplantation genetic testing are options once a pathogenic variant is confirmed. Accurate variant classification is essential to avoid counseling on benign variants (e.g., p.Pro34Ser) (Finding 6).
- **Secondary/tertiary prevention:** No proven presymptomatic disease-modifying intervention; tertiary prevention focuses on complication management (respiratory, nutrition, falls) within ALS/FTD care standards [PMID: 42113599].

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *CHCHD10* is conserved in mammals; mouse ortholog *Chchd10* (the human-equivalent S59L is modeled as mouse S55L) [PMID: 30877432; PMID: 38583639]. The paralog pair CHCHD2/CHCHD10 arose by gene duplication during evolution [PMID: 36158221].
- **Natural disease in other species:** No well-documented naturally occurring CHCHD10 disease in companion animals or wildlife is established (not available in OMIA at time of review). Disease knowledge derives from engineered models.
- **Comparative biology:** The MICOS/cristae machinery and CHCHD10 function are evolutionarily conserved (yeast MICOS mutants recapitulate cristae defects), supporting cross-species mechanistic conservation [PMID: 39478664].
- **Zoonotic potential:** None (non-infectious genetic disease).

### 15. Model Organisms

| Model | Type | Key features / recapitulation | Reference |
|---|---|---|---|
| S59L / S55L knock-in mouse | Mammalian, knock-in | Tissue-specific toxic gain-of-function; mtISR; fatal mitochondrial cardiomyopathy with enhanced mitophagy; muscle defect precedes NMJ/motor-neuron loss | [PMID: 30877432; PMID: 38583639; PMID: 30874923] |
| C2/C10 double-knockout mouse | Mammalian, KO | OMA1-mediated L-OPA1 cleavage; cristae disruption; cardiomyopathy; mtISR; phenocopies KI mutants | [PMID: 32338760] |
| G66V knock-in mouse / patient cells | Mammalian + iPSC | Dose-dependent severity; energy/redox/creatine dysregulation | [PMID: 40400037] |
| Patient iPSC-derived motor neurons (S59L, G66V) | In vitro (human) | Caspase-dependent death; mitochondrial transport defects; therapy testbed (nifuroxazide) | [PMID: 39478664; PMID: 40400037] |
| Patient fibroblasts | In vitro (human) | Network fragmentation, cristae abnormalities, impaired mtDNA repair, apoptosis inhibition | [PMID: 26666268; PMID: 39478664] |
| *C. elegans* | Invertebrate | Genetic complementation showing LoF-in-complementation + dominant-negative activity; synaptic/TDP-43 phenotypes | [PMID: 28585542] |
| Yeast MICOS mutants | Cellular | MICOS/cristae biology; repurposing screen platform | [PMID: 39478664] |
| CHCHD2-mutant hESC/NPC (paralog) | In vitro (human) | MICOS/cristae defects; Elamipretide rescue | [PMID: 30496485] |

**Model limitations:** Mouse KI models show prominent cardiomyopathy that may exceed the human cardiac phenotype; full FTD-like cognitive/behavioral features and the complete ALS motor-neuron degeneration timeline are incompletely captured; TDP-43 pathology recapitulation is partial and its causal link remains under study [PMID: 35787294; PMID: 30877432].

---

## Mechanistic Model / Interpretation

```
CHCHD10 dominant missense mutation (S59L, R15L, G66V, G58R ...)
        │  (toxic gain-of-function; protein misfolding/aggregation)
        ▼
Disassembly of MICOS complex (MIC60/CHCHD3/CHCHD6) ──► cristae junction loss / cristae collapse
        │                                                        │
        ▼                                                        ▼
Nucleoid disorganization; impaired mtDNA repair            OMA1 activation ──► L-OPA1 cleavage
        │                                                        │
        ▼                                                        ▼
Multiple mtDNA deletions (muscle) ◄──────────── Respiratory chain deficiency; complex V defect
        │                                                        │
        └──────────────► Mitochondrial Integrated Stress Response (mtISR) ◄─────────┘
                                     │
                 ┌───────────────────┼─────────────────────────┐
                 ▼                   ▼                          ▼
  Impaired KIF5B mito-transport   Metabolic/redox/creatine   Cytoplasmic TDP-43
  (syntaphilin dysregulation)     dysregulation              accumulation/aggregation
                 │                   │                          │  (partly inferred)
                 └───────────────────┴─────────────┬────────────┘
                                                    ▼
              Muscle mito defect → NMJ degeneration → motor neuron death
              + frontotemporal & cerebellar neuronal loss
                                                    ▼
        Clinical FTDALS2: ALS + FTD-like decline + ataxia + mitochondrial myopathy
        (severity ∝ degree of MICOS disruption; allele- and dosage-dependent)
```

The disorder is unified by a single upstream lesion — a misfolding dominant CHCHD10 mutant — that corrupts inner-membrane architecture. The **upstream** events (MICOS disassembly, cristae collapse) are the most severity-determining; **downstream** events (mtISR, transport failure, TDP-43 pathology, neuronal death) produce the clinical picture and connect FTDALS2 to the wider ALS/FTLD-TDP family. The allele determines where on the severity spectrum a patient falls, from mild SMAJ (metabolic dysregulation without frank myopathy) to severe FTD-ALS with mtDNA instability.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the report |
|---|---|---|
| [24934289](https://pubmed.ncbi.nlm.nih.gov/24934289/) | *A mitochondrial origin for FTD/ALS through CHCHD10* | Founding family; multisystem phenotype, ragged-red/COX-neg fibres, mtDNA instability |
| [26666268](https://pubmed.ncbi.nlm.nih.gov/26666268/) | *CHCHD10 mutations promote loss of cristae junctions* | MICOS disassembly, cristae/nucleoid loss, impaired mtDNA repair, apoptosis inhibition |
| [32338760](https://pubmed.ncbi.nlm.nih.gov/32338760/) | *Loss of CHCHD2/CHCHD10 activates OMA1* | OMA1→L-OPA1 cleavage mechanism; mtISR; cardiomyopathy |
| [30877432](https://pubmed.ncbi.nlm.nih.gov/30877432/) | *ALS/FTD mutant CHCHD10 mice: toxic GoF* | Knock-in S55L mouse; tissue-specific toxic gain-of-function + stress response |
| [28585542](https://pubmed.ncbi.nlm.nih.gov/28585542/) | *LoF CHCHD10 mutations, TDP-43, synapses* | Dominant-negative activity; cytoplasmic TDP-43 accumulation |
| [30092269](https://pubmed.ncbi.nlm.nih.gov/30092269/) | *MICOS integrity and severity* | Severity ∝ MICOS disruption; SMAJ lacks myopathy/mtDNA instability |
| [30874923](https://pubmed.ncbi.nlm.nih.gov/30874923/) | *Muscle defect precedes NMJ/motor neuron loss* | Pathology staging; confirms S59L founding mutation |
| [25428574](https://pubmed.ncbi.nlm.nih.gov/25428574/) | *LOSMoN/SMAJ caused by CHCHD10* | p.G66V mild allele; AD inheritance; spectrum breadth |
| [37021679](https://pubmed.ncbi.nlm.nih.gov/37021679/) | *CHCHD2/CHCHD10 pathogenesis & precision therapy* | Genotype–phenotype map; gain-of-function misfolding mechanism |
| [27056076](https://pubmed.ncbi.nlm.nih.gov/27056076/) | *CHCHD10 screening in Chinese ALS* | Rarity: 0.4% mutation frequency |
| [28318595](https://pubmed.ncbi.nlm.nih.gov/28318595/) | *CHCHD10 in Mainland China ALS* | "Controversial role" — explained by benign vs pathogenic variant confusion |
| [39478664](https://pubmed.ncbi.nlm.nih.gov/39478664/) | *Nifuroxazide rescues MICOS defects* | Experimental therapy; KIF5B/syntaphilin transport mechanism |
| [40400037](https://pubmed.ncbi.nlm.nih.gov/40400037/) | *Dose-dependent CHCHD10 & creatine metabolism* | Metabolic dysregulation; dosage-dependent severity; homozygous patient |
| [35787294](https://pubmed.ncbi.nlm.nih.gov/35787294/) | *CHCHD10, TDP-43 pathology* | Insoluble CHCHD10 co-aggregates with phospho-TDP-43 in FTLD-TDP brains |
| [30496485](https://pubmed.ncbi.nlm.nih.gov/30496485/) | *PD-linked CHCHD2 impairs MICOS* | Paralog data; Elamipretide rescue; heterodimer biology |
| [36158221](https://pubmed.ncbi.nlm.nih.gov/36158221/) | *CHCHD2 vs CHCHD10* | Heterodimerization; evolutionary duplication |
| [35791387](https://pubmed.ncbi.nlm.nih.gov/35791387/) | *IDPs in neurodegeneration* | CHCHD10 intrinsically disordered; drug-target implications |
| [42113599](https://pubmed.ncbi.nlm.nih.gov/42113599/) | *ALS: A Review* | Standard-of-care therapies; survival; multidisciplinary benefit |
| [42666355](https://pubmed.ncbi.nlm.nih.gov/42666355/) | *Therapeutic challenges in ALS* | Precision-medicine landscape; trial-design context |
| [40409314](https://pubmed.ncbi.nlm.nih.gov/40409314/) | *Trehalose HEALEY trial* | Negative ALS trial; illustrates therapeutic difficulty |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** No robust prevalence/incidence, sex-ratio, or survival statistics exist specifically for FTDALS2; figures are extrapolated from ALS/FTD generally.
2. **CHCHD10→TDP-43 causal link is partly inferred.** How mitochondrial dysfunction produces cytoplasmic TDP-43 aggregation is correlative in human tissue and not fully resolved mechanistically [PMID: 35787294].
3. **Variant interpretation remains a pitfall.** The historical inclusion of benign polymorphisms (p.Pro34Ser) inflated apparent pathogenicity; some rarer variants remain VUS. Systematic functional classification is incomplete.
4. **Model–human mismatch.** Mouse KI cardiomyopathy may not mirror the human cardiac burden, and cognitive/behavioral FTD features are under-modeled.
5. **No disease-modifying therapy validated in humans.** All CHCHD10-specific interventions (nifuroxazide, elamipretide, mtISR/metabolic strategies) are preclinical.
6. **Epigenetic and gene–environment contributions are essentially uncharacterized.**

---

## Proposed Follow-up Experiments / Actions

1. **Curate a CHCHD10 variant registry** integrating gnomAD frequencies, ACMG classification, and phenotype to formally resolve VUS and retire benign misattributions (extends Finding 6).
2. **Functional high-throughput assays** (MICOS integrity, cristae morphology, OMA1/OPA1 cleavage, mtISR readouts) to classify each reported variant along the severity gradient.
3. **Test nifuroxazide and elamipretide head-to-head** in isogenic S59L/G66V iPSC motor neurons and knock-in mice, with mitochondrial-transport and cristae endpoints [PMID: 39478664; PMID: 30496485].
4. **Develop fluid biomarkers** from the metabolic signature (creatine/energy/redox metabolites) for diagnosis and trial stratification [PMID: 40400037].
5. **Mechanistic dissection of the CHCHD10→TDP-43 axis** using proximity-labeling and conditional models to establish causality versus correlation [PMID: 35787294; PMID: 28585542].
6. **Natural-history / registry study** across the CHCHD10 spectrum to define genotype-specific progression and survival, enabling genotype-stratified trial design.
7. **Explore ASO/gene-silencing approaches** targeting the mutant allele, leveraging the dominant gain-of-function/dosage-dependent mechanism [PMID: 40400037].

---

*Evidence source types are noted throughout: human clinical (family/cohort studies, autopsy), model organism (knock-in/KO mice, C. elegans, yeast), in vitro (patient fibroblasts, iPSC-derived motor neurons, hESC/NPC), and computational/population-genetic (gnomAD variant frequency analysis).*


## Artifacts

- [OpenScientist final report](Frontotemporal_Dementia_And_Or_Amyotrophic_Lateral_Sclerosis_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Frontotemporal_Dementia_And_Or_Amyotrophic_Lateral_Sclerosis_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001638` (1 mention) - the report calls it "Spectrum-dependent"; HP calls it **Cardiomyopathy**
- `HP:0009830` (1 mention) - the report calls it "Allele-dependent"; HP calls it **Peripheral neuropathy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034976` (1 mention) - the report calls it "response to endoplasmic-reticulum/mitochondrial stress"; GO calls it **response to endoplasmic reticulum stress**
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names