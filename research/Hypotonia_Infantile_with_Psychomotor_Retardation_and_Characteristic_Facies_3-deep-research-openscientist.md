---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T09:19:22.164103'
end_time: '2026-08-19T09:35:14.467496'
duration_seconds: 952.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypotonia, Infantile, with Psychomotor Retardation and Characteristic
    Facies 3
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
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42563865
  relevance_assessed: 20
  on_topic: 17
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypotonia_Infantile_with_Psychomotor_Retardation_and_Characteristic_Facies_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypotonia_Infantile_with_Psychomotor_Retardation_and_Characteristic_Facies_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3** covering all of the
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

# Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 3 (IHPRF3 / TBCK-Related Encephaloneuropathy)

## Summary (Answer to the Research Question)

**Infantile Hypotonia with Psychomotor Retardation and Characteristic Facies-3 (IHPRF3; OMIM #616900)** is an ultrarare **autosomal recessive** neurodevelopmental and **progressive neurodegenerative** disorder caused by **biallelic loss-of-function variants in *TBCK*** (TBC1-domain-containing kinase, chromosome 4q24). Affected children present in infancy with **profound hypotonia, global developmental delay/severe intellectual disability, epilepsy, characteristic (often coarsening) facial dysmorphism, and brain atrophy/white-matter changes**, frequently progressing to a lysosomal-storage-like neurodegenerative course with lipofuscin accumulation (proposed neuronal ceroid lipofuscinosis subtype **CLN15**). Mechanistically, TBCK loss **downregulates mTOR (mTORC1) signaling** and disrupts **RAB5-dependent endolysosomal trafficking and autophagy**; because mTOR remains responsive to exogenous **L-leucine**, leucine supplementation has been proposed as a candidate directed therapy, though care remains largely supportive.

*Evidence base: This report synthesizes human clinical case series/cohorts, patient-derived iPSC/neuroprogenitor studies, and neuropathology. No experimental data files were provided; all content is literature-derived.*

---

## 1. Disease Information

- **Overview:** A severe childhood-onset encephaloneuropathy characterized by infantile hypotonia, psychomotor/developmental delay, intellectual disability, epilepsy, and characteristic facies, with progressive CNS deterioration. Also termed **TBCK deficiency disorder (TBCK-DD)** or **TBCK-related encephaloneuropathy**.
- **Key identifiers:**
  - **OMIM:** #616900 (phenotype); *TBCK* gene OMIM *616899*.
  - **Mondo:** MONDO:0014635 (Hypotonia, infantile, with psychomotor retardation and characteristic facies 3).
  - **Orphanet:** ORPHA:494526 (TBCK-related intellectual disability syndrome).
  - **ICD-10:** best mapped to G71.2/Q87-range congenital/neuromuscular categories; **ICD-11:** LD24 / 8C (no specific code).
  - **MeSH:** no dedicated term; indexed under *Muscle Hypotonia*, *Intellectual Disability*, *Neurodevelopmental Disorders*.
  - **HGNC:** *TBCK* (HGNC:28348).
- **Synonyms:** IHPRF3; TBCK syndrome; TBCK deficiency disorder; TBCK-related encephaloneuropathy; hypotonia, infantile, with psychomotor retardation and characteristic facies-3; (proposed) neuronal ceroid lipofuscinosis type 15 / CLN15.
- **Data source type:** Aggregated disease-level knowledge derived from **individual patient reports and small cohorts** (WES-diagnosed families) — not EHR-scale datasets. The founding description reported 13 individuals from 9 families (PMID 27040691); a 2019 review compiled 33 cases (PMID 30103036).

## 2. Etiology

- **Primary cause (genetic):** Biallelic (homozygous or compound heterozygous) pathogenic variants in ***TBCK***. *"13 individuals from nine unrelated families and affected by likely pathogenic biallelic variants in TBC1-domain-containing kinase (TBCK) were identified through whole-exome sequencing"* (PMID 27040691). Autosomal recessive: *"an autosomal recessive disorder caused by biallelic pathogenic variants of the TBCK gene"* (PMID 36273129).
- **Genetic risk factors:** The disease is monogenic/Mendelian; the sole causal locus is *TBCK*. **Consanguinity** substantially increases risk (multiple homozygous cases in consanguineous/first-cousin unions, e.g., PMID 39865381). No established modifier genes; genotype–phenotype correlation is imperfect (PMID 32363625).
- **Environmental risk factors:** None established. Onset is congenital/genetic; no toxin, infectious, or lifestyle trigger is implicated.
- **Protective factors:** None specifically identified. In carriers, a single functional *TBCK* allele is sufficient (parents asymptomatic, PMID 36273129).
- **Gene–environment interactions:** The only therapeutically relevant "environmental" modifier is **dietary L-leucine**, which can reactivate residual mTOR signaling (PMID 27040691) — an interaction exploited for potential treatment rather than a disease cause.

## 3. Phenotypes

Core phenotypes (with suggested HPO terms, typical onset, and qualitative frequency):

| Phenotype | Type | HPO term | Onset | Frequency |
|---|---|---|---|---|
| Profound/generalized hypotonia | Clinical sign | HP:0001290 / HP:0001252 | Neonatal–infantile | Nearly all (~100%) |
| Global developmental delay | Sign | HP:0001263 | Infantile | ~100% |
| Intellectual disability (often severe/profound) | Sign | HP:0001249 / HP:0010864 | Childhood | ~100% |
| Seizures / epilepsy | Sign | HP:0001250 | Infancy–childhood | Common (majority) |
| Facial dysmorphism (coarse, hypertelorism, tented upper lip, exaggerated Cupid's bow, macroglossia, arched eyebrows) | Physical | HP:0000271, HP:0000316, HP:0000219, HP:0000158, HP:0002553 | Progressive (coarsening with age) | Variable–common |
| Brain atrophy / white-matter changes | Lab/imaging | HP:0002059 / HP:0002500 | Childhood | Common |
| Corpus callosum agenesis/hypoplasia | Imaging | HP:0001274 | Congenital | Occasional |
| Respiratory insufficiency / recurrent infections | Sign | HP:0002093 | Progressive | Common (major cause of death) |
| Myopathic changes on biopsy | Lab | HP:0003198 | Variable | Reported subset |
| Cardiac malformations (ToF, aortic arch anomalies) | Sign | HP:0001631 / HP:0001647 | Congenital | Rare/emerging |
| Feeding difficulties / failure to thrive | Sign | HP:0011968 / HP:0001508 | Infantile | Common |

- **Severity:** Severe to profound; variable across variants. Older children may develop coarse, storage-disorder-like features (PMID 27040691).
- **Progression:** **Progressive/neurodegenerative** — *"pathogenic mutations of the said gene lead to a progressive neurodegenerative disease"* (PMID 30103036).
- **Quality-of-life impact:** Severe — most affected individuals are non-ambulatory, nonverbal, dependent for all activities of daily living, often requiring gastrostomy feeding and respiratory support.

## 4. Genetic / Molecular Information

- **Causal gene:** ***TBCK*** (TBC1-domain-containing kinase), 4q24; HGNC:28348; encodes a protein with **three conserved domains — an N-terminal Ser/Thr (pseudo)kinase domain, a central TBC (Rab-GAP) domain, and a C-terminal rhodanese-homology domain (RHOD)** — with long and short isoforms generated by alternative splicing (PMID 33240423). Biochemical study of purified full-length protein confirms TBCK is a **catalytically inactive class I pseudokinase** lacking canonical VAIK/HRD/DFG motifs and nucleotide binding (PMID 42546825).
- **Representative pathogenic variants (ClinVar/literature):**
  - c.247C>T, **p.Arg83Ter** (nonsense) — novel in a Chinese patient (PMID 36273129).
  - **p.Gln164\*** (nonsense, exon 6) — LOF (PMID 37876076).
  - c.753dup, **p.Lys252\*** (frameshift/truncating) (PMID 30103036).
  - **c.1532G>A** (missense) — recurrent; associated with cardiac involvement (PMID 39865381).
  - Early truncating variant with **complete absence of TBCK protein** and myopathy (PMID 32363625).
  - **c.376C>T, p.Arg126\* (p.R126X)** — recurrent **founder** stop-gain variant predominating in individuals of **Puerto Rican/"Boricua" ancestry**; defines "TBCK-encephaloneuropathy / Boricua syndrome" (PMID 42563865).
- **Variant classification:** Pathogenic/likely pathogenic per ACMG/AMP (PMID 36273129). **Variant types:** predominantly nonsense, frameshift, splice, and structural/duplication (LOF); some missense. **Functional consequence:** **loss of function** — *"TBCK was absent in cells from affected individuals"* (PMID 27040691).
- **Allele frequency (gnomAD v4, this analysis):** Individual pathogenic alleles are ultrarare. Most pathogenic truncating variants have exome AF <1e-5 (often singletons or absent). The **founder p.Arg126\* (c.376C>T; 4-106262103-G-A)** is the most enriched pathogenic LoF allele: **exome AF ≈ 6.0×10⁻⁵ (1/16,569 alleles); genome AF ≈ 2.4×10⁻⁴ (1/4,209 alleles)**, the higher genome frequency reflecting over-representation in admixed/Latino samples. Historical: c.247C>T ~8.2×10⁻⁶ in ExAC (PMID 36273129).
- **Gene constraint (gnomAD v4):** *TBCK* is **loss-of-function tolerant** — pLI ≈ 0, oe_lof = 0.87 (90% CI 0.74–1.03; LOEUF ~1.03) — consistent with recessive inheritance in which heterozygous carriers are largely unaffected.
- **Allelic architecture:** ClinVar lists **882 TBCK variants**; pathogenic truncating alleles are **distributed across the gene (marked allelic heterogeneity)** with no mutational hotspot other than the Puerto Rican founder allele.
- **Somatic vs germline:** **Germline**, biallelic.
- **Modifier genes:** None validated. Functional partners **PPP1R21** and **FERRY3/C12orf4** form a complex with TBCK (PMID 41789809) and are candidate biology-level modifiers.
- **Epigenetics/chromosomal abnormalities:** No specific methylation signature or recurrent chromosomal aberration; chromosomal microarray is typically normal aside from runs of homozygosity in consanguineous families (PMID 39865381).

**Suggested ontology terms:** Gene — *TBCK* (HGNC:28348); MONDO:0014635.

## 5. Environmental Information

- **Environmental factors:** None causative. **Infectious agents:** none. **Lifestyle factors:** not applicable to disease causation. The only relevant environmental/nutritional variable is **L-leucine** as a candidate therapeutic modulator (PMID 27040691).

## 6. Mechanism / Pathophysiology

- **Molecular pathways:** **mTOR / mTORC1 signaling** — TBCK normally supports mTOR activity; its loss reduces downstream signaling, evidenced by **decreased phospho-S6**: *"decreased phosphorylation of phospho-ribosomal protein S6 was also observed, a finding suggestive of downregulation of mTOR signaling"* (PMID 27040691). TBCK also acts as a **RAB5-GAP** within the **TBCK–PPP1R21–FERRY3/C12orf4 complex** governing endo-lysosomal homeostasis (PMID 41789809).
- **Cellular processes:** Impaired **ER-to-Golgi vesicle transport, autophagosome biogenesis, cell-cycle progression, and cell migration** in patient iNPCs: *"Lack of functional TBCK protein in iNPC is associated with impaired endoplasmic reticulum-to-Golgi vesicle transport and autophagosome biogenesis, as well as altered cell cycle progression and severe impairment in the capacity of migration"* (PMID 35095425). Dysregulated **autophagy–lysosome** flux (enhanced mTORC1-mediated autophagosome formation with reduced Rab-mediated autophagosome–lysosome fusion) drives storage (PMID 30591081).
- **Protein dysfunction:** Loss of function / absent protein; TBCK's Rab-GAP and scaffolding roles are lost.
- **Metabolic/storage changes:** **Lipofuscin and carbohydrate-rich storage material** accumulate — *"a widespread and massive accumulation of lipofuscin storage material in neurons of the central nervous system"* (PMID 30591081). **Lysosomal dysfunction impairs mitochondrial quality control**, contributing to neurodegeneration (PMID 34816123).
- **RNA/ribosomal dysregulation:** Multi-omics of TBCK-deficient cells shows **altered ribosomal function, RNA splicing, and miRNA networks** (PMID 41040160); patient-derived neurons exhibit **compartment-specific mRNA and lysosomal trafficking defects** (PMID 40093117), consistent with a role in RNA transport.
- **Immune involvement:** Not a primary feature; **vacuolated lymphocytes** are a storage marker (PMID 30591081).
- **Tissue damage mechanism:** Progressive intraneuronal storage and impaired neurogenesis/neuronal migration → neurodevelopmental deficit plus neurodegeneration.
- **Causal chain:** Biallelic *TBCK* LOF → loss of Rab5-GAP activity + reduced mTORC1 (↓pS6) → defective endolysosomal trafficking, secretory transport, and autophagosome–lysosome fusion → lipofuscin/carbohydrate storage + impaired neuroprogenitor proliferation/migration → hypotonia, developmental delay, and progressive neurodegeneration. **Upstream:** *TBCK* loss; **downstream:** mTOR, RAB5/autophagy, storage accumulation, neuronal dysfunction.

**Suggested ontology terms:** GO:0031929 (TOR signaling); GO:0006914 (autophagy); GO:0016197 (endosomal transport); GO:0005096 (GTPase activator activity); GO:0006888 (ER-to-Golgi vesicle transport); CL:0000031 (neuroblast/neural progenitor), CL:0000540 (neuron), CL:0000127 (astrocyte).

## 7. Anatomical Structures Affected

- **Organ level:** **Central nervous system** (primary) — cerebral cortex, white matter, ventricles, corpus callosum; **skeletal muscle** (secondary myopathy); **heart** (rare malformations); systemic storage in **spleen and liver** (PMID 30591081). Body systems: nervous, musculoskeletal, occasionally cardiovascular, and respiratory (secondary).
- **Tissue/cell level:** **Neurons** (lipofuscin storage), **astrocytes** (storage), lymphocytes (vacuolation); neural progenitor cells (migration/proliferation defects).
- **Subcellular level:** **Lysosome/autophagosome** (GO:0005764, GO:0005776), **endoplasmic reticulum & Golgi** (GO:0005783, GO:0005794), **endosome** (GO:0005768).
- **Localization/lateralization:** **Bilateral, diffuse** CNS involvement (ventriculomegaly, widened subarachnoid space, atrophy, white-matter changes) (PMID 36273129).

**Suggested UBERON terms:** UBERON:0000955 (brain); UBERON:0002316 (white matter); UBERON:0001851 (cortex); UBERON:0002037 (cerebellum); UBERON:0001134 (skeletal muscle tissue).

## 8. Temporal Development

- **Onset:** Congenital/**infantile** — hypotonia and delay evident in early infancy.
- **Onset pattern:** Insidious/chronic; developmental delay recognized within the first months to ~15 months (PMID 36273129).
- **Progression:** **Progressive neurodegenerative** course (PMID 30103036); older children develop coarsening facies and storage features (PMID 27040691). Course is generally slowly progressive with variable rate; severe forms cause **premature death** (PMID 30591081).
- **Duration:** Chronic, lifelong; substantially shortened life expectancy in severe cases.
- **Critical periods:** Early neurodevelopmental window (neurogenesis/migration) is central; any mTOR-directed intervention would plausibly need to be early, though efficacy is unproven.

## 9. Inheritance and Population

- **Epidemiology:** **Ultrarare**; only tens of cases reported worldwide (33 reviewed by 2019, PMID 30103036). No reliable prevalence/incidence estimates; Orphanet classifies prevalence as <1/1,000,000.
- **Inheritance:** **Autosomal recessive** (PMID 36273129). **Penetrance:** essentially complete in biallelic LOF. **Expressivity:** variable (severity, muscle, cardiac, imaging features). **Heterozygotes:** population-level gnomAD data show LoF tolerance (LOEUF ~1), yet targeted study reports a *mild* neurologic syndrome in some human and mouse heterozygotes (PMID 37353954) — i.e., largely recessive with a subtle possible dosage effect. No anticipation (not a repeat-expansion disorder).
- **Consanguinity:** Strong contributor — multiple homozygous cases in consanguineous families (PMID 39865381). **Founder effect (quantified, gnomAD v4 + 1000 Genomes, this analysis):** the p.Arg126\* allele (rs575822089) is **~45× enriched in Admixed American/Latino** samples (AMR genome AF 1.97×10⁻³, carrier ~1/253) vs Non-Finnish European (AF 4.4×10⁻⁵), and reaches **AF ≈ 1.0×10⁻² in 1000 Genomes Puerto Ricans (carrier ~1/49)** — a strong "Boricua syndrome" founder signal (PMID 42563865). The allele is essentially absent in African, East Asian, South Asian, Finnish, Ashkenazi Jewish, and Middle Eastern groups, and **no homozygotes** are seen in gnomAD (consistent with a severe recessive phenotype). **Carrier frequency** for TBCK deficiency overall is low in general (non-founder) populations, consistent with the ultrarare, mostly private pathogenic alleles.
- **Demographics:** Originally reported mainly in individuals of European ancestry; subsequently described across populations including the **first non-Caucasian (Chinese) patient** (PMID 36273129), broadening geographic distribution. A pronounced **founder effect in Puerto Rico/Latino (AMR) populations** (p.R126*, ~45× enriched vs NFE; PUR carrier ~1/49) concentrates cases in the **Boricua** population, where prevalence may be higher than expected (4 diagnoses in 6 months at one center; PMID 42563865). Consanguineous populations (e.g., Middle East, South Asia) are also enriched via private homozygous alleles. No strong sex bias (autosomal); age distribution centers on infants/children.

## 10. Diagnostics

- **Genetic testing (definitive):** **Whole-exome sequencing** is the primary diagnostic route (PMID 27040691, PMID 39865381); WGS, multigene hypotonia/neurodevelopmental panels including *TBCK*, or targeted single-gene testing (e.g., for known founder variants) are alternatives. Chromosomal microarray is typically normal (may show runs of homozygosity) (PMID 39865381). Variants classified per **ACMG/AMP** (PMID 36273129).
- **Biochemical/functional:** Absent TBCK protein and **reduced phospho-S6** on Western blot in patient cells (research assay; PMID 27040691). **Vacuolated lymphocytes** and tissue storage material on biopsy support a storage phenotype (PMID 30591081). Muscle biopsy may show **nonspecific myopathic changes** (PMID 32363625).
- **Imaging:** Brain **MRI** — cerebral/cerebellar atrophy, white-matter changes, ventriculomegaly, widened subarachnoid space, occasional corpus callosum agenesis (PMID 27040691, PMID 36273129, PMID 39865381), and characteristically **periventricular leukomalacia (PVL)-like changes** in the absence of prematurity — a diagnostic clue prompting *TBCK* testing (PMID 36522252).
- **RNA-seq diagnostics:** Transcriptome sequencing (fibroblasts > blood) can diagnose TBCK-associated encephalopathy missed by conventional ES/CMA (PMID 33001864). Fetal echocardiography/ultrasound may detect cardiac anomalies and cystic hygroma in affected pregnancies (PMID 39865381).
- **Clinical criteria / differential diagnosis:** No formal criteria; diagnosis is molecular. **Differentials:** other causes of infantile hypotonia with DD/ID and coarse facies — lysosomal storage disorders (mucopolysaccharidoses, NCLs), congenital myopathies, other IHPRF forms (**IHPRF1/NALCN, IHPRF2/UNC80**), Prader-Willi, congenital disorders of glycosylation, and mitochondrial disease. Storage-disease workup is typically negative except for TBCK (PMID 30591081).
- **Screening:** Not part of standard newborn screening. **Carrier/cascade screening** and **prenatal/preimplantation genetic testing** are informative in known families (utilized for prenatal diagnosis in PMID 39865381).

## 11. Outcome / Prognosis

- **Survival/mortality:** Guarded; severe forms feature **premature death** (PMID 30591081), commonly from **respiratory failure/recurrent infections** related to hypotonia and neurodegeneration. **Central hypoventilation/respiratory insufficiency is a major, under-recognized complication** — 5/6 in one cohort required respiratory support (PMID 36522252), warranting early respiratory surveillance. No formal survival statistics exist given rarity.
- **Morbidity/function:** Profound disability — most patients are non-ambulatory, nonverbal, and fully dependent, often requiring feeding-tube and respiratory support.
- **Disease course:** Progressive; complications include epilepsy, scoliosis, contractures, aspiration, feeding failure, and infections.
- **Prognostic factors:** Variant severity (complete LOF/absent protein associated with severe multisystem presentations, e.g., myopathy PMID 32363625; cardiac malformation with c.1532G>A, PMID 39865381). Neurorehabilitation showed limited benefit in a reported case (PMID 36273129).

## 12. Treatment

- **No approved disease-modifying therapy.** Management is **supportive and multidisciplinary** (PMID 37876076): antiseizure medications for epilepsy, physical/occupational/speech therapy, nutritional support (gastrostomy), respiratory care, orthopedic management of scoliosis/contractures.
- **Candidate directed therapy — L-leucine:** Rationale from retained mTOR responsiveness — *"activation of the mTOR pathway in response to L-leucine supplementation was retained, suggesting a possible avenue for directed therapies for this condition"* (PMID 27040691). Efficacy remains unproven clinically.
- **Rehabilitation:** Neurorehabilitation training reported with poor response in at least one case (PMID 36273129).
- **Experimental/future:** mTOR-pathway modulation and endolysosomal/autophagy-targeted approaches are conceptually motivated by the RAB5-GAP/FERRY complex biology (PMID 41789809); no registered disease-specific trials established. **Genetic counseling** and reproductive options are central to family management.

**Suggested NCIT terms:** Supportive Care; Anticonvulsant Therapy; Physical Therapy; Nutritional Support; Leucine (dietary supplement). **CHEBI:** L-leucine (CHEBI:15603); sirolimus/rapamycin (CHEBI:9168) is conceptually contraindicated as an mTOR inhibitor given baseline mTORC1 downregulation.

## 13. Prevention

- **Primary prevention:** Not applicable (monogenic). **Genetic counseling** for at-risk (especially consanguineous) families; 25% recurrence risk per pregnancy for carrier couples.
- **Reproductive/secondary prevention:** **Carrier screening**, **prenatal diagnosis**, and **preimplantation genetic testing** in known families (demonstrated prenatally in PMID 39865381). **Cascade testing** of relatives. **Population-targeted carrier screening** for the p.Arg126\* founder allele is high-yield in individuals of Puerto Rican/Latino ancestry (PUR carrier frequency ~1/49; this analysis, PMID 42563865), and equitable access to genetic testing improves ascertainment (PMID 42563865).
- **Tertiary prevention:** Anticipatory management of seizures, aspiration/respiratory infections, feeding difficulties, and orthopedic complications to reduce morbidity.

## 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *TBCK* is conserved across vertebrates — human (NCBI Taxon 9606), mouse *Tbck* (NCBI Taxon 10090, Gene ID 271981), zebrafish *tbck* (NCBI Taxon 7955). Functional conservation demonstrated: mouse *Tbck* loss causes leukoencephalopathy (PMID 42182390) and zebrafish *tbck* is required for heart development (PMID 36574072).
- **Natural disease in animals:** No well-characterized naturally occurring animal counterpart is established in OMIA; the disorder is defined in humans and studied via engineered models.
- **Comparative biology:** Evolutionary conservation of the TBC (Rab-GAP), rhodanese, and pseudokinase domains supports cross-species modeling; heterozygous phenotypes are conserved between mice and humans (PMID 37353954). **Zoonotic potential:** none (non-infectious, genetic).

## 15. Model Organisms

- **Human cellular models:** **Patient-derived iPSCs → induced neuroprogenitor cells (iNPCs)** demonstrate impaired ER-to-Golgi transport, autophagosome biogenesis, cell-cycle, and migration (PMID 35095425). Patient-derived neurons show compartment-specific mRNA and lysosomal trafficking defects (PMID 40093117); patient fibroblasts/lymphoblasts show absent TBCK, reduced pS6, and autophagic vesicle accumulation (PMID 27040691, 42563865). Multi-omics in patient cells reveal ribosomal/RNA-splicing/miRNA dysregulation (PMID 41040160).
- **Mouse models (mammalian):** A **novel mouse model of TBCK Syndrome** recapitulates a **degenerative leukoencephalopathy with multisystem involvement**, including neurodevelopmental, **craniofacial, and pulmonary** features and a unique enamel/dentin/alveolar-bone **mineralization** defect (PMID 42182390, 41756984). **Heterozygous (haploinsufficient)** *Tbck* variants cause a **mild neurologic syndrome in both mice and humans** (PMID 37353954) — relevant to carrier counseling.
- **Zebrafish (invertebrate/vertebrate screen):** *tbck* knockdown identified it as **essential for heart development (atrioventricular canal formation)** (PMID 36574072), providing a mechanistic basis for the emerging human cardiac phenotype.
- **Phenotype recapitulation:** Mouse models capture CNS leukoencephalopathy, craniofacial, and pulmonary components with good face validity; zebrafish captures cardiac requirement.
- **Limitations:** Cellular models incompletely capture progressive in vivo neurodegeneration; cross-species differences in lifespan/lysosomal storage may limit modeling of the human storage/CLN15 phenotype.
- **Resources:** MGI (mouse *Tbck*), ZFIN (zebrafish *tbck*); NCBI Gene orthologs — mouse *Tbck* (Gene ID 271981), zebrafish *tbck*.

---

## Supported vs. Refuted Hypotheses

**Supported:**
1. IHPRF3 is autosomal recessive, caused by biallelic LOF in *TBCK* (PMID 27040691, 36273129).
2. Pathophysiology involves mTOR downregulation plus RAB5/endolysosomal–autophagy dysfunction (PMID 27040691, 35095425, 41789809).
3. The disorder is progressive/neurodegenerative with lysosomal storage (lipofuscin; proposed CLN15) (PMID 30591081, 30103036).
4. The phenotype extends beyond CNS to muscle and (rarely) heart (PMID 32363625, 39865381).
5. Residual mTOR responsiveness to L-leucine offers a therapeutic rationale (PMID 27040691).

**Refuted / not supported:**
- Hypotonia is *purely* neurogenic — refuted; primary muscle disease can contribute (PMID 32363625).
- It is a classical single-substrate lysosomal storage disease — refuted; >20 known LSDs excluded, storage is heterogeneous (PMID 30591081).

## Limitations and Future Directions

- **Rarity:** Only tens of cases; no robust prevalence, survival, or genotype–phenotype statistics.
- **Therapeutics:** Leucine benefit is theoretical; no controlled trials. Need for validated in vivo models and natural-history studies.
- **Mechanism:** Relationship between mTOR downregulation and endolysosomal/RAB5 dysfunction (upstream vs. parallel) requires clarification (PMID 35095425, 41789809).
- **Diagnosis:** Broader awareness needed so hypotonia + coarse facies + storage-negative workup prompts *TBCK* sequencing.

### Key References (PMID)
27040691 (Bhoj 2016, foundational cohort & mTOR/leucine); 30591081 (Beck-Wödl 2018, CLN15/storage neuropathology); 30103036 (Zapata-Aldana 2019, 33-case review, progressive neurodegeneration); 35095425 (Moreira 2021, iNPC secretory/autophagy defects); 32363625 (Saredi 2020, myopathy); 36273129 (Tan 2022, first non-Caucasian case, ACMG); 37876076 (Chand 2023, LOF nonsense case); 39865381 (Mastromoro 2025, cardiac involvement, prenatal); 41789809 (Chen 2026, TBCK–PPP1R21–FERRY3 RAB5-GAP complex); 42563865 (De Luca-Ramirez 2023, Puerto Rican p.R126*/Boricua founder); 36522252 (Sabanathan 2023, hypoventilation & PVL-like MRI); 33240423 (Wu 2021, three-domain structure/isoforms); 42546825 (Maurya 2026, class I pseudokinase); 34816123 (Tintos-Hernández 2021, lysosomal–mitochondrial quality control); 41040160 (Diaz-Rosado 2025, ribosome/RNA-splicing/miRNA multi-omics); 40093117 (Flores-Mendez 2025, mRNA & lysosomal trafficking in patient neurons); 37353954 (Nair 2023, heterozygote mild syndrome, mouse); 42182390 (Melendez-Perez 2026, mouse model); 41756984 (Katsura 2026, mouse mineralization/leukoencephalopathy); 36574072 (Ma 2022, zebrafish tbck heart development); 33001864 (Murdock 2021, RNA-seq diagnostics).


## Artifacts

- [OpenScientist final report](Hypotonia_Infantile_with_Psychomotor_Retardation_and_Characteristic_Facies_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypotonia_Infantile_with_Psychomotor_Retardation_and_Characteristic_Facies_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 20 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42563865` *(abstract only)*: "TBCK-encephaloneuropathy / Boricua syndrome"
  - Text part not found as substring: 'TBCK-encephaloneuropathy / Boricua syndrome' (note: only abstract available for PMID:42563865, full text may contain this excerpt)