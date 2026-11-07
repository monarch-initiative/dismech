---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T11:33:20.041519'
end_time: '2026-11-07T12:03:51.285889'
duration_seconds: 1831.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypotonia, Ataxia, and Delayed Development Syndrome
  mondo_id: MONDO:0015021
  category: Mendelian
  causal_genes: EBF3
  omim_id: OMIM:617330
  synonyms: hypotonia, ataxia, and delayed development syndrome; HADDS; EBF3 neurodevelopmental
    disorder; HADDS; developmental delay-ataxia-hypotonia-facial dysmorphism syndrome
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
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 13
  validator_version: 0.5.1
term_validation:
  total_terms: 28
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 17
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: EBF3-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: EBF3-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia, Ataxia, and Delayed Development Syndrome
- **MONDO ID:** MONDO:0015021 (if available)
- **Causal gene(s):** EBF3
- **OMIM:** OMIM:617330
- **Synonyms:** hypotonia, ataxia, and delayed development syndrome; HADDS; EBF3 neurodevelopmental disorder; HADDS; developmental delay-ataxia-hypotonia-facial dysmorphism syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypotonia, Ataxia, and Delayed Development Syndrome** covering all of the
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

# Hypotonia, Ataxia, and Delayed Development Syndrome (HADDS): A Comprehensive Disease Characterization

**Disease:** Hypotonia, Ataxia, and Delayed Development Syndrome (HADDS)
**Causal gene:** *EBF3* (Early B-cell Factor 3; HGNC:19087; gene MIM 607407)
**Identifiers:** MONDO:0015021 · OMIM:617330 · Orphanet:658843
**Category:** Mendelian, autosomal dominant neurodevelopmental disorder

---

## Summary

Hypotonia, Ataxia, and Delayed Development Syndrome (HADDS) is a rare, autosomal-dominant neurodevelopmental disorder caused by **heterozygous loss-of-function of *EBF3***, a highly conserved Collier/Olf/EBF (COE) family transcription factor located at chromosome 10q26.3. The disorder was defined simultaneously by three independent whole-exome sequencing studies in 2017, which identified *de novo* missense, nonsense, frameshift, splice-site, and in-frame duplication variants, as well as whole-gene deletions, in individuals with a recognizable syndrome of congenital hypotonia, ataxia, global developmental delay, expressive speech impairment, facial dysmorphism, and genitourinary dysfunction. The unifying molecular mechanism is **haploinsufficiency**: most pathogenic variants reduce the dosage of functional EBF3 protein, and the fact that complete EBF3 deletion (via a 10q26.3 microdeletion) reproduces the phenotype confirms that one functional copy of the gene is insufficient for normal neurodevelopment.

Mechanistically, EBF3 is a dosage-sensitive transcription factor (gnomAD pLI ≈ 1.00; LOEUF upper bound 0.346) that binds DNA through a zinc-knuckle/zinc-finger (ZNF) motif and activates transcription of target genes. Pathogenic missense variants cluster in the DNA-binding domain (recurrent residues Arg163 and Arg209), where they impair DNA binding, cause cytoplasmic mislocalization, and abolish transcriptional activation of reporter genes such as *CDKN1A*. During brain development, EBF3 acts downstream of the homeobox selector gene *ARX* and within a *Prdm8–EBF3–NeuroD1* axis to control neuronal migration and the multipolar-to-bipolar transition of migrating neurons; disruption of this program is the inferred cause of the cerebellar malformation (vermis hypoplasia with a characteristic radial "dandelion-sign" foliation) and the cortical/white-matter abnormalities seen on imaging.

Clinically, HADDS is lifelong and largely static, with **highly variable expressivity** — developmental delay is the only near-universal feature, while ataxia, abnormal muscle tone, and MRI abnormalities each occur in roughly a third to two-thirds of patients, and rare individuals have normal IQ. Severity correlates with the location of missense variants: those perturbing the zinc-finger domain define a high-risk subtype. There is **no disease-specific or disease-modifying therapy**; management is entirely supportive and multidisciplinary (physical, occupational, and speech therapy; aggressive surveillance and treatment of neurogenic bladder to protect renal function; ophthalmologic management of strabismus; developmental and educational support). The disorder is ultra-rare, known only from small case series and one observational registry.

---

## Key Findings

### Finding 1 — HADDS is caused by heterozygous loss-of-function of *EBF3* via haploinsufficiency

Three independent 2017 exome studies established that *de novo* variants in *EBF3* — spanning missense, nonsense, frameshift, splice-site, and a 9-bp duplication — cause a syndromic neurodevelopmental disorder. The variants are predicted to trigger nonsense-mediated mRNA decay (NMD) and reduce functional protein dosage. Critically, complete deletion of *EBF3* within a 10q26.3 microdeletion reproduces the HADDS phenotype, which is the strongest line of evidence that the mechanism is **haploinsufficiency** rather than a dominant-negative or gain-of-function effect.

As stated in the clinical-spectrum review, *"EBF3 pathogenic variants have been predicted to result in nonsense-mediated mRNA decay and haploinsufficiency"* and *"total deletion of EBF3 associated with a 10q26.3 microdeletion also causes HADDS symptoms, supporting the concept that HADDS results from haploinsufficiency of EBF3"* ([PMID: 34050706](https://pubmed.ncbi.nlm.nih.gov/34050706/)). The founding report described *"de novo variants in EBF3"* as the cause ([PMID: 28017372](https://pubmed.ncbi.nlm.nih.gov/28017372/)).

**Evidence type:** human clinical (exome sequencing, cohort studies).

### Finding 2 — EBF3 missense variants in the DNA-binding zinc-knuckle impair transcriptional activation

In vitro functional assays in HEK293T cells demonstrated that EBF3 mutant proteins have significantly reduced or absent ability to activate transcription of the reporter gene *CDKN1A*. Most mutants mislocalized to the cytoplasm and were less tightly associated with chromatin, and genome-wide RNA-seq and ChIP-seq showed reduced DNA binding and gene-regulatory activity. The recurrent *de novo* variants affect a single conserved residue in a zinc finger motif that is crucial for DNA binding, and these variants are deleterious in a *Drosophila* model.

Direct quotes: *"By transactivation assays, all EBF3 mutants showed significantly reduced or no ability to activate transcription of the reporter gene CDKN1A"* and *"mutant EBF3 had reduced genome-wide DNA binding and gene-regulatory activity"* ([PMID: 28017373](https://pubmed.ncbi.nlm.nih.gov/28017373/)). The founding study noted that *"the de novo variants affect a single conserved residue in a zinc finger motif crucial for DNA binding and are deleterious in a fly model"* ([PMID: 28017372](https://pubmed.ncbi.nlm.nih.gov/28017372/)).

**Evidence type:** in vitro (cell-based transactivation, RNA-seq, ChIP-seq) and in vivo model organism (*Drosophila*).

### Finding 3 — Neurogenic bladder / urologic dysfunction is a frequent, early feature

Genitourinary involvement is a distinctive and clinically important feature of HADDS. In a 52-patient aggregate series (33 female : 19 male), 67% had a urologic diagnosis, with a high prevalence of urinary tract infection, vesicoureteral reflux (VUR), and neurogenic bladder, and females disproportionately affected. In a separate 8-patient series, neurogenic bladder was diagnosed in infancy (median 6.5 months) and required cystostomy in all but one case. The proposed mechanism is impaired relaxation of the urinary sphincter producing detrusor-sphincter dyssynergia.

As stated: *"We hypothesize a high rate of bladder dysfunction secondary to the EBF3 variant's impact on relaxation of the urinary sphincter leading to detrusor sphincter dyssynergia (DSD)"* ([PMID: 37718233](https://pubmed.ncbi.nlm.nih.gov/37718233/)), and *"neurogenic bladder was diagnosed in infancy (the median 6.5 months), was more frequent than previously reported, and required cystostomy in all but one case"* ([PMID: 34050706](https://pubmed.ncbi.nlm.nih.gov/34050706/)).

**Suggested HPO terms:** HP:0000011 (Neurogenic bladder), HP:0000076 (Vesicoureteral reflux), HP:0000010 (Recurrent urinary tract infections).

**Evidence type:** human clinical (retrospective cohort and case series).

### Finding 4 — Cerebellar vermis hypoplasia with a radial "dandelion-sign" foliation is a characteristic neuroimaging feature

In a 6-patient neuroimaging series (2 female : 4 male, ages 2–12), developmental milestones were invariably delayed, all patients showed ataxic signs confirmed by SARA (Scale for the Assessment and Rating of Ataxia) scores — often with hypotonia — and brain MRI in all children revealed a cerebellar malformation with vermis hypoplasia and a peculiar foliation anomaly characterized by radial disposition of the cerebellar folia (the **"dandelion sign"**). Neurophysiologic examinations (EEG, evoked potentials) were unremarkable.

Direct quotes: *"Brain MRI revealed in all children a cerebellar malformation with vermis hypoplasia and a peculiar foliation anomaly characterized by a radial disposition of cerebellar folia (dandelion sign)"* and *"All patients showed ataxic signs, as confirmed by SARA scores, often associated with hypotonia"* ([PMID: 37090941](https://pubmed.ncbi.nlm.nih.gov/37090941/)).

**Suggested HPO terms:** HP:0001320 (Cerebellar vermis hypoplasia), HP:0001251 (Ataxia), HP:0001252 (Hypotonia), HP:0002194 (Delayed gross motor development).

**Evidence type:** human clinical (neuroimaging case series).

### Finding 5 — Autosomal dominant, usually *de novo*, with documented parental mosaicism affecting recurrence risk

Across the 2017 cohorts, *EBF3* variants arose *de novo* in the majority of cases (e.g., 8 of 10 individuals in the Harms et al. series). Importantly, the missense variant c.625C>T (p.Arg209Trp) was inherited by two affected siblings from their clinically healthy, mosaic mother — direct evidence of germline/somatic mosaicism with a nonzero recurrence risk for apparently unaffected parents. Recurrent substitutions cluster at DNA-binding residues (e.g., Arg163, Arg209); an independent case confirmed a *de novo* c.625G>A (p.Arg209Trp) variant impairing DNA binding, localization, and transactivation.

Direct quotes: *"the missense variant c.625C>T (p.Arg209Trp) was inherited by two affected siblings from their healthy mother, who is mosaic"* ([PMID: 28017373](https://pubmed.ncbi.nlm.nih.gov/28017373/)); *"a de novo heterozygous c.625G>A (p.Arg209Trp) variant of the EBF3 gene"* ([PMID: 36317217](https://pubmed.ncbi.nlm.nih.gov/36317217/)).

**Evidence type:** human clinical (segregation and mosaicism analysis).

### Finding 6 — Missense variants disrupting the zinc-finger (ZNF) domain define a high-severity genotype–phenotype subtype

An integrated phenotypic/genotypic study of 41 individuals, combined with a literature meta-analysis (total n = 83 with EBF3-related neurodevelopmental disorder) using quantitative severity scales, found that patient symptom severity correlates with missense variants perturbing the zinc-finger (ZNF) domain, which stabilizes the EBF3–DNA interaction. In vivo *Drosophila* UAS-GAL4 rescue experiments and in vitro luciferase assays showed that ZNF-associated variants failed to restore viability and impaired transcriptional activation, whereas the recurrent DNA-binding-domain variant p.Arg209Trp partially rescued fly viability and preserved some function — providing a mechanistic basis for the severity gradient.

Direct quotes: *"patient symptom severity correlates with EBF3 missense variants perturbing the ZNF, which is a key protein domain required for stabilizing the interaction between EBF3 and the target DNA sequence"* and *"ZNF-associated variants failed to restore viability in the fruit fly and impaired transcriptional activation"* ([PMID: 35340043](https://pubmed.ncbi.nlm.nih.gov/35340043/)).

**Evidence type:** human clinical (genotype–phenotype correlation) plus in vivo/in vitro functional validation.

### Finding 7 — *De novo* noncoding regulatory (enhancer hs737) variants also implicate *EBF3* in autism

Whole-genome sequencing of 2,671 autism families (discovery cohort 516, replication 2,155) identified an excess of *de novo* variants in the brain-active enhancer **hs737** (discovery p = 0.0172; significant replication), which targets *EBF3* — a gene that is genome-wide significant in neurodevelopmental disorders. This demonstrates that *EBF3* dysregulation can arise through both coding and noncoding *de novo* variation, broadening the mutational spectrum relevant to the EBF3 phenotypic continuum.

Direct quotes: *"we identify DNVs in the hs737 enhancer in individuals with autism"* and *"we find hs737 targets the gene EBF3 that is genome-wide significant in NDDs"* ([PMID: 34256850](https://pubmed.ncbi.nlm.nih.gov/34256850/)).

**Evidence type:** human clinical (whole-genome sequencing, enhancer burden analysis).

### Finding 8 — *EBF3* is a highly constrained, dosage-sensitive gene (gnomAD), corroborating haploinsufficiency

gnomAD v2.1.1 constraint metrics for *EBF3* (ENSG00000108001; chr10:129,835,233–129,973,053, minus strand) strongly support intolerance to loss of function:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.00 (0.99999) | Extreme intolerance to LoF |
| Observed/expected LoF | 0.233 (18 obs vs 77.1 exp) | ~77% fewer LoF variants than expected |
| LOEUF (upper bound) | 0.346 | Below the 0.35 haploinsufficiency threshold |
| LoF Z | 5.71 | Strong constraint |
| Missense Z | 4.39 (oe_mis = 0.65) | Missense constraint |
| Synonymous Z | −0.21 | Neutral (as expected) |

Identifiers: HGNC:19087; gene MIM 607407; aliases COE3, O/E-2, HADDS. The genic constraint provides an orthogonal, population-genetics line of evidence that a single functional copy of *EBF3* is insufficient.

**Evidence type:** computational / population genetics (gnomAD).

### Finding 9 — ClinVar catalogs hundreds of *EBF3* variants, including ~230 pathogenic/likely pathogenic

A ClinVar query (2026-11) returned 528 *EBF3* variant records total, of which 162 are classified Pathogenic and 68 Likely pathogenic (~230 P/LP); 414 records are single-nucleotide variants. Pathogenic variant classes span missense (clustering in the DNA-binding/zinc-finger domain), nonsense, frameshift, and splice-site changes, plus whole-gene deletions (10q26.3). Recurrent residues include Arg163 and Arg209 in the DNA-binding domain.

| Variant class | Representative examples | Functional consequence |
|---|---|---|
| Missense (DNA-binding/ZNF) | p.Arg163Gly, p.Arg163Leu, p.Arg209Trp, p.Arg152Cys, p.Phe211Leu | Loss of DNA binding, mislocalization, loss of transactivation |
| Nonsense | p.Arg470* (C-terminal), p.Tyr321* | Truncation / NMD → haploinsufficiency |
| Frameshift | Various | NMD → haploinsufficiency |
| Splice-site | Various | Aberrant splicing → LoF |
| Whole-gene deletion | 10q26.3 microdeletion | Null allele (phenocopy) |

**Evidence type:** curated variant database (ClinVar).

### Finding 10 — Highly variable expressivity, including normal-IQ cases; developmental delay is the only near-universal feature

In a 12-patient Chinese cohort (5 missense + 7 CNVs), developmental delay/intellectual disability was present in 100%, but ataxia in only 33% (6/9), abnormal muscle tone in 55% (6/11), and aberrant brain MRI in 64% (7/11). Novel missense variants localized to the DNA-binding domain (R152C and F211L altered subcellular localization; R163G shifted distribution to a granular pattern). Separately, two unrelated patients with *de novo* variants (p.Arg152Leu; p.Tyr321*) had IQ in the normal range, demonstrating that EBF3-related neurodevelopmental disorder can occur **without** intellectual disability; diffusion tensor imaging showed asymmetric longitudinal fasciculus (white-matter long-tract) abnormalities.

Direct quotes: *"All of these patients exhibited developmental delay/intellectual disability. Ataxia was observed in 33% (6/9) of the patients, and abnormal muscle tone was observed in 55% (6/11) of the patients. Aberrant MRI reports were noted in 64% (7/11) of the patients"* ([PMID: 36937983](https://pubmed.ncbi.nlm.nih.gov/36937983/)); *"Our results demonstrate that EBF3 mutations can underlie neurodevelopmental disorders without intellectual disability"* ([PMID: 34177436](https://pubmed.ncbi.nlm.nih.gov/34177436/)).

| Phenotype | Frequency (12-pt cohort) | Suggested HPO term |
|---|---|---|
| Developmental delay / intellectual disability | 100% | HP:0001263 / HP:0001249 |
| Abnormal muscle tone (hypotonia) | 55% (6/11) | HP:0001252 |
| Aberrant brain MRI | 64% (7/11) | HP:0002060 |
| Ataxia | 33% (6/9) | HP:0001251 |

**Evidence type:** human clinical (cohort with quantitative frequencies).

### Finding 11 — *EBF3* is a dosage-sensitive regulator of neuronal migration acting downstream of *ARX* and within a Prdm8–EBF3–NeuroD1 axis

Developmental neurobiology studies in mouse and in vitro place EBF3 in a defined gene-regulatory hierarchy controlling neuronal migration:

- *Ebf2* and *Ebf3*, singly or together, control the migration of Cajal–Retzius cells arising from the cortical hem ([PMID: 22421355](https://pubmed.ncbi.nlm.nih.gov/22421355/)): *"both Ebf2 and Ebf3, singly or together, control the migration of CR cells arising in the cortical hem."*
- The homeobox selector gene *Arx* directly represses *Ebf3*; ectopic *Ebf3* expression in the ventral telencephalon prevents neuronal tangential migration, and silencing *Ebf3* in *Arx*-mutant tissue partially rescues tangential cell movement ([PMID: 19627984](https://pubmed.ncbi.nlm.nih.gov/19627984/): *"its ectopic expression in ventral telencephalon was found to prevent neuronal tangential migration"*; *"Arx is sufficient to repress Ebf3 endogenous expression"*; see also [PMID: 18799476](https://pubmed.ncbi.nlm.nih.gov/18799476/)).
- *Ebf3* is a *Prdm8* target that drives the multipolar-to-bipolar transition of migrating neocortical neurons via positive feedback on *NeuroD1* ([PMID: 29113800](https://pubmed.ncbi.nlm.nih.gov/29113800/): *"Ebf3 is a key regulator of neuronal migration via multipolar-to-bipolar transition"*).

This hierarchy explains the phenotypic overlap between EBF3 and ARX disorders and links reduced EBF3 dosage to defective cortical and cerebellar neuronal migration — the inferred substrate for the ataxia, hypotonia, developmental delay, and the dandelion-sign cerebellar malformation.

**Evidence type:** model organism (mouse) and in vitro developmental biology.

### Finding 12 — No disease-specific therapy exists; management is supportive; the disorder is ultra-rare

A ClinicalTrials.gov query (2026-11) returned no interventional/therapeutic trial specific to *EBF3* or HADDS; the only EBF3-tagged study is the observational Simons Searchlight registry (NCT01238250), which lists *EBF3* among >150 neurodevelopmental genes. HADDS is ultra-rare — the reported literature comprises small case series (first described in 2017; the largest aggregate review assembled 52 patients, [PMID: 37718233](https://pubmed.ncbi.nlm.nih.gov/37718233/): *"We identified 52 patients (33F:19M) through literature (28F:18M) and retrospective review (5F:1M)"*) — and no formal prevalence/incidence estimate is published (Orphanet:658843). Reported management across series is multidisciplinary supportive care: physical/occupational/speech therapy; treatment of neurogenic bladder (clean intermittent catheterization/cystostomy, surveillance for VUR/UTI and renal protection); ophthalmologic management of strabismus; and developmental/educational support.

**Evidence type:** clinical trial registry, case-series synthesis.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function lesion in *EBF3*** arises — most often *de novo* (missense in the DNA-binding/ZNF domain, nonsense, frameshift, splice-site), or as a whole-gene 10q26.3 deletion, or (rarely) a noncoding enhancer hs737 variant. *This leads to →*
2. **Reduced dosage of functional EBF3 protein** (haploinsufficiency). Truncating alleles trigger nonsense-mediated decay; missense alleles in the zinc-knuckle impair folding/DNA contact. *This results in →*
3. **Impaired EBF3 DNA binding and transcriptional activation.** Mutant EBF3 shows reduced/absent transactivation of targets (e.g., *CDKN1A*), cytoplasmic mislocalization, weaker chromatin association, and genome-wide loss of binding. *This leads to →*
4. **Dysregulation of EBF3-dependent neurodevelopmental gene programs.** EBF3 normally acts downstream of *ARX* and within a *Prdm8 → EBF3 → NeuroD1* feedback loop. Loss of EBF3 output disrupts the multipolar-to-bipolar transition and tangential/radial migration of cortical and Cajal–Retzius neurons. *This results in →*
5. **Abnormal neuronal migration and cerebellar/cortical patterning** — inferred to produce cerebellar vermis hypoplasia with radial "dandelion-sign" foliation and white-matter (longitudinal fasciculus) abnormalities. *This leads to →*
6. **Clinical manifestations:** congenital hypotonia, ataxia, global developmental delay with prominent expressive-speech impairment, intellectual disability (variable), facial dysmorphism, strabismus, and neurogenic bladder (via inferred detrusor-sphincter dyssynergia).

**Branch point:** severity tracks with **where** the missense variant falls — ZNF-domain variants (which destabilize the EBF3–DNA interaction) define a high-severity subtype, whereas certain DNA-binding-domain variants such as p.Arg209Trp retain partial function and are associated with milder outcomes, including rare normal-IQ cases.

```
 EBF3 LoF variant (de novo missense/nonsense/frameshift/splice,
 10q26.3 deletion, or hs737 enhancer DNV)
            │  haploinsufficiency (NMD / impaired protein)
            ▼
 ↓ functional EBF3 dosage
            │  impaired DNA binding + cytoplasmic mislocalization
            ▼
 ↓ transcriptional activation of EBF3 targets (e.g. CDKN1A)
            │  within ARX ⊣ EBF3  and  Prdm8 → EBF3 → NeuroD1 axes
            ▼
 defective neuronal migration / multipolar→bipolar transition
            │
   ┌────────┴─────────────────────────┐
   ▼                                   ▼
 cerebellar vermis hypoplasia      cortical / white-matter
 ("dandelion sign")                migration defects
   │                                   │
   ▼                                   ▼
 ataxia, hypotonia              developmental delay, ID (variable),
                                speech impairment, dysmorphism,
                                strabismus, neurogenic bladder
```

### Ontology annotations

- **Gene/protein:** *EBF3* (HGNC:19087), COE-family DNA-binding transcription factor.
- **GO biological process:** GO:0001764 (neuron migration), GO:0021954 (central nervous system neuron development), GO:0045944 (positive regulation of transcription by RNA Pol II), GO:0006357 (regulation of transcription by RNA Pol II).
- **GO cellular component:** GO:0005634 (nucleus), GO:0000785 (chromatin); mutants aberrantly in GO:0005737 (cytoplasm).
- **Cell types (CL):** CL:0000099 (interneuron), CL:0012001 (neuron of the cerebral cortex), Cajal–Retzius cell, cerebellar neurons.
- **Anatomy (UBERON):** UBERON:0004720 (cerebellar vermis), UBERON:0002037 (cerebellum), UBERON:0000955 (brain), UBERON:0001255 (urinary bladder).
- **Disease (MONDO):** MONDO:0015021.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [28017372](https://pubmed.ncbi.nlm.nih.gov/28017372/) | *A Syndromic NDD Caused by De Novo Variants in EBF3* | Human clinical + fly | Founding paper; de novo variants, ZNF localization (F001, F002) |
| [28017373](https://pubmed.ncbi.nlm.nih.gov/28017373/) | *Mutations in EBF3 Disturb Transcriptional Profiles...* | In vitro + human | Transactivation/ChIP-seq loss; mosaic inheritance (F002, F005) |
| [29162653](https://pubmed.ncbi.nlm.nih.gov/29162653/) | *De novo variants in EBF3* | Human clinical | Core phenotype delineation (hypotonia, ataxia, dysmorphism) |
| [34050706](https://pubmed.ncbi.nlm.nih.gov/34050706/) | *Clinical spectrum of EBF3 variants/deletions* | Human clinical | Haploinsufficiency; deletion phenocopy; early neurogenic bladder (F001, F003) |
| [37718233](https://pubmed.ncbi.nlm.nih.gov/37718233/) | *Urologic manifestations of HADDS* | Human clinical | 52-patient series; DSD mechanism; ultra-rarity (F003, F012) |
| [37090941](https://pubmed.ncbi.nlm.nih.gov/37090941/) | *Neurologic/neuroradiologic features* | Human clinical | Dandelion-sign cerebellar malformation; SARA ataxia (F004) |
| [36317217](https://pubmed.ncbi.nlm.nih.gov/36317217/) | *Clinical features and EBF3 variant in a child* | Human clinical | Recurrent p.Arg209Trp, de novo (F005) |
| [35340043](https://pubmed.ncbi.nlm.nih.gov/35340043/) | *High-risk subtype for ZNF-domain missense* | Human + fly/luciferase | ZNF severity genotype–phenotype (F006) |
| [34256850](https://pubmed.ncbi.nlm.nih.gov/34256850/) | *Coding and noncoding variants in EBF3* | Human WGS | Enhancer hs737 DNVs in autism (F007) |
| [36937983](https://pubmed.ncbi.nlm.nih.gov/36937983/) | *EBF3-related NDD in 12 Chinese patients* | Human clinical | Phenotype frequencies; variable expressivity (F010) |
| [34177436](https://pubmed.ncbi.nlm.nih.gov/34177436/) | *Neuroimaging findings in EBF3-NDD* | Human clinical | Normal-IQ cases; DTI white-matter asymmetry (F010) |
| [40073166](https://pubmed.ncbi.nlm.nih.gov/40073166/) | *Nonsense variant in C-terminal transactivation domain* | Human clinical | C-terminal truncation; behavioral phenotype expansion |
| [22421355](https://pubmed.ncbi.nlm.nih.gov/22421355/) | *EBF2/3 regulate Cajal–Retzius migration* | Mouse | Migration role (F011) |
| [19627984](https://pubmed.ncbi.nlm.nih.gov/19627984/) | *Arx as regional key selector gene* | Mouse | ARX represses EBF3; tangential migration (F011) |
| [18799476](https://pubmed.ncbi.nlm.nih.gov/18799476/) | *Arx transcriptional targets in basal forebrain* | Mouse | EBF3 a direct ARX target (F011) |
| [29113800](https://pubmed.ncbi.nlm.nih.gov/29113800/) | *Prdm8 target Ebf3 regulates multipolar-to-bipolar transition* | Mouse/in vitro | Prdm8–EBF3–NeuroD1 axis (F011) |
| [42711312](https://pubmed.ncbi.nlm.nih.gov/42711312/) | *Non-cell-autonomous roles for UNC-3/EBF* | *C. elegans* | Ortholog circuit-level mechanism; CEBP-1 driver |
| [42182317](https://pubmed.ncbi.nlm.nih.gov/42182317/) | *Negative autoregulation of dosage-sensitive TF* | *C. elegans* | EBF/UNC-3 dosage sensitivity concept (supports F008) |

**Consistency across the evidence base:** The haploinsufficiency model (F001, F008) is supported convergently by human genetics (deletion phenocopy), population constraint (pLI ≈ 1), and in vitro loss of function (F002). The migration mechanism (F011) is drawn entirely from model-organism work and is therefore an *inferred* explanation for the human imaging phenotype rather than a directly demonstrated human mechanism. No contradicting evidence was identified; the main tension is the breadth of expressivity (F010), which the ZNF-severity model (F006) partially reconciles.

---

## Section-by-Section Characterization

**1. Disease Information.** HADDS (MONDO:0015021; OMIM:617330; Orphanet:658843) is an autosomal-dominant neurodevelopmental disorder caused by *EBF3*. Synonyms: HADDS; EBF3 neurodevelopmental disorder; developmental delay–ataxia–hypotonia–facial dysmorphism syndrome. No dedicated ICD-10/11 or MeSH code; it maps to generic neurodevelopmental/cerebellar categories. Information is derived from aggregated disease-level resources and small patient case series, not large EHR datasets.

**2. Etiology.** Primary cause is genetic — heterozygous LoF variants in *EBF3* (germline, usually *de novo*; rarely transmitted via parental mosaicism). No environmental, infectious, or lifestyle causes are known. The only recognized recurrence-risk modifier is parental germline/somatic mosaicism (F005). No protective alleles or gene–environment interactions are established.

**3. Phenotypes.** Near-universal: global developmental delay (HP:0001263) with expressive-speech impairment. Common: hypotonia (HP:0001252), ataxia (HP:0001251), intellectual disability (HP:0001249, variable), facial dysmorphism, strabismus (HP:0000486), neurogenic bladder (HP:0000011), cerebellar vermis hypoplasia (HP:0001320). Onset is congenital/neonatal; course is largely static; severity is variable (F006, F010). Quality-of-life impact is driven by mobility/communication impairment and urologic morbidity.

**4. Genetic/Molecular.** Causal gene *EBF3* (HGNC:19087, gene MIM 607407, chr10q26.3). ~230 P/LP ClinVar records; recurrent DNA-binding residues Arg163 and Arg209; variant classes include missense, nonsense, frameshift, splice, and whole-gene deletion (F009). Functional consequence: loss of function/haploinsufficiency (F001, F002, F008). No established modifier genes beyond the ZNF-domain positional effect; no disease-specific epigenetic mechanism reported.

**5. Environmental.** Not applicable — HADDS is a monogenic disorder with no known environmental, lifestyle, or infectious contributors.

**6. Mechanism/Pathophysiology.** See the causal chain above (F001–F002, F008, F011).

**7. Anatomical Structures.** Primary: central nervous system — cerebellum/vermis (UBERON:0004720), cerebral cortex, white-matter long tracts. Secondary: urinary bladder (UBERON:0001255) and upper urinary tract (via VUR/neurogenic bladder); eyes (strabismus). Subcellular: nucleus/chromatin (normal EBF3 localization) with pathologic cytoplasmic mislocalization of mutants.

**8. Temporal Development.** Congenital onset; insidious recognition in infancy. Static/non-progressive neurodevelopmental course (lifelong). Neurogenic bladder presents early (median 6.5 months). Critical period is early neurodevelopment; the main intervention window is early supportive/rehabilitative therapy and renal-protective urologic surveillance.

**9. Inheritance and Population.** Autosomal dominant; mostly *de novo*; incomplete reporting of penetrance but highly variable expressivity. No formal prevalence/incidence (ultra-rare). Female predominance in ascertained urologic cohorts (33F:19M) likely reflects ascertainment and the urologic phenotype rather than a true sex bias. Parental mosaicism documented; no founder effects or consanguinity role established.

**10. Diagnostics.** Molecular diagnosis via exome/genome sequencing, NDD gene panels including *EBF3*, single-gene testing, or chromosomal microarray (detects 10q26.3 deletions). Brain MRI (cerebellar vermis hypoplasia, dandelion-sign foliation) and SARA ataxia scoring support the clinical picture; urodynamic/renal imaging for bladder dysfunction. Differential diagnoses include other congenital ataxias/cerebellar hypoplasias, ARX-related disorders, and 10q26 deletion/ring-chromosome-10 syndromes.

**11. Outcome/Prognosis.** Lifelong disability with static course; no reported reduction in survival from the neurodevelopmental phenotype itself, though neurogenic bladder poses a risk of renal complications if unmanaged. Prognostic factor: ZNF-domain missense variants predict greater severity. No validated prognostic biomarkers.

**12. Treatment.** No disease-modifying therapy. Supportive/rehabilitative care: physical, occupational, and speech therapy; clean intermittent catheterization or cystostomy and VUR/UTI surveillance for neurogenic bladder; ophthalmologic management of strabismus; educational support. Suggested NCIT terms: physical therapy, occupational therapy, speech therapy, intermittent catheterization.

**13. Prevention.** No primary prevention. Secondary/tertiary measures are genetic counseling (recognizing mosaicism-related recurrence risk), prenatal/preimplantation testing for known familial variants, and proactive renal-protective urologic surveillance to prevent complications.

**14. Other Species / Natural Disease.** Orthologs: mouse *Ebf3*, *C. elegans unc-3*, *Drosophila knot/collier*-family. No naturally occurring companion-animal disease is cataloged; relevance is as experimental models. Mechanisms are evolutionarily conserved (migration, dosage-sensitive terminal-selector function).

**15. Model Organisms.** *Drosophila* (UAS-GAL4 rescue assays demonstrating variant deleteriousness and ZNF severity), mouse (*Ebf3*/*Ebf2* migration studies, Prdm8–EBF3–NeuroD1 axis), and *C. elegans* (*unc-3* dosage-sensitivity and non-cell-autonomous circuit roles). Models recapitulate the transcription-factor loss-of-function and neuronal-migration phenotypes but do not fully reproduce the human cerebellar/urologic clinical syndrome.

---

## Limitations and Knowledge Gaps

1. **Mechanism is largely inferred for humans.** The neuronal-migration causal chain (F011) rests on mouse and invertebrate data; the direct link between EBF3 haploinsufficiency and the human dandelion-sign cerebellar malformation has not been demonstrated at the tissue level in patients.
2. **No epidemiology.** No prevalence or incidence estimate exists (Orphanet:658843); the total reported literature is a few hundred patients at most, limiting frequency estimates for individual phenotypes.
3. **Ascertainment bias.** Female predominance and the high urologic burden derive from cohorts partly ascertained through urology clinics; true population sex ratio and penetrance of each feature are uncertain.
4. **Genotype–phenotype resolution is incomplete.** The ZNF-severity correlation (F006) is robust but does not explain normal-IQ outliers (F010) or the full spectrum; C-terminal transactivation-domain variants are under-characterized.
5. **No therapeutics.** There are no interventional trials, no biomarkers of progression, and no validated outcome measures beyond SARA for ataxia.
6. **Epigenetic, metabolomic, and proteomic data are absent** for this disorder specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Human neuropathology/imaging correlation.** Systematic volumetric MRI and, where available, neuropathologic study to directly test whether the dandelion-sign malformation reflects the migration defect predicted by mouse models.
2. **Variant-function atlas.** Deep mutational scanning of *EBF3* across DNA-binding, ZNF, and transactivation domains with transactivation/localization readouts to build a quantitative severity map and reclassify variants of uncertain significance.
3. **Prospective natural-history registry.** Expand the Simons Searchlight (NCT01238250) EBF3 cohort with standardized developmental, ataxia (SARA), and urodynamic assessments to establish phenotype frequencies, penetrance, and progression.
4. **Urologic mechanism study.** Test the detrusor-sphincter-dyssynergia hypothesis directly with urodynamics in a defined EBF3 cohort and correlate with variant type.
5. **Dosage-restoration proof of concept.** Given the haploinsufficiency mechanism and extreme constraint, evaluate dosage-upregulation strategies (e.g., ASO-mediated or CRISPR-activation of the wild-type allele, enhancer hs737 targeting) in neuronal/organoid models.
6. **iPSC and brain-organoid models** from patients carrying ZNF-domain vs DNA-binding vs truncating variants to resolve genotype-specific cellular phenotypes and screen candidate modifiers.

---

*Report compiled from 12 confirmed findings and 27 reviewed papers over 5 investigation iterations. Evidence types are labeled per finding (human clinical, model organism, in vitro, computational). Causal-chain steps that rest on model-organism data are flagged as inferred.*


## Artifacts

- [OpenScientist final report](EBF3-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](EBF3-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 20 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045944` (1 mention) - the report calls it "positive regulation of transcription by RNA Pol II"; GO calls it **positive regulation of transcription by RNA polymerase II**
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `CL:0012001` (1 mention) - the report calls it "neuron of the cerebral cortex"; CL calls it **neuron of the forebrain**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:19087` - called "EBF3", "Gene/protein:** *EBF3"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`.

25 of 28 terms resolved to a current term; the rest could not be looked up either way.