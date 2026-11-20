---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-03T11:21:59.506921'
end_time: '2026-11-03T11:35:21.308439'
duration_seconds: 801.8
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Staphyloenterotoxemia
  mondo_id: MONDO:0005971
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: staphylococcal food poisoning; staphylococcal toxemia due to food
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
  relevance_assessed: 20
  on_topic: 17
  validator_version: 0.5.1
term_validation:
  total_terms: 23
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005971
    reported_labels:
    - if available
    - staphylococcal food poisoning
    ontology_label: staphyloenterotoxemia
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Staphyloenterotoxemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Staphyloenterotoxemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Staphyloenterotoxemia
- **MONDO ID:** MONDO:0005971 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** staphylococcal food poisoning; staphylococcal toxemia due to food
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Staphyloenterotoxemia** covering all of the
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

# Staphyloenterotoxemia (Staphylococcal Food Poisoning): A Comprehensive Disease Characterization

**Disease:** Staphyloenterotoxemia (staphylococcal food poisoning; staphylococcal toxemia due to food)
**MONDO ID:** MONDO:0005971 · **MeSH:** Staphylococcal Food Poisoning (D013205) · **ICD-10:** A05.0 · **ICD-11:** bacterial foodborne intoxication · **OMIM:** not applicable (not a human Mendelian disease) · **Orphanet:** not a listed rare disease (common foodborne illness)
**Category:** Infectious Disease (toxin-mediated food intoxication)
**Causal "gene(s)":** *Bacterial* staphylococcal enterotoxin (*se*) genes — **sea, seb, sec, sed, see** and >20 newer *se/sel* types — carried by *Staphylococcus aureus* (NCBI Taxon:1280). **There is no human causal gene** and no OMIM Mendelian entry.

---

## Summary

**Staphyloenterotoxemia is not a genetic disease and not an active bacterial infection — it is an acute intoxication caused by ingesting preformed, heat-stable staphylococcal enterotoxins (SEs) that *Staphylococcus aureus* has already produced in mishandled food.** The "causal genes" named in the research template refer to *bacterial* enterotoxin genes (*sea*, *seb*, *sec*, *sed*, *see*, and a large family of newer *se/sel* genes carried on prophages, pathogenicity islands, plasmids, and the *egc* cluster), not any human gene. There is no OMIM entry, no inheritance pattern, no human susceptibility locus, and no genetic test of the patient; the disease is diagnosed epidemiologically and by direct detection of toxin or *se* genes in food/isolates. SEA is the enterotoxin most frequently implicated in human outbreaks.

The clinical syndrome is a short-incubation emetic gastroenteritis: nausea, forceful repeated vomiting, retching, and abdominal cramps begin roughly 1–6 hours after ingestion (typically 2–4 h), often with variable non-bloody diarrhea and usually without high fever, and resolve spontaneously within 24–48 hours. The short incubation is the signature of a *preformed* toxin acting directly, in contrast to the ~12–24 h incubation of most live-pathogen foodborne infections. Because the toxin is heat-stable, ordinary cooking/reheating does not inactivate it, and the toxin persists in food even after the bacteria are gone — so control must prevent toxin *formation* through hygiene and temperature management, and treatment of the ill patient is purely supportive (rehydration ± antiemetics; antibiotics are not indicated).

Mechanistically the disease has **two separable arms**. The dominant, clinically defining arm is an **emetic reflex**: enterotoxin binds intestinal submucosal mast cells, triggering degranulation and release of serotonin (5-HT) and histamine, which activate 5-HT3 receptors on vagal afferent neurons to drive the vomiting reflex — a pathway proven by vagotomy and 5-HT3-antagonist experiments in animal models. The second arm is the **superantigen** property of SEs: they cross-link MHC class II on antigen-presenting cells with T-cell-receptor Vβ domains, causing polyclonal T-cell activation and a pro-inflammatory cytokine storm (IL-2, IFN-γ, TNF) that underlies toxic-shock-like illness at high or parenteral doses. These two arms explain why the same toxin family produces both a self-limited emetic illness (oral food dose) and severe systemic superantigen pathology (high-dose/parenteral contexts).

---

## Key Findings

### F001 — Etiology: a preformed-toxin intoxication, not infection or inherited disease

Staphyloenterotoxemia is caused by ingestion of **preformed** *S. aureus* enterotoxins in food, not by colonization or an inherited defect. In the 2024 Shenzhen corporate-canteen outbreak, both *S. aureus* and enterotoxin A were recovered from patient specimens and from the implicated hand-shredded chicken, with an attack rate of 15% and a strong association with the suspect food (RR ≈ 5.91, 95% CI 1.41–24.76) ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)). The investigators explicitly noted that *"brief steaming before service would not have removed preformed toxin,"* underscoring that the agent is a heat-stable toxin rather than a live organism. Surveillance literature frames the general etiology plainly: *"Staphylococcal foodborne illness is a prevalent global foodborne disease caused by the ingestion of food contaminated with Staphylococcus aureus enterotoxins"* ([PMID: 41331910](https://pubmed.ncbi.nlm.nih.gov/41331910/)). The "causal genes" are therefore *bacterial* enterotoxin genes; **no human Mendelian cause exists and OMIM has no entry.**

### F002 — Emetic mechanism: mast-cell 5-HT/histamine → 5-HT3 vagal afferents → vomiting

The vomiting that defines the illness is a neuro-immune reflex. In the house musk shrew (*Suncus murinus*) emesis model, SEA-induced emesis was blocked by a 5-HT synthesis inhibitor and a 5-HT3 receptor antagonist, SEA increased intestinal 5-HT release, and *"SEA-induced emesis was also abolished by surgical vagotomy,"* establishing that *"the 5-HT3 receptors on vagal afferent neurons are essential for SEA-stimulated emesis"* ([PMID: 17517065](https://pubmed.ncbi.nlm.nih.gov/17517065/)). In the common marmoset primate model, *"SEA bound with submucosal mast cells and induced mast cell degranulation"* and histamine release, and the classical emetic SEs (SEA/SEB/SEC) induced vomiting whereas the non-emetic superantigen TSST-1 did not ([PMID: 31112582](https://pubmed.ncbi.nlm.nih.gov/31112582/)). The upstream trigger is thus mast-cell degranulation; the downstream effector is the vagal-afferent 5-HT3 emetic pathway.

### F003 — Heat stability: temperature abuse drives toxin accumulation; preformed toxin survives cooking

SEs are explicitly *"heat-stable enterotoxins encoded by virulence genes sea and seb"* ([PMID: 42418034](https://pubmed.ncbi.nlm.nih.gov/42418034/)). Predictive microbiology in chicken shows that *S. aureus* grows and begins producing detectable enterotoxin once populations exceed roughly 6.5–8.0 log CFU/g (e.g., at 37 °C after 8–13 h), with some growth possible as low as 10 °C in certain products ([PMID: 42314251](https://pubmed.ncbi.nlm.nih.gov/42314251/)). Critically, the toxin persists in food *"even in the absence of viable microorganisms, making direct toxin detection essential"* ([PMID: 42190559](https://pubmed.ncbi.nlm.nih.gov/42190559/)), and in the Shenzhen outbreak brief steaming failed to remove preformed toxin ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)). This is the single most important control-and-diagnosis fact: **cooking kills bacteria but not toxin.**

### F004 — Superantigen arm: MHC II × TCR-Vβ cross-linking → polyclonal T-cell cytokine storm

SEs are superantigens that *"polyclonally activate T cells by cross-linking MHC class II on antigen-presenting cells with T cell receptor (TCR) Vβ regions, generating potent IL-2/IFN-γ/TNF responses"* distinct from conventional peptide-MHC-restricted activation ([PMID: 41187575](https://pubmed.ncbi.nlm.nih.gov/41187575/)). SEB-type toxins are pyrogenic superantigens capable of inducing toxic shock ([PMID: 30909619](https://pubmed.ncbi.nlm.nih.gov/30909619/)). Mucosa-associated invariant T (MAIT) cells are among the most powerful early cytokine producers in response to SEB and then rapidly acquire an anergic/exhausted phenotype, defining a mechanism of superantigen-induced immunopathology followed by immunosuppression ([PMID: 28632753](https://pubmed.ncbi.nlm.nih.gov/28632753/)). This arm is largely separable from the emetic reflex and dominates at high or parenteral toxin doses.

### F005 — Epidemiology & prognosis: among the most common foodborne diseases, self-limited, heavily under-reported

Staphylococcal food poisoning is *"one of the most common Foodborne Diseases (FBD) in the world,"* with *"underreporting caused by the short duration of clinical symptoms and lack of medical care"* ([PMID: 36809532](https://pubmed.ncbi.nlm.nih.gov/36809532/)). It is described as a *"leading foodborne illness"* ([PMID: 42220823](https://pubmed.ncbi.nlm.nih.gov/42220823/)) and a *"prevalent global foodborne disease"* ([PMID: 41331910](https://pubmed.ncbi.nlm.nih.gov/41331910/)). Outbreaks are characteristically point-source with high attack rates — e.g., 16 of 107 exposed employees (attack rate 15.0%) in the Shenzhen canteen outbreak ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)).

### F006 — Food vehicles and reservoirs: post-cooking-handled protein/dairy foods; colonized handlers and mastitic milk

Implicated vehicles include hand-shredded cooked chicken ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)), cheese and dairy ([PMID: 42220823](https://pubmed.ncbi.nlm.nih.gov/42220823/)), retail meats and camel meat/offal ([PMID: 42376519](https://pubmed.ncbi.nlm.nih.gov/42376519/)), and milk from animals with subclinical mastitis, where PCR detected enterotoxin genes in coagulase-positive staphylococci ([PMID: 42376077](https://pubmed.ncbi.nlm.nih.gov/42376077/)). Food handlers are a major reservoir: *"Food handlers can contain these dangerous bacteria, which can contaminate food and cause staphylococcal food poisoning"* ([PMID: 41331910](https://pubmed.ncbi.nlm.nih.gov/41331910/)), and an asymptomatic colonized food handler was identified in the Shenzhen outbreak ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)).

### F007 — Causal "genes": the staphylococcal enterotoxin (*se*) gene family, SEA predominating in human outbreaks

The classical enterotoxins SEA–SEE (genes *sea*, *seb*, *sec*, *sed*, *see*) plus >20 newer *se/sel* types (e.g., *seg–selu*, *seh*, *ser*) constitute the "causal gene" set. In a genomic study of foodborne-outbreak *S. aureus* isolates, *"all strains produced classical staphylococcal enterotoxins, with staphylococcal enterotoxin (SEA) showing the highest detection rate (63.16%)"* ([PMID: 42350958](https://pubmed.ncbi.nlm.nih.gov/42350958/)). Reservoir-specific prevalence differs: in spent laying hens, *"503 of 995 isolates (50.6%) carried one or more staphylococcal enterotoxin (SE) genes, with seh being the most prevalent, followed by sed and ser"* ([PMID: 42425691](https://pubmed.ncbi.nlm.nih.gov/42425691/)); in buffalo subclinical-mastitis isolates, *sec* (8.5%), *sea* (8.2%), *sed* (4.5%), *seb* (2.8%), and *see* (1.7%) were detected ([PMID: 42406231](https://pubmed.ncbi.nlm.nih.gov/42406231/)).

### F008 — Diagnosis: epidemiology + direct toxin detection and *se*-gene PCR/WGS, not host testing

Because toxin persists without viable bacteria, *"direct toxin detection [is] essential for food safety surveillance"* ([PMID: 42190559](https://pubmed.ncbi.nlm.nih.gov/42190559/)). Enterotoxin is quantified by ELISA on culture supernatants and in food matrices (*"we quantified production of selected enterotoxins in culture supernatants… by enzyme-linked immunosorbent assay (ELISA)"*) ([PMID: 42425691](https://pubmed.ncbi.nlm.nih.gov/42425691/)), and outbreak investigation combines culture, immunoassay toxin detection, WGS virulence-gene profiling, and MLST ([PMID: 42350958](https://pubmed.ncbi.nlm.nih.gov/42350958/); [PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)). Emerging rapid platforms (e.g., aptasensors for *S. aureus*) are in development ([PMID: 42967785](https://pubmed.ncbi.nlm.nih.gov/42967785/)). **No patient genetic/host test is used.**

### F009 — Animal models: emesis bioassays plus natural disease in food animals

Emetic activity is studied in toxin-challenge (non-genetic) models: the house musk shrew reproduces SEA-induced emesis via intestinal 5-HT/5-HT3/vagal signaling ([PMID: 17517065](https://pubmed.ncbi.nlm.nih.gov/17517065/)), and the common marmoset is a primate emetic model in which *"Common marmosets were administered classical SEs, including SEA, SEB and SEC, and exhibited multiple vomiting responses. However, a non-emetic staphylococcal superantigen, toxic shock syndrome toxin-1, did not induce emesis"* ([PMID: 31112582](https://pubmed.ncbi.nlm.nih.gov/31112582/)). Rhesus/cynomolgus monkeys and kittens are historical emetic bioassays. Enterotoxigenic *S. aureus* naturally colonizes food-producing animals — *"S. aureus was detected in 649 of 800 birds (81.1%)"* in spent laying hens ([PMID: 42425691](https://pubmed.ncbi.nlm.nih.gov/42425691/)) — and causes bovine/buffalo subclinical mastitis carrying *se* genes ([PMID: 42376077](https://pubmed.ncbi.nlm.nih.gov/42376077/); [PMID: 42406231](https://pubmed.ncbi.nlm.nih.gov/42406231/)).

### F010 — Prevention: food-safety control of toxin formation; no vaccine or genetic prophylaxis

Primary prevention targets the two preventable failures seen in outbreaks: *"bare-hand contact with cooked, ready-to-eat food, and inadequate cooling of large batches during storage"* ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)). Because preformed heat-stable toxin survives reheating and persists without viable bacteria ([PMID: 42190559](https://pubmed.ncbi.nlm.nih.gov/42190559/)), control must prevent toxin *formation* via temperature control (rapid cooling, cold holding), supported by predictive growth/toxin models ([PMID: 42314251](https://pubmed.ncbi.nlm.nih.gov/42314251/)). Upstream biocontrol is experimental: a *Lactobacillus/Bifidobacterium* consortium achieved a *"4.56 log₁₀ CFU/mL reduction and 58.1% enterotoxin suppression at 72 h"* with *sea* downregulation in vitro ([PMID: 42418034](https://pubmed.ncbi.nlm.nih.gov/42418034/)), and lytic bacteriophage UHP46 reduced *S. aureus* in dairy matrices ([PMID: 42782413](https://pubmed.ncbi.nlm.nih.gov/42782413/)). **There is no human vaccine or pharmacologic prophylaxis.**

### F011 — Clinical phenotype: acute, short-incubation (~1–6 h) emetic gastroenteritis, self-limited in 24–48 h

SEs are *"thermostable superantigenic proteins produced by Staphylococcus aureus that are responsible for staphylococcal food poisoning (SFP) in humans"* ([PMID: 42625416](https://pubmed.ncbi.nlm.nih.gov/42625416/)). The hallmark is rapid onset 0.5–6 h (typically 2–4 h) after ingestion, dominated by nausea, forceful repeated vomiting, retching, and abdominal cramping, often with non-bloody diarrhea; fever is usually absent or low-grade. The short incubation reflects the action of *preformed* toxin (vs ~12–24 h for most live-pathogen foodborne infections). Animal data mechanistically explain the emesis-dominant phenotype ([PMID: 31112582](https://pubmed.ncbi.nlm.nih.gov/31112582/); [PMID: 17517065](https://pubmed.ncbi.nlm.nih.gov/17517065/)).

### F012 — Treatment: supportive only; antibiotics not indicated

Because illness results from preformed toxin rather than active infection, eradicating bacteria is irrelevant to the acute episode and antibiotics do not alter its course; management is symptomatic (fluid/electrolyte replacement ± antiemetics). The self-limited course — *"the short duration of clinical symptoms"* ([PMID: 36809532](https://pubmed.ncbi.nlm.nih.gov/36809532/)) — means supportive care suffices for the typical oral-dose illness. No toxin-specific antidote or vaccine is approved; biocontrol ([PMID: 42418034](https://pubmed.ncbi.nlm.nih.gov/42418034/)) and phage ([PMID: 42782413](https://pubmed.ncbi.nlm.nih.gov/42782413/)) are food-stage interventions, not human therapeutics.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. S. aureus (carrying se gene[s]) contaminates protein-/dairy-rich food,
   typically via a colonized food handler's hands or mastitic animal milk.
        → leads to
2. Temperature abuse (inadequate cooling / warm holding) permits S. aureus
   growth to ~>6.5–8 log CFU/g.
        → results in
3. Secretion and accumulation of preformed, HEAT-STABLE enterotoxin(s)
   (SEA predominant) in the food.
        → (cooking/reheating kills bacteria but NOT toxin)
4. Ingestion of toxin-laden food delivers preformed SE to the gut lumen.
        → branches into TWO arms:

   ── ARM A (dominant, emetic) ───────────────────────────────────────
   5a. SE binds intestinal submucosal MAST CELLS
         → induces mast-cell DEGRANULATION
   6a. Release of SEROTONIN (5-HT) and HISTAMINE in small intestine
         → activates 5-HT3 receptors on VAGAL AFFERENT neurons
   7a. Vagal signaling to brainstem emetic center
         → VOMITING, nausea, retching, cramps  (abolished by vagotomy)

   ── ARM B (superantigen, dose-dependent) ──────────────────────────
   5b. SE cross-links MHC class II (APC) × TCR Vβ (T cell)
         → POLYCLONAL T-cell activation (MHC-II/Vβ-restricted, not peptide)
   6b. Cytokine storm: IL-2, IFN-γ, TNF (MAIT cells early, then anergic)
         → systemic inflammation; at high/parenteral dose → TOXIC SHOCK
8. Self-limited resolution in 24–48 h as toxin is cleared (Arm A);
   or severe systemic illness requiring intensive support (Arm B).
```

**Upstream vs downstream.** The upstream initiating events are entirely *exogenous* (bacterial contamination + temperature abuse + toxin synthesis); there is no host genetic lesion. Within the host, mast-cell degranulation (Arm A) and MHC-II/TCR-Vβ engagement (Arm B) are the proximal upstream events, with 5-HT3/vagal signaling and the cytokine cascade, respectively, as downstream effectors.

**Why two arms matter.** The marmoset experiment is decisive: classical emetic SEs (SEA/SEB/SEC) cause vomiting, but the superantigen TSST-1 does not — demonstrating that superantigenicity and emesis are *separable* properties of these toxins ([PMID: 31112582](https://pubmed.ncbi.nlm.nih.gov/31112582/)). In ordinary oral food poisoning, Arm A dominates and the illness is self-limited; Arm B becomes clinically important at high systemic/parenteral exposure (e.g., toxic shock).

### Comparative enterotoxin-gene prevalence by reservoir

| Source / study | Dominant *se* gene(s) | Key figure | PMID |
|---|---|---|---|
| Human foodborne-outbreak isolates | **SEA** | SEA detection 63.16% | [42350958](https://pubmed.ncbi.nlm.nih.gov/42350958/) |
| Spent laying hens (poultry) | **seh** > sed > ser | 50.6% carried ≥1 *se* gene; 81.1% birds carried *S. aureus* | [42425691](https://pubmed.ncbi.nlm.nih.gov/42425691/) |
| Buffalo subclinical mastitis | **sec** > sea > sed > seb > see | sec 8.5%, sea 8.2% | [42406231](https://pubmed.ncbi.nlm.nih.gov/42406231/) |

### Ontology term suggestions

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0005971 (staphylococcal food poisoning) |
| Phenotype (HPO) | HP:0002013 Vomiting; HP:0002018 Nausea; HP:0002027 Abdominal pain; HP:0002014 Diarrhea |
| Biological process (GO) | GO:0001821 histamine secretion; GO:0002830 positive regulation of type 2 immune response; GO:0042098 T cell proliferation; GO:0001816 cytokine production; GO:0042310 vasoconstriction (shock arm) |
| Cell types (CL) | CL:0000097 mast cell; CL:0000624 CD4-positive αβ T cell; CL:0000940 mucosal invariant T (MAIT) cell; CL:0000236 B cell/APC (MHC-II); CL:0002254 enterocyte of small intestine |
| Anatomy (UBERON) | UBERON:0002108 small intestine; UBERON:0001155 colon; UBERON:0001759 vagus nerve; UBERON:0000945 stomach |
| Chemical (CHEBI) | CHEBI:28790 serotonin (5-HT); CHEBI:18295 histamine; staphylococcal enterotoxin (protein toxin) |

---

## Section-by-Section Characterization

**1. Disease information.** Acute self-limited emetic food intoxication. Identifiers: MONDO:0005971; MeSH "Staphylococcal Food Poisoning" (D013205); ICD-10 A05.0 (foodborne staphylococcal intoxication). **No OMIM** (not a Mendelian disease). Synonyms: staphylococcal food poisoning, staphylococcal toxemia due to food, staphylococcal enterotoxicosis. Information is derived from **aggregated disease-level** sources (outbreak investigations, surveillance, food-microbiology studies), not individual-patient genetic records (F001, F005).

**2. Etiology.** Primary cause is **infectious/toxigenic-environmental**: ingestion of preformed *S. aureus* enterotoxins. Risk factors are environmental/behavioral — poor food hygiene, bare-hand contact with ready-to-eat food, temperature abuse, colonized food handlers, mastitic animal milk. **No human genetic risk, protective, or gene-environment factors** apply (F001, F003, F006, F010).

**3. Phenotypes.** Symptoms/signs: vomiting (dominant), nausea, abdominal cramps, variable non-bloody diarrhea; fever usually absent/low-grade. Onset acute (~1–6 h); severity mild–moderate (self-limited) but occasionally severe with dehydration; course episodic/self-limited over 24–48 h. Frequency: vomiting near-universal; diarrhea variable (F002, F011).

**4. Genetic/molecular.** "Causal genes" are *bacterial*: *sea*, *seb*, *sec*, *sed*, *see* plus *seg–selu*, *seh*, *ser*, etc., carried on prophages, pathogenicity islands, plasmids, and the enterotoxin gene cluster (*egc*). SEA predominant in human outbreaks. No human HGNC gene, no pathogenic human variant, no ACMG classification, no allele-frequency/gnomAD data applicable. The relevant "variants" are *se*-gene presence/absence and SE serotype (F007).

**5. Environmental.** Vehicles: handled cooked meats/poultry, dairy/cheese, salads, cream-filled bakery. Reservoirs: human nasal/skin carriage, animal mastitis. Lifestyle factor: food-handling practices (F003, F006).

**6. Mechanism.** See causal chain above — two arms (emetic mast-cell/5-HT3/vagal reflex; superantigen MHC-II×TCR-Vβ cytokine storm) (F002, F004).

**7. Anatomical structures.** Primary: small-intestinal mucosa (submucosal mast cells, enterocytes); vagal afferents (UBERON:0001759). In the superantigen/shock arm, systemic lymphoid tissue and vasculature. Bilateral/systemic rather than lateralized (F002).

**8. Temporal development.** Onset acute, ~0.5–6 h (typically 2–4 h). No chronic stages; self-limited, resolving in 24–48 h; spontaneous remission the rule (F011).

**9. Inheritance & population.** **No inheritance pattern** (not genetic). Among the most common foodborne diseases globally; heavily under-reported; point-source outbreaks with high attack rates (e.g., 15%). No sex or ethnic predilection beyond exposure (F005).

**10. Diagnostics.** Epidemiologic linkage + direct toxin detection (ELISA/immunoassay) in food/supernatant; *se*-gene PCR; WGS + MLST for outbreak typing; emerging aptasensor/biosensor platforms. No host genetic testing. Differential: *Bacillus cereus* emetic toxin (similar short-incubation vomiting), other preformed-toxin intoxications, norovirus (F008).

**11. Prognosis.** Excellent — self-limited, full recovery in 24–48 h; mortality rare, mainly from dehydration in vulnerable persons or from severe superantigen/toxic-shock presentations (F005, F011, F012).

**12. Treatment.** Supportive: oral/IV rehydration, electrolyte correction, antiemetics as needed. **Antibiotics not indicated** (toxin-mediated). NCIT suggestions: NCIT:C70962 Fluid Replacement/Rehydration; antiemetic therapy (F012).

**13. Prevention.** Food hygiene (hand hygiene, glove/utensil use, exclude colonized handlers), temperature control (rapid cooling, cold holding, avoid prolonged warm holding), mastitis management in dairy herds. Experimental food-stage biocontrol (probiotics, bacteriophage). No vaccine (F010).

**14. Other species / natural disease.** Enterotoxigenic *S. aureus* naturally colonizes/infects poultry (81.1% carriage in spent laying hens), cattle and buffalo (subclinical mastitis with *se* genes), camels, and other food animals — important as reservoirs feeding the human food chain (F006, F009).

**15. Model organisms.** Non-genetic toxin-challenge emesis models: house musk shrew (*Suncus murinus*), common marmoset (*Callithrix jacchus*), historically rhesus/cynomolgus monkeys and kittens. These recapitulate the emetic phenotype and dissected the mast-cell/5-HT3/vagal pathway; they do not model a human genotype (none exists) (F002, F009).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/) | *Shenzhen hand-shredded chicken outbreak* | Anchors preformed-toxin etiology, attack rate, preventable control points |
| [41331910](https://pubmed.ncbi.nlm.nih.gov/41331910/) | *S. aureus among food handlers (meta-analysis)* | Food-handler reservoir; general etiology statement |
| [17517065](https://pubmed.ncbi.nlm.nih.gov/17517065/) | *SE emesis via intestinal 5-HT* | Proves 5-HT3/vagal emetic pathway (vagotomy abolishes emesis) |
| [31112582](https://pubmed.ncbi.nlm.nih.gov/31112582/) | *Histamine/mast-cell emesis in marmoset* | Mast-cell degranulation upstream; SE vs TSST-1 separability |
| [41187575](https://pubmed.ncbi.nlm.nih.gov/41187575/) | *SEs in cancer immunotherapy* | Defines superantigen MHC-II×TCR-Vβ mechanism and cytokines |
| [30909619](https://pubmed.ncbi.nlm.nih.gov/30909619/) | *Pyrogenic toxins induce toxic shock* | Superantigen → toxic shock (Arm B) |
| [28632753](https://pubmed.ncbi.nlm.nih.gov/28632753/) | *MAIT cells & superantigen immunopathology* | Early cytokine source then anergy — immunosuppression mechanism |
| [42314251](https://pubmed.ncbi.nlm.nih.gov/42314251/) | *Predictive modeling in chicken* | Growth/toxin thresholds; temperature dependence |
| [42190559](https://pubmed.ncbi.nlm.nih.gov/42190559/) | *Detection of foodborne protein toxins* | Toxin persists without bacteria → direct detection essential |
| [42418034](https://pubmed.ncbi.nlm.nih.gov/42418034/) | *Multi-strain probiotic suppression* | Heat-stable *sea/seb*; experimental biocontrol |
| [36809532](https://pubmed.ncbi.nlm.nih.gov/36809532/) | *Staphylococcal toxin in food (protocol/meta)* | Global frequency; under-reporting; short-duration symptoms |
| [42350958](https://pubmed.ncbi.nlm.nih.gov/42350958/) | *Genomic/virulence of outbreak isolates* | SEA predominance (63.16%); WGS/MLST diagnostics |
| [42425691](https://pubmed.ncbi.nlm.nih.gov/42425691/) | *S. aureus in spent laying hens* | *se*-gene prevalence; poultry reservoir; ELISA method |
| [42406231](https://pubmed.ncbi.nlm.nih.gov/42406231/) | *S. aureus buffalo mastitis MLST* | Enterotoxin-gene prevalence in dairy reservoir |
| [42220823](https://pubmed.ncbi.nlm.nih.gov/42220823/) | *SFP from cheese products* | Dairy vehicle; "leading foodborne illness" |
| [42625416](https://pubmed.ncbi.nlm.nih.gov/42625416/) | *Nonclassical enterotoxin genes, mastitis milk* | Classifies SE types; thermostable superantigen definition |
| [42782413](https://pubmed.ncbi.nlm.nih.gov/42782413/) | *Phage UHP46 biocontrol in dairy* | Experimental food-stage phage intervention |
| [42967785](https://pubmed.ncbi.nlm.nih.gov/42967785/) | *MOF aptasensor for S. aureus* | Emerging rapid detection platform |

**Evidence source types.** Human clinical/epidemiologic: 42700799, 41331910, 36809532, 42220823, 42350958. Animal model (in vivo emesis): 17517065, 31112582. In vitro/mechanistic immunology: 41187575, 30909619, 28632753. Food microbiology / in vitro: 42314251, 42418034, 42190559, 42425691, 42406231, 42782413, 42967785.

---

## Limitations and Knowledge Gaps

- **No patient-level or omics datasets were analyzed.** This disease has no human genetic component; the investigation is necessarily literature-based and the "molecular profiling" sections (patient transcriptomics/proteomics/metabolomics) are not applicable.
- **Clinical incubation/frequency figures (0.5–6 h; vomiting near-universal)** derive from established CDC/clinical-microbiology descriptions rather than from a single quantified cohort in the reviewed set; exact per-symptom frequencies are approximate.
- **Mechanistic emesis data are primarily from animal models** (shrew, marmoset). While concordant and mechanistically compelling, human in-vivo confirmation of the full 5-HT3/vagal chain is inferential.
- **The superantigen/toxic-shock arm** is dose- and route-dependent; its contribution to ordinary oral food poisoning (vs parenteral/high-dose exposure) is not precisely quantified.
- **One cited snippet (PMID 30909619)** was flagged as a title-level ("mismatch") match rather than an abstract quote; the superantigen-shock claim is independently supported by PMID 41187575 and 28632753.
- **Quantitative global burden** (incidence per 100,000) is poorly defined because of systematic under-reporting of this short, self-limited illness.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify per-symptom frequencies** from a pooled modern outbreak dataset (vomiting, diarrhea, fever, cramps, incubation distribution) to populate HPO frequency annotations precisely.
2. **Molecular dose–response mapping** of emetic vs superantigen activity across SE serotypes (SEA–SEE, SEH, newer *sel* types) in a standardized marmoset/shrew assay to rank clinical risk by toxin type.
3. **Validate direct-toxin rapid diagnostics** (aptasensor, LC-MS/MS) against gold-standard ELISA in real food matrices for point-of-care outbreak confirmation ([PMID: 42967785](https://pubmed.ncbi.nlm.nih.gov/42967785/)).
4. **Field-test food-stage biocontrol** (probiotic consortia, phage UHP46) in dairy/poultry supply chains for toxin-formation suppression, with *sea*/*seb* expression readouts ([PMID: 42418034](https://pubmed.ncbi.nlm.nih.gov/42418034/); [PMID: 42782413](https://pubmed.ncbi.nlm.nih.gov/42782413/)).
5. **Strengthen handler-screening and temperature-control interventions** and measure outbreak-rate reduction, targeting the two documented control points (bare-hand contact; inadequate cooling) ([PMID: 42700799](https://pubmed.ncbi.nlm.nih.gov/42700799/)).
6. **Mechanistic therapeutics**: test whether 5-HT3 antagonists (e.g., ondansetron) shorten symptom duration in human SFP, given the animal-model pathway evidence ([PMID: 17517065](https://pubmed.ncbi.nlm.nih.gov/17517065/)).

---

*Report compiled from 12 confirmed findings and 34 reviewed papers over 5 investigation iterations. Staphyloenterotoxemia (MONDO:0005971) is a toxin-mediated food intoxication with no human causal gene; its "causal genes" are the bacterial staphylococcal enterotoxin (se) gene family.*


## Artifacts

- [OpenScientist final report](Staphyloenterotoxemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Staphyloenterotoxemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005971` (5 mentions) - the report calls it "if available", "staphylococcal food poisoning"; MONDO calls it **staphyloenterotoxemia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0005971` - called "if available", "staphylococcal food poisoning"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.
