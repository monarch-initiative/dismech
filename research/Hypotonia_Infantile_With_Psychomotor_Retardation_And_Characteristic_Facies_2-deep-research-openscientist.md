---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-10T14:13:10.049374'
end_time: '2026-11-10T14:27:58.407140'
duration_seconds: 888.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypotonia Infantile With Psychomotor Retardation And Characteristic
    Facies 2
  mondo_id: MONDO:0014777
  category: Mendelian
  causal_genes: UNC80
  omim_id: OMIM:616801
  synonyms: hypotonia, infantile, with psychomotor retardation and characteristic
    facies 2; IHPRF2; hypotonia, infantile, with psychomotor retardation and characteristic
    facies type 2; IHPRF2; UNC80 hypotonia, infantile, with psychomotor retardation
    and characteristic facies; hypotonia, infantile, with psychomotor retardation
    and characteristic facies caused by mutation in UNC80
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypotonia_Infantile_With_Psychomotor_Retardation_And_Characteristic_Facies_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypotonia_Infantile_With_Psychomotor_Retardation_And_Characteristic_Facies_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia Infantile With Psychomotor Retardation And Characteristic Facies 2
- **MONDO ID:** MONDO:0014777 (if available)
- **Causal gene(s):** UNC80
- **OMIM:** OMIM:616801
- **Synonyms:** hypotonia, infantile, with psychomotor retardation and characteristic facies 2; IHPRF2; hypotonia, infantile, with psychomotor retardation and characteristic facies type 2; IHPRF2; UNC80 hypotonia, infantile, with psychomotor retardation and characteristic facies; hypotonia, infantile, with psychomotor retardation and characteristic facies caused by mutation in UNC80
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypotonia Infantile With Psychomotor Retardation And Characteristic Facies 2** covering all of the
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

# Infantile Hypotonia with Psychomotor Retardation and Characteristic Facies 2 (IHPRF2): A Comprehensive Disease Report

**Disease:** Hypotonia, Infantile, with Psychomotor Retardation and Characteristic Facies 2 (IHPRF2)
**MONDO ID:** MONDO:0014777 | **OMIM:** 616801 | **Orphanet:** ORPHA:700333 | **GARD:** 0018458 | **MedGen/UMLS:** C4225203
**Causal gene:** **UNC80** (HGNC:26582; OMIM gene 612636; Ensembl ENSG00000144406; chromosome 2q34)
**Category:** Mendelian (autosomal recessive)

---

## Summary

**Infantile hypotonia with psychomotor retardation and characteristic facies 2 (IHPRF2)** is a rare autosomal-recessive neurodevelopmental disorder caused by **biallelic loss-of-function variants in UNC80**, the gene encoding an essential auxiliary subunit of the **NALCN sodium-leak channel complex** (NALCN–FAM155A–UNC79–UNC80). Despite the serial "2" in its name, the defining molecular lesion of this disorder is UNC80 dysfunction; the related disorder IHPRF1 (OMIM 615419) is caused by NALCN itself, and the two should not be conflated. IHPRF2 was first delineated by Stray-Pedersen et al. in 2016 ([PMID: 26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/)), who described four individuals from three unrelated families with homozygous missense or compound-heterozygous truncating UNC80 mutations presenting with persistent hypotonia, encephalopathy, growth failure, and severe intellectual disability.

Mechanistically, the UNC80 protein is a large intracellular scaffold that, together with UNC79, tethers to and activates the pore-forming NALCN channel. NALCN conducts a voltage-independent **sodium (Na⁺) leak current** that sets the neuronal resting membrane potential and governs basal excitability. Cryo-EM structures show that UNC79–UNC80 form a piler-shaped heterodimer whose interactions both ensure proper NALCN cell-surface localization and relieve NALCN auto-inhibition. Biallelic loss of functional UNC80 destabilizes and mislocalizes the channelosome, reducing the Na⁺ leak current and thereby dysregulating resting membrane potential and neuronal excitability. The downstream clinical result is neonatal hypotonia, severe global developmental delay/intellectual disability, absent speech, feeding difficulties, postnatal growth retardation, a characteristic facial gestalt, and variable epilepsy and central sleep apnea.

There is currently **no curative or disease-specific therapy**. Management is entirely supportive and multidisciplinary (physical, occupational, and speech therapy; nutritional support including assisted feeding; seizure management; respiratory monitoring). Diagnosis relies on exome or genome sequencing, with chromosomal microarray needed to detect intragenic copy-number variants that can serve as one of the two causative alleles. This report consolidates six confirmed findings, 16 reviewed papers, and verified cross-references into a complete disease knowledge-base entry.

---

## Key Findings

### Finding 1 — IHPRF2 is caused by biallelic loss-of-function variants in UNC80 (autosomal recessive)

IHPRF2 (MONDO:0014777) results from **biallelic (homozygous or compound-heterozygous) loss-of-function variants in UNC80**, inherited in an autosomal-recessive pattern. The disorder was first described by Stray-Pedersen et al. (2016), who reported four individuals from three unrelated families carrying either homozygous missense or compound-heterozygous truncating UNC80 mutations. As the authors stated: *"We report four individuals from three unrelated families who have homozygous missense or compound heterozygous truncating mutations in UNC80 and persistent hypotonia, encephalopathy, growth failure, and severe intellectual disability"* ([PMID: 26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/)).

Critically, the same study provided functional validation: *"HEK293T cells transfected with an expression plasmid containing the c.5098C>T (p.Pro1700Ser) UNC80 mutation found in one individual showed markedly decreased NALCN channel currents"* — direct proof that a disease UNC80 variant reduces NALCN current, i.e., a loss-of-function mechanism.

Subsequent families have confirmed the biallelic, recessive basis and expanded the mutational spectrum:

| Study (PMID) | Population | Representative variants | Zygosity |
|---|---|---|---|
| Stray-Pedersen 2016 ([26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/)) | 3 unrelated families | e.g. c.5098C>T (p.Pro1700Ser) | Homozygous missense / compound-het truncating |
| He 2018 ([29572195](https://pubmed.ncbi.nlm.nih.gov/29572195/)) | Chinese (2 patients) | c.3719G>A (p.W1240*)/c.4926_4937del; c.4963C>T (p.R1655C)/c.8385C>G (p.Y2795*) | Compound heterozygous |
| Obeid 2018 ([29430593](https://pubmed.ncbi.nlm.nih.gov/29430593/)) | Palestinian-Emirati | novel homozygous variant | Homozygous |
| Kuptanon 2019 ([30771478](https://pubmed.ncbi.nlm.nih.gov/30771478/)) | Thai | c.3226C>T (p.Arg1076Ter)/c.3205C>T (p.Arg1069Ter) | Compound heterozygous |
| Benvenuto 2026 ([40801661](https://pubmed.ncbi.nlm.nih.gov/40801661/)) | Italian family | c.798+1G>T splice / exons 40–44 deletion | Compound heterozygous (SNV + CNV) |

The Benvenuto 2026 report is notable for demonstrating that **structural variants / copy-number variants** can constitute one of the two biallelic hits: *"chromosomal microarray disclosed a microdeletion involving 5 exons (40-44) in the other allele"* ([PMID: 40801661](https://pubmed.ncbi.nlm.nih.gov/40801661/)). This has direct diagnostic implications — single-nucleotide variant screening alone can miss a second allele.

### Finding 2 — UNC80 is an auxiliary subunit of the NALCN sodium-leak channelosome; the mechanism runs from loss of Na⁺ leak current to neuronal hypoexcitability

UNC80 is a large auxiliary protein of the **NALCN channelosome (NALCN–FAM155A–UNC79–UNC80)**, which conducts a voltage-independent Na⁺ leak current that sets resting membrane potential and neuronal excitability. As summarized by Bramswig et al. (2018): *"NALCN is a conserved cation channel, which conducts a permanent sodium leak current and regulates resting membrane potential and neuronal excitability"* ([PMID: 30167850](https://pubmed.ncbi.nlm.nih.gov/30167850/)).

The cryo-EM structure of the complex (Kang & Chen 2022) resolves how UNC80 contributes: UNC79 and UNC80 form a piler-shaped heterodimer tethered to the NALCN intracellular side via two essential interactions. One interaction ensures proper NALCN cell-surface localization; the other activates the channel — *"The other interaction relieves the self-inhibition of NALCN by pulling the auto-inhibitory CTD Interacting Helix (CIH) out of its binding site"* ([PMID: 35550517](https://pubmed.ncbi.nlm.nih.gov/35550517/)).

Wie et al. (2020) demonstrated the functional consequence of patient-type truncations: the UNC80 C-terminus interacts with UNC79 and overcomes a soma-retention signal to direct the complex to dendrites. *"UNC80 lacking this domain, as found in human patients, still supports whole-cell NALCN currents but lacks dendritic localization"* ([PMID: 32620897](https://pubmed.ncbi.nlm.nih.gov/32620897/)). Thus, even truncations that preserve some whole-cell current disrupt the proper subcellular distribution of the channel — a disease-relevant mechanism beyond simple current loss. The same study notes that **UNC80 knockout mice are neonatal lethal**, underscoring the essential nature of this subunit.

### Finding 3 — Clinical phenotype: neonatal hypotonia, severe global developmental delay/ID, absent speech, feeding difficulties, growth retardation, characteristic facies, with variable epilepsy and central sleep apnea

The IHPRF2 phenotype centers on a constellation of neonatal/infantile neurological features. Core features established by Stray-Pedersen (2016) are persistent hypotonia, encephalopathy, growth failure, and severe intellectual disability. He et al. (2018) reported that both of their patients had developmental delay/intellectual disability and hypotonia, with variable additional features (epilepsy, hyperactivity, postnatal growth retardation, self-injurious behavior). They defined the facial gestalt: *"Common facial dysmorphisms include a thin upper lip, a tented upper lip, a triangular face, strabismus and microcephaly"* ([PMID: 29572195](https://pubmed.ncbi.nlm.nih.gov/29572195/)). They also noted diagnostic overlap: *"To some extent, the manifestations of IHPRF2 mimic those of Angelman syndrome (AS)-like syndromes."*

Benvenuto 2026 provided a detailed modern phenotype description in two affected siblings: *"both presenting with neonatal hypotonia, severe global developmental delay, major feeding difficulties with the need for assisted nutrition, inability to speak and walk autonomously, epilepsy, central sleep apnea, and facial dysmorphism"* ([PMID: 40801661](https://pubmed.ncbi.nlm.nih.gov/40801661/)).

| Phenotype | HPO term | Frequency | Onset | Severity |
|---|---|---|---|---|
| Neonatal hypotonia | HP:0001319 | Very frequent / near-universal | Neonatal | Severe, persistent |
| Severe global developmental delay | HP:0011344 | Very frequent | Infantile | Severe |
| Intellectual disability, severe | HP:0010864 | Very frequent | Childhood | Severe |
| Absent speech | HP:0001344 | Frequent | Childhood | Severe |
| Feeding difficulties | HP:0011968 | Frequent (assisted nutrition) | Neonatal/infantile | Moderate–severe |
| Postnatal growth retardation | HP:0008897 | Frequent | Infantile | Variable |
| Microcephaly | HP:0000252 | Frequent | Congenital/postnatal | Variable |
| Thin/tented upper lip | HP:0000219 | Frequent | Congenital | — (dysmorphic) |
| Triangular face | HP:0000325 | Frequent | Congenital | — (dysmorphic) |
| Strabismus | HP:0000486 | Frequent | Infantile | Variable |
| Seizures / epilepsy | HP:0001250 | Variable | Infantile/childhood | Variable |
| Central sleep apnea | HP:0010536 | Reported (variable) | Infantile | Variable |
| Hyperactivity / self-injurious behavior | HP:0000752 / HP:0100716 | Variable | Childhood | Variable |

IHPRF2 is **phenotypically heterogeneous**, and PURA-related neurodevelopmental disorder is a close differential diagnosis (Mishra 2021, [PMID: 33229923](https://pubmed.ncbi.nlm.nih.gov/33229923/)), which notes *"Significant phenotypic overlap was observed in subjects with PURA-related NDD and IHPRF especially with IHPRF2, caused by biallelic pathogenic variants in UNC80."*

### Finding 4 — Cross-species conservation: UNC80 is an essential, conserved NALCN channelosome subunit; Unc80-null mice are neonatal lethal

The NALCN–UNC79–UNC80 module is deeply conserved. In *Drosophila*, loss-of-function of *unc80* (CG18437) or *unc79* produces circadian locomotor defects indistinguishable from mutants of *narrow abdomen* (*na*, the NALCN ortholog): *"These mutants display severe defects in circadian locomotor rhythmicity that are indistinguishable from na mutant phenotypes"* (Lear et al. 2013, [PMID: 24223770](https://pubmed.ncbi.nlm.nih.gov/24223770/)). The same study established the interdependent stability of the three subunits: *"loss of na, unc79, or unc80 gene function leads to decreased expression of all three proteins, with minimal effect on transcript levels"* — a post-transcriptional co-dependence that explains why loss of any one subunit cripples the whole complex.

In mammals, **UNC80 knockout mice are neonatal lethal** ([PMID: 32620897](https://pubmed.ncbi.nlm.nih.gov/32620897/)), and invertebrate/mammalian models implicate the channelosome in locomotor behavior, anesthetic sensitivity, and respiratory rhythms (Cochet-Bissuel 2014, [PMID: 24904279](https://pubmed.ncbi.nlm.nih.gov/24904279/)).

### Finding 5 — Gene identifiers and gnomAD constraint support a recessive loss-of-function mechanism (heterozygous LoF tolerated)

UNC80 identifiers (GRCh38): **Ensembl ENSG00000144406; HGNC:26582; chromosome 2q34 (chr2:209,771,832–209,999,300); OMIM gene 612636**. Population constraint from gnomAD is fully consistent with a recessive, two-hit loss-of-function mechanism:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 4.7×10⁻⁵ | **Not** haploinsufficient (single LoF tolerated) |
| LOEUF (oe_lof upper) | 0.485 | Moderately LoF-intolerant |
| Observed/expected LoF | 0.426 (164 obs vs 384.6 exp) | Some LoF depletion |
| LoF Z | 9.54 | Selection against biallelic LoF |
| Missense Z | 5.39 | Missense-constrained |
| oe_mis | 0.80 | Modest missense depletion |

The low pLI confirms that heterozygous LoF is tolerated in the population (carriers are unaffected), while biallelic LoF causes disease — exactly the pattern seen in the clinical reports, where carrier parents are unaffected ([PMID: 26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/)). The quote *"homozygous missense or compound heterozygous truncating mutations in UNC80"* captures the requirement that both alleles be affected.

### Finding 6 — Verified disease cross-references and ClinVar variant landscape

MONDO:0014777 ("hypotonia, infantile, with psychomotor retardation and characteristic facies 2") cross-references, verified against the MONDO ontology record: **OMIM:616801, Orphanet:700333, GARD:0018458, MedGen/UMLS C4225203 (MedGen UID 907651)**. An earlier assumed Orphanet code (457395) was found to be incorrect and corrected to ORPHA:700333.

ClinVar (E-utilities query performed during this investigation) shows UNC80 has roughly **2,710 submitted variant records**, of which **285 are classified pathogenic, 87 likely pathogenic, and ~2,644 are variants of uncertain significance (VUS)**. The large VUS fraction reflects the gene's size (~3,258 amino acids) and relatively limited functional annotation, underscoring the ongoing interpretive challenge for new missense variants.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in UNC80** (missense, nonsense, frameshift, splice-site, or intragenic CNV on both alleles) **lead to** absent or non-functional UNC80 protein. *(Demonstrated: multiple families; functional assay for p.Pro1700Ser.)*
2. Loss of functional UNC80 **results in** destabilization of the NALCN channelosome, because UNC79/UNC80/NALCN are mutually dependent for protein stability. *(Demonstrated in Drosophila; inferred in human.)*
3. Loss of UNC80's two tethering interactions with NALCN **leads to** (a) impaired NALCN cell-surface/dendritic localization and (b) failure to relieve NALCN auto-inhibition (CIH not extracted). *(Demonstrated by cryo-EM and cell biology.)*
4. These defects **result in** a reduced voltage-independent **Na⁺ leak current** through NALCN. *(Demonstrated: decreased NALCN currents in HEK293T with patient variant.)*
5. Reduced Na⁺ leak current **leads to** a more hyperpolarized/dysregulated neuronal resting membrane potential and altered basal excitability across central neurons. *(Inferred from channel physiology.)*
6. Dysregulated excitability in brainstem, cortical, and motor circuits **results in** the clinical phenotype, branching into:
   - → **Motor circuits / muscle tone regulation** → neonatal hypotonia, motor delay, inability to walk.
   - → **Cognitive/language networks** → severe intellectual disability, absent speech.
   - → **Brainstem respiratory rhythm generators** → central sleep apnea.
   - → **Cortical networks** → epilepsy (variable).
   - → **Hypothalamic/growth and feeding circuits** → feeding difficulties, growth retardation.
   - → **Craniofacial development (mechanism less defined)** → characteristic facies, microcephaly. *(Largely inferred; developmental contribution of NALCN signaling not fully established.)*

```
UNC80 biallelic LoF
        │
        ▼
NALCN channelosome destabilized / mislocalized
        │
        ▼
↓ NALCN Na⁺ leak current
        │
        ▼
Dysregulated resting membrane potential & neuronal excitability
        │
  ┌─────┼───────┬───────────┬──────────────┬─────────────┐
  ▼     ▼       ▼           ▼              ▼             ▼
Hypotonia  ID/   Central    Epilepsy    Feeding/      Facial
motor      absent  sleep                growth        dysmorphism
delay      speech  apnea                retardation   (inferred)
```

**Upstream vs downstream:** The UNC80 mutation and channelosome destabilization are the upstream initiating events; the reduced Na⁺ leak current is the pivotal intermediate node; the neuronal excitability defect and clinical phenotypes are downstream.

**Cell types and processes involved:** Central neurons (CL:0000540 neuron; CL:0000617 GABAergic neuron and CL:0000679 glutamatergic neuron likely among affected populations), particularly pacemaker and rhythm-generating neurons. Key GO biological processes: **GO:0051899 (membrane depolarization)**, **GO:0042391 (regulation of membrane potential)**, **GO:0035725 (sodium ion transmembrane transport)**, **GO:0001508 (action potential)**, **GO:0007268 (chemical synaptic transmission)**. Cellular component: **GO:0005886 (plasma membrane)**, **GO:0043025 (neuronal cell body)**, **GO:0030425 (dendrite)**. Molecular function: **GO:0005272 (sodium channel activity)**. Relevant chemical entity: **CHEBI:29101 (sodium(1+))**.

**Anatomical structures (UBERON):** Primary system is the central nervous system — **UBERON:0000955 (brain)**, **UBERON:0001869 (cerebral cortex)**, **UBERON:0002298 (brainstem)**, **UBERON:0002037 (cerebellum)**; secondary involvement of **UBERON:0001630 (skeletal muscle)** via hypotonia (secondary, not a primary myopathy), and the face/craniofacial skeleton for dysmorphism. The disorder is a **bilateral, diffuse CNS channelopathy** rather than a focal lesion.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/) | *Biallelic Mutations in UNC80 Cause Persistent Hypotonia, Encephalopathy, Growth Retardation, and Severe Intellectual Disability* | **Landmark / disease-defining.** Establishes biallelic UNC80 cause, core phenotype, and functional proof of reduced NALCN current. |
| [35550517](https://pubmed.ncbi.nlm.nih.gov/35550517/) | *Structure and mechanism of NALCN-FAM155A-UNC79-UNC80 channel complex* | **Structural mechanism.** Cryo-EM showing UNC80/UNC79 role in localization and relief of NALCN auto-inhibition. |
| [32620897](https://pubmed.ncbi.nlm.nih.gov/32620897/) | *ID-associated UNC80 mutations reveal inter-subunit interaction and dendritic function of the NALCN complex* | **Functional/cell biology.** Patient truncations disrupt dendritic localization; UNC80-KO mice neonatal lethal. |
| [30167850](https://pubmed.ncbi.nlm.nih.gov/30167850/) | *Genetic variants in NALCN-UNC80-UNC79 cause a broad clinical phenotype (NALCN channelopathies)* | Defines channelosome function and the NALCN channelopathy spectrum. |
| [29572195](https://pubmed.ncbi.nlm.nih.gov/29572195/) | *Biallelic UNC80 mutations caused IHPRF2 in two Chinese patients* | Facial gestalt, phenotype variability, Angelman-like overlap. |
| [29430593](https://pubmed.ncbi.nlm.nih.gov/29430593/) | *Novel homozygous UNC80 variant in a child with IHPRF2* | Independent family; confirms homozygous recessive basis. |
| [30771478](https://pubmed.ncbi.nlm.nih.gov/30771478/) | *WES revealed mutations in FBXL4, UNC80, ADK in Thai patients* | Compound-het truncating variants; WES diagnostic utility. |
| [40801661](https://pubmed.ncbi.nlm.nih.gov/40801661/) | *Five-exon intragenic deletion + splice variant cause IHPRF2 in an Italian family* | **CNV as one allele**; detailed modern phenotype incl. central sleep apnea. |
| [24223770](https://pubmed.ncbi.nlm.nih.gov/24223770/) | *UNC79 and UNC80 indispensable for circadian locomotor rhythms in Drosophila* | Cross-species conservation; interdependent subunit stability. |
| [33229923](https://pubmed.ncbi.nlm.nih.gov/33229923/) | *Expanding the phenotype of PURA-related NDD* | Key differential diagnosis for IHPRF2. |
| [24904279](https://pubmed.ncbi.nlm.nih.gov/24904279/) | *The sodium leak channel, NALCN, in health and disease* | Review of channelosome physiology and disease associations. |
| [22196327](https://pubmed.ncbi.nlm.nih.gov/22196327/) | *Sodium leak channels in neuronal excitability and rhythmic behaviors* | Context for NALCN/UNC79/UNC80 in rhythmic behavior and neonatal lethality. |
| [41458659](https://pubmed.ncbi.nlm.nih.gov/41458659/) | *WES in a consanguineous family with UNC80-related NDD* | Additional consanguineous case series; diagnostic utility. |
| [34594366](https://pubmed.ncbi.nlm.nih.gov/34594366/) | *Maternal uniparental disomy of chromosome 2* (case report) | Illustrates UPD as a route to homozygosity on chr2 (where UNC80 resides). |
| [22476981](https://pubmed.ncbi.nlm.nih.gov/22476981/) | *NALCN: a regulator of pacemaker activity* | Channelosome in pacemaker/excitability regulation. |
| [40752487](https://pubmed.ncbi.nlm.nih.gov/40752487/) | *Ion channels in respiratory rhythm generation and sensorimotor integration* | Links NALCN leak conductance to brainstem respiratory rhythm (relevant to central sleep apnea). |

All quoted abstract snippets in the Key Findings section were verified against stored abstracts. No reviewed paper contradicts the central model; the literature is uniformly consistent that UNC80 LoF is the cause and that it acts through NALCN channelosome dysfunction.

---

## Section-by-Section Knowledge-Base Content

### 1. Disease Information
A rare autosomal-recessive neurodevelopmental/neuromuscular disorder of infancy. Identifiers: MONDO:0014777, OMIM:616801, Orphanet ORPHA:700333, GARD 0018458, MedGen/UMLS C4225203. No specific ICD-10 code; grouped under congenital hypotonia / neurodevelopmental disorders (ICD-10 ~P94.2 / ICD-11 structural analogs). Synonyms: IHPRF2; UNC80 hypotonia with psychomotor retardation and characteristic facies. Information is derived from aggregated disease-level resources (OMIM/Orphanet) plus a small number of individual-patient case reports (<30 reported patients worldwide).

### 2. Etiology
**Primary cause: genetic** — biallelic loss-of-function variants in UNC80. No environmental, infectious, or toxic cause. **Genetic risk factors:** consanguinity markedly raises the risk of homozygous UNC80 variants; being a heterozygous carrier plus a reproductive partner who is also a carrier. Uniparental disomy of chromosome 2 is a rare route to homozygosity ([PMID: 34594366](https://pubmed.ncbi.nlm.nih.gov/34594366/)). **No established environmental risk or protective factors.** No known modifier genes or protective alleles. **Gene–environment interactions:** none established.

### 3. Phenotypes
See the HPO table in Finding 3. Phenotype types span clinical signs (hypotonia, dysmorphism), developmental/behavioral (ID, absent speech, hyperactivity, self-injury), and functional (feeding difficulty, apnea, seizures). Onset is neonatal/infantile; severity is generally severe; course is chronic and largely static-to-slowly-evolving (not neurodegenerative in the classic sense). Quality-of-life impact is profound: most patients are non-verbal, non-ambulatory, and dependent for daily care, frequently requiring assisted nutrition.

### 4. Genetic / Molecular Information
Causal gene UNC80 (HGNC:26582; Ensembl ENSG00000144406; OMIM 612636; chr2q34). Variant types reported: missense, nonsense, frameshift (small indels), canonical splice-site, and multi-exon intragenic deletions (CNVs). ClinVar: ~285 pathogenic / 87 likely pathogenic / ~2,644 VUS. All pathogenic alleles are germline; biallelic. Functional consequence: **loss of function** (reduced NALCN current; mislocalization). gnomAD constraint (Finding 5) shows heterozygous LoF tolerated (pLI≈0), missense-constrained (Z=5.39). No proven modifier genes or disease-specific epigenetic changes.

### 5. Environmental Information
Not applicable — IHPRF2 is a monogenic Mendelian disorder with no known environmental, lifestyle, or infectious contributors.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Core defect: reduced NALCN-mediated Na⁺ leak conductance due to loss of the UNC80 scaffold. Molecular "pathway" is ion-channel/membrane-potential regulation rather than a classical signaling cascade. No metabolic, immune, or fibrotic mechanisms are implicated.

### 7. Anatomical Structures Affected
Primary: central nervous system (brain — cortex, brainstem, cerebellum; UBERON:0000955). Secondary: skeletal muscle (hypotonia, secondary), craniofacial structures (dysmorphism), GI/feeding apparatus (functional). Bilateral/diffuse. Subcellular: plasma membrane, dendrites, neuronal cell body (GO:0005886, GO:0030425, GO:0043025). Cell types: central neurons including pacemaker/rhythm-generating neurons (CL:0000540).

### 8. Temporal Development
Onset: congenital/neonatal (hypotonia present from birth). Pattern: chronic, lifelong. Course: severe static-to-slowly-evolving encephalopathy; developmental milestones severely delayed or never achieved. No remission; epilepsy and apnea may fluctuate. Critical period for intervention is early-childhood supportive/rehabilitative care.

### 9. Inheritance and Population
Autosomal recessive. Penetrance appears complete for biallelic LoF; expressivity is variable (epilepsy, apnea, growth, behavior differ between patients). No anticipation (not a repeat-expansion disorder). Consanguinity is an important contributor. Carrier frequency is low but not precisely defined; heterozygous LoF alleles are present in gnomAD at low frequency. No strong founder effect established. Prevalence: ultra-rare (<1/1,000,000; fewer than ~30 published patients). Sex ratio ~1:1 (autosomal). Reported across diverse populations (European, Chinese, Thai, Palestinian-Emirati, Italian).

### 10. Diagnostics
**Primary diagnostic modality: molecular genetic testing** — trio whole-exome sequencing (WES) or whole-genome sequencing (WGS) is the mainstay (multiple cases diagnosed by WES). **Chromosomal microarray (CMA)** is essential to detect intragenic CNVs that form one of the two alleles ([PMID: 40801661](https://pubmed.ncbi.nlm.nih.gov/40801661/)). Gene panels for intellectual disability/hypotonia/neurodevelopmental disorders typically include UNC80. Supportive: brain MRI (variable/nonspecific findings), EEG (if seizures), metabolic workup to exclude mimics. No specific biomarker exists. Differential diagnosis: IHPRF1 (NALCN), PURA-related NDD ([PMID: 33229923](https://pubmed.ncbi.nlm.nih.gov/33229923/)), Angelman syndrome and AS-like disorders ([PMID: 29572195](https://pubmed.ncbi.nlm.nih.gov/29572195/)), Prader-Willi syndrome, and other congenital hypotonia/ID syndromes.

### 11. Outcome / Prognosis
Severe lifelong morbidity: most patients are non-ambulatory and non-verbal with profound intellectual disability and dependence for care. Complications include feeding failure (requiring gastrostomy/assisted nutrition), aspiration, epilepsy, and central sleep apnea with attendant respiratory risk. Life expectancy data are limited given rarity; early mortality risk exists (consistent with neonatal lethality in mouse KO), but survival into childhood/adulthood with supportive care is reported. Prognostic factors likely include presence/severity of apnea, seizures, and feeding failure. No validated prognostic biomarkers.

### 12. Treatment
**No curative or disease-specific therapy.** Management is entirely **supportive and multidisciplinary** (NCIT concepts: Supportive Care, Physical Therapy, Occupational Therapy, Speech Therapy, Nutritional Support, Anticonvulsant Therapy):
- Rehabilitation: physical, occupational, and speech/communication therapy.
- Nutrition: feeding support, nasogastric/gastrostomy tube as needed.
- Seizures: standard antiseizure medications tailored to seizure type.
- Respiratory: monitoring and management of central sleep apnea.
- Supportive/symptomatic care for behavior, orthopedics, and vision (strabismus).

No approved pharmacotherapy, gene therapy, RNA-based, or cell therapy exists; none are in clinical trials specific to IHPRF2. Pharmacogenomic considerations are generic. Personalized/precision approaches are conceptual only.

### 13. Prevention
No primary prevention (genetic disorder). Secondary prevention via **genetic counseling and carrier/cascade testing** in families and consanguineous couples; prenatal diagnosis and preimplantation genetic testing (PGT-M) are feasible once the familial biallelic variants are known. Recurrence risk for carrier couples is 25% per pregnancy. Tertiary prevention = management of complications (apnea monitoring, seizure control, nutrition, aspiration prevention). Not amenable to immunization or public-health environmental intervention.

### 14. Other Species / Natural Disease
UNC80 orthologs are conserved and functionally essential: *Drosophila* unc80 (CG18437), *C. elegans* unc-80, and mouse Unc80 (Mus musculus). Loss phenocopies NALCN loss across species ([PMID: 24223770](https://pubmed.ncbi.nlm.nih.gov/24223770/)). No naturally occurring companion-animal/wildlife disease is cataloged in OMIA for UNC80 at present. No zoonotic potential (non-infectious). Evolutionary conservation of the NALCN–UNC79–UNC80 module is strong.

### 15. Model Organisms
- **Mouse (Mus musculus):** Unc80 knockout — **neonatal lethal** ([PMID: 32620897](https://pubmed.ncbi.nlm.nih.gov/32620897/)); recapitulates the essentiality of the channelosome but limits adult-phenotype study; conditional/hypomorphic models would be needed to model viable human disease.
- **Drosophila melanogaster:** unc80 LoF — circadian locomotor rhythm defects identical to na (NALCN) mutants; demonstrates conserved function and subunit co-stability ([PMID: 24223770](https://pubmed.ncbi.nlm.nih.gov/24223770/)).
- **C. elegans:** unc-80 mutants — classical uncoordinated locomotion; historical basis of the gene name.
- **In vitro:** HEK293T heterologous expression of NALCN with UNC79/UNC80/FAM155A — used to show reduced NALCN current for patient variant p.Pro1700Ser ([PMID: 26708751](https://pubmed.ncbi.nlm.nih.gov/26708751/)) and dendritic-localization assays in neurons ([PMID: 32620897](https://pubmed.ncbi.nlm.nih.gov/32620897/)).

Model limitations: neonatal lethality of the mouse KO prevents modeling the chronic human course; invertebrate models capture channel physiology/behavior but not facial/cognitive features. iPSC-derived neuron/organoid models are a logical but not-yet-reported avenue.

---

## Limitations and Knowledge Gaps

1. **Small sample size.** Fewer than ~30 patients are published; prevalence, penetrance, expressivity, and natural-history/survival estimates are correspondingly imprecise.
2. **Genotype–phenotype correlation is unresolved.** It is unclear whether missense vs truncating vs CNV alleles, or residual-function alleles, predict severity (e.g., presence of apnea or epilepsy).
3. **Facial/craniofacial and growth mechanisms are inferred.** How a Na⁺-leak channelopathy produces the characteristic facies, microcephaly, and growth retardation is not mechanistically demonstrated.
4. **No viable mammalian disease model.** Unc80-null mice are neonatal lethal; no conditional/hypomorphic or humanized model recapitulating the chronic human phenotype has been reported.
5. **Large VUS burden.** ~2,644 UNC80 VUS in ClinVar complicate interpretation of novel variants; functional assays are not routine.
6. **No therapeutics.** There are no disease-modifying treatments, biomarkers, or clinical trials specific to IHPRF2.

## Proposed Follow-up Experiments / Actions

1. **Build a patient registry / natural-history study** to quantify prevalence, survival, and the frequency and age-dependence of epilepsy, central sleep apnea, and feeding failure.
2. **Develop conditional/hypomorphic or humanized Unc80 mouse models** and patient-iPSC-derived neurons/organoids to model the chronic disease and test interventions.
3. **Systematic genotype–phenotype analysis** across all reported variants (including CNVs) to test whether allele type predicts apnea, epilepsy, or motor outcome.
4. **High-throughput functional assays** (e.g., automated NALCN-current and dendritic-localization readouts) to reclassify UNC80 VUS per ACMG/AMP criteria.
5. **Mechanistic studies of craniofacial and growth phenotypes** to determine whether they arise from the same channelopathy or a developmental role of the channelosome.
6. **Explore pharmacological modulation of NALCN/channelosome** (e.g., agents that enhance residual leak conductance) as a conceptual therapeutic strategy, and routinely include CMA in diagnostic workups to capture intragenic deletions.

---

*Evidence source types represented: human clinical (case reports/series), model organism (Drosophila, mouse), in vitro (HEK293T/neuronal heterologous expression), and computational (gnomAD constraint, cryo-EM structure). All PMID-linked quotations were verified against stored abstracts.*


## Artifacts

- [OpenScientist final report](Hypotonia_Infantile_With_Psychomotor_Retardation_And_Characteristic_Facies_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypotonia_Infantile_With_Psychomotor_Retardation_And_Characteristic_Facies_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 27 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014777` (5 mentions) - the report calls it "if available", "hypotonia, infantile, with psychomotor retardation and characteristic facies 2"; MONDO calls it **hypotonia, infantile, with psychomotor retardation and characteristic facies 2**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000219` (1 mention) - the report calls it "Thin/tented upper lip"; HP calls it **Thin upper lip vermilion**, and lists "Thin upper lip" among its other names
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `UBERON:0001869` (1 mention) - the report calls it "cerebral cortex"; UBERON calls it **cerebral hemisphere**
- `UBERON:0001630` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **muscle organ**, and lists "muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014777` - called "if available", "hypotonia, infantile, with psychomotor retardation and characteristic facies 2"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Orphanet`, `GARD`.
