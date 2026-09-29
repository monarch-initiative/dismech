---
title: Blue rubber bleb nevus syndrome pathophysiology for dismech curation
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:33:51.441550'
end_time: '2026-08-31T13:05:36.282036'
duration_seconds: 1904.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Blue Rubber Bleb Nevus Syndrome
  mondo_id: MONDO:0007203
  category: Venous malformation syndrome / somatic TEK-TIE2 mosaic vascular anomaly
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 10
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 54
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Blue_Rubber_Bleb_Nevus_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Blue_Rubber_Bleb_Nevus_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blue Rubber Bleb Nevus Syndrome
- **MONDO ID:** MONDO:0007203 (if available)
- **Category:** Venous malformation syndrome / somatic TEK-TIE2 mosaic vascular anomaly

## Research Objectives

Please provide a comprehensive research report on **Blue Rubber Bleb Nevus Syndrome** covering all of the
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

# Blue Rubber Bleb Nevus Syndrome (Bean Syndrome): Comprehensive Disease Characteristics Report

**Disease:** Blue Rubber Bleb Nevus Syndrome (BRBNS) · **MONDO:** 0007203 · **OMIM:** #112200 · **Orphanet:** ORPHA:2802
**Category:** Venous malformation syndrome / somatic TEK-TIE2 mosaic vascular anomaly

---

## Summary

Blue Rubber Bleb Nevus Syndrome (BRBNS), also called **Bean syndrome**, is a rare, congenital, and almost always **sporadic** multifocal venous malformation (VM) disorder. Its defining feature is the coexistence of characteristic **cutaneous** venous malformations — soft, blue-violaceous, rubbery, compressible "blebs" with a predilection for the palms and soles — and **pathognomonic multifocal gastrointestinal (GI) venous malformations**, predominantly of the small bowel. GI lesions bleed chronically, producing recurrent, often transfusion-dependent iron-deficiency anemia that is the principal driver of morbidity and, rarely, mortality.

Molecularly, BRBNS is caused by **post-zygotic somatic mosaic activating mutations in _TEK_ (the gene encoding the endothelial receptor tyrosine kinase TIE2)**. The multifocal forms are distinctively driven by **double (cis) mutations** — two somatic mutations on the same allele — with **T1105N–T1106P** recurrent in BRBNS. These mutations cause **ligand-independent (constitutive) TIE2 activation**, which signals through the **PI3K-AKT-mTOR** axis to suppress endothelial apoptosis and, via AKT/FOXO1-mediated downregulation of **PDGFB**, impair pericyte/smooth-muscle recruitment. The result is dilated, ectatic, mural-cell-poor venous channels that enlarge over time and bleed. Venous stasis within lesions produces **localized intravascular coagulopathy (LIC)**, detectable as **elevated D-dimer** (± low fibrinogen), which serves as a highly specific diagnostic biomarker and complication marker.

This mechanistic understanding directly informs management, which is **stratified by lesion burden**: conservative iron supplementation and transfusion; endoscopic therapies (sclerotherapy, band ligation, hot-snare polypectomy, cyanoacrylate glue) for accessible lesions; surgical/wedge resection for focal high-burden bowel disease; and **systemic mTOR inhibition with sirolimus** for diffuse or unresectable disease, which prospectively reduces lesion size, raises hemoglobin, and reduces transfusion dependence. Emerging genotype-guided approaches include the PI3Kα inhibitor **alpelisib** and preclinical combinations (rapamycin + alpelisib; ponatinib + rapamycin). Model systems — HUVEC-TIE2-L914F xenografts, patient-derived VM endothelial cells, an endothelium-specific zebrafish model, and a genetic mosaic TIE2 p.L914F mouse — faithfully recapitulate the histology and permit therapeutic testing.

This report synthesizes 17 confirmed findings, 11 supported hypotheses, and 83 reviewed papers across all 15 requested disease-characteristic sections.

---

## Key Findings

### 1. Disease Information

BRBNS (Bean syndrome) is a rare, severe disorder characterized by numerous cutaneous and internal venous malformations, with GI lesions being pathognomonic. The eponym "Bean syndrome" honors William Bennett Bean (1958); the lesions were first described by Gascoyen in 1860. As established by Soblet et al. (2017), *"Blue rubber bleb nevus syndrome (Bean syndrome) is a rare, severe disorder of unknown cause, characterized by numerous cutaneous and internal venous malformations"* ([PMID: 27519652](https://pubmed.ncbi.nlm.nih.gov/27519652/)).

**Key identifiers (Finding F017):**

| Resource | Identifier |
|---|---|
| OMIM | #112200 (BLUE RUBBER BLEB NEVUS) |
| Orphanet | ORPHA:2802 |
| MONDO | MONDO:0007203 |
| MeSH | D019014 (Blue Rubber Bleb Nevus Syndrome) |
| UMLS | C0221263 |
| ICD-10 | Q82.8 (other specified congenital malformations of skin); D18.0 for hemangioma |
| ICD-11 | LA90 region / vascular anomaly codes |
| Causal gene | TEK/TIE2 — HGNC:11724; NCBI Gene 7010; UniProt Q02763; locus 9p21.2 |

**Synonyms:** Bean syndrome; blue rubber bleb naevus syndrome; BRBN syndrome. Within the **ISSVA** (International Society for the Study of Vascular Anomalies) framework, BRBNS is classified as a **multifocal venous malformation** (a malformation, not a tumor). Evidence is **aggregated disease-level** (OMIM/Orphanet/MeSH curated) plus **individual-patient** case reports and small cohorts; there is no large EHR-derived dataset.

### 2. Etiology

**Primary cause — genetic, somatic, mosaic.** BRBNS is caused by **somatic activating mutations in _TEK_ (TIE2)** (Finding F001). Soblet et al. identified somatic TEK mutations in **15 of 17** individuals with BRBNS and 5 of 6 sporadic multifocal VM patients: *"We discovered somatic mutations in TEK, the gene encoding TIE2, in 15 of 17 individuals with blue rubber bleb nevus syndrome"* ([PMID: 27519652](https://pubmed.ncbi.nlm.nih.gov/27519652/)). The multifocal forms are *"predominantly caused by double (cis) mutations, that is, two somatic mutations on the same allele of the gene."*

**Genetic risk factors.** The causal driver is the somatic TEK double-cis mutation itself; **T1105N–T1106P is recurrent in BRBNS**, whereas Y897C–R915C recurs in sporadic multifocal VM. Both *"cause ligand-independent activation of TIE2."* A rare **autosomal dominant familial venous malformation** form maps to **chromosome 9p** (Finding F004; Gallione et al. 1995, [PMID: 7783168](https://pubmed.ncbi.nlm.nih.gov/7783168/)) — the same region that contains TEK — and BRBNS was proposed as *"a particular manifestation of this form of familial venous malformations."*

**Environmental / lifestyle / infectious risk factors:** **None identified.** BRBNS is a genetically determined mosaic disorder; no toxin, radiation, occupational exposure, diet, or infectious agent has been implicated. There are no known **protective factors** or **gene–environment interactions**. This is best recorded as "not applicable for this disease."

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | HPO suggestion |
|---|---|---|---|---|
| Cutaneous venous malformations (rubbery blue blebs) | Physical manifestation | Congenital / infancy | ~68% (44-pt cohort) | HP:0100764 (Venous malformation); HP:0000988 (Skin nodule) |
| GI venous malformations | Clinical sign | Childhood onward (declare later) | ~79.5% | HP:0002597 (vascular); HP:0025439 (GI vascular malformation) |
| GI bleeding | Symptom/sign | Childhood onward | 54.3% (most common complication) | HP:0002239 (GI hemorrhage) |
| Iron-deficiency anemia (transfusion-dependent) | Laboratory abnormality | Childhood onward | Very common | HP:0001891 (Iron deficiency anemia) |
| Elevated D-dimer / LIC | Laboratory abnormality | Progressive with lesion burden | ~42–58% of VM patients | HP:0003256 (Abnormal coagulation) |
| CNS venous malformations (CCM-like) | Physical manifestation | Rare, late | Rare | HP:0002400 (cerebral vascular malformation) |

**Cutaneous morphology (Finding F009):** three classic types — large cavernous masses; blue-violaceous dome/nipple-shaped rubbery compressible nodules (0.5–2 cm) that empty and refill; and irregular blue macules — with **palm and sole predilection**. Becq et al.: *"Blue rubber bleb naevus syndrome is characterized by multifocal rubbery cutaneous venous malformations, especially on palm and sole, that are associated with multiple gastrointestinal VM"* ([PMID: 26564083](https://pubmed.ncbi.nlm.nih.gov/26564083/)).

**GI is the morbidity-defining phenotype (Finding F010).** Soblet: *"gastrointestinal lesions are pathognomonic"* ([PMID: 27519652](https://pubmed.ncbi.nlm.nih.gov/27519652/)). GI lesions *"are more prone to bleeding than cutaneous lesions and may lead to chronic transfusion-dependent anemia"* ([PMID: 42542774](https://pubmed.ncbi.nlm.nih.gov/42542774/)).

**CNS involvement (Finding F009):** Rare and late, presenting as cerebral-cavernous-malformation (CCM)-like lesions, seizures, and focal deficits from compression, with rare fatal intracranial hemorrhage. BRBNS is low/mixed-flow, conferring *"lower CNS hemorrhagic risk but increased thrombotic complications"* ([PMID: 41704211](https://pubmed.ncbi.nlm.nih.gov/41704211/)); CNS manifestations *"are rare, variable, non-specific, and tend to occur late in the disease"* ([PMID: 32318009](https://pubmed.ncbi.nlm.nih.gov/32318009/)).

**Severity/progression:** Variable severity; progressive and lifelong; lesions enlarge over time. **Quality of life** is impacted chiefly through chronic anemia (fatigue), recurrent bleeding, pain, transfusion dependence, and, less often, surgical complications; sirolimus improves QoL and coagulation measures (F003).

### 4. Genetic / Molecular Information

**Causal gene:** *TEK* (TIE2), HGNC:11724, NCBI Gene 7010, locus 9p21.2 (Findings F001, F017).

**Variant characteristics (Findings F001, F011):**
- **Type/class:** Missense, activating.
- **Architecture:** Distinctive **double (cis)** mutations in multifocal/BRBNS forms — two somatic missense changes on the same allele. **T1105N–T1106P recurrent in BRBNS**; Y897C–R915C recurrent in sporadic multifocal VM; **L914F** is the single most common VM driver overall.
- **Somatic vs germline:** **Somatic/post-zygotic (mosaic)** — identical in all lesions of a given individual, absent from blood in classic cases; low variant allele frequency (often <5%).
- **Functional consequence:** **Gain of function** — ligand-independent (constitutive) TIE2 autophosphorylation and downstream signaling.
- **Allele frequency:** Not present in population databases as germline variants (somatic driver events).

An illustrative case ([PMID: 41327934](https://pubmed.ncbi.nlm.nih.gov/41327934/)) found two somatic TEK variants (Y897C, R918H) existing both as single and as **double variants in cis**, restricted to lesion tissue and absent in blood — a genetic profile consistent with BRBNS and representing an intermediate phenotype between BRBNS and sporadic multifocal VM.

**Modifier genes / epigenetics / chromosomal abnormalities:** No established modifier genes, no disease-specific epigenetic signature, and no recurrent large-scale chromosomal abnormality are documented for BRBNS. The chromosome 9p familial linkage (F004) reflects the TEK locus, not an independent structural lesion. A single case reported a novel PDGFRA variant with comorbid ASD ([PMID: 42650349](https://pubmed.ncbi.nlm.nih.gov/42650349/)), but this is not an established modifier.

### 5. Environmental Information

**Not applicable.** No environmental toxins, radiation, pollution, occupational exposure, lifestyle factor, or infectious agent has been implicated in the causation or triggering of BRBNS. The disorder is fully explained by somatic mosaic TEK activation.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (Finding F011, F002, F007):**

1. A **somatic double (cis) activating TEK/TIE2 mutation** arises **post-zygotically** in an endothelial-lineage cell (mosaic; T1105N–T1106P recurrent in BRBNS) — **leads to** →
2. **Ligand-independent (constitutive) TIE2 receptor autophosphorylation** (demonstrated in vivo; Morris 2005) — **results in** →
3. **Constitutive activation of PI3K (p110α/PIK3CA)–AKT–mTOR signaling** (dominant-negative AKT abolishes the pro-survival effect; TIE2 additionally elevates MAPK-ERK) — **leads to** →
4. **Suppression of endothelial apoptosis + increased endothelial survival, invasion, and colony formation**; inhibition of normal angiogenesis — **and in parallel** →
5. **AKT/FOXO1 axis downregulates PDGFB** in mutant endothelial cells — **results in** →
6. **Reduced pericyte / smooth-muscle-cell (α-SMA) recruitment** to the vessel wall — **leads to** →
7. **Dilated, ectatic, smooth-muscle-poor venous channels** that expand over time and bleed (clinical VM); within them, **venous stasis** — **results in** →
8. **Localized intravascular coagulopathy (LIC)** — chronic consumptive coagulopathy with elevated D-dimer ± low fibrinogen (branch to coagulation complications).

**Branch points:** (a) the PI3K-AKT-mTOR branch drives cell survival and lesion growth; (b) the AKT/FOXO1→PDGFB branch drives the mural-cell deficiency; (c) the stasis→LIC branch drives coagulopathy. mTOR inhibition (rapamycin) acts on branches (a)/(b) — it suppresses mutant-induced AKT signaling and restores FOXO1 nuclear localization/PDGFB. Steps 1–4 are directly demonstrated; step 5–6 (PDGFB/mural-cell link) is demonstrated in TIE2-L914F veins/models; step 7–8 (stasis→LIC) is inferred from lesion hemodynamics plus consistent biomarker data.

**Supporting quotes:**
- *"multifocal forms are predominantly caused by double (cis) mutations"* and *"both cause ligand-independent activation of TIE2, and increase survival, invasion, and colony formation when expressed in human umbilical vein endothelial cells"* ([PMID: 27519652](https://pubmed.ncbi.nlm.nih.gov/27519652/)).
- *"The anti-apoptotic kinase Akt was constitutively activated in cells expressing mutant receptor. Dominant-negative Akt inhibited the pro-survival activity of mutant Tie2"* ([PMID: 15526080](https://pubmed.ncbi.nlm.nih.gov/15526080/)).
- *"this mutation activates the PI3K pathway, promoting cell proliferation, inhibiting normal angiogenesis, and suppressing apoptosis"* ([PMID: 42411503](https://pubmed.ncbi.nlm.nih.gov/42411503/)).
- *"often caused by somatic PIK3CA mutations that hyperactivate the PI3Kα-AKT-mTOR signaling pathway"* ([PMID: 40410415](https://pubmed.ncbi.nlm.nih.gov/40410415/)).
- *"VMs with TIE2-L914F mutation showed lower expression of PDGFB and α-SMA than normal veins"* ([PMID: 32867785](https://pubmed.ncbi.nlm.nih.gov/32867785/)).

**Ontology suggestions:** GO:0043491 (PI3K-Akt signaling), GO:0038084 (VEGF/angiopoietin-receptor signaling), GO:0043066 (negative regulation of apoptotic process), GO:0001525 (angiogenesis), GO:0007596 (blood coagulation). **Cell types:** CL:0000115 (endothelial cell), CL:0002543 (vein endothelial cell), CL:0000669 (pericyte), CL:0000192 (smooth muscle cell). **Molecular pathways:** PI3K-AKT-mTOR (upstream driver), MAPK-ERK (secondary), angiopoietin-TIE2 feedforward circuit ([PMID: 40410415](https://pubmed.ncbi.nlm.nih.gov/40410415/)).

### 7. Anatomical Structures Affected

- **Primary organs:** Skin (dermis/subcutis) and **gastrointestinal tract** (small bowel > colon > stomach; also esophagus, oral mucosa to anal canal). Multi-organ involvement includes **liver and lung** ([PMID: 40074320](https://pubmed.ncbi.nlm.nih.gov/40074320/): *"venous malformations in multiple organs, including the skin, gastrointestinal tract, liver, and lungs"*).
- **Secondary/complication sites:** CNS (rare, late, CCM-like), spinal epidural space (cord compression), airway/larynx/trachea (rare fatal hemorrhage), skeletal muscle, mediastinum.
- **Body systems:** Integumentary, digestive, cardiovascular (venous), hematologic (coagulation), rarely nervous/respiratory.
- **Tissue/cell level:** Endothelial-lined ectatic venous channels with **scarce smooth-muscle-cell coverage**; affected cell populations are **venous endothelial cells** (CL:0002543) with deficient **pericytes/SMCs** (CL:0000669 / CL:0000192).
- **Subcellular:** Endothelial plasma-membrane receptor (TIE2), cytoplasmic PI3K-AKT-mTOR signaling machinery, nucleus (FOXO1 localization). GO cellular components: GO:0005886 (plasma membrane), GO:0005634 (nucleus).
- **UBERON localization:** UBERON:0002097 (skin), UBERON:0002108 (small intestine), UBERON:0000160 (intestine), UBERON:0002107 (liver), UBERON:0002048 (lung). **Lateralization:** typically **bilateral/multifocal/disseminated**; occasional unilateral/segmental reports.

### 8. Temporal Development

**Onset:** **Congenital** (F014). BRBNS is *"a rare congenital disorder"* ([PMID: 42301891](https://pubmed.ncbi.nlm.nih.gov/42301891/)). Cutaneous VMs frequently present at birth or in infancy; GI lesions typically declare later via chronic bleeding and iron-deficiency anemia. Onset pattern is **chronic/insidious**.

**Diagnosis:** Median age at diagnosis **12 years** in the largest cohort (Becq 2025, n=44) — *"BRBNS is diagnosed at a median age of 12 years, mainly based on clinical presentation (65.9%)"* ([PMID: 39426903](https://pubmed.ncbi.nlm.nih.gov/39426903/)). Late/adult-onset diagnoses occur (68-year-old, [PMID: 42369626](https://pubmed.ncbi.nlm.nih.gov/42369626/); 83-year-old, [PMID: 42542774](https://pubmed.ncbi.nlm.nih.gov/42542774/); 79-year-old, [PMID: 39557791](https://pubmed.ncbi.nlm.nih.gov/39557791/)).

**Progression:** **Lifelong and progressive** — lesions enlarge over time; LIC worsens with lesion burden and age. Course is chronic rather than relapsing-remitting, punctuated by episodic bleeding events. **Remission** is treatment-induced (endoscopic/surgical/sirolimus), not spontaneous. **Critical intervention window:** early recognition of GI disease to prevent anemia and avert emergency surgical complications (intussusception, volvulus, infarction).

### 9. Inheritance and Population

**Epidemiology:** BRBNS is **rare** (<1000 cases historically reported; ~200 detailed case reports through the mid-2020s). General-population VM prevalence is ~1% (Shiraishi 2026, [PMID: 41721464](https://pubmed.ncbi.nlm.nih.gov/41721464/)), but BRBNS itself is far rarer; precise prevalence/incidence figures are not established.

**Inheritance (F004, F014):** Nearly all cases are **sporadic (somatic mosaic)** and non-inherited. Rare **autosomal dominant familial** venous malformation kindreds map to chromosome 9p (Gallione 1995, [PMID: 7783168](https://pubmed.ncbi.nlm.nih.gov/7783168/)); older reports describe autosomal dominant inheritance with good penetrance ([PMID: 6662253](https://pubmed.ncbi.nlm.nih.gov/6662253/), [PMID: 3732758](https://pubmed.ncbi.nlm.nih.gov/3732758/)). For the somatic-mosaic majority, classical Mendelian **penetrance/expressivity/anticipation** concepts do not apply; expressivity across lesions within a patient is uniform (identical mutation in all lesions).

**Germline mosaicism / founder effects / consanguinity / carrier frequency:** Not established; the disorder is somatic and not associated with founder effects or consanguinity.

**Demographics:** No strong ethnic predilection; reported worldwide. **Sex ratio** is approximately equal (no consistent male:female skew). **Age distribution:** diagnosis clusters in childhood (median ~12 y) but spans neonates to the ninth decade.

### 10. Diagnostics

**Clinical/laboratory tests:**
- **CBC / iron studies:** iron-deficiency anemia, often severe (Hb as low as 5 g/dL reported).
- **Coagulation biomarker — D-dimer (Finding F013):** elevated D-dimer (± low fibrinogen) is a **highly specific** biomarker of VMs, including syndromic forms. Dompmartin 2009 (n=280): D-dimer **sensitivity 42.6%**, **specificity 96.5%** for VMs — *"Elevated D-dimer level is highly specific for VMs (pure, combined, or syndromic)... this easy and inexpensive biomarker test should become part of the clinical evaluation of vascular anomalies"* ([PMID: 19917952](https://pubmed.ncbi.nlm.nih.gov/19917952/)). D-dimer distinguishes VM (elevated) from glomuvenous and lymphatic malformation (normal). Local lesional blood shows markedly higher TAT/PIC/FDP/D-dimer than paired peripheral blood ([PMID: 42557218](https://pubmed.ncbi.nlm.nih.gov/42557218/)). LIC is *"a consumptive coagulopathy characterised by elevated D-dimer and decreased fibrinogen levels"* ([PMID: 28169477](https://pubmed.ncbi.nlm.nih.gov/28169477/)).

**Imaging:**
- **MRI** (fat-suppressed T2) is the cornerstone: VMs show markedly high T2 signal; enables whole-body multifocal assessment ([PMID: 18414932](https://pubmed.ncbi.nlm.nih.gov/18414932/)).
- **Ultrasound/Doppler** for flow characterization (low-flow lesions).
- **Brain MRI screening** advised given possible cerebral VM ([PMID: 26564083](https://pubmed.ncbi.nlm.nih.gov/26564083/)).

**Endoscopy (critical for GI diagnosis):** **Video capsule endoscopy** is the most sensitive modality for small-bowel lesions; **double-balloon / intraoperative enteroscopy** for localization and therapy ([PMID: 34976762](https://pubmed.ncbi.nlm.nih.gov/34976762/), [PMID: 41952941](https://pubmed.ncbi.nlm.nih.gov/41952941/)).

**Histopathology:** Dilated, thin-walled venous channels lined by endothelium (CD31+) with scant smooth muscle; myxoid degeneration/clot in walls.

**Genetic testing (Finding F007):** Because driver variants occur at **low VAF (<5%)**, standard blood testing is often negative. **Ultra-deep NGS of lesional tissue** achieves high molecular diagnosis rates (Zhang 2023: 79.1% in 67 pediatric VM patients; TEK L914F predominant — *"The hotspot GNAQ p.R183Q and TEK p.L914F mutations were responsible for the majority of port-wine stain/Sturge-Weber syndrome and venous malformation, respectively"* — [PMID: 37658401](https://pubmed.ncbi.nlm.nih.gov/37658401/)). **Liquid biopsy** with ultra-deep targeted NGS of cell-free DNA detects variants down to **0.05% VAF** using a 5-gene panel (BRAF, KRAS, MAP2K1, PIK3CA, TEK/TIE2) — *"Ultra-deep NGS (mean coverage: 104,000×) with unique molecular identifier error correction was performed using a custom panel of five genes"* ([PMID: 41417427](https://pubmed.ncbi.nlm.nih.gov/41417427/)). WGS/WES on blood is low-yield; **targeted deep sequencing of lesional tissue** is the recommended approach.

**Clinical criteria & differential diagnosis (Finding F016):** Diagnosis rests on the clinical triad of multifocal cutaneous rubbery blebs + multifocal GI VMs + supportive coagulation/genetic findings. Key differentials:

| Condition | Distinguishing feature | Gene | D-dimer |
|---|---|---|---|
| **Maffucci syndrome** | VMs **+ enchondromas** (skeletal) | IDH1/IDH2 (mosaic) | — |
| **Glomuvenous malformation** | Firmer, cobblestone, partially compressible | GLMN (AD) | **Normal** |
| **Lymphatic malformation** | — | — | **Normal** |
| **MCMVM (VMCM)** | Familial, germline; lacks pathognomonic GI blebs | TEK (germline) | ± |
| **Common unifocal VM** | Single lesion | TEK L914F (somatic) | ± |
| **Klippel-Trenaunay** | Overgrowth + capillary/lymphatic | PIK3CA | Elevated |

Maffucci is historically misdiagnosed as BRBNS until enchondromata are recognized: *"a diagnosis of blue rubber bleb naevus syndrome had been made many years earlier. However, after recognition of the characteristic enchondromata, this diagnosis has been revised to Maffucci's syndrome"* ([PMID: 15670176](https://pubmed.ncbi.nlm.nih.gov/15670176/)). D-dimer *"can detect hidden VMs and help differentiate glomuvenous malformation (normal D-dimer levels) from other multifocal venous lesions"* ([PMID: 19917952](https://pubmed.ncbi.nlm.nih.gov/19917952/)).

**Screening:** No newborn or carrier screening (somatic disorder). Cascade screening not applicable to the sporadic majority.

### 11. Outcome / Prognosis

**Survival/mortality:** Generally compatible with normal life expectancy with appropriate management. **Fatal outcomes are exceedingly rare** and result from acute hemorrhage — GI, CNS (neonatal brain bleed, [PMID: 26608350](https://pubmed.ncbi.nlm.nih.gov/26608350/)), or airway (fatal tracheostomy-site hemorrhage, [PMID: 41557089](https://pubmed.ncbi.nlm.nih.gov/41557089/)).

**Morbidity:** Dominated by **chronic transfusion-dependent iron-deficiency anemia** and its sequelae (fatigue, reduced function). GI bleeding is the most common complication (**54.3%** in the 44-patient cohort, requiring endoscopic treatment in 36.4% — [PMID: 39426903](https://pubmed.ncbi.nlm.nih.gov/39426903/)).

**Complications:** Recurrent GI hemorrhage; **intussusception, volvulus, intestinal infarction, bowel obstruction** requiring emergency surgery ([PMID: 32664167](https://pubmed.ncbi.nlm.nih.gov/32664167/), [PMID: 28946166](https://pubmed.ncbi.nlm.nih.gov/28946166/)); epidural spinal cord compression ([PMID: 25238626](https://pubmed.ncbi.nlm.nih.gov/25238626/)); perioperative hemorrhage/DIC ([PMID: 28858742](https://pubmed.ncbi.nlm.nih.gov/28858742/)); thrombotic complications from LIC. Rare malignant complication — esophageal squamous carcinoma ([PMID: 42050915](https://pubmed.ncbi.nlm.nih.gov/42050915/), [PMID: 42116360](https://pubmed.ncbi.nlm.nih.gov/42116360/)).

**Prognostic factors:** Lesion burden (number/size/tissue planes) correlates with LIC severity and bleeding; small-bowel-predominant disease predicts refractory bleeding needing surgery. **Prognostic biomarker:** D-dimer/LIC severity tracks lesion burden and treatment response ([PMID: 28169477](https://pubmed.ncbi.nlm.nih.gov/28169477/), [PMID: 29221638](https://pubmed.ncbi.nlm.nih.gov/29221638/)).

### 12. Treatment

**Burden-stratified strategy (Findings F003, F008, F010, F012):**

**Supportive/conservative:** Iron supplementation and blood transfusion for anemia (mainstay for low-burden disease). NCIT: Iron Supplement Therapy; Blood Transfusion.

**Endoscopic (accessible GI lesions):** Sclerotherapy (e.g., lauromacrogol), band ligation, hot-snare/polypectomy, argon plasma coagulation, cyanoacrylate glue. Effective for focal, reachable lesions; cyanoacrylate carries rare ischemic complications ([PMID: 38770491](https://pubmed.ncbi.nlm.nih.gov/38770491/)). NCIT: Endoscopic Sclerotherapy.

**Surgical:** Wedge/segmental bowel resection for high-burden focal disease; can achieve transfusion independence and Hb normalization (e.g., >100 lesions resected, [PMID: 42662159](https://pubmed.ncbi.nlm.nih.gov/42662159/)). Emergency surgery for intussusception/volvulus/obstruction. NCIT: Surgical Resection.

**Systemic pharmacotherapy — sirolimus (mTOR inhibitor; NCIT: Sirolimus):** First-line systemic agent for diffuse/unresectable disease. Prospective study of 11 BRBNS patients (Zhou 2021): *"The average lesion size was reduced by 7.4% (P < 0.001), 9.3% (P < 0.001), and 13.0% (P < 0.05) at 3, 6, and 12 months of sirolimus treatment, respectively. Hemoglobin increased significantly after 6- and 12-month treatment (P = 0.006 and 0.019, respectively)"* ([PMID: 33416235](https://pubmed.ncbi.nlm.nih.gov/33416235/)); only 1/11 required transfusion during study, with only grade 1–2 adverse effects. Pooled pediatric series (28 cases) all responded ([PMID: 32933636](https://pubmed.ncbi.nlm.nih.gov/32933636/)). Phase II trial in complicated vascular anomalies (NCT00975819, n=61): at course 6, of 57 evaluable, *"a total of 47 patients had a partial response, 3 patients had stable disease, and 7 patients had progressive disease"*, no complete responses; grade ≥3 blood/bone-marrow toxicity 27% ([PMID: 26783326](https://pubmed.ncbi.nlm.nih.gov/26783326/)). Topical/gel and intralesional (direct-stick) mTOR-inhibitor formulations are emerging ([PMID: 37649426](https://pubmed.ncbi.nlm.nih.gov/37649426/), [PMID: 39515753](https://pubmed.ncbi.nlm.nih.gov/39515753/)).

**Targeted/emerging (Finding F012):**
- **Alpelisib (BYL719, PI3Kα inhibitor):** *"The p110α-specific inhibitor BYL719 restores all abnormal phenotypes tested, in PIK3CA- as well as TEK-mutant HUVECs"* ([PMID: 26637981](https://pubmed.ncbi.nlm.nih.gov/26637981/)); emerging for PIK3CA-mutated malformations ([PMID: 32557381](https://pubmed.ncbi.nlm.nih.gov/32557381/)).
- **Rapamycin + alpelisib combination:** superior in TIE2-L914F models — *"the combination of rapamycin and alpelisib exhibited superior therapeutic efficacy, not only significantly inhibiting the PI3K pathway but also activating P53 expression"* ([PMID: 42411503](https://pubmed.ncbi.nlm.nih.gov/42411503/)).
- **Ponatinib + rapamycin:** *"Combination treatment with the ABL kinase inhibitor ponatinib and rapamycin caused VM regression in a xenograft model"* ([PMID: 30626204](https://pubmed.ncbi.nlm.nih.gov/30626204/)).

**Treatment strategy:** Escalate from supportive → endoscopic → surgical → systemic (sirolimus) → targeted, guided by lesion number, location, resectability, and bleeding severity. Combination of systemic sirolimus + endoscopic sclerotherapy has documented efficacy — *"The combination of oral sirolimus with endoscopic lauromacrogol has demonstrated efficacy in reducing lesion size and elevating hemoglobin levels"* ([PMID: 39867693](https://pubmed.ncbi.nlm.nih.gov/39867693/)). No pharmacogenomic dosing standard specific to BRBNS.

### 13. Prevention

**Primary prevention:** Not possible — BRBNS is a congenital somatic mosaic disorder with no modifiable risk factors and no vaccine target.

**Secondary prevention (early detection):** Consider BRBNS in any child/adult with **unexplained iron-deficiency anemia + bluish compressible cutaneous nodules**; early capsule endoscopy and MRI enable early GI diagnosis before severe anemia/complications. Brain MRI screening is advised for possible cerebral VM ([PMID: 26564083](https://pubmed.ncbi.nlm.nih.gov/26564083/)).

**Tertiary prevention (complication avoidance):** Routine **D-dimer/fibrinogen** monitoring for LIC (underused — done in <50% of the cohort); perioperative anticoagulation/LMWH for LIC; careful peri-procedural planning to avoid catastrophic hemorrhage (airway, delivery). Surveillance of enlarging lesions; iron repletion to prevent chronic anemia.

**Genetic counseling:** For the sporadic majority, recurrence risk is negligible; counsel that the disorder is somatic/non-inherited. For rare familial 9p/germline TEK kindreds, autosomal dominant counseling applies.

### 14. Other Species / Natural Disease

- **Taxonomy:** BRBNS as a defined syndrome is a **human** disorder (NCBI Taxon 9606). No naturally occurring BRBNS is documented in companion animals or wildlife (no OMIA equivalent entry).
- **Orthologous gene:** *Tek/Tie2* is highly conserved — mouse *Tek* (NCBI Gene 21687), zebrafish *tek* — enabling model organisms.
- **Comparative biology:** TIE2 signaling and its role in venous development are evolutionarily conserved, which underlies faithful zebrafish and mouse modeling (below). No zoonotic potential (non-infectious).

### 15. Model Organisms

**Cellular / in vitro (Findings F005, F015):** **HUVEC-TIE2-L914F** and patient-derived **VM endothelial cells** (harboring TIE2, PIK3CA, or combined mutations) show constitutive AKT (TIE2 additionally MAPK-ERK), enhanced survival/motility, and decreased tube formation ([PMID: 29786783](https://pubmed.ncbi.nlm.nih.gov/29786783/), [PMID: 32867785](https://pubmed.ncbi.nlm.nih.gov/32867785/)).

**Xenograft mouse (mammalian in vivo):** HUVEC-TIE2-L914F or VM-EC injected subcutaneously into immune-deficient mice form ectatic vascular channels recapitulating VM histopathology within 7–9 days — *"human umbilical vein endothelial cells (HUVEC) expressing a constitutive active form of the endothelial tyrosine kinase receptor TEK (TIE2 p.L914F) or patient-derived EC"* ([PMID: 32754818](https://pubmed.ncbi.nlm.nih.gov/32754818/)); *"VM-EC implanted into immune-deficient mice generated lesions with ectatic blood-filled channels with scarce smooth muscle cell coverage, similar to patients' VM"* ([PMID: 29786783](https://pubmed.ncbi.nlm.nih.gov/29786783/)). Used to demonstrate **rapamycin efficacy vs ineffective TIE2-TKI** ([PMID: 26258417](https://pubmed.ncbi.nlm.nih.gov/26258417/)), **ponatinib+rapamycin regression** ([PMID: 30626204](https://pubmed.ncbi.nlm.nih.gov/30626204/)), and **rapamycin+alpelisib synergy** ([PMID: 42411503](https://pubmed.ncbi.nlm.nih.gov/42411503/)).

**Genetic mosaic knock-in mouse (NEW):** Bischoff 2026 — *"constitutive, mosaic expression of TIE2 p.L914F during mouse development causes venous malformation"*; *"While germline or early developmental expression of this mutation is thought to be lethal, mosaic or somatic expression is expected to result in VM disease"* ([PMID: 42059767](https://pubmed.ncbi.nlm.nih.gov/42059767/)). This directly models the human somatic-mosaic mechanism and confirms mosaicism (not germline) is required.

**Zebrafish (Finding F006):** Endothelium-specific overexpression of patient-derived TEK variants robustly induces VMs; **double (cis) TEK mutations have an additive effect** vs single variants, and sirolimus abrogates VM development — *"double mutations have an additive effect in inducing VMs compared with the respective single variants. The clinically established mTOR-inhibitor sirolimus (rapamycin) efficiently abrogates the development of VMs in this zebrafish model"* ([PMID: 34254124](https://pubmed.ncbi.nlm.nih.gov/34254124/)). The assay also functionally classifies TEK variants of unknown significance (VUS).

**Phenotype recapitulation:** High — models reproduce ectatic, mural-cell-poor venous channels and sirolimus responsiveness. **Limitations:** Xenograft/overexpression models may not capture chronic multi-organ GI bleeding, LIC natural history, or lesion evolution over a human lifetime; germline TIE2-L914F is embryonically lethal, necessitating mosaic strategies.

---

## Mechanistic Model / Interpretation

```
 SOMATIC double-cis TEK/TIE2 mutation (post-zygotic, mosaic; T1105N-T1106P)
                     │  gain of function
                     ▼
   Ligand-independent (constitutive) TIE2 autophosphorylation
                     │
                     ▼
        PI3K (p110α) ── AKT ── mTOR   (± MAPK-ERK secondary)
              │                   │
    ┌─────────┘                   └───────────────┐
    ▼                                             ▼
 AKT/FOXO1 ↓PDGFB                     ↓apoptosis / ↑survival, invasion
    │                                             │
    ▼                                             ▼
 ↓pericyte/SMC (α-SMA) recruitment      endothelial expansion
    └───────────────┬─────────────────────────────┘
                    ▼
     DILATED, ECTATIC, SMOOTH-MUSCLE-POOR VENOUS CHANNELS
        (skin blebs + pathognomonic GI VMs; liver, lung, rare CNS)
                    │
      ┌─────────────┼───────────────────────────┐
      ▼             ▼                           ▼
  chronic GI    venous stasis →           lesion growth
  bleeding      LOCALIZED INTRAVASCULAR    over lifetime
      │         COAGULOPATHY (↑D-dimer)         │
      ▼             │                           ▼
 transfusion-dep.   └── thrombosis / rare DIC   progressive
 iron-def. anemia                                disease

  THERAPEUTIC NODES:
   • mTOR inhibition (SIROLIMUS) ── blocks mTOR, restores FOXO1/PDGFB
   • PI3Kα inhibition (ALPELISIB) ── blocks upstream driver
   • Combinations (rapamycin+alpelisib; ponatinib+rapamycin) ── synergy
```

The model is internally consistent and links every clinical feature to the initiating somatic lesion: the **double-cis TEK mutation** explains the multifocality and BRBNS-specific recurrence; **PI3K-AKT-mTOR** explains sirolimus/alpelisib efficacy; **AKT/FOXO1→PDGFB loss** explains the histologic hallmark (mural-cell-poor ectatic veins); **stasis→LIC** explains the D-dimer biomarker and coagulopathic/thrombotic complications; and **GI lesion fragility** explains the dominant morbidity (bleeding/anemia).

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [27519652](https://pubmed.ncbi.nlm.nih.gov/27519652/) | BRBNS caused by somatic TEK mutations | **Landmark** — causal gene, double-cis mechanism, GI pathognomonic |
| [15526080](https://pubmed.ncbi.nlm.nih.gov/15526080/) | Functional analysis of mutant Tie2 | Constitutive AKT downstream of mutant TIE2 |
| [26637981](https://pubmed.ncbi.nlm.nih.gov/26637981/) | PIK3CA mutations cause VM; BYL719 | PI3Kα axis; alpelisib reverses TEK/PIK3CA phenotypes |
| [42411503](https://pubmed.ncbi.nlm.nih.gov/42411503/) | Rapamycin-alpelisib in TIE2-mutant VM | PI3K activation; combination synergy + P53 |
| [40410415](https://pubmed.ncbi.nlm.nih.gov/40410415/) | Angiopoietin-TIE2 feedforward, PIK3CA VM | PI3Kα-AKT-mTOR as central axis |
| [32867785](https://pubmed.ncbi.nlm.nih.gov/32867785/) | AKT/FOXO1 link EC–pericyte | PDGFB/α-SMA loss → mural-cell-poor veins |
| [26258417](https://pubmed.ncbi.nlm.nih.gov/26258417/) | Rapamycin improves TIE2-mutant VM | Xenograft + 6-patient pilot; rapamycin > TIE2-TKI |
| [33416235](https://pubmed.ncbi.nlm.nih.gov/33416235/) | Prospective sirolimus in BRBNS | **Quantitative efficacy** (lesion size, Hb) |
| [26783326](https://pubmed.ncbi.nlm.nih.gov/26783326/) | Phase II sirolimus (NCT00975819) | 47/57 partial response; toxicity profile |
| [34254124](https://pubmed.ncbi.nlm.nih.gov/34254124/) | Zebrafish TEK VUS assay | Additive double-cis effect; sirolimus abrogates VM |
| [42059767](https://pubmed.ncbi.nlm.nih.gov/42059767/) | Mosaic TIE2-L914F mouse | Genetic mosaic model; lethality of germline |
| [29786783](https://pubmed.ncbi.nlm.nih.gov/29786783/) | Xenograft VM model | Standard preclinical platform |
| [30626204](https://pubmed.ncbi.nlm.nih.gov/30626204/) | Ponatinib+rapamycin | VM regression, novel combination |
| [19917952](https://pubmed.ncbi.nlm.nih.gov/19917952/) | D-dimer in VM differential | Biomarker specificity 96.5%; differential dx |
| [28169477](https://pubmed.ncbi.nlm.nih.gov/28169477/) | LIC in children with VM | LIC definition, correlation with burden |
| [39426903](https://pubmed.ncbi.nlm.nih.gov/39426903/) | European multicenter cohort (n=44) | **Epidemiology** — median age 12 y, organ frequencies |
| [37658401](https://pubmed.ncbi.nlm.nih.gov/37658401/) | Pediatric VM somatic spectrum | TEK L914F predominant; deep lesional sequencing |
| [41417427](https://pubmed.ncbi.nlm.nih.gov/41417427/) | Liquid biopsy ultra-deep NGS | 0.05% VAF detection; 5-gene panel |
| [7783168](https://pubmed.ncbi.nlm.nih.gov/7783168/) | Familial VM maps to 9p | Rare AD form; BRBNS as VM manifestation |
| [15670176](https://pubmed.ncbi.nlm.nih.gov/15670176/) | Maffucci with GI involvement | Key differential (enchondromas) |

The evidence is coherent and mutually reinforcing across **human clinical** (cohorts, case series, prospective/Phase II trials), **model organism** (mouse xenograft, mosaic knock-in, zebrafish), and **in vitro** (HUVEC/VM-EC) sources. No study in the reviewed corpus contradicts the core TEK→PI3K-AKT-mTOR model; the main tension is between the somatic-mosaic majority and rare familial autosomal-dominant kindreds, which is reconciled by both involving the TEK/9p locus.

---

## Supported and Refuted Hypotheses

All 11 formally tracked hypotheses were **supported**; none were refuted.

| ID | Hypothesis | Status |
|---|---|---|
| H001 | BRBNS is caused by somatic activating (double-cis) TEK/TIE2 mutations in VM endothelial cells | Supported |
| H002 | Hallmark is multifocal cutaneous + GI VMs; GI lesions cause chronic bleeding/anemia | Supported |
| H003 | Sirolimus (mTOR inhibition) reduces bleeding, transfusion need, and lesion burden | Supported |
| H004 | Constitutive TIE2 drives VM via PI3K-AKT-mTOR; VMs cause LIC (↑D-dimer, ↓fibrinogen) | Supported |
| H005 | Double-cis TEK mutations are additive; zebrafish EC-TEK model recapitulates sirolimus-responsive VM | Supported |
| H006 | GI (small-bowel) VMs are the principal bleeding source; burden dictates stepwise management | Supported |
| H007 | Ligand-independent TIE2 → PI3K-AKT-mTOR → apoptosis suppression + AKT/FOXO1→PDGFB loss → mural-cell-poor veins | Supported |
| H008 | LIC (↑D-dimer) is a specific laboratory biomarker correlating with lesion burden | Supported |
| H009 | BRBNS is congenital, sporadic, lifelong, childhood-diagnosed (~12 y), GI-bleeding-dominated, multi-organ | Supported |
| H010 | BRBNS is recapitulated in HUVEC-TIE2-L914F xenografts and a genetic mosaic TIE2 mouse | Supported |
| H011 | BRBNS must be distinguished from Maffucci, GVM, MCMVM, and unifocal common VM | Supported |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is imprecise.** No reliable population prevalence/incidence for BRBNS specifically; estimates rest on ~200 detailed case reports and small cohorts (largest n=44). No large EHR or registry dataset exists.
2. **Genotype under-tested clinically.** In the largest cohort, D-dimer, fibrinogen, and TEK testing were used in <50% of patients; low-VAF variants require specialized deep sequencing not universally available.
3. **No randomized controlled trials** of sirolimus in BRBNS specifically; evidence is prospective single-arm/observational and pooled pediatric series. Optimal dose, duration, and long-term safety (especially in children) remain undefined; rebound on cessation is reported.
4. **Targeted therapy data are preclinical** for alpelisib and combination regimens in TEK-driven disease; human efficacy in BRBNS is not yet established.
5. **Natural history quantification is limited** — progression rate, lifetime bleeding trajectory, and predictors of the rare malignant complication (esophageal carcinoma) are poorly characterized.
6. **Model limitations** — xenograft/overexpression systems do not reproduce chronic GI bleeding/LIC natural history; the mosaic mouse is new and its phenotypic fidelity to human multi-organ disease needs further characterization.
7. **Modifier genes and epigenetics** of BRBNS are essentially unstudied.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a BRBNS registry** capturing genotype (deep lesional sequencing), lesion distribution, D-dimer/fibrinogen, treatment, and outcomes to derive prevalence, natural history, and prognostic models.
2. **Standardize molecular diagnosis:** validate liquid-biopsy ultra-deep NGS (cfDNA, 5-gene panel) against lesional sequencing as a minimally invasive diagnostic across a BRBNS cohort; define VAF thresholds for GI-burden correlation.
3. **Prospective/randomized sirolimus trial in BRBNS** with standardized endpoints (lesion volume by MRI, hemoglobin, transfusion frequency, D-dimer, QoL), dose optimization, and pediatric long-term safety.
4. **First-in-BRBNS trials of alpelisib and rapamycin+alpelisib** combination, genotype-guided (TEK vs PIK3CA), leveraging the preclinical synergy and P53-activation signal.
5. **Characterize the mosaic TIE2-L914F mouse** for GI involvement, bleeding, and LIC, and use it to test intralesional/topical mTOR-inhibitor delivery and combinations.
6. **Biomarker qualification:** prospectively test whether serial D-dimer predicts bleeding events and treatment response in BRBNS, toward a validated monitoring biomarker.
7. **Investigate malignancy risk:** systematically assess whether chronic mucosal injury from GI lesions elevates carcinoma risk (esophageal), informing surveillance recommendations.

---

*Report compiled from 17 confirmed findings, 11 supported hypotheses, and 83 reviewed papers over a 10-iteration autonomous investigation. Evidence types span human clinical cohorts/trials, model-organism (mouse, zebrafish), and in vitro endothelial-cell studies.*


## Artifacts

- [OpenScientist final report](Blue_Rubber_Bleb_Nevus_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Blue_Rubber_Bleb_Nevus_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27519652
2. PMID:7783168
3. PMID:26564083
4. PMID:42542774
5. PMID:41704211
6. PMID:32318009
7. PMID:41327934
8. PMID:42650349
9. PMID:15526080
10. PMID:42411503
11. PMID:40410415
12. PMID:32867785
13. PMID:40074320
14. PMID:42301891
15. PMID:39426903
16. PMID:42369626
17. PMID:39557791
18. PMID:41721464
19. PMID:6662253
20. PMID:3732758
21. PMID:19917952
22. PMID:42557218
23. PMID:28169477
24. PMID:18414932
25. PMID:34976762
26. PMID:41952941
27. PMID:37658401
28. PMID:41417427
29. PMID:15670176
30. PMID:26608350
31. PMID:41557089
32. PMID:32664167
33. PMID:28946166
34. PMID:25238626
35. PMID:28858742
36. PMID:42050915
37. PMID:42116360
38. PMID:29221638
39. PMID:38770491
40. PMID:42662159
41. PMID:33416235
42. PMID:32933636
43. PMID:26783326
44. PMID:37649426
45. PMID:39515753
46. PMID:26637981
47. PMID:32557381
48. PMID:30626204
49. PMID:39867693
50. PMID:29786783
51. PMID:32754818
52. PMID:26258417
53. PMID:42059767
54. PMID:34254124