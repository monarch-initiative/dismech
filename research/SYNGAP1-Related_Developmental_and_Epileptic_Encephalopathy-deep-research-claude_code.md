---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T07:24:19.815399'
end_time: '2026-07-18T07:29:27.157806'
duration_seconds: 307.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SYNGAP1-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
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
  - claude-opus-4-8
  web_search_requests: 10
  num_turns: 12
  total_cost_usd: 1.6154385
  session_id: ad6646bd-c39c-4770-be8f-1212a1a64a2f
  stop_reason: end_turn
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SYNGAP1-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SYNGAP1-Related Developmental and Epileptic Encephalopathy** covering all of the
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

Alright, I've got a rich, well-cited picture. Here's the full report.

---

# SYNGAP1-Related Developmental and Epileptic Encephalopathy — Comprehensive Research Report

> A quick orientation before we dive in, because this disease is a bit of a naming hydra: what the clinic now calls **SYNGAP1-related developmental and epileptic encephalopathy (SYNGAP1-DEE)** is the *same entity* that OMIM still files under the dusty old label "mental retardation, autosomal dominant 5 (MRD5)." Same gene, same kids, three decades of shifting vocabulary. Think of it like a river that's been renamed by every town it passes through — I'll flag the aliases as we go so the knowledge-base entry can carry them all.
>
> **Evidence-hygiene note for the curator (you, Harry):** PMIDs I pulled *directly from the searches* are marked ✓. A handful of foundational mechanism papers I'm citing from background knowledge are marked ⚠︎VERIFY — run `just fetch-reference PMID:XXXX` on those before any snippet goes into a YAML, per the project's DR-hallucination SOP. I've kept quotes as exact strings from the abstracts I actually fetched.

---

## 1. Disease Information

**What it is.** SYNGAP1-DEE is a monogenic **synaptopathy** — a disease of the synapse, the little chemical handshake between neurons — caused by having only one working copy of the *SYNGAP1* gene (haploinsufficiency). Clinically it's a near-obligate triad: **developmental delay/intellectual disability (essentially 100%), generalized epilepsy (~84–92%), and autism/behavioral–sensory abnormalities (~57–68%)**, layered on early hypotonia (floppiness) and a distinctive, hard-to-treat epilepsy syndrome. Developmental delay almost always shows up *first*, in the first months to ~2 years of life, and seizures arrive later — a temporal signature that matters diagnostically ([Vlaskamp et al. 2019, Neurology, PMID:30541864 ✓](https://pubmed.ncbi.nlm.nih.gov/30541864/)).

**Key identifiers** (from GenCC/OMIM/Orphanet/MalaCards searches):
- **Gene:** *SYNGAP1*, HGNC:11497, locus **6p21.32**
- **OMIM disease:** [#612621](https://www.omim.org/entry/612621) — "Intellectual developmental disorder, autosomal dominant 5; MRD5"
- **MONDO:** MONDO:0012960 (intellectual developmental disorder, autosomal dominant 5); the "SYNGAP1-related developmental and epileptic encephalopathy" concept is also carried by [NORD/Orphanet](https://rarediseases.org/mondo-disease/syngap1-related-developmental-and-epileptic-encephalopathy/) — worth confirming the exact MONDO with `runoak` since there may be a newer DEE-specific term
- **Orphanet:** [ORPHA:544254](https://www.orpha.net/en/disease/detail/544254)
- **ICD-10:** G40.4 (generalized epilepsy) / F79 for the ID axis; **ICD-11:** LD90.Y (per search)
- **MeSH:** no dedicated descriptor; indexed under Intellectual Disability + Epilepsies, Generalized + *SYNGAP1* supplementary concept

**Synonyms / alternative names:** SYNGAP1-related intellectual disability; SYNGAP1-ID; MRD5; mental retardation, autosomal dominant 5; SYNGAP1 encephalopathy; SYNGAP1-related nonsyndromic ID with epilepsy; SYNGAP1 syndrome (advocacy usage, [CureSYNGAP1](https://curesyngap1.org/)).

**Data provenance.** The knowledge base here should draw on *aggregated disease-level* sources — GeneReviews ([NBK537721](https://www.ncbi.nlm.nih.gov/books/NBK537721/)), Orphanet, and published cohort/registry studies — rather than individual EHR. The two big modern denominators are the **SynGAP Research Fund / Ciitizen digital natural-history registry** (147 patients, [Wiltrout et al. 2024, Epilepsia, PMC12375243 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375243/)) and the **Vlaskamp 2019 international cohort** (57 patients, PMID:30541864).

---

## 2. Etiology

**Primary cause — genetic, monogenic.** Heterozygous **loss-of-function (LoF)** variants in *SYNGAP1*, or 6p21.32 microdeletions encompassing the gene. The overwhelming majority are **de novo** (a fresh mutation in the child, not inherited) — this was the founding observation ([Hamdan et al. 2009, NEJM 360:599–605, PMID:19196676 ✓](https://pubmed.ncbi.nlm.nih.gov/19196676/); [Hamdan et al. 2011, PMID:21237447 ✓](https://pubmed.ncbi.nlm.nih.gov/21237447/)). The disease mechanism is **dosage** — you need two full servings of SynGAP protein and one isn't enough; there's no rescuing spare.

**Risk factors.**
- *Genetic:* The causal variant IS the risk factor; because it's de novo, classic "susceptibility loci / modifier genes" don't drive occurrence. Advanced parental age is a weak generic contributor to de novo mutation rates (not SYNGAP1-specific).
- *Environmental / lifestyle / occupational:* **None established.** This is a "bad luck at conception" disorder, not an exposure disorder. No toxin, infection, diet, or occupational link.

**Protective factors.** No genetic or environmental protective factors are established in humans. *Mechanistically interesting caveat from mouse work:* the disease is developmental-timing-sensitive, so the "protective" lever is **when** you restore protein, not any exogenous exposure (see §6/§15).

**Gene–environment interactions.** Not applicable in the conventional sense. The one real "×environment" axis is **seizure triggers**: eating and eye-closure provoke reflex seizures in a substantial minority (~25% eating-triggered; [Vlaskamp 2019](https://pubmed.ncbi.nlm.nih.gov/30541864/)) — an interaction between the genetic substrate and sensory/behavioral state, not toxicology.

---

## 3. Phenotypes

The phenotype is a **generalized DEE plus a neurodevelopmental disorder**. Frequencies below are anchored to the 147-patient registry ([Wiltrout 2024 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375243/)) and the 57-patient Vlaskamp cohort ([2019 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC6340340/)).

**Neurodevelopmental / cognitive**
- **Global developmental delay / intellectual disability** — HP:0001263 / HP:0001249. Frequency ~**100%** ("All patients were diagnosed with global developmental delay (GDD) and/or ID"). Usually moderate–severe, occasionally mild. Onset: infancy; **precedes seizures**. Course: developmental **plateau between ~2 and 5 years**, possibly epilepsy-modulated ([Kim et al. 2024, AJMG-A, PMID:38563110 ✓](https://pubmed.ncbi.nlm.nih.gov/38563110/)).
- **Absent/impaired speech** — HP:0001344 / HP:0000750. Genotype-linked: "83% of individuals with variants in exons 1–4 were able to speak in phrases vs 31% of individuals with variants in exons 5–19" ([Wiltrout 2024 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375243/)).
- **Autism spectrum disorder / autistic behavior** — HP:0000717 / HP:0000729. ~**57–68%**.
- **Behavioral problems** (HP:0000708) ~68%; **anxiety** (HP:0000739); **aggression/impulsivity**.

**Epilepsy (the DEE core)** — HP:0011097 (generalized), HP:0002133 (status), HP:0002123 (generalized myoclonic)
- **Generalized epilepsy** overall ~**84–92%**; "Of the 57 patients, 56 had epilepsy: generalized in 55" ([Vlaskamp 2019 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC6340340/)).
- **Eyelid myoclonia with absences** — HP:0032648 (eyelid myoclonia) / HP:0002121 (absence). **~65%** — the signature semiology.
- **Myoclonic seizures** — HP:0032794/HP:0002123. **~34%**.
- **Atypical absences** HP:0007270 **~20%**; **typical absences** HP:0011147 **~18%**.
- **Atonic / drop attacks** — HP:0010819. **~14%**; a *novel* semiology described as "eyelid myoclonia evolving to a myoclonic-atonic or atonic seizure."
- **Reflex seizures triggered by eating** — ~**25%**; and by **eye closure**.
- **Epilepsy syndromic overlap:** myoclonic-atonic epilepsy (Doose), epilepsy with eyelid myoclonia (Jeavons-like), epilepsy with myoclonic absences.
- **Onset:** median **~2 years** (Vlaskamp) to **31–34 months** (registry), range ~4 months–7 years. **Course: often refractory and evolving** — up to ~35% show semiology evolution; EEG shifts from **occipital → frontal** discharges with age ([Frontiers/Kim EEG study 2024](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2024.1321282/full)).

**Motor / tone**
- **Hypotonia** — HP:0001252 (early, prominent). **Ataxia / abnormal gait** — HP:0001251 / HP:0001288, ~**47%**. **Unstable/wide-based gait**.

**Systemic / other**
- **Sleep problems** — HP:0002360, ~**61%**.
- **Feeding difficulties** — HP:0011968, ~**47%**; oral-motor dysfunction, drooling.
- **Constipation / GI dysmotility** — HP:0002019.
- **High pain threshold / abnormal pain sensitivity** and **strabismus** (HP:0000486) reported.
- **Behavioral/sensory abnormalities** (sensory-seeking) frequently noted.

**Quality-of-life impact.** Severe and pervasive: most affected individuals are **non- or minimally-verbal**, need lifelong supervision, and the combination of refractory seizures + autism + sleep disruption drives heavy caregiver burden. No SYNGAP1-specific EQ-5D/SF-36 dataset exists; QoL is captured qualitatively in registry/advocacy work ([Graglia et al. 2025 roadmap, PMID:39807402 ✓](https://pubmed.ncbi.nlm.nih.gov/39807402/)).

**Genotype–phenotype summary:** variants toward the **5′ end (exons 1–6)** trend milder for ID/ASD but carry **higher refractory-epilepsy** risk; SH3-binding-motif variants show **lower epilepsy** frequency ([Hong et al. 2025, Clin Genet](https://onlinelibrary.wiley.com/doi/10.1111/cge.14661); [Wiltrout 2024 ✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375243/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SYNGAP1*** (synaptic Ras-GTPase-activating protein 1), **HGNC:11497**, chromosome **6p21.32**, ~19 exons, multiple C-terminal isoforms (α1, α2, β, γ). OMIM gene *603384*; disease *612621*.

**Pathogenic variants.**
- **Type/class:** predominantly **loss-of-function** — nonsense, frameshift, canonical splice-site, and a smaller share of missense (often clustering in the C2/GAP catalytic domain). Whole-gene/6p21.32 microdeletions (CNVs) also cause it. LoF-intolerant gene (very high pLI in gnomAD).
- **ACMG classification:** the vast majority are **pathogenic/likely pathogenic**; truncating de novo variants meet PVS1+PS2. VUS are typically missense.
- **Allele frequency:** essentially **absent from population databases** (gnomAD) — consistent with a highly penetrant, de novo, LoF disorder.
- **Origin:** **germline, de novo** in the overwhelming majority; rare inherited cases from a mildly affected or mosaic parent exist (relevant to recurrence counseling).
- **Functional consequence:** **haploinsufficiency** (loss of function, dosage). Not a classic dominant-negative for truncating alleles, though some C-terminal isoform-specific variants may perturb splice-form balance ([Endogenous Syngap1 α splice forms, eLife 2022](https://elifesciences.org/articles/75707)).

**Modifier genes.** None validated; residual phenotypic variance is attributed to variant position/isoform impact rather than a mapped modifier.

**Epigenetics.** No established disease-driving DNA-methylation or histone signature. (A reproducible "episignature" for SYNGAP1 has not been robustly reported the way it has for some other NDD genes — an open question, not an established feature.)

**Chromosomal abnormalities.** **6p21.32 microdeletions** spanning *SYNGAP1* are a recognized cause; detectable by chromosomal microarray. Contiguous-gene deletions can add extra features beyond the core phenotype.

Ontology anchors: gene → HGNC:11497; suggest GO/CL/UBERON terms in §6–§7.

---

## 5. Environmental Information

- **Environmental factors:** none — no toxin, radiation, pollution, or occupational contribution to disease *causation*.
- **Lifestyle factors:** none causal. Diet is relevant only *therapeutically* (ketogenic diet, §12) and as a *seizure trigger* (eating-induced reflex seizures).
- **Infectious agents:** none — not an infectious or post-infectious disease.

This section is genuinely **not applicable** as an etiologic axis; SYNGAP1-DEE is purely genetic.

---

## 6. Mechanism / Pathophysiology

Here's where the biology gets gorgeous. Picture the excitatory synapse's postsynaptic density (PSD) as a crowded loading dock. **SynGAP** is one of the most abundant proteins on that dock — a **Ras/Rap GTPase-activating protein** tethered to the NMDA-receptor complex via PSD-95. Its day job is to keep the **Ras→ERK/MAPK** and **Rap** signaling switches *turned off* until a legitimate calcium signal (through the NMDA receptor + CaMKII) says "go." SynGAP is thus a **brake on synaptic strengthening** ([Frontiers "SYNGAP1: Mind the Gap," PMID:26912996 ✓](https://pubmed.ncbi.nlm.nih.gov/26912996/)).

**The causal chain (upstream → downstream):**

1. **Trigger — SynGAP haploinsufficiency.** ~50% less SynGAP protein at the PSD.
2. **Dysregulated small-GTPase signaling.** Loss of GAP activity → **constitutively elevated Ras-GTP → hyperactive ERK/MAPK**, plus disturbed Rap signaling. The brake is half-off. *(GO:0032312 regulation of ARF/Ras GTPase activity; GO:0007265 Ras signal transduction; GO:0000186 activation of MAPKK activity.)*
3. **Aberrant AMPA-receptor trafficking.** Excess Ras/ERK drives **premature insertion of AMPA receptors** into the postsynaptic membrane, increasing excitatory synaptic strength too early. *(GO:0032281 AMPA glutamate receptor complex; GO:0098976 excitatory chemical synaptic transmission.)*
4. **Precocious dendritic-spine maturation.** Spines "grow up too fast," **shortening the critical window of plasticity** — the developmental period when circuits are supposed to stay malleable ([Clement et al. 2012, Cell 151:709–723 ⚠︎VERIFY PMID:23141539](https://www.sciencedirect.com/science/article/pii/S0092867412012408); [critical-period paper, PMC4326604](https://pmc.ncbi.nlm.nih.gov/articles/PMC4326604/)). *(GO:0060997 dendritic spine morphogenesis; GO:0050803 regulation of synapse structure/activity.)*
5. **Circuit-level E/I imbalance.** "Early hard-wiring" of cortical and thalamocortical circuits → **excitation/inhibition imbalance, abnormal cortical oscillations, and impaired plasticity** → the substrate for both **cognitive impairment** and **generalized seizures** ([synaptic-neoteny study, Neuron 2024](https://www.cell.com/neuron/fulltext/S0896-6273(24)00529-4)).
6. **Clinical manifestation.** ID + generalized epilepsy + autistic/behavioral features.

**This maps cleanly onto your existing `epilepsy_excitation_inhibition_imbalance` module** — the conserved chain "ion-channel/synaptic dysfunction → E/I imbalance → hyperexcitability/hypersynchrony → seizures." SYNGAP1-DEE is a near-textbook **synaptic (rather than ion-channel) conformer** of `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`. Worth a `conforms_to` edge.

**Protein dysfunction:** loss of a PSD scaffold-associated enzyme → downstream signaling deregulation (not aggregation/misfolding). UniProt Q96PV0 (SYNGAP1_HUMAN).

**Cellular processes / cell types:** the disorder is intrinsic to **excitatory glutamatergic cortical/hippocampal pyramidal neurons** (CL:0000598 pyramidal neuron; CL:0000679 glutamatergic neuron; CL:0000617/CL:0000540 neuron), with interneuron-circuit consequences. **Subcellular:** the **postsynaptic density of the dendritic spine** (GO:0014069 postsynaptic density; GO:0043197 dendritic spine).

**Metabolic / immune / fibrosis / oxidative:** none primary — this is not a metabolic, autoimmune, or degenerative disease.

**Molecular profiling / advanced tech:** human **xenotransplanted cortical neuron** and iPSC models show **disrupted "synaptic neoteny"** (the human-specific slow synapse maturation), tying SynGAP loss to accelerated human-neuron maturation ([Neuron 2024](https://www.cell.com/neuron/fulltext/S0896-6273(24)00529-4)). Mouse cortical CRISPR/functional-genomics and re-expression studies underpin the reversibility work (§15). No disease-defining metabolomic/proteomic biomarker panel exists yet.

---

## 7. Anatomical Structures Affected

- **Organ / system:** **central nervous system** (UBERON:0001017), specifically **cerebral cortex** (UBERON:0000956) and **hippocampus** (UBERON:0002421); **thalamocortical** circuitry implicated. Body system: **nervous system** (predominant); secondary GI dysmotility (enteric nervous system) and no primary cardiac/renal/hepatic involvement.
- **Tissue / cell:** **gray-matter neural tissue**; **excitatory glutamatergic pyramidal neurons** (CL:0000598) are the primary affected population; downstream inhibitory-interneuron circuit dysfunction.
- **Subcellular:** **postsynaptic density** (GO:0014069) of **dendritic spines** (GO:0043197) on excitatory synapses (GO:0060076); the NMDA-receptor/PSD-95 signaling complex.
- **Localization / laterality:** **bilateral, diffuse/generalized** cortical involvement (consistent with generalized epilepsy and global ID); brain MRI is **usually normal or nonspecific** — this is a functional/microstructural, not gross-structural, disorder.

---

## 8. Temporal Development

- **Onset:** **congenital/infantile** for the neurodevelopmental axis — hypotonia and developmental delay in the first months to ~2 years, **before** seizures. **Epilepsy onset** median ~2 years (range ~4 months–7 years).
- **Pattern:** **chronic**, largely **static-to-plateauing** developmental course rather than frank neurodegeneration; a notable **plateau/relative regression window at ~2–5 years** ([Kim 2024 ✓](https://pubmed.ncbi.nlm.nih.gov/38563110/)).
- **Epilepsy course:** frequently **drug-resistant** and **evolving** — semiology and EEG change over childhood (occipital→frontal discharge migration; eyelid myoclonia → myoclonic → atonic evolution in ~35%).
- **Remission:** seizures may improve in some by adolescence/adulthood but ID and autism **persist lifelong**; spontaneous remission of the disorder does not occur.
- **Critical period:** the animal data make this the therapeutically pivotal concept — an **embryonic/early-postnatal developmental window** during which circuit assembly is derailed, with implications for the timing of any disease-modifying therapy (§15).

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal dominant**, **HP:0000006**; nearly always **de novo**. **Penetrance essentially complete** for the LoF variants; **expressivity variable** (severity tracks variant position/isoform). No **anticipation** (not a repeat-expansion disorder). **Germline/somatic mosaicism** in a parent is a real, if uncommon, recurrence mechanism → warrants parental testing and counseling. **No founder effects, no consanguinity role, no carrier-frequency concept** (it's not a recessive/carrier disease).

**Epidemiology.** Prevalence figures diverge sharply by source and this is worth flagging in the KB:
- Orphanet lists **<1/1,000,000** as a documented point prevalence — almost certainly an **underestimate** (SYNGAP1 is widely regarded as **under-diagnosed**, [CureSYNGAP1](https://curesyngap1.org/blog/why-are-we-so-sure-that-syngap1-related-intellectual-disability-is-under-diagnosed/)).
- **Yield-based estimates are much higher:** **~1% of epileptic encephalopathy** cohorts and **~0.75% of unexplained ID** cohorts carry pathogenic *SYNGAP1* variants ([GeneReviews NBK537721](https://www.ncbi.nlm.nih.gov/books/NBK537721/); [Vlaskamp 2019 ✓](https://pubmed.ncbi.nlm.nih.gov/30541864/)). Some reviews put the population incidence at **1–4/10,000**, i.e. **~0.5–4% of ID**, making it **one of the more common single-gene causes of ID-with-epilepsy**.
- **Curation guidance:** record the coarse band honestly — the *true* population prevalence is genuinely uncertain; the *diagnostic yield* numbers (~1% of DEE, ~0.75% of ID) are the more defensible, better-sourced claims. In your `Prevalence` schema I'd use `measure_type: POINT_PREVALENCE`, `prevalence_class` for the Orphanet band, but lean on the yield statistics in `notes` with their cohort context.

**Demographics.** **No ethnic predilection**; global distribution (de novo). **Sex ratio ~1:1** (50% male in both the 147- and 57-patient cohorts). **Age distribution:** pediatric-diagnosed, lifelong condition; adult cases increasingly recognized via reanalysis ([adult WES "cold case," PMC10617251](https://pmc.ncbi.nlm.nih.gov/articles/PMC10617251/)).

---

## 10. Diagnostics

**The diagnosis is genetic.** There is no biochemical or imaging test that makes it — those support and exclude.

**Genetic testing (definitive):**
- **First-line:** **broad genomic testing** — **exome (WES)** or **genome (WGS)**, or a **DEE/ID multigene panel** that includes *SYNGAP1*. High-yield in the "developmental delay → later generalized epilepsy" phenotype.
- **Chromosomal microarray (CMA):** catches **6p21.32 microdeletions** that sequencing panels can miss.
- **Single-gene testing / targeted variant analysis:** for family cascade or confirming a specific variant.
- **Parental testing:** to establish de novo status and screen for mosaicism (recurrence risk).
- Karyotype/FISH/mtDNA/repeat-expansion testing: **low yield / not indicated** for the typical presentation.

**Supportive / phenotyping tests:**
- **EEG** (the key functional test): generalized (poly)spike-wave, often with **eyelid-myoclonia-associated discharges**, photosensitivity, eating/eye-closure-triggered discharges; **occipital→frontal** shift with age. EEG is central to characterizing the epilepsy but is **not specific**.
- **Brain MRI:** **usually normal/nonspecific** — its main value is ruling out structural mimics.
- **Developmental / neuropsychological assessment**, **autism evaluation (ADOS/ADI-R)**, sleep evaluation.
- **No validated blood/CSF biomarker** exists.

**Clinical criteria & differential.** No formal consensus criteria; diagnosis rests on genotype + compatible phenotype. **Differential diagnosis** (the "generalized DEE with myoclonic/absence/atonic seizures + ID" neighborhood): **Dravet syndrome (*SCN1A*)**, **Doose/myoclonic-atonic epilepsy**, **Jeavons syndrome (eyelid myoclonia with absences)**, **Lennox-Gastaut syndrome**, **Angelman syndrome (*UBE3A*)**, **STXBP1-, SLC6A1-, GABA-pathway DEEs**, and **KANSL1/other ID-with-epilepsy genes**. Distinguishing feature: **developmental delay clearly preceding seizure onset**, plus the eyelid-myoclonia/eating-triggered semiology.

**Screening.** Not on newborn-screening panels; **no carrier screening** (de novo dominant). Ascertainment is via **diagnostic genomic testing in ID/DEE**, and increasingly via **exome/genome reanalysis** of previously undiagnosed patients — a real-world driver of the "under-diagnosed" story.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** **Life expectancy is generally not markedly shortened**, and it is **not a primarily lethal disorder**; however, like other refractory DEEs it carries an elevated risk of **SUDEP (sudden unexpected death in epilepsy)** and seizure/status-related and aspiration-related morbidity. No robust disease-specific mortality rate is published.
- **Morbidity / function:** **high lifelong disability** — most individuals are non-/minimally verbal, dependent for daily activities, and require lifelong support. Autism, sleep disruption, and behavioral challenges compound the ID.
- **Disease course / complications:** refractory epilepsy, injury from atonic drop attacks, feeding/aspiration issues, constipation, sleep disorder, behavioral crises.
- **Recovery potential:** the ID/autism axis is **stable and permanent** with current care; seizures are **often refractory** but may attenuate over time in some. No spontaneous recovery.
- **Prognostic factors:** **variant position/isoform** and **epilepsy severity/refractoriness** are the main prognostic levers (e.g., 5′/exon-1–4 variants → better language outcomes; refractory epilepsy → worse developmental trajectory). No validated prognostic biomarker beyond genotype.
- **QoL measures:** no SYNGAP1-specific instrument; generic pediatric-NDD and caregiver-burden tools are used in registry/advocacy contexts.

---

## 12. Treatment

**Bottom line: no disease-modifying therapy is approved yet — care is symptomatic — but the precision-medicine pipeline is unusually active** ([Graglia et al. 2025 roadmap, PMID:39807402 ✓](https://pubmed.ncbi.nlm.nih.gov/39807402/)).

**Antiseizure medications (mainstay; MAXO:0000058 pharmacotherapy / MAXO:0000630 pharmacotherapy):**
- **Broad-spectrum ASMs favored** for generalized/myoclonic seizures: **valproate**, **lamotrigine**, **levetiracetam**, **ethosuximide** (for absences), **clobazam**, and **cannabidiol (Epidiolex)** — the latter with reported benefit in SYNGAP1-associated refractory/myoclonic-atonic epilepsy ([CBD in MAE, Epileptic Disorders 2025](https://onlinelibrary.wiley.com/doi/abs/10.1002/epd2.20321)).
- **Caution:** as with other generalized epilepsies, sodium-channel blockers (e.g., carbamazepine/phenytoin) can **worsen** myoclonic/absence seizures.
- **Ketogenic diet** (MAXO:0001056 / dietary intervention MAXO:0000088) — used in refractory cases with anecdotal benefit.

**Supportive / rehabilitative (large share of real-world management):**
- **Speech-language therapy**, **occupational therapy**, **physical therapy** (MAXO:0000011 physical therapy; MAXO:0000020-class rehabilitation), **AAC (augmentative communication)** devices.
- **Behavioral/ASD interventions**, **sleep management** (melatonin), **feeding/GI management**, **genetic counseling** (MAXO:0000079).

**Investigational / disease-modifying pipeline (the exciting part):**
- **Antisense oligonucleotides (ASOs):** the leading modality. **CAMP4 Therapeutics' CMP-SYNGAP-01** — an **intrathecal ASO that upregulates SYNGAP1 expression** (a "regulatory RNA"/upregulation approach rather than knockdown) — **entered GLP toxicology in Oct 2025**, with a **Phase 1/2 first-in-human start targeted for 2H 2026** ([CAMP4 announcement](https://investors.camp4tx.com/news-releases/news-release-details/camp4-therapeutics-initiates-glp-toxicology-studies-cmp-syngap)). Multiple companies + academic groups have **ASO and AAV programs** in pipelines ([roadmap PMID:39807402 ✓](https://pubmed.ncbi.nlm.nih.gov/39807402/)).
- **AAV gene therapy:** preclinical **AAV delivery of full-length SYNGAP1 rescued epileptic and behavioral phenotypes in mice** ([Molecular Therapy 2025](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(25)00759-2)) — proof-of-concept for gene supplementation.
- **Discontinued for the class:** **soticlestat (TAK-935)**, a cholesterol-24-hydroxylase inhibitor trialed across DEEs, was **discontinued by Takeda in 2025** after Phase 3 misses in Dravet/LGS ([Takeda statement](https://www.takeda.com/newsroom/statements/2025/takeda-provides-update-on-soticlestat/)) — it was never SYNGAP1-specific.
- **Other explored approaches:** taurine supplementation and ketogenic diet (anecdotal); ERK/MAPK-pathway modulation is a rational target given the mechanism but not clinically validated.

**Pharmacogenomics / personalized medicine:** the whole *point* of the ASO/AAV work is **genotype-directed dosage restoration**; ASO eligibility is being formally assessed for SYNGAP1 among infantile genetic epilepsies ([medRxiv 2025](https://www.medrxiv.org/content/10.64898/2025.12.02.25341084.full.pdf)).

**Treatment strategy:** individualized ASM selection for generalized/myoclonic semiology + aggressive developmental/behavioral support; enrollment in the **SYNGAP1/Brain Gene Registry** and natural-history studies to be trial-ready ([Brain Gene Registry, PMID:40282364 ✓](https://pubmed.ncbi.nlm.nih.gov/40282364/)).

---

## 13. Prevention

- **Primary prevention:** **not possible** — de novo dominant mutation; no modifiable exposure. Only **reproductive options** apply for a family with an identified proband: **prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** in the rare inherited/mosaic-parent scenario, and **recurrence-risk counseling** (empirically low but non-zero due to possible parental germline mosaicism).
- **Secondary prevention (early detection → early intervention):** the actionable lever. **Early genomic diagnosis** (broad WES/WGS in ID/DEE, plus **exome reanalysis**) enables early developmental therapy and trial-readiness — and, if disease-modifying therapy arrives, the **developmental critical period** makes *early* treatment potentially decisive.
- **Tertiary prevention (complication reduction):** seizure control to limit injury/SUDEP, aspiration/nutrition management, sleep and behavioral support, physical/OT to preserve function.
- **Immunization / public-health / environmental measures:** **not applicable** (not infectious/environmental).
- **Genetic counseling** (MAXO:0000079) is the central preventive-medicine service: de novo status confirmation, mosaicism screening, and family-planning guidance.

---

## 14. Other Species / Natural Disease

- **Taxonomy of the ortholog:** *SYNGAP1* is deeply conserved across vertebrates — human **NCBITaxon:9606**, mouse *Syngap1* (**NCBITaxon:10090**, MGI), rat (**NCBITaxon:10116**), zebrafish (**NCBITaxon:7955**, ZFIN).
- **Naturally occurring disease in animals:** **none catalogued** — there is **no spontaneous companion-animal or livestock SYNGAP1 disease** in OMIA; all animal disease is **engineered** (see §15). So this is genuinely **not applicable** as a "natural disease of other species."
- **Comparative biology / evolutionary conservation:** the **NMDAR–SynGAP–Ras/ERK–AMPAR** synaptic module is highly conserved, which is *why* rodent models translate mechanistically. A striking human-specific twist: **"synaptic neoteny"** (protracted human synapse maturation) is disrupted by SynGAP loss in xenotransplanted human neurons — a conservation-*with-a-human-difference* story ([Neuron 2024](https://www.cell.com/neuron/fulltext/S0896-6273(24)00529-4)).
- **Zoonotic potential / cross-species transmission:** **not applicable** (genetic, non-transmissible).

---

## 15. Model Organisms

The model story is the crown jewel here, because it delivered the field's central hope: **the disorder may be at least partly reversible even after development.**

- **Mouse (*Syngap1*^+/− heterozygous knockout)** — the workhorse (MGI). Recapitulates **cognitive deficits, autistic-like behaviors, and epilepsy/interictal spiking** ([comprehensive behavioral analysis, PMC7292322](https://pmc.ncbi.nlm.nih.gov/articles/PMC7292322/)). Homozygous null is embryonic-lethal — consistent with dosage-critical function.
- **Critical-period / developmental-timing models:** *Syngap1* haploinsufficiency **"damages a postnatal critical period of pyramidal cell structural maturation linked to cortical circuit assembly"** ([PMC4326604](https://pmc.ncbi.nlm.nih.gov/articles/PMC4326604/)). **Conditional/temporal genetic-rescue** experiments show **full protection when the gene is restored in cortical progenitors mid-to-late embryonically, but limited benefit from CNS-wide reversal begun in adulthood** — establishing a developmental window.
- **Adult-reversal models (the therapeutic-optimism papers):** **"Re-expression of SynGAP protein in adulthood improves translatable measures of brain function and behavior"** ([Creson/Rumbaugh et al., eLife 2019](https://elifesciences.org/articles/46752)) — adult restoration improved memory measures and **eliminated sleep-worsened interictal events**. So: development sets the ceiling, but **adult intervention still moves meaningful endpoints** — the biological rationale for ASO/gene therapy in already-diagnosed children and adults.
- **Isoform models:** endogenous **α-splice-form** manipulation shows specific isoforms **promote cognition and seizure protection** ([eLife 2022](https://elifesciences.org/articles/75707)) — relevant to designing expression-restoring therapeutics.
- **Gene-therapy proof-of-concept:** **AAV full-length *SYNGAP1* rescued epileptic and behavioral phenotypes** in the mouse model ([Molecular Therapy 2025](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(25)00759-2)).
- **Human cellular models:** **iPSC-derived neurons, cortical organoids, and xenotransplanted human cortical neurons** — reveal disrupted **synaptic neoteny/maturation** ([Neuron 2024](https://www.cell.com/neuron/fulltext/S0896-6273(24)00529-4)); ideal for `evidence_source: IN_VITRO`. Other systems: rat, zebrafish, and *Drosophila* orthologs exist for pathway work.
- **Model limitations:** mouse heterozygotes **under-model the full human seizure severity** (interictal spikes ± occasional seizures rather than the florid human eyelid-myoclonia/absence syndrome); and the **human-specific neoteny** biology can't be captured in rodent neurons — a genuine `HUMAN_MODEL_MISMATCH` candidate for your KB (evidence exists in models, but translational fidelity of the *seizure* phenotype and the human-maturation timeline is the open question).

---

## Curation notes for the dismech entry

- **Module conformance:** strong `conforms_to: epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` — SYNGAP1-DEE is a clean *synaptic* (non-channel) conformer. The mechanistic chain in §6 gives you the trigger→consequence nodes.
- **`HUMAN_MODEL_MISMATCH` discussion:** the mouse-vs-human seizure-severity gap and the human synaptic-neoteny biology are worth a `kind: HUMAN_MODEL_MISMATCH` discussion, not a generic knowledge gap — evidence *exists* in models, fidelity is the question.
- **Prevalence honesty:** curate the Orphanet <1/1,000,000 band but foreground the **~1% of DEE / ~0.75% of ID** yield statistics with cohort context in `notes`; note explicit under-diagnosis.
- **Genotype–phenotype:** the exon-1–4 vs exon-5–19 language split and the 5′/refractory-epilepsy trade-off are quotable, well-sourced, and belong in `genetic`/subtype notes.
- **⚠︎VERIFY before snippeting:** re-fetch PMIDs I cited from background memory (Clement 2012 Cell ~PMID:23141539; eLife 46752/75707; PMC4326604 — confirm authors/year) with `just fetch-reference` and confirm exact abstract substrings. The ✓-marked PMIDs (19196676, 21237447, 30541864, 38563110, 39807402, 40282364) came straight from the searches and the two fetched abstracts (PMC6340340, PMC12375243) gave verbatim quotes you can lift directly.

**Sources:**
- [Vlaskamp et al. 2019, *Neurology* — SYNGAP1 encephalopathy: a distinctive generalized DEE (PMID:30541864)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6340340/)
- [Wiltrout et al. 2024, *Epilepsia* — Comprehensive phenotypes of SYNGAP1-related disorder (147 patients)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375243/)
- [Kim et al. 2024, *Am J Med Genet A* — genotype/phenotype & longitudinal insights (PMID:38563110)](https://pubmed.ncbi.nlm.nih.gov/38563110/)
- [Hamdan et al. 2009, *NEJM* — Mutations in SYNGAP1 in nonsyndromic MR (PMID:19196676)](https://pubmed.ncbi.nlm.nih.gov/19196676/)
- [Hamdan et al. 2011 — De novo SYNGAP1 mutations in nonsyndromic ID and autism (PMID:21237447)](https://pubmed.ncbi.nlm.nih.gov/21237447/)
- [GeneReviews — SYNGAP1-Related Intellectual Disability (NBK537721)](https://www.ncbi.nlm.nih.gov/books/NBK537721/)
- [Orphanet — SYNGAP1-related DEE (ORPHA:544254)](https://www.orpha.net/en/disease/detail/544254)
- [OMIM #612621 — MRD5](https://www.omim.org/entry/612621)
- [Frontiers — "SYNGAP1: Mind the Gap" (PMID:26912996)](https://pubmed.ncbi.nlm.nih.gov/26912996/)
- [Clement et al. 2012, *Cell* — pathogenic SYNGAP1 mutations & dendritic-spine maturation](https://www.sciencedirect.com/science/article/pii/S0092867412012408)
- [Creson/Rumbaugh et al. 2019, *eLife* — adult re-expression of SynGAP](https://elifesciences.org/articles/46752)
- [Critical-period damage paper, PMC4326604](https://pmc.ncbi.nlm.nih.gov/articles/PMC4326604/)
- [Endogenous Syngap1 α splice forms, *eLife* 2022](https://elifesciences.org/articles/75707)
- [AAV full-length SYNGAP1 rescue, *Molecular Therapy* 2025](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(25)00759-2)
- [SYNGAP1 deficiency disrupts synaptic neoteny, *Neuron* 2024](https://www.cell.com/neuron/fulltext/S0896-6273(24)00529-4)
- [Graglia et al. 2025 — SynGAP Research Fund therapeutics roadmap (PMID:39807402)](https://pubmed.ncbi.nlm.nih.gov/39807402/)
- [SYNGAP1 Syndrome and the Brain Gene Registry, 2025 (PMID:40282364)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12026819/)
- [CAMP4 CMP-SYNGAP-01 GLP toxicology announcement, Oct 2025](https://investors.camp4tx.com/news-releases/news-release-details/camp4-therapeutics-initiates-glp-toxicology-studies-cmp-syngap)
- [Takeda soticlestat (TAK-935) discontinuation, 2025](https://www.takeda.com/newsroom/statements/2025/takeda-provides-update-on-soticlestat/)
- [Comprehensive behavioral analysis of heterozygous Syngap1 KO mice, PMC7292322](https://pmc.ncbi.nlm.nih.gov/articles/PMC7292322/)
- [Hong et al. 2025, *Clinical Genetics* — genotype–phenotype correlations in MRD5](https://onlinelibrary.wiley.com/doi/10.1111/cge.14661)