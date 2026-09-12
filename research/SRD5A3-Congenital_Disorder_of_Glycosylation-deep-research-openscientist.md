---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T15:28:39.042226'
end_time: '2026-09-01T16:13:36.656894'
duration_seconds: 2697.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SRD5A3-Congenital Disorder of Glycosylation
  mondo_id: ''
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
  path: SRD5A3-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SRD5A3-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SRD5A3-Congenital Disorder of Glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SRD5A3-Congenital Disorder of Glycosylation** covering all of the
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

# SRD5A3-Congenital Disorder of Glycosylation (SRD5A3-CDG): A Comprehensive Disease Characterization Report

**Category:** Mendelian (autosomal recessive inborn error of metabolism)
**Compiled:** 2026-09-01 | Evidence base: primary literature (PMIDs cited inline)

## Summary

**SRD5A3-Congenital Disorder of Glycosylation (SRD5A3-CDG; OMIM #612379; CDG type Iq; Orphanet ORPHA:79320)** is a rare autosomal recessive inborn error of metabolism caused by biallelic loss-of-function variants in *SRD5A3* (steroid 5α-reductase type 3; chromosome 4q12; HGNC:24420; OMIM *611715). The gene encodes **polyprenol reductase**, the enzyme that catalyzes the final, committed step of dolichol biosynthesis — reduction of the α-isoprene unit of polyprenol to form dolichol ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)). Because dolichol is the obligate lipid carrier for the dolichol-linked oligosaccharide (LLO) precursor of protein N-glycosylation, and also anchors glycans used in O-/C-mannosylation and glycosylphosphatidylinositol (GPI) anchor biosynthesis, enzyme deficiency produces a **CDG type I** biochemical defect (hypoglycosylation of nascent glycoproteins) that branches to affect multiple glycosylation pathways at the endoplasmic reticulum (ER) membrane.

Clinically, SRD5A3-CDG is a **congenital multisystem neuro-ophthalmologic-dermatologic disorder**. Its consistent core features are intellectual disability/psychomotor delay, muscular hypotonia, cerebellar ataxia with cerebellar hypoplasia/atrophy, and a characteristic ocular spectrum (congenital nystagmus, optic disc pallor/optic atrophy, early-onset retinal dystrophy, ocular coloboma, cataract), frequently accompanied by ichthyosiform skin/chronic dermatitis. The historically separate **Kahrizi syndrome** (OMIM 612713: intellectual disability, coloboma, cataract, kyphosis) is allelic — indeed the same disorder ([PMID: 20700148](https://pubmed.ncbi.nlm.nih.gov/20700148/)). Adult-onset/progressive features include kyphosis/scoliosis, retinitis pigmentosa, and cataracts ([PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)).

The disorder is **ultrarare**, with roughly 60 cases reported worldwide and approximately 23 distinct pathogenic variants described as of 2022. Diagnosis relies on exome/genome sequencing (including intragenic copy-number analysis) supported by a CDG-I serum transferrin pattern and biochemical demonstration of an elevated polyprenol/dolichol ratio. **No disease-modifying therapy exists**; management is symptomatic and multidisciplinary. Repurposing of the HMG-CoA reductase inhibitor atorvastatin and dietary dolichol supplementation remain experimental. This report synthesizes eight confirmed findings across 35 reviewed papers to populate the disease knowledge-base template.

---

## Key Findings

### Finding 1 — Genetic cause: biallelic loss-of-function *SRD5A3* variants encoding polyprenol reductase

*SRD5A3* (chromosome 4q12; HGNC:24420; OMIM *611715) encodes **polyprenol reductase**, which reduces the α-isoprene unit of polyprenol to form dolichol. Dolichol is the obligate lipid carrier for the dolichol-linked oligosaccharide precursor used in protein N-glycosylation, O-/C-mannosylation, and GPI-anchor synthesis. Biallelic pathogenic variants cause SRD5A3-CDG (a CDG type I disorder; OMIM #612379), inherited in an **autosomal recessive** manner. The seminal functional study established both gene function and disease causation: *"We found that SRD5A3 is necessary for the reduction of the alpha-isoprene unit of polyprenols to form dolichols, required for synthesis of dolichol-linked monosaccharides, and the oligosaccharide precursor used for N-glycosylation"* ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)).

Notably, the same study observed residual dolichol in enzyme-depleted cells: *"The presence of residual dolichol in cells depleted for this enzyme suggests the existence of an unexpected alternative pathway for dolichol de novo biosynthesis"* ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)). This alternative/"detour" pathway — recently shown to be evolutionarily conserved in budding yeast ([PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)) — explains why patients retain partial glycosylation capacity despite null variants and likely accounts for survival compatible with life in this disorder.

### Finding 2 — Core clinical phenotype: neurodevelopmental, ophthalmologic, cerebellar, and cutaneous involvement

Across independent patient cohorts, SRD5A3-CDG presents a recognizable multisystem picture: intellectual disability/psychomotor delay, muscular hypotonia, cerebellar ataxia with cerebellar hypoplasia/atrophy, congenital nystagmus, optic disc pallor/optic atrophy, early-onset retinal dystrophy, ocular coloboma, cataract, and ichthyosiform skin/chronic dermatitis. A concise clinical summary describes *"a severe metabolic disease manifesting as muscle hypotonia, developmental delay, cerebellar ataxia and ocular symptoms; typically, nystagmus and optic disc pallor"* ([PMID: 31638560](https://pubmed.ncbi.nlm.nih.gov/31638560/)).

The **ocular phenotype** is a prominent and often presenting feature, with *"early-onset retinal dystrophy as a primary manifestation"* ([PMID: 28253385](https://pubmed.ncbi.nlm.nih.gov/28253385/)). The allelic **Kahrizi syndrome** highlights the coloboma-cataract-kyphosis axis: *"a novel syndrome consisting of mental retardation, coloboma, cataract and kyphosis (Kahrizi syndrome, OMIM 612713)"* ([PMID: 20700148](https://pubmed.ncbi.nlm.nih.gov/20700148/)). Phenotypic diversity is real: monozygotic twins have been reported with early-infancy generalized tonic-clonic seizures (a less common feature) yet entirely normal brain MRI at 20 months, demonstrating that the characteristic cerebellar structural anomalies may be absent early in life ([PMID: 41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/)).

**Suggested HPO terms:** HP:0001249 (Intellectual disability), HP:0001252 (Hypotonia), HP:0001251 (Ataxia), HP:0001321 (Cerebellar hypoplasia), HP:0000639 (Nystagmus), HP:0000648 (Optic atrophy), HP:0000556 (Retinal dystrophy), HP:0000589 (Coloboma), HP:0000518 (Cataract), HP:0008064 (Ichthyosis), HP:0002650 (Scoliosis), HP:0002808 (Kyphosis), HP:0001250 (Seizure).

### Finding 3 — Biochemical signature: extensive serum hypoglycosylation, elevated polyprenol/dolichol ratio, CDG-I transferrin pattern

Patient fibroblasts exhibit a **high polyprenol/dolichol ratio with normal dolichol amounts**, the biochemical fingerprint of the enzyme defect: *"Quantification of dolichol and unreduced polyprenol in the patient's fibroblasts demonstrated a high polyprenol/dolichol ratio with normal amounts of dolichol"* ([PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/)). Serum transferrin isoelectric focusing shows a **CDG type I** pattern, though a caveat exists — up to ~70% of transferrin may be correctly glycosylated in some patients, so screening can be falsely reassuring, and transferrin protein variants can further confound interpretation (as documented in PMM2-CDG, [PMID: 37876147](https://pubmed.ncbi.nlm.nih.gov/37876147/)).

Quantitative serum N-glycoproteomics reveals the breadth of the defect: *"Extensive hypoglycosylation of serum proteins was observed in patients, with 245 of 291 altered glycopeptides decreased in SRD5A3-CDG"* ([PMID: 41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/)), affecting haptoglobin, plasma serine protease inhibitor, alpha-1-B glycoprotein, alpha-2-macroglobulin, ceruloplasmin, and albumin (including at non-canonical sites). Albumin-derived glycopeptides are emerging as diagnostic biomarkers across CDG subtypes including SRD5A3-CDG ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/)). Molecular diagnosis is confirmed by exome/genome sequencing **with intragenic copy-number analysis**, because structural variants occur: *"we identified as a second compound heterozygous variant a previously not reported tandem duplication of exons 2-4 in SRD5A3"* ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/)).

### Finding 4 — No disease-modifying therapy; symptomatic management with atorvastatin repurposing under investigation

With ~60 reported cases, treatment is limited to **symptomatic/supportive management**: developmental therapies, ophthalmologic and orthopedic care, and seizure control. A recent study developed the first high-throughput disease models and reported repurposing of the HMG-CoA reductase inhibitor **atorvastatin** as an experimental therapeutic strategy: *"Approximately 60 cases have been reported, with treatment limited to symptomatic management"* ([PMID: 41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/)). Dietary **dolichol supplementation** has been proposed conceptually, supported by plant polyprenol-reductase rescue experiments (Finding 5). A broad 2024 CDG treatment overview reinforces that most CDG remain symptomatically managed: *"Mostly, we are only able to manage the disease symptoms rather than to address the underlying cause"* ([PMID: 39236565](https://pubmed.ncbi.nlm.nih.gov/39236565/)), while noting that *"Innovative therapies, targeting both the root cause and resulting manifestations, have transitioned from the research stage to practical application"* for some subtypes (e.g., dietary sugar therapies in MPI-, PGM1-, and PMM2-CDG).

### Finding 5 — Evolutionary conservation: plant/yeast models recapitulate the defect and dolichol rescues it

The polyprenol-to-dolichol reduction step is deeply conserved. *Arabidopsis thaliana* orthologs PPRD1 and PPRD2 encode polyprenol reductases: *"which are orthologous to human SRD5A3 (steroid 5α reductase type 3) and encode polyprenol reductases responsible for conversion of polyprenol to dolichol in Arabidopsis thaliana"* ([PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)). PPRD2 deficiency is lethal (male sterility) and is **partially rescued by dolichol**: *"Shortage of dolichol in PPRD2-deficient cells is partially rescued by PPRD1 overexpression or by supplementation with dolichol"* ([PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)), implicating impaired protein glycosylation as the major underlying factor. The conserved dolichol biosynthesis "detour" pathway in budding yeast ([PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)) provides an additional tractable model system. These conserved systems provide the mechanistic rationale for dietary dolichol supplementation as a conceptual therapeutic avenue.

### Finding 6 — Ultrarare disorder with variable expressivity, adult-onset progression, and founder alleles

Fewer than ~60 cases have been reported worldwide, with ~23 distinct variants known by 2022: *"So far, only 23 distinct mutations were described"* ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/)). Inheritance is autosomal recessive with high representation of **consanguineous families** and population **founder alleles** (e.g., p.Gln96delinsX in Baluchi/South Asian families). Expressivity is variable even for recurrent alleles: *"Homozygosity for the SRDA3 deletion p.Gln96delinsX is not always associated with ocular coloboma"* ([PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/)). Comparison of children and adults with *SRD5A3* mutations delineated progressive/adult-onset features: *"allowing us to delineate the features that may develop over time with this disorder including kyphosis, retinitis pigmentosa, and cataracts"* ([PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)). In the 280-patient FCDGC natural history cohort, dolichol-metabolism disorders (which include SRD5A3-CDG) comprised ~5% of participants ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).

### Finding 7 — Mechanism: dolichol deficiency impairs multiple ER glycosylation pathways

SRD5A3-derived dolichol is required for synthesis of dolichol-linked monosaccharides and the oligosaccharide precursor (**Glc3Man9GlcNAc2-PP-dolichol**) assembled in the ER during the dolichol cycle: *"required for synthesis of dolichol-linked monosaccharides, and the oligosaccharide precursor used for N-glycosylation"* ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)). Dolichyl-phosphate (Dol-P) is a **rate-limiting intermediate** of N-glycosylation and is recycled to the cytoplasmic ER leaflet after cleavage of dolichyl pyrophosphate: *"During protein N-glycosylation, dolichyl pyrophosphate (Dol-P-P) is discharged in the lumenal monolayer of the endoplasmic reticulum (ER)"* ([PMID: 18077451](https://pubmed.ncbi.nlm.nih.gov/18077451/)). Because dolichol also anchors glycans in O-/C-mannosylation and GPI-anchor biosynthesis, the deficiency produces a CDG type I biochemical defect (hypoglycosylation of nascent proteins) that **branches** to impair those pathways as well.

### Finding 8 — CDG therapy is largely symptomatic; no established SRD5A3-specific therapy and no isolated mouse disease model

A 2024 overview (Quelhas & Jaeken) confirms that available CDG treatment options remain limited and mostly symptomatic, though targeted root-cause therapies have recently reached practice for some subtypes ([PMID: 39236565](https://pubmed.ncbi.nlm.nih.gov/39236565/)). For SRD5A3-CDG specifically, no disease-specific therapy is established; atorvastatin repurposing is experimental. A key **model-organism gap** exists: no isolated *Srd5a3*-knockout mouse disease model has been characterized — a mouse ~1.2 Mb 5qC3.3 deletion encompassing *Srd5a3* caused peri-implantation lethality attributable to *Exoc1*, not *Srd5a3*: *"deletion of a > 1.2-Mb genomic region containing nine genes (Kit, Kdr, Srd5a3, Tmeme165, Clock, Pdcl2, Nmu, Exoc1, and Cep135)"* ([PMID: 26346620](https://pubmed.ncbi.nlm.nih.gov/26346620/)).

---

## Detailed Section-by-Section Report

### 1. Disease Information

**Overview.** SRD5A3-CDG is an autosomal recessive congenital disorder of glycosylation of the dolichol-metabolism subgroup. Dysfunction of polyprenol reductase blocks the terminal step of dolichol synthesis, reducing availability of the LLO precursor required for protein N-glycosylation and impairing other dolichol-dependent glycan pathways, producing a congenital multisystem disorder dominated by neurodevelopmental, cerebellar, ophthalmologic, and cutaneous features.

**Key identifiers:**
- **OMIM (disease):** #612379 (Congenital disorder of glycosylation, type Iq)
- **OMIM (allelic):** #612713 (Kahrizi syndrome)
- **OMIM (gene):** *611715 (*SRD5A3*)
- **Orphanet:** ORPHA:79320 (SRD5A3-CDG)
- **Gene / HGNC:** *SRD5A3* / HGNC:24420
- **Chromosome:** 4q12
- **Suggested MONDO:** MONDO:0012997 (congenital disorder of glycosylation, type Iq) — verify against current MONDO release
- **ICD-10:** E77.8 (other disorders of glycoprotein metabolism); **ICD-11:** 5C51.1 (disorders of protein glycosylation) — subtype-level codes are not disease-specific
- **MeSH:** Congenital Disorders of Glycosylation (D018981) — no SRD5A3-specific descriptor

**Synonyms / alternative names:** SRD5A3-CDG; CDG type Iq (CDG-Iq); steroid 5α-reductase type 3 deficiency; polyprenol reductase deficiency; Kahrizi syndrome (allelic); congenital disorder of glycosylation with intellectual disability, coloboma, cataract and kyphosis.

**Information source type.** Disease-level knowledge derives predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and from **published individual/small-cohort case reports and case series** plus the multicenter FCDGC natural history study — not from large EHR datasets, consistent with ultrarare-disease evidence.

### 2. Etiology

**Causal factors — genetic.** SRD5A3-CDG is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *SRD5A3*** ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)). There is no environmental or infectious cause.

**Genetic risk factors.** The only risk factor is inheritance of two pathogenic *SRD5A3* alleles. **Consanguinity** substantially increases risk (many cases arise in consanguineous families), and **founder alleles** exist in specific populations (e.g., p.Gln96delinsX in Baluchi/South Asian families; [PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/)).

**Environmental risk factors / protective factors / gene-environment interactions.** **Not applicable** — as a Mendelian metabolic disorder, no established environmental risk, protective, or gene-environment interaction factors have been reported. No genetic modifier or protective alleles have been defined, though the conserved dolichol "detour"/alternative biosynthesis pathway ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/); [PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)) likely modulates residual glycosylation capacity and phenotypic severity.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Intellectual disability / psychomotor delay | Cognitive/developmental | Congenital/infantile | Very frequent (near-universal) | HP:0001249 |
| Muscular hypotonia | Clinical sign | Neonatal/infantile | Very frequent | HP:0001252 |
| Cerebellar ataxia | Neurological sign | Infantile/childhood | Frequent | HP:0001251 |
| Cerebellar hypoplasia/atrophy | Imaging/structural | Congenital (may be absent early) | Frequent | HP:0001321 / HP:0001272 |
| Congenital nystagmus | Ophthalmologic sign | Congenital/infantile | Frequent | HP:0000639 |
| Optic disc pallor / optic atrophy | Ophthalmologic sign | Infantile | Frequent | HP:0000648 |
| Early-onset retinal dystrophy | Ophthalmologic | Early childhood | Frequent (can be presenting) | HP:0000556 |
| Ocular coloboma | Physical malformation | Congenital | Variable | HP:0000589 |
| Cataract | Ophthalmologic | Congenital→adult | Variable/progressive | HP:0000518 |
| Ichthyosiform skin / chronic dermatitis | Cutaneous | Infantile | Frequent | HP:0008064 |
| Kyphosis / scoliosis | Skeletal | Adult-onset/progressive | Variable | HP:0002808 / HP:0002650 |
| Retinitis pigmentosa | Ophthalmologic | Adult-onset/progressive | Variable | HP:0000510 |
| Seizures (incl. GTCS) | Neurological | Variable (can be early) | Less common | HP:0001250 |

**Onset, severity, progression.** Most features are **congenital or infantile-onset**. Severity is **variable** (mild to severe), and expressivity varies even for identical genotypes ([PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/)). The neurodevelopmental deficit is generally **stable/non-degenerative** in its cognitive component, while several features are **progressive** (kyphosis, retinitis pigmentosa, cataracts; [PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)). Structural cerebellar findings may be **absent in the first years** despite prominent neurological symptoms ([PMID: 41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/)).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36/PROMIS data exist for SRD5A3-CDG. By extrapolation from CDG cohorts, the combination of intellectual disability, ataxia, and visual impairment causes substantial dependency and impaired daily functioning; the FCDGC cohort found 100% of participants had developmental differences and high burdens of neurologic, GI/liver, and musculoskeletal involvement ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).

### 4. Genetic / Molecular Information

**Causal gene.** *SRD5A3* (HGNC:24420; OMIM *611715; chromosome 4q12), encoding polyprenol reductase (UniProt Q9H8P0). Loss of function is the disease mechanism ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)).

**Pathogenic variants.** Approximately **23 distinct variants** were described by 2022 ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/)). Reported variant classes include:
- **Frameshift** (e.g., the homozygous frameshift in the original Kahrizi-syndrome family; [PMID: 20700148](https://pubmed.ncbi.nlm.nih.gov/20700148/))
- **Nonsense** (e.g., c.57G>A, p.Trp19Ter, ACMG-pathogenic; [PMID: 41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/))
- **Missense** (e.g., c.509A>G, p.Tyr170Cys, likely pathogenic; [PMID: 41667393](https://pubmed.ncbi.nlm.nih.gov/41667393/))
- **In-frame deletion/indel** founder allele (p.Gln96delinsX; [PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/))
- **Intragenic structural variants** — a tandem duplication of exons 2–4 ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/))

**ACMG/AMP classification.** Reported variants are predominantly **pathogenic or likely pathogenic**, consistent with the broader FCDGC cohort in which most CDG variants were classified pathogenic/likely pathogenic ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)). **Allele frequencies** in gnomAD are very low (consistent with an ultrarare recessive disorder); founder alleles are enriched in specific populations.

**Origin and functional consequence.** Variants are **germline**; there is no somatic component. Functional consequence is **loss of function** (reduced/absent polyprenol reductase activity → impaired dolichol synthesis).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes or epigenetic mechanisms have been reported. The conserved alternative dolichol biosynthesis pathway is a candidate biological modifier of residual glycosylation ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/); [PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)). No characteristic large-scale chromosomal abnormalities are associated, though intragenic copy-number changes must be sought ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/)).

### 5. Environmental Information

**Not applicable.** SRD5A3-CDG is a purely genetic Mendelian disorder. No environmental toxins, lifestyle factors, or infectious agents cause or trigger the disease. (Of note, the DPMS/dolichol-phosphate-mannose pathway is a host dependency factor for flaviviruses such as dengue/Zika [PMID: 31915280](https://pubmed.ncbi.nlm.nih.gov/31915280/), but this concerns viral biology, not SRD5A3-CDG etiology.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in *SRD5A3*** reduce/abolish **polyprenol reductase** activity. *(demonstrated; [PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/))*
2. Loss of enzyme activity **prevents reduction of the α-isoprene unit of polyprenol**, so polyprenol accumulates and **dolichol formation is impaired** → elevated polyprenol/dolichol ratio in cells. *(demonstrated; [PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/))*
3. Reduced dolichol/dolichyl-phosphate **limits synthesis of dolichol-linked monosaccharides and the LLO precursor Glc3Man9GlcNAc2-PP-dolichol** in the ER (Dol-P is rate-limiting). *(demonstrated; [PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/); [PMID: 18077451](https://pubmed.ncbi.nlm.nih.gov/18077451/))*
4. Deficient LLO precursor **leads to protein N-hypoglycosylation** (a CDG type I defect) — extensive across serum glycoproteins. *(demonstrated; [PMID: 41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/))*
   - **Branch 4a:** Reduced dolichol-anchored glycan donors also **impair O-/C-mannosylation and GPI-anchor biosynthesis**. *(inferred from shared dolichol dependency; [PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/); [PMID: 40902550](https://pubmed.ncbi.nlm.nih.gov/40902550/))*
5. Widespread hypoglycosylation **disrupts glycoprotein folding, stability, trafficking, and function** across many tissues. *(inferred; general glycoprotein quality-control biology, [PMID: 10794707](https://pubmed.ncbi.nlm.nih.gov/10794707/))*
6. Tissue-level dysfunction — most sensitively in **developing brain/cerebellum, retina/eye, and skin** — **results in** the clinical phenotype: intellectual disability, hypotonia, cerebellar ataxia/hypoplasia, the ocular spectrum, and ichthyosis. *(clinical correlation; [PMID: 31638560](https://pubmed.ncbi.nlm.nih.gov/31638560/))*
   - **Branch 6a (residual pathway):** A conserved alternative dolichol biosynthesis pathway supplies residual dolichol, **mitigating severity** and explaining survival and partial glycosylation. *(inferred/demonstrated in models; [PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/); [PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/))*

**ASCII pathway diagram:**

```
 SRD5A3 biallelic LoF
        │ (loss of polyprenol reductase activity)
        ▼
 Polyprenol NOT reduced ──► ↑ polyprenol/dolichol ratio
        │ (dolichol/Dol-P deficient)
        ▼
 ↓ Dolichol-linked monosaccharides + LLO (Glc3Man9GlcNAc2-PP-Dol)  [ER membrane]
        │
        ├──► ↓ N-glycosylation (CDG type I)  ──► serum protein hypoglycosylation
        ├──► ↓ O-/C-mannosylation (branch, inferred)
        └──► ↓ GPI-anchor synthesis (branch, inferred)
                    │
                    ▼
        Glycoprotein misfolding / dysfunction (multi-tissue)
                    │
        ┌───────────┼───────────────┬─────────────┐
        ▼           ▼               ▼             ▼
   Brain/cerebellum  Eye/retina    Skin        Skeleton (progressive)
   ID, hypotonia,    nystagmus,    ichthyosis  kyphosis/scoliosis
   ataxia, hypoplasia optic atrophy,
                     retinal dystrophy,
                     coloboma, cataract
```

**Molecular pathway / cellular process / compartment.** The defect is in **dolichol biosynthesis** feeding the **protein N-glycosylation (dolichol) cycle** at the **ER membrane**. Key GO terms: GO:0019408 (dolichol biosynthetic process), GO:0006486 (protein glycosylation), GO:0006487 (protein N-linked glycosylation), GO:0006506 (GPI anchor biosynthetic process), GO:0035269 (protein O-linked mannosylation). Cellular compartment: GO:0005789 (endoplasmic reticulum membrane), GO:0005783 (endoplasmic reticulum). Enzyme activity: polyprenol reductase (EC 1.3.1.94).

**Metabolic changes.** Isoprenoid/dolichol lipid metabolism is directly disrupted (elevated polyprenol, relatively preserved absolute dolichol via the detour pathway). **Immune involvement** is not a primary feature of SRD5A3-CDG (unlike immune-relevant CDG such as MOGS-, PGM3-, VPS13B-CDG). **Molecular profiling** to date is dominated by serum N-glycoproteomics showing broad hypoglycosylation ([PMID: 41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/)); a GTEx in-silico study noted that tissue vulnerability in CDG does not simply track baseline gene expression ([PMID: 42472049](https://pubmed.ncbi.nlm.nih.gov/42472049/)).

**Cell types (suggested CL terms):** cerebellar Purkinje cell (CL:0000121), photoreceptor cell (CL:0000210), keratinocyte (CL:0000312). **Suggested CHEBI:** polyprenol (CHEBI:26250), dolichol (CHEBI:23514), dolichyl phosphate (Dol-P), dolichyl diphosphate.

### 7. Anatomical Structures Affected

- **Primary organs/systems:** central nervous system, especially **cerebellum** (UBERON:0002037) and cerebrum; **eye/retina** (UBERON:0000970 / retina UBERON:0000966, optic nerve UBERON:0000941); **skin** (UBERON:0002097).
- **Secondary/progressive involvement:** **skeleton/spine** (kyphosis, scoliosis; vertebral column UBERON:0002415).
- **Body systems:** nervous, ophthalmic/sensory, integumentary, musculoskeletal.
- **Tissue/cell level:** neural tissue (cerebellar neurons incl. Purkinje cells), retinal photoreceptors, epidermal keratinocytes.
- **Subcellular level:** **endoplasmic reticulum membrane** (site of the dolichol cycle; GO:0005789) is the primary affected compartment.
- **Lateralization:** manifestations are typically **bilateral/generalized** (e.g., bilateral nystagmus, bilateral optic atrophy, symmetric cerebellar involvement).

### 8. Temporal Development

- **Onset:** **Congenital / neonatal-infantile**, with hypotonia, nystagmus, and developmental delay evident early; onset pattern is **chronic/insidious**.
- **Progression:** The cognitive deficit is broadly **static**, while specific features are **progressive** — kyphosis, retinitis pigmentosa, and cataracts develop or worsen over time ([PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)). Cerebellar structural changes may **appear or become detectable later**, being absent on early MRI in some infants ([PMID: 41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/)).
- **Course/duration:** **Chronic, lifelong.** No spontaneous remission. **Critical period:** early childhood neurodevelopment is the key window for supportive/early-intervention therapies; any future disease-modifying therapy would presumably need early initiation.

### 9. Inheritance and Population

- **Epidemiology:** Ultrarare; **~60 cases reported worldwide**; precise prevalence/incidence are unavailable (well under Orphanet's rare-disease threshold). Dolichol-metabolism disorders were ~5% of the 280-patient FCDGC natural history cohort ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).
- **Inheritance:** **Autosomal recessive** ([PMID: 20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/)).
- **Penetrance:** Complete for biallelic LoF (all reported biallelic carriers are affected), with **variable expressivity** ([PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/)).
- **Anticipation / germline mosaicism:** Not applicable/not reported (non-repeat-expansion disorder).
- **Founder effects / consanguinity:** Documented — p.Gln96delinsX founder allele in Baluchi/South Asian families; frequent consanguinity ([PMID: 30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/)).
- **Carrier frequency:** Not precisely established; expected very low given rarity.
- **Sex ratio:** ~1:1 (autosomal); no sex predilection. In the FCDGC cohort overall, sexes were roughly balanced ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).
- **Geographic distribution:** Cases reported across diverse populations (European, South Asian, Middle Eastern, Egyptian, etc.); founder alleles create regional clustering.

### 10. Diagnostics

**Recommended approach.** Diagnosis is genetic-first in the modern setting: **exome or genome sequencing** including **intragenic copy-number/structural-variant analysis** ([PMID: 35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/)), supported by biochemical screening.

**Laboratory / biochemical tests:**
- **Serum transferrin isoelectric focusing / CDT analysis** → **CDG type I** pattern. Caveat: can be **falsely reassuring** (substantial correctly glycosylated transferrin in some patients) and confounded by transferrin protein variants ([PMID: 37876147](https://pubmed.ncbi.nlm.nih.gov/37876147/)).
- **Polyprenol/dolichol ratio** in fibroblasts (elevated) — biochemical confirmation of the enzyme defect ([PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/)).
- **Serum N-glycoproteomics** demonstrating extensive hypoglycosylation ([PMID: 41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/)); **albumin glycopeptides** as emerging biomarkers ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/)).

**Imaging / functional / electrophysiology:** Brain **MRI** (cerebellar hypoplasia/atrophy — may be normal early); ophthalmologic evaluation with **fundus photography, autofluorescence, and electroretinogram (ERG)** for retinal dystrophy ([PMID: 41667393](https://pubmed.ncbi.nlm.nih.gov/41667393/)).

**Genetic testing modalities:** WES and WGS are the highest-yield tools; targeted CDG gene panels including *SRD5A3*; single-gene *SRD5A3* testing (incl. deletion/duplication analysis). Karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not applicable**.

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist; diagnosis rests on the phenotype + CDG-I biochemistry + biallelic *SRD5A3* variants. **Differential diagnosis** includes other CDG type I subtypes (notably **PMM2-CDG**, the most common), other dolichol-pathway CDG (**DHDDS-, DPM1/3-, SRD5A3-**), Leber congenital amaurosis/early-onset retinal dystrophies, and cerebellar hypoplasia syndromes; distinguishing features are the specific combination of retinal dystrophy, coloboma/cataract, ichthyosis, and the elevated polyprenol/dolichol ratio.

**Screening.** No newborn screening exists for SRD5A3-CDG. Carrier and cascade testing are appropriate in known families.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics; the disorder is **chronic and compatible with survival into adulthood** (adult patients are described; [PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)), consistent with residual glycosylation via the alternative dolichol pathway. Severe early presentations (e.g., seizures) can occur ([PMID: 41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/)).
- **Morbidity/disability:** Substantial and lifelong — intellectual disability, ataxia, and progressive visual loss drive major functional impairment and dependency.
- **Complications/progression:** Progressive kyphosis/scoliosis, retinitis pigmentosa, and cataracts ([PMID: 27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/)); seizures in a minority.
- **Prognostic factors:** Genotype (null vs hypomorphic), residual enzyme/dolichol pathway activity, and severity of neurodevelopmental involvement are the main determinants; validated prognostic biomarkers are not established. The Nijmegen Progression CDG Rating Scale (NPCRS) is used across CDG to grade severity ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).

### 12. Treatment

**No disease-modifying therapy is established.** Management is **symptomatic and multidisciplinary** ([PMID: 41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/); [PMID: 39236565](https://pubmed.ncbi.nlm.nih.gov/39236565/)):
- **Neurodevelopmental:** early intervention, physical/occupational/speech therapy (NCIT: Rehabilitation Therapy).
- **Ophthalmologic:** low-vision support, cataract surgery as indicated (NCIT: Cataract Surgery).
- **Orthopedic:** management of kyphosis/scoliosis.
- **Seizure control:** standard antiseizure medications (e.g., levetiracetam is effective in related CDG; [PMID: 37955240](https://pubmed.ncbi.nlm.nih.gov/37955240/)) (NCIT: Levetiracetam).

**Experimental / investigational:**
- **Atorvastatin repurposing** (HMG-CoA reductase inhibitor) — reported as an experimental strategy in newly developed high-throughput SRD5A3-CDG models ([PMID: 41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/)). NCIT: Atorvastatin Calcium (C29014).
- **Dietary dolichol supplementation** — conceptual, supported by dolichol rescue in plant PPRD2-deficient models ([PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)).
- **Cross-CDG precedents for root-cause "sugar" therapies** (not yet demonstrated for SRD5A3-CDG): D-galactose in PGM1-CDG ([PMID: 41182978](https://pubmed.ncbi.nlm.nih.gov/41182978/)), oral mannose in MPI-CDG, and epalrestat (aldose reductase inhibitor) in PMM2-CDG ([PMID: 34652821](https://pubmed.ncbi.nlm.nih.gov/34652821/)) illustrate the emerging targeted-therapy landscape ([PMID: 39236565](https://pubmed.ncbi.nlm.nih.gov/39236565/)).

**Pharmacogenomics, gene/cell/RNA therapy, immunotherapy, surgery-as-cure:** No SRD5A3-specific advanced therapeutics exist; these remain future directions.

### 13. Prevention

- **Primary prevention:** Not applicable at the population level (genetic disease). **Genetic counseling** for at-risk families, carrier testing, and reproductive options (prenatal diagnosis, preimplantation genetic testing) are the principal preventive tools, especially in consanguineous families and founder-allele populations.
- **Secondary prevention:** No population newborn screen; **cascade testing** in known families enables early diagnosis and supportive intervention.
- **Tertiary prevention:** Proactive surveillance and management of progressive complications (vision, spine, seizures) to reduce morbidity.
- **Immunization / public-health / environmental interventions:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** The polyprenol→dolichol reduction step is deeply conserved. Human *SRD5A3* has orthologs in *Arabidopsis thaliana* (**PPRD1, PPRD2**; [PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)) and in **budding yeast** (*Saccharomyces cerevisiae*), where the three-step dolichol "detour" pathway is conserved ([PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)). Mouse ortholog: *Srd5a3* ([PMID: 26346620](https://pubmed.ncbi.nlm.nih.gov/26346620/)).
- **Natural/veterinary disease:** No naturally occurring SRD5A3-CDG has been reported in companion animals or wildlife (no OMIA entry identified in this investigation).
- **Comparative biology:** The conservation of the enzyme and the dolichol-rescue phenotype (PPRD2-deficient plants rescued by dolichol) indicates a conserved mechanism linking dolichol supply to protein glycosylation across kingdoms ([PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)).
- **Transmission / zoonosis:** Not applicable.

### 15. Model Organisms

| Model | Type | Utility / recapitulation | Reference |
|---|---|---|---|
| *Arabidopsis thaliana* pprd2 | Plant genetic | Lethal (male sterility); dolichol shortage; **rescued by dolichol supplementation** — establishes causal role of dolichol/glycosylation | [PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/) |
| *S. cerevisiae* (dolichol detour pathway) | Yeast | Confirms conserved alternative dolichol biosynthesis; tractable for pathway dissection | [PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/) |
| Patient fibroblasts | In vitro (human) | Elevated polyprenol/dolichol ratio; hypoglycosylation — core biochemical model | [PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/) |
| High-throughput SRD5A3-CDG disease models | In vitro (recent) | Enabled atorvastatin repurposing screen | [PMID: 41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/) |
| Mouse *Srd5a3* | Mammalian | **Gap:** no isolated *Srd5a3*-null disease model characterized; a ~1.2 Mb 5qC3.3 deletion including *Srd5a3* caused peri-implantation lethality attributable to *Exoc1*, not *Srd5a3* | [PMID: 26346620](https://pubmed.ncbi.nlm.nih.gov/26346620/) |

**Model limitations.** Plant/yeast models capture the enzymatic and glycosylation defect but not the mammalian neuro-ophthalmologic phenotype. The absence of a validated isolated *Srd5a3*-knockout mouse model is a major gap for preclinical therapeutic testing.

---

## Mechanistic Model / Interpretation

SRD5A3-CDG is best understood as a **substrate-supply failure in the dolichol cycle**. The single enzymatic lesion (polyprenol reductase deficiency) sits **upstream** of the entire dolichol-dependent glycosylation machinery. Its immediate, demonstrated consequence is an **elevated polyprenol/dolichol ratio** — polyprenol accumulates because it cannot be reduced, while absolute dolichol is partly preserved by a conserved **alternative/detour biosynthesis pathway**. This residual dolichol is mechanistically important: it explains both the survival of patients (versus embryonic lethality expected from total glycosylation failure) and the observation of substantial correctly glycosylated transferrin in some patients.

**Downstream**, dolichyl-phosphate limitation throttles assembly of the LLO precursor, producing broad **protein N-hypoglycosylation** (demonstrated by serum glycoproteomics: 245/291 altered glycopeptides decreased). Because dolichol is a shared currency, the defect **branches** to O-/C-mannosylation and GPI-anchor synthesis (inferred). The tissue selectivity of the clinical phenotype — brain/cerebellum, eye/retina, skin — reflects the particular sensitivity of these developing tissues to glycoprotein dysfunction rather than tissue-specific enzyme expression (GTEx analysis found baseline expression does not predict CDG tissue vulnerability). The temporal profile (congenital onset with later-emerging kyphosis, retinitis pigmentosa, cataracts) suggests both a **developmental** component (cerebellar hypoplasia, coloboma) and a slowly **progressive/degenerative** component (retinal, lens, skeletal).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [20637498](https://pubmed.ncbi.nlm.nih.gov/20637498/) | *SRD5A3 required for polyprenol→dolichol; mutated in CDG* | F001, F007 — gene function, disease causation, residual pathway |
| [22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/) | *Life with too much polyprenol* | F003 — elevated polyprenol/dolichol ratio biomarker |
| [41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/) | *Extensive hypoglycosylation of serum N-glycoproteins* | F003 — 245/291 glycopeptides decreased |
| [35339718](https://pubmed.ncbi.nlm.nih.gov/35339718/) | *SRD5A3-CDG: intragenic tandem duplication* | F003, F006 — CNV diagnosis; ~23 variants |
| [20700148](https://pubmed.ncbi.nlm.nih.gov/20700148/) | *Kahrizi syndrome frameshift in SRD5A3* | F002 — allelic Kahrizi phenotype |
| [31638560](https://pubmed.ncbi.nlm.nih.gov/31638560/) | *Review of SRD5A3 variants and ocular findings* | F002 — core clinical features |
| [28253385](https://pubmed.ncbi.nlm.nih.gov/28253385/) | *SRD5A3-CDG with early-onset retinal dystrophy* | F002 — retinal dystrophy as presenting feature |
| [27480077](https://pubmed.ncbi.nlm.nih.gov/27480077/) | *SRD5A3-CDG adult-onset features* | F006 — progressive kyphosis, RP, cataracts |
| [30019980](https://pubmed.ncbi.nlm.nih.gov/30019980/) | *Undiagnosed SRD5A3-CDG girl* | F006 — founder allele, variable expressivity |
| [26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/) | *Arabidopsis PPRD2 deficiency* | F005 — orthology, dolichol rescue |
| [42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/) | *Dolichol detour pathway conserved in yeast* | F001, F005 — conserved alternative pathway |
| [18077451](https://pubmed.ncbi.nlm.nih.gov/18077451/) | *Recycling of dolichyl monophosphate* | F007 — ER dolichol cycle, Dol-P recycling |
| [41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/) | *Repurposing atorvastatin for SRD5A3-CDG* | F004 — ~60 cases; experimental therapy |
| [39236565](https://pubmed.ncbi.nlm.nih.gov/39236565/) | *Treatment of CDG: an overview* | F004, F008 — symptomatic care; emerging targeted therapies |
| [26346620](https://pubmed.ncbi.nlm.nih.gov/26346620/) | *Peri-implantation lethality on 5qC3.3* | F008 — mouse model gap (Exoc1, not Srd5a3) |
| [38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/) | *FCDGC natural history cohort (n=280)* | Epidemiology — dolichol disorders ~5%; NPCRS |
| [41769439](https://pubmed.ncbi.nlm.nih.gov/41769439/) | *Monozygotic twins, SRD5A3-CDG* | Phenotype diversity; normal early MRI; nonsense variant |
| [41667393](https://pubmed.ncbi.nlm.nih.gov/41667393/) | *Egyptian SRD5A3-CDG patient* | Missense p.Tyr170Cys; ERG diagnostics |
| [41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/) | *Albumin as a glycoprotein biomarker in CDG* | Emerging albumin glycopeptide biomarker |
| [37876147](https://pubmed.ncbi.nlm.nih.gov/37876147/) | *Misleading transferrin variants in CDG* | Diagnostic caveat for transferrin screening |
| [34652821](https://pubmed.ncbi.nlm.nih.gov/34652821/) | *Epalrestat/sorbitol in PMM2-CDG* | Cross-CDG targeted-therapy precedent |
| [41182978](https://pubmed.ncbi.nlm.nih.gov/41182978/) | *D-galactose in PGM1-CDG* | Cross-CDG dietary-sugar precedent |
| [40902550](https://pubmed.ncbi.nlm.nih.gov/40902550/) | *Genetic disorders of dolichol synthesis and utilization* | Review — dolichol pathway/CDG classification |

**Evidence source types:** The evidence base is predominantly **human clinical** (case reports, case series, natural history cohort) and **in vitro** (patient fibroblasts, glycoproteomics), complemented by **model-organism** work in plants and yeast. There are **no** large randomized trials, no validated mammalian in-vivo disease model, and no computational/GWAS studies relevant to this Mendelian disorder.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** With ~60 cases, all clinical claims derive from case reports/series and one natural history cohort; frequencies are qualitative, and formal prevalence/incidence, survival, and QoL metrics are unavailable.
2. **No validated mammalian disease model.** The absence of a characterized isolated *Srd5a3*-knockout mouse ([PMID: 26346620](https://pubmed.ncbi.nlm.nih.gov/26346620/)) hampers mechanistic and preclinical therapeutic studies.
3. **Branch mechanisms inferred.** Impairment of O-/C-mannosylation and GPI-anchor synthesis is inferred from shared dolichol dependency rather than directly demonstrated in SRD5A3-CDG patients.
4. **Diagnostic pitfalls.** Transferrin-based screening can be falsely reassuring; intragenic CNVs require dedicated analysis — both risk under-/mis-diagnosis.
5. **No proven therapy.** Atorvastatin repurposing and dolichol supplementation are experimental; no clinical efficacy data exist for SRD5A3-CDG.
6. **Genotype–phenotype correlation is weak.** Variable expressivity (even for identical alleles) is unexplained; modifier genes and the quantitative contribution of the alternative dolichol pathway are undefined.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional/tissue-specific *Srd5a3* mouse model** (e.g., neural- and eye-restricted knockouts) to overcome the peri-implantation lethality confounded by *Exoc1*, enabling phenotype recapitulation and therapeutic testing.
2. **Validate atorvastatin efficacy** in patient-derived models (iPSC-derived neurons/organoids, cerebellar and retinal organoids) and, if positive, design an n-of-few clinical trial with glycosylation biomarkers as endpoints ([PMID: 41648237](https://pubmed.ncbi.nlm.nih.gov/41648237/)).
3. **Test dietary dolichol supplementation** rescue in mammalian patient-derived systems, building on plant/yeast rescue data ([PMID: 26628744](https://pubmed.ncbi.nlm.nih.gov/26628744/)).
4. **Directly quantify O-/C-mannosylation and GPI-anchor defects** in patient cells to confirm the inferred mechanistic branches.
5. **Standardize diagnostics:** adopt reflex confirmatory testing (polyprenol/dolichol ratio, glycoproteomics, CNV analysis) whenever transferrin screening is normal but clinical suspicion is high; evaluate **albumin glycopeptides** as a robust biomarker ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/)).
6. **Enroll SRD5A3-CDG patients in the FCDGC natural history study** to build prospective longitudinal outcome, NPCRS severity, and QoL data ([PMID: 38959600](https://pubmed.ncbi.nlm.nih.gov/38959600/)).
7. **Map founder alleles and carrier frequencies** in high-consanguinity populations to guide carrier screening and reproductive counseling.

---

*Report compiled from 8 confirmed findings across 35 reviewed publications. Evidence is predominantly human-clinical and in-vitro, supplemented by conserved plant/yeast models. All mechanistic and clinical claims are cited to primary literature by PMID; inferred steps are explicitly labeled.*


## Artifacts

- [OpenScientist final report](SRD5A3-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SRD5A3-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (2 mentions) - the report calls it "Intellectual disability", "Very frequent (near-universal)"; HP calls it **Intellectual disability**
- `HP:0001252` (2 mentions) - the report calls it "Hypotonia", "Very frequent"; HP calls it **Hypotonia**
- `HP:0001251` (2 mentions) - the report calls it "Ataxia", "Frequent"; HP calls it **Ataxia**
- `HP:0000639` (2 mentions) - the report calls it "Nystagmus", "Frequent"; HP calls it **Nystagmus**
- `HP:0000648` (2 mentions) - the report calls it "Optic atrophy", "Frequent"; HP calls it **Optic atrophy**
- `HP:0000556` (2 mentions) - the report calls it "Retinal dystrophy", "Frequent (can be presenting)"; HP calls it **Retinal dystrophy**
- `HP:0000589` (2 mentions) - the report calls it "Coloboma", "Variable"; HP calls it **Coloboma**
- `HP:0000518` (2 mentions) - the report calls it "Cataract", "Variable/progressive"; HP calls it **Cataract**
- `HP:0008064` (2 mentions) - the report calls it "Ichthyosis", "Frequent"; HP calls it **Ichthyosis**
- `HP:0001250` (2 mentions) - the report calls it "Seizure", "Less common"; HP calls it **Seizure**
- `MONDO:0012997` (1 mention) - the report calls it "congenital disorder of glycosylation, type Iq"; MONDO calls it **cholestasis-pigmentary retinopathy-cleft palate syndrome**
- `HP:0000510` (1 mention) - the report calls it "Variable"; HP calls it **Rod-cone dystrophy**
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum", "Primary organs/systems:** central nervous system, especially **cerebellum"; UBERON calls it **cerebellum**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019408` (obsolete dolichol biosynthetic process) (1 mention) - replaced by `GO:0043048`
- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0019408` (1 mention) - the report calls it "dolichol biosynthetic process"; GO calls it **obsolete dolichol biosynthetic process**
- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `GO:0035269` (1 mention) - the report calls it "protein O-linked mannosylation"; GO calls it **protein O-linked glycosylation via mannose**, and lists "protein O-linked mannosylation" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001249` - called "Intellectual disability", "Very frequent (near-universal)"
- `HP:0001252` - called "Hypotonia", "Very frequent"
- `HP:0001251` - called "Ataxia", "Frequent"
- `HP:0000639` - called "Nystagmus", "Frequent"
- `HP:0000648` - called "Optic atrophy", "Frequent"
- `HP:0000556` - called "Retinal dystrophy", "Frequent (can be presenting)"
- `HP:0000589` - called "Coloboma", "Variable"
- `HP:0000518` - called "Cataract", "Variable/progressive"
- `HP:0008064` - called "Ichthyosis", "Frequent"
- `HP:0001250` - called "Seizure", "Less common"
- `UBERON:0002037` - called "cerebellum", "Primary organs/systems:** central nervous system, especially **cerebellum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
