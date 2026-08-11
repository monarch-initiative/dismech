---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-04T00:08:01.672424'
end_time: '2026-08-04T00:20:57.233762'
duration_seconds: 775.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chorioamnionitis
  mondo_id: ''
  category: Infectious
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 31
  num_turns: 50
  total_cost_usd: 4.597875
  session_id: 4c54264b-cb15-466f-8258-355abfb59881
  stop_reason: end_turn
citation_count: 60
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chorioamnionitis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Chorioamnionitis** covering all of the
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

# Chorioamnionitis — Comprehensive Disease Research Report

**Prepared:** 2026-08-04 · **Target:** dismech knowledge base entry (`kb/disorders/Chorioamnionitis.yaml`) · **Category:** Infectious

> **Read this first — snippet discipline.** Every quoted passage below is tagged `[VERBATIM]` (pulled from the PubMed abstract page and believed to be an exact substring) or `[PARAPHRASE]` (the fetch returned a summarizer's rewording — **do not** paste it into an `evidence.snippet:` field). Per the dismech SOP, run `just fetch-reference PMID:XXXXXXX` and `just validate-references` on every citation before committing. Every ontology ID in this report is a *candidate* and must survive `just validate-terms`; I've flagged confidence explicitly in §16.

---

## 1. Disease Information

### What it is

Chorioamnionitis is inflammation of the fetal membranes — the amnion and chorion — and, by extension, of the amniotic fluid, umbilical cord, decidua and sometimes the fetus itself. Think of the amniotic sac as a sealed fermentation vessel: it's supposed to be a closed, low-microbe compartment, and chorioamnionitis is what happens when something breaches the seal (or when the vessel's own tissue starts screaming without any invader at all). The condition sits at the intersection of infection, sterile inflammation, and the physiological inflammatory program of labor itself, which is exactly why its nomenclature has been fought over for a decade.

Three overlapping entities travel under the name, and conflating them is the single biggest curation trap here:

| Entity | Basis of diagnosis | Notes |
|---|---|---|
| **Clinical chorioamnionitis / intraamniotic infection (IAI)** | Maternal fever + supporting clinical signs, intrapartum | The bedside syndrome. Poorly specific for actual infection. |
| **Histologic (acute) chorioamnionitis** | Placental pathology — neutrophil infiltration of chorion/amnion | Frequently *silent*; the majority of cases are clinically undiagnosed. |
| **Intra-amniotic inflammation (microbial-associated vs. sterile)** | Amniotic fluid IL-6 / MMP-8 ± culture / PCR-ESI-MS | The mechanistic ground truth; requires amniocentesis. |

ACOG's definition: *"Intraamniotic infection, also known as chorioamnionitis, is an infection with resultant inflammation of any combination of the amniotic fluid, placenta, fetus, fetal membranes, or decidua."* `[VERBATIM]` — ACOG Committee Opinion No. 712, Obstet Gynecol 2017;130(2):e95-e101 (**PMID:28742677**).

### The "Triple I" reclassification (2015–2016)

In January 2015 an NICHD expert panel convened specifically because the word "chorioamnionitis" had become a semantic swamp:

> *"The panel noted that the term chorioamnionitis has been used to label a heterogeneous array of conditions characterized by infection and inflammation or both with a consequent great variation in clinical practice for mothers and their newborns. Therefore, the panel proposed to replace the term chorioamnionitis with a more general, descriptive term: 'intrauterine inflammation or infection or both,' abbreviated as 'Triple I.'... It is particularly important to recognize that an isolated maternal fever is not synonymous with chorioamnionitis."* `[VERBATIM]` — Higgins RD, Saade G, Polin RA, et al. Obstet Gynecol 2016;127(3):426-436 (**PMID:26855098**).

**Triple I diagnostic tiers (NICHD 2016):**
- **Isolated maternal fever** — oral temp ≥39.0 °C once, *or* 38.0–38.9 °C persisting on repeat at 30 min. No other findings.
- **Suspected Triple I** — fever *plus* ≥1 of: baseline fetal tachycardia (>160 bpm for ≥10 min); maternal WBC >15,000/mm³ without corticosteroids; definite purulent cervical discharge.
- **Confirmed Triple I** — suspected Triple I *plus* objective laboratory confirmation: positive amniotic fluid Gram stain, low AF glucose, positive AF culture, **or** placental pathology showing diagnostic infection/inflammation.

ACOG (CO 712, 2017) then softened this back toward practical bedside use: suspected IAI is diagnosed when *"the maternal temperature is greater than or equal to 39.0°C or when the maternal temperature is 38.0–38.9°C and one additional clinical risk factor is present."* `[VERBATIM]` (**PMID:28742677**). Note that ACOG deliberately kept the term "intraamniotic infection" rather than adopting "Triple I" — the two vocabularies coexist in current literature. Adoption of Triple I has been patchy, and dismech should probably curate the *entity* under the historical name with both definitional frameworks captured as `definitions[]` blocks.

### Identifiers

| System | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0000409** — "chorioamnionitis" | Confirmed against OLS4. Definition: *"a morphologic finding indicating inflammation of the fetal sac membranes"*. **Use this as `disease_term`.** Per your `new-mondo-term-ols-cache-miss` memory, seed both `DiseaseTerm` and `DiseaseOrSubtypeTerm` enum caches. |
| **ICD-10-CM** | **O41.12-** "Chorioamnionitis" | Non-billable at 5 characters; trimester-specific children O41.121x / .122x / .123x / .129x, plus fetus-identifier 7th characters. Neonatal-side code: **P02.7** ("Newborn affected by chorioamnionitis"). |
| **ICD-11** | JA85.1 / JA85 (Infection of amniotic sac and membranes) | Verify against the WHO ICD-11 browser before curating. |
| **MeSH** | **D002821** "Chorioamnionitis" | MeSH scope note: inflammation of chorion and amnion with connected tissues including fetal vessels and umbilical cord, often from ascending intrauterine infection. |
| **SNOMED CT** | 11612004 "Chorioamnionitis" | Verify; SNOMED is guide-only per dismech policy. |
| **OMIM** | *None* — not a Mendelian disorder | |
| **Orphanet** | *None* — not a rare disease | Do **not** attempt an `ORPHA:` reference here. |
| **DOID** | DOID:13892 (chorioamnionitis) | Cross-referenced by MONDO. |

### Synonyms / alternative names

Amnionitis · intraamniotic infection (IAI) · intra-amniotic infection · intrauterine infection · amniotic infection syndrome · "Triple I" (intrauterine inflammation or infection or both) · acute chorioamnionitis (histologic) · membranitis · placental acute inflammation · ascending intrauterine infection. Related-but-distinct terms that should **not** be merged: *funisitis* (umbilical cord inflammation — a fetal response), *chorionic vasculitis*, *deciduitis*, *villitis of unknown etiology* (chronic, non-infectious, different lesion class), *chronic chorioamnionitis* (a distinct lymphocytic lesion of late preterm birth).

### Data provenance

Both individual-patient and aggregate. Clinical chorioamnionitis is a routine EHR/administrative diagnosis (ICD-10 O41.12-, present in birth certificate data and in large claims/registry sets like NIS, Kaiser, Consortium on Safe Labor), which makes it a good candidate for a computable phenotype `definitions[]` block. The mechanistic literature, by contrast, is dominated by a small number of amniocentesis-based cohorts (chiefly the NICHD Perinatology Research Branch, Wayne State/Detroit and Seoul National University), which are individual-patient but highly selected. Placental pathology data come from institutional pathology series standardized (since 2016) by the Amsterdam consensus.

---

## 2. Etiology

### 2.1 Primary causal factors

Chorioamnionitis is **not a genetic disease**. It is an acquired, largely infectious/inflammatory condition with four recognized causal routes and one large sterile category.

**Route 1 — Ascending infection from the lower genital tract (dominant, ~majority of preterm cases).** Organisms move cervix → choriodecidual space → chorion/amnion → amniotic fluid → fetus. Romero's canonical staging:

- **Stage I** — alteration of vaginal/cervical flora, or pathogenic organisms in the cervix (bacterial vaginosis is the archetype).
- **Stage II** — organisms cross into the choriodecidual space and reside in the lower uterine pole between membranes and chorion (**deciduitis / choriodeciduitis**).
- **Stage III** — organisms breach the amnion into the amniotic cavity (**amnionitis / intra-amniotic infection**); may involve chorionic plate vessels (**choriovasculitis**).
- **Stage IV** — fetal involvement: aspiration/swallowing of infected fluid → congenital pneumonia, otitis, conjunctivitis; hematogenous spread → fetal bacteremia and sepsis.

Histologic progression follows the same order — chorio-deciduitis is the early stage, chorio-deciduo-amnionitis the advanced stage of ascending intrauterine infection (**PMID:26574743**).

**Route 2 — Hematogenous / transplacental.** Rare but important. *Listeria monocytogenes* is the archetype; recent molecular work supports hematogenous dissemination on the basis of *"acute intervillositis and the detection of L. monocytogenes in the amniotic fluid and intervillous space of the placenta combined with the absence of this organism in the vagina"* `[PARAPHRASE — reverify]` (**PMID:40643048**). Also *Treponema pallidum*, *Mycobacterium tuberculosis*, *Brucella*, *Coxiella burnetii*, and some viruses.

**Route 3 — Iatrogenic / retrograde.** Amniocentesis, chorionic villus sampling, fetoscopy, cerclage placement, intrauterine transfusion, retained IUD, amnioinfusion, internal fetal/uterine monitoring. Retrograde spread from the fallopian tubes into the peritoneal cavity is a fourth theoretical route (rarely documented).

**Route 4 — Sterile intra-amniotic inflammation (no organism at all).** This is the plot twist of the last fifteen years and it must be represented in the pathograph. In preterm labor with intact membranes:

> *"(i) The frequency of sterile intra-amniotic inflammation was significantly greater than that of microbial-associated intra-amniotic inflammation [26% (35/135) versus 11% (15/135); (P = 0.005)], (ii) patients with sterile intra-amniotic inflammation delivered at comparable gestational ages had similar rates of acute placental inflammation and adverse neonatal outcomes as patients with microbial-associated intra-amniotic inflammation, and (iii) patients with sterile intra-amniotic inflammation and high AF concentrations of HMGB1 (≥8.55 ng/mL) delivered earlier than those with low AF concentrations of HMGB1 (P = 0.02)."* `[VERBATIM]` — Romero R, Miranda J, Chaiworapongsa T, et al. Am J Reprod Immunol 2014;72(5):458-74 (**PMID:25078709**).

**Route 5 (term-specific) — epidural-associated systemic maternal inflammation.** At term, "clinical chorioamnionitis" is frequently neither infection nor even intra-amniotic: *"Clinical chorioamnionitis is a syndrome caused by intraamniotic infection, sterile intraamniotic inflammation (inflammation without bacteria), or systemic maternal inflammation induced by epidural analgesia."* `[PARAPHRASE — reverify]` — Jung E, Romero R, et al. Am J Obstet Gynecol 2024;230(3S):S807-S840 (**PMID:38233317**). Epidural-related fever is associated with elevated serum IL-6 and IL-8 and is essentially never microbial (**PMID:21343762**); one term series found grade 1–2 histologic chorioamnionitis in 34% of placentas with actual infection in only 4%.

### 2.2 Microbiology (see also §5.3)

Amniotic fluid isolates in preterm labor, in rough order of frequency: **genital mycoplasmas** — *Ureaplasma urealyticum* / *Ureaplasma parvum* (the single most common), *Mycoplasma hominis*; **anaerobes** — *Fusobacterium nucleatum*, *Sneathia (Leptotrichia) sanguinegens*, *Bacteroides* spp., *Peptostreptococcus*; **facultative organisms** — *Gardnerella vaginalis*, *Streptococcus agalactiae* (GBS), *Escherichia coli*, *Enterococcus*, *Streptococcus anginosus* group; **fungi** — *Candida albicans* (strongly associated with cerclage and retained IUD). Infection is **usually polymicrobial**.

Molecular methods substantially outperform culture: 16S rRNA sequencing detects uncultivable organisms including *Sneathia*, *Leptotrichia*, *Bergeyella*, *Clostridiales*, and oral-origin taxa (**PMID:19144804**, J Clin Microbiol 2008). *Fusobacterium nucleatum* is a periodontal organism, supporting the oral-hematogenous seeding hypothesis for a subset of cases.

### 2.3 Risk factors

**Obstetric / mechanical (strongest, and mostly modifiable-ish):**

| Risk factor | Direction/effect |
|---|---|
| Prolonged rupture of membranes (>18–24 h) | Chorioamnionitis in ~40% of PROM persisting >24 h |
| Prolonged labor, especially prolonged second stage | Strong, dose-dependent |
| Multiple digital vaginal examinations (esp. after ROM) | Dose-dependent |
| Nulliparity | Consistent |
| Internal fetal/uterine monitoring | Consistent |
| Meconium-stained amniotic fluid | Consistent (and bidirectional — inflammation → meconium passage) |
| Epidural analgesia | Strongly associated with *fever*, weakly/not with true infection |
| Labor induction / augmentation, amnioinfusion, cerclage | Moderate |

**Microbiological/colonization:** GBS colonization, bacterial vaginosis, *Trichomonas vaginalis*, *Neisseria gonorrhoeae*, *Chlamydia trachomatis*, cervical insufficiency with exposed membranes, short cervix, prior preterm birth, periodontal disease.

**Host/demographic:** young maternal age; nulliparity; obesity (high BMI); smoking; alcohol; immunocompromise (HIV — histologic acute chorioamnionitis prevalence studied in Ugandan HIV+ cohorts, **PMC6459589**); anemia; low socioeconomic status; African-American ancestry (confounded by access and by BV prevalence); prior clinical chorioamnionitis (population-based recurrence risk documented in Washington State 1989–2008, **PMC3587161**).

**Gestational age is the single most powerful "risk factor" for the histologic lesion.** Histologic acute chorioamnionitis prevalence is *"3-5% at term, increasing to 94% at 21-24 weeks"* `[PARAPHRASE — reverify]` — Kim CJ, Romero R, et al. Am J Obstet Gynecol 2015;213(4 Suppl):S29-52 (**PMID:26428501**). This inverse relationship is the most important epidemiological fact about the disease.

### 2.4 Protective factors

- **Intrapartum antibiotic prophylaxis for GBS** — reduces early-onset GBS disease >80% (1.8 → 0.23 per 1,000 live births) but is a neonatal-outcome intervention more than a chorioamnionitis-prevention one.
- **Latency antibiotics in PPROM** (ampicillin+erythromycin, "Mercer protocol") — prolong latency and reduce chorioamnionitis incidence (**Mercer et al., JAMA 1997**; ORACLE I, Lancet 2001).
- **Limiting digital cervical examinations** after ROM; sterile speculum preference.
- **Vaginal cleansing with povidone-iodine or chlorhexidine before cesarean** — reduces postoperative endometritis (Cochrane).
- **Azithromycin-based extended-spectrum prophylaxis at unscheduled cesarean** (C/SOAP trial, Tita et al., N Engl J Med 2016) — reduces post-cesarean infection.
- **Treatment of bacterial vaginosis** — protective in high-risk women in some but *not* all trials; screening/treating unselected low-risk women has not reproducibly reduced preterm birth. Curate this as equivocal.
- **Genetic protective alleles:** none established. Some cytokine-promoter "low-producer" genotypes (e.g., IL-6 −174 GG, TNF −308 GG) have been reported as lower-risk in individual studies, but these are inconsistent and should be curated as `PARTIAL` or omitted.

### 2.5 Gene–environment interaction

The best-characterized GxE signal in this space is TNF genotype × bacterial vaginosis:

> Maternal carriers of the TNF-2 allele (TNF −308A) had increased risk of spontaneous preterm birth (OR 2.7, 95% CI 1.7–4.5); *"The association between TNF-2 and preterm birth was modified by bacterial vaginosis, with those having a susceptible genotype and bacterial vaginosis showing increased odds of preterm birth compared with those who did not (OR 6.1, 95% CI 1.9-21.0)"* `[PARAPHRASE — reverify]` — Macones GA, et al. Am J Obstet Gynecol 2004 (**PMID:15284722**).

This is a genuinely useful dismech pattern: **environmental exposure (BV) × host inflammatory genotype → amplified inflammatory response → preterm birth**. Caveat it heavily — a subsequent meta-analysis found *no* statistically significant association between TNF −308G>A and preterm birth overall, and later work (**PMID:15507966**) implicated TNF −863 rather than −308. Curate as an EMERGING/contested hypothesis with an explicit `KNOWLEDGE_GAP` discussion, not as settled mechanism.

---

## 3. Phenotypes

### 3.1 Maternal clinical phenotypes (intrapartum)

| Phenotype | Category | Frequency | Candidate HPO |
|---|---|---|---|
| **Maternal fever** (≥39.0 °C once, or 38.0–38.9 °C sustained) | Clinical sign | Obligate for clinical dx (~100% by definition) | HP:0001945 Fever |
| **Maternal tachycardia** (>100 bpm) | Clinical sign | Frequent (~50–80%) | HP:0001649 Tachycardia |
| **Fetal tachycardia** (baseline >160 bpm ≥10 min) | Clinical sign | Frequent (~40–70%) | *Verify — "Fetal tachycardia" term needed* |
| **Uterine fundal tenderness** | Symptom/sign | Occasional (~4–25%) | *No good HPO term* |
| **Purulent or malodorous amniotic fluid / cervical discharge** | Clinical sign | Occasional (~5–22%) | *Verify vaginal-discharge term* |
| **Maternal leukocytosis** (WBC >15,000/mm³) | Lab abnormality | Frequent (~70–90%) | HP:0001974 Leukocytosis |
| **Elevated CRP** | Lab abnormality | Frequent | HP:0011227 Elevated circulating C-reactive protein concentration |
| **Reduced uterine contractility / dysfunctional labor** | Physical manifestation | Frequent | *No clean HPO term — model as pathophysiology node* |
| **Maternal sepsis** (rare, severe) | Clinical | Rare (<1%) | HP:0100806 Sepsis |

Note that the classic "malodorous fluid + uterine tenderness" triad is a *late and insensitive* finding; most cases present as fever plus tachycardia in a laboring nullipara with an epidural.

### 3.2 Fetal / neonatal phenotypes

| Phenotype | Category | Frequency | Candidate HPO |
|---|---|---|---|
| Preterm birth | Clinical | ~40–70% of preterm births have intrauterine infection/inflammation | HP:0001622 Premature birth |
| Premature rupture of membranes / PPROM | Clinical | Very frequent as both cause and consequence | **HP:0001788** Premature rupture of membranes |
| Early-onset neonatal sepsis | Clinical | ~1–4% of exposed term newborns; higher preterm | HP:0100806 Sepsis (+ neonatal onset qualifier) |
| Congenital/neonatal pneumonia | Clinical | Occasional | *Verify pneumonia term* |
| Neonatal respiratory distress | Clinical | Frequent in preterm | HP:0002098 Respiratory distress |
| Bronchopulmonary dysplasia | Clinical | Increased odds; effect modified by postnatal exposures | *Verify — HPO BPD term* |
| Necrotizing enterocolitis | Clinical | Increased odds | *Verify* |
| Intraventricular hemorrhage | Clinical | Increased odds | *Verify* |
| Cystic periventricular leukomalacia | Radiologic/pathologic | RR 3.0 (clinical CA), RR 2.1 (histologic CA) | *Verify PVL term* |
| Cerebral palsy | Clinical, long-term | RR 1.9 preterm (clinical CA); RR 4.7 term | HP:0100021 Cerebral palsy (verify) |
| Retinopathy of prematurity | Clinical | Increased odds | *Verify* |
| Patent ductus arteriosus | Clinical | Increased odds (meta-analysis, PMC4574167) | HP:0001643 Patent ductus arteriosus |
| Elevated cord-blood IL-6 (>11 pg/mL) — FIRS | Lab abnormality | Defines FIRS type I | *Model as `biochemical`, not phenotype* |
| Fetal/neonatal death, stillbirth | Clinical | Rare-to-occasional | HP:0001622-adjacent; use `Stillbirth` term |

### 3.3 Characteristics

- **Onset:** exclusively **gestational/perinatal**. Maternal phenotype is intrapartum or, in preterm cases, antepartum. Neonatal phenotypes are congenital-to-neonatal onset, with a long-term neurodevelopmental tail into childhood.
- **Severity:** variable and gestational-age-dependent. *"Chorioamnionitis was severe in 74% of preterm but in only 15% of term deliveries."*
- **Progression:** **acute and episodic-to-progressive**. Untreated intra-amniotic infection progresses over hours-to-days; the histologic lesion progresses through defined stages. Once delivery occurs the maternal disease is self-limited; the fetal sequelae are *not* — FIRS-associated brain and lung injury is progressive over months to years.
- **Duration:** maternal — self-limited (resolves within days of delivery and antibiotics). Neonatal — potentially lifelong (cerebral palsy, chronic lung disease).
- **Quality of life:** maternal QoL impact is short-term but real (fever, pain, higher cesarean rate, postpartum hemorrhage, longer stay, breastfeeding disruption, NICU separation). Offspring QoL impact is where the burden actually lives — CP and severe neurodevelopmental disability carry lifelong disability weights (GBD). No chorioamnionitis-specific EQ-5D/SF-36 literature exists; use CP- and prematurity-specific instruments (e.g., PedsQL Cerebral Palsy Module, GMFCS-stratified utilities) as proxies and label the linkage as inferential.

---

## 4. Genetic / Molecular Information

**Bottom line: there are no causal genes.** Chorioamnionitis is not Mendelian, has no OMIM entry, no pathogenic variants, no ClinVar submissions as a monogenic condition, no chromosomal abnormalities, and no genetic testing indication. Anything a deep-research tool tells you about "causal genes for chorioamnionitis" is a hallucination or a Named Entity Confusion event — apply the `just preflight-dr` logic mentally: MONDO:0000409 records **no** `RO:0004003` causal gene, so a DR preflight would return `SKIP`, and the manual checks apply.

What *does* exist is a modest, largely non-replicated **susceptibility-variant** literature. Curate these with `relationship_type: SUSCEPTIBILITY` and `inheritance_term: HP:0010982` (polygenic) **only** if you can quote a real abstract; otherwise leave the `genetic:` block empty.

| Gene | HGNC | Variant | Reported association | Evidence quality |
|---|---|---|---|---|
| **TNF** | hgnc:11892 | −308 G>A (TNF-2, rs1800629) | SPTB OR 2.7; BV interaction OR 6.1 (**PMID:15284722**) | Contested — null meta-analyses |
| **TNF** | hgnc:11892 | −863 C>A (rs1800630) | Adverse outcomes after preterm labor (**PMID:15507966**) | Single study |
| **IL6** | hgnc:6018 | −174 G>C (rs1800795) | Preterm birth / histologic chorioamnionitis | Inconsistent |
| **IL1RN** | hgnc:6000 | VNTR allele 2 | Preterm birth, intra-amniotic inflammation | Inconsistent |
| **TLR4** | hgnc:11850 | Asp299Gly (rs4986790) | Reduced LPS responsiveness; altered risk | Inconsistent |
| **IL10** | hgnc:5962 | −1082, −819, −592 haplotypes | Histologic chorioamnionitis (Caucasoid case-control, **PMC554771**) | Single study |
| **MBL2** | hgnc:6922 | Low-producing haplotypes | Increased infection susceptibility | Weak |
| **SERPINH1, COL4A3, MMP9, MMP1** | — | Promoter variants | PPROM susceptibility, some ancestry-specific | Weak |

A useful HuGE review of preterm-birth genetics exists (*Genetic variation associated with preterm birth: A HuGE review*, Genet Med) — treat it as the umbrella citation for "many candidate genes, little replication."

**Epigenetics.** Emerging and thin. Reported: differential placental DNA methylation in histologic chorioamnionitis; cord-blood methylation signatures of intrauterine inflammation; histone-modification-mediated priming of the fetal innate immune compartment (trained immunity) after in-utero LPS/Ureaplasma exposure in animal models. No validated epigenetic biomarker exists. Curate as `KNOWLEDGE_GAP`.

**Chromosomal abnormalities:** none. **Somatic variation:** not applicable. **Modifier genes:** not established.

---

## 5. Environmental Information

### 5.1 Environmental / exposure factors
- **Iatrogenic instrumentation** — the dominant "environmental" exposure: digital cervical exams, internal monitors, amniocentesis, cerclage, IUD retention, amnioinfusion.
- **Air pollution / particulate matter** — associated with preterm birth generally; a direct chorioamnionitis link is not established.
- **Occupational exposures** — no established specific link.
- **Heat exposure / ambient temperature** — confounds fever-based diagnosis; no causal link.

### 5.2 Lifestyle factors
Cigarette smoking (↑ risk, and ↑ PPROM); alcohol use (↑ risk, listed among StatPearls risk factors); illicit drug use; obesity/high BMI; poor periodontal health (periodontitis → oral organisms in amniotic fluid, notably *F. nucleatum*); nutritional deficiency; sexual activity and vaginal douching (via microbiome disruption); short interpregnancy interval.

### 5.3 Infectious agents (with NCBI Taxonomy IDs)

| Organism | NCBITaxon | Role |
|---|---|---|
| *Ureaplasma parvum* | NCBITaxon:134821 | Most common single isolate; low-grade chronic inflammation |
| *Ureaplasma urealyticum* | NCBITaxon:2130 | Robust host response despite "low virulence" reputation |
| *Mycoplasma hominis* | NCBITaxon:2098 | Frequent co-isolate |
| *Streptococcus agalactiae* (GBS) | NCBITaxon:1311 | Major cause of early-onset neonatal sepsis |
| *Escherichia coli* | NCBITaxon:562 | Major cause of EOS in preterm |
| *Fusobacterium nucleatum* | NCBITaxon:851 | Oral-origin; hematogenous seeding; causes stillbirth in mice |
| *Gardnerella vaginalis* | NCBITaxon:2702 | BV-associated |
| *Sneathia sanguinegens* | NCBITaxon:40543 | Uncultivable; 16S-detected |
| *Bacteroides* spp. | NCBITaxon:816 | Anaerobic |
| *Candida albicans* | NCBITaxon:5476 | Cerclage/IUD-associated; severe outcomes |
| *Listeria monocytogenes* | NCBITaxon:1639 | Hematogenous route |
| *Trichomonas vaginalis* | NCBITaxon:5722 | Risk factor via BV-like dysbiosis |

On *Ureaplasma* specifically — the "commensal" framing is wrong:

> *"Patients with preterm premature rupture of membranes and microbial invasion of the amniotic cavity with U urealyticum are associated with a robust host inflammatory response in the fetal, amniotic, and maternal compartments."* `[VERBATIM]` — Yoon BH, Romero R, et al. Am J Obstet Gynecol 1998;179(5):1254-60 (**PMID:9822511**). In that series, histologic chorioamnionitis was present in **100% (22/22)** of *U. urealyticum*-positive cases vs **42% (30/72)** of culture-negative cases.

---

## 6. Mechanism / Pathophysiology

Here's the causal chain, told as one continuous story, then decomposed into pathograph nodes.

### 6.1 Narrative causal chain

A shift in the vaginal microbiome (loss of *Lactobacillus* dominance, rise of BV-associated anaerobes) removes the chemical fence at the cervix. Organisms — or, in the sterile route, host debris and stress signals from stretched, aging membranes — reach the choriodecidual interface. There, pattern-recognition receptors on decidual stromal cells, chorionic trophoblast, amnion epithelium, and resident macrophages read the signal: **TLR4** for Gram-negative LPS, **TLR2/TLR6** for lipoproteins and mycoplasmal lipoproteins, **TLR9** for bacterial CpG DNA, and **RAGE/TLR4** for the alarmin HMGB1 in the sterile arm. Both microbial PAMPs and sterile DAMPs converge on the *same* receptor plumbing — which is exactly why sterile and microbial intra-amniotic inflammation produce indistinguishable placental pathology and comparably bad neonatal outcomes.

Receptor engagement activates **MyD88 → IRAK → TRAF6 → IKK → NF-κB** and, in parallel, the **MAPK** cascades. NF-κB drives transcription of IL-1β, IL-6, IL-8/CXCL8, TNF-α, CCL2, and the NLRP3 inflammasome components. Assembled **NLRP3 inflammasome → caspase-1 → mature IL-1β and IL-18**, plus gasdermin-D-mediated pyroptosis of amnion and decidual cells — this is the amplification step that turns a signal into a syndrome.

Three downstream output arms then run in parallel:

1. **Chemotaxis arm.** CXCL8/IL-8 and CXCL1/2 establish a gradient into the amniotic cavity. Maternal neutrophils exit decidual venules and march through chorion into amnion (the **maternal inflammatory response, MIR**). Later, *fetal* neutrophils cross chorionic-plate vessel walls and umbilical vessels into Wharton's jelly (the **fetal inflammatory response, FIR** = chorionic vasculitis + funisitis). This directional two-source neutrophil traffic *is* histologic chorioamnionitis.
2. **Uterotonic arm.** IL-1β and TNF-α upregulate **PTGS2/COX-2** and phospholipase A2, releasing arachidonic acid and generating **prostaglandins E2 and F2α**, while downregulating **HPGD** (15-hydroxyprostaglandin dehydrogenase), the enzyme that normally destroys them. Prostaglandins plus increased **GJA1/connexin-43** and oxytocin-receptor expression convert the quiescent myometrium into a contractile syncytium → **preterm labor**.
3. **Tissue-destruction arm.** Neutrophil and amnion-derived **MMP-8** (neutrophil collagenase) and **MMP-9** (gelatinase B), plus elastase, degrade the amniochorionic collagen scaffold; TIMPs fall; the membranes lose tensile strength → **PPROM**. The same proteases plus IL-8-driven neutrophil influx into the cervical stroma cause collagen remodeling → **cervical ripening**.

Meanwhile, the fetus mounts its own systemic response. Fetal plasma IL-6 rises, defining **FIRS**:

> *"A systemic fetal inflammatory response, as determined by an elevated fetal plasma interleukin-6 value, is an independent risk factor for the occurrence of severe neonatal morbidity."* `[VERBATIM — conclusion sentence]` — Gomez R, Romero R, Ghezzi F, Yoon BH, Mazor M, Berry SM. Am J Obstet Gynecol 1998;179(1):194-202 (**PMID:9704787**).

FIRS is multi-organ. In the **lung**, aspirated infected fluid plus cytokines cause fetal pneumonitis and paradoxical "inflammatory lung maturation" (surfactant up, alveolarization and microvascular development down) → the arrested-development phenotype of BPD. In the **brain**, circulating IL-1β/IL-6/TNF-α plus systemic hypotension activate microglia; pre-oligodendrocytes — exquisitely vulnerable at 23–32 weeks — die by oxidative and excitotoxic injury; myelination fails → **periventricular leukomalacia** and later **cerebral palsy**. In the **gut**, inflammatory priming plus impaired mesenteric perfusion predisposes to **NEC**. In the **eye**, altered IGF-1/VEGF signaling contributes to **ROP**. In the **heart/vasculature**, cytokines impair ductal closure → **PDA**. The thymus involutes.

There are two immunologically distinct flavors of FIRS:

> FIRS **Type I** shows *"upregulation of host immune responses, including neutrophil and monocyte functions, together with a proinflammatory cytokine storm"*; FIRS **Type II** shows *"a mild chronic inflammatory response involving perturbation of HLA transcripts, suggestive of fetal semiallograft rejection."* `[PARAPHRASE — reverify]` — Para R, Romero R, Miller D, et al. ImmunoHorizons 2021;5(9):735-751 (**PMID:34521696**). Type I is defined by cord IL-6 >11 pg/mL + acute funisitis; Type II by cord CXCL10 >82.34 pg/mL + chronic placental inflammation + cord IL-6 <11 pg/mL. **Only Type I belongs on this entry**; Type II belongs with chronic chorioamnionitis / villitis of unknown etiology.

### 6.2 Suggested pathograph nodes

| Node | `biological_scale` | Key content |
|---|---|---|
| Vaginal Microbiome Dysbiosis and Cervical Barrier Breach | ORGANISM | BV, loss of *Lactobacillus*; trigger node |
| Ascending Microbial Invasion of the Choriodecidual Space | TISSUE | Stage II; deciduitis |
| Pattern Recognition Receptor Activation (TLR4/TLR2) | MOLECULAR | GO:0002224; PAMP and DAMP convergence |
| Alarmin Release and Sterile Inflammatory Signaling | MOLECULAR | HMGB1/RAGE; the sterile arm |
| NF-κB-Driven Proinflammatory Cytokine Production | CELLULAR | IL-1β, IL-6, TNF-α, CXCL8 |
| NLRP3 Inflammasome Activation and Pyroptosis | CELLULAR | Caspase-1, mature IL-1β, GSDMD |
| Chemokine Gradient Formation and Neutrophil Chemotaxis | CELLULAR | GO:0030593 |
| Maternal Inflammatory Response (Acute Chorioamnionitis) | TISSUE | Maternal neutrophils in chorion/amnion |
| Fetal Inflammatory Response (Funisitis / Chorionic Vasculitis) | TISSUE | Fetal neutrophils in cord/chorionic vessels |
| Prostaglandin Synthesis and Myometrial Activation | MOLECULAR | PTGS2 ↑, HPGD ↓, GJA1 ↑ |
| MMP-Mediated Extracellular Matrix Degradation | MOLECULAR | MMP-8/MMP-9; TIMP ↓ |
| Membrane Weakening and Preterm Prelabor Rupture | TISSUE | PPROM |
| Preterm Labor and Birth | ORGANISM | |
| Fetal Inflammatory Response Syndrome (FIRS Type I) | ORGANISM | Cord IL-6 >11 pg/mL |
| Fetal Pulmonary Inflammation and Arrested Alveolarization | TISSUE | → BPD |
| Microglial Activation and Pre-Oligodendrocyte Injury | CELLULAR | → PVL, CP |
| Reduced Myometrial Contractility (Maternal, Term) | TISSUE | → dysfunctional labor, atony, PPH |
| Early-Onset Neonatal Sepsis | ORGANISM | |

Note the elegant/annoying duality worth flagging as a `mechanistic_hypotheses` pair: the same inflammatory mediator load that *drives* preterm labor also *impairs* term myometrial contractility (→ cesarean and postpartum hemorrhage). Curate as two hypothesis groups (`preterm_uterotonic_activation` vs `term_myometrial_suppression`) rather than as a single contradictory edge — the mechanisms differ by gestational age and receptor context (**PMID:29848185**).

### 6.3 Molecular profiling

- **Transcriptomics / single-cell.** The reference resource is the human placenta single-cell atlas of parturition: *"Cell types most affected by labor were fetal stromal and maternal decidual cells in the chorioamniotic membranes (CAMs) and maternal and fetal myeloid cells in the placenta. Cell-cell interaction analyses showed that CAM and placental cell types participated in labor-driven maternal and fetal signaling, including the collagen, C-X-C motif ligand (CXCL), tumor necrosis factor (TNF), galectin, and interleukin-6 (IL-6) pathways."* `[VERBATIM]` — Garcia-Flores V, Romero R, Tarca AL, et al. Sci Transl Med 2024;16(729):eadh8335 (**PMID:38198568**). Companion resources: single-cell atlas of murine reproductive tissues during preterm labor (Cell Rep 2022); single-cell transcriptional signatures of the human placenta in term and preterm parturition (eLife 2019, Pique-Regi et al.).
- **Proteomics.** Amniotic fluid proteomic "MR score" (Buhimschi/Weiner) — a 4-biomarker SELDI-TOF fingerprint (defensin-2, defensin-1, S100A12, S100A8) predicting intra-amniotic inflammation and neonatal sepsis (**PLOS Med 2007, 4(1):e18**).
- **Metabolomics.** Amniotic fluid glucose depletion is the oldest metabolic signature (mean 5 ± 2.4 mg/dL in IAI vs 39.8 ± 18.4 mg/dL without). Elevated AF lactate and altered LDH isoform mapping also reported. NMR/MS metabolomic signatures of intra-amniotic infection exist but are not clinically deployed.
- **Lipidomics.** Prostaglandin and platelet-activating-factor species elevated in amniotic fluid; lysophosphatidylcholine and oxidized-lipid signatures reported. Thin literature.
- **Functional genomics.** No CRISPR/RNAi screens specific to chorioamnionitis. TLR4-antagonist pharmacological "screens" in NHP/rodent stand in for this (**PMC2774271**).

---

## 7. Anatomical Structures Affected

**Primary (maternal-fetal interface):**
- Chorion — **UBERON:0003124** *(verify)*
- Amnion — **UBERON:0000305** *(verify)*
- Chorioamniotic (extraembryonic/fetal) membranes — verify best UBERON parent, possibly UBERON:0000478 extraembryonic structure
- Decidua — **UBERON:0002450** *(verify)*
- Placenta — **UBERON:0001987** *(verify)*
- Amniotic fluid — **UBERON:0000173** *(verify)*
- Umbilical cord (incl. Wharton's jelly) — **UBERON:0002331** *(verify)*
- Uterus / myometrium — **UBERON:0000995 / UBERON:0001296** *(verify)*
- Uterine cervix — **UBERON:0000002** *(verify)*
- Vagina — **UBERON:0000996** *(verify)*

**Secondary (fetal/neonatal end-organ):** lung (UBERON:0002048), brain — specifically periventricular white matter and germinal matrix (UBERON:0002316 white matter, verify), intestine (UBERON:0000160), eye/retina (UBERON:0000970 / UBERON:0000966), heart/ductus arteriosus (UBERON:0001496 verify), thymus (UBERON:0002370).

**Body systems:** reproductive, immune, respiratory, nervous, digestive, cardiovascular.

**Tissue types:** amniotic squamous/cuboidal **epithelium**; chorionic **trophoblast**; decidual and chorionic **connective/stromal tissue**; myometrial **smooth muscle**; umbilical vascular **endothelium and smooth muscle**; Wharton's jelly (specialized mucous connective tissue).

**Cell populations (Cell Ontology candidates):**
- neutrophil — **CL:0000775** (the defining cell of the lesion)
- macrophage — **CL:0000235**; Hofbauer cell (fetal placental macrophage) — verify
- decidual stromal cell — verify CL term
- trophoblast cell — **CL:0000351**
- amnion epithelial cell — verify
- fibroblast / stromal cell — **CL:0000057 / CL:0000499**
- T cell — **CL:0000084**; regulatory T cell — **CL:0000815** (depleted/skewed by *Ureaplasma*)
- natural killer cell — **CL:0000623** (decidual NK)
- endothelial cell of umbilical vein — verify (HUVEC-adjacent)
- microglial cell — **CL:0000129** *(verify)* — fetal brain injury arm
- oligodendrocyte precursor / pre-oligodendrocyte — verify — the vulnerable target in PVL
- uterine smooth muscle cell — **CL:0002601** *(verify)*

**Subcellular (GO Cellular Component):** NLRP3 inflammasome complex (**GO:0072559**, verify); plasma membrane TLR complexes; endosome (TLR9 signaling); nucleus (NF-κB translocation); extracellular region/matrix (**GO:0031012**); neutrophil azurophil/specific granules (verify); mitochondrion (ROS, mtDNA release as a DAMP).

**Localization / lateralization:** the ascending lesion is characteristically **most severe at the lower uterine pole / membrane rupture site** and around the cervical os, tapering toward the placental disc — this gradient is itself diagnostic of the ascending route. Not lateralized in the left/right sense. Funisitis affects the umbilical **vein first** (phlebitis), then arteries (arteritis), which is a stageable temporal marker.

---

## 8. Temporal Development

**Onset.** Congenital/gestational by definition. Antepartum in the PPROM/preterm-labor route; intrapartum in the term route. Onset pattern is **acute to subacute** (hours to days), though a low-grade *Ureaplasma* colonization can smolder for **weeks** — the "very chronic ureaplasma colonization" of the fetal sheep model.

**Stages.** Use the two complementary staging systems:

*Romero clinical/microbiological staging (ascending route)* — Stage I cervicovaginal dysbiosis → Stage II choriodeciduitis → Stage III intra-amniotic infection (amnionitis, choriovasculitis) → Stage IV fetal infection.

*Amsterdam consensus histologic staging (Khong TY, Mooney EE, Ariel I, et al., Arch Pathol Lab Med 2016;140(7):698-713, **PMID:27223167**)* — two axes:

- **Maternal inflammatory response (MIR):** Stage 1 acute subchorionitis/chorionitis; Stage 2 acute chorioamnionitis (neutrophils in the amnion/chorionic connective tissue); Stage 3 necrotizing chorioamnionitis (amniocyte necrosis, karyorrhexis, basement-membrane thickening). Grade 1 = not severe; Grade 2 = severe (confluent inflammation or subchorionic microabscesses).
- **Fetal inflammatory response (FIR):** Stage 1 chorionic vasculitis or umbilical phlebitis; Stage 2 umbilical arteritis (involvement of ≥1 umbilical artery); Stage 3 necrotizing funisitis. Grade 1/2 by severity, Grade 2 requiring near-confluent intramural neutrophils with attenuation of vascular smooth muscle.

Amsterdam recognizes *"only stages 2–3 to represent a fully developed histological chorioamnionitis, with stage 1 being a sensitive but less specific indicator"* — an important curation nuance, since much of the older literature counts Stage 1 as positive and therefore reports inflated prevalences.

**Progression rate.** Rapid once intra-amniotic invasion occurs. Untreated, the interval from intra-amniotic infection to delivery is typically short (days); severity of neonatal outcome tracks both organism and duration of exposure. Progression from chorio-deciduitis to chorio-deciduo-amnionitis is measurable in days (**PMID:26574743**).

**Course.** Maternal: **acute, self-limited**, resolving with delivery + antibiotics. Fetal/neonatal: acute illness followed by either recovery or a **progressive/static-disability** course (BPD improving over years; CP static but with evolving functional consequences).

**Remission.** Maternal remission is treatment-induced and near-universal with delivery + antibiotics. Notably, **intra-amniotic infection can be eradicated with antibiotics without delivering** in a subset — see §12.

**Critical periods.**
- **23–32 weeks** — the pre-oligodendrocyte vulnerability window for white-matter injury; also the canalicular/saccular lung window where inflammation arrests alveolarization.
- **Latency period after PPROM** — the intervention window for latency antibiotics + antenatal corticosteroids + magnesium sulfate.
- **≥18 hours ROM** — the inflection point for infection risk and for GBS prophylaxis indication.
- **Intrapartum, first 4 hours of fever** — the window in which myometrial contractility declines (~2 hours post-fever onset), driving the cesarean/atony risk.

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source/notes |
|---|---|---|
| Clinical chorioamnionitis, all births (US) | **1–5%** (commonly quoted 1–4%) | Definition-dependent |
| Clinical chorioamnionitis, national US administrative data | **1.29%** of >9 million live births | Recent national analysis |
| Secular trend | **2.7% (1995–96) → 6.0% (2009–10)** | Kaiser Permanente Southern California; rate more than doubled |
| Clinical chorioamnionitis at term | ~2–5% of term deliveries | |
| Histologic acute chorioamnionitis at term | **3–5%** | Kim 2015 (PMID:26428501) |
| Histologic acute chorioamnionitis at 21–24 weeks | **94%** | Kim 2015 — the key gradient |
| Histologic chorioamnionitis in PPROM | ~24% in one series (72/295); higher in others | PMC10079121 |
| Intrauterine infection as cause of preterm birth | **~25–40%** of all preterm births; up to 40–70% of early preterm | Goldenberg RL, Hauth JC, Andrews WW. N Engl J Med 2000;342(20):1500-7 (**PMID:10816189** — *no abstract available*, cite as review) |
| Microbial invasion of amniotic cavity in preterm labor | **~35%**, of which ~28% *Ureaplasma* | |
| Sterile intra-amniotic inflammation in preterm labor, intact membranes | **26%** vs 11% microbial-associated | PMID:25078709 |

**Incidence expressed per 100,000 for the dismech `Prevalence` block:** clinical chorioamnionitis ≈ **1,290–5,000 per 100,000 live births** (`measure_type: BIRTH_PREVALENCE`, `prevalence_class: ABOVE_1_IN_1000`, `rate_per_100000: 1290` for the national-administrative estimate; add a second record for the histologic lesion at term, ~3,000–5,000/100,000, and a third for the 21–24-week stratum at ~94,000/100,000 which is the striking one). Use `population:` for the cohort and put the verbatim source phrasing in `notes:`.

### Inheritance

**Not applicable as a Mendelian trait.** If an `inheritance:` block is curated at all, it should be `HP:0010982` **Polygenic inheritance** with `relationship_type: SUSCEPTIBILITY` on the contributing genes, and the block `description` must state plainly that the condition is acquired and infectious/inflammatory with only modest, unreplicated host-genetic modification. There is **no** penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency to curate. Do not invent these.

### Population demographics

- **Geographic:** global; higher burden in low- and middle-income settings tracking untreated genital infection, limited antenatal care, and higher preterm-birth rates (sub-Saharan Africa, South Asia). US data show substantial regional and institutional variation driven partly by diagnostic-threshold differences.
- **Ancestry/ethnicity:** higher reported rates in Black and Hispanic US populations. This tracks BV prevalence, preterm-birth disparity, and healthcare access — curate as an epidemiological association with an explicit note that no genetic basis is established. Getting this framing wrong is a real harm; be careful.
- **Sex ratio:** the maternal condition is by definition female. For the *fetal/neonatal* phenotypes, male fetuses have somewhat worse inflammation-associated outcomes (male disadvantage in preterm neurodevelopmental injury), a consistent but modest effect.
- **Age distribution:** maternal — reproductive age, with elevated risk at the young extreme (<20 years). Neonatal — perinatal onset with sequelae presenting through early childhood.

---

## 10. Diagnostics

### Clinical criteria
As in §1: NICHD Triple I tiers (isolated fever / suspected / confirmed) and ACOG CO 712 thresholds. The clinical diagnosis is **sensitive but poorly specific** — the central diagnostic problem of this disease.

### Laboratory tests

**Maternal blood:** CBC with differential (WBC >15,000/mm³, left shift; confounded by corticosteroids and by labor itself), CRP, procalcitonin (better specificity than CRP for true infection), blood cultures (positive in a minority), lactate if sepsis suspected.

**Amniotic fluid (via amniocentesis — the reference standard, but invasive and rarely performed at term):**

| Test | Threshold | Performance |
|---|---|---|
| **Gram stain** | Any organisms | Highly specific, poorly sensitive (misses mycoplasmas entirely — no cell wall) |
| **Glucose** | **<14–15 mg/dL** | Mean 5 ± 2.4 mg/dL in IAI vs 39.8 ± 18.4 mg/dL without; *"more sensitive and more specific than Gram's stain"* |
| **WBC count** | >50 cells/mm³ | Moderate |
| **LDH** | Elevated; isoform mapping | Research-grade |
| **IL-6** | **≥2.6 ng/mL** (Romero) or ≥11.3 ng/mL depending on assay | Sens 88%, spec 70%, PPV 67%, NPV 89% |
| **MMP-8** | Rapid point-of-care strip | Sens 80%, spec 87%, PPV 81%, NPV 86% |
| **Culture** (aerobic + anaerobic + **mycoplasma-specific**) | Growth | Definitive but slow and insensitive |
| **Broad-range PCR / PCR-ESI-MS, 16S rRNA sequencing** | Detection | Detects uncultivable organisms; the modern reference |

An important curation point: **AF IL-6/MMP-8 define *inflammation*; culture/PCR define *infection*.** The 2×2 of these two axes (microbial-associated inflammation / sterile inflammation / colonization without inflammation / neither) is the correct mechanistic taxonomy and should shape the `definitions[]` and `biochemical` blocks.

**Fetal/neonatal:** cord-blood IL-6 (>11 pg/mL defines FIRS type I), cord CXCL10 (>82.34 pg/mL, FIRS type II), neonatal CBC with I:T ratio, CRP, procalcitonin, blood culture, CSF if indicated, gastric aspirate/surface cultures (low yield, largely abandoned).

**LOINC anchors** (verify all): serum glucose, WBC count, CRP, procalcitonin, IL-6, and the amniotic-fluid analyte codes. Given your `loinc-no-reference-ranges` memory, do **not** attempt to source reference intervals from LOINC — cite the primary literature intervals above and put non-citable lab-manual provenance in `notes:`.

### Imaging and functional tests
- **Ultrasound:** limited direct value. Findings suggesting infection: absent fetal breathing movements, biophysical profile ≤6, oligohydramnios after PPROM, "sludge" (dense amniotic-fluid debris near the internal os — a marker of intra-amniotic infection and short cervix), short cervical length, thickened/echogenic membranes. In *Listeria* chorioamnionitis, characteristic fetal ultrasound features are described (**PMID:23429225**).
- **Electronic fetal monitoring:** baseline fetal tachycardia >160 bpm; reduced FHR variability; absent accelerations. FHR patterns in chorioamnionitis carry independent CP risk information (**PMID:36433630**).
- **Neonatal cranial ultrasound / MRI:** IVH, cystic PVL, diffuse white-matter injury.
- **No role for maternal CT/MRI/PET.**

### Histopathology (the reference standard for the lesion)
Placental examination per Amsterdam criteria: staged and graded MIR and FIR as in §8. Immunohistochemistry (CD15, myeloperoxidase) can help distinguish maternal vs. fetal neutrophils in ambiguous cases; XY-FISH or HLA-typing definitively assigns neutrophil origin in research settings. **Necrotizing funisitis** implies chronic (days-to-weeks) fetal inflammation and carries the worst neurodevelopmental prognosis.

### Genetic testing
**None indicated.** Not applicable: WGS, WES, gene panels, single-gene testing, CMA, karyotype, FISH, mtDNA testing, repeat-expansion testing. This is worth stating explicitly in the entry so downstream tools don't infer absence-of-evidence.

### Omics-based diagnostics
- **Proteomics:** AF proteomic MR score (defensins + S100 proteins) — validated in research settings, not clinically deployed.
- **Transcriptomics:** maternal-blood placenta-derived scRNA-seq signatures detectable in circulation and predictive of spontaneous preterm birth (Garcia-Flores 2024, **PMID:38198568**) — the most promising non-invasive avenue.
- **Metabolomics:** AF NMR/MS signatures — research only.
- **Liquid biopsy:** cell-free RNA/DNA in maternal plasma — emerging.
- **Cervicovaginal fluid proteomics** — patented approaches exist; not standard of care.

### Differential diagnosis

| Alternative | Distinguishing features |
|---|---|
| **Epidural-related maternal fever** | Fever after epidural placement, no purulent discharge, WBC often normal-ish, IL-6 elevated but AF sterile, no fetal tachycardia in many cases, antibiotics don't help |
| Urinary tract infection / pyelonephritis | CVA tenderness, pyuria, positive urine culture |
| Influenza, COVID-19, other systemic viral illness | Respiratory symptoms, seasonality, viral testing |
| Appendicitis | RLQ/migrating pain, peritoneal signs, leukocytosis without genital findings |
| Placental abruption | Vaginal bleeding, uterine hypertonus, non-reassuring FHR, no fever |
| Dehydration/environmental hyperthermia | Responds to hydration/cooling |
| Drug fever, transfusion reaction | Temporal association |
| Thyroid storm | Rare; thyrotoxic features |
| Chronic chorioamnionitis / villitis of unknown etiology | Lymphocytic, not neutrophilic; late preterm; maternal anti-fetal rejection biology |
| Post-partum endometritis | Onset after delivery |

### Screening
- **Universal antenatal GBS screening at 36 0/7 – 37 6/7 weeks** (ACOG 2020 / AAP; stewardship moved from CDC to ACOG+AAP in 2018) — not screening for chorioamnionitis per se, but the main population-level intervention in this space.
- **BV screening:** recommended only in symptomatic women or high-risk (prior preterm birth) contexts; USPSTF recommends *against* screening asymptomatic low-risk pregnant persons.
- **Cervical length screening** in women with prior spontaneous preterm birth — identifies the high-risk group.
- **No newborn/carrier/cascade screening applies.**

---

## 11. Outcome / Prognosis

### Maternal
- **Mortality:** very low in high-resource settings (<0.1%); maternal sepsis from chorioamnionitis remains a meaningful contributor to maternal death in low-resource settings.
- **Morbidity:** *"Maternal morbidity from intraamniotic infection also can be significant, and may include dysfunctional labor requiring increased intervention, postpartum uterine atony with hemorrhage, endometritis, peritonitis, sepsis, adult respiratory distress syndrome and, rarely, death."* `[VERBATIM]` — ACOG CO 712 (**PMID:28742677**). Add: cesarean delivery (2–3× increased), wound infection, pelvic abscess, septic pelvic thrombophlebitis, necrotizing fasciitis (rare), blood transfusion, prolonged hospitalization.
- **Recovery:** essentially complete with treatment. Recurrence risk in a subsequent pregnancy is elevated (population-based, **PMC3587161**).
- **Important negative:** *"Intraamniotic infection alone is rarely, if ever, an indication for cesarean delivery."* `[VERBATIM]` — ACOG CO 712.

### Neonatal — short term
Pooled effect sizes worth curating (each needs its own PMID + verified snippet):
- **Early-onset sepsis:** combined OR **3.45 (95% CI 2.02–5.89)** for chorioamnionitis overall in preterm infants; histologic chorioamnionitis unadjusted pooled OR **4.42 (2.68–7.29)** for confirmed EOS and **5.88 (3.68–9.41)** for any EOS (Frontiers in Immunology 2020 systematic review/meta-analysis/meta-regression, **PMC7289970**).
- **Composite adverse neonatal outcomes:** approximately **2- to 3.5-fold increased odds** of perinatal death, EOS, septic shock, pneumonia, meningitis, IVH, cerebral white-matter damage, ROP, NEC, and long-term disability including CP.
- **PDA:** significant association on meta-analysis (**PMC4574167**).
- **Funisitis specifically** carries worse short-term prematurity outcomes than chorioamnionitis alone (frequentist + Bayesian meta-analysis, **PMID:36830092**).

### Neonatal — long term
> *"Using a random effects model, clinical chorioamnionitis was significantly associated with both cerebral palsy (RR, 1.9; 95% CI, 1.4-2.5) and cPVL (RR, 3.0; 95% CI, 2.2-4.0) in preterm infants. The RR of histologic chorioamnionitis and cerebral palsy was 1.6 (95% CI, 0.9-2.7) in preterm infants, and histologic chorioamnionitis was significantly associated with cPVL (RR, 2.1; 95% CI, 1.5-2.9). Among full-term infants, a positive association was found between clinical chorioamnionitis and cerebral palsy (RR, 4.7; 95% CI, 1.3-16.2)."* `[VERBATIM]` — Wu YW, Colford JM Jr. JAMA 2000;284(11):1417-1424 (**PMID:10989405**).

Additional long-term: bronchopulmonary dysplasia and childhood respiratory morbidity/asthma; neurodevelopmental impairment and lower cognitive scores; increased long-term infectious morbidity of offspring (**PMID:38337508**); associations with autism spectrum disorder and schizophrenia in the broader maternal-immune-activation literature (weaker, confounded — curate as EMERGING with a `KNOWLEDGE_GAP`).

### Prognostic factors
Gestational age at exposure (dominant); presence and stage of **funisitis** (fetal, not just maternal, response — much stronger predictor); **cord IL-6 >11 pg/mL** (FIRS); necrotizing funisitis (worst); organism identity (*Candida*, GBS, *E. coli* worse than *Ureaplasma* alone for acute sepsis; *Ureaplasma* disproportionately associated with BPD); duration of ROM; maternal antibiotic administration; antenatal corticosteroid exposure; birthweight; male sex; presence of chronic vs acute inflammation.

**Prognostic biomarkers:** cord-blood IL-6, CXCL10; AF MMP-8 and IL-6; neonatal CRP/procalcitonin trajectory; the AF proteomic MR score.

---

## 12. Treatment

### Maternal — intrapartum antibiotics (standard of care)

Per ACOG CO 712 (**PMID:28742677**): *"Administration of intrapartum antibiotics is recommended whenever an intraamniotic infection is suspected or confirmed."*

| Regimen | Detail | NCIT anchor |
|---|---|---|
| **Ampicillin + gentamicin** (first line) | Ampicillin 2 g IV q6h + gentamicin 2 mg/kg load then 1.5 mg/kg q8h (or 5 mg/kg q24h) | Pharmacotherapy **NCIT:C15986** + `therapeutic_agent` ampicillin (CHEBI:28971 *verify*), gentamicin (CHEBI — *verify*) |
| **Add clindamycin or metronidazole** for cesarean delivery | Anaerobic coverage at cord clamp | + clindamycin (CHEBI:3745 *verify*) / metronidazole (CHEBI:6909 *verify*) |
| **Penicillin-allergic (mild)** | Cefazolin + gentamicin | |
| **Penicillin-allergic (severe)** | Clindamycin *or* vancomycin + gentamicin | |
| **Duration** | Through delivery; *"Antibiotic therapy should only be continued postdelivery in women with risk factors for postpartum endometritis, such as bacteremia or persistent fever"* `[VERBATIM]` | |

Adjuncts: **antipyretics** (acetaminophen — CHEBI:46195, *verify*) — reduces maternal and fetal tachycardia and may reduce unnecessary intervention; **delivery** is the definitive therapy for the maternal disease (but *not* an automatic indication for cesarean); IV hydration; oxytocin augmentation with anticipation of atony; active management of the third stage.

**Modality tags:** `therapeutic_modality: SMALL_MOLECULE` for the antibiotics, `SURGERY` for cesarean, `SUPPORTIVE`→ use `NCIT:C15747` Supportive Care with `BEHAVIORAL`/`OTHER` as appropriate.

### Preterm-specific / expectant-management regimens

- **PPROM latency antibiotics — "Mercer protocol":** IV ampicillin 2 g + erythromycin 250 mg q6h × 48 h, then oral amoxicillin 250 mg + erythromycin base 333 mg q8h × 5 days. Prolongs latency, reduces chorioamnionitis, reduces prematurity-related neonatal morbidity (Mercer BM et al., JAMA 1997).
- **ORACLE I (Lancet 2001):** erythromycin improved short-term neonatal outcomes in PPROM; **co-amoxiclav prolonged pregnancy but significantly increased neonatal necrotizing enterocolitis** — hence the standing prohibition on amoxicillin-clavulanate in PPROM. This is a great `WRONG_STATEMENT`/harm-of-treatment evidence item.
- **Azithromycin substitution for erythromycin** — comparable latency, possibly lower chorioamnionitis and postpartum endometritis rates (**PMC7368187**); increasingly the practical default given erythromycin supply issues.
- **Intra-amniotic infection eradication (Yoon/Romero regimen):** ceftriaxone + clarithromycin + metronidazole. *"The rates of intra-amniotic inflammation and intra-amniotic inflammation/infection in patients who received regimen 2 decreased during treatment from 68.8% to 52.1% and from 75% to 54.2%, respectively... intra-amniotic inflammation/infection was eradicated in 33.3% of patients who received regimen 2, but in none who received regimen 1."* `[VERBATIM]` — Lee J, Romero R, Kim SM, Chaemsaithong P, Yoon BH. J Matern Fetal Neonatal Med 2016;29(17):2727-37 (**PMID:26441216**). In preterm labor with intact membranes, eradication was confirmed in **79%** of those with follow-up amniocentesis (**PMID:30928566**). This is a genuinely under-appreciated therapeutic finding and deserves an EMERGING hypothesis node — the field's default is "infection means deliver," and these data say a subset can be *treated*.
- **Antenatal corticosteroids** (betamethasone/dexamethasone) — administered even in the setting of chorioamnionitis at eligible gestational ages; net benefit favors administration. NCIT:C15986 + betamethasone.
- **Magnesium sulfate** for fetal neuroprotection <32 weeks — relevant given the PVL/CP pathway.
- **Tocolysis is contraindicated** in confirmed intra-amniotic infection.

### Cesarean-associated prophylaxis
- Pre-incision cefazolin (standard).
- **Adjunctive azithromycin 500 mg IV** at unscheduled cesarean in labor or after ROM — C/SOAP trial (Tita ATN et al., N Engl J Med 2016) reduced composite postoperative infection.
- Vaginal preparation with povidone-iodine/chlorhexidine before cesarean.

### Neonatal management
- **Preterm exposed newborns:** blood culture + empiric ampicillin + gentamicin, with de-escalation at 36–48 h if cultures negative and infant well (Puopolo KM, Benitz WE, Zaoutis TE; AAP COFN/COID, Pediatrics 2018 — separate statements for ≥35 0/7 wk and ≤34 6/7 wk).
- **Well-appearing term/late-preterm exposed newborns:** the field has moved decisively from "treat everyone exposed" to risk-stratified care. The **Kaiser Permanente neonatal early-onset sepsis risk calculator** stratifies to observe-only / observe-and-evaluate / evaluate-and-consider-treatment / evaluate-and-treat, and substantially reduces empiric antibiotic exposure without missed sepsis in the published series (**PMID:29275925**, **PMID:29467522**, **PMID:37827729**). *"Previous CDC and AAP management strategies from 2010 to 2012 contributed to unnecessary EOS evaluations of asymptomatic newborns ≥35 weeks' gestation, including evaluation and antibiotics on all newborns exposed to chorioamnionitis regardless of clinical appearance."* `[PARAPHRASE — reverify]`
- Supportive: respiratory support/surfactant, caffeine, thermoregulation, nutrition; NEC and BPD prevention bundles.

### Not applicable
Gene therapy, cell therapy, RNA-based therapies, targeted small-molecule oncology-style therapies, immunotherapies (checkpoint inhibitors), rehabilitation *for the acute maternal illness*. **Rehabilitation IS relevant downstream** for CP-affected offspring (physical therapy NCIT:C15302, occupational therapy NCIT:C121351, speech therapy NCIT:C159273) — curate those on the sequelae, not on chorioamnionitis itself.

### Experimental / trial landscape
Search ClinicalTrials.gov for: NCT registrations on azithromycin vs erythromycin for PPROM (e.g., NCT07183462 for late PPROM), intra-amniotic infection eradication regimens, antenatal N-acetylcysteine for inflammation-associated fetal brain injury, IL-1 receptor antagonist (anakinra) and the small-molecule IL-1R antagonist **rytvela (101.10)** for intrauterine inflammation (preclinical→early clinical), TLR4 antagonists, and probiotic/vaginal-microbiome-modulation trials. Populate `clinical_trials:` with `just fetch-reference NCT…` — do **not** hand-write these, and remember `phase` is an enum (`PHASE_III`, not "Phase III").

### Pharmacogenomics
No established PGx for this indication. Relevant general PGx: aminoglycoside ototoxicity and **MT-RNR1 m.1555A>G** (CPIC guideline — a genuine, curatable, actionable gene-drug pair given that gentamicin is first-line therapy here). That's the one PGx item worth including, and it's a nice one because it's real, actionable, and specific to the standard regimen.

---

## 13. Prevention

**Primary prevention**
- Universal antenatal **GBS screening at 36 0/7–37 6/7 weeks** with intrapartum penicillin prophylaxis for colonized women, ROM ≥18 h, prior GBS-affected infant, GBS bacteriuria, or intrapartum fever with unknown status. Reduced early-onset GBS disease from **1.8 → 0.23 per 1,000 live births**.
- **Minimize digital cervical examinations**, especially after ROM; prefer sterile speculum; avoid unnecessary internal monitoring.
- **Avoid/limit unnecessary labor induction and prolonged latent-phase management** where clinically reasonable.
- Treat symptomatic **bacterial vaginosis, trichomoniasis, gonorrhea, chlamydia**; treat asymptomatic bacteriuria.
- **Periodontal care** in pregnancy (mechanistically motivated by *F. nucleatum*; randomized trials of periodontal treatment have *not* reduced preterm birth — curate the mechanism as plausible and the intervention as ineffective, which is a nice honest pairing).
- **Smoking cessation**, weight management, adequate interpregnancy interval.
- Aseptic technique for amniocentesis/CVS/cerclage; timely removal of retained IUD.
- Vaginal cleansing before cesarean; adjunctive azithromycin at unscheduled cesarean.

**Secondary prevention**
- Early recognition of PPROM; latency antibiotics; serial monitoring for infection (temperature, WBC, FHR, fetal movement).
- Amniocentesis for AF IL-6/MMP-8/culture in selected PPROM and preterm-labor cases → antibiotic eradication attempt.
- Cervical-length screening + vaginal progesterone / cerclage in the appropriate high-risk groups (prevents preterm birth, and by extension exposure).
- Serial GBS-status verification; prompt intrapartum prophylaxis.

**Tertiary prevention**
- Antenatal corticosteroids; magnesium sulfate for neuroprotection <32 weeks.
- Delivery timing decisions balancing infection against prematurity.
- Risk-stratified neonatal EOS evaluation (avoiding *iatrogenic* harm from over-treatment — antibiotic exposure in the first week is itself associated with NEC, late-onset sepsis, and microbiome disruption).
- Neurodevelopmental follow-up programs for exposed preterm infants.

**Immunization.** No licensed vaccine prevents chorioamnionitis. **Maternal GBS conjugate/protein vaccines** are in advanced clinical development (Pfizer hexavalent GBS6, MinervaX) and are the most plausible future primary-prevention tool; WHO has published preferred product characteristics. Influenza and Tdap vaccination in pregnancy are unrelated to this pathway. Curate GBS vaccines as EXPERIMENTAL with `therapeutic_modality: VACCINE`, `NCIT:C15346` vaccination.

**Genetic counseling / genetic screening / PGD / prenatal genetic testing:** **not applicable.** State this explicitly.

**Public health interventions:** antenatal care access and coverage; STI screening and partner treatment programs; skilled birth attendance and clean-delivery practices (WHO); antimicrobial stewardship in obstetrics and neonatology; hand hygiene and infection-control bundles on labor and delivery.

---

## 14. Other Species / Natural Disease

Chorioamnionitis and its cousin, placentitis, are genuinely important in veterinary medicine — this isn't a courtesy section.

| Species | NCBITaxon | Natural disease |
|---|---|---|
| **Horse** (*Equus caballus*) | NCBITaxon:9796 | **Placentitis** is a leading cause of abortion, premature birth, and weak foals. Two forms: (a) **ascending bacterial placentitis** (*Streptococcus equi* subsp. *zooepidemicus*, *E. coli*, *Leptospira*, *Klebsiella*) with cervical-star lesions; (b) **nocardioform placentitis** — focal mucoid lesions on the ventral uterine body/horn bases, **85% caused by *Amycolatopsis* spp. and *Crossiella equi***, gram-positive branching actinomycetes; episodic outbreaks, mechanism still poorly understood. Transcriptomic analysis of equine chorioallantois in nocardioform placentitis has mapped the immune networks involved (Vet Res 2021). |
| **Cattle** (*Bos taurus*) | NCBITaxon:9913 | ***Ureaplasma diversum*** causes placentitis, fetal alveolitis, abortion and weak calves, mainly in the last trimester. Its membrane-associated lipoproteins activate inflammatory genes **through the NF-κB pathway via TLR4** (**PMC6052353**) — a direct mechanistic homolog of the human *Ureaplasma* story. Also *Brucella abortus*, *Coxiella burnetii*, *Campylobacter fetus*, *Tritrichomonas foetus*, *Chlamydia*, BVDV. |
| **Sheep** (*Ovis aries*) | NCBITaxon:9940 | *Chlamydia abortus* (enzootic abortion of ewes) and *Coxiella burnetii* — both **zoonotic**, causing severe disease including chorioamnionitis and pregnancy loss in exposed pregnant humans. The sheep is also *the* experimental model (see §15). |
| **Goat** (*Capra hircus*) | NCBITaxon:9925 | *C. abortus*, *C. burnetii* |
| **Pig** (*Sus scrofa*) | NCBITaxon:9823 | *Leptospira*, *Brucella suis*, PRRSV-associated placentitis |
| **Dog / Cat** | NCBITaxon:9615 / 9685 | *Brucella canis*, *E. coli*, *Streptococcus* placentitis; feline herpesvirus, FIV/FeLV-associated losses |
| **Rhesus macaque** (*Macaca mulatta*) | NCBITaxon:9544 | Naturally occurring chorioamnionitis reported in colonies; also the premier experimental model |

**Comparative pathology.** The neutrophilic ascending-infection pattern is broadly conserved across placental mammals, but placental architecture is *not* — humans and NHPs are hemochorial and discoid; ruminants are epitheliochorial/cotyledonary; horses are diffuse epitheliochorial. This is the single most important caveat for cross-species extrapolation and belongs in a `HUMAN_MODEL_MISMATCH` discussion: an epitheliochorial placenta has more physical layers between maternal blood and fetus, which changes both microbial access and cytokine transfer. Sheep, the workhorse fetal-physiology model, are exactly the mismatch case.

**Evolutionary conservation.** TLR4/MyD88/NF-κB signaling, IL-1/IL-6/TNF, the NLRP3 inflammasome, MMP-8/MMP-9, and prostaglandin synthesis are deeply conserved across mammals (Alliance of Genome Resources / HomoloGene orthologs exist for all of these). The *timing* control of parturition, by contrast, is poorly conserved — mice depend on luteolysis/progesterone withdrawal, humans do not — which limits mouse preterm-labor models specifically.

**Zoonotic potential / cross-species transmission.** Real and clinically important: *Coxiella burnetii* (Q fever) and *Chlamydia abortus* from parturient small ruminants cause human placentitis, chorioamnionitis and pregnancy loss; *Brucella* spp.; *Listeria monocytogenes* (foodborne, from animal reservoirs); *Toxoplasma gondii* (felid definitive host). Pregnant people are specifically counseled to avoid lambing/kidding operations — a real public-health rule grounded in this mechanism.

**Orthologous genes** for the mechanism nodes: mouse *Tlr4* (NCBI Gene 21898), *Il6* (16193), *Il1b* (16176), *Tnf* (21926), *Nlrp3* (216799), *Ptgs2* (19225), *Mmp9* (17395) — verify all IDs before curating.

---

## 15. Model Organisms

Chorioamnionitis has an unusually good and unusually *large-animal*-weighted model landscape, because the key readouts (fetal lung, fetal brain, chronic instrumentation) need a big fetus.

### Non-human primate — rhesus macaque (*Macaca mulatta*, NCBITaxon:9544)
The gold standard: hemochorial discoid placenta, similar gestational immunology, chronic catheterization possible.
- **Intra-amniotic *U. parvum*:** *"U. parvum decreased regulatory T cells (Tregs) and activated interferon γ production in these Tregs in the fetus"*, with organism thriving in AF and colonizing fetal lung but only **modest** inflammation and no severe chorioamnionitis, plus increased uterine **connexin-43** (**PMID:27601620**, J Infect Dis 2016;214(10):1597-1604). `[PARAPHRASE for the framing sentences — the quoted clause appears verbatim; reverify.]`
- ***Ureaplasma parvum* or *Mycoplasma hominis* as sole pathogens cause chorioamnionitis, preterm delivery, and fetal pneumonia in rhesus macaques** (Novy MJ, Grigsby PL et al., Reprod Sci 2009) — the definitive Koch's-postulate-style demonstration for genital mycoplasmas.
- **Intra-amniotic LPS causes acute neuroinflammation in preterm rhesus macaques** (**PMC5011884**) — the cleanest primate link from intra-amniotic inflammation to fetal brain injury.
- **Intra-amniotic IL-1β** → decidual neutrophil recruitment and activation (**PMC4342792**) — isolates the cytokine arm from the microbe.
- **TLR4 antagonist pretreatment** inhibited LPS-induced preterm uterine contractility, cytokines and prostaglandins in rhesus monkeys (**PMC2774271**) — a genuine mechanistic intervention study and the best evidence for TLR4 as a druggable node.

### Sheep (*Ovis aries*, NCBITaxon:9940) — the fetal-lung workhorse
- **Intra-amniotic *E. coli* LPS** (typically 10 mg, 2 or 7 days before preterm delivery at ~124 d gestation) → influx of inflammatory cells into fetal lung, lung inflammation, and *functional lung maturation* — the classic dissociation of surfactant induction from structural maturation (Kallapur SG, Jobe AH and colleagues; **PMC2660220**).
- **Intra-amniotic *Ureaplasma parvum*** → chronic low-grade lung inflammation with functional maturation (**PMC3006269**).
- **A20 (TNFAIP3)** upregulation in fetal lung in the sheep LPS model (**PMC8794675**) — the negative-feedback/tolerance arm.
- Also used for fetal brain injury (white-matter), gut, and thymic involution readouts, and for "inflammation tolerance" (a second LPS dose produces a blunted response).
- **Limitation to record:** epitheliochorial cotyledonary placenta, not hemochorial; and outbred, non-genetically-tractable.

### Mouse (*Mus musculus*, NCBITaxon:10090) — the mechanism/genetics workhorse
- **Intrauterine LPS infusion model** (time-pregnant CD-1; mini-laparotomy, LPS into the uterus between the first two gestational sacs) — reproducible preterm birth plus fetal brain injury (**PMID:31419431**, Am J Pathol 2019 characterization).
- **IL-1 receptor antagonist:** *"IL-1 receptor blockade prevents fetal cortical brain injury but not preterm birth in a mouse model of inflammation-induced preterm birth and perinatal brain injury"* (**PMC3989434**) — a clean dissociation of the brain-injury and parturition arms, and an important nuance for any therapeutic node.
- **Intra-amniotic HMGB1** → preterm labor/birth in **57%** of mice vs **0%** of controls (**PMID:26781934**) — the sterile-inflammation proof of principle.
- ***Fusobacterium nucleatum*** induces premature and term stillbirths in pregnant mice, implicating oral bacteria (Infect Immun 2004;72(4):2272-2279).
- **Nr4a1** mediates perinatal neuroinflammation in murine preterm labor (Cell Death Dis 2019).
- **Single-cell atlas of murine reproductive tissues during preterm labor** (Cell Rep 2022) — the mouse counterpart of the human atlas.
- **Knockouts/transgenics available (MGI/IMPC/KOMP):** *Tlr4*, *Tlr2*, *Myd88*, *Il1r1*, *Il6*, *Tnf*, *Nlrp3*, *Casp1*, *Ptgs2*, *Mmp9*, *Trif/Ticam1*. Conditional and reporter lines exist for most.
- **Limitations to record:** progesterone-withdrawal-dependent parturition (unlike humans); hemochorial but labyrinthine placenta; multiparous with very short gestation; systemic vs intra-amniotic route matters enormously and much of the literature uses intraperitoneal LPS, which is *not* the same disease.

### Rabbit, rat, guinea pig
Rabbit intracervical *E. coli* inoculation is a classic ascending-infection model (Fidel/Gibbs). Rat and guinea-pig LPS models are used for fetal brain injury; guinea pigs have the advantage of a more human-like brain-growth trajectory.

### In vitro / cellular
- **Human chorioamniotic membrane explants** — the direct model; e.g., *"Incubation of chorioamniotic membranes with HMGB1 induced the release of mature IL-1beta and IL-6"* (Biol Reprod 2016;95(6):130).
- Primary human amnion epithelial cells, chorion trophoblasts, decidual stromal cells, myometrial smooth-muscle cells (hTERT-immortalized lines).
- Cell lines: HTR-8/SVneo (extravillous trophoblast), BeWo/JEG-3 (choriocarcinoma, trophoblast surrogates), THP-1 (monocyte/macrophage), WISH (amnion-derived, but HeLa-contaminated — **flag this, it's a real reproducibility landmine**).
- **Organ-on-chip:** feto-maternal interface-on-chip (FMi-OOC), placenta-on-a-chip, and amnion membrane-on-chip systems (Menon and colleagues) — used to study ascending propagation of inflammation across membrane layers.
- **Organoids/iPSCs:** trophoblast organoids, endometrial/decidual organoids, iPSC-derived microglia for the neuroinflammation arm.

### Phenotype recapitulation summary

| Feature | NHP | Sheep | Mouse | Explant/chip |
|---|---|---|---|---|
| Ascending route | ✔✔ | ✔ | ✔ (intrauterine) | ✔ (FMi-OOC) |
| Histologic chorioamnionitis | ✔✔ | ✔✔ | ✔ | n/a |
| Funisitis / FIRS | ✔✔ | ✔ | limited | n/a |
| Preterm labor | ✔✔ | ✔ | ✔✔ | n/a |
| Fetal lung injury/BPD-like | ✔ | ✔✔ | ✔ | n/a |
| Fetal brain injury/PVL-like | ✔ | ✔ | ✔✔ | n/a |
| Genetic tractability | ✘ | ✘ | ✔✔ | ✔ |
| Cost/throughput | ✘ | ~ | ✔✔ | ✔✔ |

**Model databases:** MGI, IMPC, KOMP/EuMMCR, IMSR, MMRRC, RGD, ZFIN (no meaningful zebrafish model here — no placenta), Alliance of Genome Resources, Cellosaurus, ATCC.

---

## 16. Ontology Term Candidates — verification required

**Do not paste any of these into YAML without running `just validate-terms`.** Confidence is my honest read, not a substitute for OAK.

**MONDO (high confidence):** `MONDO:0000409` chorioamnionitis.

**HPO — high confidence:** HP:0001788 Premature rupture of membranes · HP:0001945 Fever · HP:0001649 Tachycardia · HP:0001974 Leukocytosis · HP:0001622 Premature birth · HP:0002098 Respiratory distress · HP:0100806 Sepsis · HP:0001643 Patent ductus arteriosus.
**HPO — medium, verify:** HP:0011227 Elevated circulating C-reactive protein concentration · HP:0100021 Cerebral palsy · HP:0001561/HP:0001562 Polyhydramnios/Oligohydramnios.
**HPO — needs lookup:** fetal tachycardia; periventricular leukomalacia; intraventricular hemorrhage (neonatal); necrotizing enterocolitis; bronchopulmonary dysplasia; retinopathy of prematurity; stillbirth; purulent vaginal discharge. There may be **no** HPO term for "chorioamnionitis" itself; the entry's identity should hang off MONDO, not HPO.

**GO biological process — high confidence:** GO:0006954 inflammatory response · GO:0006955 immune response · GO:0030593 neutrophil chemotaxis · GO:0032496 response to lipopolysaccharide · GO:0002224 toll-like receptor signaling pathway · GO:0001516 prostaglandin biosynthetic process · GO:0030198 extracellular matrix organization · GO:0022617 extracellular matrix disassembly · GO:0032611 interleukin-1 beta production · GO:0032635 interleukin-6 production · GO:0032640 tumor necrosis factor production · GO:0050829 defense response to Gram-negative bacterium · GO:0050830 defense response to Gram-positive bacterium · GO:0007567 parturition · GO:0006979 response to oxidative stress.
**GO — verify label drift:** GO:0007249 (canonical NF-κB signal transduction — label was renamed; your `snippet-validator-normalizes-whitespace` and MONDO-obsoletion memories apply here too, check live OLS not just the local sqlite).
**GO molecular function:** GO:0004222 metalloendopeptidase activity.
**GO cellular component:** GO:0072559 NLRP3 inflammasome complex · GO:0031012 extracellular matrix.

**CL — high confidence:** CL:0000775 neutrophil · CL:0000235 macrophage · CL:0000351 trophoblast cell · CL:0000084 T cell · CL:0000815 regulatory T cell · CL:0000623 natural killer cell · CL:0000057 fibroblast.
**CL — needs lookup:** decidual stromal cell; amnion epithelial cell; Hofbauer cell; microglial cell; oligodendrocyte precursor cell; uterine smooth muscle cell; endothelial cell of umbilical vein.

**UBERON — needs verification across the board:** placenta, amnion, chorion, decidua, amniotic fluid, umbilical cord, uterus, myometrium, uterine cervix, vagina, lung, brain white matter, intestine, retina.

**CHEBI:** CHEBI:16412 lipopolysaccharide (high) · CHEBI:15551 prostaglandin E2 (high) · CHEBI:17234 glucose (high) · CHEBI:46195 paracetamol (high) · ampicillin, gentamicin, clindamycin, azithromycin, erythromycin, metronidazole, ceftriaxone, betamethasone (all **verify**; per your `therapeutic-agent-chebi-only-cache` memory, prefer CHEBI over NCIT for `therapeutic_agent`).

**NCIT (treatment actions):** NCIT:C15986 Pharmacotherapy · NCIT:C15747 Supportive Care · NCIT:C15329 Surgical Procedure (cesarean — look for a specific cesarean-section term) · NCIT:C15346 Vaccination (GBS vaccine, experimental) · NCIT:C15302 Physical Therapy (downstream CP care).

**NCBITaxon:** as listed in §5.3 and §14.

---

## 17. Curation notes for the dismech entry

A few things that will save time (and reviewer round-trips) when this becomes `kb/disorders/Chorioamnionitis.yaml`:

- **Model the sterile arm as a first-class `mechanistic_hypotheses` group, not a footnote.** Sterile intra-amniotic inflammation is *more common* than microbial in preterm labor with intact membranes (26% vs 11%) and produces equivalent outcomes. An entry that treats this as purely infectious would be wrong on its own headline claim, and a reviewer will catch it. Suggested groups: `microbial_associated_inflammation` (CANONICAL), `sterile_alarmin_driven_inflammation` (CANONICAL — genuinely co-equal, not "alternative"), `epidural_systemic_maternal_inflammation` (ALTERNATIVE, term-specific).
- **Category check.** The template says Infectious. That's defensible but incomplete — consider `classifications` that also capture the inflammatory/perinatal dimension, and say so in the entry notes rather than silently forcing it into one bucket.
- **Module conformance candidates.** No existing dismech module is a clean fit. The closest structural analogy is `intestinal_barrier_dysfunction`'s insult-agnostic convergence logic — several distinct upstream insults (microbial, sterile/alarmin, epidural-systemic) converging on one downstream inflammatory cascade. This entry is arguably a good *seed* for a new **`ascending_mucosal_barrier_infection`** or **`sterile_vs_microbial_inflammatory_convergence`** module later; don't force a conformance declaration now.
- **Two `KNOWLEDGE_GAP` discussions worth writing:** (1) no validated non-invasive test distinguishes microbial-associated from sterile intra-amniotic inflammation, so antibiotic decisions are made blind; (2) the causal direction between histologic chorioamnionitis and preterm labor is not fully resolved at term, where inflammation may be a *consequence* of labor rather than its cause.
- **One `HUMAN_MODEL_MISMATCH` discussion:** placental architecture differs fundamentally between the sheep/ruminant models (epitheliochorial) and humans (hemochorial), and mouse parturition is progesterone-withdrawal-dependent while human parturition is not — so neither the dominant fetal-physiology model nor the dominant genetics model reproduces the human timing mechanism.
- **Evidence-source discipline:** the sheep, macaque, and mouse citations are `MODEL_ORGANISM`; the chorioamniotic-membrane explant and cell-line work is `IN_VITRO`; the amniocentesis cohorts, meta-analyses, and guidelines are `HUMAN_CLINICAL`. Do not let a macaque or sheep citation be the sole support for a human phenotype node — that's a recurring reviewer finding.
- **NEC (Named Entity Confusion) risk: low but non-zero.** "Chorioamnionitis" is unambiguous, but watch for drift into *chronic* chorioamnionitis, villitis of unknown etiology, and FIRS type II — those are a different lesion class with different biology (maternal anti-fetal rejection), and a DR report that wanders into them will look coherent and validate cleanly while describing the wrong entity.
- Remember the folded-scalar hyphen rule and the square-bracket-in-snippet rule from your CI memories — several of the quotes above contain bracketed statistics (e.g., `[26% (35/135) versus 11% (15/135)`), which **will** pass a local check and then fail CI. Trim those quotes at a bracket-free boundary before committing.

---

## Sources

**Primary literature (PubMed):**
- [Kim CJ, Romero R, et al. Acute chorioamnionitis and funisitis: definition, pathologic features, and clinical significance. AJOG 2015;213(4 Suppl):S29-52 — PMID:26428501](https://pubmed.ncbi.nlm.nih.gov/26428501/)
- [Gomez R, Romero R, Ghezzi F, Yoon BH, Mazor M, Berry SM. The fetal inflammatory response syndrome. AJOG 1998;179(1):194-202 — PMID:9704787](https://pubmed.ncbi.nlm.nih.gov/9704787/)
- [Romero R, Miranda J, et al. Prevalence and clinical significance of sterile intra-amniotic inflammation. Am J Reprod Immunol 2014;72(5):458-74 — PMID:25078709](https://pubmed.ncbi.nlm.nih.gov/25078709/)
- [Higgins RD, Saade G, Polin RA, et al. Evaluation and Management of Women and Newborns With a Maternal Diagnosis of Chorioamnionitis: Summary of a Workshop. Obstet Gynecol 2016;127(3):426-436 — PMID:26855098](https://pubmed.ncbi.nlm.nih.gov/26855098/)
- [ACOG Committee Opinion No. 712: Intrapartum Management of Intraamniotic Infection. Obstet Gynecol 2017;130(2):e95-e101 — PMID:28742677](https://pubmed.ncbi.nlm.nih.gov/28742677/)
- [Wu YW, Colford JM Jr. Chorioamnionitis as a risk factor for cerebral palsy: a meta-analysis. JAMA 2000;284(11):1417-1424 — PMID:10989405](https://pubmed.ncbi.nlm.nih.gov/10989405/)
- [Khong TY, Mooney EE, Ariel I, et al. Sampling and Definitions of Placental Lesions: Amsterdam Placental Workshop Group Consensus Statement. Arch Pathol Lab Med 2016;140(7):698-713 — PMID:27223167](https://pubmed.ncbi.nlm.nih.gov/27223167/)
- [Jung E, Romero R, Suksai M, et al. Clinical chorioamnionitis at term. AJOG 2024;230(3S):S807-S840 — PMID:38233317](https://www.ajog.org/article/S0002-9378(23)00080-7/abstract)
- [Yoon BH, Romero R, et al. Microbial invasion of the amniotic cavity with Ureaplasma urealyticum. AJOG 1998;179(5):1254-60 — PMID:9822511](https://pubmed.ncbi.nlm.nih.gov/9822511/)
- [Lee J, Romero R, Kim SM, Chaemsaithong P, Yoon BH. A new antibiotic regimen treats and prevents intra-amniotic inflammation/infection in preterm PROM. J Matern Fetal Neonatal Med 2016;29(17):2727-37 — PMID:26441216](https://pubmed.ncbi.nlm.nih.gov/26441216/)
- [Antibiotic administration can eradicate intra-amniotic infection or inflammation in preterm labor with intact membranes — PMID:30928566](https://pubmed.ncbi.nlm.nih.gov/30928566/)
- [Garcia-Flores V, Romero R, et al. Deciphering maternal-fetal cross-talk in the human placenta during parturition using scRNA-seq. Sci Transl Med 2024;16(729):eadh8335 — PMID:38198568](https://pubmed.ncbi.nlm.nih.gov/38198568/)
- [Para R, Romero R, et al. The Distinct Immune Nature of the Fetal Inflammatory Response Syndrome Type I and Type II. ImmunoHorizons 2021;5(9):735-751 — PMID:34521696](https://academic.oup.com/immunohorizons/article/5/9/735/7820217)
- [Senthamaraikannan P, Presicce P, et al. Intra-amniotic Ureaplasma parvum-Induced Maternal and Fetal Inflammation in Rhesus Macaques. J Infect Dis 2016;214(10):1597-1604 — PMID:27601620](https://pubmed.ncbi.nlm.nih.gov/27601620/)
- [Goldenberg RL, Hauth JC, Andrews WW. Intrauterine infection and preterm delivery. N Engl J Med 2000;342(20):1500-7 — PMID:10816189 (no abstract)](https://pubmed.ncbi.nlm.nih.gov/10816189/)
- [Macones GA, et al. A polymorphism in the promoter region of TNF and bacterial vaginosis — PMID:15284722](https://pubmed.ncbi.nlm.nih.gov/15284722/)
- [Adverse outcomes after preterm labor and TNF-alpha polymorphism -863 — PMID:15507966](https://pubmed.ncbi.nlm.nih.gov/15507966/)
- [Timing of Histologic Progression from Chorio-Deciduitis to Chorio-Deciduo-Amnionitis — PMID:26574743](https://pubmed.ncbi.nlm.nih.gov/26574743/)
- [Intra-Amniotic Administration of HMGB1 Induces Spontaneous Preterm Labor and Birth — PMID:26781934](https://pubmed.ncbi.nlm.nih.gov/26781934/)
- [DAMPs in preterm labor and preterm PROM: HMGB1 — PMID:21958433](https://pubmed.ncbi.nlm.nih.gov/21958433/)
- [Association of epidural-related fever and noninfectious inflammation in term labor — PMID:21343762](https://pubmed.ncbi.nlm.nih.gov/21343762/)
- [Molecular evidence for hematogenous dissemination of Listeria monocytogenes intraamniotic infection — PMID:40643048](https://pubmed.ncbi.nlm.nih.gov/40643048/)
- [Utility of Early-Onset Sepsis Risk Calculator for Neonates Born to Mothers with Chorioamnionitis — PMID:29275925](https://pubmed.ncbi.nlm.nih.gov/29275925/)
- [Association of Funisitis with Short-Term Outcomes of Prematurity: meta-analysis — PMID:36830092](https://pubmed.ncbi.nlm.nih.gov/36830092/)
- [The Association between Term Chorioamnionitis during Labor and Long-Term Infectious Morbidity of the Offspring — PMID:38337508](https://pubmed.ncbi.nlm.nih.gov/38337508/)
- [Suspected Chorioamnionitis and Myometrial Contractility — PMID:29848185](https://pubmed.ncbi.nlm.nih.gov/29848185/)
- [Impact of microbial invasion of amniotic cavity and type of microorganisms on neonatal outcome — PMID:28094842](https://pubmed.ncbi.nlm.nih.gov/28094842/)
- [Chorioamnionitis caused by Listeria monocytogenes: ultrasound features — PMID:23429225](https://pubmed.ncbi.nlm.nih.gov/23429225/)
- [Fetal heart rate patterns complicated by chorioamnionitis and subsequent cerebral palsy — PMID:36433630](https://pubmed.ncbi.nlm.nih.gov/36433630/)

**PMC / journal full text:**
- [Association of Histological and Clinical Chorioamnionitis With Neonatal Sepsis: meta-analysis (Front Immunol 2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7289970/)
- [Uncultivated Bacteria as Etiologic Agents of Intra-Amniotic Inflammation Leading to Preterm Birth (J Clin Microbiol 2008)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2620857/)
- [HMGB1 Induces an Inflammatory Response in the Chorioamniotic Membranes (Biol Reprod 2016)](https://ncbi.nlm.nih.gov/pmc/articles/PMC5315428)
- [IL-1 Receptor Blockade Prevents Fetal Cortical Brain Injury But Not Preterm Birth](https://ncbi.nlm.nih.gov/pmc/articles/PMC3989434)
- [Intra-amniotic LPS causes acute neuroinflammation in preterm rhesus macaques](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5011884/)
- [Airway inflammatory cell responses to intra-amniotic LPS in a sheep model of chorioamnionitis](https://ncbi.nlm.nih.gov/pmc/articles/PMC2660220)
- [Inflammation in fetal sheep from intra-amniotic injection of Ureaplasma parvum](https://ncbi.nlm.nih.gov/pmc/articles/PMC3006269)
- [TLR4 antagonist inhibits LPS-induced preterm uterine contractility in rhesus monkeys](https://pmc.ncbi.nlm.nih.gov/articles/PMC2774271/)
- [Ureaplasma diversum lipoproteins activate inflammatory genes through NF-κB via TLR4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6052353/)
- [Acute Histologic Chorioamnionitis at Term: Nearly Always Noninfectious](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3296706/)
- [Polymorphisms in immunoregulatory genes and risk of histologic chorioamnionitis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC554771/)
- [Chorioamnionitis and Neonatal Outcomes (review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720117/)
- [Chorioamnionitis and Patent Ductus Arteriosus: systematic review and meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4574167/)
- [Azithromycin vs erythromycin in PPROM: lower chorioamnionitis and endometritis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7368187/)
- [A population-based study of the risk of repeat clinical chorioamnionitis, Washington State 1989–2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC3587161/)
- [Transcriptomic analysis of equine chorioallantois in nocardioform placentitis (Vet Res 2021)](https://link.springer.com/article/10.1186/s13567-021-00972-4)
- [Fusobacterium nucleatum Induces Premature and Term Stillbirths in Pregnant Mice (Infect Immun 2004)](https://journals.asm.org/doi/10.1128/iai.72.4.2272-2279.2004)
- [Characterization of an Adapted Murine Model of Intrauterine Inflammation–Induced Preterm Birth (Am J Pathol 2019)](https://www.sciencedirect.com/science/article/pii/S0002944019308508)
- [Proteomic Profiling of the Amniotic Fluid to Detect Inflammation, Infection, and Neonatal Sepsis (PLOS Med 2007)](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.0040018)
- [Advances in Medical Diagnosis of Intra-Amniotic Infection](https://pmc.ncbi.nlm.nih.gov/articles/PMC3790267/)

**Guidelines, ontologies and reference resources:**
- [ACOG — Intrapartum Management of Intraamniotic Infection (Committee Opinion 712)](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2017/08/intrapartum-management-of-intraamniotic-infection)
- [ACOG — Prevention of Group B Streptococcal Early-Onset Disease in Newborns (2020)](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2020/02/prevention-of-group-b-streptococcal-early-onset-disease-in-newborns)
- [AAP — Management of Infants at Risk for Group B Streptococcal Disease (Pediatrics 2019)](https://publications.aap.org/pediatrics/article/144/2/e20191881/38546/Management-of-Infants-at-Risk-for-Group-B)
- [CDC — Clinical Overview of Group B Strep Disease](https://www.cdc.gov/group-b-strep/hcp/clinical-overview/index.html)
- [StatPearls — Chorioamnionitis (NCBI Bookshelf NBK532251)](https://www.ncbi.nlm.nih.gov/books/NBK532251/)
- [Merck Manual Professional — Intraamniotic Infection (Chorioamnionitis)](https://www.merckmanuals.com/professional/gynecology-and-obstetrics/intrapartum-complications/intraamniotic-infection)
- [Mondo Disease Ontology — Monarch Initiative](https://mondo.monarchinitiative.org/)
- [ICD-10-CM O41.12 Chorioamnionitis](https://www.icd10data.com/ICD10CM/Codes/O00-O9A/O30-O48/O41-/O41.12)
- [Kaiser Permanente — Rate of Chorioamnionitis More than Doubled since 1995](https://www.kp-scalresearch.org/rate-of-chorioamnionitis-more-than-doubled-since-1995/)
- [Frontiers in Medicine 2023 — Clinical chorioamnionitis: where do we stand now?](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1191254/full)
- [Intrauterine inflammation, infection, or both (Triple I): A new concept for chorioamnionitis (Pediatr Neonatol 2017)](https://www.pediatr-neonatol.com/article/S1875-9572(17)30027-X/fulltext)