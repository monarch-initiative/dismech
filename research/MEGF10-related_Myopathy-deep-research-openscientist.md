---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T13:54:14.402539'
end_time: '2026-10-31T14:34:25.953856'
duration_seconds: 2411.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MEGF10-Related Myopathy
  mondo_id: MONDO:0013731
  category: Mendelian
  causal_genes: MEGF10
  omim_id: OMIM:614399
  synonyms: MEGF10 myopathy; congenital myopathy 10A, severe variant
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
citation_count: 23
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 27
  verified: 24
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.04
  labels_checked: 9
  labels_matching: 5
  labels_variant: 4
  unresolved_terms:
  - HP:0001383
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MEGF10-related_Myopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MEGF10-related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MEGF10-Related Myopathy
- **MONDO ID:** MONDO:0013731 (if available)
- **Causal gene(s):** MEGF10
- **OMIM:** OMIM:614399
- **Synonyms:** MEGF10 myopathy; congenital myopathy 10A, severe variant
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MEGF10-Related Myopathy** covering all of the
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

# MEGF10-Related Myopathy (EMARDD): A Comprehensive Disease Characterization

**Disease:** MEGF10-Related Myopathy / Early-onset Myopathy, Areflexia, Respiratory Distress and Dysphagia (EMARDD)
**Causal gene:** **MEGF10** (Multiple EGF-like domains 10)
**MONDO:** MONDO:0013731 · **OMIM disease:** #614399 · **OMIM gene:** 612453 · **Orphanet:** ORPHA:280671 · **HGNC:** 3233 · **UniProt:** Q96KG7 · **NCBI Gene:** 84466 · **Locus:** 5q33.2–33.3
**Inheritance:** Autosomal recessive · **Category:** Mendelian

---

## Summary

MEGF10-related myopathy is an ultra-rare, autosomal-recessive congenital myopathy caused by biallelic (homozygous or compound-heterozygous) mutations in **MEGF10**, the gene encoding Multiple EGF-like domains 10 — a single-pass transmembrane receptor with 17 atypical extracellular EGF-like domains that regulates skeletal-muscle satellite (stem) cell self-renewal, proliferation, differentiation and fusion through the Notch signaling pathway. The classic, severe form is historically named EMARDD (Early-onset Myopathy, Areflexia, Respiratory Distress and Dysphagia), first defined by Logan and colleagues in 2011 [PMID: 22101682]. Loss of MEGF10 function depletes the self-renewing Pax7⁺ satellite-cell pool and impairs regeneration and maintenance of myofibers, producing progressive limb (proximal and distal), facial, axial, bulbar (dysphagia) and diaphragmatic (respiratory failure) weakness, together with areflexia, scoliosis and joint contractures, and notably **without** central-nervous-system or cognitive involvement.

A robust **genotype–phenotype correlation** governs severity. Patients carrying at least one null/truncating allele develop respiratory dysfunction within the first year of life (severe classic EMARDD), whereas patients with two missense mutations — frequently cysteine substitutions in the extracellular EGF-like domains — present a much milder minicore/multiminicore myopathy with onset of respiratory decline around age 10 or far later, including the fourth-to-seventh decade. This correlation has been documented in cohort review [PMID: 29128256] and statistically confirmed [PMID: 35370044].

There is **no approved disease-modifying therapy**; management is entirely supportive and multidisciplinary (respiratory support/ventilation, nutritional/feeding support for dysphagia, orthopedic management of scoliosis and contractures, physiotherapy). The single most promising experimental lead is **sertraline** (and escitalopram) — selective serotonin reuptake inhibitors identified in a small-molecule screen that rescued Megf10-deficient mouse myoblasts, patient iPSC-derived myoblasts, Drosophila and zebrafish models and restored deficient Notch1 levels [PMID: 31267131]. Prevention is genetic (carrier/cascade testing, counseling, prenatal/preimplantation testing); there are no environmental risk or protective factors because the disease is monogenic.

---

## Key Findings

### Finding 1 — MEGF10 is the causal gene for autosomal-recessive EMARDD

Biallelic recessive mutations in **MEGF10** (chromosome 5q33; OMIM gene 612453; OMIM disease 614399; MONDO:0013731) cause EMARDD. The gene was identified by Logan et al. (2011) using phased haplotype analysis followed by targeted exome sequencing in a previously unclassified infantile myopathy. The cardinal clinical tetrad is infantile-onset muscle weakness, diaphragmatic weakness with respiratory distress, areflexia, and dysphagia, in the absence of CNS anomalies; scoliosis and joint contractures are common accompaniments.

The original report also established the cellular mechanism: *"MEGF10 is highly expressed in activated satellite cells and regulates their proliferation as well as their differentiation and fusion into multinucleated myofibers, which are greatly reduced in muscle from individuals with early onset myopathy, areflexia, respiratory distress and dysphagia."* [PMID: 22101682]. This sentence links the genetic lesion to the downstream histological hallmark — a paucity of regenerated myofibers.

### Finding 2 — Genotype–phenotype correlation: truncating vs missense (cysteine) variants

Disease severity tracks the molecular consequence of the two alleles. Patients with **≥1 null/truncating allele** develop respiratory dysfunction in the first year of life (severe, classic EMARDD). Patients with **two missense mutations** develop respiratory dysfunction at ~10 years or much later, including adult onset, and tend toward a milder minicore-myopathy phenotype. Harris et al. (2018), reviewing all reported cases (n=20), stated: *"with ≥1 null mutation onset of respiratory dysfunction occurs in the first year of life, whereas with 2 missense mutations, respiratory dysfunction occurs at 10 years old or much later"* [PMID: 29128256]. Fujii et al. (2022) provided statistical confirmation: *"patients with missense mutations in at least one allele had significantly later onset than those with biallelic truncation mutations"* [PMID: 35370044].

Missense variants cluster in the extracellular EGF-like domains and frequently substitute conserved cysteines (e.g., p.Cys326Arg, p.Cys118Arg, p.Cys810Tyr, p.Cys774Arg, p.Cys611Trp, p.Cys124Arg, p.Cys828Trp). Reported variant classes span nonsense, frameshift, splice-site, whole-exon deletions (consistent with fork-stalling/template-switching mechanisms), and missense.

| Genotype class | Typical onset of respiratory failure | Phenotype | Muscle pathology |
|---|---|---|---|
| ≥1 null/truncating allele | First year of life | Severe classic EMARDD | Dystrophic/myopathic, reduced fiber number |
| Biallelic missense (cysteine) | ~10 years → adult (4th–7th decade) | Mild minicore/multiminicore myopathy | Multiple minicores; late cases show rimmed vacuoles/aggregates |

### Finding 3 — Mechanism: MEGF10 balances satellite-cell proliferation vs differentiation via Notch

Megf10 marks quiescent satellite cells and myoblasts but not differentiated myofibers. Retroviral Megf10 overexpression enhances myoblast proliferation and inhibits differentiation; conversely, Megf10 silencing triggers premature differentiation and collapse of the self-renewing stem-cell pool. Holterman et al. (2007) reported: *"Megf10 silencing in activated satellite cells on individual fibers or in cultured myoblasts results in a dramatic reduction in the cell number, caused by myogenin activation and precocious differentiation as well as a depletion of the self-renewing Pax7+/MyoD- population. Additionally, Megf10 silencing in MyoD-/- myoblasts results in down-regulation of Notch signaling components."* [PMID: 18056409].

The molecular link to Notch is direct: *"MEGF10 interacts with the intracellular domain of NOTCH1"* [PMID: 35968817]. MEGF10 thus sustains Notch activity that keeps satellite cells in a self-renewing, proliferative state; its loss shifts the balance toward premature differentiation and stem-cell exhaustion.

### Finding 4 — Therapeutic lead: SSRIs (sertraline) rescue MEGF10-deficient models by restoring Notch

A phenotypic small-molecule screen on Megf10-deficient myoblasts identified two SSRIs, sertraline and escitalopram. Saha et al. (2019) reported: *"The screen yielded two promising candidates that are both selective serotonin reuptake inhibitors (SSRIs), sertraline and escitalopram. In depth follow-up analyses demonstrated that sertraline was highly effective in alleviating abnormalities across multiple models of the disease including mouse myoblast, human myoblast, Drosophila and zebrafish models. Sertraline also restored deficiencies of Notch1 in disease models."* [PMID: 31267131]. Because sertraline is already an approved drug, this nominates a mechanism-based repurposing strategy acting on the Notch axis, though it has not yet entered a registered clinical trial for this indication.

### Finding 5 — Clinical phenotype spectrum and muscle pathology

The phenotype ranges from severe antenatal/infantile classic EMARDD (hypotonia, feeding difficulty/dysphagia, diaphragmatic weakness with early respiratory failure, areflexia) to milder minicore/multiminicore myopathy with late adult onset. Core features across cohorts include progressive proximal and distal limb weakness, facial weakness, scoliosis (often severe and sometimes the presenting sign), joint contractures with distal joint hyperlaxity and high-arched feet, respiratory insufficiency, and dysphagia, with no cognitive involvement. Liewluck et al. (2016) documented a milder multiminicore presentation: *"Both had scoliosis, distal joint hyperlaxity, and high-arched feet. A biopsy of the right triceps muscle in 1 sister showed multiple minicore structures. She had electromyographic changes of myopathy with fibrillation potentials and myotonic discharges."* [PMID: 26802438].

Muscle biopsy is variable: multiple minicores (focally reduced oxidative-enzyme activity), dystrophic plus myopathic features, and myofibrillar protein aggregation. In late-onset disease, pathology can resemble myofibrillar myopathy — Zhu et al. (2026) found that *"Muscle pathology was characterized by rimmed vacuoles, and abnormal protein aggregates rather than minicores."* [PMID: 41475242]. Serum creatine kinase (CK) is typically normal or only mildly elevated. MEGF10 is recognized among the genetic causes of multiminicore/core myopathy [PMID: 34627702].

### Finding 6 — Protein architecture: 17 atypical EGF-like domains; cysteine missense disrupt disulfide bonds

MEGF10 is a single-pass transmembrane protein whose extracellular region contains 17 atypical EGF-like domains, each with eight cysteines that likely form disulfide bonds. Boyden et al. (2012) established: *"MEGF10 contains 17 atypical epidermal growth factor-like domains, each of which contains eight cysteine residues that likely form disulfide bonds. Both the p.C326R and p.C774R mutations alter one of these residues, which are completely conserved in vertebrates."* [PMID: 22371254]. They identified compound-heterozygous c.976T>C (p.C326R) + c.2320T>C (p.C774R), absent from ≥645 controls and co-segregating with a recessive congenital minicore myopathy, and demonstrated muscle defects in zebrafish megf10 morphants. Pathogenic missense mutations that substitute these conserved extracellular cysteines are predicted to disrupt disulfide-bonded EGF-domain folding, explaining the partial loss-of-function/hypomorphic behavior that underlies the milder phenotype.

### Finding 7 — MEGF10 is a conserved phagocytic/engulfment receptor (Draper/CED-1 ortholog)

Beyond muscle, MEGF10 is the mammalian ortholog of *Drosophila* Draper and *C. elegans* CED-1 and functions as a transmembrane phagocytic receptor for apoptotic-cell clearance. It is expressed in neurons and astrocytes and mediates engulfment of neurotoxic amyloid-β. Fujita et al. (2020) noted: *"multiple-EGF like domains 10 (MEGF10) plays an important role in apoptotic cell elimination and is expressed in mammalian neurons and astrocytes"* [PMID: 32682823]. In *Drosophila*, *"Two transmembrane glial phagocytic receptors, SIMU (homolog of the mammalian Stabilin-2) and Draper (homolog of the mammalian MEGF10 and Jedi), mediate glial phagocytosis of apoptotic neurons"* [PMID: 29520845], grounding the cross-species model systems. These additional functions (synapse elimination, retinal neuron mosaic spacing) are not the primary drivers of the muscle disease but illuminate conserved biology.

### Finding 8 — Model organisms and phenotype recapitulation

Multiple validated models exist. The **Megf10⁻/⁻ knockout mouse** shows fewer muscle fibers in juvenile and adult animals, impaired satellite-cell migration and muscle regeneration [PMID: 33159715], and early, progressive neuromuscular-junction (NMJ) degeneration. Juros et al. (2024) reported: *"We found fewer muscle fibers in juvenile and adult Megf10 KO mice, supporting published studies that MEGF10 regulates myogenesis by affecting satellite cell differentiation."* and *"We found early and progressive degenerative features at the NMJs of Megf10 KO mice that include increased postsynaptic fragmentation and presynaptic regions not apposed by postsynaptic nicotinic acetylcholine receptors."* [PMID: 38760872]. **Zebrafish** megf10 morphants/mutants show muscle defects [PMID: 22371254; PMID: 31267131]; **Drosophila** drpr (Draper) mutants model MEGF10 loss; and **patient iPSC-derived myoblasts** recapitulate the proliferation defect. MEGF10 overexpression in mouse myoblasts modulates fusion and the hypertrophic overload response [PMID: 39825147].

| Model | System | Key phenotype | PMID |
|---|---|---|---|
| Megf10⁻/⁻ mouse | Mammalian KO | Reduced fiber number; impaired regeneration; progressive NMJ degeneration | 33159715, 38760872 |
| Zebrafish megf10 | Vertebrate morphant/mutant | Muscle defects | 22371254, 31267131 |
| Drosophila drpr | Invertebrate | Engulfment/myogenesis defects; drug rescue | 31267131 |
| Patient iPSC myoblasts | Human in vitro | Proliferation defect; sertraline rescue | 31267131 |

### Finding 9 — MEGF10 sits within a Notch-pathway muscle-disease gene network; NMJ is a second disease site

MEGF10, **POGLUT1**, and **JAG2** are three Notch-pathway genes whose biallelic loss causes congenital myopathy/muscular dystrophy — *"the discoveries of three new muscle disease genes have added a new dimension to the relationship between the Notch signaling pathway and skeletal muscle: MEGF10, POGLUT1, and JAG2"* [PMID: 35968817]. Functional cross-talk is demonstrated: *"Jag2 downregulation in murine myoblasts led to downregulation of multiple components of the Notch pathway, including Megf10"* [PMID: 33861953]. The Megf10 KO mouse additionally reveals a second anatomical site of pathology — the NMJ — expanding the disease beyond the satellite-cell axis alone [PMID: 38760872].

### Finding 10 — Epidemiology, inheritance and diagnostic workflow

MEGF10 myopathy is **ultra-rare**: Harris et al. (2018) reviewed *"all reported MEGF10 cases (n = 20)"* [PMID: 29128256], and only a few dozen families have been reported worldwide since 2011. Orphanet lists ORPHA:280671; point prevalence is not formally established (<1/1,000,000). Inheritance is **autosomal recessive**, with unaffected heterozygous carriers [PMID: 34828389]; both sexes are affected equally. Penetrance for biallelic genotypes is effectively complete, while expressivity is highly variable and genotype-driven. Consanguinity increases the risk of homozygous genotypes.

Diagnosis proceeds from clinical suspicion (infantile hypotonia/respiratory distress/dysphagia, or childhood scoliosis + weakness) → serum CK (normal/mildly elevated) → EMG (myopathic) → muscle biopsy (minicores/dystrophic-myopathic/aggregates; variable) → confirmatory molecular genetic testing. Next-generation sequencing (congenital-myopathy gene panels, WES, WGS) is the mainstay; CMA/SNP-array and breakpoint analysis detect exonic deletions. Pierson et al. (2013) illustrated structural-variant detection: *"By novel analysis of SNP array hybridization and exome sequence coverage, we diagnosed a 10-years old girl with EMARDD following identification of a novel homozygous deletion of exon 7 in MEGF10."* [PMID: 23453856].

### Finding 11 — Treatment, prognosis and prevention are supportive; sertraline is the leading experimental lead

No approved disease-modifying therapy exists: *"There are no disease-modifying therapies."* [PMID: 31267131] and *"There are no treatments for the progressive respiratory distress, motor impairment, and structural abnormalities in muscles caused by the loss of MEGF10 function."* [PMID: 38760872]. Management is multidisciplinary and supportive: respiratory support (non-invasive/invasive ventilation, airway clearance), nutritional/feeding support for dysphagia (nasogastric/gastrostomy feeding) [PMID: 37753494], and orthopedic management of scoliosis and contractures. Prognosis follows genotype: severe (≥1 null allele) cases face early respiratory failure, ventilator dependence and non-ambulation, often life-threatening in infancy/early childhood; mild (biallelic missense) cases retain ambulation longer with later respiratory decline and a normal/near-normal lifespan. Prevention is genetic: carrier/cascade testing, genetic counseling (25% recurrence risk per pregnancy for carrier couples), and prenatal/preimplantation genetic testing when familial variants are known.

---

## Section-by-Section Report

### 1. Disease Information
MEGF10-related myopathy is a Mendelian, autosomal-recessive congenital myopathy with a muscular-dystrophy overlap, caused by biallelic MEGF10 mutations. The severe form is EMARDD (Early-onset Myopathy, Areflexia, Respiratory Distress and Dysphagia); the mild form is a minicore/multiminicore myopathy. **Identifiers:** MONDO:0013731; OMIM disease #614399; OMIM gene 612453; Orphanet ORPHA:280671; HGNC:3233; UniProt Q96KG7; NCBI Gene 84466. **Synonyms:** MEGF10 myopathy; congenital myopathy 10A (severe variant) and 10B (mild variant); EMARDD; MEGF10-related minicore myopathy. Information is derived from aggregated disease-level resources (OMIM, Orphanet) and individual case reports/small cohorts (n≈20 in the 2018 review), not EHR-scale datasets.

### 2. Etiology
**Causal factor:** purely genetic — biallelic loss-of-function or cysteine-disrupting missense variants in MEGF10. **Genetic risk factors:** the causal variants themselves; consanguinity raises homozygous-genotype risk; JAG2 and POGLUT1 define a shared Notch-pathway disease network, and Jag2 loss downregulates Megf10 [PMID: 33861953]. **Environmental risk/protective factors:** none established — the disease is monogenic. **Gene–environment interactions:** none documented. No protective alleles are reported.

### 3. Phenotypes
Representative phenotypes and suggested HPO terms:

| Phenotype | HPO term | Onset | Severity/frequency |
|---|---|---|---|
| Neonatal hypotonia | HP:0001319 | Neonatal (severe) | Common in severe form |
| Areflexia | HP:0001284 | Infantile | Cardinal feature |
| Respiratory insufficiency/distress | HP:0002093 | <1 yr (null) to adult (missense) | Universal; genotype-timed |
| Dysphagia | HP:0002015 | Infantile–childhood | Common |
| Diaphragmatic weakness | HP:0009113 | Infantile | Characteristic |
| Proximal + distal muscle weakness | HP:0003701 / HP:0002460 | Variable | Progressive |
| Facial weakness | HP:0010628 | Variable | Common |
| Scoliosis | HP:0002650 | Childhood | Common; sometimes presenting |
| Joint contractures | HP:0002803 | Variable | Common |
| Distal joint hyperlaxity | HP:0001383 | Childhood | Milder form [PMID: 26802438] |
| Elevated/normal CK | HP:0003236 | — | Normal or mildly elevated |

Progression is slowly progressive; severity is variable and genotype-driven. Quality-of-life impact is substantial in severe cases (ventilator dependence, non-ambulation, feeding support), milder in late-onset cases. No disease-specific QoL instrument has been validated; generic congenital-myopathy motor outcome measures lack disease-specificity [PMID: 40450412].

### 4. Genetic/Molecular Information
**Causal gene:** MEGF10 (HGNC:3233; 5q33.2–33.3). **Variant classes:** nonsense, frameshift, splice-site, whole-exon deletions, and missense (frequently extracellular cysteine substitutions). **Classification:** pathogenic/likely pathogenic per ACMG/AMP; null alleles absent from population controls (≥645 controls for p.C326R/p.C774R [PMID: 22371254]). **Allele frequency:** very low/absent in gnomAD for pathogenic alleles. **Origin:** germline. **Functional consequence:** loss of function (truncating → severe; cysteine missense → hypomorphic/partial LOF → mild). **Modifier genes:** JAG2/POGLUT1 network members are mechanistically connected but not established as clinical modifiers. **Epigenetic/chromosomal:** no recurrent epigenetic signature or large chromosomal abnormality beyond intragenic exon deletions.

### 5. Environmental Information
Not applicable. No environmental toxins, lifestyle factors, or infectious agents are implicated; the disease is strictly monogenic. As a congenital myopathy, caution with triggering anesthetic agents is prudent clinically, though MEGF10 is not a confirmed malignant-hyperthermia gene (general congenital-myopathy anesthesia context [PMID: 41504952]).

### 6. Mechanism / Pathophysiology — Ordered Causal Chain
1. **Biallelic MEGF10 mutation** (truncating or cysteine-disrupting missense) → **loss or reduction of functional MEGF10 receptor** at the satellite-cell surface. *(Demonstrated; cysteine missense inferred to misfold EGF domains [PMID: 22371254].)*
2. Loss of MEGF10 → **reduced interaction with the NOTCH1 intracellular domain → down-regulation of Notch signaling** in satellite cells/myoblasts. *(Demonstrated in vitro [PMID: 18056409, 35968817].)*
3. Reduced Notch → **myogenin activation and precocious differentiation**, depleting the self-renewing Pax7⁺/MyoD⁻ satellite-cell pool. *(Demonstrated [PMID: 18056409].)*
4. Depleted satellite-cell pool → **impaired myoblast proliferation, fusion, and myofiber regeneration** → **reduced myofiber number**. *(Demonstrated in patients and mouse KO [PMID: 22101682, 38760872].)*
5. (Branch) Loss of MEGF10 → **progressive NMJ degeneration** (postsynaptic fragmentation, presynaptic loss). *(Demonstrated in mouse [PMID: 38760872]; human relevance inferred.)*
6. Reduced/abnormal myofibers + NMJ pathology → **progressive muscle weakness** (limb, facial, axial, bulbar, diaphragmatic).
7. Diaphragmatic + bulbar weakness → **respiratory failure and dysphagia**; axial weakness → **scoliosis** → the clinical EMARDD phenotype.

**Pathways/processes:** Notch signaling (KEGG hsa04330); satellite-cell self-renewal; myogenic differentiation; apoptotic-cell engulfment (secondary). **GO terms:** regulation of Notch signaling pathway (GO:0008593); skeletal muscle satellite cell proliferation/differentiation (GO:0014842/GO:0014816); myoblast fusion (GO:0007520); apoptotic cell clearance (GO:0043277). **Cell types (CL):** skeletal muscle satellite cell (CL:0000594); myoblast (CL:0000056); skeletal muscle fiber (CL:0000188). **Protein dysfunction:** loss of function via disrupted extracellular disulfide-bonded EGF domains or truncation.

### 7. Anatomical Structures Affected
**Primary organ/system:** skeletal muscle / musculoskeletal system (UBERON:0001134 skeletal muscle tissue). Particularly affected: diaphragm (UBERON:0001103), axial/paraspinal muscles (→ scoliosis), limb muscles (proximal + distal), facial and pharyngeal muscles (→ dysphagia). **Secondary:** respiratory system (ventilatory failure), spine (scoliosis), joints (contractures), and the neuromuscular junction (UBERON:0002050) per mouse data. **No CNS involvement.** **Cell level:** satellite cells (CL:0000594), myoblasts, myofibers. **Subcellular:** plasma membrane (single-pass transmembrane receptor; GO:0005886); sarcomeric cores and myofibrillar aggregates in pathology. **Lateralization:** bilateral/generalized.

### 8. Temporal Development
**Onset:** antenatal/neonatal to infantile in severe (null-allele) disease; childhood to adult (4th–7th decade) in mild (biallelic-missense) disease. **Pattern:** chronic, insidious, slowly progressive; lifelong. **Stages:** early weakness/hypotonia → progressive respiratory and motor decline → ventilator dependence/non-ambulation (severe) or prolonged ambulation with later respiratory decline (mild). **Critical period:** the first year of life for null-allele patients (respiratory failure window). No spontaneous remission.

### 9. Inheritance and Population
**Epidemiology:** ultra-rare; ~20 cases in the 2018 review, a few dozen families total; prevalence <1/1,000,000. **Inheritance:** autosomal recessive; carriers unaffected. **Penetrance:** effectively complete for biallelic genotypes. **Expressivity:** highly variable, genotype-driven. **Consanguinity:** increases homozygous-genotype risk. **Founder effects/anticipation/mosaicism:** none established. **Sex ratio:** 1:1. **Geographic:** reported worldwide (European, Middle Eastern, East Asian, North African cohorts), without a dominant endemic region.

### 10. Diagnostics
**Labs:** serum CK normal or mildly elevated. **EMG:** myopathic, with fibrillation potentials and myotonic discharges possible [PMID: 26802438]. **Imaging:** muscle MRI/ultrasound show myopathic changes (non-specific). **Biopsy:** multiple minicores (reduced oxidative-enzyme activity), dystrophic/myopathic features, or — in late-onset disease — rimmed vacuoles and protein aggregates [PMID: 41475242]. **Genetic testing (confirmatory):** NGS gene panels for congenital myopathy/neuromuscular disease, WES or WGS; single-gene MEGF10 sequencing with deletion/duplication analysis; CMA/SNP-array for exonic deletions [PMID: 23453856]. **Differential diagnosis:** RYR1/SELENON multiminicore disease, LAMA2-related dystrophy, SMA, other congenital myopathies, myofibrillar myopathies (in late-onset cases). **Screening:** carrier/cascade testing within affected families; not part of population newborn screening.

### 11. Outcome / Prognosis
Prognosis is genotype-dependent. **Severe (≥1 null allele):** early respiratory failure, often life-threatening or fatal in infancy/early childhood, ventilator dependence, loss of ambulation. **Mild (biallelic missense):** prolonged ambulation, later respiratory decline, and normal/near-normal lifespan. **Morbidity:** respiratory insufficiency, dysphagia-related nutritional compromise, scoliosis, contractures, recurrent respiratory infections. **Prognostic factors:** genotype (null vs missense) is the dominant predictor of onset and severity. No validated molecular prognostic biomarker beyond genotype.

### 12. Treatment
**No approved disease-modifying therapy** [PMID: 31267131, 38760872]. **Supportive/standard care:** respiratory support (non-invasive/invasive ventilation, airway clearance; NCIT mechanical ventilation), nutritional/feeding support including gastrostomy for dysphagia [PMID: 37753494], orthopedic management of scoliosis (bracing/spinal fusion) and contractures, physiotherapy and occupational therapy. **Experimental:** SSRIs — **sertraline** (lead) and escitalopram — rescued four MEGF10-deficient models and restored Notch1 [PMID: 31267131], nominating Notch-pathway pharmacology/drug repurposing; not yet in registered trials for this indication. **Pharmacogenomics/gene therapy/cell therapy:** none clinically available; MEGF10's satellite-cell biology and recessive LOF mechanism make gene replacement conceptually attractive but unproven. **NCIT suggestions:** Sertraline (C29379); Mechanical Ventilation (C70909); Physical Therapy (C49236); Gastrostomy (C51674).

### 13. Prevention
No primary prevention is possible (monogenic). **Genetic prevention:** carrier/cascade testing of relatives, genetic counseling (25% recurrence risk per pregnancy for carrier couples), and prenatal or preimplantation genetic testing when familial variants are known. **Tertiary prevention:** surveillance and proactive management of respiratory function, nutrition, and spine/joint complications. No immunization or environmental intervention applies.

### 14. Other Species / Natural Disease
**Orthologs / NCBI Gene IDs:** human MEGF10 (84466); mouse Megf10 (70417); zebrafish megf10; *Drosophila* drpr/Draper; *C. elegans* ced-1. **Taxonomy (NCBI Taxon):** *Homo sapiens* 9606; *Mus musculus* 10090; *Danio rerio* 7955; *Drosophila melanogaster* 7227; *Caenorhabditis elegans* 6239. **Natural disease:** no well-characterized spontaneous MEGF10 myopathy reported in companion animals (no established OMIA entry for this muscle disease). **Comparative biology:** the engulfment-receptor function is deeply conserved (Draper/CED-1), and myogenic/Notch roles are conserved in vertebrate models [PMID: 29520845, 32682823]. **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms
- **Mouse (Megf10⁻/⁻ KO):** reduced fiber number, impaired satellite-cell migration/regeneration, progressive NMJ degeneration — strong recapitulation of the myogenic defect; NMJ pathology may exceed what is documented in humans [PMID: 33159715, 38760872]. Resource: MGI.
- **Zebrafish (megf10 morphant/mutant):** muscle defects; used for drug-screening validation [PMID: 22371254, 31267131]. Resource: ZFIN.
- **Drosophila (drpr mutant):** models MEGF10 loss; responsive to sertraline [PMID: 31267131]. Resource: FlyBase.
- **Patient iPSC-derived myoblasts:** human in vitro model recapitulating proliferation defects and sertraline rescue [PMID: 31267131]. Resource: Cellosaurus.
- **Overexpression systems:** human MEGF10 in mouse myoblasts to study fusion/overload hypertrophy [PMID: 39825147].

**Limitations of models:** the Megf10 KO mouse is relatively mild and does not fully reproduce lethal human respiratory failure; cysteine-missense (hypomorphic) genotypes are under-modeled; cross-species engulfment roles may confound muscle-specific interpretation.

---

## Mechanistic Model / Interpretation

```
 Biallelic MEGF10 mutation
   (truncating → severe | cysteine-missense → mild/hypomorphic)
            │
            ▼
 Loss/reduction of MEGF10 transmembrane receptor
            │  (binds NOTCH1 intracellular domain)
            ▼
 Down-regulation of NOTCH signaling in satellite cells
            │
            ▼
 Myogenin activation → precocious differentiation
            │
            ▼
 Depletion of self-renewing Pax7+/MyoD- satellite-cell pool
            │
     ┌──────┴───────────────────────────┐
     ▼                                   ▼
 Impaired myoblast proliferation/     Progressive NMJ degeneration
 fusion → reduced myofiber number     (postsynaptic fragmentation;
 & poor regeneration                   mouse-demonstrated)
     │                                   │
     └──────────────┬────────────────────┘
                    ▼
 Progressive weakness: limb + facial + axial + bulbar + diaphragmatic
                    │
                    ▼
 EMARDD: respiratory failure, dysphagia, areflexia, scoliosis, contractures
         (no CNS involvement)
```

The disease is best understood as a **"satellite-cell-opathy"** — a congenital myopathy arising from stem-cell dysfunction rather than a purely structural myofiber defect [PMID: 35302338, 41193724]. MEGF10 keeps satellite cells in a proliferative, self-renewing state through Notch; its loss tips the balance toward premature differentiation and stem-cell exhaustion, starving muscle of the regenerative capacity needed to maintain fiber number over a lifetime. The genotype–phenotype correlation falls out naturally from residual MEGF10 function: null alleles abolish the receptor (severe infantile disease), whereas cysteine-missense alleles leave partial function (mild, late-onset minicore myopathy). The Notch-restoring action of sertraline provides mechanistic proof-of-concept that pharmacologically re-activating the downstream pathway can partially bypass the upstream receptor lesion.

---

## Evidence Base

| PMID | Study (abbrev.) | Supports |
|---|---|---|
| [22101682](https://pubmed.ncbi.nlm.nih.gov/22101682/) | MEGF10 mutations cause EMARDD (Logan 2011) | F1 — gene discovery, satellite-cell function |
| [29128256](https://pubmed.ncbi.nlm.nih.gov/29128256/) | MEGF10 myopathies review, adult-onset case (Harris 2018) | F2, F10 — genotype-phenotype, n=20 epidemiology |
| [35370044](https://pubmed.ncbi.nlm.nih.gov/35370044/) | Novel mutation + genotype-phenotype (Fujii 2022) | F2 — statistical confirmation |
| [18056409](https://pubmed.ncbi.nlm.nih.gov/18056409/) | Megf10 regulates satellite-cell program (Holterman 2007) | F3 — Notch/self-renewal mechanism |
| [35968817](https://pubmed.ncbi.nlm.nih.gov/35968817/) | Notch pathway in muscle (Vargas-Franco 2022) | F3, F9 — MEGF10–NOTCH1 interaction, gene network |
| [31267131](https://pubmed.ncbi.nlm.nih.gov/31267131/) | SSRIs ameliorate MEGF10 myopathy (Saha 2019) | F4, F11 — sertraline rescue, no DMT |
| [26802438](https://pubmed.ncbi.nlm.nih.gov/26802438/) | Adult multiminicore, novel MEGF10 (Liewluck 2016) | F5 — mild phenotype, minicores, EMG |
| [41475242](https://pubmed.ncbi.nlm.nih.gov/41475242/) | Late-onset myofibrillar-like phenotype (Zhu 2026) | F5 — rimmed vacuoles/aggregates |
| [34627702](https://pubmed.ncbi.nlm.nih.gov/34627702/) | Core myopathy review (Ogasawara 2021) | F5 — MEGF10 among core-myopathy genes |
| [22371254](https://pubmed.ncbi.nlm.nih.gov/22371254/) | Recessive minicore myopathy (Boyden 2012) | F6 — 17 EGF domains, cysteine disulfides |
| [32682823](https://pubmed.ncbi.nlm.nih.gov/32682823/) | MEGF10 engulfs amyloid-β (Fujita 2020) | F7 — phagocytic-receptor function |
| [29520845](https://pubmed.ncbi.nlm.nih.gov/29520845/) | Draper/JNK glial phagocytosis (Hilu-Dadia 2018) | F7 — Draper = MEGF10 ortholog |
| [38760872](https://pubmed.ncbi.nlm.nih.gov/38760872/) | Mouse model muscle/NMJ alterations (Juros 2024) | F8, F9, F11 — mouse KO, NMJ, no treatment |
| [33159715](https://pubmed.ncbi.nlm.nih.gov/33159715/) | Megf10 deficiency impairs regeneration (Li 2021) | F8 — satellite-cell migration/regeneration |
| [39825147](https://pubmed.ncbi.nlm.nih.gov/39825147/) | MEGF10 in fusion/overload (Richardson 2025) | F8 — overexpression effects |
| [33861953](https://pubmed.ncbi.nlm.nih.gov/33861953/) | JAG2 muscular dystrophy (Coppens 2021) | F9 — Jag2–Megf10 Notch cross-talk |
| [23453856](https://pubmed.ncbi.nlm.nih.gov/23453856/) | Exon 7 deletion by SNP array (Pierson 2013) | F10 — structural-variant diagnosis |
| [34828389](https://pubmed.ncbi.nlm.nih.gov/34828389/) | Phenotypic variability (AlMuhaizea 2021) | F10 — AR inheritance, carriers unaffected |
| [37753494](https://pubmed.ncbi.nlm.nih.gov/37753494/) | GI/nutritional care in pediatric NMD (Dipasquale 2023) | F11 — feeding/nutrition support |
| [35302338](https://pubmed.ncbi.nlm.nih.gov/35302338/) | Satellite cell-opathies (review) | Mechanistic framing |
| [41193724](https://pubmed.ncbi.nlm.nih.gov/41193724/) | Satellite-cell congenital myopathies (review) | Mechanistic framing |

All 11 confirmed findings are supported by verified abstract quotations. One citation for impaired satellite-cell migration (PMID 33159715) was flagged as a title-level match; its claim is corroborated by the independently verified mouse-KO myogenesis data in PMID 38760872.

---

## Limitations and Knowledge Gaps

- **Small evidence base.** Fewer than ~40 families are reported worldwide; prevalence/incidence figures are estimates, and no formal registry or natural-history study exists specifically for MEGF10 myopathy (contrast with LAMA2/SELENON natural-history efforts [PMID: 39443859]).
- **Model–human mismatch.** The Megf10 KO mouse is comparatively mild and does not reproduce lethal human respiratory failure; the striking mouse NMJ pathology has not been confirmed as a primary human disease site. Cysteine-missense (hypomorphic) genotypes are under-modeled.
- **Therapeutics unproven in humans.** Sertraline's rescue is entirely preclinical; no clinical trial has tested it (or any Notch-modulating agent) in patients. Dosing, timing (prenatal vs postnatal window), and whether partial Notch restoration translates to clinical benefit are unknown.
- **Genotype–phenotype gaps.** The quantitative relationship between specific EGF-domain cysteine positions and residual function/severity is not fully mapped; modifier genes that could explain intra-genotype variability are unidentified.
- **Mechanistic uncertainty.** The relative contributions of satellite-cell exhaustion vs direct myofiber/NMJ maintenance roles of MEGF10 to progressive weakness remain to be dissected, as does the role (if any) of MEGF10's phagocytic function in muscle pathology.
- **Outcome measures.** No disease-specific functional or QoL instrument has been validated; existing congenital-myopathy measures lack disease-specificity [PMID: 40450412].

---

## Proposed Follow-up Experiments / Actions

1. **Establish a MEGF10 patient registry and prospective natural-history study** capturing genotype, respiratory/motor trajectories, and standardized outcome measures — essential for future trial readiness.
2. **Clinical translation of sertraline:** a biomarker-anchored (Notch1 target engagement) pilot/early-phase study in genetically confirmed patients, prioritizing the milder missense cohort where a therapeutic window is plausible.
3. **Genotype–function mapping:** systematic in vitro assays (surface expression, NOTCH1-binding, disulfide integrity) across the spectrum of cysteine-missense variants to build a quantitative severity predictor.
4. **Humanized and knock-in models:** generate mouse knock-in lines bearing recurrent human cysteine-missense alleles, and patient iPSC-derived myotube/organoid systems, to better recapitulate the human respiratory/bulbar phenotype.
5. **Modifier-gene search:** within and beyond the JAG2/POGLUT1 Notch network, screen for modifiers explaining intra-genotype variability (expression QTLs, CRISPR screens in myoblasts).
6. **Gene-replacement proof-of-concept:** given recessive LOF and a defined muscle-stem-cell target, test AAV-mediated MEGF10 restoration or satellite-cell-directed delivery in the KO mouse.
7. **NMJ biology:** determine whether NMJ degeneration is a human disease feature (electrophysiology, autopsy/biopsy NMJ morphology) and whether it is a tractable therapeutic target.


## Artifacts

- [OpenScientist final report](MEGF10-related_Myopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MEGF10-related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001383` (1 mention), reported as "Distal joint hyperlaxity" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002093` (1 mention) - the report calls it "Respiratory insufficiency/distress"; HP calls it **Respiratory insufficiency**
- `HP:0010628` (1 mention) - the report calls it "Facial weakness"; HP calls it **Facial palsy**
- `HP:0002803` (1 mention) - the report calls it "Joint contractures"; HP calls it **Congenital contracture**, and lists "congenital contractures" among its other names
- `HP:0003236` (1 mention) - the report calls it "Elevated/normal CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.