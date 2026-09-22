---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:14:49.760802'
end_time: '2026-09-21T05:02:12.820051'
duration_seconds: 2843.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: X-linked Dominant Chondrodysplasia Chassaing-Lacombe Type
  mondo_id: MONDO:0010463
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
citation_count: 10
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 17
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0010463
    reported_labels:
    - MONDO
    ontology_label: X-linked dominant chondrodysplasia, Chassaing-Lacombe type
  - term_id: HP:0005830
    reported_labels:
    - Poor skull mineralization
    ontology_label: Flexion contracture of toe
  - term_id: HP:0001010
    reported_labels:
    - Body/limb asymmetry
    ontology_label: Hypopigmentation of the skin
  - term_id: UBERON:0005430
    reported_labels:
    - growth plate
    ontology_label: ansa cervicalis
  - term_id: NCIT:C1531
    reported_labels:
    - histone deacetylase inhibitor
    ontology_label: Recombinant Eotaxin
  labels_variant: 8
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: X-linked_Dominant_Chondrodysplasia_Chassaing-Lacombe_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: X-linked_Dominant_Chondrodysplasia_Chassaing-Lacombe_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Dominant Chondrodysplasia Chassaing-Lacombe Type
- **MONDO ID:** MONDO:0010463 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked Dominant Chondrodysplasia Chassaing-Lacombe Type** covering all of the
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

# X-linked Dominant Chondrodysplasia, Chassaing–Lacombe Type — Comprehensive Disease Characterization Report

**Disease:** X-linked Dominant Chondrodysplasia, Chassaing–Lacombe Type
**Identifiers:** OMIM #300863 · ORPHA:163966 · MONDO:0010463 · MedGen C3275476/C4304401
**Causal gene:** *HDAC6* (Xp11.23; OMIM \*300272; HGNC:14064)
**Category:** Mendelian, X-linked dominant (male-lethal)

> **CRITICAL NOTE ON ETIOLOGY.** The template header pairs this disease with *MBTPS2*. That is **incorrect**. The verified causal gene for Chassaing–Lacombe chondrodysplasia (OMIM #300863) is **HDAC6**, via a 3′-UTR regulatory variant (Simon et al. 2010, [PMID: 20181727](https://pubmed.ncbi.nlm.nih.gov/20181727/)). *MBTPS2* causes a **different** set of X-linked disorders (IFAP/BRESHECK, keratosis follicularis spinulosa decalvans, X-linked Olmsted syndrome, and one form of osteogenesis imperfecta) and is discussed here only as a differential-diagnosis / look-alike gene. All etiologic, mechanistic, and therapeutic statements below refer to **HDAC6**.

---

## Summary

X-linked dominant chondrodysplasia of the Chassaing–Lacombe type is an **ultra-rare, X-linked dominant, male-lethal skeletal dysplasia** first delineated in a single large four-generation French family (Chassaing et al. 2005, [PMID: 16001442](https://pubmed.ncbi.nlm.nih.gov/16001442/)). Hemizygous males present with a severe, perinatally lethal congenital chondrodysplasia — severe platyspondyly, distinctive metaphyseal cupping of the metacarpals/metatarsals/phalanges, hydrocephaly with macrocephaly, and microphthalmia — while heterozygous females are far more mildly and variably affected, showing short stature, body/limb asymmetry, and mild intellectual disability. This male-severe/female-mild dichotomy with male lethality is the signature of X-linked dominant inheritance with variable expression in heterozygous carriers.

The molecular cause is a **3′-untranslated region (3′-UTR) variant in *HDAC6***, NM_006044.4:c.\*281A>T, which lies precisely within the seed-match site for the microRNA **hsa-miR-433** (Simon et al. 2010, [PMID: 20181727](https://pubmed.ncbi.nlm.nih.gov/20181727/)). The variant abolishes miR-433–mediated post-transcriptional repression of *HDAC6*, leading to **HDAC6 over-expression** and, downstream, to **profound α-tubulin hypoacetylation** — the biochemical signature of excess HDAC6 tubulin-deacetylase activity. This is a **gain-of-expression (dosage) mechanism**, at the opposite end of the dosage axis from loss of function: *Hdac6*-knockout mice are viable and fertile, underscoring that it is HDAC6 *excess*, not deficiency, that drives disease.

Because the entire disease-defining evidence base rests on **two primary papers (2005 clinical delineation; 2010 molecular mechanism)** describing a single family, many downstream sections of a standard disease template — natural-history cohorts, treatment trials, prognostic biomarkers, faithful animal models — are essentially empty for this specific condition. The pathophysiological bridge from HDAC6 over-expression to the skeletal phenotype is best explained through HDAC6's established role in **primary cilium disassembly** (the HEF1/NEDD9–Aurora-A–HDAC6 pathway) and the cilium's central role in growth-plate Hedgehog signaling — but this bridge is **inferred, not directly demonstrated in patients**. Confidence is HIGH for the causal gene/variant, inheritance, and core phenotype; MODERATE for the α-tubulin-hypoacetylation biomarker (single study); and LOW/INFERRED for the ciliary-Hedgehog growth-plate mechanism and any therapeutic rationale.

---

## Section 1 — Disease Information

**Overview.** X-linked dominant chondrodysplasia, Chassaing–Lacombe type, is a rare Mendelian skeletal dysplasia characterized in affected males by severe chondrodysplasia with platyspondyly, distinctive brachydactyly with metaphyseal cupping, hydrocephaly, and microphthalmia, with perinatal lethality; heterozygous females show a milder, variable phenotype (short stature, body asymmetry, mild intellectual disability). It was originally delineated by Chassaing, Lacombe and colleagues in 2005.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #300863 — "Chondrodysplasia with platyspondyly, distinctive brachydactyly, hydrocephaly, and microphthalmia" |
| Orphanet | ORPHA:163966 |
| MONDO | MONDO:0010463 |
| MedGen | C3275476 / C4304401 |
| Gene | *HDAC6* (OMIM \*300272; HGNC:14064; Xp11.23) |
| ICD-10 / ICD-11 | No disease-specific code (grouped under skeletal dysplasias / Q77–Q78) |
| MeSH | No dedicated MeSH descriptor |

**Synonyms / alternative names.** Chassaing–Lacombe chondrodysplasia; X-linked dominant chondrodysplasia with platyspondyly, distinctive brachydactyly, hydrocephaly, and microphthalmia. Orphanet classifies it among X-linked syndromic intellectual disability disorders (germline *HDAC6* mutation), last reviewed February 2011 by Pr Didier Lacombe.

**Data provenance.** Information derives from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, MedGen, ClinVar) and from **individual-patient clinical/molecular reports** of a single extended family — not from EHR or large registries.

---

## Section 2 — Etiology

**Primary cause (genetic).** The disease is monogenic and X-linked. The causal lesion is the germline *HDAC6* 3′-UTR variant **c.\*281A>T**, which segregates completely with disease in the founding family and disrupts the hsa-miR-433 seed site, de-repressing *HDAC6* (Simon et al. 2010, [PMID: 20181727](https://pubmed.ncbi.nlm.nih.gov/20181727/)).

> "We have identified a variant (c.\*281A>T) in the 3′ untranslated region (UTR) of the HDAC6 gene that totally segregates with the disease. The variant is located in the seed sequence of hsa-miR-433." — Simon et al. 2010

**Genetic risk factors.** The disease-causing variant itself is the sole established genetic determinant. In heterozygous females, the **pattern of X-inactivation** acts as a modifier of expressivity: skewing toward expression of the mutant allele in a given tissue increases local severity (see Sections 5 and 9).

**Environmental risk factors / protective factors / gene–environment interactions.** **Not applicable / none reported.** As a fully penetrant Mendelian variant, there are no established environmental risk factors, protective alleles, or gene–environment interactions. No modifier genes beyond X-inactivation status have been identified.

---

## Section 3 — Phenotypes

Phenotypes are drawn from Chassaing et al. 2005 ([PMID: 16001442](https://pubmed.ncbi.nlm.nih.gov/16001442/)) and the OMIM #300863 clinical synopsis. The phenotype is strongly **sex-dimorphic**.

### Affected males (severe, perinatally lethal)

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Intrauterine growth retardation | HP:0001511 | Growth | Prenatal onset |
| Hydrocephaly | HP:0000238 | CNS/structural | Detectable prenatally |
| Macrocephaly | HP:0000256 | Craniofacial | |
| Frontal bossing | HP:0002007 | Craniofacial | |
| Microphthalmia | HP:0000568 | Ocular | |
| Small, low-set ears | HP:0000369 | Craniofacial | |
| Short flat nose | HP:0003196 / HP:0005280 | Craniofacial | |
| Poor skull mineralization | HP:0005830 | Skeletal | |
| Severe platyspondyly | HP:0000926 | Skeletal | Core radiographic sign |
| Thin ribs | HP:0000883 | Skeletal | |
| Eleven pairs of ribs | HP:0000878 | Skeletal | In 2 patients |
| Iliac wing hypoplasia | HP:0002866 | Skeletal | Poor pubic ossification |
| Metaphyseal cupping (metacarpals/metatarsals/phalanges) | HP:0003021 | Skeletal | **Distinctive** sign |
| Brachydactyly | HP:0001156 | Skeletal | |
| Hypoplastic calcaneus | — | Skeletal | |

**Bone histology (males):** severe flattening of poorly delimited, under-ossified vertebral body anlagen; intervertebral disks thickened with abnormal craniocaudal orientation of fibroblasts.

### Affected females (mild, variable)

| Phenotype | HPO term | Type |
|---|---|---|
| Short stature | HP:0004322 | Growth |
| Body/limb asymmetry | HP:0001010 | Physical |
| Mild intellectual disability | HP:0001256 | Neurodevelopmental |

> "Radiographs showed severe platyspondyly and various bone abnormalities including a distinctive metaphyseal cupping of the metacarpals, metatarsals, and phalanges. The affected females were less affected and showed small stature, sometimes associated with body asymmetry and mild mental retardation." — Chassaing et al. 2005

**Characteristics.** *Onset:* congenital/prenatal in males; childhood-apparent in females. *Severity:* severe (males) vs. mild (females). *Progression:* males die perinatally (no progression observed); female features are essentially stable/static. *Frequency:* within the single reported family, described features were present in essentially all affected males; female features were milder and variable. **Quality-of-life data (EQ-5D/SF-36) are not available** for this ultra-rare disease.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *HDAC6* (histone deacetylase 6), Xp11.23; OMIM \*300272; HGNC:14064; NCBI Gene 10013.

**Pathogenic variant.**
- **Founding variant:** NM_006044.4:c.\*281A>T, in the 3′-UTR (exon 29), within the hsa-miR-433 seed match. **Variant type:** non-coding regulatory (3′-UTR / miRNA-binding-site). **Functional consequence:** gain of expression — loss of miR-433 repression → HDAC6 over-expression (demonstrated at protein level in affected fetal thymus). **Origin:** germline. **Classification:** pathogenic in the context of complete segregation (LOD 3.30) and functional validation, though it predates formal ACMG/AMP frameworks.
- **Additional candidate:** ClinVar lists a separate missense candidate NM_006044.4(HDAC6):c.2090C>T (p.Thr697Ile), RCV001198391, annotated to this disease — suggesting possible further allelic heterogeneity, though not independently validated here.

> "The HDAC6 protein was found to be over-expressed in thymus from an affected male fetus." — Simon et al. 2010

**Allele frequency.** The private c.\*281A>T variant is not a population polymorphism; no meaningful gnomAD frequency is expected for a private, disease-segregating, male-lethal allele.

**Functional consequence class.** Gain of expression / gain of function at the pathway level (excess deacetylase activity), NOT loss of function. This is the key dosage insight: *Hdac6*-null mice are viable and fertile (Zhang et al. 2008, [PMID: 18180281](https://pubmed.ncbi.nlm.nih.gov/18180281/)).

**Modifier genes / epigenetics.** The principal modifier of expression in females is **X-chromosome inactivation** (tissue-level mosaicism); the disease mechanism itself is a **post-transcriptional (miRNA-regulation) defect**. No DNA-methylation or histone-modification disease signatures are reported.

**Chromosomal abnormalities.** None; the disorder is a point variant, not a structural/aneuploidy syndrome.

---

## Section 5 — Environmental Information

**Not applicable.** No environmental factors, toxins, lifestyle factors, or infectious agents are implicated. This is a purely genetic Mendelian disorder.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. Germline *HDAC6* 3′-UTR variant **c.\*281A>T** disrupts the **hsa-miR-433 seed-match site** → **leads to** loss of miR-433 binding to the *HDAC6* transcript. *(Directly demonstrated: reporter and endogenous assays in MG63 cells.)*
2. Loss of miR-433 repression **results in** **HDAC6 mRNA/protein over-expression**. *(Directly demonstrated: HDAC6 protein elevated in affected fetal thymus and in left-arm fibroblasts of an asymmetric female.)*
3. Excess HDAC6 (a cytoplasmic α-tubulin deacetylase) **leads to** **profound α-tubulin hypoacetylation** (with increased total α-tubulin). *(Directly demonstrated in affected fetal thymus.)*
4. **[INFERRED]** Tubulin hypoacetylation and elevated HDAC6 activity **result in** destabilization / premature disassembly of the **primary cilium** in relevant cell types, via the established HEF1/NEDD9–Aurora-A–HDAC6 ciliary-resorption pathway. *(Inferred from HDAC6 cilia biology; not shown in patients.)*
5. **[INFERRED]** In **growth-plate chondrocytes**, cilium destabilization **leads to** attenuated ciliary **Indian Hedgehog (IHH)** and mechanotransduction signaling. *(Inferred.)*
6. **[INFERRED]** Disorganized chondrocyte proliferation/hypertrophy and defective endochondral ossification **result in** platyspondyly, metaphyseal cupping, brachydactyly, and the broader chondrodysplasia. *(Inferred.)*

**Branch (females):** X-inactivation mosaicism determines, tissue-by-tissue, whether the mutant allele is expressed → focal HDAC6 over-expression → **lateralized/asymmetric** skeletal and growth phenotype.

> "Concomitantly, the level of total alpha-tubulin, a target of HDAC6, was found to be increased in the affected fetal thymus, whereas the level of acetylated alpha-tubulin was found to be profoundly decreased." — Simon et al. 2010

> "The mutated HDAC6 allele was expressed in 31% of left arm-derived fibroblasts, whereas it was not expressed in the right arm. Overexpression of HDAC6 was observed in left arm-derived fibroblasts." — Simon et al. 2010

### ASCII schematic

```
 c.*281A>T (HDAC6 3'-UTR, miR-433 seed)
            │ abolishes miR-433 binding   [DEMONSTRATED]
            ▼
   HDAC6 over-expression                  [DEMONSTRATED - fetal thymus]
            │ excess tubulin deacetylase
            ▼
   α-tubulin HYPOacetylation              [DEMONSTRATED - fetal thymus]
            │
            ▼   (HEF1/NEDD9–AuroraA–HDAC6)
   Primary cilium destabilization         [INFERRED]
            │
            ▼
   ↓ ciliary IHH / mechano-signaling      [INFERRED]
            │
            ▼
   Disorganized growth-plate ossification [INFERRED]
            │
            ▼
   Platyspondyly · metaphyseal cupping · chondrodysplasia
```

**Molecular pathways / cellular processes.** Post-transcriptional gene regulation (microRNA silencing), tubulin acetylation/deacetylation homeostasis, primary-cilium assembly/disassembly cycle, and (inferred) Hedgehog signaling in the growth plate. Suggested GO terms: *histone deacetylase activity* (GO:0004407), *tubulin deacetylase activity* (GO:0042903), *protein deacetylation* (GO:0006476), *cilium disassembly* (GO:0061523), *smoothened signaling pathway* (GO:0007224), *endochondral ossification* (GO:0001958). Suggested CL terms: *chondrocyte* (CL:0000138), *growth-plate chondrocyte*.

**Protein dysfunction.** HDAC6 (class IIb deacetylase; two catalytic domains + ZnF-UBP ubiquitin-binding domain) is over-abundant; substrates include α-tubulin, HSP90, and cortactin, and it mediates aggresome formation/autophagic clearance (Zhu 2023 [PMID: 37002569](https://pubmed.ncbi.nlm.nih.gov/37002569/); Su 2010 [PMID: 21416996](https://pubmed.ncbi.nlm.nih.gov/21416996/)). Excess deacetylase activity, not misfolding, is the defect.

**Metabolic / immune / biochemical.** No specific metabolic or immune abnormality is implicated in the disease itself. The measurable biochemical abnormality is decreased acetylated α-tubulin.

### Supporting HDAC6–cilia literature

> "interactions between the prometastatic scaffolding protein HEF1/Cas-L/NEDD9 and the oncogenic Aurora A (AurA) kinase at the basal body of cilia causes phosphorylation and activation of HDAC6, a tubulin deacetylase, promoting ciliary disassembly" — Pugacheva et al. 2007, [PMID: 17604723](https://pubmed.ncbi.nlm.nih.gov/17604723/)

Plk1 also activates HDAC6 to drive ciliary deacetylation/resorption before mitosis (Wang et al. 2013, [PMID: 23345402](https://pubmed.ncbi.nlm.nih.gov/23345402/)).

---

## Section 7 — Anatomical Structures Affected

- **Primary organs / systems:** the **skeleton / skeletal system** (UBERON:0001434), especially the **vertebral column** (UBERON:0001130 → platyspondyly), **growth plate** (UBERON:0005430), and tubular bones of hands/feet (metaphyseal cupping, brachydactyly). Also the **central nervous system** — **ventricular system of brain** (hydrocephaly) — and the **eye** (UBERON:0000970 → microphthalmia).
- **Secondary involvement:** craniofacial skeleton (skull hypoplasia, frontal bossing), ribs, ilium/pubis.
- **Tissue level:** connective tissue / cartilage; affected cell population = **chondrocytes** (CL:0000138), particularly growth-plate chondrocytes; intervertebral-disk fibroblasts show abnormal orientation.
- **Subcellular level (GO CC):** **microtubule cytoskeleton** (GO:0015630), **ciliary axoneme** (GO:0005930), **cytoplasm** (GO:0005737). HDAC6 is predominantly cytoplasmic.
- **Localization / lateralization:** males — generalized/bilateral skeletal involvement; females — characteristically **asymmetric/lateralized** (e.g., unilateral limb hypotrophy) owing to X-inactivation mosaicism.

---

## Section 8 — Temporal Development

- **Onset:** **congenital/prenatal** in males (IUGR, hydrocephaly, and skeletal abnormalities detectable on prenatal ultrasound); childhood-apparent in females.
- **Onset pattern:** chronic/congenital (developmental).
- **Progression / course:** in males, **perinatally lethal** — three affected male fetuses were terminated after prenatal detection, and a fourth died at 6 days of life; effectively no postnatal progression is observed. In females, features (short stature, asymmetry, mild ID) are **static/stable and lifelong**.
- **Critical period:** intrauterine skeletal development (endochondral ossification) is the window of vulnerability and, in principle, the only window for hypothetical intervention.

> "Identification of skeletal abnormalities and hydrocephaly during the pregnancy of three male fetuses led to termination of the pregnancies. A fourth affected male died at 6 days of life." — Chassaing et al. 2005

---

## Section 9 — Inheritance and Population

- **Inheritance pattern:** **X-linked dominant, male-lethal.** Hemizygous males are severely affected and die perinatally; heterozygous females are mildly/variably affected. Original pedigree: 4 affected males and 6 affected females across 4 generations.
- **Gene mapping:** Xp11.3–q13.1, 24-Mb interval, LOD = 3.30 (Simon et al. 2010).
- **Penetrance:** high/complete for the molecular genotype; **expressivity is highly variable in females**, governed by X-inactivation.
- **Germline mosaicism / anticipation / founder effects / consanguinity:** not reported / not applicable.
- **Epidemiology:** described in a **single large French family**; Orphanet lists prevalence as "unknown" — effectively **ultra-rare (<1/1,000,000)**. No incidence figures exist.
- **Sex ratio / demographics:** disease burden falls on hemizygous males (lethal) and heterozygous females (mild). No ethnic predilection can be established from one family.

> "The disease locus was ascribed to a 24 Mb interval in Xp11.3-q13.1. We have identified a variant (c.\*281A>T) in the 3′ untranslated region (UTR) of the HDAC6 gene that totally segregates with the disease." — Simon et al. 2010

---

## Section 10 — Diagnostics

- **Imaging (cornerstone of clinical diagnosis):** skeletal radiography demonstrating **severe platyspondyly**, **distinctive metaphyseal cupping** of metacarpals/metatarsals/phalanges, poor skull mineralization, thin ribs (sometimes 11 pairs), iliac wing hypoplasia. **Prenatal ultrasound** detects skeletal abnormalities and hydrocephaly in affected male fetuses.
- **Histopathology:** flattened, under-ossified vertebral anlagen; thickened intervertebral disks with abnormally oriented fibroblasts.
- **Biochemical marker (research):** decreased **acetylated α-tubulin** / increased total α-tubulin and HDAC6 over-expression in patient tissue — a research biomarker, not a validated clinical assay.
- **Genetic testing (definitive):** targeted sequencing of *HDAC6* **including the 3′-UTR** (essential — a coding-only panel or a standard exome pipeline may miss the c.\*281A>T regulatory variant). WES/WGS with attention to non-coding/3′-UTR regions and X-linkage; segregation analysis; X-inactivation studies in females to interpret expressivity.
- **Differential diagnosis:** other platyspondylic/lethal skeletal dysplasias; MBTPS2- and MBTPS1-related skeletal disorders (allelic-gene look-alikes on the X); X-linked syndromic intellectual-disability disorders. Distinguishing feature: the *HDAC6* 3′-UTR miR-433 variant with male lethality and female asymmetry.
- **Screening:** in a known family — prenatal testing / cascade testing for the familial variant; preimplantation genetic testing is feasible in principle. No population newborn screening exists.

---

## Section 11 — Outcome / Prognosis

- **Males:** **perinatally lethal** — near-uniform demise in utero or within days of birth. Prognosis is grave.
- **Females:** **normal or near-normal life expectancy** with lifelong but mild morbidity — short stature, body/limb asymmetry, and mild intellectual disability; no reported progressive organ failure.
- **Prognostic factors:** sex (hemizygous vs. heterozygous) is the dominant determinant; in females, degree and direction of X-inactivation skewing modulates severity.
- **Complications / QoL / survival statistics:** no formal cohort survival data, QoL instruments, or standardized morbidity metrics exist for this ultra-rare disorder.

---

## Section 12 — Treatment

- **Disease-specific therapy:** **none exists.** Management is **supportive** and centered on **reproductive/genetic counseling**.
- **Supportive care:** for surviving females, standard management of short stature, orthopedic monitoring of asymmetry, and developmental/educational support for mild intellectual disability.
- **Mechanistically rational but untested concept:** **HDAC6-selective inhibitors** (e.g., tubastatin A, tubacin, ricolinostat/ACY-1215) restore α-tubulin acetylation without altering histone acetylation (Depetter 2019 [PMID: 30694564](https://pubmed.ncbi.nlm.nih.gov/30694564/); Zhang 2014 [PMID: 24844691](https://pubmed.ncbi.nlm.nih.gov/24844691/)). In principle they could counter HDAC6-excess biochemistry, but there is **no preclinical or clinical evidence in this disease**, and the lethal skeletal phenotype arises in utero, limiting postnatal therapeutic windows. Suggested NCIT concept: *histone deacetylase inhibitor* (NCIT:C1531).

> "Selective HDAC6 inhibitors resulted in α-tubulin acetylation with no impact on histone acetylation" — Depetter et al. 2019

---

## Section 13 — Prevention

- **Primary prevention:** not applicable (Mendelian congenital disorder) except through reproductive planning.
- **Genetic counseling / screening:** the mainstay. For families carrying the c.\*281A>T variant — carrier identification in females, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** to prevent transmission; counseling regarding 50% transmission risk and sex-dependent outcome (affected males lethal, affected females mild).
- **Behavioral / public-health / immunization / prophylaxis:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthology:** *HDAC6* is highly conserved with 1:1 orthologs across >160 organisms — mouse *Hdac6* (NCBI Gene 15185; MGI:1333752), rat *Hdac6* (RGD 619981), zebrafish *hdac6* (NCBI Gene 565482; ZFIN); HomoloGene 31353. Structural divergence exists: the human protein carries 8 SE14 tetradecapeptide repeats absent from mouse, *Drosophila*, and *C. elegans* orthologs (Bertos et al. 2004).
- **Natural disease in other species:** **none reported.** No naturally occurring HDAC6 chondrodysplasia in companion animals or wildlife was identified (no OMIA entry for a comparable phenotype).
- **Zoonotic potential:** not applicable.

---

## Section 15 — Model Organisms

- **Available in vivo tool:** the constitutive **Hdac6-knockout mouse** (Zhang et al. 2008, [PMID: 18180281](https://pubmed.ncbi.nlm.nih.gov/18180281/)) — **viable, fertile, hyperacetylated tubulin**, with only a small increase in cancellous bone mineral density. This is a **loss-of-function** tool and therefore does **NOT** model the disease, which is caused by HDAC6 **over-expression**.
- **Missing models:** **no** knock-in of the c.\*281A>T 3′-UTR / miR-433-site variant, and **no** HDAC6-overexpression skeletal model recapitulating the human chondrodysplasia has been published. This is a major gap.
- **Zebrafish relevance:** zebrafish crispant screening is an established platform for skeletal-dysplasia gene validation ([PMID: 39817421](https://pubmed.ncbi.nlm.nih.gov/39817421/)), offering a route to model growth-plate/ciliary consequences of *hdac6* dysregulation.

> "HDAC6-deficient mice are viable and fertile and show hyperacetylated tubulin in most tissues... the lack of HDAC6 results in a small increase in cancellous bone mineral density." — Zhang et al. 2008

---

## Mechanistic Model / Interpretation

The unifying model is a **dosage disorder of a tubulin deacetylase driven by loss of microRNA control**. A single non-coding base change (c.\*281A>T) removes miR-433 repression, HDAC6 protein rises, and α-tubulin becomes hypoacetylated. Because HDAC6 is the effector deacetylase in the HEF1/NEDD9–Aurora-A–HDAC6 (and Plk1) primary-cilium disassembly pathway, its over-abundance plausibly destabilizes cilia in chondrocytes, blunting ciliary Hedgehog/mechanotransduction that orchestrates growth-plate maturation and endochondral ossification — producing platyspondyly, metaphyseal cupping, and the broader chondrodysplasia. The **X-inactivation branch** elegantly explains the female phenotype: the direct demonstration that the mutant allele was expressed (and HDAC6 over-expressed) only in the *hypotrophic left-arm* fibroblasts of an asymmetric female ties tissue-level mosaicism directly to lateralized disease.

Two dosage anchors bracket the model: **loss** of HDAC6 (knockout mouse) is benign, while **gain** (this disease) is severe and male-lethal — establishing that the pathogenic direction is over-expression, and that HDAC6-selective inhibition is the mechanistically logical (if unproven) countermeasure.

| Feature | Males (hemizygous) | Females (heterozygous) |
|---|---|---|
| HDAC6 expression | Uniformly ↑ | Mosaic ↑ (X-inactivation-dependent) |
| Skeletal phenotype | Severe, generalized | Mild, asymmetric |
| CNS/eye | Hydrocephaly, microphthalmia | Mild ID |
| Outcome | Perinatal lethal | Near-normal lifespan |

---

## Evidence Base

| PMID | Paper (abbrev.) | Role |
|---|---|---|
| [16001442](https://pubmed.ncbi.nlm.nih.gov/16001442/) | *X-linked dominant chondrodysplasia with platyspondyly, distinctive brachydactyly, hydrocephaly, and microphthalmia* (Chassaing et al. 2005) | Clinical/radiographic delineation; pedigree; inheritance; male lethality |
| [20181727](https://pubmed.ncbi.nlm.nih.gov/20181727/) | *A mutation in the 3′-UTR of HDAC6 abolishing hsa-miR-433 regulation...* (Simon et al. 2010) | **Defining molecular paper** — causal variant, HDAC6 over-expression, α-tubulin hypoacetylation, X-inactivation–asymmetry link |
| [18180281](https://pubmed.ncbi.nlm.nih.gov/18180281/) | *Mice lacking HDAC6...* (Zhang et al. 2008) | Establishes dosage model (loss-of-function benign); bone-density role |
| [17604723](https://pubmed.ncbi.nlm.nih.gov/17604723/) | *HEF1-dependent Aurora A activation induces disassembly of the primary cilium* (Pugacheva et al. 2007) | Basis for inferred HDAC6→cilium mechanism; HDAC6 inhibitors stabilize cilia |
| [23345402](https://pubmed.ncbi.nlm.nih.gov/23345402/) | *PCM1 recruits Plk1...* (Wang et al. 2013) | Plk1–HDAC6 ciliary resorption, reinforcing cilium mechanism |
| [30694564](https://pubmed.ncbi.nlm.nih.gov/30694564/) | *Selective pharmacological inhibitors of HDAC6...* (Depetter et al. 2019) | HDAC6-selective inhibitors restore α-tubulin acetylation — therapeutic rationale |
| [24844691](https://pubmed.ncbi.nlm.nih.gov/24844691/) | *Tubastatin A/ACY-1215...* (2014) | Further HDAC6-inhibitor pharmacology |
| [37002569](https://pubmed.ncbi.nlm.nih.gov/37002569/) / [21416996](https://pubmed.ncbi.nlm.nih.gov/21416996/) | HDAC6 biology reviews | Structure, substrates, aggresome/autophagy roles |
| [19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/), [23316014](https://pubmed.ncbi.nlm.nih.gov/23316014/), [20672378](https://pubmed.ncbi.nlm.nih.gov/20672378/), [34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/) | MBTPS2 disorder papers | **Background on allelic look-alike gene — NOT causal for this disease** |

**Important correction embedded in the evidence base:** early iterations of this investigation initially attributed the disease to *MBTPS2* (an X-linked intramembrane protease in the SREBP/cholesterol pathway). That attribution was **overturned** — MBTPS2 variants cause IFAP/KFSD/Olmsted syndromes and one form of osteogenesis imperfecta, distinct X-linked disorders. The definitive genetic mapping and functional work (Simon et al. 2010) unambiguously identifies *HDAC6* as causal for Chassaing–Lacombe chondrodysplasia.

---

## Limitations and Knowledge Gaps

1. **n = 1 family.** The entire disease is defined by a single French pedigree; prevalence, penetrance ranges, and phenotypic spectrum cannot be generalized.
2. **Closed evidence base.** Targeted searches found **no new primary reports since 2010**; the disease knowledge is effectively frozen at the two founding papers.
3. **Single-study biomarker.** The α-tubulin-hypoacetylation signature rests on one study's fetal-thymus assay.
4. **Inferred, not demonstrated, growth-plate mechanism.** The cilium→Hedgehog→chondrodysplasia bridge is extrapolated from HDAC6 cilia biology; it has not been shown in patient chondrocytes or growth plate.
5. **No disease model.** No knock-in of c.\*281A>T and no HDAC6-overexpression skeletal model exist; the available mouse is loss-of-function.
6. **No therapy evidence.** HDAC6-inhibitor rescue is purely conceptual, and prenatal lethality of males constrains the intervention window.
7. **Possible allelic heterogeneity unconfirmed.** A ClinVar missense candidate (p.Thr697Ile) is annotated but not independently validated.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a faithful animal model:** knock-in the *HDAC6* 3′-UTR c.\*281A>T variant (or a chondrocyte-targeted HDAC6-overexpression allele) in mouse or zebrafish; phenotype the growth plate (Alizarin Red, microCT) and vertebral ossification. Zebrafish crispant/overexpression screening ([PMID: 39817421](https://pubmed.ncbi.nlm.nih.gov/39817421/)) offers a rapid route.
2. **Test the ciliary hypothesis directly:** in patient-derived (or iPSC-derived) chondrocytes, quantify primary-cilium length/frequency, ciliary α-tubulin acetylation, and Hedgehog pathway output (GLI targets) vs. controls; test rescue by HDAC6-selective inhibitors (tubastatin A, ACY-1215).
3. **Validate the biomarker:** replicate the α-tubulin-hypoacetylation finding in additional patient tissues/fibroblasts and correlate with X-inactivation status.
4. **Resolve allelic heterogeneity:** functionally characterize the ClinVar p.Thr697Ile candidate and screen additional chondrodysplasia cohorts (including 3′-UTR/non-coding analysis) for further *HDAC6* variants.
5. **Refine molecular diagnostics:** ensure diagnostic pipelines explicitly interrogate the *HDAC6* 3′-UTR / miR-433 site, which coding-focused panels would miss.
6. **Counseling infrastructure:** formalize prenatal-diagnosis and PGT-M protocols for affected families.

---

*Confidence grading:* **HIGH** — causal gene/variant (*HDAC6* c.\*281A>T), X-linked dominant male-lethal inheritance, and core male/female phenotype (directly demonstrated). **MODERATE** — α-tubulin-hypoacetylation biomarker (single study). **LOW / INFERRED** — cilium–Hedgehog growth-plate mechanism and HDAC6-inhibitor therapeutic rationale (extrapolated, untested in this disease).


## Artifacts

- [OpenScientist final report](X-linked_Dominant_Chondrodysplasia_Chassaing-Lacombe_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](X-linked_Dominant_Chondrodysplasia_Chassaing-Lacombe_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 30 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010463` (2 mentions) - the report calls it "MONDO"; MONDO calls it **X-linked dominant chondrodysplasia, Chassaing-Lacombe type**
- `HP:0005830` (1 mention) - the report calls it "Poor skull mineralization"; HP calls it **Flexion contracture of toe**
- `HP:0001010` (1 mention) - the report calls it "Body/limb asymmetry"; HP calls it **Hypopigmentation of the skin**
- `UBERON:0005430` (1 mention) - the report calls it "growth plate"; UBERON calls it **ansa cervicalis**
- `NCIT:C1531` (1 mention) - the report calls it "histone deacetylase inhibitor"; NCIT calls it **Recombinant Eotaxin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000238` (1 mention) - the report calls it "Hydrocephaly"; HP calls it **Hydrocephalus**, and lists "Hydrocephaly" among its other names
- `HP:0000369` (1 mention) - the report calls it "Small, low-set ears"; HP calls it **Low-set ears**
- `HP:0000926` (1 mention) - the report calls it "Severe platyspondyly"; HP calls it **Platyspondyly**
- `HP:0000878` (1 mention) - the report calls it "Eleven pairs of ribs"; HP calls it **11 pairs of ribs**
- `HP:0002866` (1 mention) - the report calls it "Iliac wing hypoplasia"; HP calls it **Hypoplastic iliac wing**, and lists "Small iliac wings" among its other names
- `HP:0003021` (1 mention) - the report calls it "Metaphyseal cupping (metacarpals/metatarsals/phalanges)"; HP calls it **Metaphyseal cupping**
- `UBERON:0001434` (1 mention) - the report calls it "skeleton / skeletal system"; UBERON calls it **skeletal system**
- `GO:0005930` (1 mention) - the report calls it "ciliary axoneme"; GO calls it **axoneme**, and lists "ciliary axoneme" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000138` - called "chondrocyte", "chondrocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.