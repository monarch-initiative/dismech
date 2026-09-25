---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T07:17:31.993198'
end_time: '2026-09-25T07:41:50.500039'
duration_seconds: 1458.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Staphylococcal Toxic Shock Syndrome
  mondo_id: MONDO:0020545
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 24
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 36
  verified: 32
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.03
  labels_checked: 17
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - fever
    - sign
    ontology_label: Fever
  - term_id: GO:0002504
    reported_labels:
    - antigen processing and presentation of peptide or polysaccharide antigen via
      MHC class II
    - MHC class II antigen presentation
    ontology_label: antigen processing and presentation of peptide or polysaccharide
      antigen via MHC class II
  - term_id: HP:0000988
    reported_labels:
    - sign
    ontology_label: Skin rash
  - term_id: HP:0007550
    reported_labels:
    - sign
    ontology_label: Hypohidrosis or hyperhidrosis
  - term_id: HP:0001873
    reported_labels:
    - lab
    ontology_label: Thrombocytopenia
  labels_variant: 6
  unresolved_terms:
  - CHEBI:63591
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Staphylococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Staphylococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Staphylococcal Toxic Shock Syndrome
- **MONDO ID:** MONDO:0020545 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Staphylococcal Toxic Shock Syndrome** covering all of the
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

# Staphylococcal Toxic Shock Syndrome (MONDO:0020545): A Comprehensive Disease Characterization

## Summary

Staphylococcal toxic shock syndrome (TSS) is an acute, toxin-mediated, multi-system illness caused by strains of *Staphylococcus aureus* that secrete pyrogenic-toxin **superantigens**. In menstrual TSS (mTSS) the dominant toxin is **toxic shock syndrome toxin-1 (TSST-1)**, encoded by the *tst* gene carried on mobile Staphylococcal Pathogenicity Islands (SaPIs); in non-menstrual TSS (nmTSS) the enterotoxins **SEB** and **SEC** account for a large share of cases. These superantigens do not undergo conventional antigen processing. Instead they bridge **MHC class II** molecules on antigen-presenting cells directly to the **variable region of the T-cell receptor β-chain (TCR Vβ)**, polyclonally activating up to ~20% of the T-cell repertoire (versus ~0.01% for a conventional antigen). The resulting **cytokine storm** — dominated by TNF-α and IFN-γ — produces the cardinal clinical tetrad of fever, diffuse macular erythroderma, hypotension, and multi-organ involvement, followed by desquamation during convalescence.

TSS is fundamentally an infectious/toxin-mediated disease rather than a heritable one. There are no causal human genes; host susceptibility is instead polygenic and immunological, governed by two factors: (1) the presence or absence of protective **neutralizing anti-TSST-1 antibody**, and (2) **HLA class II haplotype**, where DR15/DQ6 alleles are protective and DR14/DR7/DQ5 alleles increase risk. The bacterial "genetics" of the disease are those of *S. aureus*: *tst* resides on horizontally transmissible pathogenicity islands mobilized by helper bacteriophages, and toxin expression is tuned by the global regulators **agr**, **sarA**, **σB (SigB)**, and **Rot**.

Management rests on early recognition, source control (e.g., tampon removal, abscess drainage), and combination antibiotic therapy pairing an anti-staphylococcal agent with a **protein-synthesis-inhibitor** (clindamycin or linezolid) that shuts off toxin translation — while avoiding β-lactam monotherapy, which can paradoxically *induce* toxin production. Adjunctive intravenous immunoglobulin (IVIG) and intensive supportive care complete the regimen. Prevention is chiefly behavioral (tampon absorbency and hygiene) because no licensed human vaccine exists, although detoxified TSST-1 toxoids are protective in animal models. This report synthesizes 11 confirmed findings across 63 reviewed papers, organized against the 15-section disease-characterization template.

---

## Key Findings

### Finding 1 — Superantigen mechanism: MHC II / TCR Vβ bridging drives a lethal cytokine storm

The central pathophysiological engine of staphylococcal TSS is superantigen-mediated T-cell activation. TSST-1 (and the related enterotoxins) bind **outside** the peptide-binding groove of MHC class II and simultaneously engage specific TCR Vβ chains — notably **Vβ2** for TSST-1 — thereby cross-linking antigen-presenting cells to T cells regardless of antigen specificity. This polyclonally activates whole T-cell subsets, producing an "exuberant" release of pro-inflammatory cytokines that causes shock.

Causal, in-vivo evidence comes from a murine model in which **all** mice co-administered TSST-1 and control immunoglobulin died, whereas costimulation blockade with **CTLA4Ig rescued 75%** and sharply reduced TSST-1-induced serum **TNF-α and IFN-γ** ([PMID: 8892617](https://pubmed.ncbi.nlm.nih.gov/8892617/)). The abstract states: *"Lethal toxic shock syndrome (TSS) results from the MHC class II presentation of bacterial superantigens, most commonly toxic shock syndrome-1 (TSST-1), to specific TCR Vbeta-bearing T cells. This superantigen-induced stimulation of whole T cell subsets leads to the exuberant cytokine production that in turn causes the shock syndrome."* The rescue result — *"While all mice co-administered TSST-1 and control Ig died, 75% of the CTLA4Ig plus TSST-1-treated mice survived... markedly diminished TSST-1 induced serum levels of TNF-alpha and IFN-gamma"* — demonstrates that the lethality is cytokine-mediated and costimulation-dependent.

**Ontology anchors:** GO:0042092 (type 2 immune response), GO:0002438 (acute inflammatory response), GO:0032609 (interferon-gamma production), GO:0032640 (tumor necrosis factor production); CL:0000084 (T cell); TNF-α/IFN-γ as protein mediators.

### Finding 2 — Menstrual TSS: TSST-1-producing MSSA, and current CDC criteria miss early cases

Menstrual staphylococcal TSS is overwhelmingly caused by **methicillin-sensitive *S. aureus* (MSSA)** producing TSST-1. In a French nationwide ICU cohort of **102 mTSS patients** (median age 18 years), **all blood cultures were sterile**, MSSA grew from **92 of 96 vaginal samples**, and the *tst* gene was present in **66 of 76 (87%)** screened strains ([PMID: 33906228](https://pubmed.ncbi.nlm.nih.gov/33906228/)). Key quotes: *"Methicillin-sensitive Staphylococcus aureus grew from 92 of 96 vaginal samples"* and *"toxic shock syndrome toxin 1 was isolated from 66 strains (87%)."*

Clinically important, the study exposed the **insensitivity of the CDC case definition at presentation**: *"At ICU admission, no patient met the 2011 CDC criteria for confirmed m-TSS, and only 53 (52%) fulfilled the criteria for probable m-TSS."* Despite severe illness (84% required vasopressors, 21% intubation), the modern short-term prognosis was favorable: *"No patient required limb amputation or died in the ICU."* This distinguishes staphylococcal mTSS from streptococcal TSS, which carries much higher mortality.

**Ontology anchors:** UBERON:0000996 (vagina); HP:0001945 (fever), HP:0011009 (acute hypotension); the sterile-blood-culture / colonized-mucosa pattern reflects the toxin-mediated (rather than bacteremic) nature of the disease.

### Finding 3 — Host EGFR signaling amplifies mucosal pathology and is a druggable target

Beyond systemic T-cell activation, TSST-1 exerts local effects on mucosal epithelium. TSST-1 and α-toxin induce **ADAM- and EGFR-dependent IL-8 production** from human vaginal epithelial cells and porcine vaginal mucosa, with EGFR signaling accounting for the majority of the epithelial IL-8 response to both purified toxins and live *S. aureus*. Critically, pharmacological EGFR blockade was protective: *"inhibition of EGFR signaling with the EGFR-specific tyrosine kinase inhibitor AG1478 significantly increases survival in a rabbit model of mTSS"* ([PMID: 27414801](https://pubmed.ncbi.nlm.nih.gov/27414801/)). The mechanism is defined by the finding that *"TSST-1 and α-toxin induce ADAM- and EGFR-dependent cytokine production from human vaginal epithelial cells."* This identifies **host EGFR** as a downstream amplifier and a potential host-directed therapeutic target.

**Ontology anchors:** EGFR (HGNC:3236); GO:0007173 (epidermal growth factor receptor signaling pathway); GO:0071356 (cellular response to tumor necrosis factor); CL:0000066 (epithelial cell); interleukin-8 as chemokine mediator.

### Finding 4 — *tst* expression is controlled by staphylococcal global virulence regulators (sarA, agr)

TSST-1 production is not constitutive; it is embedded in the *S. aureus* virulence regulatory network. The global regulator **SarA up-regulates *tst***: *"sarA up-regulates both toxic shock syndrome toxin 1 gene (tst) expression and staphylococcal enterotoxin B production, respectively"* ([PMID: 9829932](https://pubmed.ncbi.nlm.nih.gov/9829932/)), and participates in environmental signal transduction responding to aeration. The **agr** quorum-sensing system operates in a cell-density-dependent manner (specific *agr* expression rises above OD600 ≈ 0.14), but *tst* is partly uncoupled from agr control: *"the amount of specific expression of tst is modulated independently of agr"* ([PMID: 12586420](https://pubmed.ncbi.nlm.nih.gov/12586420/)). This regulatory layering explains why toxin output varies with growth phase, oxygenation, and micro-environmental conditions such as those inside a tampon-filled vagina.

### Finding 5 — *tst* is carried on mobile SaPI pathogenicity islands mobilized by helper phages

The genetic basis of TSST-1 capability is horizontal, not vertical. *tst* is part of a discrete **15.2 kb genetic element** absent in TSST-1-negative strains: *"Tst, the gene for toxic shock syndrome toxin-1 (TSST-1), is part of a 15.2 kb genetic element in Staphylococcus aureus that is absent in TSST-1-negative strains"* ([PMID: 9720870](https://pubmed.ncbi.nlm.nih.gov/9720870/)). The prototype **SaPI1** is excised, circularized, and transduced at high frequency by helper phages ϕ13 and 80α ([PMID: 11489124](https://pubmed.ncbi.nlm.nih.gov/11489124/)), while the bovine island **SaPIbov** additionally carries *sec-bovine* and *sel* ([PMID: 11114901](https://pubmed.ncbi.nlm.nih.gov/11114901/)). The mobility drives dissemination: *"Their mobility may be responsible for the spread of TSST-1 production among S. aureus strains."*

Transcription of *tst* is further modulated by stress and repressor circuits — the alternative sigma factor **σB strongly represses** toxin expression *"via at least two distinct regulatory pathways dependent upon sarA and agr,"* and **Rot** also contributes ([PMID: 26275216](https://pubmed.ncbi.nlm.nih.gov/26275216/)).

**Genetic map (bacterial):** *tst* / SaPI1 (integrates near *tyrB*), SaPI2 (in *trp* region), SaPIbov (adjacent to *gmps*); regulators *sarA*, *agr*, *sigB*, *rot*.

### Finding 6 — Non-menstrual TSS: a family of superantigens (TSST-1, SEB, SEC) plus endotoxin synergy

While TSST-1 causes nearly all menstrual TSS, **non-menstrual TSS** is mediated by a broader superantigen family. *"TSST-1, staphylococcal enterotoxin B and C are also responsible for most cases of non-menstrual TSS"* ([PMID: 24816557](https://pubmed.ncbi.nlm.nih.gov/24816557/)). Historically, vaginal isolates produced TSST-1 (alone or with EntC1), whereas EntB- or EntC1-producing strains without TSST-1 were common in nmTSS ([PMID: 2494691](https://pubmed.ncbi.nlm.nih.gov/2494691/)). In community-associated MRSA (USA400), 31 related isolates produced **SEB (n=5) or SEC (n=26) and none made TSST-1** ([PMID: 12499191](https://pubmed.ncbi.nlm.nih.gov/12499191/)).

Two additional mechanistic properties amplify severity: superantigens *"are also capable of enhancing the toxic effects of endogenous endotoxin. This interaction appears to be critical in mediating the severity of TSS and related mortality"* — a **superantigen–endotoxin synergy** — and they cause a distinctive form of adaptive immune suppression ([PMID: 24816557](https://pubmed.ncbi.nlm.nih.gov/24816557/)).

| Setting | Dominant toxin(s) | Typical organism |
|---|---|---|
| Menstrual TSS | TSST-1 | MSSA (vaginal colonizer) |
| Non-menstrual TSS | TSST-1, SEB, SEC | MSSA or MRSA (wound, surgical, skin, respiratory) |
| CA-MRSA (USA400) nmTSS | SEB or SEC | MRSA |

### Finding 7 — HLA class II immunogenetics modulate severity (protective vs high-risk haplotypes)

Because superantigens act through MHC class II, **host HLA haplotype** shapes the magnitude of the response. Protective and high-risk haplotypes have been defined for superantigen-driven toxic shock: *"HLA-II-DR15/DQ6 alleles strongly protect against severe sepsis, HLA-II-DR14/DR7/DQ5 alleles significantly increase the risk for toxic shock syndrome"* ([PMID: 21282506](https://pubmed.ncbi.nlm.nih.gov/21282506/)). The protective **DRB1\*1501/DQB1\*0602** haplotype quantitatively blunts the response: *"Patients with the DRB1\*1501/DQB1\*0602 haplotype mounted significantly reduced responses and were less likely to develop severe systemic disease (P < 0.0001)"* ([PMID: 12436116](https://pubmed.ncbi.nlm.nih.gov/12436116/)). Protective alleles skew cytokine output toward anti-inflammatory IL-10 over IFN-γ. These data were generated with streptococcal superantigens but are mechanistically transferable to staphylococcal superantigens, which use the identical MHC-II presentation route.

**Ontology anchors:** HLA-DRB1 (HGNC:4948), HLA-DQB1 (HGNC:4944); GO:0002504 (antigen processing and presentation of peptide or polysaccharide antigen via MHC class II).

### Finding 8 — Detoxified TSST-1 toxoids protect in animal models; no licensed human vaccine exists

Active immunization with detoxified TSST-1 is protective preclinically. Recombinant single (**G31R, H135A**) and double (**G31R/H135A**) mutant TSST-1 and formaldehyde-inactivated toxoids had minimal mitogenicity/toxicity; after primary immunization plus three boosts, **all vaccinated rabbits developed anti-TSST-1 antibody and survived a lethal superantigen-plus-LPS challenge** ([PMID: 11818153](https://pubmed.ncbi.nlm.nih.gov/11818153/)): *"all vaccinated animals developed antibody titers against TSST-1 and were protected against challenge with a lethal doses of superantigen potentiated with lipopolysaccharide."* Neutralizing antibodies map predominantly to the **N-terminal residues 1–15** of TSST-1 ([PMID: 12399195](https://pubmed.ncbi.nlm.nih.gov/12399195/)). The same paper underscores the therapeutic gap: *"Up to now there is no treatment for staphylococcal toxic shock syndrome, a disease mainly induced by toxic shock syndrome toxin-1(TSST-1)."*

**Ontology anchors:** NCIT toxoid vaccine; the LPS-potentiation model directly recapitulates the superantigen–endotoxin synergy of Finding 6.

### Finding 9 — TSST-1 is a structurally divergent superantigen with stringent Vβ2.1 specificity

Structural biology explains TSST-1's unusually narrow Vβ preference. The crystal structure of TSST-1 bound to human TCR **Vβ2.1** shows it engages the TCR *"in a markedly different way than do other SAgs,"* accounting for its high Vβ specificity, and confirms the bimolecular bridging mechanism: *"Superantigens (SAGs) bind simultaneously to major histocompatibility complex (MHC) and T-cell receptor (TCR) molecules, resulting in the massive release of inflammatory cytokines that can lead to toxic shock syndrome (TSS) and death"* ([PMID: 17268555](https://pubmed.ncbi.nlm.nih.gov/17268555/)). The determinant of specificity is a non-canonical loop: *"the non-canonical length of CDR2β is a critical determinant for recognition by TSST-1"* ([PMID: 21127057](https://pubmed.ncbi.nlm.nih.gov/21127057/)). TSST-1 is a ~22 kDa pyrogenic toxin superantigen with an N-terminal OB-fold domain and a C-terminal β-grasp domain.

**Ontology anchors:** UniProt P06886 (TSST-1, *S. aureus*); Pfam PF02876 (Staphylococcal/streptococcal toxin, β-grasp); GO:0042288 (MHC class I protein binding — analog for MHC engagement); PDB structures of the TSST-1–TCR complex.

### Finding 10 — Protein-synthesis-inhibitor antibiotics suppress toxin; β-lactams can induce it

Antibiotic choice directly modulates toxin output, providing the rationale for adjunctive anti-toxin therapy. Sub-inhibitory **nafcillin (a β-lactam) induced and prolonged** mRNA and increased production of PVL, α-toxin and TSST-1, whereas **clindamycin and linezolid** markedly suppressed toxin production: *"clindamycin and linezolid markedly suppressed translation, but not transcription, of toxin genes"* ([PMID: 17191165](https://pubmed.ncbi.nlm.nih.gov/17191165/)). The same study warns: *"by inducing and enhancing toxin production, inadvertent use of beta-lactam antibiotics to treat methicillin-resistant S. aureus infections may contribute to worse outcomes."* The clindamycin effect is robust even in resistant strains: *"sub-MICs of clindamycin decrease Panton-Valentine leucocidin, toxic-shock-staphylococcal toxin (TSST-1) and alpha-haemolysin (Hla) expression"* — retained in inducible clindamycin-resistant isolates ([PMID: 30342546](https://pubmed.ncbi.nlm.nih.gov/30342546/)).

**Ontology anchors:** NCIT clindamycin, linezolid; CHEBI:3745 (clindamycin), CHEBI:63591 (linezolid); the transcription-vs-translation distinction pinpoints the ribosome as the drug target.

### Finding 11 — Clinical phenotype and epidemiologic shift after tampon changes

TSS is *"characterized by fever, rash, hypotension, multiorgan involvement, and desquamation"* and reflects among the most severe *S. aureus* disease ([PMID: 15777108](https://pubmed.ncbi.nlm.nih.gov/15777108/)). The staphylococcal case definition was established in the early 1980s. The epidemiology shifted markedly after high-absorbency tampons were reformulated/withdrawn: *"Changes in the manufacturing and use of tampons led to a decline in staphylococcal TSS over the past decade, while the incidence of nonmenstrual staphylococcal TSS increased. Nonmenstrual TSS and menstrual TSS are now reported with almost equal frequency."* Compared with streptococcal TSS, staphylococcal TSS involves more superficial sites and bacteremia is less common.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (trigger → clinical manifestation)

```
1. S. aureus acquires tst on a mobile SaPI via helper-phage transduction (φ13, 80α)
        └─ leads to → a toxin-competent strain colonizing skin/mucosa (e.g., vagina)
2. Local micro-environment (high aeration, neutral pH, protein, elevated CO2 in a
   tampon-filled vagina) + quorum sensing (agr) + SarA activation
        └─ leads to → up-regulated tst transcription (repressed by sigmaB/Rot when stressed)
3. TSST-1 is secreted and crosses the mucosal epithelial barrier
        └─ BRANCH A (local): TSST-1 + alpha-toxin engage ADAM/EGFR on epithelium
              └─ results in → IL-8 / chemokine release, barrier disruption, toxin uptake
        └─ BRANCH B (systemic): TSST-1 bridges MHC class II (APC) to TCR Vbeta2.1 (T cell)
4. Polyclonal activation of up to ~20% of T cells (antigen-independent)
        └─ leads to → massive TNF-alpha and IFN-gamma (+ IL-1, IL-2) release = cytokine storm
5. Cytokine storm (amplified by synergy with endogenous LPS/endotoxin)
        └─ results in → vasodilation, capillary leak, myocardial depression
6. Distributive shock + multi-organ hypoperfusion
        └─ leads to → fever, diffuse erythroderma, hypotension, renal/hepatic/CNS/GI
           dysfunction, coagulopathy
7. Convalescent phase
        └─ results in → desquamation (palms/soles), typically 1–2 weeks after onset

Host modifiers acting on steps 4–6:
   - Neutralizing anti-TSST-1 antibody (N-terminal residues 1-15) → blocks step 3-4
   - HLA-DR15/DQ6 → blunts step 4 (protective); HLA-DR14/DR7/DQ5 → augments (risk)
   - Antibiotic choice: clindamycin/linezolid → suppress step 2-3 (translation);
     beta-lactams → can induce step 2 (worse)
```

### Upstream vs downstream summary

| Layer | Element | Role | Direction |
|---|---|---|---|
| Bacterial genetics | SaPI/*tst*, agr, sarA, σB, Rot | Determine whether/how much toxin is made | Most upstream |
| Toxin | TSST-1 (SEB/SEC) | Bridges MHC II ↔ TCR Vβ | Initiating molecular lesion |
| Local host | EGFR/ADAM epithelial axis | Amplifies mucosal cytokines, barrier breach | Early amplifier |
| Systemic host | T-cell activation, TNF-α/IFN-γ | Cytokine storm | Core effector |
| Host modifiers | Anti-toxin antibody, HLA II | Set threshold/severity | Modulatory |
| Synergy | Endogenous endotoxin (LPS) | Enhances lethality | Downstream amplifier |
| Clinical | Shock, multi-organ failure, desquamation | Manifestation | Most downstream |

### Anatomy, cells, and processes

- **Primary sites (UBERON):** vagina (UBERON:0000996) in mTSS; skin/soft tissue, surgical wounds, respiratory tract in nmTSS. **Systems involved:** cardiovascular (shock), integumentary (erythroderma/desquamation), renal, hepatic, hematologic, gastrointestinal, CNS.
- **Cell types (CL):** CD4+ T cells (CL:0000624) and T cells broadly (CL:0000084); antigen-presenting cells / dendritic cells (CL:0000451), monocytes/macrophages (CL:0000235); epithelial cells (CL:0000066).
- **Biological processes (GO):** GO:0032640 (TNF production), GO:0032609 (IFN-γ production), GO:0002438 (acute inflammatory response), GO:0007173 (EGFR signaling), GO:0002504 (MHC class II antigen presentation).

---

## Section-by-Section Findings (against the 15-section template)

### 1. Disease Information
Acute toxin-mediated multi-system illness of *S. aureus* superantigens. Identifiers: **MONDO:0020545**; MeSH "Shock, Septic"/"Toxic Shock Syndrome" (D012772); ICD-10 **A48.3** (Toxic shock syndrome); ICD-11 staphylococcal toxic shock coded under staphylococcal disease. Synonyms: staphylococcal TSS, TSS, menstrual/tampon-associated TSS. Information is derived from **aggregated disease-level resources** (case series, ICU cohorts, surveillance) rather than a single-gene patient/EHR registry.

### 2. Etiology
**Primary cause:** infection/colonization by TSST-1– (or SEB/SEC-) producing *S. aureus* (Findings 1, 2, 6). **Genetic risk factors (host):** no causal Mendelian gene; susceptibility is polygenic via **HLA class II** (DR14/DR7/DQ5 increase risk; DR15/DQ6 protect — Finding 7) and via absence of neutralizing anti-toxin antibody. **Environmental risk factors:** high-absorbency tampon use, prolonged tampon retention, menstruation, surgical/postpartum wounds, nasal packing, skin/soft-tissue infection, and inadvertent β-lactam monotherapy that induces toxin (Findings 10, 11). **Protective factors:** pre-existing neutralizing anti-TSST-1 antibody (acquired with age), protective HLA haplotype, lower-absorbency products/menstrual hygiene. **Gene–environment interaction:** the same toxin dose produces divergent severity depending on host HLA haplotype and antibody status — a direct GxE effect at the MHC-II/TCR interface.

### 3. Phenotypes
Cardinal manifestations (per case definition and cohorts, Findings 2, 11):

| Phenotype | Type | HPO suggestion | Frequency / note |
|---|---|---|---|
| Fever | sign | HP:0001945 | Near-universal (defining criterion) |
| Diffuse macular erythroderma ("sunburn" rash) | sign | HP:0000988 | Defining criterion |
| Hypotension / shock | sign | HP:0011009 / HP:0001635 | Very common; 84% needed vasopressors in ICU cohort |
| Desquamation (palms/soles) | sign | HP:0007550 | Convalescent, 1–2 wks |
| Multi-organ involvement (≥3 systems) | lab/clinical | renal HP:0000083, hepatic HP:0001392, GI HP:0002014, muscular HP:0003198 | Defining criterion |
| Vomiting/diarrhea | symptom | HP:0002013 / HP:0002014 | Common at onset |
| Myalgia / elevated CPK | sign/lab | HP:0003198 / HP:0003236 | Common |
| Thrombocytopenia | lab | HP:0001873 | Common |

Onset is **acute** (hours–days), severity **severe** but potentially reversible, course **self-limited** with treatment; QoL impact is acute/critical rather than chronic, though ICU survivors may have transient organ dysfunction.

### 4. Genetic/Molecular Information
**No human causal genes.** The disease "genes" are bacterial: ***tst*** (TSST-1) on SaPI1/SaPI2/SaPIbov; ***seb***, ***sec*** for enterotoxins (Findings 5, 6). Host **modifier loci:** HLA-DRB1/DQB1 (Finding 7). No pathogenic germline human variants, no ClinVar entries, no chromosomal abnormalities apply. "Somatic vs germline" and gnomAD allele-frequency fields are **not applicable**. Bacterial regulatory control operates via agr/sarA/σB/Rot (Findings 4, 5).

### 5. Environmental Information
**Infectious agent:** *Staphylococcus aureus* (NCBI:txid1280), MSSA in mTSS, MSSA/MRSA in nmTSS (Findings 2, 6). **Environmental/lifestyle factors:** tampon absorbency and retention time, menstruation, surgical wounds, nasal packing (Finding 11). No toxin/radiation/pollution etiology.

### 6. Mechanism / Pathophysiology
Fully developed above (see Mechanistic Model). Molecular pathways: MHC-II/TCR-Vβ superantigen bridging → NF-κB/cytokine transcription; EGFR/ADAM epithelial signaling. Immune involvement: polyclonal T-cell activation + innate cytokine amplification + LPS synergy + paradoxical adaptive immune suppression. Protein dysfunction: this is a **toxin gain-of-function** on host receptors, not a host protein defect.

### 7. Anatomical Structures Affected
Primary: vaginal mucosa (mTSS, UBERON:0000996), skin/soft tissue and wounds (nmTSS). Secondary/systemic: cardiovascular system, kidney (UBERON:0002113), liver (UBERON:0002107), skin (UBERON:0002097), CNS, GI tract, skeletal muscle. Lateralization: **bilateral/systemic**. Subcellular: cell-surface MHC-II and TCR (plasma membrane, GO:0005886); no organelle-specific lesion.

### 8. Temporal Development
**Onset:** acute, any age but menstrual form peaks in adolescents/young women (median 18 y in ICU cohort, Finding 2). **Course:** rapidly progressive over hours to a few days; **self-limited** with prompt source control and antibiotics; convalescent desquamation at 1–2 weeks. **Critical period:** the first hours of shock — early recognition and toxin suppression are the intervention window. Recurrence can occur if anti-toxin antibody fails to develop.

### 9. Inheritance and Population
**Not inherited** — no Mendelian pattern. Epidemiology: menstrual TSS incidence fell sharply after tampon reformulation; menstrual and non-menstrual now occur with roughly equal frequency (Finding 11). Population: menstrual form predominantly in menstruating adolescents/young women; non-menstrual form across ages and sexes. Host HLA distribution influences population-level severity (Finding 7).

### 10. Diagnostics
**Clinical/CDC criteria** (fever ≥38.9°C, diffuse macular erythroderma, hypotension, desquamation, ≥3-organ involvement, negative alternative cultures) — but note **poor sensitivity at ICU admission** (Finding 2). **Microbiology:** blood cultures typically **sterile**; *S. aureus* recovered from vaginal/wound sites; toxin/gene detection (*tst*) supports diagnosis. **Laboratory:** elevated CPK, transaminases, creatinine; thrombocytopenia; leukocytosis with left shift. **Differential diagnosis:** streptococcal TSS (higher mortality, more bacteremia), septic shock, Kawasaki disease, Rocky Mountain spotted fever, drug reactions (SJS/TEN), leptospirosis, measles. Genetic testing is **not applicable** for diagnosis.

### 11. Outcome/Prognosis
Modern menstrual TSS in ICU care has **low mortality** (no ICU deaths or amputations in the 102-patient French cohort; 84% vasopressors, 21% intubation — Finding 2), contrasting with historically higher rates and with streptococcal TSS mortality. Prognostic factors: promptness of source control and anti-toxin antibiotic therapy, HLA haplotype, comorbidity, and toxin type. Recovery is generally complete; recurrence risk exists without protective antibody.

### 12. Treatment
Combination strategy: (1) **source control** (remove tampon/foreign body, drain abscess); (2) **anti-staphylococcal antibiotic** — anti-staphylococcal β-lactam for MSSA or vancomycin for MRSA — **paired with a protein-synthesis-inhibitor toxin suppressor** (clindamycin, NCIT; or linezolid) because β-lactam monotherapy can *induce* toxin (Finding 10); (3) **IVIG** to neutralize circulating superantigen; (4) intensive supportive care (fluids, vasopressors, organ support). Investigational/host-directed: EGFR tyrosine-kinase inhibition (AG1478, preclinical — Finding 3); engineered neutralizing scFv / high-affinity soluble TCR domains. **Pharmacogenomics:** HLA haplotype conditions severity but is not yet used to guide therapy.

### 13. Prevention
**Primary:** behavioral — lower-absorbency tampons, frequent changing, alternating with pads, hygiene; wound care. **Secondary:** early recognition and prompt treatment. **Tertiary:** toxin-suppressing antibiotics + IVIG to limit organ damage; recurrence prevention by avoiding tampons after an episode until anti-toxin antibody documented. **Vaccine:** detoxified TSST-1 toxoids protect in animals but **none licensed for humans** (Finding 8).

### 14. Other Species / Natural Disease
*S. aureus* superantigen disease occurs in animals: **SaPIbov** carries *tst* and *sec-bovine* in bovine mastitis strains (Finding 5, [PMID: 11114901](https://pubmed.ncbi.nlm.nih.gov/11114901/)), demonstrating natural TSST-1/SEC production in cattle and evolutionary conservation of the superantigen–Vβ mechanism (bovine-Vβ-specific T-cell expansion). Zoonotic transfer of toxin-bearing mobile elements is plausible given phage-mediated mobility. Species: *Bos taurus* (NCBI:txid9913), *S. aureus* (NCBI:txid1280).

### 15. Model Organisms
- **Rabbit** models of menstrual TSS: used to show EGFR-dependence and AG1478 protection (Finding 3) and superantigen lethality; strong recapitulation of shock physiology.
- **Mouse** models: TSST-1 + potentiator lethality; CTLA4Ig rescue demonstrating cytokine-mediated death (Finding 1). Note murine T cells are relatively insensitive to some superantigens, often requiring LPS potentiation or HLA-transgenic/D-galactosamine sensitization.
- **In vitro:** human PBMC / vaginal epithelial cells for Vβ expansion, cytokine, and EGFR/IL-8 assays.
- Limitations: no single model captures the full human HLA-II repertoire; LPS potentiation is often required, and human-specific Vβ2 responses are best studied in HLA-transgenic or human-cell systems.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding(s) | Evidence type |
|---|---|---|---|
| [8892617](https://pubmed.ncbi.nlm.nih.gov/8892617/) | TSST-1-induced death prevented by CTLA4Ig | F1 (mechanism, cytokine storm) | Mouse in vivo |
| [33906228](https://pubmed.ncbi.nlm.nih.gov/33906228/) | Menstrual TSS French nationwide study | F2 (mTSS = MSSA/TSST-1; CDC criteria insensitive) | Human ICU cohort (n=102) |
| [27414801](https://pubmed.ncbi.nlm.nih.gov/27414801/) | EGFR signaling mediates systemic TSS effects | F3 (EGFR amplifier, AG1478 protection) | Rabbit + human cell |
| [9829932](https://pubmed.ncbi.nlm.nih.gov/9829932/) | Role of SarA in virulence | F4 (sarA up-regulates tst) | Bacterial genetics |
| [12586420](https://pubmed.ncbi.nlm.nih.gov/12586420/) | Cell density, agr, tst expression | F4 (agr/tst relationship) | Bacterial genetics |
| [9720870](https://pubmed.ncbi.nlm.nih.gov/9720870/) | tst on mobile pathogenicity islands | F5 (SaPI, phage mobility) | Bacterial genetics |
| [11489124](https://pubmed.ncbi.nlm.nih.gov/11489124/) | Molecular genetics of SaPI1 | F5 (phage-dependent excision/transfer) | Bacterial genetics |
| [11114901](https://pubmed.ncbi.nlm.nih.gov/11114901/) | SaPIbov multiple superantigens | F5, F14 (bovine island, sec-bovine) | Bacterial genetics |
| [26275216](https://pubmed.ncbi.nlm.nih.gov/26275216/) | SigB/Rot/SarA on tst promoter | F5 (σB repression, multifactorial control) | Bacterial genetics |
| [24816557](https://pubmed.ncbi.nlm.nih.gov/24816557/) | Superantigen enhancement of endotoxin shock | F6 (SEB/SEC, endotoxin synergy) | Review |
| [2494691](https://pubmed.ncbi.nlm.nih.gov/2494691/) | Analysis of TSS isolates producing SEB/SEC1 | F6 (nmTSS toxin distribution) | Human isolates |
| [12499191](https://pubmed.ncbi.nlm.nih.gov/12499191/) | CA- vs HA-MRSA molecular analysis | F6 (USA400 SEB/SEC, no TSST-1) | Bacterial epidemiology |
| [21282506](https://pubmed.ncbi.nlm.nih.gov/21282506/) | Genetic variation & superantigen cytokine polarization | F7 (protective/high-risk HLA) | Human immunogenetics |
| [12436116](https://pubmed.ncbi.nlm.nih.gov/12436116/) | Immunogenetic basis of invasive GAS outcomes | F7 (DRB1*1501/DQB1*0602 protective, P<0.0001) | Human immunogenetics |
| [11818153](https://pubmed.ncbi.nlm.nih.gov/11818153/) | Double-mutant/formaldehyde TSST-1 vaccine | F8 (protective toxoid; no human vaccine) | Rabbit vaccine |
| [12399195](https://pubmed.ncbi.nlm.nih.gov/12399195/) | Epitope mapping of neutralizing TSST-1 antibodies | F8 (N-terminal 1–15 epitope) | In vitro/rabbit |
| [17268555](https://pubmed.ncbi.nlm.nih.gov/17268555/) | Structural basis of TSST-1 T-cell activation | F9 (Vβ2.1 structure, MHC/TCR bridging) | Crystal structure |
| [21127057](https://pubmed.ncbi.nlm.nih.gov/21127057/) | CDR2β governs Vβ specificity | F9 (non-canonical CDR2β determinant) | Structural/functional |
| [17191165](https://pubmed.ncbi.nlm.nih.gov/17191165/) | Antibiotics & exotoxin gene expression | F10 (clindamycin/linezolid suppress; β-lactam induces) | In vitro bacterial |
| [30342546](https://pubmed.ncbi.nlm.nih.gov/30342546/) | Clindamycin suppresses virulence | F10 (clindamycin ↓TSST-1 even in resistant strains) | In vitro bacterial |
| [15777108](https://pubmed.ncbi.nlm.nih.gov/15777108/) | TSS in children: epidemiology & management | F11 (clinical phenotype, epidemiologic shift) | Review |

**Supporting/context papers reviewed but not primary to a finding** include the superantigen SElX bifunctional-toxin study ([PMID: 28880920](https://pubmed.ncbi.nlm.nih.gov/28880920/)), soluble high-affinity TCR neutralization of SEC ([PMID: 23161916](https://pubmed.ncbi.nlm.nih.gov/23161916/)), human neutralizing scFvs against TSST-1 ([PMID: 28218671](https://pubmed.ncbi.nlm.nih.gov/28218671/)), the ST22-PT MRSA clone with duplicated *tst* ([PMID: 38408643](https://pubmed.ncbi.nlm.nih.gov/38408643/)), exotoxin/endotoxin cytokine induction ([PMID: 29056305](https://pubmed.ncbi.nlm.nih.gov/29056305/)), and multiple invasive-GAS surveillance papers used to contrast staphylococcal with streptococcal TSS.

---

## Limitations and Knowledge Gaps

1. **HLA evidence is largely streptococcal.** The protective/high-risk haplotype data (Finding 7) were generated with streptococcal superantigens. Because both toxin families use identical MHC-II presentation, the inference to staphylococcal TSS is mechanistically sound but not directly demonstrated for TSST-1 in a large human cohort.
2. **EGFR host-directed therapy is preclinical.** AG1478 protection (Finding 3) is shown only in a rabbit model; no human trial data exist.
3. **No licensed human vaccine and limited human trial data.** Toxoid protection (Finding 8) is animal-only; human immunogenicity/efficacy remains unproven.
4. **IVIG evidence is largely extrapolated.** As with streptococcal TSS, controlled human trial evidence for IVIG and clindamycin adjuncts in staphylococcal TSS is limited and partly extrapolated from streptococcal/pediatric data.
5. **Case-definition insensitivity.** The CDC criteria under-capture early cases (Finding 2), meaning surveillance likely underestimates incidence and biases cohorts toward severe/late presentations.
6. **Model-organism gaps.** Murine T cells are relatively insensitive to human superantigens without LPS potentiation or HLA-transgenics, limiting mechanistic fidelity.
7. **Bacterial-regulation complexity.** The interplay of agr/sarA/σB/Rot on *tst* is condition-dependent; precise in-vivo triggers within the human vaginal micro-environment are inferred, not fully mapped.

---

## Proposed Follow-up Experiments / Actions

1. **HLA association study in staphylococcal TSS specifically** — genotype DRB1/DQB1 in a modern mTSS/nmTSS cohort (e.g., extend the French ICU registry) to confirm DR15/DQ6 protection and DR14/DR7/DQ5 risk for TSST-1 disease directly.
2. **Human-relevant EGFR-inhibition study** — evaluate approved EGFR TKIs or topical vaginal EGFR blockade in HLA-transgenic mouse or human vaginal organoid TSS models, then a safety/PK bridging study, to translate Finding 3.
3. **Toxoid vaccine advancement** — advance G31R/H135A double-mutant TSST-1 (± SEB/SEC toxoids as a multivalent candidate) into Phase I human immunogenicity trials, targeting the protective N-terminal 1–15 epitope.
4. **Prospective antibiotic-adjunct trial** — randomized evaluation of clindamycin (or linezolid) + IVIG versus standard care in staphylococcal TSS, powered on organ-failure-free days, to move Finding 10 from in-vitro rationale to clinical proof.
5. **Improved diagnostics** — develop a rapid point-of-care TSST-1/SEB/SEC toxin and *tst*/agr-type assay to overcome CDC-criteria insensitivity at presentation (Finding 2).
6. **Surveillance re-tooling** — reconcile physician-diagnosed vs criteria-based case ascertainment for staphylococcal TSS (as done for streptococcal STSS) to produce reliable modern incidence estimates.
7. **Host-modifier mechanism** — single-cell profiling of Vβ2 T-cell and monocyte responses across protective vs risk HLA backgrounds to define the IL-10/IFN-γ switch quantitatively.

---

*Report compiled from 11 confirmed findings and 63 reviewed papers across a 5-iteration autonomous investigation. Evidence types are distinguished as human clinical, bacterial genetics/epidemiology, animal model, in vitro, and structural/computational throughout.*


## Artifacts

- [OpenScientist final report](Staphylococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Staphylococcal_Toxic_Shock_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 17 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (2 mentions) - the report calls it "fever", "sign"; HP calls it **Fever**
- `GO:0002504` (2 mentions) - the report calls it "antigen processing and presentation of peptide or polysaccharide antigen via MHC class II", "MHC class II antigen presentation"; GO calls it **antigen processing and presentation of peptide or polysaccharide antigen via MHC class II**
- `HP:0000988` (1 mention) - the report calls it "sign"; HP calls it **Skin rash**
- `HP:0007550` (1 mention) - the report calls it "sign"; HP calls it **Hypohidrosis or hyperhidrosis**
- `HP:0001873` (1 mention) - the report calls it "lab"; HP calls it **Thrombocytopenia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `CHEBI:63591` (1 mention), reported as "linezolid" - CHEBI does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0002438` (2 mentions) - the report calls it "acute inflammatory response"; GO calls it **acute inflammatory response to antigenic stimulus**
- `GO:0032609` (2 mentions) - the report calls it "interferon-gamma production", "IFN-γ production"; GO calls it **type II interferon production**, and lists "IFNG production" among its other names
- `GO:0032640` (2 mentions) - the report calls it "tumor necrosis factor production", "TNF production"; GO calls it **tumor necrosis factor production**, and lists "TNF production" among its other names
- `HP:0011009` (2 mentions) - the report calls it "acute hypotension"; HP calls it **Acute**, and lists "Acute onset" among its other names
- `GO:0007173` (2 mentions) - the report calls it "epidermal growth factor receptor signaling pathway", "EGFR signaling"; GO calls it **epidermal growth factor receptor signaling pathway**, and lists "EGFR signaling pathway" among its other names
- `GO:0042288` (1 mention) - the report calls it "MHC class I protein binding — analog for MHC engagement"; GO calls it **MHC class I protein binding**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0032609` - called "interferon-gamma production", "IFN-γ production"
- `GO:0032640` - called "tumor necrosis factor production", "TNF production"
- `HP:0001945` - called "fever", "sign"
- `GO:0007173` - called "epidermal growth factor receptor signaling pathway", "EGFR signaling"
- `GO:0002504` - called "antigen processing and presentation of peptide or polysaccharide antigen via MHC class II", "MHC class II antigen presentation"