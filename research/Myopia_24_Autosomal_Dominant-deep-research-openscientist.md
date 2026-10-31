---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T20:31:34.675112'
end_time: '2026-10-22T21:23:59.679314'
duration_seconds: 3145.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Myopia 24, Autosomal Dominant
  mondo_id: MONDO:0014411
  category: Mendelian
  causal_genes: not recorded
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
citation_count: 15
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:24891338
  relevance_assessed: 18
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 15
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0014411
    reported_labels:
    - MONDO
    ontology_label: myopia 24, autosomal dominant
  - term_id: HP:0012801
    reported_labels:
    - Increased axial length of the globe
    - Increased axial length
    ontology_label: Narrow jaw
  - term_id: HP:0007917
    reported_labels:
    - Posterior staphyloma
    ontology_label: Tractional retinal detachment
  - term_id: GO:0005385
    reported_labels:
    - zinc ion transmembrane transporter activity
    - Zinc transport
    ontology_label: zinc ion transmembrane transporter activity
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Myopia_24_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Myopia_24_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopia 24, Autosomal Dominant
- **MONDO ID:** MONDO:0014411 (if available)
- **Causal gene(s):** not recorded
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

Please provide a comprehensive research report on **Myopia 24, Autosomal Dominant** covering all of the
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

# Myopia 24, Autosomal Dominant (MYP24): A Comprehensive Disease Characterization

**MONDO:0014411 · OMIM #615420 · Causal gene: _SLC39A5_ (ZIP5) · HGNC:20502 · 12q13.3**

---

## Summary

**Myopia 24, autosomal dominant (MYP24)** is a rare Mendelian form of non-syndromic high (axial) myopia caused by heterozygous, damaging variants in **_SLC39A5_**, the gene encoding the basolateral zinc-uptake transporter **ZIP5**. The disease was defined molecularly by Guo et al. in 2014, who used whole-genome linkage plus exome sequencing to identify a co-segregating nonsense mutation (c.141C>G, p.Y47*) in a multigenerational Chinese family with severe high myopia, with additional variants in independent families and sporadic cases [PMID: 24891338]. The disease name "Myopia 24" is a serial locus designation and does not itself name the gene; the correct and intended gene for MONDO:0014411 / OMIM #615420 is _SLC39A5_, and this report follows that identifier anchor throughout.

Mechanistically, MYP24 is a disorder of **scleral extracellular-matrix (ECM) homeostasis**. Reduced ZIP5 function lowers intracellular zinc in scleral fibroblasts, which destabilizes Smad proteins and inhibits BMP/TGF-β signalling, thereby decreasing transcription of collagen and other ECM genes (COL1A1, COL2A1, COL4A1, FN1, LAMA1). The weakened sclera permits excessive posterior-globe elongation, producing early-onset, progressive axial high myopia (spherical equivalent ≤ −6.00 D; axial length typically > 26 mm). Because axial elongation itself is the proximate driver of sight-threatening complications — myopic maculopathy, posterior staphyloma, choroidal neovascularization, retinal detachment, cataract, and glaucoma — the long-term morbidity of MYP24 is visual rather than life-limiting.

There is **no gene-specific or zinc-targeted therapy** for MYP24. Management mirrors general high-myopia care: optical refractive correction, pediatric axial-elongation control (low-dose atropine, orthokeratology, defocus/aspherical-lenslet spectacles), encouragement of protective outdoor time, and lifelong retinal surveillance for complications. The gene–disease relationship, while reproducible, rests on a limited number of families and cohorts that are overwhelmingly East Asian (Chinese), and several reported variants remain candidate/VUS rather than definitively curated in ClinVar/ClinGen.

---

## Key Findings

### Finding 1 — MYP24 is caused by heterozygous _SLC39A5_ (ZIP5) mutations

MYP24 (MONDO:0014411; OMIM #615420) is an autosomal dominant, non-syndromic high myopia caused by heterozygous mutations in **_SLC39A5_** on chromosome **12q13.3**, which encodes the zinc transporter **ZIP5**. The defining study combined whole-genome linkage analysis with exome sequencing in a non-syndromic severe high myopia family and identified a nonsense mutation co-segregating with the phenotype; the same variant appeared in an unrelated sporadic case, and a second missense variant co-segregated in a separate family. Neither variant was present in 1,276 controls.

> "We identified a nonsense mutation (c.141C>G:p.Y47*) in SLC39A5 co-segregating with the phenotype in a non-syndromic severe high myopia family. The same nonsense mutation (c.141C>G:p.Y47*) was detected in a sporadic case and a missense mutation (c.911T>C:p.M304T) was identified and co-segregated in another family" — [PMID: 24891338](https://pubmed.ncbi.nlm.nih.gov/24891338/)

Consolidated gene identifiers: **_SLC39A5_**, HGNC:20502, NCBI Gene 283375, Ensembl ENSG00000139053, UniProt Q6ZMH5, OMIM *608730; protein product **ZIP5** (SLC39 / ZIP family zinc transporter).

### Finding 2 — Disease mechanism: a zinc → Smad → TGF-β → scleral ECM axis

The causal variants disrupt a signalling cascade that controls scleral collagen/ECM synthesis. Wild-type (but not disease-associated) SLC39A5 regulates Smad1, a key phosphoprotein downstream of the BMP/TGF-β pathway, and SLC39A5 is abundantly expressed in the sclera and retina during eye development [PMID: 24891338]. Functional dissection in cells showed that SLC39A5 loss produces zinc deficiency that destabilizes Smad proteins, inhibiting TGF-β signalling and downstream ECM synthesis; re-expression rescues the phenotype [PMID: 34302427].

> "the SLC39A5 depletion-induced zinc deficiency destabilized Smad proteins, which inhibited the TGF-β signalling and downstream ECM synthesis, thus contributing to the pathogenesis" — [PMID: 34302427](https://pubmed.ncbi.nlm.nih.gov/34302427/)

> "wild-type, but not disease-associated SLC39A5 inhibited the expression of Smad1, a key phosphate protein in the downstream of the BMP/TGF-β (bone morphogenic protein/transforming growth factor-β) pathway" — [PMID: 24891338](https://pubmed.ncbi.nlm.nih.gov/24891338/)

SLC39A5-knockout HEK293 cells show migration/morphogenesis defects and reduced transcription of ECM genes COL1A1, COL2A1, COL4A1, FN1, and LAMA1, via blocked R-Smad phosphorylation [PMID: 34302427].

### Finding 3 — Pathogenic variant spectrum

Reported heterozygous _SLC39A5_ variants in non-syndromic high myopia span nonsense, frameshift, and missense classes, all rare/absent in population databases (gnomAD, 1000G, ExAC; AF < 0.01) and predicted damaging by multiple in-silico tools (SIFT, PolyPhen-2, PROVEAN, etc.):

| Variant (cDNA) | Protein | Class | Source | PMID |
|---|---|---|---|---|
| c.141C>G | p.Y47* | Nonsense | Guo 2014 | [24891338](https://pubmed.ncbi.nlm.nih.gov/24891338/) |
| c.911T>C | p.M304T | Missense | Guo 2014 | [24891338](https://pubmed.ncbi.nlm.nih.gov/24891338/) |
| c.1238G>C | p.G413A | Missense | Jiang 2014 | [25525168](https://pubmed.ncbi.nlm.nih.gov/25525168/) |
| c.860C>T | p.P287L | Missense | Feng 2017 | [28442722](https://pubmed.ncbi.nlm.nih.gov/28442722/) |
| c.956G>C | p.R319T | Missense | Feng 2017 | [28442722](https://pubmed.ncbi.nlm.nih.gov/28442722/) |
| c.726dupA | p.Arg243fs*140 | Frameshift | Liu 2020 | [32215939](https://pubmed.ncbi.nlm.nih.gov/32215939/) |
| c.145G>A | p.E49K | Missense | Ye 2023 | [36964802](https://pubmed.ncbi.nlm.nih.gov/36964802/) |
| c.325G>T | p.G109W | Missense | Ye 2023 | [36964802](https://pubmed.ncbi.nlm.nih.gov/36964802/) |
| c.577G>A | — | Missense | Liu 2025 | [40920702](https://pubmed.ncbi.nlm.nih.gov/40920702/) |

> "one novel frameshift mutation (c.726dupA, p.Arg243fs*140) in SLC39A5" — [PMID: 32215939](https://pubmed.ncbi.nlm.nih.gov/32215939/)

> "three novel missense mutations, c.860C > T, p.Pro287Leu and c.956G > C, p.Arg319Thr in SLC39A5" — [PMID: 28442722](https://pubmed.ncbi.nlm.nih.gov/28442722/)

The combination of a clear nonsense/frameshift (loss-of-function) spectrum and the functional evidence that wild-type ZIP5 is required for Smad/TGF-β regulation supports a **loss-of-function** mechanism acting dominantly (haploinsufficiency or dominant-negative of the signalling module).

### Finding 4 — Clinical phenotype: early-onset axial high myopia with retinopathy risk

High myopia is defined as refractive error ≤ −6.00 D. SLC39A5-related cases are early-onset (presenting < 7 years in early-onset high myopia [eo-HM] cohorts), with eo-HM probands showing median spherical equivalent roughly −9.5 to −11.25 D and median axial length ~26–27 mm [PMID: 36964802]. In a 731-patient cross-sectional study, SLC39A5 was among genes "more relevant to eye elongation," and axial length was quantitatively tied to downstream morbidity:

> "1-mm increase in AL conferred 10.84% higher risk of pathologic retinopathy (Category ≥2) as well as 7.35% higher risk of low vision (best-corrected visual acuities <0.3)" — [PMID: 31560770](https://pubmed.ncbi.nlm.nih.gov/31560770/)

> "SLC39A5, CCDC111, BSG, and P4HA2 were more relevant to eye elongation" — [PMID: 31560770](https://pubmed.ncbi.nlm.nih.gov/31560770/)

**Phenotype characteristics:** onset childhood/early-onset; severity moderate-to-severe; progression progressive during growth years; the primary phenotype is axial high myopia with age-accumulating complication risk. **Quality-of-life impact** is driven by refractive dependence and, in those who progress to pathologic myopia, by irreversible central vision loss.

**Suggested HPO terms:** HP:0011003 (High myopia); HP:0012801 (Increased axial length of the globe); HP:0000545 (Myopia); HP:0007917 (Posterior staphyloma); HP:0000541 (Retinal detachment).

### Finding 5 — Inheritance, penetrance, and population distribution

MYP24 is autosomal dominant (OMIM #615420), co-segregating across multigenerational families [PMID: 24891338]. Reported families/probands are overwhelmingly East Asian (Chinese) cohorts. Monogenic high myopia genes collectively explain only a minority of eo-HM families, and SLC39A5 is one of >17 candidate genes:

> "Sixteen potentially pathogenic variants predicted to affect protein function in eight of seventeen causative genes for HM in fifteen (13.3%) families were revealed" — [PMID: 36964802](https://pubmed.ncbi.nlm.nih.gov/36964802/)

High myopia overall is predominantly polygenic/multifactorial, placing MYP24 in context as a rare Mendelian subset:

> "The cross-ancestry meta-analysis identified 932 RE-associated variants" — [PMID: 42009823](https://pubmed.ncbi.nlm.nih.gov/42009823/)

No gene-specific prevalence/incidence rate (per 100,000) exists; penetrance appears high within reported families but is not formally quantified; no founder effect, germline mosaicism, or consanguinity role has been specifically established for SLC39A5.

### Finding 6 — ZIP5 is a basolateral zinc-uptake transporter controlling organismal zinc status

Human/mouse ZIP5 is a Zn(II)-specific uptake transporter of the SLC39/ZIP family. Unusually, it is **not** endocytosed/down-regulated by zinc repletion and localizes to the **basolateral** membrane of polarized cells, mediating serosal-to-mucosal zinc transport [PMID: 15322118]. It is expressed in intestine, pancreas, liver, and kidney (zinc-homeostatic tissues) and, importantly for disease, abundantly in sclera and retina during eye development [PMID: 24891338].

> "the endocytic removal of mZip5 from the plasma membrane is not triggered by zinc treatment. Thus, the activity of mZip5 does not appear to be down-regulated by zinc repletion" — [PMID: 15322118](https://pubmed.ncbi.nlm.nih.gov/15322118/)

The **_Slc39a5_-knockout mouse** is viable and fertile but shows altered zinc homeostasis:

> "total knockout of ZIP5 led to increased zinc in the liver in mice fed a zinc-adequate (ZnA) diet but impaired accumulation of pancreatic zinc in mice fed a zinc-excess (ZnE) diet" — [PMID: 24303081](https://pubmed.ncbi.nlm.nih.gov/24303081/)

### Finding 7 — Scleral ECM/collagen weakening is the effector step

The sclera is the primary effector tissue. In myopia it undergoes ECM remodeling — changes in composition, collagen organization, and biomechanical integrity — producing axial elongation; experimental scleral-strengthening therapies (posterior scleral reinforcement, collagen crosslinking) are under investigation [PMID: 42309346]. SLC39A5/ZIP5 is abundantly expressed in the sclera and controls scleral-fibroblast ECM gene transcription via the zinc–Smad–TGF-β axis [PMID: 24891338; 34302427].

> "excessive axial elongation resulting in biomechanical weakening of the sclera, and increasing the risk of complications such as posterior staphyloma, myopic macular degeneration, retinal detachment, cataract, and glaucoma" — [PMID: 42309346](https://pubmed.ncbi.nlm.nih.gov/42309346/)

### Finding 8 — Complications and prognosis

Axial elongation biomechanically weakens the sclera, raising lifetime risk of posterior staphyloma, myopic macular degeneration, choroidal neovascularization, peripheral retinal degeneration, retinal detachment, cataract, and glaucoma [PMID: 42309346; 39036706]. Approximately one in three high-myopia patients develop visual impairment with age; anxiety is recognized as the first extra-ocular complication of high myopia [PMID: 39036706]. MYP24 is **not life-limiting**; its morbidity is visual.

> "one in three patients with high myopia develop visual impairment with age" — [PMID: 39082137](https://pubmed.ncbi.nlm.nih.gov/39082137/)

### Finding 9 — Environmental/gene–environment context and protective factors

Although MYP24 is Mendelian, the broader myopia phenotype is strongly modified by environment. Increased **outdoor time** is protective against rapid axial growth, plausibly via sunlight-driven retinal dopamine release; excessive near work and reduced outdoor exposure increase risk; parental myopia is a major risk factor/confounder, and urban living modestly raises risk.

> "actively engaging in outdoor activities had a protective effect in the 7-9-year group (OR, 0.65, 95% CI 0.43 to 0.97)" — [PMID: 39890431](https://pubmed.ncbi.nlm.nih.gov/39890431/)

> "a compelling connection between increased outdoor time and a decreased risk of myopia in children. This protective effect may primarily be attributed to exposure to the characteristics of natural light (i.e., sunlight) and the release of retinal dopamine" — [PMID: 38297353](https://pubmed.ncbi.nlm.nih.gov/38297353/)

There is **no infectious or toxic etiology**. In Mendelian MYP24, genetic liability is primary but environmental modifiers plausibly influence the rate of axial elongation.

### Finding 10 — Management: no gene-specific therapy; standard myopia control

No approved gene-/zinc-targeted therapy exists. Management follows general high-myopia care: optical correction plus pediatric axial-elongation control with low-dose atropine (0.01–0.05%), orthokeratology, and defocus/aspherical-lenslet spectacles (DIMS, HAL). Combination therapy outperforms monotherapy:

> "AL elongation was lower in the AOK group than in the OK group at 3, 6, and 12 months (0.03 ± 0.06 vs. 0.09 ± 0.04; 0.09 ± 0.08 vs. 0.18 ± 0.07; and 0.20 ± 0.12 vs. 0.33 ± 0.09 mm, respectively; all P < 0.05)" — [PMID: 42770659](https://pubmed.ncbi.nlm.nih.gov/42770659/)

Pathologic complications require retinal surveillance and intervention. **Suggested NCIT terms:** C62043 (Atropine); treatment chemical entity CHEBI:16684 (atropine).

---

## Mechanistic Model

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous damaging _SLC39A5_ variant** (nonsense/frameshift/damaging missense) **leads to** reduced functional ZIP5 zinc-transporter protein (loss of function acting dominantly).
2. Reduced ZIP5 activity in scleral fibroblasts **results in** decreased intracellular zinc availability (*inferred for sclera from cell models; demonstrated in vitro* [PMID: 34302427]).
3. Zinc deficiency **leads to** destabilization of Smad proteins [PMID: 34302427].
4. Smad destabilization **results in** impaired BMP/TGF-β signalling (blocked R-Smad phosphorylation; loss of wild-type SLC39A5's regulation of Smad1) [PMID: 24891338; 34302427].
5. Inhibited TGF-β signalling **leads to** reduced transcription of scleral ECM genes (COL1A1, COL2A1, COL4A1, FN1, LAMA1) [PMID: 34302427].
6. Reduced collagen/ECM synthesis **results in** scleral ECM remodeling and biomechanical weakening [PMID: 42309346].
7. Weakened sclera **leads to** excessive posterior-globe axial elongation (axial length > 26 mm; SE ≤ −6 D) [PMID: 31560770].
8. Axial elongation **results in** the clinical phenotype of early-onset high myopia and, cumulatively with age, **branches to** sight-threatening complications: myopic maculopathy, posterior staphyloma, choroidal neovascularization, retinal detachment, cataract, and glaucoma [PMID: 42309346; 39036706; 31560770].

```
 SLC39A5 variant
        │ (↓ ZIP5 function)
        ▼
 ↓ intracellular Zn²⁺  ──► Smad destabilization ──► ↓ BMP/TGF-β signalling
        │                                                   │
        │                                                   ▼
        │                                    ↓ COL1A1/COL2A1/COL4A1/FN1/LAMA1
        │                                                   │
        ▼                                                   ▼
   (zinc homeostasis                         Scleral ECM weakening (UBERON:0001773)
    tissues: gut/pancreas/                               │
    liver — mouse KO)                                    ▼
                                             Axial elongation (HP:0012801)
                                                         │
                             ┌───────────────────────────┼───────────────────────────┐
                             ▼                            ▼                            ▼
                    Myopic maculopathy          Retinal detachment            Glaucoma / cataract
```

**Upstream vs downstream:** the mutation and the zinc/Smad/TGF-β steps are upstream and molecular; scleral ECM weakening is the pivotal effector; axial elongation and retinal/choroidal complications are downstream and clinical.

**Cell types / processes.** Primary cell: scleral fibroblast (CL:0000057). Biological processes: GO:0005385 (zinc ion transmembrane transporter activity), GO:0007179 (transforming growth factor beta receptor signaling pathway), GO:0030198 (extracellular matrix organization). Chemical entities: CHEBI:29105 (zinc(2+)); CHEBI:16684 (atropine).

### Anatomical and ontology crosswalk

| Level | Structure | Ontology term |
|---|---|---|
| Organ (primary) | Posterior sclera | UBERON:0001773 (sclera) |
| Organ (secondary) | Retina | UBERON:0000966 (retina) |
| Tissue/cell | Scleral fibroblast | CL:0000057 (fibroblast) |
| Phenotype | High myopia | HP:0011003 |
| Phenotype | Increased axial length | HP:0012801 |
| Process | Zinc transport | GO:0005385 |
| Process | TGF-β signalling | GO:0007179 |
| Process | ECM organization | GO:0030198 |
| Disease | MYP24 | MONDO:0014411 / OMIM #615420 |
| Treatment | Atropine | NCIT C62043 / CHEBI:16684 |

### Identifier crosswalk

| Identifier type | Value |
|---|---|
| MONDO | MONDO:0014411 |
| OMIM (disease) | #615420 (MYP24) |
| Gene | SLC39A5 |
| HGNC | HGNC:20502 |
| NCBI Gene | 283375 |
| Ensembl | ENSG00000139053 |
| UniProt | Q6ZMH5 |
| OMIM (gene) | *608730 |
| Locus | 12q13.3 |
| Protein | ZIP5 |
| ICD-10 / ICD-11 | H52.1 / 9D00.1 |
| MeSH | D009216 (Myopia); D047475 (pathologic myopia) |

---

## Section-by-Section Notes

- **1. Disease information** — Non-syndromic AD axial high myopia; identifiers as tabulated above; information is derived from aggregated disease-level resources (OMIM, gene cohorts) plus individual-family genetic studies, not large EHR cohorts.
- **2. Etiology** — Primary cause is genetic (heterozygous SLC39A5 variants). Environmental modifiers (near work, outdoor time, parental myopia, urbanization) influence the broader myopia phenotype. No protective genetic variant is established; outdoor time is the best-supported protective environmental factor.
- **3. Phenotypes** — Dominated by high myopia (HP:0011003) and increased axial length (HP:0012801), childhood onset, progressive, with complication phenotypes developing with age.
- **4. Genetic/molecular** — See variant table; loss-of-function dominant mechanism; no established modifier genes, epigenetic changes, or chromosomal abnormalities specific to MYP24.
- **5. Environmental** — No toxic/infectious etiology; lifestyle factors modulate axial growth rate.
- **6. Mechanism** — See causal chain and diagram.
- **7. Anatomy** — Primary sclera (UBERON:0001773); secondary retina/choroid; scleral fibroblast (CL:0000057); bilateral involvement.
- **8. Temporal development** — Childhood/early onset; chronic, progressive during ocular growth; lifelong.
- **9. Inheritance/population** — AD; East-Asian–predominant reporting; rare Mendelian subset of high myopia.
- **10. Diagnostics** — Clinical: cycloplegic refraction, axial-length biometry, fundus/OCT for complications. Genetic: WES/targeted high-myopia gene panels including SLC39A5; single-gene/Sanger confirmation and segregation.
- **11. Outcome/prognosis** — Not life-limiting; visual morbidity accrues with axial elongation (~1 in 3 develop visual impairment).
- **12. Treatment** — Generic myopia control (atropine, ortho-K, DIMS/HAL); no gene-specific therapy; retinal intervention for complications.
- **13. Prevention** — Outdoor time; axial-growth control in children; genetic counseling (50% offspring risk, AD).
- **14. Other species** — Orthologous mouse _Slc39a5_; no naturally occurring ocular SLC39A5 disease reported in animals.
- **15. Model organisms** — _Slc39a5_-knockout mouse (zinc homeostasis); ocular/axial phenotype not reported — a key model gap.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [24891338](https://pubmed.ncbi.nlm.nih.gov/24891338/) | Landmark (human + in vitro) | Defines SLC39A5 as the MYP24 gene; nonsense/missense variants; BMP/TGF-β–Smad regulation; scleral/retinal expression |
| [34302427](https://pubmed.ncbi.nlm.nih.gov/34302427/) | Mechanistic (in vitro) | Zinc–Smad–TGF-β–ECM axis; SLC39A5 depletion reduces COL/FN/LAMA transcription; rescue on re-expression |
| [25525168](https://pubmed.ncbi.nlm.nih.gov/25525168/) | Variant cohort (human) | SLC39A5 missense c.1238G>C/p.G413A among eoHM genes |
| [28442722](https://pubmed.ncbi.nlm.nih.gov/28442722/) | Variant cohort (human) | Novel SLC39A5 missense variants in 187 high-myopia patients |
| [32215939](https://pubmed.ncbi.nlm.nih.gov/32215939/) | Variant cohort (human) | Frameshift c.726dupA LoF variant |
| [36964802](https://pubmed.ncbi.nlm.nih.gov/36964802/) | Variant cohort (human) | Monogenic genes explain ~13.3% of eo-HM families; additional SLC39A5 variants |
| [40920702](https://pubmed.ncbi.nlm.nih.gov/40920702/) | Variant cohort (human) | SLC39A5 c.577G>A in eo-HM; rarity in gnomAD/ExAC/1000G |
| [31560770](https://pubmed.ncbi.nlm.nih.gov/31560770/) | Phenotype/epidemiology (human) | SLC39A5 tied to eye elongation; axial length → retinopathy/low-vision risk |
| [15322118](https://pubmed.ncbi.nlm.nih.gov/15322118/) | Protein biology (in vitro) | ZIP5 basolateral localization; not zinc-down-regulated |
| [24303081](https://pubmed.ncbi.nlm.nih.gov/24303081/) | Model organism (mouse) | Slc39a5-KO zinc-homeostasis phenotype; pancreatic protection |
| [42309346](https://pubmed.ncbi.nlm.nih.gov/42309346/) | Mechanism/therapy review | Scleral ECM remodeling as biomechanical basis; scleral-strengthening approaches |
| [39036706](https://pubmed.ncbi.nlm.nih.gov/39036706/) | Clinical review | High-myopia complication spectrum; anxiety as extra-ocular complication |
| [39082137](https://pubmed.ncbi.nlm.nih.gov/39082137/) | Clinical review | ~1 in 3 develop visual impairment; prevalence context |
| [42770659](https://pubmed.ncbi.nlm.nih.gov/42770659/) | Interventional (human) | Atropine + ortho-K combination slows axial elongation |
| [42768333](https://pubmed.ncbi.nlm.nih.gov/42768333/) | Interventional (human) | Ortho-K + atropine vs DIMS + atropine for AL control |
| [39890431](https://pubmed.ncbi.nlm.nih.gov/39890431/) | Epidemiology (human) | Outdoor time protective (OR 0.65) against rapid axial growth |
| [38297353](https://pubmed.ncbi.nlm.nih.gov/38297353/) | Review | Mechanism of outdoor-time protection (sunlight → retinal dopamine) |
| [42009823](https://pubmed.ncbi.nlm.nih.gov/42009823/) | GWAS (human) | 932 refractive-error variants; polygenic context for Mendelian MYP24 |

**Evidence source types:** the gene–disease relationship is supported by **human clinical/genetic** studies (family segregation + case cohorts) and **in vitro functional** work; the available **model organism** is the Slc39a5-knockout mouse, which models systemic zinc handling but has not been reported to recapitulate the ocular/axial myopia phenotype.

---

## Limitations and Knowledge Gaps

- **Narrow evidence base / ancestry bias.** Essentially all reported MYP24 families and cohorts are East Asian (Chinese). Prevalence, incidence, penetrance estimates, and variant frequencies outside this population are unknown. No formal epidemiological rate (per 100,000) exists for the SLC39A5-specific subtype.
- **Gene–disease validity caveat.** Several reported variants are candidate/VUS and are not yet curated as definitively pathogenic in ClinVar/ClinGen. A formal ClinGen gene–disease validity classification was not confirmed in this investigation.
- **Mechanism partly inferred.** The zinc→Smad→TGF-β→ECM chain is demonstrated in cell models (HEK293, SLC39A5-KO), not directly in human scleral tissue of patients; the scleral step is inferred from expression data plus general myopia scleral biology.
- **No disease-specific animal model of the ocular phenotype.** The Slc39a5-KO mouse characterizes systemic zinc handling, not axial myopia; phenotype recapitulation for the eye is unestablished.
- **Penetrance/expressivity quantitatively uncharacterized.** AD inheritance is clear, but numeric penetrance, age-dependence, and intrafamilial variability are not well quantified for SLC39A5 specifically.
- **No gene-specific therapeutics or biomarkers.** There is no validated molecular biomarker, no zinc-/TGF-β-targeted intervention, and no pharmacogenomic data for MYP24.
- **Cross-species/natural disease data absent.** No naturally occurring SLC39A5 ocular disease in companion animals or wildlife was identified (OMIA/veterinary data not located for this subtype).

---

## Proposed Follow-up Experiments / Actions

1. **Engineer an eye-relevant model.** Generate scleral-fibroblast–specific or knock-in (patient-variant) mouse/zebrafish models and quantify axial length, refraction, and scleral collagen architecture to test whether SLC39A5 loss produces axial elongation in vivo.
2. **Human scleral validation.** Where tissue is available (e.g., surgical/post-mortem highly myopic sclera), measure zinc content, Smad phosphorylation, and ECM-gene expression to confirm the in-vitro chain in patient tissue.
3. **ClinGen curation.** Submit the aggregated variant/segregation evidence for formal ClinGen gene–disease validity classification and deposit variants in ClinVar with ACMG/AMP evidence codes.
4. **Ancestry diversification.** Screen SLC39A5 in non–East-Asian high-myopia cohorts to estimate the gene's contribution and variant spectrum across populations and establish penetrance.
5. **Therapeutic hypothesis testing.** Evaluate whether local zinc supplementation or TGF-β-pathway modulation can restore scleral ECM synthesis in model systems — a mechanism-rational, disease-specific avenue distinct from generic myopia control.
6. **Genotype-stratified natural history.** Follow SLC39A5-positive patients longitudinally for axial-elongation rate and complication incidence versus polygenic high myopia, to determine whether monogenic cases warrant intensified surveillance.

---

*Evidence types: human clinical/genetic (segregation + cohorts), in vitro functional, model organism (mouse), and computational (variant prediction, GWAS context). All mechanistic and clinical claims are anchored to the PMIDs cited above.*


## Artifacts

- [OpenScientist final report](Myopia_24_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Myopia_24_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:24891338`: "wild-type, but not disease-associated SLC39A5 inhibited the expression of Smad1, a key phosphate protein in the downstream of the BMP/TGF-β (bone morphogenic protein/transforming growth factor-β) pathway"
  - closest text in source: "Furthermore, we found that wild-type, but not disease-associated SLC39A5 inhibited the expression of Smadl, a key phosphate protein in the downstream of the BMP/TGF-β (bone morphogenic protein/transforming growth factor-β) pathway"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014411` (5 mentions) - the report calls it "MONDO"; MONDO calls it **myopia 24, autosomal dominant**
- `HP:0012801` (4 mentions) - the report calls it "Increased axial length of the globe", "Increased axial length"; HP calls it **Narrow jaw**
- `HP:0007917` (1 mention) - the report calls it "Posterior staphyloma"; HP calls it **Tractional retinal detachment**
- `GO:0005385` (2 mentions) - the report calls it "zinc ion transmembrane transporter activity", "Zinc transport"; GO calls it **zinc ion transmembrane transporter activity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007179` (2 mentions) - the report calls it "transforming growth factor beta receptor signaling pathway", "TGF-β signalling"; GO calls it **transforming growth factor beta receptor signaling pathway**, and lists "TGFbeta receptor signalling pathway" among its other names
- `GO:0030198` (2 mentions) - the report calls it "extracellular matrix organization", "ECM organization"; GO calls it **extracellular matrix organization**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012801` - called "Increased axial length of the globe", "Increased axial length"
- `GO:0005385` - called "zinc ion transmembrane transporter activity", "Zinc transport"
- `GO:0007179` - called "transforming growth factor beta receptor signaling pathway", "TGF-β signalling"
- `GO:0030198` - called "extracellular matrix organization", "ECM organization"