---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T12:37:20.599878'
end_time: '2026-10-14T13:05:22.786173'
duration_seconds: 1682.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: DNASE2 Deficiency
  mondo_id: MONDO:0800132
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DNASE2_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DNASE2_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DNASE2 Deficiency
- **MONDO ID:** MONDO:0800132 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DNASE2 Deficiency** covering all of the
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

# DNASE2 Deficiency (Autoinflammatory–Pancytopenia Syndrome, AIPCS): Comprehensive Disease Characteristics Report

**Disease:** DNASE2 Deficiency / Autoinflammatory–Pancytopenia Syndrome (AIPCS)
**MONDO:** MONDO:0800132 · **OMIM:** #619858 · **Category:** Mendelian (autosomal recessive)

> Evidence base: This is an ultra-rare disease with a small primary human literature (first described 2017). Mechanistic depth comes largely from mouse genetics, which recapitulate the human phenotype well. Evidence-source types are flagged throughout as **[human]**, **[mouse]**, **[in vitro]**, or **[computational]**.

---

## Summary

DNASE2 deficiency — formally designated **Autoinflammatory–Pancytopenia Syndrome (AIPCS; MONDO:0800132, OMIM #619858)** — is an ultra-rare, autosomal-recessive monogenic **type I interferonopathy** caused by biallelic loss-of-function variants in *DNASE2* (chromosome 19p13.13). The gene encodes **DNase II-alpha**, a 360-amino-acid ubiquitously expressed lysosomal acid endonuclease that degrades DNA derived from apoptotic cells and from nuclei expelled by erythroblasts during definitive erythropoiesis. When this enzyme is lost, undegraded self-DNA accumulates within macrophage lysosomes and leaks to the cytosol, where it is sensed by the **TLR-independent cGAS–STING–TBK1–IRF3/7** axis. The result is constitutive overproduction of type I interferon (principally IFN-β), accompanied by a separable TNF-α–driven inflammatory program, which together produce a congenital/neonatal-onset multisystem autoinflammatory disease.

The core human phenotype, first defined by Rodero et al. in 2017, comprises severe neonatal anemia, membranoproliferative glomerulonephritis, liver fibrosis, deforming arthropathy, and anti-DNA antibodies, all on a background of a strong blood interferon signature and constitutive STAT1/STAT3 phosphorylation. Subsequent case reports have expanded the spectrum to include an extremely severe antenatal presentation (fetal hydrops, intrauterine growth restriction, cardiomyopathy, persistent pancytopenia, hepatosplenomegaly, cholestatic jaundice, and hemophagocytic lymphohistiocytosis–like features with marked hyperferritinemia), as well as recurrent fevers, vasculitic skin lesions/chilblains, gastrointestinal inflammation, lipodystrophy, and subcortical white-matter lesions.

The disease mechanism is exceptionally well validated by *Dnase2*-null mouse genetics: embryonic lethality from IFN-β–driven lethal anemia is rescued by crossing onto an *Ifnar*-null background, sensing is TLR-independent, and the surviving mice develop a chronic, TNF-α–dependent, rheumatoid-arthritis-like polyarthritis driven in part by IFN-γ–producing Th1 cells independent of type I IFN. Diagnosis rests on the blood interferon signature, reduced DNase II enzymatic activity, and exome/genome sequencing. Mechanism-directed treatment centers on **JAK1/2 inhibitors** (baricitinib, ruxolitinib) to suppress IFN signaling, with a strong preclinical rationale for anti-TNF therapy against the arthritis component and hematopoietic stem-cell transplantation as a conceptual cure.

---

## Key Findings

### F001 — DNASE2 deficiency is an autosomal-recessive type I interferonopathy caused by biallelic loss-of-function *DNASE2* variants **[human]**

The defining human study is Rodero et al. (2017), which identified biallelic *DNASE2* mutations in three patients from two families, each with loss of DNase II endonuclease activity, elevated IFN-alpha protein measured by digital ELISA, enhanced interferon signaling on RNA-Seq, and constitutive upregulation of phosphorylated STAT1 and STAT3 in patient lymphocytes and monocytes. In the authors' words: *"In both families we identify biallelic mutations in DNASE2, associated with a loss of DNase II endonuclease activity. We record increased interferon alpha protein levels using digital ELISA, enhanced interferon signaling by RNA-Seq analysis and constitutive upregulation of phosphorylated STAT1 and STAT3 in patient lymphocytes and monocytes"* [PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/). Subsequent reports confirmed additional biallelic/homozygous pathogenic variants, including a proximal intronic splice-site variant causing type I interferon-mediated autoinflammation in two unrelated patients [PMID: 41472683](https://pubmed.ncbi.nlm.nih.gov/41472683/), which describes DNase II as *"a lysosomal endonuclease critical for degrading DNA during erythropoiesis and apoptosis"* and confirms recessive biallelic loss-of-function inheritance. This establishes the disease as a monogenic, recessive interferonopathy with a clear molecular signature.

### F002 — Core clinical phenotype: neonatal anemia, membranoproliferative glomerulonephritis, liver fibrosis, deforming arthropathy, and anti-DNA antibodies **[human]**

The index cohort variably demonstrated a stereotyped multisystem picture: *"we identify two siblings and a singleton variably demonstrating severe neonatal anemia, membranoproliferative glomerulonephritis, liver fibrosis, deforming arthropathy and increased anti-DNA antibodies"* [PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/). Peripheral blood showed increased erythroblasts and a hematological-disease transcriptomic signature, linking the anemia directly to the enzyme's erythropoietic role. The 2026 Omani neonatal report expanded the severe end of the spectrum, with disease *"manifesting antenatally with fetal hydrops, intrauterine growth restriction, and cardiomyopathy. Postnatally, the infant developed persistent pancytopenia, hepatosplenomegaly, cholestatic jaundice, and hemophagocytic lymphohistiocytosis-like features, including marked hyperferritinemia"* [PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/).

### F003 — Mechanism: undegraded self-DNA drives cGAS–STING-dependent type I IFN, with an IFNAR-independent inflammatory branch **[mouse, in vitro]**

Mouse genetics establish an unambiguous causal chain. *Dnase2*-null embryos accumulate undigested DNA in macrophages and die in utero from IFN-β–driven lethal anemia; crucially, *"When the DNase II-deficient mice were crossed with mice deficient in type I interferon receptor, the resultant 'double-mutant' mice were born healthy"* [PMID: 15568025](https://pubmed.ncbi.nlm.nih.gov/15568025/), proving type I IFN signaling via IFNAR is causally required for lethal anemia. Sensing is TLR-independent: *"The ablation of Toll-like receptor (TLR) 3 and 9, or their adaptor molecules (MyD88 and TRIF), had no effect on the lethality of the DNase II(-/-) mice. These results indicate that there is a TLR-independent sensing mechanism"* [PMID: 16301743](https://pubmed.ncbi.nlm.nih.gov/16301743/), implicating cytosolic cGAS–STING. This is confirmed functionally: DNase2-deficient patient fibroblasts have a constitutively primed cGAS–STING–TBK1 pathway [PMID: 33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/). A type I IFN-independent branch also contributes — in *Dnase2/Ifnar* double-knockout mice, chronic polyarthritis is driven by IFN-γ–producing Th1 cells [PMID: 31464028](https://pubmed.ncbi.nlm.nih.gov/31464028/) — and STING contributes to paradoxical ectopic bone formation [PMID: 27740718](https://pubmed.ncbi.nlm.nih.gov/27740718/).

### F004 — DNase II acts non-cell-autonomously in macrophages to degrade erythroid-expelled nuclear DNA; it is essential for definitive erythropoiesis **[mouse]**

Kawane et al. (2001) showed that DNase II-null mice are not born, dying of severe anemia, and that transfer of mutant fetal liver cells into irradiated wild-type mice generated mature red blood cells, demonstrating a non-cell-autonomous mechanism. Histochemistry localized the critical enzyme source: *"the critical cellular sources of DNase II are macrophages present at the site of definitive erythropoiesis in the fetal liver. Thus, DNase II in macrophages appears to be responsible for destroying the nuclear DNA expelled from erythroid precursor cells"* [PMID: 11375492](https://pubmed.ncbi.nlm.nih.gov/11375492/). This directly explains the anemia: central nurse macrophages in erythroblastic islands normally phagocytose and digest the extruded erythroblast nucleus, and without DNase II this DNA accumulates and triggers IFN.

### F005 — Two-branch mechanism: IRF3/7-dependent IFN-β drives embryonic anemia; TNF-α drives chronic polyarthritis (IFN-independent) **[mouse]**

Kawane et al. (2006) found that *Dnase2⁻/⁻ Ifnar⁻/⁻* mice (and mice with induced DNase II deletion) develop chronic, destructive polyarthritis resembling rheumatoid arthritis, with high serum anti-CCP antibody, rheumatoid factor, and MMP-3. *"Early in the pathogenesis, expression of the gene encoding tumour necrosis factor (TNF)-alpha was upregulated in the bone marrow, and administration of anti-TNF-alpha antibody prevented the development of arthritis"* [PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/). Okabe et al. (2008) dissected the transcriptional logic: *"DNase II(-/-)IRF3(-/-)IRF7(-/-) mice do not suffer from anemia, but they still produce TNF-alpha, and age-dependently develop chronic polyarthritis"* [PMID: 18991290](https://pubmed.ncbi.nlm.nih.gov/18991290/). Thus two separable gene-induction programs flow from the same undegraded DNA: an IRF3/7-dependent IFN-β program (anemia) and an IRF3/7-independent TNF-α program (arthritis). HMGB-1 is an additional pathogenic mediator in the arthritis model, with HMGB-1 blockade ameliorating disease [PMID: 20533288](https://pubmed.ncbi.nlm.nih.gov/20533288/).

### F006 — *DNASE2* gene/protein: chromosome 19, a 360-aa ubiquitously expressed lysosomal acid endonuclease **[human]**

Yasuda et al. (1998) cloned the human DNase II cDNA: *"an open reading frame of 1080 bases, which encoded a single polypeptide of 360 amino acids (signal peptide, 16; propeptide, 91; mature protein, 253)"* and established that *"DNase II is ubiquitously expressed in human tissues, and the DNase II gene (DNASE2) was assigned to chromosome 19"* [PMID: 9446563](https://pubmed.ncbi.nlm.nih.gov/9446563/). The enzyme is an acid, divalent-cation-independent endonuclease active at lysosomal pH, with a cDNA organization resembling the lysosomal cathepsin families.

### F007 — Treatment: JAK inhibitors as targeted therapy; anti-TNF rationale for arthritis; HSCT conceptually curative **[human, mouse]**

In the severe antenatal case, *"Whole-exome sequencing enables definitive diagnosis, and Janus kinase inhibitors have emerged as targeted immunomodulatory therapy"* [PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/). JAK1/2 inhibitors (baricitinib, ruxolitinib) reduce the interferon signature and systemic/dermatologic inflammation across type I interferonopathies, with greater benefit in mild/intermediate phenotypes and earlier initiation [PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/). The mouse arthritis branch is prevented by *"administration of anti-TNF-alpha antibody"* [PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/). Allogeneic HSCT achieved cure in the related interferonopathy SAVI [PMID: 42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/), supporting a hematopoietic-targeted curative strategy since DNase II's critical role is in macrophages.

### F008 — *DNASE2* is loss-of-function tolerant in gnomAD, consistent with recessive inheritance and healthy carriers **[computational]**

gnomAD constraint metrics for *DNASE2* (ENSG00000105612) indicate tolerance of heterozygous loss of function: pLI ≈ 1.5×10⁻⁸ (effectively 0), observed/expected LoF = 0.87 (90% CI 0.64–1.21), lof_z = 0.59, mis_z = 0.81. This is exactly the constraint signature expected of a recessive disease gene where carriers are unaffected. Verified identifiers (via mygene.info): HGNC:2960, Entrez 1777, Ensembl ENSG00000105612, locus 19p13.13, UniProt O00115; mouse ortholog *Dnase2a* (Entrez 13423, MGI:1329019).

### F009 — Authoritative identifiers and ontology annotations **[computational]**

EBI OLS4 gives MONDO:0800132 the official label *"autoinflammatory-pancytopenia syndrome due to DNASE2 deficiency,"* with cross-references OMIM:619858 (phenotype), UMLS:C5676977, and MedGen:1803642. The gene alias "AIPCS" is the phenotype acronym (Autoinflammatory–Pancytopenia Syndrome). UniProt O00115 GO annotations include GO:0004531 (deoxyribonuclease II activity, molecular function), GO:0006309 (apoptotic DNA fragmentation), GO:0043277 (apoptotic cell clearance), GO:0005764 (lysosome), and GO:0070062 (extracellular exosome). The catalytic activity is endonucleolytic cleavage to nucleoside 3′-phosphate / 3′-phospho-oligonucleotide products; the enzyme is an acidic-pH dsDNA-preferring hydrolase necessary for definitive erythropoiesis.

### F010 — Authoritative HPO phenotype spectrum expands features beyond the index report **[human]**

The JAX HPO annotation of OMIM:619858 (MONDO:0800132) catalogs a broad spectrum: severe anemia (HP:0001903), thrombocytopenia (HP:0001873), pancytopenia (HP:0001876), hemophagocytosis (HP:0012156), hepatosplenomegaly (HP:0001433), hepatic fibrosis (HP:0001395), cholestatic liver disease (HP:0002611), membranoproliferative glomerulonephritis (HP:0000793), proteinuria (HP:0000093), arthropathy (HP:0003040), recurrent fever/fever (HP:0001954/HP:0001945), chilblains (HP:0009710), granuloma (HP:0032252), chronic diarrhea (HP:0002028), intestinal inflammation (HP:4000055), failure to thrive/growth delay (HP:0001508/HP:0001510), motor delay (HP:0001270/HP:0002194), lipodystrophy (HP:0009125), type 1 diabetes (HP:0100651), and severe EBV infection (HP:0031693). Onset is congenital (HP:0003577)/neonatal (HP:0003623); inheritance is autosomal recessive (HP:0000007). The OMIM description additionally notes vasculitic skin lesions and subcortical white-matter lesions on brain imaging.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** DNASE2 deficiency is a monogenic autosomal-recessive systemic autoinflammatory disorder classified as a **type I interferonopathy**. Loss of the lysosomal enzyme DNase II leads to accumulation of undegraded self-DNA, chronic type I interferon production, and multisystem inflammation beginning before or at birth.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0800132 ("autoinflammatory-pancytopenia syndrome due to DNASE2 deficiency") |
| OMIM (phenotype) | #619858 |
| UMLS | C5676977 |
| MedGen | 1803642 |
| Gene (HGNC) | *DNASE2*, HGNC:2960 |
| Entrez Gene | 1777 |
| Ensembl | ENSG00000105612 |
| UniProt | O00115 |
| Orphanet | Not established as a distinct ORPHA code at time of research (ultra-rare; <10 reported families) |
| ICD-10/ICD-11 | No specific code; falls under autoinflammatory/immunodeficiency groupings |
| MeSH | No dedicated descriptor; indexed via *DNASE2* and "interferon type I" |

**Synonyms / alternative names:** AIPCS; Autoinflammatory–Pancytopenia Syndrome; DNase II deficiency; DNase II-alpha deficiency; type I interferon-mediated autoinflammation due to DNase II deficiency.

**Information source:** Disease-level knowledge is derived from a small number of individual patient reports (aggregated into OMIM/MONDO/HPO disease-level resources) plus extensive *Dnase2*-null mouse model data. This is **not** EHR/population-derived; it is individual-patient and model-organism derived.

### 2. Etiology

**Causal factors.** The disease is **purely genetic**: biallelic (homozygous or compound heterozygous) loss-of-function variants in *DNASE2* [PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/). There is no infectious or primary environmental cause.

**Genetic risk factors.** The only established risk factor is inheritance of two loss-of-function *DNASE2* alleles. *DNASE2* is LoF-tolerant in gnomAD (pLI ≈ 0, LOEUF upper bound 1.21), so heterozygous carriers are healthy (F008). Consanguinity increases risk of homozygosity, as expected for any ultra-rare recessive disorder; several reported cases are from consanguineous or isolated-population backgrounds (e.g., the Omani neonate, [PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/)).

**Environmental risk / protective factors.** None established. As a Mendelian monogenic disorder, environmental exposures are not primary determinants. Mechanistically, a bacterial/LPS (TLR4) stimulus can amplify IFN output in cells with a primed cGAS–STING pathway [PMID: 33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/), suggesting infections could trigger flares, but this is inferred rather than demonstrated clinically.

**Protective genetic factors.** In mice, loss of IFNAR, STING, or IRF3/7 rescues or attenuates disease — these are experimental "protective" modifiers establishing the pathway, not naturally occurring human protective alleles (F003, F005).

**Gene–environment interactions.** Not formally characterized in humans. The cGAS–STING priming data ([PMID: 33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/)) imply plausible interaction between the genetic lesion and microbial/LPS exposure, but this remains hypothetical.

### 3. Phenotypes

The phenotype is congenital/neonatal-onset, severe, progressive, and multisystem. Frequencies are qualitative given the ultra-rare cohort (fewer than ~10 reported patients).

| Phenotype | HPO term | Type | Onset | Severity | Notes |
|---|---|---|---|---|---|
| Severe anemia | HP:0001903 | Lab/clinical | Neonatal/antenatal | Severe | Core feature; from failed erythroblast DNA clearance |
| Thrombocytopenia | HP:0001873 | Lab | Neonatal | Moderate–severe | Part of pancytopenia |
| Pancytopenia | HP:0001876 | Lab | Neonatal | Severe | Severe spectrum |
| Hemophagocytosis / HLH-like | HP:0012156 | Lab/clinical | Neonatal | Severe | With hyperferritinemia (PMID 42491852) |
| Hepatosplenomegaly | HP:0001433 | Clinical sign | Neonatal | Moderate–severe | |
| Hepatic fibrosis | HP:0001395 | Pathology | Infancy | Progressive | |
| Cholestatic liver disease | HP:0002611 | Lab/clinical | Neonatal | Variable | |
| Membranoproliferative glomerulonephritis | HP:0000793 | Pathology | Childhood | Progressive | With proteinuria (HP:0000093) |
| Deforming arthropathy | HP:0003040 | Clinical sign | Childhood | Progressive, deforming | TNF-driven branch |
| Recurrent fever | HP:0001954 / HP:0001945 | Symptom | Early | Episodic | Autoinflammatory |
| Chilblains / vasculitic skin lesions | HP:0009710 | Physical | Early | Variable | Interferonopathy skin signature |
| Granuloma | HP:0032252 | Pathology | Variable | — | |
| Intestinal inflammation / chronic diarrhea | HP:4000055 / HP:0002028 | Clinical | Early | Variable | |
| Failure to thrive / growth delay | HP:0001508 / HP:0001510 | Clinical | Infancy | Variable | |
| Motor delay | HP:0001270 / HP:0002194 | Neurodevelopmental | Infancy | Variable | |
| Lipodystrophy | HP:0009125 | Physical | Variable | — | Shared with other interferonopathies |
| Type 1 diabetes | HP:0100651 | Lab/clinical | Variable | — | |
| Severe EBV infection | HP:0031693 | Clinical | Variable | — | |
| Subcortical white-matter lesions | (imaging) | Imaging | Variable | — | Per OMIM description |
| Increased anti-DNA antibodies | — | Lab | Childhood | — | Lupus-like autoimmunity |

**Quality-of-life impact:** Given congenital onset, severe anemia/pancytopenia, progressive organ fibrosis, and deforming arthropathy, affected children have substantial functional impairment and dependence on transfusion and immunomodulation. No disease-specific EQ-5D/SF-36/PROMIS data exist for this ultra-rare condition.

### 4. Genetic/Molecular Information

**Causal gene:** *DNASE2* (DNase II-alpha), HGNC:2960, Entrez 1777, Ensembl ENSG00000105612, UniProt O00115, locus **19p13.13**; phenotype OMIM #619858.

**Pathogenic variants.** Biallelic loss-of-function variants cause disease. Reported types include missense variants abolishing endonuclease activity (index families, [PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/)), a novel *DNASE2* mutation in a severe antenatal case ([PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/)), and a **proximal intronic splice-site variant** in two unrelated patients ([PMID: 41472683](https://pubmed.ncbi.nlm.nih.gov/41472683/)). Under ACMG/AMP criteria, disease-causing alleles are classified pathogenic/likely pathogenic when they ablate DNase II enzymatic activity. **Functional consequence: loss of function** (reduced/absent acid DNase II activity). Origin is **germline**; no somatic/cancer association. Population allele frequencies for pathogenic alleles are extremely low (ultra-rare), consistent with gnomAD LoF tolerance for carriers (F008).

**Modifier genes.** No human modifiers confirmed. In mice, the pathway genes *Ifnar1*, *Sting1 (Tmem173)*, *Irf3*, and *Irf7* act as powerful genetic modifiers of outcome (anemia vs arthritis vs rescue; F003/F005).

**Epigenetics / chromosomal abnormalities.** Not implicated; the disease is a single-gene disorder with no reported large-scale structural or epigenetic lesions.

### 5. Environmental Information

No environmental toxins, radiation, lifestyle factors, or infectious agents are established as causes. The disease is monogenic. The only mechanistically plausible environmental modulator is microbial/LPS stimulation amplifying IFN in cGAS–STING-primed cells ([PMID: 33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/)) — potentially relevant to flares but unproven clinically. Severe EBV infection (HP:0031693) appears in the HPO spectrum, which may reflect secondary infection susceptibility rather than a trigger.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function *DNASE2* variants **result in** absent/severely reduced lysosomal acid DNase II activity (F001, F006).
2. Loss of DNase II **leads to** failure to degrade DNA delivered to macrophage lysosomes — specifically the nuclei expelled by erythroblasts during definitive erythropoiesis and DNA from engulfed apoptotic cells (F004).
3. Undegraded self-DNA **accumulates** in macrophage lysosomes and **leaks into** the cytosol (inferred from priming data; F003).
4. Cytosolic self-DNA **activates** the TLR-independent **cGAS–STING–TBK1** sensing pathway (F003; TLR-independence demonstrated, [PMID: 16301743](https://pubmed.ncbi.nlm.nih.gov/16301743/)).
5. **Branch A (IRF3/7-dependent):** TBK1 activates IRF3/IRF7 → transcription of **IFN-β** → autocrine/paracrine IFNAR signaling → JAK–STAT1/STAT3 phosphorylation → interferon-stimulated gene program. In the embryo this **causes** lethal anemia; rescued by IFNAR loss (F003, F005).
6. **Branch B (IRF3/7-independent):** the same DNA induces **TNF-α** (and HMGB-1) independent of IRF3/7 and type I IFN → **chronic deforming polyarthritis**; prevented by anti-TNF, and in *Ifnar*-null mice driven further by **IFN-γ–producing Th1 cells** (F005; [PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/), [PMID: 18991290](https://pubmed.ncbi.nlm.nih.gov/18991290/), [PMID: 31464028](https://pubmed.ncbi.nlm.nih.gov/31464028/)).
7. Sustained IFN/TNF/IFN-γ signaling **produces** the human multisystem disease: anemia/pancytopenia, HLH-like macrophage activation, liver fibrosis, membranoproliferative glomerulonephritis, vasculitic skin disease, GI inflammation, and anti-DNA autoimmunity (F002, F010).
8. A STING-dependent side-branch **contributes to** paradoxical ectopic bone formation at sites of DNA accrual (F003; [PMID: 27740718](https://pubmed.ncbi.nlm.nih.gov/27740718/)).

```
 DNASE2 LoF (lysosome)
        │ no DNA degradation
        ▼
 Undegraded self-DNA in macrophages  ── UBERON: fetal liver, bone marrow
        │ cytosolic leak
        ▼
 cGAS ─► STING ─► TBK1   (TLR-independent)
        │                         │
   IRF3/7 dependent          IRF3/7 independent
        │                         │
      IFN-β ─► IFNAR          TNF-α / HMGB-1 ─► (Th1/IFN-γ)
        │ JAK-STAT1/3             │
   ANEMIA, IFN signature      CHRONIC ARTHRITIS
   (rescued by Ifnar-/-)      (blocked by anti-TNF)
```

**Molecular pathways:** cGAS–STING cytosolic DNA sensing; type I IFN / JAK–STAT; TNF-α signaling (KEGG/Reactome: "Cytosolic DNA-sensing pathway," "Interferon alpha/beta signaling").

**Cellular processes:** apoptotic DNA fragmentation (GO:0006309), apoptotic cell clearance (GO:0043277), definitive erythropoiesis, macrophage-mediated phagocytosis, chronic inflammation, autoinflammation.

**Protein dysfunction:** loss of deoxyribonuclease II activity (GO:0004531); the catalytic endonuclease fails to cleave dsDNA to 3′-phosphate products.

**Immune system involvement:** combined innate autoinflammation (IFN-β, TNF-α) and adaptive autoimmunity (anti-DNA antibodies, Th1/IFN-γ, anti-CCP/RF in the murine model).

**Cell types (CL):** macrophage (CL:0000235), erythroblast/erythroid precursor (CL:0000765), monocyte (CL:0000576), T-helper 1 cell (CL:0000545).

**Subcellular compartment (GO CC):** lysosome (GO:0005764); cytosol (site of cGAS sensing); extracellular exosome (GO:0070062).

**Molecular profiling:** patient RNA-Seq shows an enhanced interferon signature; blood IFN signatures (6-gene ISG panels) are measurable by RT-qPCR/Nanostring [PMID: 30413290](https://pubmed.ncbi.nlm.nih.gov/30413290/); proteomic ISG signatures (IFIT5, ISG15, OAS2) are detectable even in neonatal dried blood spots [PMID: 40319946](https://pubmed.ncbi.nlm.nih.gov/40319946/).

### 7. Anatomical Structures Affected

- **Primary organs/systems:** hematopoietic system and **bone marrow/fetal liver** (UBERON:0002371 / UBERON:0002107) — site of erythropoiesis and the primary lesion; **liver** (UBERON:0002107) — fibrosis/cholestasis; **kidney** (UBERON:0002113) — membranoproliferative glomerulonephritis; **joints/synovium** (UBERON:0002217) — deforming arthropathy; **skin** (UBERON:0002097) — vasculitis/chilblains.
- **Secondary involvement:** spleen (hepatosplenomegaly), gastrointestinal tract (intestinal inflammation), heart (cardiomyopathy in severe antenatal case), CNS white matter (subcortical lesions), endocrine pancreas (type 1 diabetes).
- **Body systems:** hematologic/immune, hepatobiliary, renal/urinary, musculoskeletal, integumentary, digestive, cardiovascular, nervous, endocrine.
- **Tissue/cell level:** macrophages (central nurse macrophages of erythroblastic islands), erythroid precursors, monocytes, synovial cells, glomerular cells; connective tissue (fibrosis).
- **Subcellular:** lysosome (primary), cytosol, nucleus (source of self-DNA).
- **Lateralization:** systemic/bilateral (e.g., polyarthritis is symmetric).

### 8. Temporal Development

- **Onset:** congenital (HP:0003577) to neonatal (HP:0003623); the most severe cases present antenatally with hydrops and IUGR ([PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/)).
- **Onset pattern:** acute/severe in neonates; chronic-progressive thereafter.
- **Progression:** progressive multisystem disease with accumulating organ fibrosis (liver, kidney) and deforming, destructive arthropathy; episodic fevers/flares superimposed.
- **Duration:** chronic, lifelong without disease-modifying therapy.
- **Critical period:** the perinatal/early-infancy window is the key period of vulnerability and the opportune time for intervention (early JAK-inhibitor initiation is associated with better outcomes in interferonopathies, [PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/)).

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007); biallelic LoF required.
- **Penetrance:** appears complete in biallelic LoF individuals (all reported cases affected); expressivity is **variable** (antenatal-lethal to childhood deforming arthropathy).
- **Carrier status:** heterozygotes are healthy; *DNASE2* LoF tolerance in gnomAD supports this (F008).
- **Epidemiology:** **ultra-rare** — fewer than ~10 patients reported worldwide across a handful of families; no reliable prevalence/incidence estimates. No dedicated Orphanet prevalence class.
- **Consanguinity/founder effects:** consanguinity elevates risk (reported in isolated-population cases); no established founder allele.
- **Sex ratio:** no sex bias expected or reported (autosomal recessive).
- **Geographic distribution:** cases reported from Europe and the Middle East (e.g., Oman); no endemic clustering beyond consanguineous pedigrees.

### 10. Diagnostics

- **Laboratory:** CBC (severe anemia, cytopenias, erythroblastosis), ferritin (markedly elevated in HLH-like disease), liver enzymes/bilirubin (cholestasis), urinalysis (proteinuria), autoantibodies (anti-DNA, and in the mouse model anti-CCP/RF/MMP-3).
- **Functional enzyme assay:** reduced/absent DNase II endonuclease activity is a specific confirmatory test ([PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/)).
- **Biomarker — interferon signature:** the blood IFN signature (6-gene ISG panel by RT-qPCR or Nanostring) is the gold-standard screen for type I interferonopathies [PMID: 30413290](https://pubmed.ncbi.nlm.nih.gov/30413290/); IFN-alpha protein can be quantified by digital ELISA; constitutive p-STAT1/p-STAT3 in lymphocytes/monocytes supports the diagnosis. Neonatal dried-blood-spot proteomics (IFIT5, ISG15, OAS2) can reveal a subclinical/presymptomatic signature [PMID: 40319946](https://pubmed.ncbi.nlm.nih.gov/40319946/).
- **Imaging:** brain MRI (subcortical white-matter lesions); abdominal imaging (hepatosplenomegaly, fibrosis); joint imaging (erosive arthropathy); echocardiography (cardiomyopathy in severe cases).
- **Histopathology:** liver fibrosis; membranoproliferative glomerulonephritis on renal biopsy; bone marrow with erythroid changes/hemophagocytosis.
- **Genetic testing:** **WES or WGS** is the definitive diagnostic approach ([PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/): "Whole-exome sequencing enables definitive diagnosis"); targeted single-gene *DNASE2* testing or an interferonopathy/autoinflammatory gene panel can confirm biallelic variants. CMA/karyotype/FISH/mtDNA/repeat testing are not indicated (single-gene point/splice variants).
- **Differential diagnosis:** other type I interferonopathies — Aicardi–Goutières syndrome (TREX1, RNASEH2A/B/C, SAMHD1, ADAR, IFIH1), SAVI (*TMEM173/STING1*), ISG15 deficiency, USP18 deficiency, COPA syndrome — plus congenital infections (TORCH), neonatal lupus, HLH, and congenital dyserythropoietic anemias. DNase II deficiency is distinguished by the combination of severe neonatal anemia + glomerulonephritis + liver fibrosis + arthropathy with reduced DNase II activity and biallelic *DNASE2* variants.
- **Screening:** cascade carrier testing of relatives once a familial variant is known; the IFN/DBS signature could in principle support newborn screening but is not standard.

### 11. Outcome/Prognosis

- **Survival/mortality:** severe; the antenatal end of the spectrum carries high perinatal mortality (hydrops, cardiomyopathy, HLH-like disease) [PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/). The complete murine knockout is embryonic-lethal, underscoring the severity of total loss of function.
- **Morbidity:** high — transfusion-dependent anemia, progressive liver and renal disease, and destructive deforming arthropathy cause major disability.
- **Complications:** HLH/macrophage activation, end-organ fibrosis, renal failure risk, joint destruction, growth failure, infection susceptibility.
- **Prognostic factors:** severity of residual DNase II activity, age/timing of onset (antenatal = worst), and timeliness of IFN-targeted therapy. No validated prognostic biomarkers specific to this disease beyond the IFN signature as an activity marker.
- **Recovery:** without disease-modifying therapy the course is chronic-progressive; JAK inhibition and (conceptually) HSCT may substantially alter outcome.

### 12. Treatment

- **Pharmacotherapy — JAK inhibitors (primary targeted therapy; NCIT "Janus Kinase Inhibitor"):** baricitinib and ruxolitinib (JAK1/2) reduce the IFN signature and immunologic/dermatologic inflammation across interferonopathies ([PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/)); JAK inhibitors are explicitly highlighted as targeted therapy in DNASE2 deficiency ([PMID: 42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/)). Tofacitinib (JAK1/3) has benefited skin lesions in related interferonopathy ([PMID: 40176112](https://pubmed.ncbi.nlm.nih.gov/40176112/)). Monitoring for viral reactivation/infection is required.
- **Anti-TNF therapy (NCIT "TNF Inhibitor"):** strong preclinical rationale for the arthritis branch — anti-TNF-α antibody prevented polyarthritis in the mouse model ([PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/)).
- **Hematopoietic stem cell transplantation (NCIT "Allogeneic Hematopoietic Stem Cell Transplantation"):** conceptually curative because the critical DNase II function is in macrophages/hematopoietic cells; allo-HSCT cured the related interferonopathy SAVI ([PMID: 42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/)).
- **Supportive care:** red-cell transfusions, management of liver/renal disease, treatment of HLH-like flares, nutrition/growth support.
- **Experimental/future:** STING or cGAS inhibitors and IFNAR-targeting biologics are mechanistically rational but not yet used for this disease. Gene/enzyme-replacement approaches are theoretical.
- **Pharmacogenomics:** none specific; JAK-inhibitor dosing follows interferonopathy experience.

### 13. Prevention

- **Primary prevention:** not possible for a monogenic disease; **genetic counseling** and reproductive options (carrier testing, prenatal diagnosis, preimplantation genetic testing) are the mainstays for at-risk/consanguineous families.
- **Secondary prevention:** early recognition via the blood/DBS interferon signature and prompt genetic diagnosis enable early JAK-inhibitor initiation, which is associated with better outcomes ([PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/)); neonatal DBS proteomics may detect presymptomatic disease ([PMID: 40319946](https://pubmed.ncbi.nlm.nih.gov/40319946/)).
- **Tertiary prevention:** disease-modifying immunomodulation to prevent organ fibrosis and joint destruction; infection surveillance during immunosuppression.
- **Immunization/public-health/environmental measures:** not applicable (non-infectious, non-environmental).

### 14. Other Species / Natural Disease

- **Mouse ortholog:** *Dnase2a* (Entrez 13423, MGI:1329019), NCBI Taxon 10090 (*Mus musculus*). The mechanism is evolutionarily conserved: macrophage DNase II is required for definitive erythropoiesis and for preventing DNA-driven IFN/TNF autoinflammation (F003–F005).
- **Natural disease in other species:** no well-documented naturally occurring DNASE2-deficiency disease in companion animals or wildlife is recorded in the reviewed literature; the knowledge base is dominated by engineered mouse models.
- **Comparative biology:** the murine phenotypes (embryonic-lethal anemia; chronic polyarthritis on *Ifnar*-null background) recapitulate the human hematologic and articular features, making the mouse an excellent comparative model.
- **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms

- **Primary model:** the **mouse** (*Mus musculus*, Taxon 10090), *Dnase2a* (MGI:1329019).
- **Genetic models available:**
  - *Dnase2⁻/⁻* constitutive knockout — embryonic-lethal severe anemia from macrophage-accumulated DNA and IFN-β ([PMID: 15568025](https://pubmed.ncbi.nlm.nih.gov/15568025/), [PMID: 11375492](https://pubmed.ncbi.nlm.nih.gov/11375492/)).
  - *Dnase2⁻/⁻ Ifnar⁻/⁻* double knockout — rescued from anemia, develops chronic RA-like polyarthritis ([PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/)).
  - *Dnase2⁻/⁻ Irf3⁻/⁻ Irf7⁻/⁻* triple knockout — no anemia, still TNF-α and arthritis, dissecting the two branches ([PMID: 18991290](https://pubmed.ncbi.nlm.nih.gov/18991290/)).
  - Inducible/conditional *Dnase2* deletion — adult-onset arthritis ([PMID: 17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/)).
  - Triple *Sting/Dnase2/Ifnar* knockout — demonstrates STING's role in ectopic bone ([PMID: 27740718](https://pubmed.ncbi.nlm.nih.gov/27740718/)).
- **Cellular models:** DNase2-deficient patient fibroblasts with a constitutively primed cGAS–STING–TBK1 pathway ([PMID: 33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/)); patient lymphocytes/monocytes showing constitutive p-STAT1/3 ([PMID: 29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/)).
- **Phenotype recapitulation:** excellent for the hematologic (anemia) and articular (arthritis) components and for the IFN/TNF mechanism. **Limitations:** the complete knockout's embryonic lethality requires genetic rescue (IFNAR loss) to study post-natal disease, which alters the IFN axis; some human features (glomerulonephritis, liver fibrosis, neurologic lesions) are less completely modeled.
- **Resources:** MGI (*Dnase2a*, MGI:1329019); Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

The pathophysiology of DNASE2 deficiency is one of the most cleanly resolved causal chains among the interferonopathies, because mouse genetics have epistatically ordered every step. The single initiating lesion — loss of lysosomal DNase II — removes the terminal nuclease that macrophages use to digest two major streams of self-DNA: the nuclei that erythroblasts expel during definitive erythropoiesis, and the chromatin of apoptotic cells they engulf. The undigested DNA becomes a danger signal. Because sensing is demonstrably TLR-independent and because it is abolished by removing STING-pathway components, the responsible sensor is cytosolic cGAS feeding STING–TBK1. From TBK1 the signal **bifurcates**: an IRF3/7-dependent arm makes IFN-β (producing the lethal fetal anemia and the human IFN signature), and an IRF3/7-independent arm makes TNF-α (and HMGB-1), producing the chronic deforming arthritis. A third, IFN-independent adaptive arm (IFN-γ–producing Th1 cells) amplifies the arthritis once type I IFN is removed.

This branched architecture directly rationalizes therapy. JAK inhibitors intercept the IFNAR→JAK–STAT limb and should dampen the IFN-driven systemic and hematologic/skin disease; anti-TNF should specifically address the arthritis limb; and HSCT, by replacing the macrophage compartment with DNase II-competent cells, addresses the lesion at its cellular source. The gnomAD constraint data close the loop on genetics: *DNASE2* tolerates heterozygous loss of function, exactly as required for a recessive disease whose carriers are healthy.

| Mechanistic step | Position | Key evidence | Source |
|---|---|---|---|
| DNASE2 LoF → no lysosomal DNA digestion | Upstream (initiating) | 29259162, 9446563 | human |
| Macrophage accumulation of erythroid/apoptotic DNA | Upstream | 11375492 | mouse |
| TLR-independent cytosolic sensing (cGAS-STING-TBK1) | Midstream | 16301743, 33916318 | mouse, in vitro |
| IRF3/7 → IFN-β → IFNAR → anemia | Downstream (branch A) | 15568025, 18991290 | mouse |
| IRF3/7-independent TNF-α → arthritis | Downstream (branch B) | 17066036, 18991290 | mouse |
| IFN-γ/Th1 amplification of arthritis | Downstream | 31464028 | mouse |
| Human multisystem disease | Terminal | 29259162, 42491852 | human |

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [29259162](https://pubmed.ncbi.nlm.nih.gov/29259162/) | Defining human study | Biallelic *DNASE2* LoF; IFN signature; core phenotype (F001, F002) |
| [41472683](https://pubmed.ncbi.nlm.nih.gov/41472683/) | Human case series | Intronic splice variant; confirms recessive LoF; lysosomal role (F001) |
| [42491852](https://pubmed.ncbi.nlm.nih.gov/42491852/) | Human case report | Severe antenatal spectrum; WES diagnosis; JAK inhibitors (F002, F007) |
| [11375492](https://pubmed.ncbi.nlm.nih.gov/11375492/) | Mouse | DNase II macrophage non-cell-autonomous role in erythropoiesis (F004) |
| [15568025](https://pubmed.ncbi.nlm.nih.gov/15568025/) | Mouse genetics | IFN-β/IFNAR causally required for lethal anemia (F003) |
| [16301743](https://pubmed.ncbi.nlm.nih.gov/16301743/) | Mouse genetics | TLR-independent self-DNA sensing → cGAS-STING (F003) |
| [33916318](https://pubmed.ncbi.nlm.nih.gov/33916318/) | Patient cells | Constitutively primed cGAS-STING-TBK1 in DNase2-deficient fibroblasts (F003) |
| [17066036](https://pubmed.ncbi.nlm.nih.gov/17066036/) | Mouse | TNF-α drives arthritis; anti-TNF protective (F005, F007) |
| [18991290](https://pubmed.ncbi.nlm.nih.gov/18991290/) | Mouse genetics | IRF3/7-dependent (anemia) vs independent (TNF/arthritis) branches (F005) |
| [31464028](https://pubmed.ncbi.nlm.nih.gov/31464028/) | Mouse | IFN-γ/Th1 drives type I IFN-independent arthritis (F003) |
| [27740718](https://pubmed.ncbi.nlm.nih.gov/27740718/) | Mouse | STING required for ectopic bone formation (F003) |
| [20533288](https://pubmed.ncbi.nlm.nih.gov/20533288/) | Mouse | HMGB-1 pathogenic in the arthritis model; blockade ameliorates |
| [9446563](https://pubmed.ncbi.nlm.nih.gov/9446563/) | Molecular | DNASE2 cloning; 360-aa protein; chr 19; ubiquitous expression (F006) |
| [30413290](https://pubmed.ncbi.nlm.nih.gov/30413290/) | Diagnostic | 6-gene IFN signature (RT-qPCR/Nanostring) for interferonopathies |
| [40319946](https://pubmed.ncbi.nlm.nih.gov/40319946/) | Diagnostic | Neonatal DBS proteomic IFN signature (IFIT5, ISG15, OAS2) |
| [41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/) | Treatment | JAK1/2 inhibitor efficacy in interferonopathies (F007) |
| [42137281](https://pubmed.ncbi.nlm.nih.gov/42137281/) | Treatment | Allo-HSCT cured SAVI — rationale for HSCT (F007) |
| [40176112](https://pubmed.ncbi.nlm.nih.gov/40176112/) | Treatment | Tofacitinib for interferonopathy skin lesions |

---

## Limitations and Knowledge Gaps

- **Ultra-rare N:** Fewer than ~10 human patients are reported; frequencies, penetrance, and genotype–phenotype correlations are qualitative, not statistical.
- **Human mechanism partly inferred:** The cytosolic leak of DNA and the precise cGAS–STING engagement in patients is supported by fibroblast priming data and by mouse genetics, but the full in-vivo human chain is inferred rather than directly demonstrated.
- **No validated human therapy trials:** JAK-inhibitor and anti-TNF evidence is extrapolated from related interferonopathies and the mouse model; no DNASE2-specific controlled trials exist. HSCT is conceptual for this disease (demonstrated only in SAVI).
- **Model caveats:** The complete *Dnase2* knockout is embryonic-lethal, so post-natal mechanisms are studied on genetically altered (IFNAR-null) backgrounds that themselves perturb the IFN axis; renal, hepatic, and neurologic features are less well modeled.
- **Epidemiology/prognosis:** No prevalence, survival, or QoL data specific to AIPCS; no Orphanet prevalence class; no natural-history cohort.
- **Identifiers:** Orphanet/ICD/MeSH do not yet carry a dedicated code for this ultra-rare entity.

## Proposed Follow-up Experiments / Actions

1. **Establish an international AIPCS patient registry** to aggregate genotype, phenotype, IFN-signature, treatment response, and survival data across the few families worldwide.
2. **Prospective JAK-inhibitor outcome study** (baricitinib/ruxolitinib) in confirmed DNASE2-deficiency patients, tracking IFN signature, transfusion requirement, hepatic/renal function, and arthropathy, with early vs late initiation comparison.
3. **Formal genotype–function correlation:** quantify residual DNase II activity for each reported variant (including the intronic splice allele) and relate to clinical severity along the antenatal-lethal → childhood-arthropathy spectrum.
4. **Direct in-patient cGAS–STING engagement assays** (e.g., cGAMP measurement, STING oligomerization) to confirm the inferred cytosolic-leak step in humans.
5. **Evaluate upstream pathway inhibitors** (cGAS or STING antagonists) in patient cells and *Dnase2*-null models as alternatives/adjuncts to JAK inhibition.
6. **Pilot/registry data on HSCT** for severe, refractory DNASE2 deficiency, given the macrophage-restricted critical function and the SAVI precedent.
7. **Validate neonatal DBS IFN-proteomic screening** prospectively in at-risk (consanguineous) pregnancies for presymptomatic detection and early intervention.

---

*Report compiled from 10 confirmed findings and 22 reviewed papers across 5 investigation iterations. Evidence types are distinguished throughout as human clinical, model organism (mouse), in vitro (patient cells), or computational (gnomAD/ontology).*


## Artifacts

- [OpenScientist final report](DNASE2_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DNASE2_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 26 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800132` (6 mentions) - the report calls it "if available", "autoinflammatory-pancytopenia syndrome due to DNASE2 deficiency"; MONDO calls it **autoinflammatory-pancytopenia syndrome due to DNASE2 deficiency**
- `UBERON:0002217` (1 mention) - the report calls it "joints/synovium"; UBERON calls it **synovial joint**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004531` (2 mentions) - the report calls it "deoxyribonuclease II activity, molecular function"; GO calls it **deoxyribonuclease II activity**
- `HP:0001903` (2 mentions) - the report calls it "Severe anemia"; HP calls it **Anemia**
- `HP:0012156` (2 mentions) - the report calls it "Hemophagocytosis / HLH-like"; HP calls it **Hemophagocytosis**
- `HP:0003040` (2 mentions) - the report calls it "Deforming arthropathy"; HP calls it **Arthropathy**
- `HP:0009710` (2 mentions) - the report calls it "Chilblains / vasculitic skin lesions"; HP calls it **Chilblains**, and lists "Chilblain lesions" among its other names
- `HP:0031693` (3 mentions) - the report calls it "Severe EBV infection"; HP calls it **Severe Epstein Barr virus infection**, and lists "Severe EBV infection" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0800132` - called "if available", "autoinflammatory-pancytopenia syndrome due to DNASE2 deficiency"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `OMIM`, `UMLS`.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
