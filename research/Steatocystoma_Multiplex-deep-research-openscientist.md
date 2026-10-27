---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T17:32:01.360240'
end_time: '2026-10-23T18:15:51.512203'
duration_seconds: 2630.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Steatocystoma Multiplex
  mondo_id: MONDO:0008485
  category: Mendelian
  causal_genes: KRT17
  omim_id: not recorded
  synonyms: sebocystomatosis
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 16
  validator_version: 0.3.0
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0032320
    reported_labels:
    - cutaneous cyst/steatocystoma
    ontology_label: Affected
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Steatocystoma_Multiplex-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Steatocystoma_Multiplex-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Steatocystoma Multiplex
- **MONDO ID:** MONDO:0008485 (if available)
- **Causal gene(s):** KRT17
- **OMIM:** not recorded
- **Synonyms:** sebocystomatosis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Steatocystoma Multiplex** covering all of the
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

# Steatocystoma Multiplex (MONDO:0008485): A Comprehensive Disease Characteristics Report

**Causal gene: _KRT17_ (keratin 17; HGNC:6427; NCBI Gene 3872; OMIM gene 148069). Disease OMIM 184500. Synonym: sebocystomatosis.**

---

## Summary

Steatocystoma multiplex (SM) is an autosomal dominant benign genodermatosis of the pilosebaceous unit caused by heterozygous missense mutations in the **1A helix-initiation rod domain of _KRT17_ (keratin 17)**. The disorder manifests as multiple firm, non-tender, sebum-filled dermal cysts of the sebaceous follicle, distributed preferentially on the trunk, axillae, groin, and limbs, typically emerging around puberty under androgenic drive. The mutations cluster at a conserved helix-initiation motif, with **Arg94 (R94) as the predominant hotspot** (R94C, R94H) and **Asn92 (N92) as a secondary hotspot** (N92H, N92S). These variants act through a **dominant-negative mechanism**: the mutant keratin protein is incorporated into the keratin intermediate-filament network, where it disrupts hydrophobic interactions and surface-charge contacts required for keratin dimer/tetramer assembly, producing defective filament formation and cytoplasmic keratin aggregation in the cells lining the sebaceous duct.

A central and well-documented feature of this gene is **allelism**: identical _KRT17_ mutations (notably R94C) can produce either classical SM or pachyonychia congenita type 2 (PC-2, now PC-K17), establishing that SM and PC-2 lie on a single _KRT17_ phenotypic spectrum and that the specific phenotype is "independent of the specific mutation involved" (Covello 1998). Cutaneous cysts and natal teeth are the KRT17-signature phenotypes among the pachyonychia-congenita keratin genes. A systematic review of 145 confirmed cases provides quantitative natural-history data: median onset age of **23 years**, median diagnosis age of **31 years** (≈8-year diagnostic delay), with familial cases (~26%) showing significantly earlier onset and greater severity.

There is **no cure**; management is symptomatic and includes surgical excision, drainage, cryotherapy, oral isotretinoin (especially for the suppurative variant), laser, and biologics for inflammatory/suppurative disease. Because SM belongs to the dominant-negative keratinopathy class, **allele-specific siRNA** — clinically validated in pachyonychia congenita (TD101 against KRT6A, first-in-human phase Ib trial) — represents a rational, mechanism-targeted future therapy. SM does not affect lifespan and has no malignant potential; its burden is cosmetic, psychosocial, and related to secondary infection/scarring.

---

## Key Findings

### Finding 1 — SM is caused by heterozygous missense mutations in the 1A rod domain of _KRT17_

Landmark sequencing studies have established that SM arises from co-segregating heterozygous missense mutations clustered in the conserved **helix-initiation (1A) domain** of _KRT17_, inherited in an autosomal dominant manner. Smith et al. (1997) first reported the N92H and R94H mutations in two families diagnosed as steatocystoma multiplex: *"We also show heterozygous missense mutations in K17 (N92H and R94H) in two families diagnosed as steatocystoma multiplex"* ([PMID: 9008238](https://pubmed.ncbi.nlm.nih.gov/9008238/)). Covello et al. (1998) extended the mutational spectrum with R94C and N92S and underlined the appendageal expression of K17: *"Keratin 17 (K17) is a differentiation-specific keratin expressed in the nail bed, hair follicle, sebaceous gland and other epidermal appendages"* ([PMID: 9767294](https://pubmed.ncbi.nlm.nih.gov/9767294/)). The recurrent R94C allele was subsequently confirmed in a four-generation Chinese pedigree in which direct sequencing *"revealed a heterozygous mutation, c.280C/T (R94C), which was located in exon 1 of the KRT17 gene in all 10 affected family members"* — absent in 15 unaffected relatives and 100 controls ([PMID: 26165312](https://pubmed.ncbi.nlm.nih.gov/26165312/)). Together these studies demonstrate strong genotype co-segregation and establish the 1A domain hotspot as the molecular signature of SM.

### Finding 2 — SM and pachyonychia congenita type 2 are allelic _KRT17_ disorders; phenotype is mutation-independent

A defining insight into SM genetics is that it is **allelic** with pachyonychia congenita type 2. Covello et al. reported two unrelated families carrying the **identical R94C mutation**, one presenting as classical PC-2 and the other as steatocystoma multiplex, and concluded that *"the alternate phenotypes which arise from these genetic lesions in K17 are independent of the specific mutation involved"* ([PMID: 9767294](https://pubmed.ncbi.nlm.nih.gov/9767294/)). This implies that **modifier genes and/or environmental factors**, rather than the specific nucleotide change, determine whether a carrier develops predominantly cysts (SM) or predominantly nail/palmoplantar disease (PC-2). More recently, Koprulu et al. (2022) showed that KRT17 R94H in the **homozygous (recessive)** state causes an atypical pachyonychia congenita, while *"Heterozygous variants in KRT17 cause PC2 (PC-K17) with main characteristics of pachyonychia, subungual keratosis, palmoplantar keratoderma, hyperhidrosis, oral leukokeratosis and epidermal cysts, or steatocystoma multiplex, both with dominant inheritance"* ([PMID: 35676340](https://pubmed.ncbi.nlm.nih.gov/35676340/)). SM should therefore be understood as one pole of a continuous KRT17 phenotypic spectrum.

### Finding 3 — Keratin 17 biology (hair-follicle cycling, stress response, TNFα/NF-κB) informs SM pathophysiology

K17 is not merely a structural scaffold; it is a stress-responsive, signaling-active intermediate filament. Tong & Coulombe (2006) showed that **Krt17-null mice develop alopecia** in the first postnatal week: *"Keratin 17 (K17)-null mice develop alopecia in the first week post-birth, correlating with hair shaft fragility and untimely apoptosis in the hair bulb"* ([PMID: 16702408](https://pubmed.ncbi.nlm.nih.gov/16702408/)). They further identified *"K17 and TNFalpha as two novel and interdependent regulators of hair cycling,"* linking K17 to TNFα/NF-κB signaling through its interaction with TRADD; TNFα ablation partially rescues the hair-cycle defect. Additional work shows K17 regulates nuclear morphology and chromatin organization ([PMID: 33008845](https://pubmed.ncbi.nlm.nih.gov/33008845/)) and participates in a Rac1-mediated DNA-damage response in keratinocytes ([PMID: 41880216](https://pubmed.ncbi.nlm.nih.gov/41880216/)). These functions explain why K17 dysfunction preferentially perturbs appendageal (sebaceous gland, hair follicle, nail bed) homeostasis — the tissues in which cysts and dystrophy arise.

### Finding 4 — SM clinical phenotype: benign sebum-filled sebaceous-follicle cysts with onset in adolescence/early adulthood

Clinically, steatocystomas are *"benign, sebum-filled cysts of the sebaceous follicle that typically manifest as firm nontender lesions of variable size and location"* ([PMID: 41363957](https://pubmed.ncbi.nlm.nih.gov/41363957/)). They occur as isolated (simplex), grouped multiple (multiplex), or suppurative (steatocystoma multiplex suppurativum, SMS) forms. The characteristic distribution is described by Marasca et al. (2020): *"The occurrence of multiple asymptomatic cutaneous cysts on the axillae, groin, trunk, and limbs characterizes the disease"* ([PMID: 33088817](https://pubmed.ncbi.nlm.nih.gov/33088817/)). The **histopathology is diagnostic**: a dermal cyst lined by stratified squamous epithelium with a characteristic eosinophilic corrugated ("shark-tooth") cuticle and **absent granular layer**, with flattened sebaceous gland lobules in or adjacent to the cyst wall. Sharma et al. describe *"a cyst… in the mid-dermis, lined by stratified squamous, agranular epithelium, which contained degenerated keratin"* ([PMID: 29998099](https://pubmed.ncbi.nlm.nih.gov/29998099/)). Lesions are usually asymptomatic but can be disfiguring and may become secondarily infected or scarred.

### Finding 5 — Quantitative epidemiology: median onset age 23, familial cases ~26% with earlier onset, Arg94 predominant mutation site

A systematic review of 145 confirmed SM cases from 82 publications (Sun 2026) provides the most robust quantitative natural history to date. There is no clear geographical or ethnic predilection. *"The median age at onset was 23 years and the median age at diagnosis was 31 years, reflecting a diagnostic delay of approximately 8 years"* ([PMID: 42518883](https://pubmed.ncbi.nlm.nih.gov/42518883/)). Familial disease is a meaningful minority with a more severe course: *"Familial cases (26.2%) had a significantly earlier age at onset (13.5 vs. 30.0 years, P < 0.001) and diagnosis (22.0 vs. 35.0 years, P < 0.001), and higher rates of infected lesions and nail dystrophy."* Hidradenitis suppurativa co-occurrence was more prevalent in females (12.5% vs 1.5%, P = 0.019). At the molecular level, *"KRT17 was the most frequently mutated gene, with Arg94 as the predominant mutation site."* These data confirm young-adult onset, a substantial diagnostic delay, and the Arg94 hotspot across aggregated cases.

### Finding 6 — SM belongs to the dominant-negative keratinopathy class; allele-specific siRNA is a validated therapeutic paradigm

SM sits within a family of **dominant-negative keratin disorders**. Pachyonychia congenita — including the K17/PC-K17 subtype allelic with SM — is *"an autosomal dominant genodermatosis caused by heterozygous mutations in any one of the genes encoding the differentiation-specific keratins K6a, K6b, K16, or K17,"* with epidermal cysts among its features ([PMID: 21430705](https://pubmed.ncbi.nlm.nih.gov/21430705/)). The dominant-negative aggregation mechanism is directly druggable: Leachman et al. developed a mutant allele-specific siRNA (TD101) against KRT6A N171K and demonstrated *"potent inhibition of the mutant allele and reversal of the cellular aggregation phenotype"* in vitro ([PMID: 18495438](https://pubmed.ncbi.nlm.nih.gov/18495438/)), then advanced it to a first-in-human phase Ib trial: *"This trial represents the first time that siRNA has been used in a clinical setting to target a mutant gene or a genetic disorder, and the first use of siRNA in human skin"* ([PMID: 19935778](https://pubmed.ncbi.nlm.nih.gov/19935778/)), achieving callus regression without adverse events. Allele-specific RNAi can discriminate single-nucleotide differences, silencing only the mutant allele ([PMID: 26264709](https://pubmed.ncbi.nlm.nih.gov/26264709/)). This provides a clear, mechanism-matched therapeutic avenue for SM.

### Finding 7 — KRT17 mutations specifically associate with cysts and natal teeth; hotspot mutations destabilize keratin assembly (structural modeling)

Within genetically confirmed pachyonychia congenita cohorts, the KRT17 genotype is specifically associated with cysts. In 254 PC patients, Eliason et al. found *"a strong association of natal teeth and cysts in carriers of a KRT17 mutation"* ([PMID: 22264670](https://pubmed.ncbi.nlm.nih.gov/22264670/)). Wu et al. integrated genotype, protein structure, and phenotype using the International PC Research Registry, confirming *"cutaneous cysts, follicular hyperkeratosis, and natal teeth with K17 mutations,"* and provided the structural mechanism: *"hotspot missense mutations in PC largely disrupted hydrophobic interactions or surface charge. The former may destabilize keratin dimers/tetramers, whereas the latter likely interferes with higher-order keratin filament formation"* ([PMID: 34116063](https://pubmed.ncbi.nlm.nih.gov/34116063/)). Specific KRT17 alleles further modify phenotype; e.g., KRT17 p.L99P is associated with increased fingernail involvement and 20-nail dystrophy, whereas p.N92S trends milder ([PMID: 33486795](https://pubmed.ncbi.nlm.nih.gov/33486795/)). This explains why cysts are the KRT17-signature manifestation and links the Arg94/Asn92 hotspots mechanistically to impaired filament assembly.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous missense mutation** arises in the 1A helix-initiation rod domain of _KRT17_ (hotspots R94C/R94H, N92H/N92S) — germline, inherited autosomal dominant (or de novo). *(Demonstrated by co-segregation studies.)*
2. The mutation **leads to** a single amino-acid substitution at a conserved residue critical for coiled-coil dimer formation. *(Demonstrated.)*
3. The altered residue **disrupts** hydrophobic packing and/or surface-charge interactions needed for keratin heterodimer and tetramer assembly (K17 pairs with a type II partner keratin). *(Inferred from protein-structure modeling, Wu 2021.)*
4. Because the mutant protein is still expressed and incorporated, it **acts in a dominant-negative fashion**, poisoning the intermediate-filament network assembled from both wild-type and mutant subunits. *(Inferred from the keratinopathy paradigm; directly demonstrated for homologous keratins via aggregation-reversal siRNA experiments.)*
5. Defective assembly **results in** cytoplasmic keratin aggregation and mechanical/stress fragility specifically in **K17-expressing appendageal epithelia** (sebaceous duct, hair follicle, nail bed). *(Inferred; aggregation demonstrated in homologous K6a system.)*
6. In the **sebaceous follicle/duct**, compromised epithelial integrity and abnormal keratinization **malform the sebaceous duct**, which **branches** toward: (a) **sebum retention** within a closed, agranular squamous-lined cyst → the steatocystoma lesion; and (b) **impaired appendageal homeostasis** manifesting (variably) as nail dystrophy, follicular hyperkeratosis, and natal teeth on the PC spectrum. *(Lesion histology demonstrated; branch to PC features demonstrated in allelic patients.)*
7. Androgenic activation of sebaceous glands around **puberty leads to** clinical emergence of multiple cysts (explaining the early-twenties onset). *(Inferred from onset timing and sebaceous-gland biology.)*
8. Secondary events — rupture, bacterial infection, inflammation — **result in** the suppurative variant (SMS), scarring, and occasional overlap with hidradenitis suppurativa. *(Demonstrated clinically.)*

```
KRT17 1A-domain missense (R94C/H, N92H/S)
        │  destabilizes coiled-coil
        ▼
Impaired keratin dimer/tetramer assembly ──(dominant-negative)──► cytoplasmic keratin aggregation
        │
        ▼
Appendageal epithelial fragility (sebaceous duct, hair follicle, nail bed)
        │
        ├──► sebaceous-duct malformation ──► sebum retention ──► STEATOCYSTOMA (cysts)
        │                                   (+ puberty/androgen trigger)
        └──► nail dystrophy / natal teeth / follicular hyperkeratosis (PC-2 spectrum branch)
                                   │
                                   └──► rupture/infection ──► suppurative variant (SMS), scarring
```

### Upstream vs downstream

| Level | Element | Evidence type |
|-------|---------|---------------|
| Upstream (initiating) | KRT17 1A-domain missense mutation (R94, N92) | Human genetic (co-segregation) |
| Molecular | Loss of dimer/tetramer stability; dominant-negative filament poisoning | Structural modeling + keratinopathy paradigm |
| Cellular | Keratin aggregation, appendageal epithelial fragility | In vitro (homologous keratins) |
| Tissue | Sebaceous-duct malformation, sebum retention cyst | Human histopathology |
| Clinical (downstream) | Multiple cysts; variable nail/tooth features; suppuration | Human clinical |

### Ontology term suggestions

- **Gene/protein:** KRT17 (HGNC:6427); GO:0045095 keratin filament; GO:0005882 intermediate filament; GO:0030280 structural constituent of skin epidermis; GO:0008544 epidermis development; GO:0045109 intermediate filament organization.
- **Cell types (CL):** CL:0000312 keratinocyte; CL:0002190 sebaceous gland cell (sebocyte); CL:0002559 hair follicle cell.
- **Anatomy (UBERON):** UBERON:0002073 hair follicle; UBERON:0001821 sebaceous gland; UBERON:0002067 dermis; UBERON:0001003 skin epidermis; UBERON:0000014 zone of skin (trunk/axilla/groin).
- **Phenotype (HPO):** HP:0032320 cutaneous cyst/steatocystoma; HP:0200039 papule; HP:0001596 alopecia (K17 biology); HP:0008069 natal tooth; HP:0008404 nail dystrophy.
- **Disease (MONDO):** MONDO:0008485 steatocystoma multiplex.
- **Chemical (CHEBI):** CHEBI:6716 isotretinoin (treatment); sebum constituents (triglycerides, squalene, wax esters).
- **Treatment (NCIT):** surgical excision; isotretinoin therapy; cryosurgery; laser therapy.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|------|------------------|---------------|----------|
| [9008238](https://pubmed.ncbi.nlm.nih.gov/9008238/) | K17 missense mutations → PC-2 or SM-like phenotype | Human genetic | F1 — N92H/R94H in SM families |
| [9767294](https://pubmed.ncbi.nlm.nih.gov/9767294/) | K17 mutations cause SM or PC-2 | Human genetic | F1, F2 — R94C/N92S; allelism; mutation-independent phenotype |
| [26165312](https://pubmed.ncbi.nlm.nih.gov/26165312/) | R94C in SM | Human genetic | F1 — co-segregation in 4-gen pedigree |
| [35676340](https://pubmed.ncbi.nlm.nih.gov/35676340/) | Recessive atypical PC (KRT17 R94H) | Human genetic | F2 — dominant vs recessive KRT17 spectrum |
| [16702408](https://pubmed.ncbi.nlm.nih.gov/16702408/) | K17 modulates hair cycling (TNFα) | Mouse model | F3 — K17 appendageal biology |
| [33008845](https://pubmed.ncbi.nlm.nih.gov/33008845/) | K17 regulates nuclear morphology/chromatin | In vitro | F3 — non-structural K17 functions |
| [41880216](https://pubmed.ncbi.nlm.nih.gov/41880216/) | K17 in Rac1-mediated DDR | In vitro | F3 — K17 stress response |
| [41363957](https://pubmed.ncbi.nlm.nih.gov/41363957/) | Steatocystomas: update | Clinical review | F4 — core lesion definition |
| [33088817](https://pubmed.ncbi.nlm.nih.gov/33088817/) | SM case (anti-IL-12/23) | Human clinical | F4 — distribution/asymptomatic |
| [29998099](https://pubmed.ncbi.nlm.nih.gov/29998099/) | Facial SM clinicopathology | Human clinical | F4 — histopathology |
| [42518883](https://pubmed.ncbi.nlm.nih.gov/42518883/) | Epidemiology systematic review | Aggregated (145 cases) | F5 — onset, familial, hotspot |
| [21430705](https://pubmed.ncbi.nlm.nih.gov/21430705/) | PC molecular genetics | Review/registry | F6 — dominant-negative keratin class |
| [18495438](https://pubmed.ncbi.nlm.nih.gov/18495438/) | Therapeutic siRNA for PC | In vitro | F6 — aggregation reversal |
| [19935778](https://pubmed.ncbi.nlm.nih.gov/19935778/) | First-in-human siRNA trial | Clinical trial (Ib) | F6 — allele-specific siRNA validated |
| [26264709](https://pubmed.ncbi.nlm.nih.gov/26264709/) | Allele-specific RNAi review | Review | F6 — single-nucleotide discrimination |
| [22264670](https://pubmed.ncbi.nlm.nih.gov/22264670/) | 254 PC patients phenotype | Human cohort | F7 — cysts/natal teeth ↔ KRT17 |
| [34116063](https://pubmed.ncbi.nlm.nih.gov/34116063/) | Genotype–structurotype–phenotype | Human + modeling | F7 — structural mechanism |
| [33486795](https://pubmed.ncbi.nlm.nih.gov/33486795/) | Predictive genetic variants in PC | Human cohort | F7 — allele-specific modifiers |

**Supporting context papers:** K17 in disease pathogenesis (psoriasis to dermatoses) ([PMID: 30306595](https://pubmed.ncbi.nlm.nih.gov/30306595/)); PC-associated PPK pathophysiology and Keap1-Nrf2 ([PMID: 31021398](https://pubmed.ncbi.nlm.nih.gov/31021398/)); PC clinical features and future treatments ([PMID: 37766547](https://pubmed.ncbi.nlm.nih.gov/37766547/)); molecular clinical endpoints for siRNA trials ([PMID: 21191405](https://pubmed.ncbi.nlm.nih.gov/21191405/)); treatment case reports — isotretinoin + cryotherapy for SMS ([PMID: 10812703](https://pubmed.ncbi.nlm.nih.gov/10812703/)), combination laser therapy ([PMID: 22487444](https://pubmed.ncbi.nlm.nih.gov/22487444/)), SMS review ([PMID: 41736170](https://pubmed.ncbi.nlm.nih.gov/41736170/)), hybrid SM/EVHC cyst ([PMID: 40998547](https://pubmed.ncbi.nlm.nih.gov/40998547/)).

---

## Report by Template Section

### 1. Disease Information
Steatocystoma multiplex is a rare, benign, autosomal dominant genodermatosis of the pilosebaceous unit, characterized by multiple sebum-filled dermal cysts. **Identifiers:** MONDO:0008485; OMIM 184500; causal gene _KRT17_ (HGNC:6427; NCBI Gene 3872); Orphanet (steatocystoma multiplex); ICD-10 L72.2 (steatocystoma multiplex); MeSH "Steatocystoma Multiplex." **Synonyms:** sebocystomatosis; steatocystoma multiplex (familial). Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, systematic review) and from individual case reports/pedigrees rather than EHR-scale cohorts.

### 2. Etiology
**Primary cause: genetic** — heterozygous missense mutations in the 1A domain of _KRT17_ (dominant-negative). **Genetic risk:** causal hotspot variants at Arg94 (R94C, R94H) and Asn92 (N92H, N92S); a positive family history is the dominant risk factor (familial cases ~26%). **Environmental/hormonal:** androgen-driven sebaceous activation at puberty is the main modulator of lesion emergence; no toxins, infections, or occupational exposures are established as causal. **Protective factors:** none genetically or environmentally established. **Gene–environment interaction:** the mutation-independent SM-versus-PC2 phenotype (identical R94C → different disease) implies modifier genes and/or hormonal/environmental context determine phenotypic expression ([PMID: 9767294](https://pubmed.ncbi.nlm.nih.gov/9767294/)).

### 3. Phenotypes
- **Multiple cutaneous cysts** (physical manifestation): firm, non-tender, skin-colored to yellowish dermal papules/nodules; onset adolescence/early adulthood (median 23 y); slow/chronic progression; defining, near-universal feature. HPO: HP:0032320 (cutaneous cyst/steatocystoma); HP:0200039 (papule).
- **Sebum discharge** on puncture (clinical sign).
- **Suppuration/secondary infection** (SMS variant): episodic inflammation, pain, scarring; higher in familial cases.
- **Nail dystrophy** (variable; PC spectrum overlap): HP:0008404.
- **Natal teeth / dental anomalies** (variable, KRT17-associated): HP:0008069.
- **Quality-of-life impact:** usually asymptomatic but can be *"significantly disfiguring"* ([PMID: 31915618](https://pubmed.ncbi.nlm.nih.gov/31915618/)); psychosocial burden, particularly with facial/extensive involvement; coil-1A mutation carriers report more emotional issues (Wu 2021). Does not affect lifespan.

### 4. Genetic / Molecular Information
**Causal gene:** _KRT17_ (gene OMIM 148069), type I intermediate filament, chromosome 17q21.2. **Pathogenic variants:** missense substitutions in the 1A helix-initiation motif — R94C (c.280C>T), R94H, N92H, N92S; classified pathogenic/likely pathogenic by co-segregation and recurrence. **Allele frequency:** absent/extremely rare in population databases (gnomAD), consistent with high-penetrance dominant disease. **Origin:** germline. **Functional consequence:** dominant-negative (not simple loss of function) — mutant subunit impairs filament assembly ([PMID: 34116063](https://pubmed.ncbi.nlm.nih.gov/34116063/)). **Modifier genes:** unidentified but inferred from mutation-independent SM/PC2 divergence and allele-specific nail severity (e.g., KRT17 L99P) ([PMID: 33486795](https://pubmed.ncbi.nlm.nih.gov/33486795/)). **Epigenetics / chromosomal abnormalities:** none established for SM.

### 5. Environmental Information
No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents are established as causes. Hormonal (androgenic) drive at puberty modulates expression. Secondary bacterial infection contributes to the suppurative variant but is a downstream complication, not a cause.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. In brief: KRT17 1A-domain mutation → destabilized keratin dimer/tetramer assembly → dominant-negative filament poisoning and cytoplasmic aggregation in K17-expressing appendageal epithelia → sebaceous-duct malformation → sebum-retention cysts, with a branch to variable nail/tooth features on the PC spectrum and a secondary branch to suppuration/scarring. No single canonical signaling pathway (Wnt/MAPK/mTOR) is causal; relevant K17-linked signaling includes TNFα/NF-κB (hair cycling) and Keap1-Nrf2/oxidative-stress responses described in the broader PC literature.

### 7. Anatomical Structures Affected
**Primary organ:** skin (integumentary system). **Specific sites:** pilosebaceous unit — sebaceous gland/duct (UBERON:0001821), hair follicle (UBERON:0002073), within the dermis (UBERON:0002067). **Distribution:** trunk, axillae, groin, limbs (occasionally face/scalp; rare acral subcutaneous variant). **Tissue type:** epithelial (stratified squamous, agranular cyst lining). **Cells:** sebocytes (CL:0002190), keratinocytes (CL:0000312). **Subcellular:** cytoplasmic intermediate-filament/keratin network (GO:0045095 keratin filament; GO:0005856 cytoskeleton). **Lateralization:** bilateral/generalized, non-lateralized.

### 8. Temporal Development
**Onset:** typically peri-/post-pubertal; median onset 23 years (familial 13.5 y, sporadic 30.0 y) ([PMID: 42518883](https://pubmed.ncbi.nlm.nih.gov/42518883/)). **Pattern:** insidious, chronic. **Progression:** slow accumulation of lesions; stable-to-progressive; lifelong. Suppurative variant is episodic/relapsing. **Remission:** no spontaneous resolution; individual lesions can be cleared by procedures. **Critical window:** puberty (androgen-driven sebaceous activation) marks clinical emergence.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant (rare homozygous KRT17 → recessive atypical PC, [PMID: 35676340](https://pubmed.ncbi.nlm.nih.gov/35676340/)). **Penetrance:** high, with variable expressivity. **Prevalence:** rare; no precise figure; no clear geographic/ethnic predilection ([PMID: 42518883](https://pubmed.ncbi.nlm.nih.gov/42518883/)). **Sex ratio:** roughly equal overall; HS co-occurrence female-predominant (12.5% vs 1.5%, P=0.019). **Familial fraction:** ~26.2% of reported cases; remainder sporadic (de novo or under-ascertained). **Anticipation / founder effects / consanguinity:** not established (recurrent R94 reflects a mutational hotspot, not a founder haplotype).

### 10. Diagnostics
**Clinical:** recognition of multiple characteristic cysts; puncture reveals oily/sebum material. **Histopathology (gold standard):** dermal cyst with agranular stratified squamous lining, eosinophilic corrugated cuticle, and sebaceous lobules in the wall ([PMID: 29998099](https://pubmed.ncbi.nlm.nih.gov/29998099/)). **Dermoscopy:** yellow homogeneous background with peripheral linear vessels. **Genetic testing:** single-gene KRT17 sequencing (exon 1 / 1A domain) or keratin/PC gene panel confirms diagnosis and distinguishes mimics; WES/WGS useful in atypical cases. **Differential diagnosis:** eruptive vellus hair cysts (can co-occur/form hybrid cysts, [PMID: 40998547](https://pubmed.ncbi.nlm.nih.gov/40998547/)), epidermoid cysts, milia, hidradenitis suppurativa (for SMS), trichofolliculoma. No specific blood biomarker or imaging test.

### 11. Outcome / Prognosis
**Benign; no malignant potential; normal life expectancy.** Morbidity is cosmetic and psychosocial; the suppurative variant causes pain, recurrent infection, and scarring. Lesions are chronic and do not spontaneously remit. Prognostic factors for severity include familial disease and early onset (associated with infected lesions and nail dystrophy). No disease-specific mortality.

### 12. Treatment
No cure; symptom-directed. **Pharmacotherapy:** oral isotretinoin (CHEBI:6716; reduces sebaceous activity/inflammation, especially for SMS — [PMID: 10812703](https://pubmed.ncbi.nlm.nih.gov/10812703/)); antibiotics for secondary infection; biologics (anti-TNF, anti-IL-12/23, anti-IL-17) reported for suppurative/HS-overlap disease ([PMID: 41736170](https://pubmed.ncbi.nlm.nih.gov/41736170/)). **Procedural:** surgical excision (most definitive for isolated lesions), incision/drainage, mini-incision extraction, cryotherapy, and laser (1450-nm diode targeting sebaceous glands + 1550-nm fractional erbium targeting cysts — [PMID: 22487444](https://pubmed.ncbi.nlm.nih.gov/22487444/)). **Emerging/experimental:** mutation-targeted **allele-specific siRNA** (paradigm validated in PC: TD101 — [PMID: 19935778](https://pubmed.ncbi.nlm.nih.gov/19935778/)); no SM-specific approved targeted therapy yet. NCIT terms: surgical excision, isotretinoin therapy, cryosurgery, laser therapy.

### 13. Prevention
No primary prevention (genetic etiology). **Secondary/tertiary:** early recognition to shorten the ~8-year diagnostic delay; treatment of individual lesions and prompt management of suppuration to prevent scarring. **Genetic counseling:** autosomal dominant → 50% transmission risk; offer KRT17 testing and family counseling; prenatal/preimplantation testing is technically feasible but rarely pursued given the benign, non-lethal nature. No vaccine or public-health intervention applicable.

### 14. Other Species / Natural Disease
Human disease (NCBI Taxon 9606). Orthologous gene _Krt17_ exists in mouse (NCBI Gene 16667) and other mammals. **Krt17-null mice** develop alopecia and hair-shaft fragility ([PMID: 16702408](https://pubmed.ncbi.nlm.nih.gov/16702408/)), modeling appendageal K17 function but **not** the human cystic phenotype (null vs dominant-negative). No naturally occurring SM-equivalent disease is documented in companion animals or wildlife (OMIA); no zoonotic relevance.

### 15. Model Organisms
**Mouse:** Krt17 knockout (alopecia/hair-cycle phenotype) recapitulates appendageal dependence on K17 but not cysts; the dominant-negative human mechanism is not reproduced by a null allele. A dominant-negative R94 knock-in would be the ideal, currently unavailable, model. **In vitro:** patient-derived keratinocytes and transfected cell systems demonstrate keratin aggregation (shown for homologous keratins). **iPSC/organoid** sebaceous or skin-appendage models are plausible future systems. Resources: MGI (Krt17), IMPC/IMSR. **Limitations:** no model fully recapitulates the human sebaceous-duct cyst; most mechanistic inference is extrapolated from homologous PC keratins (K6a/K16) and structural modeling.

---

## Limitations and Knowledge Gaps

1. **No dominant-negative animal model of SM.** Available mouse data come from Krt17-null (loss-of-function) animals, which model K17's role in hair cycling but not the human dominant-negative cystogenesis; the sebaceous-duct cyst phenotype has not been recapitulated in vivo.
2. **Mechanism partly inferred by homology.** Direct demonstration of mutant K17 aggregation and filament poisoning for the specific SM hotspot alleles is limited; aggregation-reversal and allele-specific-siRNA evidence derives from homologous keratins (K6a) in PC.
3. **Modifier genes unidentified.** The mutation-independent SM-versus-PC2 divergence strongly implies genetic/environmental modifiers, but none are molecularly identified.
4. **Epidemiology is case-report-based.** Even the systematic review aggregates only 145 cases; true prevalence/incidence, penetrance estimates, and population-level data are lacking, with likely publication/ascertainment bias toward severe and familial cases.
5. **No controlled treatment trials.** Therapeutic evidence is case reports/series; no randomized data exist for isotretinoin, laser, or biologics in SM, and allele-specific siRNA has not been tested in SM specifically.
6. **Androgen/puberty link is inferential.** The onset timing suggests hormonal modulation, but direct mechanistic data in SM are absent.

## Proposed Follow-up Experiments / Actions

1. **Generate a Krt17 R94C/H knock-in mouse** (dominant-negative) and characterize sebaceous-duct architecture, cyst formation, and androgen responsiveness to create the first faithful SM model.
2. **Patient-derived sebocyte/skin organoids or iPSC appendage models** carrying SM hotspot alleles to test keratin aggregation and filament assembly directly in the relevant cell type.
3. **Allele-specific siRNA/ASO against KRT17 R94C** — design and validate single-nucleotide-discriminating knockdown in patient keratinocytes/sebocytes, then intralesional proof-of-concept, mirroring the TD101 PC paradigm.
4. **Modifier-gene discovery** via whole-genome sequencing and phenotype association in SM-versus-PC2 families sharing identical KRT17 alleles.
5. **Prospective natural-history registry** to establish penetrance, prevalence, sex ratio, QoL metrics (DLQI/SF-36), and standardized severity scoring — reducing reliance on case reports.
6. **Structural/biophysical validation** (cryo-EM, in vitro filament-assembly assays) of how R94 and N92 substitutions specifically destabilize K17 dimer/tetramer formation.
7. **Clinical trial design** for isotretinoin dosing and laser combinations (1450-nm + 1550-nm) with objective lesion-count endpoints.

---

## Consensus Answer

Steatocystoma multiplex (MONDO:0008485; OMIM 184500) is an autosomal dominant benign genodermatosis caused by heterozygous missense mutations in the 1A helix-initiation rod domain of **KRT17 (keratin 17)**, with Arg94 and Asn92 as recurrent hotspots. These mutations act by a dominant-negative mechanism—destabilizing keratin dimer/tetramer assembly and causing cytoplasmic keratin aggregation—that malforms the sebaceous-follicle duct and produces multiple sebum-retention cysts, typically emerging in the early-to-mid twenties. SM is allelic with pachyonychia congenita type 2 on a single KRT17 phenotypic spectrum (cysts being the KRT17 signature); it does not affect lifespan, and management is symptomatic (excision, drainage, isotretinoin, laser, biologics for the suppurative variant), with allele-specific siRNA as a rational emerging mechanism-targeted therapy.


## Artifacts

- [OpenScientist final report](Steatocystoma_Multiplex-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Steatocystoma_Multiplex-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032320` (2 mentions) - the report calls it "cutaneous cyst/steatocystoma"; HP calls it **Affected**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0200039` (2 mentions) - the report calls it "papule"; HP calls it **Pustule**, and lists "Pimple" among its other names