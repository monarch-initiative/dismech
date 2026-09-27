---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T01:39:08.591591'
end_time: '2026-09-04T01:43:47.006307'
duration_seconds: 278.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 17
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
  num_turns: 24
  total_cost_usd: 1.3805762000000001
  session_id: 1d4c83ee-98b8-54c2-892b-3815ba752722
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 17
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 17** covering all of the
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

I'll research this by searching authoritative genetics/cardiology databases for the specific OMIM "Hypertrophic Cardiomyopathy 17" locus and gene.

I now have sufficient primary-literature material to compile the comprehensive report.

# Hypertrophic Cardiomyopathy 17 (CMH17 / JPH2-Related Hypertrophic Cardiomyopathy) — Research Report

## 1. Disease Information

**Overview.** Hypertrophic Cardiomyopathy 17 (CMH17) is a rare, autosomal dominant form of familial hypertrophic cardiomyopathy (HCM) caused by heterozygous missense mutations in **JPH2** (junctophilin-2, chromosome 20q13.12), a non-sarcomeric structural protein essential for cardiac excitation–contraction coupling. It represents one of the "minor" genetic subtypes of HCM — distinct from the major sarcomeric-protein loci (MYH7/CMH1, MYBPC3/CMH4, etc.) — and was the first human disease linked to genetic defects in a junctional membrane complex (JMC) protein rather than a sarcomere or Z-disc component (Landstrom et al., 2007, PMID:17509612).

**Key identifiers:**
- **OMIM phenotype:** #613873 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 17; CMH17 ([OMIM entry 613873](https://omim.org/entry/613873))
- **OMIM gene:** *605267 — JUNCTOPHILIN 2; JPH2 (chr 20q13.12)
- **HGNC:** JPH2, hgnc:19420
- **MONDO:** The general "familial hypertrophic cardiomyopathy" umbrella term is MONDO:0005045 (also cross-referenced as MONDO:0024573 for the broader "familial hypertrophic cardiomyopathy" concept); no CMH17-specific MONDO subtype term was found in the searches performed — CMH17 currently maps as a JPH2-caused subtype under the general HCM MONDO node, consistent with ClinGen's own use of MONDO:0005045 for the JPH2–HCM gene-disease validity curation.
- **ClinGen Gene-Disease Validity:** JPH2–HCM classified **Moderate** (autosomal dominant), re-affirmed on 2022 re-curation ([ClinGen CGGV assertion](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_378a727d-0c5b-4563-9c96-ac18a2902742-2017-07-18T160000.000Z))
- **Inheritance:** Autosomal dominant (for the HCM phenotype; biallelic JPH2 loss-of-function variants instead cause a distinct, more severe dilated cardiomyopathy/early heart-failure phenotype — see §9)
- **Synonyms:** CMH17; Junctophilin-2-related hypertrophic cardiomyopathy; JPH2 cardiomyopathy

**Provenance of information:** Data are aggregated disease-level findings from case series/cohort studies (Landstrom 2007; Matsushita 2007, PMID for Japanese G505S/R436C cohort; Vanninen et al. Finnish T161K family study, PMC6147424) rather than a single large EHR-derived cohort — reflecting the rarity of this HCM subtype (only ~16 probands/6 unique variants reported across 5 publications as of the 2022 ClinGen curation).

Sources: [OMIM #613873](https://omim.org/entry/613873), [OMIM *605267](https://omim.org/entry/605267), [ClinGen JPH2-HCM](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_378a727d-0c5b-4563-9c96-ac18a2902742-2017-07-18T160000.000Z), [PubMed 17509612](https://pubmed.ncbi.nlm.nih.gov/17509612/)

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic — heterozygous missense variants in JPH2 disrupting the junctophilin-2 protein's calcium-handling scaffolding function at the cardiomyocyte junctional membrane complex.

**Genetic risk factors:**
- Causal heterozygous JPH2 missense variants: S101R, Y141H, S165F (Landstrom 2007, PMID:17509612); G505S, R436C (Matsushita 2007, Japanese cohort, *Journal of Human Genetics*); T161K/p.(Thr161Lys) (Vanninen et al., Finnish founder variant, PMC6147424); E169K (Beavers/Landstrom et al. 2013, JACC, PMID:23973696 — associated with juvenile-onset paroxysmal atrial fibrillation in the context of HCM screening).
- The ClinGen panel notes "considerable background noise" in the JPH2 variant literature — i.e., population-level rare-variant burden complicates unambiguous pathogenicity assignment for novel missense changes, which is part of why the gene-disease validity is capped at **Moderate** rather than Definitive/Strong.
- No modifier genes for CMH17 specifically were identified in the literature reviewed; general HCM modifier-gene concepts (e.g., ACE, hypertension-associated loci influencing hypertrophy severity) apply nonspecifically across HCM genotypes but were not documented for JPH2 carriers specifically.

**Environmental/lifestyle risk factors:** None specific to CMH17 were identified; as with sarcomeric HCM, intense athletic conditioning and systemic hypertension can influence phenotypic expression/exacerbation of LVH in genotype-positive individuals generically, but no JPH2-specific environmental interaction data were found.

**Protective factors:** None reported specifically for JPH2; variant absence from gnomAD/ExAC/1000 Genomes population databases is used as supporting evidence *against* the variant being common/benign, not as a described protective factor per se.

**Gene-environment interaction:** Not specifically studied for JPH2-HCM in the literature surveyed.

Sources: [PMID:17509612](https://pubmed.ncbi.nlm.nih.gov/17509612/), Matsushita et al., *J Hum Genet* ([nature.com/articles/jhg200774](https://www.nature.com/articles/jhg200774)), [PMC6147424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6147424/), [PMID:23973696](https://pubmed.ncbi.nlm.nih.gov/23973696/)

---

## 3. Phenotypes

Because CMH17 is a form of HCM, its core phenotype overlaps substantially with sarcomeric HCM but with a documented additional burden of **conduction disease and arrhythmia**, reflecting JPH2's specific role in calcium-channel/ryanodine-receptor coupling (rather than pure sarcomeric hypercontractility).

| Phenotype | Frequency/detail (from JPH2 cohorts) | Suggested HP term |
|---|---|---|
| Left ventricular hypertrophy | Defining feature; mean max wall thickness 20.4±5.2 mm in the Finnish T161K cohort (n=20 heterozygotes) | HP:0001639 (Hypertrophic cardiomyopathy) / HP:0001712 (Left ventricular hypertrophy) |
| Atrial/ventricular arrhythmia | 13/20 (65%) of T161K heterozygotes | HP:0011675 (Arrhythmia) |
| Conduction defects (3rd-degree AV block, bundle branch block) | ~45% of T161K-affected individuals | HP:0011711 (Third degree atrioventricular block) / HP:0005110 (Atrioventricular block) |
| Systolic dysfunction / heart failure (some end-stage) | ~45% of T161K cohort | HP:0001635 (Congestive heart failure) |
| Paroxysmal atrial fibrillation (juvenile onset) | Reported in E169K carriers (2/203 screened HCM probands) | HP:0004758 (Paroxysmal atrial fibrillation) |
| Age-dependent penetrance | 71% penetrant by age 60, 100% by age 80 (T161K) | n/a (penetrance descriptor) |
| Age of onset | Mean 26.9±20.6 years at diagnosis (T161K cohort) — wide variance reflecting age-dependent penetrance | — |

**Progression:** Age-dependent, progressive — increasing penetrance with age and progression to systolic heart failure documented in a subset of carriers, distinguishing it somewhat from the more classically "stable" hypertrophic phenotype of some sarcomeric HCM forms. The authors of the Finnish study characterize T161K-associated disease as "atypical HCM" given the prominent conduction-system and heart-failure component.

**Quality of life:** Not separately quantified in JPH2-specific literature; general HCM QoL burden (exertional dyspnea, arrhythmia-related limitation) applies.

Sources: [PMC6147424 (Vanninen et al.)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6147424/), [PMID:23973696](https://pubmed.ncbi.nlm.nih.gov/23973696/)

---

## 4. Genetic/Molecular Information

**Causal gene:** JPH2 (HGNC:19420; OMIM *605267), chromosome 20q13.12. Encodes junctophilin-2, a cardiac-specific member of the junctophilin family that spans the sarcoplasmic reticulum (SR) membrane via a C-terminal transmembrane domain while its N-terminal MORN (Membrane Occupation and Recognition Nexus) repeat domain tethers to the plasma membrane/T-tubule, physically bridging the L-type calcium channel (CaV1.2) at the T-tubule with the ryanodine receptor (RyR2) on the SR — the structural basis of cardiac calcium-induced calcium release (CICR).

**Reported pathogenic/likely pathogenic missense variants (heterozygous, HCM-associated):**

| Variant (protein) | Cohort/publication | Notes |
|---|---|---|
| p.Ser101Arg (S101R) | Landstrom 2007, PMID:17509612 | 1 of 388 unrelated white HCM probands negative for 8 myofilament + 5 Z-disc genes |
| p.Tyr141His (Y141H) | Landstrom 2007 | Same cohort |
| p.Ser165Phe (S165F) | Landstrom 2007; mechanistic follow-up in Communications Biology 2025 (PMID:41291214) | Absent in 1000 ethnic-matched control alleles; shown to cause JPH2 autoinhibition disrupting CaV1.2 binding |
| p.Gly505Ser (G505S) | Matsushita et al. 2007, Japanese cohort | Identified in 4 unrelated Japanese probands; statistically significant vs. controls; not found in DCM or RCM patients |
| p.Arg436Cys (R436C) | Matsushita et al. 2007 | Found but did not reach statistical significance vs controls |
| p.Thr161Lys / T161K | Vanninen et al., PLOS ONE 2018, PMC6147424; functional iPSC-CM study PMID:37371654 | Finnish founder variant; 20 affected individuals across 9 families; co-segregation in 6/9 families |
| p.Glu169Lys / E169K | Beavers/Landstrom et al. 2013, JACC, PMID:23973696 | Found in 2/203 unrelated HCM probands screened for juvenile-onset paroxysmal AF; impairs JPH2–RyR2 binding, causing SR Ca²⁺ leak |

**Variant classification (ACMG/ClinVar):** Most JPH2 variants are submitted to ClinVar but "are often classified as variants of uncertain significance (VUS) due to a lack of family member surveillance and segregation studies," though several (e.g., T161K, S165F) have been upgraded from VUS to likely pathogenic/pathogenic with additional segregation and functional evidence. Population database absence (gnomAD, ExAC, 1000 Genomes) is consistently cited as supporting evidence across these variants.

**Functional consequences:** All studied HCM-associated JPH2 missense variants converge on a mechanism of **disrupted intracellular calcium handling and junctional membrane complex disorganization**, rather than the sarcomeric hypercontractility mechanism of MYH7/MYBPC3 HCM:
- Landstrom (2007): "Each human mutation caused (i) protein reorganization of junctophilin-2, (ii) perturbations in intracellular calcium signaling, and (iii) marked cardiomyocyte hyperplasia [hypertrophy]" in cellular overexpression models.
- S165F (Nature Communications Biology 2025, PMID:41291214): induces an aberrant intramolecular ("autoinhibitory") interaction within JPH2 that folds back onto its own N-terminal MORN-repeat inner groove — the normal CaV1.2 cytoplasmic-tail binding site — thereby disrupting the JPH2–CaV1.2 interaction, compromising ER/SR–plasma-membrane junctions, and producing hypertrophy in COS7 and H9c2 cell models.
- T161K (Biomedicines 2023, PMID:37371654): iPSC-cardiomyocytes show prolonged action potential duration (APD50, APD90), slowed L-type calcium current (ICa) inactivation kinetics, and phase-3 early afterdepolarizations (EADs) correlating with slower ICa inactivation — providing a direct cellular arrhythmogenic mechanism.
- E169K (JACC 2013, PMID:23973696): impairs JPH2 binding to RyR2, reducing RyR2 stabilization and promoting SR Ca²⁺ leak → triggered activity → atrial arrhythmia, replicated in a JPH2-E169K mouse model.

**Modifier genes:** None specifically documented for CMH17.

**Epigenetic information:** No JPH2/CMH17-specific epigenetic (DNA methylation/histone) data identified.

**Chromosomal abnormalities:** None — CMH17 is caused by point (missense) mutations, not structural chromosomal rearrangements.

**Genetic heterogeneity note:** Biallelic (homozygous/compound heterozygous), typically loss-of-function, JPH2 variants cause a **distinct, more severe recessive phenotype** — early-onset dilated cardiomyopathy (DCM) and heart failure — as opposed to the dominant missense-driven HCM phenotype of CMH17 (see §9 and the systematic review below).

Sources: [PMID:17509612](https://pubmed.ncbi.nlm.nih.gov/17509612/), [Matsushita 2007 (J Hum Genet)](https://www.nature.com/articles/jhg200774), [PMID:41291214 / Commun Biol 2025](https://www.nature.com/articles/s42003-025-09244-9), [PMID:37371654 / Biomedicines 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10295168/), [PMID:23973696 / JACC 2013](https://www.jacc.org/doi/10.1016/j.jacc.2013.06.052), [OMIM *605267](https://omim.org/entry/605267)

---

## 5. Environmental Information

No JPH2/CMH17-specific environmental, toxin, occupational, or infectious-agent contributors were identified in the literature surveyed. As a monogenic structural-protein cardiomyopathy, environmental contribution is presumed secondary/modifying rather than causal (as with general HCM, systemic hypertension and intense endurance exercise are nonspecific modifiers of hypertrophy severity, but this was not documented specifically for JPH2 carriers).

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. A heterozygous missense mutation in JPH2 (e.g., S165F, T161K, E169K, G505S) **alters the structure of junctophilin-2's N-terminal MORN-repeat domain or its RyR2/CaV1.2-binding surfaces**, demonstrated directly for S165F, which is shown by AlphaFold-guided structural and biochemical analysis to fold back and autoinhibit its own CaV1.2-binding groove (PMID:41291214).
2. This structural perturbation **impairs JPH2's tethering function at the junctional membrane complex (JMC)** — the specialized ER/SR–T-tubule junction where JPH2 normally holds the plasma-membrane L-type Ca²⁺ channel (CaV1.2) in close apposition (~12–15 nm) to the SR ryanodine receptor (RyR2), leading to (i) impaired CaV1.2 tethering (S165F) and/or (ii) impaired RyR2 stabilization (E169K).
3. Loss of JMC integrity and impaired JPH2–RyR2/CaV1.2 coupling **disrupts calcium-induced calcium release (CICR)**: SR Ca²⁺ leak (E169K mechanism, via reduced RyR2 stabilization) or altered ICa inactivation kinetics (T161K mechanism, via prolonged L-type current) — both documented directly in patient-derived/mutant cellular models.
4. Disrupted calcium signaling **drives two parallel downstream consequences**, branching by which aspect of Ca²⁺ handling is most affected:
   - **Branch A (hypertrophic remodeling):** Chronic altered intracellular Ca²⁺ handling and JMC disorganization triggers compensatory/maladaptive cardiomyocyte hypertrophic signaling, producing cardiomyocyte enlargement in cellular overexpression models (S101R/Y141H/S165F; Landstrom 2007) and, in vivo, hypertrophic interventricular septum, increased LV mass, and asymmetric LV hypertrophy in a JPH2 mouse model, with histology confirming cardiomyocyte hypertrophy and disarray "consistent with HCM" (per ClinGen curation).
   - **Branch B (arrhythmogenesis):** SR Ca²⁺ leak / prolonged Ca²⁺ current inactivation causes triggered activity — early afterdepolarizations documented directly in T161K iPSC-cardiomyocytes ("The occurrence of phase 3 EADs during the spontaneous beating was only observed in T161K hiPSC-CMs") and atrial arrhythmia in E169K carriers and mice via impaired RyR2 stabilization → SR Ca²⁺ leak → triggered activity.
5. Clinically, Branch A manifests as **left ventricular hypertrophy, diastolic dysfunction, and (in a subset) progression to systolic heart failure**; Branch B manifests as **atrial/ventricular arrhythmia, atrioventricular conduction block, and increased sudden cardiac death risk** — the two branches co-occurring within the same patients/families (e.g., 65% arrhythmia prevalence and 45% conduction-defect prevalence alongside LVH in the T161K Finnish cohort), which is the basis for characterizing JPH2-HCM as clinically "atypical" relative to purely sarcomeric HCM.
6. This dual hypertrophic + arrhythmogenic mechanism is inferred to be **distinct from sarcomeric HCM's primary mechanism** (myofilament hypercontractility/inefficient ATP utilization from MYH7/MYBPC3/TNNT2 variants), and is instead grounded in a **calcium-handling/JMC-structural** pathway — making CMH17 mechanistically closer to certain arrhythmia syndromes (e.g., catecholaminergic polymorphic ventricular tachycardia, which also involves RyR2 dysregulation) than to classical sarcomeric HCM, though the downstream hypertrophic phenotype converges with sarcomeric HCM.

### Category detail

- **Molecular pathways:** Calcium-induced calcium release (CICR) at the cardiac junctional membrane complex; L-type calcium channel (CaV1.2)–ryanodine receptor 2 (RyR2) coupling.
- **Cellular processes:** Impaired excitation–contraction coupling; cardiomyocyte hypertrophic remodeling; SR Ca²⁺ leak; triggered arrhythmic activity (early afterdepolarizations).
- **Protein dysfunction:** Loss of normal JPH2 tertiary structure/binding-groove accessibility (autoinhibition in S165F); impaired protein–protein interaction with CaV1.2 and RyR2; reported "protein reorganization" of junctophilin-2 in cellular models.
- **Biochemical/ion-channel abnormalities:** Slowed L-type Ca²⁺ current (ICa) inactivation kinetics (T161K); reduced RyR2 stabilization / increased SR Ca²⁺ leak (E169K).
- **Tissue damage mechanisms:** Cardiomyocyte hypertrophy and myocyte disarray (general HCM hallmark, documented in the JPH2 mouse model).
- **Single-cell/advanced technology findings:** Perforated patch-clamp electrophysiology and digital-image-correlation contractility analysis in CRISPR-corrected isogenic iPSC-cardiomyocyte pairs (T161K study) represent the most granular functional dataset available for a JPH2 HCM variant.

**Suggested GO terms:** GO:0086013 (membrane repolarization in ventricular cardiac muscle cell), GO:0086036 (regulation of cardiac muscle cell membrane potential), GO:0014809 (regulation of skeletal muscle contraction by regulation of release of sequestered calcium ion — analogous cardiac process is GO:0010881, regulation of cardiac muscle contraction by regulation of the release of sequestered calcium ion), GO:0007512 (adult heart development, for hypertrophic remodeling context).
**Suggested CL term:** CL:0002129 (cardiac muscle myoblast) / CL:0000746 (cardiac muscle cell).

Sources: [PMID:17509612](https://pubmed.ncbi.nlm.nih.gov/17509612/), [PMID:41291214](https://www.nature.com/articles/s42003-025-09244-9), [PMID:37371654](https://pmc.ncbi.nlm.nih.gov/articles/PMC10295168/), [PMID:23973696](https://www.jacc.org/doi/10.1016/j.jacc.2013.06.052), [ClinGen JPH2-HCM curation](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_378a727d-0c5b-4563-9c96-ac18a2902742-2017-07-18T160000.000Z)

---

## 7. Anatomical Structures Affected

- **Organ level:** Heart (primary); cardiovascular system. Secondary complications from arrhythmia/heart failure can involve pulmonary congestion, cerebral embolism (from AF-related thrombus, general HCM risk), etc.
- **Anatomical site (UBERON):** Left ventricle (specifically the interventricular septum, per the JPH2 mouse model showing "hypertrophic interventricular septum"), UBERON:0002082 (cardiac ventricle) / UBERON:0006566 (interventricular septum).
- **Tissue/cell level:** Cardiac muscle tissue; cardiomyocytes (CL:0000746) specifically at the T-tubule/sarcoplasmic-reticulum junction.
- **Subcellular level (GO Cellular Component):** Junctional sarcoplasmic reticulum membrane / T-tubule (GO:0014701, junctional sarcoplasmic reticulum membrane), plasma membrane, L-type calcium channel complex, ryanodine receptor complex.
- **Laterality:** Not applicable (LVH is typically asymmetric-septal in HCM generally, as noted in the mouse model — "asymmetric LV hypertrophy").

---

## 8. Temporal Development

- **Onset:** Variable, age-dependent; mean age at diagnosis 26.9±20.6 years in the largest documented JPH2-HCM cohort (T161K, Finnish), reflecting a wide range from young adulthood into later life.
- **Progression:** Age-dependent penetrance — 71% penetrant by age 60, 100% by age 80 (T161K cohort) — with disease course progressing from isolated LVH to, in a substantial subset (~45%), systolic dysfunction/heart failure, including some cases of "end-stage severe left ventricular failure."
- **Pattern:** Progressive overall, but arrhythmic events (atrial/ventricular arrhythmia in 65% of T161K carriers) can be episodic/paroxysmal within an overall progressive structural disease course.
- **Critical periods:** Not specifically defined for JPH2-HCM; general HCM natural-history literature emphasizes adolescence/young adulthood as when LVH typically becomes echocardiographically apparent, consistent with the mean age-of-diagnosis data above.

---

## 9. Inheritance and Population

- **Epidemiology:** CMH17 has no disease-specific prevalence estimate (extremely rare; only ~16 probands / 6 unique variants across 5 publications reported through 2022 per ClinGen). General HCM prevalence (all genetic causes combined) is estimated at 1:500 by echocardiographic LVH criteria, with some estimates as high as 1:200–1:250 when genetic testing and family cascade screening are incorporated.
- **Inheritance pattern:** Autosomal dominant for the HCM phenotype (heterozygous missense variants). Notably, JPH2 displays **two distinct modes of inheritance mapping to different phenotypes**: a systematic review ("One gene, two modes of inheritance, four diseases," *Trends in Cardiovascular Medicine*, 2021, [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1050173821001420)) of 61 variant-positive individuals found that:
  - **Autosomal dominant, heterozygous** missense variants → HCM (76% of AD cases) and arrhythmia/SCD (24% of AD cases).
  - **Autosomal recessive, homozygous/compound-heterozygous, typically loss-of-function** variants → early-onset dilated cardiomyopathy (DCM) with severe early heart failure (distinct from CMH17 proper).
  - Overall breakdown across the reviewed cohort: ~80% had cardiac disease, comprising 47% HCM, 18% DCM, and 14% arrhythmia/SCD.
- **Penetrance:** Age-dependent and incomplete at younger ages — 71% by age 60, 100% by age 80 in the best-documented (T161K) family series — consistent with typical incomplete/age-dependent penetrance seen across HCM genotypes generally.
- **Expressivity:** Variable — carriers of the same variant (T161K) range from isolated LVH to arrhythmia/conduction block to end-stage heart failure.
- **Founder effects:** T161K is described as a **Finnish founder variant**, identified across nine unrelated Finnish families.
- **Consanguinity:** Relevant primarily to the distinct recessive/biallelic JPH2-DCM phenotype (not CMH17 itself), where homozygous loss-of-function variants have been reported, e.g., in a Greater Middle Eastern cohort with a novel homozygous variant causing neonatal DCM (PMC6588559).
- **Sex ratio / geographic distribution:** No JPH2-specific sex-ratio data were identified; variants have been reported in white/Caucasian (Landstrom 2007), Japanese (Matsushita 2007), and Finnish (Vanninen 2018) cohorts, indicating the gene is not population-restricted, though individual variants (T161K) show founder-population clustering.

Sources: [PMC6147424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6147424/), [ScienceDirect systematic review](https://www.sciencedirect.com/science/article/abs/pii/S1050173821001420), [PMC6588559](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6588559/), [ClinGen curation](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_378a727d-0c5b-4563-9c96-ac18a2902742-2017-07-18T160000.000Z)

---

## 10. Diagnostics

- **Clinical tests:** Echocardiography (2D/Doppler) to document LV wall thickness ≥15 mm (or ≥13 mm with family history) in the absence of another cause; cardiac MRI for detailed wall-thickness/fibrosis (late gadolinium enhancement) assessment (general HCM standard, not JPH2-specific in the sources reviewed).
- **Electrophysiology:** 12-lead ECG and ambulatory Holter monitoring are of particular relevance for CMH17 given the documented high burden of arrhythmia (65%) and conduction defects including third-degree AV block (LOINC/clinical neurophysiology standard tests); electrophysiologic study may be warranted given the AV-block burden.
- **Genetic testing:** JPH2 is included as a "minor"/secondary gene on comprehensive HCM multi-gene panels (alongside the core sarcomeric genes MYH7, MYBPC3, TNNT2, TNNI3, TPM1, MYL2, MYL3, ACTC1, and other minor genes such as PRKAG2, CSRP3, TNNC1, PLN, JPH2 itself). Given the Moderate (not Definitive) ClinGen gene-disease validity classification, JPH2 variant results should be interpreted with caution and ideally supported by segregation data.
- **Functional/research-grade diagnostics:** Patient-specific iPSC-cardiomyocyte modeling with isogenic CRISPR-corrected controls has been used as a research-grade functional validation tool for a specific JPH2 variant (T161K) to establish pathogenicity via electrophysiological phenotyping.
- **Differential diagnosis:** Other genetic HCM causes (sarcomeric-gene HCM, RASopathy-associated HCM, glycogen-storage/PRKAG2 cardiomyopathy, Fabry disease, Danon disease, amyloidosis/transthyretin or AL) — general HCM differential, not JPH2-specific literature found.
- **Screening:** Cascade family genetic screening is implied as standard given the autosomal dominant inheritance and documented within-family segregation (6/9 Finnish families) with age-dependent penetrance, supporting periodic re-screening of genotype-positive/phenotype-negative relatives as they age (given 100% penetrance is not reached until age 80).

Sources: [PMC6147424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6147424/), [PMID:37371654](https://pmc.ncbi.nlm.nih.gov/articles/PMC10295168/)

---

## 11. Outcome/Prognosis

- **Mortality/SCD risk:** No JPH2-specific SCD incidence rate was identified; general HCM literature reports an overall SCD incidence of ~1%/year in adults, and HCM is the most common identifiable cause of sudden cardiac death in individuals under 35 in the U.S., including athletes. Given CMH17's documented arrhythmia burden (65% arrhythmia, 45% conduction block, and specific EAD-driven arrhythmogenic mechanism for T161K), individualized SCD risk stratification is particularly relevant, though no JPH2-specific SCD risk model exists.
- **Heart failure progression:** Systolic dysfunction develops in ~45% of the T161K cohort, with a subset progressing to end-stage LV failure — indicating a comparatively higher heart-failure burden than typically reported for classic sarcomeric HCM cohorts (where heart failure with reduced ejection fraction, or "burnt-out" HCM, occurs in a minority, generally cited around 5–10% over long-term follow-up in sarcomeric HCM literature, though this comparison figure was not independently re-verified for this report).
- **Complications:** Third-degree AV block requiring consideration of pacemaker implantation; atrial fibrillation/flutter with thromboembolic risk; ventricular arrhythmia.
- **Prognostic factors:** Age (penetrance and disease burden both increase with age); specific variant (T161K carries a well-documented conduction-disease/heart-failure phenotype; E169K is specifically linked to arrhythmia rather than isolated LVH).

Sources: [PMC6147424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6147424/), [StatPearls HCM overview](https://www.ncbi.nlm.nih.gov/books/NBK430788/)

---

## 12. Treatment

No JPH2/CMH17-specific treatment trial data were identified; management follows general HCM treatment algorithms, informed by CMH17's particular arrhythmia/conduction-disease burden.

- **Pharmacotherapy (general HCM, applicable to CMH17):**
  - Beta-blockers and non-dihydropyridine calcium channel antagonists (e.g., verapamil) — first-line for symptomatic obstructive/non-obstructive HCM (NCIT:C15986, Pharmacotherapy; therapeutic_agent classes: beta-adrenergic antagonists, calcium channel blockers).
  - **Cardiac myosin inhibitors** (novel disease-modifying drug class for obstructive HCM):
    - **Mavacamten** — first-in-class allosteric cardiac myosin ATPase inhibitor, FDA-approved 2022 for NYHA class II–III symptomatic obstructive HCM, reduces hypercontractility. Available only through a REMS program.
    - **Aficamten** — next-generation cardiac myosin inhibitor, FDA-approved December 2024/2025 based on the SEQUOIA-HCM phase 3 trial, which showed ~60% of aficamten-treated patients had improved physical-activity-limitation scores versus 24% placebo. Also REMS-restricted.
    - These agents target the hypercontractile sarcomeric mechanism and are approved for **obstructive** HCM broadly; no data specifically address efficacy in JPH2-driven (non-sarcomeric) HCM, where the primary mechanism is calcium-handling/JMC dysfunction rather than sarcomeric hypercontractility — a potentially important mechanistic mismatch for future study.
  - Antiarrhythmic therapy (e.g., amiodarone, disopyramide for obstructive symptoms) and anticoagulation for atrial fibrillation, given CMH17's documented AF burden.
- **Device/interventional therapy:**
  - **Permanent pacemaker implantation** — particularly relevant given the ~45% third-degree AV block/conduction-defect burden documented in CMH17 (T161K cohort), an unusually high rate compared to classic sarcomeric HCM.
  - **Implantable cardioverter-defibrillator (ICD)** for primary/secondary SCD prevention per standard HCM risk stratification (NCIT device-category concept; clinical action term NCIT:C15329, Surgical Procedure, for implantation).
  - **Septal reduction therapy** (surgical myectomy or alcohol septal ablation) for drug-refractory obstructive physiology (NCIT:C15329, Surgical Procedure / NCIT:C16186, Orthopedic Surgical Procedure is not applicable — better mapped to general cardiac surgical procedure terms).
- **Supportive care:** Standard heart-failure management (diuretics, guideline-directed medical therapy) for the subset progressing to systolic dysfunction.
- **Genetic counseling:** Recommended given autosomal dominant inheritance with age-dependent penetrance (NCIT:C15240, Genetic Counseling).
- **Experimental/research-stage:** JPH2 gene-therapy approaches (AAV-mediated JPH2 overexpression) have shown efficacy in rescuing heart-failure phenotypes in preclinical (non-HCM-specific, general heart-failure) models per search results (International Journal of Cardiology), representing a potential future targeted approach for JPH2-related cardiomyopathy specifically, though not yet in human trials for CMH17.

Sources: [FDA aficamten approval / Healio](https://www.healio.com/news/cardiology/20251219/fda-approves-aficamten-for-adults-with-obstructive-hcm), [Mavacamten StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK582152/), [Eur Heart J mavacamten review](https://academic.oup.com/eurheartj/article/44/44/4622/7296449)

---

## 13. Prevention

No JPH2/CMH17-specific primary-prevention data exist (monogenic disease; primary prevention is not applicable in the traditional sense). Standard applicable measures:

- **Secondary prevention:** Cascade genetic screening of at-risk relatives given autosomal dominant inheritance and documented within-family segregation; periodic re-screening given age-dependent penetrance (up to age 80).
- **Tertiary prevention:** ICD implantation for SCD prevention in high-risk carriers; pacemaker for progressive conduction disease; anticoagulation for AF-related stroke prevention.
- **Genetic counseling:** Reproductive counseling for carriers, standard for autosomal dominant cardiomyopathy.
- **Prenatal/preimplantation genetic testing:** Not specifically documented for JPH2 in the sources reviewed, but methodologically available as for other monogenic AD cardiomyopathies via standard PGT-M workflows.

---

## 14. Other Species / Natural Disease

No naturally occurring JPH2-associated cardiomyopathy in companion animals or wildlife was identified in the literature surveyed (no OMIA hits found in this research pass). JPH2 orthologs are broadly conserved across vertebrates (mouse Jph2, NCBI Gene; part of the junctophilin gene family with evolutionary conservation documented in "Molecular evolution of the junctophilin gene family," PMC2685503), but disease association has only been established via engineered/induced models, not spontaneous natural disease.

---

## 15. Model Organisms

- **Genetically engineered mouse models:**
  - **Global JPH2 knockout mice:** Embryonic lethal, with loss of junctional membrane complexes and poorly developed T-tubules, establishing JPH2's essential developmental role (fidelity: high for demonstrating protein necessity, but the phenotype—embryonic lethality—does not model postnatal HCM).
  - **Cardiac-specific JPH2 knockdown/conditional knockout mice:** Impaired cardiac contractility, heart failure, increased mortality — models the general consequence of JPH2 loss of function on cardiac performance, informative for the recessive/LOF-associated DCM phenotype rather than CMH17 specifically.
  - **JPH2 E169K knock-in/expressing mice:** Recapitulate triggered activity and supraventricular (atrial) arrhythmia matching the human E169K phenotype, directly linking impaired JPH2–RyR2 binding to arrhythmogenesis (PMID:23973696).
  - **JPH2 mutant transgenic/knock-in mouse model (cited in ClinGen curation, likely G505S- or missense-variant based):** Shows "hypertrophic interventricular septum, increased LV mass, asymmetric LV hypertrophy" with histology confirming "cardiomyocyte hypertrophy and disarray consistent with HCM" — the most direct in vivo recapitulation of the CMH17 hypertrophic phenotype.
- **Cellular/in vitro models:**
  - **Patient-derived iPSC-cardiomyocytes with CRISPR/Cas9-corrected isogenic controls** (T161K) — the most granular functional model, recapitulating prolonged action potential duration, arrhythmogenic early afterdepolarizations, and slowed calcium-current inactivation kinetics characteristic of human CMH17 electrophysiology; explicitly validated by the authors as recapitulating "the cellular phenotype of HCM caused by a mutation in a non-sarcomeric gene."
  - **COS7 and H9c2 cell overexpression models** (S165F) — used to demonstrate autoinhibitory structural mechanism and resultant cellular hypertrophy.
  - **Primary mouse skeletal myotube overexpression** (S165F) — shows increased myotube diameter and resting cytosolic Ca²⁺, indicating the mechanism extends to skeletal muscle in overexpression systems (relevant to JPH2's dual cardiac/skeletal muscle isoform biology, though CMH17 itself is a cardiac-restricted phenotype).
- **Model limitations:** No model captures the full clinical spectrum (LVH + conduction disease + heart failure) simultaneously in a single validated system; iPSC-CM models capture cellular electrophysiology but not tissue-level hypertrophic remodeling or conduction-system anatomy; mouse knock-in/knockout models capture structural hypertrophy or arrhythmia individually but published data reviewed here did not identify one model demonstrating the complete co-occurring phenotype triad seen in Finnish T161K patients.

Sources: [PMID:23973696 (JACC 2013)](https://www.jacc.org/doi/10.1016/j.jacc.2013.06.052), [PMID:37371654 (Biomedicines 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10295168/), [PMID:41291214 (Commun Biol 2025)](https://www.nature.com/articles/s42003-025-09244-9), [ClinGen curation](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_378a727d-0c5b-4563-9c96-ac18a2902742-2017-07-18T160000.000Z), [Molecular evolution of junctophilin gene family, PMC2685503](https://pmc.ncbi.nlm.nih.gov/articles/PMC2685503/)

---

## Notes on Evidence Gaps and Curation Considerations

1. **Gene-disease validity is Moderate, not Definitive** (ClinGen, re-affirmed 2022) — curation of CMH17 should reflect appropriate epistemic caution; the panel explicitly notes "the mechanism for disease remains unknown" (i.e., not conclusively established beyond the calcium-handling hypothesis) and that "more evidence is needed to establish this association definitively."
2. **MONDO mapping is ambiguous** — no CMH17-specific MONDO term was confirmed in this research pass; verify against the live MONDO ontology/Monarch resolution before binding `disease_term`/`mappings.mondo_mappings` (likely `skos:narrowMatch` to MONDO:0005045 general familial HCM, pending confirmation).
3. **OMIM full-text access (omim.org direct fetch) was blocked by the environment's outbound proxy** during this research session; all OMIM content above is derived from search-result excerpts rather than a direct page fetch, and should be re-verified against the live OMIM entry (#613873) before use as a primary citation source in curation, per this repository's evidence-fetching policy (`just fetch-reference`).
4. **JPH2 displays a genotype-phenotype spectrum broader than CMH17 alone** (dominant missense → HCM/arrhythmia vs. recessive LOF → severe early DCM) — curators should ensure any dismech entry for CMH17 is scoped specifically to the dominant HCM phenotype and cross-references rather than conflates the distinct recessive JPH2-DCM entity, consistent with the "Digenic/Oligogenic" and general lump/split guidance in this repository's design decisions for genetically heterogeneous conditions.
5. Several full-text sources (ScienceDirect systematic review, Nature Communications Biology S165F paper, direct OMIM pages) could not be directly fetched in this session due to proxy/access restrictions; findings from these sources here are based on search-engine-summarized excerpts and should be independently re-verified with exact-quote snippets against the primary source (or its cached/PMC mirror) before being used as curated evidence in the knowledge base, per the `dismech-references` skill's exact-quote requirement.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004758` (1 mention) - the report calls it "Paroxysmal atrial fibrillation"; HP calls it **Effort-induced polymorphic ventricular tachycardia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0086013` (1 mention) - the report calls it "membrane repolarization in ventricular cardiac muscle cell"; GO calls it **membrane repolarization during cardiac muscle cell action potential**
- `GO:0007512` (1 mention) - the report calls it "adult heart development, for hypertrophic remodeling context"; GO calls it **adult heart development**
- `CL:0002129` (1 mention) - the report calls it "cardiac muscle myoblast"; CL calls it **regular atrial cardiac myocyte**, and lists "atrial cardiac muscle cell" among its other names
- `UBERON:0006566` (1 mention) - the report calls it "interventricular septum"; UBERON calls it **left ventricle myocardium**, and lists "left ventricular myocardium" among its other names
