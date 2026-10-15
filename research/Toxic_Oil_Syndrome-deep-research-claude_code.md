---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-19T01:41:55.077041'
end_time: '2026-09-19T01:45:58.600108'
duration_seconds: 243.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Toxic Oil Syndrome
  mondo_id: MONDO:0016421
  category: Environmental
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
  web_search_requests: 12
  num_turns: 13
  total_cost_usd: 1.1503988
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Toxic Oil Syndrome
- **MONDO ID:** MONDO:0016421 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Toxic Oil Syndrome** covering all of the
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

I now have sufficient primary-literature-grounded material to compile a comprehensive report. Here is the complete research report.

---

# Toxic Oil Syndrome (TOS): Comprehensive Disease Characteristics Report

## 1. Disease Information

**Overview.** Toxic Oil Syndrome (TOS, Spanish: *síndrome del aceite tóxico*, colloquially "lo de la colza") is a multisystem toxic-immunologic disease caused by ingestion of illegally sold, industrial rapeseed (colza) oil that had been denatured with 2% aniline for non-food/industrial use and then illegally re-refined and sold door-to-door as cheap "olive oil" in Spain in spring 1981 ([PubMed 6116011](https://pubmed.ncbi.nlm.nih.gov/6116011/?dopt=Abstract); [PubMed 6633617](https://pubmed.ncbi.nlm.nih.gov/6633617/)). It is a point-source environmental/toxicologic epidemic rather than an infectious or classically genetic disease, and virtually all epidemiological, clinical, and mechanistic data derive from a single, extensively studied Spanish cohort (aggregated disease-level surveillance/registry data plus individual clinical follow-up studies), not from ongoing EHR-based case ascertainment.

The illness is a three-phase syndrome: an **acute** toxic-allergic pneumonopathy (respiratory distress, interstitial/alveolar infiltrates, fever, myalgia, rash, eosinophilia), an **intermediate** phase (peripheral edema, skin induration, hepatic dysfunction, pulmonary hypertension), and a **chronic** phase (scleroderma-like skin sclerosis, peripheral neuropathy, joint contractures, sicca syndrome) that can persist for decades ([ScienceDirect S0190962288700468](https://www.sciencedirect.com/science/article/abs/pii/S0190962288700468); [PubMed 3961509](https://pubmed.ncbi.nlm.nih.gov/3961509/)).

**Key identifiers:**
- **MONDO:** MONDO:0016421
- **Orphanet:** ORPHA:227972 ("Toxic oil syndrome") — described as "a rare intoxication, due to consumption of a rapeseed oil denatured with aniline 2%, characterized by generalized vascular lesions affecting all organs and vessels... and presenting with severe incapacitating myalgias, marked peripheral eosinophilia and pulmonary infiltrates" ([Orphanet ORPHA:227972](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=227972))
- **MeSH:** "Toxic Oil Syndrome" (D019867)
- **ICD-10/ICD-11:** No dedicated code identified in searched sources; historically coded under toxic-effect/adverse-event categories (e.g., ICD-9-CM 989.89-adjacent "toxic effect of other substances") rather than a named entity. Confirm exact ICD-10-CM/ICD-11 mapping via direct database lookup before curation.
- **OMIM:** Not a Mendelian disorder; no OMIM phenotype number.

**Synonyms:** Spanish toxic oil syndrome; Spanish toxic-oil syndrome; toxic-allergic syndrome caused by ingestion of rapeseed oil denatured with aniline; "colza oil syndrome"; "lo de la colza."

## 2. Etiology

**Primary causal factor — environmental/toxicologic, not genetic or infectious.** The causal agent is the ingestion of illegally re-refined rapeseed oil that had been industrially denatured with aniline. The syndrome does **not** resemble classic aniline or acetanilide intoxication; instead it has been provisionally, and then more specifically, attributed to reaction products formed between aniline/acetanilide and the oil's fatty-acid components — termed collectively "oleoanilides" ([PubMed 6116011](https://pubmed.ncbi.nlm.nih.gov/6116011/?dopt=Abstract)). Subsequent case-control chemical epidemiology strongly implicated a specific chemical class: **fatty-acid esters of 3-(N-phenylamino)-1,2-propanediol (PAP)**, byproducts of the aniline-oil reaction, as the most probable etiologic agents ([PubMed 10069247](https://pubmed.ncbi.nlm.nih.gov/10069247/); [PubMed 7918809](https://pubmed.ncbi.nlm.nih.gov/7918809/)).

**Risk factors:**
- *Environmental/exposure*: purchase of oil from itinerant door-to-door salesmen rather than licensed retail outlets was the dominant exposure risk — in one household study in the Orcasur district of Madrid, all affected households had purchased oil from traveling salesmen, versus only 34% of unaffected households ([Grokipedia summary](https://grokipedia.com/page/Toxic_oil_syndrome); ["Lo de la colza" — Nursing Clio](https://nursingclio.org/2025/07/31/lo-de-la-colza-mass-poisoning-state-neglect-and-corruption-after-the-spanish-transition/)).
- *Geographic*: concentrated in Madrid province (~71% of the ~14,292–19,828 reported cases) and 13 other central/northwestern Spanish provinces; incidence exceeded 300 cases/100,000 in Segovia and Palencia ([NEJM 1983](https://www.nejm.org/doi/full/10.1056/NEJM198312083092302)).
- *Sex/age*: of the long-term surveillance cohort of 20,084 subjects, 60.6% were women and 39.4% men; TOS was the leading cause of death among subjects under 40 years of age, with the shortest post-onset survival among women and younger patients ([ScienceDirect S0895435603001197](https://www.sciencedirect.com/science/article/abs/pii/S0895435603001197)).
- *Genetic susceptibility (host modifier, not causal)*: HLA class I/II alleles modulate severity and chronicity (see Section 4/9).
- *Storage/dose-persistence*: "late cases" of TOS occurred among people who consumed oil that had been stored for up to a year, indicating the etiologic agent(s) persisted in stored oil over time ([ScienceDirect 0278691589900471](https://www.sciencedirect.com/science/article/abs/pii/0278691589900471)).

**Protective factors:** No genetic or dietary protective factor has been robustly established; certain HLA haplotypes were associated with lower likelihood of chronic/severe disease relative to DR2/DR4-DQ8/A24 carriers (see below), which functions as a relative rather than absolute protective association.

**Gene–environment interaction:** This is the central etiologic feature of TOS beyond the initial toxic exposure — identical oil exposure produced markedly different clinical trajectories (self-limited acute illness vs. progression to chronic scleroderma-like disease vs. death) that correlate with host HLA genotype, indicating a gene–environment interaction in which a xenobiotic (oleoanilide/PAP-ester) triggers an aberrant, HLA-restricted immune response in susceptible individuals ([ScienceDirect S0378427405003103](https://www.sciencedirect.com/science/article/abs/pii/S0378427405003103); [PubMed 15979827](https://pubmed.ncbi.nlm.nih.gov/15979827/)).

## 3. Phenotypes

Phenotypes are drawn from Spanish Clinical Commission (Ministry of Health, August 1981) case criteria and subsequent cohort/case-series literature. Frequencies below are qualitative characterizations from the literature; a curated entry should mine the NEJM 1983 clinical-epidemiology paper and the 14-case immunopathologic series for precise percentages.

| Phenotype | Type | Phase | Suggested HP term |
|---|---|---|---|
| Fever | Sign | Acute | HP:0001945 Fever |
| Cough / dyspnea | Symptom | Acute | HP:0002090 Bronchitis; HP:0002094 Dyspnea |
| Pulmonary infiltrates (interstitial/alveolar) | Radiographic sign | Acute | HP:0002088 Abnormal pulmonary interstitial morphology |
| Pleural effusion | Sign | Acute | HP:0002202 Pleural effusion |
| Peripheral (blood) eosinophilia | Lab abnormality | Acute–chronic | HP:0001880 Eosinophilia |
| Myalgia (often severe/incapacitating) | Symptom | Acute–chronic | HP:0003326 Myalgia |
| Skin rash | Sign | Acute | HP:0000988 Skin rash |
| Hepatosplenomegaly | Sign | Acute | HP:0001433 Hepatosplenomegaly |
| Generalized lymphadenopathy | Sign | Acute | HP:0002716 Lymphadenopathy |
| Peripheral edema | Sign | Intermediate | HP:0000969 Edema |
| Skin induration / scleroderma-like sclerosis | Sign | Chronic | HP:0100678 Skin plaque; HP:0100692 Skin nodule (or free text — no exact HP scleroderma-secondary term) |
| Hepatic dysfunction / liver disease | Lab/clinical | Intermediate–chronic | HP:0001392 Abnormality of the liver |
| Pulmonary arterial hypertension | Sign | Intermediate–chronic | HP:0002092 Pulmonary hypertension |
| Sicca syndrome (dry eyes/mouth) | Symptom | Chronic | HP:0031000 Dry eye; HP:0031416 Dry mouth |
| Peripheral (sensorimotor) neuropathy | Sign | Chronic | HP:0009830 Peripheral neuropathy |
| Joint contractures | Sign | Chronic | HP:0034680 / HP:0001371 Flexion contracture |
| Raynaud phenomenon | Symptom | Chronic | HP:0025595 Raynaud phenomenon |
| Livedo reticularis | Sign | Chronic | HP:0100672 Livedo reticularis |
| Carpal tunnel syndrome | Sign | Chronic | HP:0100628 Carpal tunnel syndrome |
| Dysphagia | Symptom | Chronic | HP:0002015 Dysphagia |
| Alopecia | Sign | Chronic | HP:0001596 Alopecia |
| Cachexia / weight loss | Sign | Intermediate–chronic | HP:0004325 Decreased body weight |
| Fatigue | Symptom | Chronic (persistent) | HP:0012378 Fatigue |
| Cognitive difficulties (frontal-subcortical) | Symptom | Chronic (decades later) | HP:0100543 Cognitive impairment |
| Psychiatric complaints | Symptom | Chronic | (context-dependent; no single HP term) |

**Characteristics:**
- *Onset*: adult-onset, epidemic point-source exposure (interval between ingestion of contaminated oil and symptom onset of 4–10 days) ([ScienceDirect/CHEST summary](https://journal.chestnet.org/article/S0012-3692(16)49122-1/fulltext)).
- *Severity/frequency*: roughly half of the ~20,000 affected individuals recovered from the acute phase without apparent sequelae; the remainder progressed to intermediate and/or chronic disease with severe myalgia, eosinophilia, peripheral nerve damage, sclerodermiform skin lesions, sicca syndrome, alopecia, and joint contractures ([ScienceDirect overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/toxic-oil-syndrome)).
- *Progression*: staged and largely unidirectional (acute → intermediate → chronic), though partial recovery has been documented in chronic-phase patients beyond 2 years post-onset.
- *Quality of life (long-term)*: a 2022 SF-36 health-related quality-of-life study in survivors documented persistently reduced physical and mental health domain scores relative to the general population decades after exposure ([IJE 2022](https://academic.oup.com/ije/article/51/2/491/6301183)). Among 91 individuals re-evaluated more than a decade after exposure, over half reported persistent fatigue, muscle cramps, arthralgias, subjective cognitive difficulties, and psychiatric complaints.

## 4. Genetic/Molecular Information

TOS has **no causal single-gene etiology** — it is a toxin-triggered disease — but host genetics substantially modifies severity and chronicity via HLA:

- **HLA-DR2**: phenotypic frequency was markedly increased in patients who died of TOS (73.5%) compared with TOS-affected survivors (25.6%), unaffected family members (28.5%), unrelated controls (23.9%), and controls who died of other causes (38.4%) — i.e., DR2 tracks with fatal/severe disease ([PubMed 10746782](https://pubmed.ncbi.nlm.nih.gov/10746782/)).
- **HLA-DR4-DQ8** and **HLA-A24**: independently associated with susceptibility to chronic TOS; HLA-B blank (homozygosity/no detected B antigen) frequency was decreased in chronic TOS ([PubMed 8803534](https://pubmed.ncbi.nlm.nih.gov/8803534/)).
- **DQα-chain arginine-52**: an amino-acid polymorphism in the DQ α-chain (Arg52) was independently associated with TOS susceptibility, analogous to a mechanism described in other HLA-linked autoimmune/toxin-triggered diseases ([ScienceDirect S0378427405003103](https://www.sciencedirect.com/science/article/abs/pii/S0378427405003103)).
- **HLA-transgenic mouse functional validation**: HLA-DR2/DQ6 transgenic mice exposed to TOS-implicated oils showed higher eosinophil percentages (DQ6-linked) and IgE levels (DR2-linked) than DR3- or DR4-transgenic mice, supporting a genetically restricted immunomodulatory mechanism ([PubMed 15979827](https://pubmed.ncbi.nlm.nih.gov/15979827/)).

**Molecular etiologic agent(s)/chemical entities (CHEBI candidates for curation):**
- **Oleoanilides** — the general class of fatty-acid–acetanilide reaction products originally implicated.
- **3-(N-phenylamino)-1,2-propanediol (PAP)** and its **fatty-acid esters** (mono- and di-oleoyl esters, linoleic diester) — the leading specific etiologic candidates, epidemiologically linked to TOS-implicated oils ([PubMed 10069247](https://pubmed.ncbi.nlm.nih.gov/10069247/); [Lipids journal](https://link.springer.com/article/10.1007/s11745-001-0823-4)).
- **3-(Phenylamino)alanine (PAA)** — a biotransformation product of PAP (demonstrated in rat hepatocytes and human liver tissue), mechanistically linking TOS to the chemically distinct but clinically overlapping 1989 U.S. **eosinophilia-myalgia syndrome (EMS)**, in which PAA was found as a contaminant of implicated L-tryptophan lots ([PubMed 8555405](https://pubmed.ncbi.nlm.nih.gov/8555405/); [Mayo Clin Proc](https://www.mayoclinicproceedings.org/article/S0025-6196(12)60172-4/fulltext)).
- Incubation of PAP with human liver microsomes generates a **reactive quinoneimine intermediate**, implicating a reactive-metabolite bioactivation mechanism ([search summary, per Chem Res Toxicol 8(7):911](https://pubs.acs.org/crtoec/article-abstract/8/7/911/1243235/)).
- Structural analogy between PAP-diesters and **platelet-activating factor (PAF)** has been proposed as contributing to the eosinophilic/inflammatory response ([Toxicology, S0378427496038623](https://www.sciencedirect.com/science/article/abs/pii/S0378427496038623)).

There is no described pathogenic germline variant, no described epigenetic signature specific to TOS, and no chromosomal abnormality associated with the disease — all molecular data concern the exogenous toxin and its host-immune interaction rather than a heritable lesion.

## 5. Environmental Information

- **Primary environmental factor**: consumption of illegally distributed, industrially aniline-denatured (2%) rapeseed oil that was re-refined by unlicensed processors to remove color/odor and then fraudulently sold as edible/olive oil ([PubMed 6116011](https://pubmed.ncbi.nlm.nih.gov/6116011/?dopt=Abstract)). This is a discrete, non-recurring environmental/regulatory-failure exposure rather than an ongoing occupational or ambient toxin.
- **Persistence**: the causal toxin(s) persisted in stored oil for up to a year, generating "late cases" after the initial 1981 outbreak ([ScienceDirect 0278691589900471](https://www.sciencedirect.com/science/article/abs/pii/0278691589900471)).
- **Lifestyle factor**: reliance on door-to-door itinerant oil vendors (a socioeconomic/behavioral exposure route) rather than licensed retail supply chains was the operative lifestyle/consumer-behavior risk factor.
- **Infectious agents**: none — TOS is not infectious and has no described microbial trigger or co-factor.

## 6. Mechanism / Pathophysiology

**Ordered causal chain (as currently understood; several links are inferred rather than fully demonstrated):**

1. Ingestion of illegally re-refined rapeseed oil **denatured with aniline** *leads to* systemic exposure to reaction byproducts formed between aniline/acetanilide and oil fatty-acid components ("oleoanilides"), most specifically fatty-acid esters of **3-(N-phenylamino)-1,2-propanediol (PAP)** — *inferred from epidemiologic case-control chemistry, not directly demonstrated in exposed humans at the time of the epidemic* ([PubMed 10069247](https://pubmed.ncbi.nlm.nih.gov/10069247/)).
2. Hepatic/microsomal metabolism of PAP *results in* bioactivation to a reactive **quinoneimine intermediate** and to the metabolite **3-(phenylamino)alanine (PAA)** — *demonstrated in vitro in rat hepatocytes and human liver tissue* ([PubMed 8555405](https://pubmed.ncbi.nlm.nih.gov/8555405/)).
3. PAP/PAA and their esters *trigger* activation of circulating polymorphonuclear leukocytes, including generation of **reactive oxygen metabolites** in human PMNs — *demonstrated in vitro* ([ScienceDirect S0378427496038623](https://www.sciencedirect.com/science/article/abs/pii/S0378427496038623)) — and structurally resemble **platelet-activating factor (PAF)**, which *may contribute to* eosinophil recruitment and vascular permeability changes — *inferred from structural analogy*.
4. In genetically susceptible individuals (particularly those carrying **HLA-DR2**, **HLA-DR4-DQ8**, or **HLA-A24**, or the **DQα-Arg52** polymorphism), this toxic exposure *drives* an aberrant, HLA-restricted adaptive immune response with a **Th2-skewed cytokine profile** (elevated IL-4, IL-5 relative to IFN-γ in affected lung tissue) — *demonstrated by cytokine mRNA expression analysis of TOS lung biopsies* ([PubMed 9074654](https://pubmed.ncbi.nlm.nih.gov/9074654/)).
5. The Th2-skewed response *leads to* marked **peripheral and tissue eosinophilia**, elevated IgE, and **T-cell activation** — *demonstrated in patient and transgenic-mouse studies* ([PubMed 15979827](https://pubmed.ncbi.nlm.nih.gov/15979827/)).
6. Concurrently, the toxin(s) *cause* direct or immune-mediated **endothelial injury** in both small and large vessels across multiple organs, with pronounced **intimal proliferation** (edematous, with vacuolated cells in the media and loss of vascular smooth muscle in elastic pulmonary arteries) and **medial hypertrophy** with intimal proliferation in muscular pulmonary arteries, in one reported case severe enough to **completely occlude the arterial lumen** — *demonstrated histopathologically* ([PMC459646](https://pmc.ncbi.nlm.nih.gov/articles/PMC459646/); [Virchows Arch, pathology of new toxic syndrome](https://link.springer.com/article/10.1007/BF00496569)).
7. Pulmonary vascular endothelial injury and remodeling *result in* **pulmonary arterial hypertension**, a major driver of intermediate- and chronic-phase morbidity and mortality — *demonstrated clinically and by autopsy series*.
8. Perivascular and interstitial inflammatory infiltration and eosinophil-derived mediators *drive* release of **fibrogenic growth factors**, notably **TGF-β** and **PDGF-AA**, which *lead to* progressive tissue fibrosis — *demonstrated in comparative EMS/TOS tissue studies* ([PubMed 8285738](https://pubmed.ncbi.nlm.nih.gov/8285738/)).
9. Dermal and fascial fibrosis *manifests as* **scleroderma-like skin sclerosis**, joint contractures, and sicca syndrome in the chronic phase, overlapping clinically and histologically with idiopathic systemic sclerosis and related connective-tissue diseases — *demonstrated clinically* ([PubMed 3961509](https://pubmed.ncbi.nlm.nih.gov/3961509/)).
10. Concurrent nerve involvement (mechanism less well defined — possibly ischemic/microvascular and/or direct toxic/immune injury to peripheral nerve) *leads to* chronic **peripheral (sensorimotor) neuropathy** — *largely inferred from clinical/electrophysiologic observation rather than a fully worked-out cellular mechanism*.
11. In a minority of long-term survivors, ongoing frontal-subcortical circuit dysfunction is detectable by eye-tracking and cognitive testing **four decades** after exposure, but blood biomarkers (NfL, GFAP, pTau217) do **not** show the elevation pattern typical of progressive neurodegenerative disease — suggesting a **static or slowly evolving immune/vascular injury pattern rather than ongoing neurodegeneration** — *demonstrated in 2025 case-control biomarker and eye-tracking studies* ([PMC12155236](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155236/); [Frontiers 2025](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1666809/full); [PMC12155933](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155933/)).

**Cell types/processes for ontology binding (suggested):**
- **GO** biological processes: GO:0006954 inflammatory response; GO:0043304 regulation of mast cell degranulation (context-dependent); GO:0030101 natural killer cell activation (if relevant); GO:0030099 myeloid cell differentiation (eosinophilopoiesis); GO:0001525 angiogenesis / vascular remodeling; GO:0030198 extracellular matrix organization (fibrosis); response to xenobiotic stimulus GO:0009410.
- **CL** cell types: CL:0000771 eosinophil; CL:0000542 lymphocyte / CL:0000909 CD4-positive, alpha-beta T cell (Th2 subset CL:0000546); CL:0000115 endothelial cell; CL:0000499 stromal cell / CL:0002548 fibroblast of connective tissue (fibrosis); CL:0002139 endothelial cell of vascular tree.
- **UBERON**: UBERON:0002048 lung; UBERON:0001981 blood vessel; UBERON:0002037 cerebellum (n/a) — more relevantly UBERON:0002370 thymus is not central; primary organs: UBERON:0002048 lung, UBERON:0002107 liver, UBERON:0000178 skin (integument), UBERON:0001021 nerve, UBERON:0001981 blood vessel, UBERON:0000948 heart (secondary, cor pulmonale from PAH).
- **CHEBI**: candidate entries for "3-(phenylamino)-1,2-propanediol", "3-phenylaminoalanine", "acetanilide", "aniline" — verify exact CHEBI CURIEs via OAK/ChEBI lookup before binding (not independently confirmed in this research pass).

## 7. Anatomical Structures Affected

- **Primary organs**: lungs (pneumonitis, pulmonary vascular disease, pulmonary hypertension); skin/subcutaneous tissue and fascia (edema → induration → scleroderma-like sclerosis); peripheral nervous system (sensorimotor neuropathy).
- **Secondary/systemic involvement**: liver (hepatic dysfunction, hepatosplenomegaly, elevated relative risk of liver disease — RR 3.83 in long-term follow-up, [ScienceDirect S0895435603001197](https://www.sciencedirect.com/science/article/abs/pii/S0895435603001197)); joints (contractures); exocrine glands (sicca/Sjögren-like syndrome); vasculature systemically (large- and small-vessel involvement, "generalized vascular lesions affecting all organs and vessels" per Orphanet); reticuloendothelial system (lymphadenopathy, splenomegaly); central/peripheral nervous system in the long-term (frontal-subcortical cognitive dysfunction).
- **Body systems**: respiratory, cardiovascular (pulmonary hypertension, thromboembolism of great arteries), integumentary, musculoskeletal, hepatic, immune, peripheral/central nervous system.
- **Tissue/cell level**: vascular endothelium and media (elastic and muscular pulmonary arteries), dermal fibroblasts/fascia, hepatocytes (site of PAP bioactivation), circulating eosinophils and T lymphocytes.
- **Subcellular**: hepatic microsomal/cytochrome P450-associated bioactivation of PAP to reactive quinoneimine (endoplasmic reticulum, GO Cellular Component: GO:0005783).
- **Laterality**: bilateral/systemic — not a lateralized disease.

## 8. Temporal Development

- **Onset**: adult-onset, epidemic exposure; symptom onset 4–10 days after ingestion of contaminated oil ([CHEST summary](https://journal.chestnet.org/article/S0012-3692(16)49122-1/fulltext)).
- **Pattern**: acute onset of respiratory/systemic illness, evolving in a subset of patients through a staged, largely progressive course.
- **Stages** (well defined in this literature, unusually so for an environmental disease):
  - *Acute* (~first 2 months): pulmonary edema/infiltrates, fever, rash, eosinophilia, myalgia.
  - *Intermediate* (approximately months 2–4): peripheral edema, dermal induration, hepatic dysfunction, pulmonary hypertension, sicca syndrome, hypertriglyceridemia, cachexia — reached by roughly 60% of all TOS patients.
  - *Chronic* (beyond month 4, with partial recovery possible after ~2 years in some patients): scleroderma-like cutaneous sclerosis, peripheral neuropathy, joint contractures, Raynaud phenomenon, sicca/Sjögren syndrome, carpal tunnel syndrome, dysphagia, persistent pulmonary hypertension.
- **Progression rate**: variable — roughly half of patients recovered from the acute phase without sequelae; the remainder progressed, and progression through intermediate to chronic phase correlates with HLA genotype and disease severity markers.
- **Duration**: for those developing chronic disease, TOS is a lifelong condition — persistent fatigue, myalgia, arthralgia, cognitive complaints, and psychiatric symptoms are documented in survivors assessed more than four decades after the 1981 exposure ([PMC12484009](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484009/); [PMC12155933](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155933/)).
- **Critical period**: the initial acute/subacute phase (first weeks to ~4 months) appears to be the critical window in which the eventual severity/chronicity trajectory is largely determined, correlating with HLA genotype.

## 9. Inheritance and Population

- **Epidemiology**: ~19,828–20,084 cases reported in Spain in 1981–1982 (estimates vary slightly by source/cohort-closure date), concentrated in Madrid province (71% of cases) and 13 other central/northwestern provinces, with incidence exceeding 300/100,000 in Segovia and Palencia ([NEJM 1983](https://www.nejm.org/doi/full/10.1056/NEJM198312083092302)). This is a historical point-source epidemic with **zero ongoing incidence** since the causal oil was withdrawn from sale in 1981 — it is not an endemic or recurring disease.
- **Mortality**: 315 deaths reported by June 1982 in early surveillance; longer surveillance to 1995 of the full 20,084-subject cohort recorded 1,799 total deaths, of which 356 were TOS-related (overall epidemic mortality historically cited around 8.4%, with figures up to 839 deaths cited in some secondary EMS-comparison sources — cohort definitions and follow-up windows differ across sources and should be reconciled against the primary registry paper before final figures are curated) ([ScienceDirect S0895435603001197](https://www.sciencedirect.com/science/article/abs/pii/S0895435603001197); [PubMed 8412642](https://pubmed.ncbi.nlm.nih.gov/8412642/)).
- **Inheritance pattern**: not a Mendelian/heritable disease — inheritance pattern is **not applicable**; susceptibility is modulated by HLA genotype (a polygenic host-modifier effect on a toxin-induced disease), not by a single causal locus.
- **Sex ratio**: cohort was 60.6% female / 39.4% male; TOS-related deaths occurred with shortest survival times in women and in those under 40.
- **Age distribution**: all ages affected; TOS was the **leading cause of death** in the affected cohort among those under age 40.
- **Geographic distribution**: strictly confined to the distribution network of the adulterated oil within Spain — no cases outside Spain, and no cases since the source oil was withdrawn, making TOS a geographically and temporally bounded historical epidemic.
- **Genetic population considerations**: no founder effect, consanguinity role, or carrier-frequency concept applies (non-heritable disease); HLA allele frequencies (DR2, DR4-DQ8, A24) in the Spanish population are the relevant "population genetics" consideration, functioning purely as severity/susceptibility modifiers of an exogenous exposure.

## 10. Diagnostics

- **Clinical case definition**: formal diagnostic criteria were established by the **Spanish Clinical Commission** (Ministry of Health and Consumer Affairs) in August 1981, combining epidemiologic exposure history (consumption of oil from the implicated distribution channels) with the characteristic clinical/laboratory triad of respiratory symptoms, marked peripheral eosinophilia, and myalgia, in the appropriate geographic/temporal context ([CHEST summary](https://journal.chestnet.org/article/S0012-3692(16)49122-1/fulltext)).
- **Laboratory tests**: peripheral blood eosinophil count (hallmark finding); liver function tests (elevated in intermediate/chronic phase); IgE levels (elevated in genetically susceptible subgroups); triglycerides (elevated, intermediate phase).
- **Imaging**: chest radiography demonstrating interstitial or alveolar infiltrates with or without pleural effusion in the acute phase; later imaging for pulmonary hypertension assessment (echocardiography historically, right heart catheterization for confirmation).
- **Functional tests**: pulmonary function testing (restrictive pattern in advanced pulmonary fibrosis/hypertension); right-heart catheterization for pulmonary hypertension confirmation.
- **Biopsy/histopathology**: skin biopsy showing scleroderma-like dermal/fascial fibrosis in chronic phase; lung/vascular histopathology (in fatal cases) showing the characteristic intimal proliferation and medial hypertrophy of pulmonary arteries described above ([PMC459646](https://pmc.ncbi.nlm.nih.gov/articles/PMC459646/)).
- **Genetic testing**: not diagnostic for TOS itself, but **HLA typing** (DR2, DR4-DQ8, A24) has been used in research settings as a severity/prognostic biomarker rather than a diagnostic test.
- **Emerging/research biomarkers**: recent (2025) blood biomarker panels for neurodegeneration — neurofilament light chain (NfL), glial fibrillary acidic protein (GFAP), phosphorylated tau 217 (pTau217) — have been used in long-term survivor case-control research to characterize the chronic neurocognitive phenotype, showing no elevation pattern typical of progressive neurodegenerative disease ([PMC12155236](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155236/)); eye-tracking has been used as an objective research measure of frontal-subcortical dysfunction ([Frontiers 2025](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1666809/full)).
- **Differential diagnosis**: idiopathic eosinophilia-myalgia syndrome (chemically/clinically overlapping, distinguished by L-tryptophan exposure history rather than oil exposure); idiopathic systemic sclerosis/scleroderma; hypereosinophilic syndrome; eosinophilic pneumonia of other causes; other causes of pulmonary arterial hypertension.
- **Screening**: not applicable — there is no ongoing population at risk; the relevant "screening" activity was 1981-era regulatory/epidemiologic case-finding, not a recurring clinical screening program.

## 11. Outcome/Prognosis

- **Mortality**: acute-phase deaths were predominantly due to **respiratory failure from noncardiogenic pulmonary edema**; intermediate-phase deaths were dominated by **thromboembolism of the great arteries and pulmonary hypertension**; chronic-phase deaths were predominantly due to **restrictive respiratory failure secondary to severe neurologic infection and pulmonary hypertension** ([ScienceDirect S0895435603001197](https://www.sciencedirect.com/science/article/abs/pii/S0895435603001197)).
- **Long-term relative risks** (vs. general/unaffected comparison, from cohort follow-up): liver disease RR 3.83; pulmonary hypertension RR 3.19; motor neuropathy RR 2.24; pulmonary infection RR 1.54; eosinophilia RR 1.14.
- **Recovery**: approximately half of all affected individuals recovered from the acute phase without apparent long-term sequelae. Among those progressing to intermediate/chronic disease, partial recovery of skin sclerosis has been documented beyond 2 years post-onset in some patients, but many carry persistent morbidity for life.
- **Quality of life**: SF-36-based assessment in 2022 documented persistently reduced physical and mental health-related quality of life in survivors relative to the general Spanish population, decades after exposure ([IJE 2022](https://academic.oup.com/ije/article/51/2/491/6301183)).
- **Prognostic factors**: HLA genotype (DR2 with fatal disease; DR4-DQ8/A24 with chronicity), phase reached (acute-only vs. progression to intermediate/chronic), sex (female) and younger age (<40) associated with shorter survival among those who die of TOS-related causes.
- **Neurocognitive prognosis**: four decades post-exposure, survivors show measurable frontal-subcortical cognitive dysfunction by objective eye-tracking testing, but blood neurodegeneration biomarkers argue against an ongoing progressive neurodegenerative process, suggesting a largely static injury pattern from the original toxic/immune insult rather than a worsening trajectory ([PMC12484009](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484009/); [PMC12155236](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155236/)).

## 12. Treatment

**No specific antidote exists.** Management is supportive/symptomatic and multidisciplinary. Multiple immunomodulatory and antifibrotic agents were trialed without convincing benefit:

- **Corticosteroids** (NCIT:C2942 / treatment_term NCIT:C15986 Pharmacotherapy) — used, particularly in acute/subacute phases, to control inflammation and eosinophilia; benefit was inconsistent and not clearly disease-modifying for chronic sequelae.
- **Azathioprine**, **penicillamine** — immunomodulatory/antifibrotic agents trialed for chronic sclerodermiform disease; no convincing therapeutic effect demonstrated.
- **Plasmapheresis** — trialed; no convincing effect.
- **Vitamin E, superoxide dismutase** — antioxidant approaches trialed given the oxidative/PMN-activation component of pathogenesis; no convincing effect.
- **Vasodilators** — used symptomatically, presumably for pulmonary hypertension and Raynaud phenomenon management (NCIT term candidates: NCIT:C29688-type vasodilator class terms — verify exact CURIE).
- **Supportive care** (NCIT:C15747 Supportive Care) — mainstay of management: respiratory support in acute pulmonary edema, nutritional support for cachexia, management of secondary infection.
- **Rehabilitation** (NCIT:C15315 Rehabilitation) / **Physical therapy** (NCIT:C15302) — for joint contractures and neuropathy-related disability.
- **Genetic counseling** — not applicable (non-heritable disease).
- **Experimental/advanced therapeutics** — no gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy has been developed or trialed specifically for TOS; this reflects both its status as a closed historical epidemic and the era (early 1980s) in which acute management decisions were made.
- **Treatment outcomes summary**: per the WHO 1991 meeting report and subsequent reviews, none of the pharmacologic interventions trialed (corticosteroids, azathioprine, penicillamine, plasmapheresis, vitamin E, superoxide dismutase, vasodilators, anti-inflammatories) produced a convincing therapeutic effect on the underlying disease course ([ScienceDirect S0049017205800174](https://www.sciencedirect.com/science/article/abs/pii/S0049017205800174); [syndrome.co.uk summary](https://syndrome.co.uk/toxic-oil-syndrome)).
- **Clinical trials**: no NCT-registered interventional trials specific to TOS were identified (consistent with its status as a closed 1981 epidemic predating ClinicalTrials.gov and lacking an ongoing at-risk population).

## 13. Prevention

- **Primary prevention**: entirely regulatory/public-health — withdrawal of the adulterated oil from sale in 1981, and subsequent Spanish and EU regulatory tightening of edible-oil labeling, distribution licensing, and denaturant-tracking requirements to prevent industrial (non-food) oils from re-entering the food supply chain. There is no vaccine, chemoprophylaxis, or individual behavioral intervention relevant to this disease beyond avoiding the (now nonexistent) contaminated product.
- **Secondary prevention**: 1981-era case-finding and epidemiologic surveillance (the Spanish Clinical Commission registry) to identify and treat affected individuals early in the acute phase, when corticosteroid/supportive intervention may reduce acute morbidity.
- **Tertiary prevention**: multidisciplinary chronic-disease management (rehabilitation, symptomatic treatment of pulmonary hypertension, neuropathy, and sicca syndrome) to limit disability in those who progressed to chronic disease.
- **Genetic counseling / screening**: not applicable (non-heritable).
- **Public health**: the TOS epidemic directly motivated strengthened food-safety and adulteration-control legislation in Spain and contributed to broader European food-safety regulatory reform; it remains a canonical case study in toxicology and public-health/regulatory-failure literature (see the 2025 historical/political analysis, ["Lo de la colza"](https://nursingclio.org/2025/07/31/lo-de-la-colza-mass-poisoning-state-neglect-and-corruption-after-the-spanish-transition/)).
- **Environmental intervention**: control of industrial denaturant (aniline) use and tracking, and enforcement against unlicensed oil re-refining/distribution — the specific regulatory intervention that ended the epidemic.

## 14. Other Species / Natural Disease

- **Taxonomy**: TOS as a clinical entity is described only in humans (*Homo sapiens*, NCBITaxon:9606); it is not a naturally occurring veterinary disease.
- **Breed**: not applicable.
- **Natural disease in other species**: none reported — TOS is not a spontaneously occurring animal disease; all animal data derive from deliberate experimental exposure (see Section 15).
- **Comparative biology**: the closest naturally/epidemically occurring comparator in another population is the U.S. **eosinophilia-myalgia syndrome (EMS)** of 1989, caused by contaminated L-tryptophan supplements, which shares clinical (eosinophilia, myalgia, fasciitis/fibrosis, in some cases scleroderma-like skin change) and chemical (shared PAA metabolite) features with TOS, suggesting partially convergent or shared pathogenic mechanisms across two independent toxin exposures ([Mayo Clin Proc](https://www.mayoclinicproceedings.org/article/S0025-6196(12)60172-4/fulltext); [NEJM 1990](https://www.nejm.org/doi/full/10.1056/NEJM199008093230601)).
- **Zoonotic potential**: not applicable — TOS is a toxin-induced disease, not a transmissible one.

## 15. Model Organisms

- **HLA-transgenic mice**: mice expressing human HLA-DR2/DQ6, DR3, or DR4 haplotypes were exposed to TOS-implicated oils/oil components. DR2/DQ6-expressing mice showed higher eosinophilia and IgE than DR3/DR4-expressing mice, functionally validating the human HLA-association data and modeling genetic restriction of the immunomodulatory response ([PubMed 15979827](https://pubmed.ncbi.nlm.nih.gov/15979827/)).
- **Mouse toxicologic models of PAP/fatty-acid anilides**: administration of fatty acid anilides and the linoleic diester of PAP to mice produced weight loss, pulmonary hemorrhage/congestion/emphysema, and increased blood eosinophilia, supporting these compounds as candidate etiologic agents and providing an acute toxicologic model of the pulmonary/hematologic phenotype ([Arch Toxicol, S002040050641](https://link.springer.com/article/10.1007/s002040050641); [PubMed 7779449](https://pubmed.ncbi.nlm.nih.gov/7779449/); [PubMed 10650923](https://pubmed.ncbi.nlm.nih.gov/10650923/)).
- **Rodent (non-HLA) "search for an animal model"**: a dedicated study explicitly titled "A search for an animal model of the Spanish toxic oil syndrome" concluded that no conventional rodent model fully recapitulates the human multisystem chronic phenotype, particularly the scleroderma-like fibrotic and neuropathic components ([ScienceDirect S027869150200114X](https://www.sciencedirect.com/science/article/abs/pii/S027869150200114X)).
- **Lewis rat EMS model (cross-referenced comparator)**: female Lewis rats given L-tryptophan implicated in human EMS developed fasciitis and perimyositis resembling human EMS pathology; while not a TOS model per se, this is the most relevant fibrotic-phenotype rodent model in the literature comparator disease and is cited as a partial model for the shared PAA-associated fibrotic mechanism ([PubMed 2243145](https://pubmed.ncbi.nlm.nih.gov/2243145/); [JCI 114902](https://www.jci.org/articles/view/114902)).
- **In vitro human systems**: human polymorphonuclear leukocyte cultures exposed to PAP and its mono-/di-oleyl esters, used to model reactive-oxygen-metabolite generation ([ScienceDirect S0378427496038623](https://www.sciencedirect.com/science/article/abs/pii/S0378427496038623)); human liver microsome/hepatocyte incubations used to model PAP bioactivation to reactive quinoneimine and to PAA ([PubMed 8555405](https://pubmed.ncbi.nlm.nih.gov/8555405/)).
- **Model limitations**: no existing model — mouse or rat — reproduces the full chronic human phenotype (progressive scleroderma-like skin sclerosis, peripheral neuropathy, pulmonary arterial hypertension, and decades-long cognitive dysfunction). HLA-transgenic mice model the genetic-restriction/Th2-skewing immune mechanism; toxicologic mouse models capture acute pulmonary/hematologic effects of specific candidate compounds; neither models chronic fibrotic/vascular remodeling or the neurologic phenotype.
- **Applications**: the HLA-transgenic mouse model is useful for studying gene–environment interaction and immune mechanism; the acute mouse toxicology models are useful for compound-identification/structure-activity work distinguishing candidate etiologic agents; no model exists for late-stage drug development, since TOS is a closed epidemic with no active patient-recruitment or therapeutic pipeline.

---

## Summary of Key Ontology/Identifier Candidates for Curation

| Category | Suggested term (verify CURIE before binding) |
|---|---|
| Disease | MONDO:0016421 (Toxic oil syndrome); ORPHA:227972 |
| Genes/host modifiers | HLA-DRB1 (DR2, DR4 alleles), HLA-DQB1 (DQ8), HLA-A (A24) — HGNC IDs for HLA loci should be resolved via HGNC before binding `genetic:` blocks |
| Chemical entities | 3-(N-phenylamino)-1,2-propanediol (PAP); 3-(phenylamino)alanine (PAA); aniline; acetanilide; oleoanilide — resolve CHEBI CURIEs |
| Phenotypes | See Section 3 table (HP terms) |
| Cell types | CL:0000771 eosinophil; CL:0000115 endothelial cell; CL:0002548 fibroblast |
| Biological processes | GO:0006954 inflammatory response; GO:0030198 extracellular matrix organization; angiogenesis/vascular remodeling GO terms |
| Anatomy | UBERON:0002048 lung; UBERON:0000178 skin epidermis/integument; UBERON:0001021 nerve; UBERON:0002107 liver; UBERON:0001981 blood vessel |
| Treatment | NCIT:C15986 Pharmacotherapy (corticosteroids); NCIT:C15747 Supportive Care; NCIT:C15315 Rehabilitation; NCIT:C15302 Physical Therapy |

**Note on evidence base:** Nearly all primary literature on TOS dates from 1981–2005, reflecting its nature as a closed historical epidemic; a smaller but active cluster of 2022–2025 publications addresses long-term (four-decade) survivor outcomes (quality of life, cognition, neurodegeneration biomarkers). For dismech curation, prioritize: the 1983 NEJM clinical-epidemiology paper, the 2003 survival cohort paper, the PAP/PAA mechanistic series (1994–2001), the HLA association papers (1996–2005), and the 2025 long-term biomarker/cognitive papers — each should be fetched and quote-verified per standard evidence-curation practice before use.

**Sources:**
- [Toxic-allergic syndrome caused by ingestion of rapeseed oil denatured with aniline (PMID:6116011)](https://pubmed.ncbi.nlm.nih.gov/6116011/?dopt=Abstract)
- [Clinical epidemiology of toxic-oil syndrome (PMID:6633617)](https://pubmed.ncbi.nlm.nih.gov/6633617/)
- [Factors associated with pathogenicity of oils related to TOS (PMID:7918809)](https://pubmed.ncbi.nlm.nih.gov/7918809/)
- [Epidemiologic evidence for a new class of compounds associated with TOS (PMID:10069247)](https://pubmed.ncbi.nlm.nih.gov/10069247/)
- [Pulmonary vascular lesions in the toxic oil syndrome in Spain (PMC459646)](https://pmc.ncbi.nlm.nih.gov/articles/PMC459646/)
- [The toxic oil syndrome (PMID:8001309)](https://pubmed.ncbi.nlm.nih.gov/8001309/)
- [Toxic Oil Syndrome: Review of Immune Aspects of the Disease](https://www.tandfonline.com/doi/full/10.1080/15476910590960143)
- [Toxic-Oil Syndrome — CHEST Journal](https://journal.chestnet.org/article/S0012-3692(16)49122-1/fulltext)
- [Biotransformation of PAP to PAA (PMID:8555405)](https://pubmed.ncbi.nlm.nih.gov/8555405/)
- [Absorption and effects of PAP esters — Lipids](https://link.springer.com/article/10.1007/s11745-001-0823-4)
- [Acute pathology of fatty acid anilides and PAP diester in mice (PMID:10650923)](https://pubmed.ncbi.nlm.nih.gov/10650923/)
- [Comparison of acute pathology induced by PAP and mono-oleoyl ester (PMID:7779449)](https://pubmed.ncbi.nlm.nih.gov/7779449/)
- [Effects of PAP esters on reactive oxygen metabolites in human PMNs](https://www.sciencedirect.com/science/article/abs/pii/S0378427496038623)
- [Orphanet: Toxic oil syndrome (ORPHA:227972)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=227972)
- [Toxic oil syndrome — MalaCards / MONDO](https://www.malacards.org/card/toxic_oil_syndrome)
- [Toxic oil syndrome: Survival in the whole cohort between 1981 and 1995](https://www.sciencedirect.com/science/article/abs/pii/S0895435603001197)
- [Toxic oil syndrome: health-related quality-of-life assessment using SF-36 (IJE 2022)](https://academic.oup.com/ije/article/51/2/491/6301183)
- [Late cases of toxic oil syndrome: agent persisted in stored oil](https://www.sciencedirect.com/science/article/abs/pii/0278691589900471)
- [Frontal-subcortical dysfunction in toxic oil syndrome (Frontiers 2025)](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1666809/full)
- [Toxic oil syndrome. A long-term follow-up of a cohort of 332 patients (PMID:8412642)](https://pubmed.ncbi.nlm.nih.gov/8412642/)
- [DR2 antigens associated with severity of disease in TOS (PMID:10746782)](https://pubmed.ncbi.nlm.nih.gov/10746782/)
- [Frequencies of HLA-A24 and HLA-DR4-DQ8 in chronic TOS (PMID:8803534)](https://pubmed.ncbi.nlm.nih.gov/8803534/)
- [Genetic approaches in the understanding of Toxic Oil Syndrome](https://www.sciencedirect.com/science/article/abs/pii/S0378427405003103)
- [A search for an animal model of the Spanish toxic oil syndrome](https://www.sciencedirect.com/science/article/abs/pii/S027869150200114X)
- [TOS: genetic restriction and immunomodulatory effects in HLA-transgenic mice (PMID:15979827)](https://pubmed.ncbi.nlm.nih.gov/15979827/)
- [The toxic oil syndrome: an exogenously induced autoimmune reaction (PMID:9112238)](https://pubmed.ncbi.nlm.nih.gov/9112238/)
- [Toxic oil syndrome: features overlapping various forms of scleroderma (PMID:3961509)](https://pubmed.ncbi.nlm.nih.gov/3961509/)
- [Clinical, pathologic, and immunopathologic manifestations of TOS: 14 cases](https://www.sciencedirect.com/science/article/abs/pii/S0190962288700468)
- [Cytokine mRNA expression in lung tissue from TOS patients: Th2 mechanism (PMID:9074654)](https://pubmed.ncbi.nlm.nih.gov/9074654/)
- [Fibrogenic growth factors in EMS and TOS (PMID:8285738)](https://pubmed.ncbi.nlm.nih.gov/8285738/)
- [L-tryptophan implicated in EMS causes fasciitis/perimyositis in Lewis rat (PMID:2243145)](https://pubmed.ncbi.nlm.nih.gov/2243145/)
- [3-(Phenylamino)alanine — link between EMS and TOS (Mayo Clin Proc)](https://www.mayoclinicproceedings.org/article/S0025-6196(12)60172-4/fulltext)
- [An investigation of the cause of EMS associated with tryptophan use (NEJM 1990)](https://www.nejm.org/doi/full/10.1056/NEJM199008093230601)
- [Clinical Epidemiology of Toxic-Oil Syndrome (NEJM 1983)](https://www.nejm.org/doi/full/10.1056/NEJM198312083092302)
- ["Lo de la colza": mass poisoning, state neglect, and corruption — Nursing Clio (2025)](https://nursingclio.org/2025/07/31/lo-de-la-colza-mass-poisoning-state-neglect-and-corruption-after-the-spanish-transition/)
- [Toxic Oil Syndrome: Current Knowledge and Future Perspectives (PMC1059810)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1059810/)
- [Blood Biomarkers of Neurodegeneration over Four Decades After TOS (PMC12155236)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155236/)
- [Cognitive Functioning in TOS Survivors: Case-Control Study (PMC12155933)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12155933/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 28 |
| On topic | 15 |
| Off topic | 0 |

28 of 29 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0016421` (3 mentions) - the report calls it "if available"; MONDO calls it **toxic oil syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0100672` (obsolete Vaginal hernia) (1 mention) - replaced by `HP:0031607`
- `NCIT:C29688` (GR6 Protein) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
