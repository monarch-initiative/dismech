---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-01T16:51:23.016289'
end_time: '2026-09-01T17:00:37.428748'
duration_seconds: 554.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ethylene Glycol Poisoning
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
  web_search_requests: 19
  num_turns: 44
  total_cost_usd: 4.785746250000001
  session_id: 54b62ddf-e529-40b0-945d-4c22e2abb9ab
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ethylene Glycol Poisoning
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ethylene Glycol Poisoning** covering all of the
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

I'll pull the local reference caches and the existing draft, then search the literature.

Cached EXTRIP systematic review is rich. Now the gaps: epidemiology, mechanism detail, veterinary disease, identifiers.

# Ethylene Glycol Poisoning — Disease Characteristics Research Report

**Compiled 2026-09-01. Target: MONDO:0017861.**

Ethylene glycol is not the poison. Its metabolites are. That single fact organizes everything below — the antidote, the latent period, the two separate organ injuries, and the reason a treated patient walks out and an untreated one does not.

Ontology identifiers marked ✅ were verified against this repository's committed term caches (`cache/hp`, `cache/go`, `cache/cl`, `cache/uberon`, `cache/chebi`, `cache/ncit`, `cache/mondo`, `cache/ncbitaxon`) or against the EBI Ontology Lookup Service during this session. Terms marked ⚠ are suggestions I did not verify.

---

## 1. Disease Information

Ethylene glycol poisoning is acute chemical injury from ingesting ethylene glycol, most often as automotive antifreeze, engine coolant, or de-icing fluid. The parent compound is a sweet, colorless, viscous diol. It is mildly intoxicating and little else. Hepatic alcohol dehydrogenase converts it to glycolate, which acidifies the blood, and then to oxalate, which precipitates with calcium in the kidney.

> "EG itself has minimal toxicity, but its metabolites are responsible for most of the clinical effects; glycolate contributes to the acidemia, while deposition of calcium oxalate crystals in tissues causes AKI and neurological complications" — Ghannoum et al., *Crit Care* 2023, PMID:36765419

### Identifiers

| Resource | Identifier | Status |
|---|---|---|
| MONDO | `MONDO:0017861` ethylene glycol poisoning | ✅ verified in `cache/mondo/terms.csv` |
| CHEBI (agent) | `CHEBI:30742` ethylene glycol | ✅ verified via OLS |
| CAS (agent) | 107-21-1 | from EPA hazard summary |
| MeSH (agent) | `D019855` Ethylene Glycol, tree `D02.033.455.250.268` | ✅ confirmed present via NCBI E-utilities MeSH search |
| ICD-10-CM | `T52.3X-` Toxic effect of glycols, 7th-character extensions by intent (`T52.3X1` accidental, `T52.3X2` intentional self-harm, `T52.3X3` assault, `T52.3X4` undetermined) | coding-level answer |
| ICD-10 (per MalaCards mapping) | `T52.8` | ⚠ conflicts with the Orphanet mapping to `T52.3`; resolve before binding |
| UMLS | `C0413194` | ⚠ from MalaCards, not verified at source |
| OMIM | not applicable — no Mendelian etiology | — |
| Orphanet | ⚠ a record appears at `orpha.net/en/disease/detail/31826`; the page would not render for me and I did not confirm the ORPHA number | unverified |
| ICD-11 | ⚠ not verified this session | unverified |

There is no MeSH disease descriptor. The literature is indexed as `Ethylene Glycol/poisoning`, which matters when you build a PubMed query.

**Synonyms and alternative names.** Ethylene glycol toxicity. Ethylene glycol intoxication. Antifreeze poisoning. Antifreeze ingestion. Glycol poisoning. Ethylene glycol toxicosis (the veterinary usage). Note the near-homonym trap: **diethylene glycol (DEG) poisoning is a different disease** with a different terminal metabolite (2-hydroxyethoxyacetic acid, not oxalate) and a different clinical signature dominated by delayed neuropathy. The 2022 Gambia and Uzbekistan pediatric mass poisonings were principally DEG events with EG co-contamination. Do not merge them.

**Data provenance.** The knowledge base for this disease is built almost entirely from individual-patient data — case reports, small retrospective chart reviews, and poison-center call records. The EXTRIP systematic review screened 1,296 articles, included 226, and found **no randomized controlled trials** (PMID:36765419). Aggregated disease-level resources exist for the chemical (ATSDR, EPA, NPDS annual reports) but not for the syndrome. Every treatment recommendation in the field rests on very low quality evidence by GRADE.

---

## 2. Etiology

### Causal factors

The cause is exposure. Ingestion is the route that matters. Inhalation and dermal contact from occupational use do not produce the syndrome at realistic exposures.

- **Deliberate self-poisoning.** The dominant adult mechanism. In the pooled EXTRIP case series (n = 446), median age was 42 years and 80% were male, with a median ingested dose of 250 mL (IQR 150–500).
- **Accidental ingestion.** Children and pets, drawn by the sweet taste. A Czech series of 86 accidental "1–3 swallow" ingestions had zero deaths (PMID:36765419, citing Krenova).
- **Ethanol substitution.** Drinking antifreeze as a cheap intoxicant, individually or in clusters.
- **Contaminated pharmaceuticals.** Glycol-adulterated syrup excipients. An outbreak, not a poisoning.
- **Occupational.** Aircraft de-icing generates EG vapor and mist. This has not produced the classic syndrome.

### Dose

A threshold dose is poorly defined and the often-quoted lethal dose is softer than it sounds.

> "The often-quoted lethal dose in an untreated 70 kg adult is 100 mL, although there are several cases of toxicity and even death below this dose." — PMID:36765419

> "Aircraft de-icing workers systemically exposed to an estimated 27 mg/kg from aerosolized EG (≈ 2 mL of pure EG) did not demonstrate any adverse effects." — PMID:36765419

Self-experiments with 10–30 mL of pure EG caused no harm. Toxicity did not occur in seven untreated patients with EG concentrations below 4.8 mmol/L (30 mg/dL). Some sources set a risk threshold at a peak concentration above 3.2 mmol/L (20 mg/dL).

### Risk factors

**Genetic.** None established. There is no causal variant, no susceptibility locus with a published association, and no GWAS. I searched for ADH1B / ADH1C / ALDH2 effects on toxic-alcohol handling and found only the well-worked ethanol literature. The inference that a high-activity ADH1B allele would accelerate bioactivation is biologically reasonable and, as far as I can find, **untested for ethylene glycol**. Record it as a hypothesis or not at all.

**Environmental and behavioral — the real risk set.**

| Factor | Direction | Note |
|---|---|---|
| Suicidal intent, psychiatric illness | ↑↑ | dominant adult mechanism |
| Alcohol use disorder | ↑ | substitute-intoxicant ingestion |
| Male sex | ↑ | 80% of pooled cases (PMID:36765419) |
| Household storage of antifreeze in unlabeled containers | ↑ | classic pediatric mechanism |
| Age under 5 years | ↑ | exploratory ingestion; sweet taste |
| Delay to treatment 6–12 h | ↑↑ | more metabolite formed before ADH is blocked |
| Pre-existing CKD | ↑ | reduced renal EG clearance, prolonged half-life |
| Access to fomepizole and dialysis | ↓↓ | the single largest determinant of survival |

### Protective factors

**Co-ingested ethanol is genuinely protective**, and this is the one protective factor with a mechanism you can draw.

> "EG toxicity is modulated by co-ingestion with ethanol because this decreases EG metabolism" — PMID:36765419

Ethanol is a competing ADH substrate. It is the antidote arriving before the diagnosis. Fifty-five percent of the pooled cohort had co-ingested ethanol, and notably the "late/severe" subgroup had *less* ethanol co-ingestion (36%) than the "early" subgroup (61%).

No genetic protective factor is known.

### Gene-environment interactions

None documented for humans. The interesting structural point is the mirror relationship with **primary hyperoxaluria**: PH1 (`MONDO:0009823` ✅, *AGXT*), PH2 (`MONDO:0009824` ✅, *GRHPR*), PH3 (`MONDO:0013327` ✅, *HOGA1*) are inherited failures of the same glyoxylate-handling node that ethylene glycol overwhelms acutely. Whether a PH carrier is more vulnerable to acute EG poisoning is unstudied. It is a well-posed question and I flag it as a knowledge gap, not a finding.

---

## 3. Phenotypes

Phenotypes sort by stage, and stage is a clock. That is the single most useful clinical fact about this disease.

### Neurologic / behavioral (0–12 h, and again at 5–20 days)

| Phenotype | HPO term | Frequency / note |
|---|---|---|
| Inebriation, ataxia | `HP:0001251` Ataxia ✅ | earliest sign; mimics ethanol |
| Altered mental status | `HP:0001289` Confusion ✅ | n = 237/446 pooled (53%) |
| Drowsiness | `HP:0002329` Drowsiness ✅ | early |
| Lethargy | `HP:0001254` Lethargy ✅ | early |
| Coma | `HP:0001259` Coma ✅ | n = 127/446 (28%); an EXTRIP dialysis indication |
| Seizure | `HP:0001250` Seizure ✅ | n = 44/446 (10%) |
| Encephalopathy | `HP:0001298` Encephalopathy ✅ | — |
| Cerebral edema | `HP:0002181` Cerebral edema ✅ | n = 10/446 (2%); crystal deposition in cerebral vessels |
| Nystagmus | `HP:0000639` Nystagmus ✅ | reported |
| Ophthalmoplegia | `HP:0000602` Ophthalmoplegia ✅ | delayed, cranial-nerve phase |
| Papilledema | `HP:0001085` Papilledema ✅ | with cerebral edema |
| Facial palsy | `HP:0010628` Facial palsy ✅ | **delayed sequela, day 5–20**; CN VII most common; may be bilateral |
| Peripheral neuropathy | `HP:0009830` Peripheral neuropathy ✅ | delayed sensorimotor; can be severe enough to cause complete paralysis |
| Tetany | `HP:0001281` Tetany ✅ | secondary to hypocalcemia |

Delayed neurologic disease is the part clinicians miss. Cranial neuropathies appear **8 to 18 days** after ingestion, especially in late presenters, and post-mortem work attributes them to localized inflammation around oxalate microcrystals. Recovery may take a year. Basal ganglia and brainstem injury are rare; MRI shows T2 hyperintensity in midbrain, hippocampi, basal nuclei, and thalami.

### Renal (12 h onward)

| Phenotype | HPO term | Frequency |
|---|---|---|
| Acute kidney injury | `HP:0001919` Acute kidney injury ✅ | **30–70%** across cohorts (PMID:36765419); n = 295/446 (66%) in the ECTR-selected pooled series |
| Oliguria | `HP:0100520` Oliguria ✅ | preceding anuria |
| Elevated creatinine | `HP:0003259` Elevated circulating creatinine concentration ✅ | appears ~12 h |
| Crystalluria | `HP:0020074` Crystalluria ✅ | calcium oxalate crystals, n = 85/446 |
| Hyperoxaluria | `HP:0003159` Hyperoxaluria ✅ | plasma oxalate peaked at 89 µmol/L (normal <6.3±1.1) on day 3, PMID:18696123 |
| Hematuria | `HP:0000790` Hematuria ✅ | — |
| Proteinuria | `HP:0000093` Proteinuria ✅ | — |
| Flank pain | `HP:0030157` Flank pain ✅ | — |
| Nephrocalcinosis | `HP:0000121` Nephrocalcinosis ✅ | PMID:18696123 — developed despite alkaline citrate prophylaxis |
| Renal insufficiency | `HP:0000083` Renal insufficiency ✅ | — |
| Chronic kidney disease | `HP:0012622` Chronic kidney disease ✅ | 16.8% at discharge, <5% at 6 months |

### Metabolic and laboratory (3–12 h)

| Phenotype | HPO term | Note |
|---|---|---|
| Metabolic acidosis | `HP:0001942` Metabolic acidosis ✅ | high anion gap; median lowest pH 7.08 (IQR 6.89–7.23) |
| Hypocalcemia | `HP:0002901` Hypocalcemia ✅ | calcium sequestered as oxalate |
| Hyperkalemia | `HP:0002153` Hyperkalemia ✅ | with AKI |
| Prolonged QT interval | `HP:0001657` Prolonged QT interval ✅ | consequence of hypocalcemia |

Median lowest bicarbonate 6.9 mmol/L. Median anion gap 32 mmol/L. Median osmol gap 40. Median peak glycolate 15.9 mmol/L. Patients have survived pH below 6.60.

### Cardiopulmonary and gastrointestinal

| Phenotype | HPO term | Note |
|---|---|---|
| Tachycardia | `HP:0001649` Tachycardia ✅ | — |
| Tachypnea | `HP:0002789` Tachypnea ✅ | Kussmaul respiration compensating acidosis |
| Hypertension | `HP:0000822` Hypertension ✅ | early cardiotoxic phase |
| Hypotension | `HP:0002615` Hypotension ✅ | n = 26/446; mortality marker |
| Respiratory failure | `HP:0002878` Respiratory failure ✅ | mortality marker; 155/446 ventilated |
| Pulmonary edema | `HP:0100598` Pulmonary edema ✅ | autopsy finding |
| Nausea | `HP:0002018` Nausea ✅ | — |
| Vomiting | `HP:0002013` Vomiting ✅ | — |
| Abdominal pain | `HP:0002027` Abdominal pain ✅ | can dominate a delayed presentation |

### Severity, progression, quality of life

Severity is **variable and dose-and-delay dependent**, not intrinsic. Progression is **acute and monophasic** in the metabolic phase, with a distinct **delayed relapse** in the neurologic phase. Nothing here is episodic or relapsing-remitting.

Quality-of-life data are absent. I found no EQ-5D, SF-36, or PROMIS study of ethylene glycol survivors. The functional burden that is documented is dialysis dependence (2.9% at discharge, under 1% at 6 weeks) and residual cranial or peripheral neuropathy taking up to a year to resolve. **This is a genuine gap in the literature, not a gap in my search.**

---

## 4. Genetic / Molecular Information

There is nothing here, and saying so plainly is the correct entry.

- **Causal genes:** none. This is an acquired toxic exposure. No OMIM entry, no ClinVar submissions, no gene panel.
- **Pathogenic variants:** not applicable.
- **Modifier genes:** none demonstrated. Plausible but untested candidates are *ADH1B*, *ADH1C*, *ALDH2*, *HAO1* (glycolate oxidase), *LDHA*, *AGXT*, and *GRHPR*.
- **Epigenetics:** no data.
- **Chromosomal abnormalities:** not applicable.

The genes that matter are the ones encoding the enzymes that *do the poisoning*, and they are wild-type. This is the pattern for a bioactivation toxicity: normal metabolism, abnormal substrate.

| Enzyme | Gene | Role |
|---|---|---|
| Alcohol dehydrogenase 1B | *ADH1B* (`hgnc:250` ⚠) | EG → glycolaldehyde; **the antidote target** |
| Aldehyde dehydrogenase 2 | *ALDH2* (`hgnc:404` ⚠) | glycolaldehyde → glycolate |
| Hydroxyacid oxidase 1 (glycolate oxidase) | *HAO1* (`hgnc:4809` ⚠) | glycolate → glyoxylate; **rate-limiting** |
| Lactate dehydrogenase A | *LDHA* (`hgnc:6535` ⚠) | glycolate → glyoxylate → oxalate |
| Alanine-glyoxylate aminotransferase | *AGXT* (`hgnc:341` ⚠) | glyoxylate → glycine; **detoxifying**, pyridoxine-dependent |

HGNC identifiers above are ⚠ — I did not resolve them this session. Verify before binding.

---

## 5. Environmental Information

**Environmental factors.** Ethylene glycol is the main component of commercial antifreeze and engine coolant, and is present in de-icing fluids, hydraulic fluids, brake fluid, and industrial solvents. It is manufactured at very large scale in the United States. Occupational exposure at airports is inhalational and dermal, from sprayed de-icing formulation generating vapor and mist. OSHA regulates workroom air at a maximum of 50 ppm, following the ACGIH guideline.

Ontology suggestions for exposure: I checked `cache/ecto/terms.csv` and **no ethylene glycol exposure term is currently cached in this repository**. The pattern to follow is `ECTO:0900004` exposure to arsenic via ingestion. An `exposure to ethylene glycol via ingestion` term needs an ECTO search before binding. Do not invent one.

**Lifestyle factors.** Alcohol use disorder, as a route to substitute-intoxicant ingestion. Storage practice — antifreeze decanted into a beverage container is the pediatric mechanism.

**Infectious agents.** Not applicable.

---

## 6. Mechanism / Pathophysiology

### The causal chain

1. **Ethylene glycol is ingested** and absorbed quickly and completely from the gastrointestinal tract. Bioavailability is 100% in rodent data. Protein binding is negligible. It distributes into total body water, volume of distribution 0.5–0.8 L/kg. **Leads to** a rising plasma concentration of an osmotically active, largely unmetabolized small molecule.

2. **Unmetabolized ethylene glycol produces CNS depression and an osmolal gap.** This is the whole of the parent compound's contribution. **Results in** inebriation and ataxia clinically indistinguishable from ethanol, and a raised measured-minus-calculated osmolality, with a normal anion gap.

3. **Hepatic alcohol dehydrogenase oxidizes ethylene glycol to glycolaldehyde.** One third of absorbed EG leaves unchanged in urine; two thirds are oxidized. **This is the committed step, and the only step any antidote blocks.** GO: `GO:0004022` alcohol dehydrogenase (NAD+) activity ✅. Substrate `CHEBI:30742` ✅ → product `CHEBI:17071` glycolaldehyde ✅.

4. **Aldehyde dehydrogenase rapidly converts glycolaldehyde to glycolate.** GO: `GO:0004029` aldehyde dehydrogenase (NAD+) activity ✅. Product `CHEBI:29805` glycolate ✅. Glycolaldehyde is transient and does not accumulate.

5. **Glycolate accumulates and drives high anion gap metabolic acidosis.** It piles up because the *next* step is slow. **Results in** the acidemia that appears "after a latent period of approximately 3–6 h after ingestion" (PMID:36765419). Glycolate concentration, not EG concentration, is what predicts outcome — the EXTRIP mortality break sits at 12 mmol/L.

6. **Glycolate oxidase converts glycolate to glyoxylate. This is the rate-limiting step.** Lactate dehydrogenase performs the same conversion, glycolate resembling lactate. GO: `GO:0003973` (S)-2-hydroxy-acid oxidase activity ✅. Product `CHEBI:36655` glyoxylate ✅.
   - *Side consequence, diagnostically loud:* glycolate's structural similarity to lactate makes point-of-care lactate-oxidase analyzers read it as lactate. The discrepancy between a point-of-care and a laboratory lactate — the **lactate gap** — is a real bedside clue derived directly from the mechanism. The size of the artifact is analyzer-dependent: one comparison found massive false elevation on a Radiometer 700 and elevations ≤4 mmol/L on iSTAT and Bayer analyzers even at 40 mmol/L glycolate.

7. **Glyoxylate branches three ways.** This is the therapeutic fork.
   - **Toxic branch:** glyoxylate → **oxalate** (`CHEBI:132952` ✅), largely via LDH. GO: `GO:0033610` oxalate biosynthetic process ✅.
   - **Detoxifying branch A:** glyoxylate → glycine, via alanine-glyoxylate aminotransferase. GO: `GO:0008453` L-alanine:glyoxylate transaminase activity ✅. **Pyridoxine-dependent** (`CHEBI:16709` pyridoxine ✅).
   - **Detoxifying branch B:** glyoxylate → α-hydroxy-β-ketoadipate. **Thiamine-dependent** (`CHEBI:18385` thiamine(1+) ✅).
   - The cofactor rationale is why thiamine and pyridoxine are given. **The rationale is all there is.** "Thiamine and pyridoxine are used to facilitate the conversion of glyoxylate to non-toxic metabolites rather than oxalate, but their clinical utility has never been determined." (PMID:36765419)

8. **Oxalate binds calcium and precipitates as calcium oxalate monohydrate.** `CHEBI:60579` calcium oxalate ✅. Precipitation happens preferentially in the proximal tubule, where water reabsorption concentrates the filtrate to supersaturation. **Leads to** two separate injuries: mechanical/chemical damage to the tubule, and systemic calcium depletion.

9. **Calcium oxalate monohydrate crystals — not the oxalate ion — kill proximal tubular epithelial cells.** This is the mechanistic result to cite, and it is a clean one.

   > "In rat red blood cells, oxalate ions showed no hemolytic effect, while crystals produced concentration-dependent hemolysis. Human proximal tubule cells exposed to crystal suspensions above 3 mM exhibited cytotoxicity through lactate dehydrogenase release, whereas oxalate solutions prevented cytotoxicity when EDTA blocked crystal formation." — Guo & McMartin, *Toxicology* 2005, PMID:15695020 (evidence source: IN_VITRO)

   The same work found that **acidosis enhances crystal toxicity to human cells, while glycolate does not**. So step 5 is not merely parallel to step 9 — it potentiates it. Draw that edge.

10. **Proximal tubular epithelial cell death produces acute kidney injury.** Renal tubular epithelial necrosis with calcium oxalate crystals in the tubular lumina is the characteristic histology. **Results in** oliguria and then anuria.

11. **Acute kidney injury feeds back on step 1.** One quarter of total EG clearance is renal and directly proportional to GFR. Losing kidney function prolongs the EG half-life. **This is a self-amplifying loop**, and it is why AKI predicts death: "AKI is a marker of metabolite-mediated organ injury, and it delays kidney excretion of EG. Death very seldom occurs if AKI is not present." (PMID:36765419)

12. **Calcium sequestration produces hypocalcemia**, and hypocalcemia produces tetany, seizures, and QT prolongation. A parallel branch off step 8, not downstream of the kidney.

13. **Crystals deposit in cerebral vessels and meninges.** Birefringent crystals have been demonstrated within the walls of CNS blood vessels at autopsy, with associated inflammation and edema. **Leads to** cerebral edema, and rarely to basal ganglia and brainstem injury.

14. **Late crystal deposition around cranial nerves produces delayed neuropathy**, day 5–20, most often CN VII, attributed post-mortem to localized inflammation around oxalate microcrystals. This branch runs on a different clock from everything above and appears **after** the metabolic crisis is treated.

### Where the mechanism is inferred rather than demonstrated

Steps 1–10 are demonstrated. Step 13 rests on autopsy correlation. Step 14 rests on post-mortem inference plus timing — the inflammatory link is proposed, not proven in life. The specific inflammatory effector downstream of crystal contact (NLRP3 inflammasome assembly, `GO:0044546` ✅) is well worked out for calcium oxalate in the *nephrolithiasis* literature but I did not find it demonstrated for acute EG poisoning. Mark it as a hypothesis if you model it.

### Supporting categories

- **Molecular pathways:** glyoxylate and dicarboxylate metabolism (KEGG map00630). GO: `GO:0046487` glyoxylate metabolic process ✅, `GO:0019532` oxalate transport ✅.
- **Cellular processes:** necrotic and apoptotic proximal tubular cell death (`GO:0006915` apoptotic process ✅, `GO:0008219` cell death ✅), oxidative stress response (`GO:0034599` cellular response to oxidative stress ✅), inflammatory response (`GO:0006954` ✅), mitochondrial permeability transition (`GO:0005757` mitochondrial permeability transition pore complex ✅).
- **Protein dysfunction:** none. No protein is misfolded or mutated. The enzymes work correctly on the wrong substrate. This is an important negative for a knowledge base built around protein defects.
- **Metabolic changes:** high anion gap acidosis from glycolate; secondary lactate elevation; NADH/NAD+ shift from two consecutive dehydrogenase steps.
- **Immune involvement:** secondary crystal-associated inflammation only. No autoimmunity, no immunodeficiency.
- **Tissue damage mechanisms:** crystal-mediated membrane damage, necrosis, acidosis-potentiated cytotoxicity, tubular obstruction.
- **Molecular profiling:** no human transcriptomic, proteomic, or metabolomic study of EG-poisoned patients that I located. Rat hyperoxaluria/nephrolithiasis transcriptomics exist (inflammatory changes tracking crystal deposition) but describe the *model*, not the poisoning. **Do not import those as human evidence.**
- **Single-cell, spatial, multi-omics, CRISPR screens:** none for this disease.

---

## 7. Anatomical Structures Affected

### Organ level

| Structure | UBERON | Role |
|---|---|---|
| Kidney | `UBERON:0002113` ✅ | **primary target organ** |
| Liver | `UBERON:0002107` ✅ | site of bioactivation, not of injury |
| Brain | `UBERON:0000955` ✅ | edema, focal injury |
| Meninx | `UBERON:0002360` ✅ | crystal deposition at autopsy |
| Basal ganglion | `UBERON:0002420` ✅ | rare focal injury, MRI T2 hyperintensity |
| Facial nerve | `UBERON:0001647` ✅ | delayed cranial neuropathy, CN VII |
| Lung | `UBERON:0002048` ✅ | pulmonary edema, secondary |
| Heart | `UBERON:0000948` ✅ | tachycardia, QT prolongation, secondary |

The liver is worth a note. It is where the poison is made and it is not where the damage lands. That dissociation is the whole shape of the disease.

Body systems: renal/urinary (primary), nervous (primary and delayed), cardiovascular (secondary), respiratory (secondary), musculoskeletal via tetany (secondary).

### Tissue and cell level

| Cell type | CL | Note |
|---|---|---|
| Epithelial cell of proximal tubule | `CL:0002306` ✅ | **the dying cell** |
| Kidney proximal convoluted tubule epithelial cell | `CL:1000838` ✅ | more specific alternative |
| Kidney tubule cell | `CL:1000507` ✅ | broader |
| Hepatocyte | `CL:0000182` ✅ | bioactivation site |
| Kidney resident macrophage | `CL:1000698` ✅ | crystal-associated inflammation — inferred |
| Macrophage | `CL:0000235` ✅ | general |

Tissue types: renal tubular epithelium (primary), vascular endothelium in CNS vessels, meningeal connective tissue, peripheral nerve.

### Subcellular level

Extracellular and luminal crystal deposition is the dominant compartment — the crystals sit in the tubular lumen and contact the apical membrane. Intracellular consequences reported are mitochondrial injury and membrane damage (`GO:0005757` mitochondrial permeability transition pore complex ✅). Guo & McMartin document "membrane damage and organelle injury" (PMID:15695020).

### Localization and lateralization

Renal involvement is **bilateral and symmetric** — it is a filtered toxin, not a focal lesion. Cerebral involvement is diffuse (edema) with occasional bilateral deep-grey focal lesions. Cranial neuropathy is the exception: it may be **unilateral or bilateral**, and unilateral facial nerve paralysis has been reported as an isolated presenting feature.

---

## 8. Temporal Development

### Onset

Any age. Onset is **acute** and the interval from exposure to first symptom is 30 minutes to a few hours. Median time from ingestion to hospital admission in the pooled EXTRIP series was 10 hours (IQR 4–18) — 6 hours for the early group, 12 for the late group. That six-hour difference is most of the prognosis.

### The three stages

| Stage | Window | Dominant feature | Labs |
|---|---|---|---|
| 1 — Neurologic | 0–12 h (StatPearls: 0–4 h) | inebriation, ataxia, vomiting | **elevated osmolar gap, normal anion gap** |
| 2 — Cardiopulmonary / metabolic | 4–12 h (acidemia from 3–6 h) | tachycardia, tachypnea, hypertension then hypotension, coma, seizures | **high anion gap acidosis**, osmolar gap falling |
| 3 — Renal | 12 h onward | oliguria, flank pain, AKI | rising creatinine, crystalluria, hypocalcemia |
| 4 — Delayed neurologic | day 5–20 | cranial neuropathy, peripheral neuropathy | may be normal |

> "During this time, there is often an elevated osmolar gap without an elevated anion gap." — StatPearls, NBK537009, stage 1

> "An anion gap metabolic acidosis develops secondary to the accumulation of glycolic acid." — StatPearls, stage 2

The two gaps trade places as the parent compound is consumed. That crossover is the diagnostic signature and also the trap: **a patient presenting late has a normal osmolar gap and is sicker, not safer.**

### Progression, duration, remission

Progression is rapid without treatment and arrested by treatment. Course is **self-limited if the exposure is single and the antidote is given** — this is not a chronic disease. Duration of the acute illness: median hospital stay 16 days (IQR 7–23), ICU stay 5 days.

Recovery timings:

| Endpoint | Median | Source |
|---|---|---|
| AKI duration | 7–10 days | PMID:36765419 |
| Kidney replacement therapy for AKI | 9 days (IQR 3–14) | PMID:36765419 |
| Creatinine normalization after AKI | 21 days (IQR 7–40) | PMID:36765419 |
| Plasma oxalate normalization (pediatric case) | day 7 after ingestion | PMID:18696123 |
| Time to death, when death occurs | 96 h (IQR 24–264) | PMID:36765419 |
| Cranial nerve recovery | up to 1 year | delayed-sequelae literature |

Remission is treatment-induced. Spontaneous recovery occurs after small ingestions.

### Critical periods

The intervention window is **before glycolate accumulates**. That is the whole therapeutic proposition, and it is the strongest mechanistic statement in the disease:

> "Administered early, fomepizole prevents EG-related renal failure and methanol-related visual and neurological injuries. When administered prior to the onset of significant acidosis or organ injury, fomepizole may obviate the need for hemodialysis." — Mégarbane, *Open Access Emerg Med* 2010, PMID:27147840

A delay of 6–12 hours between ingestion and treatment is associated with increased immediate and long-term complications in several studies, though not confirmed in others (PMID:36765419).

---

## 9. Inheritance and Population

### Epidemiology

United States poison-center figures, cited inside the EXTRIP review from NPDS:

> "In 2020, the US poison control centers reported 6036 calls relating to EG, 586 of which had at least moderate clinical effects and 30 of which resulted in death" — PMID:36765419

StatPearls reports 6,374 case mentions in 2016, of which 686 involved children under 12.

I checked the 2023 NPDS annual report (PMID:39688840). Its abstract reports 2,080,659 human exposures and 3,272 exposure-related deaths overall but **carries no ethylene-glycol-specific figure**; the substance tables are behind the paywalled full text. So the most recent EG-specific national count I can cite is 2020.

Rough rates on a US population of ~330 million: **~1.8 calls per 100,000 per year**, of which ~0.18 per 100,000 have at least moderate effects and ~0.009 per 100,000 die. Treat these as my arithmetic on the 2020 figure, not as a published rate.

No incidence or prevalence figure exists in Orphanet, GBD, or WHO for this as a named disease. A Polish national health-fund study identified 174 ICD-10-coded cases in 2010 with 47 deaths (PMID:36765419, citing Swiderska), and a Romanian multicenter series captured 56 confirmed cases across 2012–2017 during "a large EG poisoning epidemic."

### Inheritance

Not applicable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency. All these fields are correctly empty for this entry.

### Population demographics

| Variable | Value | Source |
|---|---|---|
| Median age | 42 years (IQR 28–52) | PMID:36765419, n = 446 |
| Male fraction | 80% | PMID:36765419 |
| Male fraction, severe/late subgroup | 84% | PMID:36765419 |
| Male fraction, early subgroup | 67% | PMID:36765419 |
| Children under 12 (US, 2016) | 686 of 6,374 case mentions | StatPearls |

The sex skew is roughly 4:1 male, and it widens with severity. That is consistent with the mechanism being deliberate self-poisoning rather than exposure.

**Geographic distribution.** Not endemic. Distribution tracks antifreeze availability, poison-center coverage, and antidote access. High mortality persists where fomepizole and dialysis are not readily available. Cluster events are the exception to the sporadic pattern: mass ingestion at a US military base in 2023 (11 soldiers over 12 hours, all survived — *Mil Med* 2023), and pharmaceutical-contamination outbreaks with much higher lethality.

**Age distribution.** Bimodal in shape — a small pediatric accidental peak under 5, and a large adult peak in the fourth and fifth decades.

---

## 10. Diagnostics

### Laboratory

| Test | LOINC / note | Interpretation |
|---|---|---|
| Serum ethylene glycol, gas chromatography | reference lab, hours to days turnaround | confirmatory; often too slow to guide the first dose |
| Plasma glycolate | rarely available; **the best prognostic analyte** | >12 mmol/L → dialysis (EXTRIP strong rec) |
| Osmolality, measured vs calculated | osmolal gap | raised early, **normal late** |
| Basic metabolic panel | anion gap | Na⁺ + K⁺ − Cl⁻ − HCO₃⁻; >27 mmol/L → dialysis |
| Arterial blood gas | pH, HCO₃⁻ | median lowest pH 7.08 in pooled series |
| Serum calcium | `HP:0002901` | hypocalcemia supports the diagnosis |
| Creatinine | `HP:0003259` | rises from ~12 h |
| Urine microscopy | calcium oxalate crystals | **supportive, not diagnostic** — sensitivity poor, seen in only 85/446 |
| Point-of-care vs laboratory lactate | **lactate gap** | glycolate cross-reacts with lactate-oxidase POC assays |

Calculated osmolarity: `2[Na] + BUN/1.6 + glucose/18 + ethanol/4.6` (StatPearls).

Two cautions that matter more than the tests themselves. First, **a normal osmolal gap never excludes poisoning** — early presenters may have a normal gap and consequential ingestions, and late presenters have converted the gap into an anion gap. Second, **the lactate gap is analyzer-dependent**; a hospital whose POC device is an iSTAT will not see the artifact that a Radiometer 700 shows.

Also note: urine fluorescence under Wood's lamp, from the sodium fluorescein added to some antifreeze, is widely taught and **unreliable**. I did not find supporting evidence for it in this session's sources and would not curate it as a diagnostic without one.

A glycerol-dehydrogenase-based enzymatic EG assay has been reported with accuracy comparable to gas chromatography and faster turnaround (Filip et al.). This is the main recent diagnostic advance.

### Imaging and electrophysiology

Brain MRI in acute poisoning shows T2 hyperintensity in midbrain, hippocampi, basal nuclei, and thalami. CT may show rapid cerebral edema. ECG for QT prolongation from hypocalcemia. Nerve conduction studies for the delayed neuropathy. Renal ultrasound is nonspecific.

### Biopsy and pathology

Renal tubular epithelial necrosis with birefringent calcium oxalate crystals in tubular lumina. Confocal laser scanning microscopy has been used to characterize crystals in a fatal case. Biopsy is not required for diagnosis and is mostly a post-mortem finding.

### Genetic testing

Not applicable at every level — no WGS, WES, panel, single-gene, CMA, karyotype, FISH, mtDNA, or repeat-expansion indication. Leave these fields empty.

### Omics-based diagnostics

None in clinical use.

### Clinical criteria and differential

There is no formal consensus diagnostic criterion set. Diagnosis is history plus the gap profile plus, when obtainable, a confirmatory concentration.

Differential diagnosis for high-anion-gap metabolic acidosis with altered mental status:

| Condition | Distinguishing feature |
|---|---|
| Methanol poisoning (`MONDO:0017860` ✅) | visual loss, putaminal necrosis; **no** oxalate crystals, no AKI early |
| Diethylene glycol poisoning | delayed severe neuropathy; **no** oxalate; different metabolite |
| Diabetic ketoacidosis | ketones, hyperglycemia |
| Lactic acidosis / metformin | true lactate elevated on **both** POC and lab assay — no lactate gap |
| Salicylate poisoning | mixed respiratory alkalosis, tinnitus |
| Isopropanol ingestion | osmolal gap, ketosis, **no acidosis** |
| Propylene glycol (iatrogenic) | lorazepam/diazepam infusion history |
| Uremic acidosis | chronic, no osmolal gap |
| 5-oxoprolinuria | chronic acetaminophen, malnutrition |

The discriminator against methanol is renal: EG kills the kidney and spares the eye; methanol does the reverse.

### Screening

No population screening exists and none is indicated. Case-finding is presentation-driven.

---

## 11. Outcome / Prognosis

### Mortality

Mortality has fallen by an order of magnitude and the fall is the story.

| Era | Mortality | Source |
|---|---|---|
| Pre-1960 | >80% | PMID:36765419 |
| 1970s–1980s | 30–40% | PMID:36765419 |
| 1990s | declining | PMID:36765419 |
| Present day | **<10%** | PMID:36765419 |

The EXTRIP pooled patient-level cohort (n = 446) had **18.7% mortality** overall. That figure is higher than contemporary practice because the cohort is case-report-derived and dialysis-selected. Read it stratified instead:

| Group | Definition | Mortality |
|---|---|---|
| Early EG poisoning | glycolate ≤12 mmol/L **or** anion gap ≤28 mmol/L (n = 84) | **3.6%** |
| Late EG poisoning | glycolate >12 mmol/L **or** anion gap >28 mmol/L (n = 147) | **20.4%** |

> "In the subgroup of patients with a glycolate concentration ≤ 12 mmol/L (or anion gap ≤ 28 mmol/L), mortality was 3.6%; in this subgroup, outcomes in patients receiving ECTR were not better than in those who did not receive ECTR." — PMID:36765419

Median time to death is 96 hours after ingestion. There is no 5-year or 10-year survival concept — survivors of the acute event have normal life expectancy absent residual CKD.

### Morbidity, disability, recovery

| Sequela | At discharge | On extended follow-up |
|---|---|---|
| Any CKD | 16.8% | <5% at 6 months |
| Dialysis-dependent CKD | 2.9% | <1% at 6 weeks |
| CNS sequelae | 3.3% | rare persistence |

> "Persisting sequelae are unusual in survivors. AKI lasts approximately 7–10 days and kidney function returns to baseline in most patients." — PMID:36765419

EXTRIP is explicit that the discharge figures overestimate, because follow-up was short. Long-term dialysis dependence after one year is a rare-case-report phenomenon. Overall incidence of persisting sequelae "appears to be less than 1%."

Recovery potential is **excellent with early treatment and good even with late treatment if the patient survives the acidosis**. Patients have survived pH below 6.60, bicarbonate below 2 mmol/L, ingestions above 1 L, and EG concentrations above 200 mmol/L.

### Prognostic factors

| Factor | Effect | Strength |
|---|---|---|
| Plasma glycolate concentration | **strongest** | mortality break at 12 mmol/L |
| Anion gap | strong | break at 27–28 mmol/L |
| Presence of AKI | strong | "Death very seldom occurs if AKI is not present" |
| Coma | strong | repeatedly replicated |
| Respiratory failure | strong | |
| Hypotension | strong | |
| Seizures | strong | |
| Arterial pH | strong | |
| **Plasma EG concentration** | **weak** | "poorly predictive of mortality" |
| **Reported ingested dose** | **weak** | prognostic only if treatment is delayed |

That last pair is the counterintuitive and important one. The concentration of the poison you can measure fastest tells you the least. EXTRIP recommends *against* dialysis based on reported dose alone.

**Prognostic biomarker:** plasma glycolate. It is the right analyte and it is the one most hospitals cannot measure. Anion gap is the surrogate.

### Complications

Acute kidney injury; anion gap metabolic acidosis; cerebral edema; seizures; hypocalcemic tetany and QT prolongation; multi-organ failure; nephrocalcinosis; cranial and peripheral neuropathy; chronic kidney disease; anoxic brain injury.

Procedure-related complications are real and are counted separately by EXTRIP. Central venous catheter insertion carries a 0.1–2.1% serious complication rate. Hemodialysis and CKRT serious complications run about 0.005%; hemoperfusion 1.9%. Ethanol as antidote causes altered consciousness in 5–15%, bradycardia in 10–12%, and hypoglycemia in 16% of children. Fomepizole causes rare anaphylaxis, bradycardia, hypotension.

---

## 12. Treatment

### Pharmacotherapy — antidotes

**Fomepizole (4-methylpyrazole)** is first-line. `CHEBI:5141` fomepizole ✅.

> "Fomepizole, a potent alcohol dehydrogenase (ADH) inhibitor, is an efficient and safe antidote that prevents or reduces toxic EG and methanol metabolism. Although no study has compared its efficacy with ethanol, fomepizole is recommended as a first-line antidote." — PMID:27147840

Dosing (PMID:27147840; StatPearls concurs):
- Loading dose **15 mg/kg**, IV or oral, independent of alcohol concentration
- Then **10 mg/kg every 12 hours** for four doses (increase to 15 mg/kg thereafter for prolonged therapy)
- Continue until alcohol concentration is **<30 mg/dL**
- **During dialysis: 1 mg/kg/h continuous infusion**, or dose every 4 hours — fomepizole is itself dialyzed, with an on-dialysis half-life of 1.5–3.0 h and extracorporeal clearance above 100 mL/min
- No concentration monitoring needed
- Contraindicated in pyrazole allergy; safe in children; not recommended in pregnancy

The pivotal trial is Brent et al., *N Engl J Med* 1999;340(11), **PMID:10080845** — 19 patients with plasma EG ≥20 mg/dL. Conclusion: fomepizole administered early prevents renal injury by inhibiting formation of toxic metabolites.

**Ethanol** is the alternative where fomepizole is unavailable. `CHEBI:16236` ethanol ✅. It competes with EG for ADH, but binds less avidly, requires concentration monitoring to a target near 100–150 mg/dL, and carries sedation, hypoglycemia, and bradycardia risk. Ethanol prolongs the EG half-life to 8.5–14 h; fomepizole prolongs it to 12–18 h.

### Adjuncts

| Agent | Rationale | Evidence |
|---|---|---|
| **Thiamine** (`CHEBI:18385` ✅, `NCIT:C874` ✅) | shunts glyoxylate to α-hydroxy-β-ketoadipate | **none** — "clinical utility has never been determined" |
| **Pyridoxine** (`CHEBI:16709` ✅) | shunts glyoxylate to glycine | **none** |
| **Sodium bicarbonate** | corrects acidemia; acidosis potentiates crystal cytotoxicity (PMID:15695020) | mechanistic; 196/446 received it |
| **Alkaline citrate** | raises urinary oxalate solubility | one pediatric case; **nephrocalcinosis developed anyway** (PMID:18696123) |
| **Calcium replacement** | corrects hypocalcemia | supportive; use cautiously, it feeds crystal formation |

Be honest in the entry about thiamine and pyridoxine. They are given because the mechanism says they should work, not because anyone has shown they do.

### Extracorporeal treatment

EXTRIP recommendations, all at very low quality of evidence (PMID:36765419):

| Indication | Recommendation |
|---|---|
| Reported dose alone | **recommend against** dialysis |
| EG >50 mmol/L (>310 mg/dL), fomepizole used | **suggest** dialysis |
| EG >50 mmol/L, ethanol used | **recommend** dialysis |
| EG 20–50 mmol/L, ethanol used | **suggest** dialysis |
| EG >10 mmol/L (>62 mg/dL), no antidote | **recommend** dialysis |
| Osmol gap >50 (fomepizole) | **suggest**; (ethanol) **recommend** |
| Osmol gap >10, no antidote | **recommend** |
| **Glycolate >12 mmol/L** | **recommend** |
| Glycolate 8–12 mmol/L | **suggest** |
| **Anion gap >27 mmol/L** | **recommend** |
| Anion gap 23–27 mmol/L | **suggest** |
| Coma | **recommend** |
| Seizures | **recommend** |
| AKI, KDIGO stage 2 or 3 | **recommend** |
| CKD, eGFR <45 mL/min/1.73 m² | **suggest** |

Modality: intermittent hemodialysis first, CKRT if IHD is unavailable. Cessation: stop when anion gap <18 mmol/L; suggest stopping when EG <4 mmol/L (25 mg/dL) or acid-base is corrected.

Dialyzability: EG is *dialyzable* by IHD (level B), glycolate *dialyzable* (level C), EG *moderately dialyzable* by CKRT (level D), *slightly dialyzable* by peritoneal dialysis (level C) and hemoperfusion (level D). Hemodialysis clearance can exceed 200 mL/min and mass removal can exceed 100 g in a 6-hour session. Rebound occurred in 21% of the cohort, median 30% of the immediate post-dialysis concentration.

**Fomepizole may replace dialysis in the right patient.** In a French series, five patients with EG concentrations from 46.5 to 345 mg/dL treated with fomepizole alone and no dialysis developed no renal injury. The EXTRIP evidence table for early poisoning found no reduction in mortality, dialysis dependence, neurological damage, or short-term dialysis need when dialysis was added to fomepizole — only reduced cost and length of stay. That is a change in the standard of care and should be curated as such.

### Not applicable

Gene therapy, cell therapy, RNA therapeutics, targeted therapy, immunotherapy, and surgery are all not applicable. Kidney transplantation (`NCIT:C15265` ✅) is relevant only for the rare survivor with irreversible ESKD. Rehabilitation applies to residual neuropathy.

### NCIT treatment terms

| Treatment | NCIT | Status |
|---|---|---|
| Pharmacotherapy (antidote administration) | `NCIT:C15986` | ✅ |
| Hemodialysis | `NCIT:C15248` | ✅ |
| Dialysis | `NCIT:C15221` | ✅ |
| Renal Replacement Therapy | `NCIT:C126400` | ✅ |
| Supportive Care | `NCIT:C15747` | ✅ |
| Mechanical Ventilation | `NCIT:C70909` | ✅ |
| Invasive Mechanical Ventilation | `NCIT:C191573` | ✅ |
| Kidney Transplantation | `NCIT:C15265` | ✅ |
| Thiamine (agent) | `NCIT:C874` | ✅ |

Fomepizole and pyridoxine have no NCIT term in this repository's cache — bind them as `therapeutic_agent` with the CHEBI identifiers above under a `NCIT:C15986` action term.

### Treatment algorithm

Suspect on history or an unexplained anion gap. Give fomepizole immediately, before any concentration returns — "Treatment should be started as soon as possible, based on history and initial findings including anion gap metabolic acidosis, while awaiting measurement of alcohol concentration" (PMID:27147840). Correct acidemia. Then decide about dialysis on the glycolate or anion gap, not the EG level. Adjust the antidote dose upward during dialysis. Watch for rebound after stopping. Then watch again at day 5 to 20 for the neuropathy nobody was expecting.

**Pharmacogenomics:** none established.

---

## 13. Prevention

### Primary prevention

- **Bittering agents.** Denatonium benzoate added to antifreeze at 30–50 ppm. Oregon mandated it first for consumer automotive products with ≥10% EG; seventeen states followed; a voluntary US industry agreement extended it nationally in 2012. **The evidence that it works is negative.** The Oregon Poison Center recorded 332 EG and 117 methanol exposures among preschool children from 1987–2003 with *no change in annual frequency* after the 1995 mandate (see PMID:15171494, "Was it necessary to add Bitrex (denatonium benzoate) to automotive products?"). The Consumer Product Safety Commission has questioned its effectiveness. Cost is 2–3 cents per gallon. Curate this as an intervention with equivocal-to-absent evidence, not as a success.
- **Product substitution.** Propylene glycol antifreeze, materially less toxic.
- **Storage and labeling.** Never decant into beverage containers. The pediatric and veterinary mechanisms are almost entirely storage failures.
- **Pharmaceutical excipient quality control.** After the Gambia and Uzbekistan events, WHO issued medical product alerts on glycol-contaminated syrups. This is the intervention with the largest attributable mortality reduction available globally.
- **Occupational controls.** OSHA workroom air maximum 50 ppm per ACGIH; skin and eye protection for de-icing crews.
- **Means restriction and mental health care.** The dominant adult mechanism is self-harm, so this is the highest-yield primary prevention and the one least often listed.

### Secondary prevention

Early recognition. Poison center consultation. Rapid antidote access — stocking fomepizole is itself a preventive measure against renal injury, since the antidote given before acidosis prevents the disease rather than treating it.

### Tertiary prevention

Adequate ADH blockade continued through and after dialysis, to prevent glycolate reaccumulation. Monitoring for rebound. Follow-up renal function at 6 weeks and 6 months. Surveillance for delayed neuropathy through day 20.

### Not applicable

Immunization, genetic screening, carrier screening, preimplantation diagnosis, prenatal testing, genetic counseling, prophylactic medication. All empty for this entry.

---

## 14. Other Species / Natural Disease

Ethylene glycol toxicosis is a major veterinary emergency, and the veterinary literature is in some respects better than the human literature because the exposures are unintentional and the dosing is known.

### Taxonomy

| Species | NCBITaxon | Note |
|---|---|---|
| Homo sapiens | `NCBITaxon:9606` ✅ | |
| Canis lupus familiaris | `NCBITaxon:9615` ✅ | common natural disease |
| Felis catus | `NCBITaxon:9685` ✅ | **most susceptible** |
| Rattus norvegicus | `NCBITaxon:10116` ✅ | experimental |
| Mus musculus | `NCBITaxon:10090` ✅ | experimental, less sensitive |

> "All animals are susceptible to ethylene glycol toxicosis; however, dogs and cats are most commonly affected." — Merck Veterinary Manual

### Comparative dose and course

| | Cat | Dog | Human |
|---|---|---|---|
| Minimum lethal dose | **1.4 mL/kg** | 4.4–6.6 mL/kg | ~100 mL in a 70 kg adult (~1.4 mL/kg), often quoted, frequently violated |
| Early phase | 30 min – 12 h | 30 min – 12 h | 0–12 h |
| Renal failure onset | **12–24 h** | 36–72 h | >12 h |
| POC test detection limit | 20 mg/dL | 50 mg/dL | — |
| Fomepizole loading dose | **125 mg/kg** | 20 mg/kg | 15 mg/kg |

The cat is the outlier in both directions. It needs a third the dose to die and roughly eight times the fomepizole per kilogram to be saved. Cats also collapse into oliguric renal failure a day or two before dogs do.

Dog fomepizole protocol: 20 mg/kg IV initially, then 15 mg/kg at 12 and 24 h, then 5 mg/kg at 36 h. Cat protocol: 125 mg/kg initially, then 31.3 mg/kg at 12, 24, and 36 h. Ethanol (20% IV) is the alternative in both.

### Comparative pathology

> "Renal tubular epithelial necrosis with calcium oxalate crystals in the tubular lumina is characteristic." — Merck Veterinary Manual

Identical to the human lesion. Secondary findings in dogs and cats include pulmonary edema and hemorrhagic gastroenteritis. Calcium oxalate crystalluria indicates a poor prognosis in animals, and prognosis "varies inversely with the amount of time that elapses between ingestion and initiation of treatment" — the same statement made in the human literature, from an independent evidence base.

### Evolutionary conservation and orthologs

The full pathway is conserved across mammals — ADH, ALDH, glycolate oxidase (HAO1), LDH, and AGXT all have vertebrate orthologs. That conservation is why dog and rat models translate for this disease when they fail for so many others. The mechanism is chemistry, not physiology. Ortholog NCBI Gene IDs were not resolved this session.

### Transmission

No zoonotic potential. Not transmissible. Cross-species susceptibility is universal because the pathway is universal.

**OMIA:** ethylene glycol toxicosis is an acquired toxicosis, not a Mendelian trait, so there is no OMIA record to cite.

---

## 15. Model Organisms

### Rat — the workhorse

Male rats fed ethylene glycol are the standard model of calcium oxalate nephropathy, and they are used far more often to study **kidney stones** than to study poisoning. Keep that distinction when importing evidence.

- **Kidney is the most sensitive target organ** in rats and mice after intermediate-duration oral exposure (ATSDR toxicological profile). Lesions: oxalate crystal deposition, tubular dilation, vacuolation, degeneration.
- **Sensitivity ordering: males > females; rats > mice; Wistar > other rat strains.** Male Wistar rats are roughly twice as sensitive to EG nephrotoxicity as male F-344 rats.
- The strain difference is metabolic, not anatomical: after EG treatment, plasma oxalate and urine oxalate excretion were markedly higher in Wistar than F344, with slightly lower urine calcium in Wistars, while total urinary protein was higher in F344 at all times (see *Toxicol Sci* 2004 Wistar/F-344 subchronic comparison, and PMID:19244400, PMID:20534866).

That strain difference is the closest thing this disease has to a genetic modifier, and it sits in a rat.

### Dog — the therapeutic model

EXTRIP identified two controlled dog experiments (PMID:36765419):

> "In one experiment, an LD400 dose of EG was given to 23 dogs; 13 were treated with intravenous NaHCO3 and 10 were treated with a single session of hemodialysis for 20–24 h. All died in the NaHCO3 group while two died in the hemodialysis group (p < 0.0001), suggesting a beneficial effect of hemodialysis."

A second experiment in six EG-poisoned dogs found no benefit from hemoperfusion — all died. Both results have held up: hemodialysis works, hemoperfusion does not.

Dogs and cats also provide **naturally occurring disease**, which is rarer and more valuable than induced disease. This is the ideal `animal_models` entry with `relationship: RECAPITULATES` and high fidelity, because the species gets the same disease from the same chemical by the same route.

### In vitro

- **Human proximal tubule (HPT) cell cultures.** The system behind PMID:15695020. Exposure to COM crystal suspensions above 3 mM caused LDH release; oxalate in solution with EDTA to block crystallization did not. Acidosis enhanced crystal toxicity to human cells; glycolate did not. **Rat cells were more sensitive than human cells** — an explicit species-difference caveat you should carry into any fidelity statement.
- **Rat erythrocytes.** Hemolysis assay distinguishing crystal from ion toxicity.

### Not used

Zebrafish, Drosophila, C. elegans, yeast, iPSC-derived systems, organoids — I found none for this disease. A kidney organoid crystal-exposure model would be an obvious and currently missing NAM.

### Phenotype recapitulation and limitations

| Model | Recapitulates | Fidelity | Limitation |
|---|---|---|---|
| Dog, acute EG poisoning | AKI, acidosis, death; dialysis response | HIGH | dosing controlled, unlike human overdose |
| Cat, natural toxicosis | AKI, crystalluria, rapid course | HIGH | far more sensitive than humans; timing compressed |
| Male Wistar rat, oral EG | oxalate nephropathy, crystalluria | MODERATE | strain- and sex-specific; chronic/subchronic dosing, not acute overdose; **acidosis and CNS phase not the focus** |
| Mouse, oral EG | oxalate nephropathy | LOW–MODERATE | less sensitive than rat |
| HPT cell culture + COM crystals | crystal-induced tubular cell death | MODERATE | isolated cells, no tubular flow, no crystal-concentrating gradient |

**No model reproduces the delayed cranial neuropathy.** That is the largest gap between the models and the human disease, and it is exactly where the human mechanism is weakest.

### Model databases

MGI, RGD, ZFIN, IMSR, EMMA, MMRRC, Cellosaurus, ATCC. None hold a dedicated EG-poisoning resource — the models here are procedural (dose an animal), not genetic (order a strain), so there is no repository line to cite.

---

## Curation notes and known gaps

Things I could not establish, stated as fact rather than hedged:

1. **The ORPHA identifier is unverified.** The page did not render for me.
2. **The ICD-10 mapping conflicts.** MalaCards says T52.8; Orphanet says T52.3; ICD-10-CM coding practice uses T52.3X-. Resolve before binding.
3. **The ICD-11 code is unverified.**
4. **No EG-specific 2023 or 2024 national exposure count.** The 2023 NPDS abstract carries no substance-level figure and the tables are paywalled. The most recent citable EG figure is 2020: 6,036 calls, 586 with at least moderate effects, 30 deaths.
5. **No ECTO exposure term is cached** for ethylene glycol ingestion. It needs an ECTO search, not a guess.
6. **No quality-of-life instrument has ever been applied** to this disease.
7. **No human omics data of any kind** exist for EG poisoning.
8. **HGNC identifiers in section 4 are unverified.**
9. The **Guo & McMartin abstract** in section 6 came from Europe PMC's summary rendering, not from the reference cache. Fetch it with `just fetch-reference PMID:15695020` before quoting it as an evidence snippet — do not lift my paraphrase into a `snippet:` field.
10. Only four references are currently in this worktree's cache: PMID:36765419, PMID:27147840, PMID:18696123, PMID:16134263. Everything else cited here needs fetching before it can carry an evidence item.

---

## Sources

- [Ghannoum M et al. Extracorporeal treatment for ethylene glycol poisoning: systematic review and recommendations from the EXTRIP workgroup. *Crit Care* 2023. PMID:36765419](https://doi.org/10.1186/s13054-022-04227-2) — the single most important source here; full text is in this worktree's reference cache
- [Mégarbane B. Treatment of patients with ethylene glycol or methanol poisoning: focus on fomepizole. *Open Access Emerg Med* 2010. PMID:27147840](https://doi.org/10.2147/OAEM.S5346)
- [Stapenhorst L, Hesse A, Hoppe B. Hyperoxaluria after ethylene glycol poisoning. *Pediatr Nephrol* 2008. PMID:18696123](https://doi.org/10.1007/s00467-008-0917-8)
- [Keiran S, Bhimani B, Dixit A. Ethylene glycol toxicity. *Am J Kidney Dis* 2005. PMID:16134263](https://doi.org/10.1053/j.ajkd.2005.06.009)
- [Guo C, McMartin KE. The cytotoxicity of oxalate, metabolite of ethylene glycol, is due to calcium oxalate monohydrate formation. *Toxicology* 2005. PMID:15695020](https://pubmed.ncbi.nlm.nih.gov/15695020/)
- [Brent J et al. Fomepizole for the treatment of ethylene glycol poisoning. *N Engl J Med* 1999. PMID:10080845](https://pubmed.ncbi.nlm.nih.gov/10080845/)
- [Ethylene Glycol Toxicity. StatPearls, NCBI Bookshelf NBK537009](https://www.ncbi.nlm.nih.gov/books/NBK537009/)
- [2023 Annual Report of the National Poison Data System. *Clin Toxicol* 2024. PMID:39688840](https://pubmed.ncbi.nlm.nih.gov/39688840/)
- [Ethylene Glycol Toxicosis in Animals. Merck Veterinary Manual](https://www.merckvetmanual.com/toxicology/ethylene-glycol-toxicosis/ethylene-glycol-toxicosis-in-animals)
- [Was it necessary to add Bitrex (denatonium benzoate) to automotive products? PMID:15171494](https://pubmed.ncbi.nlm.nih.gov/15171494/)
- [Strain differences in urinary factors that promote calcium oxalate crystal formation in ethylene glycol-treated rats. PMID:19244400](https://pubmed.ncbi.nlm.nih.gov/19244400/)
- [Involvement of urinary proteins in the rat strain difference in sensitivity to ethylene glycol-induced renal toxicity. PMID:20534866](https://pubmed.ncbi.nlm.nih.gov/20534866/)
- [ATSDR Toxicological Profile for Ethylene Glycol, Potential for Human Exposure](https://www.ncbi.nlm.nih.gov/books/NBK600982/)
- [EPA Ethylene Glycol Hazard Summary (CAS 107-21-1)](https://www.epa.gov/sites/default/files/2016-09/documents/ethylene-glycol.pdf)
- [Lactate gap — a clinical tool for diagnosing and managing ethylene glycol poisoning. *Toxicology Reports* 2024](https://www.sciencedirect.com/science/article/pii/S2773232024000415)
- [Falsely elevated point-of-care lactate measurement after ingestion of ethylene glycol. *CMAJ* 2007](https://www.cmaj.ca/content/176/8/1097)
- [Unusual Clinical Presentation of Ethylene Glycol Poisoning: Unilateral Facial Nerve Paralysis. *Case Rep Med* 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3835194/)
- [Delayed ethylene glycol poisoning presenting with abdominal pain and multiple cranial and peripheral neuropathies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912929/)
- [Beyond the Usual Suspects: Ethylene Glycol Poisoning Complicated by Rare Neurological Sequelae](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11081402/)
- [Mass Poisoning From Ethylene Glycol at a U.S. Military Base. *Mil Med* 2023](https://academic.oup.com/milmed/article/188/9-10/e3261/6958179)
- [Ethylene Glycol Poisoning with a Near-Normal Osmolal Gap: A Diagnostic Challenge](https://pmc.ncbi.nlm.nih.gov/articles/PMC7785502/)
- [Ethylene Glycol Elimination Kinetics and Outcomes in Patients Managed Without Hemodialysis. *Ann Emerg Med*](https://www.sciencedirect.com/science/article/abs/pii/S0196064411018841)
- [MeSH record D019855, Ethylene Glycol](https://meshb.nlm.nih.gov/record/ui?ui=D019855)
- [Ethylene Glycol Poisoning, MalaCards](https://www.malacards.org/card/ethylene_glycol_poisoning)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.
