---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:00:33.223140'
end_time: '2026-10-30T23:24:29.944250'
duration_seconds: 1436.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Megalencephaly-polydactyly Syndrome
  mondo_id: MONDO:0958279
  category: Mendelian
  causal_genes: MYCN
  omim_id: OMIM:620748
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
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0100306
    reported_labels:
    - Neuroblastoma
    ontology_label: Muscle fiber hyaline bodies
  - term_id: HP:0000074
    reported_labels:
    - Pyeloureteral/renal dilatation
    ontology_label: Ureteropelvic junction obstruction
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Megalencephaly-polydactyly_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Megalencephaly-polydactyly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megalencephaly-polydactyly Syndrome
- **MONDO ID:** MONDO:0958279 (if available)
- **Causal gene(s):** MYCN
- **OMIM:** OMIM:620748
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Megalencephaly-polydactyly Syndrome** covering all of the
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

# Megalencephaly-Polydactyly Syndrome (MYCN) — Comprehensive Disease Characteristics Report

**Disease:** Megalencephaly-polydactyly syndrome, also termed **MPAPA** (Megalencephaly, Polydactyly, And Predisposition to cancer / neuroblastoma)
**MONDO ID:** MONDO:0958279 · **OMIM:** 620748 · **Causal gene:** **MYCN** (N-Myc, HGNC:7559; UniProt P04198; cytoband 2p24.3)
**Inheritance:** Autosomal dominant (de novo)
**Category:** Mendelian multiple-congenital-anomaly / neurodevelopmental disorder

---

## Summary

**Megalencephaly-polydactyly syndrome (MPAPA; MONDO:0958279; OMIM #620748) is caused by germline gain-of-function missense variants in *MYCN*** — the gene encoding the **N-Myc** basic-helix-loop-helix-leucine-zipper (bHLH-LZ) transcription factor. The disease-causing variants (**p.Thr58Met** [c.173C>T] and **p.Pro60Leu**) fall inside the **MYC-box-I (MBI) phosphodegron** of N-Myc, the short N-terminal motif that normally tags the protein for destruction. By removing or disrupting the Thr58 phosphoacceptor site, these variants abolish GSK3β-primed, FBXW7-ubiquitin-ligase-mediated proteasomal degradation of N-Myc. The result is a **stabilized, degradation-resistant N-Myc oncoprotein** — the exact molecular mirror image of **Feingold syndrome type 1** (OMIM 164280), which is caused by *MYCN* loss-of-function (haploinsufficiency) and produces the opposite phenotype of microcephaly and brachydactyly.

Clinically, MPAPA presents with **megalencephaly/macrocephaly, ventriculomegaly, a characteristically hypoplastic corpus callosum, postaxial polydactyly of hands and feet, developmental and motor delay, impaired intellectual development, dysmorphic facial features, postnatal growth retardation, and a predisposition to infantile neuroblastoma**. The disorder is ultra-rare: the entity was defined on just three unrelated individuals (two carrying p.Thr58Met, one fetus carrying p.Pro60Leu). Neuroblastoma was detected in 2 of the 3 reported patients, both of whom carried the recurrent p.Thr58Met allele.

Mechanistically, the pathology is one of **excess progenitor proliferation**. A knock-in *Mycn*-T58M mouse faithfully recapitulates the human megalencephaly and polydactyly, and brain analysis pinpointed **excess proliferation of intermediate (basal) neural precursors during neurogenesis** as the cellular cause of megalencephaly; kidney and female reproductive tract anomalies arise from the same overproliferation during organogenesis. Because the molecular lesion is a *failure of N-Myc degradation*, agents that re-impose N-Myc turnover — notably **Aurora-A inhibitors** (alisertib/MLN8237) and **BET/BRD4 inhibitors** — provide a mechanism-matched (though still experimental) therapeutic rationale, alongside clinically indicated neuroblastoma surveillance.

---

## Key Findings

### Finding 1 — MPAPA is caused by de novo gain-of-function *MYCN* p.Thr58Met (and p.Pro60Leu)

The index report (Kato et al., 2019, [PMID: 30573562](https://pubmed.ncbi.nlm.nih.gov/30573562/)) identified a **de novo heterozygous missense mutation c.173C>T; p.Thr58Met** in *MYCN* in an individual with an undiagnosed neurodevelopmental disorder characterized by megalencephaly and polydactyly. Thr58 is the conserved GSK-3β phosphodegron residue within MYC-box I; its substitution to methionine abolishes the phosphodegradation signal, stabilizing the N-Myc oncoprotein — a **gain-of-function** mechanism. This is the direct mirror image of **Feingold syndrome type 1** (OMIM 164280), which results from *MYCN* loss-of-function and produces microcephaly and brachydactyly. As stated in a Feingold review ([PMID: 41005613](https://pubmed.ncbi.nlm.nih.gov/41005613/)): *"Feingold syndrome type 1 (FS1) (OMIM 164280) is an autosomal dominant condition due to heterozygous loss of function variants in MYCN gene or to 2p24 deletion encompassing MYCN gene."* This dose-dependent model — loss of function → microcephaly, gain of stability → megalencephaly — is the conceptual backbone of the disease.

### Finding 2 — The Thr58/GSK-3β phosphodegron controls N-Myc turnover and is required for neural precursor growth arrest

N-Myc is destabilized by phosphorylation of a conserved amino-terminal GSK-3β motif at Thr58, which primes it for FBXW7-mediated proteasomal degradation ([PMID: 16139224](https://pubmed.ncbi.nlm.nih.gov/16139224/)): *"Myc family transcription factors are destabilized by phosphorylation of a conserved amino-terminal GSK-3beta motif."* Critically, this degradation step is a **prerequisite for cerebellar granule neuron precursor (CGNP) growth arrest and differentiation**: *"N-myc phosphorylation-mediated degradation is a prerequisite for CGNP growth arrest and differentiation."* Upstream, PI3K/AKT signaling suppresses GSK-3β to inhibit Thr58 phosphorylation and stabilize N-Myc; INSM1 was shown to activate *"PI3K/AKT/GSK3β pathways to suppress N-myc phosphorylation (Thr-58) and inhibited degradation of N-myc"* ([PMID: 26456864](https://pubmed.ncbi.nlm.nih.gov/26456864/)). A p.Thr58Met substitution removes the phosphoacceptor residue, rendering N-Myc degradation-resistant and locking neural precursors in a proliferative state rather than permitting the growth arrest needed for normal brain patterning.

### Finding 3 — Mouse models establish N-Myc as a dose-dependent regulator of brain/cerebellar size

Conditional loss of N-Myc reduces brain size. Nestin-Cre conditional knockout of N-myc in neural stem/precursor cells causes **microcephaly** with a strong reduction of cerebellar granule neural progenitors ([PMID: 20658325](https://pubmed.ncbi.nlm.nih.gov/20658325/)): *"Separate murine knockout (KO) of either c- or N-myc genes in neural stem and precursor cells (NSC) driven by nestin-cre causes microcephaly."* Inducible/reversible models confirm the dose-dependence: *"Loss of N-myc at the neonatal stage results in reduced proliferation of granule cell precursors (GCPs) and reduced cerebellar volume/mass"* ([PMID: 26238256](https://pubmed.ncbi.nlm.nih.gov/26238256/)), where N-Myc acts as a "key switch" regulating the GCP proliferation cycle via Shh signaling and cyclin D2 (Ccnd2). Shh induces N-Myc, which maintains CGNP proliferation partly through β-catenin ([PMID: 32495183](https://pubmed.ncbi.nlm.nih.gov/32495183/)). These loss-of-function data predict that a *stabilizing* variant would increase brain size — exactly the megalencephaly seen in MPAPA.

### Finding 4 — Stabilized N-Myc drives a pro-proliferative transcriptional program, but overexpression alone is insufficient for tumorigenesis

N-Myc is a bHLH-LZ transcription factor that activates cell-cycle and biosynthetic programs and cooperates with β-catenin to drive progenitor-renewal programs ([PMID: 28993399](https://pubmed.ncbi.nlm.nih.gov/28993399/)): *"β-catenin cooperates with the transcription factor Myc to activate the progenitor renewal program."* It also maintains productive RNA Pol II elongation on cell-cycle genes during S phase ([PMID: 34847357](https://pubmed.ncbi.nlm.nih.gov/34847357/)). Importantly, enforced MYCN overexpression in murine sympathoadrenal progenitors increased proliferation and neural-lineage commitment but was **not sufficient to form tumors** ([PMID: 26222553](https://pubmed.ncbi.nlm.nih.gov/26222553/)): *"MYCN promoted proliferation of both sympathoadrenal progenitor spheres and differentiated neurons derived from these spheres, but there was also an increase in apoptosis."* This explains why MPAPA produces overgrowth and a tumor *predisposition* rather than universal malignancy — additional cooperating events are required for frank neuroblastoma.

### Finding 5 — Clinical spectrum of MPAPA and the second causal variant p.Pro60Leu

OMIM #620748 (MPAPA) is autosomal dominant, caused by heterozygous gain-of-function *MYCN* variants. Two recurrent MYC-box-I variants are reported: **c.173C>T p.Thr58Met** (index case, Kato 2019, [PMID: 30573562](https://pubmed.ncbi.nlm.nih.gov/30573562/)) and **p.Pro60Leu** (Nishio 2023, [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)). As Nishio et al. report: *"we report two unrelated megalencephalic patients with polydactyly harboring MYCN variants of p.Pro60Leu and Thr58Met"* and confirm that *"germline loss-of-function variants are responsible for Feingold syndrome, characterized by microcephaly."* Core features include megalencephaly/macrocephaly, ventriculomegaly, hypoplastic corpus callosum, postaxial polydactyly of hands and feet, developmental/motor delay, impaired intellectual development, dysmorphic facies (prominent forehead, hypertelorism, epicanthus, high-arched palate, long philtrum), postnatal growth retardation, and neuroblastoma predisposition. Additional anomalies in the fetal p.Pro60Leu case included Meckel diverticulum and pyeloureteral dilatation. p.Thr58Met is absent from gnomAD but present in COSMIC (as a somatic cancer mutation).

### Finding 6 — Knock-in *Mycn*-T58M mouse recapitulates the syndrome; megalencephaly is driven by excess intermediate neural precursor proliferation

Both disease variants reduce Thr58 phosphorylation, decreasing FBXW7-mediated degradation ([PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)): *"Functional analyses for MYCN-Pro60Leu and MYCN-Thr58Met revealed decreased phosphorylation at Thr58, which reduced protein degradation mediated by FBXW7 ubiquitin ligase."* A gain-of-function mouse model recapitulated the human phenotype: *"The gain-of-function mouse model recapitulated the human phenotypes of megalencephaly and polydactyly, while brain analyses revealed excess proliferation of intermediate neural precursors during neurogenesis, which we determined to be the pathomechanism underlying megalencephaly."* Multi-organ involvement arises by the same route: *"the kidney and female reproductive tract exhibited overt morphological anomalies, possibly as a result of excess proliferation during organogenesis."* In mouse neural progenitors, T58M N-Myc was more stable and induced higher cyclin D1 (Ccnd1) and cyclin D2 (Ccnd2) than wild type.

### Finding 7 — MPAPA is a hereditary neuroblastoma-predisposition syndrome; hypoplastic corpus callosum is a distinguishing radiologic feature

Neuroblastoma was detected in 2 of 3 reported MYCN gain-of-function patients during infancy; in one, neuroblastoma diagnosed at age 3 months responded well to chemotherapy and surgery ([PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)). The variant p.Thr58Met also occurs as a *somatic* mutation in neuroblastoma, astrocytoma, and mesonephric carcinoma (COSMIC), underscoring its oncogenic potential. N-Myc is normally tightly controlled by sequential phosphorylation (Ser62 → Thr58) and SCF-FBXW7-mediated proteasomal degradation; the germline degron variants defeat this control. A **hypoplastic corpus callosum despite a megalencephalic cerebrum** was present in all three cases and is considered a characteristic radiologic feature distinguishing MPAPA from other megalencephaly syndromes (e.g., MPPH3, which shows polymicrogyria). Nishio et al. note the disorder *"shows a mirror phenotype of Feingold syndrome, and reveal[s] that MYCN plays a crucial proliferative"* role.

### Finding 8 — Genotype–phenotype distribution across the three reported patients; neuroblastoma segregates with p.Thr58Met

The disease entity is established on three unrelated individuals:

| Patient | Variant | Key phenotype | Neuroblastoma | Reference |
|---|---|---|---|---|
| Index, 15-y-old boy | p.Thr58Met (c.173C>T) | Megalencephaly, ventriculomegaly, hypoplastic corpus callosum, intellectual disability, polydactyly | **Yes** | Kato 2019, [PMID: 30573562](https://pubmed.ncbi.nlm.nih.gov/30573562/) |
| 8-month-old Japanese boy | p.Thr58Met | Megalencephaly, polydactyly | **Yes** | Nishio 2023, [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/) |
| Fetus (French family, TOP) | p.Pro60Leu | Ventriculomegaly, macrocephaly, postaxial polydactyly, hypertelorism, low-set ears, retrognathia, Meckel diverticulum, pyeloureteral dilatation | Unknown (terminated) | Nishio 2023, [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/) |

Nishio et al. confirm the disorder was *"complicated with neuroblastoma detected in two out of the three patients."* Both tumor-bearing patients carried p.Thr58Met; the p.Pro60Leu fetus was terminated so its tumor status is unknown. p.Pro60Leu lies immediately adjacent to Thr58 in MYC box I; both variants are absent from gnomAD and present in COSMIC.

### Finding 9 — N-Myc protein architecture places both disease variants inside the MYC-box-I phosphodegron

N-Myc (UniProt P04198; 464 aa; bHLHe37) comprises an **N-terminal transactivation domain** containing **MYC box I (MBI, ~residues 46–63**, harboring the Thr58/Ser62 phosphodegron) and **MYC box II (MBII, ~110–134**, binding TRRAP/SAGA coactivators), plus a **C-terminal bHLH-LZ domain (~346–440)** whose basic region contacts the E-box (CACGTG) and whose HLH+LZ mediate obligate heterodimerization with MAX (the structural paradigm is the c-Myc–MAX–DNA complex, PDB 1NKP). Degradation is ordered: CDK1 phosphorylates Ser62 (stabilizing) → GSK3β phosphorylates Thr58 → PP2A dephosphorylates Ser62 → FBXW7 recognizes pThr58 → K48-linked ubiquitination → proteasomal degradation; USP28/USP7 deubiquitinases oppose this. Both disease variants — **p.Thr58Met** (removes the phosphoacceptor) and **p.Pro60Leu** (immediately adjacent, within MBI) — reduce Thr58 phosphorylation and FBXW7 recognition, stabilizing N-Myc, while leaving the DNA-binding/MAX-dimerization machinery intact ([PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)).

### Finding 10 — Aurora-A and BET inhibitors destabilize N-Myc: a mechanism-matched (experimental) therapeutic rationale

Because MPAPA arises from degron variants that *stabilize* N-Myc, therapeutics that **re-impose N-Myc degradation** are mechanism-matched. Key evidence (from neuroblastoma models, not yet tested in MPAPA):
- **Aurora-A inhibitors:** MLN8054 and MLN8237 (alisertib) *"disrupt the Aurora-A/N-Myc complex and promote degradation of N-Myc mediated by the Fbxw7 ubiquitin ligase"* ([PMID: 23792191](https://pubmed.ncbi.nlm.nih.gov/23792191/)) — directly restoring the FBXW7 pathway escaped by MPAPA mutations.
- **Structural basis:** cryo-EM shows Aurora-A binding protects N-Myc from degradation; conformation-disrupting kinase inhibitors reverse this ([PMID: 27837025](https://pubmed.ncbi.nlm.nih.gov/27837025/)).
- **Combination:** dual BRD4 (I-BET151) + AURKA (alisertib) inhibition is synergistic against MYCN-driven tumors ([PMID: 30153557](https://pubmed.ncbi.nlm.nih.gov/30153557/)).
- **Interaction inhibitor:** PHA-680626 disrupts the AURKA/N-Myc interaction ([PMID: 34884931](https://pubmed.ncbi.nlm.nih.gov/34884931/)).

Mechanistic class summary: Aurora-A inhibitors (alisertib/MLN8237, MLN8054, PHA-680626), BET/BRD4 inhibitors (JQ1, I-BET151) that lower MYCN transcription, and GSK3β/FBXW7-axis modulators all converge on reducing N-Myc abundance.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. De novo germline missense variant in MYCN MYC-box-I phosphodegron
   (p.Thr58Met removes the phospho-acceptor; p.Pro60Leu disrupts the adjacent motif)
        │ leads to
        ▼
2. Loss of GSK3β-mediated Thr58 phosphorylation of N-Myc
        │ results in
        ▼
3. Failure of FBXW7 (SCF E3 ligase) to recognize the phosphodegron
   → reduced K48-ubiquitination → escape from proteasomal degradation
        │ leads to
        ▼
4. STABILIZED, degradation-resistant N-Myc protein accumulates
   (DNA-binding & MAX-dimerization domains intact → still transcriptionally active)
        │ drives
        ▼
5. Sustained pro-proliferative transcription: cyclin D1/D2 (CCND1/CCND2) ↑,
   cell-cycle & biosynthetic genes ↑, cooperation with β-catenin/Wnt
        │ branches ▼                         ▼                          ▼
   ┌────────────────────┐   ┌─────────────────────────┐   ┌──────────────────────────┐
   │ 6a. Excess         │   │ 6b. Excess proliferation │   │ 6c. "Second-hit"         │
   │ proliferation of   │   │ of limb/organ            │   │ cooperating events in    │
   │ intermediate/basal │   │ progenitors              │   │ sympathoadrenal lineage  │
   │ neural precursors  │   │                          │   │ (MYCN alone insufficient)│
   └─────────┬──────────┘   └───────────┬─────────────┘   └────────────┬─────────────┘
             ▼                          ▼                               ▼
   Megalencephaly,            Postaxial polydactyly,        Infantile NEUROBLASTOMA
   ventriculomegaly,          kidney & female               (predisposition;
   hypoplastic corpus         reproductive tract            seen in 2/3 patients,
   callosum, DD/ID            anomalies                     both p.Thr58Met)
```

### Upstream vs downstream
- **Upstream (initiating):** the degron mutation and the resulting failure of FBXW7-dependent degradation (steps 1–3).
- **Central node:** stabilized N-Myc protein (step 4) — the single molecular hub from which all phenotypes radiate.
- **Downstream (effector):** the cell-cycle/biosynthetic transcriptional program and progenitor overproliferation (steps 5–6), which translate directly into the overgrowth phenotypes. Step 6c is *inferred* (cooperating oncogenic events are required but not individually identified in these patients).

### Cell types and biological processes
- **Cell types (CL):** intermediate/basal neural progenitor cells (neural-lineage; basal progenitors of the subventricular zone), cerebellar granule neuron progenitors, neural stem cells (CL:0000047), sympathoadrenal/neural-crest-derived progenitors (neuroblast, CL:0000031).
- **Biological processes (GO):** GO:0008284 positive regulation of cell population proliferation; GO:0006468/GO:0016567 protein phosphorylation / ubiquitination; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process (lost); GO:0021846 cell proliferation in forebrain; GO:0007399 nervous system development; GO:0045944 positive regulation of transcription by RNA Pol II.
- **Cellular components (GO CC):** GO:0005634 nucleus (N-Myc action), GO:0005829 cytosol (degradation machinery).

### Mirror-image relationship with Feingold syndrome

| Feature | MPAPA (this disease) | Feingold syndrome type 1 |
|---|---|---|
| *MYCN* lesion | Gain-of-function (stabilizing degron variant) | Loss-of-function (truncation / deletion / haploinsufficiency) |
| N-Myc dose | ↑ (excess, stabilized) | ↓ (reduced) |
| Head size | **Megalencephaly / macrocephaly** | **Microcephaly** |
| Digits | **Postaxial polydactyly** | Brachydactyly, syndactyly, digital anomalies |
| OMIM | 620748 | 164280 |
| Cancer | Neuroblastoma predisposition | Not characteristic |

This clean dose-response dichotomy is among the most elegant genotype–phenotype relationships in developmental genetics and constitutes the strongest conceptual support for the gain-of-function model.

---

## Section-by-Section Reference Content

### 1. Disease Information
- **Overview:** Ultra-rare autosomal-dominant multiple-congenital-anomaly/neurodevelopmental syndrome of brain and limb overgrowth with neuroblastoma predisposition, caused by stabilizing *MYCN* degron variants.
- **Identifiers:** MONDO:0958279; OMIM #620748; causal gene *MYCN* (HGNC:7559). ICD-10/ICD-11, MeSH, and Orphanet-specific codes are not established for this newly delineated entity. Synonyms: **MPAPA** (megalencephaly, polydactyly, and predisposition to cancer/neuroblastoma); "gain-of-function MYCN syndrome."
- **Information source:** Aggregated from individual published case reports plus a knock-in mouse model (not EHR-derived cohort data).

### 2. Etiology
- **Causal factor:** purely genetic — de novo heterozygous gain-of-function *MYCN* missense variants in MYC-box-I (p.Thr58Met, p.Pro60Leu).
- **Genetic risk factors:** the causal variants themselves; no modifier loci identified. Variants are de novo (parents unaffected).
- **Environmental risk/protective factors:** none identified or expected — this is a monogenic developmental disorder.
- **Gene–environment interactions:** none documented.

### 3. Phenotypes (suggested HPO terms and frequencies among the 3 reported cases)

| Phenotype | HPO term | Type | Onset | Frequency |
|---|---|---|---|---|
| Megalencephaly/macrocephaly | HP:0001355 / HP:0000256 | Physical/imaging | Congenital/prenatal | 3/3 |
| Ventriculomegaly | HP:0002119 | Imaging | Congenital/prenatal | 3/3 |
| Hypoplastic corpus callosum | HP:0002079 | Imaging sign | Congenital | 3/3 (distinguishing) |
| Postaxial polydactyly (hands/feet) | HP:0100259 / HP:0001162 | Physical | Congenital | 3/3 |
| Developmental/motor delay | HP:0012758 / HP:0001270 | Behavioral/clinical | Infancy | present |
| Intellectual disability | HP:0001249 | Behavioral | Childhood | present |
| Dysmorphic facies (prominent forehead, hypertelorism, epicanthus, high-arched palate, long philtrum) | HP:0000316, HP:0000286, HP:0000218, HP:0000343 | Physical | Congenital | present |
| Postnatal growth retardation | HP:0008897 | Clinical | Infancy | present |
| Neuroblastoma | HP:0100306 | Neoplasm | Infancy | 2/3 |
| Meckel diverticulum | HP:0002245 | Physical | Congenital | 1/3 (fetus) |
| Pyeloureteral/renal dilatation | HP:0000074 | Imaging | Prenatal | 1/3 (fetus) |

- **Severity:** moderate–severe, variable. **Progression:** developmental features are static/stable; neuroblastoma risk is confined to infancy. **QoL impact:** substantial — intellectual disability and developmental delay impair daily functioning; neuroblastoma adds major (though often treatable) burden. Formal QoL instruments have not been applied to this ultra-rare entity.

### 4. Genetic / Molecular Information
- **Causal gene:** *MYCN* (OMIM 164840), 2p24.3.
- **Pathogenic variants:** c.173C>T p.Thr58Met (recurrent) and p.Pro60Leu. Both are missense, within MYC-box-I. **ACMG classification:** pathogenic/likely pathogenic (de novo, functionally validated, absent from gnomAD). **Allele frequency:** absent from gnomAD; present in COSMIC as somatic cancer mutations. **Origin:** germline (de novo) in MPAPA; the same residue changes occur somatically in neuroblastoma/astrocytoma/mesonephric carcinoma. **Functional consequence:** gain-of-function via protein stabilization (not altered DNA binding).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none specifically identified for MPAPA. (Note: *somatic MYCN amplification* at 2p24 is the classic neuroblastoma lesion but is distinct from MPAPA's germline point mutations.)

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors. The disease is monogenic and de novo.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. Key molecular pathways: **FBXW7/SCF ubiquitin–proteasome degradation** (lost), **GSK3β/PI3K-AKT** signaling (regulates Thr58 phosphorylation), **Shh → N-Myc → cyclin D2/β-catenin** proliferative axis, **Wnt/β-catenin** cooperation, and **MYCN-driven RNA Pol II elongation**. Downstream cellular process: dysregulated cell-cycle entry and failure of progenitor growth arrest.

### 7. Anatomical Structures Affected
- **Primary organ:** brain (UBERON:0000955) — cerebrum, lateral ventricles (UBERON:0002285), corpus callosum (UBERON:0002336).
- **Other organs:** limbs/digits (UBERON:0002544), kidney (UBERON:0002113), female reproductive tract (UBERON:0000474), adrenal medulla/sympathetic nervous system (neuroblastoma origin).
- **Body systems:** central & peripheral nervous, musculoskeletal, genitourinary.
- **Tissue/cell level:** neural progenitor/germinal zones (intermediate/basal progenitors), neural-crest-derived sympathoadrenal cells.
- **Subcellular:** nucleus (GO:0005634, N-Myc transcriptional action); ubiquitin-proteasome machinery in cytosol.
- **Lateralization:** bilateral (megalencephaly, ventriculomegaly, polydactyly).

### 8. Temporal Development
- **Onset:** congenital/prenatal (macrocephaly, ventriculomegaly, polydactyly detectable antenatally).
- **Course:** developmental/structural features are stable (non-progressive). Neuroblastoma risk is an infancy-limited critical window — the key period for surveillance. Intellectual disability is lifelong.

### 9. Inheritance and Population
- **Epidemiology:** ultra-rare; only 3 reported individuals — prevalence/incidence not estimable.
- **Inheritance:** autosomal dominant, essentially all cases **de novo**. **Penetrance:** appears high for the core malformation phenotype. **Expressivity:** variable (e.g., tumor status, additional anomalies). No anticipation, founder effects, or consanguinity role (de novo mechanism). **Carrier frequency:** not applicable. **Sex ratio / demographics:** indeterminate from 3 cases (two Japanese boys, one French fetus).

### 10. Diagnostics
- **Genetic testing is definitive:** trio whole-exome (WES) or whole-genome (WGS) sequencing detecting a de novo *MYCN* MYC-box-I missense variant; targeted single-gene/*MYCN* sequencing confirms. Standard neuroblastoma-amplification assays (FISH/CMA for 2p24 amplification) will **miss** these point mutations — sequencing is required.
- **Imaging:** brain MRI (megalencephaly, ventriculomegaly, **hypoplastic corpus callosum** — the distinguishing feature). Prenatal ultrasound (macrocephaly, ventriculomegaly, polydactyly). Abdominal imaging/urinary catecholamine metabolites for neuroblastoma surveillance.
- **Differential diagnosis:** MPPH syndromes / PIK3CA-related overgrowth spectrum (PROS, e.g., MCAP — distinguished by capillary malformations and polymicrogyria rather than hypoplastic corpus callosum; [PMID: 31929958](https://pubmed.ncbi.nlm.nih.gov/31929958/), [PMID: 32692051](https://pubmed.ncbi.nlm.nih.gov/32692051/)); Feingold syndrome (mirror phenotype); other megalencephaly-polydactyly overgrowth syndromes.

### 11. Outcome / Prognosis
- **Survival/mortality:** no cohort mortality data. The one treated neuroblastoma responded well to chemotherapy and surgery, suggesting favorable tumor prognosis when detected early. One pregnancy was terminated.
- **Morbidity:** driven by intellectual disability/developmental delay (lifelong) and neuroblastoma risk (infancy).
- **Prognostic factors:** p.Thr58Met genotype associated with observed neuroblastoma in both carriers; early tumor detection improves outcome.

### 12. Treatment
- **No disease-specific or curative therapy exists.** Management is supportive and surveillance-based: developmental/early-intervention services, physical/occupational/speech therapy, management of hydrocephalus/ventriculomegaly as indicated, and **active neuroblastoma surveillance** in infancy (imaging ± urinary catecholamines).
- **Neuroblastoma treatment** follows standard protocols (chemotherapy, surgery) — effective in the reported case.
- **Mechanism-matched experimental rationale (not yet tested in MPAPA):** N-Myc-destabilizing agents — **Aurora-A inhibitors** (alisertib/MLN8237 [NCIT: Alisertib], MLN8054, PHA-680626) and **BET/BRD4 inhibitors** (JQ1, I-BET151), which restore FBXW7-mediated degradation or lower MYCN transcription, respectively ([PMID: 23792191](https://pubmed.ncbi.nlm.nih.gov/23792191/), [PMID: 30153557](https://pubmed.ncbi.nlm.nih.gov/30153557/), [PMID: 34884931](https://pubmed.ncbi.nlm.nih.gov/34884931/)).

### 13. Prevention
- **Primary prevention:** not possible (de novo). **Genetic counseling:** recurrence risk is low (de novo) but germline/gonadal mosaicism cannot be excluded; prenatal/preimplantation testing possible once a familial variant is known. **Secondary prevention:** neuroblastoma surveillance in affected infants (tertiary prevention of tumor complications).

### 14. Other Species / Natural Disease
- **Orthologue:** mouse *Mycn* (NCBI Gene ID 18109). No naturally occurring animal disease described (OMIA entry not established). The Thr58 degron and its regulation are evolutionarily conserved across Myc-family proteins, making the mechanism broadly conserved.

### 15. Model Organisms
- **Knock-in *Mycn*-T58M mouse** (gain-of-function): **recapitulates megalencephaly and polydactyly**, with kidney and female reproductive tract anomalies; brain analysis localized the defect to excess intermediate neural precursor proliferation ([PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)). This is the pivotal disease model.
- **Conditional *N-myc* knockout mice** (Nestin-Cre, Foxg1-Cre) — loss-of-function models producing microcephaly, defining the dose-dependence ([PMID: 20658325](https://pubmed.ncbi.nlm.nih.gov/20658325/), [PMID: 24376126](https://pubmed.ncbi.nlm.nih.gov/24376126/), [PMID: 26238256](https://pubmed.ncbi.nlm.nih.gov/26238256/)).
- **In vitro:** murine neural progenitors and sympathoadrenal progenitor spheres expressing WT vs T58M N-Myc ([PMID: 26222553](https://pubmed.ncbi.nlm.nih.gov/26222553/), [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)).
- **Limitations:** models derived from a single degron allele; the T58M mouse does not necessarily capture the full human neurocognitive phenotype, and spontaneous neuroblastoma penetrance in the model is not fully characterized.

---

## Evidence Base

| PMID | Paper (abbreviated) | Role in this report |
|---|---|---|
| [37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/) | *Gain-of-function MYCN causes a megalencephaly-polydactyly syndrome manifesting mirror phenotypes of Feingold syndrome* | **Pivotal** — defines the syndrome, p.Pro60Leu + p.Thr58Met, FBXW7 mechanism, knock-in mouse, intermediate-progenitor overproliferation, neuroblastoma in 2/3 |
| 30573562 | Kato et al. 2019 (index case) | First report of de novo *MYCN* p.Thr58Met with megalencephaly/polydactyly/neuroblastoma |
| [16139224](https://pubmed.ncbi.nlm.nih.gov/16139224/) | *Cdk1 complex regulates N-myc phosphorylation and turnover* | Establishes GSK3β/Thr58 degradation and its requirement for CGNP growth arrest |
| [26456864](https://pubmed.ncbi.nlm.nih.gov/26456864/) | *INSM1 increases N-myc stability* | Confirms Thr-58 phosphorylation governs N-Myc degradation via PI3K/AKT/GSK3β |
| [20658325](https://pubmed.ncbi.nlm.nih.gov/20658325/) | *c- and N-myc regulate neural precursor fate* | N-myc KO → microcephaly (dose-dependence) |
| [26238256](https://pubmed.ncbi.nlm.nih.gov/26238256/) | *N-myc key switch for GCP proliferation* | Reversible control of cerebellar size by N-Myc |
| [32495183](https://pubmed.ncbi.nlm.nih.gov/32495183/) | *Shh → β-catenin maintains CGNPs* | Shh–N-Myc–β-catenin proliferative axis |
| [26222553](https://pubmed.ncbi.nlm.nih.gov/26222553/) | *MYCN in sympathoadrenal progenitors* | MYCN overexpression drives proliferation but is insufficient for tumorigenesis |
| [28993399](https://pubmed.ncbi.nlm.nih.gov/28993399/) | *Myc cooperates with β-catenin in nephron progenitors* | Myc/β-catenin progenitor-renewal cooperation |
| [34847357](https://pubmed.ncbi.nlm.nih.gov/34847357/) | *MYCN recruits nuclear exosome to RNAPII* | MYCN sustains cell-cycle transcription in S phase |
| [41005613](https://pubmed.ncbi.nlm.nih.gov/41005613/) | *Rare features in Feingold syndrome type 1* | Documents MYCN loss-of-function → microcephalic mirror phenotype |
| [23792191](https://pubmed.ncbi.nlm.nih.gov/23792191/) | *Aurora-A inhibitors induce N-myc degradation* | Mechanism-matched therapeutic rationale (restore FBXW7 degradation) |
| [27837025](https://pubmed.ncbi.nlm.nih.gov/27837025/) | *Structural basis of N-Myc binding by Aurora-A* | Structural basis for destabilization strategy |
| [30153557](https://pubmed.ncbi.nlm.nih.gov/30153557/) | *Dual BRD4 + AURKA inhibition* | Synergistic N-Myc-lowering combination |
| [34884931](https://pubmed.ncbi.nlm.nih.gov/34884931/) | *PHA-680626 inhibits AURKA/N-Myc* | Additional N-Myc-destabilizing agent |

**Evidence source types:** human clinical (3 case reports), model organism (knock-in and conditional mouse), in vitro (progenitor cultures), structural/computational (PDB 1NKP, cryo-EM of AURKA/N-Myc).

---

## Limitations and Knowledge Gaps

1. **Extremely small sample (n=3).** The entire clinical description rests on three individuals, limiting confidence in phenotype frequencies, penetrance, expressivity, and sex/ethnic distribution.
2. **Neuroblastoma penetrance unknown.** Observed in 2/3 (both p.Thr58Met); the p.Pro60Leu fetus was terminated, so whether p.Pro60Leu confers equal tumor risk is unknown. True lifetime cancer risk cannot be estimated.
3. **No natural history / prognosis data.** Long-term neurodevelopmental trajectory, life expectancy, and adult outcomes are undefined.
4. **No epidemiology.** Prevalence, incidence, and demographic distribution are unknowable from current data.
5. **Therapeutics untested in MPAPA.** Aurora-A/BET inhibitor rationale is extrapolated entirely from neuroblastoma models; no in-human or even MPAPA-mouse treatment data exist, and systemic N-Myc suppression during development has unclear safety.
6. **Genotype–phenotype correlation preliminary.** The apparent segregation of neuroblastoma with p.Thr58Met could be chance given n=3.
7. **Mouse-model gaps.** The degree to which the T58M mouse models human intellectual disability and spontaneous tumor incidence is incompletely reported.
8. **No formal QoL, imaging-registry, or ontology (ICD/Orphanet/MeSH) coding** yet exists for this newly delineated entity.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international MPAPA registry / GeneMatcher cascade** to identify additional cases and refine penetrance (especially neuroblastoma), expressivity, and genotype–phenotype correlations (p.Thr58Met vs p.Pro60Leu and any novel MBI variants).
2. **Define a neuroblastoma surveillance protocol** for molecularly confirmed infants (abdominal ultrasound + urinary catecholamine metabolites at defined intervals through the infancy risk window) and prospectively evaluate it.
3. **Characterize tumor penetrance and spectrum in the knock-in mouse**, including whether a p.Pro60Leu knock-in differs from T58M in tumor incidence.
4. **Test N-Myc-destabilizing agents (alisertib, I-BET151) in the T58M mouse** to obtain the first preclinical proof-of-concept for a mechanism-matched therapy, with careful developmental-safety readouts.
5. **Single-cell / spatial transcriptomics of the T58M embryonic brain** to map which precursor populations (basal/intermediate progenitors) are expanded and quantify the N-Myc target program driving overgrowth.
6. **Patient iPSC-derived cerebral organoids** carrying the degron variants to model human-specific neurodevelopmental consequences and screen stabilization-reversing compounds.
7. **Quantify N-Myc protein half-life and FBXW7 binding** for each variant in human neural progenitors to establish a stability–phenotype gradient.
8. **Formal ontology/registry coding** (ICD-11, Orphanet, MeSH) and a GeneReviews chapter to standardize clinical recognition and differential diagnosis from PROS/MPPH/Feingold.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 26 reviewed papers. Primary source for the disease definition: Nishio et al. 2023 ([PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)); index case: Kato et al. 2019 (PMID: 30573562).*


## Artifacts

- [OpenScientist final report](Megalencephaly-polydactyly_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Megalencephaly-polydactyly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 9 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100306` (1 mention) - the report calls it "Neuroblastoma"; HP calls it **Muscle fiber hyaline bodies**
- `HP:0000074` (1 mention) - the report calls it "Pyeloureteral/renal dilatation"; HP calls it **Ureteropelvic junction obstruction**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002079` (1 mention) - the report calls it "Hypoplastic corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `UBERON:0002544` (1 mention) - the report calls it "Other organs:** limbs/digits"; UBERON calls it **digit**, and lists "limb digit" among its other names