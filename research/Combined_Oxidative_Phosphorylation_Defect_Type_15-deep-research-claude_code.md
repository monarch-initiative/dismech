---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-17T19:07:08.842080'
end_time: '2026-09-17T19:12:36.126295'
duration_seconds: 327.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 15
  mondo_id: MONDO:0013987
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
  num_turns: 28
  total_cost_usd: 1.5632342000000004
  session_id: 02de2005-7bcd-5191-9c2e-13b68aa9faf8
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 8
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 15
- **MONDO ID:** MONDO:0013987 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 15** covering all of the
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

I'll research Combined Oxidative Phosphorylation Defect Type 15 (COXPD15) now and compile the full report.

Confirmed: COXPD15 is caused by **MTFMT** mutations (not MRPL44, which causes COXPD16 — an important disambiguation). Let me gather detailed data on MTFMT, phenotypes, variants, and mechanism.

I now have sufficient primary-literature-backed detail to compile the full report.

I have comprehensive, well-sourced data now. Compiling the full report.

---

# Combined Oxidative Phosphorylation Deficiency 15 (COXPD15) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Combined oxidative phosphorylation deficiency 15 (COXPD15) is a rare, autosomal recessive mitochondrial disease of impaired mitochondrial protein synthesis, caused by biallelic pathogenic variants in **MTFMT** (mitochondrial methionyl-tRNA formyltransferase). It typically presents in infancy or early childhood with hypotonia, ataxia, developmental delay, and neuroimaging/neuropathology consistent with **Leigh syndrome**, reflecting a combined deficiency of respiratory chain complexes (most consistently complex I, often together with complex IV) ([OMIM #614947](https://www.omim.org/entry/614947); [Orphanet ORPHA:319524](https://www.orpha.net/en/disease/detail/319524); [GARD](https://rarediseases.info.nih.gov/diseases/17456/combined-oxidative-phosphorylation-defect-type-15)).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | #614947 |
| OMIM (gene, MTFMT) | *611766 |
| Orphanet | ORPHA:319524 |
| MONDO | MONDO:0013987 |
| Gene (HGNC) | MTFMT, HGNC:29666 |
| NCBI Gene | 123263 |
| UniProt | Q96DP5 |
| Cytoband | 15q22.31 |
| Allelic disorder | Mitochondrial Complex I Deficiency, Nuclear Type 27 (MC1DN27), OMIM #618248 — same gene, overlapping/milder-to-variable phenotype |

**Synonyms:** COXPD15; Leigh syndrome due to MTFMT deficiency; MTFMT-related mitochondrial disease; Combined oxidative phosphorylation defect type 15.

**Evidence base:** This entry is derived almost entirely from **aggregated case-series and cohort literature** (the largest being a 38-patient natural-history study, PMID:30911575) rather than from a single large EHR-scale population resource — appropriate for an ultra-rare Mendelian disorder without disease-level registries.

---

## 2. Etiology

**Disease causal factor:** COXPD15 is a monogenic, purely genetic disorder — **biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in MTFMT** are necessary and sufficient. No environmental, infectious, or purely mechanistic (non-genetic) causal pathway has been described.

**Genetic risk factors:**
- Causal gene: **MTFMT** (mitochondrial methionyl-tRNA formyltransferase), nuclear-encoded, imported into mitochondria.
- A single missense/splicing allele, **c.626C>T** (historically annotated p.Ser209Leu, but functionally causing **exon 4 skipping and a frameshift**, p.Arg181SerfsTer6), is a recurrent **European founder variant** and the single most common pathogenic MTFMT allele — found in **~50% of the 38-patient Hayhurst et al. cohort**, homozygous in 7 patients (PMID:30911575). Its highest population allele frequency is **0.001059 in gnomAD v3.1.2 non-Finnish European**, consistent with carrier frequency expectations for an ultra-rare autosomal recessive disease.
- The remaining allelic spectrum spans **frameshift (n=6), missense (n=5) and nonsense (n=5)** variants across the 16 pathogenic alleles catalogued in that cohort; most cause loss of MTFMT protein or severely reduced steady-state levels (PMID:24461907, PMID:30911575).
- No modifier genes have been formally established, though phenotypic variability (see below) suggests genetic background effects are plausible but uncharacterized.

**Environmental/exposure risk factors:** None established. There is no reported association with toxins, occupational exposure, maternal factors, or lifestyle.

**Protective factors:** None specifically described for MTFMT deficiency. General principles for mitochondrial disease (avoidance of respiratory-chain-toxic drugs such as valproate, aminoglycosides, and metabolic stressors like prolonged fasting or intercurrent illness) are extrapolated from mitochondrial disease management guidelines rather than MTFMT-specific evidence.

**Gene-environment interaction:** Not documented. As a fully penetrant recessive enzymopathy of mitochondrial translation, the disease model is gene-dosage/loss-of-function driven rather than gene-environment interactive, though intercurrent metabolic stress (febrile illness, catabolic states) is anecdotally reported to precipitate decompensation in mitochondrial disease broadly.

---

## 3. Phenotypes

The phenotype spectrum has broadened considerably from the original Leigh-syndrome-centric description (2011) to a wider multisystem picture (2015–2023), and severity ranges from **fatal neonatal presentations to adult-onset neurodegeneration** (search results synthesizing OMIM #618248/#614947).

### Core/classic phenotype (original and majority of cases)
| Phenotype | Type | HPO suggestion | Notes |
|---|---|---|---|
| Muscular hypotonia | Sign | HP:0001252 (Hypotonia) | Presenting feature in most patients |
| Gait ataxia | Sign | HP:0002066 (Gait ataxia) | Common; motor abnormalities present in 94% of the 38-patient cohort (PMID:30911575) |
| Pyramidal tract signs (mild, bilateral) | Sign | HP:0007256 (Progressive pyramidal tract signs) / HP:0002493 | |
| Global developmental delay | Sign | HP:0001263 (Global developmental delay) | Present in 59% (PMID:30911575); affects speech and coordination predominantly |
| Intellectual disability | Sign | HP:0001249 (Intellectual disability) | Subsequent to developmental delay |
| Lactic acidosis | Lab abnormality | HP:0003128 (Lactic acidosis) | Classic biochemical marker of OXPHOS disease |
| Leigh-syndrome neuropathology / MRI | Sign/imaging | HP:0002490 (Leigh disease) / HP:0007033 (Bilateral basal ganglia lesions) | T2/FLAIR hyperintensities in basal ganglia and/or midbrain in 7 of the original patients; some with subcortical white-matter lesions |
| Short stature | Sign | HP:0004322 | |
| Obesity | Sign | HP:0001513 | Somewhat unusual for a mitochondrial disease (more often failure to thrive) |
| Microcephaly | Sign | HP:0000252 | |
| Strabismus | Sign | HP:0000486 | |
| Nystagmus | Sign | HP:0000639 | |
| Reduced visual acuity / optic atrophy | Sign | HP:0000572 / HP:0000648 | Ocular involvement in 59% of cohort (PMID:30911575) |

### Extended/newer phenotypes (expanding the spectrum, 2015–2023)
- **Cardiac dysfunction / cardiomyopathy** — present in 53% of the 38-patient cohort (PMID:30911575).
- **Autonomic instability and arrhythmia** — a 2023 case report (PMID:36873085) documented severe hypertension/tachycardia crises and recurrent supraventricular tachycardia in a c.626C>T-homozygous boy, expanding the phenotype to brainstem-mediated autonomic dysregulation.
- **Hyperphagia and neurogenic bladder/bowel dysfunction** — also newly reported in the same case, attributed to dorsal brainstem T2/FLAIR signal change (PMID:36873085).
- **Hemiplegic migraine** and **pigmentary retinopathy** — reported in the childhood-onset multisystem disease literature more broadly associated with mitochondrial translation defects (context noted in search results discussing overlapping MRPL44/mitoribosome disease features — flagged here as adjacent literature, not MTFMT-specific, so treat cautiously and verify per-source before citing as an MTFMT phenotype).
- **Nonprogressive mobile dystonia** — a distinct clinical presentation reported in MTFMT-related disease (PMID:36704074).
- **Parkinsonism in adulthood** — an adult patient with homozygous c.626C>T presented with Leigh syndrome followed by later-onset parkinsonism (PMC6278240), underscoring the very wide age-of-onset/phenotype range.
- **Renal insufficiency and hepatopathy** — reported as additional features in the broader mitochondrial-translation-defect literature.
- **Macrocephaly with progressive leukodystrophy** — one of the phenotypes listed under the allelic MC1DN27 entry (OMIM #618248), illustrating that MTFMT variants can produce leukodystrophy rather than classic Leigh-pattern imaging in some patients.
- **Selective visual pathway vulnerability with a mild neurological phenotype** — described for a novel MTFMT mutation (Neurogenetics, 2016), showing that some genotypes produce disproportionate optic-pathway involvement with otherwise mild disease.

**Phenotype characteristics:**
- **Onset:** Infancy to early childhood most common (median age of presentation 14 months in the 38-patient cohort; range birth to 17 years) (PMID:30911575); adult-onset presentations also reported.
- **Severity/progression:** Variable — from lethal neonatal multisystem disease to a **slowly progressive** or even **nonprogressive** course in some patients (PMID:25797485 describes a "slowly progressive multisystem disease" pattern in the allelic mitoribosome-disease literature; note this specific PMID concerns MRPL44/COXPD16, included here as a contrasting allelic-mimic disease, not MTFMT). For MTFMT-COXPD15 itself, disease course is more indolent than most causes of Leigh syndrome.
- **Frequency/penetrance:** All reported biallelic pathogenic-variant carriers are symptomatic (fully penetrant recessive disease), though phenotypic severity varies substantially by variant and possibly by genetic background.
- **Quality of life impact:** Motor disability (ataxia, spasticity), intellectual disability, and visual impairment (registered sight-impaired in at least one reported case) impose substantial functional burden; no formal EQ-5D/SF-36 data exist for this ultra-rare disease.

---

## 4. Genetic/Molecular Information

**Causal gene:** MTFMT (HGNC:29666; OMIM *611766; NCBI Gene 123263; UniProt Q96DP5), 15q22.31, encoding a 389-amino-acid, ~43.8 kDa mitochondrial matrix enzyme.

**Discovery:** Tucker et al. (2011, *Cell Metabolism* 14:428–434; **PMID:21907147**) used MitoExome targeted sequencing to identify **compound heterozygous MTFMT mutations** in two unrelated children with Leigh syndrome and combined OXPHOS deficiency — the founding report for this disease gene. Their abstract establishes: "Fibroblasts from these patients have impaired Met-tRNAMet formylation, peptide formylation, and mitochondrial translation... severe defects in mitochondrial translation that can be rescued by exogenous expression of MTFMT," directly demonstrating causality via complementation.

**Expanded genetic cohorts:**
- Haack et al. (2014, *Molecular Genetics and Metabolism* 111:342–352; **PMID:24461907**) — "Phenotypic spectrum of eleven patients and five novel MTFMT mutations identified by exome sequencing and candidate gene screening." Identified nine additional patients from eight families with Leigh encephalopathy or white-matter disease, microcephaly, intellectual disability, ataxia, and hypotonia; "all novel mutations predict a loss-of-function or result in a severe decrease in MTFMT protein in patients' fibroblasts accompanied by reduced steady-state levels of complex I and IV subunits."
- Hayhurst et al. (2019, *Annals of Clinical and Translational Neurology*; **PMID:30911575**) — the largest natural-history study (38 patients: 8 new, 9 previously published with added data, 21 from literature review). Reports "16 pathogenic variants: frameshift (n=6), missense (n=5) and nonsense (n=5)"; 30 patients compound heterozygous, 8 homozygous.

**Variant classification / pathogenicity:** Per ACMG/AMP framework as applied in ClinVar, the recurrent **c.626C>T** allele (NM_139242.4) is classified pathogenic/likely pathogenic for Leigh syndrome ([ClinVar RCV000190888](https://www.ncbi.nlm.nih.gov/clinvar/RCV000190888/)). Mechanistically it disrupts the 3' splice acceptor region near exon 4, causing **exon 4 skipping** and a downstream frameshift (p.Arg181SerfsTer6) rather than a simple missense substitution as its nucleotide-based p.Ser209Leu name would suggest — an important nomenclature caveat for curation.

**Variant type/class:** Missense, nonsense, frameshift, and splice-region variants are all represented; no gross structural rearrangements (CNVs) have been reported as a mechanism.

**Allele frequency:** c.626C>T has a maximum population allele frequency of **0.001059** (gnomAD v3.1.2, non-Finnish European), consistent with a founder allele in an ultra-rare recessive disease; other pathogenic alleles are private/family-specific and expected to be singleton or near-absent in population databases (gnomAD, 1000 Genomes) — consistent with strong purifying selection against biallelic loss of an essential translation-initiation enzyme.

**Somatic vs. germline:** Exclusively germline; no somatic mosaicism or oncologic association reported.

**Functional consequence:** Predominantly **loss-of-function / hypomorphic** — reduced or absent formyltransferase activity, reduced steady-state MTFMT protein, and downstream defective mitochondrial translation. Biochemical characterization of specific pathogenic missense alleles has been performed directly on recombinant enzyme (PMID:25288793, "Biochemical characterization of pathogenic mutations in human mitochondrial methionyl-tRNA formyltransferase"), demonstrating impaired catalytic function rather than a dominant-negative or gain-of-function mechanism.

**Modifier genes:** None formally established.

**Epigenetics / chromosomal abnormalities:** Not implicated; this is a classic biallelic point-mutation/small-indel Mendelian disease with no reported epigenetic or large chromosomal contribution.

**Allelic disorder distinction:** The same gene also causes **Mitochondrial Complex I Deficiency, Nuclear Type 27 (MC1DN27, OMIM #618248)**, characterized by isolated, very low complex I activity with normal complex II/III/IV, and overlapping features (developmental delay, hypotonia/spasticity, ophthalmologic abnormalities). This reflects a phenotypic continuum rather than two mechanistically distinct diseases — the "COXPD15" vs. "MC1DN27" split is a historical/biochemical distinction (combined vs. isolated complex deficiency) rather than a different causal gene or mechanism.

---

## 5. Environmental Information

No environmental toxin, occupational exposure, dietary, or lifestyle factor has been identified as causal or contributory. There is no infectious trigger reported for disease onset. (One tangential, MTFMT-adjacent finding worth flagging for future literature-scanning rather than direct curation: a 2020 *Scientific Reports* paper reports "MTFMT deficiency correlates with reduced mitochondrial integrity and enhanced host susceptibility to intracellular infection" — this describes a cellular/functional consequence of MTFMT loss on infection susceptibility in an experimental model, not an environmental cause of the human disease, and should be evaluated carefully before use as a phenotype or environmental-factor claim.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from lesion to clinical manifestation)

1. **Biallelic pathogenic MTFMT variants** (e.g., the founder c.626C>T splice/frameshift allele, or other frameshift/nonsense/missense alleles) → **loss or severe reduction of functional MTFMT enzyme** in the mitochondrial matrix (demonstrated directly: PMID:24461907 shows "severe decrease in MTFMT protein in patients' fibroblasts"; PMID:25288793 shows reduced catalytic activity of specific mutant recombinant enzyme).
2. Loss of MTFMT enzymatic activity → **failure to formylate mitochondrial Met-tRNA^Met^** to generate fMet-tRNA^Met^ ("impaired Met-tRNAMet formylation," PMID:21907147). This step is a **direct, demonstrated** biochemical consequence (assayed in patient fibroblasts), not inferred.
3. Because mammalian mitochondria possess only a **single Met-tRNA species** that must serve both translation initiation (as fMet-tRNA^Met^) and internal elongation (as unformylated Met-tRNA^Met^), a deficit in formylation **leads to** insufficient substrate for the mitochondrial translation initiation factor IF2mt, which has high affinity specifically for the formylated species and recruits it to the ribosomal P site.
4. Reduced fMet-tRNA^Met^ availability → **impaired initiation of mitochondrial mRNA translation genome-wide** ("severe defects in mitochondrial translation," rescued by exogenous MTFMT re-expression, establishing direct causality; PMID:21907147).
5. Defective translation of the 13 mtDNA-encoded OXPHOS subunits → **decreased synthesis/stability of respiratory chain complex subunits**, particularly those of **complex I** (universally reduced: "Complex I was decreased in all patients" in the largest cohort, PMID:30911575) and, in many patients, also **complex IV** ("reduced steady-state levels of complex I and IV subunits," PMID:24461907; "loss of complex I and IV subunits in all cases" on fibroblast analysis, PMID:30911575).
6. Combined or isolated complex I(/IV) deficiency → **impaired oxidative phosphorylation and ATP synthesis**, with compensatory upregulation of anaerobic glycolysis → **systemic lactic acidosis** (a downstream, largely inferred-but-well-documented biochemical consequence consistent with virtually all mitochondrial OXPHOS diseases).
7. Chronic bioenergetic failure, with particular vulnerability in **high energy-demand, post-mitotic tissues** (basal ganglia, brainstem, cerebellum, myocardium, optic pathway) → **region-specific neurodegeneration and necrotizing lesions**, producing the classic **Leigh-syndrome neuropathological/neuroimaging pattern** (bilateral basal ganglia and midbrain T2/FLAIR hyperintensity) as well as cardiomyopathy, optic atrophy, and (in cases with dorsal brainstem involvement) autonomic dysregulation, hyperphagia, and neurogenic bladder/bowel dysfunction (PMID:36873085) — this brainstem-localization-to-symptom link is **directly imaged and inferred by anatomical correlation**, not experimentally proven at the causal-pathway level.
8. Downstream/parallel branch: reduced ATP and chronic cellular stress in postmitotic CNS and retinal/optic-nerve tissue → progressive **developmental delay, ataxia, pyramidal signs, and optic atrophy/visual impairment**, while in a subset of patients a **milder, non-progressive, or even improving course** is observed relative to Leigh syndrome caused by other nuclear genes (PMID:30911575) — the mechanistic basis for this comparatively favorable trajectory is not established and is an open question (possibly residual formylation via translational read-through, partial enzyme activity from hypomorphic alleles, or tissue-specific compensation).

### Molecular pathways
Mitochondrial translation initiation pathway (mtDNA-encoded polycistronic mRNA translation machinery: mtIF2, mtIF3, the 55S mitoribosome, mt-tRNA maturation) — not a classical signaling cascade (no KEGG/Reactome equivalent of Wnt/MAPK/PI3K involvement reported). GO Biological Process: **GO:0070900** (mitochondrial tRNA methylation is not correct — recommend **GO:0071026**, nuclear-transcribed mRNA catabolic process, is not appropriate either; the most precise GO BP term is **GO:0070125** "mitochondrial translational elongation" is elongation-specific — the initiation-specific term is **GO:0070126**, "mitochondrial translational termination," also not correct). The directly applicable GO Molecular Function term is **GO:0004479** (methionyl-tRNA formyltransferase activity), and the applicable GO Biological Process term is **GO:0070124** (mitochondrial translational initiation). (Ontology term suggestions should be verified against current GO/OAK lookups before binding, per this repository's term-validation discipline.)

### Cellular processes
Impaired mitochondrial translation broadly disrupts **oxidative phosphorylation / ATP generation** (GO:0006119, oxidative phosphorylation), with secondary effects plausibly including increased **reactive oxygen species generation** and **compensatory mitophagy/mitochondrial biogenesis responses**, though these have not been specifically characterized for MTFMT deficiency in the literature reviewed here (flag as inferred/extrapolated from general mitochondrial disease biology, not MTFMT-specific data).

### Protein dysfunction
MTFMT itself: loss-of-function via reduced catalytic activity (biochemically confirmed for specific pathogenic missense alleles, PMID:25288793) or reduced protein stability/steady-state level (frameshift/nonsense alleles, PMID:24461907). This is a **loss-of-function** mechanism throughout — no gain-of-function or dominant-negative behavior has been reported.

### Metabolic changes
**Lactic acidosis** (elevated blood/CSF lactate) is the principal reported metabolic biomarker, reflecting a shift toward anaerobic glycolysis secondary to OXPHOS failure — standard for combined respiratory chain disorders.

### Immune system involvement
Not implicated as a primary disease mechanism. (The tangential *Scientific Reports* finding on MTFMT and susceptibility to intracellular infection describes an experimental/cellular observation about mitochondrial integrity and host defense, not an established immunological arm of the human disease's pathophysiology.)

### Tissue damage mechanisms
Chronic bioenergetic insufficiency in high-demand tissue (basal ganglia, brainstem, myocardium, optic nerve) leading to **necrotizing, spongiform lesions** characteristic of Leigh syndrome pathology on autopsy/imaging; oxidative stress is presumed contributory by analogy to other OXPHOS diseases but not specifically documented for MTFMT in the sources reviewed.

### Biochemical abnormalities
- **Enzyme deficiency:** methionyl-tRNA formyltransferase activity loss (direct assay data, PMID:25288793).
- **Respiratory chain enzymology:** complex I deficiency (universal in the largest cohort), frequently combined with complex IV deficiency; multiple respiratory chain deficiencies in 59% and isolated complex I deficiency in 31% of biopsied patients (PMID:30911575).

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic, single-cell, or spatial-transcriptomic datasets specific to MTFMT/COXPD15 were identified in this search; characterization to date has relied on targeted biochemical assays (formylation assay, mitochondrial translation labeling, BN-PAGE/Western blot for OXPHOS subunit steady-state levels) in patient fibroblasts, which is standard for this disease class but leaves an omics gap for future curation.

### Suggested ontology terms for this section
- **GO:0004479** — methionyl-tRNA formyltransferase activity (molecular function)
- **GO:0070124** — mitochondrial translational initiation (biological process)
- **GO:0006119** — oxidative phosphorylation (biological process)
- **GO:0032543** — mitochondrial translation (broader parent term)
- **CL:0000540** — neuron (basal ganglia/brainstem neurons affected)
- **CL:0000746** — cardiac muscle cell (cardiomyopathy)
- **CL:0000573** — retinal cone cell / **CL:0000287** — eye photoreceptor cell (optic pathway involvement — verify against CL for the precise cell population, e.g., retinal ganglion cell CL:0000740)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (basal ganglia, midbrain/brainstem, cerebellum), consistent with classic Leigh syndrome; skeletal muscle; heart (cardiomyopathy in >50% of a large cohort); eyes/optic pathway (optic atrophy, nystagmus, strabismus, reduced acuity).
- **Secondary:** Kidney (renal insufficiency reported in extended phenotype literature), liver (hepatopathy reported), autonomic nervous system/bladder-bowel (neurogenic dysfunction in a documented case).
- **Body systems:** Nervous, cardiovascular, musculoskeletal (short stature), ophthalmologic, and — in some patients — gastrointestinal/genitourinary (hyperphagia, neurogenic bladder/bowel).

**Tissue/cell level:** Neurons of the basal ganglia and dorsal brainstem (necrotizing lesions); cardiomyocytes; skeletal myocytes (biopsy-demonstrated combined complex I/IV deficiency); retinal/optic nerve tissue.

**Subcellular level:** **Mitochondrial matrix** (site of MTFMT enzymatic activity and mitoribosome translation), specifically **GO:0005759** (mitochondrial matrix); downstream effect on the **mitochondrial inner membrane** respiratory chain complexes (GO:0005743).

**Localization/lateralization:** Basal ganglia and midbrain lesions are typically **bilateral and symmetric**, the hallmark neuroimaging pattern of Leigh syndrome; some patients show additional bilateral subcortical white-matter involvement.

Suggested UBERON terms: **UBERON:0002420** (basal ganglion), **UBERON:0001894** (midbrain), **UBERON:0000955** (brain), **UBERON:0000948** (heart), **UBERON:0000970** (eye).

---

## 8. Temporal Development

**Onset:** Median age of presentation **14 months** (range: birth to 17 years) in the largest cohort (PMID:30911575); classic infantile/early-childhood onset is most typical, but neonatal-lethal and adult-onset (including adult parkinsonism, PMC6278240) presentations occur, giving this disease one of the **widest onset ranges** among Leigh-syndrome-causing genes.

**Onset pattern:** Typically insidious/subacute developmental regression or plateauing, sometimes punctuated by acute metabolic decompensation during intercurrent illness (standard for Leigh syndrome, though not separately quantified for MTFMT here).

**Progression:**
- Disease course is **notably milder and slower-progressing** than Leigh syndrome caused by other nuclear genes: "patients with pathogenic variants in MTFMT have a milder clinical phenotype and disease progression compared to Leigh syndrome caused by other nuclear defects" (PMID:30911575).
- Some cases show a **nonprogressive** motor phenotype (e.g., nonprogressive mobile dystonia, PMID:36704074).
- Progression rate is otherwise **variable**, spanning rapidly fatal neonatal disease to stable/slowly evolving pediatric and adult presentations.

**Patterns:**
- No formal remission pattern is described; the disease is generally considered a static-to-slowly-progressive encephalopathy rather than relapsing-remitting.
- Acute crises (e.g., the autonomic/arrhythmia episode in PMID:36873085) can occur superimposed on a chronic baseline.
- No specific "critical window" for intervention has been defined, though early recognition/genetic diagnosis is emphasized given the comparatively favorable prognosis relative to other Leigh syndrome genes.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence: <1 per 1,000,000** (Orphanet/GARD classification of an ultra-rare disease); no incidence figures are published, consistent with an extremely rare Mendelian condition largely reported through case series rather than population surveillance.
- MTFMT variants are nonetheless cited as "a frequent cause of mitochondriopathies" and c.626C>T as "one of the most frequent disease alleles underlying OXPHOS disorders" **relative to other nuclear Leigh syndrome genes**, i.e., MTFMT is a disproportionately common single-gene cause within diagnosed nuclear-Leigh-syndrome cohorts, even though the disease overall remains ultra-rare in the general population.

**Inheritance pattern:** **Autosomal recessive.** Both alleles must be pathogenic (homozygous or compound heterozygous); heterozygous carriers are asymptomatic. Recurrence risk for carrier parents is the standard **25%** per pregnancy.

**Penetrance:** Appears **complete** for biallelic loss-of-function/hypomorphic genotypes based on all reported cases being clinically symptomatic, though expressivity (severity, organ involvement, age of onset) is highly variable.

**Expressivity:** **Highly variable** — from neonatal lethality to adult-onset parkinsonism in individuals homozygous for the same c.626C>T allele, indicating that genotype alone does not fully predict phenotype; genetic background and/or stochastic/environmental modifiers are presumed but uncharacterized.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for MTFMT, but is a theoretical consideration in any autosomal recessive disease's genetic counseling.

**Founder effect:** **Yes** — c.626C>T is considered a **European founder mutation**, present homozygously in multiple unrelated families and carrying the highest gnomAD allele frequency among pathogenic MTFMT alleles (0.001059 in non-Finnish Europeans).

**Consanguinity:** Not specifically quantified in the sources reviewed, but as with most ultra-rare autosomal recessive disorders, consanguineous unions would be expected to elevate homozygosity risk for rarer private alleles (general principle, not MTFMT-specific data found).

**Carrier frequency:** Directly inferable from the c.626C>T gnomAD frequency (~1 in 944 in non-Finnish Europeans for that allele alone); overall MTFMT pathogenic-allele carrier frequency (summing all alleles) is not separately published.

**Population demographics:**
- Reported cases are predominantly of **European ancestry** (consistent with the founder allele), though the disease is not confined to any single ethnic group; case reports also include patients from other regions (e.g., a Tunisian family with a novel MRPL44 — not MTFMT — variant, illustrating the broader mitoribosome-disease literature landscape, PMID via link.springer.com/10.1007/s11033-025-10556-6, but note this concerns the allelic COXPD16 gene MRPL44, not MTFMT/COXPD15).
- **Sex ratio:** No skew reported; autosomal recessive inheritance predicts equal male:female risk, consistent with case reports.
- **Age distribution:** Bimodal-to-continuous, skewed toward infantile/childhood onset but with a long tail into adulthood (see Temporal Development above).

---

## 10. Diagnostics

**Laboratory tests:**
- **Blood/CSF lactate** — elevated (lactic acidosis), a standard first-line biochemical clue for mitochondrial disease (LOINC analytes for lactate).
- **Muscle biopsy respiratory chain enzymology** — reduced complex I activity (universal in the largest reported cohort) with or without concurrent complex IV reduction; complex II/III activity typically preserved, distinguishing this from complex II/III-specific disorders.
- **Fibroblast studies** (research/diagnostic-adjacent): mitochondrial translation labeling assay showing globally reduced synthesis of mtDNA-encoded polypeptides; BN-PAGE/immunoblot showing reduced steady-state complex I and IV subunit levels; Met-tRNA^Met^ formylation assay (largely research-use).

**Biomarkers:** Blood/CSF lactate (nonspecific); no MTFMT-specific circulating biomarker has been validated.

**Imaging:** **Brain MRI** is central to diagnosis — bilateral, symmetric T2/FLAIR hyperintensity in the basal ganglia and/or midbrain (classic Leigh syndrome pattern), sometimes with additional subcortical white-matter signal change or dorsal brainstem involvement (correlating with autonomic phenotype in one report, PMID:36873085).

**Functional tests:** Cardiac echocardiography for cardiomyopathy screening (given 53% prevalence of cardiac dysfunction in the largest cohort); ophthalmologic exam (visual acuity, fundoscopy for optic atrophy/pigmentary changes) and possibly visual evoked potentials given documented optic-pathway vulnerability.

**Electrophysiology:** ECG/Holter monitoring is clinically relevant given documented arrhythmia (SVT) risk (PMID:36873085); no MTFMT-specific EEG or EMG signature reported.

**Biopsy/pathology:** Muscle biopsy typically shows biochemical (enzymatic) rather than the ragged-red-fiber histologic pattern more classic for mtDNA-mutation disease, consistent with a nuclear-encoded translation-factor defect.

**Genetic testing:**
- **Recommended approach:** Given the phenotypic overlap with dozens of other nuclear and mtDNA Leigh-syndrome genes, **exome sequencing or a mitochondrial/Leigh-syndrome gene panel** including MTFMT is the standard diagnostic route today, as was used in essentially all cited discovery/cohort studies (Tucker 2011: MitoExome; Haack 2014: exome sequencing/candidate gene screening; Hayhurst 2019: mixed panel/exome).
- **Single-gene testing** for MTFMT is appropriate when the recurrent c.626C>T founder allele is suspected (e.g., European ancestry, classic Leigh MRI) or for targeted familial/carrier testing once a proband's variants are known.
- **Whole genome sequencing** would capture the known variant classes (missense/nonsense/frameshift/splice) equally well as WES but is not specifically reported as necessary for this gene (no deep intronic variants reported to date).
- **Chromosomal microarray/karyotype/FISH:** Not relevant — no CNV or chromosomal mechanism reported.
- **Mitochondrial DNA testing:** Important as part of the differential (to exclude primary mtDNA-encoded Leigh syndrome genes such as MT-ATP6, MT-ND genes) rather than as a positive test for MTFMT disease itself, since MTFMT is nuclear-encoded.

**Differential diagnosis:** The broader genetic causes of **Leigh syndrome / Leigh syndrome spectrum** — mtDNA genes (MT-ATP6, MT-ND1-6, MT-tRNA genes), nuclear complex I assembly/subunit genes (NDUFS/NDUFA family — cf. NDUFA13, NDUFS4), SURF1 (complex IV assembly), PDHA1 (pyruvate dehydrogenase deficiency), and other mitochondrial translation genes (IARS2, MRPL44/COXPD16, MTO1). Clinically, **MTFMT-related Leigh syndrome should be favored when the course is unexpectedly indolent/nonprogressive or when adult survival occurs**, given its comparatively favorable natural history.

**Screening:** No population or newborn screening program specifically targets MTFMT; diagnosis is case-driven following clinical/biochemical suspicion of mitochondrial disease. Carrier screening and prenatal/preimplantation genetic testing are appropriate once a familial variant is identified, per standard autosomal recessive genetic counseling practice.

---

## 11. Outcome/Prognosis

**Survival:** This is the best-characterized outcome data point for the disease. In the 38-patient natural-history cohort (PMID:30911575):
- **74% of patients were alive** at last clinical review, with a **median follow-up of 6.8 years**.
- **~29% survived into adulthood.**
- This contrasts sharply with the **median survival of 2.4 years reported for Leigh syndrome overall** (from a separate multicenter Leigh syndrome natural-history study, PMC4021638), establishing MTFMT-associated Leigh syndrome as having a **comparatively favorable prognosis** among genetic causes of Leigh syndrome — the paper's own title states this explicitly: "Leigh syndrome caused by mutations in MTFMT is associated with a better prognosis."

**Morbidity/function:** Persistent motor disability (ataxia, spasticity), intellectual disability, and visual impairment (including registered sight impairment in at least one case) are common long-term sequelae even among survivors. Cardiac dysfunction (53% of the cohort) is a significant driver of morbidity and a monitoring priority.

**Complications:** Documented complications include cardiomyopathy, supraventricular tachyarrhythmia requiring pharmacologic treatment, hypertensive/autonomic crises requiring inotropic support, and bilateral optic atrophy leading to significant visual impairment.

**Recovery potential:** No disease-modifying therapy exists (see Treatment); recovery is generally limited to stabilization rather than reversal of established neurological deficits, though the overall **nonprogressive-to-slowly-progressive** course in many patients allows for meaningful long-term functional survival relative to other Leigh syndrome etiologies.

**Prognostic factors:** The specific causal gene (MTFMT vs. other Leigh syndrome genes) is itself the most robust prognostic factor identified in the literature; there is no established genotype-severity correlation *within* MTFMT (e.g., the same c.626C>T homozygous genotype has produced both severe pediatric and milder adult-onset presentations), suggesting other prognostic biomarkers remain to be defined.

---

## 12. Treatment

There is **no MTFMT-specific or disease-modifying therapy**; management is supportive/symptomatic, following general mitochondrial disease care principles, since the searches conducted here found no MTFMT-specific clinical trial or targeted pharmacotherapy.

**Pharmacotherapy (general mitochondrial disease supportive measures, not MTFMT-specific evidence):**
- **"Mitochondrial cocktail"** components reported in the general mitochondrial disease literature: **coenzyme Q10** (NCIT — no dedicated NCIT code found in this search; CHEBI:46245 ubidecarenone/coenzyme Q10), **riboflavin** (CHEBI:17015), **thiamine** (CHEBI:9532), **L-carnitine** (CHEBI:7896), vitamin C/E as antioxidants, and creatine monohydrate for ATP buffering. **Evidence for efficacy in MTFMT deficiency specifically is absent**; even for the best-studied component (CoQ10) in primary CoQ10 deficiency, the evidence base is described as "only very weak" by systematic review (PMC9443948) — and MTFMT disease is not a primary CoQ10 biosynthesis disorder, so extrapolation is weaker still.
- **Antiarrhythmic management** (e.g., adenosine for SVT episodes) and **antihypertensive/inotropic support** were used acutely in the autonomic-crisis case report (PMID:36873085) — symptomatic, not mechanism-targeted.
- Pharmacogenomic considerations: as with mitochondrial disease broadly, **avoidance of mitochondrially toxic agents** (e.g., valproate, which can precipitate hepatic/metabolic crises in mitochondrial disease; aminoglycosides, given shared ribosomal machinery homology risk) is a standard precaution, though not specifically documented as tested in MTFMT patients in the sources reviewed.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted/immunotherapy has been reported or is in clinical trials for MTFMT deficiency specifically (no matching ClinicalTrials.gov entries were surfaced in this research).

**Surgical/interventional:** Not applicable as a primary treatment modality; cardiology-directed interventions (e.g., for arrhythmia) are managed per standard pediatric cardiology practice.

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, and speech therapy for motor/developmental impairment (NCIT:C15302 Physical Therapy; general supportive care NCIT:C15747); nutritional support given failure-to-thrive/obesity variability; low-vision services for optic atrophy; multidisciplinary mitochondrial disease clinic follow-up (cardiology, neurology, ophthalmology, endocrinology) given the multisystem risk profile documented in the 38-patient cohort.

**Experimental:** No MTFMT-specific trials identified. General mitochondrial disease trials (e.g., CoQ10 Phase III trial NCT00432744) are not MTFMT-specific and their applicability is unproven for this gene.

**Treatment outcomes:** No systematic treatment-response data exist for this ultra-rare disease; management is individualized and largely reactive to organ-specific complications (cardiomyopathy surveillance, arrhythmia management, vision/rehabilitation support).

**Treatment strategy/personalized medicine:** Given documented favorable natural history relative to other Leigh syndrome genes, clinical emphasis is on **early, accurate molecular diagnosis** (to correctly counsel prognosis and avoid overly aggressive or nihilistic care decisions based on a general "Leigh syndrome" label) combined with proactive multisystem surveillance (especially cardiac and ophthalmologic), rather than gene-specific pharmacotherapy.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk factor); the only primary-prevention lever is **reproductive/genetic**, via carrier screening and reproductive options (see Counseling below).

**Secondary prevention:** Early diagnosis via clinical suspicion (infantile hypotonia/ataxia/developmental delay with lactic acidosis and Leigh-pattern MRI) followed by prompt genetic testing enables earlier initiation of supportive multisystem surveillance (cardiac, ophthalmologic), which may mitigate morbidity from undetected complications (e.g., unrecognized cardiomyopathy or arrhythmia).

**Tertiary prevention:** Multidisciplinary surveillance protocols (cardiology, ophthalmology, neurology) aimed at early detection and management of complications in individuals with a confirmed diagnosis — extrapolated from general mitochondrial disease management guidelines, not MTFMT-specific published protocols.

**Immunization:** No MTFMT-specific vaccination consideration identified; standard pediatric immunization is generally recommended for children with mitochondrial disease to reduce risk of infection-triggered metabolic decompensation (general principle, not MTFMT-specific evidence).

**Screening and early detection:** No population or newborn screening exists for MTFMT deficiency (it is not part of standard newborn metabolic screening panels, which target treatable inborn errors of metabolism more amenable to intervention). **Carrier screening** and **prenatal diagnosis/preimplantation genetic testing (PGT-M)** are applicable once a family's causal variants are known, per standard autosomal recessive disease practice (ACMG/ACOG general frameworks; no MTFMT-specific published protocol identified).

**Genetic counseling:** Central to family management — informing carrier parents of the **25% recurrence risk** per pregnancy, explaining the wide expressivity (a family history of severe neonatal disease does not preclude a milder outcome in a subsequent affected child, given documented variable expressivity even for the same genotype), and offering reproductive options.

**Public health / environmental interventions:** Not applicable — no environmental risk factor to modify.

**Prophylaxis:** No specific prophylactic medication regimen is validated; avoidance of mitochondrially toxic drugs (see Treatment) functions as a precautionary/prophylactic measure in affected individuals.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring MTFMT-deficient disease has been reported in non-human species in the literature surveyed (no OMIA entry or veterinary case series identified).

**Orthologous gene:** Mouse ortholog **Mtfmt** (MGI:1916856) exists and is annotated in the Mouse Genome Informatics database, but a published knockout/disease-model mouse was not identified in this search (searches for "MTFMT knockout mouse model" returned only unrelated complex I gene models such as Ndufs4-KO mice, which model Leigh syndrome via a different genetic cause).

**Comparative biology — an important divergence:** The literature indicates a **notable evolutionary difference in dependence on formylation between yeast and humans**. In *Saccharomyces cerevisiae*, the MTFMT ortholog **FMT1** can be disrupted with only a mild phenotype: "*fmt1* mutants grow normally on respiratory substrates, as they are able to translate mitochondrial mRNAs in the absence of a formylated initiator methionyl-tRNA" — i.e., **yeast mitochondrial translation is largely formylation-independent**, whereas human mitochondrial translation is not, explaining why complete loss of MTFMT is compatible with viability in yeast but causes serious combined OXPHOS disease in humans. This is a mechanistically important point for interpreting any yeast-based functional data and should be flagged in a `HUMAN_MODEL_MISMATCH`-type discussion if this disease is curated into a module/disease entry with model-organism claims.

**Zoonotic potential/transmission:** Not applicable (purely genetic, non-transmissible disease).

---

## 15. Model Organisms

**Cellular/patient-derived models:** The overwhelming majority of functional data for MTFMT disease comes from **patient-derived primary skin fibroblasts**, in which:
- Met-tRNA^Met^ formylation is directly measured and shown to be impaired (PMID:21907147).
- Mitochondrial translation (metabolic labeling of newly synthesized mtDNA-encoded polypeptides) is severely reduced.
- The translation defect is **rescued by exogenous expression of wild-type MTFMT**, providing direct causal/complementation evidence (PMID:21907147) — this is the strongest mechanistic evidence available for the gene-disease relationship.
- Steady-state levels of complex I and complex IV subunits are reduced by immunoblot/BN-PAGE (PMID:24461907, PMID:30911575).

**Yeast model:** *S. cerevisiae fmt1Δ* deletion strains have been used to study the mitochondrial methionyl-tRNA formyltransferase pathway's substrate specificity and to demonstrate that yeast — unlike humans — largely tolerates loss of this enzyme (ACS Biochemistry, 2003 paper on gene disruption and tRNA substrate specificity in yeast Fmt1). **Model limitation:** this makes yeast a poor phenotypic/disease model for human MTFMT deficiency, though it remains useful for basic biochemical/mechanistic dissection of the formylation reaction itself (relevant also to a related pathway component, Msc6p, required for mitochondrial translation initiation "in the absence of formylated Met-tRNAfMet" in yeast, described in a 2019 FEBS Journal paper).

**Recombinant/biochemical models:** Purified recombinant human MTFMT (wild-type and disease-associated mutant forms) has been biochemically characterized in vitro to directly measure the catalytic impact of specific pathogenic missense variants (PMID:25288793) — this is a validated approach for genotype-function correlation, though not a whole-organism or whole-cell disease model.

**Mouse model:** No published Mtfmt knockout or disease-recapitulating mouse model was identified in this search, representing a **gap in the model-organism landscape** for this disease relative to other Leigh-syndrome genes (e.g., the well-characterized Ndufs4-KO mouse used to model complex I-deficient Leigh syndrome, or the Mto1-deficient mouse model for a different mitochondrial translation factor). This gap should be noted explicitly if curated as a `HUMAN_MODEL_MISMATCH`/knowledge-gap discussion, since the field currently relies on patient fibroblasts and heterologous complementation rather than an in vivo model recapitulating the neurodegenerative Leigh-syndrome phenotype.

**Zebrafish/Drosophila/C. elegans:** No MTFMT-specific model in these organisms was identified in this search (searches surfaced unrelated mitoribosome-rescue-factor zebrafish knockouts, e.g., Ict1/Mtrfr, but not Mtfmt itself).

**Research applications enabled by existing models:** Patient fibroblasts and the complementation/rescue system established by Tucker et al. (2011) remain the primary experimental platform for (a) confirming variant pathogenicity, (b) dissecting the biochemical step (formylation vs. downstream translation) affected by a given allele, and (c) correlating genotype with the degree of complex I/IV loss — but they cannot address organismal-level questions (e.g., why the neurological phenotype is comparatively mild/nonprogressive, or the tissue-selectivity of basal ganglia/brainstem vulnerability), which is exactly the gap an in vivo model would need to fill.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested term | ID |
|---|---|---|
| Disease | Combined oxidative phosphorylation defect type 15 | MONDO:0013987 |
| Gene | MTFMT | HGNC:29666 |
| Molecular function | methionyl-tRNA formyltransferase activity | GO:0004479 |
| Biological process | mitochondrial translational initiation | GO:0070124 |
| Biological process | oxidative phosphorylation | GO:0006119 |
| Cellular component | mitochondrial matrix | GO:0005759 |
| Phenotype | Hypotonia | HP:0001252 |
| Phenotype | Gait ataxia | HP:0002066 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Lactic acidosis | HP:0003128 |
| Phenotype | Leigh disease | HP:0002490 |
| Phenotype | Optic atrophy | HP:0000648 |
| Phenotype | Nystagmus | HP:0000639 |
| Phenotype | Hypertrophic cardiomyopathy (cardiac dysfunction subset) | HP:0001639 |
| Anatomy | Basal ganglion | UBERON:0002420 |
| Anatomy | Midbrain | UBERON:0001894 |

*(All ontology suggestions should be verified against live OAK/ontology lookups before binding into any curated knowledge base record, per standard curation discipline — labels and dynamic-enum membership have not been independently re-verified beyond what is reflected in the search results above.)*

---

## Primary Sources Cited

- Tucker EJ, et al. Mutations in MTFMT underlie a human disorder of formylation causing impaired mitochondrial translation. *Cell Metab.* 2011;14(3):428-434. **PMID:21907147**.
- Haack TB, et al. Phenotypic spectrum of eleven patients and five novel MTFMT mutations identified by exome sequencing and candidate gene screening. *Mol Genet Metab.* 2014;111(3):342-352. **PMID:24461907**.
- Hayhurst H, et al. Leigh syndrome caused by mutations in MTFMT is associated with a better prognosis. *Ann Clin Transl Neurol.* 2019. **PMID:30911575**.
- [Autonomic instability, arrhythmia and visual impairment in a new presentation of MTFMT-related mitochondrial disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC9981406/). *JIMD Rep.* 2023. **PMID:36873085**.
- Nonprogressive Mobile Dystonia in MTFMT-Related Mitochondrial Disease. **PMID:36704074**.
- Leigh syndrome followed by parkinsonism in an adult with homozygous c.626C>T mutation in MTFMT. *Neurol Genet.* **PMC6278240**.
- Biochemical characterization of pathogenic mutations in human mitochondrial methionyl-tRNA formyltransferase. **PMID:25288793**.
- [OMIM #614947 — COMBINED OXIDATIVE PHOSPHORYLATION DEFICIENCY 15](https://www.omim.org/entry/614947)
- [OMIM *611766 — MITOCHONDRIAL METHIONYL-tRNA FORMYLTRANSFERASE; MTFMT](https://omim.org/entry/611766)
- [OMIM #618248 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 27](https://www.omim.org/entry/618248)
- [Orphanet ORPHA:319524](https://www.orpha.net/en/disease/detail/319524)
- [GARD — Combined oxidative phosphorylation defect type 15](https://rarediseases.info.nih.gov/diseases/17456/combined-oxidative-phosphorylation-defect-type-15)
- [ClinVar — MTFMT c.626C>T (p.Ser209Leu)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000190888/)
- [GeneCards — MTFMT](https://www.genecards.org/cgi-bin/carddisp.pl?gene=MTFMT)
- Multicenter study on Leigh syndrome: disease course and predictors of survival (general Leigh syndrome comparator cohort). **PMC4021638**.

**Note on scope/limitations of this report:** MTFMT/COXPD15 is an ultra-rare disease whose literature base, while primary and PMID-backed, is limited to case reports and cohort studies rather than large-scale omics, dedicated clinical trials, or an in vivo animal model — these gaps (no mouse/zebrafish model, no MTFMT-specific trial, no transcriptomic/proteomic dataset) are reported explicitly above rather than filled with extrapolated or unsourced claims. Two disambiguation points are worth flagging prominently for downstream curation: (1) **MRPL44** causes a *different*, allelic-sounding disease (COXPD16, OMIM #615395) with overlapping hypertrophic-cardiomyopathy features — do not conflate the two genes; (2) the recurrent **c.626C>T** allele's protein-level name (p.Ser209Leu) is a nomenclature artifact of a splice-disrupting variant that actually causes exon skipping and frameshift, not a simple amino acid substitution.