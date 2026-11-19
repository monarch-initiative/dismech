---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T17:55:10.670888'
end_time: '2026-10-30T18:27:14.567968'
duration_seconds: 1923.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Encephalopathy Due To Hydroxykynureninuria
  mondo_id: MONDO:0009372
  category: Mendelian
  causal_genes: KYNU
  omim_id: OMIM:236800
  synonyms: Xanthurenic aciduria; kynureninase deficiency
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Encephalopathy_Due_To_Hydroxykynureninuria-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Encephalopathy_Due_To_Hydroxykynureninuria-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Encephalopathy Due To Hydroxykynureninuria
- **MONDO ID:** MONDO:0009372 (if available)
- **Causal gene(s):** KYNU
- **OMIM:** OMIM:236800
- **Synonyms:** Xanthurenic aciduria; kynureninase deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Encephalopathy Due To Hydroxykynureninuria** covering all of the
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

# Encephalopathy Due To Hydroxykynureninuria (KYNU Deficiency): Comprehensive Disease Report

**Disease:** Encephalopathy Due To Hydroxykynureninuria
**MONDO ID:** MONDO:0009372 · **OMIM:** 236800
**Causal gene:** **KYNU** (kynureninase; HGNC:6469; NCBI Gene 8942; UniProt Q16719; chromosome 2q22.2)
**Synonyms:** Xanthurenic aciduria; hydroxykynureninuria; kynureninase deficiency

---

## Summary

The disease catalogued under MONDO:0009372 / OMIM 236800 ("encephalopathy due to hydroxykynureninuria," also called **xanthurenic aciduria** or **hydroxykynureninuria**) is an **autosomal-recessive inborn error of tryptophan metabolism caused by biallelic loss-of-function variants in the gene KYNU**, which encodes the pyridoxal-5′-phosphate (PLP)-dependent enzyme **kynureninase**. Kynureninase catalyzes the hydrolytic cleavage of 3-hydroxy-L-kynurenine to 3-hydroxyanthranilic acid (and, with lower efficiency, of L-kynurenine to anthranilic acid) within the **kynurenine pathway**, the de novo route from tryptophan to nicotinamide adenine dinucleotide (NAD⁺). When kynureninase activity is lost, upstream metabolites accumulate and are excreted massively in urine — xanthurenic acid, 3-hydroxykynurenine, and kynurenine — producing the characteristic biochemical signature, while flux to NAD⁺ is reduced.

Over nearly six decades the understanding of this entity has transformed. The condition was first described in the 1960s as a benign-appearing biochemical trait ("hydroxykynureninuria"), and the first molecular confirmation came in 2007, when a Somali boy and his brother with massive xanthurenic aciduria were found to be homozygous for a KYNU missense variant. The pivotal conceptual shift came in 2017, when biallelic loss-of-function KYNU variants (alongside variants in HAAO) were shown to cause **Congenital NAD Deficiency Disorder (CNDD)** — a syndrome of vertebral, cardiac, renal and limb (VCRL) malformations historically overlapping with VACTERL association and Catel-Manzke syndrome. The unifying mechanism is **NAD⁺ deficiency during embryogenesis**, and crucially, malformations are **preventable by niacin (vitamin B3) supplementation** in animal models.

The disease is therefore best understood as a **gene × environment disorder with extreme variable expressivity**: identical biallelic KYNU genotypes can produce anything from an asymptomatic urinary metabolite trait to multisystem congenital malformations with developmental delay and premature death, depending substantially on maternal dietary NAD-precursor (tryptophan/niacin) status during pregnancy. This has profound and hopeful clinical implications — it is one of a small number of structural birth-defect syndromes that may be **preventable through maternal vitamin supplementation**.

---

## Key Findings

### Finding 1 — KYNU (kynureninase) deficiency causes xanthurenic aciduria / hydroxykynureninuria through a block in the tryptophan→NAD kynurenine pathway

The core molecular lesion of this disease is loss of kynureninase activity, which interrupts the kynurenine pathway and causes upstream metabolites to accumulate. The first molecular proof came from *Xanthurenic aciduria due to a mutation in KYNU encoding kynureninase* ([PMID: 17334708](https://pubmed.ncbi.nlm.nih.gov/17334708/)), which reported that **"Massive urinary excretion of xanthurenic acid, 3-hydroxykynurenine and kynurenine, known as xanthurenic aciduria or hydroxykynureninuria, in a young Somali boy suggested kynureninase deficiency."** The index patient was homozygous for KYNU c.593A>G (p.T198A), and an affected younger brother carried the same genotype — establishing the gene–biochemistry link and the recessive inheritance.

This biochemical block was independently confirmed in *Biallelic variants in KYNU cause a multisystemic syndrome with hand hyperphalangism* ([PMID: 31923704](https://pubmed.ncbi.nlm.nih.gov/31923704/)), in which **"Plasma and urine metabolomic analysis of two patients indicated a block along the tryptophan catabolic pathway and urine organic acid analysis showed excretion of xanthurenic acid."** The reported KYNU variants in that cohort included a large deletion of exons 1–8 combined with p.R428W, as well as p.R330Q and p.W109S — a mix of null and missense alleles.

Mechanistically, when kynureninase cannot cleave 3-hydroxykynurenine, 3-hydroxykynurenine accumulates and is diverted by transamination (via kynurenine aminotransferases) into **xanthurenic acid**, the hallmark urinary metabolite; kynurenine itself also accumulates and spills into urine. The accumulated/diverted metabolites define the diagnostic urine profile (CHEBI: xanthurenic acid CHEBI:10072; 3-hydroxy-L-kynurenine CHEBI:1547; L-kynurenine CHEBI:16946).

### Finding 2 — Biallelic KYNU loss-of-function causes Congenital NAD Deficiency Disorder (CNDD/VCRL), rescuable by niacin in animal models

The landmark reconceptualization of this disease came from *NAD Deficiency, Congenital Malformations, and Niacin Supplementation* ([PMID: 28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/), *New England Journal of Medicine*, Shi et al. 2017). In patients with combinations of cardiac, vertebral and renal defects, **"Variants were identified in two genes that encode enzymes of the kynurenine pathway, 3-hydroxyanthranilic acid 3,4-dioxygenase (HAAO) and kynureninase (KYNU)."** The specific KYNU alleles reported included p.V57Efs*21 and compound heterozygous p.Y156*/p.F349Kfs*4 — all loss-of-function. Mutant enzymes had greatly reduced in vitro activity, and patients had reduced circulating NAD.

The paper established the downstream mechanism explicitly: **"Nicotinamide adenine dinucleotide (NAD) is synthesized de novo from tryptophan through the kynurenine pathway. The patients had reduced levels of circulating NAD."** Critically, *Kynu*-null and *Haao*-null mouse embryos recapitulated the same constellation of malformations, which arose from gestational NAD deficiency — and **niacin supplementation during gestation prevented the malformations**. This simultaneously demonstrated causation (NAD deficiency is the proximate teratogenic driver) and identified a preventive intervention.

This finding redefined the disease: the "encephalopathy/hydroxykynureninuria" trait and the severe multisystem malformation syndrome are two ends of one NAD-deficiency spectrum arising from the same enzymatic block.

### Finding 3 — CNDD is a gene × environment disorder with highly variable expressivity; prevention/treatment requires NAD-precursor (B3 vitamer) supplementation, with amidated precursors preferred for distal blocks

The gene × environment nature of this disorder — and the nuances of supplementation — are best demonstrated by work on the related pathway gene NADSYN1, which sits downstream and shares the CNDD phenotype. *A metabolic signature for NADSYN1-dependent congenital NAD deficiency disorder* ([PMID: 38357931](https://pubmed.ncbi.nlm.nih.gov/38357931/), Szot et al. 2024) identified 13 further individuals with biallelic variants whose **"phenotypes ranging from multiple severe malformations to the complete absence of malformation"** — documenting the extraordinary variable expressivity that characterizes CNDD, even within families.

The same study established a therapeutically crucial principle about *which* B3 vitamer works, depending on where the pathway block lies: **"While for Nadsyn1+/- mothers, any B3 vitamer was suitable to raise NAD, preventing embryo loss and malformation, Nadsyn1-/- mothers required supplementation with amidated NAD precursors (nicotinamide or nicotinamide mononucleotide) bypassing their metabolic block."** By analogy, because KYNU acts upstream in the de novo (tryptophan) arm, an amidated precursor that enters via the salvage/Preiss-Handler route (nicotinamide, nicotinamide mononucleotide, nicotinamide riboside) bypasses the KYNU block and should be preferred over tryptophan or precursors requiring de novo synthesis.

Human evidence that supplementation raises the NAD pool comes from an adult NADSYN1-CNDD patient ([PMID: 36649848](https://pubmed.ncbi.nlm.nih.gov/36649848/)) whose NAD pool rose approximately 25% after nicotinamide supplementation. The explicit framing of CNDD as a "gene × environment disorder caused by disruptions of the kynurenine pathway" appears in the 2026 review ([PMID: 42798303](https://pubmed.ncbi.nlm.nih.gov/42798303/)).

### Finding 4 — Kynureninase is a PLP-dependent fold-type I enzyme that strongly prefers 3-hydroxy-L-kynurenine over L-kynurenine

Understanding the enzyme's biochemistry explains the metabolite profile and informs therapeutic engineering. Human kynureninase (HsKYNase) is a **pyridoxal-5′-phosphate (PLP)-dependent** hydrolase of the aminotransferase (fold-type I) family. Protein-engineering studies note that the wild-type **"human enzyme (HsKYNase) has very low activity for kynurenine and shows no therapeutic effect"** ([PMID: 36465553](https://pubmed.ncbi.nlm.nih.gov/36465553/)) — i.e., the physiological human enzyme preferentially cleaves **3-hydroxy-L-kynurenine** (to 3-hydroxyanthranilic acid + L-alanine) rather than L-kynurenine. This substrate preference explains why 3-hydroxykynurenine and its transamination product xanthurenic acid dominate the urinary signature in KYNU deficiency.

Catalysis depends on an intact PLP-binding pocket, and studies of engineered variants show that **"the amino acid substitutions in BF-HsKYNase allosterically affect the flexibility of the pyridoxal-5′-phosphate (PLP) binding pocket"** ([PMID: 35658075](https://pubmed.ncbi.nlm.nih.gov/35658075/)), modulating the rate-limiting chemical step. This has two implications for the disease: (1) missense variants that perturb PLP binding or active-site geometry are plausibly pathogenic through catalytic loss of function; and (2) the enzyme's PLP dependence connects the pathway to vitamin B6 status (pyridoxine), historically relevant to xanthurenic acid excretion (xanthurenic aciduria is also a classic marker of B6 deficiency).

### Finding 5 — KYNU deficiency presents on a spectrum from asymptomatic xanthurenic aciduria to VCRL malformations with hand hyperphalangism, mimicking VACTERL / Catel-Manzke syndrome

The clinical phenotype is remarkably broad. At the mild end, *Xanthurenic aciduria due to a mutation in KYNU* ([PMID: 17334708](https://pubmed.ncbi.nlm.nih.gov/17334708/)) described two brothers with the full biochemical phenotype who had **"neither... symptoms of niacin deficiency"** — essentially an asymptomatic metabolic trait. At the severe end, *Biallelic variants in KYNU cause a multisystemic syndrome with hand hyperphalangism* ([PMID: 31923704](https://pubmed.ncbi.nlm.nih.gov/31923704/)) described **"three patients with hand hyperphalangism, heart defect, short stature, and mild to severe developmental delay, all of whom were initially given a clinical diagnosis of Catel-Manzke syndrome."** Notably, a multi-exon KYNU deletion (exons 1–8) was detectable only with copy-number variant analysis — a diagnostic lesson.

The overlap with recognized malformation associations is substantial. *Further description of two patients with biallelic variants in NADSYN1* ([PMID: 35491967](https://pubmed.ncbi.nlm.nih.gov/35491967/), Kortbawi et al. 2022) notes that NAD-deficiency disorders **"overlap with the anomalies present in vertebral, anal, cardiac, tracheoesophageal, radial and renal, and limb anomalies (VATER/VACTERL) association and often result in premature death; children who survive typically have developmental delays or intellectual disability."** Thus KYNU deficiency can masquerade as VACTERL association or Catel-Manzke syndrome, and should be considered in those differential diagnoses — especially because, unlike most causes of those phenotypes, it is biochemically detectable and potentially preventable.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in KYNU** (nonsense, frameshift, large deletion, or damaging missense affecting the PLP pocket) **lead to** absent or severely reduced kynureninase enzyme activity.
2. Loss of kynureninase activity **results in** a block in the de novo kynurenine pathway at the hydrolysis of 3-hydroxy-L-kynurenine → 3-hydroxyanthranilic acid (the physiologically preferred reaction of the human enzyme).
3. The block **causes** accumulation of upstream metabolites — 3-hydroxykynurenine and kynurenine — which **branch** into two consequences:
   - **Branch A (biochemical/diagnostic):** accumulated 3-hydroxykynurenine is transaminated to **xanthurenic acid**, and kynurenine/3-hydroxykynurenine spill into urine → **xanthurenic aciduria / hydroxykynureninuria** (the measurable trait).
   - **Branch B (pathogenic):** reduced downstream flux **leads to** decreased de novo synthesis of **NAD⁺**.
4. During embryogenesis, if maternal dietary NAD precursors (tryptophan, niacin/nicotinamide) are insufficient to compensate, the NAD⁺ shortfall **results in** a critical deficiency of NAD⁺ in the developing embryo (inferred to impair NAD⁺-dependent processes — energy metabolism, PARP/sirtuin signaling, redox balance — during organogenesis; the precise molecular targets in human embryos remain inferred rather than fully demonstrated).
5. Embryonic NAD⁺ deficiency during organogenesis **causes** congenital malformations — **vertebral, cardiac, renal and limb (VCRL)** defects, hand hyperphalangism, and in severe cases miscarriage/premature death — i.e., **Congenital NAD Deficiency Disorder (CNDD)**.
6. Postnatally, persistent NAD-pathway dysfunction and/or the malformations themselves **contribute to** developmental delay and intellectual disability in survivors.

**Gene × environment modifier (acts on steps 3B–5):** Maternal NAD-precursor status is the dominant environmental modifier. Abundant maternal niacin/tryptophan **can prevent** the NAD⁺ shortfall and therefore the malformations, even with the same biallelic genotype — explaining the spectrum from asymptomatic xanthurenic aciduria to severe multisystem malformation.

### Schematic

```
 Tryptophan
    │  (TDO/IDO, KMO, ...)
    ▼
 L-Kynurenine ──► 3-Hydroxy-L-kynurenine
                         │
            KYNU (kynureninase, PLP-dependent)  ✖ BLOCKED
                         │
         ┌───────────────┴───────────────────────┐
         ▼ (physiological)                        ▼ (diverted, accumulating)
 3-Hydroxyanthranilic acid              3-OH-kynurenine, kynurenine
         │                                        │ transamination
         ▼ (HAAO → ... → NADSYN1)                 ▼
       NAD⁺  ◄─ reduced flux             XANTHURENIC ACID  → URINE
         │                               (xanthurenic aciduria /
         │                                hydroxykynureninuria)
         ▼  (if maternal niacin/Trp insufficient)
  EMBRYONIC NAD⁺ DEFICIENCY
         │
         ▼
  VCRL malformations, hand hyperphalangism, developmental delay
  (Congenital NAD Deficiency Disorder; VACTERL/Catel-Manzke mimic)

  RESCUE: maternal amidated B3 vitamer (nicotinamide / NMN / NR)
          bypasses the upstream KYNU block → restores NAD⁺ → prevents malformation
```

### Upstream vs downstream

- **Upstream (initiating):** KYNU genotype → loss of kynureninase catalysis → metabolite block.
- **Midstream (dual output):** metabolite accumulation (→ diagnostic xanthurenic aciduria) AND reduced NAD⁺ synthesis.
- **Downstream (clinical):** embryonic NAD⁺ deficiency → malformations; postnatal developmental delay.
- **Dominant modifier:** maternal/dietary NAD-precursor availability determines whether the downstream clinical branch is expressed.

### Ontology suggestions

- **Gene/protein:** KYNU (HGNC:6469); GO biological process: *NAD biosynthetic process* (GO:0009435), *tryptophan catabolic process to kynurenine* (GO:0019441), *quinolinate biosynthetic process* (GO:0019805); GO molecular function: *kynureninase activity* (GO:0030429), *pyridoxal phosphate binding* (GO:0030170); GO cellular component: *cytosol* (GO:0005829).
- **Phenotypes (HPO):** Vertebral segmentation defect (HP:0003422), Abnormal heart morphology / congenital heart defect (HP:0001627), Renal hypoplasia/agenesis (HP:0008678), Short stature (HP:0004322), Global developmental delay (HP:0001263), Intellectual disability (HP:0001249), Hyperphalangy (HP:0009811), Aminoaciduria (HP:0003355) as nearest general term for the urinary metabolite abnormality.
- **Anatomy (UBERON):** vertebral column (UBERON:0001130), heart (UBERON:0000948), kidney (UBERON:0002113), limb (UBERON:0002101), brain (UBERON:0000955).
- **Chemical (CHEBI):** xanthurenic acid (CHEBI:10072), 3-hydroxy-L-kynurenine (CHEBI:1547), L-kynurenine (CHEBI:16946), NAD⁺ (CHEBI:15846), nicotinamide (CHEBI:17154), niacin/nicotinic acid (CHEBI:15940), pyridoxal 5′-phosphate (CHEBI:18405).
- **Treatment (NCIT):** Nicotinamide (NCIT:C577), Niacin/Nicotinic Acid (NCIT:C545), Dietary supplement / Nutritional support.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|------|-----------------|---------------|----------|
| [17334708](https://pubmed.ncbi.nlm.nih.gov/17334708/) | Xanthurenic aciduria due to a mutation in KYNU | Human clinical/genetic | First molecular proof: KYNU mutation → xanthurenic aciduria; asymptomatic trait end of spectrum (F1, F5) |
| [28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/) | NAD Deficiency, Congenital Malformations, Niacin Supplementation (NEJM) | Human + mouse | KYNU/HAAO LoF → reduced NAD → VCRL malformations; niacin prevents in mice (F2) |
| [31923704](https://pubmed.ncbi.nlm.nih.gov/31923704/) | Biallelic KYNU variants cause multisystemic syndrome with hand hyperphalangism | Human clinical/genetic/metabolomic | Confirms tryptophan-pathway block; Catel-Manzke mimic; CNV detection (F1, F5) |
| [38357931](https://pubmed.ncbi.nlm.nih.gov/38357931/) | Metabolic signature for NADSYN1-dependent CNDD | Human + mouse | Variable expressivity; amidated precursors required for distal block (F3) |
| [36649848](https://pubmed.ncbi.nlm.nih.gov/36649848/) | Adult NADSYN1-associated CNDD, NAD analysis | Human clinical | Nicotinamide supplementation raised NAD pool ~25% (F3) |
| [42798303](https://pubmed.ncbi.nlm.nih.gov/42798303/) | Biallelic variants … CNDD (2026 review) | Review | CNDD framed as gene × environment disorder of kynurenine pathway (F3) |
| [36465553](https://pubmed.ncbi.nlm.nih.gov/36465553/) | Switching the rate-limiting step of an immunotherapeutic enzyme | In vitro / protein engineering | Human KYNase prefers 3-OH-kynurenine; low activity for kynurenine (F4) |
| [35658075](https://pubmed.ncbi.nlm.nih.gov/35658075/) | Leveraging intrinsic flexibility to engineer enzyme activity | In vitro / structural | KYNU is PLP-dependent; PLP-pocket flexibility controls catalysis (F4) |
| [35491967](https://pubmed.ncbi.nlm.nih.gov/35491967/) | Two patients with biallelic NADSYN1 variants | Human clinical | VACTERL overlap; premature death; developmental delay in survivors (F5) |
| [35484986](https://pubmed.ncbi.nlm.nih.gov/35484986/) | NAD⁺ deficiency in human malformations and miscarriage: pleiotropy model | Review/hypothesis | Broad CNDD pleiotropy framework (context) |
| [39829932](https://pubmed.ncbi.nlm.nih.gov/39829932/) | Zebrafish model of NAD deficiency disorder | Model organism | Additional non-mammalian CNDD model (context) |
| [37300479](https://pubmed.ncbi.nlm.nih.gov/37300479/) | NAD Deficiency and Mammalian Development | Review | Developmental role of NAD (context) |

**Historical/primary descriptions (pre-molecular era):** *Hydroxykynureninuria* ([PMID: 6015911](https://pubmed.ncbi.nlm.nih.gov/6015911/)); *Hydroxykynureninuria: abnormal tryptophan metabolism probably due to kynureninase deficiency* ([PMID: 14169454](https://pubmed.ncbi.nlm.nih.gov/14169454/)); *Familial hydroxykynureninuria* ([PMID: 649181](https://pubmed.ncbi.nlm.nih.gov/649181/)); *Hydroxykynureninuria, a case report* ([PMID: 7152601](https://pubmed.ncbi.nlm.nih.gov/7152601/)). These 1960s–1980s reports established the biochemical phenotype and inferred kynureninase deficiency decades before KYNU was sequenced.

---

## Section-by-Section Compilation

### 1. Disease Information
Encephalopathy due to hydroxykynureninuria (xanthurenic aciduria; kynureninase deficiency) is a rare autosomal-recessive inborn error of tryptophan catabolism. **Identifiers:** MONDO:0009372; OMIM 236800; gene KYNU (HGNC:6469); Orphanet lists it within kynurenine-pathway/CNDD disorders; ICD-10 maps best to E70.8 (other disorders of aromatic amino-acid metabolism). The modern literature increasingly subsumes it under **Congenital NAD Deficiency Disorder (CNDD)**. Information is derived from a combination of **aggregated disease-level resources** (OMIM, Orphanet) and **individual patient reports/case series** (the KYNU and NADSYN1/HAAO cohorts). The name "encephalopathy" is partly historical; the predominant modern phenotype is congenital malformation ± neurodevelopmental delay rather than a classic progressive encephalopathy.

### 2. Etiology
**Causal factor:** biallelic (homozygous or compound heterozygous) loss-of-function variants in **KYNU**. **Genetic risk factors:** the only established determinant is biallelic pathogenic KYNU genotype; **consanguinity** increases risk (several reported families are consanguineous; e.g., the homozygous Somali brothers). **Environmental risk / protective factors:** maternal dietary **NAD-precursor (tryptophan, niacin/nicotinamide) deficiency** during pregnancy is the major environmental factor that converts a biochemical trait into congenital malformations; conversely, **adequate maternal niacin is protective** (demonstrated in mouse models). **Gene–environment interaction** is the defining feature: genotype sets susceptibility, maternal NAD-precursor status determines expression.

### 3. Phenotypes
- **Laboratory abnormalities (obligate):** xanthurenic aciduria, elevated urinary 3-hydroxykynurenine and kynurenine, reduced circulating NAD (nearest HPO: Aminoaciduria HP:0003355).
- **Structural (variable):** vertebral segmentation defects (HP:0003422), congenital heart defects (HP:0001627), renal hypoplasia/agenesis (HP:0008678), limb/hand anomalies including hyperphalangy (HP:0009811), short stature (HP:0004322).
- **Neurodevelopmental:** global developmental delay (HP:0001263), intellectual disability (HP:0001249) in survivors of the severe form.
- **Onset:** congenital/prenatal for malformations; the biochemical trait is present from birth. **Severity:** highly variable (asymptomatic → severe/lethal). **Frequency among affected:** metabolite abnormalities ~obligate; malformations present in the severe CNDD subset. **QoL:** severe end entails major disability and premature death; mild end may be clinically silent.

### 4. Genetic / Molecular Information
**Causal gene:** KYNU (OMIM *605197; HGNC:6469; chr 2q22.2). **Reported pathogenic variants** include missense (p.T198A, p.R428W, p.R330Q, p.W109S), nonsense (p.Y156*), frameshift (p.V57Efs*21, p.F349Kfs*4), and a **large multi-exon deletion (exons 1–8)** detectable only by CNV analysis. **Variant classification:** pathogenic/likely pathogenic per ACMG; most are loss-of-function. **Allele frequency:** individually very rare in gnomAD (consistent with a rare recessive disorder). **Origin:** germline. **Functional consequence:** loss of function (reduced/absent kynureninase catalytic activity). **Modifier genes:** other kynurenine-pathway genes (HAAO, NADSYN1) cause the same CNDD phenotype and may act as pathway-level modifiers; no specific intragenic modifier established. **Epigenetic/chromosomal abnormalities:** none specifically implicated beyond the structural KYNU deletion.

### 5. Environmental Information
The key environmental factor is **maternal dietary NAD-precursor status** (tryptophan and niacin/vitamin B3). Low dietary niacin unmasks malformations; sufficient intake is protective. Vitamin **B6 (pyridoxine)** status is mechanistically relevant because kynureninase is PLP-dependent, and xanthurenic aciduria is also a classic marker of B6 deficiency. No infectious agents are involved.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full numbered causal chain. In brief: KYNU LoF → kynureninase block → (a) accumulation/diversion of 3-hydroxykynurenine to xanthurenic acid (diagnostic) and (b) reduced de novo NAD⁺ synthesis → embryonic NAD⁺ deficiency (gated by maternal precursor supply) → VCRL malformations and developmental delay. **Pathways:** kynurenine/NAD de novo pathway (KEGG hsa00380 tryptophan metabolism; Reactome NAD biosynthesis). **Biochemical defect:** PLP-dependent kynureninase deficiency. **Metabolic change:** impaired amino-acid (tryptophan) catabolism and NAD⁺ cofactor depletion.

### 7. Anatomical Structures Affected
**Primary organs/systems:** axial skeleton/vertebral column (UBERON:0001130), heart (UBERON:0000948), kidneys/renal system (UBERON:0002113), limbs (UBERON:0002101); nervous system (UBERON:0000955) for neurodevelopmental involvement. **Lateralization:** malformations are typically bilateral/midline (vertebral, cardiac, renal). **Subcellular:** cytosolic enzyme (kynureninase, GO:0005829); NAD⁺ depletion affects mitochondrial and nuclear NAD-dependent processes. **Cell/tissue level:** broadly affects dividing embryonic progenitor populations during organogenesis (no single CL cell type is specifically targeted; the effect is a systemic cofactor deficiency).

### 8. Temporal Development
**Onset:** congenital (malformations arise during embryonic organogenesis; biochemical trait present from birth). **Pattern:** the malformation damage is fixed at birth (non-progressive structurally), but neurodevelopmental sequelae and growth deficits manifest over childhood. **Critical period:** the therapeutic window is **periconceptional/gestational** — maternal supplementation must occur during pregnancy to prevent malformations; postnatal supplementation cannot reverse structural defects. **Course:** severe cases may be lethal prenatally/neonatally; mild cases are lifelong but asymptomatic.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance/expressivity:** highly variable expressivity (asymptomatic trait → severe malformation/miscarriage), modified by maternal environment; biochemical penetrance is high. **Consanguinity:** contributory (reported consanguineous and founder-type families). **Epidemiology:** ultra-rare; precise prevalence/incidence not established (only a few dozen molecularly confirmed CNDD cases across KYNU/HAAO/NADSYN1). **Sex ratio:** no established predilection. **Carrier frequency:** not precisely defined; individual alleles are rare in gnomAD.

### 10. Diagnostics
**Biochemical:** urine organic acid / metabolomic analysis showing xanthurenic acid, 3-hydroxykynurenine and kynurenine excretion; plasma/urine metabolomics showing a tryptophan-pathway block; reduced circulating NAD. **Genetic testing:** single-gene KYNU testing, gene panels covering kynurenine/NAD-pathway genes (KYNU, HAAO, NADSYN1), or WES/WGS — with the important caveat that **CNV/deletion analysis is required** because large KYNU deletions (exons 1–8) are missed by SNV-only sequencing. **Imaging:** skeletal survey (vertebral segmentation), echocardiography (cardiac defects), renal ultrasound. **Differential diagnosis:** VACTERL/VATER association, Catel-Manzke syndrome, and other causes of vertebral/cardiac/renal/limb malformations — distinguished by the characteristic urinary metabolite signature and KYNU genotype.

### 11. Outcome / Prognosis
Prognosis spans the full range: asymptomatic biochemical trait with normal life expectancy at the mild end; at the severe end, CNDD "often results in premature death," and survivors typically have developmental delay/intellectual disability ([PMID: 35491967](https://pubmed.ncbi.nlm.nih.gov/35491967/)). Prognosis is largely determined prenatally; the prognostic modifier is the severity/number of organ malformations. No formal survival statistics exist given rarity.

### 12. Treatment
**Primary/preventive:** maternal **NAD-precursor (vitamin B3) supplementation** during pregnancy to prevent malformations — the central therapeutic insight. Because KYNU acts upstream, **amidated precursors (nicotinamide, nicotinamide mononucleotide, nicotinamide riboside)** that bypass the de novo block are preferred over tryptophan (by analogy to the NADSYN1 data, [PMID: 38357931](https://pubmed.ncbi.nlm.nih.gov/38357931/)). Human data show nicotinamide raises the NAD pool (~25%, [PMID: 36649848](https://pubmed.ncbi.nlm.nih.gov/36649848/)). **Postnatal:** supportive and surgical management of malformations (cardiac surgery, orthopedic/vertebral and renal management), developmental/rehabilitative support. No approved gene therapy or targeted drug. **NCIT terms:** Nicotinamide (NCIT:C577), Niacin (NCIT:C545). **PLP/vitamin B6** repletion is a reasonable adjunct given the PLP dependence of the enzyme, though it cannot restore a null enzyme.

### 13. Prevention
**Primary prevention:** periconceptional/gestational maternal niacin/nicotinamide supplementation in at-risk pregnancies (standard prenatal vitamin niacin content may be insufficient for biallelic carriers; higher-dose amidated precursors are rational). **Secondary:** carrier screening in consanguineous families; prenatal/preimplantation genetic testing where the familial variants are known; biochemical screening (urinary xanthurenic acid). **Genetic counseling:** autosomal-recessive recurrence risk (25%), with counseling on the potentially preventable nature of malformations through maternal supplementation.

### 14. Other Species / Natural Disease
**Model/ortholog species:** mouse (*Kynu*; NCBI Gene) and zebrafish NAD-pathway models recapitulate CNDD. Kynureninase is evolutionarily conserved; bacterial kynureninases (e.g., in oral and mosquito gut microbiota) perform the same 3-hydroxykynurenine → 3-hydroxyanthranilic acid reaction ([PMID: 35437328](https://pubmed.ncbi.nlm.nih.gov/35437328/), [PMID: 40988889](https://pubmed.ncbi.nlm.nih.gov/40988889/)), underscoring deep conservation of the enzymatic step. No naturally occurring companion-animal disease is specifically documented for KYNU deficiency.

### 15. Model Organisms
- **Mouse:** *Kynu*-null and *Haao*-null embryos develop VCRL-type malformations from NAD deficiency, and **niacin supplementation during gestation prevents them** ([PMID: 28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/)) — the strongest causal/preventive model. *Nadsyn1* mouse models further dissect precursor requirements ([PMID: 38357931](https://pubmed.ncbi.nlm.nih.gov/38357931/)).
- **Zebrafish:** a CNDD model recapitulates multisystem anomalies ([PMID: 39829932](https://pubmed.ncbi.nlm.nih.gov/39829932/)).
- **Recapitulation:** models reproduce the malformation spectrum and the niacin-rescue phenotype well; **limitation:** they less directly model the human neurodevelopmental/"encephalopathy" component and the full range of mild human presentations.

---

## Limitations and Knowledge Gaps

1. **Few molecularly confirmed KYNU patients.** The evidence base rests on a handful of families; precise prevalence, penetrance, sex ratio, and genotype–phenotype correlations are not statistically defined.
2. **"Encephalopathy" nomenclature vs. reality.** The historical name implies a progressive encephalopathy, but the modern molecular phenotype is congenital malformation ± neurodevelopmental delay. The relationship between the original 1960s "hydroxykynureninuria" cases and the severe CNDD phenotype is a spectrum unified by mechanism, but the neurological manifestations remain under-characterized.
3. **Human embryonic mechanism inferred.** The step from NAD⁺ deficiency to specific malformations is demonstrated in mice/zebrafish; the exact NAD⁺-dependent molecular targets in human embryogenesis are inferred, not directly proven.
4. **Supplementation regimen for KYNU specifically.** Optimal precursor, dose, and timing for human KYNU-deficient pregnancies are extrapolated from NADSYN1/mouse data; no KYNU-specific clinical trial exists.
5. **Modifier genetics.** Whether specific modifier alleles (beyond maternal diet) tune expressivity is unknown.

## Proposed Follow-up Experiments / Actions

1. **Registry and natural history study** of all molecularly confirmed KYNU/HAAO/NADSYN1 (CNDD) patients to quantify penetrance, phenotype frequencies, and long-term neurodevelopmental outcomes.
2. **Prospective maternal NAD-metabolome profiling** in at-risk pregnancies (known biallelic KYNU carriers) to correlate maternal NAD/precursor levels with offspring outcome and define a protective threshold.
3. **Controlled supplementation trial** (nicotinamide vs. nicotinamide riboside, dose-finding) in mouse *Kynu*-null dams to define the KYNU-specific optimal amidated-precursor regimen and critical gestational window.
4. **Functional characterization** of each reported KYNU missense variant (p.T198A, p.R428W, p.R330Q, p.W109S) via recombinant enzyme kinetics and PLP-binding assays, leveraging the structural insights from [PMID: 35658075](https://pubmed.ncbi.nlm.nih.gov/35658075/) and [PMID: 36465553](https://pubmed.ncbi.nlm.nih.gov/36465553/), to build a genotype–activity–phenotype map.
5. **Diagnostic guideline:** promote urinary xanthurenic-acid metabolomic screening + KYNU CNV analysis in the VACTERL/Catel-Manzke diagnostic workup, given the preventable nature of the disorder and the risk of missing large deletions.
6. **Preconception counseling protocol** for consanguineous families with a prior affected child, incorporating high-dose amidated B3 supplementation during subsequent pregnancies.

---

*Evidence-source legend:* Human clinical/genetic (17334708, 31923704, 28792876, 35491967, 36649848); mouse model (28792876, 38357931); zebrafish model (39829932); in vitro/structural (36465553, 35658075); review/hypothesis (42798303, 35484986, 37300479).


## Artifacts

- [OpenScientist final report](Encephalopathy_Due_To_Hydroxykynureninuria-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Encephalopathy_Due_To_Hydroxykynureninuria-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.
