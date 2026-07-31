---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T02:11:56.028350'
end_time: '2026-07-31T02:57:36.910020'
duration_seconds: 2740.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SHH Holoprosencephaly Spectrum
  mondo_id: ''
  category: Genetic
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
  path: SHH_Holoprosencephaly_Spectrum-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SHH_Holoprosencephaly_Spectrum-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SHH Holoprosencephaly Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SHH Holoprosencephaly Spectrum** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# SHH Holoprosencephaly Spectrum — Comprehensive Disease Characterization Report

**Disease:** SHH Holoprosencephaly Spectrum (HPE3)
**Category:** Genetic (autosomal dominant, developmental)
**Key identifiers:** OMIM #142945 (HPE3); *SHH* gene OMIM \*600725; MONDO:0016296; ORPHA:2162; ICD-10 Q04.2; ICD-11 LA05.0; MeSH D016142; HGNC:10848 (SHH); UniProt Q15465; Ensembl ENSG00000164690

*Evidence source labels: [H] human clinical/registry, [M] model organism, [V] in vitro, [C] computational/structural. PMIDs cited inline.*

---

## Summary

**SHH holoprosencephaly (HPE3) is the most common single-gene, non-chromosomal cause of holoprosencephaly (HPE) — the failure of the embryonic forebrain (prosencephalon) to cleave into two cerebral hemispheres between the 18th and 28th day of gestation.** It is an autosomal-dominant disorder caused by heterozygous loss-of-function of *Sonic Hedgehog (SHH)*, which lowers SHH morphogen signaling in the rostroventral forebrain during a narrow developmental window. The consequence is a graded midline brain–face malformation continuum, spanning cyclopia and alobar HPE at the severe end through semilobar, lobar, and the middle interhemispheric variant, down to isolated "microforms" (solitary median maxillary central incisor [SMMCI], ocular hypotelorism) at the mild end. *SHH* is the first-identified and most frequently mutated of at least seven implicated HPE genes (*SHH, ZIC2, SIX3, TGIF, PTCH1, GLI2, TDGF1*) and underlies ~17% of familial HPE.

A defining feature is **extreme variability**: markedly incomplete penetrance and highly variable expressivity mean a single variant can produce lethal brain malformation in one relative and only a subtle facial sign — or nothing detectable — in another. Critically, in the largest genotype–phenotype cohort (396 individuals), *SHH* variants biased toward the *milder* end, more often causing non-HPE (64%) than frank HPE (36%), and mutation-positive microform carriers may have normal or even above-average intellect. This variability reflects a "multiple-hit" genetic architecture (co-occurring variants in modifiers such as *GAS1*, and pathways including NODAL, NOTCH, WNT/PCP, FGF, RAS/ERK, cilia, and cohesin) combined with gene–environment interaction, most prominently maternal pregestational diabetes, with additional signals from alcohol, female sex, and twinning.

**Clinically, HPE carries among the lowest survival of all rare structural congenital anomalies (~36% at 10 years; alobar HPE is usually lethal neonatally).** No curative or disease-modifying therapy exists; care is supportive and centers on prenatal imaging diagnosis, genetic counseling with molecular cascade testing, and management of the characteristic complications — seizures, autonomic instability, and hypothalamic–pituitary endocrinopathy, of which central diabetes insipidus (~47% of HPE patients) is the hallmark. Causation is definitively established by the landmark *Shh*-null mouse (cyclopia, loss of the ventral neural tube), and human *SHH* variants have been functionally validated in zebrafish rescue assays.

---

## Key Findings

### Finding 1 — SHH is the leading single-gene cause of HPE, acting via haploinsufficiency of Sonic Hedgehog signaling

Holoprosencephaly results from incomplete cleavage of the prosencephalon between the 18th and 28th days of gestation. At least seven genes are positively implicated, of which *SHH* was the first identified and is the most frequently mutated ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/): *"To date, seven genes have been positively implicated in HPE: Sonic hedgehog (SHH), ZIC2, SIX3, TGIF, PTCH, GLI2 and TDGF1."*). The convergent mechanism across these diverse genes is disruption of Hedgehog signaling — *"disruption of Sonic hedgehog expression and/or signaling in the rostroventral region of the embryo is a major common effect of these mutations"* ([PMID: 19186244](https://pubmed.ncbi.nlm.nih.gov/19186244/)). Inheritance is autosomal dominant with markedly incomplete penetrance and variable expressivity: *"even HPE in pedigrees is characterized by incomplete penetrance and variable expressivity"* ([PMID: 19186244](https://pubmed.ncbi.nlm.nih.gov/19186244/)). The molecular basis is haploinsufficiency — loss of one functional *SHH* allele lowers morphogen output below the threshold required for normal midline forebrain patterning. [H/M]

### Finding 2 — HPE forms a graded clinical spectrum with correlated brain–face severity

HPE is classically divided into three ranges of increasing severity — **lobar, semilobar, and alobar** — plus the milder **middle interhemispheric variant (MIHV/syntelencephaly)** ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/): *"Three ranges of increasing severity are described: lobar, semi-lobar and alobar HPE."*). Facial anomalies parallel brain severity along the "face predicts the brain" principle: severe forms show *"cyclopia, proboscis, median or bilateral cleft lip/palate,"* while minor forms show *"ocular hypotelorism or solitary median maxillary central incisor"*, and microforms can occur with a structurally normal brain ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/)). A nationwide Japanese survey (n=49 anatomically typed) found: **40.8% alobar, 40.8% semilobar, 10.4% lobar** ([PMID: 31886593](https://pubmed.ncbi.nlm.nih.gov/31886593/): *"20 were alobar (40.8%), 20 were semilobar (40.8%), five were lobar (10.4%)"*). [H]

### Finding 3 — HPE has the lowest survival among rare structural congenital anomalies

Birth prevalence is ~1/16,000 live births but ~1/250 conceptuses, indicating that the great majority of affected pregnancies are lost in utero ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/): *"It is estimated to occur in 1/16,000 live births and 1/250 conceptuses."*); Japan's birth-prevalence rate was 1.54/10,000 live births ([PMID: 31886593](https://pubmed.ncbi.nlm.nih.gov/31886593/)). Two independent registries confirm HPE has the worst survival of the conditions studied:

| Registry / Study | Survival metric | Value | Source |
|---|---|---|---|
| EUROCAT multi-registry (rare CAs) | 1 week | 58.1% (95% CI 44.3–76.2) | [PMID: 35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/) |
| EUROCAT | 1 year | 47.4% (95% CI 36.4–61.6) | [PMID: 35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/) |
| EUROCAT | 10 years | 35.6% (95% CI 22.2–56.9) | [PMID: 35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/) |
| Texas registry (1999–2018) | 10 years | 36.9% (lowest of 30 conditions) | [PMID: 37868647](https://pubmed.ncbi.nlm.nih.gov/37868647/) |

*"Arhinencephaly/holoprosencephaly had the lowest survival at all ages"* ([PMID: 35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/)); *"Ten-year survival varied by condition, ranging from 36.9% for holoprosencephaly to 99.3% for pyloric stenosis"* ([PMID: 37868647](https://pubmed.ncbi.nlm.nih.gov/37868647/)). Prognosis is strongly severity-dependent; alobar HPE is uniformly unfavorable neonatally. [H]

### Finding 4 — Penetrance/expressivity are shaped by "multiple-hit" genetics and gene–environment interaction

Clinical expression is *"extremely variable"* and is attributed to the number and type of HPE gene variants, with environmental agents contributing and evidence for a "multiple hits" requirement — e.g., patients carrying combined *GAS1* + *SHH* variants ([PMID: 20583177](https://pubmed.ncbi.nlm.nih.gov/20583177/): *"Environmental agents may also contribute to the severity as well as the requirement of multiple hits."*). Recent reviews implicate modifiers across the **NODAL, NOTCH, WNT/PCP, FGF, and RAS/ERK1/2 pathways** plus ciliary and cohesin components ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/): *"These include modulators of the NODAL, NOTCH, WNT/PCP, FGF, and RAS/ERK1/2 pathways as well as components of ciliary structures and cohesin complexes."*), and emphasize that *"incomplete penetrance, broad phenotypic heterogeneity, and gene-environment interactions complicate diagnostic and counselling efforts"* ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)). Mechanistically, SHH signaling requires **cholesterol modification** of the ligand and a coreceptor handoff via GAS1/SCUBE2 to PTCH1 ([PMID: 35231446](https://pubmed.ncbi.nlm.nih.gov/35231446/): *"how GAS1 recognizes the SHH palmitate and cholesterol modifications in modular fashion and how it facilitates lipid-dependent SHH handoff to PTCH1"*), providing a molecular bridge between sterol-disrupting exposures and HPE risk. [H/V/C]

### Finding 5 — SHH accounts for ~17% of familial HPE; ligand lipidation is required; human variants are functionally validated

*"Mutations in SHH underlie most familial (17%) cases of HPE"* ([PMID: 23055936](https://pubmed.ncbi.nlm.nih.gov/23055936/)). The same study established that Hedgehog acyltransferase (Hhat), required for N-terminal palmitoylation of SHH, is essential: *"Hhat is required for post-translational palmitoylation of Hedgehog (Hh) proteins; and, in the absence of Hhat, Hh secretion from producing cells is diminished"* ([PMID: 23055936](https://pubmed.ncbi.nlm.nih.gov/23055936/)). Loss of Hhat in mouse produces severe acrania-holoprosencephaly-agnathia by diminishing SHH secretion and perturbing long-range signaling, with downstream disruption of FGF, BMP, and ERK and extensive apoptosis in craniofacial primordia. Because *"only a minor fraction of known SHH variants have been experimentally proven to lead to abnormal function"* ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)), human missense variants have been functionally validated by phenotypic rescue in a *shha* CRISPR/Cas9 zebrafish assay — an important tool given the abundance of variants of uncertain significance (VUS). [M/V]

### Finding 6 — Hypothalamic–pituitary dysfunction (central diabetes insipidus ~47%) and extracephalic involvement are key managed features

Endocrine dysfunction is a central management issue. In a cohort screened for *SHH*/*GLI2*, *"Diabetes insipidus was common in patients with HPE (47%) but infrequent in patients with congenital hypopituitarism or SOD (7% and 8%, respectively)"* ([PMID: 25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/)); anterior pituitary deficiency occurred in 53% of HPE patients, and a heterozygous nonsense *SHH* variant (p.Tyr175Ter) was found in an alobar HPE patient with hypopituitarism. In human (typically heterozygous) HPE, *"the pituitary gland, no matter how hypoplastic, is present in most cases of human holoprosencephaly, unlike animals in which it is always said to be absent"* ([PMID: 20013843](https://pubmed.ncbi.nlm.nih.gov/20013843/)) — a dosage difference between heterozygous human and homozygous animal models. Beyond brain and face, nonchromosomal nonsyndromic HPE shows *"a wide spectrum of extracephalic manifestations"* across organ systems ([PMID: 29761634](https://pubmed.ncbi.nlm.nih.gov/29761634/)). [H]

### Finding 7 — Mutation-positive microform HPE can present with normal or above-average intellect

A finding that reframes genetic counseling: Solomon et al. presented 5 patients with clear microform HPE signs, *all* with above-average intellect, molecular cause identified in 4/5 (*SHH, SIX3, GLI2, FGF8*) ([PMID: 23112757](https://pubmed.ncbi.nlm.nih.gov/23112757/): *"Here we present 5 patients with clear phenotypic signs of microform holoprosencephaly, all of whom have evidence of above-average intellectual function."*). This contradicts the assumption that intellectual disability marks the mildly affected carrier parent and captures the full expressivity range *"ranging from brain malformations incompatible with life to individuals with normal brain findings and subtle midline facial differences"* ([PMID: 23112757](https://pubmed.ncbi.nlm.nih.gov/23112757/)). Cognitive status therefore cannot be used to identify carriers — molecular testing of at-risk relatives is required. [H]

### Finding 8 — SHH variants skew toward the mild end; truncating variants are more severe than non-truncating

In the largest *SHH* cohort (396 individuals, 157 kindreds), *"SHH mutations more commonly resulted in non-HPE (64%) than frank HPE (36%), and non-HPE was significantly more common in patients with SHH than in those with mutations in the other common HPE related genes (p<0.0001 compared to ZIC2 or SIX3)"* ([PMID: 22791840](https://pubmed.ncbi.nlm.nih.gov/22791840/)). Within *SHH*, a genotype–severity gradient exists: *"Individuals with truncating mutations were significantly more likely to have frank HPE than those with non-truncating mutations (49% vs 35%, respectively; p=0.012)"* ([PMID: 22791840](https://pubmed.ncbi.nlm.nih.gov/22791840/)), with N-terminal clustering. A European series of 645 probands (4-gene yield 25%) confirmed positional biology: *"the most severe HPE types were associated with SIX3 and ZIC2 mutations, whereas microforms were associated with SHH mutations"* ([PMID: 21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/)); a brain–face correlation held for *SHH/SIX3/TGIF* but not *ZIC2*. Inheritance differs by gene: *"The SHH, SIX3, and TGIF mutations were inherited in more than 70% of these cases, whereas 70% of the mutations in ZIC2 occurred de novo"* ([PMID: 21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/)).

| Gene | Spectrum position | Inheritance | Brain–face correlation |
|---|---|---|---|
| **SHH** | Milder end; microforms; non-HPE 64% | >70% inherited | Yes |
| SIX3 | Severe end | >70% inherited | Yes |
| ZIC2 | Severe end | ~70% de novo | No |
| TGIF | Variable | >70% inherited | Yes |

[H]

### Finding 9 — Nongenetic risk factors: maternal pregestational diabetes, female predominance, twinning, alcohol

A systematic review identified *"maternal diabetes, twinning, and a predominance of females"* as consistently replicated nongenetic risk factors ([PMID: 29761639](https://pubmed.ncbi.nlm.nih.gov/29761639/)). A case-control study found maternal pregestational diabetes in **9.2% of cases vs 0% of controls (p=.02)**, plus elevated odds for alcohol (aOR 1.73) and aerosol/hair-spray exposure (aOR 2.46), and significant gene–environment interactions ([PMID: 33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/): *"maternal pregestational diabetes (9.2% of cases and 0 controls, p = .02)"*). A meta-analysis of >80 million births ranked HPE among the highest anomaly-specific risks with pregestational diabetes (RR ~18.18, 95% CI 4.03–82.06) ([PMID: 35104296](https://pubmed.ncbi.nlm.nih.gov/35104296/)); the National Birth Defects Prevention Study reported aOR 13.1 (95% CI 7.0–24.5) ([PMID: 31454511](https://pubmed.ncbi.nlm.nih.gov/31454511/)). In an adult HPE cohort, *"Factors associated with long-term survival included HPE subtype not alobar, female gender, and nontypical facial features"* ([PMID: 28640243](https://pubmed.ncbi.nlm.nih.gov/28640243/)). [H]

### Finding 10 — Definitive genetic proof from mouse; specific alleles produce isolated microforms

The landmark targeted *Shh* knockout established causation: *Shh* *"plays a critical role in patterning of vertebrate embryonic tissues,"* with early defects *"in the establishment or maintenance of midline structures, such as the notochord and the floorplate"* and later defects including *"absence of distal limb structures, cyclopia, absence of ventral cell types within the neural tube"* ([PMID: 8837770](https://pubmed.ncbi.nlm.nih.gov/8837770/)) — directly recapitulating human HPE. At the mild extreme, the *SHH* missense allele **I111F** segregated with **solitary median maxillary central incisor (SMMCI)** without HPE, and *"this mutation may be specific for the SMMCI phenotype since it has not been found in the HPE population or in normal controls"* ([PMID: 11471164](https://pubmed.ncbi.nlm.nih.gov/11471164/)). SMMCI can associate with pituitary insufficiency, short stature, microcephaly, and congenital nasal pyriform aperture stenosis. [M/H]

---

## Mechanistic Model / Interpretation

SHH-HPE is best understood as a **threshold disorder of morphogen dosage**. SHH is a graded morphogen that patterns the ventral midline of the developing forebrain via the prechordal plate. A single loss-of-function allele lowers total signaling; whether the phenotype crosses into frank HPE, a microform, or clinical normality depends on whether SHH output at gestational days 18–28 falls above or below the patterning threshold. That threshold is not fixed — it is modulated by variant severity, genetic background/additional hits, and environmental inputs.

```
        GENETIC              +           ENVIRONMENT
  (SHH LOF + modifiers)              (diabetes, alcohol, sterol disruption)
             \                              /
              \                            /
               ▼                          ▼
      ── Net SHH signaling at GD 18–28 (rostroventral forebrain) ──
                          │
        above threshold ──┼── below threshold
         (normal /        │        (microform → lobar → semilobar → alobar)
          carrier)        │
                          ▼
              Correlated brain + face midline phenotype
```

**Causal chain (upstream → downstream):**

```
Heterozygous SHH LOF variant
   → reduced SHH ligand production / secretion / lipidation (cholesterol + palmitate)
      → subthreshold Hedgehog signaling in rostroventral forebrain (GD 18–28)
         → failed induction/maintenance of ventral midline (floorplate, notochord)
            → incomplete cleavage of prosencephalon + apoptosis in craniofacial primordia
               → graded midline brain (alobar↔lobar↔microform) & face defects
                  → clinical: seizures, developmental delay, dysautonomia,
                    hypothalamic-pituitary dysfunction (central DI ~47%)
```

This model explains the disease's paradoxes: why *SHH* variants skew mild (ligand haploinsufficiency often leaves signaling nearer threshold than transcription-factor genes *SIX3/ZIC2*); why mutation-positive relatives can be asymptomatic or high-functioning; and why maternal diabetes so dramatically elevates risk (metabolic disruption pushing signaling below threshold in a genetically susceptible embryo). **Pathway:** Sonic Hedgehog signaling (KEGG hsa04340; Reactome R-HSA-5358351). SHH is autocatalytically cleaved and dual-lipidated, dispatched by DISP1, carried by SCUBE2, handed via GAS1/CDON/BOC to PTCH1, relieving inhibition of SMO and activating GLI2/GLI3. Suggested **GO terms:** GO:0007224 (smoothened signaling pathway), GO:0021871 (forebrain regionalization), GO:0021775 (smoothened signaling in ventral spinal cord patterning), GO:0006915 (apoptotic process), GO:0016540 (protein autoprocessing). Suggested **CL terms:** CL:0000681 (radial glial cell), CL:0011020 (neural progenitor), CL:0000333 (cranial neural crest cell), floor-plate cells. Suggested **CHEBI:** CHEBI:16113 (cholesterol), CHEBI:15756 (palmitic acid). Suggested **UBERON:** UBERON:0001890 (forebrain), UBERON:0001898 (hypothalamus), UBERON:0000007 (pituitary), UBERON:0000970 (eye).

---

## Section-by-Section Characterization (Full Template Coverage)

### 1. Disease Information
SHH-HPE denotes the subset of holoprosencephaly caused by heterozygous *SHH* variants (HPE type 3), plus its graded continuum from cyclopia/alobar HPE to isolated microforms. **Identifiers:** OMIM #142945 (HPE3), *SHH* \*600725; MONDO:0016296; ORPHA:2162; ICD-10 Q04.2; ICD-11 LA05.0; MeSH D016142; HGNC:10848; UniProt Q15465; Ensembl ENSG00000164690. **Synonyms:** Holoprosencephaly type 3; SHH-related HPE; arhinencephaly (older/registry term); microform HPE; cyclopia–cebocephaly–ethmocephaly (severe facial forms). **Source type:** aggregated disease-level resources (OMIM, Orphanet, HPO) and primary literature/registries (EUROCAT, Texas, Japan) — not individual EHR ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/)).

### 2. Etiology
**Primary cause:** heterozygous LOF of *SHH* → haploinsufficiency ([PMID: 19186244](https://pubmed.ncbi.nlm.nih.gov/19186244/)). **Genetic modifiers:** *GLI2, PTCH1, GAS1, CDON, BOC, DISP1, FGF8, TGIF1, ZIC2, SIX3, TDGF1*; combined *GAS1*+*SHH* illustrates multiple hits ([PMID: 20583177](https://pubmed.ncbi.nlm.nih.gov/20583177/)); NODAL/NOTCH/WNT-PCP/FGF/RAS-ERK/cilia/cohesin ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)). **Environmental risk:** maternal pregestational diabetes, twinning, female predominance ([PMID: 29761639](https://pubmed.ncbi.nlm.nih.gov/29761639/)); alcohol and aerosol exposure ([PMID: 33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/)). **Protective:** preconception glycemic control, adequate maternal cholesterol/nutrition, teratogen avoidance; no validated protective allele. **GxE:** threshold trait with documented statistical interactions and a cholesterol-dependent mechanistic basis ([PMID: 33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/), [PMID: 35231446](https://pubmed.ncbi.nlm.nih.gov/35231446/)).

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Holoprosencephaly (forebrain non-cleavage) | Structural CNS | HP:0001360 | Congenital | Severe–variable | Defining |
| Microcephaly | Structural | HP:0000252 | Congenital | Mod–severe | Common |
| Cyclopia/synophthalmia | Craniofacial | HP:0009914 | Congenital | Severe (alobar) | Rare, severe end |
| Proboscis | Craniofacial | HP:0010306 | Congenital | Severe | Severe end |
| Hypotelorism | Craniofacial | HP:0000601 | Congenital | Mild–mod | Very common |
| Median/bilateral cleft lip-palate | Craniofacial | HP:0410030 / HP:0000175 | Congenital | Mod–severe | Common |
| Solitary median maxillary central incisor | Dental/microform | HP:0006315 | Childhood | Mild | Microform marker |
| Developmental delay / intellectual disability | Neurodevelopmental | HP:0001263 / HP:0001249 | Infancy | Variable–severe | Common in survivors |
| Seizures | Neurological | HP:0001250 | Neonatal–infancy | Mod–severe | Common |
| Central diabetes insipidus | Endocrine | HP:0000873 | Neonatal–infancy | Variable | ~47% |
| Dysautonomia (temperature/HR/respiratory) | Autonomic | HP:0012332 | Neonatal | Severe | Frequent (severe forms) |
| Feeding difficulties | Functional | HP:0011968 | Neonatal | Mod–severe | Common |

Onset is congenital/prenatal; course is static-structural with progressive (epilepsy) or fluctuating (DI, dysautonomia) complications. QoL impact ranges from profound (alobar) to negligible (microform carriers with normal intellect, [PMID: 23112757](https://pubmed.ncbi.nlm.nih.gov/23112757/)).

### 4. Genetic / Molecular Information
**Causal gene:** *SHH* (7q36.3). **Variant types:** missense (most common, N-terminal clustering), nonsense/truncating (e.g., p.Tyr175Ter, [PMID: 25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/)), frameshift, splice, whole-gene/7q36 deletions, and enhancer variants. Truncating → more frank HPE (49% vs 35%, [PMID: 22791840](https://pubmed.ncbi.nlm.nih.gov/22791840/)). **Classification:** ACMG/AMP; large VUS burden motivating functional assays ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)). **Allele frequency:** pathogenic alleles ultra-rare in gnomAD; *SHH* LOF-constrained. **Origin:** germline; >70% inherited ([PMID: 21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/)); germline mosaicism relevant to recurrence. **Consequence:** loss of function/haploinsufficiency; allele-specific microforms (I111F, [PMID: 11471164](https://pubmed.ncbi.nlm.nih.gov/11471164/)). **Chromosomal:** trisomy 13/18, 7q36/13q/2p deletions ([PMID: 31886593](https://pubmed.ncbi.nlm.nih.gov/31886593/), [PMID: 24764759](https://pubmed.ncbi.nlm.nih.gov/24764759/)). **Epigenetic:** long-range *SHH* enhancers regulate spatial dosage; HPE-specific methylation data limited (gap).

### 5. Environmental Information
Maternal pregestational diabetes (hyperglycemic teratogenesis), alcohol, aerosol/hair-spray occupational exposure ([PMID: 33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/)); retinoic acid, cholesterol-biosynthesis inhibitors, and the classic SHH-antagonist cyclopamine (Veratrum californicum, causing ovine cyclopia). Sterol disruption impairs SHH cholesterol modification ([PMID: 35231446](https://pubmed.ncbi.nlm.nih.gov/35231446/)). **Infectious agents: not a cause** — HPE is developmental, not infectious.

### 6. Mechanism / Pathophysiology
See the Mechanistic Model section above. Cellular processes: impaired ventral neural progenitor specification, altered proliferation/differentiation balance, apoptosis in craniofacial primordia, and cilium-dependent transduction. Protein dysfunction: reduced secreted/processed SHH ligand; lipidation is obligatory (HHAT loss → severe phenotype, [PMID: 23055936](https://pubmed.ncbi.nlm.nih.gov/23055936/)). Metabolic: cholesterol pivotal for SHH autoprocessing and SMO regulation. **No immune involvement**; **not degenerative** — a developmental patterning failure. Human tissue omics are limited (gap).

### 7. Anatomical Structures Affected
**Primary:** forebrain/telencephalon and diencephalon (UBERON:0001890, UBERON:0000956, UBERON:0001898), pituitary (UBERON:0000007). **Secondary:** eyes/orbits (UBERON:0000970), midface/nose, palate, endocrine axis, craniofacial skeleton. **Tissue/cell:** neuroepithelium, ventral neural progenitors, floor plate, prechordal plate, frontonasal neural crest. **Subcellular:** primary cilium (GO:0005929), plasma membrane (SMO/PTCH1), ER/Golgi (SHH processing), nucleus (GLI). **Laterality:** characteristically **midline, bilateral/symmetric**.

### 8. Temporal Development
**Onset:** congenital, 4th gestational week (days 18–28); detectable by first-trimester ultrasound in severe forms ([PMID: 35821640](https://pubmed.ncbi.nlm.nih.gov/35821640/)). **Course:** malformation is non-progressive; alobar frequently lethal in utero/neonatally, milder forms chronic lifelong. **Critical period:** periconceptional–early first trimester is the sole window for primary prevention; no postnatal correction of the malformation is possible.

### 9. Inheritance and Population
**Epidemiology:** ~1/16,000 live births; ~1/250 conceptuses; Japan BPR 1.54/10,000 ([PMID: 17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/), [PMID: 31886593](https://pubmed.ncbi.nlm.nih.gov/31886593/)). **Inheritance:** autosomal dominant, incomplete (developmental, non–age-dependent) penetrance, highly variable expressivity ([PMID: 19186244](https://pubmed.ncbi.nlm.nih.gov/19186244/)). **Recurrence:** >70% of *SHH* variants inherited → substantial recurrence risk and need for cascade testing ([PMID: 21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/)); germline mosaicism reported. **No anticipation** (not a repeat disorder); no established founder effect. **Demographics:** consistent female predominance and over-representation of twinning ([PMID: 29761639](https://pubmed.ncbi.nlm.nih.gov/29761639/)); severe facial forms reported preferentially in females ([PMID: 24764759](https://pubmed.ncbi.nlm.nih.gov/24764759/)).

### 10. Diagnostics
**Imaging (cornerstone):** first-trimester ultrasound (monoventricle, fused thalami, absent falx) and fetal/postnatal MRI for subtyping ([PMID: 42006104](https://pubmed.ncbi.nlm.nih.gov/42006104/)). **Genetic algorithm:** (1) chromosomal microarray + karyotype first; (2) sequencing + dosage of core genes *SHH, ZIC2, SIX3, TGIF1* ± expanded HPE panels; (3) WES/WGS for unresolved cases, capturing enhancer/deep-intronic variants ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)); functional zebrafish assays reclassify VUS ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)). **Endocrine workup:** screen for central DI and anterior pituitary deficiency ([PMID: 25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/)). **Differential:** septo-optic dysplasia, agenesis of corpus callosum, hydranencephaly, severe hydrocephalus; syndromic contexts (trisomy 13, SLOS). **Screening:** prenatal ultrasound; cascade family testing including for microforms (SMMCI, hypotelorism).

### 11. Outcome / Prognosis
Severity-dependent; ~36% 10-year survival, lowest among rare CAs ([PMID: 35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/), [PMID: 37868647](https://pubmed.ncbi.nlm.nih.gov/37868647/)). Alobar: days–weeks; semilobar: months–years; lobar/MIHV/microform: can reach adulthood. Favorable survival predictors: non-alobar subtype, female sex, atypical (milder) facial features ([PMID: 28640243](https://pubmed.ncbi.nlm.nih.gov/28640243/)). Survivor morbidity: severe neurodevelopmental disability, epilepsy, endocrinopathy (DI, panhypopituitarism), dysautonomia, feeding failure, spasticity.

### 12. Treatment
**No cure or disease-modifying therapy; supportive, multidisciplinary care (MAXO terms suggested).** Antiepileptic drugs for seizures; **desmopressin** for central DI plus hydrocortisone/levothyroxine/GH/sex-steroid replacement for pituitary deficiency ([PMID: 25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/)); management of dysautonomia. **Surgical:** gastrostomy for feeding failure, cleft lip/palate repair, craniofacial reconstruction, CSF shunting if hydrocephalus. **Rehabilitative:** PT/OT/speech, developmental services. **Palliative care and counseling** central in severe forms. No approved gene/RNA/cell therapy; HH-pathway agonists remain preclinical (note that HH *antagonists* vismodegib/sonidegib are approved for HH-driven cancers — the opposite pathway direction).

### 13. Prevention
**Primary:** periconceptional glycemic control in diabetic mothers; avoidance of alcohol, retinoids, and sterol-disrupting exposures; adequate maternal nutrition/cholesterol ([PMID: 31454511](https://pubmed.ncbi.nlm.nih.gov/31454511/), [PMID: 35104296](https://pubmed.ncbi.nlm.nih.gov/35104296/)). **Secondary:** first-trimester ultrasound screening; prenatal molecular testing. **Tertiary:** proactive treatment of DI, hypopituitarism, seizures, aspiration. **Counseling:** essential given AD inheritance with low penetrance/variable expressivity; cascade testing, prenatal diagnosis, and PGT-M options — with the caveat that cognitive status cannot identify carriers ([PMID: 23112757](https://pubmed.ncbi.nlm.nih.gov/23112757/)). **Not applicable:** immunization (non-infectious).

### 14. Other Species / Natural Disease
**Taxonomy:** mouse (NCBI:txid10090), zebrafish (txid7955), sheep (txid9940), human (txid9606). **Orthologs (NCBI Gene):** human *SHH* 6469; mouse *Shh* 20423; zebrafish *shha* 30269. **Natural disease (OMIA):** classic ovine cyclopia ("monkey-faced lamb") from *Veratrum californicum* grazing (cyclopamine, an SMO antagonist) — the discovery that revealed HH-pathway/cholesterol biology; sporadic HPE in dogs, cats, cattle. **Comparative biology:** deeply conserved midline patterning; zebrafish/mouse mutants recapitulate cyclopia. **Transmission:** none — non-infectious, non-zoonotic.

### 15. Model Organisms
**Mouse (MGI):** *Shh* knockout — cyclopia, absent ventral neural tube, notochord/floorplate defects ([PMID: 8837770](https://pubmed.ncbi.nlm.nih.gov/8837770/)); *Hhat* mutants — acrania-holoprosencephaly-agnathia ([PMID: 23055936](https://pubmed.ncbi.nlm.nih.gov/23055936/)); *Fgf8* hypomorphs — HPE with hypothalamic-pituitary defects ([PMID: 21832120](https://pubmed.ncbi.nlm.nih.gov/21832120/)). Conditional/knock-in and pathway-gene models available (IMPC/KOMP/MMRRC). **Zebrafish (ZFIN):** *shha* CRISPR/Cas9 rescue assay for variant validation ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)). **In vitro:** HH-reporter lines, iPSC-derived ventral forebrain organoids. **Recapitulation:** strong for severe (homozygous/null) phenotype; key limitation is that human heterozygous HPE retains a hypoplastic pituitary whereas homozygous animal models lack it entirely ([PMID: 20013843](https://pubmed.ncbi.nlm.nih.gov/20013843/)); mice usually need homozygous/compound hits, bridged by sensitized backgrounds and gene-environment paradigms. **Resources:** MGI, IMPC/KOMP, MMRRC, ZFIN, Alliance of Genome Resources, OMIA.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in report |
|---|---|---|
| [17274816](https://pubmed.ncbi.nlm.nih.gov/17274816/) | *Holoprosencephaly* (review) | Seven HPE genes; severity spectrum; prevalence; GD18–28 timing |
| [19186244](https://pubmed.ncbi.nlm.nih.gov/19186244/) | *Murine models of holoprosencephaly* | Convergent SHH-signaling mechanism; incomplete penetrance |
| [22791840](https://pubmed.ncbi.nlm.nih.gov/22791840/) | *396 individuals with SHH mutations* | SHH skews mild (non-HPE 64%); truncating > non-truncating |
| [21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/) | *645 European HPE cases* | Gene-specific spectrum position; inheritance vs de novo |
| [23055936](https://pubmed.ncbi.nlm.nih.gov/23055936/) | *Hhat mutations perturb Hedgehog* | 17% familial figure; palmitoylation required |
| [32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/) | *SHH variants in zebrafish* | Functional validation; VUS problem |
| [35231446](https://pubmed.ncbi.nlm.nih.gov/35231446/) | *SHH–Patched1 complex structure* | Cholesterol/palmitate & GAS1 handoff to PTCH1 |
| [25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/) | *SHH & congenital hypopituitarism* | Central DI 47%; anterior pituitary 53%; p.Tyr175Ter |
| [20013843](https://pubmed.ncbi.nlm.nih.gov/20013843/) | *Hedgehog & endocrine gland development* | Heterozygous human vs homozygous animal pituitary |
| [29761634](https://pubmed.ncbi.nlm.nih.gov/29761634/) | *Extracephalic manifestations of NCNS-HPE* | Multi-organ involvement |
| [23112757](https://pubmed.ncbi.nlm.nih.gov/23112757/) | *High intellect in microform HPE* | Normal/above-average intellect in carriers |
| [35351164](https://pubmed.ncbi.nlm.nih.gov/35351164/) | *Survival of rare CAs (EUROCAT)* | Lowest survival across ages |
| [37868647](https://pubmed.ncbi.nlm.nih.gov/37868647/) | *Survival, Texas 1999–2018* | 10-yr survival 36.9%, lowest of 30 |
| [31886593](https://pubmed.ncbi.nlm.nih.gov/31886593/) | *Nationwide survey, Japan* | BPR 1.54/10,000; subtype frequencies |
| [29761639](https://pubmed.ncbi.nlm.nih.gov/29761639/) | *Nongenetic risk factors (review)* | Diabetes, twinning, female predominance |
| [33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/) | *Environmental risk & GxE* | Pregestational diabetes 9.2% vs 0%; alcohol; GxE |
| [35104296](https://pubmed.ncbi.nlm.nih.gov/35104296/) | *Diabetes & anomalies meta-analysis* | HPE RR ~18 with pregestational diabetes |
| [31454511](https://pubmed.ncbi.nlm.nih.gov/31454511/) | *Diabetes & specific birth defects (NBDPS)* | HPE aOR 13.1 |
| [28640243](https://pubmed.ncbi.nlm.nih.gov/28640243/) | *Adults/adolescents with HPE* | Survival predictors |
| [8837770](https://pubmed.ncbi.nlm.nih.gov/8837770/) | *Shh-null mice (Chiang 1996)* | Definitive causal model; midline mechanism |
| [11471164](https://pubmed.ncbi.nlm.nih.gov/11471164/) | *SHH & SMMCI* | I111F allele → isolated microform |
| [20583177](https://pubmed.ncbi.nlm.nih.gov/20583177/) | *GAS1 sequence changes* | Multiple-hit model; environmental contribution |
| [41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/) | *Recent advances (2024 review)* | Modifier pathways; GxE; counseling complexity |
| [24764759](https://pubmed.ncbi.nlm.nih.gov/24764759/) | *HPE in South America* | Chromosomal (~27%) & mutation-yield context |
| [21832120](https://pubmed.ncbi.nlm.nih.gov/21832120/) | *FGF8 mutations & HPE* | Recessive HPE + hypothalamo-pituitary model |
| [42006104](https://pubmed.ncbi.nlm.nih.gov/42006104/) | *Brain-face connection in HPE* | Prenatal imaging; alobar outcomes |
| [35821640](https://pubmed.ncbi.nlm.nih.gov/35821640/) | *First-trimester detectable anomalies* | Timing of prenatal diagnosis |

---

## Limitations and Knowledge Gaps

1. **VUS burden:** Only a minor fraction of *SHH* variants are functionally proven pathogenic ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)); most classification relies on segregation and in silico prediction.
2. **Penetrance quantification:** Incomplete penetrance is well-documented qualitatively but poorly quantified numerically per variant class — a major counseling gap ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)).
3. **Modifier attribution:** The specific contribution of individual modifier genes/pathways (NODAL, NOTCH, WNT/PCP, cilia, cohesin) to any given patient's phenotype is rarely resolvable ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)).
4. **Model dosage mismatch:** Null animal models overstate severity relative to typically heterozygous human disease, especially for pituitary presence/absence ([PMID: 20013843](https://pubmed.ncbi.nlm.nih.gov/20013843/)).
5. **Ascertainment/survivor bias:** With ~1/250 conceptus loss vs 1/16,000 live births, live-birth cohorts underrepresent the most severe biology.
6. **Epidemiologic confounding:** Nongenetic risk associations (diabetes, alcohol) are observational; residual confounding and reverse causation remain possible despite consistent replication.
7. **Omics gaps:** No human HPE-tissue transcriptomic/epigenomic/methylation profiles specific to *SHH*-HPE were identified; no validated HPE-specific QoL instrument exists.

---

## Proposed Follow-up Experiments / Actions

1. **Variant functional atlas:** Systematically classify reported *SHH* missense/truncating variants using the established zebrafish *shha* rescue assay ([PMID: 32939873](https://pubmed.ncbi.nlm.nih.gov/32939873/)) plus a mammalian GLI-reporter signaling assay, converting VUS into actionable calls and mapping genotype→signaling→phenotype.
2. **Quantitative penetrance modeling:** Combine multi-cohort pedigree data (Solomon 2012, Mercier 2011) to estimate variant-class-specific penetrance and expressivity distributions for counseling ([PMID: 22791840](https://pubmed.ncbi.nlm.nih.gov/22791840/), [PMID: 21940735](https://pubmed.ncbi.nlm.nih.gov/21940735/)).
3. **GxE mechanistic test:** In *Shh*-heterozygous mice, test whether maternal hyperglycemia and sterol-synthesis inhibitors shift phenotype severity, directly probing the threshold model and cholesterol-dependent lipidation ([PMID: 35231446](https://pubmed.ncbi.nlm.nih.gov/35231446/), [PMID: 33111505](https://pubmed.ncbi.nlm.nih.gov/33111505/)).
4. **Modifier screen:** CRISPR screen of NODAL/NOTCH/WNT-PCP/FGF/RAS-ERK/cilia/cohesin candidates in a sensitized *Shh*-heterozygous background to quantify epistatic contributions to threshold crossing ([PMID: 41102431](https://pubmed.ncbi.nlm.nih.gov/41102431/)).
5. **Prospective endocrine surveillance protocol:** Standardize screening for central DI and anterior pituitary deficiency in all molecularly confirmed HPE-spectrum patients, given ~47%/53% frequencies ([PMID: 25056824](https://pubmed.ncbi.nlm.nih.gov/25056824/)).
6. **Preconception prevention trial:** Evaluate intensified periconceptional glycemic-control programs for HPE risk reduction in diabetic mothers, leveraging the large diabetes effect sizes ([PMID: 31454511](https://pubmed.ncbi.nlm.nih.gov/31454511/), [PMID: 35104296](https://pubmed.ncbi.nlm.nih.gov/35104296/)).

---

*Report compiled from 10 confirmed findings and 52 reviewed papers across 5 investigation iterations. Evidence source types are noted throughout: human clinical cohorts/registries [H], mouse and zebrafish model organisms [M], in vitro/structural biology [V], and computational/epidemiological meta-analyses [C].*


## Artifacts

- [OpenScientist final report](SHH_Holoprosencephaly_Spectrum-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SHH_Holoprosencephaly_Spectrum-deep-research-openscientist_artifacts/final_report.pdf)