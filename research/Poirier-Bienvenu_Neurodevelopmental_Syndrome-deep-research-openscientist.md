---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:25.635947'
end_time: '2026-11-05T00:33:04.513919'
duration_seconds: 2318.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Poirier-Bienvenu Neurodevelopmental Syndrome
  mondo_id: MONDO:0032889
  category: Mendelian
  causal_genes: CSNK2B
  omim_id: OMIM:618732
  synonyms: POBINDS; CSNK2B-related neurodevelopmental disorder
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
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 10
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:39236211
  - PMID:38395944
  - PMID:34740143
  relevance_assessed: 18
  on_topic: 15
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 11
  labels_variant: 2
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
  path: Poirier-Bienvenu_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Poirier-Bienvenu_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Poirier-Bienvenu Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0032889 (if available)
- **Causal gene(s):** CSNK2B
- **OMIM:** OMIM:618732
- **Synonyms:** POBINDS; CSNK2B-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Poirier-Bienvenu Neurodevelopmental Syndrome** covering all of the
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

# Poirier-Bienvenu Neurodevelopmental Syndrome (POBINDS): A Comprehensive Disease Characterization Report

**Disease:** Poirier-Bienvenu Neurodevelopmental Syndrome (POBINDS)
**Causal gene:** ***CSNK2B*** — encoding the β (regulatory) subunit of casein kinase 2 (CK2)
**MONDO:** MONDO:0032889 · **OMIM:** #618732 · **Orphanet:** ORPHA:689397 · **GARD:** 0027366 · **UMLS/MedGen:** C5231482
**Category:** Mendelian, autosomal dominant (almost always *de novo*)

---

## Summary

Poirier-Bienvenu Neurodevelopmental Syndrome (POBINDS; MONDO:0032889, OMIM #618732) is a rare, autosomal dominant neurodevelopmental disorder caused by heterozygous, almost always *de novo*, pathogenic variants in **CSNK2B**. This gene encodes the **β (regulatory) subunit of casein kinase 2 (CK2)**, a ubiquitously expressed, constitutively active serine/threonine protein kinase holoenzyme (α₂β₂) with hundreds of substrates across signal transduction, cell cycle, cytoskeletal regulation, and neuronal development. The disorder was first established in 2017 by exome sequencing of two intellectual-disability trios, and by 2024–2025 more than 80–100 individuals had been reported. The defining clinical dyad is **early-onset generalized epilepsy** (seizure onset usually before 2 years of age) and **developmental delay / intellectual disability (DD/ID)** of highly variable severity, spanning near-normal cognition with pharmacoresponsive seizures to profound ID with intractable epilepsy and refractory status epilepticus.

The dominant disease mechanism is **loss-of-function (LOF) / haploinsufficiency**: nonsense, frameshift, splice-site, and many missense variants converge on a reduced pool of functional CK2β, destabilizing the CK2 holoenzyme and lowering its kinase activity. CSNK2B is among the most loss-of-function-constrained genes in the human genome (gnomAD pLI ≈ 1.0, LOEUF 0.22) and is one of the top-ranked *de novo* mutation genes relative to gene size, explaining the dominant *de novo* genetics. A mechanistically distinct **allelic branch** exists: specific missense variants at codon 32 (p.Asp32His, p.Asp32Asn, p.Asp32Tyr) do **not** act by simple LOF but rather upregulate CSNK2B and exert a **dominant-negative** effect that disrupts canonical **Wnt/β-catenin** signaling, producing a separate **Intellectual Disability–Craniodigital Syndrome (IDCS)** with dysmorphism and digital anomalies rather than the epilepsy-dominant POBINDS phenotype.

There is no disease-specific or curative therapy. Management is **symptomatic and multidisciplinary**: antiseizure medications (frequently polytherapy), developmental and rehabilitative therapies, and endocrine surveillance (notably for growth-hormone deficiency, present in a substantial subset). Approximately 40% of patients have pharmacoresistant epilepsy, and **seizure control correlates statistically with cognitive outcome**, making early and effective seizure management the single most actionable prognostic lever. Model systems — embryonic-lethal mouse CK2β knockouts, CRISPR knockout neurons, and patient-derived lymphoblastoid/fibroblast lines — underscore the organism-level essentiality and dosage sensitivity of CK2β.

---

## Section 1 — Disease Information

POBINDS is a Mendelian neurodevelopmental disorder characterized in most individuals by **developmental delay/intellectual disability and seizures**, caused by heterozygous pathogenic variants in **CSNK2B** (the β regulatory subunit of CK2). It was first delineated by Poirier, Bienvenu, and colleagues in 2017 ([PMID: 28585349](https://pubmed.ncbi.nlm.nih.gov/28585349/)), who "identified two de novo splice variants (c.175+2T>G; c.367+2T>C) in the CSNK2B gene encoding the β subunit of the Caseine kinase 2 (CK2)." GeneReviews (2024) describes "CSNK2B-related neurodevelopmental disorder (CSNK2B-NDD), reported in more than 80 individuals to date, … characterized in most individuals by developmental delay (DD)/intellectual disability (ID) and seizures" ([PMID: 39236211](https://pubmed.ncbi.nlm.nih.gov/39236211/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032889 |
| OMIM | #618732 |
| Orphanet | ORPHA:689397 |
| GARD | 0027366 |
| UMLS / MedGen | C5231482 / MedGen 1684718 |
| Gene (HGNC) | CSNK2B, HGNC:2460 |
| NCBI Gene | 1460 |
| Ensembl | ENSG00000204435 |
| UniProt | P67870 |
| Locus | 6p21.33 (within the MHC region) |

**Synonyms / alternative names:** POBINDS; CSNK2B-related neurodevelopmental disorder (CSNK2B-NDD); CSNK2B-related developmental and epileptic encephalopathy (in severe cases). This disorder (β subunit, CSNK2B) is distinct from the α-subunit disorder CSNK2A1 / Okur-Chung Neurodevelopmental Syndrome (OCNDS).

**Information source:** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews) synthesizing **individual-patient case reports and cohort studies** (e.g., the 25-patient Ernst et al. cohort, the 9-patient Italian Orsini cohort, and a pooled analysis of 103 individuals). It is not derived from population EHR mining.

---

## Section 2 — Etiology

**Disease causal factor — genetic, monogenic.** POBINDS is caused by heterozygous pathogenic variants in **CSNK2B**. There is no environmental, infectious, or multifactorial contribution to disease causation; it is a classic monogenic *de novo* dominant disorder.

**Genetic risk factors.** The causal variants are pathogenic/likely pathogenic *de novo* changes in CSNK2B (missense, nonsense, frameshift, splice-site, and whole-gene/contiguous 6p21 deletions). The underlying "risk" is essentially the elevated *de novo* mutation rate at this locus: a meta-analysis of 46,489 disease-associated *de novo* mutations ranked CSNK2B among "the top-10 genes with the highest proportions of DNM relative to gene size … H3-3 A, DDX3X, CSNK2B, PURA, ZC4H2, STXBP1, SCN1A, SATB2, H3-3B and TUBA1A" ([PMID: 38395944](https://pubmed.ncbi.nlm.nih.gov/38395944/)). Advanced paternal age is a general risk factor for *de novo* mutations but has not been specifically quantified for CSNK2B.

**Environmental risk factors / protective factors / gene–environment interactions.** None are established or expected for a monogenic *de novo* disorder. No protective alleles, modifier genes, dietary, or lifestyle factors have been identified. This absence is itself informative for the knowledge base: POBINDS risk is determined at conception by the presence of the *de novo* variant.

**Modifier of severity (intragenic):** The strongest determinant of phenotypic severity is the **location** of the variant within the protein (see Sections 4 and 6), not an external modifier gene.

---

## Section 3 — Phenotypes

The core phenotype is **early-onset generalized epilepsy + DD/ID**. In the 25-patient cohort of Ernst et al. (Epilepsia 2021), "most individuals had developmental delay and generalized epilepsy with onset in the first 2 years," with "a broad spectrum of phenotypic severity, ranging from early normal development with pharmacoresponsive seizures to profound intellectual disability with intractable epilepsy and recurrent refractory status epilepticus" ([PMID: 34041744](https://pubmed.ncbi.nlm.nih.gov/34041744/)).

Phenotype frequencies from the largest pooled cohort (103 individuals; Zhang et al., Acta Epileptol 2026): "Seizures occurred in 94.2% of patients, 87.4% were diagnosed with epilepsy, and seizure onset before 24 months of age in 87.2%" ([PMID: 42764391](https://pubmed.ncbi.nlm.nih.gov/42764391/)).

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Seizures (generalized tonic-clonic, myoclonic, absence; also focal) | Clinical sign | Neonatal–early childhood (<24 mo in ~87%) | Mild→intractable; status epilepticus in severe | ~94% | HP:0001250 (Seizure); HP:0002069 (Bilateral tonic-clonic); HP:0002123 (Generalized myoclonic) |
| Developmental delay / intellectual disability | Behavioral/cognitive | Infancy–childhood | Borderline/mild → severe/profound | Majority >5 y have ID | HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability) |
| Hypotonia (infancy) | Clinical sign | Infancy | Variable | Less consistent | HP:0001252 (Hypotonia) |
| Ataxia / impaired coordination | Clinical sign | Childhood | Variable | Less consistent | HP:0001251 (Ataxia) |
| Neurobehavioral/psychiatric features (autistic features, ADHD) | Behavioral | Childhood | Variable | Subset | HP:0000708 (Behavioral abnormality); HP:0000729 (Autistic behavior) |
| Short stature / growth hormone deficiency | Lab/physical | Childhood | Variable | ~66% short stature | HP:0004322 (Short stature); HP:0000824 (Growth hormone deficiency) |
| Digital anomalies (more characteristic of IDCS branch) | Physical | Congenital | Variable | Subset | HP:0100259 (Postaxial polydactyly) |
| Facial dysmorphism | Physical | Congenital | Mild | Subset | HP:0001999 (Abnormal facial shape) |
| Vascular/endocrine anomalies | Clinical sign | Variable | Variable | Subset (Italian cohort) | — |

**Quality-of-life impact:** Driven primarily by seizure burden and degree of ID. Individuals with pharmacoresistant epilepsy have greater cognitive/motor impairment and higher dependency; those with normal neurological development (≈27% in the Bonanni cohort) all had pharmacosensitive epilepsy. No disease-specific EQ-5D/SF-36/PROMIS data are available; QoL is inferred from epilepsy and ID severity.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** CSNK2B (HGNC:2460; NCBI Gene 1460; Ensembl ENSG00000204435; UniProt P67870), locus **6p21.33**. Encodes **Casein kinase II subunit beta**, a 215–amino-acid protein that functions as the regulatory/scaffolding subunit of the CK2 holoenzyme (α₂β₂). It contains a **zinc-finger/dimerization domain** and an **α-subunit interaction region** (~residues 188–193), and participates in Wnt signaling.

**Pathogenic variants and classification.** All major classes are reported and classified pathogenic/likely pathogenic per ACMG/AMP (most arising *de novo*, PS2-supported):

| Variant class | Examples | Functional consequence |
|---|---|---|
| Splice-site | c.175+2T>G; c.367+2T>C; c.367+5G>A; c.367+6T>C | mRNA instability → LOF |
| Nonsense / frameshift | e.g., c.634_635del (p.Lys212AspfsTer33) | Truncation → LOF/haploinsufficiency |
| Missense (various domains) | p.Arg111Pro; p.Cys137Phe (zinc-finger) | Protein destabilization, impaired dimerization → LOF |
| Missense (codon 32) | p.Asp32His; p.Asp32Asn; p.Asp32Tyr | **Dominant-negative**, Wnt disruption → IDCS (distinct) |
| Start-codon | c.1A>G p.(Met1?) | Reduced/abolished translation; milder/endocrine presentation |
| Structural | Whole-gene / contiguous 6p21 deletions | Gene loss → haploinsufficiency |

**Allele frequency:** Pathogenic *de novo* variants are essentially **absent from population databases** (gnomAD). CSNK2B is under extreme constraint: pLI = 0.99999; observed/expected LoF = 0.069 (obs 2 vs expected 28.8; LOEUF upper bound 0.218); LoF Z = 4.24; missense also constrained (mis_Z = 4.37; oe_mis = 0.385) (gnomAD, GRCh38). This constraint directly supports haploinsufficiency as the dominant mechanism (Finding F007).

**Somatic vs germline:** Variants are germline (constitutional) *de novo*. **Mosaicism** has been documented — Chen et al. 2023 reported a p.Lys212AspfsTer33 carrier with "mutant mosaicism, and the proportion of alleles in peripheral blood DNA was 28%" ([PMID: 37020656](https://pubmed.ncbi.nlm.nih.gov/37020656/)) — relevant to recurrence counseling.

**Functional consequences:** For POBINDS, **loss of function / haploinsufficiency** (reduced CK2 holoenzyme activity). For the codon-32 IDCS branch, a **dominant-negative** gain of abnormal function on the Wnt pathway.

**Genotype–phenotype correlation:** Variant **location** predicts severity better than variant **type**. In the 103-patient pooled analysis, there was "no significant difference in seizure/epilepsy/drug-resistant-epilepsy incidence among mutation-type groups," whereas "mutations outside annotated protein domains showed higher epilepsy penetrance than those within domains (P = 0.034)" ([PMID: 42764391](https://pubmed.ncbi.nlm.nih.gov/42764391/)). Earlier work found "individuals with missense variants in the zinc finger domain had manageable seizures (p = 0.009) and milder intellectual disability (p = 0.003) than those with missense variants in other domains" ([PMID: 35774559](https://pubmed.ncbi.nlm.nih.gov/35774559/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** No specific modifier genes or disease-specific DNA-methylation (episignature) findings are established. Contiguous 6p21.33 deletions encompassing CSNK2B can cause the disorder and are detectable by chromosomal microarray.

---

## Section 5 — Environmental Information

**Not applicable.** POBINDS is a monogenic *de novo* genetic disorder. No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are implicated in its causation. Fever may act as a nonspecific seizure trigger (febrile convulsions reported in some individuals), but this is a seizure precipitant rather than an etiologic agent.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

**Primary (POBINDS, LOF branch):**

1. A heterozygous *de novo* **CSNK2B** variant (nonsense, frameshift, splice, or destabilizing missense) **leads to** reduced quantity of stable, functional CK2β protein (mRNA/protein instability; impaired dimerization/localization).
2. Reduced CK2β **results in** decreased assembly of the CK2 holoenzyme (α₂β₂) and **reduced CK2 holoenzyme kinase activity** (haploinsufficiency; *demonstrated* in patient cells and in vitro).
3. Reduced CK2 activity **leads to** hypophosphorylation of CK2's many neuronal substrates governing neuronal migration, cytoskeletal dynamics, synaptic function, and ion-channel/excitability regulation (*partly inferred*; CK2 substrate breadth is established, substrate-specific links in POBINDS are incompletely mapped).
4. Disrupted neuronal development and excitatory/inhibitory balance **results in** cortical network hyperexcitability → **early-onset generalized epilepsy**, and impaired neurodevelopment → **developmental delay/intellectual disability** (*clinically demonstrated*; precise circuit mechanism *inferred*).
5. Seizure burden, where poorly controlled, **further impairs** cognitive development (seizure control correlates with cognitive outcome), creating a feed-forward branch worsening the NDD phenotype.

**Allelic branch (IDCS, dominant-negative Wnt):**

1b. A **CSNK2B codon-32** missense variant (p.Asp32His/Asn/Tyr) **leads to** *upregulated* CSNK2B transcript/protein that acts dominant-negatively.
2b. The mutant CK2β **impairs interaction with DVL3 and β-catenin**, **resulting in** markedly reduced phosphorylated β-catenin and absent active nuclear β-catenin.
3b. Global **dysregulation of canonical Wnt/β-catenin signaling** (313 CK2 substrates enriched for nuclear β-catenin regulation show absent phosphorylation) **leads to** the craniodigital syndrome (dysmorphism, digital anomalies, ID) — **distinguishable from POBINDS**.

```
                 CSNK2B de novo variant
                 /                      \
   LOF / haploinsufficiency        codon-32 missense (Asp32)
   (↓ stable CK2β)                 (↑ CK2β, dominant-negative)
          |                               |
   ↓ CK2 holoenzyme assembly       impaired DVL3 / β-catenin binding
   ↓ CK2 kinase activity           ↓ phospho-β-catenin, no nuclear β-catenin
          |                               |
   hypophosphorylation of          dysregulated canonical
   neuronal CK2 substrates         Wnt/β-catenin signaling
          |                               |
   network hyperexcitability +     craniodigital morphogenesis defect
   impaired neurodevelopment              |
          |                          IDCS (dysmorphism, digits, ID)
   EPILEPSY + DD/ID (POBINDS)
          |
   poor seizure control → worse cognition (feed-forward)
```

### Detail by category

- **Molecular pathways:** CK2 is a master pleiotropic kinase; the IDCS branch specifically implicates **canonical Wnt/β-catenin signaling** ([PMID: 35571680](https://pubmed.ncbi.nlm.nih.gov/35571680/)). Suggested GO: GO:0016055 (Wnt signaling pathway), GO:0006468 (protein phosphorylation).
- **Cellular processes:** Neuronal migration, cytoskeletal organization, cell proliferation, adhesion. CK2β knockout in GN11 immature neurons produced "dramatic alterations in the cytoskeleton" and impaired migration ([PMID: 31779225](https://pubmed.ncbi.nlm.nih.gov/31779225/)). Suggested GO: GO:0001764 (neuron migration), GO:0007010 (cytoskeleton organization).
- **Protein dysfunction:** Reduced CK2β stability and impaired holoenzyme formation. Zinc-finger-domain variants "destabilize the protein and affect holoenzyme formation, effectively reducing the pool of competent holoCK2" ([PMID: 40317201](https://pubmed.ncbi.nlm.nih.gov/40317201/)).
- **Biochemical abnormality:** Reduced CK2 serine/threonine kinase activity (a kinase hypofunction). "Reduced casein kinase 2 holoenzyme activity may represent a unifying pathogenesis" ([PMID: 35774559](https://pubmed.ncbi.nlm.nih.gov/35774559/)).
- **Immune/metabolic/tissue-damage categories:** Not primary drivers; there is no autoimmune, inflammatory, oxidative-stress, or fibrotic mechanism established. Metabolic involvement manifests indirectly via endocrine (growth-hormone) axis dysfunction.
- **Subcellular compartments:** CK2β localizes to the nucleus and cytoplasm; mislocalization is part of the missense pathomechanism. Suggested GO cellular component: GO:0005956 (protein kinase CK2 complex), GO:0005634 (nucleus).
- **Cell types involved:** Neurons (CNS), suggested CL:0000540 (neuron); broadly expressed but neurodevelopmental tissues clinically dominant.

Upstream = reduced functional CK2β/CK2 activity (or dominant-negative Wnt disruption); downstream = network hyperexcitability, impaired neurodevelopment, and (for IDCS) craniodigital morphogenesis defects.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ/system:** Central nervous system / brain (UBERON:0000955, brain; UBERON:0001950, neocortex). Body system: **nervous system** (UBERON:0001016).
- **Secondary organ involvement:** Endocrine system — pituitary/growth-hormone axis (short stature/GHD in ~66%); vascular anomalies in a subset; musculoskeletal/craniofacial in the IDCS branch (digits, craniofacial skeleton).
- **Tissue/cell level:** Nervous tissue; neurons (CL:0000540), with cortical and likely excitatory/inhibitory neuronal populations implicated through excitability imbalance. Migration/cytoskeletal defects implicate developing/immature neurons (modeled in GN11 cells).
- **Subcellular level:** Nucleus (GO:0005634), cytoplasm, and the protein kinase CK2 complex (GO:0005956).
- **Localization & lateralization:** Diffuse/bilateral CNS involvement consistent with **generalized epilepsy**; neuroimaging is frequently normal or nonspecific, indicating a functional rather than focal structural lesion.

---

## Section 8 — Temporal Development

- **Onset:** Congenital genetic basis with clinical onset in **infancy/early childhood**. Seizure onset is before 24 months in ~87% of patients ([PMID: 42764391](https://pubmed.ncbi.nlm.nih.gov/42764391/)); the Bonanni cohort described clustered generalized tonic-clonic or myoclonic seizures with onset <18 months and delayed development in >75% ([PMID: 34740143](https://pubmed.ncbi.nlm.nih.gov/34740143/)).
- **Onset pattern:** Subacute to chronic; epilepsy may present acutely with seizure clusters or status epilepticus.
- **Progression / course:** Generally **non-neurodegenerative** but **lifelong (chronic)**. Severity is largely set early; developmental trajectory depends heavily on seizure control. Epilepsy may be stable/pharmacoresponsive or episodic with refractory clusters and recurrent status epilepticus in severe cases.
- **Remission patterns:** Treatment-induced seizure control is achievable in the majority (~60%); some achieve normal neurological development. No spontaneous resolution of the underlying disorder.
- **Critical period:** Early childhood (first ~2 years) is the key window — both the period of seizure onset and the window in which effective seizure control most plausibly protects cognitive development.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal dominant**, "typically caused by a de novo pathogenic variant… Almost all probands … have the disorder as the result of a de novo pathogenic variant. Rarely, individuals … have an affected parent" ([PMID: 39236211](https://pubmed.ncbi.nlm.nih.gov/39236211/)).
- **Penetrance:** High/complete for *de novo* carriers; **expressivity is highly variable** (severity spectrum from near-normal to profound).
- **Recurrence risk / mosaicism:** Low sib recurrence unless a parent carries the variant (then 50%). **Germline/somatic mosaicism** documented (28% blood allele fraction; [PMID: 37020656](https://pubmed.ncbi.nlm.nih.gov/37020656/)) → nonzero recurrence risk even with apparently negative parental testing.
- **Mutability:** CSNK2B is among the **top-10 most *de novo*-mutable disease genes relative to size** ([PMID: 38395944](https://pubmed.ncbi.nlm.nih.gov/38395944/)) and is extremely LOF-intolerant (pLI ≈ 1.0).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** Not applicable — variants are *de novo*, not inherited founder alleles; consanguinity is irrelevant for a dominant *de novo* mechanism.
- **Carrier frequency:** Not applicable (no recessive carrier state; pathogenic variants absent from gnomAD).
- **Epidemiology:** Rare; exact prevalence/incidence not established. >80 individuals reported by 2024, ~100 by 2025. No reported ethnic predilection, geographic clustering, or established sex bias; cohorts include diverse populations (European, Italian, Chinese).

---

## Section 10 — Diagnostics

**Diagnosis is molecular.** Identification of a heterozygous CSNK2B pathogenic variant via exome/genome sequencing or a multigene epilepsy/NDD panel is the diagnostic standard (GeneReviews 2024).

- **Genetic testing approach:** Exome sequencing (WES) or genome sequencing (WGS) with trio analysis to confirm *de novo* status; NGS **epilepsy/developmental-and-epileptic-encephalopathy (DEE) and intellectual-disability panels** that include CSNK2B; single-gene testing when CSNK2B is clinically suspected; **chromosomal microarray (CMA)** to detect contiguous 6p21.33 deletions encompassing CSNK2B. Karyotyping, FISH, mtDNA, and repeat-expansion testing are not indicated for the typical presentation.
- **EEG:** Typically shows epileptiform abnormalities — generalized/multifocal spike-and-wave and polyspikes consistent with generalized epilepsy.
- **Neuroimaging (MRI):** Frequently **normal or nonspecific**; e.g., "No abnormality was detected in the head magnetic resonance imaging (MRI)" ([PMID: 40211296](https://pubmed.ncbi.nlm.nih.gov/40211296/)). Normal MRI supports a genetic rather than structural diagnostic pathway.
- **Endocrine workup:** Growth assessment and GH-axis testing given ~66% short stature / frequent GHD.
- **Biomarkers / labs:** No specific biochemical biomarker; routine metabolic workup is typically normal.
- **Differential diagnosis:** Other genetic generalized/developmental epileptic encephalopathies (e.g., STXBP1-, SCN1A-, KCNQ2-related DEE), other *de novo* NDD-epilepsy genes; the α-subunit disorder CSNK2A1/OCNDS; and the **CSNK2B codon-32 IDCS** branch when craniodigital dysmorphism predominates.
- **Screening:** No population or newborn screening (rare, *de novo*). Carrier screening is not applicable. Cascade testing is only relevant where a parent is found to be mosaic or affected.

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** Not primarily life-limiting; no established reduction in survival, though severe refractory epilepsy/status epilepticus carries associated morbidity and risk. No disease-specific mortality rate is published.
- **Morbidity/function:** Driven by epilepsy severity and degree of ID; ranges from near-normal functioning to profound disability with dependency.
- **Key prognostic factor — seizure control:** In the Bonanni cohort (n≈15), "epilepsy was pharmaco-resistant in 40%. All the individuals (27%) with normal neurological development had pharmaco-sensitive epilepsy," and "a statistically significant correlation between seizure control and the severity of cognitive impairment was documented (χ²(3) = 9.44; p = .024)" ([PMID: 34740143](https://pubmed.ncbi.nlm.nih.gov/34740143/)). Thus pharmacoresponsiveness is both an outcome and a prognostic marker.
- **Genotype-based prognosis:** Variant **location** (intra- vs extra-domain; zinc-finger missense) stratifies seizure manageability and ID severity ([PMID: 42764391](https://pubmed.ncbi.nlm.nih.gov/42764391/); [PMID: 35774559](https://pubmed.ncbi.nlm.nih.gov/35774559/)).
- **Complications:** Refractory status epilepticus, developmental regression with poorly controlled seizures, short stature/GHD, and (branch-dependent) skeletal/vascular anomalies.
- **Recovery potential:** No cure; developmental/motor gains achievable with rehabilitation. Yang et al. (2025, n=4) reported seizures effectively controlled in 3/4 with conventional antiseizure medication and rehabilitation-improved motor/intellectual function, though "language recovery was slow."

---

## Section 12 — Treatment

**No disease-specific or curative therapy exists; management is supportive and symptomatic** (GeneReviews 2024).

- **Pharmacotherapy (antiseizure medications, NCIT: Anticonvulsant Agent):** Polytherapy is common. Yang et al. note "there is no specific treatment, and antiepileptic therapy usually requires the combination of two or more anti-epileptic drugs" ([PMID: 34370157](https://pubmed.ncbi.nlm.nih.gov/34370157/)). Agents reported across cohorts include **valproate** and **levetiracetam**, among others. ~40% have pharmacoresistant epilepsy ([PMID: 34740143](https://pubmed.ncbi.nlm.nih.gov/34740143/)).
- **Endocrine therapy:** **Growth hormone** replacement for documented GHD, with reported growth response ([PMID: 33166063](https://pubmed.ncbi.nlm.nih.gov/33166063/); [PMID: 39676320](https://pubmed.ncbi.nlm.nih.gov/39676320/)).
- **Supportive/rehabilitative:** Physical, occupational, and speech therapy; developmental/educational support. Motor and intellectual function improve with rehabilitation; language recovery is often slow.
- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** None approved or in trials specific to POBINDS. Computational drug-repurposing (Souza 2025) proposed caryophyllene oxide, linoleic acid, and tangeretin as candidate multi-target neuroprotective compounds with CSNK2B as a hub target — **not clinically validated**.
- **Pharmacogenomics:** No disease-specific pharmacogenomic guidance; standard ASM pharmacogenetics (e.g., HLA-related) applies generally, not CSNK2B-specifically.
- **Treatment strategy:** Individualized seizure management is the priority given its prognostic link to cognition; multidisciplinary care (neurology, endocrinology, developmental/rehabilitation, genetics) is standard.

Suggested NCIT: Anticonvulsant Agent (ASMs); Growth Hormone Therapy; Rehabilitation Therapy.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for a *de novo* monogenic disorder; no modifiable risk factors.
- **Secondary prevention:** Early molecular diagnosis enables prompt, optimized seizure management — the key lever for improving developmental outcome given the seizure-control/cognition correlation.
- **Tertiary prevention:** Aggressive seizure control, endocrine surveillance (growth/GH), developmental surveillance and early rehabilitation to limit complications.
- **Genetic counseling:** Essential. Low recurrence risk for *de novo* cases, but **mosaicism** can confer nonzero recurrence risk; prenatal/preimplantation testing is possible for families with a known variant or a mosaic/affected parent. (GeneReviews, NSGC/ACMG frameworks.)
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthology / taxonomy:** CSNK2B is highly evolutionarily conserved. Orthologs: mouse *Csnk2b* (NCBI Gene 13000), with conservation extending to *Drosophila* and yeast (where CK2β is non-essential, unlike mammals). CK2β acquired essential functions in mammals (see Section 15).
- **Natural disease in other species:** No naturally occurring CSNK2B-related neurodevelopmental disease is catalogued in companion animals or wildlife (no OMIA entry identified for this disorder). Disease knowledge derives from engineered models, not spontaneous veterinary disease.
- **Comparative biology:** Mammalian CK2β is **cell-essential and embryonically essential**, whereas yeast survive without functional CK2β — a key comparative-biology contrast underscoring mammalian dosage sensitivity ([PMID: 12529396](https://pubmed.ncbi.nlm.nih.gov/12529396/)).
- **Zoonotic potential / cross-species transmission:** Not applicable (genetic disorder).

---

## Section 15 — Model Organisms

| Model | Type | Key finding | Phenotype recapitulation / limitation |
|---|---|---|---|
| **Mouse constitutive *Csnk2b* knockout** | Mammalian, genetic KO | Homozygous KO → postimplantation embryonic lethality; embryos small at E6.5, reduced proliferation (no overt apoptosis), resorbed by E7.5; homozygous ES cells unobtainable ([PMID: 12529396](https://pubmed.ncbi.nlm.nih.gov/12529396/)) | Demonstrates essentiality/dosage sensitivity; **cannot model the heterozygous human neurodevelopmental phenotype** directly — a conditional/heterozygous or knock-in model is needed |
| **Conditional mouse KO** | Mammalian, conditional | Loss of CK2β deleterious for ES cells and primary embryonic fibroblasts ([PMID: 12529396](https://pubmed.ncbi.nlm.nih.gov/12529396/)) | Confirms cell-level essentiality |
| **GN11 immature neuron CRISPR KO** | Cellular (neuronal) | CK2β knockout "counteracts cell migration, inducing dramatic alterations in the cytoskeleton" ([PMID: 31779225](https://pubmed.ncbi.nlm.nih.gov/31779225/)) | Links CK2β loss to neuronal migration/cytoskeletal defects relevant to neurodevelopment; in vitro only |
| **Patient-derived LCLs / fibroblasts** | Human in vitro | Reduced CK2 activity, mRNA/protein instability (LOF); for Asp32, Wnt/β-catenin dysregulation ([PMID: 36833176](https://pubmed.ncbi.nlm.nih.gov/36833176/); [PMID: 35571680](https://pubmed.ncbi.nlm.nih.gov/35571680/)) | Principal human models for mechanism; lack neural-circuit/organismal context |

**Resources:** MGI (*Csnk2b*), IMPC for engineered alleles; patient-derived lines are the key human in vitro resource. A faithful heterozygous/knock-in or neuron-specific conditional mouse recapitulating epilepsy + DD/ID remains a notable gap.

---

## Mechanistic Model / Interpretation

POBINDS is best understood as a **CK2-dosage disease**. CSNK2B is extraordinarily intolerant to loss of function (pLI ≈ 1.0, LOEUF 0.22), and the mammalian CK2β subunit is both cell-essential and embryonically essential. A single *de novo* hit that reduces the pool of functional CK2β — via mRNA/protein instability (truncating/splice variants) or protein destabilization/impaired dimerization (many missense variants) — lowers CK2 holoenzyme activity below a threshold required for normal neurodevelopment, producing early-onset generalized epilepsy and DD/ID. The convergence of all LOF variant classes on the same "reduced holoCK2" endpoint explains why **variant type is a weak predictor of severity**, while **variant location** (intra- vs extra-domain, zinc-finger missense) — which determines *how much* residual function remains — is a better predictor.

A mechanistically separable **codon-32 (Asp32) branch** breaks this LOF rule: these variants *increase* CSNK2B expression yet act **dominant-negatively** to collapse canonical Wnt/β-catenin signaling, yielding a craniodigital syndrome (IDCS) rather than epilepsy-dominant POBINDS. This two-branch architecture (LOF→POBINDS vs Asp32 dominant-negative→IDCS) is the central nuance for a knowledge base: *one gene, two allelic disorders with opposite directionality of molecular effect.*

Finally, the **seizure-control ↔ cognition** correlation introduces a clinically actionable feed-forward loop: poorly controlled early seizures appear to worsen the developmental trajectory. This makes early genetic diagnosis and optimized antiseizure therapy the most consequential intervention in the absence of any targeted treatment.

---

## Evidence Base

| PMID | Role | Support |
|---|---|---|
| [28585349](https://pubmed.ncbi.nlm.nih.gov/28585349/) | Founding paper (Poirier/Bienvenu) | Establishes CSNK2B as causal via *de novo* splice variants |
| [39236211](https://pubmed.ncbi.nlm.nih.gov/39236211/) | GeneReviews (2024) | Gene–disease relationship, AD/*de novo* inheritance, >80 individuals, supportive care |
| [34041744](https://pubmed.ncbi.nlm.nih.gov/34041744/) | Ernst et al., cohort (n=25) | Early-onset generalized epilepsy + DD; broad severity spectrum |
| [42764391](https://pubmed.ncbi.nlm.nih.gov/42764391/) | Zhang et al., pooled (n=103) | Phenotype frequencies (94.2% seizures; 87.2% <24 mo); location>type for penetrance |
| [35774559](https://pubmed.ncbi.nlm.nih.gov/35774559/) | Zhang et al., Front Neurosci | Unifying reduced-holoenzyme pathogenesis; zinc-finger genotype–phenotype |
| [40317201](https://pubmed.ncbi.nlm.nih.gov/40317201/) | Kavaliova et al. | Missense variants destabilize protein, reduce competent holoCK2 |
| [36833176](https://pubmed.ncbi.nlm.nih.gov/36833176/) | Di Stazio et al. | mRNA/protein instability → reduced CK2 complex (haploinsufficiency) |
| [38395944](https://pubmed.ncbi.nlm.nih.gov/38395944/) | Lopes-Marques et al. | CSNK2B among top-10 *de novo*-mutable genes per size |
| [37020656](https://pubmed.ncbi.nlm.nih.gov/37020656/) | Chen et al. | Mosaicism (28% blood allele fraction) |
| [35571680](https://pubmed.ncbi.nlm.nih.gov/35571680/) | Asif et al., HGG Adv | Asp32 dominant-negative Wnt disruption → IDCS |
| [34983633](https://pubmed.ncbi.nlm.nih.gov/34983633/) | Wilke et al. | Independent Asp32Tyr craniodigital case |
| [34740143](https://pubmed.ncbi.nlm.nih.gov/34740143/) | Bonanni et al. | 40% pharmacoresistant; seizure control↔cognition (p=.024) |
| [34370157](https://pubmed.ncbi.nlm.nih.gov/34370157/) | Yang et al. | No specific treatment; ASM polytherapy |
| [39676320](https://pubmed.ncbi.nlm.nih.gov/39676320/) | Aouchiche et al. | 66% short stature; GHD; isolated GHD presentation |
| [33166063](https://pubmed.ncbi.nlm.nih.gov/33166063/) | Selvam et al. | Linear-growth abnormality; GH therapy response |
| [12529396](https://pubmed.ncbi.nlm.nih.gov/12529396/) | Buchou et al. | Mouse KO embryonic lethal; mammalian CK2β cell-essential |
| [31779225](https://pubmed.ncbi.nlm.nih.gov/31779225/) | Lettieri et al. | Neuron CK2β KO → migration/cytoskeletal defects |
| [40211296](https://pubmed.ncbi.nlm.nih.gov/40211296/) | Yang et al. (2025) | Normal MRI; seizures controlled in 3/4; slow language recovery |

---

## Limitations and Knowledge Gaps

1. **Substrate-level mechanism incomplete.** The chain from "reduced CK2 activity" to "cortical hyperexcitability/epilepsy" is inferred; the specific CK2 neuronal substrates (ion channels, synaptic proteins) driving epileptogenesis in POBINDS are not definitively mapped.
2. **No faithful in-vivo neurodevelopmental model.** The mouse null is embryonic-lethal; a heterozygous/knock-in or neuron-conditional model recapitulating epilepsy + DD/ID is lacking, limiting preclinical testing.
3. **Epidemiology unquantified.** No reliable prevalence/incidence, penetrance-by-age, or sex-ratio estimates; cohorts are small and ascertainment-biased toward severe/epileptic presentations.
4. **Phenotype expansion ongoing.** Milder non-epileptic and endocrine-predominant presentations (e.g., isolated GHD, start-codon variant) suggest the reported spectrum under-samples mild cases.
5. **No episignature / modifier data.** Disease-specific DNA-methylation signatures and genetic modifiers of severity are unexplored.
6. **No targeted therapy evidence.** Repurposing candidates are purely computational and unvalidated.
7. **Citations require independent re-verification.** PMIDs/snippets are carried from prior iterations marked "unchecked" and should be re-validated against primary abstracts before external publication.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a heterozygous Csnk2b⁺/⁻ and patient-variant knock-in mouse** (and/or neuron-specific conditional KO) to test for spontaneous seizures, EEG abnormalities, and cognitive/behavioral deficits — the critical missing in-vivo model.
2. **Map disease-relevant CK2 substrates in neurons** via phosphoproteomics in patient iPSC-derived neurons/organoids vs isogenic controls, focusing on ion-channel and synaptic targets to connect kinase hypofunction to hyperexcitability.
3. **Build a prospective international natural-history registry** to quantify prevalence, penetrance, sex ratio, developmental trajectories, and genotype (location)–phenotype correlations with adequate power.
4. **Formal genotype–phenotype meta-analysis** distinguishing LOF-POBINDS vs Asp32-IDCS branches, and testing the intra- vs extra-domain penetrance signal in an expanded cohort.
5. **Evaluate whether early, aggressive seizure control improves cognitive outcome** in a longitudinal/treatment-stratified study, directly testing the seizure-control↔cognition causal hypothesis.
6. **Assess DNA-methylation episignature** for diagnostic VUS resolution and define endocrine (GH-axis) surveillance guidelines.
7. **Validate computational repurposing candidates** (e.g., in neuron/organoid models) before any clinical consideration.
8. **Re-verify all cited PMIDs and quoted snippets** against primary abstracts prior to knowledge-base ingestion.

---

*Report compiled from a 5-iteration autonomous investigation; 11 confirmed findings integrated. Evidence sources span human clinical cohorts, in vitro patient-cell studies, cellular CRISPR models, mouse genetics, and population constraint databases (gnomAD).*


## Artifacts

- [OpenScientist final report](Poirier-Bienvenu_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Poirier-Bienvenu_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 18 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39236211` *(abstract only)*: "CSNK2B-related neurodevelopmental disorder (CSNK2B-NDD), reported in more than 80 individuals to date, … characterized in most individuals by developmental delay (DD)/intellectual disability (ID) and seizures"
  - closest text in source: "CLINICAL CHARACTERISTICS: CSNK2B-related neurodevelopmental disorder (CSNK2B-NDD), reported in more than 80 individuals to date, is characterized in most individuals by developmental delay (DD) / intellectual disability (ID) and seizures"
- `PMID:38395944` *(abstract only)*: "the top-10 genes with the highest proportions of DNM relative to gene size … H3-3 A, DDX3X, CSNK2B, PURA, ZC4H2, STXBP1, SCN1A, SATB2, H3-3B and TUBA1A"
  - closest text in source: "Of the 13,277 human genes in which DNMs have so far been found, the top-10 genes with the highest proportions of DNM relative to gene size were H3-3 A, DDX3X, CSNK2B, PURA, ZC4H2, STXBP1, SCN1A, SATB2, H3-3B and TUBA1A"
- `PMID:39236211` *(abstract only)*: "typically caused by a de novo pathogenic variant… Almost all probands … have the disorder as the result of a de novo pathogenic variant. Rarely, individuals … have an affected parent"
  - closest text in source: "Almost all probands reported to date whose parents have undergone molecular genetic testing have the disorder as the result of a de novo pathogenic variant"
- `PMID:34740143` *(abstract only)*: "a statistically significant correlation between seizure control and the severity of cognitive impairment was documented (χ²(3) = 9.44; p = .024)"
  - closest text in source: "The severity of cognitive and motor impairments was higher in the group with pharmaco-resistant epilepsy, and a statistically significant correlation between seizure control and the severity of cognitive impairment was documented (χ2(3) = 9.44; p = .024) INTERPRETATION: Early seizure onset, clustered seizures and delayed development in both males and females were early clinical markers in most patients with CSNK2B mutations"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0032889` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Poirier-Bienvenu neurodevelopmental syndrome**, and lists "POBINDS" among its other names
- `GO:0005634` (2 mentions) - the report calls it "nucleus", "Subcellular level:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "nucleus", "Subcellular level:** Nucleus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

24 of 26 terms resolved to a current term; the rest could not be looked up either way.