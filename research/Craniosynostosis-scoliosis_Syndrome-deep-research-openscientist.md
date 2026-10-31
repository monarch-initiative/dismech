---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:01:12.355229'
end_time: '2026-10-30T23:31:14.263392'
duration_seconds: 1801.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Craniosynostosis-Scoliosis Syndrome
  mondo_id: MONDO:0980974
  category: Mendelian
  causal_genes: DHRS3
  omim_id: OMIM:621499
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 9
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Craniosynostosis-scoliosis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniosynostosis-scoliosis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniosynostosis-Scoliosis Syndrome
- **MONDO ID:** MONDO:0980974 (if available)
- **Causal gene(s):** DHRS3
- **OMIM:** OMIM:621499
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Craniosynostosis-Scoliosis Syndrome** covering all of the
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

# Craniosynostosis–Scoliosis Syndrome (DHRS3 deficiency): A Comprehensive Disease Characterization

**Disease:** Craniosynostosis–Scoliosis Syndrome
**MONDO:** MONDO:0980974 · **OMIM:** 621499 · **Causal gene:** **DHRS3** (SDR16C1)
**Category:** Mendelian, autosomal recessive

---

## Summary

Craniosynostosis–Scoliosis Syndrome (OMIM 621499; MONDO:0980974) is an ultra‑rare, autosomal‑recessive developmental disorder caused by **biallelic hypomorphic variants in DHRS3** (dehydrogenase/reductase 3; also called SDR16C1; HGNC:17693; NCBI Gene 9249; Ensembl ENSG00000162496; UniProt O75911; chromosome 1p36.21). DHRS3 encodes a 302‑amino‑acid, membrane‑associated, NADPH‑dependent **all‑trans‑retinaldehyde reductase** that reduces retinaldehyde back to retinol, thereby limiting the production of the morphogen **all‑trans‑retinoic acid (RA)**. When DHRS3 activity is lost, this brake on RA biosynthesis is released and the embryo is exposed to excess RA — a **genetic phenocopy of retinoic‑acid/isotretinoin embryopathy**.

The disease was defined by Hashimoto and colleagues in 2025 ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)), who studied 8 sibships (12 individuals) carrying 5 homozygous DHRS3 variants. Five homozygotes from three families presented a congruent syndrome of **coronal craniosynostosis, dysmorphic facial features, congenital heart disease (4/5), and scoliosis (5/5)**. Promoter/5′UTR deletions reduced DHRS3 transcription by 90–98%, and affected individuals showed **reduced plasma retinol and elevated plasma retinoic acid** relative to controls and heterozygous relatives — a direct functional readout of the enzymatic defect.

Mechanistically, DHRS3 acts in a **reciprocal complex with RDH10**: RDH10 oxidizes retinol to retinaldehyde (toward RA synthesis), while RDH10‑activated DHRS3 reduces retinaldehyde back to retinol (away from RA synthesis), and the two enzymes mutually activate one another to maintain retinoid homeostasis. Excess RA drives **premature osteogenic differentiation of cranial suture mesenchyme** (through RUNX2 and BMP–SMAD1/5/9 signaling), producing craniosynostosis, and **disrupts somite segmentation and HOX‑based axial patterning**, producing scoliosis and vertebral anomalies. The model is strongly corroborated by the embryonic‑lethal *Dhrs3*‑null mouse (~40% increased ATRA, cardiac/skeletal/palatal defects) and by the human precedent of **CYP26B1** deficiency (loss of the RA‑degrading enzyme), which likewise causes craniosynostosis and skeletal fusions. There is no disease‑specific therapy; management is symptomatic and surgical.

---

## Key Findings

### Finding 1 — DHRS3 deficiency is an autosomal‑recessive retinoic acid embryopathy

The landmark study establishing this disease ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)) examined **8 sibships comprising 12 individuals** with **5 homozygous DHRS3 variants**. Five homozygotes drawn from three families — carrying a promoter/5′UTR deletion or the missense variant **p.(Val171Met)** — displayed a congruent clinical picture: coronal craniosynostosis, dysmorphic facial features, congenital heart disease (4 of 5), and scoliosis (5 of 5). In deletion homozygotes, **DHRS3 transcription was reduced by 90–98%**, confirming a hypomorphic loss‑of‑function state. Plasma biochemistry showed **significantly reduced retinol and elevated retinoic acid** (exceeding the normal range) compared with controls and heterozygous relatives.

The authors frame the disorder as a human genetic counterpart to teratogenic RA exposure, noting that *"Signaling by the morphogen all-trans retinoic acid (RA) is critical for embryonic development, during which its tissue concentration must be tightly regulated"* and that they *"define a novel developmental syndrome associated with biallelic hypomorphic variants in"* DHRS3. The inheritance is therefore **autosomal recessive**, driven by biallelic hypomorphic alleles. (OMIM 621499; MONDO:0980974.)

### Finding 2 — Mechanism: DHRS3 reduces retinaldehyde to retinol in a reciprocal complex with RDH10 to prevent RA excess

DHRS3 is not a constitutively active enzyme in isolation; it **requires RDH10 for full catalytic activity**. Once activated, it becomes *"a robust high affinity all-trans-retinaldehyde-specific reductase that effectively converts retinaldehyde back to retinol, decreasing the rate of retinoic acid biosynthesis"* ([PMID: 24733397](https://pubmed.ncbi.nlm.nih.gov/24733397/)). The two enzymes reciprocally activate one another, creating a balanced control point over retinoid flux.

Genetic loss of DHRS3 in mice produces the predicted biochemical signature: *"Lack of DHRS3 leads to a 40% increase in the levels of ATRA"* ([PMID: 24005908](https://pubmed.ncbi.nlm.nih.gov/24005908/)), along with ~55–60% reductions in retinol and retinyl esters, compensatory downregulation of RA‑synthetic genes, and ~120% upregulation of the RA‑degrading enzyme *Cyp26a1*. DHRS3 expression is itself **directly regulated by RAR/RXR**, forming a negative‑feedback loop for RA homeostasis — *"DHRS3 plays a critical role in this regulation by converting retinaldehyde to retinol, preventing excessive retinoic acid formation"* ([PMID: 39420244](https://pubmed.ncbi.nlm.nih.gov/39420244/)).

### Finding 3 — Craniosynostosis arises from RA‑driven premature osteogenesis of cranial suture mesenchyme

Excess all‑trans‑RA enhances osteogenic differentiation of cranial suture‑derived mesenchymal cells: *"Addition of retinoic acid enhanced the osteogenic differentiation of suture-derived mesenchymal cells in vitro, including up-regulation of alkaline phosphatase activity and Runx2 expression"* ([PMID: 20134361](https://pubmed.ncbi.nlm.nih.gov/20134361/)), while simultaneously repressing proliferation. Downstream, atRA activates BMP signaling — *"BMP signal pathway was found to be activated by atRA, as seen from increased expression of BMPR-2 and pSMAD1/5/9"* ([PMID: 30392121](https://pubmed.ncbi.nlm.nih.gov/30392121/)) — to drive premature suture fusion, an effect that can be blocked by the BMP antagonist Noggin.

The strongest human parallel is **CYP26B1** deficiency: *"We have identified human null and hypomorphic mutations in the gene encoding the RA-degrading enzyme CYP26B1 that lead to skeletal and craniofacial anomalies, including fusions of long bones, calvarial bone hypoplasia, and craniosynostosis"* ([PMID: 22019272](https://pubmed.ncbi.nlm.nih.gov/22019272/)). Because CYP26B1 and DHRS3 both constrain RA (by degradation and by reduced synthesis, respectively), their loss converges on the same craniofacial and skeletal phenotype. Pharmacologic RA excess (isotretinoin embryopathy) likewise produces craniofacial, cardiac, CNS, and skeletal malformations ([PMID: 29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/); [PMID: 34773723](https://pubmed.ncbi.nlm.nih.gov/34773723/)).

### Finding 4 — Plasma retinoid profile is a functional biomarker; scoliosis reflects RA disruption of somite/HOX axial patterning

In DHRS3 homozygotes, plasma retinol was significantly reduced and RA was elevated above the normal range versus controls and heterozygotes; an engineered **DHRS3‑Val171Met** construct showed reduced retinaldehyde‑reduction capacity, lower retinol, and higher RA ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)). This provides a plausible, measurable biochemical biomarker.

RA is a core determinant of axial segmentation. It acts as a posterior‑to‑anterior gradient opposing FGF/WNT within the somite segmentation wavefront: *"this signal is displaced posteriorly by a system of traveling signaling gradients-the wavefront-which depends on the Wnt, FGF, and retinoic acid pathways"* ([PMID: 19651306](https://pubmed.ncbi.nlm.nih.gov/19651306/)). Dysregulated RA perturbs the segmentation clock and vertebral patterning: *"RA depletion thus disrupts timely somite formation at the transition, eventually leading to the loss of one somite and the resultant cervical vertebra"* ([PMID: 24284210](https://pubmed.ncbi.nlm.nih.gov/24284210/)). Disruption of this program provides the mechanistic basis for scoliosis and vertebral anomalies in the syndrome.

### Finding 5 — Retinoic‑acid signaling is an established convergent node in the syndromic craniosynostosis gene network

DHRS3 fits squarely into the known genetic architecture of syndromic craniosynostosis. A large exome study of **526 proband‑parent trios** found a marked excess of damaging de novo variants and concluded that *"De novo variants implicate chromatin modification, transcriptional regulation, and retinoic acid signaling in syndromic craniosynostosis"* ([PMID: 37086723](https://pubmed.ncbi.nlm.nih.gov/37086723/)). More broadly, craniosynostosis candidate genes form a functional network in which *"numerous candidate genes for craniosynostosis belonging to the FGF, Wnt, BMP, Ras/ERK, ephrin, hedgehog, STAT, and retinoic acid signaling pathways have been identified"* ([PMID: 30976277](https://pubmed.ncbi.nlm.nih.gov/30976277/)). The gene alias **CRSS** aligns with the syndrome name.

### Finding 6 — Gene constraint and protein data confirm a recessive hypomorphic loss‑of‑function mechanism

gnomAD constraint metrics show DHRS3 is **not haploinsufficient**: pLI = 0.014, observed/expected LoF = 0.52 (14 observed vs 27.2 expected), LOEUF = 0.81, missense Z = 1.78, LoF Z = 2.14. Heterozygous loss‑of‑function is tolerated, consistent with a **recessive** disease requiring biallelic hypomorphic alleles. UniProt O75911 annotates a 302‑aa "Short‑chain dehydrogenase/reductase 3" catalyzing all‑trans‑retinol + NADP⁺ ⇌ all‑trans‑retinal + NADPH + H⁺ (operating in the retinal→retinol reductive direction to limit RA); it is membrane‑associated and belongs to the classical SDR family (Pfam PF00106; InterPro IPR002347 and the NAD(P)‑binding Rossmann‑like fold IPR036291). Tissue expression is highest in heart, placenta, lung, liver, kidney, pancreas, thyroid, and testis, with **no expression detected in brain** — consistent with a primarily non‑neural, developmental/metabolic role. This anchors the retinaldehyde‑reductase function in limiting RA, since *"Signaling by the morphogen all-trans retinoic acid (RA) is critical for embryonic development, during which its tissue concentration must be tightly regulated"* ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)).

### Finding 7 — Conserved orthologs and validated model organisms

DHRS3 is evolutionarily conserved. Verified orthologs include **mouse *Dhrs3*** (NCBI Gene 20148; MGI:1315215; chromosome 4) and **zebrafish *dhrs3a*** (NCBI Gene 445083; ZFIN ZDB‑GENE‑040801‑217) plus the paralog *dhrs3b*. The *Dhrs3*‑null mouse is the principal validated disease model: *"Consequently, Dhrs3(-/-) embryos die late in gestation and display defects in cardiac outflow tract formation, atrial and ventricular septation, skeletal development, and palatogenesis"* ([PMID: 24005908](https://pubmed.ncbi.nlm.nih.gov/24005908/)). The same model has been used to study aberrant coronary vasculature arising from RA imbalance ([PMID: 29806219](https://pubmed.ncbi.nlm.nih.gov/29806219/)). Human DHRS3 has 117 ClinVar entries.

---

## Mechanistic Model

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic DHRS3 variants** (promoter/5′UTR deletion reducing transcription 90–98%, or missense p.Val171Met reducing catalytic activity) **lead to** loss of all‑trans‑retinaldehyde reductase function. *(demonstrated — PMID 40519748)*
2. Loss of DHRS3 reductase activity **results in** failure to convert retinaldehyde back to retinol, **removing a brake on RA biosynthesis**. *(demonstrated — PMID 24733397, 24005908)*
3. This **leads to** embryonic **retinoic‑acid excess** (elevated RA, reduced retinol in plasma and tissues). *(demonstrated in patients and mouse — PMID 40519748, 24005908)*
4. Excess RA activates RAR/RXR transcriptional programs in target tissues, branching into three principal arms:
   - **4a (skull):** RA **drives** premature osteogenic differentiation of cranial suture mesenchyme via RUNX2↑, alkaline phosphatase↑, and BMPR‑2/pSMAD1/5/9 activation → **coronal craniosynostosis**. *(demonstrated in vitro/animal — PMID 20134361, 30392121; human precedent PMID 22019272)*
   - **4b (axial skeleton):** RA **disrupts** the FGF/WNT‑opposed segmentation wavefront, the segmentation clock, and HOX‑based vertebral identity → **scoliosis and vertebral anomalies**. *(inferred from RA biology — PMID 19651306, 24284210)*
   - **4c (heart & face):** RA perturbs outflow‑tract/septal and craniofacial morphogenesis → **congenital heart disease and facial dysmorphism**. *(demonstrated in mouse; paralleled by isotretinoin embryopathy — PMID 24005908, 29806219, 29308367)*

### Pathway schematic

```
   RDH10 (oxidation) ──►  RETINALDEHYDE  ──►  ALDH1A (RA synthesis)  ──►  RETINOIC ACID
        ▲                     │                                               │
        │ reciprocal          │ DHRS3 reduction (BRAKE)                       │ RAR/RXR
        │ activation          ▼                                               ▼
        └──────────────────  RETINOL                                 target gene programs
                                                                              │
   DHRS3 LOSS  ──► brake removed ──► RA EXCESS ──┬── suture osteogenesis → CRANIOSYNOSTOSIS
                                                 ├── somite/HOX disruption → SCOLIOSIS
                                                 ├── OFT/septation defects → CONGENITAL HEART DISEASE
                                                 └── craniofacial morphogenesis → DYSMORPHISM
   (CYP26B1 degrades RA — its loss phenocopies DHRS3 loss)
```

Upstream node: the DHRS3/RDH10 enzymatic set‑point for RA. Downstream effectors: RUNX2 and BMP–SMAD osteogenic programs; the segmentation clock/HOX axial code; cardiac outflow‑tract morphogenesis.

---

## Section‑by‑Section Report

### 1. Disease Information
- **Overview:** An ultra‑rare, autosomal‑recessive multisystem developmental syndrome characterized by coronal craniosynostosis, scoliosis, congenital heart disease, and facial dysmorphism, caused by biallelic hypomorphic DHRS3 variants that produce embryonic retinoic‑acid excess — effectively a **genetic retinoic acid embryopathy** ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)).
- **Identifiers:** OMIM 621499; MONDO:0980974; causal gene DHRS3 (HGNC:17693). Dedicated Orphanet/ICD‑11/MeSH identifiers were not established at the time of investigation (recently described entity).
- **Synonyms:** None formally recorded; the gene alias **CRSS** matches the syndrome name.
- **Information source:** Derived from aggregated disease‑level resources and a primary multi‑family clinical/genetic study (12 individuals across 8 sibships), not population EHR.

### 2. Etiology
- **Primary cause:** Genetic — biallelic (homozygous) hypomorphic DHRS3 variants, mechanistically mediated by **retinoic‑acid excess** during embryogenesis.
- **Genetic risk factors:** The causal variants themselves (promoter/5′UTR deletion; missense p.Val171Met). As a recessive disorder, **consanguinity** and carrier status in both parents are the key risk context. RDH10 and CYP26 enzymes are mechanistically linked modifiers of RA balance.
- **Environmental risk factors / gene–environment interaction:** Exogenous retinoids (e.g., isotretinoin, high‑dose vitamin A) phenocopy the disorder and would be expected to **exacerbate** RA excess; this is a plausible (though not directly demonstrated) gene–environment interaction. Maternal vitamin A status may modulate severity given DHRS3's role in retinoid homeostasis.
- **Protective factors:** None established. By mechanistic logic, strict avoidance of exogenous retinoids and careful vitamin A balance would be prudent.

### 3. Phenotypes
Core phenotypes and suggested HPO terms (frequencies from the 5 well‑characterized homozygotes, [PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)):

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Coronal craniosynostosis | Physical/structural | Core feature | HP:0004440 (coronal craniosynostosis) |
| Scoliosis | Physical/structural | 5/5 | HP:0002650 |
| Congenital heart disease | Structural | 4/5 | HP:0001627 |
| Dysmorphic facial features | Physical | Core feature | HP:0001999 |
| Elevated retinoic acid / reduced retinol | Laboratory abnormality | Observed in homozygotes | (abnormal circulating vitamin A metabolism) |

- **Onset:** Congenital (prenatal developmental origin).
- **Severity/progression:** Structural anomalies are congenital and largely stable once formed; craniosynostosis and scoliosis are progressive in their secondary consequences (skull growth restriction, spinal curve progression) without intervention.
- **Quality‑of‑life impact:** Dominated by craniofacial surgery burden, potential raised intracranial pressure, cardiac morbidity, and orthopedic/spinal sequelae. Disease‑specific QOL instruments have not been reported for this new entity.

### 4. Genetic / Molecular Information
- **Causal gene:** DHRS3 / SDR16C1 (HGNC:17693; NCBI Gene 9249; Ensembl ENSG00000162496; UniProt O75911; chromosome **1p36.21**).
- **Pathogenic variants:** A regulatory **promoter/5′UTR deletion** (reducing transcription 90–98%) and a **missense p.(Val171Met)**; 5 homozygous variants total across the cohort. Functional assays confirmed the missense allele reduces retinaldehyde‑reduction capacity ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)). DHRS3 has 117 ClinVar entries.
- **Classification / type:** Hypomorphic loss‑of‑function; variant types include regulatory deletion and missense.
- **Origin & consequence:** Germline; **loss of function** (hypomorphic, not complete null in survivors).
- **Population frequency / constraint:** gnomAD shows DHRS3 is LoF‑tolerant in heterozygotes (pLI 0.014; LOEUF 0.81), consistent with recessive disease.
- **Modifier genes:** RDH10 (obligate activating partner), CYP26A1/B1 (RA degradation, compensatory), ALDH1A enzymes (RA synthesis) are mechanistic modifiers of RA level.
- **Epigenetic / chromosomal:** No disease‑specific epigenetic signature or recurrent chromosomal abnormality reported.

### 5. Environmental Information
- **Environmental factors:** Exogenous retinoids (isotretinoin, excess vitamin A) are teratogens that produce an overlapping embryopathy and are the principal relevant non‑genetic exposure.
- **Lifestyle factors:** Maternal vitamin A intake during pregnancy is mechanistically relevant.
- **Infectious agents:** Not applicable.

### 6. Mechanism / Pathophysiology
Presented as the causal chain above. In brief: DHRS3 loss → failure of retinaldehyde→retinol reduction → **RA excess** → RAR/RXR‑driven premature suture osteogenesis (RUNX2, BMP‑SMAD1/5/9), disrupted somite/HOX axial patterning, and cardiac/craniofacial dysmorphogenesis.
- **Molecular pathways:** Retinoic acid signaling (RAR/RXR); BMP‑SMAD; intersecting FGF/WNT segmentation gradients.
- **Cellular processes:** Osteogenic differentiation of cranial suture mesenchyme; reduced progenitor proliferation; somite segmentation.
- **Protein dysfunction:** Reduced catalytic reductase activity of DHRS3 (hypomorphic LoF); normal protein is a membrane SDR‑family enzyme.
- **Suggested GO/CL terms:** GO:0042572 (retinol metabolic process), GO:0001501 (skeletal system development), GO:0048705 (skeletal system morphogenesis), GO:0030509 (BMP signaling pathway), GO:0001756 (somitogenesis); CL:0000062 (osteoblast), CL:0000134 (mesenchymal stem cell), CL:0000222 (mesodermal cell). CHEBI: retinoic acid (CHEBI:26536), retinol (CHEBI:17336), retinaldehyde (CHEBI:17898).

### 7. Anatomical Structures Affected
- **Organ/system level:** Skull (calvaria, coronal suture; UBERON:0004768 cranial suture), vertebral column/spine (UBERON:0001130), heart (UBERON:0000948; outflow tract and septa), craniofacial skeleton (UBERON:0010323). Body systems: skeletal, cardiovascular, craniofacial.
- **Tissue/cell level:** Cranial suture mesenchyme / mesenchymal stem cells, osteoblasts, paraxial mesoderm/somite cells.
- **Subcellular level:** DHRS3 is membrane‑associated (endoplasmic reticulum/membrane; GO:0005783, GO:0016020), where retinoid metabolism occurs.
- **Lateralization:** Coronal synostosis may be unilateral or bilateral; scoliosis is by definition asymmetric.

### 8. Temporal Development
- **Onset:** Congenital; the pathogenic events occur during embryogenesis (RA‑sensitive windows of cranial suture, somite, and cardiac development).
- **Progression:** Structural defects are fixed at birth but have progressive secondary consequences (skull growth restriction → raised intracranial pressure; spinal curve progression with growth).
- **Critical periods:** Early embryonic organogenesis for RA‑dependent patterning; postnatal suture patency windows for surgical timing.

### 9. Inheritance and Population
- **Inheritance:** Autosomal recessive; biallelic hypomorphic variants required.
- **Penetrance/expressivity:** Congruent core phenotype across the five characterized homozygotes suggests reasonably consistent expressivity; cohort size is too small to quantify penetrance precisely.
- **Consanguinity/founder effects:** Recessive inheritance with homozygous variants across sibships implies a role for consanguinity; specific founder effects not established.
- **Epidemiology:** Ultra‑rare; prevalence/incidence not yet estimable (first described 2025, 12 individuals). Sex ratio and geographic distribution not established.

### 10. Diagnostics
- **Genetic testing (primary):** Molecular diagnosis by **exome or genome sequencing** identifying biallelic DHRS3 variants; targeted single‑gene or panel testing where DHRS3 is included. Because the disease involves **regulatory (promoter/5′UTR) variants** that exome‑only approaches may miss, WGS adds diagnostic value.
- **Biochemical biomarker:** **Plasma retinoid profile** (elevated all‑trans‑retinoic acid, reduced retinol) is a candidate functional biomarker supporting pathogenicity ([PMID: 40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/)).
- **Imaging:** CT of the skull (suture fusion), spinal radiography (scoliosis), echocardiography (congenital heart disease).
- **Differential diagnosis:** Syndromic craniosynostoses (FGFR‑related: Apert, Crouzon, Pfeiffer; TWIST1 Saethre‑Chotzen), **CYP26B1‑related** craniosynostosis/skeletal anomaly syndrome, and **retinoic acid/isotretinoin embryopathy** (teratogenic phenocopy — distinguished by maternal exposure history and absence of biallelic DHRS3 variants).

### 11. Outcome / Prognosis
- Prognosis is determined by severity of craniosynostosis (risk of raised intracranial pressure), congenital heart disease, and scoliosis. No survival/mortality statistics exist for this newly described human syndrome. In the **mouse null** model the phenotype is embryonic‑lethal, but surviving human homozygotes carry hypomorphic (not null) alleles, consistent with viable but multisystem disease.
- **Complications:** Raised intracranial pressure, neurocognitive sequelae secondary to skull constraint, cardiac morbidity, progressive spinal deformity.

### 12. Treatment
- **No disease‑specific therapy exists.** Management is symptomatic and multidisciplinary:
  - **Surgical (craniosynostosis):** Cranial vault remodeling / fronto‑orbital advancement; endoscopic suture release with helmet therapy; spring‑assisted cranioplasty (NCIT: craniofacial surgery / cranioplasty). Craniosynostosis surgical series support good outcomes with both open and minimally invasive approaches.
  - **Cardiac:** Surgical repair of congenital heart defects as indicated.
  - **Spinal:** Orthopedic management of scoliosis (bracing/surgery).
  - **Supportive/rehabilitative:** Developmental support and multidisciplinary follow‑up.
- **Mechanism‑based speculation (not clinically validated):** Because the disease reflects RA excess, modulation of RA signaling is a conceptual target; however, no such therapy has been tested, and the prenatal developmental timing limits feasibility.

### 13. Prevention
- **Primary prevention:** Genetic counseling for at‑risk (especially consanguineous) families; carrier testing and reproductive options (prenatal diagnosis, preimplantation genetic testing) once familial variants are known.
- **Avoidance of exogenous retinoids** in pregnancy is universally recommended and mechanistically pertinent.
- **Secondary prevention:** Early imaging surveillance of sutures, spine, and heart in known biallelic carriers to enable timely surgical intervention.

### 14. Other Species / Natural Disease
- **Orthologs:** Mouse *Dhrs3* (Gene 20148; MGI:1315215); zebrafish *dhrs3a* (Gene 445083; ZFIN ZDB‑GENE‑040801‑217) and *dhrs3b*. Human DHRS3 is well conserved across vertebrates.
- **Natural disease in animals:** No naturally occurring DHRS3 disease analog is recorded in companion/wildlife species (no dedicated OMIA entry at investigation time); relevant data come from engineered models.
- **Comparative biology:** The RA‑homeostasis mechanism is evolutionarily conserved; zebrafish *cyp26b1* loss produces craniosynostosis and skeletal fusions ([PMID: 22019272](https://pubmed.ncbi.nlm.nih.gov/22019272/)), reinforcing cross‑species conservation of RA‑excess skeletal pathology.

### 15. Model Organisms
- **Principal model:** *Dhrs3*‑null mouse — recapitulates RA‑excess biochemistry (~40% increased ATRA) and cardiac outflow‑tract/septal, skeletal, and palatal malformations with late‑gestation lethality ([PMID: 24005908](https://pubmed.ncbi.nlm.nih.gov/24005908/)); also used to model aberrant coronary vasculature ([PMID: 29806219](https://pubmed.ncbi.nlm.nih.gov/29806219/)).
- **Phenotype recapitulation:** Strong for the biochemical mechanism and cardiac/skeletal/craniofacial anomalies; **limitation** is embryonic lethality of the complete null, which does not model viable hypomorphic human disease — a hypomorphic/conditional allele would better mirror patients.
- **Other systems:** Zebrafish (*dhrs3a/b*; and *cyp26b1* for the RA‑excess skeletal phenotype), plus in vitro cranial suture mesenchymal cell cultures and human somitogenesis/axioloid models for RA‑dependent segmentation.
- **Resources:** MGI (mouse), ZFIN (zebrafish).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [40519748](https://pubmed.ncbi.nlm.nih.gov/40519748/) | *Identification and characterization of DHRS3 deficiency, a retinoic acid embryopathy of humans* | **Defining clinical/genetic study**; establishes disease, variants, biomarker, inheritance |
| [24733397](https://pubmed.ncbi.nlm.nih.gov/24733397/) | *Retinaldehyde reductase activity of DHRS3 reciprocally activated by RDH10* | Enzymatic mechanism and RDH10 dependence |
| [24005908](https://pubmed.ncbi.nlm.nih.gov/24005908/) | *DHRS3 essential for preventing excess RA during development* | Mouse null; 40% ATRA increase; cardiac/skeletal/palatal defects |
| [39420244](https://pubmed.ncbi.nlm.nih.gov/39420244/) | *Feedback regulation of retinaldehyde reductase DHRS3* | RAR/RXR negative‑feedback loop for RA homeostasis |
| [20134361](https://pubmed.ncbi.nlm.nih.gov/20134361/) | *RA enhances osteogenesis in cranial suture mesenchymal cells* | RA→RUNX2/ALP→premature osteogenesis (craniosynostosis) |
| [30392121](https://pubmed.ncbi.nlm.nih.gov/30392121/) | *Noggin blocks RA‑induced suture fusion* | BMP‑SMAD1/5/9 downstream of RA; rescuable by Noggin |
| [22019272](https://pubmed.ncbi.nlm.nih.gov/22019272/) | *Craniosynostosis from defective localized RA degradation (CYP26B1)* | Human precedent: genetic RA excess → craniosynostosis/skeletal fusions |
| [19651306](https://pubmed.ncbi.nlm.nih.gov/19651306/) | *Hox vertebral identities in spine precursors* | RA in segmentation wavefront → axial/vertebral patterning (scoliosis) |
| [24284210](https://pubmed.ncbi.nlm.nih.gov/24284210/) | *RA controls head‑to‑trunk linkage in zebrafish* | RA dysregulation alters somite number/vertebral patterning |
| [37086723](https://pubmed.ncbi.nlm.nih.gov/37086723/) | *De novo variants in syndromic craniosynostosis* | Independent implication of RA signaling in syndromic craniosynostosis |
| [30976277](https://pubmed.ncbi.nlm.nih.gov/30976277/) | *Structural genome variations in craniosynostosis* | RA within the craniosynostosis gene network |
| [29806219](https://pubmed.ncbi.nlm.nih.gov/29806219/) | *Altered RA signaling and mouse coronary vasculature* | DHRS3‑deficient model; cardiac/coronary consequences |
| [29308367](https://pubmed.ncbi.nlm.nih.gov/29308367/) / [34773723](https://pubmed.ncbi.nlm.nih.gov/34773723/) | *Retinoic acid embryopathy case reports* | Teratogenic phenocopy: craniofacial/cardiac/CNS/skeletal spectrum |

**Evidence source types:** human clinical (40519748, 22019272, 29308367, 34773723), model organism (24005908, 29806219, 24284210), in vitro/cellular (20134361, 30392121, 24733397), and genomic/network (37086723, 30976277).

---

## Limitations and Knowledge Gaps

- **Small cohort:** The disease is defined by 12 individuals (8 sibships), with 5 deeply characterized homozygotes. Penetrance, full phenotypic spectrum, prevalence, sex ratio, and natural history are not yet quantifiable.
- **Scoliosis mechanism is inferred:** The link from RA excess to scoliosis rests on well‑established RA/somitogenesis biology ([PMID: 19651306](https://pubmed.ncbi.nlm.nih.gov/19651306/), [PMID: 24284210](https://pubmed.ncbi.nlm.nih.gov/24284210/)) rather than direct demonstration in DHRS3 patients.
- **Model mismatch:** The complete *Dhrs3*‑null mouse is embryonic‑lethal, whereas human disease is caused by viable hypomorphic alleles — a hypomorphic/conditional model is needed to fully mirror the human condition.
- **No therapy and limited diagnostics:** No disease‑specific treatment exists; the plasma‑retinoid biomarker needs validation as a diagnostic/prognostic tool in a larger cohort.
- **Ontology/identifier gaps:** Orphanet, ICD, and MeSH entries are not yet established for this recently described entity.

## Proposed Follow‑up Experiments / Actions

1. **Expand the patient cohort** via GeneMatcher/MatchMaker Exchange to refine the phenotype, penetrance, and variant spectrum; specifically assess the frequency and nature of regulatory (promoter/5′UTR) alleles, which argue for genome over exome sequencing.
2. **Generate a hypomorphic/conditional *Dhrs3* mouse** (or zebrafish *dhrs3a/b* model) to capture viable craniosynostosis and scoliosis phenotypes and to map RA‑sensitive developmental windows.
3. **Validate the plasma‑retinoid biomarker** (RA↑, retinol↓) prospectively for diagnostic and functional‑variant‑classification utility.
4. **Functionally characterize additional DHRS3 variants** (reductase assays, RDH10 co‑expression) to build an evidence base for ACMG classification.
5. **Test mechanism‑based modulation of RA/BMP signaling** (e.g., Noggin‑type BMP antagonism, RA‑pathway modulators) in suture organoid and animal models, informed by the Noggin‑rescue result ([PMID: 30392121](https://pubmed.ncbi.nlm.nih.gov/30392121/)).
6. **Establish ontology/registry entries** (Orphanet, ICD‑11, MeSH) and a natural‑history registry to support epidemiology and outcomes research.

---

*Report compiled from a five‑iteration autonomous investigation; 7 findings confirmed across 29 reviewed papers. All mechanistic and clinical claims are anchored to the cited primary literature.*


## Artifacts

- [OpenScientist final report](Craniosynostosis-scoliosis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniosynostosis-scoliosis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001999` (1 mention) - the report calls it "Core feature"; HP calls it **Abnormal facial shape**, and lists "Dysmorphic facial features" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

22 of 24 terms resolved to a current term; the rest could not be looked up either way.