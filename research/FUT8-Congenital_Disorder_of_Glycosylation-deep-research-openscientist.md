---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T18:12:07.725828'
end_time: '2026-11-12T18:25:23.367515'
duration_seconds: 795.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: FUT8-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0020775
  category: Mendelian
  causal_genes: FUT8
  omim_id: OMIM:618005
  synonyms: not recorded
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
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 21
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 6
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0036065
    ontology_label: obsolete fucosylation
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: FUT8-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: FUT8-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FUT8-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0020775 (if available)
- **Causal gene(s):** FUT8
- **OMIM:** OMIM:618005
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **FUT8-Congenital Disorder of Glycosylation** covering all of the
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

# FUT8-Congenital Disorder of Glycosylation (FUT8-CDG): Comprehensive Disease Characterization Report

**MONDO:** MONDO:0020775 · **OMIM:** 618005 · **Causal gene:** **FUT8** (α-1,6-fucosyltransferase) · **Category:** Mendelian, autosomal recessive · **CDG classification:** Type II (CDG-IIj)

---

## Summary

**FUT8-Congenital Disorder of Glycosylation is an ultra-rare, autosomal-recessive, multisystem inborn error of metabolism caused by biallelic loss-of-function variants in the gene _FUT8_**, which encodes the Golgi-resident α-(1,6)-fucosyltransferase — the sole enzyme in humans that performs "core fucosylation," the attachment of a fucose residue to the innermost N-acetylglucosamine (GlcNAc) of N-linked glycoproteins. Despite the disease name referencing "glycosylation" generically, the specific molecular lesion is the abolition of core fucose, and the causal gene is unambiguously **FUT8** (HGNC:4019; NCBI Gene 2530; UniProt Q9BYC5; chromosome 14q23.3).

The disorder was first delineated in 2018 when biallelic pathogenic _FUT8_ variants were identified by whole-exome sequencing in three unrelated individuals ([PMID: 29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/)), and the clinical/molecular spectrum was expanded in 2020 to approximately seven reported patients ([PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/)). The phenotype is a severe congenital syndrome: intrauterine growth restriction, profound developmental and growth delay (often with shortened limbs), hypotonia, microcephaly, seizures, feeding difficulties, respiratory abnormalities, and shortened lifespan, with at least one reported case of childhood glaucoma ([PMID: 31580894](https://pubmed.ncbi.nlm.nih.gov/31580894/)).

Mechanistically, loss of core fucose impairs the signaling of multiple N-glycosylated growth-factor receptors (TGF-β1 receptor, EGFR, PDGFR, VEGFR-2) and neural cell-adhesion molecules (Contactin-2/NCAM), as established primarily in _Fut8_-null mouse models and confirmed by human glycomics. Diagnosis rests on demonstrating **complete loss of core fucosylation on serum N-glycans by mass spectrometry** plus biallelic _FUT8_ variants, because standard transferrin isoelectric-focusing screening can be normal (core fucose does not affect sialylation). There is no approved disease-modifying therapy; oral **L-fucose** has been trialed, and management is otherwise supportive.

---

## Key Findings

### Finding 1 — FUT8-CDG is caused by biallelic loss-of-function variants in _FUT8_, abolishing core fucosylation

Whole-exome sequencing of three unrelated affected individuals identified pathogenic _FUT8_ variants; the first (from a consanguineous family) was homozygous for **c.715C>T (p.Arg239\*)**, a nonsense variant producing a truncated, non-functional protein ([PMID: 29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/)). _FUT8_ encodes a Golgi-localized α-1,6-fucosyltransferase that is the only enzyme capable of transferring fucose to the innermost GlcNAc of N-linked glycoproteins.

> *"Fucosyltransferase 8 (FUT8) encodes a Golgi-localized α1,6 fucosyltransferase that is essential for transferring the monosaccharide fucose into N-linked glycoproteins, a process known as 'core fucosylation.'"* — [PMID: 29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/)

Because FUT8 is the sole core fucosyltransferase, biallelic loss of function produces a complete, rather than partial, deficiency of this glycan modification. **Evidence type:** human clinical + molecular.

**Ontology anchors:** gene FUT8 (HGNC:4019); GO:0036065 *fucosylation*; GO:0008424 *glycoprotein 6-α-L-fucosyltransferase activity*; disease MONDO:0020775.

### Finding 2 — Clinical phenotype: IUGR, severe growth/developmental delay, hypotonia, microcephaly, seizures, respiratory complications

The recurrent, defining clinical features were enumerated across the two primary clinical reports and a case report.

> *"The clinical characteristics of patients with FUT8-CDG include intrauterine growth retardation, feeding difficulties, hypotonia, microcephaly, seizures, short stature, developmental delay, and respiratory abnormalities."* — [PMID: 31580894](https://pubmed.ncbi.nlm.nih.gov/31580894/)

> *"...who presented with intrauterine growth retardation, severe developmental and growth delays with shortened limbs, neurological impairments, and respiratory complications."* — [PMID: 29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/)

The 2019 report also described the **first case of glaucoma** in FUT8-CDG, expanding the ophthalmologic spectrum ([PMID: 31580894](https://pubmed.ncbi.nlm.nih.gov/31580894/)). **Evidence type:** human clinical.

**Suggested HPO terms with qualitative frequency:**

| Phenotype | HPO term | Type | Onset | Frequency (reported cases) |
|---|---|---|---|---|
| Intrauterine growth retardation | HP:0001511 | Physical/prenatal | Prenatal/congenital | Very frequent |
| Global developmental delay | HP:0001263 | Clinical sign | Neonatal/infancy | Very frequent |
| Growth delay / short stature | HP:0001510 / HP:0004322 | Physical | Congenital | Very frequent |
| Muscular hypotonia | HP:0001252 | Clinical sign | Neonatal | Frequent |
| Microcephaly | HP:0000252 | Physical | Congenital | Frequent |
| Seizure | HP:0001250 | Clinical sign | Infancy | Frequent |
| Feeding difficulties | HP:0011968 | Symptom | Neonatal | Frequent |
| Respiratory abnormality | HP:0002086 | Clinical sign | Neonatal/infancy | Frequent |
| Shortened limbs | HP:0009826 | Physical | Congenital | Reported |
| Glaucoma | HP:0000501 | Clinical sign | Childhood | Rare (single case) |

**Quality-of-life impact:** Given the combination of profound developmental delay, seizures, feeding difficulty, and respiratory compromise, affected children have severe functional impairment and high dependency; no formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

### Finding 3 — Mechanism: loss of core fucose dysregulates TGF-β1, EGF, PDGF and VEGFR-2 growth-factor receptor signaling

The mechanistic link between core-fucose loss and disease phenotype is best established in **_Fut8_-null mice**, which display growth retardation and emphysema-like lung destruction.

> *"Fut8(-/-) mice have a marked dysregulation of TGF-beta1 receptor activation and signaling, as assessed by TGF-beta1 binding assays and Smad2 phosphorylation analysis."* — [PMID: 16236725](https://pubmed.ncbi.nlm.nih.gov/16236725/)

Dysregulated TGF-β1 receptor signaling drives MMP-12/MMP-13 overexpression and elastin (extracellular matrix) downregulation, producing emphysema; exogenous TGF-β1 rescues the phenotype. Core fucosylation is also required for EGF- and PDGF-receptor signaling:

> *"...core fucosylation is crucial for growth factor receptors such as TGF-beta1 and EGF receptor-mediated biological functions."* — [PMID: 17132494](https://pubmed.ncbi.nlm.nih.gov/17132494/)

A parallel mechanism involves VEGFR-2:

> *"...vascular endothelial growth factor receptor-2 (VEGFR-2) expression was significantly suppressed in Fut8(-/-) mice."* — [PMID: 19179362](https://pubmed.ncbi.nlm.nih.gov/19179362/)

VEGFR-2 suppression raises ceramide and drives alveolar apoptosis, contributing to the emphysematous lung phenotype. An additional growth-retardation mechanism operates through the **EGFR–trypsin–PAR-2 axis**: _Fut8_ loss down-regulates trypsinogens and attenuates proteinase-activated receptor-2 signaling, with EGF-induced receptor phosphorylation blunted ([PMID: 16861703](https://pubmed.ncbi.nlm.nih.gov/16861703/)). **Evidence type:** model organism + in vitro.

**Ontology anchors:** GO:0007179 *TGF-β receptor signaling pathway*; GO:0007173 *EGFR signaling pathway*; GO:0048010 *VEGFR signaling pathway*; CHEBI:28351 *fucose*; CHEBI:17761 *ceramide*.

### Finding 4 — _Fut8_-null mouse model: ~70% neonatal lethality, growth retardation, emphysema, neurobehavioral abnormalities

The knockout mouse is the principal disease model and recapitulates the severity of the human phenotype.

> *"70% of Fut8-deficient (Fut8(-/-)) mice that lack core fucose structure die within 3 days after birth, but the remainder survive for up to several weeks although they show growth retardation as well as emphysema."* — [PMID: 24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/)

Surviving mice partially compensate by up-regulating bisecting GlcNAc (via GnT-III/_Mgat3_) through Wnt/β-catenin signaling — an adaptive glycan response ([PMID: 24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/)). The model also shows neurobehavioral pathology:

> *"Fut8(-/-) mice exhibit multiple behavioral abnormalities consistent with a schizophrenia-like phenotype."* — [PMID: 21471224](https://pubmed.ncbi.nlm.nih.gov/21471224/)

These include hyperlocomotion, working-memory and prepulse-inhibition (PPI) deficits, and decreased striatal serotonin metabolites; even heterozygous _Fut8(+/-)_ mice showed stress-induced PPI deficits, suggesting dosage sensitivity ([PMID: 21471224](https://pubmed.ncbi.nlm.nih.gov/21471224/)). **Evidence type:** model organism. (Note: the exact behavioral-phenotype quote above should be re-verified against the stored abstract before database ingestion — it was flagged as a snippet mismatch in the knowledge state, though the finding itself is well supported.)

### Finding 5 — Diagnostic biomarker: complete loss of core (α-1,6) fucosylation on serum N-glycans

Serum N-glycan analysis provides the direct, disease-specific biomarker.

> *"Analysis of serum N-glycans revealed a complete lack of core fucosylation, an important diagnostic biomarker of FUT8-CDG."* — [PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/)

A comprehensive LC-MS N-glycan profiling platform for CDG type II independently confirmed the signature:

> *"...reduced fucosylation was observed in patients with FUT8-CDG and SLC35C1-CDG."* — [PMID: 42511652](https://pubmed.ncbi.nlm.nih.gov/42511652/)

Because FUT8-CDG is a CDG type II (Golgi-processing) disorder and core fucose is not required for sialylation, **serum transferrin isoelectric focusing may be normal** — making glycomics/mass spectrometry the reliable test. **Evidence type:** human clinical.

### Finding 6 — Treatment: oral L-fucose supplementation is the principal disease-specific therapy attempted

> *"FUT8-CDG is a severe multisystem disorder caused by mutations in..."* — *L-Fucose treatment of FUT8-CDG*, [PMID: 33312876](https://pubmed.ncbi.nlm.nih.gov/33312876/)

Oral L-fucose has been trialed as a targeted approach, with the rationale of boosting the GDP-fucose salvage pathway to drive any residual FUT8 activity ([PMID: 33312876](https://pubmed.ncbi.nlm.nih.gov/33312876/)). Fucose therapy across fucosylation-defect CDGs has been reviewed ([PMID: 34389986](https://pubmed.ncbi.nlm.nih.gov/34389986/)). However, no approved disease-modifying therapy exists for any CDG:

> *"...no FDA/EMA-approved disease-modifying therapy is currently available for any CDG, and most interventions remain off-label, experimental, or supported by limited observational evidence."* — [PMID: 42813231](https://pubmed.ncbi.nlm.nih.gov/42813231/)

Management is otherwise supportive: nutritional/feeding support, anti-seizure medication, respiratory care, and developmental therapies. **Evidence type:** human clinical + review.

**Suggested NCIT terms:** fucose (dietary monosaccharide therapy); supportive-care interventions (nutritional support, anticonvulsant therapy, respiratory support).

### Finding 7 — Epidemiology: ultra-rare (~7 reported patients by 2020); autosomal recessive with consanguinity/homozygosity

> *"...we report an additional four unrelated affected individuals homozygous for novel pathogenic variants in FUT8."* — [PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/)

Combined with the original three cases, this brings the total to approximately seven reported patients. All reported individuals are homozygous, several from consanguineous families — the pattern expected for a rare autosomal-recessive disorder. FUT8-CDG belongs to a small group of fucosylation CDGs:

> *"Only five types of congenital disorders of glycosylation (CDG) related to an impaired fucosylation have been described to date: FUT8-CDG, FCSK-CDG, POFUT1-CDG SLC35C1-CDG, and the only recently described GFUS-CDG."* — [PMID: 34389986](https://pubmed.ncbi.nlm.nih.gov/34389986/)

Across all fucosylation CDGs combined there are only ~25 reported patients. **Evidence type:** human clinical + review.

### Finding 8 — Neurodevelopmental mechanism: FUT8 core-fucosylation sustains cerebellar granule neuron development via Cntn2/NCAM

A 2025 study provided a specific mechanistic link for the neurodevelopmental phenotype. FUT8 and core fucosylation are abundant in the cerebellum, and cerebellar granule-neuron-progenitor (GNP)-specific _Fut8_ deletion impairs GNP proliferation/differentiation, neuronal development, synaptic physiology, and motor coordination.

> *"Fut8 deficiency reduced Contactin 2 (Cntn2) expression, a member of neural cell adhesion molecules (NCAMs). Furthermore, ectopic Cntn2 can rescue the neuronal defects induced by Fut8 deficiency."* — [PMID: 39604780](https://pubmed.ncbi.nlm.nih.gov/39604780/)

This establishes Cntn2/NCAM as a key downstream effector linking core-fucose loss to cerebellar/neurodevelopmental pathology, complementing the earlier schizophrenia-like behavioral findings ([PMID: 21471224](https://pubmed.ncbi.nlm.nih.gov/21471224/)). **Evidence type:** model organism.

**Ontology anchors:** CL:0000120 *granule cell*; UBERON:0002037 *cerebellum*; GO:0007156 *homophilic cell adhesion via plasma membrane adhesion molecules*; GO:0022008 *neurogenesis*.

### Finding 9 — FUT8 protein architecture and the GT-B catalytic mechanism disrupted by pathogenic variants

The human FUT8 crystal structure was solved at 2.6 Å resolution.

> *"The overall structure of FUT8 was found to consist of three domains: an N-terminal coiled-coil domain, a catalytic domain, and a C-terminal SH3 domain."* — [PMID: 17172260](https://pubmed.ncbi.nlm.nih.gov/17172260/)

The catalytic domain adopts a **GT-B-type glycosyltransferase fold** (not GT-A) containing a Rossmann fold that forms the GDP-β-L-fucose donor-binding site; FUT8 transfers fucose from GDP-fucose to the reducing-terminal GlcNAc of N-linked glycans. Structural studies further detailed substrate recognition and catalysis ([PMID: 32220931](https://pubmed.ncbi.nlm.nih.gov/32220931/)). The same work connected FUT8 loss of function to growth-factor-receptor pathology:

> *"FUT8 null mice showed severe growth retardation and emphysema-like lung-destruction as a result of the dysfunction of epidermal growth factor and transforming growth factor-beta receptors."* — [PMID: 17172260](https://pubmed.ncbi.nlm.nih.gov/17172260/)

Reported pathogenic variants are biallelic and include nonsense (e.g., c.715C>T, p.Arg239\*) and missense changes that cause loss of enzymatic function ([PMID: 29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/); [PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/)). **Gene coordinates:** FUT8, chromosome 14q23.3; HGNC:4019; NCBI Gene 2530; UniProt Q9BYC5. **Evidence type:** computational/structural + human molecular.

### Finding 10 — Diagnostic pitfall: transferrin screening can be normal; differential centers on other fucosylation CDGs

Because core (α-1,6) fucose loss does not alter transferrin sialylation, first-line transferrin isoelectric focusing can be non-diagnostic; confirmation requires serum N-glycan mass spectrometry showing absent core fucosylation plus biallelic _FUT8_ variants ([PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/); [PMID: 42511652](https://pubmed.ncbi.nlm.nih.gov/42511652/)). The differential diagnosis is the other fucosylation CDGs:

> *"Only five types of congenital disorders of glycosylation (CDG) related to an impaired fucosylation have been described to date: FUT8-CDG, FCSK-CDG, POFUT1-CDG SLC35C1-CDG, and the only recently described GFUS-CDG."* — [PMID: 34389986](https://pubmed.ncbi.nlm.nih.gov/34389986/)

Notably, **SLC35C1-CDG** (leukocyte adhesion deficiency II / CDG-IIc; a GDP-fucose transporter defect) is distinguished clinically by leukocyte-adhesion immunodeficiency and recurrent infection. In LAD II fibroblasts, reduced Golgi GDP-fucose preferentially lowers core fucosylation:

> *"...core fucosylation was affected to a greater extent compared with other types of fucosylation of N-linked oligosaccharides."* — [PMID: 15917429](https://pubmed.ncbi.nlm.nih.gov/15917429/)

This glycomic overlap underscores the need for genetic confirmation to distinguish FUT8-CDG from the transporter disorder. **Evidence type:** human clinical + in vitro.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in _FUT8_** (nonsense e.g. p.Arg239\*, or missense disrupting the GT-B catalytic domain) **lead to** absence of functional Golgi α-1,6-fucosyltransferase. *(Demonstrated — WES + structural data.)*
2. Loss of FUT8 activity **results in** complete failure of **core fucosylation** — no fucose is added to the innermost GlcNAc of N-linked glycans across all glycoproteins. *(Demonstrated — serum N-glycan MS.)*
3. Absence of core fucose **alters the function of multiple N-glycosylated receptors and adhesion molecules**. The chain then branches:
   - **Branch A (growth):** impaired TGF-β1R, EGFR, PDGFR signaling + EGFR–trypsin–PAR-2 axis suppression **leads to** growth-factor-receptor dysfunction → **intrauterine growth restriction, severe growth/developmental delay, shortened limbs**. *(Demonstrated in mouse/in vitro; inferred for human.)*
   - **Branch B (lung/vascular):** TGF-β1R dysregulation → MMP-12/MMP-13 up, elastin down; plus VEGFR-2 suppression → ceramide-driven alveolar apoptosis **results in** emphysema-like lung injury → **respiratory abnormalities**. *(Demonstrated in mouse; inferred for human.)*
   - **Branch C (neurodevelopment):** reduced Contactin-2 (Cntn2/NCAM) in cerebellar granule-neuron progenitors **leads to** impaired GNP proliferation/differentiation, synaptic dysfunction, and altered monoamine systems → **microcephaly, seizures, developmental delay, neurobehavioral abnormality**. *(Demonstrated in mouse; inferred for human.)*
4. The convergent multisystem failure **produces** the severe congenital phenotype with high early mortality (mouse ~70% neonatal lethality; shortened human lifespan). *(Demonstrated in mouse; consistent with human severity.)*

```
 FUT8 biallelic LoF
        │
        ▼
 No core α1,6-fucose on N-glycans (global)
        │
        ├──────────────┬────────────────────┐
        ▼              ▼                     ▼
  TGF-βR/EGFR/      VEGFR-2 ↓           Cntn2 (NCAM) ↓
  PDGFR signaling   → ceramide↑         in cerebellar GNPs
   dysfunction      → alveolar          → impaired neuro-
   + EGFR-trypsin-   apoptosis           genesis/synapses
   PAR-2 axis ↓          │                     │
        │          MMP-12/13↑,                 │
        ▼          elastin↓                    ▼
   Growth failure,      │              Microcephaly, seizures,
   IUGR, limb           ▼              dev. delay, behavior
   shortening       Emphysema /
                    respiratory
                    disease
        └──────────────┴─────────────────────┘
                        ▼
         Severe congenital multisystem disease
            (high mortality / short lifespan)
```

### Upstream vs downstream

- **Upstream (primary lesion):** _FUT8_ mutation → absent core fucosylation (a single, global biochemical defect).
- **Downstream (effectors):** receptor-specific signaling failures (TGF-β1R, EGFR, PDGFR, VEGFR-2) and adhesion-molecule deficits (Cntn2/NCAM) are the proximate causes of organ-level pathology. The disease is thus a "single upstream defect, many downstream effectors" model — explaining its pleiotropic, multisystem presentation.

### Anatomical structures affected

| Level | Structure | Ontology term |
|---|---|---|
| Organ | Brain (cerebellum), lungs, eyes, skeleton, GI/pancreas | UBERON:0002037 (cerebellum); UBERON:0002048 (lung); UBERON:0000970 (eye) |
| Body system | Nervous, respiratory, musculoskeletal, digestive | — |
| Cell | Cerebellar granule neurons/progenitors; alveolar epithelial cells; pancreatic acinar cells | CL:0000120 (granule cell); CL:0000066 (epithelial cell) |
| Subcellular | Golgi apparatus (site of FUT8 action); secreted/membrane glycoproteins | GO:0005795 (Golgi stack); GO:0005796 (Golgi lumen) |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [29304374](https://pubmed.ncbi.nlm.nih.gov/29304374/) | *Biallelic mutations in FUT8 cause a CDG with defective fucosylation* | Human clinical/molecular | F001, F002, F009 — founding disease description; variant p.Arg239\* |
| [32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/) | *Expanding the molecular and clinical phenotypes of FUT8-CDG* | Human clinical/molecular | F005, F007, F010 — biomarker, case count, AR pattern |
| [31580894](https://pubmed.ncbi.nlm.nih.gov/31580894/) | *Childhood glaucoma in FUT8-CDG* | Human clinical | F002 — phenotype list; first glaucoma case |
| [16236725](https://pubmed.ncbi.nlm.nih.gov/16236725/) | *Dysregulation of TGF-β1 receptor... emphysema in core-fucose-deficient mice* | Model organism | F003 — TGF-β1R mechanism |
| [17132494](https://pubmed.ncbi.nlm.nih.gov/17132494/) | *Phenotype changes of Fut8 KO mouse* | Model organism | F003 — EGFR/growth-factor mechanism |
| [19179362](https://pubmed.ncbi.nlm.nih.gov/19179362/) | *Requirement of Fut8 for VEGFR-2 expression* | Model organism | F003 — VEGFR-2/ceramide mechanism |
| [16861703](https://pubmed.ncbi.nlm.nih.gov/16861703/) | *Trypsinogen down-regulation / PAR-2 in Fut8-null mice* | Model organism/in vitro | F003 — EGFR–trypsin–PAR-2 growth axis |
| [24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/) | *Absence of core fucose up-regulates GnT-III and Wnt targets* | Model organism | F004 — lethality, growth, compensatory GnT-III |
| [21471224](https://pubmed.ncbi.nlm.nih.gov/21471224/) | *Fut8-deficient mice: schizophrenia-like phenotype* | Model organism | F004, F008 — neurobehavioral phenotype |
| [39604780](https://pubmed.ncbi.nlm.nih.gov/39604780/) | *FUT8 regulates cerebellar neurogenesis via Cntn2* | Model organism | F008 — Cntn2/NCAM neurodevelopmental mechanism |
| [17172260](https://pubmed.ncbi.nlm.nih.gov/17172260/) | *Crystal structure of mammalian FUT8* | Structural/computational | F009 — three-domain GT-B architecture |
| [32220931](https://pubmed.ncbi.nlm.nih.gov/32220931/) | *Structural basis of substrate recognition and catalysis by FUT8* | Structural | F009 — catalytic mechanism detail |
| [33312876](https://pubmed.ncbi.nlm.nih.gov/33312876/) | *L-Fucose treatment of FUT8-CDG* | Human clinical | F006 — fucose therapy trial |
| [34389986](https://pubmed.ncbi.nlm.nih.gov/34389986/) | *CDG with defective fucosylation* (review) | Review | F006, F007, F010 — fucosylation-CDG differential |
| [42813231](https://pubmed.ncbi.nlm.nih.gov/42813231/) | *CDG: State of the Art in 2026* (review) | Review | F006 — no approved therapy |
| [42511652](https://pubmed.ncbi.nlm.nih.gov/42511652/) | *Diagnosis of CDG type II by comprehensive N-glycan MS profiling* | Human clinical/methods | F005, F010 — MS diagnostic confirmation |
| [15917429](https://pubmed.ncbi.nlm.nih.gov/15917429/) | *Core fucosylation in LAD II/CDG-IIc fibroblasts* | In vitro | F010 — differential (SLC35C1) glycomic overlap |

### Broader FUT8 biology context (supportive, not disease-specific)

Several recent papers underscore how central core fucosylation is across physiology — reinforcing why its complete loss is so damaging: FUT8-mediated fucosylation modulates IgG effector function (afucosylated IgG enhances ADCC; [PMID: 35844552](https://pubmed.ncbi.nlm.nih.gov/35844552/)), platelet activation and thrombosis ([PMID: 42237907](https://pubmed.ncbi.nlm.nih.gov/42237907/)), coronavirus receptor (APN) entry ([PMID: 42149951](https://pubmed.ncbi.nlm.nih.gov/42149951/)), and neuroinflammation via TGF-βR/VEGFR/EGFR/integrins/gp130 ([PMID: 41917387](https://pubmed.ncbi.nlm.nih.gov/41917387/)). FUT8 is also a recurrent oncology target (ovarian, glioblastoma, prostate cancers), where overexpression drives progression — the mirror image of the loss-of-function disease ([PMID: 41786877](https://pubmed.ncbi.nlm.nih.gov/41786877/); [PMID: 41592739](https://pubmed.ncbi.nlm.nih.gov/41592739/); [PMID: 42832539](https://pubmed.ncbi.nlm.nih.gov/42832539/)).

---

## Section-by-Section Synthesis

### 1. Disease Information
FUT8-CDG (CDG type IIj) is an autosomal-recessive multisystem congenital disorder of glycosylation caused by deficiency of core fucosylation. **Identifiers:** MONDO:0020775; OMIM:618005; causal gene FUT8 (HGNC:4019). Orphanet and ICD-11 entries fall under the broader CDG category (ICD-11 5C53.0, "Disorders of glycoprotein metabolism"; ICD-10 E77.8). Information is derived from **aggregated disease-level resources and individual case reports** (~7 patients), not from large EHR cohorts. Synonyms: "FUT8-CDG," "CDG-IIj," "congenital disorder of glycosylation type IIj," "alpha-(1,6)-fucosyltransferase deficiency."

### 2. Etiology
**Causal factor:** purely genetic — biallelic loss-of-function _FUT8_ variants. No environmental, infectious, or acquired triggers are implicated. **Genetic risk factors:** consanguinity (homozygosity for private variants). **Protective/modifier factors:** not established in humans; in mice, compensatory up-regulation of bisecting GlcNAc (GnT-III/Wnt) partially offsets core-fucose loss ([PMID: 24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/)), a candidate modifier pathway. **Gene–environment interactions:** none documented.

### 3. Phenotypes
See Finding 2 table. Onset is **congenital/neonatal**; severity is **severe**; course is **chronic** from birth with early mortality risk. Quality-of-life impact is profound owing to combined neurologic, respiratory, and feeding impairment.

### 4. Genetic/Molecular Information
**Causal gene:** FUT8 (14q23.3). **Variant types:** nonsense (c.715C>T, p.Arg239\*) and missense; all reported are biallelic/homozygous with **loss-of-function** consequence. **Classification:** pathogenic (ACMG) based on segregation, functional glycan loss, and enzyme biology. **Allele frequency:** pathogenic alleles are private/ultra-rare in gnomAD. **Origin:** germline. **Modifier genes/epigenetics/chromosomal abnormalities:** none established in humans.

### 5. Environmental Information
Not applicable — a monogenic inborn error with no environmental, lifestyle, or infectious contribution.

### 6. Mechanism/Pathophysiology
See the ordered causal chain and diagram above (Findings 3, 4, 8, 9).

### 7. Anatomical Structures Affected
See anatomy table above — primary involvement of brain (cerebellum), lungs, eyes, skeleton; Golgi apparatus is the subcellular site of the defect.

### 8. Temporal Development
**Onset:** congenital/prenatal (IUGR). **Pattern:** chronic, non-episodic, present from birth. **Progression:** severe and early; mouse model shows ~70% death within 3 days of birth, implying a critical perinatal window. Human lifespan is shortened. No remission occurs.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** complete in biallelic carriers. **Expressivity:** severe, with some phenotypic range (e.g., glaucoma in one case). **Epidemiology:** ultra-rare (~7 reported patients; part of ~25 total fucosylation-CDG patients). Consanguinity and founder/private homozygous variants predominate. No sex predilection expected (autosomal). **Carrier frequency:** not established but presumed very low.

### 10. Diagnostics
**First-line pitfall:** transferrin isoelectric focusing may be normal (Finding 10). **Definitive:** serum N-glycan mass spectrometry showing absent core fucosylation ([PMID: 32049367](https://pubmed.ncbi.nlm.nih.gov/32049367/); [PMID: 42511652](https://pubmed.ncbi.nlm.nih.gov/42511652/)) **plus** molecular confirmation by WES/WGS or targeted _FUT8_ sequencing / CDG gene panels. **Differential:** other fucosylation CDGs (SLC35C1/LAD II — distinguished by immunodeficiency and recurrent infection; FCSK, POFUT1, GFUS).

### 11. Outcome/Prognosis
Severe prognosis: profound neurodevelopmental disability, respiratory compromise, feeding failure, and shortened lifespan. No formal survival statistics exist given ultra-rarity. Prognostic factors are inferred to include severity of respiratory and seizure involvement.

### 12. Treatment
No approved disease-modifying therapy ([PMID: 42813231](https://pubmed.ncbi.nlm.nih.gov/42813231/)). **Disease-specific trial:** oral **L-fucose** (salvage-pathway rationale; [PMID: 33312876](https://pubmed.ncbi.nlm.nih.gov/33312876/)). **Supportive:** nutritional/feeding support, anticonvulsants, respiratory care, developmental/physical/occupational/speech therapy, ophthalmologic management (glaucoma). **Experimental/future:** gene/enzyme replacement and substrate therapy remain conceptual.

### 13. Prevention
**Primary:** genetic counseling for consanguineous/at-risk families; carrier testing and prenatal/preimplantation genetic diagnosis once a familial variant is known. **Secondary/tertiary:** early supportive intervention to prevent complications. No population screening exists.

### 14. Other Species / Natural Disease
No naturally occurring FUT8-CDG is reported in companion animals or wildlife (OMIA). The orthologous mouse gene _Fut8_ (NCBI Gene 53618) is highly conserved, and the knockout recapitulates key features — evidence of strong evolutionary conservation of the core-fucosylation mechanism. No zoonotic relevance.

### 15. Model Organisms
The **_Fut8_-knockout mouse** (MGI) is the principal model: ~70% neonatal lethality, growth retardation, emphysema, and schizophrenia-like neurobehavior ([PMID: 24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/); [PMID: 21471224](https://pubmed.ncbi.nlm.nih.gov/21471224/)). **Conditional (cerebellar GNP-specific) _Fut8_ deletion** models the neurodevelopmental mechanism via Cntn2 ([PMID: 39604780](https://pubmed.ncbi.nlm.nih.gov/39604780/)). In vitro, _Fut8_-knockdown pancreatic acinar carcinoma cells model the growth/EGFR–PAR-2 defect ([PMID: 16861703](https://pubmed.ncbi.nlm.nih.gov/16861703/)). **Recapitulation:** strong for growth failure, respiratory, and neurobehavioral domains; **limitations:** mouse perinatal lethality and species differences in glycan compensation limit modeling of the full human survival/clinical course.

---

## Limitations and Knowledge Gaps

1. **Extremely small human cohort (~7 patients).** All epidemiology, penetrance, expressivity, and natural-history statements are low-confidence and based on case reports; no registry or longitudinal data exist.
2. **Human mechanism is largely inferred from mouse.** The TGF-β1R/EGFR/PDGFR/VEGFR-2 and Cntn2 mechanisms are demonstrated in _Fut8_-null or conditional mice and in vitro, not directly in patient tissue. Human-specific validation is lacking.
3. **Treatment efficacy unproven.** L-fucose has been trialed, but no controlled outcome data establish benefit; there is no approved therapy.
4. **No formal QoL, survival, or prognostic-biomarker data** owing to rarity.
5. **Diagnostic under-ascertainment risk** because transferrin screening can be normal — true prevalence may be underestimated.
6. **One citation (PMID 21471224) was flagged as a snippet "mismatch"** in the knowledge state; the schizophrenia-like phenotype is well-supported by the paper's title and corroborating sources, but the exact quote should be re-verified against the abstract before database ingestion.

## Proposed Follow-up Experiments / Actions

1. **Establish an international FUT8-CDG patient registry** to aggregate phenotype, variant, natural-history, and treatment-response data beyond the current ~7 cases.
2. **Human-tissue mechanistic validation:** assess TGF-β1R/EGFR/VEGFR-2 signaling and Cntn2 levels in patient-derived fibroblasts or iPSC-derived neurons/organoids to confirm the mouse-derived causal chain.
3. **Systematic L-fucose trial** with glycomic (serum core-fucose) and clinical endpoints; test whether salvage-pathway loading restores any fucosylation given the typical complete loss-of-function genotype.
4. **Patient-specific genotype–function mapping:** express reported missense variants against the solved GT-B structure ([PMID: 17172260](https://pubmed.ncbi.nlm.nih.gov/17172260/); [PMID: 32220931](https://pubmed.ncbi.nlm.nih.gov/32220931/)) to quantify residual activity and genotype–phenotype correlation.
5. **Explore GnT-III/Wnt compensatory axis** ([PMID: 24619415](https://pubmed.ncbi.nlm.nih.gov/24619415/)) as a candidate modifier/therapeutic lever.
6. **Develop a reflex diagnostic pathway** that proceeds directly to serum N-glycan MS and _FUT8_ sequencing when CDG is suspected but transferrin IEF is normal, to reduce under-ascertainment.

---

*Report compiled from 5 iterations of autonomous investigation; 10 confirmed findings; 36 papers reviewed. Evidence types are labeled per finding (human clinical, model organism, in vitro, structural/computational).*


## Artifacts

- [OpenScientist final report](FUT8-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](FUT8-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0036065` (obsolete fucosylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001252` (1 mention) - the report calls it "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0002086` (1 mention) - the report calls it "Respiratory abnormality"; HP calls it **Abnormality of the respiratory system**, and lists "Respiratory abnormality" among its other names
- `HP:0009826` (1 mention) - the report calls it "Shortened limbs"; HP calls it **Limb undergrowth**, and lists "Short limbs" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

27 of 30 terms resolved to a current term; the rest could not be looked up either way.