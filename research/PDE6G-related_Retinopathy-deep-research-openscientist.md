---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:01:06.934381'
end_time: '2026-10-30T23:45:22.997846'
duration_seconds: 2656.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PDE6G-Related Retinopathy
  mondo_id: MONDO:1040034
  category: Mendelian
  causal_genes: PDE6G
  omim_id: not recorded
  synonyms: Retinitis pigmentosa 57; RP57
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
citation_count: 10
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.4.0
term_validation:
  total_terms: 35
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 10
  labels_variant: 4
  unresolvable_prefixes:
  - Gene
  - OMIM
  - NCBIGene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PDE6G-related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PDE6G-related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PDE6G-Related Retinopathy
- **MONDO ID:** MONDO:1040034 (if available)
- **Causal gene(s):** PDE6G
- **OMIM:** not recorded
- **Synonyms:** Retinitis pigmentosa 57; RP57
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PDE6G-Related Retinopathy** covering all of the
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

# PDE6G-Related Retinopathy (Retinitis Pigmentosa 57, RP57): A Comprehensive Disease Characterization

**Disease:** PDE6G-Related Retinopathy | **Causal gene:** **PDE6G** (phosphodiesterase 6G, rod cGMP-specific, γ-subunit; HGNC:8788; NCBI Gene:5148)
**MONDO:** MONDO:1040034 (also mapped as MONDO:0013315) | **OMIM:** #613582 | **Synonyms:** Retinitis pigmentosa 57; RP57
**Category:** Mendelian, autosomal recessive

---

## Summary

PDE6G-Related Retinopathy (Retinitis Pigmentosa 57, RP57; OMIM #613582) is a severe, early-onset, autosomal-recessive rod–cone dystrophy caused by biallelic **loss-of-function of PDE6G**, the gene encoding the 87-amino-acid inhibitory γ-subunit (Pγ) of rod photoreceptor cGMP phosphodiesterase (PDE6). PDE6 is the central effector enzyme of the rod phototransduction cascade: light-activated transducin relieves Pγ-mediated inhibition of the PDE6 catalytic dimer (PDE6A/PDE6B), triggering rapid cGMP hydrolysis, closure of cGMP-gated cation channels, and photoreceptor hyperpolarization. When Pγ is lost, this inhibitory control collapses, cGMP homeostasis is dysregulated, and rod photoreceptors degenerate early and rapidly, followed by secondary cone loss — the hallmark of retinitis pigmentosa. The disease was defined in a single consanguineous Muslim Arab-Israeli kindred in which genome-wide homozygosity mapping localized a 4.7-Mb region on chromosome 17q25.3 and identified the pathogenic splice-donor variant **c.187+1G>T** ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)).

The clinical picture is a classic but severe rod–cone dystrophy: markedly constricted visual fields, severely reduced or extinguished scotopic and photopic electroretinograms (ERG), midperipheral bone-spicule pigmentation, optic disc pallor, attenuated retinal vessels, loss of foveal reflex, and cystoid macular edema. Onset is in childhood, and inheritance is strictly autosomal recessive. The official Human Phenotype Ontology (HPO) annotation set for OMIM:613582 comprises ten terms, all sourced to the founding family report.

RP57 is one of the rarest genetic subtypes of a genetically heterogeneous disease group (retinitis pigmentosa, >90 causative genes, overall prevalence ~1/4000). Population genomics (gnomAD v4) show PDE6G is **loss-of-function-tolerant in heterozygotes** (pLI ≈ 0.0004; observed/expected LoF = 0.91), consistent with a recessive gene whose carriers are healthy; the estimated carrier frequency is ~1 in 6,600 and the random-mating affected frequency ~1 in 170 million, explaining why cases essentially require consanguinity. ClinVar documents a small loss-of-function allelic series (nonsense, frameshift, essential-splice, start-loss) plus large 17q25.3 copy-number events. There is currently no approved therapy; management is supportive, but PDE6-related RP is among the most tractable targets for AAV-mediated gene supplementation, which has achieved durable rescue even at advanced disease stages in related PDE6 models. A theoretical pharmacologic caution applies: PDE6-cross-reactive inhibitors (e.g., sildenafil) selectively impair retinal function in PDE6-γ-deficient mice.

---

## Key Findings

### Finding 1 — PDE6G loss-of-function causes autosomal-recessive early-onset RP (RP57)

Dvir and colleagues performed genome-wide homozygosity mapping in two sibships of an extended consanguineous Muslim Arab-Israeli family with severe early-onset autosomal-recessive RP, mapping a shared 4.7-Mb homozygous region on chromosome 17q25.3 that contains **PDE6G** ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)). Sequencing of all coding exons and exon–intron boundaries revealed a homozygous single-base change, **c.187+1G>T**, in the conserved intron 3 donor splice site. The variant cosegregated with disease, and an in vitro splicing assay confirmed aberrant splicing. As the authors state: *"Sequencing of all coding exons, including exon-intron boundaries, revealed a homozygous single base change (c.187+1G>T) located in the conserved intron 3 donor splice site of PDE6G."* They further note that *"One of the genes located in this interval is PDE6G, encoding for the inhibitory gamma subunit of rod photoreceptor cyclic GMP-phosphodiesterase."* This established PDE6G as the causal gene of RP57 (MONDO:1040034). **Evidence type:** human clinical/genetic.

### Finding 2 — Clinical phenotype: severe rod–cone dystrophy with extinguished ERG and macular edema

In the founding family, affected individuals had *"markedly constricted visual fields"* and *"Both scotopic and photopic electroretinograms were severely reduced or completely extinct,"* indicating combined rod and cone dysfunction ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)). Funduscopy showed *"typical bone spicule-type pigment deposits spread mainly at the midperiphery, as well as pallor of the optic disk."* Macular involvement included loss of the foveal reflex and cystoid macular edema confirmed on optical coherence tomography (OCT). These features situate RP57 within the classic RP clinical spectrum (worldwide RP prevalence ~1/4000) but at the severe, early-onset end. **Evidence type:** human clinical.

### Finding 3 — Mechanism: PDE6 γ-subunit loss dysregulates cGMP hydrolysis in rod outer segments, driving photoreceptor death

PDE6 is the central effector enzyme of the rod/cone phototransduction cascade — a tetramer of two catalytic subunits (rod PDE6A/PDE6B) and two inhibitory γ-subunits (rod PDE6G). As reviewed, *"As the central effector enzyme of the G-protein coupled visual transduction pathway, activation of PDE6 catalysis causes a rapid decrease in cGMP levels that results in closure of cGMP-gated ion channels in the photoreceptor plasma membrane"* ([PMID: 34170501](https://pubmed.ncbi.nlm.nih.gov/34170501/)), and *"mutations in PDE6 genes result in various retinal diseases that currently lack therapeutic treatment strategies."* In vivo mouse studies of PDE6γ mutants demonstrate that the γ-subunit normally restrains dark PDE6 activity: ILE86TER rods *"showed a decreased rate of decay of the photoresponse, consistent with decreased inhibition of PDE6 α and β by PDE6γ. Furthermore, ILE86TER rods had a higher rate of spontaneous activation of PDE6 than WT rods"* ([PMID: 21920434](https://pubmed.ncbi.nlm.nih.gov/21920434/)). Loss of Pγ therefore dysregulates cGMP signaling and reduces holoenzyme stability, the upstream lesion that triggers photoreceptor death. **Evidence type:** in vitro / model organism / review.

### Finding 4 — Pde6g-deficient mouse recapitulates early-onset RP; PDE6-RP is gene-therapy-tractable even at late stages

A *Pde6g* preclinical mouse model exhibits *"early onset and rapid rod degeneration, with the vast majority gone by P16,"* leading to retinal remodeling of inner retinal neurons, RPE, and vasculature, including acellular capillaries ([PMID: 37363133](https://pubmed.ncbi.nlm.nih.gov/37363133/)) — faithfully reproducing the severe, early human phenotype. In the related *Pde6b* RP model, restoring the wild-type gene in rod photoreceptors produced *"stable, sustained rescue of photoreceptor structure and function for at least 1 year, demonstrating gene therapy efficacy after onset of degeneration"* ([PMID: 29721933](https://pubmed.ncbi.nlm.nih.gov/29721933/)). A therapeutic window exists: *"when fewer than 13% of rods remain, our genetic rescue halts photoreceptor degeneration, electroretinography (ERG) functional decline and inner retinal remodeling"* at 16 weeks, whereas treatment at 24 weeks failed ([PMID: 35195763](https://pubmed.ncbi.nlm.nih.gov/35195763/)). **Evidence type:** model organism.

### Finding 5 — PDE6G-RP is an ultra-rare subtype within genetically heterogeneous RP (>90 genes)

RP is a group of inherited retinal diseases affecting >1 million people worldwide that *"show tremendous genetic and phenotypic heterogeneity, involving over 90 genes in its causation"* ([PMID: 40575766](https://pubmed.ncbi.nlm.nih.gov/40575766/)); no curative treatment exists, though gene therapy, stem cells, optogenetics, retinal prosthetics, and pharmacotherapy are emerging. Within this landscape, PDE6G/RP57 is among the rarest causes — the defining disease was described in a single consanguineous Arab-Israeli kindred, against an overall RP prevalence of *"1 in 4000"* ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)). **Evidence type:** review / human clinical.

### Finding 6 — Gene–drug interaction: PDE6-inhibiting drugs (sildenafil) selectively impair retinal function in PDE6-γ-deficient mice

In mice heterozygous for the *Pde6g*-null allele (PDEG tm1/+), the PDE5/PDE6 inhibitor sildenafil produced a reversible, dose-dependent decrease in ERG a- and b-wave amplitudes, while wild-type mice were unaffected: *"ERGs of the PDEG:(tm1)/+ mice treated with sildenafil showed a reversible, dose-dependent decrease in a- and b-wave amplitudes. Wild-type mice treated with sildenafil did not show significant differences"* ([PMID: 11157892](https://pubmed.ncbi.nlm.nih.gov/11157892/)). This reveals heightened sensitivity of PDE6-γ-compromised retina to pharmacologic PDE6 inhibition and motivates a theoretical caution for carriers/patients exposed to PDE5/PDE6-cross-reactive drugs. **Evidence type:** model organism.

### Finding 7 — gnomAD: PDE6G is LoF-tolerant in heterozygotes (recessive); carrier frequency ~1/6,600

gnomAD v4 shows PDE6G (ENSG00000185527; chr17:81,650,459–81,663,112; 4 exons) is **not** loss-of-function-constrained: pLI ≈ 0.0004, observed/expected LoF = 0.91 (observed 10 / expected 10.95), LoF Z = 0.24 — consistent with a recessive gene whose heterozygous LoF carriers are healthy. High-confidence truncating alleles are each ultra-rare (AF 1.4×10⁻⁶ to 6.8×10⁻⁶; e.g., p.Arg33Ter AC = 10, AF 6.8×10⁻⁶). The founding RP57 allele c.187+1G>T is present at AC = 2/1,461,730 (AF 1.37×10⁻⁶). Summing high-confidence LoF alleles gives q ≈ 7.6×10⁻⁵ → estimated carrier frequency ~1.5×10⁻⁴ (**≈1 in 6,600**) and random-mating affected frequency q² ≈ 5.8×10⁻⁹ (**≈1 in 170 million**). This quantitatively explains the ultra-rarity and consanguinity dependence; cases arise via homozygosity-by-descent, as in the founding family (*"Genome-wide homozygosity mapping was conducted in two sibships from an extended consanguineous Muslim Arab Israeli family,"* [PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)). **Evidence type:** computational / population genomics.

### Finding 8 — ClinVar documents a loss-of-function allelic series in PDE6G beyond the founding variant

ClinVar contains 149 PDE6G records (22 Pathogenic, 4 Likely pathogenic, 6 Conflicting, 66 VUS, 41 Likely benign, 8 Benign, 2 Benign/Likely benign). PDE6G-specific pathogenic/likely-pathogenic small variants include the founding splice-donor c.187+1G>T (Pathogenic), a second essential-splice variant c.146+1G>T (Pathogenic), the nonsense c.97C>T/p.Arg33Ter (Pathogenic), the frameshift c.69dup/p.Arg24fs (Pathogenic), and the start-loss c.2T>A/p.Met1Lys (Likely pathogenic); c.95del/p.Gln32fs and c.206del/p.Pro69fs are Conflicting. Large 17q25.3 copy-number gains (×3 duplications) and deletions spanning PDE6G are also catalogued as Pathogenic (contiguous multi-gene events). The founding c.187+1G>T allele anchors this series: *"revealed a homozygous single base change (c.187+1G>T) located in the conserved intron 3 donor splice site of PDE6G"* ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)). The uniform LoF nature of pathogenic alleles confirms a loss-of-function disease mechanism. **Evidence type:** variant database curation.

### Finding 9 — Official HPO disease annotations for RP57 retrieved and integrated

The JAX HPO Annotation Network for OMIM:613582 (RP57; gene NCBIGene:5148 = PDE6G) returns ten phenotype annotations, all sourced to [PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/): Reduced visual acuity (HP:0007663, frequency 6/6), Constriction of peripheral visual field (HP:0001133, 4/4), Rod-cone dystrophy (HP:0000510), Spicular pigmentation of the retina (HP:0007737), Optic disc pallor (HP:0000543, young-adult onset), Absent foveal reflex (HP:0030825), Cystoid macular edema (HP:0011505), Attenuation of retinal blood vessels (HP:0007843), Childhood onset (HP:0011463), and Autosomal recessive inheritance (HP:0000007). The single source documents the constricted fields and extinguished rod+cone ERG that define the phenotype set. **Evidence type:** ontology curation / human clinical.

---

## Section-by-Section Report

### 1. Disease Information

PDE6G-Related Retinopathy is **Retinitis Pigmentosa 57 (RP57)**, a severe autosomal-recessive, early-onset rod–cone dystrophy caused by biallelic loss-of-function of **PDE6G**. It is an inherited retinal degeneration in which rod photoreceptors degenerate first, followed by cones, producing progressive loss of peripheral and night vision and eventual central visual loss.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #613582 |
| OMIM (gene PDE6G) | *180073 / 614494 |
| MONDO | MONDO:1040034 (also MONDO:0013315) |
| Gene (HGNC) | HGNC:8788, PDE6G |
| NCBI Gene | 5148 |
| Ensembl | ENSG00000185527 |
| Locus | 17q25.3 |

**Synonyms:** Retinitis pigmentosa 57; RP57; PDE6G-related retinitis pigmentosa. **Information source type:** Aggregated disease-level resources (OMIM, Orphanet, HPO, ClinVar, gnomAD) and primary literature, principally the founding family case series (not large EHR-derived cohorts).

### 2. Etiology

**Causal factor:** Purely genetic — biallelic loss-of-function variants in PDE6G. The founding pathogenic allele is the intron-3 essential-splice variant c.187+1G>T ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)); ClinVar documents additional nonsense, frameshift, essential-splice, and start-loss alleles plus 17q25.3 CNVs (Finding 8).

**Genetic risk factors:** The principal risk factor is **consanguinity** / homozygosity-by-descent. Because PDE6G is LoF-tolerant in heterozygotes (carrier ~1/6,600; Finding 7), affected individuals almost always inherit two null alleles identical by descent, so a family history of consanguinity dramatically raises risk. No common susceptibility loci or modifier genes are established.

**Environmental risk factors:** None established as causal. A pharmacologic gene–drug interaction exists (PDE6-cross-reactive inhibitors such as sildenafil selectively impair retinal function in PDE6-γ-deficient animals; Finding 6), which is a theoretical exacerbating exposure rather than a cause.

**Protective factors:** None specifically documented. By analogy to other RP forms, avoidance of excessive light exposure and general ocular health measures are prudent but unproven for RP57.

**Gene–environment interactions:** The best-documented interaction is pharmacologic (PDE6-inhibitor sensitivity; Finding 6). No dietary or toxicant GxE interactions are established.

### 3. Phenotypes

All ten official HPO annotations derive from the founding family ([PMID: 20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/)); see Finding 9.

| Phenotype | HPO term | Type | Frequency | Onset/Course |
|---|---|---|---|---|
| Rod-cone dystrophy | HP:0000510 | Clinical sign (ERG/functional) | Characteristic | Childhood onset, progressive |
| Reduced visual acuity | HP:0007663 | Symptom | 6/6 | Progressive |
| Constriction of peripheral visual field | HP:0001133 | Clinical sign | 4/4 | Progressive |
| Spicular (bone-spicule) retinal pigmentation | HP:0007737 | Physical manifestation | Characteristic | Midperipheral |
| Optic disc pallor | HP:0000543 | Clinical sign | Present | Young-adult onset (HP:0011462) |
| Absent foveal reflex | HP:0030825 | Clinical sign | Present | — |
| Cystoid macular edema | HP:0011505 | Clinical sign (OCT) | Present | Variable |
| Attenuation of retinal blood vessels | HP:0007843 | Clinical sign | Present | Young-adult onset |
| Childhood onset | HP:0011463 | Onset modifier | — | — |
| Autosomal recessive inheritance | HP:0000007 | Inheritance modifier | — | — |

**Severity:** Severe — scotopic and photopic ERGs are severely reduced or extinguished, indicating combined rod and cone dysfunction. **Progression:** Progressive, consistent with RP natural history. **Quality-of-life impact:** Severe and lifelong — progressive peripheral then central vision loss causes major functional disability (mobility, reading, driving), with cystoid macular edema further threatening central acuity. Disease-specific QoL instruments for RP57 are not available; general RP QoL burden applies.

### 4. Genetic / Molecular Information

**Causal gene:** PDE6G (HGNC:8788; Gene 5148; ENSG00000185527; 17q25.3; 4 exons) encoding Pγ, the 87-aa inhibitory γ-subunit of rod PDE6.

**Pathogenic variants (ClinVar; Finding 8):**

| Variant | Protein | Type | Classification |
|---|---|---|---|
| c.187+1G>T | — (intron-3 donor) | Essential splice | Pathogenic (founding allele) |
| c.146+1G>T | — | Essential splice | Pathogenic |
| c.97C>T | p.Arg33Ter | Nonsense | Pathogenic |
| c.69dup | p.Arg24fs | Frameshift | Pathogenic |
| c.2T>A | p.Met1Lys | Start-loss | Likely pathogenic |
| c.95del | p.Gln32fs | Frameshift | Conflicting |
| c.206del | p.Pro69fs | Frameshift | Conflicting |
| 17q25.3 gains/deletions | — | CNV (multi-gene) | Pathogenic |

**Variant class:** All established pathogenic small variants are loss-of-function (nonsense, frameshift, essential-splice, start-loss). **Allele frequencies (gnomAD v4; Finding 7):** all ultra-rare — c.187+1G>T AF 1.37×10⁻⁶; p.Arg33Ter AF 6.8×10⁻⁶; summed high-confidence LoF q ≈ 7.6×10⁻⁵. **Origin:** Germline. **Functional consequence:** Loss of function (loss of the inhibitory γ-subunit; reduced holoenzyme stability and dysregulated dark PDE6 activity — Finding 3).

**Modifier genes:** None established for RP57. **Epigenetic information:** None specifically reported for this disease. **Chromosomal abnormalities:** Large 17q25.3 copy-number gains and deletions spanning PDE6G are catalogued in ClinVar as contiguous multi-gene events rather than isolated PDE6G lesions.

### 5. Environmental Information

**Environmental factors:** None causal. **Lifestyle factors:** None established. **Infectious agents:** Not applicable — RP57 is a monogenic inherited retinal degeneration. The one relevant non-genetic consideration is iatrogenic: systemic PDE6-cross-reactive inhibitors (sildenafil and related PDE5 inhibitors) selectively reduce retinal function in PDE6-γ-deficient animals (Finding 6), suggesting a theoretical avoidance recommendation.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A biallelic loss-of-function variant in **PDE6G** (e.g., c.187+1G>T essential-splice) **leads to** absent or non-functional rod Pγ inhibitory subunit. *(Demonstrated: founding family + splicing assay, [PMID: 20655036].)*
2. Loss of Pγ **results in** loss of inhibitory control over the rod PDE6 catalytic dimer (PDE6A/PDE6B) and reduced PDE6 holoenzyme expression/stability. *(Demonstrated in vivo in PDE6γ-mutant mice: increased spontaneous dark PDE6 activity, [PMID: 21920434].)*
3. Dysregulated PDE6 catalysis **leads to** abnormal cGMP hydrolysis and disrupted cGMP homeostasis in rod outer segments (the cascade in which PDE6 activation normally drops cGMP to close CNG channels, [PMID: 34170501]). *(Inferred for the human null state from the central role of PDE6 in phototransduction.)*
4. Disrupted cGMP/CNG-channel signaling and phototransduction failure **result in** rod photoreceptor dysfunction (extinguished scotopic ERG) and **lead to** rapid rod photoreceptor death. *(Demonstrated in the Pde6g mouse: most rods gone by P16, [PMID: 37363133].)*
5. Rod loss **leads to** secondary (non-cell-autonomous) cone photoreceptor death — the branch producing extinguished photopic ERG and eventual central vision loss. *(Inferred from the extinguished photopic ERG in patients [PMID: 20655036] and the general RP paradigm of secondary cone death.)*
6. Progressive photoreceptor loss **results in** inner-retinal remodeling, RPE and vascular changes (attenuated vessels, acellular capillaries), bone-spicule pigment migration, optic disc pallor, and cystoid macular edema — the clinical RP phenotype. *(Demonstrated remodeling in the Pde6g mouse, [PMID: 37363133]; clinical signs, [PMID: 20655036].)*

**Molecular pathway:** Rod cGMP phototransduction (G-protein-coupled; rhodopsin → transducin → PDE6 → cGMP/CNG channel). **Cellular processes:** Photoreceptor cell death (apoptosis/remodeling), retinal remodeling. **Protein dysfunction:** Loss of function of Pγ, the intrinsically disordered inhibitory subunit, with loss of holoenzyme regulation and stability. **Biochemical abnormality:** Dysregulated cGMP-specific phosphodiesterase activity → cGMP imbalance. **Metabolic link:** cGMP second-messenger metabolism.

**Suggested GO terms:** phototransduction (GO:0007602); detection of light stimulus involved in visual perception (GO:0050908); cGMP metabolic process (GO:0046068); 3',5'-cyclic-GMP phosphodiesterase activity (GO:0047555); photoreceptor cell maintenance (GO:0045494); regulation of rhodopsin mediated signaling pathway (GO:0022400). **Suggested CL terms:** retinal rod cell (CL:0000604), retinal cone cell (CL:0000573), retinal pigment epithelial cell (CL:0002586). **Suggested CHEBI:** cGMP (CHEBI:16356).

### 7. Anatomical Structures Affected

- **Organ:** Eye (UBERON:0000970); retina (UBERON:0000966). **Body system:** Visual/nervous (sensory). **Secondary:** optic nerve/disc (pallor), retinal vasculature (attenuation), macula (cystoid edema).
- **Tissue/cell:** Neural retina; primary target **rod photoreceptors** (CL:0000604), secondary **cone photoreceptors** (CL:0000573); downstream RPE (CL:0002586) and inner retinal neurons (remodeling).
- **Subcellular:** Rod **outer segment** (GO:0001750, photoreceptor outer segment), where PDE6 operates; photoreceptor connecting cilium/disc membranes.
- **Localization:** Bilateral, roughly symmetric; pigmentary changes predominate in the **midperiphery** with later macular involvement (macula lutea UBERON:0001782 / fovea UBERON:0000401).

### 8. Temporal Development

**Onset:** Childhood (HP:0011463), early-onset severe disease. **Onset pattern:** Insidious/chronic-progressive. **Progression:** Progressive rod-then-cone degeneration; rapid in the mouse model (most rods lost by P16, [PMID: 37363133]), with early severe/extinguished ERG in humans. **Course:** Chronic, lifelong, progressive; no spontaneous remission. **Critical period / therapeutic window:** Model data define a window in which gene supplementation can halt degeneration while sufficient photoreceptors remain (rescue effective with <13% rods remaining at 16 weeks but not at 24 weeks in the Pde6b model; [PMID: 35195763]) — implying earlier intervention is essential.

### 9. Inheritance and Population

**Inheritance:** Autosomal recessive (HP:0000007). **Penetrance:** Presumed complete in biallelic LoF homozygotes/compound heterozygotes (consistent across the founding family). **Expressivity:** Severe; limited data preclude firm expressivity statements. **Anticipation:** Not applicable (not a repeat-expansion disorder). **Carrier frequency:** ~1 in 6,600 (gnomAD-derived; Finding 7). **Affected frequency (random mating):** ~1 in 170 million (q²), so observed cases cluster in consanguineous families. **Founder effect:** The c.187+1G>T allele was described in a single extended consanguineous Muslim Arab-Israeli kindred ([PMID: 20655036]); no broad founder population is established. **Consanguinity:** Central to disease occurrence. **Epidemiology:** Ultra-rare; no prevalence/incidence estimates exist specifically for RP57; it is one of the rarest contributors to RP (overall RP ~1/4000; >90 genes). **Sex ratio:** Expected ~1:1 (autosomal). **Geographic distribution:** No endemic distribution established beyond the index family.

### 10. Diagnostics

**Clinical/functional tests:** Full-field **electroretinography (ERG)** is the key functional test — scotopic and photopic responses are severely reduced or extinguished. **OCT** documents macular structure and cystoid macular edema. **Fundus examination / autofluorescence** shows bone-spicule pigmentation, vascular attenuation, optic disc pallor. **Visual field testing (perimetry)** quantifies peripheral constriction. **Biomarkers:** No specific biochemical/circulating biomarker; the diagnosis is genetic. **Genetic testing (definitive):** Because RP is genetically heterogeneous (>90 genes), **next-generation sequencing gene panels** for inherited retinal dystrophies or **whole-exome/whole-genome sequencing** are the recommended first-line approach; PDE6G is included on comprehensive IRD panels. Homozygosity mapping is valuable in consanguineous pedigrees (the discovery method; [PMID: 20655036]). **Chromosomal microarray** can detect the 17q25.3 CNVs catalogued in ClinVar. **Differential diagnosis:** Other PDE6-related RP (PDE6A, PDE6B), congenital stationary night blindness (PDE6B H258N), other autosomal-recessive RP genes, syndromic RP (Usher, Bardet-Biedl) — distinguished by extra-ocular features and molecular testing. **Screening:** Cascade carrier testing in affected families and carrier screening in consanguineous couples; no population newborn screening exists.

### 11. Outcome / Prognosis

**Survival/mortality:** RP57 is non-lethal; it does not reduce life expectancy. **Morbidity:** Significant, progressive visual disability — the dominant outcome is severe, eventually profound, bilateral vision loss with functional blindness in advanced stages. **Disease course:** Progressive and lifelong; complications include cystoid macular edema (threatens central acuity) and the mobility/independence impacts of field loss. **Recovery:** No spontaneous recovery; vision loss is irreversible without intervention. **Prognostic factors:** Residual photoreceptor count and age at any future therapeutic intervention are the key determinants (therapeutic-window data from PDE6 models; [PMID: 35195763]). **Prognostic biomarkers:** None validated beyond structural (OCT ellipsoid zone/outer nuclear layer) and functional (ERG) measures used generally in RP.

### 12. Treatment

**Current standard:** No approved disease-modifying therapy. Management is **supportive**: low-vision rehabilitation and visual aids, orientation and mobility training, treatment of cystoid macular edema (e.g., carbonic anhydrase inhibitors, used generally in RP-CME), and genetic counseling. Vitamin A supplementation is debated in RP generally and not specifically validated for RP57.

**Experimental / leading candidate — gene therapy:** AAV-mediated **gene supplementation** is the most promising approach. In the related Pde6b model, wild-type gene restoration produced durable (≥1 year) rescue even after degeneration onset ([PMID: 29721933]), with a defined window of efficacy ([PMID: 35195763]); the Pde6g mouse provides a model to test PDE6G supplementation ([PMID: 37363133]). Emerging modalities broadly under investigation for RP include gene therapy, stem cells, optogenetics, retinal prosthetics, and pharmacotherapy ([PMID: 40575766]).

**Pharmacogenomic caution:** PDE5/PDE6-cross-reactive inhibitors (e.g., sildenafil) selectively impair retinal function in PDE6-γ-deficient animals ([PMID: 11157892]) and should be used cautiously in PDE6G patients/carriers.

**Suggested NCIT terms:** Gene Therapy (NCIT:C15431); Supportive Care (NCIT:C15277); Rehabilitation Therapy (NCIT:C15917).

### 13. Prevention

- **Primary prevention:** Not applicable (genetic). The principal lever is **genetic counseling** for consanguineous families and at-risk carriers.
- **Genetic screening:** Cascade carrier testing in families with a proband; carrier screening for consanguineous couples; **preimplantation genetic testing (PGT)** and **prenatal diagnosis** are options once the familial variant is known.
- **Secondary prevention:** Early molecular diagnosis to enable timely intervention within the therapeutic window and early management of cystoid macular edema.
- **Tertiary prevention:** Low-vision rehabilitation and complication management.
- **Pharmacologic avoidance:** Caution with PDE6-cross-reactive inhibitors (Finding 6).

### 14. Other Species / Natural Disease

**Taxonomy / orthologs:** PDE6G is conserved across vertebrates; mouse ortholog *Pde6g* (NCBI Gene 18587). **Model-organism disease:** Engineered *Pde6g*-deficient mice recapitulate early-onset rapid rod degeneration ([PMID: 37363133]). **Natural animal disease:** Naturally occurring PDE6-related retinal degenerations are well documented in dogs for the catalytic subunits — e.g., *PDE6B*-null **rcd1** and *PDE6A*-related forms — which model the human catalytic-subunit RP forms; a naturally occurring canine *PDE6G* retinopathy is not specifically established in the reviewed literature. **Comparative biology:** The rod phototransduction cascade and PDE6 holoenzyme architecture are evolutionarily conserved, so mechanisms translate across mammals. Of note, cross-species isoform differences exist (e.g., rod PDE6G can functionally substitute in cones in mouse; [PMID: 25739440]), a caveat for extrapolation. **Zoonotic potential:** None (non-infectious, genetic).

### 15. Model Organisms

| Model | Type | Key features | Reference |
|---|---|---|---|
| *Pde6g*-deficient mouse (preclinical RP model) | Mammalian, genetic null | Early-onset, rapid rod degeneration (most rods gone by P16); inner-retinal, RPE, and vascular remodeling incl. acellular capillaries | [PMID: 37363133](https://pubmed.ncbi.nlm.nih.gov/37363133/) |
| PDE6γ ILE86TER transgenic (on Pde6g-null background) | Mammalian, knock-in/transgenic | Decreased photoresponse decay, increased spontaneous dark PDE6 activity, reduced PDE6 expression — defines Pγ inhibitory/stabilizing role | [PMID: 21920434](https://pubmed.ncbi.nlm.nih.gov/21920434/) |
| PDEG tm1/+ (Pde6g-null heterozygote) | Mammalian | Sildenafil-induced reversible ERG suppression (gene–drug interaction) | [PMID: 11157892](https://pubmed.ncbi.nlm.nih.gov/11157892/) |
| *Pde6b* RP mouse (related subunit) | Mammalian | Gene-supplementation rescue durable ≥1 yr; defined therapeutic window | [PMID: 29721933](https://pubmed.ncbi.nlm.nih.gov/29721933/), [PMID: 35195763](https://pubmed.ncbi.nlm.nih.gov/35195763/) |

**Phenotype recapitulation:** The *Pde6g* mouse strongly recapitulates the human severe, early-onset rod–cone degeneration. **Limitations:** Mouse retinas are rod-dominant and lack a macula/fovea, so cystoid macular edema and foveal phenotypes are not modeled; cross-species PDE6 isoform substitution ([PMID: 25739440]) can also modify phenotype. **Applications:** Mechanistic dissection of Pγ loss and preclinical testing of AAV gene supplementation and therapeutic-window timing. **Resources:** MGI, IMPC/IMSR for *Pde6g* alleles.

---

## Mechanistic Model / Interpretation

```
  PDE6G biallelic LoF variant (e.g., c.187+1G>T essential splice)   [Finding 1, 8]
                         │  leads to
                         ▼
     Absent / non-functional rod Pγ inhibitory subunit
                         │  results in
                         ▼
  Loss of inhibitory control of PDE6 catalytic dimer (A/B)
  + reduced PDE6 holoenzyme stability/expression                    [Finding 3]
                         │  leads to
                         ▼
   Dysregulated cGMP hydrolysis in rod outer segments
   (abnormal cGMP / CNG-channel gating; phototransduction failure)  [Finding 3]
                         │  results in
                         ▼
        Rod dysfunction (extinguished scotopic ERG)
                         │  leads to
                         ▼
        Rapid ROD photoreceptor death                               [Finding 2, 4]
                    │              │
       leads to     │              │ leads to (secondary, non-cell-autonomous)
                    ▼              ▼
   Inner-retinal / RPE /      CONE photoreceptor death
   vascular REMODELING        (extinguished photopic ERG)
   (bone spicules, vessel          │
    attenuation, disc pallor,      │ leads to
    cystoid macular edema)         ▼
                    └──────►  Progressive peripheral → central
                              VISION LOSS (clinical RP57)           [Finding 2, 9]
```

The disease is mechanistically clean: a single recessive loss-of-function lesion in a non-redundant, rod-specific regulatory subunit removes the brake on the central phototransduction effector enzyme, dysregulating the second messenger (cGMP) that photoreceptors depend on for survival. This places RP57 firmly among the **PDE6-related retinopathies** (alongside PDE6A, PDE6B, PDE6C/PDE6H forms), differing by which subunit is lost but converging on cGMP dysregulation and photoreceptor death. Because the defect is loss-of-function (not a toxic gain-of-function), **gene supplementation** is mechanistically rational — simply restoring Pγ should reconstitute holoenzyme regulation — and related-subunit models confirm durable rescue within a therapeutic window.

---

## Evidence Base

| PMID | Role | How it supports/challenges findings |
|---|---|---|
| [20655036](https://pubmed.ncbi.nlm.nih.gov/20655036/) | **Founding/defining** | Establishes PDE6G causality (c.187+1G>T), clinical phenotype, inheritance; sole source for all 10 HPO annotations. Supports F001, F002, F005, F007, F008, F009. |
| [34170501](https://pubmed.ncbi.nlm.nih.gov/34170501/) | Mechanism (review) | PDE6 as central phototransduction effector; links PDE6-gene mutations to untreated retinal disease. Supports F003. |
| [21920434](https://pubmed.ncbi.nlm.nih.gov/21920434/) | Mechanism (in vivo) | PDE6γ restrains dark PDE6 activity; loss dysregulates cGMP signaling and reduces expression. Supports F003. |
| [37363133](https://pubmed.ncbi.nlm.nih.gov/37363133/) | Model organism | Pde6g mouse recapitulates early-onset rapid rod loss + remodeling. Supports F004. |
| [29721933](https://pubmed.ncbi.nlm.nih.gov/29721933/) | Therapeutic (model) | Durable gene-supplementation rescue after onset in PDE6 RP. Supports F004. |
| [35195763](https://pubmed.ncbi.nlm.nih.gov/35195763/) | Therapeutic (model) | Defines therapeutic window (<13% rods rescuable at 16 wk, fails at 24 wk). Supports F004. |
| [40575766](https://pubmed.ncbi.nlm.nih.gov/40575766/) | Context (review) | RP heterogeneity (>90 genes), emerging therapies. Supports F005. |
| [11157892](https://pubmed.ncbi.nlm.nih.gov/11157892/) | Gene–drug interaction | Sildenafil selectively suppresses ERG in Pde6g-null heterozygotes. Supports F006. |
| [33860373](https://pubmed.ncbi.nlm.nih.gov/33860373/), [32898583](https://pubmed.ncbi.nlm.nih.gov/32898583/), [39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/) | Structural/mechanistic | PDE6 structure, Pγ regulation, allosteric activation — background for gene-supplementation and allosteric-activator strategies. |

---

## Limitations and Knowledge Gaps

1. **Single defining pedigree.** The disease phenotype rests almost entirely on one consanguineous family ([PMID: 20655036]); all 10 HPO annotations come from this single source, limiting confidence in frequency estimates, expressivity, and the full phenotypic range.
2. **No human natural-history or epidemiologic data** specific to RP57 (no prevalence/incidence, no longitudinal visual-decline rates, no QoL instruments).
3. **Human mechanistic data are extrapolated** from PDE6 biology and mouse/in-vitro models; the precise cGMP dynamics and cell-death pathway in human PDE6G-null retina are inferred, not directly measured.
4. **No PDE6G-specific therapeutic data.** Gene-therapy evidence derives from the related *Pde6b* model; a PDE6G gene-supplementation proof-of-concept in the Pde6g mouse is a gap.
5. **Carrier/affected frequency estimates are computational** (gnomAD-derived), subject to ascertainment and reference-population limits.
6. **Cross-species isoform caveats** (e.g., rod PDE6G substituting in mouse cones; [PMID: 25739440]) complicate translation of mouse phenotypes to human cone involvement.

## Proposed Follow-up Experiments / Actions

1. **Expand the genotype–phenotype series.** Aggregate additional PDE6G biallelic cases via IRD registries and matchmaking (GeneMatcher) to validate the HPO frequency set, establish expressivity, and detect modifiers.
2. **PDE6G-specific gene supplementation.** Test AAV-*PDE6G* (rod-targeted) in the Pde6g mouse to confirm rescue and map the human-relevant therapeutic window, mirroring the Pde6b paradigm ([PMID: 29721933], [PMID: 35195763]).
3. **Natural-history study.** Longitudinal OCT (ellipsoid zone/ONL), ERG, and perimetry in any identifiable patients to define progression rate and optimal intervention timing.
4. **cGMP-pathway pharmacology.** Evaluate PDE6 allosteric modulators and cGMP-lowering/CNG-modulating strategies ([PMID: 32898583], [PMID: 34170501]) as non-genetic adjuncts, and formally document the sildenafil/PDE6-inhibitor caution in clinical guidance.
5. **Variant curation.** Reclassify the Conflicting frameshift alleles (c.95del, c.206del) with functional splicing/expression assays to firm up the LoF allelic series.
6. **iPSC retinal organoids** from patient cells to model human PDE6G-null photoreceptor degeneration and test editing/supplementation in a human context.

---

*Evidence-source legend:* human clinical/genetic (founding family, registries), model organism (mouse Pde6g/Pde6b), in vitro/structural (PDE6 biochemistry/cryo-EM), computational (gnomAD, ClinVar curation).


## Artifacts

- [OpenScientist final report](PDE6G-related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PDE6G-related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 14 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007737` (2 mentions) - the report calls it "Spicular (bone-spicule) retinal pigmentation"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone corpuscle fundus pigmentation" among its other names
- `CL:0000604` (2 mentions) - the report calls it "rod photoreceptors"; CL calls it **retinal rod cell**, and lists "rod" among its other names
- `CL:0000573` (2 mentions) - the report calls it "cone photoreceptors"; CL calls it **retinal cone cell**, and lists "cone" among its other names
- `UBERON:0000970` (1 mention) - the report calls it "Organ:** Eye"; UBERON calls it **eye**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `OMIM`, `NCBIGene`.

31 of 35 terms resolved to a current term; the rest could not be looked up either way.