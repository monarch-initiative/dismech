---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-01T20:49:17.020435'
end_time: '2026-08-01T21:15:57.379955'
duration_seconds: 1600.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculofaciocardiodental Syndrome
  mondo_id: ''
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
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Oculofaciocardiodental_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Oculofaciocardiodental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculofaciocardiodental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculofaciocardiodental Syndrome** covering all of the
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

# Oculofaciocardiodental (OFCD) Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** Oculofaciocardiodental Syndrome
**OMIM:** 300166 · **Orphanet:** ORPHA:2712 · **MONDO:** 0010588 · **Category:** Mendelian (X-linked dominant, male-lethal)
**Causal gene:** *BCOR* (BCL6 corepressor), Xp11.4

---

## Summary

Oculofaciocardiodental (OFCD) syndrome is an ultra-rare X-linked dominant, presumptively male-lethal multiple congenital anomaly disorder caused by germline **loss-of-function (null/truncating) mutations in *BCOR***, the gene encoding the BCL6 corepressor located at Xp11.4. The condition is defined clinically by a diagnostic tetrad reflected in its name — **ocular** (congenital cataract, microphthalmia, secondary glaucoma), **facial** (dysmorphism: long narrow face, high nasal bridge, broad/bifid nose, cleft palate), **cardiac** (atrial/ventricular septal defects, valvular anomalies, laterality defects/dextrocardia), and **dental** anomalies — with **radiculomegaly of the canines (root gigantism)** serving as the pathognomonic sign that frequently brings these patients to clinical attention through dentistry. Fewer than a few hundred cases have been documented worldwide, and the disorder is chronically underrecognized.

Mechanistically, BCOR is a defining subunit of the non-canonical **Polycomb repressive complex 1.1 (PRC1.1)** — together with RING1B/RNF2, PCGF1, and KDM2B — which is recruited to nonmethylated CpG islands to remove H3K36me2 and deposit repressive H2A monoubiquitylation. Loss of BCOR function produces at least **two well-characterized, tissue-specific causal chains**. In dental mesenchymal stem cells, BCOR loss derepresses **AP-2α (TFAP2A)** and increases activating histone marks (H3K4/H3K36 methylation), enhancing osteo-/dentinogenic potential and driving the pathognomonic radiculomegaly; nonsense-mediated mRNA decay (NMD) of premature-termination-codon *BCOR* transcripts (via UPF1) modulates BMP2 and is integral to this phenotype. In the left lateral plate mesoderm, the **BCL6–BCOR complex normally restrains Notch signaling**; its loss permits uncontrolled Notch activity, ESR1/HDAC1-mediated silencing of *Pitx2*, and consequent cardiac and laterality defects.

A key genotype–phenotype dosage rule emerges: **null *BCOR* alleles cause female OFCD (lethal in hemizygous males)**, whereas the **hypomorphic missense variant c.254C>T (p.Pro85Leu)** produces the allelic, milder **male X-linked recessive Lenz microphthalmia syndrome**. The phenotypic spectrum has expanded to include neurological features, pituitary/brain abnormalities, and an emerging tumor-predisposition dimension (lymphoma, insulinomas), consistent with BCOR's known tumor-suppressor role in leukemias and sarcomas. No disease-modifying therapy exists; management is symptomatic, multidisciplinary, and accompanied by genetic counseling for X-linked reproductive risk.

---

## 1. Disease Information

**Overview.** OFCD syndrome is a rare X-linked dominant developmental disorder affecting the eyes, face, heart, and teeth. It was first described by Hayward in 1980 and is characterized by congenital cataracts, dysmorphic facial features, congenital heart disease, and distinctive dental abnormalities, most notably **radiculomegaly (root gigantism) of the canines**, which is pathognomonic ([PMID: 30484210](https://pubmed.ncbi.nlm.nih.gov/30484210/); [PMID: 23827343](https://pubmed.ncbi.nlm.nih.gov/23827343/)). It is frequently unrecognized by medical and dental professionals, and historically only ~20 cases were reported, though the count has grown with molecular diagnosis ([PMID: 19093058](https://pubmed.ncbi.nlm.nih.gov/19093058/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 300166 |
| Orphanet | ORPHA:2712 |
| MONDO | MONDO:0010588 |
| Gene (HGNC) | *BCOR* (HGNC:20893), Xp11.4 |
| MeSH | Oculofaciocardiodental syndrome / Microphthalmia (associated) |

**Synonyms / alternative names.** OFCD syndrome; Oculo-facio-cardio-dental syndrome; MCOPS2 (in the microphthalmia syndromic series); part of the "X-linked microphthalmia" spectrum allelic with **Lenz microphthalmia syndrome (MAA2)**.

**Information source.** Disease-level knowledge derives predominantly from **aggregated resources (OMIM, Orphanet)** and from **individual patient case reports/small family series** rather than large EHR datasets, reflecting the disorder's rarity.

---

## 2. Etiology

**Primary cause — genetic.** OFCD is a monogenic Mendelian disorder caused by **germline loss-of-function mutations in *BCOR***. Ng et al. (2004) identified frameshift, deletion, and nonsense mutations in *BCOR* across seven OFCD families, establishing null *BCOR* alleles as causal ([PMID: 15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/)):

> "we found different frameshift, deletion and nonsense mutations in BCOR in seven families affected with OFCD"

Subsequent cohorts confirmed *BCOR* as the sole molecular cause ([PMID: 15770227](https://pubmed.ncbi.nlm.nih.gov/15770227/); [PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)):

> "Our data confirm that BCOR is the causative gene for OFCD syndrome" ([PMID: 15770227](https://pubmed.ncbi.nlm.nih.gov/15770227/))

**Genetic risk factors.** The only established risk factor is possession of a pathogenic *BCOR* null allele. Nearly all reported OFCD variants create premature termination codons subject to NMD. There are no known common susceptibility loci or polygenic contributions; this is a fully penetrant Mendelian condition rather than a complex trait.

**Environmental / infectious risk factors.** **None identified.** No toxins, teratogens, lifestyle factors, or infectious agents are implicated in OFCD causation. As a germline single-gene disorder, environmental modifiers are not established.

**Protective factors.** None known at the genetic or environmental level. The principal biological "modifier" of severity is **X-inactivation mosaicism** in heterozygous females — skewed inactivation favoring the wild-type allele can yield mild or nearly asymptomatic carriers ([PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Gene–environment interactions.** Not applicable/established; OFCD is driven by intrinsic developmental gene dosage rather than gene–environment interplay.

---

## 3. Phenotypes

OFCD phenotypes are congenital physical malformations and structural anomalies. The four cardinal domains and representative HPO terms:

| Domain | Features | Frequency | Suggested HPO |
|---|---|---|---|
| **Ocular** | Congenital cataract (near-universal), microphthalmia, microcornea, secondary/congenital glaucoma, persistent fetal vasculature, foveal photoreceptor atrophy | Cataract ~universal; others variable | HP:0000518 (Cataract), HP:0000568 (Microphthalmia), HP:0000501 (Glaucoma), HP:0000482 (Microcornea) |
| **Facial** | Long narrow face, high nasal bridge, broad/pointed/bifid nose, cleft palate/submucous cleft, ear anomalies | Common, variable | HP:0000278 (Long face), HP:0000426 (Prominent nasal bridge), HP:0000175 (Cleft palate), HP:0000453 (Bifid nose) |
| **Cardiac** | Atrial septal defect, ventricular septal defect, mitral valve anomalies/regurgitation, patent ductus arteriosus, laterality defects/dextrocardia | Common | HP:0001631 (ASD), HP:0001629 (VSD), HP:0001633 (Abnormal mitral valve), HP:0001651 (Dextrocardia) |
| **Dental** | **Radiculomegaly of canines (pathognomonic)**, oligodontia/tooth agenesis, delayed eruption, persistent deciduous teeth, malocclusion (Class III), open apices | Radiculomegaly frequent in permanent dentition | HP:0000705 (Abnormal dental root morphology), HP:0000670 (Oligodontia), HP:0006335 (Delayed eruption of teeth) |

**Radiculomegaly characteristics.** This is the defining sign. Affected canine roots reach extreme lengths — e.g., a mandibular canine of 47.5 mm ([PMID: 20825507](https://pubmed.ncbi.nlm.nih.gov/20825507/)) and 38.0 mm calculated at **+14.8 SD** above normal ([PMID: 30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/)). Novel radiographic features include calcified dental papillae beneath open apices and pulp-stone-like calcifications; radiculomegaly develops progressively over years and is confirmed on orthopantomogram/CBCT ([PMID: 30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/)). In one Czech series, radiculomegaly occurred in 3/5 patients with permanent teeth, with additional agenesis, cleft lip/palate, and Class III malocclusion ([PMID: 39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/)).

**Expanded phenotype.** Ragge et al. (2019) broadened OFCD to include neuropathy, muscle hypotonia, pituitary underdevelopment, brain atrophy, lipoma, and the first description of childhood lymphoma ([PMID: 29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/)):

> "broaden the phenotypic description for OFCD to include neuropathy, muscle hypotonia, pituitary underdevelopment, brain atrophy, lipoma and the first description of childhood lymphoma in an OFCD case"

Skeletal features include 2nd–3rd toe syndactyly and radioulnar synostosis ([PMID: 22301464](https://pubmed.ncbi.nlm.nih.gov/22301464/); [PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Onset, severity, progression.** Onset is **congenital**. Severity is **variable** (X-inactivation-dependent in females), ranging from mild/underdiagnosed to multi-system. Structural malformations are **stable** post-development, but radiculomegaly is **progressive** through dental maturation, and glaucoma may progress.

**Quality-of-life impact.** Substantial: potential blindness from cataract/glaucoma, cardiac morbidity, chronic complex dental/orthodontic needs, facial dysmorphism with psychosocial impact, and variable neurodevelopmental involvement. Formal EQ-5D/SF-36 data are not available for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***BCOR*** (BCL6 corepressor), Xp11.4, OMIM *300485. Sole cause of OFCD ([PMID: 15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/); [PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Variant types.** Predominantly **truncating/null**: frameshift, nonsense, and deletion variants creating premature termination codons. Reported examples include c.2382del p.(Lys795Argfs\*12) and c.3914dup p.(Gln1306Alafs\*20) ([PMID: 39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/)); c.888delG p.(Asn297Ilefs\*80) ([PMID: 22301464](https://pubmed.ncbi.nlm.nih.gov/22301464/)); c.3668delC ([PMID: 38244688](https://pubmed.ncbi.nlm.nih.gov/38244688/)); c.265G>A ([PMID: 30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/)); intron-11 deletions ([PMID: 38178193](https://pubmed.ncbi.nlm.nih.gov/38178193/)). Most are **de novo** or **transmitted from affected mothers**.

**Variant classification.** Reported pathogenic OFCD variants are classified **pathogenic/likely pathogenic** per ACMG/AMP, largely by loss-of-function mechanism (PVS1) plus segregation/de novo criteria.

**Allele frequency.** OFCD-causing variants are private/absent from population databases (gnomAD); *BCOR* loss-of-function is strongly constrained.

**Somatic vs germline.** OFCD is **germline**. Notably, **somatic** *BCOR*/*BCORL1* inactivating mutations occur in acute myeloid leukemia, myelodysplastic syndrome, and various sarcomas ([PMID: 24515802](https://pubmed.ncbi.nlm.nih.gov/24515802/)) — a mechanistic bridge to the emerging tumor-predisposition dimension in germline cases:

> "inactivating somatic BCOR and BCORL1 mutations in patients with acute myeloid leukemia (AML), myelodysplastic syndrome (MDS)"

**Functional consequence.** **Loss of function**, largely mediated by **NMD** of PTC-containing transcripts. Critically, both the OFCD-mutant truncated form and the Lenz p.P85L form retain the ability to interact with BCL6 and repress transcription, implicating **defects in alternative BCOR functions** rather than simple loss of BCL6 corepression ([PMID: 15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/)):

> "BCOR P85L and an OFCD-mutant form of BCOR can interact with BCL-6 and efficiently repress transcription"

**Genotype–phenotype dosage rule (Finding F007).** Null alleles → **female OFCD** (male-lethal); hypomorphic missense **p.Pro85Leu → male Lenz microphthalmia** ([PMID: 29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/)):

> "OFCD is an X-linked dominant syndrome caused by a variety of BCOR null mutations" … "is caused by hypomorphic BCOR variants, mainly by a specific missense variant c.254C > T, p.(Pro85Leu)"

**Modifier genes.** No classical modifier genes established. **X-inactivation skewing** is the dominant modifier of expressivity in females. A reported case with co-occurring *BCOR* and *MYLK* variants (multilocus pathogenic variation) altered surgical/cardiovascular risk stratification ([PMID: 41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/)).

**Epigenetic information.** *BCOR* itself acts through chromatin: loss increases activating H3K4/H3K36 methylation and reduces repressive H2A ubiquitylation at target loci (see Section 6). Disease-specific DNA methylation signatures are not established.

**Chromosomal abnormalities.** OFCD is typically a point/small-indel disorder, but genomic rearrangements at Xp have been reported alongside *BCOR* variants, including microduplications at Xp22.2-22.13 (involving *NHS*) and Xp21.3 ([PMID: 22301464](https://pubmed.ncbi.nlm.nih.gov/22301464/)).

---

## 5. Environmental Information

**Not applicable.** OFCD is a germline monogenic disorder. No environmental toxins, radiation, pollution, occupational exposures, lifestyle/behavioral factors, or infectious agents are known to cause or trigger it. This section is included for completeness and to signal a genuine negative.

---

## 6. Mechanism / Pathophysiology

OFCD pathophysiology centers on loss of BCOR, a **PRC1.1** subunit, producing tissue-specific transcriptional derepression via two principal causal chains.

### BCOR and PRC1.1 (Finding F004)

BCOR nucleates the non-canonical Polycomb complex **PRC1.1**, comprising **RING1B/RNF2, PCGF1, and KDM2B**, recruited to nonmethylated CpG islands ([PMID: 24515802](https://pubmed.ncbi.nlm.nih.gov/24515802/)):

> "The BCL6 corepressor (BCOR) complex comprises ring finger protein 1B (RNF2/RING1B), polycomb group ring finger 1 (PCGF1), and lysine-specific demethylase 2B (KDM2B) and is uniquely recruited to nonmethylated CpG islands, where it removes histone H3K36me2 and induces repressive histone H2A monoubiquitylation"

Mouse work confirms BCOR/PRC1.1 developmental roles; conditional deletion recapitulates OFCD features (cleft palate/mandibular hypoplasia via neural crest; syndactyly via lateral mesoderm) ([PMID: 32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/)):

> "BCOR associates with Polycomb group proteins to form one subfamily of the diverse Polycomb repressive complex 1 (PRC1) complexes, designated PRC1.1"

**GO terms:** GO:0031519 (PcG protein complex), GO:0006355 (regulation of transcription, DNA-templated), GO:0016575 (histone deacetylation), GO:0035518 (histone H2A monoubiquitination), GO:0000122 (negative regulation of transcription by RNA Pol II).

### Causal chain 1 — Dental radiculomegaly via AP-2α derepression (Finding F003)

Fan et al. (2009, *Nat Cell Biol*) showed OFCD-patient mesenchymal stem cells (MSCs) with *BCOR* mutation have increased osteo-/dentinogenic potential. **AP-2α (TFAP2A)** is a repressive BCOR target abnormally activated on *BCOR* loss ([PMID: 19578371](https://pubmed.ncbi.nlm.nih.gov/19578371/)):

> "AP-2alpha was identified as a repressive target of BCOR, and BCOR mutation resulted in abnormal activation of AP-2alpha"
> "BCOR mutation increased histone H3K4 and H3K36 methylation in MSCs, thereby reactivating transcription of silenced target genes"

NMD adds a regulatory layer: UPF1 binds PTC-containing *BCOR* transcripts; UPF1 knockdown upregulates *BCOR*, and mutant *BCOR* alters **BMP2** in periodontal ligament cells ([PMID: 38244688](https://pubmed.ncbi.nlm.nih.gov/38244688/)).

**Causal chain:** *BCOR* null → NMD/loss of PRC1.1 repression → ↑H3K4/H3K36me + ↓H2Aub at MSC targets → derepression of AP-2α (and altered BMP2) → enhanced osteo-/dentinogenesis → **canine radiculomegaly**.

### Causal chain 2 — Cardiac/laterality defects via Notch–Pitx2 (Finding F006)

The **BCL6–BCOR complex normally restrains Notch signaling**. Sakano et al. (2010, *Genes Dev*) showed BCL6 forms a complex with BCOR on Notch-target promoters (e.g., *ESR1/*Enhancer of split related 1) and competes with the Notch1 intracellular domain, excluding coactivator Mastermind-like1 ([PMID: 20230751](https://pubmed.ncbi.nlm.nih.gov/20230751/)):

> "BCL6 forms a complex with BCL6 corepressor (BCoR) on the promoters of selected Notch target genes such as enhancer of split related 1. BCL6 also inhibits the transcription of these genes by competing for the Notch1 intracellular domain, preventing the coactivator Mastermind-like1 (MAM1) from binding"

Tanaka et al. (2014) linked this to laterality: ESR1 (downstream of Notch) represses *Pitx2* by binding the left-side ASE enhancer and recruiting HDAC1, blocking p300 ([PMID: 24440151](https://pubmed.ncbi.nlm.nih.gov/24440151/)):

> "uncontrolled Notch activity in the left LPM caused by dysfunction of BCOR may result in cardiac/laterality defects of OFCD syndrome"

**Causal chain:** *BCOR* null → BCL6–BCOR fails to restrain Notch in left lateral plate mesoderm → uncontrolled Notch/ESR1–HDAC1 activity → **silencing of *Pitx2*** → disrupted left–right patterning → **septal defects, valve anomalies, dextrocardia/laterality defects**. Consistent with the human male case showing dextrocardia ([PMID: 26196063](https://pubmed.ncbi.nlm.nih.gov/26196063/)).

### Upstream vs downstream summary

```
        BCOR NULL (germline, X-linked)
                 │  loss of PRC1.1 repression / NMD of PTC transcripts
     ┌───────────┴─────────────────────────────┐
 Dental MSCs                              Left lateral plate mesoderm
     │ derepress AP-2α (↑H3K4/H3K36me)         │ BCL6–BCOR fails to restrain Notch
     │ altered BMP2                            │ ↑Notch → ESR1/HDAC1 → ↓Pitx2
     ▼                                         ▼
 RADICULOMEGALY                       CARDIAC / LATERALITY DEFECTS
 (osteo-/dentinogenesis↑)             (septal defects, dextrocardia)
```

**Neoplasia dimension.** BCOR's tumor-suppressor role (somatic inactivation in AML/MDS/sarcomas; [PMID: 24515802](https://pubmed.ncbi.nlm.nih.gov/24515802/)) plausibly underlies germline OFCD tumor reports — childhood lymphoma ([PMID: 29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/)) and metachronous multiple insulinomas ([PMID: 42324136](https://pubmed.ncbi.nlm.nih.gov/42324136/)).

**Cell types (CL) / compartments (GO CC):** mesenchymal stem cell (CL:0000134), periodontal ligament fibroblast, odontoblast (CL:0000060), neural crest cell (CL:0000333); nucleus/chromatin (GO:0005634 nucleus, GO:0000785 chromatin). **CHEBI:** BMP2 (protein), estrogen/ESR1 signaling.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** eye/lens (UBERON:0000019 eye; UBERON:0000965 lens), heart (UBERON:0000948), teeth/canine (UBERON:0001091 tooth), craniofacial skeleton (UBERON:0010363). **Secondary/other:** brain (UBERON:0000955), pituitary (UBERON:0000007), skeleton (hand/foot — syndactyly, radioulnar synostosis), pancreas (endocrine, insulinoma).

**Body systems:** visual, cardiovascular, craniofacial/skeletal, dental/stomatognathic, nervous, endocrine.

**Tissue/cell level:** dental mesenchymal stem cells and periodontal ligament (radiculomegaly); neural crest-derived craniofacial mesenchyme (cleft palate, mandibular hypoplasia); lateral plate mesoderm (cardiac/laterality, syndactyly); lens epithelium (cataract). CL terms as in Section 6.

**Subcellular:** nucleus/chromatin (site of PRC1.1 action, GO:0005634).

**Localization / lateralization:** Ocular and dental findings are typically **bilateral**; cardiac laterality defects are intrinsically **asymmetric** (dextrocardia, situs abnormalities).

---

## 8. Temporal Development

- **Onset:** Congenital; ocular (cataract) and cardiac malformations present at/near birth. Dental radiculomegaly manifests and progresses through childhood/adolescence as the permanent dentition develops.
- **Onset pattern:** Chronic/developmental (structural malformations arise in utero).
- **Progression:** Structural malformations are stable after development; **radiculomegaly is progressive** over years ([PMID: 30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/), 30-year longitudinal follow-up); glaucoma may be progressive and vision-threatening.
- **Course:** Chronic, lifelong; not episodic or relapsing–remitting.
- **Critical periods:** Embryonic organogenesis (eye, heart, left–right patterning) is the window of vulnerability; postnatal windows matter for cataract/glaucoma surgery timing and orthodontic intervention before radiculomegaly completion.

---

## 9. Inheritance and Population

**Inheritance.** X-linked dominant with presumed **male lethality** ([PMID: 15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/)):

> "Oculofaciocardiodental syndrome (OFCD; OMIM 300166) is inherited in an X-linked dominant pattern with presumed male lethality"

Mouse models confirm male lethality — *Bcor* hemizygous null males die by ~E9.5, while heterozygous mosaic females show OFCD-like defects ([PMID: 32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/)):

> "Bcor hemizygosity in the entire male embryo resulted in embryonic lethality by E9.5"

**Penetrance/expressivity.** High penetrance in females but **highly variable expressivity**, governed by X-inactivation. Mosaic/skewed females may be mild or asymptomatic ([PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Mosaicism.** Somatic/germline mosaic *BCOR* mutations documented in females, including asymptomatic carriers ([PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Rare males.** Males with *BCOR* variants are exceptional (e.g., missense p.R540Q with dextrocardia; [PMID: 26196063](https://pubmed.ncbi.nlm.nih.gov/26196063/)); hypomorphic p.P85L males present as Lenz microphthalmia rather than OFCD.

**Epidemiology.** Ultra-rare; prevalence not precisely established (Orphanet: <1/1,000,000). Historically ~20–40 reported cases, expanding with molecular testing ([PMID: 19093058](https://pubmed.ncbi.nlm.nih.gov/19093058/); [PMID: 22449596](https://pubmed.ncbi.nlm.nih.gov/22449596/)). No founder effects, consanguinity role (dominant), or ethnic predilection established; cases reported worldwide (Korea, Vietnam, Czech Republic, Japan, etc.).

**Sex ratio.** Overwhelmingly **female** due to male lethality.

---

## 10. Diagnostics

**Clinical/radiographic.** Diagnosis is often triggered by **canine radiculomegaly** on orthopantomogram/CBCT — pathognomonic and detectable by dentists ([PMID: 30484210](https://pubmed.ncbi.nlm.nih.gov/30484210/); [PMID: 30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/)). Ophthalmologic exam (cataract, microphthalmia, glaucoma, and posterior-segment findings such as persistent fetal vasculature and foveal photoreceptor atrophy on multimodal imaging; [PMID: 38699441](https://pubmed.ncbi.nlm.nih.gov/38699441/)) and echocardiography (septal defects, valve anomalies, laterality) complete the workup.

**Genetic testing (confirmatory).** **Single-gene *BCOR* sequencing** or **exome/trio exome sequencing** is the diagnostic standard, validated by Sanger sequencing and segregation analysis ([PMID: 39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/); [PMID: 41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/)). **Chromosomal microarray/CNV analysis** detects deletions/duplications and associated Xp rearrangements ([PMID: 22301464](https://pubmed.ncbi.nlm.nih.gov/22301464/)). WES/WGS also enables detection of multilocus pathogenic variation (e.g., co-occurring *MYLK*) with clinical consequences ([PMID: 41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/)).

**Diagnostic criteria.** Core triad emphasized: **congenital cataract, microphthalmia, and radiculomegaly**, plus examination for skeletal defects (radioulnar synostosis) and cardiac/laterality defects ([PMID: 19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/)).

**Differential diagnosis.** Lenz microphthalmia syndrome (allelic; male, hypomorphic *BCOR*); Nance-Horan syndrome (*NHS*, overlapping ocular/dental features); other syndromic microphthalmia (SOX2, OTX2, STRA6, BMP4, HCCS, SMOC1) ([PMID: 22005280](https://pubmed.ncbi.nlm.nih.gov/22005280/)).

**Screening.** Any patient with **congenital cataract plus dental abnormalities (radiculomegaly)** — even without family history — should be referred for genetic testing ([PMID: 39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/)). Cascade testing in families; prenatal/preimplantation testing feasible once a familial variant is known.

---

## 11. Outcome / Prognosis

**Survival.** In affected females, life expectancy is generally near-normal, dominated by cardiac severity and surgical complications; hemizygous males are typically not viable (embryonic lethality). No formal survival statistics exist for this ultra-rare condition.

**Morbidity / function.** Chief morbidities: **visual impairment/blindness** (cataract, glaucoma, posterior-segment atrophy), **cardiac disease** (septal/valvular/laterality), lifelong **dental/orthodontic** burden, facial dysmorphism, and variable neurodevelopmental involvement (hypotonia, neuropathy, brain/pituitary abnormalities; [PMID: 29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/)).

**Complications.** Dental abscess from radiculomegalous teeth ([PMID: 38178193](https://pubmed.ncbi.nlm.nih.gov/38178193/)); glaucoma; cardiac sequelae; emerging **tumor risk** — childhood lymphoma ([PMID: 29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/)) and metachronous insulinomas requiring repeated surgery ([PMID: 42324136](https://pubmed.ncbi.nlm.nih.gov/42324136/)).

**Prognostic factors.** Degree of X-inactivation skewing (expressivity), cardiac defect severity, glaucoma control, and presence of additional pathogenic variants (MPV) that raise surgical risk ([PMID: 41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/)). No validated molecular prognostic biomarkers.

---

## 12. Treatment

**No disease-modifying/curative therapy exists.** Management is **symptomatic, organ-directed, and multidisciplinary**.

| Domain | Interventions | NCIT suggestion |
|---|---|---|
| Ocular | Cataract extraction / lensectomy with anterior vitrectomy & posterior capsulotomy; glaucoma surgery; visual rehabilitation | NCIT:C15277 (Ophthalmologic surgery) |
| Cardiac | Surgical/interventional repair of septal defects and valve anomalies; PDA closure | NCIT:C157769 (Cardiac surgery) |
| Dental | Endodontic (root canal) management of radiculomegalous teeth; extractions; surgical-orthodontic treatment with light forces to avoid ankylosis | NCIT:C15855 (Orthodontics); NCIT:C15329 (Endodontic therapy) |
| Craniofacial | Cleft palate repair; orthognathic surgery for Class III malocclusion | NCIT:C51823 (Orthognathic surgery) |
| Oncologic | Surgical resection of insulinomas; surveillance/treatment of lymphoma | NCIT:C15329 |
| Genetic | Genetic counseling for X-linked reproductive risk | NCIT:C15417 (Genetic counseling) |

Endodontic treatment of radiculomegalous canines is technically challenging (extreme root length, multiple canals) ([PMID: 20825507](https://pubmed.ncbi.nlm.nih.gov/20825507/)). Surgical-orthodontic therapy can effectively correct skeletal disharmony and improve occlusion/function ([PMID: 22449596](https://pubmed.ncbi.nlm.nih.gov/22449596/)). Perioperative planning must integrate cardiac risk, and evolving genomic findings (e.g., *MYLK*) may alter surgical decision-making ([PMID: 41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/)).

**Pharmacogenomics / advanced therapeutics (gene, cell, RNA-based, targeted, immuno).** None established or approved for OFCD. No experimental clinical trials with NCT identifiers are documented for this condition.

---

## 13. Prevention

- **Primary prevention:** Not applicable (germline congenital disorder); no vaccination or risk-factor modification.
- **Secondary prevention / early detection:** High index of suspicion in any child with **congenital cataract + radiculomegaly/dental anomalies** → early referral for genetic testing and specialized dental care ([PMID: 39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/)). Early ophthalmologic and cardiac evaluation improves outcomes.
- **Tertiary prevention:** Timely cataract/glaucoma surgery to preserve vision; cardiac repair; ongoing dental surveillance; **tumor surveillance** given emerging lymphoma/insulinoma associations ([PMID: 42324136](https://pubmed.ncbi.nlm.nih.gov/42324136/)).
- **Genetic counseling:** Central to prevention — X-linked dominant with male lethality; discuss recurrence risk, prenatal/preimplantation testing, and cascade testing of at-risk female relatives.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *BCOR* is conserved; mouse *Bcor* (NCBI Gene 71458) and *Xenopus* *bcor* are the key experimental orthologs.
- **Model organism disease:** Mouse *Bcor* null recapitulates key OFCD/PRC1.1 developmental defects with male lethality ([PMID: 32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/)); *Xenopus* studies established the laterality/Notch–Pitx2 role ([PMID: 20230751](https://pubmed.ncbi.nlm.nih.gov/20230751/); [PMID: 24440151](https://pubmed.ncbi.nlm.nih.gov/24440151/)).
- **Natural veterinary disease:** No naturally occurring OFCD-equivalent syndrome is documented in companion animals or wildlife (OMIA); this is a genuine gap.
- **Evolutionary conservation:** BCOR/PRC1.1 chromatin functions and left–right patterning via Notch–Pitx2 are deeply conserved across vertebrates, supporting cross-species mechanistic translation.
- **Zoonotic potential:** Not applicable.

---

## 15. Model Organisms

| Model | Type | Contribution / phenotype recapitulation |
|---|---|---|
| **Mouse (*Bcor*)** | Mammalian; conditional/tissue-specific knockout alleles | Male embryonic lethality by ~E9.5; heterozygous mosaic females show OFCD-like defects. Tissue-specific deletion recapitulates cleft palate/mandibular hypoplasia (neural crest) and syndactyly (lateral mesoderm), defining PRC1.1 developmental roles ([PMID: 32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/)) |
| **Xenopus** | Vertebrate embryo | Established BCOR requirement for left–right patterning; BCL6–BCOR restrains Notch to maintain Pitx2 in left LPM ([PMID: 20230751](https://pubmed.ncbi.nlm.nih.gov/20230751/); [PMID: 24440151](https://pubmed.ncbi.nlm.nih.gov/24440151/)) |
| **Human patient MSCs / periodontal ligament cells** | In vitro / primary cells | Direct mechanistic dissection of radiculomegaly: AP-2α derepression, H3K4/H3K36 methylation increases, UPF1/NMD–BMP2 axis ([PMID: 19578371](https://pubmed.ncbi.nlm.nih.gov/19578371/); [PMID: 38244688](https://pubmed.ncbi.nlm.nih.gov/38244688/)) |

**Model limitations.** Complete male knockouts are embryonic-lethal, requiring conditional/mosaic strategies; no single model reproduces the full human ocular–facial–cardiac–dental tetrad simultaneously. Radiculomegaly (a human dental-specific phenotype) is best studied in patient-derived cells rather than rodent teeth.

**Resources:** MGI (mouse *Bcor*), Xenbase, Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

OFCD is fundamentally a **chromatin/Polycomb dosage disorder**. A single functional dose of BCOR is required for normal development; its loss removes PRC1.1-mediated repression at CpG-island targets in specific progenitor populations, unleashing tissue-specific transcriptional programs. Two mechanistically independent but conceptually unified derepression events explain the two most distinctive features:

1. **AP-2α derepression in dental MSCs → radiculomegaly** (enhanced osteo-/dentinogenesis; modulated by NMD/UPF1 and BMP2).
2. **Notch de-restraint in left LPM → ESR1/HDAC1 silencing of Pitx2 → cardiac/laterality defects.**

The **dosage/allele-class rule** unifies OFCD and Lenz microphthalmia into one BCOR spectrum: **null alleles → female OFCD (male-lethal)**; **hypomorphic p.P85L → male Lenz**. Because both allele classes retain BCL6 binding and repression, the pathogenic defect lies in **alternative, dose-sensitive BCOR/PRC1.1 functions**. Finally, BCOR's somatic tumor-suppressor role rationalizes the emerging neoplasia dimension (lymphoma, insulinoma) in germline patients.

---

## Evidence Base

| PMID | Title (abbrev.) | Support |
|---|---|---|
| [15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/) | OFCD and Lenz result from distinct BCOR mutation classes | Null → OFCD; P85L → Lenz; both retain BCL6 repression; X-linked male lethality |
| [15770227](https://pubmed.ncbi.nlm.nih.gov/15770227/) | Novel BCOR mutations in OFCD | Confirms BCOR as sole cause |
| [19367324](https://pubmed.ncbi.nlm.nih.gov/19367324/) | BCOR analysis across OFCD/Lenz/laterality | Female OFCD null cohort; mosaicism; diagnostic criteria |
| [19578371](https://pubmed.ncbi.nlm.nih.gov/19578371/) | BCOR regulates MSC function epigenetically | Radiculomegaly mechanism: AP-2α, H3K4/H3K36me |
| [38244688](https://pubmed.ncbi.nlm.nih.gov/38244688/) | NMD/UPF1 in OFCD root formation | UPF1–BCOR–BMP2 axis in radiculomegaly |
| [24515802](https://pubmed.ncbi.nlm.nih.gov/24515802/) | Polycomb disruption in cancers | PRC1.1 composition; somatic BCOR in AML/MDS |
| [32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/) | Conditional Bcor PRC1.1 mouse | Male lethality E9.5; OFCD-like tissue defects |
| [20230751](https://pubmed.ncbi.nlm.nih.gov/20230751/) | BCL6 canalizes Notch transcription | BCL6–BCOR restrains Notch (Xenopus LR patterning) |
| [24440151](https://pubmed.ncbi.nlm.nih.gov/24440151/) | Molecular pathogenesis of cardiac/laterality defects | Notch→ESR1/HDAC1→Pitx2 chain |
| [29974297](https://pubmed.ncbi.nlm.nih.gov/29974297/) | Expanding BCOR microphthalmia phenotype | Neuro/pituitary/lymphoma expansion; null vs P85L rule |
| [26196063](https://pubmed.ncbi.nlm.nih.gov/26196063/) | Male BCOR case with dextrocardia | Human laterality confirmation |
| [42324136](https://pubmed.ncbi.nlm.nih.gov/42324136/) | Metachronous insulinomas in OFCD | Tumor predisposition dimension |
| [41236190](https://pubmed.ncbi.nlm.nih.gov/41236190/) | Compound BCOR + MYLK burden | Surgical risk stratification / MPV |
| [39438869](https://pubmed.ncbi.nlm.nih.gov/39438869/) | Czech OFCD families dental phenotype | Radiculomegaly 3/5; novel frameshift variants |
| [30544426](https://pubmed.ncbi.nlm.nih.gov/30544426/) | Radiological findings & radiculomegaly | +14.8 SD root length; 30-yr follow-up |
| [20825507](https://pubmed.ncbi.nlm.nih.gov/20825507/) | Endodontic treatment of radiculomegaly | 47.5 mm root; treatment challenge |

---

## Limitations and Knowledge Gaps

1. **Epidemiology:** No reliable prevalence/incidence estimates; case-report-driven knowledge with ascertainment bias.
2. **Quality-of-life:** No formal EQ-5D/SF-36/PROMIS data.
3. **Tumor risk:** The neoplasia association (lymphoma, insulinoma) is based on single/few cases; magnitude of risk and surveillance guidelines are undefined.
4. **Genotype–phenotype:** Beyond the null-vs-P85L rule, fine correlations (variant position, X-inactivation quantification) remain incompletely mapped.
5. **Therapeutics:** No disease-modifying therapy, no clinical trials; the reversibility of chromatin derepression is untested clinically.
6. **Animal models:** No naturally occurring veterinary counterpart; no model reproduces the full human tetrad.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international OFCD registry** to define prevalence, natural history, and tumor incidence with standardized QoL instruments.
2. **Quantitative X-inactivation studies** correlating skewing with expressivity to enable prognostic counseling.
3. **Tumor-surveillance protocol development** given emerging lymphoma/insulinoma reports — assess whether periodic endocrine/hematologic screening is warranted.
4. **Patient-derived iPSC/organoid models** (dental, cardiac, retinal) to test whether pharmacologic modulation of Notch, HDAC (e.g., HDAC inhibitors), or NMD can rescue OFCD-relevant transcriptional programs.
5. **Chromatin profiling (CUT&RUN/ChIP-seq for H2Aub, H3K4/H3K36me) in patient cells** to build a tissue-specific derepression map and identify additional therapeutic targets.
6. **Systematic ACMG-based reclassification** of all reported *BCOR* variants and functional assays for rare missense variants to sharpen genotype–phenotype boundaries between OFCD and Lenz.

---

*Report compiled from 7 confirmed findings and 26 reviewed publications. Evidence source types: predominantly human clinical case reports/series, mouse and Xenopus model organism studies, and in vitro patient-cell mechanistic work.*


## Artifacts

- [OpenScientist final report](Oculofaciocardiodental_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Oculofaciocardiodental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)