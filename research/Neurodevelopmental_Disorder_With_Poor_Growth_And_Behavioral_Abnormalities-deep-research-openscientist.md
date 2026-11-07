---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T17:24:00.341429'
end_time: '2026-10-25T17:49:30.563670'
duration_seconds: 1530.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Poor Growth And Behavioral Abnormalities
  mondo_id: MONDO:0859377
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 14
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0011154
    reported_labels:
    - Receptive language delay
    ontology_label: Focal autonomic seizure
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Poor_Growth_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Poor_Growth_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Poor Growth And Behavioral Abnormalities
- **MONDO ID:** MONDO:0859377 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Poor Growth And Behavioral Abnormalities** covering all of the
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

# Neurodevelopmental Disorder With Poor Growth and Behavioral Abnormalities (NEDGBA): Comprehensive Research Report

**Disease:** Neurodevelopmental Disorder With Poor Growth And Behavioral Abnormalities
**MONDO ID:** MONDO:0859377 | **OMIM:** #620242 | **MedGen:** C5830273 | **UMLS:** C5830273 | **DOID:** 0081444
**Causal gene:** **ATP9A** (ATPase Phospholipid Transporting 9A; HGNC gene, NCBI Gene ID 10079, OMIM *609126; 20q13.2)

---

## Summary

The disease specified by **MONDO:0859377 / OMIM #620242** — abbreviated **NEDGBA** (Neurodevelopmental Disorder with poor Growth and Behavioral Abnormalities) — is a rare Mendelian neurodevelopmental disorder caused by variants in **ATP9A**, a gene on chromosome 20q13.2 encoding a **class II P4-ATPase phospholipid flippase**. Because the descriptive disease name does not name a gene and could be confused with many similarly-named neurodevelopmental conditions, we confirmed the gene assignment through identifier cross-referencing: MONDO:0859377 → OMIM 620242 → MedGen C5830273, with the NCBI gene link resolving unambiguously to **ATP9A (Gene ID 10079, alias NEDGBA)**. This report therefore concerns the **ATP9A-related neurodevelopmental disorder**, not any other similarly-named entity.

ATP9A is a transmembrane lipid flippase that translocates phospholipids (notably phosphatidylserine) across endosomal and trans-Golgi membranes, and it is a central driver of the **endosome-to-plasma-membrane recycling pathway**. Mechanistically, ATP9A modulates the activation of the small GTPases **RAB5 and RAB11** to govern endocytic recycling, and it participates in an evolutionarily conserved **MON2:DOPEY2:ATP9A complex** that cooperates with the SNX3-retromer to sort **Wntless (WLS)** and enable **Wnt secretion**. Loss of ATP9A function impairs recycling of cargo such as transferrin and GLUT1, perturbs Wnt signaling, and — in neurons — disrupts neurite morphology, dendritic-spine maturation, and synaptic transmission. These cellular defects plausibly explain the clinical phenotype of severe intellectual disability, speech and motor delay, postnatal growth failure with secondary microcephaly, and behavioral abnormalities.

The disorder shows **dual inheritance**. The predominant form is **autosomal recessive**, caused by biallelic truncating/splice loss-of-function variants and strongly enriched in consanguineous families (reported from Iran, Pakistan, and the Middle East). A more recently recognized **autosomal dominant** form arises from de novo heterozygous missense variants clustering in the catalytic P-type ATPase core. ATP9A is highly constrained against loss-of-function in population databases (gnomAD pLI ≈ 1.0, LOEUF 0.205), consistent with its essential role. The condition is ultra-rare (~7 families / ~13 patients worldwide), static (non-progressive), and currently managed only with supportive, multidisciplinary care; an **Atp9a-null mouse** faithfully recapitulates key human features (muscle weakness, memory deficits, and hyperkinetic movement disorder).

---

## Key Findings

### Finding 1 — ATP9A is the causal gene for MONDO:0859377 / OMIM #620242

The gene underlying this disorder is **ATP9A** on **20q13.2**. Identifier cross-referencing confirms the mapping: MONDO:0859377 corresponds to OMIM 620242 and MedGen C5830273, and the NCBI gene link resolves to ATP9A (Gene ID 10079, alias **NEDGBA**, OMIM *609126). The disease was first delineated from **two consanguineous families with homozygous splice-altering ATP9A variants**, in which three individuals presented with severe intellectual disability, motor and speech impairment, and behavioral anomalies.

> *"We identified two consanguineous families with homozygous variants predicted to alter the splicing of ATP9A which encodes a transmembrane lipid flippase of the class II P4-ATPases. The three individuals homozygous for these putatively truncating variants presented with severe ID, motor and speech impairment, and behavioral anomalies."* — [PMID: 34764295](https://pubmed.ncbi.nlm.nih.gov/34764295/)

An independent cohort reinforced the gene–disease relationship, detecting **homozygous truncating variants** (early premature termination codons; canonical splice-site variants) that caused intellectual disability, postnatal microcephaly, and failure to thrive, with substantially reduced ATP9A mRNA in patient cells ([PMID: 34379057](https://pubmed.ncbi.nlm.nih.gov/34379057/)). Together these establish ATP9A as the causal gene with convergent evidence from multiple independent families.

### Finding 2 — ATP9A is a P4-ATPase flippase controlling endosomal recycling and Wnt secretion

ATP9A localizes to **phosphatidylserine-positive early/recycling endosomes and the trans-Golgi network (TGN)**. Functional studies show that its depletion **delays transferrin recycling** from endosomes to the plasma membrane and traps the glucose transporter **GLUT1** in endosomes, while leaving EGF degradation and Shiga-toxin retrograde transport intact — indicating a selective role in the recycling (not degradative or retrograde) pathway.

> *"Depletion of ATP9A delayed the recycling of transferrin from endosomes to the plasma membrane."* — [PMID: 27733620](https://pubmed.ncbi.nlm.nih.gov/27733620/)

ATP9A additionally forms an **evolutionarily conserved MON2:DOPEY2:ATP9A complex** that cooperates with the SNX3-retromer to sort **Wntless** and drive **Wnt secretion**, a developmentally critical signaling pathway. Suppression of the *C. elegans* orthologue **tat-5** phenocopies retromer loss and perturbs Wnt signaling.

> *"SNX3 associates with an evolutionary conserved endosome-associated membrane re-modelling complex composed of MON2, DOPEY2 and the putative aminophospholipid translocase, ATP9A."* — [PMID: 30213940](https://pubmed.ncbi.nlm.nih.gov/30213940/)

Consistent with these mechanisms, patient fibroblasts show reduced ATP9A mRNA and dysregulated interacting genes **ARPC3** and **SNX3** ([PMID: 34379057](https://pubmed.ncbi.nlm.nih.gov/34379057/)).

### Finding 3 — Dual inheritance: recessive loss-of-function and dominant de novo missense

Population genetics indicate ATP9A is highly intolerant to both loss-of-function and missense change: gnomAD **pLI = 0.9999**, **LOEUF (oe_lof_upper) = 0.205**, oe_lof = 0.109, **missense Z = 4.15**, **lof Z = 6.62**. The recessive form arises from biallelic truncating/splice variants. A distinct **autosomal dominant** mechanism was subsequently described, with **five de novo heterozygous missense variants** — p.(Thr393Arg), p.(Glu400Gln), p.(Lys461Glu), p.(Gly552Ala), and p.(His713Asp) — in patients with intellectual disability.

> *"we propose a novel mode of inheritance for ATP9A-related disorders with the identification of five de novo heterozygous missense variants (p.(Thr393Arg), p.(Glu400Gln), p.(Lys461Glu), p.(Gly552Ala), and p.(His713Asp)), in patients with intellectual disability."* — [PMID: 40226306](https://pubmed.ncbi.nlm.nih.gov/40226306/)

Functionally, overexpression of mutant Atp9a in HeLa cells and primary neurons caused **loss of mature dendritic spines**, and shRNA knockdown reduced dendrite number, supporting pathogenicity of the dominant missense alleles ([PMID: 40226306](https://pubmed.ncbi.nlm.nih.gov/40226306/)).

### Finding 4 — Phenotype spectrum

Aggregated HPO annotations across three reports (PMID 34379057, 34764295, 36604604) define a consistent clinical picture dominated by neurodevelopmental, growth, and behavioral features:

| Phenotype (HPO suggestion) | Frequency | Notes |
|---|---|---|
| Severe intellectual disability (HP:0010864) | 7/9 | Core feature |
| Delayed speech/language development (HP:0000750) | 6/6 | Universal |
| Motor delay (HP:0001270) | 6/6 | Universal |
| Poor fine motor coordination (HP:0007010) | 6/6 | Universal |
| Attention deficit hyperactivity disorder (HP:0007018) | 5/5 | Core behavioral feature |
| Hypotonia (HP:0001252) | 3/3 | |
| Muscle weakness (HP:0001324) | 3/3 | |
| Absent speech (HP:0001344) | 3/3 | |
| Receptive language delay (HP:0011154) | 3/3 | |
| Postnatal growth retardation (HP:0008897) | 3/3 | "Poor growth" |
| Failure to thrive (HP:0001508) | 3/3 | "Poor growth" |
| Secondary (postnatal) microcephaly (HP:0005484) | 5/9 | Postnatal brain-growth defect |
| Sleep disturbance (HP:0002360) | 5/6 | |
| Short attention span (HP:0000736) | 3/3 | |
| Gastroesophageal reflux (HP:0002020) | 3/3 | |
| Aggressive behavior (HP:0000718) | 2/2 | |
| Strabismus (HP:0000486) | 3/6 | |
| 2-3 toe cutaneous syndactyly (HP:0004691) | 2/3 | |
| Autistic behavior / motor stereotypy / seizure | variable (seizure ~1/3) | Minority |

Brain MRI findings include **corpus callosum hypoplasia, cerebellar vermis hypoplasia, and delayed CNS myelination**. Dysmorphism includes **smooth philtrum (3/3)** and **thin upper lip (3/3)**. Onset is infantile/childhood (5/6 infantile).

> *"the nonsense mutations c.433C>T/c.658C>T/c.983G>A (p. Arg145*/p. Arg220*/p. Trp328*) in ATP9A (NM_006045.3) cause autosomal recessive hypotonia, intellectual disability (ID) and attention deficit hyperactivity disorder (ADHD)."* — [PMID: 36604604](https://pubmed.ncbi.nlm.nih.gov/36604604/)

### Finding 5 — Atp9a-null mouse recapitulates the disorder; RAB5/RAB11 recycling mechanism

A knockout mouse model provides strong in vivo validation. **Atp9a-null mice show decreased muscle strength, memory deficits, and a hyperkinetic movement disorder**, together with abnormal neurite morphology and impaired synaptic transmission in primary motor cortex and hippocampus — paralleling the patient features of hypotonia/weakness, intellectual disability, and ADHD-like hyperkinesis.

> *"Atp9a null mice show decreased muscle strength, memory deficits and hyperkinetic movement disorder, recapitulating the symptoms observed in patients."* — [PMID: 36604604](https://pubmed.ncbi.nlm.nih.gov/36604604/)

Mechanistically, the same study established the molecular pathway: ATP9A localizes to endosomes and drives endosomal recycling by modulating small-GTPase activation.

> *"plays a pivotal role in endosomal recycling pathway by modulating small GTPase RAB5 and RAB11 activation."* — [PMID: 36604604](https://pubmed.ncbi.nlm.nih.gov/36604604/)

Pathogenic mutants mislocalize and cause aberrant endosomal recycling, and ATP9A is required for maintaining neurite morphology and neural-cell viability in vitro. This complements independent evidence for ATP9A's role in transferrin/GLUT1 recycling (PMID 27733620) and SNX3-retromer/Wnt secretion (PMID 30213940).

### Finding 6 — Protein identity and variant spectrum

ATP9A corresponds to **UniProt O75110**, "Probable phospholipid-transporting ATPase IIA," a **1047-amino-acid** class II P4-ATPase. Its catalytic reaction is: **ATP + H₂O + phospholipid(side 1) → ADP + phosphate + phospholipid(side 2)**. It localizes to early/recycling/late endosome membranes, the TGN, and the plasma membrane. Relevant GO annotations include **ATPase-coupled intramembrane lipid carrier activity (GO:0140326)**, **phospholipid translocation (GO:0045332)**, **regulation of endocytic recycling (GO:2001135)**, and **neuron projection morphogenesis (GO:0048812)**.

The disease-variant spectrum is **predominantly truncating/splice (loss-of-function)** in recessive cases — e.g., c.433C>T (p.Arg145*), c.658C>T (p.Arg220*), c.983G>A (p.Trp328*), plus splice variants; ClinVar also contains a likely-pathogenic splice variant NM_006045.3:c.1181-2A>G. gnomAD shows **no biallelic LoF in controls** (pLI ≈ 1.0). Dominant de novo missense cases (p.Thr393Arg, p.Glu400Gln, p.Lys461Glu, p.Gly552Ala, p.His713Asp) act via an altered protein with ER retention or impaired dendritic-spine maturation rather than simple haploinsufficiency.

### Finding 7 — Dominant de novo missense variants cluster in the catalytic ATPase core

The dominant missense variants map directly onto the **conserved catalytic P-type ATPase core** (P- and N-domains). UniProt O75110 identifies the catalytic phosphorylation residue as **Asp391** (forms the 4-aspartylphosphate intermediate within the canonical **DKTGT** motif), with ATP/Mg²⁺-binding residues at positions 391–393, 502, 544–549, 568, 597, 677–679, and 759–789. The reported de novo variants cluster here: **p.Thr393Arg** lies within the DKTGT phosphorylation motif adjacent to Asp391; **p.Glu400Gln** and **p.Lys461Glu** fall in the phosphorylation/nucleotide-binding region; **p.Gly552Ala** sits near nucleotide-binding residues 544–549; and **p.His713Asp** is near the 677–679/759 binding cluster. Domain architecture (InterPro/Pfam) comprises P-type ATPase IV (IPR006539), a HAD-like hydrolase fold, E1-E2 ATPase (PF00122), PhoLip_ATPase_N/C (PF16209/PF16212), and 10 transmembrane segments. This spatial clustering in the catalytic machinery provides a structural rationale for how heterozygous missense alleles impair function.

### Finding 8 — Clinical summary: ultra-rare, static, consanguinity-enriched, supportively managed

**Epidemiology:** ultra-rare; approximately **7 families / ~13 patients** reported worldwide across four studies (PMID 34764295, 34379057, 36604604, 40226306). No prevalence or incidence estimate exists, and there is no dedicated Orphanet entry (Monarch/MONDO cross-references only to DOID:0081444, MedGen C5830273, OMIM 620242, UMLS C5830273).

**Inheritance:** predominantly autosomal recessive (consanguinity-enriched; Iran/Pakistan/Middle East), with a distinct autosomal dominant de novo missense form. Penetrance appears complete; expressivity is variable (mild-to-severe ID; seizures in a minority, ~1/3).

**Course:** congenital-to-infantile onset, **static (non-progressive) developmental encephalopathy**; secondary (postnatal) microcephaly indicates a postnatal brain-growth critical window.

**Diagnosis:** molecular (WES/WGS or ID gene panels; RNA/fibroblast studies for splice variants); brain MRI may show corpus callosum/cerebellar vermis hypoplasia and delayed myelination; CMA/karyotype typically normal.

**Treatment:** no disease-specific or curative therapy — symptomatic/supportive multidisciplinary care.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (from initiating lesion to clinical manifestation)

1. **ATP9A variant** (biallelic truncating/splice LoF **OR** de novo heterozygous missense in the catalytic core) **leads to** loss or dysfunction of the ATP9A phospholipid flippase. *(Demonstrated: reduced mRNA for truncating variants, PMID 34379057; mislocalization and spine defects for missense, PMID 40226306.)*
2. Reduced flippase activity **results in** impaired phospholipid (phosphatidylserine) translocation across endosomal/TGN membranes. *(Inferred from biochemical function, UniProt O75110 / PMID 27733620.)*
3. This **leads to** defective modulation of **RAB5 and RAB11** GTPase activation and impaired endosome-to-plasma-membrane recycling of cargo (transferrin, GLUT1). *(Demonstrated: PMID 36604604, PMID 27733620.)*

   **Branch A →** Impaired **SNX3-retromer / MON2:DOPEY2:ATP9A** sorting of **Wntless** **results in** reduced **Wnt secretion** and perturbed developmental signaling. *(Demonstrated in cells and C. elegans, PMID 30213940.)*
4. In neurons, defective recycling and signaling **result in** abnormal **neurite morphology**, **loss of mature dendritic spines**, and reduced neuronal viability. *(Demonstrated: PMID 40226306, PMID 36604604.)*
5. These cellular defects **lead to** impaired **synaptic transmission** in motor cortex and hippocampus. *(Demonstrated in Atp9a-null mice, PMID 36604604.)*
6. Network-level synaptic/developmental dysfunction **results in** the clinical phenotype: severe **intellectual disability**, **speech/motor delay with hypotonia**, **ADHD and other behavioral abnormalities**, and (via disrupted postnatal brain and somatic growth) **postnatal growth failure with secondary microcephaly**. *(Clinical correlation; mouse recapitulation, PMID 36604604.)*

```
ATP9A LoF / missense
        │
        ▼
 ↓ flippase activity (PS translocation)
        │
        ▼
 ↓ RAB5/RAB11 activation ──► impaired endosome→PM recycling (transferrin, GLUT1)
        │                                         │
        │                                         └──► Branch A: ↓ SNX3-retromer
        │                                              Wntless sorting ──► ↓ Wnt secretion
        ▼
 abnormal neurite morphology / ↓ dendritic spines / ↓ neuron viability
        │
        ▼
 impaired synaptic transmission (cortex, hippocampus)
        │
        ▼
 ID + speech/motor delay + ADHD/behavioral abnormalities + poor growth + 2° microcephaly
```

**Upstream vs downstream:** The flippase lesion and the RAB5/RAB11 recycling defect (plus the Wnt-secretion branch) are **upstream**; neurite/spine and synaptic defects are **intermediate**; the behavioral/cognitive/growth phenotype is **downstream**. **Cell types** implicated (CL suggestions): neuron (CL:0000540), glutamatergic neuron (CL:0000679), hippocampal pyramidal neuron, cortical neuron. **Anatomy** (UBERON): cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421), cerebellar vermis (UBERON:0004720), corpus callosum (UBERON:0002336). **Subcellular** (GO cellular component): recycling endosome (GO:0055037), early endosome membrane (GO:0031901), trans-Golgi network membrane (GO:0032588), plasma membrane (GO:0005886). **Biological processes** (GO): phospholipid translocation (GO:0045332), regulation of endocytic recycling (GO:2001135), neuron projection morphogenesis (GO:0048812), dendritic spine development (GO:0060996), Wnt signaling pathway (GO:0016055).

---

## Section-by-Section Report

### 1. Disease Information
NEDGBA is a rare Mendelian neurodevelopmental disorder characterized by intellectual disability, speech/motor delay, poor postnatal growth (failure to thrive, secondary microcephaly), and behavioral abnormalities (ADHD, aggression, autistic features). **Identifiers:** MONDO:0859377; OMIM #620242; MedGen C5830273; UMLS C5830273; DOID:0081444. No dedicated Orphanet or specific ICD-10/ICD-11 code was identified; MeSH indexing is via general neurodevelopmental-disorder terms. **Synonyms:** NEDGBA; ATP9A-related neurodevelopmental disorder. Information is derived from **aggregated disease-level resources and small published patient cohorts** (case series), not large EHR datasets.

### 2. Etiology
**Causal factor:** genetic — pathogenic variants in **ATP9A**. **Genetic risk factors:** biallelic truncating/splice LoF variants (recessive) or de novo heterozygous missense variants in the catalytic core (dominant). **Environmental risk factors:** none established; **consanguinity** is a major demographic risk factor for the recessive form. **Protective factors:** none specifically identified. **Gene–environment interactions:** none characterized.

### 3. Phenotypes
See Finding 4 table. Phenotype types span developmental/cognitive (ID, speech/motor delay), behavioral (ADHD, aggression, autistic behavior, sleep disturbance), physical/growth (failure to thrive, postnatal microcephaly, dysmorphism), neuromuscular (hypotonia, weakness), gastrointestinal (GERD), ophthalmologic (strabismus), and structural brain anomalies. Onset is neonatal-to-infantile; severity is moderate-to-severe; course is static. Quality-of-life impact is substantial given severe ID and dependence for daily functioning, though no formal QoL instrument data exist for this ultra-rare disorder.

### 4. Genetic/Molecular Information
**Causal gene:** ATP9A (HGNC; NCBI Gene 10079; OMIM *609126; 20q13.2). **Variants:** recessive truncating/splice (c.433C>T/p.Arg145*, c.658C>T/p.Arg220*, c.983G>A/p.Trp328*, NM_006045.3:c.1181-2A>G splice) — classified pathogenic/likely pathogenic per ACMG; dominant de novo missense (p.Thr393Arg, p.Glu400Gln, p.Lys461Glu, p.Gly552Ala, p.His713Asp). **Allele frequency:** biallelic LoF absent in gnomAD controls; ATP9A is LoF-constrained (pLI ≈ 1.0, LOEUF 0.205). **Origin:** germline. **Functional consequence:** loss of function (recessive); altered/possibly dominant-negative or hypomorphic protein with ER retention/spine-maturation defects (dominant). **Modifier genes/epigenetics/chromosomal abnormalities:** none established (CMA/karyotype typically normal).

### 5. Environmental Information
No environmental factors, lifestyle factors, or infectious agents are implicated. This is a monogenic disorder.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above.

### 7. Anatomical Structures Affected
**Primary organ/system:** central nervous system (brain) — cerebral cortex, hippocampus, cerebellar vermis, corpus callosum, with delayed myelination. **Body systems:** nervous (primary), musculoskeletal (hypotonia/weakness), gastrointestinal (GERD), growth/endocrine (failure to thrive). **Cell level:** neurons (dendritic spines, neurites). **Subcellular:** recycling/early endosomes, TGN, plasma membrane. **Localization:** bilateral, central.

### 8. Temporal Development
Congenital-to-infantile onset; insidious/chronic; static (non-progressive) encephalopathy; lifelong duration. Microcephaly is **postnatal (secondary)**, defining a postnatal brain-growth **critical window**. No remission.

### 9. Inheritance and Population
Predominantly **autosomal recessive** (consanguinity-enriched; Iran, Pakistan, Middle East), plus a distinct **autosomal dominant de novo** form. Penetrance appears complete; expressivity variable. No prevalence/incidence estimates (ultra-rare, ~7 families/~13 patients). Carrier frequency not established; no founder mutation defined. No marked sex bias reported.

### 10. Diagnostics
**Genetic testing** is the diagnostic cornerstone: WES/WGS or intellectual-disability gene panels; single-gene/targeted testing; **RNA or patient-fibroblast studies** to resolve splice variants. **Imaging:** brain MRI may reveal corpus callosum and cerebellar vermis hypoplasia and delayed myelination. **CMA/karyotype:** typically normal. **Differential diagnosis:** other autosomal-recessive ID syndromes with microcephaly, failure to thrive and behavioral disturbance; distinguished by ATP9A genotype.

### 11. Outcome/Prognosis
No mortality data; the disorder is static and compatible with survival into adulthood. Morbidity is driven by severe ID, communication/motor impairment, and behavioral/sleep problems, with high dependence for daily functioning. No disease-specific prognostic biomarkers.

### 12. Treatment
No curative or disease-specific therapy exists. Management is **symptomatic and supportive/multidisciplinary**: early developmental intervention; physical, occupational, and speech therapy; nutritional support for failure to thrive; and targeted management of ADHD, sleep disturbance, seizures (minority), and GERD. NCIT intervention concepts: supportive care, physical therapy, occupational therapy, speech therapy, nutritional support. No gene/cell/RNA-targeted therapies are in trials.

### 13. Prevention
No primary prevention beyond **genetic counseling**. For at-risk/consanguineous families: **carrier and cascade testing**, and reproductive options including **PGT-M (preimplantation genetic testing for monogenic disorders)** and prenatal testing. Secondary/tertiary prevention focuses on early intervention and complication management.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal or wildlife disease is documented. The *C. elegans* orthologue **tat-5** is functionally conserved (its suppression phenocopies retromer loss and perturbs Wnt signaling, PMID 30213940), supporting evolutionary conservation of the mechanism. Orthologues exist in mouse (*Atp9a*) and other vertebrates.

### 15. Model Organisms
The key model is the **Atp9a-null (knockout) mouse**, which recapitulates decreased muscle strength, memory deficits, and hyperkinetic movement disorder, with abnormal neurite morphology and impaired synaptic transmission (PMID 36604604). Cellular models include **HeLa cells** and **primary neurons** (overexpression/knockdown demonstrating dendritic-spine and dendrite defects, PMID 40226306) and **patient fibroblasts** (reduced mRNA, dysregulated ARPC3/SNX3, PMID 34379057). The *C. elegans* **tat-5** model supports the conserved Wnt/retromer mechanism. **Limitations:** mouse behavioral phenotypes do not fully capture human cognitive/speech deficits, and no model yet dissects the dominant-missense mechanism in vivo.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [34764295](https://pubmed.ncbi.nlm.nih.gov/34764295/) | *Biallelic truncation variants in ATP9A are associated with a novel autosomal recessive NDD* | Human clinical | Primary gene–disease link; recessive splice/truncating variants; core phenotype |
| [34379057](https://pubmed.ncbi.nlm.nih.gov/34379057/) | *Biallelic truncating variants in ATP9A* | Human clinical + cell | Independent confirmation; microcephaly, failure to thrive; reduced mRNA; ARPC3/SNX3 dysregulation |
| [36604604](https://pubmed.ncbi.nlm.nih.gov/36604604/) | *Atp9a null mice recapitulate NDD; RAB5/RAB11 mechanism* | Model organism + human | KO mouse recapitulation; RAB5/RAB11 endosomal-recycling mechanism; nonsense variants causing AR hypotonia/ID/ADHD |
| [40226306](https://pubmed.ncbi.nlm.nih.gov/40226306/) | *Heterozygous missense variants in ATP9A* | Human clinical + cell | Dominant de novo missense mechanism; dendritic-spine/dendrite defects |
| [27733620](https://pubmed.ncbi.nlm.nih.gov/27733620/) | *ATP9A required for endosome-to-PM recycling* | In vitro | Core recycling function (transferrin, GLUT1) |
| [30213940](https://pubmed.ncbi.nlm.nih.gov/30213940/) | *SNX3-retromer requires MON2:DOPEY2:ATP9A for Wntless sorting/Wnt secretion* | In vitro + C. elegans | Wnt-secretion branch; evolutionary conservation (tat-5) |

All six papers are mutually reinforcing; no paper contradicts the ATP9A gene–disease assignment or the endosomal-recycling mechanism. The two inheritance mechanisms (recessive LoF vs dominant missense) are complementary rather than conflicting.

---

## Limitations and Knowledge Gaps

- **Very small evidence base:** ~7 families / ~13 patients worldwide. Prevalence/incidence are unknown, and phenotype frequencies are derived from tiny denominators (e.g., 7/9, 3/3) that will shift as more cases accrue.
- **No Orphanet/ICD-specific entry**, limiting standardized epidemiological indexing.
- **Dominant mechanism incompletely resolved:** whether the de novo missense variants act via haploinsufficiency, dominant-negative, or gain-of-function is not definitively established; no in vivo model of the missense alleles exists.
- **Genotype–phenotype correlations** (e.g., which variants predict seizures, severity) are not yet defined.
- **Wnt-secretion branch** is demonstrated in cell/worm systems but not directly shown to be the operative mechanism in patient neurons.
- **No natural animal disease, no biomarkers, no therapies** — treatment evidence is entirely supportive and extrapolated from general NDD care.

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry / GeneMatcher recruitment** to expand the cohort, refine phenotype frequencies, and enable genotype–phenotype correlation (recessive LoF vs dominant missense; seizure predictors).
2. **Functional dissection of dominant missense alleles:** patient-derived iPSC neurons/organoids and knock-in mouse models to determine whether p.Thr393Arg etc. are loss-of-function, dominant-negative, or gain-of-function, and to test flippase activity and RAB5/RAB11 cycling directly.
3. **Quantify the Wnt-secretion branch in neurons:** measure Wntless trafficking and Wnt target-gene output in patient cells to establish whether this branch contributes to the brain-growth/microcephaly phenotype.
4. **Biomarker discovery:** metabolomic/lipidomic profiling of patient fibroblasts/plasma (phosphatidylserine handling) and transcriptomics (ARPC3, SNX3, RAB effectors) to identify a diagnostic or monitoring signature.
5. **Deep brain phenotyping of Atp9a-null mice** across the postnatal growth window to pinpoint the critical period and test candidate interventions (e.g., modulators of endosomal recycling or Wnt signaling).
6. **Clinical care consensus:** develop supportive-care management guidance (ADHD, sleep, GERD, nutrition) specific to this disorder and standardize MRI reporting (corpus callosum, cerebellar vermis, myelination).

---

### Ontology term appendix
- **Gene/protein:** ATP9A (HGNC), UniProt O75110; GO:0140326, GO:0045332, GO:2001135, GO:0048812, GO:0060996, GO:0016055
- **Phenotypes (HPO):** HP:0010864, HP:0000750, HP:0001270, HP:0007018, HP:0001252, HP:0001508, HP:0008897, HP:0005484, HP:0002360, HP:0000718, HP:0004691
- **Cell types (CL):** CL:0000540, CL:0000679
- **Anatomy (UBERON):** UBERON:0000956, UBERON:0002421, UBERON:0004720, UBERON:0002336
- **Subcellular (GO CC):** GO:0055037, GO:0031901, GO:0032588, GO:0005886
- **Disease (MONDO):** MONDO:0859377


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Poor_Growth_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Poor_Growth_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011154` (1 mention) - the report calls it "Receptive language delay"; HP calls it **Focal autonomic seizure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000750` (2 mentions) - the report calls it "Delayed speech/language development"; HP calls it **Delayed speech and language development**
- `HP:0004691` (2 mentions) - the report calls it "2-3 toe cutaneous syndactyly"; HP calls it **2-3 toe syndactyly**, and lists "2-3 toes syndactyly" among its other names