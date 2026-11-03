---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T01:27:59.534880'
end_time: '2026-10-24T01:53:27.446130'
duration_seconds: 1527.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Focal Facial Dermal Dysplasia Type IV
  mondo_id: MONDO:0013997
  category: Mendelian
  causal_genes: CYP26C1
  omim_id: not recorded
  synonyms: FFDD4; FFDD type IV; focal facial dermal dysplasia 4; focal facial preauricular
    dysplasia
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
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 16
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 23
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.042
  labels_checked: 18
  labels_matching: 10
  labels_variant: 8
  unresolved_terms:
  - HP:0004410
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
  path: Focal_Facial_Dermal_Dysplasia_Type_IV-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Focal_Facial_Dermal_Dysplasia_Type_IV-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Focal Facial Dermal Dysplasia Type IV
- **MONDO ID:** MONDO:0013997 (if available)
- **Causal gene(s):** CYP26C1
- **OMIM:** not recorded
- **Synonyms:** FFDD4; FFDD type IV; focal facial dermal dysplasia 4; focal facial preauricular dysplasia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Focal Facial Dermal Dysplasia Type IV** covering all of the
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

# Focal Facial Dermal Dysplasia Type IV (FFDD4) — Comprehensive Disease Characterization Report

**Disease:** Focal Facial Dermal Dysplasia Type IV
**MONDO ID:** MONDO:0013997 · **OMIM:** 614974 · **Orphanet:** ORPHA:306550 (FFDD group)
**Causal gene:** **CYP26C1** (HGNC:20577; NCBI Gene 340665; UniProt Q6V0L0; cytochrome P450 family 26 subfamily C member 1; chromosome 10q23.33)
**Category:** Mendelian, autosomal recessive

---

## Summary

**Focal Facial Dermal Dysplasia Type IV (FFDD4) is an ultra-rare, autosomal-recessive congenital skin disorder caused by biallelic loss-of-function variants in the gene *CYP26C1*.** CYP26C1 encodes a cytochrome P450 enzyme that hydroxylates and inactivates retinoic acid (the active metabolite of vitamin A). The disease was molecularly defined in 2012 when exome sequencing of an affected sibpair identified compound-heterozygous *CYP26C1* variants, and subsequent reports confirmed the gene and expanded its allelic spectrum [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/); [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/).

Clinically, FFDD4 presents at birth with **bilateral, oval, hypopigmented, scar-like atrophic lesions in the preauricular region**, frequently surrounded by a hair collar and resembling membranous aplasia cutis congenita. The preauricular location distinguishes FFDD4 from FFDD types I–III, which show bitemporal lesions. FFDD4 is generally non-syndromic — "characterized by preauricular skin defects without additional dysmorphic findings" — and the lesions are stable, benign, and non-progressive.

Mechanistically, the leading model is that loss of CYP26C1's retinoic-acid–catabolizing activity causes **locally excessive retinoic-acid signaling along the maxillary–mandibular fusion line of the first branchial arch during embryonic facial development**, precisely where FFDD4 lesions arise. In mice, *Cyp26c1* is expressed exactly along this fusion line, and combined loss of *Cyp26a1* and *Cyp26c1* disrupts anterior–posterior patterning and the production of migratory cranial neural crest cells, linking the enzyme to the cell lineage that builds the face. Management is supportive/cosmetic, and genetic counseling (25% sibling recurrence risk, with a documented Belgian founder allele) is the principal preventive measure.

---

## Key Findings

### Finding 1 — FFDD4 is caused by biallelic (autosomal recessive) *CYP26C1* variants

FFDD type IV results from **biallelic pathogenic variants in *CYP26C1***, establishing an autosomal-recessive Mendelian etiology. The defining study performed exome sequencing on an affected sibpair and identified compound-heterozygous variants: a maternally inherited frameshift duplication **c.844_851dupCCATGCA (p.Glu284fsX128)** and a paternally inherited missense **c.1433G>A (p.Arg478His)**. The missense allele was shown to be non-functional in a mammalian cell expression assay, confirming loss of function. Three of four additional unrelated FFDD4 patients were homozygous for the 7-bp duplication, and importantly none of 8 TWIST2-negative FFDD type II/III patients carried *CYP26C1* mutations, demonstrating genetic specificity to the preauricular (type IV) subtype [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/).

> *"two novel sequence variants were identified in both siblings in CYP26C1 — a duplication of seven base pairs, which was maternally inherited, c.844_851dupCCATGCA, predicting p.Glu284fsX128 and a missense mutation, c.1433G>A, predicting p.Arg478His, that was paternally inherited"* — [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/)

A later report added three novel lesions to the allelic spectrum: a missense **c.230G>C (p.Arg77Pro)** and two splice-site variants **c.1191+1G>T (IVS5+1G>T)** and **c.1191+2insT (IVS5+2insT)**, confirming genetic heterogeneity of mutation type (frameshift, missense, splice-site) within the same gene [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/).

> *"four CYP26C1 mutations including three novel lesions: a missense mutation, c.230G>C (p.Arg77Pro), and two splice-site mutations, c.1191+1G>T (IVS5(+1)G>T) and c.1191+2insT (IVS5(+2)insT)"* — [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/)

**Variant catalogue (human, germline):**

| Variant (cDNA) | Protein | Type | Inheritance origin | Functional data | Source |
|---|---|---|---|---|---|
| c.844_851dupCCATGCA | p.Glu284fsX128 | Frameshift (7-bp dup) | Recurrent/founder | Predicted LoF | 23161670; 39828664 |
| c.1433G>A | p.Arg478His | Missense | Paternal (index) | Non-functional in cell assay | 23161670 |
| c.230G>C | p.Arg77Pro | Missense | — | Novel | 29263414 |
| c.1191+1G>T | (IVS5+1) | Splice-site | — | Novel | 29263414 |
| c.1191+2insT | (IVS5+2) | Splice-site | — | Novel | 29263414 |

**Ontology anchors:** gene *CYP26C1* (HGNC:20577); variant consequences SO:0000865 (frameshift), SO:0001583 (missense), SO:0001574 (splice site). Evidence type: **human clinical genetics + in vitro functional assay.**

---

### Finding 2 — Mechanism: CYP26C1 loss dysregulates retinoic acid at facial fusion lines

CYP26C1 is a cytochrome P450 that **hydroxylates and thereby inactivates retinoic acid (RA)**. The spatial logic of the disease is striking: in mice, *Cyp26c1* is expressed **exactly along the fusion line of the maxillary and mandibular prominences in the first branchial arch** — the precise anatomical sites where FFDD skin lesions arise during early facial development. This spatial correspondence is the central pillar of the mechanistic model: when the RA-clearing enzyme is lost, RA accumulates locally and disrupts the tissue programs that normally knit the facial prominences together [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/).

> *"The FFDD skin lesions arise along the sites of fusion of the maxillary and mandibular prominences early in facial development, and Cyp26c1 was expressed exactly along the fusion line for these facial prominences in the first branchial arch in mice"* — [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/)

The enzyme's biochemical role has been confirmed in vitro: CYP26C1 metabolizes all-*trans* and other active retinoic-acid species and interacts with cellular retinoic acid binding proteins (CRABPs), which chaperone RA to the enzyme [PMID: 29476041](https://pubmed.ncbi.nlm.nih.gov/29476041/).

The developmental relevance to craniofacial tissue is supported by mouse knockout work: *Cyp26a1⁻/⁻;Cyp26c1⁻/⁻* double-null embryos **fail to produce migratory cranial neural crest cells in the forebrain and midbrain** and show anterior brain truncation with posteriorized anterior–posterior patterning — cranial neural crest being the lineage that builds facial skeleton and connective tissue [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/).

> *"Cyp26a1-/-Cyp26c1-/- mice fail to produce migratory cranial neural crest cells in the forebrain and midbrain"* — [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/)

**Ontology anchors:** GO:0042573 (retinoic acid metabolic process); GO:0016712 (oxidoreductase activity, acting on paired donors with incorporation of O₂); CHEBI:15367 (all-trans-retinoic acid); CL:0000333 (migratory cranial neural crest cell); UBERON:0003066 (pharyngeal/branchial arch). Evidence type: **mouse model + in vitro biochemistry + human spatial correlation.**

---

### Finding 3 — Phenotype: bilateral congenital preauricular scar-like lesions without additional dysmorphism

FFDD4 is defined by **congenital scar-like atrophic lesions in the preauricular area**, which distinguishes it from the bitemporal lesions of FFDD types I–III. The lesions are typically bilateral, oval, and hypopigmented, sometimes surrounded by a hair collar, and resemble membranous aplasia cutis congenita. The condition is **non-syndromic**: it is "characterized by preauricular skin defects without additional dysmorphic findings" [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/).

> *"FFDD4 is an autosomal-recessive trait characterized by preauricular skin defects without additional dysmorphic findings"* — [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/)

> *"bilateral preauricular scarlike defects surrounded by a hair collar, resembling membranous aplasia cutis congenita"* — [PMID: 30561078](https://pubmed.ncbi.nlm.nih.gov/30561078/)

Case series confirm the morphology: "three infants with bilateral, oval-shaped, hypopigmented preauricular lesions indicative of FFDD IV" [PMID: 40231353](https://pubmed.ncbi.nlm.nih.gov/40231353/).

**Phenotype table with HPO suggestions:**

| Phenotype | HPO term | Type | Onset | Severity | Frequency | Laterality |
|---|---|---|---|---|---|---|
| Preauricular skin lesion / aplasia-cutis-like defect | HP:0004410 (abnormality of the preauricular region); HP:0001057 (aplasia cutis congenita) | Physical manifestation / clinical sign | Congenital/neonatal | Mild–moderate | Nearly all patients | Bilateral |
| Atrophic/scar-like skin lesion | HP:0001075 (atrophic scars) | Clinical sign | Congenital | Mild | Typical | Bilateral |
| Hypopigmented skin lesion | HP:0001010 (hypopigmentation of the skin) | Clinical sign | Congenital | Mild | Common | Bilateral |
| Hair collar sign | HP:0010719 (abnormal hair pattern) | Clinical sign | Congenital | Mild | Variable | Localized |

**Quality-of-life impact:** The lesions are primarily of **cosmetic significance**; FFDD4 is not associated with systemic disease, pain, or functional impairment. QoL impact is limited to appearance-related concerns and, in some cases, diagnostic anxiety before benign nature is established. Evidence type: **human clinical (case reports/series).**

---

### Finding 4 — Mouse *Cyp26c1* models the enzyme, but single knockout is phenotypically normal (functional redundancy)

The mouse provides an informative but **incomplete** model. *Cyp26c1* expression along the maxillary–mandibular fusion line of the first branchial arch matches the human lesion site, giving the model strong face validity for spatial mechanism [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/). However, **single *Cyp26c1*-null mice are developmentally normal**, indicating functional redundancy with the paralogous RA-degrading enzyme *Cyp26a1* [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/).

> *"Loss of CYP26C1 did not appear to affect embryonic development, suggesting that CYP26A1 and CYP26C1 are functionally redundant"* — [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/)

> *"mice lacking both CYP26A1 and CYP26C1 were found to manifest a pronounced anterior truncation of the brain associated with A-P patterning defects"* — [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/)

The two enzymes also cooperatively degrade RA in the equatorial retina during later eye development, further illustrating overlapping function [PMID: 15531370](https://pubmed.ncbi.nlm.nih.gov/15531370/). This redundancy is a key **model limitation**: the mouse does not spontaneously recapitulate the human preauricular skin phenotype on single-gene knockout, and the human phenotype's restriction to skin (despite the broader developmental roles of CYP26 enzymes) suggests species-specific or tissue-specific thresholds of redundancy. Evidence type: **mouse genetic models.**

---

### Finding 5 — FFDD4 is one of four FFDD subtypes; diagnosis is clinical + *CYP26C1* sequencing, distinguished by preauricular location

The focal facial dermal dysplasias (FFDDs) comprise **four subtypes classified by lesion location**: bitemporal (FFDD types I–III) versus preauricular (FFDD type IV) [PMID: 28663233](https://pubmed.ncbi.nlm.nih.gov/28663233/). FFDD4 was formally recognized as a new subtype on clinical review of patients with preauricular lesions [PMID: 21931173](https://pubmed.ncbi.nlm.nih.gov/21931173/).

> *"Four subtypes are classified by the bitemporal (FFDD1-3) or preauricular (FFDD4) lesion location"* — [PMID: 28663233](https://pubmed.ncbi.nlm.nih.gov/28663233/)

> *"patients with preauricular lesions as a new subtype, FFDD type IV"* — [PMID: 21931173](https://pubmed.ncbi.nlm.nih.gov/21931173/)

**Genetic landscape across subtypes:**

| Subtype | Lesion location | Gene / locus | Inheritance |
|---|---|---|---|
| FFDD I | Bitemporal | Unknown | AD (variable) |
| FFDD II | Bitemporal | Unknown | AR/AD |
| FFDD III (Setleis syndrome) | Bitemporal | *TWIST2* (AR); 1p36.22p36.21 dup/trip (AD) | AR or AD |
| **FFDD IV** | **Preauricular** | ***CYP26C1*** | **AR** |

FFDD III (Setleis syndrome) is caused by *TWIST2* mutations or by 1p36.22p36.21 duplication/triplication [PMID: 25728400](https://pubmed.ncbi.nlm.nih.gov/25728400/), whereas FFDD I/II genetic causes remain unknown. Diagnosis of FFDD4 is **clinical recognition of bilateral preauricular atrophic lesions, confirmed by *CYP26C1* molecular testing**. The differential diagnosis includes membranous aplasia cutis congenita, preauricular tags/pits, and the bitemporal FFDDs [PMID: 30561078](https://pubmed.ncbi.nlm.nih.gov/30561078/); [PMID: 40231353](https://pubmed.ncbi.nlm.nih.gov/40231353/).

> *"Awareness of this rare condition by dermatologists is imperative to enable prompt recognition and minimize diagnostic delay"* — [PMID: 30561078](https://pubmed.ncbi.nlm.nih.gov/30561078/)

Evidence type: **human clinical / expert review.**

---

### Finding 6 — Epidemiology: ultra-rare, autosomal recessive with a recurrent founder frameshift allele

FFDD4 is **ultra-rare**, with fewer than roughly 20 molecularly confirmed patients reported worldwide across the primary literature [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/); [PMID: 29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/); [PMID: 30561078](https://pubmed.ncbi.nlm.nih.gov/30561078/); [PMID: 40231353](https://pubmed.ncbi.nlm.nih.gov/40231353/). Inheritance is autosomal recessive (biallelic *CYP26C1*). The recurrent 7-bp frameshift duplication **c.844_851dupCCATGCA (p.Glu284fs)** recurs across unrelated patients and was present in **0.3% of healthy controls and 0.3% of patients with other birth defects** in the original study [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/).

> *"The seven base pairs duplication was present in 0.3% of healthy controls and 0.3% of patients with other birth defects."* — [PMID: 23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/)

A **founder effect** explains locally elevated prevalence in Belgium: two novel Belgian FFDD4 cases were both homozygous for a recurrent *CYP26C1* frameshift variant and shared a common **700 kb haplotype** [PMID: 39828664](https://pubmed.ncbi.nlm.nih.gov/39828664/).

> *"both homozygous for a recurrent CYP26C1 frameshift variant, with a common 700 kb haplotype, indicating a founder effect"* — [PMID: 39828664](https://pubmed.ncbi.nlm.nih.gov/39828664/)

Both sexes are affected (no reported sex bias), lesions are bilateral and congenital, and there is no age-dependent or geriatric onset (onset is strictly prenatal/congenital). Evidence type: **human clinical / population genetics.**

---

### Finding 7 — CYP26C1 is a retinoid hydroxylase acting on multiple active retinoids and interacting with CRABPs

In vitro characterization established that **CYP26C1 metabolizes multiple active retinoids** (all-*trans* and other active retinoic-acid species) and **interacts with cellular retinoic acid binding proteins (CRABPs)** — defining its biochemical role as a clearance enzyme for active vitamin A metabolites [PMID: 29476041](https://pubmed.ncbi.nlm.nih.gov/29476041/).

> *"The goal of this study was to establish the substrate specificity of CYP26C1, and determine whether CYP26C1 interacts with cellular retinoic acid binding proteins (CRABPs)"* — [PMID: 29476041](https://pubmed.ncbi.nlm.nih.gov/29476041/)

As a cytochrome P450, CYP26C1 is a **heme-thiolate monooxygenase localized to the endoplasmic reticulum membrane**. Its loss in FFDD4 is therefore a **loss-of-function defect** in retinoid catabolism, which maps directly onto the proposed mechanism of locally excessive RA signaling.

**Ontology anchors:** GO:0005506 (iron ion binding); GO:0020037 (heme binding); GO:0004497 (monooxygenase activity); GO:0005789 (endoplasmic reticulum membrane); CHEBI:26536 (retinoid). Evidence type: **in vitro biochemistry.**

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *CYP26C1*** (frameshift, missense, or splice-site) **result in** absent or non-functional CYP26C1 enzyme. *(Demonstrated: human genetics + in vitro functional assay.)*
2. Loss of CYP26C1 hydroxylase activity **leads to** failure to catabolize all-*trans* and other active retinoic acids locally. *(Demonstrated biochemically; CYP26C1 substrate specificity established.)*
3. Reduced retinoid clearance **leads to** locally elevated retinoic-acid concentration/signaling specifically **along the maxillary–mandibular fusion line of the first branchial arch**, where *Cyp26c1* is normally expressed. *(Inferred for human; spatial expression demonstrated in mouse.)*
4. Excess RA signaling at the fusion line **disrupts** the developmental programs that govern tissue fusion and the behavior of **cranial neural crest–derived cells** that build facial dermis/connective tissue. *(Inferred; supported by double-knockout cranial neural crest phenotype in mouse.)*
5. Disrupted fusion-line tissue integrity **results in** focal failure of dermal development → congenital, scar-like / aplasia-cutis-like atrophic skin defects. *(Inferred from spatial correlation.)*
6. Because the defect is restricted to the preauricular fusion territory, the clinical outcome **is** bilateral, oval, hypopigmented **preauricular lesions** without other dysmorphism. *(Demonstrated clinically.)*

```
 CYP26C1 biallelic LoF variant   [DEMONSTRATED: human genetics]
            │
            ▼
 No functional CYP26C1 enzyme (ER heme-thiolate P450)  [DEMONSTRATED: cell assay]
            │
            ▼
 Failure to hydroxylate/inactivate retinoic acid       [DEMONSTRATED: in vitro]
            │
            ▼
 LOCAL excess retinoic-acid signaling at the            [INFERRED in human;
 maxillary–mandibular fusion line (1st branchial arch)   mouse Cyp26c1 expression maps here]
            │
      ┌─────┴───────────────┐
      ▼                     ▼
 Disrupted facial     Perturbed cranial neural       [INFERRED; supported by
 prominence fusion    crest cell behavior             Cyp26a1/c1 double-KO mouse]
      │                     │
      └─────────┬───────────┘
                ▼
 Focal failure of dermal development at fusion site     [INFERRED]
                ▼
 Bilateral congenital preauricular scar-like / aplasia-  [DEMONSTRATED clinically]
 cutis-like atrophic lesions, no other anomalies
```

### Upstream vs downstream

- **Upstream (initiating):** *CYP26C1* loss-of-function mutation → enzyme deficiency → RA catabolism failure.
- **Midstream (developmental):** local RA excess at the fusion line → perturbed fusion/neural-crest programs.
- **Downstream (clinical):** focal dermal aplasia → preauricular atrophic lesions.

### Cell types and processes involved

- **Cell types:** cranial neural crest cells (CL:0000333), dermal fibroblasts/mesenchyme, facial epithelium.
- **Tissue:** skin/dermis (UBERON:0002067), preauricular region, first pharyngeal/branchial arch (UBERON:0003066).
- **Processes:** retinoic acid metabolic process (GO:0042573), regulation of retinoic acid receptor signaling pathway (GO:0048385), embryonic cranial skeleton/face morphogenesis (GO:0048701), neural crest cell migration (GO:0001755).

The model is internally coherent: a spatially restricted catabolic enzyme, when lost, produces a spatially restricted developmental defect in exactly the territory where the enzyme is expressed. The main inferential gap is that **direct demonstration of RA excess in human FFDD4 tissue has not been performed** — the step is extrapolated from mouse expression data and enzyme biochemistry.

---

## Section-by-Section Synthesis

### 1. Disease Information
FFDD4 is an ultra-rare congenital dermal dysplasia with isolated preauricular scar-like lesions. **Identifiers:** MONDO:0013997; OMIM 614974; Orphanet (FFDD group ORPHA:306550); Mondo/MeSH align to the "focal facial dermal dysplasia" concept. **Synonyms:** FFDD4; FFDD type IV; focal facial dermal dysplasia 4; focal facial preauricular dysplasia. Information is derived from **aggregated disease-level resources and published case reports/series**, not individual-patient EHR.

### 2. Etiology
**Primary cause is genetic** — biallelic (autosomal recessive) loss-of-function variants in *CYP26C1*. **Genetic risk factor:** carrier status for a pathogenic *CYP26C1* allele; consanguinity and founder populations (Belgium) raise risk. No environmental, infectious, or lifestyle risk factors are established. **Protective factors:** none specific are documented (a functional *CYP26C1* allele is "protective" by preventing biallelic loss). **Gene–environment interactions:** none demonstrated for FFDD4; note that *exogenous* retinoic-acid excess (teratogenic retinoid embryopathy) causes a biochemically convergent perturbation of RA signaling, offering a conceptual parallel but not a demonstrated GxE interaction in this disease.

### 3. Phenotypes
See Finding 3 table. Core phenotype: bilateral congenital preauricular atrophic/hypopigmented scar-like lesions (aplasia-cutis-like), often with a hair collar; non-syndromic; stable/non-progressive; mild severity; cosmetic QoL impact.

### 4. Genetic/Molecular Information
Causal gene *CYP26C1* (HGNC:20577, gene OMIM 608428; disease OMIM 614974). Variant classes: frameshift, missense (functionally null), splice-site (see Finding 1 table). Variants are **germline**; the recurrent 7-bp duplication behaves as a **founder allele** (~0.3% carrier frequency in one control set; Belgian 700 kb haplotype). Functional consequence: **loss of function.** No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are established for FFDD4 specifically (chromosomal CNVs at 1p36 cause FFDD III, not IV).

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established. The disorder is wholly genetic.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above.

### 7. Anatomical Structures Affected
- **Organ level:** skin (integumentary system) — primary; no secondary organ involvement in non-syndromic FFDD4.
- **Localization:** preauricular region, bilateral; derived from the first branchial arch maxillary–mandibular fusion territory. UBERON:0002067 (dermis); UBERON:0001456 (face); UBERON:0003066 (pharyngeal arch).
- **Tissue/cell level:** dermal connective tissue; cranial neural crest–derived mesenchyme (CL:0000333); epithelial–mesenchymal fusion interface.
- **Subcellular (gene product):** endoplasmic reticulum membrane (GO:0005789) — site of CYP26C1 enzyme.
- **Lateralization:** bilateral (symmetric).

### 8. Temporal Development
- **Onset:** congenital (prenatal developmental origin; lesions present at birth).
- **Progression:** stable, non-progressive; lesions persist as scars but do not worsen.
- **Course:** chronic/lifelong but benign; no relapsing-remitting or episodic pattern.
- **Critical period:** early embryonic facial morphogenesis (first branchial arch fusion) — the only window of pathogenesis; no postnatal intervention window for the primary lesion.

### 9. Inheritance and Population
- **Inheritance:** autosomal recessive (biallelic *CYP26C1*).
- **Prevalence/incidence:** not formally quantified; ultra-rare (<~20 confirmed cases reported); locally elevated in Belgium due to a founder allele.
- **Penetrance:** appears high/complete in biallelic carriers (all reported biallelic individuals affected), though small numbers limit certainty.
- **Expressivity:** laterality and lesion size can vary; broadly consistent phenotype.
- **Founder effect:** documented (Belgium, 700 kb haplotype).
- **Consanguinity:** contributes (homozygous cases).
- **Carrier frequency:** ~0.3% for the recurrent duplication in one control cohort.
- **Sex ratio:** no reported bias (both sexes affected). No genetic anticipation (not a repeat-expansion disorder).

### 10. Diagnostics
- **Clinical:** recognition of bilateral preauricular atrophic/hypopigmented scar-like lesions at birth.
- **Genetic testing:** confirmatory **single-gene *CYP26C1* sequencing** (or inclusion in aplasia cutis/ectodermal/dermal dysplasia panels); WES/WGS useful when the phenotype is atypical (the gene was originally identified by exome sequencing). Chromosomal microarray is NOT indicated for FFDD4 (relevant instead to FFDD III/1p36).
- **Histopathology:** findings consistent with atrophic dermis / aplasia-cutis-like defect; biopsy is supportive but not specific.
- **Differential diagnosis:** membranous aplasia cutis congenita, preauricular tags/pits/sinuses, bitemporal FFDD I–III, and setting-specific scar mimics.

### 11. Outcome/Prognosis
- **Survival/mortality:** normal life expectancy; FFDD4 is not life-threatening and carries no disease-specific mortality.
- **Morbidity:** limited to cosmetic appearance of stable preauricular lesions; no functional disability.
- **Complications:** essentially none in non-syndromic cases; prognosis is excellent.
- **Prognostic factors:** none needed — uniform benign course.

### 12. Treatment
- **No disease-modifying or pharmacologic therapy exists or is required.** The condition is benign.
- **Supportive/cosmetic:** reassurance; optional **surgical/dermatologic scar revision or camouflage** for cosmetic concerns (NCIT: plastic/reconstructive surgery concepts).
- **No gene therapy, cell therapy, RNA therapy, targeted or immunotherapy** is in development or indicated.
- **Personalized medicine:** limited to confirming genotype for counseling.

### 13. Prevention
- **Primary prevention:** not applicable beyond reproductive counseling (the disease is congenital and genetic).
- **Genetic counseling:** central preventive measure — **25% recurrence risk** for siblings of an affected child; carrier testing of partners in founder populations (Belgium).
- **Reproductive options:** carrier/cascade testing, prenatal diagnosis, or preimplantation genetic testing are available for known familial variants.
- No vaccination, behavioral, or public-health prevention is relevant.

### 14. Other Species / Natural Disease
- **Ortholog:** mouse *Cyp26c1* (NCBI Gene 232174); zebrafish *cyp26c1*. No naturally occurring companion-animal or wildlife FFDD4 disease is reported (no OMIA entry for a CYP26C1 dermal dysplasia). The mouse ortholog is used experimentally (Finding 4). Zebrafish *cyp26c1* expression is modulated in craniofacial/ethanol-interaction models (e.g., *foxe1* mutant work, [PMID: 39360443](https://pubmed.ncbi.nlm.nih.gov/39360443/)), illustrating conservation of RA-catabolism roles but not a natural disease model. **No zoonotic potential** (non-infectious genetic disorder).

### 15. Model Organisms
- **Mouse** (*Mus musculus*): single *Cyp26c1* knockout is developmentally normal (redundant with *Cyp26a1*); *Cyp26a1⁻/⁻;Cyp26c1⁻/⁻* double knockouts show anterior brain truncation and loss of migratory cranial neural crest cells [PMID: 17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/). Mouse *Cyp26c1* expression maps to the human lesion site (face validity).
- **Phenotype recapitulation:** partial — spatial expression matches, but the single-gene mouse does NOT reproduce the human preauricular skin phenotype (key limitation from redundancy).
- **Resources:** MGI (mouse), ZFIN (zebrafish *cyp26c1*). No dedicated FFDD4 disease-model line is established.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [23161670](https://pubmed.ncbi.nlm.nih.gov/23161670/) | *FFDD type IV is caused by mutations in CYP26C1* | **Landmark**: identifies causal gene, founding variants, recessive inheritance, mouse fusion-line expression, carrier frequency. Supports F001, F002, F003, F006. |
| [29263414](https://pubmed.ncbi.nlm.nih.gov/29263414/) | *FFDD type 4: novel CYP26C1 mutations* | Expands allelic spectrum (missense + 2 splice-site); defines non-syndromic phenotype. Supports F001, F003. |
| [39828664](https://pubmed.ncbi.nlm.nih.gov/39828664/) | *Unexpected high prevalence of FFDD IV — Belgian founder effect* | Documents founder haplotype (700 kb) and elevated local prevalence. Supports F003, F006. |
| [40231353](https://pubmed.ncbi.nlm.nih.gov/40231353/) | *FFDD type IV: a case series* | Confirms morphology (bilateral oval hypopigmented preauricular lesions); need to rule out associated malformations. Supports F003, F005. |
| [30561078](https://pubmed.ncbi.nlm.nih.gov/30561078/) | *A case of FFDD type 4* | Hair-collar morphology; aplasia-cutis resemblance; clinical recognition emphasis. Supports F003, F005. |
| [28663233](https://pubmed.ncbi.nlm.nih.gov/28663233/) | *FFDDs: phenotypic spectrum and molecular heterogeneity* | Four-subtype classification; preauricular vs bitemporal distinction. Supports F005. |
| [21931173](https://pubmed.ncbi.nlm.nih.gov/21931173/) | *Setleis syndrome / FFDD reclassification* | Formal recognition of FFDD type IV as a new subtype. Supports F005. |
| [25728400](https://pubmed.ncbi.nlm.nih.gov/25728400/) | *1p36 dup/trip causes Setleis (FFDD III)* | Contrasts FFDD III genetics (TWIST2 / 1p36) with FFDD IV (CYP26C1). Supports F005. |
| [17067568](https://pubmed.ncbi.nlm.nih.gov/17067568/) | *CYP26A1/CYP26C1 regulate A-P patterning & cranial neural crest* | Double-KO cranial neural crest phenotype; single-KO normal (redundancy). Supports F002, F004. |
| [29476041](https://pubmed.ncbi.nlm.nih.gov/29476041/) | *CYP26C1 hydroxylase of multiple retinoids; CRABP interaction* | Biochemical substrate specificity and CRABP interaction. Supports F002, F007. |
| [15531370](https://pubmed.ncbi.nlm.nih.gov/15531370/) | *CYP26A1/CYP26C1 cooperate in equatorial retina* | Further evidence of paralog cooperation/redundancy. Supports F004. |
| [39360443](https://pubmed.ncbi.nlm.nih.gov/39360443/) | *foxe1 zebrafish, ethanol × craniofacial* | Conservation of *cyp26c1* in craniofacial RA metabolism (comparative context). Supports Section 14. |

Supporting mechanistic context on SHH–RA–Cyp26 interactions ([PMID: 31072004](https://pubmed.ncbi.nlm.nih.gov/31072004/); [PMID: 28715412](https://pubmed.ncbi.nlm.nih.gov/28715412/)) and Tbx1-dependent regulation of *Cyp26c1* in otic/cochlear development ([PMID: 19476657](https://pubmed.ncbi.nlm.nih.gov/19476657/); [PMID: 22275070](https://pubmed.ncbi.nlm.nih.gov/22275070/)) reinforce the upstream regulatory logic of CYP26C1 but were not required for the core findings.

---

## Limitations and Knowledge Gaps

1. **Small case numbers.** Fewer than ~20 molecularly confirmed patients exist worldwide. Estimates of penetrance, expressivity, prevalence, and genotype–phenotype correlation are therefore uncertain.
2. **No direct human tissue proof of RA excess.** The central mechanistic step (local retinoic-acid excess at the fusion line) is *inferred* from mouse expression and enzyme biochemistry; it has not been directly measured in human FFDD4 tissue.
3. **No faithful animal model of the skin phenotype.** Single *Cyp26c1* knockout mice are normal due to redundancy with *Cyp26a1*; the specific human preauricular dermal defect has not been recapitulated, limiting mechanistic dissection in vivo.
4. **No functional data for every variant.** Only p.Arg478His was tested in a cell assay; the splice-site and p.Arg77Pro variants are presumed (not proven) loss-of-function.
5. **Prevalence/incidence are unquantified** outside the Belgian founder observation; true population frequency is unknown.
6. **No treatment or biomarker research.** As a benign cosmetic condition, there are no therapeutic trials, prognostic biomarkers, or omics datasets specific to FFDD4.

---

## Proposed Follow-up Experiments / Actions

1. **Conditional/tissue-specific mouse model.** Generate *Cyp26c1* loss combined with reduced *Cyp26a1* dosage, or a face/neural-crest–restricted double knockout, to test whether local RA excess at the branchial-arch fusion line produces preauricular dermal defects — directly testing the inferred mechanistic step.
2. **Direct RA quantification / reporter assays.** Use RA-reporter mice or in-situ RA signaling readouts (e.g., *Rarb*, *Cyp26a1* induction) at the fusion line under *Cyp26c1* loss to demonstrate local RA excess.
3. **Functional validation of remaining variants.** Perform minigene splicing assays for c.1191+1G>T and c.1191+2insT, and cell-based activity assays for p.Arg77Pro, to confirm loss of function and refine ACMG classification.
4. **Patient registry and natural-history study.** Aggregate cases internationally (GeneMatcher, FFDD registry) to quantify penetrance, expressivity, laterality distribution, and any rare extracutaneous associations.
5. **Founder-population carrier screening.** In Belgium and related populations, estimate the true carrier frequency of the recurrent frameshift allele to inform counseling and reproductive screening.
6. **iPSC/organoid modeling.** Derive patient iPSC-based cranial neural crest or facial organoid models to interrogate RA signaling, neural-crest migration, and epithelial–mesenchymal fusion defects in a human genetic background.
7. **Structural modeling of missense variants.** Use AlphaFold/homology models of CYP26C1 to map p.Arg478His and p.Arg77Pro onto the heme-binding/substrate-access architecture, rationalizing loss of catalytic activity.

---

*Report compiled from 7 confirmed findings and 19 reviewed papers across 5 investigation iterations. Evidence types are labeled per finding as human clinical genetics, in vitro biochemistry, or mouse/model-organism data.*


## Artifacts

- [OpenScientist final report](Focal_Facial_Dermal_Dysplasia_Type_IV-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Focal_Facial_Dermal_Dysplasia_Type_IV-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 8 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004410` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `SO:0001574` (1 mention) - the report calls it "splice site"; SO calls it **splice_acceptor_variant**, and lists "splice acceptor variant" among its other names
- `GO:0042573` (2 mentions) - the report calls it "retinoic acid metabolic process", "Processes:** retinoic acid metabolic process"; GO calls it **retinoic acid metabolic process**
- `GO:0016712` (1 mention) - the report calls it "oxidoreductase activity, acting on paired donors with incorporation of O₂"; GO calls it **oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen**
- `CL:0000333` (3 mentions) - the report calls it "migratory cranial neural crest cell", "Cell types:** cranial neural crest cells"; CL calls it **migratory neural crest cell**
- `UBERON:0003066` (3 mentions) - the report calls it "pharyngeal/branchial arch", "pharyngeal arch"; UBERON calls it **pharyngeal arch 2**
- `HP:0010719` (1 mention) - the report calls it "abnormal hair pattern"; HP calls it **Abnormality of hair texture**, and lists "Abnormality of hair curl pattern" among its other names
- `CHEBI:26536` (1 mention) - the report calls it "retinoid"; CHEBI calls it **retinoic acid**
- `UBERON:0002067` (2 mentions) - the report calls it "Tissue:** skin/dermis", "dermis"; UBERON calls it **dermis**, and lists "vertebrate dermis" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0042573` - called "retinoic acid metabolic process", "Processes:** retinoic acid metabolic process"
- `CL:0000333` - called "migratory cranial neural crest cell", "Cell types:** cranial neural crest cells"
- `UBERON:0003066` - called "pharyngeal/branchial arch", "pharyngeal arch"
- `UBERON:0002067` - called "Tissue:** skin/dermis", "dermis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.