---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:06:32.185098'
end_time: '2026-10-24T13:19:20.404222'
duration_seconds: 768.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Macular Degeneration, Early-onset
  mondo_id: MONDO:0014501
  category: Mendelian
  causal_genes: FBN2
  omim_id: OMIM:616118
  synonyms: early-onset macular degeneration; EOMD; FBN2-related maculopathy
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
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 9
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014501
    reported_labels:
    - MONDO
    ontology_label: macular degeneration, early-onset
  - term_id: HP:0000592
    reported_labels:
    - Central scotoma
    ontology_label: Blue sclerae
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Macular_Degeneration_Early-onset-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Macular_Degeneration_Early-onset-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Macular Degeneration, Early-onset
- **MONDO ID:** MONDO:0014501 (if available)
- **Causal gene(s):** FBN2
- **OMIM:** OMIM:616118
- **Synonyms:** early-onset macular degeneration; EOMD; FBN2-related maculopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Macular Degeneration, Early-onset** covering all of the
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

# Macular Degeneration, Early-onset (FBN2-related): A Comprehensive Disease Characterization

**Disease:** Macular Degeneration, Early-onset (EOMD)
**MONDO ID:** MONDO:0014501 · **OMIM:** 616118 · **Causal gene:** **FBN2** (fibrillin-2)
**Category:** Mendelian, autosomal dominant

---

## Summary

**Early-onset macular degeneration (EOMD; MONDO:0014501, OMIM 616118) is a rare autosomal-dominant Mendelian maculopathy caused by heterozygous variants in *FBN2*, the gene encoding fibrillin-2** — a large cysteine-rich glycoprotein of the elastin-rich extracellular matrix (ECM). The disease was defined molecularly by Ratnapriya et al. (2014), who used whole-exome sequencing of a two-generation family with dominant maculopathy to identify the index variant **p.Glu1144Lys** in *FBN2* ([PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)). The same study showed that *FBN2* sits at the interface of Mendelian and complex disease: a common non-synonymous *FBN2* variant (rs154001, p.Val965Ile) is also modestly associated with age-related macular degeneration (AMD), making *FBN2* an "allelic series" gene that links a rare early-onset dominant maculopathy to the far more common polygenic AMD.

Mechanistically, EOMD is best understood as a **Bruch's-membrane fibrillinopathy**. Fibrillin-2 localizes to the central elastic lamina of Bruch's membrane (BrM), the pentalaminar ECM sheet separating the retinal pigment epithelium (RPE) from the choriocapillaris. Loss or dysfunction of fibrillin-2 has two coupled consequences: (1) it weakens the structural elastic scaffold of BrM, and (2) it dysregulates the bioavailability of sequestered TGF-β/BMP growth factors, because fibrillins normally sequester these latent complexes in the ECM. The downstream cascade — elastin/microfibril breakdown, drusen accumulation, complement activation, elastin-derived-peptide-driven inflammation and angiogenesis, and ultimately choroidal neovascularization (CNV) — recapitulates in an accelerated, genetically-determined form the central ECM pathology of AMD.

There is **no gene-specific cure**. Clinical management is supportive and mirrors AMD care: anti-VEGF therapy (ranibizumab, aflibercept, brolucizumab, faricimab) for the neovascular (wet) complication, low-vision rehabilitation, and genetic counseling for an autosomal-dominant trait with apparently incomplete/age-dependent penetrance. Two mechanism-directed strategies are promising at the preclinical stage: **FBN2 recombinant-protein replacement** (rescued retinopathy in a retina-specific *Fbn2* knock-down mouse; [PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)) and **elastase inhibition** to preserve BrM elastin ([PMID: 37174708](https://pubmed.ncbi.nlm.nih.gov/37174708/)).

---

## Disease Information (Section 1)

**Overview.** EOMD is a rare inherited macular dystrophy with onset earlier than typical AMD, characterized by drusen-like deposits at the level of Bruch's membrane/RPE, progressive macular degeneration, and risk of choroidal neovascularization leading to central vision loss. It is caused by heterozygous variants in **FBN2 (fibrillin-2)**, an elastin-associated ECM glycoprotein.

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0014501 |
| OMIM | 616118 (Macular degeneration, early-onset) |
| Gene | FBN2 (HGNC:3604; NCBI Gene 2201; Ensembl ENSG00000138829; chromosome 5q23.3) |
| Protein (UniProt) | P35556 (FBN2_HUMAN) |
| MeSH | Macular Degeneration (D008268) — no EOMD-specific MeSH term |
| ICD-10 | H35.3 (degeneration of macula and posterior pole) — non-specific |

**Synonyms / alternative names:** early-onset macular degeneration; EOMD; FBN2-related maculopathy; macular degeneration, early-onset, autosomal dominant.

**Information source.** The knowledge base entry is derived from **aggregated disease-level resources** (OMIM, primary literature) and a small number of individual pedigrees/case series rather than large EHR cohorts. The defining evidence comes from a single index family plus mutation screening of additional maculopathy patients ([PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)).

---

## Etiology (Section 2)

**Primary cause — genetic.** EOMD is a Mendelian, autosomal-dominant disorder. The primary cause is a heterozygous pathogenic variant in **FBN2**. The index variant is a missense change, **p.Glu1144Lys**, identified by whole-exome sequencing:

> *"we performed whole exome sequencing in four individuals of a two-generation family with autosomal dominant maculopathy and identified a rare variant p.Glu1144Lys in Fibrillin 2 (FBN2), a glycoprotein of the elastin-rich extracellular matrix (ECM)"* — [PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)

Screening of 192 additional maculopathy patients revealed further rare *FBN2* variants predicted to disrupt function, supporting an allelic series.

**Genetic risk factors (complex disease).** A common *FBN2* non-synonymous variant **rs154001 (p.Val965Ile)** showed suggestive association with AMD (OR = 1.10; P = 3.79 × 10⁻⁵) in 10,337 cases vs 11,174 controls, demonstrating that the same locus contributes to multifactorial AMD risk:

> *"We detect suggestive association of a common FBN2 non-synonymous variant, rs154001 (p.Val965Ile) with AMD in 10 337 cases and 11 174 controls (OR = 1.10; P-value = 3.79 × 10(-5))"* — [PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)

**Environmental risk factors.** No EOMD-specific environmental triggers have been established. By analogy with AMD, aging, oxidative stress, and smoking plausibly accelerate BrM ECM degradation, but direct evidence in FBN2-EOMD is **not available**. Because EOMD is monogenic and early-onset, environmental factors are expected to act as modifiers rather than primary causes.

**Protective factors.** No genetic or environmental protective factors specific to EOMD have been characterized. (Not available.)

**Gene–environment interactions.** Not directly studied in EOMD. The dual role of *FBN2* (rare dominant variant → EOMD; common variant → AMD susceptibility) suggests the gene's ECM/growth-factor function is a convergence point where genetic load and age-related/environmental ECM stress combine. This remains inferred.

---

## Phenotypes (Section 3)

EOMD phenotypes are ophthalmologic and centered on the macula. Because the molecularly-defined cohort is small, frequencies are qualitative.

| Phenotype | Type | HPO term (suggested) | Characteristics |
|-----------|------|----------------------|-----------------|
| Macular degeneration | Clinical sign | HP:0000608 (Macular degeneration) | Early-onset (earlier than typical AMD); progressive |
| Drusen / sub-RPE deposits | Clinical sign (imaging) | HP:0011510 (Macular drusen) | Hallmark BrM-level deposits; early sign |
| Reduced visual acuity | Symptom | HP:0000572 (Visual impairment) | Variable; progressive central vision loss |
| Choroidal neovascularization | Clinical sign (complication) | HP:0011506 / CNV | Sight-threatening wet complication |
| Central scotoma | Symptom | HP:0000592 (Central scotoma) | Corresponds to macular lesions |
| Metamorphopsia | Symptom | — | Distortion typical of maculopathy |
| Reduced ERG amplitude (model) | Laboratory/functional | HP:0000512 (Abnormal electroretinogram) | Shown in Fbn2 knock-down mouse ([PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)) |

**Age of onset:** Earlier than age-related AMD — childhood-to-adult rather than geriatric; exact distribution is not well-defined given the small cohort.
**Severity:** Variable, ranging from drusen-only to chorioretinal involvement with CNV.
**Progression:** Progressive.
**Quality-of-life impact:** Central vision loss impairs reading, writing, driving, face recognition, and stereoscopic vision — the same functional losses that make AMD the leading cause of irreversible central blindness in older adults ([PMID: 24938626](https://pubmed.ncbi.nlm.nih.gov/24938626/)). EOMD-specific QoL instruments (EQ-5D/SF-36) have not been reported. (Not available.)

---

## Genetic / Molecular Information (Section 4)

**Causal gene.** *FBN2* (fibrillin-2), HGNC:3604, chromosome 5q23.3, UniProt P35556. FBN2 is a ~2,900-residue modular glycoprotein built mainly of calcium-binding EGF-like domains and TB (TGF-β-binding/8-cysteine) domains that templates microfibril and elastic-fiber assembly.

**Pathogenic variants.**

| Variant | Type | Disease | Notes |
|---------|------|---------|-------|
| p.Glu1144Lys (NM_001999) | Missense | EOMD (index) | Segregated in two-generation pedigree ([PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)) |
| Additional rare FBN2 variants | Predicted damaging | EOMD/maculopathy | Found by screening 192 patients |
| rs154001 (p.Val965Ile) | Missense, common | AMD susceptibility | OR 1.10, P = 3.79×10⁻⁵ |

**Variant classification:** The index p.Glu1144Lys is reported as a rare, segregating, disease-causing variant; by ACMG/AMP framing it draws support from segregation (PP1), rarity (PM2), and in-silico damage prediction (PP3). Many *FBN2* variants elsewhere in ClinVar relate to **congenital contractural arachnodactyly (CCA / Beals-Hecht syndrome)** rather than EOMD (see below), so curation must distinguish the ocular from the skeletal phenotype.

**Allele frequency:** The index variant and EOMD-associated variants are rare in population databases (gnomAD); rs154001 is common.

**Somatic vs germline:** Germline. No somatic involvement.

**Functional consequence:** Loss / reduction of fibrillin-2 function. Retinal FBN2 protein is reduced in both AMD and EOMD patients, and a loss-of-function mouse recapitulates retinopathy that is rescued by FBN2 protein — consistent with a **loss-of-function / haploinsufficiency-like** mechanism for the ocular phenotype:

> *"the retinal protein expression of FBN2 was reduced in patients with AMD and EOMD"* — [PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)

**Genotype–phenotype note — allelic disorders.** *FBN2* is pleiotropic. Variants in the **central region (classically exons 24–35)** of *FBN2* typically cause **congenital contractural arachnodactyly (CCA/Beals syndrome)**, an autosomal-dominant connective-tissue disorder with arachnodactyly, camptodactyly, joint contractures, crumpled ears, and scoliosis ([PMID: 42299845](https://pubmed.ncbi.nlm.nih.gov/42299845/); [PMID: 39911746](https://pubmed.ncbi.nlm.nih.gov/39911746/)). Variants **outside the central region** are linked to thoracic aortic disease and to short stature/brachydactyly/joint-contracture phenotypes ([PMID: 40406865](https://pubmed.ncbi.nlm.nih.gov/40406865/); [PMID: 40199564](https://pubmed.ncbi.nlm.nih.gov/40199564/)). The EOMD-associated variants constitute a distinct, ocular-predominant arm of the *FBN2* allelic spectrum.

**Modifier genes:** Not formally defined for EOMD. Candidate modifiers by analogy with AMD ECM biology include *EFEMP1*, *TIMP3*, *FBLN5*, complement genes (*CFH*), *ARMS2/HTRA1*, and ADAMTS proteases that process fibrillins ([PMID: 24938626](https://pubmed.ncbi.nlm.nih.gov/24938626/)).

**Epigenetic information / chromosomal abnormalities:** No EOMD-specific DNA-methylation, histone-modification, or large-scale chromosomal findings reported. (Not available / not applicable.)

---

## Environmental Information (Section 5)

- **Environmental factors / toxins:** None established as causal for EOMD (monogenic disease). (Not available.)
- **Lifestyle factors:** Not specifically studied in EOMD; smoking and oxidative stress are AMD risk factors that may plausibly accelerate shared BrM pathology but are unproven here.
- **Infectious agents:** Not applicable. EOMD is a genetic, non-infectious ECM disorder.

---

## Mechanism / Pathophysiology (Section 6)

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Heterozygous *FBN2* variant (e.g., p.Glu1144Lys)** → leads to reduced/dysfunctional fibrillin-2 protein in the retina/Bruch's membrane (demonstrated: reduced FBN2 protein in patient retina; [PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)).
2. **Reduced functional fibrillin-2** → results in defective microfibril/elastic-fiber assembly in the **central elastic lamina of Bruch's membrane**, where FBN2 normally resides (demonstrated localization: [PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)).
3. *Branch A — structural:* **Weakened elastic lamina** → reduces the integrity of the BrM molecular sieve → promotes abnormal deposition (drusen) and loss of BrM barrier function (inferred from AMD BrM biology; [PMID: 19747980](https://pubmed.ncbi.nlm.nih.gov/19747980/)).
4. *Branch B — signaling:* **Loss of fibrillin-2's sequestration of latent TGF-β/BMP complexes** → results in dysregulated TGF-β/BMP bioavailability and signaling (established fibrillin function; [PMID: 19513754](https://pubmed.ncbi.nlm.nih.gov/19513754/), [PMID: 17708531](https://pubmed.ncbi.nlm.nih.gov/17708531/)).
5. **Elastin/microfibril breakdown** (aggravated by excess elastase and reduced protease inhibition) → generates elastin-derived peptides (EDPs) and anti-elastin antibodies → drives inflammatory and angiogenic responses (demonstrated associations; [PMID: 35798060](https://pubmed.ncbi.nlm.nih.gov/35798060/), [PMID: 37174708](https://pubmed.ncbi.nlm.nih.gov/37174708/)).
6. **Drusen + complement cascade activation** → represent the earliest degenerative signs at the RPE–BrM interface (inferred from AMD; [PMID: 19747980](https://pubmed.ncbi.nlm.nih.gov/19747980/)).
7. **Reduced BrM elastin integrity + elevated VEGF** → leads to **choroidal neovascularization (CNV)** in the macula (demonstrated spatial correspondence; [PMID: 37174708](https://pubmed.ncbi.nlm.nih.gov/37174708/)).
8. **Macular degeneration / CNV** → results in central scotoma, metamorphopsia and progressive central vision loss (clinical manifestation).

### Detail by category

**Molecular pathways.** Central pathway is **TGF-β/BMP superfamily signaling**, regulated by fibrillin microfibrils. Fibrillins sequester latent TGF-β and BMP in the ECM:

> *"the instructive role reflects the ability of fibrillins to sequester transforming growth factor beta (TGFbeta) and bone morphogenetic protein (BMP) complexes in the extracellular matrix"* — [PMID: 19513754](https://pubmed.ncbi.nlm.nih.gov/19513754/)

> *"fibrillin-1 and fibrillin-2 mutations perturb signaling events mediated by TGF-beta superfamily members"* — [PMID: 17708531](https://pubmed.ncbi.nlm.nih.gov/17708531/)

ADAMTS proteases (ADAMTS6/10, ADAMTSL2) that process fibrillins and LTBPs further couple microfibril turnover to TGF-β activation, YAP/TAZ mechanotransduction and downstream angiogenic signaling ([PMID: 36368447](https://pubmed.ncbi.nlm.nih.gov/36368447/); [PMID: 30060141](https://pubmed.ncbi.nlm.nih.gov/30060141/)) — suggested GO terms: **GO:0007179 (transforming growth factor beta receptor signaling pathway)**, **GO:0030509 (BMP signaling pathway)**.

**Cellular processes.** Inflammation (complement activation), angiogenesis (CNV), and RPE/endothelial ECM remodeling. GO:0006954 (inflammatory response), GO:0001525 (angiogenesis), GO:0030198 (extracellular matrix organization).

**Protein dysfunction.** Loss/reduction of fibrillin-2 function → impaired elastic-fiber template assembly (GO:0048251, elastic fiber assembly) and impaired growth-factor sequestration.

**Tissue damage mechanisms.** Oxidative/proteolytic degradation of BrM elastin; elastase activity degrades elastin and drives VEGF; AMD donor BrM/choroid shows lower alpha-1 antitrypsin (a serine-protease inhibitor), tilting the protease/anti-protease balance toward elastin loss ([PMID: 40210893](https://pubmed.ncbi.nlm.nih.gov/40210893/)).

**Immune involvement.** Complement cascade activation at drusen; EDP-driven inflammation and anti-elastin antibodies ([PMID: 35798060](https://pubmed.ncbi.nlm.nih.gov/35798060/)).

**Cell types (suggested CL terms):** retinal pigment epithelial cell (CL:0002586), choroidal/blood vessel endothelial cell (CL:0000071), fibroblast-like ECM-producing cells.

### Upstream vs downstream

```
UPSTREAM  FBN2 variant → ↓ fibrillin-2 → defective BrM elastic lamina
               │                                   │
               │ (signaling branch)                │ (structural branch)
               ▼                                   ▼
        dysregulated TGF-β/BMP            weakened BrM sieve + elastin breakdown
               │                                   │
               └──────────────┬────────────────────┘
                              ▼
            drusen + complement activation + EDP inflammation
                              ▼
                    ↑ VEGF → choroidal neovascularization
                              ▼
DOWNSTREAM        central vision loss (macular degeneration)
```

---

## Anatomical Structures Affected (Section 7)

| Level | Structure | Ontology (suggested) |
|-------|-----------|----------------------|
| Organ | Eye; retina (macula) | UBERON:0000970 (eye); UBERON:0001782 (macula lutea) |
| Primary site | **Bruch's membrane** (central elastic lamina) | Bruch's membrane |
| Adjacent | Retinal pigment epithelium | RPE |
| Adjacent | Choroid / choriocapillaris | UBERON:0001776 (choroid) |
| Tissue | Elastin/collagen-rich ECM (connective) | — |
| Cell | RPE cell; choroidal endothelial cell | CL:0002586; CL:0000071 |
| Subcellular | Extracellular matrix (secreted) | GO:0031012 (extracellular matrix) |

Bruch's membrane is the defining locus:

> *"BM is an elastin- and collagen-rich extracellular matrix that acts as a molecular sieve"* — [PMID: 19747980](https://pubmed.ncbi.nlm.nih.gov/19747980/)

**Lateralization:** Bilateral (hereditary maculopathy), though asymmetric severity/CNV onset is common.

---

## Temporal Development (Section 8)

- **Onset:** Earlier than age-related AMD (hence "early-onset"); insidious, chronic.
- **Stages:** (1) drusen-only/sub-RPE deposits → (2) macular degenerative change → (3) choroidal neovascularization (wet, sight-threatening). This parallels the dry→wet AMD progression.
- **Progression rate:** Slow and progressive, with variable expressivity (drusen-only to chorioretinal involvement, as seen in dominant early-onset maculopathy pedigrees; [PMID: 17302207](https://pubmed.ncbi.nlm.nih.gov/17302207/)).
- **Course:** Chronic, lifelong, progressive; no spontaneous remission.
- **Critical period for intervention:** The window before/at CNV onset — anti-VEGF therapy is most beneficial when neovascular activity is treated promptly.

---

## Inheritance and Population (Section 9)

- **Inheritance pattern:** Autosomal dominant.

> *"Sanger sequencing validated the segregation of this variant in the complete pedigree, including two additional affected and one unaffected individual"* — [PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)

- **Penetrance:** Apparently incomplete / age-dependent — the index pedigree included an unaffected carrier.
- **Expressivity:** Variable (drusen-only to CNV).
- **Epidemiology:** EOMD is very rare; precise prevalence/incidence are **not established** (defined by individual pedigrees/case series rather than registries).
- **Genetic anticipation / germline mosaicism / founder effects:** Not reported for EOMD. (Note: low-level parental mosaicism has been documented for *FBN2* in the CCA phenotype, [PMID: 42299845](https://pubmed.ncbi.nlm.nih.gov/42299845/), but not for EOMD.)
- **Consanguinity:** Not relevant (dominant).
- **Carrier frequency:** Not applicable in the recessive sense; disease alleles are rare.
- **Population demographics / sex ratio / geographic distribution:** No ethnic predilection or sex bias established; the common AMD-associated rs154001 is distributed broadly. (EOMD-specific data not available.)

---

## Diagnostics (Section 10)

**Clinical/ophthalmic workup.**
- **Imaging:** Color fundus photography, spectral-domain OCT (sub-RPE vs sub-retinal deposits), fundus autofluorescence, fluorescein angiography (FA) and indocyanine-green angiography (ICGA) for CNV, OCT-angiography. Multimodal imaging characterizes drusen and detects CNV ([PMID: 22496012](https://pubmed.ncbi.nlm.nih.gov/22496012/); [PMID: 42132463](https://pubmed.ncbi.nlm.nih.gov/42132463/)).
- **Electrophysiology:** Full-field ERG (often normal), multifocal ERG (reduced macular amplitude/delayed implicit time), EOG — useful to localize dysfunction to the macula ([PMID: 17302207](https://pubmed.ncbi.nlm.nih.gov/17302207/)).

**Genetic testing (confirmatory).** Diagnosis is confirmed by identifying a pathogenic *FBN2* variant via:
- **Single-gene *FBN2* sequencing**, or
- **Inherited-retinal-disease / maculopathy gene panels**, or
- **Whole-exome sequencing (WES)** — the method used in the original discovery ([PMID: 24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/)).

WGS and chromosomal microarray add little beyond targeted sequencing for a point-variant disorder; karyotyping/FISH/mtDNA/repeat-expansion testing are **not applicable**.

**Biomarkers (research-stage).** Elevated serum elastin-derived peptides (EDPs) and anti-elastin antibodies accompany reduced BrM elastin integrity in AMD and may be relevant to EOMD ([PMID: 35798060](https://pubmed.ncbi.nlm.nih.gov/35798060/)). Reduced retinal FBN2 protein is a tissue-level marker ([PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)). None are clinically validated for EOMD.

**Differential diagnosis.** Other autosomal-dominant early-onset maculopathies, distinguished genetically:

| Condition | Gene | Distinguishing feature |
|-----------|------|------------------------|
| Malattia Leventinese / Doyne honeycomb dystrophy | *EFEMP1* (p.Arg345Trp) | Radial/honeycomb drusen ([PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/); [PMID: 42720932](https://pubmed.ncbi.nlm.nih.gov/42720932/)) |
| North Carolina macular dystrophy (phenocopy) | *PRDM13*/MCDR1 region | Early non-progressive macular lesions ([PMID: 17302207](https://pubmed.ncbi.nlm.nih.gov/17302207/)) |
| Sorsby fundus dystrophy | *TIMP3* | Early CNV, night blindness |
| Pattern dystrophy / Best disease | *PRPH2* / *BEST1* | Vitelliform lesions, abnormal EOG |
| Stargardt disease | *ABCA4* | Flecks, usually recessive |

> *"Malattia Leventinese is a rare autosomal dominant macular dystrophy caused by a single"* — [PMID: 41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/)

**Screening.** Cascade genetic testing of at-risk relatives once the familial *FBN2* variant is known. No population newborn/carrier screening (rare dominant disorder).

---

## Outcome / Prognosis (Section 11)

- **Survival/mortality:** EOMD is **not life-limiting**; it does not affect survival. (The ocular-predominant *FBN2* phenotype is distinct from aortic/connective-tissue *FBN2* phenotypes that carry systemic risk.)
- **Morbidity/disability:** Principal burden is progressive central vision loss impairing reading, driving, and face recognition — the functional disability of macular disease.
- **Disease course:** Chronic progressive; CNV is the major sight-threatening complication.
- **Prognostic factors (CNV/visual outcome, extrapolated from neovascular macular disease):** younger age, better baseline visual acuity, smaller hemorrhage size, and thicker subfoveal choroid predict better visual outcomes in submacular hemorrhage from neovascular disease ([PMID: 42177934](https://pubmed.ncbi.nlm.nih.gov/42177934/)). Foveal involvement predicts worse acuity in peripapillary CNV ([PMID: 42132463](https://pubmed.ncbi.nlm.nih.gov/42132463/)).
- **Recovery potential:** No recovery of lost photoreceptors; anti-VEGF can stabilize/partially improve acuity in the wet phase.

---

## Treatment (Section 12)

There is **no gene-specific approved therapy**. Management mirrors AMD.

**Pharmacotherapy — anti-VEGF (standard of care for the neovascular/wet complication).** Intravitreal **ranibizumab, aflibercept, brolucizumab, faricimab** (and biosimilars) reduce central macular thickness and stabilize vision (NCIT: *Anti-VEGF Therapy*; *Ranibizumab* C48094; *Aflibercept* C70846). Evidence base: aflibercept 8 mg improves anatomy in refractory neovascular AMD ([PMID: 42026508](https://pubmed.ncbi.nlm.nih.gov/42026508/)); treat-and-extend regimens with longer-half-life agents reduce treatment burden ([PMID: 42054086](https://pubmed.ncbi.nlm.nih.gov/42054086/)); ranibizumab biosimilars are non-inferior and improve access ([PMID: 42054089](https://pubmed.ncbi.nlm.nih.gov/42054089/)).

**Advanced / experimental (preclinical for EOMD specifically):**
- **FBN2 protein replacement:** Intravitreal recombinant fbn2 rescued retinopathy in a retina-specific *Fbn2* knock-down mouse —

> *"After additional and repeated application of fbn2 recombinant protein, the retinopathy improved with an increase in retinal thickness and ERG amplitude"* — [PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/)

- **Elastase inhibition:** Preserving BrM elastin is a therapeutic strategy in mouse and human AMD models ([PMID: 37174708](https://pubmed.ncbi.nlm.nih.gov/37174708/)); alpha-1 antitrypsin augmentation is a related protease-inhibition approach ([PMID: 40210893](https://pubmed.ncbi.nlm.nih.gov/40210893/)).
- **Gene therapy / RNA therapy:** Conceptually attractive (AAV gene supplementation or editing) but **not yet reported** for *FBN2*-EOMD; the large *FBN2* cDNA (~8.6 kb) exceeds standard AAV capacity, a practical hurdle.

**Supportive/rehabilitative:** Low-vision aids, Amsler-grid self-monitoring, occupational therapy; AREDS-type antioxidant supplementation is of unproven benefit specifically in EOMD.

**Pharmacogenomics:** No EOMD-specific pharmacogenomic guidance. (Not available.)

---

## Prevention (Section 13)

- **Primary prevention:** Not possible for the genetic cause; general ocular-health and anti-oxidant/anti-smoking measures are reasonable but unproven in EOMD.
- **Secondary prevention:** Early detection via ophthalmic surveillance (OCT, Amsler grid) in known carriers to catch CNV promptly.
- **Tertiary prevention:** Prompt anti-VEGF for CNV to prevent irreversible vision loss.
- **Genetic counseling:** Central — autosomal-dominant inheritance with 50% transmission risk and incomplete/age-dependent penetrance; cascade testing and reproductive options (prenatal/PGT) can be discussed once the familial variant is known.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## Other Species / Natural Disease (Section 14)

- **Orthologous gene:** *Fbn2* (mouse NCBI Gene 14119; chromosome 18), highly conserved; fibrillin-2 function in elastic-fiber assembly and TGF-β/BMP regulation is evolutionarily conserved ([PMID: 19513754](https://pubmed.ncbi.nlm.nih.gov/19513754/)).
- **Natural disease in other species:** No well-characterized naturally-occurring FBN2 maculopathy in companion animals/wildlife is documented in the reviewed literature. (Not available.)
- **Comparative biology:** The conserved fibrillin/TGF-β axis underlies multiple species' connective-tissue phenotypes; mouse *Fbn2* models are informative (below).
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## Model Organisms (Section 15)

| Model | Type | Key features | Reference |
|-------|------|--------------|-----------|
| Retina-specific *Fbn2* knock-down mouse (AAV-sh-fbn2) | Mammalian, induced genetic | Exudative retinopathy of deep retinal layers, reduced axial length, reduced ERG amplitudes; **rescued by intravitreal fbn2 recombinant protein** | [PMID: 37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/) |
| ADAMTS10 WMS mouse (CRISPR) | Mammalian | Perturbed fibrillin microfibrils, abundant fibrillin-2, altered BMP/GDF8 and SMAD1/5/8 vs p38/MAPK signaling | [PMID: 30060141](https://pubmed.ncbi.nlm.nih.gov/30060141/) |
| *FBN2*-related connective-tissue models | Mammalian | Inform TGF-β/BMP dysregulation (systemic, not ocular) | [PMID: 17708531](https://pubmed.ncbi.nlm.nih.gov/17708531/) |

**Phenotype recapitulation:** The retina-specific *Fbn2* knock-down mouse reproduces the loss-of-function retinopathy and, importantly, demonstrates reversibility with protein replacement — strong support for a dosage-sensitive, treatable mechanism.
**Limitations:** It is a knock-down (not the human missense allele), targets retina acutely, and does not model the slow, lifelong human BrM degeneration or dominant inheritance dynamics.
**Resources:** MGI (*Fbn2*), IMPC/IMSR for additional alleles.

---

## Mechanistic Model / Interpretation

EOMD is a **monogenic model of the ECM arm of AMD**. The unifying interpretation across all five confirmed findings is that **fibrillin-2 is a structural-and-signaling keystone of the Bruch's-membrane elastic lamina**, and that reducing its function tips the macular RPE–BrM–choroid complex toward the same degenerative endpoint reached more slowly in polygenic, age-related AMD. The two mechanistic branches (structural weakening of the elastic sieve; dysregulated TGF-β/BMP bioavailability) are not alternatives but co-occurring consequences of the same lesion, and they converge on drusen formation, complement/inflammatory activation, elastin-breakdown-driven angiogenesis, and CNV. The fact that **common *FBN2* variation modestly raises AMD risk while rare *FBN2* variation causes early-onset Mendelian disease** is the clearest evidence that this single ECM gene operates along a dosage/severity continuum.

```
       RARE strong FBN2 variant           COMMON FBN2 variant (rs154001)
                │                                     │
         EOMD (Mendelian, AD)                 small ↑ AMD risk (OR 1.10)
                │                                     │
                └──────── shared BrM ECM pathology ───┘
                 (elastin loss, drusen, complement, CNV)
```

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|------|--------------------|----------------|
| [24899048](https://pubmed.ncbi.nlm.nih.gov/24899048/) | **Defining paper** — identifies FBN2 p.Glu1144Lys in EOMD family; BrM localization; rs154001 AMD association | Human genetics (WES + case-control) |
| [37100863](https://pubmed.ncbi.nlm.nih.gov/37100863/) | Reduced FBN2 in AMD/EOMD retina; knock-down mouse retinopathy rescued by FBN2 protein | Human tissue + model organism |
| [19513754](https://pubmed.ncbi.nlm.nih.gov/19513754/) | Fibrillins sequester TGF-β/BMP in ECM | Review / mechanism |
| [17708531](https://pubmed.ncbi.nlm.nih.gov/17708531/) | FBN mutations perturb TGF-β superfamily signaling | Review / mechanism |
| [19747980](https://pubmed.ncbi.nlm.nih.gov/19747980/) | BrM composition/function; drusen + complement as earliest AMD signs | Review |
| [35798060](https://pubmed.ncbi.nlm.nih.gov/35798060/) | Reduced BrM elastin integrity; EDPs and anti-elastin antibodies elevated | Review |
| [37174708](https://pubmed.ncbi.nlm.nih.gov/37174708/) | BrM elastin breakdown corresponds to CNV; elastase inhibition therapeutic | Human + mouse |
| [40210893](https://pubmed.ncbi.nlm.nih.gov/40210893/) | Alpha-1 antitrypsin maintains BrM integrity; lower in AMD donors | Mouse + human donor |
| [24938626](https://pubmed.ncbi.nlm.nih.gov/24938626/) | ECM/MMP-TIMP dysregulation in AMD BrM | Review |
| [41971199](https://pubmed.ncbi.nlm.nih.gov/41971199/), [42720932](https://pubmed.ncbi.nlm.nih.gov/42720932/) | EFEMP1 differential diagnosis | Human clinical |
| [17302207](https://pubmed.ncbi.nlm.nih.gov/17302207/) | Dominant early-onset maculopathy phenotyping/differential | Human clinical |
| [36368447](https://pubmed.ncbi.nlm.nih.gov/36368447/), [30060141](https://pubmed.ncbi.nlm.nih.gov/30060141/) | ADAMTS–fibrillin–TGF-β coupling | In vitro / mouse |
| [42026508](https://pubmed.ncbi.nlm.nih.gov/42026508/), [42054086](https://pubmed.ncbi.nlm.nih.gov/42054086/), [42054089](https://pubmed.ncbi.nlm.nih.gov/42054089/), [42177934](https://pubmed.ncbi.nlm.nih.gov/42177934/), [42132463](https://pubmed.ncbi.nlm.nih.gov/42132463/) | Anti-VEGF treatment evidence & CNV prognosis (extrapolated) | Human clinical |
| [42299845](https://pubmed.ncbi.nlm.nih.gov/42299845/), [39911746](https://pubmed.ncbi.nlm.nih.gov/39911746/), [40406865](https://pubmed.ncbi.nlm.nih.gov/40406865/), [40199564](https://pubmed.ncbi.nlm.nih.gov/40199564/), [40436996](https://pubmed.ncbi.nlm.nih.gov/40436996/) | FBN2 allelic disorders (CCA/aortic) — genotype–phenotype context | Human clinical |

---

## Limitations and Knowledge Gaps

1. **Small human cohort.** EOMD is defined by essentially one index family plus mutation screening; prevalence, penetrance estimates, age-of-onset distribution, and sex ratio are not robustly established.
2. **Mechanism largely inferred from AMD.** Much of the BrM elastin/complement/CNV cascade is demonstrated in AMD and model systems, then extrapolated to EOMD; direct EOMD tissue studies are limited to reduced FBN2 protein.
3. **Variant-specific functional data sparse.** The precise molecular consequence of p.Glu1144Lys (loss-of-function vs dominant-negative vs altered TGF-β sequestration) is not fully resolved.
4. **No EOMD natural history or registry data**; no validated EOMD-specific biomarkers or QoL instruments.
5. **Therapeutics are preclinical** (protein replacement, elastase inhibition); the large *FBN2* cDNA complicates AAV gene therapy.
6. **Modifier genes and gene–environment interactions** remain hypothetical.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the FBN2-EOMD cohort** via inherited-retinal-disease registries and GeneMatcher to firm up penetrance, expressivity, and onset distribution, and to build an allelic map distinct from CCA/aortic FBN2 variants.
2. **Functional characterization of p.Glu1144Lys** in RPE/organoid and microfibril-assembly assays: quantify microfibril integrity, TGF-β/BMP activation (SMAD2/3 vs SMAD1/5/8), and whether the allele is loss-of-function or dominant-negative.
3. **Knock-in mouse (or iPSC-RPE)** carrying the human missense allele to model dominant inheritance and slow BrM degeneration more faithfully than the knock-down.
4. **Biomarker validation:** test serum EDPs, anti-elastin antibodies, and circulating/tissue FBN2 as EOMD diagnostic/prognostic markers.
5. **Therapeutic development:** advance FBN2 protein replacement and elastase/protease-inhibition (including alpha-1 antitrypsin augmentation) toward CNV-prevention endpoints; evaluate dual-AAV or non-viral delivery to overcome FBN2 size limits.
6. **TGF-β/BMP axis modulation:** test whether normalizing TGF-β bioavailability mitigates drusen/CNV in models, given the ADAMTS–fibrillin–TGF-β coupling.

---

*Report compiled from 5 discovery iterations, 5 confirmed findings, and 26 reviewed papers. Evidence types are labeled (human clinical, model organism, in vitro, review/computational) throughout.*


## Artifacts

- [OpenScientist final report](Macular_Degeneration_Early-onset-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Macular_Degeneration_Early-onset-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014501` (3 mentions) - the report calls it "MONDO"; MONDO calls it **macular degeneration, early-onset**
- `HP:0000592` (1 mention) - the report calls it "Central scotoma"; HP calls it **Blue sclerae**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011510` (1 mention) - the report calls it "Macular drusen"; HP calls it **Drusen**
- `HP:0000572` (1 mention) - the report calls it "Visual impairment"; HP calls it **Visual loss**