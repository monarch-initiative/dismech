---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T18:59:01.623465'
end_time: '2026-09-09T19:26:02.620286'
duration_seconds: 1621.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Sponastrime Type
  mondo_id: MONDO:0010068
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
citation_count: 12
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 3
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0000944
    reported_labels:
    - Platyspondyly / vertebral abnormalities
    ontology_label: Abnormal metaphysis morphology
  - term_id: HP:0002650
    reported_labels:
    - Narrow lumbar interpedicular distances
    - Scoliosis
    ontology_label: Scoliosis
  - term_id: HP:0005789
    reported_labels:
    - Metaphyseal striations
    ontology_label: Generalized osteosclerosis
  - term_id: HP:0001541
    reported_labels:
    - Delayed carpal ossification
    ontology_label: Ascites
  - term_id: HP:0004315
    reported_labels:
    - Hypogammaglobulinemia
    ontology_label: Decreased circulating IgG concentration
  labels_variant: 9
  obsolete_terms:
  - term_id: HP:0001388
    ontology_label: obsolete Joint laxity
    replaced_by: HP:0001382
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spondyloepimetaphyseal_Dysplasia_Sponastrime_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spondyloepimetaphyseal_Dysplasia_Sponastrime_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Sponastrime Type
- **MONDO ID:** MONDO:0010068 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Sponastrime Type** covering all of the
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

# Spondyloepimetaphyseal Dysplasia, Sponastrime Type — Comprehensive Disease Report

**MONDO:** MONDO:0010068 · **OMIM:** #271510 · **Orphanet:** ORPHA:93357 · **Category:** Mendelian (autosomal recessive skeletal dysplasia)

> Evidence base: This report is derived from **aggregated disease-level literature and case series/reports** (there is no population EHR dataset for this ultra-rare disorder). Primary sources are cited by PMID. Evidence source types are flagged: *human clinical*, *in vitro*, *model organism*, *computational*.

---

## Summary

**Spondyloepimetaphyseal dysplasia, Sponastrime type ("SPONASTRIME dysplasia") is an ultra-rare autosomal-recessive skeletal dysplasia caused by biallelic hypomorphic (loss-of-function) variants in *TONSL* (8q24.3), which encodes the Tonsoku-like DNA-repair protein.** The disease name is an acronym derived from its cardinal radiographic features: **SPO**ndylar abnormalities, **NA**sal changes (midface hypoplasia/depressed nasal bridge), and **STRI**ations of the **ME**taphyses. First delineated by Fanconi et al. in 1983, it remained a purely descriptive radiological entity for 36 years until two independent 2019 studies ([PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/); [PMID: 30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/)) identified *TONSL* as the causal gene.

Mechanistically, SPONASTRIME dysplasia is a **genome-instability disorder**. TONSL is the H4K20me0-reading subunit of the TONSL–MMS22L complex, which is recruited to newly replicated ("post-replicative") chromatin to promote homologous-recombination (HR) repair of stalled and collapsed replication forks. Hypomorphic *TONSL* variants impair this function, producing replication stress, spontaneous chromosome breakage, defective cell proliferation, and increased apoptosis in dividing cells. The prevailing (partly inferred) model holds that loss of proliferating growth-plate chondrocytes underlies the endochondral-ossification defects that manifest as disproportionate short stature, age-dependent vertebral abnormalities, and metaphyseal striations, with branch effects in hematopoietic and other rapidly dividing tissues (neutropenia, hypogammaglobulinemia).

Clinically, patients present with **severe disproportionate short-limb short stature** (adult heights ~91–135 cm), platyspondyly with characteristic age-dependent "pear-shaped" vertebral bodies, metaphyseal striations (distal femur/proximal tibia), midface hypoplasia, frontal bossing, joint laxity, and variable childhood cataracts, short dental roots, and immunologic/hematologic abnormalities. Intelligence is normal in most classic cases, though a historically delineated variant subgroup features severe intellectual disability. Diagnosis rests on radiological criteria confirmed by molecular testing (WES/WGS or targeted *TONSL*/skeletal-dysplasia panels). Only supportive management exists; growth hormone therapy has shown little benefit. Fewer than ~30–40 cases have been reported worldwide.

---

## 1. Disease Information

- **Overview:** An ultra-rare, congenital, autosomal-recessive spondyloepimetaphyseal dysplasia (SEMD) characterized by disproportionate short stature, distinctive age-dependent vertebral abnormalities, metaphyseal striations, and midface hypoplasia. It is caused by biallelic hypomorphic *TONSL* variants and is mechanistically a DNA-repair/genome-instability disorder.
- **Key identifiers:** MONDO:0010068; OMIM #271510; Orphanet ORPHA:93357; MeSH — indexed under skeletal dysplasias/osteochondrodysplasias; ICD-10 Q77.8 (other osteochondrodysplasia with defects of growth of tubular bones and spine) / ICD-11 LD24 range for osteochondrodysplasias (no unique code).
- **Synonyms / alternative names:** SPONASTRIME dysplasia; Sponastrime dysplasia; SPONASTRIME (**SPO**ndylar and **NA**sal changes with **STRI**ations of the **ME**taphyses).
- **Data source:** Aggregated disease-level resources (OMIM, Orphanet) and primary case series/reports — not individual EHR data. This reflects the disorder's extreme rarity.

---

## 2. Etiology

- **Primary cause (genetic):** Biallelic (homozygous or compound-heterozygous) **hypomorphic loss-of-function variants in *TONSL*** (8q24.3). This is a monogenic Mendelian disorder ([PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/); [PMID: 30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/)). See Finding F001.
- **Genetic risk factors:** The causal variants themselves are the risk factor; no separate susceptibility loci or GWAS signals apply (Mendelian disease). Recurrent variants include **R934W** and **G973R**. Complete loss of function is embryonic-lethal, so viable disease requires residual (hypomorphic) function.
- **Environmental risk factors:** None known. No toxin, radiation, infectious, occupational, dietary, age, or sex association exists — the disorder is fully explained by germline genetics.
- **Protective factors:** None identified (genetic or environmental).
- **Gene–environment interactions:** None established. Phenotypic variability (F004) is more likely attributable to allelic heterogeneity and putative genetic modifiers than to environmental interactions.

---

## 3. Phenotypes

Cardinal and associated features with suggested HPO terms (Burrage 2019 [PMID: 30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/); Cooper 2000 [PMID: 10797420](https://pubmed.ncbi.nlm.nih.gov/10797420/); Langer 1997 [PMID: 9133352](https://pubmed.ncbi.nlm.nih.gov/9133352/); Arponen 2025 [PMID: 40122363](https://pubmed.ncbi.nlm.nih.gov/40122363/); see Finding F003).

| Phenotype | HPO term | Type | Onset | Severity/Frequency |
|---|---|---|---|---|
| Disproportionate short-limb short stature | HP:0004322 | Physical/growth | Congenital | Severe (~ −6 SD); near-universal; adult height 91–135 cm |
| Platyspondyly / vertebral abnormalities | HP:0000944 | Clinical sign (radiographic) | Childhood, **age-dependent** | Characteristic "pear-shaped" bodies; near-universal |
| Narrow lumbar interpedicular distances | HP:0002650 | Radiographic sign | Childhood | Diagnostic |
| Metaphyseal striations | HP:0005789 | Radiographic sign | Childhood | Distal femur/proximal tibia; cardinal (may be absent early in spectrum cases) |
| Midface hypoplasia | HP:0011800 | Physical | Congenital/childhood | Common |
| Depressed nasal bridge / short upturned nose | HP:0005280 | Physical | Congenital | Common |
| Frontal bossing | HP:0002007 | Physical | Childhood | Common |
| Lumbar lordosis | HP:0002938 | Clinical sign | Childhood | Common |
| Scoliosis | HP:0002650 | Clinical sign | Childhood | Frequent |
| Coxa vara | HP:0002812 | Radiographic sign | Childhood | Frequent |
| Delayed carpal ossification | HP:0001541 | Radiographic sign | Childhood | Frequent |
| Joint laxity / hypermobility | HP:0001388 | Physical | Childhood | Frequent |
| Childhood cataracts | HP:0000519 | Ophthalmologic | Childhood | Subset |
| Short dental roots / dentin dysplasia I-like | HP:0000601 / HP:0009900 | Dental | Childhood | Subset (Arponen 2025) |
| Hypogammaglobulinemia | HP:0004315 | Laboratory | Variable | Subset |
| Neutropenia | HP:0001875 | Laboratory | Variable | Subset (Yao 2025) |
| Severe intellectual disability / microcephaly | HP:0010864 / HP:0000252 | Neurodevelopmental | Congenital | **Variant form only** |
| Arnold–Chiari I malformation | HP:0007099 | Neurologic | Childhood | Rare (Jeong 2016) |

- **Progression:** Skeletal features are chronic and progressive relative to peers; vertebral radiographic changes evolve with age. Short stature is fixed.
- **Quality of life:** Not formally measured (no EQ-5D/SF-36/PROMIS data). Impact derives chiefly from short stature, orthopedic complications (scoliosis, coxa vara), and, where present, visual impairment (cataracts) or immune susceptibility. Intelligence and life expectancy are typically normal in classic disease.

Direct quote (Burrage 2019): *"characterized by spine (spondylar) abnormalities, midface hypoplasia with a depressed nasal bridge, metaphyseal striations, and disproportionate short stature. Scoliosis, coxa vara, childhood cataracts, short dental roots, and hypogammaglobulinemia have also been reported."*

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***TONSL*** (Tonsoku-like DNA repair protein), chromosome **8q24.3**; NCBI Gene ID **4796**; HGNC:11989; UniProt **Q96HA7**; OMIM gene *604546*. Disease OMIM #271510.
- **Pathogenic variants:** Biallelic; a mix of **missense, frameshift, and nonsense** hypomorphic (partial loss-of-function) alleles spanning multiple domains. Recurrent variants **R934W** and **G973R**. Novel variants continue to be reported (Yao 2025 [PMID: 40794898](https://pubmed.ncbi.nlm.nih.gov/40794898/); Zhu 2024 [PMID: 38684304](https://pubmed.ncbi.nlm.nih.gov/38684304/); Micale 2020 [PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)).
- **Variant classification:** Pathogenic/likely pathogenic per ACMG; functional assays (fibroblast complementation, HEK293T expression, dimerization studies) provide PS3-level functional evidence.
- **Allele frequency:** Very low/absent in gnomAD (consistent with a rare recessive disorder); no common founder allele established.
- **Origin:** **Germline**; no somatic/mosaic mechanism. Inherited from unaffected heterozygous carrier parents.
- **Functional consequence:** Loss of function / hypomorphic. Complete null is embryonic-lethal (mouse), so only residual-function alleles produce viable disease. R934W and G973R abolish UBL-domain dimerization ([PMID: 42525765](https://pubmed.ncbi.nlm.nih.gov/42525765/)).
- **Modifier genes:** None specifically identified, though phenotypic variability implies their existence.
- **Epigenetic information:** No disease-specific DNA-methylation/histone-modification signature reported. (Note: TONSL's *function* is to read the H4K20me0 chromatin mark, but this is its normal biology, not a disease epigenetic lesion.)
- **Chromosomal abnormalities:** None as a cause. The *cellular consequence*, however, is spontaneous chromosome breakage from defective DNA repair ([PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)).

---

## 5. Environmental Information

Not applicable. No environmental factors (toxins, radiation, pollution, occupational exposure), lifestyle factors (smoking, diet, exercise, alcohol), or infectious agents are known to cause or trigger SPONASTRIME dysplasia. It is a purely genetic monogenic disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *TONSL* variants** reduce protein function by disrupting the ankyrin-repeat domain (ARD; H4K20me0 reading) or the ubiquitin-like (UBL) domain (dimerization) — *demonstrated* ([PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/); [PMID: 42525765](https://pubmed.ncbi.nlm.nih.gov/42525765/)). **Leads to →**
2. **Impaired recruitment of the TONSL–MMS22L complex** to post-replicative chromatin marked by H4K20me0 — *demonstrated* ([PMID: 27338793](https://pubmed.ncbi.nlm.nih.gov/27338793/)). **Results in →**
3. **Compromised homologous-recombination repair** of replication-associated double-strand breaks at stalled/collapsed forks — *demonstrated* ([PMID: 30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/); [PMID: 27338793](https://pubmed.ncbi.nlm.nih.gov/27338793/)). **Leads to →**
4. **Replication stress and spontaneous chromosome breakage** in patient cells — *demonstrated* ([PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)). **Results in →**
5. **Defective cell proliferation and increased apoptosis** of dividing cells — *demonstrated* ([PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)). **Then branches:**
   - **6a (skeletal branch — INFERRED):** Loss of proliferating **growth-plate chondrocytes** → impaired **endochondral ossification** → disproportionate short stature, metaphyseal striations, age-dependent vertebral dysplasia.
   - **6b (hematopoietic/immune branch — observed):** Depletion/dysfunction of rapidly dividing progenitors → **neutropenia and hypogammaglobulinemia**.
   - **6c (other proliferative tissues — observed):** lens epithelium (cataracts), odontoblasts (short dental roots/dentin anomalies).
7. **Complete loss of TONSL is embryonic-lethal** in mouse, defining the requirement for residual function in viable disease — *demonstrated* ([PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/)).

```
 TONSL biallelic hypomorphic variants (ARD or UBL domain)
              │  (loss of H4K20me0 reading / dimerization)
              ▼
 Failure to recruit TONSL–MMS22L to post-replicative chromatin
              │
              ▼
 Defective HR repair of replication-associated DSBs
              │
              ▼
 Replication stress → spontaneous chromosome breaks
              │
              ▼
 Impaired proliferation + increased apoptosis of dividing cells
        ┌─────────────┼──────────────────┬───────────────┐
        ▼             ▼                  ▼               ▼
 Growth-plate    Hematopoietic     Lens epithelium   Odontoblasts
 chondrocytes    progenitors       (cataracts)       (short roots)
 (INFERRED)      (neutropenia,
        │         hypogammaglob.)
        ▼
 Impaired endochondral ossification
 → short stature, metaphyseal striations, vertebral dysplasia
```

### Detail by category

- **Molecular pathways:** DNA double-strand-break repair via **homologous recombination**; replication-fork protection/restart. The TONSL–MMS22L complex is the effector. Not a classical signaling cascade (Wnt/MAPK/mTOR) disease.
- **Cellular processes:** DNA replication, DNA-damage response, cell-cycle progression, **apoptosis** (increased), **proliferation** (decreased) — all demonstrated in patient fibroblasts.
- **Protein dysfunction:** Loss/reduction of TONSL function via impaired H4K20me0 reading (ARD variants) or loss of homodimerization (UBL-domain variants R934W/G973R). Hypomorphic, not gain-of-function or dominant-negative.
- **Metabolic changes:** None specific reported.
- **Immune involvement:** Secondary — hypogammaglobulinemia and neutropenia in a subset, consistent with impaired proliferation of immune/hematopoietic progenitors.
- **Tissue damage mechanism:** Genome instability (chromosome breaks) → apoptosis and proliferation failure in dividing cell populations.
- **Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, single-cell, or CRISPR-screen dataset specific to this disease is available.

### Ontology annotations

- **GO biological process:** double-strand break repair via homologous recombination (GO:0000724); DNA replication (GO:0006260); chromatin binding (GO:0003682); replication fork processing (GO:0031297); endochondral ossification (GO:0001958, downstream); apoptotic process (GO:0006915).
- **GO cellular component:** nucleus (GO:0005634); chromatin (GO:0000785); replication fork (GO:0005657).
- **CL cell types:** chondrocyte (CL:0000138), growth-plate chondrocyte, neutrophil (CL:0000775), B cell/plasma cell (CL:0000236 / CL:0000786), lens fiber cell (CL:0011004), odontoblast (CL:0000060).

---

## 7. Anatomical Structures Affected

- **Primary organ/system — skeletal:** vertebral column (platyspondyly, pear-shaped bodies; UBERON:0001130), metaphyses of long bones (striations; UBERON:0002515), growth plate (UBERON:0006332), hips (coxa vara), carpal bones (delayed ossification), craniofacial skeleton (midface hypoplasia, frontal bossing).
- **Secondary/associated:** eye — lens (childhood cataracts; UBERON:0000965); teeth (short roots, dentin dysplasia I-like; UBERON:0001091); immune/hematopoietic system (hypogammaglobulinemia, neutropenia); nervous system (Arnold–Chiari I in a subset; intellectual disability in variant form).
- **Tissue level:** cartilage/connective tissue (growth-plate chondrocytes) primarily.
- **Subcellular level:** nucleus / chromatin / replication fork (site of TONSL function; GO:0005634, GO:0005657).
- **Lateralization:** bilateral / symmetric skeletal involvement.

---

## 8. Temporal Development

- **Onset:** congenital / early childhood; short stature and radiographic changes evident in infancy/childhood. Onset pattern is chronic/insidious rather than acute.
- **Progression:** chronic, lifelong, non-remitting. Vertebral radiographic features are **age-dependent** and evolve through childhood into adulthood (Cooper 2000 [PMID: 10797420](https://pubmed.ncbi.nlm.nih.gov/10797420/)). Short stature is fixed/progressive relative to peers.
- **Course:** stable-to-progressive; not episodic or relapsing-remitting. Disease duration is lifelong.
- **Critical periods:** the childhood window of active growth-plate function is when skeletal manifestations develop; no established intervention alters the trajectory.
- **Remission:** none (no spontaneous or treatment-induced remission).

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare. Orphanet prevalence **<1/1,000,000** (ORPHA:93357). By 2000, only ~12–16 patients from 6 families had been reported (Cooper 2000 [PMID: 10797420](https://pubmed.ncbi.nlm.nih.gov/10797420/): *"To date, 12 patients from 6 families have been reported."*); total reported cases remain ~30–40 worldwide. No formal incidence figure.
- **Inheritance:** **Autosomal recessive**; biallelic *TONSL* variants; both parents are obligate unaffected carriers (Zhu 2024 [PMID: 38684304](https://pubmed.ncbi.nlm.nih.gov/38684304/): variants *"were inherited from her phenotypically normal parents."*). Sibling recurrence risk 25%.
- **Penetrance:** Complete for the biallelic genotype (all reported biallelic individuals are affected).
- **Expressivity:** **Variable** — severity of short stature and presence of cataracts, dental, immune, and (in the variant form) neurodevelopmental features differ between patients (F004).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects:** None established.
- **Carrier frequency:** Not estimated; expected very low given rarity.
- **Population demographics:** No ethnic predilection; cases reported across European, Asian, and other populations. Sex ratio approximately equal (recessive). Age distribution: diagnosed in childhood; affected across the lifespan.

---

## 10. Diagnostics

- **Clinical/radiological (mainstay):** Diagnostic **radiological criteria** (Langer 1997 [PMID: 9133352](https://pubmed.ncbi.nlm.nih.gov/9133352/): *"The radiological features are more specific than the clinical ones. We have developed diagnostic radiological criteria based on information from our five cases and from six previously published ones."*) — age-dependent vertebral changes (pear-shaped bodies, platyspondyly, narrow lumbar interpedicular distances), metaphyseal striations (distal femur/proximal tibia), delayed carpal ossification. Imaging: skeletal survey / X-ray.
- **Genetic testing (definitive):** **WES/WGS or targeted *TONSL* sequencing / skeletal-dysplasia gene panels** identifying biallelic *TONSL* variants. WES has been the diagnostic modality in most recent reports (Chang 2019; Burrage 2019; Zhu 2024 [PMID: 38684304](https://pubmed.ncbi.nlm.nih.gov/38684304/)). Single-gene *TONSL* testing/segregation confirms carrier parents. CMA/karyotyping/FISH/mtDNA/repeat-expansion testing are not indicated for diagnosis (the causal lesion is a small variant).
- **Supportive laboratory tests:** serum immunoglobulins (hypogammaglobulinemia), CBC (neutropenia); cytogenetic analysis of cultured fibroblasts may reveal spontaneous chromosome breaks (Micale 2020 [PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)).
- **Biomarkers / omics:** No validated circulating biomarker; no metabolomic/proteomic/lipidomic diagnostic signature.
- **Differential diagnosis:** spondyloepimetaphyseal dysplasia with joint laxity (leptodactylic/Hall type; Sulko 2008 [PMID: 18841068](https://pubmed.ncbi.nlm.nih.gov/18841068/)), spondyloepiphyseal dysplasia (SED — a documented initial misdiagnosis in Cooper 2000), other dysplasias with metaphyseal striations (e.g., osteopathia striata), and other short-stature SEMDs.
- **Screening:** Not part of newborn screening. Cascade/carrier testing of relatives is possible once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No disease-specific mortality data; **life expectancy appears essentially normal** with supportive care in classic disease. (Complete TONSL loss is embryonic-lethal, but affected individuals have residual-function alleles.)
- **Morbidity/function:** Driven by short stature, orthopedic complications (scoliosis, coxa vara), visual impairment (cataracts) where present, and immune susceptibility (hypogammaglobulinemia/neutropenia) in a subset. In the variant form, intellectual disability is a major morbidity.
- **QoL measures:** Not formally quantified (no EQ-5D/SF-36/PROMIS data).
- **Complications:** scoliosis, coxa vara, cataract-related visual loss, recurrent infections (if immunodeficient), Chiari I malformation (rare), dental problems.
- **Prognostic factors:** genotype (residual function level), presence/absence of the neurodevelopmental variant phenotype, and immune/hematologic involvement. No validated prognostic biomarker.

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** Management is entirely supportive/symptomatic. Suggested NCIT clinical-intervention concepts in brackets.

- **Pharmacotherapy:** None disease-specific. Immunoglobulin replacement if clinically significant hypogammaglobulinemia [NCIT: Immunoglobulin Therapy]. Pharmacogenomics: not applicable.
- **Growth hormone:** Trialed but **largely ineffective** (Yao 2025 [PMID: 40794898](https://pubmed.ncbi.nlm.nih.gov/40794898/): *"Six-month growth hormone therapy was administered to the patient after confirmed diagnosis, with limited improvement."*) [NCIT: Recombinant Human Growth Hormone Therapy].
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None available or in trials.
- **Surgical/interventional:** Orthopedic correction of scoliosis/coxa vara [NCIT: Orthopedic Surgery]; cataract surgery [NCIT: Cataract Extraction]; neurosurgical foramen-magnum decompression for Chiari I (Jeong 2016 [PMID: 27149441](https://pubmed.ncbi.nlm.nih.gov/27149441/): *"The malformation was successfully treated by decompression of the foramen magnum and elevation of the cerebellum, with complete resolution of pain."*) [NCIT: Decompression Surgery].
- **Supportive/rehabilitative:** physical/occupational therapy, dental care, ophthalmologic monitoring, audiology as needed.
- **Experimental treatments / trials:** None registered.
- **Treatment strategy:** multidisciplinary supportive care coordinated by clinical genetics, orthopedics, ophthalmology, immunology, and dentistry.

---

## 13. Prevention

- **Primary prevention:** Not possible (genetic disorder). The only preventive avenue is **genetic counseling** — 25% sibling recurrence risk, carrier testing of at-risk relatives, and reproductive options (prenatal diagnosis or preimplantation genetic testing, PGT-M) once the familial *TONSL* variants are known [NCIT: Genetic Counseling].
- **Secondary prevention:** Early ophthalmologic screening for cataracts, immune evaluation, and orthopedic surveillance in diagnosed individuals to detect and treat complications early.
- **Tertiary prevention:** Management of complications as above.
- **Immunization / behavioral / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *TONSL* is evolutionarily conserved. Human *TONSL* (NCBI Gene 4796); mouse *Tonsl* (*Mus musculus*, NCBI Taxon 10090); zebrafish *tonsl* (*Danio rerio*, NCBI Taxon 7955).
- **Natural disease in other species:** No naturally occurring SPONASTRIME-equivalent disease has been reported in companion animals or wildlife (no OMIA entry). Existing animal models are engineered, not natural.
- **Comparative biology:** The DNA-repair function of TONSL is conserved across vertebrates, supporting the mechanistic model; complete loss is lethal in mouse.
- **Transmission / zoonosis:** Not applicable (non-communicable genetic disorder).

---

## 15. Model Organisms

- **Mouse:** A **knock-in *Tonsl* model is embryonic-lethal** (Chang 2019 [PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/): *"a knock-in (KI) Tonsl mouse model leads to embryonic lethality, implying the physiological importance of TONSL."*). Establishes essentiality; **limitation:** complete-null models cannot recapitulate the postnatal skeletal phenotype, so hypomorphic/conditional models are needed.
- **Zebrafish:** *tonsl* used alongside complementation assays to support variant pathogenicity (Burrage 2019 [PMID: 30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/)).
- **In vitro human models:** Patient dermal fibroblasts show cellular defects **complemented by wild-type TONSL** (Chang 2019 [PMID: 30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/): *"cellular defects in dermal fibroblasts from affected individuals are complemented by the expression of wild-type TONSL"*) — direct causal proof. Patient fibroblasts show spontaneous chromosome breaks, reduced proliferation, and increased apoptosis (Micale 2020 [PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)). HEK293T transfection assays confirmed pathogenicity of novel variants (Yao 2025 [PMID: 40794898](https://pubmed.ncbi.nlm.nih.gov/40794898/)).
- **Phenotype recapitulation:** Cellular models faithfully reproduce the genome-instability phenotype; no whole-animal model reproduces the skeletal dysplasia (a key gap).
- **Resources:** MGI (mouse *Tonsl*), ZFIN (zebrafish *tonsl*).

---

## Mechanistic Model / Interpretation (Synthesis)

SPONASTRIME dysplasia unifies a **molecular defect in replication-coupled DNA repair** with a **tissue-level phenotype of failed skeletal growth**. The upstream mechanism is firmly established: TONSL reads the H4K20me0 mark on newly deposited histones to recruit the TONSL–MMS22L HR complex to post-replicative chromatin ([PMID: 27338793](https://pubmed.ncbi.nlm.nih.gov/27338793/)); hypomorphic variants disrupt either the reader (ARD) or dimerization (UBL) function ([PMID: 42525765](https://pubmed.ncbi.nlm.nih.gov/42525765/)), impairing repair and causing chromosome breakage, proliferation failure, and apoptosis in patient cells ([PMID: 32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/)). The **downstream tissue specificity** — why a general DNA-repair defect produces a predominantly skeletal phenotype — is the central inferential step: growth-plate chondrocytes are among the most proliferative postnatal cell populations, so they may be selectively vulnerable to a proliferation/apoptosis defect, explaining short stature, metaphyseal striations, and vertebral dysplasia, with parallel effects in other high-turnover tissues (marrow, lens, odontoblasts). The requirement for **residual function** (null is embryonic-lethal) explains why the disease is compatible with life and why severity tracks with allelic residual activity.

---

## Evidence Base

| PMID | Title (abbreviated) | Source type | Contribution |
|---|---|---|---|
| [30773278](https://pubmed.ncbi.nlm.nih.gov/30773278/) | *Hypomorphic Mutations in TONSL Cause SPONASTRIME Dysplasia* | Human clinical + mouse + in vitro | Causal gene (10/13); embryonic-lethal KI mouse; fibroblast complementation |
| [30773277](https://pubmed.ncbi.nlm.nih.gov/30773277/) | *Bi-allelic Variants in TONSL Cause SPONASTRIME Dysplasia and a Spectrum...* | Human clinical + zebrafish | Independent confirmation; broader spectrum; phenotype description |
| [27338793](https://pubmed.ncbi.nlm.nih.gov/27338793/) | *H4K20me0 marks post-replicative chromatin and recruits the TONSL–MMS22L DNA repair complex* | In vitro/molecular | Defines TONSL molecular function — mechanistic anchor |
| [32959051](https://pubmed.ncbi.nlm.nih.gov/32959051/) | *Novel TONSL variants... chromosome breaks, defective proliferation and apoptosis* | In vitro (patient cells) | Cellular genome-instability phenotype |
| [42525765](https://pubmed.ncbi.nlm.nih.gov/42525765/) | *Pathogenic TONSL variants impair protein dimerization and DNA repair* | Structural/in vitro | R934W/G973R abolish UBL dimerization |
| [10797420](https://pubmed.ncbi.nlm.nih.gov/10797420/) | *SPONASTRIME dysplasia: report of an 11-year-old boy...* | Human clinical | Radiographic/physical phenotype; rarity |
| [9133352](https://pubmed.ncbi.nlm.nih.gov/9133352/) | *Sponastrime dysplasia: diagnostic criteria...* | Human clinical | Radiological diagnostic criteria |
| [40122363](https://pubmed.ncbi.nlm.nih.gov/40122363/) | *Dental and craniofacial manifestations in sponastrime dysplasia* | Human clinical | Dental phenotype; height range |
| [7551156](https://pubmed.ncbi.nlm.nih.gov/7551156/) | *Heterogeneity of SPONASTRIME dysplasia: variant with severe MR* | Human clinical | Phenotypic heterogeneity; severe-ID subgroup |
| [8152878](https://pubmed.ncbi.nlm.nih.gov/8152878/) | *Sponastrime dysplasia: two siblings with mental retardation* | Human clinical | Variant-form family |
| [40794898](https://pubmed.ncbi.nlm.nih.gov/40794898/) | *SPONASTRIME dysplasia with novel TONSL mutation; GH treatment* | Human clinical + in vitro | Neutropenia; limited GH efficacy; functional assay |
| [38684304](https://pubmed.ncbi.nlm.nih.gov/38684304/) | *Child with SPONASTRIME dysplasia, compound heterozygous TONSL* | Human clinical | AR inheritance from carrier parents; WES |
| [27149441](https://pubmed.ncbi.nlm.nih.gov/27149441/) | *Arnold Chiari Malformation With Sponastrime Dysplasia* | Human clinical | Chiari I complication and surgical management |
| [18841068](https://pubmed.ncbi.nlm.nih.gov/18841068/) | *SEMD with joint laxity, leptodactylic/Hall type* | Human clinical | Key differential diagnosis |
| [7824362](https://pubmed.ncbi.nlm.nih.gov/7824362/) | *Sponastrime dysplasia: report on a male patient* | Human clinical | Early case; severe ossification delay |

---

## Limitations and Knowledge Gaps

1. **Chondrocyte mechanism is inferred, not proven.** The link from genome instability to the specific skeletal phenotype (growth-plate chondrocyte depletion → endochondral ossification defect) has not been directly demonstrated in a bone/chondrocyte model.
2. **No viable whole-animal disease model.** Complete *Tonsl* knockout is embryonic-lethal; tissue-specific or patient-variant knock-in models are required to study skeletal pathogenesis in vivo.
3. **Weak genotype–phenotype correlation.** Why some patients have severe intellectual disability/microcephaly and others normal cognition (with overlapping skeletal features) is unresolved; residual-function level and modifier genes are candidate explanations.
4. **Small N (~30–40 cases).** Phenotype frequencies (cataracts, immunodeficiency, neutropenia, Chiari I) are qualitative rather than precise percentages.
5. **No natural-history study or registry**, so progression rates, adult outcomes, and QoL are not systematically documented.
6. **No therapeutic pipeline.** Management is supportive; growth hormone is largely ineffective; no disease-modifying strategy exists.

---

## Proposed Follow-up Experiments / Actions

1. **Conditional / knock-in mouse models** carrying patient hypomorphic alleles (e.g., R934W, G973R) or chondrocyte-specific *Tonsl* deletion to directly test the growth-plate-chondrocyte hypothesis (measure chondrocyte proliferation, apoptosis, endochondral ossification).
2. **Patient-iPSC-derived chondrocytes / cartilage organoids** to assay replication stress, γH2AX foci, chromosome breakage, and proliferation/apoptosis in the disease-relevant cell type, with wild-type TONSL rescue.
3. **Structure–function dissection** across all reported variants (ARD vs. UBL vs. other domains), correlating residual H4K20me0-reading, dimerization, and HR-repair activity with clinical severity — building a validated functional assay for ACMG PS3 variant classification.
4. **International registry / natural-history study** to quantify phenotype frequencies, age-dependent radiographic evolution, immune/hematologic penetrance, and long-term outcomes.
5. **Systematic immunophenotyping and marrow evaluation** to characterize the hematologic/immunologic branch and guide surveillance.
6. **Modifier discovery** via combined WGS + transcriptomics across the cohort to explain the ID/microcephaly variant subgroup.
7. **gnomAD/large-cohort carrier-frequency estimation** for recurrent and predicted-LOF *TONSL* alleles to inform recurrence risk and possible under-diagnosis.

---

*Report compiled from 8 confirmed findings and 15 reviewed papers across 5 investigation iterations. Evidence types span human clinical, in-vitro human, and model-organism sources. Key mechanistic steps (molecular reader function, HR-repair defect, chromosome breakage, proliferation/apoptosis defect, embryonic lethality of null) are experimentally demonstrated; the chondrocyte-to-skeletal-phenotype link is the principal inferred step.*


## Artifacts

- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Sponastrime_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Sponastrime_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000944` (1 mention) - the report calls it "Platyspondyly / vertebral abnormalities"; HP calls it **Abnormal metaphysis morphology**
- `HP:0002650` (2 mentions) - the report calls it "Narrow lumbar interpedicular distances", "Scoliosis"; HP calls it **Scoliosis**
- `HP:0005789` (1 mention) - the report calls it "Metaphyseal striations"; HP calls it **Generalized osteosclerosis**
- `HP:0001541` (1 mention) - the report calls it "Delayed carpal ossification"; HP calls it **Ascites**
- `HP:0004315` (1 mention) - the report calls it "Hypogammaglobulinemia"; HP calls it **Decreased circulating IgG concentration**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001388` (obsolete Joint laxity) (1 mention) - replaced by `HP:0001382`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004322` (1 mention) - the report calls it "Disproportionate short-limb short stature"; HP calls it **Short stature**
- `HP:0005280` (1 mention) - the report calls it "Depressed nasal bridge / short upturned nose"; HP calls it **Depressed nasal bridge**, and lists "Depressed bridge of nose" among its other names
- `HP:0002938` (1 mention) - the report calls it "Lumbar lordosis"; HP calls it **Lumbar hyperlordosis**, and lists "Lumbar lordosis" among its other names
- `HP:0001388` (1 mention) - the report calls it "Joint laxity / hypermobility"; HP calls it **obsolete Joint laxity**
- `HP:0000519` (1 mention) - the report calls it "Childhood cataracts"; HP calls it **Developmental cataract**, and lists "Congenital cataracts" among its other names
- `HP:0001875` (1 mention) - the report calls it "Neutropenia"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0007099` (1 mention) - the report calls it "Arnold–Chiari I malformation"; HP calls it **Chiari type I malformation**, and lists "Arnold Chiari type I malformation" among its other names
- `GO:0005634` (2 mentions) - the report calls it "GO cellular component:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `CL:0000138` (1 mention) - the report calls it "CL cell types:** chondrocyte"; CL calls it **chondrocyte**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002650` - called "Narrow lumbar interpedicular distances", "Scoliosis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.