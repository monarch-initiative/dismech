---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:59:16.789691'
end_time: '2026-10-31T19:24:42.730689'
duration_seconds: 1525.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: '"Hyperbiliverdinemia"'
  mondo_id: MONDO:0013595
  category: Mendelian
  causal_genes: BLVRA
  omim_id: OMIM:614156
  synonyms: green jaundice
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 10
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hyperbiliverdinemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hyperbiliverdinemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** "Hyperbiliverdinemia"
- **MONDO ID:** MONDO:0013595 (if available)
- **Causal gene(s):** BLVRA
- **OMIM:** OMIM:614156
- **Synonyms:** green jaundice
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **"Hyperbiliverdinemia"** covering all of the
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

# Hyperbiliverdinemia (Green Jaundice): A Comprehensive Disease Profile

**Disease:** Hyperbiliverdinemia (green jaundice) · **MONDO:** MONDO:0013595 · **OMIM:** 614156
**Causal gene:** **BLVRA** (biliverdin reductase A; HGNC:1062; NCBI Gene 644; gene MIM *109750; UniProt P53004; chr7p13, GRCh38 chr7:43,758,009–43,808,868 (+ strand); ENSG00000106605; canonical transcript ENST00000265523) · **Category:** Mendelian, autosomal recessive

---

## Summary

**Hyperbiliverdinemia**, also called **green jaundice**, is a rare autosomal-recessive inborn error of heme catabolism caused by **biallelic loss-of-function variants in *BLVRA***, the gene encoding **biliverdin reductase A (BVRα; EC 1.3.1.24)**. Under normal physiology, heme is degraded by heme oxygenase to the green pigment **biliverdin IXα**, which BVRα then reduces, using NADPH/NADH, to the yellow pigment **bilirubin IXα**. When BVRα is absent or non-functional, this final reduction step fails and biliverdin IXα accumulates in serum, urine, bile and milk, producing a characteristic green discoloration of body fluids and tissues ([PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/), [PMID: 27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/)).

The disease was defined molecularly by Nytofte and colleagues in 2011, who identified a **homozygous nonsense mutation c.214C>A (p.Ser44\*)** in *BLVRA* in two unrelated Inuit women from Greenland. Strikingly, the clinical phenotype — green jaundice — is **latent**: it becomes visible only when a superimposed **cholestasis / biliary obstruction** raises the metabolic flux through the heme-degradation pathway, and it resolves after the obstruction is surgically relieved ([PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/)). The causal allele is a **population-restricted founder variant** enriched in the Greenlandic Inuit, where it reaches ~1% homozygosity and ~4.5% heterozygosity ([PMID: 27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/)).

The condition is **biochemically benign**. *BLVRA* is **loss-of-function tolerant** in population databases (gnomAD pLI ≈ 0, observed/expected LoF = 0.67), heterozygous carriers are asymptomatic, and even homozygous individuals are healthy in the absence of cholestasis — the index family included unaffected homozygous siblings, indicating **reduced penetrance**. Management is directed at the **underlying cholestatic process**, not at the enzyme defect. Beyond its namesake reductase activity, BVRα is a well-characterized **"moonlighting" protein** acting as a Ser/Thr/Tyr kinase, scaffold, and transcription factor in insulin, MAPK/ERK and PKC signaling; interestingly, the complete human BVRα null is clinically mild, suggesting these non-canonical functions are either dispensable or redundant in humans.

---

## Key Findings

### Finding 1 — Hyperbiliverdinemia is caused by biallelic loss-of-function *BLVRA* variants

The defining report (Nytofte et al., 2011) studied two unrelated Inuit women from different geographical areas of Greenland who exhibited episodic green jaundice during biliary obstruction. Coding-sequence analysis of the biliverdin reductase alpha gene (*BLVRA*) detected three single-nucleotide changes — c.90G→A, c.214C→A and c.743A→C — predicting p.Ala3Thr, **p.Ser44X** and p.Gly220Gly, of which the **c.214C→A (p.Ser44X) nonsense allele** is the pathogenic driver ([PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/)). HPLC–MS/MS demonstrated **hypercholanaemia and high concentrations of biliverdin IXα in serum, urine, bile and milk**, with absent or only moderate hyperbilirubinemia; crucially, the **hyperbiliverdinaemia disappeared after surgical correction of the cholestasis**.

> *"Analysis of the coding sequence of the biliverdin reductase alpha (BVRα) gene (BLVRA) detected three single-nucleotide polymorphisms: c.90G→A, c.214C→A and c.743A→C, which result in p.Ala3Thr, p.Ser44X and p.Gly220Gly"* — [PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/)

> *"high-performance liquid chromatography tandem mass spectrometry showed hypercholanaemia and high concentrations of biliverdin IXα in serum, urine, bile and milk. Hyperbiliverdinaemia disappeared after surgical correction of the cholestasis"* — [PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/)

The segregation pattern supported autosomal-recessive inheritance with **reduced penetrance**: both parents of one patient were heterozygous, while a homozygous brother and the proband's homozygous sister were **unaffected** — consistent with the requirement for a second, cholestatic "hit" to unmask the phenotype. Functional confirmation came from in-vitro expression work showing the variant yields a dead enzyme:

> *"The mutation (c.214C>A) in BLVRA results in a non-functional enzyme (mutBVRα). Consequently, homozygous carriers suffering from cholestasis develop green jaundice."* — [PMID: 27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/)

**Evidence type:** human clinical + in-vitro functional. **Confidence:** High.

### Finding 2 — The p.Ser44\* allele is a Greenlandic Inuit founder variant

Gonzalez-Sanchez et al. (2016) screened 311 individuals in Greenland and found the mutant *BLVRA* allele at appreciable frequency — approximately **1% homozygous (a/a) and 4.5% heterozygous (A/a)**. Together with the observation that the two index cases came from different geographical areas of Greenland, this is consistent with a **population-specific founder allele** rather than recurrent mutation.

> *"a screening of the mut-BLVRA allele (a) in 311 individuals in Greenland revealed that this SNP was relatively frequent in the Inuit population studied (1% a/a and 4.5% A/a)"* — [PMID: 27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/)

**Evidence type:** human population genetics. **Confidence:** High (single population).

### Finding 3 — BVRα is a moonlighting protein (reductase + kinase + scaffold + transcription factor)

Human biliverdin reductase (hBVR / BVRα, EC 1.3.1.24) is a dual-cofactor (NADPH/NADH) oxidoreductase that also moonlights as a **Ser/Thr/Tyr kinase, scaffold/anchor protein, and bZip transcription factor**. It acts as an **upstream activator of the insulin/IGF-1 signaling pathway** and of multiple **PKC isoforms**, is required for ERK1/2 activation and nucleocytoplasmic shuttling, and forms an **hBVR–PKCδ–ERK2 ternary complex** essential for ERK2-mediated gene activation ([PMID: 22419908](https://pubmed.ncbi.nlm.nih.gov/22419908/), [PMID: 22065579](https://pubmed.ncbi.nlm.nih.gov/22065579/), [PMID: 17919068](https://pubmed.ncbi.nlm.nih.gov/17919068/)).

> *"hBVR is a Ser/Thr/Tyr-kinase, a scaffold protein, a transcription factor, and an intracellular transporter of gene regulators. hBVR is an upstream activator of the insulin/IGF-1 signaling pathway and of protein kinase C (PKC) kinases"* — [PMID: 22419908](https://pubmed.ncbi.nlm.nih.gov/22419908/)

Mouse genetics confirm that catalytic and non-catalytic roles are **separable**: catalytic-dead *Blvra* missense mutants (G17A, E97A) retain non-canonical functions while losing ~80–95% of oxidoreductase activity (see Finding 5). The clinical mildness of the human p.Ser44\* null — which removes **all** of these functions — indicates that, in humans, loss of BVRα's moonlighting roles is tolerated, at least under normal environmental conditions.

**Evidence type:** in-vitro biochemistry + model organism. **Confidence:** High for biochemistry; interpretation of human tolerance is inferred.

### Finding 4 — *BLVRA* is loss-of-function tolerant; the Inuit allele is essentially absent from gnomAD

gnomAD v4 constraint metrics for *BLVRA* (ENSG00000106605; canonical transcript ENST00000265523; chr7p13, ~43.78–43.81 Mb, GRCh38) show the gene is **not haploinsufficient**: pLI = 1.2×10⁻⁵, observed/expected LoF = **0.67** (90% CI 0.48–0.96), 22 observed vs 32.8 expected LoF alleles, LOEUF upper bound 0.96. This LoF-tolerant profile is fully consistent with the asymptomatic status of heterozygous carriers and the benign nature of the homozygous state.

The patient nonsense allele (legacy c.214C>A, p.Ser44\*; MANE-equivalent c.131C>A at chr7:43,788,022) is **not observed in gnomAD r4**, as expected for a geographically restricted founder variant. The same codon carries only ultra-rare missense alleles (c.131C>T p.Ser44Leu, AF ≈ 7×10⁻⁷; c.131C>G p.Ser44Trp), and all ~19 catalogued *BLVRA* nonsense/LoF alleles are singleton or ultra-rare (AF < 7×10⁻⁵).

**Evidence type:** computational / population database. **Confidence:** High.

### Finding 5 — Mouse models separate catalytic from moonlighting roles and reveal a bilirubin–malaria axis

Mesquita et al. generated knock-in mice carrying **G17A** (in the NAD(P)H-binding motif) and **E97A** (in the reductase motif) missense mutations that reduce BVRA oxidoreductase activity by ~95% and ~80–90% respectively, while sparing non-catalytic functions ([PMID: 41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/), [PMID: 42199930](https://pubmed.ncbi.nlm.nih.gov/42199930/)). These hypomorphs demonstrate that BVRA's **anti-malarial effect relies on its catalytic activity** and define a **minimal bilirubin threshold** required for parasite control and malaria resolution. Complementary work established that the bilirubin produced by BVRA is a **metabolite-based resistance mechanism against *Plasmodium***, reframing jaundice as an adaptive antimalarial response ([PMID: 40504905](https://pubmed.ncbi.nlm.nih.gov/40504905/), [PMID: 40060532](https://pubmed.ncbi.nlm.nih.gov/40060532/)).

> *"we generated mice harboring G17A and E97A missense mutations in its NAD(P)H-binding and reductase motifs"* — [PMID: 42199930](https://pubmed.ncbi.nlm.nih.gov/42199930/)

> *"To disentangle the contribution of BVRA catalytic activity over its non-canonical functions we generated..."* — [PMID: 41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/)

At the cellular level, CRISPR-Cas9 knockout of *Blvra* in mouse hepa1c1c7 hepatocytes produced **increased ROS, lipid accumulation, and reduced mitochondrial biogenesis and respiration**, highlighting a cytoprotective, antioxidant role for the BVRα/bilirubin axis in liver cells ([PMID: 31422074](https://pubmed.ncbi.nlm.nih.gov/31422074/)).

> *"The loss of BVRA resulted in the reduction of mitochondria number, decreased expression of markers of mitochondrial biogenesis, uncoupling, oxidation, and fusion, which paralleled reduced mitochondrial oxygen consumption. BVRA KO cells exhibited increased levels of ROS"* — [PMID: 31422074](https://pubmed.ncbi.nlm.nih.gov/31422074/)

**Evidence type:** model organism (mouse) + in-vitro. **Confidence:** High.

### Finding 6 — Gene identity and identifiers independently verified

NCBI Gene (ID 644) / mygene.info confirm: symbol **BLVRA**; name "biliverdin reductase A"; **HGNC:1062**; gene OMIM **\*109750**; cytoband **7p13**; GRCh38 chr7:43,758,009–43,808,868 (+ strand); Ensembl **ENSG00000106605**; UniProt **P53004**. The NCBI RefSeq summary states the product *"catalyze[s] the conversion of biliverdin to bilirubin in the presence of NADPH or NADH"* and that *"Mutations in this gene are associated with hyperbiliverdinemia,"* corroborating the causal-gene assignment for disease OMIM 614156 / MONDO:0013595.

**Evidence type:** reference database. **Confidence:** High.

### Finding 7 — p.Ser44\* ablates the NADPH-binding Rossmann fold and the entire catalytic/substrate domain

UniProt P53004 (BVRα, 296 aa) annotates a **bipartite architecture**: an N-terminal **Rossmann-fold NADPH-binding domain** with cofactor-contact residues at 16–19, **44–46**, 77–80 and 98, and a C-terminal **substrate-binding domain** bearing a structural Zn²⁺ site (residues 280, 281, 292, 293). Residue 44 (Ser) lies **within** the NADP⁺-binding segment 44–46, immediately following β-strand 37–43. The nonsense variant **p.Ser44\* truncates the protein at codon 44**, deleting ~253 of 296 residues (**~85% of the protein**) — removing most of the cofactor site, the catalytic core, and the entire C-terminal substrate-binding/Zn domain. This structural amputation fully explains the observed null-enzyme phenotype. The human structure is available as PDB 2H63; pathway references KEGG hsa:644 and Reactome R-HSA-189483 (Heme degradation).

> *"The mutation (c.214C>A) in BLVRA results in a non-functional enzyme (mutBVRα)"* — [PMID: 27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/)

**Evidence type:** computational / structural annotation. **Confidence:** High.

### Finding 8 — The NADP(H)-binding residues and Ser44 are strictly conserved across mammals

Alignment of N-terminal sequences of BVRα orthologs — human (P53004, 296 aa), mouse (Q9CY64, 295 aa) and rat (P46844, 295 aa) — shows the dinucleotide-binding Rossmann fingerprint "F-G-V-V-V-V-G-V-G-R-A-G-S-V-R" (human residues ~9–23; GxGxxG motif at Gly15/Gly17/Gly20) is **identical across all three species**, and the cofactor-contact segment at positions 43–46 ("V-S-R-R", containing the disease residue **Ser44** plus Arg45/Arg46) is conserved. This strict conservation underscores the functional importance of the exact residue destroyed by the p.Ser44\* nonsense allele. (The bovine accession Q58DM8 is a divergent/mis-annotated mitochondrial sequence and was excluded.)

**Evidence type:** computational / comparative sequence. **Confidence:** High.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *BLVRA* loss-of-function** (homozygous nonsense c.214C>A / p.Ser44\*) **leads to** a truncated transcript/protein terminating at codon 44.
2. Truncation at Ser44 **results in** deletion of ~85% of BVRα, including the NADPH-binding Rossmann fold, catalytic core and substrate-binding/Zn domain (**inferred** from UniProt domain annotation + structure; functional null confirmed in vitro).
3. The absent catalytic BVRα **leads to** failure of the terminal reaction of heme catabolism: **biliverdin IXα → bilirubin IXα (NADPH-dependent reduction) does not occur**.
4. Under **baseline heme turnover**, flux is low enough that residual biliverdin is cleared and the patient remains **clinically silent** (explains reduced penetrance / asymptomatic homozygotes).
5. A **superimposed cholestasis / biliary obstruction** (second hit) **increases** heme-degradation flux and **impairs biliary excretion**, which **results in** accumulation of **biliverdin IXα in serum, urine, bile and milk** → visible **green jaundice**, with only mild/absent hyperbilirubinemia (because the downstream bilirubin cannot be formed).
6. **Relief of the obstruction** (surgical) **reverses** the biliverdin accumulation and the green jaundice resolves.

Branch (model-organism / mechanistic context, not required for the human phenotype):
- Loss of catalytic BVRα also **reduces bilirubin**, a potent antioxidant. In cells this **leads to** increased ROS, lipid accumulation and mitochondrial dysfunction ([PMID: 31422074](https://pubmed.ncbi.nlm.nih.gov/31422074/)); in mice it **lowers** the bilirubin pool below a **threshold needed for anti-malarial parasite control** ([PMID: 41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/), [PMID: 42199930](https://pubmed.ncbi.nlm.nih.gov/42199930/)). These consequences are subclinical in human carriers under normal conditions.

### Pathway schematic

```
      Heme
        │  heme oxygenase (HMOX1/2) + O2, NADPH
        ▼
  Biliverdin IXα  (GREEN)  ──── CO + Fe²⁺ released
        │
        │  BILIVERDIN REDUCTASE A (BVRα / BLVRA)  ← DEFECTIVE in disease
        │  NADPH/NADH-dependent reduction
        ▼
   Bilirubin IXα  (YELLOW, antioxidant)
        │  UGT1A1 glucuronidation
        ▼
  Conjugated bilirubin → bile → gut

  In disease:  BVRα absent  ⇒  reaction blocked
               + cholestasis (↑flux, ↓excretion)
               ⇒  Biliverdin IXα accumulates  ⇒  GREEN JAUNDICE
```

### Section-by-section synthesis

| Template section | Summary for Hyperbiliverdinemia |
|---|---|
| **1. Disease info** | Rare AR inborn error of heme catabolism; green jaundice. IDs: OMIM 614156, MONDO:0013595, gene OMIM *109750. Disease-level aggregated resources + ~2 index patients. |
| **2. Etiology** | Monogenic: biallelic *BLVRA* LoF. "Risk factor" that unmasks phenotype = **cholestasis/biliary obstruction**. Founder allele in Inuit. No environmental cause of the gene defect. |
| **3. Phenotypes** | **Green discoloration of serum/urine/bile/milk (biliverdinuria)**, episodic, triggered by cholestasis, reversible; mild/absent hyperbilirubinemia. Onset tied to intercurrent cholestasis (adult cases reported). HPO: Jaundice (HP:0000952), Cholestasis (HP:0001396), Abnormal urine color. Mild QoL impact. |
| **4. Genetics** | Causal gene **BLVRA** (HGNC:1062). Pathogenic variant c.214C>A / **p.Ser44\*** (nonsense, LoF, null enzyme). Also exonic/biliverdinuria variants reported ([PMID: 39766828](https://pubmed.ncbi.nlm.nih.gov/39766828/)). LoF-tolerant gene (gnomAD). No known modifier genes beyond the cholestasis trigger. |
| **5. Environment** | No toxin/infection causes the gene defect; **cholestasis of any cause** (gallstones, obstruction, pregnancy) is the environmental trigger of visible disease. |
| **6. Mechanism** | See causal chain above. Pathway: heme degradation (Reactome R-HSA-189483). GO: biliverdin reductase (NAD(P)H) activity (GO:0004074), heme catabolic process (GO:0042167). |
| **7. Anatomy** | Primary: **liver / hepatobiliary system** (UBERON:0002107 liver; UBERON:0002394 bile duct). Systemic pigment deposition (serum, urine, milk). Cell type: hepatocyte (CL:0000182). Subcellular: cytosol (GO:0005829). |
| **8. Temporal** | Episodic/fluctuating, tied to cholestatic episodes; reversible; otherwise lifelong latent trait. |
| **9. Inheritance/population** | Autosomal recessive; **reduced penetrance** (needs cholestasis). Founder allele in Greenlandic Inuit (~1% a/a, ~4.5% carriers). Both sexes; index cases female (coincidental). |
| **10. Diagnostics** | Green serum/urine; **HPLC-MS/MS identifies biliverdin IXα**; disproportionately low bilirubin relative to green color. Confirm by *BLVRA* sequencing. Differential: other causes of green/dark urine, cholestatic jaundice. |
| **11. Prognosis** | **Benign**; biliverdinemia reverses with relief of cholestasis. No excess mortality attributable to the enzyme defect. |
| **12. Treatment** | Treat the **underlying cholestasis** (e.g., surgical correction of obstruction). No enzyme-directed therapy needed. NCIT: surgical bile-duct decompression / cholestasis management (supportive). |
| **13. Prevention** | Genetic counseling / carrier awareness in Inuit populations; no vaccine/public-health measure applicable. |
| **14. Other species** | Orthologs: mouse *Blvra* (NCBI Gene 109778), rat *Blvra* (P46844). No well-documented natural companion-animal disease; mouse models engineered. |
| **15. Model organisms** | Mouse: CRISPR KO (hepatocytes), catalytic-dead knock-ins G17A / E97A. Recapitulate loss of catalysis, ↑ROS, bilirubin-threshold biology; do not reproduce the cholestasis-dependent human green jaundice directly. |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/) | Homozygous nonsense c.214C>A in *BLVRA* → biliverdin accumulation during cholestasis | Human clinical | **Defining paper** — identifies p.Ser44\*, biliverdin IXα accumulation, reversibility, AR inheritance with reduced penetrance (Findings 1, 2) |
| [27387768](https://pubmed.ncbi.nlm.nih.gov/27387768/) | Protective role of biliverdin; non-functional mutBVRα | In-vitro functional + population | Confirms null enzyme; documents Inuit founder allele frequencies (Findings 1, 2, 7) |
| [22419908](https://pubmed.ncbi.nlm.nih.gov/22419908/) | BVR regulates the three PKC classes | In-vitro biochemistry | Moonlighting kinase/scaffold/TF roles (Finding 3) |
| [22065579](https://pubmed.ncbi.nlm.nih.gov/22065579/) | hBVR–PKCδ–ERK2 ternary complex | In-vitro biochemistry | ERK2 signaling scaffold function (Finding 3) |
| [17919068](https://pubmed.ncbi.nlm.nih.gov/17919068/) | BVR at MAPK/PI3K cross-talk | In-vitro biochemistry | bZip transcription-factor + kinase roles (Finding 3) |
| [31422074](https://pubmed.ncbi.nlm.nih.gov/31422074/) | CRISPR *Blvra* KO → oxidative stress, lipid accumulation | Model organism / in-vitro | Cellular consequences of BVRA loss (Finding 5) |
| [41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/) | BVR catalytic activity essential for malaria resistance | Model organism (mouse) | Catalytic-dead knock-ins; bilirubin–malaria axis (Finding 5) |
| [42199930](https://pubmed.ncbi.nlm.nih.gov/42199930/) | Hypomorphic *Blvra* defines bilirubin antimalarial threshold | Model organism (mouse) | G17A/E97A alleles, bilirubin threshold (Finding 5) |
| [40504905](https://pubmed.ncbi.nlm.nih.gov/40504905/) / [40060532](https://pubmed.ncbi.nlm.nih.gov/40060532/) | A metabolite-based resistance mechanism against malaria | Model organism | Bilirubin as antimalarial metabolite (Finding 5 context) |
| [39766828](https://pubmed.ncbi.nlm.nih.gov/39766828/) | Biliverdinuria caused by exonic variant | Human clinical | Additional *BLVRA* variant beyond the Inuit founder allele (Section 4) |
| [26146841](https://pubmed.ncbi.nlm.nih.gov/26146841/) | Genetic modifiers of neonatal hyperbilirubinemia (incl. *BLVRA*) | Human association | Context for bilirubin-pathway genetics (distinct phenotype) |
| [27897348](https://pubmed.ncbi.nlm.nih.gov/27897348/) | Active-site serine of BLVR**B** (IXβ reductase) | In-vitro / structural | Comparator paralog (BLVRB ≠ BLVRA); illustrates serine criticality (Finding 7 context) |
| [14694903](https://pubmed.ncbi.nlm.nih.gov/14694903/) | Conserved *Blvra* segment mouse vs human | Comparative genomics | Ortholog/synteny context (Finding 8) |

**Note on paralog disambiguation:** *BLVRB* (biliverdin reductase B, IXβ reductase) is a distinct gene; the Ser111Leu BLVRB loss-of-function affecting hematopoiesis ([PMID: 27897348](https://pubmed.ncbi.nlm.nih.gov/27897348/)) is a **different disease** and should not be conflated with BLVRA-driven hyperbiliverdinemia.

---

## Supported and Refuted Hypotheses

- **Supported:** Hyperbiliverdinemia (MONDO:0013595, OMIM 614156) is caused by biallelic LoF in *BLVRA* (not a look-alike gene). The p.Ser44\* nonsense allele produces a null enzyme by truncating the NADPH-binding and catalytic domains. The allele is an Inuit founder variant. The phenotype requires a cholestatic second hit and is reversible. *BLVRA* is LoF-tolerant, explaining the benign course.
- **No hypotheses were refuted** — the investigation was confirmatory/verificational, with all 8 findings corroborated across independent databases and primary literature.

---

## Limitations and Knowledge Gaps

- **Extremely small clinical series.** The human disease is defined essentially by two index patients plus family members from one population ([PMID: 21278388](https://pubmed.ncbi.nlm.nih.gov/21278388/)), with a small number of additional biliverdinuria reports ([PMID: 39766828](https://pubmed.ncbi.nlm.nih.gov/39766828/)). Prevalence outside Greenland is unknown.
- **Penetrance / trigger not quantified.** The dependence on cholestasis is clear qualitatively, but the proportion of homozygotes who ever manifest, and the threshold of cholestasis required, are not established.
- **Natural history / long-term outcomes** in homozygotes (e.g., subtle effects of lifelong low bilirubin on oxidative stress, metabolic or infectious risk) are uncharacterized in humans; the mouse data ([PMID: 31422074](https://pubmed.ncbi.nlm.nih.gov/31422074/), [PMID: 41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/)) raise hypotheses not yet tested clinically.
- **Moonlighting-function relevance in humans.** Despite extensive in-vitro evidence that BVRα scaffolds insulin/PKC/ERK signaling ([PMID: 22419908](https://pubmed.ncbi.nlm.nih.gov/22419908/)), human null individuals are clinically mild — the physiological importance of these non-canonical roles in people remains unresolved.
- **No treatment trials** — not applicable given benign course; no enzyme-replacement or gene-therapy need.
- **Allelic spectrum** is narrow; whether other *BLVRA* LoF genotypes produce identical phenotypes is largely untested.

---

## Proposed Follow-up Experiments / Actions

1. **Expand carrier/homozygote screening** in Greenlandic Inuit and related Arctic populations to quantify penetrance and natural history, correlating genotype with episodes of cholestasis and bilirubin/biliverdin levels.
2. **Targeted metabolomics (HPLC-MS/MS)** panel for biliverdin IXα as a confirmatory diagnostic in any patient presenting with green serum/urine and disproportionately low bilirubin — formalize as a differential-diagnosis workflow.
3. **Deep phenotyping of homozygotes under metabolic/oxidative challenge** to test whether the mouse-derived phenotypes (↑ROS, lipid accumulation, mitochondrial dysfunction, altered infection susceptibility) have human correlates.
4. **Epidemiological link to malaria/infection resistance:** given the mouse bilirubin–malaria threshold data ([PMID: 41497634](https://pubmed.ncbi.nlm.nih.gov/41497634/), [PMID: 42199930](https://pubmed.ncbi.nlm.nih.gov/42199930/)), investigate whether *BLVRA* LoF or low-bilirubin genotypes modulate human infection outcomes.
5. **Functional characterization of additional *BLVRA* alleles** (e.g., the exonic biliverdinuria variant, [PMID: 39766828](https://pubmed.ncbi.nlm.nih.gov/39766828/)) by in-vitro expression, to map the allelic spectrum and genotype–phenotype relationships.
6. **Structural modeling / AlphaFold confirmation** of the truncated p.Ser44\* product versus PDB 2H63 to formally document loss of the Rossmann and substrate domains (Finding 7).

---

*Report compiled from 8 confirmed findings and 16 reviewed papers across 5 investigation iterations. Evidence is predominantly human clinical (founding disease description), supplemented by in-vitro biochemistry, mouse model organism studies, and reference/population databases.*


## Artifacts

- [OpenScientist final report](Hyperbiliverdinemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hyperbiliverdinemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

9 of 10 terms resolved to a current term; the rest could not be looked up either way.