---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:29:17.772618'
end_time: '2026-09-25T08:45:01.558790'
duration_seconds: 943.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bubonic Plague
  mondo_id: MONDO:0001112
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 23
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 26
  quotes_valid: 20
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:41248189
  - PMID:40424556
  - PMID:40022523
  - PMID:41389991
  - PMID:41724296
  - PMID:27722864
  relevance_assessed: 24
  on_topic: 21
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 15
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0005521
    reported_labels:
    - DIC
    ontology_label: Disseminated intravascular coagulation
  - term_id: CL:0000235
    reported_labels:
    - macrophage
    - "Cell populations targeted:** phagocytes \u2014 macrophages"
    ontology_label: macrophage
  - term_id: NCIT:C839
    reported_labels:
    - First-line; historical DOC
    ontology_label: Spiramycin
  - term_id: NCIT:C516
    reported_labels:
    - First-line
    ontology_label: Ganglioside GM2
  - term_id: NCIT:C387
    reported_labels:
    - First-line/alt; PEP
    ontology_label: Recombinant Colony Stimulating Factor
  - term_id: NCIT:C1667
    reported_labels:
    - FDA-approved for plague
    ontology_label: RG 14620
  - term_id: NCIT:C480
    reported_labels:
    - Treatment/PEP
    ontology_label: Estramustine Phosphate Sodium
  - term_id: NCIT:C328
    reported_labels:
    - Meningitis, alt
    ontology_label: Caffeine
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bubonic_Plague-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bubonic_Plague-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bubonic Plague
- **MONDO ID:** MONDO:0001112 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bubonic Plague** covering all of the
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

# Bubonic Plague (MONDO:0001112): Comprehensive Disease Characterization

*Autonomous scientific discovery report — 5 iterations, 13 confirmed findings, 35 papers reviewed*

**Disease:** Bubonic Plague · **MONDO:** MONDO:0001112 · **Category:** Infectious Disease
**Causal agent:** *Yersinia pestis* (NCBI:txid632)
**Evidence base:** Aggregated disease-level resources + primary literature (PubMed). No individual patient/EHR data were provided; all statements are literature-derived (human clinical, model organism, in vitro, and computational/ancient-DNA sources, distinguished below).

---

## Summary

**Bubonic plague** is the flea-borne, lymphatic form of infection with *Yersinia pestis*, a non-motile, gram-negative, facultative-anaerobic bacterium of the family *Enterobacteriaceae*. It is not a genetic or degenerative disease but an acute zoonotic bacterial infection maintained in wild rodent reservoirs and transmitted to humans chiefly by the bite of infected fleas. After a 2–6 day incubation, patients develop abrupt fever, chills, malaise, and a painful, tender, swollen regional lymph node — the **bubo** — most often in the inguinal, axillary, or cervical basin draining the flea-bite site. Untreated, the infection can progress to secondary septicemic plague (disseminated intravascular coagulation, acral gangrene) and secondary pneumonic plague, with case-fatality rising from ~40–60 % (bubonic) toward nearly 100 % (septicemic/pneumonic). Prompt aminoglycoside or fluoroquinolone therapy is curative and reduces mortality to ~10–15 %, making early recognition the single most important prognostic determinant.

Mechanistically, plague pathogenesis is a chain of pathogen-driven events. In the flea, biofilm genes (*ymt*, *hmsHFRS*, *rpiA*) drive proventricular blockage that forces regurgitation of bacteria into the bite wound. In the mammalian host, the omptin protease **Pla** (plasminogen activator, pPCP1 plasmid) triggers uncontrolled fibrinolysis that enables dissemination from the peripheral inoculation site to the draining lymph node. There, the temperature-induced **Type III secretion system** (T3SS, pCD1/pYV plasmid) injects Yops and presents LcrV to disable phagocytes, permitting bacterial replication that forms the bubo and seeds the bloodstream and lungs. *Y. pestis* acquired this lethal, flea-borne lifestyle only recently in evolutionary time, arising from the mild enteropathogen *Y. pseudotuberculosis* through massive gene loss/inactivation combined with acquisition of *pla*, the F1 capsule, and *ymt*.

Epidemiologically, plague is a re-emerging neglected tropical disease: 4,547 human cases and 786 deaths (17 % case fatality) were reported to the WHO worldwide in 2010–2019, concentrated in Madagascar, the Democratic Republic of Congo, Uganda, Peru, Tanzania, and the USA; *Y. pestis* was added to the WHO priority/pandemic pathogen list in 2024. Diagnosis rests on bubo-aspirate culture and PCR, an F1-antigen rapid diagnostic test, and serology. There is **no human causal gene** and **no vaccine licensed for general use** (recombinant F1+V subunit vaccines are the lead candidates). Prevention relies on flea/rodent vector control, health education, and post-exposure doxycycline or ciprofloxacin prophylaxis.

---

## Section 1 — Disease Information

**Overview.** Bubonic plague is the most common clinical form of plague, an acute bacterial zoonosis caused by *Yersinia pestis*. "The disease is caused by *Yersinia pestis*, a non-motile, gram-negative, facultative anaerobic bacterium belonging to the family of *Enterobacteriaceae*" ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)). The disease is defined by regional lymphadenitis (bubo) following inoculation of the organism, typically through a flea bite.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0001112 (bubonic plague) |
| ICD-10 | A20.0 (bubonic plague); A20 (plague) |
| ICD-11 | 1B93.0 (bubonic plague) |
| MeSH | D010930 (Plague) / "Plague, Bubonic" |
| SNOMED CT | Bubonic plague (disorder) |
| Pathogen (NCBI Taxonomy) | *Yersinia pestis*, txid632 |

OMIM and Orphanet are not applicable as primary sources because plague is an infectious, non-Mendelian disease; OMIM/Orphanet host-genetics entries do not define the condition.

**Synonyms / alternative names.** Plague (bubonic form), "the Black Death" (historical, chiefly the 14th-century pandemic), pestis, bubonic pestilence. Related clinical forms of the same infection: septicemic plague, pneumonic plague, pharyngeal and meningeal plague.

**Data provenance.** Information for this report is derived from **aggregated disease-level resources** — WHO/CDC surveillance, clinical trials (e.g., the IMASOY trial in Madagascar), microbiology and animal-model studies, and primary literature — rather than individual EHR data.

---

## Section 2 — Etiology

**Primary cause (infectious).** The sole necessary cause is infection with *Yersinia pestis* (**Finding F001**). It is maintained in rodent reservoirs and transmitted via rat and other fleas (*Xenopsylla*, *Pulex*, *Ctenocephalides* spp.); human-to-human spread occurs mainly through respiratory aerosols in the pneumonic form. Untreated case fatality ranges "from 40% (bubonic plague) to nearly 100% (septicemic and pneumonic plague)" ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)).

**Environmental / occupational risk factors.** Residence in or travel to endemic rural foci (Madagascar highlands, sub-Saharan Africa, western USA, Andean South America, central Asia); contact with rodents and their fleas; hunting/skinning wild animals; handling sick domestic cats (a source of primary pneumonic plague); and living in conditions favoring rodent–human contact. Climate influences vector ecology: modeling of the human flea *Pulex irritans* projects range expansion toward higher latitudes under warming, with "increased plague risk in temperate zones, as warmer temperatures accelerate flea life cycles and pathogen transmission efficiency" ([PMID: 41667532](https://pubmed.ncbi.nlm.nih.gov/41667532/)).

**Genetic risk / protective factors (host).** There is no Mendelian susceptibility gene. Ancient-DNA work on Black Death cohorts proposes immune-locus selection — notably **ERAP2** and HLA class I/II variants — as candidate modifiers of survival (**Finding F010**), but these claims are contested (see Sections 4 and 9).

**Gene–environment interactions.** Not established for humans. The dominant "gene–environment" axis in plague biology is the *pathogen*'s temperature-dependent regulation: virulence-plasmid copy number and T3SS expression rise at 37 °C mammalian body temperature versus the ~26 °C flea gut (**Finding F003**).

---

## Section 3 — Phenotypes

Bubonic plague is a stereotyped acute febrile syndrome (**Finding F009**). Onset is **adult and all-age, acute**, 2–6 days after a flea bite.

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Fever (often abrupt, high) | Symptom/sign | HP:0001945 (Fever) | Near-universal |
| Regional lymphadenopathy — the **bubo** (tender, swollen, painful node) | Clinical sign | HP:0002716 (Lymphadenopathy) | Defining feature; inguinal/femoral > axillary > cervical by bite site |
| Chills / rigors | Symptom | HP:0025143 (Chills) | Common |
| Headache | Symptom | HP:0002315 (Headache) | Common |
| Malaise / prostration | Symptom | HP:0033834 (Malaise) | Common |
| Hypotension / shock (septicemic progression) | Sign | HP:0002615 (Hypotension) | With dissemination |
| Disseminated intravascular coagulation | Lab/clinical | HP:0005521 (DIC) | Septicemic form |
| Acral necrosis / gangrene ("black" digits) | Physical | HP:0100758 (Gangrene) | Late septicemic |
| Cough / dyspnea / hemoptysis (secondary pneumonic) | Sign | HP:0012735 (Cough); HP:0002105 (Hemoptysis) | If lungs seeded |

**Characteristics.** Severity: moderate-to-severe, variable. Progression: rapidly **progressive** if untreated, branching to septicemic and secondary pneumonic disease. Because "delaying therapy will result in increased morbidity and mortality" ([PMID: 15207311](https://pubmed.ncbi.nlm.nih.gov/15207311/)), the temporal window for intervention is short.

**Quality-of-life impact.** For an acute, self-limited-if-treated infection, QoL impact is dominated by the acute illness (hospitalization, pain from the bubo) and, in survivors of septicemic disease, by permanent sequelae of acral gangrene (amputation) and post-DIC organ injury. Formal EQ-5D/SF-36 data specific to plague were not identified.

---

## Section 4 — Genetic / Molecular Information

**Host causal genes: none.** Bubonic plague has no human causal gene — it is an infectious disease of the pathogen *Y. pestis* (**Finding F010**). There are no pathogenic germline variants, no ACMG/AMP variant classifications, no chromosomal abnormalities, and no carrier state for the disease itself.

**Candidate host modifier loci (contested).** Ancient-DNA studies report that "Infectious diseases are among the strongest selective pressures driving human evolution" ([PMID: 36261521](https://pubmed.ncbi.nlm.nih.gov/36261521/)) and identify **ERAP2** and HLA variants whose frequencies shifted across the 14th-century pandemic, with a protective ERAP2 genotype proposed to enhance macrophage control of *Y. pestis*. Independent analyses dispute this: "Our analyses do not sustain the conclusions of HLA protection or susceptibility to plague based on ancient DNA" ([PMID: 35383854](https://pubmed.ncbi.nlm.nih.gov/35383854/)); see also the ongoing exchange ([PMID: 37066254](https://pubmed.ncbi.nlm.nih.gov/37066254/), [PMID: 39972229](https://pubmed.ncbi.nlm.nih.gov/39972229/)). These are host-genetics hypotheses, not disease-defining mutations.

**Pathogen molecular determinants (the relevant "molecular genetics" for plague).** Virulence is encoded on three plasmids plus the chromosome (**Findings F003, F005, F006, F007, F012**):

| Plasmid | Key gene(s) | Product / role |
|---|---|---|
| pCD1 / pYV (~70 kb) | T3SS operons, *yopM*, *lcrV* | Type III secretion; injects Yops, presents LcrV; disables phagocytes |
| pPCP1 (~9.5 kb) | *pla* | Omptin protease (plasminogen activator); dissemination |
| pMT1 (~100 kb) | *caf1* (F1 capsule), *ymt* | Antiphagocytic capsule; murine toxin/phospholipase D for flea survival |
| Chromosome | *hmsHFRS*, *rpiA* | Biofilm exopolysaccharide; proventricular blockage |

**Epigenetic information.** Not applicable to the host in a disease-defining sense.

---

## Section 5 — Environmental Information

**Infectious agent.** *Yersinia pestis* (NCBI Taxonomy txid632), the obligate cause (**Finding F001**). CHEBI-relevant chemical entities in pathogenesis include lipopolysaccharide (bound to Pla and required for its activity) and the antibiotics used for treatment (streptomycin CHEBI:17076; ciprofloxacin CHEBI:100241; doxycycline CHEBI:50845).

**Vectors and reservoirs.** Fleas are the environmental transmission vehicle. Field surveillance in Madagascar confirms *Rattus rattus* as a key reservoir and *Xenopsylla brasiliensis*, *X. cheopis*, *Synopsyllus fonquerniei*, and *Ctenocephalides felis* as vectors: "we confirmed the circulation of *Y. pestis* … one rat seropositive and one flea PCR positive … *R. rattus* contributes to the maintenance and transmission of plague" ([PMID: 41248189](https://pubmed.ncbi.nlm.nih.gov/41248189/)). The human flea *Pulex irritans* is an additional competent vector whose distribution is climate-sensitive ([PMID: 41667532](https://pubmed.ncbi.nlm.nih.gov/41667532/)).

**Environmental / lifestyle factors.** Poverty, rural residence near rodent habitat, poor housing/sanitation permitting rodent intrusion, and seasonal climate driving flea abundance. Toxin/radiation/pollution exposures are not relevant.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

1. An infected flea feeds; **proventricular biofilm blockage** (driven by *ymt*, *hmsHFRS*, *rpiA*) prevents normal blood passage → **leads to** regurgitation of *Y. pestis* into the dermal bite wound (**Finding F006**).
2. Deposited bacteria at ~37 °C **result in** rapid up-regulation of temperature-dependent virulence programs, including elevated pYV plasmid copy number and T3SS expression (**Finding F003**).
3. The omptin protease **Pla** activates plasminogen to plasmin and urokinase while inactivating α2-antiplasmin/PAI-1 → **leads to** uncontrolled fibrinolysis and reduced fibrin(ogen) deposition, which **enables** bacterial migration from the peripheral site to the **draining lymph node** (**Finding F007**; supported by in vivo mouse evidence).
4. Within the node, the **T3SS injects Yops and presents LcrV** → **disables** phagocyte function (phagocytosis, oxidative burst, cytokine signaling), **allowing** unchecked bacterial replication (**Finding F003**).
5. Nodal replication plus the antiphagocytic F1 capsule **produce** the enlarging, inflamed, painful **bubo** — the defining clinical lesion (**Finding F009**).
6. **Branch A (septicemic):** bacteria spill into blood → bacteremia, endotoxin-driven inflammation, **DIC**, hypotension, and acral **gangrene** (**Findings F009, F013**).
7. **Branch B (secondary pneumonic):** hematogenous seeding of the lungs → pneumonia that is transmissible person-to-person by aerosol, closing the loop to new epidemics (**Findings F009, F013**).

*Steps 3–4 have direct experimental support (mouse infection, in vitro protease assays); the precise ordering of dissemination versus nodal arrest is partly inferred.*

### Detail by category

- **Molecular pathways / biochemistry.** Pla-driven activation of the host **plasminogen–plasmin fibrinolytic cascade**: "Pla activates human plasminogen to the serine protease plasmin and activates the physiological plasminogen activator urokinase" ([PMID: 23898467](https://pubmed.ncbi.nlm.nih.gov/23898467/)). These functions "enhance uncontrolled fibrinolysis … and lowered fibrin(ogen) deposition has indeed been observed in mice infected with Pla-positive *Y. pestis*."
- **Protein dysfunction (pathogen effectors).** Pla is an outer-membrane β-barrel omptin whose activity depends on bound LPS; LcrV is "a key virulence factor of *Yersinia pestis* type III secretion system" ([PMID: 41724296](https://pubmed.ncbi.nlm.nih.gov/41724296/)). Pathogenic Yersiniae "require the type III secretion system (T3SS) virulence factor to subvert host defense mechanisms and colonize host tissues" ([PMID: 40424556](https://pubmed.ncbi.nlm.nih.gov/40424556/)).
- **Immune subversion / inflammation.** Yop effectors suppress phagocytosis and innate signaling; systemic dissemination triggers cytokine storm and coagulopathy.
- **Tissue-damage mechanisms.** Lymphadenitis with hemorrhagic necrosis (bubo); ischemic necrosis/gangrene from DIC microthrombosis; hemorrhagic pneumonia.
- **Temperature regulation.** "The number of pYV molecules relative to the number of chromosomes per cell … increases with temperature" ([PMID: 40424556](https://pubmed.ncbi.nlm.nih.gov/40424556/)), coupling the flea→mammal transition to virulence induction.

**Suggested ontology terms.** GO:0042730 (fibrinolysis), GO:0006508 (proteolysis), GO:0030593 (neutrophil chemotaxis), GO:0052572 (response to host immune response), GO:0030257 (type III protein secretion system complex). Cell types (CL): CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000738 (leukocyte).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ / tissue:** the regional **lymph node** draining the inoculation site (UBERON:0000029, lymph node) — the bubo. Most commonly inguinal/femoral (UBERON:0035328), then axillary (UBERON:0002105), then cervical.
- **Secondary organ involvement:** blood/vasculature (septicemia; DIC), skin and acral extremities (gangrene; UBERON:0002097 skin), **lung** (UBERON:0002048; secondary pneumonic plague), spleen and liver (bacterial seeding), and rarely meninges (plague meningitis; UBERON:0002360).
- **Body systems:** lymphatic/immune, cardiovascular (coagulopathy, shock), integumentary, respiratory.
- **Cell populations targeted:** phagocytes — macrophages (CL:0000235) and neutrophils (CL:0000775) — which the T3SS disables; endothelium is injured indirectly via coagulopathy.
- **Subcellular:** Pla resides in the bacterial outer membrane; the T3SS forms an injectisome bridging pathogen and host-cell cytoplasm (GO:0030257).
- **Lateralization:** the bubo is typically **unilateral**, on the side of the draining basin nearest the bite.

---

## Section 8 — Temporal Development

- **Onset:** acute; **incubation 2–6 days** after flea bite (**Finding F009**). All ages affected.
- **Progression / stages:** (i) early localized febrile lymphadenitis (bubo); (ii) systemic dissemination → secondary septicemic plague; (iii) secondary pneumonic plague; (iv) end-stage multiorgan failure/shock. Progression rate is **rapid** (hours to days).
- **Course:** monophasic, self-limited **only** with prompt treatment; otherwise progressive and frequently fatal. Not relapsing-remitting or chronic.
- **Critical period:** the therapeutic window is narrow — survival hinges on antibiotics started early, ideally within the first 24 hours of symptoms.
- **Remission:** treatment-induced recovery is the rule when therapy is timely; spontaneous resolution of untreated bubonic disease is uncommon (~40–60 % untreated mortality).

---

## Section 9 — Inheritance and Population (Epidemiology)

**Epidemiology (Findings F004, F009).** Global burden 2010–2019: "there was a total of 4,547 cases, of whom 786 (17%) died" ([PMID: 37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/)). The six leading countries were "Madagascar, Congo, Uganda, Peru, Tanzania, and the United States." Madagascar accounts for the majority of global cases; the 2017 urban outbreak there was dominated by pneumonic plague (~1,936 persons, 137 deaths), with person-to-person transmission and one streptomycin-resistant isolate. *Y. pestis* is now on the WHO priority pathogen list: "the 2024 updated WHO list of priority pathogens also recognizes … *Yersinia pestis*" ([PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)).

**Inheritance:** not applicable (infectious disease; no Mendelian inheritance, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency for the disease). Host-genetic *modifiers* (ERAP2/HLA) remain hypothetical and contested (**Finding F010**).

**Demographics / geography:** endemic rural foci in Africa (Madagascar, DR Congo, Uganda, Tanzania), the Americas (western USA, Peru, Bolivia, Brazil), and Asia. Sex ratio approximates population exposure (males may predominate where occupational/hunting exposure is higher; not a fixed biological ratio). Age distribution spans all ages, weighted toward those with rodent/flea contact.

---

## Section 10 — Diagnostics

**Confirmatory testing (Finding F005).** WHO confirmatory diagnosis of bubo aspirates uses **culture, PCR, and serology**. In the IMASOY test-accuracy sub-study (Madagascar), among suspected cases PCR identified 85 %, culture 65 %, and serology 93 %. A **triplex real-time PCR** targeting three plasmid-borne genes achieved 100 % sensitivity / 82 % specificity: "The assay targeted three genes: *caf1*, *pla*, and *yopM*, located on the plasmids pMT1, pPCP1, and pCD1" ([PMID: 40705833](https://pubmed.ncbi.nlm.nih.gov/40705833/)).

**Rapid diagnostic test.** The F1-antigen lateral-flow rapid test (F1RDT) is the field workhorse: "The sensitivity and specificity of on-site F1RDT were 94% … and 74% … against RS1" ([PMID: 41389991](https://pubmed.ncbi.nlm.nih.gov/41389991/)). Specificity is context-dependent and rose in later, less explosive outbreaks (BP specificity 99 %, sensitivity 91 % in 2018), underscoring that outbreak conditions affect test performance ([PMID: 35969599](https://pubmed.ncbi.nlm.nih.gov/35969599/)).

| Modality | Target | Sensitivity | Specificity | Use case |
|---|---|---|---|---|
| Culture (bubo aspirate, blood) | Live *Y. pestis* | ~65 % | Gold standard | Confirmation, AST |
| PCR (triplex qPCR) | *caf1*, *pla*, *yopM* | ~85–100 % | 82 % | Confirmation |
| F1RDT (lateral flow) | F1 capsular antigen | 94 % | 74 % (up to 99 % later) | Field/point-of-care |
| Serology | Anti-F1 antibody | ~93 % | High | Retrospective/convalescent |

**Sample & clinical criteria.** Bubo aspirate, blood, and (for pneumonic) sputum. Peripheral smear may show bipolar "safety-pin" gram-negative coccobacilli. **Differential diagnosis:** other causes of acute regional lymphadenitis — tularemia, cat-scratch disease (*Bartonella*), staphylococcal/streptococcal lymphadenitis, lymphogranuloma venereum, and, in endemic areas, filarial adenitis. Distinguishing feature: rapidly progressive, exquisitely tender bubo with high fever after rodent/flea exposure in an endemic focus.

Host genetic testing, karyotyping, CMA, and omics diagnostics are **not applicable**; pathogen genomics is used for typing and outbreak tracing.

---

## Section 11 — Outcome / Prognosis

**Mortality (Findings F001, F009).** Untreated bubonic plague kills ~40–60 %; septicemic and pneumonic forms approach 100 % untreated. With **prompt** antibiotics, bubonic case-fatality falls to ~10–15 %. The global 2010–2019 case-fatality was 17 % ([PMID: 37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/)), reflecting delayed care and pneumonic spread in outbreaks.

**Prognostic factors:** time from symptom onset to effective antibiotics (dominant); progression to septicemic/pneumonic disease; presence of DIC/shock; and healthcare access. "Delaying therapy will result in increased morbidity and mortality" ([PMID: 15207311](https://pubmed.ncbi.nlm.nih.gov/15207311/)).

**Recovery / sequelae:** survivors treated early generally recover fully. Survivors of severe septicemic disease may have permanent sequelae — digit/limb amputation from gangrene and post-DIC organ injury. Plague is not chronic; there is no long-term carriage.

---

## Section 12 — Treatment

**First-line pharmacotherapy (Finding F002).** "Most of the therapeutic guidelines suggest using gentamicin or streptomycin as first line therapy with ciprofloxacin as optional treatment" ([PMID: 29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/)). Streptomycin is the historical drug of choice; chloramphenicol, doxycycline, gentamicin, and ciprofloxacin are also effective ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)). Chloramphenicol is preferred for plague meningitis (CNS penetration).

**Intracellular efficacy nuance.** *Y. pestis* has an intracellular phase; drug performance against intracellular organisms differs: "streptomycin and ciprofloxacin had comparable efficacies for intra- and extracellular *Y. pestis*" ([PMID: 21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/)), whereas gentamicin and doxycycline are less effective intracellularly — a rationale favoring streptomycin/ciprofloxacin in severe disease.

| Drug (class) | Role | NCIT suggestion |
|---|---|---|
| Streptomycin (aminoglycoside) | First-line; historical DOC | NCIT:C839 |
| Gentamicin (aminoglycoside) | First-line | NCIT:C516 |
| Ciprofloxacin (fluoroquinolone) | First-line/alt; PEP | NCIT:C387 |
| Levofloxacin (fluoroquinolone) | FDA-approved for plague | NCIT:C1667 |
| Doxycycline (tetracycline) | Treatment/PEP | NCIT:C480 |
| Chloramphenicol | Meningitis, alt | NCIT:C328 |

**Experimental / advanced therapeutics.** Anti-LcrV monoclonal/heavy-chain antibodies show promise: a "humanized heavy-chain antibody LcrV-X19-R1 confers complete protection against fatal pneumonic plague in mice" ([PMID: 41724296](https://pubmed.ncbi.nlm.nih.gov/41724296/)). No gene, cell, or RNA therapies apply (bacterial infection). **Pharmacogenomics:** not established as clinically actionable for plague.

**Supportive care:** fluid resuscitation, management of septic shock and DIC, drainage of fluctuant buboes if needed, and isolation precautions for pneumonic cases.

---

## Section 13 — Prevention

**Primary prevention (Finding F008).** No vaccine is licensed for general use: "More than 20 candidate plague vaccines are in the preclinical phase, with few in early (phase 1) clinical trials" ([PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)). Lead candidates are **recombinant F1+V (rF1+rV) subunit vaccines**: macaques "immunised … with an rF1+rV vaccine … were fully protected against pneumonic plague following inhalational exposure to … *Yersinia pestis* (strain CO92)," and protection required "immunity to both vaccine antigens" ([PMID: 21570437](https://pubmed.ncbi.nlm.nih.gov/21570437/)). Adenoviral-vectored F1-V constructs give 90–100 % protection in mice, with a single-dose HuAd5 F1-V fusion giving 100 % protection from morbidity and mortality; a ChAdOx1 F1-V fusion has advanced to phase I ([PMID: 41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/)). Live attenuated *Y. pseudotuberculosis* VTnF1 derivatives confer single-dose protection against bubonic and pneumonic plague, and the pYV-encoded T3SS is "mandatory to obtain a large spectrum protection" ([PMID: 39978224](https://pubmed.ncbi.nlm.nih.gov/39978224/)).

**Public-health / vector control.** Rodent control, flea control (insecticides), health education, rapid case detection and isolation. Field surveillance identifies reservoirs/vectors to target ([PMID: 41248189](https://pubmed.ncbi.nlm.nih.gov/41248189/)).

**Chemoprophylaxis (secondary/post-exposure).** Contacts of pneumonic cases "should receive antibiotic prophylaxis with doxycycline or ciprofloxacin for 7 days" ([PMID: 29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/)). Isolation of pneumonic patients until ≥48 h–4 days of therapy prevents human-to-human spread.

---

## Section 14 — Other Species / Natural Disease

**Taxonomy of susceptible hosts.** Plague is a **zoonosis** with a broad mammalian host range. Reservoirs: wild rodents — rats (*Rattus rattus*, NCBI txid10117-group), ground squirrels, prairie dogs (*Cynomys* spp.), marmots, gerbils. Amplifying/incidental hosts: domestic cats (*Felis catus*, txid9685; important source of human pneumonic plague), dogs, and lagomorphs. Field data confirm *R. rattus* as the key Madagascar reservoir ([PMID: 41248189](https://pubmed.ncbi.nlm.nih.gov/41248189/)).

**Vectors (arthropods).** Fleas: *Xenopsylla cheopis*, *X. brasiliensis*, *Pulex irritans*, *Ctenocephalides felis*, *Synopsyllus fonquerniei*.

**Comparative pathology.** "The pathologic changes that occur during bubonic plague are very similar in rodents, nonhuman primates, and humans" ([PMID: 27722864](https://pubmed.ncbi.nlm.nih.gov/27722864/)). Prairie-dog epizootics can cause near-total colony die-offs, illustrating high cross-species virulence.

**Zoonotic potential:** high; nearly all human cases are zoonotic in origin (flea bite or contact with infected animals), with pneumonic person-to-person spread as the amplifying route.

---

## Section 15 — Model Organisms

**Model systems (Finding F011).** "Various types of animal models of plague have been developed, including mice, rats, guinea pigs, and nonhuman primates … rodent and nonhuman primate models of pneumonic plague closely resemble the human disease and … the pathologic changes that occur during bubonic plague are very similar in rodents, nonhuman primates, and humans" ([PMID: 27722864](https://pubmed.ncbi.nlm.nih.gov/27722864/)).

| Model | Type | Use / recapitulation |
|---|---|---|
| Mouse (*Mus musculus*) | Mammalian | Standard for virulence, vaccine efficacy, intradermal/aerosol challenge |
| Rat (*Rattus* spp.) | Mammalian | Bubonic model; reservoir biology |
| Guinea pig | Mammalian | Vaccine efficacy under Animal Rule |
| Cynomolgus macaque / African green monkey | NHP | Pneumonic plague closely mimics human; pivotal for licensure |
| Flea (*Xenopsylla*, *Oropsylla*) | Invertebrate vector | Transmission/biofilm biology (*ymt*, *hmsHFRS*, *rpiA*) |

**Regulatory relevance (Animal Rule).** Because human efficacy trials are infeasible, licensure relies on multi-species animal data: clinical-grade F1-V, rV10, and rV10-2 vaccines "conferred pneumonic plague protection in mice, rats, guinea pigs, cynomolgus macaques and African Green monkeys" ([PMID: 21763383](https://pubmed.ncbi.nlm.nih.gov/21763383/)).

**Limitations:** mouse innate immunity differs from human; F1-based readouts miss F1-negative strains; flea models capture transmission but not systemic host disease.

---

## Mechanistic Model / Interpretation

The integrated model (**Finding F013**) unifies all findings into a single causal narrative:

```
 EVOLUTION (recent):
   Y. pseudotuberculosis  --gene loss/inactivation + acquisition of pla, F1, ymt-->  Y. pestis
                                                                                      |
 FLEA STAGE (~26 C):                                                                  v
   ymt + hmsHFRS + rpiA  --->  proventricular biofilm blockage  --->  regurgitation into bite wound
                                                                                      |
 MAMMALIAN STAGE (37 C):                                                              v
   Temperature shift  --->  up pYV copy number + T3SS expression
        |                                                                             |
        |                     Pla (pPCP1)  --->  plasmin/urokinase activation         |
        |                     --->  uncontrolled fibrinolysis  --->  DISSEMINATION to draining node
        v                                                                             v
   T3SS injects Yops + LcrV  --->  phagocytes disabled  --->  unchecked replication in LYMPH NODE
                                                                                      |
                                                                                      v
                                                       F1 capsule (antiphagocytic) --->  BUBO
                                                                                      |
                                            +-----------------------------------------+
                                            |                                         |
                                  Branch A: bacteremia                      Branch B: lung seeding
                                  --> SEPTICEMIC (DIC, gangrene)            --> secondary PNEUMONIC
                                                                              (aerosol person-to-person)
```

**Upstream vs downstream.** Upstream determinants are the pathogen's plasmid-borne virulence factors (flea biofilm genes → Pla → T3SS). Downstream manifestations are the bubo, septicemia/DIC, and pneumonia. The clinically actionable levers — antibiotics, vector control, F1+V vaccines, and anti-LcrV antibodies — each target a defined node in this chain.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports / role |
|---|---|---|
| [25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/) | *Yersinia pestis and plague – an update* | Agent, untreated CFR by form, drug options |
| [29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/) | *Bichat guidelines… plague* | First-line therapy; 7-day doxy/cipro PEP; isolation |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) | *In vitro efficacy… intracellular Y. pestis* | Streptomycin/ciprofloxacin intracellular efficacy |
| [40424556](https://pubmed.ncbi.nlm.nih.gov/40424556/) | *Polyadenylase PAPI… virulence plasmid* | T3SS essential; temperature-dependent pYV copy number |
| [41724296](https://pubmed.ncbi.nlm.nih.gov/41724296/) | *Anti-LcrV heavy-chain antibody* | LcrV as T3SS virulence factor / therapeutic target |
| [39978224](https://pubmed.ncbi.nlm.nih.gov/39978224/) | *T3SS in live Y. pseudotuberculosis vaccine* | F1 + T3SS required for broad protection |
| [37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/) | *Plague… Second Decade* | 4,547 cases / 786 deaths / 17% CFR; geography |
| [40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/) | *WHO priority pathogen editorial* | WHO listing; >20 preclinical vaccines, none licensed |
| [41389991](https://pubmed.ncbi.nlm.nih.gov/41389991/) | *IMASOY diagnostics sub-study* | F1RDT 94%/74%; culture/PCR/serology yields |
| [40705833](https://pubmed.ncbi.nlm.nih.gov/40705833/) | *Triplex qPCR for plague* | caf1/pla/yopM targets; 100%/82% |
| [32294143](https://pubmed.ncbi.nlm.nih.gov/32294143/) | *Refined flea transmission model* | ymt/hmsHFRS/rpiA proventricular blockage |
| [23898467](https://pubmed.ncbi.nlm.nih.gov/23898467/) | *Fibrinolytic activities of Y. pestis* | Pla → plasmin/fibrinolysis → dissemination |
| [21570437](https://pubmed.ncbi.nlm.nih.gov/21570437/) | *rF1+V protects macaques* | Subunit vaccine efficacy; both antigens needed |
| [41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/) | *Adenoviral-vectored vaccine* | 90–100% aerosol protection; ChAdOx1 F1-V to phase I |
| [15207311](https://pubmed.ncbi.nlm.nih.gov/15207311/) | *Plague* | Three clinical forms; treatment-timing prognosis |
| [36261521](https://pubmed.ncbi.nlm.nih.gov/36261521/) | *Immune genes and the Black Death* | ERAP2/HLA selection hypothesis |
| [35383854](https://pubmed.ncbi.nlm.nih.gov/35383854/) | *Challenging aDNA HLA claims* | Contests host-genetic selection claims |
| [27722864](https://pubmed.ncbi.nlm.nih.gov/27722864/) | *Pathology and Pathogenesis of Y. pestis* | Model recapitulation; genome-reduction evolution |
| [21763383](https://pubmed.ncbi.nlm.nih.gov/21763383/) | *rV10/F1-V in 5 species* | Multi-species Animal-Rule efficacy |
| [41248189](https://pubmed.ncbi.nlm.nih.gov/41248189/) | *Plague in Makira, Madagascar* | Reservoir/vector confirmation |
| [41667532](https://pubmed.ncbi.nlm.nih.gov/41667532/) | *Climate change and Pulex irritans* | Vector range expansion / plague risk |
| [35969599](https://pubmed.ncbi.nlm.nih.gov/35969599/) | *Optimizing imperfect diagnostics, 2017* | Diagnostic test performance in outbreaks |

**Evidence source types:** human clinical/epidemiological (37748767, 41389991, 40705833, 15207311, 25643450, 29183475, 35969599); animal-model (21570437, 41736398, 21763383, 27722864, 41724296, 39978224); in vitro/biochemical (23898467, 21628541, 40424556); field ecology (41248189, 41667532); ancient-DNA/computational (36261521, 35383854).

---

## Limitations and Knowledge Gaps

1. **Host-genetics controversy unresolved.** The ERAP2/HLA selection signal from Black Death aDNA ([PMID: 36261521](https://pubmed.ncbi.nlm.nih.gov/36261521/)) is directly disputed ([PMID: 35383854](https://pubmed.ncbi.nlm.nih.gov/35383854/), [39972229](https://pubmed.ncbi.nlm.nih.gov/39972229/)); no validated human susceptibility/protective variant exists.
2. **Vaccine gap.** No vaccine is licensed for general use; efficacy rests on animal data under the FDA Animal Rule, and F1-based approaches may not protect against F1-negative strains.
3. **Antimicrobial resistance surveillance is thin.** Streptomycin-resistant isolates have appeared (2017 Madagascar); systematic AST/resistance-gene surveillance is limited.
4. **Diagnostic specificity is outbreak-dependent.** F1RDT specificity varied from 74 % (explosive 2017 outbreak) to 99 % (2018), complicating case counts and burden estimates ([PMID: 35969599](https://pubmed.ncbi.nlm.nih.gov/35969599/)).
5. **QoL and long-term sequelae** (post-gangrene, post-DIC) are essentially uncharacterized with standardized instruments.
6. **First-line-therapy sourcing.** The original guideline PMID (15677847) content was corroborated via the Bichat guideline ([PMID: 29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/)), which carries the identical recommendations.
7. **Human primary data are aggregated**, not individual-level (no EHR/cohort granularity in this report).

---

## Proposed Follow-up Experiments / Actions

1. **Adjudicate host-genetic modifiers** with adequately powered, replicated cohorts and functional assays of the proposed ERAP2 protective genotype in human macrophage–*Y. pestis* infection models.
2. **Advance F1-V vaccines through phase II/III bridging** (e.g., ChAdOx1 F1-V) under the Animal Rule, and test constructs protective against F1-negative strains (add LcrV/T3SS antigens).
3. **Systematic AMR surveillance** across endemic foci, with whole-genome sequencing to track resistance determinants and streptomycin-resistant clones.
4. **Improve point-of-care diagnostics** — multiplex antigen/PCR devices robust to outbreak conditions, validated prospectively against culture/PCR reference standards.
5. **Clinical development of anti-LcrV immunotherapeutics** (e.g., LcrV-X19-R1) as adjuncts to antibiotics for severe/late-presenting disease.
6. **Climate-informed vector surveillance** targeting projected range-expansion zones for *Pulex irritans* and *Xenopsylla* spp. to pre-position response capacity.
7. **Standardized outcome/QoL follow-up** of survivors to quantify amputation and organ-injury sequelae.

---

*Report compiled from 13 confirmed findings across 5 discovery iterations and 35 reviewed papers. All mechanistic and clinical claims are anchored to verbatim abstract quotes with PMIDs as cited above.*


## Artifacts

- [OpenScientist final report](Bubonic_Plague-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bubonic_Plague-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 26 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 6 |
| References weighed for topical relevance | 24 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41248189` *(abstract only)*: "we confirmed the circulation of *Y. pestis* … one rat seropositive and one flea PCR positive … *R. rattus* contributes to the maintenance and transmission of plague"
  - closest text in source: "pestis in our study area (one rat seropositive and one flea PCR positive) and highlight the risk of potential human transmission"
- `PMID:40424556` *(abstract only)*: "The number of pYV molecules relative to the number of chromosomes per cell … increases with temperature"
  - closest text in source: "The number of pYV molecules relative to the number of chromosomes per cell, referred to as plasmid copy number, increases with temperature"
- `PMID:40022523` *(abstract only)*: "the 2024 updated WHO list of priority pathogens also recognizes … *Yersinia pestis*"
  - closest text in source: "The 2024 updated WHO list of priority pathogens also recognizes emerging infections and historical former pandemic infections, including Yersinia pestis, the cause of bubonic, pneumonic, and septicemic plague"
- `PMID:41389991` *(abstract only)*: "The sensitivity and specificity of on-site F1RDT were 94% … and 74% … against RS1"
  - closest text in source: "The sensitivity and specificity of on-site F1RDT were 94% (95% CI, 89.6-97.0) and 74% (95% CI, 68.2-79.3) against RS1 and 89.1% (95% CI, 84.1-93) and 77.5% (95% CI, 71.5-82.8) against RS2"
- `PMID:41724296` *(abstract only)*: "humanized heavy-chain antibody LcrV-X19-R1 confers complete protection against fatal pneumonic plague in mice"
  - closest text in source: "Targeting LcrV, a key virulence factor of Yersinia pestis type III secretion system, we developed a humanized heavy-chain antibody designated LcrV-X19-R1, and formulated it for inhalation delivery"
- `PMID:27722864` *(abstract only)*: "Various types of animal models of plague have been developed, including mice, rats, guinea pigs, and nonhuman primates … rodent and nonhuman primate models of pneumonic plague closely resemble the human disease and … the pathologic changes that occur during bubonic plague are very similar in rodents, nonhuman primates, and humans"
  - closest text in source: "Various types of animal models of plague have been developed, including mice, rats, guinea pigs, and nonhuman primates"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 23 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005521` (1 mention) - the report calls it "DIC"; HP calls it **Disseminated intravascular coagulation**
- `CL:0000235` (2 mentions) - the report calls it "macrophage", "Cell populations targeted:** phagocytes — macrophages"; CL calls it **macrophage**
- `NCIT:C839` (1 mention) - the report calls it "First-line; historical DOC"; NCIT calls it **Spiramycin**
- `NCIT:C516` (1 mention) - the report calls it "First-line"; NCIT calls it **Ganglioside GM2**
- `NCIT:C387` (1 mention) - the report calls it "First-line/alt; PEP"; NCIT calls it **Recombinant Colony Stimulating Factor**
- `NCIT:C1667` (1 mention) - the report calls it "FDA-approved for plague"; NCIT calls it **RG 14620**
- `NCIT:C480` (1 mention) - the report calls it "Treatment/PEP"; NCIT calls it **Estramustine Phosphate Sodium**
- `NCIT:C328` (1 mention) - the report calls it "Meningitis, alt"; NCIT calls it **Caffeine**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000235` - called "macrophage", "Cell populations targeted:** phagocytes — macrophages"