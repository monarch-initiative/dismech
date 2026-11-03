---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:16:22.329073'
end_time: '2026-10-16T20:57:07.708049'
duration_seconds: 2445.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ACCES Syndrome
  mondo_id: MONDO:0859262
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ACCES_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ACCES_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACCES Syndrome
- **MONDO ID:** MONDO:0859262 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ACCES Syndrome** covering all of the
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

# ACCES Syndrome (Aplasia Cutis Congenita with Ectrodactyly Skeletal Syndrome): A Comprehensive Disease Characterization

**Disease:** ACCES Syndrome · **MONDO:** [MONDO:0859262](https://monarchinitiative.org/MONDO:0859262) · **OMIM:** #619959 · **Gene:** *UBA2* (19q13.11) · **Category:** Mendelian, autosomal dominant

---

## Summary

**ACCES syndrome (Aplasia Cutis Congenita with Ectrodactyly Skeletal Syndrome; OMIM #619959, MONDO:0859262) is a rare autosomal-dominant multiple-congenital-anomaly disorder caused by haploinsufficiency of *UBA2*, the gene encoding the catalytic subunit (SAE2) of the heterodimeric SUMO-activating (E1) enzyme, located at chromosome 19q13.11.** The disorder was first delineated as a recognizable Mendelian entity in 2021 through exome sequencing of 16 affected individuals from 7 unrelated families ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). *UBA2* lies immediately adjacent to the minimal deletion overlap region of the previously described 19q13.11 contiguous-gene microdeletion syndrome, and recognition that point mutations and small intragenic losses of *UBA2* alone reproduce the skin-and-limb phenotype established UBA2 haploinsufficiency as the molecular cause.

The core phenotype pairs **aplasia cutis congenita** (localized congenital absence of skin, most often of the scalp) with **ectrodactyly / split-hand–split-foot malformation (SHFM)**, accompanied by highly variable growth retardation, dysmorphic facial features, neurodevelopmental delay, and skeletal, ectodermal, craniofacial, cardiac, renal, and genital anomalies. Expressivity is strikingly variable — ranging from a full multi-organ malformation syndrome to isolated split hand/foot malformation, and in some pedigrees to a skeletal-dysplasia–like presentation that can mimic autosomal-dominant spondyloepiphyseal dysplasia tarda. Because UBA2 is the rate-limiting enzyme of the entire protein SUMOylation cascade, reduced gene dosage lowers global SUMO conjugation, which de-represses chromatin-regulated cell-fate programs and perturbs neural-crest differentiation and FGF/FGFR signaling during a narrow window of early embryogenesis, generating the characteristic craniofacial, skin, and limb malformations.

The mechanistic model is unusually well supported for an ultra-rare disorder: human loss-of-function and missense variants and overlapping 19q13.11 deletions; a zebrafish *uba2*-null model that phenocopies human features and in which human missense mRNA fails to rescue (confirming loss of function); a pharmacological pregnant-mouse model using the selective SUMO-E1 inhibitor TAK981 that reproduces aplasia-cutis-like skin, craniofacial deformities and syndactyly while implicating neural-crest and FGFR pathways by transcriptomics; and population-genetic constraint data (gnomAD pLI ≈ 1.0, LOEUF 0.24) confirming that *UBA2* is exquisitely intolerant to loss of function. No disease-specific therapy exists; management is supportive and multidisciplinary.

---

## Key Findings

### Finding 1 — ACCES is caused by *UBA2* haploinsufficiency (OMIM #619959, 19q13.11)

Exome sequencing across **16 affected subjects from 7 unrelated families** identified seven *UBA2* loss-of-function and missense sequence variants as the cause of a recognizable syndrome combining variable aplasia cutis congenita and ectrodactyly ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). The gene, *UBA2* (ubiquitin-like modifier–activating enzyme 2, also called SUMO-activating enzyme subunit 2 / SAE2), sits at **chromosome 19q13.11**, immediately adjacent to the minimal deletion overlap region of the 19q13.11 contiguous-gene deletion syndrome — the discovery paper notes that *"UBA2 (ubiquitin-like modifier-activating enzyme 2) lies adjacent to the minimal deletion overlap region"* and that *"seven human UBA2 loss-of-function and missense sequence variants were detected."* A subsequent report reiterates the nosology: *"Aplasia Cutis Congenita with Ectrodactyly Skeletal Syndrome (ACCES, OMIM #619959) is an extremely rare multiple congenital anomalies syndrome caused by haploinsufficiency of the UBA2 gene"* ([PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/)). The disease is inherited in an **autosomal dominant** manner.

### Finding 2 — ACCES is a multisystem malformation syndrome with highly variable expressivity

The *UBA2*-related phenotype is multisystem. The original cohort documented *"ACC, ectrodactyly, neurodevelopmental abnormalities, ectodermal, skeletal, craniofacial, cardiac, renal, and genital anomalies"* ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). Later reports expanded the recognized spectrum to include growth retardation, dysmorphic facies, developmental dysplasia of the hip (DDH), scoliosis, and internal-organ abnormalities ([PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/)).

Expressivity is **highly variable**, spanning a broad clinical continuum:
- **Severe/classic end:** full multiple-congenital-anomaly phenotype with scalp ACC + ectrodactyly + systemic involvement.
- **Mild end:** isolated split hand/foot malformation without the full ACCES phenotype — *"the rising number of reported UBA2 variants associated with isolated split hand/ft malformations without a full ACCES phenotype highlights the functional importance of UBA2 in distal limb morphogenesis"* ([PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/)).
- **Atypical/skeletal end:** a spondyloepiphyseal-dysplasia-like presentation; the authors of [PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/) explicitly note the *"highly variable expressiveness of ACCES syndrome."*

### Finding 3 — Mechanism: loss of UBA2-mediated SUMOylation disrupts development of affected tissues

UBA2 is the **catalytic subunit of the heterodimeric SUMO E1 activating enzyme (SAE1/UBA2)** that is obligatory for all SUMO conjugation. Functional validation in zebrafish established causality: *uba2* is expressed in eye, brain, and pectoral fins; *uba2*-null fish *"showed deficient growth, microcephaly, microphthalmia, mandibular hypoplasia, and abnormal fins"* — phenocopying the human features — and critically, *"uba2-mRNAs with human missense variants failed to rescue nullizygous zebrafish phenotypes,"* proving the human missense alleles are loss-of-function ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). The authors conclude the work *"highlights the importance of SUMOylation in the development of affected tissues."*

### Finding 4 — Pharmacological SUMOylation inhibition in pregnant mice recapitulates ACCES and implicates neural-crest/FGF dysregulation

Transient suppression of SUMOylation with the **selective SUMO-E1 inhibitor TAK981** during early post-implantation mouse embryogenesis produced a dose-dependent phenocopy: at low dose, *"viable mice with craniofacial deformities often accompanied by hydrocephalus, syndactyly and an aplasia cutis-like phenotype,"* while high dose caused embryonic lethality with disrupted nuclear/nucleolar integrity ([PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)). Transcriptomics revealed *"the repression of genes involved in neural crest differentiation in the TAK981-treated embryos as well as the overexpression of the Fgfr gene family"* — genes whose gain-of-function mutations cause human craniosynostosis. The authors explicitly link this to human disease: *"haploinsufficiency for the SUMOylation machinery's E1 enzyme, UBA2, leads to various phenotypic traits in humans, including craniofacial malformations and aplasia cutis congenita."*

### Finding 5 — Differential diagnosis and nosology: overlap with EEC, 19q13.11 microdeletion, Adams–Oliver, and SE(M)D

The ACC-plus-ectrodactyly combination overlaps several entities:
- **EEC (ectrodactyly–ectodermal dysplasia–clefting, *TP63*):** a 19q13.11 microdeletion patient was *"followed for a long time under an ectrodactyly ectodermal dysplasia-clefting (EEC) syndrome and was subsequently diagnosed with a 19q13.11 microdeletion"* ([PMID: 29988626](https://pubmed.ncbi.nlm.nih.gov/29988626/)), prompting the recommendation to test EEC-like patients for 19q13.11 imbalance.
- **19q13.11 contiguous-gene deletion syndrome:** larger deletions add dosage-sensitive genes beyond *UBA2* (e.g., *WTIP* for hypospadias; the KRAB-ZNF cluster), producing developmental delay, growth retardation, microcephaly, ectodermal dysplasia, and male genital anomalies. The deletion literature provides *"further definition of the 19q13.11 microdeletion syndrome phenotype, including the first presentation of ectrodactyly in the syndrome"* ([PMID: 24243649](https://pubmed.ncbi.nlm.nih.gov/24243649/); see also [PMID: 22378287](https://pubmed.ncbi.nlm.nih.gov/22378287/)).
- **Spondyloepiphyseal/spondyloepimetaphyseal dysplasia (SE(M)D):** atypical ACCES can mimic a skeletal dysplasia — *"the dominant inheritance pattern in the pedigree suggested a pre-diagnosis of spondyloepiphyseal dysplasia tarda"* ([PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/)).
- **Aplasia cutis congenita broadly** is etiologically heterogeneous (Frieden 1986 classification; [PMID: 3514708](https://pubmed.ncbi.nlm.nih.gov/3514708/)) and includes genetic, teratogenic, vascular-disruptive, and syndromic forms (e.g., Adams–Oliver, Scalp–Ear–Nipple/*KCTD1*).

### Finding 6 — gnomAD constraint confirms *UBA2* is highly haploinsufficiency-prone

Population-genetic constraint metrics independently corroborate the dosage-sensitivity mechanism. For *UBA2* (Ensembl ENSG00000126261; HGNC:30661; GRCh38 chr19:34,428,352–34,471,251), gnomAD reports **pLI = 1.0** (probability of loss-of-function intolerance), observed/expected LoF ratio **oe_lof = 0.142 (90% CI 0.090–0.236; LOEUF = 0.236)**, **LoF Z = 6.39**, and **missense mis_z = 4.50 (oe_mis = 0.62)**. These values place *UBA2* among the most loss-of-function–intolerant genes in the genome and show significant depletion of missense variants as well — exactly the pattern expected for a haploinsufficient developmental gene.

| Constraint metric | Value | Interpretation |
|---|---|---|
| pLI | 1.0 | Extreme LoF intolerance |
| LOEUF (oe_lof upper) | 0.24 | Top constraint decile |
| oe_lof | 0.142 (CI 0.090–0.236) | ~86% fewer LoF than expected |
| LoF Z | 6.39 | Strong depletion |
| missense Z | 4.50 | Significant missense constraint |

### Finding 7 — UBA2/SAE2 biochemistry: catalytic E1 subunit that activates SUMO via an ATP-dependent thioester

UniProt **Q9UBT2** describes UBA2 (SUMO-activating enzyme subunit 2 / SAE2) as forming a heterodimer with SAE1; the complex is the SUMO E1 ligase that *mediates ATP-dependent activation of SUMO proteins followed by formation of a thioester bond between a SUMO protein and a conserved active-site cysteine residue on UBA2/SAE2* for SUMO1, SUMO2, SUMO3 and probably SUMO4. UBA2 passes activated SUMO to the single SUMO E2 conjugating enzyme **UBE2I (Ubc9)** and localizes to both cytoplasm and nucleus.

Suggested **GO annotations:** SUMO activating enzyme complex ([GO:0031510](http://amigo.geneontology.org/amigo/term/GO:0031510)), SUMO activating enzyme activity ([GO:0019948](http://amigo.geneontology.org/amigo/term/GO:0019948)), protein sumoylation ([GO:0016925](http://amigo.geneontology.org/amigo/term/GO:0016925)), ATP binding ([GO:0005524](http://amigo.geneontology.org/amigo/term/GO:0005524)), positive regulation of protein sumoylation ([GO:0033235](http://amigo.geneontology.org/amigo/term/GO:0033235)).

### Finding 8 — UBA2 is evolutionarily conserved; zebrafish and mouse models recapitulate ACCES

*UBA2* orthologs are conserved **from yeast to human**: human *UBA2* (NCBI Gene 10054; OMIM \*613295), mouse *Uba2* (50995), rat *Uba2* (308508), zebrafish *uba2* (406672), chicken (415784), *Xenopus tropicalis* (549845), dog (476490), cow (507005), *Drosophila* (44496), *S. cerevisiae* *UBA2* (851998), and *Arabidopsis* (816686). This deep conservation reflects the essentiality of SUMOylation and explains why cross-species models faithfully reproduce human features.

### Finding 9 — Verified MONDO:0859262 cross-references and official definition

EBI OLS4 (MONDO ontology) confirms **MONDO:0859262**, label *"ACCES syndrome,"* with equivalentTo cross-references **OMIM:619959, MedGen:1804308, and UMLS:C5677019**. Official MONDO synonyms include *"aplasia cutis congenita with ectrodactyly skeletal syndrome"* and *"UBA2-related neurodevelopmental disorder, aplasia cutis congenita with ectrodactyly skeletal syndrome."* The MONDO definition reads: *"A rare congenital disease caused by a mutation in the UBA2 gene, characterized by scalp defects, digital and skeletal anomalies, early growth deficiency, and neurodevelopmental delay. Ectrodactyly presents in some cases."* No Orphanet, ICD, or MeSH cross-reference is present in MONDO.

---

## Section-by-Section Report

### 1. Disease Information

ACCES syndrome is a rare autosomal-dominant multiple-congenital-anomaly disorder defined by the co-occurrence of aplasia cutis congenita and ectrodactyly/split-hand–foot malformation with variable skeletal, craniofacial, neurodevelopmental, and internal-organ involvement. It was delineated as a distinct Mendelian entity in 2021 ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)).

**Key identifiers:**
- **MONDO:** MONDO:0859262 (label "ACCES syndrome")
- **OMIM (phenotype):** #619959; **OMIM (gene):** *UBA2* \*613295
- **UMLS/MedGen:** C5677019 / MedGen:1804308
- **HGNC:** 30661; **NCBI Gene:** 10054; **Ensembl:** ENSG00000126261
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No dedicated code identified (not cross-referenced in MONDO).

**Synonyms:** Aplasia Cutis Congenita with Ectrodactyly Skeletal Syndrome; UBA2-related neurodevelopmental disorder; UBA2-related disorder/spectrum (encompassing isolated SHFM at the mild end).

**Source of information:** Derived from aggregated disease-level resources (OMIM, MONDO, UniProt, gnomAD) and from individual-patient case reports/series (clinical reports in PMIDs 34040189, 39149811, 42557106, 40073198, 29988626).

### 2. Etiology

**Primary cause — genetic.** Heterozygous loss-of-function or deleterious missense variants in *UBA2*, or contiguous 19q13.11 deletions encompassing *UBA2*, cause the disease via haploinsufficiency ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). There is no environmental or infectious cause for the Mendelian disorder itself.

**Genetic risk factors:** The causal variant is itself the determinant; most cases are *de novo*, though autosomal-dominant familial transmission occurs. In the broader 19q13.11 deletion syndrome, additional dosage-sensitive genes (*WTIP*, KRAB-ZNF cluster) modify the phenotype ([PMID: 22378287](https://pubmed.ncbi.nlm.nih.gov/22378287/)).

**Environmental risk / protective factors:** None established for the Mendelian form. Notably, the mouse model demonstrates that a *pharmacological* reduction of SUMOylation during pregnancy (TAK981) phenocopies the disorder — an experimental "environmental" analog rather than a natural risk factor ([PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)).

**Gene–environment interactions:** Not characterized in humans. The TAK981 model suggests a critical early-embryonic window in which reduced SUMOylation capacity is maximally teratogenic.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Frequency/notes |
|---|---|---|---|---|
| Aplasia cutis congenita (scalp) | Physical malformation | HP:0001057 | Congenital | Hallmark; variable |
| Ectrodactyly / split-hand–foot malformation | Skeletal malformation | HP:0100257 / HP:0001161 | Congenital | Hallmark; variable (can be isolated) |
| Growth retardation | Clinical sign | HP:0001510 | Prenatal/postnatal | Common |
| Neurodevelopmental delay / ID | Behavioral/cognitive | HP:0001263 / HP:0001249 | Infancy/childhood | Variable |
| Dysmorphic facial features | Physical | HP:0001999 | Congenital | Common |
| Microcephaly | Clinical sign | HP:0000252 | Congenital | Reported |
| Ectodermal dysplasia features | Physical | HP:0000968 | Congenital | Reported |
| Developmental dysplasia of hip | Skeletal | HP:0001385 | Infancy | Reported ([PMID:39149811]) |
| Scoliosis | Skeletal | HP:0002650 | Childhood | Reported |
| Cardiac anomalies (e.g., ASD) | Physical | HP:0001627 | Congenital | Subset |
| Renal anomalies | Physical | HP:0000077 | Congenital | Subset |
| Genital anomalies (e.g., hypospadias) | Physical | HP:0000078 | Congenital | Subset (stronger in deletion syndrome) |

Severity and progression: congenital malformations are structural and stable after birth; neurodevelopmental features evolve during childhood. Expressivity is highly variable both between and within families. Quality-of-life impact is driven chiefly by limb function (SHFM), neurodevelopmental outcome, and the surgical/cosmetic burden of scalp ACC; formal QoL instrument data (EQ-5D/SF-36/PROMIS) are not available for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** *UBA2* (HGNC:30661; NCBI Gene 10054; OMIM \*613295; Ensembl ENSG00000126261; GRCh38 chr19:34,428,352–34,471,251).

**Pathogenic variants:** Seven original variants comprised loss-of-function (nonsense, frameshift, splice) and missense classes ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)); subsequent reports add further missense and splice-site variants, including a prenatally diagnosed splice-site variant ([PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/)) and a novel variant in an Indian family ([PMID: 40073198](https://pubmed.ncbi.nlm.nih.gov/40073198/)). Variants are **germline**. Functional consequence is **loss of function / haploinsufficiency** — confirmed because human missense mRNA fails to rescue the zebrafish null ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). Allele frequencies are effectively absent/ultra-rare in gnomAD, consistent with strong constraint (pLI≈1.0).

**Chromosomal abnormalities:** Contiguous-gene deletions of 19q13.11 encompassing *UBA2* produce an overlapping, generally broader phenotype ([PMID: 24243649](https://pubmed.ncbi.nlm.nih.gov/24243649/); [PMID: 22378287](https://pubmed.ncbi.nlm.nih.gov/22378287/); [PMID: 29988626](https://pubmed.ncbi.nlm.nih.gov/29988626/)).

**Modifier genes / epigenetics:** No validated human modifiers for the pure *UBA2* form; in the deletion syndrome, co-deleted *WTIP* and KRAB-ZNF genes act as phenotype modifiers. Because the primary defect reduces SUMOylation — a chromatin-regulating post-translational modification — downstream epigenetic dysregulation is mechanistically expected (the mouse model showed "epigenetic scars" and altered nuclear/nucleolar integrity at high dose; [PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious agents are established causes of the Mendelian disorder. The only "environmental" analog is experimental pharmacological SUMO-E1 inhibition during pregnancy in mice (TAK981), which is teratogenic and phenocopies ACCES ([PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)) — relevant as a safety consideration for SUMO-inhibitor oncology drugs in pregnancy, not as a natural risk factor.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous *UBA2* loss-of-function or deleterious missense variant (or a 19q13.11 deletion spanning *UBA2*) **reduces functional UBA2 protein to ~50%** (haploinsufficiency). *[Demonstrated: human genetics + gnomAD constraint.]*
2. Reduced UBA2 **lowers assembly/activity of the SAE1–UBA2 (SUMO E1) heterodimer**, the rate-limiting enzyme that ATP-dependently activates SUMO1/2/3 via a thioester to its active-site cysteine. *[Demonstrated: UniProt biochemistry; inferred for patient variants.]*
3. Diminished E1 activity **reduces global protein SUMOylation** (less SUMO charging of the E2 Ubc9/UBE2I and downstream substrates). *[Inferred from enzyme kinetics; supported by pharmacological inhibition model.]*
4. Hypo-SUMOylation **dysregulates SUMO-dependent transcriptional repression and chromatin/nuclear-body function**, de-repressing or mis-timing cell-fate programs. *[Inferred; supported by transcriptomic changes in mouse model.]*
5. This **branches** into:
   - **(5a)** **Repression of neural-crest differentiation genes** → craniofacial and skin/ectodermal malformation (aplasia cutis, dysmorphism, mandibular hypoplasia). *[Demonstrated in mouse transcriptomics; [PMID: 39985830].]*
   - **(5b)** **Dysregulation (overexpression) of the FGFR gene family** → disturbed limb/craniofacial morphogenesis (ectrodactyly/SHFM, syndactyly, craniosynostosis-like changes). *[Demonstrated in mouse transcriptomics; [PMID: 39985830].]*
6. Disrupted apical ectodermal ridge / distal-limb morphogenesis and impaired scalp skin/skull formation during a **critical early-embryonic window** → the clinical hallmarks of **aplasia cutis congenita + ectrodactyly**, plus variable skeletal, cardiac, renal, genital, and neurodevelopmental anomalies. *[Demonstrated across human, zebrafish, and mouse models.]*

```
UBA2 LoF/missense (het)  ──►  ↓ SAE1–UBA2 (SUMO E1) activity  ──►  ↓ global SUMOylation
                                                                        │
                                                                        ▼
                                           dysregulated chromatin / cell-fate programs
                                               │                              │
                                 (5a) ↓ neural-crest differentiation   (5b) ↑ FGFR family
                                               │                              │
                                 aplasia cutis, craniofacial         ectrodactyly/SHFM,
                                 malformation, dysmorphism           syndactyly, skeletal
                                               └──────────────┬───────────────┘
                                                              ▼
                                                   ACCES clinical phenotype
```

**Molecular pathways:** protein SUMOylation (upstream, primary); FGF/FGFR signaling (downstream); neural-crest gene-regulatory network (downstream). **Cellular processes:** cell differentiation, nuclear/nucleolar organization, chromatin regulation. **Cell types:** neural-crest cells ([CL:0000333](http://purl.obolibrary.org/obo/CL_0000333)), ectodermal/epidermal keratinocytes, limb-bud mesenchyme/chondrocytes. **Subcellular (GO CC):** SUMO activating enzyme complex ([GO:0031510](http://amigo.geneontology.org/amigo/term/GO:0031510)), nucleus, nucleolus, cytoplasm. **GO BP:** protein sumoylation ([GO:0016925](http://amigo.geneontology.org/amigo/term/GO:0016925)), neural crest cell differentiation ([GO:0014033](http://amigo.geneontology.org/amigo/term/GO:0014033)), embryonic limb morphogenesis ([GO:0030326](http://amigo.geneontology.org/amigo/term/GO:0030326)).

### 7. Anatomical Structures Affected

- **Primary:** skin — scalp/vertex (aplasia cutis; [UBERON:0000403](http://purl.obolibrary.org/obo/UBERON_0000403) scalp, [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) skin of body); limbs — hands and feet/autopod (ectrodactyly; [UBERON:0002398](http://purl.obolibrary.org/obo/UBERON_0002398) manus, [UBERON:0002387](http://purl.obolibrary.org/obo/UBERON_0002387) pes).
- **Craniofacial/skeletal:** skull, mandible ([UBERON:0001684](http://purl.obolibrary.org/obo/UBERON_0001684)), vertebral column (scoliosis), hip joint (DDH).
- **Nervous system:** brain ([UBERON:0000955](http://purl.obolibrary.org/obo/UBERON_0000955)) — microcephaly, neurodevelopmental delay, hydrocephalus (model).
- **Secondary/subset:** heart ([UBERON:0000948](http://purl.obolibrary.org/obo/UBERON_0000948)) — ASD/septal defects; kidney ([UBERON:0002113](http://purl.obolibrary.org/obo/UBERON_0002113)); external genitalia (hypospadias); eye ([UBERON:0000970](http://purl.obolibrary.org/obo/UBERON_0000970)) — microphthalmia in model.
- **Lateralization:** limb malformations often bilateral but can be asymmetric; scalp ACC typically midline/vertex.
- **Cell/tissue level:** ectoderm-derived epithelium, neural-crest derivatives, limb mesenchyme/cartilage.

### 8. Temporal Development

- **Onset:** congenital/prenatal — structural anomalies are present at birth and can be detected prenatally (a splice-site variant was diagnosed prenatally; [PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/)).
- **Progression:** structural malformations are non-progressive/stable; neurodevelopmental features evolve through infancy and childhood; secondary orthopedic issues (scoliosis, DDH) may require ongoing management.
- **Course:** chronic, lifelong, non-remitting (a congenital malformation syndrome rather than a degenerative disease).
- **Critical period:** early post-implantation embryogenesis — the window during which SUMOylation reduction is maximally teratogenic in the mouse model ([PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)).

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant; many cases *de novo*, with documented familial transmission.
- **Penetrance / expressivity:** apparently high penetrance for *some* phenotype but **highly variable expressivity** — ranging from full ACCES to isolated SHFM ([PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/); [PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/)).
- **Epidemiology:** "extremely rare" — no formal prevalence/incidence established; fewer than ~20 families reported in the literature at the time of this review. The original cohort comprised 16 subjects from 7 families ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)).
- **Population/sex distribution:** no sex predilection established for ACCES itself (hypospadias in the deletion syndrome affects males). Reported across diverse populations (including an Indian family, [PMID: 40073198](https://pubmed.ncbi.nlm.nih.gov/40073198/)); no founder effect or consanguinity role identified (dominant, often *de novo*). Carrier frequency is effectively nil given ultra-rarity and strong constraint.

### 10. Diagnostics

- **Genetic testing is the diagnostic cornerstone.** Recommended approach: **exome or genome sequencing** (how the disorder was discovered; detects point/indel variants), or a **gene panel** including *UBA2* and SHFM/ectodermal-dysplasia genes. **Chromosomal microarray (CMA)** detects 19q13.11 deletions and should be considered in EEC-like or deletion-phenotype patients ([PMID: 29988626](https://pubmed.ncbi.nlm.nih.gov/29988626/)).
- **Prenatal diagnosis** is feasible when a variant is known or detected ([PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/)).
- **Clinical/imaging:** skeletal survey/radiographs for ectrodactyly, scoliosis, DDH; echocardiography for cardiac anomalies; renal ultrasound; neurodevelopmental assessment and brain imaging as indicated; histopathology confirms ACC ([PMID: 3514708](https://pubmed.ncbi.nlm.nih.gov/3514708/)).
- **Differential diagnosis:** EEC syndrome (*TP63*), 19q13.11 microdeletion syndrome, Adams–Oliver syndrome, Scalp–Ear–Nipple syndrome (*KCTD1*; [PMID: 42820132](https://pubmed.ncbi.nlm.nih.gov/42820132/)), isolated SHFM, and — for atypical skeletal presentations — spondyloepiphyseal dysplasia tarda ([PMID: 39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/)).
- **No specific biomarker** or biochemical assay is established; functional SUMOylation assays remain research tools.

### 11. Outcome / Prognosis

Prognosis depends on the specific constellation and severity of malformations. Scalp ACC with large/deep defects carries risks of infection, hemorrhage, and (rarely) dural/meningeal exposure requiring careful management ([PMID: 42820132](https://pubmed.ncbi.nlm.nih.gov/42820132/)). Limb malformation affects fine-motor function and may require reconstructive surgery and rehabilitation. Neurodevelopmental outcome is variable. No systematic survival/mortality, QoL-instrument, or natural-history cohort data exist for this ultra-rare disorder; prognosis is individualized. Many patients survive to adulthood (familial dominant transmission is documented), indicating that the condition is generally compatible with life, with morbidity driven by structural and neurodevelopmental burden.

### 12. Treatment

**No disease-specific or curative therapy exists.** Management is **supportive and multidisciplinary:**
- **Scalp ACC:** conservative wound care is often preferred, even for extensive lesions, to avoid neonatal anesthetic/hemorrhagic/infectious risk; surgical grafting reserved for selected large defects ([PMID: 42820132](https://pubmed.ncbi.nlm.nih.gov/42820132/); [PMID: 42166395](https://pubmed.ncbi.nlm.nih.gov/42166395/)).
- **Limb malformation (SHFM):** orthopedic/plastic-surgical reconstruction and occupational therapy as indicated ([NCIT:C157812] reconstructive surgical procedure).
- **Skeletal:** scoliosis bracing/surgery; DDH management.
- **Cardiac/renal/genital:** anomaly-specific surgical/medical care.
- **Neurodevelopmental:** early intervention, physical/occupational/speech therapy, educational support.
- **Genetic counseling** for affected families (autosomal dominant, variable expressivity).

No pharmacotherapy, gene therapy, RNA therapy, or targeted therapy is approved or in trials for ACCES. Pharmacogenomics is not applicable.

### 13. Prevention

Primary prevention is not possible for a dominant congenital disorder. Relevant measures are reproductive and secondary:
- **Genetic counseling** and **cascade testing** of at-risk relatives once a familial variant is identified.
- **Prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** for known familial variants ([PMID: 42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/)).
- **Tertiary prevention:** early orthopedic, cardiac, renal, and developmental surveillance to prevent/limit complications.
No vaccine, population screening, or behavioral/environmental prevention applies.

### 14. Other Species / Natural Disease

No naturally occurring *UBA2*-related ACCES-equivalent disease is reported in companion animals or wildlife (no OMIA entry identified). However, *UBA2* is deeply conserved, with orthologs across mammals, birds, amphibians, fish, insects, yeast, and plants (Finding 8), and the SUMOylation pathway is essential across eukaryotes. This conservation underlies the validity of cross-species disease modeling. No zoonotic potential (non-infectious Mendelian disorder).

| Species | Gene | NCBI Gene ID |
|---|---|---|
| Human | *UBA2* | 10054 |
| Mouse | *Uba2* | 50995 |
| Rat | *Uba2* | 308508 |
| Zebrafish | *uba2* | 406672 |
| Chicken | *UBA2* | 415784 |
| *Xenopus tropicalis* | *uba2* | 549845 |
| Dog | *UBA2* | 476490 |
| Cow | *UBA2* | 507005 |
| *Drosophila* | *Uba2* | 44496 |
| *S. cerevisiae* | *UBA2* | 851998 |
| *Arabidopsis* | *SAE2* | 816686 |

### 15. Model Organisms

- **Zebrafish (*Danio rerio*):** *uba2*-null model recapitulates deficient growth, microcephaly, microphthalmia, mandibular hypoplasia, and abnormal fins; human missense mRNA fails to rescue — the key functional proof of loss-of-function pathogenicity ([PMID: 34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/)). **Recapitulation: strong** for craniofacial/growth/fin (limb-analog) features.
- **Mouse (*Mus musculus*), pharmacological:** pregnant mice given the selective SUMO-E1 inhibitor TAK981 produce offspring with craniofacial deformities, hydrocephalus, syndactyly, and an aplasia-cutis-like phenotype; transcriptomics implicate neural-crest repression and FGFR overexpression ([PMID: 39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/)). **Recapitulation: strong** for skin/craniofacial/limb features and mechanism. **Limitation:** a drug-induced dose model rather than a genetic *Uba2*-haploinsufficient mouse; a published germline *Uba2* heterozygous mouse phenotype was not identified in this review.
- **Model applications:** dissecting the SUMOylation → neural-crest/FGFR axis; defining the teratogenic window; testing candidate modifiers. **Gap:** no reported iPSC/organoid or conditional-knockout mouse specific to ACCES yet.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [34040189](https://pubmed.ncbi.nlm.nih.gov/34040189/) | *UBA2 variants underlie a recognizable syndrome with variable ACC and ectrodactyly* | Human genetics + zebrafish | **Foundational** — defines disease, gene, LoF mechanism, zebrafish rescue |
| [39985830](https://pubmed.ncbi.nlm.nih.gov/39985830/) | *Transient pharmacological inhibition of SUMOylation during pregnancy induces craniofacial malformations in offspring mice* | Mouse model + transcriptomics | Mechanism — neural-crest/FGFR axis; teratogenic window |
| [39149811](https://pubmed.ncbi.nlm.nih.gov/39149811/) | *Atypical ACCES resembling dominant SED tarda* | Human clinical | Variable expressivity; skeletal-dysplasia mimicry; confirms haploinsufficiency |
| [42557106](https://pubmed.ncbi.nlm.nih.gov/42557106/) | *Prenatal diagnosis of a splice-site UBA2 variant* | Human clinical | Mild end (isolated SHFM); prenatal diagnosis; distal-limb role |
| [40073198](https://pubmed.ncbi.nlm.nih.gov/40073198/) | *Novel UBA2 variant causing ACCES in an Indian family* | Human clinical | Population breadth; novel variant |
| [29988626](https://pubmed.ncbi.nlm.nih.gov/29988626/) | *19q13.11 microdeletion overlapping EEC* | Human clinical | Differential diagnosis (EEC); CMA utility |
| [24243649](https://pubmed.ncbi.nlm.nih.gov/24243649/) | *19q12q13.1 deletions, 5 patients* | Human clinical | Deletion-syndrome phenotype incl. ectrodactyly |
| [22378287](https://pubmed.ncbi.nlm.nih.gov/22378287/) | *19q13.11 cryptic deletion; WTIP and hypospadias* | Human clinical | Contiguous-gene modifiers (WTIP, KRAB-ZNF) |
| [28509170](https://pubmed.ncbi.nlm.nih.gov/28509170/) | *Cystinuria in 19q12q13.1 deletion* | Human clinical | Deletion-syndrome gene content (SLC7A9) |
| [3514708](https://pubmed.ncbi.nlm.nih.gov/3514708/) | *ACC: clinical review and classification* | Review | Frieden classification; ACC heterogeneity |
| [32501579](https://pubmed.ncbi.nlm.nih.gov/32501579/) | *Classification of ACC, 25-year review* | Clinical series | Modern ACC nosology |
| [42820132](https://pubmed.ncbi.nlm.nih.gov/42820132/) | *Familial ACC with meningeal exposure* | Case report | Differential (SENS/KCTD1); conservative management |
| [42166395](https://pubmed.ncbi.nlm.nih.gov/42166395/) | *ACC type V with SUA and ASD* | Case report | ACC management; differential |

Non-UBA2 constraint/biochemistry evidence (Findings 6, 7, 9) derives from gnomAD, UniProt Q9UBT2, and EBI OLS4/MONDO — database resources, not PubMed-indexed papers.

---

## Mechanistic Model / Interpretation

ACCES is best understood as a **dosage disease of the SUMOylation machinery**. Because SAE1–UBA2 is the single, rate-limiting E1 gateway for all SUMO conjugation, a 50% reduction in UBA2 does not abolish SUMOylation (that would be embryonically lethal, as the high-dose TAK981 arm shows) but instead produces a **sub-threshold, tissue- and time-sensitive deficit**. The developing embryo tolerates this globally yet fails selectively in processes most dependent on robust SUMO-mediated transcriptional control during a narrow early window — above all the **neural-crest gene-regulatory network** (craniofacial, skin/ectoderm) and **FGF/FGFR-dependent limb morphogenesis**. This two-branch output elegantly explains the otherwise puzzling pairing of aplasia cutis (an ectoderm/neural-crest problem) with ectrodactyly (a limb-patterning problem) in one syndrome, and the extreme variability reflects stochastic crossing of developmental thresholds. The convergent evidence — human LoF genetics, a non-rescuing zebrafish null, a mechanism-revealing mouse pharmacological model, and genome-wide constraint — makes this one of the better-validated mechanisms among ultra-rare malformation syndromes.

---

## Limitations and Knowledge Gaps

1. **No formal epidemiology** (prevalence, incidence, sex ratio) — fewer than ~20 families reported.
2. **No genetic *Uba2*-haploinsufficient mouse** phenotype in the literature reviewed; mechanism rests on a *pharmacological* mouse model plus a zebrafish *null* (homozygous) model rather than a dosage-matched genetic mammal.
3. **Direct demonstration of reduced SUMOylation in patient tissues is lacking** — step 3 of the causal chain is inferred from enzyme biochemistry and the inhibitor model.
4. **Genotype–phenotype correlation is unresolved** — why some *UBA2* variants cause isolated SHFM and others full ACCES is unknown; no validated modifiers for the pure form.
5. **No natural-history, QoL, survival, or treatment-outcome data** exist.
6. **No Orphanet/ICD/MeSH codes** currently cross-referenced; nosology still consolidating.
7. **gnomAD/UniProt/MONDO claims** are database-derived and not independently re-validated here.

## Proposed Follow-up Experiments / Actions

1. **Generate a genetic *Uba2*^+/− mouse** (and conditional neural-crest/limb-bud knockouts) to confirm haploinsufficiency recapitulates ACCES and to map tissue-specific requirements.
2. **Quantify global and substrate-specific SUMOylation** in patient-derived fibroblasts/iPSCs to directly test step 3 of the causal chain.
3. **Patient iPSC → neural-crest and limb-bud/organoid differentiation** to test the predicted neural-crest-repression and FGFR-dysregulation branches in a human system.
4. **Establish an international registry** to define prevalence, penetrance, genotype–phenotype correlations, natural history, and QoL.
5. **Systematic ClinVar/variant functional assays** (zebrafish rescue, in vitro E1 activity) to classify new *UBA2* VUS and clarify the SHFM-vs-ACCES determinants.
6. **Pharmacovigilance** for SUMO-E1 inhibitors (e.g., TAK981/subasumstat) regarding embryo-fetal toxicity, given the teratogenic mouse data.
7. **Pursue formal Orphanet/ICD-11 coding** to improve ascertainment and knowledge-base interoperability.

---

*Evidence source legend: Human clinical (case reports/series, exome/CMA); Model organism (zebrafish null, mouse pharmacological); Database/computational (gnomAD constraint, UniProt biochemistry, MONDO/OLS4). This report integrates 9 confirmed findings and 20 reviewed papers across 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](ACCES_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ACCES_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 11 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859262` (7 mentions) - the report calls it "if available", "MONDO", "label "ACCES syndrome"; MONDO calls it **ACCES syndrome**
- `HP:0001057` (1 mention) - the report calls it "Physical malformation"; HP calls it **Aplasia cutis congenita**
- `HP:0001510` (1 mention) - the report calls it "Clinical sign"; HP calls it **Growth delay**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0000252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Microcephaly**
- `HP:0000968` (1 mention) - the report calls it "Physical"; HP calls it **Ectodermal dysplasia**
- `HP:0001385` (1 mention) - the report calls it "Skeletal"; HP calls it **Hip dysplasia**
- `HP:0002650` (1 mention) - the report calls it "Skeletal"; HP calls it **Scoliosis**
- `HP:0001627` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal heart morphology**
- `HP:0000077` (1 mention) - the report calls it "Physical"; HP calls it **Abnormality of the kidney**
- `HP:0000078` (1 mention) - the report calls it "Physical"; HP calls it **Abnormality of the genital system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0859262` - called "if available", "MONDO", "label "ACCES syndrome"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`.
