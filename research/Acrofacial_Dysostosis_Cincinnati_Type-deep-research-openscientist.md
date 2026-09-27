---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T07:41:21.160053'
end_time: '2026-09-02T08:16:58.721165'
duration_seconds: 2137.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acrofacial Dysostosis Cincinnati Type
  mondo_id: ''
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
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 18
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014651
    reported_labels:
    - MONDO
    ontology_label: acrofacial dysostosis Cincinnati type
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - NCBIGene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acrofacial_Dysostosis_Cincinnati_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acrofacial_Dysostosis_Cincinnati_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acrofacial Dysostosis Cincinnati Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Acrofacial Dysostosis Cincinnati Type** covering all of the
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

# Acrofacial Dysostosis, Cincinnati Type (AFDCIN): A Comprehensive Disease Characterization

**Disease:** Acrofacial Dysostosis, Cincinnati Type (AFDCIN)
**Key identifiers:** OMIM #616462 · MONDO:0014651 · ORPHA:457395 · Causal gene *POLR1A* (HGNC:9082; NCBIGene:25885; OMIM *616404)
**Category:** Mendelian, autosomal dominant (usually de novo)

---

## Summary

Acrofacial Dysostosis, Cincinnati type (AFDCIN) is an ultra-rare, autosomal dominant craniofacial malformation syndrome caused by heterozygous pathogenic variants in **POLR1A**, the gene encoding the largest catalytic subunit of **RNA Polymerase I (Pol I)**. It was first defined in 2015 in three unrelated individuals, each carrying a heterozygous *POLR1A* mutation, and belongs to the family of **ribosomopathies** — developmental disorders arising from impaired ribosome biogenesis ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/)). The clinical hallmark is a **Treacher Collins–like mandibulofacial dysostosis** (malar and mandibular hypoplasia, micrognathia, downslanting palpebral fissures, external-ear anomalies, cleft palate), historically accompanied by variable **limb ("acro-") anomalies**. A 2023 cohort expansion to 20 individuals broadened the recognized spectrum to include prominent **neurodevelopmental abnormalities** (hypotonia, developmental delay, seizures) and **structural cardiac defects** ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).

Mechanistically, AFDCIN is a **Pol I ribosomopathy**. Loss of POLR1A function reduces transcription of the **47S pre-ribosomal RNA**, the rate-limiting step of ribosome biogenesis. Because **cranial neural crest cells (NCCs)** and the neuroepithelium sustain exceptionally high rates of rRNA synthesis and protein translation during embryogenesis, they are selectively vulnerable to this deficit. The resulting **nucleolar stress triggers TP53-dependent apoptosis** of neuroepithelial progenitors, depleting the migrating neural crest population that builds most of the facial skeleton. This causal chain — validated in a *polr1a* zebrafish model — links the molecular lesion to the craniofacial phenotype and explains why a "housekeeping" transcription defect produces tissue-specific malformations ([PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/); [PMID: 35881792](https://pubmed.ncbi.nlm.nih.gov/35881792/)).

The *POLR1A* mutational spectrum is **dual**: it includes both **missense** variants (POLR1A is strongly missense-constrained, gnomAD mis_z = 5.08) and **truncating loss-of-function** alleles (nonsense, frameshift), plus large **2p11.2 copy-number variants**, indicating that both dominant missense/dominant-negative effects and haploinsufficiency can contribute. There is no disease-specific or targeted therapy; management is **supportive and multidisciplinary** (airway, feeding, craniofacial reconstruction, developmental support). TP53-pathway modulation prevents the phenotype partially in animal models but is not a human therapy. This report consolidates seven confirmed findings across the investigation into a mechanistically coherent, frequency-annotated characterization suitable for a disease knowledge-base entry.

---

## 1. Disease Information

**Overview.** AFDCIN is a rare Mendelian craniofacial dysostosis first delineated by Weaver and colleagues at Cincinnati Children's Hospital (hence "Cincinnati type"). "Acrofacial dysostosis" denotes a group of disorders combining **facial dysostosis** (mandibulofacial/otomandibular malformation) with **limb (acral) anomalies**. AFDCIN is distinguished within this group by its molecular cause: heterozygous *POLR1A* dysfunction ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/)).

**Key identifiers.**

| Resource | Identifier |
|----------|------------|
| OMIM (phenotype) | #616462 |
| OMIM (gene *POLR1A*) | *616404 |
| MONDO | MONDO:0014651 |
| Orphanet | ORPHA:457395 |
| Gene (HGNC) | HGNC:9082 (*POLR1A*) |
| NCBI Gene | 25885 |
| MANE transcript | NM_015425.6 |
| Ensembl gene | ENSG00000068654 |
| ICD-10 | Q87.0 (congenital malformation syndromes predominantly affecting facial appearance) — no AFDCIN-specific code |
| ICD-11 | LD2F.1Y (other specified developmental anomalies of face/neck) — no specific code |

**Synonyms / alternative names.** Acrofacial dysostosis, Cincinnati type; AFDCIN; POLR1A-related acrofacial dysostosis; Cincinnati-type mandibulofacial dysostosis. Within the broader literature it is increasingly grouped with **Pol I–related ribosomopathies** alongside Treacher Collins syndrome types 2–4 ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)).

**Source of information.** All data are derived from **aggregated disease-level resources** and **published case series** (n < 25 total reported individuals) plus model-organism and in vitro studies — not from large EHR/registry populations. The disease is too rare for population EHR analysis.

---

## 2. Etiology

**Primary cause — genetic.** AFDCIN is a monogenic disorder caused by **heterozygous pathogenic variants in *POLR1A***. Each of the three originally described individuals carried a heterozygous *POLR1A* mutation ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/): *"Each individual has a heterozygous mutation in POLR1A, which encodes a core component of RNA polymerase 1."*). The cohort was later expanded to 20 individuals with ≥13 unique heterozygous variants ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).

**Genetic risk factors.** The causal variant itself is the risk factor; there are no established modifier loci or susceptibility alleles. Because most cases are **de novo**, the principal "risk factor" for a new case is a spontaneous germline mutation event. **Advanced parental age** is a plausible but unproven contributor to de novo mutation rate (general principle, not disease-specific).

**Environmental risk factors.** None identified. AFDCIN is a purely genetic Mendelian disorder; there is no evidence for toxic, infectious, nutritional, or lifestyle contributions to its occurrence.

**Protective factors.** No genetic or environmental protective factors are documented in humans. In animal models, **genetic inhibition of tp53** suppresses neuroepithelial apoptosis and partially ameliorates the cranioskeletal phenotype — a "protective" mechanism at the pathway level, not a naturally occurring protective allele ([PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/)).

**Gene–environment interactions.** None described. Given the fully genetic etiology and severe developmental phenotype, gene–environment interaction is not a feature of this disease.

---

## 3. Phenotypes

AFDCIN produces a **multi-system phenotype** dominated by craniofacial malformation, with neurodevelopmental, cardiac, growth, airway, and limb involvement. Phenotype frequencies below are drawn from authoritative **HPO annotations** (ontology.jax.org; primary sources [PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/) and [PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)) tallied across the reported cohort.

| Phenotype | HPO term | Frequency (cohort) | Type |
|-----------|----------|--------------------|------|
| Congenital onset | HP:0003577 | 15/20 (75%) | Onset |
| Hypotonia | HP:0001252 | 10/17 (59%) | Neurological sign |
| Hypertelorism | HP:0000316 | 9/16 (56%) | Craniofacial sign |
| Global developmental delay | HP:0001263 | 8/14 (57%) | Neurodevelopmental |
| Micrognathia | HP:0000347 | 9/21 (43%) | Craniofacial sign |
| Microcephaly | HP:0000252 | 6/16 (38%) | Craniofacial/growth |
| Abnormality of limbs | HP:0040064 | 6/17 (35%) | Skeletal (acral) |
| Cleft palate | HP:0000175 | 6/20 (30%) | Craniofacial |
| Low-set ears | HP:0000369 | 6/17 (~35%) | Craniofacial |
| Microtia | HP:0008551 | 5/21 (24%) | Craniofacial |
| Ptosis | HP:0000508 | 5/18 (~28%) | Ocular/facial |
| Seizure | HP:0001250 | 5/5 (subset) | Neurological |
| Patent foramen ovale | HP:0001655 | 4/14 (29%) | Cardiac |
| Ventricular septal defect | HP:0001629 / HP:0001643 | 3/14 (21%) | Cardiac |
| Facial asymmetry | HP:0000324 | 3/18 (17%) | Craniofacial |
| Metopic synostosis | HP:0011330 | 3/18 (17%) | Craniofacial |
| Cleft lip | HP:0410030 | 2/17 (12%) | Craniofacial |

**Explicitly ABSENT features (important for differential diagnosis):** **Craniosynostosis** HP:0001363 (0/15) and **Macrocephaly** HP:0000256 (0/13).

**Craniofacial core.** The facial gestalt is **Treacher Collins–reminiscent**: malar (zygomatic) and mandibular hypoplasia, micrognathia, downslanting palpebral fissures, external-ear anomalies (microtia, low-set ears), and cleft palate ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).

**Limb (acral) anomalies.** Present in ~35% and variable; their presence with facial dysostosis defines the "acrofacial" designation. In the original series, 2/3 individuals had limb anomalies ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/)).

**Newly recognized systems (2023 expansion).** Neurodevelopmental abnormalities and structural cardiac defects were added to the spectrum ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/): *"observed numerous additional phenotypes including neurodevelopmental abnormalities and structural cardiac defects, in combination with highly prevalent craniofacial anomalies and variable limb defects."*).

**Characteristics.** Onset is **congenital** (75% congenital onset). Severity is **variable** — from milder mandibulofacial dysostosis to severe multi-system disease. The malformations are **structural and non-progressive** (stable after birth), though secondary complications (airway obstruction, feeding difficulty) evolve over infancy. Variable expressivity is attributed in part to **variant-specific molecular effects** ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/): *"In vitro assessments demonstrate variable effects of individual pathogenic variants on ribosomal RNA synthesis and nucleolar morphology, which supports the possibility of variant-specific phenotypic effects in affected individuals."*).

**Quality-of-life impact.** No formal QoL instrument (EQ-5D, SF-36, PROMIS) data exist for this ultra-rare disease. Anticipated impacts, by analogy to mandibulofacial dysostoses: neonatal **airway compromise** and **feeding difficulty** (micrognathia, cleft palate), **hearing loss** (ear anomalies), **speech** impairment, **neurodevelopmental** disability, and psychosocial impact of facial difference. These require lifelong multidisciplinary support.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***POLR1A*** (HGNC:9082; NCBIGene:25885; OMIM *616404), located at **chromosome 2p11.2** (GRCh38 chr2:86,020,216–86,106,155). POLR1A encodes the **largest catalytic subunit of RNA Polymerase I**, the enzyme dedicated to transcribing the 47S ribosomal RNA precursor ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/): *"Heterozygous pathogenic variants in POLR1A, which encodes the largest subunit of RNA Polymerase I, were previously identified as the cause of acrofacial dysostosis, Cincinnati-type."*).

**Pathogenic variant spectrum (MANE NM_015425.6).** ClinVar lists ~63 pathogenic/likely-pathogenic *POLR1A* records. Representative small variants:

| Class | Example variant | Protein | ClinVar significance |
|-------|-----------------|---------|----------------------|
| Missense | c.928C>T | p.(Arg310Cys) | Likely pathogenic |
| Missense | c.2357C>T | p.(Thr786Ile) | Pathogenic |
| Missense | c.4685G>T | p.(Cys1562Phe) | Likely pathogenic |
| Nonsense | c.2164C>T | p.(Arg722Ter) | Likely pathogenic |
| Nonsense | c.2527C>T | p.(Arg843Ter) | Pathogenic |
| Nonsense | c.4297G>T | p.(Glu1433Ter) | Likely pathogenic |
| Frameshift | c.6del | p.(Ile3fs) | P/LP |
| Frameshift | c.190del | p.(Cys64fs) | P/LP |
| Frameshift | c.2374dup | p.(Tyr792fs) | P/LP |
| Frameshift | c.2267_2288del | p.(Ser756fs) | P/LP |
| Frameshift | c.3649del | p.(Gln1217fs) | P/LP |
| Missense (modeled) | Met496Ile | p.(Met496Ile) | disrupts DNA binding/polymerase activity ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)) |

**Structural variants.** Large **2p11.2 CNVs** (contiguous-gene deletions/duplications encompassing *POLR1A*) are also reported, consistent with a haploinsufficiency contribution.

**Variant classification.** Per ACMG/AMP, disease alleles are classified pathogenic or likely pathogenic; **many additional missense alleles remain VUS**, reflecting the challenge of interpreting missense change in a large essential subunit.

**Allele frequency.** Disease alleles are **absent or ultra-rare in gnomAD** (de novo, embryonic-lethal-adjacent). *POLR1A* itself is broadly conserved and highly expressed.

**Functional consequences — dual mechanism.** Two lines of evidence indicate that both dominant missense effects and haploinsufficiency operate:

- **Constraint.** gnomAD constraint for *POLR1A*: **missense Z = 5.08** (strong missense intolerance; oe_mis = 0.75), LoF **LOEUF ≈ 0.49** (oe_lof = 0.41), pLI = 0.22, lof_z = 7.18. Thus POLR1A is **highly intolerant of missense change** and only **moderately tolerant of loss of function** — a pattern favoring **missense/dominant-negative** pathogenesis while not excluding LoF.
- **Mutational spectrum.** The co-occurrence of **missense, truncating (nonsense/frameshift) LoF**, and **whole-gene CNV** pathogenic alleles indicates that **haploinsufficiency also contributes** ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).

Structural modeling of the p.Met496Ile variant suggested **disruption of DNA binding and polymerase activity**, mechanistically linking a specific missense change to reduced Pol I catalytic function ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)).

**Modifier genes.** None established. Phenotypic heterogeneity is attributed primarily to variant-specific effects rather than trans-acting modifiers.

**Epigenetic information / chromosomal abnormalities.** No disease-specific methylation signature is described. Chromosomal-level lesions relevant to AFDCIN are the **2p11.2 CNVs** noted above.

---

## 5. Environmental Information

Not applicable. AFDCIN is a **monogenic developmental disorder** with **no known environmental, lifestyle, toxic, or infectious contributors**. No teratogen, occupational exposure, dietary factor, or pathogen is implicated in its causation or triggering.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous *POLR1A* variant** (missense, truncating LoF, or whole-gene CNV) **reduces the function or dosage of the largest catalytic subunit of RNA Polymerase I**.
2. Reduced Pol I activity **leads to deficient transcription of 47S pre-ribosomal RNA** (the rate-limiting step of ribosome biogenesis) — *demonstrated in polr1a zebrafish*.
3. Deficient rRNA transcription **results in reduced ribosome (monosome/polysome) assembly and impaired protein translation** — *demonstrated*.
4. Impaired ribosome biogenesis **causes nucleolar stress**, which **results in stabilization/activation of TP53** — *demonstrated in Pol I ribosomopathy models*.
5. TP53 activation **leads to apoptosis of neuroepithelial progenitor cells** — *demonstrated (Tp53-dependent neuroepithelial apoptosis)*.
6. Neuroepithelial apoptosis **results in a deficiency of migrating cranial neural crest cells (NCCs)** — the progenitors of most craniofacial skeletal structures — *demonstrated*.
7. Reduced NCC number and proliferation **leads to hypoplasia of NCC-derived craniofacial skeleton** → **mandibulofacial dysostosis** (malar/mandibular hypoplasia, micrognathia, ear/palate defects).
   - **Branch A (cranial):** the same neuroepithelial vulnerability **contributes to neurodevelopmental phenotypes** (hypotonia, developmental delay, microcephaly, seizures) — *inferred*.
   - **Branch B (cardiac/limb):** NCC and mesodermal contributions to cardiac outflow and limb development **contribute to structural cardiac and limb anomalies** — *inferred*.
8. **Tissue selectivity** arises because **NCC progenitors sustain unusually high rRNA transcription and translation**, rendering them **particularly sensitive to rRNA synthesis defects** — *demonstrated* ([PMID: 35881792](https://pubmed.ncbi.nlm.nih.gov/35881792/): *"High expression of Pol I subunits sustains elevated rRNA transcription in NCC progenitors, which supports their high tissue-specific levels of protein translation, but also makes NCCs particularly sensitive to rRNA synthesis defects."*).

```
POLR1A variant (missense / LoF / CNV)
        │  ↓ Pol I catalytic function / dosage
        ▼
↓ 47S pre-rRNA transcription  ──────────────►  [rate-limiting step]
        │
        ▼
↓ ribosome biogenesis / translation
        │
        ▼
Nucleolar stress ──► TP53 stabilization/activation
        │
        ▼
Neuroepithelial apoptosis (TP53-dependent)
        │
        ▼
Cranial neural crest cell deficiency  ◄── high tissue-specific
        │                                  translation demand
        ├──► craniofacial skeletal hypoplasia → mandibulofacial dysostosis
        ├──► (inferred) neurodevelopmental anomalies
        └──► (inferred) cardiac / limb anomalies
```

### Detail by category

- **Molecular pathways:** RNA Polymerase I–dependent **rDNA/rRNA transcription** and **ribosome biogenesis**; downstream **TP53 (p53) tumor-suppressor / nucleolar stress response** signaling. Convergence on **nucleolar organization and ribosomal RNA transcription** was confirmed by network analyses (STRING, Pathway Commons) placing POLR1A among Pol I / ribosome-biogenesis partners ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)).
- **Cellular processes:** **Apoptosis** (TP53-dependent) of neuroepithelial cells; **reduced cell proliferation** of neural crest progenitors; a **DNA-damage/nucleolar-stress response** (related Pol I disorders show rDNA damage and DNA-damage response, [PMID: 29364875](https://pubmed.ncbi.nlm.nih.gov/29364875/)).
- **Protein dysfunction:** Missense variants can act as **loss-of-function or dominant-negative** within the Pol I holoenzyme (e.g., p.Met496Ile disrupts DNA binding/polymerase activity); truncating variants and CNVs reduce dosage (**haploinsufficiency**).
- **Metabolic changes:** Reduced **translational capacity** in high-demand progenitors; no specific small-molecule metabolic defect.
- **Immune involvement:** None; not an immune-mediated disease.
- **Tissue damage mechanism:** **Nucleolar stress → apoptosis** of specific progenitor pools; the injury is developmental (failure to form structures) rather than degenerative.
- **Epigenetic changes:** Not specifically implicated; the lesion is at the level of Pol I transcription of rDNA.
- **Molecular profiling:** Zebrafish *polr1a* mutants show reduced 47S rRNA, reduced monosomes/polysomes, and impaired translation ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/); [PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/): *"This results in Tp53-dependent neuroepithelial apoptosis, diminished neural crest cell proliferation and cranioskeletal anomalies."*). In vitro patient-variant assays show **variable effects on rRNA synthesis and nucleolar morphology** ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).

**Suggested ontology terms.** GO biological process: rRNA transcription (GO:0009303), transcription by RNA polymerase I (GO:0006360), ribosome biogenesis (GO:0042254), regulation of apoptotic process (GO:0042981), neural crest cell migration (GO:0001755), neural crest cell development (GO:0014033). GO cellular component: nucleolus (GO:0005730), RNA polymerase I complex (GO:0005736). CL cell types: neural crest cell (CL:0000333), neuroepithelial cell (CL:0000710).

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Primary:** craniofacial skeleton and soft tissues — zygoma/malar (UBERON:0001683 zygomatic bone), mandible (UBERON:0001684), maxilla (UBERON:0002397), palate (UBERON:0001716), external ear/auricle (UBERON:0001757).
- **Nervous system (UBERON:0001016):** brain/neuroepithelium — hypotonia, developmental delay, microcephaly, seizures.
- **Cardiovascular system (UBERON:0004535):** heart — VSD, patent foramen ovale.
- **Musculoskeletal / limbs (UBERON:0002101):** variable acral anomalies.
- **Respiratory / upper airway:** secondary obstruction from micrognathia/palatal cleft.

**Tissue / cell level.** The critical target is the **cranial neural crest cell** (CL:0000333) and the **neuroepithelium** (CL:0000710) from which affected NCCs derive. Downstream, **cartilage/bone (skeletal connective tissue)** of the face is hypoplastic.

**Subcellular level.** The initiating compartment is the **nucleolus (GO:0005730)**, site of Pol I–driven rRNA transcription; the effector pathway involves the **nucleus** (TP53) and the **cytoplasmic translational machinery** (ribosomes, GO:0005840).

**Localization / lateralization.** Craniofacial involvement is typically **bilateral**, though **facial asymmetry** (HP:0000324) occurs in ~17%. Limb involvement is variable and can be asymmetric.

---

## 8. Temporal Development

- **Onset:** **Congenital** — malformations are established during embryonic craniofacial development; 75% of the cohort had documented congenital onset (HP:0003577). Onset pattern is **structural/developmental**, not acute.
- **Progression:** The primary malformations are **stable/non-progressive** after birth. There are no "stages." Secondary sequelae evolve over infancy and childhood — **airway obstruction** and **feeding difficulty** are most critical in the neonatal period; **hearing, speech, and developmental** trajectories unfold thereafter.
- **Course:** Chronic, **lifelong** structural condition managed by staged reconstruction and developmental support.
- **Critical periods:** The **embryonic window of neural crest specification, proliferation, and migration** is the vulnerable/opportunity window — the point at which the ribosome-biogenesis deficit exerts its damage. In animal models, **TP53-pathway inhibition during this window** partially prevents the phenotype ([PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/)), but no equivalent human intervention exists.
- **Remission:** Not applicable — structural malformation does not remit; surgical correction is the only means of anatomical improvement.

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare.** Fewer than ~25 individuals reported worldwide (3 in 2015; expanded to 20 in 2023). No reliable prevalence/incidence estimate exists; Orphanet classifies it among ultra-rare craniofacial disorders (ORPHA:457395).
- **Inheritance pattern:** **Autosomal dominant.** Most cases are **de novo** (spontaneous), consistent with reduced reproductive fitness of severely affected individuals.
- **Penetrance:** Presumed high/complete for the malformation phenotype among carriers of established pathogenic variants; formal penetrance estimates are unavailable given small numbers.
- **Expressivity:** **Variable**, attributed to variant-specific molecular effects on rRNA synthesis and nucleolar morphology ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented but theoretically possible; relevant to recurrence-risk counseling for apparently de novo cases.
- **Founder effects / consanguinity:** None (dominant, de novo; consanguinity is not a risk factor).
- **Carrier frequency:** Not applicable (dominant, not carrier-based).
- **Population demographics:** No ethnic predilection; cases reported across populations. **Sex ratio** appears roughly equal (no strong sex bias reported). Age distribution: diagnosed in **infancy/childhood** given congenital malformation.

---

## 10. Diagnostics

**Diagnostic approach.** Diagnosis rests on **clinical recognition** of Treacher Collins–like mandibulofacial dysostosis (with/without limb anomalies) followed by **molecular confirmation** of a heterozygous pathogenic *POLR1A* variant.

**Genetic testing (the definitive test).**
- **Exome sequencing (WES)** or a **craniofacial/mandibulofacial dysostosis gene panel** including *POLR1A* is the highest-yield approach; the original discovery used exome sequencing ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/)).
- **Single-gene *POLR1A* sequencing** (MANE NM_015425.6) is appropriate when the phenotype is characteristic.
- **Chromosomal microarray (CMA)** detects **2p11.2 CNVs** involving *POLR1A*.
- **Genome sequencing (WGS)** can capture both SNVs and structural variants in one assay.
- Related genes to include on a differential panel: *TCOF1, POLR1C, POLR1D, POLR1B* (Treacher Collins types 1–4), *EFTUD2, SF3B4* (other acrofacial dysostoses).

**Clinical / imaging tests.** Craniofacial **CT/X-ray** documents malar and mandibular hypoplasia; **echocardiography** screens for cardiac defects; **audiology** assesses hearing; **airway evaluation** (endoscopy/polysomnography) assesses obstruction; **brain MRI** and developmental assessment characterize neurodevelopmental involvement. No specific biomarker or laboratory abnormality is diagnostic.

**Clinical criteria.** No formal consensus diagnostic criteria exist; diagnosis is gestalt-based plus molecular confirmation.

**Differential diagnosis.** Chief differentials — **Treacher Collins syndrome** (types 1–4; *TCOF1/POLR1C/POLR1D/POLR1B*), **mandibulofacial dysostosis with microcephaly** (*EFTUD2*), **Nager acrofacial dysostosis** (*SF3B4*), **oculoauriculovertebral spectrum/Goldenhar**. Distinguishing features favoring AFDCIN: the **specific *POLR1A* genotype**, and the **absence of craniosynostosis and macrocephaly** (both 0/cohort). Notably, AFDCIN overlaps clinically and mechanistically with **Sweeney-Cox, Saethre-Chotzen, Robinow-Sorauf, and TCS types 2–4**, all now proposed as part of a **Pol I–related ribosomopathy spectrum** ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)).

**Screening.** No newborn or carrier screening exists. **Cascade testing** of parents is used mainly to establish de novo status and recurrence risk.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No formal survival statistics. Prognosis is driven by **severity of airway compromise and associated anomalies** (cardiac, CNS). Severe neonatal airway obstruction and feeding failure are the principal early-life threats; with modern multidisciplinary craniofacial care many affected individuals survive into childhood and beyond.
- **Morbidity / function:** Substantial. Long-term morbidity includes **hearing loss, speech impairment, feeding/airway issues, facial difference, and neurodevelopmental disability** (hypotonia 59%, developmental delay 57%, seizures in a subset).
- **Disease course:** Chronic and stable structurally; complications (recurrent otitis/hearing loss, obstructive sleep apnea, dental/orthognathic issues) accrue over time.
- **Recovery potential:** The malformations do not spontaneously resolve but are **partially correctable surgically**. Neurodevelopmental outcome depends on the degree of CNS involvement.
- **Prognostic factors:** Extent of airway obstruction, presence/severity of cardiac and CNS anomalies, and — molecularly — the **variant-specific effect** on Pol I function, which correlates with phenotypic severity ([PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/)).
- **Quality-of-life instruments:** No disease-specific QoL data available.

---

## 12. Treatment

**No disease-modifying or targeted therapy exists.** Management is **supportive, symptom-directed, and multidisciplinary**, coordinated through a craniofacial team.

**Supportive / surgical mainstays.**
- **Airway management:** positioning, nasopharyngeal airway, mandibular distraction osteogenesis, or tracheostomy for severe micrognathia-related obstruction. A **non-surgical intra-oral orthopaedic appliance** has been reported to relieve upper-airway obstruction in related mandibular micrognathia/craniofacial anomalies and may be applicable ([PMID: 9633164](https://pubmed.ncbi.nlm.nih.gov/9633164/)).
- **Feeding support:** specialized feeding, NG/gastrostomy as needed.
- **Cleft palate repair** and staged **craniofacial/orthognathic reconstruction** (NCIT: Reconstructive Surgery).
- **Hearing / ear:** audiologic management, bone-conduction/hearing aids, otologic/reconstructive surgery for microtia.
- **Cardiac:** management/repair of structural defects as indicated.
- **Neurodevelopmental:** early intervention, physical/occupational/speech therapy; seizure management.

**Pharmacotherapy / pharmacogenomics / advanced therapeutics.** No approved pharmacologic, gene, cell, or RNA-based therapy. **Pathway-level proof of concept** exists only in animal models: **genetic inhibition of tp53** suppresses neuroepithelial apoptosis and partially ameliorates the cranioskeletal phenotype, but **does not restore rDNA transcription or NCC proliferation** ([PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/)) — a conceptual, embryonic-window intervention with no human translation.

**Experimental / trials.** No AFDCIN-specific clinical trials (NCT) identified. Given ultra-rarity, care follows general craniofacial-anomaly best practice rather than disease-specific protocols.

**Suggested NCIT terms:** Reconstructive Surgery (C15329), Supportive Care (C15277), Physical Therapy (C15367), Speech Therapy (C15451), Tracheostomy (C51844).

---

## 13. Prevention

- **Primary prevention:** Not possible — the disease arises from spontaneous de novo mutation. No modifiable risk factor exists.
- **Secondary prevention:** **Prenatal detection** — characteristic mandibulofacial anomalies may be identified on prenatal ultrasound; **prenatal molecular testing** is possible when a familial variant is known.
- **Tertiary prevention:** Early multidisciplinary intervention to **prevent complications** (airway monitoring/sleep studies, hearing surveillance, developmental support) is the principal preventive strategy.
- **Genetic counseling:** Central to management. For a de novo case, recurrence risk to parents is low but nonzero (germline mosaicism); an affected individual has a **50% transmission risk** (autosomal dominant). **Preimplantation genetic testing** and prenatal diagnosis are options when the variant is known.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Model species with disease relevance:** **Zebrafish** (*Danio rerio*, NCBI Taxon 7955) *polr1a* mutants recapitulate the core mechanism and cranioskeletal phenotype ([PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/); [PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/)). Related Pol I subunit models (*polr1c*, *polr1d*) reproduce Treacher Collins–like anomalies ([PMID: 27448281](https://pubmed.ncbi.nlm.nih.gov/27448281/)).
- **Orthologous genes:** *Polr1a* in mouse (*Mus musculus*, Taxon 10090) and zebrafish; the gene and Pol I function are **deeply evolutionarily conserved** across eukaryotes.
- **Naturally occurring disease in animals:** No naturally occurring *POLR1A*-related acrofacial dysostosis is documented in companion animals or wildlife (no OMIA entry noted). The disease is known only through humans and engineered/mutant models.
- **Comparative biology:** The **NCC-selective vulnerability to nucleolar stress** is conserved across zebrafish, *Xenopus*, mouse, and human, making cross-species comparison highly informative ([PMID: 25756904](https://pubmed.ncbi.nlm.nih.gov/25756904/); [PMID: 24497835](https://pubmed.ncbi.nlm.nih.gov/24497835/)).
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

| Model | Type | Genetic manipulation | Phenotype recapitulation | Reference |
|-------|------|----------------------|--------------------------|-----------|
| **Zebrafish** *polr1a* mutant | Vertebrate | Loss-of-function | Deficient 47S rRNA transcription, ↓ monosomes/polysomes, Tp53-dependent neuroepithelial apoptosis, ↓ NCC proliferation, cranioskeletal anomalies mimicking human disease | [PMID: 25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/); [PMID: 29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/) |
| **Zebrafish** *polr1c* / *polr1d* mutants | Vertebrate | Homozygous LoF | Cartilage hypoplasia, TCS-like cranioskeletal defects; tp53 inhibition ameliorates | [PMID: 27448281](https://pubmed.ncbi.nlm.nih.gov/27448281/) |
| ***Xenopus* nol11 knockdown** | Vertebrate | Morpholino knockdown | Impaired pre-rRNA transcription/processing, apoptosis, abnormal craniofacial cartilage; p53 rescue | [PMID: 25756904](https://pubmed.ncbi.nlm.nih.gov/25756904/) |
| **Zebrafish** *wdr43* (fantome) | Vertebrate | Point mutation/premature stop | Ribosome biogenesis defect, p53-dependent NCC craniofacial cartilage defects | [PMID: 24497835](https://pubmed.ncbi.nlm.nih.gov/24497835/) |
| ***Drosophila* Nopp140 RNAi** | Invertebrate | RNAi depletion | Nucleolar stress, ribosome loss, apoptosis (p53-independent in fly) | [PMID: 23412656](https://pubmed.ncbi.nlm.nih.gov/23412656/) |
| **Patient-variant in vitro assays** | Cellular | Expression of individual *POLR1A* variants | Variable effects on rRNA synthesis and nucleolar morphology | [PMID: 37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/) |

**Phenotype recapitulation.** The zebrafish *polr1a* model is the **primary disease model** and faithfully reproduces the mechanistic cascade and craniofacial output. **Limitations:** models capture craniofacial/NCC biology well but incompletely model the human **neurodevelopmental** and **cardiac** spectrum; the **acral/limb** component is not the focus of fish models; and *Drosophila* apoptosis is p53-independent, limiting mechanistic transfer.

**Resources:** ZFIN (zebrafish), MGI (mouse orthologue *Polr1a*), Xenbase (*Xenopus*), FlyBase (*Drosophila*).

---

## Mechanistic Model / Interpretation

AFDCIN is best understood as a **prototypical Pol I ribosomopathy** that sits within a **continuum of RNA Polymerase I–related craniofacial syndromes** together with Treacher Collins types 2–4, Sweeney-Cox, Saethre-Chotzen, and Robinow-Sorauf ([PMID: 41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/)). The unifying logic is that a **quantitative reduction in ribosome-building capacity** — whether from a *POLR1A* missense change that cripples the catalytic subunit or from a truncating/CNV allele that halves its dosage — is tolerated by most cells but **not** by the metabolically extreme **cranial neural crest**, which must synthesize protein at very high rates to proliferate and migrate on schedule. When rRNA supply falls below this demand, **nucleolar stress activates TP53**, apoptosis prunes the neuroepithelial/NCC pool, and the craniofacial skeleton that those cells would have built is left hypoplastic. This elegantly resolves the central paradox of the ribosomopathies: how a housekeeping defect yields a **tissue-specific** malformation.

Two refinements distinguish this investigation's model. **First, the mechanism is genotype-graded:** individual variants exert **variable effects on rRNA synthesis and nucleolar morphology**, and this molecular gradient plausibly underlies the observed **variable expressivity** and the newly appreciated multi-system (neurodevelopmental, cardiac) breadth. **Second, the mutational mechanism is dual.** gnomAD constraint (mis_z = 5.08) marks POLR1A as exquisitely missense-intolerant — the signature of a subunit where a single altered residue can poison the holoenzyme (loss-of-function or dominant-negative) — yet the presence of bona fide truncating and whole-gene-deletion pathogenic alleles shows that **haploinsufficiency also causes disease**. The practical implication is that AFDCIN cannot be reduced to a single molecular class; variant interpretation must accommodate both mechanisms.

The **TP53 node** is the most therapeutically provocative element. Across zebrafish, *Xenopus*, and mouse models, genetic p53 inhibition **rescues the apoptosis and partially the skeleton without correcting the upstream rRNA deficit** — establishing p53 as a **downstream, druggable effector** but also warning that suppressing apoptosis leaves the fundamental ribosome shortfall unaddressed and carries oncogenic risk. Any future intervention would need to act within the **narrow embryonic window** of neural crest development, which is currently inaccessible in human patients.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [25913037](https://pubmed.ncbi.nlm.nih.gov/25913037/) | *AFDCIN is caused by POLR1A dysfunction* | Founding paper: 3 individuals, heterozygous *POLR1A*; zebrafish model; establishes gene and dominant inheritance |
| [37075751](https://pubmed.ncbi.nlm.nih.gov/37075751/) | *POLR1A variants underlie phenotypic heterogeneity* | Cohort expansion to 20; adds neurodevelopmental + cardiac phenotypes; variant-specific rRNA/nucleolar effects |
| [29750247](https://pubmed.ncbi.nlm.nih.gov/29750247/) | *tp53-dependent and independent signaling in AFDCIN* | Defines causal chain: rRNA deficit → Tp53 neuroepithelial apoptosis → NCC deficiency → cranioskeletal anomalies; p53 inhibition as prevention |
| [35881792](https://pubmed.ncbi.nlm.nih.gov/35881792/) | *Requirement for rRNA transcription in development* | Explains NCC tissue-selective vulnerability to rRNA synthesis defects |
| [41010008](https://pubmed.ncbi.nlm.nih.gov/41010008/) | *Pol I dysfunction underlying craniofacial syndromes* | Positions AFDCIN within a Pol I ribosomopathy spectrum; structural modeling of p.Met496Ile |
| [29364875](https://pubmed.ncbi.nlm.nih.gov/29364875/) | *Tissue-selective nucleolar stress and rDNA damage* | Nucleolar stress → rDNA damage → p53 apoptosis in cranial NCCs (mechanistic parallel) |
| [27448281](https://pubmed.ncbi.nlm.nih.gov/27448281/) | *Polr1c/Polr1d in craniofacial development* | Companion Pol I subunit zebrafish models; tp53 rescue |
| [25756904](https://pubmed.ncbi.nlm.nih.gov/25756904/) | *Nol11 in Xenopus craniofacial development* | Cross-species conservation; p53 rescues skeleton but not ribosome defect |
| [24497835](https://pubmed.ncbi.nlm.nih.gov/24497835/) | *Wdr43 in zebrafish development* | Ribosome biogenesis → p53-dependent NCC craniofacial defects |
| [23412656](https://pubmed.ncbi.nlm.nih.gov/23412656/) | *Nucleolar stress in Drosophila (Nopp140)* | Invertebrate nucleolar-stress model (p53-independent apoptosis) |
| [34714179](https://pubmed.ncbi.nlm.nih.gov/34714179/) | *Mandibulofacial dysostoses case series (India)* | Context on phenotypic/molecular heterogeneity of mandibulofacial dysostoses |
| [9633164](https://pubmed.ncbi.nlm.nih.gov/9633164/) | *Non-surgical airway management* | Supportive-care option for micrognathia-related airway obstruction |

**Evidence source types:** human clinical case series (n < 25 total), model-organism studies (zebrafish/Xenopus/Drosophila), in vitro variant assays, and computational/constraint analyses (gnomAD, ClinVar, structural modeling). No randomized trials or large registries exist.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~25 individuals reported; frequencies (e.g., micrognathia 43%) rest on small denominators and are subject to ascertainment bias toward severe cases.
2. **No epidemiologic data.** Prevalence, incidence, penetrance, and survival are not formally quantified.
3. **Genotype–phenotype correlation is incomplete.** Although variant-specific in vitro effects are demonstrated, the mapping from specific *POLR1A* alleles to clinical severity and to the missense-vs-LoF mechanistic split remains only partially resolved; many missense alleles are VUS.
4. **Human mechanism is inferential for non-craniofacial systems.** The neurodevelopmental, cardiac, and limb branches of the causal chain are extrapolated from the craniofacial mechanism and model organisms, not directly demonstrated in human tissue.
5. **No therapeutics.** p53-pathway rescue is confined to embryonic animal models with no human translation and unresolved oncogenic-safety concerns.
6. **No QoL / natural-history data** and no standardized diagnostic criteria.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & natural-history study** to establish prevalence, penetrance, survival, and standardized phenotype frequencies with adequate denominators.
2. **Systematic genotype–phenotype correlation** pairing each *POLR1A* variant with quantitative rRNA-synthesis/nucleolar-morphology assays and detailed phenotyping to test the missense-severity vs LoF hypothesis and to reclassify VUS.
3. **Functional reclassification pipeline** (deep mutational scanning of *POLR1A* in a cellular Pol I–activity readout) to resolve the many missense VUS in ClinVar.
4. **Conditional / graded mouse models** (mammalian *Polr1a* allelic series) to model the neurodevelopmental and cardiac branches not captured in fish and to test dosage vs dominant-negative mechanisms.
5. **Therapeutic window studies** probing whether modulating nucleolar stress/p53 (or boosting ribosome biogenesis) during neural crest development can rescue the phenotype safely — using the established zebrafish and future mouse models.
6. **Standardized diagnostic criteria and multidisciplinary care guideline** for AFDCIN within the broader Pol I ribosomopathy spectrum, incorporating the absence of craniosynostosis/macrocephaly as discriminating features.

---

*Report compiled from 7 confirmed findings and 12 reviewed papers across a 5-iteration autonomous investigation. Evidence is predominantly human case-series plus model-organism and computational data; no clinical-trial-level evidence exists for this ultra-rare disorder.*


## Artifacts

- [OpenScientist final report](Acrofacial_Dysostosis_Cincinnati_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acrofacial_Dysostosis_Cincinnati_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 22 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014651` (2 mentions) - the report calls it "MONDO"; MONDO calls it **acrofacial dysostosis Cincinnati type**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000333` (2 mentions) - the report calls it "cranial neural crest cell"; CL calls it **migratory neural crest cell**
- `CL:0000710` (2 mentions) - the report calls it "neuroepithelium"; CL calls it **neurecto-epithelial cell**, and lists "neuroepithelial cell" among its other names
- `UBERON:0002101` (1 mention) - the report calls it "Musculoskeletal / limbs"; UBERON calls it **limb**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000324` - called "Facial asymmetry", "facial asymmetry"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `NCBIGene`.