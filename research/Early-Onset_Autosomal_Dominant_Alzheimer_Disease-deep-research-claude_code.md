---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T15:05:55.501175'
end_time: '2026-07-31T15:11:38.813570'
duration_seconds: 343.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Early-Onset Autosomal Dominant Alzheimer Disease
  mondo_id: ''
  category: Neurodegenerative Disorder
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
  web_search_requests: 14
  num_turns: 21
  total_cost_usd: 1.6625238
  session_id: 1ff1ab7e-d42a-5ad6-b222-89444922f8c7
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Early-Onset Autosomal Dominant Alzheimer Disease
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disorder

## Research Objectives

Please provide a comprehensive research report on **Early-Onset Autosomal Dominant Alzheimer Disease** covering all of the
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

# Early-Onset Autosomal Dominant Alzheimer Disease (ADAD/EOFAD): Comprehensive Research Report

---

## 1. Disease Information

**Overview:** Early-Onset Autosomal Dominant Alzheimer Disease (ADAD, also called Early-Onset Familial Alzheimer Disease, EOFAD) is a fully penetrant, Mendelian form of Alzheimer's disease caused by pathogenic variants in *APP*, *PSEN1*, or *PSEN2*. It produces the same core neuropathological and clinical phenotype as sporadic late-onset AD (amyloid-β plaques, neurofibrillary tangles, progressive dementia) but with a much earlier, highly predictable age of onset — typically before age 65, and often in the 30s–50s — and with a family history consistent with autosomal dominant transmission across generations. ADAD accounts for a small minority of all AD (~1% of total AD cases; ~5–10% of early-onset AD, EOAD), but it has been disproportionately important to AD research because carriers can be identified presymptomatically decades before expected symptom onset, enabling prospective study of the full preclinical-to-symptomatic biomarker cascade (the basis of the Dominantly Inherited Alzheimer Network, DIAN).

**Key Identifiers:**
- **MONDO:** MONDO:0015140 (early-onset autosomal dominant Alzheimer disease)
- **Orphanet:** ORPHA:1020
- **OMIM (gene-specific subtypes):**
  - AD1 — OMIM:104300 (*APP*, 21q21.3)
  - AD3 — OMIM:607822 (*PSEN1*, 14q24.2)
  - AD4 — OMIM:606889 (*PSEN2*, 1q42.13)
  - Additional related OMIM entries returned by Orphanet cross-reference include 104310, 602096, 604154, 605055 (familial early-onset AD with coexisting amyloid and prion pathology), 605526, 606187, 607116, 609636, 609790, 611073, 611152, 611154 (locus/phenotype variant entries)
- **ICD-11:** 8A20.00 (Alzheimer disease, early onset) — ICD-10: G30.0
- **MeSH:** D000544 (Alzheimer Disease); no distinct MeSH term for the familial subtype specifically, indexed under "Alzheimer Disease" + genetic subheadings
- **HPO (disease-level phenotype set anchor):** HP:0002511 (Alzheimer disease); HP:0031060 (early-onset Alzheimer disease, if present in current HPO builds)

**Synonyms:** Early-onset familial Alzheimer disease (EOFAD); Familial Alzheimer disease (FAD); Autosomal dominant Alzheimer disease (ADAD); Dominantly Inherited Alzheimer Disease (DIAD, used specifically by the DIAN consortium); Presenilin-related familial Alzheimer disease.

**Data provenance:** Nearly all mechanistic and biomarker knowledge for ADAD is aggregated disease-level knowledge synthesized from large observational cohorts (DIAN Observational Study, the Colombian PSEN1 E280A "Paisa" kindred cohort, the UK/European ADAD case series) rather than isolated EHR mining — this is a rare-disease field built on international, prospectively phenotyped, longitudinally followed multi-generational kindreds. (Orphanet: [Early onset autosomal dominant Alzheimer disease](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=1020); GARD: [Early-onset autosomal dominant Alzheimer disease](https://rarediseases.info.nih.gov/diseases/12798/early-onset-autosomal-dominant-alzheimer-disease))

---

## 2. Etiology

**Disease causal factors:** ADAD is caused by heterozygous, fully penetrant (or near-fully penetrant) pathogenic variants in one of three genes, each converging on abnormal amyloid-β (Aβ) generation:
- ***PSEN1*** (presenilin-1, the catalytic subunit of γ-secretase) — the most common cause, accounting for ~69–70% of genetically-solved ADAD; over 300 pathogenic variants reported (missense predominant).
- ***APP*** (amyloid precursor protein) — missense variants near the β- or γ-secretase cleavage sites, or whole-gene duplication (as in Down syndrome trisomy 21, which produces an ADAD-like phenotype via *APP* gene-dosage) — ~13–16% of cases (variants) plus ~7.5% (duplications).
- ***PSEN2*** (presenilin-2, homologous γ-secretase subunit) — rarest cause (~2%), notably enriched in the Volga German kindreds (N141I variant).

Genetic screening studies place combined *APP*/*PSEN1*/*PSEN2* solve rates at roughly 60–70% of clinically defined familial (autosomal-dominant pedigree) early-onset AD (PLOS Medicine genetic screening study).

**Risk factors:**
- *Genetic:* Inheriting one causal variant is both necessary and (with near-complete penetrance) sufficient — this is a monogenic disorder, not a polygenic-susceptibility one. Modifier loci shift age of onset but do not determine disease occurrence: *APOE* genotype (ε4 accelerates amyloid accumulation timing in some cohorts, though effects are more modest/variable than in sporadic AD — PSEN1 E280A ε4 carriers showed amyloid-PET-positivity ~3 years earlier than non-carriers); *DAOA* rs2391191 (A/A genotype associated with later onset in PSEN1 A431E carriers, PMC12387094); specific γ-secretase "Aβ profile" generated by a given *PSEN1*/*PSEN2*/*APP* variant (ratio and composition of Aβ37/38/40/42/43 species correlates linearly with age at onset across all three genes — PMC12032737, unifying "spectrum of γ-secretase dysfunction" model).
- *Environmental:* Age is the dominant non-genetic modifier of symptom expression (variant-specific mean onset age, but individual variance of years-to-decades exists even within families carrying the identical variant). Educational attainment is protective/moderating for cognitive trajectory independent of neuropathological burden (cognitive reserve effect; Nature Communications, PMC10447560). Head trauma and cardiovascular risk factors are implicated as accelerants in sporadic AD but are less well-characterized as modifiers specifically in ADAD.
- *Reduced penetrance exceptions:* Rare variants such as PSEN1 H163Y show documented reduced penetrance with symptom-free survival into advanced age in some carriers (22-year follow-up study, PMC5944151), indicating unmeasured genetic/epigenetic/environmental modifiers exist even in "fully penetrant" genes.

**Protective factors:** *APOE* ε2 has been associated with delayed cognitive decline/onset in some ADAD cohorts (contrasted with ε4 acceleration). No validated environmental protective factor is specific to ADAD; general cognitive-reserve/educational-attainment effects (moderating clinical expression of a fixed pathological burden) are the best-supported protective modifiers.

**Gene-environment interactions:** Formal GxE studies in ADAD are sparse given the small, geographically dispersed kindred sizes; the strongest documented interaction is the education × APOE interaction on cognitive trajectory (education moderates but does not eliminate the negative effect of APOE ε4 on cognition in mutation carriers).

---

## 3. Phenotypes

ADAD presents the core sporadic-AD phenotype (progressive episodic memory impairment leading to global dementia) plus a materially higher rate of "atypical"/non-amnestic and neurological accompaniments than late-onset sporadic AD, particularly with *PSEN1* variants.

**Core cognitive/behavioral phenotype:**
- **Episodic memory impairment** (initial and near-universal presenting symptom) — HP:0002354 (Memory impairment) / HP:0031830 (?) — best mapped to HP:0002354.
- **Progressive dementia** — HP:0000726 (Dementia)
- **Behavioral/personality change** (frequently an early presenting feature alongside or preceding memory loss) — HP:0000708 (Behavioral abnormality) / HP:0000722 (Irritability) / HP:0100716 (Self-injurious behavior, situational)
- **Language impairment / aphasia** — HP:0002381 (Aphasia)
- **Executive dysfunction** — HP:0002357 (?), best represented as HP:0002344 (Attention deficit) or a general HP:0031466 executive-function term depending on HPO build.

**Neurological accompaniments enriched in ADAD (especially *PSEN1*):**
- **Myoclonus** — HP:0001336 — onset relatively early in disease course in ~70% of those affected; strong predictor of subsequent seizures.
- **Seizures** — HP:0001250 — early-onset seizures in ~30% of affected individuals with myoclonus, late-onset in ~50%; individuals with myoclonus are 40% (PSEN1) to 50% (APP) more likely to develop seizures than those without (Lancet Neurology case series; ScienceDirect DIAN-OBS comparison, S1474442216302290).
- **Spastic paraparesis** — HP:0007256 (Progressive spastic paraparesis) — variably associated with specific *PSEN1* variants (e.g., the "spastic paraparesis variant" phenotype); pyramidal signs seen in ~25% of PSEN1 carriers in some series, restricted to PSEN1 (not seen with APP/PSEN2) — a genotype-phenotype correlation.
- **Extrapyramidal signs** (parkinsonism) — HP:0002548 (Extrapyramidal sign)
- **Cerebellar ataxia** — HP:0001251 — rare/exceptional.
- **Intracerebral hemorrhage** — HP:0001342 — associated particularly with certain *APP* variants causing cerebral amyloid angiopathy (CAA), e.g., Dutch/Iowa-type variants.
- **Visual disturbance / posterior cortical features** — HP:0000505 (Visual impairment)

**Phenotype characteristics:**
- *Age of onset:* Highly variant-specific. *PSEN1* mutations cause the earliest onset overall (mean often 30s–50s; documented range from as young as ~24 years to the 60s). *PSEN2* and *APP* variants show delayed onset relative to *PSEN1* — recent quantitative work estimates mean delays of ~27 years for *PSEN2* and ~8 years for *APP* relative to *PSEN1* (2025 study cited above).
- *Severity/progression:* Uniformly progressive; disease course pattern is relentlessly progressive (not relapsing-remitting), typically over 8–10 years from symptom onset to death, though this varies by variant.
- *Frequency of specific neurological signs:* Varies substantially by variant and gene (see above percentages); a UK case series and DIAN-OBS comparison found systematic differences between published literature phenotype summaries and directly-observed DIAN-OBS cohort data, cautioning against over-generalizing single-kindred phenotype reports (PMC12738114).

**Quality of life impact:** Progressive loss of independent function (activities of daily living), caregiver burden, and — because of early working-age onset — substantial socioeconomic and family-planning impact distinct from late-onset AD (loss of employment/income during peak career/parenting years; documented psychological burden and elevated suicidal ideation risk in at-risk relatives undergoing predictive testing, PMC10046467).

---

## 4. Genetic/Molecular Information

**Causal genes:**
| Gene | HGNC | OMIM (gene) | Locus | Approx. % of solved ADAD |
|---|---|---|---|---|
| *PSEN1* | HGNC:9508 | 104311 | 14q24.2 | ~69% |
| *APP* | HGNC:620 | 104760 | 21q21.3 | ~13% (point variants) + ~7.5% (duplication) |
| *PSEN2* | HGNC:9509 | 600759 | 1q42.13 | ~2% |

**Pathogenic variants:**
- *PSEN1* — >300 reported pathogenic missense variants distributed across all 9 transmembrane domains; classified pathogenic/likely pathogenic per ACMG/AMP in ClinVar. Loss of normal γ-secretase substrate-processivity (rather than simple gain- or loss-of-function) is now understood as the shared mechanism: variants shift the ratio of Aβ species toward longer, more amyloidogenic forms (Aβ42, Aβ43) relative to Aβ40. Example founder variants: E280A (Colombian "Paisa" kindred, the largest single-family ADAD cohort in the world), A431E (Jalisco, Mexico, founder variant).
- *APP* — Variants cluster near the β-secretase (Swedish, KM670/671NL), α-secretase (e.g., London V717I), and γ-secretase cleavage sites, shifting APP processing toward increased total Aβ production or toward the more aggregation-prone Aβ42 species; the *APP* locus duplication (as in trisomy 21 / Down syndrome) causes ADAD-like early-onset AD purely through increased gene dosage/protein level, without any coding variant — direct evidence that increased Aβ production alone is sufficient to cause the disease.
- *PSEN2* — Fewer variants known; N141I is the classic Volga German founder variant; generally later, more variable onset and comparatively reduced penetrance versus *PSEN1*.
- **Variant type spectrum:** Predominantly missense for *PSEN1*/*PSEN2*; missense and structural (duplication) for *APP*. Frameshift/nonsense variants are rare/atypical since loss-of-function null alleles of *PSEN1* generally do not cause the classical ADAD phenotype (informing a "partial loss of normal function / gain of abnormal function" model for missense variants rather than simple haploinsufficiency).
- **Allele frequency:** Pathogenic ADAD-causing variants are essentially absent or present at extremely low frequency (rarely >1 allele) in population reference databases (gnomAD), consistent with strong negative selection against a childhood/reproductive-age-compatible but ultimately lethal, fully penetrant dominant disease.
- **Somatic vs. germline:** Germline in essentially all classical ADAD kindreds; no established somatic-mosaicism mechanism is a primary ADAD cause (contrast with some other neurogenetic disorders), though germline mosaicism has been raised as a genetic-counseling consideration for apparent de novo cases.
- **Functional consequence:** The unifying functional theme (PMC12032737, "spectrum of γ-secretase dysfunction") is altered γ-secretase processivity of APP substrate, producing a quantitatively predictable shift in the Aβ42(43)/Aβ40 ratio that correlates linearly with age at onset across *PSEN1*, *PSEN2*, and *APP* variants — a genotype→biochemistry→age-of-onset relationship that is one of the most quantitatively robust genotype-phenotype correlations in neurodegenerative disease.

**Modifier genes:** *APOE* (ε2/ε3/ε4), *DAOA* (rs2391191), with ongoing multiomic work (PMC11699654) identifying "common endotypes" across PSEN1/PSEN2/APP mutation carriers suggesting shared downstream modifier pathways (inflammatory/astrocytic) independent of the specific causal gene.

**Epigenetic information:** No established disease-defining epigenetic lesion in ADAD itself (unlike, e.g., imprinting disorders); epigenetic dysregulation (DNA methylation changes at AD-associated loci, histone modification changes) is an active downstream/consequence research area in both sporadic and familial AD but is not established as causal.

**Chromosomal abnormalities:** The *APP* locus duplication (21q21.3) is the clearest chromosomal/structural mechanism; complete trisomy 21 (Down syndrome) produces an obligate ADAD-like phenotype via 3-copy *APP* dosage, with virtually universal AD neuropathology by the 40s and clinical dementia in a majority of individuals with Down syndrome by their 50s–60s — this is a widely used "genetically determined AD" comparator model in the field.

---

## 5. Environmental Information

ADAD is, by definition, monogenically determined with near-complete penetrance, so environmental/lifestyle factors are best understood as modifiers of the *timing and expression* of an essentially inevitable disease rather than determinants of whether disease occurs.
- **Environmental toxin/occupational factors:** No ADAD-specific toxin exposure has been established as a modifier; general AD-epidemiology environmental factors (air pollution, pesticide exposure) are studied in sporadic AD but not specifically validated in ADAD cohorts.
- **Lifestyle factors:** Educational attainment/cognitive reserve is the best-evidenced modifier of clinical (not necessarily pathological) trajectory in ADAD mutation carriers (Nature Communications, PMC10447560). Cardiovascular risk-factor management (as in sporadic AD) is plausibly beneficial but not specifically validated as modifying ADAD's core amyloid-driven course.
- **Infectious agents:** Not implicated as a cause of ADAD. (The broader "infectious hypothesis" of sporadic AD, e.g., HSV-1, periodontal pathogens, remains investigational and is not part of the ADAD causal model, which is fully explained by the monogenic amyloidogenic mechanism.)

---

## 6. Mechanism / Pathophysiology

**Overview causal chain (the amyloid cascade hypothesis, as directly demonstrated by ADAD genetics):**

1. **Trigger (molecular scale):** Pathogenic *PSEN1*/*PSEN2* variant alters γ-secretase complex processivity, OR pathogenic *APP* variant/duplication alters substrate availability or cleavage-site accessibility → shift in the ratio and length distribution of Aβ peptides generated from sequential β- and γ-secretase cleavage of APP, favoring longer, more aggregation-prone species (Aβ42, Aβ43) over Aβ40.
2. **Aβ aggregation and amyloidosis (molecular→cellular):** Increased relative Aβ42/43 production → oligomerization → fibrillization → extracellular amyloid plaque deposition (diffuse and neuritic plaques) and, for certain *APP* variants, cerebral amyloid angiopathy (vascular Aβ deposition). This is the earliest detectable biomarker change, beginning ~20–25 years before expected symptom onset in DIAN cohort data (Bateman et al., NEJM 2012 — landmark longitudinal biomarker cascade paper; [NEJM full text](https://www.nejm.org/doi/full/10.1056/NEJMoa1202753)).
3. **Downstream tauopathy:** Amyloid pathology precipitates (via still partially defined mechanisms involving synaptic dysfunction, oxidative stress, and kinase dysregulation) hyperphosphorylation of microtubule-associated protein tau by kinases including GSK-3β; presenilins themselves (via γ-secretase-dependent and -independent roles) normally help regulate GSK-3β subcellular localization and restrain tau hyperphosphorylation, so presenilin dysfunction can directly promote tauopathy in addition to its Aβ-generating effect. Hyperphosphorylated tau detaches from microtubules, impairing axonal transport, and self-aggregates into paired helical filaments forming intraneuronal neurofibrillary tangles — occurring downstream of and temporally after amyloid changes in the DIAN cascade (tau PET/CSF changes emerge and progress after amyloid positivity).
4. **Neuroinflammation / microglial dysfunction (cellular):** Aβ plaques and early oligomers activate microglia; TREM2 (via DAP12-SYK signaling) mediates microglial phagocytic clearance of Aβ and, together with complement (C1q) and APOE, mediates aberrant microglial synaptic pruning/engulfment. Chronic activation produces a maladaptive, disease-associated microglial (DAM) state contributing to a self-perpetuating neuroinflammatory milieu rather than effective clearance.
5. **Synaptic and neuronal injury (cellular→tissue):** Soluble Aβ oligomers directly impair synaptic function and induce neuronal hyperactivity; combined amyloid/tau/neuroinflammatory burden drives synaptic loss (the pathological correlate best correlated with cognitive impairment), followed by neuronal loss.
6. **Neurodegeneration and atrophy (tissue→organism):** Progressive regional brain atrophy (starting in medial temporal lobe/hippocampus, later diffuse), declining cerebral glucose metabolism (FDG-PET hypometabolism), and clinical cognitive decline — occurring last in the DIAN cascade, ~10–20 years after the earliest amyloid biomarker changes.

**Suggested GO terms (biological processes):**
- GO:0034205 amyloid-beta formation
- GO:1902430 negative regulation of amyloid-beta formation (relevant to pathway perturbation)
- GO:0007172 signal complex assembly (γ-secretase complex context) / GO:0070765 gamma-secretase complex
- GO:0006338 chromatin remodeling (epigenetic downstream, if modeled)
- GO:0050890 cognition (phenotypic endpoint)
- GO:0001764 neuron migration / GO:0007399 nervous system development (not primary)
- GO:0043523 regulation of neuron apoptotic process
- GO:0045087 innate immune response (microglial activation)
- GO:0006979 response to oxidative stress

**Suggested CL terms (cell types):**
- CL:0000540 neuron (generic); CL:0000031 (neuroblast, not relevant)
- CL:0000679 glutamatergic neuron (pyramidal/cortical neurons preferentially affected)
- CL:0000129 microglial cell
- CL:0000127 astrocyte (reactive astrogliosis)
- CL:0002453 oligodendrocyte precursor cell (secondary white-matter involvement, less central)

**Molecular functions/UniProt/PDB:** APP (UniProt P05067); PSEN1 (UniProt P49768); PSEN2 (UniProt P49810); γ-secretase complex structures resolved by cryo-EM (PDB entries exist for human γ-secretase, e.g., 5A63, 5FN2).

**Metabolic/biochemical:** Downstream mitochondrial dysfunction and impaired glucose metabolism (FDG-PET hypometabolism is a core biomarker); altered lipid metabolism (cholesterol trafficking) links to *APOE* modifier effects.

**Molecular profiling / advanced technologies:** Multi-omic integration work across PSEN1/PSEN2/APP carriers has identified convergent ("common endotype") transcriptomic/proteomic signatures independent of the specific causal gene (PMC11699654), and iPSC-derived astrocyte models of *PSEN1* variants show disrupted regulated intramembrane proteolysis predisposing to inflammatory phenotypes (PMC12181884) — evidence that presenilin dysfunction has γ-secretase-independent, immune-relevant cellular consequences beyond simple amyloidogenesis.

---

## 7. Anatomical Structures Affected

**Organ level:** Primary organ — brain (UBERON:0000955). Body system — nervous system (UBERON:0001016). Secondary/complication involvement: cerebral vasculature (in *APP*-variant-associated cerebral amyloid angiopathy, risk of intracerebral hemorrhage); spinal cord/corticospinal tract involvement clinically manifesting as spastic paraparesis in specific *PSEN1* variants.

**Tissue/cell level:**
- Cerebral cortex (UBERON:0000956), especially medial temporal lobe / hippocampus (UBERON:0002421) — earliest and most severe atrophy.
- Entorhinal cortex (UBERON:0002728) — early tau pathology site (Braak staging origin).
- Precuneus/posterior cingulate — early amyloid-PET/FDG-PET signal.
- Cell populations: large glutamatergic pyramidal neurons (CL:0000679) selectively vulnerable; microglia (CL:0000129) and astrocytes (CL:0000127) reactively involved; cerebrovascular smooth muscle/endothelium involved in CAA.

**Subcellular level:** Extracellular amyloid plaques (GO:0097418 neurofibrillary tangle for the intracellular counterpart); GO:0005789 endoplasmic reticulum membrane and GO:0031090 organelle membrane (site of γ-secretase activity — PSEN1/2 are ER/Golgi/plasma-membrane transmembrane proteins); GO:0005739 mitochondrion (downstream dysfunction); GO:0045202 synapse (site of Aβ oligomer toxicity and microglial synaptic pruning).

**Localization:** Bilateral, generally symmetric involvement (contrast with focal neurodegenerative syndromes); progresses from medial temporal to diffuse neocortical involvement per Braak/Thal staging schemes, mirrored in amyloid-PET (Thal phases) and tau-PET (Braak-like patterns) in DIAN cohort imaging.

---

## 8. Temporal Development

**Onset:** Adult onset, defined as pre-senile (<65 years) and typically much earlier — commonly 30s–50s, occasionally younger depending on variant (as young as mid-20s reported for some aggressive *PSEN1* variants). Onset pattern is insidious, not acute — a subtle prodromal decline over months to a few years before diagnosis.

**Progression (the DIAN biomarker cascade — a hallmark, extensively validated natural-history finding):**
1. Aβ42 CSF changes and amyloid-PET positivity — begin ~20–25 years before expected symptom onset (estimated from parental age at onset within a kindred).
2. Cerebral glucose hypometabolism (FDG-PET) — begins ~10–15 years before onset (~7–10 years after earliest amyloid change).
3. Hippocampal/structural atrophy and initial subtle cognitive decline — begin roughly 10–15 years, becoming clearly measurable ~5 years before clinical onset.
4. Clinical Dementia Rating (CDR) transition to symptomatic/impaired — the defined "onset."
5. Progressive dementia over subsequent years to death (variable, commonly 8–10 years post-diagnosis, similar to sporadic AD trajectory once symptomatic).

(Bateman et al. 2012 NEJM, "Clinical and Biomarker Changes in Dominantly Inherited Alzheimer's Disease"; subsequent DIAN longitudinal work confirming and refining timing, e.g., Neurology 2018 "Longitudinal cognitive and biomarker changes in dominantly inherited Alzheimer disease," and the 2025 "15 years of longitudinal…measures in DIAN" (npj Dementia) update.)

**Disease stages:** Preclinical (biomarker-positive, cognitively normal) → prodromal/MCI (mild cognitive impairment due to AD) → mild dementia → moderate dementia → severe/end-stage dementia — the CDR and DIAN "Estimated Years to Symptom Onset" (EYO) framework are the field-standard staging tools, distinct from generic AJCC-style staging (not applicable to a non-oncologic disease).

**Progression rate/course:** Once symptomatic, relentlessly progressive, non-remitting; among the more rapid dementia trajectories compared with typical sporadic late-onset AD, partly reflecting younger baseline health and higher pathological burden at a given clinical stage in some series, though this is debated.

**Patterns:** No spontaneous or treatment-induced remission is described; anti-amyloid immunotherapy trials (below) aim to slow but not yet reverse progression. The presymptomatic ~20-year biomarker-positive window is the field's key "critical period" for intervention — the rationale for the DIAN-TU prevention trials targeting mutation carriers before symptom onset.

---

## 9. Inheritance and Population

**Epidemiology:**
- EOAD overall (<65y onset, all causes) prevalence ≈ 41.2 per 100,000 persons at risk in population-based estimates; incidence in the 45–64 age band ≈ 6.3/100,000/year, prevalence ≈ 24.2/100,000, rising steeply approaching age 65.
- ADAD specifically (autosomal-dominant EOAD, ADEOAD): population prevalence ≈ 5.3 per 100,000 persons at risk (same population-based study cited above).
- ADAD is estimated to account for **~1% of all AD cases** overall, and **~5–10% of early-onset AD cases** are attributable to dominantly inherited mutations, with the remainder of EOAD considered sporadic/complex/oligogenic.
- Among familial EOAD (patients with ≥1 affected first-degree relative, 35–60% of EOAD), only 10–15% show a clear autosomal-dominant transmission pattern solvable by *APP*/*PSEN1*/*PSEN2* testing.

**Inheritance pattern:** Autosomal dominant (HP:0000006). Penetrance is near-complete/"fully penetrant" for the great majority of *PSEN1* variants and the *APP* variants/duplication; documented exceptions with reduced/age-dependent penetrance exist (e.g., PSEN1 H163Y). *PSEN2* variants (e.g., N141I) show somewhat more variable, occasionally incomplete penetrance and later/more variable onset than *PSEN1*.

**Expressivity:** Variable — age of onset varies not only between genes and between different variants within a gene, but also between individuals carrying the *identical* variant within the same family, implicating modifier genes (APOE, DAOA) and other unmeasured factors.

**Genetic anticipation:** Not a defined feature of ADAD (unlike repeat-expansion disorders); no systematic earlier-onset-in-successive-generations pattern is established.

**Germline mosaicism:** A recognized genetic-counseling consideration for apparent de novo *PSEN1*/*APP* cases (parental germline mosaicism can produce unaffected parents with an affected child and residual recurrence risk for future pregnancies), though formally documented cases specific to ADAD genes are limited in the literature relative to other dominant disorders.

**Founder effects:** Well documented — *PSEN1* E280A in the Colombian "Paisa" kindred (~6,000-member, ~1,200 carrier-lineage pedigree, the world's largest single ADAD kindred, central to the Colombia-API prevention trial); *PSEN1* A431E in the Jalisco, Mexico population; *PSEN2* N141I in Volga German-descended families in the United States.

**Consanguinity:** Not a relevant risk factor for this autosomal *dominant* disorder (in contrast to recessive conditions) — a single inherited or de novo copy is sufficient.

**Carrier frequency:** Population carrier frequency of any single pathogenic ADAD variant is extremely low (rare/private variants, or locally elevated only within founder-effect populations/kindreds); no meaningful general-population carrier screening frequency exists comparable to recessive-disease carrier screening.

**Population demographics:** No strong evidence for differential susceptibility by ethnicity beyond the founder-population enrichments noted above (Colombian, Mexican, Volga German lineages) — these reflect genealogical founder effects, not differential biological susceptibility. Sex ratio: approximately equal (autosomal, not sex-linked), consistent with Mendelian expectation, though *APOE*-related modifier effects (and sporadic-AD female-predominance patterns) may subtly influence age-of-onset/progression statistics by sex in some analyses. Age distribution of affected individuals is, by definition, the defining "early-onset" feature (predominantly 30s–50s at symptom onset, contrasted with the ≥65y peak of sporadic AD).

---

## 10. Diagnostics

**Clinical tests:**
- **Biomarkers (CSF):** CSF Aβ42/Aβ40 ratio (decreased) and phosphorylated tau (p-tau181, increasingly p-tau217, p-tau231) are core, guideline-incorporated AD biomarkers; CSF p-tau217/Aβ42 ratio and p-tau217 phosphorylation occupancy show improved performance over p-tau181 for detecting amyloid and tau pathology (Nature Aging, PMC study cited above).
- **Blood-based biomarkers:** Plasma p-tau217 and the p-tau217/Aβ1-42 ratio now show AUC 0.94–0.97 for detecting amyloid pathology against CSF/PET reference standards, a major recent (2024–2025) advance enabling non-invasive, scalable case detection and monitoring — highly relevant for at-risk ADAD family members considering testing and for trial screening/enrollment.
- **Imaging:** Amyloid-PET (e.g., florbetapir, Pittsburgh compound B) — earliest positive biomarker in the DIAN cascade; tau-PET (flortaucipir) — shows variant-specific signatures, e.g., a characterized flortaucipir signature specific to PSEN1 A431E carriers (PMC12740027); structural MRI for hippocampal/cortical atrophy; FDG-PET for regional hypometabolism.
- **Neurophysiology:** EEG may show abnormalities correlating with myoclonus/seizure activity, which are enriched in ADAD relative to sporadic AD.
- **Neuropathology (postmortem/rare biopsy):** Amyloid plaques (neuritic and diffuse), neurofibrillary tangles (Braak staging), cerebral amyloid angiopathy (especially with certain *APP* variants); the OMIM:605055 entry specifically flags documented coexisting amyloid and prion pathology in some familial early-onset AD cases, an important differential/comorbidity note.

**Genetic testing:**
- Recommended approach: targeted sequencing (single-gene or small panel) of *APP*, *PSEN1*, *PSEN2* in individuals with early-onset dementia (<65y) and/or a family history consistent with autosomal dominant inheritance; panel/gene-panel testing is standard of care (per GeneReviews/ClinGen-informed protocols) rather than routine WGS/WES as first-line, though WES/WGS is used when panel testing is uninformative or the phenotype is atypical.
- Predictive (presymptomatic) testing in at-risk, asymptomatic relatives follows Huntington-disease-style genetic counseling protocols (given the comparably severe, currently incurable, fully penetrant nature of the result) — pre- and post-test counseling, psychological support, and consideration of implications for insurance/employment/family planning are essential; documented elevated suicidal-ideation risk in this population underscores the need for structured counseling (PMC10046467).
- Chromosomal microarray/karyotyping is relevant specifically to detect *APP* locus duplication or trisomy 21 as a cause.
- Not relevant: mitochondrial DNA testing, repeat-expansion testing (ADAD is not a repeat-expansion disorder).

**Omics-based diagnostics:** Not yet standard clinical practice for ADAD; used in research contexts (multi-omic endotyping, PMC11699654) but blood p-tau217 is the closest omics-adjacent tool nearing clinical/trial-screening utility.

**Clinical criteria:** Standard AD clinical diagnostic frameworks (NIA-AA criteria, now biomarker-integrated) apply; DSM-5 criteria for Major/Mild Neurocognitive Disorder due to Alzheimer's Disease apply clinically. Differential diagnosis must consider: frontotemporal dementia (especially when behavioral/language-predominant presentation), other early-onset dementia genes (e.g., *MAPT*, *GRN*, *C9orf72* for FTD spectrum; prion disease given the amyloid/prion overlap noted in OMIM:605055), and reversible causes of cognitive decline in a young patient (metabolic, autoimmune, structural).

**Screening:** Cascade genetic testing in at-risk relatives once a family proband variant is identified is the standard screening approach (not population newborn screening, given adult onset). Preimplantation genetic diagnosis (PGD/PGT-M) has been successfully used to select unaffected embryos for at-risk couples (documented case for an *APP* V717L family resulting in birth of an unaffected child, PMID:11866650).

---

## 11. Outcome/Prognosis

**Survival/mortality:** ADAD is ultimately fatal; life expectancy after symptom onset is broadly comparable to or somewhat shorter than sporadic AD, commonly on the order of 8–10 years from diagnosis to death, though this varies by causal variant and access to supportive care. No disease-modifying therapy has yet been shown to alter mortality.

**Morbidity/function:** Progressive functional decline through the classic AD trajectory — loss of instrumental then basic activities of daily living, eventual total care dependency. Given the working-age onset, morbidity burden (loss of employment, caregiving strain on a typically younger family unit with dependent children) is proportionally more disruptive than in late-onset sporadic AD.

**Quality of life:** Progressive decline across cognitive, functional, and psychological domains for both patients and caregivers; documented elevated psychological distress (including suicidal ideation) in unaffected at-risk relatives navigating predictive testing decisions is itself a distinct QoL/mental-health outcome domain specific to this genetically-predictable disease.

**Complications:** Seizures and myoclonus (notably more frequent than sporadic AD, particularly with *PSEN1*); intracerebral hemorrhage in CAA-associated *APP* variants; aspiration pneumonia and other end-stage-dementia complications as the ultimate proximate causes of death, as in sporadic AD.

**Prognostic factors:** Causal gene and specific variant (via its Aβ-species "biochemical signature") is the single strongest predictor of age at onset and, to a lesser extent, of rate of progression and accompanying neurological features (myoclonus/seizures/spasticity cluster with *PSEN1*). *APOE* genotype and, more speculatively, *DAOA* genotype and educational attainment act as secondary modifiers of onset timing and/or cognitive trajectory. Biomarker trajectory (rate of amyloid accumulation, tau-PET spread) is an active area of prognostic-biomarker research within DIAN and the newer anti-tau trials (e.g., etalanetug/E2814 targeting tau spread).

---

## 12. Treatment

**Pharmacotherapy (symptomatic, shared with sporadic AD):**
- Cholinesterase inhibitors (donepezil, rivastigmine, galantamine) — MAXO term: pharmacotherapy generically (NCIT:C15986); symptomatic cognitive treatment, not disease-modifying.
- NMDA receptor antagonist (memantine) — symptomatic, moderate-to-severe stages.
- Symptomatic management of myoclonus/seizures (anti-seizure medications, e.g., levetiracetam) given their elevated frequency in ADAD.

**Advanced/disease-modifying therapeutics (the major current research/clinical frontier, largely trialed specifically in ADAD via DIAN-TU because of presymptomatic identifiability):**
- **Anti-amyloid monoclonal antibodies:**
  - *Gantenerumab* and *solanezumab* — tested in the DIAN-TU-001 platform trial (2012–2019 double-blind phase): did **not** meet the primary endpoint of slowing cognitive decline across combined symptomatic/asymptomatic cohorts, but gantenerumab produced significant, dose-dependent amyloid plaque reduction and reduced CSF tau/synaptic-degeneration/neuroinflammation markers, especially in asymptomatic carriers (Nature Medicine 2021, JAMA Neurology downstream-biomarker analysis). A subsequent open-label extension (2020–2023, up to 10 years cumulative treatment in some asymptomatic carriers) examined whether sustained, high-dose treatment yields clinical benefit (Lancet Neurology 2025); amyloid-related imaging abnormalities-edema (ARIA-E) occurred in 19.2% of gantenerumab-treated participants vs. 2.5% placebo, an important safety signal shared across the anti-amyloid antibody class.
  - *Lecanemab* — now the backbone anti-amyloid therapy in the ongoing **DIAN-TU Tau NexGen** study (initiated January 2022), combined with the investigational anti-tau antibody *etalanetug (E2814)* to test whether reducing pathological tau spread adds benefit atop amyloid removal — trial evaluates outcomes over 208 weeks; interim baseline-characteristics/6-month safety data were presented in 2025.
  - *Donanemab* — approved and studied extensively in sporadic AD (TRAILBLAZER-ALZ program) but not yet reported with ADAD-specific dominantly-inherited-cohort trial data in the current literature search.
- **Anti-tau therapy:** *Etalanetug (E2814)*, an anti-tau monoclonal antibody targeting extracellular tau spread, is being trialed specifically in DIAD mutation carriers as an adjunct to lecanemab (DIAN-TU NexGen) — this represents the field's leading edge in testing combination amyloid+tau disease-modification in a genetically-defined, presymptomatic population.
- **Gene-directed/other advanced modalities:** No approved gene therapy, RNA-based therapy (ASO/siRNA), or cell therapy for ADAD specifically exists as of this report; given the well-defined single-gene cause, ADAD is a plausible future candidate for allele-specific ASO knockdown approaches (as pursued in other dominant neurodegenerative diseases), but no ADAD-specific program has reached the clinical literature reviewed here.

**Surgical/interventional:** Not applicable as a primary treatment modality for ADAD itself.

**Supportive/rehabilitative:** Multidisciplinary dementia supportive care (physical/occupational/speech therapy as needed for functional decline), caregiver support programs, and psychiatric/behavioral symptom management (MAXO:0000950 supportive care; MAXO:0000011 physical therapy where applicable).

**Experimental/clinical trials (selected, with identifiers where available):**
- DIAN-TU Platform Trial extensions — NCT06424236 ("Dominantly Inherited Alzheimer Network Trial: An Opportunity to Prevent Dementia")
- DIAN Observational Study — NCT00869817
- Colombia-API (Alzheimer's Prevention Initiative) autosomal-dominant AD trial in the PSEN1 E280A kindred (crenezumab, subsequently discontinued as primary endpoint not met, though biomarker signals were reported)

**Treatment outcomes/adverse events:** ARIA-E/ARIA-H (amyloid-related imaging abnormalities — edema/hemorrhage) is the dominant class-wide safety concern for anti-amyloid antibodies, with meaningfully elevated incidence versus placebo across trials; monitoring via serial MRI is now standard trial (and increasingly clinical) protocol. To date, no anti-amyloid or anti-tau agent has demonstrated a clearly established clinical cognitive benefit specific to the ADAD/DIAD population, despite robust biomarker (amyloid/tau/neurodegeneration marker) modification — a key ongoing translational gap actively being addressed by the tau-directed combination trials.

**Treatment strategy/personalized medicine:** Presymptomatic/prevention-oriented dosing strategy (treating carriers years before expected onset, leveraging the known ~20-year presymptomatic biomarker window) is the field's central strategic hypothesis, distinguishing ADAD trial design fundamentally from sporadic late-onset AD trials, which necessarily enroll after some degree of established pathology/symptoms.

---

## 13. Prevention

**Primary prevention:** Not currently achievable pharmacologically (no proven method to prevent disease onset in a confirmed mutation carrier), but is the explicit long-term goal of the presymptomatic DIAN-TU/NexGen and historical API trials — administering anti-amyloid (and now anti-tau) therapy during the decades-long presymptomatic biomarker-positive window in the hope of preventing or substantially delaying clinical onset.

**Secondary prevention:** Early biomarker detection (CSF/plasma p-tau217, amyloid-PET) in known mutation carriers enables early trial enrollment and monitoring, functioning as the operational "secondary prevention" framework in this genetically-predictable disease, though it does not yet translate into a proven clinical intervention.

**Reproductive/genetic prevention:**
- Preimplantation genetic diagnosis (PGD/PGT-M) — successfully used for ADAD-causing *APP* variants to select unaffected embryos, resulting in births of unaffected children (PMID:11866650).
- Prenatal testing is possible for known-carrier pregnancies (analogous framework to other dominant, adult-onset, fully penetrant disorders such as Huntington disease), though ethically and psychologically complex given adult onset.
- Cascade/predictive genetic testing in at-risk relatives, paired with formal genetic counseling, is the standard risk-stratification and family-planning-guidance approach (NSGC/ACMG-informed protocols, modeled closely on Huntington disease predictive-testing guidelines given comparable ethical weight).

**Behavioral/lifestyle interventions:** General brain-health/cardiovascular-risk-reduction measures (as recommended for sporadic AD risk reduction) are reasonable adjuncts but are not established to meaningfully alter the essentially deterministic course in confirmed mutation carriers.

**Public health/environmental interventions:** Not a primary prevention lever for this monogenic disorder; population-level public-health prevention strategies relevant to sporadic AD (cardiovascular risk factor control, education, physical activity) do not have established ADAD-specific efficacy data.

**Prophylaxis:** The presymptomatic anti-amyloid/anti-tau trial paradigm described above is, in effect, the field's prophylaxis research program, though no agent is yet validated/approved for this indication.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring, spontaneous orthologous disease with an equivalent *PSEN1*/*PSEN2*/*APP*-driven fully penetrant dominant Alzheimer-like dementia has been well documented in non-human species under natural conditions. Aged dogs (*Canis lupus familiaris*, NCBITaxon:9615) and aged non-human primates can develop age-related, sporadic-AD-like cognitive dysfunction syndrome with some amyloid pathology, but this is an aging-associated phenomenon, not a monogenic dominant disease analogous to human ADAD.

**Orthologous genes:** *App*, *Psen1*, *Psen2* are conserved across mammals (mouse orthologs: *App* MGI:88059, *Psen1* MGI:104779, *Psen2* MGI:108086); rodents do not naturally develop human-like amyloid pathology even when carrying these orthologs unmodified, which is precisely why transgenic/knock-in humanized models were developed (see Section 15).

**Veterinary relevance:** Canine cognitive dysfunction syndrome (CCDS) is studied as a naturally occurring, sporadic aging model with some amyloid deposition, of comparative interest but not a direct ADAD model (OMIA does not list a canonical monogenic canine ADAD ortholog disease).

**Comparative biology:** The core γ-secretase/APP processing pathway is deeply evolutionarily conserved, which is precisely why humanized knock-in and transgenic rodent models (below) can be constructed to express human pathogenic variants and partially recapitulate amyloid pathology, despite the absence of natural disease in these species.

**Zoonotic potential:** Not applicable — ADAD is a purely genetic, non-transmissible disease.

---

## 15. Model Organisms

**Rodent transgenic overexpression models:** Classic APP/PS1 double-transgenic mice (overexpressing mutant human APP and PSEN1 from non-physiological promoters) robustly and reproducibly develop amyloid plaque pathology and are the most widely used preclinical AD model, but suffer from significant limitations: APP overexpression from an early age (unlike the gradual human increase), non-physiological accumulation of APP fragments (CTFs, AICD) not seen in human AD brain that may independently cause artifactual endosomal/transcriptional abnormalities, and — most importantly for translational validity — frequent failure to fully recapitulate human-comparable tau pathology, neurodegeneration, and behavioral/cognitive decline patterns at physiologically relevant timescales.

**Knock-in models (designed to address overexpression artifacts):** *App^NL-G-F^* and related humanized *App* knock-in lines (Saito/Saido-style knock-ins) express mutant human Aβ sequence at physiological levels under the endogenous promoter, better modeling the gradual human amyloid accumulation trajectory and revealing profound microglial metabolic dysregulation (Molecular Neurodegeneration, PMC9188195); however, recent work (bioRxiv 2024) reports that App-KI mice **do not display the hallmark age-dependent cognitive decline** seen in overexpression models or in human disease, and PSEN1 knock-in alone (without an accompanying APP mutation) is generally **insufficient to induce Aβ pathology at all**, indicating that a combined, humanized APP+PSEN1(or PSEN2) knock-in approach is needed to approach physiological relevance, and even then, cognitive-behavioral phenotype fidelity to human ADAD remains incompletely validated (an appropriate candidate for a `HUMAN_MODEL_MISMATCH` framing in mechanistic curation, per this project's conventions).

**Immunodeficient humanized models:** Combined APP/PSEN1 knock-in immunodeficient mice have been reported to exhibit intraneuronal Aβ pathology, microgliosis, and extensive neuronal loss (PMC11975631) — an attempt to better model the human innate-immune/microglial contribution by permitting engraftment of human microglia or other human cellular elements.

**Other model systems:**
- *Drosophila melanogaster* presenilin models (used to dissect γ-secretase-independent presenilin toxicity mechanisms, e.g., ALZFORUM-reported "protease or not" eye-phenotype screens).
- Human iPSC-derived neuronal and astrocyte models carrying patient-specific *PSEN1*/*PSEN2*/*APP* variants — increasingly central for mechanistic study (e.g., iPSC-astrocyte models showing PSEN1-variant-driven inflammatory predisposition via disrupted regulated intramembrane proteolysis, PMC12181884) and for modeling human-specific cellular contexts not well captured by rodents.
- Organoid models — cerebral/brain organoids from ADAD patient iPSCs are an emerging platform for studying 3D tissue-context amyloid/tau pathology, though standardization and long-term maturation remain limitations.

**Applications:** Mouse and iPSC models are used to dissect the amyloid-generation mechanism, test candidate anti-amyloid/anti-tau therapeutics preclinically (informing the DIAN-TU trial pipeline), and study microglial/neuroinflammatory contributions; they are less reliable for modeling the full human cognitive-behavioral phenotype or the neurological accompaniments (myoclonus, seizures, spastic paraparesis) seen in human *PSEN1* carriers.

**Model limitations (summary):** The recurring, well-documented gap across essentially all current models is a mismatch between robust amyloid (and sometimes neuroinflammatory) pathology on one hand, and inconsistent or absent age-dependent cognitive/behavioral decline and incomplete tau pathology/neurodegeneration on the other — meaning translational claims from rodent efficacy data to expected human clinical benefit should be treated cautiously, consistent with the repeated failure of preclinically-promising anti-amyloid agents to show unambiguous cognitive benefit in DIAN-TU human trials despite clear target engagement.

**Resources:** MGI (Mouse Genome Informatics) for *App*/*Psen1*/*Psen2* alleles; Alzforum "Research Models" database (the field-standard curated registry of AD mouse/model lines, including full genotype/phenotype-recapitulation summaries); JAX (Jackson Laboratory) repository for physical strain distribution.

---

## Summary Table: Key Ontology Term Suggestions

| Category | Term | ID |
|---|---|---|
| Disease | Early-onset autosomal dominant Alzheimer disease | MONDO:0015140 / ORPHA:1020 |
| Gene | PSEN1 | HGNC:9508 |
| Gene | PSEN2 | HGNC:9509 |
| Gene | APP | HGNC:620 |
| Phenotype | Dementia | HP:0000726 |
| Phenotype | Memory impairment | HP:0002354 |
| Phenotype | Myoclonus | HP:0001336 |
| Phenotype | Seizures | HP:0001250 |
| Phenotype | Progressive spastic paraparesis | HP:0007256 |
| Phenotype | Extrapyramidal sign | HP:0002548 |
| Phenotype | Intracerebral hemorrhage | HP:0001342 |
| Inheritance | Autosomal dominant inheritance | HP:0000006 |
| GO (BP) | Amyloid-beta formation | GO:0034205 |
| GO (BP) | Regulation of amyloid-beta formation | GO:1902430 |
| GO (CC) | Gamma-secretase complex | GO:0070765 |
| CL | Glutamatergic neuron | CL:0000679 |
| CL | Microglial cell | CL:0000129 |
| CL | Astrocyte | CL:0000127 |
| UBERON | Hippocampus | UBERON:0002421 |
| UBERON | Cerebral cortex | UBERON:0000956 |
| MAXO | Pharmacotherapy | NCIT:C15986 |
| Drug class | Monoclonal antibody | NCIT:C20401 |

---

## Sources

- [Orphanet: Early onset autosomal dominant Alzheimer disease](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=1020)
- [NIH GARD: Early-onset autosomal dominant Alzheimer disease](https://rarediseases.info.nih.gov/diseases/12798/early-onset-autosomal-dominant-alzheimer-disease)
- [OMIM: ALZHEIMER DISEASE, FAMILIAL EARLY-ONSET, WITH COEXISTING AMYLOID AND PRION PATHOLOGY (605055)](https://omim.org/entry/605055)
- [DAOA and APOEε4 as Modifiers of Age of Onset in ADAD PSEN1 A431E (PMC12387094)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12387094/)
- [Integrative multiomics reveals common endotypes across PSEN1, PSEN2, and APP mutations (PMC11699654)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11699654/)
- [PSEN1 mutations predispose inflammation in astrocyte model (PMC12181884)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12181884/)
- [Reduced penetrance of PSEN1 H163Y — 22-year follow-up (PMC5944151)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5944151/)
- [Aβ profiles generated by PSEN1 variants determine pathogenicity and predict age at onset (Molecular Psychiatry)](https://www.nature.com/articles/s41380-022-01518-6)
- [Spectrum of γ-secretase dysfunction as a unifying predictor of ADAD age at onset (PMC12032737)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12032737/)
- [APP, PSEN1, and PSEN2 mutations in early-onset AD: genetic screening study (PLOS Medicine)](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1002270)
- [Clinical and Biomarker Changes in Dominantly Inherited Alzheimer's Disease (NEJM, Bateman et al. 2012)](https://www.nejm.org/doi/full/10.1056/NEJMoa1202753)
- [15 years of longitudinal genetic, clinical, cognitive, imaging, and biochemical measures in DIAN (npj Dementia)](https://www.nature.com/articles/s44400-025-00047-7)
- [Longitudinal cognitive and biomarker changes in dominantly inherited Alzheimer disease (Neurology)](https://www.neurology.org/doi/10.1212/WNL.0000000000006277)
- [The amyloid cascade hypothesis: are we poised for success or failure? (PubMed 27255958)](https://pubmed.ncbi.nlm.nih.gov/27255958/)
- [The amyloid hypothesis of Alzheimer's disease at 25 years (PMC4888851)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4888851/)
- [Amyloid Cascade Hypothesis for the Treatment of AD: Progress and Challenges (PMC9662281)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9662281/)
- [Clinical phenotype and genetic associations in autosomal dominant familial AD: a case series (Lancet Neurology)](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(16)30193-4/fulltext)
- [Neurological manifestations of autosomal dominant familial AD: literature vs. DIAN-OBS comparison](https://www.sciencedirect.com/science/article/abs/pii/S1474442216302290)
- [Clinical phenotype and neuropathological correlates in ADAD: UK case series (PMC12738114)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12738114/)
- [The Flortaucipir PET signature in ADAD due to A431E PSEN1 mutation (PMC12740027)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12740027/)
- [Safety and efficacy of long-term gantenerumab in DIAD: DIAN-TU open-label extension (Lancet Neurology 2025)](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(25)00024-9/abstract)
- [A trial of gantenerumab or solanezumab in dominantly inherited Alzheimer's disease (Nature Medicine 2021)](https://www.nature.com/articles/s41591-021-01369-8)
- [Downstream Biomarker Effects of Gantenerumab or Solanezumab in DIAD: DIAN-TU-001 (JAMA Neurology)](https://jamanetwork.com/journals/jamaneurology/fullarticle/2817630)
- [NCT06424236 — DIAN Trial: Opportunity to Prevent Dementia](https://clinicaltrials.gov/study/NCT06424236)
- [NCT00869817 — Dominantly Inherited Alzheimer Network (DIAN) Observational Study](https://clinicaltrials.gov/study/NCT00869817)
- [Eisai: Lecanemab four-year efficacy/safety data, AAIC 2025](https://www.eisai.com/news/2025/news202548.html)
- [Anti-Amyloid Therapies for Alzheimer's Disease: Progress, Pitfalls, and the Path Ahead (PMC12524931)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12524931/)
- [Population prevalence of autosomal dominant Alzheimer's disease: a systematic review (Alzheimer's & Dementia)](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/alz.037129)
- [Early-Onset Autosomal Dominant Alzheimer Disease: Prevalence, Genetic Heterogeneity, and Mutation Spectrum](https://www.sciencedirect.com/science/article/pii/S0002929707623179)
- [Longitudinal clinical, cognitive and biomarker profiles: dominantly inherited vs. sporadic early-onset AD (PMC10629466)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10629466/)
- [Plasma p-tau217 and p-tau217/Aβ1-42 as biomarkers for CSF/PET-diagnosed AD (PMC11848202)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11848202/)
- [CSF tau phosphorylation occupancies at T217/T205 (Nature Aging)](https://www.nature.com/articles/s43587-023-00380-7)
- [Effect of apolipoprotein genotype and educational attainment on cognitive function in ADAD (Nature Communications)](https://www.nature.com/articles/s41467-023-40775-z)
- [Estimated age of amyloid plaque onset and impact of APOE4 in PSEN1 E280A carriers (PMC12725120)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12725120/)
- [Convergence of Presenilin- and Tau-Mediated Pathways on Axonal Trafficking (J Neurosci / PMC2962595)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2962595/)
- [Loss of presenilin function enhances tau phosphorylation and aggregation in mice (Acta Neuropathologica Communications)](https://link.springer.com/article/10.1186/s40478-021-01259-7)
- [Genetic Testing and Counseling for Early Onset Familial Alzheimer Disease (ALZFORUM)](https://www.alzforum.org/early-onset-familial-ad/diagnosisgenetics/genetic-testing-and-counseling-early-onset-familial)
- [Preimplantation diagnosis for early-onset Alzheimer disease caused by V717L mutation (PubMed 11866650)](https://pubmed.ncbi.nlm.nih.gov/11866650/)
- [Perceptions of Knowledge, Disease Impact and Predictive Genetic Testing in EOAD At-Risk Relatives (PMC10046467)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10046467/)
- [Roles of TREM2 in the Pathological Mechanism and Therapeutic Strategies of AD (PMC11573818)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11573818/)
- [TREM2 and microglial immunity in AD: mechanisms, genetics, therapeutic opportunities (PMC12956735)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12956735/)
- [Novel App knock-in mouse model shows amyloid pathology and microglial metabolic dysregulation (Molecular Neurodegeneration / PMC9188195)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9188195/)
- [APP-KI mice do not display hallmark age-dependent cognitive decline (bioRxiv 2024)](https://www.biorxiv.org/content/10.1101/2024.05.24.595745.full.pdf)
- [APP mouse models for Alzheimer's disease preclinical studies (EMBO Journal)](https://link.springer.com/article/10.15252/embj.201797397)
- [Amyloid precursor protein and presenilin-1 knock-in immunodeficient mice (PMC11975631)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11975631/)
- [Neurophysiological alterations in mice and humans carrying mutations in APP and PSEN1 genes (Alzheimer's Research & Therapy)](https://alzres.biomedcentral.com/articles/10.1186/s13195-023-01287-6)