---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T16:11:15.199373'
end_time: '2026-08-22T16:16:58.287708'
duration_seconds: 343.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aconitine Poisoning
  mondo_id: ''
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
  web_search_requests: 17
  num_turns: 27
  total_cost_usd: 1.7458768000000002
  session_id: dbeb19c7-f0c3-5dc5-b8bb-7894f948fb0c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aconitine Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Aconitine Poisoning** covering all of the
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

I'll research aconitine poisoning across mechanism, clinical, epidemiology, treatment, and genetic/model-organism angles using parallel searches.

Let me verify precise ontology term IDs/labels using this repo's OAK tooling, since the report is meant to feed dismech curation.

Given the non-interactive nature of this task, I'll finalize the report now with best-effort ontology term suggestions (flagged for verification per standard curation practice) rather than blocking on tool-approval prompts.

---

# Aconitine Poisoning — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Aconitine poisoning (aconite poisoning, monkshood/wolfsbane poisoning) is an acute toxidrome caused by ingestion, and less commonly cutaneous/mucosal absorption, of aconitine and related C19-diterpenoid alkaloids (mesaconitine, hypaconitine, jesaconitine, yunaconitine) found in *Aconitum* species (Ranunculaceae; monkshood, wolfsbane; Chinese: Fuzi/Chuanwu/Caowu). It is a toxin-mediated, non-genetic (environmental/toxicological) disease characterized predominantly by neurologic, gastrointestinal, and life-threatening cardiovascular (arrhythmic) manifestations resulting from persistent activation of voltage-gated sodium channels ([Chan, *Clin Toxicol* 2009, PMID:19514874](https://pubmed.ncbi.nlm.nih.gov/19514874/); [Zhou et al., *Forensic Sci Res* 2020, PMC7241456](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241456/)).

**Key identifiers.**
- **ICD-10-CM:** T46.991–T46.996 series is used for aconitine as a cardiotoxic agent poisoning in some coding schemes; general plant-toxin poisoning may also be coded under T62.2 (other noxious substances eaten as food, poisonous plants) depending on the jurisdiction's coding convention.
- **MeSH:** "Aconitine" (chemical, D000109); "Aconitum" (plant genus, D000110); "Plant Poisoning" (D010942).
- **MONDO/OMIM/Orphanet:** No dedicated disease-entity ID was identified — this is modeled as an environmental/toxic exposure syndrome rather than a classical nosological disease entity in these resources; curation as a dismech Environmental-category entry (parallel to `Arsenic_Poisoning`) is appropriate rather than as a genetic Disease.
- **CHEBI:** aconitine, mesaconitine, hypaconitine, and jesaconitine each have dedicated CHEBI small-molecule entries (exact CURIEs should be confirmed via OAK/CHEBI lookup before curation).

**Common synonyms:** Aconite poisoning, monkshood poisoning, wolfsbane poisoning, *Aconitum* alkaloid toxicity, Fuzi poisoning, Chuanwu/Caowu poisoning, "bushi" poisoning (Japan).

**Evidence basis:** Information is derived almost entirely from **aggregated case reports/case series** (individual poisoning episodes reported in emergency medicine, toxicology, and forensic literature), a small number of **retrospective cohort/registry analyses** (e.g., mainland China 2004–2015 retrospective, Hong Kong incidence studies), and **preclinical mechanistic studies** in cell lines (H9c2 cardiomyocytes), zebrafish embryos, and rodents. There is no large prospective clinical trial base, consistent with an acute poisoning syndrome rather than a chronic disease.

---

## 2. Etiology

**Disease causal factor:** Direct **environmental/toxicological** — ingestion (occasionally topical/mucosal exposure) of aconitine or related *Aconitum* diterpenoid alkaloids. This is fundamentally a xenobiotic exposure, not a genetic or infectious disease.

**Risk factors**

*Environmental/behavioral (dominant risk pathway):*
- Ingestion of **improperly processed or raw** *Aconitum* roots/tubers in traditional Chinese medicine (TCM) preparations (Fuzi, Chuanwu, Caowu) — inadequate boiling/steaming leaves toxic diester-diterpenoid alkaloid (DDA) content above safe thresholds ([Frontiers 2026, toxicology/detox review](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1750573/full)).
- Consumption of **homemade medicinal liquor/wine** steeped with *Aconitum* roots — a recurrent cause of clusters, e.g., the 2018 Chongqing, China outbreak reported by CDC MMWR ([MMWR 71(16), 2022](https://www.cdc.gov/mmwr/volumes/71/wr/pdfs/mm7116a2-h.pdf); [PMC9042358](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9042358/)).
- **Misidentification** of *Aconitum* tubers as edible plants (e.g., confused with wild ginseng, horseradish, or other root vegetables) leading to accidental food poisoning.
- **Co-ingestion with ethanol**, which potentiates aconitine-induced arrhythmogenesis ("ethanol-aconitine induced arrhythmia" is a specifically studied toxicological interaction; [PMID:32250090](https://pubmed.ncbi.nlm.nih.gov/32250090/)).
- **Excessive dosing / self-medication** with prepared aconite herbal formulas beyond recommended limits.
- **Intentional self-poisoning (suicide/self-harm)** — reported cases exist in both Western and Asian settings ([ScienceDirect, "Intentional ingestion of aconite: two cases of suicide"](https://www.sciencedirect.com/science/article/pii/S2665910720301080)).
- Geographic/cultural exposure: highest incidence in regions with active TCM, Ayurvedic, or Tibetan medicine use (mainland China, Hong Kong, Taiwan, Japan, Nepal, India), though sporadic cases occur worldwide from ornamental monkshood ingestion.

*Pharmacogenetic/host factors (plausible but not directly clinically demonstrated):*
- Individual variation in **CYP3A4/CYP3A5 and CYP2D6** activity — the principal enzymes metabolizing aconitine, mesaconitine, and hypaconitine via demethylation, N-deethylation, dehydrogenation, and hydroxylation ([PMID:21277363](https://www.ncbi.nlm.nih.gov/pubmed/21277363)). CYP2D6 is highly polymorphic (>130 star alleles; poor/intermediate/extensive/ultrarapid metabolizer phenotypes), and reduced-function alleles could plausibly prolong toxin exposure, though this has not been directly correlated with clinical poisoning severity in published human case series.
- **Elderly age** is repeatedly cited as a poor-prognosis modifier due to diminished physiological (cardiac, renal, hepatic) reserve rather than a distinct susceptibility mechanism.

**Protective factors**
- **Adequate herbal processing** (boiling/steaming *Aconitum* roots >2 hours) hydrolyzes the highly toxic C19-diester diterpenoid alkaloids to markedly less toxic monoester and non-ester derivatives, reducing total DDA content to <0.02% (200 μg/g) — the principal mitigation strategy used in TCM ([Frontiers review, Lai et al. 2019](https://journals.sagepub.com/doi/full/10.1177/1934578X19881548)).
- Co-administration with **Glycyrrhiza uralensis** (licorice) in classical TCM formulas has been shown experimentally to promote CYP3A-mediated metabolism of *Aconitum* toxic components, attenuating toxicity ([PMC9236245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9236245/)).
- No genetic protective variant has been specifically characterized for aconitine toxicity.

**Gene–environment interactions:** The principal G×E axis is pharmacogenetic (CYP3A4/CYP2D6 metabolizer status) modulating the rate of clearance of an environmental toxin — i.e., a toxicokinetic rather than a toxicodynamic interaction. No genome-wide association or candidate-gene susceptibility study specific to aconitine poisoning was identified.

---

## 3. Phenotypes

Aconite poisoning classically produces a triad of **neurologic, gastrointestinal, and cardiovascular** manifestations, with onset typically **within minutes to 2 hours** (documented range 3 minutes to 6 hours) of ingestion ([Chan 2009, PMID:19514874](https://pubmed.ncbi.nlm.nih.gov/19514874/); Taiwan case series latent period 10–90 min). In a 17-patient Taiwan case series, neurologic features occurred in 17/17, cardiovascular in 14/17, gastrointestinal in 9/17, and other in 5/17 patients (Annals of Emergency Medicine, [PMID:15111916](https://pubmed.ncbi.nlm.nih.gov/15111916/)).

**Neurologic/sensory (early/hallmark signs):**
- **Perioral/circumoral paresthesia and numbness** — often the earliest, most characteristic symptom; suggested HPO: Paresthesia (**HP:0003401**) — verify a more specific perioral term.
- Numbness/paresthesia of the extremities and tongue
- Ataxia (**HP:0001251**)
- Muscle weakness (**HP:0001324**), fasciculations
- Seizures (**HP:0001250**)
- Reduced consciousness / coma (**HP:0001259**)

**Gastrointestinal:**
- Nausea (**HP:0002018**), vomiting (**HP:0002013**)
- Abdominal pain (**HP:0002027**)
- Diarrhea (**HP:0002014**)
- Hypersalivation/sialorrhea

**Cardiovascular (drives mortality):**
- Palpitations
- Hypotension (**HP:0002615**), shock/cardiogenic shock
- Bradycardia (**HP:0001662**) or sinus tachycardia — bidirectional autonomic effects reported
- Ventricular ectopy, **ventricular tachycardia** (bidirectional VT is the classically described ECG hallmark), ventricular fibrillation, torsades de pointes (suggested HPO: Ventricular arrhythmia/Ventricular tachycardia — verify exact term, e.g., candidates near **HP:0004308**/**HP:0011675**)
- Cardiac arrest (**HP:0001695**)
- Refractory "electrical storm" in severe cases

**Other:** Sweating/diaphoresis, respiratory depression/failure (**HP:0002878**), hypothermia in some reports.

**Phenotype characteristics:**
- **Onset:** Acute, minutes to hours post-exposure — this is uniformly an **adult-onset acute** presentation (age of "onset" reflects timing of exposure, not developmental stage), though pediatric accidental exposures are reported.
- **Severity:** Highly variable — dose-dependent, ranging from mild paresthesia/GI upset to fulminant cardiogenic shock and death within hours.
- **Progression:** Rapid, non-relapsing (single-exposure toxidrome); severity escalates over the first several hours if untreated, then resolves with toxin clearance/elimination (half-life estimates around several hours have been reported, though pharmacokinetic data in poisoned humans are limited and heterogeneous).
- **Frequency among affected individuals:** Neurologic features are near-universal (~100% in case series); cardiovascular involvement occurs in a large minority to majority of symptomatic cases (e.g., 14/17, ~82%, in the Taiwan series); ventricular arrhythmias specifically occurred in ~4/17 (~24%) of that cohort.

**Quality of life impact:** No dedicated QoL instrument data exist for this acute toxidrome. Survivors of severe poisoning with cardiac arrest may have anoxic neurologic sequelae; most survivors of non-arrest presentations recover without long-term functional impairment, as the pathology is a reversible ion-channel-mediated electrophysiological/toxic insult rather than structural tissue destruction (absent secondary hypoxic-ischemic injury).

---

## 4. Genetic/Molecular Information

Aconitine poisoning is **not a Mendelian/genetic disease** — there are no causal or pathogenic germline variants. The molecular biology relevant to curation concerns (a) the **pharmacological target** and (b) **metabolizing-enzyme pharmacogenetics**:

**Molecular target (not a "causal gene" but the toxin's binding target):**
- **SCN5A** (cardiac voltage-gated sodium channel Nav1.5, hgnc:10593) — principal cardiac target; aconitine binds neurotoxin receptor **site 2** on the α-subunit, favoring the open channel state and causing persistent activation/blocking of inactivation, producing sustained Na⁺ influx ([Zhou et al. 2020, PMC7241456](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241456/); [PMID:9430411](https://pubmed.ncbi.nlm.nih.gov/9430411/)).
- Related neuronal/skeletal-muscle sodium channels (SCN1A–SCN4A family) mediate the neurologic and neuromuscular manifestations via the same site-2 mechanism on nerve and muscle membranes.
- Structural work on the bacterial homolog NaChBac localizes an aconitine pore-blocking interaction to residue **F224**, and aconitine has also been shown to block peak current and shift activation of **Nav1.7** (SCN9A) — relevant to the paresthesia phenotype.
- Downstream, aconitine-induced Ca²⁺ overload in cardiomyocytes is mediated in part through **TRPV2** (transient receptor potential cation channel subfamily V member 2) upregulation via **p38 MAPK** signaling, driving mitochondrial-pathway apoptosis (increased Bax/cleaved caspase-3, decreased Bcl-2) ([Wang et al. 2021, *ECAM*, PMC8426055](https://pmc.ncbi.nlm.nih.gov/articles/PMC8426055/)).

**Metabolizing-enzyme genes (pharmacokinetic, not causal):**
- **CYP3A4** (hgnc:2637) and **CYP3A5** — primary hepatic metabolizers of aconitine, mesaconitine, and hypaconitine (Km/Vmax values reported per isoform; [PMID:21277363](https://www.ncbi.nlm.nih.gov/pubmed/21277363), [PMID:21550385](https://pubmed.ncbi.nlm.nih.gov/21550385/)).
- **CYP2D6** (hgnc:2625) — secondary contributor, highly polymorphic (poor/intermediate/extensive/ultrarapid metabolizer phenotypes).
- **CYP2C19**, **CYP2E1**, **CYP1A2** — minor contributing isoforms for hypaconitine and other congeners.

**Pathogenic variants / allele frequency / somatic-vs-germline:** Not applicable — no disease-causing germline or somatic variant is implicated. This distinguishes aconitine poisoning from congenital sodium-channelopathies (e.g., Brugada syndrome, Long QT type 3) that share the *SCN5A* target but arise from inherited gain-of-function/loss-of-function variants rather than exogenous toxin binding — a mechanistically relevant but etiologically distinct comparator (see `cardiac_ion_channel_repolarization` module in dismech's channelopathy modeling).

**Epigenetic/chromosomal information:** None reported; not applicable to this acute toxic exposure.

---

## 5. Environmental Information

**Environmental factors (primary etiology, see §2):**
- Ingestion of raw or improperly processed *Aconitum* spp. tubers/roots (Fuzi, Chuanwu, Caowu; *A. carmichaelii*, *A. kusnezoffii*, *A. napellus*)
- Homemade herbal/medicinal liquor or soup prepared with aconite roots
- Contamination of other herbal products by aconite roots (misidentification during herb collection/processing) — see [PMID:26481590](https://pubmed.ncbi.nlm.nih.gov/26481590/)
- Excessive or improperly dosed TCM/Ayurvedic/Tibetan medicine formulas containing prepared aconite
- Suggested ECTO term category: exposure to plant alkaloid toxin via ingestion (specific ECTO CURIE for aconitine/Aconitum exposure should be verified via OAK before curation).

**Lifestyle factors:**
- Concurrent ethanol consumption potentiates cardiotoxicity ("ethanol-aconitine induced arrhythmia," [PMID:32250090](https://pubmed.ncbi.nlm.nih.gov/32250090/))
- Self-medication practices and use of unregulated/homemade herbal remedies without professional oversight
- Occupational/recreational exposure is rare but reported for gardeners/horticulturists handling ornamental monkshood (cutaneous absorption)

**Infectious agents:** Not applicable — aconitine poisoning is a purely chemical/toxin-mediated disease with no infectious component.

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **Ingestion/absorption of aconitine (and congeners mesaconitine, hypaconitine, jesaconitine)** → rapid gastrointestinal or mucosal absorption, with symptom onset often within minutes given high lipid solubility and membrane permeability.
2. **Binding to neurotoxin receptor site 2 on voltage-gated sodium channels** (Nav1.5/SCN5A in cardiomyocytes; Nav1.7/SCN9A and other neuronal isoforms in peripheral nerves; skeletal-muscle Nav1.4) in the **open channel state** → the channel is locked into persistent activation and becomes refractory to normal inactivation.
3. **Sustained Na⁺ influx at resting membrane potential** → membrane depolarization, repetitive/ectopic action potential firing in nerve (paresthesia, numbness, seizures), skeletal muscle (weakness, fasciculation), and cardiac tissue.
4. **Downstream cardiac electrophysiological consequences**: sodium-channel-driven early and delayed afterdepolarizations (via secondary increases in intracellular Na⁺ and Ca²⁺), producing triggered activity and re-entrant substrate → **ventricular ectopy, bidirectional ventricular tachycardia, ventricular fibrillation, and torsades de pointes**.
5. **Cellular/molecular amplification loop in cardiomyocytes**: aconitine activates **p38 MAPK** signaling, which upregulates and promotes plasma-membrane trafficking of **TRPV2**, a calcium-permeable channel, causing **sustained intracellular Ca²⁺ overload** ([PMC8426055](https://pmc.ncbi.nlm.nih.gov/articles/PMC8426055/); [Hindawi ECAM 2021](https://www.hindawi.com/journals/ecam/2021/9567056/)).
6. **Mitochondrial dysfunction and oxidative stress**: Ca²⁺ overload and direct mitochondrial injury increase reactive oxygen species (ROS) production, decrease PGC-1α expression and ATP content, and disrupt mitochondrial membrane potential.
7. **Apoptotic and inflammatory amplification**: increased pro-apoptotic Bax and cleaved caspase-3, decreased anti-apoptotic Bcl-2, and activation of the **NLRP3/ASC/caspase-1** inflammasome axis drive cardiomyocyte apoptosis and inflammation, compounding the primary electrophysiological insult.
8. **Clinical endpoint**: refractory ventricular arrhythmias and/or cardiogenic shock/cardiac arrest — the principal cause of death in severe poisoning; concurrently, GI (direct mucosal irritant/vagal effects) and neuromuscular (peripheral nerve/muscle Na⁺-channel) manifestations occur in parallel, largely upstream-independent of the cardiac cascade.

**Upstream vs. downstream:** The sodium-channel binding event (step 2) is the shared upstream trigger for all three organ-system manifestations (neuro, GI/autonomic, cardiac); the TRPV2/p38 MAPK/Ca²⁺-overload/apoptosis axis (steps 5–7) is a **cardiomyocyte-specific downstream amplifier** distinct from the primary electrophysiological (arrhythmogenic) mechanism, i.e., this maps to two parallel but interacting node types: an acute electrophysiological node (arrhythmia, minutes-scale) and a slower cytotoxic/apoptotic node (myocardial injury, hours-scale).

**Cell types involved:** cardiomyocytes (CL:0000746), peripheral sensory/motor neurons (CL:0000540), skeletal muscle cells (CL:0000188/CL:0000187), gastrointestinal epithelial/enteric neuronal elements (indirect, vagally mediated).

**Biological processes / suggested GO terms:**
- Voltage-gated sodium channel activity (GO:0005248; cardiac-specific GO:0086006)
- Cardiac muscle cell action potential (GO:0086001) / regulation of heart rate by cardiac conduction (GO:0086091)
- p38MAPK cascade (GO:0038066)
- Calcium ion transmembrane transport (GO:0070588)
- Reactive oxygen species metabolic process (GO:0072593)
- Apoptotic process (GO:0006915); intrinsic apoptotic signaling pathway (GO:0097193)
- NLRP3 inflammasome complex assembly (GO:0140639, verify)

**Protein dysfunction:** Not a loss/gain-of-function mutation but a **pharmacological gain-of-function-like state** induced by toxin binding — the channel protein is structurally normal but functionally "trapped open" by the alkaloid ligand (mechanistically analogous to, but distinct from, congenital SCN5A gain-of-function long-QT type 3 mutations).

**Metabolic changes:** Hepatic CYP3A4/3A5/2D6-mediated Phase I biotransformation (demethylation, N-deethylation, dehydrogenation, hydroxylation) generates at least six identified metabolites of aconitine in human liver microsomes; metabolite toxicity is generally reduced relative to parent compound, making hepatic clearance a rate-limiting detoxification step.

**Immune system involvement:** Secondary/minor — cardiomyocyte NLRP3/ASC/caspase-3-mediated sterile inflammation contributes to myocardial injury but is not a primary immune-mediated disease mechanism.

**Tissue damage mechanisms:** Oxidative stress and mitochondrial dysfunction (cardiomyocytes); electromechanical dysfunction without primary structural necrosis in mild-to-moderate cases; secondary hypoxic-ischemic injury to brain/other organs may occur in cardiac-arrest survivors.

**Molecular profiling / advanced technologies:** Zebrafish embryo transcriptomic/functional studies implicate **Nrf2-HO-1/JNK-Erk signaling** in aconitine-induced developmental cardiotoxicity and oxidative stress ([PMC8097150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8097150/)); H9c2 rat cardiomyoblast cell-line studies provide the TRPV2/p38 MAPK mechanistic data above. No human single-cell, spatial transcriptomic, or CRISPR screen data specific to aconitine poisoning were identified.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (myocardium — UBERON:0000948) — arrhythmogenesis and cardiomyocyte injury; Peripheral nervous system (UBERON:0000010) — sensory/motor neuropathy-like symptoms; Gastrointestinal tract (UBERON:0001007) — direct irritant and autonomic effects.
- **Secondary:** Central nervous system (UBERON:0001017) — seizures, coma (may reflect direct toxin CNS penetration and/or secondary hypoxic injury from cardiac arrest); Skeletal muscle (UBERON:0001630) — weakness, fasciculation; Kidney — secondary injury in shock states; Liver — site of metabolism, occasional hepatotoxicity reported in animal models.
- **Body systems:** Cardiovascular, nervous (central + peripheral + autonomic), gastrointestinal, musculoskeletal, and (secondarily) respiratory systems.

**Tissue/cell level:**
- Cardiac muscle tissue / cardiomyocytes (CL:0000746)
- Peripheral sensory and motor neurons (CL:0000540 or more specific subtypes)
- Skeletal muscle fibers (CL:0000188)
- Vascular smooth muscle / endothelium (secondary, via hypotension/shock)

**Subcellular level (GO Cellular Component):**
- Plasma membrane (GO:0005886) — site of Na⁺/Ca²⁺ channel toxin action
- Mitochondrion (GO:0005739) — site of ROS generation, ATP depletion, apoptotic signaling
- Sarcoplasmic reticulum (cardiomyocyte Ca²⁺ handling, indirect)

**Localization:** Systemic/multi-organ — not laterally restricted; cardiac conduction-system involvement (His-Purkinje system) has been specifically implicated in some ventricular tachycardia cases ([Ni et al. 2025, *Ann Noninvasive Electrocardiol*](https://onlinelibrary.wiley.com/doi/10.1111/anec.70040)).

---

## 8. Temporal Development

**Onset:** Acute — this is an adult (or occasionally pediatric, accidental) acute poisoning event, not a developmental-onset disease. Symptom onset after ingestion is reported as early as 3 minutes and as late as 6 hours, with most series citing a **latent period of 10–90 minutes** and majority of symptoms manifesting **within 2 hours**.

**Progression:**
- **Early phase (minutes–1 hour):** perioral/extremity paresthesia, nausea/vomiting.
- **Escalation phase (1–several hours):** progressive neuromuscular weakness, ataxia, hypotension, cardiac arrhythmias (the critical window for clinical deterioration and intervention).
- **Critical/peak phase:** refractory ventricular arrhythmias, cardiogenic shock, cardiac arrest — typically within the first several hours to about 24 hours post-ingestion in fatal cases; in a veterinary context, "death usually occurs within 6 hours" of a lethal dose.
- **Recovery phase:** With survival past the acute arrhythmic window and toxin clearance (hepatic metabolism + supportive/extracorporeal elimination), most patients recover without permanent sequelae over days.

**Disease course pattern:** Self-limited, single-exposure acute toxidrome (not relapsing-remitting or chronic) — unless re-exposure occurs (e.g., repeated dosing errors with prepared aconite formulas).

**Disease duration:** Acute and self-limited; hospitalization typically spans days for supportive/monitoring care; ECMO-supported cases may extend to 1–2+ weeks.

**Remission patterns:** Spontaneous resolution with toxin clearance and supportive/antiarrhythmic treatment in most survivors; no disease-modifying "cure" exists — management is entirely supportive/time-buying pending endogenous elimination.

**Critical periods:** The first few hours post-ingestion represent the critical intervention window (decontamination, early antiarrhythmic/hemoperfusion therapy, and — if arrhythmias become refractory — early initiation of VA-ECMO), as repeatedly emphasized across case reports ([PMC10835702](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835702/)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Approximately **5,000 aconite poisoning incidents** were reported across China, Germany, Japan, and other countries during 1993–2005, with most fatal poisonings occurring in China.
- A retrospective analysis of mainland China case reports (2004–2015) identified **53 victims across 27 published case reports**.
- Hong Kong has published dedicated incidence studies of herb-induced aconitine poisoning (Chan TY, *Drug Saf* 2002; [link](https://link.springer.com/article/10.2165/00002018-200225110-00006)) given its documented endemic TCM-related exposure.
- Sporadic outbreaks/clusters are reported globally, including a homemade medicinal liquor cluster in **Chongqing, China (2018)** described by CDC's MMWR ([MMWR 71(16), 2022](https://www.cdc.gov/mmwr/volumes/71/wr/pdfs/mm7116a2-h.pdf)), and case reports from Nepal, Bangladesh, and Western countries (typically involving ornamental monkshood or imported herbal products).

**Inheritance pattern:** Not applicable — this is not a heritable disease (no Mendelian inheritance, penetrance, expressivity, anticipation, mosaicism, or carrier-frequency concepts apply).

**Population demographics:**
- **Affected populations:** Highest burden in East and South Asian populations with active use of TCM, Tibetan medicine, and Ayurveda (China, Hong Kong, Taiwan, Japan, Nepal, India); sporadic cases occur worldwide (Europe, North America) typically from ornamental *Aconitum napellus* or imported herbal remedies.
- **Geographic distribution:** Endemic in regions with traditional herbal medicine practice; case clusters often geographically tied to a specific herbal product batch or local liquor preparation.
- **Sex ratio:** Case series show relatively balanced sex distribution (e.g., 9 men/8 women in the Taiwan cohort), though ratios vary by cohort and exposure route.
- **Age distribution:** Predominantly adults (reported cohort ranges e.g., 30–70 years); elderly patients carry disproportionately poor prognosis due to reduced physiological reserve.

---

## 10. Diagnostics

**Clinical tests:**
- **ECG monitoring** is the central bedside diagnostic and risk-stratification tool — bidirectional ventricular tachycardia is considered a characteristic (though not pathognomonic) finding in aconitine poisoning; monitoring for ventricular ectopy, VT, VF, and torsades de pointes is essential.
- **Electrolyte panel** (magnesium, potassium) — informs both diagnosis of arrhythmia risk and guides magnesium-based therapy.
- **Laboratory tests:** No routine clinical (point-of-care) assay for aconitine exists; diagnosis is primarily clinical (history of herbal/plant exposure + characteristic symptom triad + ECG findings).
- **Biomarkers:** None validated for clinical use; research-grade LC-MS/MS quantification is used in specialized/forensic settings.

**Specialized/forensic testing:**
- **LC-MS/MS** quantification of aconitine, mesaconitine, hypaconitine, and jesaconitine in whole blood, serum, or urine — validated methods report linearity 1.25–40 ng/mL with detection limits of 0.3–0.5 ng/mL ([Meng et al., *Forensic Toxicol*, PMID cited via [link](https://link.springer.com/article/10.1007/s11419-008-0060-z)]); other assays report LOD/LOQ of 0.1/0.5 ng/g in blood.
- Fatal case postmortem series report blood aconitine concentrations spanning **2.3–86.2 μg/L** (femoral blood), with detection also possible in gastric content, urine, and kidney tissue.
- **Toxicological history-taking** (identifying the specific herbal product, liquor, or plant material ingested) is often essential for definitive diagnosis, given the absence of routine hospital-based assays.

**Genetic testing:** Not applicable — this is not a genetic disease; no genetic test is diagnostic.

**Clinical criteria:** No formal diagnostic-criteria consensus statement (e.g., DSM/ICD-style) exists; diagnosis relies on a combination of exposure history, characteristic symptom triad (neuro + GI + cardiac), and supportive ECG findings, per toxicology reviews ([PMID:19514874](https://pubmed.ncbi.nlm.nih.gov/19514874/), [PMID:38613376](https://pubmed.ncbi.nlm.nih.gov/38613376/)).

**Differential diagnosis:** Other cardiotoxic plant/alkaloid poisonings (e.g., cardiac glycoside/digoxin toxicity, taxine/yew poisoning, local anesthetic systemic toxicity), other causes of bidirectional VT (severe digoxin toxicity, catecholaminergic polymorphic VT), and other causes of perioral paresthesia (hyperventilation, hypocalcemia, ciguatera/tetrodotoxin poisoning — note tetrodotoxin has an *opposite* sodium-channel mechanism, site 1 blockade vs. aconitine's site 2 activation, making the clinical distinction mechanistically instructive).

**Screening:** No population screening program exists (this is an acute exposure event, not a screenable heritable/chronic condition); prevention relies on regulatory control of raw aconite herb sale/processing (see §13).

---

## 11. Outcome/Prognosis

**Mortality:** Reported case-fatality rates vary substantially by study population and severity: an overall **in-hospital mortality of ~5.5%** has been cited for aconite poisoning broadly, while more severe/referred cohorts report much higher fatality — one retrospective analysis of 35 cases found **17 deaths (49%)** — reflecting substantial referral/severity bias across published series. A dedicated forensic toxicology series identified **25 aconitine-induced deaths (2005–2023)** in one jurisdiction ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1344622324001743)).

**Cause of death:** Predominantly **refractory ventricular arrhythmias** (VT/VF, "electrical storm") and **asystole/cardiac arrest**; cardiogenic shock is the other principal proximate cause.

**Morbidity/functional outcomes:** Survivors of non-arrest presentations generally have **full recovery without chronic sequelae**, consistent with the reversible (non-structural) nature of the primary ion-channel-mediated pathology; survivors of cardiac arrest may sustain anoxic brain injury and other complications common to any resuscitated arrest.

**Complications:** Cardiogenic shock, multi-organ hypoperfusion injury (acute kidney injury, hepatic injury) in severe/prolonged shock states, and — rarely — mechanical circulatory support-related complications (bleeding, limb ischemia) in ECMO-treated patients.

**Prognostic factors:**
- **Dose/exposure magnitude** — the poisonous dose has been cited as low as ~0.2 mg with a lethal dose in the range of **2–5 mg** (and separately, an oral minimum lethal human dose of **1–2 mg** and a "lowest lethal dose" of 28 mg/kg bodyweight reported in another source — figures vary across the literature and should be treated as approximate ranges pending consolidation from a systematic toxicology reference).
- **Time to treatment initiation** — the first several hours represent the critical intervention window.
- **Age** — elderly patients have disproportionately worse outcomes.
- **Early recognition of refractory arrhythmia and escalation to VA-ECMO** — case reports consistently associate early ECMO initiation (before irreversible multi-organ injury) with survival in otherwise refractory cases ([PMC10835702](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835702/); [WJCC 2024](https://doi.org/10.12998/wjcc.v12.i21.4842)).
- **No specific antidote exists**, which is repeatedly emphasized as a key driver of adverse outcomes in refractory cases.

---

## 12. Treatment

There is **no specific antidote** for aconitine poisoning; management is entirely **supportive and time-buying**, aimed at maintaining perfusion and cardiac rhythm until endogenous (hepatic CYP3A4/2D6-mediated) elimination occurs.

**Decontamination:**
- Early **activated charcoal** administration (gastric decontamination) if presenting soon after ingestion.
- Gastric lavage/emesis/catharsis reported historically, though evidence for efficacy is limited.

**Extracorporeal elimination:**
- **Charcoal hemoperfusion** — used in patients with ventricular arrhythmias; some series report successful reversion to sinus rhythm during/after hemoperfusion, though direct evidence of alkaloid removal efficacy is limited ([PMID unlisted; Annals of Emerg Med case series](https://www.annemergmed.com/article/S0196-0644(03)01131-4/abstract)).
- **Continuous renal replacement therapy (CRRT)** used adjunctively in multimodal regimens.

**Antiarrhythmic pharmacotherapy** (evidence largely from pooled case-report analysis — [Fitzgerald et al., *Clin Toxicol* 2017, PMID:28421842](https://pubmed.ncbi.nlm.nih.gov/28421842/)):
- **Flecainide** and **amiodarone** show the strongest association with return to sinus rhythm across pooled human case reports.
- **Lidocaine**, **mexiletine**, **procainamide**, and **electrical cardioversion** are less consistently effective and are more often associated with arrhythmia persistence.
- **Magnesium sulfate** — used both as electrolyte correction and reported in successful case reports of arrhythmia reversal / combination therapy for "aconitine-induced electrical storm" ([PMC12573093](https://pmc.ncbi.nlm.nih.gov/articles/PMC12573093/)).
- **Atropine** for symptomatic bradycardia.

**Advanced circulatory/mechanical support:**
- **Prolonged cardiopulmonary resuscitation (CPR)** and **cardiopulmonary bypass** are recommended as "time-buying" strategies in refractory cases pending toxin clearance.
- **VA-ECMO (veno-arterial extracorporeal membrane oxygenation)** — repeatedly reported as life-saving in refractory ventricular arrhythmia/cardiogenic shock; multiple recent case reports (2023–2025) document successful outcomes with early ECMO initiation, sometimes combined with hemoperfusion.
- **Ventricular assist device** support reported in at least one historical case ([PMID:7892979](https://pubmed.ncbi.nlm.nih.gov/7892979/)).

**Supportive care:**
- Continuous cardiac monitoring, hemodynamic support (vasopressors as needed), airway management/ventilatory support for respiratory depression, seizure management (benzodiazepines).

**Experimental/investigational targets:** **TRPV2** has been proposed as a potential molecular target for future pharmacotherapy of aconitine-induced cardiomyocyte injury, based on preclinical (H9c2 cell) mechanistic data — not yet in clinical use.

**Suggested NCIT terms for treatment annotation:** Pharmacotherapy (NCIT:C15986; antiarrhythmic agents as `therapeutic_agent`), Supportive Care (NCIT:C15747); Hemoperfusion and ECMO/extracorporeal circulatory support procedure terms should be verified via NCIT lookup before curation (exact CURIEs not confirmed in this research pass).

---

## 13. Prevention

**Primary prevention:**
- **Proper herbal processing**: boiling/steaming raw *Aconitum* roots for >2 hours hydrolyzes toxic C19-diester diterpenoid alkaloids to non-toxic/less-toxic derivatives, reducing total DDA content to <0.02% (200 μg/g) — the cornerstone of TCM safety practice.
- **Regulatory alkaloid-content limits**: e.g., Korean regulatory authorities cap total alkaloid content (as benzoylaconine) at 0.33% by titration method in prepared aconite products.
- **Scheduling/controlled distribution**: In India, *Aconitum* herbs are classified as **Schedule E(1) poisons** under the Drugs and Cosmetics Rules, restricting use to supervision by licensed Ayurvedic practitioners.
- Public health messaging against **self-preparation of homemade medicinal liquor/soup** using raw aconite roots, and against consuming unregulated herbal products of uncertain provenance.
- Avoidance of **co-ingestion with alcohol**, given documented potentiation of cardiotoxicity.

**Secondary prevention (early detection):** No population screening program exists; early clinical recognition of the neuro-GI-cardiac triad in a patient with a compatible exposure history is the operative "detection" strategy, supported by rapid access to ECG monitoring in emergency settings.

**Tertiary prevention:** Standardized emergency-department and ICU protocols for early antiarrhythmic therapy, hemoperfusion, and low-threshold escalation to VA-ECMO in refractory cases (see §12) function as tertiary prevention of death/major morbidity once poisoning has occurred.

**Immunization:** Not applicable (non-infectious toxin exposure).

**Genetic counseling / genetic screening:** Not applicable.

**Public health interventions:** Herbal-market regulation and quality control of TCM/Ayurvedic aconite-containing products; outbreak investigation and public communication following cluster events (e.g., CDC MMWR reporting of the 2018 Chongqing homemade liquor cluster) to prevent recurrence.

**Environmental interventions:** Regulation/labeling of ornamental monkshood sale in regions where accidental horticultural exposure has been reported; supervision of herb-collection practices to prevent inadvertent contamination of other medicinal herbs with aconite roots.

---

## 14. Other Species / Natural Disease

**Taxonomy of the source organism:** *Aconitum* spp. (family Ranunculaceae), notably *A. napellus* (monkshood, Europe/temperate regions), *A. carmichaelii* (Fuzi, China), *A. kusnezoffii* (Caowu, China) — plant NCBI Taxon IDs should be confirmed via lookup if curating the source organism (not the affected host species).

**Species naturally affected by poisoning:**
- **Livestock**: Cattle and goats are most frequently affected by grazing on monkshood in pasture settings; horses are also susceptible ([HorseDVM](https://horsedvm.com/poisonous/monkshood); [CowDVM](https://www.cowdvm.com/poisonous/monkshood); [PMC4690134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4690134/)).
- **Companion animals**: Dogs are reported to be susceptible to monkshood ingestion ([Pet Poison Helpline](https://www.petpoisonhelpline.com/poison/monkshood/)).
- **Clinical signs in animals** parallel human poisoning: initial gastrointestinal distress (drooling, bloating, emesis) followed by musculoskeletal weakness, difficulty breathing, cardiac rhythm disturbances (bradyarrhythmia), and sudden death — **death typically occurs within 6 hours** of a lethal ingested dose in livestock, with cardiac effects (heart-rate slowing) often the proximate cause.

**Comparative pathology:** The core mechanism (voltage-gated sodium channel site-2 activation) is conserved across vertebrate species, given the high evolutionary conservation of the sodium channel pore and site-2 binding region — this underlies why rodent, zebrafish, and livestock/companion-animal poisoning all recapitulate the human neuro-cardiac toxidrome.

**Veterinary relevance:** Aconite/monkshood poisoning is a recognized cause of pastoral livestock loss in regions where the plant grows wild, and a recognized companion-animal (dog) poisoning risk from ornamental garden plantings; it is managed by the same supportive/antiarrhythmic principles as human poisoning, adapted to veterinary practice.

**Zoonotic potential:** Not applicable (a toxin exposure, not a transmissible infectious disease); no cross-species transmission risk beyond shared environmental exposure to the same toxic plant.

---

## 15. Model Organisms

**Rodent models:**
- **Mouse LD50 values**: oral 1.8 mg/kg, intraperitoneal 0.31 mg/kg (also cited as 0.27 mg/kg i.p. in a second source), intravenous 0.12 mg/kg — the roughly 10-fold difference between oral and parenteral LD50 reflects substantial first-pass hepatic metabolism/reduced oral bioavailability.
- **Subacute mouse poisoning models** have characterized hematological and histopathological effects of repeated low-dose aconitine exposure ([Frontiers in Veterinary Science 2022](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2022.874660/full)).
- **Rat models** have demonstrated direct embryotoxic effects during the organogenetic period, and rat studies of aconitine-induced Ca²⁺ overload/p38 MAPK-mediated apoptosis in vivo complement the H9c2 cell-line mechanistic data ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0041008X14001896)).

**Zebrafish embryo models** — an increasingly important developmental/cardiotoxicity screening platform:
- Aconitine produces **concentration-dependent embryo mortality**, arrhythmias, extended sinus venosus–bulbus arteriosus distance, and pericardial edema.
- Reported cardiotoxic thresholds: **2.5 μg/L aconitine** and **20 μg/L mesaconitine** caused deficient cardiovascular development with yolk-sac hemorrhage and early cardiac dysfunction at 96 hours post-fertilization.
- Mechanistic zebrafish studies implicate the **Nrf2-HO-1/JNK-Erk signaling axis** in aconitine-induced developmental toxicity, oxidative stress, and ROS-mediated mitochondrial apoptosis ([PMC8097150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8097150/)), and a related study links aconitine-induced cardiotoxicity to dysregulated calcium-signaling gene expression in zebrafish embryos ([PMID:30639578](https://pubmed.ncbi.nlm.nih.gov/30639578/)).
- Zebrafish models allow **comparative cardiotoxicity ranking** of different *Aconitum* diterpene alkaloids (aconitine, mesaconitine, hypaconitine, and others).

**Cell-line (in vitro) models:**
- **H9c2 rat cardiomyoblast cell line** — the principal in vitro platform for dissecting the TRPV2/p38 MAPK/Ca²⁺-overload/apoptosis mechanism described in §6, and for testing candidate mitigating compounds.

**Model characteristics — recapitulation and limitations:**
- Both rodent and zebrafish models faithfully recapitulate the core electrophysiological (arrhythmogenic) and cytotoxic (oxidative stress/apoptotic) arms of human aconitine cardiotoxicity, consistent with the high conservation of the sodium-channel target.
- Zebrafish embryo models are particularly well suited to rapid, quantitative cardiotoxicity/developmental-toxicity screening but cannot model the full adult human clinical syndrome (e.g., adult conduction-system anatomy, His-Purkinje-specific arrhythmia mechanisms reported in some human case reports).
- Livestock/companion-animal **natural disease** (rather than induced experimental model) provides real-world corroboration of the human toxidrome but is not a controlled research model system.

**Research applications:** These models are used to (a) rank comparative toxicity of different *Aconitum* alkaloid congeners, (b) dissect molecular mechanism (TRPV2, p38 MAPK, Nrf2-HO-1/JNK-Erk pathways), and (c) screen candidate therapeutic/mitigating compounds (e.g., co-administered herbal components such as *Glycyrrhiza uralensis* that promote CYP3A-mediated detoxification).

**Model databases:** No dedicated aconitine-poisoning-specific model registry exists; relevant strains/lines are accessed via standard model-organism resources (IMSR/MGI for mouse, ZFIN for zebrafish, and standard cell-line repositories such as ATCC/Cellosaurus for H9c2).

---

## Summary of Suggested Ontology Terms (for dismech curation — verify all IDs via OAK before use)

| Category | Candidate terms |
|---|---|
| **HPO** | Paresthesia (HP:0003401), Nausea (HP:0002018), Vomiting (HP:0002013), Diarrhea (HP:0002014), Abdominal pain (HP:0002027), Ataxia (HP:0001251), Muscle weakness (HP:0001324), Seizure (HP:0001250), Coma (HP:0001259), Hypotension (HP:0002615), Bradycardia (HP:0001662), Cardiac arrest (HP:0001695), Respiratory failure (HP:0002878); ventricular tachycardia/arrhythmia terms need confirmation |
| **GO (Biological Process/MF)** | Voltage-gated sodium channel activity (GO:0005248/GO:0086006), Cardiac muscle cell action potential (GO:0086001), p38MAPK cascade (GO:0038066), Calcium ion transmembrane transport (GO:0070588), Reactive oxygen species metabolic process (GO:0072593), Apoptotic process (GO:0006915) |
| **CL** | Cardiac muscle cell (CL:0000746), Neuron (CL:0000540), Skeletal muscle fiber (CL:0000188) |
| **UBERON** | Heart (UBERON:0000948), Peripheral nervous system (UBERON:0000010), Digestive system (UBERON:0001007), Skeletal muscle organ (UBERON:0001630) |
| **CHEBI** | Aconitine, mesaconitine, hypaconitine, jesaconitine (specific CURIEs to confirm via OAK CHEBI search) |
| **HGNC/Gene** | SCN5A (hgnc:10593, molecular target), CYP3A4 (hgnc:2637), CYP2D6 (hgnc:2625) — metabolizing enzymes, not causal genes |
| **NCIT (treatment)** | Pharmacotherapy (NCIT:C15986), Supportive Care (NCIT:C15747); hemoperfusion/ECMO-specific NCIT CURIEs to confirm |

---

## Sources

- [Aconite poisoning – Chan TY, *Clin Toxicol (Phila)* 2009 (PMID:19514874)](https://pubmed.ncbi.nlm.nih.gov/19514874/)
- [Research Progress on the Molecular Mechanisms of Toxicology of Ethanol-Aconitine Induced Arrhythmia (PMID:32250090)](https://pubmed.ncbi.nlm.nih.gov/32250090/)
- [Magnesium in Aconitine-Induced Electrical Storm — PMC12662806](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12662806/)
- [Aconitum sp. alkaloids: modulation of voltage-dependent Na+ channels (PMID:9430411)](https://pubmed.ncbi.nlm.nih.gov/9430411/)
- [Bidirectional ventricular tachycardia resulting from herbal aconite poisoning — Ann Emerg Med](https://www.annemergmed.com/article/S0196-0644(04)01432-5/fulltext)
- [Clinical features and management of herb-induced aconitine poisoning (PMID:15111916)](https://pubmed.ncbi.nlm.nih.gov/15111916/)
- [Recurrent malignant ventricular arrhythmias and paresthesia — a case report — PMC10740282](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10740282/)
- [Ventricular Tachycardia Possibly Originated From the His-Purkinje System — aconitine poisoning, 2025](https://onlinelibrary.wiley.com/doi/10.1111/anec.70040)
- [Ventricular Tachycardia due to Overdose of Tibetan Drugs — PMC12117196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12117196/)
- [The management of ventricular dysrhythmia in aconite poisoning (PMID:28421842)](https://pubmed.ncbi.nlm.nih.gov/28421842/)
- [Aconite poisoning managed with a ventricular assist device (PMID:7892979)](https://pubmed.ncbi.nlm.nih.gov/7892979/)
- [A Narrative Review of Aconite Poisoning and Management, 2024/2025 (PMID:38613376)](https://pubmed.ncbi.nlm.nih.gov/38613376/)
- [Aconitum Alkaloid Poisoning Because of Contamination of Herbs by Aconite Roots (PMID:26481590)](https://pubmed.ncbi.nlm.nih.gov/26481590/)
- [Research progress of aconitine toxicity and forensic analysis of aconitine poisoning — Forensic Sciences Research, PMC7241456](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241456/)
- [Case reports of aconite poisoning in mainland China 2004–2015 — retrospective analysis](https://www.sciencedirect.com/science/article/abs/pii/S1752928X1630049X)
- [Case report: Accidental aconitine poisoning from inappropriate use of Chinese patent medicine — PMC11754414](https://pmc.ncbi.nlm.nih.gov/articles/PMC11754414/)
- [Poisoning Associated with Consumption of a Homemade Medicinal Liquor — Chongqing, China, 2018, MMWR 71(16), 2022](https://www.cdc.gov/mmwr/volumes/71/wr/pdfs/mm7116a2-h.pdf)
- [Incidence of Herb-Induced Aconitine Poisoning in Hong Kong — *Drug Safety*](https://link.springer.com/article/10.2165/00002018-200225110-00006)
- [Combined blood purification and antiarrhythmic therapy for acute aconitine poisoning — PMC12482442](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12482442/)
- [Extracorporeal membrane oxygenation in cardiovascular medication poisoning — German-wide study — PMC11410930](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11410930/)
- [Treatment of aconitine poisoning using VA-ECMO — case report, WJCC 2024](https://doi.org/10.12998/wjcc.v12.i21.4842)
- [Severe aconite poisoning treated with VA-ECMO — PMC10835702](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835702/)
- [ECMO combined with hemoperfusion for aconitine poisoning — 2025](https://journals.sagepub.com/doi/10.1177/02676591241280163)
- [Involvement of CYP3A4/5 and CYP2D6 in the metabolism of aconitine (PMID:21277363)](https://www.ncbi.nlm.nih.gov/pubmed/21277363)
- [Microsomal CYP-mediated metabolism of hypaconitine (PMID:21550385)](https://pubmed.ncbi.nlm.nih.gov/21550385/)
- [Glycyrrhiza uralensis promotes CYP3A metabolism of Aconitum toxic components — PMC9236245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9236245/)
- [Simultaneous LC-MS-MS analysis of aconitine, mesaconitine, hypaconitine, jesaconitine in whole blood — Forensic Toxicology](https://link.springer.com/article/10.1007/s11419-008-0060-z)
- [Determination of aconitine in body fluids by LC-MS-MS](https://www.researchgate.net/publication/8056950_Determination_of_aconitine_in_body_fluids_by_LC-MS-MS)
- [Aconitine Induces TRPV2-Mediated Ca2+ Influx via p38 MAPK, Promotes Cardiomyocyte Apoptosis — PMC8426055](https://pmc.ncbi.nlm.nih.gov/articles/PMC8426055/)
- [Aconitine-induced Ca2+ overload causes arrhythmia and triggers apoptosis via p38 MAPK in rats](https://www.sciencedirect.com/science/article/abs/pii/S0041008X14001896)
- [Processed lateral root of Aconitum carmichaelii: cardiotonic effects and cardiotoxicity mechanisms — Frontiers in Pharmacology](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.1026219/full)
- [Involvement of Nrf2-HO-1/JNK-Erk Signaling in Aconitine-Induced Developmental Toxicity in Zebrafish Embryos — PMC8097150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8097150/)
- [Aconitum alkaloids induce cardiotoxicity in embryonic zebrafish via cardiovascular gene expression (PMID:30639578)](https://pubmed.ncbi.nlm.nih.gov/30639578/)
- [Hematological and Histopathological Effects of Subacute Aconitine Poisoning in Mouse — Frontiers in Veterinary Science 2022](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2022.874660/full)
- [Alkaloid-Containing Plants Poisonous to Cattle and Horses in Europe — PMC4690134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4690134/)
- [Monkshood Poisoning in Cattle — CowDVM](https://www.cowdvm.com/poisonous/monkshood)
- [Monkshood Poisoning in Horses — HorseDVM](https://horsedvm.com/poisonous/monkshood)
- [Monkshood Is Toxic To Dogs — Pet Poison Helpline](https://www.petpoisonhelpline.com/poison/monkshood/)
- [Quantification and Simplified Detoxification of Fuzi, Root of Aconitum carmichaelii](https://journals.sagepub.com/doi/full/10.1177/1934578X19881548)
- [The toxicology and detoxification of Aconitum: traditional and modern views — PMC8314510](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8314510/)
- [Toxicological investigation of 25 aconitine-induced deaths from 2005 to 2023](https://www.sciencedirect.com/science/article/abs/pii/S1344622324001743)
- [Intentional ingestion of aconite: two cases of suicide](https://www.sciencedirect.com/science/article/pii/S2665910720301080)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 35 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32250090` *(abstract only)*: "ethanol-aconitine induced arrhythmia,"
  - Text part not found as substring: 'ethanol-aconitine induced arrhythmia,' (note: only abstract available for PMID:32250090, full text may contain this excerpt)
- `PMC:PMC12573093` *(abstract only)*: "aconitine-induced electrical storm"
  - Text part not found as substring: 'aconitine-induced electrical storm' (note: only abstract available for PMID:41165054, full text may contain this excerpt)
