---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T14:40:20.213578'
end_time: '2026-09-03T14:55:10.956203'
duration_seconds: 890.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RHYNS syndrome (retinitis pigmentosa, hypopituitarism, nephronophthisis,
    skeletal dysplasia)
  mondo_id: MONDO:0011202
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
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RHYNS_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RHYNS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RHYNS syndrome (retinitis pigmentosa, hypopituitarism, nephronophthisis, skeletal dysplasia)
- **MONDO ID:** MONDO:0011202 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RHYNS syndrome (retinitis pigmentosa, hypopituitarism, nephronophthisis, skeletal dysplasia)** covering all of the
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

# RHYNS Syndrome (Retinitis Pigmentosa, Hypopituitarism, Nephronophthisis, Skeletal Dysplasia): A Comprehensive Disease Characterization

**Disease:** RHYNS syndrome | **MONDO:** MONDO:0011202 | **OMIM:** 602152 | **Category:** Mendelian (autosomal recessive ciliopathy)
**Causal gene:** *TMEM67* (meckelin), chromosome 8q22.1

---

## Summary

**RHYNS syndrome is an ultra-rare, autosomal recessive multisystem ciliopathy caused by biallelic loss-of-function variants in *TMEM67*** (encoding the ciliary transition-zone protein meckelin, chromosome 8q22.1). It is clinically defined by a cardinal tetrad — **R**etinitis pigmentosa, **HY**popituitarism, **N**ephronophthisis, and **S**keletal dysplasia — from which the acronym derives. The disease was first described in 1997 in a single 17-year-old male ([PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)) and its molecular basis was resolved only in 2018, when whole-exome sequencing of the originally described family identified compound heterozygous *TMEM67* variants ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)). RHYNS sits at the mild, viable end of the exceptionally broad *TMEM67* allelic spectrum, which also encompasses lethal Meckel-Gruber syndrome (MKS3), Joubert syndrome 6 (JBTS6), COACH syndrome, and isolated nephronophthisis (NPHP11).

**Mechanistically, RHYNS is a transition-zone ciliopathy.** Defective meckelin disrupts the ciliary transition-zone gating apparatus and impairs Wnt5a–ROR2 non-canonical Wnt signalling, with downstream deregulation of Sonic hedgehog (Shh) and canonical Wnt/β-catenin signalling. This single molecular lesion branches into two broad pathological programs: (1) a **developmental patterning defect** producing skeletal dysplasia, craniofacial anomalies, sensory (conductive hearing loss) deficits, and (inferred) hypothalamic-pituitary maldevelopment; and (2) an **epithelial-maintenance defect** producing progressive fibrocystic tubulointerstitial kidney disease (nephronophthisis) and photoreceptor connecting-cilium degeneration (retinitis pigmentosa).

**No disease-modifying therapy exists.** Management is entirely supportive and organ-directed: dialysis and kidney transplantation for end-stage renal disease (curative for the renal component, as nephronophthisis does not recur in the allograft), hormone replacement for hypopituitarism (growth hormone, thyroid hormone), and low-vision support with ophthalmologic surveillance for retinitis pigmentosa. Molecular diagnosis by whole-exome sequencing or ciliopathy gene panels enables genetic counseling, prenatal diagnosis, and preimplantation genetic diagnosis. Because RHYNS is defined by only a handful of reported patients, much of its mechanistic detail is extrapolated from the far larger *TMEM67* and Joubert/Meckel literature and from animal models.

---

## 1. Disease Information

RHYNS syndrome is a Mendelian, autosomal recessive ciliopathy characterized by the tetrad of **R**etinitis pigmentosa, **HY**popituitarism, **N**ephronophthisis, and **S**keletal dysplasia. The disease was proposed as "a new syndrome" by Di Rocco and colleagues in 1997 based on a single 17-year-old boy presenting with nephronophthisis, retinitis pigmentosa, left upper-eyelid ptosis, enophthalmos, transmissive (conductive) deafness, growth-hormone (GH) and thyroid-stimulating-hormone (TSH) deficiency, and mild skeletal dysplasia ([PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)).

> "We report on a 17 6/12-year-old boy with nephronophthisis, retinitis pigmentosa, left upper eyelid ptosis, enopthalmos, transmissive deafness, GH and TSH deficiency, and mild skeletal dysplasia." — [PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| OMIM | 602152 (RHYNS SYNDROME) |
| MONDO | MONDO:0011202 |
| Orphanet | Ultra-rare; grouped with syndromic retinitis pigmentosa / ciliopathies |
| Causal gene | *TMEM67* (OMIM 609884), 8q22.1 |
| MeSH | No dedicated descriptor; indexed under ciliopathies / retinitis pigmentosa |

**Synonyms / alternative names:** Retinitis pigmentosa–hypopituitarism–nephronophthisis–skeletal dysplasia syndrome; RHYNS. Given its molecular basis, RHYNS is best understood as a **TMEM67-opathy** at the mild end of the ciliopathy continuum.

**Information source:** This report is derived from **aggregated disease-level resources** (OMIM, primary case reports, and the broader *TMEM67*/Joubert/Meckel literature), not individual EHR data. The RHYNS phenotype itself is defined by only a small number of published patients.

---

## 2. Etiology

**Disease causal factors — genetic.** RHYNS is caused by **biallelic (recessive) variants in the ciliary gene *TMEM67***. Whole-exome sequencing of the originally described RHYNS family identified compound heterozygous *TMEM67* variants: a paternally inherited nonsense variant **c.622A>T, p.(Arg208\*)** and a maternally inherited missense variant **c.1289A>G, p.(Asp430Gly)**, the latter perturbing correct splicing of exon 13 ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)). This confirmed the 1997 clinical hypothesis of autosomal recessive inheritance ([PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)).

> "Here we applied whole-exome sequencing in the originally described family with RHYNS to identify compound heterozygous variants in the ciliary gene TMEM67. Sanger sequencing confirmed a paternally inherited nonsense c.622A > T, p.(Arg208\*) and a maternally inherited missense variant c.1289A > G, p.(Asp430Gly), which perturbs the correct splicing of exon 13." — [PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)

**Genetic risk factors.** The sole established causal factor is biallelic *TMEM67* dysfunction. There are no reported common susceptibility loci or GWAS signals — RHYNS is fully Mendelian. Consanguinity and founder effects increase the risk of homozygous *TMEM67* genotypes in *TMEM67*-related disease generally; a recurrent founder missense variant p.Asn242Ser segregated across 22 affected members of 12 Iranian families with Joubert syndrome ([PMID: 28719906](https://pubmed.ncbi.nlm.nih.gov/28719906/)).

**Environmental risk factors, protective factors, and gene–environment interactions.** None are established for RHYNS. As a monogenic developmental disorder, disease occurrence is determined by genotype rather than environmental exposure. No protective alleles or modifier-driven risk reduction have been reported. This category is **not applicable** in the conventional epidemiologic sense.

---

## 3. Phenotypes

RHYNS is defined by four cardinal features plus additional craniofacial, sensory, and endocrine anomalies. Because the reported patient count is small, frequencies are qualitative and drawn from the index case ([PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)) and the first familial cases (two brothers; [PMID: 11391657](https://pubmed.ncbi.nlm.nih.gov/11391657/)).

| Phenotype | Type | HPO term (suggested) | Onset / progression | Frequency |
|-----------|------|----------------------|---------------------|-----------|
| Retinitis pigmentosa | Clinical sign / lab (ERG) | HP:0000510 | Childhood-onset, progressive | Cardinal (all cases) |
| Hypopituitarism (GH + TSH deficiency) | Lab abnormality | HP:0000871 (hypopituitarism); HP:0000824 (hypothyroidism) | Childhood; progressive growth failure | Cardinal |
| Nephronophthisis / ESRD | Clinical sign / lab | HP:0000090 | Insidious, childhood → ESRD | Cardinal |
| Skeletal dysplasia (acromelic) | Physical manifestation | HP:0002652; HP:0009826 (acromelia) | Congenital/childhood | Cardinal |
| Ptosis (left upper eyelid) | Physical sign | HP:0000508 | Congenital | Index case |
| Enophthalmos | Physical sign | HP:0000490 | — | Index case |
| Conductive (transmissive) hearing loss | Clinical sign | HP:0000405 | Childhood | Index case |
| Short stature / growth failure | Physical manifestation | HP:0004322 | Childhood | Common (GH deficiency) |

The index patient was a 17-year-old boy with "nephronophthisis, retinitis pigmentosa, left upper eyelid ptosis, enopthalmos, transmissive deafness, GH and TSH deficiency, and mild skeletal dysplasia" ([PMID: 9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/)). The two familial cases had "retinitis pigmentosa, growth hormone deficiency, and acromelic skeletal dysplasia" ([PMID: 11391657](https://pubmed.ncbi.nlm.nih.gov/11391657/)):

> "Here we report two brothers with retinitis pigmentosa, growth hormone deficiency, and acromelic skeletal dysplasia. We propose that their clinical picture is consistent with RHYNS syndrome." — [PMID: 11391657](https://pubmed.ncbi.nlm.nih.gov/11391657/)

RHYNS is cited in recent reviews as a bona fide ciliopathy cause of **syndromic retinitis pigmentosa**, distinct from the more common Usher and Bardet-Biedl syndromes:

> "Less common ciliopathies include Cohen syndrome, Joubert syndrome, cranioectodermal dysplasia, asphyxiating thoracic dystrophy, Mainzer-Saldino syndrome, and RHYNS syndrome." — [PMID: 39733931](https://pubmed.ncbi.nlm.nih.gov/39733931/)

**Quality-of-life impact.** Progressive visual loss (RP), end-stage renal disease requiring dialysis/transplant, short stature and endocrine dysfunction, and hearing impairment each impose a substantial daily-functioning burden. Disease-specific QoL instruments have not been applied to this ultra-rare condition; impact is inferred from the component disorders.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***TMEM67*** (transmembrane protein 67; encodes **meckelin**), OMIM 609884, located at **8q22.1**. Biallelic variants cause RHYNS ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)).

**Pathogenic variants in the index RHYNS family:**

| Variant (cDNA) | Protein | Type | Inheritance | Functional consequence |
|----------------|---------|------|-------------|------------------------|
| c.622A>T | p.(Arg208\*) | Nonsense | Paternal | Loss of function (truncation) |
| c.1289A>G | p.(Asp430Gly) | Missense | Maternal | Disrupts splicing of exon 13 |

Both variants act via **loss of function**. In the broader *TMEM67* spectrum, variant classification per ACMG/AMP ranges from pathogenic nonsense/frameshift (e.g., c.296delA p.Lys99SerfsTer6, [PMID: 38311563](https://pubmed.ncbi.nlm.nih.gov/38311563/)) to likely-pathogenic missense (e.g., c.1243G>A p.Val415Met, same report; c.1645C>T p.R549C in MKS3, [PMID: 26191240](https://pubmed.ncbi.nlm.nih.gov/26191240/)). Variant types documented across *TMEM67* disease include missense, nonsense, frameshift, and splice-altering changes; allele frequencies of pathogenic variants are rare/absent in gnomAD and population controls (e.g., c.1645C>T absent in 200 control chromosomes, [PMID: 26191240](https://pubmed.ncbi.nlm.nih.gov/26191240/)). All are **germline**.

**Allelic spectrum and genotype–phenotype associations.** *TMEM67* biallelic variants produce **≥8 distinguishable clinical conditions** ranging from early-lethal Meckel-Gruber syndrome to adults with only liver fibrosis — one of the widest continua in ciliopathies ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)). Key correlations from large Joubert cohorts:

- **Liver fibrosis and coloboma** are associated with loss of *TMEM67* function ([PMID: 26092869](https://pubmed.ncbi.nlm.nih.gov/26092869/)).
- **Kidney disease is frequent**, whereas **retinal degeneration is often absent** in *TMEM67* patients ([PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)):

> "Genotype-phenotype correlation revealed the absence of retinal degeneration in patients with TMEM67, C5orf52, or KIAA0586 variants. Chorioretinal coloboma was associated with a decreased risk for retinal degeneration and increased risk for liver disease. TMEM67 was frequently associated with kidney disease." — [PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)

Notably, RHYNS is distinguished within the *TMEM67* spectrum by the *presence* of retinitis pigmentosa, which is comparatively uncommon in typical *TMEM67*-Joubert patients — highlighting variable expressivity.

**Modifier genes.** Ciliary transition-zone modules interact synergistically; e.g., TMEM218 physically interacts with TMEM67/meckelin, and reduced TMEM218 dosage interacts with the NPHP module (Nphp4) to modulate ciliopathy severity ([PMID: 35137054](https://pubmed.ncbi.nlm.nih.gov/35137054/)). Oligogenic contributions (second-locus variants in other ciliopathy genes) can modify expressivity ([PMID: 21493627](https://pubmed.ncbi.nlm.nih.gov/21493627/)).

**Chromosomal abnormalities / epigenetics.** No recurrent epigenetic mechanism is established. A notable structural mechanism producing homozygosity for a *TMEM67* mutation is **maternal uniparental disomy of chromosome 8** (upd(8)mat), reported as an unexpected cause of Meckel-Gruber syndrome ([PMID: 28620746](https://pubmed.ncbi.nlm.nih.gov/28620746/)) — relevant to genetic counseling and recurrence-risk assessment.

---

## 5. Environmental Information

RHYNS is a **purely genetic monogenic disorder**. There are **no established environmental factors, lifestyle factors, or infectious agents** contributing to its causation or triggering. This section is not applicable beyond noting that environmental modifiers of the component organ diseases (e.g., nephrotoxin avoidance in chronic kidney disease) are general clinical considerations rather than RHYNS-specific etiologic factors.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *TMEM67*** (e.g., p.Arg208\* + p.Asp430Gly) → **lead to** deficient/dysfunctional meckelin protein ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)).
2. Deficient meckelin at the **ciliary transition zone** → **results in** defective transition-zone gating and impaired ciliogenesis / abnormal primary cilium morphology ([PMID: 23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/); [PMID: 28487520](https://pubmed.ncbi.nlm.nih.gov/28487520/)).
3. Impaired transition-zone function → **results in** failure to phosphorylate the non-canonical Wnt receptor **ROR2** upon Wnt5a stimulation (meckelin's N-terminal extracellular domain preferentially binds Wnt5a; ROR2 colocalises/interacts with TMEM67 at the transition zone) ([PMID: 26035863](https://pubmed.ncbi.nlm.nih.gov/26035863/)).
4. Loss of Wnt5a–ROR2 non-canonical Wnt signalling, plus secondary **deregulation of Shh and canonical Wnt/β-catenin** signalling, **branches** into:
   - **4A (developmental patterning branch):** basal-body mispositioning and disrupted planar/branching morphogenesis → **lead to** skeletal dysplasia, craniofacial anomalies (ptosis, enophthalmos), inner-ear defects (conductive hearing loss), and (inferred) hypothalamic-pituitary maldevelopment → hypopituitarism ([PMID: 26035863](https://pubmed.ncbi.nlm.nih.gov/26035863/); [PMID: 23283079](https://pubmed.ncbi.nlm.nih.gov/23283079/); [PMID: 24613594](https://pubmed.ncbi.nlm.nih.gov/24613594/)).
   - **4B (epithelial-maintenance branch):** upregulated canonical Wnt in renal/hepatic tubular epithelia → **results in** cystic tubulointerstitial fibrosis → nephronophthisis and end-stage renal disease ([PMID: 23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/)).
   - **4C (photoreceptor branch, inferred):** connecting-cilium dysfunction in photoreceptors → **leads to** progressive photoreceptor degeneration → retinitis pigmentosa (inferred from general ciliopathy biology; the connecting cilium is a specialized transition zone).

```
   Biallelic TMEM67 LoF
           │
   Dysfunctional meckelin (ciliary transition zone)
           │
   Defective TZ gating / abnormal ciliogenesis
           │
   Failed Wnt5a–ROR2 non-canonical Wnt signalling
   + deregulated Shh & canonical Wnt/β-catenin
           │
   ┌───────┼────────────────────────┐
   ▼        ▼                        ▼
 [4A]     [4B]                     [4C, inferred]
 Dev.     Renal/hepatic            Photoreceptor
 patterning epithelial Wnt↑        connecting cilium
   │        │                        │
 Skeletal  Cystic tubulointerstitial  Retinitis
 dysplasia, fibrosis → NPHP → ESRD   pigmentosa
 craniofacial,
 inner ear,
 pituitary → hypopituitarism
```

### Detail by category

**Molecular pathways.** The core lesion is in **non-canonical Wnt (planar cell polarity) signalling via Wnt5a–ROR2**, with meckelin essential for ROR2 phosphorylation:

> "TMEM67 (meckelin) is essential for phosphorylation of the non-canonical Wnt receptor ROR2 (receptor-tyrosine-kinase-like orphan receptor 2) upon stimulation with Wnt5a-conditioned medium. ROR2 also colocalises and interacts with TMEM67 at the ciliary transition zone." — [PMID: 26035863](https://pubmed.ncbi.nlm.nih.gov/26035863/)

Downstream, *Tmem67* loss produces "the loss of primary cilia, diminished Shh signalling and dorsalization of the caudal neural tube… high de-regulated canonical Wnt/β-catenin signalling" ([PMID: 23283079](https://pubmed.ncbi.nlm.nih.gov/23283079/)). Suggested pathway terms: Wnt signalling, Shh signalling, planar cell polarity.

**Cellular processes.** Ciliogenesis, ciliary transition-zone gating, basal-body positioning, epithelial branching morphogenesis, and cilium-dependent signal transduction. Meckelin is required for cilia-dependent Shh signalling and retinoic-acid-dependent neural differentiation in mouse embryonic stem cells:

> "differentiating along the neuronal lineage activate the cilia-dependent sonic hedgehog signaling machinery, which is impaired in Meckelin knock-out cells." — [PMID: 24613594](https://pubmed.ncbi.nlm.nih.gov/24613594/)

**Protein dysfunction.** Meckelin (TMEM67) is a transmembrane transition-zone protein; nonsense and splice-disrupting variants cause loss of function. Meckelin also interacts with **filamin A**, and disruption of the filamin A–meckelin interaction impairs primary cilium formation ([PMID: 32156598](https://pubmed.ncbi.nlm.nih.gov/32156598/)).

**Tissue-damage mechanisms.** Chronic sclerosing tubulointerstitial nephropathy with cortico-medullary cysts (fibrosis) drives renal failure; photoreceptor degeneration drives retinal disease.

**Suggested ontology terms.** GO:0060271 (cilium assembly), GO:0035869 (ciliary transition zone), GO:0035567 (non-canonical Wnt signaling pathway), GO:0007224 (smoothened/Shh signaling); CL:0000210 (photoreceptor cell), CL:1000507 (kidney tubule cell); UBERON:0002113 (kidney), UBERON:0000970 (eye), UBERON:0000007 (pituitary gland).

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Kidney** (UBERON:0002113) — nephronophthisis, cortico-medullary cysts, tubulointerstitial fibrosis, ESRD.
- **Eye / retina** (UBERON:0000970 / UBERON:0000966) — retinitis pigmentosa; photoreceptor layer.
- **Pituitary gland / hypothalamic-pituitary axis** (UBERON:0000007) — GH and TSH deficiency (hypopituitarism).
- **Skeleton** (UBERON:0004288) — acromelic/mild skeletal dysplasia.

**Secondary / additional involvement:** Eyelid (ptosis), orbit (enophthalmos), inner/middle ear (conductive hearing loss). Within the broader *TMEM67* spectrum, **liver** (fibrosis, ductal plate malformation) is frequently affected ([PMID: 26092869](https://pubmed.ncbi.nlm.nih.gov/26092869/)).

**Body systems:** urinary/renal, visual/nervous, endocrine, skeletal, auditory.

**Tissue and cell level:** Ciliated epithelia are the common target — renal tubular epithelial cells, retinal photoreceptors (whose connecting cilium is a modified transition zone), and (inferred) pituitary/hypothalamic ciliated cells. Suggested CL terms: CL:0000210 (photoreceptor cell), CL:1000507 (kidney tubule cell).

**Subcellular level:** The **primary cilium** and specifically the **ciliary transition zone** (GO:0035869), plus the **basal body** (GO:0036064). Meckelin is a transmembrane protein of the ciliary membrane/transition zone.

**Localization / lateralization:** Kidney and retinal involvement are **bilateral**; ptosis in the index case was unilateral (left upper eyelid).

---

## 8. Temporal Development

**Onset.** Childhood-onset and insidious. The nephronophthisis component "presents insidiously with polyuria, polydipsia, anemia and growth failure, progressing to end-stage renal disease during childhood" ([PMID: 15384098](https://pubmed.ncbi.nlm.nih.gov/15384098/)). Skeletal dysplasia is congenital/early-childhood; RP and hypopituitarism manifest in childhood and progress.

> "All cases showed insidious development of end-stage renal disease during childhood, preceded by polyuria/polydipsia, anemia, and growth failure. Decreased urinary concentrating ability and excessive sodium loss were the characteristic laboratory findings." — [PMID: 15384098](https://pubmed.ncbi.nlm.nih.gov/15384098/)

**Progression.** Chronic, progressive, lifelong. Nephronophthisis advances to ESRD, typically in the first two decades. Retinitis pigmentosa is progressive. Within severe *TMEM67* compound-heterozygous genotypes, kidney disease can present as early as **neonatal ESRD** ([PMID: 28726664](https://pubmed.ncbi.nlm.nih.gov/28726664/)); RHYNS itself represents a milder, viable end of the spectrum with survival into adulthood (index case aged 17).

**Critical periods.** Childhood is the window for growth-hormone/thyroid replacement (to permit catch-up growth) and for renal-protective monitoring before ESRD. Prenatally, severe *TMEM67* genotypes are detectable by ultrasound and molecular testing.

---

## 9. Inheritance and Population

**Epidemiology.** RHYNS is **ultra-rare** — only a handful of patients have been reported (the 1997 index case and the two familial brothers). No formal prevalence/incidence figures exist. For context, nephronophthisis (the "N") is a leading monogenic cause of childhood ESRD, accounting for **7–20% of terminal renal failure in the first two decades of life** ([PMID: 3524015](https://pubmed.ncbi.nlm.nih.gov/3524015/)):

> "Its frequency is reported to vary between 7 and 20% of all cases of terminal renal failure in childhood. Usually the onset is insidious, with polyuria, polydipsia and anaemia being the main clinical features." — [PMID: 3524015](https://pubmed.ncbi.nlm.nih.gov/3524015/)

**Inheritance.** **Autosomal recessive**, confirmed by biallelic *TMEM67* variants ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)). The first familial cases (two affected brothers) supported recessive inheritance, though the authors noted that because all four known cases were male at the time, an X-linked mode could not be formally excluded ([PMID: 11391657](https://pubmed.ncbi.nlm.nih.gov/11391657/)); the subsequent *TMEM67* discovery settled this as autosomal recessive.

**Penetrance / expressivity.** Biallelic *TMEM67* loss is highly penetrant for ciliopathy, but **expressivity is markedly variable** — the same gene produces phenotypes from lethal Meckel-Gruber to adult liver-only disease. RHYNS occupies the mild/viable pole.

**Founder effects / consanguinity.** Consanguinity increases homozygous-genotype risk. A founder p.Asn242Ser variant was identified across 22 affected members of 12 Iranian Joubert families:

> "confirmed the presence of the homozygous mutation in 22 affected members of 12 nuclear families. We propose that Asn242Ser is a founder mutation." — [PMID: 28719906](https://pubmed.ncbi.nlm.nih.gov/28719906/)

Uniparental disomy (upd(8)mat) is a rare non-Mendelian route to homozygosity ([PMID: 28620746](https://pubmed.ncbi.nlm.nih.gov/28620746/)).

**Demographics.** No established ethnic predilection specific to RHYNS. Reported cases have been male, but the small number precludes conclusions about sex ratio; autosomal recessive inheritance predicts an equal sex distribution.

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Renal:** decreased urinary concentrating ability, excessive sodium (salt) loss, anemia, rising creatinine; renal ultrasound showing normal-to-small kidneys with increased echogenicity and cortico-medullary cysts; renal biopsy showing chronic sclerosing tubulointerstitial nephropathy ([PMID: 15384098](https://pubmed.ncbi.nlm.nih.gov/15384098/); [PMID: 3524015](https://pubmed.ncbi.nlm.nih.gov/3524015/)).
- **Endocrine:** provocative GH testing, IGF-1, TSH/free T4 confirming GH and TSH deficiency; pituitary MRI (may show hypoplasia / stalk abnormalities, by analogy to pituitary stalk interruption syndrome — a ciliary-signalling-related developmental defect, [PMID: 34238482](https://pubmed.ncbi.nlm.nih.gov/34238482/)).
- **Ophthalmologic:** electroretinography (ERG) showing rod-cone dysfunction, fundoscopy with pigmentary retinopathy, OCT.
- **Auditory:** audiometry (conductive hearing loss).
- **Skeletal:** radiographic skeletal survey (acromelic dysplasia).

**Genetic testing (definitive).** Molecular confirmation via **whole-exome sequencing** or **ciliopathy/nephronophthisis gene panels** including *TMEM67*; single-gene *TMEM67* testing where phenotype is highly suggestive. WES identified the causal variants in the index RHYNS family ([PMID: 29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/)). Chromosomal microarray may be added; note UPD(8) can be detected by SNP array ([PMID: 28620746](https://pubmed.ncbi.nlm.nih.gov/28620746/)). Genetic diagnosis is "essential for reproductive counseling and the option of preimplantation and prenatal diagnosis as well as medical management and prognostic counseling for the age-dependent and progressive organ-specific manifestations" ([PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)).

**Differential diagnosis.** Other syndromic RP/ciliopathies: Senior-Løken syndrome (nephronophthisis + retinal dystrophy, e.g., IQCB1/NPHP5, [PMID: 41316455](https://pubmed.ncbi.nlm.nih.gov/41316455/)), Joubert syndrome (molar-tooth sign), Bardet-Biedl syndrome, Alström syndrome, and other nephronophthisis-related ciliopathies. The distinguishing feature of RHYNS is the combination of **hypopituitarism + skeletal dysplasia** with RP and NPHP.

**Screening.** Cascade testing of at-risk relatives once the familial *TMEM67* variants are known; prenatal and preimplantation genetic diagnosis are available.

---

## 11. Outcome / Prognosis

**Survival/mortality.** RHYNS is compatible with survival into adulthood (index case aged 17). The principal life-limiting complication is **end-stage renal disease from nephronophthisis**, which without renal replacement is fatal. There are no cohort-derived survival statistics for RHYNS specifically.

**Morbidity/function.** Substantial: progressive blindness (RP), dialysis dependence or transplant, short stature and endocrine dysfunction, hearing impairment. Quality of life is affected across visual, renal, growth, and auditory domains.

**Disease course and complications.** Chronic and progressive. Renal transplantation is definitive for the renal component (see Treatment). Within fibrocystic liver-kidney disease broadly, catch-up growth has been observed after transplantation ([PMID: 22360404](https://pubmed.ncbi.nlm.nih.gov/22360404/)).

**Prognostic factors.** Severity of the *TMEM67* genotype (truncating vs. hypomorphic missense) correlates with overall disease severity across the allelic spectrum; earlier ESRD onset (even neonatal in severe compound-heterozygotes, [PMID: 28726664](https://pubmed.ncbi.nlm.nih.gov/28726664/)) portends worse renal prognosis. Timeliness of hormone replacement affects growth outcome.

---

## 12. Treatment

**No disease-modifying or gene-targeted therapy exists.** Management is **multidisciplinary, supportive, and organ-directed** ([PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)).

| Organ system | Intervention | NCIT (suggested) |
|--------------|--------------|------------------|
| Kidney (ESRD) | Dialysis; **kidney transplantation** (definitive) | NCIT:C15366 (Kidney Transplantation); NCIT:C15248 (Dialysis) |
| Endocrine | **Growth hormone** replacement; **thyroid hormone** (levothyroxine) replacement | NCIT:C1301 (Recombinant Human GH); NCIT:C29171 (Levothyroxine) |
| Eye (RP) | Low-vision aids, ophthalmologic surveillance; nutritional support explored in ciliopathy RP | NCIT:C15277 (Supportive Care) |
| Hearing | Hearing aids / audiologic support | — |

**Kidney transplantation is a turning point** in nephronophthisis-related ciliopathy:

> "kidney transplant is a turning point" — [PMID: 42538694](https://pubmed.ncbi.nlm.nih.gov/42538694/)

Critically, **nephronophthisis does not recur in the renal allograft** because it is an intrinsic tubular disease, making transplantation effectively curative for the renal component. Pediatric outcomes for fibrocystic liver-kidney disease show a median age at first transplant of 9.7 years with generally favorable graft survival ([PMID: 25074681](https://pubmed.ncbi.nlm.nih.gov/25074681/)).

**Hormone replacement** for hypopituitarism (GH, thyroid hormone) treats the endocrine component and, with timely initiation, supports catch-up growth (catch-up growth after transplantation has been documented in fibrocystic disease, [PMID: 22360404](https://pubmed.ncbi.nlm.nih.gov/22360404/)). **Retinitis pigmentosa** currently has no curative therapy; management is low-vision support and surveillance, with nutritional/adjunctive strategies under exploration in ciliopathy RP ([PMID: 40642756](https://pubmed.ncbi.nlm.nih.gov/40642756/)).

**Experimental / future therapeutics.** No RHYNS-specific clinical trials. Gene-therapy and read-through approaches are conceptually relevant given the recessive loss-of-function mechanism but remain preclinical.

---

## 13. Prevention

RHYNS cannot be prevented in the primary (public-health) sense — it is a monogenic congenital disorder. Prevention is **reproductive and genetic**:

- **Genetic counseling** for at-risk families, quantifying the 25% recurrence risk for autosomal recessive inheritance (with UPD as a rare exception, [PMID: 28620746](https://pubmed.ncbi.nlm.nih.gov/28620746/)).
- **Carrier testing / cascade screening** once familial *TMEM67* variants are identified.
- **Prenatal diagnosis and preimplantation genetic diagnosis (PGD)**, enabled by molecular confirmation ([PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)).
- **Secondary/tertiary prevention** = organ surveillance and early intervention (renal function monitoring, endocrine replacement, ophthalmologic follow-up) to delay complications.

Immunization and behavioral/environmental interventions are not applicable to disease causation.

---

## 14. Other Species / Natural Disease

*TMEM67* is evolutionarily conserved; disease-relevant orthologs exist in **mouse (*Tmem67*), zebrafish (*tmem67*), and sheep (*TMEM67*)**. The R549 meckelin residue is conserved "across human, rat, mouse, zebrafish, chicken, wolf and platypus genomes" ([PMID: 26191240](https://pubmed.ncbi.nlm.nih.gov/26191240/)). A **naturally occurring ovine (sheep) model** carrying homozygous *TMEM67* p.(Ile681Asn; Ile687Ser) missense mutations displays hepatorenal fibrocystic disease with dysmorphic primary cilia — the first large-animal natural model of a Meckel-like *TMEM67* ciliopathy:

> "Here we describe an ovine model of MKS, with kidney and liver abnormalities, without polydactyly or occipital encephalocoele. Homozygous missense p.(Ile681Asn; Ile687Ser) mutations identified in ovine TMEM67 were pathogenic in zebrafish phenotype rescue assays." — [PMID: 28487520](https://pubmed.ncbi.nlm.nih.gov/28487520/)

This natural model has veterinary and comparative-pathology relevance, demonstrating evolutionary conservation of the transition-zone ciliary mechanism. There is no zoonotic potential (non-infectious genetic disease).

---

## 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|-------|------|--------------------------|-----------|
| ***Tmem67*-null mouse (bpck)** | Mammalian knockout | Renal cystic disease, plus eye, skeletal, and inner-ear abnormalities; upregulated canonical Wnt in cyst linings/fibroblasts | [PMID: 23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/) |
| ***Tmem67*(tm1Dgen/H1) knockout mouse** | Mammalian knockout | Pulmonary hypoplasia, ventricular septal defects, shortened body axis, limb abnormalities, basal-body/kinocilium mispositioning — phenocopies *Wnt5a* and *Ror2* knockouts | [PMID: 26035863](https://pubmed.ncbi.nlm.nih.gov/26035863/) |
| **Zebrafish *tmem67* morphants** | Vertebrate | MKS/ciliopathy phenotypes; used to validate variant pathogenicity in rescue assays | [PMID: 23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/); [PMID: 28487520](https://pubmed.ncbi.nlm.nih.gov/28487520/) |
| **Ovine (sheep)** | Mammalian, natural | Hepatorenal fibrocystic disease, dysmorphic primary cilia | [PMID: 28487520](https://pubmed.ncbi.nlm.nih.gov/28487520/) |
| **Mouse embryonic stem cells** | In vitro / cellular | Impaired cilia-dependent Shh signalling; defective retinoic-acid-dependent neural differentiation | [PMID: 24613594](https://pubmed.ncbi.nlm.nih.gov/24613594/) |

> "we analyzed phenotypes in the Tmem67 null mouse (bpck) and in zebrafish tmem67 morphants. Phenotypes similar to those in human MKS and other ciliopathy models were observed, with additional eye, skeletal and inner ear abnormalities characterized in the bpck mouse." — [PMID: 23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/)

**Model limitations.** These models capture the renal, skeletal, ocular, and inner-ear ciliopathy phenotypes and the Wnt/Shh mechanism, but no model has been reported that specifically recapitulates the **hypopituitarism** of RHYNS, and the RHYNS phenotype itself (mild/viable) differs from the more severe MKS end modeled by nulls. Resources: MGI (mouse), ZFIN (zebrafish).

---

## Mechanistic Model / Interpretation

RHYNS is best understood as **one point on a continuum of *TMEM67* transition-zone ciliopathy**. A single molecular lesion — biallelic loss of meckelin at the ciliary transition zone — produces pleiotropic, multi-organ disease because the primary cilium is a signalling hub required in nearly every tissue. The unifying pathogenic node is **failure of Wnt5a–ROR2 non-canonical Wnt signalling**, with secondary deregulation of **Shh** and **canonical Wnt/β-catenin**. This branches into a *developmental patterning* program (skeletal dysplasia, craniofacial/inner-ear anomalies, and inferred pituitary maldevelopment) and an *epithelial-maintenance* program (fibrocystic nephronophthisis; photoreceptor degeneration).

What distinguishes RHYNS clinically from typical *TMEM67*-Joubert is its particular combination: **retinitis pigmentosa is present** (uncommon in most *TMEM67* patients, where retinal degeneration is often absent, [PMID: 28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/)) alongside **hypopituitarism and skeletal dysplasia**, without the pathognomonic molar-tooth sign emphasized in Joubert. This underscores the **variable expressivity** that is the hallmark of *TMEM67* disease. The specific compound-heterozygous genotype in the index family (a truncating p.Arg208\* combined with a splice-perturbing hypomorphic p.Asp430Gly) likely produces a partial, tissue-modulated loss of function that lands the phenotype at the mild/viable end rather than at lethal Meckel-Gruber.

---

## Evidence Base

| PMID | Title (abbreviated) | Role |
|------|--------------------|------|
| [29891882](https://pubmed.ncbi.nlm.nih.gov/29891882/) | *Biallelic TMEM67 variants cause RHYNS* | **Defines causal gene & variants; landmark** |
| [9375913](https://pubmed.ncbi.nlm.nih.gov/9375913/) | *RHYNS: a new syndrome?* | **Original clinical description (tetrad)** |
| [11391657](https://pubmed.ncbi.nlm.nih.gov/11391657/) | *Familial RHYNS in two brothers* | Familial/AR evidence, expressivity |
| [26035863](https://pubmed.ncbi.nlm.nih.gov/26035863/) | *TMEM67 controls basal body positioning via non-canonical Wnt* | **Core mechanism (Wnt5a-ROR2)** |
| [23283079](https://pubmed.ncbi.nlm.nih.gov/23283079/) | *Deregulated ciliogenesis, Shh & Wnt in ciliopathy spectrum* | Downstream Shh/Wnt deregulation |
| [23393159](https://pubmed.ncbi.nlm.nih.gov/23393159/) | *Meckelin regulator of cilia function (bpck mouse, zebrafish)* | **Animal models; renal/eye/skeletal** |
| [28487520](https://pubmed.ncbi.nlm.nih.gov/28487520/) | *Ovine hepatorenal fibrocystic TMEM67 model* | Natural large-animal model |
| [24613594](https://pubmed.ncbi.nlm.nih.gov/24613594/) | *Meckelin required for Shh-dependent neural differentiation* | Developmental patterning link |
| [28125082](https://pubmed.ncbi.nlm.nih.gov/28125082/) | *Joubert 100-patient genotype-phenotype* | TMEM67 kidney/retina correlations; management |
| [26092869](https://pubmed.ncbi.nlm.nih.gov/26092869/) | *Joubert genetic heterogeneity review* | TMEM67–liver fibrosis/coloboma |
| [28719906](https://pubmed.ncbi.nlm.nih.gov/28719906/) | *Founder Asn242Ser in Iranian families* | Founder effect |
| [15384098](https://pubmed.ncbi.nlm.nih.gov/15384098/) | *Nephronophthisis in Joubert-related disorders* | **NPHP clinical/lab course** |
| [3524015](https://pubmed.ncbi.nlm.nih.gov/3524015/) | *Familial juvenile nephronophthisis* | NPHP epidemiology |
| [28726664](https://pubmed.ncbi.nlm.nih.gov/28726664/) | *Expanded TMEM67 phenotype (neonatal ESRD)* | Severity spectrum |
| [42538694](https://pubmed.ncbi.nlm.nih.gov/42538694/) | *Kidney transplant in Joubert* | Definitive renal management |
| [25074681](https://pubmed.ncbi.nlm.nih.gov/25074681/) | *Transplant in fibrocystic liver-kidney disease* | Transplant outcomes |
| [39733931](https://pubmed.ncbi.nlm.nih.gov/39733931/) | *Syndromic retinitis pigmentosa* | RHYNS recognized as ciliopathy |
| [28620746](https://pubmed.ncbi.nlm.nih.gov/28620746/) | *UPD(8) causing MKS* | Non-Mendelian mechanism/counseling |
| [26191240](https://pubmed.ncbi.nlm.nih.gov/26191240/) | *TMEM67 missense causing MKS3* | Variant conservation/pathogenicity |
| [35137054](https://pubmed.ncbi.nlm.nih.gov/35137054/) | *TMEM218–NPHP module interaction* | Modifier/oligogenic biology |

---

## Limitations and Knowledge Gaps

1. **Very small case count.** RHYNS is defined by only a few published patients; frequency, penetrance, sex ratio, and natural-history statistics are therefore anecdotal, and much detail is extrapolated from the broader *TMEM67*/Joubert/Meckel literature.
2. **Hypopituitarism mechanism is inferred, not demonstrated.** No model recapitulates the pituitary phenotype, and the causal link from ciliary Shh/Wnt dysfunction to hypothalamic-pituitary maldevelopment remains hypothetical (supported by analogy to pituitary stalk interruption syndrome, [PMID: 34238482](https://pubmed.ncbi.nlm.nih.gov/34238482/)).
3. **Retinitis pigmentosa branch is inferred** from general connecting-cilium ciliopathy biology rather than direct RHYNS histopathology.
4. **Genotype–phenotype specificity is incomplete** — why the index genotype yields RHYNS rather than another *TMEM67* phenotype is not experimentally resolved.
5. **No omics data** (transcriptomic, proteomic, metabolomic) specific to RHYNS exist.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate additional cases** via GeneMatcher / Matchmaker Exchange to build a *TMEM67*-RHYNS cohort and formally test genotype–phenotype correlation (especially the RP-present, hypopituitarism subset).
2. **Model the pituitary phenotype** — examine hypothalamic-pituitary development in *Tmem67* hypomorphic mice or patient iPSC-derived pituitary organoids to test the inferred Shh/Wnt-driven hypopituitarism mechanism.
3. **Photoreceptor connecting-cilium studies** — retinal organoids or ovine/mouse retina to directly confirm the RP branch.
4. **Functional characterization of p.Asp430Gly splicing** and the truncating allele to define residual meckelin function and correlate with phenotype mildness.
5. **Longitudinal surveillance protocol** — establish an organ-directed monitoring schedule (renal function, endocrine axes, ERG, audiometry) for confirmed *TMEM67*-RHYNS patients to define natural history and optimize intervention timing.
6. **Preclinical therapeutic exploration** — evaluate read-through / gene-supplementation strategies leveraging the recessive loss-of-function mechanism.

---

*Report compiled from 8 confirmed findings and 35 reviewed papers across 5 investigation iterations. Evidence types: human clinical case reports and cohorts, model organism (mouse, zebrafish, sheep), and in vitro/cellular studies.*


## Artifacts

- [OpenScientist final report](RHYNS_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RHYNS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 27 |
| On topic | 20 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23283079` *(abstract only)*: "the loss of primary cilia, diminished Shh signalling and dorsalization of the caudal neural tube… high de-regulated canonical Wnt/β-catenin signalling"
  - closest text in source: "An MKS-like incipient congenic group (F6 to F10) manifested very variable neurological features (including exencephaly, and frontal/occipital encephalocele) that were associated with the loss of primary cilia, diminished Shh signalling and dorsalization of the caudal neural tube"
- `PMID:15384098` *(abstract only)*: "presents insidiously with polyuria, polydipsia, anemia and growth failure, progressing to end-stage renal disease during childhood"
  - closest text in source: "All cases showed insidious development of end-stage renal disease during childhood, preceded by polyuria/polydipsia, anemia, and growth failure"
- `PMID:28719906` *(abstract only)*: "confirmed the presence of the homozygous mutation in 22 affected members of 12 nuclear families. We propose that Asn242Ser is a founder mutation."
  - closest text in source: "Sanger sequencing of a known mutation (NM_153704.5: c.725A>G; p.Asn242Ser) in TMEM67 identified from studying another Iranian family using whole-exome sequencing confirmed the presence of the homozygous mutation in 22 affected members of 12 nuclear families"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:32156598` (2 mentions) - TACC3 promotes prostate cancer cell proliferation and restrains primary cilium formation.
  - shared terms: meckelin

Weighed against this report's own most characteristic terms: `tmem67`, `rhyn`, `disease`, `renal`, `ciliopathy`, `nephronophthisis`, `pigmentosa`, `hypopituitarism`, `retinitis`, `skeletal`, `phenotype`, `variant`, `meckelin`, `kidney`, `loss`, `joubert`, `syndrome`, `dysplasia`, `ciliary`, `clinical`.
