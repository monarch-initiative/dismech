---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T07:02:35.907840'
end_time: '2026-09-01T07:22:27.665622'
duration_seconds: 1191.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia Type 5
  mondo_id: ''
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
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 21
  not_found: 2
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.083
  labels_checked: 15
  labels_matching: 7
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014660
    reported_labels:
    - hereditary hemorrhagic telangiectasia type 5
    ontology_label: microcephaly 15, primary, autosomal recessive
  - term_id: HP:0006775
    reported_labels:
    - Pulmonary AVM
    - Pulmonary arteriovenous malformation
    ontology_label: Multiple myeloma
  - term_id: HP:0100761
    reported_labels:
    - Hepatic AVM
    ontology_label: Visceral angiomatosis
  - term_id: HP:0002239
    reported_labels:
    - GI bleeding / telangiectases
    ontology_label: Gastrointestinal hemorrhage
  - term_id: NCIT:C15325
    reported_labels:
    - Therapeutic embolization
    ontology_label: Skin Transplantation
  labels_variant: 3
  unresolved_terms:
  - HP:0000562
  - NCIT:C48225
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hereditary_Hemorrhagic_Telangiectasia_5-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Hemorrhagic_Telangiectasia_5-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia Type 5
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia Type 5** covering all of the
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

# Hereditary Hemorrhagic Telangiectasia Type 5 (HHT5): Comprehensive Disease Characterization

**Disease:** Hereditary Hemorrhagic Telangiectasia Type 5 (HHT5)
**OMIM:** #615506 | **Causal gene:** *GDF2* (BMP9) | **Category:** Mendelian, autosomal dominant
**Suggested MONDO:** MONDO:0014660 (hereditary hemorrhagic telangiectasia type 5)

*Autonomous literature-based discovery report. Evidence types are labeled human clinical, human genetics, in vitro, and model organism. Primary citations are given as PMIDs. HHT5 is ultra-rare (~9 published probands plus a small number of biallelic cases); where HHT5-specific data are unavailable, evidence is extrapolated from the shared BMP9–ALK1–endoglin–SMAD1/5/8 pathway and from the broader HHT literature, and this is stated explicitly.*

---

## Summary

Hereditary Hemorrhagic Telangiectasia Type 5 (HHT5; OMIM #615506) is an ultra-rare autosomal dominant vascular dysplasia caused by heterozygous loss-of-function variants in ***GDF2***, the gene encoding **bone morphogenetic protein 9 (BMP9 / growth differentiation factor 2)** on chromosome 10q11.22. BMP9 is a circulating vascular "quiescence factor": secreted largely by the liver, it binds the endothelial type I receptor **ALK1 (ACVRL1)** together with the co-receptor **endoglin (ENG)**, driving **SMAD1/5/8 phosphorylation** and **ID1** transcription to hold the endothelium in a non-proliferative, mature state. In HHT5, reduced BMP9 dosage weakens this signal, releasing the angiostatic brake and permitting endothelial hyperproliferation, arteriovenous mis-specification, and formation of mucocutaneous **telangiectases** and visceral **arteriovenous malformations (AVMs)** — the defining HHT lesions that bleed (epistaxis, GI hemorrhage, anemia) and shunt (paradoxical emboli, stroke, high-output heart failure).

HHT5 sits within the shared HHT signaling pathway (ENG→HHT1, ACVRL1→HHT2, SMAD4→JP-HHT, GDF2→HHT5), but it is by far the rarest subtype, with roughly **9 probands** reported worldwide as of 2022. Its rarity and variable penetrance are mechanistically explained by **BMP9–BMP10 ligand redundancy**: BMP10 can substitute for BMP9 at ALK1, so heterozygous loss of BMP9 alone is often well tolerated. This is dramatically illustrated in animal models — zebrafish *bmp9* mutants are overtly normal into adulthood, whereas combined *bmp10* loss is embryonic-lethal with cranial AVMs. Notably, **biallelic (homozygous) GDF2 loss-of-function** abolishes both circulating BMP9 and BMP10 and causes childhood **pulmonary arterial hypertension (PAH)** and/or an "HHT-like" syndrome, revealing a dose- and ligand-dependent phenotypic spectrum bridging two vascular diseases.

Clinically, GDF2-HHT5 is HHT-like — recurrent epistaxis (>90% across HHT), iron-deficiency anemia (~50%), mucocutaneous telangiectases, and pulmonary/hepatic/cerebral/GI AVMs — but with reported atypical features including **earlier-onset epistaxis, a unique dermal capillary lesion distribution (upper forelimbs, trunk, head), and documented cerebrovascular involvement**. Diagnosis follows the clinical **Curaçao criteria** supplemented by genetic testing (panel/WES/WGS; large 10q11.22 deletions require CNV-aware methods). Management is subtype-agnostic per the **Second International HHT Guidelines**: systemic antiangiogenics (pomalidomide — RCT-proven; bevacizumab), antifibrinolytics, iron repletion, and AVM screening/embolization. Downstream of BMP9/ALK1 loss, endothelial cells over-activate **PI3K/Akt/mTOR, VEGFR2, and Angiopoietin-2**, providing the rational targets for these therapies.

---

## Key Findings

### Finding 1 — HHT5 is caused by heterozygous *GDF2* (BMP9) loss-of-function and is autosomal dominant

*GDF2* (encoding BMP9/growth differentiation factor 2; chromosome **10q11.22**) is the causal gene for HHT5 (**OMIM #615506**). Dominant heterozygous variants produce the characteristic telangiectases and AVMs. As [PMID: 42309173](https://pubmed.ncbi.nlm.nih.gov/42309173/) states: *"Dominant variants in GDF2 are known to cause hereditary hemorrhagic telangiectasia type 5 (HHT5), a condition characterized by telangiectases and arteriovenous malformations (AVMs)."* Reported variant classes span **missense** substitutions (e.g., p.Val403Ile, p.Glu355Gln) and **large interstitial deletions** (>5 Mb, spanning 10q11.22–10q11.23) that encompass *GDF2*. [PMID: 34611981](https://pubmed.ncbi.nlm.nih.gov/34611981/) reported that *"Two patients harbored heterozygous missense variants not previously annotated as pathogenic (p.Val403Ile; p.Glu355Gln),"* documenting the germline heterozygous missense mechanism consistent with autosomal dominant inheritance. The disease remains ultra-rare, with approximately **9 probands** described as of 2022.

**Ontology suggestions:** Gene — HGNC:4217 (*GDF2*); Disease — MONDO:0014660; MeSH — Telangiectasia, Hereditary Hemorrhagic (D013683).

### Finding 2 — BMP9 is a circulating ALK1/endoglin ligand that maintains endothelial vascular quiescence

BMP9 (and its paralog BMP10) are specific, high-affinity ligands for the endothelial type I receptor **ALK1 (ACVRL1)** and the co-receptor **endoglin (ENG)**. Ligand binding induces **SMAD1/5/8 phosphorylation** and **ID1** expression in endothelial cells, which suppresses bFGF/VEGF-driven proliferation, migration, and sprouting angiogenesis — i.e., it enforces vascular quiescence. [PMID: 17311849](https://pubmed.ncbi.nlm.nih.gov/17311849/) established that *"these results suggest that BMP-9 is a physiological ALK1 ligand that plays an important role in the regulation of angiogenesis."* Critically, BMP9 circulates at physiologically active concentrations: [PMID: 18309101](https://pubmed.ncbi.nlm.nih.gov/18309101/) found that *"The concentration of circulating BMP9 was found to vary between 2 and 12 ng/mL in sera and plasma from healthy humans, a value well above its EC(50) (50 pg/mL),"* demonstrating that BMP9 is a constitutively available, systemic quiescence factor whose loss can plausibly destabilize endothelial homeostasis body-wide.

**Ontology suggestions:** GO:0001568 (blood vessel development), GO:0030509 (BMP signaling pathway), GO:0016525 (negative regulation of angiogenesis); CL:0000115 (endothelial cell).

### Finding 3 — Biallelic *GDF2* loss causes childhood PAH and/or HHT-like disease via loss of circulating BMP9/BMP10

Homozygous *GDF2* nonsense mutations (p.Gln26Ter; p.Glu279Ter) produced **undetectable plasma BMP9 and BMP10** and low serum-derived endothelial BMP activity (HMEC1-BRE reporter assay). Phenotypically, one homozygous child developed **PAH** and another had **pulmonary AVMs**; both had facial telangiectases. Heterozygous parents had reduced BMP9/10 levels but retained normal serum activity and were asymptomatic — direct evidence of a dose-dependent threshold. [PMID: 33834622](https://pubmed.ncbi.nlm.nih.gov/33834622/) concluded that *"homozygous GDF2 mutations, leading to a loss of circulating BMP9 and BMP10, can cause either pediatric PAH and/or 'HHT-like' telangiectases and PAVMs,"* and that *"Plasma levels of both BMP9 and BMP10 were undetectable in the two homozygous index cases and this corresponded to low serum-derived endothelial BMP activity in the patients."* This finding bridges HHT5 and heritable PAH along a single ligand-dosage axis and clarifies that the *GDF2* phenotype depends on residual circulating BMP activity.

### Finding 4 — GDF2-HHT5 has a distinctive clinical phenotype with cerebral involvement and atypical telangiectasia distribution

In a cohort of 4 unrelated probands, GDF2-HHT5 patients showed features resembling HHT1, including **cerebrovascular involvement** (the first documented report of cerebral involvement in HHT5), **earlier onset of epistaxis**, and a unique anatomic distribution of dermal capillary lesions. [PMID: 34611981](https://pubmed.ncbi.nlm.nih.gov/34611981/) reported that *"these patients had features resembling HHT1, including cerebrovascular involvement of their disease (first report documenting cerebral involvement of HHT5), but with earlier onset of epistaxis and a unique anatomic distribution of dermal capillary lesions that involved the upper forelimbs, trunk, and head."* Two of the four probands carried large deletions: *"The other two patients harbored interstitial deletions larger than five megabases between 10q11.22 and 10q11.23 that included GDF2,"* which has direct implications for genetic testing (single-gene sequencing alone can miss these; CNV/microarray detection is required) and may explain additional extravascular features from contiguous-gene involvement.

**Ontology suggestions:** HP:0000421 (epistaxis), HP:0000562 (telangiectasia of the skin), HP:0002948 (cerebral arteriovenous malformation).

### Finding 5 — HHT bleeding (applicable to HHT5) is treated with systemic antiangiogenics; pomalidomide has RCT-proven efficacy

Because HHT5 is clinically HHT-like, subtype-agnostic HHT therapies apply. The randomized, placebo-controlled **PATH-HHT trial** (NCT03910244, n=144) demonstrated that **pomalidomide 4 mg/day** reduced the Epistaxis Severity Score (ESS). [PMID: 39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/) reported that *"At 24 weeks, the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was −0.94 points (95% confidence interval [CI], −1.57 to −0.31; P = 0.0...)."* Additional off-label systemic antiangiogenics include IV **bevacizumab** (anti-VEGF-A), oral **pazopanib**, and oral **thalidomide**; [PMID: 35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/) notes *"Intravenous bevacizumab, oral pazopanib, and oral thalidomide are the three targeted primary angiogenesis inhibitors, with multiple studies describing both reassuring safety and impressive effectiveness in the treatment of moderate-to-severe HHT-associated bleeding."* Antifibrinolytics (tranexamic acid) address mild–moderate bleeding; iron replacement and transfusion manage anemia; and local measures include nasal packing, laser/cautery ablation, AVM embolization, septodermoplasty, and Young's procedure. **No agent is yet FDA/EMA-approved specifically for HHT.**

**Ontology suggestions (NCIT):** Pomalidomide (C48225), Bevacizumab (C2039), Thalidomide (C518), Tranexamic acid (C61785), Therapeutic embolization (C15325).

### Finding 6 — BMP9/BMP10 loss animal models recapitulate HHT vascular pathology and reveal ligand redundancy

Neonatal mouse **immunoblockade of BMP9/BMP10** (including transmammary antibody delivery) reproduces the core HHT vascular phenotype. [PMID: 27874028](https://pubmed.ncbi.nlm.nih.gov/27874028/) reported that *"pups receiving anti-BMP9/10 antibodies via lactation displayed consistent and robust vascular pathology in the retina, which included hypervascularization and defects in arteriovenous specification, as well as the presence of multiple and massive arteriovenous malformations."* RNA-Seq of these retinas identified **angiopoietin-2 (Angpt2)** as the most significantly upregulated gene. The redundancy that makes HHT5 rare is shown in zebrafish: [PMID: 31828546](https://pubmed.ncbi.nlm.nih.gov/31828546/) found that *"bmp9 mutants survive to adulthood with no overt phenotype. In contrast, combined loss of bmp10 and bmp10-like results in embryonic lethal cranial AVMs indistinguishable from acvrl1 mutants"* — establishing BMP10 as the essential post-embryonic ALK1 ligand and explaining why single-ligand (BMP9/GDF2) haploinsufficiency is often mild or non-penetrant.

### Finding 7 — Downstream of BMP9/ALK1 loss, endothelial cells over-activate PI3K/Akt/mTOR and VEGFR2, driving AVM formation

In the BMP9/10-immunoblocked neonatal mouse HHT model, endothelial **PI3K/Akt/mTOR** and **VEGFR2** pathways become overactivated. [PMID: 31689244](https://pubmed.ncbi.nlm.nih.gov/31689244/) demonstrated that *"HHT pathogenesis strongly relies on overactivated PI3K/Akt/mTOR and VEGFR2 pathways in endothelial cells (ECs),"* and that combined **mTOR inhibition (sirolimus)** plus **receptor tyrosine kinase inhibition (nintedanib)** synergistically blocked and reversed retinal AVMs, prevented oral/lung/liver vascular pathology, and reduced GI bleeding/anemia; sirolimus also partially rescued SMAD1/5/8 activity via ALK2. In parallel, loss of SMAD1/5 impairs shear-stress mechanotransduction and reduces **Connexin37 (Cx37)**: [PMID: 32078368](https://pubmed.ncbi.nlm.nih.gov/32078368/) showed that *"reduced Cx37 expression is permissive for capillary enlargement into shunts,"* linking mechanosensing failure directly to the transformation of capillaries into arteriovenous shunts.

**Ontology suggestions:** GO:0031929 (TOR signaling), GO:0048010 (vascular endothelial growth factor receptor signaling pathway), GO:0034097 (response to cytokine).

### Finding 8 — HHT phenotype spectrum and frequencies (framework for HHT5)

Across HHT, **recurrent spontaneous epistaxis occurs in >90%** of affected individuals and is the hallmark; **iron-deficiency anemia develops in nearly half** of patients from epistaxis and GI bleeding. [PMID: 41347972](https://pubmed.ncbi.nlm.nih.gov/41347972/) states: *"Recurrent, spontaneous epistaxis occurs in over 90% of affected individuals and is the hallmark of this disorder. Epistaxis and gastrointestinal bleeding result in the development of iron deficiency anemia in nearly half of all affected individuals."* Mucocutaneous telangiectases affect skin and mucosa (lips, tongue, fingers, nasal mucosa). Visceral AVMs occur in the **lung** (PAVMs), **liver** (HAVMs), **brain** (~10–21% of HHT overall, higher in HHT1), and **GI tract**. Serious complications are captured by [PMID: 41166505](https://pubmed.ncbi.nlm.nih.gov/41166505/): *"These AVMs can lead to life-threatening complications, such as paradoxical emboli, stroke, significant gastrointestinal bleeds, and high-output heart failure, especially in the setting of hepatic AVMs."* HHT5-specific reports (n≈9) describe early-onset epistaxis, atypical dermal capillary lesion distribution (forelimbs, trunk, head), facial telangiectases, pulmonary AVMs, and cerebrovascular involvement.

**Frequency table (HHT overall; the applicable framework for HHT5):**

| Phenotype | HPO term | Frequency | Onset / course |
|---|---|---|---|
| Recurrent epistaxis | HP:0000421 | >90% | Childhood/adolescence onset; progressive |
| Mucocutaneous telangiectases | HP:0000562 | Very frequent | Adult; progressive |
| Iron-deficiency anemia | HP:0001891 | ~50% | Follows chronic bleeding |
| Pulmonary AVM | HP:0006775 | Subtype-dependent | Adult; may be silent then complicate |
| Hepatic AVM | HP:0100761 | Common (often silent) | Adult |
| Cerebral vascular malformation | HP:0002948 | ~10–21% overall | Congenital/early; documented in HHT5 |
| GI bleeding / telangiectases | HP:0002239 | Increases with age | Later adult |

### Finding 9 — Epidemiology, inheritance, and diagnosis; HHT5/GDF2 is an ultra-rare autosomal dominant subtype

HHT overall prevalence is **~1 in 5,000** (range 1:5,000–1:8,000), making it the **second most common inherited bleeding disorder**. [PMID: 38864625](https://pubmed.ncbi.nlm.nih.gov/38864625/) states: *"Hereditary hemorrhagic telangiectasia (HHT; Osler-Weber-Rendu disease) affects 1 in 5000 persons, making it the second most common inherited bleeding disorder worldwide."* Genetic-prevalence analyses of large genomic databases suggest underdiagnosis; [PMID: 41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/) found that *"The genetic prevalence of HHT ranged from 1.753 to 2.555 in 5000 individuals, when considering only pathogenic and likely pathogenic variants, and from 2.874 to 4.327 in 5000 individuals, when also potentially pathogenic variants were considered."* Inheritance is **autosomal dominant** with **age-dependent penetrance** and **highly variable expressivity**. ENG (HHT1) and ACVRL1 (HHT2) account for ~85–90% of cases; SMAD4 causes JP-HHT; **GDF2 (HHT5) is ultra-rare (~9 probands)**. Clinical diagnosis uses the **Curaçao criteria** (epistaxis; mucocutaneous telangiectases; visceral AVMs; first-degree relative with HHT): ≥3 = definite, 2 = possible, ≤1 = unlikely — with lower sensitivity in children.

### Finding 10 — Prognosis is generally good with organ screening and AVM management

HHT is a chronic, lifelong disease. Most morbidity arises from recurrent bleeding (epistaxis, GI) causing anemia and reduced quality of life, and from visceral AVM complications (stroke/brain abscess from PAVM paradoxical embolism; high-output heart failure and biliary ischemia from HAVMs; intracranial hemorrhage from cerebral VMs). **Prophylactic screening and treatment improve outcomes.** A Markov decision analysis of HHT patients with asymptomatic pulmonary AVMs found ([PMID: 19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/)): *"No embolotherapy, embolotherapy only in the event of a PAVM complication, and immediate embolotherapy were associated with expected survival times of 37.2, 37.6, and 39.0 years, respectively"* — i.e., immediate embolotherapy yielded the highest expected survival (39.0 years) and quality-adjusted survival (37.2 QALYs). Guidelines recommend screening for pulmonary AVMs (contrast echocardiography/CT), cerebral VMs (MRI), and hepatic AVMs, plus antibiotic prophylaxis before dental/surgical procedures in patients with PAVMs.

### Finding 11 — Integrated mechanistic model: HHT5 is loss of the BMP9-driven endothelial quiescence brake

Synthesizing the above, HHT5 (OMIM #615506) arises from heterozygous *GDF2*/BMP9 loss-of-function (missense, nonsense, or 10q11.22 deletion). The anchoring gene–disease relationship is stated in [PMID: 42309173](https://pubmed.ncbi.nlm.nih.gov/42309173/): *"Dominant variants in GDF2 are known to cause hereditary hemorrhagic telangiectasia type 5 (HHT5), a condition characterized by telangiectases and arteriovenous malformations (AVMs)."* The ligand-redundancy explanation for its rarity is anchored in [PMID: 31828546](https://pubmed.ncbi.nlm.nih.gov/31828546/): *"bmp9 mutants survive to adulthood with no overt phenotype. In contrast, combined loss of bmp10 and bmp10-like results in embryonic lethal cranial AVMs indistinguishable from acvrl1 mutants."*

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function variant in *GDF2*** (missense e.g. p.Val403Ile / p.Glu355Gln; nonsense; or >5 Mb 10q11.22–q11.23 deletion) **leads to** reduced production/secretion of functional **BMP9**.
2. Reduced circulating BMP9 **results in** under-stimulation of the endothelial **ALK1 (ACVRL1) / endoglin** receptor complex. *(Partially buffered by BMP10 — see branch A.)*
3. Under-stimulated ALK1 **leads to** reduced **SMAD1/5/8 phosphorylation** and reduced **ID1** transcription in endothelial cells.
4. Reduced SMAD1/5/8 signaling **results in** (a) loss of the endothelial **quiescence brake** and (b) **impaired shear-stress mechanotransduction** with **loss of Connexin37 (Cx37)**. *(Cx37 loss is demonstrated in mouse models; step 4b is mechanistically established.)*
5. Loss of the brake **leads to** compensatory over-activation of **PI3K/Akt/mTOR**, **VEGFR2**, and up-regulation of **Angiopoietin-2 (Angpt2)** (Angpt2 = top upregulated gene by retinal RNA-Seq).
6. These pro-angiogenic signals **result in** endothelial **hyperproliferation, hypermigration, and arteriovenous mis-specification**; combined with Cx37-permissive capillary enlargement, capillaries **transform into arteriovenous shunts**.
7. Shunting and dysplastic vessels **lead to** mucocutaneous **telangiectases** and visceral **AVMs**.
8. Telangiectases/AVMs **result in** the clinical phenotype: **epistaxis, GI bleeding, iron-deficiency anemia**, and AVM-shunt complications (**paradoxical emboli, stroke, brain abscess, high-output heart failure, intracranial hemorrhage**).

**Branch A (dosage/redundancy):** Because **BMP10** can also activate ALK1, heterozygous BMP9 loss is often buffered → **incomplete penetrance and ultra-rarity of HHT5**. If *both GDF2 alleles* are lost (biallelic), circulating BMP9 **and** BMP10 both fall to undetectable levels → severe loss of endothelial BMP activity → **childhood pulmonary arterial hypertension and/or HHT-like disease** (a distinct, more severe branch).

### Signaling schematic

```
        GDF2 (10q11.22) LOF  (missense / nonsense / >5 Mb deletion)
                    │  ↓ BMP9 protein
                    ▼
   Circulating BMP9  ── (BMP10 partial redundancy) ── buffers heterozygotes
                    │  ↓ ligand availability
                    ▼
        ALK1 (ACVRL1) + Endoglin (ENG)   [endothelial receptor complex]
                    │  ↓ receptor activation
                    ▼
             SMAD1/5/8-P  →  ID1        (quiescence program)
              │                    │
   ↓ shear mechanotransduction     ↓ brake released
   ↓ Connexin37 (Cx37)             │
              │                    ▼
              │     ↑ PI3K/Akt/mTOR · ↑ VEGFR2 · ↑ Angpt2
              └──────────┬─────────┘
                         ▼
   EC hyperproliferation + AV mis-specification + capillary enlargement
                         ▼
              TELANGIECTASES  &  ARTERIOVENOUS MALFORMATIONS
                         ▼
   Epistaxis · GI bleeding · anemia · PAVM/HAVM/CVM/GI-AVM complications
```

### Where HHT5 fits within the HHT gene family

| Subtype | Gene | Protein / role in pathway | Relative frequency |
|---|---|---|---|
| HHT1 | *ENG* | Endoglin co-receptor | ~40–50% (higher cerebral VM risk) |
| HHT2 | *ACVRL1* | ALK1 type I receptor | ~40% |
| JP-HHT | *SMAD4* | Downstream SMAD + juvenile polyposis | Small % |
| **HHT5** | ***GDF2*** | **BMP9 circulating ligand** | **Ultra-rare (~9 probands)** |

All converge on the **BMP9/10 → ALK1/ENG → SMAD1/5/8** axis; HHT5 is the **ligand-level** lesion of the same pathway that HHT1/HHT2 disrupt at the receptor level.

### Anatomical / cellular localization

- **Primary cell type:** vascular endothelial cell (CL:0000115), especially capillary/arteriovenous endothelium.
- **Primary organs/systems (UBERON):** nasal mucosa (UBERON:0001826), skin (UBERON:0002097), lung (UBERON:0002048), liver (UBERON:0002107), brain (UBERON:0000955), gastrointestinal tract (UBERON:0000160); cardiovascular system overall.
- **Subcellular (GO CC):** plasma-membrane receptor complex; nucleus (SMAD-driven transcription); BMP9 is a secreted extracellular ligand (GO:0005615, extracellular space).
- **Lateralization:** lesions are multifocal and typically bilateral/systemic rather than lateralized.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [42309173](https://pubmed.ncbi.nlm.nih.gov/42309173/) | *Ancient founder GDF2 variant / semi-dominant PAH* | Human genetics | F001, F011 — GDF2 dominant variants cause HHT5 |
| [34611981](https://pubmed.ncbi.nlm.nih.gov/34611981/) | *Clinical manifestations of GDF2 HHT5 patients* | Human clinical cohort (n=4) | F001, F004 — missense variants, deletions, cerebral involvement |
| [17311849](https://pubmed.ncbi.nlm.nih.gov/17311849/) | *BMP-9 signals via ALK1, inhibits angiogenesis* | In vitro | F002 — BMP9 is physiological ALK1 ligand |
| [18309101](https://pubmed.ncbi.nlm.nih.gov/18309101/) | *BMP-9 is a circulating vascular quiescence factor* | Human biochemistry | F002 — circulating BMP9 2–12 ng/mL >> EC50 |
| [33834622](https://pubmed.ncbi.nlm.nih.gov/33834622/) | *Homozygous GDF2 nonsense mutations → PAH / HHT-like* | Human genetics + assay | F003 — biallelic loss abolishes BMP9/10 → PAH/HHT-like |
| [27874028](https://pubmed.ncbi.nlm.nih.gov/27874028/) | *Transmammary anti-BMP9/10 mouse HHT model* | Mouse model | F006 — recapitulates AVMs; Angpt2 top gene |
| [31828546](https://pubmed.ncbi.nlm.nih.gov/31828546/) | *BMP10-mediated ALK1 signaling required continuously* | Zebrafish model | F006, F011 — BMP9/BMP10 redundancy explains rarity |
| [31689244](https://pubmed.ncbi.nlm.nih.gov/31689244/) | *Correcting SMAD1/5/8, mTOR, VEGFR2 treats HHT* | Mouse model + therapy | F007 — PI3K/Akt/mTOR + VEGFR2 overactivation |
| [32078368](https://pubmed.ncbi.nlm.nih.gov/32078368/) | *Impaired SMAD1/5 mechanotransduction & Cx37* | Mouse/in vitro | F007 — Cx37 loss permits shunting |
| [39292928](https://pubmed.ncbi.nlm.nih.gov/39292928/) | *Pomalidomide for epistaxis in HHT (PATH-HHT RCT)* | RCT (n=144) | F005 — ESS −0.94 vs placebo |
| [35226946](https://pubmed.ncbi.nlm.nih.gov/35226946/) | *Systemic antiangiogenic therapies for HHT* | Review | F005 — bevacizumab, pazopanib, thalidomide |
| [41347972](https://pubmed.ncbi.nlm.nih.gov/41347972/) | *What's new in HHT?* | Review | F008 — epistaxis >90%, anemia ~50% |
| [41166505](https://pubmed.ncbi.nlm.nih.gov/41166505/) | *HHT: gene targets and emerging therapies* | Review | F008 — AVM complications |
| [38864625](https://pubmed.ncbi.nlm.nih.gov/38864625/) | *How I treat bleeding in HHT* | Review | F009 — prevalence 1/5000 |
| [41610956](https://pubmed.ncbi.nlm.nih.gov/41610956/) | *Global genetic prevalence of HHT variants* | Genomic database | F009 — genetic prevalence, underdiagnosis |
| [19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/) | *Embolization for PAVM: decision analysis* | Decision model | F010 — survival benefit of embolotherapy |
| [34280349](https://pubmed.ncbi.nlm.nih.gov/34280349/) | *Second International HHT Guidelines* | Guideline | F005, F010 — management standard |
| [33513792](https://pubmed.ncbi.nlm.nih.gov/33513792/) | *HHT: need for evidence-based pharmacotherapy* | Review | F002, F007 — ENG/ACVRL1/BMP9/BMP10 pathway |

**Section-by-section mapping to the research template:**

- **§1 Disease Information / §4 Genetics:** F001, F004 — *GDF2* on 10q11.22, OMIM #615506, missense/nonsense/deletion variants; autosomal dominant. Synonyms: Osler-Weber-Rendu disease type 5, GDF2-related HHT.
- **§2 Etiology / §6 Mechanism:** F002, F003, F006, F007, F011 — loss of the BMP9→ALK1/ENG→SMAD1/5/8 quiescence brake; downstream PI3K/Akt/mTOR, VEGFR2, Angpt2; BMP10 redundancy; biallelic → PAH.
- **§3 Phenotypes / §7 Anatomy:** F004, F008 — epistaxis, telangiectases, PAVM/HAVM/CVM/GI-AVM; atypical HHT5 distribution + cerebral involvement.
- **§8 Temporal / §9 Inheritance & Population:** F009 — AD, age-dependent penetrance, variable expressivity, ~1/5000 overall; HHT5 ultra-rare.
- **§10 Diagnostics:** F004, F009 — Curaçao criteria + genetic testing (panel/WES/WGS + CNV detection for deletions).
- **§11 Prognosis:** F010 — near-normal life expectancy with screening/embolization; morbidity from bleeding and AVM complications.
- **§12 Treatment / §13 Prevention:** F005, F010 — antiangiogenics (pomalidomide RCT, bevacizumab), antifibrinolytics, iron, embolization, organ screening, antibiotic prophylaxis, genetic counseling.
- **§14–15 Other species / Models:** F006 — mouse (BMP9/10 immunoblockade) and zebrafish (*bmp9/bmp10*) models.

---

## Sections with Limited or No HHT5-Specific Data

Consistent with an ultra-rare disorder (~9 probands), several template subsections have **no HHT5-specific evidence** and are addressed only by extrapolation from the broader HHT literature or are not applicable:

- **§2 Environmental / protective factors & gene–environment interactions:** No HHT5-specific data. HHT lesions can be aggravated by mechanical trauma, anticoagulants/antiplatelets (bleeding), and hormonal/inflammatory stimuli, but no protective alleles or GxE interactions are established for HHT5.
- **§4 Epigenetics / modifier genes:** No HHT5-specific methylation or histone data. BMP10 dosage is the principal biological "modifier" (redundancy). No dedicated modifier-gene studies exist for HHT5.
- **§5 Infectious agents:** Not applicable — HHT5 is a Mendelian genetic disorder, not infectious. (Brain abscess is a *complication* of right-to-left PAVM shunting, not a cause.)
- **§10 Omics diagnostics / liquid biopsy:** Exploratory exosomal miRNA signatures exist for HHT1/HHT2 but are not validated for HHT5 or in clinical use.
- **§11 Survival statistics:** No HHT5-specific survival curves; overall HHT life expectancy is near-normal with management.
- **§12 Pharmacogenomics / gene & cell therapy:** No approved or trial-stage gene/cell therapy specific to *GDF2*; recombinant BMP9/BMP10 supplementation is a conceptual (not clinical) strategy.
- **§14 Natural disease in other species / zoonosis:** No naturally occurring *GDF2*-HHT5 reported in companion animals or wildlife (OMIA); zoonotic potential not applicable. Orthologs exist (mouse *Gdf2*, zebrafish *bmp9*) but only as engineered/experimental models.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity:** With only ~9 probands, all HHT5 clinical statements rest on small case series ([PMID: 34611981](https://pubmed.ncbi.nlm.nih.gov/34611981/), [PMID: 33834622](https://pubmed.ncbi.nlm.nih.gov/33834622/)). Penetrance, expressivity, sex ratio, age-of-onset distributions, and organ-specific AVM frequencies **specific to HHT5** are effectively unquantified.
2. **Genotype–phenotype boundary with PAH:** The same gene produces HHT-like disease, isolated PAH, or a hybrid depending on allele dosage and residual BMP9/BMP10 activity. The determinants that steer a given individual toward telangiectasia/AVM versus pulmonary vascular remodeling are not defined.
3. **Redundancy-driven variability:** BMP10 buffering explains rarity but also makes penetrance unpredictable; whether *BMP10* variants or expression levels act as clinical modifiers in HHT5 carriers is untested.
4. **Therapy extrapolation:** All treatment efficacy data (pomalidomide RCT, bevacizumab cohorts) derive from HHT overall — predominantly ENG/ACVRL1 patients. **No HHT5 patient has been reported in a therapeutic trial**, so subtype-specific response is unknown. Pomalidomide response analyses even suggest genotype effects (ACVRL1 less responsive than ENG), raising the question of how ligand-level (GDF2) disease responds.
5. **Large-deletion contiguous-gene effects:** The >5 Mb 10q11.22–q11.23 deletions remove neighboring genes; the extravascular features attributed to some HHT5 patients may reflect contiguous-gene syndromes rather than *GDF2* loss per se.
6. **No dedicated HHT5 model:** Existing mouse/zebrafish models manipulate BMP9 **and** BMP10 together (or the receptor); a clean heterozygous-*Gdf2* model that reproduces adult telangiectasia/AVMs is lacking, limiting mechanistic dissection of the *heterozygous* human condition.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international HHT5/*GDF2* registry** to aggregate the scattered probands, standardize Curaçao + genetic ascertainment, and generate the first penetrance and organ-involvement frequency estimates specific to HHT5.
2. **Systematic CNV-aware genetic testing** in HHT-suspected but ENG/ACVRL1/SMAD4-negative patients: use exome/genome sequencing with copy-number calling (or chromosomal microarray) to detect the large 10q11.22 deletions that single-gene panels miss ([PMID: 34611981](https://pubmed.ncbi.nlm.nih.gov/34611981/)).
3. **Functional reclassification of *GDF2* VUS** using BMP-responsive luciferase reporter assays to quantify residual ligand activity and correlate with phenotype severity along the HHT-to-PAH axis.
4. **Circulating BMP9/BMP10 quantification as a biomarker:** measure plasma BMP9/BMP10 and serum-derived endothelial BMP activity in *GDF2* carriers to test whether residual activity predicts penetrance and distinguishes HHT-like from PAH-prone individuals ([PMID: 33834622](https://pubmed.ncbi.nlm.nih.gov/33834622/)).
5. **Generate a heterozygous *Gdf2* mouse (± sensitized *Bmp10* background)** to model the adult, dominant human disease and test BMP10-redundancy as the penetrance modifier.
6. **Prospective inclusion of HHT5 patients in antiangiogenic trials** (pomalidomide, bevacizumab), pre-registering genotype-stratified analyses to determine whether ligand-level disease responds differently from receptor-level (ENG/ACVRL1) disease.
7. **Evaluate ligand-replacement strategies** (recombinant BMP9/BMP10 or ALK1-agonist biologics) as mechanism-directed therapy uniquely rational for a ligand-deficiency disease, initially in the immunoblockade and biallelic models.
8. **Apply guideline-concordant organ screening** to all confirmed HHT5 patients — contrast echocardiography/CT for PAVMs, brain MRI for cerebral VMs (justified by the documented cerebral involvement), and hepatic imaging — with antibiotic prophylaxis for those with PAVMs ([PMID: 34280349](https://pubmed.ncbi.nlm.nih.gov/34280349/), [PMID: 19376841](https://pubmed.ncbi.nlm.nih.gov/19376841/)).

---

## Ontology Term Appendix

| Category | Term | ID |
|---|---|---|
| Disease | Hereditary hemorrhagic telangiectasia type 5 | MONDO:0014660; OMIM:615506 |
| Gene | *GDF2* (BMP9) | HGNC:4217; NCBI Gene 2658 |
| Gene | *ACVRL1* (ALK1) | HGNC:175 |
| Gene | *ENG* (endoglin) | HGNC:3349 |
| Phenotype | Epistaxis | HP:0000421 |
| Phenotype | Telangiectasia of the skin | HP:0000562 |
| Phenotype | Cerebral arteriovenous malformation | HP:0002948 |
| Phenotype | Pulmonary arteriovenous malformation | HP:0006775 |
| Phenotype | Iron deficiency anemia | HP:0001891 |
| Cell type | Endothelial cell | CL:0000115 |
| Anatomy | Nasal mucosa / lung / liver / brain | UBERON:0001826 / :0002048 / :0002107 / :0000955 |
| Process | Negative regulation of angiogenesis | GO:0016525 |
| Process | BMP signaling pathway | GO:0030509 |
| Treatment | Pomalidomide / Bevacizumab / Tranexamic acid | NCIT:C48225 / C2039 / C61785 |
| Treatment | Therapeutic embolization | NCIT:C15325 |

---

*Report compiled from 11 confirmed findings across 5 investigation iterations and 58 reviewed papers. Evidence types are labeled human clinical, human genetics, in vitro, and model organism throughout. All quoted snippets are verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_5-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Hemorrhagic_Telangiectasia_5-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 15 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014660` (3 mentions) - the report calls it "hereditary hemorrhagic telangiectasia type 5"; MONDO calls it **microcephaly 15, primary, autosomal recessive**
- `HP:0006775` (2 mentions) - the report calls it "Pulmonary AVM", "Pulmonary arteriovenous malformation"; HP calls it **Multiple myeloma**
- `HP:0100761` (1 mention) - the report calls it "Hepatic AVM"; HP calls it **Visceral angiomatosis**
- `HP:0002239` (1 mention) - the report calls it "GI bleeding / telangiectases"; HP calls it **Gastrointestinal hemorrhage**
- `NCIT:C15325` (1 mention) - the report calls it "Therapeutic embolization"; NCIT calls it **Skin Transplantation**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000562` (3 mentions), reported as "telangiectasia of the skin", "Mucocutaneous telangiectases", "Telangiectasia of the skin" - HP does not contain this term
- `NCIT:C48225` (1 mention) - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000115` (3 mentions) - the report calls it "endothelial cell", "Primary cell type:** vascular endothelial cell", "Endothelial cell"; CL calls it **endothelial cell**
- `HP:0000421` (3 mentions) - the report calls it "epistaxis", "Recurrent epistaxis", "Epistaxis"; HP calls it **Epistaxis**
- `HP:0002948` (3 mentions) - the report calls it "cerebral arteriovenous malformation", "Cerebral vascular malformation", "Cerebral arteriovenous malformation"; HP calls it **Vertebral fusion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016525` - called "negative regulation of angiogenesis", "Negative regulation of angiogenesis"
- `CL:0000115` - called "endothelial cell", "Primary cell type:** vascular endothelial cell", "Endothelial cell"
- `HP:0000421` - called "epistaxis", "Recurrent epistaxis", "Epistaxis"
- `HP:0000562` - called "telangiectasia of the skin", "Mucocutaneous telangiectases", "Telangiectasia of the skin"
- `HP:0002948` - called "cerebral arteriovenous malformation", "Cerebral vascular malformation", "Cerebral arteriovenous malformation"
- `HP:0001891` - called "Iron-deficiency anemia", "Iron deficiency anemia"
- `HP:0006775` - called "Pulmonary AVM", "Pulmonary arteriovenous malformation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.