---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-13T17:00:38.071825'
end_time: '2026-08-13T17:09:31.274250'
duration_seconds: 533.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Formaldehyde Poisoning
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
  - claude-opus-5[1m]
  web_search_requests: 13
  num_turns: 28
  total_cost_usd: 3.3521510000000005
  session_id: c9f4f7ba-2735-40a1-9f18-c6703344220c
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Formaldehyde Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Formaldehyde Poisoning** covering all of the
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

I'm going to research this directly and write the report inline — no delegation, no background work.

sup Harry — ok, so I dug into this one directly (searches + pulled abstracts off PubMed myself). Report's below. One thing up front so you don't get burned downstream: **I've marked every quote as VERIFIED (I fetched the abstract and read it) or UNVERIFIED (came out of a search summary or a paraphrasing fetch).** Only the VERIFIED ones are safe to paste into an `evidence:` block without re-running `just fetch-reference`. And I did *not* guess a MONDO ID — you know how that ends.

---

# Formaldehyde Poisoning — Research Report

**Prepared:** 2026-08-13 · **Target entry:** `kb/disorders/Formaldehyde_Poisoning.yaml` · **Category:** Environmental

---

## 0. Framing: this is three diseases wearing one coat

Before the sections, the thing that should shape the whole entry. "Formaldehyde poisoning" is not one pathophysiology — it's a chemical whose damage mode is set almost entirely by **dose and route**, like how the same enzyme is housekeeping at one concentration and a wrecking ball at another:

1. **Acute corrosive/irritant injury** — formaldehyde as a protein crosslinker doing to your stomach lining exactly what it does to a specimen jar. Fast, local, mechanical.
2. **Acute systemic acidosis** — the metabolite (formate) is the killer, sharing a final common pathway with methanol poisoning. And formalin usually *contains* methanol, so you often get both at once.
3. **Chronic genotoxic injury** — DNA-protein crosslinks, hematopoietic stem cell attrition, nasal carcinoma. Slow, cumulative, and the one where the genetics live.

There's a fourth: **inherited failure to clear endogenous formaldehyde** (AMeD syndrome, ADH5/ALDH2). Same molecule, no exposure at all — the body poisons itself because the drain is clogged. That's a separate MONDO entity and probably a separate dismech entry, but it is *the* mechanistic Rosetta stone for the chronic arm and I've covered it here.

---

## 1. Disease Information

### Overview
Formaldehyde (HCHO; CHEBI:16842) is a colorless, pungent, highly water-soluble gas — a small, hungry electrophile that grabs nucleophilic amine and thiol groups on proteins and nucleic acids. **Formalin** is the aqueous form, typically 37–40% formaldehyde by weight, and critically it is usually **stabilized with 10–15% methanol** to stop polymerization. That methanol is not an incidental impurity; it's a co-poison that changes management.

Formaldehyde poisoning covers acute toxicity from **ingestion** (formalin — accidental, suicidal, rarely homicidal), **inhalation** (occupational/industrial, indoor air), **dermal/ocular contact**, and rare **iatrogenic** routes (intravesical formalin for refractory hemorrhagic cystitis; dialysate contamination; endodontic formaldehyde-containing sealers).

> **VERIFIED quote — PMID:10962510** (Pandey CK et al., *Hum Exp Toxicol*, 2000;19(6):360-6):
> "Ingestion can lead to immediate deleterious effects on almost all systems of the body including gastrointestinal tract, central nervous system, cardiovascular system and hepato-renal system, causing gastrointestinal hemorrhage, cardiovascular collapse, unconsciousness or convulsions, severe metabolic acidosis and acute respiratory distress syndrome."

> **VERIFIED quote — PMID:10962510:**
> "No specific antidote is available. Treatment of toxicity is supportive care of the various organ systems."

### Identifiers

| Resource | ID | Notes |
|---|---|---|
| **ICD-10-CM** | **T59.2** (T59.2X1–X4 by intent, +A/D/S encounter) | "Toxic effect of formaldehyde" — this is the *gas/vapor* branch (T51–T65) |
| **ICD-11** | NE61 / NE60-range (toxic effect of corrosive/other substances) | Verify the exact stem code; ICD-11 does not carry a dedicated formaldehyde leaf as cleanly as ICD-10 |
| **MeSH** | D005557 (Formaldehyde) + `/poisoning` or `/toxicity` subheading | No standalone "formaldehyde poisoning" descriptor |
| **CHEBI** | CHEBI:16842 (formaldehyde); CHEBI:17790 (methanol); CHEBI:30751 (formic acid); CHEBI:15740 (formate) | high confidence, still worth an OAK pass |
| **CAS** | 50-00-0 | |
| **MONDO** | ⚠️ **NOT RESOLVED.** I could not confirm a MONDO term for formaldehyde poisoning in this research. | **Do a live OLS/`runoak` lookup before curating.** Do not guess — a real-but-wrong MONDO ID is worse than none. Check whether it sits under a chemical-poisoning grouping alongside your existing `Arsenic_Poisoning` entry, and mirror whatever pattern that one used. |
| **OMIM** | 619151 — AMED SYNDROME, DIGENIC | *Not* the exposure disease; the inherited clearance failure |
| **Orphanet** | No ORPHA code for the acute exposure. AMeD syndrome should have one — check `ORPHA:` cache | |

### Synonyms
Formalin poisoning · formalin intoxication · formaldehyde toxicity · formaldehyde intoxication · methanal poisoning · formol poisoning · (occupational, non-equivalent) formaldehyde-induced occupational asthma; formaldehyde allergic contact dermatitis.

### Data provenance character
Predominantly **individual case reports and small case series** for the acute poisoning (there are no cohorts — nobody runs a formalin-ingestion RCT), **occupational cohort epidemiology** for the chronic/carcinogenic arm (NCI formaldehyde worker cohort, NIOSH cohort), **animal bioassay** for the dose-response, and **regulatory aggregate documents** (ATSDR ToxProfile 111, IARC Monograph 100F, EPA IRIS, NTP RoC). Poison-center aggregate data (AAPCC NPDS) exists but formaldehyde is not broken out cleanly.

---

## 2. Etiology

### Primary causal factor
**Exogenous formaldehyde exposure**, dose- and route-dependent. This is a toxicological entry, not a genetic one — the "cause" is the exposure and the modifiers are genetic.

### Environmental / exposure risk factors

**Occupational** (the dominant chronic-risk population):
- Anatomy/pathology/histology labs, embalming and funeral service (highest measured exposures — embalmers routinely see peaks >1 ppm)
- Wood composites: particleboard, MDF, plywood (urea-formaldehyde and phenol-formaldehyde resins)
- Textile finishing (permanent-press resins), paper, foundry (furan binders), plastics/resin manufacture
- Healthcare (disinfection, sterilization), agriculture/poultry fumigation, aquaculture (formalin as parasiticide)
- Hairdressing — keratin/"Brazilian blowout" smoothing treatments release formaldehyde on heating; FDA has moved toward restricting these

**Domestic/environmental:**
- Off-gassing from pressed-wood furniture and building products (the FEMA trailer episode after Hurricane Katrina is the reference public-health event)
- Tobacco smoke (a major indoor contributor), combustion, cooking, candles, incense
- New-build/renovated interiors with poor ventilation; higher temperature and humidity accelerate off-gassing
- Some cosmetics/personal-care via **formaldehyde releasers** (quaternium-15, DMDM hydantoin, imidazolidinyl urea, bronopol)

**Acute ingestion setting:** self-harm (dominant in reported series, especially where formalin is domestically or industrially accessible), accidental decanting into an unlabeled beverage container.

> **VERIFIED quote — PMID:35394178** (Zhang L et al., *Int J Legal Med*, 2022):
> "This article reports a case of a 50-year-old woman who died after accidentally drinking 25% formaldehyde solution in a transparent plastic bottle."

> **VERIFIED quote — PMID:10962510:**
> "Ingestion is rare because of alarming odour and irritant effect but documented in accidental, homicidal or suicidal attempts."

**Host/demographic modifiers:** children (smaller dose per kg, higher minute ventilation per kg), asthmatics and atopic individuals (lower irritant threshold), pre-existing airway disease, prior sensitization.

### Genetic risk factors — this is the good part

The clearance machinery is a **two-tier system**, and both tiers have common human variation:

| Gene | Role | Variant | Effect |
|---|---|---|---|
| **ADH5** (alcohol dehydrogenase 5 / **formaldehyde dehydrogenase** / GSNOR) | **Tier 1** — GSH-dependent oxidation of S-hydroxymethylglutathione, the main cellular formaldehyde drain | Biallelic rare LoF variants | Loss of primary detox |
| **ALDH2** (mitochondrial aldehyde dehydrogenase 2) | **Tier 2** — backup aldehyde clearance | **rs671, p.Glu504Lys** (`ALDH2*2`; also written E487K in the mature protein) — the East Asian "alcohol flush" allele, **dominant-negative** | Reduced backup capacity |

`ALDH2*2` is carried by an enormous number of people — roughly 28–45% allele-carrier frequency across East Asian populations, on the order of **500+ million people worldwide** — which makes it one of the most consequential common variants in human aldehyde biology. Its interaction with formaldehyde exposure is, to my knowledge, **not well characterized epidemiologically in FA-exposed workers**, and that's a legitimate, flaggable knowledge gap for the entry.

> **VERIFIED quote — PMID:33355142** (Oka Y et al., *Sci Adv*, 2020):
> "Here, we show that the rs671 defective allele in combination with mutations in the alcohol dehydrogenase 5 gene, which encodes formaldehyde dehydrogenase (ADH5FDH), causes a previously unidentified disorder, AMeD (aplastic anemia, mental retardation, and dwarfism) syndrome."

Downstream of clearance, the **repair** genes matter too: **FANCD2** and the broader Fanconi anemia/BRCA interstrand-crosslink pathway, DNA-protein-crosslink proteases (**SPRTN**), the p97/VCP unfoldase, and **POLQ** (theta-mediated end joining). Fanconi anemia patients are, in principle, a formaldehyde-hypersensitive population — though I'd treat "FA patients should avoid FA exposure" as biologically motivated rather than clinically demonstrated.

### Protective factors
- **Environmental:** ventilation, low-emission (CARB Phase 2 / TSCA Title VI compliant) composite wood, substitution of formaldehyde-free resins, engineering controls, respiratory protection. These are engineering facts, not epidemiologic "protective factor" findings.
- **Genetic:** none established. Wild-type `ALDH2`/`ADH5` is baseline capacity, not protection.
- **⚠️ Folate is a trap.** The intuitive move — "give folate, it feeds one-carbon metabolism" — is complicated by Burgos-Barragan's finding that the folate backbone *itself* decomposes into formaldehyde:

> **VERIFIED quote — PMID:28813411** (Burgos-Barragan G et al., *Nature*, 2017):
> "Here we show that supplementation with tetrahydrofolate, the essential cofactor of this cycle, and other oxidation-prone folate derivatives kills human, mouse and chicken cells that cannot detoxify formaldehyde or that lack DNA crosslink repair. Notably, formaldehyde is generated from oxidative decomposition of the folate backbone."

This is a genuinely nice curation nugget: **folinic acid is standard acute therapy** (to push formate → CO₂) while **folate supplementation is cytotoxic in clearance-deficient cells**. Same molecule class, opposite sign, depending on which arm of the disease you're in. Worth an explicit `discussions:` block.

### Gene–environment interaction
The cleanest GxE story here is *endogenous*: `ADH5^-/-` + `ALDH2*2` produces disease with **no exogenous exposure whatsoever**, because the body's own metabolism generates enough formaldehyde to be lethal to stem cells. That establishes the mechanism; exogenous exposure then adds to the same pool. A plausible (and untested) prediction: `ALDH2*2` carriers with `ADH5` heterozygosity should be the sensitive tail of the occupational exposure distribution. Flag as `KNOWLEDGE_GAP`.

---

## 3. Phenotypes

⚠️ **All HPO IDs below need `just validate-terms` / OAK confirmation before curation.** I've marked confidence. Frequencies are largely qualitative — the acute literature is case reports, so **omit `frequency:` rather than manufacture a band** (per your frequency-evidence SOP).

### A. Acute inhalation (irritant syndrome) — onset minutes, course acute/self-limited if exposure ends

| Phenotype | Suggested HP | Conf. | Notes |
|---|---|---|---|
| Eye irritation / lacrimation | HP:0000509 (blepharitis? — **verify**) | low | Threshold ~0.5–1 ppm; the earliest and most reliable effect |
| Nasal/throat irritation, rhinitis | HP:0002333 (**verify**) | low | |
| Cough | **HP:0012735** | high | |
| Dyspnea | **HP:0002094** | high | |
| Wheezing / bronchospasm | **HP:0030828** | high | Sensitized individuals react at ≈0.3 ppm |
| Respiratory distress | **HP:0002098** | med | |
| Pulmonary edema (high concentration) | HP:0100598 (**verify**) | med | ~50–100 ppm range |
| Chemical pneumonitis | HP:0006536 / HP:0002090 (**verify**) | low | |
| Hypoxemia | HP:0012418 (**verify**) | med | |

Dose landmarks worth curating as `notes`: irritation ~0.5–2 ppm; intolerable irritation 10–20 ppm; **NIOSH IDLH 20 ppm**; pulmonary edema/laryngospasm 50–100 ppm; potentially fatal >100 ppm.

### B. Acute ingestion (corrosive + systemic) — onset minutes to hours, severe, often fatal

**Local corrosive:**
- Oropharyngeal/esophageal/gastric burns; severe **epigastric and retrosternal pain** (HP:0011established — use HP:0002027 Abdominal pain, **verify**)
- Odynophagia, drooling, vomiting (**HP:0002013**), hematemesis, **GI hemorrhage** (HP:0002239, **verify**)
- Gastric perforation, peritonitis
- The stomach is preferentially hit — formaldehyde "fixes" the mucosa the way it fixes a specimen

**Systemic:**
- **Severe high-anion-gap metabolic acidosis** (HP:0001942 Metabolic acidosis, **verify**) — the signature lab finding, driven by formate + lactate
- Circulatory shock / cardiovascular collapse
- CNS depression → **coma** (HP:0001259, **verify**), **seizures** (HP:0001250)
- **Acute kidney injury** (HP:0001919, **verify**) progressing to anuric renal failure
- Hepatic injury, transaminase elevation (HP:0002910, **verify**)
- ARDS
- Hemolysis (reported with formic acid), DIC
- Visual disturbance/blindness — **if methanol co-ingestion is significant**; formate is the optic-nerve toxin common to both

**Late/delayed (weeks):**
- **Esophageal stricture** and **gastric outlet obstruction** — the fibrotic sequela; documented specifically after formaldehyde ingestion. Onset typically 2–8 weeks post-injury.

### C. Chronic exposure

- Occupational asthma / airway hyperreactivity (HP:0002099 Asthma, **verify**)
- **Allergic contact dermatitis** (HP:0000964 Eczema, **verify**) — type IV hypersensitivity to formaldehyde and releasers. Meta-analytic contact-allergy prevalence ≈**2.6% adults / 3.0% children**, highest in North America (~6.8%) ⚠️ UNVERIFIED (search summary of PMID:42035787 — that PMID looks anomalously high, **check it exists** before citing)
- Chronic rhinitis, nasal epithelial dysplasia/metaplasia
- Reduced pulmonary function on longitudinal occupational follow-up
- **Nasopharyngeal carcinoma**; **myeloid leukemia** (IARC Group 1 endpoints)
- Reported but contested: neurocognitive/memory complaints, sick-building-syndrome symptom clusters, adverse reproductive outcomes

### D. Inherited clearance failure (AMeD syndrome) — separate entity, childhood onset

Core triad across the reported cohort: **bone marrow failure / aplastic anemia**, **short stature**, **intellectual disability**. Roughly half show pigmentation changes; ~a quarter skeletal anomalies. Also reported: microcephaly, low birth weight, ophthalmologic findings, immune dysfunction, viral warts, progression to MDS/leukemia requiring HSCT.
⚠️ These cohort proportions come from a **paraphrased** fetch of PMID:38614309 (Matsumoto et al., *Eur J Med Genet*, 2024; n=18: 13 F / 5 M) — **re-fetch the verbatim abstract before quoting.**

### Quality of life
No formaldehyde-specific QoL instrument literature found. For the corrosive-stricture survivors, expect the caustic-ingestion QoL profile (dysphagia, repeated dilations, nutritional compromise, psychiatric comorbidity given intent). For occupational asthma/ACD, standard ACQ/DLQI-type impacts. **State as not-established rather than inventing numbers.**

---

## 4. Genetic / Molecular Information

For the **exposure disease**: no causal gene. Genetics enters as susceptibility and as the mechanistic mirror.

### Genes

| Gene | HGNC | OMIM | Role |
|---|---|---|---|
| **ADH5** | hgnc:253 (**verify**) | *103710 | GSH-dependent formaldehyde dehydrogenase (= S-nitrosoglutathione reductase, GSNOR). Tier-1 detox. |
| **ALDH2** | hgnc:404 (**verify**) | *100650 | Mitochondrial ALDH; tier-2 backup |
| **FANCD2** | hgnc:3585 (**verify**) | *613984 | Repairs formaldehyde-induced DNA crosslinks |
| **ADH1B/ADH1C, ALDH1A1** | — | — | Minor/contextual aldehyde handling |
| **SPRTN**, **VCP**, **POLQ** | — | — | DNA-protein-crosslink resolution and tolerance |

*(Note the lowercase `hgnc:` prefix — that's your repo's canonical form.)*

### Key variants
- **`ALDH2` rs671, c.1510G>A, p.Glu504Lys** — missense, **dominant-negative** (the tetramer is poisoned by one bad subunit, so heterozygotes lose most activity). gnomAD: near-absent in European/African populations, very common East Asian. ClinVar: risk factor / established pharmacogenomic variant (nitroglycerin, alcohol).
- **`ADH5` biallelic LoF** — reported variants include nonsense, frameshift, and splice-affecting alleles in Japanese AMeD patients. Rare; carrier frequency not well established outside Japan.

> **VERIFIED quote — PMID:33355142** (Oka 2020):
> "Collectively, our results suggest that the combined deficiency of formaldehyde clearance mechanisms leads to the complex clinical features due to overload of formaldehyde-induced DNA damage, thereby saturation of DNA repair processes."

> ⚠️ **PARTIAL/UNVERIFIED fragments — PMID:33512438** (Mu A et al., *Blood*, 2021): patients carry "biallelic variants in ADH5 combined with a heterozygous ALDH2*2 dominant-negative allele"; disease-model iPSC hematopoietic differentiation showed "drastically defective cell expansion." **Re-fetch for verbatim before use.** This paper also establishes **ADH5 as primary, ALDH2 as backup**, and shows partial rescue by the ALDH2 agonist **compound C1** — a nice `treatments`/`experimental_models` link.

### Functional consequence
Both are **LOSS_OF_FUNCTION** at the variant level → use `GeneticContext.functional_impact_category: LOSS_OF_FUNCTION` (or `DOMINANT_NEGATIVE` specifically for `ALDH2*2` — that's exactly the finer distinction your schema wants). At the pathway-node level, the *state* is reduced formaldehyde catabolism → `modifier: DECREASED` on the GO process node.

### Epigenetics
Formaldehyde perturbs one-carbon metabolism, which is the substrate supply line for SAM-dependent methylation — so global/locus-specific DNA methylation changes are mechanistically plausible and have been reported in exposed workers, but I'd call the human epigenomic evidence **thin and not yet curatable as a mechanism node**.

### Chromosomal
No constitutional abnormality. Acquired: **elevated sister chromatid exchange** in ADH5/ALDH2-deficient patient lymphocytes (and notably *not* in their fibroblasts — a nice tissue-specificity detail); formaldehyde causes chromosomal aberrations and micronuclei in exposed workers' lymphocytes and buccal cells. Distinguishing feature vs Fanconi anemia: **AMeD patients do not show classic DEB/MMC chromosome fragility**, which is diagnostically important.

---

## 5. Environmental Information

**Chemical:** CHEBI:16842. ECTO should have an "exposure to formaldehyde" term (and possibly route-specific children) — look it up rather than trusting me on the ID. For dismech, use `influences_mechanisms` with `environmental_effect: TRIGGERS` on the exposure→systemic-burden node, exactly the way `Arsenic_Poisoning` does it.

**Exposure limits (curate as `notes`, they're regulatory not mechanistic):**

| Standard | Value |
|---|---|
| OSHA PEL (8-h TWA) | 0.75 ppm |
| OSHA STEL (15-min) | 2 ppm |
| OSHA Action Level | 0.5 ppm |
| NIOSH REL | 0.016 ppm TWA / 0.1 ppm ceiling (15-min) — NIOSH treats it as an occupational carcinogen |
| NIOSH IDLH | 20 ppm |
| ACGIH TLV | 0.1 ppm ceiling (**verify current**) |
| WHO indoor air guideline | 0.1 mg/m³ (~0.08 ppm), 30-min average |

**Lifestyle:** tobacco smoking is a substantial personal formaldehyde source and a confounder in every occupational leukemia analysis. Alcohol matters indirectly — `ALDH2*2` carriers get acetaldehyde loading on top of formaldehyde, competing for the same tier-2 enzyme. Dietary formaldehyde exists (naturally in fruits, fish — especially gadoid fish where TMAO breaks down to formaldehyde) but is not a recognized toxicity source at dietary levels.

**Infectious agents:** N/A.

---

## 6. Mechanism / Pathophysiology

This is the section that should drive the `pathophysiology:` graph. I've written it as four causal chains with suggested `biological_scale` tags.

### Chain A — Corrosive protein crosslinking (local injury)

```
Formaldehyde contact with mucosa [MOLECULAR]
  → Schiff-base formation with protein lysine ε-amino and N-terminal amines;
    methylol adducts; methylene (-CH2-) bridge crosslinks [MOLECULAR]
  → protein denaturation/coagulation, loss of native function ("tissue fixation") [MOLECULAR]
  → coagulative necrosis of epithelium and submucosa [TISSUE]
  → mucosal ulceration, hemorrhage, perforation [TISSUE]
  → (weeks) granulation, fibrotic remodeling → stricture / gastric outlet obstruction [TISSUE]
```

> **VERIFIED quote — PMID:35394178** (Zhang 2022):
> "Of late, the mechanism of death from formaldehyde poisoning is that it rapidly causes coagulation of tissue cell protein, which may lose its normal function."

> **VERIFIED quote — PMID:35394178:**
> "Based on the pathological characteristics of the case, we put forward a new viewpoint on the mechanism of death from formaldehyde poisoning in which formaldehyde causes rapid fixation of blood in the tissue, thus leading to acute circulatory disturbance."

That second one is an interesting and *non-consensus* claim — intravascular fixation of blood causing acute circulatory failure. Curate it as its own node with `supports: PARTIAL` and an explicit `discussions:` entry noting it's a single forensic case's proposed mechanism, not established. Don't launder a hypothesis into settled pathophysiology.

The late stricture arm is a clean candidate for **`conforms_to: fibrotic_response#...`**.

### Chain B — Metabolism to formate → acidosis (systemic injury)

```
Absorbed formaldehyde [MOLECULAR]
  → spontaneous conjugation with glutathione → S-hydroxymethylglutathione [MOLECULAR]
  → ADH5 (GSH-dependent formaldehyde dehydrogenase) oxidation → S-formylglutathione
    [GO:0046294 formaldehyde catabolic process; GO:0051903 S-(hydroxymethyl)glutathione
     dehydrogenase activity — verify both]
  → esterase hydrolysis → FORMATE [MOLECULAR]
  → formate accumulation exceeding folate-dependent clearance [ORGANISM]
  → (i) high-anion-gap metabolic acidosis [ORGANISM]
    (ii) inhibition of mitochondrial cytochrome c oxidase (complex IV) → histotoxic hypoxia
         → lactate accumulation, compounding the acidosis [CELLULAR]
  → shock, CNS depression, optic neuropathy, multiorgan failure [ORGANISM]
```

Key kinetic facts for the entry:
- Formaldehyde's blood half-life is **very short (~1–2 minutes)** — it barely exists as formaldehyde once absorbed. **This is why blood formaldehyde is useless as a clinical assay and formate is the thing to measure.** ⚠️ the specific 1.5-min figure I could not verify in a fetched abstract — treat as UNVERIFIED, source it from ATSDR ToxProfile 111 or IARC Mono 100F.
- Endogenous blood formaldehyde in unexposed humans: **~2.61 ± 0.14 µg/g (range 2.05–3.09)**, i.e. roughly 0.1 mM ⚠️ UNVERIFIED (search summary attributing to IARC Mono 100F / NBK326466). Worth chasing because it's the number that makes the whole "inhalation doesn't raise systemic formaldehyde" argument.
- Formate rises fast — reported detectable/high within ~30 min of ingestion. ⚠️ UNVERIFIED.
- PMID:7265415 (Eells JT et al., *JAMA* 1981;246(11):1237-8, "Formaldehyde poisoning. Rapid metabolism to formic acid") is the classic citation for this — **but I confirmed it has NO ABSTRACT in PubMed.** Per your §4/§6 SOP: you cannot quote it. Cite it in `notes`, or find a review that states the finding quotably.

### Chain C — Genotoxicity → stem cell attrition and carcinogenesis

```
Formaldehyde (endogenous or exogenous) exceeding ADH5/ALDH2 clearance [MOLECULAR]
  → DNA adducts: N2-hydroxymethyl-deoxyguanosine; dG-dG interstrand crosslinks;
    DNA-PROTEIN CROSSLINKS (DPCs) [MOLECULAR]
  → replication fork stalling and collapse [CELLULAR]
  → engagement of FANCD2 / Fanconi-BRCA interstrand crosslink repair (GO:0036297),
    DPC proteolysis (SPRTN/p97), POLQ-mediated end joining [CELLULAR]
  → when repair capacity is saturated: persistent damage, chromosomal aberration,
    apoptosis of hematopoietic stem cells [CELLULAR]
  → HSC pool depletion → bone marrow failure / aplastic anemia [ORGANISM]
  → surviving damaged clones → clonal evolution → MDS / myeloid leukemia [ORGANISM]

Parallel local arm (inhalation):
  Formaldehyde at portal of entry [MOLECULAR]
  → nasal respiratory epithelial cytotoxicity [CELLULAR]
  → compensatory regenerative cell proliferation + sustained inflammation [TISSUE]
  → fixation of DPC-derived mutations in a proliferating field (incl. p53 mutation)
  → epithelial dysplasia → squamous metaplasia → squamous cell carcinoma [TISSUE]
```

> **VERIFIED quote — PMID:26412304** (Pontel LB et al., *Mol Cell*, 2015):
> "Endogenous formaldehyde is produced by numerous biochemical pathways fundamental to life, and it can crosslink both DNA and proteins."

> **VERIFIED quote — PMID:26412304:**
> "Adh5(-/-)Fancd2(-/-) mice reveal an essential requirement for these protection mechanisms in hematopoietic stem cells (HSCs), leading to their depletion and precipitating bone marrow failure. More widespread formaldehyde-induced DNA damage also causes karyomegaly and dysfunction of hepatocytes and nephrons."

> **VERIFIED quote — PMID:26412304:**
> "Formaldehyde is therefore an important source of endogenous DNA damage that is counteracted in mammals by a conserved protection mechanism."

> **VERIFIED quote — PMID:32686516** (Bernardini L et al., *Drug Chem Toxicol*, 2022):
> "Evaluations carried out in experimental studies showed toxic effects on different organs as lung, upper respiratory tract, bone marrow and brain as well as in cells."

**Crucial nuance for the carcinogenesis node — the dose-distribution problem.** Stable-isotope work (Swenberg and colleagues, ¹³CD₂-formaldehyde) shows exogenous inhaled formaldehyde forms adducts **only at the portal of entry**, not at distant sites, and that at low exposures **>99% of formaldehyde DNA adducts are endogenous**. ⚠️ UNVERIFIED (search summary; primary sources include the *Chem Res Toxicol* nonhuman-primate ¹³CD₂ paper and PMID:30701286). This is the central argument against a systemic mechanism for formaldehyde-induced leukemia, and it makes **leukemia the contested endpoint** — nasopharyngeal carcinoma is much better mechanistically anchored. Curate this as an explicit competing-hypothesis structure: `mechanistic_hypotheses` with a CANONICAL local-genotoxicity model and an ALTERNATIVE/contested systemic model, plus a `KNOWLEDGE_GAP` discussion. Do not present formaldehyde-leukemia as settled.

### Chain D — Immune sensitization

```
Formaldehyde penetrating skin/airway epithelium [MOLECULAR]
  → haptenation: covalent modification of self proteins [MOLECULAR]
  → dendritic cell uptake and presentation of hapten-modified peptide [CELLULAR]
  → hapten-specific T-cell priming (type IV / delayed hypersensitivity) [CELLULAR]
  → on re-exposure: T-cell-mediated dermatitis (ACD) or airway inflammation [TISSUE]
  → allergic contact dermatitis; occupational asthma [ORGANISM]
```

### Chain E — The salvage arm (why this isn't purely destructive)

Formaldehyde detoxification isn't just disposal — the formate produced feeds nucleotide synthesis.

> **VERIFIED quote — PMID:28813411** (Burgos-Barragan 2017, *Nature*):
> "Furthermore, we find that formaldehyde detoxification in human cells generates formate, and thereby promotes nucleotide synthesis. This supply of 1C units is sufficient to sustain the growth of cells that are unable to use serine, which is the predominant source of 1C units."

Curate this as physiologic context (`notes` or a non-pathological node) — it's why formaldehyde is a *normal metabolite* whose toxicity is a capacity-overflow phenomenon, which is the entry's whole thesis.

### Suggested ontology terms (⚠️ all need OAK verification)

**GO (biological process / molecular function):** GO:0046294 formaldehyde catabolic process · GO:0051903 S-(hydroxymethyl)glutathione dehydrogenase activity · GO:0004029 aldehyde dehydrogenase (NAD+) activity · GO:0006730 one-carbon metabolic process · GO:0036297 interstrand cross-link repair · GO:0006281 DNA repair · GO:0034599 cellular response to oxidative stress · GO:0006954 inflammatory response · GO:0006915 apoptotic process · GO:0006749 glutathione metabolic process

**CL:** CL:0000037 hematopoietic stem cell · CL:0002368 respiratory epithelial cell · CL:0000182 hepatocyte · CL:0000584 enterocyte · CL:0000451 dendritic cell · CL:0000625 CD8+ αβ T cell · CL:0000775 neutrophil

**GO cellular component:** GO:0005739 mitochondrion (formate/complex IV) · GO:0005634 nucleus (DPC/adducts) · GO:0005829 cytosol (ADH5)

---

## 7. Anatomical Structures Affected

**Portal of entry dominates.** This is the single most important anatomical principle for the entry — formaldehyde is so reactive it mostly doesn't get anywhere.

**Inhalation route:**
- Primary: nasal cavity and nasal mucosa (**UBERON:0001707 / UBERON:0001826**, verify), nasopharynx, larynx, trachea (**UBERON:0003126**), proximal bronchi
- Secondary at high concentration: lung parenchyma / alveoli (**UBERON:0002048**), conjunctiva and cornea (**UBERON:0000970** eye)
- Species note: rats concentrate injury in the **anterior nasal respiratory and transitional epithelium** — because they're obligate nose-breathers with high nasal deposition. Humans are oronasal breathers with different airflow, and human tumors cluster at the **nasopharynx**. This anatomical mismatch is a real `HUMAN_MODEL_MISMATCH` candidate.

**Ingestion route:**
- Primary: oropharynx, esophagus (**UBERON:0001043**), **stomach (UBERON:0000945)** — stomach worst hit; duodenum
- Secondary: liver (**UBERON:0002107**), kidney (**UBERON:0002113**, proximal tubule), brain, heart, lung (ARDS)

**Chronic/endogenous:**
- Bone marrow (**UBERON:0002371**) — HSC niche
- Skin (**UBERON:0002097**) — ACD
- Optic nerve (**UBERON:0000941**, verify) — formate-mediated, shared with methanol

**Subcellular:** cytosol (ADH5/GSH detox), mitochondrion (ALDH2; formate-inhibited complex IV), nucleus (adducts, DPCs, crosslinks).

**Lateralization:** N/A — diffuse/bilateral by exposure geometry.

---

## 8. Temporal Development

| Arm | Onset | Course |
|---|---|---|
| Acute inhalation | Seconds–minutes | Self-limited on removal; RADS/persistent hyperreactivity possible after severe exposure |
| Acute ingestion | Minutes | Fulminant. Acidosis and shock within hours; death typically within hours to days |
| Corrosive sequelae | 2–8 weeks post-injury | Stricture, gastric outlet obstruction; may need repeated dilation for years |
| Sensitization (ACD/asthma) | Weeks–months of repeat exposure to induce; minutes–days on re-challenge | Chronic-relapsing, exposure-dependent |
| Carcinogenesis | Years–decades latency | Progressive |
| AMeD syndrome | Childhood (growth/development early; marrow failure through childhood) | Progressive; HSCT-requiring |

**Critical intervention window (acute ingestion):** the first hours. Airway protection, bicarbonate, and early hemodialysis for formate. Endoscopy for injury grading is conventionally done within **12–48 hours** — early enough to grade, late enough that the injury has declared itself, and before the tissue is friable enough that scoping risks perforation.

**Remission:** the irritant syndrome resolves with removal. Corrosive damage does not remit — it heals by fibrosis. Sensitization does not remit; it's lifelong immunologic memory.

Nice mechanistic detail on reversibility from the rat bioassay — **the non-neoplastic lesions regress after exposure stops, but the carcinomas do not.** That's a real, curatable statement about which steps in the chain are reversible:

> **VERIFIED quote — PMID:6871871** (Kerns WD et al., *Cancer Res*, 1983):
> "There was regression of rhinitis, dysplasia, and metaplasia at 27 months (3 months postexposure) in the 14.3- and 5.6-ppm groups of mice and in the 2.0- and 5.6-ppm groups of rats."

---

## 9. Inheritance and Population

### Epidemiology of poisoning
No reliable prevalence or incidence figures exist for formaldehyde poisoning as such. It is **not a reportable condition**, poison-center data doesn't break it out cleanly, and the acute literature is case reports. **Curate this as `NOT_YET_DOCUMENTED` / `UNKNOWN` in the `prevalence_class` rather than inventing a number.** What can be said:
- Formalin ingestion is rare in high-income settings (the smell and immediate pain are self-limiting), and disproportionately reported from South and Southeast Asia where formalin is domestically accessible.
- Occupational exposure population: on the order of **1–2 million US workers** with some formaldehyde exposure ⚠️ UNVERIFIED — source from NIOSH/OSHA regulatory documents.

### Corrosive-ingestion outcome benchmarks (⚠️ ALL-CORROSIVE, NOT FORMALIN-SPECIFIC)
Pooled mortality **6.2%**, stricture formation **24.7%** across 44 studies / >6,000 patients; Grade III injury and intentional ingestion strongly predict both; age >60 an independent mortality risk. ⚠️ UNVERIFIED (search summary of a 2025 *Surgery* systematic review). **If you use these, label them explicitly as caustic-ingestion-general, not formaldehyde-specific** — formalin's added systemic formate toxicity means the formaldehyde-specific mortality is almost certainly worse.

### Lethal dose
**As little as 30 mL (1 oz) of 37% formaldehyde solution has been reported to cause death** ⚠️ UNVERIFIED-as-quote (ATSDR MMG for formaldehyde — a citable regulatory document, but it's not a PMID; put it in `notes` with the URL rather than forcing an `evidence:` block).

Forensic reference concentrations from a fatal case:

> **VERIFIED quote — PMID:35394178** (Zhang 2022):
> "The toxicity test results showed that the concentrations of formaldehyde in the blood and gastric tissue were 36.56 mg/kg and 274.48 mg/kg, respectively, which was consistent with death from formaldehyde poisoning."

### For AMeD syndrome
- **Inheritance:** digenic — biallelic `ADH5` + `ALDH2` rs671. Your CLAUDE.md has a whole section for this: use **`HP:0010984` Digenic inheritance**, bind the term, name both genes in the block `description`, and cite the digenicity claim separately. This is a textbook exemplar alongside `PRPH2-Related_Retinopathy`, and it belongs in the `Digenic_and_Oligogenic_Disorders` grouping.
- **Reported cases:** ~18 patients as of 2024 (13 F, 5 M) ⚠️ from paraphrased fetch — verify.
- **Population:** all reported patients to date are Japanese, which follows directly from `ALDH2*2` being effectively an East Asian allele. Not a founder effect in the classical sense — it's a *common* modifier allele meeting a *rare* one.
- **Penetrance/expressivity:** variable expressivity is explicit in the 2024 report (mild cases with only growth/developmental findings are missed).

---

## 10. Diagnostics

### The headline: **there is no useful clinical formaldehyde assay.**
Blood formaldehyde is metabolized within minutes and there's a substantial endogenous baseline, so a level is neither sensitive nor interpretable in the living patient. Diagnosis is **history + syndrome + surrogate labs**. (Post-mortem quantification in blood/gastric tissue *is* meaningful — see the forensic case above.)

### Laboratory
- **Arterial blood gas + serum chemistry → anion gap.** Severe HAGMA is the diagnostic centerpiece.
- **Serum formate** — the mechanistically correct analyte; available at reference labs, often too slow to guide the first hours.
- **Serum lactate** — elevated; contributes to the gap.
- **Osmolal gap + serum methanol** — because formalin carries methanol. An osmolal gap points at the methanol co-ingestion and changes management (fomepizole).
- CBC, coagulation, LFTs, creatinine/BUN, CK, lipase; type and cross.
- LOINC terms exist for formate, methanol, anion gap, lactate — worth binding if you populate `biochemical.reference_ranges`.

### Imaging / endoscopy
- **Upper GI endoscopy within 12–48 h** with **Zargar grading** (0, 1, 2a/2b, 3a/3b) — the single best predictor of stricture and mortality after any corrosive ingestion.
- CT abdomen/chest — increasingly preferred for full-thickness necrosis assessment and surgical triage; better specificity than endoscopy for some outcomes.
- Upright CXR / CT for perforation, mediastinitis, ARDS.
- Contrast swallow at 2–3 weeks for stricture surveillance.

### Functional / other
- Spirometry ± methacholine challenge, and **serial peak-flow with work/off-work comparison**, for suspected occupational asthma.
- **Patch testing** (formaldehyde 2% aq. is in most baseline series; also test formaldehyde releasers separately — a negative formaldehyde patch does not exclude releaser allergy).
- Nasal endoscopy/cytology in chronically exposed workers.
- Histopathology: coagulative necrosis with "fixed" tissue architecture — pathognomonic-feeling in the forensic setting.

### Genetic testing (for AMeD, not for poisoning)
- `ADH5` + `ALDH2` sequencing; the `ALDH2` rs671 genotype is on most East Asian arrays.
- **DEB/MMC chromosome breakage testing is NEGATIVE** — this is the key discriminator from Fanconi anemia in a child with marrow failure + short stature + ID.
- Elevated **sister chromatid exchange in lymphocytes** (but normal in fibroblasts).
- WES/WGS will find it; a Fanconi/IBMFS panel will only find it if `ADH5` and `ALDH2` are on the panel — many aren't. Worth stating.

### Differential diagnosis

| Condition | Distinguishing feature |
|---|---|
| **Methanol poisoning** | Shares formate/HAGMA/visual loss. Distinguished by absence of corrosive GI injury and by serum methanol/osmolal gap. **Frequently co-exists** with formalin ingestion. |
| Ethylene glycol | Oxalate crystalluria, hypocalcemia, renal failure; no corrosive injury |
| Acid/alkali caustic ingestion | Corrosive injury without the disproportionate systemic acidosis; alkali causes deeper liquefactive esophageal injury |
| Salicylate, metformin/lactic acidosis, DKA, uremia | HAGMA without corrosive injury |
| Glutaraldehyde / other aldehyde exposure | Very similar irritant profile; occupational history |
| **AMeD syndrome** vs **Fanconi anemia** | Negative chromosome fragility, no radial ray defects, digenic genotype |

### Screening
- **Occupational medical surveillance** under the OSHA formaldehyde standard: exposure monitoring, annual respiratory questionnaire, spirometry, physician evaluation for symptomatic workers.
- No population screening. No newborn screening for AMeD (and it wouldn't be actionable at birth).

---

## 11. Outcome / Prognosis

**Acute ingestion:** poor. Substantial formalin ingestion is frequently fatal within hours to days from shock + refractory acidosis + multiorgan failure. Survivors of the acute phase face sepsis, prolonged pulmonary complications, and often gastrectomy.

⚠️ UNVERIFIED (search summary of a Springer/*Intensive Care Med* case series): two patients ingesting formalin with suicidal intent presented with "extensive gastrointestinal corrosive damage, circulatory shock, metabolic acidosis, respiratory insufficiency and impairment of renal function," both required hemodialysis/hemofiltration, one required gastrectomy, and the course was "characterized by sepsis and protracted pulmonary complications." **Track down the PMID and re-fetch** — this is a good citation if it verifies.

**Prognostic factors:** volume and concentration ingested; time to presentation; **Zargar endoscopic grade** (grade 3b is the inflection point); depth of acidosis / formate level; need for vasopressors; age >60; intentional ingestion.

**Acute inhalation:** generally good with removal from exposure; high-concentration exposure can leave persistent airway hyperreactivity (RADS).

**Chronic:** occupational asthma and ACD are chronic-relapsing but not life-limiting. Nasopharyngeal carcinoma prognosis follows standard NPC staging. Formaldehyde-attributable leukemia risk remains contested (see §6).

**AMeD:** progressive marrow failure requiring HSCT in childhood; the mouse model recapitulates a "short life span."

> **VERIFIED quote — PMID:33355142** (Oka 2020):
> "Moreover, Adh5-/-Aldh2 E506K/E506K double-deficient mice recapitulated key clinical features of AMeDS, showing short life span, dwarfism, and hematopoietic failure."

**Recovery potential by tissue:** epithelial irritation → full recovery. Corrosive full-thickness injury → fibrotic, permanent. HSC depletion → not spontaneously recoverable; requires transplant. Interesting mechanistic finding worth its own node: in the mouse model, **bone marrow transplant rescued not only hematopoiesis but also nephron function**, implying a hematopoietic contribution to the renal phenotype (see the Pontel quote in §6).

---

## 12. Treatment

**Central fact: no antidote.** Everything is supportive plus enhanced elimination. (`VERIFIED` — see the PMID:10962510 quote in §1.)

### Acute ingestion

| Intervention | Detail | Suggested NCIT |
|---|---|---|
| **Airway protection** | Early intubation — laryngeal edema and aspiration risk | NCIT:C49236 Therapeutic Procedure (**verify**) |
| **Do NOT induce emesis; do NOT attempt chemical neutralization** | Re-exposes the esophagus; neutralization is exothermic | — |
| Activated charcoal | Recommended in ATSDR MMG, though binding of formaldehyde is poor and it obscures endoscopy — **contested**, curate as such | NCIT:C15986 Pharmacotherapy |
| Careful gastric lavage/NG suction | Only with a protected airway; contested given perforation risk | |
| **IV sodium bicarbonate** | For acidosis; ATSDR: adult 1 ampule, pediatric 1 mEq/kg | NCIT:C15986 + CHEBI:32139 sodium bicarbonate (**verify**) |
| Aggressive IV fluid resuscitation, vasopressors | Distributive/hypovolemic shock | NCIT:C15747 Supportive Care |
| **Hemodialysis** | **The key intervention** — clears formate *and* methanol and corrects acidosis. Low threshold. | NCIT — look up "Hemodialysis" (**verify**) |
| **Folinic acid (leucovorin)** | ~1 mg/kg IV q4h; accelerates formate → CO₂ via 10-formyl-THF dehydrogenase, the rate-limiting elimination step | NCIT:C15986 + CHEBI folinic acid (**verify**) |
| **Fomepizole or ethanol** | **ONLY if significant methanol co-ingestion** (serum methanol >20 mg/dL or elevated osmolal gap). Does *not* treat formaldehyde itself — formaldehyde is already past the ADH step. This distinction matters and is easy to get wrong. | NCIT:C15986 |
| PPI, nutritional support (NJ/TPN) | Mucosal protection, gut rest | NCIT:C15433 Nutritional Support |
| **Surgery** | Emergency gastrectomy/esophagectomy for full-thickness necrosis or perforation | NCIT:C15329 Surgical Procedure |
| **Endoscopic balloon dilation** | For strictures at 3+ weeks; often serial | NCIT — verify |

### Acute inhalation
Remove from exposure; humidified oxygen; **bronchodilators** (β₂-agonists) for bronchospasm; monitor for delayed pulmonary edema for 24–48 h; corticosteroids are used but the evidence is weak — curate as contested. Copious irrigation for eye/skin, ophthalmology referral for corneal injury.

### Chronic
- ACD: exposure avoidance/substitution (patient-specific allergen lists), topical corticosteroids, emollients
- Occupational asthma: **removal from exposure is the definitive treatment**; ICS/LABA otherwise
- Nasopharyngeal carcinoma: standard oncologic management (out of scope for this entry)

### AMeD syndrome
- **Allogeneic HSCT** — the definitive therapy for marrow failure. `NCIT:C15431` (hematopoietic cell transplantation) → `therapeutic_modality: CELL_THERAPY` per your mechanical backfill table.
- **Investigational: ALDH2 agonists** (compound C1; Alda-1 is the better-known congener). Partial rescue of hematopoietic expansion in patient-derived iPSC models — a pharmacologic chaperone/activator strategy for the dominant-negative enzyme. `therapeutic_modality: SMALL_MOLECULE`, preclinical only. Good `target_mechanisms` link back to the formaldehyde-clearance node with `ACTIVATES`.
- **Counsel against alcohol** in `ALDH2*2` carriers generally (competing substrate load).

### Pharmacogenomics
`ALDH2` rs671 is an established PGx variant (nitroglycerin bioactivation, alcohol) — relevant context but not a formaldehyde-poisoning treatment decision node today.

### Clinical trials
No trials of formaldehyde-poisoning treatment exist or plausibly could. There are ALDH2-activator trials in other indications and general caustic-injury trials. Search ClinicalTrials.gov for "ALDH2" if you want a `clinical_trials:` block; don't force one for the poisoning itself.

---

## 13. Prevention

**Primary (this is where nearly all the real-world benefit sits):**
- **Substitution** — formaldehyde-free resins, glutaraldehyde-free/formalin-free fixatives where feasible
- **Engineering controls** — local exhaust ventilation at gross-dissection and embalming stations; enclosed processes
- **Product regulation** — **TSCA Title VI / CARB ATCM Phase 2** composite-wood emission limits; EU restrictions; FDA action on formaldehyde-releasing hair-smoothing products
- **Indoor air** — WHO 0.1 mg/m³ 30-min guideline; ventilation in new construction; low-emission product selection
- **Storage/labeling** — the fatal case above hinged on formalin in "a transparent plastic bottle." Never decant into food/beverage containers. This is a cheap, high-yield public-health message.
- Smoking cessation (personal exposure reduction)
- PPE, respiratory protection, training under the OSHA formaldehyde standard (29 CFR 1910.1048)

**Secondary:** occupational medical surveillance (symptom questionnaire, spirometry); patch testing in workers with suspected ACD; no validated cancer screening for formaldehyde-exposed workers.

**Tertiary:** post-ingestion stricture surveillance and dilation; complete allergen avoidance after sensitization; job modification/removal for occupational asthma; long-term nutrition and psychiatric follow-up after intentional ingestion.

**Genetic counseling:** relevant only for AMeD — recurrence risk is complicated by digenicity (an `ADH5` carrier couple's risk is conditioned on the `ALDH2` genotype segregating too). Worth an explicit note; standard AR recurrence arithmetic doesn't apply cleanly.

**Immunization / prophylaxis:** N/A.

---

## 14. Other Species / Natural Disease

**Species (NCBITaxon):** *Rattus norvegicus* (10116), *Mus musculus* (10090), *Macaca* spp. / *Macaca fascicularis* (9541), *Equus caballus* (9796), *Canis lupus familiaris* (9615), *Gallus gallus* (9031, DT40 cells), *Danio rerio* (7955), *Homo sapiens* (9606).

**Species sensitivity is dramatically different and this matters for translation.** From the Kerns bioassay: 103 rats developed nasal SCC at 14.3 ppm versus **2 male mice** at the same concentration. Mice reflexively reduce their minute ventilation on formaldehyde exposure — they literally breathe less of it — which is a dosimetry difference, not a mechanism difference.

> **VERIFIED quote — PMID:6871871** (Kerns 1983):
> "Squamous cell carcinomas were observed in the nasal cavities of 103 rats (52 females and 51 males) and 2 male mice exposed to 14.3 ppm and in 2 rats (one male and one female) exposed to 5.6 ppm of formaldehyde gas."

> **VERIFIED quote — PMID:6871871:**
> "Significant formaldehyde-induced lesions were restricted to the nasal cavity and proximal trachea. The distribution and severity of these lesions were concentration dependent."

That "restricted to the nasal cavity and proximal trachea" line is the strongest available support for the portal-of-entry principle, and it's verified — use it.

**Natural/veterinary disease:** Formalin is widely used in **aquaculture** as a parasiticide, so overdose toxicity in fish is a real veterinary entity. A published case of **formalin intoxication in a 13-year-old Thoroughbred gelding** (survived) exists in *Equine Veterinary Journal* 2024 ⚠️ UNVERIFIED — find the PMID; it would make a nice `evidence_source: MODEL_ORGANISM` item per your veterinary edge-case rule. Formaldehyde is also used in agricultural fumigation and feed preservation, so livestock exposure occurs.

**OMIA:** I found no naturally occurring Mendelian ADH5/ALDH2 clearance disorder catalogued in animals. Worth an explicit "not found" rather than silence.

**Comparative/evolutionary:** ADH5/GSNOR is **deeply conserved** — bacteria through mammals. Pontel's framing ("counteracted in mammals by a conserved protection mechanism") captures it. That conservation is itself an argument that endogenous formaldehyde has been a persistent selective pressure for a very long time; the drain evolved because the sink was always filling.

**Zoonotic potential:** N/A — it's a chemical.

---

## 15. Model Organisms

### Genetic models (the crown jewels of this entry)

| Model | Genotype | Phenotype recapitulated | Fidelity |
|---|---|---|---|
| **`Adh5^-/-` mouse** | Single tier-1 KO | Accumulates formaldehyde-DNA adducts; relatively mild alone | MODERATE — establishes the adduct claim |
| **`Adh5^-/-Fancd2^-/-` mouse** | Clearance + repair double KO | **HSC depletion → bone marrow failure**; hepatocyte and nephron karyomegaly and dysfunction; **all animals eventually develop fatal malignancies**. BMT rescued hematopoiesis *and* nephron function. | HIGH for the genotoxic arm |
| **`Adh5^-/-Aldh2^E506K/E506K` mouse** | The AMeD genocopy (E506K = mouse equivalent of human E504K) | Short lifespan, dwarfism, hematopoietic failure | HIGH for AMeD |
| **`Aldh2^-/-Adh5^-/-` mouse** (Dingler 2020) | Two-clearance-system KO | Greatly shortened lifespan, leukemia ⚠️ UNVERIFIED — PMID:33147438, **fetch the abstract** | — |
| **Patient-derived iPSC** (Mu 2021) | `ADH5^-/-` + `ALDH2*2` | Defective hematopoietic expansion, increased DNA damage; **partial rescue by ALDH2 agonist C1** | HIGH — human genetic background |
| **Chicken DT40** | `ADH5`/FA-pathway mutants | Formaldehyde hypersensitivity; used in Burgos-Barragan's folate work | MODERATE (IN_VITRO) |

For dismech: these belong in `animal_models:` (not `experimental_models:`) with `modeled_mechanisms` links. The `Adh5^-/-Fancd2^-/-` mouse is a `RECAPITULATES` link to the HSC-depletion node with two or three good `readouts`. The iPSC model goes in `experimental_models:` with a `RESCUES` link for the C1 arm — that's a textbook use of the `RESCUES` relationship.

### Induced/exposure models
- **F344 rat inhalation bioassay** (the Kerns design: 0 / 2.0 / 5.6 / 14.3 ppm, 6 h/day, 5 d/wk, 24 months) — the canonical carcinogenicity model
- B6C3F1 mouse inhalation (much less sensitive)
- **Nonhuman primate ¹³CD₂-formaldehyde inhalation** — the definitive exogenous-vs-endogenous adduct discrimination
- Rat/mouse oral gavage formalin models for corrosive injury
- In vitro: A549, BEAS-2B, primary nasal epithelial cells, CD34+ HSPCs, lymphoblastoid lines

### Model limitations — curate these, don't hide them
1. **Rodent nasal dosimetry ≠ human.** Obligate nose-breathing rats vs oronasal humans; tumor site differs (rat nasal cavity vs human nasopharynx). → `HUMAN_MODEL_MISMATCH`.
2. **No animal model reproduces formaldehyde-induced leukemia by inhalation.** The leukemia signal is epidemiologic; the mouse leukemia comes from *genetic* clearance failure (endogenous formaldehyde), not inhalation. Conflating those two is the single most common error in this literature. → `HUMAN_MODEL_MISMATCH` + `KNOWLEDGE_GAP`.
3. Rat tumors occur only at frankly cytotoxic concentrations, well above human occupational exposure — the low-dose extrapolation is genuinely contested.
4. Genetic KO models model the *endogenous* disease; they establish mechanism plausibility for the exposure disease but are not exposure models.
5. No good animal model of the acute corrosive ingestion syndrome.

**Resources:** MGI (`Adh5`, `Aldh2`, `Fancd2` alleles), IMPC, Alliance of Genome Resources, JAX/IMSR strain repositories, RGD, Cellosaurus (DT40), ZFIN.

---

## Curation notes for the dismech entry

A few things specific to your pipeline, since that's the point of this:

**Module conformance candidates.** This entry can plausibly declare parallel `conforms_to` against several existing modules — worth checking each rather than building a from-scratch graph:
- `fibrotic_response` — the late stricture/gastric-outlet-obstruction arm
- `genome_instability_mutation` — the DPC/adduct → mutator-phenotype arm (this looks like a strong fit)
- `myelosuppression` — HSC depletion → cytopenias, though that module is framed for cytotoxic *therapy*, so read it before wiring
- `tumor_promoting_inflammation` — the chronic nasal inflammation + regenerative proliferation → SCC route
- `drug_induced_nephrotoxicity` — probably NOT; the renal injury here is genotoxic/karyomegalic rather than the dose-dependent ATN pattern that module models

**A new module might be warranted:** *reactive aldehyde clearance failure* — ADH5/ALDH2 two-tier clearance → aldehyde accumulation → DNA/protein crosslinks → repair saturation → stem cell attrition. That pattern recurs across formaldehyde, acetaldehyde/alcohol, and Fanconi anemia, so it has the recurrence property a module needs. Worth raising with Harry before building.

**Evidence discipline flags:**
- **PMID:7265415** has NO ABSTRACT. Do not quote it. Cite in `notes` only.
- The Zhang forensic "blood fixation" mechanism is one case's hypothesis — `supports: PARTIAL` plus a `discussions:` entry, not a confident causal node.
- The formaldehyde→leukemia link needs `mechanistic_hypotheses` with competing groups, not a single asserted chain.
- Rodent quotes are `evidence_source: MODEL_ORGANISM` and must not be the sole support for a human phenotype.
- Everything I marked ⚠️ UNVERIFIED needs `just fetch-reference` + `just count-verified-snippets` before it goes near a PR.

**Verified-quote inventory** (safe to curate, subject to your own cache check): PMID:10962510 · PMID:35394178 · PMID:32686516 · PMID:26412304 · PMID:6871871 · PMID:28813411 · PMID:33355142.

**Needs fetching:** PMID:38614309 (paraphrased) · PMID:33512438 (fragments only) · PMID:33147438 (not fetched) · PMID:30701286 (not fetched) · the equine formalin case · the ICM formalin case series · the corrosive-ingestion meta-analysis.

---

## Sources

- [Toxicity of ingested formalin and its management — PMID:10962510](https://pubmed.ncbi.nlm.nih.gov/10962510/)
- [A fatal case of accidental oral formaldehyde poisoning and its pathomorphological characteristics — PMID:35394178](https://pubmed.ncbi.nlm.nih.gov/35394178/)
- [Formaldehyde toxicity reports from in vitro and in vivo studies — PMID:32686516](https://pubmed.ncbi.nlm.nih.gov/32686516/)
- [Endogenous Formaldehyde Is a Hematopoietic Stem Cell Genotoxin and Metabolic Carcinogen — PMID:26412304](https://pubmed.ncbi.nlm.nih.gov/26412304/)
- [Mammals divert endogenous genotoxic formaldehyde into one-carbon metabolism — PMID:28813411](https://pmc.ncbi.nlm.nih.gov/articles/PMC5714256/)
- [Digenic mutations in ALDH2 and ADH5 impair formaldehyde clearance and cause AMeD syndrome — PMID:33355142](https://pubmed.ncbi.nlm.nih.gov/33355142/)
- [Carcinogenicity of formaldehyde in rats and mice after long-term inhalation exposure — PMID:6871871](https://pubmed.ncbi.nlm.nih.gov/6871871/)
- [Characteristic phenotypes of ADH5/ALDH2 deficiency during childhood — PMID:38614309](https://pubmed.ncbi.nlm.nih.gov/38614309/)
- [Analysis of disease model iPSCs from patients with ADH5/ALDH2 deficiency — PMID:33512438](https://pubmed.ncbi.nlm.nih.gov/33512438/)
- [Two Aldehyde Clearance Systems Are Essential to Prevent Lethal Formaldehyde Accumulation — PMID:33147438](https://pubmed.ncbi.nlm.nih.gov/33147438/)
- [Formaldehyde poisoning. Rapid metabolism to formic acid — PMID:7265415 (no abstract)](https://pubmed.ncbi.nlm.nih.gov/7265415/)
- [ATSDR Medical Management Guidelines: Formaldehyde](https://wwwn.cdc.gov/TSP/MMG/MMGDetails.aspx?mmgid=216&toxid=39)
- [ATSDR Toxicological Profile for Formaldehyde (tp111)](https://www.atsdr.cdc.gov/toxprofiles/tp111.pdf)
- [OMIM #619151 — AMED Syndrome, Digenic](https://omim.org/entry/619151) *(403'd on fetch — open in a browser)*
- [IARC Monographs Vol. 100F / meeting report — formaldehyde](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1280402/)
- [IARC Mono 100F, Other Data Relevant to Carcinogenicity (endogenous blood levels)](https://www.ncbi.nlm.nih.gov/books/NBK326466/)
- [Evaluation of inhaled low-dose formaldehyde-induced DNA adducts and DNA–protein cross-links — PMID:30701286](https://pubmed.ncbi.nlm.nih.gov/30701286/)
- [N2-Hydroxymethyl-dG adducts in nasal epithelium and bone marrow of nonhuman primates after 13CD2-formaldehyde inhalation](https://pubs.acs.org/doi/10.1021/tx1004166)
- [Formaldehyde exposure and leukemia risk: comprehensive review + network toxicogenomics](https://link.springer.com/article/10.1186/s41021-021-00183-5)
- [Prevalence of Contact Allergy to Formaldehyde and Formaldehyde Releasers: systematic review & meta-analysis](https://pubmed.ncbi.nlm.nih.gov/42035787/) *(⚠️ verify this PMID exists)*
- [Occupational contact allergy to formaldehyde and formaldehyde releasers — PMID:18976378](https://pubmed.ncbi.nlm.nih.gov/18976378/)
- [Corrosive ingestion–induced esophageal injuries: systematic review and meta-analysis](https://www.sciencedirect.com/science/article/pii/S0039606025005100)
- [Immediate and long-term outcome of corrosive ingestion — PMID:31643028](https://pubmed.ncbi.nlm.nih.gov/31643028/)
- [Survival of formalin intoxication in a 13-year-old Thoroughbred gelding — Equine Vet J 2024](https://beva.onlinelibrary.wiley.com/doi/10.1111/evj.13982)
- [ICD-10-CM T59.2 — Toxic effect of formaldehyde](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T59-/T59.2X1A)
- [Updating the biologically based dose-response model for nasal carcinogenicity of inhaled formaldehyde in the F344 rat](https://academic.oup.com/toxsci/article/193/1/1/7076626)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.
