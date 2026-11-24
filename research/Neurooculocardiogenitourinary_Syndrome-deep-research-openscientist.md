---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T18:12:32.262068'
end_time: '2026-11-05T18:32:27.590769'
duration_seconds: 1195.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurooculocardiogenitourinary Syndrome
  mondo_id: MONDO:0032850
  category: Mendelian
  causal_genes: WDR37
  omim_id: OMIM:618652
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 10
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:41279321
  - PMID:39031646
  relevance_assessed: 15
  on_topic: 11
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 41
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 17
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0032850
    reported_labels:
    - MONDO
    ontology_label: neurooculocardiogenitourinary syndrome
  - term_id: GO:0005737
    reported_labels:
    - GO cellular component:** cytoplasm
    ontology_label: cytoplasm
  - term_id: CL:0000540
    reported_labels:
    - CL cell types:** neuron
    ontology_label: neuron
  labels_variant: 7
  unresolvable_prefixes:
  - NCBIGene
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurooculocardiogenitourinary_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurooculocardiogenitourinary_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurooculocardiogenitourinary Syndrome
- **MONDO ID:** MONDO:0032850 (if available)
- **Causal gene(s):** WDR37
- **OMIM:** OMIM:618652
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurooculocardiogenitourinary Syndrome** covering all of the
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

# Neurooculocardiogenitourinary Syndrome (NOCGUS) — Comprehensive Disease Report

**Disease:** Neurooculocardiogenitourinary Syndrome (NOCGUS)
**Causal gene:** **WDR37** (WD repeat–containing protein 37; HGNC:31406; NCBIGene:22884; Ensembl ENSG00000047056; UniProt Q9Y2I8)
**OMIM:** #618652 · **MONDO:** 0032850 · **Orphanet:** 684305 · **DOID:** 0111675 · **GARD:** 0027365 · **UMLS:** C5231443 · **MedGen:** 1684841

---

## Summary

**Neurooculocardiogenitourinary syndrome (NOCGUS) is a rare, severe, autosomal-dominant multisystem developmental disorder caused by de novo missense variants (and rare splice variants) that cluster in the conserved N-terminal region upstream of the WD40 repeat domain of the *WDR37* gene** (chromosome 10p13; protein UniProt Q9Y2I8, 494 amino acids with seven WD40 repeats). The disorder was defined simultaneously in 2019 by two independent cohorts — Reis et al. (*American Journal of Human Genetics*) and Kanca et al. — who reported unrelated probands with de novo variants in a narrow N-terminal mutational hotspot. The name "neurooculocardiogenitourinary" is an acronym for the four organ systems most consistently involved: the **nervous system** (epilepsy, intellectual disability, absent speech, cerebellar hypoplasia), the **eye** (coloboma, microphthalmia, Peters/anterior-segment anomalies), the **heart** (septal defects), and the **genitourinary tract** (cryptorchidism, renal dysplasia).

The clinical picture is defined by near-universal epilepsy, global developmental delay/intellectual disability with absent speech, a recognizable facial gestalt reminiscent of CHARGE syndrome, and the hallmark ocular feature of **coloboma**. Severity is highly variable, ranging from infantile lethality with complex multisystem malformation at one extreme to milder developmental delay at the other. Mechanistically, WDR37 is a binding partner of the phosphofurin acidic cluster sorting proteins **PACS1** and **PACS2**; the WDR37–PACS1–PACS2 axis governs intracellular protein trafficking and endoplasmic-reticulum (ER) calcium handling. NOCGUS, PACS1 (Schuurs-Hoeijmakers) syndrome, and PACS2 syndrome form an overlapping clinical-molecular spectrum sharing epilepsy, intellectual disability, cerebellar atrophy, distinctive facies, and coloboma.

Importantly, population constraint data and model-organism genetics argue that NOCGUS does **not** arise from simple haploinsufficiency. *WDR37* is constrained against loss-of-function (gnomAD LOEUF 0.412, pLI 0.57), all pathogenic alleles are clustered de novo missense (not truncating), and a Drosophila *wdr37* null is homozygous viable. Mutant WDR37 protein is correctly localized but expressed at reduced levels, favoring a gain-of-function or dominant-negative mechanism. There is currently no disease-modifying therapy; management is entirely supportive and multidisciplinary.

---

## Section 1 — Disease Information

**Overview.** NOCGUS is a congenital, autosomal-dominant, multisystemic malformation/neurodevelopmental syndrome. The acronym reflects the organ systems named in the disorder: **neuro** (brain/seizures/cognition), **oculo** (eye), **cardio** (heart), and **genitourinary** (kidneys, genitalia). Kanca et al. summarized the neurodevelopmental core as "epilepsy, colobomas, facial dysmorphology reminiscent of CHARGE syndrome, developmental delay and intellectual disability, and cerebellar hypoplasia" ([PMID: 31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #618652 |
| MONDO | MONDO:0032850 |
| Orphanet | 684305 |
| Disease Ontology (DOID) | 0111675 |
| GARD | 0027365 |
| UMLS | C5231443 |
| MedGen | 1684841 |
| Causal gene | WDR37 (HGNC:31406; NCBIGene:22884; Ensembl ENSG00000047056; UniProt Q9Y2I8) |

**Synonyms / alternative names.** Official abbreviation **NOCGUS**; "WDR37 syndrome"; "WDR37-related disorder"; "WDR37-associated neurooculocardiogenitourinary syndrome." No synonyms were originally recorded in the source template; the above are established in the literature and MONDO cross-references.

**Source of information.** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, HPO) and from **individual-patient case reports/case series** published in the primary literature (Reis 2019, Kanca 2019, Hay 2020, and subsequent single-case reports). This is an ultra-rare disorder with an estimated <60 published patients; all knowledge is case-based rather than from EHR-scale or registry cohorts.

---

## Section 2 — Etiology

**Disease causal factors.** NOCGUS is a **monogenic (Mendelian) disorder**. The primary cause is a heterozygous, almost always **de novo**, pathogenic variant in *WDR37*. There is no known environmental, infectious, or multifactorial contribution. Reis et al. reported "four de novo missense variants predicted to affect the N-terminal region of WDR37—p.Ser119Phe, p.Thr125Ile, p.Ser129Cys, and p.Thr130Ile—in unrelated individuals with a previously unrecognized syndrome" ([PMID: 31327510](https://pubmed.ncbi.nlm.nih.gov/31327510/)). Kanca et al. "identified five pediatric probands with de novo variants in WDR37" ([PMID: 31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/)).

**Genetic risk factors.** The sole known genetic cause is a de novo pathogenic *WDR37* variant in the N-terminal mutational hotspot. No susceptibility loci or modifier genes have been formally established. Because variants are de novo, there are effectively no inherited risk alleles in the general population.

**Environmental risk factors.** None identified. Advanced paternal age is a theoretical contributor to de novo mutation burden generally, but has not been specifically studied in NOCGUS.

**Protective factors.** None identified (genetic or environmental). *WDR37* is constrained against loss-of-function (see Section 4), but this reflects gene essentiality rather than a protective allele.

**Gene–environment interactions.** None described. As a fully penetrant de novo Mendelian malformation syndrome, NOCGUS has no documented GxE component.

---

## Section 3 — Phenotypes

Phenotype frequencies below come from the official HPO annotation set for OMIM:618652 (frequencies derived primarily from the Kanca et al. cohort, [PMID: 31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/)), supplemented by Reis et al. and later case reports.

### Neurological phenotypes (near-universal)

| Phenotype | HPO term | Frequency | Notes |
|---|---|---|---|
| Seizure / epilepsy | HP:0001250 | 5/5 | Often early infantile onset |
| Intellectual disability | HP:0001249 | 4/4 | Typically moderate–severe |
| Global developmental delay | HP:0001263 | 4/4 | |
| Absent speech | HP:0001344 | 4/4 | |
| Cerebellar hypoplasia / vermian anomaly | HP:0001321 | Frequent | Structural brain malformation |

### Ocular phenotypes (hallmark)

| Phenotype | HPO term | Frequency | Notes |
|---|---|---|---|
| Coloboma | HP:0000589 | 4/5 | Iris, retinal, choroidal; **the hallmark feature** |
| Microphthalmia | HP:0000568 | 3/5 | |
| Peters anomaly / anterior-segment dysgenesis | HP:0000659 | 1/5 | Corneal opacity |
| Microcornea | HP:0000482 | Variable | |

### Craniofacial / dysmorphic (CHARGE-like)

| Phenotype | HPO term | Frequency |
|---|---|---|
| Abnormal palmar crease | HP:0010490 | 5/5 |
| Prominent nasal bridge | HP:0000426 | 5/5 |
| Downturned corners of mouth | HP:0002714 | 5/5 |
| Smooth philtrum | HP:0000319 | 4/4 |

### Cardiac

| Phenotype | HPO term | Frequency |
|---|---|---|
| Ventricular septal defect (most common CHD) | HP:0001629 | 3/5 |
| Atrial septal defect | HP:0001631 | 2/5 |
| Patent ductus arteriosus | HP:0001643 | 2/5 |

### Genitourinary

| Phenotype | HPO term | Frequency |
|---|---|---|
| Bilateral cryptorchidism | HP:0008689 | 2/2 (males) |
| Renal dysplasia / polycystic kidney | HP:0000110 / HP:0000113 | Reported in severe cases |

### Other

- **Sensorineural hearing impairment** (HP:0000407) — 2/4
- **Poor feeding** and **poor postnatal growth** — frequent (Reis 2019)
- **Anal atresia** — reported in a splice-variant case (Samejima 2024, [PMID: 38044197](https://pubmed.ncbi.nlm.nih.gov/38044197/))

**Phenotype characteristics.** Onset is **congenital/neonatal** for malformations (coloboma, CHD, cerebellar anomaly) and **infantile** for epilepsy. Severity is **highly variable** — Reis et al. reported "death in infancy in one individual," whereas Hay et al. (2020) expanded the spectrum "to include those with milder developmental delay" ([PMID: 32530092](https://pubmed.ncbi.nlm.nih.gov/32530092/)). The course is generally **stable/non-progressive** developmentally; a systematic review found that regression/skill loss is uncommon and the syndromes should not be classified as primarily regressive ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).

**Quality-of-life impact.** Severe, lifelong. Combined intellectual disability, absent speech, epilepsy, and visual impairment produce profound dependence for daily functioning. No disease-specific QoL instrument data (EQ-5D/SF-36/PROMIS) exist for this ultra-rare disorder.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *WDR37* (HGNC:31406; NCBIGene:22884; Ensembl ENSG00000047056; canonical transcript ENST00000358220). Genomic location chr10:1,095,478–1,178,237 (GRCh37), 10p13. Protein UniProt **Q9Y2I8** (WDR37_HUMAN), **494 amino acids**, with **seven WD40 repeats** and predominantly cytoplasmic localization.

**Pathogenic variants.** The founding variants were all **de novo missense** changes in a tight N-terminal cluster upstream of the WD40 domain:

| Variant (protein) | Source |
|---|---|
| p.Ser119Phe | Reis 2019 ([PMID: 31327510](https://pubmed.ncbi.nlm.nih.gov/31327510/)) |
| p.Thr125Ile | Reis 2019 |
| p.Ser129Cys | Reis 2019 |
| p.Thr130Ile | Reis 2019 |
| p.Thr115Ile | Hay 2020 ([PMID: 32530092](https://pubmed.ncbi.nlm.nih.gov/32530092/)) |
| p.Ser119Tyr | Hay 2020 |
| c.727-27_727-24del (intronic, aberrant splicing → p.S242_I243ins21aa) | Samejima 2024 ([PMID: 38044197](https://pubmed.ncbi.nlm.nih.gov/38044197/)) |

Hay et al. noted the variants "fall within a highly conserved region upstream of the WD-repeat domains, within an apparent mutation cluster." Sorokina et al. (2021) identified a **distinct new cluster** of disease-associated variants and performed functional analyses of mutant proteins ([PMID: 34642815](https://pubmed.ncbi.nlm.nih.gov/34642815/)).

- **Variant classification (ACMG/AMP):** Pathogenic / Likely pathogenic (de novo occurrence + hotspot clustering + absence from population databases). ClinVar (queried Nov 2026) contains ~228 *WDR37* records, dozens classified Pathogenic/Likely pathogenic.
- **Variant type/class:** predominantly **missense**; one **intronic splice** variant.
- **Allele frequency:** pathogenic alleles are **absent from gnomAD** (de novo).
- **Somatic vs germline:** **germline de novo**.
- **Functional consequence:** mutant protein is correctly localized but expressed at reduced levels — consistent with **gain-of-function or dominant-negative** rather than haploinsufficiency.

**Non-haploinsufficiency mechanism (Finding F004).** *WDR37* is constrained against loss-of-function: gnomAD v2.1.1 reports observed/expected LoF = 0.209 (90% CI 0.113–0.412; LOEUF 0.412), LoF Z = 3.93, pLI = 0.57; missense o/e = 0.637 (Z = 2.31). Critically, **all known pathogenic alleles are de novo missense (or one splice) clustered in the N-terminal/WD40 region, not truncating**. Kanca et al. showed a Drosophila *wdr37* null "are homozygous viable but display severe bang sensitivity, a phenotype associated with seizures in flies" ([PMID: 31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/)) — a homozygous-viable null supports that loss-of-function alone is not the human disease mechanism.

**Modifier genes.** None established. Given the WDR37–PACS1–PACS2 interaction, *PACS1*/*PACS2* are candidate biological modulators but have not been shown to modify NOCGUS severity.

**Epigenetic information.** No disease-specific methylation/histone signature has been reported for NOCGUS.

**Chromosomal abnormalities.** None; NOCGUS is caused by point/small variants, not by large CNVs.

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious factors contribute to NOCGUS. It is a fully penetrant monogenic de novo disorder. This section is **not applicable**.

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **de novo missense variant** arises in the conserved N-terminal region (hotspot ~aa 115–130) of *WDR37* → **leads to** an amino-acid substitution in the WDR37 protein near its WD40 β-propeller platform.
2. The variant protein is **correctly localized to the cytoplasm but expressed at reduced levels** → **results in** altered WDR37 dosage/activity (not complete loss). *[Inferred from functional studies; Sorokina 2021]*
3. Because WDR37 **binds PACS1 and PACS2 and the two proteins are mutually required for stable expression**, perturbed WDR37 → **destabilizes the WDR37–PACS1–PACS2 complex** that recognizes cargo and controls sorting. *[Demonstrated: co-IP, cryo-EM]*
4. Disruption of this complex → **impairs intracellular protein trafficking and ER calcium flux** normally controlled by Pacs1–Wdr37. *[Demonstrated in mouse: Nair-Gill 2021]*
5. **Branch A (development):** dysregulated trafficking/calcium signaling during organogenesis → **impairs development of neural crest– and neuroectoderm-derived structures** → coloboma, anterior-segment dysgenesis, cerebellar hypoplasia, CHARGE-like facies, cardiac septal and genitourinary malformations. *[Inferred from phenotype convergence across the WDR37–PACS1–PACS2 axis]*
6. **Branch B (neuronal excitability):** altered ER calcium handling and neuronal function → **lowers seizure threshold** → epilepsy (paralleled by bang-sensitivity in the Drosophila null). *[Model-organism supported]*
7. Combined developmental and functional CNS disruption → **intellectual disability, developmental delay, absent speech** — the clinical endpoint.

### Molecular detail

- **Molecular pathways / protein interactions.** Sorokina et al. showed "the ability of WDR37 to form homodimers and to strongly bind PACS1 and PACS2 phosphofurin acidic cluster sorting proteins; immunocytochemistry confirmed colocalization of WDR37 with PACS1 and PACS2 in human cells" ([PMID: 34642815](https://pubmed.ncbi.nlm.nih.gov/34642815/)). Xiao et al. solved the cryo-EM structure: "Pacs1 binds Wdr37 through a conserved interface within its furin-binding region (FBR)… This interaction stabilizes Wdr37 and is critical for the expression of both proteins" ([PMID: 41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/)).
- **Cellular processes.** ER calcium homeostasis; protein cargo sorting/trafficking; lymphocyte quiescence. Nair-Gill et al. demonstrated "Calcium flux control by Pacs1-Wdr37 promotes lymphocyte quiescence" ([PMID: 33630350](https://pubmed.ncbi.nlm.nih.gov/33630350/)).
- **Protein dysfunction.** WD40 β-propeller scaffold protein; variant substitutions in the N-terminal FBR-interacting region reduce stability and likely perturb complex assembly (dominant-negative/gain-of-function).
- **Shared axis.** Yamamoto et al. proposed that "dysregulation of the WDR37-PACS1-PACS2 axis results in a spectrum that is recognizable by intellectual disability, distinctive facial features, and coloboma," and that "this group of genes may be involved in ocular development" ([PMID: 33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/)).

### Suggested ontology terms

- **GO biological process:** protein targeting (GO:0006605); intracellular protein transport (GO:0006886); regulation of ER calcium ion concentration (GO:0032469); calcium ion transport (GO:0006816).
- **GO cellular component:** cytoplasm (GO:0005737); endoplasmic reticulum (GO:0005783).
- **CL cell types:** neuron (CL:0000540); neural crest cell (CL:0000333); cerebellar Purkinje cell (CL:0000121); lymphocyte (CL:0000542).

---

## Section 7 — Anatomical Structures Affected

**Organ level (primary).**
- **Brain** (UBERON:0000955) — cerebellum (UBERON:0002037), especially vermis; cerebral cortex.
- **Eye** (UBERON:0000970) — iris, retina, choroid (coloboma), cornea/anterior segment, globe (microphthalmia).
- **Heart** (UBERON:0000948) — interventricular/interatrial septa.
- **Kidney** (UBERON:0002113) and **male genitalia** (testis, UBERON:0000473).

**Secondary / body-system involvement.** Nervous (CNS), visual, cardiovascular, genitourinary/renal, musculoskeletal (skeletal anomalies; Hay 2020), auditory (sensorineural hearing loss), and gastrointestinal (anal atresia in one case).

**Tissue / cell level.** Neuroectoderm- and neural crest–derived tissues are prominently affected, consistent with the coloboma + craniofacial + cardiac-outflow + enteric pattern (a "neurocristopathy-like" distribution). Cerebellar Purkinje/granule neurons implicated by cerebellar hypoplasia.

**Subcellular level.** Cytoplasm (GO:0005737); endoplasmic reticulum (GO:0005783) — site of PACS1–WDR37 calcium-flux control.

**Localization / lateralization.** Ocular and genitourinary findings are typically **bilateral** (e.g., bilateral microphthalmia/coloboma, bilateral cryptorchidism), though severity can be asymmetric.

---

## Section 8 — Temporal Development

- **Onset:** **Congenital** (structural malformations present at birth; a neonatal case showed severe bilateral ocular abnormalities identified at birth — [PMID: 42546896](https://pubmed.ncbi.nlm.nih.gov/42546896/)). Epilepsy is typically **early infantile**.
- **Onset pattern:** congenital/insidious for developmental features; seizures may present acutely.
- **Progression:** Developmentally **stable/non-progressive** in most patients; regression is uncommon and does not define the disorder ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
- **Disease course:** chronic, lifelong. Severity spans infantile lethality (Reis 2019) to milder delay (Hay 2020).
- **Critical periods:** organogenesis (first trimester) is the window during which the malformations (eye, heart, cerebellum, kidney) are established — making prenatal/early mechanisms the key vulnerability window.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal dominant** (HP:0000006), essentially always via **de novo** variants. Recurrence risk for unaffected parents is low (germline mosaicism not formally documented but theoretically possible).
- **Penetrance:** Complete for the molecular/malformation phenotype among reported probands.
- **Expressivity:** **Highly variable** (infantile lethal → mild DD).
- **Epidemiology:** No prevalence/incidence estimate exists; **ultra-rare**, with <60 published patients worldwide as of 2026. Orphanet lists it without a prevalence class.
- **Founder effects / consanguinity:** Not applicable (de novo).
- **Carrier frequency:** Not applicable (de novo; constrained gene, no common pathogenic alleles).
- **Population demographics:** Reported across diverse populations (Caucasian — Hay 2020; Mexican patients — [PMID: 37064331](https://pubmed.ncbi.nlm.nih.gov/37064331/); Japanese — Samejima 2024). No ethnic predilection.
- **Sex ratio:** No established skew; genitourinary features (cryptorchidism) are male-specific.

---

## Section 10 — Diagnostics

**Genetic testing (definitive).** Diagnosis rests on identifying a de novo pathogenic *WDR37* variant. Recommended approaches:
- **Whole-exome sequencing (WES)** — the primary diagnostic modality; most reported cases were ascertained by trio exome (e.g., "Clinical exome sequencing identified a de novo pathogenic variant in the WDR37 gene, confirming the diagnosis," [PMID: 42546896](https://pubmed.ncbi.nlm.nih.gov/42546896/)).
- **Whole-genome sequencing (WGS)** — useful to detect deep intronic/splice variants (as in the c.727-27_727-24del splice case, [PMID: 38044197](https://pubmed.ncbi.nlm.nih.gov/38044197/)); RT-PCR confirmed aberrant splicing in that patient.
- **Multigene panels** — *WDR37* should be included on panels for intellectual disability, epilepsy, and structural eye disorders; Hay et al. explicitly "promote the inclusion of WDR37 on gene panels for intellectual disability, epilepsy and structural eye disorders."
- **Trio analysis** confirms de novo status, strongly supporting pathogenicity (ACMG PS2).
- CMA/karyotype/FISH are generally unrevealing (no CNV mechanism).

**Clinical / imaging workup.** Brain MRI (cerebellar hypoplasia/vermian anomaly); detailed ophthalmologic exam (coloboma, microphthalmia, anterior-segment dysgenesis); echocardiography (septal defects); renal ultrasound; hearing evaluation. "Early ophthalmologic evaluation in neonates with multisystem congenital anomalies may provide important diagnostic clues to rare genetic syndromes" ([PMID: 42546896](https://pubmed.ncbi.nlm.nih.gov/42546896/)).

**Biomarkers / omics.** No validated biochemical biomarker or clinical omics test for NOCGUS.

**Differential diagnosis.** CHARGE syndrome (facial overlap), PACS1 (Schuurs-Hoeijmakers) syndrome, PACS2 syndrome, and other coloboma/anterior-segment-dysgenesis disorders. Coloboma is a shared feature across the WDR37–PACS1–PACS2 axis ([PMID: 33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/)).

**Screening.** No newborn or carrier screening (de novo, ultra-rare).

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** Variable. At least one infant died in infancy (Reis 2019); severe neonatal presentations with complex CHD, renal dysplasia, and cerebellar malformation carry high early mortality. Milder cases survive into childhood/adulthood (an affected adult is reported in the axis-overlap literature).
- **Morbidity/function:** Profound — lifelong intellectual disability, absent speech, refractory epilepsy risk, and visual impairment produce severe disability and full-care dependence.
- **Complications:** Seizure-related morbidity, feeding difficulties/failure to thrive, visual loss, cardiac and renal complications.
- **Recovery:** No recovery of the underlying developmental deficits; developmentally stable with supportive care.
- **Prognostic factors:** Degree of structural malformation (especially CHD severity, renal involvement, cerebellar malformation) and seizure control drive outcome. No molecular prognostic biomarker beyond the general severity-by-variant correlations suggested within the hotspot.

---

## Section 12 — Treatment

**No disease-modifying therapy exists.** Management is entirely **supportive, symptomatic, and multidisciplinary**:

- **Pharmacotherapy:** Antiseizure medications for epilepsy (agent choice per seizure semiology; no NOCGUS-specific regimen). NCIT: Anticonvulsant Agent (C264).
- **Surgical/interventional:** Repair of congenital heart defects (VSD/ASD/PDA); orchidopexy for cryptorchidism; management of anal atresia/urological anomalies; ophthalmologic surgery as indicated.
- **Supportive/rehabilitative:** Early developmental intervention, physical/occupational/speech therapy (AAC given absent speech), feeding support (NG/gastrostomy for poor feeding), low-vision services, hearing aids/audiologic support.
- **Advanced therapeutics / pharmacogenomics / experimental trials:** None reported; no NCT-registered trials specific to NOCGUS. Antisense-oligonucleotide and client-protein-targeting strategies have been proposed conceptually for the related PACS1 disorder (given its gain-of-function/dominant-negative mechanism, [PMID: 36077045](https://pubmed.ncbi.nlm.nih.gov/36077045/)) and are a plausible future direction for WDR37, but remain theoretical.

**NCIT suggestions:** Supportive Care (C133453); Anticonvulsant Agent (C264); Physical Therapy (C15321); Occupational Therapy (C15317); Speech Therapy (C15349); Surgical Procedure (C15329).

---

## Section 13 — Prevention

- **Primary prevention:** Not possible (de novo mutation).
- **Secondary prevention:** Early multisystem surveillance (cardiac, renal, ophthalmologic, audiologic, developmental) after diagnosis to detect and treat complications.
- **Tertiary prevention:** Seizure control, feeding/nutrition optimization, vision/hearing support, and developmental therapies to limit secondary disability.
- **Genetic counseling:** Essential. Recurrence risk for parents of an affected de novo child is low but non-zero (germline mosaicism cannot be excluded); affected individuals rarely reproduce. Prenatal/preimplantation testing is feasible once a familial variant is known.
- **Immunization / public-health / behavioral / environmental prevention:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous genes.** *Wdr37* exists in mouse (*Mus musculus*, NCBI Taxon 10090), fly (*Drosophila melanogaster*, Taxon 7227), and *C. elegans* (Taxon 6239, ortholog *wdr-37*). The PACS–WDR37 interaction is evolutionarily conserved: in *C. elegans*, "cePACS-1 and ceWDR-37 colocalize to somatic cytoplasm… and are mutually required for expression, supporting a conclusion that the intermolecular dependence… is evolutionarily conserved" ([PMID: 39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/)).
- **Natural disease / veterinary relevance.** No naturally occurring NOCGUS-equivalent disease has been reported in companion animals or wildlife (not in OMIA). *WDR37* appears as a candidate gene in livestock growth-trait GWAS (Korean native chickens [PMID: 34440344](https://pubmed.ncbi.nlm.nih.gov/34440344/); Dongliao black pigs [PMID: 40665728](https://pubmed.ncbi.nlm.nih.gov/40665728/)), but these are unrelated QTL associations, not the human syndrome.
- **Zoonotic potential:** None (genetic disorder).

---

## Section 15 — Model Organisms

| Model | System | Key finding | Reference |
|---|---|---|---|
| *Drosophila melanogaster* | *wdr37* null | Homozygous viable but severe **bang sensitivity** (seizure-associated phenotype) — supports non-haploinsufficiency and links WDR37 to neuronal excitability | Kanca 2019 [PMID: 31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/) |
| *Mus musculus* | Pacs1–Wdr37 | Controls **ER calcium flux** to promote **lymphocyte quiescence**; loss predisposes to lymphoproliferative disease | Nair-Gill 2021 [PMID: 33630350](https://pubmed.ncbi.nlm.nih.gov/33630350/) |
| *C. elegans* | *wdr-37* / *pacs-1* | Conserved colocalization and **mutual requirement for expression**; human PACS1 complements worm PACS-1 in neurons; variant editing alters neuronal localization | [PMID: 39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/) |
| In vitro (human cells) | Overexpression / co-IP / ICC | WDR37 homodimerizes, binds PACS1/PACS2, colocalizes; variant proteins analyzed functionally | Sorokina 2021 [PMID: 34642815](https://pubmed.ncbi.nlm.nih.gov/34642815/) |
| Cryo-EM (recombinant) | Pacs1–Wdr37 complex | Structural basis of assembly; Pacs1 FBR interface stabilizes Wdr37 | Xiao 2025 [PMID: 41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/) |

**Phenotype recapitulation.** No mouse knock-in of the human N-terminal hotspot variants has been reported; existing models capture molecular (complex assembly, calcium flux) and partial neuronal (seizure-like bang sensitivity) aspects rather than the full multisystem malformation syndrome. **Model limitation:** the developmental malformation spectrum (coloboma, CHD, cerebellar hypoplasia) has not been fully reproduced in a vertebrate genetic model of the specific human variants.

---

## Mechanistic Model (synthesis)

```
 de novo WDR37 missense (hotspot aa ~115–130, N-terminal, upstream of WD40)
                         │
                         ▼
   Mutant WDR37 protein: correctly localized, REDUCED expression/stability
         (gain-of-function / dominant-negative — NOT haploinsufficiency)
                         │
                         ▼
   Destabilized WDR37–PACS1–PACS2 complex (Pacs1 FBR interface; cryo-EM)
                         │
          ┌──────────────┴───────────────┐
          ▼                              ▼
  Impaired cargo trafficking     Dysregulated ER Ca²⁺ flux
          │                              │
          ▼                              ▼
  Faulty organogenesis of         Altered neuronal excitability
  neuroectoderm/neural-crest      → lowered seizure threshold
  derivatives                              │
          │                                ▼
          ▼                            EPILEPSY
  Coloboma, anterior-segment
  dysgenesis, cerebellar
  hypoplasia, CHARGE-like facies,
  septal CHD, GU anomalies
          │
          └────────────► Intellectual disability, absent speech,
                         global developmental delay
```

The upstream, demonstrated steps are the physical WDR37–PACS1/2 interaction and the calcium-flux/lymphocyte function (in vitro and mouse). The downstream developmental branch (how trafficking/calcium dysregulation produces coloboma and the organ malformations) is **inferred from phenotypic convergence** across the WDR37–PACS1–PACS2 axis rather than directly demonstrated.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [31327510](https://pubmed.ncbi.nlm.nih.gov/31327510/) | *De Novo Missense Variants in WDR37 Cause a Severe Multisystemic Syndrome* | Founding cohort; 4 de novo N-terminal missense variants; defines multisystem phenotype incl. infantile lethality |
| [31327508](https://pubmed.ncbi.nlm.nih.gov/31327508/) | *De Novo Variants in WDR37… Epilepsy, Colobomas… Cerebellar Hypoplasia* | Independent cohort (5 probands); Drosophila null (homozygous viable, bang-sensitive); HPO frequency source |
| [34642815](https://pubmed.ncbi.nlm.nih.gov/34642815/) | *WDR37 syndrome… functional analyses of mutant proteins* | Homodimerization; strong PACS1/PACS2 binding; new variant cluster |
| [41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/) | *Structural Basis for Pacs1-Wdr37 Complex Assembly and Stability* | Cryo-EM; Pacs1 FBR interface stabilizes Wdr37; mutual expression dependence |
| [33630350](https://pubmed.ncbi.nlm.nih.gov/33630350/) | *Calcium flux control by Pacs1-Wdr37…* | Functional role in ER Ca²⁺ flux and lymphocyte quiescence (mouse) |
| [33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/) | *Coloboma… WDR37-PACS1-PACS2 axis* | Establishes the shared clinical-molecular axis; coloboma as unifying feature |
| [32530092](https://pubmed.ncbi.nlm.nih.gov/32530092/) | *Expanding the phenotypic spectrum… de novo WDR37* | Milder cases; p.Thr115Ile, p.Ser119Tyr; panel-inclusion recommendation |
| [38044197](https://pubmed.ncbi.nlm.nih.gov/38044197/) | *Splicing variant of WDR37…* | First splice variant; novel phenotypes (anal atresia, polycystic kidney) |
| [42546896](https://pubmed.ncbi.nlm.nih.gov/42546896/) | *Severe bilateral coloboma/microphthalmia in a neonate…* | Severe neonatal ocular/multisystem presentation; exome-confirmed |
| [39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/) | *PACS-1 variant… C. elegans model* | Evolutionary conservation of PACS–WDR37 interaction |
| [42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/) | *Loss of acquired skills in PACS1/PACS2/WDR37…* | Regression uncommon; not a primarily regressive disorder |
| [36077045](https://pubmed.ncbi.nlm.nih.gov/36077045/) | *Molecular basis of Schuurs-Hoeijmakers (PACS1)…* | Proposes gain-of-function/dominant-negative and ASO therapeutic concepts for the axis |

---

## Limitations and Knowledge Gaps

1. **Small N.** All clinical knowledge derives from <60 published patients; frequency estimates (e.g., 5/5, 4/5) are from tiny cohorts and are statistically fragile.
2. **No prevalence/incidence data.** Epidemiology is unquantified.
3. **Mechanism partly inferred.** The link from WDR37–PACS1/2 complex disruption to the specific developmental malformations (coloboma, CHD) is based on phenotypic convergence, not direct experimental demonstration in a vertebrate model of the human variants.
4. **No knock-in animal model** of the human N-terminal hotspot variants recapitulating the full syndrome.
5. **Genotype–phenotype correlations** within the hotspot (why some variants are lethal and others mild) are unresolved.
6. **No biomarkers, no QoL data, no natural-history study, no therapy.**

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse (or zebrafish)** carrying a human hotspot variant (e.g., p.Ser119Phe) to test whether it reproduces coloboma, cerebellar hypoplasia, CHD, and seizures — directly testing the developmental branch of the model.
2. **Quantify the variant's effect on the WDR37–PACS1–PACS2 complex** using the cryo-EM framework (Xiao 2025): measure complex stability, stoichiometry, and ER Ca²⁺ flux for each pathogenic variant to establish gain-of-function vs dominant-negative.
3. **Single-cell/spatial transcriptomics of developing eye and cerebellum** in the model to define cell-type-specific consequences (Purkinje, neural crest, optic-fissure cells).
4. **Establish an international NOCGUS registry/natural-history study** to obtain robust phenotype frequencies, survival, and genotype–phenotype correlations.
5. **Explore ASO / allele-selective knockdown** of the mutant *WDR37* allele (by analogy with PACS1 strategies, [PMID: 36077045](https://pubmed.ncbi.nlm.nih.gov/36077045/)) as a proof-of-concept precision therapy if a dominant-negative/gain-of-function mechanism is confirmed.

---

*Report compiled from OMIM, MONDO, HPO, gnomAD, UniProt, ClinVar, and primary literature. Evidence source types: human clinical case series/reports (Reis, Kanca, Hay, Samejima, neonate report, Mexican cohort); model organism (Drosophila, mouse, C. elegans); in vitro and structural (Sorokina, Xiao).*


## Artifacts

- [OpenScientist final report](Neurooculocardiogenitourinary_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurooculocardiogenitourinary_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41279321` *(abstract only)*: "Pacs1 binds Wdr37 through a conserved interface within its furin-binding region (FBR)… This interaction stabilizes Wdr37 and is critical for the expression of both proteins"
  - closest text in source: "Pacs1 binds Wdr37 through a conserved interface within its furin-binding region (FBR), the domain previously linked to cargo recognition"
- `PMID:39031646`: "cePACS-1 and ceWDR-37 colocalize to somatic cytoplasm… and are mutually required for expression, supporting a conclusion that the intermolecular dependence… is evolutionarily conserved"
  - closest text in source: "We show that cePACS-1 and ceWDR-37 colocalize to somatic cytoplasm of many types of cells and are mutually required for expression, supporting a conclusion that the intermolecular dependence of PACS1/PACS2/PACS-1 and WDR37/WDR-37 is evolutionarily conserved"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 27 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032850` (1 mention) - the report calls it "MONDO"; MONDO calls it **neurooculocardiogenitourinary syndrome**
- `GO:0005737` (2 mentions) - the report calls it "GO cellular component:** cytoplasm"; GO calls it **cytoplasm**
- `CL:0000540` (1 mention) - the report calls it "CL cell types:** neuron"; CL calls it **neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001250` (1 mention) - the report calls it "Seizure / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `HP:0001321` (1 mention) - the report calls it "Cerebellar hypoplasia / vermian anomaly"; HP calls it **Cerebellar hypoplasia**
- `HP:0000659` (1 mention) - the report calls it "Peters anomaly / anterior-segment dysgenesis"; HP calls it **Peters anomaly**
- `HP:0010490` (1 mention) - the report calls it "Abnormal palmar crease"; HP calls it **Abnormal palmar crease morphology**
- `HP:0001629` (1 mention) - the report calls it "Ventricular septal defect (most common CHD)"; HP calls it **Ventricular septal defect**, and lists "Ventricular septal defects" among its other names
- `GO:0006605` (1 mention) - the report calls it "GO biological process:** protein targeting"; GO calls it **protein targeting**
- `HP:0000006` (1 mention) - the report calls it "Autosomal dominant", "Inheritance:** **Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000006` - called "Autosomal dominant", "Inheritance:** **Autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBIGene`, `OMIM`.