---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T08:15:28.225115'
end_time: '2026-09-01T08:32:21.991297'
duration_seconds: 1013.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Respiratory Distress Syndrome
  mondo_id: ''
  category: Complex
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
  - claude-opus-5[1m]
  web_search_requests: 11
  num_turns: 47
  total_cost_usd: 5.073160000000001
  session_id: f3d4d878-32af-472a-a78b-2a5851929b0a
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Respiratory Distress Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Respiratory Distress Syndrome** covering all of the
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

# Acute Respiratory Distress Syndrome (ARDS) — Disease Characteristics Research Report

*Compiled 2026-09-01 for the dismech knowledge base. Quick orientation note before the technical part: ARDS is less a disease than a **failure mode** — the lung's version of a blown gasket. Lots of different insults, one shared way of breaking. That shapes everything below: the genetics are thin, the mechanism is rich, and most of the therapeutic wins have come from not making the injury worse rather than from fixing it.*

**Verification status.** Abstracts marked with a blockquote were retrieved verbatim via NCBI E-utilities during this session and the quoted strings are exact substrings of those abstracts. Claims sourced only from web search summaries are flagged **[unquoted — verify before use as an evidence snippet]**. Ontology identifiers marked ✅ were confirmed present in this repository's committed term caches (`cache/<prefix>/terms.csv`); those marked ⚠️ are suggestions that have **not** been resolved and must be checked with OAK before binding.

**Existing KB state.** `kb/disorders/Acute_Respiratory_Distress_Syndrome.yaml` already exists (1,783 lines, created 2026-08-08) with `has_subtypes`, `mechanistic_hypotheses`, `progression`, 11 `pathophysiology` nodes, `histopathology`, `biochemical`, `phenotypes`, `diagnosis`, `treatments`, `discussions`, and `experimental_models`. It has **no** `genetic:`, `environmental:`, `prevalence:`, `animal_models:`, `clinical_trials:`, `definitions:`, `classifications:`, `mappings:`, or `comorbidities:` blocks, and `datasets:` is empty. Sections 2, 5, 9, 10, 12 and 15 below are therefore the highest-yield for enrichment.

---

## 1. Disease Information

### Overview

ARDS is an acute, diffuse, inflammatory lung injury that follows either a direct pulmonary insult (pneumonia, aspiration, inhalation injury, pulmonary contusion) or an indirect systemic one (non-pulmonary sepsis, trauma, pancreatitis, massive transfusion). Increased permeability of the pulmonary microvascular endothelium and the alveolar epithelium produces protein-rich, non-cardiogenic pulmonary oedema and loss of aerated lung, giving bilateral radiographic opacities, intrapulmonary shunt, reduced respiratory-system compliance, and acute hypoxaemic respiratory failure.

The canonical framing from the *Nature Reviews Disease Primers* article (PMID:30872586, Thompson/Matthay/Bellani et al., *Nat Rev Dis Primers* 2019;5:18):

> "The acute respiratory distress syndrome (ARDS) is a common cause of respiratory failure in critically ill patients and is defined by the acute onset of noncardiogenic pulmonary oedema, hypoxaemia and the need for mechanical ventilation. ARDS occurs most often in the setting of pneumonia, sepsis, aspiration of gastric contents or severe trauma and is present in ~10% of all patients in intensive care units worldwide."

And on the heterogeneity that dominates modern thinking (PMID:36070787, Bos & Ware, *Lancet* 2022;400:1145-1156):

> "The pathophysiology of ARDS is complex and involves the activation and dysregulation of multiple overlapping and interacting pathways of injury, inflammation, and coagulation, both in the lung and systemically."

### Definitional history

| Definition | Year | PMID | Key features |
|---|---|---|---|
| Ashbaugh original case series | 1967 | 4143721 | *Lancet* 1967;2:319-23, "Acute respiratory distress in adults" — 12 patients, tachypnoea, hypoxaemia refractory to oxygen, reduced compliance, diffuse infiltrates |
| American-European Consensus Conference (AECC) | 1994 | — | ALI (PaO₂/FiO₂ ≤300) vs ARDS (≤200); PAWP criterion |
| **Berlin Definition** | 2012 | 22797452 | Three severity strata, timing ≤1 week, exclusion of cardiac failure by clinical judgement/echo |
| **New Global Definition** | 2024 | 37487152 | Adds HFNO, SpO₂/FiO₂, ultrasound, resource-limited category |

Berlin (PMID:22797452, *JAMA* 2012;307:2526-33):

> "A draft definition proposed 3 mutually exclusive categories of ARDS based on degree of hypoxemia: mild (200 mm Hg < PaO2/FIO2 ≤ 300 mm Hg), moderate (100 mm Hg < PaO2/FIO2 ≤ 200 mm Hg), and severe (PaO2/FIO2 ≤ 100 mm Hg)"

> "Using the Berlin Definition, stages of mild, moderate, and severe ARDS were associated with increased mortality (27%; 95% CI, 24%-30%; 32%; 95% CI, 29%-34%; and 45%; 95% CI, 42%-48%, respectively; P < .001)"

**The most important recent development in the field** is the New Global Definition (PMID:37487152, Matthay et al., *Am J Respir Crit Care Med* 2024;209(1):37-47, doi:10.1164/rccm.202303-0558WS):

> "The committee made four main recommendations: 1) include high-flow nasal oxygen with a minimum flow rate of ⩾30 L/min; 2) use PaO2:FiO2 ⩽ 300 mm Hg or oxygen saturation as measured by pulse oximetry SpO2:FiO2 ⩽ 315 (if oxygen saturation as measured by pulse oximetry is ⩽97%) to identify hypoxemia; 3) retain bilateral opacities for imaging criteria but add ultrasound as an imaging modality, especially in resource-limited areas; and 4) in resource-limited settings, do not require positive end-expiratory pressure, oxygen flow rate, or specific respiratory support devices."

Rationale, same abstract:

> "Since publication of the 2012 Berlin definition of acute respiratory distress syndrome (ARDS), several developments have supported the need for an expansion of the definition, including the use of high-flow nasal oxygen, the expansion of the use of pulse oximetry in place of arterial blood gases, the use of ultrasound for chest imaging, and the need for applicability in resource-limited settings."

The three categories are **intubated ARDS**, **non-intubated ARDS** (HFNO ≥30 L/min or NIV/CPAP with PEEP ≥5), and **ARDS in resource-limited settings**. A Spanish-language review summarises the trajectory (PMID:38644108, *Med Intensiva* 2024;48:272-281):

> "In 2021, a New Global Definition based on the Berlin definition of ARDS was proposed, which included a category for non-intubated patients, considered the use of SpO2, and established no particular requirement for oxygenation support in regions with limited resources."

Validation work using MIMIC-IV is under way (PMID:38483560, *Intensive Care Med* 2024;50:608-609, "The new global definition of acute respiratory distress syndrome: insights from the MIMIC-IV database") — **[unquoted]**.

**Paediatric ARDS is defined separately** by PALICC-2 (PMID:36661420, *Pediatr Crit Care Med* 2023, "Executive Summary of the Second International Guidelines for the Diagnosis and Management of Pediatric Acute Respiratory Distress Syndrome (PALICC-2)"; epidemiology companion PMID:36661438) — PALICC uses oxygenation index / oxygen saturation index rather than P/F, and does not require bilateral infiltrates. **[unquoted]** This is a strong candidate for a `has_subtypes` entry or a separate `definitions:` block.

### Identifiers

| Resource | Identifier | Status |
|---|---|---|
| MONDO | `MONDO:0006502` — *acute respiratory distress syndrome* | ✅ in `cache/mondo/terms.csv`; already bound in the KB entry |
| HPO | `HP:0033677` — *Acute respiratory distress syndrome* | ✅ in `cache/hp/terms.csv` |
| ICD-10-CM | J80 (Acute respiratory distress syndrome) | ⚠️ verify against `cache/icd10cm/` |
| ICD-11 | CB00 (Acute respiratory distress syndrome) | ⚠️ verify against `cache/icd11f/` |
| MeSH | D012128 (Respiratory Distress Syndrome, Adult / Acute) | ⚠️ not a dismech-bound prefix |
| SNOMED CT | 67782005 | ⚠️ guide-only in this repo |
| OMIM | **Not applicable** — no Mendelian OMIM entry; ARDS is a complex acquired syndrome |
| Orphanet | **Not applicable** — not a rare disease; no ORPHA code |
| NCIT | `NCIT:C3353` (Adult Respiratory Distress Syndrome) | ⚠️ not in the local cache; verify with `runoak -i sqlite:obo:ncit info NCIT:C3353` |

### Synonyms and alternative names

ARDS; acute respiratory distress syndrome; adult respiratory distress syndrome (historical, deprecated — the syndrome occurs in children); shock lung; wet lung; Da Nang lung (historical, Vietnam-war military usage); post-traumatic respiratory insufficiency; acute lung injury (ALI — a *former* milder category retired by the Berlin definition, now subsumed as "mild ARDS"); diffuse alveolar damage (DAD — the *histological* correlate, not a synonym; see §10); non-cardiogenic pulmonary oedema; capillary leak lung injury.

**Curation caution (Named Entity Confusion):** "respiratory distress syndrome" without a qualifier most often refers to **neonatal RDS / hyaline membrane disease** (surfactant deficiency of prematurity, `HP:0002643` *Neonatal respiratory distress* ✅) — a genuinely different disease with a different mechanism. Dataset and literature searches on the bare phrase will return neonatal RDS, and gene-symbol searches on surfactant genes (SFTPB, SFTPC, ABCA3) will return the congenital surfactant deficiencies rather than ARDS. Screen these out.

### Data provenance character

Both. ARDS knowledge derives from (a) **aggregated disease-level resources** — international point-prevalence cohorts (LUNG SAFE), RCT networks (ARDSNet/PETAL, ESICM), consensus definitions; and (b) **individual patient-level data** — EHR-derived cohorts are increasingly central. MIMIC-IV in particular is now used both to validate the global definition (PMID:38483560) and to derive subphenotypes at scale (24,363 ICU admissions in a 2025 ATS abstract; **[unquoted]**). ARDS is unusual among dismech entries in that a large fraction of its biology comes from *secondary analyses of RCT biospecimen repositories* (ARMA, ALVEOLI, FACTT, HARP-2, SAILS) rather than from disease registries.

---

## 2. Etiology

### Disease causal factors

ARDS has **no single cause**. It is a stereotyped response to a heterogeneous set of insults, conventionally split by route:

**Direct (pulmonary) insults — roughly 55-60% of cases**
- Pneumonia (bacterial, viral, fungal) — the single most common precipitant worldwide
- Aspiration of gastric contents (chemical pneumonitis from low-pH, particulate material)
- Inhalation injury (smoke, chlorine, phosgene, high-concentration oxygen)
- Pulmonary contusion (blunt chest trauma)
- Near-drowning
- Pulmonary vasculitis
- Reperfusion injury after lung transplantation or pulmonary embolectomy
- E-cigarette/vaping product use-associated lung injury (EVALI) — note the repo already has `E-Cigarette_or_Vaping_Product_Use-Associated_Lung_Injury.yaml`

**Indirect (extrapulmonary) insults — roughly 40-45%**
- Non-pulmonary sepsis (abdominal, urinary, soft-tissue) — the largest indirect category
- Severe non-thoracic trauma with shock
- Acute pancreatitis
- Massive transfusion / TRALI (transfusion-related acute lung injury)
- Cardiopulmonary bypass
- Drug overdose and drug reactions (amiodarone, bleomycin, salicylates, opioids)
- Burns
- Fat embolism syndrome
- Amniotic fluid embolism / obstetric catastrophe

Ontology suggestion for the precipitant node: the KB entry's node **"Direct Pulmonary or Indirect Systemic Insult"** already carries `conforms_to: "alveolar_capillary_barrier_failure#Alveolar-Capillary Interface Insult"`. That module is the right conformance anchor.

**Not every risk factor confers equal risk.** From the LIPS validation cohort (PMID:20802164, Gajic et al., *Am J Respir Crit Care Med* 2011;183:462-70):

> "The frequency of ALI varied according to predisposing conditions (from 3% in pancreatitis to 26% after smoke inhalation)."

> "Twenty-two hospitals enrolled 5,584 patients at risk. ALI developed a median of 2 (interquartile range 1-4) days after initial evaluation in 377 (6.8%; 148 ALI-only, 229 adult respiratory distress syndrome) patients."

This is a good source for a `RISK_FACTOR` structure and for the point that only a minority of at-risk patients progress — the host response, not the insult alone, determines who gets ARDS.

### Genetic risk factors

**There is no causal gene.** ARDS is polygenic/multifactorial with small effect sizes, and the field has been chronically underpowered — case cohorts number in the low thousands against tens of thousands for common diseases.

**Candidate-gene era (largely unreplicated).** Early candidates were *SFTPB* (surfactant protein B), *ACE*, and *IL6*. The *ACE* insertion/deletion polymorphism rs1799752 (DD genotype → higher serum ACE) has been repeatedly associated with ARDS susceptibility and mortality, with inconsistent replication. **[unquoted]** Treat all candidate-gene ARDS associations as low-confidence unless a GWAS or large meta-analysis supports them.

**GWAS-era findings (the ones with genome-wide support):**

*FLT1* / VEGFR1 (`hgnc:3763`, lowercase per repo convention — ⚠️ verify ID) — a GWAS-significant risk locus; blood *FLT1* expression is higher in ARDS patients than in other critically ill patients, and rs9513106 has been reported to reduce sepsis-associated ARDS risk, plausibly by raising soluble FLT1 and damping VEGF signalling. **[unquoted — from search summary; the primary citation needs to be retrieved and the snippet verified]**

*BORCS5* / *DUSP16* at 12p13.2 — the best-supported novel locus. From PMID:34032881 (Wei et al., *Intensive Care Med* 2021;47:761-771, "Integrative omics provide biological and clinical insights into acute respiratory distress syndrome"):

> "Meta-analyses of ARDS genome-wide association studies were performed with 1250 cases and 1583 controls in Europeans, and 387 cases and 387 controls in African Americans."

> "There was distinct genetic heterogeneity in ARDS between Europeans and African Americans. rs7967111 at 12p13.2 was functionally associated with ARDS susceptibility in Europeans (odds ratio = 1.38; P = 2.15 × 10-8). Expression of two genes annotated at this locus, BORCS5 and DUSP16, was dynamic but ultimately decreased during ARDS development, as well as downregulated in immune cells alongside COVID-19 severity."

Note the explicit ancestry heterogeneity — a genuinely important curation point, and a reason not to generalise European-ancestry loci.

*Mendelian-randomisation-nominated blood transcripts.* From PMID:37922010 (*Intensive Care Med* 2024;50:46-55, "Identification of genetic profile and biomarkers involved in acute respiratory distress syndrome"):

> "A total of 1736 traits, including 1223 blood RNA, 159 plasma proteins, and 354 non-gene phenotypes (classified by Biochemistry, Anthropometry, Disease, Nutrition and Habit, Immunology, and Treatment), exhibited a potentially causal relationship with ARDS development"

> "Regarding candidate blood RNA, four genes were validated, namely TMEM176B, SLC2A5, CDC45, and VSIG8, showing differential expression in blood of ARDS patients compared to controls, as well as dynamic expression in mouse lung tissues."

> "the addition of four blood genes and five immune cell proportions significantly improved the prediction performance of ARDS development, with 0.791 of the area under the curve from receiver-operator characteristic, compared to 0.725 for the basic model"

These are MR-nominated and transcriptionally validated, **not** established causal genes — grade any evidence item accordingly (`SUPPORT` + `directness: INDIRECT` is the honest tag for an MR-derived causal claim).

The field's own assessment of statistical power is captured by the title of an accompanying editorial: PMID:29438627, *Am J Respir Crit Care Med* 2018;197:1373-1374 — "Genome-Wide Association Study in Acute Respiratory Distress Syndrome. Finding the Needle in the Haystack to Advance Our Understanding of Acute Respiratory Distress Syndrome."

Other reported loci, all needing verification before citation: *SELPLG* (P-selectin glycoprotein ligand 1, from an African-ancestry GWAS), *PPFIA1*, *NFE2L2* (NRF2 promoter variants), *MYLK*, *ANGPT2*, *IL1RN*, *NAMPT/PBEF1*, *SOD3*, *TNF* promoter variants, *VEGFA*, *IL10*, *IL8/CXCL8*, *MIF*, *TLR1* (rs5743551). **[all unquoted]**

**COVID-19 severity loci as a partial proxy.** Because COVID-19 ARDS is a large and genetically well-powered subset, the COVID-19 Host Genetics Initiative / GenOMICC loci (*LZTFL1*/3p21.31, *DPP9*, *IFNAR2*, *TYK2*, *OAS1*, *ABO*, *MUC5B*) are frequently invoked. **Curate these under COVID-19, not under generic ARDS** — they are severity loci for one specific viral pneumonia, and the mechanism (interferon signalling, chemokine receptor expression) does not obviously generalise to aspiration or pancreatitis-associated ARDS.

**Rare-variant work** is emerging: "Rare genetic variant risks in patients with sepsis-associated acute respiratory distress syndrome" (PMC13040698) reports burden signals in sepsis-ARDS exomes. **[unquoted — retrieve PMID before use]**

Suggested `inheritance` block: `HP:0010982` **Polygenic inheritance** ⚠️ (verify in `cache/hp/`), used with `relationship_type: SUSCEPTIBILITY` gene typing per the repo's digenic/polygenic guidance.

### Environmental / acquired risk factors

- **Age** — the dominant demographic risk factor. From PMID:16236739 (Rubenfeld et al., *N Engl J Med* 2005;353:1685-93): "The incidence of acute lung injury increased with age from 16 per 100,000 person-years for those 15 through 19 years of age to 306 per 100,000 person-years for those 75 through 84 years of age."
- **Chronic alcohol use disorder** — one of the best-replicated modifiable risks, roughly doubling ARDS risk in at-risk patients; mechanistically attributed to glutathione depletion in the alveolar lining fluid and impaired alveolar epithelial barrier function. **[unquoted]**
- **Cigarette smoking** — associated with ARDS after both trauma and non-pulmonary sepsis; secondhand smoke exposure has also been implicated. **[unquoted]**
- **Chronic ambient air pollution (ozone, PM₂.₅)** — associated with higher ARDS incidence in at-risk cohorts. **[unquoted]** Good ECTO-binding candidate.
- **Hypoalbuminaemia, acidosis, tachypnoea, oxygen requirement, obesity, diabetes** — LIPS "risk modifiers"; notably **diabetes appears protective** in several sepsis cohorts (see below).
- **Iatrogenic**: high tidal volume ventilation, high FiO₂, blood-product transfusion (especially plasma from multiparous donors → TRALI), positive fluid balance, delayed source control.
- **Sex/ethnicity** — ARDS incidence is higher in men in most cohorts; US Black and Hispanic patients have higher ARDS-associated mortality, with the contribution of biology vs. access to care unresolved. **[unquoted]** Curate this carefully as an outcome disparity rather than a biological claim.

### Protective factors

- **Genetic**: no robustly established protective variant. rs9513106 (*FLT1*) has been reported as risk-reducing **[unquoted]**.
- **Diabetes mellitus** — consistently associated with *lower* ARDS incidence in septic patients, an epidemiologically robust and mechanistically unexplained finding (hypotheses include hyperglycaemia-associated neutrophil dysfunction and metformin/thiazolidinedione effects). **[unquoted]** — a strong candidate for a `KNOWLEDGE_GAP` discussion.
- **Vitamin D sufficiency and vasodilator use** — nominated by Mendelian randomisation. From PMID:34032881: "Causal inference implied that comorbidity of inflammatory bowel disease and elevated levels of C-reactive protein and interleukin-10 causally increased ARDS risk, while vitamin D supplementation and vasodilator use ameliorated risk." (Note: the VIOLET RCT of vitamin D₃ in critically ill patients at risk was neutral, so this MR signal is not confirmed by trial evidence — a good `REFUTE`/`SUPPORT` evidence pair.)
- **Lung-protective ventilation applied prophylactically** in patients *without* ARDS reduces ARDS incidence — secondary prevention, see §13.
- **Aspirin** — tested and **negative**. PMID:27179988, *JAMA* 2016, "Effect of Aspirin on Development of ARDS in At-Risk Patients Presenting to the Emergency Department: The LIPS-A Randomized Clinical Trial." **[title verified; abstract not retrieved — do not quote]**

### Gene-environment interactions

The most-cited GxE framings, all needing primary-source verification before use:
- *NFE2L2* (NRF2) promoter haplotypes × oxidative insult (trauma, hyperoxia) — the antioxidant response is the interaction surface.
- *ACE* I/D × sepsis — renin-angiotensin tone modulating pulmonary vascular permeability under an inflammatory challenge.
- Alcohol use × *GSTM1*/glutathione pathway variation — the alveolar glutathione depletion story.
- *SFTPB* variants × pneumonia — surfactant handling under a direct epithelial insult.
- *TLR1* rs5743551 × Gram-positive sepsis.

**[all unquoted]** Also note the general framing from PMID:36070787: ARDS's dependence on "activation and dysregulation of multiple overlapping and interacting pathways" makes single-locus × single-exposure models a poor fit; the field has largely shifted from GxE to **subphenotype** thinking (§6).

---

## 3. Phenotypes

ARDS phenotypes divide cleanly into (a) the defining respiratory phenotype, (b) systemic/multi-organ manifestations, (c) laboratory abnormalities, and (d) long-term sequelae. Frequencies below are approximate and reflect the intubated-ARDS population unless noted.

### Core respiratory phenotypes

| Phenotype | HPO suggestion | Frequency | Onset | Severity | Course |
|---|---|---|---|---|---|
| Acute respiratory distress syndrome (the syndrome itself) | `HP:0033677` ✅ | definitional | acute (≤7 days from insult) | variable | acute/episodic |
| Hypoxaemia | `HP:0012418` ✅ | ~100% (definitional) | acute | mild→severe by P/F stratum | may worsen over 24-72 h |
| Dyspnoea | `HP:0002094` ✅ | very frequent (pre-intubation) | acute | moderate-severe | progressive |
| Tachypnoea | `HP:0002789` ✅ | very frequent | acute | moderate-severe | progressive |
| Respiratory failure | `HP:0002878` ✅ | ~100% | acute | severe | acute |
| Respiratory failure requiring assisted ventilation | `HP:0004887` ✅ | ~76% of ARDS in LUNG SAFE received invasive MV | acute | severe | acute |
| Pulmonary oedema (non-cardiogenic) | `HP:0100598` ✅ | ~100% (pathophysiologically definitional) | acute | severe | resolves with recovery |
| Cyanosis | `HP:0000961` ✅ | occasional; severe hypoxaemia | acute | severe | acute |
| Decreased pulmonary compliance | ⚠️ `HP:0011947`? *Respiratory tract infection* — **no**; check `HP:0002094` family. A precise HPO term for reduced compliance may not exist — likely `preferred_term`-only with no binding | frequent | acute | moderate-severe | acute |
| Pulmonary fibrosis (fibroproliferative phase) | `HP:0002206` ✅ | ~20-40% of persistent ARDS shows fibroproliferation | subacute (≥day 7) | variable | may be progressive or resolve |

**Quality-of-life note per phenotype:** the acute respiratory phenotypes are experienced under sedation in most intubated patients; the QoL burden is dominated by post-ICU sequelae (below) rather than by the acute hypoxaemia itself.

### Systemic / extrapulmonary phenotypes

- **Shock requiring vasopressors** — markedly more prevalent in the hyperinflammatory subphenotype (PMID:24853585: "a higher prevalence of vasopressor use").
- **Metabolic acidosis** `HP:0001942` ✅ / **lactic acidosis** `HP:0003128` ✅ — PMID:24853585 notes "lower serum bicarbonate concentrations" in the hyperinflammatory class.
- **Acute kidney injury** ⚠️ `HP:0001919` (Acute kidney injury) — verify. A very common co-failing organ; drives RRT use.
- **Delirium / ICU-acquired encephalopathy** ⚠️ `HP:0031258`? verify.
- **ICU-acquired weakness / critical illness polyneuromyopathy** ⚠️ — relevant to the neuromuscular-blockade debate (§12).
- **Right ventricular dysfunction / acute cor pulmonale** ⚠️ — present in ~20-25% of moderate-severe ARDS; a mechanistically distinct "RV-protective" management strand.
- **Barotrauma / pneumothorax** ⚠️ `HP:0002107` (Pneumothorax) — verify. Quantified in the ART trial (PMID:28973363): "increased the risk of pneumothorax requiring drainage (3.2% vs 1.2%...) and the risk of barotrauma (5.6% vs 1.6%...)".

### Laboratory abnormalities (LOINC-codable)

- PaO₂/FiO₂ ratio ≤300 mmHg (LOINC 50984-4 ⚠️) — the defining measure
- SpO₂/FiO₂ ratio ≤315 — the new global-definition surrogate
- Elevated plasma IL-6, IL-8 (CXCL8), sTNFR-1, sRAGE, angiopoietin-2, PAI-1, surfactant protein D, ferritin
- Reduced protein C
- Elevated bronchoalveolar lavage protein / oedema-fluid-to-plasma protein ratio >0.65 (the classic bedside discriminator of non-cardiogenic oedema)
- Reduced serum bicarbonate, elevated lactate

These belong in a `biochemical:` block with `BiomarkerReadout` links — the entry already has one; adding `reference_ranges` with `interpretation_bands` would be a natural extension, though most ARDS biomarkers lack consensus clinical cut-points (flag rather than invent).

### Long-term / survivorship phenotypes

This is where the durable morbidity lives. From PMID:21470008 (Herridge et al., *N Engl J Med* 2011;364:1293-304, "Functional disability 5 years after acute respiratory distress syndrome"):

> "At 5 years, the median 6-minute walk distance was 436 m (76% of predicted distance) and the Physical Component Score on the Medical Outcomes Study 36-Item Short-Form Health Survey was 41 (mean norm score matched for age and sex, 50)."

> "With respect to this score, younger patients had a greater rate of recovery than older patients, but neither group returned to normal predicted levels of physical function at 5 years. Pulmonary function was normal to near-normal."

> "Exercise limitation, physical and psychological sequelae, decreased physical quality of life, and increased costs and use of health care services are important legacies of severe lung injury."

The striking finding — **pulmonary function normalises but physical function does not** — is a first-class curation point: the long-term disability of ARDS is largely extrapulmonary (muscle wasting, neuropathy, cognitive impairment, PTSD/depression/anxiety, i.e. post-intensive-care syndrome), not a residual lung defect. QoL instruments in the literature: SF-36 (Physical and Mental Component Scores), EQ-5D, HADS, IES-R, and the 6-minute walk test as a functional endpoint.

---

## 4. Genetic / Molecular Information

**Causal genes: none.** ARDS has no Mendelian form and no OMIM entry. Do not curate `relationship_type: CAUSATIVE` gene relationships.

**Pathogenic variants: not applicable.** There is no ACMG/AMP variant classification framework for ARDS; ClinVar contains no ARDS-associated pathogenic variants. All genetic contributions are common-variant susceptibility alleles (MAF typically >5%) with odds ratios in the 1.2-1.5 range — see the *BORCS5*/*DUSP16* OR of 1.38 (PMID:34032881). Somatic variation plays no role.

**For the `genetic:` block, curate as susceptibility rather than causation:**

| Gene | HGNC (⚠️ verify all) | Relationship type | Evidence tier |
|---|---|---|---|
| *FLT1* | `hgnc:3763` | `SUSCEPTIBILITY` | GWAS-significant; functional support via sFLT1/VEGF |
| *BORCS5* | ⚠️ | `SUSCEPTIBILITY` | GWAS-significant locus 12p13.2 (rs7967111), European ancestry only |
| *DUSP16* | ⚠️ | `SUSCEPTIBILITY` | same locus; MAPK phosphatase — mechanistically plausible |
| *ACE* | `hgnc:2707` ⚠️ | `SUSCEPTIBILITY` | candidate-gene era, inconsistent replication |
| *SFTPB* | ⚠️ | `SUSCEPTIBILITY` | candidate-gene era; watch for neonatal-RDS confusion |
| *NFE2L2* | ⚠️ | `MODIFIER` | oxidative-stress response |
| *TMEM176B, SLC2A5, CDC45, VSIG8* | ⚠️ | `SUSCEPTIBILITY` | MR-nominated + transcriptionally validated (PMID:37922010) |

**Modifier genes:** the concept applies loosely — most reported loci modify severity/mortality rather than incidence, and the two are rarely separated cleanly in the literature.

**Epigenetics.** DNA methylation and histone-modification changes have been described in ARDS and sepsis leukocytes (notably at *HIF1A*, *TNF*, and interferon-response loci) and NET-derived extracellular histones are directly cytotoxic to pulmonary endothelium (§6). ENCODE/Roadmap have no ARDS-specific tracks; the useful epigenomic resources are sepsis leukocyte methylome studies. **[unquoted]**

**Chromosomal abnormalities:** not applicable.

**Pharmacogenomics:** no established ARDS pharmacogenomic markers. The closest analogue is *predictive enrichment by subphenotype* rather than by genotype (§12, HARP-2/simvastatin).

---

## 5. Environmental Information

This section is entirely absent from the current KB entry and is one of the clearest gaps. Candidate `environmental:` entries, each needing an `influences_mechanisms` link to a named pathophysiology node (remember: **bare-name targets**, not `pathophysiology#Name`):

| Exposure | Suggested target node | `environmental_effect` | ECTO candidate |
|---|---|---|---|
| Gastric-contents aspiration | Direct Pulmonary or Indirect Systemic Insult | `TRIGGERS` | ⚠️ search ECTO for aspiration; may be unbindable |
| Smoke inhalation | Direct Pulmonary or Indirect Systemic Insult | `TRIGGERS` | ⚠️ ECTO "exposure to smoke" |
| Chronic alcohol consumption | Alveolar-Capillary Barrier Disruption | `PREDISPOSES` | ⚠️ ECTO ethanol exposure |
| Cigarette smoking | Alveolar Macrophage and Cytokine Activation | `PREDISPOSES` | ⚠️ check for an existing tobacco/cigarette binding elsewhere in the KB — run `just environmental-term-audit` for reuse candidates |
| Ambient particulate matter / ozone | Neutrophil Oxidative and Proteolytic Injury | `PREDISPOSES` | ⚠️ ECTO air-pollutant exposure |
| Chlorine / phosgene inhalation | Direct Pulmonary or Indirect Systemic Insult | `TRIGGERS` | ⚠️ |
| Hyperoxia (high FiO₂) | Neutrophil Oxidative and Proteolytic Injury | `EXACERBATES` | ⚠️ ECTO oxygen exposure |
| High tidal volume mechanical ventilation | Ventilator-Induced Lung Injury | `EXACERBATES` | likely unbindable — record the ECTO search in `review_notes:` |
| Blood-product transfusion (TRALI) | Alveolar-Capillary Barrier Disruption | `TRIGGERS` | ⚠️ |

**Repo-specific caution:** `check-environmental-evidence` is now a hard gate — every `environmental[]` entry needs its own top-level `evidence:` block (evidence on `influences_mechanisms` does not count), or a `review_notes:` beginning with the exact sentence `Left deliberately uncited.` followed by ≥20 words describing the searches run.

### Lifestyle factors

Alcohol use disorder, smoking, obesity (paradoxically associated with *lower* ARDS mortality in several cohorts — the "obesity paradox"), malnutrition/hypoalbuminaemia, and vitamin D status. **[unquoted]**

### Infectious agents

ARDS is the most common severe endpoint of lower respiratory tract infection. Organisms to consider for `NCBITaxon` binding:

| Agent | NCBITaxon (⚠️ verify) | Note |
|---|---|---|
| *Streptococcus pneumoniae* | 1313 | Leading bacterial cause; the repo has `Pneumococcal_Pneumonia.yaml` |
| SARS-CoV-2 | 2697049 | The dominant ARDS cause 2020-2022; drove the global-definition revision |
| Influenza A virus | 11320 | Seasonal and pandemic ARDS |
| *Legionella pneumophila* | 446 | |
| *Staphylococcus aureus* | 1280 | Including community-acquired MRSA necrotising pneumonia |
| *Pneumocystis jirovecii* | 42068 | The repo has `Pneumocystis_Pneumonia.yaml` |
| MERS-CoV | 1335626 | The repo has `Middle_East_Respiratory_Syndrome.yaml` |
| Respiratory syncytial virus | 11250 | Repo entry exists |
| Human metapneumovirus | 162145 | Repo entry exists |
| *Mycoplasma pneumoniae* | 2104 | Repo entry exists |

**This is a large comorbidity-curation opportunity:** ARDS is the shared severe outcome of at least six diseases already in `kb/disorders/`. A `Grouping` (e.g. "ARDS-precipitating infections") or a set of `sequelae` edges from each infection entry to the ARDS entry would make that convergence machine-queryable.

Non-infectious triggers that reach the same node: acute pancreatitis, polytrauma, burns, cardiopulmonary bypass, amniotic fluid embolism.

---

## 6. Mechanism / Pathophysiology

### The ordered causal chain

The mechanism is best read as a single trunk with three branches at the outcome. Steps marked **[inferred]** are extrapolated from model systems or human autopsy rather than demonstrated longitudinally in living patients.

1. **A direct pulmonary or indirect systemic insult delivers PAMPs and/or DAMPs to the alveolar-capillary interface**, either from the airspace side (pneumonia, aspirate, inhaled toxicant) or the vascular side (bacteraemia, circulating cytokines, activated neutrophils from a distant injury). → *leads to*
2. **Pattern-recognition receptor engagement on alveolar macrophages and alveolar epithelium** — TLR4 (LPS), TLR2, TLR3/7/9 (viral nucleic acid), RAGE, and NLRP3 inflammasome assembly — **activates NF-κB and drives transcription of TNF, IL-1β, IL-6, IL-8/CXCL8, and IL-18.** → *results in*
3. **Chemokine-gradient-driven recruitment and margination of circulating neutrophils into the pulmonary microvasculature and then the alveolar space.** The lung's capillary bed is narrower than a neutrophil, so this step is partly mechanical: activated, stiffened neutrophils are physically retained. → *results in*
4. **Neutrophil degranulation and NETosis**, releasing myeloperoxidase, neutrophil elastase, matrix metalloproteinases, reactive oxygen and nitrogen species, and extracellular chromatin decorated with citrullinated histones. → *causes*, in parallel:
   - 4a. **Proteolytic and oxidative destruction of endothelial tight and adherens junctions (VE-cadherin, occludin, claudin-5) and shedding of the endothelial glycocalyx** (syndecan-1, heparan sulphate), via heparanase and MMPs. Extracellular histones from NETs are directly cytotoxic to pulmonary endothelial cells. **[inferred, mostly in vitro/model]**
   - 4b. **Injury and death of alveolar epithelium**, disproportionately the thin, gas-exchanging **type I pneumocytes** (which cover ~95% of alveolar surface and are poorly regenerative), with necrosis, apoptosis, and pyroptosis.
5. **Loss of alveolar-capillary barrier integrity** — the two surfaces fail together, and the barrier's normal 1-µm-thick sandwich becomes leaky in both directions. → *results in*
6. **Flooding of the alveolar space with protein-rich oedema fluid** (oedema-fluid/plasma protein ratio >0.65), because plasma proteins now cross freely and the oncotic gradient that normally keeps the airspace dry is abolished. → *compounded by*
7. **Failure of alveolar fluid clearance**: injured **type II pneumocytes** lose apical ENaC and basolateral Na⁺/K⁺-ATPase function, so the pump that would drain the alveolus is disabled at exactly the moment the leak opens. Impaired clearance is one of the strongest single predictors of death. **[inferred from ex vivo human lung and clinical oedema-fluid sampling]**
8. **Type II pneumocyte injury also collapses surfactant production and increases surfactant inactivation by plasma proteins**, raising alveolar surface tension. → *leads to*
9. **Alveolar collapse and de-recruitment, most severe in dependent lung regions** (gravitational superimposed pressure) → the "baby lung": a small volume of aerated, compliant tissue receiving the whole tidal volume.
10. **Intrapulmonary shunt** — perfused but unventilated alveoli — plus dead-space ventilation from microvascular thrombosis, giving **severe hypoxaemia refractory to supplemental oxygen** and reduced respiratory-system compliance. This is the clinical syndrome.
11. **In parallel from step 4: intra-alveolar coagulation.** Tissue factor from injured epithelium and alveolar macrophages initiates extrinsic coagulation in the airspace; PAI-1 rises and protein C falls, suppressing fibrinolysis. → **fibrin-rich hyaline membranes line the alveolar ducts** — the pathological hallmark of diffuse alveolar damage.
12. **Mechanical ventilation feeds back into step 4** (ventilator-induced lung injury). Because the aerated compartment is small, a "normal" tidal volume delivers regional overdistension (volutrauma) while repeated opening and closing of unstable units produces shear injury (atelectrauma); both amplify cytokine release (biotrauma), which spills systemically. This is the loop that low-tidal-volume ventilation breaks — and the reason the single most effective ARDS therapy is a *reduction* in intervention.
13. **Systemic spillover of alveolar cytokines and translocated bacterial products drives distal organ injury** — kidney, liver, brain — producing multiple organ dysfunction syndrome, which is what most ARDS patients actually die of.
14. **Branch point at ~day 7.** Three trajectories:
    - **14a. Resolution.** Pro-resolving mediators (lipoxins, resolvins, protectins), macrophage efferocytosis of apoptotic neutrophils, macrophage repolarisation toward a reparative phenotype, restored ENaC/Na⁺-K⁺-ATPase-mediated fluid clearance, and **type II pneumocyte proliferation and transdifferentiation into type I cells** to re-epithelialise the denuded basement membrane. Note the asymmetry: the AT2 cell is both a primary victim and the progenitor responsible for repair.
    - **14b. Fibroproliferation.** Persistent injury, TGF-β signalling, fibroblast recruitment and myofibroblast differentiation, collagen deposition in the alveolar septa and airspace → organising fibrosis, persistent low compliance, ventilator dependence. Candidate `conforms_to` target: the `fibrotic_response` module.
    - **14c. Death**, usually from refractory MODS or the underlying precipitant, not from refractory hypoxaemia (which accounts for only a minority of ARDS deaths).

### Mapping to the existing KB nodes

The existing 11 pathophysiology nodes cover this chain well. Mapping:

| Chain step | Existing node |
|---|---|
| 1 | Direct Pulmonary or Indirect Systemic Insult (`biological_scale: TISSUE`) |
| 2 | Alveolar Macrophage and Cytokine Activation (CELLULAR) |
| 3-4 | Neutrophil Oxidative and Proteolytic Injury (CELLULAR) |
| (metabolic layer) | Immunometabolic Reprogramming and Mitochondrial Dysfunction (CELLULAR) |
| 12 | Ventilator-Induced Lung Injury (TISSUE) |
| 5 | Alveolar-Capillary Barrier Disruption (TISSUE) |
| 11 | Intra-Alveolar Coagulation and Fibrin Deposition (TISSUE) |
| 6-9 | Protein-Rich Alveolar Edema and Loss of Aerated Lung (TISSUE) |
| 10 | Shunt Physiology and Hypoxemic Respiratory Failure (ORGANISM) |
| 14a | Resolution and Alveolar Repair (TISSUE) |
| 14b | Fibroproliferative Remodeling and Fibrosis (TISSUE) |

**Gaps in the current node set worth considering:** step 7 (impaired alveolar fluid clearance / ENaC–Na⁺-K⁺-ATPase failure) and step 8 (surfactant dysfunction) are currently folded into the oedema node but are mechanistically distinct, separately measurable, and separately druggable (β₂-agonists targeted step 7; exogenous surfactant targeted step 8 — both failed in trials, which is itself informative). Step 13 (systemic spillover → MODS) has no node, despite being the dominant cause of death.

### Molecular pathways (GO / KEGG / Reactome)

| Process | GO term | Cache status |
|---|---|---|
| inflammatory response | `GO:0006954` | ✅ |
| toll-like receptor 4 signaling pathway | `GO:0034142` | ✅ |
| toll-like receptor signaling pathway | `GO:0002224` | ✅ |
| NLRP3 inflammasome complex assembly | `GO:0044546` | ✅ |
| NLRP3 inflammasome complex (CC) | `GO:0072559` | ✅ |
| neutrophil chemotaxis | `GO:0030593` | ✅ |
| leukocyte migration involved in inflammatory response | `GO:0002523` | ✅ |
| cytokine production involved in inflammatory response | `GO:0002534` | ✅ |
| interleukin-6 production | `GO:0032635` | ✅ |
| tumor necrosis factor production | `GO:0032640` | ✅ |
| cytokine-mediated signaling pathway | `GO:0019221` | ✅ |
| response to oxidative stress | `GO:0006979` | ✅ |
| coagulation | `GO:0050817` | ✅ |
| surfactant homeostasis | `GO:0043129` | ✅ |
| fibroblast proliferation | `GO:0048144` | ✅ |
| extracellular matrix organization | `GO:0030198` | ✅ |
| extracellular matrix disassembly | `GO:0022617` | ✅ |
| wound healing | `GO:0042060` | ✅ |
| positive regulation of NF-κB transcription factor activity | ⚠️ `GO:0043123` (label: *positive regulation of canonical NF-kappaB signal transduction*) | verify |
| neutrophil extracellular trap formation | ⚠️ `GO:1990266`? | verify |
| sodium ion transmembrane transport / ENaC | ⚠️ | verify |
| efferocytosis / apoptotic cell clearance | ⚠️ `GO:0043277`? | verify |

KEGG/Reactome anchors (not dismech-bound, but useful for the report): KEGG hsa04620 (Toll-like receptor signaling), hsa04064 (NF-κB signaling), hsa04621 (NOD-like receptor signaling), hsa04610 (Complement and coagulation cascades), hsa04370 (VEGF signaling), hsa04350 (TGF-β signaling); Reactome R-HSA-168256 (Immune System), R-HSA-140877 (Formation of Fibrin Clot).

### Cellular processes and cell types

| Cell type | CL term | Cache status | Role |
|---|---|---|---|
| alveolar macrophage | `CL:0000583` | ✅ | Sentinel; PRR sensing; cytokine amplification; later, efferocytosis and repair |
| neutrophil | `CL:0000775` | ✅ | Principal effector of tissue destruction; NETosis |
| pulmonary alveolar type 1 cell | `CL:0002062` | ✅ | Gas exchange surface; primary casualty; poorly regenerative |
| pulmonary alveolar type 2 cell | `CL:0002063` | ✅ | Surfactant production; ENaC-mediated fluid clearance; **progenitor for AT1 repair** |
| pulmonary alveolar epithelial cell (generic) | `CL:0000322` | ✅ | Use when AT1/AT2 not distinguished |
| capillary endothelial cell | `CL:0002144` | ✅ | Barrier; glycocalyx; adhesion-molecule display |
| fibroblast of lung | `CL:0002553` | ✅ | Fibroproliferative phase |
| myofibroblast cell | `CL:0000186` | ✅ | Collagen deposition |
| platelet | `CL:0000233` | ✅ | Platelet-neutrophil aggregates; microthrombosis |
| monocyte | `CL:0000576` | ✅ | Recruited; differentiates into inflammatory macrophage |

Cellular processes: pyroptosis, necroptosis, apoptosis, NETosis, efferocytosis, epithelial-mesenchymal transition (contested in ARDS), autophagy, ferroptosis (an active 2023-2025 research area in ALI models — **[unquoted]**), mitochondrial dysfunction and metabolic reprogramming toward aerobic glycolysis in alveolar macrophages.

### Protein dysfunction, metabolic changes, biochemical abnormalities

- **Surfactant proteins B and C**: reduced production and functional inactivation by leaked plasma proteins → raised alveolar surface tension.
- **VE-cadherin / claudin-5 / occludin / ZO-1**: junctional disassembly under RhoA/ROCK signalling and tyrosine phosphorylation.
- **Angiopoietin-2 vs Angiopoietin-1 / Tie2**: Ang-2 rises, antagonises Ang-1's barrier-stabilising Tie2 signal. Ang-2 is among the best-performing ARDS biomarkers.
- **RAGE (AGER)**: soluble RAGE released from injured AT1 cells — a relatively specific marker of alveolar epithelial injury.
- **Endothelial glycocalyx**: heparanase- and MMP-mediated shedding; syndecan-1 as the circulating marker.
- **Tissue factor ↑, protein C ↓, PAI-1 ↑, thrombomodulin shed**: the procoagulant/antifibrinolytic shift in the airspace.
- **ENaC (SCNN1A/B/G) and Na⁺/K⁺-ATPase (ATP1A1/ATP1B1)**: downregulated/internalised → alveolar fluid clearance failure.
- **Metabolic**: alveolar macrophage glycolytic switch; mitochondrial ROS; released mitochondrial DNA acting as a DAMP via TLR9 and cGAS-STING (the repo has a `cgas_sting_pathway_activation` module — a plausible additional conformance target).

### Immune system involvement

ARDS is a disorder of **dysregulated innate immunity** — not autoimmunity and not immunodeficiency, though both can precipitate it. The central tension is that the neutrophil response required to clear a pathogen is the same response that destroys the barrier; the syndrome is what happens when that response is neither proportionate nor properly terminated. Resolution failure — not just excess activation — is increasingly seen as the therapeutic target (PMID:36070787: "Resolution of inflammation is a coordinated process that requires downregulation of proinflammatory pathways and upregulation of anti-inflammatory pathways.").

Adaptive immunity contributes via regulatory T cells (which promote resolution and AT2 proliferation in murine models) and, in viral ARDS, via CD8⁺ T-cell-mediated epithelial killing. The repo's `cytokine_storm_hyperinflammation` module is a candidate conformance target for the hyperinflammatory subphenotype specifically.

### Tissue damage mechanisms

Oxidative stress (neutrophil NADPH oxidase, MPO-derived hypochlorous acid, mitochondrial ROS, hyperoxia), proteolysis (elastase, MMP-2/9), mechanical strain (volutrauma, atelectrauma), microvascular thrombosis with regional ischaemia, complement activation (C5a), and — in the late phase — fibrosis.

### Subphenotypes: the dominant modern framework

This is the single most consequential idea in ARDS biology since low-tidal-volume ventilation, and it deserves its own `mechanistic_hypotheses` treatment. From PMID:24853585 (Calfee et al., *Lancet Respir Med* 2014;2:611-20):

> "Independent latent class models indicated that a two-class (ie, two subphenotype) model was the best fit for both cohorts. In both cohorts, we identified a hyperinflammatory subphenotype (phenotype 2) that was characterised by higher plasma concentrations of inflammatory biomarkers, a higher prevalence of vasopressor use, lower serum bicarbonate concentrations, and a higher prevalence of sepsis than phenotype 1."

> "In the ALVEOLI cohort, the effects of ventilation strategy (high PEEP vs low PEEP) on mortality, ventilator-free days and organ failure-free days differed by phenotype (p=0·049 for mortality, p=0·018 for ventilator-free days, p=0·003 for organ-failure-free days)."

Replicated in a non-US population with a **pharmacological** treatment interaction (PMID:30078618, Calfee et al., *Lancet Respir Med* 2018;6:691-698):

> "a two-class (two subphenotype) model was an improvement over a one-class model (p<0·0001), with 353 (65%) patients in the hypoinflammatory subphenotype group and 186 (35%) in the hyperinflammatory subphenotype group."

> "Patients with the hyperinflammatory subphenotype had fewer ventilator-free days (median 2 days [IQR 0-17] vs 18 [IQR 0-23]; p<0·0001), fewer non-pulmonary organ failure-free days (15 [0-25] vs 27 [21-28]; p<0·0001), and higher 28-day mortality (73 [39%] vs 59 [17%]; p<0·0001) than did those with the hypoinflammatory subphenotype."

> "Although HARP-2 found no difference in 28-day survival between placebo and simvastatin, significantly different survival was identified across patients stratified by treatment and subphenotype (p<0·0001). Specifically, within the hyperinflammatory subphenotype, patients treated with simvastatin had significantly higher 28-day survival than did those given placebo (p=0·008)."

That last result is the field's proof of concept for **predictive enrichment**: a drug that "failed" in the whole population worked in a third of it.

A 2025 EHR-scale replication in MIMIC-IV (24,363 ICU admissions) reported 90-day mortality of 40.8% (hyperinflammatory) vs 19.1% (hypoinflammatory), adjusted OR 2.19 (95% CI 2.05-2.35), with invasive ventilation in 80.0% vs 37.5% (adjusted OR 5.67, 95% CI 5.32-6.04). **[unquoted — ATS 2025 abstract A26-18; retrieve the peer-reviewed version before citing]**

Complementary phenotyping axes to record as separate hypothesis groups:
- **Transcriptomic**: "reactive" vs "uninflamed" (Bos et al.) — largely concordant with the LCA classes. **[unquoted]**
- **Radiographic/physiologic**: focal vs diffuse loss of aeration, with a reported (and contested) differential response to recruitment. **[unquoted]**
- **Direct vs indirect insult**: distinct biomarker profiles (higher sRAGE/SP-D in direct, higher Ang-2/vWF in indirect). **[unquoted]**
- **COVID-19 vs non-COVID ARDS**: initially claimed as a distinct entity ("L" vs "H" phenotypes); the ESICM guideline's position is that COVID-19 ARDS should be managed as ARDS. The mechanistic distinctions that survived scrutiny are the degree of pulmonary microthrombosis and the duration of the illness.

### Molecular profiling

- **Transcriptomics**: whole-blood RNA-seq/microarray from ARDS and sepsis cohorts (GEO — search "ARDS", "acute lung injury", "sepsis whole blood"). The repo's `datasets:` block for ARDS is empty; `just discover-datasets Acute_Respiratory_Distress_Syndrome` followed by manual relevance triage is the right first move. **Watch the Named Entity Confusion trap**: searching "RDS" or surfactant genes will surface neonatal RDS cohorts.
- **Single-cell**: the Human Cell Atlas lung and several COVID-19 autopsy atlases (e.g. Delorey et al., Melms et al., *Nature* 2021) provide alveolar-cell-resolution ARDS data, including the description of transitional/aberrant basaloid AT2-derived states in fibrotic lung. **[unquoted]**
- **Proteomics**: plasma and BAL/oedema-fluid proteomics from ARDSNet biorepositories; PRIDE/ProteomeXchange deposits exist.
- **Metabolomics/lipidomics**: eicosanoid and specialised pro-resolving mediator profiling in BAL; Metabolomics Workbench holds sepsis/ARDS studies. **[unquoted]**
- **Functional genomics screens**: no ARDS-specific CRISPR screens; endothelial-barrier and inflammasome screens are the closest proxies.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary organ:** lung (`UBERON:0002048` ✅), bilaterally and by definition — unilateral opacities do not satisfy any ARDS definition. Injury is **bilateral but spatially heterogeneous**, with a gravitational gradient: dependent (dorsal, in a supine patient) regions collapse and consolidate while non-dependent regions remain aerated and are preferentially overdistended by positive-pressure ventilation. This spatial asymmetry is the entire rationale for prone positioning.

Relevant UBERON terms:

| Structure | UBERON | Cache |
|---|---|---|
| lung | `UBERON:0002048` | ✅ |
| alveolus of lung | `UBERON:0002299` | ✅ |
| lung parenchyma | `UBERON:0008946` | ✅ |
| lung epithelium | `UBERON:0000115` | ✅ |
| pulmonary capillary | `UBERON:0016405` | ✅ |
| lung mesenchyme | `UBERON:0004883` | ✅ |
| lung connective tissue | `UBERON:0000114` | ✅ |
| respiratory system | `UBERON:0001004` | ✅ |
| diaphragm | `UBERON:0001103` | ✅ (relevant to ventilator-induced diaphragmatic dysfunction) |
| blood-air barrier / alveolar septum | ⚠️ `UBERON:0004802`? verify |

**Secondary organ involvement:** kidney (AKI in ~40-50%), cardiovascular system (shock; right ventricular strain and acute cor pulmonale from hypoxic vasoconstriction plus raised transpulmonary pressure), brain (delirium, later cognitive impairment), liver (shock liver, cholestasis), skeletal muscle (ICU-acquired weakness), gut (barrier failure and translocation, both cause and consequence), and haematologic (DIC).

**Body systems:** respiratory (primary), cardiovascular, renal, nervous, musculoskeletal, immune/haematologic.

### Tissue and cell level

Alveolar epithelium (simple squamous AT1 + cuboidal AT2), pulmonary capillary endothelium, alveolar basement membrane, interstitial connective tissue, and — in the fibroproliferative phase — interstitial fibroblasts/myofibroblasts. Airway epithelium proximal to the alveolus is relatively spared in indirect ARDS but heavily involved in inhalational and aspiration injury. See the CL table in §6.

### Subcellular level

| Compartment | GO CC (⚠️ verify all) | Relevance |
|---|---|---|
| mitochondrion | `GO:0005739` | ROS, mtDNA release as DAMP, metabolic reprogramming |
| lamellar body | `GO:0042599` | Surfactant storage in AT2 cells |
| NLRP3 inflammasome complex | `GO:0072559` ✅ | Caspase-1 activation, IL-1β maturation |
| tight junction | `GO:0005923` | Barrier |
| adherens junction | `GO:0005912` | VE-cadherin |
| cell surface / glycocalyx | ⚠️ | Syndecan/heparan sulphate shedding |
| endoplasmic reticulum | `GO:0005783` | ER stress in injured epithelium |
| extracellular matrix | `GO:0031012` ✅ | Basement membrane denudation, later collagen deposition |

### Localization and lateralization

**Bilateral, by definition.** Distribution within each lung is heterogeneous and gravity-dependent; CT typically shows a dorsobasal gradient from normally aerated (ventral) → ground-glass → dense consolidation (dorsal). Direct-insult ARDS tends toward more focal, asymmetric consolidation; indirect ARDS toward diffuse, symmetric ground-glass. This distinction is the basis of the focal/diffuse morphological phenotype.

---

## 8. Temporal Development

### Onset

- **Age:** any age from neonate to elderly, but incidence rises steeply with age (PMID:16236739: 16 → 306 per 100,000 person-years from ages 15-19 to 75-84). Paediatric ARDS is defined separately (PALICC-2).
- **Pattern:** **acute**, by definition. The Berlin and Global definitions require onset **within one week of a known clinical insult or new/worsening respiratory symptoms**. In practice, from LUNG SAFE, most ARDS is present early: "more than 75% being diagnosed with ARDS in the first 48 hours of admission to the ICU" **[from search summary of the companion paper PMID:27608629 — unquoted]**. From LIPS (PMID:20802164): "ALI developed a median of 2 (interquartile range 1-4) days after initial evaluation."
- **Suggested `OnsetDescriptor`:** `onset_category` acute; `temporality: ACUTE`.

### Stages

The classical three overlapping histopathological phases of diffuse alveolar damage:

1. **Exudative phase (days 0-7).** Interstitial and alveolar oedema, neutrophil infiltration, hyaline membranes, capillary congestion, AT1 necrosis. Maximal hypoxaemia and lowest compliance.
2. **Proliferative phase (days ~7-21).** AT2 hyperplasia, fibroblast and myofibroblast proliferation, organisation of intra-alveolar exudate, granulation tissue. Oedema begins to clear; dead space stays high.
3. **Fibrotic phase (≥ ~2-3 weeks, in a subset).** Collagen deposition, architectural distortion, cyst formation, honeycombing on CT. Associated with prolonged ventilation and higher mortality.

These are **overlapping, not sequential**, and coexist regionally within the same lung. Many patients never reach phase 3.

### Progression rate and course

- Rapid: severity is usually maximal within the first 24-72 hours.
- Course pattern: **acute, self-limited-or-fatal** rather than relapsing or chronic. There is no "relapsing-remitting ARDS."
- Duration: median duration of mechanical ventilation in survivors, by Berlin stratum (PMID:22797452): "increased median duration of mechanical ventilation in survivors (5 days; interquartile [IQR], 2-11; 7 days; IQR, 4-14; and 9 days; IQR, 5-17, respectively; P < .001)" for mild, moderate, and severe.

### Remission patterns

Recovery is treatment-supported rather than spontaneous in most cases — the intervention keeps the patient alive while the resolution machinery (step 14a) does the actual work. Pulmonary function typically recovers to normal or near-normal by 6-12 months (PMID:21470008: "Pulmonary function was normal to near-normal"), while physical function does not.

### Critical periods

- **The pre-ARDS window (hours to ~2 days from the precipitating insult):** the only interval in which *primary* prevention is possible — this is the target of LIPS-based enrichment and of prophylactic lung-protective ventilation.
- **First 48 hours of ARDS:** the window in which prone positioning (PROSEVA enrolled within 36 h of ARDS onset), neuromuscular blockade (ACURASYS: within 48 h), and low-tidal-volume ventilation deliver their benefit.
- **~24 hours of established moderate-severe ARDS:** the DEXA-ARDS enrolment window for dexamethasone.
- **Day 7-14:** the branch point between resolution and fibroproliferation; the theoretical window for antifibrotic intervention, currently with no proven therapy.

---

## 9. Inheritance and Population

### Epidemiology

**Incidence.** The two anchor estimates:

United States, population-based (PMID:16236739, Rubenfeld et al., *N Engl J Med* 2005;353:1685-93):

> "the crude incidence of acute lung injury was 78.9 per 100,000 person-years and the age-adjusted incidence was 86.2 per 100,000 person-years."

> "We estimate that each year in the United States there are 190,600 cases of acute lung injury, which are associated with 74,500 deaths and 3.6 million hospital days."

Note this is **acute lung injury** under the pre-Berlin AECC definition and therefore includes what is now "mild ARDS"; it is not directly comparable to Berlin-ARDS incidence, and later US estimates using narrower criteria run lower (~34-64 per 100,000 person-years). **[unquoted]** Record this definitional caveat in `notes:` — comparing incidences across definitions is one of the easiest errors to make here.

**ICU period prevalence — the LUNG SAFE benchmark** (PMID:26903337, Bellani et al., *JAMA* 2016;315:788-800):

> "Of 29,144 patients admitted to participating ICUs, 3022 (10.4%) fulfilled ARDS criteria."

> "The period prevalence of mild ARDS was 30.0% (95% CI, 28.2%-31.9%); of moderate ARDS, 46.6% (95% CI, 44.5%-48.6%); and of severe ARDS, 23.4% (95% CI, 21.7%-25.2%). ARDS represented 0.42 cases per ICU bed over 4 weeks and represented 10.4% (95% CI, 10.0%-10.7%) of ICU admissions and 23.4% of patients requiring mechanical ventilation."

**Suggested `prevalence:` records** (structured slots, not the deprecated `percentage`):

```yaml
prevalence:
- population: ICU admissions, 459 ICUs in 50 countries (LUNG SAFE)
  measure_type: PERIOD_PREVALENCE
  prevalence_class: ABOVE_1_IN_1000
  rate_per_100000: 10400.0
  notes: 10.4% of ICU admissions over 4 consecutive weeks, winter 2014.
- population: United States adults (King County, WA; AECC acute lung injury)
  measure_type: ANNUAL_INCIDENCE
  prevalence_class: BAND_1_5_PER_10000
  rate_per_100000: 78.9
  notes: >-
    Crude incidence; age-adjusted 86.2 per 100,000 person-years. AECC-era
    acute lung injury, broader than Berlin ARDS.
```

**Do not mix these two** — one is a period prevalence among ICU patients, the other an annual population incidence. The `measure_type` slot exists precisely to keep them apart.

### For genetic etiology

- **Inheritance pattern:** multifactorial / polygenic. Suggested binding: `HP:0010982` *Polygenic inheritance* ⚠️.
- **Penetrance, expressivity, anticipation, germline mosaicism, founder effects, carrier frequency:** **not applicable.** ARDS has no Mendelian form. Do not populate these slots.
- **Ancestry heterogeneity is real and documented** (PMID:34032881: "There was distinct genetic heterogeneity in ARDS between Europeans and African Americans") — record this rather than a founder-effect claim.
- **Consanguinity:** not applicable.

### Population demographics

- **Sex:** male predominance in most cohorts (roughly 55-60% male), partly reflecting the sex distribution of the precipitating insults (trauma, alcohol-related illness). The ART trial cohort was "37.5% female" (PMID:28973363) — typical.
- **Age:** median around 50-60 in trial cohorts; incidence and mortality both rise with age (PMID:16236739: "Mortality increased with age from 24 percent for patients 15 through 19 years of age to 60 percent for patients 85 years of age or older (P<0.001)").
- **Geographic distribution:** worldwide. Recognised and reported ARDS incidence is strongly confounded by ICU-bed availability, ventilator access, and diagnostic capability — which is precisely why the Global Definition added a resource-limited category. Reported ICU incidence is far lower in low-income settings, and this is at least partly ascertainment, not biology.
- **Ethnic groups:** no established incidence difference attributable to ancestry; documented outcome disparities in US cohorts. **[unquoted]**

---

## 10. Diagnostics

**ARDS is a clinical-syndromic diagnosis. There is no confirmatory test.** Everything below either establishes the syndromic criteria, excludes mimics, or identifies the precipitant.

### Clinical criteria (the actual diagnostic instrument)

**New Global Definition (2024, PMID:37487152)** — all four required:
1. **Timing:** within 1 week of a known insult or new/worsening respiratory symptoms
2. **Oxygenation:** PaO₂/FiO₂ ≤300 mmHg, **or** SpO₂/FiO₂ ≤315 when SpO₂ ≤97%
3. **Imaging:** bilateral opacities on chest radiograph, CT, **or lung ultrasound**, not fully explained by effusion, collapse, or nodules
4. **Origin of oedema:** respiratory failure not fully explained by cardiac failure or fluid overload
5. **Respiratory support:** invasive MV; **or** HFNO ≥30 L/min; **or** NIV/CPAP with PEEP ≥5 cmH₂O; **or**, in resource-limited settings, no support requirement at all

Berlin severity strata retained for intubated patients (PMID:22797452): mild 200<P/F≤300, moderate 100<P/F≤200, severe P/F≤100 (all at PEEP ≥5).

**Recognition is poor in practice** — a genuinely important clinical-burden finding (PMID:26903337):

> "Clinical recognition of ARDS ranged from 51.3% (95% CI, 47.5%-55.0%) in mild to 78.5% (95% CI, 74.8%-81.8%) in severe ARDS."

> "This syndrome appeared to be underrecognized and undertreated and associated with a high mortality rate."

### Laboratory tests

- **Arterial blood gas** — PaO₂, PaCO₂, pH; the source of the P/F ratio. LOINC: 2703-7 (PaO₂), 2019-8 (PaCO₂), 11557-6 (pH) ⚠️ verify.
- **Pulse oximetry (SpO₂)** — now a definitional alternative; note the systematic **overestimation of oxygen saturation in patients with darker skin pigmentation**, which has direct diagnostic-equity implications for the SpO₂/FiO₂ criterion. **[unquoted — an important and citable 2020-2022 literature]**
- **B-type natriuretic peptide (BNP/NT-proBNP)** — to help exclude cardiogenic oedema; imperfect, since BNP rises in critical illness generally.
- **Full blood count, lactate, procalcitonin, blood/sputum cultures, respiratory viral PCR panel** — for the precipitant.
- **Bronchoalveolar lavage** — cell differential (neutrophil predominance), microbiology, and exclusion of alveolar haemorrhage or eosinophilic pneumonia.
- **Oedema-fluid-to-plasma protein ratio >0.65** — the classic bedside discriminator of increased-permeability from hydrostatic oedema. Underused, but conceptually central.

### Biomarkers

None are validated for diagnosis; all are research/prognostic tools:

| Biomarker | Compartment injured | Note |
|---|---|---|
| sRAGE (soluble receptor for advanced glycation end products) | AT1 epithelium | Highest in direct-insult ARDS |
| Surfactant protein D (SP-D) | AT2 epithelium | |
| Angiopoietin-2 | Endothelium | Among the best-performing single markers |
| von Willebrand factor antigen | Endothelium | |
| IL-6, IL-8 (CXCL8), sTNFR-1 | Inflammation | The core of the LCA subphenotype classifiers |
| PAI-1 | Coagulation/fibrinolysis | |
| Protein C (reduced) | Coagulation | |
| Ferritin | Hyperinflammation | Proposed as a practical hyperinflammatory-class marker (PMC10980828) **[unquoted]** |
| Club cell protein 16 (CC16) | Airway epithelium | |

Parsimonious 3-variable classifiers (IL-8, bicarbonate, sTNFR-1) can assign subphenotype at the bedside — the enabling step for prospective enrichment trials. **[unquoted]**

### Imaging

- **Chest radiograph** — bilateral opacities; poor inter-observer reliability, which was a known Berlin-definition weakness.
- **Chest CT** — the reference for distribution (focal vs diffuse), for complications (pneumothorax, abscess, PE), and for the fibroproliferative phase. Reveals the "baby lung."
- **Lung ultrasound** — now an accepted imaging modality under the Global Definition; B-lines, subpleural consolidation, pleural-line abnormalities. Its inclusion is the change with the biggest practical effect in resource-limited settings.
- **Echocardiography** — to assess LV function (excluding cardiogenic oedema) and RV size/function (acute cor pulmonale).
- **Electrical impedance tomography (EIT)** — research/emerging bedside regional ventilation monitoring, used for PEEP titration.

### Functional and physiologic tests

Respiratory system compliance (C_rs = Vt/(Pplat − PEEP)), driving pressure (ΔP = Pplat − PEEP; the ventilation variable most strongly associated with survival), plateau pressure, oesophageal manometry for transpulmonary pressure, dead-space fraction (V_D/V_T; strongly prognostic), oxygenation index (OI, used in paediatrics), and the recruitment-to-inflation ratio.

### Biopsy and pathology

**Open lung biopsy is rarely performed** and is reserved for cases where an alternative treatable diagnosis is suspected. The histological correlate is **diffuse alveolar damage (DAD)**: hyaline membranes, alveolar and interstitial oedema, capillary congestion, AT1 necrosis, later AT2 hyperplasia and interstitial fibroproliferation.

**A curation-critical caveat:** DAD is present in only roughly **half** of clinically defined ARDS at autopsy. From PMID:30872586: "Pathological specimens from patients with ARDS frequently reveal diffuse alveolar damage" — note *frequently*, not invariably. **DAD is neither necessary nor sufficient for the clinical syndrome, and must not be curated as a synonym for ARDS.** This clinical-pathological discordance is a legitimate `KNOWLEDGE_GAP` discussion.

### Genetic testing

**Not indicated.** There is no clinical genetic test for ARDS; no gene panel, no single-gene test, no WES/WGS indication, no CMA, no karyotype, no FISH, no mtDNA testing, no repeat-expansion testing. Genetic work is research-only. Say so explicitly in the entry rather than leaving the section blank — the absence is informative.

### Omics-based diagnostics

Research-stage only. Whole-blood transcriptomic classifiers for subphenotype assignment and plasma proteomic panels are the most developed; none is in clinical use. No liquid-biopsy or epigenomic diagnostic exists.

### Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| Cardiogenic pulmonary oedema | Elevated BNP, LV dysfunction on echo, cardiomegaly, rapid response to diuresis, oedema/plasma protein ratio <0.65 |
| Volume overload / fluid resuscitation-related oedema | Positive fluid balance, resolves with diuresis |
| Diffuse alveolar haemorrhage | Serial bloodier BAL aliquots, haemosiderin-laden macrophages, falling haemoglobin, vasculitis serology |
| Acute eosinophilic pneumonia | BAL eosinophilia >25%, dramatic steroid response |
| Acute interstitial pneumonia (Hamman-Rich) | Idiopathic — no identifiable insult; histologically DAD. `MONDO:0019203` ✅ in cache, and the repo has related interstitial-pneumonia MONDO terms cached |
| Acute exacerbation of idiopathic pulmonary fibrosis | Pre-existing fibrosis, honeycombing on prior imaging |
| Hypersensitivity pneumonitis (acute) | Exposure history; repo entry `Hypersensitivity_Pneumonitis.yaml` exists |
| Cryptogenic organising pneumonia | `MONDO:0015264` ✅; subacute course, migratory opacities |
| Drug-induced pneumonitis | Temporal drug relationship (amiodarone, bleomycin, checkpoint inhibitors) |
| Disseminated malignancy / lymphangitic carcinomatosis | Imaging pattern, history |
| Neurogenic pulmonary oedema | Preceding catastrophic CNS event |
| High-altitude pulmonary oedema | Exposure history |
| EVALI | Vaping history; repo entry exists |

These make good `differentials:` entries — **look up each MONDO ID from the sibling KB entry rather than guessing it.**

### Screening

**No population screening exists or would be sensible** (ARDS is an acute complication, not a latent disease). The functional analogue is **risk stratification of at-risk hospitalised patients** using the Lung Injury Prediction Score (PMID:20802164):

> "LIPS discriminated patients who developed ALI from those who did not with an AUC of 0.80 (95% confidence interval, 0.78-0.82)."

> "When adjusted for severity of illness and predisposing conditions, development of ALI increased the risk of in-hospital death (odds ratio, 4.1; 95% confidence interval, 2.9-5.7)."

LIPS is a good candidate for a `definitions:` entry with `definition_type: PHENOTYPE_ALGORITHM` and `derivation_basis: ESTABLISHED_CRITERIA`, `validation_status.status: VALIDATED_AGAINST_GOLD_STANDARD` (validated prospectively in the 5,584-patient multicentre cohort above).

---

## 11. Outcome / Prognosis

### Mortality

**Berlin-stratified hospital mortality (PMID:26903337, LUNG SAFE):**

> "Hospital mortality was 34.9% (95% CI, 31.4%-38.5%) for those with mild, 40.3% (95% CI, 37.4%-43.3%) for those with moderate, and 46.1% (95% CI, 41.9%-50.4%) for those with severe ARDS."

**Berlin derivation-cohort mortality (PMID:22797452):** 27% / 32% / 45% for mild / moderate / severe.

**Overall trajectory (PMID:30872586):** "Despite some improvements, mortality remains high at 30-40% in most studies."

**Subphenotype-stratified (PMID:30078618, HARP-2):** 28-day mortality 39% (hyperinflammatory) vs 17% (hypoinflammatory) — a larger spread than the Berlin severity strata produce, which is the argument that biology beats physiology as a prognostic axis.

**Population-level burden (PMID:16236739):** 190,600 US cases/year, 74,500 deaths, 3.6 million hospital days (AECC-era ALI).

**Cause of death:** predominantly multiple organ failure and the underlying precipitant; refractory hypoxaemia accounts for a minority (roughly 10-20%) of deaths. **[unquoted]** This is mechanistically important — it explains why oxygenation-improving therapies (inhaled NO, prone positioning in mild disease, ECMO) improve gas exchange without necessarily improving survival.

### Life expectancy after survival

ARDS survivors carry elevated mortality for at least 1-5 years beyond discharge relative to matched controls, driven by comorbidity and functional decline rather than lung disease. **[unquoted]**

### Morbidity, disability, and quality of life

The Herridge 5-year cohort (PMID:21470008) is the anchor — see §3 for verbatim quotes. Key points: 6-minute walk distance 76% of predicted at 5 years; SF-36 Physical Component Score 41 vs an age/sex-matched norm of 50; pulmonary function normal to near-normal; "a constellation of other physical and psychological problems developed or persisted in patients **and family caregivers** for up to 5 years"; "Patients with more coexisting illnesses incurred greater 5-year costs."

Common sequelae: ICU-acquired weakness, exercise limitation, cognitive impairment (executive function, memory), depression, anxiety, PTSD, chronic pain, joint contracture, tracheostomy-related complications, and caregiver burden. Instruments: SF-36, EQ-5D, 6MWT, HADS, IES-R, MoCA.

### Complications

Ventilator-associated pneumonia, barotrauma/pneumothorax (quantified in PMID:28973363: 3.2% vs 1.2% requiring drainage), acute kidney injury, delirium, venous thromboembolism, GI bleeding, catheter-related bloodstream infection, ICU-acquired weakness, right heart failure, and — for ECMO patients — bleeding and thrombocytopenia (PMID:29791822: "more bleeding events leading to transfusion in the ECMO group than in the control group (in 46% vs. 28% of patients...) as well as more cases of severe thrombocytopenia (in 27% vs. 16%...)").

### Recovery potential

Good pulmonary recovery is the norm in survivors; good functional recovery is not. Younger patients recover faster but, per PMID:21470008, "neither group returned to normal predicted levels of physical function at 5 years."

### Prognostic factors

- **Clinical:** age, severity stratum (P/F), non-pulmonary organ failures, shock, immunosuppression, chronic liver disease, APACHE/SOFA.
- **Physiologic:** driving pressure (ΔP), dead-space fraction (V_D/V_T), respiratory-system compliance, ventilatory ratio, oxygenation index. Driving pressure is the ventilation variable most consistently associated with survival.
- **Aetiologic:** trauma-associated ARDS has the *lowest* mortality; sepsis-associated the highest.
- **Biological:** subphenotype assignment (above); individual markers Ang-2, IL-8, sRAGE, sTNFR-1, PAI-1, protein C.
- **Radiographic:** extent of consolidation, fibroproliferative change on CT.

---

## 12. Treatment

The organising fact: **no pharmacotherapy has an established mortality benefit in unselected ARDS.** From PMID:30872586: "Treatment focuses on lung-protective ventilation; no specific pharmacotherapies have been identified." Every proven intervention is a way of supporting the patient while causing less additional injury. That is the shape of the treatment section, and it should be curated honestly — the negative trials carry as much information as the positive ones.

### Interventions with proven mortality benefit

**1. Low tidal volume ("lung-protective") ventilation** — the foundational intervention (PMID:10793162, ARDS Network ARMA trial, *N Engl J Med* 2000;342:1301-8):

> "The trial was stopped after the enrollment of 861 patients because mortality was lower in the group treated with lower tidal volumes than in the group treated with traditional tidal volumes (31.0 percent vs. 39.8 percent, P=0.007), and the number of days without ventilator use during the first 28 days after randomization was greater in this group (mean [+/-SD], 12+/-11 vs. 10+/-11; P=0.007)."

> "In patients with acute lung injury and the acute respiratory distress syndrome, mechanical ventilation with a lower tidal volume than is traditionally used results in decreased mortality and increases the number of days without ventilator use."

Target: 6 mL/kg predicted body weight, plateau pressure ≤30 cmH₂O.
`treatment_term`: `NCIT:C70909` *Mechanical Ventilation* ✅ · `therapeutic_modality: DEVICE` (or `OTHER`) · targets the **Ventilator-Induced Lung Injury** node.

**2. Prone positioning in severe ARDS** (PMID:23688302, PROSEVA, *N Engl J Med* 2013;368:2159-68):

> "The 28-day mortality was 16.0% in the prone group and 32.8% in the supine group (P<0.001). The hazard ratio for death with prone positioning was 0.39 (95% confidence interval [CI], 0.25 to 0.63). Unadjusted 90-day mortality was 23.6% in the prone group versus 41.0% in the supine group (P<0.001)"

> "In patients with severe ARDS, early application of prolonged prone-positioning sessions significantly decreased 28-day and 90-day mortality."

Sessions of ≥16 h, in P/F <150 with FiO₂ ≥0.6 and PEEP ≥5. **Severely underused** — from LUNG SAFE: "Prone positioning was used in 16.3% (95% CI, 13.7%-19.2%) of patients with severe ARDS."
`treatment_term`: ⚠️ search NCIT for a prone-positioning/patient-positioning procedure term; if none is reachable from `NCIT:C25218`, bind `NCIT:C49236` *Therapeutic Procedure* ⚠️ and carry the specificity in `preferred_term`.

**3. Dexamethasone in established moderate-severe ARDS** (PMID:32043986, DEXA-ARDS, *Lancet Respir Med* 2020;8:267-276):

> "The mean number of ventilator-free days was higher in the dexamethasone group than in the control group (between-group difference 4·8 days [95% CI 2·57 to 7·03]; p<0·0001). At 60 days, 29 (21%) patients in the dexamethasone group and 50 (36%) patients in the control group had died (between-group difference -15·3% [-25·9 to -4·9]; p=0·0047)."

> "Early administration of dexamethasone could reduce duration of mechanical ventilation and overall mortality in patients with established moderate-to-severe ARDS."

Dose: 20 mg IV daily days 1-5, then 10 mg daily days 6-10. Note the trial stopped early for slow enrolment (277 of a planned 314), which tempers the estimate — worth a `notes:` line.
`treatment_term`: `NCIT:C15986` *Pharmacotherapy* ✅ · `therapeutic_agent`: `CHEBI:41879` *dexamethasone* ✅ · `therapeutic_modality: SMALL_MOLECULE`.

**4. Dexamethasone in COVID-19 respiratory failure** (PMID:32678530, RECOVERY, *N Engl J Med* 2021;384:693-704):

> "In the dexamethasone group, the incidence of death was lower than that in the usual care group among patients receiving invasive mechanical ventilation (29.3% vs. 41.4%; rate ratio, 0.64; 95% CI, 0.51 to 0.81) and among those receiving oxygen without invasive mechanical ventilation (23.3% vs. 26.2%; rate ratio, 0.82; 95% CI, 0.72 to 0.94) but not among those who were receiving no respiratory support at randomization (17.8% vs. 14.0%; rate ratio, 1.19; 95% CI, 0.92 to 1.55)."

The severity-dependent effect direction is the notable part — steroids help when lung injury is established and appear unhelpful (possibly harmful) before it is.

### Interventions with benefit on secondary outcomes but not mortality

**5. Conservative fluid management** (PMID:16714767, FACTT, *N Engl J Med* 2006;354:2564-75):

> "The rate of death at 60 days was 25.5 percent in the conservative-strategy group and 28.4 percent in the liberal-strategy group (P=0.30...)"

> "the conservative strategy of fluid management improved lung function and shortened the duration of mechanical ventilation and intensive care without increasing nonpulmonary-organ failures."

`treatment_term`: `NCIT:C116537` *Fluid Therapy* ✅.

**6. High-flow nasal oxygen** in acute hypoxaemic respiratory failure (PMID:25981908, FLORALI, *N Engl J Med* 2015;372:2185-96):

> "The intubation rate (primary outcome) was 38% (40 of 106 patients) in the high-flow-oxygen group, 47% (44 of 94) in the standard group, and 50% (55 of 110) in the noninvasive-ventilation group (P=0.18 for all comparisons)."

> "The hazard ratio for death at 90 days was 2.01 (95% confidence interval [CI], 1.01 to 3.99) with standard oxygen versus high-flow oxygen (P=0.046) and 2.50 (95% CI, 1.31 to 4.78) with noninvasive ventilation versus high-flow oxygen (P=0.006)."

`treatment_term`: `NCIT:C94624` *Oxygen Therapy* ✅.

**7. Awake prone positioning in COVID-19 hypoxaemic failure** (PMID:34425070, *Lancet Respir Med* 2021;9:1387-1395):

> "Treatment failure occurred in 223 (40%) of 564 patients assigned to awake prone positioning and in 257 (46%) of 557 patients assigned to standard care (relative risk 0·86 [95% CI 0·75-0·98]). The hazard ratio (HR) for intubation was 0·75 (0·62-0·91), and the HR for mortality was 0·87 (0·68-1·11)"

**8. Helmet NIV** (PMID:27179847, *JAMA* 2016;315:2435-41) — single-centre, stopped early, so hypothesis-generating:

> "The intubation rate was 61.5% (n = 24) for the face mask group and 18.2% (n = 8) for the helmet group (absolute difference, -43.3%; 95% CI, -62.4% to -24.3%; P < .001)."

> "Multicenter studies are needed to replicate these findings."

### Interventions with contested or neutral results

**9. Neuromuscular blockade — a genuine contradiction in the literature, and worth curating as such.**

ACURASYS was positive (PMID:20843245, *N Engl J Med* 2010;363:1107-16):

> "The hazard ratio for death at 90 days in the cisatracurium group, as compared with the placebo group, was 0.68 (95% confidence interval [CI], 0.48 to 0.98; P=0.04), after adjustment for both the baseline PaO2:FIO2 and plateau pressure and the Simplified Acute Physiology II score."

ROSE was null (PMID:31112383, *N Engl J Med* 2019;380:1997-2008):

> "At 90 days, 213 patients (42.5%) in the intervention group and 216 (42.8%) in the control group had died before hospital discharge (between-group difference, -0.3 percentage points; 95% confidence interval, -6.4 to 5.9; P = 0.93). While in the hospital, patients in the intervention group were less physically active and had more adverse cardiovascular events than patients in the control group."

Curate this as **two evidence items on the same claim** — one `SUPPORT` (ACURASYS), one `REFUTE` (ROSE) — rather than averaging them into a hedge. The differences (ROSE used higher PEEP and lighter sedation in controls) are the substance of the disagreement.
`therapeutic_agent`: `CHEBI:140621` *cisatracurium* ✅.

**10. ECMO in very severe ARDS** (PMID:29791822, EOLIA, *N Engl J Med* 2018;378:1965-1975):

> "At 60 days, 44 of 124 patients (35%) in the ECMO group and 57 of 125 (46%) in the control group had died (relative risk, 0.76; 95% confidence interval [CI], 0.55 to 1.04; P=0.09)."

> "Among patients with very severe ARDS, 60-day mortality was not significantly lower with ECMO than with a strategy of conventional mechanical ventilation that included ECMO as rescue therapy."

Note the 28% crossover from control to rescue ECMO, which makes this a trial of *early* vs *rescue* ECMO rather than ECMO vs no ECMO — a Bayesian reanalysis favoured ECMO. **[unquoted]**
`treatment_term`: `NCIT:C171507` *Extracorporeal Membrane Oxygenation* ✅ · `therapeutic_modality: DEVICE`.

**11. Conservative oxygenation — harmful signal** (PMID:32160661, LOCO₂, *N Engl J Med* 2020;382:999-1008):

> "After the enrollment of 205 patients, the trial was prematurely stopped by the data and safety monitoring board because of safety concerns and a low likelihood of a significant difference between the two groups in the primary outcome."

> "At day 90, 44.4% of the patients in the conservative-oxygen group and 30.4% of the patients in the liberal-oxygen group had died (difference, 14.0 percentage points; 95% CI, 0.7 to 27.2). Five mesenteric ischemic events occurred in the conservative-oxygen group."

### Interventions shown to be harmful

**12. Aggressive recruitment manoeuvres with PEEP titration** (PMID:28973363, ART trial, *JAMA* 2017;318:1335-1345):

> "At 28 days, 277 of 501 patients (55.3%) in the experimental group and 251 of 509 patients (49.3%) in the control group had died (hazard ratio [HR], 1.20; 95% CI, 1.01 to 1.42; P = .041)."

> "In patients with moderate to severe ARDS, a strategy with lung recruitment and titrated PEEP compared with low PEEP increased 28-day all-cause mortality. These findings do not support the routine use of lung recruitment maneuver and PEEP titration in these patients."

### Failed pharmacotherapies (curate as REFUTE evidence — the negative record is the field's most consistent finding)

β₂-agonists (salbutamol/albuterol — `CHEBI:2549` ✅ — BALTI-2 and ALTA, both harmful or futile), exogenous surfactant, inhaled nitric oxide (`CHEBI:16480` ✅ — improves oxygenation, no mortality benefit, AKI signal), ketoconazole, lisofylline, N-acetylcysteine, activated protein C, statins in unselected patients (HARP-2, SAILS — see the subphenotype caveat below), omega-3/antioxidant enteral formulas (OMEGA — harmful), GM-CSF, keratinocyte growth factor (KGF — harmful), aspirin for prevention (LIPS-A, PMID:27179988), early high-dose methylprednisolone in late ARDS (harmful after day 14).

### Precision-medicine / predictive enrichment

The one durable positive signal from a "failed" drug — simvastatin (`CHEBI:9150` ✅) in the hyperinflammatory subphenotype (PMID:30078618, quoted in §6): "within the hyperinflammatory subphenotype, patients treated with simvastatin had significantly higher 28-day survival than did those given placebo (p=0·008)." Interpretation from the same abstract: "These findings support further pursuit of predictive enrichment strategies in critical care clinical trials."

### Cell and advanced therapies

**Mesenchymal stromal cells** — extensively tested, consistently safe, not yet efficacious. A 2024 double-blind RCT of BM-MSCs in COVID-19 ARDS missed its primary endpoint (change in P/F at day 7) but showed shorter time to oxygen discontinuation (14 vs 23 days) and shorter hospital stay (17.5 vs 28 days); PMID:38409332, *Bone Marrow Transplant* 2024. The STAT phase 2b trial randomised 120 ventilated ARDS patients (101 COVID, 19 classical) to a single IV MSC dose vs placebo. **[both unquoted — retrieve abstracts before creating evidence items]** Safety across trials is good up to 10×10⁶ cells/kg. `therapeutic_modality: CELL_THERAPY`.

**Gene therapy, gene editing, ASOs, siRNA, mRNA therapy:** none in clinical development for ARDS. `aso_details` is not applicable.

**Immunomodulators:** anti-IL-6 (tocilizumab) and JAK inhibition (baricitinib) have proven benefit in **COVID-19** specifically — e.g. PMID:33306283, ACTT-2: "Patients receiving high-flow oxygen or noninvasive ventilation at enrollment had a time to recovery of 10 days with combination treatment and 18 days with control (rate ratio for recovery, 1.51; 95% CI, 1.10 to 2.08)." Curate these under COVID-19, cross-referenced from ARDS, not as general ARDS therapy.

### Experimental pipeline (2024-2026)

**Treat all of the following as low-confidence, non-peer-reviewed corporate disclosures until a published trial report exists — do not create evidence items from press releases.** Reported agents include paridiprubart (anti-TLR4 monoclonal antibody; a phase 3 readout was announced in 2025-2026), vilobelimab (anti-C5a), STSA-1002 (C5a inhibitor), GEn-1124 (MAPK14 inhibitor), ALT-100 (anti-eNAMPT), recombinant human plasma gelsolin (rhu-pGSN, FDA Fast Track June 2025), and AV-001 (Tie2 agonist, FDA Fast Track May 2024). More than 50 companies are reported to have ARDS programmes. **[all unquoted — search-summary sourced]** The mechanistic targets are informative even where efficacy is unproven: TLR4 (chain step 2), complement C5a (step 3-4), Tie2/Ang-2 (step 5), gelsolin (actin scavenging after cell necrosis).

A host-directed-therapy **platform trial** with placebo, vilobelimab (Cohort A), and paridiprubart (Cohort B) arms is running. **[unquoted — locate the NCT identifier before curating a `clinical_trials:` entry]**

### Supportive and rehabilitative care

Sedation minimisation and daily awakening trials, early mobilisation, VTE and stress-ulcer prophylaxis, nutrition, tracheostomy for prolonged ventilation, delirium prevention, and structured post-ICU follow-up/rehabilitation. `NCIT:C15747` *Supportive Care* ✅; `NCIT:C15302` *Physical Therapy* ⚠️ and `NCIT:C15315` *Rehabilitation* ⚠️ for the recovery phase.

### Treatment algorithm

The ESICM 2023 guideline is the authoritative synthesis (PMID:37326646, *Intensive Care Med* 2023;49:727-759):

> "The CPG addressed 21 questions and formulates 21 recommendations on the following domains: (1) definition; (2) phenotyping, and respiratory support strategies including (3) high-flow nasal cannula oxygen (HFNO); (4) non-invasive ventilation (NIV); (5) tidal volume setting; (6) positive end-expiratory pressure (PEEP) and recruitment maneuvers (RM); (7) prone positioning; (8) neuromuscular blockade, and (9) extracorporeal life support (ECLS)."

> "The scope of this CPG is limited to adult patients and to non-pharmacological respiratory support strategies across different aspects of acute respiratory distress syndrome (ARDS), including ARDS due to coronavirus disease 2019 (COVID-19)."

And the 2024 BMJ state-of-the-art review (PMID:39467606, *BMJ* 2024;387:e076612):

> "Key highlights include a recommended new global definition of ARDS and updated guidelines for managing ARDS on a backbone of established interventions such as low tidal volume ventilation, prone positioning, and a conservative fluid strategy."

Practical escalation ladder: treat the precipitant → lung-protective ventilation (6 mL/kg PBW, Pplat ≤30, ΔP ≤15) → moderate PEEP → conservative fluids → if P/F <150: prone positioning ± neuromuscular blockade → consider dexamethasone → if refractory: inhaled pulmonary vasodilator as a bridge, then VV-ECMO at a specialist centre.

---

## 13. Prevention

### Primary prevention

Prevent the precipitating insults: pneumococcal and influenza vaccination (`NCIT:C15346` *Vaccination* ⚠️), COVID-19 vaccination, sepsis bundles with early antibiotics and source control, trauma prevention, aspiration precautions (head-of-bed elevation, careful sedation, swallow assessment), restrictive transfusion policies and male-predominant plasma donor selection (which substantially reduced TRALI incidence — a genuine public-health success), and alcohol- and tobacco-cessation programmes.

### Secondary prevention (the active research frontier)

- **Lung-protective ventilation in patients *without* ARDS** — intraoperatively and in the ICU — reduces subsequent ARDS incidence. **[unquoted]**
- **Restrictive fluid resuscitation** in sepsis and trauma.
- **Risk stratification with LIPS** (PMID:20802164, AUC 0.80) to enrich prevention trials.
- **Checklist-based prevention bundles** (e.g. "Checklist for Lung Injury Prevention", CLIP) — modest observational benefit. **[unquoted]**
- **Pharmacological prevention: tested and negative.** Aspirin (LIPS-A, PMID:27179988), inhaled budesonide/formoterol, and statins have all failed to prevent ARDS in at-risk patients. Curate these as `REFUTE`.

### Tertiary prevention

Preventing complications in established ARDS: VAP prevention bundles, VTE prophylaxis, sedation minimisation and delirium prevention, early mobilisation to limit ICU-acquired weakness, pressure-injury prevention (especially in proned patients — facial and chest pressure injuries are the main prone-position harm), and avoiding the interventions shown to be harmful (aggressive recruitment, conservative oxygenation targets, late high-dose steroids).

### Screening, genetic screening, and counselling

**Not applicable.** There is no ARDS screening programme, no carrier screening, no prenatal or preimplantation testing, and no role for genetic counselling. State this explicitly.

### Public health and environmental interventions

Air-quality regulation (PM₂.₅, ozone), occupational exposure limits for respiratory irritants, industrial chemical-release preparedness, tobacco control, alcohol policy, pandemic preparedness and ICU surge capacity, and — following the Global Definition's resource-limited category — expansion of pulse oximetry and lung ultrasound in low-resource settings, which is a *diagnostic-equity* intervention with direct prevention implications.

---

## 14. Other Species / Natural Disease

**ARDS is not a Mendelian animal disease and has no OMIA entry.** It occurs naturally in animals as an acquired critical-illness syndrome, and the veterinary literature explicitly borrows the human framework.

### Species with recognised naturally occurring ALI/ARDS

| Species | NCBITaxon (⚠️ verify) | Context |
|---|---|---|
| Dog (*Canis lupus familiaris*) | 9615 | Veterinary ALI/ARDS consensus criteria exist (Dorothy Russell Havemeyer working group, 2007); causes include sepsis, pancreatitis, aspiration, smoke inhalation, babesiosis |
| Cat (*Felis catus*) | 9685 | Less commonly recognised; sepsis, trauma |
| Horse (*Equus caballus*) | 9796 | Foal ARDS/acute interstitial pneumonia; equine multinodular pulmonary fibrosis as a related fibrotic outcome |
| Cattle (*Bos taurus*) | 9913 | Acute bovine pulmonary emphysema and oedema ("fog fever", 3-methylindole from tryptophan fermentation) — a naturally occurring toxic ALI with real mechanistic interest |
| Pig (*Sus scrofa*) | 9823 | Both natural (PRRSV, *Actinobacillus*) and the dominant large-animal experimental model |
| Sheep (*Ovis aries*) | 9940 | Chronically instrumented smoke-inhalation/sepsis model; the classic lung-lymph preparation |

**[all veterinary claims unquoted — retrieve the Havemeyer veterinary ALI/ARDS consensus and any OMIA/VetCompass records before creating evidence items]**

### Orthologous genes

Not meaningful for a syndrome with no causal gene. The relevant orthologies are of the *mechanism*: mouse *Tlr4*/human *TLR4*, mouse *Nlrp3*/human *NLRP3*, mouse *Scnn1a*/human *SCNN1A*, mouse *Sftpc*/human *SFTPC*. Alliance of Genome Resources and HomoloGene are the resources.

### Comparative pathology

Diffuse alveolar damage with hyaline membranes is recognisable across mammals, but there are consequential species differences that limit translation:
- **Neutrophil biology**: mouse neutrophils lack defensins and have far lower MPO content than human neutrophils; mouse blood is lymphocyte-predominant, human neutrophil-predominant.
- **Endotoxin sensitivity**: mice tolerate LPS doses that would be uniformly lethal in humans, by orders of magnitude.
- **Collateral ventilation and lobar anatomy** differ (pigs and cattle have essentially no collateral ventilation; dogs have extensive collateral channels), which changes atelectasis and recruitment behaviour.
- **Pulmonary intravascular macrophages** are present in ruminants, pigs, cats and horses but essentially absent in humans, mice and dogs — a major difference in how the lung handles circulating particulates and endotoxin.
- Mice do not spontaneously develop hyaline membranes.

### Zoonotic potential and cross-species susceptibility

ARDS itself is not transmissible; its **precipitants** frequently are. Zoonotic and cross-species agents that cause ARDS in humans: SARS-CoV-2, SARS-CoV, MERS-CoV (camel reservoir; the repo has a MERS entry), avian influenza H5N1/H7N9, hantavirus (HPS — hantavirus *pulmonary* syndrome, a distinct entity with a capillary-leak mechanism that overlaps ARDS), *Coxiella burnetii*, *Francisella tularensis*, *Bacillus anthracis*, leptospirosis (Weil's disease with pulmonary haemorrhage), and plague pneumonia.

---

## 15. Model Organisms

The essential framework document is the ATS workshop report (PMID:35103557, *Am J Respir Cell Mol Biol* 2022;66:e1-e14). It should be cited on **every** ARDS animal model entry:

> "We propose that ALI presents as a 'multidimensional entity' characterized by four 'domains' that reflect the key pathophysiologic features and underlying biology of human acute respiratory distress syndrome. These domains are 1) histological evidence of tissue injury, 2) alteration of the alveolar-capillary barrier, 3) presence of an inflammatory response, and 4) physiologic dysfunction."

> "We suggest that mechanistic studies may justifiably focus on a single domain of lung injury, but models must document alterations of at least three of the four domains to qualify as 'experimental ALI.'"

> "The continuum concept of ALI increases the flexibility and applicability of the definition to multiple models while increasing the likelihood of translating preclinical findings to critically ill patients."

This maps directly onto dismech's `ModelMechanismLink` structure: the four domains are natural `readouts`, and the "at least three of four" rule is a defensible basis for assigning `fidelity: HIGH` vs `MODERATE`.

### Induced models (there are no spontaneous genetic ARDS models)

| Model | Species | Mimics | `fidelity` guidance | Key limitation |
|---|---|---|---|---|
| Intratracheal / intranasal LPS | Mouse (10090), rat (10116) | Direct insult, TLR4 → NF-κB (chain steps 1-3) | MODERATE | No pathogen replication; mice ~1000× less LPS-sensitive than humans; self-limited, rarely lethal |
| Intratracheal HCl (acid aspiration) | Mouse, rat, rabbit | Aspiration pneumonitis; epithelial necrosis | MODERATE | Uniform, synchronous injury unlike clinical aspiration |
| Cecal ligation and puncture (CLP) | Mouse, rat | Indirect/septic ARDS (steps 1, 13) | MODERATE | Lung injury is often mild; highly variable by puncture size/needle gauge |
| Live bacterial pneumonia (*P. aeruginosa*, *S. pneumoniae*, *K. pneumoniae*) | Mouse, rat, pig | Direct infectious ARDS | MODERATE-HIGH | Strain- and dose-sensitive |
| Influenza A / SARS-CoV-2 infection | Mouse (adapted strains or K18-hACE2 transgenic), hamster (10036), ferret (9669), NHP (9544/9541) | Viral ARDS | MODERATE-HIGH | Wild-type mice are not susceptible to SARS-CoV-2 without hACE2; K18-hACE2 mice die of encephalitis, not pneumonia — a well-documented `FAILS_TO_RECAPITULATE` case |
| High-tidal-volume ventilation (VILI) | Mouse, rat, pig (9823), sheep (9940) | Ventilator-induced injury (step 12) | HIGH for the mechanical domain | Requires healthy lungs unless combined ("two-hit"); Vt used (20-40 mL/kg) far exceeds anything clinical |
| Two-hit (LPS + VILI, acid + VILI) | Mouse, rat, pig | Clinical reality of injured lung + ventilator | HIGH | Complex, low throughput |
| Oleic acid infusion | Dog (9615), pig, sheep | Endothelial injury, fat embolism | MODERATE | Chemically non-physiological; minimal inflammatory component (fails the inflammation domain) |
| Hyperoxia (>95% O₂) | Mouse, rat | Oxygen toxicity, oxidative injury | LOW-MODERATE | Slow (days); mechanism is oxidant-dominant only |
| Bleomycin | Mouse, rat | **Fibroproliferative phase only** (step 14b) | MODERATE for fibrosis | Not an ARDS model — models fibrosis; self-resolving in mice, unlike human IPF |
| Smoke inhalation ± burn | Sheep, pig | Inhalation injury | HIGH | Requires large-animal facilities |
| Ischaemia-reperfusion / transplant | Rat, pig | Primary graft dysfunction | MODERATE | Narrow clinical analogue |

### Genetic models

Not disease models but **mechanism dissection tools**: *Tlr4*⁻/⁻, *Nlrp3*⁻/⁻, *Casp1*⁻/⁻, *Il6*⁻/⁻, *Cxcr2*⁻/⁻, *Ager* (RAGE)⁻/⁻, *Nfe2l2* (Nrf2)⁻/⁻, *Angpt2* conditional, *Sftpc*-CreER lineage-tracing for AT2→AT1 transdifferentiation, *Scgb1a1*-CreER, and neutrophil- or macrophage-specific conditional deletions (LysM-Cre, Mrp8-Cre). Resources: MGI, IMPC, KOMP, IMSR, MMRRC, EMMA. Because ARDS has no causal gene, **no knockout "models ARDS"** — each models a step in the chain, and `modeled_mechanisms` should point at that specific node with an honest `relationship` (usually `PERTURBS`, not `RECAPITULATES`).

### Non-animal / NAM systems (these belong in `experimental_models:`, not `animal_models:`)

- **Human alveolar epithelial cell lines**: A549 (Cellosaurus CVCL_0023 ⚠️ — a lung adenocarcinoma line, an imperfect AT2 surrogate), NCI-H441, primary human alveolar type II cells.
- **Human pulmonary microvascular endothelial cells (HPMEC/HMVEC-L)** with trans-endothelial electrical resistance (TEER) and dextran-flux permeability readouts — directly measures chain step 5.
- **Air-liquid interface (ALI) cultures** of primary human airway/alveolar epithelium.
- **iPSC-derived AT2 organoids / alveolospheres** — currently the best system for step 7 (fluid clearance) and step 14a (AT2→AT1 repair).
- **Lung-on-a-chip** — the Ingber alveolus-chip reproduces cyclic mechanical strain plus a vascular compartment, uniquely capturing volutrauma (step 12) in a human-cell system.
- **Ex vivo lung perfusion (EVLP) of rejected human donor lungs** — the highest-fidelity human system available: measures alveolar fluid clearance directly in intact human tissue, and is where much of the MSC and β-agonist mechanistic work was done.
- **Precision-cut lung slices (PCLS)** from human tissue.

The existing KB entry already has an `experimental_models:` block; adding an `animal_models:` block with `modeled_mechanisms` links (targeting the bare node names listed in §6) would be the single highest-value structural addition.

### Research applications and limitations

Animal models have been reliable for testing **ventilation strategies** (VILI biology translated well — low tidal volume worked in animals and in humans) and unreliable for testing **pharmacotherapy** (dozens of agents that rescued LPS-treated mice have failed in humans). The honest framing for a `HUMAN_MODEL_MISMATCH` discussion: the models reproduce the injury but not the patient — no comorbidity, no age, no prior antibiotics, no concurrent organ failure, no 12-hour delay before treatment starts, and a genetically uniform host. The ATS report's "continuum" and "three of four domains" framework is the field's own attempt to fix the reporting side of this problem.

---

## Curation Recommendations for the dismech Entry

Highest-value additions to `kb/disorders/Acute_Respiratory_Distress_Syndrome.yaml`, roughly in order:

1. **`prevalence:`** — two structured records (LUNG SAFE period prevalence; Rubenfeld annual incidence), each with `measure_type` and a `notes:` line recording the definitional era. Verbatim snippets are available above for both.
2. **`environmental:`** — 8-10 exposures with `influences_mechanisms` links (bare-name targets). Run `just environmental-term-audit` first for ECTO reuse candidates. Remember the top-level `evidence:` gate.
3. **`animal_models:`** — LPS, acid aspiration, CLP, VILI, two-hit, with `modeled_mechanisms` links and PMID:35103557 as the framework citation.
4. **`genetic:`** — susceptibility-typed entries only (*FLT1*, *BORCS5*/*DUSP16*, *ACE*), with `inheritance:` bound to `HP:0010982` and a `notes:` line stating there is no causal gene.
5. **`clinical_trials:`** — the landmark set (NCT00527813 PROSEVA, NCT01731795 DEXA-ARDS, NCT00299650 ACURASYS, NCT02509078 ROSE, NCT01470703 EOLIA, NCT01374022 ART, NCT02713451 LOCO₂, NCT00281268 FACTT, NCT02010073 LUNG SAFE), all with `phase:` and `status:` as **enum values** (`PHASE_III`, `COMPLETED` — not "Phase III"/"Completed").
6. **`datasets:`** — currently empty; `just discover-datasets` then manual relevance triage, screening hard against neonatal RDS.
7. **`definitions:`** — the Global Definition, Berlin Definition, PALICC-2, and LIPS as a `PHENOTYPE_ALGORITHM` with `derivation_basis: ESTABLISHED_CRITERIA`.
8. **New `mechanistic_hypotheses` group** for the hyperinflammatory/hypoinflammatory axis, with `downstream[].hypothesis_groups` opting the relevant edges in.
9. **Two new pathophysiology nodes**: impaired alveolar fluid clearance (ENaC/Na⁺-K⁺-ATPase failure) and systemic cytokine spillover → MODS.
10. **`discussions:` with `kind: HUMAN_MODEL_MISMATCH`** for the animal-model translation failure, and `kind: KNOWLEDGE_GAP` for the DAD/clinical-syndrome discordance and the unexplained diabetes-protective effect.

Before any PR: `just validate`, `just count-verified-snippets`, `just validate-terms`, then the batched `just validate-disorders`. Every quoted snippet above that is *not* flagged `[unquoted]` was retrieved verbatim in this session and should survive the reference validator, but fetch each PMID's cache with `just fetch-reference` and re-check — whitespace normalisation and folded-scalar hyphenation are the usual failure modes, and square brackets inside snippets pass locally while failing CI.

---

## Sources

- [A New Global Definition of Acute Respiratory Distress Syndrome — PubMed](https://pubmed.ncbi.nlm.nih.gov/37487152/)
- [Experts Propose New Global Definition of ARDS — American Thoracic Society](https://site.thoracic.org/about-us/news/experts-propose-new-global-definition-of-acute-respiratory-distress-syndrome)
- [ESICM guidelines on acute respiratory distress syndrome — PubMed](https://pubmed.ncbi.nlm.nih.gov/37326646/)
- [Epidemiology, Patterns of Care, and Mortality for Patients With ARDS in ICUs in 50 Countries (LUNG SAFE) — PubMed](https://pubmed.ncbi.nlm.nih.gov/26903337/)
- [Acute respiratory distress syndrome — Nature Reviews Disease Primers](https://www.nature.com/articles/s41572-019-0069-0)
- [Latent Class Analysis of ARDS Subphenotypes — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4154544/)
- [EHR-Based Latent Profile Analysis in 24,363 ICU Admissions — AJRCCM](https://academic.oup.com/ajrccm/article/212/Supplement_1/aamag162.031/8679868)
- [Identifying a hyperinflammatory subphenotype of ARDS: may ferritin help? — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10980828/)
- [Update on the Features and Measurements of Experimental Acute Lung Injury in Animals — PubMed](https://pubmed.ncbi.nlm.nih.gov/35103557/)
- [Genomic and Genetic Approaches to Deciphering ARDS Risk and Mortality — PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC6939590)
- [Rare genetic variant risks in sepsis-associated ARDS — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13040698/)
- [Mesenchymal stromal cell therapy for COVID-19 ARDS: a double-blind RCT — PubMed](https://pubmed.ncbi.nlm.nih.gov/38409332/)
- [Allogeneic MSCs for Moderate to Severe ARDS: Phase 2b (STAT) — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360293/)
- [Pathophysiological mechanisms of ARDS: molecular to organ-level — Respiratory Research](https://link.springer.com/article/10.1186/s12931-025-03137-5)
- [Signaling pathways and potential therapeutic targets in ARDS — Respiratory Research](https://respiratory-research.biomedcentral.com/articles/10.1186/s12931-024-02678-5)
- [Unraveling the deadly dance: endothelial cells and neutrophils in sepsis-induced ALI/ARDS — Frontiers](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1551138/full)
- [ARDS Clinical Pipeline Expands with 50+ Companies — Medpath](https://trial.medpath.com/news/ards-clinical-pipeline-expands-with-50-companies-developing-novel-therapies)
- [Acute Respiratory Distress Syndrome — StatPearls, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK436002/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 46 |
| On topic | 40 |
| Off topic | 0 |

All extracted references resolved successfully.
