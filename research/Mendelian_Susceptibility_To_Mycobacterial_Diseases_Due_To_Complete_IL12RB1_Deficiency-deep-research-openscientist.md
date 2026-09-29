---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-18T17:35:02.000317'
end_time: '2026-09-18T17:51:20.344283'
duration_seconds: 978.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mendelian Susceptibility To Mycobacterial Diseases Due To Complete
    IL12RB1 Deficiency
  mondo_id: MONDO:0013955
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 9
  relevance_assessed: 26
  on_topic: 25
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 4
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0013955
    reported_labels:
    - MONDO
    ontology_label: Mendelian susceptibility to mycobacterial diseases due to complete
      IL12RB1 deficiency
  - term_id: HP:0032256
    reported_labels:
    - Tuberculosis
    ontology_label: Unusual Histoplasma capsulatum infection
  - term_id: UBERON:0002097
    reported_labels:
    - Skin and subcutaneous tissue
    ontology_label: skin of body
  - term_id: UBERON:0000167
    reported_labels:
    - Oropharyngeal mucosa
    ontology_label: oral cavity
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_IL12RB1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_IL12RB1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mendelian Susceptibility To Mycobacterial Diseases Due To Complete IL12RB1 Deficiency
- **MONDO ID:** MONDO:0013955 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mendelian Susceptibility To Mycobacterial Diseases Due To Complete IL12RB1 Deficiency** covering all of the
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

# Mendelian Susceptibility to Mycobacterial Disease due to Complete IL-12Rβ1 Deficiency — Comprehensive Disease Report

**Disease:** Mendelian Susceptibility To Mycobacterial Diseases Due To Complete IL12RB1 Deficiency
**MONDO ID:** MONDO:0013955 · **Gene:** *IL12RB1* (HGNC:5971) · **Locus:** 19q13.11 · **Inheritance:** Autosomal recessive
**Category:** Mendelian inborn error of immunity (inborn error of IFN-γ immunity)

---

## Summary

Complete IL-12 receptor β1 (IL-12Rβ1) deficiency is an autosomal-recessive inborn error of immunity and the **single most common genetic cause of Mendelian Susceptibility to Mycobacterial Disease (MSMD)**. It is caused by biallelic loss-of-function variants in *IL12RB1* (19q13.11), which encodes the β1 chain shared by the receptors for interleukin-12 (IL-12) and interleukin-23 (IL-23). Loss of this chain simultaneously abolishes IL-12-driven IFN-γ production by T and NK cells and IL-23-driven IL-17 immunity. The functional consequence is a narrow but characteristic clinical syndrome: childhood-onset disease caused by weakly virulent mycobacteria — chiefly *Mycobacterium bovis* BCG (vaccine strain) and environmental/non-tuberculous mycobacteria — and by non-typhoidal *Salmonella*, with mucocutaneous candidiasis in roughly one quarter of patients ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/), [PMID: 24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/)).

The largest characterization to date — an international survey of 141 patients from 102 kindreds across 30 countries — established that IL-12Rβ1 deficiency has a **comparatively favorable prognosis** (70% survival, mean age at follow-up 12.7 ± 9.8 years) and **incomplete clinical penetrance** (27% of genetically affected siblings remained asymptomatic) ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)). Mechanistically the disorder is classified among MSMD genes that impair the **production** of IFN-γ (with *IL12B, IRF8, ISG15, NEMO*), as opposed to those that impair the **response** to IFN-γ (*IFNGR1, IFNGR2, STAT1*, etc.) — a distinction that explains why adjunctive recombinant IFN-γ, which bypasses the receptor block, is clinically useful ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)).

A crucial diagnostic caveat is that affected individuals are **otherwise healthy with normal routine hematological and immunological tests**; diagnosis therefore requires targeted functional assays (defective cellular responses to IL-12; absent IL-12Rβ1 surface expression) and genetic confirmation ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/), [PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/)). Management centers on prolonged pathogen-directed antimycobacterial/antibacterial therapy, adjunctive recombinant IFN-γ, avoidance of the live BCG vaccine, and hematopoietic stem cell transplantation (HSCT) for severe or refractory disease, which achieves markedly higher antimycobacterial cure rates ([PMID: 31367980](https://pubmed.ncbi.nlm.nih.gov/31367980/), [PMID: 41748971](https://pubmed.ncbi.nlm.nih.gov/41748971/)). An *Il12rb1*-deficient mouse recapitulates disseminated BCG susceptibility and is being used to dissect the residual, IFN-γ-independent protective immunity that underlies the disorder's low penetrance ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/)).

---

## 1. Disease Information

**Overview.** Complete IL-12Rβ1 deficiency is an isolated (non-syndromic) inborn error of IFN-γ immunity that produces selective predisposition to clinical disease from weakly virulent intracellular pathogens — principally mycobacteria (BCG, non-tuberculous mycobacteria [NTM], and, less often, *M. tuberculosis*) and non-typhoidal *Salmonella* — in individuals who are otherwise healthy and immunocompetent against most other microbes ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/), [PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)). It is the most common of the ~21–31 recognized MSMD genetic etiologies.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013955 |
| OMIM (phenotype) | #614891 (Immunodeficiency 30 / MSMD, IL12RB1) |
| OMIM (gene) | *IL12RB1* 601604 |
| Gene / HGNC | *IL12RB1* / HGNC:5971 |
| Orphanet | MSMD (disease group) |
| MeSH | Related to "Mycobacterium Infections" / primary immunodeficiency terms |
| ICD-10 | D84.8/D84.9 (other/unspecified immunodeficiency) |
| ICD-11 | 4A00.x (inborn errors of immunity) |

**Synonyms / alternative names.** IL-12Rβ1 deficiency; interleukin-12 receptor β1 chain deficiency; IL12RB1 deficiency; MSMD due to IL-12Rβ1 deficiency; Immunodeficiency 30.

**Information source.** The disease-level knowledge here derives predominantly from **aggregated disease-level resources and cohort studies** — most notably the international 141-patient survey ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)), the earlier 41-patient cohort ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/)), and multiple national cohorts (Iran, Mexico, China) — supplemented by individual case reports.

---

## 2. Etiology

**Disease causal factor — genetic.** The disease is monogenic: biallelic (homozygous or compound-heterozygous) loss-of-function variants in *IL12RB1* that abolish surface expression of the receptor β1 chain and eliminate cellular responsiveness to IL-12 (and IL-23). Direct proof of causality comes from complementation: "*Transfection of the patients' T cells with wild-type IL12RB1 restored IL-12Rbeta1 expression and function*" ([PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/)).

**Genetic risk factors.** The causal variants are the risk factor. Because the disorder is recessive, the principal population-level risk amplifiers are **consanguinity** and **founder alleles**. Parental consanguinity is repeatedly documented in MSMD/IL-12Rβ1 cohorts from high-consanguinity regions (e.g., Iran, Turkey) ([PMID: 32602053](https://pubmed.ncbi.nlm.nih.gov/32602053/), [PMID: 30968642](https://pubmed.ncbi.nlm.nih.gov/30968642/)). The closely related IL-12p40 (*IL12B*) deficiency demonstrates recurrent founder alleles affecting 25 of 30 kindreds, supporting an analogous pattern for *IL12RB1* ([PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)).

**Environmental risk factor — the essential trigger.** Genotype alone is insufficient to cause overt disease; an **environmental/infectious exposure is the obligate second hit**. The dominant trigger is **BCG vaccination** (live attenuated *M. bovis*): among vaccinees in the near-phenocopy IL-12p40 deficiency, BCG disease occurred in 97.5% ([PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)); in the international IL-12Rβ1 cohort, BCG was the most frequent causative organism (n=65) ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)). Environmental non-tuberculous mycobacteria and *Salmonella* exposure are the other triggers.

**Protective factors.** No specific protective allele is established. However, **residual IFN-γ-independent antimycobacterial immunity** clearly protects a subset of genetically affected individuals, accounting for asymptomatic siblings and the low recurrence rate ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/), [PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)). At the public-health level, **avoiding BCG vaccination** in at-risk families is strongly protective against the most common disease trigger.

**Gene–environment interaction.** This disorder is a paradigm of gene × environment interaction: a fixed germline lesion (loss of IL-12/IL-23 signaling) becomes clinically manifest only upon encounter with specific weakly virulent intracellular pathogens, while the same individuals resist most other microbes ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/)).

---

## 3. Phenotypes

The clinical picture is dominated by infection. Frequencies below are drawn chiefly from the 141-patient international survey ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)) and the candidiasis series ([PMID: 24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/)).

| Phenotype | Type | Onset | Frequency | Suggested HPO term |
|---|---|---|---|---|
| BCG disease (BCGitis/BCGosis, local→disseminated) | Clinical sign / infection | Infancy (post-vaccination) | Most common organism (n=65 of causative isolates) | HP:0002841 (Recurrent mycobacterial infections); HP:0032262 (BCG vaccine adverse event) |
| Non-tuberculous / environmental mycobacterial disease | Infection | Childhood | n=9 | HP:0002841 |
| *M. tuberculosis* disease | Infection | Childhood | n=4 | HP:0032256 (Tuberculosis) |
| Non-typhoidal *Salmonella* infection (often disseminated) | Infection | Childhood | 22 of the 24 non-mycobacterial probands | HP:0002718 (Recurrent bacterial infections) |
| Mucocutaneous candidiasis (mostly oropharyngeal) | Infection / mucosal sign | Median 1.5 yr (earliest infection type) | ~23–25% (33/141) | HP:0002728 (Chronic mucocutaneous candidiasis) |
| Lymphadenitis / lymphadenopathy | Clinical sign | Childhood | Common | HP:0002716 (Lymphadenopathy) |
| Hepatomegaly / hepatosplenic involvement | Clinical sign | Childhood | Common in disseminated disease | HP:0002240 (Hepatomegaly) |
| Fever, failure to thrive / growth retardation | Symptom / sign | Childhood | Frequent with disseminated disease | HP:0001945; HP:0001510 |

**Onset.** First infection occurs at a **mean age of 2.4 years**; candidiasis, when present, tends to be the earliest manifestation (median 1.5 yr) ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/), [PMID: 24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/)).

**Severity / progression.** Highly **variable** — ranging from localized BCGitis to fatal disseminated disease. A hallmark is that **mycobacterial infections generally do not recur** after successful treatment, distinguishing this from IFN-γ-receptor defects ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/)); *Salmonella*, by contrast, recurs more often (in the parallel IL-12p40 disorder, salmonellosis recurred in 36.4% vs 25% mycobacterial recurrence) ([PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)).

**Quality-of-life impact.** Not formally measured with standardized instruments (EQ-5D/SF-36) in the literature reviewed. Morbidity derives from repeated hospitalizations, prolonged multidrug therapy, surgical drainage of lymphadenitis, and, in severe cases, disseminated organ involvement.

---

## 4. Genetic / Molecular Information

**Causal gene.** *IL12RB1* (OMIM 601604; HGNC:5971), 19q13.11, encoding the IL-12 receptor β1 chain shared by the IL-12 (IL-12Rβ1/IL-12Rβ2) and IL-23 (IL-12Rβ1/IL-23R) receptor complexes.

**Variant classification and types.** Reported pathogenic variants are diverse and include **missense, nonsense, frameshift, and splice-site** alleles. Examples from the reviewed literature:
- Homozygous **missense** preventing receptor expression and abolishing IL-12 responses ([PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/)).
- **Nonsense** Q285X (c.853C>T, exon 9) causing loss of surface expression ([PMID: 19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/)).
- **Splice-site** c.783+1G>A (homozygous), disease-causing ([PMID: 30968642](https://pubmed.ncbi.nlm.nih.gov/30968642/)).
- Homozygous missense or nonsense alleles in three Iranian patients that "*caused the IL-12Rβ1 protein not to be expressed on the cell membrane and completely abolished the cellular response to recombinant IL-12*" ([PMID: 29256176](https://pubmed.ncbi.nlm.nih.gov/29256176/)).

All are classified **pathogenic** under ACMG/AMP criteria on the basis of null functional effect, segregation, and rarity.

**Functional consequence.** **Complete loss of function** (null) — absent surface receptor and abolished IL-12/IL-23 signaling. There is no gain-of-function or dominant-negative mechanism; heterozygous carriers are asymptomatic.

**Origin.** **Germline**, biallelic. No somatic contribution.

**Allele frequency.** Individual pathogenic alleles are very rare in gnomAD; disease arises through recessive inheritance, enriched by consanguinity and country-specific founder alleles ([PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/), [PMID: 32602053](https://pubmed.ncbi.nlm.nih.gov/32602053/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier gene or epigenetic mechanism is established. The disorder is a point-lesion Mendelian condition, not a chromosomal/structural disorder. The residual protective immunity driving low penetrance is likely determined by redundant, partly IFN-γ-independent pathways rather than a single modifier locus ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/)).

---

## 5. Environmental Information

**Infectious agents (central to the disease).**
- ***Mycobacterium bovis* BCG** (live vaccine strain) — the dominant trigger and most frequent isolate ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)).
- **Non-tuberculous / environmental mycobacteria** (e.g., *M. avium* complex) — [PMID: 23726680](https://pubmed.ncbi.nlm.nih.gov/23726680/).
- ***Mycobacterium tuberculosis*** — less common but reported.
- **Non-typhoidal *Salmonella*** (e.g., *S.* Typhimurium), frequently disseminated ([PMID: 41771439](https://pubmed.ncbi.nlm.nih.gov/41771439/)).
- ***Candida*** species — mucocutaneous candidiasis in ~25% ([PMID: 24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/)).
- More rarely other intramacrophagic bacteria, fungi (e.g., *Histoplasma*), parasites, and perhaps a few viruses ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/), [PMID: 36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/)).

**Non-infectious environmental / lifestyle factors.** None causative. The single most consequential "environmental" exposure is a medical intervention — **BCG vaccination** — which precipitates disease in the majority of vaccinated patients. No toxin, occupational, or dietary factor is implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *IL12RB1*** (missense/nonsense/frameshift/splice) **leads to** absent or non-functional IL-12Rβ1 chain on the cell surface ([PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/), [PMID: 29256176](https://pubmed.ncbi.nlm.nih.gov/29256176/)).
2. Loss of the shared β1 chain **results in** simultaneous inability to assemble functional **IL-12 receptors** (IL-12Rβ1/β2) **and IL-23 receptors** (IL-12Rβ1/IL-23R) on T and NK cells.
3. **Branch A (IL-12 arm):** Absent IL-12 signaling **leads to** failure of STAT4 activation in T/NK cells **→** markedly reduced **IFN-γ production** ([PMID: 32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/)).
4. Deficient IFN-γ **results in** impaired activation of infected **macrophages** and defective killing of intracellular mycobacteria and *Salmonella* **→** poorly controlled, potentially disseminating infection with weakly virulent mycobacteria and non-typhoidal *Salmonella* ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)).
5. **Branch B (IL-23 arm):** Absent IL-23 signaling **leads to** impaired **IL-17/Th17 immunity** at mucosal surfaces **→** **mucocutaneous candidiasis** in ~25% of patients (inferred mechanism, strongly supported) ([PMID: 24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/)).
6. **Residual protection (why penetrance is incomplete):** Partly IFN-γ-independent and IL-12/IL-23-independent antimycobacterial pathways **provide** residual immunity, so a substantial fraction of genotype-positive individuals remain asymptomatic and mycobacterial disease seldom recurs (demonstrated in patients; dissected in *Il12rb1*-KO mice) ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/), [PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)).

```
 IL12RB1 biallelic LOF
          │
   no surface IL-12Rβ1
          │
 ┌────────┴─────────┐
 │                  │
IL-12R absent     IL-23R absent
 │                  │
↓ STAT4           ↓ Th17 / IL-17
 │                  │
↓ IFN-γ           mucosal antifungal defect
 │                  │
macrophage not     mucocutaneous
activated          candidiasis (~25%)
 │
mycobacteria & Salmonella
not killed → disseminated infection
          │
 [residual IFN-γ-independent immunity]
   → low penetrance, low recurrence
```

**Molecular pathway (upstream → downstream).** IL-12/IL-23 → IL-12Rβ1 (receptor) → JAK–STAT4 → **IFN-γ** → IFN-γR/STAT1 → macrophage antimycobacterial program. The lesion is **upstream**, at the receptor level of IFN-γ *production*; the downstream IFN-γ *response* machinery is intact — which is precisely why exogenous recombinant IFN-γ can bypass the block ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)).

**Classification.** *IL12RB1* belongs to the MSMD genes that impair the **production** of IFN-γ: "*These disorders impair the production of (IL12B, IL12RB1, IRF8, ISG15, NEMO) or the response to (IFNGR1, IFNGR2, STAT1, IRF8, CYBB) IFN-γ*" ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)). Recent genetics show "*both IL-12 and IL-23 are required for optimal levels of IFN-γ*" ([PMID: 32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/)).

**Immune system involvement.** This is a pure **immunodeficiency** (not autoimmune/autoinflammatory) of cell-mediated, granulomatous antimycobacterial immunity. Cell types involved: **T lymphocytes (CL:0000084)**, **natural killer cells (CL:0000623)**, **Th17 cells (CL:0000899)**, and **macrophages (CL:0000235)**. Biological processes: IFN-γ production (GO:0032609), positive regulation of IFN-γ production (GO:0032729), IL-12-mediated signaling (GO:0035722), IL-23-mediated signaling (GO:0038155), T-helper 17 cell differentiation (GO:0072539), macrophage activation involved in immune response (GO:0002281). Cellular component: plasma-membrane cytokine receptor complex (GO:0005886).

**Biomarker note.** Serum **neopterin remains elevated** even with complete absence of IFN-γ activity, so neopterin cannot be used to diagnose IFN-γ/IL-12/IL-23-pathway MSMD ([PMID: 16339068](https://pubmed.ncbi.nlm.nih.gov/16339068/)).

---

## 7. Anatomical Structures Affected

- **Primary body system:** immune/hematopoietic system (UBERON:0002405 immune system).
- **Lymphoreticular:** lymph nodes (UBERON:0000029) — lymphadenitis, especially axillary post-BCG; spleen (UBERON:0002106); liver (UBERON:0002107) — hepatomegaly/hepatosplenic dissemination.
- **Skin and subcutaneous tissue** (UBERON:0002097) — BCG injection-site nodules, fistulae, cutaneous NTM disease.
- **Lung** (UBERON:0002048) — mycobacterial pulmonary disease.
- **Bone marrow / disseminated reticuloendothelial involvement** in severe cases.
- **Oropharyngeal mucosa** (UBERON:0000167) — candidiasis.
- **Cell/tissue level:** macrophages within granulomas; T and NK lymphocytes (functional defect, not structural). **Subcellular:** plasma membrane (site of the missing receptor); JAK–STAT signaling in the cytosol.
- **Lateralization:** typically follows inoculation/dissemination pattern — e.g., ipsilateral (to BCG injection) axillary lymphadenitis initially, later bilateral/disseminated.

---

## 8. Temporal Development

- **Onset:** pediatric, typically **infancy to early childhood**; mean age at first infection **2.4 years**, frequently precipitated by BCG vaccination in the first months of life ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)). Onset pattern is usually **subacute** (progressive lymphadenitis/nodule) but can be acute-disseminated.
- **Progression:** variable — local disease may resolve with therapy, or progress to disseminated, life-threatening infection. Mycobacterial disease characteristically **does not recur** after cure; *Salmonella* recurs more often ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/), [PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)).
- **Course:** episodic infections superimposed on a **chronic lifelong** underlying susceptibility. Susceptibility tends to attenuate with age (adults are less prone to new mycobacterial episodes).
- **Critical period:** the peri-vaccination window in infancy is the key vulnerable/interventional period — avoiding live BCG prevents the commonest trigger.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (complete deficiency requires biallelic LOF).
- **Penetrance:** **incomplete / low** — 8/29 genetically affected siblings (27%) remained asymptomatic in the international survey ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)); most MSMD defects "*do not show complete clinical penetrance*" ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)).
- **Expressivity:** highly **variable**, from asymptomatic to fatal disseminated disease ([PMID: 24064560](https://pubmed.ncbi.nlm.nih.gov/24064560/)).
- **Founder effects / consanguinity:** major drivers; recurrent country-specific alleles and high parental consanguinity in cohorts from Iran, Turkey, and the Middle East ([PMID: 32602053](https://pubmed.ncbi.nlm.nih.gov/32602053/), [PMID: 30968642](https://pubmed.ncbi.nlm.nih.gov/30968642/)); founder effects are explicitly documented for the near-phenocopy IL-12p40 deficiency ([PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)).
- **Epidemiology:** overall a **rare** disorder; precise prevalence/incidence are not established, but IL-12Rβ1 deficiency is the **most common single genetic etiology of MSMD** ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/), [PMID: 36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/)). Diagnoses cluster in **BCG-vaccinating, high-consanguinity** populations.
- **Sex ratio / age distribution:** no strong sex bias intrinsic to the recessive disorder; cohort male predominance (e.g., 64% male in the Mexican cohort) likely reflects ascertainment ([PMID: 36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/)). Age distribution skews pediatric.
- **Anticipation / mosaicism:** not features of this disorder.

---

## 10. Diagnostics

**Key caveat:** patients are "*otherwise healthy individuals with no overt abnormalities in routine hematological and immunological tests*" ([PMID: 25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/)). Routine CBC, immunoglobulins, and lymphocyte subsets are typically normal — so a **high index of suspicion** and **specific testing** are essential.

**Functional immunology (screening).**
- Whole-blood/PBMC stimulation with **BCG ± IL-12 and BCG ± IFN-γ**, measuring IFN-γ and IL-12p40 by ELISA: deficient IFN-γ production in response to IL-12 points to the IL-12/IL-12R arm ([PMID: 31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/), [PMID: 17120032](https://pubmed.ncbi.nlm.nih.gov/17120032/)).
- **Flow cytometry** for IL-12Rβ1 surface expression on activated T cells / EBV-transformed B-cell lines: **absent expression** confirms complete deficiency ([PMID: 19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/), [PMID: 31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/)).
- **Do NOT rely on serum neopterin** — it stays elevated despite absent IFN-γ activity ([PMID: 16339068](https://pubmed.ncbi.nlm.nih.gov/16339068/)).

**Genetic testing (confirmatory).** Sanger sequencing of *IL12RB1*, targeted **immunodeficiency NGS panels**, or **whole-exome/whole-genome sequencing** identify biallelic pathogenic variants ([PMID: 31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/), [PMID: 32602053](https://pubmed.ncbi.nlm.nih.gov/32602053/)). **Dried blood spot** testing has enabled diagnosis in resource-limited/refugee settings ([PMID: 30740107](https://pubmed.ncbi.nlm.nih.gov/30740107/)). Carrier testing and prenatal diagnosis are feasible once the familial variant is known ([PMID: 19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/)).

**Microbiology / pathology.** Culture and molecular identification of mycobacteria (BCG strain confirmation) or *Salmonella*; biopsy typically shows **granulomatous inflammation** (caseous or poorly formed granulomas).

**Differential diagnosis.** Other MSMD genes (IL-12p40/*IL12B* — a near-phenocopy; *IFNGR1/2, STAT1, ISG15, IRF8, NEMO, TYK2*), chronic granulomatous disease (CGD), SCID, combined immunodeficiencies, and other primary immunodeficiencies presenting with BCG disease ([PMID: 34780073](https://pubmed.ncbi.nlm.nih.gov/34780073/), [PMID: 10959079](https://pubmed.ncbi.nlm.nih.gov/10959079/)). Distinguishing IL-12Rβ1 from IFN-γR defects matters prognostically: IL-12Rβ1 has better outcomes and non-recurring mycobacterial disease.

**Screening.** In families with a known proband, **cascade genetic testing** of siblings and **prenatal/newborn** targeted testing guide BCG-avoidance and early surveillance ([PMID: 19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/)).

---

## 11. Outcome / Prognosis

**Comparatively favorable** relative to other MSMD etiologies.

| Cohort | N (IL12RB1 / MSMD) | Key outcome |
|---|---|---|
| International survey ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/)) | 141 patients / 102 kindreds | **70% survival**; mean follow-up 12.7 ± 9.8 yr; 27% of affected sibs asymptomatic |
| Earlier cohort ([PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/)) | 41 patients | Only 5 childhood deaths; mycobacterial infections did not recur |
| Mexico ([PMID: 36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/)) | 22 MSMD (13 IL12RB1) | 7 deaths from disseminated BCG |
| Shanghai 15-yr PID/BCG cohort ([PMID: 41748971](https://pubmed.ncbi.nlm.nih.gov/41748971/)) | 109 PID w/ BCG disease (MSMD 43.1%) | 5-yr survival 80.3%, 10-yr 69.3%; HSCT success 75.8% vs 0% |

**Mortality** is driven principally by **disseminated BCG disease**, especially where diagnosis is delayed ([PMID: 36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/)). Prognostic factors include severity/dissemination at presentation, timeliness of diagnosis and antimycobacterial therapy, access to recombinant IFN-γ, and HSCT for refractory disease. Mycobacterial **recurrence is uncommon**, a favorable prognostic feature; recurrent salmonellosis is a recognized complication.

---

## 12. Treatment

**Pharmacotherapy — pathogen-directed.**
- **Prolonged multidrug antimycobacterial therapy** for BCG/NTM/TB (regimens per species and susceptibility; drug-resistant disease may require individualized regimens) ([PMID: 33631907](https://pubmed.ncbi.nlm.nih.gov/33631907/)).
- **Antibiotics** for *Salmonella* (with attention to recurrence).
- **Antifungals** for candidiasis.

**Immunomodulation — recombinant human IFN-γ (rhIFN-γ, NCIT: Recombinant Interferon Gamma).** Because the defect impairs IFN-γ *production* while the IFN-γ *response* pathway is intact, **exogenous IFN-γ bypasses the block**. In the Chinese cohort, "*77.8% of patients received rhIFN-γ treatment, which can improve the prognosis of patients with IL12RB1 deficiency*" ([PMID: 31367980](https://pubmed.ncbi.nlm.nih.gov/31367980/)). Combined antimycobacterial + IFN-γ therapy achieved control in individual refractory cases, with IFN-γ maintenance ([PMID: 41668770](https://pubmed.ncbi.nlm.nih.gov/41668770/), [PMID: 30968642](https://pubmed.ncbi.nlm.nih.gov/30968642/)).

**Hematopoietic stem cell transplantation (HSCT).** Curative for the underlying immune defect and highly effective against mycobacterial disease in severe/refractory cases: "*Patients who received hematopoietic stem cell transplantation therapy (HSCT) had a significantly higher success rate with antimycobacterial treatment (75.8% vs. 0%)*" ([PMID: 41748971](https://pubmed.ncbi.nlm.nih.gov/41748971/)). HSCT is reserved for severe/relapsing disease given the generally favorable natural history of many IL-12Rβ1 patients.

**Supportive / surgical.** Drainage or excision of suppurative lymphadenitis; nutritional support; management of disseminated organ involvement.

**Pharmacogenomics / gene & RNA therapies.** No approved gene, cell (beyond HSCT), or RNA therapy specific to *IL12RB1*; gene correction is conceptually attractive (proof-of-concept complementation restores function in vitro, [PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/)) but not clinically available.

**Suggested NCIT intervention terms:** Recombinant Interferon Gamma; Hematopoietic Stem Cell Transplantation; Antimycobacterial/Antitubercular Agents; Antibiotic Therapy; Antifungal Agent.

---

## 13. Prevention

- **Primary prevention — avoid live BCG vaccine** in individuals/families known or suspected to have MSMD; BCG is the single most common disease trigger ([PMID: 21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/), [PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)). This is the central actionable prevention measure, especially in high-TB-burden countries with universal neonatal BCG ([PMID: 41668770](https://pubmed.ncbi.nlm.nih.gov/41668770/)).
- **Secondary prevention — early recognition and treatment.** Suspect an inborn error of immunity in any child with disseminated BCG/NTM or non-typhoidal *Salmonella* disease and refer for early immunological evaluation ([PMID: 33631907](https://pubmed.ncbi.nlm.nih.gov/33631907/), [PMID: 41771439](https://pubmed.ncbi.nlm.nih.gov/41771439/)).
- **Genetic counseling / screening.** Autosomal-recessive risk counseling; **cascade testing** of siblings; **carrier and prenatal testing** once the familial variant is known ([PMID: 19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/)); consanguinity counseling. Dried-blood-spot testing extends screening to resource-limited settings ([PMID: 30740107](https://pubmed.ncbi.nlm.nih.gov/30740107/)).
- **Tertiary prevention.** Antimicrobial prophylaxis/surveillance for recurrent salmonellosis; prompt treatment of new infections; consideration of HSCT in severe/refractory disease.
- **Prophylaxis / immunization note.** No vaccine prevents the disorder; live vaccines are contraindicated. Adjunctive rhIFN-γ can be used therapeutically and, in effect, prophylactically as maintenance in refractory disease ([PMID: 41668770](https://pubmed.ncbi.nlm.nih.gov/41668770/)).

---

## 14. Other Species / Natural Disease

- **Human:** *Homo sapiens* (NCBI:txid9606). No naturally occurring companion-animal or wildlife counterpart of *IL12RB1* deficiency is documented in the reviewed literature (no OMIA entry identified for this specific defect).
- **Orthologue:** mouse *Il12rb1* (NCBI Gene ID 16161), highly conserved; the IL-12/IL-23→IFN-γ axis is evolutionarily conserved across mammals, underpinning the validity of the mouse model.
- **Zoonotic / cross-species transmission:** not applicable — this is a host genetic susceptibility, not a transmissible disease. (The triggering pathogens, e.g., *M. bovis*, do have zoonotic relevance, but the disorder itself is non-transmissible.)

---

## 15. Model Organisms

- **Primary model:** ***Il12rb1*-deficient (knockout) mouse**. It recapitulates the core human phenotype: "*Interleukin-12 receptor β1 (IL12RB1)-deficient individuals show increased susceptibilities to local or disseminated BCG infection and environmental mycobacteria infection*," and the model is used specifically to probe why "*the low clinical penetrance of IL12RB1 deficiency and low recurrence rate of mycobacteria infection suggest that protective immunity still exists in this population*" ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/)).
- **Model type:** mammalian germline knockout (constitutive). Useful for dissecting IFN-γ-dependent vs IFN-γ-independent antimycobacterial immunity, disseminated BCG pathogenesis, and correlates of residual protection.
- **Phenotype recapitulation:** good face validity for **disseminated BCG susceptibility**; captures the impaired IL-12→IFN-γ axis and the residual-immunity phenomenon.
- **Limitations:** mice are not routinely BCG-vaccinated as neonates (human trigger context differs); the candidiasis/mucosal IL-17 phenotype and the full human infection spectrum are not fully modeled; genetic background modifies penetrance.
- **In vitro / cellular models:** patient T cells and EBV-transformed B-cell lines used for expression and complementation studies — wild-type *IL12RB1* transfection restores expression and IL-12 responsiveness ([PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/)); flow-cytometry and cytokine-stimulation assays on patient PBMCs ([PMID: 31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/)).
- **Resources:** MGI (mouse *Il12rb1*); patient-derived cell lines from reference immunology laboratories.

---

## Mechanistic Model / Interpretation

The disorder is best understood as a **single upstream lesion with two downstream branches plus a safety net**:

| Element | Consequence | Clinical readout |
|---|---|---|
| Loss of IL-12Rβ1 (shared chain) | No IL-12 signaling → ↓ STAT4 → **↓ IFN-γ** | Macrophages fail to kill mycobacteria/*Salmonella* → disseminated infection |
| Loss of IL-12Rβ1 (shared chain) | No IL-23 signaling → **↓ Th17/IL-17** | Mucocutaneous candidiasis (~25%) |
| Intact IFN-γ **response** machinery | Exogenous IFN-γ still works | rhIFN-γ therapy is effective |
| Redundant IFN-γ-independent immunity | Residual mycobacterial control | Low penetrance; mycobacterial disease rarely recurs; ~70% survival |

This model coherently explains (a) the **narrow pathogen spectrum** (IL-12 is redundant for most microbes; [PMID: 12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/)), (b) the **normal routine immune tests** (the defect is a specific cytokine-receptor lesion, not a global immune failure), (c) the **therapeutic logic of rhIFN-γ** (production defect, response intact), and (d) the **favorable prognosis and incomplete penetrance** (residual immunity). It also predicts the **close phenocopy with IL-12p40/*IL12B* deficiency**, since both remove IL-12(/IL-23)-driven IFN-γ ([PMID: 10959079](https://pubmed.ncbi.nlm.nih.gov/10959079/), [PMID: 23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/)).

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [21057261](https://pubmed.ncbi.nlm.nih.gov/21057261/) | International 141-patient survey — most common MSMD etiology; 70% survival; 27% asymptomatic sibs; organism spectrum | F001 (epidemiology, prognosis, penetrance) |
| [12591909](https://pubmed.ncbi.nlm.nih.gov/12591909/) | Low penetrance, broad resistance, favorable outcome; IL-12 redundant except mycobacteria/*Salmonella* | F001 (selective susceptibility) |
| [11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/) | Complementation proof — WT *IL12RB1* restores expression/function | F002 (causality, LOF) |
| [24186907](https://pubmed.ncbi.nlm.nih.gov/24186907/) | ~25% candidiasis via impaired IL-23/IL-17 | F002 (IL-23 branch) |
| [32025907](https://pubmed.ncbi.nlm.nih.gov/32025907/) | Both IL-12 and IL-23 required for optimal IFN-γ | F002 (pathway) |
| [31367980](https://pubmed.ncbi.nlm.nih.gov/31367980/) | rhIFN-γ improves prognosis (Chinese cohort) | F003 (treatment) |
| [41748971](https://pubmed.ncbi.nlm.nih.gov/41748971/) | HSCT antimycobacterial success 75.8% vs 0%; survival curves | F003 (treatment) |
| [10959079](https://pubmed.ncbi.nlm.nih.gov/10959079/) | Places IL-12Rβ1 in the IFN-γ/IL-12 circuit; pathogen spectrum | F004 (classification) |
| [23429356](https://pubmed.ncbi.nlm.nih.gov/23429356/) | IL-12p40 phenocopy; founder effects; recurrence pattern | F004 (founder effects, differential) |
| [35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/) | *Il12rb1*-KO mouse recapitulates disseminated BCG; residual immunity | F005 (model, penetrance) |
| [29256176](https://pubmed.ncbi.nlm.nih.gov/29256176/) | Human variants abolish surface expression and IL-12 response | F005 (functional genetics) |
| [25453225](https://pubmed.ncbi.nlm.nih.gov/25453225/) | Production-vs-response classification; normal routine tests; broad spectrum | F006 (diagnosis, mechanism) |
| [16339068](https://pubmed.ncbi.nlm.nih.gov/16339068/) | Neopterin remains elevated — not a usable diagnostic marker | Diagnostics caveat |
| [31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/) | Functional flow + stimulation assays; novel variants | Diagnostics |
| [36044171](https://pubmed.ncbi.nlm.nih.gov/36044171/) | Mexican cohort — IL12RB1 leading MSMD cause; BCG-driven mortality | Epidemiology/prognosis |
| [32602053](https://pubmed.ncbi.nlm.nih.gov/32602053/) | Iranian cohort — consanguinity, allelic heterogeneity | Population genetics |
| [30968642](https://pubmed.ncbi.nlm.nih.gov/30968642/), [30740107](https://pubmed.ncbi.nlm.nih.gov/30740107/), [33631907](https://pubmed.ncbi.nlm.nih.gov/33631907/), [41668770](https://pubmed.ncbi.nlm.nih.gov/41668770/), [41771439](https://pubmed.ncbi.nlm.nih.gov/41771439/), [19099833](https://pubmed.ncbi.nlm.nih.gov/19099833/), [24064560](https://pubmed.ncbi.nlm.nih.gov/24064560/), [23726680](https://pubmed.ncbi.nlm.nih.gov/23726680/), [34780073](https://pubmed.ncbi.nlm.nih.gov/34780073/) | Case reports/cohorts — variant types, DBS diagnosis, IFN-γ maintenance, Salmonella presentation, prenatal diagnosis, variable penetrance, NTM disease, BCG differential | Phenotypes, variants, treatment, prevention |

**Evidence source types:** human clinical cohorts and case reports (majority); in vitro functional/complementation studies ([PMID: 11424023](https://pubmed.ncbi.nlm.nih.gov/11424023/), [PMID: 31158284](https://pubmed.ncbi.nlm.nih.gov/31158284/)); model-organism (mouse) study ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/)).

---

## Limitations and Knowledge Gaps

1. **No precise prevalence/incidence figures.** IL-12Rβ1 deficiency is established as the most common MSMD etiology but exact population rates are unquantified; ascertainment is biased toward BCG-vaccinating, high-consanguinity regions.
2. **Penetrance mechanism incompletely defined.** The identity of the residual IFN-γ-independent protective pathway(s) is unresolved; the mouse model is actively being used to address this ([PMID: 35891311](https://pubmed.ncbi.nlm.nih.gov/35891311/)).
3. **No standardized quality-of-life or disability outcome data** (EQ-5D/SF-36/PROMIS) for this disorder.
4. **Genotype–phenotype correlation is weak/absent.** Complete-null alleles produce variable severity; no consistent modifier gene is identified.
5. **Treatment evidence is largely observational** (cohorts/case series), not randomized; optimal rhIFN-γ dosing/duration and precise HSCT indications remain to be standardized.
6. **Candidiasis–IL-17 link is well-supported but mechanistically inferred** rather than directly proven in each patient.

---

## Proposed Follow-up Experiments / Actions

1. **Define residual immunity:** use the *Il12rb1*-KO mouse and patient cells to map the IFN-γ-independent antimycobacterial pathway(s) that explain low penetrance and non-recurrence (single-cell transcriptomics of granuloma macrophages; IL-12/IL-23-independent IFN-γ sources).
2. **Registry and natural-history study:** establish a prospective international registry to quantify prevalence, long-term outcomes, and standardized QoL measures.
3. **Genotype–modifier discovery:** whole-genome sequencing of concordant/discordant sib pairs to identify penetrance modifiers.
4. **Therapeutic optimization:** prospective evaluation of rhIFN-γ dosing/duration and clearer HSCT-selection criteria; explore gene-correction (autologous HSC + *IL12RB1* repair) building on in vitro complementation proof-of-concept.
5. **Screening policy:** evaluate targeted pre-BCG screening (cascade genetic testing, dried-blood-spot assays) in high-consanguinity, high-TB-burden populations to prevent BCG disease.
6. **Biomarker development:** validate IL-12-response functional assays and flow-cytometric IL-12Rβ1 expression as standardized frontline diagnostics (and formally deprecate neopterin for this purpose).

---

*Report compiled from 6 confirmed findings and 30 reviewed papers across the autonomous discovery iterations. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_IL12RB1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_IL12RB1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013955` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Mendelian susceptibility to mycobacterial diseases due to complete IL12RB1 deficiency**
- `HP:0032256` (1 mention) - the report calls it "Tuberculosis"; HP calls it **Unusual Histoplasma capsulatum infection**
- `UBERON:0002097` (1 mention) - the report calls it "Skin and subcutaneous tissue"; UBERON calls it **skin of body**
- `UBERON:0000167` (1 mention) - the report calls it "Oropharyngeal mucosa"; UBERON calls it **oral cavity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002728` (1 mention) - the report calls it "Chronic mucocutaneous candidiasis"; HP calls it **Recurrent mucocutaneous candidiasis**, and lists "Chronic mucocutaneous candidiasis" among its other names
- `UBERON:0000029` (1 mention) - the report calls it "Lymphoreticular:** lymph nodes"; UBERON calls it **lymph node**