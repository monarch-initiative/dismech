---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T17:55:47.201255'
end_time: '2026-10-30T18:19:43.171774'
duration_seconds: 1435.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Disability X-linked Syndromic Houge Type
  mondo_id: MONDO:0030909
  category: Mendelian
  causal_genes: CNKSR2
  omim_id: OMIM:301008
  synonyms: intellectual developmental disorder, X-linked, syndromic, Houge type
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Disability_X-linked_Syndromic_Houge_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Disability_X-linked_Syndromic_Houge_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability X-linked Syndromic Houge Type
- **MONDO ID:** MONDO:0030909 (if available)
- **Causal gene(s):** CNKSR2
- **OMIM:** OMIM:301008
- **Synonyms:** intellectual developmental disorder, X-linked, syndromic, Houge type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability X-linked Syndromic Houge Type** covering all of the
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

# Intellectual Disability, X-linked, Syndromic, Houge Type (MRXSHG): A Comprehensive Disease Characterization

**Disease:** Intellectual developmental disorder, X-linked, syndromic, Houge type (MRXSHG)
**Causal gene:** **CNKSR2** (Connector enhancer of kinase suppressor of Ras 2; also known as *CNK2* / *MAGUIN*), located at Xp22.12
**MONDO:** MONDO:0030909 · **OMIM:** 301008 · **Category:** Mendelian, X-linked

---

## Summary

**Intellectual disability, X-linked, syndromic, Houge type (MRXSHG)** is an ultra-rare, male-predominant X-linked neurodevelopmental disorder caused by **loss-of-function variants in the *CNKSR2* gene** at Xp22.12. *CNKSR2* encodes **CNKSR2/MAGUIN (CNK2)**, a multidomain postsynaptic-density scaffold protein that physically links the PSD-95/S-SCAM synaptic scaffold machinery to Raf-1/MAPK and Rac/Cdc42 small-GTPase signaling. The disorder was first delineated as a distinct entity by Vaags and colleagues in 2014, who described eight hemizygous males with the characteristic triad of intellectual disability, early-childhood epilepsy, and abrupt, lifelong loss of language [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/). The name "Houge type" honors Gunnar Houge, a co-author of that defining series; note that the superficially similar alias "KSR2" refers to a different (metabolic) gene — the disease gene here is **CNKSR2**.

Clinically, MRXSHG falls within the **epilepsy–aphasia spectrum**. Affected individuals typically present in early childhood (often before age 5) with seizures and an EEG pattern of **continuous spike-and-wave during slow-wave sleep (CSWS / electrical status epilepticus in sleep, ESES)**. This epileptic encephalopathy is accompanied — and frequently followed — by developmental regression, particularly a striking and permanent loss of expressive language, together with attention-deficit/hyperactivity, and variable autistic features. The epileptiform activity is age-dependent and tends to remit over time, but the cognitive and language deficits persist as a static (non-degenerative) disability throughout life; the oldest reported patient was 62 years old, indicating normal-range survival.

Mechanistically, loss of CNKSR2 disrupts dendritic-spine morphogenesis and impairs the synaptic localization of PSD-95 and surface accumulation of AMPA receptors in hippocampal neurons, producing abnormal excitatory synaptic transmission and network hyperexcitability. A *Cnksr2*-knockout mouse recapitulates the increased neural activity and behavioral phenotypes of the human epilepsy–aphasia syndrome, supporting a conserved, causal role for CNKSR2 loss. There is **no curative or gene-targeted therapy**; management is symptomatic — antiseizure medications, benzodiazepines/corticosteroids/ethosuximide/sulthiame for the ESES component, speech and behavioral therapy, and genetic counseling. Prevention is limited to genetic counseling, carrier testing of at-risk females, and prenatal/preimplantation genetic diagnosis for known familial variants.

---

## 1. Disease Information

MRXSHG is a **monogenic, X-linked syndromic form of intellectual disability** characterized by the combination of intellectual disability, attention problems, early-childhood epilepsy with CSWS, and abrupt, lifelong language loss. It sits within the clinical continuum of the **epilepsy–aphasia spectrum / developmental and epileptic encephalopathy with spike-wave activation in sleep (DEE-SWAS)**.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030909 |
| OMIM | 301008 |
| Gene | CNKSR2 (HGNC), Xp22.12 |
| Disease category | Mendelian, X-linked recessive (with female expression under skewed XCI) |

**Synonyms / alternative names:** intellectual developmental disorder, X-linked, syndromic, Houge type; Houge type of X-linked syndromic mental retardation; MRXSHG; CNKSR2-related developmental and epileptic encephalopathy with spike-wave activation in sleep.

**Source of information:** The knowledge base for this disorder is derived almost entirely from **aggregated case reports and small case series** of individual patients (clinical, genetic, and EEG data) plus mechanistic studies in cell and mouse models — not from population-level EHR or registry resources. The largest synthesis aggregated 49 patients [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/).

---

## 2. Etiology

**Primary cause — genetic.** MRXSHG is caused by **hemizygous (males) or heterozygous (females) loss-of-function variants in *CNKSR2***. The disorder is purely genetic; **no environmental, infectious, toxic, or lifestyle cause has been identified**, and none is implicated as a trigger.

**Genetic risk factors.** The sole established risk factor is possession of a pathogenic *CNKSR2* variant. Pathogenic alleles are predominantly loss-of-function: nonsense, frameshift, and canonical splice-site variants, with a minority of missense variants and whole- or partial-gene Xp22.12 deletions. In one series, 14 distinct variants comprised five nonsense, three frameshift, two splice, and four missense variants, of which 13 were novel [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/). Many arise *de novo*. A **recurrent CpG mutational hotspot** underlies recurrent nonsense alleles such as p.Arg729* and p.Arg712*, described as "a CGA>TGA transition at a CpG dinucleotide consistent with a mutational hotspot" [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/).

**Sex as a risk factor.** Being male is a major determinant of risk and severity, reflecting X-linkage (see Section 9). The observed male-to-female ratio is **11.2:1** [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/).

**Modifier of female expression — X-chromosome inactivation.** In carrier females, the degree of **skewed X-inactivation** modifies whether and how severely they are affected; one symptomatic female showed marked XCI skewing of 85:15 [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/).

**Protective factors / gene–environment interactions.** No genetic protective modifiers, protective alleles, dietary/lifestyle protective factors, or gene–environment interactions have been reported for this disorder. In females, balanced (non-skewed) X-inactivation favoring the wild-type allele is the closest analogue to a protective modifier.

---

## 3. Phenotypes

Phenotype frequencies are best quantified from the 49-patient synthesis [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/), supplemented by the founding cohort [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/).

| Phenotype | Frequency | HPO suggestion | Type |
|---|---|---|---|
| Global developmental delay / intellectual disability | 100% (49/49) | HP:0001263 / HP:0001249 | Clinical / cognitive |
| Epilepsy | 91.8% (45/49) | HP:0001250 | Clinical sign |
| Attention-deficit/hyperactivity (ADHD) | 77.6% (38/49) | HP:0007018 | Behavioral |
| Absence of speech / language loss | 75.5% (37/49) | HP:0001344 | Clinical |
| ESES / CSWS on sleep EEG | 44.4% (16/36 with sleep EEG) | HP:0002528 (related) | Laboratory (EEG) |
| Sleep disturbances | 28.6% (14/49) | HP:0002360 | Clinical |
| Feeding difficulties | 12.2% | HP:0011968 | Clinical |
| Autism spectrum disorder | 10.2% | HP:0000717 | Behavioral |
| Abnormal muscle tone | 6.1% | HP:0003808 | Clinical sign |
| Microcephaly | 6.1% | HP:0000252 | Physical |
| Facial dysmorphism | 4.1% | HP:0001999 | Physical |

The founding cohort distilled the signature as "intellectual disability, attention problems, and abrupt lifelong language loss following a brief early childhood epilepsy with continuous spike-waves in sleep" [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/).

**Additional / rarer features** reported in individual cases include excessive appetite, elongated face, reduced body weight, and digital (finger) anomalies [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/), [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/), and delayed bone age / temporal-lobe underdevelopment [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/).

**Phenotype characteristics.**
- **Age of onset:** Epilepsy typically in early childhood, often **before age 5** [PMID: 38443014](https://pubmed.ncbi.nlm.nih.gov/38443014/). Developmental delay is usually apparent from infancy/toddlerhood.
- **Severity:** Variable but generally moderate-to-severe for cognition and language; seizures range from controllable to refractory.
- **Progression:** The characteristic course is **regression** (notably abrupt language loss) during the active epilepsy/ESES window, after which cognition is **static** (non-degenerative).

**Quality-of-life impact.** The combination of permanent language loss, intellectual disability, ADHD, and (in many) refractory epilepsy produces substantial, lifelong impairment of communication, learning, independence, and daily functioning. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CNKSR2* (Xp22.12; OMIM 301008). The gene is **highly loss-of-function intolerant** in gnomAD, consistent with its essential synaptic role.

**Pathogenic variants.** The variant spectrum is dominated by **loss-of-function alleles** — nonsense, frameshift, and splice-site — plus a minority of missense variants and structural Xp22.12 deletions. Representative, literature-confirmed variants include:

| Variant (cDNA / protein) | Type | Note | Source |
|---|---|---|---|
| c.2134C>T, p.(Arg712*) | Nonsense | CpG hotspot; symptomatic female w/ skewed XCI | [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/) |
| p.Arg729* | Nonsense | Recurrent CpG hotspot (CGA>TGA); severe male | [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/) |
| c.64+1G>A | Splice | Mildly affected female | [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/) |
| c.625C>T, p.(Gln209*) | Nonsense | Novel; VPA-responsive seizures | [PMID: 34114993](https://pubmed.ncbi.nlm.nih.gov/34114993/) |
| c.1102G>T, p.(Gly368*) | Nonsense | Novel; Chinese MRXSHG boy | [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/) |
| c.1658-3_1676del | Splice (aberrant spliceosome) | Minigene-confirmed | [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/) |
| c.2489dup, p.(Arg831Glufs*21) | Frameshift insertion | First frameshift insertion reported | [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/) |

**Variant classification.** Reported pathogenic variants are classified **pathogenic / likely pathogenic** under ACMG/AMP guidance; in one series all 14 variants met pathogenic/likely-pathogenic criteria, "of which 13 are novel" [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/). At least 34 distinct variants had been catalogued by 2025 [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/).

**Allele frequency.** Pathogenic alleles are absent or ultra-rare in population databases (gnomAD); *CNKSR2* is LoF-intolerant.

**Origin.** **Germline**; frequently *de novo*. No somatic disease role.

**Functional consequence.** **Loss of function** (haploinsufficiency in males via a single X; dosage/XCI-dependent in females). Missense/frameshift variants are inferred to destabilize the protein — molecular-dynamics simulation of a frameshift mutant showed increased rigidity and altered structural stability versus wild type [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/).

**Modifier genes / epigenetics.** No classical modifier genes are established. The principal epigenetic modifier of expression is **X-chromosome inactivation** in carrier females [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/). No disease-specific DNA-methylation episignature has been reported.

**Chromosomal abnormalities.** Contiguous **Xp22.12 deletions** encompassing *CNKSR2* are detectable by chromosomal microarray and are a recognized cause.

---

## 5. Environmental Information

There are **no established environmental, lifestyle, or infectious contributors** to MRXSHG. The disorder is monogenic. Environmental factors (toxins, radiation, pollution, occupational exposure), lifestyle factors (smoking, diet, alcohol), and infectious agents are **not applicable** as causes. (Standard seizure-provoking factors — sleep deprivation, intercurrent illness, missed medication — may exacerbate the epilepsy component non-specifically, as in any epilepsy.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **loss-of-function variant in *CNKSR2*** (nonsense/frameshift/splice/missense or Xp22.12 deletion) **leads to** absent or non-functional CNKSR2/MAGUIN protein in neurons (haploinsufficiency in hemizygous males).
2. Loss of CNKSR2 **removes a postsynaptic-density scaffold** that normally links PSD-95/S-SCAM to Raf-1/MAPK and to Rac/Cdc42 small-GTPase signaling [PMID: 10753660](https://pubmed.ncbi.nlm.nih.gov/10753660/), [PMID: 35053419](https://pubmed.ncbi.nlm.nih.gov/35053419/).
3. This **results in** dysregulated **Rac GTPase cycling** at dendritic spines (loss of the CNK2–Vilse/ARHGAP39 interaction that balances RacGDP/GTP) **and impaired PSD-95 synaptic targeting** [PMID: 24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/), [PMID: 36803960](https://pubmed.ncbi.nlm.nih.gov/36803960/).
4. Which **leads to** defective **dendritic-spine morphogenesis** and **reduced PSD size**, plus impaired hippocampal development (neuronal proliferation, migration, synaptogenesis) [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/).
5. Which **results in** reduced **AMPA-receptor surface accumulation** and altered postsynaptic glutamatergic response [PMID: 36803960](https://pubmed.ncbi.nlm.nih.gov/36803960/).
6. The net synaptic/network effect **leads to** **increased neural activity / network hyperexcitability** (demonstrated in the *Cnksr2*-null mouse) [PMID: 34580165](https://pubmed.ncbi.nlm.nih.gov/34580165/).
7. Which **manifests clinically** as early-childhood **epilepsy with CSWS/ESES**, and — via disruption of language-network development during a critical period (inferred) — **abrupt, lifelong language loss**, together with **intellectual disability and ADHD** [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/).

> *Branch point:* In carrier **females**, skewed X-inactivation favoring the mutant allele **leads to** a symptomatic phenotype, whereas balanced/favorable XCI leaves females asymptomatic or mildly affected [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/), [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/).

### Detail by category

**Molecular pathways.** CNKSR2/MAGUIN is the mammalian homologue of *Drosophila* CNK, a Raf-interacting scaffold; MAGUIN-1 binds the kinase domain of **Raf-1**, and "MAGUIN-1 may link Raf-1 to components of synapses assembled by PSD-95/SAP90 and S-SCAM," connecting Raf-1 to the **RAF–MEK–ERK (MAPK)** cascade at the synapse [PMID: 10753660](https://pubmed.ncbi.nlm.nih.gov/10753660/). CNKSR2 "interacts with different molecules, including RAF1, ARHGAP39, and CYTH2, and regulates the Mitogen-Activated Protein Kinase (MAPK) cascade and small GTPase signaling" [PMID: 35053419](https://pubmed.ncbi.nlm.nih.gov/35053419/). It also coordinates **Rac/Cdc42** signaling (Rac1, α/β-PIX, GIT1/2, PAK3/4, cytohesins) [PMID: 24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/). *(GO:0000165 MAPK cascade; GO:0007264 small GTPase mediated signal transduction.)*

**Cellular processes.** Dendritic-spine morphogenesis (GO:0060997), postsynaptic density assembly/organization, AMPA-receptor clustering/trafficking (GO:0098978 glutamatergic synapse), regulation of excitatory postsynaptic potential, and hippocampal neuron development. CNK2 is "a spatial modulator of Rac cycling during spine morphogenesis… the interaction with Vilse is critical for maintaining RacGDP/GTP levels at a balance required for spine formation" [PMID: 24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/).

**Protein dysfunction.** Truncating variants produce **loss of function** via absent protein or nonsense-mediated decay; missense/frameshift variants alter structural stability (molecular-dynamics evidence of increased rigidity) [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/).

**Biochemical abnormalities.** "Genetic ablation of MAGUIN impaired PSD-95 localization and α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic (AMPA) receptor surface accumulation in cultured hippocampal neurons," reducing the glutamatergic postsynaptic response [PMID: 36803960](https://pubmed.ncbi.nlm.nih.gov/36803960/); imbalanced RacGDP/GTP cycling [PMID: 24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/).

**Metabolic / immune / infectious involvement.** None established; this is a synaptic-scaffold disorder without a primary metabolic, immune, or inflammatory component.

**Cell types & subcellular localization.** Primarily **excitatory (glutamatergic) neurons** (CL:0000679 glutamatergic neuron; CL:0000617 pyramidal neuron), with CNKSR2 enriched in **dendrites and dendritic spines / postsynaptic density** (GO:0014069 postsynaptic density; GO:0043197 dendritic spine; GO:0098978 glutamatergic synapse). Membrane/synaptic localization depends on the pleckstrin-homology (PH) domain and is NMDA-receptor-independent [PMID: 12028359](https://pubmed.ncbi.nlm.nih.gov/12028359/).

### Molecular architecture of CNKSR2/MAGUIN

CNKSR2/MAGUIN is a multidomain scaffold containing **SAM, CRIC, PDZ, and PH domains** and a C-terminal PDZ-binding motif [PMID: 35053419](https://pubmed.ncbi.nlm.nih.gov/35053419/). MAGUIN-1 "is localized at the plasma membrane via the plekstrin homology domain and the C-terminal region and interacts with PSD-95/SAP90 and S-SCAM via a C-terminal PDZ domain-binding motif" [PMID: 10207009](https://pubmed.ncbi.nlm.nih.gov/10207009/). A short isoform, MAGUIN-2, lacks the PDZ-binding motif and does not bind PSD-95/S-SCAM, yet still localizes to synapses via the PH domain; "the synaptic targeting of MAGUIN does not require N-methyl-d-aspartate (NMDA) receptor activity" [PMID: 12028359](https://pubmed.ncbi.nlm.nih.gov/12028359/).

```
 CNKSR2 LoF variant (Xp22.12)
        │
        ▼
 Absent/nonfunctional CNKSR2/MAGUIN scaffold
        │
   ┌────┴─────────────────────────┐
   ▼                              ▼
 Impaired PSD-95 / S-SCAM     Dysregulated Rac/Cdc42
 targeting; ↓AMPAR surface    cycling (loss of Vilse
 (↓glutamatergic response)    interaction) + ↓Raf-1/MAPK
   └────────────┬────────────────┘
                ▼
   Defective dendritic-spine morphogenesis,
   ↓PSD size, impaired hippocampal development
                ▼
   Network hyperexcitability (mouse-validated)
                ▼
   Epilepsy + CSWS/ESES → lifelong language loss,
   intellectual disability, ADHD
```

---

## 7. Anatomical Structures Affected

**Organ level.** The **brain** is the primary and essentially sole affected organ (nervous system; UBERON:0000955 brain). The principal structures implicated are the **hippocampus** and, in some patients, the **basal ganglia**.

- CNKSR2 is "predominantly expressed in dendrites… vital for dendritic spine morphogenesis in hippocampal neurons," and its loss-of-function variants "result in reduced PSD size and impaired hippocampal development" [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/), with hippocampal atrophy reported on imaging (UBERON:0002421 hippocampal formation).
- A distinct neuroimaging phenotype showed **basal ganglia** involvement: "Brain MRI revealed involvement of the basal ganglia, predominantly the neostriatum, and along with the subependymal aspects with focal cavitations involving, especially the bilateral caudate heads," with relative sparing of globus pallidi and posterior putamina [PMID: 37929438](https://pubmed.ncbi.nlm.nih.gov/37929438/) (UBERON:0002435 striatum; UBERON:0001873 caudate nucleus).
- Temporal-lobe findings (underdeveloped right temporal lobe, widened fissure) were noted in one case [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/) (UBERON:0001871 temporal lobe).
- **Many patients have normal brain MRI**; neuroimaging findings are variable and not required for diagnosis.

**Tissue / cell level.** Nervous tissue; **excitatory glutamatergic/pyramidal neurons** (CL:0000679; CL:0000617), with pathology centered on **dendrites and dendritic spines**.

**Subcellular level.** **Postsynaptic density** and **dendritic spine** (GO:0014069; GO:0043197); plasma membrane/synaptic membrane localization via the PH domain.

**Lateralization.** Predominantly **bilateral** functional involvement (generalized/bisynchronous epileptiform activity); some structural findings reported as bilateral (caudate heads) or asymmetric (right temporal lobe) in individual cases.

---

## 8. Temporal Development

- **Onset:** Congenital/early neurodevelopmental background with **epilepsy onset in early childhood, often before age 5** — "CNKSR2 related D/EE SWAS may be early onset and occur before the age of 5 years in some" [PMID: 38443014](https://pubmed.ncbi.nlm.nih.gov/38443014/). Onset of seizures may be acute/subacute; developmental delay is insidious from infancy.
- **Progression / course:** A **regressive phase** coincides with the active epilepsy/ESES window — "abrupt lifelong language loss following a brief early childhood epilepsy with continuous spike-waves in sleep" [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/). The CSWS/ESES epileptiform activity is **age-dependent and tends to remit** over years, but the **cognitive and language deficits are static and permanent** (non-degenerative).
- **Disease duration:** **Chronic, lifelong.** The oldest reported patient was 62 years, indicating normal-range survival [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/).
- **Critical period:** The ESES-active window of early-to-mid childhood is a **critical period** for both injury (language-network disruption) and potential intervention (aggressive seizure/ESES control to protect cognition).

---

## 9. Inheritance and Population

**Epidemiology.** MRXSHG is **ultra-rare**, with roughly **50 patients reported worldwide** (one synthesis aggregated 49 [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/); an earlier report noted only ~10 cases [PMID: 37929438](https://pubmed.ncbi.nlm.nih.gov/37929438/)). **No population prevalence or incidence has been established.**

**Inheritance.** **X-linked**, recessive in males (hemizygous). "Hemizygous males are typically severely affected, whereas symptomatic females remain rare and incompletely characterized" [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/).

**Penetrance / expressivity.** Essentially complete penetrance in hemizygous males; **variable expressivity**. In carrier females, expression depends on **X-chromosome inactivation**: a symptomatic female with p.(Arg712*) showed "X-chromosome inactivation analysis of her white blood cell DNA showed marked skewing (85:15)" [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/).

**De novo origin / mutational hotspot.** Many variants are *de novo* (13/14 novel in one series [PMID: 39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/)); a **recurrent CpG hotspot** ("a CGA>TGA transition at a CpG dinucleotide consistent with a mutational hotspot") produces recurrent nonsense alleles (p.Arg729*, p.Arg712*) [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/).

**Sex ratio.** Male-predominant, **11.2:1** male:female [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/).

**Founder effects / consanguinity / anticipation / germline mosaicism.** No founder effect, consanguinity requirement (X-linked, not autosomal recessive), genetic anticipation (not a repeat-expansion disorder), or confirmed germline mosaicism has been established; carrier frequency is not defined given the rarity and LoF-intolerance of the gene.

**Geographic / ethnic distribution.** Cases are reported globally (including multiple Chinese families [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/), [PMID: 34114993](https://pubmed.ncbi.nlm.nih.gov/34114993/)); no ethnic or geographic clustering is established.

---

## 10. Diagnostics

**Electrophysiology (central to diagnosis).** Overnight/sleep **EEG** demonstrating **continuous spike-and-wave during slow-wave sleep (CSWS / ESES)**, typically with a high spike-wave index, is the hallmark electrographic finding. "Early surveillance EEG may aid in diagnosis" [PMID: 38443014](https://pubmed.ncbi.nlm.nih.gov/38443014/). The clinical picture may also include atypical absence status epilepticus, within which *CNKSR2* is one of seven recognized monogenic causes (UBE3A, CNKSR2, TRPM3, KCNH2, NEXMIF, SYNGAP1, GABRB1) [PMID: 42112912](https://pubmed.ncbi.nlm.nih.gov/42112912/).

**Genetic testing (confirmatory).**
- **Whole-exome or whole-genome sequencing** with parental segregation is the primary route to molecular diagnosis [PMID: 42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/), [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/).
- **Single-gene / panel testing** of *CNKSR2* (epilepsy/ID/epilepsy-aphasia panels) is appropriate when the phenotype is recognized.
- **Chromosomal microarray (CMA)** detects contiguous **Xp22.12 deletions** involving *CNKSR2*.
- Supportive functional assays: minigene splicing for splice variants [PMID: 39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/); XCI assays in females [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/).
- Mitochondrial DNA testing, karyotyping-only, FISH, and repeat-expansion testing are **not primary** modalities for this nuclear, non-repeat X-linked gene.

**Neuroimaging.** Brain **MRI** is often normal but may show hippocampal atrophy, basal ganglia/caudate changes, or temporal-lobe abnormalities (see Section 7); imaging is supportive, not diagnostic.

**Clinical criteria / differential diagnosis.** There are no formal consensus diagnostic criteria; diagnosis rests on the **clinical triad + CSWS/ESES EEG + pathogenic *CNKSR2* variant**. Differential diagnoses include other epilepsy–aphasia spectrum / DEE-SWAS disorders and genetic causes of CSWS/ESES — e.g., **GRIN2A**-related epilepsy-aphasia, Landau–Kleffner syndrome, and other monogenic/chromosomal causes (UBE3A/Angelman, SYNGAP1, NEXMIF, GABRB1, KCNH2, TRPM3, ring chromosome 20) [PMID: 42112912](https://pubmed.ncbi.nlm.nih.gov/42112912/).

**Omics / biomarkers.** No validated blood/CSF biomarker, metabolomic, proteomic, or methylation-episignature diagnostic exists; diagnosis is genetic + electroclinical.

---

## 11. Outcome / Prognosis

**Survival.** Life expectancy appears **normal-range**; the oldest reported patient was 62 years [PMID: 25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/). No disease-specific mortality rate is established. The disorder is not reported as directly life-limiting, though refractory epilepsy carries generic seizure-related risks.

**Morbidity / disability.** Morbidity is **high and lifelong**, dominated by intellectual disability (100%), permanent language loss (~75%), ADHD (~78%), and epilepsy (~92%, refractory in ~47%) [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/). These produce major, persistent impairment of communication, learning, and independence.

**Disease course.** After the active ESES window, cognition is **static** (non-degenerative); seizures often improve with age but language deficits generally do not recover.

**Prognostic factors.** Seizure tractability (controllable vs refractory) and the timing/aggressiveness of ESES control are the main modifiable prognostic variables; in females, XCI pattern predicts severity. **No validated prognostic biomarker** exists.

---

## 12. Treatment

There is **no curative or gene-targeted therapy**. Management is **symptomatic and supportive**, centered on seizure/ESES control, developmental support, and behavioral management.

**Pharmacotherapy — antiseizure medications (NCIT: Anticonvulsant Agent).**

| Drug | Role | Evidence |
|---|---|---|
| Valproate (valproic acid) | First-line ASM; VPA stopped seizures in a case | [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/), [PMID: 34114993](https://pubmed.ncbi.nlm.nih.gov/34114993/) |
| Carbamazepine, Lamotrigine | ASMs; part of the 41.2% achieving control | [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/) |
| Ethosuximide + Sulthiame | Improved a female with ESES/regression | [PMID: 40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/) |
| High-dose diazepam | For DEE-SWAS / ESES EEG improvement | [PMID: 40095560](https://pubmed.ncbi.nlm.nih.gov/40095560/) |
| High-dose IV corticosteroid (methylprednisolone) | For refractory CSWS/ESES when ASMs fail | [PMID: 15607609](https://pubmed.ncbi.nlm.nih.gov/15607609/) |

Quantitatively, "14 (41.2%) achieved seizure control with valproate, carbamazepine, or lamotrigine; 16 (47.1%) had refractory epilepsy" [PMID: 42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/). For the ESES component, "an add-on high-dose intravenous corticosteroid seems to be effective in the treatment of patients with electrical status epilepticus during slow-wave sleep syndrome, especially when antiepileptic drugs fail" [PMID: 15607609](https://pubmed.ncbi.nlm.nih.gov/15607609/).

**Supportive / rehabilitative.** Speech and language therapy, special education, occupational therapy, and behavioral management for ADHD/ASD features (NCIT: Rehabilitation Therapy; Speech Therapy; Behavioral Therapy).

**Advanced / experimental therapeutics.** No gene therapy, RNA-based therapy, cell therapy, targeted therapy, or immunotherapy exists or is in trials for MRXSHG. No pharmacogenomic guidance is specific to this disorder.

**Treatment strategy.** Early recognition of the CSWS/ESES window and **aggressive control of epileptiform activity** (ASMs → benzodiazepines/corticosteroids/sulthiame/ethosuximide for refractory ESES) is the rationale for attempting to preserve cognition during the critical window, combined with lifelong developmental/educational support.

---

## 13. Prevention

**Primary prevention.** None possible — the disorder is a *de novo* or inherited monogenic condition with no environmental cause; no vaccine or risk-factor modification applies.

**Secondary prevention.** Early **sleep EEG surveillance** to detect CSWS/ESES, enabling prompt treatment during the critical window to mitigate cognitive/language regression [PMID: 38443014](https://pubmed.ncbi.nlm.nih.gov/38443014/).

**Tertiary prevention.** Optimized seizure management, developmental/behavioral therapy, and support to limit disability and complications.

**Genetic prevention / counseling.** The mainstay of prevention is **genetic counseling**: carrier testing of at-risk females, recurrence-risk assessment (including recognition of the CpG hotspot and *de novo* risk), and **prenatal or preimplantation genetic diagnosis** for known familial variants. Early detection of pathogenic variants "has the potential to avert the birth of another affected individual in the family" [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/). Immunization and public-health/environmental interventions are not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / gene orthology.** The disease mechanism is conserved; *CNKSR2* has a mouse ortholog **Cnksr2** (*Mus musculus*, NCBI Taxon 10090) and an invertebrate counterpart — *Drosophila* **CNK**, the founding Raf-interacting scaffold [PMID: 10753660](https://pubmed.ncbi.nlm.nih.gov/10753660/).
- **Natural disease in other species.** **No naturally occurring CNKSR2 disorder in companion animals or wildlife** has been reported (no OMIA entry identified). Veterinary/zoonotic relevance: **not applicable** — this is not a transmissible or infectious disease.
- **Evolutionary conservation.** The scaffold's role in linking Raf-1/MAPK and Rac signaling at synapses is conserved from *Drosophila* CNK to mammalian MAGUIN/CNKSR2, underpinning the validity of cross-species models.

---

## 15. Model Organisms

**Mouse (primary model).** The **_Cnksr2_-knockout mouse** is the key disease model: "Cnksr2 Loss in Mice Leads to Increased Neural Activity and Behavioral Phenotypes of Epilepsy-Aphasia Syndrome" [PMID: 34580165](https://pubmed.ncbi.nlm.nih.gov/34580165/). It recapitulates **network hyperexcitability** and EAS-spectrum behaviors, validating causality and conserved mechanism (resource: MGI).

**Cellular / in vitro models.** Primary **hippocampal neuron cultures** have been used to demonstrate that genetic ablation of MAGUIN/Cnksr2 "impaired PSD-95 localization and AMPA receptor surface accumulation" and reduced glutamatergic response [PMID: 36803960](https://pubmed.ncbi.nlm.nih.gov/36803960/), and that CNK2 acts as "a spatial modulator of Rac cycling during spine morphogenesis" [PMID: 24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/). **In silico / molecular-dynamics** simulations have modeled the structural impact of specific variants [PMID: 41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/).

**Invertebrate.** *Drosophila* CNK provides the evolutionary and mechanistic antecedent (Raf interaction, eye development) [PMID: 10753660](https://pubmed.ncbi.nlm.nih.gov/10753660/).

**Phenotype recapitulation & limitations.** The mouse model reproduces the **electrophysiological hyperexcitability** and behavioral correlates of EAS. Limitations include the difficulty of modeling the human-specific **language-loss** phenotype and the age-dependent CSWS/ESES EEG signature, and the limited availability of conditional/humanized or iPSC-derived human-neuron/organoid models in the published literature.

---

## Mechanistic Model / Interpretation

MRXSHG is fundamentally a **synaptopathy**. CNKSR2/MAGUIN sits at a hub where three signaling systems converge at the excitatory postsynaptic density: the **PSD-95/S-SCAM scaffold** (via its PDZ-binding motif), **Raf-1/MAPK** (via Raf-1 kinase-domain binding), and **Rac/Cdc42** GTPase cycling (via Vilse/ARHGAP39 and PIX/GIT/PAK partners). When CNKSR2 is lost, each arm is perturbed: PSD-95 and AMPA receptors are mislocalized (weakening and destabilizing excitatory synapses), Rac cycling at spines becomes imbalanced (impairing spine morphogenesis), and hippocampal development is globally compromised. The emergent, system-level consequence is a **hyperexcitable, abnormally wired cortical–hippocampal network**, validated independently in the knockout mouse.

This provides a coherent causal line from genotype to clinic: molecular scaffold loss → synaptic/structural deficits → network hyperexcitability → **early-childhood epilepsy with CSWS/ESES** during a developmental critical period → **permanent language loss and intellectual disability**. The static nature of the cognitive deficit after the epilepsy window, together with the therapeutic rationale for aggressively suppressing ESES, follows naturally from this model. The X-linkage and the XCI-dependent female phenotype are explained by gene dosage on the single (male) or variably-inactivated (female) X.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [25223753](https://pubmed.ncbi.nlm.nih.gov/25223753/) | *Absent CNKSR2 causes seizures and intellectual, attention, and language deficits* | Founding clinical delineation; defines the core triad and lifelong course |
| [42244324](https://pubmed.ncbi.nlm.nih.gov/42244324/) | 49-patient MRXSHG synthesis | Phenotype frequencies, 11.2:1 sex ratio, treatment-response rates |
| [35053419](https://pubmed.ncbi.nlm.nih.gov/35053419/) | *Functions of CNKSR2 and its association with NDDs* | Domain architecture; MAPK/small-GTPase scaffold identity |
| [24656827](https://pubmed.ncbi.nlm.nih.gov/24656827/) | *CNK2 scaffold interacts with Vilse…* | Rac-cycling mechanism in spine morphogenesis |
| [36803960](https://pubmed.ncbi.nlm.nih.gov/36803960/) | *s-Afadin binds MAGUIN/Cnksr2…* | PSD-95/AMPAR mislocalization on CNKSR2 loss |
| [39707601](https://pubmed.ncbi.nlm.nih.gov/39707601/) | *Novel digital anomalies, hippocampal atrophy, mutations…* | Variant spectrum; hippocampal/dendritic-spine role |
| [34580165](https://pubmed.ncbi.nlm.nih.gov/34580165/) | *Cnksr2 Loss in Mice…* | Mouse model: hyperexcitability + EAS behaviors |
| [40873128](https://pubmed.ncbi.nlm.nih.gov/40873128/) | Female DEE-SWAS + strong XCI | XCI skewing explains symptomatic females; ethosuximide/sulthiame response |
| [42541982](https://pubmed.ncbi.nlm.nih.gov/42541982/) | Splice & recurrent p.Arg729* variants | CpG hotspot; sex-dependent expression |
| [10207009](https://pubmed.ncbi.nlm.nih.gov/10207009/) / [10753660](https://pubmed.ncbi.nlm.nih.gov/10753660/) / [12028359](https://pubmed.ncbi.nlm.nih.gov/12028359/) | MAGUIN biochemistry | PSD-95/S-SCAM & Raf-1 binding; PH-domain localization |
| [37929438](https://pubmed.ncbi.nlm.nih.gov/37929438/) | Novel neuroimaging phenotype | Basal ganglia/caudate involvement |
| [38443014](https://pubmed.ncbi.nlm.nih.gov/38443014/) | Two CNKSR2 DEE-SWAS cases + review | Early (<5 y) onset; EEG surveillance value |
| [15607609](https://pubmed.ncbi.nlm.nih.gov/15607609/) / [40095560](https://pubmed.ncbi.nlm.nih.gov/40095560/) | Corticosteroid / high-dose diazepam for ESES | ESES-directed therapy |
| [34114993](https://pubmed.ncbi.nlm.nih.gov/34114993/) / [39920708](https://pubmed.ncbi.nlm.nih.gov/39920708/) / [41946974](https://pubmed.ncbi.nlm.nih.gov/41946974/) | Case reports | Variant expansion; VPA response; genetic-counseling value |
| [42112912](https://pubmed.ncbi.nlm.nih.gov/42112912/) | AASE genetic landscape review | Differential diagnosis context |

No paper in the evidence base contradicted the central model; the literature is convergent across human clinical, mouse, and in-vitro sources.

---

## Limitations and Knowledge Gaps

- **Small N / ascertainment bias.** All clinical knowledge derives from ~50 reported patients, mostly case reports; phenotype frequencies and the 11:1 sex ratio are susceptible to ascertainment and publication bias.
- **No population epidemiology.** Prevalence, incidence, and carrier frequency are unknown.
- **No validated biomarker or episignature**, and no formal diagnostic criteria.
- **Genotype–phenotype correlation is immature** — the functional difference between truncating, missense, and deletion alleles, and the quantitative XCI threshold for female expression, are not well defined.
- **Model gaps.** The human-specific language phenotype and age-dependent ESES EEG are not fully captured; conditional, humanized, or iPSC-neuron/organoid models are underdeveloped in the literature.
- **No disease-modifying therapy** and no trials targeting CNKSR2 biology; QoL and long-term natural-history data are lacking.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to define natural history, phenotype frequencies with confidence intervals, seizure/ESES trajectories, and long-term outcomes.
2. **Systematic genotype–phenotype and XCI study** correlating variant class and quantitative X-inactivation ratios with severity in males and carrier females.
3. **iPSC-derived neuron and cerebral-organoid models** from patient variants to test synaptic (AMPAR trafficking, spine density) and network (multi-electrode-array hyperexcitability) phenotypes and to screen candidate ASMs/ESES therapies.
4. **Prospective ESES-intervention trial** testing whether early, aggressive suppression of CSWS/ESES (benzodiazepines/corticosteroids/sulthiame/ethosuximide) during the critical window preserves language and cognition.
5. **Biomarker discovery** (quantitative EEG metrics, CSF/plasma synaptic markers, methylation episignature) for diagnosis and prognosis.
6. **Preclinical gene-dosage restoration** (AAV gene replacement or ASO/upregulation strategies) in the *Cnksr2*-knockout mouse, assessing reversibility and the therapeutic window.
7. **Standardize diagnostic and counseling pathways**, including routine sleep-EEG surveillance in *CNKSR2*-variant carriers and cascade testing of at-risk females.

---

*Evidence source types used: human clinical (case reports/series, EEG, imaging), model organism (Cnksr2-knockout mouse), in vitro (hippocampal neurons, biochemistry), and computational (molecular dynamics). Ontology suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) are provided inline for knowledge-base population.*


## Artifacts

- [OpenScientist final report](Intellectual_Disability_X-linked_Syndromic_Houge_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Disability_X-linked_Syndromic_Houge_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030909` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **intellectual disability, X-linked, syndromic, Houge type**
- `HP:0002528` (1 mention) - the report calls it "related"; HP calls it **Granulovacuolar degeneration**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0030909` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 20 |
| On topic | 14 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24656827` *(abstract only)*: "a spatial modulator of Rac cycling during spine morphogenesis… the interaction with Vilse is critical for maintaining RacGDP/GTP levels at a balance required for spine formation"
  - closest text in source: "Through mutant analysis, protein depletion and rescue experiments, we identify CNK2 as a spatial modulator of Rac cycling during spine morphogenesis and find that the interaction with Vilse is critical for maintaining RacGDP/GTP levels at a balance required for spine formation."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10753660` (9 mentions) - Association of membrane-associated guanylate kinase-interacting protein-1 with Raf-1.
  - shared terms: maguin

Weighed against this report's own most characteristic terms: `cnksr2`, `female`, `eses`, `variant`, `disorder`, `language`, `loss`, `gene`, `epilepsy`, `csws`, `patient`, `phenotype`, `genetic`, `eeg`, `mrxshg`, `disability`, `intellectual`, `hippocampal`, `maguin`, `seizure`.
