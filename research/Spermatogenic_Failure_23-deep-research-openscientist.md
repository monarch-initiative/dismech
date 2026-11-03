---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-17T01:16:08.932449'
end_time: '2026-10-17T01:33:29.502018'
duration_seconds: 1040.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 23
  mondo_id: MONDO:0054727
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_23-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_23-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 23
- **MONDO ID:** MONDO:0054727 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 23** covering all of the
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

# Spermatogenic Failure 23 (SPGF23 / TEX14): Comprehensive Disease Characteristics Report

**Disease:** Spermatogenic Failure 23 (SPGF23)
**MONDO ID:** MONDO:0054727 · **OMIM:** #617707 · **Causal gene:** *TEX14* (MIM 605792)
**Category:** Mendelian, autosomal recessive
**Report date:** 2026-10-17

---

## Summary

**Spermatogenic Failure 23 (SPGF23) is a rare, autosomal-recessive Mendelian form of non-obstructive azoospermia (NOA) caused by biallelic loss-of-function mutations in *TEX14* (testis-expressed gene 14), located on chromosome 17q22.** TEX14 encodes a 1,497-amino-acid, testis-restricted inactive serine/threonine (pseudo)kinase that serves as the essential structural scaffold of germ-cell **intercellular bridges (ICBs)** — stable cytoplasmic channels that connect developing male germ cells into a functional syncytium. When TEX14 is lost, these bridges fail to form, spermatogenesis arrests at the pachytene/meiotic stage (a "maturation arrest" histology), no mature spermatozoa are produced, and the affected man is azoospermic and infertile.

The molecular mechanism is well defined. TEX14 carries a conserved **GPPX₃Y motif** that binds the midbody protein **CEP55** with high affinity, competitively excluding the ESCRT-recruiting proteins ALIX (PDCD6IP) and TSG101. This converts what would be a transient cytokinetic midbody into a permanent intercellular bridge, arresting abscission so that daughter germ cells remain connected. These bridges enable cytoplasmic sharing of mRNAs and proteins required to complete meiotic DNA replication, chromosome synapsis, meiotic double-strand-break repair, and transposon repression. Loss of the bridges therefore produces downstream meiotic failure and genome-integrity defects, culminating in germ-cell arrest and azoospermia. The phenotype is strikingly **male-specific**: female *Tex14*-null mice lack embryonic ICBs yet remain fertile.

SPGF23 is a non-lethal, non-progressive, isolated reproductive disorder with no systemic features. Diagnosis relies on semen analysis (azoospermia), hormonal/karyotype workup to exclude other causes, and gene-panel or exome sequencing identifying biallelic *TEX14* variants; testicular histology shows meiotic/maturation arrest. There is no disease-modifying therapy. Management centers on assisted reproduction via microdissection testicular sperm extraction (micro-TESE) with intracytoplasmic sperm injection (ICSI); however, because SPGF23 causes complete (pre-spermatid) meiotic arrest, the probability of recovering usable spermatozoa is low. Genetic counseling is the principal preventive intervention.

---

## 1. Disease Information

**Overview.** SPGF23 is an inherited male infertility disorder defined by non-obstructive azoospermia (absence of sperm in the ejaculate due to failed sperm production, not blockage) resulting from an intrinsic germ-cell defect. The spermatogenic program initiates normally through spermatogonial amplification and entry into meiosis but halts before the completion of the first meiotic division, so post-meiotic spermatids and spermatozoa are absent or severely depleted.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #617707 (Spermatogenic failure 23) |
| OMIM (gene) | 605792 (*TEX14*) |
| MONDO | MONDO:0054727 |
| Gene (NCBI) | 56155 (*TEX14*) |
| UniProt | Q8IWB6 |
| HGNC | *TEX14* |
| Cytoband | 17q22 |
| Mouse ortholog | *Tex14* (MGI) |

**Synonyms / alternative names:** Spermatogenic failure 23; SPGF23; non-obstructive azoospermia due to *TEX14* deficiency; TEX14-related maturation (meiotic) arrest. In the broader literature the condition falls under "non-obstructive azoospermia (NOA)" and "maturation arrest / meiotic arrest."

**Source of information.** The entry is derived from **aggregated disease-level resources** (OMIM, ClinVar, UniProt) combined with **individual-patient reports** (consanguineous/affected families described by Gershoni et al. 2017, Fakhro et al. 2018, and a compound-heterozygous NOA patient in [PMID: 40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/)) and **model-organism data** (*Tex14*-null mouse, [PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/)). It is not EHR-derived population data.

---

## 2. Etiology

**Primary cause — genetic.** SPGF23 is monogenic: it is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function mutations in *TEX14***. There is no environmental or infectious cause for this specific Mendelian entity; it is a germline genetic disorder of meiosis.

**Genetic risk factors.** The causal variants are LoF *TEX14* alleles. In the original human families the mutations were homozygous (consanguineous Iraqi-Jewish brothers, Gershoni et al. 2017; Jordanian brothers with maturation arrest, Fakhro et al. 2018). A recurrent **compound-heterozygous** genotype — c.802A>T (p.Ser268Cys) together with c.1021C>T (p.Arg341*) — was identified in an NOA patient with pachytene meiotic arrest and impaired intercellular-bridge assembly ([PMID: 40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/)). ClinVar (RefSeq NM_031272.5) catalogs 352 *TEX14* records, 42 classified pathogenic/likely-pathogenic, predominantly nonsense, frameshift, and canonical splice variants. Being autosomal recessive, carriers of a single allele are unaffected; **consanguinity** increases homozygosity risk and is a documented contributor.

**Environmental / lifestyle risk factors.** Not applicable as a *cause* of SPGF23 — the disorder is fully genetic. General male-fertility risk modifiers (heat, gonadotoxins, smoking) are not established disease modifiers for this entity.

**Protective factors.** None established. No protective *TEX14* alleles or environmental modifiers are known. Given complete recessive inheritance with apparently complete penetrance in males, biallelic LoF essentially determines the phenotype.

**Gene–environment interactions.** No specific GxE interactions are documented for SPGF23. This is a classical high-penetrance Mendelian disorder in which genotype is the dominant determinant.

---

## 3. Phenotypes

The phenotype is reproductive and essentially monosystemic. There are no neurological, cardiac, skeletal, or other somatic manifestations.

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO term |
|---|---|---|---|---|---|
| Non-obstructive azoospermia | Laboratory/clinical | Post-pubertal (detected in adulthood) | Severe | Obligate (defining) | HP:0011961 (Azoospermia) |
| Male infertility | Clinical | Adult | Severe | ~100% of affected males | HP:0003251 (Male infertility) |
| Meiotic / maturation arrest (spermatogenic arrest) | Histological | Adult | Severe | Characteristic | HP:0008669 (Abnormal spermatogenesis) |
| Decreased testicular size (variable) | Physical sign | Adult | Mild–moderate/variable | Variable | HP:0008734 (Decreased testicular size) |
| Normal secondary sexual characteristics / normal androgens | (Context) | — | — | Typical | — |

**Phenotype characteristics.**
- **Age of onset:** Clinically manifest in adulthood, usually at infertility workup; biologically the defect begins at the onset of meiosis after puberty.
- **Severity:** Severe with respect to fertility (complete azoospermia).
- **Progression:** Stable/non-progressive. The germ-cell arrest is fixed; it is not a degenerative disorder.
- **Frequency:** Azoospermia and infertility are obligate features in affected (biallelic) males.

**Quality-of-life impact.** The impact is confined to reproduction and its psychosocial sequelae (involuntary childlessness, distress associated with infertility). There is no effect on lifespan, physical functioning, or general health. No disease-specific QoL instrument has been applied to SPGF23 specifically.

---

## 4. Genetic / Molecular Information

**Causal gene.** *TEX14* (testis-expressed 14), OMIM 605792, NCBI Gene 56155, UniProt Q8IWB6, chromosome 17q22. Transcript reference NM_031272.5; protein 1,497 aa.

**Protein architecture (UniProt Q8IWB6):**
- Protein-kinase-like domain, residues ~227–518 — **catalytically inactive (pseudokinase)**
- Conserved **CEP55-binding GPPX₃Y motif**, residues ~795–801
- Destruction box (D-box), residues ~852–860
- Ankyrin (ANK) repeats and multiple intrinsically disordered regions
- **Testis-restricted expression**; subcellular localization to cytoplasm, midbody, and chromosome/centromere/kinetochore

**Pathogenic variant spectrum (ClinVar, NM_031272.5).** The spectrum is **dominated by loss-of-function alleles**, consistent with a LoF disease mechanism:

| Variant type | Representative alleles |
|---|---|
| Nonsense | c.2943G>A (p.Trp981Ter); c.2944C>T (p.Gln982Ter); c.3549C>A (p.Cys1183Ter); c.3168C>A (p.Tyr1056Ter); c.3652A>T (p.Arg1218Ter); c.1021C>T (p.Arg341*) |
| Frameshift | c.1380dup (p.Ala461fs); c.899dup (p.Tyr300Ter); c.3482_3486del (p.Pro1161fs); c.3625_3628del (p.Ser1209fs); c.2650_2660del (p.Ser884fs) |
| Canonical splice-site | c.137-1G>A; c.4267+1G>A; c.2576+2T>G |
| Missense (likely pathogenic) | c.1490T>C (p.Leu497Pro), in the kinase-like domain |
| Missense (VUS) | p.Pro893Arg; p.Ala64Val; p.Asn83His; p.Glu1351Gly; p.Ser268Cys |
| Conflicting | c.1003C>T (p.Arg335Ter) |

Classification follows ACMG/AMP criteria; the predominance of nonsense, frameshift, and splice variants supports **loss of function** as the mechanism. Variant counts: 352 total records, 42 pathogenic/likely-pathogenic.

**Allele frequency.** Pathogenic *TEX14* LoF alleles are individually rare in gnomAD, consistent with a recessive, reproduction-limiting disorder. Variants are **germline** in origin (somatic/COSMIC not applicable).

**Functional consequence.** **Loss of function.** Haploinsufficiency is not the issue — heterozygotes are fertile; biallelic LoF is required. The compound-heterozygous human variants disrupt intercellular-bridge assembly ([PMID: 40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/)).

**Modifier genes.** No validated clinical modifiers. Partner/pathway proteins include CEP55, ALIX (PDCD6IP), TSG101, KIF23/MKLP1, and RBM44; of these, RBM44 is dispensable (its knockout does not impair fertility; [PMID: 21364893](https://pubmed.ncbi.nlm.nih.gov/21364893/)).

**Epigenetics.** No disease-specific methylation/chromatin signature is defined for SPGF23. Notably, loss of ICBs causes **retrotransposon derepression** during meiosis — an epigenetic/genome-defense consequence rather than a primary cause ([PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/)).

**Chromosomal abnormalities.** Large 17q22 copy-number losses/gains encompassing *TEX14* exist in ClinVar/DECIPHER but are non-specific contiguous-gene CNVs, not the typical cause of isolated SPGF23. (Chromosomal causes of NOA generally — Klinefelter syndrome, Y-microdeletions — are distinct entities to exclude.)

---

## 5. Environmental Information

**Environmental factors:** None causal. SPGF23 is a Mendelian disorder.
**Lifestyle factors:** None established as modifiers of this specific genotype–phenotype.
**Infectious agents:** Not applicable — SPGF23 is not infectious or acquired.

(General NOA can have environmental/toxic contributors, but these do not apply to the *TEX14*-defined Mendelian entity.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LoF mutation in *TEX14*** → leads to absence or non-functional TEX14 protein in germ cells. *(Demonstrated — human families and mouse knockout.)*
2. **Loss of TEX14** → the conserved GPPX₃Y motif is no longer available to bind CEP55, so TEX14 cannot outcompete ALIX/TSG101 at the midbody. *(Demonstrated biochemically — [PMID: 20176808](https://pubmed.ncbi.nlm.nih.gov/20176808/); simulation [PMID: 37409705](https://pubmed.ncbi.nlm.nih.gov/37409705/).)*
3. **ESCRT abscission machinery (ALIX/TSG101) is recruited to the midbody unopposed** → cytokinetic abscission proceeds to completion instead of being arrested. *(Inferred from the competitive-binding model.)*
4. **Daughter germ cells separate rather than remaining connected** → **intercellular bridges fail to form** (undetectable by EM in TEX14-null testis). *(Demonstrated — [PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/).)*
5. **Loss of ICBs abolishes cytoplasmic sharing** of mRNAs and proteins between connected germ cells. *(Demonstrated by scRNA-seq — [PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/).)*

   Branch A → **Spermatogonial compartment:** reduced expansion of undifferentiated type-A spermatogonia and fewer differentiating A1 spermatogonia, with loss of synchrony from the type-B stage onward. *([PMID: 32438343](https://pubmed.ncbi.nlm.nih.gov/32438343/).)*

   Branch B → **Meiotic compartment:** germ cells fail to complete meiotic DNA replication, chromosome synapsis, and meiotic double-strand-break repair; retrotransposons are derepressed and retrotransposon-encoded proteins accumulate. *([PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/).)*

6. **Meiotic progression halts before completion of the first meiotic division (pachytene/meiotic maturation arrest)** → post-meiotic spermatids and spermatozoa are not produced. *(Demonstrated — [PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/).)*
7. **No mature sperm in testis/ejaculate → non-obstructive azoospermia → male infertility** (clinical manifestation). *(Demonstrated — human NOA patients.)*

```
 TEX14 biallelic LoF
          │
          ▼
 No GPPX3Y–CEP55 binding ──► ALIX/TSG101 occupy midbody ──► abscission completes
          │                                                        │
          ▼                                                        ▼
 Intercellular bridges NOT formed ◄──────────────── daughter cells separate
          │
          ├──► Branch A: spermatogonial asynchrony, fewer A1 spermatogonia
          │
          └──► Branch B: failed meiotic DNA replication / synapsis / DSB repair
                         + retrotransposon derepression
          │
          ▼
 Meiotic (pachytene) arrest ──► no spermatids/spermatozoa ──► NON-OBSTRUCTIVE AZOOSPERMIA
```

### Supporting detail

**Molecular pathway — abscission control via CEP55/ESCRT.** The central event is competition at the midbody. In somatic cells CEP55 recruits ALIX and TSG101 to activate ESCRT-III-mediated abscission. In germ cells, **TEX14's GPPX₃Y motif binds CEP55 strongly, blocking the homologous GPPX₃Y motifs of ALIX and TSG101**, thereby preventing ESCRT recruitment and arresting abscission to create a stable bridge ([PMID: 20176808](https://pubmed.ncbi.nlm.nih.gov/20176808/)). Metadynamics simulations confirm TEX14's high affinity and low dissociation rate for CEP55 outcompete ALIX ([PMID: 37409705](https://pubmed.ncbi.nlm.nih.gov/37409705/)). Reinforcing CEP55's central role, *Cep55* overexpression also causes male-specific sterility, acting through sustained PI3K/AKT signaling and loss of FOXO1 nuclear retention ([PMID: 29683733](https://pubmed.ncbi.nlm.nih.gov/29683733/)).

**Cellular processes.** Arrested cytokinetic abscission (bridge formation); cytoplasmic/organelle sharing across the germ-cell syncytium; meiotic cell-cycle progression; DNA double-strand-break repair during meiotic recombination; transposon silencing. Downstream, disrupted bridges can produce **multinucleated giant cells** and apoptosis, as seen when ICBs are destabilized by FAR1 loss ([PMID: 37039784](https://pubmed.ncbi.nlm.nih.gov/37039784/)) or YKT6 loss ([PMID: 40528727](https://pubmed.ncbi.nlm.nih.gov/40528727/)).

**Protein dysfunction.** LoF alleles (nonsense/frameshift/splice) eliminate or truncate TEX14, removing the GPPX₃Y–CEP55 scaffolding function. TEX14 is a **pseudokinase** — its kinase-like domain is catalytically inactive — so it acts structurally, not enzymatically. Beyond bridges, TEX14 also contributes to **kinetochore–microtubule attachment during mitosis**, a second function (UniProt).

**Transcriptomic / single-cell evidence.** scRNA-seq shows ICBs enable transcript sharing between connected germ cells, and integrative RNA-seq of bridge-deficient testis reveals downregulation of late germ-cell developmental genes and upregulation of ECM/cell–cell-interaction genes ([PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/); [PMID: 37039784](https://pubmed.ncbi.nlm.nih.gov/37039784/)).

**Suggested ontology terms.**
- GO biological process: GO:0007283 (spermatogenesis); GO:0045172 (intercellular bridge / germline ring canal); GO:0007140 (male meiotic nuclear division); GO:0000281/GO:0007093 (cytokinesis/abscission regulation); GO:0010526 (retrotransposon silencing).
- GO cellular component: GO:0045172 (intercellular bridge); GO:0030496 (midbody); GO:0000776 (kinetochore).
- CL cell types: CL:0000020 (spermatogonium); CL:0000017 (spermatocyte); CL:0000019 (sperm); CL:0000216 (Sertoli cell, context).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary organ:** Testis (UBERON:0000473), specifically the seminiferous tubules (UBERON:0001343) / seminiferous epithelium.
- **Body system:** Male reproductive system (UBERON:0000079). No secondary organ involvement; this is an isolated gonadal/germ-cell disorder.

**Tissue and cell level.**
- Tissue: germinal (seminiferous) epithelium.
- **Target cell populations:** male germ cells — spermatogonia (CL:0000020), spermatocytes (CL:0000017) — which fail to progress; spermatids/spermatozoa (CL:0000019) are absent. Sertoli cells (CL:0000216) remain and support the arrested epithelium.

**Subcellular level.**
- **Intercellular bridge** (GO:0045172) — the structure that fails.
- **Midbody** (GO:0030496) — site of the CEP55/TEX14/ESCRT decision.
- **Kinetochore/centromere** (GO:0000776) — TEX14's secondary mitotic site.
- Cytoplasm — the shared compartment lost when bridges fail.

**Localization / lateralization.** Bilateral (both testes affected); diffuse within the seminiferous epithelium.

---

## 8. Temporal Development

**Onset.** Biologically, the defect manifests at the first wave of meiosis after pubertal activation of spermatogenesis; clinically it is detected in adulthood during infertility evaluation. Onset pattern is **chronic/insidious** — there is no acute event.

**Progression.** The disorder is **stable and non-progressive**. Spermatogenesis is arrested at a fixed developmental checkpoint (pachytene/meiotic division) rather than degenerating over time. Disease duration is **lifelong**, but it does not worsen systemically and does not shorten life.

**Patterns.** No spontaneous remission; no treatment-induced remission of the germ-cell defect (assisted reproduction bypasses, but does not cure, the block). The relevant "critical period" is developmental — the meiotic-entry window where the bridge-dependent syncytium is required.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive** (OMIM #617707). Affected individuals are homozygous or compound heterozygous for *TEX14* LoF alleles; heterozygous carriers are unaffected and fertile.

**Penetrance / expressivity.** In males, biallelic LoF appears **highly/completely penetrant** for azoospermia. Expressivity of secondary features (e.g., testicular volume) may be variable. **No genetic anticipation** (not a repeat-expansion disorder).

**Sex-specificity.** The requirement for TEX14 is **male-specific**. TEX14 is an essential component of both male and female embryonic ICBs, yet **female *Tex14*-null mice are fertile** while males are sterile ([PMID: 19020301](https://pubmed.ncbi.nlm.nih.gov/19020301/)). Thus SPGF23 is a disorder of male fertility; female biallelic carriers would be expected to be unaffected for fertility.

**Consanguinity / founder effects.** Consanguinity is a documented contributor (homozygous cases in consanguineous families). No broad founder effect is established; individual rare alleles predominate.

**Carrier frequency.** Individual pathogenic *TEX14* alleles are rare in gnomAD; aggregate carrier frequency for SPGF23-causing biallelic genotypes is low but not precisely quantified.

**Epidemiology.** Precise prevalence/incidence of SPGF23 specifically are **not established**. Context: NOA affects ~1% of all men and is the most severe form of male infertility ([PMID: 40658795](https://pubmed.ncbi.nlm.nih.gov/40658795/)); *TEX14* is one of many monogenic causes within this heterogeneous group and accounts for a small fraction of cases. The sex ratio is effectively male-only for the fertility phenotype.

---

## 10. Diagnostics

**Clinical tests.**
- **Semen analysis:** azoospermia on ≥2 centrifuged specimens (HP:0011961). Normal ejaculate volume with azoospermia points to a non-obstructive etiology when combined with hormones/volume.
- **Hormonal profile:** FSH, LH, testosterone, inhibin B — to classify as non-obstructive (often elevated FSH) and exclude hypogonadotropic causes.
- **Imaging:** scrotal ultrasound to assess testicular volume and exclude obstruction/varicocele.
- **Biopsy/histopathology:** testicular histology shows **meiotic/maturation arrest** — germ cells present up to the spermatocyte stage, with absent or markedly reduced post-meiotic spermatids. This histological pattern is the hallmark.

**Genetic testing (the definitive diagnostic route).**
- **Karyotype** and **Y-chromosome microdeletion (AZF)** screening first, to exclude Klinefelter syndrome and AZF deletions (the commonest chromosomal causes of NOA; see [PMID: 42223426](https://pubmed.ncbi.nlm.nih.gov/42223426/), [PMID: 38511217](https://pubmed.ncbi.nlm.nih.gov/38511217/)).
- **Whole-exome sequencing (WES)** or **NOA gene panels** including *TEX14* to detect biallelic variants. WES is an effective tool for genetic diagnosis of primary male infertility ([PMID: 39267058](https://pubmed.ncbi.nlm.nih.gov/39267058/)), and targeted NGS panels increase diagnostic yield in idiopathic SPGF ([PMID: 32655042](https://pubmed.ncbi.nlm.nih.gov/32655042/)).
- Confirm biallelic status by **segregation/Sanger** and apply **ACMG/AMP** classification (biallelic LoF = pathogenic).

**Biomarkers / omics-based prognostic diagnostics.** Testicular transcript markers of post-meiotic germ cells correlate with sperm-retrieval success: post-meiotic markers are significantly reduced in maturation-arrest testes and in negative vs positive sperm-retrieval groups ([PMID: 30054974](https://pubmed.ncbi.nlm.nih.gov/30054974/)). No validated circulating biomarker is SPGF23-specific.

**Clinical criteria / differential diagnosis.** No disease-specific criteria beyond azoospermia + meiotic arrest + biallelic *TEX14*. The differential diagnosis of NOA/maturation arrest includes Klinefelter syndrome, Y-microdeletions, Sertoli-cell-only syndrome ([PMID: 41485595](https://pubmed.ncbi.nlm.nih.gov/41485595/)), and other single-gene meiotic-arrest genes (TEX11, TEX15, MEIOB, SYCP3, SOHLH1, NR5A1, SOX30, etc.) — distinguished by genetic testing.

**Screening.** Carrier/cascade screening within affected families; no population newborn screening (reproductive, non-lethal phenotype).

---

## 11. Outcome / Prognosis

**Survival / mortality.** SPGF23 does **not affect survival, life expectancy, or mortality**. It is confined to reproductive function.

**Morbidity / quality of life.** Morbidity is reproductive (infertility) and psychosocial. No physical disability.

**Disease course.** Stable, lifelong, non-progressive.

**Fertility prognosis (the key outcome).** Because SPGF23 produces a **complete meiotic (pachytene) maturation arrest** with absent spermatids, the prognosis for recovering mature spermatozoa at **micro-TESE is poor**. Post-meiotic transcript markers are significantly lower in failed sperm-retrieval cases ([PMID: 30054974](https://pubmed.ncbi.nlm.nih.gov/30054974/)), and a pre-spermatid arrest implies few or no retrievable sperm. Focal residual spermatogenesis cannot be excluded a priori, so micro-TESE may still be attempted, but with counseling about low yield.

**Prognostic factors.** Degree/completeness of the arrest; presence of any post-meiotic cells on histology; FSH and testicular volume (general NOA predictors).

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** There is no pharmacologic, gene, cell, or RNA therapy for the underlying germ-cell defect. Management is reproductive.

| Intervention | Role in SPGF23 | Suggested NCIT concept |
|---|---|---|
| **Microdissection TESE (micro-TESE)** | Surgical attempt to recover focal spermatozoa from testicular tissue; low expected yield given complete meiotic arrest | NCIT: Testicular Sperm Extraction |
| **ICSI (intracytoplasmic sperm injection)** | If any viable sperm are retrieved, used for assisted fertilization | NCIT: Intracytoplasmic Sperm Injection |
| **Donor sperm / adoption** | Family-building alternatives when retrieval fails | — |
| **Genetic counseling** | Risk assessment, family planning, cascade testing | NCIT: Genetic Counseling |

- **Pharmacotherapy / hormonal therapy:** No evidence of benefit for a structural meiotic-arrest genotype (empirical gonadotropin/antiestrogen therapy used in some NOA is not expected to overcome a *TEX14*-null block).
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None available or in trials for SPGF23.
- **Experimental:** No SPGF23-specific registered trials identified.
- **Personalized medicine:** Genotype confirms etiology and informs realistic counseling about micro-TESE yield.

---

## 13. Prevention

Because SPGF23 is a non-lethal recessive reproductive disorder, "prevention" is reproductive-genetic rather than public-health.

- **Primary prevention:** Not applicable in the conventional sense; avoidance of the affected genotype is only possible via reproductive planning.
- **Genetic / reproductive prevention:** **Carrier screening** in relatives, **genetic counseling**, and, for couples at risk, **preimplantation genetic testing (PGT)** or prenatal diagnosis to inform reproductive choices. (Note: because affected males are infertile, transmission to offspring occurs only through assisted reproduction using retrieved sperm, in which case sons could inherit a pathogenic allele.)
- **Immunization / behavioral / environmental / prophylaxis:** Not applicable.
- **Counseling:** The principal preventive intervention — informs recurrence risk and reproductive options.

---

## 14. Other Species / Natural Disease

- **Taxonomy / model species:** *Mus musculus* (NCBI Taxon 10090) is the principal model.
- **Orthologous gene:** mouse *Tex14* (MGI; NCBI Gene ortholog). The GPPX₃Y–CEP55 interaction and bridge function are **evolutionarily conserved** ([PMID: 20176808](https://pubmed.ncbi.nlm.nih.gov/20176808/)); RBM44, another bridge protein, is conserved between mouse and human ([PMID: 21364893](https://pubmed.ncbi.nlm.nih.gov/21364893/)).
- **Natural disease in other species / veterinary relevance:** No naturally occurring companion-animal or wildlife SPGF23 equivalent is documented (OMIA); intercellular bridges are, however, a conserved feature of metazoan germlines.
- **Comparative biology:** The male-specific essentiality of TEX14 (sterile males, fertile females) is conserved in mouse, mirroring the expected human sex-specific phenotype.
- **Zoonotic potential:** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

**Primary model — *Tex14*-knockout mouse.** The *Tex14⁻/⁻* mouse is the foundational and highly faithful model of SPGF23.

| Feature | Mouse *Tex14⁻/⁻* | Human SPGF23 | Concordance |
|---|---|---|---|
| Male fertility | Sterile | Infertile (azoospermic) | ✔ |
| Spermatogenic block | Halts before completion of the first meiotic division | Pachytene/meiotic maturation arrest | ✔ |
| Intercellular bridges | Absent (undetectable by EM) | Impaired bridge assembly | ✔ |
| Female fertility | Normal (fertile) | Expected unaffected (male-specific) | ✔ |
| Early meiotic markers | Expressed | — | ✔ |

- **Model types:** Mammalian (mouse) germline knockout; also conditional/cell-type-specific models of related bridge genes (e.g., *Ykt6* cKO, [PMID: 40528727](https://pubmed.ncbi.nlm.nih.gov/40528727/); *Far1* KO, [PMID: 37039784](https://pubmed.ncbi.nlm.nih.gov/37039784/)) that destabilize TEX14/ICBs secondarily.
- **Phenotype recapitulation:** Excellent — the mouse reproduces the azoospermia, meiotic arrest, and bridge loss, and provided the mechanistic framework ([PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/); [PMID: 19020301](https://pubmed.ncbi.nlm.nih.gov/19020301/)).
- **Model limitations:** Human allelic heterogeneity (missense VUS, hypomorphs, potential focal residual spermatogenesis) is not fully captured by a null mouse; the complete-null mouse may be more severe than some human hypomorphic genotypes.
- **Applications:** Dissecting bridge biology, cytoplasmic sharing (scRNA-seq), meiotic DSB repair and transposon control, and testing whether residual spermatogenesis is ever achievable.
- **Resources:** MGI / IMSR for *Tex14* alleles.

---

## Key Findings (with evidence)

### Finding 1 — Biallelic *TEX14* LoF causes SPGF23 (NOA with meiotic arrest)
OMIM #617707 attributes SPGF23 to homozygous/biallelic *TEX14* mutation (17q22), autosomal recessive. Human families (Gershoni 2017; Fakhro 2018) and a recurrent compound-heterozygous genotype (c.802A>T p.Ser268Cys; c.1021C>T p.Arg341*) in an NOA patient with pachytene arrest and impaired bridge assembly establish causality in humans. *Tex14⁻/⁻* mice are sterile with arrest before the first meiotic division.
> "we identified a novel compound heterozygous mutation in TEX14 (c.802A>T, p.S268C and c.1021C>T, p.R341*) in a patient with NOA" — [PMID: 40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/)
> "Spermatogenesis in Tex14(-/-) mice progresses through the transit amplification of diploid spermatogonia and the expression of early meiotic markers but halts before the completion of the first meiotic division" — [PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/)

### Finding 2 — TEX14 builds intercellular bridges by converting CEP55 from abscission factor to bridge component
TEX14's conserved GPPX₃Y motif binds CEP55, competitively excluding ALIX/TSG101 and the ESCRT machinery from the midbody, arresting abscission to form a stable bridge. Without TEX14, bridges are undetectable by EM. Simulations confirm TEX14's high affinity/low dissociation outcompetes ALIX; *Cep55* overexpression independently causes male sterility.
> "an evolutionarily conserved GPPX3Y motif of TEX14 binds strongly to CEP55 to block similar GPPX3Y motifs of ALIX and TSG101 from interacting and localizing to the midbody" — [PMID: 20176808](https://pubmed.ncbi.nlm.nih.gov/20176808/)
> "In the absence of TEX14, intercellular bridges are not observed by using electron microscopy and other markers" — [PMID: 16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/)

### Finding 3 — Intercellular bridges enable cytoplasmic sharing required for meiosis, DSB repair, synapsis, and transposon repression
In bridge-deficient male germ cells, meiotic DNA replication, synapsis, and DSB repair fail, and retrotransposons are derepressed with accumulation of retrotransposon-encoded proteins; scRNA-seq shows bridges enable transcript sharing. Bridge loss also causes spermatogonial asynchrony and, downstream (e.g., FAR1 loss), multinucleated giant cells.
> "germ cells fail to complete meiotic DNA replication, synapsis and meiotic double-strand break repair. They also derepress retrotransposons and accumulate retrotransposon-encoded proteins during meiosis" — [PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/)
> "intercellular bridges enable cytoplasmic exchange between connected germ cells in testes" — [PMID: 39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/)

### Finding 4 — TEX14 requirement is male-specific
TEX14 is essential for both male and female embryonic bridges (with MKLP1/KIF23), but female *Tex14*-null mice are fertile while males are sterile — making SPGF23 a male-specific fertility disorder. RBM44, another bridge protein, is dispensable.
> "TEX14 is an essential component of male and female embryonic intercellular bridges" — [PMID: 19020301](https://pubmed.ncbi.nlm.nih.gov/19020301/)

### Finding 5 — Meiotic/maturation arrest predicts low surgical sperm-retrieval yield
Post-meiotic transcript markers are significantly reduced in maturation-arrest testes and lower in negative vs positive micro-TESE groups; SPGF23's complete pachytene arrest therefore implies a low-yield retrieval prognosis.
> "Post-meiotic markers were significantly reduced in negative vs. positive sperm retrieval groups" — [PMID: 30054974](https://pubmed.ncbi.nlm.nih.gov/30054974/)

### Finding 6 — TEX14 is a 1,497-aa testis-restricted inactive (pseudo)kinase with dual bridge/kinetochore roles
UniProt Q8IWB6: pseudokinase domain (227–518), GPPX₃Y CEP55-binding motif (795–801), D-box, ANK repeats; testis-restricted; localizes to cytoplasm, midbody, and kinetochore; required for intercellular bridges and for mitotic kinetochore–microtubule attachment; disease annotation SPGF23.

### Finding 7 — ClinVar variant spectrum is LoF-dominated, confirming the LoF mechanism
352 *TEX14* records (42 P/LP); pathogenic alleles for SPGF23/NOA are overwhelmingly nonsense, frameshift, and canonical splice variants, with one likely-pathogenic kinase-domain missense (p.Leu497Pro) and several VUS missense — consistent with loss of function.
> "pathogenic biallelic TEX14 mutations are recurrent genetic etiologies of NOA in humans" — [PMID: 40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/)

---

## Mechanistic Model / Interpretation

SPGF23 is best understood as a **structural disorder of the germ-cell syncytium**. The male germline is normally a connected network: after each mitotic/meiotic division, cells deliberately *fail* abscission and remain joined by intercellular bridges. This is not a byproduct but a programmed requirement — the bridges allow haploid and diploid cells to share transcripts and proteins so that the entire clone matures synchronously and so that genome-defense (transposon silencing) and meiotic recombination machinery are adequately supplied.

TEX14 is the molecular switch that creates these bridges. By binding CEP55 at the midbody, it blocks the ESCRT abscission pathway that would otherwise sever the cells. Remove TEX14 and the switch defaults to "abscission on": cells separate, the syncytium never forms, cytoplasmic sharing is lost, and the meiotic program stalls at pachytene. The ClinVar spectrum (nonsense/frameshift/splice) and the fertile-female/sterile-male dichotomy both point to simple loss of function as the disease mechanism, with no dominant-negative or gain-of-function contribution required. The clinical endpoint — complete azoospermia with meiotic arrest — follows deterministically, which is why management is limited to assisted reproduction (with a sobering, low expected yield) and genetic counseling.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [16549803](https://pubmed.ncbi.nlm.nih.gov/16549803/) | Landmark (mouse) | TEX14 essential for bridges and male fertility; meiotic arrest phenotype |
| [20176808](https://pubmed.ncbi.nlm.nih.gov/20176808/) | Mechanism | GPPX₃Y–CEP55 binding blocks ALIX/TSG101 abscission |
| [19020301](https://pubmed.ncbi.nlm.nih.gov/19020301/) | Mechanism/sex-specificity | Embryonic bridges in both sexes; female fertile, male sterile |
| [39929837](https://pubmed.ncbi.nlm.nih.gov/39929837/) | Downstream function | Bridges required for meiosis, DSB repair, transposon repression |
| [32438343](https://pubmed.ncbi.nlm.nih.gov/32438343/) | Downstream function | Spermatogonial asynchrony without bridges |
| [37039784](https://pubmed.ncbi.nlm.nih.gov/37039784/) | Corroborating | FAR1 loss disrupts TEX14/ICBs → giant cells, arrest |
| [40528727](https://pubmed.ncbi.nlm.nih.gov/40528727/) | Corroborating | YKT6 loss destabilizes TEX14 bridges → meiotic arrest |
| [29683733](https://pubmed.ncbi.nlm.nih.gov/29683733/) | Partner biology | CEP55 overexpression → male-specific sterility |
| [37409705](https://pubmed.ncbi.nlm.nih.gov/37409705/) | Computational | Simulations confirm TEX14 outcompetes ALIX for CEP55 |
| [21364893](https://pubmed.ncbi.nlm.nih.gov/21364893/) | Contrast | RBM44 bridge protein dispensable — highlights TEX14's unique essentiality |
| [40492599](https://pubmed.ncbi.nlm.nih.gov/40492599/) | Human causality | Recurrent compound-het TEX14 in NOA; disrupted bridge assembly |
| [30054974](https://pubmed.ncbi.nlm.nih.gov/30054974/) | Prognosis | Post-meiotic markers predict sperm-retrieval success |
| [32655042](https://pubmed.ncbi.nlm.nih.gov/32655042/), [39267058](https://pubmed.ncbi.nlm.nih.gov/39267058/), [38511217](https://pubmed.ncbi.nlm.nih.gov/38511217/) | Diagnostics | NGS/WES panels for SPGF/NOA diagnostic yield |
| [41485595](https://pubmed.ncbi.nlm.nih.gov/41485595/), [40658795](https://pubmed.ncbi.nlm.nih.gov/40658795/), [42223426](https://pubmed.ncbi.nlm.nih.gov/42223426/) | Context/DDx | SCOS, NOA epidemiology, chromosomal causes to exclude |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is unquantified.** Precise prevalence, incidence, and carrier frequency for SPGF23 specifically are not established; it is a minor fraction within the broad ~1% NOA population.
2. **Allelic heterogeneity and genotype–phenotype correlation.** Most functional evidence comes from null alleles/mouse knockout. Whether human missense/hypomorphic variants (several current VUS) produce partial phenotypes or permit focal residual spermatogenesis is not resolved.
3. **Micro-TESE yield in human SPGF23 is inferred,** largely from the maturation-arrest biology and marker studies rather than direct TEX14-cohort retrieval data; actual success rates are unreported.
4. **Human histopathology detail is limited** — bridge ultrastructure in human TEX14 patients is less characterized than in mouse.
5. **No disease modifiers or therapeutics** are known; no SPGF23-specific trials exist.
6. **Female carriers/homozygotes** — the male-specific prediction rests on mouse data; human female biallelic carriers are essentially unstudied.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble a *TEX14* patient registry** to quantify prevalence, allelic spectrum, testicular histology, and **micro-TESE success rates**, directly validating the low-yield prognosis.
2. **Functional validation of VUS** (p.Pro893Arg, p.Ala64Val, p.Asn83His, p.Glu1351Gly, p.Ser268Cys, p.Leu497Pro) via CEP55-binding assays and bridge-reconstitution in cell models to reclassify per ACMG.
3. **Single-cell/spatial transcriptomics of human TEX14 testis** to confirm the bridge-dependent cytoplasmic-sharing and transposon-derepression mechanisms seen in mouse.
4. **Correlate residual post-meiotic markers** ([PMID: 30054974](https://pubmed.ncbi.nlm.nih.gov/30054974/)) with retrieval outcomes in genotype-confirmed SPGF23 to build a predictive tool.
5. **Humanized/knock-in mouse models** of specific patient missense alleles to test for hypomorphic phenotypes and any rescue windows.
6. **Genetic-counseling protocol** for families, including cascade carrier testing and reproductive options (PGT, donor sperm), given confirmed autosomal-recessive inheritance.

---

*Evidence source types represented: human clinical (families, NOA cohorts, ClinVar, OMIM, UniProt), model organism (mouse Tex14/Cep55/Far1/Ykt6), in vitro (binding/IP), and computational (metadynamics).*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_23-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_23-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054727` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **spermatogenic failure 23**
- `HP:0011961` (2 mentions) - the report calls it "Azoospermia", "Semen analysis:** azoospermia on ≥2 centrifuged specimens"; HP calls it **Non-obstructive azoospermia**
- `GO:0045172` (3 mentions) - the report calls it "intercellular bridge / germline ring canal", "intercellular bridge", "Intercellular bridge"; GO calls it **germline ring canal**
- `GO:0007093` (1 mention) - the report calls it "cytokinesis/abscission regulation"; GO calls it **mitotic cell cycle checkpoint signaling**
- `CL:0000020` (2 mentions) - the report calls it "spermatogonium", "Target cell populations:** male germ cells — spermatogonia"; CL calls it **spermatogonium**
- `UBERON:0000473` (1 mention) - the report calls it "Primary organ:** Testis"; UBERON calls it **testis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0010526` (1 mention) - the report calls it "retrotransposon silencing"; GO calls it **transposable element silencing**, and lists "retrotransposon silencing" among its other names
- `GO:0000776` (2 mentions) - the report calls it "kinetochore", "Kinetochore/centromere"; GO calls it **kinetochore**
- `CL:0000216` (2 mentions) - the report calls it "Sertoli cell, context"; CL calls it **Sertoli cell**
- `UBERON:0000079` (1 mention) - the report calls it "Body system:** Male reproductive system"; UBERON calls it **male reproductive system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0054727` - called "if available", "MONDO"
- `HP:0011961` - called "Azoospermia", "Semen analysis:** azoospermia on ≥2 centrifuged specimens"
- `GO:0045172` - called "intercellular bridge / germline ring canal", "intercellular bridge", "Intercellular bridge"
- `GO:0030496` - called "midbody", "Midbody"
- `GO:0000776` - called "kinetochore", "Kinetochore/centromere"
- `CL:0000020` - called "spermatogonium", "Target cell populations:** male germ cells — spermatogonia"

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.
