---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-16T20:44:40.634175'
end_time: '2026-09-16T21:02:02.340925'
duration_seconds: 1041.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Myasthenic Syndrome 7
  mondo_id: MONDO:0014468
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
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Myasthenic_Syndrome_7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myasthenic_Syndrome_7-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myasthenic Syndrome 7
- **MONDO ID:** MONDO:0014468 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myasthenic Syndrome 7** covering all of the
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

# Congenital Myasthenic Syndrome 7 (CMS7 / SYT2-Related Presynaptic Myasthenia): A Comprehensive Disease Characterization

**MONDO:** MONDO:0014468 · **OMIM:** #616040 (CMS7A, dominant) / #619461 (CMS7B, recessive) · **Gene:** SYT2 (synaptotagmin-2) · **Category:** Mendelian, rare

---

## Summary

**Congenital Myasthenic Syndrome 7 (CMS7)** is an ultra-rare, genetically determined **presynaptic** disorder of neuromuscular transmission caused by germline variants in **SYT2 (synaptotagmin-2)**, the protein that serves as the calcium sensor for fast, synchronous acetylcholine (ACh) release at the neuromuscular junction (NMJ). Because the primary lesion sits in the nerve terminal rather than the muscle endplate, CMS7 behaves clinically and electrophysiologically like a genetic mimic of the autoimmune Lambert–Eaton myasthenic syndrome (LEMS): low compound muscle action potential (CMAP) amplitudes at rest that facilitate (increment) after brief exercise or high-frequency stimulation, together with a characteristically prolonged post-tetanic potentiation. The disease is important out of proportion to its rarity because it is **treatable** — patients respond to the potassium-channel blocker 3,4-diaminopyridine (3,4-DAP) and to acetylcholinesterase inhibitors such as pyridostigmine.

CMS7 has **two inheritance modes with distinct severity**. Autosomal **dominant** disease arises from heterozygous missense or in-frame variants clustered in the **C2B calcium-binding domain** (canonically p.Asp307Ala and p.Pro308Leu), which act by a **dominant-negative** mechanism; these patients present with slowly progressive or non-progressive distal lower-limb weakness and wasting, foot deformities (pes cavus), fatigable weakness, hyporeflexia/areflexia with post-exercise reflex potentiation, and a phenotype that can mimic a distal hereditary motor neuropathy/Charcot–Marie–Tooth disease. Autosomal **recessive** disease arises from **biallelic loss-of-function** variants (frameshift, nonsense, splice-site, large deletion), frequently in consanguineous families, and is substantially more severe — congenital-onset hypotonia, profound weakness, areflexia, bulbar dysfunction, and variable respiratory involvement.

This report synthesizes 13 confirmed findings drawn from 29 papers, including the seminal disease-gene reports (Herrmann 2014, Whittaker 2015), recessive-form descriptions (2019–2021), a *Drosophila* causality model, comprehensive CMS reviews (35- and 40-gene reviews), UK epidemiology, and gnomAD constraint analysis. Across the sections below, CMS7 is characterized at the level of disease identity, etiology, phenotype, molecular genetics, pathophysiology (presented as an explicit causal chain), affected anatomy, temporal course, inheritance/population genetics, diagnostics, prognosis, treatment, prevention, and model organisms. Where information is genuinely unavailable for this ultra-rare disease (e.g., formal quality-of-life instrument data, natural-history registries specific to SYT2), this is stated explicitly.

---

## 1. Disease Information

**What it is.** CMS7 is a Mendelian congenital myasthenic syndrome in which fast synchronous neurotransmitter release at the NMJ fails because of defects in the presynaptic calcium sensor synaptotagmin-2. It is one of the small group of **presynaptic** CMS subtypes that phenocopy LEMS (the "CMS-LEMS" group), alongside AGRN, MUNC13-1/UNC13A, VAMP1, and LAMA5 (F004; [PMID: 29696584](https://pubmed.ncbi.nlm.nih.gov/29696584/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014468 |
| OMIM | #616040 (CMS7A, autosomal dominant); #619461 (CMS7B, autosomal recessive) |
| Gene (HGNC) | SYT2, HGNC:11510 |
| NCBI Gene | 127833 |
| Ensembl | ENSG00000143858 |
| UniProt | Q8N9I0 |
| Cytoband | 1q32.1 |

**Synonyms / alternative names.** CMS7; SYT2-related disease; SYT2-CMS; presynaptic congenital myasthenic syndrome 7; autosomal-dominant Lambert-Eaton–like myasthenic syndrome with nonprogressive motor neuropathy (dominant form). Gene aliases: **CMS7, CMS7A, CMS7B, MYSPC, SytII** (F008).

**Data provenance.** Essentially all knowledge derives from **aggregated disease-level resources** and **individual published case reports/small case series** (~10–15 families worldwide), not from EHR/population phenotyping — a direct consequence of the disease's extreme rarity.

---

## 2. Etiology

**Primary cause — genetic.** CMS7 is a monogenic disorder caused entirely by pathogenic germline variants in **SYT2**. There is no environmental, infectious, or acquired etiology; it is not autoimmune (distinguishing it mechanistically from myasthenia gravis and from paraneoplastic LEMS). Two allelic mechanisms operate (F001, F010):

- **Dominant** heterozygous **C2B-domain missense/in-frame** variants → dominant-negative poisoning of release.
- **Recessive** biallelic **loss-of-function** variants → absence of functional SYT2.

**Genetic risk factors.** The causal variants themselves are the risk factor. For the recessive form, **consanguinity** is a major contributing factor (multiple reported homozygous cases in consanguineous families; F010; [PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/), [PMID: 36722210](https://pubmed.ncbi.nlm.nih.gov/36722210/)). No susceptibility loci, GWAS signals, or modifier genes have been established for this Mendelian disease.

**Environmental / lifestyle / protective factors.** None established. As a channel/release Mendelian disorder, there are no known dietary, occupational, toxic, or lifestyle risk or protective factors, and no gene–environment interactions have been reported. (Not applicable / not available.)

**Infectious agents.** Not applicable — CMS7 is non-infectious. Intercurrent respiratory infections can precipitate crises in the severe recessive form (a trigger of morbidity, not a cause).

---

## 3. Phenotypes

CMS7 phenotypes are **clinical signs and physical manifestations** of impaired neuromuscular transmission plus a secondary neurogenic/motor-neuropathy component. Severity is bimodal by inheritance mode (F005).

| Phenotype | Type | Onset | Severity/Course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Fatigable muscle weakness | Clinical sign | Congenital–childhood (recessive) to childhood/adult (dominant) | Fluctuating, fatigable | Core / typical | HP:0003473 (Fatigable weakness) |
| Distal lower-limb weakness & wasting | Physical | Childhood (dominant) | Slowly progressive/stable | Typical in dominant | HP:0002460 (Distal muscle weakness); HP:0003693 (Distal amyotrophy) |
| Foot deformities / pes cavus | Physical | Childhood | Stable structural | Frequent in dominant | HP:0001761 (Pes cavus) |
| Neonatal hypotonia | Clinical sign | Neonatal | Severe in recessive | Frequent in recessive | HP:0001319 (Neonatal hypotonia) |
| Hyporeflexia / areflexia | Clinical sign | Variable | With post-exercise reflex potentiation | Typical | HP:0001315 (Reduced tendon reflexes); HP:0001284 (Areflexia) |
| Ptosis / ocular weakness | Clinical sign | Variable | Fatigable | Variable | HP:0000508 (Ptosis); HP:0000602 (Ophthalmoplegia) |
| Bulbar dysfunction (weak cry, dysphonia, dysphagia) | Clinical sign | Neonatal/infancy (recessive) | Moderate–severe | Recessive-predominant | HP:0002019 (Feeding difficulties) |
| Respiratory insufficiency / recurrent infections | Clinical sign | Infancy (recessive) | Severe; morbidity/mortality driver | Recessive-predominant | HP:0002093 (Respiratory insufficiency); HP:0002205 (Recurrent respiratory infections) |
| Delayed motor development | Clinical sign | Infancy | Variable | Recessive-predominant | HP:0001270 (Motor delay) |
| Elevated CK (mild) | Lab abnormality | — | e.g., CPK 501 U/L | Occasional | HP:0003236 (Elevated creatine kinase) |

Key supporting evidence (F005): a 2025 case-based review synthesizing 28 cases describes SYT2-related disease as *"characterized by distal muscle atrophy in the lower limbs, foot deformities and, in some cases, neonatal hypotonia,"* with most mutations in the C2B domain ([PMID: 41331967](https://pubmed.ncbi.nlm.nih.gov/41331967/)). The dominant-vs-recessive severity gradient is explicit: *"The recessive form of CMS caused by a SYT2 mutation showed far more severe clinical manifestations than the dominant form"* ([PMID: 34037996](https://pubmed.ncbi.nlm.nih.gov/34037996/)). Distal weakness with pes cavus can mimic distal hereditary motor neuropathy/CMT ([PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/)).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36/PROMIS data exist for CMS7 (not available). Qualitatively, the dominant form causes gait impairment and fatigue affecting mobility and daily function; the recessive form causes major disability with respiratory and feeding needs. A salbutamol trial in NMJ-involving motor neuropathies (including SYT2) recorded patient-reported **fatigue** as a meaningful endpoint (F007; [PMID: 36869887](https://pubmed.ncbi.nlm.nih.gov/36869887/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **SYT2** (synaptotagmin-2), HGNC:11510, NCBI Gene 127833, Ensembl ENSG00000143858, UniProt Q8N9I0, chromosome **1q32.1** (GRCh38 chr1:202,590,596–202,710,526, minus strand) (F008).

**Protein architecture.** Synaptotagmin-2 is a synaptic-vesicle transmembrane protein with an N-terminal intravesicular/luminal region, a single transmembrane domain, and **two cytoplasmic tandem C2 domains (C2A and C2B)** that bind Ca²⁺ and phospholipids/SNAREs (F008). SYT2 is the major synaptotagmin isoform at the human NMJ and one of only three (SYT1, SYT2, SYT9) that serve as Ca²⁺ sensors for **fast synchronous** release (F002; [PMID: 17521570](https://pubmed.ncbi.nlm.nih.gov/17521570/)).

**Pathogenic variants and their mechanisms.**

| Variant (protein / cDNA) | Domain | Type | Inheritance | Mechanism | Reference |
|---|---|---|---|---|---|
| p.Asp307Ala (c.920A>C) | C2B | Missense, disrupts essential Ca²⁺-binding Asp | AD | Dominant-negative | [PMID: 25192047](https://pubmed.ncbi.nlm.nih.gov/25192047/) |
| p.Pro308Leu (c.923C>T) | C2B | Missense | AD | Dominant-negative | [PMID: 25192047](https://pubmed.ncbi.nlm.nih.gov/25192047/) |
| p.361_365del (c.1082_1096del) | C2B | In-frame deletion, de novo | AD | Dominant-negative | [PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/) |
| p.Arg397Serfs*37 (c.1191delG) | C2B C-terminus | Frameshift | AR (homozygous) | Loss of function | [PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/) |
| c.465+1G>A | splice donor | Splice | AR (homozygous) | Loss of function | [PMID: 33659639](https://pubmed.ncbi.nlm.nih.gov/33659639/) |
| c.328_331dup | — | Frameshift | AR (homozygous) | Loss of function | [PMID: 33659639](https://pubmed.ncbi.nlm.nih.gov/33659639/) |
| Large deletion exons 2–9 | multi-exon | Structural | AR (homozygous) | Loss of function | [PMID: 36722210](https://pubmed.ncbi.nlm.nih.gov/36722210/) |

**Variant classification & population frequency.** Reported pathogenic variants are **private/ultra-rare** and effectively **absent or singleton** in population databases, consistent with high penetrance and de novo/consanguineous origins (F013). gnomAD constraint for SYT2 (F013): **pLI = 0.70**, **LOEUF (upper) = 0.58**, **LoF-z = 3.34** (intolerant to complete LoF), **missense-z = 2.62** (missense-constrained), synonymous-z = 0.98 (neutral, as expected). This constraint profile explains why dominant missense variants are pathogenic and why biallelic LoF produces severe disease.

**Somatic vs germline.** All variants are **germline**. No somatic disease role.

**Functional consequences.** Dominant C2B missense/in-frame variants = **dominant-negative**; recessive truncating/splice/structural variants = **loss of function** (F008, F010; [PMID: 34037996](https://pubmed.ncbi.nlm.nih.gov/34037996/), [PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, epigenetic marks, or large chromosomal abnormalities (beyond the single-gene exonic deletion above) are established for CMS7 (not available). One mechanistic aside: in cortical neurons, calmodulin transcriptionally suppresses *SYT2*, an inverse rostral–caudal expression relationship — relevant to SYT2 biology but not established as a disease modifier ([PMID: 20729199](https://pubmed.ncbi.nlm.nih.gov/20729199/)).

---

## 5. Environmental Information

**Environmental, lifestyle, and infectious factors.** Not applicable to disease causation — CMS7 is purely Mendelian. There are no reported toxin, radiation, occupational, dietary, smoking, alcohol, or exercise contributions to disease risk. Intercurrent **respiratory infections** are clinically relevant only as **precipitants of crisis/morbidity** in the severe recessive form, not as etiologic agents (F012; [PMID: 41331967](https://pubmed.ncbi.nlm.nih.gov/41331967/)).

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

**Dominant (C2B missense/in-frame) branch:**
1. Heterozygous **C2B-domain missense/in-frame variant** in SYT2 (e.g., p.Asp307Ala disrupting an essential Ca²⁺-coordinating aspartate) **produces** a mutant synaptotagmin-2 protein that still incorporates into the release machinery.
2. The mutant protein **acts dominant-negatively**, poisoning the Ca²⁺-sensing/SNARE-coupling function of the release apparatus even in the presence of one wild-type allele (demonstrated in *Drosophila*, where co-expression with one wild-type copy reproduces disease) → **impaired coupling of Ca²⁺ influx to synchronous synaptic-vesicle fusion**.
3. This **results in** reduced quantal content (fewer ACh quanta released per nerve impulse), most evident at low stimulation frequencies.
4. Reduced ACh release **leads to** an endplate potential that intermittently fails to reach threshold → **intermittent neuromuscular transmission failure** → fatigable weakness.
5. Because residual Ca²⁺ accumulates in the terminal during repetitive/high-frequency activity, release transiently improves → **facilitation/post-exercise increment and prolonged post-tetanic potentiation** (the LEMS-like signature).
6. Chronic presynaptic dysfunction **is associated with** a secondary distal **motor neuropathy/terminal remodeling** → distal wasting, pes cavus, areflexia → the clinical phenotype.

**Recessive (biallelic LoF) branch:**
1. **Biallelic loss-of-function variants** (frameshift/nonsense/splice/deletion) **result in** absent or non-functional SYT2 protein.
2. Loss of the principal fast Ca²⁺ sensor **leads to** profound impairment of synchronous ACh release (more severe presynaptic failure than the dominant form).
3. This **results in** congenital-onset severe weakness, hypotonia, bulbar and respiratory compromise. *(The C-terminal recessive variant p.Arg397Serfs*37 disrupts a region crucial for synaptotagmin–SNARE interaction and exocytosis — inferred from structural modeling on the rat Syt1 C2B template.)*

### Molecular / cellular detail (checklist)

- **Molecular pathways / biochemical defect.** Ca²⁺-triggered synaptic-vesicle exocytosis; SYT2 is the Ca²⁺ sensor that couples voltage-gated Ca²⁺ influx to SNARE-mediated membrane fusion. The core defect is an **ion-sensor/receptor-coupling failure**, not an enzyme deficiency (F002; [PMID: 17521570](https://pubmed.ncbi.nlm.nih.gov/17521570/)). Suggested GO: **GO:0016079** (synaptic vesicle exocytosis), **GO:0017156** (calcium-ion-regulated exocytosis), **GO:0005544** (calcium-dependent phospholipid binding).
- **Cellular processes.** Presynaptic vesicle fusion, endocytic recycling, and — in the recessive form — ultrastructural remodeling of the nerve terminal (F006).
- **Protein dysfunction.** Dominant = dominant-negative interference; recessive = loss of function. C2B Ca²⁺-binding-pocket modeling (SwissModel) predicts structural disruption for pathogenic variants (F009; [PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/), [PMID: 28953919](https://pubmed.ncbi.nlm.nih.gov/28953919/)).
- **Metabolic / immune involvement.** None — no metabolic derangement and **no autoimmunity** (ACh-receptor and VGCC antibodies negative), which distinguishes CMS7 from MG and autoimmune LEMS (F011).
- **Molecular profiling (electrophysiology & ultrastructure).** Microelectrode studies in the dominant form show **markedly reduced quantal content that increases linearly with higher stimulation frequencies**; MEPP frequency is normal at rest but rises with stimulation. Electron microscopy shows **overdeveloped postsynaptic folding and abundant endosomes, multivesicular bodies, and degenerative lamellar bodies within small nerve terminals**; presynaptic failure is more prominent in the recessive form (F006; [PMID: 34037996](https://pubmed.ncbi.nlm.nih.gov/34037996/)).

**Upstream vs downstream.** Upstream = SYT2 variant → defective Ca²⁺-sensing/SNARE coupling. Downstream = reduced quantal ACh release → EPP failure → fatigable weakness, with facilitation as a distinctive downstream compensatory readout, and secondary distal neuropathy/terminal remodeling as a chronic downstream consequence.

**Cell types & CL terms.** Presynaptic **motor neuron / lower motor neuron** terminal (**CL:0000100** motor neuron; **CL:0011001** spinal cord motor neuron) and the **skeletal muscle fiber** (**CL:0000188**) postsynaptic partner.

---

## 7. Anatomical Structures Affected

- **Organ / system level.** Primary target is the **peripheral nervous system–muscle interface**: the **neuromuscular junction** (**UBERON:0002476**, neuromuscular junction; **GO:0031594** neuromuscular junction as a cellular component). Body systems: **somatic motor / musculoskeletal** and, secondarily, **respiratory** (respiratory muscle involvement in severe recessive disease) and **bulbar** musculature.
- **Tissue / cell level.** **Skeletal (striated) muscle** (**UBERON:0001134**) and the presynaptic **motor neuron terminal**. Predominant clinical involvement is **distal lower limb** in the dominant form; generalized/axial and bulbar/respiratory in the recessive form.
- **Subcellular level.** **Synaptic vesicle** and **presynaptic active zone** membranes (**GO:0008021** synaptic vesicle; **GO:0048786** presynaptic active zone). Ultrastructurally, endosomes, multivesicular bodies, and lamellar bodies accumulate in nerve terminals (F006).
- **Localization / lateralization.** Symmetric, **bilateral** involvement; distal-predominant in the dominant form. Specific sites: lower-limb muscles and feet (pes cavus). UBERON: **UBERON:0002103** (hindlimb), **UBERON:0002387** (pes/foot).

---

## 8. Temporal Development

- **Onset.** **Congenital / neonatal** in the recessive form (hypotonia, weak cry, feeding/respiratory problems from birth); **childhood-onset** distal weakness typical in the dominant form, with some presentations recognized later. Onset pattern is **chronic/insidious** rather than acute (F005, F012).
- **Progression.** Dominant form: **stable or slowly progressive**, described in the seminal report as a *"nonprogressive motor neuropathy"* and in the biallelic series as *"stable or slowly progressive distal weakness of variable severity"* (F012; [PMID: 25192047](https://pubmed.ncbi.nlm.nih.gov/25192047/), [PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)). Recessive form: severe from birth with variable respiratory course.
- **Course pattern & duration.** **Chronic, lifelong**, with a **fluctuating/fatigable** functional pattern superimposed on a stable structural baseline. No spontaneous remission is described; symptomatic improvement is **treatment-induced** (3,4-DAP, AChE inhibitors).
- **Critical periods.** The neonatal/infantile period is the window of greatest vulnerability (respiratory failure risk) and the key window for diagnosis and initiation of treatment in the severe recessive form.

---

## 9. Inheritance and Population

**Epidemiology.** CMS7/SYT2-CMS is **ultra-rare**. Genetically confirmed CMS overall prevalence is estimated at **6.5 per million overall and 8.5 per million in the pediatric population** in the UK (n=442 cohort; F004; [PMID: 41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/)), with an earlier estimate of **9.2 per million** ([PMID: 34736634](https://pubmed.ncbi.nlm.nih.gov/34736634/)). The most common CMS subtypes are CHRNE, DOK7, and RAPSN; **SYT2-CMS is one of the rarest presynaptic subtypes, with only ~10–15 families reported worldwide** across dominant and recessive forms (F004). No incidence figures are available specifically for CMS7.

**Inheritance genetics (F010, F013).**

| Feature | Dominant (CMS7A) | Recessive (CMS7B) |
|---|---|---|
| Pattern | Autosomal dominant (multigenerational or de novo) | Autosomal recessive |
| Variant class | C2B missense / in-frame | Biallelic LoF (frameshift/nonsense/splice/deletion) |
| Mechanism | Dominant-negative | Loss of function |
| Penetrance | High (segregates in families; de novo cases) | High |
| Consanguinity | Not typically | Frequently present |
| Severity | Milder, slowly progressive | Severe, congenital |

De novo dominant occurrence is documented (*"a new de novo heterozygous in frame deletion of the SYT2 gene"*; [PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/)). Recessive disease is documented across multiple consanguineous families (*"we report seven patients of five families, with biallelic loss of function variants in SYT2"*; [PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)).

**Penetrance, expressivity, anticipation, mosaicism, founder effects.** Penetrance appears **high**; expressivity is **variable** (severity gradient by allele type). **No genetic anticipation** (not a repeat-expansion disorder). No germline mosaicism or founder effects reported. **Carrier frequency** is not quantifiable — pathogenic variants are absent/singleton in gnomAD (F013).

**Population demographics.** No ethnic predilection beyond the association of the recessive form with **consanguineous** populations. No sex bias reported; both sexes affected (autosomal). Geographic distribution: cases reported across Europe, the Middle East, and Asia — sporadic, without endemic clustering.

---

## 10. Diagnostics

Diagnosis integrates **presynaptic electrophysiology** with **molecular genetics** (F011).

**Electrophysiology (the diagnostic hallmark).** Repetitive nerve stimulation (RNS) shows **low baseline CMAP amplitude**, a **decremental response at low frequency**, and a **marked increment/facilitation after brief exercise or high-frequency stimulation**, with **prolonged post-tetanic potentiation lasting up to ~60 minutes** and single-fiber EMG jitter/blocking — a LEMS-like presynaptic signature (F006, F011; [PMID: 26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/): *"Electrophysiologic testing revealed features indicative of a presynaptic deficit in neurotransmitter release with posttetanic potentiation lasting up to 60 minutes"*; [PMID: 29696584](https://pubmed.ncbi.nlm.nih.gov/29696584/): *"They have low compound muscular action potential amplitude that increment after brief exercise (facilitation) or high-frequency repetitive nerve stimulation"*).

**Laboratory.** CK normal or mildly elevated (e.g., 501 U/L; [PMID: 41331967](https://pubmed.ncbi.nlm.nih.gov/41331967/)). **ACh-receptor and VGCC antibodies negative** — critical for excluding autoimmune MG/LEMS.

**Genetic testing.** SYT2 is identified via **whole-exome sequencing** and **multigene CMS/neuromuscular NGS panels**, with Sanger confirmation; **chromosomal microarray/exome** can detect large exonic deletions (the exons 2–9 deletion; [PMID: 36722210](https://pubmed.ncbi.nlm.nih.gov/36722210/)). Because CMS is now attributable to **~40 genes**, panel/exome testing is the standard first-line molecular approach ([PMID: 40533459](https://pubmed.ncbi.nlm.nih.gov/40533459/), [PMID: 36835142](https://pubmed.ncbi.nlm.nih.gov/36835142/)). Single-gene SYT2 testing is appropriate when the LEMS-like presynaptic phenotype is recognized. WGS is useful for deep-intronic/structural variants when panel/exome is negative. Mitochondrial DNA testing, karyotyping, FISH, and repeat-expansion testing are **not indicated**.

**Muscle biopsy / pathology.** Typically shows only **mild/nonspecific neurogenic** features; EM (research setting) shows the terminal remodeling described above (F006; [PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/)).

**Differential diagnosis.** Autoimmune LEMS (antibody-positive, often paraneoplastic); other presynaptic CMS (AGRN, VAMP1, UNC13A/MUNC13-1, LAMA5, SLC5A7, SLC18A3); distal hereditary motor neuropathy / Charcot–Marie–Tooth; spinal muscular atrophy; and congenital myopathies (F011; [PMID: 29696584](https://pubmed.ncbi.nlm.nih.gov/29696584/), [PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/)).

**Screening.** No population newborn screening exists for CMS7. **Cascade genetic testing** of relatives and, where a familial variant is known, prenatal/preimplantation options apply.

---

## 11. Outcome / Prognosis

- **Survival / mortality.** No formal survival statistics exist. The dominant form is compatible with normal life expectancy. In the severe recessive form, **respiratory insufficiency and recurrent respiratory infections** are the principal drivers of morbidity and potential mortality (F012; [PMID: 41331967](https://pubmed.ncbi.nlm.nih.gov/41331967/), [PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)).
- **Morbidity / function.** Dominant form: mobility limitation from distal weakness and foot deformity, fatigue. Recessive form: major disability with feeding/respiratory support needs in infancy.
- **Disease course & recovery.** Symptoms are chronic; **substantial functional improvement is achievable with treatment** even in severe recessive disease — *"Treatment with an acetylcholinesterase inhibitor pursued in three patients showed clinical improvement with increased strength and function"* ([PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)).
- **Prognostic factors.** The strongest prognostic determinant is **allele class / inheritance mode** (dominant missense = milder; biallelic LoF = severe), followed by degree of respiratory involvement and treatment responsiveness. No molecular prognostic biomarkers beyond genotype.

---

## 12. Treatment

CMS7 is **treatable**, and — as in CMS generally — the choice of agent is **subtype-specific** (F003; [PMID: 30032336](https://pubmed.ncbi.nlm.nih.gov/30032336/)). There is **no role for immunotherapy** (it is not autoimmune).

| Therapy | Class / mechanism | Evidence in SYT2-CMS | Suggested NCIT |
|---|---|---|---|
| **3,4-Diaminopyridine (amifampridine)** | K⁺-channel blocker; prolongs presynaptic depolarization → more Ca²⁺ influx → more ACh release | Clinical benefit + improved neuromuscular transmission in dominant form ([PMID: 26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/)); ameliorated fatigue in recessive form ([PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/)) | NCIT:C61693 (Amifampridine) |
| **Pyridostigmine** (AChE inhibitor) | Prolongs ACh at the endplate | Ameliorated fatigue in recessive case ([PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/)); AChE-inhibitor improved strength/function in biallelic patients ([PMID: 32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/)) | NCIT:C739 (Pyridostigmine) |
| **Salbutamol / albuterol** (β2-agonist) | β-adrenergic modulation of endplate | **Mixed/limited**: improved patient-reported fatigue but no clear motor/neurophysiologic benefit in NMJ-involving motor neuropathies incl. SYT2 ([PMID: 36869887](https://pubmed.ncbi.nlm.nih.gov/36869887/)); **ineffective** in one recessive case ([PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/)) | NCIT:C29082 (Albuterol) |

Mechanistically, 3,4-DAP is the rational first-line agent for a presynaptic release deficit because it augments Ca²⁺ influx and quantal release; AChE inhibitors are a useful adjunct/alternative. The pharmacologic logic mirrors treatment of LEMS. Broader CMS treatment principles: *"Cholinergic agents, β-adrenergic agonists, and open-channel blockers remain the principal treatment modalities,"* and pyridostigmine should be **avoided** in DOK7, AChE deficiency, and slow-channel CMS — underscoring the necessity of an accurate genetic diagnosis before treatment ([PMID: 30032336](https://pubmed.ncbi.nlm.nih.gov/30032336/)).

**Supportive / rehabilitative.** Respiratory support and infection management (severe recessive disease), physical/occupational therapy, orthotic management of foot deformities, and nutritional/feeding support in infancy.

**Advanced/experimental therapeutics.** None approved specifically for CMS7. No gene, cell, or RNA therapy exists. A research-stage delivery concept exploits SYT2's luminal domain: intravenously administered **anti-SYT2 antibodies selectively localize to NMJs** and are retrogradely transported to motor neurons — a potential future neuron-targeted delivery route rather than a CMS7 therapy ([PMID: 40454418](https://pubmed.ncbi.nlm.nih.gov/40454418/)).

**Pharmacogenomics / personalized medicine.** Treatment is effectively **genotype-guided** at the level of CMS subtype (presynaptic → 3,4-DAP/AChE inhibitor). No SYT2-specific pharmacogenomic variants are described.

---

## 13. Prevention

CMS7 is a Mendelian disorder, so prevention is **genetic**, not behavioral or environmental.

- **Primary prevention.** Not applicable in the public-health sense. The relevant tools are **genetic counseling**, **carrier testing** of at-risk relatives (recessive form), and reproductive options — **prenatal diagnosis** and **preimplantation genetic testing** — where a familial pathogenic variant is known.
- **Secondary prevention.** Early recognition of the LEMS-like presynaptic electrophysiology → prompt genetic diagnosis → early initiation of 3,4-DAP/AChE inhibitors to prevent avoidable disability; vigilant respiratory monitoring and prompt treatment of respiratory infections in the severe recessive form.
- **Tertiary prevention.** Respiratory support, immunization against respiratory pathogens (influenza, pneumococcus) to reduce infection-triggered crises, orthopedic/rehabilitative management of contractures and foot deformities.
- **Counseling.** Recurrence risk is **50%** for offspring of a dominant-variant carrier and **25%** for siblings in recessive families; consanguinity counseling is relevant.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** SYT2 is evolutionarily conserved. Mouse **Syt2** (NCBI Gene 20680) is the ortholog and is the major fast-release Ca²⁺ sensor in caudal brain/brainstem and motor neurons (F009; [PMID: 17521570](https://pubmed.ncbi.nlm.nih.gov/17521570/), [PMID: 20729199](https://pubmed.ncbi.nlm.nih.gov/20729199/)). *Drosophila melanogaster* synaptotagmin is functionally orthologous for modeling purposes. NCBI Taxa: *Mus musculus* (10090), *Drosophila melanogaster* (7227).
- **Natural disease in other species.** No naturally occurring SYT2 congenital myasthenic syndrome has been reported in companion animals or wildlife (no OMIA entry noted); CMS7 is, to date, a human-described disease with experimental animal models rather than a recognized spontaneous veterinary disease. (Not available.)
- **Comparative biology.** The evolutionary conservation of synaptotagmin's Ca²⁺-sensor function underpins the validity of invertebrate and rodent models; the fly heterozygous model recapitulates the human dominant-negative phenotype (see Section 15).

---

## 15. Model Organisms

- **Drosophila melanogaster (primary causality model).** Expressing the human-homologous C2B mutation (P308-equivalent) in flies **lacking native synaptotagmin was lethal**, demonstrating the residue is critical for synaptotagmin function; **co-expression with one wild-type copy** (mimicking the heterozygous human state) produced **neurological/behavioral manifestations similar to patients** and **dominant disruption of synaptic-vesicle exocytosis** — directly establishing pathogenicity and the dominant-negative mechanism (F009; [PMID: 28953919](https://pubmed.ncbi.nlm.nih.gov/28953919/): *"When expressed in the absence of native synaptotagmin, this mutation is lethal, demonstrating for the first time that this residue plays a critical role in synaptotagmin function"* and *"Drosophila carrying this mutation developed neurological and behavioral manifestations similar to those of human patients"*).
- **Mouse (Syt2).** The mouse ortholog is the validated fast-release Ca²⁺ sensor for brainstem/motor-neuron synapses ([PMID: 17521570](https://pubmed.ncbi.nlm.nih.gov/17521570/)); Syt2-manipulated rodents inform normal SYT2 physiology, though a dedicated CMS7 patient-variant knock-in mouse is not prominently reported.
- **In silico / structural modeling.** C2B Ca²⁺-binding-pocket modeling (SwissModel; rat Syt1 C2B X-ray template) predicts structural disruption for pathogenic variants and supports variant interpretation ([PMID: 33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/), [PMID: 32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/)).
- **Phenotype recapitulation & limitations.** The fly model faithfully reproduces the **dominant-negative exocytosis defect and dominant inheritance**; it does not capture the human distal motor-neuropathy/foot-deformity phenotype or the recessive LoF disease, and mammalian models specifically engineered with patient recessive alleles are lacking. Applications: dissecting Ca²⁺-sensing/SNARE coupling, dominant-negative mechanism, and candidate therapeutics.

---

## Mechanistic Model / Interpretation

```
                 SYT2 (1q32.1) — Ca2+ sensor for fast synchronous ACh release
                                     |
        +----------------------------+-----------------------------+
   DOMINANT branch                                          RECESSIVE branch
   Heterozygous C2B missense/in-frame                  Biallelic LoF (fs/nonsense/
   (p.Asp307Ala, p.Pro308Leu, in-frame del)            splice/large deletion)
        |                                                       |
   Dominant-negative protein                               Absent/nonfunctional SYT2
   poisons release machinery                                   |
        |                                                       |
        +----------------> Impaired Ca2+->SNARE coupling <------+
                                     |
                     Reduced quantal ACh release per impulse
                                     |
                     Endplate potential intermittently subthreshold
                                     |
              +----------------------+-----------------------------+
      Fatigable weakness                          Facilitation / post-exercise
      (RNS decrement at low Hz)                    increment; prolonged PTP (~60 min)
                                     |
              Chronic terminal remodeling -> distal motor neuropathy
              (distal wasting, pes cavus, areflexia)
                                     |
      Dominant: milder, slowly progressive | Recessive: severe congenital,
      treatable (3,4-DAP, AChE inhibitors)  | bulbar/respiratory, treatable
```

The unifying concept is that **CMS7 is a disorder of presynaptic quantal release** in which allele class dictates severity: a poisoning (dominant-negative) mechanism produces a milder, distal, neuropathy-mimicking disease, while complete loss of the fast Ca²⁺ sensor produces severe congenital myasthenia. The **facilitation** phenomenon — pathognomonic on electrophysiology — is the direct downstream readout of residual Ca²⁺ rescuing release during repetitive activity, and it is precisely this mechanism that **3,4-DAP exploits therapeutically**.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [25192047](https://pubmed.ncbi.nlm.nih.gov/25192047/) | Seminal disease-gene report; dominant C2B missense variants; AD LEMS-like + nonprogressive motor neuropathy |
| [26519543](https://pubmed.ncbi.nlm.nih.gov/26519543/) | Electrophysiology (presynaptic deficit, prolonged PTP) and 3,4-DAP treatability in dominant form |
| [34037996](https://pubmed.ncbi.nlm.nih.gov/34037996/) | Dominant vs recessive comparison; quantal-content and EM ultrastructural findings |
| [32776697](https://pubmed.ncbi.nlm.nih.gov/32776697/) | Biallelic LoF recessive CMS7; AChE-inhibitor benefit; stable/slowly progressive course |
| [32250532](https://pubmed.ncbi.nlm.nih.gov/32250532/) | Recessive p.Arg397Serfs*37; 3,4-DAP/pyridostigmine effective, albuterol ineffective; C-terminal SNARE-interaction modeling |
| [33659639](https://pubmed.ncbi.nlm.nih.gov/33659639/) | New homozygous recessive variants (c.465+1G>A, c.328_331dup); myopathy-mimicking presentation |
| [33320396](https://pubmed.ncbi.nlm.nih.gov/33320396/) | De novo dominant in-frame deletion; CMT/neuropathy mimic; genetic-testing recommendation |
| [36722210](https://pubmed.ncbi.nlm.nih.gov/36722210/) | Large exonic deletion (exons 2–9) detected by exome+microarray; consanguineous recessive |
| [28953919](https://pubmed.ncbi.nlm.nih.gov/28953919/) | Drosophila model establishing causality and dominant-negative mechanism |
| [17521570](https://pubmed.ncbi.nlm.nih.gov/17521570/) | SYT1/2/9 as fast-release Ca²⁺ sensors; SYT2 as major NMJ isoform |
| [29696584](https://pubmed.ncbi.nlm.nih.gov/29696584/) | Places SYT2 in the CMS-LEMS presynaptic group; defines facilitation hallmark |
| [30032336](https://pubmed.ncbi.nlm.nih.gov/30032336/) | CMS treatment principles; subtype-specific drug choice; no immunotherapy |
| [41331967](https://pubmed.ncbi.nlm.nih.gov/41331967/) | 28-case review; core phenotype; C2B clustering; representative case features |
| [41251564](https://pubmed.ncbi.nlm.nih.gov/41251564/) | UK CMS prevalence (6.5/8.5 per million) |
| [34736634](https://pubmed.ncbi.nlm.nih.gov/34736634/) | Earlier CMS prevalence (9.2 per million); >30 genes |
| [40533459](https://pubmed.ncbi.nlm.nih.gov/40533459/) / [36835142](https://pubmed.ncbi.nlm.nih.gov/36835142/) | 40- and 35-gene CMS reviews; panel/exome testing standard |
| [36869887](https://pubmed.ncbi.nlm.nih.gov/36869887/) | Salbutamol trial in NMJ-involving motor neuropathies incl. SYT2 |
| [20729199](https://pubmed.ncbi.nlm.nih.gov/20729199/) | SYT2 regulation/expression biology (calmodulin, rostral–caudal) |
| [40454418](https://pubmed.ncbi.nlm.nih.gov/40454418/) | Anti-SYT2 luminal-domain antibody NMJ targeting (future delivery concept) |

All quoted snippets above are verbatim from the corresponding abstracts as recorded in the knowledge state (findings F001–F013).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → weak epidemiology.** Only ~10–15 families are reported worldwide; there are **no CMS7-specific prevalence/incidence figures, no natural-history registries, and no formal survival/QoL data**. Prevalence is inferred from all-CMS studies.
2. **No controlled treatment trials.** Efficacy of 3,4-DAP and AChE inhibitors rests on **case reports and small series**, not randomized data. Salbutamol data are mixed and derive from a heterogeneous cohort.
3. **Genotype–phenotype correlation incomplete.** The dominant-negative vs LoF dichotomy is well supported, but finer correlations (specific variant → severity/organ involvement) remain anecdotal.
4. **Model-organism gaps.** Causality is proven in *Drosophila*; a mammalian knock-in carrying a patient dominant allele, and models of the recessive LoF disease, are lacking — limiting preclinical therapeutic testing.
5. **No modifier/epigenetic data.** No modifier genes, epigenetic marks, or environmental modifiers have been identified.
6. **QoL/functional instruments unmeasured.** No EQ-5D/SF-36/PROMIS or ICF-based disability data specific to CMS7.

---

## Proposed Follow-up Experiments / Actions

1. **International SYT2-CMS registry.** Aggregate all reported and unpublished cases to derive genotype-stratified natural history, treatment-response rates, and survival — the single highest-value action given rarity.
2. **Prospective, protocolized 3,4-DAP ± pyridostigmine response study.** Standardized RNS/CMAP endpoints plus patient-reported fatigue to formalize the treatment evidence base (currently case-level).
3. **Patient-variant knock-in mouse models.** Generate C2B dominant-negative (e.g., p.Asp307Ala) and biallelic-LoF mice to reproduce distal neuropathy and severe congenital disease respectively, and to test therapeutics.
4. **Structure-function dissection of C2B variants.** Combine cryo-EM/AlphaFold modeling with electrophysiology in reconstituted or iPSC-derived motor-neuron/NMJ systems to map how each variant perturbs Ca²⁺ binding and SNARE coupling.
5. **iPSC-derived motor neuron / NMJ-on-chip modeling.** Patient-derived systems to screen candidate presynaptic-release enhancers beyond 3,4-DAP.
6. **Explore SYT2-targeted delivery.** Evaluate the anti-SYT2 luminal-domain NMJ-targeting antibody shuttle ([PMID: 40454418](https://pubmed.ncbi.nlm.nih.gov/40454418/)) as a route for future gene- or protein-replacement approaches to the recessive LoF form.
7. **Refine diagnostic pathways.** Promote recognition of the LEMS-like presynaptic RNS signature in antibody-negative patients to shorten time-to-genetic-diagnosis and ensure SYT2 is on CMS/neuropathy NGS panels.

---

*Report compiled from 13 confirmed findings (F001–F013) across 29 reviewed publications. Evidence types: predominantly human clinical case reports/series and comprehensive reviews, supplemented by a Drosophila causality model, rodent/in-vitro SYT2 physiology, and computational (gnomAD constraint, structural modeling) analyses.*


## Artifacts

- [OpenScientist final report](Congenital_Myasthenic_Syndrome_7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myasthenic_Syndrome_7-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 10 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:41251564` (3 mentions) - Prevalence and Geographical Distribution of Patients With Congenital Myasthenic Syndromes in the United Kingdom.
  - shared terms: congenital

Weighed against this report's own most characteristic terms: `recessive`, `disease`, `cms7`, `dominant`, `syt2`, `form`, `variant`, `severe`, `presynaptic`, `motor`, `gene`, `distal`, `dominant-negative`, `respiratory`, `congenital`, `c2b`, `release`, `function`, `mechanism`, `biallelic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
