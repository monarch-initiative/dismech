---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T18:26:20.903663'
end_time: '2026-07-31T18:44:52.713823'
duration_seconds: 1111.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Claes-Jensen Type X-Linked Intellectual Disability
  mondo_id: ''
  category: Genetic
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
  - claude-opus-5[1m]
  web_search_requests: 2
  num_turns: 69
  total_cost_usd: 5.289843000000001
  session_id: e56d6e6d-6f76-458c-a2fc-f8e9c4de86f1
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Claes-Jensen Type X-Linked Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Claes-Jensen Type X-Linked Intellectual Disability** covering all of the
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

I have a comprehensive evidence base. Writing the report now.

# Comprehensive Research Report
# Claes–Jensen Type X‑Linked Intellectual Disability (MRXSCJ)

**Prepared:** 2026‑07‑31 · **Target for:** dismech KB entry `kb/disorders/Claes-Jensen_Type_X-Linked_Intellectual_Disability.yaml`

---

## ⚠️ Curation Preamble — Read Before Using This Report

**1. Named Entity Confusion (NEC) preflight — PASSED.** This disease sits in two high‑NEC‑risk classes (eponymic XLID syndrome; member of a numbered `MRXS`/`MRXSCJ` series). Identity was cross‑anchored on four independent sources before any content was gathered:

| Anchor | Value | Source |
|---|---|---|
| MONDO | `MONDO:0010355` "syndromic X-linked intellectual disability Claes-Jensen type" | EBI OLS4 API (MONDO) |
| OMIM xref | `OMIM:300534` (MRXSCJ) | OLS4 MONDO xrefs; MedGen 335139; HPO/JAX annotation API |
| Causal gene | **KDM5C** (Xp11.22), `hgnc:11114`, `NCBIGene:8242` | HPO/JAX annotation API; ClinGen; MedGen |
| Orphanet | `ORPHA:85279` "KDM5C-related syndromic X-linked intellectual disability" | OLS4 (ORDO); MedGen |

All four agree on gene = KDM5C. No mismatch. Other xrefs: `DOID:0060809`, `UMLS:C1845243`, `MedGen:335139`, `GARD:0016744`.

**2. Snippet-verification caveat — MANDATORY.** Abstracts in this report were retrieved via the NCBI E‑utilities `efetch` endpoint but were passed through a summarizing model, which imposes a ~125‑character quote ceiling. The quoted strings below are **candidate snippets, not verified snippets.** Before any of them is committed as a dismech `evidence.snippet`, run:

```bash
just fetch-reference PMID:XXXXXXXX
just validate-references kb/disorders/Claes-Jensen_Type_X-Linked_Intellectual_Disability.yaml
```

Likewise, every non‑HPO ontology ID suggested here (GO, CL, UBERON, CHEBI, NCIT) is a **candidate** and must pass `just validate-terms`. HPO terms in §3 are exceptions — they were pulled directly from the authoritative HPO/JAX annotation API for `OMIM:300534` and carry real annotation frequencies.

**3. Environment note.** The MCP `pubmed` and `ols-mcp` servers and local `runoak` were not permission‑granted in this non‑interactive run; all data came from direct API fetches (NCBI E‑utilities, EBI OLS4 REST, HPO/JAX API, ClinGen, UniProt REST, MGI, PMC). Section 9 prevalence is consequently thinner than ideal — Orphanet's epidemiology table (API 401 / site bot‑walled) could not be read and should be filled in from the local `ORPHA_85279` cache via `just structured-rebuild-orphanet --id 85279`.

---

## 1. Disease Information

### Overview

Claes–Jensen type syndromic X‑linked intellectual disability (MRXSCJ) is a rare X‑linked chromatinopathy caused by loss‑of‑function variants in **KDM5C** (Xp11.22), encoding the histone H3 lysine‑4 di‑/tri‑methyl (H3K4me2/me3) demethylase JARID1C/SMCX. It is one of the more frequently mutated single genes in X‑linked intellectual disability (XLID).

The core clinical picture in hemizygous males is intellectual disability (usually moderate–severe) with **short stature, microcephaly, hyperreflexia/spasticity, seizures, maxillary hypoplasia, and aggressive or disinhibited behaviour**. Heterozygous females — historically dismissed as "carriers" — are now recognised to be affected far more often than the "X‑linked recessive" label implies, though more mildly.

Orphanet's definition (ORDO:85279):

> "A rare multiple congenital anomalies/dysmorphic syndrome characterized by mild to severe intellectual deficit associated with variable clinical manifestations including spasticity, cryptorchidism, maxillary hypoplasia, alopecia areata, epilepsy, short stature, impaired speech, and behavioral problems."

### Key Identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0010355` |
| **OMIM** | `300534` (MRXSCJ); gene `314690` (KDM5C) |
| **Orphanet** | `ORPHA:85279` |
| **Disease Ontology** | `DOID:0060809` |
| **UMLS / MedGen** | `C1845243` / `335139` |
| **GARD** | `0016744` |
| **Gene** | KDM5C — `hgnc:11114`, `NCBIGene:8242`, `Ensembl:ENSG00000126012`, `UniProt:P41229` |
| **ICD‑10** | No specific code; coded under **F79** (unspecified intellectual disabilities) or **Q87.8**; ICD‑11 ≈ **LD90.Y / 6A00.Z** (no dedicated rubric) |
| **MeSH** | No dedicated descriptor; indexed under *Mental Retardation, X-Linked* / *Intellectual Disability* |

### Synonyms and Alternative Names

From OLS4 (MONDO) and MedGen:
- Intellectual developmental disorder, X‑linked syndromic, Claes‑Jensen type
- **MRXSCJ**, MRXSJ
- Intellectual developmental disorder, X‑linked, syndromic **16** (MRXS16)
- KDM5C‑related syndromic X‑linked intellectual disability (Orphanet preferred)
- **Claes‑Jensen syndrome (CJS)** — used widely in recent literature
- **KDM5C‑NDD** (KDM5C neurodevelopmental disorder) — the emerging, sex‑neutral, non‑eponymic term preferred by the 2026 RARE‑X cohort (PMID:41537560)
- Historic/discouraged: "Mental retardation, X‑linked, syndromic, Claes‑Jensen type"; "…JARID1C‑related"; XLMR with short stature and hyperreflexia

> **Nomenclature recommendation for the KB entry:** keep `MONDO:0010355` as `disease_term`, but consider `KDM5C-Related Neurodevelopmental Disorder` in the description as the modern label, since the eponym encodes an outdated male‑only, recessive framing that the female data (§3, §9) refute.

### Data Provenance Character

Information is **aggregated disease‑level** (OMIM, Orphanet, MONDO, HPO annotations, ClinGen) layered over **individual‑patient case series**. There is no EHR‑derived cohort. The two largest patient‑level aggregations are:
- **PMID:41537560** (Terry et al., *Hum Mol Genet* 2026) — the **RARE‑X KDM5C Data Collection Program**, a *patient‑contributed registry* (caregiver survey), 31 new individuals + literature meta‑analysis to **269 individuals / 130 families / 122 unique variants**. This is the closest thing to a natural‑history dataset and is patient‑reported, not clinician‑abstracted.
- **PMID:39835750** (Ghasemi et al., *Mol Genet Genomic Med* 2025) — systematic literature review of **175 previously reported cases** + 1 novel variant.

---

## 2. Etiology

### Disease Causal Factors

**Monogenic, genetic, fully penetrant in males.** MRXSCJ is caused by germline loss‑of‑function variants in *KDM5C*. There is no infectious, environmental, or multifactorial component to disease causation. ClinGen's Intellectual Disability and Autism GCEP classified the KDM5C ↔ X‑linked syndromic intellectual disability relationship as **Definitive** (2018‑09‑19), inheritance X‑linked.

The causal chain is: *KDM5C* LoF → reduced/absent H3K4me2/me3 demethylase activity (± loss of non‑enzymatic scaffolding) → failure to restrain H3K4 trimethylation at CpG‑island promoters and enhancers → derepression of non‑neuronal, germline and cryptic transcriptional programs plus mistimed WNT signalling during corticogenesis → abnormal neuronal differentiation, dendritic arborisation and spine maturation → intellectual disability, seizures, behavioural phenotype.

### Risk Factors

**Genetic (causal, not "susceptibility"):**
- Hemizygosity for a pathogenic *KDM5C* variant in a 46,XY individual → essentially complete penetrance for ID (98% of males in meta‑analysis, PMID:41537560).
- Heterozygosity in a 46,XX individual → **incomplete, variable penetrance** (56% with ID in meta‑analysis; 4/19 completely asymptomatic in Carmignac et al., PMID:32279304).
- **Being male** is the single largest risk factor for severe expression. This is not merely dosage: *KDM5C* **escapes X‑inactivation**, so females normally express KDM5C from both X chromosomes and carry a higher baseline dose (Agulnik et al., PMID:7951230; Bonefas & Iwase, PMID:36831303 — "KDM5C escapes X-inactivation, thereby presenting at a higher level in females").
- **Maternal carrier status** (~10% of RARE‑X probands maternally inherited; historically the dominant mode in multiplex families).
- **De novo occurrence** — >50% of the RARE‑X cohort; paternal inheritance rare (~1%).
- **Domain location of the variant** is a severity/phenotype modifier: "Patients with mutated variants in the catalytic domain were more likely to experience seizures" (PMID:39835750).

**Environmental:** No established environmental risk factors. Advanced paternal age is a generic risk for de novo point mutation but has not been specifically demonstrated for *KDM5C*.

### Protective Factors

- **Favourably skewed X‑chromosome inactivation** in heterozygous females is the classic candidate protective mechanism — but the evidence is inconsistent. Shen et al. (PMID:36536324) documented a symptomatic female with a de novo nonsense variant and explicitly "no significant skewed X-inactivation," and Carmignac et al. found asymptomatic and symptomatic females without a clean XCI correlate. Because *KDM5C* escapes XCI, XCI skewing is an incomplete explanatory model — this is a genuine open question worth curating as a `KNOWLEDGE_GAP` discussion.
- **Residual enzymatic activity.** Ghasemi et al. propose that "Missense mutations in catalytic domains may retain partial enzymatic activity, potentially producing milder phenotypes than nonsense mutations" (PMID:39835750). The R1115H variant is the extreme case — normal catalytic activity and stability, yet still pathogenic via a non‑enzymatic route (PMID:29670509).
- **KMT2A dosage reduction — experimental, model‑organism only.** Vallianatos et al. showed genetic epistasis: "Double mutation of Kmt2a and Kdm5c clearly reversed dendritic morphology, key behavioral traits" (PMID:32483278). This is a *mouse* result; it is a therapeutic hypothesis, not a human protective factor.
- No dietary, lifestyle, or nutritional protective factor is described.

### Gene–Environment Interactions

Not established for MRXSCJ. Two leads worth flagging as hypotheses:
1. **Illness as a decompensation trigger.** Shaheen et al. (PMID:40346491) report developmental regression with loss of ambulation "following acute viral illness at 22 months." A single case — insufficient to assert a G×E interaction, but a candidate for a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` note.
2. **Immune/interferon axis.** Liao et al. (PMID:41743791) found KDM5C‑mutant zebrafish have "disrupted antiviral and interferon-related signaling," raising the possibility that infectious exposure interacts with the KDM5C lesion. Zebrafish only; unreplicated in humans.
3. **Upstream regulatory interaction with ARX** is gene–gene, not gene–environment: "KDM5C, a gene known to be mutated in XLID-affected children and involved in chromatin remodeling, is directly regulated by ARX" (Poeta et al., PMID:23246292). ARX polyalanine expansions are hypomorphic for KDM5C transactivation — a shared regulatory path to ID+epilepsy.

---

## 3. Phenotypes

### 3.1 Authoritative HPO Annotations (HPO/JAX API, `OMIM:300534`)

These are the **canonical, real** HPO annotations with real observed fractions. `n/m` = affected/assessed. Use these fractions to justify any `frequency:` enum you assign (per `docs/frequency-evidence-guidelines.md`) — but note that most fractions come from small early cohorts and are superseded for common features by the 2025–2026 cohorts in §3.2.

**Neurological / cognitive**

| HPO ID | Term | Annotated frequency |
|---|---|---|
| HP:0001249 | Intellectual disability | **25/26** |
| HP:0010864 | Severe intellectual disability | 8/8 |
| HP:0001263 | Global developmental delay | 3/3 |
| HP:0000750 | Delayed speech and language development | 3/3 |
| HP:0001270 | Motor delay | 3/3 |
| HP:0001250 | Seizure | 8/35 |
| HP:0032792 | Tonic seizure | 1/3 |
| HP:0001347 | Hyperreflexia | 3/6 |
| HP:0002395 | Lower limb hyperreflexia | — |
| HP:0001257 | Spasticity | 7/20 |
| HP:0007020 | Progressive spastic paraplegia | — |
| HP:0003487 | Babinski sign | — |
| HP:0006895 | Lower limb hypertonia | — |
| HP:0000297 | Facial hypotonia | — |
| HP:0002362 | Shuffling gait | — |
| HP:0008944 | Distal lower limb amyotrophy | — |
| HP:0007021 | Pain insensitivity | 2/20 |

**Behavioural**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0000718 | Aggressive behavior | 13/38 |
| HP:0000752 | Hyperactivity | 3/3 |
| HP:0000711 | Restlessness | — |
| HP:0000744 | Low frustration tolerance | — |

**Growth**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0004322 | Short stature | **13/18** |
| HP:0001508 | Failure to thrive | 3/3 |
| HP:0004325 | Decreased body weight | 3/3 |

**Craniofacial**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0000252 | Microcephaly | 7/20 |
| HP:0000256 | Macrocephaly | 2/20 |
| HP:0000327 | Hypoplasia of the maxilla | 7/23 |
| HP:0000218 | High palate | 6/12 |
| HP:0000699 | Diastema | 6/22 |
| HP:0000303 | Mandibular prognathia | 2/20 |
| HP:0000347 | Micrognathia | 1/20 |
| HP:0000221 | Furrowed tongue | 2/2 |
| HP:0000426 | Prominent nasal bridge | 2/6 |
| HP:0000319 | Smooth philtrum | 1/20 |
| HP:0000219 | Thin upper lip vermilion | 1/20 |
| HP:0000350 | Small forehead | 1/20 |
| HP:0000574 | Thick eyebrow | 1/6 |
| HP:0000582 | Upslanted palpebral fissure | 1/20 |
| HP:0000400 | Macrotia | 2/2 |
| HP:0000411 | Protruding ear | 3/6 |

**Ophthalmological**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0000486 | Strabismus | **11/29** |
| HP:0000540 | Hypermetropia | 3/20 |
| HP:0000545 | Myopia | 1/20 |
| HP:0000490 | Deeply set eye | 1/20 |

**Genitourinary**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0008734 | Decreased testicular size | 3/29 |
| HP:0000028 | Cryptorchidism | 2/20 |
| HP:0000054 | Micropenis | 1/20 |

**Skeletal / limb**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0001773 | Short foot | 3/3 |
| HP:0001176 | Large hands | 2/2 |
| HP:0002967 | Cubitus valgus | 2/2 |
| HP:0000767 | Pectus excavatum | 2/2 |
| HP:0001156 | Brachydactyly | — |
| HP:0009882 | Short distal phalanx of finger | — |
| HP:0001762 | Talipes equinovarus | — |
| HP:0008124 | Talipes calcaneovarus | — |
| HP:0001371 | Flexion contracture | 1/6 |

**Other systems**

| HPO ID | Term | Frequency |
|---|---|---|
| HP:0002205 | Recurrent respiratory infections | 3/3 |
| HP:0002788 | Recurrent upper respiratory tract infections | 3/3 |
| HP:0002232 | Patchy alopecia | 1/20 |
| HP:0001081 | Cholelithiasis | 2/20 |

**Onset / inheritance annotations:** `HP:0011463` Childhood onset (3/3); `HP:0001419` X‑linked recessive inheritance.

### 3.2 Modern Cohort Frequencies (supersede HPO fractions for common features)

**Ghasemi et al. 2025 (PMID:39835750) — 175 literature cases, sex‑stratified:**

| Feature | Males (n≈101) | Females (n≈53) |
|---|---|---|
| Intellectual disability | **96%** | **79%** |
| Speech / language impairment | 91% | 70% |
| Behavioural problems | 88% | 60% |
| Facial dysmorphism | 84% | 71% |
| Short stature | 75% | 50% |
| Seizures / epilepsy | **64%** | **19%** |

**Terry et al. 2026 RARE‑X (PMID:41537560) — 31 new (19 M / 12 F) + meta‑analysis to 269 individuals (153 M / 112 F / 4 unspecified):**

Meta‑analysis:
- Intellectual disability: **82% overall** — 98% of males, 56% of females
- ID severity: males predominantly **severe (70%)**; females predominantly **mild (56%)**
- Seizures: **35% overall** — 47% of males, 18% of females
> "47% of males having (or had) seizures, and 18% females having (or had) seizures"

RARE‑X new cohort (caregiver‑reported, therefore higher ascertainment of "soft" features):
- Brain/nervous system involvement 100%; communication challenges 93%
- Seizures 48% (M 42%, F 56%); first seizure age 1–10 y, **median 2 y**
- Growth issues 78%; **short stature 75%** of growth respondents
- Behavioural concerns 78%; short attention span 88%, impulsivity 88%, **anxiety 71%**, **ASD 65%**
- Vision/eye problems 74%; **abnormal eye movement (strabismus/nystagmus) 91%**
- Digestive issues 74%; **constipation 83%**

> ⚠️ **Discrepancy to record in the KB, not smooth over.** Female seizure frequency is 18–19% in the two literature meta‑analyses but **56%** in the RARE‑X new female cohort. Male seizure frequency is 47% (RARE‑X meta) vs 64% (Ghasemi). These are ascertainment artefacts running in opposite directions: registry self‑enrolment enriches for symptomatic females; historical XLMR‑family literature enriches for severely affected males. Curate the *range* with both citations, or omit `frequency:` per the frequency‑evidence SOP.

### 3.3 Phenotype Characteristics

**Age of onset:** Congenital/neonatal in the sense that the lesion is germline; **clinically recognised in infancy to early childhood**. HPO annotates `HP:0011463` childhood onset. Developmental delay is typically noticed in the first 1–3 years (walking ~12 months but first words at ~3 years in the Liao proband, PMID:41743791). Seizure onset median 2 years (range 1–10 y). Prenatal‑onset short stature is documented (PMID:40125771).

**Severity:** Highly variable. Males skew severe (70% severe ID); females skew mild (56% mild). The full range spans **severe ID with progressive spastic paraplegia** (the original Claes family) to a documented case with **no intellectual disability at all** — Murati et al. describe "An 8-year-old boy with prenatal-onset short stature, ophthalmological abnormalities" carrying a "KDM5C variant typically linked to Claes-Jensen syndrome" but without ID (PMID:40125771).

**Progression:** The cognitive deficit is **static/non‑degenerative** — a neurodevelopmental, not neurodegenerative, disorder. However, several elements *are* progressive:
- Spastic paraplegia: "severe mental retardation, slowly progressive spastic paraplegia, facial hypotonia, and maxillary hypoplasia" (Claes et al. 2000, PMID:10982473)
- Seizures: episodic, may emerge in mid‑childhood after an initially seizure‑free period
- Behavioural difficulties: often intensify around adolescence
- One report of **regression** post‑viral illness with loss of ambulation (PMID:40346491) — isolated, needs replication

**Quality‑of‑life impact (per phenotype):**
| Domain | Impact |
|---|---|
| Intellectual disability + communication (93%) | Dominant driver of dependency; lifelong support needs; most affected males non‑ or minimally verbal in the severe range |
| Seizures (35–48%) | Injury risk, medication burden, driving/independence restriction, caregiver vigilance |
| Behaviour: aggression, impulsivity (88%), anxiety (71%) | Frequently the leading caregiver stressor; drives placement decisions and psychotropic prescribing |
| Spasticity / gait | Mobility loss, contractures, orthopaedic surgery, wheelchair dependency in the paraplegic subset |
| Short stature (50–78%) | Cosmetic/psychosocial; endocrine work‑up burden |
| Vision (74%; abnormal eye movement 91%) | Amblyopia risk if untreated; a **highly actionable, under‑recognised** domain (PMID:40125771) |
| GI/constipation (83%) | Chronic discomfort, feeding difficulty, contributes to behavioural escalation |

**No disease‑specific QoL instrument** (EQ‑5D/SF‑36/PROMIS) has been applied to this cohort. This is a genuine gap.

---

## 4. Genetic / Molecular Information

### Causal Gene

**KDM5C** — lysine demethylase 5C. Aliases: **JARID1C, SMCX, XE169, DXS1272E**.
- Locus: **Xp11.22** · `hgnc:11114` · `NCBIGene:8242` · OMIM `314690` · `Ensembl:ENSG00000126012` · `UniProt:P41229`
- Reference transcript: **NM_004187.5**
- Protein: 1,560 aa; EC 1.14.11.67

**Protein architecture (UniProt P41229):**

| Domain | Residues | Role |
|---|---|---|
| **JmjN** | 14–55 | Structural; stabilises JmjC fold |
| **ARID** | 79–169 | DNA binding (AT‑rich interaction domain) |
| **PHD‑type 1 zinc finger** | 326–372 | Reads unmodified/H3K9me3 histone tails |
| **JmjC (catalytic)** | 468–634 | Fe(II)/2‑oxoglutarate–dependent demethylase active site |
| **C5HC2 zinc finger** | 707–759 | Required for catalysis (completes the split JmjC) |
| **PHD‑type 2 zinc finger** | 1187–1248 | Reads H3K4me3 — product/substrate recognition |

Note the **"PLU‑1"/Tower** region is used in the clinical literature to describe the long linker between C5HC2 and PHD2 (PMID:41743791, PMID:39835750). Cofactor: **Fe²⁺** (one ion per subunit, catalytic). Localisation: **nucleus**. Tissue specificity: ubiquitous, **highest in brain and skeletal muscle** — directly consistent with the neurological + growth/muscle phenotype.

Enzymatic specificity: demethylates **H3K4me3 → me2 → me1**, not to unmethylated product, and does *not* act on H3K9/K27/K36/K79 or H4K20.
> "SMCX (JARID1C), which encodes a JmjC-domain protein, reversed H3K4me3 to di- and mono- but not unmethylated products" — Iwase et al., *Cell* 2007 (PMID:17320160)

### Pathogenic Variants

**Variant spectrum (RARE‑X meta‑analysis, 122 unique variants across 130 families; PMID:41537560):**

| Class | Proportion |
|---|---|
| Missense | ~50% |
| Nonsense | 23% |
| Frameshift | 18% |
| Splice | 5% |
| Other (microdeletion, intronic) | 3% |

Concordant with Ghasemi et al. (PMID:39835750; 80 unique variants): missense 41 (51%), nonsense 27 (34%), del/dup 6 (8%), splice 6 (8%).

**Missense variant distribution by domain** (PMID:41537560): **JmjC 36%**, interdomain 33%, ARID 11%, C5HC2 9%, PLU‑1/Tower 5%, PHD2 3%, JmjN 3%. The catalytic JmjC domain is the missense hotspot — and catalytic‑domain variants are enriched for seizures (PMID:39835750).

**Landmark variants:**

| Variant (protein) | Type | Functional consequence | Source |
|---|---|---|---|
| p.Asp87Gly (D87G) | Missense, ARID | **No** effect on activity or localisation; minimal effect on ARID stability/DNA binding | UniProt; PMID:16541399; PMID:26580603 |
| p.Ala77Thr (A77T) | Missense, ARID | Minimal effect on ARID stability/DNA binding | PMID:18697827; PMID:26580603 |
| p.Ala388Pro | Missense | Impairs enzymatic activity; reduces H3K9me3 binding | UniProt |
| p.Asp402Tyr | Missense, JmjC | Decreased enzymatic activity | UniProt |
| p.Ser451Arg (S451R) | Missense | Conserved residue; segregates with ID | PMID:16538222 |
| p.Pro480Leu | Missense, JmjC | Reduced enzymatic activity in patient fibroblasts | UniProt |
| p.Cys640Tyr | Missense | De novo | UniProt |
| p.Phe642Leu | Missense, JmjC | Impairs enzymatic activity | UniProt; PMID:16541399 |
| p.Leu731Phe | Missense, C5HC2 | Impairs enzymatic activity | UniProt |
| p.Arg750Trp / p.Tyr751Cys | Missense, C5HC2 | Y751C impairs activity | UniProt; PMID:16541399 |
| p.Arg332* | Nonsense | Truncating | PMID:16541399 |
| p.Cys724* (c.2172C>A) | Nonsense | Truncating | PMID:24583395 |
| p.Gln902* (c.2704C>T, ex19) | Nonsense, Tower/SPECL2 | **Likely pathogenic (ACMG)**; ClinVar SCV004034082 | PMID:39835750 |
| p.Arg929* (c.2785C>T) | Nonsense | Triggers NMD: mRNA down but protein paradoxically **up**, with altered subcellular localisation | PMID:39948613 |
| p.Arg943* (c.2827C>T) | Nonsense | De novo; regression phenotype | PMID:40346491 |
| p.Val1075Tyrfs*2 (c.3223delG) | Frameshift | Complete loss of KDM5C protein | PMID:25666439 |
| p.Ser1178* (c.3533C>A) | Nonsense | **De novo in a female**; no skewed XCI | PMID:36536324 |
| p.Glu1283* (c.3847G>T) | Nonsense | **De novo in a 27‑y‑old female**; moderate ID | PMID:36553533 |
| p.Arg1115His (R1115H) | Missense | **Normal** activity and stability, yet pathogenic — non‑enzymatic mechanism | PMID:29670509 |
| p.Met1_Glu165del | Translation‑initiation | N‑terminally truncated, unstable, no detectable activity | PMID:25666439 |
| c.3019del | Frameshift, PLU‑1 | Impairs transcription, expression, stability; zebrafish phenotype | PMID:41743791 |
| c.782‑2A>T | Splice acceptor (ARID–PHD1 linker) | Aberrant splicing → PTC in exon 7 → ~375 aa truncated protein | PMID:41743791 |
| c.633G>C (p.Arg211Arg) | Synonymous | Predicted to create an exonic splicing enhancer; co‑segregates — **VUS** | PMID:24583395 |

**Variant classification and population frequency:**
- **ClinVar:** 528 KDM5C records classified Pathogenic or Likely Pathogenic (E‑utilities count, July 2026).
- **gnomAD constraint (via ClinGen):** **pLI = 1**, **LOEUF = 0.17** — extreme intolerance to loss of function, among the most constrained genes in the genome. Pathogenic variants are absent or vanishingly rare in gnomAD; there is no meaningful population allele frequency.
- **ClinGen Dosage Sensitivity (2023‑07‑27):** **Haploinsufficiency score 3 — Sufficient Evidence**; Triplosensitivity 0 — No Evidence. Haploinsufficiency (not gain‑of‑function or triplosensitivity) is the established mechanism.
- **Origin:** **Germline** only for MRXSCJ. (Somatic *KDM5C* mutation is a well‑known driver in **clear cell renal cell carcinoma** — PMID:39955388, PMID:37293154 — but that is a distinct, unrelated disease context and must not be conflated with MRXSCJ.)

**Functional consequence class — LOSS OF FUNCTION**, achieved by at least four distinct routes:
1. **Transcript loss / NMD** — "expression studies revealed the almost complete absence of the mutated JARID1C transcript" (PMID:15586325)
2. **Protein destabilisation** — missense variants that "compromise stability and enzymatic activity" (PMID:25666439)
3. **Direct catalytic impairment** — "Several XLMR-patient point mutations reduced SMCX demethylase activity" (PMID:17320160)
4. **Non‑enzymatic / scaffolding loss** — R1115H: "The KDM5C-R1115H substitution does not have an impact on enzymatic activity," yet fails to suppress targets → "KDM5C may have non-enzymatic roles in gene regulation" (PMID:29670509). Reinforced in *Drosophila*: "KDM5 operates in conjunction with local chromatin contexts to employ demethylase-dependent and independent mechanisms" (PMID:41340160).

Route 4 is mechanistically important for the KB: **it means "loss of demethylase activity" alone is an incomplete pathophysiology node.** Model the enzymatic and non‑enzymatic arms separately.

### Modifier Genes

- **KMT2A** — the opposing H3K4 methyltransferase (Wiedemann‑Steiner syndrome gene). Mouse double mutants show mutual suppression: "shared reduced dendritic spines and increased aggression" in single mutants, reversed in doubles (PMID:32483278). The strongest candidate genetic modifier and the leading therapeutic hypothesis.
- **KDM1A (LSD1)** — cooperative, not opposing: double forebrain‑specific KO produces "stronger ectopic expression of non-neuronal genes in hippocampal neurons and thousands of de novo H3K4me3-enriched regions" and "more severe behavioral impairments than the single ifKOs" (PMID:40864554). A candidate severity modifier.
- **ARX** — *upstream* regulator, not a modifier per se: ARX polyalanine expansions reduce KDM5C transactivation, and "Kdm5c mRNA diminution led to a severe decrease in the KDM5C content during in vitro neuronal differentiation" (PMID:23246292).
- **KDM5D** (Y‑linked paralogue) — a *theoretical* male‑specific partial buffer, but KDM5D is expressed in a restricted manner and does not rescue; in fact its Y‑linkage is part of why males lack the female two‑copy advantage. KDM5C and KDM5D have demonstrably non‑equivalent consequences (PMID:39955388, ccRCC context).

### Epigenetic Information

This disease **is** an epigenetic disorder, and it also **produces** a secondary, measurable epigenetic signature.

**Primary epigenetic lesion:** failure to remove H3K4me3/me2 at CpG‑island promoters. Iwase et al. found "94% of Kdm5c-bound promoters contain a CpG island, representing significant enrichment" (P < 1×10⁻²⁶), with the effect concentrated on lowly expressed genes: "Low-expressed Kdm5c-target genes showed most noticeable increase in expression (~7% increase, P = 1.4 × 10⁻⁸) and H3K4me3 (~12% increase, P < 2.2 × 10⁻¹⁶)". Crucially, "global levels of H3K4me1, me2 or me3 are comparable in WT and Kdm5c-KO neurons" — **the defect is locus‑specific fine‑tuning, not a bulk chromatin collapse.** This is the single most important mechanistic nuance to encode.

**Secondary DNA‑methylation episignature:** Schenkel et al. defined a peripheral‑blood epi‑signature comprising **1,769 individual CpGs and 9 genomic regions** in 7 male patients vs 56 controls, with 6 healthy female carriers showing intermediate changes (PMID:29456765). See §10 for diagnostic performance. Separately, Grafodatskaya/Chénier‑era work reported **multilocus loss of DNA methylation** in KDM5C‑mutant individuals (PMID:23356856), and a monozygotic‑twin methylation study exists (PMID:31419599).

**Downstream chromatin consequences:** patient fibroblasts show "local changes in chromatin conformation and gene expression" (PMID:25666439).

### Chromosomal Abnormalities

MRXSCJ is predominantly a **sequence‑level** disorder. However:
- **Microdeletions** involving *KDM5C* are within the ~3% "other" variant class (PMID:41537560) and one pathogenic hemizygous deletion was found by NGS gene‑dosage analysis in an XLID cohort (PMID:25649377).
- ClinGen HI score 3 means an Xp11.22 CNV encompassing *KDM5C* is interpretable as causative in a male.
- Larger contiguous Xp11.22 deletions may also involve neighbouring XLID genes (e.g. *IQSEC2*, *SMC1A* region) — expect a blended phenotype; check CMA breakpoints.
- No recurrent translocation, inversion, or aneuploidy association.

---

## 5. Environmental Information

**Not applicable as a causal category.** MRXSCJ is a fully monogenic germline disorder.

- **Environmental factors / toxins / radiation / occupational exposure:** none implicated. No CTD‑curated chemical–disease association specific to MRXSCJ.
- **Lifestyle factors:** none causal. Relevant only as downstream management targets (nutrition for failure‑to‑thrive; activity for spasticity; sleep hygiene).
- **Infectious agents:** none causal. Two peripheral observations, both weak and non‑causal: (a) one case of regression after acute viral illness (PMID:40346491); (b) recurrent respiratory/URT infections are annotated phenotypes (HP:0002205, HP:0002788, both 3/3 in a small series) — likely secondary to hypotonia/aspiration rather than a primary immunodeficiency. The zebrafish interferon/TLR finding (PMID:41743791) is a *transcriptomic* dysregulation of antiviral pathways, not evidence of infectious causation.

---

## 6. Mechanism / Pathophysiology

### 6.1 The Causal Chain (upstream → downstream)

```
[MOLECULAR] KDM5C loss-of-function variant (LoF / destabilised / catalytically dead / scaffold-dead)
      │
      ├─► Reduced H3K4me3/me2 demethylase activity at CpG-island promoters + enhancers
      │        (locus-specific, NOT global — bulk H3K4me levels are normal)
      │
      └─► Loss of non-enzymatic scaffolding (REST/HDAC1-2/G9a complex; R1115H arm)
                 │
[MOLECULAR/CELLULAR]  ▼
   Failure of transcriptional fine-tuning:
      • Derepression of REST target neuronal genes at NRSE elements (SCN2A, SYN1)
      • Spurious transcription: germline genes, non-neuronal genes, cryptic promoters
      • Failure to fine-tune activity-regulated enhancers
      • Mistimed canonical WNT signalling output
                 │
[CELLULAR]       ▼
   • Premature/mistimed primary → intermediate progenitor transition; altered neurogenesis timing
   • Reduced ribosome biogenesis and translation (Drosophila arm)
   • Loss of neuronal identity maintenance (adult genome surveillance failure)
                 │
[TISSUE]         ▼
   • Reduced dendritic arborisation (basolateral amygdala pyramidal neurons)
   • Reduced dendritic spine density (~45% of WT in BLA; 9% reduction in motor cortex)
   • Immature, thin (non-mushroom) spine morphology
   • Increased CA1 pyramidal neuron intrinsic excitability; altered ion channel expression
                 │
[ORGANISM]       ▼
   Intellectual disability · seizures · aggression/anxiety/ASD · impaired social behaviour
   · memory deficits · short stature · spasticity
```

### 6.2 Molecular Pathways

**(a) H3K4 methylation writer–eraser balance (the core axis).**
KDM5C is the eraser; KMT2A/MLL1 is the writer. The disorder is a **stoichiometry disease** of this pair. Suggested GO: `GO:0032453` (histone H3K4 demethylase activity — *verify label*), `GO:0034720`/`GO:0140939` (histone H3K4 demethylation — **label changed in recent GO releases; must verify with OAK**), `GO:0006338` chromatin remodeling, `GO:0005506` iron ion binding.

**(b) REST/NRSF neuronal gene silencing.**
> "SMCX and REST co-occupy the neuron-restrictive silencing elements" · "loss of SMCX activity impairs REST-mediated neuronal gene regulation" (Tahiliani et al., *Nature* 2007, PMID:17468742)

SMCX assembles with **HDAC1/HDAC2**, the H3K9 methyltransferase **G9a (EHMT2)**, and **REST** at NRSE elements in promoters of *SCN2A* and *SYN1*. RNAi depletion derepresses these targets with increased H3K4me3. **Note the direct line from this to the seizure phenotype:** *SCN2A* is itself a major epilepsy gene. Candidate GO: `GO:0016575` histone deacetylation, `GO:0045892` negative regulation of DNA-templated transcription.

**(c) Canonical WNT signalling — the 2024 *Nature* mechanism, and the most therapeutically actionable.**
Karwacki‑Neisius et al. (PMID:38383780) established that "KDM5C is identified as a safeguard to ensure that neurodevelopment occurs at an appropriate timescale," acting by modulating WNT output during a defined developmental window to time the primary→intermediate progenitor transition. Critically, the deficit is **pharmacologically reversible within that window**: transient WNT inhibition "rescue[s] the transcriptomic and chromatin landscapes in patient-derived cells," and "WNT inhibition during this developmental period also rescues behavioural changes of Kdm5c knockout mice." The window matters — "only a transient alteration" is required, "WNT functioning in a transient nature to affect long-lasting cognitive function." Candidate GO: `GO:0060070` canonical Wnt signaling pathway; `GO:0021895` cerebral cortex neuron differentiation.

**(d) Ribosome biogenesis / translation (invertebrate arm).**
Zamurrad et al. (PMID:29490272) found in *kdm5^A512P* flies "a striking downregulation of genes required for ribosomal assembly and function" with reduced translation, and "kdm5^A512P flies also showed impaired learning and/or memory." They argue "the primary defect of the KDM5A512P mutation is a loss of histone demethylase activity." **Not yet demonstrated in mammals** — flag as `MODEL_ORGANISM` and a candidate `HUMAN_MODEL_MISMATCH`.

**(e) Interferon / Toll‑like receptor innate‑immune signalling (emerging, zebrafish only).**
Liao et al. (PMID:41743791): both novel variants produced overwhelmingly *upregulated* DEGs (355/363 and 320/326 up) enriched for "antiviral and interferon-related signaling," with *TLR3, NFKB1, IFNB1, IRF7, SAT1a, SAT1b* all up. The TLR inhibitor **CU‑CPT 4a** partially rescued morphology and restored spontaneous swimming. Candidate GO: `GO:0034138` toll-like receptor 3 signaling pathway, `GO:0060337` type I interferon-mediated signaling pathway. **Zebrafish only; unreplicated; do not present as established human mechanism.**

**(f) ARX → KDM5C transcriptional axis (upstream).**
ARX directly binds a conserved noncoding element to activate *KDM5C*; polyalanine‑expanded ARX is hypomorphic. This links two XLID+epilepsy genes into one path (PMID:23246292).

### 6.3 Cellular Processes

- **Neuronal differentiation and identity maintenance.** Scandaglia et al.: "Kdm5c plays a critical role as a repressor responsible for the developmental silencing of germline genes" and, in the adult, "preventing the incorrect activation of non-neuronal and cryptic promoters in adult neurons" (PMID:28978483). This is a **two‑phase** role — developmental silencing plus lifelong genome surveillance — and both phases should be separate pathophysiology nodes.
- **Enhancer fine‑tuning during activity‑dependent plasticity** — "fine-tuning activity-regulated enhancers during neuronal maturation" (PMID:28978483).
- **Dendritogenesis and spine maturation.** Candidate GO: `GO:0016358` dendrite development, `GO:0060998` regulation of dendritic spine development.
- **Neuronal excitability.** Martín‑González et al. found "altered hippocampal expression of ion channels" and increased CA1 pyramidal excitability in KDM1A/KDM5C double KO (PMID:40864554) — a direct cellular substrate for seizures.
- **Cell‑autonomous neuronal requirement.** The RARE‑X *Drosophila* work is decisive: "Reducing the expression of its single Kdm5 gene in neurons, but not glia, led to spontaneous and stimulus-induced seizures" (PMID:41537560). Glia are dispensable for the seizure phenotype.
- **Chromatin‑context dependence.** "altered gene expression in both alleles correlates with preexisting chromatin signatures" (PMID:41340160) — KDM5C's effect is conditional on the local chromatin state, not uniform.

### 6.4 Protein Dysfunction

Four mechanistically distinct failure modes (detailed in §4): transcript loss/NMD, protein destabilisation, catalytic inactivation, and scaffold/recruitment failure with intact catalysis. A fifth, unusual mode: the R929X allele shows "The mRNA levels of the mutant gene were down-regulated, while the protein level" was up, with "Altering the subcellular localization of the protein" (PMID:39948613) — i.e. a truncated protein that escapes to the wrong compartment. No amyloid/aggregation mechanism. No dominant‑negative mechanism has been demonstrated; ClinGen's HI‑3 / TS‑0 assignment supports pure haploinsufficiency.

### 6.5 Metabolic Changes

No primary metabolic derangement; MRXSCJ is not an inborn error of metabolism. Biochemical work‑up in the original Belgian family was normal: "Biochemical investigations, neuroimaging and neuropathology were normal" (PMID:9377804). The only metabolic dimension is the enzyme's own cofactor dependence — **Fe²⁺ and 2‑oxoglutarate** (candidate CHEBI: `CHEBI:29033` iron(2+), `CHEBI:16810` 2-oxoglutarate — *verify*). Endocrine abnormalities are more frequent in affected females ("Endocrine disorders were more frequent in females", PMID:32279304) but are unexplained and not mechanistically linked.

### 6.6 Immune System Involvement

No autoimmunity, no immunodeficiency established. Two threads: recurrent respiratory infections as an annotated phenotype (likely secondary), and the zebrafish interferon/TLR overactivation (§6.2e) — "suggesting aberrant immune activation" (PMID:41743791). Treat as an **emerging hypothesis**, `MODEL_ORGANISM` evidence only.

### 6.7 Tissue Damage Mechanisms

**There is no tissue destruction.** No oxidative stress, ischaemia, fibrosis, necrosis, or inflammation‑driven damage. Adult Kdm5c‑KO mice show "no gross abnormalities in the cytoarchitecture of the adult Kdm5c-KO cerebral cortex, hippocampus, or amygdala" (PMID:26804915). The pathology is **structural‑microscopic and functional** — dendritic/spine hypoplasia and transcriptional miswiring, not lesional. The one progressive element (spastic paraplegia) implies a corticospinal‑tract dysfunction of unclear substrate; human neuropathology was normal (PMID:9377804).

> **Curation implication:** do **not** conform this entry to a degeneration/fibrosis/injury module. If a module fits at all, it is developmental/chromatin, and the relevant near‑neighbour is the chromatinopathy class rather than any existing dismech module. Consider proposing a `chromatin_h3k4_writer_eraser_imbalance` module — KDM5C/KMT2A/KDM1A/KMT2D form a genuinely conserved, recurrent writer–eraser axis across Claes‑Jensen, Wiedemann‑Steiner, Kabuki and KDM1A‑related NDD.

### 6.8 Epigenetic Changes

Covered in §4 (primary H3K4me3 dysregulation; secondary DNA‑methylation episignature; multilocus methylation loss).

### 6.9 Molecular Profiling

**Transcriptomics:**
- *Mouse (Iwase 2016, PMID:26804915):* "larger number of up-regulated genes than down-regulated genes is consistent with the enzymatic activity of Kdm5c, which removes the active chromatin mark H3K4me2/3." **Brain‑region‑specific** effects — "Synaptic pathways such as 'Glutamate Neurotransmitter Release Cycle' and 'Nicotinic acetylcholine receptors' are down-regulated in the KO amygdala but not in the frontal cortex." A class of genes was "down-regulated in KO amygdala but unchanged in KO frontal cortex… highly relevant for neuronal differentiation, neuron-projection development, and synapses."
- *Mouse, sex‑stratified (Bonefas & Iwase 2023, PMID:36831303):* "gene expression and behavioral abnormalities are readily detectable in Kdm5c-heterozygous female mice."
- *Zebrafish (PMID:41743791):* 363 DEGs (355↑/8↓) for c.3019del; 326 DEGs (320↑/6↓) for c.782‑2A>T — strongly derepression‑biased, matching the eraser‑loss prediction.
- *Human patient‑derived cells (PMID:38383780):* WNT‑inhibitor treatment rescued transcriptomic and chromatin landscapes.
- *Drosophila (PMID:29490272):* ribosomal assembly gene downregulation.

**Epigenomics:** ChIP‑seq for KDM5C occupancy and H3K4me3 (PMID:26804915, PMID:28978483, PMID:40864554, PMID:41340160); genome‑wide DNA methylation array (PMID:29456765, PMID:23356856).

**Proteomics / metabolomics / lipidomics:** **No dedicated studies.** Genuine gap.

**Single‑cell / spatial transcriptomics:** **No published single‑cell or spatial dataset specific to MRXSCJ.** Given the strong brain‑region‑ and cell‑type‑specificity of the mouse phenotype (amygdala ≫ cortex), single‑cell profiling is the highest‑value missing experiment. Record as a `KNOWLEDGE_GAP` with a `proposed_experiments` entry.

**Functional genomics screens:** *KDM5C* appears in a genome‑wide screen for 2‑cell‑like state regulators (PMID:37488355) — developmental biology context, not MRXSCJ.

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary:** **Brain** (`UBERON:0000955`) — the overwhelmingly dominant target. Within it:
- Cerebral cortex (`UBERON:0000956`) — frontal/motor cortex spine density reduction
- Hippocampal formation (`UBERON:0002421`) — ectopic non‑neuronal gene expression, CA1 hyperexcitability
- **Amygdala, specifically the basolateral amygdala** — the most severely affected structure in the mouse (dendritic length ↓, spine density ~45% of WT). Candidate UBERON for BLA: `UBERON:0002873` — **verify with OAK**
- Forebrain (`UBERON:0001890`) — the conditional‑KO target region
- Corticospinal tract — implied by progressive spastic paraplegia; no direct imaging/pathology evidence

**Secondary / other systems:**
| System | Involvement | UBERON candidate |
|---|---|---|
| Musculoskeletal / growth axis | Short stature, brachydactyly, cubitus valgus, pectus excavatum, contractures | `UBERON:0002204` musculoskeletal system |
| Craniofacial skeleton | Maxillary hypoplasia, micrognathia/prognathia, high palate | `UBERON:0002397` maxilla |
| Visual system | Strabismus, refractive error, abnormal eye movement (91%) | `UBERON:0000970` eye |
| Reproductive | Cryptorchidism, small testes, micropenis | `UBERON:0000473` testis |
| GI | Constipation (83%), cholelithiasis | `UBERON:0001155` colon; `UBERON:0002110` gallbladder |
| Respiratory | Recurrent infections (likely secondary) | `UBERON:0001004` respiratory system |
| Integumentary | Patchy alopecia / alopecia areata | `UBERON:0002097` skin of body |
| Skeletal muscle | High KDM5C expression (UniProt); no described myopathy | `UBERON:0001134` skeletal muscle tissue |

### Tissue and Cell Level

**Nervous tissue** is the affected tissue type. Cell populations, with candidate CL terms (all require OAK verification):

| Cell type | Evidence | CL candidate |
|---|---|---|
| Neuron (generic) | Cell‑autonomous requirement — neurons not glia (PMID:41537560) | `CL:0000540` |
| Pyramidal neuron (BLA, CA1) | Dendritic/spine defects; hyperexcitability (PMID:26804915, PMID:40864554) | `CL:0000598` |
| Glutamatergic neuron | Glutamate release-cycle genes downregulated (PMID:26804915) | `CL:0000679` |
| Hippocampal neuron | Ectopic non‑neuronal gene expression (PMID:40864554) | `CL:0002608` |
| Neural progenitor / intermediate progenitor | Mistimed primary→intermediate transition (PMID:38383780) | `CL:0011020` (neural progenitor) — **verify** |
| Glia / astrocyte | **Explicitly NOT required** for the seizure phenotype (PMID:41537560) | `CL:0000127` (negative finding) |
| Dermal fibroblast | Patient cells used for functional assay — an assay substrate, not a disease site (PMID:25666439) | `CL:0000057` |
| Chondrocyte | Impaired cartilage development in zebrafish (PMID:41743791) — model organism only | `CL:0000138` |

### Subcellular Level

- **Nucleus** (`GO:0005634`) — KDM5C's exclusive localisation (UniProt). Mislocalisation is itself pathogenic for the R929X allele (PMID:39948613).
- **Chromatin / nucleosome** (`GO:0000785`) — the substrate. Specifically **CpG‑island promoters** and **activity‑regulated enhancers**.
- **Dendritic spine** (`GO:0043197`) — the principal affected structure.
- **Synapse** (`GO:0045202`) — downstream.
No mitochondrial, ER, lysosomal, or peroxisomal involvement.

### Localization and Lateralization

Brain involvement is **bilateral and symmetric**. Microcephaly is generalised. Spastic paraplegia is bilateral and lower‑limb predominant (`HP:0006895` lower limb hypertonia, `HP:0002395` lower limb hyperreflexia) — a **length‑dependent corticospinal pattern**. Strabismus may be unilateral or alternating. Cryptorchidism may be unilateral or bilateral. Alopecia is patchy/focal (`HP:0002232`). One neuroimaging finding: "faint hyperintensities in posterior periventricular white matter suggesting dysmyelination" (PMID:40346491) — single case, bilateral posterior periventricular.

---

## 8. Temporal Development

### Onset

- **Biological onset:** prenatal — WNT‑dependent progenitor mistiming occurs during **corticogenesis**, in utero (PMID:38383780). Prenatal‑onset short stature is documented (PMID:40125771).
- **Clinical onset:** infancy to early childhood. HPO annotates `HP:0011463` childhood onset (3/3).
- **Onset pattern: insidious / chronic.** Not acute. Presents as failure to attain milestones rather than loss of them.
- **Typical presentation sequence:** hypotonia and feeding/growth concerns in infancy → gross‑motor delay (walking ~12 mo or later) → **marked expressive language delay** (first words often ~3 y) → behavioural difficulties in preschool/school years → seizures (median 2 y, range 1–10 y) → spasticity/gait deterioration in some, from mid‑childhood.

### Progression

**Stages** — no formal staging system exists. A pragmatic natural‑history framing:

| Stage | Age | Features |
|---|---|---|
| Infancy | 0–2 y | Hypotonia, feeding difficulty, failure to thrive, growth deceleration, early seizures in some |
| Early childhood | 2–6 y | Global developmental delay declared; severe expressive language delay; ID becomes measurable; strabismus; seizure onset peak |
| School age | 6–12 y | Behavioural phase — aggression, impulsivity, hyperactivity, anxiety; ASD diagnosis; emerging hyperreflexia/spasticity |
| Adolescence/adult | >12 y | Static cognitive plateau; behavioural challenges often peak; progressive spastic paraplegia and contractures in the affected subset; adult dependency established |

**Progression rate:** The **cognitive** deficit is **static** — it does not degenerate. The **motor** phenotype is **slowly progressive** in the spastic‑paraplegia subset: "slowly progressive spastic paraplegia" (PMID:10982473). Overall course pattern: **chronic, lifelong, static‑with‑a‑slowly‑progressive‑motor‑component**, punctuated by **episodic** seizures.

**Duration:** Lifelong. Not self‑limited.

### Patterns

**Remission:** No spontaneous remission of ID. Seizures may be well controlled or remit with antiseizure medication in a subset — no quantitative data available. Behavioural difficulties may improve with intervention and maturation.

**Critical periods — the most important temporal fact in this disease.** The 2024 *Nature* work established a discrete, closable developmental window during which WNT modulation is corrective: use of "WNT signalling modulators at specific times reveal that only a transient alteration" is needed, with WNT inhibition in that window rescuing both molecular and behavioural phenotypes in Kdm5c‑KO mice. This defines a **time‑limited therapeutic opportunity in embryonic/early‑postnatal corticogenesis** — and, by implication, means that intervention after that window may not be corrective for the cognitive phenotype. Additional practical windows: early amblyopia detection (visual critical period), and early language/behavioural intervention.

---

## 9. Inheritance and Population

### Epidemiology

**Point prevalence: not established.** No population‑based prevalence or incidence estimate exists for MRXSCJ. Orphanet's epidemiology class for ORPHA:85279 could not be retrieved in this run (API 401 / site bot protection) — **retrieve it from the local structured cache** (`just structured-rebuild-orphanet --id 85279`) before populating a `Prevalence` record. Given ORPHA:85279's designation as a rare multiple‑congenital‑anomaly syndrome, expect `BELOW_1_IN_1000000` or `NOT_YET_DOCUMENTED`.

**What *is* quantified is the gene's share of XLID — a case‑fraction, not a prevalence.** Curate this with `Genetic.case_fractions`, **not** as a `Prevalence` record:

| Estimate | Cohort | Source |
|---|---|---|
| **0.7–2.8%** of XLID | Cited range in current reviews | Hatch et al. 2021, as cited in PMID:41743791 and PMID:40346491 ("Mutations, either maternally transmitted or de novo, account for 0.7-2.8%") |
| **~3.3%** (7/210 families) | XLMR families, brain‑expressed gene screen | Jensen et al. 2005 (PMID:15586325) — "in 210 families with XLMR, we identified seven different mutations in JARID1C" |
| **0.7%** | 143 Brazilian males with probable XLID | Gonçalves et al. 2014 (PMID:24583395) — "KDM5C pathogenic mutational frequency of 0.7% among males with probable XLID" |
| Present among 18 pathogenic variants across 13 XLID genes | 150 male XLID patients, targeted NGS of 107 genes | Tzschach et al. 2015 (PMID:25649377) — familial 26% (13/50) vs sporadic 5% (5/100) overall diagnostic yield |

The widely repeated "2.8–3.3%" figure is best read as the **upper bound from ascertained multiplex XLMR families**, and 0.7% as the yield in unselected/regional cohorts. Report the range with both citations; do not pick one.

For context: ID affects "up to 2% of the population world-wide" (PMID:29670509), and XLID is genetically heterogeneous — "a genetically heterogeneous condition involving more than 100 genes" (PMID:32279304).

### Genetic Etiology Parameters

**Inheritance pattern:** X‑linked. HPO annotates `HP:0001419` **X‑linked recessive inheritance** and OMIM titles it X‑linked recessive — but this label is **empirically wrong for females** and should be curated with a caveat. With 56% of heterozygous females affected (PMID:41537560), the disorder behaves as **X‑linked with markedly sex‑biased severity / incomplete female penetrance**, not clean recessive.

> **KB recommendation:** carry `HP:0001419` (matching the authoritative annotation) but add a second `Inheritance` block or a `notes` field stating the empirical female penetrance. Do **not** silently assert `HP:0001417` (X-linked dominant) — that overcorrects.

**Modes of transmission (RARE‑X cohort, PMID:41537560):**
- **De novo: >50%**
- Maternally inherited: ~10%
- Paternally inherited: ~1% (rare; an affected/mosaic father transmitting to daughters)
- Remainder untested/unknown

This is a major shift from the historical picture. Early gene discovery was done in multiplex XLMR families, which by construction were maternally transmitted; contemporary trio exome ascertainment reveals that **de novo occurrence is now the majority mode**.

**Penetrance:**
- **Males: essentially complete** for ID — 96% (PMID:39835750) to 98% (PMID:41537560). The 8‑year‑old boy without ID (PMID:40125771) is the documented exception and shows penetrance is not literally 100%.
- **Females: incomplete** — 56–79% with ID/learning disability; Carmignac et al. found **4/19 heterozygous females completely asymptomatic** (PMID:32279304).

**Expressivity: highly variable**, in both sexes. Range spans no‑ID to severe ID with progressive spastic paraplegia, within and across families. Carmignac: "All affected individuals presented with learning disabilities or ID (mostly moderate)."

**Genetic anticipation:** **Not applicable.** No repeat expansion mechanism.

**Germline mosaicism:** Not specifically documented for *KDM5C*, but must be assumed possible for recurrence‑risk counselling given the high de novo rate (standard practice: quote ~1% empiric recurrence risk after an apparently de novo variant, higher if maternal mosaicism is detected).

**Founder effects:** None reported. Variants are private/family‑specific; the spectrum is dominated by unique variants (122 unique variants across 130 families — **near‑complete allelic heterogeneity**).

**Consanguinity:** Not a factor — X‑linked, not autosomal recessive.

**Carrier frequency:** Not estimable at population level. Given pLI=1 / LOEUF=0.17 and the near‑absence of LoF variants in gnomAD, carrier frequency is very low and dominated by de novo events.

### Population Demographics

**Affected populations:** No ethnic predilection. Cases reported from Belgium (index family), Australia, USA, Germany, Netherlands, Italy, France, Brazil, China, Thailand, Estonia, Palestine, and elsewhere. First Latin American screen: PMID:24583395. First Palestinian case: PMID:40346491.

**Geographic distribution:** Worldwide, no clustering. Reporting bias favours countries with established exome‑sequencing diagnostics — apparent geography reflects diagnostic access, not biology.

**Geographic distribution of specific variants:** None; no recurrent founder allele.

**Sex ratio:** Historical literature: strongly male‑predominant (the RARE‑X literature meta‑analysis is 153 M : 112 F ≈ **1.4:1**, already far less skewed than the classic "X‑linked recessive" expectation). The RARE‑X *new* cohort is **61% M : 39% F ≈ 1.6:1**. Females are systematically under‑ascertained; the true molecular sex ratio in an unbiased sequencing cohort is likely closer to 1:1, with severity — not occurrence — being the sex‑biased variable.

**Age distribution:** RARE‑X participants ranged **2–20 years** (mean 10.6 y males, 12.4 y females). Adults are markedly under‑represented in the literature — most published individuals are children, which biases natural‑history and prognosis data toward the paediatric course. Oldest well‑described individuals include a 27‑year‑old woman (PMID:36553533) and a 48‑year‑old (PMID:40544030).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory tests:** No diagnostic biochemical abnormality. Routine metabolic work‑up is normal — "Biochemical investigations, neuroimaging and neuropathology were normal" (PMID:9377804). Standard ID work‑up (CK, thyroid function, plasma amino acids, urine organic acids, acylcarnitines) serves to *exclude* alternatives. Endocrine evaluation (IGF‑1, growth‑hormone axis, thyroid) is warranted for short stature and for the female endocrine excess (PMID:32279304). No LOINC‑coded disease‑specific analyte.

**Biomarkers:** The **DNA‑methylation episignature is the only validated biomarker** (below). No protein or metabolite biomarker.

**Imaging:** Brain MRI is **usually normal or non‑specific** — its role is exclusionary. Reported findings are limited to "faint hyperintensities in posterior periventricular white matter suggesting dysmyelination" in a single case (PMID:40346491). Microcephaly is a clinical/OFC measurement, not an imaging diagnosis. Bone age and skeletal survey may be indicated for short stature/brachydactyly.

**Functional tests:** Formal neuropsychological/developmental assessment (Bayley, WISC, Vineland) is essential for ID diagnosis and severity grading. Ophthalmological assessment — **explicitly under‑used and high‑yield** given 91% abnormal eye movement and the amblyopia risk; PMID:40125771 argues "importance of ophthalmological assessments in X-linked syndromes."

**Electrophysiology:** **EEG** is indicated in all patients — 35–48% have seizures, tonic seizures documented (`HP:0032792`). No pathognomonic EEG signature described. EMG/NCS is not routinely indicated (the motor phenotype is upper‑motor‑neuron), though distal lower‑limb amyotrophy (`HP:0008944`) may prompt it. ECG not indicated.

**Biopsy / pathology:** Not diagnostically indicated. Human neuropathology was unremarkable (PMID:9377804). Skin biopsy for **fibroblast culture** is a *research* tool for functional variant assays (PMID:25666439).

### Genetic Testing

**Recommended approach.** MRXSCJ is clinically non‑specific enough that gene‑first testing is standard:

1. **Trio exome sequencing (WES)** or **genome sequencing (WGS)** — first‑line for unexplained global developmental delay/ID. Trio design is essential given >50% de novo.
2. **Chromosomal microarray (CMA)** — either first‑line alongside, or reflex; detects the Xp11.22 microdeletion subset (~3% of the variant spectrum) that sequencing may miss.
3. **XLID gene panel** — a valid alternative in a family with an X‑linked pedigree. Tzschach et al.'s 107‑gene XLID panel achieved ">10 reads for approximately 96% of coding bases at mean coverage of 124 reads" and yielded 26% in familial vs 5% in sporadic cases (PMID:25649377). *KDM5C* is on all commercial XLID and ID/epilepsy panels; GTR lists dedicated single‑gene tests (e.g. GTR 581685).
4. **Single‑gene KDM5C sequencing** — only for targeted familial‑variant testing / cascade screening once a variant is known.
5. **DNA methylation episignature (EpiSign)** — see below; use as a reflex for VUS resolution and carrier confirmation.

**Modalities not indicated:** karyotype (too low resolution; normal in these patients), FISH (no recurrent rearrangement), mtDNA testing (not mitochondrial), repeat‑expansion testing (no repeat mechanism) — except as differential‑diagnosis exclusions (e.g. FMR1 CGG for fragile X).

**A specific pitfall:** synonymous and deep‑intronic variants can be pathogenic via splicing — c.633G>C (p.Arg211Arg) was predicted to create "an Exonic Splicing Enhancer sequence" and co‑segregated (PMID:24583395); c.782‑2A>T is a canonical splice‑acceptor change producing a PTC (PMID:41743791). RNA studies should be considered before dismissing a segregating synonymous or splice‑region variant.

### Omics‑Based Diagnostics

**Epigenomics — the standout.** Schenkel et al.'s Claes‑Jensen episignature (PMID:29456765) is clinically deployed within the EpiSign framework:
- Derived from 7 male patients vs 56 matched controls; **1,769 CpGs, 9 genomic regions**
- 6 healthy female carriers showed intermediate, distinguishable changes
- "Highly specific computational model using the most significant methylation changes demonstrated 100% accuracy" in the training cohort
- "The 100% specificity of this unique epi-signature was further confirmed on additional 500 unaffected controls" plus 600 ID/DD patients including other episignature cohorts
- Clinical use: "can be used for molecular diagnosis and carrier identification and assist with interpretation of genetic variants" of unknown significance

Real‑world confirmation: Koparir et al. (PMID:41957673) applied EpiSign to 400 NDD individuals — "Seventeen percent of individuals (67/400) harbored variants in chromatinopathy-associated genes," "26 individuals (43%) exhibited disorder-specific episignatures," with KDM5C among the confirmed genes; "Integration of EpiSign analysis facilitated variant reclassification." Methylation profiling has been used specifically "to the reclassification of a variant" (PMID:35781022).

> ⚠️ **Important caveat — do not overstate episignature performance.** Husson et al.'s independent multicentre evaluation (PMID:37872275) found published episignatures perform very unequally: "While ATRX, DNMT3A, KMT2D, and NSD1 signatures displayed a 100% sensitivity, CREBBP-RSTS reached <40%," concluding "Episignatures do not perform equally well. Some signatures are ready for confident use" and "It is imperative to characterise the actual validity perimeter and interpretation of each episignature." The KDM5C signature's original 100% figures come from a **7‑patient training cohort** and reflect *specificity* against large control sets more than *sensitivity* across the full allelic spectrum. Curate the 100% claim as training‑cohort performance with this limitation stated.

**RNA sequencing:** Research tool; potential clinical value for splice‑variant resolution. **Proteomics, metabolomics, liquid biopsy:** no diagnostic role.

### Clinical Criteria

**No formal, standardised diagnostic criteria exist** (no DSM/ICD/society criteria for MRXSCJ). Diagnosis is **molecular**: a pathogenic/likely pathogenic *KDM5C* variant in a compatible phenotype. Historical clinical suspicion criteria remain useful for gene prioritisation — Abidi et al. concluded "male patients with mental retardation, short stature and hyperreflexia should be considered candidates for mutations in the JARID1C gene" (PMID:18697827), and reported in their nine males "mental retardation (100%), short stature (55%), hyperreflexia (78%), seizures (33%) and aggressive behaviour (44%)."

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **Wiedemann‑Steiner syndrome (KMT2A)** | The mechanistic mirror‑image (writer vs eraser); hypertrichosis cubiti, distinct facies; AD |
| **Kabuki syndrome (KMT2D/KDM6A)** | Characteristic facies, persistent fetal fingertip pads, cardiac defects, immune deficiency |
| **KDM1A‑related NDD** | Cooperative partner gene; overlapping chromatin phenotype |
| **ATR‑X syndrome (ATRX)** | Alpha‑thalassaemia, HbH inclusions, genital anomalies, severe XLID |
| **Other XLID genes** (IQSEC2, MED12, SLC9A6, CUL4B, OPHN1, UPF3B, ZDHHC9, AP1S2, DLG3, SMC1A, UBE2A) | All co‑detected in the same panels (PMID:25649377); require sequencing to distinguish |
| **Fragile X (FMR1)** | Macroorchidism (vs *small* testes in MRXSCJ — a useful discriminator), long face, large ears; repeat expansion |
| **Coffin‑Lowry (RPS6KA3)** | Tapering fingers, characteristic facies, drop attacks |
| **Hereditary spastic paraplegia (SPG1/L1CAM, SPG2/PLP1)** | Both explicitly excluded in the original Claes family — "The two known loci for X-linked mental retardation and spastic paraplegia are excluded" (PMID:10982473) |
| **Snyder‑Robinson (SMS)** | XLID with osteoporosis, thin habitus, seizures |
| **Renpenning syndrome (PQBP1)** | XLID with microcephaly and short stature — close phenocopy |

Because the phenotype is non‑specific, **the differential is effectively "all XLID/ID" and is resolved by sequencing, not by clinical discrimination.**

### Screening

- **Newborn screening:** Not included in any programme; no treatable metabolic marker. Not appropriate under current criteria.
- **Carrier screening (population):** Not offered; not on expanded carrier screening panels.
- **Cascade / family screening: yes, and important.** Once a familial variant is known, test at‑risk female relatives — both for reproductive counselling and because **carrier females are frequently affected** and may benefit from their own diagnosis. The episignature independently identifies healthy carriers (PMID:29456765).
- **Prenatal / preimplantation:** Available for known familial variants (see §13).
- **Risk stratification:** No validated model. Male sex and a catalytic‑domain variant are the two crude severity predictors currently available.

---

## 11. Outcome / Prognosis

> **Evidence quality warning:** there is **no published survival study, no mortality analysis, and no longitudinal natural‑history cohort with adult outcomes** for MRXSCJ. The RARE‑X cohort — the largest prospective dataset — has a maximum age of 20 years. Everything in this section about survival is inference, and should be curated as such (or omitted) rather than asserted.

### Survival and Mortality

- **Survival rate (5‑/10‑year/overall): no data.**
- **Life expectancy:** Not established. There is **no evidence of shortened lifespan** attributable to the disorder itself — it is not a degenerative or organ‑failure condition, and individuals into their 40s are described (PMID:40544030). Any excess mortality would be expected to arise from the generic ID‑population risks: seizure‑related events (including SUDEP, given 35–48% epilepsy), aspiration in the hypotonic/dysphagic subset, and immobility complications in the spastic‑paraplegia subset. **None of these has been quantified for MRXSCJ.**
- **Mortality rate / disease‑specific mortality:** no data.

### Morbidity and Function

Morbidity is **substantial and lifelong**, dominated by cognitive and behavioural burden:
- 82% ID overall (98% males, 56% females); males predominantly **severe** (70%)
- Communication challenges 93%; most severely affected males have minimal expressive language
- Behavioural concerns 78% — impulsivity 88%, short attention span 88%, anxiety 71%, ASD 65%
- Mobility: progressive spastic paraplegia in a subset → contractures, gait loss, wheelchair dependency
- Most affected males require **lifelong supported living**; independent living is realistic only for mildly affected individuals, disproportionately female
- ICF domains affected: learning and applying knowledge, communication, mobility (subset), self‑care, interpersonal interactions

**Quality‑of‑life measures:** **No EQ‑5D, SF‑36, PROMIS, or disease‑specific QoL instrument has been administered.** The RARE‑X caregiver survey is the closest proxy and captures symptom burden rather than validated QoL. This is a clear, actionable research gap.

### Disease Course and Complications

| Complication | Notes |
|---|---|
| Epilepsy, potentially refractory | 35–48%; median onset 2 y |
| Progressive spastic paraplegia, contractures | Subset; slowly progressive |
| Aggression / behavioural crisis | The leading cause of care breakdown and psychotropic escalation |
| Amblyopia from untreated strabismus | Preventable with early ophthalmology |
| Chronic constipation | 83% — under‑recognised, drives discomfort/behaviour |
| Failure to thrive, feeding difficulty | Infancy |
| Aspiration / recurrent respiratory infection | Secondary to hypotonia |
| Cryptorchidism → fertility/malignancy risk | Requires urological management |
| Cholelithiasis | Reported (2/20), unexplained |
| Osteoporosis/fracture | Expected with immobility; not specifically studied |

**Recovery potential:** **None for the established cognitive deficit under current therapy** — this is a static, structural neurodevelopmental condition. The WNT data (PMID:38383780) are the first credible evidence that the phenotype is *biologically* reversible, but only within an early developmental window and only in mice/patient cells.

### Prediction

**Prognostic factors (all weak, none validated):**
1. **Sex** — the strongest predictor. Male → severe (70% severe ID); female → mild (56% mild).
2. **Variant domain** — catalytic (JmjC/C5HC2) variants associate with seizures (PMID:39835750).
3. **Variant class** — the *hypothesis* that "Missense mutations in catalytic domains may retain partial enzymatic activity, potentially producing milder phenotypes than nonsense mutations" (PMID:39835750). **Unproven, and complicated by R1115H** (normal activity, still pathogenic) and by D87G (normal activity, disease‑associated). Do not curate as established.
4. **Early seizure onset** — plausibly predicts worse cognitive outcome, as in most DEEs; **not demonstrated** in MRXSCJ.
5. **Residual expressive language** at age 5 — a general ID prognostic anchor; not MRXSCJ‑specific.

**Prognostic biomarkers:** **None.** The episignature is diagnostic, not prognostic — no correlation between episignature strength and severity has been established.

---

## 12. Treatment

> **There is no disease‑modifying therapy, no approved drug, no gene therapy, and no interventional clinical trial for MRXSCJ.** Management is entirely symptomatic, supportive, and multidisciplinary. Everything below labelled "experimental" is preclinical.

### Pharmacotherapy (all symptomatic)

| Indication | Agents | NCIT candidate |
|---|---|---|
| Seizures | Standard antiseizure medications; choice by seizure semiology (tonic seizures documented). **No MRXSCJ‑specific ASM data or recommended agent.** | `NCIT:C15986` Pharmacotherapy + therapeutic_agent per drug |
| ADHD / impulsivity (88%) | Stimulants, alpha‑2 agonists — standard ID/ADHD practice | `NCIT:C15986` |
| Aggression / irritability | Atypical antipsychotics (risperidone, aripiprazole) — standard ASD/ID practice | `NCIT:C15986` |
| Anxiety (71%) | SSRIs — standard practice | `NCIT:C15986` |
| Spasticity | Baclofen, botulinum toxin | `NCIT:C15986` |
| Constipation (83%) | Osmotic laxatives, bowel regimen | `NCIT:C15986` |
| Short stature | Growth hormone **not indicated absent documented GH deficiency**; no MRXSCJ evidence base | — |

**Pharmacogenomics:** ClinGen reports **0 CPIC and 0 PharmGKB records** for KDM5C. No gene‑specific PGx guidance. Standard CYP2D6/CYP2C19 considerations apply to the psychotropics used, unrelated to KDM5C.

### Advanced Therapeutics

- **Gene therapy / gene replacement:** none. Conceptually challenging — a 1,560‑aa protein whose dose must be *balanced* (both loss and excess are deleterious, cf. the KMT2A epistasis) and whose critical window may be prenatal.
- **Gene editing:** none.
- **RNA‑based therapies (ASO/siRNA/mRNA):** none. Note that a *KDM5C* upregulation strategy (e.g. targeting a repressive element or NMD‑escape approach) is theoretically attractive for haploinsufficiency but entirely unexplored.
- **Cell therapy, immunotherapy, targeted therapy:** none.

### Experimental / Preclinical Strategies

Three distinct, non‑overlapping preclinical leads — worth curating as `mechanistic_hypotheses` with `status: EMERGING` and explicit `MODEL_ORGANISM` evidence tagging:

1. **Transient WNT inhibition during a developmental window** (strongest lead). "WNT inhibition during this developmental period also rescues behavioural changes of Kdm5c knockout mice" and rescues "the transcriptomic and chromatin landscapes in patient-derived cells" (PMID:38383780, *Nature* 2024). **Limitation:** the window may close before postnatal diagnosis is possible — the central translational obstacle.
2. **Rebalancing the H3K4 writer–eraser pair (KMT2A inhibition).** "Double mutation of Kmt2a and Kdm5c clearly reversed dendritic morphology, key behavioral traits," supporting "balancing a single writer-eraser pair to ameliorate their associated disorders" (PMID:32483278). A genetic, not pharmacological, proof of concept; MLL1/menin inhibitors exist in oncology and are a conceivable repurposing route.
3. **Toll‑like receptor pathway inhibition (CU‑CPT 4a).** In zebrafish, treatment at ½ LC50 "partially restored morphological defects, including head area, body length and eye size" and "spontaneous swimming activity was restored"; the authors propose "Targeting the regulation of TRL related receptors (such as TLR3) may become a potential strategy" (PMID:41743791). **Weakest of the three** — zebrafish only, single study, unreplicated, and the interferon signature has no human correlate yet.

**ClinicalTrials.gov:** no interventional trial registered for MRXSCJ/KDM5C‑NDD. The **RARE‑X KDM5C Data Collection Program** (PMID:41537560) is an observational patient‑registry, not a trial, and is the appropriate referral for families seeking research participation.

### Surgical and Interventional

- **Orchidopexy** for cryptorchidism (`NCIT:C15329` / `NCIT:C16186` candidates)
- **Strabismus surgery** and refractive correction (`NCIT:C15329`)
- **Orthopaedic surgery** for contractures, foot deformity (talipes equinovarus/calcaneovarus), scoliosis (`NCIT:C16186` Orthopedic Surgical Procedure)
- **Cholecystectomy** if symptomatic cholelithiasis
- **Gastrostomy** in the failure‑to‑thrive/dysphagia subset
- Epilepsy surgery: no reported role

### Supportive and Rehabilitative — the mainstay

| Intervention | NCIT candidate | `therapeutic_modality` |
|---|---|---|
| Early intervention / developmental therapy | `NCIT:C15315` Rehabilitation | `BEHAVIORAL` |
| **Speech and language therapy** (93% communication challenges; AAC often needed) | `NCIT:C159273` | `BEHAVIORAL` |
| Physical therapy (spasticity, gait) | `NCIT:C15302` | `BEHAVIORAL` |
| Occupational therapy | `NCIT:C121351` | `BEHAVIORAL` |
| Applied behaviour analysis / behavioural support | `NCIT:C181743` | `BEHAVIORAL` |
| Special education, IEP | — | `BEHAVIORAL` |
| Nutritional support for FTT | `NCIT:C15433` — **note CLAUDE.md caveat: do NOT auto‑tag as BEHAVIORAL** | assess per intervention |
| Supportive care, coordination | `NCIT:C15747` | — |
| **Genetic counselling** | `NCIT:C15240` | — |

### Treatment Outcomes

**Response rates:** No quantitative data for any intervention. **Adverse events:** none disease‑specific; standard profiles for the symptomatic agents used. Aggression and hyperactivity in this population frequently drive polypharmacy — a recognised iatrogenic risk in ID generally.

### Treatment Strategy

No published clinical practice guideline or care pathway exists for MRXSCJ. Practical algorithm, synthesised from the phenotype frequencies:

1. **At diagnosis:** baseline developmental/neuropsychological assessment; **EEG**; **formal ophthalmological exam** (91% abnormal eye movement — highest‑yield under‑performed test); growth chart with OFC; feeding/GI assessment; genital exam (males); genetic counselling; offer episignature if variant is a VUS.
2. **Ongoing surveillance:** annual growth/OFC; annual vision; developmental re‑assessment; seizure review; behavioural review; spasticity/gait exam; bowel review.
3. **Escalate:** ASM for seizures; behavioural intervention before psychotropics; PT/orthopaedics for progressive spasticity.
4. **Family:** cascade testing of at‑risk females; recurrence‑risk counselling; connect to RARE‑X registry and patient advocacy.

**Combination therapies / personalised medicine:** No genotype‑guided treatment exists. The nearest thing to precision stratification is domain‑based seizure risk (catalytic‑domain variants → heightened seizure surveillance) — reasonable clinical prudence, but not a validated rule.

---

## 13. Prevention

**Primary prevention of the disease itself is not possible** — it is a germline monogenic condition, and >50% of cases arise de novo, meaning most cases are unpredictable and unpreventable. "Prevention" here means recurrence prevention within families plus prevention of secondary complications.

### Prevention Levels

**Primary (preventing occurrence):** Limited to reproductive options in families with a known variant (below). No vaccination, no risk‑factor modification, no environmental avoidance is relevant.

**Secondary (early detection and intervention):** This is where real benefit lies.
- **Early molecular diagnosis** via trio WES/WGS in unexplained global developmental delay — ends the diagnostic odyssey, enables targeted surveillance, and (given the WNT critical‑window data) may eventually enable window‑timed intervention.
- **Cascade testing** of at‑risk female relatives — identifies affected/at‑risk females who are currently under‑diagnosed.
- **Episignature testing** to resolve VUS and confirm carriers (PMID:29456765).
- **Early ophthalmology** to prevent amblyopia — the clearest preventable morbidity.
- **Early EEG and seizure recognition.**
- **Early speech/AAC intervention.**

**Tertiary (preventing complications in affected individuals):**
- Seizure control to reduce injury and SUDEP risk
- Spasticity management and stretching/orthotics to prevent contractures
- Bowel regimen to prevent chronic constipation and impaction
- Nutritional support to prevent FTT sequelae
- Orchidopexy to reduce cryptorchidism‑related fertility/malignancy risk
- Behavioural support to prevent crisis and placement breakdown
- Fall/fracture prevention in the immobile subset

### Immunization

No disease‑specific vaccine strategy. **Routine childhood immunisation is indicated and should not be deferred** — recurrent respiratory infections are an annotated feature (`HP:0002205`, `HP:0002788`), making influenza and pneumococcal vaccination particularly worthwhile. Note that the zebrafish interferon findings do **not** constitute any contraindication.

### Screening and Early Detection

- **Population screening / newborn screening:** not indicated, not available (no treatable metabolic marker; does not meet Wilson‑Jungner criteria).
- **Carrier screening:** not on expanded carrier panels.
- **Genetic screening in families with a known variant:**
  - **Prenatal diagnosis** — CVS or amniocentesis for the known familial variant
  - **Preimplantation genetic testing for monogenic disease (PGT‑M)** — technically straightforward for a known *KDM5C* variant
  - Both require prior identification of the familial variant; counsel explicitly that **a female fetus carrying the variant has a substantial (~56%) chance of being affected**, which materially changes historical "carrier daughters are unaffected" counselling
- **Risk stratification:** no validated model.

### Behavioural Interventions

None reduce disease risk. Behavioural intervention is treatment (§12), not prevention.

### Counselling

**Genetic counselling is the central preventive intervention** (`NCIT:C15240`). Key content, updated for current evidence:

1. **De novo is now the majority mode (>50%)** — a substantially lower recurrence risk than the classic X‑linked‑recessive family framing implies. Quote empiric ~1% for gonadal mosaicism after an apparently de novo variant.
2. **Carrier mother:** 50% transmission to each child; sons who inherit will be affected (~98%); **daughters who inherit have ~56% chance of ID/learning disability and ~18–19% chance of seizures** — they are not reliably unaffected.
3. **Affected male:** all daughters obligate carriers, no sons affected (rare paternal transmission documented, ~1%).
4. Offer maternal testing, cascade testing of maternal relatives, and prenatal/PGT‑M options.
5. Counsel on the **wide variable expressivity** including the documented no‑ID case — prognosis cannot be predicted precisely from genotype.
6. Connect to the **RARE‑X KDM5C Data Collection Program** and patient advocacy.

Carmignac et al. make the counselling point directly: consideration of "XLID genes in females, even in sporadic affected individuals" is required (PMID:32279304).

### Public Health / Environmental Interventions / Prophylaxis

Not applicable — no environmental determinant, no infectious transmission, no prophylactic medication or procedure.

---

## 14. Other Species / Natural Disease

### Taxonomy

*KDM5C* orthologues are present across vertebrates and, as a single ancestral *KDM5* gene, across bilaterians:

| Species | NCBI Taxon | Gene | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | KDM5C | 8242 |
| *Mus musculus* | `NCBITaxon:10090` | Kdm5c | **MGI:99781** (ChrX:151,016,016–151,057,531, + strand) |
| *Rattus norvegicus* | `NCBITaxon:10116` | Kdm5c | RGD ortholog |
| *Danio rerio* | `NCBITaxon:7955` | kdm5c | ZFIN |
| *Drosophila melanogaster* | `NCBITaxon:7227` | **Kdm5/lid** ("little imaginal discs") — **single** KDM5 family gene, **autosomal** | FlyBase |
| *Caenorhabditis elegans* | `NCBITaxon:6239` | rbr-2 | WormBase |

The *Drosophila* situation is analytically valuable: a **single autosomal** *Kdm5* gene collapses the KDM5A/B/C/D paralogue redundancy and removes sex‑chromosome dosage effects. The RARE‑X team exploited exactly this — fly seizures show "no sex differences in flies (unlike humans), reflecting autosomal Kdm5 location" (PMID:41537560), cleanly attributing the human sex bias to X‑linkage/XCI‑escape rather than to KDM5 biology itself.

### Breed

**Not applicable.** No breed‑associated *KDM5C* disorder in any domestic species. No VBO identifier applies.

### Natural Disease in Other Species

**None documented.** An OMIA search for KDM5C returned **"No phene records found"** — there is no naturally occurring *KDM5C* disease in companion animals, livestock, or wildlife. All non‑human disease models are **engineered**, not natural.

**Veterinary relevance:** none.

### Comparative Biology

**Evolutionary conservation is high and functionally validated.** Three independent lines:
- Sequence: the S451R variant residue "is conserved" across JARID1 family members "and in mouse and fruit fly" (PMID:16538222); pathogenic missense variants "alter evolutionarily conserved amino acids" (PMID:15586325); ARID‑domain disease variants "are located in a highly-conserved part of the ARID structure" (PMID:26580603).
- Enzymatic: H3K4me3 demethylase activity is shared across the whole KDM5 family — "Other family members including SMCY, RBP2, and PLU-1 also demethylated H3K4me3" (PMID:17320160).
- Phenotypic: the cognitive/behavioural consequence of KDM5 loss is conserved from fly (impaired learning/memory, seizures) through zebrafish (behavioural and morphological defects) to mouse (memory deficits, aggression, social deficits) to human (ID, seizures, aggression). **This cross‑phylum concordance is unusually strong for an ID gene** and materially raises confidence in the model systems.

**Comparative pathology — differences worth noting:**
- Mouse Kdm5c‑KO shows **no gross brain cytoarchitectural abnormality**, mirroring the largely normal human MRI — good fidelity.
- The mouse phenotype is **regionally selective** (basolateral amygdala ≫ motor cortex); no human equivalent has been sought.
- Fly *Kdm5* loss produces a **ribosome/translation** deficit not yet demonstrated in mammals — a candidate `HUMAN_MODEL_MISMATCH`.
- Zebrafish mutants show **cartilage/craniofacial** defects and an **interferon** signature; the craniofacial arm loosely echoes human maxillary hypoplasia, but the interferon arm has no human correlate.

### Transmission

**Not applicable** — non‑infectious, no zoonotic potential, no cross‑species susceptibility.

---

## 15. Model Organisms

### 15.1 Mouse — the principal mammalian model

**Resource:** MGI:99781. **38 total mutations and alleles** (7 endonuclease‑mediated, 24 gene‑trapped, 7 targeted); **22 strains/lines** available via IMSR. "22 phenotypes from 4 alleles in 4 genetic backgrounds." MGI explicitly curates a mouse model of **"Syndromic X-linked intellectual disability Claes-Jensen type (OMIM:300534)."**

**Model types available:** constitutive knockout, gene‑trap, targeted/conditional (floxed), endonuclease‑mediated (CRISPR) alleles, and **forebrain‑specific inducible KO (ifKO)** used in the Barco lab studies.

**Phenotype recapitulation — Iwase et al. 2016 (PMID:26804915), the flagship:**

| Domain | Mouse finding | Human counterpart |
|---|---|---|
| Aggression | "latency of the first attack to the intruder mouse was significantly shorter for Kdm5c-KO than WT mice (KO: 12.7 ± 2.4 sec, n = 13; WT: 37.6 ± 9.2 sec, n = 13; P < 0.05)" | Aggressive behaviour, HP:0000718, 13/38 |
| Social behaviour | "WT mice spent significantly more time exploring the stimulus mouse than an inanimate object, Kdm5c-KO mice spent similar time between the two" | ASD 65% |
| Memory | "Kdm5c-KO mice showed significantly reduced freezing responses"; Morris water maze "significantly slower decline in latency" (P<0.01) | Intellectual disability |
| Anxiety | "Kdm5c-KO mice spent significantly more time in the open arms of the maze" — i.e. **reduced** anxiety‑like behaviour | ⚠️ **Direction mismatch** — humans show anxiety in 71% |
| Growth | "Kdm5c-KO mice exhibited smaller body size and reduced body weight (P < 0.005)" — noted as "comparable to shorter stature in ~60% of affected individuals" | Short stature 50–78% |
| Brain structure | "no gross abnormalities in the cytoarchitecture of the adult Kdm5c-KO cerebral cortex, hippocampus, or amygdala" | Normal/near-normal MRI |
| Dendrites (BLA) | "dendrites of BLA pyramidal neurons showed significantly reduced total length (P < 0.0005)"; "reduced spine density, approximately 45% of WT"; spines "noticeably thinner," lacking "mature mushroom-like morphology" | No human data |
| Dendrites (motor cortex) | "slight (9%) but significant reduction of spine density (P < 0.05)" | No human data |
| Chromatin | "94% of Kdm5c-bound promoters contain a CpG island" (P<1×10⁻²⁶); "global levels of H3K4me1, me2 or me3 are comparable in WT and Kdm5c-KO neurons" | Consistent with locus-specific human episignature |

**Model limitations (Iwase 2016):**
- **Seizures were not a reported phenotype**, despite 35–48% seizure frequency in humans. The seizure phenotype had to be modelled in *Drosophila* instead (PMID:41537560) — a real gap in the mouse.
- **Anxiety runs the wrong direction** (mouse anxiolytic‑like, human anxious).
- **Heterozygous females were not examined**: "The KDM5C gene is X-linked in humans and mice, and affected human individuals are predominantly male, so we focused our analyses on male hemizygous animals." This omission was corrected seven years later by Bonefas & Iwase (PMID:36831303), who found "gene expression and behavioral abnormalities are readily detectable in Kdm5c-heterozygous female mice" and identified "sex-specific consequences of a reduced KDM5C dose in social behavior, gene expression." **This is a case study in how a male‑only model design propagated the false 'unaffected carrier' assumption.**
- No craniofacial or skeletal phenotype characterised; no epilepsy, GI, or ophthalmological modelling.

**Other key mouse studies:**
- **Scandaglia et al. 2017 (PMID:28978483)** — Kdm5c‑null + forebrain‑specific inducible KO. Established the developmental‑repressor and adult‑surveillance dual role.
- **Vallianatos et al. 2020 (PMID:32483278)** — *Kmt2a;Kdm5c* double mutant; mutual suppression. The therapeutic proof of concept.
- **Martín‑González et al. 2025 (PMID:40864554)** — *Kdm1a;Kdm5c* double inducible forebrain KO; synergistic loss of neuronal identity and increased CA1 excitability.
- **Karwacki‑Neisius et al. 2024 (PMID:38383780)** — Kdm5c‑KO + human patient‑derived cells; WNT‑window rescue. The most translationally significant mouse result to date.

### 15.2 Zebrafish (*Danio rerio*)

Two generations of work:
- **Iwase et al. 2007 (PMID:17320160)** — original: zebrafish and mammalian neuron studies revealed "roles in neuronal survival and dendritic development linked to demethylase activity."
- **Liao et al. 2026 (PMID:41743791)** — a full patient‑variant model. Two clinical variants (c.3019del, c.782‑2A>T) expressed in zebrafish:
  - Morphology: "significantly reduced head area, body length, and eye size compared with control and WT groups" — **directly models microcephaly and short stature**; Alcian blue showed "impaired cartilage development"
  - **Specificity control performed:** "Co-injection with WT KDM5C mRNA rescued these phenotypic defects" — an important rigour marker
  - Behaviour: "All behavioral parameters were significantly altered in the c.3019del and c.782-2A>T groups" (reduced distance travelled and swimming speed), partially rescued by WT mRNA
  - Transcriptomics: 363 and 326 DEGs, overwhelmingly upregulated, enriched for antiviral/interferon responses; six validated genes (TLR3, NFKB1, IFNB1, IRF7, SAT1a, SAT1b)
  - Pharmacological rescue: CU‑CPT 4a at ½ LC50 — "Treatment partially restored morphological defects" and "spontaneous swimming activity was restored"

**Strengths:** rapid, scalable variant‑function assay with built‑in WT rescue control; models the growth/microcephaly axis the mouse handles less directly. **Limitations:** morpholino/mRNA‑injection transient models rather than stable germline mutants; the interferon signature is unreplicated and may be an injection artefact; no cognitive readout; single study.

### 15.3 *Drosophila melanogaster*

**Single autosomal *Kdm5*/*lid* gene** — the analytical advantage described in §14.

- **Zamurrad et al. 2018 (PMID:29490272)** — *kdm5^A512P*, a knock‑in of the fly residue equivalent to a human KDM5C disease missense variant. Found "a striking downregulation of genes required for ribosomal assembly and function" and reduced translation; "kdm5^A512P flies also showed impaired learning and/or memory." Concluded "the primary defect of the KDM5A512P mutation is a loss of histone demethylase activity."
- **Terry et al. 2026 (PMID:41537560)** — the seizure model, and the most clinically decisive fly result:
  - Neuronal knockdown (*elav>shKdm5*): mechanical stress "Significantly more knockdown flies exhibited seizures (53%) than controls (19%)"; heat stress 58% vs 9%; spontaneous 6.74% vs 0%
  - **Cell‑type specificity:** "Reducing the expression of its single Kdm5 gene in neurons, but not glia, led to spontaneous and stimulus-induced seizures"
  - **Dissociation from gross morphology:** mushroom body reduction caused morphological defects but **not** seizures — separating the structural from the excitability phenotype
- **Yheskel et al. 2025 (PMID:41340160)** — compared demethylase‑dead (*Kdm5^JmjC\**) vs pathogenic ID variant (*Kdm5^L854F*). Found the two "produced divergent effects on H3K4me3 distribution" yet "similar transcriptional dysregulation" not correlated with recruitment, H3K4me3, or accessibility; instead "altered gene expression in both alleles correlates with preexisting chromatin signatures." Conclusion: "KDM5 operates in conjunction with local chromatin contexts to employ demethylase-dependent and independent mechanisms."
- Related: Hatch et al. on the KDM5–Prospero axis in mushroom body development; PMID:39677601 (bioRxiv preprint) on KDM5 insulator activity in the brain — **preprint, not peer‑reviewed; do not cite as evidence.**

**Strengths:** the only system that has reproduced the **seizure** phenotype; enables clean neuron‑vs‑glia and enzymatic‑vs‑non‑enzymatic dissection; no paralogue redundancy or sex‑chromosome confound. **Limitations:** no mammalian cortex; "learning/memory" assays are only loosely homologous to human cognition; the ribosome finding remains fly‑specific.

### 15.4 Cellular and In Vitro Models

- **Patient‑derived primary fibroblasts** — the workhorse for variant functional assay: protein stability, demethylase activity, and "local changes in chromatin conformation and gene expression" (PMID:25666439).
- **Patient‑derived cells for WNT rescue** — used in PMID:38383780; the substrate for demonstrating pharmacological reversibility.
- **Primary cortical/hippocampal neuron culture** with KDM5C overexpression — used to show R1115H's non‑enzymatic defect in post‑mitotic neurons (PMID:29670509).
- **Biochemical/structural:** recombinant ARID domain with urea‑induced unfolding and binding free‑energy calculations (PMID:26580603) — a `COMPUTATIONAL` + `IN_VITRO` hybrid.
- **iPSC / cerebral organoids:** **no published MRXSCJ iPSC or organoid model.** Given the WNT‑timed progenitor mechanism, human cortical organoids are the obvious missing system and the single highest‑value model gap. Curate as `KNOWLEDGE_GAP` with `proposed_experiments`.

### 15.5 Model Databases

MGI (MGI:99781), IMSR (22 strains), IMPC, KOMP/EuMMCR, ZFIN, FlyBase, WormBase, Alliance of Genome Resources, Cellosaurus (for patient fibroblast lines, where deposited).

---

## Appendix A — Consolidated Reference List

Landmark and current sources, with PMIDs for `just fetch-reference`.

**Disease definition and clinical delineation**
| PMID | Citation | Evidence source |
|---|---|---|
| 9377804 | Claes S et al. *Clin Genet* 1997 — original Belgian family (linkage then placed at Xq27‑28) | HUMAN_CLINICAL |
| 10982473 | Claes S et al. *Am J Med Genet* 2000 — "Novel syndromic form of X-linked complicated spastic paraplegia" | HUMAN_CLINICAL |
| 15586325 | Jensen LR et al. *Am J Hum Genet* 2005 — **gene discovery**, 7 mutations in 210 XLMR families | HUMAN_CLINICAL |
| 16541399 | Tzschach A et al. *Hum Mutat* 2006 — 5 novel mutations | HUMAN_CLINICAL |
| 16538222 | Santos C et al. *Eur J Hum Genet* 2006 — S451R | HUMAN_CLINICAL |
| 18697827 | Abidi FE et al. *J Med Genet* 2008 — ID + short stature + hyperreflexia triad; frequencies | HUMAN_CLINICAL |
| 24583395 | Gonçalves TF et al. *Eur J Med Genet* 2014 — Brazilian screen, 0.7% frequency | HUMAN_CLINICAL |
| 25649377 | Tzschach A et al. *Eur J Hum Genet* 2015 — 107-gene XLID NGS panel | HUMAN_CLINICAL |
| 32279304 | **Carmignac V et al. *Clin Genet* 2020 — female phenotype, 19 new individuals** | HUMAN_CLINICAL |
| 39835750 | **Ghasemi et al. *Mol Genet Genomic Med* 2025 — 175-case review, sex-stratified frequencies** | HUMAN_CLINICAL |
| 41537560 | **Terry et al. *Hum Mol Genet* 2026 — RARE-X, 269 individuals + Drosophila seizures** | HUMAN_CLINICAL + MODEL_ORGANISM (split the evidence items) |

**Case reports expanding the spectrum**
| PMID | Citation |
|---|---|
| 36536324 | Shen R et al. *BMC Neurol* 2022 — female, de novo p.S1178X, no skewed XCI |
| 36553533 | Lintas C et al. *Genes* 2022 — 27-y-old female, de novo p.Glu1283* |
| 39948613 | Meng Y et al. *Ital J Pediatr* 2025 — p.R929X, NMD + mislocalisation |
| 40346491 | Shaheen MM et al. *BMC Pediatr* 2025 — first Palestinian case, post-viral regression |
| 40125771 | Murati FA et al. *J Pediatr Ophthalmol Strabismus* 2025 — **Claes-Jensen without ID** |

**Mechanism**
| PMID | Citation | Evidence source |
|---|---|---|
| 7951230 | Agulnik AI et al. *Hum Mol Genet* 1994 — SMCX **escapes X-inactivation** | IN_VITRO |
| 17320160 | Iwase S et al. *Cell* 2007 — KDM5 family are H3K4 demethylases | IN_VITRO |
| 17468742 | Tahiliani M et al. *Nature* 2007 — **SMCX–REST/HDAC/G9a**, SCN2A/SYN1 | IN_VITRO |
| 23246292 | Poeta L et al. *Am J Hum Genet* 2013 — **ARX → KDM5C** regulatory axis | MODEL_ORGANISM + IN_VITRO |
| 23356856 | *BMC Med Genomics* 2013 — multilocus loss of DNA methylation | HUMAN_CLINICAL |
| 25666439 | Brookes E et al. *Hum Mol Genet* 2015 — protein stability + activity | IN_VITRO |
| 26580603 | Peng Y et al. *Int J Mol Sci* 2015 — ARID domain variants | COMPUTATIONAL + IN_VITRO |
| 26804915 | **Iwase S et al. *Cell Rep* 2016 — Kdm5c-KO mouse** | MODEL_ORGANISM |
| 28978483 | Scandaglia M et al. *Cell Rep* 2017 — spurious transcription, enhancer fine-tuning | MODEL_ORGANISM |
| 29670509 | Vallianatos CN et al. *Front Mol Neurosci* 2018 — **R1115H, non-enzymatic role** | IN_VITRO |
| 29490272 | Zamurrad S et al. *Cell Rep* 2018 — Drosophila kdm5^A512P, ribosome/translation | MODEL_ORGANISM |
| 32483278 | Vallianatos CN et al. *Commun Biol* 2020 — **KMT2A/KDM5C mutual suppression** | MODEL_ORGANISM |
| 34536985 | Hatch HAM & Secombe J *FEBS J* 2022 — review | OTHER |
| 36831303 | **Bonefas & Iwase *Cells* 2023 — sexually dimorphic; heterozygous females affected** | MODEL_ORGANISM |
| 38383780 | **Karwacki-Neisius V et al. *Nature* 2024 — WNT window, rescue** | MODEL_ORGANISM + IN_VITRO |
| 40864554 | Martín-González AM et al. *Cell Rep* 2025 — KDM1A/KDM5C cooperation | MODEL_ORGANISM |
| 41340160 | Yheskel M et al. *Epigenetics Chromatin* 2025 — chromatin-context dependence | MODEL_ORGANISM |
| 41743791 | Liao et al. *Front Mol Neurosci* 2026 — zebrafish, TLR/interferon, CU-CPT 4a | MODEL_ORGANISM |

**Diagnostics / epigenetics**
| PMID | Citation |
|---|---|
| 29456765 | **Schenkel LC et al. *Clin Epigenetics* 2018 — Claes-Jensen episignature** |
| 31419599 | *Eur J Med Genet* 2020 — monozygotic twin methylation fingerprint |
| 35781022 | *Eur J Med Genet* 2022 — methylation profiling for variant reclassification |
| 37872275 | **Husson T et al. *Eur J Hum Genet* 2024 — independent episignature evaluation (caveat source)** |
| 41957673 | Koparir A et al. *Clin Epigenetics* 2026 — chromatinopathies, 400 individuals, EpiSign |

**Non-literature resources consulted:** EBI OLS4 (MONDO, ORDO); HPO/JAX annotation API (`OMIM:300534`); NCBI MedGen 335139; NCBI ClinVar (528 P/LP records); ClinGen (Gene-Disease Validity: Definitive, ID & Autism GCEP 2018-09-19; Dosage HI=3/TS=0, 2023-07-27; pLI=1, LOEUF=0.17); UniProt P41229; MGI:99781; OMIA (no entries).

---

## Appendix B — Curation Notes for the dismech Entry

**Suggested pathophysiology node chain** (each `biological_scale` tagged; keep nodes atomic — see the single-value discipline in CLAUDE.md):

| Node | `biological_scale` | Key evidence |
|---|---|---|
| KDM5C Loss of Function | MOLECULAR | PMID:15586325, PMID:25666439 |
| Impaired H3K4me3/me2 Demethylation at CpG-Island Promoters | MOLECULAR | PMID:17320160, PMID:26804915 |
| Loss of Non-Enzymatic KDM5C Scaffolding Function | MOLECULAR | PMID:29670509, PMID:41340160 |
| REST Complex Target Derepression | MOLECULAR | PMID:17468742 |
| Dysregulated Canonical WNT Signalling During Corticogenesis | CELLULAR | PMID:38383780 |
| Mistimed Progenitor Transition and Neurogenesis | CELLULAR | PMID:38383780 |
| Spurious Transcription and Loss of Neuronal Identity | CELLULAR | PMID:28978483, PMID:40864554 |
| Impaired Dendritic Arborisation and Spine Maturation | TISSUE | PMID:26804915 |
| Neuronal Hyperexcitability | CELLULAR | PMID:40864554, PMID:41537560 |
| Intellectual Disability and Neurobehavioural Phenotype | ORGANISM | PMID:41537560, PMID:39835750 |

**Module conformance:** No existing dismech module is a good fit. `epilepsy_excitation_inhibition_imbalance` is a *partial* fit at the seizure node only (`epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`) — the KDM1A/KDM5C ion-channel and CA1-excitability data (PMID:40864554) and the neuron-specific fly seizure result (PMID:41537560) support conformance there. Do **not** force-fit any degeneration, fibrosis, or storage module. Consider proposing a new `chromatin_h3k4_writer_eraser_imbalance` module (see §6.7).

**Recommended `discussions` entries:**
- `KNOWLEDGE_GAP` — no single-cell or spatial transcriptomic data despite strong region-specificity (amygdala ≫ cortex) in mouse; `proposed_experiments`: snRNA-seq of human post-mortem or iPSC-derived cortical/amygdalar tissue.
- `KNOWLEDGE_GAP` — no iPSC/cerebral organoid model; the WNT critical-window mechanism cannot be tested in human tissue without one.
- `KNOWLEDGE_GAP` — no validated QoL instrument, no survival/mortality data, no adult natural-history cohort (RARE-X max age 20 y).
- `KNOWLEDGE_GAP` — XCI skewing does not reliably explain the female phenotype spectrum, and KDM5C escapes XCI; the determinant of female severity is unknown.
- `HUMAN_MODEL_MISMATCH` — mouse Kdm5c-KO shows **reduced** anxiety-like behaviour whereas 71% of humans have anxiety; and the mouse does **not** seize despite 35–48% human epilepsy (seizures required a *Drosophila* model). Both are direction/presence mismatches, not absent evidence.
- `HUMAN_MODEL_MISMATCH` — the *Drosophila* ribosome/translation deficit (PMID:29490272) and the zebrafish interferon/TLR signature (PMID:41743791) have no demonstrated human correlate.

**Do not curate as established:** the TLR/interferon therapeutic axis (zebrafish, n=1 study); the "missense = milder than nonsense" genotype–phenotype rule (contradicted by R1115H and D87G); episignature 100% sensitivity (training-cohort figure, n=7, with PMID:37872275 as the counterweight); post-viral regression as a disease feature (single case).