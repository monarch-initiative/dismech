---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T17:32:01.355149'
end_time: '2026-10-23T17:46:51.721035'
duration_seconds: 890.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dysferlinopathy
  mondo_id: MONDO:0016145
  category: Mendelian
  causal_genes: DYSF
  omim_id: not recorded
  synonyms: qualitative or quantitative defects of dysferlin; DYSF-related muscular
    dystrophy; limb-girdle muscular dystrophy R2 dysferlin-related; Miyoshi myopathy
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
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 20
  validator_version: 0.3.0
term_validation:
  total_terms: 40
  verified: 35
  not_found: 1
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.028
  labels_checked: 11
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15431
    reported_labels:
    - gene therapy
    ontology_label: Hematopoietic Cell Transplantation
  labels_variant: 2
  unresolved_terms:
  - HP:0003734
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dysferlinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dysferlinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dysferlinopathy
- **MONDO ID:** MONDO:0016145 (if available)
- **Causal gene(s):** DYSF
- **OMIM:** not recorded
- **Synonyms:** qualitative or quantitative defects of dysferlin; DYSF-related muscular dystrophy; limb-girdle muscular dystrophy R2 dysferlin-related; Miyoshi myopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Dysferlinopathy** covering all of the
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

# Dysferlinopathy (MONDO:0016145): A Comprehensive Disease Characteristics Report

**Causal gene:** *DYSF* (dysferlin), chromosome 2p13.2 | **Inheritance:** Autosomal recessive | **Category:** Mendelian

---

## Summary

**Dysferlinopathy is an autosomal recessive muscular dystrophy caused by biallelic loss-of-function variants in *DYSF*, the gene encoding dysferlin — a large (~237 kDa), Ca²⁺-sensing, multi-C2-domain transmembrane protein responsible for repairing injured skeletal muscle plasma membrane (sarcolemma).** When both *DYSF* alleles are defective, muscle fibers lose the capacity to reseal the micro-tears generated by normal contraction. The consequence is a self-amplifying cycle of membrane leakage, complement activation, inflammation, myofiber necrosis, and progressive replacement of muscle with fat and fibrous tissue. This core lesion — a failure of Ca²⁺-dependent sarcolemmal resealing — was established directly in dysferlin-null mice ([PMID: 12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/)) and is remarkable for occurring despite a fully intact dystrophin-glycoprotein complex, distinguishing dysferlinopathy mechanistically from Duchenne/Becker muscular dystrophy.

Clinically, one gene produces a spectrum of phenotypes that classically falls into three overlapping presentations from the same mutational pool: **limb-girdle muscular dystrophy R2/2B** (proximal pelvic and shoulder-girdle weakness), **Miyoshi myopathy** (distal onset in the calf/gastrocnemius), and **distal myopathy with anterior tibial onset (DMAT/DACM)**. Onset is typically in the late teens to twenties, serum creatine kinase (CK) is markedly elevated, and progression is slow-to-intermediate, with loss of ambulation commonly in the fourth decade. Respiratory decline and cardiac involvement are usually late and affect a minority. A striking and clinically important feature is that affected individuals are frequently athletic before onset, and vigorous exercise appears to accelerate progression — a gene-environment interaction consistent with the membrane-repair defect.

There is currently **no approved disease-modifying therapy**; management is supportive (physiotherapy with exercise moderation, respiratory and cardiac surveillance, mobility aids). The leading experimental therapeutic is **dual/overlap-AAV full-length dysferlin gene replacement**, developed to circumvent the fact that the ~6.5 kb *DYSF* coding sequence exceeds single-AAV packaging capacity. Diagnosis rests on absent/markedly reduced dysferlin on muscle immunohistochemistry or Western blot (with peripheral blood monocytes as a validated surrogate), confirmed by *DYSF* genetic testing, supported by a characteristic — but not universal — muscle MRI fat-infiltration pattern.

---

## Key Findings

### 1. Genetic cause: biallelic *DYSF* loss of function (F001)

Dysferlinopathy is caused by biallelic (autosomal recessive) pathogenic variants in *DYSF* on chromosome 2p13. The gene was identified through positional cloning of a novel 6.9 kb muscle cDNA, whose protein product was named "dysferlin": *"we recently identified a novel, full-length 6.9 kb muscle cDNA, whose corresponding protein we designated 'dysferlin'"* ([PMID: 10791095](https://pubmed.ncbi.nlm.nih.gov/10791095/)). A defining genetic feature is phenotypic pleiotropy — the same mutation can manifest as different clinical syndromes: *"Identical mutations in the dysferlin gene can produce more than one myopathy phenotype (MM, limb-girdle dystrophy, distal myopathy with anterior tibial onset)"* ([PMID: 10791095](https://pubmed.ncbi.nlm.nih.gov/10791095/)). Biallelic pathogenic variants produce absent or reduced dysferlin in muscle.

- **Ontology:** Gene *DYSF* (HGNC:3097); disease MONDO:0016145.
- **Evidence type:** Human genetic / positional cloning.

### 2. Dysferlin protein architecture and Ca²⁺-sensitive phospholipid binding (F012)

Dysferlin is a large (~237 kDa) type-II transmembrane protein with a single C-terminal transmembrane anchor and multiple cytoplasmic C2 domains (C2A–C2G), plus DysF and FerA (four-helix bundle) domains; it is a member of the fer-1-like/ferlin family. The N-terminal **C2A domain binds negatively charged phospholipids (phosphatidylserine) in a Ca²⁺-sensitive manner**, and this activity is a direct target of disease mutations: *"A dysferlin point mutation responsible for muscular dystrophy was engineered into the dysferlin C2A domain and demonstrated reduced calcium-sensitive phospholipid binding"* ([PMID: 11959863](https://pubmed.ncbi.nlm.nih.gov/11959863/)). Beyond passive binding, ferlin C2 domains actively remodel membranes: *"dysferlin, otoferlin, and myoferlin do not merely passively adsorb to membranes but actively sculpt lipid bilayers"* ([PMID: 23859474](https://pubmed.ncbi.nlm.nih.gov/23859474/)). The FerA domain is a membrane-associating four-helix bundle ([PMID: 30026467](https://pubmed.ncbi.nlm.nih.gov/30026467/)), and structural comparison of myoferlin vs dysferlin C2A domains reveals distinct membrane-binding behavior ([PMID: 31004665](https://pubmed.ncbi.nlm.nih.gov/31004665/)).

- **Ontology:** GO:0005544 (calcium-dependent phospholipid binding); CHEBI:18303 phosphatidyl-L-serine; InterPro ferlin / C2 / DysF / FerA domains.
- **Evidence type:** In vitro / structural biology.

### 3. Primary mechanism: defective Ca²⁺-dependent sarcolemmal membrane repair (F008)

The dysferlin-null mouse provides the definitive demonstration of the core disease mechanism. These mice develop progressive muscular dystrophy despite an intact dystrophin-glycoprotein complex: *"dysferlin-null mice maintain a functional dystrophin-glycoprotein complex but nevertheless develop a progressive muscular dystrophy"* ([PMID: 12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/)). Using a two-photon laser injury assay, dysferlin-deficient fibers fail to reseal: *"dysferlin-deficient muscle fibres are defective in Ca2+-dependent sarcolemma resealing"* ([PMID: 12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/)). In healthy muscle, dysferlin-enriched vesicles accumulate and fuse to form a membrane "patch" at the injury site; in dysferlin-null muscle, sub-sarcolemmal vesicles accumulate but do not resolve the lesion. Dysferlin is the vertebrate homologue of *C. elegans* fer-1, which mediates vesicle fusion in spermatids — underscoring an evolutionarily conserved membrane-fusion role.

- **Ontology:** GO:0061024 (membrane organization); GO:0001778 (plasma membrane repair); CL:0008002 (skeletal muscle fiber).
- **Evidence type:** Model organism (mouse) + in vitro injury assay.

### 4. The membrane-repair complex: MG53(TRIM72)–caveolin-3–dysferlin (F014, F002)

Dysferlin does not act alone. A molecular complex of **MG53 (TRIM72), caveolin-3 (Cav3), and dysferlin** is required for sarcolemmal repair: *"a molecular complex formed by MG53, dysferlin, and Cav3 is essential for repair of muscle membrane damage"* ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/)). MG53 performs the trafficking step: *"MG53 mediates active trafficking of intracellular vesicles to the sarcolemma and is required for movement of dysferlin to sites of cell injury during repair patch formation"* ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/)). This explains why caveolin-3 mutations (e.g., P104L, R26Q) that trap Cav3 in the Golgi produce aberrant MG53/dysferlin localization and defective repair in a dominant-negative fashion — linking several muscular dystrophies through a shared repair pathway.

- **Ontology:** GO:0048306 (calcium-dependent protein binding); protein partners TRIM72/MG53, CAV3.
- **Evidence type:** In vitro / cell biology.

### 5. Complement activation as a disease-specific downstream effector (F002)

A critical, therapeutically actionable discovery is that the immune/complement system is a central downstream amplifier of muscle injury specifically in dysferlinopathy. In dysferlin-null mice, complement factors are upregulated in muscle, and genetic ablation of the central complement component C3 is protective: *"genetic disruption of the central component (C3) of the complement system ameliorated muscle pathology in dysferlin-deficient mice but had no significant beneficial effect in a genetically distinct model of muscular dystrophy, mdx mice"* ([PMID: 21060153](https://pubmed.ncbi.nlm.nih.gov/21060153/)). The fact that C3 ablation helps dysferlin-deficient but **not** mdx (dystrophin-deficient) mice demonstrates that complement is a disease-specific, not generic, driver — making it a rational, dysferlinopathy-selective therapeutic target.

- **Ontology:** GO:0006956 (complement activation); GO:0006954 (inflammatory response).
- **Evidence type:** Model organism (mouse genetics).

### 6. Clinical spectrum: three classic phenotypes from one gene (F010)

Dysferlinopathy presents as a clinical spectrum with three classic presentations: *"limb-girdle muscular dystrophy 2B (LGMD2B) with predominantly proximal weakness, Miyoshi myopathy (MM) with calf muscle weakness and atrophy, and distal myopathy with anterior tibial onset (DMAT) with tibialis muscle atrophy"* ([PMID: 23254335](https://pubmed.ncbi.nlm.nih.gov/23254335/)). Onset is typically young-adult (late teens to twenties), with markedly elevated serum CK and muscle biopsy showing absence/drastic decrease of dysferlin on immunohistochemistry. Recurrent mutations differ by population (e.g., c.3112C>T and c.1045dup reported in China).

| Phenotype | Primary muscle involvement | HPO suggestion |
|---|---|---|
| LGMD R2 / LGMD2B | Proximal — pelvic & shoulder girdle | HP:0003701 (proximal muscle weakness) |
| Miyoshi myopathy (MM) | Distal — calf/gastrocnemius weakness & atrophy | HP:0003693 (distal amyotrophy); HP:0003734 |
| DMAT / DACM | Distal — tibialis anterior atrophy | HP:0009053 (distal lower-limb weakness) |
| Shared | Elevated CK | HP:0003236 (elevated serum CK) |

- **Evidence type:** Human clinical / genetic cohort.

### 7. Epidemiology within the LGMD landscape, and founder effects (F009, F003)

Dysferlinopathy is a substantial contributor to autosomal recessive LGMD. In a large Italian cohort (181 patients / 155 families), it was the second most common defect, with *"LGMD2B (dysferlin) 18.7%"* of cases, behind calpainopathy (LGMD2A, 28.4%) ([PMID: 17994539](https://pubmed.ncbi.nlm.nih.gov/17994539/)). Clinical severity ranking among LGMD subtypes was reported as: *"The order of decreasing clinical severity was: sarcoglycanopathy, calpainopathy, dysferlinopathy, and caveolinopathy"* ([PMID: 17994539](https://pubmed.ncbi.nlm.nih.gov/17994539/)). Frequency varies geographically — the Czech cohort was dominated by calpainopathy with *"a smaller proportion of LGMD R2 dysferlin-related"* ([PMID: 37526466](https://pubmed.ncbi.nlm.nih.gov/37526466/)).

Founder mutations and ethnic clustering are well documented: *"Three ethnic clusters have previously been described in Dysferlinopathy: the Libyan Jewish population originating in the area of Tripoli, Italian and Spanish populations"* ([PMID: 17825554](https://pubmed.ncbi.nlm.nih.gov/17825554/)). In Jews of the Caucasus, a homozygous frameshift (c.2779delG, codon 927) causes dysferlin truncation/loss, with a quantified carrier burden: *"The possible existence of a founder effect is strengthened by our finding of a 4% carrier frequency in this community"* ([PMID: 17825554](https://pubmed.ncbi.nlm.nih.gov/17825554/)).

- **Evidence type:** Human clinical / population genetics.

### 8. Natural history and muscle MRI fat-fraction progression (F004)

The Jain Clinical Outcome Study (COS) is the key natural-history dataset: *"The Jain Clinical Outcome Study for Dysferlinopathy (COS) followed the largest cohort of patients (n=187) with genetically confirmed dysferlinopathy throughout a three-year natural history study"* ([PMID: 36972667](https://pubmed.ncbi.nlm.nih.gov/36972667/)). Longitudinal muscle-MRI fat-fraction (FF) modeling showed FF *"was expected to be higher the older patients were and the earlier the age at symptom onset"* and that *"Women had absolute FF values 8.8% higher than men in the lower leg"* ([PMID: 40740171](https://pubmed.ncbi.nlm.nih.gov/40740171/)). Muscles acting on the same joint movement progressed similarly; no FF-trajectory differences were found by ethnicity or specific genetic variant. Importantly, although a classical thigh-dominant MRI pattern exists, roughly 63% of patients failed at least one established imaging criterion and ~13% were outliers ([PMID: 36972667](https://pubmed.ncbi.nlm.nih.gov/36972667/)) — so imaging supports, but cannot replace, molecular diagnosis.

- **Evidence type:** Human natural-history cohort / imaging.

### 9. Prognosis: slow-to-intermediate progression; wheelchair in the 4th decade (F011)

A Tunisian cohort (n=20; sex ratio 1; median age 50.5 y; follow-up 5–48 y) found median age at onset 17 y, with phenotype distribution LGMDR2 35%, proximodistal 35%, Miyoshi 10%, DMAT 10%, asymptomatic hyperCKemia 10%. At last evaluation, *"more than half of patients (55%) were on wheelchair. Loss of ambulation occurred generally during the fourth decade"* ([PMID: 37716854](https://pubmed.ncbi.nlm.nih.gov/37716854/)). *"Disease progression was mainly slow to intermediate regardless of the phenotype"* with marked intra- and inter-familial heterogeneity ([PMID: 37716854](https://pubmed.ncbi.nlm.nih.gov/37716854/)). Late cardiac complications affected a minority: *"two patients with a proximodistal phenotype (10%) developed dilated cardiomyopathy and mitral valve regurgitation"* ([PMID: 37716854](https://pubmed.ncbi.nlm.nih.gov/37716854/)), generally after ~20 years of disease.

- **Evidence type:** Human clinical longitudinal cohort.

### 10. Respiratory and cardiac involvement (F005)

In 48 Japanese dysferlinopathy patients, respiratory involvement was present in a minority: *"Of the 47 patients, 10 had reduced percent forced vital capacity (%FVC), and 4 required non-invasive positive pressure ventilation"* ([PMID: 26088049](https://pubmed.ncbi.nlm.nih.gov/26088049/)). %FVC correlated with disease duration and was lower in non-ambulatory and older (≥65 y) patients. QRS prolongation occurred in 19/46 on ECG, and while echocardiography showed no overt LV dysfunction, *"Histopathology of autopsied cases revealed mild cardiomyopathy and moderate diaphragm involvement"* ([PMID: 26088049](https://pubmed.ncbi.nlm.nih.gov/26088049/)). This supports a surveillance (not continuous intervention) posture for heart and lungs, and is consistent with a growing literature on dysferlin's role in cardiomyocyte membrane integrity and t-tubule biology ([PMID: 26415898](https://pubmed.ncbi.nlm.nih.gov/26415898/), [PMID: 39011635](https://pubmed.ncbi.nlm.nih.gov/39011635/), [PMID: 24572254](https://pubmed.ncbi.nlm.nih.gov/24572254/)).

- **Evidence type:** Human clinical + autopsy.

### 11. Diagnosis via peripheral blood monocyte dysferlin assay (F007)

Dysferlin is expressed in peripheral blood monocytes (PBM), providing a minimally invasive diagnostic surrogate. Western blot of PBM shows reductions concordant with muscle: *"A comparable severe reduction in dysferlin was demonstrated in both skeletal muscle and PBM"* ([PMID: 21658164](https://pubmed.ncbi.nlm.nih.gov/21658164/)). This is particularly valuable in monoallelic cases: *"Dysferlin and/or dysferlin mRNA abnormalities are diagnostic for dysferlinopathy when mutational analysis detects a mutation in one allele only"* ([PMID: 21658164](https://pubmed.ncbi.nlm.nih.gov/21658164/)). mRNA analysis helps distinguish symptomatic heterozygotes from true patients, and MLPA detects large deletions/duplications missed by sequencing.

- **Evidence type:** Human diagnostic / in vitro.

### 12. Gene-environment interaction: exercise accelerates progression (F013)

A mechanistically coherent and clinically crucial observation is that mechanical overload worsens disease: *"A retrospective cohort study suggests that exercise may actually increase rate of disease progression in dysferlinopathy"* ([PMID: 30036194](https://pubmed.ncbi.nlm.nih.gov/30036194/)). Because contraction generates sarcolemmal micro-injuries that dysferlin-deficient fibers cannot efficiently reseal, mechanical stress directly drives myofiber damage. This matches the frequent clinical history of an athletic premorbid phase followed by rapid decline, and argues for exercise moderation in management.

- **Evidence type:** Human retrospective cohort + mechanistic inference.

### 13. Dual-AAV gene replacement as the lead experimental therapy (F006)

The *DYSF* coding sequence (~6.5 kb) exceeds single-AAV packaging capacity (~4.7 kb). Dual/overlap-AAV vectors reconstitute the full-length protein: *"Dual adeno-associated virus vectors have been developed, defined by a region of homology, to serve as a substrate for reconstitution of the full 6.5 kb dysferlin cDNA"* ([PMID: 28707952](https://pubmed.ncbi.nlm.nih.gov/28707952/)). Systemic delivery in dysferlin-deficient mice produced long-term expression and functional improvement (membrane repair, MRI/MRS) 4–13 months post-treatment. Truncated "nanodysferlins" are an alternative, but have functional limits: *"Nanodysferlins support membrane repair and binding to TRIM72/MG53 but do not localize to t-tubules or stabilize Ca[2+]"* ([PMID: 38779337](https://pubmed.ncbi.nlm.nih.gov/38779337/)) — indicating full-length protein may be needed to restore t-tubule and calcium-handling functions.

- **Ontology:** NCIT:C15431 (gene therapy); adeno-associated viral vector.
- **Evidence type:** Model organism (mouse) preclinical.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *DYSF* (2p13.2)** result in absent or severely reduced dysferlin protein in skeletal muscle. *(Demonstrated — human genetics + protein assays.)*
2. **Loss of dysferlin** removes the Ca²⁺-sensor/membrane-fusion component of the sarcolemmal repair machinery; the C2A domain's Ca²⁺-dependent phosphatidylserine binding is lost. *(Demonstrated — in vitro C2A mutation studies.)*
3. **Normal muscle contraction generates micro-tears** in the sarcolemma; intracellular Ca²⁺ influx at the lesion normally nucleates a dysferlin-enriched repair patch delivered by MG53 trafficking in complex with caveolin-3. *(Demonstrated — mouse laser-injury imaging + complex biochemistry.)*
4. **Without dysferlin, Ca²⁺-dependent resealing fails** → the membrane tear persists; sub-sarcolemmal vesicles accumulate but cannot form a competent patch. *(Demonstrated — dysferlin-null mouse.)*
5. **Unresealed membrane leaks** → sustained Ca²⁺ overload, leakage of CK into blood (very high serum CK), and exposure of intracellular contents. *(Demonstrated/inferred.)*
6. **BRANCH A — Complement/inflammation:** membrane damage triggers complement activation (C3-dependent), inflammatory cell infiltration, and amplification of myofiber injury — a disease-specific effector (C3 ablation rescues dysferlin-null but not mdx mice). *(Demonstrated — mouse genetics.)*
7. **Repeated injury → myofiber necrosis and degeneration-regeneration cycling** that eventually exhausts/outpaces repair. *(Demonstrated/inferred.)*
8. **Fibro-fatty replacement of muscle** (quantifiable as rising MRI fat fraction with age and earlier onset) → progressive weakness. *(Demonstrated — natural-history imaging.)*
9. **Clinical manifestation:** proximal (LGMD R2), distal-calf (Miyoshi), or anterior-tibial (DMAT) weakness; slow-to-intermediate progression to wheelchair dependence (commonly 4th decade); late/minor respiratory (diaphragm) and cardiac (mild cardiomyopathy, QRS prolongation) involvement. *(Demonstrated — human cohorts.)*
10. **MODIFIER — mechanical overload/exercise** accelerates steps 3–8 by increasing injury faster than the deficient repair system can compensate. *(Human retrospective + mechanistic inference.)*

```
  DYSF biallelic LoF
          │
          ▼
  Absent dysferlin ──► C2A loses Ca²⁺-dependent PS binding
          │
          ▼
  Contraction micro-tears ──► Ca²⁺ influx
          │                         │
          ▼                         ▼
  FAILED Ca²⁺-dependent        (MG53–Cav3–dysferlin
  membrane resealing            patch cannot form)
          │
    ┌─────┴───────────────┐
    ▼                     ▼
 Complement (C3)     Ca²⁺ overload /
 + inflammation      CK leak
    │                     │
    └──────────┬──────────┘
               ▼
       Myofiber necrosis
               ▼
   Fibro-fatty replacement (↑MRI fat fraction)
               ▼
   Progressive weakness → wheelchair (~4th decade)
        + late diaphragm/cardiac involvement
               ▲
   Exercise / mechanical overload = accelerant
```

### Upstream vs downstream

- **Upstream (initiating, disease-defining):** *DYSF* mutation → absent dysferlin → failed Ca²⁺-dependent membrane repair. These are necessary and causal.
- **Downstream (effectors / amplifiers, candidate drug targets):** complement C3 activation, inflammation, Ca²⁺ dysregulation, necrosis, fibro-fatty remodeling. These are modifiable without correcting the genetic defect.
- **Modifier:** mechanical load (exercise) acts on the injury-generation rate.

### Anatomy, cells, and compartments

| Level | Structures involved | Ontology suggestion |
|---|---|---|
| Organ/system | Skeletal muscle (musculoskeletal system); secondary: diaphragm (respiratory), heart (minor/late) | UBERON:0001134 (skeletal muscle tissue); UBERON:0001103 (diaphragm); UBERON:0000948 (heart) |
| Tissue | Striated skeletal muscle | UBERON:0002036 / muscle tissue |
| Cell | Skeletal muscle fiber; satellite cell/myoblast; macrophage; peripheral blood monocyte (diagnostic surrogate) | CL:0008002 (skeletal muscle fiber); CL:0000056 (myoblast); CL:0000235 (macrophage); CL:0000576 (monocyte) |
| Subcellular | Sarcolemma (plasma membrane), cytoplasmic vesicles, T-tubules, sarcoplasmic reticulum junctional complexes | GO:0042383 (sarcolemma); GO:0030315 (T-tubule); GO:0016529 (sarcoplasmic reticulum) |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [10791095](https://pubmed.ncbi.nlm.nih.gov/10791095/) | Positional cloning of Miyoshi/LGMD gene | Human genetic | F001 — DYSF identity, pleiotropy |
| [12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/) | *Defective membrane repair in dysferlin-deficient MD* | Mouse + in vitro | F008 — core Ca²⁺-resealing defect |
| [19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/) | *MG53–Cav3–dysferlin membrane repair* | In vitro | F014, F002 — repair complex |
| [21060153](https://pubmed.ncbi.nlm.nih.gov/21060153/) | *Complement C3 ablation attenuates pathology* | Mouse genetics | F002 — disease-specific complement driver |
| [11959863](https://pubmed.ncbi.nlm.nih.gov/11959863/) | *Ca²⁺-sensitive phospholipid binding of C2 domains* | In vitro | F012 — mutation disrupts C2A binding |
| [23859474](https://pubmed.ncbi.nlm.nih.gov/23859474/) | *C2 domains alter lipid bilayer packing* | In vitro | F012 — active membrane sculpting |
| [30026467](https://pubmed.ncbi.nlm.nih.gov/30026467/) | *FerA four-helix bundle domain* | Structural | F012 — FerA domain |
| [31004665](https://pubmed.ncbi.nlm.nih.gov/31004665/) | *Myoferlin vs dysferlin C2A structure* | Structural | F012 — C2A membrane binding |
| [23254335](https://pubmed.ncbi.nlm.nih.gov/23254335/) | *DYSF mutations in Chinese patients* | Human clinical | F010 — three phenotypes |
| [17994539](https://pubmed.ncbi.nlm.nih.gov/17994539/) | *Italian LGMD correlations* | Human cohort | F009 — 18.7% frequency, severity rank |
| [37526466](https://pubmed.ncbi.nlm.nih.gov/37526466/) | *Czech LGMD genetics* | Human cohort | F009 — geographic variation |
| [17825554](https://pubmed.ncbi.nlm.nih.gov/17825554/) | *Dysferlinopathy in Caucasus Jews* | Population genetics | F003 — founder effects, 4% carrier |
| [36972667](https://pubmed.ncbi.nlm.nih.gov/36972667/) | *Muscle imaging outlier population* | Human imaging | F004 — COS cohort, MRI pattern |
| [40740171](https://pubmed.ncbi.nlm.nih.gov/40740171/) | *Longitudinal fat-fraction modeling* | Human imaging | F004 — FF predictors, sex difference |
| [37716854](https://pubmed.ncbi.nlm.nih.gov/37716854/) | *Dysferlinopathy in Tunisia* | Human longitudinal | F011 — progression, prognosis |
| [26088049](https://pubmed.ncbi.nlm.nih.gov/26088049/) | *Respiratory/cardiac function (Japan)* | Human + autopsy | F005 — respiratory/cardiac |
| [21658164](https://pubmed.ncbi.nlm.nih.gov/21658164/) | *Dysferlin in muscle and monocytes* | Human diagnostic | F007 — PBM assay, monoallelic dx |
| [28707952](https://pubmed.ncbi.nlm.nih.gov/28707952/) | *Dysferlin overlap-vector delivery* | Mouse preclinical | F006 — dual-AAV therapy |
| [38779337](https://pubmed.ncbi.nlm.nih.gov/38779337/) | *Nanodysferlins* | In vitro | F006 — truncated construct limits |
| [30036194](https://pubmed.ncbi.nlm.nih.gov/30036194/) | *Exercise in muscle disorders* | Human retrospective | F013 — exercise accelerant |

**Convergence of evidence:** The core mechanism (failed Ca²⁺-dependent sarcolemmal repair) is supported by independent lines — mouse genetics ([PMID: 12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/)), structural/biochemical studies of the C2A domain ([PMID: 11959863](https://pubmed.ncbi.nlm.nih.gov/11959863/), [PMID: 23859474](https://pubmed.ncbi.nlm.nih.gov/23859474/)), and the repair-complex biology ([PMID: 19380584](https://pubmed.ncbi.nlm.nih.gov/19380584/)). The complement-C3 finding ([PMID: 21060153](https://pubmed.ncbi.nlm.nih.gov/21060153/)) is particularly strong because it uses a disease-specific control (mdx mice) to show selectivity.

---

## Section-by-Section Template Coverage

### 1. Disease Information
Dysferlinopathy (MONDO:0016145) is an autosomal recessive, progressive muscular dystrophy caused by *DYSF* deficiency. Key identifiers: gene *DYSF* (HGNC:3097, 2p13.2, NCBI Gene 8291, UniProt O75923); MONDO:0016145; OMIM gene 603009, LGMD2B/R2 253601, Miyoshi myopathy 1 254130, DMAT 606768; Orphanet ORPHA:206 (dysferlinopathy), ORPHA:268 (LGMD2B), ORPHA:45448 (Miyoshi); ICD-10 G71.0, ICD-11 8C70.0; MeSH "Muscular Dystrophies, Limb-Girdle"/"Distal Myopathies". Synonyms: qualitative/quantitative defects of dysferlin; DYSF-related muscular dystrophy; LGMD R2 dysferlin-related (formerly LGMD2B); Miyoshi myopathy; distal anterior compartment myopathy (DMAT/DACM); primary dysferlinopathy. Information is drawn from aggregated disease-level resources and clinical cohorts (not single-patient EHR).

### 2. Etiology
**Primary cause:** genetic — biallelic loss-of-function *DYSF* variants (F001). **Genetic risk:** causal variants span missense, frameshift, nonsense, splice-site, and large deletions/duplications; founder alleles cluster in Libyan Jewish, Italian, Spanish, and Caucasus Jewish (c.2779delG) populations (F003). No established non-genetic cause. **Environmental/modifier:** mechanical overload / vigorous exercise accelerates progression — the principal documented gene-environment interaction (F013). **Protective factors:** none genetically established; exercise moderation is the main modifiable protective behavior (inference from F013). **Modifier genes:** candidate repair-pathway partners (MG53/TRIM72, CAV3, annexins, AHNAK) are mechanistically implicated, but no validated human severity-modifier locus is established.

### 3. Phenotypes
Core phenotypes (with HPO suggestions): proximal muscle weakness (HP:0003701), distal/calf weakness and atrophy (HP:0003693, HP:0003734), tibialis anterior atrophy / foot drop (HP:0009027), markedly elevated serum CK / hyperCKemia (HP:0003236), difficulty climbing stairs (HP:0003551), scapular winging (HP:0003691), loss of ambulation (HP:0002505), restrictive ventilatory defect (HP:0002091), and (minority/late) dilated cardiomyopathy (HP:0001644). Onset: young-adult (late teens–20s; median ~17 y, F011). Severity: moderate (intermediate among LGMDs, F009). Progression: slow-to-intermediate, progressive (F011). Frequency: proximal and distal forms each ~35% in one cohort; asymptomatic hyperCKemia ~10% (F011). QoL impact is driven primarily by progressive mobility loss (wheelchair commonly in the 4th decade), with preserved cognition.

### 4. Genetic / Molecular
Causal gene *DYSF* (2p13.2, ~55 exons, protein 2080 aa / ~237 kDa) (F001, F012). Variant classes: missense, frameshift, nonsense, splice-site, structural (MLPA-detectable CNVs) (F007, F010). Example alleles: c.2779delG (Caucasus founder, F003), c.5289G>C/p.Glu1763Asp (F007), c.1375dup/p.Met459Asnfs*15 (F010 literature), c.3112C>T and c.1045dup (China, F010). Functional consequence: loss of function — truncating alleles abolish protein; missense alleles destabilize dysferlin and/or impair C2A Ca²⁺/phospholipid binding (F012). Germline, inherited; not somatic. No disease-specific epigenetic or large-chromosomal mechanism. Founder allele carrier frequency up to 4% (F003).

### 5. Environmental
No toxin, infectious, or occupational cause. The one robust environmental modifier is **mechanical load/exercise** accelerating progression (F013). High-intensity/eccentric exercise is relatively contraindicated.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above (F001→F012→F008→F014→F002→F004→F010/F011). Molecular processes: Ca²⁺-dependent phospholipid binding and vesicle fusion (GO:0005544, GO:0061025), plasma-membrane repair (GO:0001778), complement activation (GO:0006956), inflammation (GO:0006954). Cell types: skeletal muscle fiber (CL:0008002), satellite cell/myoblast (CL:0000056), macrophage (CL:0000235), monocyte (CL:0000576). Compartments: sarcolemma (GO:0042383), T-tubule (GO:0030315). Inflammatory infiltrates can mimic polymyositis on biopsy (a diagnostic pitfall).

### 7. Anatomical Structures
Primary: skeletal muscle (UBERON:0001134), with characteristic pelvic/posterior-thigh, gastrocnemius/soleus (UBERON:0011907), and tibialis anterior (UBERON:0001385) patterns. Secondary: diaphragm (UBERON:0001103) and heart (UBERON:0000948), generally late/mild (F005). CNS, cognition, and sensation are spared. Subcellular lesion localizes to the sarcolemma and vesicular trafficking machinery. Involvement is bilateral and roughly symmetric, limb-predominant.

### 8. Temporal Development
Onset: young adulthood (median ~17 y), insidious/chronic; presymptomatic hyperCKemia often precedes weakness. Course: slow-to-intermediate, steadily progressive (not relapsing-remitting). Stages: (i) presymptomatic hyperCKemia; (ii) early ambulant weakness; (iii) advancing proximal+distal weakness; (iv) loss of ambulation (~4th decade, F011); (v) wheelchair with possible respiratory/cardiac complications. Lifelong; no spontaneous remission. Critical intervention window is the long presymptomatic/early-ambulant phase before extensive fibro-fatty replacement (F004).

### 9. Inheritance and Population
Autosomal recessive (F001); high penetrance with variable expressivity; no anticipation (not a repeat disorder); germline mosaicism not recognized. ~18.7% of Italian LGMD (F009); Orphanet-order prevalence for LGMD2B ~1–9/1,000,000 generally, higher in founder communities. Founder effects with population-specific alleles; consanguinity increases local prevalence (F003). Carrier frequency up to 4% in specific communities. Sex ratio ~1:1 (F011), though women show higher lower-leg MRI fat fraction (F004).

### 10. Diagnostics
Markedly elevated serum CK (often 10–150× ULN; LOINC 2157-6) is the key screen. Muscle biopsy: dystrophic changes, often with inflammation, and absent/reduced dysferlin on IHC/Western blot (F010). Peripheral blood monocyte dysferlin Western blot is a validated surrogate, useful in monoallelic cases (F007). Muscle MRI shows a characteristic but non-universal (~63% fail ≥1 criterion) fat-infiltration pattern (F004). EMG myopathic; ECG may show QRS prolongation (F005). Genetic confirmation via NGS neuromuscular panel or WES + MLPA (CNVs); WGS resolves deep-intronic variants. Karyotype/FISH/CMA/mtDNA/repeat testing not applicable. Differential diagnosis: other recessive LGMDs (calpainopathy LGMD R1, anoctaminopathy LGMD R12, sarcoglycanopathies, FKRP LGMD R9), inflammatory myopathy/polymyositis, Pompe disease, and other distal myopathies (GNE, ANO5). No newborn screening; cascade/founder-variant screening appropriate.

### 11. Outcome / Prognosis
Near-normal lifespan in most; mortality low, usually from late respiratory or (rarely) cardiac complications. Major morbidity is progressive mobility loss — ~55% wheelchair-dependent, loss of ambulation in the 4th decade (F011). Complications: restrictive respiratory insufficiency (minority need NIV, F005), dilated cardiomyopathy in ~10% after ~20 years (F011), contractures, falls. Prognostic factors: earlier onset and older age predict higher MRI fat fraction (F004); female sex associated with higher lower-leg FF. Prognostic biomarkers: MRI fat fraction (validated), serum CK, functional outcome measures.

### 12. Treatment
No approved disease-modifying drug; management supportive/multidisciplinary. Supportive/rehabilitative: physiotherapy with exercise moderation (F013), occupational therapy (NCIT:C15329), orthoses, mobility aids, respiratory support (NIV when FVC declines, F005; NCIT:C94400), cardiac monitoring with standard heart-failure therapy if cardiomyopathy develops, nutrition/weight management. Pharmacotherapy: no proven agent; unlike Duchenne, corticosteroids are not established and may be detrimental. Experimental lead: dual/overlap-AAV full-length dysferlin gene replacement (F006; NCIT:C15431). Downstream-target strategies (complement inhibition, F002; membrane-repair enhancers such as recombinant MG53; exon skipping) are preclinical/early-phase. Nanodysferlin constructs partially rescue but miss t-tubule/Ca²⁺ functions (F006). Main gene-therapy translational risks: anti-capsid/transgene immunity, hepatotoxicity.

### 13. Prevention
No primary prevention of the genetic disease; genetic counseling, carrier/cascade screening, and reproductive options (prenatal diagnosis, preimplantation genetic testing) in known families/founder communities (F003). Secondary: early CK testing and family screening. Tertiary: activity modification to reduce exercise-driven damage (F013), respiratory/cardiac surveillance, physiotherapy for contractures, vaccination against respiratory pathogens in those with reduced pulmonary reserve. Immunization/public-health/environmental interventions not applicable to causation.

### 14. Other Species / Natural Disease
*DYSF* is evolutionarily conserved: mouse *Dysf* (NCBI Gene 26903; Taxon 10090), rat *Dysf* (Taxon 10116), zebrafish *dysf* (Taxon 7955), and the invertebrate homologue *fer-1* in *C. elegans* (Taxon 6239). The membrane-repair/vesicle-fusion function is conserved from fer-1 (spermatid vesicle fusion) to mammalian dysferlin (sarcolemmal repair) (F008). Dysferlin-deficient dystrophy occurs naturally and in engineered mouse strains; it is not a prominent natural veterinary entity. Not zoonotic or communicable.

### 15. Model Organisms
**Mouse (primary, recapitulates disease well):** dysferlin-null knockouts develop progressive dystrophy with defective Ca²⁺-dependent resealing despite intact dystrophin-glycoprotein complex (F008) — the definitive model-organism proof of mechanism. Naturally dysferlin-deficient strains include SJL/J (splice-site) and A/J (ETn insertion); the congenic B6.A-Dysf (Bla/J) is a clean-background model. These show late-onset, slowly progressive proximal/pelvic and paraspinal myopathy with inflammation and complement upregulation (F002), and serve as the AAV gene-therapy platform (F006). **Limitations:** murine disease is milder, slower, and less distal than human Miyoshi myopathy; cardiac phenotype is subtle; muscle-group distribution differs. **In vitro/cellular:** patient myoblasts/myotubes, iPSC-derived myocytes, and recombinant C2/FerA/DysF constructs for biophysics (F012); laser-wounding repair assays. **Other organisms:** zebrafish *dysf* mutants (muscle integrity); *C. elegans* fer-1 (ancestral ferlin biology). Resources: MGI, IMSR, Jackson Laboratory, Jain Foundation repositories.

---

## Limitations and Knowledge Gaps

1. **No primary molecular-profiling data were generated** in this investigation; all findings are literature-derived. No patient-level transcriptomic, proteomic, or metabolomic datasets were analyzed.
2. **Genotype–phenotype correlation remains weak.** The same mutation produces different phenotypes (F001), and the COS found no FF-trajectory differences by variant (F004) — the modifiers determining proximal vs distal onset are unidentified.
3. **Complement as a human therapeutic target is unproven.** The C3 evidence is from mouse genetics (F002); no human complement-inhibition trial outcome is reported here.
4. **Cardiac risk is ambiguous.** Overt LV dysfunction was absent on echocardiography in the Japanese cohort, yet autopsy showed mild cardiomyopathy and a minority develop dilated cardiomyopathy late (F005, F011) — true cardiac natural history needs prospective cardiac MRI.
5. **Exercise evidence is retrospective** (F013); the dose/intensity threshold that is harmful vs beneficial is undefined, and prospective controlled studies are lacking.
6. **Gene-therapy data are preclinical** (mouse) (F006); human efficacy, durability, immunogenicity, and the functional adequacy of reconstituted vs full-length protein (nanodysferlin t-tubule deficit) are unresolved.
7. **Epidemiology is region-biased.** Prevalence estimates derive from referral cohorts (Italy, Czechia, Tunisia, Japan) rather than population-based registries; a precise global prevalence (per 100,000) was not established.

## Proposed Follow-up Experiments / Actions

1. **Analyze a human dysferlinopathy transcriptomic/proteomic dataset (GEO/PRIDE)** to confirm complement and inflammatory pathway upregulation in patient muscle and identify candidate severity modifiers — directly testing whether the mouse C3 mechanism (F002) operates in humans.
2. **Build a genotype–phenotype modifier analysis** using the Jain COS cohort (F004): test whether residual dysferlin level (not just variant type) predicts FF trajectory, and whether the female lower-leg FF excess (8.8%) reflects fiber-type or hormonal modifiers.
3. **Prospective cardiac MRI substudy** to resolve the echo-vs-autopsy discrepancy (F005) and define true cardiac penetrance and timing.
4. **Prospective controlled exercise-dosing study** to quantify the harmful threshold and whether low-intensity activity is safe/beneficial (F013).
5. **Human trial design for complement inhibition** (e.g., C3/C5-targeted agents) as a downstream, disease-specific therapy independent of gene correction (F002).
6. **Head-to-head preclinical comparison of dual-AAV full-length dysferlin vs nanodysferlin** on t-tubule localization and Ca²⁺ handling, to settle whether truncated constructs are therapeutically sufficient (F006).
7. **Expand carrier-screening programs** in identified founder populations (Libyan/Caucasus Jewish, Italian, Spanish) given quantified carrier frequencies up to 4% (F003).

---

*Report compiled from 14 confirmed findings across 5 iterations and 34 reviewed papers. Evidence types span human clinical cohorts, population genetics, mouse models, in vitro/structural biology, and preclinical gene therapy.*


## Artifacts

- [OpenScientist final report](Dysferlinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dysferlinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 11 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15431` (2 mentions) - the report calls it "gene therapy"; NCIT calls it **Hematopoietic Cell Transplantation**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003734` (2 mentions) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0009053` (1 mention) - the report calls it "distal lower-limb weakness"; HP calls it **Distal lower limb muscle weakness**
- `HP:0003236` (2 mentions) - the report calls it "elevated serum CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:3097` - called "DYSF", "Ontology:** Gene *DYSF"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.