---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:24.380945'
end_time: '2026-11-05T00:12:42.640830'
duration_seconds: 1098.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MSX2-Related Craniosynostosis
  mondo_id: MONDO:0011481
  category: Mendelian
  causal_genes: MSX2
  omim_id: OMIM:604757
  synonyms: craniosynostosis type 2; CRS2; Warman-Mulliken-Hayward syndrome; craniosynostosis,
    Warman type
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
citation_count: 18
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 14
  validator_version: 0.5.1
term_validation:
  total_terms: 36
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 23
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MSX2-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MSX2-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MSX2-Related Craniosynostosis
- **MONDO ID:** MONDO:0011481 (if available)
- **Causal gene(s):** MSX2
- **OMIM:** OMIM:604757
- **Synonyms:** craniosynostosis type 2; CRS2; Warman-Mulliken-Hayward syndrome; craniosynostosis, Warman type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MSX2-Related Craniosynostosis** covering all of the
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

# MSX2-Related Craniosynostosis (Boston-Type, CRS2): Comprehensive Disease Report

**Disease:** MSX2-Related Craniosynostosis (Boston-type) · **Causal gene: MSX2** (msh homeobox 2, HGNC:7392, UniProt P35548, 5q35.2)
**MONDO:0011481** ("craniosynostosis 2") · **OMIM #604757** · **Orphanet ORPHA:1541** · **DOID:0061009** · **MedGen/UMLS C1858160** · **SNOMED CT 720817008**

---

## Summary

MSX2-Related Craniosynostosis, historically called **Boston-type craniosynostosis (CRS2)** and also **Warman-Mulliken-Hayward syndrome**, is a rare autosomal dominant disorder of premature cranial-suture fusion caused by **gain-of-activity** alterations of the homeodomain transcription factor **MSX2** on chromosome 5q35.2. The disease is genetically distinct from the many FGFR-, TWIST1-, and EFNB1-driven craniosynostosis syndromes; its defining molecular lesion is the recurrent missense change at **codon 148 of MSX2** (p.Pro148His in the original Boston kindred, with subsequent families carrying p.Pro148Leu and other Pro148 substitutions), and, less commonly, **MSX2 copy-number gains** (intragenic duplication and 5q35 triplication). The proline at position 148 corresponds to position 7 of the MSX2 homeodomain and is highly conserved.

The central mechanistic insight — established across human genetics and reciprocal mouse models — is that **MSX2 is dosage-sensitive and bidirectionally determines skull phenotype**. *Increased* MSX2 activity drives excessive osteogenic differentiation and proliferation of cranial-suture osteoprogenitors, producing premature suture fusion (craniosynostosis). *Decreased* MSX2 activity (haploinsufficiency) produces the opposite phenotype: defective calvarial ossification with persistent enlarged parietal foramina (PFM). This reciprocity is one of the clearest dosage-phenotype relationships in human developmental genetics and has been validated by transgenic mice overexpressing mutant Msx2 (which develop craniosynostosis and ectopic cranial bone) and Msx2-null mice (which develop calvarial foramina from defective osteoprogenitor proliferation).

Clinically, Boston-type craniosynostosis shows **highly variable expression and incomplete penetrance**, ranging from isolated single-suture synostosis to severe multi-suture fusion with turribrachycephaly and (in the original family) cloverleaf skull. Multiple endocranial erosions ("digital markings") on CT are a recurrent diagnostic clue. Extracranial features are generally mild (minor limb/digit anomalies, refraction errors); copy-number gains have additionally caused ocular colobomas and microphthalmia-spectrum defects. Intelligence is typically normal. The condition is **extraordinarily rare** — only a handful of families reported worldwide — against a background craniosynostosis birth prevalence of ~1 in 2,500. Management is entirely surgical (cranial vault remodeling or endoscopic suturectomy, <1% mortality) combined with genetic counseling; no targeted pharmacotherapy exists.

---

## Key Findings

### Finding 1 — The recurrent causal lesion is a gain-of-function missense change at MSX2 codon 148

The original Boston kindred reported by Jabs et al. (1993) carries a **C>A transversion in MSX2** that substitutes **histidine for a highly conserved proline at position 7 of the homeodomain** — equivalent to **p.Pro148His (P148H)** in full-length protein numbering. The variant segregated with autosomal dominant craniosynostosis with no recombination to an intronic MSX2 marker, establishing MSX2 as the causal gene.

> *"a histidine substitutes for a highly conserved proline at position 7 of the MSX2 homeodomain exclusively in affected members"* — [PMID: 8106171](https://pubmed.ncbi.nlm.nih.gov/8106171/)

For nearly two decades this remained the only reported MSX2 craniosynostosis mutation. Two subsequent families then independently confirmed **codon 148 as a recurrent causal locus**: one carrying **p.Pro148Leu** (c.443C>T) and another carrying a different Pro148 substitution.

> *"A c.443C>T missense mutation in MSX2, which predicts p.Pro148Leu was identified and segregated with the disease in all affected family members"* — [PMID: 23949913](https://pubmed.ncbi.nlm.nih.gov/23949913/)

The convergence of three unrelated families on the same codon — the protein's homeodomain DNA-contacting region — is strong evidence that this residue is uniquely sensitive and that the mechanism involves altered DNA-binding behavior rather than simple protein ablation.

### Finding 2 — MSX2 dosage bidirectionally determines skull phenotype: gain causes craniosynostosis, loss causes parietal foramina

This is the cornerstone finding of MSX2 biology. Wilkie et al. (2000) identified heterozygous **loss-of-function** MSX2 lesions — a ~206 kb whole-gene deletion, a homeodomain RK159-160 deletion, and the R172H substitution — in three families with **parietal foramina (PFM)**. The PFM mutant proteins showed **>85% reduction in DNA binding**, in direct contrast to the craniosynostosis-causing P148H, which binds the same DNA target with *enhanced* affinity.

> *"PFM and craniosynostosis result, respectively, from loss and gain of activity in an MSX2-mediated pathway of calvarial osteogenic differentiation"* — [PMID: 10742103](https://pubmed.ncbi.nlm.nih.gov/10742103/)

> *"Mouse Msx2 protein with either of the homeodomain mutations exhibited more than 85% reduction in binding to an optimal Msx2 DNA-binding site"* — [PMID: 10742103](https://pubmed.ncbi.nlm.nih.gov/10742103/)

The dosage model is reinforced from the opposite direction by **copy-number gains**: MSX2 **gene triplication** within a complex 5q35 rearrangement ([PMID: 18000908](https://pubmed.ncbi.nlm.nih.gov/18000908/)) and **intragenic duplication** ([PMID: 24666290](https://pubmed.ncbi.nlm.nih.gov/24666290/)) both cause craniosynostosis — i.e., *more* MSX2 recapitulates the gain-of-function phenotype. Thus a continuous allelic series runs from loss of function (parietal foramina) through normal dosage to gain of function/overdosage (craniosynostosis).

| MSX2 activity | Molecular lesion | Skull phenotype | OMIM |
|---|---|---|---|
| **Gain** | p.Pro148His/Leu; gene duplication/triplication | Craniosynostosis (Boston-type, CRS2) | #604757 |
| Normal | wild-type | Normal calvarial ossification | — |
| **Loss** (haploinsufficiency) | whole-gene deletion; RK159-160del; R172H | Enlarged parietal foramina (PFM) | #168500 |

### Finding 3 — Reciprocal mouse models confirm the dosage mechanism acts through osteoprogenitor proliferation

The dosage model is not merely inferred from human genetics; it is directly demonstrated by two complementary mouse models. Transgenic mice **overexpressing mutant (Boston-type) Msx2** in the developing skull develop **craniosynostosis and ectopic cranial bone**, recapitulating the human gain-of-function phenotype (Liu et al., 1995).

> *"expression of the mouse counterpart of this mutant gene in the developing skulls of transgenic mice causes craniosynostosis and ectopic cranial bone"* — [PMID: 7597092](https://pubmed.ncbi.nlm.nih.gov/7597092/)

Conversely, **Msx2-null mice** show defective skull ossification and persistent calvarial foramina arising from **defective proliferation of osteoprogenitors at the osteogenic front** — phenocopying human MSX2 haploinsufficiency (Satokata et al., 2000).

> *"This phenotype results from defective proliferation of osteoprogenitors at the osteogenic front during calvarial morphogenesis, and closely resembles that associated with human MSX2 haploinsufficiency in parietal foramina"* — [PMID: 10742104](https://pubmed.ncbi.nlm.nih.gov/10742104/)

These models pinpoint the **cellular target** (the osteoprogenitor/pre-osteoblast pool at the osteogenic front of the suture) and the **cellular process** (proliferation and differentiation balance). Calvarial defects in Msx2−/− mice are further enhanced by concurrent Msx1 loss, indicating that **Msx-gene dosage as a family** modifies the phenotype.

### Finding 4 — P148H shows enhanced DNA binding but reduced protein stability; the functional output is context-dependent

The mechanistic picture at the protein level is nuanced. The P148H substitution **increases MSX2 binding affinity** for its DNA response element — the original basis for the gain-of-function hypothesis.

> *"The increased binding affinity of MSX2 (P148H) to the response element has led many to hypothesize that the substitution is a gain-of-function mutation"* — [PMID: 18786927](https://pubmed.ncbi.nlm.nih.gov/18786927/)

However, Yoon et al. (2008) reported that wild-type MSX2 stimulates suture-mesenchyme cell proliferation and cyclin D1, whereas P148H does not. P148H has a **shorter half-life, is more heavily ubiquitylated (via the Praja1 E3 ligase), and is degraded faster**, and it increases ubiquitylation of co-expressed wild-type MSX2 — behaving as a **dominant-negative** in that assay.

> *"The ubiquitylation of Msx2-WT was higher in the presence of Msx2 (P148H), which indicated that P148H functions as a dominant-negative mutant"* — [PMID: 18786927](https://pubmed.ncbi.nlm.nih.gov/18786927/)

The reconciliation is that MSX2 function is **context- and target-dependent**: the mutation can enhance binding/repression at some targets while destabilizing the protein and interfering with wild-type at others. Crucially, the **net human phenotype (craniosynostosis) and the copy-number-gain data both indicate that the pathway output in the suture is one of increased MSX2 activity** — overdosage of MSX2 and P148H converge on the same clinical endpoint.

### Finding 5 — MSX2 acts as a BMP-inducible transcriptional repressor antagonized by DLX5 at osteoblast genes

MSX2 is a **transcriptional repressor** whose activity is finely balanced against the activator DLX5. Msx and Dlx homeoproteins **heterodimerize through their homeodomains**, with dimerization and DNA binding being mutually exclusive, producing reciprocal functional antagonism (Zhang et al., 1997).

> *"Msx proteins act as transcriptional repressors and Dlx proteins act as activators, while in combination, Msx and Dlx proteins counteract each other's transcriptional activities"* — [PMID: 9111364](https://pubmed.ncbi.nlm.nih.gov/9111364/)

At a concrete osteoblast-differentiation target, MSX2 represses the **osteocalcin promoter by ~80%**, and DLX5 completely reverses this repression (Newberry et al., 1998).

> *"Msx2 suppresses transcriptional activity by ca. 80%. However, Dlx5 completely reverses Msx2 repression of the OC promoter"* — [PMID: 9819228](https://pubmed.ncbi.nlm.nih.gov/9819228/)

Upstream, **BMP4 induces Msx2 expression**, placing MSX2 downstream of BMP signaling in the osteogenic program; YY1 can additionally activate Msx2 independent of BMP (Tan et al., 2002).

> *"bone morphogenetic protein type 4 (BMP4) regulates Msx2 expression in embryonic tissues"* — [PMID: 11861914](https://pubmed.ncbi.nlm.nih.gov/11861914/)

### Finding 6 — Clinical spectrum: variable multi-suture involvement, endocranial erosions, mild extracranial features; very rare

Reported families show autosomal dominant inheritance with **highly variable expression and incomplete penetrance**. Affected individuals range from isolated sagittal or unicoronal synostosis to severe trigonocephaly and multi-suture (coronal, sagittal, metopic, lambdoid) fusion. **Multiple endocranial erosions ("digital markings") on CT** are a recurrent diagnostic clue shared with the original family.

> *"our patients share with the original family autosomal dominant inheritance and the presence of multiple endocranial erosions on CT imaging"* — [PMID: 23918290](https://pubmed.ncbi.nlm.nih.gov/23918290/)

Extracranial features include cutaneous syndactyly/minor limb anomalies and refraction errors; MSX2 copy-number gain additionally caused ocular colobomas and microphthalmia-spectrum defects. MSX2 is explicitly described as a **very rare cause** of craniosynostosis — only a handful of families worldwide — against a background craniosynostosis birth prevalence of ~1 in 2,500.

> *"MSX2 mutations are a very rare cause of craniosynostosis"* — [PMID: 24666290](https://pubmed.ncbi.nlm.nih.gov/24666290/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** MSX2-Related (Boston-type) craniosynostosis is an autosomal dominant premature fusion of one or more cranial sutures caused by gain-of-activity variants of the MSX2 homeodomain transcription factor. It is syndromic in that extracranial (limb, ocular) features can occur, but these are typically mild, and intelligence is usually normal.

**Key identifiers:** MONDO:0011481 ("craniosynostosis 2"); OMIM #604757; Orphanet ORPHA:1541; DOID:0061009; GARD 0005538; MedGen/UMLS C1858160 (MedGen UID 346753); SNOMED CT 720817008. ICD-10 maps to Q75.0 (craniosynostosis). MeSH: Craniosynostoses (D003398). Gene: MSX2 — Ensembl ENSG00000120149, NCBI Entrez Gene 4488, HGNC:7392, UniProt P35548, cytoband 5q35.2 (GRCh38 chr5:174,724,551–174,730,896, + strand).

**Synonyms:** craniosynostosis type 2; CRS2; Boston-type craniosynostosis; Warman-Mulliken-Hayward syndrome; craniosynostosis, Warman type.

**Information source:** Aggregated disease-level resources (OMIM, Orphanet, HPO, ClinVar) plus individual family case reports; there is no EHR-scale cohort owing to extreme rarity.

### 2. Etiology

**Causal factors — genetic.** The primary cause is heterozygous gain-of-activity of MSX2: recurrent missense change at codon 148 (p.Pro148His, p.Pro148Leu, other Pro148 substitutions) and copy-number gains (intragenic duplication, 5q35 triplication). There is no known infectious or primary environmental cause.

**Genetic risk factors.** The causal variants themselves are the risk determinant; MSX1/MSX2 gene-family dosage acts as a modifier (mouse data). No common susceptibility loci are implicated in this Mendelian form.

**Environmental risk factors.** None established for the MSX2 form specifically. In craniosynostosis broadly, a population study found **primarily null associations** between maternal periconceptional alcohol and craniosynostosis ([PMID: 39665132](https://pubmed.ncbi.nlm.nih.gov/39665132/)) — not specific to MSX2.

**Protective factors / gene-environment interactions.** None documented for this disorder. Information not available.

### 3. Phenotypes

The official HPO annotation set for OMIM:604757 comprises **22 terms** (JAX/HPO annotation). Characteristic features:

| Phenotype | HPO term | Notes |
|---|---|---|
| Craniosynostosis | HP:0001363 | Core feature; multi-suture common |
| Bicoronal synostosis | HP:0011318 | |
| Unicoronal synostosis | HP:0011315 | |
| Metopic synostosis | HP:0011330 | |
| Trigonocephaly | HP:0000243 | From metopic fusion |
| Turricephaly | HP:0000262 | Tower skull |
| Brachycephaly | HP:0000248 | |
| Frontal bossing | HP:0002007 | |
| Hypotelorism | HP:0000601 | |
| Wormian bones | HP:0002645 | |
| Cleft soft palate | HP:0000185 | |
| Supernumerary tooth | HP:0011069 | |
| Brachydactyly | HP:0001156 | Mild limb/digit anomaly |
| Triphalangeal thumb | HP:0001199 | |
| Myopia | HP:0000545 | Refraction error |
| Hypermetropia | HP:0000540 | |
| Visual field defect | HP:0001123 | |
| Headache | HP:0002315 | Possible raised ICP |
| Seizure | HP:0001250 | |
| Intellectual disability | HP:0001249 | Atypical; intelligence usually normal |
| Infantile onset | HP:0003593 | |
| Autosomal dominant inheritance | HP:0000006 | |

The curated OMIM description adds **turribrachycephaly, cloverleaf skull, supraorbital-ridge hypoplasia, short first metatarsal, and middle phalangeal agenesis of the feet**, with normal intelligence typical. **Onset is congenital/infantile**; severity is **variable** (mild single-suture to severe multi-suture); the suture fusion itself is **stable/non-progressive** once formed, but secondary raised intracranial pressure can progress without surgery. **Quality-of-life impact** derives chiefly from head-shape abnormality, potential raised ICP, and the burden of cranial surgery; treated patients generally have QoL comparable to controls (general NSC data, [PMID: 40210850](https://pubmed.ncbi.nlm.nih.gov/40210850/)).

### 4. Genetic / Molecular Information

**Causal gene:** MSX2 (OMIM *123101; HGNC:7392; Entrez 4488; UniProt P35548), 5q35.2.

**Pathogenic variants.** Recurrent **missense at codon 148**: c.442C>A p.Pro148His (original Boston family), c.443C>T p.Pro148Leu, and a further Pro148 substitution. Also **copy-number gains**: intragenic duplication and 5q35 triplication. ClinVar lists **298 submitted MSX2 variants**, of which **45 Pathogenic and 7 Likely Pathogenic**, spanning both the gain-of-function craniosynostosis and the loss-of-function parietal-foramina allelic disorders. Variant types: **missense** (craniosynostosis, gain of function) and **copy-number gain** (gain of function/overdosage); the allelic PFM disorder involves **whole-gene deletion, in-frame homeodomain deletion, and loss-of-function missense (R172H)**. All reported craniosynostosis variants are **germline**; de novo cases arise but most families show dominant transmission. Population allele frequency in gnomAD is effectively absent for the pathogenic codon-148 changes (private family variants). **Functional consequence:** gain of MSX2 pathway activity (enhanced DNA binding and/or overdosage), with an additional dominant-negative/protein-stability component for P148H.

**Modifier genes:** MSX1 (gene-family dosage modifies calvarial phenotype in mouse); DLX5 (functional antagonist). **Epigenetic information:** none specifically characterized for this disorder. **Chromosomal abnormalities:** 5q35 duplication/triplication within complex rearrangements cause the craniosynostosis phenotype via MSX2 overdosage.

### 5. Environmental Information

No environmental factor, lifestyle factor, or infectious agent is established as a cause or trigger of MSX2-related craniosynostosis. The disorder is monogenic. (General craniosynostosis environmental associations such as maternal alcohol are null/weak and not MSX2-specific.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline **gain-of-activity MSX2 lesion** (p.Pro148His/Leu missense, or gene duplication/triplication) **results in** increased MSX2 pathway activity in cranial-suture mesenchyme — via enhanced DNA-binding affinity (P148H) and/or increased MSX2 gene dosage (CNV).
2. MSX2 sits **downstream of BMP4** signaling (BMP4 induces MSX2; YY1 can also activate it) — so the lesion **amplifies a BMP-driven osteogenic signal** (*inferred for the human mutant; demonstrated that BMP4 regulates Msx2*).
3. Elevated MSX2 **shifts the MSX2↔DLX5 repressor/activator balance** at osteoblast-differentiation genes (e.g., osteocalcin), which MSX2 represses by ~80% and DLX5 reverses — perturbing the timing of osteogenic differentiation at the suture.
4. This **leads to** dysregulated **proliferation and differentiation of osteoprogenitors at the osteogenic front** of the suture (the exact cellular target identified in Msx2 mouse models).
5. Dysregulated osteoprogenitor behavior **results in** premature ossification across the suture — **premature suture fusion (craniosynostosis)** — and, in gain-of-function models, ectopic cranial bone.
6. Fused sutures **constrain calvarial growth perpendicular to the suture**, **leading to** the abnormal head shapes (turribrachycephaly, trigonocephaly, cloverleaf skull) and, where multiple sutures fuse, **raised intracranial pressure**, endocranial erosions ("digital markings"), headache, visual compromise, and (rarely) seizures.

**Branch (opposite dosage):** A *loss-of-function* MSX2 lesion instead **results in** defective osteoprogenitor proliferation at the osteogenic front → deficient parietal ossification → **enlarged parietal foramina** (the reciprocal allelic disorder).

**Pathways/processes/terms.** BMP signaling (upstream); homeodomain transcriptional repression (MSX2) antagonized by DLX5. Cellular processes: **GO:0008284 positive regulation of cell proliferation**, **GO:0001649 osteoblast differentiation**, **GO:0060349 bone morphogenesis**. Cell types: **CL:0007010 preosteoblast / CL:0000062 osteoblast**, cranial neural-crest– and mesoderm–derived **mesenchymal stem cells (CL:0000134)** of the suture. Protein dysfunction: altered DNA-binding and reduced protein stability (enhanced Praja1-mediated ubiquitylation of P148H). No metabolic, immune, or infectious component.

### 7. Anatomical Structures Affected

- **Organ level:** skull/calvaria (primary); brain (secondary, via raised ICP); eye (refraction errors, colobomas with CNVs). Body system: **skeletal (craniofacial)**; secondarily nervous and visual systems.
- **Tissue/cell level:** cranial suture **mesenchyme** and its **osteoprogenitors/osteoblasts** at the osteogenic front; connective/bone tissue.
- **Subcellular:** nucleus (**GO:0005634**) — MSX2 is a nuclear transcription factor acting at target promoters; the ubiquitin-proteasome system governs its turnover.
- **Localization (UBERON):** cranial sutures — **UBERON:0007617 cranial suture**; specific sutures: coronal, sagittal, metopic, lambdoid; parietal bone (**UBERON:0000210**) for the reciprocal PFM disorder. Lateralization: **bilateral or asymmetric** depending on sutures involved (e.g., unicoronal = unilateral).

### 8. Temporal Development

**Onset:** congenital/infantile — suture fusion present at or shortly after birth. **Onset pattern:** chronic developmental (prenatal). **Progression:** the primary suture fusion is essentially **stable once established**, but head-shape deformity and secondary raised ICP can **progress during the period of rapid brain growth** (first 1–2 years), defining the **critical window for surgical intervention** (ideally within the first year; endoscopic repair favored ≤4 months). **Course:** non-episodic; lifelong structural change. **Remission:** only treatment-induced (surgical correction).

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006).
- **Penetrance/expressivity:** incomplete penetrance and highly variable expressivity within families.
- **Epidemiology:** MSX2-related Boston type is **extraordinarily rare** (a handful of families worldwide). Background craniosynostosis birth prevalence is **~1 in 2,500** ([PMID: 36593018](https://pubmed.ncbi.nlm.nih.gov/36593018/)); syndromic forms are ~15% of cases, and MSX2 is a very rare subset of those. Regional incidence data (e.g., Oman 2.5/10,000 live births, male:female ~1.5:1) are for craniosynostosis overall, not MSX2 specifically ([PMID: 39698983](https://pubmed.ncbi.nlm.nih.gov/39698983/)).
- **Anticipation / germline mosaicism / founder effects / consanguinity / carrier frequency:** no evidence of anticipation or founder effects; the private family variants have negligible population allele frequency. Consanguinity is not relevant (dominant). No carrier-frequency estimate applies.
- **Demographics:** no ethnic predilection established given rarity; sex ratio not skewed for the MSX2 form.

### 10. Diagnostics

- **Imaging:** skull **CT with 3D reconstruction** is the diagnostic mainstay — demonstrates fused sutures and the characteristic **multiple endocranial erosions ("digital markings")**; plain radiographs and ultrasound (fontanelle) are adjuncts.
- **Clinical exam:** abnormal head shape (turribrachycephaly, trigonocephaly, cloverleaf), palpable suture ridging, frontal bossing, hypotelorism.
- **Genetic testing:** **single-gene MSX2 sequencing** or inclusion of MSX2 in a **craniosynostosis gene panel** (FGFR1/2/3, TWIST1, MSX2, EFNB1, TCF12, ERF); **chromosomal microarray (CMA)** to detect 5q35 duplication/triplication; WES/WGS for undiagnosed cases. GTR/ClinVar/GeneReviews are primary resources.
- **No laboratory biomarker** (blood/urine/metabolic) exists; diagnosis is radiologic + molecular.
- **Clinical criteria / differential diagnosis:** distinguish from FGFR-related syndromes (Apert, Crouzon, Pfeiffer, Muenke — typically more severe limb/facial features), Saethre-Chotzen (TWIST1), and non-syndromic single-suture synostosis. MSX2 is suggested by AD inheritance, variable multi-suture involvement, mild extracranial features, endocranial erosions, and normal intelligence.
- **Screening:** cascade genetic testing of at-risk relatives once a familial variant is known; prenatal/preimplantation testing is feasible.

### 11. Outcome / Prognosis

- **Survival/mortality:** life expectancy is **normal**; the disorder is not life-limiting. Surgical mortality for craniosynostosis repair is **<1%** ([PMID: 40210850](https://pubmed.ncbi.nlm.nih.gov/40210850/)).
- **Morbidity:** driven by raised ICP (if multi-suture and untreated), visual field defects, headaches, and the morbidity of cranial surgery. Treated patients generally achieve good cosmetic and functional outcomes.
- **Function/QoL:** intelligence typically normal; school-age children with treated non-syndromic craniosynostosis show subtle lower cognitive/behavioral performance on average but patient-reported QoL comparable to controls ([PMID: 40210850](https://pubmed.ncbi.nlm.nih.gov/40210850/)).
- **Complications:** raised intracranial pressure, visual compromise, recurrence requiring reoperation.
- **Prognostic factors:** number of sutures involved and presence/severity of raised ICP; earlier surgery generally yields better morphometric outcomes.

### 12. Treatment

- **Primary treatment is surgical.** Options (from the craniosynostosis literature): **cranial vault remodeling (CVR)**, **fronto-orbital advancement/remodeling**, **endoscope-assisted strip craniectomy/suturectomy with postoperative orthotic (helmet) therapy**, **spring-assisted cranioplasty**, and **distraction osteogenesis** for complex three-dimensional deformities ([PMID: 42686138](https://pubmed.ncbi.nlm.nih.gov/42686138/)). Posterior vault expansion (remodeling, distraction, or spring-assisted) is used for raised ICP in multi-suture disease.
- **Timing:** surgery is ideally in the **first year of life**; early endoscopic repair (≤4 months) yields superior morphometric gains, lower blood loss, and shorter stays ([PMID: 42059979](https://pubmed.ncbi.nlm.nih.gov/42059979/)).
- **NCIT terms:** cranial vault remodeling / craniectomy / fronto-orbital advancement (surgical interventions).
- **Pharmacotherapy / gene therapy / RNA therapy / targeted therapy:** **none** — there is no approved or investigational molecularly targeted drug therapy for MSX2 craniosynostosis.
- **Supportive/rehabilitative:** ophthalmologic management of refraction errors; neurosurgical ICP monitoring; developmental support as needed.

### 13. Prevention

- **Primary prevention:** not possible for a germline monogenic disorder; **genetic counseling** and reproductive options (prenatal diagnosis, preimplantation genetic testing) are the relevant interventions once a familial variant is known.
- **Secondary prevention:** early diagnosis (prenatal imaging/molecular, early infant exam) to enable timely surgery and prevent raised-ICP sequelae.
- **Tertiary prevention:** ICP monitoring and reoperation to prevent neurological/visual complications.
- **Counseling:** autosomal dominant 50% transmission risk; counsel on variable expressivity and incomplete penetrance.

### 14. Other Species / Natural Disease

- **Ortholog:** mouse **Msx2** (NCBI Gene 17702); zebrafish and chick msx orthologs exist. Evolutionary conservation of the homeodomain and of the BMP→Msx→Dlx osteogenic module is high.
- **Natural disease in other species:** no well-characterized spontaneous MSX2 craniosynostosis in companion animals is documented (OMIA). The disease is studied almost exclusively via engineered mouse models (below).
- **Comparative biology:** mouse Msx2 gain- and loss-of-function reproduce human craniosynostosis and parietal foramina respectively, demonstrating strong cross-species mechanistic conservation.

### 15. Model Organisms

- **Mouse (Mus musculus, NCBI Taxon 10090):**
  - **Transgenic Msx2 (Boston-type mutant) overexpression** → craniosynostosis + ectopic cranial bone ([PMID: 7597092](https://pubmed.ncbi.nlm.nih.gov/7597092/)). Models the **gain-of-function** human phenotype well.
  - **Msx2 knockout (Msx2−/−)** → defective skull ossification, persistent calvarial foramina from defective osteoprogenitor proliferation; pleiotropic bone and ectodermal-organ defects ([PMID: 10742104](https://pubmed.ncbi.nlm.nih.gov/10742104/)). Models the **loss-of-function/parietal-foramina** allelic disorder.
  - **Msx1;Msx2 compound mutants** reveal gene-family dosage modification.
- **Phenotype recapitulation:** excellent for the core calvarial dosage phenotype (both directions). **Limitations:** mouse models do not fully capture the variable multi-suture pattern, endocranial erosions, or the human extracranial spectrum; the dominant-negative/protein-stability nuance of P148H is best studied in cell-based assays (Praja1 ubiquitylation, [PMID: 18786927](https://pubmed.ncbi.nlm.nih.gov/18786927/)).
- **Resources:** MGI (Msx2), IMPC/IMSR for alleles; cell-based transfection assays for transcriptional/stability studies.

---

## Mechanistic Model / Interpretation

```
        BMP4  --induces-->  MSX2 (homeodomain repressor)  <--antagonizes-- DLX5 (activator)
                                   |                                 ^
     [YY1 activates MSX2           |  represses osteoblast genes     | heterodimerize via
      independent of BMP]          |  (e.g. osteocalcin ~80%)        | homeodomain (mutually
                                   v                                 | exclusive w/ DNA binding)
                        osteoprogenitors at the
                        OSTEOGENIC FRONT of cranial suture
                                   |
        +--------------------------+---------------------------------+
     GAIN of MSX2 activity                                  LOSS of MSX2 activity
  (P148H enhanced binding;                               (deletion, RK159-160del,
   gene duplication/triplication)                          R172H; >85% down DNA binding)
        |                                                         |
   dysregulated osteoprogenitor                           reduced osteoprogenitor
   proliferation & premature                              proliferation,
   differentiation                                        deficient ossification
        |                                                         |
   PREMATURE SUTURE FUSION + ectopic bone                 ENLARGED PARIETAL
   = CRANIOSYNOSTOSIS (Boston-type, #604757)              FORAMINA (#168500)
        |
   abnormal head shape (turribrachycephaly,
   trigonocephaly, cloverleaf) +/- raised ICP,
   endocranial erosions, visual compromise
```

The unifying interpretation is a **dosage rheostat**: MSX2 activity must be held within a narrow window for normal calvarial ossification. Push it up (missense gain of function or extra gene copies) and sutures fuse too early; push it down (haploinsufficiency) and ossification fails, leaving parietal foramina. P148H is mechanistically subtle — it enhances DNA binding at some targets yet is itself unstable and can act dominant-negatively at others — but the **convergent human genetics (missense + copy-number gain) and reciprocal mouse models place the net suture-level output firmly on the "too much MSX2" side**. The cellular locus of action is the osteoprogenitor pool at the osteogenic front, and the pathway context is BMP4→MSX2⊣(DLX5)→osteoblast-differentiation genes.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [8106171](https://pubmed.ncbi.nlm.nih.gov/8106171/) | Homeodomain MSX2 mutation in AD craniosynostosis | Original P148H discovery (Finding 1) |
| [23949913](https://pubmed.ncbi.nlm.nih.gov/23949913/) | Second mutation (p.Pro148Leu) | Confirms codon 148 recurrence (Finding 1) |
| [23918290](https://pubmed.ncbi.nlm.nih.gov/23918290/) | Second family, clinical-spectrum expansion | Variable expression; endocranial erosions (Finding 6) |
| [10742103](https://pubmed.ncbi.nlm.nih.gov/10742103/) | MSX2 haploinsufficiency → skull defects | Dosage model, >85% down binding (Finding 2) |
| [7597092](https://pubmed.ncbi.nlm.nih.gov/7597092/) | Msx2 transgenic mice | Gain-of-function mouse model (Finding 3) |
| [10742104](https://pubmed.ncbi.nlm.nih.gov/10742104/) | Msx2 knockout mice | Loss-of-function mouse model; osteoprogenitor mechanism (Finding 3) |
| [18786927](https://pubmed.ncbi.nlm.nih.gov/18786927/) | P148H ubiquitin-dependent degradation | Enhanced binding vs reduced stability (Finding 4) |
| [9111364](https://pubmed.ncbi.nlm.nih.gov/9111364/) | Msx/Dlx heterodimerization | MSX2 repressor antagonized by DLX5 (Finding 5) |
| [9819228](https://pubmed.ncbi.nlm.nih.gov/9819228/) | Osteocalcin regulation by Msx2/Dlx5 | ~80% repression, DLX5 reversal (Finding 5) |
| [11861914](https://pubmed.ncbi.nlm.nih.gov/11861914/) | YY1/BMP4 regulation of Msx2 | BMP4 upstream of MSX2 (Finding 5) |
| [24666290](https://pubmed.ncbi.nlm.nih.gov/24666290/) | MSX2 duplication, eye defects | Copy-number gain; rarity (Findings 2, 6) |
| [18000908](https://pubmed.ncbi.nlm.nih.gov/18000908/) | MSX2 triplication (dup5q) | Overdosage → craniosynostosis (Finding 2) |
| [36593018](https://pubmed.ncbi.nlm.nih.gov/36593018/) | Molecular mechanisms review | Background prevalence 1:2,500; MSX2 among key genes |
| [40210850](https://pubmed.ncbi.nlm.nih.gov/40210850/) | Non-syndromic craniosynostosis review | Surgical mortality <1%, QoL, timing |
| [42059979](https://pubmed.ncbi.nlm.nih.gov/42059979/) | Ideal surgical age | Early endoscopic repair window |
| [42686138](https://pubmed.ncbi.nlm.nih.gov/42686138/) | Operative strategy review | Surgical options |
| [10879654](https://pubmed.ncbi.nlm.nih.gov/10879654/) | MSX1/MSX2 craniofacial disorders | Gain vs loss contrast summary |

**Evidence-type mix:** human clinical genetics (family studies, ClinVar), model-organism (mouse transgenic and knockout), in-vitro/cell-based (DNA-binding, ubiquitylation, promoter assays), and computational/database cross-referencing (Ensembl, MyGene, OLS4/MONDO, HPO/JAX).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity:** only a handful of MSX2 craniosynostosis families are reported, so penetrance, expressivity, and genotype-phenotype correlations rest on small numbers; no population-scale natural-history or QoL data specific to MSX2 exist.
2. **Mechanistic ambiguity of P148H:** the coexistence of enhanced DNA binding (gain of function) and reduced protein stability/dominant-negative behavior is not fully resolved; the precise target genes dysregulated in human sutures are not mapped.
3. **No omics in patients:** there are no transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets from MSX2-craniosynostosis patient suture tissue; mechanism is inferred from mouse and cell models.
4. **No targeted therapy or biomarker:** management is purely structural/surgical; no molecular prognostic biomarker exists.
5. **Modifier landscape under-characterized:** beyond MSX1 gene-family dosage (mouse), human modifiers of the variable expressivity are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived models:** generate iPSC-derived cranial neural-crest/osteoprogenitor organoids carrying P148H and MSX2 duplication to directly test proliferation/differentiation output and reconcile the gain-of-function vs dominant-negative debate.
2. **Suture-specific transcriptomics/single-cell:** profile osteogenic-front cells in Msx2-gain and -loss mouse models (and any available patient tissue) to define the dysregulated target-gene program and confirm the BMP4→MSX2⊣DLX5→osteocalcin axis in vivo.
3. **Allelic-series functional assay:** systematically compare DNA binding, protein half-life, Praja1-mediated ubiquitylation, and transcriptional output across P148H, P148L, and other Pro148 substitutions to build a quantitative genotype-function map.
4. **Registry/cascade data collection:** aggregate reported families into a shared registry to refine penetrance/expressivity estimates and endocranial-erosion specificity as a diagnostic marker.
5. **Therapeutic exploration:** test whether modulating BMP signaling or MSX2 stability (proteasome pathway) alters suture fusion in the transgenic mouse — a first step toward any non-surgical intervention.

---

*Report prepared from 9 confirmed findings across 5 iterations and 32 reviewed papers. All mechanistic and clinical claims are cited to primary literature by PMID; ontology terms (HPO, GO, CL, UBERON, MONDO) are suggested throughout for knowledge-base annotation.*


## Artifacts

- [OpenScientist final report](MSX2-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MSX2-Related_Craniosynostosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 23 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 0 |

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000006` - called "Autosomal dominant inheritance", "Inheritance:** autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

33 of 36 terms resolved to a current term; the rest could not be looked up either way.