---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-18T18:27:22.668968'
end_time: '2026-09-18T18:46:14.709966'
duration_seconds: 1132.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 97 with autoinflammation (IMD97), the autosomal recessive
    inborn error of immunity caused by biallelic loss-of-function variants in PIK3CG
    encoding the p110-gamma catalytic subunit of PI3K-gamma. This is NOT TBK1 deficiency.
  mondo_id: MONDO:0030717
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_97_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_97_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 97 with autoinflammation (IMD97), the autosomal recessive inborn error of immunity caused by biallelic loss-of-function variants in PIK3CG encoding the p110-gamma catalytic subunit of PI3K-gamma. This is NOT TBK1 deficiency.
- **MONDO ID:** MONDO:0030717 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 97 with autoinflammation (IMD97), the autosomal recessive inborn error of immunity caused by biallelic loss-of-function variants in PIK3CG encoding the p110-gamma catalytic subunit of PI3K-gamma. This is NOT TBK1 deficiency.** covering all of the
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

# Immunodeficiency 97 with Autoinflammation (IMD97): A Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 97 with autoinflammation (IMD97)
**Gene:** *PIK3CG* (biallelic loss-of-function) — encodes the p110γ catalytic subunit of PI3Kγ
**Inheritance:** Autosomal recessive
**MONDO:** MONDO:0030717 | **OMIM (phenotype):** 619802 | **OMIM (gene):** 601232
**Explicit scope note:** This report concerns the *PIK3CG*-related inborn error of immunity. It is **NOT** TBK1 deficiency and is **NOT** *PIK3CD*-related Activated PI3Kδ Syndrome (APDS).

---

## Summary

Immunodeficiency 97 with autoinflammation (IMD97) is an ultra-rare, autosomal-recessive inborn error of immunity (IEI) caused by biallelic loss-of-function (LOF) variants in *PIK3CG*, the gene encoding p110γ — the sole class IB phosphoinositide 3-kinase (PI3K) catalytic subunit. p110γ is expressed predominantly in leukocytes (myeloid cells, T cells, and B cells) and is uniquely activated downstream of G-protein-coupled receptors (GPCRs, via Gβγ) and Ras to generate the second-messenger lipid PIP3. The disease was first defined in a single human patient in 2019 ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)) and independently confirmed in a second report in 2020 ([PMID: 33054089](https://pubmed.ncbi.nlm.nih.gov/33054089/)). It was formally admitted as a distinct IEI entity by the International Union of Immunological Societies (IUIS) Expert Committee.

The hallmark of IMD97 is a **paradoxical dual phenotype**: a **humoral immunodeficiency** (impaired B-cell/antibody-secreting-cell differentiation, hypogammaglobulinemia, poor vaccine responses, recurrent sinopulmonary infections, cytopenias) coexisting with **myeloid-driven autoinflammation and tissue immunopathology** (T-lymphocytic pneumonitis, colitis). Mechanistically, loss of p110γ removes a cell-intrinsic signal required for B cells to differentiate into antibody-secreting cells ([PMID: 38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/)), while simultaneously de-repressing a GSK3α/β-dependent program in macrophages and monocytes that drives excessive IL-12/IL-23 production upon Toll-like receptor (TLR) stimulation ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)). The autoinflammatory tissue disease is microbiota-dependent: *Pik3cg*-deficient mice only recapitulate the human phenotype after exposure to natural microbiota (co-housing with pet-store mice).

This report synthesizes eight confirmed findings and 54 reviewed papers across all 15 requested disease-characteristic domains. Because IMD97 is described in only a handful of patients worldwide, several clinical domains (formal epidemiology, prognosis statistics, trial-based treatment data) rest on case reports and mechanistic extrapolation rather than cohort evidence — these gaps are flagged explicitly throughout. The genetic reality of the entity is nonetheless firmly established: ClinVar curates specific pathogenic missense, nonsense, and frameshift *PIK3CG* LOF alleles to IMD97, and gnomAD constraint metrics (pLI ≈ 0) confirm heterozygous carriers are healthy — consistent with the recessive model.

---

## Key Findings

### F001 — IMD97 is caused by biallelic loss-of-function *PIK3CG* variants that abolish the p110γ catalytic subunit

The first human patient, reported by Takeda et al. (2019, *JCI*), carried **bi-allelic, loss-of-function mutations in *PIK3CG* resulting in absence of the p110γ catalytic subunit of PI3Kγ**. Her clinical history comprised **childhood-onset antibody defects, cytopenias, and T-lymphocytic pneumonitis and colitis** ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)). A second, independent report by Thian et al. (2020, *JACI*) described **germline biallelic *PIK3CG* mutations in a multifaceted immunodeficiency with immune dysregulation** ([PMID: 33054089](https://pubmed.ncbi.nlm.nih.gov/33054089/)), confirming the entity and its autosomal-recessive inheritance.

*PIK3CG* maps to chromosome **7q22.3** (GRCh38 chr7:106,865,278–106,908,980, + strand); the protein product is UniProt **P48736** (PK3CG_HUMAN); HGNC:8978; Ensembl ENSG00000105851. This finding establishes both the genetic cause (biallelic LOF, loss of p110γ) and the core clinical triad — humoral immunodeficiency, cytopenias, and organ-specific lymphocytic inflammation.

> *Evidence source:* human clinical (two independent index reports).

### F002 — PI3Kγ loss dysregulates macrophage/monocyte cytokine output (elevated IL-12/IL-23) via GSK3α/β, driving autoinflammation

Takeda et al. showed that **PI3Kγ-deficient macrophages and monocytes produce elevated inflammatory IL-12 and IL-23 in a GSK3α/β-dependent manner upon TLR stimulation** ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)). At the cellular level the patient showed reduced memory B cells, memory CD8⁺ T cells, and regulatory T (Treg) cells, with increased CXCR3⁺ tissue-homing CD4 T cells — a signature consistent with skewing toward inflammatory, tissue-infiltrating adaptive responses.

Critically, the mouse model established causality and environmental dependence: **_Pik3cg_-deficient mice recapitulate major features of human disease after exposure to natural microbiota through co-housing with pet-store mice.** This positions the myeloid IL-12/IL-23 axis as the mechanistic engine of the autoinflammatory arm of IMD97 and identifies GSK3α/β as the intermediate node de-repressed when p110γ signaling is lost.

> *Evidence source:* human clinical + model organism (mouse).

### F003 — PI3Kγ is cell-intrinsically required for B-cell differentiation into antibody-secreting cells, explaining the humoral defect

Lanahan et al. (2024, *Nature Immunology*) demonstrated that **the inborn error of immunity caused by human deficiency in PI3Kγ results in broad humoral defects**, and that **PI3Kγ functions cell-intrinsically within activated B cells in a kinase-activity-dependent manner to transduce signals required for the transcriptional program supporting differentiation of antibody-secreting cells (ASCs)** ([PMID: 38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/)). ASC fate coincides with up-regulation of *PIK3CG* expression, and differentiation is impaired when PI3Kγ is disrupted in naive B cells, in memory B cells (upon TLR activation), and in human tonsillar organoids.

This finding is pivotal because it resolves the apparent paradox of a "myeloid" kinase causing antibody deficiency: p110γ has a *direct, kinase-dependent, B-cell-intrinsic* role in the ASC transcriptional program. The humoral immunodeficiency is therefore not merely secondary to inflammation but a primary consequence of losing p110γ inside the B-cell lineage.

> *Evidence source:* human clinical + in vitro (organoid) + mechanistic.

### F004 — Structural/biophysical basis: immunodeficiency mutations at the C-terminal residue R1021 inactivate the enzyme

Rathinaswamy et al. (2021) used hydrogen–deuterium exchange mass spectrometry (HDX-MS) and biophysical assays to **define how immunodeficiency and oncogenic mutations of R1021 in the C-terminus can inactivate or activate enzyme activity** by disrupting regulatory C-terminal dynamics ([PMID: 33661099](https://pubmed.ncbi.nlm.nih.gov/33661099/)). p110γ is the class IB PI3K catalytic subunit and a key factor in immune signaling and inflammatory disease. This provides the protein-level, structural mechanism connecting a specific missense change (p.Arg1021Pro, seen in ClinVar; see F008) to loss of catalytic activity — a molecular explanation for how a single-residue change abolishes p110γ function.

> *Evidence source:* in vitro / biophysical / computational-structural.

### F005 — PI3Kγ is a myeloid/leukocyte-enriched GPCR effector controlling leukocyte trafficking, Treg homeostasis, and mucosal barrier — loss produces immunodeficiency-with-autoinflammation

Converging mouse genetics establish PI3Kγ's physiological roles: *Pik3cg*-null mice show defective myeloid/monocyte migration and recruitment ([PMID: 41794063](https://pubmed.ncbi.nlm.nih.gov/41794063/)), altered colitis susceptibility with changes in mucosal IgA/IL-10/occludin and microbiota ([PMID: 36031460](https://pubmed.ncbi.nlm.nih.gov/36031460/)), reduced neutrophil NET formation and pyroptosis ([PMID: 39024551](https://pubmed.ncbi.nlm.nih.gov/39024551/)), and roles in Treg/Th17 balance ([PMID: 36243853](https://pubmed.ncbi.nlm.nih.gov/36243853/), [PMID: 34512641](https://pubmed.ncbi.nlm.nih.gov/34512641/)). PI3Kγ is **"predominantly expressed in myeloid cells"** and **"plays a pivotal role in mediating inflammatory responses"** ([PMID: 41794063](https://pubmed.ncbi.nlm.nih.gov/41794063/)); it acts downstream of GPCRs. Takeda et al. summarize the integrated physiology: **"our results emphasize the physiological importance of PI3Kγ in restraining inflammation and promoting appropriate adaptive immune responses in both humans and mice"** ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)) — the dual role that produces simultaneous immunodeficiency and immunopathology.

> *Evidence source:* model organism (multiple) + human clinical.

### F006 — Class I PI3K framework confirms PI3Kγ as the myeloid/leukocyte class IB GPCR-activated isoform generating PIP3

A 2025 review by Shaw, Barlow-Busch & Burke frames the class I PI3K pathway as a master regulator that **"plays essential roles in controlling immune cell function, metabolism, chemotaxis and proliferation,"** noting that activation of class I PI3Ks generates the signalling lipid PIP3 ([PMID: 40925445](https://pubmed.ncbi.nlm.nih.gov/40925445/)). PI3Kγ is uniquely activated by GPCRs (via Gβγ) in leukocytes, supported by Perrotta et al. (2025) showing PI3Kγ controls CD8 T-cell trafficking ([PMID: 40595568](https://pubmed.ncbi.nlm.nih.gov/40595568/)) and structural work on the Ras–PI3Kγ interface ([PMID: 42148525](https://pubmed.ncbi.nlm.nih.gov/42148525/)). This anchors the disease within the well-characterized biochemistry of class I PI3K signaling.

> *Evidence source:* review + in vitro/structural.

### F007 — gnomAD constraint (pLI ≈ 0) confirms carrier tolerance, cementing the recessive model

gnomAD constraint metrics for *PIK3CG* (GRCh38) are: **pLI = 3.8×10⁻⁸ (≈ 0; not haploinsufficient)**, observed/expected LOF (oe_lof) = **0.54 (90% CI 0.43–0.67; LOEUF ≈ 0.67)**, missense Z = **1.53**. A pLI near zero means the gene tolerates heterozygous LOF, exactly as expected for an autosomal-recessive disorder in which single-allele carriers are clinically healthy and disease requires biallelic loss. Verified identifiers confirmed in this analysis: HGNC:8978, OMIM gene 601232, UniProt P48736, Ensembl ENSG00000105851, locus chr7:106,865,278–106,908,980 (+ strand), cytoband 7q22.3.

> *Evidence source:* population genomics (gnomAD).

### F008 — ClinVar lists specific pathogenic *PIK3CG* variants curated to IMD97, spanning missense, nonsense, and frameshift LOF

ClinVar (reference transcript NM_001282426.2) annotates the following variants to **"Immunodeficiency 97 with autoinflammation"**:

| cDNA | Protein | Type | Classification |
|---|---|---|---|
| c.145C>A | p.Arg49Ser | Missense | Pathogenic |
| c.3254A>G | p.Asn1085Ser | Missense | Pathogenic |
| c.3062G>C | p.Arg1021Pro | Missense | Pathogenic |
| c.2545C>T | p.Arg849Ter | Nonsense | Conflicting |
| c.[391_397del;456_468del] | — | Frameshift/LOF (in-cis) | Pathogenic |
| c.211A>T | p.Lys71Ter | Nonsense | Likely Pathogenic |

The **p.Arg1021Pro** variant maps to the C-terminal R1021 residue shown by Rathinaswamy et al. ([PMID: 33661099](https://pubmed.ncbi.nlm.nih.gov/33661099/)) to inactivate the kinase, directly linking a curated clinical allele to an experimentally validated inactivation mechanism.

> *Evidence source:* clinical variant database (ClinVar) + biophysical corroboration.

---

## Section-by-Section Disease Characteristics

### 1. Disease Information

**Overview.** IMD97 is an autosomal-recessive inborn error of immunity combining a primary antibody deficiency (humoral immunodeficiency) with immune dysregulation and autoinflammation. It arises from complete or near-complete loss of function of PI3Kγ, the leukocyte-enriched class IB PI3K. Affected individuals present in childhood with recurrent infections, hypogammaglobulinemia, cytopenias, and organ-specific lymphocytic inflammation (notably pneumonitis and colitis) ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/), [PMID: 33054089](https://pubmed.ncbi.nlm.nih.gov/33054089/)).

**Key identifiers.**
- **MONDO:** MONDO:0030717
- **OMIM phenotype:** 619802 (Immunodeficiency 97 with autoinflammation)
- **OMIM gene:** 601232 (*PIK3CG*)
- **HGNC:** 8978 | **UniProt:** P48736 | **Ensembl:** ENSG00000105851
- **Orphanet / ICD-11 / MeSH:** No dedicated Orphanet or specific ICD-11 code was identified for IMD97 as a distinct entity; it falls under broader categories of "combined immunodeficiency with immune dysregulation" / "primary antibody deficiency." (Data not available at the granular level — flagged as a gap.)

**Synonyms / alternative names.** PI3Kγ deficiency; p110γ deficiency; PIK3CG deficiency; human PI3Kγ inborn error of immunity; immunodeficiency-97 (IMD97).

**Information source.** Disease-level knowledge derives from **individual patient reports** (a small number of index cases) integrated with **aggregated resources** (OMIM, ClinVar, gnomAD) and **mechanistic model-organism/in vitro studies**. This is not an EHR-scale or registry-scale entity.

### 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) LOF variants in *PIK3CG* that abolish or catalytically inactivate p110γ (F001, F004, F008). The mechanism is loss of function; there is no evidence for gain-of-function or dominant-negative activity in IMD97 (contrast with *PIK3CD* APDS, which is gain-of-function).

**Genetic risk factors.** The causal variants are the disease determinants; no separate susceptibility loci or GWAS signals apply to this Mendelian condition. Consanguinity increases risk of homozygous LOF (as in recessive IEIs generally).

**Environmental factors as disease modifiers.** Uniquely, the **microbiota is a required environmental cofactor** for the autoinflammatory tissue disease: *Pik3cg*-deficient mice manifest disease only after exposure to natural microbiota ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)). Microbial/TLR stimulation is the trigger that unleashes the dysregulated IL-12/IL-23 myeloid response (F002). Infectious exposures also drive the immunodeficiency phenotype (recurrent infections due to antibody failure).

**Protective factors.** No specific protective alleles or environmental protective factors are established. Heterozygous carriers are unaffected (F007). By extrapolation, a controlled/reduced microbial burden may limit autoinflammatory flares (inferred, not demonstrated in humans).

**Gene–environment interaction.** The central G×E interaction is **genotype (biallelic *PIK3CG* LOF) × microbiota/TLR ligand exposure → GSK3-dependent IL-12/IL-23 overproduction → tissue immunopathology** (F002). This is one of the clearest documented gene–microbiota interactions among IEIs.

### 3. Phenotypes

Phenotypes are drawn primarily from the two index reports and mechanistic studies. Frequencies are qualitative given the tiny cohort.

| Phenotype | Type | HPO suggestion | Onset | Notes |
|---|---|---|---|---|
| Recurrent respiratory/sinopulmonary infections | Clinical sign | HP:0002719 (Recurrent infections); HP:0002205 (Recurrent respiratory infections) | Childhood | Consequence of antibody defect |
| Antibody deficiency / hypogammaglobulinemia | Lab abnormality | HP:0004313 (Decreased circulating antibody level); HP:0002720 (Decreased IgA) | Childhood | Broad humoral defect (F003) |
| Impaired vaccine/specific antibody responses | Lab abnormality | HP:0005387 (Impaired antibody response) | Childhood | ASC differentiation failure |
| Cytopenias | Lab abnormality | HP:0001903 (Anemia); HP:0001873 (Thrombocytopenia); HP:0001882 (Leukopenia) | Childhood | Immune dysregulation |
| T-lymphocytic pneumonitis | Clinical sign / imaging | HP:0006515 (Interstitial pneumonitis) | Childhood | Tissue immunopathology (F001) |
| Colitis / inflammatory bowel disease | Clinical sign | HP:0002583 (Colitis); HP:0002037 (Inflammatory abnormality of the GI tract) | Childhood | Microbiota-dependent (F002) |
| Reduced memory B cells | Lab abnormality | HP:0031381 (Decreased circulating memory B cell count) | — | Immunophenotype (F002) |
| Reduced regulatory T cells | Lab abnormality | (reduced Treg count) | — | Loss of tolerance |
| Autoinflammation / immune dysregulation | Clinical sign | HP:0002960 (Autoimmunity); HP:0012647 (Abnormal inflammatory response) | Childhood | Core of "autoinflammation" label |

**Severity/progression.** Variable but potentially severe (combined immunodeficiency plus organ inflammation); course is chronic with episodic inflammatory flares. **Quality of life** is substantially affected by recurrent infections and chronic pneumonitis/colitis, though formal QoL instrument data (EQ-5D/SF-36) are not available for this rare disease.

### 4. Genetic / Molecular Information

**Causal gene.** *PIK3CG* (HGNC:8978; OMIM 601232; UniProt P48736), 7q22.3. Encodes p110γ, the ~1102-residue class IB PI3K catalytic subunit, which partners with regulatory subunits p101 (*PIK3R5*) and p84/p87 (*PIK3R6*).

**Pathogenic variants (F008).** Missense (p.Arg49Ser, p.Asn1085Ser, p.Arg1021Pro), nonsense (p.Arg849Ter, p.Lys71Ter), and frameshift/complex in-cis deletion (c.[391_397del;456_468del]) alleles are curated to IMD97 in ClinVar (transcript NM_001282426.2). Classifications range from Pathogenic to Likely Pathogenic (one Conflicting).

**Variant class / consequence.** All are loss-of-function or catalytically inactivating. The p.Arg1021Pro missense allele exemplifies inactivation via disruption of C-terminal regulatory dynamics (F004).

**Allele frequency / constraint.** gnomAD: pLI ≈ 0, LOEUF ≈ 0.67, missense Z = 1.53 (F007) — heterozygous LOF is tolerated, consistent with recessive inheritance and healthy carriers. Individual pathogenic alleles are rare/private.

**Somatic vs germline.** Germline (F001, "germline biallelic *PIK3CG* mutations," [PMID: 33054089](https://pubmed.ncbi.nlm.nih.gov/33054089/)). (Note: somatic *PIK3CG* alterations arise in cancer contexts but are unrelated to IMD97.)

**Modifier genes / epigenetics / chromosomal abnormalities.** None specifically established for IMD97 (data not available). Microbiota acts as the principal non-genetic modifier (Section 2).

### 5. Environmental Information

- **Environmental/toxin factors:** None specifically implicated beyond microbial exposure.
- **Lifestyle factors:** Not established.
- **Infectious agents:** Two distinct roles. (1) *Pathogens as opportunists* — recurrent bacterial sinopulmonary infections result from the antibody defect. (2) *Commensal microbiota as an autoinflammation trigger* — TLR-sensed microbial products drive GSK3-dependent IL-12/IL-23 overproduction; the disease is microbiota-dependent in the mouse model ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)). CHEBI-relevant mediators: lipopolysaccharide (TLR ligand); PIP3 (phosphatidylinositol-3,4,5-trisphosphate, CHEBI:16618 class).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LOF variants in *PIK3CG*** (missense inactivating, nonsense, or frameshift) **lead to** absence or catalytic inactivation of the p110γ subunit of PI3Kγ (F001, F004; demonstrated).
2. Loss of p110γ **results in** failure to generate PIP3 downstream of GPCR (Gβγ) and Ras stimulation in leukocytes (F005, F006; demonstrated biochemically).
3. **Branch A — Humoral immunodeficiency:** Loss of kinase-dependent PI3Kγ signaling *within activated B cells* **results in** failure of the transcriptional program driving antibody-secreting-cell differentiation (F003; demonstrated in human cells/organoids) → **leads to** hypogammaglobulinemia, poor specific/vaccine antibody responses, reduced memory B cells → **leads to** recurrent sinopulmonary infections (clinical).
4. **Branch B — Myeloid autoinflammation:** Loss of p110γ in macrophages/monocytes **de-represses GSK3α/β** so that TLR stimulation (triggered by microbiota) **results in** excessive IL-12 and IL-23 production (F002; demonstrated) → **leads to** skewed inflammatory adaptive responses (increased CXCR3⁺ tissue-homing CD4 T cells; reduced Tregs) → **leads to** tissue-infiltrative immunopathology: T-lymphocytic pneumonitis and colitis (clinical).
5. **Environmental gate:** Branch B **requires** exposure to natural microbiota — in mice, disease manifests only after microbial exposure (F002; demonstrated). This is the G×E node.
6. **Integration:** The simultaneous loss of a positive B-cell differentiation signal (Branch A) and loss of an inflammation-restraining function in myeloid cells (Branch B) **produces** the paradoxical combined immunodeficiency-plus-autoinflammation phenotype (F005; demonstrated/inferred).

```
 PIK3CG biallelic LOF
        │
        ▼
  Loss of p110γ  ──► no PIP3 from GPCR(Gβγ)/Ras in leukocytes
        │
        ├─────────────► Branch A (B-cell intrinsic, kinase-dependent)
        │                 impaired ASC transcriptional program
        │                 → hypogammaglobulinemia, ↓memory B
        │                 → recurrent infections  [IMMUNODEFICIENCY]
        │
        └─────────────► Branch B (myeloid; needs microbiota/TLR)
                          de-repressed GSK3α/β
                          → ↑IL-12 / ↑IL-23
                          → ↑CXCR3+ tissue-homing CD4 T, ↓Treg
                          → pneumonitis, colitis  [AUTOINFLAMMATION]
```

**Molecular pathways:** class I PI3K–AKT/PIP3 signaling (KEGG hsa04151); GPCR signaling; GSK3-dependent cytokine regulation; TLR signaling; IL-12/IL-23–Th1/Th17 axis (Reactome PI3K/AKT; WikiPathways PI3K-AKT).

**Cellular processes (GO suggestions):** GO:0006954 (inflammatory response); GO:0030593 (neutrophil chemotaxis); GO:0002250 (adaptive immune response); GO:0002377 (immunoglobulin production); GO:0042113 (B cell activation); GO:0016477 (cell migration); GO:0043491 (PI3K/PKB signal transduction).

**Cell types (CL suggestions):** CL:0000235 (macrophage); CL:0000576 (monocyte); CL:0000775 (neutrophil); CL:0000236 (B cell); CL:0000786 (plasma cell/ASC); CL:0000815 (regulatory T cell); CL:0000624 (CD4⁺ T cell); CL:0000625 (CD8⁺ T cell).

**Protein dysfunction:** Loss/inactivation of p110γ catalytic (kinase) activity; C-terminal (R1021) destabilization abolishes catalysis (F004).

**Immune system involvement:** Combined — humoral immunodeficiency + autoinflammation/immune dysregulation; loss of Treg-mediated tolerance contributes.

**Molecular profiling:** Human data are limited to immunophenotyping (reduced memory B, memory CD8⁺ T, Treg; increased CXCR3⁺ CD4 T) and ex vivo cytokine assays (↑IL-12/IL-23). No large-scale transcriptomic/proteomic/metabolomic patient datasets are available (gap). Lanahan et al. used tonsillar organoids and B-cell transcriptional readouts to define the ASC program dependence ([PMID: 38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/)).

### 7. Anatomical Structures Affected

- **Organ/system level:** Immune/hematopoietic system (primary); respiratory system — lungs (pneumonitis, UBERON:0002048); digestive system — colon/intestine (colitis, UBERON:0001155 colon); lymphoid organs (spleen, lymph nodes, tonsil UBERON:0002372); bone marrow/blood (cytopenias, UBERON:0002371).
- **Tissue/cell level:** Mucosal epithelium and lamina propria of gut and airway; leukocyte populations — macrophages, monocytes, neutrophils, B cells/ASCs, CD4/CD8 T cells, Tregs (CL terms in Section 6).
- **Subcellular (GO cellular component):** Plasma membrane / inner leaflet (site of PIP3 generation, GO:0005886); cytosol (GO:0005829); p110γ is a cytoplasmic/membrane-recruited kinase.
- **Localization / lateralization:** Systemic immune involvement; organ inflammation (lung, colon) is typically **bilateral/diffuse** rather than focal.

### 8. Temporal Development

- **Onset:** Childhood-onset in reported patients (F001) — pediatric, insidious to subacute, with chronic infections and inflammatory disease.
- **Progression:** Chronic and lifelong; the autoinflammatory component is episodic/fluctuating and microbiota-driven, while the antibody deficiency is persistent.
- **Course pattern:** Chronic with relapsing inflammatory flares superimposed on a stable underlying immunodeficiency.
- **Critical periods / intervention windows:** Early diagnosis enables immunoglobulin replacement and infection prophylaxis; controlling microbial/inflammatory triggers may attenuate tissue disease (inferred).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (F001, F007). Biallelic LOF required; heterozygous carriers healthy (pLI ≈ 0).
- **Penetrance/expressivity:** Presumed high penetrance for biallelic complete LOF, with variable expressivity across the immunodeficiency–autoinflammation spectrum (small n limits precision).
- **Epidemiology:** Ultra-rare; only a handful of families reported worldwide since 2019. Formal prevalence/incidence figures are **not available** (too few cases). No dedicated Orphanet prevalence class identified.
- **Consanguinity/founder effects:** Consanguinity increases likelihood of homozygous LOF (general recessive IEI principle); no specific founder allele established.
- **Carrier frequency:** Not formally estimated; individual pathogenic alleles are rare/private in gnomAD.
- **Demographics:** No established ethnic predisposition or sex bias (the index case was female; too few patients to define a sex ratio).

### 10. Diagnostics

- **Laboratory tests:** Serum immunoglobulins (IgG/IgA/IgM — hypogammaglobulinemia); specific antibody titers/vaccine responses (impaired); complete blood count (cytopenias); lymphocyte immunophenotyping (reduced memory B, memory CD8⁺ T, Treg; increased CXCR3⁺ CD4 T). LOINC-mappable panels: quantitative immunoglobulins, lymphocyte subsets.
- **Functional immunology:** Ex vivo TLR-stimulated monocyte/macrophage cytokine assays may show elevated IL-12/IL-23 (research-grade; F002). Assessment of PIP3 generation / kinase activity is research-level.
- **Imaging:** Chest CT for interstitial/lymphocytic pneumonitis; GI imaging/endoscopy with biopsy for colitis.
- **Biopsy/pathology:** Lung and colon biopsies show lymphocytic infiltration/inflammation (F001).
- **Genetic testing (definitive):** WES or WGS, or targeted IEI/primary-immunodeficiency gene panels including *PIK3CG*, with confirmation of biallelic LOF variants; single-gene *PIK3CG* sequencing when the phenotype is recognized. ClinVar-curated alleles (F008) guide classification (ACMG/AMP). Segregation analysis confirms compound-het/homozygous state.
- **Clinical criteria / classification:** Recognized as a distinct IEI by the IUIS Expert Committee (2022 and subsequent updates; [PMID: 35748970](https://pubmed.ncbi.nlm.nih.gov/35748970/), [PMID: 41608114](https://pubmed.ncbi.nlm.nih.gov/41608114/)).
- **Differential diagnosis:** Common variable immunodeficiency (CVID) and other primary antibody deficiencies ([PMID: 34153571](https://pubmed.ncbi.nlm.nih.gov/34153571/)); combined immunodeficiencies with immune dysregulation; **APDS (PIK3CD/PIK3R1 — gain-of-function, distinct mechanism and therapy)**; other monogenic IBD/autoinflammatory syndromes. Genetic testing distinguishes IMD97 definitively.
- **Screening:** Cascade genetic testing of relatives for the familial *PIK3CG* alleles; carrier testing for reproductive counseling. No newborn-screening program targets IMD97.

### 11. Outcome / Prognosis

Formal survival/mortality statistics are **not available** given the tiny cohort. Prognosis depends on control of infections (via immunoglobulin replacement and prophylaxis) and management of organ-specific inflammation (pneumonitis, colitis). Complications include chronic lung disease, chronic/refractory colitis, cytopenia-related morbidity, and infection-related events. With early diagnosis and standard IEI supportive care, meaningful morbidity reduction is expected, but recovery potential and long-term outcomes are uncharacterized (gap). Prognostic biomarkers are not established; immunoglobulin levels, infection frequency, and inflammatory activity serve as pragmatic monitoring measures.

### 12. Treatment

No IMD97-specific approved therapy or clinical trial exists (ultra-rare disease). Management follows general IEI principles and mechanistic rationale:

| Modality | Rationale / target | NCIT suggestion |
|---|---|---|
| Immunoglobulin replacement (IVIG/SCIG) | Correct antibody deficiency, reduce infections | NCIT:C561 (Immunoglobulin Therapy) |
| Antimicrobial prophylaxis | Prevent recurrent sinopulmonary infection | NCIT:C15839 (Antibiotic Therapy) |
| Immunosuppressive/anti-inflammatory agents (e.g., corticosteroids) | Control pneumonitis/colitis autoinflammation | NCIT:C15267 (Immunosuppressive Therapy) |
| Anti-cytokine biologics (anti–IL-12/IL-23, e.g., ustekinumab) — *mechanistically rational, not validated in IMD97* | Neutralize the elevated IL-12/IL-23 axis (F002) | NCIT:C2140 (Monoclonal Antibody Therapy) |
| Hematopoietic stem cell transplantation (HSCT) — *conceptually curative for a hematopoietic-intrinsic IEI; not established for IMD97* | Replace defective leukocyte compartment | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |

**Pharmacogenomics / gene therapy:** No genotype-specific pharmacogenomic data. Gene therapy is theoretical only. Note that because p110γ has a *positive* B-cell-intrinsic role (F003) yet a *restraining* role in myeloid inflammation (F002/F005), pharmacologic PI3Kγ **inhibitors** (developed for cancer/inflammation) are **contraindicated** in this LOF disease — they would worsen it. This asymmetry is a key precision-medicine caveat.

### 13. Prevention

- **Primary prevention:** Not possible for the genetic disease; **genetic counseling** for at-risk families (recessive recurrence risk 25% per pregnancy for carrier couples), carrier testing, and reproductive options (prenatal/preimplantation genetic testing).
- **Secondary prevention:** Early molecular diagnosis via IEI gene panels/WES enables prompt immunoglobulin replacement and prophylaxis before end-organ damage.
- **Tertiary prevention:** Infection prophylaxis, vaccination-adjusted strategies (recognizing impaired antibody responses), and anti-inflammatory management to prevent progressive lung/GI damage.
- **Counseling:** Cascade testing of relatives; genetic counseling per NSGC/ACMG frameworks.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Mouse *Pik3cg* (NCBI Gene 30955) is the principal ortholog used to model the disease (NCBI Taxon 10090). Human *PIK3CG* NCBI Gene 5294 (Taxon 9606).
- **Natural disease:** No well-characterized naturally occurring *PIK3CG*-deficiency disease in companion animals or wildlife is documented (data not available); the disease is understood chiefly through engineered mouse knockouts.
- **Comparative biology:** PI3Kγ function is evolutionarily conserved; mouse and human share the GPCR-activated, leukocyte-enriched biology, though the human disease required the microbiota-humanized (pet-store co-housing) model to fully recapitulate (F002).
- **Zoonotic potential:** Not applicable (non-infectious Mendelian disorder).

### 15. Model Organisms

- **Primary model:** *Pik3cg* knockout mouse (constitutive and kinase-dead alleles). This model recapitulates myeloid trafficking defects, colitis susceptibility, altered mucosal IgA/IL-10/occludin and microbiota, neutrophil NET/pyroptosis defects, and Treg/Th17 imbalance ([PMID: 41794063](https://pubmed.ncbi.nlm.nih.gov/41794063/), [PMID: 36031460](https://pubmed.ncbi.nlm.nih.gov/36031460/), [PMID: 39024551](https://pubmed.ncbi.nlm.nih.gov/39024551/), [PMID: 36243853](https://pubmed.ncbi.nlm.nih.gov/36243853/)).
- **Key model characteristic — microbiota dependence:** *Pik3cg*-deficient mice recapitulate major features of human disease **only after exposure to natural microbiota** (co-housing with pet-store mice) ([PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/)) — a critical insight into the environmental requirement and a limitation of clean SPF-housed models.
- **In vitro / cellular models:** Human tonsillar organoids and primary B-cell systems demonstrated the cell-intrinsic ASC-differentiation defect ([PMID: 38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/)); PI3Kγ-deficient HT-29/B6 human colonic epithelial cells modeled barrier/TNFα effects ([PMID: 35725890](https://pubmed.ncbi.nlm.nih.gov/35725890/)); recombinant p110γ biophysics defined R1021 inactivation ([PMID: 33661099](https://pubmed.ncbi.nlm.nih.gov/33661099/)).
- **Resources:** MGI (mouse *Pik3cg*); IMPC/KOMP knockout lines.
- **Limitations:** SPF-housed knockouts under-represent the autoinflammatory phenotype; mouse–human differences in B-cell PI3Kγ dependence require human-cell validation.

---

## Mechanistic Model / Interpretation

IMD97 is best understood as the **loss of a single leukocyte-enriched signaling node (p110γ/PIP3) that simultaneously performs two opposite immunological jobs**: it *drives* a beneficial adaptive output (B-cell → antibody-secreting-cell differentiation) and *restrains* a harmful innate output (myeloid IL-12/IL-23 via GSK3). Removing p110γ therefore subtracts a needed "go" signal from B cells and subtracts a needed "brake" from macrophages at the same time. The result is the counterintuitive coexistence of immunodeficiency and autoinflammation in one patient.

The two arms differ in their environmental gating. **Branch A (humoral)** is cell-intrinsic and largely environment-independent — it manifests as constitutive antibody failure. **Branch B (autoinflammatory)** is conditional: it needs a microbial/TLR trigger to unmask the GSK3-dependent IL-12/IL-23 excess, which is why the mouse model only "worked" after microbiota exposure. This G×E structure explains why tissue disease is episodic and localized to microbe-rich barrier organs (lung, gut).

| Feature | Branch A: Humoral immunodeficiency | Branch B: Myeloid autoinflammation |
|---|---|---|
| Cell type | B cells / ASCs | Macrophages, monocytes |
| p110γ role lost | Positive ASC-differentiation signal (kinase-dependent) | Restraint of GSK3-driven IL-12/IL-23 |
| Environmental gate | Constitutive (intrinsic) | Requires microbiota/TLR trigger |
| Clinical output | Hypogammaglobulinemia, infections | Pneumonitis, colitis |
| Key reference | [PMID: 38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/) | [PMID: 31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/) |

A crucial translational corollary: because the phenotype is **loss-of-function**, therapeutic PI3Kγ **inhibitors** (an active oncology/inflammation drug class) would aggravate IMD97 — the opposite of the APDS situation, where PI3Kδ *inhibitors* treat a gain-of-function disease. Rational therapy for IMD97 instead targets *downstream consequences*: immunoglobulin replacement for the antibody defect, and IL-12/IL-23 blockade or general anti-inflammatory therapy for the autoinflammation.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Evidence type |
|---|---|---|---|
| [31554793](https://pubmed.ncbi.nlm.nih.gov/31554793/) | Human PI3Kγ deficiency and microbiota-dependent mouse model | Index case; GSK3-dependent IL-12/IL-23; microbiota-dependent model (F001, F002, F005) | Human + mouse |
| [33054089](https://pubmed.ncbi.nlm.nih.gov/33054089/) | Germline biallelic *PIK3CG* mutations, multifaceted immunodeficiency | Independent confirmation; germline AR (F001) | Human |
| [38961274](https://pubmed.ncbi.nlm.nih.gov/38961274/) | PI3Kγ in B cells promotes antibody responses | Cell-intrinsic ASC-differentiation defect (F003) | Human + organoid |
| [33661099](https://pubmed.ncbi.nlm.nih.gov/33661099/) | Disease mutations disrupt PI3Kγ C-terminal dynamics | R1021 inactivation mechanism (F004) | Biophysical |
| [41794063](https://pubmed.ncbi.nlm.nih.gov/41794063/) | Hematopoietic PI3Kγ / macrophage trafficking | Myeloid-predominant expression & trafficking role (F005) | Mouse |
| [36031460](https://pubmed.ncbi.nlm.nih.gov/36031460/) | PI3Kγ-KO colitis / mucosa / microbiota | Barrier & microbiota phenotypes (F005) | Mouse |
| [39024551](https://pubmed.ncbi.nlm.nih.gov/39024551/) | PI3Kγ, NETs, noncanonical pyroptosis | Neutrophil effector role (F005) | Mouse |
| [40925445](https://pubmed.ncbi.nlm.nih.gov/40925445/) | Class I PI3K regulation review | Framework: PIP3, immune function (F006) | Review |
| [40595568](https://pubmed.ncbi.nlm.nih.gov/40595568/) | PI3Kγ controls CD8 T-cell trafficking | GPCR-driven T-cell trafficking (F006) | In vitro/mouse |
| [42148525](https://pubmed.ncbi.nlm.nih.gov/42148525/) | Ras–PI3Kγ interface | Ras activation of p110γ (F006) | Structural |
| [35748970](https://pubmed.ncbi.nlm.nih.gov/35748970/) / [41608114](https://pubmed.ncbi.nlm.nih.gov/41608114/) | IUIS IEI classification updates | Formal recognition as distinct IEI | Consensus classification |
| [34153571](https://pubmed.ncbi.nlm.nih.gov/34153571/) | Monogenic causes of antibody deficiency | Differential diagnosis context (CVID vs monogenic PAD) | Review |

Supporting mouse studies across diverse disease contexts (abdominal aortic aneurysm, kidney injury, periodontitis, dengue, Zika, psoriasis) consistently show PI3Kγ as a pro-inflammatory, myeloid-trafficking effector — reinforcing that its **loss** removes both inflammatory drive and inflammatory restraint depending on cell context.

---

## Limitations and Knowledge Gaps

1. **Extremely small human cohort.** Disease definition rests on a handful of index patients; frequencies, penetrance, expressivity, epidemiology (prevalence/incidence), and prognosis statistics cannot be quantified.
2. **No formal Orphanet/ICD codes** identified for IMD97 as a standalone entity; classification currently sits under broader IEI umbrellas.
3. **No treatment trials.** All therapeutic recommendations are mechanistic/extrapolated; response rates and adverse-event data specific to IMD97 are unavailable.
4. **Molecular profiling gap.** No large-scale patient transcriptomic/proteomic/metabolomic datasets exist; mechanism relies on immunophenotyping, ex vivo cytokine assays, organoids, and mouse genetics.
5. **Model translation.** SPF mouse knockouts under-represent autoinflammation; microbiota-humanized models are needed to fully mirror human disease. Mouse–human differences in B-cell PI3Kγ dependence require ongoing human-cell validation.
6. **Variant interpretation.** Some ClinVar alleles are "Conflicting" or "Likely Pathogenic"; functional validation (as done for R1021) is not available for all variants.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** (e.g., via IUIS/ESID networks) to aggregate cases, define phenotype frequencies, natural history, and treatment responses.
2. **Systematic functional characterization** of all ClinVar *PIK3CG* alleles (kinase activity, PIP3 generation, protein stability) to firm up ACMG classifications — extending the R1021 HDX-MS approach ([PMID: 33661099](https://pubmed.ncbi.nlm.nih.gov/33661099/)).
3. **Therapeutic proof-of-concept for IL-12/IL-23 blockade** (e.g., ustekinumab) in IMD97 patients or in microbiota-humanized *Pik3cg*-KO mice, testing whether targeting the GSK3-driven cytokine axis controls pneumonitis/colitis.
4. **Single-cell multi-omics of patient B cells and myeloid cells** to map the divergent transcriptional consequences of p110γ loss (validate the ASC-program defect and the myeloid IL-12/IL-23 de-repression in humans).
5. **Evaluate HSCT outcomes** as a potentially curative option for severe combined immunodeficiency-plus-autoinflammation presentations.
6. **Explicitly document contraindication of PI3Kγ inhibitors** in clinical guidance to prevent iatrogenic worsening, given the LOF nature of the disease.
7. **Formal ontology/coding submissions** to assign dedicated Orphanet and ICD-11 identifiers and complete HPO annotation with frequencies as cohort data accrue.

---

*Report compiled from 5 investigation iterations, 8 confirmed findings, and 54 reviewed papers. Evidence types are labeled throughout: human clinical, model organism, in vitro/organoid, biophysical/structural, and population genomics.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_97_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_97_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030717` (3 mentions) - the report calls it "if available"; MONDO calls it **immunodeficiency 97 with autoinflammation**
- `HP:0005387` (1 mention) - the report calls it "Impaired antibody response"; HP calls it **Combined immunodeficiency**
- `NCIT:C561` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Ibuprofen**
- `NCIT:C15839` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **Prevention and Treatment Evaluation**
- `NCIT:C15267` (1 mention) - the report calls it "Immunosuppressive Therapy"; NCIT calls it **Laryngectomy**
- `NCIT:C2140` (1 mention) - the report calls it "Monoclonal Antibody Therapy"; NCIT calls it **Adjuvant**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0031381` (1 mention) - the report calls it "Decreased circulating memory B cell count"; HP calls it **Decreased mitogen-induced T-cell proliferation**
- `GO:0043491` (1 mention) - the report calls it "PI3K/PKB signal transduction"; GO calls it **phosphatidylinositol 3-kinase/protein kinase B signal transduction**, and lists "PI3K/PKB signal transduction" among its other names
- `CL:0000786` (1 mention) - the report calls it "plasma cell/ASC"; CL calls it **plasma cell**
- `CL:0000624` (1 mention) - the report calls it "CD4⁺ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000625` (1 mention) - the report calls it "CD8⁺ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
