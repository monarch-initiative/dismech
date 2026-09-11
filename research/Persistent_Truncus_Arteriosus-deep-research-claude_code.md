---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T21:40:51.073776'
end_time: '2026-08-09T21:46:04.316155'
duration_seconds: 313.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Persistent Truncus Arteriosus
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 21
  num_turns: 24
  total_cost_usd: 1.8952571000000002
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Persistent Truncus Arteriosus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Persistent Truncus Arteriosus** covering all of the
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

I now have sufficient material to compile the comprehensive research report.

# Persistent Truncus Arteriosus (PTA) — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview:** Persistent truncus arteriosus (PTA), also called truncus arteriosus communis or common arterial trunk, is a rare, cyanotic conotruncal congenital heart defect present at birth in which the embryonic truncus arteriosus fails to septate into a separate aorta and pulmonary trunk. As a result, a **single arterial trunk arising from the heart via a single (truncal) semilunar valve** overrides a ventricular septal defect (VSD) and gives origin to the coronary arteries, one or more pulmonary arteries, and the systemic circulation, producing obligatory mixing of oxygenated and deoxygenated blood (Wikipedia; NORD; StatPearls, PMID not applicable — review source).

**Key identifiers:**
- **OMIM:** 217095 (Conotruncal Heart Malformations, CTHM) — PTA is nosologically grouped under this entry along with tetralogy of Fallot, DORV, and interrupted aortic arch, reflecting a shared developmental field defect (https://omim.org/entry/217095)
- **Orphanet:** ORPHA:3384 (Common arterial trunk) (https://www.orpha.net/en/disease/detail/3384)
- **MONDO:** MONDO:0018072
- **ICD-10-CM:** Q20.0 (Common arterial trunk)
- **MeSH:** Truncus Arteriosus, Persistent
- **Related DiGeorge/22q11.2 deletion syndrome OMIM:** 188400

**Synonyms:** Truncus arteriosus communis; common arterial trunk (CAT); persistent truncus arteriosus; truncus arteriosus (colloquial). Historically classified using the **Collett and Edwards** system (Types I–IV, based on pulmonary artery origin from the truncal root) and the **Van Praagh** system (Types A1–A4, which additionally incorporates VSD and aortic arch anomalies) — per StatPearls (NBK534774), Type A1/Type I (main pulmonary trunk arising from the left posterolateral truncal root, with a partially formed aorticopulmonary septum) is the most common, representing roughly half of cases; Type A2 (~21%) has separate, adjacent origins of the branch pulmonary arteries with an absent septum.

**Evidence basis:** Information is derived primarily from aggregated disease-level resources — clinical case series, single- and multi-center surgical outcome cohorts, autopsy/pathology series, and population-based birth-defect/epidemiological registries — rather than from a single large individual-patient EHR resource, reflecting the rarity of the condition.

---

## 2. Etiology

### Disease Causal Factors
PTA arises from **failure of aorticopulmonary (conotruncal) septation** during cardiac outflow tract (OFT) morphogenesis — i.e., failure of the conotruncal ridges/aorticopulmonary septum to form and divide the common trunk into aorta and pulmonary trunk (StatPearls NBK534774; ScienceDirect topic overview). It is fundamentally a **defect of the cardiac neural crest (CNC)–second heart field developmental unit**, with contributing genetic (chromosomal, monogenic) and environmental/teratogenic causes (see Mechanism section for the causal chain).

### Genetic Risk Factors
- **22q11.2 deletion syndrome (DiGeorge/velocardiofacial syndrome, OMIM 188400)** is the single most important genetic association, identified in **~12–35%** of PTA cases across series, with several series citing ~25% (StatPearls; PMID:9316541 "Truncus arteriosus communis associated with chromosome 22q11 deletion"). Congenital heart disease occurs in ~76% of 22q11.2-deletion patients overall, and conotruncal anomalies (TOF, interrupted aortic arch, PTA) predominate. TBX1 haploinsufficiency within the deleted region is considered the major driver of the cardiac outflow phenotype.
- **TMEM260** — Recently identified (2024) as a major non-22q11.2 genetic cause, particularly in East Asian (Japanese/Korean) populations. Biallelic loss-of-function TMEM260 variants (notably a founder variant, c.1617del, allele frequency ~0.36% in Japan) cause **Structural Heart Defects and Renal Anomalies syndrome (SHDRA)**, and TMEM260 variants may account for over half of Japanese TA cases lacking a 22q11.2 deletion (PMID:38351237, "Genetic etiology of truncus arteriosus excluding 22q11.2 deletion syndrome and identification of c.1617del, a prevalent variant in TMEM260, in the Japanese population"; correction PMID:38548934; companion paper PMC11043032).
- **NKX2-6 (OMIM *611770)** — Homozygous/biallelic homeodomain-disrupting variants (e.g., F151L) identified via autozygosity mapping in consanguineous families with common arterial trunk (PMID:15649947, Heathcote et al., *Hum Mol Genet* 2005; also PMID:32198970/Ritter et al. 2020, biallelic NKX2-6 variants and truncus arteriosus).
- **NKX2-5 (OMIM 600584)** — Variants reported in patients with PTA and interrupted aortic arch, reflecting a broader NKX2-5-associated conotruncal spectrum.
- **FOXC1/FOXC2** — Conditional inactivation in neural-crest cells produces cardiac outflow abnormalities in mouse models, implicating this pathway in human conotruncal disease.
- **GATA6** and other GATA-family transcription factors — implicated in conotruncal malformation spectrum.
- A comprehensive 2024 review, "**Human Genetics of Truncus Arteriosus**" (PMID:38884753), summarizes that beyond 22q11.2, "other congenital malformation syndromes and variants in genes encoding TBX, GATA, and NKX transcription factors and some signaling proteins have also been reported as its etiology."
- **Suggested HGNC/gene identifiers:** TBX1 (HGNC:11592), NKX2-6 (HGNC:2673), NKX2-5 (HGNC:2488), TMEM260 (HGNC:26160), FOXC1 (HGNC:3800), FOXC2 (HGNC:3801), GATA6 (HGNC:4174).

### Environmental Risk Factors
- **Maternal pregestational diabetes mellitus**: fetuses of diabetic pregnancies show a **>3-fold increased risk** of transposition of the great arteries, truncus arteriosus, and tricuspid atresia relative to non-diabetic pregnancies (PMC10671602, "Maternal Pre-Existing Diabetes: A Non-Inherited Risk Factor for Congenital Cardiopathies"). Diabetic embryopathy models show altered retinoic acid catabolism and dysregulated expression of cardiovascular developmental genes (PMC10449132).
- **Retinoic acid / isotretinoin exposure**: retinoic-acid pathway dysregulation is a recognized teratogenic route to conotruncal and aortic arch anomalies; isotretinoin (a synthetic retinoic acid analog) carries an elevated CHD risk via this mechanism.
- **Gene-environment interaction**: Maternal diabetic embryos show a synergistic increase in retinoic-acid-induced malformation susceptibility relative to euglycemic embryos, suggesting a "second hit" model relevant to human diabetic pregnancies (PMID:12196475 context, caudal regression/RA-diabetes interaction).
- No consistent sex or racial predilection is reported (StatPearls); some series note a slight male predominance without statistical significance.

### Protective Factors
No specific genetic or environmental protective factors for PTA are well-documented in the literature reviewed; periconceptional folic acid supplementation is broadly protective against congenital heart defects generally but is not specifically quantified for PTA in the sources reviewed.

### Gene-Environment Interactions
The clearest documented interaction is the **maternal diabetes × retinoic acid signaling** axis: hyperglycemia alters embryonic retinoic acid catabolism, sensitizing the conotruncal developmental field to teratogen-induced (and likely intrinsic) septation failure (PMC10449132).

---

## 3. Phenotypes

### Cardiac structural phenotype (congenital/present at birth; category: physical malformation)
- **Single arterial trunk with a single semilunar (truncal) valve** overriding a large, typically non-restrictive **VSD** (StatPearls). — Suggested term: **HP:0001719** *Truncus arteriosus* (note: cross-check exact HPO CURIE against the local OAK cache before committing; some search indices returned inconsistent HP codes for this exact term and it should be verified with `runoak`).
- **Truncal valve abnormality**: valve may be bicuspid, tricuspid, quadricuspid, or (rarely) pentacuspid; quadricuspid morphology is itself a risk factor for later reoperation.
- **Truncal valve regurgitation** — present in **~50%** of patients, ranging mild to severe; a major driver of ventricular volume overload and heart failure (Martínez-Quintana, *Transl Pediatr*; StatPearls).
- **Truncal valve stenosis** — less common (~25%), but poorly tolerated because it raises afterload on both ventricles simultaneously.
- **Right-sided or interrupted aortic arch** — right aortic arch in ~21–36% of series; aortic arch interruption defines Van Praagh Type A4.
- **Coarctation of the aorta** — critical coarctation reported in ~10% of cases.
- **Coronary artery anomalies of origin** — reported in **37–80%** of cases depending on series (ostial anomalies most common ~37–49%); no single consistent pattern, though the left coronary tends to arise more posteriorly than normal and the right coronary tends to arise from the anterior-right quadrant; single coronary artery in up to 18% of an autopsy series (PMID:837493, "Coronary arterial origin in persistent truncus arteriosus"). Coronary anomalies are an independent mortality risk factor after repair (Annals of Thoracic Surgery, S0003-4975(20)31908-1).
- **Non-confluent or absent (atretic) branch pulmonary artery** — Van Praagh Type A3.
- Additional common associated defects: secundum ASD, PDA, persistent left superior vena cava.

### Clinical/physiologic phenotype (neonatal presentation)
- **Cyanosis** (typically mild, due to complete intracardiac mixing) — often unresponsive to supplemental oxygen.
- **Signs of congestive heart failure**: tachypnea with retractions/grunting, poor feeding, failure to thrive, lethargy, hepatomegaly, jugular venous distension — emerging as pulmonary vascular resistance (PVR) physiologically falls after birth and pulmonary overcirculation develops.
- **Bounding peripheral pulses** (from diastolic runoff into the low-resistance pulmonary circuit and/or truncal regurgitation).
- **Harsh holosystolic murmur, ejection click, single loud S2** ± diastolic murmur if truncal regurgitation present.
- **Clubbing** of extremities (later/chronic finding if unrepaired).
- **22q11.2-associated extracardiac phenotype** (when syndromic): hypocalcemia/hypoparathyroidism (from parathyroid hypoplasia), thymic hypoplasia/aplasia with T-cell deficiency (profound athymia in ~1%), characteristic facial dysmorphism, cleft palate/velopharyngeal insufficiency, developmental delay/learning difficulties (>90%), and later-life psychiatric risk (autism spectrum disorder, schizophrenia).

### Phenotype characteristics
- **Age of onset**: congenital (present from birth); physiologic decompensation (CHF) typically manifests over the first days-to-weeks of life as PVR physiologically falls.
- **Severity/progression**: Without surgical correction, essentially **uniformly progressive and fatal in infancy** — mortality before 2 months of life is common, with **<20% one-year survival** without surgery (StatPearls). By roughly 6 months–4 years of unrepaired pulmonary overcirculation, irreversible pulmonary vascular obstructive disease (Eisenmenger physiology) typically precludes safe surgical correction.
- **Frequency of key associated findings** (population within PTA cohorts): truncal regurgitation ~50%; truncal stenosis ~25%; coronary anomalies 37–80%; 22q11.2 deletion 12–35% (up to ~27% in prenatally ascertained cohorts); right aortic arch ~21–36%; critical coarctation ~10%.

### Quality of life impact
Adult long-term survivors of repaired PTA report **quality of life (SF-6D) comparable to age-matched population controls** and comparable to arterial-switch-operation survivors of transposition of the great arteries, despite a higher lifetime reoperation burden (PMID:31587054, "Long-term quality of life in adults following truncus arteriosus repair"). However, objective **exercise capacity is mildly reduced** in long-term survivors — peak VO2 averaging ~70% of predicted in one 12-patient cohort followed a median 19.7 years post-repair, correlating with truncal root/neo-aortic root dilation.

### Suggested HPO terms
- Truncus arteriosus (single arterial trunk) — verify exact CURIE via local OAK/HPO lookup
- HP:0001636 Tetralogy of Fallot (for broader conotruncal-spectrum comparison, not PTA itself)
- Truncal valve regurgitation / semilunar valve insufficiency — map to the closest HPO valve-regurgitation term
- HP:0001635 Congestive heart failure
- HP:0000969 Edema / HP:0001947 Hepatomegaly (CHF signs)
- HP:0001513 Failure to thrive (or the age-specific FTT term)
- HP:0000252 Microcephaly / HP:0000750 Developmental delay (22q11.2-associated)
- HP:0002616 Aortic root aneurysm-type terms for late root dilation, if curated at disorder level

---

## 4. Genetic/Molecular Information

### Causal genes/loci
| Gene/Locus | OMIM | Role | Evidence |
|---|---|---|---|
| **22q11.2 deletion region (TBX1)** | 188400 (DiGeorge) | Haploinsufficiency of TBX1, a T-box transcription factor expressed in pharyngeal/anterior heart field mesoderm, is the leading candidate for the outflow-tract phenotype | PMID:9316541; mouse Tbx1-null phenocopies human 22q11.2DS cardiac defects |
| **NKX2-6** | *611770 | Homeodomain transcription factor in pharyngeal endoderm/OFT myocardium; biallelic homeodomain-disrupting variants cause autosomal recessive conotruncal disease including PTA | PMID:15649947; PMID:32198970 |
| **NKX2-5** | 600584 | Cardiac transcription factor; variants found in PTA and interrupted aortic arch patients | cited in OMIM 217095 |
| **TMEM260** | — (SHDRA) | Transmembrane protein of unknown precise mechanism; biallelic LOF variants (esp. East Asian founder c.1617del) cause structural heart defects + renal anomalies syndrome, with PTA as the most severe cardiac phenotype | PMID:38351237; PMC11043032; PMC11043042 |
| **FOXC1/FOXC2** | — | Forkhead transcription factors; conditional neural-crest inactivation → outflow tract defects in mice | review context |
| **GATA6** | — | GATA-family transcription factor implicated in conotruncal malformation spectrum | review context |

### Pathogenic variant characteristics
- **Variant classes**: 22q11.2 deletions are typically ~1.5–3 Mb microdeletions (detected by FISH/CMA/MLPA); NKX2-6 and TMEM260 disease-causing variants are largely **biallelic loss-of-function/missense homeodomain-disrupting** changes, consistent with **autosomal recessive** inheritance for these single-gene causes (in contrast to the typically **de novo autosomal dominant** 22q11.2 deletion).
- **Allele frequency**: TMEM260 c.1617del carrier frequency ~0.36% in the Japanese population (a founder-type variant), essentially absent outside East Asian populations.
- **Somatic vs germline**: All known causal variants for PTA are **germline**; 22q11.2 deletions are >90% de novo, with a minority inherited from a mildly-to-moderately affected parent (autosomal dominant, highly variable expressivity).
- **Functional consequence**: predominantly **loss of function / haploinsufficiency** (TBX1, NKX2-6, TMEM260), consistent with a developmental dosage-sensitivity model for outflow-tract septation genes.

### Modifier genes
Canonical **Wnt/β-catenin signaling** modifies Tbx1-driven outflow tract phenotypes: reduced β-catenin dosage significantly rescues cardiac outflow tract anomalies in a Tbx1 conditional-null 22q11.2DS mouse model, indicating Wnt/β-catenin acts genetically upstream of or in parallel with Tbx1 (PMID:28346476, PMC5386301).

### Chromosomal abnormalities
- **22q11.2 microdeletion** (most common) — the disease-defining structural variant of DiGeorge/velocardiofacial syndrome.
- No other recurrent CNV is established as a major PTA cause in the literature reviewed, though isolated case reports of other conotruncal-associated microdeletions/duplications exist.

### Epigenetic information
No PTA-specific DNA methylation or chromatin-state studies were identified in this search; this is an evidence gap.

---

## 5. Environmental Information
- **Toxin/teratogen exposure**: retinoic acid pathway agonists (isotretinoin) implicated in conotruncal defect risk via dysregulation of RA signaling central to cardiac neural crest and OFT morphogenesis.
- **Maternal metabolic factors**: pregestational (Type 1/Type 2) diabetes mellitus is the best-documented modifiable maternal risk factor, conferring >3-fold increased risk of PTA/TGA/tricuspid atresia (PMC10671602).
- **Infectious agents**: no infectious etiology is established for PTA in the literature surveyed (unlike, e.g., congenital rubella syndrome's association with PDA/pulmonary stenosis).
- **Lifestyle factors**: no PTA-specific lifestyle risk factor (smoking, alcohol) data were identified in this search; general CHD teratogen literature (e.g., alcohol, smoking) may apply non-specifically but was not directly quantified for PTA.

---

## 6. Mechanism / Pathophysiology

### Causal chain: embryology → structural defect → hemodynamic consequence

**Upstream (molecular/cellular, weeks 5–8 of human gestation):**
1. **Cardiac neural crest cell (CNCC) specification and migration** from the dorsal neural tube through pharyngeal arches III, IV, and VI into the cardiac outflow tract, where CNCCs differentiate into the elastogenic smooth muscle of the aorticopulmonary (AP) septum.
2. **Second heart field (SHF)** mesodermal cells add to the elongating outflow tract myocardium; SHF–CNCC crosstalk (FGF8, BMP, Wnt/β-catenin signaling; transcription factors TBX1, NKX2-5, NKX2-6, GATA6) patterns conotruncal septation.
3. The two spiraling streams of outflow blood flow physically influence conal and truncal septal growth; the conotruncal ridges must fuse and spiral to form the definitive aortic and pulmonary valves plus the distal AP septum.

**Point of failure:**
4. **Failure of AP septum formation / conotruncal ridge fusion** — due to CNCC ablation/dysfunction (ablation experiments in chick models directly produce PTA and outflow tract elongation failure with defective cardiac looping), TBX1 haploinsufficiency in anterior heart field mesoderm (causing premature pro-differentiation gene expression), or loss of PDGFRα/PDGFRβ signaling in Pax3+ CNCCs (disrupting cell polarity/condensation into the OFT septum) — results in **persistence of a single common arterial trunk** rather than septation into separate aorta and pulmonary trunk (PMC9601305, "Single Cell Sequencing Reveals Mechanisms of Persistent Truncus Arteriosus Formation after PDGFRα and PDGFRβ Double Knockout in Cardiac Neural Crest Cells").
5. The unseptated trunk necessarily **overrides the ventricular septal defect** because the conal septum (which normally also contributes to VSD closure) is likewise absent/malformed.

**Downstream (organ/organism-level pathophysiology, postnatal):**
6. At birth, **complete mixing of pulmonary and systemic venous return** occurs at the single ventricular-level VSD/truncal root, producing mild-to-moderate arterial desaturation (cyanosis) largely independent of any anatomic shunt restriction.
7. Because there is **no pulmonary outflow obstruction** in most cases, the ratio of pulmonary to systemic blood flow (Qp:Qs) is governed by the relative resistances of the pulmonary and systemic vascular beds. In the immediate newborn period, elevated PVR limits pulmonary flow; as **PVR physiologically falls over the first days to weeks**, pulmonary blood flow rises (pulmonary overcirculation), producing **volume-overload congestive heart failure** (tachypnea, poor feeding, hepatomegaly).
8. **Truncal valve dysfunction** — regurgitation (~50%) directly adds to ventricular volume load, compounding heart failure; stenosis (~25%) adds pressure overload/afterload to both ventricles simultaneously (since both ventricles eject through the single truncal valve), a more poorly tolerated lesion.
9. If uncorrected, chronic pulmonary overcirculation at systemic pressure (because the pulmonary bed is exposed to unrestricted systemic-level pressure via the single trunk) drives **progressive pulmonary vascular remodeling and pulmonary hypertension**, culminating in irreversible pulmonary vascular obstructive disease (Eisenmenger-type physiology) typically by early childhood, at which point surgical correction becomes contraindicated.
10. **Coronary artery anomalies** (present in a large minority-to-majority of cases due to the abnormal single-trunk geometry altering the normal aortic sinus template for coronary ostial development) create an additional substrate for perioperative and long-term myocardial ischemia/mortality risk.

### Suggested GO / CL / UBERON terms
- GO:0003151 outflow tract septum morphogenesis
- GO:0003148 outflow tract septum morphogenesis (aorticopulmonary septation specifically — verify exact GO ID)
- GO:0014032 neural crest cell development; GO:0001755 neural crest cell migration
- GO:0060575 intestinal epithelial cell differentiation (n/a — not relevant; omit)
- CL:0002350 cardiac neural crest cell (verify exact CL identifier)
- CL:0000746 cardiac muscle cell
- UBERON:0004151 outflow tract; UBERON:0002612 aorticopulmonary septum (verify against local ontology); UBERON:0002012 pulmonary trunk; UBERON:0001496 aortic valve / UBERON term for truncal/semilunar valve
- CHEBI:50648 retinoic acid (teratogen)
- CHEBI reference for prostaglandin E1/alprostadil: CHEBI:28464 (alprostadil) — verify exact ID

### Molecular profiling
No large-scale disease-specific transcriptomic/proteomic/metabolomic human PTA dataset was identified in this search (expected given the rarity and typical neonatal surgical urgency of the condition); the strongest "omics" evidence base is **single-cell sequencing of mouse CNCC-conditional-knockout models** (PMC9601305), which characterizes the CNCC condensation-failure mechanism at single-cell resolution, and **whole-genome/whole-exome sequencing cohorts** underlying the TMEM260 and other monogenic discoveries (PMID:38351237).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Heart — specifically the cardiac outflow tract/truncal root, truncal (semilunar) valve, interventricular septum (VSD), and great-vessel origins (aorta, main/branch pulmonary arteries, coronary arteries).
- **Secondary/complication-driven:** Lungs (pulmonary vascular bed — overcirculation, pulmonary hypertension, pulmonary vascular obstructive disease); liver (hepatomegaly from right heart failure); systemic circulation broadly (volume overload).
- **Body systems involved:** Cardiovascular (primary); when syndromic (22q11.2DS) — immune system (thymic hypoplasia/T-cell deficiency), endocrine (parathyroid hypoplasia/hypocalcemia), craniofacial/palatal, and neurodevelopmental/psychiatric systems.

### Tissue and cell level
- **Cardiac neural crest-derived elastogenic smooth muscle** of the (absent/malformed) aorticopulmonary septum.
- **Second heart field-derived myocardium** of the outflow tract.
- **Truncal (semilunar) valve leaflet tissue** — often dysplastic, with variable cusp number (bi-, tri-, or quadricuspid).
- **Coronary ostial/endothelial tissue** — anomalous origin patterns.
- **Pulmonary vascular smooth muscle/endothelium** — target of secondary remodeling in pulmonary hypertension.

### Subcellular level
Not a classical subcellular/organelle disease; relevant subcellular biology is at the level of transcription factor nuclear function (TBX1, NKX2-5/2-6 as GO:0005667 transcription factor complex components) and membrane protein trafficking (TMEM260 as a transmembrane protein of incompletely defined subcellular role).

### Localization
Structurally, the malformation is inherently **midline/unilateral single structure** (one trunk rather than two separate great vessels) rather than laterally paired; associated anomalies (e.g., right vs. left aortic arch) do carry laterality significance and are separately classified.

---

## 8. Temporal Development

### Onset
- **Congenital** — the structural lesion is fully established by the end of the embryonic period (~8 weeks gestation) as a failure of conotruncal septation.
- **Clinical onset of symptoms**: typically within the first days to weeks of postnatal life, as physiologic PVR decline unmasks pulmonary overcirculation and heart failure; some degree of cyanosis may be evident immediately at birth.
- **Prenatal detectability**: fetal echocardiography can detect PTA as early as 13 weeks, with routine second-trimester anomaly scanning (~18–22 weeks) as the typical diagnostic window; diagnostic accuracy for prenatal echocardiography is reported as high as 87%, though PTA can be confused with severe tetralogy of Fallot or pulmonary atresia with VSD on prenatal imaging.

### Progression (natural history, unrepaired)
- **Early infancy**: progressive congestive heart failure as PVR falls and pulmonary overcirculation develops.
- **Untreated mortality**: death in infancy is probable without surgery; <20% one-year survival without repair; most deaths occur before 2 months of age.
- **By ~4 years of age** (highly variable), irreversible pulmonary vascular obstructive disease (Eisenmenger physiology) typically develops in survivors, precluding safe corrective surgery — defining a **critical treatment window** in early infancy.
- **Course pattern**: essentially **uniformly progressive** without intervention (not relapsing-remitting); with surgical correction, the course becomes one of **staged/lifelong reintervention** (conduit growth mismatch, valve degeneration) rather than cure.

### Patterns / critical periods
- The **neonatal-to-early-infancy period** is the critical therapeutic window: single-stage complete repair within the first month of life is now the preferred strategy (StatPearls), balancing operative risk against the risk of progressive pulmonary vascular disease if repair is delayed.
- **Late postoperative "critical periods"**: right ventricle-to-pulmonary-artery (RV-PA) conduits do not grow with the child, so **somatic growth itself is a driver of reintervention need**, concentrating reoperations in childhood/adolescence.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence**: ~7 per 100,000 live births annually (range cited 7–21/100,000 across sources).
- **Proportion of CHD**: <1% of all congenital heart lesions; ~4% of *critical* congenital heart defects.
- **22q11.2 deletion syndrome background prevalence**: ~1/2,150 live births generally (of which only a subset have PTA specifically).

### Inheritance pattern
- **22q11.2 deletion (the dominant genetic cause)**: **autosomal dominant**, but **>90% de novo**; when inherited, transmission is dominant from an often mildly/variably affected parent. **Variable expressivity and incomplete/variable penetrance for specific organ phenotypes** (including the cardiac phenotype) is well documented — not every deletion carrier has a conotruncal cardiac defect.
- **NKX2-6-related and TMEM260-related (SHDRA) forms**: **autosomal recessive** (biallelic variants identified in consanguineous families for NKX2-6; biallelic LOF for TMEM260).
- **Isolated/non-syndromic PTA**: largely presumed multifactorial (polygenic + environmental), consistent with the broader "second/third-hit" model of CHD genetics.
- **Founder effect**: TMEM260 c.1617del is a population-specific founder-type variant essentially restricted to Japanese/Korean populations.
- **Consanguinity**: relevant specifically to the recessive NKX2-6-associated families, in which autozygosity mapping was used for gene discovery.

### Population demographics
- **Sex ratio**: no significant sex predilection established; some series note a slight, non-significant male predominance.
- **Race/ethnicity**: no broad racial predilection reported for PTA overall, though the TMEM260 founder variant creates an ethnicity-specific (East Asian) genetic subgroup.
- **Geographic distribution**: no endemic geographic clustering beyond the population-genetic TMEM260 founder effect in Japan/Korea.
- **Termination-of-pregnancy rates after prenatal diagnosis**: substantial — one series reported 68% of fetuses diagnosed before 24 weeks did not survive to birth (spontaneous fetal death or elective termination); another reported 41.2% elective termination rate, reflecting the severity of prenatal counseling discussions.

---

## 10. Diagnostics

### Prenatal
- **Fetal echocardiography** — primary prenatal diagnostic modality; detects the single arterial trunk, large VSD, and pulmonary artery origin pattern; feasible from as early as 13 weeks, routinely by 18–22 weeks; diagnostic accuracy up to 87%, with differential challenges vs. severe tetralogy of Fallot and pulmonary atresia with VSD.
- **Prenatal genetic testing** — 22q11.2 deletion testing (e.g., via chromosomal microarray, FISH, or NIPT-adjacent approaches) recommended whenever PTA is suspected prenatally, given the ~12–35% (up to 27% in prenatal cohorts) 22q11.2DS association.

### Postnatal clinical/imaging tests
- **Transthoracic echocardiography** — primary postnatal diagnostic and surveillance modality (truncal valve morphology/function, VSD, branch PA origins, coronary origins where visualizable).
- **Cardiac MRI or CT angiography (CTA)** — used to delineate coronary anatomy, branch pulmonary artery anatomy, and aortic arch anomalies (interruption/coarctation) not fully resolved by echo.
- **Cardiac catheterization** — generally reserved for interventional procedures (e.g., balloon angioplasty/stenting of branch PA or conduit stenosis) rather than primary diagnosis.
- **Physical exam findings supporting diagnosis**: harsh holosystolic murmur, ejection click, single loud S2, ± diastolic murmur (truncal regurgitation), bounding pulses, cyanosis/clubbing, hepatomegaly.

### Genetic testing
- **Chromosomal microarray (CMA) / FISH for 22q11.2 deletion** — first-line genetic test given the high pretest probability; FISH historically used for targeted 22q11.2 detection, now largely supplanted/complemented by CMA for genome-wide resolution.
- **Gene panel / exome sequencing** — indicated when 22q11.2 deletion testing is negative, particularly to identify NKX2-6, NKX2-5, TMEM260 (especially in patients of East Asian ancestry, where TMEM260 targeted testing or panel inclusion is specifically warranted), or other monogenic conotruncal-disease genes.
- **Karyotyping** — of historical/adjunctive value for detecting other chromosomal abnormalities.

### Clinical diagnostic criteria / differential diagnosis
No formal DSM/ICD-style clinical scoring criteria exist beyond echocardiographic/anatomic definition. Key differentials: **severe tetralogy of Fallot with pulmonary atresia**, and **pulmonary atresia with VSD and major aortopulmonary collateral arteries (MAPCAs)** — both can closely mimic PTA, especially prenatally, and require careful distinction of pulmonary arterial origin (from the common trunk vs. from the descending aorta/collaterals).

### Screening
No population-level newborn screening test specifically targets PTA; however, **pulse oximetry-based critical congenital heart disease (CCHD) newborn screening**, now standard in many health systems, will typically flag PTA (and other critical CHDs) via low peripheral oxygen saturation, prompting urgent echocardiography.

---

## 11. Outcome / Prognosis

### Survival without treatment
- Mortality is probable in infancy without surgical correction; **<20% survive to one year** unrepaired (StatPearls).

### Survival with surgical repair
- **Perioperative/hospital mortality**: ~6% in a representative single-center series (3/50 patients) — two deaths from pulmonary hypertensive crisis, one from pneumonia (PLOS ONE, PMC4713837).
- **Actuarial survival**: 87.7% at both 1 and 5 years post-repair in that series; other multicenter series report **20-year survival >80%** after primary repair (StatPearls).
- **Very long-term (30-year) survival**: reported at **68.5%** in one long-term single-center cohort, with truncal valve regurgitation identified as a key risk factor for both mortality and reoperation.
- **Freedom from reoperation**: ~92.9% at 5 years in one series; another reports freedom from RV-PA conduit/branch-PA reoperation of only **59% at 5 years and 28% at 10 years**, and ~75% of patients require reintervention by 10 postoperative years — reoperation is essentially inevitable given somatic outgrowth of non-growing conduits.

### Prognostic/risk factors
- **Significant preoperative truncal valve regurgitation** — independent risk factor for mortality.
- **Quadricuspid truncal valve morphology, truncal valve insufficiency at diagnosis, and truncal valve intervention at index repair** — associated with increased reoperation risk.
- **RV-PA conduit size ≤11 mm** — associated with higher risk of early catheter-based reintervention/reoperation.
- **Coronary artery anomalies** (ostial stenosis, intramural course, juxtacommissural origin) — independently associated with increased mortality after repair.
- **Late referral / delayed repair** — associated with higher risk of postoperative pulmonary hypertensive crisis.

### Functional/quality-of-life outcomes
- Nearly all long-term survivors are in **NYHA functional class I–II**.
- Adult QOL (SF-6D) is **comparable to general-population controls** and to arterial-switch-operation (TGA) survivors, despite the higher truncus reoperation burden.
- **Exercise capacity is mildly reduced** long-term (peak VO2 ~70% of predicted in one cohort), correlating with truncal/neo-aortic root dilation.

### Complications
Early postoperative: pulmonary hypertensive crisis, low cardiac output syndrome, right bundle branch block, supraventricular tachycardia, mediastinal bleeding, pleural effusion, pneumothorax, cardiac tamponade. Late: conduit stenosis/regurgitation requiring replacement, truncal (neo-aortic) valve regurgitation/stenosis requiring repair or replacement, arrhythmia, and (in unrepaired or late-presenting patients) irreversible pulmonary vascular disease.

---

## 12. Treatment

### Medical stabilization (pre-/peri-operative)
- **Diuretics** (loop diuretics, thiazides) for congestive heart failure control. — Suggested NCIT: NCIT:C15986 (Pharmacotherapy) + therapeutic_agent class (diuretic).
- **Avoidance of supplemental oxygen** where possible, since it lowers PVR and worsens pulmonary overcirculation.
- **Prostaglandin E1 (alprostadil)** — used selectively when ductal patency is needed to support systemic perfusion (e.g., in the presence of critical coarctation or interrupted arch); dosed 0.01–0.1 mcg/kg/min IV; ~82% of infants show effective clinical improvement at the initial 0.1 mcg/kg/min dose, with effect maintained at reduced maintenance doses; key adverse effects include apnea, peripheral vasodilation, and hypotension (StatPearls: Alprostadil, NBK542217). — Suggested NCIT: NCIT:C15986 Pharmacotherapy; therapeutic_agent CHEBI (alprostadil/prostaglandin E1, verify exact CHEBI ID e.g. CHEBI:28464).
- **Correction of metabolic/electrolyte derangements.**

### Surgical repair (definitive treatment)
- **Single-stage complete primary repair**, preferably within the **first month of life**, comprising: separation of the pulmonary arterial supply from the truncal root; **VSD patch closure** (baffling the truncal/aortic outflow to the left ventricle); **RV-to-PA conduit** (homograft, valved or non-valved conduit) reconstruction of the right ventricular outflow tract; and concurrent repair of any truncal valve regurgitation/stenosis and aortic arch anomaly (coarctation repair/arch reconstruction) as needed. — Suggested NCIT: NCIT:C15329 (Surgical Procedure) / NCIT:C16186 (Orthopedic — N/A) → more specifically a cardiac surgical repair term; therapeutic_modality: SURGERY.
- **Staged repair** (e.g., pulmonary artery banding followed by delayed correction) is **not routinely recommended** due to higher morbidity/mortality compared with primary single-stage repair.
- **Truncal valve repair or replacement** — performed at index repair or later, for significant regurgitation/stenosis; a documented risk factor for reoperation when performed at index surgery (reflecting valve severity rather than a causal effect of the intervention itself).
- **Reintervention**: transcatheter balloon angioplasty/stenting of conduit or branch pulmonary artery stenosis; surgical conduit replacement as the child outgrows the original conduit — an expected, near-universal component of lifelong management (freedom from reintervention only 28% at 10 years in some series).

### Genetic counseling / multidisciplinary supportive care
- **Genetic counseling** strongly recommended given the 22q11.2 deletion association (recurrence risk implications, extracardiac surveillance needs). — NCIT:C15240 Genetic Counseling.
- **Supportive/multidisciplinary care**: pediatric cardiology, cardiac surgery, intensive care, genetics, radiology, nursing, respiratory therapy, social work, and (with age) transition to adult congenital heart disease (ACHD) specialty care; mental health support given the psychosocial burden of chronic cardiac disease and repeated procedures.
- **Immunologic/endocrine management** in 22q11.2DS-associated cases: calcium/vitamin D management for hypoparathyroidism-driven hypocalcemia; immunologic monitoring/prophylaxis for T-cell deficiency; avoidance of live vaccines in significant T-cell immunodeficiency.

### Experimental / emerging
No PTA-specific gene therapy, cell therapy, or targeted molecular therapeutic was identified in this search — treatment remains fundamentally surgical/structural, consistent with the anatomic nature of the defect. A computational modeling study (arXiv:2601.08932, "Simulations Predict Improved Valve Performance Without Direct Leaflet Intervention After Neonatal Truncus Arteriosus Repair") represents an emerging in-silico approach to optimizing surgical valve/conduit strategy rather than a new therapeutic modality per se.

### Treatment outcomes
See Section 11 (Outcome/Prognosis) for detailed survival, reoperation, and functional-outcome statistics associated with each treatment strategy.

---

## 13. Prevention

### Primary prevention
- **Optimization of pregestational maternal glycemic control** in diabetic mothers is the most directly actionable primary-prevention lever identified in this literature, given the >3-fold increased conotruncal-defect risk associated with maternal pregestational diabetes.
- **Avoidance of retinoic acid/isotretinoin exposure during pregnancy** (established teratogen avoidance, standard obstetric practice — isotretinoin carries FDA pregnancy category X / iPLEDGE program restrictions generally, not PTA-specific).
- General periconceptional folic acid supplementation is standard CHD-risk-reduction practice, though not specifically quantified for PTA in the literature surveyed.

### Secondary prevention / screening
- **Prenatal ultrasound anomaly screening** (routine second-trimester fetal echocardiography) enables early detection, allowing informed counseling, delivery planning at a cardiac surgical center, and prostaglandin availability at birth if arch anomalies are present.
- **22q11.2 deletion testing** upon prenatal or postnatal PTA diagnosis enables early identification of associated hypocalcemia, immunodeficiency, and syndromic features, allowing proactive endocrine/immunologic management.
- **Newborn pulse oximetry CCHD screening** provides a postnatal safety net for cases not detected prenatally.

### Tertiary prevention
- **Timely single-stage neonatal surgical repair** (within the first month of life) is itself the principal tertiary-prevention strategy — preventing the otherwise inevitable progression to irreversible pulmonary vascular obstructive disease.
- **Structured lifelong cardiology follow-up** (serial echocardiography, conduit/valve surveillance) to detect and intervene on conduit stenosis, valve regurgitation, and arrhythmia before they cause irreversible ventricular dysfunction.

### Genetic counseling / reproductive planning
Recommended for families of an affected child, particularly given the identifiable 22q11.2 deletion (autosomal dominant, variable expressivity, ~50% recurrence risk if a parent carries the deletion) and the autosomal recessive NKX2-6/TMEM260 forms (25% recurrence risk per pregnancy, elevated with consanguinity).

---

## 14. Other Species / Natural Disease

- **Naturally occurring PTA-like disease** is not well-documented as a spontaneous veterinary clinical entity in the sources surveyed (unlike, e.g., patent ductus arteriosus, which is common in dogs); this literature search did not identify OMIA entries or veterinary case series specifically for spontaneous PTA in companion or production animals. This is likely because complete conotruncal septation failure is generally not compatible with survival to veterinary presentation in most species, or is under-reported. (This should be flagged as an evidence gap requiring dedicated OMIA/veterinary-literature search if the KB entry requires this section populated.)
- **Comparative embryology** is well studied experimentally (see Model Organisms below) even though spontaneous natural disease reports are sparse.

---

## 15. Model Organisms

### Mouse models
- **Tbx1 conditional/null mutant mice** — the primary genetic model of 22q11.2DS-associated PTA. Tbx1-null mice show neonatal lethality with cleft palate, abnormal inner ears, absent thymus and parathyroid glands, and **persistent truncus arteriosus**, closely phenocopying the human 22q11.2 deletion syndrome cardiac phenotype. Graded hypomorphic Tbx1 dosage (100%→2%) across allelic series produces a **dosage-dependent spectrum** of outflow tract defects — PTA at the most severe end, through tetralogy of Fallot and double-outlet right ventricle at intermediate dosage — directly modeling human phenotypic variability from a single haploinsufficient locus.
- **Tbx1 conditional-null + reduced β-catenin dosage** — genetic rescue experiment demonstrating that lowering Wnt/β-catenin pathway dosage significantly rescues Tbx1-mutant outflow tract anomalies, establishing an epistatic/modifier relationship (PMID:28346476).
- **Pax3 Splotch (Sp1H) mutant mice** — classic neural-crest-deficient model; homozygotes show failure of truncus arteriosus septation and aortic arch-derived vessel anomalies, historically one of the first genetic confirmations of the CNCC-dependence of conotruncal septation (PMID:2619088, "Persistent truncus arteriosus in the Splotch mutant mouse").
- **PDGFRα/PDGFRβ double-knockout in Pax3+ cardiac neural crest cells** — recent (single-cell RNA-seq-characterized) model showing that combined loss of platelet-derived growth factor receptor signaling in CNCCs disrupts CNCC condensation/polarity within the outflow tract septum, producing PTA and elucidating a cell-biological (cytoskeletal/adhesion) mechanism distinct from pure transcription-factor loss (PMC9601305).
- **Cardiac neural crest surgical ablation (chick, extrapolated conceptually to mammalian models)** — ablation of the CNC in chick embryos directly produces PTA with failed outflow tract elongation and defective cardiac looping, establishing the foundational CNCC-dependence paradigm for conotruncal septation.

### Comparative/cross-species notes
- **Chick embryo** — the classical experimental model for CNC ablation studies of outflow tract septation; closely models the mammalian (including human) requirement for CNC-directed septation.
- **Xenopus** — notably, cardiac neural crest is *dispensable* for outflow tract septation in Xenopus, a striking cross-species divergence from chick/mouse/human biology, underscoring that CNCC-dependence of septation is not universally conserved across vertebrates and that Xenopus is a poor model for PTA specifically.
- **Zebrafish** — the zebrafish outflow tract **does not become remodeled or septated** at all (unlike higher vertebrates), so zebrafish cannot model true PTA; zebrafish CNC ablation instead alters ventricular myocardial cardiomyocyte number rather than septation. Zebrafish remain useful for dissecting general second-heart-field/outflow-tract progenitor biology (e.g., nkx2.5+ anterior lateral plate mesoderm-derived progenitors), but this is a clear **human-model-mismatch** consideration: zebrafish outflow tract biology should not be over-extrapolated to human septation-failure mechanisms without chick/mouse cross-validation.

### Applications and limitations
- Mouse Tbx1-dosage allelic series is the best-validated model for **dosage-dependent phenotypic severity**, directly relevant to the variable cardiac penetrance seen in human 22q11.2 deletion carriers.
- Chick CNC-ablation remains the classical model for **mechanistic dissection of CNCC contribution to septation** but is less genetically tractable than mouse for modern single-cell/genomic approaches.
- No model organism to date fully recapitulates the human TMEM260-SHDRA phenotype (renal + cardiac); this represents an open modeling gap.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Domain | Suggested term(s) — verify exact CURIE/label via OAK before committing |
|---|---|
| MONDO | MONDO:0018072 (Persistent truncus arteriosus / common arterial trunk) |
| Orphanet | ORPHA:3384 |
| OMIM | 217095 (Conotruncal Heart Malformations); 188400 (DiGeorge syndrome, comorbid) |
| ICD-10-CM | Q20.0 |
| HGNC genes | TBX1, NKX2-6, NKX2-5, TMEM260, FOXC1, FOXC2, GATA6 |
| GO (process) | outflow tract septum morphogenesis; neural crest cell migration; canonical Wnt signaling pathway |
| CL (cell type) | cardiac neural crest cell; second heart field cardiomyocyte progenitor |
| UBERON (anatomy) | outflow tract; aorticopulmonary septum; truncal/semilunar valve; pulmonary trunk |
| CHEBI (chemical) | retinoic acid; alprostadil (prostaglandin E1) |
| NCIT (treatment) | Surgical Procedure; Pharmacotherapy; Genetic Counseling |
| HPO (phenotype) | Truncus arteriosus (verify exact CURIE); Congestive heart failure; Failure to thrive; Developmental delay (22q11.2-associated) |

---

## Notable Evidence Gaps (flag for curators)
1. **No spontaneous veterinary/natural-disease literature** was located for PTA specifically — Section 14 is thin and should be treated as a gap pending dedicated OMIA search.
2. **No PTA-specific epigenomic/methylation dataset** was identified.
3. **Exact HPO CURIE** for "truncus arteriosus" returned inconsistent results across search sources and must be confirmed directly via `runoak -i sqlite:obo:hp` before use.
4. **Human transcriptomic/single-cell data** for PTA cardiac tissue itself (as opposed to mouse CNCC knockout models) does not appear to be well represented in the literature surveyed — mechanistic single-cell evidence is currently MODEL_ORGANISM-only, a relevant `HUMAN_MODEL_MISMATCH` consideration for pathophysiology curation.

## Sources

- [OMIM #217095 — Conotruncal Heart Malformations](https://omim.org/entry/217095)
- [OMIM #188400 — DiGeorge Syndrome](https://www.omim.org/entry/188400)
- [OMIM *611770 — NKX2-6](https://omim.org/entry/611770)
- [Orphanet — Common arterial trunk (ORPHA:3384)](https://www.orpha.net/en/disease/detail/3384)
- [GARD — Persistent truncus arteriosus](https://rarediseases.info.nih.gov/diseases/16627/persistent-truncus-arteriosus)
- [NORD — Truncus Arteriosus](https://rarediseases.org/rare-diseases/truncus-arteriosus/)
- [StatPearls — Truncus Arteriosus (NBK534774)](https://www.ncbi.nlm.nih.gov/books/NBK534774/)
- [Medscape — Truncus Arteriosus: Background, Etiology, Pathophysiology](https://emedicine.medscape.com/article/892489-overview)
- [PubMed 38884753 — Human Genetics of Truncus Arteriosus](https://pubmed.ncbi.nlm.nih.gov/38884753/)
- [PubMed 38351237 — Genetic etiology of truncus arteriosus excluding 22q11.2 deletion syndrome; TMEM260](https://pubmed.ncbi.nlm.nih.gov/38351237/)
- [PubMed 38548934 — Correction notice](https://pubmed.ncbi.nlm.nih.gov/38548934/)
- [PMC11043032 — TMEM260 c.1617del, Journal of Human Genetics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11043032/)
- [PMC11043042 — TMEM260 in truncus arteriosus, Japanese population](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11043042/)
- [PubMed 9316541 — Truncus arteriosus communis associated with chromosome 22q11 deletion](https://pubmed.ncbi.nlm.nih.gov/9316541/)
- [PMC5386301 / PubMed 28346476 — β-catenin dosage rescue in Tbx1 conditional null mouse model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5386301/)
- [PubMed 15649947 — Common arterial trunk associated with a homeodomain mutation of NKX2.6](https://pubmed.ncbi.nlm.nih.gov/15649947/)
- [PubMed 32198970 — NKX2-6 related congenital heart disease: biallelic variants](https://pubmed.ncbi.nlm.nih.gov/32198970/)
- [PubMed 2619088 — Persistent truncus arteriosus in the Splotch mutant mouse](https://pubmed.ncbi.nlm.nih.gov/2619088/)
- [PMC9601305 — Single Cell Sequencing Reveals Mechanisms of PTA Formation after PDGFRα/β Double Knockout in Cardiac Neural Crest Cells](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9601305/)
- [PubMed 837493 — Coronary arterial origin in persistent truncus arteriosus](https://pubmed.ncbi.nlm.nih.gov/837493/)
- [Annals of Thoracic Surgery — Coronary Artery Anomalies Are Associated With Increased Mortality After Truncus Arteriosus Repair](https://www.annalsthoracicsurgery.org/article/S0003-4975(20)31908-1/pdf)
- [PLOS ONE — Outcomes of Surgical Repair for Persistent Truncus Arteriosus from Neonates to Adults (PMC4713837)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4713837/)
- [PubMed 33726908 — Long-term outcomes of truncus arteriosus repair: modulated renewal competing risks analysis](https://pubmed.ncbi.nlm.nih.gov/33726908/)
- [PubMed 27126954 — Long-term Outcomes after Truncus Arteriosus Repair: Single-center 40-year experience](https://pubmed.ncbi.nlm.nih.gov/27126954/)
- [PubMed 31587054 — Long-term quality of life in adults following truncus arteriosus repair](https://pubmed.ncbi.nlm.nih.gov/31587054/)
- [PMC10328806 — Death, reoperation, and late cardiopulmonary function after truncus repair](https://pmc.ncbi.nlm.nih.gov/articles/PMC10328806/)
- [PMC11508351 — Diagnosis, Management and Outcome of Truncus Arteriosus Communis Diagnosed during Fetal Life](https://pmc.ncbi.nlm.nih.gov/articles/PMC11508351/)
- [PubMed 34028563 — Prenatal diagnosis, associated findings and postnatal outcome of fetuses with truncus arteriosus communis](https://pubmed.ncbi.nlm.nih.gov/34028563/)
- [PubMed 19015910 — Truncus arteriosus: diagnostic accuracy, outcomes, and impact of prenatal diagnosis](https://pubmed.ncbi.nlm.nih.gov/19015910/)
- [PMC10671602 — Maternal Pre-Existing Diabetes: A Non-Inherited Risk Factor for Congenital Cardiopathies](https://pmc.ncbi.nlm.nih.gov/articles/PMC10671602/)
- [PMC10449132 — Hyperglycemia alters retinoic acid catabolism in embryos exposed to maternal diabetic milieu](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449132/)
- [UpToDate — DiGeorge (22q11.2 deletion) syndrome: Clinical features and diagnosis](https://tkl.uptodate.com/contents/digeorge-22q11-2-deletion-syndrome-clinical-features-and-diagnosis/print)
- [StatPearls — Alprostadil (NBK542217)](https://www.ncbi.nlm.nih.gov/books/NBK542217/)
- [Translational Pediatrics — Truncus arteriosus and truncal valve regurgitation](https://tp.amegroups.org/article/view/24211/html)
- [Development (Journal of Biologists) — Cardiac neural crest is dispensable for outflow tract septation in Xenopus](https://journals.biologists.com/dev/article/138/10/2025/44388/Cardiac-neural-crest-is-dispensable-for-outflow)
- [NCBI Bookshelf — Utilizing Zebrafish to Understand Second Heart Field Development](https://www.ncbi.nlm.nih.gov/books/NBK500310/)
- [ICD10Data.com — Q20.0 Common arterial trunk](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q20-Q28/Q20-/Q20.0)