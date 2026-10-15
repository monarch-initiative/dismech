---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-01T23:30:22.333013'
end_time: '2026-09-01T23:44:00.777871'
duration_seconds: 818.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Isoniazid Toxicity
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
  - claude-opus-5
  web_search_requests: 7
  num_turns: 82
  total_cost_usd: 4.936262250000001
  session_id: 774654ad-e589-45c6-8eb2-649cfa40dfba
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 2
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isoniazid Toxicity
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Isoniazid Toxicity** covering all of the
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

I'll research isoniazid toxicity now and write the report inline.

# Isoniazid Toxicity — Research Report

**Prepared:** 2026-09-01. **Target:** Isoniazid Toxicity. **MONDO:** MONDO:0027677 (verified live against OLS4; `isObsolete: false`).

**A note before the content.** Isoniazid toxicity is not one disease. It is three, and they share only a molecule. The hepatic arm is what the liver does to isoniazid. The two neurological arms are what isoniazid does to vitamin B6. Everything below is organized around that split, because a causal chain that mixes them will be wrong in both directions.

Every PMID below was resolved individually through the NCBI E-utilities `efetch` endpoint and its identity confirmed. Where a quote came back through a summarizing fetch rather than the raw record, I mark it **[paraphrase-risk]**. Where I did not check something, I say so.

---

## 1. Disease Information

Isoniazid is a hydrazide of isonicotinic acid, in continuous first-line use against *Mycobacterium tuberculosis* since 1952. It is one of the most-prescribed drugs on earth and one of the most reliable causes of idiosyncratic acute liver failure in the United States.

The toxicity presents in three clinical entities that share no mechanism:

1. **Idiosyncratic hepatocellular drug-induced liver injury (DILI)** — dose-independent, latency of weeks to months, driven by hepatic bioactivation.
2. **Chronic pyridoxine-deprivation neuropathy** — dose-dependent, latency of months, driven by functional vitamin B6 deficiency.
3. **Acute overdose syndrome** — the triad of refractory seizures, anion-gap metabolic acidosis, and coma, appearing within 30 minutes to 2 hours of a large ingestion.

**Identifiers**

| Resource | Identifier | Verification |
|---|---|---|
| Mondo | `MONDO:0027677` "isoniazid toxicity" | Verified live (OLS4), not obsolete |
| Orphanet | `ORPHA:240887` (Mondo `equivalentTo` xref) | Xref verified in Mondo; the Orphanet record itself returned a bot-check page and I did **not** read it |
| ICD-10-CM | `T37.1X5A` adverse effect of antimycobacterial drugs, initial encounter; `T37.1X1A`–`T37.1X4A` poisoning by intent | Verified via ICD-10-CM code references |
| ICD-11 | Not verified this session |
| OMIM | No disease entry. The gene `NAT2` is OMIM **612182** (verified via HGNC REST) |
| MeSH | No dedicated descriptor. Indexed as `Isoniazid/adverse effects`, `Neurotoxicity Syndromes`, `Drug-Induced Liver Injury`, `Vitamin B 6 Deficiency/chemically induced` (from MeSH keyword blocks on PMID:29897291 and PMID:10842541) |
| CHEBI | `CHEBI:6030`, canonical label **"isoniazide"** — note the terminal *e*; the label is not "isoniazid" |
| CAS | 54-85-3; formula C₆H₇N₃O (LiverTox) |

**Synonyms.** Isoniazid hepatotoxicity; INH hepatitis; anti-tuberculosis drug-induced liver injury (AT-DILI/ATDH, a broader term covering the rifampicin and pyrazinamide contributions); isoniazid-induced peripheral neuropathy; isoniazid poisoning; INH overdose.

**Data derivation.** Both. Aggregated disease-level sources carry the frequency estimates (the ATS statement PMID:17021358, LiverTox NBK548754, StatPearls NBK531488). Individual-patient sources carry the mechanism and the severe tail (the Acute Liver Failure Study Group sera in PMID:23775837, poison-center series, case reports).

---

## 2. Etiology

The cause is the drug. There is no isoniazid toxicity without isoniazid. Everything else is a modifier of dose, of exposure duration, or of the patient.

### 2.1 Causal exposure

Adults take 300 mg daily (~5 mg/kg), or up to 900 mg once or twice weekly (LiverTox NBK548754). Acute toxicity generally requires ingestion above 20 mg/kg, and 80–150 mg/kg is reliably convulsant. Chronic hepatic injury is not dose-related in the ordinary sense.

### 2.2 Genetic risk factors

**NAT2 slow acetylation is the dominant, best-quantified genetic risk factor.** Three independent meta-analyses converge on roughly a threefold effect, and the newest is the largest ever assembled.

| Study | PMID | Year | Studies / N | Pooled OR (95% CI) |
|---|---|---|---|---|
| Dinegro et al., *Pharmacogenomics* | 42531284 | 2026 | 67 studies, ~14,000 individuals | **3.14 (2.64–3.74)** for ATDH |
| Tavkar et al., *Pharmacogenomics* | 41657030 | 2025/26 | 48 studies, 11,035 patients | **3.02 (2.50–3.64)**, I² = 58.74% |
| Mahajan & Tyagi, *BMC Genom Data* | 39639188 | 2024 | 24 studies | **2.52 (1.95–3.27)** |

Verbatim, from the 2026 record (PMID:42531284):

> "Slow acetylators showed a significant increased risk of anti‑tuberculosis drug‑induced hepatotoxicity (ATDH) compared with rapid or intermediate acetylators (OR 3.14, 95% CI 2.64-3.74), with a consistent direction of effect across populations despite moderate heterogeneity."

The same analysis separates the liver from everything else. Non-hepatic adverse reactions carry only "OR 1.65, 95% CI 1.01-2.67." The acetylator effect is a liver effect.

The 2024 meta-analysis names the specific slow genotypes carrying most of the signal (PMID:39639188, verbatim):

> "Among individuals with slow acetylator NAT2*5/7, NAT2*5/6, and NAT2*6/6 genotypes, there is a greater likelihood of association compared to other variations."

**ATP7B is a newly identified second locus, and it acts on NAT2 rather than beside it.** Yoon et al. found that copper handling and acetylation multiply (PMID:38424191, verbatim):

> "The presence of ATP7B gene 832R/R homozygosity (rs1061472) was found to co-occur with NAT2 UA in AT-DILI patients (P = 0.017) and to amplify the risk in NAT2 UA (OR 32.5 [4.5-1423], P = 7.5 × 10-6)."

The confidence interval is enormous and the discovery cohort was 112 patients. Treat the point estimate as a direction, not a number.

**HLA-B\*52:01 is a modest, replicated immune-side risk allele.** Nicoletti et al. ran a genome-wide association study across 125 cases and 11,596 controls in Indian and European populations, reporting **[paraphrase-risk]**:

> "HLA-B*52:01 was significant (meta-analysis odds ratio (OR) 2.67, 95% confidence interval (CI) 1.63-4.37, P = 9.4 × 10-5)." (PMID:33135175)

**CYP2E1 and the glutathione-S-transferase null genotypes** (`GSTM1`, `GSTT1`) appear repeatedly in candidate-gene work and are reviewed as susceptibility axes in PMID:41793109 (Arch Pharm 2026). Boelsterli and Lee's assessment is the honest one and it is worth carrying forward (PMID:24783247, verbatim):

> "Among the patient-specific determinants of susceptibility to INH-associated DILI, the importance of HLA genetic variants has been increasingly recognized, whereas the role of polymorphisms of drug-metabolizing enzymes (NAT2 and CYP2E1) has become less important and remains controversial."

Note the tension with the 2026 meta-analyses. Boelsterli was writing in 2014, and the pooled evidence since then has been kind to NAT2 and unkind to CYP2E1. State the NAT2 effect as established. State the CYP2E1 effect as contested.

### 2.3 Environmental and clinical risk factors

From LiverTox NBK548754, the ATS statement (PMID:17021358), and StatPearls NBK531488:

- **Age.** Hepatotoxicity runs approximately 0.5% at 20–35 years, 1.5% at 35–50, and 3% or higher above 50.
- **Female sex.** In a 140-patient AT-DILI cohort, "Female patients were significantly more likely to be diagnosed with grades 4-5 DILI than with grades 1-3 DILI (58.6% vs. 36.9%, p=0.036)" (PMID:32145061). Fatal outcomes disproportionately affect women and African Americans (LiverTox).
- **Chronic alcohol use**, **pre-existing cirrhosis**, **chronic hepatitis B or C**, **HIV coinfection**, **malnutrition**.
- **Concomitant rifampicin and pyrazinamide.** Co-administration is the single largest modifiable amplifier of hepatic risk.
- **Pregnancy and the first 3 months postpartum** — an explicit ALT-monitoring trigger in the ATS statement.
- For the **neuropathy** arm specifically, Steichen et al. list HIV, alcoholism, diabetes, renal impairment, nutritional deficiency, pregnancy, lactation, and co-prescribed neurotoxic drugs (PMID:16788441).
- **Cirrhosis** deserves its own line. A 2026 review frames the problem plainly: first-line agents "possess significant hepatotoxic potential and may precipitate hepatic decompensation," and treatment must be individualized by Child-Turcotte-Pugh or MELD score (PMID:42322387).

### 2.4 Protective factors

- **Rapid or intermediate NAT2 acetylation**, against the liver. Against the disease, it cuts the other way: in Azuma's randomized trial, standard dosing left rapid acetylators with early treatment failure in 38% of cases **[paraphrase-risk]** (PMID:23150149). Fast acetylation protects the liver and underdoses the tuberculosis.
- **Co-administered pyridoxine.** It prevents the neuropathy and it is the antidote in overdose. It does **not** prevent the hepatitis. These are separate mechanisms and pyridoxine touches only one of them.
- **Substituting a shorter rifamycin-based regimen.** In the Sterling trial, 3 months of weekly rifapentine plus isoniazid produced drug-related hepatotoxicity in 0.4% versus 2.7% for 9 months of daily isoniazid **[paraphrase-risk]** (PMID:22150035).
- **NAT2 genotype-guided dosing.** See §12.

### 2.5 Gene–environment interactions

Three are documented, and the third is the most interesting.

1. **NAT2 × rifampicin.** Slow acetylation and rifampicin co-administration compound; the toxic branch becomes much more active when both are present.
2. **NAT2 × CYP2E1 × alcohol.** Ethanol induces CYP2E1, which performs the oxidation step downstream of acetylation. The interaction is mechanistically obligatory and epidemiologically messy.
3. **NAT2 × ATP7B × copper.** Yoon et al. demonstrated it in cells, not just in a cohort (PMID:38424191, verbatim): "In vitro experiments using human liver-derived cell lines (HepG2 and SNU387 cells) revealed toxic synergism between INH and Cu, which were strongly augmented in cells with defective NAT2 and ATP7B activity, leading to increased mitochondrial reactive oxygen species generation, mitochondrial dysfunction, DNA damage, and apoptosis."

That is a gene–gene–micronutrient interaction with a cellular readout. It is the strongest new etiologic finding in this area since the HLA work.

---

## 3. Phenotypes

Frequencies below are drawn from LiverTox NBK548754 and StatPearls NBK531488 unless a PMID is given. Both are aggregated secondary sources; the underlying primary studies differ in their hepatotoxicity definitions, which the ATS statement names as the central obstacle to comparing them.

### 3.1 Hepatic

| Phenotype | HP term | Frequency | Onset | Course |
|---|---|---|---|---|
| Elevated ALT | `HP:0031964` Elevated circulating alanine aminotransferase concentration | 10–20% transient; >5× ULN in 3–5% | 2 wk – 6 mo | Often resolves on continued therapy |
| Elevated AST | `HP:0031956` Elevated circulating aspartate aminotransferase concentration | With ALT | 2 wk – 6 mo | As above |
| Drug-induced hepatitis | `HP:0012115` Hepatitis | Clinically apparent with jaundice in 0.5–1% | 2 wk – 6 mo | Progressive if drug continued |
| Jaundice | `HP:0000952` Jaundice | In the 0.5–1% symptomatic group | Follows prodrome | Resolves on withdrawal |
| Hyperbilirubinemia | `HP:0002904` Hyperbilirubinemia | With jaundice | — | — |
| Acute hepatic failure | `HP:0006554` Acute hepatic failure | ~10% of jaundiced cases | Weeks | Transplant or death |
| Nausea | `HP:0002018` Nausea | Prodromal, common | Precedes jaundice | Self-limited on withdrawal |
| Anorexia | `HP:0002039` Anorexia | Prodromal, common | Precedes jaundice | — |
| Vomiting | `HP:0002013` Vomiting | Common | — | — |
| Hepatomegaly | `HP:0002240` Hepatomegaly | Variable | — | — |
| Skin rash | `HP:0000988` Skin rash | Uncommon, mild | Early if present | — |
| Fever | `HP:0001945` Fever | Uncommon | Early if present | — |
| Eosinophilia | not confirmed in this session's cache | Uncommon | — | — |
| Antinuclear antibody positivity | `HP:0003493` Antinuclear antibody positivity | Occurs without liver injury | — | Low titre |

Latency, verbatim from LiverTox: *"The typical time to onset of injury ranges from 2 weeks to 6 months, but can be as long as one year and as short as one week."*

The hypersensitivity picture is deliberately understated in the primary source (LiverTox, verbatim): *"Features of hypersensitivity such as rash, fever and eosinophilia can occur, but are not common, and are usually mild if present at all."* This absence is exactly why the injury was classified as non-immune for forty years, and why Metushi's antibody work mattered.

### 3.2 Chronic neurological

| Phenotype | HP term | Frequency | Onset | Course |
|---|---|---|---|---|
| Peripheral neuropathy | `HP:0009830` Peripheral neuropathy | 1.1% general; 6.5% in older patients (StatPearls); dose-dependent | Months of therapy | Reversible with pyridoxine |
| Distal sensory impairment | `HP:0002936` Distal sensory impairment | With neuropathy | Months | Stocking-glove, ascending |
| Paresthesia | `HP:0003401` Paresthesia | With neuropathy | Months | "numbness, tingling, and a burning sensation in all the extremities" (StatPearls) |
| Optic neuritis | `HP:0100653` Optic neuritis | Rare | Months | Decreased acuity, eye pain, colour disturbance |
| Optic atrophy | `HP:0000648` Optic atrophy | Rare sequela | Late | May be permanent |
| Psychosis | `HP:0000709` Psychosis | 1–2% reported incidence (PMID:36875946) | Variable | Responds to pyridoxine |
| Sideroblastic anemia | `HP:0001924` Sideroblastic anemia | Rare | Months | B6-responsive |
| Systemic lupus erythematosus (drug-induced) | `HP:0002725` Systemic lupus erythematosus | Rare | Months | Resolves on withdrawal |

On psychosis, verbatim (PMID:36875946): *"Psychosis is one such rare adverse effect which has a reported incidence of 1%-2%."*

The neuropathy is a nutritional deprivation, not a poisoning. The nerve is starved of a cofactor. That is why it is preventable with a vitamin and why it recovers.

### 3.3 Acute overdose

| Phenotype | HP term | Frequency in overdose | Onset | Course |
|---|---|---|---|---|
| Seizure | `HP:0001250` Seizure | The defining feature | 30 min – 2 h | Refractory to standard anticonvulsants |
| Status epilepticus | `HP:0002133` Status epilepticus | Common in large ingestion | 30 min – 2 h | Terminated by pyridoxine |
| Metabolic acidosis | `HP:0001942` Metabolic acidosis | Near-universal | With seizures | Resolves with seizure control |
| Lactic acidosis | `HP:0003128` Lactic acidosis | With acidosis | With seizures | Secondary to convulsive muscle activity |
| Coma | `HP:0001259` Coma | Common | Hours | Reverses on pyridoxine |
| Encephalopathy | `HP:0001298` Encephalopathy | Post-ictal or anoxic | Hours | Anoxic injury may persist |
| Confusion | `HP:0001289` Confusion | Early | Minutes–hours | — |
| Ataxia | `HP:0001251` Ataxia | Early | Minutes–hours | — |
| Hyperglycemia | `HP:0003074` Hyperglycemia | Reported | — | — |
| Hyperkalemia | `HP:0002153` Hyperkalemia | Reported | — | — |
| Rhabdomyolysis | `HP:0003201` Rhabdomyolysis | With prolonged seizures | Hours | — |

Maw and Aitken state the syndrome in one line (PMID:17535059, verbatim): *"Isoniazid toxicity produces a triad of coma, metabolic acidosis and seizures. The seizures are often refractory to traditional antiepileptics."*

The acidosis is worth understanding correctly. StatPearls, verbatim: *"metabolic acidosis is associated with elevated lactate, likely secondary to muscle contraction from seizure activity."* It is a consequence of the convulsions, not a parallel poisoning. Stop the seizures and the lactate falls.

### 3.4 Quality of life

I found no isoniazid-specific EQ-5D, SF-36, or PROMIS data. That is a real gap, not an omission. The functional burdens that would be measured are: residual sensory neuropathy after recovery; anoxic cognitive sequelae after prolonged status epilepticus (StatPearls names "anoxic encephalopathy and dementia" as potential complications); and the downstream cost of interrupting tuberculosis treatment, which the ATS statement treats as the principal harm of over-cautious monitoring.

---

## 4. Genetic and Molecular Information

**There are no causal genes.** This is a drug toxicity, not a Mendelian disease. There is no pathogenic variant, no inheritance pattern for the disease itself, no somatic component, no chromosomal abnormality, and no carrier frequency to report. What exists is a set of germline susceptibility loci acting on a pharmacological insult.

### 4.1 Susceptibility genes

| Gene | HGNC | Locus | Role | Evidence |
|---|---|---|---|---|
| `NAT2` | `hgnc:7646` | 8p22 | Acetylates isoniazid; slow alleles → ~3× ATDH risk | PMID:42531284, 41657030, 39639188 |
| `CYP2E1` | `hgnc:2631` | — | Oxidizes acetylhydrazine/hydrazine to reactive species; also an autoantibody target | PMID:23775837, 41793109 |
| `ATP7B` | `hgnc:870` | — | Copper transport; rs1061472 832R/R amplifies NAT2 ultraslow risk | PMID:38424191 |
| `HLA-B` | `hgnc:4932` | 6p21 | `HLA-B*52:01` risk allele, OR 2.67 | PMID:33135175 |
| `GSTM1` | `hgnc:4632` | — | Null genotype, contested | PMID:41793109 |
| `GSTT1` | `hgnc:4641` | — | Null genotype, contested | PMID:41793109 |
| `CYP3A4` | `hgnc:2637` | — | Forms covalent INH adducts; autoantibody target | PMID:23775837 |
| `SOD2` | `hgnc:11180` | — | Mitochondrial superoxide dismutase; a candidate susceptibility axis in the mitochondrial-stress model | PMID:24783247 (framework only) |

`NAT2` full identifiers, verified live via the HGNC REST API: HGNC:7646, N-acetyltransferase 2, 8p22, OMIM 612182, Entrez 10, Ensembl ENSG00000156006, UniProt P11245, previous symbol AAC2.

Two further genes appear as **mechanistic targets**, not susceptibility loci. Do not model them as risk genes.

- `PDXK` (`hgnc:8819`), pyridoxal kinase — the enzyme isoniazid metabolites inhibit.
- `GAD1` (`hgnc:4092`), glutamate decarboxylase — the PLP-dependent enzyme that fails downstream.

### 4.2 Variant classification and nomenclature

`NAT2` is characterized by star-allele haplotypes, not by ACMG/AMP pathogenicity tiers. `NAT2*4` is the reference rapid allele; `NAT2*5`, `*6`, and `*7` haplotype families define slow acetylation. Star-allele nomenclature **transitioned to PharmVar in March 2024**, and ClinPGx (formerly PharmGKB) and CPIC now use the PharmVar naming. Anything written before that date may use superseded haplotype names. I did not pull gnomAD haplotype frequencies directly.

**CPIC has published a NAT2 guideline — for hydralazine, not isoniazid** (PMID:40974042, *Clin Pharmacol Ther* 2025;118(6):1430-1436). There is, as of my searches, **no CPIC guideline for NAT2 and isoniazid**. Do not cite one.

Reported slow-acetylator frequencies vary enormously by population **[paraphrase-risk, from a search-result synthesis I did not trace to the primary study]**: ultra-slow acetylator frequencies of roughly 29–54% in European, African, and South East Asian groups, against 4.75% in Japanese and 11.11% in East Asian populations, with Indian studies spanning 4% to 62%. Treat these as an order-of-magnitude claim and re-source them before curation.

### 4.3 Epigenetics

Epigenetic modification of drug-metabolizing enzyme expression is reviewed as a susceptibility axis in PMID:41793109. No quantified isoniazid-specific methylation or histone finding is available. This is an open area, not an established one.

---

## 5. Environmental Information

The environmental factor **is the drug**. This entry's exposure is pharmaceutical, which makes ECTO the natural binding ontology; I did not find an `exposure to isoniazid` term in the local ECTO cache and did not confirm one exists.

**Chemical entities**

| Compound | CHEBI | Note |
|---|---|---|
| Isoniazid | `CHEBI:6030` | Canonical label is **"isoniazide"** |
| Rifampicin | `CHEBI:28077` | Co-administered amplifier |
| Hydrazine | `CHEBI:15571` | Hydrolysis metabolite, hepatotoxic |
| Acetylhydrazine | no exact CHEBI term; closest is `CHEBI:2422` **acetohydrazide** | Same compound, different name; verify before binding |
| Pyridoxine | `CHEBI:16709` | The antidote |
| Pyridoxal 5′-phosphate | `CHEBI:18405` | The depleted cofactor |
| GABA | `CHEBI:16865` | The depleted neurotransmitter |

**Lifestyle factors.** Chronic alcohol consumption, through CYP2E1 induction and through nutritional depletion. Malnutrition, which worsens both arms. Dietary copper exposure now has a mechanistic claim attached to it (PMID:38424191), though no dietary-intake study exists.

**Infectious agents.** *Mycobacterium tuberculosis* is the indication, not the cause. Three infections act as risk modifiers: hepatitis B virus, hepatitis C virus, and HIV. The ATS statement singles out HIV for mandatory ALT monitoring during treatment of TB disease.

---

## 6. Mechanism and Pathophysiology

### 6.1 Chain A — hepatic injury

The chemistry of the first step is genuinely disputed, and the field has changed its mind. I present the branch rather than hiding it.

1. Oral isoniazid is absorbed and reaches the hepatocyte (`CL:0000182`) in the liver (`UBERON:0002107`). Peak serum concentration occurs within 2 hours of a 300 mg dose, at 3–5 µg/mL (StatPearls).
2. **Branch point.** Two competing accounts of bioactivation:
   - **2a — the acetylhydrazine model (superseded).** NAT2 (`GO:0004060` arylamine N-acetyltransferase activity) acetylates isoniazid to acetyl-isoniazid, which is hydrolysed to acetylhydrazine. CYP2E1 (`GO:0004497` monooxygenase activity) oxidizes acetylhydrazine to N-hydroxy-acetylhydrazine, which dehydrates to acetyl diazene. Slow acetylation was originally expected to matter because it shunts more drug down the amidase route to free hydrazine (`CHEBI:15571`).
   - **2b — the direct-bioactivation model (current).** Isoniazid itself is bioactivated to a reactive metabolite. Metushi, Uetrecht and Phillips, verbatim: *"INH itself is directly bioactivated to a reactive metabolite, which in some patients leads to an immune response and liver injury"* (PMID:26773235).
3. The reactive species forms **covalent protein adducts**. This is demonstrated, not inferred: *"INH was found to form covalent adducts with CYP2E1, CYP3A4, and CYP2C9"* (PMID:23775837, verbatim).
4. **The chain now forks into two arms that both run.**

**Arm A1 — mitochondrial injury (leads to hepatocyte death).**

5. Isoniazid and/or hydrazine impair mitochondrial function (`GO:0005739` mitochondrion). Boelsterli and Lee, verbatim: *"INH and/or INH metabolites (e.g. hydrazine) can cause mitochondrial injury, which can lead to mitochondrial oxidant stress and impairment of energy homeostasis."*
6. Underlying complex I impairment converts a tolerable dose into a lethal one. Verbatim: *"underlying impairment of complex I function can trigger massive hepatocellular injury induced by otherwise nontoxic concentrations of INH superimposed on these mitochondrial deficiencies"* (PMID:24783247). This is the two-hit structure of the whole hepatic arm.
7. Reactive oxygen species accumulate (`GO:0006979` response to oxidative stress; `GO:0034599` cellular response to oxidative stress), glutathione is consumed (`GO:0006749` glutathione metabolic process), and DNA damage follows. In the NAT2/ATP7B copper-synergy cells this sequence is measured directly (PMID:38424191).
8. Hepatocyte apoptosis (`GO:0097284` hepatocyte apoptotic process; `GO:0006915` apoptotic process) → transaminase release → the clinical hepatitis.

**Arm A2 — immune amplification (leads to the severe phenotype).**

5′. Adducted proteins act as haptens. Innate signalling through TLR4 and adaptive HLA-restricted presentation are both proposed, under what the 2026 review calls a dual-hit framing (PMID:41793109).
6′. An adaptive response develops. Metushi et al. found antibodies in 15 of 19 cases of isoniazid-induced liver failure — 8 anti-INH, 11 anti-CYP2E1, 14 anti-INH-modified-CYP2E1, 14 anti-CYP3A4, 10 anti-CYP2C9 — and *"None of these Abs were detected in sera from INH-treated controls without significant liver injury"* (PMID:23775837, verbatim). Their conclusion, verbatim: *"These data provide strong evidence that INH induces an immune response that causes INH-induced liver injury."*
7′. The dominant subclass is IgG3, which fixes complement and marks a Th1 response **[paraphrase-risk]** (PMID:24786179).
8′. Inflammation (`GO:0006954` inflammatory response) amplifies the hepatocyte death from Arm A1 into acute liver failure.

**The branch has a clinical consequence, and it is the important one.** Verbatim, PMID:26773235: *"Most cases involve mild liver injury, which resolves with immune tolerance, while other cases appear to have a more severe phenotype that is associated with the production of anti-drug/anti-CYP P450 antibodies and can progress to liver failure."* Transaminase elevation that resolves on continued treatment is not a paradox to be explained away. It is immune tolerance developing, and it is the expected outcome in most patients.

### 6.2 Chain B — acute overdose neurotoxicity

This chain is short, fast, and completely separate from Chain A.

1. A large ingestion (>20 mg/kg; reliably convulsant at 80–150 mg/kg) delivers isoniazid to the central nervous system (`UBERON:0001017`, `UBERON:0000955` brain).
2. Isoniazid metabolites **inhibit pyridoxal kinase** (`GO:0008478` pyridoxal kinase activity; gene `PDXK`, `hgnc:8819`), blocking conversion of pyridoxine to its active form.
3. In parallel, isoniazid — a hydrazide — **condenses directly with pyridoxal phosphate to form an inactive hydrazone**, which is renally cleared. Two mechanisms, one deficit.
4. Pyridoxal 5′-phosphate (`CHEBI:18405`) falls. This is a **functional** vitamin B6 deficiency: total-body B6 need not be low, and the deficit appears within hours.
5. Glutamate decarboxylase (`GO:0004351` glutamate decarboxylase activity; `GAD1`, `hgnc:4092`) is a PLP-dependent enzyme and loses its cofactor.
6. GABA synthesis fails (`GO:0009449` GABA biosynthetic process; note the canonical GO label is **"GABA biosynthetic process"**, not the spelled-out form). GABA (`CHEBI:16865`) falls in GABAergic neurons (`CL:0000617`).
7. Inhibitory tone collapses against unchanged glutamatergic drive. StatPearls: *"This functional depletion of pyridoxine causes a disruption of glutamate and GABA homeostasis and leads to an excessive excitatory milieu in the brain."*
8. Seizures (`HP:0001250`), often status epilepticus (`HP:0002133`), refractory to standard anticonvulsants — because the lesion is upstream of the GABA-A receptor and benzodiazepines have no substrate to potentiate.
9. Convulsive muscle activity generates lactate → anion-gap metabolic acidosis (`HP:0001942`, `HP:0003128`). **This step is a consequence of step 8, not a parallel toxicity.**
10. Coma (`HP:0001259`), and if seizures persist, anoxic encephalopathy.

**Step 4 is where the antidote acts, and that is why the antidote works in minutes.** Supplying pyridoxine restores the substrate for whatever pyridoxal kinase activity remains and reverses steps 5 through 10.

### 6.3 Chain C — chronic peripheral neuropathy

Same lesion as Chain B, different tempo, different tissue.

1. Months of therapeutic dosing produce sustained low-grade PLP depletion by the same two mechanisms (kinase inhibition plus hydrazone formation).
2. PLP-dependent metabolism fails in the peripheral nervous system (`UBERON:0000010`), in long axons and their Schwann cells (`CL:0002573`; `GO:0042552` myelination). **This step is mechanistically inferred rather than demonstrated in human tissue** — the human evidence is clinical and therapeutic, not histological.
3. Distal axonopathy in a length-dependent, stocking-glove distribution, ascending proximally.
4. Sensory symptoms first: paresthesia (`HP:0003401`), burning, distal sensory impairment (`HP:0002936`). Motor involvement is later and less common.
5. In the optic nerve (`UBERON:0000941`, canonical label **"cranial nerve II"**), the same deprivation produces optic neuritis (`HP:0100653`) and, rarely, optic atrophy (`HP:0000648`).
6. Reversal on pyridoxine supplementation. Steichen et al., **[paraphrase-risk]**: *"Pyridoxine is preventative in low dosage and curative in high dosage"* (PMID:16788441).

### 6.4 Molecular profiling and advanced technologies

I found no isoniazid-toxicity single-cell atlas, no spatial transcriptomics, no human multi-omics integration, and no CRISPR screen. The available omics is rodent and cell-line: transcriptional readouts of NLRP3 inflammasome activation and Nrf2 suppression in Sprague-Dawley rats (PMID:41587410), and mitochondrial-ROS and apoptosis readouts in HepG2 and SNU387 (PMID:38424191). Recording this absence honestly is better than dressing up the rodent data.

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: liver (`UBERON:0002107`). Primary and independent: central nervous system (`UBERON:0001017`), brain (`UBERON:0000955`), peripheral nervous system (`UBERON:0000010`), and cranial nerve II (`UBERON:0000941`). Secondary: skeletal muscle in convulsive rhabdomyolysis; kidney, only through myoglobin load. Body systems: hepatobiliary, central nervous, peripheral nervous, visual, haematopoietic (sideroblastic anemia).

**Tissue and cell level.** Hepatocyte (`CL:0000182`) is the target cell of Chain A. Kupffer cell (`CL:0000091`) and T cell (`CL:0000084`) participate in Arm A2; both assignments are inferred from the innate/adaptive framing in PMID:41793109 rather than demonstrated in isoniazid-injured human liver. Hepatic stellate cell (`CL:0000632`) appears in the rodent fibrosis readout (PMID:41587410), not in the human injury. GABAergic neuron (`CL:0000617`) is the target of Chain B. Schwann cell (`CL:0002573`) and the peripheral sensory neuron (`CL:0000540`) are the targets of Chain C.

**Subcellular level.** Mitochondrion (`GO:0005739`) is the central compartment of Arm A1, specifically respiratory complex I. Cytosol for the PLP-dependent decarboxylation of Chain B. Endoplasmic reticulum for CYP2E1/CYP3A4 adduct formation.

**Lateralization.** Bilateral and symmetric throughout. The neuropathy is length-dependent and symmetric; asymmetry should prompt a different diagnosis.

---

## 8. Temporal Development

| Arm | Onset | Pattern | Progression | Duration |
|---|---|---|---|---|
| Hepatic | 2 weeks – 6 months; range 1 week – 1 year | Insidious, prodromal | Asymptomatic elevation → symptomatic hepatitis → jaundice → failure | Self-limited on withdrawal; ~10% of jaundiced cases progress |
| Neuropathy | Months of therapy | Insidious | Ascending, length-dependent | Reversible over months |
| Overdose | 30 minutes – 2 hours | Acute, abrupt | Seizure → status → acidosis → coma | Minutes to reverse with antidote |

**The critical windows.** For the liver, LiverTox: *"Most frequently, the injury is self-limited and begins to resolve within a week of stopping isoniazid."* The intervention window is the interval between the first symptom and jaundice, which is why symptom education outperforms scheduled bloodwork. For overdose, the window is the first hour, and the limiting factor is whether the hospital has enough pyridoxine on the shelf — which is the specific question Maw and Aitken surveyed every accredited Australian emergency department about (PMID:17535059).

**Remission.** Treatment-induced in every arm. Rechallenge succeeds in up to 80% of cases in prospective studies (LiverTox), which is itself an argument for tolerance rather than sensitization in the common phenotype. But rechallenge is also an independent risk factor for severe injury in the AT-DILI cohort (PMID:32145061). Both are true. Rechallenge is usually fine and occasionally catastrophic.

---

## 9. Inheritance and Population

**Exposure denominator.** WHO's Global Tuberculosis Report 2025 records that in 2024, **5.3 million people at high risk were provided TB preventive treatment** — 3.5 million close contacts and 1.8 million others — up from 4.7 million in 2023. Add the population under treatment for TB disease. The exposed denominator is in the tens of millions annually and the toxicity is a rate applied to that.

**Hepatic incidence.**

| Measure | Rate | Source |
|---|---|---|
| Transient ALT elevation | 10–20% | LiverTox |
| ALT >5× ULN | 3–5% | LiverTox |
| Clinically apparent injury with jaundice | 0.5–1% | LiverTox |
| Fatal hepatitis | 0.05–0.1% | LiverTox |
| Hepatotoxicity, monitored LTBI cohort | **0.10% of 11,141 starting; 0.15% of those completing** | PMID:10086436 |
| Drug-related hepatotoxicity, 9 months daily INH, trial setting | 2.7% | PMID:22150035 |
| Drug-related hepatotoxicity, 3 months weekly rifapentine + INH | 0.4% | PMID:22150035 |

The Nolan cohort is the number to lead with for monitored preventive therapy, verbatim: *"Eleven patients (0.10% of those starting, and 0.15% of those completing treatment) had hepatotoxic reactions to isoniazid during preventive treatment."* Their conclusion was that the rate *"was lower than has been reported previously"* and that clinicians should have greater confidence in the regimen's safety. Note the 27-fold spread between that number and the Sterling trial's 2.7% — regimen, duration, and hepatotoxicity definition differ, and the ATS statement names exactly that heterogeneity as the reason the literature does not reconcile.

**Acute poisoning incidence.** StatPearls reports **54 cases reported to US poison control centers in 2020**. I did not open the 2023 or 2024 National Poison Data System annual reports (PMID:39688840, PMID:41432769) to extract isoniazid-specific counts, so I cannot give a current figure.

**Inheritance.** Not applicable to the disease. The susceptibility alleles segregate as ordinary autosomal codominant pharmacogenetic haplotypes: `NAT2` slow acetylation requires two slow alleles, so slow-acetylator status is inherited as an autosomal recessive trait. Penetrance of the *toxicity* is very low even in slow acetylators — an OR of 3 against a baseline of ~1% means most slow acetylators tolerate the drug.

**Demographics.** Risk rises monotonically with age above 35. Women appear over-represented in severe injury and in fatalities. Slow-acetylator frequency varies several-fold between populations, which means the population-attributable fraction of the NAT2 effect is itself population-specific. Sex ratio of the *toxicity* is not cleanly separable from the sex ratio of TB treatment.

---

## 10. Diagnostics

**Laboratory.** ALT and AST (`HP:0031964`, `HP:0031956`), total and direct bilirubin, alkaline phosphatase, INR, albumin, complete blood count, basic metabolic panel with anion gap, creatine kinase, and serum lactate. StatPearls describes the chronic pattern as *"marked alanine aminotransferase and aspartate aminotransferase elevations (greater than 10 times the upper limit of normal)"* with alkaline phosphatase usually under 2× ULN. LiverTox gives worked R values of 45.9 and 8.1 — both hepatocellular.

**Hy's law** (ALT >3× ULN with total bilirubin >2× ULN and no cholestasis) is the severity discriminator, and it was elevated in the severe stratum of the AT-DILI cohort (PMID:32145061).

**Biomarkers.** No validated isoniazid-specific biomarker exists. ALT is the operational one. Antinuclear antibodies may appear without injury and are not diagnostic. The anti-INH and anti-CYP antibody panel from PMID:23775837 discriminated liver-failure cases from tolerant controls perfectly in a 19-case series and is the most promising research assay, but it is not clinically available.

**Imaging.** No diagnostic role. Ultrasound is used to exclude biliary obstruction.

**Electrophysiology.** Nerve conduction studies confirm a length-dependent axonal sensory polyneuropathy in the chronic arm. EEG in overdose shows generalized epileptiform activity; it does not distinguish aetiology.

**Biopsy.** Rarely required. When performed, hepatocellular necrosis without prominent eosinophilia or granulomas. No pathognomonic finding.

**Genetic testing.** `NAT2` genotyping or acetylator phenotyping. This is the one genetic test with a randomized trial behind it (§12). Panels typically assay the `NAT2*5`, `*6`, `*7`, and `*14` defining SNPs. Whole exome and whole genome sequencing have no established role. Chromosomal microarray, karyotype, FISH, mitochondrial DNA testing, and repeat-expansion testing are all **not applicable**.

**Clinical criteria.** No consensus diagnostic criteria exist for isoniazid toxicity as such. The operative thresholds come from the ATS statement (PMID:17021358, verbatim): *"Treatment should be interrupted and, generally, a modified or alternative regimen used for those with ALT elevation more than three times the upper limit of normal (ULN) in the presence of hepatitis symptoms and/or jaundice, or five times the ULN in the absence of symptoms."* Causality is usually assessed with RUCAM.

**Differential diagnosis.** From StatPearls, and it is a good list:

- *Acute presentation:* undiagnosed seizure disorder, metabolic derangement, intracranial hemorrhage, ethanol or sedative withdrawal, sympathomimetic toxicity, and **hydrazine or gyromitrin mushroom toxicity** — which shares the exact mechanism and the exact antidote.
- *Jaundice:* viral hepatitis, obstructive jaundice, hemolysis, other DILI (including the co-administered rifampicin and pyrazinamide).
- *Neuropathy:* alcoholic and diabetic neuropathy.
- *Optic neuritis:* ethambutol toxicity — which matters, because ethambutol is in the same regimen — plus autoimmune disease and multiple sclerosis.

**Screening.** ALT monitoring, not population screening. The ATS statement targets it: during LTBI treatment, monitor those who chronically consume alcohol, take concomitant hepatotoxic drugs, have viral hepatitis or other pre-existing liver disease or abnormal baseline ALT, have had prior isoniazid hepatitis, or are pregnant or within 3 months postpartum. During treatment of TB disease, add everyone with HIV. Some experts add everyone over 35.

---

## 11. Outcome and Prognosis

**Acute overdose.** Good with the antidote, and the antidote is the whole prognosis. StatPearls: *"rapid treatment with pyridoxine leads to the resolution of seizures, coma, and metabolic acidosis."* Against that, the EXTRIP systematic review found **12.5% mortality among 40 patients with clinical data available** **[paraphrase-risk]** (PMID:33660266). Both statements are compatible: outcome is excellent when adequate pyridoxine is given promptly and poor when it is not.

**Hepatic injury.** Most cases resolve within a week of stopping the drug. Roughly 10% of jaundiced cases progress to acute liver failure requiring emergency transplantation or ending in death (LiverTox). LiverTox is blunt about the aggregate burden, verbatim: *"Even with monitoring, isoniazid remains a major cause of acute liver failure due to idiosyncratic reactions, and is associated with several instances of acute liver failure and death or emergency liver transplantation in the United States each year."* Case-fatality for clinically apparent hepatitis is 0.05–0.1% of all recipients.

**Neuropathy and optic neuritis.** Usually reversible with pyridoxine and drug adjustment. StatPearls notes that *"some patients"* retain residual sensory neuropathy.

**Prognostic factors.** Age over 50. Female sex. Jaundice at presentation (Hy's law). Rising INR. Continued dosing after symptom onset — the single most modifiable factor. Multidrug regimens and re-challenge (PMID:32145061). Pre-existing cirrhosis, where decompensation rather than transaminitis is the endpoint (PMID:42322387). For overdose: time to adequate pyridoxine, and duration of status epilepticus.

**Morbidity and disability.** Anoxic encephalopathy and dementia after prolonged status epilepticus. Residual sensory neuropathy. Post-transplant morbidity in survivors of acute liver failure. No isoniazid-specific disability or quality-of-life instrument data was found.

---

## 12. Treatment

### 12.1 Acute overdose

**Pyridoxine is the antidote and there is no substitute for it.** Dosing, verbatim from StatPearls: *"If the amount of INH ingested is known, pyridoxine should be given at a gram-for-gram equivalent dose. If the amount of INH is unknown, a 70 mg/kg dose up to a maximum of 5 g is recommended."* A second dose may be given if seizures persist. *"Rapid resolution of seizure and coma is expected with pyridoxine administration."*

- `treatment_term`: `NCIT:C15986` Pharmacotherapy; `therapeutic_agent`: `CHEBI:16709` pyridoxine, or `NCIT:C62619` Pyridoxine / `NCIT:C48030` Pyridoxine Hydrochloride.
- **Oral pyridoxine works when intravenous is unavailable.** A Sri Lankan case gave 4.2 g by nasogastric tube, matching the ingested isoniazid dose, and concluded that *"oral pyridoxine can substitute for intravenous pyridoxine with almost similar efficacy at a low cost"* in resource-limited settings **[paraphrase-risk]** (PMID:28789699). One case is one case. But intravenous pyridoxine stock-outs are the recurring practical failure in this poisoning, and this is the recorded workaround.

**Benzodiazepines** are adjunctive and act synergistically at the GABA-A receptor, but they cannot substitute for restoring the substrate. `NCIT:C15986` Pharmacotherapy.

**Activated charcoal** (`NCIT:C77524`) for early presentation with a protected airway.

**Extracorporeal treatment is not recommended.** The EXTRIP workgroup, verbatim: *"The EXTRIP workgroup suggests against performing ECTR in addition to standard care (weak recommendation, very low quality of evidence)"* (PMID:33660266). Isoniazid is moderately dialyzable, and that is not the point — patients receiving supportive care with adequately dosed pyridoxine do well without it, and dialysis removes pyridoxine too. The single exception the workgroup allows: when standard pyridoxine is unavailable and seizures resist GABA-A agonists. `NCIT:C15248` Hemodialysis.

**Supportive care** — airway, ventilation, correction of acidosis after seizure control. `NCIT:C15747` Supportive Care.

### 12.2 Hepatotoxicity

**Stop the drug.** LiverTox, verbatim: *"Isoniazid should be discontinued for any confirmed elevation of ALT above 5 times the ULN or above 3 times ULN in the presence of symptoms."*

**Sequential reintroduction** once enzymes normalize: *"the potential hepatotoxic drugs can be restarted one at a time with careful monitoring"* (StatPearls).

**Corticosteroids** are often used with, in LiverTox's words, *"scant evidence for their benefit."* Do not present them as standard care.

**Liver transplantation** (`NCIT:C15271`) for acute liver failure.

**No specific pharmacotherapy exists.** Preclinical hepatoprotectants — isoliquiritigenin acting through Nrf2 activation and NLRP3 inhibition — are rat-stage only (PMID:41587410).

### 12.3 Neuropathy and optic neuritis

Pyridoxine supplementation, plus dose reduction. Steichen et al. suggest checking acetylator status and considering isoniazid at 3 mg/kg/day or less in slow acetylators **[paraphrase-risk]** (PMID:16788441).

### 12.4 Pharmacogenomics — the one place genotype changes the dose

`NAT2` genotype-guided dosing has randomized evidence behind it. Azuma et al. randomized 172 Japanese patients with newly diagnosed pulmonary TB to conventional ~5 mg/kg dosing versus acetylator-adjusted dosing **[paraphrase-risk on the quoted figures]** (PMID:23150149):

> "INH-DILI occurred in 78 % of the slow acetylators in the STD-treatment, while none of the slow acetylators in the PGx-treatment experienced either INH-DILI or early treatment failure."

Rapid acetylators, meanwhile, went from 38% early treatment failure to 15.0%. The intervention improves both ends of the distribution — it is not a safety-versus-efficacy trade.

A later monotherapy pilot in healthy volunteers gave slow acetylators 200 mg instead of 300 mg and found *"a more stable serum liver enzyme profile and a lower incidence of adverse drug reactions"*, with adverse-reaction rates of 12.5%, 60%, and 33.3% in the rapid-reference, slow-standard-dose, and slow-reduced-dose groups **[paraphrase-risk]** (PMID:33165168).

**Caveat that must travel with this.** There is no CPIC guideline for NAT2 and isoniazid. The 2025 CPIC NAT2 guideline covers hydralazine (PMID:40974042). Genotype-guided isoniazid dosing is evidence-supported and not guideline-endorsed. Those are different claims.

### 12.5 Regimen substitution as toxicity avoidance

The most effective treatment for isoniazid hepatotoxicity is a shorter regimen. Sterling et al., **[paraphrase-risk]**: 3 months of weekly rifapentine plus isoniazid was non-inferior for TB prevention (0.19% vs 0.43%), completed more often (82.1% vs 69.0%), and produced drug-related hepatotoxicity in 0.4% versus 2.7% (PMID:22150035).

### 12.6 Not applicable

Gene therapy, cell therapy, RNA-based therapy, targeted therapy, immunotherapy, and surgery — none apply, other than transplantation as salvage.

---

## 13. Prevention

**Primary.**
- **Pyridoxine co-prescription** at 10–25 mg daily for patients at neuropathy risk: HIV infection, diabetes, alcoholism, renal failure, malnutrition, pregnancy, lactation, and adolescents. This prevents Chains B and C. It does **not** prevent Chain A, and asserting otherwise is a common and consequential error.
- **Patient and regimen selection**, which the ATS statement puts first among its recommendations, *"to optimize benefits over risks."*
- **Regimen substitution** to 3HP or another rifamycin-based short course.
- **NAT2-guided dosing** where genotyping is available.
- **Child-resistant packaging and dosing education.** StatPearls names accidental pediatric overdose explicitly.
- **Adequate pyridoxine stocking in emergency departments.** This is a public-health intervention, not a clinical one, and it was the entire point of the Australian hospital survey in PMID:17535059.

**Secondary.** Targeted ALT monitoring per the ATS risk list (§10), at roughly monthly intervals in high-risk patients. Symptom education — teaching patients to stop the drug and call at the first nausea, anorexia, or dark urine — outperforms scheduled bloodwork, because the injury can develop between visits.

**Tertiary.** Prompt withdrawal at threshold. Cautious sequential rechallenge only in mild cases. Avoidance of concurrent hepatotoxins and alcohol.

**Immunization.** Not applicable to the toxicity. BCG affects TB incidence and therefore exposure to isoniazid, which is a distinct and indirect claim.

**Genetic counseling.** Not applicable in the Mendelian sense. `NAT2` acetylator status is a pharmacogenetic result, and cascade testing of relatives has no established value.

**Public health.** The whole risk profile is a function of how many people take the drug and for how long. Shortening TB preventive treatment is a toxicity-prevention measure at population scale.

---

## 14. Other Species and Natural Disease

**There is no natural disease.** Isoniazid toxicity does not occur spontaneously in any species. It occurs where the compound is administered, and in veterinary practice that is almost entirely **malicious or accidental canine poisoning** — isoniazid is a well-recognized dog-baiting agent, and dogs present with the same refractory-seizure and acidosis picture. I did not retrieve a primary veterinary source for that claim in this session, so treat it as unverified background rather than a citable fact.

**Species used experimentally:** *Rattus norvegicus* (`NCBITaxon:10116`), *Mus musculus* (`NCBITaxon:10090`), *Oryctolagus cuniculus* (`NCBITaxon:9986`), *Canis lupus familiaris* (`NCBITaxon:9615`) as a poisoning presentation. Human is `NCBITaxon:9606`.

**Orthology carries a trap.** The murine and human N-acetyltransferase gene names are **not** aligned by number: the mouse gene called *Nat2* is the ortholog of human `NAT1`, and mouse *Nat1* corresponds functionally to human `NAT2`. I did not re-verify this against the Alliance of Genome Resources in this session, and it should be checked before any cross-species annotation. A curator who maps "mouse Nat2" onto "human NAT2" by name will invert the whole pharmacogenetics.

**Comparative pathology.** Rodents do not reproduce human idiosyncratic isoniazid DILI. They reproduce dose-dependent oxidative hepatocellular injury, which is a different thing. The rat model in PMID:41587410 uses 50 mg/kg orally to produce transaminase elevation, lipid peroxidation, NLRP3 activation, steatosis, and fibrosis — mechanistically informative, and not a model of the human idiosyncratic reaction. Boelsterli and Lee's framing explains why: the human event needs a susceptibility hit that healthy inbred rodents do not carry.

**No zoonotic component.** Not transmissible.

---

## 15. Model Organisms

| System | Type | What it models | Fidelity | Limitation | Source |
|---|---|---|---|---|---|
| Sprague-Dawley rat, INH 50 mg/kg p.o. | Mammalian in vivo | Dose-dependent oxidative hepatocellular injury, NLRP3 inflammasome activation, Nrf2 suppression, ferroptosis, steatosis, fibrosis | Moderate for the intrinsic-toxicity arm | Does not reproduce human idiosyncrasy; no NAT2 polymorphism equivalent | PMID:41587410 |
| HepG2 and SNU387 cells | In vitro, human-derived | INH × copper synergy; mitochondrial ROS, mitochondrial dysfunction, DNA damage, apoptosis under defective NAT2/ATP7B | Good for the specific gene interaction | Immortalized lines, supraphysiological exposure, no immune compartment | PMID:38424191 |
| Mitochondrial-deficiency models (complex I impairment as a sensitizing background) | Mammalian in vivo, conceptual framework | The two-hit structure: underlying mitochondrial deficit converts a nontoxic INH concentration into massive hepatocellular injury | The most explanatory framework available | I did **not** confirm the specific published model (e.g. an Sod2 heterozygous mouse) in this session; the framework is from the review | PMID:24783247 |
| Human patient sera, Acute Liver Failure Study Group | Human, ex vivo | Anti-INH and anti-CYP2E1/3A4/2C9 antibody response in liver failure | Highest — this is the human disease | 19 cases; no animal correlate exists | PMID:23775837 |

**What no model captures.** The idiosyncrasy itself. Every animal model produces injury by dosing hard enough; the human disease appears in 0.5–1% of people taking an ordinary dose. Boelsterli and Lee close their review on exactly this point, verbatim: *"points to the existing large gaps in our understanding of the pathogenesis."*

**Resources.** MGI, RGD, Alliance of Genome Resources, Cellosaurus for HepG2 and SNU387. I did not query any of them directly.

---

## Ontology Term Register

Every identifier below was resolved either against this repository's committed term caches or live against OLS4 / the HGNC REST API during this session. Labels are the canonical ontology labels, which in four cases differ from the name a curator would guess.

**Watch these four.** `CHEBI:6030` is labelled **"isoniazide"**. `GO:0009449` is labelled **"GABA biosynthetic process"**. `UBERON:0000941` is labelled **"cranial nerve II"**. There is no CHEBI term labelled "acetylhydrazine"; the compound is `CHEBI:2422` **"acetohydrazide"**, and I did not confirm CHEBI treats it as the same entity.

| Domain | Terms |
|---|---|
| Disease | `MONDO:0027677` isoniazid toxicity |
| Phenotype | `HP:0031964`, `HP:0031956`, `HP:0012115`, `HP:0000952`, `HP:0002904`, `HP:0006554`, `HP:0001399`, `HP:0002240`, `HP:0002018`, `HP:0002013`, `HP:0002039`, `HP:0000988`, `HP:0001945`, `HP:0003493`, `HP:0009830`, `HP:0002936`, `HP:0003401`, `HP:0100653`, `HP:0000648`, `HP:0000709`, `HP:0001924`, `HP:0002725`, `HP:0001250`, `HP:0002133`, `HP:0001942`, `HP:0003128`, `HP:0001259`, `HP:0001298`, `HP:0001289`, `HP:0001251`, `HP:0003074`, `HP:0002153`, `HP:0003201`, `HP:0001873`, `HP:0001903` |
| Biological process / function | `GO:0004060`, `GO:0004497`, `GO:0006805`, `GO:0008478`, `GO:0004351`, `GO:0009449`, `GO:0042816`, `GO:0006979`, `GO:0034599`, `GO:0006749`, `GO:0097284`, `GO:0006915`, `GO:0006954`, `GO:0042552`, `GO:0005739` |
| Cell type | `CL:0000182`, `CL:0000091`, `CL:0000632`, `CL:0000084`, `CL:0000617`, `CL:0002573`, `CL:0000540` |
| Anatomy | `UBERON:0002107`, `UBERON:0000955`, `UBERON:0001017`, `UBERON:0000010`, `UBERON:0000941` |
| Chemical | `CHEBI:6030`, `CHEBI:15571`, `CHEBI:2422`, `CHEBI:16709`, `CHEBI:18405`, `CHEBI:16865`, `CHEBI:28077` |
| Gene | `hgnc:7646` NAT2, `hgnc:2631` CYP2E1, `hgnc:2637` CYP3A4, `hgnc:870` ATP7B, `hgnc:4932` HLA-B, `hgnc:4632` GSTM1, `hgnc:4641` GSTT1, `hgnc:11180` SOD2, `hgnc:8819` PDXK, `hgnc:4092` GAD1 |
| Treatment | `NCIT:C15986` Pharmacotherapy, `NCIT:C62619` Pyridoxine, `NCIT:C48030` Pyridoxine Hydrochloride, `NCIT:C77524` Activated Charcoal, `NCIT:C15248` Hemodialysis, `NCIT:C15271` Liver Transplantation, `NCIT:C15747` Supportive Care, `NCIT:C49236` Therapeutic Procedure |

---

## What I Did Not Verify

Stated as fact, because it is fact.

- I did not open the Orphanet record for `ORPHA:240887`. The site returned a bot-check page. The cross-reference from Mondo is verified; the Orphanet label and content are not.
- I did not read OMIM directly. It returned HTTP 403. The `NAT2` OMIM number 612182 comes from the HGNC REST record, not from OMIM.
- I did not extract isoniazid-specific counts from the 2023 or 2024 National Poison Data System annual reports.
- I did not pull gnomAD allele frequencies for `NAT2` haplotypes. The population frequency figures in §4.2 came through a search synthesis and should be re-sourced.
- I did not confirm the specific published mitochondrial-sensitization mouse model behind the complex I two-hit finding.
- I did not confirm the mouse/human `Nat1`/`Nat2` nomenclature inversion against the Alliance of Genome Resources.
- I did not find any isoniazid-specific quality-of-life instrument data, single-cell dataset, spatial transcriptomics dataset, or CRISPR screen. I believe none exist; I did not exhaustively establish that.
- Quotes marked **[paraphrase-risk]** came back through a summarizing fetch rather than the raw PubMed record. Verify them against the source before putting them in an evidence `snippet`.

---

## Sources

- [ATS statement: hepatotoxicity of antituberculosis therapy (PMID:17021358)](https://pubmed.ncbi.nlm.nih.gov/17021358/)
- [Nolan et al., Hepatotoxicity associated with isoniazid preventive therapy, JAMA 1999 (PMID:10086436)](https://pubmed.ncbi.nlm.nih.gov/10086436/)
- [Boelsterli & Lee, Mechanisms of isoniazid-induced idiosyncratic liver injury (PMID:24783247)](https://pubmed.ncbi.nlm.nih.gov/24783247/)
- [Metushi et al., Anti-isoniazid and anti-CYP antibodies in liver failure, Hepatology 2014 (PMID:23775837)](https://pubmed.ncbi.nlm.nih.gov/23775837/)
- [Metushi et al., IgG3 dominant anti-isoniazid antibodies (PMID:24786179)](https://pubmed.ncbi.nlm.nih.gov/24786179/)
- [Metushi, Uetrecht & Phillips, Br J Clin Pharmacol 2016 (PMID:26773235)](https://pubmed.ncbi.nlm.nih.gov/26773235/)
- [Yoon et al., Synergistic toxicity with copper and NAT2, Exp Mol Med 2024 (PMID:38424191)](https://pubmed.ncbi.nlm.nih.gov/38424191/)
- [Dinegro et al., NAT2 acetylation phenotype meta-analysis, Pharmacogenomics 2026 (PMID:42531284)](https://pubmed.ncbi.nlm.nih.gov/42531284/)
- [Tavkar et al., NAT2 variants in AT-DILI meta-analysis (PMID:41657030)](https://pubmed.ncbi.nlm.nih.gov/41657030/)
- [Mahajan & Tyagi, NAT2 pharmacogenomics meta-analysis, BMC Genom Data 2024 (PMID:39639188)](https://pubmed.ncbi.nlm.nih.gov/39639188/)
- [Nicoletti et al., Genetic risk factors in isoniazid-containing regimen DILI (PMID:33135175)](https://pubmed.ncbi.nlm.nih.gov/33135175/)
- [Batool et al., Isoniazid and rifampicin hepatotoxicity: from metabolism to immunity (PMID:41793109)](https://pubmed.ncbi.nlm.nih.gov/41793109/)
- [Azuma et al., NAT2 genotype-guided regimen RCT (PMID:23150149)](https://pubmed.ncbi.nlm.nih.gov/23150149/)
- [Yoo et al., NAT2 genotype-guided isoniazid monotherapy pilot (PMID:33165168)](https://pubmed.ncbi.nlm.nih.gov/33165168/)
- [Sterling et al., Three months of rifapentine and isoniazid, NEJM 2011 (PMID:22150035)](https://pubmed.ncbi.nlm.nih.gov/22150035/)
- [Maw & Aitken, Isoniazid overdose case series (PMID:17535059)](https://pubmed.ncbi.nlm.nih.gov/17535059/)
- [EXTRIP workgroup, Extracorporeal treatment for isoniazid poisoning (PMID:33660266)](https://pubmed.ncbi.nlm.nih.gov/33660266/)
- [Dilrukshi et al., Oral pyridoxine substitution (PMID:28789699)](https://pubmed.ncbi.nlm.nih.gov/28789699/)
- [Yadav et al., Pyridoxine in isoniazid-induced psychosis (PMID:36875946)](https://pubmed.ncbi.nlm.nih.gov/36875946/)
- [Steichen et al., Isoniazid induced neuropathy: consider prevention (PMID:16788441)](https://pubmed.ncbi.nlm.nih.gov/16788441/)
- [Shetty & Shah, Isoniazid-induced neuropathy in a pre-pubertal child (PMID:29897291)](https://pubmed.ncbi.nlm.nih.gov/29897291/)
- [Zhao et al., DILI from anti-tuberculosis treatment cohort (PMID:32145061)](https://pubmed.ncbi.nlm.nih.gov/32145061/)
- [Singh et al., Isoliquiritigenin in isoniazid hepatotoxicity, SD rats (PMID:41587410)](https://pubmed.ncbi.nlm.nih.gov/41587410/)
- [Shastri & Taneja, Tuberculosis in cirrhosis (PMID:42322387)](https://pubmed.ncbi.nlm.nih.gov/42322387/)
- [Eadon et al., CPIC guideline for NAT2 and hydralazine (PMID:40974042)](https://pubmed.ncbi.nlm.nih.gov/40974042/)
- [LiverTox: Isoniazid, NCBI Bookshelf NBK548754](https://www.ncbi.nlm.nih.gov/books/NBK548754/)
- [StatPearls: Isoniazid Toxicity, NCBI Bookshelf NBK531488](https://www.ncbi.nlm.nih.gov/books/NBK531488/)
- [WHO Global Tuberculosis Report 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025)
- [ICD-10-CM T37.1X5A, adverse effect of antimycobacterial drugs](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T37-/T37.1X5A)
- [Bishnu et al., CYP2E1 in antitubercular drug-induced hepatotoxicity, Int J Hepatol 2025](https://onlinelibrary.wiley.com/doi/10.1155/ijh/9980298)
- [Surarak et al., Efficacy, safety and pharmacokinetics of isoniazid affected by NAT2 polymorphisms, Clin Transl Sci 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11022300/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 30 |
| On topic | 21 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:39688840` (1 mention) - 2023 Annual Report of the National Poison Data System® (NPDS) from America's Poison Centers®: 41st Annual Report.
  - shared terms: drug
- `PMID:41432769` (1 mention) - 2024 Annual report of the National Poison Data System® (NPDS) from America's Poison Centers(®): 42nd annual report.
  - shared terms: drug

Weighed against this report's own most characteristic terms: `isoniazid`, `liver`, `toxicity`, `treatment`, `injury`, `drug`, `pyridoxine`, `nat2`, `neuropathy`, `acute`, `verbatim`, `failure`, `paraphrase-risk`, `month`, `livertox`, `patient`, `disease`, `gene`, `hepatitis`, `hepatic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
