---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-16T20:44:40.634179'
end_time: '2026-09-16T21:28:33.430383'
duration_seconds: 2632.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Action Myoclonus-Renal Failure Syndrome
  mondo_id: MONDO:0009699
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Action_Myoclonus-Renal_Failure_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Action_Myoclonus-Renal_Failure_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Action Myoclonus-Renal Failure Syndrome
- **MONDO ID:** MONDO:0009699 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Action Myoclonus-Renal Failure Syndrome** covering all of the
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

# Action Myoclonus–Renal Failure Syndrome (AMRF): A Comprehensive Disease Characteristics Report

**Disease:** Action Myoclonus–Renal Failure Syndrome
**MONDO ID:** MONDO:0009699 · **OMIM:** #254900 (EPM4) · **Orphanet:** ORPHA:163703
**Category:** Mendelian, autosomal recessive lysosomal disorder
**Causal gene:** *SCARB2* (encoding LIMP-2) · HGNC:10534 · Ensembl ENSG00000138760 · UniProt Q14108 · chr4q21.1

---

## Summary

Action Myoclonus–Renal Failure Syndrome (AMRF) is an ultra-rare, autosomal recessive, multisystem lysosomal disorder that unites two seemingly unrelated clinical problems: a **progressive myoclonus epilepsy (PME)** with preserved cognition and a **proteinuric collapsing focal segmental glomerulosclerosis (FSGS)** that progresses to end-stage renal failure. The syndrome is caused by **biallelic loss-of-function variants in *SCARB2***, the gene encoding **lysosomal integral membrane protein type 2 (LIMP-2)**. LIMP-2 is the mannose-6-phosphate–independent sorting receptor that traffics **β-glucocerebrosidase (GCase)** from the endoplasmic reticulum (ER) to the lysosome. When LIMP-2 is absent or misfolded, GCase fails to reach the lysosome, is retained in the ER, and lysosomal GCase activity falls—producing a partial, tissue-specific enzyme deficiency and downstream glycosphingolipid dysregulation.

The mechanistic chain runs from mutation → LIMP-2 loss/ER-retention → GCase mistrafficking → partial lysosomal GCase deficiency → accumulation of the toxic glycosphingolipid **glucosylsphingosine (GlcSph)** and glucosylated cholesterol (rather than bulk glucosylceramide storage) → neuronal and podocyte injury → the branched clinical phenotype of cortical action myoclonus, tremor, ataxia and seizures on the neurological arm, and glomerular collapse with proteinuria and renal failure on the renal arm. Because residual GCase remains high in leukocytes but is severely deficient in fibroblasts and tissue, standard leukocyte enzyme assays are normal—a diagnostic pitfall that distinguishes AMRF from classical Gaucher disease.

Clinically, AMRF typically presents in **adolescence or young adulthood** (tremor onset ~20 years, disabling action myoclonus ~22 years), with proteinuria often detected in childhood-to-early-adulthood and progressing to renal failure within 0–8 years. Cognition is characteristically spared. There is no approved disease-modifying therapy; management is symptomatic (antimyoclonic/antiseizure drugs, dialysis and renal transplantation). Emerging disease-modifying strategies include **substrate-reduction therapy with miglustat** and **vitamin E repletion**, the latter validated in *Scarb2*-knockout mice. Diagnosis rests on the combination of cortical-myoclonus electrophysiology, urinalysis/renal biopsy findings, and molecular confirmation of biallelic *SCARB2* variants.

---

## Key Findings

### F001 — AMRF is caused by biallelic loss-of-function mutations in *SCARB2* (LIMP-2)

Two independent 2008 studies established the genetic basis of AMRF. Berkovic and colleagues used homozygosity mapping in three unrelated families to map the disease locus to 4q13-21 and identified *SCARB2/LIMP-2* by microarray expression analysis; mutations were found in all three mapping families plus two additional AMRF families, associated with an absence of SCARB2 protein. As the authors state, *"The ancestral lysosomal-membrane protein SCARB2/LIMP-2 is responsible for AMRF"* ([PMID: 18308289](https://pubmed.ncbi.nlm.nih.gov/18308289/)). Independently, Balreira et al. identified a homozygous nonsense mutation at codon 178 (**W178X**), noting that *"A homozygous nonsense mutation in codon 178 of SCARB2 was found in the patient, whereas her healthy parents were heterozygous for the mutation"* ([PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)). Crucially, the same paper established the protein's function—*SCARB2* encodes LIMP-2, *"the sorting receptor for beta-glucocerebrosidase."* This gene-to-function link is the foundation of all downstream mechanistic understanding of AMRF.

**Ontology/annotation:** Gene *SCARB2* (HGNC:10534); protein LIMP-2 / SR-B2 (UniProt Q14108); MONDO:0009699; OMIM #254900.

### F002 — The renal phenotype is proteinuric collapsing focal segmental glomerulosclerosis

The renal lesion of AMRF is a severe, collapsing variant of FSGS. Berkovic et al. describe AMRF as *"the remarkable combination of focal glomerulosclerosis, frequently with glomerular collapse, and progressive myoclonus epilepsy"* ([PMID: 18308289](https://pubmed.ncbi.nlm.nih.gov/18308289/)). Balreira et al. reported nephrotic syndrome with *"a strong accumulation of C1q in capillary loops and mesangium of kidney"* ([PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)), a pattern designated **nephropathy C1q**. Chaves et al. confirmed PME with nephropathy C1q in two siblings ([PMID: 21782476](https://pubmed.ncbi.nlm.nih.gov/21782476/)). The presence of collapse and podocyte injury points to the podocyte as the principal renal target cell.

**Ontology/annotation:** HP:0000097 (Focal segmental glomerulosclerosis); HP:0000100 (Nephrotic syndrome); HP:0000093 (Proteinuria); UBERON:0000074 (renal glomerulus); CL:0000653 (podocyte).

### F003 — *Limp2/Scarb2* knockout mice recapitulate multisystem AMRF-relevant pathology

The mouse model predates the human gene discovery and is central to mechanistic understanding. Gamp et al. showed that LIMP-2–deficient mice develop uni/bilateral hydronephrosis from ureteropelvic junction obstruction, serious hearing impairment (spiral ganglia and hair cell loss, stria vascularis degeneration), and a peripheral demyelinating neuropathy: *"LIMP-2-deficient mice are also characterized by a peripheral demyelinating neuropathy"* ([PMID: 12620969](https://pubmed.ncbi.nlm.nih.gov/12620969/)). Berkovic's reanalysis of the same knockout revealed intracellular inclusions in cerebral and cerebellar cortex and subtle glomerular changes. More recently, Li et al. showed that *Scarb2*-deficient mice have age-dependent dietary lipid malabsorption and vitamin E deficiency via gut dysbiosis and FXR hyperactivation, and importantly that *"inhibiting FXR or supplementing vitamin E ameliorates the neuromotor impairment and neuropathy in Scarb2 knockout mice"* ([PMID: 38635907](https://pubmed.ncbi.nlm.nih.gov/38635907/))—a translationally significant therapeutic lead.

### F004 — LIMP-2 loss disrupts glycosphingolipid homeostasis (GlcSph, GlcChol) rather than causing bulk GlcCer storage

A key refinement of the "lysosomal storage" paradigm comes from Gaspar et al., who showed that in *Limp2-/-* mouse tissues the only consistently deficient lysosomal enzyme was GCase, and that *"GCase deficiency in tissues does not correlate with increases in GlcCer, but rather with increases in glucosylsphingosine (GlcSph) and glucosylated cholesterol (GlcChol)"* ([PMID: 40639771](https://pubmed.ncbi.nlm.nih.gov/40639771/)). This reframes AMRF as a disorder of **toxic glycosphingolipid accumulation** (GlcSph is a bioactive, cytotoxic lyso-lipid) rather than classical macromolecular storage. The same study explains a longstanding diagnostic anomaly: *"residual GCase is remarkably high in leukocytes,"* accounting for the normal leukocyte enzyme assays seen in patients despite tissue-level deficiency.

**Ontology/annotation:** CHEBI:88431 (glucosylsphingosine); GO:0006687 (glycosphingolipid metabolic process).

### F005 — Neurological phenotype: adolescent/young-adult onset tremor, progressive action myoclonus, ataxia, seizures — without dementia

Badhwar et al., in the landmark series of 15 patients from 9 families, quantified the neurological course: *"Tremor (onset 17-26 years, mean 19.8 years, median 19 years) and progressively disabling action myoclonus (onset 14-29 years, mean 21.7 years, median 21 years), with infrequent generalized seizures (onset 20-28 years, mean 22.7 years, median 22 years) and cerebellar features are characteristic"* ([PMID: 15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/)). The same series established the renal timeline: *"Proteinuria, detected between ages 9 and 30 years in all cases, progressed to renal failure in 12 out of 15 patients within 0-8 years after proteinuria detection."* Rubboli et al. emphasized the preserved cognition and cortical origin of the myoclonus: *"The main clinical features were adolescent-young adulthood onset, progressive action myoclonus, ataxia, absence of cognitive deterioration and, in most cases, epilepsy"* ([PMID: 22050460](https://pubmed.ncbi.nlm.nih.gov/22050460/)), with rhythmic myoclonic jerks at 12–20 Hz resembling postural tremor and a demonstrated cortical origin via EEG–EMG coherence.

**Ontology/annotation:** HP:0001336 (Myoclonus); HP:0002345 (Action tremor); HP:0001251 (Ataxia); HP:0001250 (Seizure); HP:0007000 (Photosensitive myoclonic seizures); absence of HP:0001268 (Mental deterioration).

### F006 — *SCARB2* mutations cause a spectrum from AMRF to PME without renal failure; C-terminal variant location influences age of onset

The renal phenotype is not fully penetrant. Rubboli et al. described five Italian PME patients with *SCARB2* mutations but **without renal impairment**: *"We describe the clinical and neurophysiologic features of PME associated with SCARB2 mutations without renal impairment"* ([PMID: 22050460](https://pubmed.ncbi.nlm.nih.gov/22050460/)), indicating variable expressivity/incomplete penetrance of the renal arm. Atasu et al., in an in-depth literature review, found a genotype–phenotype correlation: *"only the C terminal localization of the pathogenic variant significantly affected the clinical presentation, particularly the age at onset"* ([PMID: 35346091](https://pubmed.ncbi.nlm.nih.gov/35346091/)), while variant type had no major impact on the overall course. Intrafamilial heterogeneity is documented even among siblings sharing an identical truncating variant (p.N45MfsX88).

### F007 — Treatment is largely symptomatic; substrate reduction therapy (miglustat) shows promise; vitamin E is a candidate

No disease-modifying therapy is approved. Management is symptomatic: antimyoclonic/antiseizure medication (valproate, levetiracetam, piracetam, clonazepam, perampanel) and renal replacement therapy. Badhwar et al. underscore the historical importance of renal support: *"The syndrome was not recognized prior to the advent of dialysis and renal transplantation because of its rapidly fatal course if renal failure is untreated"* ([PMID: 15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/)). Two lines of evidence support **substrate-reduction therapy (SRT)**: Chaves et al. reported that *"When substrate-reduction therapy, to correct the possible glucocerebroside storage in the cells with glucocerebrosidase deficiency, was administered to one of the siblings, a significant improvement was observed"* ([PMID: 21782476](https://pubmed.ncbi.nlm.nih.gov/21782476/)); and Quraishi et al. reported that miglustat halted myoclonus progression, resolved dysphagia, and allowed reacquisition of skills ([PMID: 34337151](https://pubmed.ncbi.nlm.nih.gov/34337151/)). Vitamin E repletion or FXR inhibition ameliorated neuromotor deficits in *Scarb2*-knockout mice ([PMID: 38635907](https://pubmed.ncbi.nlm.nih.gov/38635907/)).

**Ontology/annotation:** NCIT candidate terms — Miglustat (glucosylceramide synthase inhibitor / SRT), Valproate, Levetiracetam, Clonazepam, Perampanel, Renal Dialysis, Kidney Transplantation, Vitamin E supplementation.

### F008 — LIMP-2 has pleiotropic non-lysosomal roles informing multisystem involvement

Beyond its GCase-sorting role, LIMP-2 has additional functions that may contribute to the multisystem phenotype. Schroen et al. showed LIMP-2 is a component of the cardiac intercalated disc that associates with cadherin; *"these LIMP-2 null mice failed to mount a hypertrophic response to increased blood pressure but developed cardiomyopathy"* ([PMID: 17485520](https://pubmed.ncbi.nlm.nih.gov/17485520/)). Gonzalez et al. reviewed LIMP-2 as *"a receptor for specific enteroviruses, two unanticipated findings that reaffirm the myriad roles of lysosomal proteins"* ([PMID: 24389070](https://pubmed.ncbi.nlm.nih.gov/24389070/)) (EV71, coxsackievirus A16), noting ~14 disease-causing *SCARB2* mutations known as of 2014.

### F009 — *SCARB2* is tolerant of heterozygous loss-of-function (gnomAD), consistent with autosomal recessive inheritance

gnomAD constraint metrics for *SCARB2* (ENSG00000138760, chr4:76,158,737–76,234,536, GRCh38) show the gene is **not haploinsufficient**: pLI = 0.0009, observed/expected LoF (oe_lof) = 0.49 with a LOEUF (90% CI upper bound) of 0.67 (observed LoF = 29 vs expected 58.6); missense Z = 1.60. This tolerance of heterozygous LoF is exactly what is expected for a recessive disease gene where a single functional allele suffices. It is consistent with the clinical observation that carriers are healthy—Balreira's *"healthy parents were heterozygous for the mutation"* ([PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)). The disease is catalogued as EPM4 (progressive myoclonic epilepsy-4 with or without renal failure), OMIM #254900.

### F010 — Diagnosis combines cortical-myoclonus electrophysiology, renal/urinalysis findings, and *SCARB2* molecular testing

AMRF diagnosis is a three-legged stool. **Electrophysiology** shows cortical action myoclonus: giant somatosensory evoked potentials, marked photosensitivity, and 12–20 Hz rhythmic myoclonic jerks with EEG–EMG coherence demonstrating cortical origin ([PMID: 22050460](https://pubmed.ncbi.nlm.nih.gov/22050460/)). Hotait et al. highlighted distinctive EEG features: *"this report emphasizes the presence of two EEG patterns, fixation-off phenomenon, and bursts of parasagittal spikes exclusively seen during REM sleep that appear to be characteristic of this condition"* ([PMID: 33343627](https://pubmed.ncbi.nlm.nih.gov/33343627/)). **Renal workup** detects proteinuria on urinalysis and collapsing FSGS on biopsy. **Molecular testing** is the gold standard—Yari et al. exemplify this: *"Genetic analysis identified a homozygous splicing c.423+1 G>A variant in the SCARB2 gene of the proband and his affected sister"* ([PMID: 33772352](https://pubmed.ncbi.nlm.nih.gov/33772352/)). Critically, enzyme testing must use fibroblasts, not leukocytes: Balreira found *"a normal beta-glucocerebrosidase activity in leukocytes, but a severe enzymatic deficiency in cultured skin fibroblasts"* ([PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)).

### F011 — Prognosis: progressive, disabling, with early mortality

Historically fatal from untreated renal failure, AMRF's prognosis is now driven by relentless neurological decline. Badhwar et al. note the disease *"was not recognized prior to the advent of dialysis and renal transplantation because of its rapidly fatal course if renal failure is untreated"* ([PMID: 15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/)). Quraishi et al. characterize AMRF as *"a rare, progressive myoclonic epilepsy with early mortality"* ([PMID: 34337151](https://pubmed.ncbi.nlm.nih.gov/34337151/)). The trajectory is proteinuria (childhood–early adulthood) → renal failure within 0–8 years, and action myoclonus/tremor progressing to severe disability, dysphagia, and death (often from neurological complications, aspiration, or status epilepticus once renal failure is managed). Cognition is typically preserved throughout ([PMID: 22050460](https://pubmed.ncbi.nlm.nih.gov/22050460/)).

### F012 — Mechanistic basis: AMRF mutations cause ER retention of LIMP-2 and disrupt pH-dependent coiled-coil binding to GCase

The molecular pathology is precisely characterized. Blanz et al. showed that *"All mutations investigated in this study lead to a retention of LIMP-2 in the endoplasmic reticulum (ER) but affect the binding to beta-GC differentially"* ([PMID: 19933215](https://pubmed.ncbi.nlm.nih.gov/19933215/)); binding occurs through a highly conserved amphipathic coiled-coil domain (segment 145–288), and its disruption abolishes GCase binding. Zachos et al. defined the release mechanism: *"the lumenal acidification mediated by the vacuolar (H(+))-ATPase triggers the dissociation of LIMP-2 and GC in late endosomal/lysosomal compartments"* ([PMID: 22537104](https://pubmed.ncbi.nlm.nih.gov/22537104/)), with a critical histidine residue conferring pH sensitivity. In patient cells, Balreira confirmed GCase mislocalization: *"decreased amounts of beta-glucocerebrosidase, which was mainly located in the endoplasmic reticulum, as assessed by its sensitivity to Endo H"* ([PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)).

### F013 — Anatomical involvement: cerebral/cerebellar cortex, kidney glomeruli/podocytes, peripheral nerve; lysosome the key compartment

Badhwar et al. documented the tissue-level pathology: *"Brain autopsy in two patients revealed extraneuronal pigment accumulation. Renal biopsies showed collapsing glomerulopathy, a severe variant of focal glomerulosclerosis"* ([PMID: 15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/)). Berkovic's knockout reanalysis localized storage pathology: the mice *"showed intracellular inclusions in cerebral and cerebellar cortex, and the kidneys showed subtle glomerular changes"* ([PMID: 18308289](https://pubmed.ncbi.nlm.nih.gov/18308289/)). The cortical origin of myoclonus localizes to sensorimotor cortex; the peripheral nervous system shows axonal/demyelinating polyneuropathy; and the subcellular locus is the lysosome (LIMP-2 being a lysosomal integral membrane protein).

**Ontology/annotation:** UBERON:0000956 (cerebral cortex); UBERON:0002129 (cerebellar cortex); UBERON:0002113 (kidney); UBERON:0000074 (renal glomerulus); UBERON:0000044 (peripheral nerve); GO:0005764 (lysosome); GO:0005783 (endoplasmic reticulum); CL:0000653 (podocyte); CL:0000540 (neuron).

### F014 — Epidemiology and etiology: ultra-rare, purely monogenic autosomal recessive; consanguinity increases risk

AMRF is ultra-rare (Orphanet ORPHA:163703; prevalence <1/1,000,000). Only ~4 patients were known before 2004; Badhwar's landmark series expanded this: *"We now describe 15 individuals with AMRF from five countries"* ([PMID: 15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/)). Since 2008, several dozen *SCARB2*-related cases have been reported worldwide, many from consanguineous families—Ekmekci et al. note *"This study examines a consanguineous family with multiple members presenting myoclonic epilepsy"* ([PMID: 37529812](https://pubmed.ncbi.nlm.nih.gov/37529812/)). The etiology is entirely genetic (biallelic pathogenic *SCARB2* variants); no environmental, infectious, toxic, or lifestyle cause is implicated. Sex ratio is ~1:1, as expected for an autosomal recessive disorder.

### F015 — Prevention is limited to genetic counseling, carrier/cascade testing, and prenatal/PGD; secondary/tertiary prevention targets renal and nutritional complications

Because AMRF is Mendelian with no modifiable environmental cause, there is no primary prevention. Risk reduction relies on genetic counseling of at-risk and consanguineous families, carrier testing, cascade testing of relatives, and prenatal or preimplantation genetic diagnosis once the familial *SCARB2* variants are known (carriers being unaffected per [PMID: 18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/)). **Secondary prevention** consists of early urinalysis surveillance for proteinuria to enable timely renal management. **Tertiary prevention** includes dialysis/transplant, aspiration precautions, antimyoclonic therapy, and—based on mouse data—vitamin E supplementation for the malabsorption-driven deficiency: *"supplementing vitamin E ameliorates the neuromotor impairment and neuropathy in Scarb2 knockout mice"* ([PMID: 38635907](https://pubmed.ncbi.nlm.nih.gov/38635907/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *SCARB2*** (nonsense, frameshift, splice-site, or missense) *leads to* absence, truncation, or misfolding of the LIMP-2 protein. *(Demonstrated — F001, F012)*
2. Mutant/absent LIMP-2 *results in* retention of LIMP-2 in the **endoplasmic reticulum** and failure of the LIMP-2–GCase complex to traffic to the lysosome. *(Demonstrated — F012)*
3. ER-retained, unescorted **β-glucocerebrosidase (GCase) is mistargeted** and remains Endo H–sensitive in the ER instead of maturing in the lysosome. *(Demonstrated in patient fibroblasts — F004, F012)*
4. Mistrafficking *results in* **partial, tissue-specific lysosomal GCase deficiency** — severe in brain, kidney, and fibroblasts, but with high residual activity in leukocytes. *(Demonstrated — F004, F010)*
5. Reduced lysosomal GCase *leads to* dysregulated glycosphingolipid catabolism, with accumulation of the toxic lyso-lipid **glucosylsphingosine (GlcSph)** and **glucosylated cholesterol**, rather than bulk glucosylceramide storage. *(Demonstrated in mouse tissue — F004; toxicity to human tissue inferred)*
6. Glycosphingolipid dysregulation and lysosomal dysfunction *result in* cellular injury that **branches** by tissue:
   - **6a (neurological arm):** Injury to cortical/cerebellar neurons *leads to* cortical hyperexcitability → **cortical action myoclonus, tremor, ataxia, photosensitive seizures**, with intracellular inclusions and extraneuronal pigment. Cognition is spared. *(Demonstrated clinically/pathologically — F005, F013)*
   - **6b (renal arm):** Injury to **podocytes** *leads to* **collapsing focal segmental glomerulosclerosis** with C1q deposition → proteinuria/nephrotic syndrome → **end-stage renal failure**. *(Demonstrated — F002, F013)*
   - **6c (peripheral/systemic arm, partly from mouse):** *Leads to* peripheral demyelinating/axonal neuropathy; and (mouse) gut dysbiosis → FXR hyperactivation → lipid malabsorption → **vitamin E deficiency** compounding neuromotor deficits. *(Demonstrated in mouse; human relevance inferred — F003)*
7. Progressive neuronal and glomerular damage *results in* **cumulative disability and early mortality** — historically from untreated renal failure, now predominantly from neurological decline once dialysis/transplant manages the kidney. *(Demonstrated — F011)*

```
   SCARB2 biallelic LoF
          │
          ▼
   LIMP-2 absent / ER-retained  ──(no lysosomal sorting receptor)
          │
          ▼
   GCase mistrafficked → trapped in ER (Endo H–sensitive)
          │
          ▼
   Partial lysosomal GCase deficiency (tissue-specific;
   high residual in leukocytes → normal blood assay)
          │
          ▼
   ↑ Glucosylsphingosine (GlcSph) + glucosylated cholesterol
   (toxic lyso-lipids, NOT bulk GlcCer storage)
          │
     ┌────┴───────────────┬─────────────────────┐
     ▼                    ▼                     ▼
  NEURONS              PODOCYTES          PERIPHERAL NERVE / GUT
  cortex/cerebellum    glomerulus         + (mouse) dysbiosis→FXR
     │                    │                     │
     ▼                    ▼                     ▼
  Cortical action     Collapsing FSGS      Neuropathy; vit E
  myoclonus, tremor,  + C1q deposition     deficiency (mouse)
  ataxia, seizures    → proteinuria →
  (cognition SPARED)  renal failure
     │                    │
     └──────────┬─────────┘
                ▼
    Progressive disability + early mortality
```

### Upstream vs downstream

- **Upstream (initiating):** *SCARB2* mutation → LIMP-2 loss → ER retention → GCase mistrafficking. These are the shared, obligate steps.
- **Midstream (biochemical):** partial GCase deficiency → GlcSph/GlcChol accumulation.
- **Downstream (phenotypic, branched):** neuronal injury (myoclonus/ataxia/seizures), podocyte injury (FSGS/renal failure), peripheral nerve and systemic/nutritional effects. The **renal arm is incompletely penetrant** (F006), explaining pure-PME cases; **C-terminal variant location modulates age of onset** (F006), the only established genotype–phenotype modifier.

### Cell types and biological processes

| Level | Entity | Ontology suggestion |
|---|---|---|
| Biological process | Lysosomal protein transport / GSL catabolism | GO:0007041, GO:0006687 |
| Biological process | ER retention / protein misfolding | GO:0034976 |
| Cell type | Cortical/cerebellar neuron | CL:0000540 |
| Cell type | Podocyte | CL:0000653 |
| Cell type | Schwann cell / peripheral nerve | CL:0002573 |
| Compartment | Lysosome | GO:0005764 |
| Compartment | Endoplasmic reticulum | GO:0005783 |
| Metabolite | Glucosylsphingosine | CHEBI:88431 |

---

## Evidence Base

| PMID | Study (short title) | Type | Supports finding(s) | Contribution |
|---|---|---|---|---|
| [18308289](https://pubmed.ncbi.nlm.nih.gov/18308289/) | *Array-based gene discovery… SCARB2/LIMP-2* | Human genetics | F001, F002, F013 | Maps AMRF to 4q13-21; identifies *SCARB2* as causal; defines renal pathology |
| [18424452](https://pubmed.ncbi.nlm.nih.gov/18424452/) | *Nonsense mutation in LIMP-2 gene…* | Human genetics/biochem | F001, F002, F009, F010, F012 | W178X mutation; recessive segregation; C1q nephropathy; fibroblast vs leukocyte assay; ER localization of GCase |
| [12620969](https://pubmed.ncbi.nlm.nih.gov/12620969/) | *LIMP-2/LGP85 deficiency…in mice* | Mouse model | F003, F013 | Hydronephrosis, deafness, peripheral demyelinating neuropathy |
| [38635907](https://pubmed.ncbi.nlm.nih.gov/38635907/) | *Gut dysbiosis…Scarb2 deficiency* | Mouse model | F003, F007, F015 | FXR/vitamin E axis; therapeutic rescue |
| [40639771](https://pubmed.ncbi.nlm.nih.gov/40639771/) | *LIMP-2 deficiency…glycolipid abnormalities* | Mouse biochem | F004 | GlcSph/GlcChol accumulation; high leukocyte residual GCase |
| [15364701](https://pubmed.ncbi.nlm.nih.gov/15364701/) | *AMRF: characterization of a unique cerebro-renal disorder* | Human clinical series (n=15) | F005, F007, F011, F013, F014 | Ages of onset; renal timeline; prognosis; anatomy; rarity |
| [22050460](https://pubmed.ncbi.nlm.nih.gov/22050460/) | *PME without renal failure caused by SCARB2* | Human clinical/neurophysiology | F005, F006, F010, F011 | Preserved cognition; cortical myoclonus; renal-sparing spectrum |
| [35346091](https://pubmed.ncbi.nlm.nih.gov/35346091/) | *Genotype-Phenotype correlations of SCARB2* | Review | F006, F014 | C-terminal variant location affects onset age |
| [34337151](https://pubmed.ncbi.nlm.nih.gov/34337151/) | *Miglustat Therapy for AMRF* | Case report | F007, F011 | SRT halts myoclonus; early mortality framing |
| [21782476](https://pubmed.ncbi.nlm.nih.gov/21782476/) | *PME with nephropathy C1q due to SCARB2* | Case report (2 sibs) | F002, F007 | SRT improvement; C1q nephropathy |
| [17485520](https://pubmed.ncbi.nlm.nih.gov/17485520/) | *LIMP-2…cardiac intercalated disc* | Mouse model | F008 | Non-lysosomal cardiac role |
| [24389070](https://pubmed.ncbi.nlm.nih.gov/24389070/) | *LIMP-2: new player in lysosome pathology* | Review | F008 | Enterovirus receptor; pleiotropy |
| [19933215](https://pubmed.ncbi.nlm.nih.gov/19933215/) | *Disease-causing LIMP-2 mutations…binding to β-GC* | In vitro | F012 | ER retention; coiled-coil binding domain |
| [22537104](https://pubmed.ncbi.nlm.nih.gov/22537104/) | *Critical histidine…pH-sensitive binding* | In vitro | F012 | pH-dependent V-ATPase release mechanism |
| [33343627](https://pubmed.ncbi.nlm.nih.gov/33343627/) | *Distinctive EEG Patterns in SCARB2 PME* | Case report | F010 | Fixation-off phenomenon; REM parasagittal spikes |
| [33772352](https://pubmed.ncbi.nlm.nih.gov/33772352/) | *Novel homozygous splice-site in SCARB2* | Case report | F010 | Molecular confirmation via WES (c.423+1G>A) |
| [37529812](https://pubmed.ncbi.nlm.nih.gov/37529812/) | *AMRF Case Report with Bioinformatic Annotations* | Case report | F013, F014 | Consanguinity; polyneuropathy |

**Evidence source distinction:** Human clinical (18308289, 18424452, 15364701, 22050460, 35346091, 34337151, 21782476, 33343627, 33772352, 37529812); mouse model (12620969, 38635907, 40639771, 17485520); in vitro (19933215, 22537104); computational/constraint (gnomAD for F009).

---

## Section-by-Section Data Summary

### 1. Disease Information
AMRF is an autosomal recessive cerebro-renal lysosomal disorder combining progressive myoclonus epilepsy with collapsing FSGS/renal failure. Identifiers: MONDO:0009699; OMIM #254900 (EPM4); ORPHA:163703. Synonyms: EPM4; progressive myoclonic epilepsy 4 with or without renal failure; myoclonus-nephropathy syndrome; action myoclonus–renal failure syndrome. Information is aggregated from disease-level resources plus small clinical case series/reports (individual patients).

### 2. Etiology
Primary cause is purely genetic: biallelic LoF variants in *SCARB2* (F001, F014). Genetic risk factor: two pathogenic *SCARB2* alleles; consanguinity elevates risk (F014). No environmental, infectious, toxic, lifestyle risk or protective factors are established. C-terminal variant location is the only identified modifier of onset (F006). No meaningful gene–environment interaction is documented in humans, though the mouse gut-dysbiosis/vitamin-E axis (F003) hints at a diet-modifiable secondary pathway.

### 3. Phenotypes
| Phenotype | Type | HPO | Onset | Progression | Frequency |
|---|---|---|---|---|---|
| Action myoclonus | Clinical sign | HP:0001336 | mean 21.7 y | Progressive/disabling | Near-universal |
| Tremor | Clinical sign | HP:0002345 | mean 19.8 y | Progressive | Common (often first) |
| Ataxia / cerebellar signs | Clinical sign | HP:0001251 | Young adult | Progressive | Common |
| Generalized seizures | Clinical sign | HP:0002197 | mean 22.7 y | Episodic | Most cases (infrequent seizures) |
| Photosensitivity | Neurophysiologic | HP:0007000 | Young adult | — | Pronounced |
| Proteinuria/FSGS | Lab/pathology | HP:0000097 | ages 9–30 | Progressive → renal failure | ~universal in AMRF; absent in renal-sparing PME |
| Peripheral neuropathy | Clinical sign | HP:0009830 | Variable | Progressive | Variable |
| Preserved cognition | (Negative) | — | — | Stable | Characteristic |

QoL impact is severe due to disabling myoclonus, dysphagia, and dialysis dependence.

### 4. Genetic/Molecular
Causal gene *SCARB2* (HGNC:10534; OMIM *602257). Variant types: nonsense (W178X), frameshift (p.N45MfsX88), splice-site (c.423+1G>A), missense—all loss-of-function; classified pathogenic/likely pathogenic under ACMG. gnomAD: LoF-tolerant (LOEUF 0.67), consistent with recessive inheritance (F009). Germline origin. Functional consequence: loss of function via ER retention (F012). No established modifier genes beyond variant position; no epigenetic mechanism or chromosomal abnormality implicated.

### 5. Environmental
Not applicable—no environmental, lifestyle, or infectious cause. (Note: LIMP-2 is an enterovirus receptor, but this is unrelated to AMRF causation — F008.)

### 6. Mechanism
See Mechanistic Model above (F004, F012, F013).

### 7. Anatomical Structures
Primary organs: brain (cerebral/cerebellar cortex — UBERON:0000956/0002129) and kidney (glomerulus — UBERON:0000074). Secondary: peripheral nerve (UBERON:0000044). Cells: neurons (CL:0000540), podocytes (CL:0000653). Subcellular: lysosome (GO:0005764), ER (GO:0005783). Bilateral/symmetric involvement (F013).

### 8. Temporal Development
Onset: adolescence–young adulthood, insidious/chronic. Course: relentlessly progressive; proteinuria → renal failure within 0–8 years; myoclonus progressively disabling. No spontaneous remission. Lifelong (F005, F011).

### 9. Inheritance and Population
Autosomal recessive; ultra-rare (<1/1,000,000); ~1:1 sex ratio; consanguinity/founder effects in some kindreds. Carriers unaffected (F009, F014). Penetrance of the neurological phenotype is high; renal penetrance is incomplete/variable (F006).

### 10. Diagnostics
Cortical-myoclonus electrophysiology (giant SEPs, photosensitivity, EEG–EMG coherence, fixation-off phenomenon, REM parasagittal spikes); urinalysis/renal biopsy (collapsing FSGS, C1q); molecular *SCARB2* testing (WES/panel/single-gene) as gold standard; fibroblast (not leukocyte) GCase assay (F010).

### 11. Outcome/Prognosis
Progressive, disabling, early mortality; historically fatal from renal failure, now neurological. Cognition preserved. No 5-year survival figures established for this ultra-rare disease (F011).

### 12. Treatment
Symptomatic: antimyoclonic/antiseizure drugs (valproate, levetiracetam, piracetam, clonazepam, perampanel), renal replacement therapy. Emerging: SRT with miglustat (F007), vitamin E repletion (F007, F015). No approved disease-modifying therapy.

### 13. Prevention
Genetic counseling, carrier/cascade testing, prenatal/PGD; proteinuria surveillance; dialysis/transplant; vitamin E (F015).

### 14. Other Species / Natural Disease
Mouse (*Mus musculus*, NCBI:txid10090) *Scarb2* ortholog; knockout models are the principal natural/experimental analog (F003). No naturally occurring companion-animal AMRF documented in the reviewed literature.

### 15. Model Organisms
Mouse *Scarb2/Limp2* knockout — recapitulates peripheral neuropathy, hydronephrosis, deafness, cortical inclusions, and (with aging) vitamin-E-deficient neurodegeneration; validated therapeutic rescue with vitamin E/FXR inhibition (F003). Limitation: mice show prominent hydronephrosis/deafness not central to human AMRF and less pronounced glomerulosclerosis, so the model captures the neurological and lysosomal biology better than the human collapsing-FSGS renal phenotype.

---

## Limitations and Knowledge Gaps

1. **No natural history cohort with survival statistics.** Because AMRF is ultra-rare (only dozens of reported cases), there are no Kaplan–Meier survival curves, formal prevalence/incidence figures, or validated prognostic models; prognosis is inferred from small series and case reports.
2. **Renal phenotype in the mouse is incomplete.** The knockout emphasizes hydronephrosis, deafness, and neuropathy rather than the collapsing FSGS central to human AMRF, limiting mechanistic study of the podocyte injury pathway.
3. **GlcSph toxicity is demonstrated in mouse tissue, not directly in human AMRF brain/kidney.** The step linking GlcSph accumulation to neuronal/podocyte death is inferred for humans (F004).
4. **Therapeutic evidence is anecdotal.** Miglustat and vitamin E data derive from single case reports and mouse studies; no controlled trials exist.
5. **Incomplete penetrance of the renal arm is unexplained** beyond the C-terminal variant correlation (F006); the modifiers determining whether a patient develops renal failure are unknown.
6. **Epigenetic, transcriptomic, proteomic, and single-cell profiling of human AMRF tissue is essentially absent** from the reviewed literature.

## Proposed Follow-up Experiments / Actions

1. **Establish an international AMRF registry** to derive natural-history data (age-specific survival, renal-vs-neurological mortality, penetrance of the renal phenotype).
2. **Podocyte-specific or conditional *Scarb2* knockout / patient iPSC-derived podocyte and cortical-neuron models** to dissect the branched neuro-renal injury and test whether GlcSph reduction rescues each cell type.
3. **Prospective trial (or n-of-1 protocols) of miglustat SRT** in genetically confirmed AMRF, with GlcSph as a pharmacodynamic biomarker in CSF/plasma.
4. **Test vitamin E repletion and FXR modulation in human patients**, translating the mouse gut-dysbiosis/malabsorption finding, with serum vitamin E and neuropathy endpoints.
5. **Systematic genotype–phenotype study** correlating variant position (especially C-terminal), residual GCase activity, and GlcSph levels with renal-arm penetrance and onset age.
6. **Develop plasma GlcSph as a diagnostic/monitoring biomarker**, potentially resolving the leukocyte-assay pitfall and enabling earlier diagnosis.
7. **Cascade carrier screening and reproductive counseling protocols** for consanguineous kindreds with known *SCARB2* variants.

---

*Report compiled from 15 confirmed findings across 5 investigation iterations and 36 reviewed papers. Evidence types are distinguished as human clinical, mouse model, in vitro, and computational throughout.*


## Artifacts

- [OpenScientist final report](Action_Myoclonus-Renal_Failure_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Action_Myoclonus-Renal_Failure_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.
