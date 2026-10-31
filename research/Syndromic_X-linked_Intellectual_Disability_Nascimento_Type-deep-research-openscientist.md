---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-10-25T04:08:41.396861'
end_time: '2026-10-25T04:08:41.403181'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Syndromic X-linked Intellectual Disability Nascimento Type
  mondo_id: MONDO:0010461
  causal_genes: UBE2A (hgnc:12472)
  omim_id: '300860'
  synonyms: UBE2A deficiency syndrome; X-linked intellectual disability-nail dystrophy-seizures
    syndrome; Nascimento syndrome; MRXSN
  category: Genetic (X-linked recessive neurodevelopmental)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Syndromic X-linked Intellectual Disability Nascimento Type
- **MONDO ID:** MONDO:0010461 (if available)
- **Causal gene(s):** UBE2A (hgnc:12472)
- **OMIM:** 300860
- **Synonyms:** UBE2A deficiency syndrome; X-linked intellectual disability-nail dystrophy-seizures syndrome; Nascimento syndrome; MRXSN
- **Category:** Genetic (X-linked recessive neurodevelopmental)

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Syndromic X-linked Intellectual Disability Nascimento Type** covering all of the
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

# Syndromic X-linked Intellectual Disability, Nascimento Type (UBE2A Deficiency Syndrome)

**Comprehensive Disease Characteristics Report**
MONDO:0010461 · OMIM 300860 · Causal gene: **UBE2A** (HGNC:12472)

---

## Summary (Answer to the Research Question)

Syndromic X-linked Intellectual Disability Nascimento type — more commonly called **UBE2A deficiency syndrome** (OMIM #300860, MONDO:0010461) — is an ultra-rare X-linked recessive neurodevelopmental malformation syndrome caused by loss-of-function of **UBE2A** (ubiquitin-conjugating enzyme E2A; HGNC:12472; the human ortholog of yeast RAD6, also called RAD6A/HR6A). Affected hemizygous males present with moderate-to-severe intellectual disability, absent/impaired speech, seizures, a recognizable craniofacial gestalt (synophrys, prominent supraorbital ridges, deep-set almond-shaped eyes, depressed nasal bridge, wide mouth, "myxedematous" facies), skin/appendage anomalies (generalized hirsutism, onychodystrophy/nail dystrophy), urogenital anomalies (micropenis), and — especially with larger Xq24 deletions — congenital heart defects. UBE2A is an E2 enzyme that, partnered with specific E3 ligases, monoubiquitinates PCNA (RAD18; translesion DNA synthesis/post-replication repair), monoubiquitinates histone H2B (BRE1/RNF20-40; transcription), and functions with Parkin in mitochondrial quality control; loss of these activities disrupts neuronal function (learning/mGluR-dependent long-term depression) and multi-organ development. There is no curative or targeted therapy; management is supportive and multidisciplinary.

**Evidence base:** This report is derived from aggregated disease-level resources (OMIM, Orphanet) and the primary clinical/molecular literature — predominantly individual case reports and small case series (human clinical evidence), complemented by model-organism (mouse, Drosophila, yeast) and in-vitro biochemical/structural evidence. No large registries, EHR cohorts, or omics datasets exist for this ultra-rare disorder.

---

## 1. Disease Information

**Overview.** A clinically recognizable syndromic form of X-linked intellectual disability characterized by developmental delay, moderate-to-severe ID, seizures, distinctive facial dysmorphism, skin/nail anomalies, hirsutism, and urogenital malformations (Cordeddu 2020, PMID 32415735; Czeschik 2013, PMID 24053514). First reported by Nascimento, Otto, de Brouwer & Vianna-Morgante in 2006 (PMID 16909393).

> *"UBE2A deficiency, that is, intellectual disability (ID) Nascimento type (MIM 300860), is an X-linked syndrome characterized by developmental delay, moderate to severe ID, seizures, dysmorphisms, skin anomalies, and urogenital malformations."* (PMID 32415735)

**Key identifiers.**
- **OMIM:** 300860 (Mental retardation, X-linked, syndromic, Nascimento-type)
- **MONDO:** MONDO:0010461
- **Orphanet:** ORPHA:447980 (UBE2A deficiency / X-linked intellectual disability, Nascimento type)
- **Gene:** UBE2A — HGNC:12472; NCBI Gene 7319; Ensembl ENSG00000077721; UniProt P49459; cytoband Xq24; gene OMIM *312180
- **ICD-10:** no specific code; grouped under Q87/F70–F79 (intellectual disability) and X-linked ID categories
- **ICD-11:** LD90.Y / 6A00 (disorders of intellectual development) with genetic etiology
- **MeSH:** indexed via "Intellectual Disability" + "Genetic Diseases, X-Linked"

**Synonyms / alternative names.** UBE2A deficiency syndrome; X-linked intellectual disability type Nascimento; X-linked mental retardation, Nascimento type; Nascimento syndrome; X-linked intellectual disability–nail dystrophy–seizures syndrome; MRXSN; MRXSN (syndromic X-linked intellectual developmental disorder, Nascimento form).

---

## 2. Etiology

**Primary cause — genetic (monogenic, loss of function).** The disease is caused exclusively by loss-of-function of **UBE2A**. Two lesion classes:
1. **Intragenic UBE2A variants** — missense, nonsense/truncating, canonical splice-site, exonic splice-disrupting (including synonymous) and small in-frame deletions.
2. **Xq24 contiguous-gene microdeletions** (≈7.1 kb to ≥386 kb) encompassing UBE2A ± neighboring genes (CXorf56, NKRF, SEPTIN6/SEPT6, MIR766, and in larger deletions SLC25A5/SLC25A43) (Tolmacheva 2020, PMID 32485717; Thunstrom 2015, PMID 25287747).

> *"This is the first description of a mutation in a ubiquitin-conjugating enzyme gene as the cause of a human disease."* (Nascimento 2006, PMID 16909393)

**Genetic risk factors.** The sole risk factor is a pathogenic UBE2A allele on the X chromosome; being male (hemizygous) is required for the full phenotype. Family history of X-linked ID / carrier mother is the key risk indicator. No susceptibility loci or polygenic contribution are described. **Modifier genes:** in contiguous-gene deletions, co-deleted genes (e.g., SEPTIN6, NKRF, SLC25A5) may modify severity; larger deletions correlate with congenital heart defects (Thunstrom 2015, PMID 25287747).

**Environmental risk factors.** None established; this is a Mendelian disorder. Not caused by toxins, infection, or lifestyle.

**Protective factors.**
- **Genetic/epigenetic (female carriers):** completely/extremely skewed X-chromosome inactivation preferentially silences the mutant allele, rendering heterozygous carrier females clinically unaffected (Czeschik 2013, PMID 24053514; Tolmacheva 2020, PMID 32485717).
> *"all carrier females are unaffected and presented with a completely skewed X inactivation in blood"* (PMID 24053514)
- **Paralog redundancy:** the autosomal paralog UBE2B (HR6B) shares RAD6 enzymatic activity and may partially compensate in non-neural tissues (inferred).
- No dietary/lifestyle protective factors are relevant.

**Gene–environment interactions.** None documented. The principal modifier is epigenetic (X-inactivation skewing), not environmental.

---

## 3. Phenotypes

Onset is **congenital/early childhood**; the cognitive course is **static (non-progressive)**. Frequencies below are qualitative (recurrent/common vs. variable) because the total reported cohort is small (~58 males). Phenotype types are noted as clinical sign (S), physical/morphological (M), behavioral/cognitive (B), or laboratory (L).

**Neurodevelopmental (near-universal, severe impact on daily functioning):**
- Intellectual disability, moderate–severe (B) — HP:0002342 / HP:0010864; near 100%
- Global developmental delay / motor delay (B) — HP:0001263, HP:0001270
- Absent or severely impaired speech (B/S) — HP:0001344 / HP:0000750; very common
- Seizures / epilepsy (S) — HP:0001250; frequent
- Hypotonia (S) — HP:0001252; reported
- Behavioral abnormalities (B) — HP:0000708

**Craniofacial dysmorphism (recognizable gestalt, common):**
- Synophrys — HP:0000664; prominent supraorbital ridges — HP:0000336-region; deep-set, almond-shaped eyes — HP:0000490/HP:0000492; depressed nasal bridge — HP:0005280; prominent columella — HP:0000426; hypoplastic alae nasi — HP:0000430; macrostomia/wide mouth — HP:0000154; high forehead — HP:0000348; myxedematous (puffy/coarse) appearance.

**Skin/appendages (common):**
- Generalized hirsutism — HP:0001007
- Onychodystrophy / nail dystrophy — HP:0003761; HP:0001597
- Myxedematous skin / abnormal skin appearance

**Genitourinary (common in males):**
- Micropenis — HP:0000054; other urogenital anomalies — HP:0000119; cryptorchidism reported

**Cardiovascular (variable; enriched in large deletions):**
- Congenital heart defect — HP:0001627 (abnormal heart morphology)

**Metabolic/endocrine & other (variable):**
- Obesity — HP:0001513 (Budny 2010, PMID 20412111)
- Hearing loss — HP:0000365 (Yan 2022, PMID 35846913)
- Pineal gland cysts/tumors — HP:0012514-region; hypogammaglobulinemia — HP:0004313 (Cordeddu 2020, PMID 32415735)
- Rare/expanding features: retinal coloboma, esophageal atresia with tracheoesophageal fistula, camptodactyly, clinodactyly, long broad toes (Thunstrom 2015, PMID 25287747); white-matter MRI hyperintensities (Ma 2019, PMID 31566921)

> *"Common clinical features in these patients include moderate to severe intellectual disability (ID), heart defects, dysmorphic features such as high forehead, synophrys, prominent supraorbital ridges, almond-shaped and deep-set eyes, wide mouth, myxedematous appearance, hirsutism, onychodystrophy, and genital anomalies."* (PMID 25287747)

**Quality-of-life impact.** Severe and lifelong: profound ID with absent/limited speech precludes independent living; most individuals require full-time care. Seizures, recurrent infections (hypogammaglobulinemia), and cardiac disease add morbidity. No disease-specific QoL instrument has been applied; generic ID disability frameworks (ICF) apply.

---

## 4. Genetic / Molecular Information

**Causal gene.** UBE2A (HGNC:12472; gene OMIM *312180; Xq24). Encodes a 152-aa E2 ubiquitin-conjugating enzyme (UniProt P49459) with a conserved UBC catalytic fold and the active-site cysteine (Cys88).

**Pathogenic variants (representative, all germline, all loss-of-function; ACMG classes pathogenic/likely pathogenic):**
- **Missense:** p.Arg11Gln (R11Q), p.Gly23Arg (G23R) (Budny 2010, PMID 20412111); p.Gly26Arg (G26R) (Tsurusaki 2017, PMID 28611923); p.Tyr82Cys (Y82C) (Jia 2020, PMID 32222108); p.Glu62Lys, p.Arg95Cys, p.Thr99Ala, p.Arg135Trp (Cordeddu 2020, PMID 32415735). Several (Glu62, Arg95, Thr99, Asp101) destabilize the E3-binding domain.
- **Nonsense/truncating:** p.Gln128* (Q128X; c.382C>T) — the first-described mutation, removes 25 C-terminal residues (Nascimento 2006, PMID 16909393).
- **In-frame deletions:** p.Val81_Ala83del, p.Asp101del (Cordeddu 2020, PMID 32415735).
- **Splice-site / splice-disrupting:** c.241+1G>A (Yan 2022, PMID 35846913); c.331-2A>G → r.331_359del / p.L112SfsX17 (Ma 2019, PMID 31566921); synonymous last-nucleotide-of-exon c.330G>A causing exon-5 skipping (Giugliano 2018, PMID 29283210).
- **Structural:** Xq24 microdeletions encompassing UBE2A (CMA-detectable).

**Allele frequency.** Pathogenic alleles are absent/ultra-rare in population databases; UBE2A is highly constrained and intolerant to loss-of-function (gnomAD; consistent with an essential housekeeping enzyme). **Somatic vs germline:** germline (constitutional); recurrence can occur through **maternal germline mosaicism** even when the variant is undetectable in maternal blood (Giugliano 2018, PMID 29283210).

**Functional consequence.** Uniformly **loss of function** (reduced E2 ubiquitin-conjugating activity and/or accelerated protein degradation); no gain-of-function or dominant-negative mechanism established.

**Modifier genes.** Co-deleted Xq24 genes in contiguous-gene deletions (SEPTIN6, NKRF, CXorf56, SLC25A5/SLC25A43) may modulate severity. The paralog UBE2B may buffer effects.

**Epigenetic information.** The disease intersects epigenetic regulation in two ways: (i) UBE2A itself drives **histone H2B monoubiquitination (H2Bub1)**, a chromatin mark coupled to H3K4/H3K36 methylation and transcription elongation (Pirngruber 2009, PMID 19844166); (ii) **X-inactivation skewing** governs carrier-female phenotype (PMID 24053514).

**Chromosomal abnormalities.** Interstitial Xq24 microdeletions (e.g., 168 kb, 239 kb, 386 kb) are a recurrent structural cause (PMID 32485717, PMID 40156274); detectable by chromosomal microarray.

---

## 5. Environmental Information

Not applicable — this is a monogenic genetic disorder. No environmental toxins, radiation, occupational exposures, lifestyle factors, or **infectious agents** cause or trigger it. (No NCBI Taxonomy pathogen association.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **loss-of-function UBE2A lesion** (intragenic variant or Xq24 deletion) in a hemizygous male **results in** reduced/absent functional UBE2A (RAD6A) E2 ubiquitin-conjugating enzyme (demonstrated for truncating/deletion alleles; several missense/in-frame alleles additionally **lead to** accelerated protein degradation — PMID 32415735).
2. Reduced UBE2A activity **leads to** deficient transfer of ubiquitin to substrates via its partner E3 ligases (a conserved "backside" β2–β3 β-turn couples catalysis to E3 engagement; patient variants disrupt this — PMID 42095445). This branches into three downstream arms:
   - **Arm A (DNA repair):** impaired RAD18-dependent **PCNA Lys164 monoubiquitination** → defective translesion DNA synthesis / post-replication repair (RAD6A–(RAD18)₂ ternary complex; PMID 21967848). *Contribution to the neurodevelopmental phenotype is inferred, not demonstrated in patient neurons.*
   - **Arm B (transcription/chromatin):** impaired BRE1/RNF20-40-dependent **histone H2B monoubiquitination (H2Bub1)** → dysregulated transcription elongation and downstream H3K4me3/H3K36me3 (PMID 19844166). *Inferred as a developmental-gene-expression mechanism.*
   - **Arm C (mitochondrial quality control):** impaired cooperation with the E3 ligase **Parkin** → mitochondrial dysfunction and impaired synaptic transmission (shown in Drosophila dUBE2A mutants; PMID 26476408). *Branch demonstrated in fly, inferred in human.*
3. In neurons, loss of UBE2A **results in** impaired **mGluR-dependent long-term depression (LTD)** and a major **spatial-learning deficit** (demonstrated in Ube2a-knockout mice; PMID 26476408) → **intellectual disability, impaired speech, and cognitive dysfunction**.
4. In non-neural developing tissues, loss of a ubiquitously expressed housekeeping E2 **leads to** dysmorphogenesis → craniofacial dysmorphism, skin/nail/hair anomalies, cardiac, and urogenital malformations (mechanism at the organ level is inferred from pleiotropy rather than tissue-specific experiments).
5. Seizures arise from the resulting cortical/neuronal dysfunction; recurrent infection arises where hypogammaglobulinemia is present; these **contribute to** morbidity and, in severe cases, early mortality.

### Detail by category
- **Molecular pathways:** ubiquitin–proteasome system / ubiquitin-conjugation cascade (E1→E2(UBE2A)→E3); post-replication DNA repair (RAD6–RAD18–PCNA); H2B ubiquitination–H3K4/K36 methylation transcription axis (P-TEFb/CDK9); PINK1–Parkin mitophagy (Arm C). Reactome: R-HSA-110314/RAD18 pathway; R-HSA-8866654 (E3 ubiquitin ligases).
- **Cellular processes:** DNA damage tolerance, transcription-coupled chromatin modification, mitochondrial quality control/mitophagy, synaptic plasticity (LTD). GO: GO:0006301 (postreplication repair), GO:0033523 (histone H2B ubiquitination), GO:0016567 (protein ubiquitination), GO:0000209 (protein polyubiquitination), GO:0007613/GO:0007612 (memory/learning), GO:0060292 (LTD of synaptic transmission).
- **Protein dysfunction:** loss of catalytic E2 activity and/or protein destabilization; UBC-fold perturbation; impaired E3 binding. Molecular function GO:0061631 / GO:0004842 (ubiquitin-protein transferase).
- **Metabolic changes:** mitochondrial/energy-metabolism impairment inferred via the Parkin branch; no human metabolomic signature reported.
- **Immune involvement:** hypogammaglobulinemia in a subset → humoral immunodeficiency, recurrent infection (PMID 32415735).
- **Epigenetic changes:** reduced H2Bub1 (loss-of-enzyme) and X-inactivation skewing (carrier modifier).
- **Molecular profiling:** no patient transcriptomic/proteomic/metabolomic/lipidomic or single-cell/spatial datasets are published for this disease. Functional-genomics context comes from targeted mouse/fly/yeast genetics, not CRISPR screens.
- **Upstream vs downstream:** the UBE2A LoF lesion is the single upstream driver; all three ubiquitination arms are proximal downstream effects; synaptic/cognitive and organ-malformation phenotypes are distal.
- **Cell types (CL):** neurons (CL:0000540), hippocampal pyramidal neurons; cardiomyocytes (CL:0000746); keratinocytes (CL:0000312); germ cells/spermatids (paralog context).

---

## 7. Anatomical Structures Affected

**Organ level — primary:** central nervous system / brain (UBERON:0000955) — cerebral white matter (UBERON:0002316; MRI hyperintensities in centrum semiovale), with hippocampus (UBERON:0002421) implicated by model-organism learning/LTD data. **Body systems:** nervous system (primary); integumentary (skin UBERON:0002097, nails UBERON:0001705, hair follicle); cardiovascular (heart UBERON:0000948); genitourinary/reproductive (penis UBERON:0000989; kidney/urinary tract); endocrine/metabolic; immune/hematologic (hypogammaglobulinemia); pineal gland (UBERON:0001905, cysts/tumors).

**Secondary involvement:** recurrent respiratory/other infections (immunodeficiency), feeding/digestive issues; esophageal atresia/TEF in rare cases.

**Tissue/cell level:** nervous tissue (neurons, CL:0000540); epithelial tissue (skin/nail — keratinocytes CL:0000312); cardiac muscle (cardiomyocytes CL:0000746); hair follicle. **Subcellular (GO Cellular Component):** nucleus (GO:0005634; PCNA/H2B ubiquitination), chromosome/chromatin (GO:0000785), mitochondrion (GO:0005739; Parkin arm), cytosol (GO:0005829).

**Localization / lateralization:** brain and systemic involvement are **bilateral/symmetric**; white-matter changes reported bilaterally (centrum ovale/semiovale).

---

## 8. Temporal Development

- **Onset:** congenital (HP:0003577); dysmorphism present at birth, developmental delay evident in infancy; insidious/chronic (not acute).
- **Progression:** cognitive impairment is **static/stable (non-progressive)** — a developmental, not neurodegenerative, disorder; disability is **lifelong/chronic**. Seizures may be episodic. No defined "stages."
- **Progression rate:** not applicable (stable); comorbidities (cardiac disease, infections) determine health trajectory.
- **Remission:** none (no spontaneous remission of ID); seizures may respond to antiepileptic drugs.
- **Critical periods:** the prenatal/early-postnatal window of brain and organ development is the period of vulnerability; after birth, intervention is supportive (early developmental intervention) rather than disease-modifying.

---

## 9. Inheritance and Population

- **Inheritance:** **X-linked recessive** (HP:0001419). Affected males are hemizygous; carrier mothers transmit the allele.
- **Penetrance:** essentially **complete in hemizygous males**; in carrier females, effectively non-penetrant owing to completely skewed X-inactivation (PMID 24053514).
- **Expressivity:** **variable** — from moderate ID with mild dysmorphism to severe multisystem disease with congenital heart defects (PMID 32415735).
- **Genetic anticipation:** none (not a repeat-expansion disorder).
- **Germline mosaicism:** documented (maternal), with recurrence risk despite negative maternal blood testing (PMID 29283210).
- **Founder effects / consanguinity:** no founder allele; consanguinity reported in some families (e.g., a consanguineous family with a 7.1-kb deletion, PMID 24053514) but not required.
- **Carrier frequency:** unknown; ultra-rare.
- **Epidemiology:** ultra-rare — **~58 affected males reported worldwide as of 2025** (PMID 40156274; Cordeddu 2020 reviewed 40). No reliable prevalence/incidence estimate (Orphanet: <1/1,000,000, likely underdiagnosed — PMID 24053514).
- **Demographics:** reported across diverse populations (European, Chinese, Japanese, others) with no ethnic predilection. **Sex ratio:** essentially all affected individuals are **male**; carrier females unaffected. Age distribution spans neonates to adults.

> *"X-linked intellectual disability type Nascimento is a clinically very distinct entity that might be underdiagnosed to date."* (PMID 24053514)

---

## 10. Diagnostics

**Diagnostic approach.** Clinical recognition of the gestalt (syndromic ID + characteristic facies + hirsutism + onychodystrophy + micropenis ± heart defect) prompts molecular confirmation.

**Genetic testing (confirmatory; NCIT C15709 Genetic Testing):**
- **Whole-exome sequencing (WES)** / targeted ID gene panels — detect intragenic variants (high yield; the main diagnostic route for point mutations) (e.g., PMID 32222108, 35846913).
- **Single-gene UBE2A sequencing** (Sanger) — confirmation and familial cascade/segregation testing.
- **Chromosomal microarray (CMA)** — detects Xq24 microdeletions (used in several cases, e.g., PMID 40156274, 32485717). Essential because deletions are missed by sequencing-only workflows.
- **WGS** — can capture both SNVs and CNVs; useful when WES+CMA are nondiagnostic.
- **RNA studies** — important to classify splice-region/synonymous variants (demonstrated exon skipping / aberrant transcripts, PMID 31566921, 29283210).
- **X-inactivation assay** in the mother — supports carrier interpretation (skewed XCI).
- Karyotype/FISH, mtDNA testing, and repeat-expansion testing are **not** indicated as primary tests.

**Supporting clinical tests:** brain MRI (may show bilateral white-matter hyperintensities — PMID 31566921); EEG for seizures; echocardiography/cardiac evaluation (CHD); renal/genitourinary ultrasound; serum immunoglobulins (hypogammaglobulinemia screen — PMID 32415735); pineal imaging surveillance given cyst/tumor risk. No specific biochemical biomarker or enzyme assay is used diagnostically.

**Clinical criteria / differential diagnosis.** No formal consensus criteria; diagnosis is molecular. Differential includes other syndromic XLID and dysmorphic ID syndromes with hirsutism/coarse facies — e.g., Cornelia de Lange syndrome (synophrys/hirsutism), Coffin–Siris, Wiedemann–Steiner, and other X-linked ID syndromes; distinguished by UBE2A genotype.

**Screening.** Not part of newborn screening. Relevant screening is **cascade/carrier testing** of at-risk female relatives and **prenatal/preimplantation genetic testing** in known-variant families.

---

## 11. Outcome / Prognosis

- **Survival/life expectancy:** many affected males survive into adulthood, but **early mortality occurs** — the first reported **sudden infant death** in UBE2A deficiency (neonate with 386-kb Xq24 deletion; PMID 40156274) and **4 of 9 affected members deceased** in one multigenerational family (PMID 40695520). No formal survival statistics exist (ultra-rare).
- **Mortality drivers:** congenital heart defects, complications of severe disability (aspiration, infections), and — where present — immunodeficiency.
- **Morbidity/disability:** severe lifelong intellectual disability with absent/limited speech; high dependency; seizures; recurrent infections. Generic ID/ICF disability frameworks apply; no disease-specific QoL data.
- **Disease course:** chronic, static cognitive impairment; non-recoverable (no restoration of cognition).
- **Prognostic factors:** lesion type/size — **larger Xq24 deletions correlate with congenital heart defects and more severe multisystem disease** (PMID 25287747, 32415735); presence of CHD, severe seizures, or hypogammaglobulinemia worsens prognosis. No molecular prognostic biomarker beyond genotype.

> *"suggest considerable prevalence of heart defects in the group of patients with larger deletions of Xq24 in comparison to the patients having intragenic UBE2A mutations"* (PMID 25287747)

---

## 12. Treatment

**No disease-specific, targeted, or curative therapy exists.** No approved gene therapy, cell therapy, RNA therapy, immunotherapy, or pharmacogenomic-guided treatment. Management is **supportive, symptom-directed, and multidisciplinary** (NCIT C15376 Supportive Care):

- **Pharmacotherapy:** antiepileptic/anticonvulsant drugs for seizures (NCIT C264 Anticonvulsant Agent); standard symptomatic medications. No pharmacogenomic guidance specific to the disease.
- **Advanced therapeutics:** none available; conceptual rationale for future gene/enzyme-restoration approaches exists (given LoF mechanism) but none in trials.
- **Surgical/interventional:** surgical repair of congenital heart defects and urogenital anomalies (e.g., hypospadias/cryptorchidism); management of esophageal atresia/TEF where present.
- **Supportive/rehabilitative:** early developmental intervention; special education; physical therapy (NCIT C15329), occupational therapy (NCIT C98136), and speech-language therapy for communication; nutritional support; dermatologic care for skin/nail anomalies.
- **Immunologic:** evaluation for hypogammaglobulinemia with immunoglobulin replacement and infection prophylaxis when indicated (PMID 32415735).
- **Surveillance:** cardiac, neurologic (seizures), immunologic, and pineal (cyst/tumor) monitoring.
- **Experimental trials:** no disease-specific interventional trials (ClinicalTrials.gov) identified.
- **Genetic counseling** (NCIT C15431) is a core component (see §13).

---

## 13. Prevention

- **Primary prevention:** not possible to prevent the mutation; relevant primary prevention is **reproductive** — genetic counseling, carrier testing of at-risk female relatives, and reproductive options (prenatal diagnosis, preimplantation genetic testing [PGT-M], donor options) in known-variant families (ACMG/ACOG frameworks).
- **Secondary prevention:** early molecular diagnosis enables early developmental intervention and timely detection/treatment of seizures, heart defects, immunodeficiency, and pineal lesions.
- **Tertiary prevention:** complication surveillance and management (cardiac, immunologic, neurologic) to reduce morbidity/mortality; proactive monitoring is emphasized following the sudden-infant-death report (PMID 40156274).
- **Counseling specifics:** X-linked recessive recurrence — carrier mothers have 50% transmission to each son (affected) and 50% of daughters are carriers; emphasize residual recurrence risk from **germline mosaicism** even when parental blood testing is negative (PMID 29283210); assess maternal X-inactivation.
- **Immunization / public-health / environmental / behavioral prevention:** not applicable (non-infectious, non-environmental). Routine vaccination is advisable where hypogammaglobulinemia is present (clinical judgment).

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** no naturally occurring UBE2A-deficiency disease is catalogued in companion animals, livestock, or wildlife (OMIA); the disorder is human and experimental-model-based. Not zoonotic or infectious.
- **Orthologous genes (NCBI Gene):** *Saccharomyces cerevisiae* **RAD6/UBC2** (NCBI Gene 851193; taxon 4932); *Drosophila melanogaster* **UbcD6/dUBE2A** (taxon 7227); *Mus musculus* **Ube2a** (NCBI Gene 22209; taxon 10090); human paralog **UBE2B/HR6B** (HGNC:12473).
- **Comparative biology / conservation:** UBE2A is deeply evolutionarily conserved; the C-terminal region truncated in patients is conserved from Drosophila to vertebrates (PMID 16909393), and human HHR6A/HHR6B partially complement the yeast rad6 defect (PMID 8575614) — underpinning the validity of cross-species models.
- **Transmission:** not applicable.

---

## 15. Model Organisms

- **Mouse (Mus musculus; MGI gene Ube2a):** **Ube2a knockout** — major **spatial-learning deficit** and impaired **mGluR-dependent LTD**, with normal basal synaptic transmission, LTP, motor coordination, and (notably) **no epilepsy**; establishes a causal role for UBE2A in learning/memory (Bruinsma 2016, PMID 26476408).
  > *"Ube2a knockout mice have a major deficit in spatial learning tasks, whereas other tested phenotypes, including epilepsy and motor coordination, were normal."* (PMID 26476408)
  - **Paralog model — Ube2b/HR6B knockout:** male infertility with derailed postmeiotic spermatid chromatin condensation (PMID 8797826) and altered synaptonemal-complex structure with ~20–25% increased meiotic crossing-over (PMID 12556476) — illustrating RAD6-family roles in chromatin/meiosis and functional redundancy.
- **Drosophila melanogaster:** **dUBE2A** mutants show impaired synaptic transmission; dUBE2A binds the E3 ligase **Parkin** (mitochondrial function) — modeling the mitochondrial/synaptic arm (reviewed in PMID 26476408).
- **Yeast (S. cerevisiae RAD6):** foundational model for RAD6 biochemistry — post-replication repair, N-end-rule degradation, histone ubiquitination, sporulation; human orthologs partially complement rad6 mutants (PMID 8575614). Structural/mechanistic insight into the Rad6 "backside" β-turn and E3 engagement comes from yeast Rad6 and human UBE2A/UBE2B (PMID 42095445).
- **Cellular/in vitro:** biochemical reconstitution of RAD6A–RAD18–PCNA ubiquitination (PMID 21967848); patient-variant protein-stability/degradation assays (PMID 32415735). No iPSC/organoid disease model is published.
- **Model types available:** constitutive knockout (mouse Ube2a, Ube2b), invertebrate mutants (Drosophila), yeast deletion; **conditional/humanized UBE2A models are not established.**
- **Phenotype recapitulation & limitations:** the mouse Ube2a KO faithfully models the **cognitive/learning** component and pinpoints mGluR-LTD, but **does not reproduce seizures, craniofacial dysmorphism, or systemic malformations** — partly due to redundancy with Ube2b; Drosophila captures the mitochondrial/synaptic arm. Thus models collectively illuminate mechanism (especially synaptic plasticity and mitochondrial/DNA-repair/chromatin functions) but no single model reproduces the full human syndrome.
- **Resources:** MGI (mouse), FlyBase (Drosophila), SGD (yeast), Alliance of Genome Resources.

---

## Supported vs. Refuted Hypotheses

**Supported by evidence:**
- UBE2A loss-of-function is the monogenic cause (all variant classes converge on LoF) — PMID 16909393, 32415735.
- X-linked recessive inheritance with skewed-XCI protection of carrier females — PMID 24053514.
- UBE2A acts as a RAD6 E2 enzyme in PCNA/H2B ubiquitination and Parkin-linked mitochondrial QC — PMID 21967848, 19844166, 26476408.
- Causal role of UBE2A in learning/mGluR-LTD (mouse) — PMID 26476408.
- Genotype–phenotype trend: larger Xq24 deletions → more congenital heart defects — PMID 25287747, 32415735.

**Refuted / not supported:**
- That UBE2A point mutations are a common cause of nonsyndromic XLID — refuted: no UBE2A mutations found in 15 nonsyndromic + 4 syndromic XLID families mapped to the region (PMID 16909393).
- That the mouse KO phenotype includes epilepsy — not supported (epilepsy normal in Ube2a KO; PMID 26476408), indicating species/redundancy differences.
- Environmental or infectious etiology — not applicable/refuted (Mendelian disorder).

---

## Limitations and Future Directions

**Limitations.** (1) Ultra-rare disease (~58 reported males) — frequencies are qualitative; no formal prevalence, survival, or QoL statistics. (2) Evidence is dominated by case reports/small series (potential ascertainment/publication bias toward severe phenotypes). (3) No human omics (transcriptomic/proteomic/metabolomic/single-cell) datasets; mechanistic arms (DNA repair, transcription, mitochondrial) are inferred in patients from model systems. (4) No patient-derived iPSC/organoid models; mouse KO incompletely recapitulates the syndrome.

**Future directions.** Natural-history registries and genotype–phenotype correlation across lesion types; patient iPSC-derived neurons/organoids to test which ubiquitination arm (PCNA repair vs H2B transcription vs Parkin/mitochondria) drives neurodevelopmental dysfunction; targeting mGluR-LTD pharmacologically (as in other NDDs); exploration of gene/enzyme-restoration strategies given the clean LoF mechanism; standardized surveillance protocols (cardiac, immunologic, pineal) following reports of early/sudden death.

---

### Key Ontology Anchors
MONDO:0010461 · OMIM 300860 · ORPHA:447980 · Gene UBE2A HGNC:12472 (UniProt P49459) · HPO: HP:0001419 (X-linked recessive), HP:0010864/HP:0002342 (ID), HP:0001250 (seizures), HP:0000664 (synophrys), HP:0001007 (hirsutism), HP:0003761 (onychodystrophy), HP:0000054 (micropenis), HP:0001627 (CHD) · GO:0061631/GO:0004842, GO:0006301, GO:0033523, GO:0060292 · UBERON:0000955 (brain), UBERON:0002316 (white matter), UBERON:0002097 (skin), UBERON:0001705 (nail), UBERON:0000948 (heart), UBERON:0000989 (penis), UBERON:0001905 (pineal gland) · CL:0000540 (neuron) · GO CC: GO:0005634 (nucleus), GO:0005739 (mitochondrion) · NCIT: C15376, C264, C15329, C98136, C15431, C15709.


## Artifacts

- [OpenScientist final report](final_report.html)
- [OpenScientist final report](final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 13 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:21967848` (3 mentions) - Asymmetric nature of two subunits of RAD18, a RING-type ubiquitin ligase E3, in the human RAD6A-RAD18 ternary complex.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `ube2a`, `disease`, `seizure`, `heart`, `gene`, `deletion`, `defect`, `x-linked`, `genetic`, `type`, `disability`, `xq24`, `male`, `phenotype`, `congenital`, `disorder`, `hypogammaglobulinemia`, `infection`, `intellectual`, `cardiac`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
