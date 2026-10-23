---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T20:50:05.178644'
end_time: '2026-10-14T21:03:52.930929'
duration_seconds: 827.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Doyne Honeycomb Retinal Dystrophy
  mondo_id: MONDO:0007471
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
citation_count: 15
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 21
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 5
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: UBERON:0002423
    reported_labels:
    - macula
    ontology_label: hepatobiliary system
  - term_id: UBERON:0004864
    reported_labels:
    - "RPE\u2013Bruch's membrane interface"
    ontology_label: vasculature of retina
  - term_id: HP:0011506
    reported_labels:
    - Macular drusen
    ontology_label: Choroidal neovascularization
  - term_id: HP:0012508
    reported_labels:
    - Symptom
    ontology_label: Metamorphopsia
  - term_id: HP:0007814
    reported_labels:
    - Clinical sign
    ontology_label: Retinal pigment epithelial mottling
  - term_id: HP:0030500
    reported_labels:
    - Clinical sign
    ontology_label: Yellow/white macular lesion
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Doyne_Honeycomb_Retinal_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Doyne_Honeycomb_Retinal_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Doyne Honeycomb Retinal Dystrophy
- **MONDO ID:** MONDO:0007471 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Doyne Honeycomb Retinal Dystrophy** covering all of the
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

# Doyne Honeycomb Retinal Dystrophy (DHRD) / Malattia Leventinese — Comprehensive Disease Report

**Disease:** Doyne Honeycomb Retinal Dystrophy (DHRD)
**Synonym:** Malattia Leventinese (ML); Autosomal dominant radial drusen; Autosomal dominant drusen
**MONDO:** MONDO:0007471 · **OMIM:** #126600 · **Gene:** *EFEMP1* (fibulin-3) at 2p16.1 · **Inheritance:** Autosomal dominant · **Category:** Mendelian

**Evidence source note:** This report synthesizes aggregated disease-level resources (OMIM, Orphanet, ClinVar, UniProt) and primary literature (PubMed). It is **not** derived from individual patient EHR data. Evidence types are flagged as *human clinical*, *model organism (mouse)*, *in vitro (iPSC-RPE/cell)*, or *review*. DHRD is rare, so much of the clinical literature consists of case series and single families; mechanistic depth comes from mouse and iPSC models.

---

## Summary

Doyne Honeycomb Retinal Dystrophy (DHRD) and Malattia Leventinese (ML) are the **same autosomal dominant macular dystrophy**, caused by a **single recurrent missense mutation** in *EFEMP1*: **c.1033C>T, p.Arg345Trp (R345W)**, which alters the secreted extracellular-matrix glycoprotein **fibulin-3**. This degree of genetic homogeneity is remarkable: essentially every molecularly confirmed case worldwide carries this one variant, which was mapped to chromosome 2p16-21 and found absent in 477 controls and 494 age-related macular degeneration (AMD) patients, establishing both specificity and the monogenic nature of the disease ([PMID: 10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/)).

Mechanistically, mutant fibulin-3 **misfolds and is retained intracellularly** within retinal pigment epithelium (RPE) cells rather than being efficiently secreted ([PMID: 12242346](https://pubmed.ncbi.nlm.nih.gov/12242346/)). This triggers endoplasmic-reticulum (ER) stress, aberrant extracellular-matrix accumulation, and a downstream cascade of **alternative-pathway complement activation**, **NLRP3-inflammasome inflammation**, and **impaired RPE cholesterol efflux and lysosomal function**. The clinical consequence is the early-adult-onset accumulation of **radial / honeycomb sub-RPE drusen** between the RPE and Bruch's membrane, producing progressive, bilateral central vision loss, sometimes complicated by secondary choroidal neovascularization (CNV).

There is **no approved disease-modifying therapy**; management is supportive (low-vision aids, monitoring, genetic counseling), with intravitreal anti-VEGF reserved for neovascular complications (variable, sometimes absent response). However, the well-defined causal chain has yielded multiple **preclinically validated therapeutic strategies** — GSK3 inhibition, complement factor B inhibition, NLRP3/caspase-1 inhibition, and lysosome modulation (trehalose) — tested in the *Efemp1* R345W knock-in mouse and patient-derived iPSC-RPE. Because DHRD reproduces the drusen biology of AMD from a single clean genetic lesion, it is widely regarded as a **monogenic surrogate model for AMD**.

---

## Key Findings

### F001 — A single recurrent *EFEMP1* R345W mutation causes DHRD/ML

A single heterozygous missense variant — *EFEMP1* **c.1033C>T, p.Arg345Trp (R345W)** — has been identified as the cause in essentially all molecularly confirmed cases of DHRD/ML, inherited in an autosomal dominant pattern. *EFEMP1* encodes the secreted ECM glycoprotein **fibulin-3 (F3)**. Recent case reports from previously unreported populations (the first Scandinavian case, [PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/); Indian cases, [PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)) continue to confirm R345W as the sole recurrent pathogenic variant.

> *"A single variant in EFEMP1: c.1033C>T (R345W) has been identified as the cause in all cases."* — [PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/)

> *"Malattia Leventinese is a rare autosomal dominant macular dystrophy caused by a single"* — [PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)

### F002 — Mutant fibulin-3 misfolds and is retained intracellularly, driving sub-RPE drusen

Marmorstein et al. ([PMID: 12242346](https://pubmed.ncbi.nlm.nih.gov/12242346/)) showed that wild-type EFEMP1 is a secreted protein whereas mutant EFEMP1 (R345W) is **misfolded, secreted inefficiently, and retained within cells**. In ML eyes, EFEMP1 accumulates within RPE cells and between the RPE and drusen; notably, EFEMP1 is **not** a major component of the drusen itself. In AMD eyes, EFEMP1 accumulates beneath the RPE overlying drusen. Patient-derived iPSC-RPE models from ML patients show fibulin-3 and ApoE aggregation, increased ER stress, and enhanced apoptosis ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)).

> *"wild-type EFEMP1 is a secreted protein whereas mutant EFEMP1 is misfolded, secreted inefficiently, and retained within cells"* — [PMID: 12242346](https://pubmed.ncbi.nlm.nih.gov/12242346/)

> *"MAL iPSC-RPE exhibited fibulin-3 and apolipoprotein E (ApoE) aggregation, increased endoplasmic reticulum stress, and enhanced apoptosis"* — [PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)

### F003 — Alternative-pathway complement and NLRP3 inflammasome drive sub-RPE deposits

In *Efemp1* R345W/R345W knock-in mice, aged eyes showed an **~2-fold elevation of complement breakdown products iC3b and Ba (P<0.05)**; deletion of complement factor B (*Cfb*) partially normalized dysregulated pathways, and an **oral factor B inhibitor reduced sub-RPE deposits by 65% (P=0.029)** ([PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)). Genetic removal of *Nlrp3* and its downstream effector caspase-1 (*Casp1*) protected against R345W *Efemp1*-induced basal laminar deposit formation ([PMID: 39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/); [PMID: 41198612](https://pubmed.ncbi.nlm.nih.gov/41198612/)). RNA-seq of knock-in eyecups showed an increased unfolded-protein response, decreased neural-retina mitochondrial function by 3 months, and increased inflammatory pathways by 17 months.

> *"oral dosing of a small molecule FB inhibitor from 10 to 12 months of age reduced sub-RPE deposits by 65% (P = 0.029)"* — [PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)

> *"Complement activation was increased in aged Efemp1ki/ki eyes with an approximately 2-fold elevation of complement breakdown products iC3b and Ba (P < 0.05)"* — [PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)

> *"we directly tested the role of Nlrp3 and its downstream effector, caspase 1 (Casp1) in mediating early AMD-like pathology"* — [PMID: 39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/)

### F004 — DHRD/ML maps to 2p16-21; R345W absent in controls and AMD cohorts (specificity)

Stone et al. (1999, [PMID: 10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/)) mapped both ML and DHRD loci to **chromosome 2p16-21** and identified a single non-conservative Arg345Trp mutation in *EFEMP1* in all families studied. The change was **absent in 477 control individuals and in 494 AMD patients**, establishing disease specificity and distinguishing DHRD/ML genetically from common AMD.

> *"a single non-conservative mutation (Arg345Trp) in the gene EFEMP1 ... in all families studied. This change was not present in 477 control individuals or in 494 patients with age-related macular degeneration"* — [PMID: 10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/)

### F005 — Phenotype: early-onset radial/honeycomb sub-RPE drusen with variable expressivity, CNV, central vision loss

Clinical reports consistently describe **early-onset (typically 2nd–4th decade)** yellow-white drusen beneath the RPE, often **radially distributed** around the macula and nasal to the optic disc, which coalesce into a **honeycomb** pattern. Drusen show increased fundus autofluorescence. Complications include RPE changes and secondary CNV. Marked **intra- and inter-familial phenotypic variability** in visual loss and imaging findings occurs despite the identical genotype ([PMID: 25111685](https://pubmed.ncbi.nlm.nih.gov/25111685/); [PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/); [PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)).

> *"Intrafamilial patients with Malattia leventinese/Doyne honeycomb retinal dystrophy seem to be phenotypically variable in visual loss, ophthalmoscopic findings, autofluorescence imaging, and optical coherence tomography changes"* — [PMID: 25111685](https://pubmed.ncbi.nlm.nih.gov/25111685/)

> *"All cases exhibited early-onset central vision loss and small, radially distributed drusen, consistent with ML/DHRD"* — [PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)

### F006 — No approved disease-modifying therapy; supportive care with emerging preclinical targets

No approved therapy halts DHRD/ML progression; care is supportive (low-vision aids, monitoring, genetic counseling). Secondary CNV is treated with intravitreal anti-VEGF, though responses are variable and sometimes absent ([PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/)). Nanosecond **2RT laser** has been piloted and may stabilize some functional parameters without structural change ([PMID: 38023612](https://pubmed.ncbi.nlm.nih.gov/38023612/)). Preclinical disease-modifying strategies target the causal pathway: **GSK3 inhibition (CHIR99021)** reduced R345W-associated basal laminar deposits ([PMID: 39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/)); an **oral complement factor B inhibitor** reduced sub-RPE deposits by 65% ([PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)); **NLRP3/caspase-1 ablation** prevented deposits ([PMID: 39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/)); and the lysosome modulator **trehalose** reduced drusen-like deposits in patient iPSC-RPE ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)).

> *"treatment of 8-month-old R345W+/+ knockin mice with CHIR (25 mg/kg i.p., 1 mo) was well tolerated and significantly reduced R345W F3-associated AMD-like basal laminar deposit number and size, thereby preventing the main pathological feature in these mice"* — [PMID: 39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/)

> *"2RT treatment in DHRD may improve or stabilize some retinal function parameters without significant structural changes"* — [PMID: 38023612](https://pubmed.ncbi.nlm.nih.gov/38023612/)

> *"Secondary choroidal neovascularizations were identified on both eyes, and anti-vascular endothelial growth factor was administered, without effect"* — [PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/)

### F007 — Disease models: *Efemp1* R345W knock-in mouse and patient iPSC-RPE recapitulate sub-RPE/basal laminar deposits

The principal in vivo model is the **Efemp1 p.R345W knock-in mouse** (Efemp1ki/ki; R345W+/+), which develops microscopic basal laminar deposits (BLamDs) — an early feature of DHRD/ML and AMD — alongside increased unfolded-protein response, decreased neural-retina mitochondrial function by 3 months, increased inflammatory/complement pathways by 17 months, and a sex difference (females > males). A **HiBiT luminescent tag** knocked into the endogenous F3 locus enables high-throughput fibulin-3 detection for drug screening ([PMID: 39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/)). In vitro, **patient-derived iPSC-RPE** recapitulate fibulin-3/ApoE aggregation, ER stress, apoptosis, and (with photoreceptor outer-segment feeding) drusen-like deposits containing ApoE, complement, and collagen IV ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)); isogenic DHRD iPSC-RPE revealed impaired cholesterol efflux via CES1 downregulation ([PMID: 33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/)).

> *"Aged Efemp1 R345W/R345W knock-in mice (Efemp1ki/ki) develop microscopic deposits on the basal side of retinal pigment epithelial cells (RPE), an early feature in DHRD/ML and AMD"* — [PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)

> *"Long-term culture with photoreceptor outer segments led to drusen-like deposits containing ApoE, complement components, and collagen IV accumulation"* — [PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)

### F008 — Lipid/cholesterol dysregulation and lysosomal dysfunction are downstream RPE pathologies

DHRD iPSC-RPE exhibit abnormal intracellular lipid-droplet accumulation and pericellular lipid-rich deposits, driven by **downregulation of carboxylesterase 1 (CES1)** — impairing conversion of cholesteryl ester to free cholesterol and thus cholesterol efflux ([PMID: 33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/)). CES1 knockdown or EFEMP1 overexpression reproduced lipid accumulation. Independently, ML iPSC-RPE show **lysosomal dysfunction with reduced TFEB** transcripts and altered lysosomal gene programs, plus increased hexosylceramide and bis(monoacylglycero)phosphate; trehalose restored lysosomal function and reduced drusen-like deposits, MMP2 activation, and apoptosis ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)).

> *"we detected significant downregulation of carboxylesterase 1 (CES1), an enzyme that converts cholesteryl ester to free cholesterol, an indispensable process in cholesterol export"* — [PMID: 33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/)

> *"A key pathological feature was lysosomal dysfunction associated with altered regulation of lysosomal gene programs, including reduced transcription factor EB transcript levels"* — [PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)

### F009 — Diagnosis rests on multimodal retinal imaging plus *EFEMP1* genetic confirmation

Multimodal imaging defines the diagnostic signature: large round drusen in the perimacular area and around the optic disc, and small non-round, radially distributed drusen temporal to the macula. **Fundus autofluorescence (FAF)** shows intense autofluorescence of large drusen; on **fluorescein (FA)/indocyanine green (ICGA) angiography**, large round drusen become hyperfluorescent late while small radial drusen decrease fluorescence; **OCT** shows hyperreflective material between RPE and Bruch's membrane causing focal dome-shaped or diffuse RPE elevation ([PMID: 22814526](https://pubmed.ncbi.nlm.nih.gov/22814526/)). Best-corrected visual acuity ranged 20/25 to 20/200. Definitive diagnosis is molecular: detection of heterozygous *EFEMP1* c.1033C>T (p.Arg345Trp) by single-gene testing, inherited retinal disease gene panels, or exome sequencing ([PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)).

> *"OCT showed the large round drusen as focal or diffuse deposition of hyperreflective material between the RPE and Bruch membrane within the macula, determining focal dome-shaped or diffuse RPE elevation"* — [PMID: 22814526](https://pubmed.ncbi.nlm.nih.gov/22814526/)

> *"The smallest drusen were not round, radially distributed, mostly localized temporally to the macula"* — [PMID: 22814526](https://pubmed.ncbi.nlm.nih.gov/22814526/)

### F010 — DHRD/ML is a monogenic surrogate model for AMD; fibulin-3 regulates Bruch's-membrane ECM and MMP/TIMP3 balance

A 2026 review frames DHRD as *"a monogenic disorder that serves as a surrogate model for AMD due to similar phenotypic manifestations,"* focusing on interactions between EFEMP1, matrix metalloproteinases (MMPs), tissue inhibitor of metalloproteinases-3 (TIMP3), and complement factors, and states the EFEMP1 R345W mutation *"causes rapid disease progression through impaired protein secretion, abnormal matrix accumulation, and complement dysregulation"* ([PMID: 42569289](https://pubmed.ncbi.nlm.nih.gov/42569289/)). In both DHRD/ML and AMD, drusen form as extracellular deposits between RPE and Bruch's membrane, and both share alternative-complement activation (factor H/factor B axis; [PMID: 17659362](https://pubmed.ncbi.nlm.nih.gov/17659362/)).

> *"Doyne Honeycomb Retinal Dystrophy-a monogenic disorder that serves as a surrogate model for AMD due to similar phenotypic manifestations"* — [PMID: 42569289](https://pubmed.ncbi.nlm.nih.gov/42569289/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A germline heterozygous *EFEMP1* **c.1033C>T (p.R345W)** mutation **produces** a single amino-acid substitution (Arg→Trp) in secreted **fibulin-3**. *(demonstrated — [PMID: 10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/))*
2. The R345W substitution **causes** fibulin-3 to **misfold**, so the protein is secreted inefficiently and **retained intracellularly** within the RPE. *(demonstrated — [PMID: 12242346](https://pubmed.ncbi.nlm.nih.gov/12242346/))*
3. Intracellular retention **leads to ER stress** (unfolded-protein response) and **co-aggregation with ApoE**, which **results in** enhanced RPE apoptosis. *(demonstrated in iPSC-RPE and knock-in eyecups — [PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/))*
4. **Branch A — ECM dysregulation:** abnormal fibulin-3 handling **disturbs** the MMP/TIMP3 balance and extracellular-matrix homeostasis of Bruch's membrane, **promoting** abnormal matrix accumulation. *(mechanistic review — [PMID: 42569289](https://pubmed.ncbi.nlm.nih.gov/42569289/))*
5. **Branch B — Complement:** sub-RPE changes **activate** the alternative complement pathway (↑iC3b, ↑Ba; factor B–dependent), which **drives** sub-RPE deposit accumulation. *(demonstrated — [PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/))*
6. **Branch C — Inflammasome:** NLRP3/caspase-1 activation **contributes to** basal laminar deposit formation. *(demonstrated by genetic ablation — [PMID: 39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/))*
7. **Branch D — Lipid/lysosome:** CES1 downregulation **impairs** cholesterol efflux → lipid-droplet accumulation; reduced TFEB **causes** lysosomal dysfunction → impaired clearance. *(demonstrated in iPSC-RPE — [PMID: 33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/); [PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/))*
8. Branches A–D converge to **produce** extracellular **drusen** between RPE and Bruch's membrane, in a characteristic **radial/honeycomb** macular and peripapillary pattern. *(demonstrated — [PMID: 22814526](https://pubmed.ncbi.nlm.nih.gov/22814526/))*
9. Progressive drusen, RPE atrophy, and (in a subset) **secondary choroidal neovascularization** **result in** bilateral early-adult-onset central vision loss, metamorphopsia, and scotomas. *(demonstrated — [PMID: 25111685](https://pubmed.ncbi.nlm.nih.gov/25111685/); [PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/))*

```
EFEMP1 R345W → fibulin-3 misfolding → intracellular retention / ER stress / ApoE co-aggregation → RPE apoptosis
                                              │
            ┌─────────────────┬──────────────┼─────────────────┬───────────────────┐
            ▼                 ▼               ▼                 ▼                   ▼
       ECM / MMP-TIMP3   Alternative     NLRP3 / Casp1    CES1↓ cholesterol    TFEB↓ lysosomal
       dysregulation     complement      inflammasome     efflux impaired      dysfunction
            └─────────────────┴──────────────┴─────────────────┴───────────────────┘
                                              ▼
                      Sub-RPE / basal-laminar DRUSEN (radial → honeycomb)
                                              ▼
                RPE atrophy ± secondary CNV  →  bilateral central vision loss
```

**Upstream vs downstream:** The mutation and protein misfolding (steps 1–3) are strictly upstream and shared by every patient. Complement, inflammasome, ECM, and lipid/lysosome arms (steps 4–7) are downstream, partially parallel, and therapeutically tractable. Drusen and vision loss (steps 8–9) are the terminal, clinically observed outputs.

**Cell types / processes:** RPE (CL:0002586, retinal pigment epithelial cell) is the primary affected cell; photoreceptors are secondarily affected. Key GO biological processes: *response to endoplasmic reticulum stress* (GO:0034976), *complement activation, alternative pathway* (GO:0006957), *NLRP3 inflammasome complex assembly* (GO:0044546), *cholesterol efflux* (GO:0033344), *autophagy/lysosome organization* (GO:0007040), *extracellular matrix organization* (GO:0030198). Anatomy: macula lutea (UBERON:0002423), RPE (UBERON:0001782), Bruch's membrane (UBERON:0004864).

---

## Section-by-Section Report

### 1. Disease Information
DHRD is a rare, autosomal dominant, bilateral **macular dystrophy** characterized by early-onset sub-RPE drusen forming a honeycomb pattern. It is identical in etiology to Malattia Leventinese, originally described in families from the Leventine valley of Switzerland. **Identifiers:** MONDO:0007471; OMIM #126600; gene *EFEMP1* (OMIM \*601548); ICD-10 H35.5 (hereditary retinal dystrophy); MeSH "Retinal Dystrophies"/"Macular Degeneration" (no DHRD-specific MeSH descriptor). **Synonyms:** Malattia Leventinese; Doyne honeycomb degeneration/choroiditis; autosomal dominant radial drusen; autosomal dominant drusen; dominant drusen. Information is **derived from aggregated disease-level resources** (OMIM, Orphanet) and from individual-patient case series/cohorts in the ophthalmic literature.

### 2. Etiology
**Causal factor:** purely genetic — a single heterozygous *EFEMP1* R345W mutation (F001, F004). **Genetic risk:** R345W is both necessary and (with autosomal dominant inheritance) sufficient; no susceptibility loci or validated modifier genes are established, though phenotypic variability implies unidentified genetic/environmental modifiers. **Environmental/lifestyle risk factors, protective factors, infectious agents, and gene–environment interactions are not established** for this monogenic disease. Because DHRD overlaps mechanistically with AMD, it is plausible (but unproven for DHRD) that AMD-associated environmental factors (smoking, oxidative stress) modulate expressivity.

### 3. Phenotypes
| Phenotype | Type | HPO term | Onset | Progression | Frequency |
|---|---|---|---|---|---|
| Macular/peripapillary drusen (radial → honeycomb) | Clinical sign | HP:0011506 (Macular drusen) | 2nd–4th decade | Progressive | Near-universal (hallmark) |
| Reduced central visual acuity | Symptom | HP:0007663 / HP:0000572 (central scotoma) | Early–mid adult | Progressive, variable | Common |
| Metamorphopsia | Symptom | HP:0012508 | Adult | Variable | Common |
| RPE atrophy/changes | Clinical sign | HP:0007814 | Adult | Progressive | Subset |
| Choroidal neovascularization | Clinical sign | HP:0030500 | Adult | Episodic complication | Subset |
| Abnormal fundus autofluorescence | Lab/imaging | — | Adult | Progressive | Characteristic |

Severity and progression are **variable even within families** sharing R345W ([PMID: 25111685](https://pubmed.ncbi.nlm.nih.gov/25111685/)). **Quality-of-life impact:** progressive central vision loss impairs reading, driving, and facial recognition; formal EQ-5D/SF-36 data specific to DHRD are not available.

### 4. Genetic / Molecular Information
**Causal gene:** *EFEMP1* (HGNC:3218; fibulin-3; 2p16.1; OMIM \*601548). **Pathogenic variant:** c.1033C>T, p.Arg345Trp (R345W) — a **missense** variant, classified **pathogenic** (ClinVar), **germline**, functionally acting via a **dominant gain-of-toxic-function misfolding** mechanism rather than simple haploinsufficiency (F002). **Allele frequency:** effectively absent in population databases and in 477 controls / 494 AMD cases ([PMID: 10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/)). **Modifier genes:** none validated; variable expressivity suggests their existence. **Epigenetic information:** none specific to DHRD. **Chromosomal abnormalities:** none — this is a point mutation.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established for DHRD; it is a Mendelian point-mutation disorder. Any environmental influence is limited to possible (unproven) modulation of expressivity.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain and branch diagram. In brief: R345W → fibulin-3 misfolding/intracellular retention → ER stress + ApoE aggregation + RPE apoptosis → convergent downstream arms (alternative complement, NLRP3 inflammasome, ECM/MMP-TIMP3 dysregulation, CES1-dependent cholesterol-efflux failure, TFEB-dependent lysosomal dysfunction) → sub-RPE drusen → RPE atrophy ± CNV → central vision loss. Molecular profiling (knock-in RNA-seq) shows early unfolded-protein response and mitochondrial decline, with later inflammatory/complement upregulation ([PMID: 35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/)). Lipidomics of ML iPSC-RPE shows increased hexosylceramide and BMP ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/)).

### 7. Anatomical Structures Affected
**Organ:** eye — specifically the **macula** (UBERON:0002423) and peripapillary retina. **Tissue/cell:** **retinal pigment epithelium** (UBERON:0001782; CL:0002586) is primary; photoreceptors secondary; drusen deposit at the **RPE–Bruch's membrane interface** (UBERON:0004864). **Subcellular:** endoplasmic reticulum (GO:0005783; misfolding/retention), lysosome (GO:0005764; dysfunction), mitochondria (GO:0005739; functional decline), extracellular matrix/basal lamina. **Localization:** bilateral, macular + peripapillary (nasal to optic disc).

### 8. Temporal Development
**Onset:** typically 2nd–4th decade (early adult); insidious/chronic. Drusen may be detectable before symptoms. **Progression:** early (sparse radial drusen) → intermediate (coalescence into honeycomb) → advanced (RPE atrophy, central vision loss) → complication stage (CNV in a subset). Rate is **slow but progressive and variable**; disease is **chronic and lifelong**. **Patterns:** no spontaneous remission; CNV episodes are episodic. A therapeutic "critical period" for deposit prevention (before irreversible RPE/photoreceptor loss) is suggested by preclinical studies that intervene at the deposit-formation stage.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant, **high/near-complete but age-dependent penetrance**, with **variable expressivity** (F005). **Epidemiology:** rare; precise prevalence/incidence not well quantified. Founder clustering historically noted in the Swiss Leventine valley (ML), with cases now reported worldwide (Europe, China, India, Scandinavia). **No genetic anticipation** (not a repeat-expansion disorder). Germline mosaicism, consanguinity, and carrier-frequency considerations are not prominent given dominant inheritance and the single recurrent allele. **Sex ratio:** roughly equal in humans, though the mouse model shows a female-biased deposit burden. Age distribution skews toward adult diagnosis.

### 10. Diagnostics
**Clinical/imaging** (F009): fundoscopy (radial/honeycomb drusen), **OCT** (hyperreflective sub-RPE material, dome-shaped RPE elevation), **FAF** (intense drusen autofluorescence), **FA/ICGA** (late hyperfluorescence of large drusen). Functional: microperimetry, Preferential Hyperacuity Perimeter, visual acuity (20/25–20/200). **Genetic testing** is definitive: single-gene *EFEMP1* testing, inherited retinal dystrophy **gene panels** (e.g., Illumina MiSeq), or **WES/WGS** detecting heterozygous c.1033C>T. Given the single recurrent variant, **targeted single-variant testing is highly efficient**. **Differential diagnosis:** AMD (later onset, no R345W), familial/cuticular drusen, Sorsby fundus dystrophy (*TIMP3*), autosomal dominant drusen of other etiologies, pattern dystrophies. **Screening:** cascade/predictive genetic testing of at-risk relatives.

### 11. Outcome / Prognosis
DHRD is **not life-threatening**; survival and mortality are unaffected. Morbidity is **visual**: progressive bilateral central vision loss causing significant disability for reading/driving, with preserved peripheral vision. CNV, when it occurs, accelerates central loss. **Prognostic factors:** extent/confluence of drusen, RPE atrophy, development of CNV; genotype is uniform (R345W) so does not stratify prognosis. No validated molecular prognostic biomarkers specific to DHRD. Recovery potential is limited once atrophy develops.

### 12. Treatment
**No approved disease-modifying therapy** (F006). **Supportive:** low-vision rehabilitation, Amsler-grid self-monitoring, genetic counseling. **Neovascular complications:** intravitreal **anti-VEGF** (bevacizumab/ranibizumab/aflibercept; NCIT: Anti-VEGF Therapy) — response variable, sometimes absent ([PMID: 33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/)). **Interventional (experimental):** nanosecond **2RT laser** — functional stabilization without structural change ([PMID: 38023612](https://pubmed.ncbi.nlm.nih.gov/38023612/)). **Preclinically validated disease-modifying candidates:**

| Strategy | Agent | Model | Effect | PMID |
|---|---|---|---|---|
| GSK3 inhibition | CHIR99021 (25 mg/kg i.p., 1 mo) | R345W+/+ mouse | ↓ basal laminar deposit number & size | [39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/) |
| Complement factor B inhibition | Oral small-molecule FB inhibitor | Efemp1ki/ki mouse | Sub-RPE deposits −65% (P=0.029) | [35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/) |
| NLRP3/caspase-1 inhibition | Genetic ablation (*Nlrp3*, *Casp1*) | R345W mouse | Prevented basal laminar deposits | [39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/) |
| Lysosome modulation | Trehalose | ML iPSC-RPE | ↓ drusen-like deposits, MMP2, apoptosis | [42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/) |

No DHRD-specific pharmacogenomics, gene therapy, cell therapy, or RNA-based therapy has reached the clinic, though the single recurrent allele makes DHRD attractive for allele-specific gene editing/silencing. Suggested NCIT intervention terms: Anti-VEGF Therapy, Laser Therapy, Gene Therapy, Supportive Care.

### 13. Prevention
No primary prevention exists for a germline Mendelian disease. **Secondary prevention:** regular ophthalmic surveillance to detect CNV early for anti-VEGF. **Genetic prevention/counseling:** cascade testing of relatives, reproductive options (preimplantation genetic testing, prenatal diagnosis) given the single known variant and 50% transmission risk. **Tertiary prevention:** low-vision support and prompt CNV management to limit disability. No immunization or public-health/environmental interventions apply.

### 14. Other Species / Natural Disease
No naturally occurring R345W-driven DHRD/ML is documented in companion or wild animals (no OMIA entry for this specific disease). **Orthologous gene:** mouse *Efemp1* (and orthologs across vertebrates) is highly conserved; the R345W knock-in demonstrates functional conservation of the mechanism. No zoonotic or cross-species transmission applies (non-infectious genetic disease).

### 15. Model Organisms
**In vivo:** the **Efemp1 p.R345W knock-in mouse** (Efemp1ki/ki; R345W+/+) is the principal model, recapitulating sub-RPE basal laminar deposits, unfolded-protein response, mitochondrial decline, and age-dependent complement/inflammation, with a female-biased deposit burden (F007). A **HiBiT-tagged F3 locus** mouse enables high-throughput fibulin-3 quantification for drug screening ([PMID: 39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/)). **In vitro:** **patient-derived iPSC-RPE** (and isogenic CRISPR-corrected controls) reproduce fibulin-3/ApoE aggregation, ER stress, apoptosis, CES1-dependent lipid accumulation, TFEB-linked lysosomal dysfunction, and (with outer-segment feeding) drusen-like deposits ([PMID: 42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/); [PMID: 33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/)). **Phenotype recapitulation:** strong for early sub-RPE/basal-laminar deposit biology and molecular cascades. **Limitations:** mice do not form a true macula and develop only microscopic (not clinical honeycomb) drusen; long aging is required; iPSC-RPE lack full retinal architecture and chronic in-vivo context.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [10369267](https://pubmed.ncbi.nlm.nih.gov/10369267/) | Single *EFEMP1* mutation for ML and DHRD | Human genetic | F001, F004 (single causal variant, 2p16-21, specificity) |
| [12242346](https://pubmed.ncbi.nlm.nih.gov/12242346/) | Aberrant EFEMP1 accumulation underlies drusen | Human tissue / in vitro | F002, F010 (misfolding, intracellular retention) |
| [25111685](https://pubmed.ncbi.nlm.nih.gov/25111685/) | ML/DHRD Chinese family | Human clinical | F005 (variable expressivity, CNV, FAF) |
| [22814526](https://pubmed.ncbi.nlm.nih.gov/22814526/) | Multimodal characterization of ML | Human clinical/imaging | F009 (OCT, FAF, FA/ICGA, radial drusen) |
| [33689237](https://pubmed.ncbi.nlm.nih.gov/33689237/) | First Scandinavian DHRD case | Human clinical | F001, F005, F006 (R345W, CNV, anti-VEGF no effect) |
| [41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/) | Early-onset drusen in ML (Indian cases) | Human clinical/genetic | F001, F005, F009 (single variant, radial drusen, panel testing) |
| [35943778](https://pubmed.ncbi.nlm.nih.gov/35943778/) | Complement factor B critical for sub-RPE deposits | Mouse model | F003, F007 (complement, knock-in model, FB inhibitor) |
| [39464028](https://pubmed.ncbi.nlm.nih.gov/39464028/) | *Nlrp3* removal protects against deposits | Mouse model | F003, F006 (inflammasome) |
| [41198612](https://pubmed.ncbi.nlm.nih.gov/41198612/) | *Nlrp3* removal (R345W) | Mouse model | F003 (NLRP3/caspase-1 in BLamDs) |
| [39114980](https://pubmed.ncbi.nlm.nih.gov/39114980/) | GSK3 inhibition prevents AMD-like pathology | Mouse model | F006, F007 (CHIR99021, HiBiT model) |
| [42484373](https://pubmed.ncbi.nlm.nih.gov/42484373/) | Restoring lysosomal function (trehalose) in ML | iPSC-RPE | F002, F007, F008 (aggregation, lysosome, TFEB, trehalose) |
| [33909993](https://pubmed.ncbi.nlm.nih.gov/33909993/) | Impaired cholesterol efflux in juvenile macular degeneration | iPSC-RPE | F007, F008 (CES1, lipid efflux) |
| [38023612](https://pubmed.ncbi.nlm.nih.gov/38023612/) | Nanosecond 2RT laser in DHRD | Human case series | F006 (interventional functional benefit) |
| [42569289](https://pubmed.ncbi.nlm.nih.gov/42569289/) | EFEMP1–TIMP3 interactions & AMD relevance | Review | F010 (monogenic surrogate for AMD, MMP/TIMP3) |
| [17659362](https://pubmed.ncbi.nlm.nih.gov/17659362/) | Molecular biology of AMD | Review | F010 (alternative complement in AMD) |
| [32911658](https://pubmed.ncbi.nlm.nih.gov/32911658/) | Pathophysiological significance of fibulin-3 | Review | F002, F010 (fibulin-3 biology) |

---

## Limitations and Knowledge Gaps

- **Epidemiology is poorly quantified.** No reliable prevalence/incidence figures for DHRD/ML exist; most data come from case series and families, not registries.
- **Mechanism of dominance is incompletely resolved.** Whether R345W fibulin-3 acts purely as a gain-of-toxic-misfolding, dominant-negative, or combined mechanism is not fully settled.
- **Modifiers of expressivity are unknown.** Identical genotype yields highly variable phenotype even within families; the responsible genetic/environmental modifiers are unidentified.
- **Model limitations.** Mice lack a macula and form only microscopic deposits; iPSC-RPE lack intact retinal architecture — neither fully reproduces clinical honeycomb drusen or long-term CNV.
- **No human therapeutic trials of the preclinical targets.** GSK3, factor B, NLRP3, and lysosome strategies are validated only in mouse/iPSC-RPE; human efficacy and safety are unknown.
- **Quality-of-life data are absent.** No DHRD-specific EQ-5D/SF-36/PROMIS outcomes have been reported.
- **Causal-chain branch ordering is partly inferred.** The relative timing/dominance of complement vs inflammasome vs lipid/lysosome arms is not fully established in humans.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry** — establish a multicenter DHRD/ML cohort with standardized multimodal imaging to quantify prevalence, progression rate, CNV incidence, and vision-loss trajectories.
2. **Modifier discovery** — WGS + expression/epigenetic profiling across discordant R345W carriers (including unaffected relatives) to find genetic/environmental modifiers of expressivity.
3. **Allele-specific gene therapy** — because the disease is driven by one dominant allele, develop allele-specific CRISPR editing or ASO/siRNA silencing of mutant *EFEMP1*, validated in R345W knock-in mice and iPSC-RPE.
4. **Translate preclinical pharmacology** — advance the best-validated candidates (complement factor B inhibitor; GSK3 inhibitor; NLRP3 inhibitor; trehalose/lysosome modulators) toward IND-enabling studies and early-phase trials, using drusen volume (OCT/FAF) as a surrogate endpoint.
5. **Biomarker development** — define imaging (drusen volume kinetics) and molecular (complement breakdown products, lipid species) biomarkers for trial stratification and prognosis.
6. **Improved models** — generate macula-bearing or longer-lived models (e.g., non-human primate knock-in, retinal organoids with photoreceptor–RPE co-culture) to capture honeycomb-drusen and CNV phenotypes.
7. **Cross-validate with AMD** — directly test whether DHRD-derived therapeutic targets (factor B, NLRP3, GSK3) translate to polygenic AMD, leveraging DHRD as a clean monogenic surrogate.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 18 reviewed papers. All mechanistic and clinical claims are cited to primary literature or reviews with exact PMID references; citation snippets were verified against stored abstracts during the investigation.*


## Artifacts

- [OpenScientist final report](Doyne_Honeycomb_Retinal_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Doyne_Honeycomb_Retinal_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002423` (2 mentions) - the report calls it "macula"; UBERON calls it **hepatobiliary system**
- `UBERON:0004864` (2 mentions) - the report calls it "RPE–Bruch's membrane interface"; UBERON calls it **vasculature of retina**
- `HP:0011506` (1 mention) - the report calls it "Macular drusen"; HP calls it **Choroidal neovascularization**
- `HP:0012508` (1 mention) - the report calls it "Symptom"; HP calls it **Metamorphopsia**
- `HP:0007814` (1 mention) - the report calls it "Clinical sign"; HP calls it **Retinal pigment epithelial mottling**
- `HP:0030500` (1 mention) - the report calls it "Clinical sign"; HP calls it **Yellow/white macular lesion**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007040` (1 mention) - the report calls it "autophagy/lysosome organization"; GO calls it **lysosome organization**