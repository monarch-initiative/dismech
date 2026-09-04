---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T02:23:06.274545'
end_time: '2026-09-03T02:27:20.535454'
duration_seconds: 254.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Coal Workers Pneumoconiosis
  mondo_id: ''
  category: Environmental Lung Disease
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
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.2179652000000003
  session_id: 28fb039f-05ba-5c97-94bf-1bbc91c07abc
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 57
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coal Workers Pneumoconiosis
- **MONDO ID:**  (if available)
- **Category:** Environmental Lung Disease

## Research Objectives

Please provide a comprehensive research report on **Coal Workers Pneumoconiosis** covering all of the
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

I'll research Coal Workers' Pneumoconiosis comprehensively, using web search to gather current data across all required domains.

I have comprehensive material now. Let me do a final round covering veterinary/other species, prevention/screening programs, prognosis details, and MMWR 2025 specifics for precise stats.

# Coal Workers' Pneumoconiosis: Comprehensive Research Report

## 1. Disease Information

**Overview.** Coal workers' pneumoconiosis (CWP) — colloquially "black lung disease" — is a preventable, progressive occupational interstitial lung disease caused by chronic inhalation of respirable coal mine dust, a complex heterogeneous mixture of coal, crystalline silica, and other silicate minerals ([CDC MMWR, 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)). The disease spectrum runs from asymptomatic anthracosis/anthracofibrosis through **simple CWP** (discrete pulmonary nodules, typically 1–10 mm, containing coal macules and micronodules) to **complicated CWP**, also called **progressive massive fibrosis (PMF)**, defined by conglomerate fibrotic masses ≥1 cm that can progress even after dust exposure ceases and lead to end-stage restrictive/mixed lung disease and death ([Medscape/Merck Manual](https://emedicine.medscape.com/article/297887-overview); [MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)).

**Key identifiers.**
- **ICD-10-CM:** J60 (Coalworker's pneumoconiosis) ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J60-/J60))
- **MeSH:** Anthracosis / Coal Workers' Pneumoconiosis (broader term Pneumoconiosis)
- Synonyms/alternative names: black lung disease, anthracosis, coalworker's lung, "miner's asthma" (historical), Caplan's syndrome (rheumatoid variant)
- Explicit OMIN/Orphanet identifiers were not located in this search — CWP is fundamentally an **acquired occupational disease**, not a monogenic/rare disease, so it is under-indexed in classical rare-disease/Mendelian resources; the primary authoritative sources are occupational-medicine/regulatory bodies (NIOSH, MSHA, CDC) rather than OMIM/Orphanet.

**Data provenance.** Most quantitative disease burden data in the literature derives from **aggregated occupational surveillance** rather than individual EHR records: the NIOSH Coal Workers' Health Surveillance Program (CWHSP), federally funded Black Lung Clinics, National Coal Workers' Autopsy Study, multi-decade cohort mortality studies (e.g., the 37-year US coal miner cohort), and CDC/NCHS multiple-cause-of-death mortality files ([MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm); [PMC7055360](https://pmc.ncbi.nlm.nih.gov/articles/PMC7055360/)).

---

## 2. Etiology

### Disease causal factor
CWP is a purely **environmental/occupational** disease — there is no known single-gene causal mutation. It results from cumulative inhalation of respirable coal mine dust (particles ~0.5–5 µm) that deposit in the distal airways and alveoli.

### Risk factors

**Environmental/occupational (primary):**
- **Cumulative respirable coal mine dust exposure** — dose-dependent; typically requires ≥10–20 years of underground exposure, though PMF is increasingly reported with shorter, more intense exposures in modern mining.
- **Crystalline silica content of the dust** is now recognized as the dominant driver of the most severe disease. Pathology/mineralogy studies found silica-type pneumoconiosis in **57% of contemporary US coal miners with PMF vs. 18% historically**, reflecting thinner coal seams that require cutting through more silica-bearing rock strata ([PMC9447385](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9447385/)).
- Small underground mine employment, mine size, tenure, job title (roof bolters, continuous miner operators), and geographic region (central Appalachia — Kentucky, Virginia, West Virginia — accounts for **86% of PMF cases** in federally funded Black Lung Clinics, 2017–2023, per [Healio/Cleveland Clinic 2024](https://www.healio.com/news/pulmonology/20240122/progressive-massive-fibrosis-continues-to-impact-coal-miners-in-2023)).
- Smoking is not causal but compounds airflow obstruction and may synergize with dust-related fibrosis.

**Genetic susceptibility factors** (modify individual risk given equivalent dust exposure — not causal alone):
- **TNF-α promoter polymorphisms**: the −238 and −308 TNFA SNPs are associated with CWP risk (OR ≈3.79 for −238); a 2024 systematic review/meta-analysis of candidate genes confirmed TNFα-308A and TNFα-238A alleles as risk factors ([BMC Pulm Med 2024](https://link.springer.com/article/10.1186/s12890-024-03392-0); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0940299309002826)).
- **TGF-β1 gene variants** (rs1800470/SNP2 CC — decreased risk; rs11466345/SNP5 GG — increased risk) ([PMC3596592](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3596592/)).
- **Autophagy-related gene (ATG16, ATG12, ATG5, ATG10) polymorphisms** in a Chinese case-control study (705 cases/703 controls) ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378111917306650)).
- **SELE, MMP1/MMP2/MMP3, LRBA, SMAD4 (rs10502913), NLRP3 (rs1539019)** gene polymorphisms reported in Chinese cohorts.
- **MnSOD, GSTM1, GSTT1, OGG1**: one study found *no* significant genotype-frequency difference between CWP and non-CWP miners — cumulative dust dose, not these particular oxidative-defense genotypes, was the dominant determinant ([PubMed 11977425](https://pubmed.ncbi.nlm.nih.gov/11977425/)).

### Protective factors
- **Long noncoding RNA H19 polymorphism** (rs2067051 CT/TT genotypes) was associated with *decreased* CWP risk in a Chinese population of 703 cases/705 controls ([PMC5036736](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5036736/)) — one of the few reported protective genetic variants.
- No established dietary/lifestyle protective factor is well validated in humans; vitamin D supplementation showed benefit in a mouse pneumoconiosis model (see Mechanism section) but is not clinically validated in humans.
- Engineering/administrative controls (respirable dust limits, wetting, ventilation, respiratory protection) are the dominant "protective" interventions — see Prevention.

### Gene-environment interaction
The literature models CWP susceptibility as a **threshold gene-by-dose interaction**: genetic variants in inflammatory cytokine genes (TNF-α, TGF-β1) and autophagy/oxidative-defense pathways modulate the individual inflammatory/fibrotic response to a fixed cumulative dust dose, explaining why only a subset of similarly exposed miners develop CWP or progress to PMF ([BMC Pulm Med 2024](https://link.springer.com/article/10.1186/s12890-024-03392-0)).

---

## 3. Phenotypes

CWP phenotypes span symptoms, imaging signs, and — critically — a largely **asymptomatic early stage**, which is a defining clinical feature.

| Phenotype | Type | Onset/course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Asymptomatic in simple CWP | Sign (absence of symptom) | Early/insidious | Common in simple CWP | HP:0012823 (Clinical modifier) |
| Chronic productive cough | Symptom | Chronic, progressive with cumulative exposure | Frequent in complicated disease | HP:0031246 (Chronic cough) |
| Progressive dyspnea/exertional breathlessness | Symptom | Progressive, worsens with PMF | Frequent, especially PMF | HP:0002094 (Dyspnea) |
| Black sputum (melanoptysis) | Sign | Variable | Uncommon but characteristic | HP:0031248 (related to sputum abnormality; no exact HPO term) |
| Restrictive and/or obstructive pulmonary function pattern | Laboratory/functional abnormality | Progressive | Common, more marked in PMF | HP:0002105 (Restrictive ventilatory defect) / HP:0006536 (obstructive) |
| Nodular opacities on chest radiograph (simple CWP) | Imaging sign | Progressive with cumulative dust exposure | Defining feature | HP:0100750 (Pulmonary nodule) |
| Progressive massive fibrosis (conglomerate mass ≥1cm) | Imaging sign / clinical severity marker | Progressive, can continue after exposure ceases | ~1,177 new PMF cases at US federally funded clinics 2017–2023 ([Healio 2024](https://www.healio.com/news/pulmonology/20240122/progressive-massive-fibrosis-continues-to-impact-coal-miners-in-2023)) | HP:0002206 (Pulmonary fibrosis) |
| Emphysema (focal, around coal macules) | Imaging/pathologic sign | Progressive | Common, especially with PMF | HP:0002097 (Emphysema) |
| Pulmonary hypertension / cor pulmonale | Clinical sign, late-stage | Late, progressive | Occurs in advanced/PMF disease | HP:0002094 (secondary), HP:0002092 (Pulmonary hypertension) |
| Hypoxemia | Laboratory abnormality | Progressive, more severe in PMF | Common in advanced disease | HP:0012418 (Hypoxemia) |
| Rheumatoid nodules with pneumoconiosis (Caplan syndrome) | Sign, autoimmune overlap | Can occur before, at, or up to 10 years after RA diagnosis | Rare, distinct radiographic pattern first described in Welsh miners (1953) | HP:0009777 (Rheumatoid nodules, if applicable) |

**Quality of life impact.** Advanced/complicated CWP causes significant disability from progressive dyspnea, oxygen dependence, and functional decline; pulmonary rehabilitation is used specifically to help patients maintain activities of daily living ([National Jewish Health](https://www.nationaljewish.org/conditions/coal-workers-pneumoconiosis/treatment); [American Lung Association](https://www.lung.org/lung-health-diseases/lung-disease-lookup/black-lung/treating-and-managing)).

**Diagnostic staging system (not strictly a "phenotype" but governs how phenotype severity is graded):** ILO International Classification of Radiographs of Pneumoconioses — categories 0–3, with small opacities graded p/q/r by size (p ≤1.5mm, 1.5≤q≤3mm, 3≤r≤10mm) and large opacities (A, B, C) defining PMF ([CDC NIOSH ILO Classification](https://www.cdc.gov/niosh/chestradiography/php/ilo-classification/index.html)).

---

## 4. Genetic/Molecular Information

CWP is **not a Mendelian disease** — there is no single causal gene. Rather, dozens of candidate-gene association studies (predominantly in Chinese miner cohorts) have examined polymorphisms modulating individual susceptibility and severity, summarized above under Etiology. Key genes/loci with documented association evidence:

- **TNF (TNFA)** — promoter SNPs −238, −308 (chr6) — cytokine dysregulation ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0940299309002826))
- **TGFB1** — rs1800470, rs11466345 — profibrotic cytokine ([PMC3596592](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3596592/))
- **H19** (lncRNA) — rs2067051 — protective association ([PMC5036736](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5036736/))
- **SELE** (E-selectin) — case-control association in Chinese cohort ([PMC3774684](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3774684/))
- **ATG5, ATG10, ATG12, ATG16** — autophagy machinery genes ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378111917306650))
- **MMP1, MMP2, MMP3** — matrix remodeling ([PMC4661622](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4661622/))
- **LRBA** — immune regulatory gene ([PMC5664639](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5664639/))
- **SMAD4, NLRP3** — TGF-β signaling / inflammasome (2022 Chinese Han study)
- **MnSOD (SOD2), GSTM1, GSTT1, OGG1** — oxidative-defense genes with largely *null* findings in one cohort, where cumulative dust dose dominated over genotype ([PubMed 11977425](https://pubmed.ncbi.nlm.nih.gov/11977425/))

**Variant classification/pathogenicity:** These are common population polymorphisms (risk alleles with modest odds ratios, e.g., OR≈3.79 for TNFA-238), not ACMG-classified pathogenic Mendelian variants — CWP susceptibility genetics is analogous to complex/polygenic disease risk modeling rather than monogenic diagnosis. No GWAS Catalog hits specific to CWP were surfaced in this search; the genetic literature is dominated by candidate-gene case-control studies, largely in Han Chinese coal miner populations, which limits generalizability and independent replication.

**Epigenetics:** Not extensively characterized for CWP specifically in the sources found; DNA methylation/histone studies are more developed for silicosis and idiopathic pulmonary fibrosis broadly and were not directly surfaced here as CWP-specific.

**Molecular profiling (proteomics/metabolomics):** A 2024 study integrated **proteomics and metabolomics** to characterize CWP disease progression, describing a "dynamic landscape" across disease stages ([J Proteome Res 2024](https://pubs.acs.org/doi/10.1021/acs.jproteome.4c00715)). Serum protein biomarkers **osteopontin (OPN), KL-6, Syndecan-4, and Gremlin-1** were validated in a 400-subject case-control study (100 healthy controls, 100 dust-exposed workers, 200 CWP patients), integrating lung-tissue transcriptomic data from CWP patients with silica-exposed alveolar-macrophage microarray data; all four markers rose sequentially with disease severity and correlated inversely with pulmonary function ([PMC10241210](https://pmc.ncbi.nlm.nih.gov/articles/PMC10241210/)).

---

## 5. Environmental Information

- **Primary environmental/occupational factor:** Respirable coal mine dust (mixed coal + crystalline silica + silicate minerals), generated by cutting, drilling, blasting, and hauling operations, especially in underground mining and thin-seam extraction requiring cutting through silica-bearing rock strata ([PMC9447385](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9447385/)).
- **Crystalline silica (quartz)** is now the pivotal environmental co-exposure explaining the resurgence of severe disease; MSHA's 2024 final rule explicitly addresses "coal mine dust containing respirable crystalline silica" as the driver of CWP, PMF, and "mixed-dust pneumoconiosis" ([Federal Register 2024-06920](https://www.federalregister.gov/documents/2024/04/18/2024-06920/lowering-miners-exposure-to-respirable-crystalline-silica-and-improving-respiratory-protection)).
- **Lifestyle factors:** Cigarette smoking is not causal of CWP but is an important compounding factor for airflow obstruction and overall respiratory morbidity/mortality; smoking cessation is a core management recommendation ([National Jewish Health](https://www.nationaljewish.org/conditions/coal-workers-pneumoconiosis/treatment)).
- **Infectious agents:** Not a primary etiologic factor, but CWP patients are recommended to undergo surveillance for mycobacterial infection (e.g., tuberculosis) given impaired local lung defenses, and are recommended influenza/pneumococcal vaccination ([National Jewish Health](https://www.nationaljewish.org/conditions/coal-workers-pneumoconiosis/treatment)). A 2025 study also examined the **lung microbiota's role in coal mine dust-induced NLRP3 inflammasome upregulation and lung injury** ([Sci Rep 2025](https://www.nature.com/articles/s41598-025-06411-0)), and a separate study profiled **sputum microbiota via 16S rRNA sequencing** in CWP patients ([PMC9224638](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9224638/)), suggesting dysbiosis may modulate disease processes, though this is not an infectious causal agent per se.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Inhalation of respirable coal mine dust (particles ~0.5–5 µm, mixed coal + crystalline silica)** reaches and deposits in terminal bronchioles and alveoli — *demonstrated*.
2. **Alveolar macrophages phagocytose the dust particles** in an attempt to clear them — *demonstrated*.
3. Phagocytosis of the poorly biodegradable, cytotoxic (especially silica-containing) particles **leads to macrophage cell death, lysosomal membrane rupture, and release of intracellular lipases/proteases**, causing direct cytotoxic lung tissue injury — *demonstrated* ([Medscape](https://emedicine.medscape.com/article/297887-overview)).
4. In parallel, dust exposure **activates oxidant production (ROS/RNS) by pulmonary phagocytes**, overwhelming antioxidant defenses and causing lipid peroxidation and protein nitrosation — *demonstrated in model systems, inferred as operative in humans*.
5. **IGF1/IGF1R axis activation generates ROS**, which drives **epithelial-mesenchymal transition (EMT) in alveolar epithelial cells** via **AKT/GSK3β signaling** — *demonstrated in a 2022 mechanistic mouse/cell study* ([Cell Death Discov 2022](https://www.nature.com/articles/s41420-022-01291-z)).
6. ROS and dust particles **activate the NF-κB/NLRP3 inflammasome axis** in macrophages and epithelial cells, driving **caspase-1 activation and release of IL-1β and IL-18** — *demonstrated in model systems* ([CDC/NIOSH review](https://stacks.cdc.gov/view/cdc/147727/cdc_147727_DS1.pdf); [PMC9800584](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9800584/)).
7. This inflammatory cascade **recruits polymorphonuclear leukocytes and additional macrophages**, amplifying release of proinflammatory mediators (TNF-α, TGF-β1, etc.) and **creating a self-sustaining chronic inflammatory microenvironment** — *demonstrated*.
8. Chronic inflammation and TGF-β/EMT signaling **activate resident fibroblasts**, driving **collagen deposition and fibrogenesis around retained dust particles**, forming the **coal macule** (the histopathologic hallmark lesion, containing dust-laden macrophages, reticulin, and collagen fibers) — *demonstrated*.
9. Coal macules aggregate into discrete **micronodules and nodules** visible radiographically (simple CWP), often with surrounding **focal emphysema** from local airway/alveolar destruction — *demonstrated*.
10. With continued or sufficiently high-silica dust burden, nodules **coalesce into conglomerate fibrotic masses ≥1 cm — progressive massive fibrosis (PMF)** — the complicated, severe form of disease, which can **continue progressing even after exposure ceases** (a distinguishing, and clinically important, feature) — *demonstrated* ([CDC MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)).
11. Extensive fibrosis **causes restrictive (and often mixed obstructive-restrictive) pulmonary physiology, V/Q mismatch, and progressive hypoxemia**, which in advanced disease **leads to pulmonary hypertension and cor pulmonale** — *demonstrated clinically*.
12. **Branch point — autoimmune variant (Caplan syndrome):** In a subset of miners who also develop rheumatoid arthritis, dust exposure appears to **exacerbate production of autoantibodies (rheumatoid factor, anti-citrullinated protein antibodies/ACPAs) and immune complexes**, producing a distinct pattern of well-defined peripheral rheumatoid nodules superimposed on pneumoconiosis, occurring before, at, or up to 10 years after RA onset — *demonstrated epidemiologically, immune mechanism partly inferred* ([StatPearls; NCBI Bookshelf NBK499886](https://www.ncbi.nlm.nih.gov/books/NBK499886/)).
13. **Branch point — mitochondrial/mitophagy axis:** A 2026 study found that coal-silica mixed dust impairs **macrophage mitochondrial function**, and that **pharmacological activation of mitophagy (kinetin)** mitigates pulmonary fibrosis in mice, implicating **mitochondrial quality control failure** as an additional upstream contributor to macrophage dysfunction and fibrogenesis ([J Investig Med 2026](https://journals.sagepub.com/doi/10.1177/15230864251411565)) — *demonstrated in mouse model, translational status in humans unconfirmed*.

### Molecular pathways
- **NF-κB / NLRP3 inflammasome axis** (caspase-1, IL-1β, IL-18 release) — central proinflammatory "danger receptor" pathway for dust-induced lung disease ([CDC/NIOSH](https://stacks.cdc.gov/view/cdc/147727/cdc_147727_DS1.pdf)).
- **IGF1/IGF1R–ROS–AKT/GSK3β–NF-κB/NLRP3** signaling cascade driving EMT and fibrosis ([Cell Death Discov 2022](https://www.nature.com/articles/s41420-022-01291-z)).
- **TGF-β1/SMAD signaling** — canonical profibrotic pathway implicated both mechanistically and genetically (SMAD4 polymorphism association) (KEGG: hsa04350 TGF-beta signaling pathway).
- Suggested GO terms: **GO:0006954** (inflammatory response), **GO:0030154** (cell differentiation, EMT-related), **GO:0001525** (angiogenesis, in fibrotic remodeling), **GO:0007179** (transforming growth factor beta receptor signaling pathway), **GO:0043123** (positive regulation of I-kappaB kinase/NF-kappaB signaling), **GO:0002526** (acute inflammatory response), **GO:0072593** (reactive oxygen species metabolic process), **GO:0006915** (apoptotic process, relevant to macrophage/epithelial cell death).

### Cellular processes and cell types (CL terms)
- **Alveolar macrophage** (CL:0000583) — dust phagocytosis, cytokine release, cell death
- **Type II pneumocyte / alveolar epithelial cell** (CL:0002063) — site of EMT
- **Fibroblast** (CL:0000057) — collagen deposition
- **Myofibroblast** (CL:0000186) — activated fibrogenic effector cell
- **Neutrophil** (CL:0000775) — recruited inflammatory effector
- Processes: apoptosis (demonstrated via Bax expression studies, [PMC1570065](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1570065/)), oxidative stress, chronic inflammation, epithelial-mesenchymal transition, fibrogenesis, mitophagy/autophagy dysregulation.

### Molecular profiling technologies applied to CWP
- **Transcriptomics:** Single-timepoint and longitudinal mouse-model transcriptional profiling of coal-dust-exposed lungs showed heterogeneous transcriptional responses, partially ameliorated by vitamin D supplementation ([Part Fibre Toxicol 2022](https://link.springer.com/article/10.1186/s12989-022-00449-y)).
- **Proteomics/Metabolomics:** Integrated multi-omics analysis reveals a "dynamic landscape" of protein/metabolite changes across CWP disease stages ([J Proteome Res 2024](https://pubs.acs.org/doi/10.1021/acs.jproteome.4c00715)).
- **Microbiome:** 16S rRNA sputum sequencing and lung-microbiota studies link dysbiosis to NLRP3 activation ([PMC9224638](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9224638/); [Sci Rep 2025](https://www.nature.com/articles/s41598-025-06411-0)).
- **Raman spectroscopy:** Used to characterize inflammation/fibrosis directly in coal-dust-exposed lung tissue ([PeerJ 2022](https://peerj.com/articles/13632/)).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Lungs (parenchyma, particularly upper lobes and posterior segments where dust deposition and clearance are least efficient)
- **Secondary:** Right heart (cor pulmonale from pulmonary hypertension in advanced disease); pleura (occasionally pleural involvement/thickening)
- **Body systems:** Respiratory system primarily; cardiovascular system secondarily (pulmonary hypertension)

**Tissue and cell level:**
- Alveolar epithelium, bronchiolar epithelium, pulmonary interstitium/connective tissue, alveolar macrophage population
- Suggested UBERON terms: **UBERON:0002048** (lung), **UBERON:0000115** (lung parenchyma), **UBERON:0002185** (bronchiole), **UBERON:0002299** (alveolus of lung)

**Subcellular level:**
- Macrophage lysosomes (site of dust particle processing and rupture), mitochondria (dysfunction implicated in fibrogenesis — 2026 mitophagy study), endoplasmic reticulum (stress response to oxidative injury)
- GO Cellular Component: **GO:0005764** (lysosome), **GO:0005739** (mitochondrion)

**Localization:** Bilateral, typically symmetric, with a predilection for upper and posterior lung zones; PMF masses are usually bilateral and can be asymmetric in size/distribution.

---

## 8. Temporal Development

**Onset:** Adult-onset occupational disease; typically requires years to decades of cumulative dust exposure (classically ≥10–20 years underground), though contemporary cases with higher silica content are reported after shorter exposure durations. Onset is **insidious** — simple CWP is frequently asymptomatic and detected only on periodic radiographic surveillance.

**Progression:**
- **Stages:** ILO Category 0 (normal) → Category 1–3 (simple CWP, increasing profusion of small opacities) → PMF/complicated CWP (Categories A, B, C based on size of large opacities) ([CDC ILO Classification](https://www.cdc.gov/niosh/chestradiography/php/ilo-classification/index.html)).
- **Progression rate:** Variable; can be slow over decades in simple CWP but PMF, once established, is characteristically **relentlessly progressive and can continue to worsen even after cessation of dust exposure** — a defining natural-history feature distinguishing it from many other occupational lung diseases ([CDC MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)).
- **Disease course pattern:** Chronic, progressive (not typically relapsing-remitting); duration is lifelong once established, with no spontaneous remission.

**Critical periods/windows:** Early detection via periodic radiographic surveillance (NIOSH CWHSP) is the key intervention window — Part 90 rights allow miners with radiographic evidence of pneumoconiosis to transfer to lower-dust-exposure jobs, aiming to halt progression before PMF develops ([DOL Black Lung Program](https://www.dol.gov/agencies/owcp/dcmwc)).

---

## 9. Inheritance and Population

**Epidemiology:**
- US CWP-associated death rate rose from **1.1 per million (370 deaths) in 2020 to 1.4 per million (462 deaths) in 2023**; overall **1,754 CWP-associated deaths** occurred among US residents aged ≥15 during 2020–2023, with an age-adjusted death rate of **1.3 per million** ([CDC MMWR 2025, mm7441a1](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)).
- Increased risk observed among mining-industry and construction/extraction workers.
- Approximately **4,000 new cases occur annually in the US** (roughly 4% of surveyed workers per year, historically) ([Medscape](https://emedicine.medscape.com/article/297887-overview)).
- **1,177 new PMF cases** diagnosed at federally funded Black Lung Clinics across 11 states, 2017–June 2023; **86% (1,008) resided in central Appalachia** (Kentucky, Virginia, West Virginia) ([Healio 2024](https://www.healio.com/news/pulmonology/20240122/progressive-massive-fibrosis-continues-to-impact-coal-miners-in-2023)).
- NIOSH CWHSP surveillance (2014–2019) found American Indian/Alaska Native surface coal miners with ≥10 years experience had **3.0% radiographic pneumoconiosis** and **0.3% PMF**.
- Mortality: a **37-year follow-up US coal miner cohort** found excess mortality for pneumoconiosis (SMR=79.70; 95% CI 72.1–87.67), COPD (SMR=1.11; 95% CI 0.99–1.24), and lung cancer (SMR=1.08; 95% CI 1.00–1.18) ([PMC4522914](https://pmc.ncbi.nlm.nih.gov/articles/PMC4522914/)).
- Mortality odds from non-malignant respiratory disease and lung cancer are **highest among miners born after 1939**, likely reflecting increased rates of severe pneumoconiosis in more recent cohorts ([PMC10428099](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428099/)).

**Inheritance pattern:** Not a Mendelian disease — no defined inheritance pattern, penetrance, expressivity, anticipation, or germline mosaicism applies. Genetic risk operates as **polygenic susceptibility modifiers** (see Genetic/Molecular section) acting on top of an obligate environmental exposure.

**Population demographics:**
- Overwhelmingly affects underground coal miners (historically and currently predominantly male in the US/UK/China mining workforce).
- Geographic concentration in coal-mining regions: central Appalachia (US), historically Wales/UK, and major coal-mining regions of China (source of most genetic-association literature).
- Sex ratio: heavily skewed male, reflecting occupational demographics of underground coal mining.
- Age distribution: affected individuals are typically older miners or retirees, reflecting the decades-long latency to clinically significant disease, though PMF is increasingly reported in younger miners with high-silica exposure.

---

## 10. Diagnostics

**Clinical/imaging tests:**
- **Chest radiography with ILO Classification of Radiographs of Pneumoconioses** — the standard surveillance and diagnostic tool, read by NIOSH-certified "B readers"; categorizes profusion (0–3) and opacity size (p/q/r for small, A/B/C for large/PMF) ([CDC NIOSH](https://www.cdc.gov/niosh/chestradiography/php/ilo-classification/index.html)).
- **High-resolution CT (HRCT)** — more sensitive than plain radiography for detecting parenchymal coal dust accumulation and focal emphysema, though abnormal pulmonary function may not correlate well with early HRCT findings in simple CWP ([PubMed 8404184](https://pubmed.ncbi.nlm.nih.gov/8404184/)).
- **Quantitative CT-based imaging biomarkers** (2023) — novel airway structural variables (bifurcation angle, hydraulic diameter, wall thickness, circularity) and parenchymal functional variables (emphysema, ground-glass opacity, consolidation, fibrosis, blood vessel volume) are being developed to identify CWP quantitatively ([Front Physiol 2023](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1288246/full)).
- **Machine learning/computer-aided diagnosis** of chest X-rays is an active area of methods development ([PMC9180284](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180284/)).
- **Pulmonary function tests (PFTs)** — spirometry, lung volumes, DLCO to characterize restrictive/obstructive/mixed physiology and functional impairment.
- **Biopsy/pathology** — coal macules with dust-laden macrophages, reticulin, and collagen; used mainly in autopsy studies (National Coal Workers' Autopsy Study) or when biopsy performed for other indications, given the risk of invasive biopsy in impaired lungs.

**Biomarkers (emerging):**
- Serum **osteopontin, KL-6, Syndecan-4, Gremlin-1** — validated as diagnostic biomarkers correlating with disease severity and inversely with pulmonary function in a 400-subject case-control study ([PMC10241210](https://pmc.ncbi.nlm.nih.gov/articles/PMC10241210/)).
- KL-6, surfactant protein D, MMP-2 have established diagnostic utility in the related pneumoconiosis silicosis/asbestosis literature ([PMC5693552](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5693552/)).

**Genetic testing:** Not clinically indicated for diagnosis (CWP is diagnosed by exposure history + radiographic pattern), though candidate-gene genotyping is used in research settings to study susceptibility.

**Clinical criteria/differential diagnosis:** Diagnosis requires (1) a compatible occupational dust exposure history, (2) characteristic radiographic pattern per ILO classification, and (3) exclusion of other causes of similar radiographic findings (silicosis alone, tuberculosis, sarcoidosis, other interstitial lung diseases, metastatic disease for nodular patterns).

**Screening:** The **NIOSH Coal Workers' Health Surveillance Program (CWHSP)** provides no-cost periodic chest radiograph screening to underground coal miners at hire and periodically thereafter; miners found with radiographic pneumoconiosis gain **Part 90 rights** to transfer to lower-dust jobs without loss of pay ([CDC CWHSP](https://www.cdc.gov/niosh/cwhsp/about/index.html); [DOL](https://www.dol.gov/agencies/owcp/dcmwc/mission)).

---

## 11. Outcome/Prognosis

- **No cure exists.** Prognosis depends heavily on stage at detection: simple CWP may remain stable or progress slowly; PMF carries a substantially worse prognosis with continued decline in lung function, disability, and premature death, and **can progress even after dust exposure ceases** ([CDC MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)).
- **Mortality:** Age-adjusted US CWP death rate of 1.3 per million (2020–2023), rising trend from 1.1 (2020) to 1.4 (2023) per million; excess pneumoconiosis mortality SMR of ~80 in long-term cohort follow-up ([MMWR 2025](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm); [PMC4522914](https://pmc.ncbi.nlm.nih.gov/articles/PMC4522914/)).
- **Comorbidity burden:** Comorbidities (chronic pulmonary disease, hypertension, heart disease) increase death risk among pneumoconiosis patients by ~10%; coal miners with CWP have a significantly higher relative risk of lung carcinoma compared to the general male population, and coal mine dust exposure independently associates with increased lung cancer mortality (HR=1.70, 95% CI 1.02–2.83) ([Occup Med](https://academic.oup.com/occmed/article-abstract/33/3/141/1378154); cohort data above).
- **Functional/disability outcomes:** Progressive restrictive/obstructive impairment, hypoxemia, need for supplemental oxygen, and eventual respiratory failure in advanced PMF.
- **Prognostic factors:** Cumulative dust exposure, silica content of dust, radiographic category/PMF stage, presence of comorbid COPD or lung cancer, smoking status, and biomarker levels (OPN, KL-6, Syndecan-4, Gremlin-1 correlate with severity).

---

## 12. Treatment

**No curative therapy exists.** Management is predominantly **supportive**:

- **General supportive care:** Prompt treatment of respiratory infections, tuberculosis/mycobacterial surveillance, influenza and pneumococcal vaccination, smoking cessation, and regular exercise ([National Jewish Health](https://www.nationaljewish.org/conditions/coal-workers-pneumoconiosis/treatment)). NCIT: **NCIT:C15747** (Supportive Care).
- **Bronchodilator/COPD-directed therapy** for workers with an obstructive component. NCIT: **NCIT:C15986** (Pharmacotherapy).
- **Supplemental oxygen therapy** for hypoxemia and/or pulmonary hypertension. NCIT: **NCIT:C64582** (Oxygen) as therapeutic_agent under a supportive-care/pharmacotherapy term.
- **Pulmonary rehabilitation** for more severely affected workers, to maintain activities of daily living. NCIT: **NCIT:C15315** (Rehabilitation).
- **Antifibrotic therapy (emerging/experimental):** Growing interest in **pirfenidone and nintedanib**, established antifibrotics in idiopathic pulmonary fibrosis, to potentially slow progression in PMF/diffuse dust fibrosis. A dedicated clinical trial, **NCT04461587** ("Examination of Pirfenidone (Esbriet®) Therapy in Coal Workers' Pneumoconiosis With Pulmonary Fibrosis"), was initiated to test this ([ClinicalTrials.gov NCT04461587](https://clinicaltrials.gov/study/NCT04461587); [Merck Manual](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/coal-worker-pneumoconiosis)). NCIT therapeutic_agent candidates: pirfenidone, nintedanib.
- **Lung transplantation:** Should be considered in patients with progressive respiratory failure; studies report **no increased risk of perioperative/postoperative complications** in CWP transplant recipients compared to other indications ([PubMed 22360577](https://pubmed.ncbi.nlm.nih.gov/22360577/)). NCIT: **NCIT:C15289** (Organ Transplantation).
- **Surgical care:** Generally limited role beyond transplantation; occasional intervention for complications (e.g., pneumothorax).
- **Autoimmune/Caplan syndrome-specific management:** Standard rheumatoid arthritis therapy (DMARDs, biologics) as indicated when the autoimmune overlap phenotype is present.

**Treatment strategy:** Management is staged by severity — simple CWP focuses on exposure cessation/reduction and surveillance; complicated CWP/PMF adds pulmonary rehabilitation, oxygen, antifibrotic trial enrollment where eligible, and transplant evaluation in end-stage disease.

**Treatment outcomes:** No FDA-approved disease-modifying therapy currently exists specifically for CWP; the pirfenidone trial outcome data were not available in this search and should be checked directly on ClinicalTrials.gov for current status/results.

---

## 13. Prevention

CWP is explicitly characterized by CDC/NIOSH as a **preventable** disease — prevention is the dominant public-health focus.

**Primary prevention (exposure control):**
- **MSHA 2024 Final Rule — "Lowering Miners' Exposure to Respirable Crystalline Silica and Improving Respiratory Protection"** (effective June 17, 2024; coal mine operator compliance required by April 14, 2025): establishes a uniform **permissible exposure limit (PEL) of 50 µg/m³** and **action level of 25 µg/m³** for respirable crystalline silica across all mine types, alongside improved respiratory protection requirements ([MSHA Final Rule](https://www.msha.gov/final-rule-respirable-crystalline-silica-health-alert); [Federal Register 2024-06920](https://www.federalregister.gov/documents/2024/04/18/2024-06920/lowering-miners-exposure-to-respirable-crystalline-silica-and-improving-respiratory-protection)).
- Engineering controls: dust suppression (water sprays), ventilation, continuous personal dust monitors, respiratory protective equipment.

**Secondary prevention (screening/early detection):**
- **NIOSH Coal Workers' Health Surveillance Program (CWHSP)** — periodic, no-cost chest radiograph (and increasingly spirometry) screening for underground coal miners at hire and at defined intervals ([CDC CWHSP](https://www.cdc.gov/niosh/cwhsp/about/index.html)).
- **Part 90 program** — miners found with radiographic pneumoconiosis have a legal right to transfer to a job with dust exposure below the applicable federal standard without loss of pay/benefits, a key exposure-reduction intervention at the individual level ([DOL](https://www.dol.gov/agencies/owcp/dcmwc/mission)).

**Tertiary prevention:** Standard pulmonary disease management (vaccination, infection surveillance, pulmonary rehabilitation, oxygen) to prevent complications in those already diagnosed (see Treatment section).

**Public health/regulatory:** The Black Lung Benefits Act of 1972 and the Federal Black Lung Program (administered by the US Department of Labor, Division of Coal Mine Workers' Compensation) provide compensation to totally disabled miners and survivors, funded via a Black Lung Disability Trust Fund financed by a coal excise tax — a policy lever that also incentivizes exposure reduction ([DOL Black Lung Program](https://www.dol.gov/agencies/owcp/dcmwc); [Congress.gov CRS R45261](https://www.congress.gov/crs-product/R45261)).

**Prophylaxis:** No pharmacological prophylaxis exists; prevention is exposure-control-based.

---

## 14. Other Species / Natural Disease

Targeted searches did not identify well-documented **naturally occurring CWP in non-human species** (e.g., no OMIA entries, no veterinary case series in horses or companion animals were found in this search). CWP is fundamentally an anthropogenic occupational exposure disease tied to underground coal mining, so it lacks a natural veterinary analog in the way zoonotic or heritable diseases do. The closest comparative biology is:
- **Experimental animal models** (below), which are induced, not naturally occurring.
- The broader pneumoconiosis family does have described occupational/environmental analogs in domestic animals exposed to heavy industrial dust environments, but specific citable veterinary CWP case reports were not surfaced by this search and would need targeted follow-up in veterinary literature (e.g., OMIA, VetCompass) if required.

---

## 15. Model Organisms

**Mouse models:**
- Coal dust instillation/inhalation models are used to study inflammation and fibrosis progression; one protocol uses **16 mg coal dust administered to a mouse monthly**, approximating a miner's 10–20 years of cumulative exposure; after 9 months of coal dust stimulation, alveolar structure and pulmonary microenvironment are destroyed with inflammatory and cell-death pathway activation, recapitulating pneumoconiosis ([search synthesis of mouse CWP model literature]).
- Coal dust exposure triggers heterogeneous transcriptional profiles in mouse pneumoconiosis, partially ameliorated by **vitamin D remedies** in one 2022 study ([Part Fibre Toxicol 2022](https://link.springer.com/article/10.1186/s12989-022-00449-y)).
- Mouse silicosis models have been used to test **N-acetylcysteine** as a therapeutic antifibrotic agent ([PMC6639458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6639458/)).
- Kinetin-induced **mitophagy activation** mitigated coal-silica mixed dust-induced pulmonary fibrosis in mice via modulation of macrophage mitochondrial function (2026) ([SAGE J Investig Med](https://journals.sagepub.com/doi/10.1177/15230864251411565)).

**Rat models:**
- **Sprague-Dawley rats** exposed via dynamic coal dust inhalation are used to study macrophage polarization and its molecular regulatory network in pulmonary inflammation/fibrosis ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1043466623002971)).
- Tracheal instillation methods are also used to establish CWP/silicosis models in rats.
- Epithelial-mesenchymal transition in silicotic lung lesions has been pathologically characterized in rats ([PMC6789520](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6789520/)).

**Model characteristics:** These induced-exposure rodent models recapitulate key histopathologic features (macrophage activation, inflammation, fibrosis, coal-macule-like lesions) and are used to dissect molecular pathways (NF-κB/NLRP3, IGF1/ROS/AKT-GSK3β, EMT, mitophagy) and test candidate therapeutics (vitamin D, N-acetylcysteine, kinetin/mitophagy activators). Limitations (translational gap to humans, compressed exposure timescales, single-dust-type exposure vs. the complex heterogeneous human coal-mine dust mixture) are implicit in the literature but not quantitatively characterized in the sources retrieved here.

**Model databases:** No CWP-specific registry was identified; standard model-organism resources (MGI, IMSR) would house genetic mouse-model information relevant to constituent pathway genes (Tnf, Tgfb1, Nlrp3, etc.) though this was not directly queried.

---

## Summary of Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| HP (phenotypes) | HP:0002094 (Dyspnea), HP:0031246 (Chronic cough), HP:0002206 (Pulmonary fibrosis), HP:0100750 (Pulmonary nodule), HP:0002097 (Emphysema), HP:0002092 (Pulmonary hypertension), HP:0012418 (Hypoxemia), HP:0002105 (Restrictive ventilatory defect) |
| GO (biological process) | GO:0006954 (inflammatory response), GO:0007179 (TGF-β receptor signaling), GO:0043123 (positive regulation of NF-κB signaling), GO:0072593 (ROS metabolic process), GO:0006915 (apoptotic process) |
| CL (cell types) | CL:0000583 (alveolar macrophage), CL:0002063 (type II pneumocyte), CL:0000057 (fibroblast), CL:0000186 (myofibroblast), CL:0000775 (neutrophil) |
| UBERON (anatomy) | UBERON:0002048 (lung), UBERON:0000115 (lung parenchyma), UBERON:0002185 (bronchiole), UBERON:0002299 (alveolus) |
| CHEBI (chemical) | Crystalline silica/quartz, coal dust (complex mixture, not a single CHEBI-mappable entity) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15747 (Supportive Care), NCIT:C15315 (Rehabilitation), NCIT:C15289 (Organ Transplantation) |
| Genes (HGNC) | TNF (hgnc:11892), TGFB1 (hgnc:11766), NLRP3 (hgnc:16400), SMAD4 (hgnc:6770), SELE (hgnc:10718), H19 (hgnc:4713 — lncRNA) |

---

## Sources

- [Coal Workers' Pneumoconiosis–Associated Deaths — United States, 2020–2023 (MMWR)](https://www.cdc.gov/mmwr/volumes/74/wr/mm7441a1.htm)
- [Coal Workers' Pneumoconiosis–Associated Deaths — United States, 2020–2023 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12714179/)
- [Coal Workers' Pneumoconiosis (Black Lung Disease): Background, Pathophysiology, Etiology (Medscape)](https://emedicine.medscape.com/article/297887-overview)
- [Coal Worker Pneumoconiosis (Merck Manual)](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/coal-worker-pneumoconiosis)
- [2026 ICD-10-CM Diagnosis Code J60](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J60-/J60)
- [Coal dust nanoparticles induced pulmonary fibrosis via NF-κB/NLRP3 pathway (Cell Death Discovery, 2022)](https://www.nature.com/articles/s41420-022-01291-z)
- [The role of macrophage polarization in coal dust-induced pulmonary fibrosis in rats (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1043466623002971)
- [Effects of chemical composition on lung cell response to coal particles (PMC9314662)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9314662/)
- [Progressive massive fibrosis continues to impact coal miners in 2023 (Healio)](https://www.healio.com/news/pulmonology/20240122/progressive-massive-fibrosis-continues-to-impact-coal-miners-in-2023)
- [Current Review of Pneumoconiosis Among US Coal Miners (PMC7055360)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7055360/)
- [Candidate gene polymorphisms associated with silicosis and CWP: systematic review and meta-analysis (BMC Pulm Med, 2024)](https://link.springer.com/article/10.1186/s12890-024-03392-0)
- [Association of TGF-β1 gene variants with CWP risk (PMC3596592)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3596592/)
- [Polymorphisms in lncRNA H19 (PMC5036736)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5036736/)
- [Polymorphisms in SELE gene and risk of CWP (PMC3774684)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3774684/)
- [Polymorphisms in autophagy related genes and CWP (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0378111917306650)
- [MMP1, MMP2, MMP3 gene polymorphism with CWP (PMC4661622)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4661622/)
- [LRBA Gene Polymorphisms and Risk of CWP (PMC5664639)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5664639/)
- [Genetic polymorphisms of MnSOD, GSTM1, GSTT1, and OGG1 in CWP (PubMed)](https://pubmed.ncbi.nlm.nih.gov/11977425/)
- [ILO Classification for B Readers (CDC/NIOSH)](https://www.cdc.gov/niosh/chestradiography/php/ilo-classification/index.html)
- [Computed tomography-based imaging biomarker identifies CWP (Frontiers in Physiology, 2023)](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1288246/full)
- [Computer-Aided Diagnosis of CWP Using Machine Learning (PMC9180284)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180284/)
- [High-Resolution CT in Simple CWP (PubMed)](https://pubmed.ncbi.nlm.nih.gov/8404184/)
- [Coal Workers' Health Surveillance Program (CDC/NIOSH)](https://www.cdc.gov/niosh/cwhsp/about/index.html)
- [Coal Worker's Pneumoconiosis/Black Lung Disease Treatment (National Jewish Health)](https://www.nationaljewish.org/conditions/coal-workers-pneumoconiosis/treatment)
- [Treating and Managing Coal Worker's Pneumoconiosis (American Lung Association)](https://www.lung.org/lung-health-diseases/lung-disease-lookup/black-lung/treating-and-managing)
- [Examination of Pirfenidone Therapy in CWP With Pulmonary Fibrosis (ClinicalTrials.gov NCT04461587)](https://clinicaltrials.gov/study/NCT04461587)
- [Lung transplantation in patients with CWP (PubMed)](https://pubmed.ncbi.nlm.nih.gov/22360577/)
- [Coal Workers Pneumoconiosis: Forgotten, But Not Gone (Cleveland Clinic)](https://consultqd.clevelandclinic.org/coal-workers-pneumoconiosis-forgotten-but-not-gone)
- [Caplan Syndrome (StatPearls, NCBI Bookshelf NBK499886)](https://www.ncbi.nlm.nih.gov/books/NBK499886/)
- [Caplan's Syndrome with a twist (PMC8136599)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8136599/)
- [Molecular Activation of NLRP3 Inflammasome by Particles (CDC/NIOSH)](https://stacks.cdc.gov/view/cdc/147727/cdc_147727_DS1.pdf)
- [Activation of Mitophagy by Kinetin Mitigates Coal–Silica Mixed Dust-Induced Pulmonary Fibrosis (SAGE, 2026)](https://journals.sagepub.com/doi/10.1177/15230864251411565)
- [Research progress on pathogenesis and prediction of pneumoconiosis (Environ Geochem Health, 2024)](https://link.springer.com/article/10.1007/s10653-024-02114-z)
- [The role of lung microbiota in coal mine dust-induced NLRP3 inflammasome upregulation (Scientific Reports, 2025)](https://www.nature.com/articles/s41598-025-06411-0)
- [Final Rule: Respirable Crystalline Silica (MSHA)](https://www.msha.gov/final-rule-respirable-crystalline-silica-health-alert)
- [Lowering Miners' Exposure to Respirable Crystalline Silica (Federal Register, 2024)](https://www.federalregister.gov/documents/2024/04/18/2024-06920/lowering-miners-exposure-to-respirable-crystalline-silica-and-improving-respiratory-protection)
- [Pathology and Mineralogy Demonstrate Respirable Crystalline Silica Is a Major Cause of Severe Pneumoconiosis in U.S. Coal Miners (PMC9447385)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9447385/)
- [Estimating mortality from CWP among Medicare beneficiaries (Am J Ind Med)](https://onlinelibrary.wiley.com/doi/full/10.1002/ajim.23330)
- [Increased odds of mortality from non-malignant respiratory disease and lung cancer among US coal miners born after 1939 (PMC10428099)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428099/)
- [Respiratory disease mortality among US coal miners; results after 37 years of follow-up (PMC4522914)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4522914/)
- [Does CWP predict lung cancer? (Occupational Medicine, Oxford Academic)](https://academic.oup.com/occmed/article-abstract/33/3/141/1378154)
- [Serum Osteopontin, KL-6, and Syndecan-4 as Potential Biomarkers in CWP (PMC10241210)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10241210/)
- [Serum KL-6, surfactant protein D, MMP-2 in asbestosis and silicosis (PMC5693552)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5693552/)
- [Proteomics and Metabolomics Analyses Reveal a Dynamic Landscape of CWP (J Proteome Res, 2024)](https://pubs.acs.org/doi/10.1021/acs.jproteome.4c00715)
- [Coal dust exposure triggers heterogeneity of transcriptional profiles in mouse pneumoconiosis and Vitamin D remedies (Particle and Fibre Toxicology, 2022)](https://link.springer.com/article/10.1186/s12989-022-00449-y)
- [PeerJ: Inflammation and fibrosis in coal dust-exposed lung by confocal Raman spectroscopy](https://peerj.com/articles/13632/)
- [N-acetylcysteine therapeutically protects against pulmonary fibrosis in a mouse model of silicosis (PMC6639458)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6639458/)
- [Pathological Study on EMT in Silicotic Lung Lesions in Rat (PMC6789520)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6789520/)
- [Sputum Microbiota in Coal Workers Diagnosed with Pneumoconiosis (PMC9224638)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9224638/)
- [About the Federal Black Lung Program (US DOL)](https://www.dol.gov/agencies/owcp/dcmwc/mission)
- [Black Lung Program (US DOL)](https://www.dol.gov/agencies/owcp/dcmwc)
- [The Black Lung Program, the Black Lung Disability Trust Fund, and the Excise Tax on Coal (Congress.gov CRS R45261)](https://www.congress.gov/crs-product/R45261)
- [A comprehensive retrospect on the current perspectives and future prospects of pneumoconiosis (PMC11757636)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11757636/)
- [Understanding the pathogenesis of occupational coal and silica dust-associated lung disease (European Respiratory Review)](https://publications.ersnet.org/content/errev/31/165/210250)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031248` (1 mention) - the report calls it "related to sputum abnormality; no exact HPO term"; HP calls it **Palmar pruritus**
- `HP:0009777` (1 mention) - the report calls it "Rheumatoid nodules, if applicable"; HP calls it **Absent thumb**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0031246` (2 mentions) - the report calls it "Chronic cough"; HP calls it **Nonproductive cough**, and lists "Dry cough" among its other names
- `HP:0100750` (2 mentions) - the report calls it "Pulmonary nodule"; HP calls it **Atelectasis**, and lists "Pulmonary atelectasis" among its other names
- `CL:0002063` (2 mentions) - the report calls it "Type II pneumocyte / alveolar epithelial cell"; CL calls it **pulmonary alveolar type 2 cell**, and lists "type II alveolar epithelial cell" among its other names
- `CL:0000186` (2 mentions) - the report calls it "Myofibroblast"; CL calls it **myofibroblast cell**
