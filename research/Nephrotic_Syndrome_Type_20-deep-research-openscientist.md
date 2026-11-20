---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T16:55:47.906260'
end_time: '2026-11-09T17:11:38.656167'
duration_seconds: 950.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Nephrotic Syndrome Type 20
  mondo_id: MONDO:0026726
  category: Mendelian
  causal_genes: TBC1D8B
  omim_id: OMIM:301028
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
citation_count: 5
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.5.1
term_validation:
  total_terms: 24
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCBITaxon:7955
    reported_labels:
    - tbc1d8b
    ontology_label: Danio rerio
  labels_variant: 6
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nephrotic_Syndrome_Type_20-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nephrotic_Syndrome_Type_20-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 20
- **MONDO ID:** MONDO:0026726 (if available)
- **Causal gene(s):** TBC1D8B
- **OMIM:** OMIM:301028
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 20** covering all of the
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

# Nephrotic Syndrome Type 20 (NPHS20): A Comprehensive Disease Characterization

**Disease:** Nephrotic Syndrome Type 20 | **MONDO:** MONDO:0026726 | **OMIM:** #301028
**Causal gene:** *TBC1D8B* (TBC1 domain family member 8B) | **Gene OMIM:** *301027 | **Locus:** Xq22.3
**Inheritance:** X-linked (recessive, with variable female expression) | **Category:** Mendelian monogenic podocytopathy

---

## Summary

**Nephrotic Syndrome Type 20 (NPHS20) is an ultra-rare, X-linked monogenic kidney disease caused by hemizygous loss-of-function variants in *TBC1D8B***, a gene on chromosome Xq22.3 (gene OMIM *301027; HGNC:24715) that encodes a Rab-GTPase–activating protein (RabGAP). Despite the generic serial name "Nephrotic Syndrome Type 20," the disease is definitively linked to *TBC1D8B*, not to the other podocyte genes (NPHS1/nephrin, NPHS2/podocin, etc.) that cause the numbered nephrotic syndromes. The gene–disease relationship has been formally curated by ClinGen (assertion dated 2023-04-25) and is aggregated in GenCC, where submitter classifications range from Strong (Labcorp/Invitae) to Limited.

Mechanistically, TBC1D8B binds and inactivates the small GTPases RAB11A/RAB11B, master regulators of endosomal recycling. Loss of TBC1D8B function disinhibits RAB11 and impairs both endosomal maturation and the endocytic recycling of nephrin — the central structural protein of the podocyte slit diaphragm. The resulting mistrafficking of nephrin produces podocyte foot-process effacement, loss of slit diaphragms, nephrotic-range proteinuria, and focal segmental glomerulosclerosis (FSGS). This causal chain has been validated in human podocytes/fibroblasts, in zebrafish (knockdown/knockout rescued by wild-type but not mutant human mRNA), and in *Drosophila* nephrocytes.

Clinically, NPHS20 presents as the classic nephrotic triad (heavy proteinuria, hypoalbuminemia, edema) with highly variable onset — from neonatal/congenital to adulthood (reported age range ~1 month to 59 years) — and predominantly, but not universally, steroid-resistant disease. Only about 13 cases have been reported worldwide as of 2024. Diagnosis is genetic (whole-exome/genome sequencing or SRNS/FSGS gene panels) plus kidney biopsy showing FSGS and diffuse foot-process effacement. Management is supportive and immunosuppressive; progression to end-stage kidney disease (ESKD) is treated with transplantation, notably **without post-transplant disease recurrence**, consistent with a podocyte-intrinsic genetic mechanism. No gene-specific or curative therapy exists.

---

## Key Findings

### Finding 1 — NPHS20 is caused by hemizygous loss-of-function variants in X-linked *TBC1D8B*

NPHS20 (OMIM #301028; MONDO:0026726) is caused by pathogenic variants in **TBC1D8B** (TBC1 domain family member 8B; gene OMIM *301027; HGNC:24715), located on **Xq22.3**. The disease was defined through two concurrent 2019 reports: Dorval et al. identified hemizygous missense mutations in two families with X-linked early-onset steroid-resistant nephrotic syndrome (SRNS) with FSGS by exome sequencing, and Kampf et al. identified hemizygous missense mutations in five additional families. Reported variants include Q246H and F291S (Dorval), R64C, T780S, and W461X (Kampf), and p.Lys210Ter/K210Ter (Xu 2024).

Inheritance is X-linked: affected males are hemizygous, while carrier mothers and sisters are usually unaffected or mildly affected — though symptomatic female carriers are documented (see Finding 5).

> *"By exome sequencing, we identified missense mutations in TBC1D8B in two families with an X-linked early-onset SRNS with FSGS."* — [PMID: 30661770](https://pubmed.ncbi.nlm.nih.gov/30661770/)

> *"TBC1D8B was recently discovered as a novel disease-causing gene for X-linked NPHS."* — [PMID: 39468641](https://pubmed.ncbi.nlm.nih.gov/39468641/)

### Finding 2 — TBC1D8B regulates RAB11-dependent vesicular trafficking of nephrin in podocytes

TBC1D8B is a **Rab-GTPase–activating protein** that binds and inhibits active RAB11A/RAB11B, key regulators of endocytic recycling. Dorval et al. showed that TBC1D8B is present in human glomeruli, interacts with Rab11b, and that both internalization and recycling were dramatically decreased in affected individuals' podocytes and fibroblasts. Kampf et al. showed that TBC1D8B co-precipitates with nephrin, that patient mutations reduce its affinity for both RAB11 and nephrin, and that silencing TBC1D8B increases basal autophagy and exocytosis. In *Drosophila* nephrocytes, TBC1D8B silencing causes mistrafficking of fly nephrin in a Rab11-dependent manner. Thus, loss of TBC1D8B disinhibits RAB11, disturbing proper nephrin trafficking to the slit diaphragm.

> *"both internalization and recycling processes were dramatically decreased in affected individuals' podocytes and fibroblasts, confirming the crucial role of TBC1D8B in the cellular recycling processes, probably as a Rab11b GTPase-activating protein"* — [PMID: 30661770](https://pubmed.ncbi.nlm.nih.gov/30661770/)

> *"variants in the TBC1D8B gene on the X chromosome can lead to early-onset focal segmental glomerulosclerosis and steroid-resistant nephrotic syndrome by affecting endocytosis and recycling of nephrin"* — [PMID: 35970429](https://pubmed.ncbi.nlm.nih.gov/35970429/)

### Finding 3 — Clinical spectrum: variable-onset nephrotic syndrome with podocyte foot-process effacement and FSGS

The phenotype is the classic nephrotic triad: severe proteinuria (**HP:0000093**), hypoalbuminemia (**HP:0003073**), and edema (**HP:0000969**). Onset ranges from neonatal/congenital to adult:

- **Neonatal:** Xu 2024 reported an infant (onset ~1 month) with NPHS plus acute kidney injury, severe edema, proteinuria, and an encephalopathy episode (coma/epilepsy, transient corpus callosum DWI change).
- **Childhood:** Dorval and Kampf families had early-onset childhood SRNS.
- **Adult:** Fang 2023 reported a 19-year-old with adult-onset, steroid-dependent nephrotic syndrome.

Histology shows **focal segmental glomerulosclerosis (HP:0000097)**; electron microscopy shows diffuse podocyte foot-process effacement and loss of slit diaphragms. Steroid response is variable — most cases are steroid-resistant, but steroid-sensitive/steroid-dependent cases (responsive to prednisone ± cyclosporine) occur. Severe early-onset cases progress to CKD/ESRD.

> *"He had a complete remission of nephrotic syndrome after full-dose prednisone and cyclosporine treatment. Unfortunately, a relapse of nephrotic syndrome occurred during prednisone tapering."* — [PMID: 35970429](https://pubmed.ncbi.nlm.nih.gov/35970429/)

> *"The child, at 1 month, showed severe edema and proteinuria and unexplained coma with epilepsy."* — [PMID: 39468641](https://pubmed.ncbi.nlm.nih.gov/39468641/)

### Finding 4 — Zebrafish and *Drosophila* models recapitulate TBC1D8B-dependent proteinuria and nephrin mistrafficking

Dorval et al. showed that both knockdown and knockout of the unique zebrafish *tbc1d8b* ortholog induce proteinuria, which is rescued by wild-type human *TBC1D8B* mRNA but **not** by patient-mutant mRNAs — directly demonstrating pathogenicity and loss-of-function. *tbc1d8b⁻/⁻* zebrafish show a retracted glomerulus in an enlarged Bowman capsule, foot-process effacement, and loss of slit diaphragms. In *Drosophila*, silencing TBC1D8B in podocyte-like nephrocytes causes mistrafficking of fly nephrin; nephrin trafficking requires Rab11, and Rab11 overexpression phenocopies TBC1D8B silencing (Kampf et al.).

> *"In zebrafish we demonstrated that both knockdown and knockout of the unique TBC1D8B ortholog-induced proteinuria and that this phenotype was rescued by human TBC1D8B mRNA injection, but not by either of the two mutated mRNAs."* — [PMID: 30661770](https://pubmed.ncbi.nlm.nih.gov/30661770/)

### Finding 5 — Ultra-rare (~13 reported cases); mostly missense variants with no clear genotype–phenotype correlation

As of 2024, only **~13 cases** of NPHS20 have been reported worldwide. The reported *TBC1D8B* variants are mainly missense (9/13, ~69%); the remainder are 3 nonsense and 1 frameshift, distributed across functional domains (GRAM and TBC/RabGAP domains). Reported variants include Q246H, F291S, R64C (SSNS), T780S (SRNS), W461X, H906R (p.His906Arg, SSNS infant), p.Lys210Ter (GRAM1 domain, neonatal), and a frameshift in the TBC domain (adult female).

Onset spans congenital to age 59; 10/13 (77%) presented from childhood (3–9 y) to adulthood (18–59 y), while 3 presented at <3 years and were more severe. A proposed transcript-based genotype–phenotype rule (TBC1D8B-a–specific variants → SSNS; common-region → SRNS) was **rejected**, because R64C → SSNS but T780S → SRNS. Inheritance is X-linked: affected hemizygous males; heterozygous females range from asymptomatic carriers to non-nephrotic proteinuria and even FSGS/NS (e.g., a 49-year-old woman). Consanguinity was reported in Turkish and Pakistani families. No population-level prevalence/incidence estimates exist; there is no Orphanet prevalence class; gnomAD shows TBC1D8B loss-of-function variants are rare.

> *"a 49-year-old Chinese woman with nephrotic syndrome, characterized by normal kidney function but poor response to hormonal and immunosuppressive therapy, indicative of steroid-resistant nephrotic syndrome"* — [PMID: 39664988](https://pubmed.ncbi.nlm.nih.gov/39664988/)

### Finding 6 — Treatment is largely supportive/immunosuppressive; mostly steroid-resistant, variable CNI response, no post-transplant recurrence

No gene-specific or curative therapy exists; management follows general nephrotic syndrome/SRNS care. Most patients are steroid-resistant (corticosteroids, **NCIT:C198**), but steroid-sensitive (Hou 2021 infant, remission on glucocorticoids) and steroid-dependent (Fang 2023 adult: complete remission on full-dose prednisone + cyclosporine, relapse on prednisone taper) cases occur. Supportive care includes RAAS blockade (ACE inhibitors/ARBs) for proteinuria, diuretics for edema, albumin, lipid management, and thromboprophylaxis. Calcineurin inhibitors (cyclosporine **NCIT:C916**, tacrolimus) show partial benefit in some patients. Progressive cases reach ESKD (ages 2.8 and 9 years in the index families), requiring dialysis and kidney transplantation (**NCIT:C15366**); importantly, **no post-transplant disease recurrence** was observed, consistent with a podocyte-intrinsic genetic disease. No clinical trials, gene therapy, or RNA therapies are reported.

> *"The TBC1D8B protein interacts with nephrin, a podocyte slit diaphragm protein, regulates vesicle transport, and functions in the pathogenesis of NS."* — [PMID: 34858901](https://pubmed.ncbi.nlm.nih.gov/34858901/)

### Finding 7 — Diagnosis relies on WES/WGS or podocyte gene panels plus kidney biopsy

Diagnosis is fundamentally genetic: all reported cases were identified by trio/whole-exome sequencing (WES) or whole-genome sequencing (WGS), often confirmed by Sanger sequencing. TBC1D8B is included in hereditary/steroid-resistant nephrotic syndrome and FSGS gene panels. Clinical/laboratory findings of nephrotic syndrome: heavy proteinuria/albuminuria (urine protein up to ~20 g/day), hypoalbuminemia (serum albumin as low as ~11 g/L), hyperlipidemia, and edema, with variable serum creatinine/eGFR. Kidney biopsy (light microscopy) shows FSGS (including the perihilar variant); electron microscopy shows diffuse foot-process effacement and slit-diaphragm loss; immunofluorescence shows TBC1D8B in human glomeruli.

The TBC1D8B protein (**UniProt Q0IIM8**) contains a GRAM domain and a C-terminal TBC (Tre-2/Bub2/Cdc16) RabGAP domain. Truncating variants (e.g., p.Lys210Ter) reduce protein expression (Western blot), and missense variants in the TBC domain impair RabGAP/nephrin function. Differential diagnosis includes other genetic SRNS/FSGS (NPHS1/nephrin, NPHS2/podocin, WT1, INF2, TRPC6, ACTN4), congenital nephrotic syndrome, and immune-mediated/primary FSGS — distinguished by family history, X-linked male predominance, genetics, and absence of post-transplant recurrence.

> *"Immunofluorescence studies revealed TBC1D8B presence in human glomeruli, and affected individual podocytes displayed architectural changes associated with migration defects commonly found in FSGS."* — [PMID: 30661770](https://pubmed.ncbi.nlm.nih.gov/30661770/)

### Finding 8 — Primary affected structure is the glomerular podocyte; models are invertebrate/zebrafish, no mouse model yet

The primary affected structure is the **kidney (UBERON:0002113)**, specifically the **renal glomerulus (UBERON:0000074)** and the **glomerular visceral epithelial cell/podocyte (CL:0000653)**. The molecular lesion localizes to the podocyte slit diaphragm and the endocytic recycling compartment (**GO:0055037 recycling endosome; GO:0005096 GTPase activator activity; GO:0032456 endocytic recycling**). Secondary/systemic consequences of nephrotic syndrome include edema, hypercoagulability/thromboembolism, infection susceptibility (urinary immunoglobulin loss), hyperlipidemia, and, in progressive cases, CKD/ESKD.

Model organisms: **zebrafish** (*Danio rerio*, NCBITaxon:7955) *tbc1d8b* knockdown/knockout recapitulate proteinuria, glomerular retraction, foot-process effacement, and slit-diaphragm loss, rescued by WT but not mutant human mRNA; ***Drosophila melanogaster*** (NCBITaxon:7227) nephrocyte silencing recapitulates Rab11-dependent nephrin mistrafficking. The mouse ortholog is *Tbc1d8b* (NCBI Gene 76127; MGI:1918101), but **no published knockout mouse model of NPHS20 exists** (a notable limitation). No naturally occurring animal disease (OMIA) is recorded.

### Finding 9 — Verified gene/protein identifiers and domain architecture

Authoritative identifiers for the NPHS20 causal gene:

| Resource | Identifier |
|---|---|
| Gene symbol | TBC1D8B |
| HGNC | HGNC:24715 *(corrects earlier draft listing HGNC:29148)* |
| NCBI Gene | 54885 |
| Ensembl | ENSG00000133138 |
| Gene OMIM | *301027 |
| UniProt | Q0IIM8 |
| Cytogenetic location | Xq22.3 (chrX:106,802,673–106,876,150, GRCh38) |
| Transcripts | 7 |
| Mouse ortholog | *Tbc1d8b* (MGI:1918101; NCBI Gene 76127) |
| Gene synonyms | GRAMD8B, FLJ20298 |

The full-length protein is **1,120 amino acids** and comprises two N-terminal GRAM domains, a central TBC (Tre-2/Bub2/Cdc16) RabGAP domain, and a C-terminal EF-hand domain. Disease association: nephrotic syndrome type 20 (MONDO:0026726), X-linked. A PubMed search for 2025 TBC1D8B nephrotic syndrome literature returned no new papers; the evidence base remains the ~6 primary reports from 2019–2024.

### Finding 10 — ClinGen/GenCC validation; endosomal maturation implicated

The **TBC1D8B–Nephrotic Syndrome Type 20 (X-linked)** gene-disease relationship is formally curated by **ClinGen** (assertion dated 2023-04-25) and aggregated in **GenCC**, where submitter classifications range from Strong (Labcorp/Invitae) through Moderate/Supportive to Limited. TBC1D8B is included in diagnostic gene panels (e.g., Genomics England PanelApp "Proteinuric renal disease," panel 106) and catalogued in MalaCards (Nephrotic syndrome, type 20).

Mechanistically, beyond the original RAB11-recycling model, Milosavljevic et al. (2022) generated a stable TBC1D8B deletion/null allele in *Drosophila* nephrocytes and demonstrated that TBC1D8B is required for **endosomal maturation** and nephrin endocytosis — extending the trafficking defect to an endosomal maturation step that is upstream of, or parallel to, the recycling defect.

---

## Section-by-Section Report

### 1. Disease Information

NPHS20 is an ultra-rare, X-linked inherited podocytopathy — a monogenic form of steroid-resistant nephrotic syndrome (SRNS) that progresses to FSGS. Key identifiers: **OMIM #301028** (phenotype), **MONDO:0026726**, gene **OMIM *301027**. There is no distinct Orphanet prevalence class and no specific ICD-10/ICD-11 code (it falls under the broader category of genetic/steroid-resistant nephrotic syndrome and FSGS; MeSH terms: Nephrotic Syndrome; Glomerulosclerosis, Focal Segmental). Synonyms/alternative names: "NPHS20," "Nephrotic syndrome, type 20, X-linked," "TBC1D8B-associated nephrotic syndrome/FSGS." Information is **disease-level aggregated from individual case reports and small family cohorts** (not EHR-derived); the evidence base is ~6–7 primary publications (2019–2024) plus a ClinGen curation.

### 2. Etiology

The sole established cause is **genetic**: hemizygous loss-of-function variants in *TBC1D8B* on Xq22.3. No environmental, infectious, lifestyle, toxic, or occupational causes are implicated. **Genetic risk factors** are the causal variants themselves (predominantly missense, also nonsense/frameshift; see Finding 5). No susceptibility loci, modifier genes, or protective variants/alleles have been identified. **Consanguinity** was noted in Turkish and Pakistani families, consistent with rare recessive-acting alleles. No gene–environment interactions, protective diets, or environmental protective factors are reported — expected for a fully penetrant (in hemizygous males) monogenic trait.

### 3. Phenotypes

| Phenotype | HPO term | Type | Onset / severity / frequency |
|---|---|---|---|
| Proteinuria (nephrotic-range) | HP:0000093 | Lab abnormality | All cases; up to ~20 g/day; severe |
| Hypoalbuminemia | HP:0003073 | Lab abnormality | All cases; albumin as low as ~11 g/L |
| Edema | HP:0000969 | Clinical sign | Common; variable severity |
| Focal segmental glomerulosclerosis | HP:0000097 | Histopathology | Biopsy finding; defining lesion |
| Steroid-resistant nephrotic syndrome | HP:0000100 (nephrotic syndrome) | Clinical | Most cases (variable; some SSNS/SDNS) |
| Hyperlipidemia | HP:0003077 | Lab abnormality | Expected feature of NS |
| Chronic kidney disease / ESRD | HP:0012622 / HP:0003774 | Clinical | Severe early-onset cases |
| Encephalopathy (single neonatal case) | HP:0001298 | Clinical (uncertain) | One case; significance unresolved |

Onset ranges neonatal → adult (~1 month to 59 years). Progression is variable: stable/relapsing in milder cases, progressive to ESKD in severe early-onset cases. **Quality-of-life impact:** chronic proteinuria, edema, immunosuppression side effects, and (in progressive cases) dialysis/transplant substantially affect daily functioning; no disease-specific QoL instrument data exist.

### 4. Genetic / Molecular Information

**Causal gene:** *TBC1D8B* (see Finding 9 for identifiers). **Pathogenic variants:** predominantly missense (~69%), plus nonsense (W461X, p.Lys210Ter) and frameshift. Variant classification per ClinVar/ClinGen ranges from pathogenic/likely pathogenic to VUS; functional rescue assays (zebrafish) support pathogenicity of key missense variants. **Variant types:** missense, nonsense, frameshift — located across GRAM and TBC/RabGAP domains. **Allele frequency:** TBC1D8B LoF variants are rare in gnomAD. **Origin:** germline (X-linked); no somatic involvement. **Functional consequence:** loss of function — truncating variants reduce protein expression; missense variants reduce RabGAP activity and affinity for RAB11/nephrin. **Modifier genes, epigenetic changes, and chromosomal abnormalities:** none identified/reported.

### 5. Environmental Information

Not applicable. NPHS20 is a monogenic disorder with no established environmental factors, lifestyle contributors, toxins, or infectious triggers.

### 6. Mechanism / Pathophysiology

See the **Mechanistic Model** section below for the full ordered causal chain. In brief: *TBC1D8B* LoF → loss of RabGAP activity → disinhibited RAB11A/RAB11B → defective endosomal maturation and endocytic recycling → nephrin mistrafficking away from the slit diaphragm → foot-process effacement and slit-diaphragm loss → proteinuria/nephrotic syndrome → FSGS → CKD/ESKD. Molecular pathway: **RAB11-dependent endocytic recycling** (GO:0032456); cellular processes include autophagy and exocytosis (dysregulated on silencing). Cell type: glomerular podocyte (CL:0000653). Subcellular compartments: recycling endosome (GO:0055037), slit diaphragm.

### 7. Anatomical Structures Affected

- **Organ:** kidney (UBERON:0002113), specifically renal glomerulus (UBERON:0000074).
- **Tissue/cell:** glomerular visceral epithelial cell / podocyte (CL:0000653); glomerular filtration barrier/slit diaphragm.
- **Subcellular:** recycling endosome (GO:0055037); slit diaphragm membrane.
- **Secondary systems:** systemic (edema, hypercoagulability, hyperlipidemia, infection susceptibility from immunoglobulin loss). Bilateral renal involvement.

### 8. Temporal Development

**Onset:** congenital/neonatal to late adult (~1 month–59 years); pattern insidious to subacute. **Progression:** variable — some stable/relapsing, severe early-onset cases progress rapidly to ESKD (reported ages 2.8 and 9 years). Disease course is chronic and lifelong. **Remission:** treatment-induced remission occurs in steroid-sensitive/dependent cases (relapse on taper). **Critical period:** early intervention in steroid-responsive cases may delay progression; no formal window established.

### 9. Inheritance and Population

**Inheritance:** X-linked (hemizygous affected males; heterozygous females usually unaffected but can show proteinuria/FSGS/NS). **Epidemiology:** ultra-rare, ~13 cases worldwide; no prevalence/incidence estimates; no Orphanet prevalence class. **Penetrance:** apparently high in hemizygous males; variable/incomplete in heterozygous females. **Expressivity:** highly variable (onset, severity, steroid response). **Consanguinity:** reported (Turkish, Pakistani families). No founder effect, anticipation, or germline mosaicism reported. **Sex ratio:** male-predominant (X-linked). **Carrier frequency:** not established; gnomAD LoF variants rare.

### 10. Diagnostics

Diagnosis is genetic (WES/WGS, SRNS/FSGS gene panels including TBC1D8B; Sanger confirmation) plus kidney biopsy (FSGS on light microscopy; diffuse foot-process effacement and slit-diaphragm loss on EM; TBC1D8B immunofluorescence in glomeruli). Laboratory: nephrotic-range proteinuria/albuminuria, hypoalbuminemia, hyperlipidemia; variable creatinine/eGFR. Differential: NPHS1, NPHS2, WT1, INF2, TRPC6, ACTN4-related SRNS/FSGS; congenital nephrotic syndrome; immune-mediated/primary FSGS — distinguished by X-linked male predominance, genetics, and absence of post-transplant recurrence. CMA/karyotyping/FISH/mtDNA/repeat-expansion testing are not relevant to this point-variant disorder.

### 11. Outcome / Prognosis

Prognosis is variable and correlates loosely with onset age. Severe early-onset (<3 y) cases progress to ESKD in early childhood; later-onset cases may be steroid-responsive with better short-term outcomes. No survival statistics specific to NPHS20 exist. Key complications: ESKD requiring dialysis/transplant, plus general NS complications (thromboembolism, infection, hyperlipidemia). Recovery: transplantation is effective (no recurrence). Prognostic factors: onset age, steroid response, and rate of GFR decline; no validated prognostic biomarkers.

### 12. Treatment

See Finding 6. Supportive (RAAS blockade, diuretics, albumin, lipid/thrombosis management) plus immunosuppression (corticosteroids NCIT:C198; calcineurin inhibitors — cyclosporine NCIT:C916, tacrolimus). Most steroid-resistant; some steroid-sensitive/dependent. ESKD managed by dialysis and kidney transplantation (NCIT:C15366) without recurrence. No gene therapy, RNA therapy, targeted therapy, or clinical trials reported. Personalized/genotype-guided therapy is not yet available.

### 13. Prevention

No primary prevention (monogenic). **Genetic counseling** is central: X-linked recurrence risk assessment, carrier testing of at-risk females, and family planning guidance (prenatal/preimplantation genetic testing possible for known familial variants). Cascade testing of relatives enables early detection. Secondary prevention: monitoring proteinuria/renal function in known carriers. No immunization or public-health measures apply.

### 14. Other Species / Natural Disease

No naturally occurring animal disease (no OMIA entry). Orthologs: mouse *Tbc1d8b* (NCBI Gene 76127), zebrafish *tbc1d8b* (NCBITaxon:7955), *Drosophila* ortholog (NCBITaxon:7227). No zoonotic or cross-species transmission (genetic disease). Evolutionary conservation of the RAB11-nephrin trafficking mechanism underlies the utility of invertebrate/fish models.

### 15. Model Organisms

- **Zebrafish** (*Danio rerio*, ZFIN): *tbc1d8b* knockdown (morpholino) and knockout recapitulate proteinuria, glomerular retraction, foot-process effacement, and slit-diaphragm loss; rescued by WT but not mutant human mRNA — strong phenotype recapitulation and a pathogenicity assay.
- ***Drosophila melanogaster*** (FlyBase): nephrocyte-specific silencing and a stable null allele recapitulate Rab11-dependent nephrin mistrafficking and defective endosomal maturation.
- **Mouse** (*Tbc1d8b*, MGI:1918101): ortholog exists but **no published disease model** — a key gap.
- **Applications:** mechanistic dissection of RAB11-nephrin trafficking, variant pathogenicity testing. **Limitations:** invertebrate/fish nephron anatomy differs from mammalian glomerulus; no mammalian model for preclinical therapy.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **hemizygous loss-of-function variant in *TBC1D8B*** (missense in the GRAM/TBC domain, nonsense, or frameshift) on Xq22.3 **leads to** reduced or absent functional RabGAP protein in the podocyte (truncating variants reduce protein expression; missense variants reduce affinity for RAB11 and nephrin).
2. Loss of RabGAP activity **results in** failure to hydrolyze GTP on RAB11A/RAB11B, leaving RAB11 constitutively active (disinhibited).
3. Disinhibited/dysregulated RAB11 **leads to** defective endosomal maturation and impaired endocytic recycling within the podocyte (demonstrated in human cells; extended to endosomal maturation in *Drosophila* by Milosavljevic 2022).
4. Defective trafficking **results in** mistrafficking of **nephrin** — the slit-diaphragm protein that normally cycles between the plasma membrane and endosomes — away from its correct position at the slit diaphragm (shown in patient cells and *Drosophila* nephrocytes; *inferred* to be the proximate cause of slit-diaphragm loss in humans).
5. Loss of nephrin at the slit diaphragm **leads to** podocyte foot-process effacement and loss of slit diaphragms (seen on EM in patients and zebrafish).
6. Podocyte injury **results in** a disrupted glomerular filtration barrier → heavy proteinuria → hypoalbuminemia → edema (the nephrotic triad), plus secondary hyperlipidemia, hypercoagulability, and infection susceptibility.
7. Ongoing podocyte loss/injury **leads to** focal segmental glomerulosclerosis (FSGS) and, in severe/early-onset cases, progression to CKD/ESKD.

```
TBC1D8B LoF variant (Xq22.3)
        │ loss of RabGAP activity
        ▼
RAB11A/RAB11B remain GTP-bound (disinhibited)
        │
        ├──► defective endosomal maturation  (Drosophila null; Milosavljevic 2022)
        └──► impaired endocytic recycling    (patient podocytes/fibroblasts)
                         │  both converge on
                         ▼
          Nephrin mistrafficking away from slit diaphragm
                         │
                         ▼
     Foot-process effacement + slit-diaphragm loss (EM)
                         │
                         ▼
   Proteinuria → hypoalbuminemia → edema (nephrotic triad)
                         │
                         ▼
                        FSGS → CKD/ESKD
                         │
                         ▼
          Transplant → NO recurrence (podocyte-intrinsic)
```

**Upstream vs downstream:** The *TBC1D8B* mutation and RAB11 dysregulation are the upstream initiating events; nephrin mistrafficking and slit-diaphragm loss are the central mediators; proteinuria, FSGS, and ESKD are downstream consequences. The absence of post-transplant recurrence is a key corollary: because the defect is intrinsic to the host podocyte's trafficking machinery (not a circulating factor), a genetically normal donor kidney is not re-injured.

**Cell types and processes:** glomerular podocyte (CL:0000653); biological processes include endocytic recycling (GO:0032456), recycling endosome function (GO:0055037), and GTPase activator activity (GO:0005096).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [30661770](https://pubmed.ncbi.nlm.nih.gov/30661770/) | *TBC1D8B Loss-of-Function Mutations Lead to X-Linked Nephrotic Syndrome via Defective Trafficking Pathways* | Human genetics + zebrafish + in vitro | Foundational: establishes causation, RabGAP/Rab11b mechanism, glomerular localization, zebrafish rescue (Findings 1, 2, 4, 7, 8) |
| [35970429](https://pubmed.ncbi.nlm.nih.gov/35970429/) | *Adult-Onset FSGS With Steroid-Dependent NS Caused by a Novel TBC1D8B Variant* | Human case report + review | Adult-onset, steroid-dependent phenotype; links variants to defective nephrin endocytosis/recycling (Findings 2, 3, 6) |
| [39468641](https://pubmed.ncbi.nlm.nih.gov/39468641/) | *Novel TBC1D8B variant causes neonatal NS combined with AKI* | Human case report | Neonatal severe phenotype, possible extrarenal involvement; confirms TBC1D8B as X-linked NPHS gene (Findings 1, 3) |
| [34858901](https://pubmed.ncbi.nlm.nih.gov/34858901/) | *Novel [TBC1D8B variant]* (Hou 2021) | Human case report | Steroid-sensitive infant case; nephrin-interaction/vesicle-transport basis for treatment rationale (Finding 6) |
| [39664988](https://pubmed.ncbi.nlm.nih.gov/39664988/) | *Adult-onset female FSGS with NS caused by a [TBC1D8B frameshift]* | Human case report | Symptomatic female carrier with TBC-domain frameshift; female expression and variant spectrum (Finding 5) |
| [36137753](https://pubmed.ncbi.nlm.nih.gov/36137753/) | *Nephrotic Syndrome Gene [TBC1D8B]* (Milosavljevic 2022) | *Drosophila* null allele | Extends mechanism to endosomal maturation and nephrin endocytosis (Finding 10) |

The evidence base is internally consistent: two independent 2019 human genetics studies (with zebrafish and fly functional validation) established causation and mechanism, and subsequent case reports (2021–2024) expanded the phenotypic and variant spectrum while reproducing the same trafficking theme. The 2022 *Drosophila* null-allele study and the ClinGen/GenCC curation strengthen the gene-disease assertion and refine the mechanism. No study has challenged the core TBC1D8B–RAB11–nephrin model.

---

## Limitations and Knowledge Gaps

- **Extreme rarity (~13 cases):** No reliable prevalence/incidence estimates, no Orphanet prevalence class, and limited statistical power for genotype–phenotype correlation. Most evidence is from single case reports and two small family cohorts.
- **No genotype–phenotype rule:** A proposed transcript-based rule was refuted; what determines steroid responsiveness and onset age remains unknown. Modifier genes have not been identified.
- **No mouse model:** Functional validation rests on zebrafish and *Drosophila*; a mammalian (mouse) knockout/conditional model that recapitulates FSGS is lacking, limiting preclinical therapeutic testing.
- **Extrarenal involvement uncertain:** A single neonatal case had encephalopathy (coma/epilepsy, transient corpus callosum DWI change); whether this is a true extrarenal manifestation of TBC1D8B loss or a complication of severe nephrotic syndrome/AKI is unresolved.
- **Female carrier expression poorly characterized:** Reports of symptomatic heterozygous females (including FSGS/NS) suggest variable X-inactivation effects, but penetrance and spectrum in females are not systematically studied.
- **No disease-specific therapy or trials:** Treatment is extrapolated from general SRNS care; there are no NPHS20-specific clinical trials, biomarkers of progression, or targeted agents.
- **Epigenetics, chromosomal abnormalities, environmental/infectious triggers, and gene–environment interactions:** Not applicable / not reported for this monogenic disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional podocyte-specific *Tbc1d8b* knockout mouse** to establish a mammalian model, characterize natural history (onset, proteinuria, FSGS, ESKD), and enable preclinical therapeutic testing.
2. **Establish an international NPHS20 patient registry** to pool the ~13+ cases, systematically capture variant data, onset, steroid response, progression, and transplant outcomes, and power genotype–phenotype analyses.
3. **Structure–function studies of patient variants** (GRAM vs TBC domain; missense vs truncating) using RabGAP activity assays and nephrin-binding assays to define a mechanistic basis for steroid responsiveness and onset variability.
4. **Patient-derived iPSC → podocyte/organoid models** to test whether RAB11 pathway modulation (e.g., small-molecule RAB11 inhibition or restoration of endosomal maturation) rescues nephrin trafficking — a candidate precision-therapy avenue.
5. **Characterize female carriers** with X-inactivation analysis correlated to phenotype severity to clarify penetrance and counseling implications.
6. **Investigate the single neonatal encephalopathy observation** by assessing TBC1D8B expression in neural tissue and reviewing additional early-onset cases for CNS involvement.
7. **Curate and submit all reported variants to ClinVar** with standardized ACMG/AMP classifications to improve diagnostic interpretation for future cases.

---

*Report compiled from 10 confirmed findings and 6 primary publications (2019–2024) plus ClinGen/GenCC curation. All mechanistic and clinical claims are anchored to the cited PMIDs with verified abstract quotations.*


## Artifacts

- [OpenScientist final report](Nephrotic_Syndrome_Type_20-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nephrotic_Syndrome_Type_20-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 12 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:7955` (2 mentions) - the report calls it "tbc1d8b"; NCBITaxon calls it **Danio rerio**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000093` (2 mentions) - the report calls it "Proteinuria (nephrotic-range)"; HP calls it **Proteinuria**
- `UBERON:0002113` (2 mentions) - the report calls it "Organ:** kidney"; UBERON calls it **kidney**
- `CL:0000653` (4 mentions) - the report calls it "Tissue/cell:** glomerular visceral epithelial cell / podocyte"; CL calls it **podocyte**, and lists "glomerular visceral epithelial cell" among its other names
- `GO:0055037` (4 mentions) - the report calls it "Subcellular:** recycling endosome"; GO calls it **recycling endosome**
- `GO:0032456` (3 mentions) - the report calls it "RAB11-dependent endocytic recycling"; GO calls it **endocytic recycling**
- `HP:0001298` (1 mention) - the report calls it "Encephalopathy (single neonatal case)"; HP calls it **Encephalopathy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.