---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:39:33.121727'
end_time: '2026-10-15T02:29:26.414517'
duration_seconds: 2993.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glutathione Reductase Deficiency
  mondo_id: MONDO:0019531
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
citation_count: 14
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 17
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:11924113
  relevance_assessed: 16
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Glutathione_Reductase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glutathione_Reductase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glutathione Reductase Deficiency
- **MONDO ID:** MONDO:0019531 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glutathione Reductase Deficiency** covering all of the
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

# Glutathione Reductase Deficiency: A Comprehensive Disease Characteristics Report

**Disease:** Glutathione Reductase Deficiency (hereditary)
**MONDO ID:** MONDO:0019531
**OMIM:** 618660 (Hemolytic anemia due to glutathione reductase deficiency)
**Gene:** *GSR* (HGNC:4623), chromosome 8p12
**Category:** Mendelian, autosomal recessive
**Report date:** 2026-10-15

---

## Summary

Glutathione reductase (GR) deficiency exists in **two biologically distinct forms that must not be conflated**. The first and overwhelmingly more common form is an **acquired, riboflavin-responsive partial deficiency**: because GR requires FAD (derived from dietary riboflavin/vitamin B2) as a cofactor, dietary riboflavin insufficiency lowers measured GR activity. This form is reversible with riboflavin supplementation, affects a substantial fraction of some populations (~20–25% partial deficiency in a Saudi cohort), and is clinically benign. The second form — the subject of this report and the entity catalogued under MONDO:0019531 — is a **rare, hereditary, autosomal recessive enzymopathy** caused by biallelic loss-of-function mutations in the *GSR* gene. This hereditary form is **irreversible** (not corrected by riboflavin or FAD) and is extraordinarily rare: only 2 cases were found among >15,000 blood samples screened.

Mechanistically, GSR encodes a homodimeric, FAD-dependent, NADPH-disulfide oxidoreductase (EC 1.8.1.7; UniProt P00390) that regenerates reduced glutathione (GSH) from oxidized glutathione disulfide (GSSG). Loss of this recycling capacity cripples the GSH-dependent antioxidant defense of erythrocytes and the ocular lens, producing the clinical triad of **oxidant-triggered (favism) hemolytic anemia, cataracts, and neonatal jaundice**. Critically, the phenotype is usually **mild and episodic rather than chronic**, because a parallel, evolutionarily conserved **thioredoxin/thioredoxin-reductase (Trx/TrxR) system** partially compensates for the loss of GSSG reduction. This buffering is reflected in population genetics: *GSR* is completely loss-of-function tolerant in gnomAD (pLI ≈ 0), predicting a biallelic frequency near 1 in 4 million — consistent with the near-absence of hereditary cases in population screens.

Management is limited to **oxidant-trigger avoidance (fava beans, oxidant drugs, infection-related oxidative stress) and supportive transfusion during hemolytic crises**, mirroring the paradigm established for G6PD deficiency. There is no disease-specific pharmacotherapy, and riboflavin does not help the hereditary form. Prognosis is favorable, with described enzyme-null individuals surviving to adulthood with only episodic, trigger-related hemolysis. A striking inversion of the disease biology is that GSR has been identified as the *top cellular suppressor of ferroptosis*, making the very function lost in this deficiency an exploitable vulnerability in oncology.

---

## Key Findings

### Finding 1 — Hereditary GR deficiency is an ultra-rare autosomal recessive disorder caused by biallelic *GSR* loss-of-function mutations

Hereditary GR deficiency is defined molecularly by biallelic loss-of-function variants in *GSR* on chromosome 8p12 (also mapped to 8p21.2 in cytogenetic deletion reports). Its rarity is well documented: Kamerbeek and colleagues found hereditary GR deficiency in **only 2 cases when testing more than 15,000 blood samples** ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)).

The molecular lesions span the classic loss-of-function spectrum. In one family (presenting with favism and cataract), patients carried a **homozygous 2,246-bp deletion** such that "translated GR is expected to lack almost the complete dimerization domain, which results in unstable and inactive enzyme" ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)). A second, novel patient presenting with severe neonatal jaundice was a **compound heterozygote**, "with a premature stop codon on one allele and a substitution of glycine 330, a highly conserved residue in the superfamily of NAD(P)H-dependent disulfide reductases, into alanine on the other allele" ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)). The Gly330Ala substitution drastically impairs thermostability.

The autosomal recessive inheritance was established decades earlier in the landmark consanguineous family of Loos et al., where "a virtually complete absence of glutathione reductase activity was found in the erythrocytes of all three children (one male, two females) from a consanguineous marriage" ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)), with intermediate parental enzyme values — the classic signature of recessive inheritance.

### Finding 2 — Clinical phenotype: favism-triggered hemolysis, cataracts, and neonatal jaundice

The clinical spectrum is narrow and oxidative-stress-related. In the classic family, "clinically, this deficiency was manifested by hemolytic crises after eating fava beans in the eldest daughter (patient), and possibly by cataracts in her own and in her brother's eyes" ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)). The novel compound-heterozygous patient presented "with severe neonatal jaundice" ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)).

The diagnostic hallmark is oxidative instability of erythrocyte glutathione: "severely diminished glutathione stability during incubation with acetylphenylhydrazine was observed in the erythrocytes of the siblings" ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)), with intermediate values in the obligate-carrier parents. Importantly, leukocytes are also affected (PMN ~8%, lymphocytes ~4%, monocytes ~15% of normal GR activity), reflecting the ubiquitous expression of the enzyme.

**Suggested HPO terms:** Hemolytic anemia (HP:0001878), Hemolytic anemia with episodic crises, Cataract (HP:0000518), Neonatal hyperbilirubinemia/Neonatal jaundice (HP:0006579), Jaundice (HP:0000952), Reticulocytosis (HP:0001923).

### Finding 3 — Two distinct forms: common acquired (riboflavin-responsive) vs. rare irreversible hereditary

This distinction is central to the disease entity and to its diagnosis. In 1,691 Saudi individuals, "the overall frequency of partial GR deficiency was 24.5% and 20.3% in males and females respectively. In addition, 17.8% of males and 22.4% of females suffered from GR deficiency due to riboflavin deficiency. This could be easily corrected by dietary supplementation with riboflavin. **No cases of severe GR deficiency were identified**" ([PMID: 11924113](https://pubmed.ncbi.nlm.nih.gov/11924113/)).

By contrast, the hereditary form is refractory: "the enzyme activity could not be restored either by addition of FAD in vitro or by administration of riboflavin in vivo" ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)). The dependence of GR on FAD is also the basis of the **erythrocyte glutathione reductase activation coefficient (EGRAC)**, the standard functional biomarker of riboflavin/vitamin B2 status.

| Feature | Acquired (riboflavin-responsive) | Hereditary (*GSR* mutation) |
|---|---|---|
| Cause | Dietary riboflavin/FAD deficiency | Biallelic *GSR* LoF variants |
| Frequency | Common (~20–25% partial in some populations) | Ultra-rare (2 / >15,000) |
| FAD/riboflavin response | Corrects deficiency (EGRAC normalizes) | No response |
| Enzyme protein | Present | Absent or unstable |
| Clinical impact | Benign | Episodic hemolysis, cataract, jaundice |
| Inheritance | Nutritional | Autosomal recessive |

### Finding 4 — GSR supports neutrophil host defense (model organisms)

Beyond erythrocytes, GSR is required for phagocyte function. In *Gsr*-null mice, "Gsr-deficient neutrophils displayed a very transient oxidative burst that abruptly ceased shortly after stimulation" and "Gsr-null mice exhibited enhanced susceptibility to Escherichia coli challenge, indicated by dramatically increased bacterial burden, cytokine storm, striking histological abnormalities, and substantially elevated mortality" ([PMID: 22279102](https://pubmed.ncbi.nlm.nih.gov/22279102/)). GSR also promotes fungal clearance (systemic *Candida*) and neutrophil extracellular trap (NET) formation. The human correlate appears in the Loos family, where patient neutrophils showed abnormal oxygen consumption after zymosan phagocytosis — though clinically significant immunodeficiency is **not** a prominent feature of the human hereditary disease, again pointing to compensation. Notably, "Gsr deficiency resulted in increased activities of cytosolic thioredoxin and thioredoxin [reductase]" in mouse cochlea ([PMID: 28686716](https://pubmed.ncbi.nlm.nih.gov/28686716/)), where the thioredoxin system fully compensates.

### Finding 5 — GSR is a homodimeric FAD/NADPH-disulfide oxidoreductase with a defined catalytic cycle

Human GR (EC 1.8.1.7; UniProt P00390) transfers electrons NADPH → FAD → active-site redox-active disulfide → GSSG, regenerating 2 GSH. Near-atomic synchrotron cryocrystallography (1.1–0.95 Å) showed that "the bound NADPH and redox-active disulfide are positioned optimally on opposite sides of the flavin for a 1,2-addition across a flavin double bond" and that "compression in the active site causes overlapping van der Waals radii and distortion in the nicotinamide ring of the NADPH substrate, which enhances catalysis via stereoelectronic effects" ([PMID: 18638483](https://pubmed.ncbi.nlm.nih.gov/18638483/)).

Pathogenic variants act by destabilizing this fold: the 2,246-bp deletion removes most of the **dimerization domain**, preventing the functional dimer, while Gly330Ala impairs thermostability ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)). GR belongs to the NAD(P)H-dependent disulfide reductase (Pyr_redox / class-I pyridine nucleotide-disulfide oxidoreductase) superfamily.

**Suggested GO terms:** glutathione-disulfide reductase activity (GO:0004362), flavin adenine dinucleotide binding (GO:0050660), NADP binding (GO:0050661), cell redox homeostasis (GO:0045454), glutathione metabolic process (GO:0006749). **CHEBI:** glutathione (CHEBI:16856), glutathione disulfide (CHEBI:17858), NADPH (CHEBI:16474), FAD (CHEBI:16238).

### Finding 6 — Pathophysiology: loss of NADPH→GSH recycling impairs antioxidant defense, causing oxidant-triggered hemolysis and cataract

In erythrocytes, NADPH from the oxidative pentose phosphate pathway (PPP) is the principal reductant; GR uses it to regenerate GSH, which — via glutathione peroxidase and in parallel with catalase — detoxifies H2O2 and organic/lipid peroxides. When an enzyme deficiency limits NADPH/GSH supply, "distinct membrane alterations result causing a removal of the damaged cells by the monocyte-macrophage system" ([PMID: 8813716](https://pubmed.ncbi.nlm.nih.gov/8813716/)). GR deficiency sits among the rare inborn RBC antioxidant defects: "NADPH is the main source of reduction equivalents in RBCs... When NADPH becomes limiting, red cells are prone to being damaged" ([PMID: 24316370](https://pubmed.ncbi.nlm.nih.gov/24316370/)).

The cataract phenotype reflects a parallel mechanism in the lens: "human cataractous lenses showed decreased activities of glutathione reductase, glutathione peroxidase... superoxide dismutase" with GSH depletion and lipid peroxidation ([PMID: 1737065](https://pubmed.ncbi.nlm.nih.gov/1737065/)).

### Finding 7 — Management is supportive; the hereditary form is generally mild with favorable prognosis

No disease-specific pharmacotherapy exists. Because the hereditary form is riboflavin/FAD-unresponsive ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)), management parallels other oxidant-triggered RBC enzymopathies such as G6PD deficiency: a "G6PD-deficient patient... lacks the ability to protect red blood cells against oxidative stresses from certain drugs, metabolic conditions, infections, and ingestion of fava beans" ([PMID: 19769422](https://pubmed.ncbi.nlm.nih.gov/19769422/)) — the same oxidant-avoidance paradigm applies here. Prognosis is favorable because "the amount of reduced glutathione in the erythrocytes was normal in each case" ([PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)) at baseline, explaining the absence of chronic hemolysis between oxidant challenges, consistent with thioredoxin-system compensation ([PMID: 28686716](https://pubmed.ncbi.nlm.nih.gov/28686716/)).

### Finding 8 — *GSR* is loss-of-function tolerant in gnomAD, predicting ~1 in 4 million biallelic births

gnomAD v4 constraint for *GSR* (ENSG00000104687, chr8:30,678,066–30,727,846, GRCh38) shows **pLI ≈ 1.8×10⁻¹⁴** (completely LoF-tolerant), observed/expected LoF = 48/56.5 (oe_lof = 0.85, 90% CI 0.67–1.08), LoF Z = 0.96 — no depletion of truncating variants. Across 4,174 variants, 203 high-confidence predicted-LoF variants summed to an allele frequency ≈ 4.9×10⁻⁴, giving a heterozygous carrier frequency ≈ 0.10% (~1 in 1,000) and a predicted biallelic frequency (q²) ≈ 2.4×10⁻⁷ (~1 in 4 million). The two most common stop-gained alleles lie at the extreme 3′ end of the gene, likely truncating only terminal residues, so the true pathogenic-carrier rate is even lower — consistent with "only 2 cases when testing more than 15,000 blood samples" ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)).

### Finding 9 — Thioredoxin backup for GSSG reduction is evolutionarily conserved, explaining the mild phenotype

The mildness of the phenotype is explained by a conserved alternative GSSG-reducing system. In *Saccharomyces cerevisiae*, cells lacking GLR1 (the GSSG-reductase ortholog) survive, and "the thioredoxin-thioredoxin reductase system can function as an alternative system" to reduce GSSG in vivo ([PMID: 19951944](https://pubmed.ncbi.nlm.nih.gov/19951944/)). Overexpressing TRX1/TRX2 lowers GSSG; deleting them in *glr1* cells raises it. Glr1 "has been shown to colocalize to the cytoplasm and mitochondria" ([PMID: 15701801](https://pubmed.ncbi.nlm.nih.gov/15701801/)), relevant to compartment-specific redox roles. This mirrors mammalian data (mouse cochlea, [PMID: 28686716](https://pubmed.ncbi.nlm.nih.gov/28686716/)). **Orthologs:** mouse *Gsr* (NCBI Gene 14782), *S. cerevisiae* GLR1 (YPL091W).

### Finding 10 — Diagnosis rests on the erythrocyte GR assay (± FAD), EGRAC, and *GSR* sequencing

The diagnostic workup comprises: (1) a red-cell GR activity assay measuring NADPH-dependent GSSG reduction, performed **with and without added FAD** — hereditary deficiency is low and FAD-unresponsive, whereas acquired riboflavin deficiency normalizes; the EGRAC is "the functional biomarker... considered to be the gold standard index" of riboflavin status ([PMID: 27170501](https://pubmed.ncbi.nlm.nih.gov/27170501/)); (2) protein detection by Western blot — "the GR protein was undetectable by Western blotting" in the enzyme-null family ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)); (3) molecular confirmation by *GSR* sequencing/deletion analysis; (4) functional glutathione-stability testing (acetylphenylhydrazine). In riboflavin-deficiency assessment, "samples with AC ≥ 1.3 were considered riboflavin-deficient" ([PMID: 11924113](https://pubmed.ncbi.nlm.nih.gov/11924113/)). **Differential diagnosis:** G6PD deficiency and other hereditary non-spherocytic hemolytic anemias (glutathione synthesis defects, pyruvate kinase deficiency), distinguished by their specific enzyme assays.

### Finding 11 — GSR is a top suppressor of ferroptosis — the disease biology in reverse

A genome-wide CRISPR-knockout screen identified that "glutathione reductase (GSR), a central enzyme maintaining reduced glutathione (GSH) homeostasis, was identified as the top suppressor of ferroptosis" and "GSR knockout or pharmacological inhibition markedly sensitized diverse cancer cell lines to RSL3-induced ferroptosis, while GSR overexpression conferred resistance" ([PMID: 42681644](https://pubmed.ncbi.nlm.nih.gov/42681644/)). This positions the GSH-regenerating function lost in the deficiency as an exploitable cancer vulnerability, and is consistent with the synthetic-lethal dependence of low-GSR cancers on the thioredoxin system.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *GSR* loss-of-function mutation** (2,246-bp deletion removing the dimerization domain; nonsense allele; Gly330Ala destabilizing missense) **leads to** absent or unstable GR protein (demonstrated: undetectable by Western blot; [PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)).
2. Loss of functional homodimeric GR **results in** inability to transfer electrons from NADPH via FAD to reduce GSSG → GSH (demonstrated enzymatically; [PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)).
3. Impaired GSH regeneration **leads to** a diminished capacity to buffer acute oxidative loads, although baseline GSH remains normal because consumption is low at rest (demonstrated: normal resting GSH; [PMID: 947404](https://pubmed.ncbi.nlm.nih.gov/947404/)).
4. **Branch A (erythrocyte):** An exogenous oxidant challenge (fava bean divicine/isouramil, oxidant drugs, infection) **results in** accumulation of H2O2/organic peroxides that GSH-dependent peroxidases cannot clear → oxidation of hemoglobin and membrane proteins → membrane alterations → macrophage removal of damaged cells → **acute hemolytic anemia** ([PMID: 8813716](https://pubmed.ncbi.nlm.nih.gov/8813716/); [PMID: 24316370](https://pubmed.ncbi.nlm.nih.gov/24316370/)).
5. **Branch B (neonatal):** The oxidative lability of neonatal red cells **results in** hemolysis-driven **neonatal jaundice/hyperbilirubinemia** ([PMID: 17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/)).
6. **Branch C (lens):** Chronic failure of lens GSH-dependent peroxide detoxification **leads to** lipid peroxidation and protein oxidation → **cataract** (inferred by analogy to cataractous-lens enzyme profiles; [PMID: 1737065](https://pubmed.ncbi.nlm.nih.gov/1737065/)).
7. **Compensation (dampening node):** In parallel, the **thioredoxin/thioredoxin-reductase system** reduces GSSG and limits oxidative damage, **resulting in** a phenotype that is episodic rather than chronic (demonstrated in yeast and mouse; [PMID: 19951944](https://pubmed.ncbi.nlm.nih.gov/19951944/); [PMID: 28686716](https://pubmed.ncbi.nlm.nih.gov/28686716/)).

```
   GSR biallelic LoF mutation
            │
            ▼
   Absent / unstable GR protein
            │
            ▼
   No NADPH→FAD→GSSG electron transfer  ──┐
            │                             │  (parallel)
            ▼                             ▼
   GSH not regenerated            Trx/TrxR system reduces GSSG
            │                             │  (partial compensation
   + OXIDANT TRIGGER                      │   → mild, episodic phenotype)
   (fava bean, drug, infection)          │
            │ ───────────────────────────┘
   ┌────────┼─────────────┐
   ▼        ▼             ▼
 RBC      Neonatal      Lens
 hemolysis jaundice     cataract
```

**Upstream vs downstream:** The mutation and loss of enzyme activity are upstream; oxidant-triggered peroxide accumulation is the central node; tissue-specific damage (hemolysis, jaundice, cataract) is downstream. The Trx/TrxR system is a lateral, upstream-acting buffer that sets the overall mildness.

**Cell types (CL) and anatomy (UBERON):** erythrocyte (CL:0000232), neutrophil (CL:0000775), lens fiber cell (CL:0011004); blood (UBERON:0000178), lens of camera-type eye (UBERON:0000965), liver (UBERON:0002107, secondary via bilirubin handling). **Subcellular (GO CC):** cytosol (GO:0005829), mitochondrion (GO:0005739) — GR has both cytosolic and mitochondrial isoforms from the single gene.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | How it supports the findings |
|---|---|---|---|
| [17185460](https://pubmed.ncbi.nlm.nih.gov/17185460/) | Molecular basis of GR deficiency in human blood cells | Human clinical/molecular | Defines causal LoF variants, rarity (2/>15,000), absent protein — anchors Findings 1, 2, 5, 8, 10 |
| [947404](https://pubmed.ncbi.nlm.nih.gov/947404/) | Familial deficiency of GR in human blood cells | Human clinical | Establishes AR inheritance, favism/cataract phenotype, FAD/riboflavin non-responsiveness, normal baseline GSH — Findings 1, 2, 3, 6, 7 |
| [11924113](https://pubmed.ncbi.nlm.nih.gov/11924113/) | GR deficiency in Saudi Arabia | Human epidemiology | Quantifies acquired riboflavin-responsive form and absence of hereditary cases — Findings 3, 10 |
| [18638483](https://pubmed.ncbi.nlm.nih.gov/18638483/) | Catalytic cycle of human GR near 1 Å | Structural/in vitro | Defines the FAD/NADPH catalytic mechanism — Finding 5 |
| [22279102](https://pubmed.ncbi.nlm.nih.gov/22279102/) | GR facilitates host defense / oxidative burst / NETs | Mouse model | Neutrophil host-defense role, transient burst defect — Finding 4 |
| [28686716](https://pubmed.ncbi.nlm.nih.gov/28686716/) | GSR not essential in mouse cochlea; Trx backup | Mouse model | Thioredoxin compensation for GSR loss — Findings 4, 7, 9 |
| [8813716](https://pubmed.ncbi.nlm.nih.gov/8813716/) | Hemolytic anemias due to RBC enzyme deficiencies | Review | Mechanistic link from redox-enzyme deficiency to hemolysis — Findings 6, 10 |
| [24316370](https://pubmed.ncbi.nlm.nih.gov/24316370/) | Inborn defects in antioxidant systems of RBCs | Review | NADPH as main RBC reductant; GR deficiency context — Finding 6 |
| [1737065](https://pubmed.ncbi.nlm.nih.gov/1737065/) | Peroxide-metabolizing systems of the lens | Human/in vitro | Links reduced GR + oxidative stress to cataract — Finding 6 |
| [19769422](https://pubmed.ncbi.nlm.nih.gov/19769422/) | Perioperative management of G6PD-deficient patient | Review | Oxidant-avoidance management paradigm — Finding 7 |
| [27170501](https://pubmed.ncbi.nlm.nih.gov/27170501/) | Riboflavin status, MTHFR, blood pressure | Review | EGRAC as gold-standard functional assay — Finding 10 |
| [19951944](https://pubmed.ncbi.nlm.nih.gov/19951944/) | Trx-TrxR as alternative GSSG-reducing system in yeast | Model organism | Conserved thioredoxin backup — Finding 9 |
| [15701801](https://pubmed.ncbi.nlm.nih.gov/15701801/) | Overlapping cytoplasmic/mitochondrial redox systems in yeast | Model organism | Dual localization of GSR ortholog — Finding 9 |
| [42681644](https://pubmed.ncbi.nlm.nih.gov/42681644/) | GR deficiency potentiates ferroptosis/cuproptosis immunogenicity | In vitro/CRISPR | GSR as top ferroptosis suppressor — Finding 11 |
| [35361806](https://pubmed.ncbi.nlm.nih.gov/35361806/) | In silico analysis of deleterious GSR SNPs | Computational | Confirms disease definition; flags candidate deleterious nsSNPs |
| [16528753](https://pubmed.ncbi.nlm.nih.gov/16528753/) | 8 Mb interstitial 8p12-p21.2 deletion | Human clinical | Confirms *GSR* chromosomal location within a contiguous-gene region |

### Section-by-section factual summary

**1. Disease information.** MONDO:0019531; OMIM 618660; gene *GSR* (HGNC:4623). Synonyms: hereditary glutathione reductase deficiency, GR deficiency, GSR deficiency, hemolytic anemia due to glutathione reductase deficiency. MeSH concept: Glutathione Reductase/deficiency. Information is derived from a handful of aggregated case reports/families plus population screens — not from large EHR cohorts.

**2. Etiology.** Primary cause is genetic (biallelic *GSR* LoF). The sole well-established **environmental/trigger factor** is oxidative stress (fava bean ingestion — divicine/isouramil, oxidant drugs, infection). Consanguinity is a risk factor (Loos family). No protective genetic alleles are established; the thioredoxin system acts as an endogenous compensatory buffer rather than a protective "allele." **Gene–environment interaction** is the defining feature: the genotype is clinically silent until an oxidant exposure precipitates hemolysis.

**3. Phenotypes.** Hemolytic anemia (episodic, oxidant-triggered; HP:0001878), cataract (HP:0000518), neonatal jaundice (HP:0006579). Onset ranges from neonatal (jaundice) to childhood/adult (favism, cataract). Severity is mild-to-moderate and episodic rather than progressive. Frequencies cannot be given as robust percentages owing to the tiny number of described patients.

**4. Genetic/molecular.** Causal gene *GSR* (8p12). Variant types observed: large deletion (2,246 bp, LoF), nonsense (premature stop), missense (Gly330Ala, destabilizing). Functional consequence: loss of function via protein instability/loss of dimerization. gnomAD: LoF-tolerant (pLI≈0). No established modifier genes in humans, though the Trx system is the principal functional modifier. No intrinsic epigenetic or chromosomal-abnormality mechanism, though *GSR* can be deleted within contiguous-gene 8p deletions ([PMID: 16528753](https://pubmed.ncbi.nlm.nih.gov/16528753/)).

**5. Environmental.** Oxidant triggers (fava beans/divicine, oxidant drugs, infection). No infectious agent causes the disease.

**6. Mechanism.** See the causal chain and diagram above.

**7. Anatomical structures.** Primary: blood/erythrocytes (UBERON:0000178, CL:0000232); lens (UBERON:0000965). Secondary: liver (bilirubin handling); neutrophils (CL:0000775, host-defense — subclinical in humans). Subcellular: cytosol and mitochondria.

**8. Temporal development.** Onset neonatal to adult; course chronic-lifelong at the genetic level but clinically episodic/trigger-dependent; non-progressive between crises.

**9. Inheritance and population.** Autosomal recessive; predicted biallelic frequency ~1 in 4 million (gnomAD); carrier frequency ~0.1% upper bound. Complete penetrance of the biochemical deficiency; clinical expressivity variable and trigger-dependent. Consanguinity increases risk. No established sex predilection or founder population.

**10. Diagnostics.** Erythrocyte GR assay ±FAD; EGRAC; Western blot; *GSR* sequencing/deletion analysis; acetylphenylhydrazine glutathione-stability test. Differential: G6PD deficiency, other RBC enzymopathies.

**11. Prognosis.** Favorable; survival to adulthood; episodic hemolysis without chronic anemia; normal baseline GSH.

**12. Treatment.** Supportive only: oxidant-trigger avoidance; transfusion in crises; phototherapy/exchange transfusion for neonatal jaundice as per standard neonatology. Riboflavin ineffective for the hereditary form. **NCIT suggestions:** Blood Transfusion (NCIT:C15360), Supportive Care (NCIT:C15277), Phototherapy (NCIT:C15349).

**13. Prevention.** Genetic counseling for consanguineous/carrier families; trigger avoidance (tertiary prevention). No population screening is warranted given rarity.

**14. Other species / natural disease.** *Gsr*-null mice (NCBI Gene 14782) are viable with host-defense and lung-development phenotypes; *S. cerevisiae glr1Δ* (YPL091W) is a standard antioxidant-deficient model. No prominent naturally occurring companion-animal disease is catalogued.

**15. Model organisms.** Mouse *Gsr* knockout (host defense, hyperoxic lung responses), yeast *glr1Δ* (oxidative-stress sensitivity, thioredoxin compensation). These models recapitulate the biochemical defect and the thioredoxin-buffering principle but **do not** fully reproduce the human favism-hemolysis phenotype, because mouse/yeast oxidative challenges differ from human fava-bean exposure.

---

## Limitations and Knowledge Gaps

- **Extremely small patient base.** The entire human literature on the hereditary disease rests on a handful of families. Frequencies, penetrance, and genotype–phenotype correlations cannot be estimated with statistical confidence.
- **Cataract causality is inferential.** The lens mechanism is supported by analogy to cataractous-lens enzyme profiles ([PMID: 1737065](https://pubmed.ncbi.nlm.nih.gov/1737065/)) rather than by direct study of *GSR*-null lenses.
- **No natural-history or registry data.** There are no longitudinal cohorts, QoL instruments, or mortality statistics specific to this disorder.
- **gnomAD estimate is a model.** The ~1-in-4-million figure assumes LoF-variant pathogenicity; several common "LoF" alleles are 3′-terminal and likely benign, so the estimate is an upper bound on biallelic frequency and a lower bound on rarity.
- **Human immune phenotype unquantified.** The neutrophil host-defense role is robust in mice but not demonstrated to cause clinical immunodeficiency in humans.
- **No pharmacogenomic or targeted-therapy data** exist for the deficiency itself.

---

## Proposed Follow-up Experiments / Actions

1. **GeneMatcher / undiagnosed-disease network query** to assemble additional biallelic *GSR* cases and build a minimal natural-history series.
2. **Functional variant characterization:** recombinant expression and thermostability/activity assays of *GSR* missense variants (e.g., Gly330Ala) to establish an ACMG-aligned functional-evidence pipeline (PS3) for VUS classification.
3. **Patient-derived iPSC erythroid and lens-epithelial models** to directly test oxidant-challenge hemolysis and cataractogenesis, and to quantify thioredoxin-system compensation (TXN/TXNRD1 knockdown rescue experiments).
4. **ClinVar curation:** deposit/annotate the known pathogenic alleles (2,246-bp deletion, nonsense, Gly330Ala) with supporting PMIDs to improve diagnostic interpretation.
5. **Targeted re-analysis of hemolytic-anemia gene panels** (including *GSR*) in unexplained G6PD-normal non-spherocytic hemolytic anemia and favism-like presentations.
6. **Therapeutic hypothesis test:** evaluate whether boosting the thioredoxin arm (or avoiding thioredoxin-reductase inhibitors such as auranofin-class drugs) modulates oxidative susceptibility in *GSR*-deficient models — a direct translation of the compensation finding.

---

## Consensus Answer

Glutathione Reductase Deficiency (MONDO:0019531) is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function variants in *GSR* (chromosome 8p12), the gene encoding the FAD/NADPH-dependent flavoenzyme that regenerates reduced glutathione (GSH) from GSSG; its loss cripples erythrocyte and lens antioxidant defense and produces oxidant-triggered (favism) hemolytic anemia, neonatal jaundice, and cataracts. The phenotype is usually mild and episodic because the evolutionarily conserved thioredoxin/thioredoxin-reductase system partially compensates — consistent with *GSR* being genetically loss-of-function-tolerant (gnomAD pLI≈0; predicted biallelic frequency ≈1 in 4 million) and with viable Gsr-knockout mice and glr1Δ yeast. This rare hereditary enzyme-null disease must be distinguished from the common acquired riboflavin-responsive deficiency (discriminated by the EGRAC), and management is limited to oxidant-trigger avoidance and supportive transfusion, since riboflavin corrects only the acquired form.


## Artifacts

- [OpenScientist final report](Glutathione_Reductase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glutathione_Reductase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11924113` *(abstract only)*: "samples with AC ≥ 1.3 were considered riboflavin-deficient"
  - closest text in source: "Samples with AC > or = 1.3 were considered riboflavin-deficient"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

26 of 27 terms resolved to a current term; the rest could not be looked up either way.