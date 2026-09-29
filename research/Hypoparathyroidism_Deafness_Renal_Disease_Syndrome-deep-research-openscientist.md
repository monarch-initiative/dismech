---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T19:10:49.597968'
end_time: '2026-09-23T19:55:04.506063'
duration_seconds: 2654.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypoparathyroidism-Deafness-Renal Disease Syndrome
  mondo_id: MONDO:0007797
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
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypoparathyroidism_Deafness_Renal_Disease_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypoparathyroidism_Deafness_Renal_Disease_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypoparathyroidism-Deafness-Renal Disease Syndrome
- **MONDO ID:** MONDO:0007797 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypoparathyroidism-Deafness-Renal Disease Syndrome** covering all of the
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

# Hypoparathyroidism–Deafness–Renal Disease Syndrome (HDR / Barakat Syndrome): A Comprehensive Disease Characterization

**Disease:** Hypoparathyroidism–Deafness–Renal Disease Syndrome (HDR syndrome; Barakat syndrome)
**MONDO ID:** MONDO:0007797 · **OMIM:** #146255 · **Causal gene:** *GATA3* (10p14) · **Category:** Mendelian, autosomal dominant

---

## Summary

Hypoparathyroidism–Deafness–Renal disease syndrome (HDR, also called Barakat syndrome) is a rare **autosomal-dominant Mendelian disorder** caused by **haploinsufficiency of the dual zinc-finger transcription factor *GATA3***, mapped to chromosome **10p14**. The landmark deletion-mapping work of Van Esch and colleagues in 2000 defined a critical ~200-kb region containing *GATA3* and demonstrated that a single ~50% reduction in functional GATA3 dose is sufficient to produce the disease ([PMID: 10935639](https://pubmed.ncbi.nlm.nih.gov/10935639/)). Because GATA3 is a developmental master regulator deployed independently in the pharyngeal pouches, inner ear, and developing kidney, its dosage reduction impairs **three parallel, tissue-specific transcriptional programs**, producing the characteristic — but frequently incomplete — triad of hypoparathyroidism, bilateral sensorineural deafness, and renal dysplasia.

The mechanistic core of HDR is now well established across human genetics and model organisms. In the parathyroid, GATA3 sits atop a **GATA3 → GCM2/GCMB → PTH transcriptional cascade** essential for parathyroid progenitor differentiation and survival ([PMID: 20484821](https://pubmed.ncbi.nlm.nih.gov/20484821/)). In the cochlea, GATA3 specifies the prosensory domain, drives hair-cell maturation and innervation, and maintains spiral ganglion neuron survival ([PMID: 23666531](https://pubmed.ncbi.nlm.nih.gov/23666531/), [PMID: 31069810](https://pubmed.ncbi.nlm.nih.gov/31069810/)). In the kidney, GATA3 is required for metanephric development, and its loss yields diverse dysplastic renal phenotypes that can progress to focal segmental glomerulosclerosis (FSGS) and end-stage renal disease (ESRD) ([PMID: 27387476](https://pubmed.ncbi.nlm.nih.gov/27387476/)). Phenotypic expressivity is highly variable — even within families — and is modulated by upstream developmental modifier pathways (**BMP, SHH/Hedgehog, Notch**) and, in larger 10p terminal deletions, by contiguous-gene (DiGeorge-2) effects.

Clinically, HDR is diagnosed by the biochemical signature of hypoparathyroidism (hypocalcemia, hyperphosphatemia, inappropriately low/normal PTH), audiometric confirmation of bilateral sensorineural hearing loss, renal imaging, and molecular confirmation via *GATA3* sequencing plus copy-number analysis (aCGH/MLPA/FISH) for whole-gene deletions. There is **no disease-modifying therapy**; management is organ-directed — calcium and activated vitamin D (or, increasingly, PTH-replacement with palopegteriparatide) for hypoparathyroidism, hearing aids/cochlear implants for deafness, and dialysis/transplantation for ESRD. Renal progression is the principal determinant of long-term prognosis. This report synthesizes 15 confirmed findings from 58 reviewed papers into a complete disease knowledge-base entry organized along the 15-section research template.

---

## Key Findings

### Finding 1 — HDR is caused by GATA3 haploinsufficiency at 10p14

Van Esch et al. (2000) performed deletion mapping in two HDR patients and defined a **critical ~200-kb region on 10p14–pter containing the *GATA3* gene**. They identified one nonsense mutation and two intragenic deletions predicting loss of function, and confirmed the mechanism by demonstrating **absent DNA binding of the mutant GATA3 protein**. This established GATA3 as the single causal gene and haploinsufficiency (a 50% loss of functional protein) as the disease mechanism. The authors concluded that "*GATA3 is essential in the embryonic development of the parathyroids, auditory system and kidneys*" ([PMID: 10935639](https://pubmed.ncbi.nlm.nih.gov/10935639/)), directly linking the single gene to the three organs of the clinical triad. HDR is inherited in an autosomal-dominant fashion (OMIM #146255).

### Finding 2 — GATA3 mutation spectrum and age-dependent penetrance

The 20-year review by Lemos & Thakker (2020) aggregated **124 families (177 patients)** and defined the mutation spectrum: **40% frameshift indels, 23% missense, 14% nonsense, 6% splice-site, 1% in-frame indels, 15% whole-gene deletions, and 1% whole-gene duplication** ([PMID: 32442337](https://pubmed.ncbi.nlm.nih.gov/32442337/)). Missense mutations cluster in the two zinc-finger domains. Penetrance of the three cardinal features differs: **deafness 93%, hypoparathyroidism 87%, renal defects 61%**, with mean ages of diagnosis of 15.3, 7.5, and 14.0 years respectively. Whole-gene deletions and truncating mutations are diagnosed earlier than missense variants, consistent with a dosage/severity relationship.

| Mutation type | Frequency | Notes |
|---|---|---|
| Frameshift indels | 40% | Truncating; typically LoF |
| Missense | 23% | Cluster in ZnF1/ZnF2 |
| Nonsense | 14% | Truncating |
| Whole-gene deletions | 15% | Earlier diagnosis; may include contiguous genes |
| Splice-site | 6% | |
| In-frame indels | 1% | |
| Whole-gene duplication | 1% | Rare |

| Feature | Penetrance | Mean age at diagnosis |
|---|---|---|
| Deafness (sensorineural) | 93% | 15.3 y |
| Hypoparathyroidism | 87% | 7.5 y |
| Renal defects | 61% | 14.0 y |

### Finding 3 — Structural basis: two zinc fingers with distinct functions

GATA3 is a **dual zinc-finger transcription factor**. Functional dissection of HDR missense mutants established a division of labor: the **C-terminal zinc finger (ZnF2) binds DNA**, while the **N-terminal zinc finger (ZnF1) stabilizes DNA binding and mediates interaction with the cofactor FOG (Friend of GATA)** ([PMID: 15705923](https://pubmed.ncbi.nlm.nih.gov/15705923/)). The ZnF1 missense mutant **Thr272Ile** reduced DNA-binding affinity, abolished interaction with ZnF1/ZnF6 of the cofactor FOG2, and reduced luciferase reporter activity by >65% (P<0.001) without disturbing nuclear localization ([PMID: 19723756](https://pubmed.ncbi.nlm.nih.gov/19723756/)). The ZnF1 mutant **R276P** reduced GATA-motif binding affinity while retaining FOG interaction ([PMID: 15705923](https://pubmed.ncbi.nlm.nih.gov/15705923/)). These mechanistic studies explain how point mutations produce partial loss of function equivalent to haploinsufficiency.

### Finding 4 — Model organism: Gata3-null mice show renal and neural-crest defects

*Gata3*−/− mouse embryos die by ~11 days post-coitum from **noradrenaline deficiency of the sympathetic nervous system** (reduced *Th* and *Dbh* mRNA). Pharmacological rescue with catechol intermediates prolonged survival and unmasked late defects including **renal hypoplasia and developmental defects in cephalic neural-crest-derived structures** ([PMID: 10835639](https://pubmed.ncbi.nlm.nih.gov/10835639/)). These phenotypes are directly relevant to the renal and craniofacial features of HDR and demonstrate that GATA3 is essential in multiple developmental lineages.

### Finding 5 — HDR renal phenotype is diverse, dysplastic, and can progress to ESRD/FSGS

Belge et al. (2017) studied 8 patients from 5 families plus a literature review: **sensorineural deafness in 100%, hypoparathyroidism in 6/8, renal abnormalities in 6/8**, described as "*diverse and of dysplastic nature*" ([PMID: 27387476](https://pubmed.ncbi.nlm.nih.gov/27387476/)). Three patients developed **nephrotic-range proteinuria and reached ESRD between ages 19 and 61**, with **FSGS histologically demonstrated in one**. The renal spectrum in HDR broadly includes renal dysplasia/hypoplasia, cysts, vesicoureteral reflux, agenesis, and hypocalciuric or proteinuric disease. Marked **intrafamilial variability** was noted (e.g., mother vs. son). This establishes renal disease as the most heterogeneous and prognostically important component of the triad.

### Finding 6 — Mechanism of sensorineural deafness

Mouse studies delineate a multi-step cochlear mechanism. Conditional *Gata3* knockout disrupts cochlear morphogenesis (shortened cochlear duct, fewer hair/supporting cells), **fails to specify the prosensory domain**, and causes apoptotic depletion of spiral ganglion neurons: "*Loss of Gata3 function leads to the failure in the specification of prosensory domain and subsequently, to increased cell death in the cochlear duct*" ([PMID: 23666531](https://pubmed.ncbi.nlm.nih.gov/23666531/)). Postnatally, GATA3 is required for the **biophysical maturation, growth, and innervation of inner hair cells and survival of outer hair cells**; heterozygous loss causes progressive hearing loss modeling HDR ([PMID: 31069810](https://pubmed.ncbi.nlm.nih.gov/31069810/)). Even with catecholamine rescue, Gata3-null ears show only partial morphogenesis — a cochlear duct forms but neurosensory development fails ([PMID: 21553382](https://pubmed.ncbi.nlm.nih.gov/21553382/)), matching the human hearing phenotype.

### Finding 7 — The GATA3 → GCM2/GCMB → PTH cascade underlies hypoparathyroidism

Grigorieva et al. (2010) provided the definitive parathyroid mechanism. *Gata3*+/− mice challenged with a low-calcium/vitamin-D-deficient diet showed **higher mortality, lower plasma calcium and PTH, and smaller parathyroid glands with reduced Ki-67 proliferation**. E11.5 *Gata3*+/− embryos had smaller parathyroid-thymus primordia with fewer *Gcm2*-expressing cells; *Gata3*−/− embryos showed **no *Gcm2* expression** and gross defects of the 3rd/4th pharyngeal pouches with absent parathyroid-thymus primordia. EMSA, luciferase, and ChIP assays showed **GATA3 binds a functional double-GATA motif in the *GCMB* (*GCM2*) promoter**: "*GATA3 is critical for the differentiation and survival of parathyroid progenitor cells and, with GCM2/B, forms part of a transcriptional cascade in parathyroid development and function*" ([PMID: 20484821](https://pubmed.ncbi.nlm.nih.gov/20484821/)).

### Finding 8 — GATA3 acts within a Notch/Hedgehog network in the pharyngeal pouch

Figueiredo et al. (2016), using an avian model, placed GATA3/GCM2 parathyroid specification downstream of **Hedgehog** and dependent on **Notch** signaling. Hedgehog loss reduced the *Gata3/Gcm2*-expression domain at median/anterior pouch territories, and Notch impairment reduced *Gcm2/Pth* parathyroid-fated domains and compromised gland development ([PMID: 27544844](https://pubmed.ncbi.nlm.nih.gov/27544844/)). GATA3 and GCM2 co-localize in the parathyroid-fated endoderm, embedding the HDR cascade within a conserved organogenesis network.

### Finding 9 — Large 10p deletions produce a contiguous-gene DiGeorge-2 phenotype

Two non-overlapping regions on 10p have distinct consequences. The **telomeric HDR1 region (10p14–pter, containing *GATA3*)** causes the HDR triad, whereas the more proximal **DGCR2 / DiGeorge critical region II (10p13–p14)** is associated with congenital heart defects (notably atrial septal defect), thymus hypoplasia/aplasia (T-cell defect), facial dysmorphism, and developmental delay: "*Haploinsufficiency of a more proximal region, located on 10p13-10p14, designated as DGCR2 is associated with congenital heart defects and thymus hypoplasia/aplasia or T cell defect*" ([PMID: 22407589](https://pubmed.ncbi.nlm.nih.gov/22407589/)). Patients with large terminal deletions may show both HDR and DiGeorge-2 features, and hypoparathyroidism-related hypocalcemia can worsen heart failure — one report noted hypocalcemia "*lasted for three weeks and resulted in repeated episodes of heart failure*" ([PMID: 18795911](https://pubmed.ncbi.nlm.nih.gov/18795911/)).

### Finding 10 — Germline HDR vs. somatic GATA3 alterations in cancer are distinct

HDR results from **heterozygous germline loss-of-function**. Separately, GATA3 is a recurrent **somatic driver in breast cancer** — mutated in ~8% of inflammatory breast cancers and frequently altered in luminal/ER+ tumors ([PMID: 40378057](https://pubmed.ncbi.nlm.nih.gov/40378057/)) — and serves as an immunohistochemical lineage marker for breast/urothelial carcinoma. Importantly, **no established increased cancer risk has been reported for constitutional HDR**; the germline and somatic contexts are mechanistically separate.

### Finding 11 — Treatment is organ-directed and symptomatic

There is no therapy that corrects GATA3 haploinsufficiency. Hypoparathyroidism is managed with **oral calcium and activated vitamin D (calcitriol/alfacalcidol)**, targeting low-normal serum calcium to avoid hypercalciuria, nephrocalcinosis, and stones — conventional treatment "*does not fully replace the functions of PTH and can lead to … nephrocalcinosis, kidney stones and brain calcifications*" ([PMID: 28857066](https://pubmed.ncbi.nlm.nih.gov/28857066/)). **PTH-replacement therapy** has advanced substantially: **palopegteriparatide (TransCon PTH)**, a long-acting PTH(1-34) prodrug, was "*approved … as the first true replacement therapy for hypoPT management*" ([PMID: 39987371](https://pubmed.ncbi.nlm.nih.gov/39987371/)). In the phase-3 PaTHway trial it produced a mean eGFR increase of **8.9 mL/min/1.73 m² (P<0.0001)** sustained through 104 weeks ([PMID: 42166177](https://pubmed.ncbi.nlm.nih.gov/42166177/)) — a renally relevant benefit for HDR patients. Deafness is managed with hearing aids/cochlear implants, and ESRD with dialysis and transplantation (long-term graft success is documented, [PMID: 41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/)).

### Finding 12 — Zebrafish recapitulates the HDR triad

Pan et al. (2025) identified a heterozygous *GATA3* missense variant **p.Cys288Tyr (c.863G>A, exon 4, ZnF region)** segregating with the complete triad in a Chinese family. In vivo zebrafish assays showed the variant "*deleterious impact … on the gill buds, otoliths, and pronephros*" ([PMID: 39505798](https://pubmed.ncbi.nlm.nih.gov/39505798/)) — the piscine analogs of parathyroid, auditory, and renal tissues — validating zebrafish as a tractable HDR model that recapitulates all three organ systems.

### Finding 13 — Diagnosis: biochemical triad plus GATA3 molecular/CMA testing

Diagnosis rests on (i) **hypocalcemia with hyperphosphatemia and inappropriately low/normal PTH**; (ii) **bilateral sensorineural hearing loss on audiometry**; and (iii) **renal anomalies on ultrasound**. Confirmation is by **GATA3 sequencing** and, for whole-gene deletions, **chromosomal microarray/aCGH, MLPA, or FISH**. Tanaka et al. (2026) used "*targeted next-generation sequencing-based kidney disease panels … and copy number variations were assessed using array comparative genomic hybridization*" ([PMID: 42595857](https://pubmed.ncbi.nlm.nih.gov/42595857/)). The triad is frequently incomplete: in a CKD cohort, "*only 40% exhibited the complete triad*", with deafness and renal manifestations predominating ([PMID: 42595857](https://pubmed.ncbi.nlm.nih.gov/42595857/)). Hypocalcemic seizures are a common presenting sign, and HDR can be misdiagnosed as Alport syndrome ([PMID: 41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/)).

### Finding 14 — Extended phenotype and surveillance

Rive Le Gouard et al. (2024) reported 28 patients plus a systematic review and found that features "*described as rare initially, do not seem to be so rare after all (genital malformations and basal ganglia calcifications)*", while hearing loss is "*almost always present*" ([PMID: 38940299](https://pubmed.ncbi.nlm.nih.gov/38940299/)). Missense pathogenic variants localize near the two zinc fingers. The authors recommend that "*follow up of patients with HDR syndrome should include monitoring of parathyroid function and vesicoureteral reflux in order to prevent complications*" ([PMID: 38940299](https://pubmed.ncbi.nlm.nih.gov/38940299/)). Additional reported features include hypocalcemic seizures/tetany, nephrolithiasis/nephrocalcinosis, and rare associations such as juvenile idiopathic arthritis ([PMID: 41190486](https://pubmed.ncbi.nlm.nih.gov/41190486/)).

### Finding 15 — Phenotypic variability modulated by BMP and SHH

Swartz et al. (2021, zebrafish) showed *gata3* is expressed in maxillary neural crest and required between 24–30 hpf for palate development, and that "*gata3 expression in maxillary neural crest requires Bmp signaling and … blocking Bmp signaling … can phenocopy gata3 mutants*"; GATA3 re-expression rescues Bmp-blockade defects, placing GATA3 **downstream of BMP** ([PMID: 34033651](https://pubmed.ncbi.nlm.nih.gov/34033651/)). **Shh signaling modulates the variable phenotypic output** of the Bmp–Gata3 pathway, and even *gata3*-null mutants show highly variable craniofacial defects — a developmental basis for the variable expressivity seen clinically.

---

## Complete Report by Research Template Section

### 1. Disease Information

HDR syndrome is a rare autosomal-dominant Mendelian disorder defined by the triad of **h**ypoparathyroidism, sensorineural **d**eafness, and **r**enal disease/dysplasia. It was first described by Barakat in 1977 and molecularly resolved in 2000 with the identification of *GATA3* haploinsufficiency ([PMID: 10935639](https://pubmed.ncbi.nlm.nih.gov/10935639/)).

**Key identifiers:** MONDO:0007797 · OMIM #146255 · Orphanet ORPHA:2237 · gene *GATA3* (HGNC:4172, NCBI Gene 2625). MeSH indexes it under hypoparathyroidism/sensorineural hearing loss/congenital abnormalities; ICD-10 maps approximately to E20.8 (other hypoparathyroidism) with additional codes for hearing loss and renal anomaly.

**Synonyms:** Barakat syndrome; HDR syndrome; hypoparathyroidism–sensorineural deafness–renal dysplasia syndrome; hypoparathyroidism–deafness–renal anomaly syndrome.

**Data source:** Knowledge here is derived from **aggregated disease-level resources** (OMIM, Orphanet), cohort/case-series literature (fewer than ~200–250 reported patients), and model-organism studies — not from large EHR datasets, reflecting the disease's rarity.

### 2. Etiology

- **Primary cause:** monoallelic loss-of-function of *GATA3* (10p14) — point mutations (frameshift, nonsense, missense, splice) or whole-gene/contiguous deletions (Findings 1–2).
- **Genetic risk factors:** the causal locus is *GATA3* itself; there are no established common susceptibility loci or modifier genes proven in humans, though **developmental modifier pathways (BMP, SHH, Notch, Hedgehog)** modulate expressivity in models (Findings 8, 15).
- **Environmental risk factors:** none established as causal. Dietary calcium/vitamin-D status modulates the *severity/penetrance* of hypocalcemia (the Gata3+/− mouse becomes symptomatic only under low-calcium challenge, Finding 7) — a gene–environment interaction relevant to clinical decompensation rather than to disease origin.
- **Protective factors:** none identified. There are no reported protective alleles.
- **Gene–environment interaction:** low dietary calcium/vitamin-D unmasks latent hypoparathyroidism in the haploinsufficient state (Finding 7).

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset | Frequency |
|---|---|---|---|---|
| Hypoparathyroidism / hypocalcemia | Lab abnormality | HP:0000829 / HP:0002901 | Neonatal–childhood (mean 7.5 y) | ~87% |
| Sensorineural hearing loss (bilateral) | Clinical sign | HP:0000407 | Congenital–childhood (mean 15.3 y) | ~93% |
| Renal dysplasia/hypoplasia/agenesis/cysts | Physical/imaging | HP:0000110 / HP:0000107 / HP:0000104 | Congenital–adult (mean 14.0 y) | ~61% |
| Hypocalcemic seizures/tetany | Symptom | HP:0002199 | Neonatal–childhood | Common presenting sign |
| Hyperphosphatemia | Lab abnormality | HP:0002905 | Concurrent with hypoPT | Frequent |
| Vesicoureteral reflux | Clinical sign | HP:0000076 | Childhood | Reported |
| Proteinuria / FSGS / ESRD | Lab/pathology | HP:0000093 / HP:0000097 / HP:0003774 | Adult | Subset (progressive) |
| Basal ganglia calcification | Imaging | HP:0002135 | Adult | Underrecognized |
| Genital/genitourinary malformation | Physical | HP:0000811 | Congenital | Underrecognized |

Severity and progression are **variable**; hearing loss is often progressive and near-universally penetrant (Findings 2, 6, 14). **Quality-of-life impact:** deafness affects communication and development (mitigated by early cochlear implantation); hypoparathyroidism carries risk of seizures and lifelong medication burden; ESRD imposes dialysis/transplant burden. Disease-specific QoL instruments have not been reported; general hypoparathyroidism data indicate substantial symptom burden.

### 4. Genetic / Molecular Information

- **Causal gene:** *GATA3* (HGNC:4172; OMIM *131320; 10p14), a dual C4-type zinc-finger transcription factor.
- **Variant spectrum (Finding 2):** 40% frameshift, 23% missense, 14% nonsense, 6% splice, 15% whole-gene deletions, 1% in-frame indels, 1% duplication. Missense variants cluster in ZnF1/ZnF2.
- **Variant classification:** pathogenic/likely-pathogenic per ACMG for truncating and validated missense variants; functional assays (EMSA, luciferase, yeast two-hybrid, zebrafish) resolve VUS (Findings 3, 12).
- **Allele frequency:** private/de novo or family-segregating; essentially absent from gnomAD (loss-of-function-intolerant gene).
- **Origin:** germline; many de novo. (Somatic GATA3 alterations are a separate oncologic phenomenon, Finding 10.)
- **Functional consequence:** loss of function / haploinsufficiency (Finding 1); some missense variants act via loss of DNA binding and/or loss of FOG cofactor interaction (Finding 3).
- **Modifier genes:** *GCM2/GCMB* (downstream effector, Finding 7); BMP/SHH/Notch pathway components as developmental modifiers (Findings 8, 15).
- **Chromosomal abnormalities:** 10p14–pter deletions of varying size; large terminal deletions extend into the DiGeorge-2 (DGCR2) region (Finding 9).

### 5. Environmental Information

No environmental, lifestyle, or infectious agents cause HDR. Dietary calcium/vitamin-D status modulates the clinical severity of hypocalcemia (Finding 7). No toxicological or occupational exposures are implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous loss-of-function lesion in *GATA3* (point mutation or deletion) **leads to** ~50% reduction of functional GATA3 protein (haploinsufficiency) — *demonstrated* ([PMID: 10935639](https://pubmed.ncbi.nlm.nih.gov/10935639/)).
2. Reduced GATA3 dose **results in** insufficient transcriptional activity at GATA target loci during development — *demonstrated in vitro* via loss of DNA binding and FOG interaction ([PMID: 15705923](https://pubmed.ncbi.nlm.nih.gov/15705923/), [PMID: 19723756](https://pubmed.ncbi.nlm.nih.gov/19723756/)).
3. The dosage deficit crosses tissue-specific thresholds in three lineages, branching the mechanism:

   **Branch A — Parathyroid:** Reduced GATA3 **fails to fully activate the *GCM2/GCMB* promoter** → fewer/hypoplastic parathyroid progenitors → reduced PTH synthesis → hypoparathyroidism → hypocalcemia + hyperphosphatemia → tetany/seizures (*demonstrated in mouse*, [PMID: 20484821](https://pubmed.ncbi.nlm.nih.gov/20484821/); embedded in Hedgehog/Notch pouch network, [PMID: 27544844](https://pubmed.ncbi.nlm.nih.gov/27544844/)).

   **Branch B — Cochlea:** Reduced GATA3 **fails to specify the prosensory domain** → increased apoptosis in the cochlear duct, defective hair-cell maturation/innervation, spiral-ganglion neuron loss → bilateral (often progressive) sensorineural deafness (*demonstrated in mouse*, [PMID: 23666531](https://pubmed.ncbi.nlm.nih.gov/23666531/), [PMID: 31069810](https://pubmed.ncbi.nlm.nih.gov/31069810/), [PMID: 21553382](https://pubmed.ncbi.nlm.nih.gov/21553382/)).

   **Branch C — Kidney:** Reduced GATA3 **impairs metanephric/nephric development** → renal dysplasia/hypoplasia/agenesis/cysts; in a subset, glomerular injury → proteinuria → FSGS → ESRD (*human clinical + mouse*, [PMID: 27387476](https://pubmed.ncbi.nlm.nih.gov/27387476/), [PMID: 10835639](https://pubmed.ncbi.nlm.nih.gov/10835639/)).

4. Modifier pathways (**BMP upstream of GATA3; SHH/Hedgehog and Notch modulating output**) **tune** the threshold in each tissue, *inferred* to explain the wide variable expressivity and incomplete triad ([PMID: 34033651](https://pubmed.ncbi.nlm.nih.gov/34033651/), [PMID: 27544844](https://pubmed.ncbi.nlm.nih.gov/27544844/)).

```
                 GATA3 LoF (10p14)  →  ~50% protein  →  sub-threshold transcription
                          │
        ┌─────────────────┼──────────────────────────┐
        ▼                 ▼                           ▼
  PARATHYROID          COCHLEA                       KIDNEY
  GATA3→GCM2/GCMB      prosensory spec. fails        metanephric dev. impaired
  →↓PTH progenitors    →hair-cell/SGN loss           →dysplasia/hypoplasia
  →hypoPT→↓Ca/↑PO4     →sensorineural deafness        →VUR, cysts; →FSGS/ESRD
  →seizures/tetany
        ▲                 ▲                           ▲
        └── modifiers: BMP (upstream), SHH, Notch, Hedgehog tune thresholds ──┘
```

**Molecular pathways / GO & CL suggestions:** transcriptional regulation (GO:0006357), parathyroid gland development (GO:0060017), inner ear morphogenesis (GO:0042472), metanephros development (GO:0001656), pharyngeal system development. Cell types (CL): parathyroid chief cell (CL:0000446), cochlear hair cell / inner hair cell (CL:0000589 / CL:0002365), spiral ganglion neuron (CL:0000205), nephron progenitor/renal epithelial cells. Chemical entities (CHEBI): calcium ion (CHEBI:29108), phosphate, calcitriol (CHEBI:17823).

**Immune involvement:** GATA3 is also the master Th2 transcription factor; while the reviewed germline HDR literature does not establish primary immunodeficiency, rare autoimmune associations (JIA) have been reported and large 10p deletions cause thymic/T-cell defects via the DiGeorge-2 region (Findings 9, 14).

### 7. Anatomical Structures Affected

- **Organ level (primary):** parathyroid glands (UBERON:0001132), inner ear/cochlea (UBERON:0001844), kidney (UBERON:0002113). **Secondary:** brain basal ganglia (calcifications, UBERON:0002420), heart (in DiGeorge-2 contiguous deletions), thymus (DiGeorge-2), genitalia.
- **Body systems:** endocrine, auditory/nervous, urinary/renal.
- **Tissue/cell level:** parathyroid chief cells; cochlear sensory epithelium (hair cells, supporting cells) and spiral ganglion neurons; renal metanephric epithelium/glomerular podocytes (FSGS).
- **Subcellular (GO CC):** nucleus (GO:0005634) — GATA3 is a nuclear transcription factor; DNA-binding via zinc-finger domains.
- **Localization / lateralization:** deafness and (typically) renal involvement are **bilateral**, though renal anomalies can be asymmetric/unilateral (e.g., unilateral agenesis).

### 8. Temporal Development

- **Onset:** congenital to childhood; hypoparathyroidism often presents earliest (neonatal hypocalcemic seizures; mean 7.5 y), deafness may be congenital or progressive (mean 15.3 y), renal disease congenital-to-adult (mean 14.0 y) (Finding 2).
- **Onset pattern:** developmental/congenital lesion with variable clinical unveiling; hypocalcemia can present acutely (seizure/tetany).
- **Progression:** hearing loss often **progressive**; renal disease may be **stable or progressive** to ESRD; hypoparathyroidism is **chronic and lifelong**.
- **Disease course:** chronic, lifelong; no spontaneous remission. Critical intervention windows: early audiologic intervention (cochlear implantation) and vigilant calcium/renal management.

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant; many de novo cases; germline (Finding 1).
- **Penetrance:** high but incomplete and age-dependent; triad frequently incomplete (only ~40% complete in one cohort) (Findings 2, 13). **Expressivity:** highly variable, including intrafamilial (Findings 5, 14, 15).
- **Epidemiology:** rare; fewer than ~200–250 patients reported in the literature; precise prevalence/incidence not established (Orphanet lists it as rare). No robust founder effect, sex bias, or specific ethnic predilection established; cases reported worldwide.
- **Consanguinity:** not required (dominant). **Carrier frequency:** not applicable in the recessive sense; affected heterozygotes transmit with 50% risk.
- **Anticipation/mosaicism:** no repeat-expansion mechanism; anticipation not a feature. Germline mosaicism is plausible but not systematically documented.

### 10. Diagnostics

- **Laboratory:** low serum calcium, high phosphate, inappropriately low/normal intact PTH; check magnesium, 25-OH and 1,25-(OH)₂ vitamin D, urinary calcium, renal function (creatinine/eGFR), urinalysis for proteinuria.
- **Audiology:** pure-tone audiometry / ABR confirming bilateral sensorineural hearing loss; temporal-bone imaging (may mimic X-linked stapes gusher, [PMID: 29073906](https://pubmed.ncbi.nlm.nih.gov/29073906/)).
- **Imaging:** renal ultrasound (dysplasia, hypoplasia, agenesis, cysts, reflux); brain CT for basal ganglia calcification.
- **Genetic testing:** *GATA3* single-gene sequencing; NGS kidney/deafness/hypoparathyroidism panels; **CMA/aCGH, MLPA, or FISH** for whole-gene and contiguous deletions ([PMID: 42595857](https://pubmed.ncbi.nlm.nih.gov/42595857/)). Low-coverage WGS/WES can detect large 10p deletions ([PMID: 40763967](https://pubmed.ncbi.nlm.nih.gov/40763967/)).
- **Clinical criteria / differential:** diagnosis is clinical triad + molecular confirmation. **Differential diagnosis:** Alport syndrome (misdiagnosis reported, [PMID: 41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/)), DiGeorge/22q11 and 10p-DiGeorge-2 syndromes, isolated autosomal-dominant hypoparathyroidism, branchio-oto-renal syndrome, renal coloboma (PAX2) syndrome.
- **Screening:** cascade genetic testing of at-risk relatives; hearing screening; renal imaging in mutation carriers.

### 11. Outcome / Prognosis

- **Survival/mortality:** not a primary shortening of lifespan when managed; mortality risk is driven by complications of hypocalcemia (seizures, in DiGeorge-2 heart failure) and renal failure.
- **Morbidity:** deafness (developmental/communication impact), lifelong hypoparathyroidism management, and CKD/ESRD are the main disabilities. Renal progression to ESRD is the principal long-term prognostic determinant (Finding 5).
- **Recovery/complications:** hearing rehabilitated with implants; ESRD treatable by transplantation with documented long-term graft success ([PMID: 41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/)); complications of conventional calcium/vitamin-D therapy include nephrocalcinosis, stones, and brain calcification ([PMID: 28857066](https://pubmed.ncbi.nlm.nih.gov/28857066/)).
- **Prognostic factors:** genotype (whole-gene deletions/truncating variants diagnosed earlier); presence and progression of renal disease; adequacy of calcium/PTH management.

### 12. Treatment

| Domain | Intervention | NCIT (suggested) | Evidence |
|---|---|---|---|
| Hypoparathyroidism (conventional) | Oral calcium + activated vitamin D (calcitriol/alfacalcidol), target low-normal Ca | Calcium supplement; Calcitriol | [PMID: 28857066](https://pubmed.ncbi.nlm.nih.gov/28857066/), [PMID: 29633734](https://pubmed.ncbi.nlm.nih.gov/29633734/) |
| Hypoparathyroidism (replacement) | rhPTH(1-84); **palopegteriparatide** (long-acting PTH(1-34) prodrug) | Parathyroid Hormone; Teriparatide analog | [PMID: 39987371](https://pubmed.ncbi.nlm.nih.gov/39987371/), [PMID: 42166177](https://pubmed.ncbi.nlm.nih.gov/42166177/), [PMID: 42656047](https://pubmed.ncbi.nlm.nih.gov/42656047/) |
| Deafness | Hearing aids; **cochlear implantation** | Cochlear Implant | [PMID: 29073906](https://pubmed.ncbi.nlm.nih.gov/29073906/) |
| Renal (ESRD) | Dialysis; **kidney transplantation** | Kidney Transplantation | [PMID: 41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/) |

There is **no gene-, cell-, or RNA-based disease-modifying therapy**. Palopegteriparatide is notable for renal benefit: mean eGFR rose 8.9 mL/min/1.73 m² (P<0.0001) and 97% of patients became independent of conventional therapy in PaTHway; real-world data confirm reduced hypercalciuria and pill burden ([PMID: 42656047](https://pubmed.ncbi.nlm.nih.gov/42656047/)). Management targets low-normal serum calcium to protect the kidney (Finding 11). No specific pharmacogenomic guidance exists for HDR.

### 13. Prevention

- **Primary prevention:** not possible (Mendelian); genetic counseling for 50% transmission risk; prenatal/preimplantation genetic diagnosis available for known familial variants.
- **Secondary prevention:** early hearing screening and renal imaging in carriers; biochemical surveillance for hypocalcemia.
- **Tertiary prevention (Finding 14):** lifelong monitoring of parathyroid function and vesicoureteral reflux to prevent complications ([PMID: 38940299](https://pubmed.ncbi.nlm.nih.gov/38940299/)); careful calcium/vitamin-D titration to avoid nephrocalcinosis and stones; early cochlear implantation.
- **Counseling:** genetic counseling and cascade testing of relatives are central.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** mouse *Gata3* (NCBI Gene 14462; Mus musculus, NCBI:txid10090), zebrafish *gata3* (Danio rerio, NCBI:txid7955), chicken/avian *Gata3*. GATA3 is deeply evolutionarily conserved.
- **Natural disease in other species:** no spontaneous naturally occurring HDR-equivalent disorder is reported in companion animals/wildlife in the reviewed literature; the conservation of GATA3 function across vertebrates is inferred from experimental models rather than natural veterinary disease.
- **Comparative biology:** mouse (renal + neural crest defects, catecholamine-dependent lethality), zebrafish (gill bud/otolith/pronephros), and avian (pharyngeal pouch) models all reproduce facets of the human triad (Findings 4, 8, 12), demonstrating conserved mechanisms.
- **Zoonotic potential:** not applicable (non-infectious genetic disease).

### 15. Model Organisms

| Model | Type | Key phenotype | Recapitulation | PMID |
|---|---|---|---|---|
| *Gata3*−/− mouse | Knockout (mammalian) | Embryonic lethal ~E11 (noradrenaline deficiency); rescued embryos show renal hypoplasia + neural-crest defects | Partial (renal, craniofacial); lethality limits triad study | [PMID: 10835639](https://pubmed.ncbi.nlm.nih.gov/10835639/) |
| *Gata3*+/− mouse | Heterozygous | ↓PTH, ↓Ca, small parathyroids under low-Ca; progressive hearing loss | Strong (parathyroid + auditory) — models haploinsufficiency | [PMID: 20484821](https://pubmed.ncbi.nlm.nih.gov/20484821/), [PMID: 31069810](https://pubmed.ncbi.nlm.nih.gov/31069810/) |
| Conditional *Gata3* cKO mouse | Conditional | Prosensory specification failure, cochlear cell death, SGN loss | Strong (cochlear mechanism) | [PMID: 23666531](https://pubmed.ncbi.nlm.nih.gov/23666531/), [PMID: 21553382](https://pubmed.ncbi.nlm.nih.gov/21553382/) |
| Zebrafish *gata3* | Knockdown/variant | Gill bud, otolith, pronephros defects; craniofacial variability | Strong — recapitulates all three organ analogs | [PMID: 39505798](https://pubmed.ncbi.nlm.nih.gov/39505798/), [PMID: 34033651](https://pubmed.ncbi.nlm.nih.gov/34033651/) |
| Avian (chick) pouch model | In vivo developmental | Gata3/Gcm2 domain reduced by Hedgehog/Notch loss | Mechanistic (parathyroid specification network) | [PMID: 27544844](https://pubmed.ncbi.nlm.nih.gov/27544844/) |

**Limitations of models:** mouse null lethality requires pharmacologic rescue that itself alters development; heterozygous mice need dietary challenge to reveal hypoparathyroidism (incomplete penetrance of biochemical phenotype at baseline). **Resources:** MGI (mouse), ZFIN (zebrafish). Model databases: MGI, IMPC, ZFIN.

---

## Mechanistic Model / Interpretation

HDR is best understood as a **single-gene, three-organ developmental dosage disease**. GATA3 is a pleiotropic master transcription factor independently deployed in the parathyroid-fated pharyngeal endoderm, the cochlear prosensory epithelium, and the developing metanephros. A ~50% reduction in functional protein does not uniformly disable all targets; rather, each tissue has its own **dosage threshold** below which its developmental program fails. This threshold model explains the disease's defining clinical feature — **variable, often incomplete expressivity** — without invoking different mutations for different organs. The single best-characterized effector arm is the parathyroid **GATA3 → GCM2/GCMB → PTH** cascade, where GATA3 directly binds a double-GATA motif in the GCMB promoter; the cochlear arm operates through prosensory specification and hair-cell/neuron survival; the renal arm through metanephric morphogenesis with a downstream vulnerability to glomerular (FSGS) injury.

Superimposed on this core are two sources of phenotypic modulation. First, **developmental modifier pathways** — BMP acts upstream of GATA3, while SHH/Hedgehog and Notch tune its output — set tissue-specific thresholds and, when perturbed, shift the phenotype; this provides a molecular rationale for variable expressivity even among relatives sharing an identical variant. Second, **deletion size** matters: point mutations and small deletions produce "pure" HDR, whereas large 10p terminal deletions co-delete the DiGeorge-2 (DGCR2) region, adding cardiac (ASD), thymic/immune, and neurodevelopmental features. The germline HDR context is mechanistically distinct from the somatic GATA3 mutations that drive breast/urothelial cancers, and there is no evidence of elevated cancer risk in HDR.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [10935639](https://pubmed.ncbi.nlm.nih.gov/10935639/) | Established *GATA3* haploinsufficiency as cause; critical 200-kb 10p14 region | Human genetics |
| [32442337](https://pubmed.ncbi.nlm.nih.gov/32442337/) | 124-family mutation spectrum + penetrance | Human review |
| [15705923](https://pubmed.ncbi.nlm.nih.gov/15705923/), [19723756](https://pubmed.ncbi.nlm.nih.gov/19723756/) | ZnF1/ZnF2 functional roles; missense LoF mechanism | In vitro |
| [10835639](https://pubmed.ncbi.nlm.nih.gov/10835639/) | Gata3-null mouse renal/neural-crest defects | Mouse |
| [27387476](https://pubmed.ncbi.nlm.nih.gov/27387476/) | Dysplastic renal spectrum, FSGS/ESRD | Human clinical |
| [23666531](https://pubmed.ncbi.nlm.nih.gov/23666531/), [31069810](https://pubmed.ncbi.nlm.nih.gov/31069810/), [21553382](https://pubmed.ncbi.nlm.nih.gov/21553382/) | Cochlear mechanism of deafness | Mouse |
| [20484821](https://pubmed.ncbi.nlm.nih.gov/20484821/) | GATA3→GCMB→PTH cascade | Mouse + in vitro |
| [27544844](https://pubmed.ncbi.nlm.nih.gov/27544844/) | Hedgehog/Notch network in pouch | Avian |
| [22407589](https://pubmed.ncbi.nlm.nih.gov/22407589/), [18795911](https://pubmed.ncbi.nlm.nih.gov/18795911/), [15253763](https://pubmed.ncbi.nlm.nih.gov/15253763/) | DiGeorge-2 contiguous-gene distinction | Human genetics |
| [40378057](https://pubmed.ncbi.nlm.nih.gov/40378057/) | Somatic GATA3 in cancer (distinct from HDR) | Human oncology |
| [28857066](https://pubmed.ncbi.nlm.nih.gov/28857066/), [39987371](https://pubmed.ncbi.nlm.nih.gov/39987371/), [42166177](https://pubmed.ncbi.nlm.nih.gov/42166177/), [42656047](https://pubmed.ncbi.nlm.nih.gov/42656047/) | Treatment: conventional + PTH replacement | Clinical trials/reviews |
| [39505798](https://pubmed.ncbi.nlm.nih.gov/39505798/), [34033651](https://pubmed.ncbi.nlm.nih.gov/34033651/) | Zebrafish model; BMP/SHH modifiers | Zebrafish |
| [42595857](https://pubmed.ncbi.nlm.nih.gov/42595857/), [38940299](https://pubmed.ncbi.nlm.nih.gov/38940299/), [41064049](https://pubmed.ncbi.nlm.nih.gov/41064049/) | Diagnosis, extended phenotype, surveillance, transplant | Human clinical |

---

## Limitations and Knowledge Gaps

- **Rarity limits epidemiology:** precise prevalence, incidence, sex ratio, and geographic/ethnic distribution are not firmly established (<~250 reported patients); no large registry or EHR-scale dataset exists.
- **Genotype–phenotype correlation is imperfect:** apart from a trend for earlier diagnosis with truncating/whole-gene-deletion variants, the molecular basis of which organs are affected in a given patient remains unpredictable; modifier evidence (BMP/SHH/Notch) is mostly from non-human models.
- **Renal progression predictors unknown:** why only a subset progress to FSGS/ESRD is unclear; no validated prognostic biomarkers.
- **QoL data absent:** no disease-specific quality-of-life instruments have been applied to HDR.
- **Human mechanistic data are indirect:** the parathyroid and cochlear cascades are demonstrated largely in mice/zebrafish; direct human tissue confirmation is limited.
- **No natural veterinary disease** characterized, and no disease-modifying therapy exists.

## Proposed Follow-up Experiments / Actions

1. **Build an international HDR registry** to define prevalence, penetrance, natural history, and renal-progression rates with longitudinal biomarker data.
2. **Genotype–phenotype and modifier study:** correlate variant class/position (ZnF1 vs ZnF2, deletion size) with organ involvement and severity; genotype BMP/SHH/NOTCH pathway variants as candidate human modifiers.
3. **Renal prognostic biomarkers:** prospectively track proteinuria, eGFR, and podocyte injury markers to identify predictors of FSGS/ESRD; evaluate whether early PTH-replacement (palopegteriparatide) preserves renal function in HDR specifically.
4. **iPSC/organoid models:** derive patient iPSC-based kidney and inner-ear organoids to test tissue-specific dosage thresholds and screen threshold-raising interventions.
5. **Functional triage pipeline:** standardize zebrafish (gill bud/otolith/pronephros) + in-vitro DNA-binding/FOG-interaction assays for rapid VUS reclassification.
6. **Clinical guideline development:** codify surveillance (parathyroid function, VUR, hearing, renal imaging) and calcium-target management to minimize nephrocalcinosis and support early cochlear implantation.

---

*Report compiled from 15 confirmed findings and 58 reviewed papers. Evidence types span human clinical genetics, mouse/zebrafish/avian model organisms, and in-vitro functional assays. HDR syndrome (MONDO:0007797; OMIM #146255) is caused by GATA3 haploinsufficiency at 10p14.*


## Artifacts

- [OpenScientist final report](Hypoparathyroidism_Deafness_Renal_Disease_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypoparathyroidism_Deafness_Renal_Disease_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007797` (4 mentions) - the report calls it "if available"; MONDO calls it **hypoparathyroidism-deafness-renal disease syndrome**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0002199` (1 mention) - the report calls it "Symptom"; HP calls it **Hypocalcemic seizures**
- `HP:0002905` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperphosphatemia**
- `HP:0000076` (1 mention) - the report calls it "Clinical sign"; HP calls it **Vesicoureteral reflux**
- `HP:0002135` (1 mention) - the report calls it "Imaging"; HP calls it **Basal ganglia calcification**
- `HP:0000811` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal external genitalia morphology**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 28 |
| On topic | 19 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28857066` *(abstract only)*: "*does not fully replace the functions of PTH and can lead to … nephrocalcinosis, kidney stones and brain calcifications*"
  - closest text in source: "Conventional treatment includes activated vitamin D and/or calcium supplements, but this treatment does not fully replace the functions of PTH and can lead to short-term problems (such as hypocalcaemia, hypercalcaemia and increased urinary calcium excretion) and long-term complications (which include nephrocalcinosis, kidney stones and brain calcifications)"
- `PMID:39987371` *(abstract only)*: "*approved … as the first true replacement therapy for hypoPT management*"
  - closest text in source: "Recently, the Food & Drug Administration and the European Medicines Agency approved palopegteriparatide as the first true replacement therapy for hypoPT management"
- `PMID:39505798` *(abstract only)*: "*deleterious impact … on the gill buds, otoliths, and pronephros*"
  - closest text in source: "In vivo studies using a zebrafish animal model revealed the deleterious impact of the variant on the gill buds, otoliths, and pronephros"
- `PMID:42595857`: "*targeted next-generation sequencing-based kidney disease panels … and copy number variations were assessed using array comparative genomic hybridization*"
  - closest text in source: "Targeted next-generation sequencing-based kidney disease panels were used, and copy number variations were assessed using array comparative genomic hybridization"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:15253763` (1 mention) - Interstitial deletion of 10p and atrial septal defect in DiGeorge 2 syndrome.
  - shared terms: deletion, patient

Weighed against this report's own most characteristic terms: `gata3`, `renal`, `hdr`, `hypoparathyroidism`, `deafness`, `hearing`, `disease`, `parathyroid`, `loss`, `cochlear`, `pth`, `deletion`, `phenotype`, `model`, `triad`, `patient`, `esrd`, `variant`, `development`, `function`.
