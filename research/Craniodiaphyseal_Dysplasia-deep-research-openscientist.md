---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T19:10:54.286786'
end_time: '2026-09-23T19:42:31.917688'
duration_seconds: 1897.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Craniodiaphyseal Dysplasia
  mondo_id: MONDO:0021021
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Craniodiaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Craniodiaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniodiaphyseal Dysplasia
- **MONDO ID:** MONDO:0021021 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Craniodiaphyseal Dysplasia** covering all of the
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

# Craniodiaphyseal Dysplasia (CDD): A Comprehensive Disease Characterization Report

**Target disease:** Craniodiaphyseal Dysplasia
**MONDO:** MONDO:0021021 | **OMIM:** 122860 (autosomal dominant) | **Orphanet:** ORPHA:1513 | **Category:** Mendelian sclerosing bone dysplasia

---

## Summary

Craniodiaphyseal dysplasia (CDD) is an extremely rare, severe, progressive sclerosing bone dysplasia characterized by massive generalized hyperostosis and sclerosis of the skull and facial bones ("leontiasis ossea") together with diaphyseal hyperostosis and defective modeling of the long bones. The relentless deposition of bone progressively narrows the craniofacial foramina and encroaches on the brain, compressing cranial nerves, the foramen magnum, and intracranial contents. The clinical consequences — blindness, sensorineural and conductive hearing loss, facial palsy, raised intracranial pressure, seizures, and premature death — arise directly from this mechanical encroachment rather than from a metabolic or systemic derangement.

The molecular basis of the classic **autosomal-dominant** form is a defect in the secretion of **sclerostin**, the osteocyte-derived protein encoded by *SOST*. Heterozygous mutations in the *SOST* secretion signal peptide (**c.61G>A, p.Val21Met**; **c.61G>T, p.Val21Leu**) greatly reduce sclerostin secretion through a **dominant-negative** mechanism, which distinguishes CDD from the recessive loss-of-function *SOST* disorders sclerosteosis and van Buchem disease. Sclerostin normally binds the Wnt co-receptors LRP4/5/6 to antagonize canonical Wnt/β-catenin signaling in osteoblasts; when secreted sclerostin is reduced, this brake on bone formation is released, canonical Wnt signaling is de-repressed, and osteoblast-driven hyperostosis ensues. A phenotypically overlapping **recessive** form is caused by biallelic loss-of-function variants in *SP7*/Osterix, an osteoblast master transcription factor, establishing genetic heterogeneity for the CDD phenotype.

There is no approved disease-modifying pharmacotherapy. Management is symptomatic and surgical — decompressive craniectomy, staged craniofacial reduction osteoplasty, and rehabilitation of hearing loss (including bone-anchored hearing aids). The sclerostin–Wnt axis is strongly validated in the opposite (therapeutic) direction by the anti-sclerostin antibody romosozumab, which is bone-anabolic in osteoporosis — confirming the direction of CDD causality but implying that no safe pro-sclerostin ("bone-quieting") therapy yet exists. Preclinical leads include the chemical chaperone sodium 4-phenylbutyrate (4-PBA), which suppresses hyperostosis in an osteocyte unfolded-protein-response (UPR) mouse model consistent with CDD, and competitive modulation of the LRP4/6–sclerostin interface.

---

## 1. Disease Information

**Overview.** CDD is "a rare, sporadic form of craniotubular bone dysplasia, characterized by massive generalized hyperostosis and sclerosis, particularly of the skull and facial bones, leading to severe deformity" ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). It is regarded as the most severe member of the *SOST*-related craniotubular hyperostosis spectrum.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0021021 |
| OMIM | 122860 (Craniodiaphyseal dysplasia, autosomal dominant) |
| Orphanet | ORPHA:1513 (Craniodiaphyseal dysplasia) |
| ICD-10 | Q78.8 (Other specified osteochondrodysplasias) |
| ICD-11 | LD24.Y / FB80.Y (skeletal dysplasia grouping) |
| MeSH | Craniofacial / hyperostosis terms (no dedicated unique descriptor) |
| Gene(s) | *SOST* (dominant); *SP7*/Osterix (recessive) |

**Synonyms / alternative names.** Craniodiaphyseal dysplasia; CDD; "leontiasis ossea" is a descriptive term for the facial appearance (not a synonym for the disease as a whole).

**Information source.** The evidence base is derived almost entirely from **aggregated disease-level resources and individual published case reports / small case series** (OMIM, Orphanet, and a limited primary literature of fewer than ~two dozen reported patients), rather than from EHR-derived cohorts. This is a direct consequence of the disease's extreme rarity.

---

## 2. Etiology

**Primary cause — genetic.** CDD is a monogenic Mendelian disorder.

- **Autosomal-dominant CDD** is caused by heterozygous missense mutations in the **secretion signal peptide of *SOST*** (sclerostin). Kim et al. (2011) identified c.61G>A (p.Val21Met) and c.61G>T (p.Val21Leu) in two unrelated children with CDD: *"We discovered mutations c.61G>A (Val21Met) and c.61G>T (Val21Leu) [in] two children with CDD. As these mutations are located in the secretion signal of the SOST gene, we tested their effect on secretion by transfecting the mutant constructs into 293E cells. Intriguingly, these mutations greatly reduced the secretion of SOST"* ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/)).
- **Autosomal-recessive CDD** is caused by biallelic variants in ***SP7*/Osterix**, an osteoblast transcription factor (Hendrickx et al. 2023, [PMID: 36436818](https://pubmed.ncbi.nlm.nih.gov/36436818/); Gauthier et al. 2024, [PMID: 37918503](https://pubmed.ncbi.nlm.nih.gov/37918503/)).

**Genetic risk factors.** The causal variants are themselves the risk determinants; there are no established common susceptibility loci or modifier genes for this ultra-rare Mendelian condition. Most dominant cases appear to arise **de novo** (sporadic), consistent with the disease's severity and reproductive impact.

**Environmental risk factors.** None established. CDD is not attributable to toxins, infection, nutrition, occupation, age, or sex. Family history is relevant only in the rare familial / recessive settings.

**Protective factors.** None identified. No protective alleles or environmental exposures are known.

**Gene–environment interactions.** None documented. The osteocyte UPR (endoplasmic reticulum stress) has been proposed as an intracellular **contributory amplifier** of the phenotype (see Section 6), but this is a cell-biological mechanism rather than an environmental exposure.

---

## 3. Phenotypes

CDD phenotypes are predominantly **physical/skeletal manifestations and clinical signs**, with secondary **neurological** signs from bony encroachment. Onset is in **early childhood**, severity is **severe**, and the course is **progressive**.

| Phenotype | Type | Suggested HPO | Onset / severity / course | Notes & evidence |
|---|---|---|---|---|
| Cranial hyperostosis / sclerosis | Physical/imaging | HP:0004493 (Thickened calvaria); HP:0004437 (Cranial hyperostosis) | Childhood; severe; progressive | Calvarial thickness "nearly 4 cm" ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)) |
| Facial hyperostosis / distortion ("leontiasis ossea") | Physical sign | HP:0011856 (facial bone hyperostosis) | Childhood; severe; progressive | Massive facial bone deposition ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)) |
| Macrocephaly | Physical sign | HP:0000256 | Childhood | ([PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)) |
| Diaphyseal hyperostosis / defective long-bone modeling (undertubulation) | Imaging | HP:0100670 (Diaphyseal sclerosis); HP:0005791 (Undertubulation) | Childhood; progressive | ([PMID: 1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/); [PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)) |
| Clavicular / rib / axial sclerosis | Imaging | HP:0100692 (Sclerotic clavicle) | Childhood; progressive | ([PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)) |
| Optic atrophy / visual loss / blindness | Neurological sign | HP:0000648 (Optic atrophy); HP:0000618 (Blindness) | Childhood–adolescence; progressive | Cranial-nerve II compression ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)) |
| Hearing loss (sensorineural + conductive) | Sign | HP:0000407 (SNHL); HP:0000405 (conductive) | Childhood; progressive | ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/); [PMID: 31132523](https://pubmed.ncbi.nlm.nih.gov/31132523/)) |
| Facial nerve palsy | Sign | HP:0010628 (Facial palsy) | Childhood; progressive | Foraminal narrowing ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)) |
| Raised intracranial pressure | Sign | HP:0002516 | Childhood; progressive | ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/); [PMID: 1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/)) |
| Seizures | Sign | HP:0001250 | Variable | ([PMID: 1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/)) |

**Frequency.** Because reported cases number only in the low tens, phenotype frequencies are qualitative. Craniofacial hyperostosis, facial distortion, and diaphyseal long-bone involvement are essentially **universal (defining features)**; cranial-nerve compression syndromes (visual loss, hearing loss, facial palsy) and raised ICP are **common** and progressive.

**Quality-of-life impact.** Severe and multi-domain: progressive sensory loss (blindness, deafness), facial disfigurement, chronic headache from raised ICP, and neurological morbidity substantially impair daily functioning. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal genes.**

| Gene | HGNC / locus | Inheritance | OMIM | Role |
|---|---|---|---|---|
| *SOST* (sclerostin) | HGNC:13771; 17q21.31 | Autosomal dominant | 122860 (CDD); 605740 (*SOST*) | Osteocyte-secreted Wnt antagonist |
| *SP7* / Osterix | HGNC:17321; 12q13.13 | Autosomal recessive | 606633 (*SP7*) | Osteoblast master transcription factor |

**Pathogenic variants (dominant *SOST*).**

- **c.61G>A (p.Val21Met)** and **c.61G>T (p.Val21Leu)** — missense substitutions within the **secretion signal peptide**. Both were shown to greatly reduce SOST secretion in transfected 293E cells ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/)).
- **Variant type/class:** missense, signal-peptide.
- **Functional consequence:** **dominant-negative** reduction of extracellular sclerostin (not simple haploinsufficiency). Kim et al. conclude: *"Unlike the other SOST-related conditions, sclerosteosis and Van Buchem disease that are inherited as recessive traits[, CDD] seem to be caused by a dominant negative mechanism"* ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/)).
- **Classification (ACMG/AMP):** pathogenic (functional secretion assay + segregation with severe phenotype).
- **Allele frequency:** absent from population databases (gnomAD) — private, disease-causing variants.
- **Origin:** germline; dominant cases frequently de novo.

**Pathogenic variants (recessive *SP7*).** Gauthier et al. reported biallelic loss-of-function variants — **c.359_362del (p.Asp120Valfs\*11)** and **c.1163_1174delinsT (p.Pro388Leufs\*33)** — producing a sclerotic skeletal dysplasia overlapping juvenile Paget's disease and CDD: *"SP7 variants may also cause sclerotic skeletal dysplasias (SSD), partially overlapping with Juvenile Paget's disease and craniodiaphyseal dysplasia, characterized by skull hyperostosis, long bones sclerosis, large ribs and clavicles, and possible recurrent fractures"* ([PMID: 37918503](https://pubmed.ncbi.nlm.nih.gov/37918503/)). These are biallelic frameshift loss-of-function variants.

**Modifier genes.** None formally established. The wider Wnt/sclerostin axis genes (*LRP4*, *LRP5*, *LRP6*) are mechanistically adjacent (Section 6) and were explicitly excluded in a mild adult CDD-like case (Janssens et al. 2003, [PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)).

**Epigenetic information.** No disease-specific DNA-methylation or histone data for CDD. At the mechanistic level, osteocyte ER stress/UPR modulates *SOST* transcription (Section 6), but this is regulatory rather than a documented epigenetic mark.

**Chromosomal abnormalities.** None; CDD is a single-gene disorder without characteristic aneuploidy, translocation, or copy-number signature.

---

## 5. Environmental Information

- **Environmental factors:** None identified. CDD is not linked to toxins, radiation, or occupational exposure.
- **Lifestyle factors:** None. Not related to smoking, diet, exercise, or alcohol.
- **Infectious agents:** Not applicable; CDD is non-infectious.

*(The osteocyte UPR mechanism (Section 6) is an intrinsic cell-stress pathway, not an environmental exposure, though in principle it could be modulated pharmacologically.)*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous *SOST* signal-peptide mutation** (p.Val21Met / p.Val21Leu) is present in osteocytes → **impairs trafficking/secretion of sclerostin** (demonstrated in 293E cells) via a **dominant-negative** effect ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/)).
2. Reduced secretion **leads to** decreased **extracellular sclerostin** available at the bone surface.
3. Because sclerostin normally **binds LRP4/5/6 to antagonize canonical Wnt/β-catenin signaling**, its deficiency **results in de-repression (activation) of Wnt/β-catenin signaling** in osteoblasts ([PMID: 19936252](https://pubmed.ncbi.nlm.nih.gov/19936252/); [PMID: 35099616](https://pubmed.ncbi.nlm.nih.gov/35099616/)).
4. Activated Wnt signaling **drives osteoblast commitment, differentiation, and enhanced periosteal/endosteal bone formation** → **generalized hyperostosis** ([PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/)).
5. *(Inferred amplifier branch)* Osteocyte **ER stress / unfolded protein response (UPR)** can independently **delay osteocyte maturation and suppress *SOST* expression**, converging on the same "low sclerostin → active Wnt → hyperostosis" output ([PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/)).
6. Sustained bone deposition **produces craniofacial + diaphyseal hyperostosis** that **narrows the skull foramina and the foramen magnum**.
7. Foraminal narrowing **compresses cranial nerves and the brainstem**, which **results in** optic atrophy/blindness, sensorineural + conductive hearing loss, facial palsy, raised intracranial pressure, and death ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)).

**Convergent recessive branch:** biallelic **loss of *SP7*/Osterix** disrupts osteoblast transcriptional programming and **leads to** an overlapping sclerotic skeletal phenotype ([PMID: 36436818](https://pubmed.ncbi.nlm.nih.gov/36436818/); [PMID: 37918503](https://pubmed.ncbi.nlm.nih.gov/37918503/)).

```
 SOST signal-peptide mutation (dominant-negative)          SP7/Osterix biallelic LOF
              |                                                      |
   impaired sclerostin secretion                          disrupted osteoblast
              |                                            transcriptional program
     ↓ extracellular sclerostin                                     |
              |                                                     |
   de-repressed Wnt/β-catenin  ←── (osteocyte UPR suppresses SOST)  |
              |                                                     |
     ↑ osteoblast bone formation  ←─────────────────────────────────┘
              |
   generalized HYPEROSTOSIS (cranium, face, diaphyses)
              |
   narrowing of skull foramina / foramen magnum
              |
   cranial-nerve & brainstem compression → blindness, deafness,
   facial palsy, ↑ICP, death
```

### Detail by category

- **Molecular pathways:** Canonical **Wnt/β-catenin** signaling is the central pathway; sclerostin is its physiologic osteocyte-derived antagonist acting at **LRP4/5/6** co-receptors. Sclerostin also modulates **BMP** signaling ([PMID: 19936252](https://pubmed.ncbi.nlm.nih.gov/19936252/)).
- **Cellular processes:** Osteoblast commitment, differentiation, matrix formation/mineralization; osteocyte maturation. GO suggestions: **GO:0001649** (osteoblast differentiation), **GO:0060348** (bone development), **GO:0045668** (negative regulation of osteoblast differentiation — normally exerted by sclerostin), **GO:0016055** (Wnt signaling pathway), **GO:0030282** (bone mineralization), **GO:0030968** (endoplasmic reticulum unfolded protein response).
- **Protein dysfunction:** Sclerostin (**UniProt Q9BQB4**) is a secreted glycoprotein; the signal-peptide mutation impairs its **secretion**, reducing the extracellular pool — a functional loss at the tissue level achieved through a dominant-negative cellular mechanism.
- **Metabolic changes:** No characteristic systemic metabolic derangement in CDD. (Osteocyte bioenergetics/PPARG links to sclerostin exist in the broader literature but are not CDD-specific.)
- **Immune system involvement:** None; CDD is not an immunologic or inflammatory disease.
- **Tissue-damage mechanisms:** Injury is **mechanical/compressive** — bony encroachment on neural foramina causing compression neuropathy of cranial nerves and brainstem, plus raised ICP — rather than oxidative, fibrotic, or necrotic.
- **Biochemical abnormalities:** Deficiency of functional extracellular sclerostin at the osteocyte–osteoblast interface.
- **Epigenetic changes:** Not established for CDD.
- **Molecular profiling:** No human transcriptomic/proteomic/metabolomic CDD datasets; mechanistic data derive from mouse models and in vitro assays.

**Cell types involved (CL suggestions):** osteocyte (**CL:0000137**), osteoblast (**CL:0000062**), osteoprogenitor/mesenchymal stem cell (**CL:0000134**). **Anatomical/UBERON:** cranium/skull (**UBERON:0003128 / UBERON:0000209**), facial bone, diaphysis of long bone (**UBERON:0004769**), periosteum (**UBERON:0002515**), foramen magnum.

---

## 7. Anatomical Structures Affected

**Organ level.**
- *Primary:* **Bone** — skull/calvaria, facial bones, mandible; long-bone diaphyses; clavicles, ribs, axial skeleton (macrocephaly; near-4-cm calvarial thickness; [PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/); [PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)).
- *Secondary:* **Nervous system** — cranial nerves (II optic, VII facial, VIII vestibulocochlear), brainstem, and brain, through foraminal narrowing and raised ICP ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)); **special-sense organs** (visual and auditory systems).
- *Body systems:* skeletal (primary); nervous and sensory (secondary).

**Tissue and cell level.** Connective tissue — bone. Cellular effectors: **osteoblasts** (excessive bone formation) driven by loss of the **osteocyte**-derived sclerostin brake (CL:0000062, CL:0000137).

**Subcellular level.** **Endoplasmic reticulum / secretory pathway** — the signal-peptide mutation impairs ER-to-extracellular trafficking of sclerostin; osteocyte **ER stress/UPR** is implicated as an amplifier. GO cellular-component suggestions: **GO:0005783** (endoplasmic reticulum), **GO:0005576** (extracellular region), **GO:0005615** (extracellular space).

**Localization / lateralization.** Bilateral and symmetric skeletal involvement. Temporal-bone CT in the *SOST* hyperostosis spectrum shows *"diffuse osteosclerosis affecting the bilateral ossicular chains and internal auditory meatus, as well as stenosis of the bilateral internal auditory meatus"* ([PMID: 40605263](https://pubmed.ncbi.nlm.nih.gov/40605263/)).

---

## 8. Temporal Development

- **Onset:** Early childhood; congenital predisposition with clinical manifestation in the first years of life. Reported probands are children (Kim's two patients; a 10-year-old with hearing loss, [PMID: 31132523](https://pubmed.ncbi.nlm.nih.gov/31132523/); a patient requiring decompression at age 12, [PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). Rare milder cases are diagnosed in adulthood (56-year-old woman, [PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)).
- **Onset pattern:** insidious, chronic.
- **Progression:** relentless and progressive — *"progressive encroachment of the craniofacial foramina and brain by the relentless deposition of bone"* ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). No spontaneous remission.
- **Disease course:** chronic, lifelong, progressive; not episodic or relapsing-remitting.
- **Critical periods:** Childhood and adolescence — the window in which bony overgrowth compromises neural foramina and interventions (decompression) can preserve vision, hearing, and life.

---

## 9. Inheritance and Population

**Epidemiology.** Extremely rare — described as *"extremely rare"* ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/)) and *"a rare, sporadic form of craniotubular bone dysplasia"* ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). Orphanet lists an estimated prevalence **<1/1,000,000**; fewer than ~two dozen cases are reported worldwide. Precise incidence/prevalence figures cannot be reliably estimated.

**Genetic etiology.**
- **Inheritance:** **Autosomal dominant** (*SOST* signal-peptide mutations), typically de novo/sporadic; **autosomal recessive** (biallelic *SP7*/Osterix).
- **Penetrance / expressivity:** Dominant *SOST* cases are severe and appear highly penetrant; expressivity is variable across the *SOST* hyperostosis spectrum (severe classic CDD to milder adult-diagnosed cases).
- **Genetic anticipation:** Not applicable (no repeat-expansion mechanism).
- **Germline mosaicism / founder effects / consanguinity:** No documented founder effect for CDD; consanguinity is relevant to the recessive *SP7* form. (By contrast, the related recessive disorder **sclerosteosis** shows a well-known Afrikaner founder effect: minimum prevalence ~1/75,000, gene frequency ~0.0035, [PMID: 187366](https://pubmed.ncbi.nlm.nih.gov/187366/) — but this is a distinct disease.)
- **Carrier frequency:** Not applicable for the dominant form; not established for recessive *SP7*.

**Population demographics.** No ethnic predilection established for CDD; cases are geographically scattered. Sex ratio approximately equal (autosomal inheritance); reported in both sexes, with pregnancies managed in an affected woman ([PMID: 1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/)). Age distribution skews to pediatric diagnosis.

---

## 10. Diagnostics

**Clinical/imaging (the diagnostic cornerstone).**
- **Radiography/CT:** massive skull and facial-bone hyperostosis/sclerosis with facial distortion and macrocephaly; long-bone diaphyseal endostosis with undertubulation (loss of normal metaphyseal modeling); sclerotic clavicles, ribs, and axial skeleton ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/); [PMID: 1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/); [PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)). Janssens et al.: *"marked sclerosis and hyperostosis of the skull bones is present resulting in macrocephaly. Most tubular bones of the limbs, as well as the clavicles, are affected by sclerosis"* ([PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)).
- **Temporal-bone CT (SOST spectrum):** *"diffuse osteosclerosis affecting the bilateral ossicular chains and internal auditory meatus, as well as stenosis of the bilateral internal auditory meatus"* ([PMID: 40605263](https://pubmed.ncbi.nlm.nih.gov/40605263/)).
- **MRI:** skull thickening with loss of the diploic marrow signal.
- **Laboratory tests / biomarkers:** No specific diagnostic blood/urine biomarker. Serum **sclerostin** could in principle be low; bone-turnover markers reflect bone formation but are non-specific. No validated CDD biomarker exists.
- **Audiometry / ophthalmology:** to detect and monitor cranial-nerve compression (hearing loss, optic atrophy).

**Genetic testing (confirmatory).**
- Recommended approach: targeted **single-gene *SOST* sequencing** for suspected dominant CDD; **WES/WGS** or a **sclerosing bone dysplasia gene panel** when the phenotype overlaps other craniotubular disorders, which also captures recessive **_SP7_/Osterix** ([PMID: 21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/); [PMID: 36436818](https://pubmed.ncbi.nlm.nih.gov/36436818/)).
- CMA / karyotype / FISH / mtDNA / repeat-expansion testing are **not** indicated (single-gene, non-structural, non-mitochondrial, non-repeat disorder).

**Clinical criteria / differential diagnosis.** Diagnosis rests on the characteristic craniofacial + diaphyseal radiographic pattern plus molecular confirmation. CDD must be differentiated from other craniotubular hyperostoses:

| Condition | Gene | Inheritance | Distinguishing features vs CDD |
|---|---|---|---|
| **Craniodiaphyseal dysplasia** | *SOST* (signal peptide) / *SP7* | AD / AR | Most severe; massive facial hyperostosis; no syndactyly |
| Sclerosteosis | *SOST* (LOF) | AR | **Syndactyly of 2nd/3rd fingers**, gigantism ([PMID: 1259284](https://pubmed.ncbi.nlm.nih.gov/1259284/); [PMID: 187366](https://pubmed.ncbi.nlm.nih.gov/187366/)) |
| Van Buchem disease | *SOST* (regulatory) | AR | Milder; no syndactyly |
| Craniometaphyseal dysplasia | *ANKH*/*GJA1* | AD/AR | Metaphyseal (not diaphyseal) flaring; can be misdiagnosed as CDD ([PMID: 40639871](https://pubmed.ncbi.nlm.nih.gov/40639871/)) |
| Camurati-Engelmann disease | *TGFB1* | AD | Diaphyseal dysplasia; *TGFB1* excluded in a CDD case ([PMID: 14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/)) |

The three *SOST*-related craniotubular hyperostoses are grouped mechanistically: *"Loss of sclerostin gene function is related to 3 different craniotubular hyperostosis processes: sclerosteosis, craniodiaphyseal dysplasia, and van Buchem disease"* ([PMID: 29264888](https://pubmed.ncbi.nlm.nih.gov/29264888/)). The recessive disorder sclerosteosis is set apart by additional limb findings: *"Sclerosteosis is a unique autosomal recessive condition in which skeletal overgrowth is associated with syndactyly and digital malformation"* ([PMID: 1259284](https://pubmed.ncbi.nlm.nih.gov/1259284/)).

**Screening.** No population newborn or carrier screening (ultra-rare, mostly de novo dominant). **Cascade/prenatal testing** is possible in families with a known variant.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Guarded. The natural course leads to *"compression of cranial nerves, the foramen magnum, and intracranial contents [that] commonly leads to blindness, loss of hearing, and death"* ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). No formal 5-/10-year survival statistics exist owing to rarity; premature death from brainstem/foramen-magnum compression or raised ICP is a recognized outcome.
- **Morbidity / disability:** High and progressive — blindness, deafness, facial palsy, chronic headache, facial disfigurement, neurological impairment. Substantial lifelong disability.
- **Quality of life:** Severely affected across sensory, functional, and psychosocial domains; no disease-specific QoL instruments applied.
- **Complications:** Cranial-nerve palsies, raised intracranial pressure, seizures, and (in the recessive *SP7* form) recurrent fractures ([PMID: 37918503](https://pubmed.ncbi.nlm.nih.gov/37918503/)).
- **Recovery potential:** No spontaneous recovery; surgical decompression can preserve function and life but does not halt the underlying bone deposition.
- **Prognostic factors:** Severity and rate of foraminal narrowing; timeliness of decompressive surgery; degree of cranial-nerve involvement at presentation. No molecular prognostic biomarker validated.

---

## 12. Treatment

**No approved disease-modifying pharmacotherapy exists.** Management is symptomatic, surgical, and rehabilitative.

**Surgical / interventional (mainstay).**
- **Decompressive craniectomy** for raised ICP: *"Significant brain compression with signs and symptoms of increased intracranial pressure was managed successfully with decompressing craniectomy at age 12 years, enlarging the anterior and middle fossae. Calvarial thickness measured nearly 4 cm"* ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)).
- **Staged craniofacial / mandibular reduction osteoplasty** (recontouring) for deformity and foraminal decompression ([PMID: 8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/)). *(NCIT: cranial decompression; craniofacial reconstructive surgery.)*
- Decompression of specific neural foramina (e.g., optic canal, internal auditory meatus) to preserve vision and hearing.

**Supportive / rehabilitative.**
- **Bone-anchored hearing aid (BAHA)** for hearing rehabilitation: *"we describe the first case of craniodiaphysial dysplasia rehabilitated with Bone-Anchored Hearing Aid, despite the concerns inherent to the involvement of the skull bone that characterizes the disease"* ([PMID: 31132523](https://pubmed.ncbi.nlm.nih.gov/31132523/)). *(NCIT: hearing aid; auditory rehabilitation.)*
- Ophthalmologic and audiologic surveillance; symptomatic management of headache and seizures.

**Pharmacotherapy / advanced therapeutics.** None approved. The sclerostin–Wnt axis is **pharmacologically validated in the opposite direction**: the anti-sclerostin antibody **romosozumab** is bone-anabolic — *"Romosozumab, a sclerostin inhibitor with both anabolic and antiresorptive effects"* ([PMID: 42761068](https://pubmed.ncbi.nlm.nih.gov/42761068/)) — increasing spine and hip BMD in osteoporosis (lumbar spine +14.47 ± 8.74%, p<0.001; total hip +4.15 ± 5.92%, p<0.001; [PMID: 42417976](https://pubmed.ncbi.nlm.nih.gov/42417976/)). This confirms that *lowering* sclerostin drives bone gain (the CDD direction) but implies there is **no safe pro-sclerostin ("bone-quieting") therapy** currently available. A theoretical CDD therapy would need to *restore* Wnt inhibition (e.g., sclerostin replacement/mimetic or LRP6 modulation) — the reverse of osteoporosis drug development.

**Experimental / preclinical leads.**
- **Chemical chaperone sodium 4-phenylbutyrate (4-PBA):** suppressed hyperostosis in the osteocyte-UPR mouse model consistent with CDD — *"A clear relationship between the activation of the unfolded protein response was established and the onset of hyperostosis that can be suppressed with a chemical chaperone, sodium 4-phenobutyrate (4-PBA)"* ([PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/)).
- **LRP4–sclerostin interface modulation:** competitive blocking studied for anabolism ([PMID: 35099616](https://pubmed.ncbi.nlm.nih.gov/35099616/)) — conceptually reversible for CDD.

**Personalized/genotype-guided care.** Distinguishing dominant *SOST* from recessive *SP7* CDD informs recurrence-risk counseling and prognosis but does not yet change pharmacologic management.

---

## 13. Prevention

- **Primary prevention:** Not possible — a genetic disorder, largely de novo. No modifiable risk factors.
- **Secondary prevention:** Early diagnosis (radiographic + molecular) and **surveillance** of vision, hearing, and ICP to time decompressive surgery before irreversible cranial-nerve damage — the principal opportunity for prevention of morbidity.
- **Tertiary prevention:** Surgical decompression and reduction osteoplasty to prevent blindness, deafness, and death from foraminal/brainstem compression; hearing rehabilitation.
- **Immunization / public-health / environmental interventions:** Not applicable.
- **Genetic counseling:** Central. For dominant *SOST* CDD, counsel on de novo occurrence and 50% transmission risk from an affected parent; for recessive *SP7* CDD, counsel on 25% recurrence and consanguinity. **Prenatal / preimplantation genetic testing** is feasible when the familial variant is known.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring companion-animal or wildlife equivalent of CDD is documented in OMIA. Disease knowledge derives from engineered laboratory models (Section 15).
- **Orthologous genes:** *Sost* (mouse, **NCBI Gene 74499**; *Mus musculus*, **NCBI:txid10090**); *Sp7*/Osterix (mouse). Both are conserved and functionally validated (below).
- **Comparative biology:** *Sost*-deficient mice recapitulate the high-bone-mass consequence of sclerostin loss, and *"Sost/SOST deficiency induces lifelong bone gain in mice and humans"* ([PMID: 23901037](https://pubmed.ncbi.nlm.nih.gov/23901037/)) — demonstrating strong evolutionary conservation of the sclerostin–Wnt bone-formation mechanism.
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Mammalian (mouse) models are the principal system.**

| Model | Type | Key phenotype | Relevance to CDD | Evidence |
|---|---|---|---|---|
| *Sost*−/− (global KO) | Knockout | High bone mass via increased bone formation; elevated femoral-neck BV/TV | Models the sclerostin-deficiency → high-bone-mass output | [PMID: 33339872](https://pubmed.ncbi.nlm.nih.gov/33339872/); [PMID: 31437568](https://pubmed.ncbi.nlm.nih.gov/31437568/) |
| *Sost*/*SOST* deficiency (mouse + human) | Genetic | Lifelong bone gain | Cross-species validation of mechanism | [PMID: 23901037](https://pubmed.ncbi.nlm.nih.gov/23901037/) |
| AAV8-Sp7-Cre postnatal *Sost* KO | Conditional/somatic | Increased bone anabolism in adults; decreased canalicular density | Confirms postnatal role of *Sost* in bone homeostasis | [PMID: 36462771](https://pubmed.ncbi.nlm.nih.gov/36462771/) |
| Osteocyte-UPR transgenic | Transgenic (gain of ER stress) | Generalized hyperostosis; SOST suppressed; Wnt activated; **rescued by 4-PBA** | Phenotype *"highly consistent with craniodiaphyseal dysplasia"* — closest CDD-specific model | [PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/) |

**Phenotype recapitulation.** *Sost*-loss models faithfully reproduce the **high-bone-mass / hyperostosis** endpoint central to CDD (*"Loss-of-function mutations in the Sost gene lead to high bone mass phenotypes"*, [PMID: 33339872](https://pubmed.ncbi.nlm.nih.gov/33339872/)), and the osteocyte-UPR transgenic reproduces **generalized hyperostosis explicitly likened to CDD** with a druggable rescue: *"As the phenotype is highly consistent with craniodiaphyseal dysplasia (CDD; OMIM 122860), we propose activation of the UPR could be part of the disease mechanism for CDD patients"* ([PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/)).

**Limitations.** No mouse carries the exact human *SOST* signal-peptide (p.Val21Met/Leu) dominant-negative allele; existing KOs model loss of function rather than the dominant-negative secretion defect. Murine models capture bone overgrowth but incompletely reproduce the human craniofacial "leontiasis ossea" and cranial-nerve compression syndrome. A caution flag from the literature: *Sost* haploinsufficiency combined with glucocorticoid excess produced lethal cardiac tamponade in mice ([PMID: 30664862](https://pubmed.ncbi.nlm.nih.gov/30664862/)), highlighting potential off-target cardiovascular effects of sclerostin-axis manipulation.

**Resources:** MGI (mouse *Sost*, *Sp7*); IMPC/KOMP for conditional alleles.

---

## Mechanistic Model / Interpretation

CDD is best understood as a **"loss-of-the-brake" bone disease**. Sclerostin is the physiologic osteocyte-derived antagonist that restrains Wnt-driven osteoblast bone formation by binding LRP4/5/6. In dominant CDD, a signal-peptide mutation blocks sclerostin from leaving the cell (a dominant-negative secretion defect), so the extracellular brake is lost, canonical Wnt/β-catenin signaling runs unchecked, and osteoblasts deposit bone relentlessly across the skull, face, and diaphyses. Because the skull is a closed compartment perforated by fixed foramina, the pathology's clinical severity comes not from any metabolic toxicity but from **mechanical geometry**: bone fills the foramina and cranial cavity, strangling cranial nerves II/VII/VIII and the brainstem. The osteocyte UPR provides a plausible intracellular amplifier that further suppresses *SOST* and can, on its own, generate a CDD-like phenotype in mice. A parallel recessive route through *SP7*/Osterix loss reaches an overlapping sclerotic phenotype by disrupting the osteoblast transcriptional program upstream/parallel to the sclerostin–Wnt node.

The therapeutic corollary is striking and well-supported: pharmaceutical companies deliberately **inhibit** sclerostin (romosozumab) to *build* bone in osteoporosis. CDD is essentially the endogenous, lifelong version of that intervention. This confirms the causal direction beyond doubt but also explains why no drug exists for CDD — the field has optimized tools to *lower* sclerostin, whereas CDD needs the opposite (restore Wnt inhibition), a direction with no approved agent and the added hazard, seen in mice, of cardiovascular effects from sclerostin-axis perturbation.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [21221996](https://pubmed.ncbi.nlm.nih.gov/21221996/) | *SOST signal-peptide mutations in AD CDD* | **Landmark** — identifies causal p.Val21Met/Leu; demonstrates reduced secretion; establishes dominant-negative mechanism |
| [8827383](https://pubmed.ncbi.nlm.nih.gov/8827383/) | *Reduction osteoplasty for CDD* | Core clinical phenotype, progression, cranial-nerve compression, surgical decompression |
| [28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/) | *Osteocyte UPR causes CDD-consistent hyperostosis* | UPR→SOST suppression→Wnt→hyperostosis; 4-PBA rescue; CDD-like mouse model |
| [19936252](https://pubmed.ncbi.nlm.nih.gov/19936252/) | *Lrp4, receptor for sclerostin* | Sclerostin binds LRP5/6 and inhibits Wnt — normal function whose loss drives CDD |
| [35099616](https://pubmed.ncbi.nlm.nih.gov/35099616/) | *Blocking LRP4–sclerostin interface* | Confirms LRP4/6–sclerostin mechanism; reversible-modulation concept |
| [36436818](https://pubmed.ncbi.nlm.nih.gov/36436818/) | *Recessive CDD from SP7/Osterix* | Establishes genetic heterogeneity (recessive form) |
| [37918503](https://pubmed.ncbi.nlm.nih.gov/37918503/) | *SP7-related bone disorder follow-up* | Biallelic *SP7* LOF variants; CDD-overlapping sclerotic dysplasia |
| [29264888](https://pubmed.ncbi.nlm.nih.gov/29264888/) | *Sclerostin mechanisms/disorders* | Groups CDD with sclerosteosis & van Buchem (SOST spectrum) |
| [1259284](https://pubmed.ncbi.nlm.nih.gov/1259284/) / [187366](https://pubmed.ncbi.nlm.nih.gov/187366/) | *Sclerosteosis clinical features* | Differential diagnosis: recessive, syndactyly, founder effect |
| [40639871](https://pubmed.ncbi.nlm.nih.gov/40639871/) | *CMD misdiagnosed as CDD* | Differential: craniometaphyseal dysplasia |
| [14564212](https://pubmed.ncbi.nlm.nih.gov/14564212/) | *Mild CDD case* | Milder/adult phenotype; excluded TGFB1/LRP5; radiographic features |
| [40605263](https://pubmed.ncbi.nlm.nih.gov/40605263/) | *SOST LOF, sclerosteosis-1* | Temporal-bone CT findings in SOST hyperostosis spectrum |
| [31132523](https://pubmed.ncbi.nlm.nih.gov/31132523/) | *BAHA in CDD* | Hearing rehabilitation option |
| [1987972](https://pubmed.ncbi.nlm.nih.gov/1987972/) | *Pregnancy in CDD* | Raised ICP, cranial-nerve palsies, seizures, long-bone modeling defects |
| [23901037](https://pubmed.ncbi.nlm.nih.gov/23901037/) | *Reversing SOST-deficiency disorders* | Cross-species: SOST deficiency → lifelong bone gain |
| [33339872](https://pubmed.ncbi.nlm.nih.gov/33339872/) / [31437568](https://pubmed.ncbi.nlm.nih.gov/31437568/) / [36462771](https://pubmed.ncbi.nlm.nih.gov/36462771/) | *Sost KO mouse models* | High-bone-mass phenotype validating the mechanism |
| [42761068](https://pubmed.ncbi.nlm.nih.gov/42761068/) / [42417976](https://pubmed.ncbi.nlm.nih.gov/42417976/) | *Romosozumab* | Anti-sclerostin antibody is bone-anabolic — validates CDD causal direction |
| [30664862](https://pubmed.ncbi.nlm.nih.gov/30664862/) | *Sost haploinsufficiency → cardiac tamponade* | Safety caution for sclerostin-axis manipulation |

**Evidence-source mix:** human clinical case reports/series (phenotype, surgery, genetics), in vitro secretion assay (293E cells), and model-organism (mouse) studies. No large human cohorts, omics datasets, or randomized trials exist for CDD itself.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Fewer than ~two dozen reported CDD cases; almost all knowledge is from case reports. Prevalence, incidence, penetrance, and QoL are estimated qualitatively, not measured.
2. **Genotype–phenotype spectrum incompletely defined.** Only two dominant *SOST* signal-peptide alleles and a few recessive *SP7* variants are described; the full mutational spectrum and modifiers are unknown.
3. **Dominant-negative mechanism partly inferred.** Reduced secretion is demonstrated in a cell line; how mutant sclerostin dominantly interferes with wild-type protein at the tissue level is not fully resolved. The UPR amplifier is a plausible but not yet human-confirmed contributor.
4. **No faithful animal model of the human allele.** Existing mice model loss-of-function or ER stress, not the specific dominant-negative signal-peptide defect, and do not fully reproduce craniofacial/cranial-nerve pathology.
5. **No disease-modifying therapy or trials.** Management is entirely symptomatic/surgical; the required "pro-sclerostin/Wnt-inhibition" direction has no approved drug and carries potential cardiovascular risk.
6. **No CDD-specific omics.** No transcriptomic, proteomic, metabolomic, or epigenomic patient datasets exist.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying the human *SOST* p.Val21Met (or p.Val21Leu) allele to model the dominant-negative secretion defect and test whether it reproduces craniofacial hyperostosis and cranial-nerve compression.
2. **Test sclerostin-restoring / Wnt-inhibiting strategies** preclinically — recombinant/engineered sclerostin mimetics, LRP6 antagonism, or DKK1 pathway modulation — to establish proof-of-concept for slowing bone deposition, monitoring for the cardiovascular signal flagged in [PMID: 30664862](https://pubmed.ncbi.nlm.nih.gov/30664862/).
3. **Evaluate chemical chaperones (4-PBA)** and broader UPR modulators in CDD-relevant models, building on [PMID: 28973168](https://pubmed.ncbi.nlm.nih.gov/28973168/), toward a repurposing rationale.
4. **Establish an international CDD registry / natural-history study** pooling *SOST* and *SP7* cases to quantify onset, progression rate, cranial-nerve outcomes, surgical timing/efficacy, and survival.
5. **Standardize molecular diagnosis** via a sclerosing bone dysplasia gene panel (including *SOST*, *SP7*, *ANKH*, *TGFB1*, *LRP5*) with functional secretion assays for novel *SOST* variants.
6. **Patient-derived iPSC osteocyte/organoid models** to study the dominant-negative secretion defect and UPR in a human genetic background and to screen candidate therapeutics.
7. **Prospective surveillance protocols** (serial vision, audiometry, ICP/imaging) to define optimal timing of decompressive surgery — the current best lever on morbidity and mortality.

---

*Report compiled from 12 confirmed findings across 33 reviewed papers over 5 investigation iterations. Evidence types: human clinical (case reports/series), in vitro (secretion assays), and model-organism (mouse). CDD remains an ultra-rare disorder where mechanistic understanding substantially outpaces therapeutic options.*


## Artifacts

- [OpenScientist final report](Craniodiaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Craniodiaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 12 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:187366` (5 mentions) - Sclerosteosis - an autosomal recessive disorder
  - shared terms: recessive

Weighed against this report's own most characteristic terms: `cdd`, `bone`, `sost`, `sp7`, `sclerostin`, `disease`, `recessive`, `hyperostosis`, `loss`, `mechanism`, `dysplasia`, `secretion`, `upr`, `phenotype`, `dominant`, `osteocyte`, `genetic`, `wnt`, `craniofacial`, `model`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0021021` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **craniodiaphyseal dysplasia, autosomal dominant**
- `HP:0011856` (1 mention) - the report calls it "facial bone hyperostosis"; HP calls it **Pica**
- `HP:0000256` (1 mention) - the report calls it "Physical sign"; HP calls it **Macrocephaly**
- `HP:0100692` (1 mention) - the report calls it "Sclerotic clavicle"; HP calls it **Increased corneal curvature**
- `HP:0002516` (1 mention) - the report calls it "Sign"; HP calls it **Increased intracranial pressure**
- `HP:0001250` (1 mention) - the report calls it "Sign"; HP calls it **Seizure**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0021021` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
