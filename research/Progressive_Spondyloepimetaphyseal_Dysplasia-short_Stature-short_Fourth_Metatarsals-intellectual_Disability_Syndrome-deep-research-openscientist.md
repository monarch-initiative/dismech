---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-20T07:16:34.750150'
end_time: '2026-08-20T07:30:51.651034'
duration_seconds: 856.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth
    Metatarsals-intellectual Disability Syndrome
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
citation_count: 5
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:30063090
  relevance_assessed: 6
  on_topic: 6
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Progressive_Spondyloepimetaphyseal_Dysplasia-short_Stature-short_Fourth_Metatarsals-intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Spondyloepimetaphyseal_Dysplasia-short_Stature-short_Fourth_Metatarsals-intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth Metatarsals-intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth Metatarsals-intellectual Disability Syndrome** covering all of the
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

# Spondyloepimetaphyseal Dysplasia, Faden–Alkuraya Type (SEMD-FADA / RSPRY1): Comprehensive Disease Characterization

## Summary

**Progressive Spondyloepimetaphyseal Dysplasia–Short Stature–Short Fourth Metatarsals–Intellectual Disability Syndrome** is the descriptive Orphanet name for **Spondyloepimetaphyseal Dysplasia, Faden–Alkuraya type (SEMD-FADA)**, an ultra-rare autosomal-recessive skeletal dysplasia. It is catalogued as **OMIM #616723**, **Orphanet ORPHA:457395**, and **GARD 17808**. The disorder is caused by **biallelic loss-of-function variants in *RSPRY1*** (ring finger and SPRY domain–containing protein 1), a 576–amino-acid protein encoded on chromosome **16q13** that contains a C3HC4-type (RING) zinc-finger and a SPRY domain. First delineated by Faden and colleagues in 2015 through combined autozygome/exome analysis of a consanguineous Saudi family, the condition has since been reported in additional families from Saudi Arabia, Peru, Turkey, and India, establishing both allelic and phenotypic heterogeneity.

The **core clinical phenotype** comprises progressive spondyloepimetaphyseal dysplasia, disproportionate short stature, short fourth metatarsals, facial dysmorphism, and intellectual disability. The expanded skeletal spectrum includes mild spondylar (vertebral) dysplasia with platyspondyly and vertebral wedging, epimetaphyseal dysplasia of the long bones with **coxa vara** and **genu valgum**, brachymesophalangy with cone-shaped epiphyses (cono-brachydactyly), **craniosynostosis**, slipped capital femoral epiphyses, scoliosis, pes planus, and joint dislocation. Neurodevelopmental involvement (intellectual disability, developmental delay, hypotonia) is variable, and at least one proband showed **progressive loss of ambulation** leading to wheelchair dependence.

Mechanistically, RSPRY1 acts as a negative regulator of **TGF-β/SMAD signaling** during endochondral ossification. Loss of RSPRY1 produces **constitutive, SMAD3-dependent activation** of the TGF-β pathway with downstream dysregulation of extracellular-matrix (ECM) genes, disrupting the tightly balanced growth-factor signaling required for orderly bone formation. The protein is expressed predominantly in **osteoblasts, osteocytes, and periosteal/perichondrial cells** (with minimal chondrocyte expression), explaining the endochondral bone phenotype. No disease-specific or curative therapy exists; management is supportive and multidisciplinary. This report synthesizes seven confirmed findings across five investigation iterations, drawing on six primary papers.

---

## Key Findings

### Finding 1 — SEMD-FADA is caused by biallelic loss-of-function *RSPRY1* variants (autosomal recessive)

The genetic basis of the disease was established by **combined autozygome/exome analysis** of four affected siblings from a consanguineous Saudi family, which identified a **homozygous frameshift mutation in *RSPRY1* undergoing nonsense-mediated decay (NMD)**. A simplex case from Peru carried a homozygous likely-pathogenic missense variant in the same gene, confirming allelic causation ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

> "Combined autozygome/exome analysis identified a homozygous frameshift mutation in RSPRY1 with resulting nonsense-mediated decay." — [PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)

Two additional families subsequently broadened the allelic spectrum, harbouring a homozygous **c.377delT (p.Ile126fs\*)** frameshift in exon 2 and a homozygous **splice-site c.516+2T>A** variant at the exon 4/intron 4 boundary ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)).

> "Whole exome sequencing revealed a novel homozygous [c.377delT] [p.Ile126fs\*] frameshift mutation at exon 2 in one family, while Sanger sequencing revealed a novel homozygous splice site mutation [c.516+2T>A] at exon 4/intron 4 border of RSPRY1 in the other family." — [PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)

The recurrence in **consanguineous pedigrees** with homozygous truncating and splice variants firmly supports an **autosomal-recessive, loss-of-function** disease mechanism.

### Finding 2 — Core and expanded clinical phenotype

The index family (4 siblings) and the Peruvian case defined the recognizable phenotypic tetrad: **progressive spondyloepimetaphyseal dysplasia, short stature, facial dysmorphism, short fourth metatarsals, and intellectual disability** ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

> "comprising progressive spondyloepimetaphyseal dysplasia, short stature, facial dysmorphism, short fourth metatarsals, and intellectual disability" — [PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)

Delineation of five additional individuals expanded the skeletal hallmarks and clarified that most patients are **normocephalic** and that intellectual disability is **variable** rather than obligate. One patient had a **cemento-ossifying fibrous lesion of the maxilla** ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)).

> "The skeletal hallmarks include (a) mild spondylar dysplasia, (b) epimetaphyseal dysplasia of the long bones associated with coxa vara and genu valgum, (c) brachymesophalangy with cone-shaped epiphyses, and (d) craniosynostosis." — [PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)

| Phenotype domain | Manifestations | HPO term suggestions |
|---|---|---|
| Growth | Disproportionate short stature | HP:0004322 (Short stature) |
| Spine | Platyspondyly, mild spondylar dysplasia, vertebral wedging, scoliosis, posterior scalloping | HP:0000944, HP:0002650 |
| Long bones | Epimetaphyseal dysplasia, coxa vara, genu valgum, metaphyseal cupping/fraying, small epiphyses, slipped capital femoral epiphyses | HP:0002812, HP:0002857, HP:0003411 |
| Hands/feet | Short 4th metatarsals, brachymesophalangy, cone-shaped epiphyses, pes planus, rocker-bottom feet, overriding toes | HP:0001832, HP:0005819, HP:0001845 |
| Skull/craniofacial | Craniosynostosis, copper-beaten skull, malar hypoplasia, facial dysmorphism | HP:0001363, HP:0000272 |
| Neurodevelopment | Intellectual disability (variable), developmental delay, hypotonia | HP:0001249, HP:0001252 |
| Joints | Joint dislocation (novel feature) | HP:0001373 |

### Finding 3 — Pathogenesis involves TGF-β signaling dysregulation and ECM/growth-factor disruption

A 2025 functional study framed the disease within a broader class of skeletal dysplasias that arise from disrupted extracellular-matrix dynamics and growth-factor-dependent signaling, implicating **RSPRY1 — a protein with RING and SPRY domains — in bone development** and connecting its loss to **TGF-β pathway dysregulation** ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)).

> "RSPRY1, a secreted protein with RING and SPRY domains, has been implicated in bone development" — [PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)

> "often arise due to disruptions in extracellular matrix (ECM) dynamics and growth factor-dependent signaling pathways" — [PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)

### Finding 4 — RSPRY1 loss causes constitutive, SMAD3-dependent TGF-β activation with ECM dysregulation

Transcriptomic analysis of fibroblasts from patients with homozygous *RSPRY1* mutations showed **significant enrichment of TGF-β signaling and ECM-related pathways**, with **SMAD2 and SMAD3** showing the highest transcription-factor enrichment and key effector genes **SMAD3, COL1A1, and TRPV4**. RSPRY1-knockout fibroblasts exhibited **enhanced motility in wound-healing assays**, a phenotype **abrogated in RSPRY1+SMAD3 double-knockout** cells — demonstrating SMAD3-dependence. A **limited response to exogenous TGF-β** in RSPRY1-deficient cells indicated the pathway was already **constitutively active** ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)).

> "RSPRY1, a secreted protein with RING and SPRY domains, has been implicated in bone development" — [PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)

This is the pivotal mechanistic finding: RSPRY1 normally **restrains** TGF-β/SMAD3 signaling, and its loss unleashes constitutive, SMAD3-driven activation that dysregulates ECM production in bone-forming cells.

### Finding 5 — Expanded variant/phenotype spectrum: novel p.Cys551Tyr missense and joint dislocation

Two Indian sisters presenting with short stature, facial dysmorphism, progressive vertebral defects, small epiphyses, cupping and fraying of metaphyses, brachydactyly, and short metatarsals were found to carry a **homozygous missense variant c.1652G>A; p.(Cys551Tyr)** in *RSPRY1*. **Joint dislocation** was reported as a novel clinical feature of the condition ([PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)).

> "Two siblings presenting with short stature, facial dysmorphism, progressive vertebral defects, small epiphysis, cupping and fraying of metaphyses, brachydactyly, and short metatarsals harbored a homozygous missense variant c.1652G>A;p.(Cys551Tyr) in the RSPRY1 gene." — [PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)

> "We observed joint dislocation as a novel clinical feature of this condition." — [PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)

### Finding 6 — Exact index variants and detailed multisystem phenotype including progressive loss of ambulation

Faden et al. (2015) identified in the consanguineous Saudi family a homozygous 1-bp duplication **c.1279dupA (p.Thr427AsnfsTer10)** that segregated fully with disease and was **absent from 650 Saudi control exomes and ExAC**; the Peruvian boy carried homozygous **c.121G>T (p.Gly41Cys / G41C)** at a conserved residue ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/); OMIM #616723).

> "Combined autozygome/exome analysis identified a homozygous frameshift mutation in RSPRY1 with resulting nonsense-mediated decay." — [PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)

The OMIM clinical synopsis proband — a 13-year-old girl — showed delayed motor milestones, **walked at 5 years then progressively lost ambulation and became wheelchair-bound**, generalized hypotonia, microcephaly, flattened occiput, malar hypoplasia, low-set small ears, short neck, short hands, rocker-bottom feet with overriding toes, genu valgum, and scoliosis. Skeletal survey documented generalized osteopenia, delayed bone age, **copper-beaten skull with premature suture closure (craniosynostosis)**, short metacarpals, platyspondyly, anterior vertebral wedging and posterior scalloping, thoracolumbar scoliosis, narrow pelvis, bilateral coxa vara, short/slender long bones, small epiphyses, metaphyseal cupping/fraying (tibia/fibula), slipped capital femoral epiphyses, short femoral neck, and distal femoral bowing.

### Finding 7 — RSPRY1 orthologs, expression pattern, and knockout mouse resources

*RSPRY1* is conserved **1:1 across human (NCBI Gene 89970; 16q13), mouse (*Rspry1*, MGI:1914860), rat, and zebrafish (*rspry1*, NCBI 565154; ENSDARG00000062558)**. The human protein shares **97% amino-acid identity with mouse and rat** and contains a SPRY domain plus a putative C3HC4-type (RING) zinc finger. Faden et al. showed *Rspry1* is expressed in **mouse limb-bud mesenchyme from E12.5** and, at E18.5 (primary ossification), is abundant in **developing endochondral bones and skeletal muscle** (with signal also in heart, kidney, and brain), localizing strongly to **osteoblasts and osteocytes**, minimally to chondrocytes, and prominently in perichondrium/periosteum ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

> "we detect strong RSPRY1 protein localization in murine embryonic osteoblasts and periosteal cells during primary endochondral ossification, consistent with a role in bone development" — [PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)

Targeted knockout alleles exist (**Rspry1^tm1(KOMP)Wtsi**, MGI:4419609; **Rspry1^tm1Lex**, MGI:5007310) with corresponding IMPC/IMSR strains, but **no published mouse model recapitulating the human skeletal dysplasia phenotype** was identified.

---

## Mechanistic Model / Interpretation

RSPRY1 integrates into the growth-factor circuitry that governs endochondral ossification. The convergent genetic, transcriptomic, and functional data support the following causal chain:

```
Biallelic LOF RSPRY1 variants (frameshift/splice/missense)
        │  (NMD of truncating alleles → loss of protein)
        ▼
Loss of RSPRY1 negative regulation of TGF-β pathway
        │
        ▼
Constitutive, SMAD3-dependent TGF-β/SMAD activation
   (↑ SMAD2/SMAD3 TF activity; ↑ SMAD3, COL1A1, TRPV4)
        │
        ▼
Dysregulated ECM dynamics in osteoblasts / periosteum / perichondrium
   (bone-forming cells, minimal chondrocyte expression)
        │
        ▼
Disordered endochondral ossification
        │
        ▼
Progressive spondyloepimetaphyseal dysplasia, short stature,
short 4th metatarsals, craniosynostosis, coxa vara/genu valgum,
SCFE, scoliosis, joint dislocation ± intellectual disability
```

**Upstream vs downstream.** The upstream trigger is loss of the RSPRY1 protein (a RING+SPRY E3-ligase-like/adaptor molecule). The proximate downstream node is de-repression of TGF-β/SMAD3, and the terminal downstream events are ECM misregulation and defective bone matrix deposition during endochondral ossification.

**Cell types and processes.** Affected cells are principally **osteoblasts (CL:0000062)** and **osteocytes (CL:0000137)** plus **periosteal/perichondrial fibroblasts**; chondrocytes are relatively spared at the expression level. Relevant biological processes include **endochondral ossification (GO:0001958)**, **ossification (GO:0001503)**, **TGF-β receptor signaling pathway (GO:0007179)**, **SMAD protein signal transduction (GO:0060395)**, **extracellular matrix organization (GO:0030198)**, and **regulation of ossification (GO:0030278)**. Cellular components implicated include the **RING-type zinc finger / ubiquitin-ligase machinery** and the **extracellular matrix (GO:0031012)**.

**Ontology anchors.** MONDO: SEMD Faden–Alkuraya type (mapped to OMIM #616723). Gene: HGNC *RSPRY1*. UBERON anatomical sites: vertebral column (UBERON:0001130), long bone epiphysis (UBERON:0001438) and metaphysis (UBERON:0004958), metatarsal bone (UBERON:0001448), cranial suture (UBERON:0007712), femoral neck. CHEBI/pathway: TGF-β (protein signal), collagen type I (COL1A1). NCIT interventions are limited to supportive/orthopedic categories (see Treatment).

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution | Evidence type |
|---|---|---|---|
| [26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/) | *Identification of a Recognizable Progressive Skeletal Dysplasia Caused by RSPRY1 Mutations* | Foundational: gene discovery (c.1279dupA, c.121G>T), core phenotype, mouse expression pattern | Human clinical + model organism |
| [30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/) | *Further delineation of SEMD Faden–Alkuraya type … cono-brachydactyly and craniosynostosis* | Expanded skeletal hallmarks; new variants c.377delT, c.516+2T>A; variable ID; normocephaly | Human clinical |
| [38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/) | *Two sisters with RSPRY1-related SEMD* | Novel missense p.Cys551Tyr; joint dislocation as new feature | Human clinical |
| [39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/) | *Unraveling the Role of RSPRY1 in TGF-β Pathway Dysregulation* | Mechanism: constitutive SMAD3-dependent TGF-β activation; ECM dysregulation; wound-healing rescue by SMAD3 KO | In vitro / patient fibroblasts + computational |
| [39706863](https://pubmed.ncbi.nlm.nih.gov/39706863/) | *Genetic and allelic heterogeneity in 248 Indians with skeletal dysplasia* | Population/cohort context; RSPRY1 among expanded genotype–phenotype spectrum; high AR proportion and consanguinity | Human clinical cohort |
| [27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/) | *16q12.2q21 deletion with developmental delay, epilepsy, short stature* | Supports RSPRY1 haploinsufficiency contributing to skeletal defects within a contiguous-gene deletion | Human clinical (case) |

The four RSPRY1-specific papers ([26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/), [30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/), [38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/), [39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)) are mutually reinforcing: gene discovery, phenotype expansion, allelic expansion, and mechanism, respectively. The cohort study ([39706863](https://pubmed.ncbi.nlm.nih.gov/39706863/)) situates the disorder among predominantly autosomal-recessive skeletal dysplasias in consanguineous populations, and the deletion case ([27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/)) provides orthogonal support that RSPRY1 dosage loss produces skeletal defects.

---

## Epidemiology, Inheritance, Diagnostics, Prognosis, Treatment & Prevention (Consolidated)

**Epidemiology & inheritance.** SEMD-FADA is **ultra-rare** with only a handful of families reported worldwide (Saudi Arabia, Peru, Turkey, India); precise prevalence/incidence figures are unavailable (Orphanet lists it without a firm prevalence estimate). Inheritance is **autosomal recessive**; reported cases arise in **consanguineous** unions, consistent with homozygous variants identified by autozygosity mapping. Penetrance appears complete for the skeletal phenotype among biallelic carriers, with **variable expressivity** particularly for intellectual disability and head circumference. No founder variant has been established, though recurrence in specific populations reflects consanguinity.

**Diagnostics.** Diagnosis rests on **radiographic skeletal survey** (platyspondyly, epimetaphyseal changes, coxa vara, genu valgum, cone-shaped epiphyses, craniosynostosis, short 4th metatarsals) combined with **molecular confirmation** of biallelic *RSPRY1* variants via **whole-exome/whole-genome sequencing** or targeted skeletal-dysplasia gene panels; single-gene testing/Sanger confirmation and segregation analysis complete the workup. Differential diagnoses include other spondyloepimetaphyseal dysplasias and cono-brachydactyly syndromes. No specific serum/urine biomarker exists.

**Prognosis.** The disorder is **progressive**: short stature, worsening epimetaphyseal disease, slipped capital femoral epiphyses, and scoliosis accrue over childhood, and at least one patient **progressively lost ambulation and became wheelchair-bound**. Life expectancy has not been reported as significantly shortened; morbidity is driven by orthopedic disability and, where present, cognitive impairment.

**Treatment.** There is **no disease-specific or curative therapy**. Management is **supportive and multidisciplinary**: orthopedic surgery (for coxa vara, SCFE, scoliosis, joint dislocation), **craniosynostosis surgery** where indicated, physical/occupational therapy and mobility aids, developmental and educational support for intellectual disability, and **genetic counseling** for consanguineous families. Relevant NCIT categories are limited to supportive/orthopedic interventions (e.g., NCIT orthopedic surgical procedure, physical therapy, genetic counseling). The mechanistic identification of constitutive TGF-β/SMAD3 activation raises the theoretical possibility of **TGF-β pathway inhibition** as a future targeted strategy, but this remains entirely experimental.

**Prevention.** Primary prevention is limited to **genetic counseling**, **carrier testing** in at-risk families, and options such as **prenatal diagnosis** or **preimplantation genetic testing** once the familial variant is known. Public-health counseling regarding consanguinity is relevant in populations where the disorder recurs.

**Other species / model organisms.** *Rspry1* is conserved in mouse, rat, and zebrafish. Off-the-shelf **knockout mouse alleles** (Rspry1^tm1(KOMP)Wtsi; Rspry1^tm1Lex) are available through IMPC/IMSR, but **no published model recapitulates the human skeletal dysplasia**, and no naturally occurring animal disease has been described.

---

## Limitations and Knowledge Gaps

1. **Very small case count.** Fewer than ~15 molecularly confirmed individuals are reported, so genotype–phenotype correlations, penetrance estimates, and natural-history data are provisional. No formal prevalence/incidence exists.
2. **Mechanism largely from patient fibroblasts.** The constitutive SMAD3-dependent TGF-β activation was demonstrated in dermal fibroblasts and knockout fibroblast lines ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)), not in primary human osteoblasts/chondrocytes; whether the same circuit operates identically in the growth plate in vivo is inferred, not proven.
3. **No phenotype-recapitulating animal model.** Although knockout alleles exist, none has been reported to reproduce the human skeletal dysplasia, leaving in-vivo mechanism and therapeutic testing unaddressed.
4. **Protein biochemistry incomplete.** RSPRY1 is variably described as "secreted" and as a RING+SPRY protein; its precise molecular activity (e.g., E3 ubiquitin ligase substrate specificity toward TGF-β/SMAD components) is not experimentally resolved.
5. **Variant interpretation.** Missense variants (p.Gly41Cys, p.Cys551Tyr) require ongoing ACMG re-evaluation and functional validation; allele frequencies in gnomAD for these are effectively absent/ultra-rare, consistent with pathogenicity but not exhaustively characterized here.
6. **Intellectual disability mechanism unexplained.** Whether ID reflects a direct neuronal role of RSPRY1 (expressed in brain) or a secondary consequence remains unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional/global Rspry1-knockout mouse and phenotype the skeleton** (micro-CT of long bones, spine, skull sutures; growth-plate histology) to test whether it recapitulates SEMD, coxa vara, craniosynostosis, and SCFE.
2. **Assay TGF-β/SMAD3 signaling directly in patient- and CRISPR-derived osteoblasts/chondrocytes** (phospho-SMAD3 Western blot, SMAD-responsive luciferase reporters, RNA-seq) to confirm the fibroblast findings in bone-lineage cells.
3. **Test pharmacologic TGF-β/SMAD3 inhibition** (e.g., ALK5/TGFBR1 inhibitors) in RSPRY1-null cellular and, if validated, murine models to establish proof-of-concept for a targeted therapy.
4. **Define RSPRY1 biochemistry**: determine whether the RING domain confers E3 ubiquitin-ligase activity and identify SMAD-pathway substrates via IP–mass spectrometry; localize the protein (secreted vs intracellular).
5. **Establish an international patient registry** to capture natural history, ambulation trajectory, craniosynostosis outcomes, and quality-of-life measures, and to refine penetrance/expressivity.
6. **Functionally validate missense variants** (p.Gly41Cys, p.Cys551Tyr) in expression/degradation and signaling assays to firm up ACMG classification.
7. **Screen contiguous-gene-deletion cohorts** (16q12–q21) for skeletal features to quantify the contribution of RSPRY1 dosage ([PMID: 27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/)).

---

## Consensus Answer

Spondyloepimetaphyseal dysplasia, Faden–Alkuraya type (SEMD-FADA; OMIM #616723, Orphanet ORPHA:457395) is an ultra-rare autosomal-recessive skeletal dysplasia caused by biallelic loss-of-function variants in *RSPRY1* (16q13; a 576-aa RING+SPRY protein). Its core phenotype is progressive spondyloepimetaphyseal dysplasia with short stature, short fourth metatarsals, facial dysmorphism, and intellectual disability, plus craniosynostosis, coxa vara/genu valgum, slipped capital femoral epiphyses, scoliosis, and sometimes progressive loss of ambulation; pathogenesis involves constitutive, SMAD3-dependent TGF-β/ECM signaling dysregulation in osteoblasts and perichondrium during endochondral ossification. Management is supportive and multidisciplinary, as no disease-specific therapy exists.


## Artifacts

- [OpenScientist final report](Progressive_Spondyloepimetaphyseal_Dysplasia-short_Stature-short_Fourth_Metatarsals-intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Spondyloepimetaphyseal_Dysplasia-short_Stature-short_Fourth_Metatarsals-intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30063090` *(abstract only)*: "Whole exome sequencing revealed a novel homozygous [c.377delT] [p.Ile126fs\*] frameshift mutation at exon 2 in one family, while Sanger sequencing revealed a novel homozygous splice site mutation [c.516+2T>A] at exon 4/intron 4 border of RSPRY1 in the other family."
  - closest text in source: "Whole exome sequencing revealed a novel homozygous [c.377delT] [p.Ile126fs*] frameshift mutation at exon 2 in one family, while Sanger sequencing revealed a novel homozygous splice site mutation [c.516+2T>A] at exon 4/intron 4 border of RSPRY1 in the other family"