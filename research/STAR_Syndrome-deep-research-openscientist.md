---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:29.771844'
end_time: '2026-11-05T00:13:17.471105'
duration_seconds: 1127.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: STAR Syndrome
  mondo_id: MONDO:0010408
  category: Mendelian
  causal_genes: CCNQ
  omim_id: OMIM:300707
  synonyms: STAR syndrome, X-linked dominant
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
citation_count: 9
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 3
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:29088509
  - PMID:28886341
  relevance_assessed: 9
  on_topic: 8
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010408
    reported_labels:
    - MONDO
    ontology_label: syndactyly-telecanthus-anogenital and renal malformations syndrome
  labels_variant: 1
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
  path: STAR_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: STAR_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** STAR Syndrome
- **MONDO ID:** MONDO:0010408 (if available)
- **Causal gene(s):** CCNQ
- **OMIM:** OMIM:300707
- **Synonyms:** STAR syndrome, X-linked dominant
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **STAR Syndrome** covering all of the
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

# STAR Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** STAR syndrome (toe **S**yndactyly, **T**elecanthus, **A**nogenital and **R**enal malformations)
**MONDO:** MONDO:0010408 · **OMIM (phenotype):** 300707 · **OMIM (gene):** 300708 · **Orphanet:** ORPHA:83617
**Causal gene:** **CCNQ** (HGNC-approved symbol; historical/alias symbol **FAM58A**, protein "Cyclin M" / "Cyclin Q")
**Inheritance:** X-linked dominant, essentially female-limited

---

## Summary

STAR syndrome is an ultra-rare X-linked dominant congenital malformation syndrome defined by the tetrad of **toe Syndactyly, Telecanthus, and Anogenital and Renal malformations**. Its causal gene is **CCNQ** — the HGNC-approved symbol for the gene historically published as **FAM58A**, located at **Xq28**. The gene product is **Cyclin Q** (also called Cyclin M; UniProt Q8N1B3, 248 amino acids), the activating cyclin of the orphan cyclin-dependent kinase **CDK10**. The syndrome was first delineated by Unger and colleagues in 2008, who identified causative FAM58A/CCNQ mutations in all affected individuals across multiple families and established the X-linked dominant inheritance pattern ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/)). It is important to distinguish STAR syndrome from the separate, biallelic recessive **CDK10**-deficiency disorder (severe growth retardation, spine malformations), which affects the kinase partner rather than the cyclin ([PMID: 28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/)).

Mechanistically, STAR-associated Cyclin Q mutants **fail to bind CDK10**, abolishing the kinase activity of the CDK10/Cyclin Q complex ([PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/)). The downstream consequences converge on two documented axes: (1) **impaired proteasomal degradation of the transcription factor ETS2**, which accumulates in patient-derived cells and elevates MAPK/RAS-pathway output; and (2) **dysregulation of the PKN2–RhoA–actin cytoskeletal axis**, which drives aberrant assembly and elongation of the **primary cilium**. Kidney tissue from a STAR patient displays dilated renal tubules and abnormal, elongated cilia, directly linking the renal malformation to a ciliopathy-like mechanism ([PMID: 27104747](https://pubmed.ncbi.nlm.nih.gov/27104747/)). The CDK10/Cyclin Q complex additionally phosphorylates RNA polymerase II C-terminal domain (CTD), c-MYC, and RB1, situating it within transcriptional and cell-cycle control ([PMID: 35291876](https://pubmed.ncbi.nlm.nih.gov/35291876/)).

The disorder is essentially limited to females, consistent with presumed male lethality; this is quantitatively supported by strong gnomAD loss-of-function constraint on CCNQ (pLI 0.99, LOEUF 0.44; 3 observed vs 17.7 expected LoF variants). The phenotypic spectrum is broad and includes a **lethal "STAR plus" form** associated with large contiguous-gene Xq28 deletions. There is no disease-specific or curative therapy — management is supportive, malformation-directed (surgical correction of syndactyly, anorectal and renal anomalies), and anchored by genetic counseling.

---

## 1. Disease Information

**Overview.** STAR syndrome is a recognizable multiple-congenital-anomaly syndrome whose name is an acronym for its cardinal features: toe **S**yndactyly, **T**elecanthus, and **A**nogenital and **R**enal malformations. All four cardinal features were present in every affected individual in the original cohort ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/)). It is a developmental disorder of Mendelian, X-linked dominant inheritance.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0010408 |
| OMIM (phenotype) | 300707 |
| OMIM (gene, CCNQ/FAM58A) | 300708 |
| Orphanet | ORPHA:83617 |
| Gene (HGNC) | CCNQ, HGNC:28434 |
| NCBI Gene | 92002 |
| Ensembl | ENSG00000262919 |
| UniProt (protein) | Q8N1B3 (Cyclin-Q) |

**Synonyms / alternative names.** "STAR syndrome"; "Syndactyly, telecanthus, and anogenital and renal malformations"; "Toe syndactyly–telecanthus–anogenital and renal malformations syndrome." The causal gene has been published under both **FAM58A** (original) and **CCNQ** (current HGNC symbol); the protein is referred to as **Cyclin M** and **Cyclin Q** interchangeably in the literature.

**Information source.** The disease-level knowledge base here is derived from **aggregated resources** (OMIM, Orphanet, gnomAD, UniProt, InterPro) combined with a small set of **individual patient reports and case series** (the primary literature). Because the condition is ultra-rare, essentially all clinical knowledge comes from individual or small-pedigree case reports rather than large registries or EHR cohorts.

---

## 2. Etiology

**Disease causal factors.** STAR syndrome is a **monogenic, genetic** disorder. The primary cause is **loss of function of CCNQ/FAM58A** on Xq28. Two variant mechanisms are documented: (a) **intragenic point mutations** (e.g., the nonsense variant c.651G>A, p.Trp217*) and (b) **contiguous-gene microdeletions** at Xq28 that remove CCNQ (and, when large, neighboring genes). There are no established environmental or infectious causes.

**Genetic risk factors.** The disease-causing variants are themselves the sole genetic "risk factor." Being female is the principal demographic determinant of observed disease, because affected males are presumed to be non-viable (male lethality). gnomAD constraint metrics confirm that CCNQ is highly intolerant to loss of function (pLI 0.989; LOEUF 0.438; 3 observed vs 17.7 expected LoF variants), consistent with pathogenic LoF and male lethality.

**Environmental / lifestyle risk factors.** None identified. STAR syndrome is congenital and determined by the germline genotype; no toxin, occupational exposure, diet, or lifestyle factor is implicated.

**Protective factors.** No genetic modifier alleles or environmental protective factors have been reported. In females, **X-inactivation patterns** (skewing toward silencing the mutant allele) are a plausible but unproven modifier of expressivity — this remains inferred rather than demonstrated.

**Gene–environment interactions.** None documented; the disorder is explained by the germline CCNQ lesion alone.

---

## 3. Phenotypes

The cardinal tetrad was present in all affected individuals in the founding study ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/)). Severity is **variable** even within a single pedigree, and the spectrum has expanded with subsequent reports.

| Phenotype | Type | Suggested HPO term | Onset | Frequency / notes |
|---|---|---|---|---|
| Toe syndactyly | Physical malformation | HP:0001770 (Toe syndactyly) | Congenital | Cardinal; all patients in original cohort |
| Telecanthus | Physical sign | HP:0000506 (Telecanthus) | Congenital | Cardinal |
| Anogenital malformation (anal stenosis/atresia, clitoromegaly, urogenital sinus) | Physical malformation | HP:0002023 (Anal atresia); HP:0008665 (Anal stenosis); HP:0008730 (Clitoromegaly) | Congenital | Cardinal |
| Renal malformation (renal hypoplasia, dysplasia, vesicoureteral reflux) | Physical malformation | HP:0000089 (Renal hypoplasia); HP:0000076 (Vesicoureteral reflux) | Congenital | Cardinal |
| Congenital heart disease | Clinical sign | HP:0001627 (Abnormal heart morphology) | Congenital | Reported in severe cases |
| Ocular: medial upper-eyelid prominences, madarosis, optic nerve hypoplasia, peripapillary atrophy, macular drusen | Clinical signs | HP:0000540 (Optic nerve hypoplasia); HP:0000561 (Absent eyelashes / madarosis) | Congenital | Mother–daughter pair ([PMID: 26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/)) |
| Tethered spinal cord | Clinical sign | HP:0002144 (Tethered cord) | Congenital/childhood | Added by multigenerational pedigree ([PMID: 28322501](https://pubmed.ncbi.nlm.nih.gov/28322501/)) |
| Hearing loss | Sensory sign | HP:0000365 (Hearing impairment) | Childhood | Added by same pedigree |
| "STAR plus" (cleft lip/palate, omphalocele, cerebral malformations) | Severe/lethal | HP:0410030 (Cleft lip); HP:0001539 (Omphalocele) | Congenital | Lethal form with large Xq28 deletion ([PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/)) |

**Severity and progression.** Severity ranges from **mild** (e.g., a mother with unilateral foot syndactyly, telecanthus, anal stenosis, and a hypoplastic kidney) to **lethal** (STAR plus). Malformations are structural and **stable/non-progressive** once formed, though secondary renal functional decline can occur over time. In the mother–daughter pair, the daughter's presentation was uniformly more severe than the mother's, illustrating intrafamilial variable expressivity ([PMID: 26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/)).

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare condition. Impact is driven by the burden of multiple reconstructive surgeries (syndactyly, anorectal, urogenital), renal function monitoring, and, where present, developmental or sensory impairment. Lethal forms have the most extreme impact (neonatal death).

---

## 4. Genetic / Molecular Information

**Causal gene.** **CCNQ** (alias FAM58A), Xq28; HGNC:28434; NCBI Gene 92002; Ensembl ENSG00000262919 (transcripts ENST00000440428 / ENST00000576892); gene OMIM 300708. The protein, **Cyclin Q** (UniProt Q8N1B3), is 248 amino acids and contains **two cyclin-box folds** — InterPro IPR048055 ("Cyclin-Q first cyclin box") and IPR048053 ("Cyclin-Q second cyclin box"), with Pfam domains PF00134 (Cyclin_N) and PF21797 (CycT2-like C-terminal).

**Pathogenic variants.**

| Variant | Type | Classification | Consequence |
|---|---|---|---|
| c.651G>A, p.Trp217* (NM_152274) | Nonsense | Pathogenic | Truncates terminal 31 residues (217–248), removing part of the C-terminal/second cyclin box ([PMID: 28322501](https://pubmed.ncbi.nlm.nih.gov/28322501/)) |
| Original FAM58A mutations (Unger 2008) | Point mutations / small lesions | Pathogenic | Loss of function ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/)) |
| ~130 kb Xq28 deletion including FAM58A | Contiguous-gene deletion | Pathogenic | LoF + flanking genes → lethal STAR plus ([PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/)) |

**Functional consequence.** **Loss of function.** STAR-associated Cyclin Q mutants are **unable to interact with CDK10** ([PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/)), abolishing kinase-complex activity. The p.Trp217* truncation removes the C-terminal cyclin-box region required for CDK10 binding, mechanistically explaining the loss of interaction.

**Allele frequency.** Pathogenic variants are not present at appreciable frequency in population databases; CCNQ shows only 3 observed LoF variants against 17.7 expected in gnomAD (strong depletion; LoF Z = 2.96, missense Z = 2.19).

**Somatic vs germline.** **Germline** (constitutional, congenital). No somatic STAR-syndrome mechanism is described, although CDK10/Cyclin Q is noted to act as a **tumour suppressor** in other contexts ([PMID: 35291876](https://pubmed.ncbi.nlm.nih.gov/35291876/)).

**Modifier genes / epigenetics.** No specific modifier genes identified. In females, **X-chromosome inactivation** is the most plausible epigenetic modifier of expressivity (inferred). No DNA-methylation or histone-modification signature is established for the disease.

**Chromosomal abnormalities.** Contiguous-gene **Xq28 microdeletions** are a documented cause; large deletions correlate with the lethal STAR plus phenotype.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious agents contribute to STAR syndrome. It is a purely genetic, congenital malformation syndrome. This section is **not applicable** beyond noting the absence of non-genetic contributors.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A germline **loss-of-function lesion in CCNQ/FAM58A** (point mutation such as p.Trp217*, or Xq28 deletion) **truncates or eliminates Cyclin Q**, removing part of its C-terminal cyclin box.
2. The truncated/absent Cyclin Q **cannot bind CDK10** → **loss of CDK10/Cyclin Q kinase complex activity** (demonstrated: STAR mutants fail to interact with CDK10, [PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/)).
3. Loss of kinase activity **branches** into two documented downstream effects:
   - **Branch A (transcription-factor / MAPK axis):** CDK10/Cyclin Q normally phosphorylates **ETS2** and promotes its **proteasomal degradation**. Without the kinase, **ETS2 protein accumulates** (observed in STAR patient cells) → **increased ETS/MAPK transcriptional output** (demonstrated, [PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/)).
   - **Branch B (cytoskeleton / cilium axis):** CDK10/Cyclin Q normally phosphorylates **PKN2** on Thr121/Thr124 within its RhoA-binding domain. Loss of this phosphorylation **destabilizes RhoA and the actin network** → **aberrant assembly and elongation of the primary cilium** (demonstrated; ectopic RhoA rescues the phenotype, [PMID: 27104747](https://pubmed.ncbi.nlm.nih.gov/27104747/)).
4. **Abnormal, elongated primary cilia** and dysregulated developmental signaling **lead to** the congenital malformations — directly evidenced by **dilated renal tubules and abnormal elongated cilia in STAR patient kidney tissue** ([PMID: 27104747](https://pubmed.ncbi.nlm.nih.gov/27104747/)).
5. These developmental defects **result in** the clinical tetrad (toe syndactyly, telecanthus, anogenital and renal malformations) and the broader phenotypic spectrum.

```
CCNQ/FAM58A LoF (p.Trp217*, Xq28 del)
        │  truncates C-terminal cyclin box
        ▼
Cyclin Q cannot bind CDK10
        │  loss of CDK10/Cyclin Q kinase activity
        ├───────────────────────────┐
        ▼ (Branch A)                 ▼ (Branch B)
 ETS2 not phosphorylated      PKN2 not phosphorylated (T121/T124)
        │ not degraded               │ RhoA destabilized
        ▼                            ▼
 ETS2 accumulates             actin network dysregulated
        │ ↑MAPK/ETS output           │
        ▼                            ▼
   developmental       primary cilium over-assembly/elongation
   signaling imbalance         │  (ciliopathy-like)
        └───────────┬──────────┘
                    ▼
     Congenital malformations: toe syndactyly, telecanthus,
     anogenital + renal anomalies (dilated renal tubules,
     abnormal cilia seen in patient kidney)
```

### Detail by category

- **Molecular pathways.** CDK10/Cyclin Q sits at the intersection of **ETS2/MAPK-RAS signaling**, **RhoA–PKN2 cytoskeletal signaling**, and **transcriptional/cell-cycle control** (RNA Pol II CTD, c-MYC, RB1 phosphorylation, [PMID: 35291876](https://pubmed.ncbi.nlm.nih.gov/35291876/)). Suggested GO: **GO:0004693** (cyclin-dependent protein serine/threonine kinase activity), **GO:0007399** (nervous system development), **GO:0060271** (cilium assembly).
- **Cellular processes.** Primary **ciliogenesis** (aberrant cilium elongation), **actin cytoskeleton organization**, **proteasomal protein degradation**, and **cell-growth/cell-cycle modulation**. Suggested GO: **GO:0030036** (actin cytoskeleton organization), **GO:0043161** (proteasome-mediated ubiquitin-dependent protein catabolic process).
- **Protein dysfunction.** **Loss of function** by truncation of the cyclin partner → failure of complex assembly (not misfolding/aggregation). The lesion disables an activating cyclin rather than the enzyme itself.
- **Metabolic changes.** Comparative transcriptomics of Cdk10-knockout mouse organs revealed **lipid metabolic changes** consistent with growth impairment ([PMID: 28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/)) — relevant to the kinase partner's loss and a reasonable proxy for pathway output in STAR.
- **Biochemical abnormality.** Deficient **serine/threonine kinase activity** of the CDK10/Cyclin Q holoenzyme.
- **Tissue-level mechanism.** Ciliary dysfunction in renal tubular epithelium → **dilated renal tubules** (patient tissue); developmental signaling imbalance in limb, midface, and cloacal/urogenital fields.
- **Molecular profiling.** ETS2 accumulation in patient cells (proteomic-level observation); longer cilia in CDK10-knockout MEFs; lipid-metabolic transcriptomic shifts in knockout organs.

**Cell types (suggested CL terms):** renal tubular epithelial cell (**CL:0002518**), ciliated epithelial cell (**CL:0000067**), fibroblast (**CL:0000057**). **Anatomy (UBERON):** kidney (**UBERON:0002113**), renal tubule (**UBERON:0001231**). **Subcellular (GO cellular component):** cilium (**GO:0005929**).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** kidney (UBERON:0002113), anorectal region / anus (UBERON:0001245), external genitalia / clitoris (UBERON:0003233), toes/feet (UBERON:0001466), periorbital/midface region (telecanthus).
- **Secondary / associated organ involvement:** heart (congenital heart disease), eye and optic nerve (ocular anomalies, optic nerve hypoplasia; UBERON:0000941 optic nerve), spinal cord (tethered cord; UBERON:0002240), ear/auditory system (hearing loss), and in lethal forms the brain (cerebral malformations; UBERON:0000955) and ventral body wall (omphalocele).
- **Body systems:** genitourinary, gastrointestinal (anorectal), musculoskeletal (digits), craniofacial, and variably cardiovascular, nervous, auditory, and visual systems.
- **Tissue/cell level:** epithelial tissue (renal tubular and ciliated epithelium), with primary-cilium pathology the unifying cellular lesion. Suggested CL: renal tubular epithelial cell (CL:0002518), ciliated cell (CL:0000064).
- **Subcellular level:** **primary cilium (GO:0005929)**, **actin cytoskeleton (GO:0015629)**, **proteasome complex (GO:0000502)**, and nucleus (transcriptional substrates RNA Pol II CTD, c-MYC, RB1).
- **Localization / lateralization:** malformations may be **unilateral or bilateral and asymmetric** — e.g., unilateral foot syndactyly and hypoplastic left kidney in one mother, versus bilateral renal hypoplasia in her more severely affected daughter ([PMID: 26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/)).

---

## 8. Temporal Development

- **Onset:** **Congenital** — all cardinal malformations are present at birth and often detectable prenatally (e.g., oligohydramnios from renal anomalies). Onset pattern is structural/developmental rather than acute.
- **Progression:** Structural anomalies are **stable** once formed. Secondary **renal functional decline** may progress with age depending on the severity of renal hypoplasia/dysplasia. The lethal STAR plus form progresses rapidly to **neonatal/early-infant death** (respiratory failure at 6 weeks in the reported case, [PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/)).
- **Disease course:** Chronic and lifelong in survivors; defined by the burden of congenital anomalies and their surgical management.
- **Critical period:** **Embryonic organogenesis** is the window of vulnerability (limb, midface, cloacal/urogenital, and renal development). There is no postnatal window for mechanistic "cure"; postnatal care is reconstructive and supportive.

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare.** Fewer than a few dozen cases are reported worldwide; precise prevalence/incidence figures are not established (Orphanet ORPHA:83617). No population-based incidence data exist.
- **Inheritance pattern:** **X-linked dominant**, established by Unger et al. who found causative FAM58A mutations on Xq28 in all affected individuals and inferred X-linked dominant inheritance ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/)).
- **Sex ratio:** Essentially **female-limited**; affected males are presumed non-viable (male lethality), consistent with the strong LoF constraint on CCNQ.
- **Penetrance / expressivity:** Apparently high penetrance in heterozygous females but **highly variable expressivity**, documented across a multigenerational pedigree and in mother–daughter pairs ([PMID: 28322501](https://pubmed.ncbi.nlm.nih.gov/28322501/); [PMID: 26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/)). Variable **X-inactivation** is the leading (inferred) explanation.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** No founder effect or consanguinity role established; de novo occurrence and familial transmission both documented.
- **Carrier frequency:** Not applicable in the classic sense — heterozygous females are affected, not silent carriers.
- **Population demographics:** No ethnic predilection or geographic clustering reported; cases are sporadic across populations.

---

## 10. Diagnostics

- **Clinical recognition:** Diagnosis is suspected from the characteristic tetrad (toe syndactyly + telecanthus + anogenital + renal malformations) in a female. STAR syndrome should be included in the **differential diagnosis of anorectal malformation in female neonates**, as highlighted in a clinical/genetic ARM case series ([PMID: 36062518](https://pubmed.ncbi.nlm.nih.gov/36062518/)).
- **Imaging:** Renal/urogenital ultrasound (hypoplasia, reflux, urogenital sinus), echocardiography (congenital heart disease), spinal imaging (tethered cord), and ophthalmologic examination (a full ophthalmic exam is warranted given reported ocular anomalies, [PMID: 26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/)).
- **Genetic testing (definitive):**
  - **Single-gene testing / sequencing of CCNQ (FAM58A)** detects intragenic point mutations (e.g., p.Trp217*).
  - **Whole-exome sequencing (WES)** has been diagnostic in practice — clinical WES identified the c.651G>A (p.Trp217*) variant across a pedigree ([PMID: 28322501](https://pubmed.ncbi.nlm.nih.gov/28322501/)).
  - **Chromosomal microarray / array CGH** detects Xq28 contiguous-gene deletions (array CGH was part of the original gene discovery and detects deletion cases, [PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/); [PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/)).
  - **X-inactivation studies** may help interpret expressivity in females.
- **Omics-based diagnostics:** Not routinely used; **ETS2 protein level** in patient cells is a research-grade functional readout, not a clinical test.
- **Clinical criteria:** No formal consensus diagnostic criteria exist; diagnosis rests on phenotype plus molecular confirmation of a pathogenic CCNQ variant/deletion.
- **Differential diagnosis:** Other causes of VACTERL/VATER-spectrum and anorectal malformations, other telecanthus/hypertelorism syndromes, and other ciliopathies with renal and limb involvement.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Highly **variable and genotype-dependent**. Patients with **intragenic point mutations are generally survivable** into adulthood (the original pedigrees include affected adult mothers). Patients with **large Xq28 deletions** can have the **lethal STAR plus** phenotype — one such female died at 6 weeks from respiratory failure ([PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/)).
- **Morbidity / function:** Determined by renal function, the extent of anorectal/urogenital reconstruction needed, and any neurodevelopmental, auditory, or visual involvement. Chronic kidney disease is the principal long-term risk.
- **Quality-of-life measures:** No formal instruments applied in the literature (ultra-rare disease).
- **Complications:** Chronic kidney disease, recurrent urinary tract infection (reflux), complications of anorectal and reconstructive surgery, and in lethal forms respiratory failure.
- **Prognostic factors:** **Variant type/size is the strongest prognostic factor** — point mutation (survivable) vs large contiguous-gene deletion (potentially lethal). Severity of renal and cardiac involvement also predicts outcome.

---

## 12. Treatment

**There is no disease-specific or curative therapy.** Management is entirely **supportive and malformation-directed**, requiring multidisciplinary care.

- **Surgical/interventional:** Correction of **toe syndactyly**, repair of **anorectal malformations** (anoplasty for anal stenosis/atresia), **urogenital reconstruction** (clitoromegaly, urogenital sinus), management of **vesicoureteral reflux**, **congenital heart disease** repair where indicated, and neurosurgical release of **tethered cord**. Suggested NCIT concepts: Surgical Procedure (NCIT:C15329), Reconstructive Surgery.
- **Supportive / rehabilitative:** Nephrology follow-up for renal function; audiology and ophthalmology management for sensory anomalies; developmental support where needed. Suggested NCIT: Supportive Care (NCIT:C15346).
- **Pharmacotherapy / advanced therapeutics:** **None disease-specific.** No approved drugs, gene therapy, cell therapy, RNA-based therapy, or targeted therapy exist. The molecular target (CDK10/Cyclin Q kinase complex) is not currently druggable for STAR, and because the defect is a developmental loss of function arising during organogenesis, postnatal pharmacologic restoration is not a realistic current option.
- **Experimental:** No registered clinical trials specific to STAR syndrome.
- **Personalized medicine / counseling:** Genotype (point mutation vs deletion) informs prognosis and counseling. Suggested NCIT: Genetic Counseling (NCIT:C15587).

---

## 13. Prevention

- **Primary prevention:** Not possible for de novo cases. For families with a known pathogenic CCNQ variant, **genetic counseling, prenatal testing, and preimplantation genetic testing (PGT)** are the available options to prevent recurrence.
- **Secondary prevention:** Early detection via prenatal imaging (renal anomalies, oligohydramnios) and cascade genetic testing of at-risk female relatives.
- **Tertiary prevention:** Prevent complications in affected individuals — renal protection, infection prophylaxis for reflux, and timely surgical correction to reduce long-term morbidity.
- **Counseling:** Genetic counseling is central: X-linked dominant inheritance with likely male lethality, variable expressivity in females, and recurrence-risk assessment. **NSGC/ACMG** frameworks and **GeneReviews**-style counseling apply.
- **Immunization / public health / environmental interventions:** Not applicable (non-infectious, non-environmental genetic disorder).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** The gene is conserved in mammals; **mouse (Mus musculus, NCBI Taxon 10090)** is the principal model species.
- **Orthologous genes:** Mouse *Ccnq* / *Fam58a* (Cyclin Q) and its partner *Cdk10*. The CDK10/Cyclin M(Q) module is evolutionarily conserved.
- **Natural disease in other species:** No naturally occurring STAR-syndrome equivalent is reported in companion animals or wildlife (no OMIA entry identified in this investigation). Veterinary relevance is limited to engineered mouse models.
- **Comparative biology:** The **CDK10-knockout mouse** recapitulates several features of CDK10-related human disease (growth retardation, skeletal defects, kidney and lung abnormalities) and, at the cellular level, **longer primary cilia** — mirroring the ciliary mechanism central to STAR syndrome ([PMID: 28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/)). This cross-species conservation of the ciliary phenotype supports evolutionary conservation of the disease mechanism.

---

## 15. Model Organisms

| Model | Type | Key phenotype | Relevance to STAR |
|---|---|---|---|
| **Cdk10-knockout mouse** (conditional/constitutive) | Mammalian, genetic | Postnatal death with severe growth retardation, skeletal defects, kidney and lung abnormalities; **MEFs develop longer cilia**; lipid-metabolic transcriptomic changes | Models the kinase-partner loss; recapitulates renal and ciliary phenotypes central to STAR ([PMID: 28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/)) |
| **STAR patient-derived fibroblasts** | Human, in vitro | **Increased ETS2 protein**; used to show loss of CDK10 binding | Direct patient-cell validation of the molecular mechanism ([PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/)) |
| **Recombinant CDK10/Cyclin Q complex** | In vitro biochemistry | Phosphorylates ETS2, PKN2, RNA Pol II CTD, c-MYC, RB1 | Defines the substrate repertoire of the complex ([PMID: 35291876](https://pubmed.ncbi.nlm.nih.gov/35291876/)) |

**Model characteristics.** The Cdk10-knockout mouse captures the **ciliary and renal** dimensions of the human disease and demonstrates the kinase's role in transducing signals at the primary cilium. **Limitations:** the mouse models the kinase (CDK10) rather than the cyclin (CCNQ), and knockout mice die postnatally, so they imperfectly model the female-limited, variably expressive human phenotype. No dedicated **Ccnq/Fam58a** mouse model of STAR syndrome was identified in this investigation, representing a clear gap. Resources: MGI (mouse), and patient-derived fibroblast lines in the primary literature.

---

## Mechanistic Model / Interpretation

STAR syndrome is best understood as a **cyclin-deficiency disorder that disables a developmental kinase module**. The unifying lesion is loss of the activating cyclin (Cyclin Q), which renders CDK10 inactive. From that single node, two experimentally supported branches explain the pleiotropic malformations:

1. A **transcription-factor branch**, in which failure to degrade ETS2 raises MAPK/ETS output — a plausible driver of developmental patterning defects.
2. A **ciliary/cytoskeletal branch**, in which loss of PKN2 phosphorylation destabilizes RhoA and the actin network, producing **over-elongated primary cilia**. The direct observation of dilated tubules and abnormal cilia in STAR patient kidney makes STAR a **ciliopathy-overlap syndrome** at the tissue level.

The nomenclature deserves emphasis for knowledge-base integrity: the gene is **CCNQ** (HGNC), published historically as **FAM58A**, encoding **Cyclin Q / Cyclin M (Q8N1B3)**. STAR syndrome (cyclin loss, X-linked dominant) must not be conflated with the **recessive CDK10-deficiency disorder** (kinase loss) — they are distinct conditions affecting the two halves of the same holoenzyme.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/) | FAM58A mutations cause STAR syndrome | **Foundational** — names the syndrome, identifies causal FAM58A/CCNQ at Xq28, establishes X-linked dominant inheritance and the cardinal tetrad |
| [24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/) | CDK10/Cyclin M controls ETS2 degradation; deficient in STAR | **Mechanism (Branch A)** — STAR mutants fail to bind CDK10; ETS2 accumulates in patient cells |
| [27104747](https://pubmed.ncbi.nlm.nih.gov/27104747/) | CDK10/Cyclin M regulates actin and ciliogenesis | **Mechanism (Branch B)** — PKN2/RhoA/actin axis, cilium elongation; dilated tubules and abnormal cilia in patient kidney |
| [35291876](https://pubmed.ncbi.nlm.nih.gov/35291876/) | Functional characterization of human Cdk10/Cyclin Q | **Nomenclature + substrates** — confirms Cyclin Q; adds RNA Pol II CTD, c-MYC, RB1; notes tumour-suppressor role |
| [28322501](https://pubmed.ncbi.nlm.nih.gov/28322501/) | Multigenerational pedigree; novel FAM58A variant | **Variant + spectrum** — p.Trp217* (c.651G>A); adds tethered cord, hearing loss; variable expressivity |
| [29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/) | STAR syndrome plus: lethal female form | **Spectrum** — Xq28 deletion, lethal phenotype (cleft lip/palate, omphalocele, cerebral malformations), death at 6 weeks |
| [26882209](https://pubmed.ncbi.nlm.nih.gov/26882209/) | Ocular manifestations of STAR | **Phenotype expansion** — eyelid prominences, madarosis, optic nerve hypoplasia in a mother–daughter pair |
| [28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/) | CDK10 mutations in humans and mice | **Model organism + comparative** — Cdk10-KO mouse recapitulates renal/ciliary phenotype; longer cilia; distinguishes the recessive CDK10 disorder |
| [36062518](https://pubmed.ncbi.nlm.nih.gov/36062518/) | Genetic approach to anorectal malformation | **Differential diagnosis** — STAR should be considered in female neonates with ARM |

**Direct supporting quotes (verified against abstracts):**
- "*…we found causative mutations in FAM58A on Xq28 in all affected individuals, suggesting an X-linked dominant inheritance pattern for this recognizable syndrome.*" ([PMID: 18297069](https://pubmed.ncbi.nlm.nih.gov/18297069/))
- "*We show that STAR syndrome-associated cyclin M mutants are unable to interact with CDK10.*" ([PMID: 24218572](https://pubmed.ncbi.nlm.nih.gov/24218572/))
- "*…kidney sections from a STAR patient display dilated renal tubules and abnormal, elongated cilia.*" ([PMID: 27104747](https://pubmed.ncbi.nlm.nih.gov/27104747/))
- "*She presented with cleft lip palate, omphalocele, and cerebral malformations… She died at 6 weeks from respiratory failure.*" ([PMID: 29088509](https://pubmed.ncbi.nlm.nih.gov/29088509/))
- "*…bi-allelic loss-of-function CDK10 mutations segregating with this disease… Cdk10-knockout MEFs developed longer cilia.*" ([PMID: 28886341](https://pubmed.ncbi.nlm.nih.gov/28886341/))

**Evidence-type mix:** human clinical case reports/series (18297069, 28322501, 29088509, 26882209, 36062518), human patient-cell + biochemical (24218572, 27104747, 35291876), and model organism (28886341). Population-genetics constraint data (gnomAD) provide computational support for LoF pathogenicity.

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease, small N.** All clinical knowledge derives from a handful of case reports and small pedigrees; no registries, natural-history studies, prevalence/incidence figures, or formal QoL data exist.
2. **No dedicated Ccnq/Fam58a animal model.** Mechanistic in-vivo evidence relies on the **CDK10-knockout mouse** (the kinase partner), not a cyclin-specific STAR model, leaving a gap in modeling the exact female-limited human condition.
3. **Mechanistic branches not fully integrated.** The relative contributions of the ETS2/MAPK branch versus the PKN2/RhoA/cilia branch to each specific malformation are not resolved; which malformations are ETS2-driven vs cilia-driven is inferred rather than demonstrated.
4. **Expressivity determinants unproven.** The role of X-inactivation skewing in modulating severity is plausible but not experimentally established.
5. **No therapeutics.** There is no targeted or curative treatment, and no clinical trials.
6. **Penetrance/male lethality are inferential.** Male lethality is inferred from the female-limited presentation and gnomAD constraint, not directly demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional *Ccnq/Fam58a* mouse (and/or zebrafish) model** to directly test which malformations arise from cyclin loss and to compare with the Cdk10-knockout phenotype.
2. **Patient-derived iPSC and organoid models** (kidney organoids, cloacal/urogenital models) to dissect tissue-specific ciliary vs ETS2/MAPK contributions and to serve as drug-screening platforms.
3. **Systematic X-inactivation analysis** across affected females correlating skewing with severity to test the expressivity hypothesis.
4. **Genotype–phenotype correlation study** aggregating all reported cases (point mutation vs deletion size) to formalize the prognostic rule that large Xq28 deletions predict the lethal STAR plus form.
5. **Establish an international STAR syndrome registry** to capture natural history, renal outcomes, surgical burden, and QoL.
6. **Pathway-rescue experiments** (e.g., ETS2 knockdown, RhoA restoration, or MAPK modulation) in patient cells/organoids to test whether targeting a single branch normalizes the ciliary and developmental phenotype — a prerequisite for any future therapeutic concept.

---

*Report compiled from 7 confirmed findings and 9 primary-literature sources across a 5-iteration autonomous investigation. Causal gene: **CCNQ** (FAM58A), encoding **Cyclin Q**, activating cyclin of **CDK10**.*


## Artifacts

- [OpenScientist final report](STAR_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](STAR_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:29088509` *(abstract only)*: "*She presented with cleft lip palate, omphalocele, and cerebral malformations… She died at 6 weeks from respiratory failure.*"
  - closest text in source: "She presented with cleft lip palate, omphalocele, and cerebral malformations not previously considered part of the phenotypic spectrum of this syndrome"
- `PMID:28886341` *(abstract only)*: "*…bi-allelic loss-of-function CDK10 mutations segregating with this disease… Cdk10-knockout MEFs developed longer cilia.*"
  - closest text in source: "Using homozygosity mapping, array CGH, and exome sequencing, we uncovered bi-allelic loss-of-function CDK10 mutations segregating with this disease"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010408` (2 mentions) - the report calls it "MONDO"; MONDO calls it **syndactyly-telecanthus-anogenital and renal malformations syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005929` (2 mentions) - the report calls it "Subcellular level:** **primary cilium"; GO calls it **cilium**, and lists "primary cilium" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.