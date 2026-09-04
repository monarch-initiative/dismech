---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T07:44:37.068077'
end_time: '2026-08-31T08:28:52.663276'
duration_seconds: 2655.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Specific Antibody Deficiency
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 11
  relevance_assessed: 20
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 5
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0000403
    reported_labels:
    - Common
    ontology_label: Recurrent otitis media
  - term_id: HP:0002099
    reported_labels:
    - 100% (12/12) in pediatric SAD cohort
    ontology_label: Asthma
  - term_id: HP:0003193
    reported_labels:
    - 11/12 pediatric SAD
    ontology_label: Allergic rhinitis
  - term_id: HP:0002110
    reported_labels:
    - Associated with long diagnostic delay
    ontology_label: Bronchiectasis
  - term_id: HP:0005425
    reported_labels:
    - Abnormal antibody level
    ontology_label: Recurrent sinopulmonary infections
  - term_id: GO:0002374
    reported_labels:
    - immunoglobulin production
    ontology_label: GO_0002374
  - term_id: UBERON:0002106
    reported_labels:
    - Immune tissue:** spleen
    ontology_label: spleen
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0002374
    ontology_label: GO_0002374
    replaced_by: GO:0002367
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Specific_Antibody_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Specific_Antibody_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Specific Antibody Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Specific Antibody Deficiency** covering all of the
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

# Specific Antibody Deficiency (SAD / SPAD): A Comprehensive Disease Characteristics Report

**Disease:** Specific Antibody Deficiency (also Specific Polysaccharide Antibody Deficiency, SPAD)
**Category as framed by request:** "Mendelian" — but see Summary; the disease is best classified as a **functional, largely idiopathic primary (predominantly) antibody deficiency**, not a single-gene Mendelian disorder.
**Parent classification:** IUIS-2022 Group III — Predominantly Antibody Deficiencies (PAD)
**Suggested MONDO/ontology anchors:** MONDO "specific antibody deficiency"; ICD-10 **D80.8/D80.9** (other/unspecified immunodeficiency with predominantly antibody defects); MeSH concepts under *Primary Immunodeficiency Diseases* / *Immunologic Deficiency Syndromes*.

---

## Summary

**Specific Antibody Deficiency (SAD), also termed Specific/Selective Polysaccharide Antibody Deficiency (SPAD), is a primary immunodeficiency recognized by the International Union of Immunological Societies and defined by an impaired IgG antibody response to polysaccharide antigens after 23-valent pneumococcal polysaccharide vaccine (PPSV23) challenge, in the setting of otherwise normal total IgG, IgA, IgM, and IgG subclass concentrations and normal responses to protein antigens** ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/); [PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)). The core lesion is a functional failure of the **thymus-independent type-2 (TI-2)** antibody response to bacterial capsular polysaccharides — a response that normally matures only after ~2 years of age, forms no immunologic memory, and uses a restricted IgM/IgG2 isotype repertoire ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)). Because anti-capsular antibody is deficient, encapsulated bacteria (*Streptococcus pneumoniae*, *Haemophilus influenzae* type b) are poorly opsonized, producing the hallmark phenotype of **recurrent sinopulmonary infection** that can progress to bronchiectasis when diagnosis is delayed.

Despite the "Mendelian" label of the research template, SAD is **not a single-gene disorder**. It is a functionally defined, heterogeneous, and largely idiopathic condition — effectively a diagnosis of exclusion ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/); [PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)). The same laboratory picture (impaired polysaccharide IgG with normal total IgG and normal protein-antigen responses) can arise secondarily within other defined immunodeficiencies (IgG subclass deficiency, selective IgA deficiency, Wiskott–Aldrich syndrome, DiGeorge anomaly) and acquired states (post-splenectomy, HIV, lymphoid malignancy), and rare **monogenic inborn errors of immunity (IEI) can phenocopy SAD** ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)). A mechanistic anchor is provided by the **TACI (TNFRSF13B)–NF-κB** pathway: a mouse model carrying the murine equivalent of the human CVID-associated *TNFRSF13B* A181E mutation shows selectively impaired TI-2 (TNP-Ficoll) antibody responses ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).

**Prognosis is generally good.** In children the deficiency may resolve over time ([PMID: 26454312](https://pubmed.ncbi.nlm.nih.gov/26454312/)). Management is tiered: prompt treatment of infections, **pneumococcal conjugate vaccination** (which bypasses the defect by presenting polysaccharide as a T-dependent conjugate), **antibiotic prophylaxis**, and — in refractory or severe cases — **immunoglobulin replacement therapy (IgRT)**, which in an adult SPAD cohort reduced antibiotic courses from a mean of 7.9 to 0.7 per year (p < 0.001) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/); [PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)).

---

## Section 1 — Disease Information

**Overview.** SAD/SPAD is an IUIS-recognized primary immunodeficiency in which patients experience recurrent respiratory infections with **normal immunoglobulins but diminished antibody responses to polysaccharide antigens after PPSV23** ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)). The defining laboratory phenotype is *normal IgA, IgM, total IgG and IgG subclass levels* combined with impaired anti-polysaccharide responses ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)). Diagnosis requires age ≥ 2 years (because the polysaccharide response is physiologically immature before then) and otherwise intact immunity.

> "Specific antibody deficiency is a primary immunodeficiency disease recognized by the International Union of Immunology Societies and defined by recurrent respiratory infections with normal immunoglobulins, but diminished antibody responses to polysaccharide antigens after vaccination with the 23 valent pneumococcal polysaccharide vaccine" ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)).

**Key identifiers.**
- **ICD-10:** D80.8 / D80.9 (immunodeficiency with predominantly antibody defects, other/unspecified).
- **MeSH:** indexed under *Primary Immunodeficiency Diseases* / *Immunologic Deficiency Syndromes* (no unique legacy MeSH term for SPAD specifically).
- **IUIS-2022:** Group III, predominantly antibody deficiencies.
- **OMIM / Orphanet / MONDO:** No single OMIM phenotype number applies because the disorder is functionally (not molecularly) defined. Where a knowledge base requires a MONDO node, use the MONDO term for "specific antibody deficiency."

**Synonyms / alternative names.** Specific Antibody Deficiency (SAD); Specific/Selective Polysaccharide Antibody Deficiency (SPAD); Selective Anti-Polysaccharide Antibody Deficiency; Impaired Polysaccharide Responsiveness; Partial antibody deficiency with normal immunoglobulins.

**Data source type.** The evidence base is **aggregated disease-level** (case series, cohort studies, registry data, and expert reviews) rather than derived from a single EHR dataset; there is a recognized lack of consensus on case definition ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)).

---

## Section 2 — Etiology

**Primary causal mechanism.** SAD is a **functional defect of the antibody response to capsular (TI-2) polysaccharide antigens** ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)). It is largely **idiopathic** and comprises multiple immunologic phenotypes with no single established causal gene ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)).

**Genetic risk factors.** No single Mendelian gene defines primary SAD. However:
- The **TACI (TNFRSF13B)–NF-κB** axis is mechanistically implicated: *TNFRSF13B* is mutated in ~10% of CVID patients, and the murine A144E equivalent of human A181E selectively impairs TI-2 responses ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).
- Defined **monogenic IEI can phenocopy SAD**, presenting with impaired polysaccharide IgG but normal total IgG and normal protein/conjugate responses ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

**Environmental / host risk factors.** Age (immature < 2 years), and a strong association with **atopic/allergic disease** (asthma, allergic rhinitis) — see Section 3. Adult SPAD shows **female predominance (~75%)** ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)). Secondary causes that must be excluded include splenectomy, HIV/AIDS, and lymphoid malignancy ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)).

**Protective factors.** No germline protective variant is established. The strongest *acquired* protective intervention is **pneumococcal conjugate vaccination**, which converts the polysaccharide into a T-dependent antigen and restores protection (Section 12).

**Gene–environment interactions.** Not formally characterized. The clinical picture is best understood as a functional threshold phenomenon in which an intrinsically restricted TI-2 response, host age, and a co-existing allergic diathesis converge to produce recurrent encapsulated-bacterial infection.

---

## Section 3 — Phenotypes

The dominant clinical phenotype is **recurrent sinopulmonary infection** with a striking co-association with allergic disease.

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Recurrent pneumonia | Clinical sign / infection | 91.7% in a pediatric SAD cohort (11/12) | HP:0006532 (Recurrent pneumonia) |
| Recurrent respiratory / sinopulmonary infection | Clinical sign | Defining feature | HP:0002205; HP:0011108 (Recurrent respiratory infections) |
| Recurrent otitis media | Clinical sign | Common | HP:0000403 |
| Chronic/recurrent rhinosinusitis | Clinical sign | Common | HP:0011109 (Chronic sinusitis) |
| Asthma | Comorbid allergic disease | 100% (12/12) in pediatric SAD cohort | HP:0002099 |
| Allergic rhinitis | Comorbid allergic disease | 11/12 pediatric SAD | HP:0003193 |
| Bronchiectasis | Complication (delayed dx) | Associated with long diagnostic delay | HP:0002110 |
| Impaired polysaccharide vaccine response | Laboratory abnormality | Defining | HP:0005425 (Abnormal antibody level) / functional |

In a pediatric cohort of 12 children (mean age 6 y), **recurrent pneumonia predominated (91.7%)**, and **all patients had asthma with 11/12 having allergic rhinitis** ([PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)):

> "recurrent pneumonia predominated (91.7%) as well as other respiratory and invasive infections. All patients with SAD had associated asthma, 11 had allergic rhinitis" ([PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)).

**Onset / severity / progression.** Onset is typically **childhood** (but adult diagnosis is common, median age 45 years in an adult SPAD cohort). Severity is **variable**, ranging from mild recurrent infection to severe/invasive disease. Course is **episodic** (recurrent infections) and can be **progressive** toward bronchiectasis if untreated.

**Impaired-persistence phenotype.** Some children respond normally to PPSV23 acutely but lose protective titers over one year — an "impaired persistence" (memory) phenotype: at one year, **8/20 children showed deficient responses** ([PMID: 25498324](https://pubmed.ncbi.nlm.nih.gov/25498324/)).

**Quality of life.** Primary antibody deficiencies impose substantial physical, psychological, and socioeconomic burden beyond infections and significantly reduce HRQOL ([PMID: 42447994](https://pubmed.ncbi.nlm.nih.gov/42447994/)). In pediatric PID, lower child QoL correlates strongly with higher maternal caregiving burden (r = −0.710, p < 0.001) ([PMID: 42119234](https://pubmed.ncbi.nlm.nih.gov/42119234/)). Validated instruments: SF-36, PedsQL, PROMIS, and disease-specific **PADQOL** and **CVID-QOL** ([PMID: 42447994](https://pubmed.ncbi.nlm.nih.gov/42447994/)).

---

## Section 4 — Genetic / Molecular Information

**Causal genes.** *None established for primary SAD.* The disorder is defined functionally and lacks a robust molecular case definition ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)).

**Mechanistically implicated gene.** **TNFRSF13B (TACI)** — HGNC:18153; encodes Transmembrane Activator and CAML Interactor. A CVID-associated mutation (A181E; murine equivalent A144E) impairs constitutive and ligand-induced **NF-κB** signaling and selectively degrades TI-2 antibody responses ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)). Variant type: **missense**; functional consequence: impaired signaling (hypomorphic / dominant-negative depending on allele). *TNFRSF13B* is mutated in ~10% of CVID patients.

**Monogenic phenocopies.** A 2024 review catalogs genetically defined IEI that initially present with impaired polysaccharide IgG, normal/near-normal IgG, and normal protein/conjugate responses — a picture indistinguishable from primary SAD ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)):

> "genetically defined IEI, that may initially present with an impaired IgG response to polysaccharide antigens, but normal or only slightly decreased IgG levels and normal responses to protein or conjugate vaccine antigens" ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** Not established for isolated SAD. Anti-polysaccharide deficiency does occur in chromosomal/syndromic disorders (e.g., DiGeorge/22q11) as a secondary phenomenon ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)). Allele frequency, somatic-vs-germline, and gnomAD data are not applicable to a functionally defined disease.

---

## Section 5 — Environmental Information

- **Environmental/toxin factors:** No specific toxin, radiation, or occupational exposure is causally established.
- **Lifestyle factors:** Not defined; SAD is intrinsic/functional rather than lifestyle-driven.
- **Infectious agents (triggers of the clinical phenotype, not causes of the deficiency):** encapsulated bacteria, principally ***Streptococcus pneumoniae*** and ***Haemophilus influenzae* type b**, produce the recurrent pneumonia/meningitis/otitis phenotype when anti-capsular antibody is deficient ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)):

> "In infants and young children up to the age of 2 years the antibody response to capsular polysaccharides is inadequate resulting in an increased incidence of diseases such as pneumonia, meningitis, otitis" ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. An **intrinsic/functional defect in the TI-2 (thymus-independent type-2) B-cell response** to bacterial capsular polysaccharides is present (largely idiopathic; in phenocopies, driven by a monogenic lesion such as *TNFRSF13B*/TACI–NF-κB signaling failure) → **leads to** inability to mount adequate anti-capsular IgG (especially IgG2/IgM).
2. Because the TI-2 response normally **develops late in ontogeny, forms no memory, and uses a restricted IgM/IgG2 isotype repertoire** ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)), the defect **results in** low or non-durable serotype-specific anti-pneumococcal IgG on PPSV23 challenge.
3. Deficient anti-capsular antibody **leads to** impaired opsonization and complement-mediated clearance of encapsulated bacteria (*S. pneumoniae*, Hib).
4. Impaired opsonophagocytosis **results in** recurrent/severe **sinopulmonary and invasive infections** (pneumonia, otitis, sinusitis, meningitis) ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/); [PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)).
5. Repeated/chronic airway infection, if diagnosis is delayed, **leads to** airway wall damage and **bronchiectasis** (diagnostic delay 122 vs 24 months in patients with vs without bronchiectasis, p = 0.0042) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).

**Branch (therapeutic bypass):** Presenting the polysaccharide as a **protein-conjugate vaccine** converts the antigen to a **T-dependent** stimulus → germinal-center help → memory + higher-affinity IgG → **restores protection**, bypassing the TI-2 defect ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/); [PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)).

### Molecular / cellular detail

- **Molecular pathway:** TACI (TNFRSF13B) → **NF-κB** signaling supports T-independent antibody responses; impaired signaling degrades TI-2 responses ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).
- **Cell types (CL terms):** B lymphocyte (CL:0000236); marginal-zone B cell (CL:0000844) — the principal responders to TI-2 antigens; plasma cell (CL:0000786); memory B cell (CL:0000787). Neutrophils modulate conjugate-vaccine responses by restraining Tregs (mouse/human data) ([PMID: 42565624](https://pubmed.ncbi.nlm.nih.gov/42565624/)).
- **Immune process (GO terms):** GO:0002374 (immunoglobulin production); T-independent B cell activation / humoral response; GO:0006954 (inflammatory response); GO:0045087 (innate immune response); GO:0007249 (canonical NF-κB signal transduction).
- **Immune system involvement:** immunodeficiency (humoral, functional), with prominent **allergic comorbidity** (asthma, allergic rhinitis) ([PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)).

```
[TI-2 / TACI–NF-κB defect]
        │ leads to
        ▼
[Deficient anti-capsular IgG2/IgM] ── bypassed by ──► [Conjugate vaccine → T-dependent response → protection]
        │ results in
        ▼
[Impaired opsonization of S. pneumoniae / Hib]
        │ results in
        ▼
[Recurrent sinopulmonary + invasive infection]
        │ (if diagnosis delayed) leads to
        ▼
[Bronchiectasis / chronic lung damage]
```

---

## Section 7 — Anatomical Structures Affected

- **Primary organs / systems (respiratory):** paranasal sinuses (UBERON:0001825), middle ear (UBERON:0001756), lungs/bronchi (UBERON:0002048 lung; UBERON:0002185 bronchus). Body system: **respiratory system** (UBERON:0001004).
- **Secondary/complication:** bronchiectatic airways; potential invasive spread (meningitis — meninges UBERON:0002360; bloodstream).
- **Immune tissue:** spleen (UBERON:0002106) and marginal zone are central to TI-2 responses; splenectomy is a recognized secondary cause of anti-polysaccharide deficiency ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)).
- **Tissue/cell level:** respiratory epithelium (repeated infection); B-lymphocyte/marginal-zone B-cell compartment (functional defect).
- **Subcellular (GO cellular component):** plasma membrane receptor signaling (TACI at plasma membrane, GO:0005886); nucleus (NF-κB nuclear translocation, GO:0005634).
- **Lateralization:** typically **bilateral** sinopulmonary involvement (not lateralized).

---

## Section 8 — Temporal Development

- **Onset:** Typically **childhood**; the polysaccharide response is physiologically inadequate before ~2 years, so diagnosis requires age ≥ 2 ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/); [PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)). Adult presentation is common (median diagnosis age 45 y in an adult cohort) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).
- **Onset pattern:** insidious/chronic recurrent infection.
- **Course:** episodic infections; may be **stable, self-resolving, or progressive** to bronchiectasis.
- **Duration / remission:** In children the deficiency **may resolve over time** ([PMID: 26454312](https://pubmed.ncbi.nlm.nih.gov/26454312/)); a distinct "impaired persistence" subset loses titers by one year ([PMID: 25498324](https://pubmed.ncbi.nlm.nih.gov/25498324/)).
- **Critical period / window of opportunity:** early diagnosis prevents bronchiectasis (delay strongly associated with bronchiectasis) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).

---

## Section 9 — Inheritance and Population

**Epidemiology.** Precise SAD-specific incidence/prevalence is not well established because diagnosis depends on vaccine-challenge testing and case definitions vary; SAD is frequently under-recognized. Its parent category — **predominantly antibody deficiencies** — is consistently the **largest IEI group** across registries: 41.3% (38/92) in a Colombian tertiary cohort ([PMID: 39836844](https://pubmed.ncbi.nlm.nih.gov/39836844/)) and 46.3% of 24,879 patients across 30 J-Project countries ([PMID: 36605210](https://pubmed.ncbi.nlm.nih.gov/36605210/)). Among adults with unexplained recurrent/severe encapsulated-bacterial infection, PID was found in 39.8% (95% CI 30.4–48.8), and **SPAD was the most frequent diagnosis (37/47 = 78.7%)** ([PMID: 36285530](https://pubmed.ncbi.nlm.nih.gov/36285530/)):

> "SPAD was the most frequent diagnosis by far (n = 37/47, 78.7%)" ([PMID: 36285530](https://pubmed.ncbi.nlm.nih.gov/36285530/)).

**Inheritance.** No Mendelian inheritance pattern for primary SAD (functional, largely idiopathic). Phenocopying monogenic IEI follow their own (AD/AR/X-linked) patterns ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)). Penetrance, expressivity, anticipation, founder effects, and carrier frequency are **not applicable** to a non-Mendelian functional diagnosis.

**Demographics.**
- **Sex ratio:** adult SPAD is **female-predominant (~75% female; ~3:1 F:M)** ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).
- **Age:** bimodal recognition — childhood onset and adult diagnosis (median 45 y in adults).
- **Geographic/ethnic distribution:** no specific predilection documented; recognition depends on access to vaccine-challenge testing.

---

## Section 10 — Diagnostics

**Core diagnostic test — PPSV23 vaccine challenge.** Measure **serotype-specific IgG before and 4–6 weeks after PPSV23** in patients ≥ 2 years with recurrent infection and otherwise intact immunity. An adequate response to an individual serotype is conventionally **post-immunization titer ≥ 1.3 µg/mL or a ≥ 4-fold rise over baseline** ([PMID: 9723664](https://pubmed.ncbi.nlm.nih.gov/9723664/)):

> "An adequate IgG antibody response to an individual serotype was arbitrarily defined as a postimmunization antibody titer of 1.3 microg/ml or greater or at least four times the baseline value." ([PMID: 9723664](https://pubmed.ncbi.nlm.nih.gov/9723664/))

**Age-adjusted proportion-of-serotypes criteria (pediatric).** A response above 1.3 µg/mL for **> 50% of serotypes** is normal for ages 2–5 years, and for **> 70% of serotypes** in children older than 5 years ([PMID: 25498324](https://pubmed.ncbi.nlm.nih.gov/25498324/)). Responses rise sharply in adults versus all pediatric age groups (7 months–16 years) ([PMID: 9723664](https://pubmed.ncbi.nlm.nih.gov/9723664/)).

**Diagnostics in the conjugate-vaccine (PCV) era.** Widespread PCV13/15/20 reduces the number of *unique* PPSV23 serotypes available for interpretation (11 unique after PCV13; only 4 after PCV20), yet **PPSV23 challenge retains 81–84% diagnostic accuracy** in patients aged 2–65 ([PMID: 39681261](https://pubmed.ncbi.nlm.nih.gov/39681261/)). A validated **18-plex electrochemiluminescence (ECL) assay** benchmarked against WHO ELISA in 164 sera showed **sensitivity 95%, specificity 84%, PPV 84%, NPV 95%** for SPAD ([PMID: 40637813](https://pubmed.ncbi.nlm.nih.gov/40637813/)):

> "the 18-plex ECL assay for SPAD diagnosis showed a sensitivity of 95% and specificity of 84%, positive and negative predictive values of 84% and 95%, respectively" ([PMID: 40637813](https://pubmed.ncbi.nlm.nih.gov/40637813/)).

**Supporting labs.** Normal total IgG, IgA, IgM and IgG subclasses (definitional); consider IgM/IgA anti-pneumococcal assays as adjuncts (do not replace serotype-specific IgG) ([PMID: 33877708](https://pubmed.ncbi.nlm.nih.gov/33877708/)). **Genetic testing** (WES/panels) is warranted when a monogenic IEI phenocopy is suspected — anti-polysaccharide IgG testing is recommended in the initial IEI work-up ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

**Clinical criteria / differential.** No universally accepted quantitative threshold; definition of an "adequate" response (magnitude, number of serotypes) remains controversial ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/); [PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)). **Differential diagnosis:** CVID, IgG subclass deficiency, selective IgA deficiency, XLA, Wiskott–Aldrich, DiGeorge, and secondary causes (splenectomy, HIV, malignancy) — all must be excluded ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)).

**Screening.** Immunoglobulin and vaccine-response testing should be part of the work-up of patients with recurrent sinopulmonary infection, chronic rhinosinusitis, or bronchiectasis of unclear cause; SAD/SPAD is under-diagnosed in these groups ([PMID: 36285530](https://pubmed.ncbi.nlm.nih.gov/36285530/)).

---

## Section 11 — Outcome / Prognosis

- **Overall prognosis:** generally **good**; deficiency may resolve, especially in children ([PMID: 26454312](https://pubmed.ncbi.nlm.nih.gov/26454312/)):

> "Most patients have a good prognosis. The deficiency may resolve over time, especially in children." ([PMID: 26454312](https://pubmed.ncbi.nlm.nih.gov/26454312/))

- **Key complication:** **bronchiectasis**, driven by recurrent infection and **diagnostic delay** (122 vs 24 months with vs without bronchiectasis, p = 0.0042) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).
- **Treatment outcomes:** IgRT markedly reduces infection burden (mean antibiotic courses 7.9 → 0.7 per year, p < 0.001) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)). Patients diagnosed after a single severe infection had **no relapse over median 85-month follow-up** ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).
- **Morbidity / QoL:** significant HRQOL burden; caregiver burden in pediatric disease ([PMID: 42447994](https://pubmed.ncbi.nlm.nih.gov/42447994/); [PMID: 42119234](https://pubmed.ncbi.nlm.nih.gov/42119234/)).
- **Prognostic factors:** infection history/severity, presence of bronchiectasis, and (for conjugate-vaccine protection) IgG subclass status and IgG2 at diagnosis ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/)).

---

## Section 12 — Treatment

**Tiered management ladder:** (1) prompt treatment of infections → (2) pneumococcal **conjugate vaccination** → (3) **antibiotic prophylaxis** → (4) **immunoglobulin replacement (IVIG/SCIG)** in refractory/severe cases ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/); [PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).

> "Specific antibody deficiency is managed clinically with close follow-up and prompt treatment of infections, antibiotic prophylaxis, or immune globulin therapy." ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/))

**Pneumococcal conjugate vaccine (PCV).** Because conjugate vaccines present polysaccharide as a T-dependent protein-linked antigen, they bypass the TI-2 defect. In primary humoral immunodeficiency (n = 29) given PCV13, protection was **71.4%, 66.7%, and 56.0% at 1, 6, and 12 months**; IgG subclass deficiency, Ig replacement, and higher IgG2 at diagnosis predicted long-term protection ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/)). Conjugate vaccination was favorable in **11/12** pediatric SAD patients ([PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/)). Suggested NCIT: *Pneumococcal Conjugate Vaccine*.

> "71.4%, 66.7% and 56.0% of the patients were protected at one, six and twelve months respectively" ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/)).

**Immunoglobulin replacement therapy (IgRT).** In adult SPAD, 40% received IgRT with a fall in mean antibiotic courses from 7.9 to 0.7 per year (p < 0.001) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)). Route (IVIG vs SCIG) did not significantly affect pediatric QoL ([PMID: 42119234](https://pubmed.ncbi.nlm.nih.gov/42119234/)). Suggested NCIT: *Intravenous Immunoglobulin Therapy*, *Subcutaneous Immunoglobulin*.

**Antibiotic prophylaxis.** Mainstay for reducing recurrent infection ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)).

**Personalized strategy.** Individualized because of the absence of a robust case definition and lack of controlled trials ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)). Gene/cell/RNA-based therapies are **not applicable** to primary SAD (relevant only to specific monogenic phenocopies).

| Treatment tier | Intervention | Evidence / effect | NCIT-type term |
|---|---|---|---|
| 1 | Prompt antibiotic treatment of acute infection | Standard of care | Antibiotic Therapy |
| 2 | Pneumococcal conjugate vaccine (PCV13/15/20) | Bypasses TI-2 defect; 56–71% protected over 12 mo (PID) | Pneumococcal Conjugate Vaccine |
| 3 | Antibiotic prophylaxis | Reduces recurrent infection | Antibiotic Prophylaxis |
| 4 | IgRT (IVIG/SCIG) | Antibiotic courses 7.9 → 0.7/yr (p<0.001) | Immunoglobulin Replacement Therapy |

---

## Section 13 — Prevention

- **Primary prevention:** not applicable (intrinsic functional defect); focus is on infection prevention via **conjugate vaccination** and prophylactic antibiotics ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/); [PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)).
- **Secondary prevention:** early recognition and vaccine-challenge testing to prevent bronchiectasis (delay strongly linked to bronchiectasis) ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)); immunologic evaluation of at-risk groups (recurrent sinopulmonary infection, CRS, unexplained encapsulated-bacterial infection) ([PMID: 36285530](https://pubmed.ncbi.nlm.nih.gov/36285530/)).
- **Tertiary prevention:** IgRT, airway clearance, and surveillance to prevent progression/complications.
- **Immunization:** conjugate pneumococcal and Hib vaccines (T-dependent) are the cornerstone.
- **Counseling:** genetic counseling relevant only where a monogenic phenocopy is identified ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of model species:** *Mus musculus* (NCBI:txid10090) is the principal experimental species.
- **Orthologous gene:** murine *Tnfrsf13b* (TACI) models the human TI-2 defect ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).
- **Natural disease in other species / veterinary relevance / zoonosis:** No naturally occurring animal counterpart of isolated human SAD/SPAD is documented in the reviewed literature. Not zoonotic. Not applicable.
- **Comparative/evolutionary biology:** the TI-2 anti-capsular response and TACI–NF-κB signaling are conserved between mouse and human, enabling mechanistic modeling ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).

---

## Section 15 — Model Organisms

- **Model type:** mammalian (mouse).
- **Genetic model:** transgenic mice expressing the TACI **A144E** mutant (murine equivalent of human *TNFRSF13B* A181E) on a **TACI−/−** background ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).
- **Phenotype recapitulation:** low serum IgA and **significantly impaired antibody responses to the TI-2 antigen TNP-Ficoll**, with impaired B-cell proliferation and IgG1/IgA secretion and impaired constitutive/ligand-induced NF-κB signaling ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)):

> "Transgenic mice expressing the A144E mutant on TACI(-/-) background had low serum IgA levels and significantly impaired antibody responses to the type II T-independent antigen TNP-Ficoll." ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/))

- **Additional mechanistic model:** neutrophil-depletion mouse studies show neutrophils are required for protective conjugate-vaccine antibody responses by restraining Tregs — relevant to why PCV works and how the response is regulated ([PMID: 42565624](https://pubmed.ncbi.nlm.nih.gov/42565624/)).
- **Limitations:** these models capture the **TI-2 response defect** but not the full heterogeneity or idiopathic nature of primary human SAD; they primarily model CVID-associated TACI biology.

---

## Mechanistic Model / Interpretation

SAD/SPAD is best understood as a **functional failure at one node of the humoral immune system — the thymus-independent type-2 response to bacterial capsular polysaccharides.** This response is intrinsically fragile: it matures late (inadequate < 2 years), forms no memory, and uses a narrow IgM/IgG2 repertoire ([PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)). When it fails, anti-capsular antibody is insufficient to opsonize *S. pneumoniae* and Hib, producing recurrent sinopulmonary infection. The two therapeutic levers both make sense in this framework: (1) **conjugate vaccines** re-route the antigen through T-dependent germinal-center help, restoring durable IgG ([PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/)); and (2) **IgRT** supplies the missing antibody directly ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).

The disease's "Mendelian" framing is misleading. Primary SAD has **no single causal gene** and is a diagnosis of exclusion ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/); [PMID: 8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/)). The genetic dimension enters in two ways: as **mechanistic insight** (TACI–NF-κB governs TI-2 responses; [PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)) and as **differential diagnosis** (monogenic IEI can phenocopy SAD and should be sought when clinically indicated; [PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/) | *Diagnosis and management of Specific Antibody Deficiency* | Definition + management ladder |
| [28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/) | *SAD: Controversies in Diagnosis and Management* | Normal Ig phenotype; lack of consensus |
| [8167745](https://pubmed.ncbi.nlm.nih.gov/8167745/) | *Anti-capsular polysaccharide antibody deficiency states* | TI-2 immunobiology; secondary causes |
| [9723664](https://pubmed.ncbi.nlm.nih.gov/9723664/) | *Influence of age on S. pneumoniae vaccine response* | 1.3 µg/mL / 4-fold thresholds; age dependence |
| [25498324](https://pubmed.ncbi.nlm.nih.gov/25498324/) | *SAD with normal Ig in children* | Age-adjusted pediatric criteria; impaired persistence |
| [27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/) | *SAD: PID associated to respiratory allergy* | Recurrent pneumonia 91.7%; asthma/rhinitis; PCV benefit |
| [36285530](https://pubmed.ncbi.nlm.nih.gov/36285530/) | *High frequency of SPAD in adults* | SPAD = 78.7% of PIDs; PID freq 39.8% |
| [26454312](https://pubmed.ncbi.nlm.nih.gov/26454312/) | *Specific Antibody Deficiencies* | Good prognosis; may resolve |
| [38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/) | *Monogenic IEI with impaired polysaccharide IgG* | Phenocopies; test anti-PS IgG |
| [19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/) | *Murine A181E TACI mutation* | Mouse model; TACI–NF-κB; TNP-Ficoll |
| [34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/) | *PCV13 in primary humoral immunodeficiency* | Conjugate-vaccine protection over 12 mo |
| [40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/) | *55 adult SPAD patients* | Female 75%; delay/bronchiectasis; IgRT efficacy |
| [39681261](https://pubmed.ncbi.nlm.nih.gov/39681261/) | *Functional testing in the Prevnar 20 era* | PPSV23 accuracy 81–84% in PCV era |
| [40637813](https://pubmed.ncbi.nlm.nih.gov/40637813/) | *Multiplex ECL assay for SPAD* | Sens 95% / Spec 84% vs WHO ELISA |
| [39836844](https://pubmed.ncbi.nlm.nih.gov/39836844/) | *Colombian IEI service* | PAD = largest IEI group (41.3%) |
| [36605210](https://pubmed.ncbi.nlm.nih.gov/36605210/) | *J Project 30 countries* | PAD = 46.3% of 24,879 patients |
| [42447994](https://pubmed.ncbi.nlm.nih.gov/42447994/) | *Shared decision-making / HRQOL in IEI* | QoL burden; PADQOL/CVID-QOL |
| [42119234](https://pubmed.ncbi.nlm.nih.gov/42119234/) | *QoL and care burden SCIG/IVIG* | r = −0.710 child QoL vs caregiver burden |
| [42565624](https://pubmed.ncbi.nlm.nih.gov/42565624/) | *Neutrophils and PCV responses* | Neutrophil–Treg regulation of conjugate response |
| [33877708](https://pubmed.ncbi.nlm.nih.gov/33877708/) | *IgM/IgA anti-PnPS assays* | Serotype-specific IgG remains the standard |

---

## Limitations and Knowledge Gaps

1. **No molecular case definition.** SAD is functionally defined, and thresholds for an "adequate" polysaccharide response (magnitude and number of serotypes) remain controversial and age-dependent ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/); [PMID: 9723664](https://pubmed.ncbi.nlm.nih.gov/9723664/)).
2. **Uncertain incidence/prevalence.** No robust population-level SAD-specific rates exist; estimates are inferred from PAD-category registries and at-risk cohorts ([PMID: 39836844](https://pubmed.ncbi.nlm.nih.gov/39836844/); [PMID: 36605210](https://pubmed.ncbi.nlm.nih.gov/36605210/)).
3. **PCV-era diagnostic erosion.** Universal conjugate vaccination reduces interpretable unique PPSV23 serotypes; although accuracy holds (81–84%), standardization is evolving ([PMID: 39681261](https://pubmed.ncbi.nlm.nih.gov/39681261/); [PMID: 40637813](https://pubmed.ncbi.nlm.nih.gov/40637813/)).
4. **Small cohorts, few controlled trials.** Much clinical evidence rests on modest case series; treatment is individualized ([PMID: 28588580](https://pubmed.ncbi.nlm.nih.gov/28588580/)).
5. **Genetic architecture underexplored.** The boundary between idiopathic SAD and monogenic phenocopies is not resolved; systematic genetic testing thresholds are undefined ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/)).

---

## Proposed Follow-up Experiments / Actions

1. **Harmonize the case definition:** multi-center consensus on age-adjusted, PCV-era serotype thresholds, ideally anchored to the validated 18-plex ECL assay against WHO ELISA ([PMID: 40637813](https://pubmed.ncbi.nlm.nih.gov/40637813/); [PMID: 39681261](https://pubmed.ncbi.nlm.nih.gov/39681261/)).
2. **Prospective natural-history registry** to quantify SAD-specific incidence/prevalence, resolution rates in children, and bronchiectasis risk as a function of diagnostic delay ([PMID: 40097777](https://pubmed.ncbi.nlm.nih.gov/40097777/)).
3. **Genetic yield study:** systematically apply WES/gene panels (including *TNFRSF13B*) to SAD-phenotype patients to define the proportion with identifiable monogenic phenocopies ([PMID: 38933494](https://pubmed.ncbi.nlm.nih.gov/38933494/); [PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)).
4. **Randomized/controlled comparison** of antibiotic prophylaxis vs IgRT vs conjugate-vaccine-only strategies stratified by infection severity and bronchiectasis status ([PMID: 32654695](https://pubmed.ncbi.nlm.nih.gov/32654695/)).
5. **Mechanistic follow-up** on the allergy–SAD association and on neutrophil/Treg regulation of conjugate-vaccine responses to identify predictors of durable protection ([PMID: 27614984](https://pubmed.ncbi.nlm.nih.gov/27614984/); [PMID: 42565624](https://pubmed.ncbi.nlm.nih.gov/42565624/); [PMID: 34290713](https://pubmed.ncbi.nlm.nih.gov/34290713/)).

---

*Report compiled from 15 confirmed findings across 5 investigation iterations and 72 reviewed papers. Evidence types: predominantly human clinical (cohorts, case series, registries) plus one mouse mechanistic model ([PMID: 19605846](https://pubmed.ncbi.nlm.nih.gov/19605846/)) and mouse/human conjugate-vaccine immunobiology ([PMID: 42565624](https://pubmed.ncbi.nlm.nih.gov/42565624/)).*


## Artifacts

- [OpenScientist final report](Specific_Antibody_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Specific_Antibody_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000403` (1 mention) - the report calls it "Common"; HP calls it **Recurrent otitis media**
- `HP:0002099` (1 mention) - the report calls it "100% (12/12) in pediatric SAD cohort"; HP calls it **Asthma**
- `HP:0003193` (1 mention) - the report calls it "11/12 pediatric SAD"; HP calls it **Allergic rhinitis**
- `HP:0002110` (1 mention) - the report calls it "Associated with long diagnostic delay"; HP calls it **Bronchiectasis**
- `HP:0005425` (1 mention) - the report calls it "Abnormal antibody level"; HP calls it **Recurrent sinopulmonary infections**
- `GO:0002374` (1 mention) - the report calls it "immunoglobulin production"; GO calls it **GO_0002374**
- `UBERON:0002106` (1 mention) - the report calls it "Immune tissue:** spleen"; UBERON calls it **spleen**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0002374` (GO_0002374) (1 mention) - replaced by `GO:0002367`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007249` (1 mention) - the report calls it "canonical NF-κB signal transduction"; GO calls it **canonical NF-kappaB signal transduction**