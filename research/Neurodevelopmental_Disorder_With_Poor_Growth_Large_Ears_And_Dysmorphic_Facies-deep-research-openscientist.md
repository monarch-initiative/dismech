---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-18T23:00:16.442172'
end_time: '2026-10-18T23:14:49.102077'
duration_seconds: 872.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Poor Growth, Large Ears, And Dysmorphic
    Facies
  mondo_id: MONDO:0859350
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
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 80
  verified: 75
  not_found: 0
  obsolete: 3
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCBITaxon:10116
    reported_labels:
    - Zfp668
    ontology_label: Rattus norvegicus
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0043968
    ontology_label: obsolete histone H2A acetylation
  - term_id: GO:0016573
    ontology_label: obsolete histone acetylation
  - term_id: NCIT:C159044
    ontology_label: GDC Gene Symbol Terminology
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
  path: Neurodevelopmental_Disorder_With_Poor_Growth_Large_Ears_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Poor_Growth_Large_Ears_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Poor Growth, Large Ears, And Dysmorphic Facies
- **MONDO ID:** MONDO:0859350 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Poor Growth, Large Ears, And Dysmorphic Facies** covering all of the
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

# Neurodevelopmental Disorder With Poor Growth, Large Ears, and Dysmorphic Facies (NEDGDF / ZNF668-related ZMAND)

**MONDO:0859350 · OMIM:620194 · Gene: ZNF668 (HGNC:25821)**

Comprehensive disease-knowledge-base report. Evidence base is small (one defining publication describing 3 affected individuals from 2 consanguineous families, plus in-vitro cancer-biology literature on ZNF668 function). Evidence-source types are flagged throughout as **[human clinical]**, **[in vitro]**, or **[computational]**.

---

## Summary (Answer to the Research Question)

Neurodevelopmental Disorder With Poor Growth, Large Ears, and Dysmorphic Facies (NEDGDF; proposed clinical name **ZNF668-related ZMAND** — *ZNF668-related brain malformation, microcephaly, abnormal growth, neurodevelopmental delay, and dysmorphism*) is an ultra-rare **autosomal-recessive Mendelian disorder of the DNA-damage-repair (DDR) machinery** caused by **biallelic truncating (loss-of-function) variants in *ZNF668*** (zinc finger protein 668), a nucleolar C2H2 zinc-finger protein on chromosome 16p11.2. Loss of ZNF668 impairs Tip60(KAT5)-dependent histone H2AX acetylation/chromatin relaxation and homologous-recombination repair, and destabilizes p53 via MDM2, producing genome instability. Clinically it presents in infancy with prenatal-onset growth restriction (small for gestational age, failure to thrive), microcephaly, severe global developmental delay/intellectual disability, hypotonia, brain malformation/atrophy, and a recognizable facial gestalt (large ears/macrotia, prominent nose, deep-set eyes). It was delineated by Alsaif et al., 2021 (**PMID 34313816**). There is no specific therapy; management is supportive.

---

## 1. Disease Information

**Overview.** A recognizable autosomal-recessive multisystem neurodevelopmental/dysmorphic syndrome in the growing class of **Mendelian DNA-damage-repair disorders**. First formally delineated as a distinct entity in 2021 **[human clinical]**: *"We present new evidence of a distinct disorder caused by biallelic truncating variants in ZNF668 comprising microcephaly, growth deficiency, severe global developmental delay, brain malformation, and distinct facial dysmorphism."* (Alsaif et al., PMID 34313816).

**Key identifiers.**
- **MONDO:** MONDO:0859350
- **OMIM (phenotype):** 620194
- **OMIM (gene):** 617103 (*ZNF668*)
- **MedGen:** C5774288 / CUI 1824061; **UMLS:** C5774288
- **Orphanet:** No specific ORPHAcode identified at time of writing (not available / likely pending).
- **ICD-10:** No specific code; best fit Q87.8 (other specified congenital malformation syndromes) / within Q87 + associated codes for microcephaly (Q02) and intellectual disability (F7x). **ICD-11:** best fit LD2F.1Y / LD90.Y (other specified syndromes with CNS/developmental anomalies) — no bespoke code.
- **MeSH:** No specific descriptor; indexed under Neurodevelopmental Disorders (D065886), Intellectual Disability (D008607), Microcephaly (D008831), DNA Repair-Deficiency Disorders (D049914).

**Synonyms / alternative names.**
- Neurodevelopmental disorder with poor growth, large ears, and dysmorphic facies (NEDGDF)
- ZNF668-related ZMAND (ZNF668-related brain malformation, microcephaly, abnormal growth, neurodevelopmental delay, and dysmorphism)
- ZNF668 deficiency / ZNF668-related DNA-damage-repair disorder

**Information source.** Disease-level aggregated resources (OMIM, MONDO, HPO) **derived from individual-patient case reports** in a single primary publication (PMID 34313816; 3 patients). Not EHR-derived at population scale.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) **truncating loss-of-function variants in *ZNF668*** **[human clinical]** (PMID 34313816). This is a monogenic, fully genetic etiology; no environmental or infectious cause.

**Genetic risk factors.**
- **Causal variants:** biallelic truncating (nonsense/frameshift) *ZNF668* variants. Both reported families were **consanguineous** → homozygous variants by descent.
- **Susceptibility loci / modifier genes:** none established (n too small).

**Environmental risk factors.** The only recognized "risk factor" is **parental consanguinity / shared ancestry** increasing homozygosity for rare recessive alleles. No toxin, radiation, lifestyle, or occupational exposure is implicated as a cause. (Note: because the protein participates in repair of exogenous DNA damage, DNA-damaging exposures such as ionizing/UV radiation are mechanistically relevant stressors in vitro, but are **not** disease causes.)

**Protective factors.** None identified. Being a **heterozygous carrier** is protective relative to biallelic loss (carriers are unaffected); i.e., a single functional allele is sufficient (recessive).

**Gene–environment interactions.** Not characterized. Plausible but undemonstrated interaction between residual DDR capacity and genotoxic exposure (**inferred**, not shown in patients).

---

## 3. Phenotypes

Phenotype frequencies below are from HPO annotation of OMIM:620194 (source PMID 34313816; denominators reflect the 3 reported individuals; **[human clinical]**). Onset is **infantile/congenital** (HP:0003593 Infantile onset, 3/3). Course is chronic and non-remitting; severity of neurodevelopmental impairment is **severe**. Quality-of-life impact is **profound** given severe developmental delay/intellectual disability, hypotonia, feeding difficulties, and seizures, implying lifelong dependence for daily activities (no formal EQ-5D/SF-36 data exist for this ultra-rare disease).

**Invariant (3/3 ≈ 100%) — physical/growth/neuro signs:**
- Macrotia / large ears — **HP:0000400**
- Microcephaly — **HP:0000252**
- Prominent nose — **HP:0000448**
- Small for gestational age (prenatal growth restriction) — **HP:0001518**
- Failure to thrive — **HP:0001508**
- Global developmental delay — **HP:0001263**
- Hypotonia — **HP:0001252**
- Long hallux — **HP:0001847**
- Infantile onset — **HP:0003593**

**Frequent (2/3 ≈ 67%; intellectual disability 2/2):**
- Intellectual disability — **HP:0001249**
- Seizure — **HP:0001250**
- Deeply set eyes — **HP:0000490**
- High palate — **HP:0000218**
- Preauricular skin tag — **HP:0000384**
- Hyperplasia of the maxilla — **HP:0430028**
- Hallux valgus — **HP:0001822**

**Variable (1/3 ≈ 33%; osteopenia 1/2):**
- Secundum atrial septal defect — **HP:0001684** (cardiac)
- Chorioretinal coloboma — **HP:0000567** (ophthalmologic)
- Micrognathia — **HP:0000347**
- Brain atrophy — **HP:0012444**
- Epileptic encephalopathy — **HP:0200134**
- Feeding difficulties — **HP:0011968**
- Recurrent lower respiratory tract infections — **HP:0002783**
- Diabetes mellitus — **HP:0000819** (laboratory/metabolic abnormality)
- Lower-limb spasticity — **HP:0002061**
- Pectus carinatum — **HP:0000768**
- Broad thumb — **HP:0011304**
- Clinodactyly — **HP:0030084**
- Osteopenia — **HP:0000938** (laboratory/imaging abnormality)

**Phenotype-type classification.** Physical/dysmorphic manifestations (ears, nose, eyes, palate, jaw, digits, chest), clinical neurological signs (microcephaly, hypotonia, spasticity, seizures/encephalopathy, brain atrophy), developmental/behavioral (developmental delay, intellectual disability), and laboratory abnormalities (diabetes mellitus, osteopenia). Brain malformation and DDR defect are additional features noted in the abstract (PMID 34313816).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***ZNF668*** — zinc finger protein 668. HGNC:25821; NCBI Gene 79759; OMIM gene 617103; Ensembl ENSG00000167394; canonical transcript ENST00000300849; UniProt Q96K58. Location **16p11.2** (GRCh38 chr16:31,059,772–31,074,240, minus strand). Protein: C2H2-type Krüppel-like zinc-finger (KRAB-less) transcription factor; predicted sequence-specific DNA-binding / RNA Pol II regulator; **nucleolar** localization (PMID 21852383). **[computational/in vitro]**

**Pathogenic variants.** Clinical RefSeq transcript **NM_024706.5** (protein NP_078982).
- **Type/class:** biallelic **truncating** variants (nonsense and/or frameshift) → premature termination / NMD → **loss of function** (PMID 34313816). No recurrent pathogenic missense established for the disorder.
- **Representative ClinVar pathogenic/likely-pathogenic truncating alleles** (NM_024706.5): **c.1111C>T (p.Arg371Ter)** — Pathogenic (nonsense); **c.955C>T (p.Gln319Ter)** — Pathogenic (nonsense); **c.1197del (p.Lys399fs)** — Likely pathogenic (frameshift); c.1517dup (p.Gly506_Glu507insTer) — currently VUS. The **majority of ~50 ZNF668 ClinVar records are missense/synonymous variants classified VUS or (likely) benign**, reinforcing that pathogenicity requires truncation/null rather than missense. **[computational/ClinVar]**
- **Classification (ACMG/AMP):** disease-causing variants are **pathogenic/likely pathogenic** truncating alleles segregating with disease in consanguineous families; a null variant in this LoF-intolerant gene meets the strong pathogenic criterion (PVS1).
- **IMPORTANT distinction — 16p11.2 CNVs:** *ZNF668* lies within the recurrent **16p11.2** region. Numerous ClinVar "Pathogenic" entries at 16p11.2 are **large contiguous-gene deletions/duplications** (e.g., GRCh37 chr16:30,851,860–31,156,762 x1) that encompass *ZNF668* among many genes; these represent the **dominant 16p11.2 microdeletion/microduplication syndrome**, a *distinct* disorder that must **not** be conflated with the autosomal-recessive single-gene ZNF668-ZMAND entity when interpreting chromosomal microarray.
- **Zygosity / origin:** **germline, homozygous** (both families consanguineous). No somatic/mosaic disease origin reported for the Mendelian disorder.
- **Functional consequence:** **loss of function** (haploinsufficiency is tolerated — carriers unaffected — so biallelic complete LoF is required).

**Population allele frequency / constraint (gnomAD v2.1.1, computational).** *ZNF668* is strongly **loss-of-function intolerant at the heterozygous level**: **pLI = 0.999**, **LOEUF = 0.42**, observed/expected LoF = 10/40.3 (**oe = 0.25**), **lof_z = 4.05**; missense **mis_z = 2.21**. Disease-causing truncating alleles are ultra-rare/absent in population databases. (Note the apparent paradox: strong heterozygous LoF constraint yet recessive inheritance — consistent with dosage sensitivity but sufficiency of one allele to prevent the syndrome.)

**Somatic relevance (cancer).** *ZNF668* is a **somatically mutated breast-cancer tumor-suppressor gene** (genome-wide sequencing identified frequent mutations; PMID 21852383) and shows **reduced expression associated with bladder-cancer invasiveness** (PMID 37240013) **[in vitro / tumor genomics]** — relevant to protein function, distinct from the germline recessive syndrome.

**Modifier genes / epigenetics / chromosomal abnormalities.** No disease modifiers, constitutional methylation signature, or recurrent chromosomal abnormality (CNV/translocation) defined for NEDGDF. (ZNF668 itself regulates chromatin acetylation — see Mechanism.) Not applicable / not available.

---

## 5. Environmental Information

- **Environmental factors:** None causal. The disorder is monogenic. DNA-damaging agents (ionizing radiation, UV) are mechanistically relevant **stressors** that expose the repair defect in cells (PMID 23777805) but are not disease causes. **[in vitro]**
- **Lifestyle factors:** Not applicable (congenital genetic disease).
- **Infectious agents:** None. (Recurrent lower respiratory tract infections, HP:0002783, occur as a *secondary complication* of the neurodevelopmental phenotype, not as a cause.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic truncating variant in *ZNF668*** leads to loss of full-length nucleolar ZNF668 protein (NMD/truncation). **[human clinical, PMID 34313816]**
2. Loss of ZNF668 **results in** two converging molecular deficits:
   - **Branch A (chromatin/repair):** loss of ZNF668–**Tip60 (KAT5)** cooperation **leads to** reduced ionizing-radiation-induced **histone H2AX acetylation** and **impaired chromatin relaxation** at double-strand breaks. **[in vitro, PMID 23777805]**
   - **Branch B (p53 axis):** loss of ZNF668 regulation of **MDM2** **leads to** failure to stabilize **p53** after DNA damage (ZNF668 normally restrains MDM2-mediated p53 ubiquitination/degradation). **[in vitro, PMID 21852383]**
3. Branch A **results in** decreased recruitment of homologous-recombination (HR) repair factors (and reduced RPA phosphorylation/recruitment after UV) → **defective HR / nucleotide-excision-type repair** and reduced cell survival after DNA damage. **[in vitro, PMID 23777805]**
4. Branches A+B together **result in** **genome instability / accumulated unrepaired DNA damage** and a dysregulated DNA-damage checkpoint/apoptosis balance (demonstrated as a **DNA-damage-repair defect in patient fibroblasts**). **[human clinical, PMID 34313816]**
5. Genome instability in **highly proliferative progenitors** (neural progenitors, somatic growth tissues) **leads to** impaired proliferation/increased cell death during development (**inferred**, by analogy to other microcephalic DDR/primordial-growth disorders, PMID 19473885).
6. This **results in** the clinical phenotype: **microcephaly + brain malformation/atrophy** (neural progenitor depletion), **prenatal-onset growth restriction / SGA / failure to thrive** (reduced somatic proliferation), **severe developmental delay/intellectual disability, hypotonia, seizures**, and the **dysmorphic facial/skeletal gestalt** (large ears, prominent nose, deep-set eyes, palate/jaw and digit anomalies). **[human clinical, PMID 34313816]**

**Upstream vs downstream.** Upstream = *ZNF668* LoF → chromatin-acetylation/HR-repair defect + p53 destabilization (molecular). Downstream = genome instability → progenitor attrition → microcephaly/growth failure/neurodevelopmental impairment (organ/clinical).

**Checklist detail.**
- **Molecular pathways:** DNA-damage response; homologous-recombination DSB repair; p53–MDM2 tumor-suppressor axis; chromatin (histone H2AX/H2A) acetylation by Tip60/KAT5. (Reactome: DNA Double-Strand Break Repair; HDR through HR; Regulation of TP53 Activity.)
- **Cellular processes:** DNA repair, cell-cycle checkpoint control, apoptosis/survival after genotoxic stress, chromatin remodeling, (neuro)progenitor proliferation.
- **Protein dysfunction:** complete **loss of function** of a nucleolar C2H2 zinc-finger transcriptional/chromatin regulator (truncation removes zinc-finger/functional domains).
- **Metabolic / immune:** no primary metabolic pathway defect (diabetes mellitus is a variable late feature; mechanism unclear). No primary immunodeficiency (recurrent LRTIs are secondary to neurologic status).
- **Molecular profiling (disease-specific):** no patient transcriptomic/proteomic/metabolomic/epigenomic datasets published. Functional assay = DDR defect in patient fibroblasts (PMID 34313816); RNAi/knockdown functional genomics in U2OS and mammary epithelial cells (PMIDs 23777805, 21852383).

**Suggested GO / CL terms.** GO:0006281 DNA repair; GO:0000724 double-strand break repair via HR; GO:0006325 chromatin organization; GO:0043968 histone H2A acetylation (and GO:0016573 histone acetylation); GO:0000077 DNA damage checkpoint signaling; GO:0006974 DNA-damage response; GO:0030578/GO:2000774 positive regulation of p53. Cell types (CL): CL:0000031 neuroblast (neural progenitor), CL:0000047 neuronal stem cell, CL:0002319 neural cell, CL:0000057 fibroblast.

---

## 7. Anatomical Structures Affected

**Organ / body-system level.**
- **Central nervous system (primary):** brain — microcephaly, brain malformation, brain atrophy; nervous system disorder with hypotonia, spasticity, seizures/epileptic encephalopathy. UBERON:0000955 brain; UBERON:0001890 forebrain; UBERON:0001017 central nervous system.
- **Growth / musculoskeletal (primary):** generalized growth failure; skeletal features — maxilla (UBERON:0002397), palate (UBERON:0001716), mandible/jaw (micrognathia; UBERON:0001684), thorax (pectus carinatum; UBERON:0002228 rib cage), hands/feet (broad thumb, clinodactyly, long hallux, hallux valgus; UBERON:0002389 manual digit / UBERON:0001466 pedal digit); osteopenia (reduced bone mineral density).
- **Craniofacial / ear / eye (dysmorphism):** external ear/pinna (macrotia, preauricular tag; UBERON:0001690 ear, UBERON:0001757 pinna), nose (UBERON:0000004), orbit/eye (deeply set eyes; chorioretinal coloboma — UBERON:0000479 retina/choroid).
- **Cardiovascular (secondary/variable):** heart — secundum atrial septal defect (UBERON:0000948 heart; interatrial septum).
- **Respiratory (secondary):** lower respiratory tract — recurrent infections (UBERON:0001558 lower respiratory tract).
- **Digestive (secondary):** feeding difficulties/failure to thrive (UBERON:0001007 digestive system).
- **Endocrine/metabolic (variable):** diabetes mellitus (pancreas/glucose homeostasis; UBERON:0001264 pancreas).

**Tissue / cell level.** Nervous tissue (neurons, neural progenitors) and rapidly dividing somatic/connective tissues are most affected by the proliferative/genome-instability defect; fibroblasts show the measurable repair defect **[human clinical]**. CL terms: CL:0000031 neuroblast, CL:0000047 neuronal stem cell, CL:0000057 fibroblast, CL:0000679 glutamatergic neuron (general neuronal involvement).

**Subcellular level.** **Nucleus** (GO:0005634) and specifically the **nucleolus** (GO:0005730) — ZNF668 is a nucleolar protein (PMID 21852383); sites of DNA double-strand breaks / chromatin (GO:0000785 chromatin; GO:0035861 site of DNA damage).

**Localization / lateralization.** Craniofacial and CNS involvement is **bilateral/symmetric**; chorioretinal coloboma and limb anomalies may be variable/asymmetric; ASD is a midline cardiac lesion.

---

## 8. Temporal Development

- **Onset:** **congenital / prenatal** (small for gestational age) with recognition in **infancy** (HP:0003593 Infantile onset, 3/3). Pattern is **insidious/chronic**, present from birth.
- **Progression:** **chronic, lifelong, non-remitting**. Growth failure and developmental delay are evident early; brain atrophy suggests a potentially **progressive/static-with-deterioration** CNS component in at least some individuals. Seizures/epileptic encephalopathy can evolve. No staging system exists.
- **Disease course:** stable-to-slowly-progressive developmental impairment; episodic events = seizures and intercurrent respiratory infections.
- **Remission:** none (no spontaneous or treatment-induced remission; disorder is constitutional).
- **Critical periods:** fetal and early-postnatal neurodevelopment (period of maximal neural-progenitor proliferation) is the key window of vulnerability; interventions are supportive (early developmental/rehabilitation therapy).

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** Prevalence/incidence **not established** — only **3 affected individuals from 2 consanguineous families** reported (PMID 34313816). Likely far fewer than 1 per 1,000,000; no registry data.

**Genetic etiology.**
- **Inheritance:** **Autosomal recessive** (HP:0000007) — *"ZNF668 deficiency in humans results in a recognizable autosomal recessive disorder"* (PMID 34313816).
- **Penetrance:** presumed **complete** for biallelic truncating genotype (all biallelic individuals affected), though n is tiny.
- **Expressivity:** **variable** for secondary features (cardiac, ocular, metabolic, skeletal) across the small cohort; core features (growth failure, microcephaly, DD) are consistent.
- **Anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effect:** none established; variants are family-specific/private.
- **Consanguinity:** **major role** — both families consanguineous; disorder manifests through homozygosity-by-descent. Expected to be enriched in populations with high consanguinity rates.
- **Carrier frequency:** truncating alleles are ultra-rare in gnomAD (gene strongly LoF-constrained), so carrier frequency is very low except possibly within specific consanguineous kindreds.

**Population demographics.** Reported families include Middle Eastern (Saudi; Alkuraya group) and European (French, Angers group) ancestry based on the author cohort (PMID 34313816). Predicted to be found more often in **consanguineous/endogamous populations**. **Sex ratio:** no sex bias expected (autosomal); not quantifiable (n=3). **Age distribution:** affected from birth; survivors are children (natural history into adulthood unknown).

---

## 10. Diagnostics

**Primary diagnostic modality — genetic testing.**
- **Recommended approach:** **trio whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** in a child with prenatal-onset growth restriction + microcephaly + developmental delay + dysmorphism, interpreted with **homozygosity mapping / runs-of-homozygosity** in consanguineous pedigrees (the gene-discovery route used in PMID 34313816). WGS adds value for non-coding/structural alleles. **[human clinical]**
- **Gene panels:** inclusion in broad **intellectual-disability / microcephaly / primordial-dwarfism / multiple-congenital-anomaly** NGS panels (single-gene *ZNF668* testing otherwise rarely offered).
- **Single-gene / segregation:** Sanger confirmation and parental carrier testing to confirm biallelic inheritance.
- **CMA / karyotype / FISH:** chromosomal microarray and karyotype are typically **normal** in ZNF668-ZMAND (point/truncating variants); useful mainly to exclude CNVs/aneuploidy. **Caveat:** a 16p11.2 CNV involving *ZNF668* on CMA indicates the separate **16p11.2 microdeletion/microduplication syndrome**, not the recessive single-gene disorder. Mitochondrial DNA and repeat-expansion testing: not indicated.

**Supportive clinical tests.**
- **Neuroimaging (brain MRI):** to document microcephaly, brain malformation, brain atrophy (HP:0012444). Key for phenotyping.
- **Functional DDR assay (research/supportive):** patient-fibroblast DNA-damage-repair assays demonstrate the repair defect (PMID 34313816) — a functional biomarker of pathogenicity, not a routine clinical test. **[human clinical / in vitro]**
- **EEG:** for seizures/epileptic encephalopathy.
- **Echocardiography:** for atrial septal defect.
- **Ophthalmologic exam:** for chorioretinal coloboma/deep-set eyes.
- **Growth monitoring, bone densitometry** (osteopenia), **glucose/HbA1c** (diabetes surveillance), **feeding/respiratory assessment**.
- **Biomarkers:** no specific circulating biochemical biomarker; diagnosis is molecular. LOINC-coded genetic report; no disease-specific metabolite.

**Clinical criteria / differential diagnosis.** No formal diagnostic criteria (ultra-rare). Diagnosis = compatible phenotype + biallelic LoF *ZNF668*. **Differential diagnosis:** other autosomal-recessive **microcephalic primordial dwarfism / microcephaly-DDR syndromes** and genome-instability disorders — e.g., **Seckel syndrome, microcephalic osteodysplastic primordial dwarfism type II (MOPD II)**, MCPH spectrum, Cornelia de Lange syndrome, and other DDR disorders (PMID 19473885 reviews this class). Distinguishing feature: biallelic *ZNF668* truncation with an in-vitro DDR defect and the specific facial gestalt (large ears + prominent nose + deep-set eyes).

**Screening.** Not part of newborn screening. **Cascade carrier testing** of relatives and **prenatal/preimplantation testing** available once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** not quantified. No survival statistics (n=3; natural history into adulthood unknown). Potential early-life morbidity/mortality risk from severe neurodevelopmental impairment, seizures, feeding difficulty, and recurrent respiratory infections (inferred by analogy to severe microcephaly/DDR syndromes).
- **Morbidity / disability:** **severe, lifelong**. Severe global developmental delay and intellectual disability (ICF: profound limitations in learning, communication, mobility, self-care), hypotonia ± spasticity, epilepsy. High dependency for daily activities.
- **Quality of life:** profoundly impacted; no formal EQ-5D/SF-36/PROMIS data.
- **Complications:** epileptic encephalopathy, aspiration/feeding difficulties, recurrent lower respiratory infections, cardiac (ASD), osteopenia/fracture risk, diabetes mellitus (variable), visual impairment (coloboma).
- **Recovery potential:** none for the core neurodevelopmental deficit (constitutional); supportive care improves function/comfort.
- **Prognostic factors / biomarkers:** severity of microcephaly/brain malformation and epileptic encephalopathy likely predict worse neurodevelopmental outcome (inferred). No validated prognostic molecular biomarker. **Theoretical long-term consideration:** because *ZNF668* is a tumor suppressor somatically, whether constitutional biallelic loss alters lifetime cancer risk is **unknown and unstudied** — flagged as a research gap.

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is **symptomatic and supportive/multidisciplinary** (NCIT:C15277 Supportive Care; NCIT:C15688 Symptomatic Treatment).

- **Pharmacotherapy:** none targeting ZNF668. **Antiseizure medications** for epilepsy (NCIT:C264 Anticonvulsant Agent). Standard management of diabetes mellitus if present (NCIT:C159044 Antidiabetic Agent). No pharmacogenomic guidance specific to this disorder.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **none**; no gene therapy, ASO, or targeted therapy in development. Not applicable.
- **Surgical / interventional:** as indicated for complications — e.g., **gastrostomy** for feeding failure (NCIT:C157826), **ASD repair** if hemodynamically significant (NCIT:C51818 Cardiac Surgery), strabismus/ophthalmic or orthopedic interventions as needed.
- **Supportive & rehabilitative:** nutritional support for failure to thrive; **physical, occupational, and speech/language therapy** (NCIT:C15607 Physical Therapy; NCIT:C15630 Occupational Therapy; NCIT:C15312 Speech Therapy); respiratory care/infection prophylaxis; bone-health management for osteopenia; developmental/special-education support.
- **Experimental treatments / trials:** **none registered** (no ClinicalTrials.gov NCT entries for ZNF668-related disorder).
- **Treatment outcomes / adverse events:** no disease-specific response data.
- **Treatment strategy:** individualized, guideline-based management of each manifestation; genotype-guided care limited to confirming diagnosis and enabling family counseling.

---

## 13. Prevention

- **Primary prevention:** not possible for the constitutional disease. At the family/population level, **genetic counseling about consanguinity** and recurrence risk is the principal preventive measure.
- **Secondary prevention (early detection):** early genetic diagnosis enables early developmental intervention and surveillance (seizures, cardiac, ophthalmologic, metabolic/diabetes, bone health).
- **Tertiary prevention:** proactive management to prevent complications — seizure control, aspiration/respiratory-infection prevention, nutritional optimization, bone-health measures.
- **Immunization:** routine childhood immunizations recommended (reduce respiratory-infection morbidity); no disease-specific vaccine.
- **Genetic screening / reproductive options:** **carrier (cascade) testing** of relatives; **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** for at-risk couples once familial biallelic variants are identified (ACMG/ACOG frameworks).
- **Counseling:** autosomal-recessive **25% recurrence risk** for carrier couples; emphasize consanguinity risk.
- **Public-health / environmental / prophylaxis:** not applicable beyond general measures.

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** No naturally occurring animal disease described (OMIA: none). Human disease only (**NCBITaxon:9606**).
- **Orthologous genes (NCBI Gene / ortholog symbols):** mouse **Zfp668** (Mus musculus, NCBITaxon:10090); conserved across mammals and vertebrates (the C2H2 zinc-finger architecture is evolutionarily conserved). Rat *Zfp668* (NCBITaxon:10116) predicted.
- **Veterinary relevance:** none known.
- **Comparative biology:** the **DNA-damage-response/HR-repair and p53–MDM2 pathways** in which ZNF668 acts are deeply conserved; disease-mechanism conservation is expected, but the specific syndrome has not been reported in other species. **Evolutionary conservation** of the DDR machinery underpins the expectation that loss would be deleterious across species.
- **Zoonotic / cross-species transmission:** not applicable (genetic disease).

---

## 15. Model Organisms

- **Available models:** **No published vertebrate disease model** (no reported *Zfp668* knockout mouse phenotype). **IMPC** has **no significant phenotype annotations** for mouse *Zfp668* at time of writing (not yet phenotyped or no reported significant hit) — i.e., no mouse model demonstrating phenotype recapitulation. **[computational/database]**
- **In-vitro / cellular models (the actual evidence base):**
  - **Patient-derived skin fibroblasts** — demonstrate the DNA-damage-repair defect (PMID 34313816). **[human clinical cells]**
  - **U2OS osteosarcoma cells with ZNF668 knockdown** — reduced Tip60–H2AX interaction, impaired H2AX acetylation/chromatin relaxation, defective HR, reduced survival after IR/UV (PMID 23777805). **[in vitro]**
  - **Human mammary epithelial cells** — ZNF668 knockdown sufficient to transform cells; ZNF668 suppresses proliferation/tumorigenicity; impaired DNA-damage-induced p53 stabilization (PMID 21852383). **[in vitro]**
- **Model types needed/applicable:** mouse knockout/conditional (brain-/growth-specific), zebrafish *znf668* morphant/CRISPR, and **patient iPSC-derived neural organoids** would be informative for recapitulating microcephaly/neurodevelopment — **none yet reported** (research gap).
- **Phenotype recapitulation / limitations:** current cellular models recapitulate the **molecular DDR defect** (repair, p53, chromatin) but **not** the organismal phenotype (microcephaly, growth failure, dysmorphism). No model captures the full clinical syndrome.
- **Resources:** MGI (mouse *Zfp668*), IMPC, Alliance of Genome Resources, Cellosaurus (U2OS); IMSR/KOMP for potential alleles.

---

## Supported vs. Refuted Hypotheses

**Supported.**
- NEDGDF (MONDO:0859350/OMIM 620194) is caused by **biallelic truncating LoF variants in *ZNF668***, autosomal recessive (PMID 34313816). ✔
- Mechanism is a **DNA-damage-repair defect** via impaired Tip60/H2AX-acetylation-dependent HR repair and p53–MDM2 dysregulation (PMIDs 23777805, 21852383, 34313816). ✔
- *ZNF668* is strongly **LoF-constrained** (gnomAD pLI 0.999), consistent with an essential dosage-sensitive gene. ✔
- Core invariant phenotype = prenatal-onset growth restriction + microcephaly + severe DD + facial dysmorphism (HPO frequencies, PMID 34313816). ✔

**Refuted / not supported.**
- Not an environmental, infectious, or acquired disorder. ✘
- Not a dominant/de-novo disorder (recessive; heterozygous carriers unaffected). ✘
- No evidence for a repeat-expansion/anticipation mechanism. ✘

---

## Limitations and Future Directions

**Limitations.** Evidence rests on a **single defining publication with only 3 patients**; all phenotype frequencies have denominators of 2–3 and are provisional. No natural-history, survival, QoL, or treatment-outcome data. No animal model and no patient omics datasets. Exact variant-level nomenclature (cDNA/protein HGVS) was not retrievable from abstract-level sources in this analysis and should be confirmed from the primary paper/ClinVar. Orphanet/ICD-specific codes not yet assigned. Potential constitutional cancer-risk implications of biallelic tumor-suppressor loss are unknown.

**Future directions.** (1) Identify additional families via GeneMatcher to refine the phenotype spectrum and penetrance; (2) deposit/curate variants in ClinVar; (3) generate *Zfp668* mouse/zebrafish and patient iPSC neural-organoid models to test microcephaly recapitulation; (4) characterize patient-cell transcriptomic/epigenomic signatures and p53-pathway status; (5) assess lifetime tumor risk given ZNF668's tumor-suppressor role; (6) establish surveillance guidelines (seizure, cardiac, ophthalmologic, metabolic, bone).

---

### Key References (PMIDs)
- **34313816** — Alsaif et al., 2021. *ZNF668 deficiency causes a recognizable disorder of DNA damage repair.* (Disease-defining; 3 patients; AR; DDR defect in fibroblasts; proposes ZNF668-related ZMAND.) **[human clinical]**
- **21852383** — Hu et al., 2011. *ZNF668 functions as a tumor suppressor by regulating p53 stability and function in breast cancer.* (Nucleolar protein; p53/MDM2 regulation.) **[in vitro]**
- **23777805** — Hu et al., 2013. *Zinc finger protein 668 interacts with Tip60 to promote H2AX acetylation after DNA damage.* (Chromatin relaxation; HR repair.) **[in vitro]**
- **37240013** — Okuno et al., 2023. *Reduced expression of ZNF668 in bladder cancer and its invasiveness.* **[in vitro/tumor]**
- **19473885** — Kerzendorfer & O'Driscoll, 2009. *Human DNA damage response and repair deficiency syndromes.* (Context: microcephalic DDR-disorder class.) **[review]**


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Poor_Growth_Large_Ears_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Poor_Growth_Large_Ears_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 80 |
| Resolved | 75 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:10116` (1 mention) - the report calls it "Zfp668"; NCBITaxon calls it **Rattus norvegicus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043968` (obsolete histone H2A acetylation) (1 mention)
- `GO:0016573` (obsolete histone acetylation) (1 mention)
- `NCIT:C159044` (GDC Gene Symbol Terminology) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (1 mention) - the report calls it "Autosomal recessive", "Inheritance:** **Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Autosomal recessive", "Inheritance:** **Autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.