---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:11:21.183955'
end_time: '2026-10-01T20:29:39.582468'
duration_seconds: 1098.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Disabling Pansclerotic Morphea of Childhood
  mondo_id: MONDO:0957497
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Disabling_Pansclerotic_Morphea_Of_Childhood-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Disabling_Pansclerotic_Morphea_Of_Childhood-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Disabling Pansclerotic Morphea of Childhood
- **MONDO ID:** MONDO:0957497 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Disabling Pansclerotic Morphea of Childhood** covering all of the
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

# Disabling Pansclerotic Morphea of Childhood (DPM): A Comprehensive Disease Characteristics Report

**Disease:** Disabling Pansclerotic Morphea of Childhood (DPM / DPMC)
**MONDO ID:** MONDO:0957497 · **OMIM:** #620443 · **Causal gene:** *STAT4* (gain-of-function)
**Category:** Mendelian (autosomal dominant) autoinflammatory fibrosing disease

---

## Summary

Disabling Pansclerotic Morphea of Childhood (DPM) is an ultra-rare, childhood-onset fibrosing disorder historically regarded as the most severe end of the juvenile localized scleroderma (JLS)/morphea spectrum. Until recently it was considered an idiopathic/autoimmune condition of unknown cause. In 2023, a landmark study by Baghdassarian and colleagues (*New England Journal of Medicine*) reclassified DPM as a **Mendelian, autosomal dominant, autoinflammatory disease** caused by heterozygous **gain-of-function (GOF) missense variants in the DNA-binding domain (DBD) of *STAT4*** ([PMID: 37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/)). Three novel variants — p.His623Tyr, p.Ala635Val, and p.Ala650Asp — were identified across three unrelated families and shown to amplify JAK–STAT signaling downstream of interferon and IL-6.

Clinically, DPM is characterized by **rapidly progressive, circumferential, full-thickness sclerosis** that extends beyond the dermis into subcutaneous fat, fascia, muscle, and even bone, producing chronic non-healing skin ulcers, painful joint contractures, immobility, and a substantial risk of ulcer-related cutaneous squamous cell carcinoma (SCC). A distinguishing feature from systemic sclerosis is that **internal organ fibrosis is typically absent**. Mortality is high, driven by sepsis, gangrene, cardiopulmonary complications, and malignancy. A 2025 systematic review of 86 patients reported across a century (1923–2023) confirmed its rarity and poor prognosis, and notably found that the number of treatments administered did not influence outcome — underscoring the inadequacy of conventional immunosuppression ([PMID: 39520387](https://pubmed.ncbi.nlm.nih.gov/39520387/)).

The identification of the STAT4-GOF/JAK–STAT mechanism transformed the therapeutic landscape. Whereas methotrexate, corticosteroids, and mycophenolate mofetil are frequently inadequate, the **JAK inhibitor ruxolitinib** reversed the hyperinflammatory fibroblast phenotype in vitro and produced resolution of inflammatory markers and clinical symptoms in treated patients without adverse effects. A 2025 independent Chinese case report replicated both the recurrent p.His623Tyr variant and the favorable ruxolitinib response, strengthening the genotype-guided treatment paradigm. DPM thus serves as a paradigm for how a rare "autoimmune"-appearing fibrosing disease can be a single-gene autoinflammatory disorder amenable to precision targeted therapy.

---

## 1. Disease Information

**Overview.** DPM is a rare, aggressive, childhood-onset fibrosing dermatosis. It sits at the severe extreme of the juvenile localized scleroderma (morphea) spectrum but is now understood to be genetically distinct in at least a subset of cases, caused by germline STAT4 GOF variants. The hallmark is deep, circumferential ("pansclerotic") sclerosis of the skin and underlying soft tissue, with ulceration, contractures, and progressive disability.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #620443 (DISABLING PANSCLEROTIC MORPHEA OF CHILDHOOD; DPMC) |
| MONDO | MONDO:0957497 |
| Causal gene | *STAT4* — OMIM *600558; NCBI Gene 6775; HGNC:11365; UniProt Q14765 |
| Disease class | Juvenile localized scleroderma, pansclerotic subtype (Padua/PReS classification) |

**Synonyms / alternative names:** Disabling pansclerotic morphea of childhood (DPMC); pansclerotic morphea; disabling pansclerotic morphea; (within JLS) pansclerotic/deep morphea subtype.

**Nature of information.** Evidence is derived primarily from **individual patient reports and small case series** aggregated into disease-level reviews, plus functional studies on patient-derived cells. The 2023 genetic discovery studied 4 patients from 3 families; the 2025 systematic review aggregated 86 patients from 52 reports.

---

## 2. Etiology

**Primary cause (genetic).** Heterozygous **gain-of-function missense variants in *STAT4*** (DNA-binding domain) cause autosomal dominant DPM ([PMID: 37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/)). *"Genome sequencing revealed three novel heterozygous missense gain-of-function variants in STAT4."* This is a **monogenic autoinflammatory etiology**, reclassifying the historically idiopathic/autoimmune disease.

**Genetic risk factors.** The causal variants are the GOF STAT4 DBD substitutions (p.His623Tyr, p.Ala635Val, p.Ala650Asp). No additional modifier loci have been formally mapped. Because variants are highly penetrant and dominant, carrying a single pathogenic allele is the principal risk determinant.

**Environmental risk factors.** In the broader JLS population, an environmental trigger (trauma, infection) is reported in ~13% of cases, and female sex predominates; however, for genetically-defined STAT4-DPM, the disease is driven by the germline variant. Within JLS generally, ANA positivity (42.3%) suggests an autoimmune diathesis, but this is not specific to DPM.

**Protective factors.** None established genetically or environmentally. (Not applicable / not reported.)

**Gene–environment interactions.** Not characterized for DPM. It is biologically plausible that interferon-inducing stimuli (viral infection) could exacerbate STAT4-GOF signaling, but this is inferred, not demonstrated.

---

## 3. Phenotypes

DPM phenotypes span cutaneous, musculoskeletal, hematologic/immunologic, and oncologic domains. Onset is in childhood (typically <14 years); course is **progressive**; severity is **severe**.

| Phenotype | Type | HPO suggestion | Characteristics / frequency |
|---|---|---|---|
| Circumferential cutaneous sclerosis (to fascia/muscle/bone) | Physical manifestation | HP:0100324 (Skin sclerosis) | Hallmark; rapidly progressive; near-universal |
| Chronic skin ulcers | Clinical sign | HP:0100512 (Skin ulcer) | Common; prone to infection and SCC |
| Joint contractures | Clinical sign | HP:0001371 (Flexion contracture) | Common; cause immobility |
| Immobility / loss of ambulation | Functional | HP:0002540 (Inability to walk) | Progressive disability |
| Cutaneous squamous cell carcinoma (ulcer-related) | Neoplasm | HP:0002860 (Squamous cell carcinoma) | Recognized complication; can metastasize |
| Neutropenia | Lab abnormality | HP:0001875 | Mild; in STAT4-DPM |
| Lymphopenia (CD4+ T cells) | Lab abnormality | HP:0001888 / HP:0005415 | T-cell exhaustion, Th1 skew |
| Hypogammaglobulinemia (low IgG/IgA) | Lab abnormality | HP:0004313 / HP:0002720 | Reduced IgG and IgA |
| Elevated inflammatory markers (ESR/CRP) | Lab abnormality | HP:0011227 (Elevated CRP) | Common |
| Peripheral eosinophilia | Lab abnormality | HP:0001880 | In some patients |

**Distinguishing phenotype:** *"Internal organ fibrosis is typically absent"* ([PMID: 39520387](https://pubmed.ncbi.nlm.nih.gov/39520387/)) — a key separator from systemic sclerosis.

**Quality of life.** Profound: circumferential sclerosis, contractures, chronic ulcers, and pain cause severe impairment of mobility, self-care, and daily functioning, with lifelong disability and psychosocial burden. No disease-specific EQ-5D/SF-36 data are published; impact is inferred from the severe clinical course.

---

## 4. Genetic / Molecular Information

**Causal gene.** *STAT4* (Signal Transducer And Activator Of Transcription 4), OMIM *600558, located on chromosome 2q32.2–32.3.

**Pathogenic variants** (all heterozygous, germline, autosomal dominant; DNA-binding domain; transcript NM_003151.4):

| Variant (cDNA) | Protein | Domain | Classification | Type | Consequence |
|---|---|---|---|---|---|
| c.1867C>T | p.His623Tyr (H623Y) | DBD | Pathogenic (GOF) | Missense | Gain of function |
| c.1904C>T | p.Ala635Val (A635V) | DBD | Pathogenic (GOF) | Missense | Gain of function |
| c.1949C>A | p.Ala650Asp (A650D) | DBD | Pathogenic (GOF) | Missense | Gain of function |

These are **novel, private variants**, absent from population databases (gnomAD) — consistent with a severe, largely de novo dominant disorder. **Functional consequence: gain of function** — after interferon-α stimulation, variant-carrying cells showed increased/prolonged phospho-STAT4 relative to wild-type STAT4, and STAT4 is essential for transcriptional activation downstream of IL-6 receptor signaling ([PMID: 37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/)).

**Somatic vs germline:** Germline (constitutional); recurrent de novo events documented (p.His623Tyr seen in independent unrelated patients).

**Modifier genes / epigenetics / chromosomal abnormalities:** None established (not reported / not applicable).

---

## 5. Environmental Information

For genetically-defined STAT4-DPM, **the disease is fundamentally genetic** and no specific environmental toxin, pollutant, or occupational exposure is required or established. Within the broader morphea spectrum, trauma and infection are occasionally reported triggers (~13% of JLS), and interferon-inducing stimuli could theoretically amplify STAT4 signaling (inferred). **No infectious agent causes DPM.** Lifestyle factors are not implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous germline STAT4 DNA-binding-domain missense variant** (p.His623Tyr / p.Ala635Val / p.Ala650Asp) is present constitutionally → **leads to** an altered STAT4 transcription factor with increased activity.
2. Upon cytokine stimulation (interferon-α; IL-12; IL-6-receptor signaling), the variant STAT4 **results in** increased and prolonged phosphorylation (hyperactive phospho-STAT4) relative to wild-type → i.e., **gain of function**.
3. Hyperactive STAT4 **leads to** amplified JAK–STAT transcriptional output and Th1-skewed, interferon-signature immune activation (demonstrated by single-cell RNA-seq immunodysregulatory signature).
4. This **results in** systemic immune dysregulation: mild neutropenia, CD4+ lymphopenia, T-cell exhaustion, and reduced IgG/IgA (hypogammaglobulinemia), with elevated inflammatory markers.
5. In parallel (branch), dermal **fibroblasts hypersecrete IL-6** and other inflammatory mediators → **leads to** a hyperinflammatory, profibrotic fibroblast state.
6. Dysfunctional fibroblasts show **impaired wound healing, impaired collagen-matrix contraction, and altered matrix secretion** → **results in** aberrant extracellular matrix deposition (fibrosis) plus poor re-epithelialization (chronic ulcers).
7. Deep, circumferential fibrosis **leads to** sclerosis extending to fascia, muscle, and bone, with contractures and immobility; chronic ulceration **leads to** infection risk and, over time, ulcer-related cutaneous SCC.
8. End results **→** disability, sepsis/gangrene, cardiopulmonary complications, malignancy, and high mortality.
9. **Therapeutic interruption:** JAK inhibition (ruxolitinib) blocks steps 2–3 (signal amplification) → reverses the hyperinflammatory fibroblast phenotype in vitro and resolves inflammatory markers and clinical symptoms in patients.

### Supporting detail

- **Molecular pathways:** JAK–STAT signaling (type I/II interferon and IL-6/IL-12 axes); STAT4 is the key transducer. Upstream Janus kinases (JAK1/JAK2/TYK2) activate STAT4; downstream, excessive interferon-response and IL-6 transcriptional programs drive inflammation and fibrosis.
- **Cellular processes:** Chronic inflammation, Th1 polarization, T-cell exhaustion, impaired wound healing, and profibrotic fibroblast activation.
- **Protein dysfunction:** STAT4 DBD substitutions produce a **gain-of-function** transcription factor (increased/prolonged phosphorylation and transcriptional activity), not loss of function or aggregation.
- **Immune involvement:** Autoinflammatory (innate/adaptive dysregulation) rather than classic autoantibody-mediated autoimmunity; cytopenias and hypogammaglobulinemia indicate combined immune dysregulation.
- **Tissue damage mechanism:** Fibrosis (excess/aberrant collagen matrix) plus chronic ulceration; ischemia and infection compound tissue injury.
- **Molecular profiling:** Single-cell RNA-seq of patient PBMCs revealed an immunodysregulatory expression signature *"consistent with an immunodysregulatory phenotype that were appropriately modified through JAK inhibition."* Fibroblast assays quantified IL-6 hypersecretion and matrix dysfunction.

**Suggested ontology terms:** GO:0007259 (receptor signaling pathway via JAK–STAT); GO:0006954 (inflammatory response); GO:0042060 (wound healing); GO:0030198 (extracellular matrix organization). Cell types: CL:0000057 (fibroblast), CL:0000084 (T cell), CL:0000545 (Th1 cell), CL:0000775 (neutrophil). CHEBI: ruxolitinib (CHEBI:66919).

---

## 7. Anatomical Structures Affected

- **Organ/system level — primary:** Skin (UBERON:0002097) and skin of trunk/limbs; subcutaneous tissue; **musculoskeletal system** — fascia (UBERON:0007844), skeletal muscle (UBERON:0001134), joints (UBERON:0000982), and bone (UBERON:0001474).
- **Secondary involvement:** Immune/hematologic system (cytopenias, hypogammaglobulinemia); potential cardiopulmonary complications contributing to mortality. **Internal visceral organ fibrosis is characteristically absent** (contrast with systemic sclerosis).
- **Tissue types:** Connective tissue (dermal/subcutaneous collagen, fascia) is the principal target; epithelial (epidermal ulceration) and muscle tissue secondarily involved.
- **Cell populations (CL):** Dermal fibroblasts (CL:0000057); T lymphocytes incl. CD4+/Th1 (CL:0000084, CL:0000545); neutrophils (CL:0000775); keratinocytes at ulcer margins (CL:0000312).
- **Subcellular (GO Cellular Component):** Nucleus (GO:0005634; STAT4 acts as a nuclear transcription factor); cytoplasm (GO:0005737; latent STAT4 prior to activation).
- **Localization / lateralization:** Typically **bilateral and circumferential** involvement of trunk and extremities; symmetric progression is common, though individual lesions may be asymmetric.

---

## 8. Temporal Development

- **Onset:** Childhood, predominantly **<14 years of age** (juvenile-onset). Onset pattern is subacute-to-chronic with **rapid progression** of sclerosis.
- **Progression:** Relentlessly **progressive**; sclerosis rapidly becomes circumferential and deep (fascia/muscle/bone). Contractures and ulcers accumulate over time.
- **Disease course:** Chronic, lifelong, progressive; without effective mechanism-targeted therapy, outcomes are poor and mortality is high. The 2025 review found **female patients were younger at reported death**, and the **number of treatments did not influence outcome** under conventional management.
- **Remission:** Spontaneous remission is not characteristic. **Treatment-induced improvement** has now been demonstrated with ruxolitinib (resolution of inflammatory markers and symptoms).
- **Critical period:** Early intervention — ideally before irreversible deep fibrosis, contractures, and ulceration — represents the key window; genotype-guided JAK inhibition offers an opportunity to alter natural history.

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare. Only **~86 DPM patients** have been reported in the literature (1923–2023; 52 reports). A Japanese nationwide survey estimated juvenile-onset morphea incidence at **2.11–2.87 per 1,000,000 children/year** (mean onset 7.7 yr); pansclerotic morphea is among the rarest, most severe subtypes requiring systemic immunosuppression. In the 750-patient international JLS cohort, deep morphea comprised only ~2% (linear 65%, plaque 26%, generalized 7%).
- **Inheritance:** **Autosomal dominant** (STAT4 GOF). Recurrent **de novo** variants documented (p.His623Tyr in unrelated patients).
- **Penetrance / expressivity:** High penetrance in reported families; expressivity appears severe. Formal penetrance estimates are limited by the small number of cases.
- **Genetic anticipation / mosaicism / founder effects:** Not established / not reported.
- **Consanguinity:** Not a factor (dominant mechanism).
- **Carrier frequency:** Variants are private and essentially absent from gnomAD; no meaningful population carrier frequency.
- **Demographics:** Affects children of both sexes; broader morphea shows female predominance. No specific ethnic predilection for STAT4-DPM (reported in multiple populations, including North American and Chinese patients). Sex ratio for STAT4-DPM is not firmly established given small numbers.

---

## 10. Diagnostics

**Clinical diagnosis** rests on the characteristic phenotype: rapidly progressive, circumferential, full-thickness sclerosis of trunk/limbs with ulceration and contractures.

**Histopathology (skin biopsy):** Deep dermal and subcutaneous hyalinized/sclerotic collagen, loss of adnexal structures, and thickened fascia/muscle involvement (deep morphea pattern).

**Supportive laboratory findings:** Cytopenias (neutropenia, CD4+ lymphopenia), hypogammaglobulinemia (low IgG/IgA), elevated ESR/CRP, and peripheral eosinophilia in some. **ANA** is frequently positive in localized scleroderma (42.3% in JLS) but **Scl-70 and anticentromere antibodies are usually negative** (helping exclude systemic sclerosis).

**Imaging:** MRI and ultrasound assess depth of fascial/muscle involvement and disease activity.

**Genetic testing (confirmatory):** Sequencing of *STAT4* (targeted single-gene, gene panel, exome, or genome) to identify heterozygous DNA-binding-domain GOF variants. Exome/genome sequencing was the discovery modality and is recommended for undiagnosed severe pansclerotic morphea.

**Differential diagnosis:**

| Condition | Distinguishing feature from DPM |
|---|---|
| Systemic sclerosis | Internal-organ involvement, Raynaud, Scl-70+ (all absent in DPM) |
| Eosinophilic fasciitis | Can overlap/continuum; peripheral eosinophilia, fascial inflammation |
| Chronic graft-versus-host disease | History of transplant |
| Nephrogenic systemic fibrosis | Gadolinium exposure, renal failure |
| Scleromyxedema | Mucin deposition, paraproteinemia |
| Stiff skin syndrome | Congenital, non-inflammatory, *FBN1*-related |
| Other monogenic interferonopathies | Distinct genetic/clinical profiles |

**Screening:** Cascade genetic testing of at-risk relatives once a familial STAT4 variant is identified; no population newborn screening exists.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** High mortality historically. Causes of death include **sepsis, gangrene, and cardiopulmonary involvement**; ulcer-related **metastatic SCC** also contributes. Female patients were younger at reported death.
- **Morbidity/disability:** Severe — progressive contractures, immobility, chronic ulceration, and pain lead to lifelong functional impairment.
- **Complications:** Chronic non-healing ulcers; secondary infection; cutaneous squamous cell carcinoma (can metastasize); joint contractures; cardiopulmonary involvement.
- **Recovery potential:** Deep fibrosis and contractures are largely irreversible; prevention of progression is the goal. Mechanism-targeted therapy (ruxolitinib) can halt inflammatory activity and improve symptoms.
- **Prognostic factors:** Depth/extent of sclerosis, presence of ulcers/SCC, and — critically — access to effective JAK-targeted therapy. Under conventional immunosuppression, **number of treatments did not influence outcome**, indicating a strong need for mechanism-based therapy.

---

## 12. Treatment

**Conventional immunosuppression (often inadequate).** For high-risk JLS including pansclerotic morphea, SHARE/EULAR consensus and juvenile scleroderma reviews recommend systemic therapy when disability is threatened:

| Drug | Class | NCIT | Role |
|---|---|---|---|
| Methotrexate | Antimetabolite/DMARD | NCIT:C642 | Cornerstone first-line |
| Systemic corticosteroids | Glucocorticoid | NCIT:C2271 | Adjunct, induction |
| Mycophenolate mofetil | Immunosuppressant | NCIT:C2010 | Severe/refractory |

Despite these, the 86-patient review found **the number of treatments did not influence outcome**, underscoring poor efficacy of conventional immunosuppression in DPM.

**Mechanism-targeted therapy — JAK inhibition.** The 2023 STAT4-GOF discovery provided a rational target. **Ruxolitinib** (JAK1/2 inhibitor; NCIT:C82733) *"led to improvement in the hyperinflammatory fibroblast phenotype in vitro and resolution of inflammatory markers and clinical symptoms in treated patients, without adverse effects"* ([PMID: 37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/)). A 2025 independent case (6-year-old girl, de novo p.His623Tyr) achieved marked remission on corticosteroids plus ruxolitinib (5.0 mg AM + 2.5 mg PM) ([PMID: 40518164](https://pubmed.ncbi.nlm.nih.gov/40518164/)).

**Supportive and rehabilitative care.** Aggressive wound care (ulcer prevention/healing), physiotherapy/occupational therapy to limit contractures, infection prophylaxis, pain management, and **SCC surveillance** of chronic ulcers.

**Personalized medicine:** Genotype-guided JAK–STAT blockade is the emerging standard once a STAT4 GOF variant is confirmed.

---

## 13. Prevention

- **Primary prevention:** Not possible for a de novo/dominant germline disease. Genetic counseling for affected families regarding recurrence risk (50% transmission from an affected parent; de novo risk otherwise).
- **Secondary prevention:** Early genetic diagnosis and prompt initiation of JAK-targeted therapy to prevent progression of fibrosis and contractures.
- **Tertiary prevention:** Prevent complications — vigilant ulcer/wound care, infection prophylaxis, contracture-limiting rehabilitation, and **surveillance/biopsy of chronic ulcers for SCC**.
- **Counseling:** Genetic counseling and cascade testing for at-risk relatives; prenatal/preimplantation testing is theoretically possible for a known familial variant.
- Immunization, public-health, and environmental interventions are not applicable to disease causation.

---

## 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *STAT4* is evolutionarily conserved. Human *STAT4* (NCBI Gene 6775; HGNC:11365; UniProt Q14765); mouse *Stat4* (NCBI Gene 20849); rat *Stat4* (NCBI Gene 362925).
- **Natural disease in animals:** **No naturally occurring DPM-equivalent disease is catalogued in OMIA** for companion animals or wildlife.
- **Comparative biology:** *Stat4*-knockout mice model **loss of function** (defective IL-12 signaling and impaired Th1 differentiation) and therefore do **not** represent this gain-of-function human disease.
- **Zoonotic/transmission:** Not applicable (non-infectious, genetic disease).

---

## 15. Model Organisms

- **No dedicated animal model** specifically recapitulating STAT4-GOF DPM has been reported.
- **Functional systems used:** (1) **Patient-derived primary dermal fibroblasts** demonstrating IL-6 hypersecretion, impaired wound healing, and impaired collagen-matrix contraction; (2) **cell lines reconstituted with wild-type vs variant STAT4** to measure phospho-STAT4 and transcriptional activity; (3) **single-cell RNA-seq of patient PBMCs** showing an immunodysregulatory signature normalized by JAK inhibition ([PMID: 37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/)). *"Primary skin fibroblast and cell-line assays were used to define the functional nature of the genetic defect."*
- **Limitations:** Existing *Stat4*-knockout mice model the opposite (loss of function), so a **knock-in GOF mouse (e.g., Stat4 H623Y equivalent)** is needed to capture systemic and cutaneous disease in vivo.
- **Applications:** Current cellular models support mechanistic dissection of JAK–STAT amplification, fibroblast dysfunction, and drug response (JAK-inhibitor screening).

---

## Mechanistic Model / Interpretation

```
 STAT4 DBD GOF variant (germline, heterozygous)
   p.His623Tyr / p.Ala635Val / p.Ala650Asp
                 │
                 ▼
 Cytokine stimulation (IFN-α, IL-12, IL-6R signaling)
                 │
                 ▼
 Increased & prolonged phospho-STAT4  ── GAIN OF FUNCTION
                 │
        ┌────────┴─────────────┐
        ▼                      ▼
 Immune dysregulation    Fibroblast dysfunction
 - Th1 skew, IFN sig.    - IL-6 hypersecretion
 - CD4+ lymphopenia      - impaired wound healing
 - neutropenia           - impaired matrix contraction
 - low IgG/IgA           - aberrant matrix secretion
        │                      │
        └────────┬─────────────┘
                 ▼
 Deep circumferential fibrosis + chronic ulcers
 (skin → fascia → muscle → bone)
                 │
                 ▼
 Contractures, immobility, infection, SCC → high mortality

 ┌──────────────────────────────────────────────┐
 │  RUXOLITINIB (JAK inhibitor) blocks signal     │
 │  amplification → reverses fibroblast phenotype │
 │  & resolves inflammation/symptoms              │
 └──────────────────────────────────────────────┘
```

DPM is best understood as a **single-gene autoinflammatory fibrosing disease**: an upstream STAT4 DNA-binding-domain gain-of-function lesion amplifies JAK–STAT signaling, which branches into systemic immune dysregulation and a cell-autonomous profibrotic, poorly-healing fibroblast state. The convergence of these branches produces the signature deep, circumferential sclerosis with ulceration. The upstream genetic/signaling node is pharmacologically "druggable" at the JAK level, which is why ruxolitinib — acting high in the causal chain — reverses downstream pathology where conventional broad immunosuppression (acting diffusely and non-specifically) fails.

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [37256972](https://pubmed.ncbi.nlm.nih.gov/37256972/) | Baghdassarian et al., *NEJM* 2023 | **Landmark:** identified 3 STAT4 DBD GOF variants in 3 families; defined fibroblast dysfunction & immunodysregulation; demonstrated ruxolitinib efficacy |
| [39520387](https://pubmed.ncbi.nlm.nih.gov/39520387/) | Hua et al., *Br J Dermatol* 2025 | Systematic review of 86 patients (1923–2023); clinical phenotype, absence of internal-organ fibrosis, mortality, treatment-outcome analysis |
| [40518164](https://pubmed.ncbi.nlm.nih.gov/40518164/) | Shi et al., *Zhonghua Er Ke Za Zhi* 2025 | Independent replication: de novo STAT4 p.His623Tyr with scleroderma, ruxolitinib response |
| [16368732](https://pubmed.ncbi.nlm.nih.gov/16368732/) | Zulian et al., *Rheumatology* 2006 | 750-patient JLS cohort: subtype distribution, ANA 42.3%, environmental triggers |
| [40040588](https://pubmed.ncbi.nlm.nih.gov/40040588/) | Japanese nationwide survey 2025 | Juvenile morphea incidence (2.11–2.87 per 1,000,000/yr) |
| [28543434](https://pubmed.ncbi.nlm.nih.gov/28543434/) | SCC in DPMC | Ulcer-related SCC complication |
| [29455178](https://pubmed.ncbi.nlm.nih.gov/29455178/) | DPM mortality | Sepsis, gangrene, cardiopulmonary causes |
| [24383741](https://pubmed.ncbi.nlm.nih.gov/24383741/) | DPM + eosinophilic fasciitis | Overlapping differential diagnosis |

**Key verbatim support:**
- *"Genome sequencing revealed three novel heterozygous missense gain-of-function variants in STAT4. In vitro, primary skin fibroblasts showed enhanced interleukin-6 secretion, with impaired wound healing, contraction of the collagen matrix, and matrix secretion."* (PMID 37256972)
- *"Inhibition of Janus kinase (JAK)–STAT signaling with ruxolitinib led to improvement in the hyperinflammatory fibroblast phenotype in vitro and resolution of inflammatory markers and clinical symptoms in treated patients, without adverse effects."* (PMID 37256972)
- *"Single-cell RNA sequencing revealed expression patterns consistent with an immunodysregulatory phenotype that were appropriately modified through JAK inhibition."* (PMID 37256972)
- *"DPM is characterized by rapid sclerosis with circumferential involvement that frequently extends to the fascia, muscle and bone."* and *"Internal organ fibrosis is typically absent."* (PMID 39520387)
- *"Disabling pansclerotic morphea of childhood (DPMC) is a rare disorder that confers a risk of developing ulcer-related squamous cell carcinoma (SCC)."* (PMID 28543434)

---

## Limitations and Knowledge Gaps

1. **Small sample size.** Genetic evidence derives from only 4 patients in 3 families plus 1 replication case; penetrance, expressivity, and genotype–phenotype correlations remain imprecise.
2. **Genetic heterogeneity unresolved.** Not all historically-diagnosed DPM cases have been genotyped; some of the 86 reviewed patients may have non-STAT4 etiologies. The fraction of clinically-defined DPM that is STAT4-GOF is unknown.
3. **No in vivo model.** Absence of a GOF knock-in animal model limits study of systemic disease, long-term progression, and preclinical therapeutics.
4. **Durability and long-term safety of ruxolitinib** in children with DPM are not established in controlled trials; evidence is anecdotal/short-term.
5. **No disease-specific QoL, prevalence, or survival statistics** have been formally quantified; prognosis estimates are qualitative.
6. **Modifier genes, epigenetics, and gene–environment interactions** are entirely uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype legacy cohorts.** Sequence *STAT4* (and broader interferonopathy/fibrosis panels) in archived DPM cases to estimate the STAT4-GOF fraction and detect additional causal genes.
2. **Generate a Stat4-GOF knock-in mouse** (e.g., H623Y-equivalent) to recapitulate cutaneous/systemic disease and test JAK inhibitors in vivo.
3. **Prospective registry + clinical trial of ruxolitinib** (and other JAK inhibitors/upstream biologics such as anti-IL-6) in genetically-confirmed patients, with standardized skin-score, imaging, and QoL endpoints.
4. **Deep immunophenotyping and longitudinal single-cell/spatial transcriptomics** of skin and blood on and off therapy to define biomarkers of activity and response.
5. **Structural/biochemical characterization** of DBD variants to explain how they increase STAT4 DNA binding/transcriptional output and to guide variant-specific therapeutics.
6. **Establish SCC-surveillance and wound-care guidelines** specific to DPM given the malignancy risk.

---

### Consensus Answer

Disabling Pansclerotic Morphea of Childhood (OMIM #620443; MONDO:0957497) is an ultra-rare, childhood-onset, autosomal dominant autoinflammatory fibrosing disease caused by heterozygous gain-of-function missense variants in the DNA-binding domain of *STAT4* (p.His623Tyr, p.Ala635Val, p.Ala650Asp) that amplify JAK–STAT/IL-6/interferon signaling, producing hyperinflammatory, poorly-healing dermal fibroblasts, systemic immune dysregulation, and rapidly progressive circumferential sclerosis extending to fascia, muscle, and bone with ulcers, contractures, SCC risk, and high mortality while sparing internal organs. Conventional immunosuppression (methotrexate/corticosteroids/MMF) is largely ineffective, whereas the JAK inhibitor ruxolitinib reverses the cellular phenotype and improves patients, making genotype-guided JAK–STAT blockade the key mechanism-targeted therapy.


## Artifacts

- [OpenScientist final report](Disabling_Pansclerotic_Morphea_Of_Childhood-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Disabling_Pansclerotic_Morphea_Of_Childhood-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957497` (4 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **disabling pansclerotic morphea of childhood**
- `HP:0100324` (1 mention) - the report calls it "Skin sclerosis"; HP calls it **Scleroderma**
- `HP:0100512` (1 mention) - the report calls it "Skin ulcer"; HP calls it **Decreased circulating vitamin D concentration**
- `HP:0001875` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0001880` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased total eosinophil count**
- `UBERON:0002097` (1 mention) - the report calls it "Organ/system level — primary:** Skin"; UBERON calls it **skin of body**
- `NCIT:C2271` (1 mention) - the report calls it "Glucocorticoid"; NCIT calls it **Insulin**
- `NCIT:C2010` (1 mention) - the report calls it "Immunosuppressant"; NCIT calls it **Monoclonal Antibody MDX-22**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names
- `GO:0007259` (1 mention) - the report calls it "receptor signaling pathway via JAK–STAT"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "receptor signaling pathway via JAK-STAT" among its other names
- `CL:0000545` (2 mentions) - the report calls it "Th1 cell"; CL calls it **T-helper 1 cell**, and lists "Th1 cell" among its other names
- `NCIT:C642` (1 mention) - the report calls it "Antimetabolite/DMARD"; NCIT calls it **Methotrexate**, and lists "Amethopterin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0957497` - called "if available", "MONDO"
