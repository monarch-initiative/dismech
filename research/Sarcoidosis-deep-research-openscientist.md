---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T02:36:16.714062'
end_time: '2026-07-26T02:53:30.429628'
duration_seconds: 1033.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sarcoidosis
  mondo_id: MONDO:0019338
  category: Immune
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 39
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sarcoidosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sarcoidosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sarcoidosis
- **MONDO ID:** MONDO:0019338 (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Sarcoidosis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Sarcoidosis (MONDO:0019338): A Comprehensive Disease Characteristics Report

**Disease:** Sarcoidosis · **MONDO:** MONDO:0019338 · **Category:** Immune
**Report date:** 2026-07-26 · Evidence sources: human clinical studies, GWAS, model organisms (mouse), in vitro/omics. PMIDs cited inline.

## Summary

Sarcoidosis is a multisystem, immune-mediated inflammatory disease of unknown cause, defined pathologically by **noncaseating epithelioid-cell granulomas** that most commonly involve the lungs and intrathoracic lymph nodes but can affect virtually any organ (skin, eyes, heart, nervous system, liver, spleen, and kidneys). The prevailing model is that sarcoidosis arises when a **genetically susceptible host** (strongest signals in the HLA class II region plus *BTNL2*, *ANXA11*, and *NOTCH4*) mounts an exaggerated, **HLA-restricted CD4+ Th1/Th17 granulomatous response** to persistent, poorly degradable antigens. The leading candidate antigens are remnant microbial proteins—particularly *Mycobacterium tuberculosis* catalase-peroxidase (mKatG), ESAT-6, and superoxide dismutase A (SodA)—and environmental/occupational bioaerosols, with a paradoxical inverse association with cigarette smoking.

The disease course is strikingly **bimodal**: roughly 70% of patients experience near-complete spontaneous or treatment-induced remission within two years (best exemplified by the acute HLA-DRB1*03–linked Löfgren syndrome), while approximately 30% (enriched for HLA-DRB1*15) develop chronic, progressive disease that can lead to pulmonary fibrosis, cardiac and neurological involvement, and rising, racially disparate mortality. A rare monogenic pediatric form—**Blau syndrome / early-onset sarcoidosis**—is caused by autosomal-dominant gain-of-function mutations in *NOD2 (CARD15)* and presents with the triad of arthritis, dermatitis, and uveitis.

Mechanistically, **aberrant mTORC1 activation** in macrophages and fibroblasts has emerged as a causal driver of granuloma formation and a druggable target. Diagnosis remains one of exclusion, requiring compatible clinico-radiologic features plus granuloma histology; **soluble IL-2 receptor (sIL-2R) outperforms serum ACE** as a supporting biomarker. Treatment escalates from corticosteroids to steroid-sparing agents (methotrexate, azathioprine) and anti-TNF therapy (infliximab), with emerging targeted options including the first-in-class neuropilin-2 immunomodulator **efzofitimod**, mTOR inhibitors (sirolimus), and JAK inhibitors.

---

## 1. Disease Information

**Overview.** Sarcoidosis is a chronic, systemic granulomatous disorder of unknown etiology characterized by the formation of noncaseating (non-necrotizing) epithelioid granulomas. It predominantly involves the lungs and thoracic lymph nodes (>90% of cases) but is a true multisystem disease. As the recent review notes, diagnosis relies on "*compatible clinico-radiologic features plus biopsy showing noncaseating epithelioid granulomas and exclusion of infection/malignancy*" ([PMID: 41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/)).

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0019338 |
| ICD-10 | D86 (D86.0 pulmonary, D86.2 lung with lymph nodes, D86.3 skin, D86.8 other/neurosarcoidosis, D86.9 unspecified) |
| ICD-11 | 4B20 |
| MeSH | D012507 (Sarcoidosis) |
| Orphanet | ORPHA:797 |
| OMIM | 181000 (Sarcoidosis, susceptibility, SS1); 186580/609464 (Blau syndrome / early-onset sarcoidosis, NOD2) |

**Synonyms / alternative names.** Besnier-Boeck-Schaumann disease; Boeck's sarcoid; Löfgren syndrome (acute form); Blau syndrome / early-onset sarcoidosis (monogenic pediatric form). Organ-specific terms: cardiac sarcoidosis, neurosarcoidosis, ocular/sarcoid uveitis, cutaneous sarcoidosis (e.g., lupus pernio).

**Information source.** Information is derived from a mixture of **aggregated disease-level resources** (OMIM, Orphanet, MeSH) and large **individual-patient / EHR-based cohorts** — e.g., the Swedish national register (n=9,665; [PMID: 42498935](https://pubmed.ncbi.nlm.nih.gov/42498935/)), the US TriNetX network (>108 million patients; [PMID: 41512253](https://pubmed.ncbi.nlm.nih.gov/41512253/)), and the VHA veteran cohort (n=23,745; [PMID: 39521376](https://pubmed.ncbi.nlm.nih.gov/39521376/)).

---

## 2. Etiology

**Disease causal factors.** Sarcoidosis is best modeled as a **gene–environment disease**: the ACCESS study's central hypothesis was that "*sarcoidosis occurs in genetically susceptible individuals through alteration in immune response after exposure to an environmental, occupational, or infectious agent*" ([PMID: 17684288](https://pubmed.ncbi.nlm.nih.gov/17684288/)). No single cause has been identified.

**Genetic risk factors.** A genome-wide association study in African Americans (818 cases/1,088 controls, replicated) and European Americans confirmed associations at **HLA-DRA, HLA-DRB5, HLA-DRB1, BTNL2, and ANXA11**, and identified **NOTCH4** as an independent genome-wide-significant locus (rs715299, P = 6.51×10⁻¹⁰) ([PMID: 22952805](https://pubmed.ncbi.nlm.nih.gov/22952805/)). Verbatim: "*We identified a novel sarcoidosis-associated locus, NOTCH4, that reached genome-wide significance in the combined AA samples (rs715299, P(AA-meta) = 6.51 × 10(-10))... We replicated previous European GWAS associations within HLA-DRA, HLA-DRB5, HLA-DRB1, BTNL2, and ANXA11 in both our AA and EA datasets.*" HLA-C and HLA-B associations were significant in European Americans but not African Americans. The monogenic form (Blau syndrome) is caused by *NOD2/CARD15* mutations (Section 4).

**Environmental / occupational risk factors.** The **ACCESS case-control study** (706 newly diagnosed cases + matched controls) found positive associations with agricultural employment (OR 1.46, 95% CI 1.13–1.89), occupational insecticide exposure (OR 1.61, CI 1.13–2.28), and musty-odor/mold-mildew (microbial bioaerosol) work environments (OR 1.62, CI 1.24–2.11) ([PMID: 15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)). The World Trade Center disaster demonstrated an occupational trigger: "sarcoid-like" granulomatous pulmonary disease occurred among responders at a 6-year incidence of 192/100,000, nearly double in Black vs White responders ([PMID: 21298693](https://pubmed.ncbi.nlm.nih.gov/21298693/)). Additional risk factors: female sex, African ancestry, obesity, and family history.

**Protective factors.** The most robust protective factor is **cigarette smoking**, which is inversely associated with sarcoidosis (ACCESS: ever-smoking OR 0.65, CI 0.51–0.82) ([PMID: 15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)). Verbatim: "*we observed elevated ORs for work in areas with musty odors (OR 1.62, CI 1.24-2.11) and with occupational exposure to insecticides (OR 1.61, CI 1.13-2.28), and a decreased OR related to ever smoking cigarettes (OR 0.65, CI 0.51-0.82).*" **Genetic protective factors** include HLA-DRB1*01:01, HLA-DQA1*03:01, and HLA-DQB1*03:02 in a Czech cohort ([PMID: 37153085](https://pubmed.ncbi.nlm.nih.gov/37153085/)), and the HLA-DRB1*03 allele conferring good prognosis. (Note: smoking's inverse epidemiologic association is not a basis for recommending smoking, whose net harms greatly outweigh this signal.)

**Gene–environment interactions.** The HLA class II genotype shapes which antigenic peptides are presented, effectively determining the response to environmental/microbial triggers. The 8.1 ancestral haplotype (HLA-A*01:01∼B*08:01∼C*07:01∼DRB1*03:01∼DQA1*05:01∼DQB1*02:01) associates with the benign Löfgren phenotype ([PMID: 37153085](https://pubmed.ncbi.nlm.nih.gov/37153085/)), illustrating how a specific HLA context converts an antigen exposure into a self-limited rather than chronic disease.

---

## 3. Phenotypes

Sarcoidosis phenotypes span constitutional symptoms, organ-specific manifestations, and laboratory abnormalities.

| Phenotype | Type | Frequency / notes | Suggested HPO term |
|-----------|------|-------------------|--------------------|
| Pulmonary involvement / interstitial lung disease | Clinical sign | >90% | HP:0002206 (Pulmonary fibrosis) |
| Bilateral hilar lymphadenopathy | Imaging sign | Common; CT 82.7% vs CXR 29.5% detection ([PMID: 41651390]) | HP:0100721 (Hilar lymphadenopathy) |
| Cough / dyspnea | Symptom | Common | HP:0012735 (Cough); HP:0002094 (Dyspnea) |
| Fatigue | Symptom | Very common; major QoL driver | HP:0012378 (Fatigue) |
| Erythema nodosum (part of Löfgren) | Physical manifestation | Acute presentation | HP:0012219 (Erythema nodosum) |
| Cutaneous sarcoid / lupus pernio | Physical manifestation | ~25% | HP:0000951 (Abnormal skin morphology) |
| Uveitis / ocular sarcoidosis | Clinical sign | Frequent; anterior/intermediate/posterior/panuveitis ([PMID: 42364256]) | HP:0000554 (Uveitis) |
| Cardiac involvement (arrhythmia, cardiomyopathy, sudden death) | Clinical sign | Underrecognized; can be first manifestation ([PMID: 41410048]) | HP:0011675 (Arrhythmia) |
| Neurosarcoidosis (CNS inflammation) | Clinical sign | ~5–10% | HP:0002383 (Encephalitis) |
| Hypercalcemia / hypercalciuria / nephrolithiasis | Lab abnormality | Vitamin D dysregulation; nephrolithiasis OR 1.80 in Black women ([PMID: 41646626]) | HP:0003072 (Hypercalcemia) |
| Elevated serum ACE / sIL-2R | Lab abnormality | Reflects granuloma burden | — |
| Arthritis (Blau triad) | Clinical sign | Early-onset form | HP:0001369 (Arthritis) |

**Phenotype characteristics.** Age of onset is predominantly **adult (30–60 years)**, with a second peak in women >50; the monogenic Blau form is **early childhood-onset**. Severity is **highly variable** (mild/self-limited to severe multiorgan). Progression is **episodic or progressive**, with two dominant trajectories (Section 8). Frequency among affected individuals is organ-dependent (lung near-universal; cardiac/CNS minority but high-consequence).

**Quality of life impact.** Ocular sarcoidosis causes major morbidity: one-third of sarcoid uveitis patients develop cataract (35.7%), glaucoma (30.6%), cystoid macular edema (16.1%), and low vision/blindness (10.2%) within 5 years ([PMID: 41512253](https://pubmed.ncbi.nlm.nih.gov/41512253/)). Fatigue and dyspnea are the dominant patient-reported QoL burdens; efzofitimod trials measured "*clinically meaningful improvements... across several patient-reported outcomes*" ([PMID: 36356657](https://pubmed.ncbi.nlm.nih.gov/36356657/)).

---

## 4. Genetic / Molecular Information

**Causal genes.** For classic multifactorial sarcoidosis there is **no single causal gene**; susceptibility is polygenic. The strongest and best-replicated signals are in the **MHC/HLA class II region** (HLA-DRB1, HLA-DQB1, HLA-DRA, HLA-DRB5), plus **BTNL2** (butyrophilin-like 2), **ANXA11** (annexin A11), and **NOTCH4** ([PMID: 22952805](https://pubmed.ncbi.nlm.nih.gov/22952805/)).

For the monogenic **Blau syndrome / early-onset sarcoidosis**, the causal gene is **NOD2 (CARD15)** on chromosome 16q12. It is a rare **autosomal-dominant** granulomatous disease: "*Blau syndrome is a rare, autosomal dominant granulomatous disease caused by mutations in the NOD2/CARD15 gene. While the classic triad of arthritis, dermatitis, and uveitis is well known*" ([PMID: 40667856](https://pubmed.ncbi.nlm.nih.gov/40667856/)).

**Pathogenic variants (Blau/NOD2).**

| Variant | Type | Domain | Consequence |
|---------|------|--------|-------------|
| R334W | Missense | NBD (nucleotide-binding) | Gain of function / altered signaling |
| R334Q | Missense | NBD | Gain of function |
| M513T (de novo reported) | Missense | NBD | Gain of function ([PMID: 36915122]) |

Mechanistically: "*Blau NOD2 mutations precipitate a loss of canonical NOD2 signaling*" ([PMID: 36189261](https://pubmed.ncbi.nlm.nih.gov/36189261/)) and result in loss of NOD2 cross-regulatory function. A T-cell–intrinsic role for NOD2 downstream of TCR signaling has also been proposed ([PMID: 40824708](https://pubmed.ncbi.nlm.nih.gov/40824708/)). These variants are classified **pathogenic / likely pathogenic** and are germline.

**HGNC IDs (key genes):** HLA-DRB1 (HGNC:4948), HLA-DQB1 (HGNC:4944), BTNL2 (HGNC:1142), ANXA11 (HGNC:535), NOTCH4 (HGNC:7884), NOD2 (HGNC:5331).

**Modifier genes / prognostic alleles.** HLA-DRB1 acts as a major disease-modifier: "*Human leukocyte antigen (HLA)-DRB1*03 is over-represented in LS, and is associated with a good prognosis, whereas HLA-DRB1*15-positive patients have a more chronic course of sarcoidosis*" ([PMID: 30585624](https://pubmed.ncbi.nlm.nih.gov/30585624/)). In a Czech cohort, HLA-DRB1*11:01 and DQA1*05:05 associated with advanced disease, while DRB1*03:01/DQA1*05:01 associated with remission ([PMID: 37153085](https://pubmed.ncbi.nlm.nih.gov/37153085/)). HLA-DRB1*04 correlated with elevated serum ACE and extrapulmonary manifestations ([PMID: 39393304](https://pubmed.ncbi.nlm.nih.gov/39393304/)).

**Epigenetic information & chromosomal abnormalities.** No recurrent chromosomal abnormality (aneuploidy, translocation) defines sarcoidosis. Epigenetic contributions (DNA methylation, chromatin changes affecting macrophage polarization) are an active area but were **not available** at high granularity in this review.

---

## 5. Environmental Information

**Environmental factors.** Microbial bioaerosols and occupational particulate exposures are the best-supported contributors: musty/moldy work environments (OR 1.62) and insecticide exposure (OR 1.61) ([PMID: 15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)); WTC dust produced a documented epidemic of sarcoid-like disease ([PMID: 21298693](https://pubmed.ncbi.nlm.nih.gov/21298693/)).

**Lifestyle factors.** Cigarette smoking is **inversely** associated (OR 0.65) ([PMID: 15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)). Obesity is a recognized risk factor ([PMID: 40002701](https://pubmed.ncbi.nlm.nih.gov/40002701/)). Tattoo pigments (especially black ink) can trigger localized granulomatous/uveitic reactions ([PMID: 41055154](https://pubmed.ncbi.nlm.nih.gov/41055154/)).

**Infectious agents.** *Mycobacterium tuberculosis* (NCBITaxon:1773) and *Cutibacterium/Propionibacterium acnes* (NCBITaxon:1747) are the leading candidate microbial triggers. Mycobacterial antigens (mKatG, ESAT-6, SodA) drive the disease-specific T-cell response (Sections 6/10), and *P. acnes* is used to induce sarcoid-like granulomas in animal models ([PMID: 41933939](https://pubmed.ncbi.nlm.nih.gov/41933939/)). Sarcoidosis is **not an active infection** — cultures are negative — but an immune response to **poorly degradable microbial remnants**.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream).**

```
Genetic susceptibility (HLA-DRB1/DQB1, BTNL2, ANXA11, NOTCH4; NOD2 in Blau)
        │
        ▼
Exposure to persistent, poorly degradable antigen
(mycobacterial mKatG / ESAT-6 / SodA; environmental bioaerosols)
        │
        ▼
APC (dendritic cell/macrophage) presents antigen via HLA class II
        │
        ▼
Antigen-specific CD4+ T-cell activation → Th1 (IFN-γ, IL-2) + Th17 (IL-17) skew
        │
        ▼
Macrophage activation & mTORC1 hyperactivation → M1 polarization
        │
        ▼
Epithelioid transformation + multinucleated giant cell formation
        │
        ▼
NONCASEATING GRANULOMA  ──► resolution (≈70%)
        │
        ▼ (persistent antigen / HLA-DRB1*15)
Chronic inflammation → fibroblast activation → FIBROSIS / organ damage
```

**Molecular pathways.** The central druggable node is **mTORC1**. Conditional deletion of *Tsc1* or *Tsc2* in mice "*leads to spontaneous formation of sarcoid-like granulomas, driven by hyperactivation of the mTORC1 pathway in fibroblasts and interstitial macrophages*" ([PMID: 42246493](https://pubmed.ncbi.nlm.nih.gov/42246493/)). mTORC1 regulates the **CCL24–CCR3 chemokine axis** controlling granuloma formation/maintenance. Additional pathways: NF-κB (downstream of NOD2/RIP2), STAT1 (M1 polarization), STAT3, and JAK-STAT (IFN-γ signaling; rationale for JAK inhibitors). **Suggested GO terms:** GO:0032008 (positive regulation of TOR signaling); GO:0002548 (monocyte chemotaxis); GO:0042110 (T cell activation); GO:0006954 (inflammatory response).

**Cellular processes.** Chronic granulomatous inflammation; macrophage M1 polarization; impaired autophagic clearance. Sirolimus data show "*aberrant mTORC1 activation promotes macrophage-driven inflammation and disrupts autophagic clearance, sustaining granuloma formation. Sirolimus, a selective mTORC1 inhibitor, restores autophagy and macrophage function*" ([PMID: 40996589](https://pubmed.ncbi.nlm.nih.gov/40996589/)). **Legumain (LGMN)** restrains granuloma formation by inhibiting mTORC1/STAT1-driven M1 polarization; genetic *Lgmn* deletion exacerbates granulomatous inflammation ([PMID: 41933939](https://pubmed.ncbi.nlm.nih.gov/41933939/)). **CXCR6** drives Th17 responses; targeting CXCR6 suppresses granuloma formation and pulmonary fibrosis ([PMID: 42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/)).

**Immune system involvement.** Sarcoidosis is a **CD4+ Th1/Th17-driven** disease. The granuloma consists of "*monocytes and dendritic cells, macrophages, multinucleated giant cells, and T cells*" ([PMID: 41410048](https://pubmed.ncbi.nlm.nih.gov/41410048/)). Disease-specific CD4+ T cells recognize mycobacterial ESAT-6 and KatG (Section 10). **Suggested CL terms:** CL:0000624 (CD4+ T cell); CL:0000860 (classical/M1 macrophage); CL:0000451 (dendritic cell).

**Protein dysfunction.** In Blau syndrome, mutant NOD2 exhibits altered NBD-domain conformation causing dysregulated NF-κB signaling and loss of cross-regulatory function ([PMID: 36189261](https://pubmed.ncbi.nlm.nih.gov/36189261/), [PMID: 42039171](https://pubmed.ncbi.nlm.nih.gov/42039171/)). The candidate antigen mKatG is notably **poorly soluble and protease-resistant**, explaining persistence ([PMID: 15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/)).

**Metabolic changes.** Dysregulated **vitamin D metabolism** — granuloma macrophages express 1α-hydroxylase, causing extrarenal 1,25-dihydroxyvitamin D production, hypercalcemia, hypercalciuria, and increased nephrolithiasis risk (OR 1.80 in Black women) ([PMID: 41646626](https://pubmed.ncbi.nlm.nih.gov/41646626/)).

**Single-cell / spatial profiling.** Single-cell RNA sequencing and spatial transcriptomics have "*increased our understanding of disease pathogenesis*" ([PMID: 41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/)). Direct immune mapping compared "*the immunological microenvironments of granulomas from TB and sarcoidosis patients*" ([PMID: 38385142](https://pubmed.ncbi.nlm.nih.gov/38385142/)) — sarcoid granulomas are **non-necrotizing** with a central epithelioid/giant-cell core surrounded by a CD4+ Th1/Th17 cuff, contrasting with the necrotic core of TB granulomas.

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: **lungs** (UBERON:0002048) and **intrathoracic/hilar lymph nodes** (UBERON:0000029), affected in >90%. Secondary/other organs: **skin** (UBERON:0002097), **eye/uvea** (UBERON:0000970 / UBERON:0001769), **heart** (UBERON:0000948), **CNS/brain** (UBERON:0000955), **liver** (UBERON:0002107), **spleen** (UBERON:0002106), **kidney** (UBERON:0002113).

**Body systems.** Respiratory (primary), lymphatic/immune, integumentary, cardiovascular, nervous, hepatobiliary, ocular/visual, and musculoskeletal.

**Tissue and cell level.** The affected tissue is the granuloma, composed of epithelioid macrophages (CL:0000860), multinucleated giant cells, dendritic cells (CL:0000451), and a rim of CD4+ T cells (CL:0000624) with Th17 cells; fibroblasts (CL:0000057) drive downstream fibrosis. BAL typically shows lymphocytosis with elevated CD4/CD8 ratio; BALF cell subsets carry prognostic significance ([PMID: 34198166](https://pubmed.ncbi.nlm.nih.gov/34198166/)).

**Subcellular level.** Key compartments: **lysosome/autophagosome** (impaired autophagic clearance; GO:0005764, GO:0005776) and **cytosol** (NOD2 as cytosolic sensor; GO:0005829).

**Localization / lateralization.** Pulmonary/lymph node involvement is characteristically **bilateral** and symmetric (bilateral hilar lymphadenopathy is the radiographic hallmark). Cutaneous and ocular disease may be bilateral or asymmetric.

---

## 8. Temporal Development

**Onset.** Typical onset is **adult (30–60)**, with a female second peak after 50; ocular sarcoidosis most commonly affects adults 30–60 ([PMID: 42364256](https://pubmed.ncbi.nlm.nih.gov/42364256/)). The monogenic Blau form is **early childhood-onset**. Onset ranges from **acute** (Löfgren: fever, erythema nodosum, bilateral hilar lymphadenopathy, arthralgia) to **insidious/subacute**.

**Progression — disease stages.** Pulmonary sarcoidosis is graded by the **Scadding chest X-ray stages**: 0 (normal), I (bilateral hilar lymphadenopathy), II (lymphadenopathy + parenchymal infiltrates), III (infiltrates alone), IV (fibrosis). Higher stage correlates with worse prognosis and elevated ACE ([PMID: 39393304](https://pubmed.ncbi.nlm.nih.gov/39393304/)).

**Disease course.** Population-scale trajectory analysis (Swedish register, n=9,665) identified "*two distinct trajectories... a resolving trajectory (71.5%) with near-complete remission of sarcoidosis-related visits within two years, and a chronic trajectory (28.5%) with persistently elevated visit rates over five years*" ([PMID: 42498935](https://pubmed.ncbi.nlm.nih.gov/42498935/)). The strongest predictor of chronicity was immunosuppressive treatment around diagnosis (RR 2.18, CI 2.04–2.33), a severity marker.

**Patterns.** Remission is frequently **spontaneous** (especially Löfgren / HLA-DRB1*03). Chronic disease (enriched HLA-DRB1*15) can be relapsing-remitting or progressive to fibrosis. The critical intervention window is early, before irreversible fibrotic damage.

---

## 9. Inheritance and Population

**Epidemiology.** Prevalence/incidence vary by geography and ancestry. In TriNetX, among 108,597,869 patients, 146,356 had sarcoidosis, with rising prevalence over 12 years ([PMID: 41512253](https://pubmed.ncbi.nlm.nih.gov/41512253/)). Estimated prevalence is ~10–40 per 100,000 in most Western populations, substantially higher in African Americans (~three-fold).

**Inheritance.** Classic sarcoidosis is **multifactorial/polygenic** with familial aggregation but no Mendelian pattern. Blau syndrome is **autosomal dominant** (NOD2), including de novo mutations (e.g., M513T) ([PMID: 36915122](https://pubmed.ncbi.nlm.nih.gov/36915122/)). Penetrance and expressivity are **variable**. Genetic anticipation, germline mosaicism, and founder effects are **not established** for sarcoidosis.

**Population demographics.**

| Dimension | Finding |
|-----------|---------|
| Ancestry | Higher prevalence and more severe, chronic, multiorgan disease in African-ancestry individuals |
| Sex | Female predominance (56.5–60.4% in sarcoid/sarcoid uveitis cohorts) ([PMID: 41512253]) |
| Race (sarcoid uveitis) | Majority Black/African American (43.68%) despite White majority overall ([PMID: 41512253]) |
| Mortality disparity | All-cause mortality 6.4% higher in Black vs White veterans (MRR 1.064; P=0.02) ([PMID: 39521376]) |
| Geographic | Higher incidence in Northern Europe (Scandinavia) and among US African Americans |

**Mortality trend.** In the VHA cohort (n=23,745, 2004–2022), "*all-cause mortality increased annually by 4.7% (P < .0001) and was 6.4% higher in Black than White veterans (mortality rate ratio, 1.064; P = .02)*" ([PMID: 39521376](https://pubmed.ncbi.nlm.nih.gov/39521376/)).

---

## 10. Diagnostics

**Diagnostic principle.** Diagnosis is one of **exclusion**, requiring (1) compatible clinico-radiologic features, (2) biopsy demonstrating **noncaseating epithelioid granulomas**, and (3) exclusion of infectious and neoplastic mimics ([PMID: 41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/), [PMID: 42237759](https://pubmed.ncbi.nlm.nih.gov/42237759/)).

**Laboratory biomarkers — sIL-2R outperforms serum ACE.**

| Study / cohort | sIL-2R sensitivity | ACE sensitivity | Other |
|----------------|--------------------|-----------------|-------|
| Ocular cohort ([PMID: 33420542]) | 76.4% | 37.7% | KL-6 26.3%, Ca 11.8% |
| Dermatology cohort ([PMID: 28295528]) | 52.8% | 29% | Lysozyme 26.4% |
| Suspected-sarcoidosis cohort ([PMID: 31622413]) | Sens 88% / Spec 85% | Sens 62% / Spec 76% | sIL-2R superior (p<0.0001) |

Verbatim: "*The sensitivity for sIL-2R (76.4%) was higher than for ACE (37.7%), KL-6 (26.3%), and Ca (11.8%)*" ([PMID: 33420542](https://pubmed.ncbi.nlm.nih.gov/33420542/)); "*sIL-2R was more sensitive than both ACE and lysozyme in supporting a diagnosis of sarcoidosis (52.8%) compared with ACE (29%) and lysozyme (26.4%)*" ([PMID: 28295528](https://pubmed.ncbi.nlm.nih.gov/28295528/)). sIL-2R also predicts EBUS-TBNA diagnostic yield ([PMID: 33093764](https://pubmed.ncbi.nlm.nih.gov/33093764/)). Additional labs: hypercalcemia/hypercalciuria, elevated CD4/CD8 ratio on BAL. For neurosarcoidosis, ACE is a poor biomarker; candidate markers include sIL-2R, CD4/CD8 ratio, neopterin, IFN-γ, and CCL2 ([PMID: 38875863](https://pubmed.ncbi.nlm.nih.gov/38875863/)).

**Imaging.** Contrast chest CT detects bilateral hilar lymphadenopathy far better than plain radiography (82.7% vs 29.5%) ([PMID: 41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/)). ¹⁸F-FDG PET and cardiac MRI are used for cardiac and occult-organ disease.

**Biopsy / histopathology.** Gold standard is tissue showing **noncaseating epithelioid granulomas** with exclusion of infection (special stains/culture negative) and malignancy. EBUS-TBNA combined with transbronchial lung biopsy achieved 100% diagnostic yield in stage I/II disease ([PMID: 33093764](https://pubmed.ncbi.nlm.nih.gov/33093764/)).

**Genetic testing.** Not indicated for classic multifactorial sarcoidosis. For suspected **Blau syndrome**, **single-gene or panel sequencing of NOD2 (CARD15)** is diagnostic ([PMID: 40667856](https://pubmed.ncbi.nlm.nih.gov/40667856/)). HLA typing has prognostic (not diagnostic) utility.

**Differential diagnosis.** Tuberculosis and other infections, lymphoma/malignancy, hypersensitivity pneumonitis, berylliosis, and **sarcoid-like reactions (SLR)** triggered by drugs (e.g., dupilumab, checkpoint inhibitors), malignancy, or infection ([PMID: 42237759](https://pubmed.ncbi.nlm.nih.gov/42237759/), [PMID: 42126659](https://pubmed.ncbi.nlm.nih.gov/42126659/)). Immune mapping distinguishes sarcoid from TB granulomas ([PMID: 38385142](https://pubmed.ncbi.nlm.nih.gov/38385142/)).

---

## 11. Outcome / Prognosis

**Course & remission.** Prognosis is bimodal: ~**71.5% resolve** within 2 years, ~**28.5% become chronic** ([PMID: 42498935](https://pubmed.ncbi.nlm.nih.gov/42498935/)). Löfgren syndrome (HLA-DRB1*03) carries an excellent prognosis; HLA-DRB1*15 predicts chronicity ([PMID: 30585624](https://pubmed.ncbi.nlm.nih.gov/30585624/)).

**Mortality.** Sarcoidosis mortality is **rising** (annual increase 4.7%) with persistent **Black-vs-White disparity** (MRR 1.064) ([PMID: 39521376](https://pubmed.ncbi.nlm.nih.gov/39521376/)). Leading causes of death: progressive pulmonary fibrosis/respiratory failure, cardiac sarcoidosis (arrhythmia, sudden death), and pulmonary hypertension ([PMID: 41410048](https://pubmed.ncbi.nlm.nih.gov/41410048/)).

**Morbidity & complications.** Pulmonary fibrosis; cardiac arrhythmia and sudden death (can be the initial manifestation) ([PMID: 41410048](https://pubmed.ncbi.nlm.nih.gov/41410048/)); neurosarcoidosis; ocular complications (cataract 35.7%, glaucoma 30.6%, blindness 10.2%) ([PMID: 41512253](https://pubmed.ncbi.nlm.nih.gov/41512253/)); nephrolithiasis ([PMID: 41646626](https://pubmed.ncbi.nlm.nih.gov/41646626/)); chronic fatigue.

**Prognostic factors.** Favorable: acute Löfgren onset, HLA-DRB1*03, low Scadding stage, normal ACE. Unfavorable: HLA-DRB1*15/11:01, elevated ACE with extrapulmonary manifestations ([PMID: 39393304](https://pubmed.ncbi.nlm.nih.gov/39393304/)), African ancestry, cardiac/CNS involvement, higher BALF lymphocyte/neutrophil/eosinophil counts ([PMID: 34198166](https://pubmed.ncbi.nlm.nih.gov/34198166/)), and need for early immunosuppression (RR 2.18 for chronicity) ([PMID: 42498935](https://pubmed.ncbi.nlm.nih.gov/42498935/)).

---

## 12. Treatment

Not all patients require treatment — many self-limited cases are observed. For those needing therapy, escalation is stepwise.

**Pharmacotherapy.**

| Line | Agent(s) | Class / mechanism | MAXO suggestion |
|------|----------|-------------------|-----------------|
| First | Corticosteroids (prednisone) | Broad immunosuppression | MAXO:0000305 (corticosteroid therapy) |
| Second (steroid-sparing) | Methotrexate | Antimetabolite / antifolate | MAXO:0000916 (methotrexate therapy) |
| Second | Azathioprine, leflunomide | Immunosuppressants | MAXO (immunosuppressant therapy) |
| Refractory | Infliximab (anti-TNF-α mAb) | TNF-α neutralization | MAXO (biologic/anti-TNF therapy) |

"*Corticosteroids remain the initial drug for most patients... Methotrexate is [the] most commonly used cytotoxic agent used for chronic disease, but azathioprine and leflunomide also have been shown to be useful. The tumor necrosis factor antibody infliximab has proved useful in treating refractory sarcoidosis*" ([PMID: 18539243](https://pubmed.ncbi.nlm.nih.gov/18539243/)).

**Emerging / targeted therapeutics.**

- **Efzofitimod (ATYR1923)** — first-in-class neuropilin-2–binding immunomodulator. In a randomized, double-blind, placebo-controlled phase 1b/2a trial (n=37, IV q4w × 24 weeks with forced steroid taper), it was well tolerated and produced "*a baseline-adjusted relative steroid reduction of 5%, 9%, and 22%, respectively. Clinically meaningful improvements were achieved across several patient-reported outcomes, several of which reached statistical significance in the 5 mg/kg dose arm*" ([PMID: 36356657](https://pubmed.ncbi.nlm.nih.gov/36356657/)). Mechanism: "*Efzofitimod (ATYR1923), a novel immunomodulator, selectively binds neuropilin 2, which is upregulated on immune cells in response to lung inflammation.*"
- **mTOR inhibitors (sirolimus)** — effective in refractory multisystem sarcoidosis by restoring autophagy/macrophage function ([PMID: 40996589](https://pubmed.ncbi.nlm.nih.gov/40996589/)).
- **JAK inhibitors and IL-6 receptor antagonists** — promising for refractory sarcoid uveitis on top of methotrexate/TNF inhibitors ([PMID: 42364256](https://pubmed.ncbi.nlm.nih.gov/42364256/)).
- **Preclinical targets:** CXCR6 blockade ([PMID: 42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/)); LGMN supplementation ([PMID: 41933939](https://pubmed.ncbi.nlm.nih.gov/41933939/)).

**Blau syndrome-specific.** TNF-α inhibitors are effective for ocular/joint disease ([PMID: 40667856](https://pubmed.ncbi.nlm.nih.gov/40667856/)).

**Pharmacogenomics.** No sarcoidosis-specific PGx dosing is established; standard TPMT/NUDT15 testing applies before azathioprine.

---

## 13. Prevention

**Primary prevention.** No vaccine or proven primary-prevention strategy exists. Given occupational associations, **reducing bioaerosol/mold and insecticide exposures** is rational but unproven ([PMID: 15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)).

**Secondary prevention.** Early detection of high-consequence organ involvement — particularly **cardiac screening (ECG/echo)** in newly diagnosed patients — can prevent sudden cardiac death ([PMID: 41410048](https://pubmed.ncbi.nlm.nih.gov/41410048/)). Pulmonology/sarcoidosis-clinic referral is associated with recommended cardiopulmonary screening, yet sociodemographic disparities exist (Black males and White females less likely to be referred) ([PMID: 40890688](https://pubmed.ncbi.nlm.nih.gov/40890688/)).

**Tertiary prevention.** Early steroid-sparing therapy to prevent corticosteroid toxicity and irreversible fibrosis; monitoring for vitamin D/calcium dysregulation and nephrolithiasis, especially with metabolic comorbidities ([PMID: 41646626](https://pubmed.ncbi.nlm.nih.gov/41646626/)).

**Counseling.** Genetic counseling is relevant for **Blau syndrome** (autosomal dominant, NOD2). No population carrier screening applies to classic sarcoidosis.

---

## 14. Other Species / Natural Disease

**Taxonomy.** Sarcoidosis is essentially a **human disease** (*Homo sapiens*, NCBITaxon:9606). No true naturally occurring idiopathic analog is established in companion animals or wildlife; granulomatous diseases in other species (e.g., mycobacterial granulomas) share cellular architecture but are typically infectious.

**Orthologous genes.** Key genes have clear orthologs used in modeling: mouse *Nod2* (NCBI Gene 257632), *Tsc1*/*Tsc2*, *Lgmn*, *Cxcr6*. The granuloma is an evolutionarily conserved host-defense structure, leveraged in comparative TB-vs-sarcoidosis immune mapping ([PMID: 38385142](https://pubmed.ncbi.nlm.nih.gov/38385142/)).

**Transmission / zoonotic potential.** Sarcoidosis is **not transmissible** and has **no zoonotic potential**; the mycobacterial-antigen hypothesis concerns immune reactivity to microbial remnants, not active/contagious infection.

---

## 15. Model Organisms

**Mammalian genetic models.**

| Model | Design | Phenotype recapitulation |
|-------|--------|--------------------------|
| *Fsp1-Cre; Tsc1^fl/fl* or *Tsc2^fl/fl* mouse | Conditional deletion in fibroblasts/macrophages | Spontaneous sarcoid-like granulomas via mTORC1 hyperactivation ([PMID: 42246493]) |
| *Lgmn^-/-* mouse (P. acnes-induced) | Knockout + microbial induction | Exacerbated granulomatous inflammation, increased M1 polarization ([PMID: 41933939]) |
| CXCR6-targeted mouse | Pathway inhibition | Reduced granuloma + fibrosis via Th17 suppression ([PMID: 42143504]) |

**Induced (non-genetic) models.** *Propionibacterium acnes*- and trehalose-6,6′-dimycolate (cord factor)-induced pulmonary granuloma models reproduce granuloma formation and are used to test therapeutics ([PMID: 41933939](https://pubmed.ncbi.nlm.nih.gov/41933939/)).

**Applications & limitations.** These models recapitulate **granuloma formation, macrophage polarization, and the mTORC1/STAT1 axis**, enabling target validation (mTOR inhibitors, LGMN, CXCR6). Limitations: they do not fully capture the **human HLA-restricted antigen-specific CD4+ response**, the bimodal natural history, or multiorgan heterogeneity. Cellular/in vitro systems (patient BAL T cells, monocyte-derived macrophages) complement in vivo models. **Resources:** MGI (mouse); Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

Sarcoidosis is best understood as a **three-hit convergence**: (1) a permissive HLA class II genotype, (2) exposure to a persistent, poorly degradable antigen, and (3) a resulting self-amplifying CD4+ Th1/Th17 granulomatous response in which **mTORC1 hyperactivation** locks macrophages into a granuloma-forming, autophagy-impaired state. The **HLA allele determines fate**: DRB1*03 contexts (Löfgren) tend to clear the antigen and resolve, whereas DRB1*15/11:01 contexts sustain the response toward chronic fibrosis. The "missing antigen" is increasingly resolved toward **mycobacterial remnants (mKatG, ESAT-6, SodA)**, recognized by lung-compartmentalized CD4+ T cells in most patients but rarely controls. This model unifies the genetics (HLA/BTNL2/ANXA11/NOTCH4), the environmental epidemiology (bioaerosols, WTC dust), the monogenic mirror (NOD2/Blau — a pure innate-sensing lesion producing the same granuloma), the therapeutic response (mTOR inhibition, anti-TNF, NRP2 modulation), and prognostic stratification.

---

## Evidence Base (Key Literature)

| PMID | Contribution |
|------|--------------|
| [22952805](https://pubmed.ncbi.nlm.nih.gov/22952805/) | GWAS: HLA-DRA/DRB5/DRB1, BTNL2, ANXA11, independent NOTCH4 susceptibility |
| [15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/) / [17684288](https://pubmed.ncbi.nlm.nih.gov/17684288/) | ACCESS: environmental/occupational risk and inverse smoking association |
| [42246493](https://pubmed.ncbi.nlm.nih.gov/42246493/) / [40996589](https://pubmed.ncbi.nlm.nih.gov/40996589/) / [41933939](https://pubmed.ncbi.nlm.nih.gov/41933939/) | mTORC1 as causal, druggable granuloma driver; sirolimus efficacy; LGMN restraint |
| [30585624](https://pubmed.ncbi.nlm.nih.gov/30585624/) / [37153085](https://pubmed.ncbi.nlm.nih.gov/37153085/) / [42498935](https://pubmed.ncbi.nlm.nih.gov/42498935/) | HLA-DRB1 prognostic alleles; bimodal natural history (71.5% resolve) |
| [33420542](https://pubmed.ncbi.nlm.nih.gov/33420542/) / [28295528](https://pubmed.ncbi.nlm.nih.gov/28295528/) / [31622413](https://pubmed.ncbi.nlm.nih.gov/31622413/) / [41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/) | sIL-2R > ACE; diagnosis of exclusion with granuloma histology |
| [40667856](https://pubmed.ncbi.nlm.nih.gov/40667856/) / [36189261](https://pubmed.ncbi.nlm.nih.gov/36189261/) / [36915122](https://pubmed.ncbi.nlm.nih.gov/36915122/) | Blau syndrome: AD NOD2 disease, mechanism, variants |
| [38385142](https://pubmed.ncbi.nlm.nih.gov/38385142/) / [41651390](https://pubmed.ncbi.nlm.nih.gov/41651390/) | Single-cell/spatial mapping distinguishing sarcoid vs TB granulomas |
| [36356657](https://pubmed.ncbi.nlm.nih.gov/36356657/) | Efzofitimod (NRP2 immunomodulator) steroid-sparing phase 1b/2a |
| [39521376](https://pubmed.ncbi.nlm.nih.gov/39521376/) | Rising mortality with Black-vs-White disparity |
| [15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/) / [19596780](https://pubmed.ncbi.nlm.nih.gov/19596780/) / [19050300](https://pubmed.ncbi.nlm.nih.gov/19050300/) / [17924974](https://pubmed.ncbi.nlm.nih.gov/17924974/) | Mycobacterial mKatG/ESAT-6/SodA as candidate pathogenic antigens |

Selected verbatim support for the antigen hypothesis: "*Matrix-assisted laser desorption/ionization time of flight mass spectrometry identified Mycobacterium tuberculosis catalase-peroxidase (mKatG) as one of these tissue antigens*" ([PMID: 15753209](https://pubmed.ncbi.nlm.nih.gov/15753209/)); and "*the presence of antigen-specific recognition of ESAT-6 and KatG in T cells from BAL fluid of 32/44 sarcoidosis subjects, compared to 1/27 controls (P < 0.0001)*" ([PMID: 19596780](https://pubmed.ncbi.nlm.nih.gov/19596780/)).

---

## Limitations and Knowledge Gaps

1. **Etiology remains formally unproven.** Despite strong immunological evidence for mycobacterial antigens, sarcoidosis is not an active infection, and no single agent satisfies Koch-style criteria. mKatG reactivity is present in ~55–73% of patients — not all.
2. **Missing data domains.** Detailed epigenetic profiling, comprehensive proteomic/metabolomic/lipidomic signatures, and precise population incidence figures were not resolved at high granularity in this investigation.
3. **Model organism gap.** Available mouse models capture granuloma biology but not the HLA-restricted antigen-specific human response or the bimodal natural history.
4. **Biomarker limitations.** sIL-2R and ACE both lack organ specificity (particularly poor for neurosarcoidosis); no validated biomarker reliably predicts chronicity prospectively.
5. **Therapeutic evidence.** Efzofitimod and sirolimus data derive from small/early-phase or case-series studies; large confirmatory RCTs are pending.
6. **No primary-data hypothesis tests** were run in this investigation; conclusions rest on literature synthesis of published cohorts.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective HLA + antigen-reactivity stratification:** combine HLA-DRB1 typing with BAL T-cell mKatG/ESAT-6 ELISPOT at diagnosis to predict resolving vs chronic trajectory.
2. **mTORC1 biomarker + trial:** validate phospho-S6/phospho-STAT1 in granuloma macrophages as a companion biomarker for a randomized sirolimus (or JAK-inhibitor) trial in refractory disease.
3. **Confirmatory efzofitimod RCT analysis** with organ-specific and QoL endpoints; correlate response with baseline NRP2 expression.
4. **Single-cell/spatial atlas across trajectories:** contrast resolving vs chronic granulomas to identify fibroblast/macrophage programs driving fibrosis and candidate anti-fibrotic targets (e.g., CXCR6).
5. **Disparity-focused implementation study:** address referral and mortality disparities in Black patients through targeted care-pathway interventions.
6. **NOD2/Blau mechanistic bridge:** test whether NOD2 gain-of-function and mycobacterial-driven classic sarcoidosis converge on a shared mTORC1/NF-κB macrophage program, potentially unifying monogenic and multifactorial forms.

---

*Report compiled from 44 reviewed papers and 10 confirmed findings across 5 investigation iterations. Evidence source types span human clinical cohorts (GWAS, registries, case-control), model organism (conditional-knockout mice), in vitro (patient BAL/PBMC T cells), and computational/single-cell profiling.*


## Artifacts

- [OpenScientist final report](Sarcoidosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sarcoidosis-deep-research-openscientist_artifacts/final_report.pdf)
