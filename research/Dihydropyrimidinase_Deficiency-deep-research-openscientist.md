---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T06:56:37.243357'
end_time: '2026-10-15T07:12:25.842286'
duration_seconds: 948.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dihydropyrimidinase Deficiency
  mondo_id: MONDO:0009111
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
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 16
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 13
  labels_variant: 2
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Dihydropyrimidinase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Dihydropyrimidinase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dihydropyrimidinase Deficiency
- **MONDO ID:** MONDO:0009111 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dihydropyrimidinase Deficiency** covering all of the
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

# Dihydropyrimidinase Deficiency — Comprehensive Disease Characterization

**Disease:** Dihydropyrimidinase Deficiency (DHP deficiency / DPYS deficiency)
**MONDO ID:** MONDO:0009111 · **OMIM:** 222748 · **Orphanet:** 35707
**Causal gene:** *DPYS* (dihydropyrimidinase), 8q22 · **Category:** Mendelian (autosomal recessive inborn error of metabolism)

---

## Summary

Dihydropyrimidinase (DHP) deficiency is a rare autosomal recessive inborn error of the **pyrimidine degradation pathway**, caused by biallelic loss-of-function variants in *DPYS* on chromosome 8q22. The gene encodes dihydropyrimidinase (EC 3.5.2.2), a zinc-dependent amidohydrolase and the **second enzyme** of the three-step catabolism of uracil and thymine. Loss of enzyme activity blocks the ring-opening of 5,6-dihydrouracil and 5,6-dihydrothymine, producing the biochemical hallmark of the disease — **dihydropyrimidinuria**, with markedly elevated dihydrouracil and dihydrothymine in urine, plasma, and cerebrospinal fluid.

The clinical phenotype is **strikingly variable and incompletely penetrant**, ranging from completely asymptomatic individuals to severe neurodevelopmental disease. Reported features include global/developmental delay, seizures and infantile spasms, intellectual disability, autistic features, microcephaly, white matter abnormalities, and brain atrophy, together with gastrointestinal problems (feeding difficulties, vomiting) and, more rarely, congenital heart disease. A 2024 report expanded the phenotype to include **levodopa-responsive juvenile parkinsonism**. Critically, residual enzyme activity does **not** reliably predict whether an individual will be symptomatic, and identical mutations can produce both symptomatic and asymptomatic carriers — pointing to strong genetic/environmental modification.

The single most clinically actionable aspect of the disorder is a **pharmacogenetic predisposition to severe or lethal 5-fluorouracil (5-FU)/capecitabine toxicity**, which can occur even in otherwise asymptomatic individuals and even in partial deficiency. An intriguing biological puzzle — resolved during this investigation using GTEx expression data — is that *DPYS* is expressed almost exclusively in **liver and kidney and essentially not in brain**, which reframes the prominent neurological phenotype as a **circulating-metabolite (non-cell-autonomous) effect** rather than a primary brain enzyme defect. A naturally occurring feline case provides the principal animal model, and population genetics (gnomAD) confirm that *DPYS* tolerates loss-of-function (as expected for a recessive disorder), with pathogenic missense alleles enriched in East Asian populations.

---

## Key Findings

### Finding 1 — Molecular identity: an autosomal recessive defect of pyrimidine degradation (F001)

Dihydropyrimidinase deficiency is caused by biallelic mutations in *DPYS*, which encodes the **second enzyme of the pyrimidine degradation pathway**. DHP (EC 3.5.2.2) catalyzes the ring-opening (hydrolysis) of 5,6-dihydrouracil to N-carbamyl-β-alanine and of 5,6-dihydrothymine to N-carbamyl-β-aminoisobutyric acid. The pathway runs: **uracil/thymine → (DPD) → dihydrouracil/dihydrothymine → (DHP/DPYS) → N-carbamyl-β-alanine/N-carbamyl-β-aminoisobutyrate → (β-ureidopropionase/UPB1) → β-alanine/β-aminoisobutyrate**.

The human *DHP* gene spans **>80 kb**, consists of **10 exons**, and maps to **8q22** by FISH ([PMID: 9718352](https://pubmed.ncbi.nlm.nih.gov/9718352/): *"The human DHP gene spans >80 kb and consists of 10 exons. It has been assigned to 8q22, by FISH."*). The enzyme reaction is defined precisely in the clinical literature ([PMID: 17383919](https://pubmed.ncbi.nlm.nih.gov/17383919/): *"Dihydropyrimidinase (DHP) is the second enzyme of the pyrimidine degradation pathway and it catalyses the ring opening of 5,6-dihydrouracil and 5,6-dihydrothymine to N-carbamyl-beta-alanine and N-carbamyl-beta-aminoisobutyric acid, respectively."*). Inheritance is autosomal recessive — patients are homozygous or compound heterozygous, with heterozygous (carrier) parents.

**Ontology anchors:** MONDO:0009111; gene HGNC:3012 (*DPYS*); GO:0006208 (pyrimidine nucleobase catabolic process); GO:0004157 (dihydropyrimidinase activity); CHEBI 5,6-dihydrouracil, CHEBI 5,6-dihydrothymine.

### Finding 2 — Biochemical hallmark: dihydropyrimidinuria across body fluids (F002)

The defining laboratory abnormality is marked accumulation of the two DHP substrates. Patients show **markedly elevated 5,6-dihydrouracil and 5,6-dihydrothymine in plasma, cerebrospinal fluid, and urine** ([PMID: 20362666](https://pubmed.ncbi.nlm.nih.gov/20362666/): *"Patients presented mainly with neurological and gastrointestinal abnormalities and markedly elevated levels of 5,6-dihydrouracil and 5,6-dihydrothymine in plasma, cerebrospinal fluid and urine."*). The defect is detectable by urine metabolomics: gas chromatography–mass spectrometry (GC-MS) screening reveals elevated dihydrouracil and dihydrothymine, confirmed by quantitative LC-MS/MS ([PMID: 30384990](https://pubmed.ncbi.nlm.nih.gov/30384990/): *"Gas chromatography-mass spectrometry-based urine metabolomics demonstrated significant elevations of dihydrouracil and dihydrothymine, which were subsequently confirmed by a quantitative analysis using liquid chromatography-tandem mass spectrometry."*). Comprehensive HPLC–electrospray ionization tandem MS panels reliably detect the entire spectrum of purine/pyrimidine disorders, including DHP deficiency, in a single run ([PMID: 16613999](https://pubmed.ncbi.nlm.nih.gov/16613999/)).

### Finding 3 — Highly variable, incompletely penetrant phenotype (F003)

Fewer than ~40 patients have been published. The phenotypic range spans **asymptomatic → severe neurological disease**. Reported features include global/developmental delay, seizures and infantile spasms, intellectual disability, dysmorphic facies, autistic features, microcephaly, white matter abnormalities, and brain atrophy, plus gastrointestinal abnormalities (feeding problems, vomiting). Congenital heart disease (atrioventricular septal defect, ventricular septal defect) has been reported as a rare feature.

Key quotes: ([PMID: 38958169](https://pubmed.ncbi.nlm.nih.gov/38958169/): *"Clinical findings are variable and some patients may remain asymptomatic. Global developmental delay and increased susceptibility to 5-fluorouracil are commonly reported."*) and ([PMID: 29054612](https://pubmed.ncbi.nlm.nih.gov/29054612/): *"a highly variable clinical presentation, ranging from asymptomatic to infantile spasm and reduced white matter and brain atrophy"*). Crucially, **enzyme residual activity does not discriminate symptomatic from asymptomatic individuals** ([PMID: 9718352](https://pubmed.ncbi.nlm.nih.gov/9718352/): *"There was no significant difference, in residual activity, between mutations observed in the symptomatic and those observed in the asymptomatic individuals."*). This poor genotype–phenotype and enzyme-activity–phenotype correlation is a central feature and strongly implies modifier genes and/or environmental triggers.

**Suggested HPO terms:** HP:0001263 (global developmental delay), HP:0001250 (seizures), HP:0001251 (infantile spasms → HP:0012469), HP:0001249 (intellectual disability), HP:0000729 (autistic behavior), HP:0000252 (microcephaly), HP:0002500 (cerebral white matter abnormality), HP:0002059 (cerebral atrophy), HP:0011968 (feeding difficulties), HP:0002013 (vomiting), HP:0001629 (ventricular septal defect), HP:0001674 (atrioventricular septal defect).

### Finding 4 — Pharmacogenetic predisposition to severe/lethal 5-fluorouracil toxicity (F004)

This is the most clinically consequential aspect of the disorder. **Partial DHP deficiency is itself a pharmacogenetic disorder associated with severe 5-FU toxicity** ([PMID: 15571261](https://pubmed.ncbi.nlm.nih.gov/15571261/): *"A partial dihydropyrimidinase deficiency proved to be a novel pharmacogenetic disorder associated with severe 5FU toxicity."*). Because 5-FU is itself catabolized through the pyrimidine degradation pathway, DHP deficiency slows 5-FU clearance; **lethal side-effects can occur even in asymptomatic patients** ([PMID: 19571472](https://pubmed.ncbi.nlm.nih.gov/19571472/): *"when the patients are treated with 5-fluorouracil, a pyrimidine analogue anticancer drug, lethal side-effects can be seen even in asymptomatic patients"*).

Quantitatively, dihydropyrimidine dehydrogenase (DPD/*DPYD*) deficiency accounts for ~43% of grade 3–4 5-FU toxicity ([PMID: 18075467](https://pubmed.ncbi.nlm.nih.gov/18075467/): *"Dihydropyrimidine dehydrogenase (DPD) deficiency accounts for approximately 43% of grade 3-4 toxicity to 5-fluorouracil."*); the residual unexplained toxicity is attributed in part to downstream DHP (*DPYS*) and β-ureidopropionase (*UPB1*) deficiencies. Additional case literature illustrates that severe 5-FU toxicity can also arise from thiamine deficiency/beriberi in the absence of a definable enzyme defect ([PMID: 21941485](https://pubmed.ncbi.nlm.nih.gov/21941485/)) and that a putative "enhanced thymine absorption" phenotype may contribute ([PMID: 29846282](https://pubmed.ncbi.nlm.nih.gov/29846282/)) — important differential considerations when evaluating fluoropyrimidine toxicity.

**Clinical implication:** urinary dihydropyrimidine screening and *DPYS* genotyping should be considered before fluoropyrimidine chemotherapy, alongside standard *DPYD* testing.

### Finding 5 — Protein mechanism: a zinc-dependent amidohydrolase disrupted by diverse mutation classes (F005)

DHP is a member of the **cyclic amidohydrolase family** (which also includes allantoinase, dihydroorotase, hydantoinase, and imidase) and is a **zinc metalloenzyme with a binuclear metal center** in which two metal ions are bridged by a post-translationally carbamylated lysine; the functional unit is a **homotetramer** ([PMID: 30268498](https://pubmed.ncbi.nlm.nih.gov/30268498/): *"Dihydropyrimidinase (DHPase) is a member of the cyclic amidohydrolase family... Almost all of these zinc metalloenzymes possess a binuclear metal center in which two metal ions are bridged by a post-translational carbamylated Lys."*).

Mutation analysis in 17 patients found 9 missense, 2 nonsense, 2 deletion, and 1 splice-site mutation, with **71% localizing to exons 5–8**. Most expressed mutants had no activity; p.R302Q and p.T343A retained ~3.9% and ~49% residual activity respectively. Mapping onto the crystal structure reveals **distinct structural mechanisms** ([PMID: 20362666](https://pubmed.ncbi.nlm.nih.gov/20362666/): *"The crystal structure of human DHP indicated that the point mutations p.R490C, p.R302Q and p.V364M affect the oligomerization of the enzyme. In contrast, p.M70T, p.D81G, p.L337P and p.T343A affect regions near the di-zinc centre and the substrate binding site."*). Other variants (p.S379R, p.L7V) cause global structural destabilization. East Asian/Japanese patients carry recurrent variants (e.g., Q334R, H295R, M250I) affecting active-site loops ([PMID: 29054612](https://pubmed.ncbi.nlm.nih.gov/29054612/): *"The observation that the identified mutations were more prevalent in East Asians and the Japanese population indicates that DHP deficiency may be more common than anticipated in these ethnic groups."*).

| Mutation class | Example variants | Structural/functional consequence |
|---|---|---|
| Oligomerization interface | p.R490C, p.R302Q, p.V364M | Impaired homotetramer assembly |
| Di-zinc center / substrate binding | p.M70T, p.D81G, p.L337P, p.T343A | Catalytic impairment near active site |
| Global destabilization | p.S379R, p.L7V | Misfolding / instability |
| Truncating | p.R475*, p.K501X, p.R465X, p.W117* | Loss of function / NMD |

### Finding 6 — A naturally occurring feline model (F006)

DHP deficiency occurs spontaneously in cats, providing a comparative animal model. An affected cat presented with malnutrition, depression, vomiting, and hyperammonemia; urine GC-MS showed large amounts of dihydrouracil and dihydrothymine and moderate uracil/thymine. The cat was **homozygous for the *DPYS* missense mutation c.1303G>A (p.G435R)**, which **corresponds to a known human DHP-deficiency mutation** ([PMID: 23430934](https://pubmed.ncbi.nlm.nih.gov/23430934/): *"Analysis of the feline DPYS gene encoding DHP demonstrated that the cat was homozygous for the missense mutation c.1303G>A (p.G435R) in exon 8, which corresponds to a known mutation in a human patient with DHP deficiency."*). Screening 1,000 cats found no additional carriers, indicating a very low allele frequency. The literature cites an estimated human prevalence of ~2/20,000 ([PMID: 30384990](https://pubmed.ncbi.nlm.nih.gov/30384990/): *"an estimated prevalence of 2/20,000"*).

**Taxonomy/ortholog anchors:** *Felis catus* (NCBI Taxon:9685); feline *DPYS* ortholog; the p.G435R orthologous variant links feline and human disease biology directly.

### Finding 7 — Population genetics: LoF-tolerant gene with East-Asian-enriched pathogenic alleles (F007)

Analysis of gnomAD v4 (GRCh38) constraint for *DPYS* (ENSG00000147647, chr8:104,330,324–104,467,055) confirms the recessive model: **pLI ≈ 0**, observed/expected LoF (o/e) = 0.775 (LOEUF 90% CI 0.60–1.01), LoF Z = 1.35, observed/expected LoF = 39/50.3 — i.e., **loss-of-function is tolerated**, exactly as expected for an autosomal recessive LoF disorder. Summing 87 high-confidence pLoF alleles gives a cumulative pLoF allele frequency q ≈ 8.5×10⁻⁴, implying a **pLoF-only carrier frequency ≈ 2q ≈ 1/587** and homozygous-pLoF incidence q² ≈ 1/1.4M — a **lower bound**, because pathogenic missense alleles (which dominate the real mutation spectrum) are excluded.

Recurrent pLoF alleles include p.Arg475Ter (AF 1.3×10⁻⁴), p.Glu507MetfsTer57, p.Trp117Ter, p.Arg503GlufsTer2, and p.Arg302Ter. Known pathogenic **missense** alleles show marked ancestry enrichment, corroborating clinical reports of East Asian/Japanese clustering ([PMID: 29054612](https://pubmed.ncbi.nlm.nih.gov/29054612/)):

| Variant | Population enrichment | Allele frequency |
|---|---|---|
| p.Gln334Arg (Q334R) | East Asian | 0.00209 (~1/240 EAS); ~0 elsewhere |
| p.His295Arg (H295R) | East Asian | enriched |
| p.Arg490Cys (R490C) | East Asian | enriched |
| p.Trp360Arg (W360R) | Middle Eastern | enriched |
| p.Arg475Ter (R475*) | Middle Eastern | enriched |
| p.Met250Ile (M250I) | Ashkenazi Jewish | enriched |

### Finding 8 — ClinVar allelic heterogeneity and interpretation challenge (F008)

ClinVar harbors extensive allelic heterogeneity for *DPYS*: a query returned ~300 variant records — **87 Pathogenic, 27 Likely pathogenic (114 P/LP combined), 255 Uncertain significance (VUS), plus benign/likely-benign entries**. Variant classes are predominantly single-nucleotide (missense/nonsense/splice) with small indels; **no recurrent large structural/chromosomal abnormality** is characteristic of the disease. The large VUS burden underscores the diagnostic interpretation challenge, especially given the lack of genotype–phenotype correlation.

### Finding 9 — Organ localization: a liver/kidney enzyme, not a brain enzyme (F009)

A key mechanistic insight from this investigation: GTEx v8 median expression for *DPYS* (ENSG00000147647) is dominated by **liver (132.8 TPM) and kidney cortex (39.1 TPM)** (kidney medulla 12.7 TPM), while **brain regions are very low** (frontal cortex ~1.3, cortex ~0.8 TPM) and heart/skeletal muscle/whole blood are negligible (<0.03 TPM). This mirrors the known organ localization of pyrimidine catabolism.

The implication is important for the pathophysiological model: because the enzyme is not expressed in brain, the prominent neurological phenotype is best understood as a **circulating-metabolite (non-cell-autonomous) effect** — accumulated dihydropyrimidines (and/or downstream perturbations such as reduced β-alanine/β-aminoisobutyrate availability) reach the CNS through the circulation, rather than reflecting a cell-autonomous loss of DHP in neurons.

**Anatomical/subcellular anchors:** UBERON:0002107 (liver), UBERON:0001225 (cortex of kidney); cytoplasmic localization (GO:0005737).

### Finding 10 — Phenotype expansion: levodopa-responsive juvenile parkinsonism (F010)

The phenotypic spectrum was expanded in 2024 by the **first report of levodopa-responsive juvenile parkinsonism** associated with DHP deficiency: a 13-year-old with rapidly progressive dysphagia, dysarthria, and loss of ambulation over 18 months, compound heterozygous for *DPYS* c.1393C>T (p.R465X) and c.905G>A (p.R302Q), with urinary metabolome showing markedly elevated dihydrouracil and dihydrothymine ([PMID: 39558747](https://pubmed.ncbi.nlm.nih.gov/39558747/): *"We present the first case of levodopa-responsive juvenile parkinsonism associated with dihydropyrimidinase deficiency caused by a novel DPYS variant."*). Importantly, **levodopa relieved the motor symptoms** ([PMID: 39558747](https://pubmed.ncbi.nlm.nih.gov/39558747/): *"Levodopa treatment effectively relieved the patient's motor symptoms."*) — a rare symptom-directed pharmacologic treatment opportunity.

The variant p.R302Q (c.905G>A) is recurrent — also reported homozygously in a Chinese child ([PMID: 33179229](https://pubmed.ncbi.nlm.nih.gov/33179229/)). Molecular-dynamics studies of 10 DHP variants show mutation-specific effects: oligomerization-interface disruption (T68R, D81G, G278D, L337P), stereochemistry-gate loops/substrate-binding pocket perturbation (W117R, T343A, R412M), and global collapse (W360R, G435R), while a near-normal-activity variant (R181W) showed only slight changes ([PMID: 35961217](https://pubmed.ncbi.nlm.nih.gov/35961217/): *"In the T68R, D81G, G278D, and L337P variants, the flexibilities of structures related to the interaction for oligomer formation increased in comparison with those of the wild type."*).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *DPYS* (8q22)** → reduce or abolish production of functional dihydropyrimidinase protein (truncating/NMD alleles) *or* produce misfolded/destabilized/assembly-incompetent protein (missense alleles affecting the di-zinc center, substrate-binding pocket, or homotetramer interface).
2. **Loss of DHP (EC 3.5.2.2) catalytic activity** → the second step of pyrimidine degradation **fails to open the ring** of 5,6-dihydrouracil and 5,6-dihydrothymine (*demonstrated biochemically and structurally*).
3. **Metabolic block** → accumulation of the substrates **5,6-dihydrouracil and 5,6-dihydrothymine**, with secondary elevation of upstream uracil/thymine, in **liver and kidney** (principal sites of enzyme expression) and spillover into **plasma, CSF, and urine** → **dihydropyrimidinuria** (*demonstrated*).
4. **Systemic distribution of accumulated metabolites** → because *DPYS* is **not expressed in brain** (liver/kidney enzyme), CNS exposure is driven by **circulating** dihydropyrimidines reaching the brain → *inferred* non-cell-autonomous neurotoxic/neurodevelopmental effect.
5. **Branch A — Neurodevelopmental:** developmental delay, seizures/infantile spasms, intellectual disability, autistic features, white-matter abnormality, brain atrophy, and (rarely) levodopa-responsive juvenile parkinsonism. *The molecular link from metabolite accumulation to neuronal dysfunction remains inferred.*
6. **Branch B — Gastrointestinal/systemic:** feeding problems, vomiting; in the feline model, hyperammonemia.
7. **Branch C — Pharmacogenetic 5-FU toxicity:** when exogenous fluoropyrimidine (5-FU/capecitabine) is administered, the impaired degradation pathway **slows 5-FU catabolism** → drug/metabolite accumulation → **severe or lethal systemic toxicity**, even in asymptomatic individuals (*demonstrated clinically*).
8. **Incomplete penetrance / variable expressivity** — because residual enzyme activity does not predict symptoms and identical genotypes yield discordant phenotypes, **modifier genes and/or environmental factors** (e.g., dietary pyrimidine load, drug exposure) determine whether branches A–B manifest (*inferred*).

```
 DPYS biallelic LoF
        |
        v
 Loss of dihydropyrimidinase activity (di-Zn amidohydrolase, homotetramer)
        |
        v
 Block of ring-opening: dihydrouracil + dihydrothymine accumulate (liver/kidney)
        |
        v
 Spillover -> plasma / CSF / urine  (DIHYDROPYRIMIDINURIA)
        |
   -----+-----------------------------+-----------------------------+
   |                                 |                             |
   v (circulating metabolites)       v                             v (exogenous trigger)
 CNS effects (non-cell-autonomous) GI/systemic              5-FU / capecitabine
 - dev. delay, seizures            - feeding problems         -> impaired catabolism
 - autistic features, WM changes   - vomiting                 -> SEVERE/LETHAL TOXICITY
 - juvenile parkinsonism           - (feline: hyperammonemia)    (even if asymptomatic)
        |
   [modifier genes / environment -> incomplete penetrance, variable expressivity]
```

**Upstream (primary):** *DPYS* mutation → protein dysfunction → enzymatic block → metabolite accumulation. **Downstream (secondary):** circulating-metabolite exposure of brain and tissues → neurodevelopmental and GI phenotypes; iatrogenic 5-FU toxicity is a conditional downstream branch requiring drug exposure.

**Cell types / processes:** Primary biochemical lesion in **hepatocytes (CL:0000182)** and **renal proximal tubule cells (kidney cortex)**; downstream effects in **central nervous system** (neurons; white matter / oligodendrocytes CL:0000128). Biological processes: **pyrimidine nucleobase catabolic process (GO:0006208)**, **dihydropyrimidinase activity (GO:0004157)**, cytoplasmic metabolism (GO:0005737).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [9718352](https://pubmed.ncbi.nlm.nih.gov/9718352/) | Gene structure, chromosomal localization, mutation analysis | F001 (gene structure, 8q22, 10 exons); F003 (no residual-activity difference) |
| [17383919](https://pubmed.ncbi.nlm.nih.gov/17383919/) | Two siblings with DHP deficiency | F001 (enzyme function/reaction) |
| [20362666](https://pubmed.ncbi.nlm.nih.gov/20362666/) | Phenotype/genotype/structure in 17 patients | F002 (metabolites in plasma/CSF/urine); F005 (structure–function map) |
| [30384990](https://pubmed.ncbi.nlm.nih.gov/30384990/) | Incidental detection by urine metabolome | F002 (GC-MS/LC-MS/MS); F006 (prevalence ~2/20,000) |
| [38958169](https://pubmed.ncbi.nlm.nih.gov/38958169/) | DHP deficiency with atrioventricular septal defect | F003 (variability, asymptomatic, 5-FU susceptibility) |
| [29054612](https://pubmed.ncbi.nlm.nih.gov/29054612/) | Four East Asian patients, novel/rare DPYS mutations | F003 (phenotype range); F005/F007 (East Asian enrichment) |
| [15571261](https://pubmed.ncbi.nlm.nih.gov/15571261/) | Pyrimidine defects and severe 5-FU toxicity | F004 (partial DHP deficiency = pharmacogenetic 5-FU risk) |
| [19571472](https://pubmed.ncbi.nlm.nih.gov/19571472/) | 5-FU toxicity in pyrimidine metabolic disorders | F004 (lethal toxicity in asymptomatic patients) |
| [18075467](https://pubmed.ncbi.nlm.nih.gov/18075467/) | Genetic regulation of dihydropyrimidinase | F004 (DPD ~43% of grade 3–4 toxicity) |
| [30268498](https://pubmed.ncbi.nlm.nih.gov/30268498/) | DHPase crystal structures / amidohydrolase family | F005 (zinc metalloenzyme, binuclear metal center) |
| [23430934](https://pubmed.ncbi.nlm.nih.gov/23430934/) | First feline case of dihydropyrimidinuria | F006 (feline model; orthologous p.G435R) |
| [35961217](https://pubmed.ncbi.nlm.nih.gov/35961217/) | Molecular dynamics of pathogenic variants | F005/F010 (variant-specific destabilization) |
| [39558747](https://pubmed.ncbi.nlm.nih.gov/39558747/) | Juvenile parkinsonism with DHP deficiency | F010 (levodopa-responsive parkinsonism) |
| [33179229](https://pubmed.ncbi.nlm.nih.gov/33179229/) | Chinese child, DPYS variant analysis | F010 (recurrent p.R302Q homozygous) |
| [16613999](https://pubmed.ncbi.nlm.nih.gov/16613999/) | HPLC-ESI-MS/MS purine/pyrimidine panel | F002 (comprehensive diagnostic detection) |
| [32600357](https://pubmed.ncbi.nlm.nih.gov/32600357/) | Novel stop-gain c.1501A>T p.K501X | Allelic heterogeneity; AR confirmation; liver mRNA reduction |
| [38199782](https://pubmed.ncbi.nlm.nih.gov/38199782/) | Diagnostic odyssey case + literature review | Clinical/diagnostic context |
| [39126710](https://pubmed.ncbi.nlm.nih.gov/39126710/) | Dual diagnosis (DPYS + TBX19) in Sri Lankan boy | Phenotype complexity; consanguinity |
| [21941485](https://pubmed.ncbi.nlm.nih.gov/21941485/) | 5-FU encephalopathy / beriberi differential | Differential of 5-FU toxicity |
| [29846282](https://pubmed.ncbi.nlm.nih.gov/29846282/) | "Enhanced thymine absorption" phenotype | Alternative fluoropyrimidine-toxicity mechanism |

### Section-by-section report content (template coverage)

**1. Disease Information.** DHP deficiency is a rare autosomal recessive inborn error of pyrimidine degradation. Identifiers: **OMIM 222748, Orphanet 35707, MONDO:0009111**; ICD-10 under disorders of pyrimidine metabolism (E79.8). Synonyms: dihydropyrimidinase deficiency, DHP deficiency, DHPase deficiency, dihydropyrimidinuria, DPYS deficiency. Information derives from aggregated disease-level resources plus a small set of individual case reports (<40 patients).

**2. Etiology.** The sole established cause is biallelic pathogenic *DPYS* variants (genetic). There are **no established environmental causes**; however, fluoropyrimidine drug exposure is the key **environmental trigger of the toxicity phenotype**. Risk factors: consanguinity and East Asian/Middle Eastern/Ashkenazi ancestry (founder/enriched alleles). No protective alleles defined. Gene–environment interaction is exemplified by 5-FU: a genetic enzyme deficiency becomes life-threatening only on drug exposure.

**3. Phenotypes.** See Findings 3 and 10 and HPO list above. Onset typically neonatal/infantile but ranges to adult incidental detection; severity variable (asymptomatic → severe); progression usually stable but can be progressive (juvenile parkinsonism). Frequencies are qualitative given the tiny cohort; developmental delay and 5-FU susceptibility are most commonly reported.

**4. Genetic/Molecular.** Causal gene *DPYS* (HGNC:3012, OMIM 613326), 8q22, 10 exons, >80 kb. Variant spectrum: predominantly missense, with nonsense, frameshift, splice, small indels; ClinVar ~114 P/LP and ~255 VUS. Functional consequence: **loss of function** (catalytic, metal-center, substrate-binding, or oligomerization defects). No modifier genes formally established; no characteristic epigenetic changes or large chromosomal abnormalities. Allele frequencies: p.Q334R EAS ~1/240. Germline origin.

**5. Environmental.** No toxins/infectious agents cause the disease. The decisive exogenous factor is **fluoropyrimidine chemotherapy** (5-FU, capecitabine) precipitating severe toxicity. Dietary pyrimidine load is a plausible but unproven modifier.

**6. Mechanism.** See ordered causal chain above.

**7. Anatomical structures.** Primary biochemical organs: **liver (UBERON:0002107) and kidney (UBERON:0002113 / cortex UBERON:0001225)**. Secondary: **central nervous system / brain (UBERON:0000955)**, white matter (UBERON:0002316); GI tract; rarely heart. Subcellular: cytoplasm. Lateralization not characteristic.

**8. Temporal development.** Onset congenital/pediatric most often but variable to adulthood; pattern usually chronic/insidious, occasionally rapidly progressive (parkinsonism over 18 months). Lifelong, no spontaneous remission; the critical **intervention window is avoidance of fluoropyrimidines**.

**9. Inheritance and population.** Autosomal recessive; incomplete penetrance; variable expressivity; estimated prevalence ~2/20,000 (cited); gnomAD pLoF carrier frequency ≥~1/590 (lower bound). Consanguinity and East Asian/Middle Eastern/Ashkenazi founder effects relevant. No sex predilection established.

**10. Diagnostics.** First-line: **urine organic acid / pyrimidine panel** showing elevated dihydrouracil and dihydrothymine (GC-MS, confirmed by LC-MS/MS; comprehensive HPLC-ESI-MS/MS panel). Confirmatory: ***DPYS* sequencing** (single-gene, panels, or WES/WGS). Differential diagnosis: DPD (*DPYD*) deficiency, β-ureidopropionase (*UPB1*) deficiency, and non-genetic causes of fluoropyrimidine toxicity (thiamine deficiency/beriberi; "enhanced thymine absorption"). Screening: pre-chemotherapy pyrimidine screening; cascade family testing.

**11. Outcome/Prognosis.** Highly variable; many asymptomatic individuals have normal life expectancy. No disease-specific mortality data except the catastrophic risk of **lethal 5-FU toxicity**. Prognostic factors poorly defined; residual enzyme activity is not prognostic.

**12. Treatment.** No curative therapy; **supportive/symptomatic management**. Actionable interventions: (a) **strict avoidance of fluoropyrimidines** (or extreme caution/dose modification), and (b) **levodopa** for the parkinsonism presentation (NCIT:C739 Levodopa). Seizures, developmental, GI, and feeding issues managed supportively. No gene/cell/RNA therapy exists.

**13. Prevention.** Primary: carrier screening and genetic counseling in at-risk/consanguineous families; prenatal/preimplantation diagnosis feasible given known variants. Secondary: pre-chemotherapy pyrimidine/genotype screening to prevent toxicity. Tertiary: avoid fluoropyrimidines; manage complications.

**14. Other species / Natural disease.** Spontaneous feline disease (*Felis catus*, Taxon:9685) with orthologous p.G435R — the principal natural model; veterinary relevance limited but illustrative of conserved mechanism.

**15. Model organisms.** No widely used engineered mouse/zebrafish model is established in the reviewed literature; the **naturally occurring feline case** is the primary in-vivo model, supplemented by heterologous expression of mutant protein and crystallography/molecular-dynamics for structure–function.

---

## Limitations and Knowledge Gaps

- **Tiny cohort (<40 patients)** limits frequency estimates, genotype–phenotype correlation, and natural-history/prognostic data; most "frequencies" are qualitative.
- **Unexplained incomplete penetrance:** the molecular basis for discordant phenotypes among identical genotypes is unknown — modifier genes, dietary pyrimidine load, and environmental triggers are hypothesized but not demonstrated.
- **CNS mechanism is inferred, not proven:** the circulating-metabolite (non-cell-autonomous) model is strongly supported by *DPYS* tissue expression (liver/kidney, not brain) but the specific neurotoxic species and molecular target remain uncharacterized.
- **No engineered mammalian model** (knockout mouse) was identified in the reviewed literature, limiting mechanistic dissection and therapeutic testing.
- **Large VUS burden** (~255 ClinVar VUS) impedes clinical interpretation; functional assays are not routinely available.
- **Prevalence uncertainty:** the ~2/20,000 estimate and gnomAD-derived carrier frequencies (≥~1/590) differ in scope; true prevalence (including missense alleles) is likely underestimated, especially in East Asian populations.
- **Treatment evidence is anecdotal:** levodopa response is based on a single case; no trials exist.

## Proposed Follow-up Experiments / Actions

1. **Establish a *Dpys* knockout mouse** (and/or zebrafish) to test whether the neurological phenotype is reproduced and whether it is driven by circulating metabolites (parabiosis, liver-specific vs global knockout, metabolite-rescue experiments).
2. **Metabolite neurotoxicity assays:** expose neuronal/organoid cultures to pathophysiological concentrations of dihydrouracil/dihydrothymine (± β-alanine/β-aminoisobutyrate depletion) to identify the toxic species and molecular target.
3. **Prospective pre-chemotherapy screening study** combining *DPYD* + *DPYS* (+ *UPB1*) genotyping and urinary pyrimidine ratios to quantify the *DPYS* contribution to otherwise-unexplained fluoropyrimidine toxicity and validate predictive biomarkers (e.g., urinary THY/DHT ratio).
4. **High-throughput functional classification of VUS** (saturation mutagenesis + activity/oligomerization assay) to reduce the ClinVar VUS burden and improve clinical interpretation.
5. **Modifier search:** genotype–phenotype analysis across the expanding registry to identify penetrance modifiers; collect dietary/exposure data.
6. **Natural-history registry** to define onset, progression, prognosis, and the real frequency of parkinsonism and cardiac sub-phenotypes; evaluate levodopa responsiveness systematically.
7. **Population carrier-frequency studies** in East Asian, Middle Eastern, and Ashkenazi cohorts to refine prevalence and inform targeted carrier screening.

---

*Report compiled from a 5-iteration autonomous investigation: 10 confirmed findings, 20 reviewed papers, integrating primary clinical literature, gnomAD/ClinVar population genetics, GTEx expression data, protein structural/computational studies, and a naturally occurring animal model.*


## Artifacts

- [OpenScientist final report](Dihydropyrimidinase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Dihydropyrimidinase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002500` (1 mention) - the report calls it "cerebral white matter abnormality"; HP calls it **Abnormal cerebral white matter morphology**, and lists "Cerebral white matter abnormalities" among its other names
- `HP:0001674` (1 mention) - the report calls it "atrioventricular septal defect"; HP calls it **Complete atrioventricular canal defect**, and lists "Complete atrioventricular septal defect" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.

25 of 27 terms resolved to a current term; the rest could not be looked up either way.