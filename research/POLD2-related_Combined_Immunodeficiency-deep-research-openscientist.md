---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-13T20:13:24.038719'
end_time: '2026-10-13T20:35:13.395072'
duration_seconds: 1309.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: POLD2-related Combined Immunodeficiency
  mondo_id: MONDO:1010175
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
citation_count: 8
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 29
  verified: 25
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 12
  labels_variant: 8
  obsolete_terms:
  - term_id: HP:0005354
    ontology_label: obsolete Absent cellular immunity
    replaced_by: HP:0011840
  - term_id: HP:0045080
    ontology_label: obsolete Decreased CD3+ T cell proportion
    replaced_by: HP:0005403
  unresolvable_prefixes:
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: POLD2-related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: POLD2-related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** POLD2-related Combined Immunodeficiency
- **MONDO ID:** MONDO:1010175 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **POLD2-related Combined Immunodeficiency** covering all of the
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

# POLD2-related Combined Immunodeficiency (MONDO:1010175): A Comprehensive Disease Characteristics Report

## Summary

**POLD2-related combined immunodeficiency (CID)** is an ultra-rare, autosomal-recessive, syndromic (non-severe) combined immunodeficiency caused by germline biallelic hypomorphic variants in **POLD2** (chromosome 7p13; HGNC:9176; NCBI Gene 5425; OMIM *600591), the gene encoding the **p50 accessory/scaffolding subunit of DNA polymerase δ (Polδ)**. It was first defined in 2019 by Conde and colleagues, who identified biallelic mutations in either *POLD1* or *POLD2* as the cause of a previously undescribed syndrome that combines **replicative stress, neurodevelopmental abnormalities, and immunodeficiency** ([PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)). The disorder belongs to the broader "polymerase delta deficiency" group and sits within a small allelic series of DNA polymerase δ-complex immunodeficiencies that also includes *POLD1*- and *POLD3*-related disease.

Mechanistically, loss of functional POLD2 **destabilizes the Polδ holoenzyme**, impairing DNA replication and several PCNA-dependent repair pathways. This produces **replication-associated DNA lesions and impaired cell-cycle (S-phase) progression** in proliferating cells—defects that are reversible upon overexpression of polymerase δ in patient cells. Because developing lymphocytes depend on intense proliferation and on template-dependent DNA synthesis during antigen-receptor gene rearrangement, the replicative-stress phenotype manifests most prominently as a **T-cell defect**: T-cell lymphopenia with loss of naive T cells and a restricted T-cell receptor (TCR) repertoire. The clinical picture is completed by a **neurodevelopmental component (intellectual disability)** and **sensorineural hearing loss**, producing a recognizable syndromic triad.

The evidence base for the POLD2 subtype specifically is extremely thin—essentially a single reported index patient within a handful of Polδ-complex cases—so much of the clinical, epidemiological, and therapeutic detail is inferred from the closely related *POLD1* and *POLD3* deficiencies, which share the same core mechanism. Management is supportive (infection prophylaxis, immunoglobulin replacement) with **allogeneic hematopoietic stem cell transplantation (HSCT)** as the definitive immune-directed therapy; because the underlying lesion impairs DNA repair, reduced-intensity conditioning is favored to limit regimen-related toxicity. This report organizes the available evidence across all 15 requested disease-characteristic domains, flagging clearly where information is unavailable or extrapolated.

---

## Key Findings

### Finding 1 — POLD2-related CID is an autosomal-recessive syndrome caused by germline biallelic POLD2 mutations (F001)

Conde et al. (2019) identified germline biallelic mutations in *POLD1* or *POLD2* in patients from two independent pedigrees as the cause of a previously undescribed autosomal-recessive syndrome. This was the first report of germline biallelic mutations affecting the Polδ complex in humans. POLD2 (HGNC:9176) encodes the **p50 accessory subunit** of the DNA polymerase δ heterotetramer (POLD1 catalytic + POLD2/POLD3/POLD4 accessory) and maps to chromosome 7p13 (OMIM *600591).

> *"caused by germline biallelic mutations in POLD1 or POLD2 as the underlying etiology of a previously unknown autosomal-recessive syndrome that combines replicative stress, neurodevelopmental abnormalities, and immunodeficiency"* — [PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)

This establishes the gene, the biallelic/germline nature, and the autosomal-recessive inheritance that anchor the entire disease definition.

### Finding 2 — The clinical triad: syndromic CID, neurodevelopmental impairment, and sensorineural hearing loss (F002)

The core phenotype combines replicative stress, neurodevelopmental abnormalities, and immunodeficiency (Conde 2019). Mehawej et al. (2023), describing the related POLD3 deficiency, summarized the shared clinical signature of the group:

> *"Mutations in POLD1 and POLD2 have been recently shown to be associated with a syndromic CID characterized by T cell lymphopenia with or without intellectual deficiency and sensorineural hearing loss"* — [PMID: 37030525](https://pubmed.ncbi.nlm.nih.gov/37030525/)

This defines the three recognizable components used for clinical pattern recognition: **(1) combined immunodeficiency with T-cell lymphopenia, (2) intellectual deficiency (variable), and (3) sensorineural hearing loss.**

### Finding 3 — Mechanism: POLD2 mutations destabilize the Polδ complex, causing reversible replication-associated DNA lesions (F003)

In Conde et al. (2019), patient cells showed **impaired cell-cycle progression and replication-associated DNA lesions that were reversible upon overexpression of polymerase δ**; the mutations affected the stability and interactions within the Polδ complex or its intrinsic polymerase activity. POLD2 is the p50 scaffolding subunit that bridges POLD1 (catalytic) to POLD3/POLD4 and indirectly to PCNA, so its loss destabilizes assembly of the holoenzyme.

> *"Patients' cells showed impaired cell-cycle progression and replication-associated DNA lesions that were reversible upon overexpression of polymerase δ. The mutations affected the stability and interactions within the polymerase δ complex or its intrinsic polymerase activity"* — [PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)

The reversibility upon Polδ restoration is strong evidence that the primary lesion is a **quantitative/qualitative Polδ-complex deficiency**, not an independent downstream defect—and it provides the conceptual rationale for gene/protein-restorative therapeutic strategies.

### Finding 4 — HSCT is the definitive therapy but carries DNA-repair-related conditioning-toxicity risk (F004)

For the closely related POLD1 deficiency, Keles et al. (2026) reported the first successful HSCT, noting that patients considered for HSCT may be at increased risk of regimen-related toxicity due to impaired DNA repair, and that **reduced-intensity conditioning (cyclophosphamide, fludarabine, ATG)** achieved engraftment with minimal toxicity.

> *"Patients considered for HSCT may be at increased risk of regimen-related toxicity due to impaired DNA repair"* — [PMID: 42104577](https://pubmed.ncbi.nlm.nih.gov/42104577/)

This mirrors the well-documented experience in other DNA-repair-defect SCIDs: in ARTEMIS (*DCLRE1C*) deficiency, alkylating agents are associated with poor growth and dental/endocrine late effects (Schuetz 2014, [PMID: 24144642](https://pubmed.ncbi.nlm.nih.gov/24144642/)), supporting a cautious, reduced-intensity conditioning approach in Polδ-complex disease.

### Finding 5 — Gene identifiers and population-genetic constraint consistent with recessive disease (F005)

POLD2 (DNA polymerase delta 2, accessory subunit): **HGNC:9176; NCBI Gene 5425; Ensembl ENSG00000106628; UniProt P49005; OMIM *600591.** Locus chr7p13 (GRCh38 chr7:44,114,631–44,124,407, minus strand). gnomAD v2 constraint indicates POLD2 is **NOT haploinsufficient** (heterozygous loss-of-function tolerated: pLI ≈ 0; LOEUF/oe_lof upper = 0.857; observed/expected LoF = 31/48.8) but is **missense-constrained** (missense Z = 2.68; LoF Z = 2.16). ClinVar lists ~429 POLD2 submissions, overwhelmingly VUS/likely-benign, with **no recurrent classified pathogenic CID allele**—disease variants are private/ultra-rare. The combination of LoF tolerance in heterozygotes plus missense constraint is exactly the signature expected of a **recessive disorder driven by biallelic hypomorphic (often missense) alleles**.

### Finding 6 — Disease nomenclature and identifiers: a "non-severe CID" (F006)

**MONDO:1010175** "POLD2-related combined immunodeficiency" (synonym "Polymerase D2 deficiency"); **GARD:0028136**; cataloged by Orphanet. The Orphanet/MONDO definition reads: *"A non-severe combined immunodeficiency due to polymerase delta deficiency in which the cause of the disease is a variation in the POLD2 gene."* The entity sits within the broader "polymerase delta deficiency" group alongside POLD1-related CID. Primary description: Conde et al., *J Clin Invest* 2019;129 (DOI 10.1172/jci128903).

> *"a novel syndrome with reduced functionality of the polymerase δ complex caused by germline biallelic mutations in POLD1 or POLD2"* — [PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)

### Finding 7 — POLD2 (p50) is the scaffolding subunit of both Polδ and Polζ, linking the defect to replication, repair, and antibody diversification (F007)

Per UniProt P49005, POLD2/p50 is an accessory component of **both** the DNA polymerase δ complex (POLD1/p125 + POLD2/p50 + POLD3/p66 + POLD4/p12) **and** the DNA polymerase ζ complex (REV3L, MAD2L2, POLD2, POLD3). Within Polδ, POLD2 directly interacts with POLD1, POLD3, and POLD4 but does **not** directly bind PCNA—i.e., it is the **central scaffold bridging the catalytic POLD1 to the PCNA-binding POLD3/POLD4.** Reactome maps POLD2 to a wide range of processes: processive leading/lagging-strand replication and Okazaki-fragment flap removal; mismatch repair (MutSα/MutSβ); PCNA-dependent long-patch base excision repair; nucleotide excision repair gap-filling; homologous-recombination repair; translesion synthesis termination; telomere C-strand synthesis; and crucially **"Somatic hypermutation of immunoglobulin genes by error-prone BER and error-prone MMR."**

> *"The polymerase δ complex is a heterotetramer comprising the catalytic subunit POLD1 and the accessory subunits POLD2, POLD3, and POLD4."* — [PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)

The dual membership in Polδ and Polζ, and the role in somatic hypermutation, explain why the defect can touch both **replication fidelity/genome stability** and **adaptive-immune receptor diversification**.

### Finding 8 — POLD2-related CID sits within a convergent PolD-complex T-cell immunodeficiency spectrum (F008)

The DNA polymerase δ-complex immunodeficiencies form an **allelic series with convergent T-cell phenotypes**:

- **POLD2 / POLD1 biallelic mutations** → syndromic CID with T-cell lymphopenia ± intellectual disability ± sensorineural hearing loss (Conde 2019 [PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/); Mehawej 2023 [PMID: 37030525](https://pubmed.ncbi.nlm.nih.gov/37030525/)).
- **POLD1 p.R1060C (c.3178C>T)** → recurrent/herpetic infections and T-cell lymphopenia with impaired T-cell but not B-cell proliferation, decreased naive CD4/CD8 T cells skewed to effector-memory, oligoclonality, and restricted TCRβ V-J pairing; mechanistically the mutation destabilizes Polδ, causes ineffective RFC recruitment, and disrupts the POLD1–POLD2 interaction (Cui 2020 [PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)).
- **POLD3 p.K373T (c.1118A>C)** → Omenn-syndrome SCID with severely decreased naive T cells, restricted TCR repertoire, defective early TCR recombination, S-phase entry defect, and excess dsDNA-break foci, rescued by WT POLD3; HSCT at 6 months, progressive neurological regression, death at age 4 (Riestra 2023 [PMID: 38099988](https://pubmed.ncbi.nlm.nih.gov/38099988/)).

> *"T-cell lymphopenia with impaired T-cell but not B-cell proliferation"* — [PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)

> *"the R1060C mutation disrupts the intramolecular interaction between the POLD1 CysB motif and the catalytic domain and also between POLD1 and the Polδ subunit POLD2"* — [PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)

> *"severely decreased numbers of naïve T cells associated with a restricted T-cell receptor repertoire and a defect in the early stages of TCR recombination"* — [PMID: 38099988](https://pubmed.ncbi.nlm.nih.gov/38099988/)

The POLD1 data directly demonstrate that the **POLD1–POLD2 interface** is critical for Polδ stability, which is the mechanistic reason POLD2 hypomorphs destabilize the holoenzyme and phenocopy the series.

### Finding 9 — Epidemiology and inheritance: ultra-rare autosomal-recessive with consanguinity contribution (F009)

POLD2-related CID is autosomal recessive, caused by biallelic POLD2 variants, and is **ultra-rare**—the human evidence base is essentially a single reported POLD2 index patient within a Polδ-complex spectrum of only a handful of cases. gnomAD gene-level constraint (pLI≈0; LOEUF≈0.86) indicates heterozygous LoF is tolerated, consistent with recessive inheritance and **asymptomatic carriers**; missense constraint (mis_z=2.68) indicates disease alleles are hypomorphic missense. **Consanguinity** is a recurring feature across the allelic series (e.g., the consanguineous Lebanese POLD3 family). Recurrence risk is **25% per pregnancy** for carrier couples; no founder effect, anticipation, germline mosaicism, or sex bias has been established.

> *"a consanguineous family"* — [PMID: 37030525](https://pubmed.ncbi.nlm.nih.gov/37030525/)

---

## Report by Disease-Characteristic Section

### 1. Disease Information

POLD2-related combined immunodeficiency is a **Mendelian, autosomal-recessive, syndromic non-severe combined immunodeficiency** caused by biallelic variants in *POLD2*. It is characterized by the triad of combined immunodeficiency (T-cell lymphopenia), neurodevelopmental impairment, and sensorineural hearing loss, on a background of cellular replicative stress (F001, F002, F006).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:1010175 ("POLD2-related combined immunodeficiency") |
| GARD | GARD:0028136 |
| Orphanet | Cataloged within "polymerase delta deficiency" group |
| OMIM (gene) | *600591 (POLD2); no separate phenotype MIM established for POLD2-CID at time of review |
| Gene HGNC | HGNC:9176 |
| ICD-10/ICD-11 | No disease-specific code; maps to D81.x "Combined immunodeficiencies" (ICD-10) / 4A01.1 (ICD-11, combined immunodeficiencies) |
| MeSH | No dedicated term; indexed under "Severe Combined Immunodeficiency" / "Primary Immunodeficiency Diseases" |

**Synonyms:** "Polymerase D2 deficiency"; "POLD2 deficiency"; part of "polymerase delta deficiency."

**Information source:** Aggregated disease-level resources (Orphanet, MONDO, OMIM) layered on top of **individual-patient case reports** in the primary literature. The evidence is predominantly from individual patients studied in research settings, not EHR-scale cohorts (F006).

### 2. Etiology

**Causal factor:** Purely **genetic**—germline biallelic (homozygous or compound heterozygous) hypomorphic variants in *POLD2* (F001). No environmental or infectious cause initiates the disease, though infections are the principal clinical consequence.

**Genetic risk factors:** The causal variants are the disease determinant. gnomAD constraint predicts disease alleles are **hypomorphic missense** variants (missense Z = 2.68), as complete biallelic LoF of this essential replication gene is likely incompatible with life (F005). **Consanguinity** is a major risk factor, enriching homozygosity for rare recessive alleles across the Polδ-complex series (F009).

**Environmental/lifestyle risk factors and protective factors:** None established. There are no known environmental modifiers, protective alleles, or gene–environment interactions documented for this ultra-rare disorder (not available).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity/Frequency | Evidence |
|---|---|---|---|---|---|
| T-cell lymphopenia | Lab abnormality | HP:0005403 (T-lymphocytopenia) | Infancy/childhood | Core feature; impaired T-cell proliferation | F002, F008 |
| Combined immunodeficiency / recurrent infections | Clinical sign | HP:0005354 (CID); HP:0002719 (recurrent infections) | Early childhood | Core; "non-severe" CID | F002, F006 |
| Decreased naive T cells / restricted TCR repertoire | Lab abnormality | HP:0045080 (decreased naive T cells)* | Childhood | Convergent across PolD series | F008 |
| Intellectual disability / neurodevelopmental impairment | Clinical sign | HP:0001249 (intellectual disability); HP:0012758 (neurodevelopmental delay) | Congenital/childhood | Variable ("with or without") | F002 |
| Sensorineural hearing loss | Physical manifestation | HP:0000407 (sensorineural hearing impairment) | Childhood | Recurrent syndromic feature | F002 |
| Replicative stress (cellular) | Lab/cellular | — | Constitutional | Reversible with Polδ overexpression | F003 |

*HPO term approximate; exact child term should be confirmed in the HPO browser.

**Quality-of-life impact:** Not formally measured (no EQ-5D/SF-36/PROMIS data). Expected burden derives from chronic infection susceptibility, developmental/cognitive impairment, and hearing loss affecting communication—collectively substantial but unquantified (not available).

### 4. Genetic/Molecular Information

- **Causal gene:** *POLD2* (HGNC:9176; NCBI Gene 5425; Ensembl ENSG00000106628; UniProt P49005; OMIM *600591), chr7p13 (F005).
- **Variant classification:** Disease alleles are private/ultra-rare; ClinVar (~429 POLD2 submissions) is dominated by VUS/likely-benign with **no recurrent pathogenic CID allele** established (F005). Per ACMG/AMP, pathogenicity in affected families rests on biallelic inheritance, rarity, and functional demonstration of Polδ destabilization.
- **Variant type:** Predominantly **missense** (hypomorphic), consistent with missense constraint; biallelic complete LoF is likely embryonic-lethal (F005).
- **Allele frequency:** Causal alleles are ultra-rare (absent/near-absent in gnomAD). Heterozygous LoF is tolerated (LOEUF≈0.86), so carriers exist in the population (F005, F009).
- **Origin:** Germline (F001). No somatic involvement.
- **Functional consequence:** Partial **loss of function** via destabilization of the Polδ holoenzyme / disruption of inter-subunit interactions (F003, F008).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established for POLD2 specifically (not available).

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents cause or trigger the disease. Infections (recurrent, including herpetic/opportunistic in the related POLD1 disease) are **consequences** of the immunodeficiency rather than etiologic agents (F008). (Not applicable as a cause.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Germline **biallelic hypomorphic POLD2 variants** reduce functional p50 scaffolding subunit → **leads to** destabilization of the DNA polymerase δ heterotetramer (and of Polζ, which shares POLD2) (F001, F007).
2. Destabilized/under-assembled Polδ → **results in** disrupted POLD1–POLD2 interaction and inefficient recruitment of replication machinery (RFC/PCNA loading) (F008, inferred from POLD1 R1060C data).
3. Impaired Polδ activity → **leads to** defective processive DNA synthesis and PCNA-dependent repair (MMR, long-patch BER, NER gap-filling, HR, TLS termination) (F007).
4. → **results in** **replication stress**: impaired S-phase progression and accumulation of replication-associated DNA lesions / double-strand breaks (F003; POLD3 data show excess dsDNA-break foci and S-phase entry defect, F008).
5. In highly proliferative **developing lymphocytes**, and during **TCR gene recombination/synthesis**, this replication stress → **leads to** a defect in early TCR recombination, loss of naive T cells, oligoclonality, and a **restricted TCR repertoire** (F008).
6. → **results in** **T-cell lymphopenia and impaired T-cell proliferation** (B-cell proliferation relatively spared) → clinical **combined immunodeficiency** with recurrent infections (F002, F008).
7. **Branch:** The same replication-stress mechanism in proliferating neural and cochlear progenitor tissues → **inferred to** contribute to **neurodevelopmental impairment** and **sensorineural hearing loss** (F002; mechanism for these tissues is inferred, not directly demonstrated).
8. Reversibility: Overexpression of Polδ in patient cells rescues the cell-cycle and DNA-damage phenotype, confirming the Polδ deficiency is the proximate cause (F003).

**Checklist coverage:** Molecular pathways — DNA replication (leading/lagging strand), PCNA-dependent repair, translesion synthesis via Polζ, somatic hypermutation of Ig genes (F007). Cellular processes — cell-cycle (S-phase) progression, DNA-damage response, lymphocyte proliferation (GO:0006260 DNA replication; GO:0006281 DNA repair; GO:0007049 cell cycle; GO:0042098 T cell proliferation). Protein dysfunction — loss of scaffolding function destabilizing a multi-subunit holoenzyme (F003, F007, F008). Immune involvement — immunodeficiency (primarily cellular/T-cell), with potential antibody-diversification impact via SHM (F007).

**Suggested ontology terms:** GO:0006260 (DNA replication), GO:0006281 (DNA repair), GO:0007049 (cell cycle), GO:0016446 (somatic hypermutation of immunoglobulin genes), GO:0042098 (T cell proliferation); CL:0000084 (T cell), CL:0000895 (naive thymus-derived CD4-positive, alpha-beta T cell), CL:0000900 (naive thymus-derived CD8-positive, alpha-beta T cell); subcellular GO:0005634 (nucleus), GO:0043625 (DNA polymerase delta complex).

### 7. Anatomical Structures Affected

- **Organ/system level:** **Immune system** (primary; UBERON:0002405), especially the **thymus** (UBERON:0002370) and the **T-lymphocyte compartment**; **central nervous system/brain** (UBERON:0000955) for the neurodevelopmental component; **inner ear/cochlea** (UBERON:0001844) for sensorineural hearing loss (F002).
- **Tissue/cell level:** **T lymphocytes** (CL:0000084), particularly **naive T cells** (CL:0000898), are the principal affected population (F008). Highly proliferative progenitor pools (neural progenitors, cochlear hair-cell/progenitor tissue) are implicated by inference.
- **Subcellular level:** **Nucleus** (GO:0005634) and the **replication fork / DNA polymerase δ complex** (GO:0043625); nuclear DNA is the site of the primary lesion (F003, F007).
- **Lateralization:** Hearing loss is expected bilateral (sensorineural); systemic immune/neurodevelopmental involvement is non-lateralized (inferred).

### 8. Temporal Development

- **Onset:** Congenital/pediatric. Immunodeficiency and neurodevelopmental features present in infancy/early childhood; the related POLD3 Omenn-SCID case presented in infancy with HSCT at 6 months (F008).
- **Progression:** The cellular defect is **constitutional and lifelong**. Clinical course ranges from "non-severe" CID (POLD2/POLD1) to severe, progressive disease in the POLD3 Omenn case (progressive neurological regression, death at age 4) (F006, F008).
- **Course pattern:** Chronic/progressive; infection-driven morbidity is recurrent. The critical intervention window is **early childhood**, before cumulative infectious/end-organ damage and ideally guiding timely HSCT (F004, F008).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; biallelic POLD2 variants (F001, F009).
- **Penetrance/expressivity:** Presumed high penetrance for biallelic pathogenic genotypes but **variable expressivity** (intellectual disability "with or without"; severity spans non-severe CID to Omenn syndrome across the series) (F002, F008).
- **Epidemiology:** Ultra-rare; no prevalence/incidence estimate exists. Human evidence ≈ a single POLD2 index patient within a handful of Polδ-complex cases (F009). Orphanet has not assigned a point-prevalence figure (not available).
- **Carrier frequency:** Not established; heterozygous LoF is tolerated (asymptomatic carriers exist) (F005, F009).
- **Consanguinity:** A recurring contributor across the allelic series (F009).
- **Founder effect / anticipation / mosaicism / sex ratio:** None established; no sex bias expected for an autosomal-recessive trait (F009).
- **Recurrence risk:** 25% per pregnancy for two carrier parents (F009).

### 10. Diagnostics

- **Laboratory/immunologic workup:** CBC with lymphocyte subsets (demonstrating **T-cell lymphopenia**, decreased naive T cells), lymphocyte proliferation assays (impaired T-cell proliferation), **TCR repertoire analysis** (restricted/oligoclonal), and **TREC** quantification (newborn-screening-relevant surrogate of thymic output) (F008; TREC/TCR methodology per [PMID: 19858778](https://pubmed.ncbi.nlm.nih.gov/19858778/)).
- **Functional/cellular biomarker:** Demonstration of **replicative stress**—impaired S-phase progression and replication-associated DNA lesions—reversible by Polδ overexpression, serves as a confirmatory functional assay (F003).
- **Genetic testing (definitive):** **WES or WGS** with biallelic POLD2 variant identification is the diagnostic standard; targeted CID/SCID gene panels increasingly include Polδ-complex genes. Single-gene POLD2 testing applies for cascade testing of known familial variants. Variant interpretation is challenging because most POLD2 variants are VUS, so **segregation plus functional validation** is often required (F005).
- **Audiology** (confirming sensorineural hearing loss) and **developmental/neurocognitive assessment** complete the syndromic evaluation (F002).
- **Differential diagnosis:** Other DNA-repair-defect SCID/CID (ARTEMIS/*DCLRE1C*, *LIG4*, Cernunnos/*NHEJ1*/XLF), RAG deficiency, and other syndromic CIDs with hearing loss/developmental delay; distinguished by gene identification and radiosensitivity profile (F004, F008; ARTEMIS context [PMID: 24144642](https://pubmed.ncbi.nlm.nih.gov/24144642/)).
- **Screening:** T-cell lymphopenia is detectable via **TREC-based newborn screening for SCID**, which could flag severe presentations (POLD3 Omenn-type), though "non-severe" POLD2 CID may not always trigger NBS thresholds (context: Israeli NBS program [PMID: 35487367](https://pubmed.ncbi.nlm.nih.gov/35487367/)).

### 11. Outcome/Prognosis

Prognosis is **variable and genotype/phenotype-dependent**. Non-severe CID (POLD2/POLD1) may be managed with supportive care, whereas severe Omenn-type presentations (POLD3) carry high early mortality—the reported POLD3 child had progressive neurological regression and died at age 4 despite HSCT at 6 months (F008). Successful HSCT in POLD1 deficiency demonstrates that the immune defect is **correctable**, improving infection-related prognosis (F004). The neurodevelopmental and hearing deficits are **not reversed** by HSCT (which addresses the hematopoietic compartment only), so these contribute to long-term morbidity/disability regardless of immune reconstitution (inferred). No formal survival statistics, QOL measures, or validated prognostic biomarkers exist given the tiny cohort (not available).

### 12. Treatment

| Modality | Specifics | NCIT (suggested) | Evidence |
|---|---|---|---|
| **Supportive/anti-infective** | Immunoglobulin replacement; antimicrobial prophylaxis (antibacterial/antifungal/antiviral) | NCIT:C603 (Immunoglobulin Therapy); NCIT:C305 (Antibiotic) | Standard-of-care for CID (inferred) |
| **Allogeneic HSCT (definitive)** | Reduced-intensity conditioning (cyclophosphamide, fludarabine, ATG) to limit DNA-repair-related toxicity | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) | F004; [PMID: 42104577](https://pubmed.ncbi.nlm.nih.gov/42104577/) |
| **Conditioning caution** | Avoid/minimize alkylating-agent intensity due to impaired DNA repair (late growth, dental, endocrine toxicity in related DNA-repair SCID) | — | F004; [PMID: 24144642](https://pubmed.ncbi.nlm.nih.gov/24144642/) |
| **Rehabilitative/supportive** | Hearing amplification/cochlear implant for sensorineural loss; developmental/educational support | NCIT:C15215 (Rehabilitation Therapy) | F002 (inferred) |
| **Gene/protein-restorative (experimental concept)** | Proof-of-concept that Polδ overexpression reverses the cellular phenotype supports future gene-correction approaches | — | F003 (conceptual only) |

No pharmacogenomic, RNA-based, or targeted-molecular therapies are established. No disease-specific clinical trials (NCT identifiers) were identified for POLD2 CID (not available).

### 13. Prevention

- **Primary prevention:** Not possible for the genetic cause. **Genetic counseling** for consanguineous/carrier families, **carrier screening**, and reproductive options (prenatal diagnosis, preimplantation genetic testing) are the principal preventive levers given the 25% recurrence risk (F009).
- **Secondary prevention:** **TREC-based newborn screening** can detect T-cell lymphopenia early, enabling timely intervention/HSCT before severe infection ([PMID: 35487367](https://pubmed.ncbi.nlm.nih.gov/35487367/)); cascade testing of relatives once a familial variant is known.
- **Tertiary prevention:** Infection prophylaxis, immunoglobulin replacement, avoidance of live vaccines, and audiologic/developmental support to prevent complications (inferred standard CID management).

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** POLD2 is **highly evolutionarily conserved** (an essential replication subunit). Mouse ortholog *Pold2* (*Mus musculus*, NCBI Taxon 10090); orthologs extend to zebrafish, *Drosophila*, and *S. cerevisiae* (POL31), reflecting core replisome conservation (inferred from gene function, F007).
- **Natural disease in other species:** No naturally occurring POLD2-deficiency disease is cataloged in OMIA for companion animals or wildlife (not available).
- **Comparative/zoonotic:** Not applicable (non-infectious, non-zoonotic genetic disorder).

### 15. Model Organisms

No published, purpose-built animal model of POLD2-related CID was identified in this investigation. Relevant and feasible systems (largely inferred/extrapolated):

- **Patient-derived cells (in vitro):** The best-validated system—patient fibroblasts/lymphocytes demonstrating replicative stress, impaired S-phase, and DNA lesions, with rescue by Polδ overexpression (F003). This is the key functional-validation platform.
- **Mouse (*Pold2*):** Constitutive biallelic knockout is expected to be embryonic-lethal (essential gene); **hypomorphic/conditional (e.g., lymphocyte-specific) knock-in of patient-equivalent missense alleles** would be the logical model to recapitulate T-cell-restricted replication stress (inferred; no existing model confirmed).
- **Yeast (*S. cerevisiae* POL31):** Tractable for dissecting subunit-interaction and holoenzyme-stability effects of specific variants (inferred).

**Limitations of models:** Mouse models cannot fully capture human neurodevelopmental/hearing phenotypes, and the lethality of complete LoF constrains modeling to hypomorphic alleles.

---

## Mechanistic Model / Interpretation

```
  Biallelic hypomorphic POLD2 (p50) variants
                 │  (loss of scaffolding subunit)
                 ▼
  Destabilized DNA polymerase δ holoenzyme  ── also destabilizes Polζ (shared POLD2)
                 │  (disrupted POLD1–POLD2 interface; poor RFC/PCNA coupling)
                 ▼
  Impaired processive replication + PCNA-dependent repair (MMR/BER/NER/HR/TLS)
                 │
                 ▼
  REPLICATION STRESS: S-phase arrest + replication-associated DNA lesions / dsDNA breaks
        (reversible by Polδ overexpression — proves Polδ is proximate cause)
                 │
      ┌──────────┴───────────────────────────────┐
      ▼                                           ▼
  Proliferating developing T cells            Proliferating neural / cochlear
  + TCR recombination/synthesis defect         progenitor tissues (INFERRED)
      │                                           │
      ▼                                           ▼
  Loss of naive T cells, restricted TCR,     Neurodevelopmental impairment
  impaired T-cell proliferation               + sensorineural hearing loss
      │
      ▼
  T-cell lymphopenia → COMBINED IMMUNODEFICIENCY → recurrent infections
```

The unifying theme is that **a general-purpose genome-maintenance defect produces a tissue-selective phenotype** because the most proliferation-dependent lineages (developing lymphocytes above all) are most vulnerable to replication stress. The convergence of POLD1, POLD2, and POLD3 variants on the same naive-T-cell-loss/restricted-TCR phenotype (F008) is the strongest cross-validation of this model, and the demonstrated POLD1–POLD2 physical interface (F008) supplies the molecular reason a POLD2 hypomorph destabilizes the whole complex.

### Allelic series comparison (Polδ-complex immunodeficiencies)

| Gene | Representative variant | Severity | Key immune phenotype | Neuro / hearing | Outcome | Evidence |
|---|---|---|---|---|---|---|
| **POLD2** | Private biallelic (hypomorphic) | Non-severe CID | T-cell lymphopenia, replicative stress | ± Intellectual disability, SNHL | Supportive ± HSCT (inferred) | F001, F002, F006 |
| **POLD1** | p.R1060C; biallelic | CID | T-cell lymphopenia, impaired T (not B) proliferation, naive-T loss, restricted TCRβ | ± Intellectual disability, SNHL | First successful HSCT reported | F004, F008 |
| **POLD3** | p.K373T | Severe (Omenn SCID) | Severe naive-T loss, restricted TCR, early-TCR-recombination defect, dsDNA breaks | Progressive neuro regression | HSCT at 6 mo; died age 4 | F008 |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/) | *Polymerase δ deficiency causes syndromic immunodeficiency with replicative stress* | **Primary/defining paper.** Establishes gene (POLD1/POLD2), AR inheritance, triad, reversible replicative-stress mechanism (F001, F002, F003, F006, F007) |
| [37030525](https://pubmed.ncbi.nlm.nih.gov/37030525/) | *POLD3 deficiency… neurodevelopmental delay and hearing impairment* | Summarizes POLD1/POLD2 syndromic CID phenotype; documents consanguinity (F002, F009) |
| [31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/) | *CID caused by loss-of-function mutation in POLD1* | Defines T-cell proliferation defect and the critical POLD1–POLD2 interface (F008) |
| [38099988](https://pubmed.ncbi.nlm.nih.gov/38099988/) | *POLD3 deficiency presenting as Omenn syndrome* | Severe-end phenotype; naive-T-cell loss, restricted TCR, TCR-recombination defect (F008) |
| [42104577](https://pubmed.ncbi.nlm.nih.gov/42104577/) | *Successful treatment of POLD1 deficiency with HSCT* | Definitive therapy; DNA-repair conditioning-toxicity caution (F004) |
| [24144642](https://pubmed.ncbi.nlm.nih.gov/24144642/) | *ARTEMIS vs RAG SCID following HCT* | Supports reduced-intensity conditioning in DNA-repair-defect SCID (F004) |
| [35487367](https://pubmed.ncbi.nlm.nih.gov/35487367/) | *5 years of SCID newborn screening in Israel* | TREC-based NBS context for early detection/consanguinity (Sections 10, 13) |
| [19858778](https://pubmed.ncbi.nlm.nih.gov/19858778/) | *Molecular assessment of thymus capabilities* | TREC/TCR-repertoire methodology for diagnostics (Section 10) |

All mechanistic and clinical attributions above are grounded in the verified citation snippets in the knowledge state; POLD1/POLD3 findings are applied to POLD2 by explicit analogy within the shared-mechanism allelic series, and are flagged as such.

---

## Limitations and Knowledge Gaps

1. **N≈1 for POLD2 specifically.** The POLD2 subtype rests on essentially a single reported index patient; the exact index variant(s), zygosity details, and individual clinical trajectory are not resolved in the available knowledge state. Much of the clinical/therapeutic detail is **extrapolated** from POLD1 and POLD3 disease.
2. **No epidemiology.** No prevalence, incidence, carrier frequency, sex ratio, or geographic data exist beyond "ultra-rare" and a consanguinity association.
3. **Inferred extra-immune mechanism.** The link from replication stress to neurodevelopmental impairment and sensorineural hearing loss is biologically plausible but **not directly demonstrated** at the tissue level.
4. **Variant interpretation is hard.** ClinVar POLD2 entries are overwhelmingly VUS; there is no recurrent, consensus-classified pathogenic CID allele, so diagnosis requires functional validation.
5. **No dedicated animal model** of POLD2-CID and **no disease-specific clinical trials** were identified.
6. **No QOL/prognostic/mortality statistics** specific to POLD2 exist.
7. **Ontology mappings** (several HPO/GO/CL/UBERON terms above) are suggested and should be verified against current ontology releases before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate cases via GeneMatcher / ESID / inborn-errors-of-immunity registries** to assemble a POLD2 cohort large enough to define penetrance, expressivity, and natural history.
2. **Functional variant pipeline:** Establish a standardized assay (Polδ-complex stability by co-IP, S-phase/EdU replication-stress readout, dsDNA-break foci, rescue by WT POLD2) to reclassify POLD2 VUS per ACMG functional-evidence criteria (PS3/BS3).
3. **Generate a conditional/hypomorphic *Pold2* mouse** (lymphocyte-specific or patient-equivalent knock-in) to test the replication-stress → T-cell-defect causal chain and probe neural/cochlear involvement.
4. **Single-cell immune profiling** (scRNA-seq + TCR-seq) of patient thymic emigrants/peripheral T cells to map where in T-cell development the block occurs and quantify TCR-repertoire restriction.
5. **HSCT outcome registry** for Polδ-complex deficiencies to formalize reduced-intensity conditioning protocols and quantify DNA-repair-related toxicity.
6. **Audiologic and neurodevelopmental longitudinal follow-up** post-HSCT to determine which deficits are reversible vs. fixed, informing counseling.
7. **Carrier-screening / prenatal counseling resources** for consanguineous families, including cascade-testing workflows once a familial POLD2 variant is identified.

---

*Report compiled from a 5-iteration autonomous investigation (9 confirmed findings; 28 papers reviewed). Evidence types: predominantly human clinical case reports and in vitro functional studies, with population-genetic constraint data (gnomAD) and cross-disorder analogy to POLD1/POLD3 deficiencies.*


## Artifacts

- [OpenScientist final report](POLD2-related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](POLD2-related_Combined_Immunodeficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 8 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005354` (obsolete Absent cellular immunity) (1 mention) - replaced by `HP:0011840`
- `HP:0045080` (obsolete Decreased CD3+ T cell proportion) (1 mention) - replaced by `HP:0005403`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005403` (1 mention) - the report calls it "T-lymphocytopenia"; HP calls it **Decreased total T cell count**, and lists "T lymphocytopenia" among its other names
- `HP:0045080` (1 mention) - the report calls it "decreased naive T cells"; HP calls it **obsolete Decreased CD3+ T cell proportion**
- `CL:0000084` (2 mentions) - the report calls it "T cell", "T lymphocytes", "Tissue/cell level:** **T lymphocytes"; CL calls it **T cell**, and lists "T lymphocyte" among its other names
- `GO:0005634` (2 mentions) - the report calls it "nucleus", "Nucleus", "Subcellular level:** **Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `GO:0043625` (2 mentions) - the report calls it "DNA polymerase delta complex", "replication fork / DNA polymerase δ complex"; GO calls it **delta DNA polymerase complex**
- `UBERON:0000955` (1 mention) - the report calls it "central nervous system/brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `UBERON:0001844` (1 mention) - the report calls it "inner ear/cochlea"; UBERON calls it **cochlea**
- `NCIT:C15215` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Cryosurgery**, and lists "Ablation, Cryo" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000084` - called "T cell", "T lymphocytes", "Tissue/cell level:** **T lymphocytes"
- `GO:0005634` - called "nucleus", "Nucleus", "Subcellular level:** **Nucleus"
- `GO:0043625` - called "DNA polymerase delta complex", "replication fork / DNA polymerase δ complex"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`.

25 of 29 terms resolved to a current term; the rest could not be looked up either way.