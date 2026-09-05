---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-18T21:39:05.837423'
end_time: '2026-08-18T21:49:31.850186'
duration_seconds: 626.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Hemorrhagic Telangiectasia Type 4
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 4
  num_turns: 49
  total_cost_usd: 5.1662514999999996
  session_id: 8e7064ae-55fd-4833-a192-0f15d35a63d4
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 23
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:38357927
  relevance_assessed: 31
  on_topic: 25
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hemorrhagic Telangiectasia Type 4
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hemorrhagic Telangiectasia Type 4** covering all of the
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

# Hereditary Hemorrhagic Telangiectasia Type 4 (HHT4)

**Research report for knowledge-base curation — compiled 18 August 2026**
**MONDO:0012532 · OMIM:610655 · locus 7p14 · causal gene UNIDENTIFIED**

---

## Executive summary and the central caveat for curation

HHT4 is **not a molecularly defined disease entity**. It is a *linkage locus* — a genetic-heterogeneity placeholder — established in **one single family** by a **single publication** in 2006, and the underlying gene has never been identified in the twenty years since. Every clinical, mechanistic, therapeutic, and epidemiological statement below that goes beyond "the disease in this family mapped to 7p14" is **extrapolated from hereditary hemorrhagic telangiectasia (HHT) as a whole**, and must be curated as such.

Two facts anchor the entry:

1. **The primary (and effectively only) HHT4-specific source is Bayrak-Toydemir et al., *Am J Med Genet A* 2006;140(20):2155–2162 (PMID:16969873, DOI:10.1002/ajmg.a.31450).**
2. **A PubMed query for `"HHT4" OR ("hereditary hemorrhagic telangiectasia" AND 7p14)` (run 18 Aug 2026) returns 5 records, of which only 2 concern this disease** — the 2006 original and a 2019 Korean prevalence review that merely notes HHT3/HHT4 testing is not implemented (PMID:31455059). The remaining three hits are homonyms (a rice accession, a hepatocyte cell line, and *Tetrahymena* histone genes). This is the strongest available evidence that no gene-discovery follow-up has been published.

A closely related curation hazard: **HHT3 (5q31.3–q32, OMIM:601101, MONDO:0011186) and HHT4 (7p14, OMIM:610655, MONDO:0012532) are trivially transposable.** They are adjacent members of a numbered series, both are locus-only, and reviews almost always name them in the same sentence. A transposition survives every standard anti-hallucination check (real PMID, exact snippet, valid ontology ID), so it must be caught semantically. Cross-check any 5q claim against Cole et al. 2005 (PMID:15879500) and Govani & Shovlin 2010 (PMID:20701797), which are **HHT3** papers.

---

## 1. Disease Information

### Overview

Hereditary hemorrhagic telangiectasia (HHT; Osler–Weber–Rendu disease) is an autosomal dominant multisystem vascular dysplasia in which arteriovenous malformations (AVMs) — direct artery-to-vein connections lacking an intervening capillary bed — form in mucocutaneous sites (as small telangiectases) and in viscera (as large AVMs in lung, liver, brain, spine). GeneReviews (PMID:20301525, updated 19 Feb 2026) states:

> "Hereditary hemorrhagic telangiectasia (HHT) is characterized by the presence of multiple arteriovenous malformations (AVMs) that lack intervening capillaries and result in direct connections between arteries and veins. The most common clinical manifestation is recurrent nosebleeds (epistaxis) beginning on average at age 12 years."

**HHT4 is the fourth mapped locus for this phenotype.** Bayrak-Toydemir et al. (PMID:16969873) studied one family with classic HHT in which linkage to HHT1 (*ENG*), HHT2 (*ACVRL1*) and HHT3 (5q) had been excluded, and reported:

> "Whole genome linkage analysis and fine mapping results suggested a 7 Mb region on the short arm of chromosome 7 (7p14) between STR markers D7S2252 and D7S510. We obtained a maximum two point LOD score of 3.60 with the STR marker D7S817. This region was further confirmed by haplotype analysis. These findings suggest the presence of another gene causing HHT (HHT4)."

### Identifiers (verified against MONDO via EBI OLS4, 18 Aug 2026)

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0012532** — *hereditary hemorrhagic telangiectasia type 4* |
| MONDO parent | MONDO:0019180 — *hereditary hemorrhagic telangiectasia* (sole parent) |
| OMIM | **610655** (`TELANGIECTASIA, HEREDITARY HEMORRHAGIC, TYPE 4; HHT4`) |
| MedGen | 341824 |
| UMLS | C1857688 |
| MeSH | C565691 (supplementary concept) |
| GARD | 0010615 |
| Orphanet | **No ORPHA cross-reference exists.** Orphanet codes HHT at the parent level (ORPHA:774); HHT3/HHT4 are not separately coded. Do not invent one. |
| ICD-10 | I78.0 (parent-level, HHT; no HHT4-specific code) |
| ICD-11 | Parent-level only (no type-4 code) |
| MONDO subsets | `gard_rare`, `nord_rare`, `rare` |

### Synonyms

- HHT4 (abbreviation; MONDO related synonym, xref GARD)
- Telangiectasia, hereditary hemorrhagic, type 4 (OMIM title form)
- *Inherited from the parent concept, applicable but not HHT4-specific:* Osler–Weber–Rendu disease/syndrome, Rendu–Osler–Weber syndrome, Osler disease.

### Nature of the evidence base

**Aggregated disease-level resource + a single pedigree study.** There is no HHT4 registry, no EHR-derived cohort, no biobank series. The 2006 paper is a family-based linkage study with clinical phenotyping of the pedigree. All population-level information in this report describes HHT *sensu lato*.

---

## 2. Etiology

### Causal factors

- **Primary cause:** an unidentified, presumptively heterozygous germline variant in a gene within the **7p14** interval, segregating with HHT in one pedigree with a maximum two-point LOD of 3.60 at D7S817 (PMID:16969873). The interval spans ~7 Mb between D7S2252 and D7S510.
- **Candidate genes explicitly excluded by the original authors' sequencing:** *BMPER*, *CCM2*, *RALA*, *INHBA* (reported in the 2006 paper's candidate-gene analysis and reproduced in OMIM 610655; the abstract itself does not enumerate them, so this should be curated as a full-text/OMIM-sourced claim). All four are plausible on prior biology — *BMPER* modulates BMP signaling, *CCM2* causes cerebral cavernous malformation, *RALA* is a Ras-family GTPase, *INHBA* encodes the inhibin/activin βA subunit in the TGF-β superfamily.
- **Non-genetic causes:** none. HHT is monogenic.
- **Mechanistic prior:** because all four known HHT genes (*ENG*, *ACVRL1*, *SMAD4*, *GDF2*) act in one pathway, the strong *a priori* expectation is that the HHT4 gene is a further BMP9-10/ENG/ALK1/SMAD4 pathway component or modifier. **This is a hypothesis, not a finding** — curate it as a `KNOWLEDGE_GAP`, never as pathophysiology.

### Genetic risk factors

- The segregating 7p14 haplotype is the risk factor, in a Mendelian dominant sense.
- No susceptibility loci, GWAS signals, or modifier alleles have been reported *for HHT4*.
- For HHT generally, *PTPN14* has been proposed as a modifier that "protects SMAD4 from ubiquitination and turnover to potentiate BMP9 signaling in endothelial cells" (bioRxiv preprint; treat as preliminary, not peer-reviewed evidence).

### Environmental risk factors

None established for HHT4. For HHT generally, the phenotype is modulated by physiological states that drive angiogenesis or alter hemodynamics — puberty, pregnancy, and aging correlate with lesion appearance and progression; the JCI review (PMID:38357927) frames the disease as caused by "abnormal activation of angiogenesis," and animal work shows AVMs require an angiogenic trigger (wounding, VEGF) on top of the genetic lesion (Park et al., *J Clin Invest* 2009;119:3487–96, PMID:19805914).

### Protective factors

- **Genetic:** none reported.
- **Environmental:** none established. Of note, a 20-year Danish follow-up (Kjeldsen et al., *Orphanet J Rare Dis* 2016, PMID:27876060) found **lower** cancer incidence in HHT patients than matched controls — "Cancer diagnoses had been registered in the follow-up period in 4 (5%) HHT patients and in 38 (17%) controls" — consistent with constitutively impaired angiogenesis, but this is an observation about HHT1/HHT2 patients, not a protective factor for HHT4.

### Gene–environment interactions

The best-supported GxE concept in HHT is the **"second hit / angiogenic trigger" model**: heterozygous pathway loss is necessary but not sufficient, and a local angiogenic or injury stimulus precipitates AVM formation. Evidence is model-organism (PMID:19805914). Whether it applies to the HHT4 lesion is **unknown and untestable until the gene is found**.

---

## 3. Phenotypes

### HHT4-specific phenotype

The **only** HHT4-specific phenotypic statement in the literature is in the 2006 abstract:

> "Here we report on linkage results on a family with classic features of HHT, albeit **a less severe phenotype with regards to epistaxis and telangiectases**, in which linkage to HHT1, HHT2, and HHT3 is ruled out."

and

> "The features in this family that strongly suggest the presence of a hereditary, multisystem vascular dysplasia would be easily missed during the typical evaluation and management of a patient with an AVM. This family helps emphasize the need to obtain a very detailed, targeted medical and family history for even mild, infrequent but recurring nosebleed, subtle telangiectases."

**Curation implications, all directly supported:**
- HHT4 as described is a **mild/attenuated mucocutaneous phenotype with preserved visceral AVM burden** — epistaxis is infrequent, telangiectases subtle, but an AVM brought the family to attention.
- The family is therefore at high risk of being **under-ascertained by Curaçao criteria**, which weight epistaxis and telangiectases heavily.
- Per-member clinical detail (number of affected individuals, AVM organ distribution, ages of onset) is in the **full text only** and is paywalled (Wiley/Ovid; no PMC deposit). Do not assert per-member specifics without obtaining the full text.

### Phenotype spectrum inherited from HHT (extrapolated — flag as such)

Frequencies below are for HHT overall (predominantly *ENG*/*ACVRL1* cohorts) and should carry `evidence_source: HUMAN_CLINICAL` with an explicit note that they are **parent-disease frequencies, not HHT4 frequencies**. Per the dismech frequency SOP, prefer omitting `frequency:` on HHT4 phenotypes rather than importing a band that no HHT4 evidence supports.

| Phenotype | HPO term (verified) | Type | Onset | Course | HHT-wide frequency | Source |
|---|---|---|---|---|---|---|
| Recurrent epistaxis | **HP:0000421** Epistaxis | Symptom | mean age 12 y | Recurrent, worsens with age | >90% | PMID:41347972; PMID:20301525 |
| Mucocutaneous telangiectases (lips, tongue, buccal mucosa, fingers, nose) | **HP:0001009** Telangiectasia | Clinical sign | later than epistaxis, may be childhood | Progressive, accumulate with age | ~90% | PMID:20301525 |
| Pulmonary AVM | **HP:0006548** Pulmonary arteriovenous malformation | Structural | Any age; often silent | Stable→enlarging | ~15–50% (higher in HHT1) | PMID:41713948; PMID:16164574 |
| Hepatic AVM / hepatic VM | **HP:0006574** Hepatic arteriovenous malformation | Structural | Adult | Progressive | up to ~70% on imaging (higher in HHT2) | PMID:32894695; PMID:41713948 |
| Cerebral AVM | **HP:0002408** Cerebral arteriovenous malformation | Structural | Congenital/childhood | Static, risk of rupture | ~10% | PMID:20301525; PMID:41704211 |
| Spinal AVM | **HP:0002390** Spinal arteriovenous malformation | Structural | Childhood | Static | <1% | PMID:20301525 |
| GI bleeding | **HP:0002239** Gastrointestinal hemorrhage | Symptom | "rarely seen before age 50 years" | Chronic, progressive | ~15–30% | PMID:20301525 |
| Iron-deficiency anemia | **HP:0001891** Iron deficiency anemia | Lab abnormality | Adult | Chronic, may be severe | ~50% | PMID:41347972 ("iron deficiency anemia in nearly half of all affected individuals") |
| Anemia | **HP:0001903** Anemia | Lab abnormality | — | — | — | PMID:38864625 |
| Paradoxical embolic stroke | **HP:0001297** Stroke | Complication of PAVM | Adult | Episodic | ~10–30% of PAVM carriers | PMID:32894695 |
| Transient ischemic attack | **HP:0002326** Transient ischemic attack | Complication | Adult | Episodic | — | PMID:32894695 |
| Brain abscess | **HP:0030049** Brain abscess | Complication of PAVM (right-to-left shunt) | Adult | Episodic | ~5–10% of PAVM carriers | PMID:20301525 |
| Cerebral hemorrhage | **HP:0001342** Cerebral hemorrhage | Complication of CAVM | Any | Episodic | — | PMID:41704211 |
| Hypoxemia | **HP:0012418** Hypoxemia | Lab/functional | — | Progressive with PAVM | — | PMID:20301525 |
| Dyspnea | **HP:0002094** Dyspnea | Symptom | — | — | — | — |
| Hemoptysis | **HP:0002105** Hemoptysis | Symptom | — | Episodic, can be catastrophic | rare | PMID:40457800 |
| Digital clubbing | **HP:0001217** Clubbing | Sign of chronic shunt | — | — | — | — |
| Polycythemia | **HP:0001901** Polycythemia | Lab | — | — | secondary to hypoxemia | — |
| High-output congestive heart failure | **HP:0001635** Congestive heart failure | Complication of hepatic VM | Adult | Progressive | — | PMID:32894695; PMID:41713948 |
| Pulmonary arterial hypertension | **HP:0002092** Pulmonary arterial hypertension | Complication | Adult | Progressive | 1.5–45% depending on definition | PMID:41713948 |
| Portal hypertension | **HP:0001409** Portal hypertension | Complication of hepatic VM | Adult | Progressive | — | — |
| Migraine | **HP:0002076** Migraine | Symptom | — | Episodic | increased in PAVM | — |
| Autosomal dominant inheritance | **HP:0000006** Autosomal dominant inheritance | Inheritance | — | — | — | PMID:16969873 |

*(All HPO IDs above were verified against the repository's `cache/hp/terms.csv` label cache; each label is the canonical HPO label.)*

### Quality-of-life impact

HHT-wide, not HHT4-specific. The PATH-HHT trial used a validated HHT-specific QoL instrument alongside the Epistaxis Severity Score (ESS) and demonstrated measurable impairment and treatment-responsive improvement: the mean between-group difference in HHT-specific QoL change was **−1.4 points (95% CI −2.6 to −0.3)** on a 0–16 scale (PMID:39292928). Al-Samkari (*Blood* 2024, PMID:38864625) states that "HHT-associated bleeding results in substantial psychosocial morbidity and iron deficiency anemia that may be severe." An expert consensus call for **composite hematologic outcome measures** in HHT was published in 2026 (PMID:42253246).

**Given the 2006 report describes attenuated epistaxis and telangiectases, QoL burden in HHT4 may be driven disproportionately by AVM complications rather than by bleeding — but this is inference, not data.**

---

## 4. Genetic / Molecular Information

### Causal gene: **UNKNOWN**

This is the single most important curated fact. Record it explicitly rather than leaving the gene slot silently empty.

| Attribute | Value | Evidence |
|---|---|---|
| Cytogenetic location | **7p14** | PMID:16969873 |
| Interval | ~7 Mb, flanked by **D7S2252** and **D7S510** | PMID:16969873 |
| Peak marker | **D7S817**, two-point LOD **3.60** | PMID:16969873 |
| Confirmation | Haplotype analysis in the same pedigree | PMID:16969873 |
| Gene | **Not identified (as of Aug 2026)** | PMID:25674101; PubMed sweep, this report |
| Independent replication | **None** — one family only | PubMed sweep, this report |
| Excluded candidates | *BMPER*, *CCM2*, *RALA*, *INHBA* | PMID:16969873 / OMIM:610655 |

McDonald et al. (*Front Genet* 2015, PMID:25674101) confirm the status: "Linkage analysis identified two additional HHT loci at chromosome 5q31 and chromosome 7p14, but the genes still remain unknown." The same review offers an important alternative hypothesis for gene-negative HHT — that "most of the ∼3% of patients with HHT according to Curaçao criteria who are not found to have a mutation … have an undetected deep intronic mutation in *ACVRL1* or *ENG*." **A rigorous entry should carry this as a competing interpretation of the HHT4 family alongside the novel-gene hypothesis.**

### The four established HHT/HHT-overlap genes (context, not HHT4 causes)

HGNC IDs below verified against `cache/hgnc/terms.csv` (lowercase `hgnc:` prefix is canonical in this repository):

| Gene | HGNC | Locus | Disease | Protein role |
|---|---|---|---|---|
| *ENG* | `hgnc:3349` | 9q34.11 | HHT1 (OMIM 187300) | Endoglin, BMP9/10 co-receptor (CD105) |
| *ACVRL1* | `hgnc:175` | 12q13.13 | HHT2 (OMIM 600376) | ALK1, type I BMP receptor serine/threonine kinase |
| *SMAD4* | `hgnc:6770` | 18q21.2 | JP-HHT (MONDO:0008278) | SMAD4, common-mediator SMAD |
| *GDF2* | `hgnc:4217` | 10q11.22 | HHT5 / vascular-anomaly syndrome | BMP9 ligand |

Genes relevant to differential diagnosis: *RASA1* (`hgnc:9871`, CM-AVM1), *EPHB4* (`hgnc:3395`, CM-AVM2), *CCM2* (`hgnc:21708`).

Detection rates: mutations in *ENG* and *ACVRL1* "have been reported to cause up to 85% of HHT," and the Utah group reports "approximately 96% of individuals with HHT have a mutation in these two genes, when published (Curaçao) diagnostic criteria for HHT are strictly applied" (PMID:25674101). The 2026 ERJ review puts it at ">90%" across the three main genes (PMID:41713948). **The residual few percent is the population from which HHT3/HHT4 families were drawn.**

### Pathogenic variants, classification, allele frequency, origin

- **Variant type/class:** unknown for HHT4. No variant has been reported, so no ACMG/AMP classification, no ClinVar record, no gnomAD allele frequency exists for this entity. Do not attribute any variant to HHT4.
- **Origin:** germline, inferred from dominant segregation across the pedigree (PMID:16969873). No somatic component described.
- **Functional consequence:** unknown. The prior — by analogy with *ENG*/*ACVRL1*/*SMAD4*/*GDF2*, in which HHT is "caused by loss-of-function mutations in the BMP9-10/ENG/ALK1/SMAD4 signaling pathway" (PMID:38357927) — is haploinsufficiency/loss of function, but this is untested for HHT4.
- **Modifier genes, epigenetics, chromosomal abnormalities:** nothing reported for HHT4. No DNA-methylation, histone-modification, aneuploidy, translocation, or inversion data exist. Report as "not available."

---

## 5. Environmental Information

- **Environmental factors:** none causal. HHT4 is monogenic.
- **Lifestyle:** no lifestyle factor causes HHT. Management-relevant behavioral factors (avoid vigorous nose blowing, heavy lifting, straining, nasal digital manipulation, NSAIDs/anticoagulants where bleeding is significant, scuba diving unless right-to-left shunt is excluded, liver biopsy) are listed in GeneReviews (PMID:20301525) as **"agents/circumstances to avoid"** — these are tertiary-prevention measures, not etiologic exposures.
- **Infectious agents:** not causal. Relevant only downstream: right-to-left pulmonary shunting permits bacteremic seeding, causing **brain abscess (HP:0030049)** — hence the guideline recommendation for antibiotic prophylaxis before dental and non-sterile invasive procedures, and air-filter precautions on IV lines (PMID:20301525).

No ECTO exposure term is appropriate for this entry; do not force one.

---

## 6. Mechanism / Pathophysiology

### What is established *for HHT4*

**Nothing at the molecular level.** No protein, no pathway, no cell-biological assay, no expression study exists for HHT4. The pathophysiology block should therefore be modeled as **a causal chain from an unidentified 7p14 lesion into the shared HHT effector chain**, with the first edge flagged as inferred.

### The shared HHT mechanism (inherited chain — the honest way to model HHT4 downstream biology)

The canonical, well-evidenced chain (PMID:38357927; PMID:41347972):

1. **Loss-of-function lesion in the BMP9/BMP10–ENG–ALK1–SMAD4 axis** *(MOLECULAR)* — endothelial BMP9/10 ligands bind the ALK1 type I receptor with endoglin as co-receptor; endoglin "serves as a reservoir of these ligands on the surface of ECs, enhancing ligand-induced responses."
   → GO:**GO:0030509** BMP signaling pathway (`DECREASED`/`LOSS_OF_FUNCTION`); GO:**GO:0007179** transforming growth factor beta receptor signaling pathway; GO:**GO:0060395** SMAD protein signal transduction.
2. **Failure of SMAD1/5/8-mediated transcriptional maintenance of endothelial quiescence** *(CELLULAR)* — "The BMP9-10/ENG/ALK1/SMAD4 signaling pathway maintains vascular quiescence by repressing angiogenic pathways" (PMID:38357927).
3. **De-repression of pro-angiogenic signaling, notably the VEGF axis** *(CELLULAR)* — crosstalk with the VEGF pathway is the basis for repurposing anti-VEGF drugs.
   → GO:**GO:0048010** vascular endothelial growth factor receptor signaling pathway (`INCREASED`).
4. **Excessive endothelial proliferation and dysregulated angiogenesis** *(CELLULAR)* — "abnormal activation of angiogenesis, a process causing excessive EC proliferation and hypervascularization."
   → GO:**GO:0001525** angiogenesis (`INCREASED`); GO:**GO:0001935** endothelial cell proliferation (`INCREASED`); GO:**GO:0002040** sprouting angiogenesis.
   → CL:**CL:0000071** blood vessel endothelial cell; CL:**CL:0000115** endothelial cell; CL:**CL:0002543** vein endothelial cell.
5. **Loss of the capillary bed and arteriovenous shunt formation (AVM/telangiectasis)** *(TISSUE)* — "multiple arteriovenous malformations (AVMs) that lack intervening capillaries and result in direct connections between arteries and veins" (PMID:20301525). Mural-cell recruitment is abnormal.
   → GO:**GO:0001974** blood vessel remodeling; CL:**CL:0000192** smooth muscle cell; CL:**CL:0000669** pericyte.
   → UBERON:**UBERON:0001982** capillary; UBERON:**UBERON:0001637** artery.
6. **Two divergent clinical outputs** *(ORGANISM)*:
   - **Fragile superficial lesions → hemorrhage → chronic iron loss → iron-deficiency anemia** (epistaxis, GI bleeding).
   - **Large visceral AVMs → shunt physiology** → hypoxemia and paradoxical embolism (pulmonary), high-output cardiac failure and portal hypertension (hepatic), hemorrhage (cerebral).

### Modifier of the chain: the angiogenic "second hit"

Heterozygous pathway loss alone does not reliably produce AVMs in mice; an angiogenic stimulus (wounding, exogenous VEGF) is required for de novo AVM formation (Park et al. 2009, PMID:19805914). This explains the focal, progressive, age-dependent lesion distribution and is the mechanistic bridge to why puberty and pregnancy modulate the phenotype.

### Protein dysfunction, metabolism, immunity, tissue damage, epigenetics

- **Protein dysfunction:** haploinsufficiency (reduced dosage of a receptor/co-receptor/ligand) rather than aggregation or gain of function, in the four known genes. Unknown for HHT4.
- **Metabolic changes:** no primary metabolic defect. Secondary: iron deficiency from chronic blood loss (CHEBI:18248 iron — verify with OAK before use); hepatic VM can produce a hyperdynamic circulatory state.
- **Immune involvement:** not an autoimmune or immunodeficiency disorder. Immune relevance is limited to loss of pulmonary capillary filtration permitting septic embolization.
- **Tissue damage:** hemorrhage, ischemia (paradoxical embolic stroke), and shunt-driven organ overload; not oxidative stress or fibrosis in the classic sense. Hepatic VM may progress to nodular change and **cirrhosis (HP:0001394)**/portal hypertension.
- **Epigenetics:** no data for HHT4 or for HHT more broadly at a level suitable for curation.

### Molecular profiling and advanced technologies

**No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, or CRISPR-screen dataset exists for HHT4.** There is no GEO/ArrayExpress/PRIDE/MetaboLights accession attributable to this entity. For HHT generally, endothelial-cell transcriptomic and BMP9-response studies exist (e.g., NCT05632484 studies EC genotype–phenotype under BMP9 stimulation in *ACVRL1*/*ENG*/*SMAD4* carriers), and brain-AVM single-cell/genomic work is reviewed in PMID:42106885 — none of it is HHT4-specific.

**Curation guidance:** the `datasets:` block for HHT4 should be left empty rather than populated with parent-disease or gene-only accessions. Per the repository's dataset SOP, a *GENE_ONLY* or relaxed-name search here would necessarily return HHT1/HHT2 data — a textbook Named Entity Confusion route, since HHT4 has no gene to search on.

---

## 7. Anatomical Structures Affected

Inherited from HHT; the 2006 report establishes visceral AVM involvement in the index family but the organ distribution requires full-text confirmation.

### Organ level

| Site | UBERON (verified) | Lesion | Notes |
|---|---|---|---|
| Nasal mucosa | **UBERON:0001826** nasal cavity mucosa | Telangiectases (Little's area) | Source of hallmark epistaxis |
| Lung | **UBERON:0002048** lung | PAVM | Right-to-left shunt → stroke/abscess/hypoxemia |
| Liver | **UBERON:0002107** liver | Hepatic VM (arteriovenous, arterioportal, portovenous shunts) | High-output failure, portal hypertension |
| Brain | **UBERON:0000955** brain | CAVM, micro-AVM | Hemorrhage risk |
| Skin | **UBERON:0002097** skin of body | Telangiectases (fingers, face) | |
| Tongue | **UBERON:0001723** tongue | Telangiectases | |
| Lip | **UBERON:0001834** upper lip | Telangiectases | Characteristic site |
| GI tract | UBERON:0001555 digestive tract *(verify with OAK)* | Mucosal telangiectases | Chronic occult bleeding, typically >50 y |
| Spinal cord | UBERON:0002240 spinal cord *(verify)* | Spinal AVM | Rare |

**Body systems:** cardiovascular (primary), respiratory, hepatobiliary/digestive, nervous, integumentary, hematologic (secondary).

### Tissue and cell level

- **Vascular endothelium** is the primary affected tissue — the disease is endothelial-cell-autonomous in mouse models (endothelial-specific *Acvrl1* depletion suffices; PMID:24896812).
- Cells: **CL:0000115** endothelial cell, **CL:0000071** blood vessel endothelial cell, **CL:0002543** vein endothelial cell, **CL:0000192** smooth muscle cell (mural), **CL:0000669** pericyte.

### Subcellular level

Plasma membrane receptor complex (ALK1/endoglin/BMPRII), cytoplasm→nucleus SMAD shuttling. GO cellular-component terms (`GO:0005886` plasma membrane, `GO:0005634` nucleus) are generic and add little; prefer the biological-process annotations above. No HHT4-specific subcellular data.

### Localization and lateralization

Lesions are **multifocal, bilateral, and asymmetric**, not lateralized. Telangiectases favor the face, oral mucosa, and fingertips; PAVMs favor the lower lobes.

---

## 8. Temporal Development

For HHT4 specifically: the family was ascertained via AVM presentation in adulthood, with mild/infrequent epistaxis that "would be easily missed" (PMID:16969873). No age-of-onset data are published.

Inherited from HHT (PMID:20301525):

- **Onset:** insidious, age-dependent penetrance of individual manifestations. Epistaxis begins on average at **age 12 years**; telangiectases appear later, sometimes in childhood; GI bleeding "is rarely seen before age 50 years." Cerebral AVMs are congenital.
- **Onset pattern:** chronic and insidious, punctuated by acute hemorrhagic or embolic events — "complications from bleeding or shunting may be sudden and catastrophic."
- **Progression:** lesion burden accumulates lifelong; the disease is **progressive in lesion count and severity but not staged** in an oncologic sense. There is no accepted staging system; severity is graded instrumentally (Epistaxis Severity Score 0–10; a change of ≥0.71 points is clinically significant per PMID:39292928).
- **Course pattern:** chronic/lifelong with an episodic bleeding overlay.
- **Remission:** no spontaneous remission. Treatment-induced remission of bleeding is achievable and is now the therapeutic goal.
- **Critical windows:** childhood/adolescence (initial PAVM and CAVM screening), pregnancy (PAVM growth and rupture risk — "sizable pulmonary AVMs discovered during pregnancy are treated during the second trimester"), and the pre-procedural window (prophylaxis before dental/invasive procedures once shunt is known).

---

## 9. Inheritance and Population

### Inheritance

- **Autosomal dominant** (HP:0000006), established by segregation and haplotype analysis in the index pedigree (PMID:16969873).
- **Penetrance:** near-complete for the disease but strongly **age-dependent for individual manifestations** — GeneReviews describes "considerable intrafamilial variability and age-related penetrance of individual manifestations" (PMID:20301525); Anzell et al. call HHT "a near-fully penetrant autosomal dominant disorder" (PMID:40964703). For HHT4 itself, penetrance is unquantified.
- **Expressivity:** highly variable; the JCI review describes HHT as "an inherited vascular disorder with highly variable expressivity" (PMID:38357927). The HHT4 family's mild mucocutaneous phenotype may itself be an expressivity phenomenon rather than a locus-specific signature — **an important, curatable open question**.
- **Anticipation:** none (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported for HHT4; documented occasionally in HHT generally.
- **Founder effects, consanguinity, carrier frequency:** not applicable/unknown for HHT4. A single-family locus has, by definition, a private variant.
- **Recurrence risk:** 50% to offspring of an affected individual; 50% to sibs when a parent is affected (PMID:20301525). **However, predictive genetic testing is impossible in HHT4 families because no variant has been identified** — at-risk relatives must be managed by clinical screening. This is the single most consequential practical difference between HHT4 and HHT1/HHT2.

### Epidemiology

**HHT4 prevalence is effectively 1 known family worldwide.** Curate as `CASES_IN_LITERATURE` / `ULTRA_RARE`, `rate_per_100000` unset — not as an Orphanet band.

Parent-disease epidemiology (for context, explicitly labeled):

| Estimate | Population | Measure | Source |
|---|---|---|---|
| ~1 in 5,000 | General | Point prevalence | PMID:32894695; PMID:38864625; PMID:38357927 |
| 1 in 5,000–7,000 | General | Point prevalence | PMID:41713948 |
| 1:8,000 to ~1:5,000 | Akita prefecture, Japan | Point prevalence | Dakeishi et al. 2002, PMID:11793473 — "roughly comparable with those reported in European and U.S. populations, which is contradictory to the traditional view that HHT is rare among Asians" |
| ~1 in 500,000 (ascertained) | South Korea | Ascertained prevalence | PMID:31455059 — explicitly interpreted as underdiagnosis |
| **2.1–11.9 in 5,000** | gnomAD v4.1, multiple ancestries | Genetically inferred prevalence | Anzell et al., *Circ Genom Precis Med* 2025, PMID:40964703 — "We calculated an HHT prevalence of between 2.1 in 5000 and 11.9 in 5000, or 2 to 12× higher than current estimates … HHT prevalence may be above the threshold of a rare disease" |

Note: the gnomAD-based estimate is *ENG*/*ACVRL1*-only and therefore says nothing about HHT4's contribution — but it does bound the gene-negative fraction indirectly.

**Sex ratio:** approximately 1:1. The Korean series reported 41 males and 71 females among 112 identified patients, but concluded "an almost equal prevalence among men and women" after accounting for ascertainment (PMID:31455059).

**Geographic distribution:** worldwide, no ethnic restriction. Regional high-prevalence pockets in HHT reflect founder variants in *ENG*/*ACVRL1* (e.g., Netherlands Antilles). **The HHT4 family's ancestry should be taken from the full text, not assumed.**

---

## 10. Diagnostics

### Clinical criteria — the operative diagnostic route for HHT4

Because no HHT4 gene test exists, **HHT4 is diagnosed clinically**, by the **Curaçao criteria** (Shovlin et al., *Am J Med Genet* 2000, PMID:10751092). GeneReviews states:

> "The clinical diagnosis of HHT can be established in a proband with at least three of the following diagnostic criteria: recurrent epistaxis; mucocutaneous telangiectases in characteristic locations; visceral AVMs; a first-degree relative diagnosed with HHT on the basis of the preceding criteria."

Three or more criteria = definite; two = possible/suspected; fewer than two = unlikely.

**The 2006 paper's central clinical warning is a criteria-sensitivity warning:** in a family with attenuated epistaxis and subtle telangiectases, an AVM may be the presenting and near-only finding, and "would be easily missed during the typical evaluation and management of a patient with an AVM." Curate this as a diagnostic pitfall.

### Genetic testing

- **Recommended approach:** sequential or panel-based testing of *ACVRL1*, *ENG*, *SMAD4* (± *GDF2*, *RASA1*, *EPHB4*). GeneReviews: "The molecular diagnosis is established by identification of a heterozygous pathogenic variant in *ACVRL1*, *ENG*, or *SMAD4* by molecular genetic testing." McDonald et al. propose "a five gene (*ENG, ACVRL1, SMAD4, RASA1,* and *GDF2*) NGS panel" for suspected hereditary telangiectasia that is not classic HHT (PMID:25674101).
- **HHT4 is, operationally, a diagnosis of exclusion made after this panel is negative** — plus exclusion of linkage to the known loci, which in the original study required family-based analysis.
- **Deletion/duplication analysis** of *ENG*/*ACVRL1* must be included before concluding a family is gene-negative (whole-exon deletions are a recognized cause; e.g., two distinct *ENG* deletions in one family, Wooderchak et al. 2010).
- **WES/WGS:** the appropriate modern approach for a gene-negative family. McDonald et al.: "Recent availability of whole exome and genome testing has created new opportunities to facilitate gene discovery, identify genetic modifiers to explain clinical variability, and potentially define an increased spectrum of hereditary telangiectasia disorders." **WGS is specifically indicated over WES for this population**, because the leading competing hypothesis for gene-negative HHT is a deep intronic *ACVRL1*/*ENG* variant that exome capture cannot see (PMID:25674101).
- **CMA, karyotype, FISH, mtDNA, repeat-expansion testing:** not indicated; no chromosomal or repeat mechanism is implicated.
- **A predictive test for HHT4 relatives does not exist.** Do not curate one.

### Clinical tests, imaging, and screening

Per the Second International Guidelines (PMID:32894695) and GeneReviews (PMID:20301525):

| Purpose | Test | Cadence |
|---|---|---|
| Anemia/iron status | Hematocrit, hemoglobin, **ferritin** | Annual |
| PAVM screening (adults) | **Transthoracic contrast echocardiography (TCE)** — bubble study for right-to-left shunt | Every 5 years |
| PAVM screening (children) | TCE **or** chest radiograph with pulse oximetry | Periodic |
| PAVM characterization | **Contrast chest CT** | When TCE positive |
| CAVM screening | **Brain MRI with and without contrast**, sequences detecting blood products | In infancy, and again by age 18–20 y |
| Hepatic VM | **Doppler ultrasound / contrast CT**; clinical evaluation for heart or liver failure | Adults, at diagnosis |
| GI lesions | Endoscopy/colonoscopy as indicated; in **SMAD4**-related HHT, colonoscopy from age 15 y | See JPS guidance |
| Bleeding severity | **Epistaxis Severity Score (ESS)**, 0–10, validated | Serial |
| PH assessment | **Right heart catheterization** for haemodynamic classification — "Accurate haemodynamic classification by right heart catheterisation is essential to determine the predominant mechanism" (PMID:41713948) | When PH suspected |

**Contraindicated/avoid:** liver biopsy (PMID:20301525).

**Biopsy/histopathology:** biopsy is not part of HHT diagnosis. Histology of a telangiectasis shows dilated post-capillary venules connecting directly to arterioles with loss of the intervening capillary bed and perivascular mononuclear infiltrate — reported for HHT generally, never for HHT4 tissue.

**Omics-based diagnostics:** none validated for HHT of any type. No liquid biopsy, no proteomic or metabolomic diagnostic. Biomarker research exists but is exploratory (see PMC4379940, "Research on potential biomarkers in hereditary hemorrhagic telangiectasia").

### Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| HHT1 (*ENG*), HHT2 (*ACVRL1*) | Identified pathogenic variant; HHT1 skews to PAVM/CAVM, HHT2 to hepatic VM and PAH (PMID:16164574; PMID:41713948) |
| HHT3 (5q31.3–q32) | Different locus; **do not confuse with HHT4** |
| JP-HHT (*SMAD4*, MONDO:0008278) | Juvenile GI polyposis + HHT features; requires polyposis surveillance |
| HHT5 / *GDF2*-related | BMP9 ligand defect, HHT-like/overlapping phenotype |
| CM-AVM1 (*RASA1*) / CM-AVM2 (*EPHB4*) | Multifocal capillary malformations with a pale halo; fast-flow lesions; PMID:25674101 |
| Cerebral cavernous malformation (*CCM1/2/3*) | Cavernomas, not AVMs; no epistaxis/telangiectases |
| CREST/systemic sclerosis | Telangiectases with sclerodactyly, Raynaud, anticentromere antibodies; no visceral AVM |
| Ataxia-telangiectasia | Oculocutaneous telangiectases, ataxia, immunodeficiency, radiosensitivity; recessive |
| Generalized essential telangiectasia | No AVMs, no bleeding diathesis, sporadic |
| Isolated/sporadic PAVM or brain AVM | No family history, no mucocutaneous lesions — **but note the 2006 warning that HHT4 can masquerade as exactly this** |

### Screening for asymptomatic individuals

Cascade screening in an HHT4 family must be **clinical**, not molecular: "If the pathogenic variant in the family is not known, at-risk family members should be evaluated for signs and symptoms of HHT, and screening should be offered to at-risk family members if the diagnosis cannot be ruled out" (PMID:20301525). No newborn or population carrier screening exists or is indicated.

---

## 11. Outcome / Prognosis

No HHT4-specific outcome data exist. Parent-disease data:

### Survival and mortality

The best population-based evidence is the 20-year Danish follow-up of an unselected County of Fyn cohort (Kjeldsen et al. 2016, PMID:27876060): 73 HHT patients and 218 matched controls.

> "A total of 32 (44%) HHT patients and 97 (44%) controls passed away during follow-up. The survival curves were evenly distributed showing similar survival rates in the two groups. … The mortality was not increased among Danish HHT patients compared to controls."

The authors emphasize this reflects "a clinical unselected series of HHT patients with the whole spectrum of severity" — i.e., **HHT in a well-managed population is compatible with normal life expectancy**, though referral-center series with severe visceral disease report excess early mortality. There is no 5-/10-year survival convention for HHT (not a malignancy).

**Cancer:** reduced incidence in HHT patients versus controls (5% vs 17%) in the same study — an intriguing, angiogenesis-consistent finding.

### Morbidity, disability, quality of life

Driven by (a) chronic bleeding → transfusion-dependent iron-deficiency anemia and fatigue; (b) AVM complications → stroke, brain abscess, hemorrhage, high-output heart failure, PH. Al-Samkari (PMID:38864625): HHT "affects 1 in 5000 persons, making it the second most common inherited bleeding disorder worldwide," and HHT-associated bleeding "results in substantial psychosocial morbidity and iron deficiency anemia that may be severe."

Instruments: **Epistaxis Severity Score** (disease-specific, validated), **HHT-specific QoL score** (0–16), plus generic EQ-5D/SF-36. A 2026 expert group has called for composite hematologic endpoints (PMID:42253246).

### Complications (curatable list)

Iron-deficiency anemia; transfusion dependence; paradoxical embolic stroke and TIA; brain abscess; intracerebral hemorrhage; hemothorax/hemoptysis from PAVM rupture; high-output cardiac failure; portal hypertension and biliary ischemia from hepatic VM; **pulmonary hypertension** — "PH is a recognised but heterogeneous complication of HHT, with reported prevalence ranging widely from 1.5% to 45%, depending on diagnostic methods and study populations" (PMID:41713948); pregnancy-associated PAVM hemorrhage; atrial fibrillation management dilemmas (anticoagulation vs bleeding — see the 2026 left-atrial-appendage-closure study, PMID:41506960).

### Prognostic factors

Genotype (in the known genes), AVM organ distribution and size, baseline ESS and hemoglobin/ferritin, presence of PH or high-output failure, and access to an HHT Center of Excellence. **HHT4 has no genotype-based prognostic information — its prognosis must be assessed lesion-by-lesion.** No validated prognostic biomarker exists for any HHT type.

---

## 12. Treatment

**Treatment of HHT4 is identical to treatment of HHT** — it is organ- and symptom-directed, and none of it requires knowing the gene. This is the reassuring practical corollary of the unidentified locus, and worth stating explicitly in the entry.

**Regulatory status:** as of the 2024 JCI review, "this not-so-uncommon bleeding disorder still currently lacks any FDA- or European Medicines Agency-approved (EMA-approved) therapies" (PMID:38357927), reiterated in *Blood* 2024: "there remain no regulatory agency-approved therapies for HHT" (PMID:38864625). All pharmacotherapy is off-label repurposing.

### Systemic pharmacotherapy

| Therapy | Modality | Target/mechanism | Evidence | Ontology |
|---|---|---|---|---|
| **Tranexamic acid** (oral) | SMALL_MOLECULE | Antifibrinolytic | RCT-supported for mild-to-moderate bleeding (PMID:38864625); first-line per GeneReviews 2026 | NCIT:C15986 Pharmacotherapy + **CHEBI:48669** tranexamic acid |
| **Bevacizumab** (IV) | MONOCLONAL_ANTIBODY | Anti-VEGF-A; blocks the de-repressed proangiogenic arm | "systemic antiangiogenic drugs including pomalidomide and bevacizumab for moderate-to-severe bleeding" (PMID:38864625); listed as targeted therapy in GeneReviews 2026 | NCIT:C15986 + **NCIT:C2039** Bevacizumab |
| **Pomalidomide** (oral, 4 mg daily) | SMALL_MOLECULE | Immunomodulatory/antiangiogenic | **PATH-HHT RCT (NCT03910244)**, PMID:39292928 — see below | NCIT:C15986 + **CHEBI:72690** pomalidomide |
| **Pazopanib** (oral) | SMALL_MOLECULE | Multi-target VEGFR TKI | GeneReviews 2026: "pomalidomide or pazopanib for refractory epistaxis and GI bleeding" | NCIT:C15986 + **CHEBI:71219** pazopanib |
| **Thalidomide** | SMALL_MOLECULE | Antiangiogenic (predecessor to pomalidomide) | Older series | **CHEBI:9513** thalidomide |
| **Iron replacement** ± transfusion | SMALL_MOLECULE / procedure | Repletes chronic loss | Guideline-recommended (PMID:32894695) | NCIT:C15747 Supportive Care; **NCIT:C15192** Blood Transfusion |
| Topical timolol / propranolol; doxycycline; sirolimus/tacrolimus | Various | Investigational | Small studies only | **CHEBI:39465**, **CHEBI:8499**, **CHEBI:50845**, **CHEBI:9168** |

**PATH-HHT, the practice-changing trial (Al-Samkari et al., *N Engl J Med* 2024;391:1015–1027; PMID:39292928; NCT03910244):**

> "The trial was closed to enrollment in June 2023 after a planned interim analysis met a prespecified threshold for efficacy. A total of 144 patients underwent randomization; 95 patients were assigned to receive pomalidomide and 49 to receive placebo. … At 24 weeks, the mean difference between the pomalidomide group and the placebo group in the change from baseline in the Epistaxis Severity Score was −0.94 points (95% confidence interval [CI], −1.57 to −0.31; P = 0.004). … Adverse events that were more common in the pomalidomide group than in the placebo group included neutropenia, constipation, and rash."

> "Among patients with HHT, pomalidomide treatment resulted in a significant, clinically relevant reduction in epistaxis severity."

Note pomalidomide's teratogenicity (thalidomide analog) — REMS-equivalent contraception requirements apply.

**Paradigm shift (curate as a treatment-strategy claim):** "This has led to a recent paradigm shift away from repetitive temporizing procedural management toward effective systemic medical therapeutics to treat bleeding in HHT" (PMID:38864625).

### Procedural and surgical

| Intervention | Indication | Ontology |
|---|---|---|
| **Transcatheter embolization of PAVM** | Feeding vessel ≥2–3 mm — "typically require occlusion for stroke prevention" (PMID:20301525) | **NCIT:C15230** Embolization Therapy; **NCIT:C15917** Arterial Embolization |
| Nasal ablation (laser, coblation), **septodermoplasty**, **Young's procedure** (nasal closure) | Refractory epistaxis | **NCIT:C15466** Laser Therapy; NCIT:C15329 Surgical Procedure |
| Sclerotherapy | Selected lesions | **NCIT:C62732** Sclerotherapy |
| CAVM: microsurgery, embolotherapy, **stereotactic radiosurgery** | "as indicated by size, location, or symptoms" | NCIT:C15313 Radiation Therapy; NCIT:C15329 |
| **Liver transplantation** | "recommended for individuals who do not respond to medical therapy and who develop refractory high-output heart failure" | **NCIT:C15271** Liver Transplantation |
| Left atrial appendage closure | AF with HHT bleeding risk (emerging; PMID:41506960) | NCIT:C15329 |

### Supportive, preventive and counseling

- Humidification, topical nasal moisturizers, hemostatic products.
- **Antibiotic prophylaxis** before dental and non-sterile invasive procedures when pulmonary shunting is present; **air filters** on IV lines to prevent paradoxical air embolism.
- **Genetic counseling** (**NCIT:C15240**) — in HHT4 this must cover the *absence* of a testable variant and the consequent reliance on clinical screening for at-risk relatives.
- Pregnancy: pre-conception PAVM/CAVM screening; treat sizable PAVMs in the second trimester; prefer iron repletion over transfusion for anemia (PMID:20301525; PMID:32894695).

### Advanced therapeutics and pipeline

No gene therapy, cell therapy, RNA therapy, or gene editing is available for HHT. **Gene-directed therapy is by definition impossible for HHT4 until the gene is identified** — a clean, citable rationale for gene discovery. Kasthuri (ASH Education Program 2025, PMID:41347972) describes the pipeline:

> "The initial clinical studies evaluating medications for the treatment of HHT have involved repurposing drugs that were previously approved for other indications. In the wake of these efforts, several therapies specifically for HHT are currently being developed and are in preclinical studies and early phase human trials or may soon start pivotal phase III trials."

### Pharmacogenomics

None established for HHT. No CPIC/PharmGKB HHT guideline exists.

---

## 13. Prevention

- **Primary prevention:** not possible — the disease is germline and monogenic. Only reproductive options (preimplantation or prenatal genetic testing) prevent transmission, and **these are unavailable in HHT4 because no variant is known.** This is a concrete, citable harm of the unresolved locus.
- **Secondary prevention (the main lever):** presymptomatic detection of PAVMs and CAVMs in clinically at-risk relatives, followed by preemptive embolization to prevent stroke and brain abscess. The full screening cadence is in §10.
- **Tertiary prevention:** antibiotic prophylaxis and IV air filters in shunt carriers; avoidance of anticoagulants/NSAIDs where bleeding is significant; avoidance of scuba diving "unless TCE within the last five years was negative for evidence of a right-to-left shunt"; avoidance of vigorous nose blowing, heavy lifting, straining, and nasal digital manipulation; avoidance of liver biopsy (all PMID:20301525).
- **Immunization:** no vaccine relevance beyond routine care.
- **Genetic screening:** cascade *molecular* screening is standard in HHT1/HHT2/JP-HHT and **impossible in HHT4**; cascade *clinical* screening substitutes.
- **Public health / environmental interventions:** not applicable. The relevant public-health issue is **underdiagnosis** — supported by the Korean ascertained prevalence of ~1/500,000 against an expected ~1/5,000 (PMID:31455059) and the gnomAD-derived 2–12× upward revision (PMID:40964703).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens*, **NCBITaxon:9606**. HHT4 is described only in humans.
- **Breed:** not applicable; no VBO term.
- **Orthologous genes:** **cannot be specified** — the causal gene is unknown, so no ortholog can be named. Any orthology statement in an HHT4 entry would be fabrication. (For the known HHT genes, mouse *Eng*, *Acvrl1*, *Smad4*, *Gdf2* and zebrafish *acvrl1* are the orthologs of interest.)
- **Natural disease in other species:** no naturally occurring HHT-equivalent is recorded in OMIA for any species for any HHT type. Vascular malformations occur in companion animals but are not established as an HHT homolog.
- **Comparative biology:** the BMP9/10–ALK1–endoglin–SMAD axis is deeply conserved across vertebrates — zebrafish *acvrl1* disruption (the *violet beauregarde* mutant) produces cranial vessel endothelial-cell excess and shunting (Roman et al., *Development* 2002;129:3009–19, PMID:12050147), demonstrating conservation of the arteriovenous-patterning function down to teleosts.
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious, germline genetic).

---

## 15. Model Organisms

### The HHT4-specific position

**There is no HHT4 model of any kind — no mouse, no zebrafish, no cell line, no iPSC, no organoid, no computational model.** Building one requires the gene. Any model listed under an HHT4 entry must be curated as a **model of the shared HHT mechanism**, and — under the dismech `ModelMechanismLink` semantics — should attach only to the downstream, pathway-level nodes (dysregulated BMP signaling → excess angiogenesis → AVM), **never** to the "7p14 locus lesion" trigger node, which no model reproduces. A `HUMAN_MODEL_MISMATCH` discussion is warranted: these models carry *ENG*/*ACVRL1* lesions, and their relevance to HHT4 rests entirely on the unproven assumption that the HHT4 gene lies in the same pathway.

### Models available for HHT (shared mechanism)

| Model | Type | Genotype/manipulation | Recapitulation | Key limitation | PMID |
|---|---|---|---|---|---|
| Endothelial-specific *Acvrl1* depletion, mouse | Conditional KO (mammalian, in vivo) | Cdh5-CreERT2; *Acvrl1*^fl/fl | AVMs form, with **reduced endoglin expression** — links the two HHT1/HHT2 genes mechanistically | Induced, adult/neonatal retina model; not a heterozygous germline model of human disease | 24896812 |
| ALK1 conditional KO with angiogenic trigger, mouse | Conditional KO + wound/VEGF | *Alk1* deletion + local angiogenic stimulus | **Real-time de novo AVM formation imaged**; establishes the "second hit" requirement | Requires an artificial trigger; not spontaneous | 19805914 |
| Transmammary anti-BMP9/BMP10 immunoblockade, mouse | Ligand blockade (non-genetic, in vivo) | Neutralizing antibodies delivered via milk to neonates | HHT-like vascular phenotype without a germline mutation | Ligand blockade ≠ receptor haploinsufficiency; neonatal window only | 27874028 |
| *acvrl1* mutant zebrafish (*violet beauregarde*) | Invertebrate-adjacent vertebrate genetic model | *acvrl1* loss | "Disruption of acvrl1 increases endothelial cell number in zebrafish cranial vessels" — cranial AV shunting | Embryonic/larval; no mucocutaneous telangiectasis, no epistaxis, no GI bleeding | 12050147 |
| *Eng*+/−, *Acvrl1*+/− mice | Germline heterozygous KO | — | Closest to human genotype but **low-penetrance, strain-dependent** lesions | Poor and inconsistent phenotype penetrance — the classic limitation of HHT mouse genetics | (reviewed in 38357927) |
| Patient-derived endothelial cells / BOECs | In vitro (human) | *ENG*/*ACVRL1*/*SMAD4* carrier ECs, BMP9 stimulation | Signaling readouts, not lesions | Cannot model tissue-level AVM | NCT05632484 |

**What models cannot capture** (curate as limitations): epistaxis and the nasal mucosal microenvironment; the age-dependent human accrual of telangiectases; GI bleeding after age 50; the human-specific organ distribution of visceral AVMs; and — critically for this entry — anything at all about the HHT4 lesion.

**Resources:** MGI (mouse *Eng*, *Acvrl1*, *Smad4*), ZFIN (*acvrl1*), IMPC/KOMP, Alliance of Genome Resources.

---

## Curation recommendations specific to this entry

1. **Model the gene slot as an explicit locus, not an absence.** Record `7p14`, flanking markers `D7S2252`/`D7S510`, peak marker `D7S817`, LOD 3.60 — and a first-class statement that no causal gene is known.
2. **Add a `KNOWLEDGE_GAP` discussion** on gene identity, with proposed experiments: WGS (not WES) of the original pedigree with deep-intronic and structural-variant analysis of *ACVRL1*/*ENG*; re-contact and re-phenotyping; RNA-seq of patient endothelial cells for aberrant splicing.
3. **Add a competing-interpretation discussion** citing McDonald et al. (PMID:25674101): a deep intronic *ACVRL1*/*ENG* variant is a live alternative to a novel 7p14 gene, and is not excluded by the 2006 linkage data alone.
4. **Add a `HUMAN_MODEL_MISMATCH` discussion** for any model-organism evidence imported: all existing HHT models carry known-gene lesions.
5. **Add an INTERPRETATION note on the HHT3/HHT4 transposition hazard** (5q31.3–q32 vs 7p14) — this is exactly the Named Entity Confusion class that passes every automated check.
6. **Do not populate `datasets:`.** With no gene and no cohort, every discoverable accession would be a *GENE_ONLY* or wrong-disease hit.
7. **Frequencies:** omit `frequency:` on phenotypes rather than importing HHT-wide bands; the one HHT4-specific phenotypic claim is *reduced* severity of epistaxis and telangiectases.
8. **Prevalence:** curate as `CASES_IN_LITERATURE` / `ULTRA_RARE` with no numeric rate; put the 1/5,000 parent figure on the parent entry.
9. **Treatments** can be inherited from HHT in full with high confidence, because HHT management is gene-agnostic — but gene therapy and reproductive genetic testing must be recorded as **unavailable for HHT4 specifically**.

---

## Evidence quality summary

| Claim class | Best evidence | Grade |
|---|---|---|
| 7p14 linkage, LOD 3.60, 7 Mb interval | PMID:16969873 | Single family, single publication, **unreplicated** |
| Attenuated epistaxis/telangiectasia phenotype | PMID:16969873 (abstract, verbatim) | Single family; per-member detail in paywalled full text |
| Gene remains unidentified | PMID:25674101 + PubMed sweep (Aug 2026) | Strong negative evidence |
| Autosomal dominant inheritance | PMID:16969873; PMID:20301525 | Established |
| Shared HHT pathophysiology (BMP9/10–ENG–ALK1–SMAD4) | PMID:38357927; PMID:41347972 | Strong — but **extrapolated** to HHT4 |
| Diagnostic criteria and screening | PMID:10751092; PMID:32894695; PMID:20301525 | Guideline-grade |
| Pomalidomide efficacy | PMID:39292928 (RCT, n=144) | Level 1, parent disease |
| Prevalence 1/5,000; possibly 2–12× higher | PMID:11793473; PMID:40964703 | Parent disease only |
| Normal survival in an unselected cohort | PMID:27876060 | Parent disease, population-based |
| Any HHT4-specific molecular, omics, model, or biomarker claim | **None exists** | Must be curated as absent |

---

## Sources

- [A fourth locus for hereditary hemorrhagic telangiectasia maps to chromosome 7 — PubMed (PMID:16969873)](https://pubmed.ncbi.nlm.nih.gov/16969873/)
- [OMIM 610655 — TELANGIECTASIA, HEREDITARY HEMORRHAGIC, TYPE 4](https://omim.org/entry/610655)
- [MedGen 341824 — Hereditary hemorrhagic telangiectasia type 4](https://www.ncbi.nlm.nih.gov/medgen/341824)
- [Hereditary Hemorrhagic Telangiectasia — GeneReviews (PMID:20301525, updated 19 Feb 2026)](https://www.ncbi.nlm.nih.gov/books/NBK1351/)
- [McDonald et al. 2015, HHT: genetics and molecular diagnostics in a new era (PMID:25674101)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306304/)
- [Al Tabosh et al. 2024, JCI — HHT: from signaling insights to therapeutic advances (PMID:38357927)](https://www.jci.org/articles/view/176379)
- [Al-Samkari et al. 2024, NEJM — Pomalidomide for Epistaxis in HHT (PMID:39292928)](https://pubmed.ncbi.nlm.nih.gov/39292928/)
- [Al-Samkari 2024, Blood — How I treat bleeding in HHT (PMID:38864625)](https://pubmed.ncbi.nlm.nih.gov/38864625/)
- [Kasthuri 2025, ASH Education Program — What's new in HHT (PMID:41347972)](https://pubmed.ncbi.nlm.nih.gov/41347972/)
- [Faughnan et al. 2020, Second International Guidelines for HHT (PMID:32894695)](https://pubmed.ncbi.nlm.nih.gov/32894695/)
- [Jutant et al. 2026, ERJ — Pulmonary hypertension associated with HHT (PMID:41713948)](https://pubmed.ncbi.nlm.nih.gov/41713948/)
- [Anzell et al. 2025, Circ Genom Precis Med — HHT prevalence from gnomAD (PMID:40964703)](https://pubmed.ncbi.nlm.nih.gov/40964703/)
- [Kjeldsen et al. 2016, 20-year follow-up of Danish HHT patients (PMID:27876060)](https://pubmed.ncbi.nlm.nih.gov/27876060/)
- [Dakeishi et al. 2002, Genetic epidemiology of HHT in northern Japan (PMID:11793473)](https://pubmed.ncbi.nlm.nih.gov/11793473/)
- [Kim et al. 2019, HHT in South Korea (PMID:31455059)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6736501/)
- [Cole et al. 2005, A new locus for HHT (HHT3) maps to chromosome 5 (PMID:15879500)](https://pubmed.ncbi.nlm.nih.gov/15879500/)
- [Govani & Shovlin 2010, Fine mapping of the HHT3 locus (PMID:20701797)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2924844/)
- [Park et al. 2009, JCI — Real-time imaging of de novo AVM in an HHT mouse model (PMID:19805914)](https://pubmed.ncbi.nlm.nih.gov/19805914/)
- [Tual-Chalot et al. 2014, Endothelial depletion of Acvrl1 in mice (PMID:24896812)](https://pubmed.ncbi.nlm.nih.gov/24896812/)
- [Ruiz et al. 2016, Transmammary immunoblocking of BMP9/BMP10 mouse model (PMID:27874028)](https://www.nature.com/articles/srep37366)
- [Roman et al. 2002, Disruption of acvrl1 in zebrafish cranial vessels (PMID:12050147)](https://pubmed.ncbi.nlm.nih.gov/12050147/)
- [MONDO:0012532 via EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO%3A0012532)
- [Orphanet — Hereditary hemorrhagic telangiectasia (ORPHA:774, parent concept)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=774)

**Note on ontology terms:** all HPO, GO, CL, UBERON, NCIT, CHEBI, HGNC, and MONDO identifiers presented in tables above were checked against this repository's local term caches and carry their canonical labels, except where marked *(verify with OAK)* — those are suggestions requiring `just validate-terms` confirmation before use.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 31 |
| On topic | 25 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:38357927` *(abstract only)*: "The BMP9-10/ENG/ALK1/SMAD4 signaling pathway maintains vascular quiescence by repressing angiogenic pathways"
  - closest text in source: "HHT is caused by loss-of-function mutations in the BMP9-10/ENG/ALK1/SMAD4 signaling pathway"