---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-01T15:19:38.407610'
end_time: '2026-08-01T15:48:19.642413'
duration_seconds: 1721.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Facioscapulohumeral Muscular Dystrophy
  mondo_id: ''
  category: Genetic
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
citation_count: 32
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Facioscapulohumeral_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Facioscapulohumeral_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Facioscapulohumeral Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Facioscapulohumeral Muscular Dystrophy** covering all of the
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

# Facioscapulohumeral Muscular Dystrophy (FSHD): A Comprehensive Disease Characteristics Report

**Disease category:** Genetic (autosomal-dominant / digenic myopathy)
**Suggested ontology mapping:** MONDO:0008028 (facioscapulohumeral muscular dystrophy); OMIM 158900 (FSHD1), 158901 (FSHD2); Orphanet ORPHA:269; MeSH D020391 ("Muscular Dystrophy, Facioscapulohumeral"); ICD-10 G71.0; ICD-11 8C71.

---

## Summary

Facioscapulohumeral muscular dystrophy (FSHD) is one of the most common inherited myopathies (prevalence ~1 in 8,000–20,000) and is defined clinically by slowly progressive, characteristically **asymmetric** weakness that begins in the muscles of the face, scapular stabilizers, and upper arms and later descends to the trunk and lower limbs. Despite decades of genetic confusion, FSHD is now understood as a **single-mechanism disease**: the aberrant, epigenetically de-repressed expression of the germline transcription factor **DUX4** (double homeobox 4) in skeletal muscle, where it is normally silenced. DUX4 misexpression is reached by two genetic routes that converge on the same toxic endpoint: **FSHD1 (~95%)**, caused by contraction of the D4Z4 macrosatellite repeat array to 1–10 units on a permissive 4qA haplotype at 4q35; and **FSHD2 (~5%)**, a digenic disease requiring a pathogenic variant in a chromatin repressor (most often *SMCHD1*, also *DNMT3B*, *LRIF1*) together with a borderline-length array and a permissive haplotype [PMID: 38955828; 34711481; 37703328].

Once de-repressed, DUX4 acts as a potent transcription factor that reactivates an early-embryonic/germline program — including *ZSCAN4*, *PRAMEF* family, *TRIM43*, *MBD3L*, endogenous retrotransposons, and innate-immune mediators such as *DEFB103* — and kills muscle cells primarily through caspase-3/7-dependent apoptosis, while also inhibiting nonsense-mediated decay (NMD) via UPF1 degradation and repressing the myogenic regulators *MYOD1* and *MYF5* [PMID: 22892954; 22209328; 25564732; 30446688; 37973788]. DUX4 is expressed in a rare, stochastic, **burst-like** fashion in a small subset of myonuclei, which explains how sporadic expression produces generalized wasting and why DUX4 itself is such a difficult pharmacodynamic biomarker [PMID: 30445587].

Clinically, FSHD has near-normal life expectancy but imposes a heavy quality-of-life burden through pain, fatigue, impaired mobility (~20% eventually require a wheelchair), sleep disturbance, and extramuscular comorbidities (high-frequency hearing loss, Coats-like retinal vasculopathy, and — in severe infantile cases — seizures and cognitive impairment) [PMID: 40879179; 38968057; 41037169]. Diagnosis is molecular, integrating D4Z4 repeat sizing, 4qA haplotyping, methylation profiling, and exome sequencing for FSHD2 [PMID: 42498520; 36348371]. **No disease-modifying therapy is approved**: the lead candidate losmapimod (a p38 MAPK inhibitor) failed both its phase 2b DUX4-expression endpoint and its subsequent phase 3 clinical endpoint, leaving multidisciplinary symptomatic care as the standard while a rich pipeline of DUX4-lowering RNA and small-molecule therapeutics advances [PMID: 38631764; 40580827; 28273791; 35884928].

This report synthesizes 13 confirmed findings across 59 reviewed papers and is organized to match the 15-section disease-characteristics template.

---

## Key Findings

### Finding 1 — Two genetic routes, one mechanism (DUX4 de-repression)

FSHD is caused by aberrant DUX4 expression reached by two mutually convergent genetic mechanisms. **FSHD1 (~95% of cases)** results from a pathogenic contraction of the D4Z4 macrosatellite repeat array to 1–10 repeat units in the subtelomeric region of chromosome 4 (4q35); normal arrays span roughly 8 to >100 units. Contraction produces chromatin relaxation and de-repression of the DUX4 retrogene that is embedded in the distal D4Z4 unit. **FSHD2 (~5%)** is a **digenic** disease: a pathogenic variant in a D4Z4 chromatin repressor — most often *SMCHD1* on chromosome 18, and also *DNMT3B* and *LRIF1* — combined with a borderline array (8–20 units) and a permissive haplotype. Both routes converge on epigenetic derepression and toxic DUX4 expression in skeletal muscle. *(Evidence: human clinical / review.)*

> *"In 95% of cases, FSHD patients carry a pathogenic contraction of the D4Z4 repeat units (RUs) in the subtelomeric region of chromosome 4 (4q35), which leads to the expression of DUX4 retrogene, toxic for muscles (FSHD1). Five percent of patients display the same clinical phenotype in association with a mutation in the SMCHD1 gene located in chromosome 18"* — [PMID: 38955828](https://pubmed.ncbi.nlm.nih.gov/38955828/)

> *"FSHD2 is a digenic disease and that mutations in the genes SMCHD1, DNMT3B, and more recently LRIF1, can cause FSHD2"* — [PMID: 34711481](https://pubmed.ncbi.nlm.nih.gov/34711481/)

### Finding 2 — DUX4 is an embryonic transcription factor toxic to muscle via apoptosis and NMD inhibition

DUX4 is a double-homeobox retrogene normally expressed only in the testis and early embryo (where it drives zygotic genome activation) and epigenetically silenced in somatic tissue. When misexpressed in muscle it activates early-embryonic/germline genes and retroviral elements and drives cell death **primarily through caspase-3/7-dependent apoptosis**. DUX4 protein also proteolytically degrades UPF1, a central component of the nonsense-mediated decay (NMD) machinery; because DUX4 mRNA is itself an NMD substrate, this creates a **double-negative feedback loop** that stabilizes DUX4 and contributes to its burst-like expression. At low levels, DUX4 additionally represses the myogenic regulators *MYOD1* and *MYF5*, impairing differentiation. *(Evidence: in vitro / model.)*

> *"DUX4-triggered proteolytic degradation of UPF1, a central component of the nonsense-mediated decay (NMD) machinery, is associated with profound NMD inhibition"* — [PMID: 25564732](https://pubmed.ncbi.nlm.nih.gov/25564732/)

> *"cell death does primarily occur through caspase 3/7-dependent apoptosis"* — [PMID: 37973788](https://pubmed.ncbi.nlm.nih.gov/37973788/)

> *"a large set of human myogenic genes is rapidly deregulated by DUX4, including MYOD1 and MYF5"* — [PMID: 30446688](https://pubmed.ncbi.nlm.nih.gov/30446688/)

### Finding 3 — Extramuscular comorbidities: hearing loss, retinal vasculopathy, seizures

In the population-based MD STARnet cohort (n=548), 17.2% of patients had at least one of three key comorbidities: **hearing loss 13%** (n=71, most common), **retinal abnormalities 3.6%** (n=20), and **seizures 2.0%** (n=11). Median age at diagnosis differed markedly — hearing loss 46.5 y, retinal 58.7 y, and seizures 16.5 y (half of seizure cases occurred at ≤10 y). These extramuscular features (hearing loss, Coats-like retinal vasculopathy, cognitive impairment, spinal deformity) are enriched in severe early-onset/infantile FSHD, which carries the shortest D4Z4 repeats. *(Evidence: human clinical, population-based.)*

> *"Hearing Loss (13%; n = 71) was the most frequently reported comorbidity, followed by retinal abnormalities (3.6%; n = 20) and seizures (2.0%; n = 11)"* — [PMID: 40879179](https://pubmed.ncbi.nlm.nih.gov/40879179/)

> *"Children with a severe, early-onset phenotype experience higher rates of extramuscular features, including hearing loss, cognitive impairment, and spinal deformities"* — [PMID: 41037169](https://pubmed.ncbi.nlm.nih.gov/41037169/)

### Finding 4 — Penetrance is age-dependent and incomplete; repeat size is a weak predictor

Penetrance depends on repeat size and increases into late adulthood, with roughly 17% non-penetrant and ~25% asymptomatic carriers. In a genotype–phenotype study (n=152), **familial factors accounted for 50% of the variance in disease severity**, whereas D4Z4 repeat array size explained only **~10% overall** (~30% for facial, ~15% upper limb, ~3% leg). Unaffected carriers had significantly longer arrays than symptomatic relatives (7.3 vs 6.0 units, P<0.001). Prevalence estimates range from ~1 in 20,000 to ~1 in 8,000, making FSHD one of the most common muscular dystrophies. *(Evidence: human clinical, family-based.)*

> *"Familial factors accounted for 50% of the variance in disease severity (FSHD clinical score). The explained variance by the D4Z4 repeat array size for disease severity was limited (approximately 10%)"* — [PMID: 30211448](https://pubmed.ncbi.nlm.nih.gov/30211448/)

> *"penetrance depends on repeat size and increases until late adulthood"* — [PMID: 29997197](https://pubmed.ncbi.nlm.nih.gov/29997197/)

> *"Facioscapulohumeral muscular dystrophy (FSHD) is a myopathy with prevalence of 1 in 20,000"* — [PMID: 33303865](https://pubmed.ncbi.nlm.nih.gov/33303865/)

### Finding 5 — No approved disease-modifying therapy; losmapimod failed phase 3

Losmapimod, a selective p38 α/β MAPK inhibitor that reduces DUX4 expression in vitro, was well tolerated in phase 1/2 (NCT04004000). The phase 2b **ReDUX4** trial (NCT04003974) **did not meet its primary endpoint** of reduced DUX4-driven gene expression in muscle biopsy, although some functional measures trended favorably; the subsequent phase 3 trial failed to demonstrate clear clinical benefit. Current management remains multidisciplinary and symptomatic: physical/occupational therapy, scapular fixation surgery, and management of hearing, retinal, and respiratory complications, plus pain and fatigue control. *(Evidence: human clinical trials.)*

> *"the trial failed to demonstrate a clear clinical benefit, highlighting key challenges in drug development for the disease"* — [PMID: 40580827](https://pubmed.ncbi.nlm.nih.gov/40580827/)

> *"The primary endpoint was change from baseline to either week 16 or 36 in DUX4-driven gene expression in skeletal muscle biopsy samples"* — [PMID: 38631764](https://pubmed.ncbi.nlm.nih.gov/38631764/)

### Finding 6 — ACTA1-MCM/FLExDUX4 mouse recapitulates progressive DUX4-driven pathology

The tamoxifen-inducible **ACTA1-MCM;FLExDUX4/+** bitransgenic mouse expresses low chronic DUX4 in skeletal muscle and shows progressive muscular dystrophy with DUX4-pathway molecular signatures, histological damage, and functional weakness (reduced initial force with relatively preserved power/endurance). It is the most widely used academic FSHD model and is the workhorse for testing systemic antisense DUX4-silencing therapeutics, which improve molecular and histopathological readouts including in the diaphragm. *(Evidence: model organism.)*

> *"the most commonly used by academic laboratories being ACTA1-MCM/FLExDUX4"* — [PMID: 39518930](https://pubmed.ncbi.nlm.nih.gov/39518930/)

### Finding 7 — The permissive 4qA haplotype supplies a polyadenylation signal that stabilizes DUX4 mRNA

Pathogenic DUX4 expression requires a permissive distal **4qA haplotype** that provides a polyadenylation signal (PAS) in the pLAM region immediately telomeric to the last D4Z4 unit; this PAS stabilizes the otherwise-degraded DUX4 transcript, enabling translation of full-length DUX4. The near-identical 10q26 D4Z4 array and the non-permissive 4qB haplotype lack a functional PAS and are non-pathogenic even when contracted. FSHD1 therefore requires **three** conditions: (1) D4Z4 contraction, (2) a 4qA permissive haplotype, and (3) reduced D4Z4 CpG methylation. Downstream, DUX4 inhibits muscle differentiation, sensitizes cells to oxidative stress, and induces atrophy. *(Evidence: review / in vitro.)*

> *"A unifying pathogenic model for FSHD emerged with the recognition that the FSHD-permissive 4qA haplotype corresponds to a polyadenylation signal that stabilizes the DUX4 mRNA"* — [PMID: 27816329](https://pubmed.ncbi.nlm.nih.gov/27816329/)

> *"Aberrant DUX4 expression triggers a deregulation cascade inhibiting muscle differentiation, sensitizing cells to oxidative stress, and inducing muscle atrophy"* — [PMID: 27816329](https://pubmed.ncbi.nlm.nih.gov/27816329/)

### Finding 8 — Muscle MRI reveals a specific asymmetric involvement pattern useful for diagnosis and natural history

Whole-body muscle MRI (30 FSHD vs 23 other myopathies) identified an FSHD-specific pattern of fatty replacement and atrophy, most frequently in the **trapezius, teres major, and serratus anterior**; asymmetric involvement was significantly higher in FSHD than in other myopathies. Prospective quantitative MRI shows an average yearly fat-fraction increase of **~2%** (thigh) and **~1.9%** (leg); muscles with intermediate baseline fat fraction (15–30%) or elevated water-T2 (edema >41 ms) progress fastest, and edematous muscles are at higher risk of irreversible fatty replacement. wT2 and fat fraction correlate with clinical scales, making MRI a sensitive trial biomarker. *(Evidence: human clinical imaging.)*

> *"The most frequently affected muscles, including paucisymptomatic and severely affected FSHD patients, were trapezius, teres major and serratus anterior. Moreover, asymmetric muscle involvement was significantly higher in FSHD as compared to NFSHD patients"* — [PMID: 26115655](https://pubmed.ncbi.nlm.nih.gov/26115655/)

> *"The average yearly increase in FF was 2 ± 0.6% at thigh level and 1.9 ± 0.7% at leg level"* — [PMID: 40172709](https://pubmed.ncbi.nlm.nih.gov/40172709/)

### Finding 9 — DUX4 is expressed in rare, burst-like fashion in few myonuclei

Single-cell RNA-seq of patient-derived primary myocytes identified a small FSHD-specific cell population expressing DUX4 in a dynamic, **burst-like** manner; downstream DUX4-target activation persists long after DUX4 itself has faded. Pseudotime trajectory modeling reconstructed an FSHD cellular progression from an early DUX4 burst to downstream pathway activation (oxidative stress, immune/germline programs, apoptosis). This sporadic, stochastic expression (few DUX4-positive nuclei at any moment) dilutes the bulk-tissue signal and explains the difficulty of using DUX4 as a pharmacodynamic biomarker. *(Evidence: in vitro, single-cell.)*

> *"DUX4 has been shown to be expressed in a highly dynamic burst-like manner, likely resulting in the detection of the downstream cascade of events long after DUX4 expression itself has faded"* — [PMID: 30445587](https://pubmed.ncbi.nlm.nih.gov/30445587/)

### Finding 10 — DUX4 activates a germline/retrotransposon/immune program

DUX4 directly binds and activates genes of germline and early stem-cell development (*ZSCAN4*, *PRAMEF* family, *TRIM43*, *MBD3L*) plus LTR/MaLR endogenous retrotransposons; these DUX4-target genes are reliably detected in FSHD muscle but not controls, providing direct causal support for DUX4 misexpression. DUX4 also modulates innate immunity by activating *DEFB103* (β-defensin 3), which itself inhibits muscle differentiation. Loss of D4Z4 silencing manifests as CpG hypomethylation plus loss of repressive chromatin marks (H3K9me3, H3K27me3); an Argonaute-dependent siRNA pathway normally helps repress D4Z4. Notably, DUX4 is co-opted by herpesviruses and papillomaviruses, which induce it to mimic zygotic genome activation and prevent silencing of the viral genome. *(Evidence: in vitro / molecular.)*

> *"we show that DUX4 binds and activates LTR elements from a class of MaLR endogenous primate retrotransposons and suppresses the innate immune response to viral infection, at least in part through the activation of DEFB103, a human defensin that can inhibit muscle differentiation"* — [PMID: 22209328](https://pubmed.ncbi.nlm.nih.gov/22209328/)

> *"DUX4 is a germline transcription factor and its expression in skeletal muscle leads to activation of early stem cell and germline programs and transcriptional activation of retroelements"* — [PMID: 22892954](https://pubmed.ncbi.nlm.nih.gov/22892954/)

> *"Loss of D4Z4 repression in FSHD is observed as hypomethylation of the array accompanied by loss of repressive chromatin marks"* — [PMID: 26113644](https://pubmed.ncbi.nlm.nih.gov/26113644/)

### Finding 11 — Therapeutic pipeline targets DUX4 at multiple levels

Because no disease-modifying therapy is approved, strategies target the DUX4 axis at multiple points: (1) **transcript knockdown** with antisense oligonucleotides (AOs) directed at DUX4 mRNA/its polyadenylation signal, and RNA interference/siRNA (the Argonaute-dependent D4Z4 silencing pathway is exploitable); (2) **small molecules** suppressing DUX4 transcription (p38 MAPK inhibitors such as losmapimod — phase 3 negative; BET inhibitors; β2-agonists); (3) **blocking downstream toxicity** (flavones and other compounds reduce DUX4-induced apoptosis via an mTOR-independent mechanism); and (4) **epigenetic re-silencing**. Systemic AO therapy in the ACTA1-MCM/FLExDUX4 mouse improved molecular and histopathological readouts, including in the diaphragm. Clinical candidates include siRNA approaches (e.g., del-desiran / AOC-1020 antibody-siRNA conjugate) and other DUX4-lowering agents. *(Evidence: model organism / in vitro / early clinical.)*

> *"Antisense Oligonucleotides Used to Target the DUX4 mRNA as Therapeutic Approaches in FaciosScapuloHumeral Muscular Dystrophy"* — [PMID: 28273791](https://pubmed.ncbi.nlm.nih.gov/28273791/)

> *"Long-Term Systemic Treatment of a Mouse Model Displaying Chronic FSHD-like Pathology with Antisense Therapeutics"* — [PMID: 35884928](https://pubmed.ncbi.nlm.nih.gov/35884928/)

> *"we have identified a panel of five compounds that function downstream of DUX4 activity to inhibit DUX4-induced toxicity"* — [PMID: 37973788](https://pubmed.ncbi.nlm.nih.gov/37973788/)

### Finding 12 — Major quality-of-life burden despite near-normal life expectancy

FSHD is slowly progressive with generally normal or near-normal life expectancy, but causes substantial disability — roughly **20% of patients** eventually require a wheelchair. Pain and fatigue are among the most frequent and disabling symptoms: in cross-sectional neuromuscular studies, FSHD (with DM2) had significantly higher pain prevalence than other neuromuscular disorders and controls, and fatigue was the factor most consistently associated with reduced quality of life across muscular dystrophies. FSHD patients report worse sleep (insomnia) and lower mental-wellbeing QoL domains than controls. Pain medications are prescribed long-term for ~31–40% of adults, with impaired mobility the strongest correlate. **Infantile/early-onset FSHD (~10% of patients; onset <10 y)** is more severe with higher rates of extramuscular features. *(Evidence: human clinical.)*

> *"Patients with DM2 and FSHD had significantly higher levels of pain prevalence compared to other examined NMD subgroups and the control group"* — [PMID: 38968057](https://pubmed.ncbi.nlm.nih.gov/38968057/)

> *"Pain medications were prescribed for 31.1%-40.2% of people 20 years and older"* — [PMID: 40546227](https://pubmed.ncbi.nlm.nih.gov/40546227/)

> *"An estimated 10% of FSHD patients have an early onset (onset before 10 years of age) and are traditionally classified as infantile FSHD"* — [PMID: 27530735](https://pubmed.ncbi.nlm.nih.gov/27530735/)

### Finding 13 — Molecular diagnosis integrates repeat sizing, haplotyping, methylation, and exome sequencing

Definitive diagnosis is molecular, not by biopsy. First-line testing sizes the D4Z4 repeat and determines the permissive 4qA haplotype/structure using single-molecule methods (Southern/pulsed-field electrophoresis, molecular combing, or optical genome mapping); second-line testing (DR1 methylation profiling and whole-exome sequencing for *SMCHD1*/*DNMT3B*/*LRIF1*) is reserved for borderline, non-contracted, or atypical cases. In a tertiary cohort (135 referrals), FSHD was confirmed in 89.6%, of which FSHD1 90.1%, FSHD1+2 3.3%, and FSHD2 6.6%. Long-read sequencing (Nanopore/PacBio) now resolves repeat length and CpG methylation simultaneously at nucleotide resolution. Standard short-read WGS/WES and chromosomal microarray/karyotype alone cannot size the macrosatellite, and the near-identical 10q26 array and 4qA/4qB haplotypes must be distinguished. *(Evidence: human clinical / methods.)*

> *"First-line testing included single-molecule D4Z4 repeat sizing, haplotyping and structural analysis using molecular combing or optical genome mapping. DR1 methylation profiling and whole-exome sequencing (WES) were used as second-line tests in unresolved, borderline, non-contracted or clinically atypical cases"* — [PMID: 42498520](https://pubmed.ncbi.nlm.nih.gov/42498520/)

> *"We applied Nanopore CRISPR/Cas9-targeted resequencing for the diagnosis of FSHD by simultaneous detection of D4Z4 repeat length and methylation status at nucleotide level"* — [PMID: 36348371](https://pubmed.ncbi.nlm.nih.gov/36348371/)

---

## Full Report by Template Section

### 1. Disease Information

FSHD is a slowly progressive hereditary myopathy defined by characteristically **asymmetric** weakness that begins in the facial (**facio-**), scapular (**scapulo-**), and upper-arm (**humeral**) muscles and later descends to the abdominal, foot-dorsiflexor, and pelvic-girdle muscles. It is typically classified as the second/third most common muscular dystrophy. Onset is usually between 15 and 30 years of age, but ranges from infancy to late adulthood [PMID: 41781309].

- **Key identifiers:** OMIM 158900 (FSHD1) and 158901 (FSHD2); Orphanet ORPHA:269; ICD-10 G71.0; ICD-11 8C71; MeSH D020391; MONDO:0008028.
- **Synonyms/alternative names:** facioscapulohumeral dystrophy, Landouzy–Dejerine muscular dystrophy, Landouzy–Dejerine syndrome, FSH muscular dystrophy, FSHMD.
- **Information source:** Aggregated disease-level resources (OMIM, Orphanet, MeSH) plus population registries (MD STARnet, Japanese FSHD registry, TREAT-NMD) and cohort/natural-history studies; both aggregated and patient-level data contributed to this report.

### 2. Etiology

**Causal factors — genetic/epigenetic (Findings 1, 7, 10).** The primary cause is epigenetic de-repression and toxic misexpression of DUX4 in skeletal muscle. FSHD1 (~95%): D4Z4 contraction to 1–10 units on a permissive 4qA haplotype at 4q35 [PMID: 38955828; 37703328]. FSHD2 (~5%): digenic — a chromatin-repressor variant (*SMCHD1*, *DNMT3B*, *LRIF1*) plus a borderline array and permissive haplotype [PMID: 34711481]. All routes require a permissive 4qA polyadenylation signal to stabilize DUX4 mRNA [PMID: 27816329].

**Genetic risk factors.** Shorter D4Z4 arrays and lower D4Z4 methylation increase risk and severity; the 4qA permissive haplotype is obligatory. *SMCHD1* acts as both a causal FSHD2 gene and a **modifier** of FSHD1 severity.

**Environmental/lifestyle risk factors.** No established environmental cause. Mechanical overuse and eccentric exercise are debated as local aggravators; there is no strong evidence they alter disease course. Age and (subtly) sex modify expression — several registries note earlier facial weakness and higher hearing-loss rates in females [PMID: 40203460].

**Protective factors.** Longer residual D4Z4 arrays and higher CpG methylation are protective; unaffected carriers have longer arrays than symptomatic relatives (7.3 vs 6.0 units, P<0.001) [PMID: 30211448]. No validated dietary or pharmacological protective factor exists.

**Gene–environment interactions.** DUX4 target genes overlap with the innate antiviral response, and herpesviruses/papillomaviruses actively induce DUX4 to promote replication [PMID: 38168299] — a biologically intriguing but not clinically established gene–environment axis.

### 3. Phenotypes

| Phenotype | Type | Onset / severity / progression | Frequency | Suggested HPO |
|---|---|---|---|---|
| Facial weakness (orbicularis oculi/oris) | Clinical sign | Early, often first; mild→moderate; progressive | Very frequent | HP:0000278 (facial weakness) |
| Scapular winging / shoulder-girdle weakness | Clinical sign | Adolescence/early adult; presenting complaint | Very frequent | HP:0003691 (scapular winging) |
| Asymmetric proximal upper-limb weakness | Clinical sign | Progressive, descending | Very frequent | HP:0003484 |
| Foot drop / tibialis anterior weakness | Clinical sign | Later, descending | Frequent | HP:0009027 |
| Abdominal weakness (Beevor sign) | Clinical sign | Variable | Characteristic | HP:0009063 |
| Chronic pain | Symptom | Adult; disabling | Very frequent [PMID: 38968057] | HP:0012531 |
| Fatigue | Symptom | Adult; disabling; QoL-dominant | Very frequent [PMID: 31307472] | HP:0012378 |
| High-frequency sensorineural hearing loss | Lab/sign | Adult (median 46.5 y); infantile forms earlier | 13% [PMID: 40879179] | HP:0008553 / HP:0000407 |
| Retinal vasculopathy (Coats-like) | Sign | Adult (median 58.7 y) | 3.6% [PMID: 40879179] | HP:0500049 / HP:0007843 |
| Seizures | Sign | Childhood (median 16.5 y; ½ ≤10 y) | 2.0% [PMID: 40879179] | HP:0001250 |
| Respiratory muscle weakness | Sign | Advanced disease | ~1/3 in registry [PMID: 40203460] | HP:0002747 |
| Wheelchair dependence | Functional outcome | Late | ~20% [Finding 12] | HP:0002540 |

**Quality-of-life impact.** Pain and fatigue drive QoL loss more than raw muscle weakness; FSHD scored lower than DMD on mental-wellbeing domains, and 25–81% of men with MD report sleep impairment [PMID: 31307472; 36137167].

### 4. Genetic / Molecular Information

- **Causal gene:** *DUX4* (double homeobox 4; HGNC:50800), a retrogene embedded in the distal D4Z4 unit at 4q35. The de-repression machinery involves *SMCHD1* (HGNC:29090; OMIM 614982), *DNMT3B* (HGNC:2979), and *LRIF1* (HGNC:25281) in FSHD2.
- **Pathogenic "variant" class:** FSHD1 is caused by a **structural/macrosatellite contraction** (1–10 D4Z4 units), not a point mutation — invisible to standard sequencing/microarray. FSHD2 involves loss-of-function point/indel variants in *SMCHD1* (most common), *DNMT3B*, or *LRIF1*, generally classified pathogenic/likely pathogenic per ACMG. In-cis D4Z4 duplication alleles are an emerging pathogenic class [PMID: 37703328].
- **Functional consequence:** Gain-of-toxic-function via ectopic DUX4 transcription-factor activity; the chromatin-repressor variants are loss-of-function.
- **Modifier genes:** *SMCHD1* modifies FSHD1 severity; residual repeat length and methylation modify penetrance.
- **Epigenetics:** D4Z4 CpG hypomethylation and loss of repressive H3K9me3/H3K27me3 marks are central [PMID: 26113644].
- **Chromosomal features:** 4q35 D4Z4 macrosatellite; homologous non-pathogenic 10q26 array; 4qA (permissive) vs 4qB (non-permissive) haplotypes.

### 5. Environmental Information

There are no established environmental, occupational, toxic, or infectious **causes** of FSHD — it is a monogenic/digenic epigenetic disease. Of mechanistic interest, DUX4 is actively induced by herpesviruses (α/β/γ) and papillomaviruses to mimic zygotic genome activation and evade viral-genome silencing, linking DUX4 biology to viral infection but not establishing infection as an FSHD trigger [PMID: 38168299]. Lifestyle factors (exercise type/intensity) are studied for symptom management, not causation.

### 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
D4Z4 contraction (FSHD1)  ┐
   OR                     ├─► chromatin relaxation ─► DUX4 de-repression
SMCHD1/DNMT3B/LRIF1 LOF   ┘        (needs 4qA PAS to stabilize mRNA)
(FSHD2, borderline array)
        │
        ▼
  DUX4 protein (burst-like, few nuclei)
        │
   ┌────┼───────────────┬───────────────┬──────────────┐
   ▼    ▼               ▼               ▼              ▼
germline/    retro-     UPF1 degradation  MYOD1/MYF5    oxidative
stem-cell    transposon  → NMD inhibition  repression    stress +
program      activation  → DUX4 mRNA      → impaired     DEFB103
(ZSCAN4,     (LTR/MaLR)   stabilized       myogenesis    immune
PRAMEF,                    (feedback loop)                activation
TRIM43)      │
        └────┴──► caspase-3/7 apoptosis ─► myofiber death
                                    │
                                    ▼
             progressive, asymmetric fatty replacement & weakness
                     (trapezius, teres major, serratus anterior first)
```

- **Molecular pathways:** p38 MAPK (drives DUX4 transcription; drug target), NMD pathway (inhibited via UPF1), apoptotic caspase cascade, innate antiviral/interferon program.
- **Cellular processes:** apoptosis (GO:0006915), impaired myogenic differentiation (GO:0007517), oxidative-stress response (GO:0006979), NMD (GO:0000184).
- **Protein dysfunction:** DUX4 gain-of-toxic-function (aberrant transcription-factor activity); SMCHD1/DNMT3B/LRIF1 loss-of-function.
- **Immune involvement:** DUX4 activates *DEFB103* (β-defensin 3), which inhibits muscle differentiation; broader innate-immune/interferon dysregulation [PMID: 22209328].
- **Molecular profiling:** DUX4-target gene panels (ZSCAN4, TRIM43, LEUTX, PRAMEF, MBD3L) are the standard transcriptomic biomarker; single-cell RNA-seq reveals rare burst-like DUX4+ cells [PMID: 30445587].
- **GO/CL suggestions:** biological process GO:0006915 (apoptotic process), GO:0007517 (muscle organ development); cell type CL:0000187 (muscle cell), CL:0000515 (skeletal muscle myoblast), CL:0000594 (skeletal muscle satellite cell).

### 7. Anatomical Structures Affected

- **Primary organ/tissue:** skeletal muscle (UBERON:0001134), especially facial muscles (UBERON:0001577), trapezius (UBERON:0001496), teres major, serratus anterior, biceps/triceps; later abdominal, tibialis anterior (UBERON:0001385), and pelvic girdle.
- **Secondary/systemic:** cochlea/inner ear (hearing loss; UBERON:0001846), retina (UBERON:0000966; Coats-like vasculopathy), CNS (seizures in severe infantile forms), respiratory muscles/diaphragm (UBERON:0001103).
- **Cell types:** skeletal myofibers, myoblasts, and satellite cells (CL:0000594).
- **Subcellular:** nucleus (GO:0005634; DUX4 transcription-factor site) and mitochondria/oxidative-stress machinery.
- **Lateralization:** characteristically **asymmetric/bilateral-asymmetric** — a strong diagnostic clue distinguishing FSHD from most other myopathies [PMID: 26115655].

### 8. Temporal Development

- **Onset:** typically 15–30 years (adolescent/young-adult); ~10% infantile/early-onset (<10 y) with more severe, extramuscular-rich disease; late-onset forms also occur [PMID: 41781309; 27530735].
- **Onset pattern:** insidious, chronic.
- **Progression:** slow, descending, often stepwise with periods of apparent stability; quantitative MRI shows ~2%/yr fat-fraction increase [PMID: 40172709].
- **Course:** chronic, lifelong, progressive; ~20% reach wheelchair dependence.
- **Critical periods:** infantile onset marks a vulnerability window; edematous (high-T2) muscles represent a window where intervention might prevent irreversible fatty replacement [PMID: 40172709].

### 9. Inheritance and Population

- **Epidemiology:** prevalence ~1 in 8,000–20,000 [PMID: 33303865].
- **Inheritance:** autosomal dominant (FSHD1); FSHD2 is digenic (dominant *SMCHD1* variant + permissive borderline array).
- **Penetrance:** incomplete and age-dependent (~17% non-penetrant, ~25% asymptomatic carriers) [PMID: 29997197].
- **Expressivity:** highly variable, even within families; familial factors explain ~50% of severity variance vs ~10% for repeat size [PMID: 30211448].
- **De novo / mosaicism:** a substantial minority of FSHD1 cases are de novo, frequently with somatic/germline mosaicism.
- **Sex ratio:** roughly equal, with some registries reporting earlier facial weakness and more hearing loss in females [PMID: 40203460].
- **Population diversity:** D4Z4 repeat-number distributions differ across populations (e.g., Japanese registry data) [PMID: 40203460].

### 10. Diagnostics (Finding 13)

- **Definitive test:** molecular — single-molecule D4Z4 repeat sizing + 4qA haplotyping (Southern/PFGE, molecular combing, or optical genome mapping); methylation profiling and WES (*SMCHD1*/*DNMT3B*/*LRIF1*) as second-line [PMID: 42498520].
- **Long-read sequencing:** Nanopore/PacBio simultaneously resolve repeat length and methylation at nucleotide resolution [PMID: 36348371].
- **Supportive tests:** muscle MRI (asymmetric trapezius/teres major/serratus anterior fatty replacement; wT2 edema) [PMID: 26115655; 40172709]; serum CK mildly elevated or normal; EMG myopathic; biopsy non-specific and not required.
- **Biomarkers:** DUX4-target gene panel in muscle (research/trial pharmacodynamic marker); MRI fat fraction and water-T2 as imaging biomarkers.
- **Differential diagnosis:** limb-girdle muscular dystrophies, Pompe disease, mitochondrial myopathy, scapuloperoneal syndromes, polymyositis — distinguished by the asymmetric facioscapular pattern and molecular testing.
- **Screening:** cascade genetic testing of at-risk relatives; prenatal/preimplantation diagnosis feasible where a defined pathogenic allele exists.

### 11. Outcome / Prognosis

- **Life expectancy:** generally normal/near-normal.
- **Morbidity:** substantial; ~20% wheelchair-dependent; respiratory insufficiency in advanced/infantile disease (~1/3 with respiratory dysfunction, some ventilator-dependent in registry) [PMID: 40203460].
- **QoL:** dominated by pain and fatigue; worse mental-wellbeing and sleep than controls [PMID: 38968057; 31307472; 36137167].
- **Prognostic factors:** shorter D4Z4 repeats, lower methylation, infantile onset, and *SMCHD1* co-variants predict greater severity; MRI water-T2/fat fraction predict local progression [PMID: 40172709].

### 12. Treatment (Findings 5, 11)

- **No approved disease-modifying therapy.** Losmapimod (p38 MAPK inhibitor) failed phase 2b (DUX4-expression endpoint) and phase 3 (clinical endpoint) [PMID: 38631764; 40580827].
- **Standard of care (symptomatic/supportive; NCIT: supportive care, physical therapy, occupational therapy):** physical/occupational therapy, aids/orthotics (ankle-foot orthoses for foot drop), scapular fixation/arthrodesis surgery, respiratory support, aggressive pain and fatigue management, and screening/treatment of hearing and retinal complications.
- **Pipeline (DUX4-axis):** antisense oligonucleotides against DUX4 mRNA/PAS [PMID: 28273791]; siRNA (e.g., del-desiran/AOC-1020 antibody-siRNA conjugate); small molecules suppressing DUX4 transcription (BET inhibitors, β2-agonists); downstream-toxicity blockers (flavones, mTOR-independent) [PMID: 37973788]; epigenetic re-silencing. Systemic AO improved molecular/histopathology (incl. diaphragm) in the ACTA1-MCM/FLExDUX4 mouse [PMID: 35884928].
- **Pharmacogenomics:** none established.

### 13. Prevention

- **Primary prevention:** not possible (genetic disease); genetic counseling and reproductive options (prenatal/PGT) for at-risk families.
- **Secondary prevention:** cascade genetic testing; audiology and dilated retinal exams for early detection of hearing loss and Coats-like vasculopathy, especially in short-repeat/infantile cases.
- **Tertiary prevention:** physical therapy, respiratory surveillance, fall prevention, pain/fatigue management, and orthopedic management of scapular winging and spinal deformity.
- **Counseling:** genetic counseling essential given incomplete penetrance, variable expressivity, de novo/mosaic cases, and digenic FSHD2 inheritance.

### 14. Other Species / Natural Disease

FSHD is essentially a **human-specific disease** at the genetic level: the DUX4 retrogene and the 4q35 D4Z4 macrosatellite architecture (with the permissive 4qA polyadenylation signal) are primate/human features, so no naturally occurring animal FSHD equivalent is recognized. DUX4 has orthologs/paralogs (the *Dux* family) in mouse and other mammals involved in zygotic genome activation, enabling comparative study of DUX4 biology, but not a natural disease model. No established zoonotic or veterinary relevance. NCBI Taxon: *Homo sapiens* (9606).

### 15. Model Organisms (Finding 6)

- **Principal model:** the tamoxifen-inducible **ACTA1-MCM;FLExDUX4/+** bitransgenic mouse — low chronic muscle DUX4, progressive dystrophy, DUX4-pathway molecular signature, histological damage, and functional weakness; the academic workhorse for testing DUX4-silencing AOs [PMID: 39518930; 35884928].
- **Other systems:** DUX4-inducible and AAV-DUX4 mouse models; patient-derived primary myoblasts/myotubes and iPSC-derived muscle (used for single-cell RNA-seq and drug screening) [PMID: 30445587; 37973788]; zebrafish DUX4-toxicity models.
- **Model type:** tunable overexpression models — strength is faithful DUX4-pathway recapitulation and diaphragm involvement; limitation is that they model DUX4 toxicity rather than the native human D4Z4 macrosatellite contraction/epigenetic context, and burst-like stochastic expression is hard to reproduce exactly.
- **Applications:** preclinical testing of DUX4-lowering therapeutics, biomarker development, and mechanism dissection.

---

## Mechanistic Model / Interpretation

The unifying model of FSHD is elegant: **all genetic routes lead to the same molecular villain, DUX4.** FSHD1 and FSHD2 differ only in *how* the D4Z4 array loses its repressive chromatin state (cis-contraction vs trans-acting repressor loss), but both require a permissive 4qA haplotype whose polyadenylation signal rescues the otherwise-unstable DUX4 mRNA (Finding 7). This explains a long-standing paradox — why an identical, near-homologous D4Z4 array on chromosome 10q26 is harmless, and why 4qB alleles are non-pathogenic.

Once expressed, DUX4 behaves as the germline master-regulator it evolved to be, switching on an early-embryonic/germline/retrotransposon program in a tissue where that program is catastrophic (Findings 2, 10). Muscle nuclei die by caspase-3/7 apoptosis; a self-reinforcing UPF1/NMD feedback loop stabilizes DUX4 into "bursts"; and *MYOD1*/*MYF5* repression cripples regeneration. Crucially, DUX4 is expressed in only a **tiny, stochastic subset of nuclei at any instant** (Finding 9), yet its downstream damage persists and accumulates — reconciling how a rarely-detectable transcript produces relentless, generalized wasting, and why DUX4 itself is a treacherous pharmacodynamic endpoint (a likely contributor to the losmapimod phase 2b/3 failures, Finding 5).

The clinical phenotype maps onto this biology: asymmetric involvement of trapezius/teres major/serratus anterior (Finding 8), incomplete age-dependent penetrance driven far more by familial modifiers than by repeat size (Finding 4), and a heavy pain/fatigue/mobility burden despite near-normal survival (Finding 12). The therapeutic logic follows directly: silence DUX4 (ASO/siRNA), re-repress the locus (epigenetic), or blunt downstream toxicity (Finding 11).

---

## Evidence Base

| PMID | Role in report | Supports finding(s) |
|---|---|---|
| [38955828](https://pubmed.ncbi.nlm.nih.gov/38955828/) | French national protocol; FSHD1/FSHD2 proportions & mechanism | F1 |
| [34711481](https://pubmed.ncbi.nlm.nih.gov/34711481/) | FSHD2 digenic; SMCHD1/DNMT3B/LRIF1 | F1 |
| [37703328](https://pubmed.ncbi.nlm.nih.gov/37703328/) | D4Z4 biology; in-cis duplication alleles | F1 |
| [25564732](https://pubmed.ncbi.nlm.nih.gov/25564732/) | UPF1/NMD feedback loop | F2 |
| [37973788](https://pubmed.ncbi.nlm.nih.gov/37973788/) | Caspase-3/7 apoptosis; downstream-blocking flavones | F2, F11 |
| [30446688](https://pubmed.ncbi.nlm.nih.gov/30446688/) | DUX4 represses MYOD1/MYF5 | F2 |
| [40879179](https://pubmed.ncbi.nlm.nih.gov/40879179/) | MD STARnet comorbidity frequencies | F3 |
| [41037169](https://pubmed.ncbi.nlm.nih.gov/41037169/) | Extramuscular features in severe early-onset | F3 |
| [30211448](https://pubmed.ncbi.nlm.nih.gov/30211448/) | Familial vs repeat-size variance | F4 |
| [29997197](https://pubmed.ncbi.nlm.nih.gov/29997197/) | Age-dependent penetrance | F4 |
| [33303865](https://pubmed.ncbi.nlm.nih.gov/33303865/) | Prevalence 1/20,000; borderline-allele guidance | F4 |
| [38631764](https://pubmed.ncbi.nlm.nih.gov/38631764/) | ReDUX4 phase 2b design/endpoint | F5 |
| [40580827](https://pubmed.ncbi.nlm.nih.gov/40580827/) | Phase 3 losmapimod failure | F5 |
| [39518930](https://pubmed.ncbi.nlm.nih.gov/39518930/) | ACTA1-MCM/FLExDUX4 model | F6 |
| [27816329](https://pubmed.ncbi.nlm.nih.gov/27816329/) | 4qA PAS stabilizes DUX4 mRNA | F7 |
| [26115655](https://pubmed.ncbi.nlm.nih.gov/26115655/) | MRI asymmetric pattern | F8 |
| [40172709](https://pubmed.ncbi.nlm.nih.gov/40172709/) | Quantitative MRI progression | F8 |
| [30445587](https://pubmed.ncbi.nlm.nih.gov/30445587/) | Single-cell burst-like DUX4 | F9 |
| [22209328](https://pubmed.ncbi.nlm.nih.gov/22209328/) | Retrotransposon/DEFB103 immune activation | F10 |
| [22892954](https://pubmed.ncbi.nlm.nih.gov/22892954/) | Germline/stem-cell program | F10 |
| [26113644](https://pubmed.ncbi.nlm.nih.gov/26113644/) | D4Z4 hypomethylation / chromatin | F10 |
| [28273791](https://pubmed.ncbi.nlm.nih.gov/28273791/) | ASO targeting DUX4 mRNA | F11 |
| [35884928](https://pubmed.ncbi.nlm.nih.gov/35884928/) | Systemic AO efficacy in mouse | F11 |
| [38968057](https://pubmed.ncbi.nlm.nih.gov/38968057/) | Pain burden | F12 |
| [40546227](https://pubmed.ncbi.nlm.nih.gov/40546227/) | Chronic pain-medication use | F12 |
| [27530735](https://pubmed.ncbi.nlm.nih.gov/27530735/) | Infantile FSHD ~10% | F12 |
| [42498520](https://pubmed.ncbi.nlm.nih.gov/42498520/) | Two-tier diagnostic workflow | F13 |
| [36348371](https://pubmed.ncbi.nlm.nih.gov/36348371/) | Long-read repeat+methylation diagnosis | F13 |
| [38168299](https://pubmed.ncbi.nlm.nih.gov/38168299/) | Viral induction of DUX4 (GxE context) | §5 |
| [40203460](https://pubmed.ncbi.nlm.nih.gov/40203460/) | Japanese registry; sex/population differences | §3, §9, §11 |
| [31307472](https://pubmed.ncbi.nlm.nih.gov/31307472/); [36137167](https://pubmed.ncbi.nlm.nih.gov/36137167/) | QoL, fatigue, sleep | §3, §11 |
| [41781309](https://pubmed.ncbi.nlm.nih.gov/41781309/) | Clinical overview & diagnostic pathway | §1, §8 |

---

## Limitations and Knowledge Gaps

1. **DUX4 biomarker problem.** Burst-like, rare expression makes DUX4/DUX4-target quantification noisy; this likely undermined the losmapimod DUX4-expression endpoint and complicates all future trials (Findings 5, 9).
2. **Genotype–phenotype gap.** Repeat size explains only ~10% of severity; the "familial factors" that explain ~50% are largely unidentified beyond *SMCHD1* and methylation (Finding 4).
3. **Modifier biology.** The full set of severity modifiers, and the mechanisms of the striking within-family variability and asymmetry, remain unresolved.
4. **Diagnostic access.** Gold-standard sizing/haplotyping requires specialized single-molecule or long-read methods unavailable in many labs; standard WGS/WES/microarray cannot diagnose FSHD1 (Finding 13).
5. **Model fidelity.** Overexpression mouse models capture DUX4 toxicity but not the native macrosatellite/epigenetic context or the exact stochastic burst pattern (Finding 6).
6. **Therapeutic translation.** No disease-modifying therapy has yet succeeded clinically; downstream vs upstream targeting trade-offs are unsettled.
7. **Extramuscular pathophysiology.** Mechanisms of hearing loss, retinal vasculopathy, and CNS involvement (and why they cluster in short-repeat/infantile disease) are poorly defined.

## Proposed Follow-up Experiments / Actions

1. **Develop robust, minimally-invasive DUX4-activity biomarkers** — e.g., blood-based or MRI-linked composite DUX4-target signatures — to serve as trial pharmacodynamic endpoints that overcome burst-like expression (addresses Findings 5, 9).
2. **Modifier-gene discovery** — large family-based WGS + methylation + long-read studies to identify the ~50% "familial" severity variance beyond *SMCHD1* (addresses Finding 4).
3. **Head-to-head preclinical benchmarking** of DUX4-lowering modalities (ASO vs siRNA/AOC vs epigenetic re-silencing vs downstream blockers) in ACTA1-MCM/FLExDUX4 mice with standardized diaphragm and functional readouts (addresses Findings 6, 11).
4. **MRI-guided trial enrichment** — use baseline water-T2/intermediate fat fraction to select fast-progressing muscles/patients and shorten trials (addresses Finding 8).
5. **Prospective natural-history + registry expansion** (TREAT-NMD/MD STARnet/Japanese registry) to refine penetrance, sex differences, and comorbidity incidence, especially for FSHD2 and infantile FSHD (addresses Findings 3, 4, 12).
6. **Broaden diagnostic access** by validating optical genome mapping and long-read sequencing as first-line clinical assays that jointly resolve repeat length, haplotype, and methylation (addresses Finding 13).
7. **Mechanistic study of extramuscular DUX4 effects** in cochlear and retinal tissue/models to explain the short-repeat comorbidity cluster.

---

*Report compiled from 13 confirmed findings and 59 reviewed papers across 5 investigation iterations. Evidence sources span human clinical cohorts/registries, model-organism (ACTA1-MCM/FLExDUX4 mouse), in vitro (patient myoblasts, single-cell RNA-seq), and computational/review analyses.*


## Artifacts

- [OpenScientist final report](Facioscapulohumeral_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Facioscapulohumeral_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)