---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T15:30:21.492364'
end_time: '2026-10-30T16:16:46.135351'
duration_seconds: 2784.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TPM4-related Platelet Disorder
  mondo_id: MONDO:0100487
  category: Mendelian
  causal_genes: TPM4
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001873
    reported_labels:
    - Laboratory abnormality
    ontology_label: Thrombocytopenia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TPM4-related_Platelet_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TPM4-related_Platelet_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TPM4-related Platelet Disorder
- **MONDO ID:** MONDO:0100487 (if available)
- **Causal gene(s):** TPM4
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

Please provide a comprehensive research report on **TPM4-related Platelet Disorder** covering all of the
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

# TPM4-related Platelet Disorder (MONDO:0100487) — Comprehensive Disease Characteristics Report

**Causal gene: _TPM4_ (tropomyosin 4; HGNC:12013; encoding the cytoskeletal/non-muscle tropomyosin isoform Tpm4.2).** This report concerns the autosomal dominant inherited macrothrombocytopenia caused by heterozygous variants in **TPM4**, not the muscle tropomyosinopathies caused by the related genes _TPM1_, _TPM2_, or _TPM3_. All content below pertains to the TPM4 platelet disorder.

---

## Summary

TPM4-related Platelet Disorder is a rare, **autosomal dominant inherited macrothrombocytopenia** caused by heterozygous loss-of-function (truncating) variants and rare deleterious missense variants in **TPM4**, the gene encoding the cytoskeletal (non-muscle) tropomyosin isoform **Tpm4.2**. The disorder was first defined as a Mendelian entity in 2017, when two unrelated families from the BRIDGE Bleeding and Platelet Disorders (BPD) collection were found to carry TPM4 truncating variants that segregated with low platelet counts and enlarged platelets ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)). The gene had previously been flagged through genome-wide association studies of platelet count and mean platelet volume in ~70,000 individuals, which was the lead that prompted the Mendelian search.

Mechanistically, TPM4 behaves as a **haploinsufficient** gene. A heterozygous truncating or deleterious missense variant reduces the amount of functional Tpm4.2 available to specify and stabilize the megakaryocyte actin cytoskeleton. Because Tpm4.2 binds F-actin with high affinity, competes with α-actinin, and regulates myosin and ADF/cofilin activity, its reduction destabilizes and mis-specifies actin–tropomyosin filaments. This impairs the **terminal stages of platelet production** (proplatelet formation and platelet release from megakaryocytes), yielding **fewer but larger platelets** — the defining macrothrombocytopenia — with a mild additional effect on platelet function. The mechanism is conserved: ENU-induced missense mutations and targeted inactivation of _Tpm4_ in mice reproduce a gene-dosage-dependent macrothrombocytopenia with otherwise normal blood counts ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).

Clinically, the phenotype is **mild and lifelong (non-progressive)**: mild-to-moderate thrombocytopenia, a high proportion of enlarged platelets on the blood film, and a mild mucocutaneous bleeding tendency. Standard platelet aggregation and granule secretion tests are frequently normal, so the condition is easily mistaken for immune thrombocytopenia (ITP) and **requires genetic testing (whole-exome sequencing or inherited-platelet-disorder gene panels) for a definitive diagnosis**. Missense-variant carriers (e.g., p.R182C, p.A183V) can display more prominent platelet-function defects and more significant bleeding. There is no disease-specific therapy; management is supportive (antifibrinolytics such as tranexamic acid, hormonal control of menorrhagia, desmopressin, and peri-procedural platelet support when needed).

---

## Key Findings

### Finding 1 — TPM4 truncating variants cause autosomal dominant macrothrombocytopenia

The disease-defining observation comes from Pleines et al. 2017, who identified **two unrelated families** in the BRIDGE-BPD collection carrying a TPM4 variant that truncates the TPM4 protein and **segregates with macrothrombocytopenia** — a disorder of low platelet count and enlarged platelets ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)). Direct quote: *"we have identified 2 unrelated families in the BRIDGE Bleeding and Platelet Disorders (BPD) collection who carry a TPM4 variant that causes truncation of the TPM4 protein and segregates with macrothrombocytopenia, a disorder characterized by low platelet count."*

Causality is reinforced by animal modeling in the same study: *"N-Ethyl-N-nitrosourea–induced (ENU-induced) missense mutations in Tpm4 or targeted inactivation of the Tpm4 locus led to gene dosage-dependent macrothrombocytopenia in mice"* — establishing both causation and a **gene-dosage (haploinsufficiency)** mechanism ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).

An independent Spanish pedigree later confirmed the entity: whole-exome sequencing revealed a **novel nonsense variant c.322C>T (p.Gln108\*)** in TPM4 (NM_003290.3) segregating in 5 family members with lifelong mild thrombocytopenia and enlarged platelets ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)). Quote: *"WES revealed a novel nonsense variant (c.322C>T; p.Gln108\*) in TPM4 (NM_003290.3), the gene encoding for tropomyosin-4 (TPM4)."* Together these three pedigrees (two in 2017, one in 2022) establish truncating/nonsense TPM4 variants as the cause of dominant macrothrombocytopenia in humans.

### Finding 2 — TPM4 deficiency impairs terminal platelet production and causes cytoskeletal/platelet-function defects

The core cellular defect is a failure of the **final steps of platelet manufacture**. In Pleines et al., *"Insufficient TPM4 expression in human and mouse megakaryocytes resulted in a defect in the terminal stages of platelet production and had a mild effect on platelet function"* ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).

Functional studies of the p.Gln108\* nonsense variant demonstrated a downstream cytoskeletal consequence: the variant *"led to impairment of platelet spreading capacity after stimulation with TRAP-6 and CRP, delocalization of TPM4 in activated platelets, and significantly reduced TPM4 levels"* ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)). The reduced protein level is direct evidence of haploinsufficiency, and the spreading/localization defects show impaired cytoskeletal remodeling in activated platelets.

Rare conserved **missense variants (p.R182C and p.A183V)** in 3 patients from 2 families extend the spectrum toward platelet dysfunction: these variants caused *"reduced platelet secretion, and aggregation and spreading defects suggesting that TPM4 missense variants impact platelet function and show a disordered pattern of tropo[myosin]"* ([PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)). Finally, the megakaryocyte partner protein **tropomodulin-3 (Tmod3)** associates with TM4/TPM4 and F-actin; its loss disrupts the demarcation membrane system and proplatelet formation, placing TPM4 within a defined actin-organizing module of platelet biogenesis ([PMID: 25964668](https://pubmed.ncbi.nlm.nih.gov/25964668/)).

### Finding 3 — TPM4 encodes a cytoskeletal (non-muscle) tropomyosin that specifies and stabilizes actin filaments

TPM4 is one of **four vertebrate tropomyosin genes (TPM1–TPM4)**, from which more than 40 isoforms arise through alternative splicing and alternative promoters ([PMID: 28101865](https://pubmed.ncbi.nlm.nih.gov/28101865/); [PMID: 28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/)). The relevant product in platelets/megakaryocytes is the cytoskeletal isoform **Tpm4.2**, a stress-fiber-associated tropomyosin. In vitro reconstitution showed that these cytoskeletal tropomyosins *"bound F-actin with high affinity and competed with α-actinin for actin filament binding"* ([PMID: 28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/)), and that they regulate myosin activity and protect filaments from ADF/cofilin-mediated severing.

At the conceptual level, *"Tropomyosin can be viewed as a universal regulator of the actin cytoskeleton that specifies actin filaments for cellular and intracellular functions"* ([PMID: 28101865](https://pubmed.ncbi.nlm.nih.gov/28101865/)). In the specific context of megakaryocytes, Tmod3 *"associates with TM4 and the F-actin cytoskeleton in wild-type MKs"*, and confocal microscopy shows Tmod3, TM4, and F-actin partially co-localizing near proplatelet buds ([PMID: 25964668](https://pubmed.ncbi.nlm.nih.gov/25964668/)). This provides the molecular rationale for why reducing Tpm4.2 destabilizes the actin cytoskeleton that drives proplatelet formation.

### Finding 4 — The disorder is a mild, lifelong autosomal dominant macrothrombocytopenia with low bleeding burden

Across the three reported pedigrees the clinical picture is consistent: **lifelong mild-to-moderate thrombocytopenia, a high number of enlarged platelets on blood film, and a mild mucocutaneous bleeding tendency**. In the Spanish family, *"Five family members displayed lifelong mild thrombocytopenia with a high number of enlarged platelets in blood film, and mild bleeding tendency. Patient's platelets showed normal aggregation and granule secretion response to several agonists"* ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)) — emphasizing that standard functional tests can be normal.

The more severe end of the spectrum is seen with missense alleles: *"rare conserved missense variants (p.R182C and p.A183V) in TPM4 encoding tro[po]myosin-4 in 3 patients"* were associated with platelet dysfunction and excessive bleeding ([PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)). The TPM4 platelet-count/volume signal was first detected by GWAS in ~70,000 individuals ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)), and the disorder is diagnosed within the framework of gene panels/WES for inherited platelet disorders ([PMID: 19408193](https://pubmed.ncbi.nlm.nih.gov/19408193/) for the general diagnostic paradigm).

### Finding 5 — Consolidated causal chain: TPM4 haploinsufficiency → macrothrombocytopenia

Integrating all evidence yields a stepwise mechanism from mutation to clinical phenotype (detailed in the Mechanistic Model below). The conserved, nonredundant role of TPM4 across species is captured by the original paper's conclusion of *"a nonredundant role for TPM4 in platelet biogenesis in humans and mice"* ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous TPM4 truncating variant** (e.g., p.Gln108\*) or deleterious missense variant (e.g., p.R182C, p.A183V) **leads to** reduced functional cytoskeletal tropomyosin Tpm4.2 (haploinsufficiency — reduced TPM4 protein directly demonstrated, [PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/); gene-dosage dependence shown in mice, [PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
2. Reduced Tpm4.2 **results in** destabilized and mis-specified actin–tropomyosin filaments, because Tpm4.2 normally binds F-actin with high affinity, competes with α-actinin, and regulates myosin/cofilin (in vitro; [PMID: 28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/), [PMID: 28101865](https://pubmed.ncbi.nlm.nih.gov/28101865/)).
3. Destabilized filaments **lead to** disrupted megakaryocyte demarcation membrane system and impaired actomyosin-driven proplatelet architecture (*inferred*, supported by the TMOD3–TM4–F-actin axis in megakaryocytes; [PMID: 25964668](https://pubmed.ncbi.nlm.nih.gov/25964668/)).
4. This **results in** a defect in the terminal stages of platelet production (directly demonstrated in human and mouse megakaryocytes; [PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
5. The production defect **produces** fewer, larger platelets = **macrothrombocytopenia** (demonstrated).
6. **Branch:** reduced/mis-localized Tpm4.2 in circulating platelets **also leads to** mildly impaired platelet spreading and secretion — more pronounced for missense alleles ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/), [PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)).
7. Steps 5 and 6 together **result in** a **mild mucocutaneous bleeding tendency**.

```
 TPM4 truncating / missense variant (heterozygous)
              │  (haploinsufficiency)
              ▼
 ↓ functional cytoskeletal tropomyosin Tpm4.2
              │  (↓F-actin specification/stabilization;
              │   altered α-actinin / myosin / cofilin balance)
              ▼
 Destabilized, mis-specified actin–tropomyosin filaments
              │  (TMOD3–TM4–F-actin module affected)
              ▼
 Disrupted demarcation membrane system / proplatelet architecture   [inferred]
              ▼
 Defect in TERMINAL stages of platelet production  ───────────────┐
              ▼                                                    │ (branch)
 Fewer, larger platelets = MACROTHROMBOCYTOPENIA                   ▼
              │                                     Mildly impaired platelet
              │                                     spreading & secretion
              │                                     (greater for missense alleles)
              └──────────────┬──────────────────────────────┘
                             ▼
                 Mild mucocutaneous bleeding tendency
```

### Upstream vs downstream, cells, and biological processes

- **Upstream:** the genetic lesion and the resulting reduction in Tpm4.2 protein (molecular/protein level).
- **Midstream:** actin-cytoskeleton dysregulation within **megakaryocytes** (CL:0000556, megakaryocyte) — the cell type where platelet biogenesis occurs.
- **Downstream:** quantitative and qualitative abnormalities of circulating **platelets** (CL:0000233, platelet).

**Suggested GO biological-process terms:** platelet formation (GO:0030220), megakaryocyte development (GO:0035855), actin filament organization (GO:0007015), actin cytoskeleton organization (GO:0030036), regulation of actin filament depolymerization (GO:0030834). **Suggested GO molecular-function terms:** actin binding (GO:0003779), actin filament binding (GO:0051015). **Suggested GO cellular-component terms:** actin cytoskeleton (GO:0015629), stress fiber (GO:0001725), cortical actin cytoskeleton (GO:0030864). **Suggested CL terms:** megakaryocyte (CL:0000556), platelet (CL:0000233). **Suggested CHEBI/related entities:** tranexamic acid (CHEBI:48669), desmopressin (CHEBI:4450).

---

## Section-by-Section Report

### 1. Disease Information
- **Overview:** A rare Mendelian **autosomal dominant macrothrombocytopenia** — reduced platelet count with abnormally large platelets — caused by TPM4 variants, typically mild and lifelong.
- **Key identifiers:** **MONDO:0100487**; **Gene:** TPM4 (HGNC:12013; NCBI Gene 7171; Ensembl ENSG00000167460; UniProt P67936). OMIM, Orphanet, ICD-10/11, and MeSH disease-specific identifiers were **not recorded/confirmed** in the available evidence; this is a recently delineated entity (2017) and may be captured under broad terms such as "constitutional/inherited macrothrombocytopenia." The reference transcript is **NM_003290.3**.
- **Synonyms:** TPM4-related macrothrombocytopenia; TPM4-related thrombocytopenia; tropomyosin-4-related platelet disorder. (No formally recorded synonym list available.)
- **Data source type:** Information is derived from **individual patients/families** (case series and pedigrees) combined with **aggregated population genomics** (GWAS of platelet traits) and **model-organism** data — not from a disease-level EHR registry.

### 2. Etiology
- **Causal factors:** Purely **genetic** — heterozygous pathogenic variants in TPM4. No environmental or infectious cause.
- **Genetic risk factors:** The causal variants themselves (truncating/nonsense and rare deleterious missense). GWAS identified TPM4 as influencing platelet count and mean platelet volume in ~70,000 individuals, the common-variant lead that preceded Mendelian confirmation ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Environmental/lifestyle risk factors:** None established. Age, sex, and exposures do not cause the disorder, though they may modulate bleeding expression (e.g., menorrhagia in women, bleeding with surgery/trauma).
- **Protective factors:** None specifically identified (genetic or environmental).
- **Gene–environment interactions:** None documented. Bleeding risk is expected to rise with hemostatic challenges (surgery, trauma, antiplatelet/anticoagulant drugs), but this is a general consequence of thrombocytopenia rather than a specific GxE interaction.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity | Course | Frequency |
|---|---|---|---|---|---|---|
| Thrombocytopenia (low platelet count) | Laboratory abnormality | HP:0001873 | Congenital/lifelong | Mild–moderate | Stable, non-progressive | ~100% of affected |
| Enlarged platelets / ↑MPV | Laboratory abnormality | HP:0040310 (large platelets) / HP:0011877 (↑MPV) | Congenital/lifelong | — | Stable | High (hallmark) |
| Mucocutaneous bleeding (epistaxis, bruising, menorrhagia) | Clinical sign/symptom | HP:0000978 (bruising), HP:0000421 (epistaxis), HP:0000132 (menorrhagia), HP:0001892 (abnormal bleeding) | Lifelong | Mild (missense alleles more severe) | Episodic with challenges | Variable; often mild/absent |
| Impaired platelet spreading / secretion | Laboratory abnormality (functional) | HP:0011869 (abnormal platelet function) | — | Mild; greater for missense | Stable | Variant-dependent |

- **Quality-of-life impact:** Generally low; most affected individuals are minimally symptomatic. Menorrhagia and surgical/peri-procedural bleeding are the main QoL concerns in symptomatic carriers. No disease-specific EQ-5D/SF-36/PROMIS data available.
- Normal aggregation and granule secretion can occur despite the genetic defect ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)).

### 4. Genetic / Molecular Information
- **Causal gene:** **TPM4** (tropomyosin 4), chromosome 19p13.1; HGNC:12013; UniProt P67936; transcript **NM_003290.3**.
- **Reported pathogenic variants:**

| Variant (cDNA / protein) | Type | Classification | Functional consequence | Reference |
|---|---|---|---|---|
| Truncating variants (2 BRIDGE-BPD families) | Truncating | Pathogenic | Loss of function / haploinsufficiency | [PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/) |
| c.322C>T (p.Gln108\*) | Nonsense | Pathogenic (segregates in 5 relatives) | ↓TPM4 protein; impaired spreading | [PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/) |
| p.R182C | Missense (conserved) | Likely pathogenic | ↓secretion, aggregation/spreading defect; excessive bleeding | [PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/) |
| p.A183V | Missense (conserved) | Likely pathogenic | Platelet dysfunction, disordered tropomyosin pattern | [PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/) |

- **Allele frequency:** All reported variants are rare/private (not population-polymorphic); specific gnomAD frequencies not recorded here but expected to be absent or ultra-rare.
- **Somatic vs germline:** **Germline**, constitutional.
- **Functional consequences:** Truncating/nonsense = **loss of function (haploinsufficiency)**; missense = deleterious with likely dominant-negative/mis-specification of the actin–tropomyosin filament (disordered tropomyosin pattern). Gene-dosage dependence demonstrated in mice ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Modifier genes:** None established; TMOD3 (tropomodulin-3) is a functional partner in megakaryocyte actin organization but not reported as a clinical modifier ([PMID: 25964668](https://pubmed.ncbi.nlm.nih.gov/25964668/)).
- **Epigenetic information / chromosomal abnormalities:** None reported for this disorder.

### 5. Environmental Information
- **Environmental factors, lifestyle factors, infectious agents:** **Not applicable.** This is a monogenic germline disorder with no known environmental, lifestyle, or infectious contribution. (Hemostatic stressors influence bleeding expression but do not cause the disease.)

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** above for the full ordered causal chain, ASCII diagram, and ontology-term suggestions. Key points:
- **Molecular pathway:** actin-cytoskeleton regulation via tropomyosin specification of actin filaments (not a classical signaling cascade such as Wnt/MAPK). Tropomyosins compete with α-actinin, regulate myosin II, and protect filaments from ADF/cofilin severing ([PMID: 28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/)).
- **Cellular process:** defective proplatelet formation / terminal platelet production in megakaryocytes ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Protein dysfunction:** reduced/mis-localized Tpm4.2 (loss of function for truncating; mis-specification/possible dominant-negative for missense).
- **Subcellular compartments:** actin cytoskeleton, stress fibers, demarcation membrane system of megakaryocytes.
- **Immune/metabolic involvement:** none intrinsic. (Note: distinct, non-disease-causal TPM4 biology appears in cancer contexts — e.g., TPM4 modulating ferroptosis via SCD1 in gastric cancer, [PMID: 40214825](https://pubmed.ncbi.nlm.nih.gov/40214825/) — but these are unrelated to the platelet disorder.)
- **Molecular profiling:** direct demonstration of reduced TPM4 protein in patient platelets ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)); disordered tropomyosin filament pattern with missense variants ([PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)).

### 7. Anatomical Structures Affected
- **Organ/system:** hematopoietic / **blood and bone marrow** (UBERON:0000178 blood; UBERON:0002371 bone marrow). Body system: cardiovascular/hematologic (coagulation-hemostasis).
- **Primary cells:** **megakaryocytes** (CL:0000556) in bone marrow; **platelets** (CL:0000233) in circulation.
- **Secondary involvement:** mucosal/cutaneous bleeding sites (skin, nasal mucosa, endometrium) are affected by the bleeding tendency, not by intrinsic TPM4 pathology there.
- **Subcellular:** actin cytoskeleton (GO:0015629), stress fiber (GO:0001725), demarcation membrane system.
- **Lateralization:** not applicable (systemic hematologic disorder).

### 8. Temporal Development
- **Onset:** **Congenital/constitutional**; thrombocytopenia is lifelong and typically present from birth, though often detected incidentally later in life.
- **Onset pattern:** chronic/insidious (frequently asymptomatic until an incidental CBC or a bleeding challenge).
- **Progression:** **Stable, non-progressive.** No disease staging; platelet counts remain mild-to-moderately low throughout life ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)).
- **Duration:** chronic, lifelong.
- **Remission:** none expected (constitutional). No spontaneous resolution.
- **Critical periods:** hemostatic challenges (surgery, childbirth, trauma, dental procedures, menstruation) are the windows where intervention matters.

### 9. Inheritance and Population
- **Inheritance:** **Autosomal dominant** (heterozygous variants segregate with phenotype; [PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/), [PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)).
- **Penetrance:** appears high for the hematologic phenotype within reported pedigrees (e.g., 5 affected relatives in the Spanish family), but **expressivity of the bleeding tendency is variable** (mild/absent to excessive, variant-dependent).
- **Anticipation / germline mosaicism / founder effects:** none reported.
- **Consanguinity:** not relevant (dominant).
- **Epidemiology:** **Very rare**; only a handful of families reported worldwide (two BRIDGE-BPD families, one Spanish family, and small missense series). Precise prevalence/incidence **not established** — likely underdiagnosed and under-reported because of the mild phenotype and overlap with ITP.
- **Demographics:** no established ethnic predilection; reported in European pedigrees. Sex ratio not established; women may present more often clinically due to menorrhagia.

### 10. Diagnostics
- **Laboratory tests:** **Complete blood count** showing low platelet count (HP:0001873) with **increased mean platelet volume** and large platelets on **peripheral blood film review** — the key screening findings. Platelet **aggregation and secretion studies** may be **normal** (especially truncating variants) or mildly abnormal (missense variants) ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/), [PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)).
- **Specialized tests:** platelet spreading assays (impaired after TRAP-6/CRP) and immunofluorescence showing TPM4 delocalization in activated platelets ([PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)).
- **Genetic testing (definitive):** **Whole-exome sequencing** or **inherited platelet disorder / thrombocytopenia gene panels** including TPM4; single-gene testing confirms a familial variant. Genetic diagnosis is essential because the phenotype mimics other macrothrombocytopenias and ITP ([PMID: 19408193](https://pubmed.ncbi.nlm.nih.gov/19408193/) for the inherited-platelet-disorder diagnostic paradigm).
- **Imaging / CMA / karyotype / FISH / mtDNA / repeat testing:** not indicated (no structural, mitochondrial, or repeat-expansion component).
- **Differential diagnosis:** immune thrombocytopenia (ITP) — key to avoid unnecessary immunosuppression/splenectomy; other inherited macrothrombocytopenias (MYH9-related disorder, Bernard–Soulier syndrome, GP1BA/B, ACTN1-related, TUBB1-related, ITGA2B/ITGB3-related); Glanzmann thrombasthenia and von Willebrand disease for bleeding work-up. Distinguishing features: TPM4 disorder is mild, lifelong, autosomal dominant, with large platelets and often-normal function.
- **Screening:** cascade **genetic testing of at-risk relatives** once a familial variant is identified; no population newborn screening.

### 11. Outcome / Prognosis
- **Survival/mortality:** **Normal life expectancy**; no excess mortality reported. Not a life-limiting condition.
- **Morbidity:** low overall; limited to bleeding events (notably menorrhagia and peri-procedural bleeding). Missense-variant carriers can have higher bleeding morbidity ([PMID: 34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/)).
- **Complications:** bleeding with surgery/trauma; iron-deficiency anemia from menorrhagia; risk of misdiagnosis as ITP leading to unnecessary immunosuppressive treatment or splenectomy.
- **Recovery/QoL:** generally excellent with appropriate recognition and supportive management.
- **Prognostic factors:** variant type (truncating → predominantly count defect, milder bleeding; missense → added platelet-function defect, potentially more bleeding) is the main prognostic determinant.

### 12. Treatment
There is **no disease-specific or curative therapy**; management is **supportive and bleeding-oriented**, extrapolated from general inherited-platelet-disorder care.

| Intervention | Role | NCIT suggestion |
|---|---|---|
| **Tranexamic acid** (antifibrinolytic) | Mucosal bleeding, menorrhagia, peri-procedural | NCIT Tranexamic Acid; CHEBI:48669 |
| **Desmopressin (DDAVP)** | May improve hemostasis for minor procedures | NCIT Desmopressin; CHEBI:4450 |
| **Hormonal therapy / combined oral contraceptives** | Menorrhagia control | NCIT Oral Contraceptive |
| **Platelet transfusion** | Severe bleeding or major surgery (reserve; HLA considerations) | NCIT Platelet Transfusion |
| **Recombinant activated factor VIIa** | Refractory bleeding in inherited platelet disorders (adjunct) | NCIT Recombinant Factor VIIa |
| **Iron supplementation** | Treat iron-deficiency anemia from chronic bleeding | NCIT Iron Supplement |

- **Pharmacogenomics / gene therapy / cell therapy / RNA therapy / targeted or immunotherapy:** **none applicable/available** for this disorder.
- **Treatment strategy:** avoid misdiagnosis-driven ITP therapy (steroids, IVIG, splenectomy); manage bleeding proactively around hemostatic challenges; involve hematology and genetic counseling. The general supportive toolkit for inherited platelet bleeding (antifibrinolytics, hormonal therapy, desmopressin, platelet support) parallels approaches used in other inherited platelet disorders.

### 13. Prevention
- **Primary prevention:** not possible (germline). **Genetic counseling** for autosomal dominant transmission (50% transmission risk); options include **prenatal testing** and **preimplantation genetic diagnosis** where a familial variant is known.
- **Secondary prevention:** cascade genetic testing of relatives; correct early diagnosis to prevent iatrogenic harm (unnecessary immunosuppression/splenectomy).
- **Tertiary prevention:** peri-procedural planning (antifibrinolytics, platelet support), menorrhagia control, iron repletion, and avoidance/caution with antiplatelet and anticoagulant drugs.
- **Immunization / public health / environmental interventions:** not applicable.

### 14. Other Species / Natural Disease
- **Model species:** **Mouse** (*Mus musculus*, NCBI Taxon 10090); orthologous gene **Tpm4** (NCBI Gene 326618). ENU-induced _Tpm4_ missense mutations and targeted _Tpm4_ inactivation reproduce gene-dosage-dependent macrothrombocytopenia ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Natural disease in companion animals/wildlife:** none reported (no OMIA entry identified).
- **Comparative biology / conservation:** the mechanism is **evolutionarily conserved** — *"a nonredundant role for TPM4 in platelet biogenesis in humans and mice"* ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Zoonotic potential:** not applicable.

### 15. Model Organisms
- **Mouse models (primary):**
  - **ENU-induced _Tpm4_ missense mutants** — gene-dosage-dependent macrothrombocytopenia ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
  - **Targeted _Tpm4_ inactivation (knockout)** — macrothrombocytopenia with otherwise normal blood counts, modeling haploinsufficiency ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/)).
- **Cellular/in vitro models:** human and mouse **megakaryocyte cultures** showing the terminal platelet-production defect; patient-derived platelets for spreading/secretion assays ([PMID: 28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/), [PMID: 35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/)); **in vitro reconstituted actin–tropomyosin filaments** characterizing Tpm4.2 biochemistry ([PMID: 28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/)).
- **Phenotype recapitulation:** mouse models recapitulate the core macrothrombocytopenia (low count, enlarged platelets) with gene-dosage dependence — a strong match to human disease.
- **Limitations:** mild bleeding phenotype and subtle platelet-function defects are harder to model; missense dominant-negative effects may differ between species. Resource: **MGI** for _Tpm4_ alleles.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [28134622](https://pubmed.ncbi.nlm.nih.gov/28134622/) | *Mutations in tropomyosin 4 underlie a rare form of human macrothrombocytopenia* | Human clinical + mouse + in vitro | Disease-defining: truncating TPM4 → AD macrothrombocytopenia; gene-dosage mechanism; terminal platelet-production defect; conserved human/mouse role |
| [35170221](https://pubmed.ncbi.nlm.nih.gov/35170221/) | *A novel nonsense variant in TPM4 caused dominant macrothrombocytopenia...* | Human clinical (Spanish pedigree) | Independent confirmation: p.Gln108\*; ↓TPM4 protein; impaired spreading; mild lifelong phenotype with normal aggregation/secretion |
| [34758189](https://pubmed.ncbi.nlm.nih.gov/34758189/) | *Rare missense variants in TPM4 are associated with platelet dysfunction...excessive bleeding* | Human clinical | Missense end of spectrum: p.R182C, p.A183V; reduced secretion, aggregation/spreading defects, disordered tropomyosin; excessive bleeding |
| [25964668](https://pubmed.ncbi.nlm.nih.gov/25964668/) | *Regulation of actin polymerization by tropomodulin-3 controls megakaryocyte actin organization and platelet biogenesis* | Mouse / cell biology | Places TPM4/TM4 in the TMOD3–F-actin module of proplatelet formation |
| [28216317](https://pubmed.ncbi.nlm.nih.gov/28216317/) | *Tropomyosin isoforms specify functionally distinct actin filament populations in vitro* | In vitro biochemistry | Tpm4.2 binds F-actin with high affinity, competes with α-actinin — molecular basis for destabilization |
| [28101865](https://pubmed.ncbi.nlm.nih.gov/28101865/) | *Tropomyosin structure, function, and interactions: a dynamic regulator* | Review | Tropomyosin as universal specifier/regulator of the actin cytoskeleton |
| [19408193](https://pubmed.ncbi.nlm.nih.gov/19408193/) | *Genetic testing in the diagnostic evaluation of inherited platelet disorders* | Review | Diagnostic paradigm for inherited platelet disorders (context) |

Supporting context literature: cytoskeletal tropomyosin structure/function ([PMID: 36586407](https://pubmed.ncbi.nlm.nih.gov/36586407/), [PMID: 32037094](https://pubmed.ncbi.nlm.nih.gov/32037094/), [PMID: 10986121](https://pubmed.ncbi.nlm.nih.gov/10986121/)); general inherited-platelet-disorder management ([PMID: 41201390](https://pubmed.ncbi.nlm.nih.gov/41201390/), [PMID: 40932452](https://pubmed.ncbi.nlm.nih.gov/40932452/)). Unrelated TPM4 cancer biology (not disease-causal here): [PMID: 40214825](https://pubmed.ncbi.nlm.nih.gov/40214825/), [PMID: 31804537](https://pubmed.ncbi.nlm.nih.gov/31804537/).

---

## Limitations and Knowledge Gaps

1. **Very small clinical evidence base:** only ~3 pedigrees/series directly define the disorder (two BRIDGE-BPD families, one Spanish family, a small missense series). Prevalence, penetrance, and expressivity estimates are therefore uncertain.
2. **Incomplete formal nosology:** OMIM, Orphanet, ICD, and MeSH identifiers were not confirmed in the available evidence; standardized synonyms are not catalogued.
3. **Variant-level data gaps:** exact gnomAD frequencies, full ACMG/AMP classification detail, and the complete truncating-variant coordinates from the 2017 families were not captured here.
4. **Mechanistic inference:** the demarcation-membrane / proplatelet-architecture step (step 3 of the causal chain) is inferred from the TMOD3–TM4–F-actin module rather than directly demonstrated for pathogenic TPM4 variants.
5. **Missense mechanism uncertainty:** whether missense alleles act by simple loss of function, dominant-negative mis-specification, or both is not fully resolved.
6. **No treatment trials:** all management is extrapolated/supportive; there are no disease-specific therapeutic studies or clinical-trial data (no NCT identifiers).

---

## Proposed Follow-up Experiments / Actions

1. **International variant/case registry:** aggregate all reported and new TPM4 families to estimate prevalence, penetrance, genotype–phenotype correlation (truncating vs missense), and bleeding scores (ISTH-BAT).
2. **Formal nosology curation:** confirm/create OMIM, Orphanet, and ICD-11 entries and a canonical synonym set; reconcile with MONDO:0100487.
3. **Mechanistic validation of step 3:** live-imaging of proplatelet formation and demarcation-membrane dynamics in patient-derived iPSC megakaryocytes carrying truncating vs missense TPM4 variants.
4. **Allele-mechanism dissection:** biochemical and structural (cryo-EM) comparison of wild-type vs p.R182C/p.A183V Tpm4.2 on actin filaments to test dominant-negative vs loss-of-function.
5. **Diagnostic guidance:** promote inclusion of TPM4 on thrombocytopenia panels and develop a simple clinical algorithm (large platelets + AD inheritance + often-normal aggregation → sequence TPM4) to reduce ITP misdiagnosis.
6. **Natural-history and bleeding-management study:** prospective assessment of peri-procedural outcomes and the efficacy of antifibrinolytics/desmopressin/hormonal therapy specifically in TPM4 carriers.

---

*Evidence-source legend: human clinical = patient/pedigree studies; model organism = mouse; in vitro = biochemistry/cell biology; review = synthesis. All mechanistic and clinical claims are cited to the PMIDs above; inferred steps are labeled as such.*


## Artifacts

- [OpenScientist final report](TPM4-related_Platelet_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TPM4-related_Platelet_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001873` (2 mentions) - the report calls it "Laboratory abnormality"; HP calls it **Thrombocytopenia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000556` (3 mentions) - the report calls it "megakaryocytes", "Primary cells:** **megakaryocytes"; CL calls it **megakaryocyte**
- `GO:0015629` (2 mentions) - the report calls it "Subcellular:** actin cytoskeleton"; GO calls it **actin cytoskeleton**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000556` - called "megakaryocytes", "Primary cells:** **megakaryocytes"