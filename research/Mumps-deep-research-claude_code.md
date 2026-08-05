---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-03T04:14:26.769839'
end_time: '2026-07-03T04:19:21.623780'
duration_seconds: 294.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mumps
  mondo_id: ''
  category: Infectious Disease
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
  - claude-sonnet-5
  web_search_requests: 15
  num_turns: 20
  total_cost_usd: 1.9371786000000004
  session_id: 520ca325-e58e-5587-b817-abe96e2a26c5
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mumps
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Mumps** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Mumps: Comprehensive Disease Research Report

## 1. Disease Information

**Overview.** Mumps is an acute, vaccine-preventable systemic viral infection caused by mumps virus (MuV), a member of genus *Orthorubulavirus* (family *Paramyxoviridae*), classically presenting with fever, headache, myalgia, and the hallmark finding of painful, non-suppurative swelling of one or both parotid salivary glands (parotitis), though up to a third of infections are subclinical or present only with nonspecific respiratory symptoms. Historically a universal childhood infection, mumps is now primarily controlled through the combined measles-mumps-rubella (MMR) vaccine, but it remains one of the more vaccine-mismatch-prone and outbreak-prone of the "eliminated" childhood diseases, with recurring resurgences in highly vaccinated populations (college students, military recruits, close-contact settings) attributed to a combination of waning immunity and genotype mismatch between vaccine and circulating strains (PMC7048016; PMC12711706).

**Key identifiers:**
- **ICD-11:** `1D80` Mumps — [ICD-11 MMS](https://www.findacode.com/icd-11/code-1208294714.html)
- **ICD-10-CM:** `B26` (Mumps), with subcodes `B26.0` (mumps orchitis), `B26.1` (mumps meningitis), `B26.2` (mumps encephalitis), `B26.3` (mumps pancreatitis), `B26.8` (mumps with other complications), `B26.9` (mumps without complication)
- **MeSH:** `D009107` (Mumps); `D009110` (Mumps Vaccine)
- **OMIM:** Not applicable — mumps is an acquired infectious disease, not a Mendelian disorder, so it has no OMIM phenotype/gene entry.
- **Orphanet:** Not applicable/not listed — Orphanet is scoped to rare diseases, and mumps is a common (historically near-universal) childhood infection, so it falls outside Orphanet's curation scope.
- **MONDO:** A MONDO term for mumps should exist (mumps is xref'd from ICD-11/MeSH-derived disease ontologies); **the exact MONDO CURIE should be confirmed with OAK** (`runoak -i sqlite:obo:mondo search "mumps"`) before use in a dismech entry rather than asserted here, consistent with this project's anti-hallucination policy.
- **NCBITaxon (pathogen):** `NCBITaxon:1979165` *Orthorubulavirus parotitidis* (mumps virus); older taxonomy/PMID literature uses *Mumps orthorubulavirus* / *Mumps rubulavirus*.

**Synonyms:** Epidemic parotitis; infectious parotitis; parotitis epidemica.

**Evidence basis for this report:** The information below is derived from aggregated disease-level resources — clinical/epidemiological reviews, CDC/ECDC/WHO surveillance guidance, and primary virology/immunology literature — rather than from any single patient-level EHR dataset. Frequencies given for complications (orchitis, meningitis, etc.) are pooled population-level estimates from outbreak surveillance and systematic review, not individual case data.

---

## 2. Etiology

**Causal agent.** Mumps is caused exclusively by mumps virus (MuV), a non-segmented, negative-sense single-stranded RNA virus. It is monotypic (a single serotype) but genetically diverse, currently classified into **12 recognized genotypes (A–N, excluding some letters)** based on sequence variation in the small hydrophobic (SH) and hemagglutinin-neuraminidase (HN) genes, the two most variable regions of the genome (PMC4268314; microbewiki). There is no genetic (Mendelian) causal component — this is a purely infectious etiology.

**Risk factors:**
- **Vaccination status** — the dominant risk factor. Unvaccinated individuals and those who never received MMR have the highest attack rates; however, modern outbreaks are increasingly driven by **waning vaccine-induced immunity** in adults who received both childhood doses years earlier. A meta-analysis found single-dose vaccinees had a 35.7% outbreak attack rate versus 16.4% for two doses and 10.1% for three doses (PMC12711706), and secondary vaccine failure (loss of protection after initially adequate response) is estimated at roughly 5% of recipients 6–26 years post-vaccination.
- **Age** — adults show the highest attack rates in contemporary outbreaks (31.8% pooled, versus 13.6% in children 0–10 years) (PMC12711706), a reversal of the pre-vaccine-era pattern where school-age children (5–9 years) bore the highest burden.
- **Congregate/close-contact settings** — university dormitories, military barracks, and other high-density-contact environments are classic outbreak amplifiers (e.g., the 2006 Iowa outbreak, the 2024–2025 Canadian outbreak with 5,078 cases as of October 2025).
- **Genotype mismatch** — outbreaks in vaccinated populations are disproportionately caused by **genotype G** viruses, phylogenetically distant from the **genotype A** Jeryl Lynn vaccine strain that has not circulated naturally since the 1980s; neutralizing antibody titers against genotype G are roughly half those against the homologous vaccine strain, though still generally protective (PMC/FDA science forum data; PMC9044963).
- **Season** — winter/spring peaks in temperate climates in the pre-vaccine era; less pronounced seasonality now.
- **Sex** — no strong sex-based susceptibility difference for infection itself, though male sex is a strong risk modifier for a specific complication (orchitis, post-pubertal only).

**Protective factors:**
- **Two-dose MMR vaccination** — approximately 97% protective; single dose approximately 78–88% (varies by study/era).
- **Prior natural infection** — confers durable, generally lifelong immunity (reinfection is rare though case reports exist).
- **Passive maternal antibody** — protects infants for the first several months of life.
- No specific host genetic protective variant has been characterized in the literature; unlike many chronic/genetic disorders, host genomic susceptibility loci for mumps (e.g., HLA associations) have not been robustly established in the literature surveyed — this remains a **relative knowledge gap** rather than a demonstrated null finding.

**Gene-environment interactions:** Not applicable in the classic sense (no known host genetic susceptibility locus to interact with viral exposure); the principal "gene x environment"-analogous axis in mumps is **viral genotype × vaccine-induced immune repertoire** (i.e., genotype G circulating strains vs. genotype A vaccine-elicited antibody repertoire), which functions as the closest analog to a modifier-gene interaction in this disease.

---

## 3. Phenotypes

Mumps phenotypes span symptoms/signs of the primary parotitis syndrome and several organ-specific complications from hematogenous viral dissemination. Frequencies below are pooled from a 2025 systematic review/meta-analysis of 47 studies/71,174 cases spanning 2004–2024 (PMC12711706) and CDC/ECDC clinical sources; note these are population/outbreak-level frequencies, not always internally consistent across sources (older sources give higher figures for orchitis/meningitis than the most recent meta-analysis, reflecting improved case ascertainment and vaccination status of study populations).

| Phenotype | Type | Frequency | Onset/Course | Suggested HP term* |
|---|---|---|---|---|
| Fever | Symptom | Common (prodromal) | Acute onset, precedes parotitis by 1–2 days | HP:0001945 (Fever) |
| Headache | Symptom | Common | Prodromal | HP:0002315 (Headache) |
| Myalgia | Symptom | Common | Prodromal | HP:0003326 (Myalgia) |
| Fatigue/malaise | Symptom | Common | Prodromal | HP:0012378 (Fatigue) |
| Anorexia | Symptom | Common | Prodromal | HP:0004396 (Poor appetite) |
| Parotitis (unilateral or bilateral) | Clinical sign | 60–70% of infections (PMC8471308); up to ~1/3 of infections subclinical | Onset 16–18 days post-exposure (range 12–25 days); swelling peaks day 1–3, resolves over ~1 week | Sialadenitis/parotid gland-related HP term — verify exact HP ID via OAK |
| Orchitis (post-pubertal males) | Complication | ~30% unvaccinated, ~6% vaccinated post-pubertal males (classic estimate); 63.1% of *all reported complications* in the 2025 meta-analysis, making it the single most common complication category | Onset ~4–8 days after parotitis, though can precede or occur without parotitis; 60–83% unilateral | HP:0100957 (Orchitis) — verify |
| Testicular atrophy (post-orchitis) | Sequela | Occurs in a minority of orchitis cases | Delayed, months after acute infection | HP:0000034 (Testicular atrophy) — verify |
| Oophoritis (post-pubertal females) | Complication | ~5% of postpubertal females (older estimates); rarely reported in recent meta-analysis | Acute, during/after parotitis | — |
| Aseptic meningitis | Complication | ~1–15% depending on source/era (5–10% CDC; 1.4% pooled 2025 meta-analysis; up to 10% unvaccinated in older series) | Acute, days after parotitis onset; usually self-limited | HP:0001287 (Meningitis) — verify |
| Encephalitis | Complication | 0.02–0.5% (<0.5% CDC; 0.2% pooled meta-analysis); most common cause of mumps death | Acute | HP:0002383 (Encephalitis) — verify |
| Sensorineural hearing loss (usually unilateral, sudden, permanent) | Complication | Historic estimates 1:20,000 to 1:15,000 infections; range 1/30,000–1/2,000 across studies; mumps historically the leading cause of unilateral acquired SNHL in children | Sudden onset, often within days of parotitis; ~45% have associated vestibular dysequilibrium | HP:0000407 (Sensorineural hearing loss) — confirmed in dismech `sensorineural_hair_cell_loss` module |
| Pancreatitis | Complication | ~4% (PMC4268314) to 5% (older estimates); 0.8% pooled meta-analysis | Acute, transient | HP:0001733 (Pancreatitis) — confirmed in dismech `pancreatitis_acinar_autodigestion` module |
| Transient hyperglycemia / (rare) diabetes mellitus | Complication | Rare; causal link to permanent diabetes debated | Post-pancreatitis | HP:0000819 (Diabetes mellitus) — verify |
| Mastitis | Complication | Uncommon (~1% or fewer in vaccinated postpubertal women) | Post-pubertal females | — |
| Cerebellar ataxia | Rare neurologic complication | Rare | Post-infectious | HP:0001251 (Cerebellar ataxia) — confirmed in dismech `cerebellar_purkinje_degeneration` module |
| Myocarditis | Rare complication | Rare, case-report level | Acute | — |
| Nephritis | Rare complication | Rare | Acute | — |

*HP terms marked "verify" should be confirmed against the canonical label via OAK (`runoak -i sqlite:obo:hp info <ID> -O obo`) before use, per this project's anti-hallucination policy — several are given from memory and their exact identifiers/labels were not independently re-verified against the ontology in this research pass.

**Quality of life impact:** The acute illness is typically self-limited with full recovery over 1–2 weeks; the QoL-significant long-term sequelae are (1) permanent unilateral SNHL, which can affect language development if occurring in early childhood and sound localization/social function generally, and (2) testicular atrophy following severe/bilateral orchitis, which is a recognized but not well-quantified contributor to (usually not complete) subfertility. Encephalitis survivors may have residual neurologic deficits. No dedicated mumps-specific QoL instrument was identified in this search; general EQ-5D/SF-36 data specific to mumps sequelae were not found.

---

## 4. Genetic/Molecular Information

Mumps is **not a genetic disease** in the host-Mendelian sense (no OMIM phenotype, no ClinVar variant classification, no host causal gene) — the "genetic/molecular" content relevant to a dismech entry is entirely on the **viral** side:

- **Viral genome:** Non-segmented, negative-sense ssRNA genome of 15,384 nucleotides, encoding seven genes in the order 3′-N-V/P/I-M-F-SH-HN-L-5′ (nucleoprotein, V/phospho-/I proteins, matrix, fusion, small hydrophobic, hemagglutinin-neuraminidase, large/polymerase) (PMC4268314).
- **Key viral proteins and function:**
  - **HN (hemagglutinin-neuraminidase):** Mediates receptor binding (attachment) to sialylated glycan receptors on host cells and has neuraminidase activity for viral release; a major target of neutralizing antibodies and the protein most implicated in genotype-specific antigenic differences (PMC6127219; PMC2933592).
  - **F (fusion) protein:** Mediates fusion of viral and host membranes following HN-triggered conformational change, enabling nucleocapsid entry (PMC8471308).
  - **SH protein:** A 57-amino-acid type I membrane protein; the single most variable genomic region (basis of genotyping A–N) and implicated in modulating host innate immune antagonism/apoptosis, though dispensable for viral growth in culture (Journal of Virology jvi.02686-10; PMC1367141).
  - Variations in HN and SH amino acid sequence have been statistically associated with **neurovirulence** (differential propensity to cause CNS complications), based on comparison of mumps cases with vs. without neurologic symptoms (PMC3634820).
- **Genotypes:** 12 recognized genotypes (A–N minus a few unused letters) based on SH/HN sequence. Genotype A is the Jeryl Lynn/RIT 4385 vaccine lineage (no longer in natural circulation since the 1980s); **genotype G** is the genotype responsible for the majority of contemporary outbreaks in vaccinated populations in the US/UK/Netherlands, and is antigenically distinct enough from genotype A to have driven development of genotype-G-matched candidate vaccines (FDA Science Forum; PMC9044963; jvi.01983-21).
- **Host genetics:** No robustly replicated human susceptibility locus (HLA or otherwise) for mumps infection or complication severity was identified in this literature search — this appears to be a genuine gap rather than a well-characterized null result, and is analogous to the "no established host genetic risk factor" situation seen for many acute self-limited viral infections that have not been subjected to large-scale host GWAS.
- **Somatic vs. germline:** Not applicable (infectious, not neoplastic/genetic).
- **Epigenetics:** No disease-specific host epigenetic mechanism has been characterized in the literature reviewed.
- **Chromosomal abnormalities:** Not applicable.

---

## 5. Environmental Information

- **Environmental/toxin factors:** None — mumps is a purely infectious disease with no toxin, pollutant, or occupational-exposure contribution.
- **Lifestyle factors:** Close-contact behaviors (shared drinks/utensils, kissing, crowded living — dormitories, military barracks) are the principal "lifestyle" risk modifiers, since transmission is via respiratory droplets/direct saliva contact and requires prolonged close contact.
- **Infectious agent:** **Mumps virus (MuV)**, genus *Orthorubulavirus*, family *Paramyxoviridae*. NCBI Taxonomy entry should be confirmed (`NCBITaxon` search for "Mumps orthorubulavirus"/"Orthorubulavirus parotitidis"). Enveloped, pleomorphic, ~200 nm virion.
- **Transmission:** Person-to-person via respiratory droplets or direct contact with saliva/fomites; virus is shed in saliva from approximately 1 week before to 1 week after parotitis onset (CDC/PMC4268314), with the practically infectious window commonly cited as 2 days before to 5 days after parotitis onset. Asymptomatic shedders can transmit virus.

---

## 6. Mechanism / Pathophysiology

**Causal chain — initial trigger to clinical manifestation:**

1. **Respiratory entry and local replication:** MuV is inhaled/contacted via respiratory droplets or saliva and initially infects and replicates in epithelial cells of the upper respiratory tract (nasopharynx) and regional (cervical) lymph nodes (PMC8471308).
2. **Viral entry mechanism:** MuV attaches via its HN glycoprotein to host-cell sialylated glycan receptors — a trisaccharide containing α2,3-linked sialic acid in unbranched chains (e.g., 3′-sialyllactosamine), with additional recognition of sialyl-Lewis X and GM2 ganglioside as receptors (PMC5068328/PMID:27671656; PMC6639266/PMID:31118251). HN binding triggers conformational changes propagated to the F protein, driving membrane fusion and nucleocapsid entry (PMC8471308). Beyond sialic-acid-mediated attachment, the receptor tyrosine kinases **AXL and MER** facilitate productive infection by suppressing cellular innate antiviral responses in target cells such as Sertoli/Leydig cells (PMC7336603).
3. **Primary viremia and systemic dissemination:** After several replication cycles in the respiratory tract/lymph nodes, the virus enters the bloodstream (viremia) during the early acute phase and disseminates to distant organs with permissive glandular and neural tropism — principally the salivary glands (parotid > submandibular/sublingual), but also testes/ovaries, pancreas, thyroid, and the central nervous system (meninges/brain/inner ear) (PMC4268314; PMC8471308).
4. **Organ-specific inflammatory injury:**
   - **Salivary gland (parotitis):** Viral replication in ductal/acinar epithelium triggers local inflammatory cell infiltration, glandular edema, and interstitial inflammation, producing the classic painful parotid swelling.
   - **Testis (orchitis)/ovary (oophoritis):** Direct viral infection of Sertoli and Leydig cells (testis) or granulosa cells (ovary) triggers a robust local innate immune response — Toll-like receptor 2 (TLR2) and RIG-I (retinoic-acid-inducible gene I) pathway activation — producing TNF-α, IL-6, MCP-1, CXCL10, and type I interferons (IFN-α/β) (Sci Rep srep19507; PMC4725973; ScienceDirect S0303720716302738). The resulting local inflammatory swelling within the non-distensible tunica albuginea (testis) can cause ischemic injury contributing to later testicular atrophy.
   - **CNS (meningitis/encephalitis):** Virus reaches the meninges/CNS hematogenously (and possibly via infected leukocytes), producing a lymphocytic (aseptic) meningitis; true encephalitis (parenchymal invasion) is rarer and is the principal cause of mumps mortality.
   - **Inner ear (sensorineural hearing loss):** Proposed mechanism is **hematogenous viral endolymphatic labyrinthitis** — direct viral invasion of the cochlea via the bloodstream (rather than tympanogenic or meningogenic spread) — producing atrophy/destruction of cochlear hair cells and consequent sudden, usually unilateral, profound and permanent SNHL (PMID:3767776; PMID:13762395).
   - **Pancreas (pancreatitis):** Direct viral invasion of pancreatic tissue is proposed, generally producing transient exocrine/endocrine dysfunction (hyperglycemia); rare reports of subsequent (type 3c/pancreatogenic) diabetes remain of uncertain causality.
5. **Adaptive immune control and resolution:** Mumps-specific CD4+ T cells (IFN-γ-producing) and CD8+ cytotoxic T cells (granzyme A/B, perforin) are induced; T-cell response rates are notably robust in natural infection (~80% positive) versus vaccination (~70%), and a 2021 study found that natural infection but not vaccination elicits certain cytotoxic-T-cell epitope responses, offering one candidate explanation (beyond antibody waning/genotype mismatch) for vaccine-breakthrough susceptibility (PMC/PMID:34211021).

**Upstream vs. downstream:** Respiratory entry → regional lymphatic replication → viremia are upstream/shared steps common to *all* downstream organ-specific complications, which are essentially independent, parallel branches (parotitis, orchitis/oophoritis, meningoencephalitis, labyrinthitis, pancreatitis) triggered by tissue-specific viral tropism plus locally-mounted innate/inflammatory responses, rather than a single linear cascade.

**Suggested GO terms:** `GO:0046718` (viral entry into host cell), `GO:0019064` (fusion of virus membrane with host plasma membrane), `GO:0033130` (sialic acid binding — verify), `GO:0045087` (innate immune response), `GO:0060337` (type I interferon signaling pathway), `GO:0006954` (inflammatory response), `GO:0002250` (adaptive immune response).

**Suggested CL terms:** `CL:0000216` (Sertoli cell), `CL:0000178` (Leydig cell), `CL:0000501` (granulosa cell), auditory/cochlear hair cell (verify exact CL ID), salivary gland acinar/ductal epithelial cell (verify exact CL ID), `CL:0000624` (CD4+ T cell), `CL:0000625` (CD8+ T cell).

**Molecular profiling / advanced technologies:** No transcriptomic (GEO), proteomic (PRIDE), metabolomic, single-cell, or spatial-transcriptomic dataset specific to human mumps infection was identified in this search — this is a data gap; most mechanistic work on mumps innate immune signaling has used mouse Sertoli/Leydig/granulosa cell culture models rather than -omics profiling of human tissue.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Salivary glands — parotid gland (most common; `UBERON:0001830`), submandibular gland (`UBERON:0001736`), sublingual gland.
- **Secondary (complication-associated):** Testis (`UBERON:0000473`) and epididymis; ovary (`UBERON:0000992`); pancreas (`UBERON:0001264`); meninges (`UBERON:0002360`) and brain parenchyma (`UBERON:0000955`); inner ear/cochlea (`UBERON:0001844`); breast (mastitis); heart (rare myocarditis); kidney (rare nephritis); thyroid (rare thyroiditis, case reports).
- **Body systems involved:** Exocrine/glandular system (primary), reproductive system, digestive/endocrine system (pancreas), nervous system (CNS and inner ear/CN VIII), and (rarely) cardiovascular and renal systems.

**Tissue/cell level:** Glandular epithelium (ductal and acinar cells of salivary glands), Sertoli and Leydig cells of testis, granulosa cells of ovary, cochlear hair cells (mechanotransducing sensory epithelium), pancreatic acinar/islet tissue, meningeal and neuronal/glial tissue.

**Subcellular level:** No disease-defining subcellular/organelle pathology has been characterized beyond generic viral-replication cytopathic changes; relevant GO Cellular Component terms would be plasma membrane (site of HN/F-mediated entry) and endoplasmic reticulum/Golgi (viral glycoprotein processing) rather than a disease-specific organelle lesion.

**Localization/laterality:** Parotitis is bilateral in roughly 70–90% of cases in most series (unilateral in the remainder); orchitis is unilateral in 60–83% of affected males; sensorineural hearing loss is characteristically **unilateral** (bilateral mumps deafness is very uncommon).

---

## 8. Temporal Development

- **Onset:** Incubation period 12–25 days (average commonly cited as 16–18 days; some sources state 2–4 weeks) following exposure (CDC clinical overview; PMC4268314). Onset is typically preceded by a 1–2 day nonspecific prodrome (fever, headache, myalgia, malaise, anorexia) before glandular swelling appears.
- **Onset pattern:** Acute.
- **Progression/stages:** Prodrome → parotid (± other salivary gland) swelling peaking over 1–3 days → gradual resolution over about 1 week. Organ-specific complications (orchitis, meningitis, pancreatitis) typically follow parotitis onset by days (orchitis classically 4–8 days later) but can occasionally precede parotitis or occur in its absence.
- **Rate/course:** Rapid onset, generally self-limited acute illness; no chronic/relapsing form of mumps itself exists (unlike the chronic sequelae it can leave behind — SNHL, testicular atrophy).
- **Duration:** Self-limited — acute illness resolves within 1–2 weeks in the vast majority of cases; sequelae (deafness, testicular atrophy) are permanent when they occur, but the causal infection itself does not become chronic.
- **Remission:** Not applicable in the relapsing-disease sense; the infection resolves with adaptive immunity, generally rendering the person subsequently immune (natural infection immunity considered lifelong, though not absolute).
- **Critical periods:** The pubertal/post-pubertal period is the critical window of vulnerability for orchitis/oophoritis (rare before puberty); first-trimester pregnancy has been proposed (weak, largely historical evidence) as a window of increased miscarriage risk, though modern controlled data do not clearly support increased congenital malformation risk (GOV.UK mumps-in-pregnancy guidance; PMC3296145).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Pre-vaccine era:** Incidence of 100–1,000 per 100,000 population per year globally, with epidemics recurring every 2–5 years, peaking in winter/spring in temperate climates; in the US, >185,000 cases/year were reported before vaccine introduction, predominantly in children aged 5–9 years.
- **Contemporary WHO surveillance:** ~500,000 cases/year reported to WHO on average 1999–2019 (likely a substantial undercount, since mumps is not notifiable in many countries).
- **Vaccine impact:** One-dose schedules reduce incidence by >88%; two-dose schedules by ~97%.
- **Recent outbreaks:** A large ongoing Canadian outbreak beginning October 2024 reached 5,078 cases by mid-October 2025; a 2023–2024 outbreak in Shivamogga, India provided an economic case for MMR inclusion in that country's universal immunization program; recurrent outbreaks have also affected US universities/military populations and parts of Europe.
- **Pooled outbreak attack rate (2004–2024 meta-analysis, 47 studies/21 countries/71,174 cases):** 14.5% overall; regional variation from ~7.6% (Europe) to ~29.2% (Americas)/28.8% (Eastern Mediterranean).

**Inheritance pattern:** Not applicable — mumps is an acquired infection, not a heritable genetic disease; there is no Mendelian inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency to report. (These fields, standard for genetic disorders in this template, simply do not apply to an infectious-disease dismech entry.)

**Population demographics:**
- **Age distribution:** Historically concentrated in school-age children (5–9 years); in the contemporary vaccine era, disproportionately shifted toward **young adults** (college-age and older), reflecting waning immunity plus dense-contact settings.
- **Sex ratio:** Roughly equal susceptibility to infection between sexes; complication *type* is markedly sex-specific (orchitis only in post-pubertal males; oophoritis/mastitis only in post-pubertal females).
- **Geographic distribution:** Global; higher contemporary attack rates reported in the Americas and Eastern Mediterranean regions versus Europe and South-East Asia in the recent meta-analysis, likely reflecting differences in vaccination coverage/schedule (2 vs. 3 dose) and case-ascertainment practices rather than intrinsic regional biology.
- **Genotype geography:** Genotype G circulates widely in outbreak settings in North America/Europe; other genotypes (e.g., genotype C, D, H, J, K) show more regionally restricted circulation historically (e.g., parts of Asia).

---

## 10. Diagnostics

**Preferred specimen/method:** A **buccal swab** specimen, collected after massaging the parotid gland area for ~30 seconds, obtained **≤3 days after parotitis onset**, tested by **real-time RT-PCR (rRT-PCR)** — this is the CDC-preferred combination for laboratory confirmation (CDC Mumps Laboratory Testing/Specimen Collection guidance, Jan 2025 update).

**Serology (IgM):**
- If specimen collection occurs **>3 days after onset**, CDC recommends collecting **both** a buccal swab for rRT-PCR **and** a serum specimen for IgM.
- IgM capture ELISA detects only 46–71% of rRT-PCR-confirmed cases — sensitivity is **inversely related to vaccination status**: highest detection in unvaccinated persons, intermediate after one dose, lowest after two doses — a well-documented pitfall in outbreaks among highly vaccinated populations (PMC5299122).
- A positive IgM result is supportive but not confirmatory evidence per the CSTE case definition.

**Genotyping:** SH-gene sequencing from RT-PCR-positive specimens is used for genotype assignment (surveillance/outbreak-source tracing), not for individual patient diagnosis.

**Imaging:** Not typically required for diagnosis; ultrasound may be used to characterize orchitis/oophoritis or distinguish parotitis from other causes of parotid swelling (sialolithiasis, bacterial parotitis, tumor) in atypical presentations.

**Differential diagnosis:** Bacterial (suppurative) parotitis, parotid duct stone/sialadenitis of other cause, HIV-associated parotid enlargement, other viral parotitis (parainfluenza, influenza A, EBV, CMV, coxsackievirus, adenovirus), Sjögren's syndrome/juvenile recurrent parotitis (non-infectious sialadenitis), and — for isolated CNS presentations — other causes of aseptic meningitis/encephalitis (enterovirus is the most common overall cause).

**Screening:** No population screening program exists (mumps is prevented, not screened for); the relevant "screening" surrogate is **serologic immunity screening** (e.g., pre-employment healthcare-worker immunity checks) rather than disease screening.

---

## 11. Outcome/Prognosis

- **Mortality:** Case-fatality ratio estimated at **1.6–3.8 per 10,000 cases** (PMC4268314), with essentially all deaths occurring in the context of encephalitis. Mortality is very low in the modern/vaccine era in high-resource settings.
- **Morbidity/functional outcomes:** The dominant long-term morbidity burdens are **permanent unilateral sensorineural hearing loss** (historically the leading cause of unilateral acquired childhood SNHL) and **testicular atrophy** after severe orchitis (contributing to, though rarely causing complete, subfertility — bilateral severe orchitis with bilateral atrophy causing infertility is described but uncommon). Encephalitis survivors can have residual neurologic deficits, though most mumps meningitis is self-limited without sequelae.
- **Recovery:** The acute systemic illness resolves fully in the great majority of patients within 1–2 weeks without any long-term consequence; complications, when they occur, are the exception rather than the rule (overall pooled outbreak complication rate ~10.3%, dominated by orchitis).
- **Prognostic factors:** Post-pubertal male sex (orchitis risk), unvaccinated/single-dose status (higher complication rates), and encephalitis occurrence (the dominant mortality predictor).
- **Prognostic biomarkers:** None specific/validated beyond general clinical/CNS-involvement assessment.

---

## 12. Treatment

Mumps has **no specific antiviral therapy** — management is entirely supportive.

**Pharmacotherapy (supportive):**
- Antipyretics/analgesics (e.g., acetaminophen, NSAIDs) for fever, headache, and glandular/testicular pain.
- Scrotal support and analgesia (including, in severe orchitis, sometimes corticosteroids, though evidence for corticosteroid benefit in mumps orchitis is limited/not robust).
- No antiviral drug (e.g., ribavirin) has demonstrated proven clinical benefit and none is a standard-of-care recommendation; ribavirin (`CHEBI:63580`) has been studied experimentally in vitro/in some case reports but is not an established treatment.

**Advanced therapeutics:** Not applicable — no gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy is used for mumps itself (these modalities are not relevant to this acute self-limited viral infection).

**Surgical/interventional:** Not routinely required; rare surgical intervention (e.g., testicular decompression) has been described anecdotally for severe orchitis but is not standard practice.

**Supportive/rehabilitative care:** Bed rest, hydration, dietary modification for pancreatitis (limiting oral intake if pancreatitis is significant), and — for complication sequelae — audiology/hearing rehabilitation (hearing aids/cochlear implant evaluation) for permanent SNHL.

**Isolation/infection control:** Isolation of infected individuals for 5 days after parotitis onset (droplet precautions) is a key "treatment-adjacent" public-health action to limit transmission (CDC).

**Suggested MAXO terms:** `MAXO:0000950` (supportive care); `MAXO:0001017` (vaccination — for the *preventive*, not therapeutic, arm); a hearing-rehabilitation/audiology-intervention MAXO or NCIT term for post-SNHL management (verify specific ID).

**Experimental treatments:** No active mumps-specific therapeutic (as opposed to vaccine) clinical trials were identified; most current mumps-related ClinicalTrials.gov activity concerns **vaccine strategies** (e.g., third-dose MMR effectiveness studies), not treatment of acute disease.

---

## 13. Prevention

**Primary prevention — vaccination:** The mainstay of mumps prevention is the live-attenuated mumps component of the **MMR** (or MMRV) vaccine, most commonly the **Jeryl Lynn strain** (genotype A) in the US (e.g., M-M-R II; PMC8903938 — "40 years of global experience with M-M-RII"), or the RIT 4385/Urabe/Leningrad-Zagreb strains used in other countries. Standard US schedule: first dose at 12–15 months, second dose at 4–6 years, achieving ~97% two-dose effectiveness. A **third MMR dose** has been used/modeled as an outbreak-control measure in settings of ongoing transmission (e.g., University of Iowa outbreak modeling; PMID:39401354), and a 2025 individual-based stochastic modeling study evaluated optimized mumps-vaccination strategies (Lancet eClinicalMedicine, 2025).

**Secondary prevention:** Prompt case identification (RT-PCR/IgM per CDC algorithm above) and isolation of cases (5 days post-parotitis-onset) to interrupt outbreak chains; outbreak-response vaccination (e.g., targeted third-dose campaigns in affected cohorts).

**Tertiary prevention:** Management of complications to limit their sequelae — e.g., prompt recognition/supportive management of orchitis to reduce (though not eliminate) risk of testicular atrophy; audiologic monitoring/early hearing rehabilitation after mumps-associated SNHL.

**Genetic/prenatal screening, carrier screening:** Not applicable (non-genetic, infectious disease).

**Public health interventions:** Case-based and outbreak surveillance (nationally notifiable in the US and most high-income countries), outbreak investigation and targeted vaccination campaigns in affected institutions (universities, correctional facilities, military units), health education about transmission via saliva/respiratory droplets.

**Prophylaxis:** Post-exposure vaccination is **not** established as effective for preventing disease in an already-exposed contact (unlike, e.g., measles), since the incubation period generally exceeds the time needed to mount vaccine-induced protection; there is no approved mumps-specific immunoglobulin prophylaxis in routine use.

---

## 14. Other Species / Natural Disease

Mumps virus is essentially **human-restricted** in its natural epidemiology — there is no significant naturally occurring reservoir or endemic disease of mumps virus in non-human species; unlike many zoonotic paramyxoviruses, mumps has no recognized zoonotic cycle or wildlife/companion-animal reservoir in the literature reviewed. This is itself a notable feature worth flagging in a dismech entry (i.e., "naturally occurring disease in other species" = essentially none, in contrast to the extensive experimental/model-organism literature below). No OMIA (Online Mendelian Inheritance in Animals) entries or veterinary clinical disease reports of natural mumps virus infection were identified.

---

## 15. Model Organisms

Mumps virus pathogenesis has been studied across several experimental animal systems, with **rhesus macaques** established as the best available model:

- **Rhesus macaque (NCBITaxon:9544):** The single best-characterized model — intranasal and intratracheal inoculation with clinical MuV isolates (e.g., MuV-IA, the 2006 Iowa outbreak strain) produces classic clinical mumps signs 2–4 weeks post-infection, and macaques were extensively used in the early 1990s for parotid-gland and CNS pathogenesis studies (PMC3700206/PMID:23678169; Tandfonline 10.1080/21645515.2016.1210745). Rhesus macaques were the **most susceptible** species tested to clinical MuV-IA infection.
- **Mice:** Generate humoral and cellular immune responses to MuV-IA infection but show **no overt clinical illness**; used mainly for immunogenicity/vaccine-candidate evaluation (e.g., Jeryl-Lynn-immunized mice challenged with genotype G vaccine candidates, PMC9044963) and for innate-immune mechanistic studies in isolated Sertoli/Leydig/granulosa cell culture (Sci Rep srep19507).
- **Ferrets:** Similarly generate immune responses without overt clinical disease upon MuV-IA infection; used as an intermediate model in comparative pathogenesis studies (PMC3700206).
- **Cotton rat (*Sigmodon hispidus*):** Recently used to evaluate immunogenicity of mumps vaccine candidate strains (ScienceDirect S0264410X25009375, 2025).
- **Newborn hamsters/neonatal mice (intracerebral/intraperitoneal inoculation):** Historical models confirming **neurotropism** of MuV to neurons, with differing neurovirulence between viral strains — used to map the SH/HN neurovirulence determinants discussed in Section 6.
- **Other historically examined species:** Cat, guinea pig, marmoset — generally limited replication and are not standard models today.

**Limitations:** MuV replication is limited in rodents generally, restricting their utility for humoral/cellular immunogenicity studies (though useful for innate-response mechanism and vaccine-candidate screening); no small-animal model faithfully recapitulates the full clinical parotitis/orchitis/meningoencephalitis/SNHL phenotype spectrum seen in humans — only rhesus macaques approximate the clinical disease, which limits throughput and scale for pathogenesis studies given cost/ethical constraints of NHP work. In dismech terms, this would represent good material for a `HUMAN_MODEL_MISMATCH`-style discussion node if a mechanistic claim (e.g., a specific SH-mediated neurovirulence mechanism) is sourced primarily from rodent/cell-culture data without confirmed human-tissue correlation.

**Cell-culture/in vitro systems:** Mouse Sertoli cell (TM4), Leydig cell, and ovarian granulosa cell lines have been used extensively to dissect the TLR2/RIG-I-mediated innate cytokine response to MuV infection described in Section 6 (Sci Rep srep19507; PMC4725973; ScienceDirect S0303720716302738); these are IN_VITRO/MODEL_ORGANISM-adjacent (mouse-derived cell lines) evidence sources per this project's evidence-source classification convention, and should not be used as the sole support for human phenotype claims without corroborating human clinical evidence.

---

## Summary of Suggested Ontology Terms for KB Curation

| Domain | Suggested terms (verify all via OAK before committing) |
|---|---|
| Disease identity | ICD-11 `1D80`; MeSH `D009107`; MONDO ID — confirm via `runoak -i sqlite:obo:mondo search "mumps"` |
| Pathogen | NCBITaxon for mumps orthorubulavirus — confirm exact ID |
| Phenotypes (HP) | HP:0001945 Fever; HP:0002315 Headache; HP:0003326 Myalgia; HP:0012378 Fatigue; HP:0000407 Sensorineural hearing loss (confirmed elsewhere in dismech); HP:0001733 Pancreatitis (confirmed elsewhere in dismech); HP:0001251 Cerebellar ataxia (confirmed elsewhere in dismech); Orchitis/Meningitis/Encephalitis/Testicular atrophy/Diabetes mellitus HP IDs — verify |
| Biological processes (GO) | GO:0046718 viral entry into host cell; GO:0019064 fusion of virus membrane with host plasma membrane; GO:0045087 innate immune response; GO:0060337 type I IFN signaling pathway; GO:0006954 inflammatory response |
| Cell types (CL) | CL:0000216 Sertoli cell; CL:0000178 Leydig cell; CL:0000501 granulosa cell; CL:0000624 CD4+ T cell; CL:0000625 CD8+ T cell; cochlear hair cell and salivary gland acinar/duct cell — verify |
| Anatomy (UBERON) | UBERON:0001830 parotid gland; UBERON:0001736 submandibular gland; UBERON:0000473 testis; UBERON:0000992 ovary; UBERON:0001264 pancreas; UBERON:0002360 meninges; UBERON:0001844 cochlea |
| Treatments (MAXO/NCIT) | MAXO:0000950 supportive care; MAXO:0001017 vaccination |
| Chemical (CHEBI) | CHEBI:63580 ribavirin (experimental only, not standard of care) |

---

## Key Gaps Flagged for Curators

1. **No confirmed MONDO/Orphanet ID** was located in this search — needs OAK/manual lookup before entry creation.
2. **Host genetic susceptibility (HLA or other loci)** is essentially uncharacterized in the literature — worth an explicit `KNOWLEDGE_GAP` discussion node rather than assuming absence of any genetic modifier.
3. **Mumps-in-pregnancy risk** evidence is thin and largely historical (a single 1966 study); modern data do not support a clear congenital-malformation signal — an appropriate candidate for a `KNOWLEDGE_GAP`/nuanced-evidence framing rather than a firm causal claim.
4. **Pancreatitis→diabetes causality** is explicitly stated as unclear in the reviewed literature — do not assert a firm causal pathway.
5. **Direct human tissue/-omics data** (transcriptomic, proteomic) for mumps pathogenesis is essentially absent; most cellular-mechanism evidence is mouse-cell-line-derived, a good `HUMAN_MODEL_MISMATCH` candidate if a specific innate-immune mechanistic claim is imported into a pathophysiology node.

Sources:
- [Molecular biology, pathogenesis and pathology of mumps virus - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4268314/)
- [Function of Small Hydrophobic Proteins of Paramyxovirus - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1367141/)
- [Discrimination of Mumps Virus Small Hydrophobic Gene Deletion Effects — J Virol](https://journals.asm.org/doi/10.1128/jvi.02686-10)
- [Differences in antigenic sites... genotype A and G mumps virus surface proteins - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6127219/)
- [A 176 amino acid polypeptide derived from the mumps virus HN ectodomain - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2933592/)
- [Genetic Variation in the HN and SH Genes of Mumps Viruses - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3634820/)
- [Unique Tropism and Entry Mechanism of Mumps Virus - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8471308/)
- [Roles of Sialic Acid, AXL, and MER RTKs in Mumps Virus Infection - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7336603/)
- [Trisaccharide containing α2,3-linked sialic acid is a receptor for mumps virus - PNAS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5068328/)
- [Molecular Mechanism of the Flexible Glycan Receptor Recognition by Mumps Virus - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6639266/)
- [Mumps Complications and Effects of Mumps Vaccination, England and Wales, 2002–2006 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3377415/)
- [Clinical Features of Mumps | CDC](https://www.cdc.gov/mumps/hcp/clinical-signs/index.html)
- [Clinical Overview of Mumps | CDC](https://www.cdc.gov/mumps/hcp/clinical-overview/index.html)
- [Chapter 15: Mumps | Pink Book | CDC](https://www.cdc.gov/pinkbook/hcp/table-of-contents/chapter-15-mumps.html)
- [Epidemiological trends and determinants of mumps outbreaks: a systematic review and meta-analysis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12711706/)
- [Modeling the population-level impact of a third dose of MMR vaccine - PubMed](https://pubmed.ncbi.nlm.nih.gov/39401354/)
- [Mumps Outbreak in Shivamogga, India (2023–2024) - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12883994/)
- [Evaluation and optimization of mumps-containing vaccination strategies - eClinicalMedicine](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(25)00554-1/fulltext)
- [Deafness following mumps: the possible pathogenesis and incidence of deafness - PubMed](https://pubmed.ncbi.nlm.nih.gov/3767776/)
- [Inner ear pathology in deafness due to mumps - PubMed](https://pubmed.ncbi.nlm.nih.gov/13762395/)
- [The potential dysfunction of otolith organs in patients after mumps infection - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5528881/)
- [Mumps Infection With Parotitis, Pancreatitis, and Orchitis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8906564/)
- [Mumps virus-induced innate immune responses in mouse Sertoli and Leydig cells - Sci Rep](https://www.nature.com/articles/srep19507)
- [Immune Responses to Mumps Vaccine in Adults Vaccinated in Childhood - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2561204/)
- [Mumps virus induces innate immune responses in mouse ovarian granulosa cells - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0303720716302738)
- [Novel mumps virus epitopes reveal robust cytotoxic T cell responses - Sci Rep](https://www.nature.com/articles/s41598-021-92926-1)
- [Antibody Induced by Immunization with the Jeryl Lynn Mumps Vaccine Strain - PubMed](https://www.ncbi.nlm.nih.gov/pubmed/18558869)
- [A Mumps Virus Genotype G Vaccine Candidate — FDA Science Forum](https://www.fda.gov/science-research/fda-science-forum/mumps-virus-genotype-g-vaccine-candidate-displays-enhanced-neutralization-circulating-variants-over)
- [Immunogenicity of Mumps Virus Genotype G Vaccine Candidates in Jeryl Lynn-Immunized Mice - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9044963/)
- [Exploring the Mumps Virus Glycoproteins: A Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9229384/)
- [Immunogenicity of mumps virus vaccine candidates matching circulating genotypes - PubMed](https://pubmed.ncbi.nlm.nih.gov/28623030/)
- [MMRV Testing for Clinicians (Jan 2025) | CDC](https://www.cdc.gov/mumps/media/pdfs/2025/02/MMRV-Testing-for-Clinicians_Jan2025.pdf)
- [Serology to Diagnose Mumps | CDC](https://www.cdc.gov/mumps/php/laboratories/serology.html)
- [Challenges in Interpretation of Diagnostic Test Results in a Mumps Outbreak - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5299122/)
- [Mumps Clinical Testing | CDC](https://www.cdc.gov/mumps/php/public-health-strategy/mumps-testing-aid.html)
- [Mumps Specimen Collection | CDC](https://www.cdc.gov/mumps/php/laboratories/specimen-collection.html)
- [Infection of Mice, Ferrets, and Rhesus Macaques with a Clinical Mumps Virus Isolate - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3700206/)
- [Establishing a small animal model for evaluating protective immunity against mumps virus - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0174444)
- [Evaluation of immunogenicity of mumps vaccine strains in cotton rat model - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0264410X25009375)
- [Mumps virus pathogenesis: Insights and knowledge gaps - Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/21645515.2016.1210745)
- [Presumed Cases of Mumps in Pregnancy: Clinical and Infection Control Implications - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3296145/)
- [Mumps: risk in pregnancy, infection in healthcare settings and MMR vaccine - GOV.UK](https://www.gov.uk/government/publications/mumps-risk-in-pregnancy-infection-in-healthcare-settings-and-mmr-vaccine/mumps-risk-in-pregnancy-infection-in-healthcare-settings-and-mmr-vaccine)
- [Prevention of measles, mumps and rubella: 40 years of global experience with M-M-RII - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8903938/)
- [Mumps: an Update on Outbreaks, Vaccine Efficacy, and Genomic Diversity - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7048016/)
- [Chapter 9: Mumps | Manual for the Surveillance of Vaccine-Preventable Diseases | CDC](https://www.cdc.gov/surv-manual/php/table-of-contents/chapter-9-mumps.html)
- [1D80 Mumps - ICD-11 MMS](https://www.findacode.com/icd-11/code-1208294714.html)