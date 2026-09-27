---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T19:09:59.652600'
end_time: '2026-09-05T19:27:47.472828'
duration_seconds: 1067.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mendelian Susceptibility To Mycobacterial Diseases Due To Partial
    IRF8 Deficiency
  mondo_id: MONDO:0013957
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Partial_IRF8_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Partial_IRF8_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mendelian Susceptibility To Mycobacterial Diseases Due To Partial IRF8 Deficiency
- **MONDO ID:** MONDO:0013957 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Mendelian Susceptibility To Mycobacterial Diseases Due To Partial IRF8 Deficiency** covering all of the
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

# Mendelian Susceptibility to Mycobacterial Disease due to Partial IRF8 Deficiency — Comprehensive Disease Report

**MONDO:0013957 · OMIM 614893 (IMD32A) · Orphanet 319600 · DOID:0111986 · MedGen 814919 (UMLS C3808589) · GARD 0017463**

---

## Summary

Mendelian Susceptibility to Mycobacterial Disease due to **partial IRF8 deficiency** (MSMD‑IRF8, MONDO:0013957) is a rare **autosomal dominant** inborn error of immunity caused by a **heterozygous, dosage‑sensitive** variant in *IRF8* (Interferon Regulatory Factor 8), a master myeloid transcription factor located at chromosome 16q24.1. The prototypical allele, **p.Thr80Ala (T80A; c.238A>G)**, lies within the IRF8 DNA‑binding domain and disrupts IRF8–DNA binding, thereby reducing IRF8 transcriptional activity. Because myeloid cell fate is determined in an IRF8 **dose‑dependent** manner, a partial (heterozygous) defect produces a **graded, subset‑selective** immune phenotype: a *selective depletion of circulating CD11c⁺CD1c⁺ conventional dendritic cells (cDC2)*, while sparing monocytes and other DC subsets. This is fundamentally milder than the autosomal recessive **complete** IRF8 deficiency (IMD32B, OMIM 614894; e.g., p.Lys108Glu/K108E), in which monocytes and all dendritic cells are absent and a life‑threatening syndrome ensues.

Clinically, partial IRF8 deficiency presents in childhood as **curable disseminated BCG disease** or environmental/non‑tuberculous mycobacterial infection, reflecting a functional bottleneck in the **IL‑12/23 → IFN‑γ circuit** that all ~22 genetic etiologies of MSMD share. The two originally described T80A subjects (Hambleton et al., NEJM 2011) were otherwise healthy and their mycobacterial disease was curable, in stark contrast to the recessive K108E patient, who required hematopoietic stem‑cell transplantation. The mechanistic basis — impaired dendritic‑cell antigen presentation and IL‑12 production feeding into reduced IFN‑γ and defective macrophage activation against intracellular mycobacteria — anchors the entire disease definition.

This report consolidates database‑verified identifiers, variant classifications (ClinVar: T80A "likely pathogenic," K108E "pathogenic," both absent from gnomAD v4), UniProt‑confirmed protein mapping (both residues fall within the IRF tryptophan pentad repeat DNA‑binding domain, aa 7–114), authoritative HPO phenotype annotations sourced to PMID 21524210, and the orthologous BXH2 mouse model, into a single knowledge‑base entry spanning all 15 requested sections.

---

## Key Findings

### Finding 1 — Partial IRF8 deficiency (autosomal dominant T80A) causes MSMD via selective cDC2 depletion

The landmark study of Hambleton and colleagues ([PMID: 21524210](https://pubmed.ncbi.nlm.nih.gov/21524210/), *NEJM* 2011) identified two distinct *IRF8* mutations defining two distinct diseases. The **T80A** variant was heterozygous and produced an **autosomal dominant, milder immunodeficiency** with a **selective depletion of CD11c⁺CD1c⁺ circulating dendritic cells** — the entity captured by MONDO:0013957. The authors state verbatim: *"The T80A variant was associated with an autosomal dominant, milder immunodeficiency and a selective depletion of CD11c⁺CD1c⁺ circulating dendritic cells."* They further note that they *"studied two otherwise healthy subjects with a history of disseminated but curable BCG disease in childhood,"* establishing both the clinical phenotype (curable disseminated BCG disease) and the small denominator (n=2) that underlies the disease's phenotype frequencies. Mechanistically, *"Both K108E and T80A mutations impair IRF8 transcriptional activity by disrupting the interaction between IRF8 and DNA."* This finding is the central pillar of the report: partial IRF8 deficiency = dose‑sensitive cDC2 loss driving curable MSMD.

### Finding 2 — All MSMD etiologies converge on the IL‑12/23–IFN‑γ circuit

Partial IRF8 deficiency is one member of a larger genetic family. A systematic review of **830 MSMD patients from 581 families** ([PMID: 38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/), Khavandegar et al. 2024) catalogued 299 unique mutations across 21 genes, with **lymphadenopathy the most common manifestation (378/830, 45.5%; multifocal in 35.1%)**, followed by fever (30.2%), organomegaly (24.8%), and sepsis (20.8%). The mean age was 10.4 years, the highest patient frequencies were in Iran, Turkey, and Saudi Arabia, and 45.5% had a positive family history. A 2026 review ([PMID: 42183200](https://pubmed.ncbi.nlm.nih.gov/42183200/), Qian et al.) states that *"22 genes have been implicated, all converging on the IL‑12/23‑IFN‑γ circuit, underscoring its non‑redundant role in controlling intracellular pathogens,"* with roughly 50% of patients still molecularly unsolved. This establishes the shared pathophysiologic funnel into which IRF8 deficiency feeds: impaired dendritic cell / macrophage cytokine cross‑talk that cripples IFN‑γ–dependent control of mycobacteria.

### Finding 3 — IRF8 is a dose‑dependent master transcription factor of the DC lineage; validated by the BXH2 mouse

The dose‑sensitivity that explains why heterozygous T80A gives a subset‑selective (rather than global) defect is well documented. Nishiyama & Tamura 2025 ([PMID: 40680811](https://pubmed.ncbi.nlm.nih.gov/40680811/)) show that IRF8 is pivotal for type 1 conventional DC (cDC1) differentiation, establishes the enhancer landscape at the progenitor stage, and that *"the cell fate within the myeloid lineages is determined in an IRF8 dose‑dependent manner."* Bigley et al. 2018 ([PMID: 29128673](https://pubmed.ncbi.nlm.nih.gov/29128673/)) anchor the model organism: the human IRF8 **R291Q** variant is *"orthologous to R294, which is mutated in the BXH2 IRF8‑deficient mouse,"* and IRF8 mutants *"failed to regulate the Ets/IRF composite element (EICE) or interferon‑stimulated response element (ISRE)."* Ham et al. 2025 ([PMID: 40072380](https://pubmed.ncbi.nlm.nih.gov/40072380/)) confirm that a **dominant‑negative** IRF8 form causes decreased cDC2 and mycobacterial susceptibility, phenotypically distinct from the recessive severe form. Together these establish the graded genotype→cell‑fate→phenotype logic.

### Finding 4 — T80A and K108E are database‑classified pathogenic variants absent from population databases

Database verification (gnomAD API, GRCh38) confirms *IRF8* = ENSG00000140968, chr16:85,899,162–85,922,606, canonical transcript ENST00000268638. Via ClinVar: **c.238A>G p.Thr80Ala** (16‑85909053‑A‑G) is classified **"Likely pathogenic"** (missense); **c.322A>G p.Lys108Glu** (16‑85909137‑A‑G) is classified **"Pathogenic"** (missense). **Neither variant appears in gnomAD v4** (absent from >730,000 population alleles), consistent with ultra‑rare, high‑penetrance disease alleles. The original functional evidence underlying these classifications is Hambleton 2011's demonstration that both mutations *"impair IRF8 transcriptional activity by disrupting the interaction between IRF8 and DNA."*

### Finding 5 — Corrected identifiers and protein‑domain mapping

EBI OLS4 confirms MONDO:0013957 = "Mendelian susceptibility to mycobacterial diseases due to partial IRF8 deficiency," cross‑referenced to **OMIM:614893, Orphanet:319600, DOID:0111986, MedGen:814919 (UMLS C3808589), GARD:0017463**, with synonyms including "immunodeficiency 32A / IMD32A" and "autosomal dominant … partial deficiency." The **partial/dominant form = OMIM 614893 = IMD32A** (correcting an earlier A/B label swap); the **complete/recessive form = OMIM 614894 = IMD32B**. UniProt **Q02556** (IRF8, 426 aa) shows residue 80 = Thr, 108 = Lys, 83 = Arg; the sole annotated DNA‑binding feature — the **"IRF tryptophan pentad repeat" spanning aa 7–114** — contains both Thr80 and Lys108, explaining why both variants disrupt IRF8–DNA interaction.

### Finding 6 — Official HPO phenotype annotations for OMIM:614893

The JAX HPO annotation network for OMIM:614893 (gene NCBIGene:3394 *IRF8*), all sourced to [PMID: 21524210](https://pubmed.ncbi.nlm.nih.gov/21524210/), lists: **HP:0020086 BCGitis (2/2)**, **HP:0032252 Granuloma (2/2)**, **HP:0002716 Lymphadenopathy (2/2)**, **HP:0011463 Childhood onset (2/2)**, **HP:0001945 Fever (1/2)**, **HP:0002840 Lymphadenitis (1/2)**, HP:0002721 Immunodeficiency, HP:0002719 Recurrent infections, and **HP:0000006 Autosomal dominant inheritance**. Frequencies derive from the two otherwise‑healthy T80A subjects with curable disseminated BCG disease.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous missense variant in *IRF8*** (prototypically c.238A>G, p.Thr80Ala) arises in the germline **→ results in** a single mutant IRF8 allele encoding a protein with an amino‑acid substitution in the DNA‑binding domain (IRF tryptophan pentad repeat, aa 7–114).
2. The Thr80Ala substitution **→ disrupts the IRF8–DNA interaction** (demonstrated in vitro; Hambleton 2011), lowering IRF8's ability to bind composite EICE/ISRE elements **→ results in** reduced IRF8 transcriptional output (a partial, not complete, loss of function).
3. Because myeloid lineage commitment is **IRF8 dose‑dependent** (Nishiyama & Tamura 2025), the reduced functional IRF8 dose **→ leads to** a selective failure to specify/maintain the **CD11c⁺CD1c⁺ conventional dendritic cell (cDC2)** compartment, while monocytes and other subsets are relatively spared (contrast: complete deficiency ablates all DCs + monocytes).
4. Selective cDC2 depletion **→ impairs** antigen presentation and, critically, **IL‑12/IL‑23 production** by the dendritic‑cell compartment (*inferred* from the shared MSMD circuit; the DC subset is a physiological IL‑12 source feeding the axis).
5. Reduced IL‑12/23 **→ results in** blunted **IFN‑γ** production by T cells and NK cells (the non‑redundant MSMD circuit; Qian 2026).
6. Deficient IFN‑γ signaling **→ leads to** inadequate **macrophage activation** and failure to kill ingested intracellular mycobacteria.
7. Uncontrolled mycobacterial replication (BCG vaccine strain, environmental/non‑tuberculous mycobacteria, or *M. tuberculosis*) **→ produces** the clinical phenotype: **granuloma formation, lymphadenitis/lymphadenopathy, BCGitis, fever**, and disseminated but (in the partial form) **curable** mycobacterial disease.

**Branch point:** The same gene, when hit by a *biallelic complete* loss‑of‑function (recessive K108E) or a *dominant‑negative* allele (e.g., c.1279dupT p.\*427Leuext\*42), diverts to a **more severe branch** — loss of monocytes and all DC subsets (K108E) or additional pDC/cDC1 loss with broadened viral susceptibility (dominant‑negative) — producing a life‑threatening syndrome that typically requires HSCT.

```
        IRF8 T80A (het, DBD)                 IRF8 K108E (biallelic)
                │                                     │
    partial ↓ transcriptional activity      complete loss of function
                │                                     │
     selective cDC2 (CD1c+) depletion       loss of ALL DCs + monocytes
                │                                     │
        ↓ IL-12/23 from DC                     global APC failure
                │                                     │
            ↓ IFN-γ                          severe multi-lineage defect
                │                                     │
   ↓ macrophage killing of mycobacteria      overwhelming infection
                │                                     │
   CURABLE disseminated BCG/NTM disease      LIFE-THREATENING → HSCT
   (MSMD, IMD32A / OMIM 614893)              (IMD32B / OMIM 614894)
```

### Coverage of mechanism checklist

- **Molecular pathways:** IL‑12/23 → IFN‑γ signaling axis (JAK‑STAT/STAT1 downstream); IRF8 transcriptional regulation via EICE (Ets/IRF composite) and ISRE elements. GO terms: **GO:0035722** (interleukin‑12‑mediated signaling), **GO:0060333** (interferon‑gamma‑mediated signaling), **GO:0006357** (regulation of transcription by RNA Pol II), **GO:0002250** (adaptive immune response).
- **Cellular processes:** dendritic cell differentiation (**GO:0097028**), myeloid cell differentiation (**GO:0030099**), antigen processing and presentation, granuloma formation, macrophage activation (**GO:0042116**).
- **Protein dysfunction:** loss of function via disrupted DNA binding (partial, T80A) vs. loss of nuclear localization/stability (K108E; PMID 25122610) vs. dominant‑negative sequestration (c.1279dupT; PMID 40072380).
- **Immune system involvement:** immunodeficiency (predisposition to intracellular pathogens); not primarily autoimmune, though granulomatous/inflammatory manifestations occur.
- **Cell types (CL):** conventional dendritic cell type 2 / CD1c⁺ DC (**CL:0001057 / CL:0002399**), conventional dendritic cell (**CL:0000990**), monocyte (**CL:0000576**), macrophage (**CL:0000235**), plasmacytoid DC (**CL:0000784**), neutrophil (**CL:0000775**).

---

## Anatomical, Temporal, Population, Diagnostic, Treatment & Related Sections

### Anatomical structures affected
- **Primary:** immune/hematopoietic system — bone marrow myeloid progenitors, circulating dendritic cell compartment (**UBERON:0002371** bone marrow; **UBERON:0000178** blood).
- **Secondary organ involvement:** lymph nodes (**UBERON:0000029**) — lymphadenopathy/lymphadenitis; spleen and liver (**UBERON:0002106 / UBERON:0002107**) — organomegaly; skin — BCGitis at inoculation site; potentially disseminated (lungs, bone).
- **Subcellular:** nucleus (**GO:0005634**) — site of IRF8 transcriptional action; the T80A defect impairs nuclear DNA binding, the K108E defect impairs nuclear import.
- **Lateralization:** typically regional/multifocal lymphadenopathy (35.1% multifocal in the MSMD cohort), not strictly lateralized.

### Temporal development
- **Onset:** childhood (HP:0011463); mean age across MSMD ~10.4 years; BCG complications appear after neonatal/infant vaccination in BCG‑vaccinating countries.
- **Course:** infection‑triggered and episodic; the partial form is comparatively mild and **curable** with antimycobacterial therapy — distinct from the chronic/lethal recessive form.
- **Critical period:** post‑BCG vaccination in infancy; environmental mycobacterial exposure throughout childhood.

### Inheritance and population
- **Inheritance:** autosomal dominant (HP:0000006), dosage‑sensitive haploinsufficiency / partial loss of function.
- **Penetrance/expressivity:** variable; the disease is defined from very few families, so precise penetrance is unknown. Both T80A carriers were otherwise healthy apart from mycobacterial disease.
- **Allele frequency:** T80A and K108E both absent from gnomAD v4 (ultra‑rare).
- **Epidemiology:** MSMD collectively is rare; highest reported patient frequencies in Iran, Turkey, Saudi Arabia (partly reflecting consanguinity for recessive forms and endemic TB/BCG use). Partial IRF8 deficiency specifically is described in only a handful of families.

### Diagnostics
- **Immunophenotyping (flow cytometry):** selective reduction of circulating **CD11c⁺CD1c⁺ (cDC2)** dendritic cells with preserved monocytes — the hallmark distinguishing partial from complete IRF8 deficiency (which shows monocytopenia + absent DCs + granulocytic hyperplasia).
- **Genetic testing:** single‑gene *IRF8* sequencing, MSMD gene panels, or WES/WGS; interpret against ClinVar (T80A likely pathogenic, K108E pathogenic).
- **Microbiology/histopathology:** tissue and blood culture with special attention to mycobacteria; granuloma on biopsy (non‑caseating or atypical). MSMD can masquerade as sarcoidosis or Rosai‑Dorfman disease until cultures reveal mycobacteria (PMID 40755768).
- **Differential diagnosis:** other MSMD genes (IL12RB1, IL12B, IFNGR1/2, STAT1, TYK2, SPPL2A, etc.), chronic granulomatous disease, and non‑infectious granulomatous/histiocytic disorders.

### Treatment
- **Antimycobacterial therapy:** multi‑drug regimens tailored to the isolated organism; the partial form is typically **cured** with appropriate antibiotics.
- **Adjunctive IFN‑γ:** recombinant IFN‑γ (subcutaneous) to bolster macrophage activation in the IL‑12/IFN‑γ axis (NCIT:C20495 Interferon Gamma).
- **HSCT:** reserved for severe/recessive complete IRF8 deficiency (K108E patient cured by cord‑blood transplant, PMID 25122610); generally **not required** for the partial dominant form.
- **BCG avoidance / management of BCG complications** in known carriers.

### Prevention
- **Primary:** avoid live BCG vaccination in individuals with a family history or confirmed *IRF8* variant.
- **Secondary:** cascade genetic testing of relatives; early recognition of unexplained childhood lymphadenopathy with mycobacterial workup.
- **Counseling:** autosomal dominant inheritance implies ~50% transmission risk; genetic counseling and prenatal/preimplantation options where desired.

### Other species / model organisms
- **Ortholog:** mouse *Irf8* (HomoloGene group 1629). The **BXH2 mouse** carries an *Irf8* R294 mutation orthologous to human R294/R291Q (PMID 29128673) and models IRF8 deficiency. Zebrafish and other vertebrates possess DC‑like cells with conserved IRF8‑dependent programs (PMID 41379882).
- **Model utility:** dose‑dependent knock‑in/knockout mice recapitulate DC lineage defects and mycobacterial susceptibility; useful for studying enhancer regulation (PMID 40680811, 40378239) and immunotherapeutic IRF8 reprogramming (PMID 39115195, glioblastoma model).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [21524210](https://pubmed.ncbi.nlm.nih.gov/21524210/) | *IRF8 mutations and human dendritic‑cell immunodeficiency* (Hambleton, NEJM 2011) | **Foundational.** Defines T80A (dominant, partial, selective cDC2 loss, curable BCG disease) vs K108E (recessive, complete). Source of HPO frequencies. |
| [38341181](https://pubmed.ncbi.nlm.nih.gov/38341181/) | *830 MSMD patients: systematic review* (Khavandegar 2024) | Epidemiology & clinical frequencies (lymphadenopathy 45.5%, fever 30.2%, organomegaly 24.8%, sepsis 20.8%). |
| [42183200](https://pubmed.ncbi.nlm.nih.gov/42183200/) | *MSMD: IFN‑γ‑driven immunity collapse* (Qian 2026) | 22 genes converge on IL‑12/23–IFN‑γ circuit; ~50% unsolved. |
| [40680811](https://pubmed.ncbi.nlm.nih.gov/40680811/) | *Cis/trans regulation of Irf8 enhancers* (Nishiyama & Tamura 2025) | IRF8 dose‑dependence of myeloid cell fate — explains subset‑selective phenotype. |
| [29128673](https://pubmed.ncbi.nlm.nih.gov/29128673/) | *Biallelic IRF8 mutation* (Bigley 2018) | BXH2 mouse ortholog (R294); IRF8 mutants fail to regulate EICE/ISRE. |
| [40072380](https://pubmed.ncbi.nlm.nih.gov/40072380/) | *Novel dominant‑negative IRF8* (Ham 2025) | Dominant‑negative form → decreased cDC2 + mycobacterial susceptibility; broadens phenotype. |
| [25122610](https://pubmed.ncbi.nlm.nih.gov/25122610/) | *Functional characterization of IRF8 K108E* | Complete recessive form: absent monocytes/DCs, granulocytic hyperplasia, cured by cord‑blood transplant; K108E loses nuclear localization/stability. |
| [40755768](https://pubmed.ncbi.nlm.nih.gov/40755768/) | *Hidden immune defects in childhood granulomatous disorders* | MSMD masquerading as sarcoidosis/Rosai‑Dorfman until cultures reveal mycobacteria — diagnostic caution. |
| [38535546](https://pubmed.ncbi.nlm.nih.gov/38535546/) | *Diagnosis & management of infections in MSMD* | BCG vs NTM vs MTB spectrum; culture challenges. |
| [41786143](https://pubmed.ncbi.nlm.nih.gov/41786143/) | *IL‑12/IFN‑γ axis defects and MSMD* | Management review: antibiotics, cytokine therapy, BMT. |
| [39115195](https://pubmed.ncbi.nlm.nih.gov/39115195/) | *IRF8 reprogramming in murine glioblastoma* | Confirms IRF8 as master regulator of cDC1 development (mechanistic corroboration). |

**Evidence source types:** human clinical (21524210, 25122610, 29128673, 40072380, 38341181, 40755768), model organism (29128673 BXH2 mouse, 39115195 murine GBM, 41379882 zebrafish), in vitro functional (21524210, 25122610, 40072380, 40680811), database/computational (gnomAD, ClinVar, UniProt Q02556, EBI OLS4, HPO/JAX, HomoloGene).

---

## Limitations and Knowledge Gaps

1. **Very small case base.** The dominant/partial IRF8 phenotype rests principally on two T80A subjects (Hambleton 2011) plus additional dominant‑negative families (Ham 2025). Penetrance, expressivity, sex ratio, and precise prevalence are therefore poorly quantified.
2. **Frequency figures are low‑denominator.** HPO frequencies (e.g., BCGitis 2/2, fever 1/2) derive from n=2 and should not be over‑interpreted as population estimates.
3. **Direct IL‑12/IFN‑γ measurements in T80A patients** are sparse; the cytokine‑axis steps in the causal chain are partly *inferred* from the shared MSMD circuit rather than demonstrated specifically for T80A.
4. **Genotype–phenotype boundaries** between partial LoF (T80A), dominant‑negative (c.1279dupT), and complete LoF (K108E) are still being refined; the dominant‑negative form additionally affects pDC/cDC1 and confers viral (EBV/HPV) susceptibility, blurring the classic partial‑MSMD picture.
5. **No natural‑history or registry data** specific to partial IRF8 deficiency; long‑term outcomes, relapse rates, and optimal duration of therapy are undefined.
6. **Modifier genes, epigenetics, and gene–environment interactions** (e.g., BCG strain, mycobacterial burden, endemic TB) are plausible but uncharacterized for this specific genotype.

---

## Proposed Follow‑up Experiments / Actions

1. **Aggregate an international IRF8‑MSMD cohort** (GeneMatcher, MSMD consortia) to establish penetrance, expressivity, and outcome data for dominant/partial variants specifically.
2. **Deep immunophenotyping** (spectral flow / CyTOF) of T80A carriers to quantify cDC2 vs cDC1 vs pDC vs monocyte fractions and map the exact DC‑subset bottleneck.
3. **Functional cytokine assays** (IL‑12/IL‑23 and IFN‑γ production upon TLR/mycobacterial stimulation) in patient PBMCs to convert inferred causal‑chain steps 4–6 into demonstrated ones.
4. **Isogenic knock‑in models** (T80A heterozygous mouse or human iPSC‑derived DCs) to test dose‑dependence directly and compare with BXH2/R294.
5. **Single‑cell multi‑omics of bone‑marrow progenitors** to define where in the myeloid hierarchy the partial IRF8 dose becomes limiting.
6. **Prospective trial of adjunctive IFN‑γ** vs antimycobacterials alone in genetically confirmed partial IRF8 deficiency to formalize treatment algorithms.
7. **Curate the KB entry** with the ontology appendix below and flag the historical OMIM A/B label swap (IMD32A = 614893 = partial/dominant; IMD32B = 614894 = complete/recessive).

---

## Ontology Term Appendix (for KB population)

**Disease:** MONDO:0013957 · OMIM:614893 (IMD32A) · Orphanet:319600 · DOID:0111986 · MedGen:814919 · GARD:0017463
**Gene/Protein:** HGNC:5358 *IRF8* · NCBIGene:3394 · Ensembl ENSG00000140968 · UniProt Q02556 · chr16q24.1
**Variants:** NM_002163.4:c.238A>G p.Thr80Ala (ClinVar likely pathogenic) · c.322A>G p.Lys108Glu (ClinVar pathogenic, recessive/IMD32B)
**Phenotypes (HP):** HP:0020086 BCGitis · HP:0032252 Granuloma · HP:0002716 Lymphadenopathy · HP:0002840 Lymphadenitis · HP:0001945 Fever · HP:0011463 Childhood onset · HP:0002721 Immunodeficiency · HP:0002719 Recurrent infections · HP:0000006 Autosomal dominant inheritance
**Biological processes (GO):** GO:0035722 · GO:0060333 · GO:0097028 · GO:0030099 · GO:0006357 · GO:0042116 · GO:0002250
**Cellular component (GO):** GO:0005634 nucleus
**Cell types (CL):** CL:0001057 / CL:0002399 CD1c⁺/cDC2 · CL:0000990 conventional DC · CL:0000784 pDC · CL:0000576 monocyte · CL:0000235 macrophage · CL:0000775 neutrophil
**Anatomy (UBERON):** UBERON:0002371 bone marrow · UBERON:0000178 blood · UBERON:0000029 lymph node · UBERON:0002106 spleen · UBERON:0002107 liver
**Infectious agents (NCBI Taxon):** *Mycobacterium bovis* BCG (Taxon:33892) · non‑tuberculous mycobacteria · *M. tuberculosis* (Taxon:1773)
**Treatments (NCIT):** antimycobacterial antibiotics · NCIT:C20495 Interferon Gamma · hematopoietic stem cell transplantation (severe/recessive only)
**Model organism:** *Mus musculus Irf8* (HomoloGene 1629); BXH2 strain (Irf8 R294)

---

*Report compiled across 5 discovery iterations; 7 findings recorded, 18 papers reviewed, ~11 primary PMIDs cited, all identifiers database‑verified (gnomAD, ClinVar, UniProt, EBI OLS4, JAX/HPO, HomoloGene).*


## Artifacts

- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Partial_IRF8_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Partial_IRF8_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

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
| Terms checked | 40 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 9 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013957` (6 mentions) - the report calls it "if available"; MONDO calls it **Mendelian susceptibility to mycobacterial diseases due to partial IRF8 deficiency**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`, `NCBIGene`, `Taxon`.
