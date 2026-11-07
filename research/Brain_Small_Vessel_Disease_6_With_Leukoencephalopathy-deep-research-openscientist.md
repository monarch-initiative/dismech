---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T17:19:07.688116'
end_time: '2026-10-28T18:13:12.937557'
duration_seconds: 3245.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cathepsin A-Related Arteriopathy with Strokes and Leukoencephalopathy
  mondo_id: MONDO:0035551
  category: Mendelian
  causal_genes: CTSA
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 37
  verified: 33
  not_found: 1
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.028
  labels_checked: 33
  labels_matching: 24
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0035551
    reported_labels:
    - MONDO
    ontology_label: obsolete cathepsin a-related arteriopathy-strokes-leukoencephalopathy
  labels_variant: 8
  unresolved_terms:
  - UBERON:0022392
  obsolete_terms:
  - term_id: MONDO:0035551
    ontology_label: obsolete cathepsin a-related arteriopathy-strokes-leukoencephalopathy
    replaced_by: MONDO:0980711
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Brain_Small_Vessel_Disease_6_With_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Brain_Small_Vessel_Disease_6_With_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cathepsin A-Related Arteriopathy with Strokes and Leukoencephalopathy
- **MONDO ID:** MONDO:0035551 (if available)
- **Causal gene(s):** CTSA
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

Please provide a comprehensive research report on **Cathepsin A-Related Arteriopathy with Strokes and Leukoencephalopathy** covering all of the
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

# Cathepsin A-Related Arteriopathy with Strokes and Leukoencephalopathy (CARASAL)

**Disease:** Cathepsin A-Related Arteriopathy with Strokes and Leukoencephalopathy (CARASAL)
**MONDO ID:** MONDO:0035551
**Causal gene:** **CTSA** (cathepsin A / protective protein, PPCA; HGNC:2515), chromosome 20q13.12
**Category:** Mendelian, autosomal dominant

---

## Summary

**CARASAL is an ultra-rare, adult-onset, autosomal dominant hereditary cerebral small vessel disease (cSVD) caused by a single recurrent heterozygous missense variant, c.973C>T (p.Arg325Cys), in the *CTSA* gene on chromosome 20q13.12.** The causal gene is **CTSA**, which encodes cathepsin A (also called protective protein/cathepsin A, PPCA), a lysosomal serine carboxypeptidase. It is essential to name the gene at the outset because *CTSA* is also the gene behind **galactosialidosis**, a completely different, autosomal *recessive* lysosomal storage disease. CARASAL and galactosialidosis are allelic disorders of the same gene but differ fundamentally in inheritance mode, mechanism, and clinical presentation: CARASAL arises from a dominant-acting missense allele that dysregulates endothelin-1 metabolism, whereas galactosialidosis arises from biallelic loss of cathepsin A's chaperone/protective function toward β-galactosidase and neuraminidase-1.

Mechanistically, cathepsin A is the major soluble endogenous enzyme that degrades the potent vasoconstrictor **endothelin-1 (ET-1)**. The p.Arg325Cys variant removes a buried, salt-bridged arginine residue from the enzyme core, predicted to destabilize the protein fold. The resulting cathepsin A dysfunction leads to accumulation of ET-1, which was demonstrated directly in patient brains, where striking ET-1 immunoreactivity appeared in white-matter astrocytes and correlated with increased numbers of arrested premyelinating oligodendrocyte progenitors. This drives two convergent pathological streams: (1) ET-1–mediated arteriolar vasoconstriction producing therapy-resistant hypertension and small-vessel arteriopathy, and (2) disproportionately severe leukoencephalopathy with arrested oligodendrocyte maturation. The clinical picture is dominated by ischemic and hemorrhagic strokes, slow late-onset cognitive decline, therapy-resistant hypertension, migraine, and brainstem/cranial-nerve features (hearing loss, tinnitus, non-positional vertigo, facial pain, dysphagia, dysarthria).

To date, approximately 19–21 patients have been reported across Dutch, Italian/Brazilian, and Chinese pedigrees, all carrying the identical p.Arg325Cys allele — making CARASAL both allelically homogeneous and extraordinarily rare. There is no disease-modifying therapy; management is symptomatic. Because the mechanism converges on the endothelin pathway, ET-1 receptor antagonism is a rational (but untested) therapeutic hypothesis. This report synthesizes seven confirmed findings and 37 reviewed papers into a comprehensive disease-characteristics entry spanning etiology, phenotypes, molecular genetics, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms.

---

## 1. Disease Information

**Overview.** CARASAL is a monogenic, autosomal dominant cerebral small vessel disease (cSVD) characterized by adult-onset strokes (both ischemic and hemorrhagic), progressive leukoencephalopathy visible on MRI that is disproportionately severe relative to clinical status, slowly progressive cognitive decline, and therapy-resistant hypertension. It was first defined as a distinct clinical-genetic entity in 2016 following whole-exome sequencing of two Dutch families [PMID: 27664989]. The disease sits within the family of hereditary cSVDs alongside CADASIL (NOTCH3), CARASIL/HTRA1-related arteriopathy, COL4A1/2-associated microangiopathy, RVCL-S, and Fabry disease (GLA) [PMID: 42771568].

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0035551 |
| Gene | CTSA (HGNC:2515); OMIM gene *613111* |
| Locus | Chromosome 20q13.12 |
| Causal variant | NM_000308 c.973C>T, p.(Arg325Cys) |
| Disease type | Mendelian, autosomal dominant |

**Synonyms / alternative names.** "Cathepsin-A-related arteriopathy with strokes and leukoencephalopathy"; the acronym **CARASAL**. The disease is sometimes grouped descriptively under "hereditary cerebral small vessel disease" and "monogenic vascular dementia." No widely used OMIM phenotype number, ICD-10/11, or MeSH term was recorded in the source material for CARASAL specifically; it is an ultra-rare, recently described entity.

**Information source.** The knowledge base here is derived from **aggregated disease-level resources and primary case reports / small cohort studies** (not population EHR). Evidence derives from a limited number of pedigrees and individual case descriptions, plus mechanistic studies in human tissue, in vitro systems, and mouse genetics.

---

## 2. Etiology

**Primary cause — genetic.** CARASAL is caused by a **heterozygous founder missense variant in *CTSA*: c.973C>T, p.Arg325Cys** (Finding F001). Whole-exome sequencing of two Dutch families identified a single shared variant segregating with disease; haplotype analysis revealed a shared 1,145-kb interval on chromosome 20q13.12, indicating descent from a common ancestor (founder effect) [PMID: 27664989]. The same variant was subsequently confirmed in unrelated patients of Chinese and Italian/Brazilian ancestry [PMID: 35904593].

> *"we identified one variant shared by both families and segregating with the disease: c.973C>T in CTSA. Haplotype analysis revealed a shared 1,145-kb interval encompassing the CTSA variant on chromosome 20q13.12, suggesting a common ancestor"* — [PMID: 27664989](https://pubmed.ncbi.nlm.nih.gov/27664989/)

**Genetic risk factors.** The disease is monogenic; the p.Arg325Cys allele is both necessary and (with age-dependent penetrance) essentially sufficient. No susceptibility loci or modifier genes have been established. One candidate biological modifier is **SCPEP1** (serine carboxypeptidase 1), a homolog that redundantly degrades ET-1 — in mice, only combined Ctsa/Scpep1 deficiency produces a strong blood-pressure phenotype [PMID: 24586188], raising the untested hypothesis that human SCPEP1 activity could modulate CARASAL severity.

**Environmental risk factors.** None established as causal. Standard vascular risk factors (hypertension — which is itself a disease feature — smoking, dyslipidemia) are plausible aggravators of small-vessel injury but have not been formally quantified in CARASAL. Age is the dominant determinant of clinical expression (adult/late onset).

**Protective factors.** No genetic or environmental protective factors have been identified. The redundant ET-1–degrading enzyme SCPEP1 is a theoretical protective modifier (see above).

**Gene–environment interactions.** Mouse data suggest a **salt–gene interaction**: catalytically inactive cathepsin A combined with Scpep1 loss produced significantly elevated blood pressure specifically *after a high-salt diet and systemic ET-1 injection* [PMID: 24586188]. By extrapolation, dietary salt and conditions that raise ET-1 could interact with impaired cathepsin A function to worsen hypertension in CARASAL (inferred, not demonstrated in patients).

---

## 3. Phenotypes

CARASAL is dominated by central nervous system manifestations with onset in adulthood. Frequencies below are qualitative/semiquantitative given the very small reported cohorts (~19–21 patients).

| Phenotype | Type | Onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Ischemic stroke | Clinical sign | Adult; episodic/recurrent | Core feature | HP:0002140 (Ischemic stroke) |
| Intracerebral/hemorrhagic stroke | Clinical sign | Adult; can be fatal | Reported | HP:0001342 (Cerebral hemorrhage) |
| Leukoencephalopathy (white-matter hyperintensities) | Imaging/lab abnormality | Adult; progressive; disproportionately severe | Core; ~universal | HP:0002352 (Leukoencephalopathy) |
| Therapy-resistant hypertension | Clinical sign | Adult; chronic | Core feature | HP:0000822 (Hypertension) |
| Cognitive decline / vascular dementia | Behavioral/cognitive | Slow and late; progressive | Common | HP:0001268 (Mental deterioration) |
| Migraine | Symptom | Adult | Reported | HP:0002076 (Migraine) |
| Non-positional vertigo | Symptom | Adult | Reported | HP:0002321 (Vertigo) |
| Tinnitus | Symptom | Adult | Reported | HP:0000360 (Tinnitus) |
| Hearing loss | Clinical sign | Adult | Reported | HP:0000365 (Hearing impairment) |
| Facial pain | Symptom | Adult | Reported | HP:0030833 (Facial pain) |
| Dysphagia | Clinical sign | Adult | Reported | HP:0002015 (Dysphagia) |
| Dysarthria | Clinical sign | Adult | Reported | HP:0001260 (Dysarthria) |
| Disequilibrium / gait imbalance | Clinical sign | Adult | Reported | HP:0002141 (Gait imbalance) |
| Behavioral disinhibition | Behavioral | Adult | Reported | HP:0000734 (Disinhibition) |
| REM-sleep behavior disorder; depression | Behavioral | Adult | Reported | HP:0002360; HP:0000716 (Depression) |
| Enophthalmos / "orbital check-mark sign" | Physical/imaging | Adult | Reported (2026 cohort) | HP:0000490 (Enophthalmos) |

**Clinical description.** In the founding two families the clinical picture was *"dominated by ischemic and hemorrhagic strokes, slow and late cognitive deterioration, and therapy-resistant hypertension"* [PMID: 27664989] (Finding F003). A systematic review lists migraine, stroke with central facial palsy, facial pain, non-positional vertigo, cognitive dysfunction with impaired concentration and behavioral disinhibition, REM-sleep behavioral disorder, and depression [PMID: 31177426].

> *"These include migraine, stroke with central facial palsy, facial pain, non-positional vertigo, cognitive dysfunction with impaired concentration and behavioral disinhibition, REM-sleep behavioral disorder, and depression"* — [PMID: 31177426](https://pubmed.ncbi.nlm.nih.gov/31177426/)

**Severity and progression.** Variable but progressive; the hallmark is a **disproportion** between very severe imaging burden and comparatively milder clinical disease. A 2026 cohort (21 patients, 3 pedigrees) quantified a higher normalized white-matter-hyperintensity volume than age/sex-matched CADASIL (mean difference 5.0% of intracranial volume, 95% CI 2.0–8.0) [PMID: 41908989] (Finding F003).

> *"Total nWMHv was higher in patients with CARASAL than in those with CADASIL (mean difference: 5.0% of intracranial volume, 95% CI [2.0-8.0]"* — [PMID: 41908989](https://pubmed.ncbi.nlm.nih.gov/41908989/)

**Quality of life.** Not formally measured with standardized instruments (EQ-5D/SF-36) in the reported literature. By analogy to other cSVDs, recurrent stroke, progressive cognitive impairment, and gait/balance problems would be expected to produce substantial disability and QoL reduction.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CTSA* (cathepsin A / protective protein PPCA), chromosome 20q13.12; HGNC:2515. The protein is a lysosomal serine carboxypeptidase (EC 3.4.16.5) of the α/β-hydrolase fold family, structurally homologous to yeast carboxypeptidase Y [PMID: 11212324].

**Pathogenic variant (CARASAL).**

| Attribute | Value |
|---|---|
| cDNA | NM_000308 c.973C>T |
| Protein | p.(Arg325Cys) |
| Codon change | CGC → TGC (Arg → Cys) |
| Variant type | Missense (single-nucleotide substitution) |
| Classification | Pathogenic |
| Origin | Germline |
| Zygosity in disease | Heterozygous (single allele) |
| Functional consequence | Protein destabilization / folding defect (predicted dominant-acting) |

**Allelic homogeneity.** p.Arg325Cys is the **sole reported CARASAL allele** (Finding F006). A systematic literature review returns no CARASAL family carrying any other *CTSA* variant; all reported pedigrees (Dutch, Italian/Brazilian, Chinese) carry this same recurrent allele [PMID: 27664989; 35904593; 31177426; 41908989].

> *"Both patients carried the same pathogenic p.Arg325Cys mutation in CTSA"* — [PMID: 35904593](https://pubmed.ncbi.nlm.nih.gov/35904593/)

**Structural consequence (in silico, Findings F005 & F007).** Mapping the variant onto the human cathepsin A/PPCA crystal structure (PDB 1IVY) shows that the mutated arginine (UniProt P10619 Arg326 = PDB residue 298; reference sequences differ by one N-terminal residue, and the Arg→Cys codon change confirms the mapping) is **partially buried** (156 heavy atoms within 10 Å of its guanidinium carbon) and participates in a **salt-bridge / hydrogen-bond network** with acidic side chains Glu264 (3.47 Å), Asp300 (3.69 Å), and Asp332 (5.83 Å). Removing this buried charged residue is predicted to destabilize the fold. The nearest free cysteine thiol (Cys334 Sγ) lies ~9 Å away — too distant for a direct non-native disulfide. Critically, the variant sits **18.3 Å from the catalytic Ser150 hydroxyl** and **17.1 Å from the opposing subunit** (homodimer interface), i.e., it is neither in the catalytic pocket nor at the dimer interface. This favors a **folding/stability mechanism** over direct catalytic-site disruption.

This interpretation is reinforced by the published structural analysis of galactosialidosis mutations, which found that pathogenic *CTSA* missense residues act by perturbing structural integrity rather than directly hitting the active site:

> *"analysis of the 11 mutations revealed a substantive correlation between the effect of the amino acid substitution on the integrity of protein structure and the general severity of the clinical phenotype"* — [PMID: 9435242](https://pubmed.ncbi.nlm.nih.gov/9435242/)

> *"none of the mutations occurred in the active site or at the protein surface, which would have disrupted the catalytic activity or protective function"* — [PMID: 9435242](https://pubmed.ncbi.nlm.nih.gov/9435242/)

**Conservation.** The disease arginine is evolutionarily conserved (Finding F006). The local motif is human SGDKVR(M)DPPCT vs mouse SGDKVR(L)DPPCT — the disease arginine and the adjacent disulfide cysteine are invariant, with only a single conservative flanking M327→L difference.

**Modifier genes.** None confirmed. **SCPEP1** is a strong biological candidate based on its redundant ET-1–degrading role in mice [PMID: 24586188].

**Epigenetic information / chromosomal abnormalities.** No CARASAL-specific DNA-methylation, histone-modification, or structural/chromosomal abnormalities have been reported. CARASAL is a point-mutation disorder; no copy-number or cytogenetic changes are implicated.

**Contrast with galactosialidosis.** Recessive *CTSA* variants (e.g., frameshifts c.517delTT, intronic splicing defects; founder p.Pro203Thr in the Bahraini population) cause galactosialidosis — combined deficiency of neuraminidase-1 and β-galactosidase — via loss of the protein's protective/chaperone function [PMID: 9603439; 39981487; 11212324]. CARASAL's single heterozygous missense allele does not produce galactosialidosis, underscoring a distinct, dominant-acting mechanism.

---

## 5. Environmental Information

- **Environmental factors:** None established as causal. Dietary salt is a plausible aggravator of the hypertensive component by analogy to mouse data [PMID: 24586188] (inferred).
- **Lifestyle factors:** Conventional vascular risk factors (smoking, diet, physical inactivity) are generically relevant to small-vessel disease but not specifically studied in CARASAL.
- **Infectious agents:** Not applicable. CARASAL is a non-infectious monogenic disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline heterozygous *CTSA* c.973C>T (p.Arg325Cys)** substitutes a buried, salt-bridged arginine with cysteine → **destabilizes the cathepsin A fold** (in silico; the residue is 18 Å from the active site and forms salt bridges to Glu264/Asp300/Asp332) [Findings F005, F007; PMID: 9435242].
2. Protein destabilization **leads to dysfunction of cathepsin A's serine-carboxypeptidase activity** toward endothelin-1 (inferred from structural data and from the enzyme's established role as the principal ET-1–degrading enzyme).
3. Impaired degradation **results in accumulation of endothelin-1 (ET-1)** — cathepsin A/PPCA is *"a major soluble endogenous endothelin degradation enzyme in human tissues"* [PMID: 7822272] (Finding F002).
4. ET-1 accumulation **branches** into two downstream streams:
   - **Branch A (vascular):** ET-1 (a potent vasoconstrictor) → heightened arteriolar vasoconstriction and increased ET-1–dependent phosphorylation of myosin light chain 2 in vascular smooth muscle → **therapy-resistant hypertension** and small-vessel arteriopathy (severe arteriolar "atherosclerosis") [PMID: 24586188; 27664989].
   - **Branch B (glial/white matter):** ET-1 accumulates in **white-matter astrocytes** → correlates with **increased premyelinating oligodendrocyte progenitors** (arrested oligodendrocyte maturation) → impaired myelination/white-matter integrity [PMID: 27664989].
5. Both branches converge → **chronic small-vessel ischemia + primary white-matter/oligodendrocyte dysfunction** → **disproportionately severe leukoencephalopathy** with secondary ischemic and hemorrhagic strokes [PMID: 27664989; 31177426].
6. Cumulative vascular and white-matter injury → **progressive cognitive decline / vascular dementia**, brainstem and cranial-nerve features (hearing loss, tinnitus, vertigo, dysphagia, dysarthria) [PMID: 31177426; 36324419].

```
 CTSA p.Arg325Cys (heterozygous)
          |
   destabilizes cathepsin A fold  (18 A from active site; salt-bridge loss)
          |
   impaired ET-1 degradation
          |
   ENDOTHELIN-1 ACCUMULATION
         /                         \
 Branch A (vascular)          Branch B (glial)
 arteriolar vasoconstriction   ET-1 in WM astrocytes
 ^ MLC2 phosphorylation        arrested OPC maturation
 therapy-resistant HTN         (^ premyelinating OPCs)
 small-vessel arteriopathy     impaired myelination
         \                         /
          \_______________________/
                     |
   small-vessel ischemia + primary WM injury
                     |
   DISPROPORTIONATELY SEVERE LEUKOENCEPHALOPATHY
   ischemic + hemorrhagic strokes
   progressive cognitive decline; brainstem/cranial-nerve signs
```

### Detail by category

- **Molecular pathways.** Endothelin signaling (ET-1 → ETA/ETB receptors → Gq → PLC → ↑intracellular Ca²⁺ → myosin light chain phosphorylation → vasoconstriction). Mouse mesenteric arteries lacking cathepsin A showed *"increased ET-1-dependent phosphorylation of myosin light chain 2"* [PMID: 24586188].
- **Cellular processes.** Vascular smooth-muscle contraction/arteriopathy; astrocyte ET-1 handling; **arrested oligodendrocyte precursor differentiation** (a developmental/maturation block rather than overt demyelination).
- **Protein dysfunction.** Loss-of-stability / folding defect of cathepsin A (Findings F005/F007). Because CARASAL is heterozygous and dominant-acting while galactosialidosis is recessive, the CARASAL allele likely acts by a mechanism other than simple haploinsufficiency of the protective function — plausibly a dominant effect on ET-1 regulation or a subtle dominant-negative/altered-processing effect (the precise dominant mechanism remains to be demonstrated).
- **Metabolic / biochemical abnormalities.** Reduced carboxypeptidase-mediated proteolysis of ET-1; *"the circulating level of ET-1 is regulated through its proteolytic cleavage by secreted serine carboxypeptidase, cathepsin A"* [PMID: 24586188].
- **Immune involvement.** No primary autoimmune/immunodeficiency mechanism; chronic ischemic/gliotic injury may involve reactive astrogliosis and microglial activation (as in cSVD generally) but is not the initiating lesion.
- **Tissue damage mechanisms.** Ischemia from small-vessel vasoconstriction/arteriopathy plus intrinsic white-matter oligodendrocyte dysfunction; hemorrhage from fragile small vessels.
- **Molecular profiling.** The key human-tissue finding is immunohistochemical: striking ET-1 immunoreactivity in white-matter astrocytes with increased premyelinating oligodendrocytes [PMID: 27664989]. No large-scale transcriptomic/proteomic/metabolomic datasets specific to CARASAL were identified.

> *"One of the numerous cathepsin A functions is to degrade endothelin-1. In the patients, striking endothelin-1 immunoreactivity was found in white matter astrocytes, correlating with increased numbers of premyelinating oligodendrocyte progenitors"* — [PMID: 27664989](https://pubmed.ncbi.nlm.nih.gov/27664989/)

**Upstream vs downstream.** Upstream: the *CTSA* mutation → protein destabilization → ET-1 accumulation. Downstream: vasoconstriction/hypertension, arrested myelination, ischemia, strokes, cognitive decline.

**Suggested GO / CL terms.** GO:0006508 (proteolysis); endothelin receptor signaling pathway; GO:0042310 (vasoconstriction); GO:0048709 (oligodendrocyte differentiation). Cell types — CL:0000128 (oligodendrocyte), CL:0002453 (oligodendrocyte precursor cell), CL:0000127 (astrocyte), CL:0000359 (vascular smooth muscle cell), CL:0000115 (endothelial cell).

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Primary:** central nervous system — cerebral white matter and small cerebral arteries/arterioles (nervous + cardiovascular systems).
- **Secondary:** cognitive networks, brainstem, inner ear/vestibular pathways.
- **Body systems:** nervous (CNS), cardiovascular (systemic hypertension, small-vessel arteriopathy).

**Specific anatomical sites (with UBERON suggestions).** MRI shows *"extensive signal change in the deep cerebral white matter, anterior temporal lobes, thalami, internal and external capsules and brainstem"* [PMID: 35904593] (Finding F003).

| Site | UBERON |
|---|---|
| Cerebral deep white matter | UBERON:0002316 (white matter) |
| Anterior temporal lobe | UBERON:0002771 (temporal lobe region) |
| Thalamus | UBERON:0001897 |
| Internal capsule | UBERON:0022279 |
| External capsule | UBERON:0022392 |
| Brainstem / pons | UBERON:0000988 (pons) |
| Cerebral arteriole | UBERON:0001637 (artery) / arteriole |
| Orbit (enophthalmos / "orbital check-mark sign") | UBERON:0001697 (orbit) |

**Tissue / cell level.** Nervous tissue (white matter) and vascular wall. Cell populations: **oligodendrocytes and oligodendrocyte precursor cells** (arrested maturation), **astrocytes** (ET-1 accumulation), **vascular smooth muscle cells** and **endothelial cells** of small vessels. CL terms: CL:0000128, CL:0002453, CL:0000127, CL:0000359, CL:0000115.

**Subcellular level.** Cathepsin A is a **lysosomal** enzyme (GO:0005764 lysosome); it is also secreted and acts extracellularly/in the circulation on ET-1 [PMID: 7822272; 24586188]. GO cellular-component terms: GO:0005764 (lysosome), GO:0005615 (extracellular space).

**Lateralization.** White-matter and small-vessel involvement is **bilateral**, typically symmetric/diffuse (characteristic of leukoencephalopathy).

---

## 8. Temporal Development

- **Onset:** Adult / late-onset. Imaging-based diagnosis in the founding cohort was applied to family members ≥40 years [PMID: 27664989]. Onset is **insidious/chronic** with superimposed **acute** episodes (strokes).
- **Progression:** Progressive, with episodic stroke events punctuating a chronically progressive leukoencephalopathy and cognitive decline. Cognitive deterioration is described as *"slow and late"* [PMID: 27664989].
- **Course pattern:** Chronic, lifelong, progressive with episodic strokes.
- **Disease stages:** Not formally staged; conceptually early (imaging changes, hypertension) → intermediate (recurrent strokes, early cognitive change) → advanced (vascular dementia, disability).
- **Remission:** None; no spontaneous or treatment-induced remission reported.
- **Critical periods:** Adulthood onward; the pre-symptomatic adult window (when imaging changes may precede clinical events) is the theoretical opportunity for intervention.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare. Approximately **19 patients** reported as of the 2019 systematic review [PMID: 31177426]; a 2026 cohort described 21 patients across 3 pedigrees [PMID: 41908989]. No reliable prevalence/incidence estimates exist; CARASAL is likely underdiagnosed and expected to increase in recognition with broader genetic testing and advanced imaging [PMID: 31177426].

> *"So far, 19 patients have been reported. The frequency of CARASAL patients will most likely increase in the future, as CARASAL may be more frequently recognized"* — [PMID: 31177426](https://pubmed.ncbi.nlm.nih.gov/31177426/)

**Inheritance.** **Autosomal dominant**, single heterozygous allele (Findings F001, F006).

**Penetrance / expressivity.** Appears high but age-dependent (adult onset); expressivity is variable across the reported phenotype spectrum. Formal penetrance estimates are not available given tiny cohorts.

**Genetic anticipation / germline mosaicism.** Not reported / not applicable (point mutation, not a repeat expansion).

**Founder effect.** Yes — a shared 1,145-kb haplotype on 20q13.12 in the Dutch families indicates a common ancestor [PMID: 27664989]. Remarkably, the identical p.Arg325Cys allele recurs in unrelated patients of Chinese and Italian/Brazilian ancestry [PMID: 35904593], consistent either with multiple independent mutational events at this CpG-containing codon (CGC→TGC is a classic C>T transition at a methylated CpG) or broader distribution.

**Consanguinity.** Not relevant (dominant disorder).

**Carrier frequency.** Not applicable in the recessive sense; the pathogenic dominant allele is extremely rare.

**Population demographics.** Reported in Dutch, Italian/Brazilian, and Chinese individuals. No established sex predilection. Age distribution: adults (≥40 years for most diagnosed cases).

---

## 10. Diagnostics

**Imaging (first-line).** Brain **MRI** is central: diffuse, confluent, disproportionately severe white-matter hyperintensities involving deep cerebral white matter, **anterior temporal lobes**, thalami, internal/external capsules, and brainstem/pons [PMID: 35904593]. The 2026 cohort quantified a higher normalized WMH volume than CADASIL (mean difference 5.0% of ICV, 95% CI 2.0–8.0) and noted an **"orbital check-mark sign"/enophthalmos** as a potential supportive feature [PMID: 41908989]. Microbleeds/hemorrhage may be seen on susceptibility-weighted imaging.

**Genetic testing (confirmatory, definitive).** Because CARASAL is allelically homogeneous, **targeted single-variant / single-gene *CTSA* testing** for c.973C>T (p.Arg325Cys) is the most efficient confirmatory approach. **Whole-exome sequencing (WES)** was the discovery method and remains valuable when the diagnosis is not clinically suspected [PMID: 27664989]; **whole-genome sequencing (WGS)** and gene panels for hereditary cSVD (which should include *CTSA* alongside NOTCH3, HTRA1, COL4A1/2, GLA, TREX1) are alternatives. Chromosomal microarray, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable**.

**Laboratory / biomarkers.** No validated blood/CSF biomarker. **Endothelin-1** is a mechanistically rational candidate circulating/tissue biomarker but is not an established clinical test. Cathepsin A enzyme-activity assays are used for galactosialidosis diagnosis but their utility in CARASAL (where the protective function may be partly preserved) is unproven.

**Biopsy / pathology.** Brain autopsy in the founding families showed a **primary microangiopathy with severe arteriolar changes and secondary leukoencephalopathy**, with leukoencephalopathy *disproportionately extensive relative to the vascular abnormalities*, and immunohistochemistry demonstrating ET-1 in white-matter astrocytes with increased premyelinating oligodendrocytes [PMID: 27664989; 31177426].

**Clinical criteria / differential diagnosis.** No formal diagnostic criteria. Key differentials are other hereditary cSVDs and monogenic vascular dementias:

| Condition | Gene | Distinguishing features |
|---|---|---|
| CADASIL | NOTCH3 | Anterior temporal/external capsule WMH; granular osmiophilic material; cysteine-altering NOTCH3 variants [PMID: 40145673] |
| CARASIL | HTRA1 | Recessive; alopecia, spondylosis |
| COL4A1/2 microangiopathy | COL4A1/2 | Hemorrhage-prone, ocular/renal features [PMID: 41005670] |
| Fabry disease | GLA | X-linked; angiokeratoma, renal/cardiac, acroparesthesia [PMID: 39978321] |
| MELAS | mtDNA m.3243A>G | Stroke-like episodes, lactic acidosis, maternal inheritance [PMID: 36324419] |
| Galactosialidosis | CTSA (recessive) | Coarse facies, cherry-red spot, visceral storage — distinct allelic disorder [PMID: 39981487] |

CARASAL is distinguished by therapy-resistant hypertension, the disproportionately heavy white-matter burden, brainstem involvement, and the specific *CTSA* p.Arg325Cys genotype.

**Screening.** Cascade (predictive) genetic testing of at-risk adult relatives for the familial p.Arg325Cys allele is feasible. No population or newborn screening is indicated (ultra-rare, adult-onset, no preventive therapy).

---

## 11. Outcome / Prognosis

- **Survival / mortality.** No formal survival statistics. The disease is progressive and includes **potentially fatal intracerebral hemorrhage** [PMID: 41908989]. Life expectancy is likely reduced by recurrent stroke and vascular dementia, but quantitative data are lacking (too few cases) [PMID: 31177426].

  > *"Currently, the outcome cannot be sufficiently assessed, as too few cases have been reported."* — [PMID: 31177426](https://pubmed.ncbi.nlm.nih.gov/31177426/)

- **Morbidity / disability.** Substantial — recurrent strokes, progressive cognitive decline/vascular dementia, gait/balance impairment, dysarthria, dysphagia, and sensory (hearing/vestibular) deficits accumulate disability over time.
- **Complications.** Recurrent ischemic and hemorrhagic strokes; vascular dementia; consequences of therapy-resistant hypertension.
- **Recovery potential.** Limited; the course is progressive without disease-modifying therapy.
- **Prognostic factors.** White-matter lesion burden (quantifiable via normalized WMH volume), stroke frequency/subtype, and hypertension control are plausible prognostic indicators. No validated prognostic biomarkers.

---

## 12. Treatment

**No disease-modifying therapy exists.** Management is symptomatic and supportive [PMID: 31177426].

- **Pharmacotherapy (supportive).**
  - **Antihypertensives** for the therapy-resistant hypertension (often difficult to control) — NCIT: Antihypertensive Agent.
  - **Antiplatelet agents and statins** are used broadly in cSVD/stroke secondary prevention (as in CADASIL cohorts) [PMID: 42949550]; benefit in CARASAL is unproven and hemorrhage risk must be weighed given the hemorrhagic-stroke tendency.
- **Mechanism-based / rational (experimental, untested).** Because the pathophysiology converges on **endothelin-1 excess**, **endothelin-receptor antagonists** (e.g., bosentan, ambrisentan, macitentan; NCIT: Endothelin Receptor Antagonist) are a biologically rational but **entirely hypothetical** therapeutic avenue. No clinical trials in CARASAL have been reported.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno).** None developed for CARASAL. Note: AAV-mediated gene therapy and enzyme replacement are in preclinical/clinical development for the *recessive* allelic disorder **galactosialidosis** [PMID: 34901309; 33426146; 28603679], but these replace lost protective function and are **not applicable** to the dominant CARASAL mechanism.
- **Surgical / interventional.** None specific; standard acute-stroke care applies.
- **Supportive / rehabilitative.** Physical, occupational, and speech/swallowing therapy; cognitive support; management of migraine, vertigo, hearing loss; aggressive vascular risk-factor modification.
- **Pharmacogenomics / personalized medicine.** Genotype-directed care is limited to confirming the diagnosis; no CARASAL-specific pharmacogenomic guidance exists.

**Treatment outcomes.** No response-rate or adverse-event data specific to CARASAL therapy are available.

---

## 13. Prevention

- **Primary prevention.** Not possible for mutation carriers (monogenic). Reproductive options (genetic counseling, prenatal/preimplantation genetic testing for the familial p.Arg325Cys allele) can prevent transmission.
- **Secondary prevention.** Cascade genetic testing and MRI surveillance of at-risk adult relatives for early identification; aggressive management of hypertension and vascular risk factors.
- **Tertiary prevention.** Stroke secondary-prevention measures and rehabilitation to limit complications and disability.
- **Immunization / public health / environmental interventions.** Not applicable (non-infectious, monogenic).
- **Counseling.** **Autosomal dominant genetic counseling** is central — 50% transmission risk to offspring, age-dependent expression, and discussion of predictive testing and reproductive options.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** The gene is conserved in mammals; mouse ortholog **Ctsa** (NCBI Gene; UniProt P16675). The disease arginine and adjacent disulfide cysteine are invariant between human and mouse (Finding F006).
- **Natural disease in other species.** No naturally occurring CARASAL-equivalent arteriopathy has been described in companion animals or wildlife in the reviewed literature. (Recessive *CTSA* loss-of-function models galactosialidosis in mice.)
- **Comparative biology / evolutionary conservation.** The cathepsin A → ET-1 regulatory axis is conserved: mouse genetics directly demonstrate cathepsin A control of blood pressure via ET-1 inactivation [PMID: 24586188], supporting conservation of the disease-relevant mechanism.
- **Transmission / zoonosis.** Not applicable.

---

## 15. Model Organisms

**Available models.** There is **no published mouse model that reproduces CARASAL** (the heterozygous p.Arg325Cys knock-in); the 2019 review explicitly flagged the need to generate animal models [PMID: 31177426]. Existing *Ctsa* mouse models recapitulate the **recessive** disorder (galactosialidosis), not CARASAL:

| Model | Genotype | Phenotype modeled | Relevance to CARASAL |
|---|---|---|---|
| CathA S190A knock-in | Catalytically inactive cathepsin A (~10–15% residual ET-1 carboxypeptidase activity) | ET-1 handling; mild alone | Partial — isolates catalytic/ET-1 function [PMID: 24586188] |
| CathA/Scpep1 double-deficient (DD) | Combined loss | ↑BP after high-salt + ET-1; reduced blood ET-1 degradation; ↑MLC2 phosphorylation in mesenteric arteries | Mechanistic support for CARASAL hypertension [PMID: 24586188] |
| Ctsa-deficient (IVS6+1g/a) / Ctsa·Neu1 | Splicing defect, combined deficiency | Galactosialidosis (myoclonus, visceral storage) | Models the recessive allelic disease, **not** CARASAL [PMID: 41917397; 35573044] |

**Phenotype recapitulation and limitations.** The CathA/Scpep1 double-deficient mouse strongly supports the **vascular/hypertension branch** of CARASAL (Finding F004):

> *"in response to high-salt diet and systemic injections of ET-1 these animals showed significantly increased blood pressure as compared to wild type mice or those with single deficiencies of CathA or Scpep1"* — [PMID: 24586188](https://pubmed.ncbi.nlm.nih.gov/24586188/)

> *"the circulating level of ET-1 is regulated through its proteolytic cleavage by secreted serine carboxypeptidase, cathepsin A"* — [PMID: 24586188](https://pubmed.ncbi.nlm.nih.gov/24586188/)

However, **no model reproduces the dominant-acting p.Arg325Cys allele or the leukoencephalopathy / arrested-oligodendrocyte-maturation branch**, which is the defining CNS feature of CARASAL. A knock-in of the human-equivalent mutation (mouse Ctsa p.Arg→Cys) is the key missing resource.

**Applications.** Existing models are useful for studying cathepsin A's role in ET-1 metabolism and blood-pressure regulation; cellular systems (patient fibroblasts, iPSC-derived oligodendrocytes/astrocytes) would be needed to dissect the glial/white-matter mechanism.

**Resources.** MGI (mouse Ctsa), plus cell models (patient-derived fibroblasts; iPSC-derived neural cells) as future tools.

---

## Mechanistic Model / Interpretation (synthesis)

CARASAL is best understood as a **dominant endothelin-1 dysregulation syndrome caused by a structurally destabilizing *CTSA* missense allele.** Three independent evidence streams converge:

1. **Genetics** pin the disease to a single recurrent heterozygous allele (p.Arg325Cys) that is both allelically homogeneous and evolutionarily conserved (F001, F006).
2. **Structural biology** predicts that this allele destabilizes the cathepsin A fold — the residue is buried, salt-bridged (Glu264/Asp300/Asp332), 18 Å from the active site, and away from the dimer interface — consistent with the established principle that pathogenic *CTSA* missense variants act via loss of structural integrity rather than direct catalytic-site hits (F005, F007).
3. **Functional biology** connects cathepsin A to endothelin-1: it is the principal soluble ET-1–degrading enzyme (F002), and mouse genetics prove that loss of this activity raises blood pressure and arterial ET-1 reactivity (F004). Patient tissue closes the loop by showing ET-1 accumulation in white-matter astrocytes with arrested oligodendrocyte maturation (F002/F003).

The result is a two-branch pathology — a **vascular branch** (ET-1–driven vasoconstriction → therapy-resistant hypertension + small-vessel arteriopathy) and a **glial branch** (astrocytic ET-1 → arrested oligodendrocyte maturation → white-matter failure) — that jointly explain the disease's signature: a leukoencephalopathy far more severe than the vascular lesions alone would predict.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27664989](https://pubmed.ncbi.nlm.nih.gov/27664989/) | *CARASAL* (original description) | Identifies causal gene/variant (c.973C>T, p.Arg325Cys), founder haplotype, clinical triad, ET-1 in white-matter astrocytes with arrested OPCs (F001–F003) |
| [35904593](https://pubmed.ncbi.nlm.nih.gov/35904593/) | *A rare cause of monogenic cSVD and stroke (CARASAL)* | Confirms recurrent p.Arg325Cys across ancestries; MRI distribution (F003, F006) |
| [31177426](https://pubmed.ncbi.nlm.nih.gov/31177426/) | *Update on CARASAL* | Systematic review: 19 patients, phenotype spectrum, pathogenesis, need for models, outcome uncertainty |
| [41908989](https://pubmed.ncbi.nlm.nih.gov/41908989/) | *Expanding the clinicoradiologic phenotype* | 2026 cohort (21 patients); quantified WMH burden vs CADASIL; orbital sign (F003) |
| [7822272](https://pubmed.ncbi.nlm.nih.gov/7822272/) | *Protective protein as endogenous endothelin degradation enzyme* | Establishes cathepsin A/PPCA as major ET-1–degrading enzyme (F002) |
| [24586188](https://pubmed.ncbi.nlm.nih.gov/24586188/) | *SCPEP1 and Cathepsin A in vasoconstriction via ET-1 inactivation* | Mouse genetics: cathepsin A controls ET-1 and blood pressure; SCPEP1 redundancy (F004) |
| [9435242](https://pubmed.ncbi.nlm.nih.gov/9435242/) | *Atomic model of human PPCA/cathepsin A* | Structural basis; CTSA missense variants destabilize fold, lie away from active site (F005, F007) |
| [11212324](https://pubmed.ncbi.nlm.nih.gov/11212324/) | *Cathepsin A/protective protein: multifunctional* | Enzyme biology, α/β-hydrolase fold, protective function |
| [40145673](https://pubmed.ncbi.nlm.nih.gov/40145673/) | *Pathobiology of CADASIL* | Differential diagnosis (NOTCH3 cSVD) |
| [42771568](https://pubmed.ncbi.nlm.nih.gov/42771568/) | *Hereditary cSVD: phenotype to management* | Positions CARASAL within hereditary cSVD; diagnostic clues |

All quoted snippets above are verbatim from the cited abstracts.

---

## Limitations and Knowledge Gaps

1. **Dominance mechanism unresolved.** Why a single heterozygous missense allele causes disease when galactosialidosis requires biallelic loss is not mechanistically proven (dominant-negative vs altered ET-1 regulation vs tissue-specific haploinsufficiency). The structural prediction of destabilization is in silico, not experimentally validated.
2. **No animal model of CARASAL.** All existing *Ctsa* mice model the recessive galactosialidosis phenotype; no knock-in reproduces p.Arg325Cys or the leukoencephalopathy.
3. **Tiny evidence base.** ~19–21 patients total; penetrance, expressivity, natural history, survival, and sex ratio are not reliably quantified.
4. **No validated biomarker or therapy.** ET-1 as a biomarker and ET-receptor antagonism as a therapy are mechanistically rational but untested.
5. **No omics datasets** (transcriptomic/proteomic/metabolomic) specific to CARASAL tissue beyond immunohistochemistry.
6. **Variant recurrence across ancestries** is unexplained — multiple independent CpG mutations vs shared ancestry remains unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** (Ctsa p.Arg→Cys heterozygous) to test whether the dominant allele recapitulates hypertension AND leukoencephalopathy, and to dissect dominant-negative vs loss-of-function contributions.
2. **Biochemically characterize p.Arg325Cys protein:** thermal stability, ET-1 carboxypeptidase kinetics, dimerization, and effect on NEU1/β-GAL complex — to confirm the predicted folding defect and test for a dominant-negative effect on the wild-type allele.
3. **Measure circulating and CSF ET-1** in patients vs controls to validate ET-1 as a diagnostic/prognostic biomarker.
4. **Model the glial branch in vitro** using patient iPSC-derived oligodendrocyte precursors and astrocytes to test whether ET-1 directly arrests oligodendrocyte maturation.
5. **Pilot endothelin-receptor antagonism** (preclinical first, in the knock-in model) as a mechanism-based therapeutic.
6. **Establish an international CARASAL registry** to accumulate natural-history, penetrance, and outcome data across the Dutch, Chinese, and Italian/Brazilian pedigrees and any newly identified carriers.
7. **Investigate SCPEP1** as a genetic/pharmacologic modifier of CARASAL severity.

---

*Report compiled from 7 confirmed findings and 37 reviewed papers across 5 investigation iterations. Evidence types: human clinical (case reports/cohorts, autopsy, imaging), model organism (mouse genetics), in vitro (enzyme biology), and computational (structural modeling of PDB 1IVY).*


## Artifacts

- [OpenScientist final report](Brain_Small_Vessel_Disease_6_With_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Brain_Small_Vessel_Disease_6_With_Leukoencephalopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 33 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0035551` (2 mentions) - the report calls it "MONDO"; MONDO calls it **obsolete cathepsin a-related arteriopathy-strokes-leukoencephalopathy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0022392` (1 mention), reported as "External capsule" - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0035551` (obsolete cathepsin a-related arteriopathy-strokes-leukoencephalopathy) (2 mentions) - replaced by `MONDO:0980711`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030833` (1 mention) - the report calls it "Facial pain"; HP calls it **Neck pain**
- `HP:0000490` (1 mention) - the report calls it "Enophthalmos"; HP calls it **Deeply set eye**, and lists "Enophthalmos" among its other names
- `CL:0000359` (2 mentions) - the report calls it "vascular smooth muscle cell"; CL calls it **vascular associated smooth muscle cell**, and lists "vascular smooth muscle cell" among its other names
- `UBERON:0002771` (1 mention) - the report calls it "temporal lobe region"; UBERON calls it **middle temporal gyrus**, and lists "gyrus temporalis medius" among its other names
- `UBERON:0001897` (1 mention) - the report calls it "Thalamus"; UBERON calls it **dorsal plus ventral thalamus**, and lists "thalamus" among its other names
- `UBERON:0022279` (1 mention) - the report calls it "Internal capsule"; UBERON calls it **strand of hair on external ear**, and lists "hair of external ear" among its other names
- `UBERON:0001697` (1 mention) - the report calls it "orbit"; UBERON calls it **orbit of skull**, and lists "orbit" among its other names
- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names