---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-01T20:49:18.322949'
end_time: '2026-08-01T20:54:03.223690'
duration_seconds: 284.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculofaciocardiodental Syndrome
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 20
  total_cost_usd: 1.7306106
  session_id: 25ddbf03-b4a7-56d4-aa81-2fbd0e31b562
  stop_reason: end_turn
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculofaciocardiodental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculofaciocardiodental Syndrome** covering all of the
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

# Oculofaciocardiodental (OFCD) Syndrome — Comprehensive Research Report

## 1. Disease Information

**Overview.** Oculofaciocardiodental (OFCD) syndrome, also called Microphthalmia, Syndromic 2 (MCOPS2), is an ultra-rare X-linked dominant multiple congenital anomaly syndrome affecting the eyes, face, heart, and teeth. It is caused by loss-of-function variants in **BCOR** (BCL6 corepressor, Xp11.4) and is presumed lethal in hemizygous males, so it is essentially reported only in females (with rare exceptions discussed in §9). The syndrome was clinically delineated well before its molecular cause was identified, and the causal gene was established in 2004 [Ng et al., *Nat Genet* 2004, PMID not directly captured but doi 10.1038/ng1321].

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM | #300166 (MICROPHTHALMIA, SYNDROMIC 2; MCOPS2) |
| Orphanet | ORPHA:2712 |
| MONDO | MONDO:0010261 |
| ICD-10-CM | Q87.8 (Other specified congenital malformation syndromes, not elsewhere classified) — no dedicated OFCD-specific code exists |
| MeSH | Supplementary concept records C537465 / C537735 |
| Gene (causal) | BCOR, HGNC:20893, Xp11.4; allelic disorder: Lenz microphthalmia syndrome (OMIM #309800) |
| MedGen | C1846265 |

**Synonyms:** Oculo-facio-cardio-dental syndrome; OFCD syndrome; Microphthalmia, syndromic 2; MCOPS2; Oculofaciocardiodental syndrome with radiculomegaly.

**Evidence basis:** Information is derived almost entirely from published **individual patient case reports and small case series** (the total literature comprises roughly 20 published cases/families) rather than aggregated registries or large cohort studies, reflecting the extreme rarity of the condition. Molecular mechanism data below come from mouse conditional-knockout models and patient-derived cell (periodontal ligament) studies.

---

## 2. Etiology

**Disease causal factor:** OFCD syndrome is caused by **heterozygous loss-of-function (null) variants in BCOR** in females — nonsense, frameshift, splice-site, and whole/partial gene deletion variants — that eliminate BCOR protein function ("A novel deletion mutation in the BCOR gene is associated with oculo-facio-cardio-dental syndrome," PMID:35130870; PMC8819928). It is a purely monogenic, developmental (non-degenerative) disorder — there is no described environmental, infectious, or multifactorial contribution to primary disease causation.

**Genetic risk factors:**
- The single causal locus is **BCOR** (Xp11.4). Virtually all reported OFCD-causing variants are **protein-truncating** (nonsense, frameshift, canonical splice-site) or **large deletions/duplications** predicted to result in complete loss of function of the encoded BCOR corepressor protein.
- By contrast, **missense** or **hypomorphic splice** BCOR variants in **hemizygous males** cause the phenotypically distinct, milder **Lenz microphthalmia syndrome** (X-linked recessive; OMIM #309800) rather than OFCD — establishing a clear genotype-phenotype/mutation-type correlation across the allelic series ("Oculofaciocardiodental and Lenz microphthalmia syndromes result from distinct classes of mutations in BCOR," Ng et al., *Nat Genet* 2004, doi:10.1038/ng1321; EJHG, doi:10.1038/ejhg200952).
- **De novo occurrence is the norm**; most reported cases arise from a de novo BCOR variant in the proband. Familial (mother-to-daughter) transmission has also been documented.
- **Germline mosaicism** has been demonstrated: two Indian sisters with OFCD syndrome shared an identical BCOR mutation not detectable in parental blood or buccal/saliva DNA, implying parental gonadal (germline) mosaicism (Hilton et al., *Mol Syndromol*, doi:10.1159/000365768).
- **Somatic/gonosomal mosaicism** in affected individuals contributes to variable expressivity (see §9).

**Protective factors:** None identified — there is no documented genetic modifier, environmental exposure, or lifestyle factor known to reduce risk or severity. Because this is a fully penetrant, single-gene, developmental disorder rather than a susceptibility trait, the "protective factor" framework used for complex/multifactorial disease does not straightforwardly apply.

**Gene-environment interactions:** None reported; OFCD is not known to interact with environmental exposures. (Note: BCOR is best known outside this syndrome as a somatically mutated gene in several cancers — clear-cell sarcoma of kidney, AML, retinoblastoma-associated tumors — but that somatic-cancer biology is mechanistically and clinically distinct from germline OFCD and is not itself an environmental risk factor for OFCD.)

---

## 3. Phenotypes

Because OFCD is a congenital, developmentally determined syndrome, essentially all phenotypes are present from birth or early infancy (structural malformations) with a subset of ocular and dental features that evolve/are recognized later in childhood. Below are the principal phenotype categories with suggested HPO terms and reported frequencies (frequencies compiled from case-series review; given only ~20 total published cases, precise percentages should be treated as indicative, not population-representative).

### Ocular (clinical signs) — the most characteristic and earliest-recognized features
- **Congenital cataract** (bilateral, often present from birth) — HP:0000519 (Cataract) / HP:0010786 (congenital cataract)
- **Microphthalmia** — HP:0000568
- **Microcornea** — HP:0000482
- **Secondary/congenital glaucoma** — HP:0000501
- **Ptosis** — HP:0000508
- **Blepharophimosis** — HP:0000581
- **Ankyloblepharon** — HP:0000039
- **Progressive/regressive vision impairment** — HP:0000505

### Facial dysmorphism
- **Long, narrow face** — HP:0000276
- **High nasal bridge** with septate/bifid nasal tip and cartilage separation — HP:0011832 / HP:0000437 (Depressed/high nasal bridge variants)
- **Long philtrum** — HP:0000343
- **Cleft palate** (hard and/or soft) — HP:0000175

### Cardiac
- **Atrial septal defect (ASD)** — HP:0001631
- **Ventricular septal defect (VSD)** — HP:0001629
- **Mitral valve prolapse / "floppy" valves** — HP:0001634

### Dental — the pathognomonic feature of the syndrome
- **Radiculomegaly** (extremely elongated tooth roots, particularly canines, sometimes premolars/incisors) — HP:0006486 (Radiculomegaly); considered by multiple authors the single most consistent and diagnostically distinctive finding
- **Persistent primary (deciduous) teeth** into the second decade — HP:0006335
- **Oligodontia / hypodontia** — HP:0000668 / HP:0000696
- **Hyperdontia (supernumerary teeth)** — HP:0000696 is hypodontia; hyperdontia is HP:0006466

### Skeletal / limb
- **2/3 toe syndactyly, hammertoes** — HP:0004691 / HP:0001765
- **Finger abnormalities** (reported in ~82% of a compiled case series)
- **Radioulnar synostosis** (~13%)

### Neurodevelopmental / other
- **Mild developmental/psychomotor delay** (~10% of cases)
- **Sensorineural or other hearing loss** (~9%)
- Renal and intestinal malformations (rare, isolated reports)
- Infantile hemangiomas have been reported co-occurring with OFCD, creating phenotypic overlap with PHACE syndrome in at least two cases (PMC6949664)

**Onset/severity/course:** All structural features are congenital in origin (present at or before birth), though clinical recognition of cataracts/glaucoma, dental radiculomegaly, and developmental delay may occur progressively through infancy and childhood as these features become clinically apparent (e.g., radiculomegaly is typically identified on dental radiographs in later childhood/adolescence). Severity is markedly **variable between and even within families**, attributed to differential X-inactivation mosaicism (§9). The disease course for structural anomalies is generally **stable** post-repair (surgical correction of cataracts, cardiac defects) rather than progressive, though secondary complications (e.g., glaucoma, amblyopia) can evolve.

**Quality-of-life impact:** Visual impairment from cataracts/microphthalmia/glaucoma, if uncorrected, causes significant developmental and functional impact; dental radiculomegaly complicates orthodontic and endodontic care and can affect occlusion, speech, and nutrition; cardiac septal defects may require surgical correction with associated morbidity. No formal EQ-5D/SF-36/PROMIS-based quality-of-life studies specific to OFCD were identified in the literature — this reflects the rarity of the condition rather than an absence of impact.

---

## 4. Genetic/Molecular Information

**Causal gene:** BCOR (BCL6 corepressor), HGNC:20893, located at Xp11.4; OMIM gene entry *300485. Encodes a component of the non-canonical Polycomb repressive complex 1 (PRC1.1 / ncPRC1.1).

**Variant spectrum in OFCD:**
- Nonsense mutations
- Frameshift (insertion/deletion) mutations, e.g., c.251dupT (p.N87Kfs*6) reported in a prenatally diagnosed case via whole-exome sequencing (PMC8990034); c.3668delC frameshift used in the tooth-root mechanistic study (Frontiers Physiol 2022)
- Canonical splice-site variants
- Partial or whole-gene deletions (e.g., PMC8819928 novel deletion; ClinVar entries document multiple large deletions such as g.(?_39921372)_(39923872_?)del)
- All of these variant classes converge on **complete loss of BCOR protein function**, distinguishing OFCD genetically from the missense/hypomorphic variants that cause Lenz microphthalmia in males.

**Variant classification (ACMG/ClinVar):** The great majority of BCOR variants reported in OFCD are classified **Pathogenic/Likely Pathogenic** in ClinVar under the condition "Oculofaciocardiodental syndrome" (e.g., RCV000011664, RCV000011660, RCV000640952, RCV000811990).

**Allele frequency:** Given the severe, embryonic-lethal-in-males, dominant nature of the disorder, pathogenic BCOR truncating variants are essentially **absent from population databases** (gnomAD) as germline constitutional variants — consistent with strong purifying selection against LOF alleles in males and de novo/rare familial occurrence in females.

**Somatic vs. germline:** OFCD-causing variants are germline (constitutional), typically de novo, occasionally familial or arising from parental germline mosaicism (§2, §9). (Separately, **somatic** BCOR mutations/internal tandem duplications are recurrent drivers in several malignancies — clear cell sarcoma of the kidney, acute myeloid leukemia, retinoblastoma — but this is an unrelated, cancer-specific biology, not part of the germline OFCD disease process; ASH *Blood* review on "BCOR gene alterations in hematologic diseases.")

**Functional consequence:** Loss of function — the truncated/deleted BCOR protein cannot participate in PRC1.1 assembly or transcriptional repression, and hemizygous males with complete BCOR loss die in utero (see §6).

**Modifier genes:** No disease-modifier genes have been formally established; phenotypic variability is attributed primarily to stochastic/skewed X-chromosome inactivation mosaicism rather than to trans-acting modifier loci (§9).

**Epigenetic information:** BCOR is itself part of an epigenetic transcriptional repression complex (PRC1.1), which deposits monoubiquitination on histone H2A (H2AK119ub) via the associated RING1B/RNF2 E3 ligase and KDM2B, silencing target-gene chromatin. Thus the primary molecular pathology of OFCD is itself an **epigenetic corepressor deficiency** rather than a classical structural-protein defect. No disease-specific DNA methylation or ENCODE/Roadmap epigenomic profiling studies specific to OFCD patient tissue were identified.

**Chromosomal abnormalities:** OFCD is caused by intragenic point mutations or small-to-large intragenic/whole-gene deletions of BCOR, not by whole-chromosome aneuploidy or balanced translocation; deletions can be detected by chromosomal microarray/exon-level CNV analysis in addition to sequencing.

---

## 5. Environmental Information

No environmental toxin, radiation, occupational exposure, lifestyle factor (smoking, diet, alcohol), or infectious agent has been implicated in the causation of OFCD syndrome. As a fully penetrant monogenic developmental disorder, environmental factors are not part of its established etiology, and no CTD (Comparative Toxicogenomics Database) gene-chemical interaction records specific to BCOR/OFCD causation were identified in this review.

---

## 6. Mechanism / Pathophysiology

**Molecular function of BCOR / PRC1.1 pathway:**
BCOR is a core component of a non-canonical Polycomb repressive complex, **PRC1.1**, which also contains RING1/RING1B, PCGF3/PCGF5, SKP1, and the H3K36me2/3 demethylase **KDM2B**. KDM2B targets PRC1.1 to unmethylated CpG islands, where RING1B monoubiquitinates histone H2A at lysine 119 (H2AK119ub), establishing facultative heterochromatin and repressing developmental gene-expression programs. BCOR itself acts as a corepressor scaffold, also historically characterized as a corepressor for the transcription factor **BCL6**.

GO terms of relevance:
- GO:0031519 – PcG protein complex
- GO:0035102 – PRC1 complex
- GO:0003714 – transcription corepressor activity
- GO:0031507 – heterochromatin formation

**Causal chain — from gene loss to clinical phenotype (established primarily via conditional mouse models):**

A 2020 study using **tissue-specific conditional Bcor knockout mice** ("OFCD syndrome and extraembryonic defects are revealed by conditional mutation of the Polycomb-group repressive complex 1.1 (PRC1.1) gene BCOR," PMID:32692983; PMC9583620) established that:

1. **Global/hemizygous male loss of Bcor → embryonic lethality.** Male chimeras hemizygous for gene-trapped Bcor null alleles die by embryonic day E9.5, with defects in somite formation, cardiac looping, forebrain fusion, and microcephaly (MGI:1918708). This directly explains the presumed male lethality of complete BCOR loss in humans.
2. **Neural-crest-restricted Bcor loss → craniofacial/palatal defects.** Conditional mutation in neural crest cells produces cleft palate, mandibular shortening, tympanic bone hypoplasia, ectopic salivary glands, and abnormal tongue musculature — with the causal lesion localized to the **mandibular region rather than the palatal shelves themselves**, indicating that palatal clefting in OFCD is a secondary consequence of disrupted mandibular/pharyngeal-arch neural crest development. (Strong Bcor expression is seen in prospective craniofacial tissues, correlating with the craniofacial phenotype; PMC2002546.)
3. **Isl1-lineage (heart field) Bcor loss → congenital heart disease.** Conditional loss in Isl1-expressing cardiac progenitor lineages produces persistent truncus arteriosus, ventricular septal defect, and fetal lethality — mechanistically linking BCOR loss to the ASD/VSD/outflow-tract phenotypes seen in OFCD patients.
4. **Hindlimb lateral-mesoderm Bcor loss → digit/limb defects.** Conditional loss in hindlimb progenitor cells of the lateral plate mesoderm produces 2/3 syndactyly, recapitulating the human digital/toe phenotype.
5. **Extraembryonic-lineage Bcor loss → placental insufficiency.** Loss in extraembryonic tissues causes placental defects and midgestation lethality, an additional non-cell-autonomous contributor to the overall embryonic vulnerability associated with BCOR loss.

Together these tissue-specific studies show that OFCD is best modeled as a **mosaic, tissue-distributed developmental corepressor deficiency**: the severity and combination of organ involvement in any given patient reflects which cell lineages retain a functionally active (wild-type) X chromosome versus which express the mutant BCOR allele, layered on top of these intrinsically lineage-specific developmental requirements for BCOR/PRC1.1 function.

**Dental radiculomegaly — a distinctive human-specific mechanism.** A 2022 study using patient-derived **periodontal ligament (PDL) cells** carrying a BCOR frameshift variant (c.3668delC) elucidated the molecular basis of the syndrome's most pathognomonic feature ("Molecular mechanism of hyperactive tooth root formation in oculo-facio-cardio-dental syndrome," PMC9359619):
- Loss of BCOR corepressor function leads to **failure of BCOR to bind BCL6 at the ZFPM2 promoter**, releasing transcriptional repression of **ZFPM2**, which was found upregulated ~15.5-fold in patient PDL cells.
- ZFPM2 upregulation drives elevated **alkaline phosphatase (ALP)** expression, a marker of odontoblast/cementoblast differentiation, alongside broader activation of tooth-root developmental genes (RUNX2, KLF4, NOTCH3, NOTCH4) — consistent with the "Osx and miRNAs in tooth development" pathway.
- ZFPM2 knockdown selectively normalized ALP expression, supporting a direct **BCOR → BCL6/ZFPM2 → ALP → excess cementum/dentin deposition** causal chain for radiculomegaly.
- Notably, this phenotype is **not observed in conditional Bcor knockout mice**, because rodents are monophyodont with continuously erupting/growing molars (no diphyodont replacement dentition), underscoring that radiculomegaly reflects a **human-specific dental developmental biology** not captured by the mouse model — an important human-model translational caveat.

**Cell types and biological processes implicated (suggested CL/GO terms):**
- Neural crest cells (CL:0000333) — craniofacial/palatal morphogenesis (GO:0060021 palate development)
- Cardiac progenitor cells / Isl1+ second heart field cells — cardiac septation (GO:0003281 ventricular septum development)
- Lateral plate mesoderm limb progenitors — digit morphogenesis (GO:0042733)
- Periodontal ligament fibroblasts, odontoblasts, cementoblasts (CL:0000058 odontoblast; CL:0000452 - relevant PDL lineage cells) — tooth root/cementum formation (GO:0042475 odontogenesis of dentin-containing tooth)
- Lens epithelial cells — cataractogenesis (indirect; specific BCOR-lens mechanism not yet elucidated in the literature reviewed)

**Immune involvement:** Not implicated — OFCD is a pure developmental/structural disorder with no described autoimmune or immunodeficiency component.

**Molecular profiling:** No transcriptomic, proteomic, or single-cell/spatial datasets specific to human OFCD patient tissue (beyond the targeted PDL gene-expression study above) were identified; this remains a gap given the extreme rarity of the condition and scarcity of patient-derived material.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- Eye (UBERON:0000970) — lens (cataract), globe (microphthalmia), cornea (microcornea)
- Craniofacial skeleton and soft tissue (UBERON:0001456 face) — nasal cartilage, palate (UBERON:0001743)
- Heart (UBERON:0000948) — atrial/ventricular septa, mitral valve
- Teeth (UBERON:0001091 tooth) — roots, cementum, periodontal ligament (UBERON:0002263)
- Digits/limbs (UBERON:0002544 digit) — toes, occasionally fingers, radioulnar joint

**Secondary/complication-level involvement:**
- Optic nerve/retina secondary to glaucoma
- Kidney and intestine (rare isolated malformation reports)
- CNS (mild developmental delay in a minority)
- Inner/middle ear (hearing loss in a minority)

**Body systems involved:** Ophthalmologic, craniofacial/skeletal, cardiovascular, dental/stomatognathic, and (in a minority) renal, gastrointestinal, and neurodevelopmental systems.

**Tissue/cell level:** Neural crest-derived craniofacial mesenchyme; second heart field (Isl1+) cardiac progenitors; lateral plate mesoderm-derived limb progenitors; periodontal ligament/odontogenic mesenchymal lineages (fibroblasts, cementoblasts, odontoblasts); lens epithelium.

**Subcellular level:** BCOR/PRC1.1 functions in the **nucleus** (GO:0005654 nucleoplasm), specifically at chromatin (GO:0000785) as part of the Polycomb repressive complex bound to CpG islands.

**Localization/laterality:** Ocular and digital/limb findings are typically **bilateral** (e.g., bilateral cataracts, bilateral 2/3 toe syndactyly), consistent with a systemic mosaic corepressor deficiency rather than a laterality-patterning defect; cardiac septal defects are midline structural anomalies.

---

## 8. Temporal Development

**Onset:** Congenital — the underlying structural malformations (ocular, cardiac, craniofacial, digital) originate during embryonic/fetal development and are present at birth; cases have been diagnosed prenatally by whole-exome sequencing following ultrasound-detected anomalies (PMC8990034). Dental radiculomegaly, while congenital in developmental origin, is typically not clinically/radiographically apparent until later childhood as teeth (particularly permanent canines) form and roots elongate; persistent deciduous teeth are recognized as retained teeth fail to exfoliate on schedule.

**Progression:** The structural anomalies themselves are **non-progressive** (static malformations) once formed; however, several **secondary/functional consequences can evolve over time** — e.g., cataracts can lead to progressive amblyopia if uncorrected, glaucoma can progress and threaten vision, and orthodontic/occlusal problems from radiculomegaly/oligodontia evolve through the mixed and permanent dentition. Cardiac septal defects may require surveillance for spontaneous closure (small ASD/VSD) versus progressive hemodynamic effects requiring surgery.

**Disease course:** Generally **stable, lifelong** condition with fixed structural anomalies managed surgically/medically; not degenerative. No described remission — this is a structural developmental disorder, not an inflammatory or relapsing-remitting condition.

**Critical periods:** Early infancy is a critical window for cataract surgery to prevent amblyopia; childhood/adolescence is critical for orthodontic/endodontic planning given radiculomegaly's impact on tooth extraction/root canal therapy; prenatal genetic counseling is relevant given recurrence risk from parental mosaicism.

---

## 9. Inheritance and Population

**Epidemiology:** OFCD syndrome is **ultra-rare**; the literature to date comprises approximately **20 published cases/families worldwide**, with incidence cited as "less than 1 per million." Prevalence is formally listed as "Unknown" by Orphanet given the small number of cases.

**Inheritance pattern:** **X-linked dominant, with presumed male lethality.** Heterozygous females carrying a BCOR loss-of-function allele manifest OFCD syndrome; hemizygous males with an equivalent null allele are not viable and are presumed to die in utero, consistent with the E9.5 lethality of hemizygous Bcor-null male mouse embryos. Missense/hypomorphic BCOR variants, by contrast, are compatible with male survival and cause the allelic disorder Lenz microphthalmia syndrome (X-linked recessive).

**Penetrance/expressivity:** Full penetrance is generally assumed for pathogenic heterozygous BCOR truncating variants in females, but **expressivity is highly variable** — both between unrelated families and within the same family (e.g., mother-daughter pairs with differing severity) — attributed to **differential (skewed) X-chromosome inactivation mosaicism** across tissues. The proportion of cells in a given tissue expressing the mutant versus wild-type BCOR allele determines the severity of involvement in that organ system.

**Germline mosaicism:** Documented — two affected sisters shared an identical BCOR mutation undetectable in either parent's blood/buccal DNA, indicating parental gonadal mosaicism as the transmission mechanism (Hilton et al., *Mol Syndromol*, doi:10.1159/000365768). This has direct genetic-counseling implications: even with negative parental blood testing, sibling recurrence risk is not zero.

**Somatic mosaicism / surviving males:** Rare surviving males have been reported with **somatic (postzygotic) mosaic** BCOR truncating variants rather than fully hemizygous germline null variants — consistent with the model that complete constitutional loss is embryonic-lethal in males but a mosaic (partial-tissue) loss can be compatible with survival, producing an attenuated/patchy phenotype. A related report describes a female with **biallelic mosaic** BCOR variants causing a severe ocular phenotype (bilateral anterior segment dysgenesis and cataracts) independent of typical X-inactivation-driven variability, suggesting dose-dependent pathogenicity of the mutant gene product (PMC9822961, EJHG doi:10.1038/s41431-022-01195-7).

**Founder effects / consanguinity:** No founder mutations or consanguinity association has been described; virtually all cases are attributable to independent de novo or familial (dominantly transmitted) variants rather than a population-specific founder allele.

**Population demographics:** Cases have been reported across diverse populations (including Japanese, Indian, Italian, Czech, and other cohorts cited above), with no described ethnic or geographic clustering. **Sex ratio:** essentially exclusively female-affected (consistent with the male-lethal model), aside from the rare mosaic male survivors noted above.

---

## 10. Diagnostics

**Clinical diagnostic gestalt:** Diagnosis is suspected clinically based on the combination of congenital cataract/microphthalmia, characteristic long narrow facies with high nasal bridge and cleft nasal tip, congenital heart defect (typically septal), and — the most pathognomonic single finding — **dental radiculomegaly**, and is confirmed by molecular genetic testing of BCOR.

**Laboratory/biomarker tests:** No specific serum biomarker exists; diagnosis is anatomic/radiographic and molecular.

**Imaging:**
- **Panoramic dental radiography (orthopantomogram)** is central to diagnosis, revealing the characteristic elongated tooth roots (radiculomegaly), particularly of canines.
- **Echocardiography** for cardiac septal defects and valve assessment (recommended at diagnosis and for ongoing surveillance).
- Ophthalmologic imaging (slit-lamp exam, ocular ultrasound/biometry) for cataract, microphthalmia, and glaucoma assessment.
- Skeletal radiographs for digit/toe anomalies and radioulnar synostosis as clinically indicated.

**Genetic testing:**
- **Single-gene BCOR sequence analysis** (and deletion/duplication analysis) is the recommended diagnostic test in an individual with suggestive clinical features; commercial single-gene and combined BCOR panels (covering both OFCD and Lenz microphthalmia) are available (e.g., Fulgent Genetics, PreventionGenetics).
- **Next-generation sequencing (NGS)** panels/exome sequencing detect BCOR sequence variants and copy-number variants (deletions/duplications) with reported **>99% analytic sensitivity**.
- **Whole-exome sequencing (WES)** has been used successfully for **prenatal diagnosis** when ultrasound anomalies (e.g., cardiac defect) raise suspicion, identifying novel frameshift variants such as c.251dupT (PMC8990034).
- **Chromosomal microarray** can detect larger BCOR deletions.
- Given documented germline mosaicism, a negative parental blood test does not fully exclude recurrence risk; testing of multiple tissue types (buccal, saliva) may be considered when familial recurrence is suspected without detectable parental variant in blood.

**Differential diagnosis:** Conditions with overlapping features include Lenz microphthalmia syndrome (allelic, X-linked recessive, males, milder), oculodentodigital dysplasia (GJA1-related), Nance-Horan syndrome, and — for cases with co-occurring infantile hemangiomas — PHACE syndrome (phenotypic overlap has been specifically documented; PMC6949664).

**Screening:** No population-based or newborn screening program exists (as expected for an ultra-rare monogenic disorder); genetic counseling and prenatal diagnostic testing are offered to families with a known BCOR variant given the demonstrated risk of germline mosaicism and dominant transmission.

---

## 11. Outcome/Prognosis

**Survival/mortality:** For **affected females**, OFCD syndrome is generally **compatible with normal or near-normal life expectancy**; mortality risk relates chiefly to the severity of associated congenital heart disease if unrepaired, rather than the syndrome itself being a progressive or degenerative lethal condition. For **hemizygous males** with complete (non-mosaic) BCOR loss, the condition is presumed **embryonic/fetal lethal**, and such pregnancies are not expected to result in a liveborn affected male.

**Morbidity/function:** Principal long-term morbidity relates to visual impairment (from cataract/microphthalmia/glaucoma if not adequately treated), dental/occlusal dysfunction from radiculomegaly and oligodontia, and — in a minority — mild developmental delay or hearing loss. No formal disability or quality-of-life registry data specific to OFCD were identified.

**Complications:** Amblyopia secondary to uncorrected cataract; glaucoma-related vision loss; complications from cardiac septal defects if unrepaired (rare, given typically small/moderate defect size); dental complications from radiculomegaly complicating extraction and endodontic treatment (root canal therapy is technically challenging and requires specialized techniques, see §12).

**Prognostic factors:** Severity appears to correlate with the degree/tissue distribution of skewed X-inactivation mosaicism rather than with a specific variant "hot spot" — i.e., the same or similar loss-of-function variant can produce markedly different severity between individuals depending on cellular mosaicism.

---

## 12. Treatment

There is **no disease-modifying or curative treatment** for OFCD syndrome (it is a structural developmental disorder, not an active biochemical/inflammatory process); management is entirely **symptomatic, surgical, and multidisciplinary**, coordinated across ophthalmology, cardiology, dentistry/orthodontics, and clinical genetics.

**Ophthalmologic:**
- **Cataract extraction surgery**, typically performed in infancy/early childhood to prevent amblyopia (NCIT:C15329 Surgical Procedure)
- Ongoing management of glaucoma (medical and/or surgical) (NCIT:C15986 Pharmacotherapy for IOP-lowering agents)
- Vision therapy: corrective lenses, patching for amblyopia/strabismus (NCIT:C15302 Physical Therapy-adjacent behavioral/vision therapy)

**Cardiac:**
- **Regular echocardiographic surveillance** of septal defects and valve function
- Surgical repair of significant ASD/VSD as clinically indicated (NCIT:C15329 Surgical Procedure)

**Dental/orthodontic (a major management focus given radiculomegaly):**
- Specialized **endodontic techniques** adapted for extremely long tooth roots — e.g., the modified Thermafil obturation technique to achieve adequate working length in teeth with radiculomegaly (ScienceDirect, "Endodontic Management in Oculo-Facio-Cardio-Dental Syndrome: A Case Report")
- **Orthodontic treatment** and **orthognathic surgery** (e.g., LeFort I osteotomy, bilateral sagittal split osteotomy) to correct skeletal malocclusion (NCIT:C16186 Orthopedic Surgical Procedure / relevant maxillofacial surgical terms)
- **Occlusal rehabilitation with dental implants** in cases of significant oligodontia (documented in surgical-orthodontic case report, PMID:22449596)

**Skeletal/other supportive care:** Management of syndactyly/hammertoes as functionally indicated; developmental/hearing surveillance and early intervention services for the minority with developmental delay or hearing loss.

**Genetic counseling** (NCIT:C15240 Genetic Counseling): Recommended for families given X-linked dominant inheritance with male lethality, documented germline mosaicism, and variable expressivity; prenatal diagnosis via chorionic villus sampling/amniocentesis or exome sequencing is available when a familial variant is known or fetal anomalies are suggestive.

**Experimental/advanced therapeutics:** No gene therapy, targeted molecular therapy, or clinical trials specific to OFCD syndrome were identified (searches of ClinicalTrials.gov and the broader literature returned no active or completed interventional trials) — consistent with the disorder's status as an ultra-rare structural malformation syndrome rather than a progressive biochemical disease amenable to a single molecular intervention at this time.

**Treatment outcomes:** Outcomes are generally favorable with timely surgical intervention (especially early cataract surgery to preserve vision); no systematic response-rate or adverse-event data exist beyond individual case reports given the rarity of the condition.

---

## 13. Prevention

Because OFCD syndrome results from de novo or dominantly inherited single-gene variants with a well-characterized male-lethal mechanism, **primary prevention** in the population-health sense (risk-factor modification, vaccination) is not applicable — there are no modifiable environmental or lifestyle risk factors.

- **Genetic counseling and prenatal diagnosis** represent the primary prevention/family-planning tools available: once a familial BCOR variant is identified, options include prenatal testing (CVS/amniocentesis or NIPT-guided exome approaches) and, where desired, preimplantation genetic diagnosis (PGD/PGT) for future pregnancies, particularly relevant given documented germline mosaicism that can elevate recurrence risk even when the variant is undetectable in parental blood.
- **Secondary prevention** in affected individuals centers on **early detection and treatment of ocular complications** (cataract surgery in infancy, glaucoma surveillance) to prevent irreversible amblyopia/vision loss, and echocardiographic surveillance to catch clinically significant cardiac defects early.
- **Tertiary prevention** involves ongoing multidisciplinary dental/orthodontic management to minimize functional and occlusal complications from radiculomegaly and oligodontia over the life course.
- No immunization, population screening program, or public-health/environmental intervention applies to this disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease analogous to human OFCD syndrome has been described in the literature reviewed (no OMIA entries or veterinary case series identified). BCOR is a highly conserved gene across vertebrates (orthologs present in mouse, and by extension likely in other mammals), and the mouse ortholog (**Bcor**, MGI:1918708, Chr X) has been the primary basis for experimental modeling (§15) rather than a naturally arising animal disease.

---

## 15. Model Organisms

**Mouse (*Mus musculus*) — the primary and only well-developed model system:**

- **Gene:** *Bcor* (MGI:1918708), murine ortholog of human BCOR, X-linked.
- **Global/hemizygous male loss-of-function models:** Male chimeras hemizygous for gene-trapped *Bcor* null alleles die by embryonic day E9.5, with anomalies in somite formation, cardiac looping, forebrain fusion, and microcephaly; other gene-trapped alleles produce patterning/embryo-turning defects or abnormal gastrulation (MGI allele records, e.g., MGI:5925306). This recapitulates the presumed male embryonic lethality seen in human OFCD pedigrees.
- **Conditional (tissue-specific) knockout models** ("OFCD syndrome and extraembryonic defects are revealed by conditional mutation of the Polycomb-group repressive complex 1.1 (PRC1.1) gene BCOR," *Development*, PMID:32692983) — the key functional-genomics resource for this disease — used Cre-lox conditional alleles to dissect lineage-specific requirements for Bcor:
  - **Neural crest-specific** loss → cleft palate (via mandibular, not palatal-shelf, defects), micrognathia, tympanic bone hypoplasia, ectopic salivary glands, abnormal tongue musculature — modeling human craniofacial/palatal phenotypes.
  - **Isl1-lineage (second heart field)-specific** loss → persistent truncus arteriosus, VSD, fetal lethality — modeling human congenital heart disease.
  - **Hindlimb lateral mesoderm-specific** loss → 2/3 syndactyly — modeling human digital anomalies.
  - **Extraembryonic lineage-specific** loss → placental defects, midgestation lethality — an additional non-cell-autonomous contributor without a direct postnatal human phenotype correlate (relevant to miscarriage risk).
- **Model limitations (explicit human-model mismatch):** The mouse model does **not** recapitulate dental radiculomegaly, because mice are monophyodont with continuously growing (rootless-analogous) molars, lacking the human diphyodont replacement-dentition biology in which excess root/cementum deposition manifests (Frontiers Physiol 2022, PMC9359619). This is an important, explicitly documented **translational gap** between the mouse model and the human dental phenotype — mechanistic work on radiculomegaly instead relied on **human patient-derived periodontal ligament (PDL) cells** in vitro, not the mouse model.
- **Expression studies:** *Bcor* expression has been characterized broadly across mouse embryonic development, with strong expression noted in prospective craniofacial tissues correlating with the craniofacial phenotypes ("Characterization of Bcor Expression in Mouse Development," PMC2002546).

**Cellular/in vitro models:** Patient-derived periodontal ligament (PDL) cells (heterogeneous population including osteoblasts, osteoclasts, fibroblasts, epithelial rests of Malassez, odontoblasts, cementoblasts, macrophages, and undifferentiated mesenchymal cells) have been used as a human-relevant surrogate system to dissect the BCOR–BCL6–ZFPM2–ALP mechanistic axis underlying radiculomegaly (§6).

**Resources:** MGI (Mouse Genome Informatics) *Bcor* gene page (MGI:1918708) and associated targeted/gene-trap allele records provide the catalog of available mouse alleles; no zebrafish, *Drosophila*, or *C. elegans* BCOR-ortholog disease models specific to OFCD phenotypes were identified in this review.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0010261; OMIM:300166 |
| Gene | HGNC:20893 (BCOR) |
| Phenotypes (HP) | HP:0000519/HP:0010786 (cataract/congenital cataract), HP:0000568 (microphthalmia), HP:0000501 (glaucoma), HP:0000508 (ptosis), HP:0000276 (long face), HP:0000343 (long philtrum), HP:0000175 (cleft palate), HP:0001631 (ASD), HP:0001629 (VSD), HP:0001634 (mitral valve prolapse), HP:0006486 (radiculomegaly), HP:0006335 (persistent primary teeth), HP:0000668 (oligodontia), HP:0004691/HP:0001765 (syndactyly/hammertoe) |
| Biological process (GO) | GO:0031507 (heterochromatin formation), GO:0060021 (palate development), GO:0003281 (ventricular septum development), GO:0042733 (embryonic digit morphogenesis), GO:0042475 (odontogenesis of dentin-containing tooth) |
| Cellular component (GO) | GO:0035102 (PRC1 complex), GO:0000785 (chromatin) |
| Cell types (CL) | Neural crest cell, cardiac second heart field progenitor, periodontal ligament fibroblast, odontoblast, cementoblast |
| Anatomy (UBERON) | UBERON:0000970 (eye), UBERON:0001743 (palate), UBERON:0000948 (heart), UBERON:0001091 (tooth), UBERON:0002263 (periodontal ligament), UBERON:0002544 (digit) |
| Treatment (NCIT) | NCIT:C15329 (Surgical Procedure — cataract/cardiac repair), NCIT:C16186 (Orthopedic/orthognathic surgical procedure), NCIT:C15240 (Genetic Counseling) |

---

Sources:
- [A novel deletion mutation in the BCOR gene is associated with oculo-facio-cardio-dental syndrome: a case report — BMC Pediatrics](https://link.springer.com/article/10.1186/s12887-022-03148-x) / [PMC8819928](https://pmc.ncbi.nlm.nih.gov/articles/PMC8819928/) / [PubMed 35130870](https://pubmed.ncbi.nlm.nih.gov/35130870/)
- [Case Report: Prenatal Diagnosis of a Novel Variant c.251dupT (p.N87Kfs*6) in BCOR Resulting in Oculofaciocardiodental Syndrome Using Whole-Exome Sequencing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8990034/)
- [Two Cases of Oculofaciocardiodental (OFCD) Syndrome due to X-Linked BCOR Mutations Presenting with Infantile Hemangiomas: Phenotypic Overlap with PHACE Syndrome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6949664/)
- [Congenital cataracts in females caused by BCOR mutations; report of six further families](https://www.sciencedirect.com/science/article/abs/pii/S176972121830911X)
- [OFCD syndrome and extraembryonic defects are revealed by conditional mutation of the Polycomb-group repressive complex 1.1 (PRC1.1) gene BCOR — PMC9583620](https://pmc.ncbi.nlm.nih.gov/articles/PMC9583620/) / [PubMed 32692983](https://pubmed.ncbi.nlm.nih.gov/32692983/)
- [Molecular mechanism of hyperactive tooth root formation in oculo-facio-cardio-dental syndrome — Frontiers in Physiology](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.946282/full)
- [Oculofaciocardiodental syndrome caused by a novel BCOR variant — Human Genome Variation](https://www.nature.com/articles/s41439-023-00244-x) / [PMC10261115](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10261115/)
- [Radiculomegaly as a key clinical feature in oculo-facio-cardio-dental (OFCD) syndrome — Cardiology in the Young](https://www.cambridge.org/core/journals/cardiology-in-the-young/article/abs/radiculomegaly-as-a-key-clinical-feature-in-oculofaciocardiodental-ofcd-syndrome-a-case-report-with-a-novel-truncating-variant-in-bcor-gene/B81F80A499A0553D6978B01589D3D2FF)
- [OMIM #300166 — MICROPHTHALMIA, SYNDROMIC 2 (MCOPS2)](https://omim.org/entry/300166)
- [Oculofaciocardiodental syndrome — Choroby Rzadkie (Orphanet-linked disease card, ORPHA:2712)](https://chorobyrzadkie.gov.pl/en/disease_card/2712)
- [BCOR gene alterations in hematologic diseases — Blood](https://ashpublications.org/blood/article/138/24/2455/475904/BCOR-gene-alterations-in-hematologic-diseases)
- [Oculofaciocardiodental syndrome: novel BCOR mutations and expression in dental cells — Journal of Human Genetics](https://www.nature.com/articles/jhg201424)
- [Endodontic Management in Oculo-Facio-Cardio-Dental Syndrome: A Case Report](https://www.sciencedirect.com/science/article/abs/pii/S0099239911000082)
- [Patient with oculo-facio-cardio-dental syndrome treated with surgical orthodontics — PubMed](https://pubmed.ncbi.nlm.nih.gov/22449596/)
- [Oculo-Facio-Cardio-Dental Syndrome: A Case Report about a Rare Pathological Condition — PMC6466113](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6466113/)
- [A rare genotype of biallelic mosaic variants in BCOR gene causing a bilateral ocular anterior segment dysgenesis and cataracts — European Journal of Human Genetics](https://www.nature.com/articles/s41431-022-01195-7) / [PMC9822961](https://pmc.ncbi.nlm.nih.gov/articles/PMC9822961/)
- [Evidence of Germline Mosaicism for a Novel BCOR Mutation in Two Indian Sisters with Oculo-Facio-Cardio-Dental Syndrome — Molecular Syndromology](https://karger.com/Article/FullText/365768)
- [Oculofaciocardiodental and Lenz microphthalmia syndromes result from distinct classes of mutations in BCOR — Nature Genetics](https://www.nature.com/articles/ng1321) / [PubMed 15004558](https://pubmed.ncbi.nlm.nih.gov/15004558/)
- [Novel mutations in BCOR in three patients with oculo-facio-cardio-dental syndrome, but none in Lenz microphthalmia syndrome — European Journal of Human Genetics](https://www.nature.com/articles/5201391)
- [BCOR analysis in patients with OFCD and Lenz microphthalmia syndromes, mental retardation with ocular anomalies, and cardiac laterality defects — European Journal of Human Genetics](https://www.nature.com/articles/ejhg200952)
- [Characterization of Bcor Expression in Mouse Development — PMC2002546](https://pmc.ncbi.nlm.nih.gov/articles/PMC2002546/)
- [Bcor MGI Mouse Gene Detail — MGI:1918708](https://www.informatics.jax.org/marker/MGI:1918708)
- [oculofaciocardiodental syndrome — MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/oculofaciocardiodental-syndrome)
- [Oculofaciocardiodental syndrome — Wikipedia](https://en.wikipedia.org/wiki/Oculofaciocardiodental_syndrome)
- [ICD-10 Q87.8 — Other specified congenital malformation syndromes affecting multiple systems](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q80-Q89/Q87-)