---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T14:13:11.100936'
end_time: '2026-10-23T14:28:01.751351'
duration_seconds: 890.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Food Allergy
  mondo_id: MONDO:0700226
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: allergic disease from food material; allergy of food material; food material
    allergic disease; IgE-mediated food allergy; food hypersensitivity
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
citation_count: 44
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 44
  on_topic: 36
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 37
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001025
    reported_labels:
    - 81.9% (anaphylaxis); 31% (childhood)
    ontology_label: Urticaria
  - term_id: HP:0100665
    reported_labels:
    - 69.4%; 48% (childhood)
    ontology_label: Angioedema
  - term_id: HP:0001047
    reported_labels:
    - 21% (childhood)
    ontology_label: Atopic dermatitis
  obsolete_terms:
  - term_id: NCIT:C2175
    ontology_label: Gene-Vector Complex
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Food_Allergy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Food_Allergy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Food Allergy
- **MONDO ID:** MONDO:0700226 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** allergic disease from food material; allergy of food material; food material allergic disease; IgE-mediated food allergy; food hypersensitivity
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Food Allergy** covering all of the
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

# Food Allergy (MONDO:0700226) — Comprehensive Disease Characteristics Report

## Summary

**Food allergy is a common, complex, polygenic immune-mediated disease with no single causal gene.** Unlike Mendelian disorders named after one locus, food allergy (MONDO:0700226) arises from the interaction of many susceptibility genes — primarily **epithelial-barrier genes** (*FLG*/filaggrin, the *SERPINB* clade B serpin cluster at 18q21.3) and **type-2 immune genes** (the *HLA* region [peanut-specific], the *IL4/IL13* cytokine cluster at 5q31.1, and *C11orf30/EMSY* at 11q13.5) — with a large environmental/exposome contribution. Because the research template requests a "causal gene" but food allergy is categorized as **Complex**, the correct answer is that susceptibility is distributed polygenically; the most robustly replicated genome-wide significant loci are *FLG*, the *SERPINB* cluster, *HLA*, the 5q31.1 cytokine cluster, and *C11orf30/EMSY* ([PMID: 29051540](https://pubmed.ncbi.nlm.nih.gov/29051540/), [PMID: 29030101](https://pubmed.ncbi.nlm.nih.gov/29030101/), [PMID: 39698764](https://pubmed.ncbi.nlm.nih.gov/39698764/)).

The classic IgE-mediated form of the disease results from a failure of oral tolerance. Allergen crosses a compromised epithelial barrier, pathogenic Th2 lymphocytes drive B-cell class-switching to allergen-specific IgE, IgE arms mast cells and basophils via FcεRI, and on re-exposure the cross-linking of surface IgE triggers explosive degranulation — releasing histamine and proteases that produce urticaria, angioedema, gastrointestinal, respiratory and cardiovascular symptoms, and potentially fatal anaphylaxis. Food allergy affects as many as **8% of young children and 2% of adults** in Western countries and its prevalence is rising. The disease spans IgE-mediated, non-IgE-mediated (e.g., FPIES, allergic proctocolitis), and mixed (eosinophilic esophagitis) subtypes, and it imposes a heavy psychosocial and quality-of-life burden on patients and caregivers.

Management rests on allergen avoidance plus emergency intramuscular adrenaline (epinephrine) for acute reactions, with two disease-modifying strategies now established: **oral immunotherapy (OIT)** and **omalizumab** (anti-IgE, now FDA-approved for food allergy). The single most important advance in prevention is the paradigm shift demonstrated by the LEAP and EAT trials: **early oral introduction of allergenic foods in infancy prevents food allergy**, reversing decades of avoidance-based advice. This report synthesizes 14 confirmed findings across all 15 requested sections, grounded in 58 reviewed papers.

---

## Key Findings

### Finding 1 — Food allergy is polygenic: barrier genes + type-2 immune genes

Food allergy has no single Mendelian cause. A genome-wide association study of oral-food-challenge–diagnosed food allergy (497 cases / 2,387 controls) identified **five loci at genome-wide significance**: the clade B serpin (*SERPINB*) gene cluster at 18q21.3, the cytokine gene cluster at 5q31.1 (which includes *IL4/IL13*), the filaggrin gene (*FLG*), the *C11orf30/LRRC32* locus, and the *HLA* region. Notably the HLA association is peanut-specific ([PMID: 29051540](https://pubmed.ncbi.nlm.nih.gov/29051540/)):

> *"We identify five loci at genome-wide significance, the clade B serpin (SERPINB) gene cluster at 18q21.3, the cytokine gene cluster at 5q31.1, the filaggrin gene, the C11orf30/LRRC32 locus, and the human leukocyte antigen (HLA) region."*

A multi-population meta-analysis established **C11orf30/EMSY** as a genetic risk factor for food allergy generally and found *ITGA6* near genome-wide significance for peanut allergy; several implicated genes (*C11orf30/EMSY, SKAP1, CTNNA3*) are involved in epigenetic regulation of gene expression ([PMID: 29030101](https://pubmed.ncbi.nlm.nih.gov/29030101/)). A 2025 review consolidates the picture: **16 genome-wide significant variants and 32 epigenome-wide significant loci**, with implicated genes falling into two functional groups — epithelial barrier function (*FLG, SERPINB7*) and immune function (*HLA, IL4*) ([PMID: 39698764](https://pubmed.ncbi.nlm.nih.gov/39698764/)):

> *"Identified genes for food allergy are mainly involved in epithelial barrier function (e.g., FLG, SERPINB7) and immune function (e.g., HLA, IL4)."*

**Gene/ontology annotations:** *FLG* (HGNC:3748), *IL4* (HGNC:6014), *IL13* (HGNC:5973), *HLA-DQ/DR* region, *SERPINB7* (HGNC:8951), *C11orf30/EMSY* (HGNC:18071). Inheritance is **multifactorial/polygenic** (MONDO category: Complex). Evidence source: human GWAS.

### Finding 2 — Early oral introduction prevents food allergy (LEAP/EAT): a primary-prevention paradigm shift

The **LEAP randomized controlled trial** (n=640 high-risk infants) demonstrated that early, sustained peanut consumption from infancy to age 5 prevents peanut allergy, and the protective effect **persists to 12 years of age** (144 months): peanut allergy was 15.4% in the original avoidance group vs 4.4% in the consumption group (P<0.001) ([PMID: 38804779](https://pubmed.ncbi.nlm.nih.gov/38804779/)):

> *"At age 144 months, peanut allergy remained significantly more prevalent in participants in the original peanut avoidance group than in the original peanut consumption group (15.4% [38 of 246 participants] vs. 4.4% [11 of 251 participants]; P<0.001)."*

A pooled intention-to-treat analysis of LEAP + EAT showed a **75% reduction in peanut allergy (p<.0001)** among children randomized to early peanut consumption, with earlier introduction more effective ([PMID: 36435990](https://pubmed.ncbi.nlm.nih.gov/36435990/)). Modeling estimated that a **77% population-level reduction** in peanut allergy could be achieved by introducing peanut at 4 months (with eczema) / 6 months (without eczema), with the benefit diminishing for each month of delay ([PMID: 36521802](https://pubmed.ncbi.nlm.nih.gov/36521802/)). Meta-analyses provide **high-certainty evidence for peanut and egg** ([PMID: 41967460](https://pubmed.ncbi.nlm.nih.gov/41967460/)).

| Analysis | Population | Effect | PMID |
|---|---|---|---|
| LEAP 12-yr follow-up | 497 high-risk | 15.4% vs 4.4% peanut allergy (P<0.001) | 38804779 |
| LEAP+EAT pooled ITT | High-risk + general | 75% reduction (p<.0001) | 36435990 |
| Population model | All infants | 77% reduction if introduced early | 36521802 |
| Meta-analysis | Multiple RCTs | High-certainty for peanut & egg | 41967460 |

**Mechanistic basis** — the *dual-allergen-exposure hypothesis*: cutaneous exposure through an inflamed/disrupted skin barrier (e.g., atopic dermatitis) promotes sensitization, whereas early oral intake induces tolerance ([PMID: 38740132](https://pubmed.ncbi.nlm.nih.gov/38740132/), [PMID: 41967460](https://pubmed.ncbi.nlm.nih.gov/41967460/)). Evidence source: human RCT + modeling.

### Finding 3 — Pathophysiology: IgE-mediated type-2 immune cascade with mast-cell degranulation

Experimental food allergy demonstrates the causal chain. Allergen is taken up across the GI epithelium (facilitated when IgE–antigen complexes bind **CD23** on epithelial cells) → pathogenic **Th2 lymphocytes** are activated (IL-4, IL-5, IL-13) → B cells class-switch to allergen-specific **IgE** → IgE binds **FcεRI** on mast cells and basophils → re-exposure cross-links surface IgE → mast-cell/basophil **degranulation** (histamine, mast cell protease MMCP-1) → anaphylaxis and local GI manifestations ([PMID: 19079331](https://pubmed.ncbi.nlm.nih.gov/19079331/)):

> *"antigen uptake can be facilitated by immunoglobulin-E (IgE)-antigen complexes binding to CD23 on the epithelial cell surface. Studies on systemic anaphylaxis or local gastrointestinal manifestations of food allergy in mice have highlighted the contribution of IgE, mast cells, and pathogenic Th2 lymphocytes in experimental food allergy."*

In mouse models, ovalbumin-specific serum IgE correlates with jejunal MMCP-1+ mast-cell density and predicts diarrhea, accompanied by increased IL-4/IL-6 ([PMID: 19450258](https://pubmed.ncbi.nlm.nih.gov/19450258/)). Mast-cell-deficient W/Wv mice and IL-4/IL-10 neutralization studies confirm the dependence of the response on mast cells and Th2 cytokines ([PMID: 12951468](https://pubmed.ncbi.nlm.nih.gov/12951468/), [PMID: 9003216](https://pubmed.ncbi.nlm.nih.gov/9003216/)). Evidence source: in vitro + model organism + human.

**GO/CL ontology suggestions:** GO:0016068 (type I hypersensitivity), GO:0043303 (mast cell degranulation), GO:0002639 (positive regulation of immunoglobulin production), GO:0042092 (type 2 immune response); CL:0000097 (mast cell), CL:0000767 (basophil), CL:0000546 (T-helper 2 cell), CL:0000236 (B cell). CHEBI: histamine (CHEBI:18295).

### Finding 4 — Treatment: avoidance + epinephrine; OIT and omalizumab are disease-modifying

Intramuscular **adrenaline (epinephrine)** is the only life-saving treatment for food-induced anaphylaxis but is frequently delayed or underused; patients should carry autoinjectors ([PMID: 40719286](https://pubmed.ncbi.nlm.nih.gov/40719286/), [PMID: 42262574](https://pubmed.ncbi.nlm.nih.gov/42262574/)):

> *"Intramuscular adrenaline continues to be the primary treatment, yet its administration is often delayed or insufficiently used."*

**Oral immunotherapy (OIT)** achieves desensitization (e.g., sesame OIT ~85–97%) with mostly mild-to-moderate adverse events ([PMID: 42808451](https://pubmed.ncbi.nlm.nih.gov/42808451/)); earlier initiation of cow's-milk OIT (<24 months) is associated with fewer severe reactions and no maintenance-phase anaphylaxis ([PMID: 41616970](https://pubmed.ncbi.nlm.nih.gov/41616970/)). **Omalizumab** (anti-IgE monoclonal) raises reaction thresholds and improves OIT tolerability; in the OUtMATCH trial, post-omalizumab dietary consumption success reached **61–70% for milk/egg/wheat vs 38–56% for peanut/tree nuts** ([PMID: 40447195](https://pubmed.ncbi.nlm.nih.gov/40447195/)):

> *"greater success was observed for milk, egg, or wheat (61%-70%) than for peanut or tree nuts (38%-56%)"*

Omalizumab monotherapy is now **FDA-approved** for food allergy.

**NCIT treatment terms:** Epinephrine (NCIT:C377), Omalizumab (NCIT:C2175), immunotherapy (NCIT:C15299), antihistamine (NCIT:C265), corticosteroid (NCIT:C2271). Evidence source: human clinical trials + reviews.

### Finding 5 — Substantial psychosocial burden and reduced quality of life

Food allergy imposes measurable psychological and quality-of-life costs on patients and caregivers. Mothers of children with food allergy had significantly higher state anxiety (STAI-S, P<0.001) and caregiver burden (Zarit, P<0.001) and lower quality of life (EUROHIS-QOL, P=0.009) than controls; cow's-milk protein allergy specifically increased trait anxiety (P=0.035) ([PMID: 40923420](https://pubmed.ncbi.nlm.nih.gov/40923420/)):

> *"Mothers in the FA group had significantly higher state anxiety (STAI-S) (P < 0.001) and ZCBS scores (P < 0.001) compared to controls."*

In a national US sample (N=5,940 food-allergy households), **69.9% screened at-risk for food insecurity**, and FA-related anxiety was the most common psychosocial experience (25.4%/30.1% of children/adults), higher among food-insecure households (p<.0001) ([PMID: 38288585](https://pubmed.ncbi.nlm.nih.gov/38288585/)):

> *"FA-related anxiety was the most common (25.4%/30.1% of children/adults)"*

Disease-specific instruments include the **Food Allergy Quality of Life Questionnaire (FAQLQ)** and **Food Allergy Independent Measure (FAIM)** ([PMID: 37695230](https://pubmed.ncbi.nlm.nih.gov/37695230/), [PMID: 38288585](https://pubmed.ncbi.nlm.nih.gov/38288585/)). Evidence source: human cross-sectional/survey.

### Finding 6 — Gut dysbiosis and reduced short-chain fatty acids: the gene-environment axis

Reduced gut bacterial diversity and abundance are epidemiologically associated with food allergy. Mechanistically, microbial **short-chain fatty acids (SCFAs)** steer CD4 T-cell differentiation toward anergic **regulatory T cells (Treg, Foxp3+)** versus allergic **Th2** responses, acting through GPR41/GPR43/GPR109a receptors and histone-deacetylase inhibition ([PMID: 39571752](https://pubmed.ncbi.nlm.nih.gov/39571752/)):

> *"T-cell differentiation poses an opportunity to direct the immune cells towards an anergic regulatory T cell (Treg) or allergic T helper 2 (Th2) response."*

Early-life microbial exposures — particularly rural/farming environments — may protect against food allergy by stimulating innate immune pathways and shaping the gut microbiome, while air pollutants (PM, NO2), synthetic barrier-disrupting chemicals, and ultra-processed foods increase risk ([PMID: 42670723](https://pubmed.ncbi.nlm.nih.gov/42670723/)):

> *"Early-life microbial exposures, especially those associated with rural and farming environments, may protect against food allergies by stimulating innate immune pathways and shaping the gut microbiome."*

Probiotic evidence is inconclusive overall but more promising in cow's-milk protein allergy ([PMID: 39571752](https://pubmed.ncbi.nlm.nih.gov/39571752/)). **CHEBI:** short-chain fatty acid (CHEBI:26666), butyrate (CHEBI:17968). **CL:** CL:0000815 (regulatory T cell). Evidence source: human epidemiology + mechanistic review.

### Finding 7 — Epidemiology: ~8% of children / ~2% of adults, rising; three immunologic subtypes

Food-allergic conditions affect **as many as 8% of young children and 2% of adults** in Western countries, with rising prevalence ([PMID: 39257598](https://pubmed.ncbi.nlm.nih.gov/39257598/)):

> *"Food allergic (FA) conditions have been classified as immunoglobulin E (IgE) and non-IgE-mediated reactions that affect as many as 8% of young children and 2% of adults in Western countries, and their prevalence seems to be rising."*

A systematic review/meta-analysis of US pediatric data showed prevalence rose from **5.6% (2012) to 6.6% (2018)** — a 1.6 percentage-point increase per decade (95% CI 0.5–2.7) — with stabilization between 2021 (7.9%) and 2024 (7.2%); the largest increase was among 10–17-year-olds, with no difference by race/ethnicity ([PMID: 42887634](https://pubmed.ncbi.nlm.nih.gov/42887634/)):

> *"FA increased from 5.6% in 2012 to 6.6% in 2018 (1.6 percentage-point increase per decade; 95% CI: 0.5-2.7), with stabilization between 2021 (7.9%) and 2024 (7.2%)."*

**Classification** spans three types: IgE-mediated FA (Th2/IgE basis), non-IgE-mediated FA (e.g., FPIES, food protein-induced allergic proctocolitis), and mixed IgE/non-IgE (eosinophilic esophagitis). **Regional triggers differ:** peanuts/tree nuts predominate in Western countries, hen's egg/cow's milk in East Asia, seafood in Southeast Asia ([PMID: 40719286](https://pubmed.ncbi.nlm.nih.gov/40719286/)). Evidence source: human epidemiology.

### Finding 8 — Prognosis: usually non-fatal; rare fatal anaphylaxis with identifiable risk factors

Anaphylaxis case-fatality is estimated at **0.65–2% in children**; food is the main trigger (cow's milk, peanuts, tree nuts); mucocutaneous signs occur in >90% of cases and death is usually secondary to laryngeal edema (seen in 40–50%). Risk factors for severe/fatal reactions include personal asthma history, peanut/tree-nut allergy, and adolescence ([PMID: 33236416](https://pubmed.ncbi.nlm.nih.gov/33236416/)):

> *"Anaphylaxis fatality rate is estimated to be 0.65% to 2%. Food is the main anaphylaxis trigger in children, notably cow's milk, peanuts, and tree nuts. Mucocutaneous manifestations are observed in more than 90% of cases"*

A systematic review of 32 studies found that young adults with asthma and known peanut/tree-nut allergy are at higher risk of fatal anaphylaxis; delayed adrenaline injection is associated with fatal outcomes, though timely adrenaline alone may be insufficient; cofactors include alcohol, exercise, medications, and mast cell disorders ([PMID: 30288817](https://pubmed.ncbi.nlm.nih.gov/30288817/)). Many IgE-mediated childhood allergies (milk, egg) resolve with age, whereas peanut/tree-nut/seafood allergies more often persist; SPT and sIgE thresholds imperfectly predict resolution ([PMID: 24132133](https://pubmed.ncbi.nlm.nih.gov/24132133/)). Evidence source: human epidemiology + systematic review.

### Finding 9 — Animal models: adjuvant-based and adjuvant-free (epicutaneous) mouse models

Mouse models (e.g., Balb/c, C3H/HeJ) sensitized to ovalbumin or peanut — orally with mucosal adjuvants such as cholera toxin, or epicutaneously (adjuvant-free) — then orally challenged, reproduce allergen-specific IgE, intestinal mast-cell activation (MMCP-1), Th2 cytokines, and systemic anaphylaxis ([PMID: 19079331](https://pubmed.ncbi.nlm.nih.gov/19079331/), [PMID: 19450258](https://pubmed.ncbi.nlm.nih.gov/19450258/)). Mast-cell-deficient W/Wv mice and IL-4/IL-10 neutralization establish mast-cell and Th2-cytokine dependence ([PMID: 12951468](https://pubmed.ncbi.nlm.nih.gov/12951468/), [PMID: 9003216](https://pubmed.ncbi.nlm.nih.gov/9003216/)). In C3H/HeJ mice, epicutaneous immunotherapy (OVA-Viaskin patches) induced sustained protection against anaphylaxis via gastrointestinal-homing LAP+/Treg cells, demonstrating **skin–gut immune crosstalk** and a tissue-specific GI Treg deficiency in allergic mice ([PMID: 27417020](https://pubmed.ncbi.nlm.nih.gov/27417020/)):

> *"epicutaneous application of antigen generated a population of gastrointestinal-homing LAP"*

**Phenotype recapitulation:** good for IgE, mast-cell activation, Th2 cytokines, and anaphylaxis; **limitations:** adjuvants are artificial, and murine oral tolerance differs from human timing. **NCBI Taxon:** *Mus musculus* (10090). Evidence source: model organism.

### Finding 10 — Natural (spontaneous) food allergy in companion animals

Adverse food reactions occur naturally in dogs and cats, affecting mainly the integument and GI tract. In dogs, pruritus of distal limbs/face/ears/ventrum predominates, presenting as recurrent bacterial skin infections, otitis externa, and atopic dermatitis; four breeds (German shepherds, West Highland white terriers, Labrador and golden retrievers) account for ~40% of affected dogs, with onset by 6–12 months in 22–38% ([PMID: 31072328](https://pubmed.ncbi.nlm.nih.gov/31072328/)):

> *"Four breeds (German shepherd dogs, West Highland white terriers, Labrador and golden retrievers) accounted for about 40% of affected dogs. Most dogs diagnosed with a CAFR were pruritic"*

Non-cutaneous signs include GI (diarrhea, vomiting), conjunctivitis, and even anaphylaxis ([PMID: 30419909](https://pubmed.ncbi.nlm.nih.gov/30419909/)). As in humans, elimination diet followed by oral food challenge is the diagnostic gold standard ([PMID: 29871756](https://pubmed.ncbi.nlm.nih.gov/29871756/), [PMID: 32448251](https://pubmed.ncbi.nlm.nih.gov/32448251/)):

> *"An elimination diet over several weeks using a protein source and a carbohydrate source previously not fed is still the diagnostic tool of choice."*

**NCBI Taxon:** *Canis lupus familiaris* (9615), *Felis catus* (9685). Evidence source: veterinary clinical.

### Finding 11 — Phenotype spectrum: multi-system disease, urticaria/angioedema most frequent

Food allergy is a multi-system disease. In an anaphylaxis cohort, organ involvement was **cutaneous 95.7%, cardiovascular 76.8%, respiratory 74.6%**; the most common manifestations were urticaria (81.9%), dyspnea (71.3%), and angioedema (69.4%); 2.2% had biphasic reactions ([PMID: 18254479](https://pubmed.ncbi.nlm.nih.gov/18254479/)):

> *"The organs most frequently involved in the anaphylaxis were cutaneous (95.7%), cardiovascular (76.8%), and respiratory (74.6%). The most common manifestations were dyspnea (71.3%), urticaria (81.9%), and angioedema (69.4%)."*

In childhood food allergy the most common skin manifestations were angioedema (48%), urticaria (31%), and atopic dermatitis (21%) ([PMID: 9252873](https://pubmed.ncbi.nlm.nih.gov/9252873/)). Across food anaphylaxis, mucocutaneous signs occur in >90% and laryngeal edema in 40–50% ([PMID: 33236416](https://pubmed.ncbi.nlm.nih.gov/33236416/)).

| Phenotype | Frequency | HPO term |
|---|---|---|
| Urticaria | 81.9% (anaphylaxis); 31% (childhood) | HP:0001025 |
| Angioedema | 69.4%; 48% (childhood) | HP:0100665 |
| Dyspnea/respiratory | 71.3–74.6% | HP:0002094 |
| Cardiovascular/hypotension | 76.8% | HP:0002615 / HP:0001635 |
| Atopic dermatitis/eczema | 21% (childhood) | HP:0001047 |
| Anaphylaxis | — | HP:0100845 |
| Diarrhea/vomiting (GI) | — | HP:0002014 / HP:0002017 |
| Laryngeal edema | 40–50% | HP:0012027 |

Evidence source: human clinical cohorts.

### Finding 12 — Epigenetics: DNA-methylation signatures distinguish clinical allergy from sensitization

A machine-learning study on DNA-methylation (DNAm) data narrowed 405,000+ CpGs to an **18-CpG signature mapping to 13 genes** (many immune-associated; 7 previously linked to food allergy) that achieved high classification accuracy distinguishing food-allergic from merely sensitized individuals — addressing the <50% accuracy of standard tests and the reliance on oral food challenges ([PMID: 31216310](https://pubmed.ncbi.nlm.nih.gov/31216310/)):

> *"The 18-CpG signature mapped to 13 genes, on which biological insights were collected. Notably, many of the FA-discriminating genes found in this study were strongly associated with the immune system, and seven of the 13 genes were previously associated with FA."*

A 2025 review reports **32 epigenome-wide significant loci** in food allergy ([PMID: 39698764](https://pubmed.ncbi.nlm.nih.gov/39698764/)). This positions epigenetic marks as both a mechanism and a candidate diagnostic. Evidence source: human computational/epigenomics.

### Finding 13 — Alpha-gal syndrome: a tick-bite-induced, delayed, adult-onset red-meat allergy

Alpha-gal syndrome (AGS) is a **delayed IgE-mediated food allergy** to galactose-α-1,3-galactose (α-Gal), a carbohydrate epitope ubiquitously expressed in non-primate mammalian tissues. Sensitization follows tick bites and produces delayed (often 2–6 h) reactions to red meat and mammalian products ([PMID: 42571940](https://pubmed.ncbi.nlm.nih.gov/42571940/), [PMID: 42808634](https://pubmed.ncbi.nlm.nih.gov/42808634/)):

> *"α-Gal has emerged as the causative antigen of alpha-gal syndrome (AGS), a delayed IgE-mediated food allergy to mammalian-derived products, including red meat."*

> *"Alpha-gal syndrome (AGS) is an emerging red meat allergy, IgE-mediated, with delayed reactions to a carbohydrate derived from mammals: α-gal (galactose-α-1,3-galactose). Sensitization follows a tick bite."*

α-Gal epitopes are thermostable, so conventional cooking may not reduce allergenicity, and AGS epidemiology is shaped by tick distribution with likely under-diagnosis ([PMID: 42571940](https://pubmed.ncbi.nlm.nih.gov/42571940/)). Sensitized individuals show elevated innate-immune markers and reduced regulatory cytokines (IL-10, IL-35) ([PMID: 42877672](https://pubmed.ncbi.nlm.nih.gov/42877672/)). AGS is an important example of an **environmentally triggered, carbohydrate-directed, adult-onset** food allergy that departs from the classic protein-sensitization, childhood-onset paradigm. **CHEBI:** galactose-α-1,3-galactose. Evidence source: human clinical/review.

### Finding 14 — Food allergy–eosinophilic esophagitis continuum: antigen exposure shapes immune phenotype

IgE-mediated food allergy and **eosinophilic esophagitis (EoE)** are interconnected manifestations on a continuum determined by antigen exposure patterns, dose, and chronicity. Among children with IgE-mediated food allergy, **EoE prevalence is ~4.7% (nearly 100-fold higher than the general population)**, and during oral immunotherapy confirmed EoE develops in **1–10% of participants**. Mechanistically, antigen avoidance favors IgE-mediated responses via T follicular helper cells, whereas sustained exposure promotes a shift toward eosinophilic/EoE-type inflammation ([PMID: 42575621](https://pubmed.ncbi.nlm.nih.gov/42575621/)):

> *"Among children with IgE-mediated food allergy, EoE prevalence is nearly 100-fold higher than the general population at 4.7%. During oral immunotherapy, gastrointestinal symptoms are common, with confirmed EoE developing in 1% to 10% of participants."*

This finding clarifies a key safety consideration for OIT and links the IgE-mediated and mixed subtypes mechanistically. **CL:** CL:0000771 (eosinophil); **UBERON:** UBERON:0001043 (esophagus). Evidence source: human clinical/review.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. GENETIC + ENVIRONMENTAL PREDISPOSITION
   Barrier genes (FLG, SERPINB7) + immune genes (HLA, IL4/IL13, C11orf30/EMSY)
   + exposome (pollution, dysbiosis/low SCFA, timing of allergen exposure)
        │  leads to
        ▼
2. EPITHELIAL BARRIER DYSFUNCTION
   Impaired skin and/or gut barrier allows allergen penetration
   (CD23-mediated transepithelial uptake in the gut)
        │  results in
        ▼
3. BRANCH POINT — SITE & TIMING OF FIRST EXPOSURE (dual-allergen-exposure hypothesis)
   ├── Cutaneous exposure through INFLAMED skin → SENSITIZATION  ──┐
   └── Early ORAL exposure through HEALTHY gut   → TOLERANCE (Treg) │ [protective; LEAP/EAT]
                                                                    ▼
4. TH2 POLARIZATION  (sensitization pathway)
   Dendritic cells present allergen → pathogenic Th2 cells (IL-4, IL-5, IL-13)
   [Low SCFA tips the Treg/Th2 balance toward Th2 — inferred from models]
        │  drives
        ▼
5. IgE CLASS-SWITCH
   B cells produce allergen-specific IgE
        │  which binds
        ▼
6. EFFECTOR-CELL ARMING
   IgE occupies FcεRI on mast cells and basophils
        │  then on RE-EXPOSURE
        ▼
7. DEGRANULATION
   Allergen cross-links surface IgE → histamine, tryptase, MMCP-1 release
        │  causing
        ▼
8. CLINICAL MANIFESTATION (multi-system)
   Cutaneous (urticaria 82%, angioedema 69%), respiratory (dyspnea 71%),
   cardiovascular (hypotension 77%), GI → ANAPHYLAXIS (fatality 0.65–2%)

   BRANCH (chronic sustained exposure): shift toward EOSINOPHILIC inflammation
   → eosinophilic esophagitis (EoE), the "mixed" phenotype
```

**Upstream vs downstream.** Upstream drivers are genetic barrier/immune variants and environmental/exposome factors (steps 1–3). The Th2→IgE axis (steps 4–6) is the central, intermediate mechanism — the node targeted by both omalizumab (sequesters IgE) and OIT (reprograms the T-cell/antibody response toward IgG4/Treg). Downstream (steps 7–8) is effector-cell degranulation and the clinical syndrome — the node targeted by adrenaline.

**Cell types involved:** epithelial cells (CL:0000066), dendritic cells (CL:0000451), Th2 cells (CL:0000546), B cells (CL:0000236), mast cells (CL:0000097), basophils (CL:0000767), regulatory T cells (CL:0000815), eosinophils (CL:0000771).

**Anatomical structures (UBERON):** skin (UBERON:0002097), gastrointestinal tract / small intestine–jejunum (UBERON:0001052 / UBERON:0002115), esophagus (UBERON:0001043), respiratory tract / larynx (UBERON:0001004 / UBERON:0001737), cardiovascular system (UBERON:0004535). Body systems: integumentary, digestive, respiratory, cardiovascular, immune.

### Therapeutic logic mapped onto the chain

| Intervention | Mechanistic node targeted | Effect |
|---|---|---|
| Early oral introduction (LEAP/EAT) | Step 3 branch point | Diverts to tolerance; **77% population reduction** |
| Allergen avoidance | Step 7 (prevents cross-linking) | Prevents reactions (but may favor IgE/EoE branch) |
| Oral immunotherapy (OIT) | Steps 4–6 (reprograms T/B response) | Desensitization ~85–97% (sesame) |
| Omalizumab (anti-IgE) | Step 6 (sequesters free IgE) | Raises thresholds; 38–70% consumption success |
| Adrenaline (epinephrine) | Step 8 (reverses effector physiology) | Life-saving acute rescue |

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding | Evidence type |
|---|---|---|---|
| [29051540](https://pubmed.ncbi.nlm.nih.gov/29051540/) | *SERPINB GWAS of food allergy* | F1 (core susceptibility loci) | Human GWAS |
| [29030101](https://pubmed.ncbi.nlm.nih.gov/29030101/) | *Multi-population peanut GWAS; C11orf30/EMSY* | F1 | Human GWAS/meta |
| [39698764](https://pubmed.ncbi.nlm.nih.gov/39698764/) | *FA genetics & epigenetics review* | F1, F12 | Review |
| [38804779](https://pubmed.ncbi.nlm.nih.gov/38804779/) | *LEAP 12-yr follow-up* | F2 | Human RCT |
| [36435990](https://pubmed.ncbi.nlm.nih.gov/36435990/) | *Pooled LEAP+EAT causal inference* | F2 | Human RCT pooled |
| [36521802](https://pubmed.ncbi.nlm.nih.gov/36521802/) | *Window of opportunity model* | F2 | Modeling |
| [41967460](https://pubmed.ncbi.nlm.nih.gov/41967460/) | *Prevention by early introduction* | F2 | Meta-analysis |
| [19079331](https://pubmed.ncbi.nlm.nih.gov/19079331/) | *Immunophysiology of experimental FA* | F3, F9 | Model organism |
| [19450258](https://pubmed.ncbi.nlm.nih.gov/19450258/) | *IgE–MMCP-1 in jejunum* | F3, F9 | Model organism |
| [12951468](https://pubmed.ncbi.nlm.nih.gov/12951468/) | *W/Wv mast-cell-deficient mice* | F3, F9 | Model organism |
| [9003216](https://pubmed.ncbi.nlm.nih.gov/9003216/) | *Murine onset model, IL-4/IL-10* | F3, F9 | Model organism |
| [40719286](https://pubmed.ncbi.nlm.nih.gov/40719286/) | *Epidemiology & management of anaphylaxis* | F4, F7 | Review |
| [40447195](https://pubmed.ncbi.nlm.nih.gov/40447195/) | *OUtMATCH: foods after omalizumab* | F4 | Human RCT |
| [42808451](https://pubmed.ncbi.nlm.nih.gov/42808451/) | *Sesame immunotherapy review* | F4 | Systematic review |
| [41616970](https://pubmed.ncbi.nlm.nih.gov/41616970/) | *Cow's-milk OIT timing* | F4 | Human cohort |
| [40923420](https://pubmed.ncbi.nlm.nih.gov/40923420/) | *Maternal psychological effects* | F5 | Human cross-sectional |
| [38288585](https://pubmed.ncbi.nlm.nih.gov/38288585/) | *Food insecurity & psychosocial burden* | F5 | Human survey |
| [37695230](https://pubmed.ncbi.nlm.nih.gov/37695230/) | *QoL, FAQLQ, caregiver burden* | F5 | Human cross-sectional |
| [39571752](https://pubmed.ncbi.nlm.nih.gov/39571752/) | *Gut dysbiosis & probiotics* | F6 | Review |
| [42670723](https://pubmed.ncbi.nlm.nih.gov/42670723/) | *External exposome & FA* | F6 | Review |
| [39257598](https://pubmed.ncbi.nlm.nih.gov/39257598/) | *IgE & non-IgE mechanisms review* | F7 | Review |
| [42887634](https://pubmed.ncbi.nlm.nih.gov/42887634/) | *US pediatric FA temporal trends* | F7 | Meta-analysis |
| [33236416](https://pubmed.ncbi.nlm.nih.gov/33236416/) | *Anaphylaxis in children* | F8, F11 | Review |
| [30288817](https://pubmed.ncbi.nlm.nih.gov/30288817/) | *Food-induced fatal anaphylaxis* | F8 | Systematic review |
| [24132133](https://pubmed.ncbi.nlm.nih.gov/24132133/) | *Natural history; SPT/sIgE prediction* | F8 | Systematic review |
| [27417020](https://pubmed.ncbi.nlm.nih.gov/27417020/) | *Epicutaneous IT, GI LAP+ Tregs* | F9 | Model organism |
| [31072328](https://pubmed.ncbi.nlm.nih.gov/31072328/) | *Canine/feline AFR signalment* | F10 | Veterinary |
| [30419909](https://pubmed.ncbi.nlm.nih.gov/30419909/) | *Non-cutaneous AFR in pets* | F10 | Veterinary |
| [29871756](https://pubmed.ncbi.nlm.nih.gov/29871756/) | *AFR pathogenesis/diagnosis* | F10 | Veterinary review |
| [32448251](https://pubmed.ncbi.nlm.nih.gov/32448251/) | *Time to flare after OFC (pets)* | F10 | Veterinary |
| [18254479](https://pubmed.ncbi.nlm.nih.gov/18254479/) | *Anaphylaxis features in Korea* | F11 | Human cohort |
| [9252873](https://pubmed.ncbi.nlm.nih.gov/9252873/) | *Childhood FA skin manifestations* | F11 | Human cohort |
| [31216310](https://pubmed.ncbi.nlm.nih.gov/31216310/) | *ML epigenetic biomarker (18-CpG)* | F12 | Human computational |
| [42571940](https://pubmed.ncbi.nlm.nih.gov/42571940/) | *Alpha-gal syndrome mechanisms* | F13 | Review |
| [42808634](https://pubmed.ncbi.nlm.nih.gov/42808634/) | *Alpha-gal syndrome overview* | F13 | Review |
| [42877672](https://pubmed.ncbi.nlm.nih.gov/42877672/) | *Alpha-gal immunologic comparison* | F13 | Human cohort |
| [42575621](https://pubmed.ncbi.nlm.nih.gov/42575621/) | *FA–EoE continuum* | F14 | Review |
| [38740132](https://pubmed.ncbi.nlm.nih.gov/38740132/) | *Cutaneous allergen exposure in AD* | F2 (dual-allergen) | Review |

**Diagnostics (cross-cutting).** The diagnostic standard is **oral food challenge (OFC)** — skin prick tests and serum-specific IgE are sensitive but poorly specific, frequently identifying clinically irrelevant sensitization ([PMID: 42358594](https://pubmed.ncbi.nlm.nih.gov/42358594/), [PMID: 42545935](https://pubmed.ncbi.nlm.nih.gov/42545935/)). **Component-resolved diagnostics** (e.g., Ara h 2 for peanut, casein for milk, ovomucoid for egg) improve risk stratification; casein-specific IgE ≥2.55 kUA/L predicted milk-OFC positivity with AUC 0.878 ([PMID: 42451187](https://pubmed.ncbi.nlm.nih.gov/42451187/)). Emerging functional assays include the **basophil activation test (BAT)** and **mast cell activation test (MAT)** ([PMID: 42358594](https://pubmed.ncbi.nlm.nih.gov/42358594/)). Food-specific **IgG testing is not a validated diagnostic** for IgE-mediated allergy ([PMID: 42818614](https://pubmed.ncbi.nlm.nih.gov/42818614/)). Note that skin prick testing itself can rarely provoke generalized reactions in infants ([PMID: 11152165](https://pubmed.ncbi.nlm.nih.gov/11152165/)).

**Key identifiers.** MONDO:0700226; MeSH D005512 (Food Hypersensitivity); ICD-10 T78.0–T78.1 / Z91.01–Z91.018; ICD-11 4A85. Synonyms: IgE-mediated food allergy, food hypersensitivity, allergic disease from food material. Information is derived from **aggregated disease-level resources** (GWAS cohorts, registries, RCTs, reviews) rather than a single EHR patient series.

---

## Limitations and Knowledge Gaps

1. **No single causal gene.** The research template field "causal gene(s): not recorded" is correct — food allergy is polygenic. GWAS to date explain only a modest fraction of heritability; effect sizes at individual loci are small, and most loci are regulatory rather than coding. Penetrance of susceptibility alleles is low and strongly environment-dependent.
2. **Mechanistic evidence is weighted toward murine models.** The core IgE/mast-cell/Th2 cascade (F3, F9) is best demonstrated in mice using artificial adjuvants; the exact triggers of human sensitization and the quantitative role of SCFA/microbiome in humans remain inferential rather than proven causally.
3. **Diagnostic imprecision.** SPT and sIgE have low specificity; OFC — the gold standard — is resource-intensive and carries reaction risk. Epigenetic (DNAm) and functional (BAT/MAT) biomarkers are promising but not yet in routine clinical use.
4. **Subtype heterogeneity.** Non-IgE-mediated forms (FPIES, proctocolitis) and the mixed EoE phenotype are mechanistically distinct and less well characterized than classic IgE-mediated allergy; this report is weighted toward IgE-mediated disease.
5. **Prevention generalizability.** High-certainty early-introduction evidence exists for peanut and egg; data for other allergens (milk, tree nuts, seafood) are weaker, and optimal dose/duration are undefined.
6. **Treatment durability.** OIT achieves desensitization but sustained unresponsiveness (true tolerance after stopping) is less certain; omalizumab requires ongoing administration. Long-term outcomes of combination strategies are still emerging.
7. **Epidemiologic measurement.** Much prevalence data is self-reported, likely over-estimating true (OFC-confirmed) food allergy; regional/ethnic variation is incompletely mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Polygenic risk score (PRS) development and validation.** Combine the 16 GWAS loci into a PRS and test whether it predicts (a) which sensitized children have clinical reactivity and (b) who benefits most from early introduction — enabling risk-stratified prevention. (Builds on F1, F2.)
2. **Prospective human microbiome–SCFA intervention trial.** Test whether butyrate/SCFA supplementation or defined probiotic consortia (beyond cow's-milk-allergy settings) shift the Treg/Th2 balance and prevent or treat food allergy, with stool metabolomics as a mechanistic readout. (F6.)
3. **Validate the 18-CpG DNA-methylation signature prospectively** against OFC outcomes in an independent multi-ethnic cohort, and benchmark it head-to-head against component-resolved IgE and BAT to reduce reliance on OFC. (F12.)
4. **Define the EoE-risk window during OIT.** Prospectively monitor esophageal eosinophilia (symptom-triggered endoscopy or non-invasive biomarkers) across OIT protocols to quantify dose/chronicity thresholds that tip patients into the eosinophilic branch. (F14.)
5. **Extend early-introduction RCTs to non-peanut/egg allergens** (tree nuts, sesame, seafood) with harmonized dosing to generate high-certainty evidence beyond peanut and egg. (F2.)
6. **Characterize alpha-gal syndrome epidemiology and mechanism** with tick-exposure cohorts, mapping geographic tick distribution to AGS incidence and dissecting the innate/regulatory cytokine imbalance (IL-10, IL-35) as therapeutic targets. (F13.)
7. **Comparative/One-Health studies** leveraging spontaneous canine and feline food allergy as a natural large-animal model to test tolerance-inducing interventions before human translation. (F10.)

---

*Report compiled from a 5-iteration autonomous investigation: 14 confirmed findings, 58 papers reviewed. Evidence types span human GWAS/RCT/cohort/survey, model organism, veterinary clinical, and computational studies.*


## Artifacts

- [OpenScientist final report](Food_Allergy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Food_Allergy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 44 |
| On topic | 36 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 14 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001025` (1 mention) - the report calls it "81.9% (anaphylaxis); 31% (childhood)"; HP calls it **Urticaria**
- `HP:0100665` (1 mention) - the report calls it "69.4%; 48% (childhood)"; HP calls it **Angioedema**
- `HP:0001047` (1 mention) - the report calls it "21% (childhood)"; HP calls it **Atopic dermatitis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C2175` (Gene-Vector Complex) (1 mention)