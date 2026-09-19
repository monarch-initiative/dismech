---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T22:38:44.295681'
end_time: '2026-07-31T23:03:33.819594'
duration_seconds: 1489.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: USP9X Female-Restricted Syndromic Intellectual Disability
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
  web_search_requests: 4
  num_turns: 106
  total_cost_usd: 10.566881250000002
  session_id: 222d403a-0637-4e9b-84e5-e6534910d7b6
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** USP9X Female-Restricted Syndromic Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **USP9X Female-Restricted Syndromic Intellectual Disability** covering all of the
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

# Comprehensive Research Report
## USP9X Female-Restricted Syndromic Intellectual Disability (MRXS99F / USP9X-female syndrome)

**Compiled:** 31 July 2026
**Intended use:** population of a dismech LinkML `Disease` knowledge-base entry

---

### ⚠️ Provenance and verification notes (read first)

1. **Named Entity Confusion (NEC) preflight — PASSED.** The MONDO record for the target disease explicitly names the causal gene: MONDO:0010502 is defined as *"Any X-linked syndromic intellectual disability in which the cause of the disease is a mutation in the USP9X gene"*, with `OMIM:300968` as its cross-reference. The dominant gene in the retrieved literature (USP9X) matches the MONDO/OMIM anchor. No synonym aliasing or eponymic collision was detected. Note, however, that this disease **does** sit in a moderate-NEC-risk class (a numbered XLID series, MRX99 vs. MRXS99F, differing only by the "S" and by sex-restriction) — see §1.4.
2. **Snippet fidelity.** Quotations marked **[VERBATIM]** were extracted either from the repository's `references_cache/` files (created by `linkml-reference-validator`) or from raw NCBI E-utilities `efetch` output and are exact abstract substrings. Quotations marked **[PARAPHRASE — DO NOT USE AS SNIPPET]** came back through a summarizing fetch layer and **must be re-fetched with `just fetch-reference PMID:XXXX` and re-verified** before being committed as evidence.
3. **PubMed MCP tooling was unavailable** (permission not granted in this session); all literature retrieval used NCBI E-utilities and the local reference cache.
4. **Orphanet's website is bot-blocked**; Orphanet data below came from the `api.orphadata.com` REST endpoints and the OLS MONDO mapping, not from a cached `ORPHA_480880.md` (no such cache file exists in this repo yet — it would need `just structured-rebuild-orphanet --id 480880`).

---

## 1. Disease Information

### 1.1 Concise overview

Female-restricted X-linked syndromic intellectual developmental disorder-99 (**MRXS99F**), also widely called **USP9X-female syndrome**, is an ultra-rare, clinically recognizable X-linked *dominant* neurodevelopmental malformation syndrome caused by heterozygous loss of function of the deubiquitylating enzyme gene **USP9X** at Xp11.4. It is defined by the near-universal combination of developmental delay/intellectual disability with a characteristic constellation of congenital malformations — choanal atresia, anal atresia, postaxial polydactyly, cardiac defects, cleft palate/bifid uvula, asymmetric hypomastia, progressive scoliosis, hip dysplasia — plus structural brain abnormalities (hypoplastic/absent corpus callosum, ventriculomegaly, Dandy-Walker spectrum, cerebellar hypoplasia), short stature, recognizable facial dysmorphism, hearing loss, dental anomalies, and pigmentary changes along the lines of Blaschko with body asymmetry.

The syndrome is mechanistically unusual among X-linked disorders: **USP9X escapes X-chromosome inactivation**, so a heterozygous null allele is *not* rescued by the second X, producing true haploinsufficiency in females; conversely, complete hemizygous LOF in males is believed to be embryonic-lethal, which is why the LOF phenotype is female-restricted.

> **[VERBATIM — PMID:26833328, Reijnders et al. 2016, Am J Hum Genet]**
> "Here, we report 17 females with de novo loss-of-function mutations in USP9X, encoding a highly conserved deubiquitinating enzyme. The females in our study have a specific phenotype that includes ID/developmental delay (DD), characteristic facial features, short stature, and distinct congenital malformations comprising choanal atresia, anal abnormalities, post-axial polydactyly, heart defects, hypomastia, cleft palate/bifid uvula, progressive scoliosis, and structural brain abnormalities."

> **[VERBATIM — PMID:40751225, da Silva Campos et al. 2025, J Med Case Rep]**
> "Female-restricted X-linked syndromic intellectual developmental disorder-99 is an ultrarare neurodevelopmental disorder linked to X, manifesting in female individuals due to mutations in the USP9X gene. It is characterized by developmental delays, behavioral alterations, and moderate-to-severe intellectual disability. The USP9X gene plays critical roles in protein turnover and the regulation of essential pathways during neural development."

### 1.2 Key identifiers

| Resource | Identifier | Label / notes |
|---|---|---|
| **MONDO (primary)** | `MONDO:0010502` | "Intellectual disability, X-linked 99, syndromic, female-restricted" — **not obsolete**; OMIM-derived branch |
| MONDO (Orphanet branch) | `MONDO:0018821` | "X-linked female restricted facial dysmorphism-short stature-choanal atresia-intellectual disability" — **note: MONDO currently carries two un-merged terms for this entity; flag as an upstream MONDO issue** |
| OMIM (disease) | `OMIM:300968` | INTELLECTUAL DEVELOPMENTAL DISORDER, X-LINKED 99, SYNDROMIC, FEMALE-RESTRICTED; MRXS99F |
| OMIM (gene) | `OMIM:300072` | UBIQUITIN-SPECIFIC PROTEASE 9, X-LINKED; USP9X |
| Orphanet | `ORPHA:480880` | Exact mapping to OMIM:300968; disease type = "Malformation syndrome" |
| DOID | `DOID:0112025` | female-restricted syndromic X-linked intellectual disability 99 |
| UMLS | `C4225416` (OMIM branch); `C5567523` (Orphanet branch) | |
| MedGen | `899839` / CUI `C4225416` | |
| GARD | `0024732` (OMIM branch); `0013638` (Orphanet branch) | |
| ICD-10 | `Q87.8` | *"Narrower than targeted code"* per Orphanet — i.e., a non-specific bucket ("Other specified congenital malformation syndromes"), **not** a dedicated code |
| ICD-11 | **None assigned** (no ICD-11 reference in the Orphanet cross-reference record) | |
| MeSH | **No dedicated descriptor**; indexed via *Intellectual Disability*, *X-Linked Intellectual Disability*, *Ubiquitin Thiolesterase* | |
| HGNC | `hgnc:12632` | USP9X (note dismech lowercase-prefix convention) |
| Ensembl / NCBI Gene / UniProt | `ENSG00000124486` / `8239` / `Q93008` | |

### 1.3 Synonyms and alternative names

- USP9X-female syndrome (the preferred name in the primary functional-genetics literature; Jolly et al. 2020)
- MRXS99F (abbreviation)
- Intellectual developmental disorder, X-linked 99, syndromic, female-restricted
- Mental retardation, X-linked 99, syndromic, female-restricted *(historic/discouraged)*
- USP9X X-linked syndromic intellectual disability
- X-linked female restricted facial dysmorphism–short stature–choanal atresia–intellectual disability syndrome (Orphanet phrasing)
- Female-specific syndromic intellectual disability due to USP9X
- USP9X-related syndrome / USP9X-related disorders (patient-organization and Simons Searchlight usage; note this umbrella term covers **both** the female and male presentations)

### 1.4 ⚠️ Critical disambiguation (NEC risk)

Three closely related entities are frequently conflated and must be kept distinct in the KB:

| Entity | OMIM | Sex | Variant class | Notes |
|---|---|---|---|---|
| **MRXS99F** (this entry) | #300968 | Females (heterozygous) | Complete LOF (deletion, nonsense, frameshift) *and* pathogenic missense/single-aa deletion | Syndromic, multi-organ malformations |
| **MRX99 / XLID99** | #300919 | Males (hemizygous) | Partial-LOF missense; one C-terminal truncating allele in the historic MRX99 family | Neurological-predominant; *few* congenital malformations |
| USP9X as cancer gene | — | — | Somatic | Tumor suppressor **and** oncogene depending on context; do not import cancer literature into the NDD pathograph without care |

**Documented literature error to avoid propagating:** Li et al. 2022 (PMID:35253988) writes *"female-specific syndromic ID (MIM 300969, also known as MRX99F)"* — **300969 is incorrect**; the correct OMIM number is **300968**, and the correct abbreviation is **MRXS99F**.

### 1.5 Data derivation

All disease-level information here is **aggregated from published case series and case reports** (n≈35 well-phenotyped females as of the 2020 aggregate; ≥110 individuals with USP9X-related syndrome overall as of 2024 per the Simons Searchlight registry) plus curated disease-level resources (OMIM, Orphanet, HPO annotations, ClinGen, ClinVar, DECIPHER). **No EHR-derived or population-cohort dataset exists** for this disorder. The Simons Searchlight registry (NCT01238250, recruiting) is the only prospective individual-level natural-history data collection that includes USP9X.

---

## 2. Etiology

### 2.1 Disease causal factors

**Monogenic, genetic, non-infectious, non-environmental.** The sole established cause is a heterozygous pathogenic variant in `USP9X` (Xp11.4) in a 46,XX individual. Causality operates through **haploinsufficiency**: because USP9X escapes X-inactivation, the wild-type allele on the inactive X cannot compensate for dosage loss.

> **[VERBATIM — PMID:40751225]**
> "The mutation leads to protein function loss due to haploinsufficiency, resulting in a dominant X-linked disorder."

> **[VERBATIM — PMID:33298948, Jolly et al. 2020, npj Genom Med]**
> "USP9X is an X-chromosome gene that escapes X-inactivation. Loss or compromised function of USP9X leads to neurodevelopmental disorders in males and females. While males are impacted primarily by hemizygous partial loss-of-function missense variants, in females de novo heterozygous complete loss-of-function mutations predominate, and give rise to the clinically recognisable USP9X-female syndrome."

The reason the syndrome is *female-restricted* is a lethality filter, not a dosage-compensation effect:

> **[VERBATIM — Jolly et al. 2020, full text, PMID:33298948]**
> "Males with such LOF mutations are unlikely to survive early stages post fertilisation".

Corroborated independently:

> **[VERBATIM — PMID:40751225, full text]**
> "Loss-of-function variants in male individuals have never been reported, as it is believed that total loss of protein function is incompatible with life".

### 2.2 Risk factors

**Genetic risk factors**
- *Causal:* de novo heterozygous LOF (whole/partial gene deletion, nonsense, frameshift, canonical splice) in USP9X. Also de novo pathogenic missense and single-amino-acid in-frame deletions, predominantly within the UCH catalytic domain (see §4).
- *Constraint context (why de novo LOF is deleterious):*
  > **[VERBATIM — Jolly et al. 2020, full text, PMID:33298948]**
  > "It is ranked among the top 5% of evolutionary constrained genes and is highly intolerant to variation (pLI = 1.0; z-score = 6.35)... It is essential for embryonic viability."
- *Chromosomal:* structural rearrangements disrupting USP9X. Au et al. 2017 (PMID:28377321) report a de novo pericentric X inversion whose breakpoint deleted the USP9X 5′UTR.
- *Modifier genes:* **none identified.** Li et al. 2022 (PMID:35253988) explicitly searched and failed:
  > **[VERBATIM — PMID:35253988]**
  > "To investigate the possible genetic etiology of the reduced penetrance, X-inactivation, RNA-Seq, and full quad exome analyses were attempted, but failed to identify a promising candidate modifier."
- *Second-hit confound to be aware of:* Homan et al. 2014 (PMID:24607389) found one USP9X-variant proband also carried an ARID1B microdeletion — **[VERBATIM]** *"Given our findings it is plausible that loss of function of both genes contributes to the individual's phenotype."*

**Environmental risk factors**
- **None known.** No toxin, teratogen, infection, occupational exposure, maternal-age, or lifestyle association has been reported. Advanced paternal age is a generic risk factor for de novo point mutations across NDDs but has not been specifically studied in USP9X.
- **Female sex is a phenotype-defining "risk factor"** only in the trivial sense that the LOF genotype is male-lethal.
- **Family history is usually absent** (de novo in ~95% of cases; see §9).

### 2.3 Protective factors

- **No genetic or environmental protective factors are established.**
- Two theoretically protective mechanisms have been *considered and largely rejected or left unresolved*:
  - *Skewed X-inactivation favouring the mutant allele.* Reijnders et al. found skewing >90% in 3/5 tested females, but **"skewing was not related to disease severity."** [PARAPHRASE from PMC4746365 — verify] Jolly et al. note this is confounded because USP9X escapes XCI in the first place, and blood/skin XCI may not reflect brain XCI (the PCDH19 precedent).
  - *Turner-syndrome analogy argues against simple gene-dosage rescue:*
    > **[VERBATIM — Jolly et al. 2020, full text]**
    > "Furthermore, a haploinsufficiency-like mechanism of USP9X-female NDD is not supported by e.g. phenotypes observed in Turner Syndrome with XO sex chromosome karyotype, which generally lack neurological manifestations."
  - *Interindividual variation in nonsense-mediated decay / transcriptional compensation* was proposed by Jolly et al. as a candidate penetrance modifier but is untested.
- The one documented case of **non-penetrance** (Li et al. 2022 — an asymptomatic transmitting mother and two affected non-twin sisters) and the mildly-affected transmitting mother of "Female 31" in Jolly et al. (history of scoliosis and partial hearing impairment only) prove that protective modification *exists* but is unidentified. This is a genuine **KNOWLEDGE_GAP** for the dismech entry.

### 2.4 Gene–environment interactions

**None reported.** No GxE data exist for USP9X. This should be recorded as "not applicable / no evidence" rather than left implicitly blank.

---

## 3. Phenotypes

### 3.1 HPO-annotated phenotype set with frequencies

The table below is the **complete curated HPO annotation set** for `OMIM:300968`, retrieved from the HPO annotation API (`ontology.jax.org/api/network/annotation/OMIM:300968`). Fractional frequencies derive from the Reijnders et al. 2016 cohort of 17 females (PMID:26833328). Denominators vary (e.g., x/11, x/13) because brain imaging and some assessments were not performed in all individuals — **preserve these denominators; do not renormalize to /17.**

| HPO ID | Term | Frequency (n/N) | % | Suggested `FrequencyEnum` | Category |
|---|---|---|---|---|---|
| HP:0001263 | Global developmental delay | 17/17 | 100% | OBLIGATE / VERY_FREQUENT | Nervous |
| HP:0001249 | Intellectual disability | — (100% where assessed) | ~100% | VERY_FREQUENT | Nervous |
| HP:0000750 | Delayed speech and language development | — | high | VERY_FREQUENT | Nervous |
| HP:0002079 | Hypoplasia of the corpus callosum | 8/13 | 62% | FREQUENT | Nervous |
| HP:0002119 | Ventriculomegaly | 8/11 | 73% | FREQUENT | Nervous |
| HP:0001321 | Cerebellar hypoplasia | 6/11 | 55% | FREQUENT | Nervous |
| HP:0002536 | Abnormal cortical gyration | 5/10 | 50% | FREQUENT | Nervous |
| HP:0001305 | Dandy-Walker malformation | 5/13 | 38% | OCCASIONAL–FREQUENT | Head/neck |
| HP:0001250 | Seizure | 4/17 | 24% | OCCASIONAL | Nervous |
| HP:0001290 | Generalized hypotonia | 8/17 | 47% | FREQUENT | Musculature |
| HP:0002650 | Scoliosis | 11/17 | 65% | FREQUENT | Skeletal |
| HP:0001385 | Hip dysplasia | 8/17 | 47% | FREQUENT | Skeletal |
| HP:0002827 | Hip dislocation | — | — | OCCASIONAL | Limbs |
| HP:0000365 | Hearing impairment | 11/17 | 65% | FREQUENT | Ear |
| HP:0002023 | Anal atresia | 9/17 | 53% | FREQUENT | Digestive |
| HP:0100259 | Postaxial polydactyly | 9/17 | 53% | FREQUENT | Limbs |
| HP:0000453 | Choanal atresia | 6/17 | 35% | OCCASIONAL–FREQUENT | Head/neck |
| HP:0002205 | Recurrent respiratory infections | 9/17 | 53% | FREQUENT | Immunology |
| HP:0100559 | Lower limb asymmetry | 7/17 | 41% | FREQUENT | Limbs |
| HP:0012813 | Unilateral breast hypoplasia (hypomastia) | 5/17 | 29% | OCCASIONAL | Breast |
| HP:0000193 | Bifid uvula | 5/17 | 29% | OCCASIONAL | Head/neck |
| HP:0000175 | Cleft palate | — (part of the 29% cleft palate/bifid uvula group) | — | OCCASIONAL | Head/neck |
| HP:0002926 | Abnormality of thyroid physiology | 6/17 | 35% | OCCASIONAL–FREQUENT | Endocrine |
| HP:0000998 | Hypertrichosis | 5/17 | 29% | OCCASIONAL | Skin |
| HP:0000960 | Sacral dimple | 5/17 | 29% | OCCASIONAL | Skin |
| HP:0004322 | Short stature | 9/17 | 53% | FREQUENT | Growth |
| HP:0000164 | Abnormality of the dentition | ~71% (per Reijnders re-analysis) | 71% | FREQUENT | Head/neck |
| HP:0001631 | Atrial septal defect | — | (heart defects 7/16 = 44% overall) | OCCASIONAL | Cardiovascular |
| HP:0001643 | Patent ductus arteriosus | — | | OCCASIONAL | Cardiovascular |
| HP:0000110 | Renal dysplasia | — | | OCCASIONAL | GU |
| HP:0000126 | Hydronephrosis | — | | OCCASIONAL | GU |
| HP:0011968 | Feeding difficulties | — | | FREQUENT | Digestive |
| HP:0002098 | Respiratory distress | — | | OCCASIONAL | Respiratory |
| HP:0001382 | Joint hypermobility | — | | OCCASIONAL | Other |
| HP:0000324 | Facial asymmetry | — | | OCCASIONAL | Head/neck |

**Facial/craniofacial dysmorphism cluster** (HPO IDs verified in the same annotation set): HP:0000601 Hypotelorism · HP:0000248 Brachycephaly · HP:0000341 Narrow forehead · HP:0011220 Prominent forehead · HP:0000319 Smooth philtrum · HP:0000343 Long philtrum · HP:0000431 Wide nasal bridge · HP:0005280 Depressed nasal bridge · HP:0000414 Bulbous nose · HP:0000448 Prominent nose · HP:0012745 Short palpebral fissure · HP:0000369 Low-set ears · HP:0000358 Posteriorly rotated ears.

**Ocular cluster:** HP:0000486 Strabismus · HP:0000545 Myopia · HP:0000540 Hypermetropia · HP:0000483 Astigmatism · HP:0000518 Cataract.

**Limb/extremity cluster:** HP:0001182 Tapered finger · HP:0200055 Small hand · HP:0001773 Short foot · HP:0001761 Pes cavus.

**Inheritance annotation:** HP:0001423 X-linked dominant inheritance.

### 3.2 Reijnders 2016 cohort frequencies as re-reported in a secondary source

The 2025 Brazilian case report reproduces the Reijnders frequencies in percentage form; these agree with, and slightly extend, the HPO fractions:

> **[VERBATIM — PMID:40751225, full text]**
> "Reijnders et al. [16] described the phenotypes of 17 patients carrying de novo LOF variants in USP9X. Some phenotypes observed in our patient were cited in the majority of the study's patients, such as: intellectual disability or developmental delay (100% of cases), enlarged ventricles (73%), dental abnormalities (71%), scoliosis (65%), pigmentary abnormalities along Blaschko's lines (65%), hypoplastic corpus callosum (62%), ocular abnormalities (59%), short stature (53%), hip dysplasia (47%), hypotonia (47%), and leg length discrepancy (41%)."

Note this source supplies two features **absent from the HPO annotation set** and worth curating explicitly:
- **Pigmentary abnormalities along Blaschko's lines — 65%.** Suggested term: `HP:0011356` (Abnormality of skin pigmentation along Blaschko lines) — *verify with `just validate-terms` before commit; I did not confirm this ID against OAK in this session.*
- **Leg length discrepancy — 41%** (captured in HPO as HP:0100559 Lower limb asymmetry, 7/17 = 41%; consistent).

### 3.3 Phenotype characteristics

**Age of onset.** Congenital to neonatal for structural malformations (choanal atresia, anal atresia, polydactyly, cleft palate, heart defects are present at birth and often prompt neonatal surgery). Neurodevelopmental features declare in infancy — the Brazilian proband was diagnosed with "nonprogressive encephalopathy" at 8 months. Prenatal detection is possible: Lenberg et al. 2019 (PMID:30997057) detected a USP9X variant in a fetus with isolated agenesis of the corpus callosum on prenatal ultrasound + WES, and Jolly et al.'s "Female 31" was ascertained on genetic autopsy of a terminated fetus with brain, heart and skeletal malformations. Suggested HPO onset: `HP:0003577` Congenital onset / `HP:0003623` Neonatal onset.

**Severity.** Variable. OMIM/MedGen describe the core as *"delayed psychomotor development and mild to moderate intellectual disability"*; the 2025 case-report literature describes *"moderate-to-severe intellectual disability."* The 2020 aggregate cohort makes the spread explicit:
> **[VERBATIM — Jolly et al. 2020, full text]**
> "Intellectual disability (ID) was present in all individuals where assessed, but was variable, ranging from borderline to severe. All individuals displayed problems with speech and language, the severity of which was also across a wide spectrum, ranging from somewhat innocuous delay through to complete absence."

The extremes are well documented within a single paper: Female 30 (de novo p.Trp380Ter) had *"severe ID, absent speech and severe motor disability"*, whereas Female 32 (de novo p.Ile535Asnfs*11) had *"only slight delays in speech, language and motor skills, and is now largely meeting developmental milestones."* **[VERBATIM]** This intra-syndromic range should be modelled as high variable expressivity, not as subtypes.

**Progression.** The **CNS phenotype is static (non-progressive encephalopathy)**, not neurodegenerative. Two features are explicitly **progressive**:
- **Scoliosis** — described as "progressive scoliosis" in the defining Reijnders abstract **[VERBATIM]**. Use `clinical_course: PROGRESSIVE`.
- **Hip dysplasia/dislocation and limb-length discrepancy**, which worsen with growth and drive orthopaedic surgery.
Seizures, when present (~24%), are episodic. Recurrent respiratory infections (53%) are recurrent/episodic — use `temporality: RECURRENT`.

**Quality-of-life impact (per-phenotype).**
No disease-specific QoL instrument (EQ-5D, PROMIS, SF-36) has been applied to MRXS99F; **no published QoL data exist**. Functional impact must be inferred from case-level description, which is substantial:
- *Global developmental delay + absent speech + non-ambulation* → total dependence for activities of daily living. The Brazilian proband, at 6 years: *"The child exhibited delay in all her pediatric developmental milestones and some were never acquired, such as speech and walking, and she is totally dependent for her activities of daily living."* **[VERBATIM — PMID:40751225]**
- *Motor disability* required "standing supports or wheel chairs" in 2/12 individuals in the missense cohort **[VERBATIM — Jolly 2020]**.
- *Hearing loss (65%)* compounds the speech/language deficit — a high-yield, remediable contributor.
- *Choanal atresia / anal atresia / heart defects* → neonatal surgical burden and ICU admission; one heart defect caused neonatal lethality (Female 23, Jolly 2020).
- *Scoliosis, hip dysplasia, foot deformity* → repeated orthopaedic surgery; the Brazilian proband had corrective surgery for cavovarus equinovarus feet at 4 years.
- *Behavioural disturbance* — "autism, anxiety and aggression" **[VERBATIM — Jolly 2020]** — a major family-burden driver.

**Cellular/laboratory phenotype (`category: Cellular` in dismech terms).** Patient-derived fibroblasts show reduced USP9X at both transcript and protein level, a directly citable functional readout:
> **[VERBATIM — PMID:26833328]**
> "Expression studies on both mRNA and protein level in affected-female-derived fibroblasts showed significant reduction of USP9X level, confirming the loss-of-function effect of the identified mutations."
Suggested `evidence_source: IN_VITRO` for this item.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Field | Value |
|---|---|
| Symbol | **USP9X** |
| Name | ubiquitin specific peptidase 9 X-linked |
| HGNC | `hgnc:12632` |
| Location | **Xp11.4** |
| Ensembl | ENSG00000124486 |
| NCBI Gene | 8239 |
| UniProt | **Q93008**, Ubiquitin carboxyl-terminal hydrolase 9X, **2,554 aa** |
| Gene OMIM | *300072 |
| Aliases | DFFRX, FAF, FAF-X, MRX99 |
| Previous symbols | "ubiquitin specific protease 9, X chromosome (fat facets-like Drosophila)" and variants |
| Canonical transcripts used in reports | NM_001039590.2, NM_001039591.3, ENST00000378308 |

**Protein architecture (UniProt Q93008):** USP (ubiquitin-specific protease) catalytic domain spans **residues 1557–1956**; catalytic nucleophile **Cys-1566**; proton acceptor **His-1879**; zinc-coordinating **Cys-1727 / His-1729**. Subcellular localization: cytoplasm/cytosol; **cell projection, growth cone**; **cytoplasm, cytoskeleton, cilium axoneme**; centrosome. Tissue specificity: "Widely expressed in embryonic and adult tissues."

### 4.2 Pathogenic variants

**Variant classes causing MRXS99F (in descending frequency):**
1. **Whole- or partial-gene deletions** (detectable by CMA/aCGH)
2. **Nonsense** (e.g., p.Trp380Ter, p.Arg215Ter, **p.Gln2386*** [c.7156C>T])
3. **Frameshift** (e.g., p.Arg1368Serfs*2 [c.4104_4105del], p.Ile535Asnfs*11, p.Lys296Serfs*4 [c.885_889delAAAAG], p.Thr1364Lysfs*7 [c.4091delinsAG])
4. **Canonical splice-site** (e.g., NM_001039591.3:c.2877+2T>C, in ClinVar under this condition)
5. **Missense and single-amino-acid in-frame deletions** — a genuine, later-recognized contribution
6. **Structural rearrangement** disrupting the locus (de novo pericentric X inversion removing the 5′UTR; Au et al. 2017)

Reijnders' original 17: **"12 of the 13 point mutations resulting in truncated proteins"**, i.e., predominantly protein-truncating, plus deletions, plus a single de novo missense in the catalytic domain.

**Missense contribution — the 2020 expansion:**
> **[VERBATIM — PMID:33298948]**
> "Here we provide evidence of the contribution of USP9X missense and small in-frame deletion variants in USP9X-female syndrome also. We scrutinise the pathogenicity of eleven such variants, ten of which were novel. Combined application of variant prediction algorithms, protein structure modelling, and assessment under clinically relevant guidelines universally support their pathogenicity."

**Structure-based mechanism for the catalytic-domain missense/in-frame variants** (Jolly 2020, full text, all **[VERBATIM]**):
| Variant | Predicted structural consequence |
|---|---|
| p.Tyr1881del (Female 29) | "contributes to a beta-sheet critical for the positioning of the UCH catalytic triad… predicted to alter the position of the catalytic residue p.His1879 and likely to have significant effects on catalytic activity" |
| p.Tyr1802Ser (Female 28) | disrupts "the hydrophobic surface involved in ubiquitin binding via interaction with the p.Ile36 residue of ubiquitin" |
| p.Asp1685Asn (Female 27) | "charge reversal… predicted to alter the intramolecular charge–charge interaction with p.Gln1796, and as such constrict the ubiquitin binding channel" |
| p.Leu1693Trp (Female 8) | "introduces a highly bulky tryptophan predicted to disrupt the local hydrophobic core" |
| p.Glu1764Lys (Female 33) | "lies within the zinc finger motif of the catalytic domain, which forms multiple contacts with ubiquitin and is integral to the catalytic activity" |

Summary conclusion: **[VERBATIM]** *"structural modelling of the all likely pathogenic USP9X-female variants located in the catalytic domain provides rationale for disrupted catalytic activity and/or ubiquitin binding."*

**Variants in the N-terminal region** (of largely undetermined function) are proposed to disrupt only *subsets* of substrates — the same partial-LOF logic that explains the milder male phenotype.

**Variant classification (ACMG/AMP).** All 11 missense/in-frame variants in Jolly 2020 were classified likely pathogenic under ACMG guidelines. ClinGen has curated the gene but not individual variants.

**Allele frequency.** All pathogenic alleles are **absent from population databases** (gnomAD, 1000G). The Brazilian c.7156C>T was novel in both ClinVar and DECIPHER at the time of report. gnomAD carries no USP9X LOF alleles at appreciable frequency — consistent with pLI = 1.0.

**Somatic vs. germline.** All MRXS99F-causing variants are **germline** (de novo or, rarely, maternally transmitted / maternal gonosomal-mosaic). Somatic USP9X mutations occur in cancer (COSMIC) and are enriched for LOF — Jolly et al. explicitly note that predicted-deleterious COSMIC variants cluster in the same catalytic-domain positions, and that "childhood malignancy has been reported in two female individuals with USP9X-female syndrome… and could potentially be involved in the natural course of the condition." **[VERBATIM]** This is a clinically actionable, under-recognized surveillance question.

**Functional consequence.** **Loss of function / haploinsufficiency.** For catalytic-domain missense, whether residual activity persists or a dominant-negative effect operates is **unresolved**:
> **[VERBATIM — Jolly 2020]**
> "It is yet to be determined as to whether these missense variants retain residual USP9X function or act as dominant negative alleles."
→ Curate as a dismech `discussions` entry with `kind: KNOWLEDGE_GAP`.

**ClinVar volume (queried 31 Jul 2026, E-utilities):** **1,770 total USP9X records**, of which **281 are Pathogenic or Likely Pathogenic**. (For comparison, the 2025 case report counted 990 total / 244 P+LP as of Nov 2024 — the locus is accruing submissions rapidly.)

**DECIPHER (as of Dec 2024, per PMID:40751225 full text) — [VERBATIM]:** *"we found 129 patients with variants in the USP9X gene, 31 (24%) sequence variants, 71 (55%) copy-number variants, 26 (20.2%) chromosomal anomalies, and 1 (0.8%) uniparental disomy. Of the 31 sequence variants, 15 were present in female patients and only 3 variants were an amino acid substitution with a premature stop codon… No nonsense variants were found in male patients in DECIPHER."*

### 4.3 Gene-level constraint and dosage curation

| Metric | Value | Source |
|---|---|---|
| pLI | **1.0** | Jolly 2020 full text (PMID:33298948) |
| Missense z-score | **6.35** | *ibid.* |
| Evolutionary constraint rank | top 5% of genes | *ibid.* |
| **ClinGen Gene–Disease Validity** | **Definitive** — X-linked syndromic intellectual disability (MONDO:0020119), X-linked; Intellectual Disability and Autism GCEP; 17 Nov 2021 | ClinGen |
| **ClinGen Haploinsufficiency score** | **3 — Sufficient Evidence for Haploinsufficiency** (27 Nov 2024) | ClinGen |
| ClinGen Triplosensitivity | 0 — No Evidence (27 Nov 2024) | ClinGen |

⚠️ **Curation note:** ClinGen deliberately **lumps** the male and female presentations: *"The ID/Autism GCEP has decided to lump the MOIs together and curate both males (XL dominant) and females (XL recessive) together"* for a single disease entity. dismech, following OMIM/MONDO, **splits** them. Record this as an explicit lump-vs-split rationale on the entry; the ClinGen assertion is still valid supporting evidence for the gene–disease relationship, but its disease anchor (MONDO:0020119) is broader than MONDO:0010502.

To cite the ClinGen record in dismech, first materialize the caches:
```bash
just clingen-refresh && just clingen-rebuild            # then find the USP9X CGGV assertion id
just clingen-dosage-refresh && just clingen-dosage-rebuild --id CGDS:HGNC_12632
```

### 4.4 Modifier genes

**None identified** (see §2.2). Candidate mechanisms proposed but unproven: tissue-specific variation in XCI escape; interindividual NMD efficiency; transcriptional compensation; an independent second X-chromosome abnormality (the Fragile-X-carrier precedent).

### 4.5 Epigenetic information

- **XCI escape is the central epigenetic fact.** USP9X is a well-established XCI-escape gene. Tukiainen et al. 2017 (PMID:29022598, Nature) established the general landscape: **[VERBATIM]** *"up to one-third of X-chromosomal genes are expressed from both the active and inactive X chromosomes (Xa and Xi, respectively) in female cells, with the degree of 'escape' from inactivation varying between genes and individuals."*
- **Variable, tissue-specific escape is the proposed explanation for mosaic/asymmetric features** — pigment changes along Blaschko lines, breast asymmetry, limb-length discrepancy, asymmetric brain formation:
  > **[VERBATIM — PMID:26833328]** "In several females, pigment changes along Blaschko lines and body asymmetry were observed, which is probably related to differential (escape from) X-inactivation between tissues."
  > **[VERBATIM — Jolly 2020]** "Possible role for X-inactivation in USP9X-female NDDs is suggested by several frequently observed clinical features including mosaic skin pigmentations and asymmetries in brain formation, breast development, limb development and other structures."
- **No DNA-methylation episignature** has been published for USP9X. (Episignature panels exist for many NDD genes — USP9X is not currently among them. Worth flagging as a research gap.)
- No histone-modification or chromatin-state disease data specific to MRXS99F.

### 4.6 Chromosomal abnormalities

- Xp11.4 **deletions** encompassing USP9X (55% of DECIPHER USP9X-associated cases are CNVs).
- **De novo pericentric X inversion** with a breakpoint deleting the USP9X 5′UTR (Au et al. 2017, PMID:28377321).
- Karyotype is otherwise normal (46,XX). Incidental findings are common and can mislead: the Brazilian proband carried `46,XX,inv(9)(p12q13)` — a benign paternally inherited pericentric inversion 9 polymorphism that initially misdirected the diagnostic workup.

---

## 5. Environmental Information

- **Environmental factors:** none. No entry in CTD or TOXNET links any exposure to MRXS99F. The disorder is fully genetically determined.
- **Lifestyle factors:** none.
- **Infectious agents:** none causal. ⚠️ **Clinically important negative:** the phenotype **mimics congenital infection**, and the 2025 Brazilian case was initially misdiagnosed as congenital rubella/toxoplasmosis on the basis of positive neonatal IgG serology. **[VERBATIM — PMID:40751225]** *"In our patient, initial suspicions were of congenital rubella and/or toxoplasmosis syndrome, as the results for these infectious diseases were positive in the child after birth and in the mother."* This belongs in the differential-diagnosis section, not the etiology section.

---

## 6. Mechanism / Pathophysiology

### 6.1 Top-level causal chain

```
USP9X heterozygous LOF variant (de novo, 46,XX)
  ↓  [gene escapes XCI → no compensation from Xi allele]
USP9X protein haploinsufficiency (≈50% dosage) in all tissues
  ↓  [DUB activity lost → substrates no longer rescued from proteasome]
Coordinate destabilization of multiple USP9X substrates
  ↓
Convergent dysregulation of ≥4 developmental signalling pathways
  (TGF-β/BMP · mTORC1 · Notch · Wnt/β-catenin) + cytoskeletal/adhesion defects
  ↓
   ├─ CNS arm: impaired neural progenitor proliferation & polarity,
   │           aberrant neuronal migration, failed axon outgrowth
   │             → agenesis/hypoplasia of corpus callosum, ventriculomegaly,
   │               cerebellar hypoplasia, abnormal gyration, hippocampal defects
   │             → global developmental delay, ID, speech/motor deficits, ASD, seizures
   ├─ Craniofacial/skeletal arm (neural-crest & patterning dependent)
   │             → facial dysmorphism, cleft palate/bifid uvula, hypodontia,
   │               scoliosis, hip dysplasia, polydactyly
   ├─ Midline/organ-septation arm
   │             → choanal atresia, anal atresia, septal heart defects
   └─ Mosaic arm (variable, tissue-specific XCI escape)
                 → Blaschko-line pigmentary change, body/breast/limb asymmetry
```

### 6.2 Molecular function of USP9X

USP9X is a **substrate-specific cysteine-protease deubiquitylase (DUB)** of the USP family that removes K48-linked polyubiquitin (and monoubiquitin) from substrates, rescuing them from proteasomal degradation and thereby setting their steady-state abundance.

> **[VERBATIM — Jolly 2020, full text]**
> "USP9X functions to reverse the effects of protein ubiquitylation, a frequent post-translational modification that often culminates in protein degradation via the proteasome. USP9X thus protects many of its substrates from degradation, thereby increasing their abundance and hence function. Many USP9X substrates are encoded by genes involved in brain development and neurodevelopmental disorders (NDDs)."

The authoritative review is Murtaza, Jolly & Gecz 2015 (PMID:25672900), *"La FAM fatale: USP9X in development and disease"*:
> **[VERBATIM]** "The ubiquitin-specific protease 9X (USP9X/FAM) is a substrate-specific DUB, which displays an extraordinarily high level of sequence conservation from Drosophila to mammals. It is primarily the recent revelations of USP9X's pivotal role in human cancers, both as oncogene or tumour suppressor, in developmental disorders including intellectual disability, epilepsy, autism and developmental delay that has led to a subsequent re-examination of its molecular and cellular functions."

**Crucially, USP9X is a "hub" / point of convergence**, which is why one gene produces a multi-pathway, multi-organ syndrome:
> **[VERBATIM — PMID:33188399, Kasherman et al. 2021, Cereb Cortex]**
> "Recent research has focused on proteins that act as points of convergence for multiple factors, as these may provide greater insight into understanding the biology of neurodevelopmental disorders. USP9X, a deubiquitylating enzyme that regulates the stability of many ASD-related proteins, is one such point of convergence."

### 6.3 Pathway-by-pathway mechanism (upstream → downstream)

**(A) TGF-β / BMP signalling — SMAD4 monoubiquitination.** The most mechanistically direct and best-evidenced arm; the *only* arm with a confirmed united defect in patient-derived cells.

> **[VERBATIM — PMID:19135894, Dupont et al. 2009, Cell]**
> "By means of siRNA screen we identified FAM (USP9x), a deubiquitinase acting as essential and evolutionarily conserved component in TGFbeta and bone morphogenetic protein signaling. Smad4 is monoubiquitinated in lysine 519 in vivo, a modification that inhibits Smad4 by impeding association with phospho-Smad2. FAM reverts this negative modification, re-empowering Smad4 function."

Loss of USP9X → SMAD4-K519 stays monoubiquitinated → SMAD4 cannot partner phospho-SMAD2 → TGF-β/BMP transcriptional output collapses.
Confirmed in patient cells:
> **[VERBATIM — PMID:31443933, Johnson et al. 2020, Biol Psychiatry]**
> "using patient-derived cell lines, we show loss of only specific USP9X substrates that regulate neurodevelopmental signaling pathways and a united defect in transforming growth factor β signaling."

Confirmed in mouse brain:
> **[VERBATIM — PMID:23861879, Stegeman et al. 2013, PLoS One]**
> "Usp9x absence also led to dramatic reductions in axonal length, in vivo and in vitro, which could in part be explained by a failure in Tgf-β signaling."

GO: `GO:0007179` transforming growth factor beta receptor signaling pathway (modifier: DECREASED).

**(B) mTORC1 signalling — RAPTOR stabilization.** Governs neural progenitor cell-cycle entry.

> **[VERBATIM — PMID:28341829, Bridges et al. 2017, Sci Rep]**
> "Decreasing USP9X resulted in ReNcell VM cells arresting in G0 cell cycle phase, with a concomitant decrease in mTORC1 signalling, a major regulator of G0/G1 cell cycle progression. Decreased mTORC1 signalling was also observed in Usp9x-null neurospheres and embryonic mouse brains. Further analyses revealed, (i) the canonical mTORC1 protein, RAPTOR, physically associates with Usp9x in embryonic brains, (ii) RAPTOR protein level is directly proportional to USP9X… and, (iii) USP9X deubiquitlyating activity opposes the proteasomal degradation of RAPTOR… To our knowledge, USP9X is the first deubiquitylating enzyme shown to stabilize RAPTOR."

GO: `GO:0038202` TORC1 signaling (modifier: DECREASED).

**(C) Wnt/β-catenin and Notch — via the destruction complex, ITCH and NUMB.**

> **[VERBATIM — PMID:27181636, Premarathne et al. 2017, Sci Rep]**
> "Nestin-cre mediated ablation of Usp9x from embryonic neural progenitors in vivo resulted in a transient disruption of cell adhesion and apical-basal polarity and, an increased number and ectopic localisation of intermediate neural progenitors… levels of β-catenin protein, especially S33/S37/T41 phospho-β-catenin, were markedly increased in Usp9x -/Y embryonic cortices. Loss of Usp9x altered composition of the β-catenin destruction complex possibly impeding degradation of S33/S37/T41 phospho-β-catenin… Usp9x co-localized and associated with both Itch and Numb in embryonic neocortices. Loss of Usp9x led to decreased Itch and Numb levels, and a concomitant increase in levels of the Notch intracellular domain as well as, increased expression of the Notch target gene Hes5."

GO: `GO:0016055` Wnt signaling pathway; `GO:0007219` Notch signaling pathway (both DYSREGULATED; Notch output INCREASED).

Jolly et al. summarize the four-pathway convergence: **[VERBATIM]** *"These substrates are, however, critical specifically for the function of neurodevelopmental signalling pathways TGFβ, mTOR, Notch and Wnt, all of which have been shown to be deregulated in the developing brains of mice lacking Usp9x."*

**(D) Cytoskeleton, neuronal migration and growth cones — DCX and the microtubule apparatus.**

> **[VERBATIM — PMID:24607389, Homan et al. 2014, Am J Hum Genet]**
> "Loss of Usp9x causes reduction in both axonal growth and neuronal cell migration. Although overexpression of wild-type human USP9X rescued these defects, all three USP9X variants failed to rescue axonal growth, caused reduced USP9X protein localization in axonal growth cones, and (in 2/3 variants) failed to rescue neuronal cell migration… We also performed proteomics analysis of neurons from both the wild-type and Usp9x knockout embryos and identified disruption of the cytoskeleton as the main underlying consequence of the loss of Usp9x."

The DCX link is direct and long-established:
> **[VERBATIM — PMID:15607950, Friocourt et al. 2005, Mol Cell Neurosci]**
> "Here we show that DCX interacts with the ubiquitin-specific protease Drosophila fat facets related on X chromosome (DFFRX)… DCX interacts with a novel recognition domain in DFFRX, located outside of its catalytic site. We also show that DFFRX associates with microtubules at specific subcellular compartments, including those enriched in DCX."

DCX loss itself causes X-linked lissencephaly/subcortical band heterotopia — this is the mechanistic bridge to the cortical-gyration abnormalities (HP:0002536, 5/10) and to periventricular heterotopia reported in a USP9X male (PMID:36680497).

GO: `GO:0001764` neuron migration; `GO:0030426` growth cone (CC); `GO:0022038` corpus callosum development.

**(E) Primary cilium — a partially supported, explicitly caveated arm.** Reijnders et al. pursued this because the malformation profile (polydactyly, Dandy-Walker, renal, cardiac) reads like a ciliopathy:
> **[VERBATIM — PMID:26833328]**
> "Given that some features of affected females are also reported in known ciliopathy syndromes, we examined the role of USP9X in the primary cilium and found that endogenous USP9X localizes along the length of the ciliary axoneme, indicating that its loss of function could indeed disrupt cilium-regulated processes. **Absence of dysregulated ciliary parameters in affected female-derived fibroblasts, however, points toward spatiotemporal specificity of ciliary USP9X (dys-)function.**"

⚠️ **Curation guidance:** this is a *hypothesis*, not an established mechanism — the functional test in patient cells was **negative**. Model it as a `mechanistic_hypotheses` entry with `status: EMERGING`, and do **not** declare `conforms_to: ciliopathy_dysfunction#...` on the basis of localization alone. UniProt independently supports the localization annotation (cytoskeleton, cilium axoneme; `GO:0005930` axoneme).

**(F) Seizure arm — PRICKLE2 stabilization.** Relevant to the ~24% seizure frequency:
> **[VERBATIM — PMID:25763846, Paemka et al. 2015, PLoS Genet]**
> "PRICKLE and USP9X interact through their carboxy-termini; and USP9X de-ubiquitinates PRICKLE, protecting it from proteasomal degradation. In forebrain neurons of mice, USP9X deficiency reduced levels of Prickle2 protein… The seizure phenotype was suppressed in prickle mutant flies by the small-molecule USP9X inhibitor, Degrasyn/WP1130, or by reducing the dose of fat facets a USP9X orthologue. USP9X mutations were identified by resequencing a cohort of patients with epileptic encephalopathy… These findings demonstrate that USP9X inhibition can suppress prickle-mediated seizure activity, and that USP9X variants may predispose to seizures."

⚠️ **Direction-of-effect caution:** this paper shows *inhibiting* USP9X **suppresses** seizures in the *Prickle*-mutant fly. MRXS99F involves *reduced* USP9X. These are not straightforwardly reconcilable; curate carefully and do not imply that USP9X inhibitors would treat MRXS99F seizures.

### 6.4 Other substrates (context; mostly cancer-derived, use with care)

MCL1 (PMID:20023629, Nature — *"USP9X binds MCL1 and removes the Lys 48-linked polyubiquitin chains that normally mark MCL1 for proteasomal degradation"* **[VERBATIM]**); ITCH; FBW7 (PMID:29346117, JCI); LATS1/2-Hippo (PMID:28720576); AF-6/afadin; MARK4/AMPK; SMURF1; Survivin; TRRAP; MTH1; PLK1. These establish USP9X's breadth but are largely tumour-biology findings — include in the KB only where they illuminate the NDD mechanism.

### 6.5 Cellular processes

| Process | GO term (verified) | Direction |
|---|---|---|
| Protein deubiquitination | `GO:0016579` | DECREASED |
| Cysteine-type deubiquitinase activity (MF) | `GO:0004843` | DECREASED |
| TGF-β receptor signaling | `GO:0007179` | DECREASED |
| TORC1 signaling | `GO:0038202` | DECREASED |
| Notch signaling pathway | `GO:0007219` | INCREASED (NICD/Hes5 up) |
| Wnt signaling pathway | `GO:0016055` | DYSREGULATED |
| Neuron migration | `GO:0001764` | IMPAIRED |
| Corpus callosum development | `GO:0022038` | IMPAIRED |
| Axonogenesis | `GO:0007409` *(verify with OAK)* | IMPAIRED |
| Growth cone (CC) | `GO:0030426` | — |
| Axoneme (CC) | `GO:0005930` | — |
| Cell adhesion / apical-basal polarity | *(select specific GO terms with OAK)* | DISRUPTED |

### 6.6 Protein dysfunction

Three distinct molecular lesions produce the same disease:
1. **Absence of protein** (deletion, nonsense/frameshift with NMD) → pure dosage halving.
2. **Truncated protein lacking the C-terminal UCH domain** (e.g., p.Gln2386* truncates at aa 2386 of 2554, downstream of the 1557–1956 catalytic domain but removing the C-terminus) → likely destabilized/degraded.
3. **Catalytically impaired full-length protein** (catalytic-domain missense/in-frame del) → disrupted catalysis or ubiquitin binding, per structural modelling (§4.2).

No protein misfolding/aggregation mechanism is implicated.

### 6.7 Metabolic changes

**None established.** No inborn-error-of-metabolism phenotype; no metabolomic signature published. Endocrine involvement is limited to thyroid physiology abnormality (HP:0002926, 6/17 = 35%) — mechanism unknown.

### 6.8 Immune system involvement

**Not a primary immunological disorder.** Recurrent respiratory infections (9/17 = 53%) are the most plausibly **anatomical/mechanical** in origin (choanal atresia, cleft palate, hypotonia with aspiration risk, scoliosis-related restrictive lung disease) rather than immunodeficiency; no immunological workup abnormality has been systematically reported. USP9X does have documented roles in T-cell biology (Themis stabilization, PMID:28877990; TCR signalling) — relevant background, but **no reported immunodeficiency in MRXS99F patients**. Flag as a data gap: no cohort has systematically measured immunoglobulins or lymphocyte subsets.

### 6.9 Tissue damage mechanisms

**Not applicable in the classical sense** — MRXS99F is a **developmental (dysmorphogenetic) disorder, not a degenerative or injury-mediated one.** The pathology is failure of tissue *formation* (agenesis, atresia, hypoplasia, malsegmentation), not destruction of formed tissue. There is no oxidative-stress, ischaemia, fibrosis, or necrosis mechanism. The encephalopathy is explicitly described as **non-progressive**.

### 6.10 Molecular profiling

- **Transcriptomics:** RNA-Seq performed on the incomplete-penetrance family (Li et al. 2022) — **negative for a modifier**. Pathway analysis of transcriptomes from *Usp9x*−/Y embryonic mouse brains identified **Wnt signalling as significantly affected** (Premarathne 2017). No patient-brain transcriptome exists.
- **Proteomics:** Homan et al. 2014 performed proteomics on WT vs. *Usp9x*-KO embryonic mouse neurons; principal finding = cytoskeletal disruption. Johnson et al. 2020 used patient-derived cell lines to show loss of *specific* substrates. Kasherman and colleagues have pursued cell-type-specific proteomics of the Usp9x-null brain.
- **Metabolomics / lipidomics:** **none published.**
- **Epigenomics:** none (no episignature).
- **Single-cell / spatial transcriptomics:** **none published for USP9X disease models.** A clear opportunity.
- **Functional-genomics screens:** USP9X appears in DepMap and in the Dupont siRNA screen that discovered the TGF-β role. No disease-specific CRISPR screen.
- **Neuroimaging as a "profiling" modality:** diffusion-tensor MRI in forebrain-specific KO mice revealed *"deficits in all three major forebrain commissures, as well as long-range hypoconnectivity between cortical and subcortical regions"* **[VERBATIM — PMID:33188399]** — a directly translatable readout for human connectomics studies not yet performed.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary (directly affected, developmental origin):**
| Structure | UBERON (verified where noted) | Manifestation |
|---|---|---|
| Brain | `UBERON:0000955` | global |
| Corpus callosum | **`UBERON:0002336`** ✓ | hypoplasia (62%) / agenesis |
| Lateral (telencephalic) ventricle | **`UBERON:0002285`** ✓ (telencephalic ventricle) | ventriculomegaly (73%) |
| Cerebellum | `UBERON:0002037` *(verify)* | hypoplasia (55%); Dandy-Walker (38%) |
| Cerebral cortex | `UBERON:0000956` *(verify)* | abnormal gyration (50%) |
| Hippocampal formation | `UBERON:0002421` *(verify)* | incomplete hippocampal inversion (case-level); dentate gyrus defect in mouse |
| Posterior nasal aperture / choana | **`UBERON:0004771`** (posterior nasal aperture) or **`UBERON:0010425`** (internal naris) ✓ | choanal atresia (35%) |
| Anus / anal canal | `UBERON:0001245` *(verify)* | anal atresia (53%) |
| Heart (septa) | `UBERON:0000948` *(verify)* | ASD, VSD, PDA (44%) |
| Vertebral column | `UBERON:0002412` *(verify)* | progressive scoliosis (65%) |
| Hip joint | `UBERON:0001485` *(verify)* | dysplasia/dislocation (47%) |
| Autopod (hand/foot) | `UBERON:0002398` / `UBERON:0002387` *(verify)* | postaxial polydactyly (53%) |
| Palate | `UBERON:0001716` *(verify)* | cleft palate / bifid uvula (29%) |
| Mammary gland | `UBERON:0001911` *(verify)* | asymmetric hypomastia (29%) |
| Inner ear / auditory system | `UBERON:0001846` *(verify)* | hearing impairment (65%) |
| Tooth / dentition | `UBERON:0001091` *(verify)* | hypodontia, severe crowding (71%) |
| Skin | `UBERON:0002097` *(verify)* | Blaschko-line pigmentary change (65%), hypertrichosis |
| Kidney / urinary tract | `UBERON:0002113` *(verify)* | renal dysplasia, hydronephrosis, pelvicalyceal dilatation |
| Thyroid gland | `UBERON:0002046` *(verify)* | thyroid physiology abnormality (35%) |
| Eye | `UBERON:0000970` *(verify)* | strabismus, refractive error, cataract, optic nerve atrophy |

**Secondary / complications:** lung (restrictive disease from scoliosis; aspiration pneumonia), gastrointestinal tract (feeding difficulty, constipation), cornea (the Brazilian case had bilateral corneal ulceration requiring two transplants — secondary to reduced blink/lubrication).

**Body systems:** nervous, musculoskeletal, craniofacial, cardiovascular, respiratory, digestive, genitourinary, endocrine, integumentary, special senses (auditory + visual).

⚠️ Only the UBERON IDs marked ✓ were verified against OLS in this session; the remainder must be checked with `uv run runoak -i sqlite:obo:uberon info <ID>` or `just validate-terms` before commit.

### 7.2 Tissue and cell level

| Cell type | CL (verified where noted) | Evidence |
|---|---|---|
| Neural progenitor cell | **`CL:0011020`** ✓ | Bridges 2017 (mTORC1/proliferation); Premarathne 2017 (polarity, IPC ectopia) |
| Radial glial cell | **`CL:0000681`** ✓ (also `CL:0013000` forebrain radial glial cell) | apical-basal polarity disruption in Nestin-cre KO |
| Neuron | `CL:0000540` *(verify)* | axon growth, migration defects |
| Neuroblast | `CL:0000031` *(verify)* | reduced number & abnormal morphology in postnatal dentate gyrus (Oishi 2016, PMID:27181636 — *see note*) |
| Neural stem cell | `CL:0000047` *(verify)* | reduced in SGZ; paradoxically increased sphere-forming capacity |
| Cranial neural crest cell | `CL:0011012` neural crest cell *(verify)* | inferred from the craniofacial/palatal/dental phenotype — **mechanistically plausible but NOT directly demonstrated for USP9X; mark as inferred** |
| Skin fibroblast | `CL:0000057` *(verify)* | the patient-derived cell type used for USP9X expression and cilia studies |

Tissue types: **nervous tissue** (primary), **connective/skeletal**, **epithelial** (choanal, anal, palatal — all failures of epithelial-mesenchymal patterning/canalization).

### 7.3 Subcellular level

Per UniProt Q93008 + primary literature (GO CC terms):
- Cytosol (`GO:0005829`)
- **Growth cone** (`GO:0030426`) ✓ — pathogenic variants specifically reduce USP9X growth-cone localization (Homan 2014)
- Cytoskeleton / microtubules — DCX-associated
- **Ciliary axoneme** (`GO:0005930`) ✓
- Centrosome (`GO:0005813`)
- Not nuclear-restricted; acts on both cytoplasmic and nuclear-shuttling substrates (SMAD4)

### 7.4 Localization and lateralization

- **Brain lesions are midline-predominant and bilateral**: corpus callosum (the archetypal midline commissure), the cerebellar vermis (Dandy-Walker), the ventricular system. This midline emphasis is echoed by the peripheral midline defects — cleft palate/bifid uvula, choanal atresia, anal atresia, cardiac septal defects. **A "midline patterning failure" framing is well supported and would make a coherent pathophysiology node.**
- **Explicit asymmetry is a cardinal, diagnostically useful feature** and is attributed to mosaic XCI escape: Blaschko-line pigmentation, **unilateral** breast hypoplasia (HP:0012813), lower-limb asymmetry/leg-length discrepancy (7/17 = 41%), facial asymmetry (HP:0000324), and asymmetric brain formation. In one reported case the hip dislocation was explicitly **right-sided**.
- This coexistence of **bilateral midline defects + mosaic lateralized defects** is mechanistically informative and should be preserved in the entry rather than flattened.

---

## 8. Temporal Development

**Onset.**
- *Congenital / prenatal.* Structural malformations are present at birth. Prenatal ascertainment is documented twice: an isolated fetal agenesis of the corpus callosum leading to WES diagnosis (Lenberg 2019, PMID:30997057 — **[VERBATIM]** *"Whole-exome sequencing in a female fetus detected a USP9X variant… Isolated agenesis of the corpus callosum has not been reported in association with USP9X. Identifying this variant impacted management of the subsequent pregnancy."*), and a genetic autopsy of a terminated fetus with brain, heart and skeletal defects (Jolly 2020, Female 31).
- *Neonatal.* Choanal atresia and heart defects can cause immediate respiratory/cardiac compromise. In the Brazilian case: Apgar 0/4, three cardiopulmonary arrests on day 1, 28 days of NICU, septoplasty at 28 days.
- *Infancy.* Developmental delay recognized in the first year (formal diagnosis of non-progressive encephalopathy at 8 months in the index Brazilian case).
- HPO onset terms: `HP:0003577` Congenital onset (primary); `HP:0003623` Neonatal onset.
- Onset pattern: **chronic / congenital-static**, not acute or insidious.

**Progression.**
- **No formal staging system exists.** Do not invent one.
- **CNS: static.** "Nonprogressive encephalopathy." Cognition does not decline; developmental gains occur slowly and plateau at an individual-specific level.
- **Musculoskeletal: progressive.** "Progressive scoliosis" is in the disease-defining description; hip dysplasia and foot deformity worsen with growth and weight-bearing.
- **Rate:** slow; measured over years.
- **Course pattern:** chronic, lifelong, non-remitting. Seizures (when present) are episodic; respiratory infections recurrent.
- **Duration:** lifelong.

**Patterns.**
- **Remission:** none — no spontaneous or treatment-induced remission is possible; interventions are ameliorative.
- **Critical intervention windows:**
  - *Neonatal (days 0–30):* choanal atresia and duct-dependent/septal cardiac lesions are surgical emergencies; anal atresia requires early repair.
  - *Infancy–early childhood (0–3 y):* the window for early-intervention therapies and, importantly, **for hearing-loss identification and amplification** — with 65% hearing impairment and universal speech-language involvement, undetected hearing loss is a modifiable amplifier of the communication phenotype.
  - *Childhood–adolescence:* scoliosis surveillance and bracing/surgery during the growth spurt; hip surveillance.
  - *Ophthalmic:* early detection of refractive error/strabismus/cataract to prevent amblyopia; corneal protection where blink is impaired.
- **Reported age range of described individuals:** 2 years 7 months to 23 years (Reijnders 2016 cohort) — **no adult natural-history data beyond the third decade exist.**

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| Orphanet point prevalence class | **`<1 / 1,000,000`** worldwide | Orphadata (validated), sourced to PMID:26833328 |
| Orphanet cases/families | 17 (worldwide, at time of curation) | Orphadata |
| Published incidence estimate | **≈1 in 1,000,000 live births** | PMID:40751225 full text: *"an ultrarare neurodevelopmental disorder, with an estimated incidence of 1:1,000,000 live births, which manifest as a dominant X-linked trait"* **[VERBATIM]** |
| Well-phenotyped published females | **35** (23 LOF + 12 missense/in-frame) | Jolly 2020, PMID:33298948 |
| All USP9X-related syndrome (both sexes) identified | **≥110** as of 2024 | Simons Searchlight gene guide |
| Published males with P/LP variants | 16 (Jolly 2020 comparison) → later 167 assessed variants; 12 missense with strong pathogenicity evidence (Johnson 2020) | |
| **Incidence (new cases /100,000/yr)** | **Not established** | — |

**dismech `Prevalence` block suggestion:**
```yaml
prevalence:
- population: Worldwide
  measure_type: POINT_PREVALENCE
  prevalence_class: BELOW_1_IN_1000000
  rate_per_100000: 0.1          # upper bound of the <1/1,000,000 class
  notes: Orphanet worldwide point-prevalence class <1 / 1 000 000.
- population: Worldwide
  measure_type: BIRTH_PREVALENCE
  prevalence_class: BELOW_1_IN_1000000
  rate_per_100000: 0.1
  notes: >-
    Published estimate of ~1:1,000,000 live births (da Silva Campos et al. 2025).
    Note this is an estimate quoted in a case report, not a population study.
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  rate_per_100000: null
  notes: 35 well-phenotyped females aggregated by Jolly et al. 2020; >=110 individuals
    with USP9X-related syndrome (both sexes) in the Simons Searchlight registry as of 2024.
```
⚠️ These are almost certainly **underestimates**: the disorder was only delineated in 2016, ascertainment depends on exome/genome sequencing, and the mild end of the spectrum (Female 32, "largely meeting developmental milestones") is systematically under-diagnosed.

### 9.2 Genetic epidemiology

- **Inheritance pattern:** **X-linked dominant, female-restricted** (`HP:0001423` X-linked dominant inheritance). Male hemizygous LOF is presumed embryonic-lethal, so the pedigree pattern is de novo sporadic female cases, not vertical transmission.
  ⚠️ Note the contradictory MOI labelling in the literature: ClinGen's ID/Autism GCEP annotates the lumped USP9X entity as X-linked with females "XL recessive"; OMIM/HPO annotate MRXS99F as **X-linked dominant**. Follow OMIM/HPO for this entry and record the discrepancy.
- **Penetrance:** **high but incomplete — ~95%.**
  > **[VERBATIM — PMID:35253988]** "While the penetrance of pathogenic variants in USP9X in female appears to be high (95%) and the variants frequently occur de novo, incomplete penetrance should be considered."
  Two independent non-/mildly-penetrant transmitting mothers are documented (Li 2022; Jolly 2020 Female 31's mother, who had only scoliosis and partial hearing impairment).
- **Expressivity:** **highly variable** — from borderline ID with near-normal milestones to severe ID with absent speech, non-ambulation and neonatal lethality from cardiac disease. Au et al. 2017 made this the point of their report: **[VERBATIM]** *"suggests that USP9X mutations in females can have a wider spectrum of presentation than previously appreciated."*
- **Genetic anticipation:** **not applicable** (not a repeat-expansion disorder).
- **Germline / gonosomal mosaicism:** **documented.** Jolly 2020: *"One individual had an inherited variant from their mother who were subsequently found to be mosaic, a mode which has been previously reported."* **[VERBATIM]** This has direct recurrence-risk implications and is why maternal testing is mandatory even for apparently de novo variants.
- **Founder effects:** **none.** All reported variants are private.
- **Consanguinity:** **no role** (dominant, de novo).
- **Carrier frequency:** not meaningfully defined — there is no asymptomatic-carrier state in the usual sense; a female carrying a pathogenic allele is ~95% likely to be affected, and males cannot carry a LOF allele.

### 9.3 Population demographics

- **Affected populations:** no ethnic or geographic predilection. Reported cases span the Netherlands, Sweden, UK, USA, Australia, Singapore, Canada, France, Italy, Germany, North Macedonia, Japan, Thailand, and Brazil (an admixed *Pardo* individual from northern Brazil). Under-representation of non-European populations reflects **sequencing access, not biology** — a point the Brazilian authors make explicitly.
- **Geographic distribution:** worldwide; no endemic clustering; no variant-specific geographic distribution.
- **Sex ratio:** **essentially 100% female (F:M ≈ 1:0)** for the LOF-defined syndrome, by definition of the entity. The complementary male disorder (XLID99, OMIM 300919) is caused by partial-LOF missense.
- **Age distribution:** reported individuals are overwhelmingly paediatric (published range 2y7m–23y). **No data on adults >30 years.** This is a major natural-history gap.

---

## 10. Diagnostics

### 10.1 Genetic testing (the diagnostic mainstay)

**Recommended approach.** MRXS99F is a **molecular diagnosis**; there is no biochemical or imaging test that is diagnostic on its own. The efficient pathway is:

1. **Exome or genome sequencing (trio, where possible)** — first-line. In every published case, WES/WGS made the diagnosis, often after prior non-diagnostic testing. The Brazilian case is the canonical diagnostic-odyssey illustration: normal newborn screen → karyotype (found only a benign inv(9) polymorphism) → **normal high-resolution CMA** → **WES diagnostic at age 5**.
   - Utility of **WGS** specifically demonstrated by Xue et al. 2025 (PMID:41240171), which identified a novel variant in a newborn by WGS.
   - Trio design is important because **de novo status is itself a key ACMG criterion (PS2)** for a gene where most pathogenic alleles are private.
2. **Chromosomal microarray (CMA)** — should be done in parallel or first if the phenotype includes multiple congenital anomalies, because **~55% of DECIPHER USP9X-associated cases are CNVs**. CMA will detect Xp11.4 deletions that a poorly-covered exome CNV caller may miss.
3. **Multigene ID/NDD or malformation panels** — USP9X is included on essentially all contemporary intellectual-disability/XLID and multiple-congenital-anomaly panels. Search GTR (gene 8239) for current laboratory offerings.
4. **Single-gene USP9X testing** — appropriate only for targeted confirmation, or when the gestalt is recognized clinically. Reijnders et al. showed this works: *"Four females from our cohort were identified by targeted genetic testing because their phenotype was suggestive for USP9X mutations."* **[VERBATIM]**
5. **Parental (especially maternal) testing** — **mandatory**, not optional, because of documented maternal transmission with reduced penetrance and maternal gonosomal mosaicism. **[VERBATIM — PMID:40751225]** *"Despite the de novo nature of most loss-of-function variants, maternal testing is crucial for estimating recurrence risk."*
6. **Karyotype / FISH** — low yield; reserve for suspected balanced rearrangement (as in Au et al.'s pericentric inversion, which a CMA alone might have mis-attributed).
7. **X-inactivation (HUMARA) assay** — **not diagnostically useful.** Skewing does not correlate with severity, and USP9X escapes XCI. Useful only as a research adjunct.
8. **Not indicated:** mitochondrial DNA testing, repeat-expansion testing, metabolic screening (beyond standard newborn screening) — all normal in reported cases.

**Omics-based diagnostics.** RNA-seq has been used as a *research* tool (Li 2022, to hunt a penetrance modifier — negative). Proteomics, metabolomics, epigenomics (episignature) and liquid biopsy have **no established diagnostic role** for this disorder.

### 10.2 Clinical / laboratory tests supporting the diagnosis and managing the phenotype

| Modality | Findings | Suggested terms |
|---|---|---|
| **Brain MRI** (or CT) | Hypoplastic/agenetic corpus callosum, ventriculomegaly, cerebellar hypoplasia, Dandy-Walker malformation/Blake's pouch cyst, abnormal gyration, prominent extra-axial spaces, incomplete hippocampal inversion, reduced white-matter volume, optic nerve atrophy, periventricular heterotopia (reported in a male) | HP:0002079, HP:0002119, HP:0001321, HP:0001305, HP:0002536 |
| **Echocardiography** | ASD (ostium secundum), VSD (perimembranous), PDA, pulmonary hypertension | HP:0001631, HP:0001643 |
| **Spinal radiography** | Dorsolumbar scoliosis; serial films for progression | HP:0002650 |
| **Pelvic radiography** | Acetabular flattening/verticalization, femoral head dislocation | HP:0001385, HP:0002827 |
| **Renal ultrasound** | Renal dysplasia, hydronephrosis, pelvicalyceal/ureteric dilatation | HP:0000110, HP:0000126 |
| **Audiology (ABR/behavioural)** | Hearing impairment in 65% — **should be a standing surveillance item** | HP:0000365 |
| **Ophthalmology** | Strabismus, refractive error, cataract, optic atrophy | HP:0000486, HP:0000518 |
| **Thyroid function (TSH/fT4)** | Thyroid physiology abnormality in 35% | HP:0002926 |
| **EEG** | Indicated if seizures (~24%); no USP9X-specific EEG signature | HP:0001250 |
| **Nasal endoscopy / CT** | Choanal atresia (neonatal) | HP:0000453 |
| **Dental/orthodontic assessment** | Hypodontia, severe crowding (71%) | HP:0000164 |
| **Developmental/cognitive assessment** | Standardized IQ/adaptive testing; DSM-5 ID severity grading | HP:0001249 |
| **Biopsy / histopathology** | **No diagnostic role.** Skin biopsy is used only to derive fibroblasts for research (USP9X expression, cilia assays) | — |
| **Biomarkers** | **None.** No circulating protein, metabolite, or imaging biomarker exists. USP9X protein/mRNA reduction in patient fibroblasts is a research-grade functional assay, not a clinical test | — |

### 10.3 Clinical criteria

**No formal consensus diagnostic criteria, no DSM/ICD-specific criteria, no society guideline exists.** Diagnosis = pathogenic USP9X variant + compatible phenotype. There is, however, a **recognizable clinical gestalt** sufficient to prompt targeted testing (this is what "clinically recognisable USP9X-female syndrome" in the literature means):

*Gestalt:* a girl with DD/ID + at least two of {choanal atresia, anal atresia, postaxial polydactyly, cleft palate/bifid uvula, asymmetric hypomastia, progressive scoliosis} + corpus callosum anomaly/ventriculomegaly + short stature + Blaschko-line pigmentary change/body asymmetry + hearing loss.

*Facial gestalt (Jolly 2020, verbatim):* **"deep-set eyes, telecanthus, blepharophimosis, broad nasal tip with wide alae and short collumnella, low set and dysplastic ears, small mouth and micrognathia."**
*Additional craniofacial (Nagata 2024, PMID:38755172, verbatim):* **"hypotelorism, brachycephaly, hypodontia, micrognathia, severe dental crowding, and an isolated submucous cleft palate."**

### 10.4 Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **Congenital rubella / toxoplasmosis syndrome** | Serology-driven; **documented real-world misdiagnosis** of a USP9X case. Distinguish by absence of chorioretinitis/intracranial calcification and by the malformation profile. |
| **CHARGE syndrome (CHD7)** | Also features choanal atresia, heart defects, ear anomalies, DD. Distinguish by coloboma, semicircular canal hypoplasia, cranial nerve dysfunction, hypogonadotropic hypogonadism. **The highest-priority differential.** |
| **VACTERL association** | Anal atresia, cardiac and limb defects overlap. Distinguish by tracheo-oesophageal fistula, vertebral segmentation defects, and the usual **absence of significant ID**. |
| **Ciliopathies (Bardet-Biedl, Meckel, oral-facial-digital, Joubert)** | Postaxial polydactyly, renal, cerebellar/Dandy-Walker overlap — Reijnders explicitly noted the resemblance. Distinguish by retinal dystrophy, molar-tooth sign, cystic kidneys. |
| **Pallister-Hall / Greig cephalopolysyndactyly (GLI3)** | Postaxial polydactyly + midline defects. Distinguish by hypothalamic hamartoma, bifid thumb, macrocephaly. |
| **Goltz / focal dermal hypoplasia (PORCN)** | X-linked, male-lethal, Blaschko-line skin findings, limb defects, asymmetry — **an excellent mechanistic and clinical mimic**. Distinguish by fat herniation, papillomas, split-hand/foot. |
| **Incontinentia pigmenti (IKBKG)**, **MIDAS/microphthalmia with linear skin defects** | X-linked male-lethal disorders with Blaschko-line skin findings. |
| **Other female-restricted XL NDDs** — *PCDH19* clustering epilepsy, *DDX3X* syndrome, Rett (*MECP2*) | *PCDH19* is explicitly invoked as the closest mechanistic analogue for penetrance modification. *DDX3X* is the nearest phenotypic neighbour among female-predominant XL ID genes. |
| **X-linked lissencephaly/SBH (DCX)** | Shares the migration mechanism (DCX is a USP9X partner) but has a distinct, severe cortical malformation. |
| **Dandy-Walker malformation, isolated** | When the DWM is the presenting finding. |
| **XLID99 / MRX99 (male)** | Same gene; distinguish by sex and by the near-absence of congenital malformations. |

### 10.5 Screening

- **Newborn screening:** MRXS99F is **not** and cannot be included in biochemical NBS panels (no analyte). It would only be detectable by a genomic newborn-screening programme (e.g., research protocols such as BabySeq/Generation Study).
- **Carrier screening:** not applicable (dominant, de novo; no carrier state in the reproductive-screening sense).
- **Cascade screening:** **maternal testing is indicated in every proband** (see §10.1 step 5). Testing of sisters is indicated if a maternal variant is found.
- **Prenatal:** see §13.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **No survival curve, life-expectancy figure, or mortality rate has been published.** State this explicitly rather than estimating.
- **Documented mortality events:** one neonatal death from a heart defect (Female 23, Jolly 2020); one elective termination of an affected fetus with brain, heart and skeletal malformations (Female 31, Jolly 2020). Presumed male embryonic lethality is a separate, prenatal category.
- **Expected pattern (inference, low evidence):** early mortality risk is concentrated in the **neonatal period**, driven by choanal atresia (airway) and cardiac malformations. Individuals surviving infancy appear to survive into adulthood — the published cohort included a 23-year-old. Longer-term risks would be those generic to severe ID with scoliosis and dysphagia: aspiration pneumonia, restrictive lung disease, and status epilepticus in the seizure subgroup.
- **⚠️ Unquantified but real: childhood malignancy.** Jolly et al.: *"childhood malignancy has been reported in two female individuals with USP9X-female syndrome, and could potentially be involved in the natural course of the condition."* **[VERBATIM]** Given that USP9X is a *bona fide* tumour suppressor (FBW7/c-MYC, LATS/Hippo axes) and LOF variants are enriched in COSMIC, a tumour-predisposition component is biologically plausible. **No surveillance protocol exists and the risk is unquantified — this is the single most important open clinical question for the entry.** Curate as `discussions` with `kind: KNOWLEDGE_GAP` and `proposed_experiments` (registry-based cancer-incidence study).

### 11.2 Morbidity and function

- **Intellectual disability** is universal where assessed, spanning borderline → severe. Adaptive-functioning outcomes range from largely independent (Female 32) to total dependence for all ADLs.
- **Communication** is the most consistently and severely affected domain — universal speech/language involvement, up to complete absence of speech, compounded by 65% hearing loss.
- **Mobility:** hypotonia (47%) plus hip dysplasia (47%), scoliosis (65%) and foot deformity → ambulation may be delayed, aided (standing frames, wheelchairs), or never achieved.
- **Behaviour:** autism, anxiety, aggression reported; these drive substantial family burden.
- **Disability outcomes (ICF framing):** impairments across mental functions, sensory (auditory, visual), neuromusculoskeletal and movement-related functions; activity limitations in communication, mobility and self-care; participation restrictions in education and community life.
- **Quality-of-life measures:** **none published.** No EQ-5D, SF-36, PROMIS, PedsQL or condition-specific instrument has been applied. This is a clear gap that the Simons Searchlight registry is positioned to fill.

### 11.3 Complications

Neonatal airway obstruction (choanal atresia) · congenital heart disease and pulmonary hypertension · feeding difficulty and aspiration · recurrent respiratory infection (53%) · progressive scoliosis with restrictive lung disease · hip dislocation and pain · epilepsy (~24%) · sensorineural/conductive hearing loss (65%) · visual impairment including cataract and amblyopia · dental disease from hypodontia and severe crowding · hydronephrosis/renal impairment · thyroid dysfunction (35%) · possible childhood malignancy (see above).

### 11.4 Recovery potential

**No recovery.** The malformations are structural and fixed at birth; the encephalopathy is static. Meaningful *functional* improvement is achievable with early intervention, surgical correction of malformations, hearing amplification and rehabilitation, but the underlying condition is lifelong.

### 11.5 Prognostic factors and biomarkers

- **No validated prognostic model or biomarker exists.**
- Plausible but unvalidated prognostic factors, in rough order of support:
  1. **Presence and severity of a cardiac defect** — the only documented cause of death in the cohort.
  2. **Presence of choanal atresia** — neonatal airway risk.
  3. **Extent of brain malformation** (complete ACC vs. hypoplasia; presence of Dandy-Walker) — intuitively associated with severity, but **not formally correlated** in any published analysis.
  4. **Variant class** — Jolly et al. speculate catalytic-domain variants behave like nulls while N-terminal variants may spare substrate subsets, but explicitly note *"The impact of missense mutations is less defined."* **[VERBATIM]** No genotype–phenotype correlation is established.
  5. **X-inactivation skewing** — explicitly shown **not** to correlate with severity. Do not use as prognostic.
  6. **Early hearing-loss detection and amplification** — a *modifiable* factor likely influencing communication outcome.

---

## 12. Treatment

### 12.1 Overarching statement

> **[PARAPHRASE from the Simons Searchlight gene guide — verify before use as snippet]**
> "At this point, there are no medicines designed to treat the syndrome."

There is **no disease-modifying therapy, no targeted therapy, no gene therapy, no RNA therapy, no cell therapy, no immunotherapy, and no clinical trial of any intervention** for MRXS99F. Management is entirely **supportive, symptomatic, surgical and rehabilitative**, delivered by a multidisciplinary team.

The Brazilian case documents the real-world team composition: **[VERBATIM — PMID:40751225]** *"The specialties involved included medical geneticist, genetic counselor, orthopedist, physiotherapist, occupational therapist, speech therapist, dentist, otolaryngologist, ophthalmologist, neurologist, physiatrist, cardiologist, pediatrician, and nutritionist."*

### 12.2 Treatment inventory with suggested NCIT annotations

| Treatment | Indication | `treatment_term` (NCIT) | `therapeutic_modality` |
|---|---|---|---|
| Multidisciplinary supportive care | all | `NCIT:C15747` Supportive Care | OTHER |
| Physical therapy | hypotonia, motor delay, gait, contracture prevention | `NCIT:C15302` Physical Therapy | BEHAVIORAL |
| Occupational therapy | ADLs, fine motor | `NCIT:C121351` Occupational Therapy | BEHAVIORAL |
| Speech and language therapy | universal speech/language involvement; AAC | `NCIT:C159273` Speech Therapy | BEHAVIORAL |
| Rehabilitation (general) | composite | `NCIT:C15315` Rehabilitation | BEHAVIORAL |
| Behavioural intervention (ABA/behavioural counselling) | autism, anxiety, aggression | `NCIT:C181743` Behavioral Counseling *(verify)* | BEHAVIORAL |
| Choanal atresia repair / septoplasty | neonatal airway obstruction | `NCIT:C15329` Surgical Procedure | SURGERY |
| Anorectal malformation repair | anal atresia | `NCIT:C15329` Surgical Procedure | SURGERY |
| Cardiac surgical/catheter repair | ASD, VSD, PDA | `NCIT:C15329` Surgical Procedure | SURGERY |
| Cleft palate repair | cleft palate / submucous cleft | `NCIT:C15329` Surgical Procedure | SURGERY |
| Orthopaedic surgery (scoliosis instrumentation, hip reduction, foot correction) | progressive scoliosis, hip dislocation, equinovarus | `NCIT:C16186` Orthopedic Surgical Procedure | SURGERY |
| Polydactyly excision | postaxial polydactyly | `NCIT:C16186` Orthopedic Surgical Procedure | SURGERY |
| Corneal transplantation | corneal ulceration (case-level) | `NCIT:C15289` Organ Transplantation *(verify appropriateness)* | SURGERY |
| Hearing amplification / hearing aids | 65% hearing impairment | *(no reliable NCIT clinical-action term — see CLAUDE.md note on DEVICE)* | DEVICE |
| Antiseizure pharmacotherapy | ~24% seizures; no USP9X-specific ASM data | `NCIT:C15986` Pharmacotherapy | SMALL_MOLECULE |
| Levothyroxine | hypothyroidism where present | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` levothyroxine (`CHEBI:*` — verify) | SMALL_MOLECULE |
| Nutritional support / gastrostomy | feeding difficulty, failure to thrive | `NCIT:C15433` Nutritional Support *(see CLAUDE.md caution — do NOT auto-tag BEHAVIORAL)* | OTHER |
| Genetic counselling | family, recurrence risk | `NCIT:C15240` Genetic Counseling | BEHAVIORAL |
| Dental/orthodontic management | hypodontia, severe crowding | `NCIT:C15329` Surgical Procedure / dental term *(verify)* | OTHER |

⚠️ Every NCIT ID above must be confirmed with `uv run runoak -i sqlite:obo:ncit info <ID>` and `just validate-terms` before commit. Several (`NCIT:C181743`, `NCIT:C121351`, `NCIT:C159273`) are taken from the CLAUDE.md mechanical-backfill table but should still be re-verified.

**NCIT P302 (Accepted_Therapeutic_Use_For) note:** no drug in NCIT carries an accepted-therapeutic-use assertion for MRXS99F, so `just ncit-p302-audit` will find no coverage for this entry — expected, not a gap in curation.

### 12.3 Pharmacogenomics

No USP9X-specific pharmacogenomic guidance exists (nothing in PharmGKB or CPIC keyed to USP9X for this indication). Standard CPIC guidance applies to any antiseizure medication used (e.g., *HLA-B\*15:02* / carbamazepine).

### 12.4 Experimental and future therapeutic directions

- **No registered interventional trials.** The only ClinicalTrials.gov record retrievable for "USP9X" is **NCT01238250 — "Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight"** (status: RECRUITING), which is an **observational registry/natural-history study**, not an interventional trial. It is the appropriate `clinical_trials` entry for this disease, with the caveat that its `phase` is N/A.
- **Rational targets suggested by the mechanism (all preclinical/hypothetical):** because the defect is *loss* of a stabilizing DUB, plausible strategies would be (i) downstream pathway restoration (TGF-β/SMAD4 or mTORC1 modulation), or (ii) inhibition of the opposing E3 ligase — for SMAD4, that is **Ectodermin/TIF1γ**, which Dupont et al. identified as the monoubiquitin ligase USP9X opposes (**[VERBATIM]** *"FAM opposes the activity of Ectodermin/Tif1gamma (Ecto), a nuclear factor for which we now clarify a prominent role as Smad4 monoubiquitin ligase"*). None of this has been tested in a USP9X-deficiency model.
- **⚠️ Do not** propose USP9X *inhibitors* (Degrasyn/WP1130, G9, bosutinib) as therapy — these are oncology tools that would *worsen* a haploinsufficiency state. The Paemka seizure finding (§6.3F) is the only place inhibition looks beneficial, and only in a *Prickle*-mutant context.
- **Treatment response rates / adverse events:** not applicable — no disease-specific therapy exists to report on.

### 12.5 Treatment algorithm (synthesized; no published guideline exists)

1. **Neonatal:** secure airway (assess for choanal atresia); echocardiogram; assess for anal atresia; NICU support as needed; surgical repair of life-threatening malformations.
2. **Diagnosis:** trio ES/GS ± CMA; maternal testing; genetic counselling.
3. **Baseline multisystem evaluation:** brain MRI, echocardiogram, renal ultrasound, formal audiology, ophthalmology, thyroid function, spine and hip radiographs, developmental assessment, dental review.
4. **Early intervention:** PT/OT/SLT from diagnosis; AAC where speech is absent; hearing amplification.
5. **Ongoing surveillance:** annual (or growth-spurt-intensified) scoliosis and hip assessment; repeat audiology and ophthalmology; thyroid function; seizure review; developmental/educational re-assessment; **consider (unvalidated) awareness of childhood-malignancy reports**.
6. **Surgical management as indicated** across orthopaedics, cardiology, ENT, plastic surgery.
7. **Family support:** genetic counselling for recurrence risk; connection to Simons Searchlight and USP9X family communities.

---

## 13. Prevention

- **Primary prevention: not possible.** The disorder arises from de novo mutation; there is no modifiable exposure, no vaccine-preventable component, and no risk-factor modification available. Record explicitly as "not applicable."
- **Secondary prevention (early detection):**
  - **Prenatal detection** is feasible and has changed management: fetal ultrasound findings (agenesis of the corpus callosum, ventriculomegaly, cardiac defect, polydactyly, skeletal anomaly) → prenatal exome sequencing. Lenberg et al. explicitly note *"Identifying this variant impacted management of the subsequent pregnancy."* **[VERBATIM]**
  - **Early postnatal recognition** of the gestalt shortens the diagnostic odyssey (the Brazilian case took ~5 years and three prior tests).
  - No population screening programme is warranted or exists for a <1/1,000,000 condition with no preventive intervention.
- **Tertiary prevention (preventing complications in affected individuals)** — this is where prevention effort actually lies:
  - Scoliosis surveillance and bracing to delay/avoid instrumented fusion and restrictive lung disease.
  - Hip surveillance to prevent fixed dislocation.
  - **Audiology surveillance** — preventing the compounding of communication disability by undetected hearing loss.
  - Ophthalmic surveillance to prevent amblyopia; corneal protection where blink is impaired.
  - Aspiration precautions and nutritional support to prevent recurrent pneumonia.
  - Thyroid monitoring.
- **Genetic screening / reproductive prevention:**
  - **Maternal testing after every proband diagnosis** — the pivotal step, because it converts an assumed ~0% recurrence risk into either a ~50% transmission risk (if the mother carries the variant) or a low (~1%) gonadal-mosaicism-based risk.
  - **Prenatal diagnosis** (CVS/amniocentesis with targeted variant testing) and **preimplantation genetic testing (PGT-M)** are both technically available once the familial variant is known.
  - Reproductive counselling must include that (i) affected females have a ~50% transmission risk per pregnancy, (ii) male conceptuses inheriting a LOF allele are expected to be non-viable, and (iii) penetrance in females, while ~95%, is not complete.
  - In the Brazilian case the mother declined testing, which the authors flag as leaving recurrence risk formally unresolved — a good teaching point for the entry.
- **Immunization:** routine childhood immunization per national schedule; no disease-specific vaccine strategy. Given 53% recurrent respiratory infections, **influenza, pneumococcal and RSV immunization are prudent** (extrapolated best practice, not USP9X-specific evidence).
- **Genetic counselling** (`NCIT:C15240`) is the single most important preventive intervention.
- **Public-health / environmental interventions:** not applicable.
- **Prophylaxis:** no pharmacological prophylaxis is established. Antibiotic prophylaxis and endocarditis prophylaxis follow standard indications for the specific cardiac or urinary tract lesion, not the syndrome.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologues

| Species | NCBI Taxon | Gene | Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | USP9X | 8239 | HGNC:12632; paralogue **USP9Y** on Yq11 |
| *Mus musculus* | `NCBITaxon:10090` | **Usp9x** | 22284 | **MGI:894681**; X chromosome; the workhorse model |
| *Rattus norvegicus* | `NCBITaxon:10116` | Usp9x | 363445 | RGD; few disease studies |
| *Danio rerio* | `NCBITaxon:7955` | usp9x | ZFIN | limited published NDD modelling |
| *Drosophila melanogaster* | `NCBITaxon:7227` | **faf** (*fat facets*) | FlyBase | the founding orthologue; used in the *prickle* seizure work |

**Evolutionary conservation** is a defining feature and directly underpins model validity:
> **[VERBATIM — PMID:25672900]** "The ubiquitin-specific protease 9X (USP9X/FAM) is a substrate-specific DUB, which displays an extraordinarily high level of sequence conservation from Drosophila to mammals."
> **[VERBATIM — PMID:19135894]** "…FAM (USP9x), a deubiquitinase acting as essential and evolutionarily conserved component in TGFbeta and bone morphogenetic protein signaling."

Note that the **USP9Y** paralogue exists in humans but does not rescue USP9X loss in females (irrelevant to 46,XX) and is not a modifier candidate here.

### 14.2 Natural disease in other species

- **No naturally occurring USP9X disorder is recorded in OMIA** for any companion animal, livestock species, or wildlife population. No veterinary syndrome corresponds to MRXS99F.
- All animal disease models are **experimentally engineered** (see §15), not naturally occurring.
- **Breed (VBO):** not applicable — no breed-associated USP9X disease.

### 14.3 Comparative biology

- **Comparative pathology:** the conserved core is the **CNS phenotype**. Mouse *Usp9x* deletion reproduces the corpus callosum, hippocampal, ventricular and connectivity abnormalities and the learning/memory deficit. What mouse models do **not** reproduce is the distinctive peripheral malformation set (choanal atresia, anal atresia, postaxial polydactyly, hypomastia) — a genuine human–model divergence.
- **Evolutionary conservation of mechanism:** the *prickle*-seizure axis is conserved from fly to mouse to human (Paemka 2015); the TGF-β/SMAD4 axis is conserved from *Drosophila* to mammals (Dupont 2009).
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

### 15.1 Mouse — the principal model system (MGI:894681)

**Available genetic models**
| Model | Construction | Key phenotype |
|---|---|---|
| **Constitutive *Usp9x* knockout** | germline null | **embryonic lethal** — establishes essentiality; *"It is essential for embryonic viability"* (Jolly 2020) |
| ***Usp9x*^loxP/loxP^ × Nestin-Cre** | pan-neural conditional (whole brain, progenitors + progeny) | **early postnatal lethality**; disrupted VZ/SVZ and cortical-plate organization; dramatically reduced axon length; failed TGF-β signalling; disrupted cell adhesion and apical-basal polarity; ectopic intermediate progenitors; increased phospho-β-catenin; decreased Itch/Numb with increased NICD and *Hes5* |
| ***Usp9x*^loxP/loxP^ × Emx1-Cre** | dorsal telencephalon only | **survives to adulthood**; reduction or **loss of the corpus callosum**; dramatically decreased hippocampal size; disorganized hippocampal CA3 |
| **Forebrain-specific KO (*Usp9x*^−/y^)** | Kasherman 2021 | abnormal communication and social behaviour; reduced size of multiple brain regions; DTI deficits in **all three forebrain commissures**; long-range cortical–subcortical hypoconnectivity |
| **Brain-specific KO** | Johnson 2020 | correlates of the *male* phenotype; **loss of hippocampal-dependent learning and memory** |
| Postnatal dentate gyrus analysis (conditional KO) | Oishi 2016 | smaller hippocampus and shortened DG blades from P7; reduced stem cell, neuroblast and neuronal numbers; abnormal neuroblast morphology |
| Nestin-cre-derived neurospheres / NSPCs | ex vivo | reduced mTORC1 signalling; G0 arrest; paradoxically increased sphere-forming (self-renewal) capacity |
| Gut-specific *Usp9x* deletion | Khan 2018 | reduced secretory-cell differentiation, increased progenitor proliferation, increased colitis-associated tumour burden (cancer arm, not NDD) |

**Anchor quotations (all [VERBATIM]):**
> PMID:23861879 — "Mating Usp9x(loxP/loxP) mice with mice expressing Cre recombinase from the Nestin promoter deleted Usp9x throughout the entire brain, and resulted in early postnatal lethality. Although the overall brain architecture was intact, loss of Usp9x disrupted the cellular organization of the ventricular and sub-ventricular zones, and cortical plate… Deletion of Usp9x from the dorsal telencephalon only, by mating with Emx1-cre mice, was compatible with survival to adulthood but resulted in reduction or loss of the corpus callosum, a dramatic decrease in hippocampal size, and disorganization of the hippocampal CA3 region. This latter phenotypic aspect resembled that observed in Doublecortin knock-out mice, which is an Usp9x interacting protein."

> PMID:33188399 — "Usp9x−/y mice displayed abnormal communication and social interaction behaviors. Moreover, the absence of Usp9x culminated in reductions to the size of multiple brain regions. Diffusion tensor magnetic resonance imaging revealed deficits in all three major forebrain commissures, as well as long-range hypoconnectivity between cortical and subcortical regions."

> PMID:31443933 — "In addition, we find correlates of the male phenotype in Usp9x brain-specific knockout mice, and further resolve loss of hippocampal-dependent learning and memory."

**Phenotype recapitulation — explicit authorial assessment:**
> **[VERBATIM — Jolly 2020, full text]** "Furthermore, genetic ablation of Usp9x from the developing mouse brain (loss of dosage) provides a strong recapitulation of the neurological phenotypes of these affected females, including hypoplastic corpus callosum, ventriculomegaly, and learning and memory problems."

**Model limitations — curate as `HUMAN_MODEL_MISMATCH`, not merely `KNOWLEDGE_GAP`:**
1. **Dosage mismatch.** The mouse models are *complete* conditional nulls (−/y or −/−); the human female disease is *heterozygous haploinsufficiency* in a gene that escapes XCI. A **heterozygous female mouse model that reproduces the human dosage state has not been reported** — and mouse *Usp9x* XCI-escape behaviour may differ from human. This is the single most important translational caveat.
2. **The peripheral malformation set is not modelled.** No mouse model reproduces choanal atresia, anal atresia, postaxial polydactyly, hypomastia or cleft palate — precisely the features that make the human syndrome clinically recognizable. Brain-restricted Cre drivers cannot, by construction, generate them.
3. **The mosaic/asymmetry phenotype (Blaschko lines, body asymmetry) is not modelled**, because it depends on tissue-variable XCI escape in a heterozygote.
4. **Sex mismatch.** Most published neural work is in *Usp9x*^−/y^ **males** (hemizygous conditional nulls) — the opposite sex from the human disease.
5. **The male-lethality claim itself is inferential** in humans ("believed to be incompatible with life") and rests on the constitutive-KO mouse plus the absence of male LOF in DECIPHER/ClinVar.

Suggested dismech `discussions` entry:
```yaml
discussions:
- kind: HUMAN_MODEL_MISMATCH
  attaches_to: "pathophysiology#USP9X Haploinsufficiency"
  prompt: >-
    Do conditional Usp9x-null mouse models (complete loss, usually -/y males,
    brain-restricted Cre) faithfully model human USP9X-female syndrome, which is
    heterozygous haploinsufficiency of an XCI-escape gene in 46,XX individuals
    affecting many non-neural organs?
  rationale: >-
    Mouse models strongly recapitulate the CNS phenotype (corpus callosum
    hypoplasia, ventriculomegaly, learning/memory deficits) but reproduce none of
    the defining congenital malformations (choanal atresia, anal atresia,
    postaxial polydactyly, hypomastia) nor the mosaic Blaschko-line/asymmetry
    features, which depend on tissue-variable escape from X-inactivation in a
    heterozygote.
  proposed_experiments:
  - Generate and phenotype a heterozygous Usp9x+/- female mouse, characterising
    allele-specific expression across tissues to test XCI-escape conservation.
  - Use non-neural Cre drivers (neural crest, hindgut endoderm, limb bud, nasal
    placode) to test whether tissue-specific Usp9x loss generates the malformation set.
  - Patient-derived iPSC cerebral and craniofacial organoids to model human-specific
    developmental windows.
```

### 15.2 Other systems

- ***Drosophila*** (**faf** / *fat facets*): used as the genetic-interaction system for the *prickle*–seizure axis. **[VERBATIM — PMID:25763846]** *"The seizure phenotype was suppressed in prickle mutant flies by the small-molecule USP9X inhibitor, Degrasyn/WP1130, or by reducing the dose of fat facets a USP9X orthologue."* Useful for pathway epistasis; not a morphological model of the syndrome.
- **Zebrafish:** *usp9x* orthologue exists; **no published morphant/mutant model of MRXS99F** was found. An open opportunity given zebrafish tractability for craniofacial and cilia phenotypes.
- **Cellular / in vitro:**
  - **Patient-derived dermal fibroblasts** — the key human primary system; used to demonstrate reduced USP9X mRNA and protein (Reijnders 2016) and to test ciliary parameters (negative). `evidence_source: IN_VITRO`.
  - **Patient-derived cell lines** — used by Johnson 2020 to show substrate-selective loss and the united TGF-β defect.
  - **ReNcell VM** human neural progenitor line — the system in which USP9X knockdown produced G0 arrest and reduced mTORC1 (Bridges 2017).
  - **Mouse neurospheres / primary cortical neurons** — axon outgrowth and migration rescue assays; the platform on which Homan 2014 discriminated pathogenic from benign USP9X variants.
  - **HEK293/HeLa and cancer lines** — for substrate biochemistry (SMAD4, MCL1, RAPTOR, FBW7, LATS).
  - **iPSC / organoids:** **not yet reported for USP9X.** A notable gap, and the modality most likely to bridge limitation (2) above.
- **Induced (non-genetic) models:** pharmacological USP9X inhibition (Degrasyn/WP1130, G9) is used in cancer work; **not a valid model of the LOF disease** for anything beyond acute substrate-destabilization readouts.

### 15.3 Applications and resources

**Research applications supported by existing models:** neural progenitor proliferation and self-renewal; apical-basal polarity and adhesion in the VZ/SVZ; neuronal migration; axon outgrowth and commissure formation; hippocampal development and hippocampal-dependent learning; social/communicative behaviour; connectomics via DTI; substrate-level biochemistry of TGF-β, mTORC1, Notch, Wnt; **variant functional assay** (the axon-growth/migration rescue assay is a validated, disease-relevant readout for classifying USP9X missense variants — directly useful for ACMG PS3-level evidence).

**Databases:** MGI (`MGI:894681`) · IMPC (`mousephenotype.org/data/genes/MGI:894681`) · Alliance of Genome Resources · RGD · ZFIN · FlyBase (*faf*) · IMSR/MMRRC/EMMA for strain sourcing · Cellosaurus for the cell lines · DepMap for dependency data.

---

## Appendix A — Consolidated citation list

| PMID | Short citation | Role | Cache status in this repo |
|---|---|---|---|
| **26833328** | Reijnders MR et al. 2016, *Am J Hum Genet* 98(2):373-81. DOI 10.1016/j.ajhg.2015.12.015 | **Defining paper**, n=17 females | ✅ cached (abstract) |
| **33298948** | Jolly LA et al. 2020, *npj Genom Med* 5:53. DOI 10.1038/s41525-020-00162-9 | **Key expansion**, missense contribution, n=35 aggregate, constraint metrics | ✅ cached (full text) |
| **31443933** | Johnson BV et al. 2020, *Biol Psychiatry* | Male disorder; TGF-β convergence; patient cell lines | ✅ cached |
| **24607389** | Homan CC et al. 2014, *Am J Hum Genet*. DOI 10.1016/j.ajhg.2014.02.004 | Male XLID; migration/axon growth assay; proteomics | ✅ cached |
| **40751225** | da Silva Campos TA et al. 2025, *J Med Case Rep* 19:380 | Brazilian case; incidence estimate; diagnostic odyssey; frequency re-statement | ✅ cached (full text, CC-BY) |
| **35253988** | Li D et al. 2022, *Am J Med Genet A* 188(6):1808-14 | Incomplete penetrance; 95% penetrance figure | ✅ cached |
| **33638286** | Meira JGC et al. 2021, *Am J Med Genet A* 185(5):1569-74 | Novel LOF variant + review; prenatal features | ✅ cached |
| 28377321 | Au PYB et al. 2017, *Eur J Med Genet* | Variable expressivity; X inversion | ❌ needs fetch |
| 30997057 | Lenberg JL et al. 2019, *Clin Case Rep* 7(4):656-60 | Prenatal detection, isolated ACC | ❌ needs fetch |
| 41240171 | Xue S et al. 2025, *Mol Biol Rep* | WGS diagnosis in a newborn | ❌ needs fetch |
| 38755172 | Nagata N et al. 2024, *Hum Genome Var* 11:21 | Craniofacial/dental phenotype | ❌ needs fetch |
| 36680497 | De Laurentiis A et al. 2023, *Am J Med Genet A* | Periventricular heterotopia (male) | ❌ needs fetch |
| 30828969 | — 2019 | Female-restricted syndromic ID, Thailand | ✅ cached |
| 31666975 | — 2019 | Novel USP9X variants, two XLID patients | ✅ cached |
| **19135894** | Dupont S et al. 2009, *Cell* | **SMAD4 monoubiquitination / TGF-β** | ❌ needs fetch |
| **28341829** | Bridges CR et al. 2017, *Sci Rep* | **RAPTOR / mTORC1** | ❌ needs fetch |
| **27181636** | Premarathne S et al. 2017, *Sci Rep* | **Wnt/β-catenin, Notch/Itch/Numb, adhesion & polarity** | ❌ needs fetch |
| **23861879** | Stegeman S et al. 2013, *PLoS One* | **Cortical architecture, hippocampus, TGF-β axonogenesis** | ✅ cached |
| **33188399** | Kasherman MA et al. 2021, *Cereb Cortex* | **Behaviour + DTI connectomics** | ❌ needs fetch |
| 27181636* | Oishi S et al. 2016, *Sci Rep* 6:25783 | Postnatal dentate gyrus (⚠️ **PMID needs re-verification** — see Appendix B) | ❌ |
| **25763846** | Paemka L et al. 2015, *PLoS Genet* | PRICKLE2 / seizures | ❌ needs fetch |
| **25672900** | Murtaza M, Jolly LA, Gecz J 2015, *Cell Mol Life Sci* | **Authoritative USP9X review** | ❌ needs fetch |
| 15607950 | Friocourt G et al. 2005, *Mol Cell Neurosci* | DCX–USP9X(DFFRX) interaction | ❌ needs fetch |
| 20023629 | Schwickart M et al. 2010, *Nature* | MCL1 stabilization | ❌ needs fetch |
| 29346117 | Khan OM et al. 2018, *J Clin Invest* | FBW7; intestinal tumour suppression | ❌ needs fetch |
| 29022598 | Tukiainen T et al. 2017, *Nature* | XCI escape landscape | ❌ needs fetch |
| 40663270 | Xue Y et al. 2025, *Mol Neurobiol* | Ubiquitination in the nervous system (recent review) | ❌ needs fetch |

**Non-PMID references:** `OMIM:300968`, `OMIM:300072`, `OMIM:300919`; `ORPHA:480880`; ClinGen gene-disease validity (USP9X, Definitive, 2021-11-17) and dosage (HI=3, 2024-11-27) — to cite as `CGGV:` / `CGDS:HGNC_12632` after running the ClinGen refresh/rebuild recipes; `clinicaltrials:NCT01238250`.

Before committing any of the above as evidence:
```bash
just fetch-reference PMID:19135894      # etc. for each ❌ row
just validate kb/disorders/USP9X_Female-Restricted_Syndromic_Intellectual_Disability.yaml
just validate-references kb/disorders/USP9X_Female-Restricted_Syndromic_Intellectual_Disability.yaml
just validate-terms kb/disorders/USP9X_Female-Restricted_Syndromic_Intellectual_Disability.yaml
just count-verified-snippets kb/disorders/USP9X_Female-Restricted_Syndromic_Intellectual_Disability.yaml
```

---

## Appendix B — Explicit gaps, cautions, and items I could not verify

**Information genuinely not available for this disease (record as such; do not fabricate):**
1. Survival curves, life expectancy, mortality rate, disease-specific mortality.
2. Any quality-of-life measurement (EQ-5D, SF-36, PROMIS, PedsQL).
3. Incidence per 100,000 per year (only a single quoted ~1:1,000,000 birth-incidence *estimate* from a case report).
4. Formal diagnostic criteria, society management guidelines, or a published surveillance protocol.
5. Genotype–phenotype correlation.
6. Any metabolomic, lipidomic, proteomic-biomarker, or DNA-methylation-episignature data.
7. Any interventional clinical trial.
8. Adult (>30 y) natural history.
9. Quantified cancer risk despite two reported childhood malignancies.
10. iPSC/organoid models; zebrafish models; a heterozygous female mouse model.
11. Systematic immunological evaluation despite 53% recurrent respiratory infections.

**Verification debts in this report (must be closed before curation):**
- Abstracts for **PMID:41240171, 40751225 (abstract portion), 35253988, 38755172, 36680497, 37064340** were returned through a summarizing fetch layer. The 40751225 and 35253988 text I quoted was subsequently confirmed against `references_cache/` and is verbatim; the others are marked **[PARAPHRASE]** and are not snippet-safe.
- The **Oishi et al. 2016 dentate gyrus paper**: the E-utilities result attributed the abstract *"Usp9x-deficiency disrupts the morphological development of the postnatal hippocampal dentate gyrus"* (Oishi S, Premarathne S, Harvey TJ; *Sci Rep* 2016; DOI 10.1038/srep25783) to the same PMID as the Premarathne 2017 paper in one fetch. **Re-resolve this PMID before citing** — the DOI (10.1038/srep25783) is the reliable anchor.
- **UBERON and CL identifiers** marked *(verify)* were written from domain knowledge, not confirmed against OLS/OAK in this session. Only these were verified: `UBERON:0002336`, `UBERON:0002285`, `UBERON:0004771`, `UBERON:0010425`, `CL:0011020`, `CL:0000681`, `CL:0013000`.
- **GO terms verified:** `GO:0016579`, `GO:0004843`, `GO:0007179`, `GO:0001764`, `GO:0038202`, `GO:0030426`, `GO:0005930`, `GO:0022038`. Not verified: `GO:0007409`, `GO:0016055`, `GO:0007219`, `GO:0005813`, `GO:0005829`.
- **All HPO IDs** in §3.1 came directly from the HPO annotation API for OMIM:300968 and are reliable; `HP:0011356` (Blaschko-line pigmentation) is my suggestion and is **not** in that annotation set — verify separately.
- **All NCIT IDs** in §12.2 need OAK verification.
- **gnomAD pLI=1.0 / z=6.35** is sourced to Jolly 2020's text, not to a live gnomAD query (the gnomAD GraphQL endpoint did not render through WebFetch). If a current LOEUF value is needed, query gnomAD directly.

**Two upstream data issues worth reporting:**
- **MONDO carries two un-merged terms** for this entity (`MONDO:0010502` OMIM-derived, `MONDO:0018821` Orphanet-derived), despite both mapping exactly to OMIM:300968. Worth a MONDO issue.
- **ClinGen lumps** the male and female USP9X disorders under MONDO:0020119, while OMIM/MONDO/Orphanet split them, and ClinGen additionally labels the female MOI "XL recessive" where OMIM/HPO say X-linked dominant. Record the discrepancy in the entry's notes rather than silently picking one.

---

## Sources

- [OMIM #300968 — MRXS99F](https://omim.org/entry/300968) · [OMIM *300072 — USP9X](https://omim.org/entry/300072) · [OMIM #300919 — MRX99](https://omim.org/entry/300919)
- [MONDO:0010502 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0010502) · [MONDO:0018821](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0018821)
- [Orphadata cross-referencing, ORPHA:480880](https://api.orphadata.com/rd-cross-referencing/orphacodes/480880?lang=en) · [Orphadata epidemiology, ORPHA:480880](https://api.orphadata.com/rd-epidemiology/orphacodes/480880?lang=en)
- [HPO annotations for OMIM:300968](https://ontology.jax.org/api/network/annotation/OMIM:300968)
- [MedGen C4225416](https://www.ncbi.nlm.nih.gov/medgen/?term=MRXS99F) · [Disease Ontology DOID:0112025](https://www.informatics.jax.org/disease/DOID:0112025)
- [HGNC:12632 (USP9X)](https://rest.genenames.org/fetch/symbol/USP9X) · [UniProt Q93008](https://rest.uniprot.org/uniprotkb/Q93008.txt) · [NCBI Gene 8239](https://www.ncbi.nlm.nih.gov/gene/8239)
- [ClinGen USP9X curations (HGNC:12632)](https://search.clinicalgenome.org/kb/genes/HGNC:12632) · [ClinVar USP9X](https://www.ncbi.nlm.nih.gov/clinvar/?term=USP9X%5Bgene%5D)
- [Reijnders et al. 2016, PMC4746365](https://pmc.ncbi.nlm.nih.gov/articles/PMC4746365/) · [da Silva Campos et al. 2025, PMC12317612](https://pmc.ncbi.nlm.nih.gov/articles/PMC12317612/) · [Jolly et al. 2020, npj Genomic Medicine](https://www.nature.com/articles/s41525-020-00162-9)
- [Simons Searchlight — USP9X-Related Syndrome](https://www.simonssearchlight.org/gene-guide/usp9x/) · [ClinicalTrials.gov NCT01238250](https://clinicaltrials.gov/study/NCT01238250)
- [IMPC — Usp9x (MGI:894681)](https://www.mousephenotype.org/data/genes/MGI:894681) · [SFARI Gene — USP9X](https://gene.sfari.org/database/human-gene/USP9X) · [GeneCards — USP9X](https://www.genecards.org/cgi-bin/carddisp.pl?gene=USP9X) · [NIH GTR — USP9X](https://www.ncbi.nlm.nih.gov/gtr/genes/8239/)