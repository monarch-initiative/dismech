---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T11:02:24.166356'
end_time: '2026-06-29T11:07:52.408999'
duration_seconds: 328.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Microscopic Polyangiitis
  mondo_id: ''
  category: Autoimmune
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
  - claude-opus-4-8[1m]
  web_search_requests: 11
  num_turns: 13
  total_cost_usd: 2.3037124999999996
  session_id: cc6c81f9-47e5-4b61-9f0d-3d923b899ae1
  stop_reason: end_turn
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microscopic Polyangiitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Microscopic Polyangiitis** covering all of the
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

# Comprehensive Research Report: Microscopic Polyangiitis (MPA)

> **Scope note:** MPA is one of the three ANCA-associated vasculitides (AAV), alongside granulomatosis with polyangiitis (GPA) and eosinophilic granulomatosis with polyangiitis (EGPA). Much of the strongest mechanistic and trial evidence is generated at the level of "MPO-ANCA AAV" or "AAV" rather than MPA in isolation; I flag where evidence is MPA-specific versus AAV-wide. This is a disease-level (aggregated) synthesis from ontologies, registries, consensus nomenclature, and primary literature — not individual EHR-derived patient data.

---

## 1. Disease Information

**Overview.** Microscopic polyangiitis is a primary systemic, pauci-immune, necrotizing small-vessel vasculitis affecting capillaries, venules, and arterioles (and occasionally small arteries), *without* granulomatous inflammation and *without* asthma/eosinophilia (the features that distinguish it from GPA and EGPA respectively). It is strongly associated with anti-neutrophil cytoplasmic antibodies (ANCA), predominantly the myeloperoxidase-specific perinuclear pattern (MPO-ANCA/p-ANCA). Its clinical hallmark is the **pulmonary–renal syndrome**: pauci-immune necrotizing crescentic glomerulonephritis plus alveolar capillaritis with diffuse alveolar hemorrhage. MPA is the most common cause of pulmonary–renal vasculitic syndrome.

The 2012 Revised International Chapel Hill Consensus Conference (CHCC) defines MPA as *"Necrotizing vasculitis, with few or no immune deposits, predominantly affecting small vessels... Necrotizing arteritis involving small and medium arteries may be present. Necrotizing glomerulonephritis is very common. Pulmonary capillaritis often occurs. Granulomatous inflammation is absent"* (Jennette JC et al., *Arthritis Rheum.* 2013;65:1–11, **PMID:23045170**).

**Key identifiers.**
- **MONDO:** MONDO:0007179 (microscopic polyangiitis) — *recommend verifying with OAK against the local MONDO build before committing.*
- **Orphanet:** ORPHA:727 (citable as `ORPHA:727` in the structured cache; Orphanet lists prevalence band 1–9/100,000)
- **ICD-10-CM:** M31.7; **ICD-11:** 4A44.A2 (Microscopic polyangiitis)
- **MeSH:** D055953 ("Microscopic Polyangiitis")
- **SNOMED CT:** 239928004
- **OMIM:** No single Mendelian OMIM entry (MPA is multifactorial/polygenic, not monogenic); susceptibility is captured in GWAS rather than an OMIM phenotype number.
- **UMLS CUI:** C0343192

**Synonyms / alternative names.** Microscopic polyarteritis; microscopic polyarteritis nodosa (historical/obsolete — MPA was split off from classic polyarteritis nodosa); MPA; MPO-ANCA-associated vasculitis (when MPO-positive). Note: "microscopic polyarteritis nodosa" is a deprecated synonym — the CHCC explicitly separates MPA (small-vessel, ANCA-associated) from polyarteritis nodosa (medium-vessel, ANCA-negative).

Sources: [Orphanet ORPHA:727](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=727); [ICD-10 M31.7](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M30-M36/M31-/M31.7); [StatPearls MPA](https://www.ncbi.nlm.nih.gov/books/NBK531484/).

---

## 2. Etiology

MPA is **multifactorial and polygenic** — there is no single causal gene. Disease arises from a combination of genetic susceptibility (chiefly HLA class II), environmental triggers, and a loss of immune tolerance to neutrophil granule antigens (predominantly MPO), culminating in pathogenic ANCA.

**Primary causal factors / mechanism.** Breakdown of self-tolerance to myeloperoxidase → generation of MPO-ANCA → ANCA-mediated activation of cytokine-primed neutrophils → small-vessel necrotizing inflammation. (Mechanism detailed in §6.)

**Genetic risk factors.** The landmark European GWAS by Lyons et al. (*N Engl J Med.* 2012;367:214–223, **PMID:22808956**) established that AAV genetics segregate **by ANCA serotype rather than by clinical syndrome**: PR3-ANCA associates with *HLA-DP*, *SERPINA1* (α1-antitrypsin), and *PRTN3* (proteinase 3), whereas **MPO-ANCA (and thus most MPA) associates with HLA-DQ** (*"anti-myeloperoxidase ANCA with HLA-DQ"*). Key MPA/MPO-ANCA susceptibility signals:
- **HLA-DQ** (*HLA-DQA2/HLA-DQB1*) — the dominant MPO-ANCA locus in Europeans (suggest gene descriptors `HLA-DQB1` hgnc:4944, `HLA-DQA1` hgnc:4942).
- East Asian populations: **HLA-DRB1\*09:01–DQB1\*03:03 haplotype** is a major MPA/MPO-AAV risk haplotype (common in East Asians, rare in Europeans). The **DRB1\*13:02** allele is protective against MPO-AAV/MPA in Japanese cohorts.
- Non-HLA candidate loci with weaker/population-specific support: *TYK2* (tyrosine kinase 2; Guangxi population study), *PTPN22*, *CTLA4*, *IRF5*. These are susceptibility modifiers, not causal mutations.

**Environmental risk factors.**
- **Silica/silicon dust exposure** — the best-supported environmental association, particularly for MPO-ANCA/MPA; meta-analysis of case-control studies shows positive association with AAV. Mechanistically, silica is an NLRP3-inflammasome activator (IL-1β/IL-18) and can drive neutrophil/lymphocyte activation. (Hogan SL et al. and subsequent meta-analyses.)
- **Drugs (drug-induced AAV, often high-titer MPO-ANCA)** — **propylthiouracil** and other antithyroid thionamides, **hydralazine**, **minocycline**, **penicillamine**, **levamisole-adulterated cocaine**, and some anti-TNF agents. Drug-induced disease often shows high-titer MPO-ANCA plus other autoantibodies (e.g., ANA, anti-elastase) and may remit on withdrawal.
- **Infection** — proposed triggering via molecular mimicry and neutrophil priming (e.g., *Staphylococcus aureus* nasal carriage is better established for GPA; bacterial LPS amplifies anti-MPO injury experimentally).
- **Age** (older adults), **male sex** (modest male predominance), and geography (see §9).

**Protective factors.** Specific HLA alleles (e.g., **HLA-DRB1\*13:02** in East Asians) are genetically protective. No robust dietary or lifestyle protective factor is established. (Smoking has been variably associated with PR3-AAV risk; data for MPA-protection are not solid.)

**Gene–environment interaction.** The leading model is that silica or drug exposure provides neutrophil priming/inflammasome activation and antigen exposure on a permissive HLA-DQ background, lowering the threshold for MPO-ANCA generation. The **LAMP-2/molecular-mimicry hypothesis** (Kain R et al., *Nat Med.* 2008;14:1088–1096, **PMID:18836458**) proposes that antibodies against human LAMP-2 cross-react with the bacterial adhesin FimH, linking infection to autoimmunity — though this remains debated and not consistently replicated.

Sources: [Lyons et al. NEJM 2012 (PMID:22808956)](https://pubmed.ncbi.nlm.nih.gov/22808956/); [Genetic susceptibility to AAV review (PMC4233908)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4233908/); [Environmental factors in AAV (PMC9479327)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9479327/); [HLA-DRB1*13:02 protective study (PMC4868057)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4868057/).

---

## 3. Phenotypes

MPA is a multisystem disease. Frequencies are approximate, pooled from cohort series (e.g., French Vasculitis Study Group, EUVAS). Suggested HPO terms in parentheses.

**Constitutional / prodromal (very frequent, 60–90%)**
- Fever (**HP:0001945**), weight loss (**HP:0001824**), fatigue/malaise (**HP:0012378**), myalgia (**HP:0003326**), arthralgia/arthritis (**HP:0002829 / HP:0001369**). Often a weeks-to-months prodrome.

**Renal — the dominant organ (very frequent, ~80–100%; defining feature)**
- Rapidly progressive (crescentic) glomerulonephritis (**HP:0000097** Glomerulopathy; **HP:0012622** Chronic kidney disease; **HP:0100820** Glomerulopathy with renal insufficiency).
- Hematuria (**HP:0000790**), proteinuria (**HP:0000093**), red-cell casts, elevated serum creatinine / acute kidney injury (**HP:0001919**). Renal involvement is more frequent and often more chronic/insidious in MPA than in GPA.

**Pulmonary (frequent, ~25–55%)**
- Diffuse alveolar hemorrhage from pulmonary capillaritis (**HP:0002107** Pneumothorax — no; better: **HP:0002105** Hemoptysis; **HP:0002883** alveolar hemorrhage is captured via Pulmonary hemorrhage **HP:0040223**), dyspnea (**HP:0002094**).
- **Interstitial lung disease/pulmonary fibrosis (HP:0006530 / HP:0002206)** — increasingly recognized as an MPO-ANCA/MPA-associated phenotype (UIP-pattern fibrosis), sometimes predating vasculitis by years.

**Cutaneous (frequent, ~30–60%)**
- Palpable purpura/leukocytoclastic vasculitis (**HP:0000979** Purpura; **HP:0011276** Vascular skin abnormality), livedo, skin ulcers, splinter hemorrhages, nailfold infarcts.

**Neurological (frequent, ~30–70%)**
- **Peripheral neuropathy — mononeuritis multiplex** (**HP:0007180** Mononeuritis multiplex; **HP:0009830** Peripheral neuropathy) — a hallmark of small-vessel vasculitic nerve ischemia.
- CNS involvement is less common (~10%); pachymeningitis, cerebral vasculitis.

**Gastrointestinal (occasional, ~30–50%)**
- Abdominal pain (**HP:0002027**), GI bleeding (**HP:0002239**), mesenteric ischemia.

**ENT / ocular (occasional; LESS than GPA)** — episcleritis/scleritis (**HP:0100534**), but destructive upper-airway granulomatous disease is characteristically **absent** (a key MPA-vs-GPA discriminator).

**Cardiac (less common, ~10–20%)** — pericarditis, cardiomyopathy.

**Laboratory abnormalities (phenotype "lab" type).**
- **MPO-ANCA / p-ANCA positivity** (~58–70% of MPA; PR3-ANCA in ~25–30%; ~10% ANCA-negative). LOINC for MPO-ANCA: e.g., LOINC:16718-0 (Myeloperoxidase Ab).
- Elevated CRP/ESR (**HP:0011227** Elevated CRP; **HP:0003565** Elevated ESR), normocytic anemia (**HP:0001903**), elevated creatinine, active urinary sediment, occasionally eosinophilia (mild; if marked, reconsider EGPA).

**Onset/severity/course.** Adult-onset (median ~60 yr); course ranges from indolent/"very slowly progressive" renal-limited disease to fulminant pulmonary–renal syndrome. Severity is **variable**; progression is typically **relapsing–remitting** with treatment, but renal damage accrues with each flare.

**Quality-of-life impact.** Substantial: fatigue, chronic kidney disease/dialysis dependence, peripheral neuropathic pain and motor deficits, and treatment-related morbidity (steroid effects, infection) dominate. Patient-reported outcomes (SF-36, EQ-5D, AAV-specific PRO) show persistent fatigue and physical-role limitation even in remission.

Sources: [StatPearls MPA](https://www.ncbi.nlm.nih.gov/books/NBK531484/); [Medscape MPA Practice Essentials](https://emedicine.medscape.com/article/334024-overview); [Kidney-biopsy phenotypes (PMC10702060)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10702060/).

---

## 4. Genetic / Molecular Information

- **Causal genes:** None (non-Mendelian). MPA is a complex-trait autoimmune disease.
- **Susceptibility loci (germline, common variants):**
  - **HLA-DQ** region (*HLA-DQA2*, *HLA-DQB1*) — dominant MPO-ANCA/MPA association in Europeans (Lyons et al., **PMID:22808956**). Quote: the GWAS found *"a genetic distinction between the two major ANCA serologic subgroups... anti-proteinase 3 ANCA was associated with HLA-DP... whereas anti-myeloperoxidase ANCA was associated with HLA-DQ."*
  - **HLA-DRB1\*09:01–DQB1\*03:03** risk haplotype and **HLA-DRB1\*13:02** protective allele in East Asians.
  - Weaker/inconsistent non-HLA candidates: *TYK2*, *PTPN22*, *CTLA4*, *IRF5*, *SERPINA1* (the latter more PR3-AAV).
- **Variant classification / type:** These are common **risk SNPs/HLA alleles** (susceptibility, not ACMG "pathogenic" Mendelian variants). Allele frequencies are population-stratified (HLA-DQ/DRB1 frequencies vary widely by ancestry; see gnomAD/AFND for HLA). No somatic driver; etiology is germline-background + acquired autoimmunity.
- **Functional consequence:** HLA class II risk alleles are thought to favor presentation of MPO-derived peptides to autoreactive CD4⁺ T cells, promoting B-cell help and MPO-ANCA production (loss of tolerance, not a coding loss/gain-of-function in an enzyme).
- **Modifier genes:** *SERPINA1* (α1-antitrypsin) deficiency alleles (e.g., PiZ/PiS) influence PR3-AAV severity more than MPA; complement-pathway genetics may modify severity.
- **Epigenetics:** Defective epigenetic silencing of *MPO* and *PRTN3* in neutrophils (loss of repressive H3K27me3; aberrant DNA methylation) increases autoantigen expression in AAV (Ciavatta DJ et al., *J Clin Invest.* 2010;120:3209–3219, **PMID:20697158**). This is a notable AAV epigenetic mechanism rather than MPA-specific.
- **Chromosomal abnormalities:** None characteristic.

Suggested gene descriptors: `HLA-DQB1` (hgnc:4944), `HLA-DQA1` (hgnc:4942), `HLA-DRB1` (hgnc:4948), `MPO` (hgnc:7218), `PRTN3` (hgnc:9495), `SERPINA1` (hgnc:8941).

---

## 5. Environmental Information

- **Occupational/toxic:** **Silica (crystalline silicon dioxide)** dust — strongest environmental link to MPO-ANCA/MPA (CHEBI: silicon dioxide CHEBI:9161). Also organic solvents (weaker, inconsistent).
- **Drugs (CHEBI suggestions):** propylthiouracil (CHEBI:8502), hydralazine (CHEBI:5613), minocycline (CHEBI:50694), penicillamine (CHEBI:7959), levamisole (CHEBI:6432, as cocaine adulterant). These can induce MPO-ANCA AAV resembling MPA.
- **Lifestyle:** No strong dietary/exercise driver; smoking links are stronger for PR3-AAV.
- **Infectious agents:** No single causative organism. Bacterial priming (LPS) amplifies anti-MPO injury experimentally; *S. aureus* carriage is more relevant to GPA relapse. The LAMP-2/FimH molecular-mimicry hypothesis (Gram-negative fimbriae) links infection to MPO/LAMP-2 autoimmunity but is unconfirmed.

Sources: [Environmental factors in AAV (PMC9479327)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9479327/); [Hydralazine-induced AAV (PMC10667955)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10667955/).

---

## 6. Mechanism / Pathophysiology

The pathogenesis is among the best-characterized of any autoimmune vasculitis, with strong experimental (mouse) and human evidence supporting a **directly pathogenic role for ANCA**.

**Causal chain (upstream → downstream):**

1. **Loss of tolerance to MPO → MPO-ANCA generation.** On a permissive HLA-DQ background, with environmental priming (silica, drugs, infection) and epigenetic de-repression of *MPO*, autoreactive T/B cells generate anti-MPO IgG. (Autoantigen: myeloperoxidase, UniProt **P05164**, normally in neutrophil azurophilic/primary granules.)

2. **Neutrophil priming.** Pro-inflammatory cytokines (e.g., **TNF-α, IL-1β, C5a**) prime circulating neutrophils, translocating MPO (and PR3) from granules to the cell surface where ANCA can bind. GO process suggestions: `GO:0042119` neutrophil activation; `GO:0002690` positive regulation of leukocyte chemotaxis.

3. **ANCA-mediated neutrophil activation.** Anti-MPO IgG engages surface MPO and **Fcγ receptors (FcγRIIa/FcγRIIIb)**, triggering the respiratory burst, degranulation, and release of reactive oxygen species and lytic enzymes. (`GO:0045730` respiratory burst; `GO:0043312` neutrophil degranulation.)

4. **Endothelial adhesion and transmigration → necrotizing capillaritis.** Activated neutrophils adhere to and damage small-vessel endothelium (capillaries, venules, arterioles), causing **leukocytoclasia, fibrinoid necrosis, and lysis of the vessel wall** with little/no immunoglobulin deposition ("pauci-immune"). Cell types: neutrophil (CL:0000775), monocyte/macrophage (CL:0000235), vascular endothelial cell (CL:0000115). Anatomy: capillary (UBERON:0001982), glomerular capillary (UBERON:0005751), pulmonary alveolus (UBERON:0002299).

5. **NETosis and complement amplification.** ANCA-stimulated neutrophils release **neutrophil extracellular traps (NETs)** — chromatin/DNA decorated with MPO, PR3, and histones. NETs (a) further expose MPO to perpetuate autoimmunity, (b) directly injure endothelium, and (c) **activate the alternative complement pathway**, generating **C5a**. C5a is a potent neutrophil chemoattractant that primes more neutrophils — a feed-forward amplification loop. (Kessenbrock K et al., *Nat Med.* 2009;15:623–625, **PMID:19465931**, *"Netting neutrophils in autoimmune small-vessel vasculitis."*) GO: `GO:0072576` (NET-related processes captured via `GO:0006955` immune response / extracellular trap).

6. **The complement C5a–C5aR axis as therapeutic target.** Experimental anti-MPO GN is markedly attenuated by deficiency of **complement factor B or C5**, or by **C5aR (CD88) blockade** — establishing the alternative pathway as essential and rationalizing the C5aR antagonist **avacopan** (see §12). Schreiber A et al. demonstrated C5aR's role in murine anti-MPO disease (*J Am Soc Nephrol.* 2009;20:289–298, **PMID:19092138**).

**Definitive experimental proof (model-organism evidence):** Xiao H, Heeringa P, Hu P, ... Falk RJ, Jennette JC. *"Antineutrophil cytoplasmic autoantibodies specific for myeloperoxidase cause glomerulonephritis and vasculitis in mice."* *J Clin Invest.* 2002;110:955–963 (**PMID:12370273**) — passive transfer of anti-MPO IgG into wild-type **and** into *Rag2⁻/⁻* mice (lacking T and B cells) produced pauci-immune necrotizing crescentic glomerulonephritis, proving ANCA IgG is directly pathogenic. The follow-up (Xiao H et al., *Am J Pathol.* 2005;167:39–45, **PMID:15972950**) showed **neutrophil depletion completely prevents** anti-MPO IgG-induced glomerulonephritis, proving the neutrophil is the obligate effector.

**Tissue damage modes:** ischemic + inflammatory necrosis (fibrinoid necrosis of vessel wall), oxidative injury (ROS), NET-mediated endothelial cytotoxicity, and downstream crescent formation (parietal epithelial proliferation responding to fibrin/plasma leakage into Bowman's space).

**Molecular profiling:** Transcriptomic studies of AAV blood/kidney show neutrophil-granule and interferon signatures; granulocyte subsets predict treatment response (RAVE reanalysis). Proteomics confirms circulating MPO, calprotectin (S100A8/A9), and complement Bb/C5a as activity biomarkers.

Sources: [Xiao et al. JCI 2002 (PMC151154)](https://ncbi.nlm.nih.gov/pmc/articles/PMC151154); [Xiao et al. Am J Pathol 2005 (PMID:15972950)](https://pubmed.ncbi.nlm.nih.gov/15972950/); [Kessenbrock NETs Nat Med 2009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4831636/); [Targeting complement in AAV (PMC12783592)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12783592/).

---

## 7. Anatomical Structures Affected

- **Primary organs:** **Kidney** (UBERON:0002113) — glomerulus (UBERON:0000074), glomerular capillary tuft; **Lung** (UBERON:0002048) — alveolar capillary bed (UBERON:0002299).
- **Secondary/other organs & systems:** peripheral nerves (UBERON:0001021; vasa nervorum), skin (UBERON:0002097), gastrointestinal tract (UBERON:0000160), eye (UBERON:0000970), heart/pericardium (UBERON:0002348), CNS meninges (UBERON:0002360).
- **Body systems:** renal/urinary, respiratory, peripheral nervous, integumentary, cardiovascular (small vessels systemically), digestive.
- **Vessel level:** capillaries, post-capillary venules, arterioles (and small arteries) — i.e., **small-vessel** vasculitis (UBERON:0001982 capillary; UBERON:0001980 blood vessel).
- **Tissue/cell level:** vascular endothelium (endothelial cell CL:0000115), neutrophils (CL:0000775) as effectors, monocytes/macrophages (CL:0000235), glomerular parietal epithelial cells (crescents). Connective tissue of vessel walls undergoes fibrinoid necrosis.
- **Subcellular:** neutrophil **azurophilic/primary granule** (GO:0042582) housing MPO; cell surface (translocated MPO); extracellular space (NETs, GO:0005615).
- **Localization/laterality:** systemic and **bilateral** (e.g., bilateral diffuse alveolar hemorrhage, diffuse glomerular involvement); nerve involvement is typically **asymmetric/multifocal** (mononeuritis multiplex).

---

## 8. Temporal Development

- **Onset:** Adult, typically **late-onset** (peak 6th–7th decade; median ~60 yr); rare in children. Pattern ranges from **insidious/subacute** (months of constitutional symptoms, slowly rising creatinine) to **acute/fulminant** (rapidly progressive GN ± alveolar hemorrhage). A "very slowly progressive" MPA subset is increasingly described.
- **Progression / stages:** active (induction) → remission → potential relapse → chronic damage (CKD/ESKD, pulmonary fibrosis, neuropathic deficits). Renal histology stratifies prognosis (Berden classification: focal > crescentic > mixed > sclerotic, in order of worsening renal outcome — Berden AE et al., *J Am Soc Nephrol.* 2010;21:1628–1636, **PMID:20616173**).
- **Course pattern:** **relapsing–remitting** chronic disease. Relapse rates are **lower in MPO-ANCA/MPA than in PR3-ANCA/GPA**, but each relapse risks cumulative organ damage.
- **Duration:** chronic, lifelong susceptibility; rarely self-limited (except some drug-induced cases that remit on withdrawal).
- **Remission:** treatment-induced (immunosuppression); spontaneous remission is uncommon.
- **Critical window:** early diagnosis and prompt immunosuppression before irreversible glomerular sclerosis (dialysis-dependent AKI) or fatal alveolar hemorrhage — the chief determinant of long-term renal survival.

---

## 9. Inheritance and Population

- **Epidemiology:** AAV overall incidence ~1.2–3.3/100,000/yr; **MPA incidence ~2.4–10.1 per million/yr** depending on region; prevalence in the tens per million. A worldwide systematic review/meta-analysis (Watts/others) reports geographic and serotype gradients.
- **Geographic / ethnic gradient:** **MPA (MPO-ANCA) predominates in Southern Europe and especially East Asia (Japan, China)**, whereas **GPA (PR3-ANCA) predominates in Northern Europe**. In Japan, the great majority of AAV is MPO-ANCA/MPA. This north–south / Europe–Asia gradient mirrors the HLA-DQ vs HLA-DP serotype genetics.
- **Inheritance:** **Not Mendelian** — multifactorial/polygenic with environmental contribution. No defined penetrance, expressivity, anticipation, founder effect, consanguinity role, or carrier frequency in the classical sense.
- **Sex ratio:** roughly equal to slight **male predominance** (~1.0–1.8 : 1, M:F), varying by cohort.
- **Age distribution:** strongly **age-associated**, rising with age, peak 65–74 yr.

Sources: [Worldwide incidence/prevalence meta-analysis (PMC9106044)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9106044/); [Epidemiology of GPA/MPA in France (PMID:36108505)](https://pubmed.ncbi.nlm.nih.gov/36108505/).

---

## 10. Diagnostics

**Serology (cornerstone).**
- **Indirect immunofluorescence** → perinuclear (p-ANCA) pattern; confirmed by **antigen-specific MPO-ANCA ELISA** (positive in ~58–70% of MPA). PR3-ANCA in a minority; ~10% ANCA-negative. (LOINC: MPO Ab 16718-0; PR3 Ab 14283-7.)

**Laboratory.** Serum creatinine/eGFR, urinalysis with microscopy (**dysmorphic hematuria, RBC casts, proteinuria** = active "nephritic" sediment), CRP/ESR, CBC (normocytic anemia), complement (usually normal — helps separate from immune-complex vasculitis), anti-GBM antibody (to exclude/co-diagnose Goodpasture, which can coexist in "double-positive" patients).

**Imaging.** Chest CT/HRCT for alveolar hemorrhage (ground-glass/consolidation) and interstitial fibrosis (UIP pattern); bronchoscopy with **serial bronchoalveolar lavage showing progressively bloodier returns ± hemosiderin-laden macrophages** confirms diffuse alveolar hemorrhage.

**Biopsy (diagnostic gold standard).**
- **Renal biopsy:** **pauci-immune focal necrotizing and crescentic glomerulonephritis**; immunofluorescence shows scant/absent immunoglobulin and complement (distinguishing from immune-complex and anti-GBM disease). Classified by Berden categories (focal/crescentic/mixed/sclerotic).
- **Other tissue:** skin (leukocytoclastic vasculitis), sural nerve (necrotizing vasculitis of vasa nervorum), lung (capillaritis). **Absence of granulomas** supports MPA over GPA.

**Electrophysiology.** Nerve conduction studies/EMG document axonal, asymmetric sensorimotor neuropathy (mononeuritis multiplex).

**Genetic testing.** **Not used for diagnosis** (polygenic disease); HLA/GWAS findings are research-grade risk markers, not clinical tests. No WGS/WES/panel/karyotype/repeat-expansion indication.

**Classification criteria.** The **2022 ACR/EULAR Classification Criteria for MPA** (Suppiah R et al., *Arthritis Rheumatol.* 2022;74:400–406, **PMID:35106964**; companion *Ann Rheum Dis.* 2022) — applied only after diagnosing small/medium-vessel vasculitis and excluding mimics; a cumulative **score ≥ 5** classifies MPA. Weighted items include **+ p-ANCA/MPO-ANCA (+6)**, pauci-immune GN (+3), and **negative weights for nasal/sinus involvement, c-ANCA/PR3 (−1), and eosinophilia (−4)** — i.e., features that point toward GPA or EGPA reduce the MPA score. (Earlier framework: 2012 CHCC nomenclature and the EMA/Watts algorithm.)

**Differential diagnosis.** GPA (granulomas, ENT destruction, PR3-ANCA), EGPA (asthma, eosinophilia), anti-GBM/Goodpasture disease, immune-complex small-vessel vasculitis (IgA vasculitis, cryoglobulinemic, lupus nephritis — these are *not* pauci-immune), polyarteritis nodosa (medium-vessel, ANCA-negative), infective endocarditis, and drug-induced AAV.

**Screening.** No population screening (uncommon, no presymptomatic test). ANCA testing is targeted to clinical suspicion (renal–pulmonary syndrome, mononeuritis multiplex, etc.).

Sources: [2022 ACR/EULAR MPA criteria (Wiley)](https://acrjournals.onlinelibrary.wiley.com/doi/abs/10.1002/art.41983); [Berden histopathologic classification (PMID:20616173)](https://pubmed.ncbi.nlm.nih.gov/20616173/).

---

## 11. Outcome / Prognosis

- **Survival:** Untreated, AAV with GN is frequently fatal within ~1 year; with modern immunosuppression, **5-year survival ~70–85%**. Early mortality is driven by active vasculitis (alveolar hemorrhage, sepsis from immunosuppression); later mortality by infection, cardiovascular disease, ESKD, and malignancy.
- **Renal outcome:** A major determinant; substantial fraction progress to **chronic kidney disease/ESKD** (dialysis), especially with crescentic/sclerotic biopsy class and high presenting creatinine.
- **Mortality predictors:** older age, higher creatinine/dialysis at presentation, alveolar hemorrhage, higher disease activity (BVAS), and infection. The **Five-Factor Score (FFS, 1996/2009 revision; Guillevin L et al.)** prognosticates necrotizing vasculitides.
- **Relapse:** lower in MPO-ANCA/MPA than PR3-ANCA/GPA; persistent/rising ANCA and PR3 serotype increase relapse risk.
- **Morbidity/QoL:** CKD, neuropathic pain/weakness, pulmonary fibrosis, plus treatment toxicity (glucocorticoid effects, infection, infertility/cytopenia from cyclophosphamide). Damage accrual is measured by the Vasculitis Damage Index (VDI).
- **Prognostic biomarkers:** ANCA titer trajectory (esp. PR3), renal histology class (Berden), the ANCA Renal Risk Score, and emerging complement activation markers (urinary/plasma C5a, Bb).

Sources: [Slowly vs rapidly progressive MPA (PMC11170224)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11170224/); [Austrian ÖGN/ÖGR 2023 consensus (PMC10511611)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10511611/).

---

## 12. Treatment

Management is split into **remission induction** and **remission maintenance**, plus adjuncts. Suggested MAXO/NCIT terms noted.

**Remission induction.**
- **Rituximab** (anti-CD20 B-cell depletion; therapeutic_modality MONOCLONAL_ANTIBODY) — first-line, non-inferior to cyclophosphamide and superior in relapsing disease. **RAVE trial** (Stone JH et al., *N Engl J Med.* 2010;363:221–232, **PMID:20647199**). NCIT:C2778 (Rituximab); MAXO chemotherapy/immunotherapy term `MAXO:0000647` or pharmacotherapy NCIT:C15986.
- **Cyclophosphamide** (alkylating immunosuppressant; CHEBI:4026) — classic induction, with the **CYCLOPS** pulsed-IV regimen reducing cumulative dose vs oral. Pharmacotherapy NCIT:C15986; cytotoxic.
- **Glucocorticoids** (e.g., prednisone, CHEBI:8378; methylprednisolone pulses) — backbone of induction. **PEXIVAS** (Walsh M et al., *N Engl J Med.* 2020;382:622–631, **PMID:32053298**) showed a **reduced-dose glucocorticoid regimen is non-infe­rior** for death/ESKD and **lowers serious infections** — establishing steroid-sparing as standard. MAXO `MAXO:0000058`-class glucocorticoid therapy.
- **Avacopan** (oral **C5a-receptor/CD88 antagonist**, ATC, brand TAVNEOS; FDA-approved Oct 2021; CHEBI/NCIT:C168722) — **ADVOCATE trial** (Jayne DRW et al., *N Engl J Med.* 2021;384:599–609, **PMID:33596356**): added to rituximab or cyclophosphamide, avacopan was **non-inferior at week 26 and superior for sustained remission at week 52** while enabling glucocorticoid sparing. Mechanism directly targets the C5a–C5aR amplification loop (§6). therapeutic_modality SMALL_MOLECULE.
- **Plasma exchange (therapeutic plasmapheresis; MAXO:0000063):** PEXIVAS showed **no overall benefit** on death/ESKD; now reserved for selected severe cases (e.g., severe alveolar hemorrhage or concurrent anti-GBM/very severe renal failure), per shared decision-making.

**Remission maintenance.**
- **Rituximab maintenance** — **MAINRITSAN** trials (Guillevin L et al., *N Engl J Med.* 2014;371:1771–1780, **PMID:25372085**) showed scheduled **rituximab superior to azathioprine** for preventing relapse; pooled long-term MAINRITSAN data confirm durable benefit (500 mg every 6 months × 18 months). RITAZAREM supports rituximab maintenance after rituximab induction in relapsing disease.
- **Azathioprine** (CHEBI:2948) or **methotrexate** (non-renal/limited disease; CHEBI:44185) or **mycophenolate mofetil** as alternatives.

**Pharmacogenomics.** **TPMT/NUDT15** genotyping before azathioprine to avoid severe myelosuppression (CPIC guideline). Cyclophosphamide and glucocorticoid metabolism vary individually but lack actionable routine PGx.

**Supportive/prophylactic.** *Pneumocystis jirovecii* prophylaxis (trimethoprim-sulfamethoxazole) during intensive immunosuppression; osteoporosis prophylaxis with steroids; vaccination (non-live) before immunosuppression; dialysis/renal replacement for ESKD; rehabilitation for neuropathy.

**Treatment outcomes/adverse events.** Induction achieves remission in ~70–85% by 6 months. Major harms: **serious infection** (leading cause of early death, driven by glucocorticoid + cytotoxic exposure), cytopenias, malignancy (cyclophosphamide, esp. bladder cancer/MDS with high cumulative dose), infertility, and steroid toxicity — all motivating the steroid-/cyclophosphamide-sparing shift toward rituximab + avacopan.

**Experimental / pipeline.** Complement-pathway and B-cell–directed agents, **obinutuzumab** (anti-CD20), plasma-cell-directed therapy, and trials registered on ClinicalTrials.gov (e.g., avacopan real-world and combination studies; ITN/EUVAS programs).

Sources: [RAVE NEJM 2010](https://www.nejm.org/doi/full/10.1056/NEJMoa1404231) (and design); [MAINRITSAN pooled (PMID:37918894)](https://pubmed.ncbi.nlm.nih.gov/37918894/); [PEXIVAS (PMID:32053298)](https://pubmed.ncbi.nlm.nih.gov/32053298/); [ADVOCATE/avacopan NEJM 2021](https://www.nejm.org/doi/full/10.1056/NEJMoa2023386).

---

## 13. Prevention

- **Primary prevention:** No vaccine or established population-level prevention (etiology multifactorial). Modifiable-risk reduction: minimize **occupational silica exposure** (engineering controls, respiratory protection) and avoid culprit drugs (propylthiouracil, hydralazine, minocycline) in susceptible patients; consider alternative agents and discontinue promptly if drug-induced AAV is suspected.
- **Secondary prevention (early detection):** prompt ANCA testing and biopsy in at-risk presentations (renal–pulmonary syndrome, mononeuritis multiplex, unexplained RPGN) to begin therapy before irreversible organ damage. No asymptomatic screening program.
- **Tertiary prevention (complication avoidance):** scheduled maintenance immunosuppression to prevent relapse; infection prophylaxis (PJP, vaccination); cardiovascular and bone-health risk management; ANCA/clinical monitoring for early relapse capture.
- **Genetic counseling:** not applicable in the Mendelian sense — MPA is not inherited as a single-gene disorder, and familial recurrence is rare; reassurance is generally appropriate.
- **Public health/environmental:** workplace silica regulation is the principal population-level lever.

---

## 14. Other Species / Natural Disease

- **Taxonomy of natural disease:** ANCA-associated vasculitis is fundamentally a **human disease**; there is no well-established spontaneous MPA in companion animals analogous to the human syndrome. (NCBITaxon:9606 *Homo sapiens* for the disease; experimental disease is induced in **NCBITaxon:10090 *Mus musculus***.)
- **Orthologous genes:** *Mpo* (mouse, NCBI Gene 17523), enabling the murine anti-MPO model; *Prtn3* ortholog exists but the mouse PR3 model is far weaker than the MPO model (a known cross-species limitation).
- **Veterinary/natural relevance:** No significant naturally occurring veterinary counterpart catalogued in OMIA; reported animal vasculitides differ mechanistically. **No zoonotic potential** (autoimmune, non-transmissible).
- **Comparative biology:** The conservation of MPO biology and neutrophil effector mechanisms is what makes the **mouse passive-transfer model** translationally informative, but mice do not spontaneously develop MPA — disease must be induced.

---

## 15. Model Organisms

- **Mouse (the workhorse model):**
  - **Passive-transfer anti-MPO model** (Xiao/Falk/Jennette): immunize *Mpo⁻/⁻* mice with mouse MPO → transfer anti-MPO IgG (or splenocytes) into wild-type or *Rag2⁻/⁻* recipients → **pauci-immune necrotizing crescentic glomerulonephritis and small-vessel vasculitis** that closely mimics human MPA (**PMID:12370273**). This model demonstrated direct ANCA pathogenicity and the obligatory role of neutrophils (**PMID:15972950**).
  - **Amplification/induction:** bacterial **LPS** co-administration aggravates injury via **TNF-α**, supporting the priming/infection link (Huugen D et al., *Am J Pathol.* 2005, PMC1603449).
  - **Mechanistic dissection:** factor B–, C5–, and **C5aR-deficient** mice show attenuated disease, establishing the alternative-complement/C5a axis and validating avacopan's target (Schreiber A et al., **PMID:19092138**).
  - **Genetic model types:** knockout (*Mpo⁻/⁻* immunization host; complement-gene KOs), and immunodeficient recipients (*Rag2⁻/⁻*) to isolate the antibody effector arm.
- **Rat:** the **WKY rat** develops experimental anti-MPO crescentic GN and is used to study epitope-specific pathogenicity.
- **In vitro / cellular:** human neutrophil activation assays (ANCA-induced respiratory burst, degranulation, NETosis), endothelial co-culture cytotoxicity, and complement-activation assays on NETs.
- **Phenotype recapitulation:** the murine anti-MPO model faithfully reproduces **pauci-immune necrotizing crescentic GN** and pulmonary capillaritis. **Limitations:** it is an induced (passive-transfer) model rather than spontaneous autoimmunity, does not capture the human break-of-tolerance/HLA-restricted T-cell priming, under-models the chronic relapsing course, and PR3-ANCA disease is poorly modeled — so this is best classified as `MODEL_ORGANISM` evidence that recapitulates effector mechanisms but not the full human initiation phase (a candidate `HUMAN_MODEL_MISMATCH` note for the initiation/tolerance arm).
- **Resources:** MGI (mouse *Mpo*, complement KO strains), Frontiers review "Animal Models of ANCA-Associated Vasculitis" (PMC, 2020).

Sources: [Animal models of AAV (Frontiers 2020)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.00525/full); [Xiao JCI 2002](https://ncbi.nlm.nih.gov/pmc/articles/PMC151154); [Xiao Am J Pathol 2005](https://pubmed.ncbi.nlm.nih.gov/15972950/).

---

## Key Citations (PMID-anchored, for dismech evidence items)

| Claim | Reference | PMID |
|---|---|---|
| CHCC nomenclature / MPA definition | Jennette JC et al. *Arthritis Rheum.* 2013;65:1–11 | 23045170 |
| MPO-ANCA↔HLA-DQ; PR3-ANCA↔HLA-DP (GWAS) | Lyons PA et al. *N Engl J Med.* 2012;367:214–223 | 22808956 |
| Anti-MPO IgG directly causes pauci-immune NCGN (mouse) | Xiao H et al. *J Clin Invest.* 2002;110:955–963 | 12370273 |
| Neutrophils obligatory for anti-MPO GN | Xiao H et al. *Am J Pathol.* 2005;167:39–45 | 15972950 |
| NETs in AAV pathogenesis | Kessenbrock K et al. *Nat Med.* 2009;15:623–625 | 19465931 |
| C5aR essential in murine anti-MPO disease | Schreiber A et al. *J Am Soc Nephrol.* 2009;20:289–298 | 19092138 |
| Renal histopathologic classification | Berden AE et al. *J Am Soc Nephrol.* 2010;21:1628–1636 | 20616173 |
| LAMP-2/FimH molecular mimicry hypothesis | Kain R et al. *Nat Med.* 2008;14:1088–1096 | 18836458 |
| Epigenetic autoantigen de-repression | Ciavatta DJ et al. *J Clin Invest.* 2010;120:3209–3219 | 20697158 |
| 2022 ACR/EULAR MPA classification criteria | Suppiah R et al. *Arthritis Rheumatol.* 2022;74:400–406 | 35106964 |
| Rituximab induction (RAVE) | Stone JH et al. *N Engl J Med.* 2010;363:221–232 | 20647199 |
| Rituximab maintenance (MAINRITSAN) | Guillevin L et al. *N Engl J Med.* 2014;371:1771–1780 | 25372085 |
| Reduced-dose steroids / PLEX (PEXIVAS) | Walsh M et al. *N Engl J Med.* 2020;382:622–631 | 32053298 |
| Avacopan / C5aR blockade (ADVOCATE) | Jayne DRW et al. *N Engl J Med.* 2021;384:599–609 | 33596356 |
| MAINRITSAN pooled long-term outcome | Charles P et al. *Ann Rheum Dis.* 2023 | 37918894 |

> **Curation caveats for the dismech entry:** (1) Verify **MONDO:0007179** and all ontology IDs with OAK before committing; the report suggests terms but they must pass `just validate-terms-file`. (2) **Every snippet must be re-fetched and substring-verified** via `just fetch-reference PMID:XXXX` — the abstract quotes paraphrased above are *leads*, not validated snippets (per the DR-output SOP and NEC preflight). (3) Tag mouse passive-transfer findings as `evidence_source: MODEL_ORGANISM`; keep them distinct from human-clinical phenotype support. (4) PMID:33596356 is the actual NEJM ADVOCATE paper (one web result showed an adjacent commentary PMID 34042398 — use 33596356 for the primary trial).

**Primary web sources used:**
- [Orphanet ORPHA:727](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=727)
- [StatPearls: Microscopic Polyangiitis](https://www.ncbi.nlm.nih.gov/books/NBK531484/)
- [Medscape: MPA Practice Essentials](https://emedicine.medscape.com/article/334024-overview)
- [Lyons et al. NEJM 2012 GWAS (PMID:22808956)](https://pubmed.ncbi.nlm.nih.gov/22808956/)
- [Genetic susceptibility to AAV review (PMC4233908)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4233908/)
- [Environmental factors in AAV (PMC9479327)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9479327/)
- [Xiao et al. JCI 2002 (PMC151154)](https://ncbi.nlm.nih.gov/pmc/articles/PMC151154)
- [Xiao et al. Am J Pathol 2005 (PMID:15972950)](https://pubmed.ncbi.nlm.nih.gov/15972950/)
- [NETs & alternative complement in AAV (PMC4831636)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4831636/)
- [Targeting complement in AAV (PMC12783592)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12783592/)
- [2022 ACR/EULAR MPA criteria (Suppiah, Wiley)](https://acrjournals.onlinelibrary.wiley.com/doi/abs/10.1002/art.41983)
- [ADVOCATE / Avacopan NEJM 2021](https://www.nejm.org/doi/full/10.1056/NEJMoa2023386)
- [PEXIVAS NEJM 2020 (PMID:32053298)](https://pubmed.ncbi.nlm.nih.gov/32053298/)
- [MAINRITSAN pooled analysis (PMID:37918894)](https://pubmed.ncbi.nlm.nih.gov/37918894/)
- [RAVE / rituximab maintenance NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1404231)
- [Worldwide AAV incidence/prevalence meta-analysis (PMC9106044)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9106044/)
- [Epidemiology of GPA/MPA in France (PMID:36108505)](https://pubmed.ncbi.nlm.nih.gov/36108505/)
- [Animal models of AAV (Frontiers 2020)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.00525/full)
- [Kidney-biopsy phenotypes of MPA (PMC10702060)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10702060/)
- [Austrian ÖGN/ÖGR 2023 GPA/MPA consensus (PMC10511611)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10511611/)