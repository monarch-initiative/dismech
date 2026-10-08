---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:11:09.148238'
end_time: '2026-10-01T20:27:55.874212'
duration_seconds: 1006.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 74, COVID-19-Related, X-Linked
  mondo_id: MONDO:0026767
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_74_COVID-19-related_X-linked-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_74_COVID-19-related_X-linked-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 74, COVID-19-Related, X-Linked
- **MONDO ID:** MONDO:0026767 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 74, COVID-19-Related, X-Linked** covering all of the
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

# Immunodeficiency 74, COVID-19-Related, X-Linked (IMD74): Comprehensive Disease Characterization Report

**MONDO ID:** MONDO:0026767 | **OMIM:** #301051 | **Gene:** *TLR7* (Xp22.2) | **Category:** Mendelian (X-linked recessive, infection-conditional)

---

## Summary

**Immunodeficiency 74, COVID-19-related, X-linked (IMD74)** is a Mendelian inborn error of immunity in which hemizygous **loss-of-function (LOF) variants in *TLR7*** (Toll-like receptor 7, located at Xp22.2) predispose otherwise healthy males to **life-threatening, hypoxemic COVID-19 pneumonia**. It is a disease defined by the intersection of a rare monogenic susceptibility and an obligate environmental trigger — infection with SARS-CoV-2. In the absence of the virus, affected individuals are generally healthy; the "immunodeficiency" is conditional and virus-specific. IMD74 was the first monogenic cause of severe COVID-19 to be described, discovered by rapid whole-exome sequencing of young men in two unrelated Dutch families in 2020 ([PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)).

The core mechanism is a defect in innate antiviral sensing. TLR7 is an **endosomal single-stranded RNA (ssRNA) sensor** that, upon recognizing guanosine and uridine-containing viral RNA, signals through **MyD88 and IRAK-4** to drive production of **type I and type III interferons (IFNs)**, chiefly by **plasmacytoid dendritic cells (pDCs)**. When TLR7 is non-functional, SARS-CoV-2 goes unsensed, the protective early interferon response fails, the virus replicates unchecked, and a delayed, dysregulated hyperinflammatory response produces severe lung injury. IMD74 therefore sits within the broader paradigm — established during the pandemic — that defective type I IFN immunity (whether genetic or caused by neutralizing autoantibodies) underlies at least 10% of critical COVID-19 pneumonia.

Quantitatively, rare deleterious *TLR7* variants raise the risk of severe COVID-19 roughly **5.3-fold** (95% CI 2.75–10.05; p = 5.41×10⁻⁷) in a large exome-wide burden study, and X-linked TLR7 deficiency accounts for **~1% of life-threatening COVID-19 in men under 60**, with high penetrance. Disease is strongly male-predominant because TLR7 is X-linked; heterozygous female carriers are largely protected because TLR7 **escapes X-inactivation** and is biallelically expressed in up to 30% of female immune cells. Intriguingly, the gene is bidirectionally disease-relevant: while LOF causes severe COVID-19, **TLR7 gain-of-function/hyperresponsiveness** drives interferonopathy (pandemic chilblains) and systemic lupus erythematosus. The most biologically rational, and partially RCT-supported, therapeutic strategy is **early exogenous interferon** (type III IFN-λ given early in infection) alongside vaccination to remove the viral trigger.

---

## Section 1 — Disease Information

**Overview.** IMD74 is an X-linked recessive, SARS-CoV-2–conditional inborn error of immunity. Affected hemizygous males carry loss-of-function variants in *TLR7* and are predisposed to severe/critical COVID-19 (hypoxemic pneumonia frequently requiring high-flow oxygen, mechanical ventilation, or ICU admission), typically despite being young and free of major comorbidities. It is a "disease" only in the context of infection — the genetic lesion is clinically silent until SARS-CoV-2 exposure.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #301051 (Immunodeficiency 74, COVID19-related, X-linked; IMD74) |
| MONDO | MONDO:0026767 |
| Gene | *TLR7*, HGNC, Xp22.2 |
| MeSH (related) | COVID-19; Toll-Like Receptor 7; Primary Immunodeficiency Diseases |
| ICD-10 | U07.1 (COVID-19) + D84.x (other specified immunodeficiencies) — no dedicated code |
| ICD-11 | RA01.0 (COVID-19, virus identified) + 4A00.x immunodeficiency — no dedicated code |

**Synonyms / alternative names.** Immunodeficiency 74, COVID-19-related, X-linked; IMD74; X-linked TLR7 deficiency; X-linked recessive TLR7 deficiency; TLR7-deficiency-associated severe COVID-19.

**Source of information.** Evidence is derived from a mixture of **individual patient data** (family-based WES, case series, functional studies on patient cells) and **aggregated disease-level resources** (OMIM, large multi-cohort genetic burden studies such as the COVID-19 Host Genetics Initiative). The founding studies were individual-patient (EHR + genomic), subsequently generalized by population-scale analyses.

---

## Section 2 — Etiology

**Disease causal factors.** IMD74 is caused by the combination of (1) a **germline genetic lesion** — hemizygous LOF variants in *TLR7* — and (2) an **infectious trigger** — SARS-CoV-2. Neither alone produces the disease. This is a canonical gene–environment (gene–pathogen) interaction: the monogenic defect determines who, among the infected, progresses to life-threatening disease.

**Genetic risk factors.** The causal locus is *TLR7* (Xp22.2). Rare LOF and hypomorphic missense variants are the drivers. The founding Dutch families carried rare putative LOF variants segregating with severe disease ([PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)). In the Italian GEN-COVID nested case-control cohort, deleterious *TLR7* variants were found in 2.1% of severely affected males and 0% of asymptomatic participants ([PMID: 33650967](https://pubmed.ncbi.nlm.nih.gov/33650967/)). The exome-wide burden estimate is a **5.3-fold** increase in severe disease per rare deleterious *TLR7* variant ([PMID: 36327219](https://pubmed.ncbi.nlm.nih.gov/36327219/)).

**Environmental risk factors.** The obligate environmental factor is SARS-CoV-2 infection. **Male sex** is a strong risk modifier (hemizygosity; androgen suppression of pDC IFN-I). Age <60 is the window in which the monogenic contribution is proportionally largest (since in older patients comorbidity and other factors dominate). Broader non-genetic factors that blunt pDC IFN-I (e.g., visceral adiposity) are associated with SARS-CoV-2 infection history ([PMID: 41961811](https://pubmed.ncbi.nlm.nih.gov/41961811/)), providing a converging physiological axis.

**Protective factors.** *Genetic:* carriage of a functional *TLR7* allele; in females, biallelic TLR7 expression due to escape from X-inactivation is protective. *Mechanistic/physiological:* **TLR7 hyperresponsiveness** (the opposite of IMD74) confers pDC-mediated near-sterilizing protection against SARS-CoV-2, at the cost of IFN-driven chilblains ([PMID: 40227192](https://pubmed.ncbi.nlm.nih.gov/40227192/)). Vaccination and functional type I IFN immunity are protective.

**Gene–environment interactions.** IMD74 is essentially a textbook GxE disorder: the penetrant phenotype emerges only when a *TLR7*-deficient host encounters SARS-CoV-2. The same genotype would be expected to raise risk for other TLR7-sensed ssRNA viruses, though the strongest evidence is for SARS-CoV-2.

---

## Section 3 — Phenotypes

The principal phenotype is **severe/critical COVID-19** in a young, otherwise healthy male. Component phenotypes:

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency in affected |
|---|---|---|---|---|---|
| Severe viral pneumonia / hypoxemic respiratory failure | Clinical sign | HP:0002090 (Pneumonia), HP:0012418 (Hypoxemia) | Adult (conditional on infection) | Severe | Defining feature |
| Acute respiratory distress syndrome (ARDS) | Clinical sign | HP:0033677 (ARDS) | Acute | Severe | Common in ICU cases |
| Susceptibility to viral infection (SARS-CoV-2) | Laboratory/clinical | HP:0002718 (Recurrent bacterial/viral infections) | Conditional | Variable | Defining |
| Impaired type I interferon response | Laboratory abnormality | HP:0002721 (Immunodeficiency) | — | — | Essentially all |
| Fever | Symptom | HP:0001945 | Acute | Moderate–severe | Common |
| Lymphopenia | Laboratory abnormality | HP:0001888 | Acute | Variable | Common in severe COVID-19 |

**Phenotype characteristics.** *Onset:* adult-conditional — the phenotype appears only upon SARS-CoV-2 infection, typically in men under 60 (first cases: mean age 26 years, [PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)). *Severity:* severe to critical by definition of the ascertained phenotype, though the underlying genotype can also associate with milder disease in some carriers (variable expressivity). *Progression:* acute and often rapid, following the natural history of severe COVID-19 — a self-limited (resolving or fatal) episode rather than a chronic condition. *Frequency:* among men under 60 with life-threatening COVID-19, ~1% are explained by X-linked TLR7 deficiency ([PMID: 34413140](https://pubmed.ncbi.nlm.nih.gov/34413140/)); described as high penetrance for hypoxemic pneumonia ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)).

**Quality of life impact.** During the acute episode, QoL impact is profound (ICU stay, mechanical ventilation, ECMO in severe cases). Survivors may experience post-ICU and post-COVID sequelae. Between infections, carriers are generally healthy, so chronic QoL burden is low outside infectious episodes.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *TLR7* (Toll-like receptor 7), Xp22.2; encodes an endosomal pattern-recognition receptor. OMIM gene/phenotype #301051.

**Pathogenic variants.**
- **Affected gene:** *TLR7* (HGNC: TLR7). UniProt Q9NYK1.
- **Variant classification:** Rare, biochemically deleterious variants classified as pathogenic/likely pathogenic when functional assays confirm LOF; some are hypomorphic/hypofunctional. Functional validation (luciferase reporter assays, transcriptomic response to agonist) is central to classification because many are private missense variants of otherwise uncertain significance.
- **Variant types:** Predominantly **missense** (e.g., N215S classified as LOF; D332G as hypomorphic in the Spanish cohort, [PMID: 40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/)), as well as frameshift/nonsense putative LOF variants in the founding families ([PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)).
- **Allele frequency:** Very rare in gnomAD (private or ultra-rare), consistent with strong effect sizes.
- **Origin:** Germline, hemizygous in affected males.
- **Functional consequence:** **Loss of function** — impaired ssRNA sensing and failure to induce interferon. This contrasts with the **gain-of-function** end of the TLR7 allelic spectrum seen in lupus/interferonopathy.

**Functional demonstration.** RNA-seq of patient PBMCs after stimulation with the TLR7 agonist imiquimod showed profound pathway impairment, with reduced induction of *IFNA*, *IFNG*, *RSAD2*, *ACOD1*, *IFIT2*, and *CXCL10*; hypomorphic variants failed to upregulate IFN-γ ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/)).

**Modifier genes.** Components of the TLR7 signaling axis (MyD88, IRAK4) are themselves monogenic determinants of hypoxemic COVID-19 ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)), and would be expected to modify or phenocopy the defect. Downstream IFN-pathway genes and autoantibody status (anti–type I IFN) are convergent modifiers of the same end phenotype.

**Epigenetic information.** The most important epigenetic feature is **escape from X-chromosome inactivation**: *TLR7* is biallelically expressed in up to 30% of female immune cells ([PMID: 38481993](https://pubmed.ncbi.nlm.nih.gov/38481993/)), which protects heterozygous female carriers. No skewed X-inactivation was observed in female carriers of N215S or D332G ([PMID: 40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/)).

**Chromosomal abnormalities.** None characteristic; IMD74 is a single-gene disorder, not a structural/aneuploidy syndrome.

---

## Section 5 — Environmental Information

**Infectious agent (the defining environmental factor).** **SARS-CoV-2** (severe acute respiratory syndrome coronavirus 2; NCBI Taxonomy taxid 2697049; genus *Betacoronavirus*). SARS-CoV-2 is a positive-sense ssRNA virus; its genomic/replicative ssRNA (with uridine/guanosine motifs) is the natural TLR7 ligand. Without this trigger the genotype is clinically silent.

**Environmental/physiological modifiers.** **Androgens** suppress pDC IFN-I production ([PMID: 38481993](https://pubmed.ncbi.nlm.nih.gov/38481993/)); **visceral fat obesity** is associated with lower pDC-derived IFN-α and with history of SARS-CoV-2 infection ([PMID: 41961811](https://pubmed.ncbi.nlm.nih.gov/41961811/)). **Propofol** directly binds TLR7 and inhibits its association with MyD88, attenuating IFN production — a potential iatrogenic environmental modifier in sedated/ventilated patients ([PMID: 35899460](https://pubmed.ncbi.nlm.nih.gov/35899460/)).

**Lifestyle factors.** No specific lifestyle factor causes IMD74; general determinants of COVID-19 severity apply. Vaccination is the principal modifiable protective exposure.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A hemizygous **loss-of-function variant in *TLR7*** (Xp22.2) **results in** a non-functional or hypofunctional TLR7 endosomal receptor in a male host.
2. Upon **SARS-CoV-2 infection**, viral ssRNA (guanosine- and uridine-containing) enters the endosome but the defective TLR7 **fails to recognize** it — *loss of dual-ligand sensing at the m-shaped homodimer's two ligand-binding sites* ([PMID: 27742543](https://pubmed.ncbi.nlm.nih.gov/27742543/)).
3. Failed sensing **leads to** absent/blunted **MyD88– and IRAK-4–dependent** downstream signaling ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)).
4. This **results in** failure of **plasmacytoid dendritic cells** to produce **type I (and type III) interferons** — demonstrated as impaired induction of *IFNA*, *IFNG*, *RSAD2*, *IFIT2*, *CXCL10* on agonist challenge ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/)).
5. Absent early interferon **leads to** uncontrolled **SARS-CoV-2 replication** in the respiratory tract (inferred from the IFN-deficiency paradigm; viral kinetics not directly measured in all TLR7 patients).
6. Unchecked viral spread to the lungs **results in** a delayed, dysregulated **hyperinflammatory response** — a late IFN/cytokine surge, macrophage activation, and tissue injury (branch point: pDC-primed macrophage cytokine storm, [PMID: 36083891](https://pubmed.ncbi.nlm.nih.gov/36083891/)).
7. The net result **is** **hypoxemic COVID-19 pneumonia / ARDS** requiring intensive support, with high penetrance ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)).

**Branch (protective mirror):** at the opposite end of the TLR7 dosage spectrum, **TLR7 hyperresponsiveness** produces abnormally high early IFN-I on sensing SARS-CoV-2 ssRNA → near-sterilizing pDC-mediated immunity → asymptomatic/mild infection, with IFN-driven **chilblains** as the trade-off ([PMID: 40227192](https://pubmed.ncbi.nlm.nih.gov/40227192/)).

### Detail by category

- **Molecular pathways:** TLR7 → MyD88 → IRAK4/IRAK1 → IRF7 (and NF-κB) → transcription of type I/III IFNs and ISGs. GO:0002224 (toll-like receptor signaling pathway), GO:0034154 (toll-like receptor 7 signaling pathway), GO:0060337 (type I interferon signaling pathway), GO:0032481 (positive regulation of type I interferon production).
- **Cellular processes:** innate antiviral sensing, interferon production, and downstream inflammation. Defective in pDCs; downstream, pDC-derived IFN-α normally primes macrophages — in its dysregulated form this contributes to the cytokine storm ([PMID: 36083891](https://pubmed.ncbi.nlm.nih.gov/36083891/), [PMID: 37253946](https://pubmed.ncbi.nlm.nih.gov/37253946/)).
- **Protein dysfunction:** LOF missense variants in the ectodomain leucine-rich repeats disrupt ligand binding at the structurally defined first (guanosine) and second (uridine/ssRNA) sites of the activated TLR7 dimer ([PMID: 27742543](https://pubmed.ncbi.nlm.nih.gov/27742543/)).
- **Immune system involvement:** this is a primary innate immunodeficiency of antiviral interferon immunity; it places IMD74 within the ≥10% of critical COVID-19 explained by inborn errors of type I IFN immunity and anti-IFN autoantibodies ([PMID: 34413140](https://pubmed.ncbi.nlm.nih.gov/34413140/)).
- **Tissue damage mechanisms:** delayed/exaggerated inflammation, endothelial injury, and macrophage-driven cytokine storm in the lung; late IFN surge amplifies inflammation ([PMID: 40939529](https://pubmed.ncbi.nlm.nih.gov/40939529/)).
- **Molecular profiling:** transcriptomic impairment of the TLR7/ISG program in patient cells ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/)); single-cell/lung studies show pDC infiltration coupling to macrophage IFN signatures in severe disease ([PMID: 36083891](https://pubmed.ncbi.nlm.nih.gov/36083891/)).

**Cell types (CL):** plasmacytoid dendritic cell (CL:0000784); macrophage (CL:0000235); monocyte-derived macrophage. **Upstream vs downstream:** the *TLR7* lesion and failed pDC IFN-I are upstream; viral replication, late cytokine storm, and lung injury are downstream.

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary: **lung** (UBERON:0002048) — the site of hypoxemic pneumonia/ARDS. Secondary/systemic: multi-organ involvement via systemic inflammation (kidney failure, need for ECMO in severe cases). Body system: **respiratory system** (UBERON:0001004) primarily; **immune/hematopoietic system** functionally.

**Tissue and cell level.** Affected tissues: pulmonary alveolar epithelium and endothelium (site of injury); the functionally defective cells are **plasmacytoid dendritic cells** (CL:0000784), with downstream involvement of **macrophages** (CL:0000235) and monocytes. pDCs infiltrate the lung in severe COVID-19 ([PMID: 36083891](https://pubmed.ncbi.nlm.nih.gov/36083891/)).

**Subcellular level.** The key compartment is the **endosome/endolysosome** (GO:0005768 endosome; GO:0010008 endosome membrane) — the location of TLR7. Signaling also engages trafficking machinery and the nucleus (IRF7-driven transcription).

**Localization / lateralization.** Pulmonary involvement is typically **bilateral** (bilateral ground-glass/consolidative pneumonia characteristic of severe COVID-19).

---

## Section 8 — Temporal Development

**Onset.** The underlying genotype is congenital, but the **clinical phenotype is adult-conditional** and **acute**, triggered by SARS-CoV-2 infection. First-described cases were young men (mean 26 years) ([PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)). Onset pattern: acute, following the incubation and early-symptomatic phase of COVID-19.

**Progression.** Follows the natural history of severe COVID-19: an early viral-replication phase (where interferon deficiency is most consequential) transitioning to a late hyperinflammatory phase with hypoxemia and ARDS. Progression can be **rapid**. The episode is **self-limited** in the sense of resolving (recovery) or proving fatal, rather than chronic/lifelong — though the predisposition persists for future ssRNA-viral exposures.

**Patterns / critical periods.** There is a well-defined **early therapeutic window**: interferon replacement helps when given early but not late (see Treatment). This maps onto the biology — the deficiency matters most during early viral control.

---

## Section 9 — Inheritance and Population

**Epidemiology.** No standalone prevalence/incidence figure exists because the disease is conditional on a pandemic exposure. Among the exposed with severe disease: deleterious *TLR7* variants in **2.1% of severely affected males** vs 0% asymptomatic ([PMID: 33650967](https://pubmed.ncbi.nlm.nih.gov/33650967/)); **~1%** of life-threatening COVID-19 in men under 60 is attributable to X-linked TLR7 deficiency ([PMID: 34413140](https://pubmed.ncbi.nlm.nih.gov/34413140/)).

**Inheritance.** **X-linked recessive**, environmentally (SARS-CoV-2) conditioned. Males are hemizygous and affected; females are generally protected.

**Penetrance / expressivity.** Described as **high penetrance** for hypoxemic pneumonia upon infection ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)), but penetrance is necessarily conditional on infection and is modulated by viral dose, variant severity (LOF vs hypomorphic), age, and sex. Expressivity is variable (critical pneumonia to milder disease).

**Sex ratio.** Strongly **male-predominant**. Mechanistic basis: (1) hemizygosity; (2) **escape from X-inactivation** — biallelic TLR7 expression in up to 30% of female immune cells buffers heterozygous females ([PMID: 38481993](https://pubmed.ncbi.nlm.nih.gov/38481993/)); (3) androgens suppress, and female pDCs produce more, IFN-I. In the Spanish cohort, LOF/hypomorphic variants were found only in male cases, with no skewed X-inactivation in female carriers ([PMID: 40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/)).

**Sex-consistency of rare-variant burden.** Notably, the *population burden* association of rare deleterious *TLR7* variants with severe disease was **statistically consistent across sexes** (5.3-fold) ([PMID: 36327219](https://pubmed.ncbi.nlm.nih.gov/36327219/)) — biallelic females carrying two hits, or heterozygous females with unfavorable expression, can still be at risk, even though clinically ascertained severe cases are overwhelmingly male.

**Population demographics.** Variants have been identified across Dutch, Italian, and Spanish cohorts and in multinational consortia (12 countries in the burden study). No single founder mutation; most variants are private/family-specific. Carrier frequency of deleterious variants is very low (ultra-rare in gnomAD).

---

## Section 10 — Diagnostics

**Genetic testing (definitive).** Diagnosis rests on identifying a deleterious *TLR7* variant, usually via **whole-exome or whole-genome sequencing**, as in the founding studies (rapid WES, [PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/)). Targeted *TLR7* single-gene sequencing or inclusion of *TLR7* in inborn-errors-of-immunity / severe-COVID gene panels is appropriate. Because many variants are private missense, **functional validation is essential** — luciferase reporter assays and transcriptomic response to TLR7 agonists classify variants as LOF, hypomorphic, or benign ([PMID: 40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/), [PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/)).

**Functional / immunological assays.** Stimulate patient PBMCs or isolated pDCs with TLR7 agonists (**imiquimod/R837, R848**) and measure IFN-α/IFN-γ and ISG induction (RNA-seq or protein). TLR7-deficient cells show profound impairment ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/)). Low pDC IFN-α on TLR7/8 stimulation is a functional biomarker ([PMID: 41961811](https://pubmed.ncbi.nlm.nih.gov/41961811/)).

**Laboratory tests.** General severe-COVID labs (lymphopenia, elevated inflammatory markers). Low circulating/inducible type I IFN supports the diagnosis.

**Imaging.** Chest CT showing bilateral ground-glass opacities/consolidation typical of severe viral pneumonia (supportive, non-specific).

**Clinical criteria / differential diagnosis.** A young man with no major comorbidity presenting with unexpectedly severe/critical COVID-19 should prompt consideration of IMD74 and related IEIs. **Differential:** autosomal inborn errors of type I IFN immunity (e.g., *IRF7*, *IFNAR1*); **MyD88/IRAK-4 deficiency** (phenocopy, [PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)); and the acquired phenocopy, **anti–type I IFN autoantibodies** (present in ≥10% of critical COVID-19, [PMID: 37209324](https://pubmed.ncbi.nlm.nih.gov/37209324/)). Autoantibody testing distinguishes the acquired form.

**Screening.** Genetic screening for *TLR7* has been proposed for young men with severe COVID-19 without predisposing comorbidities ([PMID: 34367187](https://pubmed.ncbi.nlm.nih.gov/34367187/)). Cascade testing of male relatives and carrier evaluation of female relatives is reasonable.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** Prognosis tracks that of critical COVID-19: high morbidity, substantial ICU mortality in the pre-vaccine era, particularly in those progressing to ARDS/ECMO. There is no disease-specific survival curve distinct from severe COVID-19 overall, but affected males are at high risk of life-threatening disease upon infection.

**Morbidity and function.** During the acute episode: mechanical ventilation, ECMO, prolonged ICU stay. Survivors face post-ICU/post-COVID sequelae. Between infections, carriers are generally healthy.

**Disease course / recovery.** The episode resolves or is fatal; recovery potential is good for those who survive the acute phase, though the predisposition persists.

**Prognostic factors.** Earlier antiviral/interferon intervention (favorable), timing within the early window, variant severity (LOF worse than hypomorphic), age, and co-existing anti-IFN autoantibodies (which would compound the deficiency). Prior vaccination is strongly favorable.

---

## Section 12 — Treatment

IMD74 lacks a dedicated approved therapy; management combines **standard severe-COVID care** with a **mechanism-targeted rationale**: replace the missing interferon early and remove the viral trigger.

**Interferon replacement (mechanism-targeted; the central rationale).** Because the defect is failed early IFN production, **exogenous interferon** is biologically rational. The TOGETHER platform RCT showed a single early subcutaneous dose of **pegylated interferon lambda-1a** (type III IFN-λ) in outpatients within 7 days of symptom onset reduced hospitalization/ED visits to **2.7% vs 5.6%** placebo (RR 0.49; 95% Bayesian CI 0.30–0.76; posterior probability of superiority >99.9%) ([PMID: 36780676](https://pubmed.ncbi.nlm.nih.gov/36780676/)). Crucially, benefit is **time-dependent**: a phase 2 trial in already-hospitalized (late) patients was negative (global OR 0.76; 95% CI 0.35–1.66; p = 0.49) ([PMID: 40818744](https://pubmed.ncbi.nlm.nih.gov/40818744/)), and an early small outpatient trial did not shorten viral shedding ([PMID: 33785743](https://pubmed.ncbi.nlm.nih.gov/33785743/)). *Caveat:* these RCTs were in general (genotype-unselected) populations; genotype-stratified trials in TLR7-deficient patients have not been done, so extrapolation is inferential. NCIT: Interferon Therapy; Recombinant Interferon.

**Antivirals.** Early direct-acting antivirals (e.g., nirmatrelvir/ritonavir, remdesivir, molnupiravir) to limit replication during the window when IFN deficiency is most consequential. NCIT: Antiviral Agent.

**Immunomodulation in the inflammatory phase.** Standard severe-COVID care (dexamethasone, IL-6 blockade such as tocilizumab, JAK inhibitors) for the late hyperinflammatory phase. Note the biological tension: IFN helps early, anti-inflammatory therapy helps late.

**Pharmacogenomic / iatrogenic caution.** **Propofol** directly binds TLR7 and inhibits its association with MyD88, attenuating IFN responses ([PMID: 35899460](https://pubmed.ncbi.nlm.nih.gov/35899460/)) — a consideration for sedation choice in these patients.

**Prevention as treatment adjunct.** Vaccination removes/attenuates the obligate trigger and is the single most important intervention (see Section 13).

**Advanced / experimental.** No gene therapy exists. Conceptually, IFN-based or pDC-targeted strategies and early IFN-λ remain the most rational experimental directions; genotype-guided trials are a logical next step.

---

## Section 13 — Prevention

**Primary prevention.** **Vaccination against SARS-CoV-2** is the cornerstone — it reduces infection and severity and thereby removes the condition under which the genotype becomes pathogenic. Vaccination is associated with reduced inflammatory marker trajectories after infection ([PMID: 37659419](https://pubmed.ncbi.nlm.nih.gov/37659419/)). Risk-factor modification and exposure avoidance in known carriers.

**Secondary prevention.** Early diagnosis and early antiviral/IFN intervention in infected carriers (exploiting the early therapeutic window). Prioritization of at-risk males for early testing and treatment.

**Genetic screening and counseling.** Proposed genetic screening of young men with severe COVID-19 without comorbidity ([PMID: 34367187](https://pubmed.ncbi.nlm.nih.gov/34367187/)); **cascade genetic testing** of relatives; **genetic counseling** for X-linked inheritance (carrier mothers, 50% transmission to sons). Female carriers should be informed that biallelic TLR7 expression generally protects them but that rare-variant risk is statistically sex-consistent.

**Tertiary prevention.** Prevent complications of severe COVID-19 (standard ICU prophylaxis, early immunomodulation in the inflammatory phase).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs.** *TLR7* is evolutionarily conserved. Mouse *Tlr7* (NCBI Gene 170743) is the principal ortholog; rat and other mammalian orthologs exist. The receptor's ssRNA-sensing function is conserved across mammals.
- **Natural disease.** No well-documented naturally occurring "IMD74-equivalent" (TLR7-deficiency severe-COVID) disease in companion animals or wildlife is established in the reviewed literature. Cross-species SARS-CoV-2 susceptibility (e.g., in certain mammals) exists but is not characterized as a TLR7-deficiency phenotype.
- **Comparative biology.** The TLR7–MyD88–IFN axis is conserved, making mouse *Tlr7* models informative for mechanism. Species differences in TLR7 ligand specificity and endosomal biology temper direct translation.
- **Zoonotic note.** SARS-CoV-2 itself is zoonotic in origin, but IMD74 as a host-genetic condition is human.

---

## Section 15 — Model Organisms

- **Mouse (*Tlr7*).** *Tlr7*-knockout mice are the standard model for TLR7 function and recapitulate loss of ssRNA/imiquimod responsiveness and impaired IFN induction. They are widely used to dissect the TLR7→MyD88→IRF7 axis. *Relevance to IMD74:* strong for the sensing/IFN mechanism; the human COVID phenotype is only partially modeled because murine SARS-CoV-2 infection requires adapted virus or humanized ACE2.
- **Gain-of-function / lupus models.** TLR7 gain-of-function and the downstream **SLC15A4–TASL–IRF5** axis drive murine lupus ([PMID: 42679023](https://pubmed.ncbi.nlm.nih.gov/42679023/), [PMID: 34197340](https://pubmed.ncbi.nlm.nih.gov/34197340/)), illuminating the opposite (hyperfunction) end of the TLR7 dosage spectrum and the bidirectional disease relevance of the gene.
- **In vitro / cellular models.** Patient-derived PBMCs and pDCs stimulated with TLR7 agonists (imiquimod, R848), and HEK/reporter cell luciferase assays for variant classification, are the key human in-vitro systems ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/), [PMID: 40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/)).
- **Model limitations.** Mouse models do not reproduce the full human severe-COVID pneumonia phenotype; human cellular assays capture the sensing/IFN defect but not whole-organism disease. No perfect animal model of IMD74 exists.
- **Resources:** MGI (mouse *Tlr7*), IMPC/IMSR for knockout lines.

---

## Mechanistic Model / Interpretation

```
  Hemizygous TLR7 loss-of-function variant (Xp22.2, male host)
                        │
                        ▼
      Non-functional endosomal TLR7 (dual G/U-ssRNA sensor)
                        │  SARS-CoV-2 infection (obligate trigger)
                        ▼
   Viral ssRNA NOT sensed in endosome  ◄──── structural basis: 2 ligand sites (PMID 27742543)
                        │
                        ▼
      No MyD88/IRAK4 signaling  (phenocopied by MyD88/IRAK4 deficiency)
                        │
                        ▼
   pDCs fail to produce type I/III IFN  (↓IFNA/IFNG/ISGs; PMID 34952932)
                        │
          ┌─────────────┴─────────────┐
          ▼ (LOF branch)              ▲ (GOF mirror branch)
  Early antiviral defense fails   Hyperresponsive TLR7 → excess
          │                        early IFN → near-sterilizing
          ▼                        immunity + chilblains (PMID 40227192)
  Unchecked SARS-CoV-2 replication
          │
          ▼
  Late hyperinflammation / macrophage cytokine storm (PMID 36083891)
          │
          ▼
  Hypoxemic COVID-19 pneumonia / ARDS (high penetrance; PMID 36880831)

  THERAPEUTIC LOGIC:  replace IFN EARLY (IFN-λ RCT, PMID 36780676)
                      — ineffective if given LATE (PMID 40818744)
```

The unifying interpretation is **TLR7 dosage**: too little early interferon (LOF) → severe COVID-19; too much (GOF) → autoinflammation/lupus but viral protection. IMD74 is the LOF pole of this axis. The clinical corollary — intervene early with interferon and remove the trigger by vaccination — follows directly from the causal chain.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/) | Genetic variants among young men with severe COVID-19 | Founding discovery (Dutch families, rapid WES) | Human clinical/genomic |
| [33650967](https://pubmed.ncbi.nlm.nih.gov/33650967/) | TLR7 variants in males (GEN-COVID) | Replication: 2.1% of severe males, 0% asymptomatic | Human case-control |
| [34413140](https://pubmed.ncbi.nlm.nih.gov/34413140/) | X-linked TLR7 deficiency in ~1% of men <60 | Quantifies attributable fraction; ≥10% IFN paradigm | Human cohort |
| [36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/) | MyD88/IRAK-4 deficiency & hypoxemic COVID-19 | Defines sensor/adaptors/pDC mechanism; high penetrance | Human clinical |
| [34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/) | Rare TLR7 variants impair cytokine signaling | Functional/transcriptomic proof of pathway impairment | In vitro / patient cells |
| [38481993](https://pubmed.ncbi.nlm.nih.gov/38481993/) | Androgens & biallelic TLR7 expression | Basis for male predominance / carrier protection | Human immunology |
| [40423910](https://pubmed.ncbi.nlm.nih.gov/40423910/) | Spanish multicentric TLR7 study | Variant classification (N215S LOF; D332G hypomorphic); no skewed XCI | Human genetic/functional |
| [40227192](https://pubmed.ncbi.nlm.nih.gov/40227192/) | TLR7 hyperresponsiveness & chilblains | GOF mirror branch; dosage model | Human mechanism |
| [27742543](https://pubmed.ncbi.nlm.nih.gov/27742543/) | TLR7 dual receptor structure | Structural basis for sensing lost in LOF | Structural biology |
| [36780676](https://pubmed.ncbi.nlm.nih.gov/36780676/) | Early peginterferon lambda (TOGETHER) | RCT: early IFN reduces progression (RR 0.49) | Human RCT |
| [40818744](https://pubmed.ncbi.nlm.nih.gov/40818744/) | Peginterferon λ in hospitalized patients | Negative late-treatment trial (OR 0.76, p=0.49) | Human RCT |
| [36327219](https://pubmed.ncbi.nlm.nih.gov/36327219/) | Exome-wide burden (HGI) | 5.3-fold risk; sex-consistent | Large human genetic |
| [37209324](https://pubmed.ncbi.nlm.nih.gov/37209324/) | Anti–type I IFN auto-Abs in BAL | Acquired phenocopy / differential | Human clinical |
| [36083891](https://pubmed.ncbi.nlm.nih.gov/36083891/) | pDC–macrophage cytokine storm | Downstream inflammatory branch | Human/mechanistic |

**Key verbatim support.**
- *"Severe coronavirus disease 2019 (COVID-19) can occur in younger, predominantly male, patients without preexisting medical conditions."* ([PMID: 32706371](https://pubmed.ncbi.nlm.nih.gov/32706371/))
- *"Overall, we found TLR7 deleterious variants in 2.1% of severely affected males and in none of the asymptomatic participants."* ([PMID: 33650967](https://pubmed.ncbi.nlm.nih.gov/33650967/))
- *"X-linked recessive deficiency of TLR7, a MyD88- and IRAK-4-dependent endosomal ssRNA sensor, impairs SARS-CoV-2 recognition and type I IFN production in plasmacytoid dendritic cells (pDCs)… underlying hypoxemic COVID-19 pneumonia with high penetrance."* ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/))
- *"Our investigation revealed a profound impairment of the TLR7 pathway in patients carrying loss-of-function variants."* ([PMID: 34952932](https://pubmed.ncbi.nlm.nih.gov/34952932/))
- *"TLR7 is a dual receptor for guanosine and uridine-containing ssRNA … all formed an activated m-shaped dimer with two ligand-binding sites."* ([PMID: 27742543](https://pubmed.ncbi.nlm.nih.gov/27742543/))
- *"carrying a rare deleterious variant in the SARS-CoV-2 sensor toll-like receptor TLR7 (on chromosome X) was associated with a 5.3-fold increase in severe disease (95% CI: 2.75-10.05, p = 5.41x10-7). This association was consistent across sexes."* ([PMID: 36327219](https://pubmed.ncbi.nlm.nih.gov/36327219/))
- *"A total of 25 of 931 patients (2.7%) in the interferon group had a primary-outcome event, as compared with 57 of 1018 (5.6%) in the placebo group … relative risk, 0.49."* ([PMID: 36780676](https://pubmed.ncbi.nlm.nih.gov/36780676/))

---

## Limitations and Knowledge Gaps

1. **Conditional penetrance is hard to quantify.** Because disease requires SARS-CoV-2 infection, true penetrance depends on exposure, viral dose, and timing; "high penetrance" is an estimate conditional on infection, not an unconditional figure.
2. **No genotype-stratified trials.** All interferon RCT evidence comes from genotype-unselected populations. Whether early IFN-λ specifically rescues TLR7-deficient patients has not been tested directly — the therapeutic rationale is strong but inferential.
3. **Variant interpretation burden.** Many *TLR7* variants are private missense requiring functional validation; VUS abound, and standardized ACMG classification for this conditional phenotype is still maturing.
4. **Female risk is paradoxical.** Clinically ascertained cases are overwhelmingly male, yet the population burden is sex-consistent (5.3-fold). The quantitative risk to heterozygous and biallelic females is incompletely resolved.
5. **No faithful animal model** of the whole-organism severe-COVID phenotype exists; mouse *Tlr7* KO captures the sensing defect but not human SARS-CoV-2 pneumonia without humanization.
6. **Overlap with acquired phenocopy.** Anti–type I IFN autoantibodies produce an overlapping end phenotype; disentangling genetic from acquired IFN deficiency in individual patients requires both genetic and autoantibody testing.
7. **Epidemiology is pandemic-dependent.** Prevalence/incidence of the clinical phenotype will vary with viral variants, population immunity, and vaccination coverage.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified interferon trial.** Conduct a prospective early-treatment trial of IFN-λ (or IFN-α) in genetically confirmed TLR7-deficient (and MyD88/IRAK4-deficient) patients at diagnosis, testing the central mechanistic prediction directly.
2. **Prospective screening protocol.** Implement rapid *TLR7* sequencing plus a functional pDC IFN assay for young men hospitalized with unexplained severe COVID-19, enabling early mechanism-guided therapy and cascade testing.
3. **Standardized functional classifier.** Build a validated luciferase + transcriptomic pipeline and a curated variant database to resolve *TLR7* VUS and generate ACMG-compatible, functional-evidence-weighted classifications.
4. **Female carrier risk study.** Quantify risk in heterozygous and biallelic female carriers as a function of X-inactivation pattern and TLR7 expression, reconciling the sex-consistent burden with male clinical predominance.
5. **Dosage-axis mapping.** Systematically map TLR7 LOF↔GOF variants against clinical outcomes (severe COVID-19 vs protection/chilblains vs lupus) to formalize the dosage model and identify the protective "sweet spot."
6. **Avoid TLR7-inhibiting sedation.** Evaluate clinically whether propofol (a TLR7 inhibitor) worsens outcomes in TLR7-deficient ventilated patients and whether alternative sedation improves IFN responses.
7. **Broaden the viral scope.** Test whether TLR7-deficient individuals are predisposed to severe disease from other ssRNA viruses (influenza, other coronaviruses), which the mechanism predicts.

---

*Report compiled from 5 iterations, 8 confirmed findings, and 31 reviewed papers. Evidence spans human clinical/genomic studies, large population genetics, functional in-vitro assays, structural biology, and randomized controlled trials.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_74_COVID-19-related_X-linked-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_74_COVID-19-related_X-linked-deep-research-openscientist_artifacts/final_report.pdf)