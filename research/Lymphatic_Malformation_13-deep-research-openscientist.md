---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T03:24:30.456901'
end_time: '2026-10-25T03:50:58.252539'
duration_seconds: 1587.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lymphatic malformation 13
  mondo_id: MONDO:0859379
  category: Mendelian
  causal_genes: THSD1
  omim_id: not recorded
  synonyms: LMPHM13; THSD1-related generalized lymphatic dysplasia; THSD1-related
    non-immune hydrops fetalis
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lymphatic_Malformation_13-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lymphatic_Malformation_13-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphatic malformation 13
- **MONDO ID:** MONDO:0859379 (if available)
- **Causal gene(s):** THSD1
- **OMIM:** not recorded
- **Synonyms:** LMPHM13; THSD1-related generalized lymphatic dysplasia; THSD1-related non-immune hydrops fetalis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lymphatic malformation 13** covering all of the
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

# Lymphatic Malformation 13 (LMPHM13): A Comprehensive Disease Characteristics Report

**Disease:** Lymphatic malformation 13 (LMPHM13)
**MONDO ID:** MONDO:0859379
**OMIM phenotype:** #620244 (established; earlier reports used the generic NIHF entry OMIM 236750)
**Causal gene:** **THSD1** (Thrombospondin type-1 domain-containing protein 1), 13q14.3
**Category:** Mendelian, autosomal recessive

---

## Summary

**Lymphatic malformation 13 (LMPHM13) is a rare autosomal-recessive lymphatic/vascular disorder caused by biallelic loss-of-function variants in the gene *THSD1* (thrombospondin type-1 domain-containing protein 1), located at chromosome 13q14.3.** The gene encodes an 852-amino-acid type-I transmembrane protein that is most highly expressed in lymphatic endothelial cells. LMPHM13 was first linked to THSD1 by Shamseldin and colleagues in 2015 through autozygosity mapping plus exome sequencing in consanguineous families, in which a THSD1 founder mutation accounted for embryonic lethality in three families and a second THSD1 mutation produced a milder phenotype of hydrops fetalis with persistent postnatal edema [[PMID: 26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/)]. Although "lymphatic malformation 13" is a serial-numbered name that does not itself identify a gene, all identifiers and the literature point consistently to THSD1 — distinct from other numbered lymphatic malformations caused by *PIEZO1*, *FLT4/VEGFR3*, *CCBE1*, *FAT4*, or *EPHB4*.

The clinical picture spans a severity spectrum. At the severe end are embryonic/fetal lethality and non-immune hydrops fetalis (NIHF) with pleural and peritoneal effusions. In survivors, LMPHM13 is a multisystem disorder including recurrent hydrocele, cutaneous/midline hemangiomas, congenital heart defects, intestinal malabsorption/protein-losing enteropathy, and dysmorphic features. At the mild/late end is chronic peripheral lymphedema persisting into adulthood (reported to age 79). Mechanistically, THSD1 stabilizes endothelial focal adhesions by suppressing FAK–Beclin-1–mediated autophagic turnover of those adhesions. When THSD1 is lost, endothelial and lymphatic-endothelial cells detach from the basement membrane and the vascular/lymphatic barrier fails, allowing fluid and protein to leak into interstitial spaces and body cavities. The same vessel-fragility mechanism underlies an allelic, dominantly-acting association of THSD1 with intracranial aneurysm and subarachnoid hemorrhage, which must be distinguished from the recessive lymphatic phenotype.

Management is entirely supportive — drainage of effusions, albumin replacement, nutritional support, and lymphatic surgery for refractory lymphedema/protein-losing enteropathy. There is no disease-modifying therapy. Prevention rests on genetic counseling with prenatal/carrier testing, particularly in consanguineous families, where most reported cases have occurred. This report synthesizes eight confirmed findings drawn from twelve primary papers covering the disease's genetics, molecular mechanism, cellular origin, clinical spectrum, model organisms, and population genetics.

---

## Key Findings

### Finding 1 — LMPHM13 is an autosomal-recessive THSD1-related lymphatic/vascular disorder

LMPHM13 (MONDO:0859379) is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *THSD1***, a gene at chromosome 13q14.3 encoding a thrombospondin type-1 domain-containing transmembrane protein. The gene–disease link was first established by Shamseldin et al. (2015), who used autozygosity mapping combined with exome sequencing in consanguineous families. In their words: *"A founder mutation in one of these genes, THSD1, which has been linked to vascular permeability, accounted for embryonic lethality in three of the study families. Unlike the other six candidate genes, we were able to identify a second mutation in THSD1 in a family with a less severe phenotype consisting of hydrops fetalis and persistent postnatal edema"* [[PMID: 26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/)]. This single observation demonstrates both the allelic severity spectrum (lethality ↔ survivable edema) and the vascular-permeability basis of the disorder.

Autosomal-recessive inheritance was independently confirmed by Abdelrahman et al. (2018), who reported a novel truncating THSD1 variant that *"cosegregates with the described phenotype in an autosomal recessive mode of inheritance"* in a consanguineous family of four affected individuals [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/)]. Multiple subsequent consanguineous-family reports (Al Rawi 2021; Saxena 2023; Lobos Urbina 2025) have reproduced AR inheritance with truncating variants, cementing the gene–disease relationship.

### Finding 2 — THSD1 stabilizes endothelial focal adhesions by suppressing FAK–Beclin-1 autophagy

The core cellular function of THSD1 is the stabilization of endothelial focal adhesions (FAs) to the basement membrane. Santiago-Sim et al. (2016), working in an in vitro endothelial model, showed that *"THSD1 loss impaired endothelial cell focal adhesion to the basement membrane. These adhesion defects could be rescued by expression of wild-type THSD1"* but not by mutant THSD1 — directly tying the molecular defect to loss of function [[PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/)].

The downstream molecular logic was defined by Xu et al. (2024): *"THSD1 negatively regulates Beclin 1, a central autophagy regulator, at FAs through interactions with focal adhesion kinase (FAK). THSD1 inactivation diminishes FAK activity and relieves its inhibitory phosphorylation on Beclin 1. This, in turn, promotes the complex formation between Beclin 1 and ATG14"* [[PMID: 38396816](https://pubmed.ncbi.nlm.nih.gov/38396816/)]. In normal cells, THSD1 keeps FAK active, FAK phosphorylates and inhibits Beclin-1, and autophagic turnover of focal adhesions is suppressed — maintaining stable endothelial attachment and barrier integrity. When THSD1 is lost, FAK activity falls, Beclin-1 is de-repressed, the Beclin-1/ATG14 autophagy-initiation complex forms, and focal adhesions are turned over by autophagy independently of the mTOR/AMPK axis. The 2025 review summarizes this as THSD1 *"promotes focal adhesion assembly and suppresses autophagy-mediated adhesion turnover, thereby stabilizing endothelial attachment and maintaining barrier function"* [[PMID: 40564011](https://pubmed.ncbi.nlm.nih.gov/40564011/)].

### Finding 3 — Clinical spectrum: NIHF with effusions, hydrocele, hemangiomas, cardiac defects, and chylous/protein-losing complications

Across case reports, LMPHM13 presents a recurrent multisystem phenotype. Abdelrahman et al. (2018) provided the canonical description in four affected children: *"Fetal onset pleural and peritoneal effusions were detected in all four patients and were born with moderate to severe hydrops fetalis that resolved with age. Follow up showed relatively normal growth and development apart from mild ascites and haemangiomas in all affected children, recurrent hydrocele in all affected males, intestinal malabsorption in two patients, dysmorphic features in two patients, and congenital cardiac defects in three out of four patients"* [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/)].

The spectrum widens at both ends. At the severe/perinatal end, Lobos Urbina (2025) reported a premature infant with a novel truncating variant (c.1009delC:p.Gln337Argfs*73) presenting ascites, pleural effusion, bilateral hydrocele, chylothorax, intestinal perforation, patent ductus arteriosus, capillary hemangiomas, dysmorphism, and midline hemangiomas [[PMID: 41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/)]. Al Rawi (2021) documented an extremely premature (25-week) infant whose course was complicated by pulmonary hypertension and chronic lung disease [[PMID: 33569873](https://pubmed.ncbi.nlm.nih.gov/33569873/)]. At the later/milder end, Mortada (2026) documented chronic lower-limb lymphedema with protein-losing enteropathy (PLE) requiring lymphatic surgery: *"the successful surgical management of chronic lower limb lymphedema and PLE in a 7-year-old male with a thrombospondin type 1 domain-containing 1 (THSD1) mutation"* [[PMID: 42583604](https://pubmed.ncbi.nlm.nih.gov/42583604/)]. Amo (2026) extended the age range dramatically with a 79-year-old woman with lifelong peripheral edema caused by a homozygous splice-site variant [[PMID: 42714234](https://pubmed.ncbi.nlm.nih.gov/42714234/)]. Importantly, NIHF frequently **resolves with age** in survivors, which distinguishes THSD1-NIHF from many other lethal hydrops etiologies [[PMID: 37993095](https://pubmed.ncbi.nlm.nih.gov/37993095/)].

### Finding 4 — Model organisms: zebrafish and mouse LOF recapitulate vascular fragility; THSD1 marks HSCs and endothelial cells

THSD1 loss-of-function has been modeled in both zebrafish and mouse. Santiago-Sim et al. (2016) reported that *"In zebrafish and mice, Thsd1 loss-of-function caused cerebral bleeding (which localized to the subarachnoid space in mice) and increased mortality"* — recapitulating the vascular-fragility phenotype [[PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/)]. Genetically engineered mouse models subsequently established a definitive role for Thsd1 in intracranial aneurysm via Thsd1/FAK signaling (reviewed in Xu 2019) [[PMID: 31055715](https://pubmed.ncbi.nlm.nih.gov/31055715/)].

The gene was originally identified (as *Tmtsp*) through a Venus knock-in reporter mouse. Takayanagi et al. (2006) *"demonstrated its specific expression in hematopoietic and endothelial cells. In lymphohematopoietic cells, Tmtsp was predominantly expressed in hematopoietic stem and progenitor cells"*, marking definitive hematopoiesis in the yolk sac and AGM region [[PMID: 16455951](https://pubmed.ncbi.nlm.nih.gov/16455951/)]. This establishes both a validated mouse reporter resource and the endothelial/hematopoietic cell-of-origin.

### Finding 5 — THSD1 is tolerant of heterozygous LOF (gnomAD pLI ≈ 0), consistent with recessive inheritance

gnomAD constraint metrics (GRCh38; THSD1 = ENSG00000136114, chr13:52,377,167–52,416,373) show THSD1 is **not haploinsufficient**: pLI = 4.0×10⁻⁹ (≈0); observed/expected LOF (oe_lof) = 0.735 (90% CI 0.559–0.979); LOF-Z = 1.53; missense-Z = 0.46. A pLI near zero means heterozygous carriers tolerate loss of one allele, which is exactly consistent with the recessive inheritance of LMPHM13 — disease requires loss of **both** alleles. Human identifiers confirmed: NCBI Gene **55901**, **HGNC:17754**, OMIM gene **616821**, UniProt **Q9NS62**, cytoband 13q14.3; mouse ortholog *Thsd1* = NCBI Gene 56229, MGI:1929096.

### Finding 6 — Protein architecture: pathogenic truncating variants remove the TSP type-1 domain, transmembrane anchor, and cytoplasmic tail

UniProt Q9NS62 defines THSD1 as an **852-aa type-I transmembrane protein**: signal peptide (1–24); extracellular domain (25–413) containing a single thrombospondin type-1 (TSP) domain at residues 340–393; transmembrane helix (414–434); and a large cytoplasmic domain (435–852), with 7 extracellular N-glycosylation sites. Reported pathogenic alleles truncate at or before these features and are predicted to abolish the TSP domain, membrane anchoring, and the cytoplasmic signaling region:

| Variant (protein / nucleotide) | Location relative to domains | Predicted effect |
|---|---|---|
| p.Glu298Ter (c.892G>T) | Before TSP domain | Loss of TSP, TM, cytoplasmic tail |
| p.Gln337Argfs*73 (c.1009delC) | At TSP domain start | Frameshift; loss of TSP + downstream |
| p.Arg388Glnfs*66 | Within TSP domain | Truncates TSP + downstream |
| c.58+2T>G | N-terminal splice site | Early truncation |
| c.1494del | Cytoplasmic region | Frameshift (ClinVar likely pathogenic) |

ClinVar for THSD1 (~60 records) is dominated by VUS (36) and likely-benign (12) entries, with one likely-pathogenic truncating variant (c.1494del) and two "pathogenic" large 13q copy-number variants. Most LMPHM13 family alleles are **private** (family-specific) and absent or under-represented in ClinVar — a recurring theme in ultra-rare recessive disease.

### Finding 7 — Single-cell expression is most enriched in lymphatic endothelial cells — a cell-of-origin link to the lymphatic phenotype

Human Protein Atlas single-cell RNA data classify THSD1 as "cell type enhanced," with the **highest expression in lymphatic endothelial cells (74.7 nCPM)**, followed by retinal ganglion cells (46.4), vascular endothelial cells (43.3), astrocytes (42.0), epididymal basal cells (39.6), fibro-adipogenic progenitors (30.7), retinal bipolar cells (27.5), and myosatellite cells (21.7). HPA RNA tissue specificity is "low tissue specificity"; subcellular location is cytosol; GTEx shows broad expression with no single dominant tissue. The lymphatic-endothelial enrichment provides a direct molecular rationale for why loss of THSD1 produces a lymphatic-dominant clinical phenotype (lymphedema, chylothorax, protein-losing enteropathy), complementing the original endothelial/HSPC expression described by Takayanagi 2006 [[PMID: 16455951](https://pubmed.ncbi.nlm.nih.gov/16455951/)].

### Finding 8 — Identifier correction: OMIM phenotype #620244 does exist

The research template listed OMIM as "not recorded," but MONDO:0859379 ("lymphatic malformation 13") cross-references (retrieved via EBI OLS4) show a **dedicated OMIM phenotype entry #620244** (exact match), plus GARD:0026725, MedGen MEDGEN:1840915, and UMLS:C5830279. Earlier case reports instead cited the older generic NIHF phenotype series OMIM 236750 (used, e.g., by Al Rawi 2021) before the specific LMPHM13 entry was established. The corrected identifier set is given in the Disease Information section below.

---

## Report by Template Section

### 1. Disease Information

LMPHM13 is a rare, Mendelian, autosomal-recessive lymphatic/vascular dysplasia. It presents prenatally most often as non-immune hydrops fetalis (serous fluid accumulation in ≥2 body cavities/interstitial spaces without red-cell alloimmunization) and, in survivors, as a multisystem disorder with persistent edema, effusions, hydrocele, hemangiomas, congenital heart defects, and protein-losing enteropathy. Information is derived from **individual patient case reports and small consanguineous-family studies** aggregated into disease-level ontology entries (MONDO, OMIM), not from population EHR cohorts.

**Key identifiers:**
- **MONDO:** 0859379
- **OMIM phenotype:** #620244 (corrected; earlier literature used generic NIHF OMIM 236750)
- **OMIM gene:** 616821 (THSD1)
- **GARD:** 0026725
- **MedGen:** 1840915 / **UMLS:** C5830279
- **HGNC:** 17754; **NCBI Gene:** 55901; **UniProt:** Q9NS62
- **ICD-10/ICD-11, MeSH, Orphanet:** No dedicated LMPHM13-specific code identified; coded under non-immune hydrops fetalis / generalized lymphatic dysplasia.

**Synonyms:** LMPHM13; THSD1-related generalized lymphatic dysplasia; THSD1-related non-immune hydrops fetalis.

### 2. Etiology

**Causal factor:** Purely genetic — biallelic loss-of-function variants in THSD1 [[PMID: 26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/)]. No environmental, infectious, or toxic cause is implicated.

**Genetic risk factors:** The principal (and sufficient) risk factor is inheritance of two LOF THSD1 alleles. **Consanguinity** is a major contributing factor — nearly all reported families are consanguineous, producing homozygous truncating alleles via identity-by-descent. A **founder mutation** in THSD1 accounted for lethality across three families in the original study [[PMID: 26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/)].

**Environmental risk / protective factors:** None established. No lifestyle, dietary, occupational, or toxic modifiers have been described. **Gene–environment interactions:** none documented; this is a monogenic disorder.

**Protective factors (genetic):** Because THSD1 is LOF-tolerant in the heterozygous state (gnomAD pLI ≈ 0, Finding 5), heterozygous carriers are unaffected — a single functional allele is protective.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Non-immune hydrops fetalis | Clinical sign | Fetal/neonatal | Core feature | HP:0001790 |
| Pleural effusion | Clinical sign | Fetal onset | 4/4 (Abdelrahman) | HP:0002202 |
| Ascites / peritoneal effusion | Clinical sign | Fetal onset | High | HP:0001541 |
| Hydrocele (males) | Physical | Congenital | All affected males | HP:0000034 |
| Hemangioma (cutaneous/midline) | Physical | Congenital | High | HP:0001028 |
| Congenital heart defect | Physical | Congenital | 3/4 (Abdelrahman) | HP:0001627 |
| Intestinal malabsorption / PLE | Lab/clinical | Infancy–childhood | Variable | HP:0002024 / HP:0002243 |
| Peripheral lymphedema | Clinical sign | Congenital–adult | Variable, persistent | HP:0001004 |
| Chylothorax | Clinical sign | Neonatal | Case reports | HP:0010310 |
| Dysmorphic features | Physical | Congenital | Variable | HP:0001999 |
| Prematurity / pulmonary hypertension | Clinical | Perinatal | Case reports | HP:0001662 / HP:0002092 |

**Severity/progression:** Highly variable — from embryonic lethality to lifelong mild edema. In many survivors hydrops/effusions **resolve with age** and growth/development are relatively normal [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/), [PMID: 37993095](https://pubmed.ncbi.nlm.nih.gov/37993095/)]. Lymphedema/PLE can be chronic and progressive, requiring surgery [[PMID: 42583604](https://pubmed.ncbi.nlm.nih.gov/42583604/)].

**Quality-of-life impact:** Not formally measured with EQ-5D/SF-36. Chronic lymphedema and PLE impose substantial burden (nutritional compromise, hypoalbuminemia, repeated interventions); perinatal cases carry mortality risk; late-presenting cases may have lifelong unexplained edema [[PMID: 42714234](https://pubmed.ncbi.nlm.nih.gov/42714234/)].

### 4. Genetic / Molecular Information

**Causal gene:** THSD1 (HGNC:17754, NCBI 55901, OMIM gene 616821), 13q14.3. **Variant types:** Predominantly truncating — nonsense, frameshift, and splice-site (see Finding 6 table). **Classification:** Family alleles are mostly private; per ACMG criteria the recurrent truncating alleles are pathogenic/likely pathogenic by PVS1 (LOF is the established mechanism). ClinVar is dominated by VUS. **Allele frequency:** Pathogenic alleles are absent/ultra-rare in gnomAD. **Origin:** Germline. **Functional consequence:** Loss of function (THSD1 is LOF-tolerant in heterozygotes; disease requires biallelic loss). **Modifier genes / epigenetics:** None established. **Chromosomal abnormalities:** Two large pathogenic 13q CNVs are recorded in ClinVar but these are not the canonical LMPHM13 mechanism.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are known. NIHF from THSD1 is monogenic; TORCH infection and chromosomal/metabolic causes must be **excluded** during diagnosis but are not causal to LMPHM13 itself [[PMID: 41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/)].

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic LOF mutation in **THSD1** → **leads to** absence/truncation of functional THSD1 protein (loss of the TSP type-1 domain, transmembrane anchor, and cytoplasmic tail). *(Demonstrated — genetics.)*
2. Loss of THSD1 at focal adhesions → **results in** diminished FAK activity. *(Demonstrated in vitro.)*
3. Reduced FAK activity → **relieves** FAK's inhibitory phosphorylation of Beclin-1. *(Demonstrated — Xu 2024.)*
4. De-repressed Beclin-1 → **promotes** formation of the Beclin-1/ATG14 autophagy-initiation complex (mTOR/AMPK-independent). *(Demonstrated.)*
5. Autophagy → **drives** turnover/disassembly of focal adhesions → **impairs** endothelial cell attachment to the basement membrane. *(Demonstrated; rescued by WT but not mutant THSD1.)*
6. Weakened endothelial/lymphatic-endothelial adhesion → **causes** vascular and lymphatic barrier failure (increased permeability, vessel fragility). *(Inferred from cellular defect + vascular-permeability link.)*
7. Barrier failure branches:
   - **Branch A (vascular/lymphatic leak):** → fluid and protein extravasation → **produces** effusions, hydrops fetalis, lymphedema, chylothorax, protein-losing enteropathy. *(Clinical correlation.)*
   - **Branch B (vessel fragility):** → **predisposes** to intracranial aneurysm/subarachnoid hemorrhage (allelic, dominantly-acting trait; modeled in mouse/zebrafish). *(Demonstrated in models.)*

**Molecular pathways:** FAK (PTK2) signaling; Beclin-1/ATG14 autophagy initiation; focal-adhesion assembly. Related vascular pathways implicated in the aneurysm literature include TGF-β and mechanotransduction [[PMID: 31055715](https://pubmed.ncbi.nlm.nih.gov/31055715/)]. **Cellular processes:** Autophagy (GO:0006914), focal adhesion assembly (GO:0048041), cell-matrix adhesion (GO:0007160), regulation of vascular permeability (GO:0043114), lymphangiogenesis (GO:0001946). **Cell types:** Lymphatic endothelial cell (CL:0002138), vascular endothelial cell (CL:0000115), hematopoietic stem cell (CL:0000037). **Subcellular:** Focal adhesion (GO:0005925); cytosol (GO:0005829); plasma membrane (THSD1 is a type-I transmembrane protein). **Protein dysfunction:** Loss of function via truncation of the TSP type-1 domain and cytoplasmic signaling region.

### 7. Anatomical Structures Affected

- **Primary organs/systems:** Lymphatic system (UBERON:0006558 lymphatic part of vasculature) and cardiovascular/vascular endothelium; serous cavities — pleural (UBERON:0002402), peritoneal (UBERON:0002358).
- **Secondary involvement:** Heart (congenital defects; UBERON:0000948), intestine (malabsorption/PLE; UBERON:0000160), scrotum/tunica vaginalis (hydrocele; UBERON:0000203), skin (hemangiomas; UBERON:0002097), lungs (pulmonary hypertension/chronic lung disease; UBERON:0002048), brain vasculature (aneurysm/subarachnoid space; UBERON:0002361).
- **Tissue/cell level:** Endothelial tissue; specifically lymphatic endothelial cells (CL:0002138) and vascular endothelial cells (CL:0000115).
- **Lateralization:** Effusions/edema are typically **bilateral/generalized**; hydrocele may be bilateral.

### 8. Temporal Development

- **Onset:** Congenital — most often prenatal (hydrops detected on fetal ultrasound, e.g., at 19 weeks' gestation) [[PMID: 41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/)]. Rare late/adult presentation of chronic edema [[PMID: 42714234](https://pubmed.ncbi.nlm.nih.gov/42714234/)].
- **Onset pattern:** Insidious/chronic antenatal fluid accumulation; acute perinatal decompensation possible.
- **Progression:** Variable. Severe end = embryonic lethality/stillbirth. Survivors frequently show **spontaneous resolution** of hydrops/effusions with age and relatively normal development [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/), [PMID: 37993095](https://pubmed.ncbi.nlm.nih.gov/37993095/)]. Lymphedema/PLE may be chronic and lifelong.
- **Critical period:** The fetal/perinatal window is the key period of vulnerability and the main opportunity for intervention (effusion drainage, respiratory support).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/)].
- **Penetrance/expressivity:** Highly **variable expressivity** (lethal ↔ mild lifelong edema), even among affected individuals; penetrance of the biallelic genotype appears high but severity is variable.
- **Consanguinity:** Central — most families are consanguineous; founder effects documented [[PMID: 26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/)].
- **Carrier frequency:** Not formally established; pathogenic alleles are ultra-rare in gnomAD. Heterozygous carriers are asymptomatic (pLI ≈ 0).
- **Epidemiology:** No prevalence/incidence estimates exist — the disorder is ultra-rare with only a few dozen reported cases worldwide.
- **Sex ratio:** No sex bias in disease (autosomal); hydrocele is, by anatomy, limited to males.
- **Geographic distribution:** Reported families are concentrated in populations with high consanguinity (Middle East/North Africa) and scattered individual reports elsewhere (e.g., Latin America; the gene was discovered in Japan-origin reporter work).

### 10. Diagnostics

- **Prenatal imaging:** Fetal ultrasound detects hydrops (effusions in ≥2 compartments), ascites, pleural effusion, hydrocele, edema.
- **Laboratory:** Hypoalbuminemia (from PLE/leak); exclude anemia/alloimmunization (to establish *non-immune* hydrops); negative TORCH study; normal karyotype/microarray to exclude chromosomal/aneuploidy causes [[PMID: 41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/)].
- **Genetic testing (confirmatory):** **Whole-exome or whole-genome sequencing** is the diagnostic modality of choice, having identified THSD1 variants in essentially all reported cases; WGS detected a deep splice variant (c.58+2T>G) in the adult case [[PMID: 42714234](https://pubmed.ncbi.nlm.nih.gov/42714234/)]. Single-gene THSD1 testing or NIHF/lymphedema gene panels are appropriate once the gene is suspected. Chromosomal microarray/karyotype serve to exclude differential diagnoses.
- **Differential diagnosis:** Other causes of NIHF — cardiac, chromosomal (e.g., Turner syndrome), metabolic/lysosomal storage, other lymphatic dysplasias (e.g., RASopathy-related, PIEZO1/CCBE1/FAT4 generalized lymphatic dysplasias), infectious (TORCH), and alloimmune hydrops [[PMID: 37993095](https://pubmed.ncbi.nlm.nih.gov/37993095/)].
- **Screening:** Cascade/carrier testing within affected families; prenatal testing in subsequent pregnancies.

### 11. Outcome / Prognosis

- **Survival/mortality:** Spans embryonic lethality to normal survival. Several reports emphasize a **favorable prognosis** in survivors once hydrops resolves [[PMID: 30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/), [PMID: 41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/)]. Prematurity complications (pulmonary hypertension, chronic lung disease) worsen perinatal prognosis [[PMID: 33569873](https://pubmed.ncbi.nlm.nih.gov/33569873/)].
- **Morbidity:** Chronic lymphedema, PLE with hypoalbuminemia/malnutrition, recurrent effusions, and surgical needs [[PMID: 42583604](https://pubmed.ncbi.nlm.nih.gov/42583604/)].
- **Prognostic factors:** Gestational age/prematurity, severity and persistence of effusions, presence of congenital heart disease, and resolution vs persistence of fluid accumulation. No molecular prognostic biomarkers are validated (though more N-terminal/complete truncations may correlate with greater severity — inferred, not proven).

### 12. Treatment

**No disease-modifying therapy exists.** Management is supportive and symptom-directed:
- **Perinatal/supportive:** Drainage of pleural/peritoneal effusions (thoracocentesis/paracentesis), respiratory support, management of pulmonary hypertension, albumin replacement, and nutritional support (NCIT: Supportive Care).
- **Nutritional:** For PLE — high-protein, medium-chain-triglyceride (MCT) diets to reduce lymphatic load (standard lymphatic-disorder management).
- **Surgical/interventional:** Lymphatic microsurgery — **peripheral lymphatic shunts/lymphovenous anastomosis** successfully managed chronic lower-limb lymphedema with PLE in a child [[PMID: 42583604](https://pubmed.ncbi.nlm.nih.gov/42583604/)]; hydrocele repair as needed; cardiac surgery for structural defects (NCIT: Surgical Procedure).
- **Pharmacogenomics / targeted / gene / cell / RNA therapies:** None reported. The FAK–Beclin-1 autophagy axis is a plausible **future** pharmacological target (e.g., autophagy modulation to stabilize focal adhesions) but is purely hypothetical at present.

### 13. Prevention

- **Primary prevention:** Not applicable beyond reproductive counseling — the disease is congenital and genetic.
- **Genetic counseling:** Central. Autosomal-recessive 25% recurrence risk for carrier couples; particularly relevant in consanguineous families. Carrier/cascade testing and prenatal diagnosis (or preimplantation genetic testing) are available once the familial variant is known.
- **Secondary prevention:** Prenatal ultrasound surveillance in at-risk pregnancies for early detection/management of hydrops.
- **Tertiary prevention:** Nutritional and surgical management to prevent PLE/lymphedema complications.

### 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Thsd1* (NCBI Gene 56229, MGI:1929096); zebrafish *thsd1* ortholog used in LOF studies. Human NCBI Gene 55901.
- **Natural disease in animals:** No naturally occurring THSD1 disease in companion animals/wildlife is documented in the reviewed literature (no OMIA entry identified here).
- **Comparative biology:** The vascular-fragility phenotype (cerebral/subarachnoid bleeding, increased mortality) is **evolutionarily conserved** across zebrafish and mouse, indicating a conserved role in vascular integrity [[PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/)].
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

### 15. Model Organisms

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| Zebrafish *thsd1* LOF | Vertebrate, in vivo | Cerebral bleeding, increased mortality | [PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/) |
| Mouse *Thsd1* LOF | Mammalian, in vivo | Subarachnoid bleeding; intracranial aneurysm (via Thsd1/FAK) | [PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/), [PMID: 31055715](https://pubmed.ncbi.nlm.nih.gov/31055715/) |
| *Tmtsp*-Venus knock-in reporter mouse | Mammalian reporter | Marks HSC/progenitor + endothelial cells; definitive hematopoiesis in yolk sac/AGM | [PMID: 16455951](https://pubmed.ncbi.nlm.nih.gov/16455951/) |
| In vitro endothelial cells | Cellular | Focal-adhesion defect; rescued by WT THSD1 | [PMID: 27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/) |

**Phenotype recapitulation:** Models reproduce the **vascular-fragility/hemorrhage** axis well (Branch B of the mechanism) but no published model has been reported to fully recapitulate the **hydrops/lymphatic-leak** axis (Branch A) — the dominant human clinical presentation. This is a notable gap. **Resources:** MGI (mouse), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
  Biallelic THSD1 LOF mutation (truncating; loses TSP domain + TM + cytoplasmic tail)
                 │
                 ▼
     Loss of THSD1 at focal adhesions
                 │
                 ▼
        ↓ FAK activity  ──────────────► ↓ inhibitory phosphorylation of Beclin-1
                 │                                   │
                 ▼                                   ▼
                                     Beclin-1 / ATG14 complex forms (mTOR/AMPK-independent)
                                                     │
                                                     ▼
                              Autophagy-mediated focal-adhesion turnover ↑
                                                     │
                                                     ▼
                   Endothelial / lymphatic-endothelial detachment from basement membrane
                                                     │
                            ┌────────────────────────┴───────────────────────┐
                            ▼                                                  ▼
          BRANCH A: Lymphatic/vascular barrier leak            BRANCH B: Vessel-wall fragility
          → effusions, hydrops fetalis, lymphedema,            → intracranial aneurysm / SAH
            chylothorax, protein-losing enteropathy              (modeled in mouse/zebrafish)
```

The unifying theme is **loss of endothelial adhesion stability**. THSD1 normally acts as a "brake" on autophagic recycling of focal adhesions via FAK-dependent suppression of Beclin-1. Its loss tips the balance toward adhesion disassembly, destabilizing both lymphatic and vascular endothelium. The single-cell enrichment of THSD1 in **lymphatic endothelial cells** (Finding 7) explains why the lymphatic branch (leak → hydrops/lymphedema/PLE) dominates the human phenotype, while the conserved vascular-fragility branch is most evident in animal models and the allelic aneurysm trait. The severity gradient — from embryonic lethality to lifelong mild edema — likely reflects a combination of allele-specific residual function, modifier background, and stochastic developmental factors, though no modifier has been mapped.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26036949](https://pubmed.ncbi.nlm.nih.gov/26036949/) | *Embryonic lethal genes by autozygosity mapping* | **Gene discovery**; THSD1 founder mutation → lethality + milder NIHF/edema; AR |
| [30055085](https://pubmed.ncbi.nlm.nih.gov/30055085/) | *Recessive truncating THSD1 variant, 4 patients* | Core phenotype description; AR cosegregation |
| [27895300](https://pubmed.ncbi.nlm.nih.gov/27895300/) | *THSD1 mutation in intracranial aneurysm/SAH* | Focal-adhesion defect in vitro; zebrafish/mouse LOF models |
| [38396816](https://pubmed.ncbi.nlm.nih.gov/38396816/) | *THSD1 suppresses autophagy via FAK–Beclin-1* | Molecular mechanism (FAK–Beclin-1–ATG14) |
| [40564011](https://pubmed.ncbi.nlm.nih.gov/40564011/) | *THSD1 multifaceted regulator (review)* | Synthesis: FA assembly, barrier function, NIHF, tumor suppression |
| [16455951](https://pubmed.ncbi.nlm.nih.gov/16455951/) | *Tmtsp marks HSC/endothelial cells* | Cell-of-origin; knock-in reporter mouse |
| [33569873](https://pubmed.ncbi.nlm.nih.gov/33569873/) | *THSD1 in extremely premature NIHF infant* | Prematurity, pulmonary hypertension, chronic lung disease |
| [42714234](https://pubmed.ncbi.nlm.nih.gov/42714234/) | *Novel THSD1 variant, chronic edema, 79-yo* | Late/adult phenotype extreme; c.58+2T>G splice variant |
| [41842780](https://pubmed.ncbi.nlm.nih.gov/41842780/) | *Novel homozygous THSD1 variant, premature NIHF* | c.1009delC:p.Gln337Argfs*73; broad perinatal phenotype |
| [37993095](https://pubmed.ncbi.nlm.nih.gov/37993095/) | *Resolving fetal hydrops* | p.Glu298Ter; recurrent NIHF; spontaneous resolution |
| [42583604](https://pubmed.ncbi.nlm.nih.gov/42583604/) | *Lymphatic shunts for PLE in THSD1 child* | Chronic lymphedema + PLE; lymphatic surgery |
| [31055715](https://pubmed.ncbi.nlm.nih.gov/31055715/) | *Intracranial aneurysms review* | Thsd1/FAK in aneurysm; mouse-model confirmation |

No reviewed paper **contradicts** the core model; the literature is consistent and cumulative, moving from gene discovery (2015) → mechanism (2016, 2024) → phenotype expansion and surgical management (2018–2026).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare, no epidemiology:** Only a few dozen cases exist; no prevalence/incidence, penetrance quantification, or genotype–phenotype statistics are possible. All human evidence is from case reports/small consanguineous families — no cohorts or trials.
2. **Lymphatic phenotype not modeled:** Animal models recapitulate vascular hemorrhage/aneurysm (Branch B) but **not** the hydrops/lymphatic-leak phenotype (Branch A) that dominates human disease — the lymphatic branch is inferred from cellular mechanism + expression, not demonstrated in a dedicated lymphatic model.
3. **Variant interpretation:** ClinVar is VUS-dominated; most LMPHM13 alleles are private and absent from population databases, limiting classification support beyond PVS1.
4. **No modifiers/epigenetics:** The basis of the dramatic severity range (lethal ↔ lifelong-mild) is unexplained; no modifier genes, epigenetic marks, or environmental interactions identified.
5. **No QoL or outcome instruments:** No standardized QoL (EQ-5D/SF-36) or natural-history data; survival statistics are anecdotal.
6. **Ontology coding incomplete:** The OMIM gap was corrected (#620244) but no dedicated ICD/Orphanet/MeSH code for LMPHM13 specifically was identified.

---

## Proposed Follow-up Experiments / Actions

1. **Lymphatic-specific model:** Generate a lymphatic-endothelial conditional *Thsd1* knockout (e.g., *Prox1-* or *Lyve1-Cre*) mouse to test whether loss directly causes lymphedema/chylous effusions/PLE — closing the Branch-A gap.
2. **Mechanism in lymphatic endothelium:** Test whether the FAK–Beclin-1–autophagy axis operates in primary human lymphatic endothelial cells, and whether autophagy inhibitors (e.g., FAK-pathway or Beclin-1 modulators) rescue focal-adhesion stability — a potential therapeutic avenue.
3. **Genotype–phenotype registry:** Establish an international THSD1/LMPHM13 registry to aggregate variants, severity, and outcomes; systematically reclassify ClinVar VUS using segregation + functional data.
4. **Functional assay for variant classification:** Develop a standardized focal-adhesion rescue assay (WT vs variant THSD1) to provide PS3-level evidence for VUS reclassification.
5. **Modifier search:** Exome/genome analysis across severity-discordant relatives to identify modifier alleles explaining the lethal-to-mild spectrum.
6. **Natural-history & QoL study:** Prospectively collect longitudinal data (effusion resolution, lymphedema, PLE, growth) with validated QoL instruments to inform counseling and prognosis.
7. **Database curation:** Propagate the corrected identifier (OMIM #620244) and the lymphatic-endothelial cell-of-origin (CL:0002138) into downstream knowledge bases.

---

*Evidence source types: human clinical (case reports/family studies), model organism (mouse/zebrafish), in vitro (endothelial cell assays), and computational (gnomAD constraint, UniProt/HPA annotation, ontology cross-references). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Lymphatic_Malformation_13-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lymphatic_Malformation_13-deep-research-openscientist_artifacts/final_report.pdf)