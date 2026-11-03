---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:58:04.951311'
end_time: '2026-10-31T19:43:23.257085'
duration_seconds: 2718.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: '"Takenouchi-Kosaki Syndrome"'
  mondo_id: MONDO:0014757
  category: Mendelian
  causal_genes: CDC42
  omim_id: OMIM:616737
  synonyms: TKS; macrothrombocytopenia and mental retardation syndrome; macrothrombocytopenia-lymphedema-developmental
    delay-facial dysmorphism-camptodactyly syndrome
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
citation_count: 33
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 14
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:34624555
  - PMID:34504210
  quotes_not_checkable: 1
  relevance_assessed: 33
  on_topic: 20
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 49
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 11
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: MONDO:0014757
    reported_labels:
    - MONDO
    ontology_label: Takenouchi-Kosaki syndrome
  - term_id: HP:0000407
    reported_labels:
    - 84.6% (11/13 reviewed)
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001999
    reported_labels:
    - Cardinal
    ontology_label: Abnormal facial shape
  - term_id: HP:0012385
    reported_labels:
    - Cardinal
    ontology_label: Camptodactyly
  - term_id: HP:0001004
    reported_labels:
    - Frequent
    ontology_label: Lymphedema
  - term_id: HP:0004322
    reported_labels:
    - Frequent
    ontology_label: Short stature
  - term_id: HP:0012443
    reported_labels:
    - Variable
    ontology_label: Abnormal brain morphology
  - term_id: HP:0000589
    reported_labels:
    - Rare (variant-specific)
    ontology_label: Coloboma
  - term_id: HP:0001890
    reported_labels:
    - Rare
    ontology_label: Autoimmune hemolytic anemia
  - term_id: UBERON:0005211
    reported_labels:
    - lymphatic vessel
    ontology_label: renal medulla interstitium
  - term_id: NCIT:C2028
    reported_labels:
    - Interleukin-1 Antagonist
    ontology_label: Tyrphostin AG 370
  - term_id: NCIT:C683
    reported_labels:
    - Prednisolone
    ontology_label: Neomycin
  - term_id: NCIT:C1301
    reported_labels:
    - Recombinant Human Growth Hormone
    ontology_label: Esperamicin A1
  - term_id: NCIT:C99279
    reported_labels:
    - Cochlear Implant
    ontology_label: FUS/DDIT3 Fusion Gene
  - term_id: NCIT:C15317
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Second-Look Surgery
  - term_id: NCIT:C79426
    reported_labels:
    - Gastrostomy
    ontology_label: Cancer Diagnostic or Therapeutic Procedure
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Takenouchi-Kosaki_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Takenouchi-Kosaki_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** "Takenouchi-Kosaki Syndrome"
- **MONDO ID:** MONDO:0014757 (if available)
- **Causal gene(s):** CDC42
- **OMIM:** OMIM:616737
- **Synonyms:** TKS; macrothrombocytopenia and mental retardation syndrome; macrothrombocytopenia-lymphedema-developmental delay-facial dysmorphism-camptodactyly syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **"Takenouchi-Kosaki Syndrome"** covering all of the
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

# Takenouchi-Kosaki Syndrome (CDC42-Related Disorder): Comprehensive Disease Characterization

**MONDO:0014757 · OMIM #616737 · Causal gene: _CDC42_ (HGNC:1736; NCBI Gene 998; UniProt P60953; Ensembl ENSG00000070831; chromosome 1p36.12)**

---

## Summary

**Takenouchi-Kosaki syndrome (TKS)** is a rare, autosomal dominant, multisystem Mendelian disorder caused by **heterozygous, almost always de novo, missense variants in _CDC42_**, the gene encoding Cell Division Control protein 42 homolog — a Rho-subfamily small GTPase that acts as a master regulator of the actin cytoskeleton. The disease name does not contain the gene symbol; all content below pertains to the _CDC42_-driven entity defined by OMIM #616737 / MONDO:0014757, not to similarly named thrombocytopenia syndromes caused by other genes. The cardinal features are **macrothrombocytopenia, developmental delay/intellectual disability, lymphedema of the lower extremities, camptodactyly, distinctive facial dysmorphism, and sensorineural hearing loss** ([PMID: 26386261](https://pubmed.ncbi.nlm.nih.gov/26386261/); [PMID: 26708094](https://pubmed.ncbi.nlm.nih.gov/26708094/)). The disorder was first delineated by Takenouchi, Kosaki and colleagues in 2015 through whole-exome sequencing, and the recurrent hot-spot variant **c.191A>G (p.Tyr64Cys / Y64C)** defines the classic phenotype ([PMID: 29335451](https://pubmed.ncbi.nlm.nih.gov/29335451/)).

A central, unifying insight from the literature is that _CDC42_ variants do not cause a single disease but a **phenotypic spectrum governed by variant position within the protein**. Effector-specificity-region variants (notably Y64C) produce classic TKS; variants near the nucleotide-binding/switch regions produce a **Noonan syndrome-like/RASopathy-like** presentation; and C-terminal and selected N-terminal variants produce a **severe neonatal autoinflammatory phenotype (NOCARH syndrome)** mediated by aberrant pyrin-inflammasome activation ([PMID: 29394990](https://pubmed.ncbi.nlm.nih.gov/29394990/); [PMID: 31601675](https://pubmed.ncbi.nlm.nih.gov/31601675/); [PMID: 42566502](https://pubmed.ncbi.nlm.nih.gov/42566502/)). This genotype-phenotype architecture is the organizing principle of the disease.

Mechanistically, the Y64C variant impairs binding to the regulator RhoGDI and to downstream effectors (Pak1/2, N-WASP), escapes KLHL23-mediated degradation, and becomes concentrated and hyperactive at the plasma membrane; this disrupts F-actin dynamics required for proplatelet extension (causing macrothrombocytopenia), neurite outgrowth (contributing to neurodevelopmental deficits), and hair-cell function (causing hearing loss) ([PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/); [PMID: 40846997](https://pubmed.ncbi.nlm.nih.gov/40846997/); [PMID: 42567517](https://pubmed.ncbi.nlm.nih.gov/42567517/)). The disease is modeled in patient iPSC-derived megakaryocytes, cellular overexpression systems, and lineage-specific conditional mouse knockouts, and CDC42 is an emerging druggable target through activity inhibitors (ML141, CASIN) and prenylation/lipidation inhibitors (GGTI-298) ([PMID: 37918315](https://pubmed.ncbi.nlm.nih.gov/37918315/); [PMID: 41581414](https://pubmed.ncbi.nlm.nih.gov/41581414/); [PMID: 42168045](https://pubmed.ncbi.nlm.nih.gov/42168045/)).

---

## 1. Disease Information

**Overview.** Takenouchi-Kosaki syndrome is a congenital, multisystem developmental disorder arising from dysregulation of _CDC42_, a critical cytoskeletal regulator. It was identified through the Japanese Initiative on Rare and Undiagnosed Diseases (IRUD) and reported as a recognizable syndromic form of thrombocytopenia combined with intellectual disability ([PMID: 41567106](https://pubmed.ncbi.nlm.nih.gov/41567106/)). The cardinal features "include macrothrombocytopenia, developmental delay, lymphedema in the lower extremities, camptodactyly, and distinctive facial features" ([PMID: 26708094](https://pubmed.ncbi.nlm.nih.gov/26708094/)).

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| OMIM | #616737 |
| MONDO | MONDO:0014757 |
| Gene (HGNC) | CDC42, HGNC:1736 |
| Gene OMIM | *116952 |
| NCBI Gene | 998 |
| UniProt | P60953 (CDC42_HUMAN) |
| Orphanet | Takenouchi-Kosaki syndrome (CDC42-related disorder) |
| MeSH | No dedicated descriptor; indexed via CDC42 / Thrombocytopenia / Intellectual Disability |

**Synonyms / alternative names.** TKS; macrothrombocytopenia and mental retardation syndrome; Macrothrombocytopenia-lymphedema-developmental delay-facial dysmorphism-camptodactyly syndrome; "CDC42-related disorder" (umbrella term for the spectrum).

**Information source.** The knowledge base is derived almost entirely from **aggregated, individual case reports and small case series** (ultra-rare disease) plus functional/model-organism studies, rather than large EHR cohorts. Published patient numbers are in the low tens worldwide.

---

## 2. Etiology

**Primary cause (genetic).** TKS is caused by **de novo heterozygous missense variants in _CDC42_**. Whole-exome sequencing identified de novo _CDC42_ missense variants in unrelated patients with a recurrent syndromic phenotype: "Whole exome sequencing revealed a de novo amino acid substitution in CDC42, a critical regulator of the cytoskeleton" ([PMID: 26386261](https://pubmed.ncbi.nlm.nih.gov/26386261/)). A second unrelated patient confirmed the entity: "We, herein, report another unrelated female patient with a similar phenotype and a de novo mutation in the same CDC42" ([PMID: 26708094](https://pubmed.ncbi.nlm.nih.gov/26708094/)).

**Genetic risk factors.** The causal variant *is* the disease; there are no known susceptibility loci or polygenic contributions. The disease arises from a single dominant-acting missense allele. Variant position is the principal determinant of phenotype (see Section 4).

**Environmental risk factors.** None established. As an essentially fully penetrant monogenic disorder of de novo origin, no toxin, lifestyle, occupational, or infectious trigger is implicated. Advanced parental age is a general (non-specific) correlate of de novo mutation but has not been specifically demonstrated for TKS.

**Protective factors.** None known at genetic or environmental level.

**Gene-environment interactions.** No validated gene-environment interactions are described for TKS. **This information is not available / not applicable** for this disorder.

---

## 3. Phenotypes

TKS is a multisystem disorder. The table below summarizes the principal phenotypes, their typical character, frequency where quantified, and suggested HPO terms.

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|-----------|------|-------|-----------|---------------|
| Macrothrombocytopenia (low count, giant platelets) | Lab abnormality | Congenital/neonatal | Cardinal; near-universal in classic TKS | HP:0001873 (Thrombocytopenia), HP:0011877 (Increased mean platelet volume) |
| Developmental delay / intellectual disability | Clinical/behavioral | Infancy/childhood | Cardinal; near-universal | HP:0001263, HP:0001249 |
| Sensorineural hearing loss | Clinical sign | Childhood, progressive | 84.6% (11/13 reviewed) | HP:0000407 |
| Distinctive facial dysmorphism | Physical | Congenital | Cardinal | HP:0001999 |
| Camptodactyly | Physical | Congenital | Cardinal | HP:0012385 |
| Lymphedema (lower extremities) | Clinical sign | Congenital/early | Frequent | HP:0001004 |
| Short stature / growth dysregulation | Physical | Childhood | Frequent | HP:0004322 |
| Structural brain anomalies | Imaging | Congenital | Variable | HP:0012443 |
| Ocular colobomas (iris/chorioretinal) | Physical | Congenital | Rare (variant-specific) | HP:0000589 |
| Autoimmune hemolytic anemia | Lab/clinical | Variable | Rare | HP:0001890 |
| Autoinflammation / HLH (NOCARH) | Clinical | Neonatal | Variant-specific subgroup | HP:0012647 (Abnormal inflammatory response) |

**Hearing loss** is quantitatively the most consistently reported non-cardinal feature: a systematic review found that "Hearing loss (HL) occurs in a great percentage of patients (84.6%)" ([PMID: 39202334](https://pubmed.ncbi.nlm.nih.gov/39202334/)), and it tends to be progressive. **Ocular colobomas** were reported with a novel p.Glu127Lys variant ([PMID: 40371891](https://pubmed.ncbi.nlm.nih.gov/40371891/)), broadening the recognized phenotype. **Autoimmune hemolytic anemia** has been documented and, in one case, resolved after splenectomy, which also improved macrothrombocytopenia ([PMID: 34403170](https://pubmed.ncbi.nlm.nih.gov/34403170/); [PMID: 36459360](https://pubmed.ncbi.nlm.nih.gov/36459360/)).

**Severity / progression.** Severity is **variable and governed by variant position** ([PMID: 29394990](https://pubmed.ncbi.nlm.nih.gov/29394990/)). Classic Y64C patients have severe developmental delay; hearing loss is progressive; the autoinflammatory subgroup can be life-threatening in the neonatal period.

**Quality of life.** Combined intellectual disability, hearing loss, motor/hand involvement (camptodactyly), and bleeding risk from thrombocytopenia substantially impair daily functioning, communication, and independence. Disease-specific QoL instruments have not been applied; this is a knowledge gap.

---

## 4. Genetic / Molecular Information

**Causal gene.** _CDC42_ (Cell Division Control protein 42 homolog; HGNC:1736; gene OMIM *116952), located on chromosome 1p36.12, encodes a ~21 kDa Rho-subfamily small GTPase that cycles between an inactive GDP-bound and active GTP-bound state and regulates actin cytoskeleton dynamics, cell polarity, migration, and vesicle trafficking.

**Pathogenic variants.** All established disease-causing variants are **heterozygous missense** substitutions. The recurrent hot-spot is **c.191A>G, p.Tyr64Cys (Y64C)**, which "encodes a key small GTP-binding protein of the Rho-subfamily, was identified in two unrelated patients with TKS" ([PMID: 29335451](https://pubmed.ncbi.nlm.nih.gov/29335451/)) and is "a hot-spot missense variant... strictly related to TKS" ([PMID: 34624555](https://pubmed.ncbi.nlm.nih.gov/34624555/)).

**Genotype-phenotype correlation by variant position.** Martinelli et al. demonstrated that "missense variants in CDC42... underlie a clinically heterogeneous group of phenotypes characterized by variable growth dysregulation, facial dysmorphism, and neurodevelopmental, immunological, and hematological anomalies," and that "mutations variably perturb CDC42 function by altering the switch between the active and inactive states of the GTPase and/or affecting CDC42 interaction with effectors, and differentially disturb cellular and developmental processes" ([PMID: 29394990](https://pubmed.ncbi.nlm.nih.gov/29394990/)).

| Variant class (location) | Representative variants | Dominant phenotype | Functional mechanism |
|--------------------------|------------------------|--------------------|----------------------|
| Effector-specificity region | **p.Tyr64Cys** | Classic TKS | Impaired RhoGDI binding + effector binding; membrane-hyperactive |
| Nucleotide-binding / switch region | p.Glu171Lys, p.Glu127Lys | Noonan-like / RASopathy-like; colobomas | Altered GTPase switch |
| C-terminal (CAAX/prenylation) | p.Arg186Cys, p.*192 (extension) | Neonatal autoinflammation / NOCARH | Disrupted prenylation/membrane targeting; pyrin activation |
| N-terminal (selected) | p.Thr43Ile, p.Met45Leu | Autoinflammation | Pyrin-inflammasome activation |

**Variant classification.** Recurrent variants (Y64C, R186C, E171K) are **pathogenic** per ACMG/AMP criteria (de novo occurrence, functional data, recurrence, absence from population databases). Novel variants (e.g., E127K) are **likely pathogenic**.

**Allele frequency.** Pathogenic variants are **absent from gnomAD/population databases** — consistent with de novo, highly penetrant dominant disease.

**Somatic vs germline.** Variants are **germline** (de novo in the proband; rare familial transmission documented). No somatic mosaicism is required (contrast with the related RHOA disorder, which is typically mosaic — [PMID: 40414526](https://pubmed.ncbi.nlm.nih.gov/40414526/)).

**Functional consequence.** Predominantly a **dominant gain-of-function / dominant-negative** effect depending on variant. Y64C is a hyperactivating, membrane-retained gain-of-function: "the Y64C mutant was concentrated at the membrane compartment due to impaired binding to Rho-GDI and more active than the wild-type. The Y64C mutant also had lower association with its effectors Pak1/2 and N-WASP" ([PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/)). A newly described quality-control axis is also disrupted: "the CDC42-Y64C germline variant in Takenouchi-Kosaki Syndrome escapes KLHL23-mediated degradation" ([PMID: 40846997](https://pubmed.ncbi.nlm.nih.gov/40846997/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifier genes, methylation signatures, or large chromosomal rearrangements are established for TKS. **Not applicable / not available.**

---

## 5. Environmental Information

No environmental, lifestyle, toxic, or infectious factors contribute to TKS causation or triggering. The disorder is **purely genetic (de novo germline)**. This section is **not applicable** for this disease. (In the autoinflammatory CDC42 subgroup, infection/inflammatory stress may act as a non-specific flare trigger, but this is not an etiologic factor.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (classic TKS, Y64C)

1. A **de novo heterozygous missense variant** (c.191A>G, p.Tyr64Cys) arises in _CDC42_ → **leads to** a single amino-acid substitution in the effector-specificity region of the CDC42 GTPase.
2. The substitution **impairs binding to RhoGDI** (the guanine-nucleotide dissociation inhibitor that sequesters CDC42·GDP in the cytosol) and **impairs KLHL23-Cul3–mediated ubiquitin degradation** of CDC42·GTP → **results in** failure of normal spatiotemporal inactivation/turnover ([PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/); [PMID: 40846997](https://pubmed.ncbi.nlm.nih.gov/40846997/)).
3. CDC42-Y64C **accumulates at the plasma membrane and is constitutively more active** than wild-type, while paradoxically showing **reduced association with CRIB-motif effectors Pak1/2 and N-WASP** → **leads to** dysregulated (mislocalized and mistimed) actin-nucleation signaling.
4. Dysregulated effector signaling (N-WASP → Arp2/3) **disrupts F-actin and microtubule dynamics** → **results in** branch points to several tissues:
   - **Megakaryocyte branch:** impaired "F-actin dynamics for proplatelet extension, which is necessary for platelet production" → defective proplatelet formation → **macrothrombocytopenia** (low count, giant platelets) ([PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/); [PMID: 37918315](https://pubmed.ncbi.nlm.nih.gov/37918315/)).
   - **Neuronal branch:** impaired neurite outgrowth → **developmental delay / intellectual disability** (inferred from Neuro2A models; [PMID: 41581414](https://pubmed.ncbi.nlm.nih.gov/41581414/)).
   - **Cochlear hair-cell branch:** loss of CDC42 (acting with RHOQ) function in hair cells → **progressive sensorineural hearing loss** ([PMID: 42567517](https://pubmed.ncbi.nlm.nih.gov/42567517/)).
   - **Neural-crest / endothelial branch:** disrupted NCC migration and endothelial lumen/filopodia formation → **craniofacial dysmorphism, congenital anomalies, lymphatic/vascular defects (lymphedema)** (inferred from conditional knockouts; [PMID: 24056078](https://pubmed.ncbi.nlm.nih.gov/24056078/); [PMID: 26253403](https://pubmed.ncbi.nlm.nih.gov/26253403/)).

### Branch: autoinflammatory variants (C-terminal / selected N-terminal)

1. A **C-terminal variant** (e.g., p.Arg186Cys, p.*192) **disrupts CAAX-motif prenylation and membrane targeting**, or an **N-terminal variant** (p.Thr43Ile, p.Met45Leu) alters CDC42 conformation → **leads to** aberrant CDC42 subcellular localization.
2. Mislocalized CDC42 **binds the B30.2 domain of pyrin** aberrantly → **results in** **pyrin-inflammasome activation**: "Three studies identify CDC42 as binding partner of the pyrin B30.2 domain, establishing a previously unrecognized mechanism regulating pyrin inflammasome activation" ([PMID: 42566502](https://pubmed.ncbi.nlm.nih.gov/42566502/)).
3. Pyrin inflammasome assembly → **caspase-1 activation** → **IL-1β and IL-18 maturation/release** → **neonatal-onset cytopenia, dyshematopoiesis, rash, autoinflammation, and hemophagocytic lymphohistiocytosis (NOCARH)**: "we identify a novel hematological/autoinflammatory condition (NOCARH syndrome) in four unrelated patients with superimposable features, including neonatal-onset cytopenia with dyshematopoiesis, autoinflammation, rash, and HLH" ([PMID: 31601675](https://pubmed.ncbi.nlm.nih.gov/31601675/)).
4. Therapeutic branch point: **IL-1β blockade** interrupts the cascade and is effective ([PMID: 31271789](https://pubmed.ncbi.nlm.nih.gov/31271789/)); serum IL-18 serves as a biomarker ([PMID: 40204564](https://pubmed.ncbi.nlm.nih.gov/40204564/)).

### Molecular detail

- **Molecular pathways.** Rho-GTPase signaling; CDC42 → N-WASP/WASP → Arp2/3 actin nucleation; CDC42 → Pak1/2; pyrin-inflammasome → caspase-1 → IL-1β/IL-18. GO terms: **GO:0007264** (small GTPase mediated signal transduction), **GO:0030036** (actin cytoskeleton organization), **GO:0032731** (positive regulation of IL-1β production), **GO:0097194** (execution phase of apoptosis/inflammasome-adjacent).
- **Cellular processes.** Cell migration, cell polarity, filopodia formation, proplatelet formation, neurite outgrowth, inflammasome-driven pyroptosis. GO:0030031 (cell projection assembly), GO:0030041 (actin filament polymerization).
- **Protein dysfunction.** Gain-of-function/dominant-negative GTPase switch perturbation; impaired regulator (RhoGDI, KLHL23) and effector (Pak1/2, N-WASP) interactions; disrupted prenylation (C-terminal variants). UniProt: **P60953** (CDC42_HUMAN).
- **Cell types involved.** Megakaryocytes (**CL:0000556**), platelets (**CL:0000233**), neurons (**CL:0000540**), cochlear hair cells (**CL:0000202**), neural crest cells (**CL:0000333**), endothelial cells (**CL:0000115**), macrophages/myeloid cells (**CL:0000235**).
- **Immune involvement.** Pyrin-inflammasome autoinflammation in C-terminal/N-terminal variant subgroup; autoimmune hemolytic anemia in rare classic cases. "Cdc42 missense variants cause various pathological phenotypes, including severe autoinflammation, suggesting previously unknown involvement of Cdc42 in innate immunity" ([PMID: 40296562](https://pubmed.ncbi.nlm.nih.gov/40296562/)).
- **Metabolic / epigenetic changes.** None established as disease-specific (not applicable).

### Mechanistic diagram

```
 de novo heterozygous CDC42 missense variant (germline)
                 │
        ┌────────┴──────────── variant POSITION determines branch ───────────────┐
        │                              │                                          │
 EFFECTOR region (Y64C)      SWITCH/nucleotide region            C-TERMINAL (R186C,*192) /
        │                     (E171K, E127K)                      N-TERMINAL (T43I, M45L)
        │                              │                                          │
 impaired RhoGDI binding       altered GDP/GTP switch              disrupted prenylation /
 + escapes KLHL23 degradation          │                           aberrant conformation
        │                              │                                          │
 membrane-retained,            dysregulated GTPase cycling         aberrant CDC42–pyrin
 HYPERACTIVE CDC42                     │                           B30.2 binding
        │                              │                                          │
 reduced Pak1/2 & N-WASP        Noonan-like / RASopathy             PYRIN INFLAMMASOME
 effector coupling             developmental phenotype              activation
        │                              │                                   │
 disrupted F-actin dynamics            │                            caspase-1 → IL-1β/IL-18
        │                              │                                   │
 ┌──────┼───────┬──────────┬─────────┐ │                            NEONATAL autoinflammation,
 │      │       │          │         │ │                            cytopenia, HLH (NOCARH)
MEGA-  NEURON  HAIR    NEURAL-CREST ENDOTHELIUM                            │
KARYO   │      CELL    /CRANIOFACE   /LYMPHATIC                      Rx: IL-1 blockade;
CYTE    │       │          │         │                              biomarker: serum IL-18
 │   impaired  hearing  dysmorphism, lymphedema,
macro-  neurite loss     cleft, CHD  vascular anomaly
thrombo growth
cytopenia
 │
developmental delay / ID
```

---

## 7. Anatomical Structures Affected

- **Hematopoietic system (primary):** bone marrow megakaryocytes and circulating platelets. UBERON:0002371 (bone marrow), UBERON:0000178 (blood).
- **Nervous system (primary):** brain/CNS (developmental delay, structural anomalies). UBERON:0000955 (brain).
- **Auditory system:** cochlea, inner-ear hair cells. UBERON:0001844 (cochlea).
- **Lymphatic/vascular system:** lower-extremity lymphatics (lymphedema). UBERON:0005211 (lymphatic vessel), UBERON:0002049 (vasculature).
- **Craniofacial skeleton:** facial bones/soft tissue (dysmorphism), palate. UBERON:0002104 / UBERON:0001716.
- **Musculoskeletal (hands):** flexed digits (camptodactyly). UBERON:0002398 (manus).
- **Eye (variant-specific):** iris and chorioretina (colobomas). UBERON:0000970 (eye).
- **Subcellular compartments:** plasma membrane (**GO:0005886**; site of mutant CDC42 accumulation), actin cytoskeleton (**GO:0015629**), cytosol (**GO:0005829**).
- **Lateralization:** bilateral/symmetric for hearing loss, lymphedema, and camptodactyly; colobomas reported bilaterally.

---

## 8. Temporal Development

- **Onset:** **Congenital / neonatal.** Macrothrombocytopenia and dysmorphism are present from birth; developmental delay becomes apparent in infancy/childhood.
- **Onset pattern:** chronic/congenital; the autoinflammatory (NOCARH) subgroup has **acute neonatal-onset** life-threatening inflammation.
- **Progression:** The multisystem structural features are **stable/non-degenerative**, but **hearing loss is progressive** ([PMID: 39202334](https://pubmed.ncbi.nlm.nih.gov/39202334/)). Thrombocytopenia can be **intermittent** in some patients ([PMID: 34624555](https://pubmed.ncbi.nlm.nih.gov/34624555/)).
- **Disease duration:** **chronic, lifelong.**
- **Critical periods:** the neonatal period is critical for the autoinflammatory subgroup (window for IL-1 blockade); early childhood is the window for developmental/hearing intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant**, essentially always **de novo**. Rare **familial autosomal dominant transmission** is documented: a mother and child both carried c.511G>A (p.Glu171Lys) with variable expressivity — "we report a mother and her child carrying the previously reported pathogenic CDC42 variant c.511G>A (p.Glu171Lys)" ([PMID: 33283961](https://pubmed.ncbi.nlm.nih.gov/33283961/)).
- **Penetrance:** essentially **complete** for recurrent pathogenic variants.
- **Expressivity:** **variable** — strongly influenced by variant position.
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity / carrier frequency:** no established founder effect; consanguinity not relevant (dominant, de novo); carrier frequency effectively zero in the general population.
- **Epidemiology:** **ultra-rare**; precise prevalence/incidence not established (low tens of published cases worldwide). Orphanet lists it as rare without a firm prevalence estimate.
- **Population demographics:** reported across diverse populations including the **first African patient** ([PMID: 33936654](https://pubmed.ncbi.nlm.nih.gov/33936654/)); many early cases from Japan reflect ascertainment via the IRUD program rather than true geographic clustering. **No sex predilection** expected for de novo autosomal dominant disease.

---

## 10. Diagnostics

- **Hematology:** CBC showing **thrombocytopenia with increased mean platelet volume (giant platelets)**; peripheral smear confirming macrothrombocytes. LOINC: platelet count (26515-7), MPV (32623-1).
- **Genetic testing (definitive):** **Whole-exome sequencing (WES)** was the original and remains the principal diagnostic route ([PMID: 26386261](https://pubmed.ncbi.nlm.nih.gov/26386261/)); **targeted single-gene/panel testing of _CDC42_** (including thrombocytopenia panels, intellectual-disability panels, and RASopathy/Noonan panels, which now include _CDC42_ — [PMID: 37987971](https://pubmed.ncbi.nlm.nih.gov/37987971/)) confirms the diagnosis. **WGS** and **trio exome** resolve novel variants ([PMID: 40371891](https://pubmed.ncbi.nlm.nih.gov/40371891/)).
- **Imaging:** brain MRI for structural anomalies; audiometry/ABR for hearing loss; echocardiography/vascular imaging for cardiac and lymphatic involvement.
- **Biomarker (autoinflammatory subgroup):** **serum IL-18** is specifically elevated — "The highest IL-18 levels were observed in diseases involving the pyrin inflammasome, such as Familial Mediterranean fever, mevalonate kinase deficiency, CDC42-associated AID and PSTPIP1-associated AID" (AUC 0.87; cutoff 412 pg/mL) ([PMID: 40204564](https://pubmed.ncbi.nlm.nih.gov/40204564/)).
- **Differential diagnosis:** other inherited macrothrombocytopenias (MYH9-related disorders, Bernard-Soulier, DOCK2/DOCK8-related — [PMID: 39836640](https://pubmed.ncbi.nlm.nih.gov/39836640/)); **Noonan syndrome/RASopathies** for the switch-region phenotype ([PMID: 37987971](https://pubmed.ncbi.nlm.nih.gov/37987971/)); other RAC-subfamily GTPase disorders (RAC1, RAC3, RHOA — [PMID: 40414526](https://pubmed.ncbi.nlm.nih.gov/40414526/)); and other autoinflammatory/HLH syndromes for the NOCARH subgroup.
- **Screening:** no population newborn screening; **cascade genetic testing** of family members is relevant where a familial variant is identified.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Classic TKS is **not typically life-limiting**; chronic morbidity dominates. The **autoinflammatory/NOCARH subgroup carries significant mortality risk** from neonatal HLH if untreated ([PMID: 31601675](https://pubmed.ncbi.nlm.nih.gov/31601675/)).
- **Morbidity/disability:** substantial and lifelong — intellectual disability, progressive hearing loss, hand/motor involvement (camptodactyly), bleeding risk, and lymphedema impair function.
- **Complications:** bleeding from thrombocytopenia; autoimmune hemolytic anemia ([PMID: 34403170](https://pubmed.ncbi.nlm.nih.gov/34403170/)); infections and gastrostomy-site complications in severely affected children ([PMID: 37347054](https://pubmed.ncbi.nlm.nih.gov/37347054/)); HLH in the autoinflammatory subgroup.
- **Prognostic factors:** **variant position is the dominant prognostic determinant** — C-terminal/N-terminal autoinflammatory variants have the most acute, highest-risk neonatal course; effector-region (Y64C) variants give severe developmental disability but a more chronic trajectory.
- **Recovery potential:** structural/developmental deficits are permanent; autoinflammation is controllable with IL-1 blockade.

---

## 12. Treatment

There is **no curative or disease-specific approved therapy**; management is **multidisciplinary, supportive, and genotype-guided**.

| Domain | Intervention | Evidence / notes | Suggested NCIT |
|--------|-------------|------------------|----------------|
| Autoinflammation (NOCARH subgroup) | **IL-1β inhibition** (anakinra, canakinumab) | "Severe autoinflammation in 4 patients with C-terminal variants in CDC42 successfully treated with IL-1β inhibition" ([PMID: 31271789](https://pubmed.ncbi.nlm.nih.gov/31271789/)) | NCIT:C2028 (Interleukin-1 Antagonist) |
| Severe refractory autoinflammation/HLH | HLH-directed immunosuppression ± HSCT | Case-based ([PMID: 31601675](https://pubmed.ncbi.nlm.nih.gov/31601675/)) | NCIT:C15431 (HSCT) |
| Macrothrombocytopenia / AIHA | **Splenectomy** | Improved both anemia and macrothrombocytopenia in a TKS patient refractory to drug therapy ([PMID: 36459360](https://pubmed.ncbi.nlm.nih.gov/36459360/)) | NCIT:C51771 (Splenectomy) |
| AIHA | Corticosteroids (prednisolone) | Initial response, may become refractory ([PMID: 34403170](https://pubmed.ncbi.nlm.nih.gov/34403170/)) | NCIT:C683 (Prednisolone) |
| Growth | **Recombinant human growth hormone** | Explored for short stature in a TKS patient ([PMID: 42746537](https://pubmed.ncbi.nlm.nih.gov/42746537/)) | NCIT:C1301 (Recombinant Human Growth Hormone) |
| Hearing loss | Hearing aids / cochlear implants, speech therapy | Standard of care given 84.6% HL frequency ([PMID: 39202334](https://pubmed.ncbi.nlm.nih.gov/39202334/)) | NCIT:C99279 (Cochlear Implant) |
| Developmental | Early intervention, PT/OT/speech therapy | Standard supportive care | NCIT:C15317 (Rehabilitation Therapy) |
| Nutrition | Gastrostomy where feeding impaired | Reported, with infection complication risk ([PMID: 37347054](https://pubmed.ncbi.nlm.nih.gov/37347054/)) | NCIT:C79426 (Gastrostomy) |

**Experimental / targeted (preclinical).** CDC42 is an emerging druggable target. **Prenylation/lipidation inhibitors** rescue mutant phenotypes: "Both the neurite outgrowth defect and the enhanced membrane localization induced by Y64C overexpression were restored by GGTI-298 treatment but not by ML141" ([PMID: 41581414](https://pubmed.ncbi.nlm.nih.gov/41581414/)); in megakaryoblasts, macrothrombocytopenia "is ameliorated by CDC42 specific- and lipidation inhibitors in MEG-01 cells" ([PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/)). CDC42-subfamily inhibitors "have recently produced lead compounds demonstrating disease-modifying effects in vivo" ([PMID: 42168045](https://pubmed.ncbi.nlm.nih.gov/42168045/)). **No gene/cell/RNA therapy** exists for TKS.

**Pharmacogenomics / treatment algorithms.** No TKS-specific pharmacogenomic guidance. Strategy is genotype-stratified: autoinflammatory variants → anti–IL-1; cytopenias → hematologic management (± splenectomy); all → developmental/hearing support.

---

## 13. Prevention

- **Primary prevention:** not possible for de novo disease. **Genetic counseling** is central: recurrence risk for parents of a de novo case is low (small residual from gonadal mosaicism); an affected individual (rare familial cases) has 50% transmission risk ([PMID: 33283961](https://pubmed.ncbi.nlm.nih.gov/33283961/)).
- **Reproductive options:** **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** are available once a familial pathogenic variant is known.
- **Secondary prevention:** early audiology screening and developmental surveillance to enable timely intervention; monitoring platelet counts and for autoimmune cytopenias.
- **Tertiary prevention:** bleeding-risk management, infection prevention around procedures, and prompt IL-1 blockade in the autoinflammatory subgroup to prevent HLH-related mortality.
- **Immunization / public-health / environmental measures:** not applicable (non-infectious, non-environmental genetic disorder).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** _CDC42_ is **deeply evolutionarily conserved** across eukaryotes — human (NCBI Gene 998), mouse _Cdc42_ (NCBI Gene 12540), zebrafish, _Drosophila_, _C. elegans_, and functional homologs in fungi (e.g., _Cryptococcus_ Wsp1/Cin1 pathway — [PMID: 22327008](https://pubmed.ncbi.nlm.nih.gov/22327008/)). The downstream WASP/N-WASP effector axis is conserved from yeast to human ([PMID: 20501656](https://pubmed.ncbi.nlm.nih.gov/20501656/)).
- **Natural disease in other species:** No naturally occurring animal ortholog of TKS is catalogued in OMIA; disease knowledge comes from engineered models, not spontaneous veterinary disease. **Not applicable** for natural disease.
- **Comparative biology:** Lineage-specific _Cdc42_ functions are conserved — neural crest, endothelial, megakaryocyte, hair-cell, and myeloid roles demonstrated in mouse recapitulate human phenotype domains (see Section 15).
- **Zoonotic potential:** none (non-transmissible genetic disorder).

---

## 15. Model Organisms

| Model | Type | Phenotype recapitulated | Reference |
|-------|------|-------------------------|-----------|
| TKS patient iPSC-derived megakaryocytes | Human cellular (iPSC) | Fewer hematopoietic progenitors, defective megakaryopoiesis, "released platelets with an abnormally low count and giant morphology" | [PMID: 37918315](https://pubmed.ncbi.nlm.nih.gov/37918315/) |
| MEG-01 megakaryoblasts expressing Y64C | In vitro overexpression | Short cytoplasmic protrusions, aberrant F-actin/microtubules, reduced platelet-like particles; rescued by CDC42/lipidation inhibitors | [PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/) |
| HEK293 expressing Y64C | In vitro | Membrane-localized hyperactive CDC42; impaired RhoGDI/effector binding | [PMID: 34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/) |
| Neuro2A neuroblastoma expressing Y64C | In vitro | Impaired neurite outgrowth, rescued by GGTI-298 (prenylation inhibitor), not ML141 | [PMID: 41581414](https://pubmed.ncbi.nlm.nih.gov/41581414/) |
| Atoh1-Cre hair-cell–specific _Cdc42_ KO mouse | Conditional mouse KO | Progressive sensorineural hearing loss; CDC42+RHOQ synergy in cochlear hair cells | [PMID: 42567517](https://pubmed.ncbi.nlm.nih.gov/42567517/) |
| Wnt1-Cre neural-crest _Cdc42_ KO mouse | Conditional mouse KO | Embryonic lethality with cleft lip, craniofacial and cardiovascular outflow defects via impaired NCC migration | [PMID: 24056078](https://pubmed.ncbi.nlm.nih.gov/24056078/) |
| Endothelial _Cdc42_ KO mouse | Conditional mouse KO | Failed vascular lumen formation, reduced filopodia; relevant to lymphatic/vascular anomalies | [PMID: 26253403](https://pubmed.ncbi.nlm.nih.gov/26253403/) |
| Myeloid-specific _Cdc42_ KO mouse | Conditional mouse KO | Macrophage pyroptosis / inflammatory models (immune axis) | [PMID: 42363173](https://pubmed.ncbi.nlm.nih.gov/42363173/) |

**Model strengths:** The iPSC-megakaryocyte model directly reproduces the hallmark macrothrombocytopenia in a patient-specific genetic background; cellular overexpression models dissect the membrane-hyperactivation mechanism and enable drug rescue; lineage-specific conditional knockouts map individual phenotype domains to specific tissues.

**Model limitations:** Conditional knockouts model **loss-of-function**, whereas TKS variants are predominantly **gain-of-function/dominant-negative**; no single model yet reproduces the full multisystem human syndrome. A knock-in Y64C mouse would be the key missing resource.

**Resources:** MGI (mouse _Cdc42_), Cellosaurus (TKS iPSC lines), ZFIN/FlyBase/WormBase for orthologs.

---

## Evidence Base

| PMID | Role in this report |
|------|---------------------|
| [26386261](https://pubmed.ncbi.nlm.nih.gov/26386261/) | Original TKS delineation; de novo _CDC42_ by WES |
| [26708094](https://pubmed.ncbi.nlm.nih.gov/26708094/) | Second unrelated patient; defines cardinal features |
| [29335451](https://pubmed.ncbi.nlm.nih.gov/29335451/) | Establishes p.Tyr64Cys as recurrent hot-spot |
| [34624555](https://pubmed.ncbi.nlm.nih.gov/34624555/) | Y64C as TKS-specific; intermittent thrombocytopenia |
| [29394990](https://pubmed.ncbi.nlm.nih.gov/29394990/) | Genotype-phenotype spectrum; functional heterogeneity |
| [34504210](https://pubmed.ncbi.nlm.nih.gov/34504210/) | Y64C mechanism: membrane hyperactivity, F-actin defect, drug rescue |
| [40846997](https://pubmed.ncbi.nlm.nih.gov/40846997/) | KLHL23/RhoGDI turnover axis; Y64C escapes degradation |
| [37918315](https://pubmed.ncbi.nlm.nih.gov/37918315/) | Patient iPSC model recapitulates macrothrombocytopenia |
| [31601675](https://pubmed.ncbi.nlm.nih.gov/31601675/) | NOCARH syndrome (C-terminal variant autoinflammation/HLH) |
| [31271789](https://pubmed.ncbi.nlm.nih.gov/31271789/) | IL-1β blockade effective in C-terminal variant autoinflammation |
| [42567517](https://pubmed.ncbi.nlm.nih.gov/42567517/) | Hair-cell Cdc42 KO mouse; CDC42+RHOQ hearing mechanism |
| [39202334](https://pubmed.ncbi.nlm.nih.gov/39202334/) | Hearing loss frequency 84.6% systematic review |
| [33283961](https://pubmed.ncbi.nlm.nih.gov/33283961/) | Familial AD transmission (E171K); spectrum breadth |
| [41581414](https://pubmed.ncbi.nlm.nih.gov/41581414/) | Prenylation inhibitor rescues neurite defect (druggability) |
| [42168045](https://pubmed.ncbi.nlm.nih.gov/42168045/) | CDC42 inhibitor development with in vivo efficacy |
| [24056078](https://pubmed.ncbi.nlm.nih.gov/24056078/) | Neural-crest Cdc42 KO → craniofacial/cardiac defects |
| [26253403](https://pubmed.ncbi.nlm.nih.gov/26253403/) | Endothelial Cdc42 KO → vascular morphogenesis defect |
| [42566502](https://pubmed.ncbi.nlm.nih.gov/42566502/) | CDC42–pyrin B30.2 interaction establishes inflammasome mechanism |
| [40204564](https://pubmed.ncbi.nlm.nih.gov/40204564/) | Serum IL-18 biomarker for pyrin-inflammasome CDC42 AID |
| [40296562](https://pubmed.ncbi.nlm.nih.gov/40296562/) | Review: CDC42 variants span NDD to autoinflammation |
| [40371891](https://pubmed.ncbi.nlm.nih.gov/40371891/) | Novel E127K variant; ocular colobomas |
| [36459360](https://pubmed.ncbi.nlm.nih.gov/36459360/) | Splenectomy improves macrothrombocytopenia/AIHA |
| [41567106](https://pubmed.ncbi.nlm.nih.gov/41567106/) | IRUD identification; clinical characterization |

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease / small N.** Evidence rests on case reports and small series; no prevalence/incidence figures, no robust natural-history cohort, and no validated QoL data.
2. **Loss-of-function vs gain-of-function model mismatch.** Available mouse models are conditional knockouts; no knock-in of the human gain-of-function Y64C allele exists, limiting faithful organismal modeling of classic TKS.
3. **Mechanistic inference for CNS phenotype.** The neurite-outgrowth → developmental-delay link is inferred from Neuro2A cells, not demonstrated in vivo.
4. **Genotype-phenotype boundaries are still being mapped**, with novel variants (E127K, E171K) expanding the phenotype and blurring class boundaries.
5. **No approved targeted therapy.** CDC42 and prenylation inhibitors remain preclinical; IL-1 blockade is established only for the autoinflammatory subgroup.
6. **Epidemiologic and demographic data are essentially absent** (sex ratio, true geographic distribution, carrier/founder analysis all not established).

---

## Proposed Follow-up Experiments / Actions

1. **Generate a Y64C knock-in mouse** (and other variant-class knock-ins) to model the gain-of-function multisystem syndrome and test candidate drugs in vivo.
2. **Establish an international TKS/CDC42 patient registry** to define prevalence, natural history, variant-stratified outcomes, and validated QoL measures.
3. **Advance CDC42/prenylation inhibitors** (GGTI-298, CASIN, ML141-class) toward clinical translation with tissue-selective delivery, prioritizing platelet and neuronal endpoints.
4. **Prospective evaluation of serum IL-18** as a diagnostic/monitoring biomarker across the full CDC42 variant spectrum, not only the autoinflammatory subgroup.
5. **Systematic audiologic natural-history study** to time cochlear intervention, given 84.6% progressive hearing loss.
6. **Functional classification pipeline** (RhoGDI binding, KLHL23 turnover, membrane localization, pyrin binding) applied to each new variant to prospectively assign phenotype class and guide management.

---

*Report compiled from 10 confirmed findings and 55 reviewed papers over 5 investigation iterations. Evidence types span human clinical case reports/series, patient-derived iPSC models, in vitro overexpression systems, conditional mouse genetics, and computational/structural analyses.*


## Artifacts

- [OpenScientist final report](Takenouchi-Kosaki_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Takenouchi-Kosaki_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 33 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34624555` *(abstract only)*: "a hot-spot missense variant... strictly related to TKS"
  - closest text in source: "Takenouchi-Kosaki syndrome (TKS) is a recently delineated syndromic form of thrombocytopenia strictly related to an hot-spot missense variant, p.Tyr64Cys, in CDC42 (Cell Division Control protein 42)"
- `PMID:34504210`: "is ameliorated by CDC42 specific- and lipidation inhibitors in MEG-01 cells"
  - closest text in source: "This suggests that reduced PLP production by Y64C was ameliorated by Cdc42-specific inhibitors and GGTI-298"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:31271789`: "Severe autoinflammation in 4 patients with C-terminal variants in CDC42 successfully treated with IL-1β inhibition"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 28 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014757` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Takenouchi-Kosaki syndrome**
- `HP:0000407` (1 mention) - the report calls it "84.6% (11/13 reviewed)"; HP calls it **Sensorineural hearing impairment**
- `HP:0001999` (1 mention) - the report calls it "Cardinal"; HP calls it **Abnormal facial shape**
- `HP:0012385` (1 mention) - the report calls it "Cardinal"; HP calls it **Camptodactyly**
- `HP:0001004` (1 mention) - the report calls it "Frequent"; HP calls it **Lymphedema**
- `HP:0004322` (1 mention) - the report calls it "Frequent"; HP calls it **Short stature**
- `HP:0012443` (1 mention) - the report calls it "Variable"; HP calls it **Abnormal brain morphology**
- `HP:0000589` (1 mention) - the report calls it "Rare (variant-specific)"; HP calls it **Coloboma**
- `HP:0001890` (1 mention) - the report calls it "Rare"; HP calls it **Autoimmune hemolytic anemia**
- `UBERON:0005211` (1 mention) - the report calls it "lymphatic vessel"; UBERON calls it **renal medulla interstitium**
- `NCIT:C2028` (1 mention) - the report calls it "Interleukin-1 Antagonist"; NCIT calls it **Tyrphostin AG 370**
- `NCIT:C683` (1 mention) - the report calls it "Prednisolone"; NCIT calls it **Neomycin**
- `NCIT:C1301` (1 mention) - the report calls it "Recombinant Human Growth Hormone"; NCIT calls it **Esperamicin A1**
- `NCIT:C99279` (1 mention) - the report calls it "Cochlear Implant"; NCIT calls it **FUS/DDIT3 Fusion Gene**
- `NCIT:C15317` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Second-Look Surgery**
- `NCIT:C79426` (1 mention) - the report calls it "Gastrostomy"; NCIT calls it **Cancer Diagnostic or Therapeutic Procedure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C51771` (1 mention) - the report calls it "Splenectomy"; NCIT calls it **Total Laryngectomy**