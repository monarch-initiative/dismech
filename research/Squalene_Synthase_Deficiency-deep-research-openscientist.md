---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T12:37:09.606156'
end_time: '2026-10-14T12:56:31.589765'
duration_seconds: 1161.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Squalene Synthase Deficiency
  mondo_id: MONDO:0032566
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
citation_count: 14
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0003231
    reported_labels:
    - organic aciduria family
    ontology_label: Hypertyrosinemia
  - term_id: HP:0012443
    reported_labels:
    - Structural brain malformations (nonspecific)
    ontology_label: Abnormal brain morphology
  - term_id: NCBITaxon:10116
    reported_labels:
    - Rattus norvegicus
    - Fdft1
    ontology_label: Rattus norvegicus
  labels_variant: 8
  obsolete_terms:
  - term_id: GO:0004310
    ontology_label: obsolete farnesyl-diphosphate farnesyltransferase activity
    replaced_by: GO:0051996
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Squalene_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Squalene_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Squalene Synthase Deficiency
- **MONDO ID:** MONDO:0032566 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Squalene Synthase Deficiency** covering all of the
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

# Squalene Synthase Deficiency — Comprehensive Disease Characterization Report

**Disease:** Squalene Synthase Deficiency (SQSD)
**MONDO ID:** MONDO:0032566 · **OMIM:** 618156 · **Gene:** *FDFT1* (farnesyl-diphosphate farnesyltransferase 1 / squalene synthase)
**Category:** Mendelian, autosomal recessive inborn error of cholesterol biosynthesis

---

## Summary

Squalene synthase deficiency (SQSD) is an ultra-rare autosomal recessive inborn error of the cholesterol (sterol) biosynthetic pathway caused by biallelic **hypomorphic** variants in *FDFT1*, the gene encoding squalene synthase (SS/SQS). Squalene synthase catalyzes the **first committed step** of cholesterol biosynthesis — the metal-dependent, head-to-head reductive condensation of two molecules of farnesyl pyrophosphate (FPP) into squalene, proceeding through a presqualene diphosphate (PSPP) intermediate. Because this step is the branch-point committing isoprenoid carbon to sterols, its disruption simultaneously (a) lowers downstream cholesterol synthesis and (b) diverts accumulating FPP into farnesol and its oxidation products. The disease was first defined clinically, biochemically, and molecularly by Coman and colleagues in 2018, who reported three affected individuals from two unrelated European families whose multisystem phenotype closely resembles **Smith-Lemli-Opitz syndrome (SLOS)**, the most common cholesterol biogenesis defect.

The clinical picture is congenital and severe: profound developmental delay, structural brain malformations, neonatal-onset generalized seizures, cortical visual impairment and optic nerve hypoplasia, facial dysmorphism, 2–3 toe cutaneous syndactyly, male genital malformations (cryptorchidism, hypospadias), and dry, markedly photosensitive skin. The biochemical hallmark is a **unique urinary organic-acid signature** of saturated and unsaturated branched-chain dicarboxylic acids and glucuronides derived from farnesol, accompanied by low total and LDL cholesterol. This profile localizes the metabolic block precisely to the squalene synthase step and is mirrored in individuals treated with pharmacologic squalene synthase inhibitors or dosed with farnesol.

Mechanistically, the best-supported causal model runs from biallelic hypomorphic *FDFT1* variants → reduced squalene synthase protein/activity → impaired embryonic cholesterol synthesis → defective cholesterol-dependent Sonic hedgehog (SHH) signaling → the SLOS-like pattern of CNS, limb, genital, and craniofacial malformations. The SHH limb of this chain is **inferred by analogy** to SLOS and to experimental cholesterol-deficiency models rather than directly demonstrated in *FDFT1*-deficient humans. Complete loss of squalene synthase is embryonic-lethal in mice (neural tube closure defects, death at ~E9.5–E12.5) and is not rescued by dietary squalene or cholesterol, which explains why viable human disease requires **partial-function (hypomorphic)** alleles that preserve residual activity. There is no disease-modifying therapy; management is entirely supportive, and HMG-CoA reductase inhibitors (statins) are mechanistically contraindicated.

---

## Key Findings

### Finding 1 — SQSD is an autosomal recessive cholesterol biosynthesis disorder caused by biallelic *FDFT1* variants and resembling SLOS

The disease-defining report (Coman et al., 2018, *American Journal of Human Genetics*) used whole-exome sequencing to identify recessive disease-causing variants in *FDFT1* in three individuals with "*profound developmental delay, brain abnormalities, 2-3 syndactyly of the toes, and facial dysmorphisms, resembling Smith-Lemli-Opitz syndrome, the most common cholesterol biogenesis defect*" [PMID: 29909962]. *FDFT1* encodes "*an evolutionarily conserved enzyme, squalene synthase (SS, farnesyl-pyrophosphate farnesyl-transferase 1), which catalyzes the first committed step in cholesterol biosynthesis.*" The plasma and urine metabolite profile localized the enzymatic block to the squalene synthase step, firmly establishing both the causal gene and the pathway-level lesion.

- **Evidence type:** Human clinical + molecular genetics (n=3, 2 families).
- **Ontology:** HGNC:3629 (*FDFT1*); MONDO:0032566; enzyme EC 2.5.1.21.

### Finding 2 — Squalene synthase catalyzes the first committed, metal-dependent head-to-head condensation of two FPP molecules via a presqualene diphosphate intermediate

Human squalene synthase crystal structures (Liu et al., 2014) establish that "*Squalene synthase (SQS) is a divalent metal-ion-dependent enzyme that catalyzes the two-step reductive 'head-to-head' condensation of two molecules of farnesyl pyrophosphate to form squalene using presqualene diphosphate (PSPP) as an intermediate*" [PMID: 24531458]. The enzyme uses NADPH and follows an ordered sequential mechanism. Two conserved aspartate-rich **DXXXD** motifs coordinate FPP through Mg²⁺, and conserved aromatic residues (e.g., Phe288/Phe286 in rat squalene synthase) are essential for the second (PSPP→squalene) half-reaction [PMID: 9575210]. Mechanistic studies of the homologous dehydrosqualene synthase CrtM show the primary carbocation forms PSPP, whose diphosphate then returns to the Mg²⁺ cluster for the second ionization [PMID: 21098670]. Squalene synthase is a C-terminally **tail-anchored ER membrane enzyme** whose insertion depends on the ER membrane protein complex (EMC): "*Insertion of the weakly hydrophobic tail-anchor (TA) of SQS into the ER membrane by the EMC ensures sufficient flux through the sterol biosynthetic pathway*" [PMID: 30578317].

- **Evidence type:** Structural biology, enzymology (human, rat, bacterial, in vitro).
- **Ontology:** GO:0004310 (farnesyl-diphosphate farnesyltransferase activity); GO:0006695 (cholesterol biosynthetic process); GO:0005789 (endoplasmic reticulum membrane); CHEBI: farnesyl diphosphate, presqualene diphosphate, squalene.

### Finding 3 — Complete squalene synthase loss is embryonic lethal with neural tube defects in mice; the enzyme is not rate-limiting

Tozawa et al. (1999) disrupted the mouse *Fdft1* (SS) gene. "*The mice homozygous for the disrupted SS gene (SS-/-) were embryonic lethal around midgestation. E9.5-10.5 SS-/- embryos exhibited severe growth retardation and defective neural tube closure*" and "*The lethal phenotype was not rescued by supplementing the dams either with dietary squalene or cholesterol*" [PMID: 10521476]. Heterozygotes were phenotypically normal despite ~50% reduced hepatic/testis SS activity and 60% lower hepatic SS mRNA, with unchanged hepatic cholesterol synthesis — "*indicating that SS is not a rate-limiting enzyme in the cholesterol biosynthetic pathway*." This is corroborated by Horvat et al. (2011): "*the absence of Fdft1 is lethal at E9.5-12.5 dpc*" [PMID: 21247357]. These data explain two central features of the human disease: heterozygous carriers are asymptomatic, and viable disease requires **partial-function alleles** that retain residual enzymatic flux.

- **Evidence type:** Mouse knockout, review.

### Finding 4 — Diagnostic biochemical hallmark: farnesol-derived branched-chain dicarboxylic aciduria with low total/LDL cholesterol

Coman et al. report a unique urine profile: increased saturated and unsaturated branched-chain dicarboxylic acids and glucuronides derived from farnesol, elevated plasma total farnesol, and low total and LDL cholesterol (squalene reduced or normal). "*The metabolite profile in plasma and urine suggested that their defect was at the level of squalene synthase*" [PMID: 29909962]. Mechanistically, the enzymatic block causes accumulation of the substrate FPP, which is dephosphorylated to **farnesol** then glucuronidated/hydroxylated/ω-oxidized to shorter branched-chain dicarboxylic acids detectable by urine organic-acid GC-MS and NMR spectroscopy. The identical profile occurs in people given pharmacologic squalene synthase inhibitors or dosed with farnesol, confirming the metabolic localization.

- **Evidence type:** Human clinical biochemistry + pharmacologic corroboration.
- **Ontology:** HP:0003231 (organic aciduria family); CHEBI: farnesol, dicarboxylic acid; HP:0003146 (hypocholesterolemia).

### Finding 5 — *FDFT1* pathogenic variants are hypomorphic non-coding/regulatory and splicing variants, not simple coding loss-of-function

Consistent with the essentiality of residual activity, the reported variants are **not** simple coding null alleles. Two affected siblings were compound heterozygous for a ~120-kb deletion encompassing *FDFT1* plus an intronic splice variant (c.880-24_880-23delinsAG) causing retention of 22 bases of intron 8 and a premature termination codon in exon 9 (predicted nonsense-mediated decay); minigene assays and fibroblast cDNA showed both normal and mis-spliced transcript (a **leaky/partial** splicing defect). A third, unrelated, non-consanguineous child was homozygous for a rare 16-bp deep-intronic deletion predicted to disrupt promoter/enhancer chromatin state, validated by luciferase reporter assay. "*Functional characterization of one variant demonstrated a partial splicing defect and altered promoter and/or enhancer activity, reflecting essential mechanisms for regulating cholesterol biosynthesis/uptake in steady state*" [PMID: 29909962]. Western blot showed markedly reduced SQS protein in patient cells, worsened in lipid-depleted media.

- **Evidence type:** Human molecular genetics + functional validation (minigene, luciferase, Western blot).
- **Implication:** Standard coding-exon sequencing may MISS these variants; WGS, CMA (for the CNV), and RNA/functional studies can be required.

### Finding 6 — Clinical spectrum

Integrating the primary report and the GeneReviews chapter (Coman, Pitt et al.; PMID: 32027475), features across the ~3 characterized individuals include:

| Phenotype | Suggested HPO term | Notes on onset/severity |
|---|---|---|
| Profound developmental delay / intellectual disability | HP:0012736 / HP:0002187 | Congenital; severe |
| Structural brain malformations (nonspecific) | HP:0012443 | Congenital |
| Generalized seizures | HP:0002197 | **Neonatal onset** |
| Cortical visual impairment | HP:0100704 | Congenital |
| Optic nerve hypoplasia | HP:0000609 | Congenital |
| Facial dysmorphism | HP:0001999 | Congenital |
| 2–3 toe cutaneous syndactyly | HP:0001770 | Congenital; shared with SLOS |
| Cryptorchidism (male) | HP:0000028 | Males |
| Hypospadias (male) | HP:0000047 | Males |
| Dry skin with photosensitivity | HP:0000958 / HP:0000992 | Severe; clinically significant sunburn within ~10 min of sun |
| Congenital heart defects | HP:0001627 | Reported/managed |
| Constipation | HP:0002019 | Managed |
| Spasticity | HP:0001257 | Managed |
| Low total & LDL cholesterol | HP:0003146 | Biochemical hallmark |

"*We report three individuals with profound developmental delay, brain abnormalities, 2-3 syndactyly of the toes, and facial dysmorphisms, resembling Smith-Lemli-Opitz syndrome*" [PMID: 29909962]. *FDFT1* is ubiquitously expressed, consistent with the multisystem pattern.

### Finding 7 — Diagnosis and differential diagnosis

Per GeneReviews (PMID: 32027475), diagnosis is established in a proband by (a) the characteristic urine organic-acid metabolites (GC-MS + NMR showing complex farnesol-derived branched-chain dicarboxylic acids/glucuronides), OR (b) identification of biallelic pathogenic *FDFT1* variants. Because the causal variants include deep-intronic/regulatory changes and a large CNV, coding-only testing may be insufficient; WGS/CMA and RNA studies may be needed. SQSD sits within the ~10 characterized Mendelian cholesterol biosynthesis disorders; four overlap clinically — **lanosterol synthase deficiency, lathosterolosis, Smith-Lemli-Opitz syndrome (DHCR7), and desmosterolosis (DHCR24)**. SQSD is differentiated by its **unique farnesol-derived dicarboxylic acid urine profile**; by contrast, SLOS shows elevated **7-dehydrocholesterol** [PMID: 20104611]. "*The metabolite profile in plasma and urine suggested that their defect was at the level of squalene synthase*" [PMID: 29909962].

### Finding 8 — Management is entirely supportive; statins contraindicated

GeneReviews states "*there are no specific disease-modifying treatments.*" Management is symptom-directed: anti-seizure medication for the neonatal generalized seizure disorder; standard treatment of congenital heart defects, constipation, cryptorchidism, hypospadias, and spasticity; feeding therapy / gastrostomy for dysphagia and poor growth; early-intervention developmental therapies (OT, PT, speech); visual stimulation for cortical visual impairment; behavioral support (ABA). **Rigorous sun protection is essential** because photosensitivity has produced clinically significant UV sunburns within ~10 minutes of direct sunlight. No approved pharmacotherapy, gene therapy, or enzyme/substrate replacement exists, and no SQSD clinical trials are registered. **Statins (HMG-CoA reductase inhibitors) are mechanistically contraindicated** because they act upstream and would further reduce already-impaired sterol flux.

### Finding 9 — Pathophysiology causal chain

See the Mechanistic Model section below. In brief: biallelic hypomorphic *FDFT1* variants → reduced SS activity → impaired embryonic cholesterol synthesis (plus FPP→farnesol diversion) → defective cholesterol-dependent Sonic hedgehog signaling → SLOS-like CNS/limb/genital/craniofacial malformations. The SHH limb is supported by: "*The protein SHH is expressed in the notochord of the CNS in the early embryo and is activated by being cleaved autocatalytically, with simultaneous covalent attachment of cholesterol to the N-terminal fragment*" [PMID: 15539288]; "*Limb, genital, CNS, and facial malformations result from gene/environment-induced cholesterol deficiency: further evidence for a link to sonic hedgehog*" [PMID: 9375918]; and "*They provide further evidence that cholesterol-deficiency-induced HPE originates from impaired Shh signaling activity in the ventral neural tube*" [PMID: 10564872].

### Finding 10 — Model organisms and comparative biology

| System | Organism / identifier | Key observation | PMID |
|---|---|---|---|
| Knockout mouse | *Mus musculus* (NCBITaxon:10090); *Fdft1*, Gene 14137 | Complete KO embryonic-lethal E9.5–10.5, neural tube defects, not rescued by dietary squalene/cholesterol; heterozygotes normal | 10521476; 21247357 |
| Natural rat model | *Rattus norvegicus* (NCBITaxon:10116); Shumiya cataract rat | Synergy of hypomorphic *Lss* + *Fdft1* alleles lowers lens cholesterol to ~57% of normal → hereditary cataract | 16440058; 33204712 |
| Cellular/in vitro | Patient fibroblasts, lymphoblasts; human cell lines | Reduced SQS protein; EMC-dependent SQS biogenesis | 29909962; 30578317 |
| Oncology (gain) | Human colon adenocarcinoma | FDFT1 upregulated, predicts poor prognosis, promotes tumor progression (synergy with SQLE) | 34939274 |

"*Hypomorphic mutations were identified in genes for lanosterol synthase (Lss) on chromosome 20 and farnesyl diphosphate farnesyl transferase 1 (Fdft1) on chromosome 15, both of which function in the cholesterol biosynthesis pathway*" and "*Cataract onset was associated with the specific combination of Lss and Fdft1 mutant alleles that decreased cholesterol levels in cataractous lenses to about 57% of normal*" [PMID: 16440058]. "*Squalene synthase (FDFT1) is an upstream enzyme of squalene epoxidase (SQLE) in cholesterol biosynthesis*" [PMID: 34939274]. **No viable mouse model of the human hypomorphic disease is yet reported — a key limitation.**

### Finding 11 — Epidemiology and inheritance

SQSD is inherited in an **autosomal recessive** manner (OMIM 618156; GeneReviews PMID: 32027475). Only ~3 affected individuals from 2 unrelated families of European descent have been reported (Coman 2018, PMID: 29909962); no formal prevalence/incidence has been established (ultra-rare). Onset is congenital/prenatal with neonatal presentation. Recurrence risk for carrier parents is the standard 25% affected / 50% carrier / 25% unaffected per pregnancy. Reported families were non-consanguineous; one proband was homozygous for a rare regulatory variant, two were compound heterozygous (120-kb deletion + intronic splice variant). Both sexes are affected (genital malformations noted in males; sex ratio not estimable at n~3). Pathogenic alleles are rare in gnomAD; complete-LoF *FDFT1* alleles are depleted (constraint), consistent with embryonic lethality of the biallelic null. Penetrance of biallelic hypomorphic genotypes appears complete; expressivity is relatively consistent and severe. "*Whole-exome sequencing was used to identify recessive disease-causing variants in FDFT1*" [PMID: 29909962].

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
(1) Biallelic HYPOMORPHIC FDFT1 variants (deep-intronic splice; promoter/
    enhancer regulatory deletion; 120-kb CNV)                     [PMID 29909962]
        │  leads to
        ▼
(2) Reduced squalene synthase protein & enzymatic activity
    (partial, not complete — complete loss is embryonic-lethal)   [PMID 10521476]
        │  results in failure to condense 2× FPP → squalene
        ▼
(3) BRANCH A: reduced de novo cholesterol synthesis      BRANCH B: FPP accumulates
    → low total & LDL cholesterol                         → dephosphorylated to farnesol
        │                                                  → ω-oxidation/glucuronidation
        │                                                  → branched-chain dicarboxylic
        │                                                     ACIDURIA (diagnostic marker)
        ▼                                                            [PMID 29909962]
(4) Embryonic cholesterol deficiency impairs covalent cholesterol
    modification & signaling of Sonic hedgehog (SHH)              [PMID 15539288]
        │  (INFERRED for SQSD by analogy to SLOS / cholesterol-deficiency models)
        ▼
(5) Impaired ventral neural-tube SHH signaling; loss of ventral
    midline cell populations/patterning                           [PMID 10564872, 9375918]
        │  leads to
        ▼
(6) SLOS-like MALFORMATIONS: structural brain malformation,
    profound developmental delay, cortical visual impairment /
    optic nerve hypoplasia, 2-3 toe syndactyly, male genital
    anomalies, facial dysmorphism, photosensitive dry skin        [PMID 29909962, 32027475]
```

**Upstream vs downstream.** The initiating molecular lesion (steps 1–2) and the immediate metabolic consequences (step 3) are **directly demonstrated** in patients. The SHH-mediated developmental steps (4–5) are **downstream and inferred** — robust for cholesterol deficiency in general (SLOS, teratogen models) but not yet shown directly in *FDFT1*-deficient human embryos.

**Pathways / processes / compartments (ontology suggestions).**
- Molecular pathway: cholesterol/sterol biosynthesis (KEGG hsa00100; Reactome "Cholesterol biosynthesis"); Sonic hedgehog signaling (Reactome "Hedgehog ligand biogenesis").
- GO biological process: GO:0016126 (sterol biosynthetic process), GO:0006695 (cholesterol biosynthetic process); GO:0007224 (smoothened signaling pathway) for the downstream developmental step.
- GO cellular component: GO:0005789 (ER membrane) — site of squalene synthase.
- Cell types (CL): ventral-midline neuroepithelial/neural cells (CL:0000031 neuroblast; CL:0002319 neural cell); hepatocytes (CL:0000182) and fibroblasts (CL:0000057) as sterol-synthesizing cells.
- Anatomy (UBERON): brain (UBERON:0000955), neural tube (UBERON:0001049), optic nerve (UBERON:0000941), skin (UBERON:0002097), external genitalia (UBERON:0000990), toes/autopod (UBERON:0002387).
- Chemicals (CHEBI): farnesyl diphosphate, presqualene diphosphate, squalene, farnesol, cholesterol, NADPH; cofactor Mg²⁺/Mn²⁺.

### Why the disease is hypomorphic, not null

The mouse knockout and the human genetics converge on one principle: **some squalene synthase activity is required for embryonic survival** because squalene/cholesterol cannot be supplied to the embryo from the diet (complete step-2/3 failure is lethal). The natural Shumiya cataract rat independently demonstrates that **partial *Fdft1* loss plus a second hit lowers tissue cholesterol enough to cause organ-specific disease** (lens cholesterol ~57% of normal → cataract), providing comparative support for a dose-dependent cholesterol-deficiency mechanism.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [29909962](https://pubmed.ncbi.nlm.nih.gov/29909962/) | *Squalene Synthase Deficiency: Clinical, Biochemical, and Molecular Characterization* | Human clinical/molecular | Disease-defining paper: gene, inheritance, phenotype, biomarker, variant types |
| [32027475](https://pubmed.ncbi.nlm.nih.gov/32027475/) | *Squalene Synthase Deficiency* (GeneReviews) | Clinical review | Diagnosis, differential, management, inheritance |
| [24531458](https://pubmed.ncbi.nlm.nih.gov/24531458/) | *Structural insights into catalytic mechanism of human squalene synthase* | Structural biology | Enzyme mechanism, Mg²⁺ dependence, PSPP intermediate |
| [30578317](https://pubmed.ncbi.nlm.nih.gov/30578317/) | *ER membrane protein complex promotes biogenesis of sterol enzymes* | Cell biology | SQS is EMC-dependent tail-anchored ER enzyme |
| [9575210](https://pubmed.ncbi.nlm.nih.gov/9575210/) | *Function-structure studies of rat hepatic squalene synthase* | Enzymology | Conserved Asp/aromatic residues; two half-reactions |
| [21098670](https://pubmed.ncbi.nlm.nih.gov/21098670/) | *Mechanism of action and inhibition of dehydrosqualene synthase* | Structural/enzymology | Head-to-head mechanism, PSPP chemistry |
| [10521476](https://pubmed.ncbi.nlm.nih.gov/10521476/) | *Embryonic lethality and defective neural tube closure in mice lacking squalene synthase* | Mouse KO | Complete loss embryonic-lethal; SS not rate-limiting |
| [21247357](https://pubmed.ncbi.nlm.nih.gov/21247357/) | *Defects in cholesterol synthesis genes in mouse and humans* | Review | *Fdft1* loss lethal E9.5–12.5; statin teratogenicity context |
| [16440058](https://pubmed.ncbi.nlm.nih.gov/16440058/) | *Lanosterol synthase mutations cause cataracts in Shumiya cataract rat* | Rat natural model | Hypomorphic *Fdft1*+*Lss* lowers cholesterol → cataract |
| [33204712](https://pubmed.ncbi.nlm.nih.gov/33204712/) | *Differential gene expression in Shumiya cataract rat lens* | Rat model | Confirms cholesterol-deficiency cataract mechanism |
| [34939274](https://pubmed.ncbi.nlm.nih.gov/34939274/) | *Squalene synthase predicts poor prognosis in colon adenocarcinoma* | Human oncology | Contrasting gain-of-expression role of FDFT1 |
| [15539288](https://pubmed.ncbi.nlm.nih.gov/15539288/) | *The function of cholesterol in embryogenesis* | Review | Cholesterol required for SHH activation |
| [10564872](https://pubmed.ncbi.nlm.nih.gov/10564872/) | *Absence of ventral cell populations in rat SLOS model* | Rat model | Cholesterol deficiency → impaired ventral SHH → HPE |
| [9375918](https://pubmed.ncbi.nlm.nih.gov/9375918/) | *Limb, genital, CNS, facial malformations from cholesterol deficiency* | Model/teratogen | Same malformation pattern via cholesterol/SHH |
| [20104611](https://pubmed.ncbi.nlm.nih.gov/20104611/) | *Cyclopia in SLOS* | Human case | SLOS differential (elevated 7-DHC); SHH-HPE severity |

**Convergence.** The human report (29909962), the GeneReviews synthesis (32027475), the enzymology/structural papers (24531458, 9575210, 21098670, 30578317), the mouse/rat models (10521476, 21247357, 16440058, 33204712), and the cholesterol–SHH developmental literature (15539288, 10564872, 9375918, 20104611) form a self-consistent model. **No retrieved paper contradicts** the core claims; the principal uncertainty is that the SHH limb has not been directly tested in *FDFT1*-deficient human tissue.

---

## Section-by-Section Summary (template coverage)

- **1. Disease information:** AR inborn error of cholesterol biosynthesis; OMIM 618156, MONDO:0032566, gene *FDFT1*. Synonyms: SQSD, squalene synthase deficiency, farnesyl-diphosphate farnesyltransferase 1 deficiency, SS deficiency. Information is disease-level/aggregated from ~3 individual patients.
- **2. Etiology:** Genetic — biallelic hypomorphic *FDFT1* variants. No environmental cause; no established protective factors. Gene–environment note: lipid-depleted conditions further reduce SQS protein in patient cells (29909962). Statin exposure in pregnancy is a relevant teratogenic analogue (21247357).
- **3. Phenotypes:** see Finding 6 table with HPO terms, onset (congenital/neonatal), severity (severe), progression (static congenital malformations), frequency (qualitative given n~3). Severe QoL impact: profound disability.
- **4. Genetic/molecular:** *FDFT1* (HGNC:3629, chr 15); variant classes = deep-intronic splice (NMD), regulatory promoter/enhancer deletion, 120-kb CNV; all germline, hypomorphic (partial LoF); rare in gnomAD; complete LoF depleted. No established human modifier genes (second-hit modifier shown in rat). No disease-specific epigenetic data.
- **5. Environmental:** None established; infectious agents N/A.
- **6. Mechanism:** see Mechanistic Model (causal chain; GO/CL/UBERON/CHEBI terms).
- **7. Anatomy:** brain/neural tube (UBERON:0000955/0001049), eye/optic nerve, skin, external genitalia, toes; ER subcellular compartment (GO:0005789); malformations largely bilateral.
- **8. Temporal:** congenital onset; static structural malformations; chronic lifelong; neonatal seizures; critical window = embryogenesis (sterol/SHH-dependent patterning).
- **9. Inheritance/population:** AR; ultra-rare (~3 individuals, 2 families, European); complete penetrance of biallelic hypomorphic genotype; standard 25% recurrence risk.
- **10. Diagnostics:** urine organic-acid GC-MS + NMR (farnesol-derived dicarboxylic acids/glucuronides); plasma farnesol ↑; total/LDL cholesterol ↓; molecular testing via multigene cholesterol-biosynthesis panel / WES / WGS / CMA / RNA studies. Differential: SLOS (7-DHC↑), lathosterolosis, desmosterolosis, lanosterol synthase deficiency.
- **11. Prognosis:** severe, lifelong profound disability; no formal survival data; no disease-modifying therapy.
- **12. Treatment:** supportive only (anti-seizure meds, cardiac/urologic/orthopedic management, feeding/gastrostomy, developmental therapies, sun protection); statins contraindicated. NCIT: supportive care; anticonvulsant therapy.
- **13. Prevention:** genetic counseling, carrier/cascade testing, prenatal/preimplantation testing for known familial variants; rigorous sun protection as tertiary prevention of UV injury.
- **14. Other species:** mouse *Fdft1* (Gene 14137, NCBITaxon:10090) — embryonic-lethal KO; rat *Fdft1* (NCBITaxon:10116) — Shumiya cataract natural model. No companion-animal natural disease reported; not zoonotic.
- **15. Model organisms:** embryonic-lethal mouse KO (no viable hypomorphic model yet); Shumiya cataract rat (partial-loss natural model); patient fibroblasts/lymphoblasts; EMC-biogenesis cell systems. Key limitation: no model recapitulating the full human hypomorphic multisystem phenotype.

---

## Limitations and Knowledge Gaps

1. **Extremely small sample (n≈3, 2 families).** All clinical/biochemical/molecular claims rest largely on a single defining report (29909962) plus its GeneReviews synthesis. Frequencies, penetrance, expressivity, and sex ratio are not statistically estimable.
2. **No prevalence/incidence data.** The disease is ultra-rare with no registry.
3. **SHH mechanism is inferred, not demonstrated in SQSD.** Steps 4–5 of the causal chain are supported only by analogy to SLOS and cholesterol-deficiency models; direct SHH assays in *FDFT1*-deficient human embryonic tissue are lacking.
4. **No viable animal model of the hypomorphic human disease.** Complete-null mice die in utero; a hypomorphic/conditional mouse recapitulating the human phenotype has not been reported.
5. **No omics (transcriptomics/proteomics/broad metabolomics), no QoL instruments, no natural-history/survival data.**
6. **No therapeutics.** No approved or trial-stage disease-modifying treatment; no registered clinical trials.

---

## Proposed Follow-up Experiments / Actions

1. **Case finding & registry.** Deploy the characteristic urine organic-acid signature (farnesol-derived branched-chain dicarboxylic acids) as a biochemical screen across undiagnosed SLOS-like cohorts and metabolic biobanks to identify additional patients and enable natural-history study.
2. **Deep-intronic/regulatory variant discovery.** Reanalyze coding-negative SLOS-like cases with WGS + RNA-seq + CMA, since pathogenic *FDFT1* alleles are frequently non-coding (deep-intronic splice, promoter/enhancer, CNV).
3. **Direct test of the SHH limb.** Generate patient-derived iPSCs and neural-tube/organoid or hypomorphic/conditional mouse models; quantify SHH processing (cholesterol-adducted N-terminal fragment), ventral patterning markers (Shh, Otx2), and sterol content to convert the inferred mechanism (steps 4–5) into direct evidence.
4. **Hypomorphic mouse model.** Engineer knock-in of a human-equivalent leaky splice or regulatory allele (or conditional partial knockdown) to obtain a viable model recapitulating the multisystem phenotype for mechanism and preclinical therapeutics.
5. **Sterol-supplementation proof-of-concept.** Evaluate whether postnatal dietary/pharmacologic cholesterol supplementation (as trialed in SLOS) offers any benefit; define biomarkers (plasma farnesol, cholesterol, urinary dicarboxylic acids) as pharmacodynamic endpoints.
6. **Variant functional pipeline.** Standardize minigene splice assays and promoter/enhancer luciferase reporters for *FDFT1* VUS classification per ACMG/AMP.

---

*Report compiled from 12 confirmed findings and 25 reviewed papers over 5 investigation iterations. Evidence sources are labeled by type (human clinical, model organism, in vitro, computational/structural). Direct abstract quotations are reproduced verbatim and attributed by PMID.*


## Artifacts

- [OpenScientist final report](Squalene_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Squalene_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003231` (1 mention) - the report calls it "organic aciduria family"; HP calls it **Hypertyrosinemia**
- `HP:0012443` (1 mention) - the report calls it "Structural brain malformations (nonspecific)"; HP calls it **Abnormal brain morphology**
- `NCBITaxon:10116` (2 mentions) - the report calls it "Rattus norvegicus", "Fdft1"; NCBITaxon calls it **Rattus norvegicus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004310` (obsolete farnesyl-diphosphate farnesyltransferase activity) (1 mention) - replaced by `GO:0051996`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004310` (1 mention) - the report calls it "farnesyl-diphosphate farnesyltransferase activity"; GO calls it **obsolete farnesyl-diphosphate farnesyltransferase activity**
- `GO:0005789` (3 mentions) - the report calls it "endoplasmic reticulum membrane", "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `HP:0003146` (2 mentions) - the report calls it "hypocholesterolemia", "Low total & LDL cholesterol"; HP calls it **Hypocholesterolemia**
- `HP:0100704` (1 mention) - the report calls it "Cortical visual impairment"; HP calls it **Cerebral visual impairment**, and lists "Cortical visual impairment" among its other names
- `HP:0001770` (1 mention) - the report calls it "2–3 toe cutaneous syndactyly"; HP calls it **Toe syndactyly**
- `HP:0000028` (1 mention) - the report calls it "Cryptorchidism (male)"; HP calls it **Cryptorchidism**
- `HP:0000047` (1 mention) - the report calls it "Hypospadias (male)"; HP calls it **Hypospadias**
- `HP:0001627` (1 mention) - the report calls it "Congenital heart defects"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005789` - called "endoplasmic reticulum membrane", "ER membrane"
- `HP:0003146` - called "hypocholesterolemia", "Low total & LDL cholesterol"
- `NCBITaxon:10116` - called "Rattus norvegicus", "Fdft1"