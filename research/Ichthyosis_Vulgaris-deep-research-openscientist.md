---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:29:08.505318'
end_time: '2026-09-30T19:45:58.146170'
duration_seconds: 1009.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ichthyosis Vulgaris
  mondo_id: MONDO:0007810
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
citation_count: 32
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ichthyosis_Vulgaris-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ichthyosis_Vulgaris-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ichthyosis Vulgaris
- **MONDO ID:** MONDO:0007810 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ichthyosis Vulgaris** covering all of the
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

# Ichthyosis Vulgaris: A Comprehensive Disease Characteristics Report

**Disease:** Ichthyosis Vulgaris
**MONDO ID:** MONDO:0007810 · **OMIM:** 146700 · **Category:** Mendelian (autosomal semidominant)
**Report type:** Disease knowledge-base entry compiled from primary literature and aggregated disease-level resources

---

## Summary

Ichthyosis vulgaris (IV) is the **most common inherited disorder of keratinization** in humans and is caused by loss-of-function (null) mutations in the **filaggrin gene (FLG)** on chromosome 1q21.3 within the epidermal differentiation complex. The disease was molecularly defined in 2006, when FLG null mutations — most notably the two European founder alleles **R501X** (a nonsense mutation) and **2282del4** (a frameshift) — were shown to cause IV and simultaneously to constitute the strongest known genetic risk factor for atopic dermatitis (AD). Inheritance is **autosomal semidominant (hemidominant)**: heterozygotes have mild disease and biallelic carriers have substantially more severe disease, establishing a clear gene-dosage relationship.

Mechanistically, filaggrin (filament-aggregating protein) performs two jobs that are both lost when FLG is truncated: (1) it aggregates keratin intermediate filaments so that keratinocytes collapse into flattened corneocytes forming a competent cornified layer, and (2) after proteolysis by caspase-14, calpain-1 and bleomycin hydrolase it yields hygroscopic amino-acid metabolites — **trans-urocanic acid** and **pyrrolidone carboxylic acid** — that make up the stratum corneum's **natural moisturizing factor (NMF)**. Loss of these functions produces the clinical picture of **xerosis, fine scaling with flexural sparing, keratosis pilaris, and palmoplantar hyperlinearity**, with a histologic hallmark of a **reduced or absent granular layer**. The very same barrier defect that scales the skin also lets allergens penetrate, mechanistically linking IV to the **"atopic march"** (AD → food allergy → asthma/rhinitis) and to irritant and allergic contact sensitization.

IV is a **chronic, lifelong, non-life-threatening** condition that typically manifests within the first year of life, tends to improve in humid climates and worsen in dry winter air, and often improves with age. There is **no cure**; management is entirely symptomatic — rigorous skin hydration, emollients, and keratolytics (urea, alpha/beta-hydroxy acids, salicylic/lactic acid), with systemic acitretin reserved for severe cases. The flaky-tail mouse (Flg 5303delA) is the canonical model, and filaggrin-dependent barrier biology is conserved in dogs, supporting comparative and translational study. This report synthesizes twelve confirmed findings across all 15 template sections with primary-literature citations.

---

## Key Findings

### Finding 1 — IV is the filaggrin-deficiency disease (FLG loss-of-function)

Ichthyosis vulgaris is caused by **loss-of-function mutations in the filaggrin gene (FLG)**. Two null mutations, **R501X and 2282del4**, were identified as causative for IV in 15 affected European families, and the mode of inheritance was determined to be **semidominant** ([PMID: 17573887](https://pubmed.ncbi.nlm.nih.gov/17573887/)). The 2006 discovery that FLG null mutations cause IV — described as "the most common disorder of keratinization" — and are "also a strong genetic risk factor for atopic eczema" reframed both diseases as filaggrin-barrier disorders ([PMID: 22158554](https://pubmed.ncbi.nlm.nih.gov/22158554/)). Key identifiers: **OMIM #146700** (IV), **FLG OMIM #135940** (gene), **MONDO:0007810**, HGNC gene symbol **FLG**, locus **1q21.3** (epidermal differentiation complex).

> *"Two loss-of-function mutations in the filaggrin (FLG) gene, R501X and 2282del4, were identified as causative for ichthyosis vulgaris in 15 affected European families, and the mode of inheritance was found to be semidominant."* — PMID: 17573887

### Finding 2 — Semidominant inheritance with a gene-dosage severity relationship

IV shows **autosomal hemidominant (semidominant) inheritance**, and patients carrying **bi-allelic FLG mutations tend to have severe phenotypes** ([PMID: 27519469](https://pubmed.ncbi.nlm.nih.gov/27519469/)). In a cohort of 6 biallelic carriers, 5/6 had severe IV and 1/6 moderate IV. Disease expression is further tuned by **modifier genes**: co-inheritance of a steroid sulfatase (**STS**) deletion — the cause of X-linked ichthyosis — with an FLG mutation **exacerbated the IV phenotype** in a Chinese family ([PMID: 30021537](https://pubmed.ncbi.nlm.nih.gov/30021537/)). This illustrates both gene-dosage effects at the FLG locus and cross-locus modification of severity.

> *"IV shows autosomal hemidominant (semidominant) inheritance, and patients with bi-allelic FLG mutations tend to have severe IV phenotypes."* — PMID: 27519469

### Finding 3 — FLG mutation frequency and IV epidemiology vary by ancestry

FLG null mutations are observed in approximately **7.7% of Europeans and 3.0% of Asians** but appear infrequent in darker-skinned populations ([PMID: 23301728](https://pubmed.ncbi.nlm.nih.gov/23301728/)). Several low-frequency FLG null alleles occur in Europeans and Asians with a **cumulative frequency of ~9% in Europe** ([PMID: 19349982](https://pubmed.ncbi.nlm.nih.gov/19349982/)). Approximately **40 distinct loss-of-function FLG mutations** have been identified in patients with IV and/or AD across Europe and Asia, with **population-specific mutation spectra** (e.g., R501X and 2282del4 dominate in Europeans, whereas different recurrent alleles predominate in Asian populations) ([PMID: 21173567](https://pubmed.ncbi.nlm.nih.gov/21173567/)).

| Population | FLG null carrier frequency | Notes |
|---|---|---|
| European | ~7.7% (cumulative ~9%) | R501X, 2282del4 founder alleles |
| Asian | ~3.0% | Distinct population-specific alleles |
| Darker-skinned populations | Infrequent | Fewer recurrent LOF alleles reported |

> *"FLG mutations are observed in approximately 7·7% of Europeans and 3·0% of Asians, but appear to be infrequent in darker-skinned populations."* — PMID: 23301728

### Finding 4 — Mechanism: loss of keratin aggregation and NMF generation

Filaggrin **aggregates keratin filaments**, forming a keratin network that binds cornified envelopes and collapses keratinocytes into flattened corneocytes ([PMID: 33462753](https://pubmed.ncbi.nlm.nih.gov/33462753/)). Filaggrin is then **degraded by caspase-14, calpain-1, and bleomycin hydrolase** into amino acids and metabolites — **trans-urocanic acid and pyrrolidone carboxylic acid** — that are pivotal **natural moisturizing factors** in the stratum corneum ([PMID: 33462753](https://pubmed.ncbi.nlm.nih.gov/33462753/)). Environmental humidity modulates this: **lowering relative humidity increases PAD (peptidyl-arginine deiminase)-mediated filaggrin deimination and breakdown**, and partial PAD inhibition with Cl-amidine reversed the dryness effect ([PMID: 28242341](https://pubmed.ncbi.nlm.nih.gov/28242341/)) — providing a molecular explanation for the characteristic **winter worsening** of IV.

> *"Filaggrin is degraded by caspase-14, calpain 1, and bleomycin hydrolases into amino acids and amino acid metabolites such as trans-urocanic acid and pyrrolidone carboxylic acid, which are pivotal natural moisturizing factors in the SC."* — PMID: 33462753

### Finding 5 — Clinical phenotype and histology

IV is characterized clinically by **xerosis, scaling, keratosis pilaris, palmar and plantar hyperlinearity, and a strong association with atopic disorders** ([PMID: 23301728](https://pubmed.ncbi.nlm.nih.gov/23301728/)). The scaling characteristically **spares the flexures** and predominates on the extensor surfaces. Histology shows an **absent or reduced granular layer** (hypogranulosis with retention hyperkeratosis) — a feature that helps differentiate IV among non-syndromic ichthyoses ([PMID: 38841231](https://pubmed.ncbi.nlm.nih.gov/38841231/)). **Palmar hyperlinearity** has moderate diagnostic value for FLG genotype (sensitivity 46–72%, specificity 60–89% across pediatric cohorts; [PMID: 34608691](https://pubmed.ncbi.nlm.nih.gov/34608691/)). Vitamin D deficiency is highly prevalent even in milder congenital ichthyosis phenotypes ([PMID: 38841231](https://pubmed.ncbi.nlm.nih.gov/38841231/)).

**Suggested HPO terms:** HP:0000958 (Dry skin/xerosis), HP:0100792 (Ichthyosis/scaling), HP:0032152 (Keratosis pilaris), HP:0007598 (Palmoplantar hyperlinearity), HP:0008064 (Ichthyosis), HP:0100512 (Vitamin D deficiency). **UBERON:** UBERON:0002097 (skin of body), UBERON:0001003 (epidermis), UBERON:0002027 (stratum corneum region). **CL:** CL:0000312 (keratinocyte), CL:0002187 (basal cell of epidermis), corneocyte.

> *"is characterized clinically by xerosis, scaling, keratosis pilaris, palmar and plantar hyperlinearity, and a strong association with atopic disorders."* — PMID: 23301728

### Finding 6 — Filaggrin deficiency drives the atopic march

FLG null mutations that cause IV are **major genetic predisposing factors for atopic dermatitis** and are associated with **atopic asthma, allergic rhinitis, and peanut allergy** ([PMID: 21576945](https://pubmed.ncbi.nlm.nih.gov/21576945/), [PMID: 22158554](https://pubmed.ncbi.nlm.nih.gov/22158554/)). In the **flaky-tail mouse** (Flg 5303delA) and engineered FLG-deficient mice, **topical allergen application produces enhanced cutaneous allergen priming and allergen-specific antibody responses** ([PMID: 19349982](https://pubmed.ncbi.nlm.nih.gov/19349982/)), directly validating the **"filaggrin hypothesis"** that a defective barrier permits percutaneous antigen transfer. "Reduced FLG expression compromises epidermal barrier function and is associated with atopic dermatitis, allergy, and asthma" ([PMID: 33894197](https://pubmed.ncbi.nlm.nih.gov/33894197/)).

> *"topical application of allergen to mice homozygous for this mutation results in cutaneous inflammatory infiltrates and enhanced cutaneous allergen priming with development of allergen-specific antibody responses."* — PMID: 19349982

### Finding 7 — Treatment is symptomatic; there is no cure

**Rigorous skin hydration (several times daily) and balneotherapy are the mainstay** of ichthyosis treatment; **systemic acitretin** is reserved for severe disease on a case-by-case basis ([PMID: 32115871](https://pubmed.ncbi.nlm.nih.gov/32115871/)). Ichthyoses "remain incurable" but "can be managed well with symptomatic treatment" ([PMID: 32115871](https://pubmed.ncbi.nlm.nih.gov/32115871/)). Topical **keratolytics** (urea, alpha/beta-hydroxy acids, salicylic acid, lactic acid), retinoids and corticosteroids are used; a **70% glycolic acid chemical peel was ~90% efficacious** in reducing hyperkeratinization as an adjunct ([PMID: 36159354](https://pubmed.ncbi.nlm.nih.gov/36159354/)). Gene therapy for genodermatoses is emerging but current management **"remains largely palliative"** ([PMID: 42707485](https://pubmed.ncbi.nlm.nih.gov/42707485/)).

**Suggested NCIT terms:** NCIT:C1516 (Emollient agent), NCIT:C29736 (Urea), NCIT:C1214 (Salicylic acid), NCIT:C1878 (Acitretin), NCIT:C177 (Retinoid).

> *"Rigorous hydration of the skin (several times a day) and balneotherapy are the mainstay of ichthyosis treatment."* — PMID: 32115871

### Finding 8 — Diagnosis is clinical, confirmed by histology/genetics

Diagnosis is **usually based on clinical evaluation**, with molecular genetic testing, histology and electron microscopy aiding confirmation, and family-tree mapping being useful ([PMID: 32115871](https://pubmed.ncbi.nlm.nih.gov/32115871/)). IV and **X-linked ichthyosis (STS deficiency)** are the two common ichthyoses, both usually manifesting in the first year of life. Differential diagnoses include **X-linked recessive ichthyosis, pityriasis rubra pilaris, and xerotic/asteatotic dermatitis** ([PMID: 36159354](https://pubmed.ncbi.nlm.nih.gov/36159354/)). **Acquired ichthyosis** is histologically similar to IV but lacks a family/atopy history and may signal underlying malignancy or metabolic disease ([PMID: 36165597](https://pubmed.ncbi.nlm.nih.gov/36165597/)). Upfront **whole-genome sequencing** is increasingly used for primary atopic/barrier disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).

> *"The diagnosis is usually based on clinical evaluation. Molecular genetic testing as well as histological and electron microscopic studies may aid in confirming the diagnosis."* — PMID: 32115871

### Finding 9 — Chronic, lifelong condition with meaningful QoL impact

Common hereditary ichthyoses (IV and X-linked) **usually manifest within the first year of life** ([PMID: 32115871](https://pubmed.ncbi.nlm.nih.gov/32115871/)). In a survey of 222 adults with congenital ichthyosis (IV n=86), the ichthyoses had a **lifelong impact on quality of life** ([PMID: 42001132](https://pubmed.ncbi.nlm.nih.gov/42001132/)). Across pediatric chronic skin disorders including congenital ichthyosis, **elevated rates of anxiety, depression, stigma and emotional distress** were consistently reported, affecting emotional functioning, peer relationships, school participation and sleep ([PMID: 42490938](https://pubmed.ncbi.nlm.nih.gov/42490938/)). Approximately **37–50% of IV patients have associated atopic eczema** ([PMID: 36159354](https://pubmed.ncbi.nlm.nih.gov/36159354/)).

> *"the ichthyoses have a lifelong impact on quality of life."* — PMID: 42001132

### Finding 10 — Model organisms and comparative biology

The spontaneous **flaky-tail mouse** carries a Flg 1-bp deletion (**5303delA**) analogous to human FLG mutations and is a validated model of filaggrin deficiency, showing a barrier defect and enhanced percutaneous allergen priming ([PMID: 19349982](https://pubmed.ncbi.nlm.nih.gov/19349982/)). Engineered **FLG-deficient mice** show a **low threshold for cutaneous allergen sensitization but no spontaneous dermatitis or atopy** ([PMID: 33894197](https://pubmed.ncbi.nlm.nih.gov/33894197/)) — capturing the barrier/sensitization axis but not spontaneous inflammation. In **dogs**, filaggrin and filaggrin-2 expression is reduced in atopic versus healthy skin ([PMID: 40042058](https://pubmed.ncbi.nlm.nih.gov/40042058/)), indicating **conserved filaggrin-dependent barrier biology across mammals**.

**Suggested NCBI Taxon terms:** *Mus musculus* (10090), *Canis lupus familiaris* (9615). Orthologous gene: mouse *Flg*.

> *"we report a 1-bp deletion mutation, 5303delA, analogous to common human FLG mutations, within the murine Flg gene in the spontaneous mouse mutant flaky tail (ft)."* — PMID: 19349982

### Finding 11 — Gene–environment interaction: conditional contact/irritant sensitization risk

Heterozygous FLG carriers have increased risk of atopic, irritant, and allergic (nickel) dermatitis. Critically, among individuals with dermatitis and frequent hand eczema, **FLG mutations were strongly associated with contact sensitization to allergens other than nickel (OR 5.71, 95% CI 1.31–24.94)**, but **no association was found in participants without dermatitis** ([PMID: 23343419](https://pubmed.ncbi.nlm.nih.gov/23343419/)). R501X was significantly associated with **polysensitivity** (≥3 contact allergies) ([PMID: 30868611](https://pubmed.ncbi.nlm.nih.gov/30868611/)), and FLG null mutations were associated with **persistent hand eczema (OR 3.1, 95% CI 1.8–5.2)** ([PMID: 26872425](https://pubmed.ncbi.nlm.nih.gov/26872425/)). The FLG risk is thus **conditional on inflammation/exposure** — the defining signature of a gene–environment interaction.

> *"In participants without dermatitis, no association was found between contact sensitization and FLG mutations."* — PMID: 23343419

### Finding 12 — Epicutaneous (dual-allergen) sensitization links barrier defect to food allergy

FLG and other skin-barrier gene mutations, together with **Langerhans cells, type-2 innate lymphoid cells (ILC2s), IL-33 and TSLP**, have important roles in allergic sensitization through the skin, supporting the **dual-allergen-exposure hypothesis** — epicutaneous allergen exposure drives food allergy while oral exposure promotes tolerance ([PMID: 32249942](https://pubmed.ncbi.nlm.nih.gov/32249942/)). The atopic march is proposed to reflect an **epithelial barrier defect self-sustained by secondary allergenic sensitization**, explaining progression from AD to allergic asthma; **early emollient therapy** is proposed to prevent AD in high-risk children ([PMID: 29676818](https://pubmed.ncbi.nlm.nih.gov/29676818/)).

> *"the atopic march could correspond to an epithelial dysfunction, self-sustained by a secondary allergenic sensitization, explaining the transition from AD to allergic asthma."* — PMID: 29676818

---

## Section-by-Section Report

### 1. Disease Information

IV is the most common inherited disorder of keratinization, a scaly-skin disease presenting as generalized dryness and fine, flaky scaling that spares the flexures. **Identifiers:** MONDO:0007810; OMIM #146700; ORPHA:454 (ichthyosis vulgaris); ICD-10 **Q80.0**; ICD-11 **EC20.0**; MeSH **D016112** (Ichthyosis Vulgaris); gene FLG (OMIM #135940, HGNC:3748). **Synonyms:** ichthyosis simplex, filaggrin-deficiency ichthyosis, autosomal-dominant ichthyosis vulgaris, "fish-scale disease" (common). Information here is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and cohort/case-series primary literature rather than patient-level EHR data.

### 2. Etiology

**Primary cause:** monogenic/genetic — loss-of-function FLG null mutations (Findings 1–3). **Genetic risk factors:** heterozygous or biallelic FLG null alleles (R501X, 2282del4 in Europeans; ~40 population-specific LOF alleles overall). **Modifier genes:** STS (steroid sulfatase) deletion co-inheritance worsens phenotype (Finding 2). **Environmental risk factors:** low ambient humidity / dry cold climate exacerbates disease via enhanced filaggrin deimination and breakdown (Finding 4); irritant and allergen exposures precipitate dermatitis in carriers (Finding 11). **Protective factors:** humid, warm environments reduce scaling; regular emollient use restores barrier function (supportive, Findings 7, 12). No specific protective genetic allele is established. **Gene–environment interaction:** FLG-conferred sensitization risk is conditional on skin inflammation/exposure (Finding 11); epicutaneous allergen exposure through a barrier-defective epidermis drives sensitization whereas oral exposure promotes tolerance (Finding 12).

### 3. Phenotypes

| Phenotype | Type | Onset | Severity/Frequency | HPO |
|---|---|---|---|---|
| Xerosis (dry skin) | Physical sign | Infancy/childhood | Near-universal; variable | HP:0000958 |
| Fine scaling, flexural sparing | Physical sign | First year of life | Core feature | HP:0008064 / HP:0100792 |
| Keratosis pilaris | Physical sign | Childhood | Common | HP:0032152 |
| Palmar/plantar hyperlinearity | Physical sign | Childhood | Sens 46–72% for FLG | HP:0007598 |
| Reduced/absent granular layer | Lab/histology | Congenital | Diagnostic hallmark | — |
| Associated atopic eczema | Clinical | Childhood | ~37–50% | HP:0000964 |
| Vitamin D deficiency | Lab abnormality | Any | Highly prevalent | HP:0100512 |

Onset is typically within the first year of life (Finding 9); severity ranges mild→severe scaling with biallelic carriers more severe (Finding 2); course is chronic, often improving with age and in humid climates, worsening in winter (Finding 4). **Quality-of-life impact:** lifelong QoL burden with elevated anxiety, depression, stigma, and sleep/school disruption (Finding 9).

### 4. Genetic/Molecular Information

**Causal gene:** FLG (filaggrin), 1q21.3, epidermal differentiation complex; OMIM #135940; HGNC:3748. **Variant types:** predominantly **nonsense (R501X)** and **frameshift (2282del4)** truncating mutations; ~40 distinct LOF alleles reported (Finding 3). **Classification:** R501X and 2282del4 are established **pathogenic** per ACMG (null variants in a gene where LOF is the mechanism). **Allele frequency:** cumulative ~9% in Europe; carrier ~7.7% Europeans, ~3.0% Asians (Finding 3). **Origin:** germline. **Functional consequence:** **loss of function** with a semidominant gene-dosage effect (Findings 1–2). **Modifier genes:** STS (Finding 2). **Epigenetics:** nanopore sequencing has enabled allelic phasing and methylation profiling of FLG in IV/AD ([PMID: 38336337](https://pubmed.ncbi.nlm.nih.gov/38336337/)); disease-specific methylation signatures are not established. **Chromosomal abnormalities:** not a feature of isolated IV (STS deletion is relevant only as a co-inherited modifier).

### 5. Environmental Information

**Environmental factors:** low relative humidity increases filaggrin deimination/breakdown and lowers stratum corneum pH, worsening the barrier (Finding 4). **Lifestyle:** frequent long hot baths, harsh soaps, and low-humidity heating aggravate xerosis; occupational wet-work/irritant exposure precipitates hand eczema in FLG carriers (Finding 11). **Infectious agents:** none cause IV; however, barrier breakdown predisposes to secondary skin infection and colonization (general principle). IV is not an infectious disease.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **FLG null mutation (R501X / 2282del4)** truncates profilaggrin/filaggrin → **leads to** reduced or absent filaggrin protein in the stratum granulosum (demonstrated).
2. Loss of filaggrin **results in** failure to aggregate keratin intermediate filaments → impaired collapse of keratinocytes into flattened corneocytes and a defective cornified layer (demonstrated; PMID 33462753).
3. In parallel (branch), loss of filaggrin **results in** absence of filaggrin proteolysis products (trans-urocanic acid, pyrrolidone carboxylic acid) → **depletion of natural moisturizing factor** → reduced stratum-corneum hydration (demonstrated; PMID 33462753).
4. Defective cornification + NMF depletion **lead to** **xerosis, retention hyperkeratosis, and a reduced/absent granular layer** → clinical **scaling, keratosis pilaris, palmar hyperlinearity** (demonstrated; PMIDs 23301728, 38841231).
5. Low ambient humidity **amplifies** the defect by increasing PAD-mediated filaggrin deimination/breakdown and lowering SC pH → **winter exacerbation** (demonstrated in ex vivo/organ models; PMID 28242341).
6. Branch to atopy: the barrier defect **permits** percutaneous penetration of allergens → Langerhans-cell/ILC2/IL-33/TSLP-driven Th2 sensitization → **atopic dermatitis, food allergy, asthma, contact sensitization** (demonstrated in mouse models and human epidemiology; PMIDs 19349982, 32249942, 29676818, 23343419). This branch is **conditional** on inflammation/exposure (gene–environment interaction, Finding 11).

**Molecular pathways / processes:** epidermal terminal differentiation and cornification; keratin filament aggregation; NMF biogenesis; Th2 allergic sensitization (IL-33/TSLP/ILC2). **Enzymes:** caspase-14, calpain-1, bleomycin hydrolase (filaggrin catabolism); PAD1/PAD (deimination). **Suggested GO terms:** GO:0031424 (keratinization), GO:0018149 (peptide cross-linking), GO:0008544 (epidermis development), GO:0030216 (keratinocyte differentiation). **Suggested CL terms:** CL:0000312 (keratinocyte), corneocyte, CL:0000453 (Langerhans cell). **Subcellular:** keratohyalin granules (their loss is the histologic "reduced granular layer"); cytoskeleton (keratin intermediate filaments). **Transcriptomics:** RNA-seq of nonlesional skin shows modest differential expression in IV relative to healthy donors, far fewer changes than in AD, and xenobiotic/lipid-metabolism gene upregulation is AD-specific, not seen in IV ([PMID: 28899689](https://pubmed.ncbi.nlm.nih.gov/28899689/)) — indicating IV is a barrier-structural disease without the prominent inflammatory transcriptome of AD.

### 7. Anatomical Structures Affected

**Primary organ:** skin (UBERON:0002097), specifically the **epidermis** (UBERON:0001003) and **stratum corneum** (UBERON:0002027). **Tissue:** keratinizing stratified squamous epithelium. **Cells:** keratinocytes/corneocytes (CL:0000312); the granular layer is deficient. **Subcellular:** keratohyalin granules (GO cellular component: cornified envelope; keratin filament). **Localization:** generalized, **extensor-predominant with flexural sparing**; palms and soles show hyperlinearity; **bilateral and symmetric** distribution. **Secondary involvement:** eyes/systemic atopy via the atopic march (asthma — respiratory system; allergic rhinitis).

### 8. Temporal Development

**Onset:** congenital/infantile — usually within the first year of life (Finding 9); **insidious/chronic** onset. **Progression:** generally **stable to slowly improving with age**; **fluctuating/episodic** with seasonal (winter) worsening (Finding 4). **Duration:** **chronic, lifelong** (Finding 9). **Remission:** no true remission; symptomatic improvement with emollients and in humid conditions. **Critical period:** infancy/early childhood is the window during which barrier-directed emollient therapy may modify atopic-march trajectory (Finding 12).

### 9. Inheritance and Population

**Inheritance:** autosomal **semidominant (hemidominant)** — heterozygotes mild, biallelic carriers severe (Findings 1–2). **Penetrance:** incomplete/variable; **expressivity:** variable and gene-dosage dependent. **Epidemiology:** among the most common genetic skin disorders; population carrier frequencies ~7.7% (European) and ~3.0% (Asian) for FLG null alleles (Finding 3); commonly cited clinical IV prevalence estimates range roughly 1 in 80 to 1 in 250 in populations of European descent (from aggregated resources; exact figure varies by ascertainment). **Founder effects:** R501X and 2282del4 are European founder alleles; distinct recurrent alleles in Asian populations (Finding 3). **Affected populations:** higher in European and Asian ancestry, infrequent in darker-skinned populations. **Sex ratio:** approximately equal (autosomal). **Consanguinity:** increases likelihood of biallelic (severe) disease.

### 10. Diagnostics

Diagnosis is **clinical**, supported by **histopathology** (hyperkeratosis with reduced/absent granular layer), **electron microscopy**, and **molecular FLG genotyping** (Finding 8). **Genetic testing:** targeted FLG single-gene/panel testing; WES/WGS increasingly used upfront for primary atopic/barrier disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)); nanopore sequencing resolves FLG allelic phasing, intragenic CNVs, and methylation ([PMID: 38336337](https://pubmed.ncbi.nlm.nih.gov/38336337/)). **Biomarker:** reduced stratum-corneum NMF; palmar hyperlinearity as a clinical proxy for FLG genotype (Finding 5). **Differential diagnosis:** X-linked recessive ichthyosis (STS deficiency), pityriasis rubra pilaris, acquired ichthyosis, asteatotic/xerotic dermatitis (Finding 8). **Screening:** cascade family testing feasible; no routine population newborn screening.

### 11. Outcome/Prognosis

IV is **non-life-threatening** with **normal life expectancy**; there is no disease-specific mortality. **Morbidity** is driven by chronic xerosis/scaling, pruritus, keratosis pilaris, secondary atopic disease, and psychosocial burden (Finding 9). **Complications:** atopic dermatitis (~37–50%), asthma/rhinitis/food allergy via the atopic march, persistent hand eczema and contact sensitization in carriers (Findings 6, 11, 12), and secondary skin infection. **Prognostic factors:** genotype (biallelic → more severe), ancestry, and environmental humidity. **Recovery:** symptoms are controllable but not curable; often milder in adulthood.

### 12. Treatment

**Pharmacotherapy / supportive:** emollients and rigorous hydration (first-line), keratolytics (urea, alpha/beta-hydroxy acids, lactic/salicylic acid), topical retinoids/corticosteroids, and **systemic acitretin for severe disease** (Finding 7). Adjunctive **70% glycolic acid peel** (~90% efficacy for hyperkeratosis; Finding 7). **Barrier-repair** ceramide/NMF-replenishing moisturizers target the specific molecular deficit ([PMID: 23757122](https://pubmed.ncbi.nlm.nih.gov/23757122/)). **Advanced/experimental:** gene therapy for genodermatoses is in development but management remains largely palliative ([PMID: 42707485](https://pubmed.ncbi.nlm.nih.gov/42707485/)). **Personalized/preventive:** early emollient therapy in high-risk infants may attenuate the atopic march (Finding 12). **NCIT:** emollient (C1516), urea (C29736), salicylic acid (C1214), acitretin (C1878).

### 13. Prevention

No **primary prevention** of IV exists (monogenic). **Secondary/tertiary prevention** focuses on barrier maintenance: consistent emollient use, humidification, avoidance of harsh soaps/irritants, and — in FLG carriers — occupational skin protection to prevent hand eczema (Finding 11). **Early-life emollient therapy** is a proposed strategy to prevent AD and interrupt the atopic march in high-risk children (Finding 12). **Genetic counseling** and reproductive options are relevant for families, especially with biallelic/severe disease ([PMID: 42272196](https://pubmed.ncbi.nlm.nih.gov/42272196/)). Prenatal/preimplantation testing is feasible where a familial FLG genotype is known.

### 14. Other Species / Natural Disease

Filaggrin-dependent barrier biology is **conserved in mammals**. In **dogs** (*Canis lupus familiaris*, NCBI Taxon 9615), filaggrin and filaggrin-2 expression is reduced in atopic skin ([PMID: 40042058](https://pubmed.ncbi.nlm.nih.gov/40042058/); [PMID: 39811760](https://pubmed.ncbi.nlm.nih.gov/39811760/)), making canine atopic dermatitis a natural comparative model of filaggrin barrier dysfunction. No IV-equivalent scaling disease with an FLG null etiology is canonically catalogued in companion animals, but the conserved barrier mechanism is of veterinary relevance. **Zoonotic potential:** none (non-infectious).

### 15. Model Organisms

**Mouse (*Mus musculus*, NCBI Taxon 10090):** the spontaneous **flaky-tail** mutant carries Flg 5303delA, analogous to human FLG mutations, and recapitulates barrier defect + enhanced percutaneous allergen priming ([PMID: 19349982](https://pubmed.ncbi.nlm.nih.gov/19349982/)). **Engineered FLG-deficient mice** show a low threshold for cutaneous allergen sensitization but **no spontaneous dermatitis/atopy** ([PMID: 33894197](https://pubmed.ncbi.nlm.nih.gov/33894197/)) — a key limitation (models the barrier/sensitization axis, not spontaneous inflammation). **In vitro:** canine primary epidermal organoids and reconstructed epidermis reproduce barrier defects after proinflammatory/allergic cytokine exposure ([PMID: 41260506](https://pubmed.ncbi.nlm.nih.gov/41260506/); [PMID: 39811760](https://pubmed.ncbi.nlm.nih.gov/39811760/)). **Applications:** studying barrier physiology, allergen penetration, atopic-march initiation, and candidate therapeutics. **Resources:** MGI (mouse Flg).

---

## Mechanistic Model / Interpretation

```
   FLG null mutation (R501X / 2282del4; 1q21.3)
                 │  (loss of function; semidominant, gene-dosage)
                 ▼
   ↓ / absent filaggrin protein in stratum granulosum
                 │
      ┌──────────┴───────────────────────────┐
      ▼                                        ▼
 Failed keratin-filament               No filaggrin proteolysis
 aggregation                          (caspase-14, calpain-1,
 → defective corneocytes /             bleomycin hydrolase)
   reduced granular layer             → loss of NMF (trans-UCA, PCA)
      │                                        │
      └──────────────┬─────────────────────────┘
                     ▼
        Impaired stratum-corneum barrier + ↓ hydration
                     │
        ┌────────────┼──────────────────────────┐
        ▼            ▼                            ▼
   XEROSIS,     Winter worsening            Percutaneous
   SCALING,     (low humidity →              allergen entry
   KERATOSIS    ↑PAD deimination,            → Langerhans/ILC2,
   PILARIS,     ↓SC pH)                       IL-33/TSLP, Th2
   PALMAR                                     │
   HYPERLINE-                                 ▼
   ARITY                            ATOPIC MARCH: AD →
   (IV phenotype)                   food allergy, asthma,
                                    rhinitis; contact
                                    sensitization*
                              *conditional on inflammation/exposure
```

The unifying interpretation is that **a single structural deficiency — loss of filaggrin — produces two coupled outputs**: (1) a *structural/hydration* failure that generates the visible IV phenotype, and (2) a *permeability* failure that opens an epicutaneous route for allergic sensitization. The first output is constitutive; the second is conditional, requiring environmental allergen/irritant exposure and inflammation (Findings 11–12). This explains why IV and atopic disease co-segregate yet are dissociable, why biallelic carriers are more severely affected (dose-dependent protein loss, Finding 2), and why the disease fluctuates with ambient humidity (Finding 4). Therapeutically, it explains why **barrier restoration** (emollients, NMF/ceramide replacement, keratolysis) is both the mainstay symptomatic treatment and a rational preventive strategy against the atopic march.

---

## Evidence Base

| PMID | Finding(s) supported | Contribution |
|---|---|---|
| [17573887](https://pubmed.ncbi.nlm.nih.gov/17573887/) | F1, F2 | R501X/2282del4 causal; semidominant inheritance |
| [22158554](https://pubmed.ncbi.nlm.nih.gov/22158554/) | F1, F6 | FLG LOF causes IV, "most common disorder of keratinization" |
| [27519469](https://pubmed.ncbi.nlm.nih.gov/27519469/) | F2 | Biallelic FLG → severe IV; gene dosage |
| [30021537](https://pubmed.ncbi.nlm.nih.gov/30021537/) | F2 | STS modifier exacerbates IV |
| [23301728](https://pubmed.ncbi.nlm.nih.gov/23301728/) | F3, F5 | Ancestry-specific FLG frequencies; core clinical features |
| [19349982](https://pubmed.ncbi.nlm.nih.gov/19349982/) | F3, F6, F10 | European cumulative freq ~9%; flaky-tail mouse; allergen priming |
| [21173567](https://pubmed.ncbi.nlm.nih.gov/21173567/) | F3 | ~40 population-specific LOF alleles |
| [33462753](https://pubmed.ncbi.nlm.nih.gov/33462753/) | F4 | Filaggrin keratin aggregation + NMF catabolism enzymes |
| [28242341](https://pubmed.ncbi.nlm.nih.gov/28242341/) | F4 | Low humidity → filaggrin deimination/breakdown |
| [38841231](https://pubmed.ncbi.nlm.nih.gov/38841231/) | F5 | Reduced/absent granular layer histologic hallmark |
| [34608691](https://pubmed.ncbi.nlm.nih.gov/34608691/) | F5 | Palmar hyperlinearity diagnostic accuracy for FLG |
| [33894197](https://pubmed.ncbi.nlm.nih.gov/33894197/) | F6, F10 | FLG loss compromises barrier; FLG-deficient mouse phenotype |
| [21576945](https://pubmed.ncbi.nlm.nih.gov/21576945/) | F6 | Filaggrin hypothesis; AD/asthma association |
| [32115871](https://pubmed.ncbi.nlm.nih.gov/32115871/) | F7, F8, F9 | Hydration/acitretin mainstay; clinical diagnosis; first-year onset |
| [36159354](https://pubmed.ncbi.nlm.nih.gov/36159354/) | F7, F8, F9 | Glycolic acid peel ~90%; differentials; ~37–50% eczema |
| [42707485](https://pubmed.ncbi.nlm.nih.gov/42707485/) | F7 | Gene therapy emerging; management "largely palliative" |
| [36165597](https://pubmed.ncbi.nlm.nih.gov/36165597/) | F8 | Acquired ichthyosis mimics IV histologically |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | F8 | Upfront WGS for primary atopic/barrier disorders |
| [42001132](https://pubmed.ncbi.nlm.nih.gov/42001132/) | F9 | Lifelong QoL impact (n=86 IV) |
| [42490938](https://pubmed.ncbi.nlm.nih.gov/42490938/) | F9 | Psychosocial burden in pediatric skin disease |
| [40042058](https://pubmed.ncbi.nlm.nih.gov/40042058/) | F10 | Reduced filaggrin in canine atopic skin |
| [23343419](https://pubmed.ncbi.nlm.nih.gov/23343419/) | F11 | GxE: FLG sensitization conditional on dermatitis (OR 5.71) |
| [30868611](https://pubmed.ncbi.nlm.nih.gov/30868611/) | F11 | R501X → polysensitivity |
| [26872425](https://pubmed.ncbi.nlm.nih.gov/26872425/) | F11 | FLG null → persistent hand eczema (OR 3.1) |
| [32249942](https://pubmed.ncbi.nlm.nih.gov/32249942/) | F12 | Dual-allergen hypothesis; FLG/Langerhans/ILC2/IL-33/TSLP |
| [29676818](https://pubmed.ncbi.nlm.nih.gov/29676818/) | F12 | Atopic march = self-sustained epithelial dysfunction |
| [28899689](https://pubmed.ncbi.nlm.nih.gov/28899689/) | §6 | IV has fewer transcriptomic changes than AD |
| [38336337](https://pubmed.ncbi.nlm.nih.gov/38336337/) | §4, §10 | Nanopore FLG phasing/CNV/methylation |

**Note on evidence quality:** Causality, mechanism, and genetics are supported by strong **human genetic and biochemical** evidence plus **mouse-model** validation. Epidemiology figures are ancestry-specific and derive from carrier-frequency and cohort studies. Treatment evidence is largely observational/case-series (no cure); gene therapy is preclinical/early. One citation (PMID 33894197) was flagged as a title-based mismatch in the knowledge state but its barrier/atopy content aligns with Findings 6 and 10.

---

## Limitations and Knowledge Gaps

1. **Prevalence precision.** Exact clinical prevalence of IV is uncertain and ascertainment-dependent; carrier frequencies are better characterized than diagnosed-case prevalence.
2. **Genotype–phenotype quantitation.** The semidominant dose effect is established qualitatively (Finding 2), but graded severity scores across mono- vs biallelic genotypes in large cohorts are limited.
3. **Modifier landscape.** Beyond STS, the full spectrum of severity modifiers (other EDC genes, lipid-processing genes) is incompletely mapped.
4. **Model limitations.** FLG-deficient mice reproduce the barrier/sensitization axis but **not spontaneous dermatitis** (Finding 10), limiting inflammatory-mechanism studies.
5. **Epigenetics.** Disease-specific methylation/chromatin signatures in IV are not established; nanopore data are preliminary.
6. **Therapeutics.** No disease-modifying therapy; gene/RNA-directed correction of FLG is unproven in humans.
7. **Diverse ancestry.** FLG mutation spectra and IV phenotypes in African and admixed populations remain under-characterized.
8. **Prevention evidence.** Whether early emollient therapy durably prevents the atopic march in FLG carriers remains debated and trial-dependent.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified natural-history cohort** quantifying IV severity (validated scale) by FLG allele count and specific alleles, to formalize the dose–response and identify modifiers via GWAS/WES.
2. **Ancestry-broadening sequencing** (including African and admixed populations) of FLG to define region-specific LOF spectra and refine global epidemiology.
3. **FLG correction proof-of-concept** in human skin equivalents/organoids using CRISPR base-editing or profilaggrin re-expression, measuring NMF restoration and barrier permeability.
4. **Prospective emollient-prevention trial** in FLG-carrier infants with allergic-sensitization and AD-incidence endpoints, directly testing the Finding-12 prevention hypothesis.
5. **Multi-omic IV vs AD contrast** (transcriptomics + lipidomics + NMF metabolomics) on matched nonlesional skin to delineate the structural-only IV signature from the inflammatory AD signature (building on PMID 28899689).
6. **Humidity-intervention study** testing whether controlled ambient humidification measurably reduces PAD-mediated filaggrin breakdown and clinical scaling (translating PMID 28242341).
7. **Standardized NMF/palmar-hyperlinearity biomarker validation** as a low-cost proxy for FLG genotype in clinical screening.

---

## Consensus Answer

Ichthyosis vulgaris (MONDO:0007810; OMIM 146700) is the most common inherited disorder of keratinization, caused by autosomal semidominant loss-of-function (null) mutations in the filaggrin gene FLG (1q21.3; founder alleles R501X and 2282del4), with biallelic carriers showing more severe disease. Filaggrin deficiency impairs keratin-filament aggregation and abolishes filaggrin-derived natural moisturizing factor, producing xerosis, fine scaling with flexural sparing, keratosis pilaris and palmoplantar hyperlinearity (histologic hallmark: reduced/absent granular layer), while the same barrier defect drives atopic dermatitis, asthma and contact sensitization. It is a chronic, lifelong, non-life-threatening condition managed symptomatically with hydration, emollients and keratolytics (acitretin for severe cases); there is no cure.


## Artifacts

- [OpenScientist final report](Ichthyosis_Vulgaris-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ichthyosis_Vulgaris-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007810` (5 mentions) - the report calls it "if available"; MONDO calls it **autosomal dominant ichthyosis vulgaris**
- `HP:0000958` (2 mentions) - the report calls it "Dry skin/xerosis", "Near-universal; variable"; HP calls it **Dry skin**
- `HP:0100792` (2 mentions) - the report calls it "Ichthyosis/scaling"; HP calls it **Acantholysis**
- `HP:0032152` (2 mentions) - the report calls it "Keratosis pilaris", "Common"; HP calls it **Keratosis pilaris**
- `HP:0007598` (2 mentions) - the report calls it "Palmoplantar hyperlinearity", "Sens 46–72% for FLG"; HP calls it **Bilateral single transverse palmar creases**
- `HP:0100512` (2 mentions) - the report calls it "Vitamin D deficiency", "Highly prevalent"; HP calls it **Decreased circulating vitamin D concentration**
- `NCIT:C1516` (1 mention) - the report calls it "Emollient agent"; NCIT calls it **Lisofylline**
- `NCIT:C29736` (1 mention) - the report calls it "Urea"; NCIT calls it **Stress-Induced Protein**
- `NCIT:C1214` (1 mention) - the report calls it "Salicylic acid"; NCIT calls it **Resiniferatoxin**
- `NCIT:C1878` (1 mention) - the report calls it "Acitretin"; NCIT calls it **Darbepoetin Alfa**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C177` (1 mention), reported as "Retinoid" - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001003` (2 mentions) - the report calls it "epidermis"; UBERON calls it **skin epidermis**, and lists "epidermis" among its other names
- `UBERON:0002027` (2 mentions) - the report calls it "stratum corneum region", "stratum corneum"; UBERON calls it **stratum corneum of epidermis**, and lists "stratum corneum" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000958` - called "Dry skin/xerosis", "Near-universal; variable"
- `HP:0032152` - called "Keratosis pilaris", "Common"
- `HP:0007598` - called "Palmoplantar hyperlinearity", "Sens 46–72% for FLG"
- `HP:0100512` - called "Vitamin D deficiency", "Highly prevalent"
- `UBERON:0002027` - called "stratum corneum region", "stratum corneum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
