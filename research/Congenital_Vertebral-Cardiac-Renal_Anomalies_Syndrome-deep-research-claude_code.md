---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T07:27:24.853339'
end_time: '2026-09-03T07:33:33.611644'
duration_seconds: 368.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Vertebral-Cardiac-Renal Anomalies Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 22
  total_cost_usd: 1.4919719999999996
  session_id: b09c6450-ce83-573e-a4a4-044c22fd0e04
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Vertebral-Cardiac-Renal Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Vertebral-Cardiac-Renal Anomalies Syndrome** covering all of the
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

I now have comprehensive, well-sourced material spanning the disease's identity, molecular genetics, mechanism, phenotype spectrum, diagnostics, management, and 2023–2025 developments. Here is the full research report.

---

# Congenital Vertebral-Cardiac-Renal Anomalies Syndrome (Congenital NAD Deficiency Disorder)

## 1. Disease Information

**Overview.** Congenital Vertebral-Cardiac-Renal Anomalies Syndrome is the Orphanet/MONDO name for a rare, genetically heterogeneous, autosomal recessive multiple-congenital-anomaly disorder caused by biallelic loss-of-function variants in the de novo NAD⁺ (nicotinamide adenine dinucleotide) biosynthesis pathway. The umbrella clinical/molecular entity is now widely referred to in the literature as **Congenital NAD Deficiency Disorder (CNDD)** — a name adopted after the causal mechanism was discovered in 2017. CNDD is genetically heterogeneous, comprising three OMIM-numbered subtypes distinguished by which pathway enzyme is disrupted:

| Subtype | OMIM | Gene | Enzyme |
|---|---|---|---|
| VCRL1 | #617660 | *HAAO* | 3-hydroxyanthranilate 3,4-dioxygenase |
| VCRL2 | #617661 | *KYNU* | Kynureninase |
| VCRL3 | #618845 | *NADSYN1* | Glutamine-dependent NAD⁺ synthetase |

Notably, the specific Orphanet/MONDO entity named "Congenital vertebral-cardiac-renal anomalies syndrome" (ORPHA:521438; also indexed as MONDO_0020831 on Open Targets) is described with the severe, infancy-lethal phenotype (hypoplastic/absent left ventricle, transposition of the great arteries, absent pulmonary trunk, hypoplastic/absent kidneys) that corresponds most closely to **VCRL3/NADSYN1 (OMIM #618845)**, while the broader GeneReviews chapter "Congenital NAD Deficiency Disorder" (NBK593504) treats all three genes (HAAO/KYNU/NADSYN1) as one clinically overlapping spectrum. Curators should be aware of this granularity mismatch: the named "vertebral-cardiac-renal anomalies syndrome" label leans toward the NADSYN1-associated, most-severe end of the CNDD spectrum, but shares identical mechanism, evidence base, and management guidance with the HAAO- and KYNU-associated forms.

**Key identifiers:**
- **OMIM:** #617660 (VCRL1/HAAO), #617661 (VCRL2/KYNU), #618845 (VCRL3/NADSYN1)
- **Orphanet:** ORPHA:521438
- **MONDO:** MONDO:0020831 (per Open Targets); the term is also cataloged as MONDO:0030077 in some secondary listings — verify against the live MONDO release before binding
- **GARD (NCATS/NIH):** Disease ID 17961
- **GeneReviews:** NBK593504 ("Congenital NAD Deficiency Disorder")
- **MedGen Concept IDs:** C4540004 (VCRL1), C4540014 (VCRL2), C5394250 (VCRL3)
- **Gene OMIM (*):** HAAO 604521; KYNU 605197; NADSYN1 608285

**Synonyms:** VCRL syndrome; Vertebral, Cardiac, Renal, and Limb Defects syndrome (1/2/3); Congenital NAD Deficiency Disorder (CNDD); HAAO-related / KYNU-related / NADSYN1-related multiple congenital anomaly syndrome; historically overlaps in the literature with "VACTERL-like association of genetic cause."

**Source of information:** Nearly all clinical knowledge derives from **aggregated disease-level resources** — case series and cohort reviews assembled from published case reports (OMIM, GeneReviews, Orphanet) rather than large prospective EHR cohorts, reflecting the rarity of the condition (GeneReviews July 2023 update: 27 reported individuals from 25 families worldwide, of whom 16 were living at time of publication).

---

## 2. Etiology

**Disease causal factors — genetic.** CNDD is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants** in one of three non-redundant genes encoding sequential enzymes of the de novo NAD⁺ synthesis pathway from dietary tryptophan: *HAAO*, *KYNU*, and *NADSYN1*. The founding paper, Shi et al. 2017 (PMID: 28792876, *N Engl J Med* 377:544–552), identified "variants … in two genes encoding enzymes of the kynurenine pathway, HAAO … and KYNU … Three patients carried homozygous variants predicting loss-of-function changes in the HAAO or KYNU proteins (HAAO p.D162*, HAAO p.W186*, or KYNU p.V57Efs*21)," and reported that "the patients had reduced levels of circulating NAD." NADSYN1 was subsequently established as a third causal gene by Szot et al. 2020 (PMID: 31883644, *Am J Hum Genet* 106:129–136), describing five individuals from four families with biallelic *NADSYN1* variants and phenotypes "rang[ing] from the isolated absence of both kidneys to multiple malformations of the vertebrae, heart, limbs, and kidney," with "no affected individual surviv[ing] for more than three months postnatally" in that severe cohort.

**Risk factors:**
- *Genetic:* Biallelic pathogenic/likely pathogenic variants in HAAO, KYNU, or NADSYN1 (per ACMG/AMP criteria, Richards et al. 2015, PMID: 25741868) are causal, not merely a risk factor — the disorder is fully penetrant when both alleles are null. Parental consanguinity substantially raises a priori risk in any autosomal recessive disorder; multiple reported families are consanguineous. A **maternal chromosome 2 isodisomy (uniparental disomy)** unmasking a homozygous *KYNU* exon-5 deletion has been documented as a distinct mechanism producing biallelic loss-of-function from a single carrier parent (Schüle et al. 2021, PMID: 34200361, *Genes* 12:879, "A Homozygous Deletion of Exon 5 of KYNU Resulting from a Maternal Chromosome 2 Isodisomy … Causes Catel-Manzke-Syndrome/VCRL Syndrome").
- *Environmental / maternal metabolic:* Because the terminal metabolite is the same essential cofactor (NAD⁺) required in the mother's own developing embryo, maternal **dietary niacin/tryptophan insufficiency**, and possibly maternal illness or drugs (e.g., isoniazid, which depletes vitamin B6 needed for kynurenine-pathway flux) that impair the mother's own NAD⁺ supply during the periconceptional/early-embryonic window, are hypothesized modifiers of severity and penetrance in genetically at-risk pregnancies, based on the mouse model data below (Shi et al. 2017).

**Protective factors:**
- **Genetic:** No protective alleles are established; heterozygous carriers of HAAO/KYNU/NADSYN1 variants are asymptomatic.
- **Environmental — niacin/nicotinamide supplementation.** This is the single most important modifiable factor identified for this disease class. Shi et al. 2017 showed in *Haao*-null and *Kynu*-null mouse embryos that malformations mirroring the human phenotype occur "owing to NAD deficiency," and that "niacin supplementation during gestation prevented the malformations in mice." Follow-on commentary (e.g., coverage of the Dunwoodie group's work, Victor Chang Cardiac Research Institute) proposed maternal supplementation strategies (in the range of ~140 mg/day investigated preclinically — roughly 10× the standard RDA for women) as a plausible clinical prevention strategy, though this has not yet been validated in a human interventional trial for genetically confirmed carrier couples. A broader systematic review/meta-analysis of maternal dietary niacin intake and congenital anomalies (PMID: 34748060) supports a population-level association between niacin status and malformation risk.

**Gene-environment interactions.** The core G×E model of this disease is that **haploinsufficient/heterozygous carrier status combines with maternal NAD⁺-precursor insufficiency** (low dietary tryptophan/niacin, malabsorption, or drugs interfering with kynurenine-pathway flux) to push total embryonic NAD⁺ below a mechanistic threshold during the vulnerable early-organogenesis window — while frank biallelic loss-of-function in the embryo itself produces a much larger, largely non-nutrition-rescuable NAD⁺ deficit. Mark 2022 (PMID: 35484986, *Am J Med Genet A* 188:2834–2849, "NAD+ deficiency in human congenital malformations and miscarriage: a new model of pleiotropy") proposes that this G×E axis underlies a wider group of overlapping malformation syndromes (VACTERL association, limb-body wall complex, pentalogy of Cantrell, OEIS complex, oculoauriculovertebral spectrum, MURCS, sirenomelia, urorectal septum malformation sequence) and recurrent miscarriage, framing NAD⁺ deficiency as a **pleiotropic developmental mechanism** rather than a single-syndrome cause.

---

## 3. Phenotypes

Phenotype frequencies below are drawn from the GeneReviews CNDD cohort synthesis (25–27 reported affected individuals; NBK593504, 2023 update) and the founding case series.

| Category | Frequency | Detail | Suggested HP term |
|---|---|---|---|
| **Congenital heart defect** | 100% (25/25) | Hypoplastic left heart (most common, 8 cases), tetralogy of Fallot (3), coarctation of the aorta, aortic stenosis, bicuspid aortic valve, mitral valve defects, absent pulmonary trunk, double-outlet right ventricle, ASD, PDA, transposition of the great arteries (in the most severe/NADSYN1-associated cases) | HP:0001627 (Abnormal heart morphology); HP:0004392 (Hypoplastic left heart); HP:0001636 (Tetralogy of Fallot); HP:0001680 (Coarctation of aorta) |
| **Short stature / growth failure** | 92% (12/13) | Height z-scores +0.25 to −6.1; often disproportionate, with shortened limbs | HP:0004322 (Short stature) |
| **Microcephaly** | 29% (7/24) | Z-scores −2.3 to −6.4 | HP:0000252 (Microcephaly) |
| **Vertebral segmentation anomalies** | 69% overall musculoskeletal; 18/26 vertebral specifically | Hemivertebrae, vertebral fusion, "butterfly" vertebrae, rib anomalies | HP:0003468 (Segmental instability of spine)/HP:0008619 (vertebral segmentation defect); HP:0002937 (Hemivertebrae) |
| **Limb anomalies** | 29% (7/24) | Hyperphalangism, short phalanges/metacarpals with accessory ossicles, shortened metatarsals, rhizomelia/brachymelia | HP:0001180 (Hyperphalangism); HP:0009601 (Ulnar deviation)/HP:0001156 (Brachydactyly) |
| **Cutaneous syndactyly** | 15% (4/26) | | HP:0001762 (Talipes equinovarus) / HP:0001548 |
| **Neuromuscular anomalies** | 22% (6/27) | Talipes, arthrogryposis, pterygia | HP:0001371 (Flexion contracture); HP:0002829 (Arthrogryposis multiplex congenita) |
| **Renal anomalies** | 59% | Dysplasia/hypoplasia (8), unilateral agenesis (6), bilateral agenesis, ureteral agenesis, hydronephrosis | HP:0000107 (Renal cyst); HP:0000089 (Renal hypoplasia/dysplasia); HP:0000122 (Unilateral renal agenesis) |
| **Developmental delay / intellectual disability** | 62% (8/13) | Ranges from normal to severe; one case with global delay + autism | HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability) |
| **Sensorineural hearing loss** | 15% (4/27) | With inner ear abnormalities | HP:0000407 (Sensorineural hearing impairment) |
| **Craniofacial dysmorphism** | 46% | Brachycephaly, prominent supraorbital ridges, hyper/hypotelorism, up/downslanting palpebral fissures, depressed nasal bridge, micrognathia, cleft soft palate — "no recognizable facial gestalt" | HP:0000369 (Low-set ears); HP:0000508 (Ptosis); HP:0000175 (Cleft palate) |
| **Endocrine** | rare | Congenital hypothyroidism (2 cases), hypoparathyroidism (1 case) | HP:0000821 (Hypothyroidism); HP:0000829 (Hypoparathyroidism) |
| **GI/other visceral** | occasional | Tracheoesophageal fistula, polysplenia, hepatomegaly, anteriorly displaced anus, pyloric stenosis | HP:0002575 (Tracheoesophageal fistula); HP:0009800 (Polysplenia) |
| **Ophthalmologic** | occasional | Strabismus, ptosis, ocular crystals, hypopigmented iris with nodules | HP:0000486 (Strabismus) |
| **Seizures** | rare | One reported Lennox-Gastaut-type case | HP:0002510 |

**Onset:** All features are congenital/present at birth or detected prenatally by ultrasound; severity spans a spectrum from prenatal loss/termination to survival into adulthood (oldest reported living patient: age 30, Erbs et al. 2023, PMID: 36649848). **Progression:** structural anomalies are static congenital malformations rather than progressive; secondary sequelae (e.g., chronic kidney disease from renal hypoplasia, scoliosis progression, hearing loss impact) can evolve postnatally and require longitudinal surveillance. **Quality of life impact:** driven mainly by the combination of congenital heart disease, renal insufficiency, developmental/intellectual disability, and orthopedic complications; no disease-specific QoL instrument has been published, but impact is analogous to other multi-system congenital anomaly syndromes requiring lifelong multidisciplinary care.

---

## 4. Genetic/Molecular Information

**Causal genes** (all three are non-redundant, sequential enzymes of the de novo NAD⁺ pathway):

| Gene | Locus | OMIM (gene) | HGNC | Protein | % of solved CNDD cases | Detection rate (sequence analysis) |
|---|---|---|---|---|---|---|
| HAAO | 2p21 | 604521 | HGNC:4796 | 3-hydroxyanthranilate 3,4-dioxygenase | ~18% | >99% |
| KYNU | 2q22.2 | 605197 | HGNC:6469 | Kynureninase | ~41% | >99% (sequence); rare additional yield from deletion/duplication testing) |
| NADSYN1 | 11q13.4 | 608285 | HGNC:29832 | Glutamine-dependent NAD⁺ synthetase | ~41% | >99% |

**Variant classification and type.** Reported variants span nonsense (e.g., HAAO p.D162*, p.W186*), frameshift (KYNU p.V57Efs*21), splice-site, missense (NADSYN1 p.A573T), and structural/copy-number variants (a homozygous KYNU exon-5 deletion via maternal isodisomy). All disease-causing genotypes are biallelic loss-of-function or severely hypomorphic, consistent with a straightforward **loss-of-function** mechanism (no dominant-negative or gain-of-function alleles reported). ACMG/AMP criteria (PMID: 25741868) are the standard classification framework applied in the primary literature (all reported variants pathogenic/likely pathogenic).

**Population allele frequency:** Individual causal variants are, as expected for an ultra-rare autosomal recessive disorder, absent or present only as very rare heterozygous alleles in gnomAD; no common founder variant has been reported across the described families (each family typically carries a private variant), though the maternal UPD2 case represents a distinct, non-Mendelian recurrence mechanism.

**Somatic vs. germline:** Exclusively **germline** — this is a developmental/Mendelian disorder, not a somatic/cancer-related condition.

**Functional consequences:** Uniform **loss of enzymatic function**, verified in several studies by in vitro expression assays showing "essentially abolished" enzyme activity for KYNU truncating alleles, and confirmed physiologically by reduced circulating NAD⁺ and accumulation of upstream pathway metabolites (3-hydroxyanthranilic acid [3HAA] elevated / NAD(H) reduced for HAAO; 3-hydroxykynurenine [3HK] elevated / NAD(H) reduced for KYNU).

**Modifier genes:** None formally established; phenotypic variability within and across families (even with identical genotypes) suggests unidentified genetic or environmental (maternal nutritional) modifiers, consistent with the mouse data showing rescue by maternal dietary niacin.

**Epigenetic information:** Not established as a primary mechanism for this disorder; NAD⁺ itself is a cofactor for epigenetic enzymes (sirtuins, PARPs), so downstream epigenetic dysregulation is mechanistically plausible but not directly documented in patient tissue to date.

**Chromosomal abnormalities:** Not a chromosomal/copy-number syndrome per se, though the KYNU exon-5 deletion via maternal isodisomy of chromosome 2 (Schüle et al. 2021) is a structural mechanism worth noting for differential/recurrence-risk counseling.

**Genetically related (allelic) disorders (per GeneReviews):**
- **HAAO:** no other associated phenotype reported.
- **KYNU:** biallelic variants can also cause isolated **hydroxykynureninuria (xanthurenic aciduria)** — a biochemical excretory phenotype without the full malformation syndrome — indicating allelic/dosage heterogeneity.
- **NADSYN1:** preliminary evidence (Lin et al. 2021, PMID: 34681008) suggests monoallelic variants may be associated with a milder spectrum of vertebral/cardiac/renal/limb/hepatic defects and intraspinal anomalies, though this requires confirmation.

**Suggested GO terms for pathway annotation:**
- GO:0034354 — "NAD biosynthesis via nicotinamide riboside salvage pathway" (salvage, contrast pathway)
- GO:0009435 — "NAD biosynthetic process" (parent term covering the de novo route)
- GO:0043420 — "anthranilate metabolic process"
- GO:0019805 — "quinolinate biosynthetic process" (product of the HAAO reaction, immediate NAD⁺ precursor)
- GO:0033721 — "3-hydroxyanthranilate 3,4-dioxygenase activity" (HAAO molecular function)
- GO:0030429 — "kynureninase activity" (KYNU molecular function)
- GO:0008795 — "NAD+ synthase activity" (NADSYN1 molecular function)

---

## 5. Environmental Information

**Environmental factors:** The dominant environmental modifier for this specific gene-driven disorder is **maternal NAD⁺-precursor (niacin/tryptophan) nutritional status** during the periconceptional and early-embryonic period, as established mechanistically in the Shi et al. 2017 mouse model. This is distinct from a classical toxin-exposure etiology — the "environmental" axis here operates through nutrient sufficiency for a genetically compromised biosynthetic pathway rather than through an exogenous toxicant.

**Lifestyle factors:** Maternal diet quality/adequacy of niacin (vitamin B3) and tryptophan intake is the principal modifiable lifestyle factor implicated; standard prenatal multivitamins in most jurisdictions do not include niacin at the doses studied preclinically (~140 mg/day, ~10× US RDA for women), so this is an area of active clinical translation rather than settled guideline recommendation.

**Infectious agents:** None implicated; this is a purely genetic/metabolic developmental disorder with no known infectious trigger.

**Drug/xenobiotic interactions (plausible, not disease-specific evidence):** Agents that deplete vitamin B6 (a cofactor for kynurenine-pathway enzymes upstream of HAAO/KYNU, e.g., isoniazid) or otherwise impair tryptophan/kynurenine-pathway flux are biologically plausible aggravating exposures in a genetically at-risk pregnancy, based on pathway biology, though disease-specific human data linking a named xenobiotic exposure to CNDD severity have not been published.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from initiating lesion to clinical manifestation):**

1. Biallelic loss-of-function variants in **HAAO**, **KYNU**, or **NADSYN1** each **abolish or severely reduce** the catalytic activity of a sequential enzyme in the de novo NAD⁺ biosynthesis pathway that converts dietary tryptophan → kynurenine → 3-hydroxykynurenine → 3-hydroxyanthranilic acid (HAAO substrate) → quinolinic acid → nicotinic acid adenine dinucleotide (NAAD) → **NAD⁺** (NADSYN1's product) — directly demonstrated by loss of enzymatic activity in expression assays (Shi et al. 2017, PMID:28792876).
2. This **leads to** accumulation of the immediate upstream metabolite for each block (3HAA for HAAO deficiency; 3HK for KYNU deficiency) and a **reduction in de novo–synthesized NAD⁺** — directly measured as reduced circulating NAD⁺/NADH in affected patients and in *Haao*-null/*Kynu*-null mouse embryos (demonstrated).
3. Because the **salvage pathway** cannot fully compensate during early embryogenesis (the bulk of adult cellular NAD⁺ is normally salvage-derived, but the embryo appears to rely disproportionately on de novo synthesis in a defined developmental window), this **results in** a critical, tissue-wide NAD⁺ deficit specifically during **early organogenesis** — inferred from the mouse rescue experiments and the stereotyped, organ-selective malformation pattern rather than directly visualized in human embryos (partly inferred).
4. NAD⁺ deficiency **impairs** core NAD⁺-dependent cellular processes required for organogenesis, including its role as an **electron acceptor for ATP synthesis** (oxidative phosphorylation/glycolysis), and as a substrate for NAD⁺-consuming enzymes (sirtuins, PARPs, cADPR synthases) that regulate chromatin state, DNA-damage response, and cell signaling — this **leads to** disrupted proliferation, differentiation, and patterning signals in the developing mesoderm-derived organ primordia (largely inferred from general NAD⁺ biology; not yet organ-specifically dissected in this disease).
5. Because heart, kidney, and vertebral column all arise from tightly time-linked mesodermal developmental programs active in the same early post-gastrulation window, this **results in** the disease's signature **co-occurring triad of cardiac, renal, and vertebral malformation**, with limb, craniofacial, and neurodevelopmental structures affected to a variable, generally lesser degree depending on the residual NAD⁺ level (dose-dependent severity — supported by the genotype-severity gradient across HAAO/KYNU vs. the more severe NADSYN1/VCRL3 cohort).
6. In the most severe cases (particularly biallelic NADSYN1 loss), this **leads to** profound structural cardiac defects (hypoplastic/absent left ventricle, transposition of the great arteries, absent pulmonary trunk) and bilateral renal agenesis/hypoplasia incompatible with postnatal survival — **resulting in** pregnancy loss or death within the first year of life (demonstrated clinically; Szot et al. 2020).
7. In milder allelic combinations (partial residual enzyme activity), this **results in** the broader, non-lethal CNDD phenotypic spectrum — short stature, isolated or combined vertebral/cardiac/renal/limb anomalies, developmental delay, and hearing loss — with survival into childhood and, in the mildest known case, adulthood (demonstrated).
8. Restoring embryonic NAD⁺ supply via maternal **dietary niacin supplementation during gestation** bypasses the enzymatic block (niacin enters NAD⁺ synthesis through the separate Preiss-Handler pathway, independent of HAAO/KYNU/NADSYN1) and **prevents** the malformation cascade in *Haao*-null and *Kynu*-null mouse embryos — demonstrated experimentally and the strongest direct mechanistic proof of the causal chain (Shi et al. 2017).

**Molecular pathways:** Kynurenine pathway / tryptophan catabolism (KEGG: hsa00380 Tryptophan metabolism); de novo NAD⁺ biosynthesis pathway (KEGG: hsa00760 Nicotinate and nicotinamide metabolism; Reactome: "Tryptophan catabolism"). No canonical developmental signaling pathway (Wnt/MAPK/mTOR) has been shown to be the direct downstream effector — the current model treats NAD⁺ depletion itself, and its downstream effects on ATP generation and NAD⁺-dependent enzymes, as the proximate lesion (Dunwoodie et al. 2023 review, "Nicotinamide Adenine Dinucleotide Deficiency and Its Impact on Mammalian Development," *Antioxid Redox Signal*, doi:10.1089/ars.2023.0349, is the most current mechanistic synthesis).

**Cellular processes:** Impaired cellular bioenergetics (ATP synthesis) and NAD⁺-dependent enzymatic signaling (sirtuin-mediated deacetylation, PARP-mediated DNA repair) in rapidly proliferating embryonic mesodermal progenitors during organogenesis are the leading hypothesized cellular mechanisms; oxidative stress has also been proposed as a downstream consequence of impaired NAD⁺/NADH redox balance.

**Protein dysfunction:** Straightforward **loss of enzymatic function** (not misfolding/aggregation) for HAAO, KYNU, and NADSYN1 — nonsense, frameshift, and splice variants predominate, consistent with a null mechanism; the one recurrent missense allele (NADSYN1 p.A573T) has been functionally shown to impair NAD⁺ synthetase activity in vitro.

**Metabolic changes:** Central to this disease — this is fundamentally a **tryptophan/NAD⁺ pathway metabolic disorder**. Biochemically diagnostic findings include elevated upstream metabolites (3HAA in HAAO deficiency; 3HK, xanthurenic acid, kynurenine in KYNU deficiency) and reduced NAD⁺/NADH; a dedicated "metabolic signature" study for NADSYN1-associated disease has been published (PMC10866660) proposing a biochemical biomarker panel for diagnosis/monitoring.

**Advanced/omics technologies:** A 2025 preprint/publication (Dunwoodie group, bioRxiv 10.1101/2025.01.10.632366; PMID: 39829932) establishes a **zebrafish model of NAD⁺ deficiency-derived congenital disorders**, extending the mouse data and explicitly raising the hypothesis that CNDD and VACTERL association "possess similar underlying causes," while noting that "the mechanism by which NAD⁺ deficiency causes CNDD developmental anomalies has not been determined" at the cellular/molecular signaling level — an open mechanistic gap appropriate to flag as a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion node in a KB entry (mouse/zebrafish recapitulate gross structural phenotype and confirm niacin rescue, but the precise cell-signaling explanation for organ selectivity remains undetermined).

**Suggested GO (biological process) / CL (cell type) terms:** GO:0009435 (NAD biosynthetic process), GO:0006979 (response to oxidative stress), GO:0006974 (cellular response to DNA damage stimulus, PARP-relevant); relevant cell types are broadly mesodermal cardiac progenitor cells (CL:0000499), metanephric mesenchyme/nephron progenitor cells (CL:1000384), and sclerotome-derived vertebral precursor cells — none of the primary literature has yet performed single-cell resolution of the affected embryonic compartments in this specific human disorder.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Heart (all major structural compartments — left ventricle, outflow tract, septa, valves), kidneys (parenchyma and collecting system), vertebral column (vertebral bodies, ribs). **Secondary/associated:** limbs (long bones, hands/feet), craniofacial skeleton and palate, inner ear, brain (microcephaly, hydrocephalus, cerebellar hypoplasia in a subset), thyroid and parathyroid glands, spleen (polysplenia), esophagus/trachea (TEF), eyes.

**Body systems involved:** Cardiovascular, renal/urinary, musculoskeletal (axial and appendicular), nervous (central and peripheral/hearing), endocrine, gastrointestinal, ophthalmologic, lymphatic (cystic hygroma).

**Suggested UBERON terms:** UBERON:0000948 (heart); UBERON:0002113 (kidney); UBERON:0002298 (vertebral column); UBERON:0002101 (limb); UBERON:0001456 (face); UBERON:0001690 (ear); UBERON:0000955 (brain); UBERON:0002046 (thyroid gland); UBERON:0001132 (parathyroid gland); UBERON:0002106 (spleen).

**Tissue/cell level:** Cardiac muscle and endocardial/outflow-tract mesenchyme; nephron epithelium and metanephric mesenchyme; sclerotome-derived vertebral chondro-osseous tissue; limb bud mesenchyme/chondrocytes. **Cell Ontology suggestions:** CL:0000746 (cardiac muscle cell), CL:0002518 (kidney epithelial cell), CL:0000138 (chondrocyte).

**Subcellular level:** Mitochondria (site of NAD⁺-dependent oxidative phosphorylation; GO:0005739) and nucleus (site of NAD⁺-dependent sirtuin/PARP chromatin and DNA-repair activity; GO:0005634) are the most mechanistically relevant compartments, given NAD⁺'s dual roles as a redox cofactor and enzymatic substrate.

**Localization/laterality:** Renal involvement can be unilateral (agenesis in 6 cases) or bilateral; cardiac and vertebral anomalies are generally midline/structural rather than strictly lateralized; limb involvement, when present, is typically bilateral and symmetric (consistent with a systemic metabolic rather than a focal teratogenic insult).

---

## 8. Temporal Development

**Onset:** Congenital — all structural anomalies originate during **embryonic organogenesis** (roughly weeks 3–8 post-conception for the heart, kidney, and vertebral primordia), detectable prenatally by ultrasound in many cases and at birth in others. This is a true prenatal-onset disorder; there is no pediatric/adult-onset variant.

**Progression:** The structural malformations themselves are **static** (fixed at the point of embryogenesis), but their **functional consequences progress postnatally** — e.g., renal hypoplasia can evolve into progressive chronic kidney disease, scoliosis from vertebral segmentation defects can worsen through skeletal growth, and developmental delay/intellectual disability trajectories unfold through childhood. Disease course is therefore best described as a **stable structural lesion with a progressive secondary functional burden**.

**Disease stages:** No formal staging system exists; clinical severity is best stratified by genotype/residual enzyme activity, ranging from prenatal lethality (most severe NADSYN1 cases) to survival into adulthood (mildest reported cases, oldest known patient age 30).

**Course pattern:** Non-relapsing, non-remitting — a fixed congenital anomaly burden with the natural history of any structural birth-defect syndrome (i.e., defined by the severity of the initial malformations rather than an episodic or fluctuating pathobiology).

**Critical period:** Explicitly established mechanistically — the mouse rescue experiments (Shi et al. 2017) demonstrate that maternal niacin supplementation **during gestation** (i.e., during the embryonic organogenesis window) is sufficient to prevent malformation, defining early gestation as the critical intervention window for any future preventive strategy in genetically at-risk pregnancies.

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — GeneReviews (2023) documents **27 reported affected individuals from 25 families worldwide** across all three genes combined, almost certainly an underascertainment given likely underdiagnosis of stillbirths/terminations and phenotypic overlap with VACTERL association. No formal population prevalence or incidence estimate (per 100,000) has been published; the disorder should be classified as **ultra-rare / cases-in-literature only** for prevalence-banding purposes.

**Inheritance pattern:** **Autosomal recessive** for all three subtypes (HAAO/KYNU/NADSYN1). GeneReviews: "The diagnosis of CNDD is established in a proband with suggestive findings and biallelic pathogenic variants in HAAO, KYNU, or NADSYN1."

**Penetrance:** Essentially complete for biallelic null genotypes, based on the consistency of the malformation phenotype across reported families, though expressivity (see below) varies widely.

**Expressivity:** Markedly **variable**, even for identical genotypes within a family, ranging from isolated bilateral renal agenesis to the full multi-organ syndrome — reflecting the hypothesized gene-environment (maternal NAD⁺ precursor sufficiency) interaction described in Section 2.

**Genetic anticipation:** Not applicable/not reported (mechanism is enzymatic loss-of-function, not a repeat-expansion disorder).

**Germline mosaicism:** Not directly documented but should be considered in recurrence-risk counseling per general AR-disorder practice; the GeneReviews chapter recommends confirmatory parental testing partly to exclude occult mosaicism/de novo scenarios.

**Founder effects:** No population-specific founder variant has been established; each reported family generally carries a private variant.

**Consanguinity:** A recognized risk factor, as for any rare autosomal recessive disorder; several reported families are consanguineous.

**Carrier frequency:** Not established (too rare for population carrier-frequency databases such as gnomAD to yield a meaningful estimate for any single pathogenic allele).

**Population demographics:** No ethnic, geographic, or sex-specific enrichment has been reported; cases have been described across multiple continents/ancestries in the literature (North America, Europe, Australia most represented, reflecting the discovering research groups' referral bases rather than a true epidemiological signal). No male:female skew is expected or reported for an autosomal recessive disorder.

**Age distribution:** By definition, congenital onset; postnatal survivors range from neonatal death (severe cases) to age 30 at last published report.

---

## 10. Diagnostics

**Suggestive findings** (GeneReviews): prenatal/postnatal imaging showing congenital heart defects (left- and/or right-sided), renal anomalies (aplasia/hypoplasia/dysplasia), vertebral anomalies (butterfly/hemi-/wedge/fused vertebrae), shortened long bones (rhizomelia/brachymelia), and short metacarpals with accessory ossicles; clinical findings of short stature, microcephaly, dysmorphic (cupped/low-set) ears, sensorineural hearing loss, nuchal redundancy/cystic hygroma, cutaneous syndactyly, hyperphalangism, developmental delay/ID, sacral dimple, clubfeet; and a compatible autosomal recessive family history (though its absence does not exclude the diagnosis).

**Establishing the diagnosis:** Biallelic pathogenic variants in HAAO, KYNU, or NADSYN1 confirmed by molecular genetic testing, via either:
1. A **gene-targeted VACTERL-association multigene panel** including HAAO, KYNU, NADSYN1 (sequence + deletion/duplication analysis), or
2. **Exome or genome sequencing** when the phenotype overlaps with other multiple-congenital-anomaly syndromes.

**Biochemical/metabolomic testing** (research/adjunct use): plasma/urine metabolite panels showing elevated upstream kynurenine-pathway intermediates (3HAA, 3HK, xanthurenic acid, kynurenine) and reduced NAD⁺/NADH; a dedicated NADSYN1 "metabolic signature" panel has been proposed (PMC10866660) as a functional confirmatory/monitoring tool alongside genetic testing.

**Imaging:** Fetal/postnatal echocardiography (cardiac defects), renal/bladder ultrasound (renal anomalies), spinal radiographs ± CT (vertebral segmentation), spinal ultrasound (<3 months) or MRI (>3 months) if dysraphism/tethered cord suspected, brain MRI if microcephaly/seizures/neuromuscular findings.

**Differential diagnosis** (GeneReviews, summarized):
- **VACTERL association** — the closest clinical mimic; distinguished by CNDD's relative rarity of anal atresia and tracheoesophageal fistula, and its higher frequency of disproportionate short stature, developmental delay, and facial dysmorphism. Mechanistic overlap is now an active research question (see Section 6).
- **Townes-Brocks syndrome** (SALL1, AD) — dysplastic/hearing-impaired ears and thumb malformations much more prominent; imperforate anus in ~84%.
- **Catel-Manzke syndrome** (TGDS, AR) — distinctive hand malformation with accessory ossicles and index-finger shortening; Pierre Robin sequence more common, cardiac/vertebral/renal anomalies rarer.
- **Fanconi anemia** (~23 genes, AR/AD/X-linked) — bone marrow failure and cancer predisposition absent in CNDD; structural anomaly rates markedly lower.
- **22q11.2 deletion syndrome** (AD) — immune deficiency and palatal anomalies far more prominent.
- **Teratogen-induced phenocopies:** diabetic embryopathy, thalidomide embryopathy, and valproate embryopathy each share partial overlap but differ in the frequency/pattern of neural tube, cleft, and limb-reduction defects (van de Putte et al. 2020, PMID: 32596782, is the key comparative reference for the VACTERL differential specifically).

**Screening:** No population newborn-screening program exists (metabolite panel is not part of standard newborn screening); prenatal ultrasound is the practical first-line detection modality given the structural nature of the anomalies; carrier/prenatal/preimplantation genetic testing is available once a family's causal variants are identified.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Highly genotype/severity-dependent. In the most severe cohort (biallelic NADSYN1, Szot et al. 2020), "no affected individual survived for more than three months postnatally," with outcomes spanning isolated bilateral renal agenesis to lethal multi-organ malformation. Across the full GeneReviews cohort of 27 individuals, 9 did not survive (5 pregnancy termination/loss, 4 deaths in the first year from severe structural defects), while 16 were living, including one individual reported alive at **age 30** (Erbs et al. 2023) — demonstrating that survival to adulthood is possible with milder genotypes and modern multidisciplinary management.

**Morbidity/function:** Long-term morbidity is driven by chronic kidney disease (in survivors with significant renal hypoplasia), residual cardiac lesions requiring ongoing cardiology follow-up, orthopedic complications (scoliosis, limb-length discrepancy), sensorineural hearing loss, and variable intellectual disability/developmental delay (up to 62% in the reviewed cohort). No standardized disability or QoL instrument has yet been applied to this population in the literature.

**Complications:** Progressive chronic kidney disease/hypertension (renal survivors), tethered spinal cord (in those with spinal dysraphism), feeding/aspiration issues from TEF or laryngeal web, hypothyroidism/hypoparathyroidism, and — where polysplenia is present — functional asplenia/infection risk.

**Recovery potential:** Structural anomalies themselves are not reversible; outcome depends on surgical/medical correction of individual organ defects (cardiac surgery, orthopedic correction, hearing aids, etc.) rather than on treating the underlying metabolic lesion, since **no NAD⁺-repletion treatment for affected individuals postnatally has yet been validated or recommended** (see Section 12).

**Prognostic factors:** Genotype/gene (NADSYN1-associated disease trends more severe/lethal than HAAO- or KYNU-associated disease in the literature to date, though formal genotype-phenotype correlation is explicitly stated as unestablished by GeneReviews), severity and combination of organ involvement (cardiac + bilateral renal disease carries the worst prognosis), and gestational NAD⁺ status (maternal nutritional modifier, per the mouse model).

---

## 12. Treatment

**No disease-modifying cure exists.** Management is **supportive and organ-specific**, coordinated through a multidisciplinary genetics/cardiology/nephrology/orthopedics/developmental team, per GeneReviews (NBK593504):

- **Congenital heart defects:** Standard pediatric cardiology/cardiac surgical management per lesion type (NCIT:C15329, Surgical Procedure; NCIT:C49236, Therapeutic Procedure).
- **Renal anomalies:** Nephrology monitoring of function/blood pressure; avoid nephrotoxic agents in those with solitary/hypoplastic kidneys.
- **Vertebral/orthopedic anomalies (scoliosis, clubfoot, limb anomalies):** Standard orthopedic management (NCIT:C16186, Orthopedic Surgical Procedure); neurosurgical management if tethered cord.
- **Cleft palate:** Craniofacial team management.
- **Hearing loss:** Hearing aids/otolaryngology referral (NCIT device pattern applies).
- **GI anomalies (TEF, pyloric stenosis, laryngeal web):** Gastroenterology/otolaryngology surgical management.
- **Polysplenia:** Hematology/immunology monitoring for functional asplenia.
- **Developmental delay/intellectual disability:** Early intervention (0–3), developmental preschool, IEP/504 supports, physical/occupational/speech therapy, ABA for autism-spectrum features, developmental pediatrics.
- **Seizures:** Standard anti-seizure medication (no CNDD-specific agent shown superior).
- **Endocrine (hypothyroidism, hypoparathyroidism):** Standard endocrinology management/hormone replacement (NCIT:C15986, Pharmacotherapy).
- **Ophthalmologic findings (strabismus, ptosis):** Standard ophthalmologic management.
- **Family/psychosocial:** Genetic counseling, social work, palliative/home-nursing referral where indicated.

**A notable and reportable gap:** despite NAD⁺ deficiency being the established root mechanism, and despite gestational niacin supplementation preventing malformation in mouse models (Shi et al. 2017), **the current GeneReviews chapter does not recommend niacin/nicotinamide/NAD⁺/NMN/NR supplementation as a treatment for affected individuals postnatally**, and no human interventional trial of maternal or child NAD⁺-precursor supplementation for this specific disorder has been published as of the most recent literature reviewed. This is an important, explicit `KNOWLEDGE_GAP` for a KB mechanism entry: the mechanistic and preclinical rationale for prevention (pre-conception/gestational niacin supplementation in confirmed carrier couples) is strong, but translation into a validated treatment/prevention guideline for humans remains an active, unresolved research question.

**Experimental/preclinical therapeutics:** Gestational niacin supplementation is the sole experimentally validated intervention to date, demonstrated only in *Haao*-null/*Kynu*-null mouse embryos (Shi et al. 2017) and now being extended in the 2025 zebrafish CNDD model (PMID: 39829932) to further dissect the rescue mechanism. No registered clinical trial (ClinicalTrials.gov) specific to CNDD/VCRL syndrome niacin prophylaxis was identified in the sources reviewed.

**Screening/counseling role of niacin data:** Even absent a formal trial, the preclinical prevention data is directly relevant to **genetic counseling for known carrier couples** planning a subsequent pregnancy, and several review/commentary sources (Dunwoodie group publications and secondary press coverage) explicitly frame periconceptional niacin supplementation as a candidate primary-prevention strategy pending clinical validation.

---

## 13. Prevention

**Primary prevention:** The strongest candidate primary-prevention strategy is **periconceptional/gestational niacin (vitamin B3) supplementation** in couples known to carry pathogenic HAAO/KYNU/NADSYN1 variants, grounded directly in the mouse rescue data (Shi et al. 2017) — niacin enters the Preiss-Handler NAD⁺-synthesis pathway independently of the three affected de novo-pathway enzymes, restoring embryonic NAD⁺ sufficiency. This remains **preclinically validated but not yet clinically proven or formally guideline-recommended** in humans, and should be characterized in a KB entry as an emerging/hypothesis-level prevention strategy rather than an established standard of care.

**Secondary prevention:** Prenatal ultrasound surveillance in known at-risk pregnancies (both parents confirmed carriers) for early detection of cardiac, renal, and vertebral anomalies, enabling informed counseling about pregnancy management and coordinated perinatal/neonatal care planning.

**Genetic counseling and reproductive options:** Central to prevention in this AR disorder. GeneReviews recommends: confirming parental carrier status by molecular testing (also serving to distinguish true biparental inheritance from de novo variants, parental mosaicism, or uniparental disomy); offering **carrier testing to reproductive partners** of known carriers, especially where consanguinity is likely; and discussing **prenatal diagnosis and preimplantation genetic testing (PGT)** once the family's causal variants are known. For each pregnancy where both parents are confirmed carriers, recurrence risk is the standard AR figure: 25% affected, 50% carrier, 25% unaffected/non-carrier.

**Public health/behavioral interventions:** No population-level screening or public health program exists for this ultra-rare disorder; prevention efforts are necessarily family- and genetics-clinic-based rather than population-based.

**Prophylaxis:** As above, gestational niacin supplementation is the only biologically targeted prophylactic candidate under discussion in the literature, but is not yet an established prophylactic guideline.

---

## 14. Other Species / Natural Disease

**Taxonomy of model organisms used:** *Mus musculus* (NCBITaxon:10090) and *Danio rerio* (NCBITaxon:7955) — no naturally occurring veterinary/companion-animal disease analog has been reported in the literature reviewed (this is a laboratory-modeled human genetic disorder rather than a condition recognized in OMIA/veterinary case series).

**Orthologous genes:** Mouse *Haao* (MGI:1919711), *Kynu* (MGI ortholog), *Nadsyn1* (MGI:1926164) are the direct murine orthologs used to generate the null-allele models; zebrafish orthologs (*haao*, *kynu*, *nadsyn1*) were used in the 2025 model.

**Comparative biology:** The kynurenine pathway and de novo NAD⁺ biosynthesis route are highly evolutionarily conserved from bacteria through vertebrates (noted explicitly in the KYNU/NAD-biosynthesis evolutionary literature), supporting cross-species mechanistic validity of the mouse and zebrafish models for this pathway, even though no spontaneous/natural veterinary disease counterpart is documented.

**Zoonotic potential/transmission:** Not applicable — this is a non-communicable genetic developmental disorder.

---

## 15. Model Organisms

**Mouse (Mus musculus):**
- **Genetic models:** *Haao*-null and *Kynu*-null knockout mice (Shi et al. 2017, PMID: 28792876) are the foundational models establishing causality.
- **Phenotype recapitulation:** Null mouse embryos develop malformations described as similar to those seen in affected human patients, attributed directly to embryonic NAD⁺ deficiency.
- **Key experimental result:** Gestational niacin supplementation of null-mutant dams **prevented** malformations in their offspring — the single most important interventional proof-of-concept in the field, directly informing both mechanism (Section 6) and prevention hypotheses (Section 13).
- **Limitations:** Mouse null models represent complete loss-of-function, which may not fully capture the phenotypic range seen with human hypomorphic/missense alleles (e.g., the milder NADSYN1 p.A573T genotype); litter-level variability and resorption patterns in these models have also been used (Mark 2022) to model human miscarriage risk, an extrapolation not yet directly validated in human tissue.

**Zebrafish (Danio rerio):**
- A 2025 study (bioRxiv 10.1101/2025.01.10.632366; PMID: 39829932; also published in a peer-reviewed venue per ScienceDirect indexing) established the first **zebrafish model of NAD⁺ deficiency-derived congenital disorders**, targeting the same pathway genes, explicitly to further probe the unresolved question of *why* NAD⁺ deficiency selectively disrupts cardiac, renal, vertebral, and limb development and to test the hypothesis of shared mechanism with VACTERL association.
- **Applications:** Zebrafish offer external embryonic development, rapid generation time, and amenability to high-throughput chemical/genetic screening — well suited to dissecting the still-open cell-signaling mechanism downstream of NAD⁺ depletion and to future compound (e.g., NAD⁺ precursor) screening.

**Resources:** MGI (Mouse Genome Informatics) for *Haao*/*Kynu*/*Nadsyn1* mouse alleles; ZFIN for zebrafish CNDD-model lines as they become deposited; no dedicated patient-derived iPSC or organoid model of CNDD was identified in the literature reviewed, representing an additional experimental-model gap relative to many other monogenic disorders.

---

## Summary Table: Key Evidence Citations

| Claim | PMID | Citation |
|---|---|---|
| HAAO/KYNU cause CNDD; mouse niacin rescue | 28792876 | Shi et al. 2017, *N Engl J Med* 377:544–552 |
| NADSYN1 (VCRL3) causal gene; severe lethal phenotype | 31883644 | Szot et al. 2020, *Am J Hum Genet* 106:129–136 |
| KYNU hand hyperphalangism phenotype expansion | 31923704 | Ehmke et al. 2020, *Bone* |
| Expanded genotypic/phenotypic spectrum | 33942433 | Szot et al. 2021, *Hum Mutat* |
| Maternal chromosome 2 isodisomy/KYNU deletion | 34200361 | Schüle et al. 2021, *Genes* 12:879 |
| Further NADSYN1 case description | 35491967 | Kortbawi et al. 2022, *Am J Med Genet A* |
| NADSYN1 clinical heterogeneity | 36951206 | Aubert-Mucca et al. 2023, *Clin Genet* |
| Oldest living patient (age 30); NAD level analysis | 36649848 | Erbs et al. 2023, *Eur J Med Genet* |
| Pleiotropy model linking CNDD to VACTERL/other spectra | 35484986 | Mark 2022, *Am J Med Genet A* 188:2834–2849 |
| VACTERL differential diagnosis comparison | 32596782 | van de Putte et al. 2020 |
| Single-variant NADSYN1 vertebral malformation | 34681008 | Lin et al. 2021, *Genes* |
| ACMG/AMP variant classification standard | 25741868 | Richards et al. 2015 |
| Zebrafish CNDD model | 39829932 | 2025, bioRxiv/peer-reviewed |
| GeneReviews comprehensive chapter | NBK593504 | Adam MP et al. (eds.), "Congenital NAD Deficiency Disorder," updated July 2023 |

---

### Sources

- [congenital vertebral-cardiac-renal anomalies syndrome - NORD](https://rarediseases.org/mondo-disease/congenital-vertebral-cardiac-renal-anomalies-syndrome/)
- [Vertebral, cardiac, renal, and limb defects syndrome 1 - MedGen](https://www.ncbi.nlm.nih.gov/medgen/1621146)
- [Orphanet: Congenital vertebral-cardiac-renal anomalies syndrome (ORPHA:521438)](https://www.orpha.net/en/disease/detail/521438)
- [Vertebral, cardiac, renal, and limb defects syndrome 2 - MedGen](https://www.ncbi.nlm.nih.gov/medgen/1624065)
- [Vertebral, cardiac, renal, and limb defects syndrome 3 - GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5394250/)
- [OMIM #617660 - VCRL1](https://www.omim.org/entry/617660)
- [OMIM #617661 - VCRL2](https://omim.org/entry/617661)
- [OMIM #618845 - VCRL3](https://omim.org/entry/618845)
- [Congenital vertebral-cardiac-renal anomalies syndrome - GARD/NCATS](https://rarediseases.info.nih.gov/diseases/17961/congenital-vertebral-cardiac-renal-anomalies-syndrome)
- [congenital vertebral-cardiac-renal anomalies syndrome - Open Targets (MONDO_0020831)](https://platform.opentargets.org/disease/MONDO_0020831)
- [Congenital NAD Deficiency Disorder - GeneReviews (NBK593504)](https://www.ncbi.nlm.nih.gov/books/NBK593504/)
- [NAD Deficiency, Congenital Malformations, and Niacin Supplementation - NEJM 2017](https://www.nejm.org/doi/full/10.1056/NEJMoa1616361)
- [A Homozygous Deletion of Exon 5 of KYNU Resulting from Maternal Chromosome 2 Isodisomy (UPD2) Causes Catel-Manzke-Syndrome/VCRL Syndrome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8227568/)
- [Bi-allelic Mutations in NADSYN1 Cause Multiple Organ Defects - Victor Chang Cardiac Research Institute](https://eprints.victorchang.edu.au/917/)
- [Bi-allelic Mutations in NADSYN1 Cause Multiple Organ Defects - AJHG/ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002929719304707)
- [A metabolic signature for NADSYN1-dependent congenital NAD deficiency disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10866660/)
- [NAD+ deficiency in human congenital malformations and miscarriage: A new model of pleiotropy - AJMG 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62764)
- [Nicotinamide Adenine Dinucleotide Deficiency and Its Impact on Mammalian Development - Dunwoodie et al. 2023](https://dx.doi.org/10.1089/ars.2023.0349)
- [A zebrafish model of NAD+ deficiency-derived congenital disorders - bioRxiv/PubMed 39829932](https://www.biorxiv.org/content/10.1101/2025.01.10.632366v1.full)
- [Effect of maternal dietary niacin intake on congenital anomalies: systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/34748060/)
- [HAAO Gene - GeneCards / OMIM 604521](https://omim.org/entry/604521)
- [NADSYN1 gene - GeneCards / OMIM 608285](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NADSYN1)
- [KYNU - Alliance of Genome Resources (HGNC:6469)](https://www.alliancegenome.org/gene/HGNC:6469)
- [Could vitamin B-3 be the answer to miscarriages and birth defects? - Medical News Today coverage of Dunwoodie group research](https://www.medicalnewstoday.com/articles/318932)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 6 |
| Terms whose name was checked | 29 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002510` (1 mention) - the report calls it "One reported Lennox-Gastaut-type case"; HP calls it **Spastic tetraplegia**
- `GO:0034354` (1 mention) - the report calls it "NAD biosynthesis via nicotinamide riboside salvage pathway"; GO calls it **'de novo' NAD+ biosynthetic process from L-tryptophan**
- `UBERON:0002298` (1 mention) - the report calls it "vertebral column"; UBERON calls it **brainstem**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001180` (obsolete Hand oligodactyly) (1 mention) - replaced by `HP:0009380`
- `GO:0043420` (obsolete anthranilate metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0043420` (1 mention) - the report calls it "anthranilate metabolic process"; GO calls it **obsolete anthranilate metabolic process**, and lists "anthranilate catabolic process" among its other names
- `GO:0033721` (1 mention) - the report calls it "3-hydroxyanthranilate 3,4-dioxygenase activity"; GO calls it **aldehyde dehydrogenase (NADP+) activity**
- `GO:0006974` (1 mention) - the report calls it "cellular response to DNA damage stimulus, PARP-relevant"; GO calls it **DNA damage response**, and lists "cellular response to DNA damage stimulus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
