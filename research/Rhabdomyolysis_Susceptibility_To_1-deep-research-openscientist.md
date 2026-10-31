---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T18:03:41.717687'
end_time: '2026-10-27T18:22:33.322263'
duration_seconds: 1131.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Rhabdomyolysis Susceptibility To 1
  mondo_id: MONDO:0859371
  category: Mendelian
  causal_genes: OBSCN
  omim_id: OMIM:620235
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 25
  on_topic: 11
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 9
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0859371
    reported_labels:
    - MONDO
    ontology_label: rhabdomyolysis, susceptibility to, 1
  - term_id: HP:0000083
    reported_labels:
    - Renal insufficiency
    - myoglobinuric AKI
    ontology_label: Renal insufficiency
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rhabdomyolysis_Susceptibility_To_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rhabdomyolysis_Susceptibility_To_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rhabdomyolysis Susceptibility To 1
- **MONDO ID:** MONDO:0859371 (if available)
- **Causal gene(s):** OBSCN
- **OMIM:** OMIM:620235
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Rhabdomyolysis Susceptibility To 1** covering all of the
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

# Rhabdomyolysis, Susceptibility To, 1 (RHABDO1) — Comprehensive Disease Report

**Disease:** Rhabdomyolysis, Susceptibility To, 1 (RHABDO1)
**MONDO ID:** MONDO:0859371 · **OMIM:** 620235 · **Causal gene:** **OBSCN** (obscurin; HGNC:16542; UniProt Q5VST9; chromosome 1q42)
**Category:** Mendelian (autosomal recessive)

> **Gene identity (stated up front):** The causal gene for Rhabdomyolysis Susceptibility To 1 is **OBSCN**, which encodes **obscurin**, a giant (~800 kDa) sarcomeric cytoskeletal/signaling protein. This report concerns the OBSCN-related entity (OMIM 620235), not rhabdomyolysis caused by other genes (e.g., RYR1, LPIN1, CPT2, PYGM, ANO5, fatty-acid-oxidation genes).

---

## Summary

**Rhabdomyolysis, Susceptibility To, 1 (RHABDO1)** is a rare Mendelian skeletal-muscle disorder caused by **bi-allelic loss-of-function (LOF) variants in OBSCN**, the gene encoding **obscurin** — a giant (~800 kDa) modular sarcomeric signaling and structural protein that physically links the contractile sarcomere (at the M-band and Z-disk) to the sarcoplasmic reticulum (SR). The disease was defined by Cabrera-Serrano and colleagues (*Brain*, 2022), who identified 10 bi-allelic LOF OBSCN variants in six unrelated patients with severe, recurrent exertional rhabdomyolysis and demonstrated reduced OBSCN expression and loss of obscurin protein in patient muscle ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)). This case series established OMIM 620235.

The core clinical picture is **teenage-onset, recurrent, severe rhabdomyolysis** precipitated by metabolic or mechanical triggers (strenuous exercise, fasting, febrile illness), accompanied by myalgia, muscle cramps, exercise intolerance, markedly elevated serum creatine kinase (CK), and myoglobinuria that risks acute kidney injury (AKI). A distinguishing feature is **cardiac sparing** — despite prior literature linking OBSCN to cardiomyopathy, RHABDO1 patients consistently lack cardiomyopathy and have normal cardiac examinations. The mechanistic model, supported by patient myoblast studies and mouse *Obscn/Obsl1* models, is that obscurin loss **disorganizes the SR and impairs Ca²⁺ re-uptake/storage**, sensitizing myofibers to metabolic and mechanical stress and precipitating episodic myofiber breakdown.

Genetically, OBSCN is **not constrained against heterozygous LOF** in gnomAD (pLI ≈ 0, LOEUF ≈ 0.94), consistent with recessive inheritance in which a single LOF allele is tolerated. In ClinVar, truncating OBSCN variants (nonsense/frameshift) associated with rhabdomyolysis are classified Pathogenic/Likely-pathogenic, whereas missense variants are predominantly Variants of Uncertain Significance (VUS). There is **no gene-specific therapy**; management is supportive (aggressive IV fluid resuscitation, electrolyte and renal monitoring during crises) combined with **trigger avoidance** and **genetic counseling**. This report synthesizes evidence across the defining human case series, three additional case reports, gnomAD constraint data, ClinVar classifications, UniProt domain architecture, Monarch/HPO phenotype annotations, and mouse models.

---

## Section 1 — Disease Information

**Overview.** RHABDO1 is an autosomal-recessive susceptibility to recurrent rhabdomyolysis — acute skeletal-muscle fiber breakdown with release of intracellular contents (CK, myoglobin, electrolytes) into the circulation. Affected individuals are often asymptomatic or only mildly symptomatic between episodes but develop severe crises when exposed to triggers. The condition is a **genetic susceptibility** rather than a continuously progressive myopathy: episodes are **trigger-dependent and episodic**, with normal or near-normal muscle strength between attacks in most patients.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 620235 (Rhabdomyolysis, susceptibility to, 1) |
| MONDO | MONDO:0859371 |
| Causal gene | OBSCN (HGNC:16542; NCBI Gene; Ensembl ENSG00000154358) |
| Protein | Obscurin, UniProt Q5VST9 |
| Cytoband | 1q42 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No dedicated RHABDO1-specific code identified; rhabdomyolysis maps to ICD-10 **M62.82** and MeSH **D012206 (Rhabdomyolysis)** |

**Synonyms / alternative names.** No formal synonyms are recorded in the template. The condition is referred to descriptively in the literature as "OBSCN-related rhabdomyolysis," "obscurin-deficiency rhabdomyolysis," and "bi-allelic OBSCN loss-of-function rhabdomyolysis."

**Information source.** The knowledge base here is derived from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD, HPO/Monarch, UniProt) and **individual patient case reports/series** in the primary literature — not from a large EHR cohort. The total reported patient count worldwide is small (roughly a dozen across the defining series and subsequent case reports).

---

## Section 2 — Etiology

**Disease causal factors.** The primary cause is **genetic**: bi-allelic (homozygous or compound-heterozygous) loss-of-function variants in OBSCN. The defining study identified 10 bi-allelic LOF OBSCN variants across six unrelated patients ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)). Disease expression, however, is **gene–environment dependent**: the genetic lesion establishes susceptibility, while an environmental/metabolic **trigger** (exertion, fasting, fever/infection) precipitates each acute episode.

**Genetic risk factors.** The causal variants are LOF alleles in OBSCN (nonsense, frameshift, canonical splice-site). Because OBSCN tolerates heterozygous LOF (gnomAD pLI ≈ 0), **two defective alleles are required** for disease. No established modifier genes are proven for RHABDO1 specifically, though the paralogue OBSL1 (obscurin-like 1) provides functional redundancy in muscle (relevant to mechanism; see Section 6).

**Environmental risk factors / triggers.** Based on the clinical descriptions: **strenuous or unaccustomed exercise**, **fasting/caloric deprivation**, **febrile illness/infection**, and likely **dehydration and heat stress** (the classic precipitants of exertional rhabdomyolysis generally). Patient myoblasts were shown to be more susceptible to **starvation** specifically ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)), providing a direct link between a metabolic trigger and cellular vulnerability.

**Protective factors.** No validated genetic protective variants or protective alleles are reported. By inference, **avoidance of triggers** (adequate hydration, avoiding prolonged fasting, graded rather than sudden intense exercise, prompt management of febrile illness) is protective against episodes. No nutritional or pharmacologic protective factor has been established.

**Gene–environment interactions.** RHABDO1 is a prototypical **gene × environment** disorder: the OBSCN LOF genotype lowers the threshold at which metabolic/mechanical stress triggers Ca²⁺ dysregulation and myofiber breakdown. The starvation-sensitivity of patient myoblasts is the best-characterized GxE link ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)).

---

## Section 3 — Phenotypes

The official Monarch/HPO disease–phenotype annotation set for MONDO:0859371 comprises **10 terms**, spanning episodic clinical features, laboratory abnormalities, and muscle-biopsy histopathology.

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Elevated circulating creatine kinase | HP:0003236 | Laboratory abnormality | Markedly elevated during episodes (CK can reach hundreds of thousands U/L in rhabdomyolysis) |
| Rhabdomyolysis | HP:0003201 | Clinical sign | Core defining feature; recurrent/episodic |
| Myalgia | HP:0003326 | Symptom | Muscle pain, often with cramps |
| Exercise intolerance | HP:0003546 | Symptom | Common trigger-associated complaint |
| Renal insufficiency | HP:0000083 | Laboratory/clinical | Secondary to myoglobinuria (AKI risk) |
| Increased variability in muscle fiber diameter | HP:0003557 | Histopathology | Muscle-biopsy finding |
| Centrally nucleated skeletal muscle fibers | HP:0003687 | Histopathology | Muscle-biopsy finding |
| Type 2 muscle fiber predominance | HP:0010602 | Histopathology | Muscle-biopsy finding |
| Distal muscle weakness | HP:0002460 | Clinical sign | Variable; not universal |
| Abnormal circulating fatty acylcarnitine concentration | HP:0012071 | Laboratory abnormality | Metabolic workup finding |

**Phenotype characteristics.**
- **Age of onset:** typically **teenage years** (adolescence), as described in the defining series — "usually with onset in the teenage years" ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)). Subsequent reports describe young adults/young patients.
- **Severity:** **severe and recurrent** episodes of rhabdomyolysis; variable between episodes and between individuals (variable expressivity).
- **Progression:** **episodic/relapsing**, trigger-dependent; not a steadily progressive degenerative myopathy. Patients are often well between episodes.
- **Frequency among affected individuals:** myalgia, muscle cramps, exercise intolerance and elevated CK are consistent features; cardiomyopathy is **characteristically absent**.

**Cardiac sparing.** Multiple reports emphasize **no cardiomyopathy**: the defining series found no cardiomyopathy despite prior OBSCN–cardiomyopathy associations and normal cardiac exams ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)); Zemorshidi et al. described two young patients "without any evidence of concomitant cardiomyopathy" ([PMID: 38159459](https://pubmed.ncbi.nlm.nih.gov/38159459/)); Sun et al. reported edema on MRI "without significant muscle weakness or cardiac abnormalities" ([PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36/PROMIS data exist for RHABDO1. By inference, QoL impact derives from recurrent painful episodes, hospitalizations for crises, exercise limitation, and anxiety about triggers; between episodes, function is often preserved.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** OBSCN (obscurin), HGNC:16542, chromosome **1q42**; Ensembl ENSG00000154358. OBSCN has **121 non-overlapping exons** and encodes **some of the largest known mRNAs in the human genome**, undergoing extensive developmentally- and tissue-regulated alternative splicing ([PMID: 40025502](https://pubmed.ncbi.nlm.nih.gov/40025502/)). The same gene underlies both a cardiomyopathy disease axis and the rhabdomyolysis axis, with isoform- and domain-specific effects.

**Pathogenic variants (RHABDO1-associated).** Pathogenic/likely-pathogenic variants are **loss-of-function** (nonsense, frameshift, canonical splice). Representative ClinVar entries (transcript NM_001386125.1), classified Pathogenic (P) or Likely-pathogenic (LP):

| cDNA | Protein | Type | ClinVar class |
|---|---|---|---|
| c.20788C>T | p.Gln6930Ter | Nonsense | Pathogenic |
| c.7485_7486insCCCGCCC | p.Thr2496fs | Frameshift | Pathogenic |
| c.5943C>A | p.Cys1981Ter | Nonsense | Likely pathogenic |
| c.25879_25880del | p.Lys8627fs | Frameshift | Likely pathogenic |
| c.20292C>G | p.Tyr6764Ter | Nonsense | Likely pathogenic |
| c.23841dup | p.Gly7948fs | Frameshift | Likely pathogenic |
| c.19607C>A | p.Ser6536Ter | Nonsense | Likely pathogenic |
| c.15307C>T | p.Gln5103Ter | Nonsense | Likely pathogenic |
| c.12859C>T | p.Gln4287Ter | Nonsense | Likely pathogenic |

Additional genotypes from case reports: compound heterozygous **c.21184C>T (nonsense)** + **c.15610+12C>T (intronic splicing; absent from gnomAD_EAS)** ([PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)); novel variants **c.24822C>A** and **c.2653+1G>C** ([PMID: 38159459](https://pubmed.ncbi.nlm.nih.gov/38159459/)); and **c.20292C>A** + **c.708del** ([PMID: 40813169](https://pubmed.ncbi.nlm.nih.gov/40813169/)).

**Variant classification caveat.** Missense, synonymous, and splice-region changes in the same rhabdomyolysis-annotated ClinVar set are **largely VUS** (e.g., p.Arg7149Pro, p.Val6753Leu, p.Trp1659Cys). This is reinforced by functional work showing that two cardiomyopathy-associated obscurin missense variants (R4344Q, R4444W) did **not** alter titin binding or domain thermostability and that R4344Q is present in **15% of African Americans**, arguing against pathogenicity — a cautionary tale for over-calling OBSCN missense variants ([PMID: 33438037](https://pubmed.ncbi.nlm.nih.gov/33438037/)). OBSCN has ~150 total P/LP ClinVar entries across all phenotypes.

**Allele frequency / population constraint.** gnomAD v2.1.1 constraint for OBSCN: **pLI = 7.4×10⁻²²⁶ (≈ 0)**, observed/expected LOF (oe_lof) = 0.88 (90% CI 0.83–0.94; **LOEUF 0.94**), with 768 observed vs 870.9 expected LOF alleles; missense constraint low (mis_z = 0.53, oe_mis = 0.99). **Interpretation:** OBSCN is not depleted of heterozygous LOF variants, consistent with recessive inheritance where carriers are unaffected.

**Somatic vs germline.** All reported variants are **germline**. No somatic involvement is relevant to this disorder.

**Functional consequences.** **Loss of function** — reduced OBSCN expression and loss of obscurin protein in patient muscle ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)). This contrasts with proposed gain-of-function/dominant-negative mechanisms sometimes invoked for OBSCN cardiomyopathy variants.

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes, epigenetic marks, or large-scale chromosomal abnormalities are described specifically for RHABDO1. OBSL1 redundancy is mechanistically relevant (Section 6). Alternative splicing of OBSCN may be regulated in part by **BUB3** ([PMID: 40025502](https://pubmed.ncbi.nlm.nih.gov/40025502/)).

---

## Section 5 — Environmental Information

**Environmental / triggering factors.** The disease requires an environmental trigger to produce episodes. Established/implicated precipitants: **strenuous or unaccustomed physical exertion**, **fasting/starvation**, **febrile illness**, and plausibly **dehydration and heat**. Patient myoblasts are specifically more susceptible to **starvation** ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)).

**Lifestyle factors.** Exercise intensity and pattern, hydration status, and fasting behavior modulate risk. There is no reported association with smoking, alcohol, or diet beyond the fasting trigger.

**Infectious agents.** No pathogen causes RHABDO1. However, **febrile infections act as triggers** of acute episodes — a general feature of metabolic/genetic rhabdomyolysis susceptibilities. (For context, infections such as SARS-CoV-2 can independently cause rhabdomyolysis, [PMID: 34871534](https://pubmed.ncbi.nlm.nih.gov/34871534/), but this is etiologically distinct from the OBSCN genetic susceptibility.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Bi-allelic LOF variant in OBSCN** (nonsense/frameshift/splice) → **loss of obscurin protein** in skeletal myofibers (*demonstrated*: reduced OBSCN expression and absent obscurin in patient muscle, [PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)).
2. Loss of obscurin **removes the structural/signaling link between the sarcomere (M-band/Z-disk) and the SR** → **disorganization of the SR** and loss of normal SR architecture (*demonstrated in mouse models; inferred in human*: combined loss of Obscn/Obsl1 disrupts SR organization, [PMID: 31098411](https://pubmed.ncbi.nlm.nih.gov/31098411/)).
3. SR disorganization + reduced SERCA/phospholamban expression → **impaired Ca²⁺ re-uptake and reduced SR Ca²⁺ storage** → **perturbed Ca²⁺ cycling** (*demonstrated in mouse*: reduced SR volume, lower SERCA/PLB, altered Ca²⁺ cycling, [PMID: 40366302](https://pubmed.ncbi.nlm.nih.gov/40366302/), [PMID: 40066567](https://pubmed.ncbi.nlm.nih.gov/40066567/)).
4. Under a **metabolic/mechanical trigger** (exercise, fasting, fever) → myofibers with compromised Ca²⁺ handling **cannot buffer the additional stress**; patient myoblasts show a greater drop in SR Ca²⁺ content upon starvation than controls (*demonstrated*, [PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)).
5. **Dysregulated cytosolic Ca²⁺ and sarcolemmal instability** → activation of Ca²⁺-dependent proteases/phospholipases and loss of membrane integrity → **myofiber necrosis / rhabdomyolysis** (*inferred mechanism; sarcolemmal instability demonstrated in Obscn/Obsl1 double-KO mouse*, [PMID: 31098411](https://pubmed.ncbi.nlm.nih.gov/31098411/)).
6. Myofiber breakdown → **release of CK and myoglobin** → markedly elevated serum CK, **myoglobinuria** → **acute kidney injury** when severe (*clinical observation*, [PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/), [PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)).

**Branch (cardiac, largely spared in RHABDO1):** In the heart, obscurin loss produces a **separate disease axis** — reduced SR volume with preserved T-tubules, lower SERCA/PLB, dilated cardiomyopathy and arrhythmia susceptibility in mice ([PMID: 40366302](https://pubmed.ncbi.nlm.nih.gov/40366302/)); domain-specific Ig58/59 deletion causes atrial remodeling and Ca²⁺-based arrhythmogenesis ([PMID: 39804820](https://pubmed.ncbi.nlm.nih.gov/39804820/)). In human RHABDO1, however, the cardiac axis is **not manifest** (cardiac sparing), likely reflecting isoform/redundancy differences between skeletal and cardiac muscle.

### Supporting molecular detail

**Protein architecture (UniProt Q5VST9, canonical 7,968 aa).** Obscurin contains **~55 Ig-like domains**, **4 fibronectin type-III (Fn3) domains**, a **calmodulin-binding IQ motif (aa 4872–4901)**, a tandem **SH3 (5600–5667)–DH (5693–5877)–PH (5895–6004) RhoGEF signaling module**, and **two C-terminal Ser/Thr protein kinase domains** (PK1 6468–6721; PK2 7672–7924). The **N-terminal Ig1–3 domains target obscurin to the M-band/Z-disk** via interactions with titin and myomesin.

**Sarcomere–SR linkage.** Obscurin's N-terminus binds **M-band titin and myomesin**; downregulation of myomesin disrupts obscurin M-band integration ([PMID: 18477606](https://pubmed.ncbi.nlm.nih.gov/18477606/)). Crystallographic work defines the titin M10–obsl1/obscurin Ig–Ig interface and shows that disease-linked titin M10 mutations disrupt this complex ([PMID: 20133654](https://pubmed.ncbi.nlm.nih.gov/20133654/)). Obscurin's C-terminus binds the N-terminal Z-disk region of titin and coassembles during myofibrillogenesis; the protein carries IQ (Ca²⁺/calmodulin) and RhoGEF (G-protein) signaling modules ([PMID: 11448995](https://pubmed.ncbi.nlm.nih.gov/11448995/)). The RhoGEF domain selectively activates **RhoA** at the M-band in skeletal muscle and responds to lengthening-contraction injury ([PMID: 19605563](https://pubmed.ncbi.nlm.nih.gov/19605563/)).

**Functional redundancy with OBSL1.** Single deletion of obscurin or Obsl1 is tolerated in mouse muscle; **only combined deletion** reveals roles in **sarcolemmal stability and SR organization** ([PMID: 31098411](https://pubmed.ncbi.nlm.nih.gov/31098411/)). This redundancy may explain variable expressivity and the relatively mild baseline state between episodes.

**Metabolic / mitochondrial dimension.** Combined Obsc/Obsl1 loss in heart altered metabolism, reduced Chchd3 (a MICOS complex protein), produced abnormal mitophagy and increased unfolded protein response ([PMID: 40066567](https://pubmed.ncbi.nlm.nih.gov/40066567/)). The abnormal acylcarnitine finding (HP:0012071) and starvation-sensitivity in human myoblasts point to an **energy-metabolism vulnerability** that intersects with Ca²⁺ handling.

**Ontology suggestions.**
- **GO biological process:** regulation of release of sequestered calcium ion into cytosol (GO:0051279); sarcomere organization (GO:0045214); muscle contraction (GO:0006936); Rho protein signal transduction (GO:0007266); striated muscle cell development (GO:0055002).
- **GO cellular component:** sarcoplasmic reticulum (GO:0016529); M band (GO:0031430); Z disc (GO:0030018); sarcomere (GO:0030017); sarcolemma (GO:0042383).
- **Cell types (CL):** skeletal muscle fiber / myofiber (CL:0000188); fast muscle cell / type II fiber (CL:0000190).
- **CHEBI:** calcium(2+) (CHEBI:29108); creatine (CHEBI:16919); creatinine (CHEBI:16737).

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary: **skeletal muscle** (striated muscle; UBERON:0001134). Secondary: **kidney** (UBERON:0002113) via myoglobinuric acute kidney injury. Body system: **musculoskeletal/muscular system** primarily; **renal/urinary system** secondarily. The **heart (myocardium, UBERON:0002349)** is characteristically **spared** in RHABDO1.

**Tissue and cell level.** Affected tissue: **skeletal muscle tissue** (UBERON:0002036); affected cells: **skeletal muscle fibers/myofibers** (CL:0000188), with **type 2 fiber predominance** (HP:0010602) on biopsy. Histopathology shows increased fiber-size variability (HP:0003557) and centrally nucleated fibers (HP:0003687).

**Subcellular level.** **Sarcoplasmic reticulum** (GO:0016529) — the key disorganized compartment; **M-band** (GO:0031430) and **Z-disk** (GO:0030018) where obscurin localizes; **sarcolemma** (GO:0042383) instability; **mitochondria** (GO:0005739) secondarily implicated via metabolic/mitophagy changes in models.

**Localization / lateralization.** Skeletal muscle involvement is **generalized/bilateral**; imaging in one case showed **bilateral lower-limb muscle edema** on MRI ([PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)).

---

## Section 8 — Temporal Development

**Onset.** Typically **adolescence (teenage years)** per the defining series ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)); additional cases are young adults. Onset of individual episodes is **acute**, tied to a trigger.

**Progression.** The disease course is **episodic/relapsing** rather than steadily progressive. Between episodes, patients are frequently well, though some show **distal muscle weakness** (HP:0002460) and biopsy changes. Individual rhabdomyolysis episodes evolve acutely (hours), with CK rising rapidly and resolving over days with supportive care.

**Patterns.** Episodes **remit** with trigger removal and supportive treatment. The **critical window** for intervention is during an acute crisis (early aggressive hydration to prevent AKI). Lifelong susceptibility persists; management is about preventing recurrence.

**Expressivity.** Variable: Sun et al. noted the proband's **mother, carrying a homozygous OBSCN variant, had only exercise-induced myalgia**, far milder than the proband's rhabdomyolysis — illustrating variable expressivity ([PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)).

---

## Section 9 — Inheritance and Population

**Inheritance pattern.** **Autosomal recessive** — bi-allelic (homozygous or compound-heterozygous) LOF variants required ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)). Supported by gnomAD constraint showing OBSCN tolerates heterozygous LOF (pLI ≈ 0, LOEUF 0.94), so carriers are generally unaffected.

**Penetrance / expressivity.** Appears **trigger-dependent** with **variable expressivity** (e.g., homozygous carrier mother with only myalgia, [PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)). Penetrance is incompletely defined due to the small number of reported cases.

**Epidemiology.** **Prevalence and incidence are not established** — RHABDO1 is a recently defined (2022), rare Mendelian condition with only ~12 reported patients across the literature. No registry-level prevalence/incidence figures exist.

**Founder effects / consanguinity / carrier frequency.** No founder mutation is established. Consanguinity may facilitate homozygous cases but is not systematically reported. Carrier frequency cannot be reliably estimated but LOF alleles are observed in gnomAD.

**Population demographics.** No ethnic predilection is established. Cases are reported from multiple populations (including East Asian cases, [PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)). **Sex ratio** is not established; reported cases include males and females. **Age distribution** skews to adolescents/young adults at first presentation.

---

## Section 10 — Diagnostics

**Laboratory tests.** During episodes: **markedly elevated serum CK** (HP:0003236), **myoglobinuria**, and renal function monitoring for AKI (HP:0000083). Metabolic workup may show **abnormal fatty acylcarnitine profile** (HP:0012071) — important because acylcarnitine abnormalities also characterize the key differential (fatty-acid oxidation disorders).

**Biomarkers.** CK and myoglobin are the principal circulating biomarkers of myofiber breakdown; absent/reduced obscurin on muscle immunostaining/Western blot is a disease-specific tissue marker ([PMID: 34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/)).

**Imaging.** Muscle **MRI** can show muscle edema (bilateral lower-limb edema reported, [PMID: 40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/)).

**Biopsy / histopathology.** Muscle biopsy may show increased fiber-size variability (HP:0003557), centrally nucleated fibers (HP:0003687), type 2 fiber predominance (HP:0010602), and reduced/absent obscurin by immunostaining.

**Genetic testing (diagnostic cornerstone).** Because OBSCN is enormous (121 exons, among the largest human transcripts, [PMID: 40025502](https://pubmed.ncbi.nlm.nih.gov/40025502/)), **next-generation sequencing (WES or WGS) is the practical approach**; large multigene **rhabdomyolysis/metabolic-myopathy panels** that include OBSCN are appropriate. Confirm **bi-allelic** status and **phase** (compound-het vs in-cis) with parental testing. Interpret **truncating variants as likely causal; treat missense as VUS** pending functional/segregation data ([PMID: 33438037](https://pubmed.ncbi.nlm.nih.gov/33438037/)).

**Clinical criteria.** No formal consensus diagnostic criteria exist. Working diagnosis = **recurrent exertional/metabolic rhabdomyolysis + bi-allelic LOF OBSCN variants + supportive muscle findings (reduced obscurin)**, after exclusion of commoner causes.

**Differential diagnosis.** Other genetic rhabdomyolysis susceptibilities and metabolic myopathies must be excluded:

| Differential | Gene / defect | Distinguishing feature |
|---|---|---|
| RYR1-related / malignant hyperthermia susceptibility | RYR1 | Anesthetic-triggered MH; RYR1 variants ([PMID: 35285867](https://pubmed.ncbi.nlm.nih.gov/35285867/)) |
| VLCAD deficiency (FAO disorder) | ACADVL | Abnormal acylcarnitines; fasting/exercise triggers ([PMID: 35405752](https://pubmed.ncbi.nlm.nih.gov/35405752/), [PMID: 29153022](https://pubmed.ncbi.nlm.nih.gov/29153022/)) |
| McArdle disease (GSD V) | PYGM | Second-wind phenomenon; fixed exercise intolerance ([PMID: 41229646](https://pubmed.ncbi.nlm.nih.gov/41229646/)) |
| Drug-induced rhabdomyolysis | statins, TKIs | Temporal drug association ([PMID: 42473504](https://pubmed.ncbi.nlm.nih.gov/42473504/), [PMID: 41585502](https://pubmed.ncbi.nlm.nih.gov/41585502/)) |
| Infection-triggered | e.g., SARS-CoV-2 | Acute infection context ([PMID: 34871534](https://pubmed.ncbi.nlm.nih.gov/34871534/)) |
| Exertional / MH-spectrum | multifactorial | Round-table consensus on ER/EHS/MH overlap ([PMID: 28430550](https://pubmed.ncbi.nlm.nih.gov/28430550/)) |

**Screening.** No newborn or population screening exists. **Cascade genetic testing** of relatives of probands is reasonable for recurrence risk and trigger-avoidance counseling.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** No disease-specific mortality data. Prognosis is generally **good with prompt supportive management**; the principal acute risk is **myoglobinuric AKI** (HP:0000083), which can require dialysis in severe rhabdomyolysis generally ([PMID: 33645199](https://pubmed.ncbi.nlm.nih.gov/33645199/)). Rhabdomyolysis can occasionally be severe even without electrolyte abnormalities or renal failure ([PMID: 42491205](https://pubmed.ncbi.nlm.nih.gov/42491205/)).

**Morbidity / function.** Between episodes, function is often preserved; recurrent crises, hospitalizations, and exercise restriction are the main morbidity. Some patients show distal weakness.

**Complications.** AKI (sometimes requiring dialysis), electrolyte derangements (hyperkalemia, hyperphosphatemia, hypocalcemia) during severe episodes, and rarely compartment syndrome (general rhabdomyolysis complications).

**Recovery potential.** Individual episodes typically **recover fully** with hydration and supportive care; CK normalizes over days.

**Prognostic factors.** Severity/number of triggers, rapidity of fluid resuscitation, baseline renal function, and degree of CK elevation influence AKI risk. No molecular prognostic biomarker specific to RHABDO1 is established.

---

## Section 12 — Treatment

**No gene-specific therapy exists.** Management is **supportive** and **preventive**.

**Acute episode management.** **Aggressive intravenous fluid resuscitation** to maintain renal perfusion and clear myoglobin; **electrolyte correction**; **renal function monitoring**; dialysis if AKI is severe. This mirrors standard rhabdomyolysis care ([PMID: 33645199](https://pubmed.ncbi.nlm.nih.gov/33645199/)). (NCIT intervention terms: **Intravenous Fluid Therapy**; **Hemodialysis**; **Supportive Care**.)

**Preventive / supportive.** **Trigger avoidance** — adequate hydration, avoiding prolonged fasting, graded conditioning rather than sudden intense/unaccustomed exertion, prompt management of febrile illness, and caution with heat. Individualized exercise-tolerance assessment (as applied in metabolic myopathies) may define safe activity limits.

**Pharmacotherapy / advanced therapeutics.** No approved pharmacologic, gene, cell, or RNA-based therapy is specific to RHABDO1. No pharmacogenomic guidance is established.

**Treatment strategy.** The practical algorithm: (1) recognize recurrent rhabdomyolysis; (2) rule out common causes; (3) genetic confirmation of bi-allelic OBSCN LOF; (4) acute supportive care during episodes; (5) long-term trigger-avoidance counseling and genetic counseling for the family.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable at population level (rare Mendelian disorder). For at-risk/affected individuals, **trigger avoidance** is the key primary preventive measure against episodes.
- **Secondary prevention:** Early recognition of prodromal myalgia/dark urine and prompt hydration to abort/limit episodes and prevent AKI.
- **Tertiary prevention:** Aggressive management during crises to prevent renal failure and complications.
- **Genetic counseling:** Autosomal-recessive recurrence risk (25% for future sibs of a proband when both parents are carriers); cascade testing of relatives; reproductive counseling.
- **No immunization, public-health, or environmental program** applies specifically.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologues:** Obscurin is conserved in mammals; mouse **Obscn** (NCBI Gene) and the paralogue **Obsl1** are the principal experimental orthologues. The invertebrate analogue is **UNC-89** (*C. elegans*), which, like obscurin, localizes to the M-band ([PMID: 18477606](https://pubmed.ncbi.nlm.nih.gov/18477606/)).
- **Natural disease in animals:** No naturally occurring OBSCN-rhabdomyolysis disease is documented in companion animals or wildlife. **Exertional rhabdomyolysis is, however, a major condition in horses** (sporadic and recurrent/chronic forms), with intrinsic genetic contributors in some equine syndromes — a comparative-biology parallel, though not OBSCN-specific ([PMID: 39880734](https://pubmed.ncbi.nlm.nih.gov/39880734/)).
- **Evolutionary conservation:** The sarcomere–SR linkage role of obscurin and its M-band targeting are conserved from invertebrates (UNC-89) to mammals, supporting cross-species mechanistic relevance.

---

## Section 15 — Model Organisms

| Model | Type | Key findings | Relevance to RHABDO1 | PMID |
|---|---|---|---|---|
| *Obscn* / *Obsl1* double-KO mouse (skeletal) | Mammalian KO | Only combined deletion reveals roles in **sarcolemmal stability and SR organization** and muscle metabolism | Strong mechanistic support for SR/sarcolemma defect; highlights OBSL1 redundancy | [31098411](https://pubmed.ncbi.nlm.nih.gov/31098411/) |
| *Obscn* KO mouse (heart) | Mammalian KO | Reduced SR volume, lower SERCA/PLB, altered Ca²⁺ cycling, compensated dilated cardiomyopathy, arrhythmia | Models the **cardiac branch**; informs Ca²⁺-handling mechanism | [40366302](https://pubmed.ncbi.nlm.nih.gov/40366302/) |
| *Obsc/Obsl1* double-KO (heart) | Mammalian KO | Diastolic dysfunction, perturbed Ca²⁺ cycling, altered metabolism, deregulated mitophagy, ↑UPR | Links obscurin loss to SR + mitochondrial/metabolic dysfunction | [40066567](https://pubmed.ncbi.nlm.nih.gov/40066567/) |
| *Obscn*-ΔIg58/59 mouse | Knock-in/deletion | Atrial remodeling, Ca²⁺-based arrhythmogenesis, TAT depletion | Domain-specific cardiac model (distinct from skeletal rhabdo) | [39804820](https://pubmed.ncbi.nlm.nih.gov/39804820/) |
| Patient-derived cultured myoblasts | In vitro (human) | Greater decrease in **SR Ca²⁺ content upon starvation** vs controls | Direct human functional evidence of impaired SR Ca²⁺ handling | [34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/) |

**Phenotype recapitulation / limitations.** Mouse models robustly recapitulate the **SR disorganization and Ca²⁺-handling defect** central to RHABDO1, but the **cardiac phenotype dominates mouse models whereas human RHABDO1 spares the heart** — a key species/isoform discrepancy. No mouse model has been reported that reproduces the human **trigger-dependent recurrent skeletal rhabdomyolysis** phenotype in isolation, partly because of OBSL1 redundancy. Human patient myoblasts provide the most disease-faithful functional readout to date. Model databases: MGI, IMPC, IMSR for murine resources.

---

## Mechanistic Model / Interpretation

```
 Bi-allelic OBSCN LOF variant (nonsense / frameshift / splice)
            │  (demonstrated: reduced OBSCN, absent obscurin in patient muscle)
            ▼
 Loss of obscurin at M-band / Z-disk  --X--  (loses titin & myomesin linkage)
            │
            ▼
 Disrupted sarcomere->SR coupling -> SR disorganization
   + reduced SERCA / phospholamban (model evidence)
            │
            ▼
 Impaired Ca2+ re-uptake & reduced SR Ca2+ storage -> perturbed Ca2+ cycling
            │
            │<---- TRIGGER (exercise / fasting / fever)
            │       (patient myoblasts: lower SR Ca2+ on starvation)
            ▼
 Cytosolic Ca2+ dysregulation + sarcolemmal instability
            │
            ▼
 Myofiber necrosis (RHABDOMYOLYSIS)
            │
            ├─> ↑↑ serum CK, myalgia, cramps, exercise intolerance
            └─> Myoglobinuria -> Acute kidney injury (risk)

 BRANCH (heart): same SR/Ca2+ lesion -> dilated CM / arrhythmia in MICE
                 but CARDIAC SPARING in human RHABDO1 (isoform/redundancy)
```

The unifying interpretation: **RHABDO1 is a sarcoplasmic-reticulum Ca²⁺-handling disorder of skeletal muscle caused by obscurin loss of function.** The upstream lesion is structural (loss of the sarcomere–SR tether); the downstream consequence is a Ca²⁺-buffering deficit that stays clinically silent until a metabolic or mechanical trigger overwhelms the compromised myofiber, producing episodic breakdown. Cardiac sparing in humans — despite a clear cardiac disease axis in mice and in OBSCN-cardiomyopathy literature — is the most striking unexplained feature and points to tissue-specific isoform usage and OBSL1 redundancy.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [34957489](https://pubmed.ncbi.nlm.nih.gov/34957489/) | Cabrera-Serrano et al., *Brain* 2022 — defining case series | **Primary source**: 10 bi-allelic LOF OBSCN variants in 6 patients; reduced OBSCN/absent obscurin; starvation-sensitive SR Ca²⁺ in myoblasts; cardiac sparing; teenage onset |
| [38159459](https://pubmed.ncbi.nlm.nih.gov/38159459/) | Zemorshidi 2024 — case report | Two young patients, novel variants, exercise intolerance/rhabdomyolysis **without cardiomyopathy** |
| [40186404](https://pubmed.ncbi.nlm.nih.gov/40186404/) | Sun 2025 — case report | Compound-het nonsense+splice; **homozygous mother with milder phenotype** (variable expressivity); MRI muscle edema, no cardiac abnormality |
| [40813169](https://pubmed.ncbi.nlm.nih.gov/40813169/) | Liu 2025 — case report + review | Young adult, two OBSCN variants; reinforces pathogenic role; notes mechanism unclear |
| [31098411](https://pubmed.ncbi.nlm.nih.gov/31098411/) | Murine Obscn/Obsl1 — *skeletal* | Only combined deletion reveals SR organization + sarcolemmal stability roles (**mechanism**) |
| [40366302](https://pubmed.ncbi.nlm.nih.gov/40366302/) | Obscn KO heart | Reduced SR volume, ↓SERCA/PLB, altered Ca²⁺ cycling (**mechanism**; cardiac branch) |
| [40066567](https://pubmed.ncbi.nlm.nih.gov/40066567/) | Obsc/Obsl1 KO heart | SR + mitochondrial/metabolic dysfunction, mitophagy (**mechanism**) |
| [39804820](https://pubmed.ncbi.nlm.nih.gov/39804820/) | Obscn-ΔIg58/59 | Atrial Ca²⁺ arrhythmogenesis (distinct cardiac axis) |
| [18477606](https://pubmed.ncbi.nlm.nih.gov/18477606/) | Titin/myomesin–obscurin M-band | Molecular basis of obscurin M-band targeting |
| [20133654](https://pubmed.ncbi.nlm.nih.gov/20133654/) | Titin M10–obsl1 structure | M-band complex structure; disease mutations disrupt it |
| [11448995](https://pubmed.ncbi.nlm.nih.gov/11448995/) | Obscurin discovery | ~800 kDa, 1q42, IQ + RhoGEF signaling, titin binding |
| [19605563](https://pubmed.ncbi.nlm.nih.gov/19605563/) | Obscurin RhoGEF | Activates RhoA at M-band; injury response |
| [33438037](https://pubmed.ncbi.nlm.nih.gov/33438037/) | Obscurin missense variants | **Cautionary**: R4344Q/R4444W not clearly pathogenic; supports VUS treatment of missense |
| [40025502](https://pubmed.ncbi.nlm.nih.gov/40025502/) | OBSCN splicing | 121 exons; extensive alternative splicing; cardiac vs skeletal isoforms |
| [39880734](https://pubmed.ncbi.nlm.nih.gov/39880734/) | Equine exertional rhabdomyolysis | Comparative biology context |
| [33645199](https://pubmed.ncbi.nlm.nih.gov/33645199/) | Rhabdomyolysis→AKI | Supportive-care/complication context |

---

## Limitations and Knowledge Gaps

1. **Very small patient numbers.** RHABDO1 was defined in 2022; only ~12 patients are reported. Prevalence, incidence, penetrance, sex ratio, and natural history are therefore poorly quantified.
2. **Mechanism partly inferred from models.** The SR-disorganization/Ca²⁺ steps rest heavily on mouse *Obscn/Obsl1* data; the only direct human functional readout is the starvation-induced SR Ca²⁺ decrease in patient myoblasts. The precise step from Ca²⁺ dysregulation to myofiber necrosis in human RHABDO1 is inferred, not demonstrated.
3. **Unexplained cardiac sparing.** Why humans spare the heart while mice develop cardiomyopathy/arrhythmia is unresolved — likely isoform/redundancy differences, but unproven.
4. **Missense variant interpretation.** Most OBSCN missense variants remain VUS; functional assays and segregation data are lacking, and a known cardiomyopathy-"associated" variant (R4344Q) is common in African Americans, cautioning against over-calling pathogenicity.
5. **No disease-specific QoL, prognosis, or therapy data.** Management is extrapolated from general rhabdomyolysis care; no clinical trials exist.
6. **No faithful animal model of the human skeletal rhabdomyolysis phenotype** exists, hampering therapeutic development.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international RHABDO1 registry** to capture natural history, penetrance, trigger profiles, sex ratio, and outcomes.
2. **Generate a skeletal-muscle-specific, trigger-inducible OBSCN-LOF mouse** (or Obscn/Obsl1 conditional) and challenge with exercise/fasting to recapitulate episodic rhabdomyolysis and test why cardiac tissue is spared.
3. **Quantitative SR Ca²⁺ handling assays** in patient iPSC-derived myotubes under exercise-/fasting-mimetic stress, measuring SERCA/phospholamban levels and Ca²⁺ transients, to confirm and quantify the human mechanism.
4. **Functional reclassification of OBSCN missense VUS** using M-band targeting, titin/myomesin binding, domain stability, and SR Ca²⁺ assays to resolve ACMG classification.
5. **Acylcarnitine/metabolomic profiling** of patients to define the metabolic vulnerability (HP:0012071) and its overlap with fatty-acid-oxidation disorders.
6. **Evaluate preventive interventions** (structured hydration, graded exercise, nutritional/anti-fasting strategies) in a prospective observational cohort, with CK and episode frequency as endpoints.
7. **Deep phenotyping of heterozygous and homozygous carriers** (e.g., the homozygous-carrier mother phenotype) to delineate the expressivity spectrum and dosage sensitivity.

---

*Report compiled from the OBSCN/RHABDO1 primary literature, gnomAD v2.1.1 constraint data, ClinVar (NM_001386125.1), UniProt Q5VST9, and Monarch/HPO disease–phenotype annotations for MONDO:0859371. Evidence types are indicated throughout as human clinical, model organism, in vitro, or computational.*


## Artifacts

- [OpenScientist final report](Rhabdomyolysis_Susceptibility_To_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rhabdomyolysis_Susceptibility_To_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859371` (4 mentions) - the report calls it "MONDO"; MONDO calls it **rhabdomyolysis, susceptibility to, 1**
- `HP:0000083` (3 mentions) - the report calls it "Renal insufficiency", "myoglobinuric AKI"; HP calls it **Renal insufficiency**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003236` (2 mentions) - the report calls it "Elevated circulating creatine kinase", "markedly elevated serum CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `HP:0010602` (3 mentions) - the report calls it "Type 2 muscle fiber predominance", "type 2 fiber predominance"; HP calls it **Type 2 muscle fiber predominance**
- `HP:0012071` (4 mentions) - the report calls it "Abnormal circulating fatty acylcarnitine concentration", "abnormal fatty acylcarnitine profile"; HP calls it **Abnormal circulating fatty acylcarnitine concentration**, and lists "Abnormal fatty acylcarnitine level" among its other names
- `GO:0016529` (2 mentions) - the report calls it "GO cellular component:** sarcoplasmic reticulum", "Sarcoplasmic reticulum"; GO calls it **sarcoplasmic reticulum**
- `GO:0030018` (2 mentions) - the report calls it "Z-disk"; GO calls it **Z disc**, and lists "Z disk" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle fibers/myofibers"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0002036` (1 mention) - the report calls it "skeletal muscle tissue"; UBERON calls it **striated muscle tissue**
- `GO:0005739` (1 mention) - the report calls it "mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003236` - called "Elevated circulating creatine kinase", "markedly elevated serum CK"
- `HP:0000083` - called "Renal insufficiency", "myoglobinuric AKI"
- `HP:0010602` - called "Type 2 muscle fiber predominance", "type 2 fiber predominance"
- `HP:0002460` - called "Distal muscle weakness", "distal muscle weakness"
- `HP:0012071` - called "Abnormal circulating fatty acylcarnitine concentration", "abnormal fatty acylcarnitine profile"
- `GO:0016529` - called "GO cellular component:** sarcoplasmic reticulum", "Sarcoplasmic reticulum"