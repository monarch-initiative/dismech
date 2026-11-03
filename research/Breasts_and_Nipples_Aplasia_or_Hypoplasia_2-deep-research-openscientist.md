---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T23:36:08.743133'
end_time: '2026-10-21T00:26:00.518572'
duration_seconds: 2991.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Breasts and Nipples Aplasia or Hypoplasia 2
  mondo_id: MONDO:0014450
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
citation_count: 9
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 13
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Breasts_and_Nipples_Aplasia_or_Hypoplasia_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Breasts_and_Nipples_Aplasia_or_Hypoplasia_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Breasts and Nipples Aplasia or Hypoplasia 2
- **MONDO ID:** MONDO:0014450 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Breasts and Nipples Aplasia or Hypoplasia 2** covering all of the
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

# Breasts and Nipples Aplasia or Hypoplasia 2 (BNAH2) — Comprehensive Disease Report

**MONDO:** MONDO:0014450 · **OMIM:** 616001 · **Gene:** *PTPRF* (LAR) · **Inheritance:** Autosomal recessive · **Category:** Mendelian, ultra-rare

---

## Summary

**Breasts and Nipples Aplasia or Hypoplasia 2 (BNAH2)** is an ultra-rare, congenital, autosomal recessive disorder of nipple-areola and breast development caused by **biallelic loss-of-function variants in *PTPRF***, the gene encoding the LAR (leukocyte common antigen-related) receptor-type protein tyrosine phosphatase. The condition was molecularly delineated in a single consanguineous Israeli Arab family in which three affected children across two branches of the pedigree carried a homozygous frameshift mutation in *PTPRF*, identified by SNP-array homozygosity mapping and candidate gene sequencing ([PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)). The phenotype is essentially isolated — a spectrum ranging from unilateral hypothelia (hypoplastic nipple) to bilateral athelia (absent nipple) with breast aplasia/hypoplasia, accompanied by a characteristic eyebrow shape, and no other consistently associated congenital or ectodermal anomalies.

Mechanistically, *PTPRF*/LAR is a transmembrane receptor tyrosine phosphatase that localizes to adherens junctions and participates in the regulation of epithelial cell–cell contacts, peptide growth-factor signaling, and the canonical Wnt pathway. Loss of LAR phosphatase activity is inferred to disrupt epithelial adhesion and signaling during development of the mammary ridge (milk line), producing the nipple and breast defect. This human causality is strongly corroborated by the mouse model: *Ptprf*(LAR)-deficient female mice develop normally but display impaired terminal differentiation of mammary alveoli at late pregnancy and a resulting lactation defect, demonstrating a conserved, essential role for LAR in mammary gland development and function ([PMID: 9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/)).

Clinically, BNAH2 carries an **excellent prognosis** with normal lifespan and no systemic involvement; the primary impacts are cosmetic, functional (inability to breastfeed in affected females), and psychosocial. There is **no disease-modifying or pharmacologic therapy**; management is reconstructive (breast and nipple-areola reconstruction via prosthetic, autologous, or fat-grafting techniques) and supportive. Because disease arises almost exclusively from shared ancestral (founder) homozygosity in consanguineous unions, prevention centers on **genetic counseling, carrier/cascade testing, and prenatal or preimplantation genetic options**. The disease is distinguished from the far more common *syndromic* causes of athelia/amastia — ulnar-mammary syndrome (*TBX3*), TP63-related ectodermal dysplasias, scalp-ear-nipple (Finlay-Marks) syndrome (*KCTD1*), and KMT2D-related disorder — by its isolated nature and recessive inheritance.

---

## Key Findings

### Finding 1 — BNAH2 is isolated congenital athelia/breast hypoplasia caused by biallelic *PTPRF* loss-of-function

The disease entity **MONDO:0014450** resolves to "breasts and/or nipples, aplasia or hypoplasia of, 2" (BNAH2), with cross-references to **OMIM:616001**, **GARD:0016044**, and **MedGen/UMLS C4014918**. The molecular cause was established by Borck and colleagues in 2014, who studied three children (one girl, two boys) from two branches of an extended consanguineous Israeli Arab family. Using **homozygosity mapping after SNP-array genotyping followed by candidate-gene sequencing**, they identified a **homozygous frameshift mutation in *PTPRF*** as the likely cause of the nipple anomalies.

> *"Using homozygosity mapping after single nucleotide polymorphism (SNP) array genotyping and candidate gene sequencing we identified a homozygous frameshift mutation in PTPRF as the likely cause of nipple anomalies in this family."* — [PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)

The affected individuals "presented with a spectrum of nipple anomalies ranging from unilateral hypothelia to bilateral athelia but no other consistently associated anomalies except a characteristic eyebrow shape," establishing both the **phenotypic spectrum** and the **essentially isolated (non-syndromic)** nature of the condition. This finding anchors the entire disease entry: BNAH2 is a Mendelian, recessive, developmental defect of the nipple-areola complex and breast.

### Finding 2 — Mechanism: *PTPRF*/LAR regulates nipple/mammary epithelial development via adherens junctions and Wnt signaling

*PTPRF* encodes the **LAR receptor-type protein tyrosine phosphatase**, which localizes to adherens junctions and regulates epithelial cell–cell contacts, peptide growth-factor signaling, and the canonical Wnt pathway.

> *"PTPRF encodes a receptor-type protein phosphatase that localizes to adherens junctions and may be involved in the regulation of epithelial cell-cell contacts, peptide growth factor signaling, and the canonical Wnt pathway."* — [PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)

The protein architecture comprises an extracellular domain of Ig-like plus fibronectin type-III repeats (cell-adhesion-molecule-like) and two intracellular PTP (protein tyrosine phosphatase) domains ([PMID: 9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/)). Population-genetic constraint data (gnomAD, GRCh38) indicate that *PTPRF* is **strongly intolerant to heterozygous loss-of-function**: pLI ≈ 1.0, LOEUF (observed/expected LoF upper bound) ≈ 0.36, LoF observed/expected ≈ 0.29, LoF-Z = 8.5, missense-Z = 4.6. This constraint is notable because BNAH2 is recessive — heterozygous carriers are unaffected for the nipple phenotype, yet complete LoF is apparently under strong purifying selection, implying essential biological roles beyond the breast.

### Finding 3 — Mouse model: *Ptprf*(LAR)-deficient females show impaired alveolar differentiation and a lactation defect

Schaapveld et al. (1997) generated mice lacking both LAR phosphatase domains. **LAR⁻/⁻ mice develop and grow normally with no appreciable histological abnormalities**, but pups of LAR⁻/⁻ females showed abnormal neonatal death. The mammary glands of LAR⁻/⁻ females were **incapable of delivering milk** owing to impaired terminal differentiation of alveoli at late pregnancy; the glands failed to switch to a lactational state and underwent rapid postpartum involution. Wild-type LAR expression is pregnancy-regulated, peaking around day 16 of gestation.

> *"Mammary glands of LAR-/- females were incapable of delivering milk due to an impaired terminal differentiation of alveoli at late pregnancy."* — [PMID: 9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/)

This model provides strong cross-species corroboration that *PTPRF*/LAR is required for mammary gland differentiation and function, directly supporting the inferred human causal mechanism. (Note the species difference: the mouse phenotype is predominantly a functional lactation defect, whereas the human phenotype is a structural nipple/breast developmental defect — see Limitations.)

### Finding 4 — Phenotype spectrum: congenital, bilateral-or-asymmetric athelia/hypothelia and breast aplasia/hypoplasia with a characteristic eyebrow shape

Borck et al. describe three affected children with a spectrum from unilateral hypothelia to bilateral athelia and absence of the nipple-areola complex, plus a characteristic eyebrow shape, with **no other consistently associated congenital or ectodermal anomalies**. The defect is present from birth (congenital) and non-progressive.

**HPO term mapping (verified via OLS/HP):**

| Phenotype | HPO term |
|---|---|
| Absent nipple / athelia | HP:0002561 |
| Aplasia/Hypoplasia of the nipples | HP:0006709 |
| Hypoplastic nipples | HP:0002557 |
| Hypoplastic areola | HP:0100853 |
| Breast aplasia | HP:0100783 |
| Aplasia/Hypoplasia of the breasts | HP:0010311 |
| Breast hypoplasia | HP:0003187 |
| Unilateral breast hypoplasia | HP:0012813 |
| Bilateral breast hypoplasia | HP:0012814 |
| Abnormal eyebrow morphology | HP:0000534 |

> *"who presented with a spectrum of nipple anomalies ranging from unilateral hypothelia to bilateral athelia but no other consistently associated anomalies except a characteristic eyebrow shape"* — [PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)

Laterality is variable (unilateral to bilateral; asymmetric expression documented within the same family), indicating **variable expressivity** despite high penetrance in homozygotes.

### Finding 5 — Differential diagnosis: BNAH2 (*PTPRF*) vs. syndromic causes of athelia/amastia

Athelia/amastia is usually *syndromic*. Distinguishing BNAH2 (isolated, autosomal recessive, *PTPRF*) from the major syndromic differentials is clinically critical:

| Condition | Gene / Inheritance | Distinguishing features (absent in BNAH2) |
|---|---|---|
| **Ulnar-mammary syndrome (UMS)** | *TBX3* haploinsufficiency / AD | Ulnar ray defects, apocrine/genital anomalies, delayed puberty/hypogonadism, pituitary hypoplasia |
| **TP63-related disorders (LMS/EEC/AEC)** | *TP63* / AD | Ectrodactyly/split-hand-foot, cleft lip/palate, lacrimal duct stenosis, nail/dental anomalies, ectodermal dysplasia |
| **Scalp-ear-nipple (Finlay-Marks) syndrome** | *KCTD1* / AD | Aplasia cutis of scalp, prominent/malformed ears; recurrent p.(Ala30Glu), p.(Pro31Leu) |
| **KMT2D missense (non-Kabuki)** | *KMT2D* / de novo | Choanal atresia, hypoparathyroidism, short stature, interstitial lung disease |
| **BNAH2** | ***PTPRF*** / **AR** | **Isolated nipple/breast defect + characteristic eyebrow; none of the above** |

> *"Ulnar-mammary syndrome (UMS) is characterized by ulnar defects, and nipple or apocrine gland hypoplasia, caused by TBX3 haploinsufficiency."* — [PMID: 30550377](https://pubmed.ncbi.nlm.nih.gov/30550377/)

> *"limb mammary syndrome (LMS), an autosomal dominant inherited disorder characterized by ectrodactyly, hypoplasia of mammary-gland and nipple, lacrimal duct stenosis, nail dysplasia, dental anomalies, cleft palate and/or cleft lip"* — [PMID: 32067224](https://pubmed.ncbi.nlm.nih.gov/32067224/)

The KMT2D phenotypic expansion is a particularly important mimic because it includes athelia: *"including athelia (absent nipples), choanal atresia, hypoparathyroidism, delayed or absent pubertal development, and extreme short stature"* ([PMID: 32083401](https://pubmed.ncbi.nlm.nih.gov/32083401/)). BNAH2 is distinguished by the **absence** of limb, ectodermal, scalp, apocrine, endocrine, and facial-dysmorphism features, and by its recessive inheritance in a consanguineous setting.

### Finding 6 — Management is reconstructive/supportive; no disease-modifying therapy

No gene-directed or pharmacologic therapy exists for *PTPRF*-related athelia. Management is **surgical/cosmetic and psychosocial**. A systematic review of congenital breast anomaly reconstruction (Dreifuss et al., 2014) quantified the modalities used across 54 individual reconstructions:

| Reconstruction modality | Patients | Percentage |
|---|---|---|
| Prosthetic (implant) | 19 | 35.2% |
| Autologous | 19 | 35.2% |
| Autologous + prosthesis | 15 | 27.8% |

> *"Prosthetic and autologous reconstructions were equally represented (19 patients each, 35.2%; Table 2). Autologous reconstruction with prosthesis was slightly less common (15 patients, 27.8%)."* — [PMID: 23896162](https://pubmed.ncbi.nlm.nih.gov/23896162/)

Mean age at reconstruction was 27.6 years (range 13–54); the nipple-areola complex was addressed in 36 cases, with the majority (66.7%) not reconstructed. **Fat grafting** is a documented option for congenital amastia ([PMID: 33830564](https://pubmed.ncbi.nlm.nih.gov/33830564/)). Timing considerations generally defer reconstruction until breast maturity/adolescence. Relevant NCIT clinical-intervention concepts include breast reconstruction, breast implant, autologous tissue reconstruction, and autologous fat transfer/grafting.

### Finding 7 — Anatomy, cell types, and molecular annotations (UBERON/CL/GO/ortholog terms)

**Affected anatomical structures** (congenital developmental defect of the milk line / mammary ridge):

| Structure | UBERON term |
|---|---|
| Nipple | UBERON:0002030 |
| Areola | UBERON:0002032 |
| Breast | UBERON:0000310 |
| Mammary gland | UBERON:0001911 |

**Tissue/cell level:** ectoderm-derived mammary/skin epithelium. Relevant Cell Ontology terms (corrected — see Finding 9): epithelial cell (CL:0000066), mammary gland epithelial cell (CL:0002327), luminal epithelial cell of mammary gland (CL:0002326), basal-myoepithelial cell of mammary gland (CL:0002324), lactocyte (CL:0002325), keratinocyte (CL:0000312).

**PTPRF protein** (UniProt **P10586**, "Receptor-type tyrosine-protein phosphatase F"/LAR; gene MIM 179590; Entrez 5792) is a plasma-membrane receptor (GO:0005886) localizing to adherens junctions.

> *"PTPRF encodes a receptor-type protein phosphatase that localizes to adherens junctions"* — [PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)

**GO annotations:** molecular function — protein tyrosine phosphatase activity (GO:0004725), transmembrane receptor PTP activity (GO:0005001), cell adhesion molecule binding (GO:0050839); biological process — cell adhesion (GO:0007155), cell migration (GO:0016477), peptidyl-tyrosine dephosphorylation (GO:0035335), cell-surface receptor PTP signaling (GO:0007185).

**Orthologs:** mouse *Ptprf* (Entrez 19268), rat (360406), dog (475389), cow (512072), chicken (424568), zebrafish (140819).

### Finding 8 — Epidemiology & inheritance: ultra-rare autosomal recessive, single-family, consanguinity-driven

BNAH2 (OMIM 616001) is defined molecularly from a single consanguineous Israeli Arab family with three affected children across two branches; it was identified by homozygosity mapping, consistent with **autosomal recessive inheritance from a shared ancestral (founder) *PTPRF* allele**.

> *"we report on three children from two branches of an extended consanguineous Israeli Arab family"* — [PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)

No prevalence or incidence figures exist; the disease is ultra-rare (<1/1,000,000; Orphanet "unknown prevalence" class). gnomAD shows that biallelic *PTPRF* loss-of-function is essentially absent in the general population (pLI ≈ 1.0; very few LoF carriers), so population carrier frequency is extremely low and disease occurs almost exclusively in consanguineous unions. **Both sexes are affected** (one girl and two boys in the index family). Penetrance of the nipple phenotype appears high in homozygotes, with **variable expressivity** (unilateral hypothelia to bilateral athelia). Consanguinity is the key modifiable risk factor.

### Finding 9 — Ontology QC corrections and confirmed cross-references

OLS/CL verification corrected the mammary-epithelial Cell Ontology assignments used in the final annotations: the correct terms are **CL:0002327** (mammary gland epithelial cell), **CL:0002326** (luminal epithelial cell of mammary gland), **CL:0002324** (basal-myoepithelial cell of mammary gland), and **CL:0002325** (lactocyte). Importantly, CL:0002325 is *lactocyte* — **not** "basal cell of mammary gland" as mis-stated in an earlier draft; the basal/myoepithelial term is CL:0002324. Keratinocyte = CL:0000312; generic epithelial cell = CL:0000066. The MONDO:0014450 cross-references were re-confirmed: **OMIM:616001, GARD:0016044, MedGen/UMLS C4014918** (MedGen CUI 863355).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic frameshift (loss-of-function) mutation in *PTPRF*** (homozygous, inherited from a shared ancestral allele in a consanguineous union) **leads to** absent or non-functional LAR receptor-type protein tyrosine phosphatase. *(Demonstrated — Borck 2014.)*
2. **Loss of LAR phosphatase activity at adherens junctions** **results in** dysregulated dephosphorylation of LAR substrates and impaired control of epithelial cell–cell contacts. *(Inferred from LAR molecular function.)*
3. **Impaired epithelial adhesion plus altered peptide growth-factor and canonical Wnt signaling** **disrupts** the coordinated proliferation, migration, and placode/bud formation of mammary-ridge (milk-line) ectodermal epithelium during embryonic development. *(Inferred; Wnt/adhesion roles documented, developmental timing in humans not directly demonstrated.)*
4. **Failure of nipple placode / mammary bud morphogenesis** **produces** the structural defect: absent or hypoplastic nipple-areola complex and underdeveloped/absent breast parenchyma. *(Demonstrated phenotype; mechanistic link inferred.)*
5. **Branch (postnatal/functional):** In the analogous mouse model, surviving LAR-deficient epithelium **fails** terminal alveolar differentiation at late pregnancy, **causing** a lactation defect. *(Demonstrated in mouse; predicts impaired lactation in affected human females who retain some breast tissue.)*
6. **Clinical manifestation:** congenital athelia/hypothelia + breast aplasia/hypoplasia with a characteristic eyebrow shape, isolated and non-progressive. *(Demonstrated.)*

```
   PTPRF biallelic LoF (homozygous frameshift)
                │
                ▼
   Absent / non-functional LAR phosphatase  ──► strong LoF constraint (pLI≈1.0)
                │
                ▼
   Dysregulated adherens-junction signaling
   (epithelial adhesion ↓, Wnt/growth-factor signaling altered)
                │
        ┌───────┴────────────────────────┐
        ▼                                 ▼
 Embryonic milk-line /            (mouse) impaired alveolar
 nipple placode morphogenesis     terminal differentiation
 fails                            at late pregnancy
        │                                 │
        ▼                                 ▼
 STRUCTURAL defect:               FUNCTIONAL defect:
 athelia / hypothelia,            lactation failure
 breast aplasia/hypoplasia        (predicted in humans)
        │
        ▼
 Isolated congenital phenotype + characteristic eyebrow
```

**Upstream vs downstream:** The *PTPRF* mutation and loss of LAR phosphatase activity are the upstream initiating events; adhesion/Wnt signaling disruption is intermediate; the structural nipple/breast defect is the downstream clinical endpoint. **Cell types involved:** ectoderm-derived mammary/skin epithelial cells (basal-myoepithelial CL:0002324, luminal CL:0002326, mammary epithelial CL:0002327, keratinocyte CL:0000312). **Key biological processes (GO):** cell adhesion (GO:0007155), peptidyl-tyrosine dephosphorylation (GO:0035335), cell-surface receptor PTP signaling (GO:0007185), cell migration (GO:0016477), all converging on mammary gland morphogenesis.

The coherence of this model rests on three independent pillars: (1) human genetic evidence (homozygous LoF segregating with phenotype in a consanguineous pedigree), (2) molecular plausibility (LAR's documented adherens-junction/Wnt roles), and (3) an animal model demonstrating an essential mammary role for the orthologous gene.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | How it supports / challenges the findings |
|---|---|---|---|
| [24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/) | *Homozygous truncating PTPRF mutation causes athelia* | Human clinical + genetics | **Foundational.** Establishes *PTPRF* biallelic LoF as the cause (F001, F002, F004, F008); defines phenotype spectrum, isolated nature, consanguineous AR inheritance, and LAR molecular function. |
| [9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/) | *Impaired mammary gland development and function in mice lacking LAR* | Model organism (mouse KO) | Corroborates essential mammary role of *Ptprf*/LAR (F003); demonstrates lactation defect; provides protein-domain architecture. Caveat: mouse defect is functional/lactational, not structural athelia. |
| [30550377](https://pubmed.ncbi.nlm.nih.gov/30550377/) | *Hypogonadotropic hypogonadism… in Ulnar-Mammary syndrome* | Human clinical | Defines UMS (*TBX3*) as a syndromic differential (F005). |
| [32067224](https://pubmed.ncbi.nlm.nih.gov/32067224/) | *Novel phenotype… TP63 molecular defect* | Human clinical | Defines TP63 limb-mammary syndrome differential with limb/ectodermal features absent in BNAH2 (F005). |
| [32083401](https://pubmed.ncbi.nlm.nih.gov/32083401/) | *Phenotypic expansion of KMT2D-related disorder* | Human clinical | Describes KMT2D-related athelia with choanal atresia/hypoparathyroidism — key mimic distinguished from BNAH2 (F005). |
| [38281558](https://pubmed.ncbi.nlm.nih.gov/38281558/) | *Spectrum of TP63-related disorders* | Human clinical | Catalogs TP63 ectodermal-dysplasia features (hypoplastic breasts/nipples) distinguishing from isolated BNAH2 (F005). |
| [39320041](https://pubmed.ncbi.nlm.nih.gov/39320041/) | *Inherited TBX3 alteration in ulnar-mammary syndrome* | Human + Drosophila model | Details UMS core features (ulnar defects, hypoplastic nipples/areolas) for differential diagnosis (F005). |
| [23896162](https://pubmed.ncbi.nlm.nih.gov/23896162/) | *Bilateral congenital amazia: systematic review* | Clinical systematic review | Quantifies reconstruction modalities — mainstay of management (F006). |
| [33830564](https://pubmed.ncbi.nlm.nih.gov/33830564/) | *Breast reconstruction via fat grafting (Finlay-Marks)* | Case report | Documents fat grafting as a reconstructive option (F006). |
| [31585491](https://pubmed.ncbi.nlm.nih.gov/31585491/) | *P63-related disorders: dermatological characteristics* | Human clinical | Supports TP63 ectodermal differential (F005). |
| [33930582](https://pubmed.ncbi.nlm.nih.gov/33930582/) | *TBX3 and TBX5 duplication: Holt-Oram/UMS overlap* | Human genetics | Supplementary TBX3/UMS differential context (F005). |
| [32016944](https://pubmed.ncbi.nlm.nih.gov/32016944/) | *Poland Syndrome with Xp22.31 duplication* | Human case | Poland syndrome differential (breast/nipple + pectoral anomalies). |

Additional literature reviewed during triage — tangential to BNAH2 — included the Bork-Baykal nipple-areola sparing phenomenon ([PMID: 30989705](https://pubmed.ncbi.nlm.nih.gov/30989705/)) and the McGovern-nipple airway device in CHARGE syndrome ([PMID: 32611869](https://pubmed.ncbi.nlm.nih.gov/32611869/)).

---

## Section-by-Section Synthesis

### 1. Disease Information
BNAH2 is an isolated congenital disorder of nipple-areola and breast development. **Identifiers:** MONDO:0014450; OMIM:616001; GARD:0016044; MedGen/UMLS C4014918 (CUI 863355). No dedicated Orphanet or specific ICD-10/ICD-11 code is established; it falls under broad categories for congenital breast/nipple malformation. **Synonyms:** "Breasts and/or nipples, aplasia or hypoplasia of, 2"; athelia (isolated); isolated congenital athelia/hypothelia. Information is derived from an **aggregated disease-level resource** basis (OMIM/MONDO) built on a single primary clinical report, not from EHR/patient-level data.

### 2. Etiology
**Causal factor:** genetic — biallelic (homozygous) loss-of-function in *PTPRF*. **Genetic risk factor:** homozygosity for a *PTPRF* LoF allele, enabled by consanguinity (founder effect). **Environmental risk factors:** none identified; **consanguinity** is the principal demographic risk driver. **Protective factors:** none specifically identified; in practical terms, outbreeding reduces recessive risk. **Gene-environment interactions:** none documented — the phenotype appears determined by genotype with variable expressivity.

### 3. Phenotypes
Congenital, non-progressive spectrum: athelia (HP:0002561), hypoplastic nipples (HP:0002557), aplasia/hypoplasia of nipples (HP:0006709), hypoplastic areola (HP:0100853), breast aplasia/hypoplasia (HP:0100783, HP:0010311, HP:0003187), uni-/bilateral breast hypoplasia (HP:0012813/HP:0012814), and abnormal eyebrow morphology (HP:0000534). Onset neonatal/congenital; severity variable (mild unilateral to severe bilateral); frequency within the single reported family: high penetrance among homozygotes. **QoL impact:** cosmetic/body-image and psychosocial effects; inability to breastfeed in affected females; no impact on general health or lifespan.

### 4. Genetic/Molecular Information
**Causal gene:** *PTPRF* (HGNC:9670; gene MIM 179590; Entrez 5792; UniProt P10586), chromosome 1p34.2. **Variant:** homozygous truncating frameshift (loss-of-function). **Classification:** pathogenic (biallelic, segregating, LoF in a constrained gene). **Allele frequency:** biallelic LoF essentially absent from gnomAD; carrier frequency extremely low. **Origin:** germline. **Functional consequence:** loss of function. **Modifier genes/epigenetics/chromosomal abnormalities:** none reported.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are implicated. BNAH2 is a monogenic developmental disorder.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** above for the ordered causal chain. Core pathway elements: adherens-junction–associated LAR tyrosine phosphatase activity, canonical Wnt signaling, and peptide growth-factor signaling governing ectodermal mammary-ridge morphogenesis.

### 7. Anatomical Structures Affected
**Primary:** nipple (UBERON:0002030), areola (UBERON:0002032), breast (UBERON:0000310), mammary gland (UBERON:0001911). **System:** integumentary/reproductive (mammary). **Tissue:** ectoderm-derived epithelium. **Cells:** mammary epithelial populations (CL:0002327, CL:0002326, CL:0002324, CL:0002325), keratinocytes (CL:0000312). **Subcellular:** plasma membrane / adherens junction (GO:0005886). **Lateralization:** bilateral, unilateral, or asymmetric.

### 8. Temporal Development
**Onset:** congenital. **Course:** stable, non-progressive, lifelong structural anomaly. No disease stages, remission, or episodic pattern. **Critical period:** embryonic mammary-ridge development (window for any theoretical developmental intervention).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Epidemiology:** ultra-rare (single reported family; no prevalence/incidence figures). **Penetrance:** high in homozygotes; **expressivity:** variable. **Consanguinity:** central. **Founder effect:** shared ancestral allele in an Israeli Arab kindred. **Sex ratio:** both sexes affected (no evident skew). **Carrier frequency:** extremely low in the general population.

### 10. Diagnostics
**Clinical:** physical examination identifying athelia/hypothelia and breast hypoplasia from birth; assessment for associated anomalies to exclude syndromes. **Genetic testing:** molecular confirmation by single-gene *PTPRF* sequencing, gene panels for congenital breast/nipple anomaly, or WES/WGS; homozygosity mapping is informative in consanguineous pedigrees. **Imaging:** ultrasound/MRI to characterize residual breast parenchyma before reconstruction. **Differential diagnosis:** UMS (*TBX3*), TP63-related disorders, scalp-ear-nipple syndrome (*KCTD1*), KMT2D-related disorder, Poland syndrome — distinguished by their extramammary features.

### 11. Outcome / Prognosis
**Excellent** — normal lifespan, no systemic morbidity or mortality. Morbidity is limited to cosmetic/psychosocial impact and (in females) inability to lactate. **Prognostic factors:** none affecting survival; extent of breast tissue influences reconstructive outcome.

### 12. Treatment
No pharmacologic or disease-modifying therapy. **Reconstructive surgery** (prosthetic implant, autologous tissue, autologous + prosthesis, or fat grafting) and **nipple-areola reconstruction**, generally deferred to breast maturity/adolescence; mean age at reconstruction ~27.6 years in congenital breast anomaly cohorts. **Supportive:** psychological support, lactation counseling where relevant. NCIT concepts: breast reconstruction, breast implant, autologous fat transfer.

### 13. Prevention
No primary medical prevention. **Genetic counseling** for consanguineous families, **carrier/cascade testing**, and **prenatal or preimplantation genetic diagnosis** are the available preventive measures. No immunization or environmental intervention applies.

### 14. Other Species / Natural Disease
*Ptprf* is conserved across mammals and vertebrates (orthologs listed in Finding 7). No naturally occurring companion-animal or wildlife disease specifically attributed to *PTPRF* nipple/breast aplasia is documented in the reviewed literature; the mouse knockout is an engineered model, not a natural disease. No zoonotic relevance.

### 15. Model Organisms
**Mouse (*Mus musculus*, NCBI:txid10090):** LAR/*Ptprf* phosphatase-domain knockout (Schaapveld et al., [PMID: 9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/)). **Phenotype recapitulation:** partial — the model reproduces an essential mammary role (impaired alveolar terminal differentiation, lactation failure) but manifests a **functional** defect rather than the **structural** athelia seen in humans. **Limitation:** overall normal development and histology in LAR⁻/⁻ mice indicates species-specific redundancy for nipple morphogenesis. **Applications:** studying LAR's role in mammary differentiation, adhesion, and Wnt/growth-factor signaling. Resources: MGI (mouse *Ptprf*, Entrez 19268); orthologs available in RGD, ZFIN (zebrafish 140819), etc.

---

## Limitations and Knowledge Gaps

1. **Single-family evidence.** The entire human genetic basis of BNAH2 rests on **one consanguineous family with three affected individuals** ([PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)). No independent replication or additional *PTPRF* families have been reported, so penetrance, full expressivity range, and genotype–phenotype correlations remain uncertain.
2. **Mechanism largely inferred.** The adherens-junction/Wnt/growth-factor signaling steps are biologically plausible and supported by LAR's known molecular functions, but the specific developmental mechanism in human nipple/mammary-ridge formation has **not been experimentally demonstrated**.
3. **Human–mouse phenotypic discordance.** The *Ptprf*-null mouse shows a functional lactation defect with otherwise normal development, not structural athelia — indicating species-specific differences and limiting direct mechanistic extrapolation.
4. **No epidemiologic data.** Prevalence, incidence, carrier frequency in specific populations, and any geographic/variant-specific distribution beyond the index kindred are unknown.
5. **No natural-history or QoL studies.** Formal quality-of-life, psychosocial-outcome, and reconstructive-outcome data **specific to BNAH2** do not exist; management evidence is extrapolated from broader congenital breast anomaly cohorts.
6. **Ontology/identifier gaps.** No dedicated Orphanet number or specific ICD-11 code was confirmed for this entity.

---

## Proposed Follow-up Experiments / Actions

1. **Case ascertainment and replication.** Query GeneMatcher, DECIPHER, and large consanguineous-population cohorts (e.g., Middle Eastern, South Asian biobanks) for additional biallelic *PTPRF* LoF individuals to replicate the gene–disease association and refine the phenotype.
2. **Functional validation of the developmental mechanism.** Use human mammary organoids / iPSC-derived mammary models with *PTPRF* knockout to test whether loss of LAR impairs nipple-placode/mammary-bud morphogenesis via adherens-junction and Wnt readouts; perform rescue experiments.
3. **Improved animal modeling.** Generate conditional/ectoderm-restricted *Ptprf* models or test redundancy with related type IIa RPTPs (*PTPRD*, *PTPRS*) to determine why mice escape structural athelia; consider zebrafish or other models of nipple-equivalent/mammary-line development.
4. **Molecular profiling.** Transcriptomic (GEO/single-cell) and proteomic characterization of *PTPRF*-null mammary epithelium to map downstream Wnt and growth-factor signaling perturbations and identify LAR substrates (e.g., EPHA2, β-catenin pathway components).
5. **Clinical/ontology curation.** Pursue an Orphanet entry and ICD-11 extension code; formalize the HPO/UBERON/CL/GO annotation set (above) in the knowledge base; register the gene–disease relationship in ClinGen for formal validity classification.
6. **Patient-centered outcomes.** Establish a registry (even for ultra-rare N) capturing reconstructive timing/modalities, lactation outcomes in affected females, and psychosocial QoL using validated instruments (e.g., BREAST-Q), to generate BNAH2-specific management evidence.

---

*Report compiled from 5 discovery iterations, 9 confirmed findings, and 14 reviewed papers. Evidence source types: human clinical genetics ([PMID: 24781087](https://pubmed.ncbi.nlm.nih.gov/24781087/)); mouse model ([PMID: 9245518](https://pubmed.ncbi.nlm.nih.gov/9245518/)); clinical review ([PMID: 23896162](https://pubmed.ncbi.nlm.nih.gov/23896162/)); differential-diagnosis clinical literature (TBX3, TP63, KMT2D, KCTD1); plus ontology/constraint database verification (MONDO, OMIM, gnomAD, OLS/HP/CL/UBERON/GO).*


## Artifacts

- [OpenScientist final report](Breasts_and_Nipples_Aplasia_or_Hypoplasia_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Breasts_and_Nipples_Aplasia_or_Hypoplasia_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002561` (2 mentions) - the report calls it "Absent nipple / athelia"; HP calls it **Absent nipple**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `GARD`.

29 of 32 terms resolved to a current term; the rest could not be looked up either way.