---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T19:17:46.088748'
end_time: '2026-10-20T19:52:00.099791'
duration_seconds: 2054.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Visceral Heterotaxy 13
  mondo_id: MONDO:0976134
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 45
  verified: 42
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Visceral_Heterotaxy_13-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Visceral_Heterotaxy_13-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Visceral Heterotaxy 13
- **MONDO ID:** MONDO:0976134 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Visceral Heterotaxy 13** covering all of the
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

# Visceral Heterotaxy 13 (HTX13): A Comprehensive Disease Characteristics Report

**Disease:** Visceral Heterotaxy 13 (HTX13)
**OMIM:** #621079 · **MONDO:** MONDO:0976134 · **Gene:** *DAND5* (HGNC:26780, 19p13.13)
**Category:** Mendelian, autosomal recessive
**Report date:** 2026-10-20

---

## Summary

**Visceral Heterotaxy 13 (HTX13; OMIM #621079) is an ultra-rare, autosomal recessive disorder of embryonic left–right (L-R) patterning caused by biallelic (homozygous or compound-heterozygous) loss-of-function (LOF) variants in *DAND5*.** *DAND5* (also called *CERL2*, *CER2*, *COCO*, *GREM3*, *DANTE*) encodes a 189-amino-acid secreted cystine-knot protein of the CAN/DAN subfamily of BMP/NODAL antagonists. At the ciliated left–right organizer (LRO) of the early embryo, DAND5 is normally expressed asymmetrically (higher on the right) and acts as a brake on NODAL signaling. When leftward cilia-driven nodal fluid flow degrades DAND5 on the left, NODAL is released to self-amplify, inducing *LEFTY* and then *PITX2* in the left lateral plate mesoderm — the molecular events that specify normal visceral asymmetry (*situs solitus*). Biallelic LOF of DAND5 abolishes this asymmetric brake, resulting in randomized or bilateral NODAL–PITX2 signaling and consequent *situs ambiguus* (heterotaxy).

The clinical phenotype is dominated by complex congenital heart disease (CHD) arising from disrupted cardiac looping and laterality, accompanied by thoraco-abdominal situs anomalies: dextrocardia, atrioventricular septal defects, transposition of the great arteries, anomalous pulmonary venous return, atrial/bronchial isomerism, asplenia or polysplenia, and intestinal malrotation. The HPO gene-to-disease annotation extends the spectrum to include recurrent infections (from asplenia), neurodevelopmental delay, and mild dysmorphism. Disease onset is congenital; inheritance is autosomal recessive, with the disorder thus far reported predominantly in consanguineous Arab-Muslim families.

HTX13 is a very recently delineated entity: the first biallelic LOF case was published in 2022, with the disorder defined through at least three unrelated families (2022–2026) plus in-vitro functional proof that pathogenic DAND5 variants cannot inhibit nodal signaling. Decades of model-organism work (mouse *Dand5*/*Cerl2*, zebrafish *charon*, *Xenopus* *coco*/*cerl-2*) independently corroborate the mechanism, and gnomAD constraint metrics (pLI = 0.002) are fully consistent with a recessive loss-of-function mechanism rather than haploinsufficiency. No HTX13-specific prevalence, survival, or therapy data exist; management and prognosis are extrapolated from the broader heterotaxy-with-CHD literature (~1/10,000 birth prevalence; ~71%/68% 5-/10-year survival).

---

## Key Findings

### Finding 1 — HTX13 is caused by biallelic loss-of-function variants in *DAND5*

OMIM #621079 (Heterotaxy, visceral, 13, autosomal; HTX13) attributes the disorder to **homozygous *DAND5* mutations** (gene MIM 609068) on chromosome 19p13. Three pathogenic alleles have been reported across unrelated families:

- **c.396dupCT** (a 2-bp duplication causing a frameshift; Bolkier et al. 2022)
- **c.197delT / c.197del, p.(Leu66Argfs*22)** (a 1-bp deletion causing a frameshift LOF; Ganapathi et al. 2022)
- A **shared homozygous variant** identified in two unrelated Arab-Muslim probands (Chorin et al. 2026)

Critically, the mechanism has been functionally validated: in a Nodal-dependent luciferase reporter assay, **DAND5 c.197del failed to inhibit Nodal signaling, whereas the wild-type construct did**, demonstrating that the frameshift produces a complete loss of function. The convergence of independent human families, a reproducible biochemical defect, and strong model-organism support establishes *DAND5* as the causal gene for HTX13.

> *"ES revealed a shared homozygous variant in the Dan Domain Family Member 5"* — [PMID: 42650045](https://pubmed.ncbi.nlm.nih.gov/42650045/) (Chorin et al. 2026)

> *"A novel biallelic loss-of-function variant in..."* — [PMID: 36316122](https://pubmed.ncbi.nlm.nih.gov/36316122/) (Ganapathi et al. 2022), reporting the c.197delT allele.

### Finding 2 — DAND5/Cerl2 is an asymmetrically expressed NODAL antagonist at the left–right organizer

In the mouse node, **Nodal and Cerl2 (the mouse ortholog of DAND5) are expressed asymmetrically**: Nodal is higher on the left, while Cerl2 — a Nodal inhibitor — is higher on the right. Leftward nodal fluid flow reduces Cerl2 on the left side, releasing NODAL to self-amplify and induce *Lefty* and then *Pitx2* in the left lateral plate mesoderm. The *inv* mutant demonstrates the causal logic directly: a localized reduction of Cerl2 up-regulates Nodal and reverses L-R asymmetry (Oki et al. 2009). More broadly, **DAND5, PKD1L1, MMP21, and CIROP form a genetic module** that has specifically evolved in vertebrate species harboring motile cilia at the LRO (Szenker-Ravi et al. 2025), placing DAND5 at the heart of a conserved laterality-determining mechanism.

> *"the expression of Nodal and Cerl2 (Dand5), which encodes an inhibitor of Nodal, is asymmetric, with the level of Nodal expression being higher on the left side and that of Cerl2 expression higher on the right"* — [PMID: 19906859](https://pubmed.ncbi.nlm.nih.gov/19906859/) (Oki et al. 2009)

> *"Four genes-DAND5, PKD1L1, MMP21, and CIROP-form a genetic module that has specifically evolved in vertebrate species that harbor motile cilia in their left-right organizer (LRO)"* — [PMID: 39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/) (Szenker-Ravi et al. 2025)

### Finding 3 — *Dand5*/*Cerl2* knockout mice model HTX13: laterality randomization plus intrinsic cardiac defects

*Cerl2*(−/−) mice show significant neonatal mortality within the first day after birth, **largely attributable to cardiac defects associated with randomization of the left–right axis**. Importantly, and independent of laterality, Cerl2-null neonates also develop massive **left-ventricular myocardial wall enlargement (hyperplasia)** driven by a high cardiomyocyte mitotic index with increased *Ccnd1* expression; echocardiography reveals left-ventricular systolic dysfunction incompatible with a long lifespan (Araújo et al. 2014). Cerl2 is normally expressed more highly in the left ventricle at E13, indicating a regionalized role in left-ventricular muscle formation that is distinct from its role in axis specification. This dual phenotype — laterality randomization plus intrinsic myocardial dysfunction — makes the Cerl2 knockout an informative model for the cardiac lethality seen in human heterotaxy.

> *"revealed a significant mortality during the first day after birth, mostly due to cardiac defects apparently associated with randomization of the left-right axis"* — [PMID: 25033293](https://pubmed.ncbi.nlm.nih.gov/25033293/) (Araújo et al. 2014)

### Finding 4 — DAND5 is a 189-aa secreted cystine-knot NODAL/BMP antagonist; gnomAD constraint confirms a recessive mechanism

DAND5 (HGNC:26780; NCBI Gene 199699; UniProt Q8N907; Ensembl ENSG00000179284; cytoband 19p13.13) encodes a **189-residue secreted protein** with an N-terminal signal peptide (aa 1–22) and a C-terminal **cystine-knot (CTCK) domain (aa 101–186)** stabilized by four disulfide bonds (Cys101–148, 115–162, 125–183, 129–185); it is N-glycosylated at N38. DAND5 belongs to the **CAN/DAN subfamily of BMP antagonists**, binds NODAL to inhibit left–right patterning, and additionally antagonizes BMP/TGF-β signaling and exhibits anti-angiogenic activity.

Population constraint metrics from gnomAD are decisive for the inheritance model: **pLI = 0.002** and **LOEUF/oe_lof = 0.87** (observed LOF = 8 vs. expected = 9.24). DAND5 is therefore **not intolerant to heterozygous loss of function** — consistent with the clinical observation that heterozygous carriers are unaffected and disease requires biallelic LOF. The two reported pathogenic frameshifts — **c.197delT** (~codon 66, upstream of the CTCK domain) and **c.396dupCT** (within the CTCK domain) — are both predicted to **abolish the cystine-knot fold**, consistent with complete loss of function.

| Attribute | Value |
|---|---|
| Gene symbol | *DAND5* (aliases *CERL2*, *CER2*, *COCO*, *GREM3*, *DANTE*) |
| HGNC | HGNC:26780 |
| NCBI Gene | 199699 |
| UniProt | Q8N907 |
| Ensembl | ENSG00000179284 |
| Cytoband | 19p13.13 |
| Protein length | 189 aa |
| Key domains | Signal peptide (1–22); CTCK cystine-knot (101–186) |
| gnomAD pLI | 0.002 (LOF-tolerant → recessive mechanism) |
| gnomAD LOEUF | 0.87 |

### Finding 5 — HTX13 phenotype spectrum (HPO) extends beyond cardiac/visceral situs to asplenia/polysplenia, neurodevelopmental delay, and dysmorphism

The HPO/JAX gene-to-disease annotation for *DAND5* (OMIM:621079) comprises **29 phenotype terms**, organized below by system. Onset is **Congenital (HP:0003577)** and inheritance is **Autosomal recessive (HP:0000007)**.

| Category | HPO phenotypes (term IDs) |
|---|---|
| Situs / laterality | Isomerism (HP:0031853), Right atrial isomerism (HP:0011536), Bronchial isomerism (HP:0031564), Dextrocardia (HP:0001651) |
| Cardiac | Complete atrioventricular canal defect (HP:0001674), Transposition of the great arteries (HP:0001669), Valvular/pulmonic stenosis (HP:0034350 / HP:0001642), Patent ductus arteriosus (HP:0001643), Infracardiac TAPVC (HP:0011721), Partial anomalous pulmonary venous return (HP:0010773), Cardiomyopathy (HP:0001638), Cardiomegaly (HP:0001640), Congestive heart failure (HP:0001635), Pulmonary arterial hypertension (HP:0002092) |
| Spleen / immune | Asplenia (HP:0001746), Polysplenia (HP:0001748), Recurrent infections (HP:0002719) |
| Gastrointestinal | Intestinal malrotation (HP:0002566), Nasogastric tube feeding (HP:0040288) |
| Neurodevelopmental | Global developmental delay (HP:0001263), Delayed speech/language (HP:0000750), Delayed fine motor development (HP:0010862), Dyskinesia (HP:0100660) |
| Dysmorphism | Hypertelorism (HP:0000316), Epicanthus (HP:0000286), Coarse facial features (HP:0000280) |

The breadth of this annotation reflects the pleiotropic downstream consequences of disrupted L-R patterning (cardiac, splenic, GI situs) plus secondary complications (recurrent infection from asplenia; feeding difficulty), and some features (neurodevelopmental delay, dysmorphism) that are reported but whose causal relationship to DAND5 loss is less firmly established given the small number of cases.

### Finding 6 — ClinVar documents two heterotaxy-associated *DAND5* frameshifts; missense variants are VUS, and large 19p13 CNVs cause other syndromes

On transcript **NM_152654.3**, ClinVar records the two HTX13 variants:

- **c.197del, p.(Leu66fs)** — condition: Heterotaxy; currently classified **Uncertain significance** (single-submitter, reflecting the rarity of the disorder despite functional evidence)
- **c.396_397dup, p.(Tyr133fs)** — condition: Heterotaxy; classified **Pathogenic/Likely pathogenic**

By contrast, **all ~20 recorded DAND5 single-nucleotide (missense) variants** (e.g., p.Arg152Cys, p.Arg112Trp, p.Gly80Glu) are classified **Benign/Likely benign or Uncertain significance**, with no established disease link — underscoring that the established disease mechanism is frameshift/truncating LOF, not missense. Separately, numerous **large 19p13 copy-number variants** (deletions/duplications spanning *DAND5*) in ClinVar are annotated to **contiguous-gene conditions** (e.g., episodic ataxia type 2 at the *CACNA1A* region; developmental and epileptic encephalopathy 42) rather than to isolated HTX13 — an important caveat for interpreting CNVs overlapping this locus.

### Finding 7 — Precise variant nomenclature, functional proof, and the full cross-species ortholog set

Ganapathi et al. 2022 ([PMID: 36316122](https://pubmed.ncbi.nlm.nih.gov/36316122/)) describe the **second unrelated biallelic HTX13 individual**, homozygous for **NM_152654.2:c.197del, p.(Leu66ArgfsTer22)**; an in-vitro assay showed this variant cannot inhibit nodal signaling versus wild-type, strengthening the evidence for autosomal recessive DAND5 heterotaxy. The **first biallelic LOF case** was reported by Bolkier et al. 2022 ([PMID: 34215651](https://pubmed.ncbi.nlm.nih.gov/34215651/)), within a cohort in which WES achieved a molecular diagnosis in 56.7% of laterality/CHD probands.

**DAND5 orthologs** (HomoloGene 51883 and model-organism databases):

| Species | Gene | NCBI Gene ID |
|---|---|---|
| Human | *DAND5* | 199699 |
| Mouse | *Dand5* / *Cerl2* | 23863 |
| Rat | *Dand5* | 685719 |
| Dog | *Dand5* | 484921 |
| Rhesus macaque | *Dand5* | 717076 |
| Chimpanzee | *Dand5* | 747680 |
| Zebrafish | *dand5* / *charon* | 791454 |
| *Xenopus tropicalis* | *dand5* / *cerl-2* / *coco* | 733727 |

> *"we describe a second unrelated individual with heterotaxy syndrome and a homozygous frameshift variant in DAND5 (NM_152654.2:c.197del..."* — [PMID: 36316122](https://pubmed.ncbi.nlm.nih.gov/36316122/)

> *"the DAND5 c.197del variant is unable to inhibit nodal signaling when compared with the wild-type expression construct"* — [PMID: 36316122](https://pubmed.ncbi.nlm.nih.gov/36316122/)

### Finding 8 — HTX13 is an ultra-rare, recently defined (2022–2026) autosomal recessive laterality disorder with limited but convergent evidence

Gene–disease validity rests on **≥3 unrelated biallelic DAND5 families** (Bolkier 2022 [PMID: 34215651]; Ganapathi 2022 [PMID: 36316122]; Chorin 2026 [PMID: 42650045]), **in-vitro functional proof** of Nodal-inhibition loss, **decades of model-organism data** (mouse *Cerl2*/*Dand5*, zebrafish *charon*, *Xenopus* *coco*), and **gnomAD constraint consistent with recessive LOF** (pLI = 0.002). No HTX13-specific prevalence, incidence, sex ratio, survival statistics, pharmacotherapy, or disease-specific therapy exist. Prognosis and management are extrapolated from the general heterotaxy-with-CHD literature, where **~1/10,000 birth prevalence** and **5-/10-year survival of ~71%/68%** are reported (context: [PMID: 42185088](https://pubmed.ncbi.nlm.nih.gov/42185088/)). Management is supportive/surgical (staged CHD repair, Ladd procedure for malrotation, asplenia infection prophylaxis); prevention consists of genetic counseling, carrier/cascade screening, and prenatal detection.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LOF variant in *DAND5*** (e.g., c.197del p.Leu66Argfs*22 or c.396dupCT) → **leads to** a truncated DAND5 protein lacking/disrupting the C-terminal cystine-knot (CTCK) domain.
2. Loss of the cystine-knot fold → **results in** a secreted protein unable to bind and inhibit NODAL (demonstrated: the c.197del variant fails to inhibit Nodal signaling in a luciferase reporter assay).
3. Absence of functional DAND5 at the ciliated left–right organizer (LRO) → **removes** the normal asymmetric "brake" on NODAL (normally higher-right DAND5 restricting NODAL to the left).
4. Loss of the asymmetric brake → **causes** randomized or bilateral NODAL self-amplification instead of normal left-restricted signaling. *(This is the branch point: the readout is stochastic because the symmetry-breaking cue is lost rather than reversed.)*
5. Dysregulated NODAL → **drives** abnormal/bilateral *LEFTY* and *PITX2* induction in the lateral plate mesoderm (inferred in human from the conserved vertebrate cascade; demonstrated in mouse/frog/fish models).
6. Loss of asymmetric *PITX2* → **results in** abnormal cardiac looping and failure of normal visceral situs specification.
7. Abnormal looping/situs → **manifests as** *situs ambiguus* (heterotaxy): dextrocardia, complex CHD (AVSD, TGA, anomalous pulmonary venous return), atrial/bronchial isomerism, asplenia or polysplenia, and intestinal malrotation.
8. In parallel (laterality-independent branch, demonstrated in mouse): loss of DAND5/Cerl2 → **causes** left-ventricular cardiomyocyte hyperplasia (↑ Ccnd1, ↑ mitotic index) → **leads to** systolic dysfunction — contributing to cardiac morbidity beyond the situs defect itself.
9. Downstream clinical complications → asplenia **leads to** susceptibility to encapsulated-organism infection; malrotation **leads to** risk of midgut volvulus; complex CHD **leads to** heart failure and perinatal/infant mortality.

### Schematic

```
 DAND5 biallelic LOF
         |
         v
 Truncated protein, disrupted cystine-knot (CTCK) domain
         |
         v
 Loss of NODAL-antagonist function  --(functionally proven: no Nodal inhibition)
         |
         v
 LRO: asymmetric "brake" on NODAL removed
         |
         +---------------- Laterality branch ----------------+
         v                                                    v
 Randomized / bilateral NODAL             (mouse) LV cardiomyocyte hyperplasia
         |                                        up Ccnd1, up mitotic index
         v                                                    |
 Abnormal LEFTY / PITX2                                       v
         |                                        LV systolic dysfunction
         v
 Abnormal cardiac looping + visceral situs failure
         |
         v
 SITUS AMBIGUUS (HETEROTAXY):
   dextrocardia . complex CHD (AVSD, TGA, anomalous pulm. venous return)
   atrial/bronchial isomerism . asplenia/polysplenia . intestinal malrotation
         |
         v
 Complications: infection (asplenia) . volvulus (malrotation) . heart failure
```

### Upstream vs. downstream, cell types, and processes

- **Upstream (initiating):** The *DAND5* LOF mutation and the resulting loss of NODAL antagonism at the LRO are the most upstream events. The relevant cell types are the **ciliated cells of the left–right organizer** (node/gastrocoel roof plate), bearing both motile and immotile (sensory) cilia.
- **Midstream:** Dysregulated NODAL–LEFTY–PITX2 signaling in the **lateral plate mesoderm**.
- **Downstream:** Abnormal morphogenesis of **cardiomyocytes** (looping heart tube, LV myocardium), **splenic mesenchyme**, and **gut endoderm/mesenchyme**, producing the organ-level phenotype.

**Suggested ontology terms:**
- *Biological process (GO):* determination of left/right symmetry (GO:0007368); nodal signaling pathway (GO:0038092); BMP signaling pathway (GO:0030509); heart looping (GO:0001947); cilium movement (GO:0003341).
- *Molecular function (GO):* BMP binding (GO:0036122); growth factor activity / cytokine antagonist activity.
- *Cellular component (GO):* extracellular space (GO:0005615) — DAND5 is secreted.
- *Cell types (CL):* ciliated cell (CL:0000064); cardiac muscle cell / cardiomyocyte (CL:0000746); epithelial cell of the left–right organizer.
- *Anatomy (UBERON):* embryonic node / left–right organizer; lateral plate mesoderm (UBERON:0003081); heart (UBERON:0000948); spleen (UBERON:0002106); intestine (UBERON:0000160).
- *Chemical (CHEBI):* no disease-specific metabolite; NODAL/BMP are proteins, not CHEBI entities.

---

## Section-by-Section Characteristics

### 1. Disease Information
HTX13 is a Mendelian disorder of visceral left–right asymmetry (situs ambiguus / heterotaxy) with complex congenital heart disease. **Identifiers:** OMIM #621079; MONDO:0976134; gene *DAND5* (MIM 609068). ICD-10 Q89.3 (situs inversus) / Q20–Q24 (congenital heart malformations) are the closest available codes; there is no HTX13-specific ICD code. **Synonyms:** Heterotaxy, visceral, 13, autosomal (HTX13); DAND5-related heterotaxy; *DAND5* aliases include CERL2, CER2, COCO, GREM3, DANTE. Information is derived from **aggregated disease-level resources** (OMIM, HPO, ClinVar) and a small number of **individual patient case reports**.

### 2. Etiology
**Causal factor:** genetic — biallelic LOF variants in *DAND5*. **Genetic risk factors:** the causal variants themselves (frameshifts); **consanguinity** is a major risk factor, as all reported families are consanguineous (Arab-Muslim descent). No environmental or infectious cause is established for HTX13 specifically. In the broader heterotaxy/laterality literature, **pregestational/maternal diabetes** is a recognized environmental risk factor for laterality spectrum disorders ([PMID: 41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/)), and some reports describe a possible rise in fetal laterality disorders around the COVID-19 pandemic ([PMID: 42110452](https://pubmed.ncbi.nlm.nih.gov/42110452/)) — but neither has been linked to DAND5-specific disease. **Protective factors:** none identified. **Gene–environment interactions:** not characterized for HTX13.

### 3. Phenotypes
See Finding 5 for the complete 29-term HPO list. The dominant, highest-frequency phenotypes are **cardiac** (complex CHD, dextrocardia, AVSD, TGA, anomalous pulmonary venous return) and **situs/laterality** (isomerism, asplenia/polysplenia, intestinal malrotation). Severity is **variable but often severe**, driven by the cardiac lesion. Onset is **congenital/neonatal**; the course is determined by CHD severity. Quality-of-life impact is substantial in affected infants (feeding difficulty requiring NG tube; surgical burden; infection risk from asplenia), though no HTX13-specific QoL instrument data exist.

### 4. Genetic/Molecular Information
**Causal gene:** *DAND5* (see Finding 4 for full identifiers). **Pathogenic variants:** c.197del p.(Leu66Argfs*22) and c.396_397dup p.(Tyr133fs), both **frameshift/truncating**, both predicted/proven LOF. **Variant classification (ACMG/ClinVar):** c.396_397dup = Pathogenic/Likely pathogenic; c.197del = Uncertain significance despite functional evidence (single submitter). **Allele frequency:** both are ultra-rare/absent in gnomAD; recessive disease requires biallelic LOF (gnomAD pLI = 0.002 confirms LOF-tolerance in heterozygotes). **Origin:** germline. **Functional consequence:** loss of function (abolished NODAL inhibition). **Missense variants** across DAND5 are benign/VUS. **Modifier genes/epigenetics:** not characterized. **Chromosomal abnormalities:** large 19p13 CNVs spanning *DAND5* are associated with contiguous-gene syndromes, not isolated HTX13 (Finding 6).

### 5. Environmental Information
No DAND5/HTX13-specific environmental, lifestyle, or infectious factor is established. Context from the broader laterality field implicates maternal pregestational diabetes as a risk factor for laterality spectrum disorders ([PMID: 41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/)).

### 6. Mechanism / Pathophysiology
Fully detailed in the **Mechanistic Model** section above: biallelic DAND5 LOF → loss of NODAL antagonism at the LRO → randomized/bilateral NODAL–LEFTY–PITX2 signaling → abnormal cardiac looping and visceral situs → heterotaxy, with a parallel laterality-independent myocardial-hyperplasia branch demonstrated in mouse. Key pathway: **NODAL/TGF-β superfamily signaling**; antagonized BMP signaling; cilia-driven nodal flow.

### 7. Anatomical Structures Affected
**Primary organs:** heart (looping, septation, great-vessel and pulmonary-venous connections), spleen (asplenia/polysplenia), intestine (malrotation). **Body systems:** cardiovascular, digestive, immune/lymphatic (spleen), respiratory (bronchial isomerism). **Tissue/cell level:** cardiomyocytes (CL:0000746); ciliated LRO cells (CL:0000064); splenic and gut mesenchyme. **Subcellular:** extracellular space (secreted DAND5); cilium/basal body at the LRO. **Localization:** thoraco-abdominal; lateralization is the defining abnormality — **abnormal/randomized laterality (isomerism, situs ambiguus)** rather than consistent unilateral/bilateral.

### 8. Temporal Development
**Onset:** congenital — the lesion acts during gastrulation/early organogenesis (symmetry-breaking at the LRO is an early-embryonic event; the critical window is the node stage). **Progression:** the structural defects are fixed at birth; clinical course is driven by CHD and its surgical palliation. **Disease course:** chronic/lifelong for survivors; mortality concentrated in the neonatal/infant period. **Critical period for intervention:** prenatal detection and perinatal/surgical planning.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (HP:0000007). **Penetrance:** appears high in biallelic individuals, but the small case number precludes precise estimates. **Expressivity:** variable (range and severity of cardiac/visceral anomalies differ between families). **Consanguinity:** central — all reported families are consanguineous. **Carrier frequency:** not established; DAND5 LOF alleles are ultra-rare in gnomAD. **Founder effect:** a shared homozygous variant in two unrelated Arab-Muslim probands (Chorin 2026) raises the possibility of a regional founder allele. **Epidemiology:** no HTX13-specific prevalence; heterotaxy overall ~1/10,000 births. **Sex ratio / age distribution:** not established for HTX13.

### 10. Diagnostics
**Imaging:** fetal echocardiography and prenatal ultrasound are the mainstay for detecting situs/cardiac anomalies (heterotaxy has among the highest prenatal detection rates, e.g., 91% in one Japanese cohort, [PMID: 42324491](https://pubmed.ncbi.nlm.nih.gov/42324491/)); postnatal echocardiography, CT/MRI, abdominal ultrasound (spleen, situs). **Laboratory:** peripheral smear for Howell–Jolly bodies (functional asplenia). **Genetic testing:** WES/WGS is the diagnostic modality that defined HTX13 (WES diagnosed 56.7% of a laterality/CHD cohort, [PMID: 34215651](https://pubmed.ncbi.nlm.nih.gov/34215651/)); targeted *DAND5* sequencing or heterotaxy/CHD gene panels; chromosomal microarray to exclude contiguous-gene CNVs. **Clinical criteria:** diagnosis based on demonstration of situs ambiguus with complex CHD plus biallelic *DAND5* LOF. **Differential diagnosis:** other heterotaxy genes (PKD1L1/HTX8, ANKS3, CCDC11, MMP21, ZIC3/HTX1, NODAL, CFC1, etc.) and primary ciliary dyskinesia.

### 11. Outcome/Prognosis
No HTX13-specific survival data. Extrapolating from heterotaxy-with-CHD cohorts: median **5-/10-year survival ~71%/68%**; **complete heart block and pulmonary venous obstruction** are key predictors of mortality ([PMID: 42185088](https://pubmed.ncbi.nlm.nih.gov/42185088/)). Asplenia-syndrome single-ventricle palliation shows ~75.7% 1-year and ~53.7% 20-year survival, worse with TAPVC/pulmonary atresia/AV-valve regurgitation ([PMID: 41614290](https://pubmed.ncbi.nlm.nih.gov/41614290/)). **Morbidity:** surgical burden, infection risk (asplenia), feeding difficulty, developmental delay. **Prognostic factors:** cardiac morphology severity, RVOT obstruction, heart block, pulmonary venous obstruction.

### 12. Treatment
**No disease-specific or gene-targeted therapy exists.** Management is **supportive and surgical**: staged congenital heart surgery (often single-ventricle palliation/Fontan pathway for complex lesions); **Ladd procedure** for intestinal malrotation; **antibiotic prophylaxis and vaccination against encapsulated organisms** for asplenia; nutritional support (NG/feeding support). Pharmacotherapy is symptomatic (heart-failure management, arrhythmia/heart-block management including pacing). **Suggested NCIT terms:** Congenital Heart Disease Surgery; Fontan Procedure; Antibiotic Prophylaxis; Vaccination. No pharmacogenomic, gene, cell, or RNA therapy is available or in trials for HTX13 specifically.

### 13. Prevention
**Primary prevention:** not applicable (congenital genetic disorder) beyond avoidance of modifiable maternal risk factors (e.g., glycemic control in pregestational diabetes, by extrapolation). **Secondary prevention / early detection:** prenatal ultrasound and fetal echocardiography for early diagnosis and delivery planning. **Genetic prevention:** **genetic counseling** for consanguineous families, **carrier/cascade screening** of relatives, **prenatal diagnosis** and **preimplantation genetic testing** for families with a known biallelic genotype. **Tertiary prevention:** asplenia infection prophylaxis; surveillance for and timely repair of malrotation to prevent volvulus.

### 14. Other Species / Natural Disease
DAND5 is highly conserved across vertebrates (orthologs in mouse, rat, dog, rhesus, chimp, zebrafish, *Xenopus* — Finding 7). The mechanism is evolutionarily conserved: DAND5/PKD1L1/MMP21/CIROP form a vertebrate LRO module tied to motile cilia ([PMID: 39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/)). No naturally occurring companion-animal/wildlife DAND5 disease is catalogued in OMIA for this entity; the disorder is essentially defined through experimental models. No zoonotic potential (non-infectious disorder).

### 15. Model Organisms
- **Mouse** (*Dand5*/*Cerl2*): knockout recapitulates laterality randomization + neonatal cardiac lethality, plus laterality-independent LV hyperplasia/systolic dysfunction (Araújo 2014, [PMID: 25033293](https://pubmed.ncbi.nlm.nih.gov/25033293/)); *inv* mutant shows Cerl2 reduction reverses asymmetry (Oki 2009, [PMID: 19906859](https://pubmed.ncbi.nlm.nih.gov/19906859/)). **Strong phenotype recapitulation** of the laterality/cardiac axis.
- **Zebrafish** (*dand5*/*charon*): laterality model; *dand5* is a standard L-R marker readout.
- **Xenopus** (*dand5*/*coco*/*cerl-2*): laterality model; *dand5* expression is a canonical early L-R asymmetry marker (used in CACNA1G, CCDC57 studies — [PMID: 40008628](https://pubmed.ncbi.nlm.nih.gov/40008628/), [PMID: 41758249](https://pubmed.ncbi.nlm.nih.gov/41758249/)).
- **In vitro:** Nodal-dependent luciferase reporter assay provided direct functional proof that patient variants cannot inhibit Nodal (Ganapathi 2022).
- **Limitations:** species differences in cilia dependence of L-R patterning; models capture the laterality/cardiac mechanism well but not the full human neurodevelopmental/dysmorphic spectrum. **Resources:** MGI, ZFIN, Xenbase, IMPC.

---

## Evidence Base

| PMID | Study (abbrev.) | Type | How it supports/challenges findings |
|---|---|---|---|
| [34215651](https://pubmed.ncbi.nlm.nih.gov/34215651/) | Bolkier et al. 2022 — WES in 30 Arab-Muslim laterality/CHD probands | Human clinical | First biallelic DAND5 LOF case (c.396dupCT); WES diagnosed 56.7% of cohort — supports Findings 1, 7, 8 |
| [36316122](https://pubmed.ncbi.nlm.nih.gov/36316122/) | Ganapathi et al. 2022 — second DAND5 individual | Human clinical + in vitro | Exact variant c.197del p.Leu66Argfs*22; functional proof of lost Nodal inhibition — supports Findings 1, 7 |
| [42650045](https://pubmed.ncbi.nlm.nih.gov/42650045/) | Chorin et al. 2026 — further support | Human clinical | Shared homozygous DAND5 variant in two unrelated probands (possible founder) — supports Findings 1, 8 |
| [19906859](https://pubmed.ncbi.nlm.nih.gov/19906859/) | Oki et al. 2009 — reversal of L-R asymmetry | Mouse model | Establishes asymmetric Nodal/Cerl2 expression and causal role of Cerl2 reduction — supports Finding 2 |
| [25033293](https://pubmed.ncbi.nlm.nih.gov/25033293/) | Araújo et al. 2014 — Cerl2 inactivation | Mouse model | Knockout models laterality-associated cardiac lethality + LV hyperplasia — supports Finding 3 |
| [39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/) | Szenker-Ravi et al. 2025 — CIROZ/LRO module | Computational/comparative | Places DAND5 in conserved vertebrate LRO genetic module — supports Finding 2 |
| [38884745](https://pubmed.ncbi.nlm.nih.gov/38884745/) | Molecular Pathways and Animal Models of Situs Defects (review) | Review | Frames NODAL-left/BMP-right paradigm and LRO cilia biology — supports mechanistic model |
| [42185088](https://pubmed.ncbi.nlm.nih.gov/42185088/) | Risk Factors for Adverse Outcome in Heterotaxy+CHD fetuses | Human clinical | Provides 5-/10-yr survival (71%/68%) and prognostic factors — context for prognosis (Finding 8) |
| [41614290](https://pubmed.ncbi.nlm.nih.gov/41614290/) | Long-term outcomes after single-ventricle palliation, asplenia | Human clinical | Asplenia-syndrome survival and surgical risk factors — context for prognosis/treatment |
| [42324491](https://pubmed.ncbi.nlm.nih.gov/42324491/) | Prenatal detection of critical CHD, Japan | Human clinical | Heterotaxy prenatal detection ~91% — context for diagnostics |
| [41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/) | Laterality spectrum disorders + pregestational diabetes | Human clinical | Maternal diabetes association — context for etiology/environment |
| [40008628](https://pubmed.ncbi.nlm.nih.gov/40008628/) | CACNA1G in Xenopus L-R patterning | Frog model | Uses dand5 as early L-R marker — supports DAND5's upstream role |
| [41758249](https://pubmed.ncbi.nlm.nih.gov/41758249/) | Ccdc57 regulates cilia/L-R patterning | Frog model + human | dand5 misexpression as readout of LRO dysfunction — supports mechanism |

**Note on citation integrity:** Two citation snippets for PMID 36316122 are flagged as "mismatch" in the knowledge state (the exact verbatim text may differ slightly from the stored abstract). The substantive claims — that this paper reports a biallelic DAND5 c.197del in a second heterotaxy patient and demonstrated loss of Nodal inhibition — are consistent with the paper's content as recorded; readers should verify exact quotations against the primary source.

---

## Limitations and Knowledge Gaps

1. **Very small case base.** HTX13 rests on ~3 unrelated families (2022–2026). Penetrance, expressivity, sex ratio, and the full phenotype spectrum are poorly defined. The neurodevelopmental and dysmorphic HPO annotations in particular may reflect single-case observations or coincidental features rather than core DAND5 consequences.
2. **Variant classification lag.** Despite functional proof, c.197del remains a single-submitter VUS in ClinVar, illustrating how rare-disease evidence propagates slowly into variant databases.
3. **No HTX13-specific epidemiology, natural history, survival, or treatment data.** All prognosis/management statements are extrapolated from general heterotaxy-with-CHD cohorts, which include many non-DAND5 etiologies and may not reflect DAND5-specific outcomes.
4. **Mechanistic inference in humans.** The NODAL–LEFTY–PITX2 downstream cascade and the LV-hyperplasia branch are demonstrated in model organisms; their precise operation in human DAND5 patients is inferred, not directly shown.
5. **Ascertainment bias toward consanguineous populations.** Reported families are Arab-Muslim/consanguineous; the allele spectrum and frequency in other populations are unknown.
6. **No genotype–phenotype map.** With only truncating alleles reported as pathogenic, the clinical consequences of hypomorphic/missense DAND5 variants (currently VUS/benign) are unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate cases via GeneMatcher / Matchmaker Exchange** to expand the HTX13 cohort, enabling estimation of penetrance, expressivity, sex ratio, and a validated phenotype spectrum (clarifying whether neurodevelopmental/dysmorphic features are core).
2. **Upgrade ClinVar classification** of c.197del by submitting the published functional (Nodal-inhibition) evidence under ACMG PS3, and encourage multi-submitter review.
3. **Founder-allele analysis** in Arab-Muslim populations: genotype the shared Chorin 2026 variant, estimate carrier frequency in regional/local cohorts, and assess a founder haplotype — informing carrier-screening programs.
4. **Patient-derived iPSC → cardiac organoid / LRO-like models** to test whether human DAND5 LOF reproduces the mouse LV-hyperplasia branch and to dissect NODAL–PITX2 dysregulation in a human context.
5. **Functional assays for DAND5 missense VUS** (Nodal-inhibition reporter) to build a genotype–function map and resolve whether any missense alleles are hypomorphic.
6. **Prospective natural-history registry** for molecularly confirmed DAND5 heterotaxy to generate disease-specific survival, surgical-outcome, and quality-of-life data rather than relying on mixed-etiology cohorts.
7. **Prenatal/perinatal pathway**: integrate DAND5 testing into heterotaxy fetal-cardiology workups given the high prenatal detection rate of heterotaxy, enabling earlier counseling and delivery planning.

---

## Consensus Answer

Visceral Heterotaxy 13 (HTX13; OMIM #621079, MONDO:0976134) is an ultra-rare autosomal recessive disorder of embryonic left–right patterning caused by biallelic loss-of-function variants in *DAND5* (HGNC:26780, 19p13.13; e.g., c.197del p.Leu66Argfs*22 and c.396_397dup p.Tyr133fs), which encodes a secreted cystine-knot NODAL antagonist at the ciliated left–right organizer. Loss of DAND5 removes the asymmetric brake on NODAL, causing randomized/bilateral NODAL–PITX2 signaling and consequent situs ambiguus with complex congenital heart disease (dextrocardia, AVSD, TGA, anomalous pulmonary venous return), isomerism, asplenia/polysplenia, and intestinal malrotation; management is supportive/surgical with no disease-specific therapy, and mouse *Dand5*/*Cerl2*, zebrafish *charon*, and *Xenopus coco* models recapitulate the laterality-plus-cardiac phenotype.


## Artifacts

- [OpenScientist final report](Visceral_Heterotaxy_13-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Visceral_Heterotaxy_13-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
| Terms checked | 45 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

42 of 45 terms resolved to a current term; the rest could not be looked up either way.