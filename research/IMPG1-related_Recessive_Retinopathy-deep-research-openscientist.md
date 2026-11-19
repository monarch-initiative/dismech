---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:00:40.530552'
end_time: '2026-10-30T23:43:25.746603'
duration_seconds: 2565.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: IMPG1-related Recessive Retinopathy
  mondo_id: MONDO:1040037
  category: Mendelian
  causal_genes: IMPG1
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.4.0
term_validation:
  total_terms: 18
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:1040037
    reported_labels:
    - Disease MONDO
    ontology_label: IMPG1-related recessive retinopathy
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
  path: IMPG1-related_Recessive_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IMPG1-related_Recessive_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IMPG1-related Recessive Retinopathy
- **MONDO ID:** MONDO:1040037 (if available)
- **Causal gene(s):** IMPG1
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

Please provide a comprehensive research report on **IMPG1-related Recessive Retinopathy** covering all of the
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

# IMPG1-related Recessive Retinopathy — Comprehensive Disease Characterization Report

**Disease:** IMPG1-related Recessive Retinopathy
**Causal gene:** **IMPG1** (interphotoreceptor matrix proteoglycan 1, encoding SPACR/IPM150)
**MONDO ID:** MONDO:1040037 · **Phenotype OMIM:** 616151 (Vitelliform macular dystrophy 4, VMD4)

---

## Summary

**IMPG1-related recessive retinopathy is a rare autosomal-recessive inherited retinal dystrophy caused by biallelic (loss-of-function or hypomorphic) variants in *IMPG1*, the gene on chromosome 6q14.1 encoding SPACR (also called IPM150), a chondroitin-sulfate proteoglycan of the interphotoreceptor matrix (IPM).** This report concerns the IMPG1 gene specifically — the causal gene named in the task header — and not the clinically similar IMPG2 (IPM200) disorder or the dominant *BEST1*/*PRPH2* vitelliform dystrophies, which are important differential diagnoses. The disease was first defined by Manes and colleagues, who identified both dominant and recessive *IMPG1* families within a vitelliform macular dystrophy (VMD) cohort [PMID: 23993198].

Mechanistically, SPACR is one of the two principal proteoglycans (with IMPG2/IPM200) that build and organize the IPM — the specialized extracellular matrix that ensheaths rod and cone photoreceptor outer segments and provides the chondroitin-sulfate–rich cone glycocalyx. Loss or dysmaturation of SPACR, or its mislocalization into the subretinal space, disrupts the IPM glycocalyx, interferes with photoreceptor outer-segment/connecting-cilium development, and leads to accumulation of subretinal "vitelliform" material. Clinically this manifests as adult-onset, slowly progressive, bilateral vitelliform maculopathy with drusen-like deposits and cone-predominant photoreceptor loss. The electro-oculogram (EOG) is characteristically normal or only mildly reduced, distinguishing it from Best disease.

The disorder is ultra-rare, accounting for a small minority of VMD families. Onset is typically in the fourth decade with moderate visual impairment (mean visual acuity ~20/40). There is no sex predilection and the disease does not affect survival. No approved disease-specific or curative therapy exists; management is supportive (low-vision rehabilitation) together with genetic counseling, carrier/cascade testing, and reproductive options. Because the recessive disease is driven by biallelic loss of function, gene-augmentation is a rational future therapeutic strategy, though no IMPG1 clinical trials currently exist.

---

## Key Findings

### Finding 1 — IMPG1 (encoding SPACR) is the causal gene; biallelic variants cause recessive vitelliform retinopathy

The foundational genetic evidence comes from a large VMD cohort in which *IMPG1* (6q14, encoding the interphotoreceptor-matrix proteoglycan SPACR/IPM150) was shown to cause disease in both dominant and recessive forms. For the **autosomal-recessive** form, two affected individuals from one family were homozygous for the splice-site variant **c.807+1G>T**, and two from a second family were compound heterozygous for **c.461T>C (p.Leu154Pro)** and **c.1519C>T (p.Arg507\*)** [PMID: 23993198]. The verbatim report states: *"Two individuals from one family affected by autosomal-recessive VMD were homozygous for the splice-site mutation c.807+1G>T, and two from another family were compound heterozygous for the mutations c.461T>C (p.Leu154Pro) and c.1519C>T (p.Arg507(∗))."* The same work establishes the gene product: *"IMPG1 encodes the SPACR protein, a component of the rod and cone photoreceptor extracellular matrix domains."*

This provides the identity link between the clinical disease (MONDO:1040037) and its molecular cause. The recessive variant spectrum includes splice-site, missense, and nonsense alleles — consistent with a loss-of-function/hypomorphic mechanism.

### Finding 2 — Mechanism: SPACR is an IPM proteoglycan whose loss/dysmaturation disrupts the matrix and causes subretinal vitelliform deposits

SPACR/IMPG1 and IMPG2 are the two major proteoglycans of the interphotoreceptor matrix, the principal source of chondroitin sulfate and constituents of the cone glycocalyx (peanut-agglutinin/PNA-positive) [PMID: 32265257]. The review by Salido & Ramamurthy states directly: *"The IPM includes the following two unique proteoglycans: IPM proteoglycan 1 (IMPG1) and IMPG2. Patients with mutations in IMPG1/IMPG2 develop visual deficits with subretinal material accumulation, highlighting the critical role of the IPM in vision."*

Both proteins carry **SEA domains** whose autoproteolytic cleavage is required for maturation; disease-associated human mutations in the SEA domain inhibit this proteolysis [PMID: 36109576]: *"Point mutations mimicking human mutations in the SEA domain of IMPG1 that are associated with vision disease inhibited proteolysis."* At the biochemical level, SPACR/Spacrcan binds hyaluronan and chondroitin sulfate via RHAMM-type hyaluronan-binding motifs, which is how it organizes the IPM [PMID: 15044457]: *"These RHAMM-type HABMs in Spacrcan are involved in hyaluronan binding."*

Together these establish a coherent lesion: defective SPACR (through absent protein, impaired SEA-domain maturation, or lost glycosaminoglycan binding) fails to build/organize the IPM glycocalyx around outer segments, and subretinal material accumulates as the clinically observed vitelliform deposit.

### Finding 3 — Clinical phenotype: adult-onset, moderate, slowly progressive vitelliform maculopathy with drusen-like deposits

In the Meunier cohort, patients with IMPG1 (or IMPG2) mutations had **late onset and moderate visual impairment**: *"Patients with IMPG1 or IMPG2 mutations had a late onset and moderate visual impairment (mean visual acuity, 20/40; mean age of onset, 42 years)"* [PMID: 25085631]. The presumed-recessive sporadic case had onset at **38 years and acuity 20/50**: *"even in the sporadic case of family 3 with a presumed recessive transmission (age at onset, 38 years; mean visual acuity, 20/50)."* Drusen-like lesions adjacent to the vitelliform deposits were observed, and most cases had a normal or only moderately reduced EOG Arden ratio [PMID: 25085631; PMID: 23993198]. The disease is a rare cause of VMD overall.

### Finding 4 — Dual inheritance (AD and AR) and a phenotypic spectrum spanning VMD to retinitis pigmentosa

*IMPG1* is one of a small set (~9) of **dual-inheritance** inherited-retinal-dystrophy (IRD) genes, in which both monoallelic (dominant) and biallelic (recessive) disease occur. In the Portuguese IRD-PT registry, dual-inheritance genes accounted for 12% of genetic diagnoses, with phenotype modulated by variant location and allele dosage [PMID: 42321002]: *"This spectrum, modulated by variant location and allele dosage, determines phenotypes and contributes to IRD heterogeneity."* Beyond classic VMD, monoallelic or biallelic *IMPG1* variants have been associated with **retinitis pigmentosa (RP)** [PMID: 32817297]: *"This study discusses a previously unreported association between monoallelic or biallelic"* IMPG1 variants and RP. The original gene description already included recessive VMD families [PMID: 23993198]. The practical implication: the IMPG1 recessive phenotype is best viewed as a spectrum from focal macular vitelliform disease to more widespread outer-retinal/RP-like degeneration.

### Finding 5 — Model-organism evidence: pathology requires IMPG1 mislocalization, not simple absence

A key mechanistic insight comes from mouse genetics. **Impg1-knockout mice have a normal retina**: *"No evident morphologic or functional deficits were found in mice lacking IMPG1"* [PMID: 32265257]. However, in **IMPG2-knockout** mice, IMPG1 abnormally accumulates in the subretinal space, forming subretinal lesions and reducing visual function: *"In the absence of IMPG2, IMPG1 abnormally accumulated at the subretinal space."* Critically, **double IMPG1/IMPG2-knockout** mice have normal structure and function — demonstrating that **aberrant IMPG1 distribution, rather than its mere loss, is the main driver of the visual alteration** in that model. Complementary metabolomics in IMPG2-deficient retinas with subretinal lesions showed *"reduced glutamate metabolism, urea cycle, and galactose metabolism suggesting affected energy metabolism"* [PMID: 37440072]. This nuance — that mislocalized matrix protein is pathogenic — is important for interpreting human disease and for therapy design.

### Finding 6 — Diagnosis relies on multimodal retinal imaging

IMPG1 vitelliform lesions are **subretinal on OCT** and **hyperautofluorescent** on short-wavelength fundus autofluorescence, with genetic panel testing confirming the diagnosis [PMID: 40315441]: *"Short-wavelength fundus autofluorescence confirmed that the lesions were hyperautofluorescent."* Multimodal **adaptive-optics** imaging of VMD showed within-lesion cone density reduced to 37% of normal and RPE to 8.4% of normal, and — importantly for differential diagnosis — *"cones were affected to a greater extent than RPE in patients with IMPG1 and IMPG2 pathogenic variants, but RPE was affected more than cones in BEST1 and PRPH2 VMD"* [PMID: 35900727]. A heterozygous p.Leu154Pro carrier showed outer-retinal ellipsoid/interdigitation-zone disruption on OCT [PMID: 30688845]: *"Optical coherence tomography revealed disorganization and decreased reflectance of the foveal ellipsoid and interdigitation zones."* The EOG Arden ratio is typically normal or mildly reduced, which helps separate IMPG1 disease from Best disease (BEST1) [PMID: 23993198].

### Finding 7 — IMPG1 is required for photoreceptor outer-segment/connecting-cilium development and IPM formation; variable expressivity with modifiers

A developmental role was demonstrated in human pluripotent stem-cell-derived retinal organoids: blocking IMPG1 (and CD44) *"affected the development of photoreceptors, their inner/outer segments and connecting cilia and disrupted IPM formation, with IMPG1 having an earlier and more significant impact"* [PMID: 29777959]. Clinically, siblings carrying an identical *IMPG1* exon-7 deletion showed divergent phenotypes (one with a single foveal lesion, the other with asymptomatic multifocal extrafoveal lesions), supporting **variable expressivity with individual modifiers** [PMID: 40315441]: *"Intrafamilial variability in the topography of the lesions with multifocality in one of the siblings suggests retina-wide abnormalities with individual modifiers modulating disease expression."*

### Finding 8 — Consolidated identifiers, classification, and management

| Attribute | Value |
|---|---|
| Gene symbol | **IMPG1** |
| HGNC | HGNC:6055 |
| NCBI Gene | 3617 |
| Ensembl | ENSG00000112706 |
| UniProt | Q17R60 (SPACR / IPM150) |
| Cytoband | 6q14.1 |
| Gene OMIM | 602870 |
| Disease MONDO | MONDO:1040037 |
| Phenotype OMIM | VMD4, 616151 |
| ICD-10 | H35.5 (hereditary retinal dystrophy) |
| Mouse ortholog | *Impg1* (NCBI Gene 63859; MGI:1926876) |
| Inheritance | Autosomal recessive (biallelic LoF/hypomorphic); IMPG1 is a dual-inheritance gene |

The disease is ultra-rare: *"IMPG1 was the causal gene in 3 families (IMPG1 1-3, 11 patients) and IMPG2 in a fourth family (2 patients)"* in the Meunier cohort [PMID: 25085631]. There is no sex predilection; onset is in adulthood; the course is slowly progressive; and there is no effect on survival. Management is supportive (low-vision rehabilitation) plus genetic counseling, carrier/cascade testing, and prenatal/preimplantation genetic testing options. Dual inheritance is confirmed [PMID: 23993198]: *"We conclude that IMPG1 mutations cause both autosomal-dominant and -recessive forms of VMD."*

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *IMPG1* variant** (splice-site c.807+1G>T; nonsense p.Arg507\*; missense p.Leu154Pro; or exon deletion) → **leads to** absent, truncated, or dysfunctional SPACR/IPM150 protein (loss-of-function / hypomorphic). *[Demonstrated genetically — PMID: 23993198]*
2. Loss of functional SPACR → **results in** failure of SEA-domain proteolytic maturation and loss of hyaluronan/chondroitin-sulfate binding, so the protein cannot assemble into the matrix. *[Demonstrated in vitro — PMID: 36109576, 15044457]*
3. Defective SPACR assembly → **disrupts** the chondroitin-sulfate–rich interphotoreceptor matrix glycocalyx that ensheaths rod and cone outer segments. *[Demonstrated — PMID: 32265257]*
4. **Branch A (developmental):** IPM disorganization during retinogenesis → **impairs** photoreceptor inner/outer-segment and connecting-cilium formation. *[Demonstrated in retinal organoids — PMID: 29777959]*
5. **Branch B (homeostatic/adult):** IPM disorganization and mislocalized matrix proteoglycan → **cause** accumulation of subretinal "vitelliform" material and separation/stress at the photoreceptor–RPE interface. *[Inferred from human imaging + supported by mouse mislocalization model — PMID: 32265257, 40315441]*
6. Subretinal deposit + outer-segment compromise → **produces** cone-predominant photoreceptor dysfunction and loss (cones affected more than RPE). *[Demonstrated by adaptive-optics imaging — PMID: 35900727]*
7. Progressive photoreceptor loss → **manifests** as adult-onset, bilateral, slowly progressive vitelliform maculopathy with moderate visual-acuity loss, metamorphopsia, and (in the broader spectrum) RP-like changes. *[Demonstrated clinically — PMID: 25085631, 32817297]*

```
 Biallelic IMPG1 LoF/hypomorphic variant
                │
                ▼
     Absent / dysfunctional SPACR (IPM150)
                │  (no SEA proteolysis; no HA/CS binding)
                ▼
     Disrupted interphotoreceptor-matrix glycocalyx
            ┌───────────────┴───────────────┐
            ▼                               ▼
  Branch A: impaired OS/cilium        Branch B: subretinal
  development (organoids)             vitelliform deposit +
            │                          matrix mislocalization
            └───────────────┬───────────────┘
                            ▼
          Cone-predominant photoreceptor dysfunction/loss
                            ▼
      Adult-onset, bilateral, progressive vitelliform maculopathy
                 (spectrum → RP-like degeneration)
```

**Upstream vs downstream:** The *IMPG1* mutation and SPACR dysfunction are the upstream lesion; IPM disorganization is the proximate intermediate; subretinal deposition and cone loss are downstream effectors of visual loss. **Cell types involved:** rod and cone photoreceptors (CL:0000573 retinal cone cell; CL:0000604 retinal rod cell), with the retinal pigment epithelium (CL:0002586) secondarily involved. **Anatomy (UBERON):** retina (UBERON:0000966), specifically the macula/fovea (UBERON:0005396 macula lutea) and the interphotoreceptor/subretinal space; photoreceptor outer segment (GO:0001750) and connecting cilium are the key subcellular sites. **Biological processes (GO):** extracellular matrix organization (GO:0030198), photoreceptor cell development/morphogenesis, visual perception (GO:0007601), glycosaminoglycan binding (GO:0005539). **Chemical entities (CHEBI):** chondroitin sulfate (CHEBI:37397), hyaluronic acid (CHEBI:16336).

A central interpretive point from the mouse work is that in the *Impg2*-null model, **mislocalized IMPG1** is pathogenic, whereas simple *Impg1* loss is tolerated in mouse. In humans, however, biallelic *IMPG1* variants clearly cause disease — implying either species differences in IPM redundancy or that human pathogenic alleles produce a mislocalized/dysfunctional product rather than a null state. This distinction matters for therapy: a pure gene-replacement approach assumes a loss-of-function target, which fits the human recessive LoF alleles but should be reconciled with the mislocalization mechanism.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [23993198](https://pubmed.ncbi.nlm.nih.gov/23993198/) | *Mutations in IMPG1 cause vitelliform macular dystrophies* | Human genetic | Defines causal gene; specific recessive variants; dual inheritance (F1, F4, F8) |
| [25085631](https://pubmed.ncbi.nlm.nih.gov/25085631/) | *Frequency and clinical pattern of VMD caused by IMPG1/IMPG2* | Human clinical cohort | Onset, acuity, rarity, EOG (F3, F8) |
| [32265257](https://pubmed.ncbi.nlm.nih.gov/32265257/) | *Proteoglycan IMPG2 shapes the IPM and modulates vision* | Review + mouse | IPM biology; Impg1-KO normal; mislocalization mechanism (F2, F5) |
| [36109576](https://pubmed.ncbi.nlm.nih.gov/36109576/) | *IMPG1/IMPG2 proteolyze in the SEA domain…* | In vitro | SEA-domain proteolysis; disease mutations inhibit it (F2) |
| [15044457](https://pubmed.ncbi.nlm.nih.gov/15044457/) | *Spacrcan binding to hyaluronan and other GAGs* | Biochemical | HA/CS binding function of SPACR (F2) |
| [29777959](https://pubmed.ncbi.nlm.nih.gov/29777959/) | *ECM expression in hPSC retinal organoids…* | In vitro (organoid) | Developmental role in OS/cilium/IPM formation (F7) |
| [32817297](https://pubmed.ncbi.nlm.nih.gov/32817297/) | *Pathogenic variants in IMPG1…* | Human genetic | IMPG1 variants associated with RP (F4) |
| [42321002](https://pubmed.ncbi.nlm.nih.gov/42321002/) | *IRD genes with dual inheritance: IRD-PT registry* | Human registry | Dual-inheritance concept; allele dosage modulation (F4) |
| [37440072](https://pubmed.ncbi.nlm.nih.gov/37440072/) | *Retinal metabolic profile in IMPG2-deficiency mice* | Mouse metabolomics | Energy-metabolism changes with subretinal lesions (F5) |
| [40315441](https://pubmed.ncbi.nlm.nih.gov/40315441/) | *Intrafamilial variability of IMPG1 vitelliform dystrophy* | Human clinical | Imaging; variable expressivity/modifiers (F6, F7) |
| [35900727](https://pubmed.ncbi.nlm.nih.gov/35900727/) | *Photoreceptor–RPE relationships in VMD by adaptive optics* | Human imaging | Cone-predominant loss distinguishing IMPG1/2 (F6) |
| [30688845](https://pubmed.ncbi.nlm.nih.gov/30688845/) | *Early-onset vitelliform dystrophy & p.Leu154Pro* | Human case | OCT outer-retinal disruption (F6) |

Supporting/context papers reviewed: IMPG2 genomic organization and candidacy [PMID: 11726612]; gene-discovery prevalence survey confirming IMPG1 as a rare VMD gene [PMID: 24702842]; RP25-locus candidate-gene analysis [PMID: 16354621]; additional AVMD case reports [PMID: 37661650].

**Consistency of the evidence:** Human genetic (23993198, 32817297), clinical/imaging (25085631, 40315441, 35900727, 30688845), in-vitro biochemistry (36109576, 15044457), organoid developmental biology (29777959), and mouse genetics/metabolomics (32265257, 37440072) converge on a single IPM-centered mechanism. The main internal tension is the discordant mouse Impg1-KO phenotype (normal) versus clear human disease, addressed in the Interpretation section.

---

## Section-by-Section Synthesis (Knowledge-Base Fields)

- **1. Disease information:** Rare autosomal-recessive macular/retinal dystrophy; MONDO:1040037; OMIM VMD4 616151; ICD-10 H35.5. Synonyms: IMPG1-related vitelliform macular dystrophy, autosomal-recessive VMD4, SPACR/IPM150 retinopathy. Evidence is from aggregated disease-level resources and published patient cohorts/case series, not EHR.
- **2. Etiology:** Purely genetic — biallelic *IMPG1* variants (splice, nonsense, missense, exon deletion). No environmental/infectious cause. Consanguinity facilitates recessive homozygous cases; IMPG1 is a dual-inheritance gene where allele dosage and variant location modulate phenotype. No established protective alleles or gene–environment interactions.
- **3. Phenotypes:** Decreased central visual acuity (HP:0000572 visual loss; HP:0007663 progressive macular degeneration), metamorphopsia, vitelliform macular lesion/subretinal deposits (HP:0011505 macular dystrophy), drusen-like deposits, outer-retinal (ellipsoid/interdigitation-zone) disruption, and in the broader spectrum pigmentary retinopathy (HP:0000510). Onset adult (4th decade), severity moderate (mean 20/40), course slowly progressive, bilateral. Quality-of-life impact is moderate — central/reading vision affected, peripheral vision/mobility relatively spared in the macular form.
- **4. Genetic/molecular:** Causal gene IMPG1 (HGNC:6055, Gene 3617). Recessive alleles: c.807+1G>T (splice), c.461T>C p.Leu154Pro (missense), c.1519C>T p.Arg507\* (nonsense), exon-7 deletion. Functional consequence: loss of function / hypomorphic with SEA-domain maturation defect. Modifiers inferred from intrafamilial variability. No epigenetic or chromosomal mechanisms described.
- **5. Environmental:** None established — monogenic disorder.
- **6. Mechanism:** See causal chain above (IPM proteoglycan loss → glycocalyx disruption → subretinal deposit + cone-predominant loss).
- **7. Anatomy:** Retina (UBERON:0000966), macula/fovea (UBERON:0005396); photoreceptor outer segment (GO:0001750) and interphotoreceptor/subretinal space; rod and cone photoreceptors (CL:0000604, CL:0000573); RPE secondarily (CL:0002586). Bilateral.
- **8. Temporal development:** Adult onset (~38–42 y), insidious/chronic, slowly progressive, lifelong; no remission; potential early window for intervention before photoreceptor loss.
- **9. Inheritance/population:** Autosomal recessive; ultra-rare (3/49 VMD families IMPG1-related); no sex predilection; carrier frequency not precisely established (ultra-rare). Penetrance appears high but expressivity variable.
- **10. Diagnostics:** Multimodal imaging (OCT subretinal vitelliform lesion, hyperautofluorescent on SW-FAF, cone-predominant loss on adaptive optics), normal/mildly reduced EOG, and molecular confirmation by IRD gene panel / WES / WGS / single-gene testing. Differential: BEST1 (abnormal EOG, RPE-predominant), PRPH2, and age-related macular degeneration.
- **11. Prognosis:** Chronic, slowly progressive central vision loss; no effect on survival; legal blindness uncommon but reading/driving vision commonly impaired.
- **12. Treatment:** No approved disease-specific therapy. Supportive low-vision rehabilitation (NCIT: Low Vision Aid / rehabilitation therapy). Gene-augmentation is a rational future strategy given biallelic LoF, but no IMPG1 trials exist.
- **13. Prevention:** No primary prevention. Genetic counseling, carrier/cascade testing, prenatal diagnosis, and preimplantation genetic testing are the relevant interventions.
- **14. Other species:** Mouse ortholog *Impg1* (Gene 63859; MGI:1926876); no major naturally occurring animal disease documented in the reviewed literature.
- **15. Model organisms:** *Impg1*-KO mouse (normal retina), *Impg2*-KO mouse (subretinal IMPG1 mislocalization/lesions), double-KO (normal); human iPSC-derived retinal organoids for developmental IPM studies.

---

## Limitations and Knowledge Gaps

- **Small evidence base.** The disease is ultra-rare; recessive genotype–phenotype correlations rest on a handful of families and individual case reports, limiting precision on penetrance, expressivity, and natural history.
- **Mouse–human discordance.** *Impg1*-KO mice are phenotypically normal, so there is no faithful recessive mouse model; the pathogenic mechanism in mouse is mislocalization (via *Impg2* loss), which may not fully recapitulate human IMPG1-null biology.
- **Overlap with IMPG2.** Much mechanistic and metabolomic detail derives from IMPG2 studies; direct IMPG1-specific functional data (beyond organoids and biochemistry) are limited.
- **Epidemiology unquantified.** No reliable prevalence/incidence or carrier-frequency estimates specific to recessive IMPG1 disease; gnomAD-based carrier calculations were not completed here.
- **Dominant vs recessive boundary.** As a dual-inheritance gene, the determinants (variant location, dosage, modifiers) that tip IMPG1 toward dominant vs recessive expression — and toward VMD vs RP — are incompletely defined.
- **No omics on human IMPG1 tissue.** Transcriptomic/proteomic/metabolomic profiling specific to human IMPG1 recessive retina is lacking.

---

## Proposed Follow-up Experiments / Actions

1. **Build a faithful IMPG1 recessive model** — generate knock-in mice (or retinal organoids) carrying human recessive alleles (e.g., p.Arg507\*, c.807+1G>T) to test whether human LoF produces subretinal deposits where the mouse Impg1-null does not, clarifying the mislocalization-vs-loss question.
2. **Genotype–phenotype registry** — aggregate IMPG1 recessive cases internationally (GeneMatcher/registry) with standardized OCT, FAF, adaptive optics, EOG/ERG and longitudinal acuity to define natural history and progression rate — essential endpoints for any future trial.
3. **Carrier-frequency/prevalence estimate** — mine gnomAD for biallelic-pathogenic burden of IMPG1 LoF alleles to estimate recessive disease prevalence and carrier frequency.
4. **SEA-domain functional assays** — systematically test recessive missense alleles (e.g., p.Leu154Pro) for SEA-domain proteolysis and HA/CS binding to classify VUS and refine ACMG scoring.
5. **Preclinical gene augmentation** — evaluate AAV-mediated IMPG1 delivery in the knock-in model, with attention to correct IPM targeting/maturation rather than mere expression.
6. **Modifier discovery** — exploit intrafamilial variability (identical-variant siblings with divergent phenotypes) via whole-genome sequencing to identify modifier loci (e.g., CD44, IMPG2) influencing expressivity.
7. **Differential-diagnosis biomarker** — validate the cone-predominant (vs RPE-predominant) adaptive-optics signature as a prospective classifier separating IMPG1/IMPG2 from BEST1/PRPH2 VMD.

---

*Evidence source legend: human clinical/genetic (23993198, 25085631, 32817297, 42321002, 40315441, 35900727, 30688845); in vitro/biochemical (36109576, 15044457); organoid developmental (29777959); mouse model (32265257, 37440072).*


## Artifacts

- [OpenScientist final report](IMPG1-related_Recessive_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IMPG1-related_Recessive_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1040037` (4 mentions) - the report calls it "Disease MONDO"; MONDO calls it **IMPG1-related recessive retinopathy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.