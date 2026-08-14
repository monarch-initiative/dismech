---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:56:42.735808'
end_time: '2026-08-01T21:21:38.105173'
duration_seconds: 1495.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 7
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
  web_search_requests: 25
  num_turns: 67
  total_cost_usd: 6.09735725
  session_id: b05aac37-96c9-40e3-8522-47d34c80d4bc
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 7
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 7** covering all of the
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

# Hypertrophic Cardiomyopathy 7 (CMH7 / TNNI3-Related HCM)
## Comprehensive Disease Characteristics Research Report

**Prepared:** 2026-08-01 · **Target:** Hypertrophic Cardiomyopathy 7 · **Category:** Genetic (Mendelian, autosomal dominant)

> **Verification note for downstream curation.** Ontology IDs marked ✅ were verified locally with OAK against `sqlite:obo:{mondo,hp,go,cl,uberon,ncit}` during this research session. Quotations marked **[verbatim]** were retrieved from the PubMed abstract record and are exact-substring candidates for `snippet:` fields. Statements marked **[paraphrase]** were summarized by an intermediary and **must be re-verified against the cached abstract with `just fetch-reference` + `just validate-references` before being used as an evidence snippet.**

---

## 1. Disease Information

### 1.1 Overview

Hypertrophic cardiomyopathy 7 (CMH7) is the designation in the OMIM/MONDO numbered-series nosology for **hypertrophic cardiomyopathy caused by heterozygous pathogenic variants in `TNNI3`**, the gene encoding cardiac troponin I (cTnI), the inhibitory subunit of the cardiac thin-filament troponin complex. It is one of the "thin-filament" sarcomeric hypertrophic cardiomyopathies, mechanistically and prognostically distinguishable from the far more common "thick-filament" forms caused by `MYBPC3` and `MYH7`.

`TNNI3` was established as the **seventh** HCM disease gene by Kimura and colleagues in 1997 — hence the numeral in "CMH7" (Kimura et al., *Nat Genet* 1997;16(4):379-82; PMID:9241277):

> **[verbatim]** "Because all the known disease genes encode major contractile elements in cardiac muscle, we have systematically characterized the cardiac sarcomere genes, including cardiac troponin I (cTnI), cardiac actin (cACT) and cardiac troponin C (cTnC) in 184 unrelated patients with HCM and found mutations in the cTnI gene in several patients. Family studies showed that an Arg145Gly mutation was linked to HCM and a Lys206Gln mutation had occurred de novo, thus strongly suggesting that cTnI is the seventh HCM gene."

CMH7 is **not** a clinically separable entity at the bedside — a patient with `TNNI3`-HCM presents as HCM. The entry's justification is genotype-anchored: `TNNI3` variants carry a distinctive **allelic-series signature** (HCM ↔ restrictive cardiomyopathy ↔ dilated cardiomyopathy from the same gene, sometimes the same variant), a distinctive **mechanistic signature** (myofilament Ca²⁺ sensitization with impaired relaxation rather than primary hypercontractility), and, for at least one variant, a distinctive **prognostic signature** (malignant early sudden death).

### 1.2 Key Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** ✅ | **MONDO:0013369** — *hypertrophic cardiomyopathy 7* | Verified via OAK. Def: *"Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the TNNI3 gene."* `is_a` MONDO:0024573 (familial hypertrophic cardiomyopathy); `RO:0004003` → HGNC:11947 (TNNI3); subsets: `rare`, `nord_rare`, `gard_rare` |
| **OMIM (phenotype)** | **#613690** — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 7; CMH7 | |
| **OMIM (gene)** | ***191044** — TROPONIN I, CARDIAC; TNNI3 | |
| **DOID** | DOID:0110313 | MONDO xref |
| **MedGen / UMLS** | C1860752 (MedGen UID 348695) | |
| **GARD** | GARD:0024916 | |
| **HGNC** | **HGNC:11947** (`hgnc:11947` in dismech lowercase convention) | |
| **NCBI Gene** | 7137 | |
| **UniProt** | **P19429** (TNNI3_HUMAN) | 210 aa, 24,008 Da |
| **Cytogenetic location** | **19q13.42** | OMIM renders as 19q13 |
| **Orphanet** | No CMH7-specific ORPHA code. Parent: **ORPHA:217569** (Familial isolated hypertrophic cardiomyopathy) — *verify code before citing* |
| **ICD-10** | **I42.1** (obstructive HCM) / **I42.2** (other HCM) | No CMH7-specific code |
| **ICD-11** | **BC43.00** Hypertrophic cardiomyopathy (approximate; verify) |
| **MeSH** | D002312 (Cardiomyopathy, Hypertrophic) / D024741 (Cardiomyopathy, Hypertrophic, Familial) |
| **ClinGen GCEP** | TNNI3 — **Definitive** for autosomal dominant HCM |

### 1.3 Synonyms and Alternative Names

From the verified MONDO record (OAK output):
- **CMH7** (EXACT; DOID:0110313, OMIM:613690)
- **TNNI3 hypertrophic cardiomyopathy** (EXACT; MONDO design pattern)
- hypertrophic cardiomyopathy caused by mutation in TNNI3 (EXACT)
- cardiomyopathy, familial hypertrophic, type 7 (EXACT)
- cardiomyopathy, hypertrophic, 7 (EXACT)
- hypertrophic cardiomyopathy type 7 (EXACT)
- cardiomyopathy, familial hypertrophic, 7 (RELATED)

Additional literature/GTR synonyms: *TNNI3-related familial hypertrophic cardiomyopathy*; *cardiac troponin I–related HCM*; *thin-filament HCM (TNNI3 subtype)*. Note that GTR also lists "CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 7, MODIFIER OF" — a distinct OMIM concept for modifier alleles.

### 1.4 Provenance of the Information

Content for this entry derives from **aggregated disease-level resources** (OMIM, MONDO, ClinVar/ClinGen, HPO, UniProt) layered on **primary human-clinical literature** — family linkage studies (Kimura 1997; Mogensen 2003), multicenter genotype–phenotype cohorts (Coppini 2014; Pua 2020), and founder-population cascade screening (Fahed 2020) — plus **model-organism** (transgenic and knock-in mouse) and **in vitro** (skinned fiber, iPSC-CM, engineered heart tissue) mechanistic work. There is no EHR/individual-patient data source specific to CMH7 in this report; the population-scale genetic architecture data (Pua 2020) come from case–control sequencing rather than EHR phenotyping.

---

## 2. Etiology

### 2.1 Disease Causal Factors

CMH7 is a **monogenic, autosomal dominant, primary sarcomeric disorder**. The causal factor is a heterozygous (rarely homozygous/compound heterozygous) variant in `TNNI3` that alters cardiac troponin I protein sequence. ClinGen's Hereditary Cardiovascular Disease GCEP classified the mechanism as **"altered gene product sequence"** with monoallelic inheritance — i.e., missense/in-frame variants acting through a **poison-peptide / dominant-negative** route, *not* haploinsufficiency. This is a crucial curation point: `TNNI3` truncating variants are **not** an established cause of HCM (and where biallelic truncating variants occur, the phenotype is lethal infantile dilated cardiomyopathy, a different entity).

The 2025 ClinGen reappraisal (Hespe et al., *J Am Coll Cardiol* 2025;85(7):727-740; PMID:39971408; DOI:10.1016/j.jacc.2024.12.010) confirmed **TNNI3 = Definitive** for autosomal dominant HCM, one of only nine definitive sarcomere HCM genes.

There is **no infectious, toxic, or acquired etiology** for CMH7 itself. Environmental factors act only as modifiers/triggers (§2.3, §5).

### 2.2 Genetic Risk Factors

**Primary causal variants (§4 for full detail).** The dominant genetic risk factor *is* the `TNNI3` variant.

**Low-penetrance risk alleles.** A distinct and curation-relevant category: some `TNNI3` missense variants behave as **population-enriched, low-penetrance risk alleles** rather than high-penetrance Mendelian variants. Pua et al. (*Circ Genom Precis Med* 2020; PMID:32815737) reported:

> **[verbatim]** "Two missense variants in thin filament encoding genes were commonly seen in Singaporean HCM (TNNI3:p.R79C, disease allele frequency [AF]=0.018; TNNT2:p.R286H, disease AF=0.022) and are enriched in Singaporean HCM when compared with Asian controls. Both variants have conflicting annotations in ClinVar and are of low penetrance but predicted deleterious."

> **[verbatim]** "Chinese HCM patients commonly have low penetrance risk alleles in TNNT2 or TNNI3 but exhibit few clinically actionable HCM variants overall, highlighting the need for greater study of HCM genetics in non-White populations."

UniProt additionally annotates **p.Pro82Ser (rs77615401)** as a **"CMH7 risk"** allele rather than a fully penetrant causal variant.

**Modifier genes and oligogenic burden.** Multiple sarcomere variants (compound/double heterozygosity) confer earlier onset and worse outcomes in HCM generally; low-penetrance sarcomere variants contribute additively to HCM risk (see *Circulation* 2024/2025, "Low Penetrance Sarcomere Variants Contribute to Additive Risk in Hypertrophic Cardiomyopathy" — verify PMID before citing). HCM polygenic background scores modulate penetrance in genotype-positive individuals. **No `TNNI3`-specific modifier locus has been established.** OMIM does carry a separate concept "CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 7, MODIFIER OF," reflecting variants that modify rather than cause.

**Family history** is the single strongest clinical genetic risk factor: first-degree relatives of a proband have a 50% prior probability of carrying the variant.

### 2.3 Environmental Risk Factors

No environmental exposure causes CMH7. Established **phenotype modifiers / event triggers** in HCM broadly, applicable to CMH7:
- **Intense competitive/burst exertion** — historically the classic trigger for SCD in HCM; the 2024 AHA/ACC guideline substantially liberalized exercise restrictions relative to prior guidance (PMID:38718139).
- **Hypertension, obesity, and metabolic syndrome** — amplify LV hypertrophy and accelerate progression to heart failure.
- **Male sex** — associated with earlier diagnosis and greater hypertrophy in HCM generally. Notably, in the `TNNI3` p.Arg21Cys founder cohort, **no sex difference in SCD was observed** (46.4% women vs 48.3% men) **[paraphrase]**.
- **Age** — age-dependent penetrance; hypertrophy typically emerges during adolescent growth spurt or, for a `TNNI3`-enriched subset, in the sixth–seventh decade (§8).
- **Dehydration, vasodilators, and sudden preload reduction** — provoke dynamic LVOT obstruction in the obstructive subset.

### 2.4 Protective Factors

- **Genetic:** Being genotype-negative in a family with a known pathogenic `TNNI3` variant is definitively protective; the 2024 AHA/ACC guideline recommends discharging such relatives from surveillance unless the variant is later reclassified. No established protective `TNNI3` allele or protective modifier haplotype has been reported.
- **Environmental/therapeutic:** Blood-pressure and weight control; avoidance of dehydration and volume depletion; ICD placement (secondary/primary prevention of arrhythmic death). Whether early disease-modifying pharmacotherapy in genotype-positive/phenotype-negative carriers prevents phenotype development remains **unproven** — this is the central open question of the VANISH-type trial paradigm (valsartan in early sarcomeric HCM) and of ongoing cardiac myosin inhibitor prevention studies.

### 2.5 Gene–Environment Interactions

The best-documented G×E axis in CMH7 is **β-adrenergic signaling × the Ser23/Ser24 PKA phosphorylation site**. cTnI Ser23/Ser24 phosphorylation by PKA is the molecular substrate of the β-adrenergic **lusitropic** (relaxation-enhancing) response: phosphorylation reduces myofilament Ca²⁺ sensitivity, accelerating relaxation during exercise/catecholamine surge. Variants in or near the RRRSS consensus motif (notably **p.Arg21Cys**) abolish this phosphorylation, so the carrier heart cannot mount the normal adrenergic relaxation response. The consequence is that **catecholaminergic stress — exercise, emotion, illness — becomes selectively arrhythmogenic and diastolically decompensating in these carriers**. Wang et al. showed the mouse counterpart directly:

> **[verbatim]** "the R21C mutation abolished the in vivo phosphorylation of Ser(23)/Ser(24) in the mutant cTnI" (Wang et al., *J Biol Chem* 2012; PMID:22086914; DOI:10.1074/jbc.M111.294306)

and reported that isolated myocytes from older R21C mice show **significant delays in Ca²⁺ decay and sarcomere relaxation only in the presence of isoproterenol** — an explicitly stress-conditional phenotype **[paraphrase — verify exact wording]**.

A second G×E consideration: **afterload (hypertension) × sarcomere Ca²⁺ sensitization** compounds the energetic mismatch (§6.4).

---

## 3. Phenotypes

### 3.1 HPO Annotations Curated to OMIM:613690

Retrieved from the HPO annotation API (`ontology.jax.org/api/network/annotation/OMIM:613690`). All HP IDs below verified with OAK ✅.

| HP ID | Term | Frequency (as annotated) | Source |
|---|---|---|---|
| **HP:0001639** ✅ | Hypertrophic cardiomyopathy | 2/2 | PMID:11815426 |
| **HP:0031992** ✅ | Apical hypertrophic cardiomyopathy | 3/6 | PMID:9241277 |
| **HP:0001716** ✅ | Wolff-Parkinson-White syndrome | 3/6 | PMID:9241277 |
| **HP:0001714** ✅ | Ventricular hypertrophy | (unspecified) | OMIM:613690 |
| **HP:0005110** ✅ | Atrial fibrillation | Occasional | OMIM:613690 |
| **HP:0003581** ✅ | Adult onset | 6/6 | PMID:11815426 |
| **HP:0000006** | Autosomal dominant inheritance | — | PMID:9241277 |

**Important caveat on the HPO frequency denominators:** these are *tiny* (2/2, 3/6, 6/6) and derive from two specific papers. PMID:11815426 is **Niimura et al., *Circulation* 2002, "Sarcomere protein gene mutations in hypertrophic cardiomyopathy of the elderly"** — a late-onset cohort (symptoms at 59.3 ± 12.3 y, diagnosis at 62.8 ± 10.8 y). The "Adult onset 6/6" annotation therefore reflects an **ascertainment-biased elderly-onset series**, not the natural onset distribution of `TNNI3`-HCM, which includes pediatric and adolescent presentations (see §3.3, §8.1). Do **not** propagate "adult onset, 6/6" as a general CMH7 frequency claim.

### 3.2 Additional Phenotypes Documented in the CMH7 Literature (HPO Suggestions)

These are well-documented for `TNNI3`-HCM in the primary literature but are not in the OMIM:613690 HPO annotation set. All HP IDs verified with OAK ✅.

**Structural / cardiac morphology**
| HP ID | Term | Comment |
|---|---|---|
| **HP:0001670** ✅ | Asymmetric septal hypertrophy | Classic HCM morphology |
| **HP:0005144** ✅ | Ventricular septal hypertrophy | |
| **HP:0031333** ✅ | Myocardial sarcomeric disarray | Histopathological hallmark; documented on autopsy in p.Arg21Cys carriers **without** gross LVH |
| **HP:0031318** ✅ | Myofiber disarray | Broader parent |
| **HP:0001685** ✅ | Myocardial fibrosis | Progressive; LGE on CMR |
| **HP:0032092** ✅ | Left ventricular outflow tract obstruction | **Less common in thin-filament HCM** (19% vs 34% thick-filament, Coppini 2014) |
| **HP:0001723** ✅ | Restrictive cardiomyopathy | Allelic/overlap phenotype (§3.4) |

**Functional**
| HP ID | Term | Comment |
|---|---|---|
| **HP:0025168** ✅ | Left ventricular diastolic dysfunction | **The core functional lesion of CMH7** |
| **HP:0001635** ✅ | Congestive heart failure | Thin-filament HCM progresses to advanced HF more often |

**Arrhythmic**
| HP ID | Term | Comment |
|---|---|---|
| **HP:0011675** ✅ | Arrhythmia | |
| **HP:0004308** ✅ | Ventricular arrhythmia | |
| **HP:0004756** ✅ | Ventricular tachycardia | NSVT more common in pediatric thin-filament HCM |
| **HP:0001645** ✅ | Sudden cardiac death | 53% of affected p.Arg21Cys carriers |
| **HP:0001695** ✅ | Cardiac arrest | |
| **HP:0005110** ✅ | Atrial fibrillation | |
| **HP:0001716** ✅ | Wolff-Parkinson-White syndrome | Specifically associated with the **p.Gly203Ser** variant (all 3 carriers in Kimura's series) |

**Symptoms**
| HP ID | Term |
|---|---|
| **HP:0002094** ✅ | Dyspnea |
| **HP:0001279** ✅ | Syncope |
| **HP:0100749** ✅ | Chest pain |
| **HP:0001962** ✅ | Palpitations |

OMIM's clinical synopsis for CMH7 describes ventricular hypertrophy that is "usually asymmetric and often involves the interventricular septum," with "dyspnea, syncope, collapse, palpitations, and chest pain; symptoms can be readily provoked by exercise" **[paraphrase from OMIM summary — OMIM is not a PMID-citable evidence source in dismech; find a primary reference for each of these]**.

### 3.3 Phenotype Characteristics

**Age of onset — genuinely bimodal/variable.**
- **Pediatric/adolescent:** Documented and clinically important. Fahed 2020's Lebanese founder cohort was ascertained specifically for pediatric-onset disease; median age at SCD was **22.5 years**. A 2024 case report describes a **14-year-old** girl with de novo `TNNI3` c.583A>T (p.Ile195Phe) presenting with nonobstructive HCM and cardiopulmonary arrest from ventricular fibrillation (PMID:38548731). Norrish et al. (*J Med Genet* 2024;61(5):420-2; PMID:38296631) report a childhood-onset thin-filament HCM cohort.
- **Adult (typical):** Second–fourth decade, as for HCM generally.
- **Elderly-onset:** `TNNI3` is over-represented among **late-onset** HCM. Niimura et al. found cTnI missense variants among 8 sarcomere variants in 31 patients diagnosed at 62.8 ± 10.8 y:
  > **[verbatim]** "Whereas defects in beta-cardiac myosin heavy chain, cardiac troponin T, and alpha-tropomyosin account for > 45% of familial hypertrophic cardiomyopathy, none were found here. Rather, mutations in cardiac myosin binding protein-C, troponin I, and alpha-cardiac myosin heavy chain caused elderly-onset hypertrophic cardiomyopathy." (PMID:11815426)

**Severity — highly variable, both inter- and intrafamilial.** OMIM notes disease expression "ranging from benign forms to malignant forms with high risk of cardiac failure and sudden cardiac death" **[paraphrase]**. Twin siblings homozygous for the *same* `TNNI3` variant have been reported with **restrictive** and **hypertrophic** phenotypes respectively **[paraphrase — locate and verify the primary report]**.

**Progression — progressive.** Documented progression to myocardial fibrosis, LV remodeling, and advanced heart failure. Coppini 2014 found thin-filament HCM (which includes `TNNI3`) had **more frequent progression to NYHA III-IV / advanced HF (15% vs 5%)** and **more systolic dysfunction or restrictive filling (20% vs 9%)** than thick-filament HCM **[paraphrase — the JACC abstract numbers must be re-verified verbatim]**.

**Frequency among affected individuals.** Aside from the small HPO denominators above, the most robustly quantified phenotype frequency in a `TNNI3` cohort is from Fahed 2020's p.Arg21Cys founder families (n=57 affected) **[all paraphrase — re-verify]**:
- SCD: 30/57 (**53%**), median age 22.5 y
- SCD as the *first* presentation: 25/30 (**83.3%**)
- LVH on echocardiography among carriers: 19/30 (**63.3%**)
- **No LVH** on echocardiography among carriers who nonetheless had events: 9/30 (**30%**)

### 3.4 The `TNNI3` Allelic Phenotype Spectrum (critical for entry scoping)

`TNNI3` is unusual among sarcomere genes for producing **four** distinct cardiomyopathy phenotypes, which UniProt's variant table catalogues explicitly:

| Phenotype | OMIM | Representative UniProt-annotated variants |
|---|---|---|
| **CMH7** — hypertrophic | #613690 | R141Q, R145G, A157V, R162P/Q, S166F, K177del, R186Q, D190H, D196N, R204H, K206Q; P82S (risk allele) |
| **RCM1** — restrictive | #115210 | L144Q, R145W, A171T, K178E, D190H, R192H |
| **CMD1FF / CMD2A** — dilated | #613286 / #611880 | A2V, K36Q, A116G, N185K |

Note **R145** and **D190** appear in *both* the HCM and RCM columns — the same residue (and in D190H's case the same substitution) can produce either phenotype. This is why `Restrictive cardiomyopathy` (HP:0001723) belongs in the CMH7 phenotype list as an overlap/spectrum finding, and why Mogensen's landmark paper is required reading:

> **[verbatim]** "We recognized a large family in which individuals were affected by either idiopathic RCM or hypertrophic cardiomyopathy (HCM). Linkage analysis to selected sarcomeric contractile protein genes identified cardiac troponin I (TNNI3) as the likely disease gene. Subsequent mutation analysis revealed a novel missense mutation, which cosegregated with the disease in the family (lod score: 4.8). To determine if idiopathic RCM is part of the clinical expression of TNNI3 mutations, genetic investigations of the gene were performed in an additional nine unrelated RCM patients with restrictive filling patterns, bi-atrial dilatation, normal systolic function, and normal wall thickness. TNNI3 mutations were identified in six of these nine RCM patients. Two of the mutations identified in young individuals were de novo mutations. All mutations appeared in conserved and functionally important domains of the gene." (Mogensen et al., *J Clin Invest* 2003;111(2):209-16; **PMID:12531876**; DOI:10.1172/JCI16336)

**Curation guidance:** keep CMH7 (MONDO:0013369) distinct from `TNNI3`-related RCM (RCM1, MONDO term for OMIM:115210) and `TNNI3`-related DCM, but cross-reference them and document the shared mechanism. This is a natural candidate for a **Grouping** (`grouping_basis: SHARED_GENE_FAMILY` + `SHARED_MECHANISM`) over the `TNNI3` allelic series.

### 3.5 Quality-of-Life Impact

No CMH7-specific QoL literature exists. HCM-general instruments and findings:
- **KCCQ-CSS** (Kansas City Cardiomyopathy Questionnaire – Clinical Summary Score) and **HCMSQ-SoB** (HCM Symptom Questionnaire, Shortness-of-Breath subscore) are the validated, regulatory-accepted HCM PROs. EXPLORER-HCM showed mavacamten improved KCCQ-CSS by **+9.1 points (95% CI 5.5 to 12.7)** and HCMSQ-SoB by **−1.8 (−2.4 to −1.2), p<0.0001** **[verbatim from abstract]**.
- Per-phenotype QoL drivers in `TNNI3`-HCM specifically: **exertional dyspnea and diastolic heart failure** (the dominant symptomatic burden given the thin-filament restrictive physiology), **ICD-related anxiety and shock burden**, **exercise restriction**, and **family/reproductive anxiety** given the 50% transmission risk and the documented pattern of SCD as first presentation.

---

## 4. Genetic / Molecular Information

### 4.1 Causal Gene

**`TNNI3`** — troponin I3, cardiac type.
- HGNC:11947 · NCBI Gene 7137 · Ensembl ENSG00000129991 · UniProt **P19429**
- Cytogenetic location **19q13.42**
- Reference transcript for HGVS: **NM_000363.5** (protein NP_000354.4)
- 8 exons; protein 210 aa, 24,008 Da
- OMIM gene entry ***191044**
- Aliases (per NCBI Gene): `cTnI`, `CMH7`, `RCM1`, `CMD1FF`, `CMD2A`

**Protein architecture (UniProt P19429, verified):**
| Region | Residues | Function |
|---|---|---|
| **Cardiac-specific N-terminal extension** | 1–43 (disordered) | Unique to the cardiac isoform; the β-adrenergic regulatory module |
| **PKA phosphorylation sites** | **Ser23, Ser24** | PKA/PKD1-mediated phosphorylation **reduces Ca²⁺ sensitivity** (lusitropy) |
| **PKC phosphorylation sites** | Ser42, Ser44 | PKC/PRKCE-dependent |
| **TnC-binding region** | 32–79 | |
| **TnI–TnT interaction** | ~80, ~97 | IT-arm coiled coil |
| **Inhibitory region + actin/TnC-binding ("switch") region** | ~129–149 | The Ca²⁺-dependent actin/TnC switch; **the HCM/RCM mutation hotspot** |
| **C-terminal mobile domain** | ~150–210 | Second actin-binding site; modulates the inhibitory region |
| Additional kinase sites | Thr31, Thr51, Thr129, Thr143 (STK4/MST1); Ser5/6, Tyr26, Ser77, Thr78, Ser166, Thr181, Ser199 | |

**Function (UniProt):** **[verbatim]** *"Inhibitory subunit of troponin, the thin filament regulatory complex which confers calcium-sensitivity to striated muscle actomyosin ATPase activity."*

**Subcellular localization:** cardiac myofibril; sarcomere; **troponin complex** (GO:0005861 ✅; cardiac troponin complex **GO:1990584** ✅).

### 4.2 Variant Spectrum

**Positional clustering.** From the pediatric case report (PMID:38548731):
> **[verbatim]** "Approximately 80% of reported pathological variants of TNNI3 are located in exons 7 and 8, which encode the domains that interact with myocardial actin and cardiac troponin C, which are sarcomere components"

This maps precisely onto the inhibitory/switch region and C-terminal mobile domain (residues ~130–210).

**CMH7 variants annotated in UniProt P19429** (position → substitution, dbSNP):

| Protein change | dbSNP | Phenotype per UniProt |
|---|---|---|
| p.Arg21Cys | rs104894723 (verify) | CMH7 — the only N-terminal-extension HCM variant |
| p.Pro82Ser | rs77615401 | **CMH7 risk allele** |
| p.Arg141Gln | rs397516347 | CMH7 |
| **p.Arg145Gly** | rs104894724 | **CMH7** (Kimura's linked variant) |
| p.Arg145Trp | rs104894724 | **RCM1** (same residue, different substitution) |
| p.Leu144Gln | rs121917760 | RCM1 |
| p.Ala157Val | rs397516353 | CMH7 |
| p.Arg162Pro / p.Arg162Gln | rs397516354 | CMH7 |
| p.Ser166Phe | rs727504242 | CMH7 |
| p.Ala171Thr | rs121917761 | RCM1 |
| p.Lys177del | — | CMH7 (in-frame deletion) |
| p.Lys178Glu | rs104894730 | RCM1 |
| p.Arg186Gln | rs397516357 | CMH7 |
| p.Asp190His | — | **CMH7 *and* RCM1** |
| p.Arg192His | rs104894729 | RCM1 |
| p.Asp196Asn | rs104894727 | CMH7 |
| p.Arg204His | rs727504275 | CMH7 |
| **p.Lys206Gln** | rs104894725 | **CMH7** (Kimura's de novo variant) |

Additional literature-reported CMH7 variants not in the above extract: **p.Gly203Ser** (associated with WPW in all 3 carriers, Kimura 1997), **p.Ile195Phe** (`c.583A>T`, de novo, pediatric VF; PMID:38548731), **p.Arg79Cys** (`c.235C>T`, low-penetrance risk allele enriched in Chinese populations; PMID:32815737), **p.Lys183del** (Japanese apical HCM — verify primary source), **p.Arg170Trp/Gly** (infantile RCM).

**Variant type / class:** overwhelmingly **missense**, with occasional **in-frame single-codon deletions** (K177del, K183del, R170 region). Splice-site and frameshift/nonsense `TNNI3` variants are **not** an established HCM mechanism; biallelic truncating variants cause lethal infantile DCM instead (see PMC11196996 — homozygous `TNNI3` frameshift in a consanguineous family with lethal infantile DCM; verify PMID).

**Variant classification (ACMG/AMP).** ClinGen has a `TNNI3`-specific variant curation specification: **CSpec GN098** (`cspec.genome.network/cspec/ui/svi/doc/GN098`), developed under the Hypertrophic Cardiomyopathy / Cardiomyopathy VCEP. Curators should apply gene-specific PM1 (hotspot = exons 7–8 / inhibitory-switch region), calibrated PS4/PM2 population thresholds, and functional-assay PS3 criteria per that spec rather than generic ACMG rules.

**Allele frequency.** Pathogenic `TNNI3` variants are individually ultra-rare (typically absent from gnomAD or at AF < 1×10⁻⁵). Exceptions that matter:
- **p.Arg79Cys** — enriched in East/Southeast Asian populations, HCM disease AF = 0.018 (PMID:32815737); present in gnomAD East Asian controls at appreciable frequency → **PM2 does not apply**, and conflicting ClinVar annotations abound.
- **rs397516354** (p.Arg162Gln/Pro) — reported gnomAD frequency ~0.006% **[paraphrase — verify against gnomAD directly]**.
- **p.Arg21Cys** — founder allele in South Lebanon (see §9).

**Somatic vs germline:** **germline** exclusively. `TNNI3` is not a somatic cancer gene; COSMIC/TCGA are not relevant. **De novo** germline variants are well documented (Kimura's K206Q; two of Mogensen's RCM variants; the p.Ile195Phe pediatric case).

**Functional consequence class:** **Gain-of-function / dominant-negative (poison peptide).** The mutant cTnI incorporates into the thin filament alongside wild-type protein and actively corrupts regulation; there is no evidence for a haploinsufficiency mechanism. Wang 2012 measured **~25% mutant cTnI incorporation in heterozygous knock-in mouse hearts** **[paraphrase]** — a small mutant fraction sufficient to produce a phenotype, consistent with dominant negativity. ClinGen's dosage-sensitivity curation for `TNNI3` (HGNC:11947) should be consulted before asserting any haploinsufficiency claim.

### 4.3 Modifier Genes

No `TNNI3`-specific modifier gene is established. General HCM modifiers that plausibly apply:
- **Second sarcomere variants** (compound/double heterozygosity) → earlier onset, worse outcome.
- **HCM polygenic risk score** background.
- Candidate (weak evidence) modifiers reported in HCM broadly: ACE I/D, endothelin-1, angiotensinogen polymorphisms — **historically reported, poorly replicated; do not curate as established.**
- OMIM's separate "CMH7, MODIFIER OF" concept implies at least one curated modifier allele in `TNNI3` itself; verify against the OMIM entry before curating.

### 4.4 Epigenetic Information

**No CMH7-specific epigenetic data exist.** Established for HCM/hypertrophied myocardium generally (and therefore downstream-consequence rather than cause):
- Fetal gene program reactivation (`NPPA`, `NPPB`, `MYH7`/`MYH6` isoform switch) — Wang 2012 explicitly reports that R21C knock-in mice "activated the fetal gene program" **[paraphrase]**.
- Differential DNA methylation and histone acetylation signatures in HCM myectomy tissue; HDAC inhibition has been explored preclinically as an antihypertrophic strategy.
- Search resources: GEO (myectomy tissue datasets), ENCODE, Roadmap Epigenomics heart samples. **No `TNNI3`-genotype-stratified epigenomic dataset is known.**

### 4.5 Chromosomal Abnormalities

**Not applicable.** CMH7 is caused by point/in-frame variants. Chromosomal microarray, karyotype, and FISH have **no diagnostic role** for CMH7 and should be flagged as not indicated. Large deletions/duplications of `TNNI3` are not an established HCM mechanism (consistent with the non-haploinsufficiency mechanism), though most clinical panels include del/dup analysis (31 of 47 GTR-listed `TNNI3` tests offer it).

---

## 5. Environmental Information

- **Environmental toxins / radiation / occupational exposure:** No established causal or modifying role specific to CMH7. CTD/TOXNET yield no `TNNI3`-HCM–specific exposure associations.
- **Lifestyle factors:** As in §2.3 — high-intensity burst exercise (arrhythmic trigger), obesity and hypertension (phenotype amplifiers), dehydration and alcohol (LVOT gradient provocation in the obstructive subset). Anabolic-androgenic steroid use is a recognized HCM-phenocopy/aggravating exposure and must be excluded in differential diagnosis.
- **Infectious agents:** **Not applicable.** No pathogen causes or triggers CMH7. (Concurrent myocarditis is a differential-diagnosis consideration for acute decompensation, not an etiology.)

---

## 6. Mechanism / Pathophysiology

### 6.1 The Causal Chain (upstream → downstream)

This is the recommended pathograph for a dismech `pathophysiology:` block. Nodes are annotated with `biological_scale` per the dismech enum.

**Node 1 — `TNNI3` missense variant in cardiac troponin I** · `biological_scale: MOLECULAR`
Heterozygous missense (or in-frame indel) variant, predominantly in exons 7–8 encoding the inhibitory/switch and C-terminal mobile domains. Mutant cTnI is expressed and **incorporates into the sarcomeric thin filament** alongside wild-type protein (~25% mutant fraction in heterozygous knock-in mice).
- Gene: `hgnc:11947` (TNNI3)
- GO CC: **GO:1990584** ✅ cardiac Troponin complex; **GO:0030017** ✅ sarcomere
- ↓ *downstream*

**Node 2 — Impaired Ca²⁺-dependent thin-filament inhibition** · `biological_scale: MOLECULAR`
Two distinguishable molecular lesions, depending on variant location:
- **(a) Switch/inhibitory-region variants (R145G, R162Q, D190H, K206Q, I195F…)** — the mutant inhibitory region fails to hold the tropomyosin–actin filament in the blocked state at low Ca²⁺, and the actin/TnC switch is biased toward the activated conformation. Wen et al. demonstrated this directly:
  > **[verbatim]** "The addition of 3 mm 2,3-butanedione monoxime at pCa 9.0 showed that there was approximately 2-4% of force generating cross-bridges attached in Tg-R145G fibers compared with less than 1.0% in Tg-WT fibers, suggesting that the mutation impairs the ability of the cardiac troponin complex to fully inhibit cross-bridge attachment under relaxing conditions." (PMID:18430738)
- **(b) N-terminal extension variant (R21C)** — destroys the PKA phosphorylation consensus, locking the filament in the *unphosphorylated*, high-Ca²⁺-sensitivity state and **abolishing β-adrenergic lusitropy**.
- GO BP: **GO:0032971** ✅ regulation of muscle filament sliding; **GO:1904114** ✅ positive regulation of muscle filament sliding; **GO:0055117** ✅ regulation of cardiac muscle contraction
- ↓

**Node 3 — Increased myofilament Ca²⁺ sensitivity** · `biological_scale: MOLECULAR`
The unifying biophysical signature of `TNNI3` cardiomyopathy variants, measured as a leftward shift of the force–pCa and ATPase–pCa relationships in skinned fibers.
> **[verbatim]** "Simultaneous measurements of ATPase activity and force in skinned papillary fibers from hcTnI R145G transgenic mice (Tg-R145G) versus hcTnI wild type transgenic mice (Tg-WT) showed a significant decrease in the maximal Ca(2+)-activated force without changes in the maximal ATPase activity and an increase in the Ca(2+) sensitivity of both ATPase and force development." (PMID:18430738)

Note the mechanistically important dissociation: **Ca²⁺ sensitivity ↑ but maximal force ↓.** `TNNI3`-HCM is therefore *not* simply "hypercontractility" in the `MYH7` R403Q sense — it is a **regulatory/relaxation** defect. This is the mechanistic root of the thin-filament clinical phenotype (mild hypertrophy, prominent diastolic/restrictive physiology).
- GO BP: **GO:0010882** ✅ regulation of cardiac muscle contraction by calcium ion signaling
- ↓ (branches to Nodes 4a, 4b, 4c)

**Node 4a — Impaired diastolic relaxation (incomplete cross-bridge detachment)** · `biological_scale: CELLULAR`
Residual force-generating cross-bridges persist at diastolic [Ca²⁺]; force and Ca²⁺ transients are prolonged.
> **[verbatim]** "Prolonged force and intracellular [Ca(2+)] transients in electrically stimulated intact papillary muscles were observed in Tg-R145G compared with Tg-WT." (PMID:18430738)
- Cell type: **CL:2000046** ✅ ventricular cardiac muscle cell (parent **CL:0000746** ✅ cardiac muscle cell)
- Phenotype: **HP:0025168** ✅ Left ventricular diastolic dysfunction
- ↓

**Node 4b — Myocardial energetic mismatch (increased tension cost)** · `biological_scale: CELLULAR`
Ca²⁺ sensitization plus reduced force-per-cross-bridge means more ATP consumed per unit of force generated.
> **[verbatim]** "Energy cost calculations demonstrated higher energy consumption in Tg-R145G fibers compared with Tg-WT fibers." (PMID:18430738)

This is the **mechano-energetic uncoupling** paradigm central to modern HCM pathophysiology: excess ATP demand exceeds mitochondrial supply, depleting the phosphocreatine/ATP ratio, driving oxidative stress, and activating hypertrophic (ERK) and fibrotic signaling **[paraphrase from recent reviews — verify a specific PMID before curating]**.
- GO BP: **GO:0006936** muscle contraction (verify); ATP metabolic process **GO:0046034** (verify)
- ↓

**Node 4c — Ca²⁺-handling remodeling and arrhythmogenic substrate** · `biological_scale: CELLULAR`
High myofilament Ca²⁺ buffering alters cytosolic Ca²⁺ transient shape and decay; the resulting Ca²⁺ mishandling, combined with disarray-generated conduction heterogeneity, creates the substrate for triggered activity and reentry. This is why `TNNI3` carriers can die suddenly **before** developing hypertrophy.
- Phenotypes: **HP:0004308** ✅ Ventricular arrhythmia; **HP:0001645** ✅ Sudden cardiac death
- ↓

**Node 5 — Compensatory hypertrophic and fibrotic remodeling** · `biological_scale: TISSUE`
Energetic stress and altered mechanotransduction activate the hypertrophic program (fetal gene reactivation) in cardiomyocytes and a fibrogenic program in cardiac fibroblasts.
> **[verbatim]** "These results suggest that the phenotype of hypertrophic cardiomyopathy is most likely caused by the compensatory mechanisms in the cardiovascular system that are activated by 1) higher energy cost in the heart resulting from a significant decrease in average force per cross-bridge, 2) slowed relaxation (diastolic dysfunction) caused by prolonged [Ca(2+)] and force transients, and 3) an inability of the cardiac TnI to completely inhibit activation in the absence of Ca(2+) in Tg-R145G mice." (PMID:18430738)

Wang 2012 confirmed in the knock-in (rather than transgenic-overexpression) context: R21C⁺/⁻ and R21C⁺/⁺ mice "activated the fetal gene program and developed a remarkable degree of cardiac hypertrophy and fibrosis" **[paraphrase]**.
- Cell types: **CL:2000046** ✅ ventricular cardiac muscle cell; **CL:0002548** ✅ fibroblast of cardiac tissue
- GO BP: **GO:0003300** ✅ cardiac muscle hypertrophy; **GO:0014898** ✅ cardiac muscle hypertrophy in response to stress; **GO:0010613** ✅ positive regulation of cardiac muscle hypertrophy
- Phenotypes: **HP:0001639** ✅ HCM; **HP:0001670** ✅ Asymmetric septal hypertrophy; **HP:0001685** ✅ Myocardial fibrosis; **HP:0031333** ✅ Myocardial sarcomeric disarray
- ↓

**Node 6 — Clinical disease: diastolic heart failure, arrhythmia, sudden death** · `biological_scale: ORGANISM`
Restrictive filling physiology → elevated filling pressures → exertional dyspnea → progression to advanced heart failure; independently, arrhythmic death.
- Phenotypes: **HP:0001635** ✅ Congestive heart failure; **HP:0002094** ✅ Dyspnea; **HP:0001279** ✅ Syncope; **HP:0001645** ✅ Sudden cardiac death; **HP:0001723** ✅ Restrictive cardiomyopathy (in the RCM-overlap arm)

### 6.2 Molecular Pathways

- **Ca²⁺-troponin–tropomyosin thin-filament regulation** (the primary lesion) — Reactome R-HSA-390522 "Striated Muscle Contraction"; KEGG hsa04260 "Cardiac muscle contraction"; KEGG **hsa05410 "Hypertrophic cardiomyopathy (HCM)"** — the most directly relevant curated pathway map.
- **β-adrenergic / PKA signaling** (Ser23/Ser24 lusitropic axis) — KEGG hsa04261 "Adrenergic signaling in cardiomyocytes".
- **Downstream hypertrophic signaling:** ERK1/2-MAPK, calcineurin–NFAT, and AMPK (energy-sensing) are implicated in the compensatory arm; PI3K-AKT-mTOR in growth. **These are inferred from HCM-general literature, not `TNNI3`-specific data — curate with appropriate hedging.**
- **TGF-β–driven interstitial fibrosis** in the remodeling arm — a plausible `conforms_to` target for the dismech `fibrotic_response` module.

### 6.3 Cellular Processes

Excitation–contraction coupling; excitation–contraction *uncoupling* (the term used by Wang and colleagues for the chronic PKA-ablated state); cardiomyocyte hypertrophy; cardiac fibroblast activation and myofibroblast transition; cardiomyocyte oxidative stress; mitochondrial dysfunction. Cardiomyocyte apoptosis is a late/end-stage contributor.

### 6.4 Protein Dysfunction

The dysfunction is **conformational/regulatory, not degradative**. Mutant cTnI folds, is stably expressed, and integrates into the troponin complex — this is precisely what makes it a dominant-negative poison peptide. There is **no misfolding, no aggregation, no proteasomal loss-of-protein mechanism**. Three distinguishable structural failure modes:
1. **Inhibitory/switch-region variants** — the mutant fails to anchor the inhibitory region on actin at low Ca²⁺.
2. **C-terminal mobile-domain variants** — loss of the second actin-binding site that normally modulates the inhibitory region; also implicated in thin-filament structural integrity (the infantile RCM cTnI-R170G/W work shows impaired interplay of sarcomeric proteins and loss of thin-filament integrity).
3. **N-terminal extension variant (R21C)** — loss of the PKA phospho-switch; a *regulatory-input* failure rather than a *filament-mechanics* failure.

Structural resources: **PDB 1J1E** (human cardiac troponin core complex in the Ca²⁺-saturated state) is the canonical structure for mapping variants; AlphaFold DB entry for P19429 covers the disordered N-terminal extension not resolved crystallographically.

### 6.5 Metabolic Changes

Increased tension cost / ATP consumption per unit force (directly measured, PMID:18430738) → reduced myocardial phosphocreatine/ATP ratio; substrate shift from fatty-acid oxidation toward glucose utilization; creatine kinase system dysfunction. These are documented for HCM broadly (including in ³¹P-MRS studies of sarcomere-variant carriers) and mechanistically predicted for CMH7, but **no `TNNI3`-genotype-specific human metabolomic study is known.** Resources: HMDB, Metabolomics Workbench.

### 6.6 Immune System Involvement

**Minimal and non-primary.** CMH7 is not autoimmune, not immunodeficient, and not driven by chronic inflammation. Low-grade macrophage infiltration accompanies interstitial fibrosis in remodeling myocardium, as in other cardiomyopathies. **Do not curate immune involvement as a mechanism node.**

### 6.7 Tissue Damage Mechanisms

- **Myocyte disarray** — the histopathological hallmark; loss of parallel myofiber alignment with whorled/interlacing architecture. Critically, disarray was found on autopsy in `TNNI3` p.Arg21Cys carriers **who had normal echocardiograms**, establishing that the tissue lesion precedes gross hypertrophy **[paraphrase]**.
- **Interstitial and replacement fibrosis** — progressive; the CMR late-gadolinium-enhancement substrate; the arrhythmic substrate.
- **Microvascular ischemia** — small-vessel dysplasia with medial hypertrophy and reduced capillary density relative to myocyte mass → supply-demand mismatch, compounding the energetic lesion of Node 4b.
- **Oxidative stress** — downstream of mitochondrial overwork.

### 6.8 Biochemical Abnormalities

The defect is in a **contractile regulatory protein**, not an enzyme, receptor, or ion channel. There is no enzyme deficiency to assay. The measurable biochemical abnormalities are:
- **Reduced/abolished PKA phosphorylation of cTnI Ser23/Ser24** (R21C and, secondarily, in end-stage failing myocardium generally).
- **Leftward-shifted force–pCa relationship** (ΔpCa₅₀) in skinned myocardium — the standard functional assay and the basis for ACMG PS3 in the `TNNI3` CSpec.
- **Increased tension cost** (ATPase/force ratio).
- **Circulating cardiac troponin I elevation** — clinically, chronically mildly elevated hs-cTnI is common in HCM and prognostically adverse. LOINC: **89579-7** (Troponin I, cardiac, high sensitivity, serum/plasma) and **10839-9** (Troponin I, cardiac, serum/plasma) — *verify LOINC codes before curating a `reference_ranges` block*. Note the pleasing but non-causal irony: the mutated gene product is itself the standard clinical biomarker of myocardial injury.
- **NT-proBNP / BNP** elevation tracks filling pressures and prognosis. LOINC 33762-6 (NT-proBNP) — verify.

### 6.9 Epigenetic Changes

See §4.4. Fetal gene program reactivation is the best-documented transcriptional-reprogramming event in the `TNNI3` knock-in model.

### 6.10 Molecular Profiling

| Modality | Status for CMH7 | Notes / resources |
|---|---|---|
| **Transcriptomics** | HCM myectomy bulk and single-nucleus RNA-seq datasets exist in GEO; **not `TNNI3`-genotype-stratified**. GTEx provides `TNNI3` baseline expression (heart LV/AA-restricted). | GEO, GTEx, Human Cell Atlas |
| **Proteomics** | Sarcomere phospho-proteomics of human HCM myectomy tissue documents cTnI hypophosphorylation in disease. Wang 2012 used top-down MS to quantify cTnI phospho-status in R21C mice. | PRIDE, ProteomeXchange, Human Protein Atlas |
| **Metabolomics** | No CMH7-specific study. HCM-general FFA-metabolism abnormalities reported. | MetaboLights, Metabolomics Workbench |
| **Lipidomics** | **No data.** | LIPID MAPS |
| **Genomic structural features** | `TNNI3` is a small, compact, highly constrained gene; no recurrent SV. | Ensembl, dbVar, DGV |

### 6.11 Advanced Technologies

- **Single-cell / single-nucleus:** snRNA-seq of HCM myectomy tissue has resolved cardiomyocyte, fibroblast, and immune compartment shifts. Not yet `TNNI3`-stratified.
- **Spatial transcriptomics:** applied to human HCM septal tissue to map disarray/fibrosis regions transcriptionally. Not `TNNI3`-specific.
- **iPSC-CM and engineered heart tissue (EHT) — this is where CMH7-adjacent single-variant work is strongest.** Hasegawa et al. (*Dev Growth Differ* 2024; PMID:38193576; DOI:10.1111/dgd.12909) generated iPSCs from a patient with early-childhood-onset RCM carrying `TNNI3` **R170W**, and compared them to an isogenic CRISPR-corrected line. R170W iPSC-CMs showed **altered Ca²⁺ kinetics including prolonged tau**, and R170W EHTs showed an **increased ratio of relaxation force to contractile force**; both were reversed in the isogenic control, and **overexpression of wild-type `TNNI3` rescued impaired relaxation** **[all paraphrase — verify against the abstract]**. This is a direct in vitro demonstration of (i) mechanism, (ii) isogenic causality, and (iii) a gene-therapy rationale. A companion study (*J Am Heart Assoc* 2024, "Impaired Relaxation in Induced Pluripotent Stem Cell-Derived Cardiomyocytes with Pathogenic TNNI3 Mutation of Pediatric Restrictive Cardiomyopathy") reports the same lesion — verify PMID.
- **Multiparametric iPSC-CM phenotyping:** a 2025 preprint ("Multiparametric Assessment of TNNI3 Variant Phenotypes in Human iPSC-Cardiomyocytes Correlates with Disease Severity in Patients", bioRxiv) reports variant-level in vitro phenotype correlating with clinical severity — **preprint, not peer-reviewed; do not curate as evidence yet.**
- **Functional genomics screens (CRISPR/RNAi):** No `TNNI3`-HCM-specific screen. DepMap is not informative (non-essential in cancer lines).

---

## 7. Anatomical Structures Affected

### 7.1 Organ Level

**Primary organ:** the **heart** (UBERON:0000948 — *verify*), specifically the **left ventricle**.
- **UBERON:0002084** ✅ heart left ventricle — the primary site of hypertrophy
- **UBERON:0002094** ✅ interventricular septum — the classic maximal-hypertrophy site in asymmetric septal HCM
- **UBERON:0004667** ✅ interventricular septum muscular part
- **UBERON:0002349** ✅ myocardium
- **UBERON:0001083** ✅ myocardium of ventricle
- **Left ventricular apex** — the distinctive site in "Japanese-type" apical HCM, over-represented in `TNNI3` carriers (Kimura found 3/36 = **8.3%** of apical HCM patients carried `TNNI3` variants; HP:0031992 ✅ annotated 3/6 for CMH7)

**Secondary involvement:**
- **Left atrium** (UBERON:0002079 — verify) — dilates secondary to chronic elevated filling pressures; substrate for atrial fibrillation (HP:0005110 ✅). **Bi-atrial dilatation** is a defining feature of the `TNNI3` restrictive-overlap phenotype (Mogensen 2003).
- **Mitral valve / mitral apparatus** — systolic anterior motion (SAM) and secondary mitral regurgitation in the obstructive subset (58% SAM in Niimura's late-onset series).
- **Pulmonary circulation** — post-capillary pulmonary hypertension from chronically elevated left-heart filling pressures.
- **Right ventricle** — involved in advanced/restrictive disease. Note that the R21C knock-in model showed **differential contractile force generation between left and right ventricles** (PMC4415466), an interesting chamber-asymmetry finding.
- **Systemic circulation / brain** — cardioembolic stroke risk from AF.

**Body systems:** **cardiovascular** (primary and, essentially, exclusive). CMH7 is a **non-syndromic, organ-restricted** disorder — there is no skeletal muscle, CNS, renal, or dermatologic involvement, because `TNNI3` expression is cardiac-restricted. This is a useful discriminator from HCM phenocopies (Fabry, Danon, Pompe, amyloidosis, RASopathies), all of which are multisystem.

### 7.2 Tissue and Cell Level

**Tissue:** cardiac muscle tissue (striated, involuntary); cardiac interstitium/connective tissue (fibrosis); intramural coronary microvasculature.

**Cell populations:**
| CL ID | Cell type | Role |
|---|---|---|
| **CL:2000046** ✅ | ventricular cardiac muscle cell | **Primary affected cell** — expresses mutant cTnI; site of Ca²⁺ sensitization, energetic stress, hypertrophy, disarray |
| **CL:0000746** ✅ | cardiac muscle cell | Broader parent |
| **CL:0002548** ✅ | fibroblast of cardiac tissue | Secondary effector — activated to myofibroblast, deposits interstitial/replacement fibrosis |
| CL:0000115 | endothelial cell of vascular tree (verify) | Microvascular dysfunction/rarefaction |
| CL:0000235 | macrophage (verify) | Minor; accompanies fibrotic remodeling |

**Cell type NOT affected:** skeletal muscle cells — `TNNI3` is cardiac-specific (the skeletal paralogs are `TNNI1` slow and `TNNI2` fast). Atrial cardiomyocytes *do* express cTnI, so atrial myopathy is mechanistically expected and clinically observed as the AF substrate.

### 7.3 Subcellular Level

| GO CC | Term | Relevance |
|---|---|---|
| **GO:1990584** ✅ | cardiac Troponin complex | **The direct molecular site of the lesion** |
| **GO:0005861** ✅ | troponin complex | Parent |
| **GO:0030017** ✅ | sarcomere | |
| GO:0030016 | myofibril (verify) | |
| GO:0005865 | striated muscle thin filament (verify) | The specific filament corrupted |
| GO:0005739 | mitochondrion (verify) | Secondary — energetic stress / oxidative damage |
| GO:0016529 | sarcoplasmic reticulum (verify) | Secondary — Ca²⁺-handling remodeling |

### 7.4 Localization and Lateralization

- **Predominantly left-sided (left ventricle),** with a strong predilection for the **basal anterior interventricular septum**; **asymmetric** by definition in the classic morphology (HP:0001670 ✅ Asymmetric septal hypertrophy).
- **Apical variant** — a distinctive `TNNI3`-enriched morphology; hypertrophy confined to the LV apex, producing the classic "ace of spades" LV cavity on ventriculography/CMR and giant negative T waves in precordial leads.
- **Concentric or nonobstructive patterns** are also seen; the pediatric p.Ile195Phe case was **nonobstructive** HCM.
- In the restrictive-overlap arm, hypertrophy may be **absent entirely** with **bi-atrial** (bilateral) dilatation as the dominant morphologic finding.

---

## 8. Temporal Development

### 8.1 Onset

**Typical age:** Genuinely broad and **trimodal in the literature**, which is itself a curation-worthy fact:
1. **Pediatric/adolescent** (first–second decade) — documented in founder cohorts and de novo cases; associated with worse outcomes.
2. **Young to middle adult** (second–fourth decade) — the modal HCM presentation.
3. **Elderly-onset** (sixth–seventh decade) — `TNNI3` is disproportionately represented here (Niimura 2002: symptoms at 59.3 ± 12.3 y, diagnosis at 62.8 ± 10.8 y, **no family history of cardiomyopathy in any of the 31 patients**).

For HPO curation, this means **HP:0003581 (Adult onset) alone is insufficient**; consider also HP:0011462 (Young adult onset), HP:0003621 (Juvenile onset), and HP:0003584 (Late onset) as a spread, with explicit `frequency` omission per the dismech frequency-evidence SOP unless a quantitative source supports each band.

**Onset pattern:** **Insidious and chronic.** Hypertrophy develops gradually, typically becoming echocardiographically detectable during adolescent somatic growth or in mid-to-late adulthood. The **catastrophic exception**: sudden cardiac death as the *first* manifestation — 83.3% of SCD events in the p.Arg21Cys founder cohort were the presenting event **[paraphrase]**.

**Critically: the genotype–phenotype latency is real and dangerous.** Fahed 2020's central finding was that **SCD occurred in carriers with entirely normal echocardiograms**, with myocyte disarray found only at autopsy. Advanced imaging (tissue Doppler, CMR with LGE) detected subclinical disease in genotype-positive/phenotype-negative carriers **[paraphrase]**. This defines a **preclinical stage** with real event risk — a strong argument for `TNNI3` genotype itself as a risk-stratification variable.

### 8.2 Progression

**Disease stages** (adapting the HCM natural-history framework):
1. **Genotype-positive / phenotype-negative (G+/P−)** — normal wall thickness; may show subtle diastolic abnormalities on tissue Doppler, ECG changes, or LGE. **Not risk-free in `TNNI3`.**
2. **Classic hypertrophic phenotype** — LVH ± obstruction, preserved EF, diastolic dysfunction. Most patients remain here lifelong.
3. **Adverse remodeling** — progressive fibrosis, atrial dilation, AF onset, worsening diastolic function, restrictive filling.
4. **End-stage / "burnt-out" HCM (HCM with LV systolic dysfunction)** — wall thinning, cavity dilation, EF < 50%. **Thin-filament genotypes are over-represented here**: Coppini 2014 reported progression to advanced HF in 15% of thin-filament vs 5% of thick-filament patients over 4.5 years mean follow-up **[paraphrase]**.
5. **Restrictive phenotype** — for the `TNNI3` allelic-series arm; may bypass the hypertrophic stage entirely.

**Progression rate:** **Slow and variable** over decades in most patients; **rapid in pediatric-onset and de novo cases** (the p.Ile195Phe girl arrested ~1 year after diagnosis).

**Course pattern:** **Chronic and progressive**, punctuated by **episodic** arrhythmic events. Never relapsing-remitting.

**Duration:** **Lifelong.** No spontaneous resolution.

### 8.3 Patterns

- **Remission:** No spontaneous remission. **Treatment-induced regression** of the LVOT gradient and symptoms occurs with mavacamten, myectomy, or ablation — but these relieve obstruction and symptoms; they are **not** demonstrated to reverse the underlying disarray/fibrosis in `TNNI3`-HCM, and CMH7 is *less* often obstructive than thick-filament HCM, making these interventions less frequently applicable.
- **Critical periods:**
  - **Adolescence** — the window of most rapid hypertrophy development; also the peak age of exertional SCD in HCM. Justifies **1–2-yearly** imaging in at-risk children (2024 AHA/ACC).
  - **The G+/P− window** — theoretically the optimal intervention point for disease modification, but no therapy is proven to prevent phenotype development.
  - **Pre-conception / prenatal** — the window for reproductive genetic counseling and PGT.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**HCM overall:**
- Classic clinically-ascertained prevalence: **~1 in 500 (0.2%; 200 per 100,000)** — the CARDIA-derived figure that dominated for two decades.
- Revised, genotype- and imaging-inclusive estimate: **~1 in 200 (0.5%; 500 per 100,000)** (Semsarian, Ingles, Maron & Maron, *J Am Coll Cardiol* 2015; PMID:25814232) — this figure includes G+/P− individuals at risk of developing disease. Also cited in the 2025 ClinGen reappraisal as "~1 in 500" **[verbatim from that abstract]**, showing both figures remain in circulation; state which you mean.

**CMH7 / `TNNI3`-HCM specifically:**
- `TNNI3` accounts for **~3% of HCM** (Fahed et al., *Circ Genom Precis Med* 2020; PMID:32885985): **[verbatim]** *"Cardiac troponin I (TNNI3) gene mutations account for 3% of hypertrophic cardiomyopathy and carriers have a heterogeneous phenotype, with increased risk of sudden cardiac death (SCD)."*
- Alternative framing: **<5%** of cardiomyopathy patients carry pathogenic `TNNI3` variants (PMID:38548731) **[verbatim]** *"The prevalence of pathological variants of TNNI3 is reportedly less than 5% in patients with cardiomyopathies, with a relatively low penetrance of approximately 50%"*
- Within **sarcomere-positive** HCM specifically, one cohort reported **18/342 = 5.3%** of single-variant Sarc+ patients had `TNNI3` variants (vs MYBPC3 57.3%, MYH7 30.7%) **[paraphrase — locate and verify the primary source]**.

**Derived CMH7 prevalence estimate (for a dismech `Prevalence` record):**
Taking HCM point prevalence at 200 per 100,000 and `TNNI3` at 3% of HCM → **~6 per 100,000 (≈1 in 17,000)**; using the 1-in-200 figure → **~15 per 100,000**. This is a **derived, not directly measured, figure** — curate as:
```
population: Worldwide
measure_type: POINT_PREVALENCE
prevalence_class: BAND_1_9_PER_100000
rate_per_100000: 6.0
notes: >-
  Derived, not directly measured: HCM clinical point prevalence ~1/500
  (200/100,000) × TNNI3 attributable fraction ~3% (PMID:32885985).
```
**Incidence:** No CMH7-specific incidence data. Birth incidence equals variant transmission rate; clinical incidence is diagnosis-driven and highly ascertainment-dependent.

### 9.2 Inheritance Genetics

**Pattern:** **Autosomal dominant** (HP:0000006). Rare biallelic (homozygous/compound heterozygous) cases occur — typically in consanguineous families, typically with a severe infantile RCM or DCM phenotype rather than classic HCM. Recessive `TNNI3` RCM is documented (BMC Med Genet 2019 — verify PMID).

For a dismech `Inheritance` block:
```yaml
inheritance:
- inheritance_term:
    preferred_term: Autosomal dominant inheritance
    term:
      id: HP:0000006
      label: Autosomal dominant inheritance
```

**Penetrance:** **Incomplete and age-dependent.** The most-cited `TNNI3` figure is **~50%** (PMID:38548731, **[verbatim]** *"with a relatively low penetrance of approximately 50%"*). Penetrance is **variant-dependent** and spans nearly the whole range:
- **p.Arg21Cys** — very high effective penetrance for *events*: 53% of affected individuals died suddenly (though note ascertainment bias in a pedigree study).
- **p.Arg79Cys** — explicitly a **low-penetrance risk allele** (PMID:32815737).
- **p.Pro82Ser** — UniProt-annotated "CMH7 risk," not fully penetrant.

**Expressivity:** **Highly variable**, both between and within families. The same variant can produce apical HCM, asymmetric septal HCM, restrictive physiology, or no detectable phenotype. Documented intrafamilial discordance includes homozygous twin siblings with divergent RCM vs HCM phenotypes.

**Genetic anticipation:** **Not applicable** — `TNNI3` is not a repeat-expansion locus. Apparent anticipation in HCM pedigrees is ascertainment bias.

**Germline mosaicism:** Not specifically documented for `TNNI3`. De novo variants are well documented (K206Q, 2 of Mogensen's RCM variants, p.Ile195Phe), so parental gonadal mosaicism is a theoretical recurrence-risk consideration in de novo cases and should be mentioned in counseling (empirical recurrence risk after an apparently de novo variant is conventionally quoted as ~1%).

**Founder effects — well documented for `TNNI3`:**
- **`TNNI3` p.Arg21Cys in South Lebanon.** Fahed et al. sequenced 29 HCM families enriched for pediatric-onset disease, found 5 families with p.Arg21Cys, and established a founder haplotype (**LOD 4.38**; probability of 5 unrelated families by chance **5×10⁻¹⁵**) **[paraphrase]**. Conclusion **[verbatim]**: *"The TNNI3 p.Arg21Cys mutation has a founder effect in South Lebanon and causes malignant hypertrophic cardiomyopathy with early SCD even in the absence of hypertrophy."*
- **`TNNI3` p.Arg79Cys in Chinese/Southeast Asian populations** — a common, population-enriched, low-penetrance allele (disease AF 0.018 in Singaporean HCM; PMID:32815737).
- The **p.Lys183del** variant has been associated with Japanese apical HCM — **verify the primary source before curating**.

**Consanguinity:** Relevant only for the rare biallelic `TNNI3` cardiomyopathies (infantile RCM/DCM), reported in consanguineous families including South African and Middle Eastern series. Not relevant to typical AD CMH7.

**Carrier frequency:** The term does not apply in the recessive sense. The relevant analogue — population frequency of pathogenic `TNNI3` variants — is very low for high-penetrance alleles (individually <1×10⁻⁵ in gnomAD; most absent), with the population-enriched exceptions noted above.

### 9.3 Population Demographics

- **Affected populations:** Worldwide, no overall ethnic predilection for `TNNI3`-HCM. Population-specific enrichments: **South Lebanese** (p.Arg21Cys), **Chinese/Singaporean** (p.Arg79Cys), **Japanese** (apical morphology among `TNNI3` carriers, per Kimura's Japanese cohort). Note a major equity gap: **[verbatim]** *"highlighting the need for greater study of HCM genetics in non-White populations"* (PMID:32815737) — Singaporean HCM patients had significantly fewer confidently interpreted variants (P/LP 18% vs 31% in Whites) and an excess of VUS (24% vs 7%) **[verbatim]**.
- **Geographic distribution:** Global; no endemic pattern. Variant-level geography as above.
- **Sex ratio:** No established sex bias in `TNNI3` variant carriage (Mendelian autosomal). HCM diagnosis overall skews male (~60:40), reflecting ascertainment and hypertrophy magnitude rather than transmission. Fahed 2020 found **no sex difference in SCD** among p.Arg21Cys carriers (46.4% women vs 48.3% men) **[paraphrase]** — worth curating, since it contradicts the general HCM pattern.
- **Age distribution:** Trimodal as in §8.1.

---

## 10. Diagnostics

### 10.1 Clinical Tests

**Imaging (the diagnostic cornerstone):**
| Test | Findings in CMH7 | Notes |
|---|---|---|
| **Transthoracic echocardiography (TTE)** | Maximal LV wall thickness ≥15 mm (unexplained), or ≥13 mm with family history; asymmetric septal or apical distribution; diastolic dysfunction; LA dilation; SAM and LVOT gradient (less common in thin-filament HCM: 19% vs 34%) | **First-line.** LOINC/RadLex terms available |
| **Cardiac MRI with LGE** | Gold standard for wall thickness, apical variants (often missed on TTE), and fibrosis burden. **LGE detects subclinical disease in `TNNI3` G+/P− carriers** | Critical for the apical variant that `TNNI3` favors |
| **Exercise stress echo** | Unmasks provocable LVOT obstruction | |
| **Tissue Doppler imaging** | Detects preclinical diastolic abnormality in G+/P− `TNNI3` carriers (Fahed 2020) | High-yield in this genotype |

**Electrophysiology:**
- **12-lead ECG** — abnormal in >90% of HCM; LVH voltage, repolarization abnormality, pathological Q waves. **Giant negative T waves in precordial leads** are the signature of the apical variant. **Ventricular pre-excitation (delta wave)** should prompt consideration of `TNNI3` p.Gly203Ser (all 3 carriers in Kimura's series had WPW) — as well as the metabolic phenocopies (PRKAG2, Danon, Pompe).
- **Ambulatory ECG (48-h Holter)** — mandatory for NSVT detection; class I for SCD risk stratification. NSVT is more common in pediatric thin-filament HCM (PMID:38296631).
- **Implantable loop recorder** — for unexplained syncope.

**Laboratory / biomarkers:**
- **hs-cTnI** and **NT-proBNP** — prognostic, not diagnostic.
- Phenocopy exclusion panel (essential): **alpha-galactosidase A activity** (males) and **GLA** sequencing (females) for Fabry; **serum/urine free light chains + immunofixation** and **⁹⁹ᵐTc-PYP scintigraphy** for transthyretin amyloidosis; **alpha-glucosidase** for Pompe; **LAMP2** for Danon; CK, lactate, ammonia for metabolic myopathies.

**Biopsy / pathology:**
- **Endomyocardial biopsy is NOT indicated for HCM diagnosis** — it is reserved for suspected infiltrative phenocopy (amyloid, sarcoid) when non-invasive workup is equivocal.
- **Histopathology** (from myectomy specimens or autopsy): **myocyte disarray** (HP:0031333 ✅) — whorled/interlacing myofiber architecture; **cardiomyocyte hypertrophy** with bizarre nuclei; **interstitial and replacement fibrosis** (HP:0001685 ✅); **intramural coronary small-vessel dysplasia** with medial hypertrophy and luminal narrowing. Autopsy in `TNNI3` p.Arg21Cys SCD victims showed disarray **without gross hypertrophy**.

### 10.2 Genetic Testing

**Recommended approach:** A **multigene HCM/cardiomyopathy NGS panel** including at minimum the nine ClinGen-definitive sarcomere genes (`MYBPC3`, `MYH7`, `TNNT2`, `TNNI3`, `TPM1`, `ACTC1`, `MYL2`, `MYL3`, plus the definitive additions from the 2025 reappraisal) and the phenocopy genes (`GLA`, `LAMP2`, `PRKAG2`, `TTR`, `PTPN11`/RASopathies, `GAA`, `FHL1`). Testing is a **class I** recommendation for HCM probands (2024 AHA/ACC, PMID:38718139).

**Diagnostic yield:** **~40%** of probands receive a P/LP variant on a modern panel (**[verbatim]** from the ClinGen reappraisal preprint: *"the yield of identifying a likely pathogenic or pathogenic variant in a proband is ~40%"*). Yield is substantially lower in non-White populations (18% in Singaporean patients, PMID:32815737).

| Modality | Utility for CMH7 |
|---|---|
| **Gene panel** | **Preferred first-line.** GTR lists **137 clinical tests** for `TNNI3`; **48** for the CMH7 condition (47 with full coding-region sequencing, 31 with del/dup, 5 targeted, 1 select-exon) |
| **Single-gene `TNNI3` testing** | Appropriate only for **cascade testing** of a known familial variant, or for targeted testing of a founder allele (e.g. p.Arg21Cys in South Lebanese families) |
| **WES** | Second-line when panel is negative and the phenotype is atypical/syndromic |
| **WGS** | Research/tertiary setting; can capture deep-intronic and structural variants. Not standard of care |
| **CMA / karyotype / FISH** | **Not indicated** — no established SV mechanism for CMH7 |
| **mtDNA testing** | Indicated only to exclude mitochondrial phenocopy (MELAS, MERRF) when extracardiac features are present. MITOMAP/MSeqDR |
| **Repeat expansion testing** | **Not applicable** (except Friedreich ataxia `FXN` GAA repeat as a hypertrophy phenocopy in the appropriate neurological context) |

**Variant interpretation:** Apply the **ClinGen `TNNI3` variant curation specification (CSpec GN098)** rather than generic ACMG/AMP rules. Key gene-specific points: PM1 hotspot = exons 7–8 (inhibitory/switch and C-terminal mobile domains, ~80% of pathogenic variants); PVS1 (null variant) **does not apply** — truncating `TNNI3` variants are not an established AD-HCM mechanism; PM2 must be relaxed for population-enriched alleles (p.Arg79Cys). The 2024 AHA/ACC guideline recommends **reconfirming reported pathogenicity every 2–3 years**.

### 10.3 Omics-Based Diagnostics

- **RNA-seq:** Not clinically used for CMH7; potential research role in resolving splice-affecting VUS.
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** **No clinical diagnostic role.** hs-cTnI is a single-analyte prognostic marker, not an omics diagnostic.

### 10.4 Clinical Criteria

**Diagnostic criteria (2024 AHA/ACC, PMID:38718139; and 2023 ESC cardiomyopathy guideline):**
- **Adults:** LV wall thickness **≥15 mm** in any segment, unexplained by loading conditions; **≥13 mm** in a first-degree relative of an HCM proband or a genotype-positive individual.
- **Children:** wall thickness **>2 SD above the predicted mean (z-score >2)**, and in relatives z-score >2.
- Diagnosis requires **exclusion** of secondary causes (hypertension, aortic stenosis, athlete's heart) and **phenocopies**.

**Differential diagnosis (with discriminators):**
| Condition | Discriminating features |
|---|---|
| **Athlete's heart** | Wall thickness usually ≤15 mm, symmetric, dilated LV cavity, normal/supranormal diastolic function, regression on detraining, no LGE |
| **Hypertensive heart disease** | Concentric, symmetric, proportional to BP burden, regresses with BP control |
| **Cardiac amyloidosis (ATTR/AL)** | Low ECG voltage *despite* thick walls, granular sparkling myocardium, diffuse subendocardial LGE, ⁹⁹ᵐTc-PYP uptake, monoclonal protein |
| **Fabry disease** | X-linked, low/absent α-Gal A, angiokeratomas, acroparesthesias, proteinuria, **short PR**, basal inferolateral LGE |
| **Danon disease** (`LAMP2`) | X-linked, **WPW**, intellectual disability, skeletal myopathy, marked LVH in young males |
| **PRKAG2 glycogen storage** | **WPW + conduction disease + progressive AV block**; sinus bradycardia |
| **Pompe (`GAA`)** | Infantile: profound hypotonia, macroglossia, low α-glucosidase |
| **RASopathies (Noonan/LEOPARD, `PTPN11`, `RAF1`)** | Dysmorphology, short stature, pulmonic stenosis, lentigines |
| **Friedreich ataxia** | Concentric LVH + progressive ataxia, `FXN` GAA expansion |
| **Mitochondrial cardiomyopathy** | Maternal inheritance, lactic acidosis, multisystem |
| **`TNNI3`-RCM** | Same gene — normal or near-normal wall thickness, bi-atrial dilatation, restrictive filling, preserved systolic function |

**The `TNNI3`-specific discriminator** — the reason CMH7 deserves its own entry — is that these phenocopies are all **multisystem**, whereas `TNNI3` disease is strictly cardiac; and among sarcomeric HCMs, `TNNI3` skews toward **milder hypertrophy with disproportionate diastolic/restrictive physiology and apical morphology**.

### 10.5 Screening

- **Cascade genetic testing** (2024 AHA/ACC, class I): offer to **first-degree relatives only if a P/LP variant is identified in the proband** **[paraphrase]**. A VUS is not actionable for cascade testing.
- **Clinical screening of first-degree relatives** where genotype is unknown or a VUS: TTE + ECG, **every 1–2 years in children/adolescents** and **every 3–5 years in adults** **[paraphrase]**; screening may begin at any age based on family history and preference. In a family with a documented malignant `TNNI3` variant (e.g. p.Arg21Cys), earlier and more intensive screening — plus consideration of CMR — is justified.
- **Genotype-negative relatives** in a family with an established P/LP variant: **discharge from surveillance**, unless the variant is subsequently downgraded **[paraphrase]**.
- **Newborn screening:** **Not applicable** — CMH7 is not on the RUSP and there is no biochemical marker.
- **Population carrier screening:** Not recommended. However, `TNNI3` **is** on the **ACMG SF v3.x secondary-findings list** (as an HCM/cardiomyopathy gene), so P/LP `TNNI3` variants are actionable incidental findings from clinical exome/genome sequencing — an important ascertainment route.

---

## 11. Outcome / Prognosis

### 11.1 Survival and Mortality

**HCM overall:** contemporary HCM-attributable annual mortality at specialist centers is **~0.5%/year**, a marked improvement over historical (~3–6%/year) estimates driven by ICD therapy and referral-center care.

**`TNNI3`-specific — this is the section where CMH7 genuinely diverges:**
- **p.Arg21Cys (South Lebanese founder):** SCD in **30/57 (53%)** of affected individuals at **median age 22.5 years**; SCD was the **first** presentation in **83.3%**; **30% of carriers who had events had no LVH on echocardiography** **[all paraphrase]**. Conclusion **[verbatim]**: *"causes malignant hypertrophic cardiomyopathy with early SCD even in the absence of hypertrophy."*
- **Thin-filament HCM generally (`TNNI3`/`TNNT2`/`TPM1`/`ACTC1`, n=80 vs 150 thick-filament, mean 4.5 y follow-up; Coppini 2014, PMID:25524337):** **arrhythmic risk comparable** between thin- and thick-filament, but **advanced heart failure markedly more common in thin-filament** (15% vs 5%) **[paraphrase]**. Verbatim conclusion: *"thin-filament mutations are associated with increased likelihood of advanced LV dysfunction and heart failure"*.
- **Pediatric `TNNI3`:** **[verbatim]** *"Patients with pathological variants of TNNI3 reportedly experience severe clinical outcomes, such as fatal arrhythmias and sudden death, even in children"* (PMID:38548731).

**Life expectancy:** Near-normal for the majority with mild/nonprogressive disease and appropriate ICD protection; **markedly reduced** in malignant-variant families and in pediatric-onset/restrictive-phenotype disease. Restrictive-phenotype `TNNI3` disease in children has a **poor prognosis** and frequently requires transplantation.

**Disease-specific mortality modes:** (1) sudden arrhythmic death; (2) progressive heart failure; (3) stroke/thromboembolism from AF.

### 11.2 Morbidity and Function

- **Symptomatic burden:** exertional dyspnea (dominant, from diastolic dysfunction), chest pain, palpitations, presyncope/syncope, fatigue.
- **Disability outcomes:** exercise limitation; occupational restriction (commercial driving, aviation, some emergency services); ICD-related activity and psychological restriction; NYHA III–IV in the ~15% of thin-filament patients who progress.
- **QoL instruments:** KCCQ-CSS, HCMSQ, SF-36, EQ-5D, PROMIS. See §3.5 for EXPLORER-HCM effect sizes.

### 11.3 Disease Course — Complications

Atrial fibrillation (HP:0005110 ✅) with cardioembolic stroke; progressive diastolic then systolic heart failure (HP:0001635 ✅); end-stage "burnt-out" HCM requiring transplant; ventricular arrhythmias and SCD (HP:0001645 ✅); infective endocarditis (rare, obstructive subset); post-capillary pulmonary hypertension; procedural complications (complete heart block after alcohol septal ablation; inappropriate ICD shocks and lead complications).

**Recovery potential:** None in the sense of disease reversal. Symptomatic recovery with septal reduction or mavacamten in the obstructive subset is substantial but is **less often applicable in CMH7**, which is disproportionately **nonobstructive**.

### 11.4 Prognostic Factors

**Established HCM SCD risk markers** (feed the HCM Risk-SCD calculator and the AHA/ACC major risk factor list): prior cardiac arrest/sustained VT; unexplained syncope; **family history of SCD**; maximal wall thickness ≥30 mm; LV apical aneurysm; **LV EF <50%**; **extensive LGE (≥15% of LV mass)** on CMR; NSVT on Holter; abnormal BP response to exercise (younger patients); young age.

**`TNNI3`-genotype-specific prognostic considerations:**
- **Genotype itself as a risk marker.** Fahed and colleagues concluded that genetic diagnosis of `TNNI3` p.Arg21Cys **may be sufficient for SCD risk stratification** independent of conventional markers **[paraphrase]** — a genuinely unusual and clinically consequential claim, because it means the standard wall-thickness- and LGE-based calculators **underestimate** risk in this genotype (their carriers died with normal echocardiograms). This should be curated as a distinct, high-value claim.
- **Thin-filament genotype** predicts heart-failure progression more than arrhythmic risk (Coppini 2014).
- **Sarcomere-positive status generally** predicts earlier onset, more fibrosis, and worse composite outcomes than sarcomere-negative HCM (SHaRe registry).
- **Multiple sarcomere variants** predict worse outcomes.

**Prognostic biomarkers:** hs-cTnI and NT-proBNP (both associated with adverse outcomes in HCM); **LGE extent on CMR** is the strongest imaging prognostic marker.

---

## 12. Treatment

**There is no `TNNI3`-specific or genotype-directed therapy in clinical use.** Management follows the **2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM guideline** (PMID:38718139; DOI:10.1161/CIR.0000000000001250 and 10.1016/j.jacc.2024.02.014). Two genotype-relevant caveats deserve prominence in a CMH7 entry: (i) CMH7 is **more often nonobstructive**, so the obstruction-directed armamentarium (disopyramide, myectomy, alcohol ablation, mavacamten) applies to a **smaller fraction** of these patients than in thick-filament HCM; and (ii) the **diastolic/restrictive** physiology and, for at least one variant, the **hypertrophy-independent SCD risk** shift management emphasis toward heart-failure care and toward a lower ICD threshold.

### 12.1 Pharmacotherapy

| Treatment | Class / MoA | Indication in CMH7 | NCIT |
|---|---|---|---|
| **Beta blockers** (metoprolol, bisoprolol, propranolol, atenolol) | β₁-adrenergic antagonist; negative inotropy/chronotropy, prolongs diastolic filling | **First-line** for symptomatic obstructive and nonobstructive HCM | `NCIT:C15986` Pharmacotherapy ✅ + `therapeutic_agent` **NCIT:C61845 Metoprolol** ✅ |
| **Non-dihydropyridine CCBs** (verapamil, diltiazem) | L-type Ca²⁺ channel blockade; negative inotropy, improved relaxation | Alternative first-line when β-blockers not tolerated. **Caution/contraindicated** with severe obstruction + hypotension | `NCIT:C15986` ✅ + **NCIT:C928 Verapamil** ✅ |
| **Disopyramide** | Class Ia antiarrhythmic; potent negative inotrope | **Add-on for obstructive HCM** refractory to β-blocker/CCB. Anticholinergic side effects | `NCIT:C15986` ✅ + **NCIT:C61730 Disopyramide** ✅ |
| **Mavacamten** | **Cardiac myosin inhibitor** — allosterically reduces actin–myosin cross-bridge formation, decreasing hypercontractility | **Obstructive HCM** with inadequate response to first-line therapy (2024 guideline). FDA-approved. **REMS program** — echo monitoring of LVEF required | `NCIT:C15986` ✅ + `therapeutic_agent` **NCIT:C174901 Mavacamten** ✅ ; `therapeutic_modality: SMALL_MOLECULE` |
| **Aficamten** | Next-generation cardiac myosin inhibitor (SEQUOIA-HCM) | Obstructive HCM; FDA review/approval status should be verified as of 2026 | Verify NCIT term |
| **Diuretics** | Loop/thiazide | Cautious use for congestion; avoid over-diuresis in obstruction | `NCIT:C15986` ✅ |
| **Anticoagulation** (DOACs preferred; warfarin) | Factor Xa / thrombin inhibition | **AF in HCM — anticoagulate regardless of CHA₂DS₂-VASc score** (class I). Highly relevant given LA dilation in CMH7 | `NCIT:C15986` ✅ |
| **Amiodarone / sotalol** | Antiarrhythmics | AF rhythm control; VT suppression adjunct to ICD | `NCIT:C15986` ✅ |

**Drugs to avoid:** pure vasodilators (dihydropyridine CCBs, nitrates, ACE-I/ARB in significant obstruction), high-dose diuretics, digoxin, and positive inotropes in obstructive disease — all worsen the LVOT gradient.

**Pharmacogenomics:**
- **Mavacamten is a CYP2C19 substrate.** Dose titration and the labeled dosing algorithm are **CYP2C19 phenotype-dependent**; poor metabolizers have substantially higher exposure and require dose adjustment. Check **PharmGKB** and the FDA label for the current genotype-guided dosing table. This is the single most clinically actionable PGx interaction in HCM care.
- **Metoprolol is a CYP2D6 substrate** — CPIC has a metoprolol/CYP2D6 guideline; poor metabolizers experience greater bradycardia.
- **Warfarin** — CYP2C9/VKORC1 (CPIC), though DOACs are now preferred.

### 12.2 Advanced Therapeutics

- **Gene therapy:** **No clinical gene therapy for `TNNI3` exists.** Strong preclinical rationale from the isogenic EHT work: **AAV-mediated wild-type `TNNI3` overexpression rescued impaired relaxation** in R170W iPSC-CMs and EHTs **[paraphrase, PMID:38193576]** — the authors explicitly note "the possible benefits of gene therapies for patients with RCM." Because the mechanism is dominant-negative (poison peptide), an **allele-specific silencing** or **base/prime-editing correction** strategy is theoretically more attractive than simple gene addition; wild-type overexpression works in the dish by dilution of the mutant fraction. Contrast with `MYBPC3`, where haploinsufficiency makes gene replacement (currently in clinical trials, e.g. TN-201) mechanistically straightforward — **that approach does not transfer to `TNNI3`.**
- **Gene editing:** Preclinical only. CRISPR correction of the `TNNI3` variant in patient iPSCs has been demonstrated (the isogenic control lines in PMID:38193576).
- **Cell therapy:** No role.
- **RNA-based therapies:** No `TNNI3` ASO or siRNA in development. An allele-selective ASO/siRNA is a logical but unrealized target given the dominant-negative mechanism.
- **Targeted therapy:** Mavacamten and aficamten are the only mechanism-targeted agents. Note a conceptual mismatch worth curating: **myosin inhibitors target hypercontractility, but the `TNNI3` lesion is Ca²⁺ sensitization with *reduced* maximal force** (PMID:18430738). Whether myosin inhibition is the mechanistically optimal intervention for thin-filament HCM — as opposed to a **Ca²⁺-desensitizing** thin-filament–directed agent — is an open and genuinely interesting question. Troponin-targeting agents that modulate thin-filament Ca²⁺ sensitivity have been shown in vitro to modulate the effects of de novo `TNNC1`/`TNNI3` infantile cardiomyopathy variants (PMC8431798 — verify PMID) but none has reached the clinic.
- **Immunotherapy:** Not applicable.

### 12.3 Surgical and Interventional

| Intervention | Role | NCIT |
|---|---|---|
| **Surgical septal myectomy** (extended Morrow) | Gold standard for drug-refractory severe obstruction at experienced centers. **Less often applicable in CMH7 (nonobstructive predominance)** | NCIT term for septal myectomy **not resolved** in this session — verify; fall back to `NCIT:C15329` Surgical Procedure with a specific `preferred_term` |
| **Alcohol septal ablation** | Catheter alternative for suitable anatomy in older/higher-surgical-risk patients. Risk of complete heart block | Verify NCIT |
| **ICD implantation** | **Primary prevention** per risk stratification; **secondary prevention** (class I) after cardiac arrest/sustained VT. **Threshold should be lower in malignant `TNNI3` genotypes.** Subcutaneous ICD used in the pediatric p.Ile195Phe case | **NCIT:C80435 Implantable Cardioverter-Defibrillator Placement** ✅ ; `therapeutic_modality: DEVICE` |
| **Catheter ablation** | AF rhythm control | Verify NCIT |
| **Dual-chamber pacing** | Legacy/limited role for obstruction; used for bradycardia | Verify NCIT |
| **Heart transplantation** | End-stage HCM, restrictive-phenotype `TNNI3` disease, or intractable arrhythmia. **Disproportionately relevant in CMH7** given restrictive/HF progression | `NCIT:C15289` Organ Transplantation ✅ ; `therapeutic_modality: SURGERY` |
| **Mechanical circulatory support (LVAD)** | Technically difficult in a small, stiff, non-dilated ventricle; **restrictive `TNNI3` physiology is a relative contraindication**. ECMO has been used as a bridge in pediatric `TNNI3` RCM with reported difficulty (PMC11157066 — verify PMID) | Verify NCIT |

### 12.4 Supportive and Rehabilitative

Heart-failure symptom management; AF rate/rhythm control and stroke prophylaxis; **cardiac rehabilitation** — the 2024 guideline endorses **moderate-intensity recreational exercise as beneficial** for most HCM patients, a significant liberalization from prior restriction-heavy guidance (`NCIT:C15315` Rehabilitation ✅); psychological support for ICD recipients and for families with a history of sudden death; palliative care in end-stage disease (`NCIT:C15747` Supportive Care ✅).

### 12.5 Experimental / Clinical Trials

- **NCT03470545** — EXPLORER-HCM (mavacamten, phase 3, completed). Registered per the abstract **[verbatim]**: *"This study is registered with ClinicalTrials.gov, NCT03470545."*
- **MAVERICK-HCM** — mavacamten in **nonobstructive** HCM (phase 2; the population most relevant to CMH7) — verify NCT.
- **ODYSSEY-HCM** — mavacamten in nonobstructive HCM (phase 3) — verify NCT and status.
- **SEQUOIA-HCM / ACACIA-HCM** — aficamten — verify NCT.
- **VALOR-HCM** — mavacamten as an alternative to septal reduction therapy — verify NCT.
- **VANISH** — valsartan in early sarcomeric HCM (disease-modification in G+/P− and early-phenotype carriers) — verify NCT; directly relevant to the CMH7 preclinical window.
- **No `TNNI3`-specific trial exists.** `TNNI3` carriers are enrolled within general HCM trials.

*(Per dismech convention, each of these requires `just fetch-reference NCT#######` before curation, with the snippet quoted from the cached ClinicalTrials.gov record.)*

### 12.6 Treatment Outcomes

**EXPLORER-HCM efficacy [all verbatim from the abstract]:**
- Primary endpoint: **45/123 (37%) mavacamten vs 22/128 (17%) placebo** (difference +19.4%, 95% CI 8.7 to 30.1; **p=0.0005**)
- Post-exercise LVOT gradient: **−36 mm Hg** (95% CI −43.2 to −28.1; p<0.0001)
- pVO₂: **+1.4 mL/kg per min** (0.6 to 2.1; p=0.0006)
- NYHA class improvement ≥1: **80/123 vs 40/128** (34% more; 95% CI 22.2 to 45.4; p<0.0001)
- **"Safety and tolerability were similar to placebo. Treatment-emergent adverse events were generally mild. One patient died by sudden death in the placebo group."**

**Adverse events of note:** mavacamten — **reversible reduction in LVEF / systolic dysfunction** (the class effect driving the REMS echo-monitoring requirement), atrial fibrillation, heart failure; disopyramide — anticholinergic effects, QT prolongation; alcohol septal ablation — complete heart block (~10%); myectomy at expert centers — <1% mortality. Resources: FAERS, MedWatch.

### 12.7 Treatment Strategy

**Algorithm (2024 AHA/ACC, adapted for CMH7):**
1. **All patients:** confirm diagnosis and exclude phenocopies → genetic testing → SCD risk stratification (with the explicit CMH7 caveat that conventional risk calculators may under-call risk in malignant `TNNI3` genotypes) → cascade family screening → exercise counseling (permissive for moderate recreational activity) → AF surveillance.
2. **Asymptomatic:** no pharmacotherapy indicated; surveillance imaging.
3. **Symptomatic + obstructive** (the minority in CMH7): β-blocker → add/switch verapamil → add disopyramide **or** mavacamten → septal reduction therapy if refractory.
4. **Symptomatic + nonobstructive** (the CMH7-typical path): β-blocker or verapamil for diastolic filling; treat congestion cautiously; **this is the therapeutic gap** — no proven disease-modifying therapy for nonobstructive HCM, which is precisely where thin-filament patients concentrate. Advanced HF → transplant evaluation.
5. **AF:** anticoagulate regardless of CHA₂DS₂-VASc; rate or rhythm control.
6. **High arrhythmic risk:** ICD.

**Personalized medicine:** currently limited to (i) genotype-driven cascade screening, (ii) genotype-informed SCD risk stratification in specific `TNNI3` variants, and (iii) **CYP2C19-guided mavacamten dosing**. Genotype-directed disease-modifying therapy for `TNNI3` remains aspirational.

---

## 13. Prevention

### 13.1 Prevention Levels

- **Primary prevention (preventing the disease):** Not achievable for variant carriage. The only true primary prevention is **reproductive**: preimplantation genetic testing for monogenic disease (PGT-M) or prenatal diagnosis, following genetic counseling. Whether early pharmacotherapy in G+/P− carriers prevents phenotype conversion is **unproven** (the VANISH question).
- **Secondary prevention (early detection):** **Cascade genetic testing** of first-degree relatives is the highest-yield intervention in CMH7 — it identifies at-risk individuals *before* phenotype and, in malignant `TNNI3` genotypes, before an event that would otherwise be first-and-fatal. Coupled with serial TTE/ECG (1–2 y children, 3–5 y adults) and CMR where LGE detection matters.
- **Tertiary prevention (preventing complications):** ICD for SCD; anticoagulation for AF-related stroke; blood-pressure and weight control to limit remodeling; heart-failure therapy; endocarditis awareness in the obstructive subset; avoidance of contraindicated vasodilators/inotropes.

### 13.2 Immunization

Not applicable as disease prevention. Standard **influenza, COVID-19, and pneumococcal vaccination** are appropriate for patients with structural heart disease to reduce decompensation from intercurrent infection.

### 13.3 Screening and Early Detection

- **Population screening: not recommended.** Neither newborn nor general-population genetic screening for HCM genes is endorsed. Pre-participation athletic screening (ECG-inclusive in the Italian/European model, history-and-exam in the US model) remains contested and is not CMH7-specific.
- **Genetic screening:** cascade testing (§10.5); **PGT-M and prenatal testing** available for known familial variants; both require formal genetic counseling.
- **Secondary-findings reporting:** `TNNI3` is on the **ACMG SF v3.x** list, so P/LP variants are reported from clinical ES/GS regardless of indication — an unavoidable and deliberate ascertainment channel.
- **Risk stratification:** HCM Risk-SCD calculator (ESC) and AHA/ACC major risk factors; **with the CMH7-specific proviso** that both underweight genotype and may miss the hypertrophy-negative `TNNI3` carrier at risk.

### 13.4 Behavioral Interventions

Moderate-intensity recreational exercise is now **endorsed** (2024 guideline) rather than broadly restricted; competitive/high-intensity athletics require **shared decision-making** with an HCM specialist. Weight management, blood-pressure control, adequate hydration, avoidance of alcohol excess and stimulants (including anabolic steroids and high-dose sympathomimetics).

### 13.5 Genetic Counseling

**Essential and non-optional in CMH7.** `NCIT:C15240` Genetic Counseling ✅. Content:
- 50% transmission risk per pregnancy (autosomal dominant).
- **Incomplete (~50%) and age-dependent penetrance, and highly variable expressivity** — a positive genotype is not a diagnosis, and a normal echocardiogram is not reassurance in a malignant-variant family.
- The `TNNI3` allelic spectrum: relatives may develop HCM, RCM, or (rarely) DCM.
- The reality of SCD as a first presentation, and the case for a low ICD threshold in high-risk families.
- Reproductive options: PGT-M, prenatal diagnosis, donor gametes, adoption, or unassisted conception with cascade screening of offspring.
- ~1% empirical recurrence risk after an apparently de novo variant (gonadal mosaicism).
- VUS management and the 2–3-yearly reinterpretation cadence.
- Psychosocial support, insurance/GINA considerations, and family communication about a heritable sudden-death risk.

Resources: NSGC, ACMG, **GeneReviews "Hypertrophic Cardiomyopathy Overview"**.

### 13.6 Public Health and Environmental Interventions

Not applicable in the classical sense. Relevant public-health measures: **AED availability and CPR training** in schools, sports venues, and public spaces (this is the highest-impact population intervention for HCM-related SCD); **cardiac-arrest registries**; **molecular autopsy** programs for sudden unexplained death in the young, which are a major route to identifying `TNNI3` families retrospectively (exactly the mechanism by which the Lebanese founder families were characterized).

### 13.7 Prophylaxis

ICD (device prophylaxis against SCD); anticoagulation (prophylaxis against AF-related stroke). **Infective endocarditis antibiotic prophylaxis is NOT routinely recommended for HCM** in current guidelines.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and Orthologs

| Species | NCBI Taxon | Gene | NCBI Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | `TNNI3` | 7137 | |
| *Mus musculus* | NCBITaxon:10090 | `Tnni3` | 21954 (verify) | Primary disease model species; chromosome 7 |
| *Rattus norvegicus* | NCBITaxon:10116 | `Tnni3` | 24837 (verify) | Physiology model |
| *Felis catus* | NCBITaxon:9685 | `TNNI3` | — | Naturally occurring HCM species (see below) |
| *Canis lupus familiaris* | NCBITaxon:9615 | `TNNI3` | — | |
| *Danio rerio* | NCBITaxon:7955 | `tnni1b`/`tnnt2a` | — | Cardiac troponin orthology in zebrafish is complicated by teleost genome duplication; `tnni3` is not a clean 1:1 ortholog. Verify with Alliance of Genome Resources before curating |

The cardiac-specific **N-terminal extension with the PKA Ser23/Ser24 site is a mammalian/amniote innovation** and is highly conserved — the reason R21C is mechanistically interpretable across species and the reason mouse models of it are informative. See "TNNI1, TNNI2 and TNNI3: Evolution, Regulation, and Protein Structure-Function Relationships" (PMC5798203) for the comparative/evolutionary treatment.

### 14.2 Naturally Occurring Disease in Other Species

**Feline HCM is the flagship naturally occurring animal HCM** — the most common feline heart disease and a genuine spontaneous model. However, **the established feline HCM genes are `MYBPC3` and `MYH7`, not `TNNI3`**:
- **OMIA:002951-9685** — Cardiomyopathy, hypertrophic, MYBPC3-related, autosomal dominant, *Felis catus*
- **OMIA:002952-9685** — Cardiomyopathy, hypertrophic, MYBPC3-related, autosomal recessive, *Felis catus*
- **OMIA:002212-9685** — Cardiomyopathy, hypertrophic, MYH7-related, *Felis catus*

Causal variants: **`MYBPC3` p.A31P** in **Maine Coon** cats (Meurs et al. 2005) and **`MYBPC3` p.R820W** in **Ragdoll** cats (Meurs et al. 2007) **[paraphrase — verify PMIDs]**. Feline HCM recapitulates human disease closely, including LVH, diastolic dysfunction, LA enlargement, arterial thromboembolism, and **sudden death**. **VBO** identifiers exist for Maine Coon and Ragdoll breeds — look them up before curating.

**A `TNNI3` variant has not been established as a cause of naturally occurring feline HCM.** A 2024 *Frontiers in Veterinary Science* paper applied ACMG criteria to feline HCM-associated gene variants (including thin-filament genes) — verify PMID and findings before asserting any `TNNI3` claim. **Curation guidance: do not assert a feline `TNNI3` natural disease. Curate feline HCM as a comparative-pathology analogue of the human disease, explicitly noting the gene mismatch.**

Naturally occurring HCM is also described in **dogs** (rare), **pigs**, and **non-human primates**; genes are largely uncharacterized.

### 14.3 Comparative Biology

- **Comparative pathology:** feline HCM shows the same triad — myocyte hypertrophy, **myofiber disarray**, and interstitial fibrosis — plus intramural arteriosclerosis, and shares the SCD and heart-failure endpoints. The key feline-specific difference is the prominence of **aortic thromboembolism ("saddle thrombus")**, far more common than in human HCM.
- **Evolutionary conservation:** the troponin regulatory mechanism is conserved across striated muscle in bilaterians; the cardiac isoform's N-terminal β-adrenergic phospho-switch is a vertebrate/mammalian specialization. Resources: Alliance of Genome Resources, HomoloGene, OrthoDB.

### 14.4 Transmission

**Not applicable.** CMH7 is a germline genetic disease. **Zero zoonotic potential; no cross-species transmission.**

---

## 15. Model Organisms

### 15.1 Mouse Models — the Primary Evidence Base

**(a) Transgenic Tg-R145G (overexpression) — Wen et al. 2008, PMID:18430738**
Cardiac-specific overexpression of human cTnI R145G. **Best-characterized biophysical model of a CMH7 variant.** Findings (verbatim quotes in §6.1): increased Ca²⁺ sensitivity of both ATPase and force; decreased maximal Ca²⁺-activated force; unchanged cross-bridge turnover; **higher energy consumption**; 2–4% residual attached cross-bridges at pCa 9.0 vs <1% in WT; prolonged force and [Ca²⁺] transients.
- **Recapitulation:** excellent for the *molecular and myofilament* phenotype (Ca²⁺ sensitization, impaired relaxation, energetic cost). This model established the mechanistic chain from variant to diastolic dysfunction.
- **Limitations:** transgenic **overexpression** (non-physiological mutant:WT stoichiometry) rather than knock-in; readouts are largely ex vivo skinned-fiber/papillary muscle; the abstract's conclusion about hypertrophy is inferential ("most likely caused by compensatory mechanisms") rather than directly demonstrated.
- Evidence classification: **MODEL_ORGANISM** (in vivo mouse) for the papillary-muscle work; skinned-fiber measurements arguably **IN_VITRO** — split evidence items accordingly per the dismech SOP.

**(b) Knock-in Tnni3^R21C — Wang et al. 2012, PMID:22086914**
The gold-standard genetic model — the mutation at the endogenous locus, in heterozygous (R21C⁺/⁻) and homozygous (R21C⁺/⁺) states.
- **[verbatim]** *"the R21C mutation abolished the in vivo phosphorylation of Ser(23)/Ser(24) in the mutant cTnI"*
- Heterozygous hearts incorporated **~25% mutant cTnI** **[paraphrase]** — a physiologically faithful allelic ratio.
- Both genotypes **"activated the fetal gene program and developed a remarkable degree of cardiac hypertrophy and fibrosis"** **[paraphrase]**.
- PKA treatment of skinned fibers "reduced (R21C⁺/⁻) or abolished (R21C⁺/⁺) the well known decrease in the Ca²⁺ sensitivity of tension" **[paraphrase]** — a direct demonstration of the lost lusitropic reserve.
- Longitudinal echo: **hypertrophy after 12 months**, with longer filling times and impaired relaxation; **isoproterenol-conditional** delays in Ca²⁺ decay and sarcomere relaxation appearing at older but not 6-month ages **[paraphrase]**.
- **Recapitulation:** excellent — reproduces the human hypertrophy, fibrosis, diastolic dysfunction, and the specific molecular lesion (loss of PKA phospho-switch).
- **Limitations:** the human p.Arg21Cys phenotype is dominated by **early sudden arrhythmic death**, which the mouse does not straightforwardly reproduce; mouse cardiac physiology (heart rate ~600 bpm, α-MHC-dominant ventricle vs human β-MHC) limits translation of relaxation kinetics; the late (12-month) hypertrophy onset compresses awkwardly against a human disease that can kill at 22.
- Follow-on: **PMC4415466** — the R21C knock-in shows **left–right ventricular differences in contractile force generation**, a chamber-asymmetry finding with no established human counterpart.

**(c) Other relevant mouse models**
- **Tg-R146G (=R145G in human numbering) and comparative R21C/R146G studies** — "Troponin I Mutations R146G and R21C Alter Cardiac Troponin Function, Contractile Properties, and Modulation by Protein Kinase A (PKA)-mediated Phosphorylation" (*J Biol Chem*) — verify PMID.
- **Long-term PKA-phosphorylation-ablation models** — "Long Term Ablation of PKA-mediated Cardiac Troponin I Phosphorylation Leads to Excitation-Contraction Uncoupling and Diastolic Dysfunction in a Knock-in Mouse Model of Hypertrophic Cardiomyopathy" (*J Biol Chem*) — verify PMID. Directly relevant to the R21C mechanism.
- **cTnI R193H (mouse) / R192H (human) RCM knock-in** — the restrictive arm of the allelic series; see "Restrictive Cardiomyopathy Caused by Troponin Mutations: Application of Disease Animal Models in Translational Studies" (PMC5165243) for the review.
- **Tnni3 null (knockout)** mice die of acute heart failure in the neonatal period as the fetal ssTnI isoform is replaced — a loss-of-function phenotype confirming that `TNNI3` is essential but **not** a model of CMH7 (which is dominant-negative, not haploinsufficient). Verify the primary reference before curating.

**Model resources:** **MGI** (`Tnni3`; search alleles at informatics.jax.org — note the MGI ID was not correctly resolved in this session and must be verified), **IMPC/KOMP** (null alleles), **IMSR** (strain availability), **MMRRC**, **EMMA**.

### 15.2 In Vitro / Cellular Models

**(a) Patient-derived iPSC-cardiomyocytes and engineered heart tissue (EHT) — the highest-value modern platform.**
Hasegawa et al. 2024 (PMID:38193576; DOI:10.1111/dgd.12909) — patient iPSC line carrying `TNNI3` **R170W** vs **isogenic CRISPR-corrected control** **[all paraphrase]**:
- R170W iPSC-CMs: **altered Ca²⁺ kinetics, prolonged tau (relaxation time constant)**
- R170W EHTs: **increased ratio of relaxation force to contractile force**
- Both phenotypes **reversed in the isogenic corrected line** — establishing variant causality
- **Wild-type `TNNI3` overexpression rescued impaired relaxation** — establishing a gene-therapy rationale
- *Evidence classification:* **IN_VITRO**

Companion: *J Am Heart Assoc* 2024, "Impaired Relaxation in Induced Pluripotent Stem Cell-Derived Cardiomyocytes with Pathogenic TNNI3 Mutation of Pediatric Restrictive Cardiomyopathy" — verify PMID.

**(b) Skinned fiber / reconstituted thin-filament biochemistry.** Human and mouse skinned papillary/trabecular preparations; recombinant troponin exchange into demembranated fibers; in vitro motility assays; ATPase assays. These generate the **force–pCa ΔpCa₅₀** measurement that anchors ACMG PS3 for `TNNI3` variants.

**(c) Human myectomy tissue.** Ex vivo trabeculae from HCM myectomy specimens (Coppini's group is the principal source) allow direct measurement of human `TNNI3`-carrier myofilament function — the closest thing to a human "model system."
- Note: "Restrictive Cardiomyopathy Troponin I R145W Mutation Does Not Perturb Myofilament Length-dependent Activation in Human Cardiac Sarcomeres" (PMC5076848) — a useful negative result showing that **not every myofilament property is disturbed**, which is worth curating as a scope constraint on the mechanism.

**(d) Structural/computational.** Molecular dynamics on the troponin core complex (PDB 1J1E) to predict variant effects; AlphaFold for the disordered N-terminal extension. *Evidence classification:* **COMPUTATIONAL**.

### 15.3 Model Characteristics Summary

| Aspect of human CMH7 | Mouse R21C KI | Mouse Tg-R145G | iPSC-CM/EHT | Feline HCM |
|---|---|---|---|---|
| Ca²⁺ sensitization | ✅ | ✅ | ✅ | n/a |
| Impaired relaxation / diastolic dysfunction | ✅ | ✅ | ✅ | ✅ |
| Loss of PKA lusitropic reserve | ✅ (definitive) | — | — | — |
| Increased tension cost / energetic mismatch | — | ✅ | ~ | — |
| Cardiac hypertrophy | ✅ (late, 12 mo) | inferred | ✗ (immature CMs) | ✅ |
| Myocyte disarray | ~ | ~ | ✗ | ✅ |
| Interstitial fibrosis | ✅ | — | ✗ (unless multicellular EHT) | ✅ |
| **Sudden arrhythmic death** | ✗ | ✗ | ✗ | ✅ |
| Restrictive/RCM phenotype | (R193H model) | — | ✅ (R170W) | — |
| Correct allelic stoichiometry | ✅ (~25% mutant) | ✗ (overexpression) | ✅ (patient-derived) | ✅ (natural) |

**The dominant translational gap — flag as a dismech `HUMAN_MODEL_MISMATCH` discussion, not a generic `KNOWLEDGE_GAP`:** the defining and lethal feature of human `TNNI3` p.Arg21Cys disease is **sudden arrhythmic death in the absence of hypertrophy at a median age of 22.5 years**, whereas the corresponding knock-in mouse develops hypertrophy slowly (after 12 months) without a comparable arrhythmic-death phenotype. Evidence exists in the model; its fidelity to the human arrhythmic mechanism is the open question. Proposed resolving experiments: programmed electrical stimulation and telemetric arrhythmia monitoring in R21C knock-in mice under β-adrenergic challenge; optical mapping of the R21C heart; arrhythmia phenotyping of R21C iPSC-CM monolayers and EHTs; and human tissue/CMR studies of the disarray–arrhythmia relationship in hypertrophy-negative carriers.

### 15.4 Research Applications

Myofilament Ca²⁺-sensitivity pharmacology (Ca²⁺ desensitizers as a mechanistically rational `TNNI3`-directed drug class); β-adrenergic/PKA signaling and lusitropic reserve; cardiac energetics and mechano-energetic uncoupling; hypertrophic and fibrotic signaling; gene-therapy and gene-editing proof-of-concept (the isogenic EHT rescue); variant functional classification for ACMG PS3.

---

## Appendix A — Master Reference List with PMIDs

| # | Citation | PMID | Evidence source | Verbatim quote available? |
|---|---|---|---|---|
| 1 | Kimura A, et al. Mutations in the cardiac troponin I gene associated with hypertrophic cardiomyopathy. *Nat Genet* 1997;16(4):379-82. DOI:10.1038/ng0897-379 | **9241277** | HUMAN_CLINICAL | ✅ **Yes — full abstract** |
| 2 | Mogensen J, et al. Idiopathic restrictive cardiomyopathy is part of the clinical expression of cardiac troponin I mutations. *J Clin Invest* 2003;111(2):209-16. DOI:10.1172/JCI16336 | **12531876** | HUMAN_CLINICAL | ✅ **Yes — full abstract** |
| 3 | Niimura H, et al. Sarcomere protein gene mutations in hypertrophic cardiomyopathy of the elderly. *Circulation* 2002 | **11815426** | HUMAN_CLINICAL | ✅ **Yes — full abstract** |
| 4 | Wen Y, et al. Functional consequences of the human cardiac troponin I hypertrophic cardiomyopathy mutation R145G in transgenic mice. *J Biol Chem* 2008;283(29):20484-94. DOI:10.1074/jbc.M801661200 | **18430738** | MODEL_ORGANISM / IN_VITRO | ✅ **Yes — full abstract** |
| 5 | Wang Y, et al. Generation and functional characterization of knock-in mice harboring the cardiac troponin I-R21C mutation. *J Biol Chem* 2012. DOI:10.1074/jbc.M111.294306 | **22086914** | MODEL_ORGANISM | ⚠️ Partial verbatim; re-fetch |
| 6 | Coppini R, et al. Clinical phenotype and outcome of HCM associated with thin-filament gene mutations. *J Am Coll Cardiol* 2014;64(24):2589-2600. DOI:10.1016/j.jacc.2014.09.059 | **25524337** | HUMAN_CLINICAL | ⚠️ Partial verbatim; re-fetch |
| 7 | Fahed AC, et al. Founder Mutation in N Terminus of Cardiac Troponin I Causes Malignant HCM. *Circ Genom Precis Med* 2020;13(5). DOI:10.1161/CIRCGEN.120.002991. PMC7676616 | **32885985** | HUMAN_CLINICAL | ⚠️ Partial verbatim; re-fetch |
| 8 | Pua CJ, et al. Genetic Studies of HCM in Singaporeans Identify Variants in TNNI3 and TNNT2 That Are Common in Chinese Patients. *Circ Genom Precis Med* 2020 | **32815737** | HUMAN_CLINICAL | ✅ **Yes — full abstract** |
| 9 | Hespe S, et al. Genes Associated With HCM: A Reappraisal by the ClinGen Hereditary Cardiovascular Disease GCEP. *J Am Coll Cardiol* 2025;85(7):727-740. DOI:10.1016/j.jacc.2024.12.010 | **39971408** | OTHER (expert panel) | ⚠️ Re-fetch; preprint PMID 39132495 / PMC11312670 |
| 10 | Ommen SR, et al. 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of HCM. *Circulation*/*JACC* 2024. DOI:10.1161/CIR.0000000000001250 | **38718139** | OTHER (guideline) | ⚠️ Re-fetch |
| 11 | Olivotto I, et al. Mavacamten for treatment of symptomatic obstructive HCM (EXPLORER-HCM). *Lancet* 2020;396(10253):759-769. DOI:10.1016/S0140-6736(20)31792-X | **32871100** | HUMAN_CLINICAL | ✅ **Yes — full abstract** |
| 12 | Semsarian C, Ingles J, Maron MS, Maron BJ. New perspectives on the prevalence of hypertrophic cardiomyopathy. *J Am Coll Cardiol* 2015 | **25814232** | HUMAN_CLINICAL | ⚠️ Re-fetch |
| 13 | Pediatric HCM caused by a novel TNNI3 variant (p.Ile195Phe). *Hum Genome Var* 2024. DOI:10.1038/s41439-024-00272-1. PMC10978967 | **38548731** | HUMAN_CLINICAL | ✅ **Yes — full abstract + 3 key claims** |
| 14 | Norrish G, et al. Childhood-onset HCM caused by thin-filament sarcomeric variants. *J Med Genet* 2024;61(5):420-422 | **38296631** | HUMAN_CLINICAL | ⚠️ Re-fetch |
| 15 | Hasegawa A, et al. Gene correction and overexpression of TNNI3 improve impaired relaxation in EHT model of pediatric RCM. *Dev Growth Differ* 2024. DOI:10.1111/dgd.12909. PMC11457505 | **38193576** | IN_VITRO | ⚠️ Re-fetch |

**Structured-source references usable directly as dismech evidence:**
- **`CGGV:` (ClinGen Gene-Disease Validity)** — the TNNI3–HCM Definitive assertion. Locate the assertion ID via `just clingen-list` and cite the validity table row.
- **`ORPHA:`** — the Orphanet familial isolated HCM record (definition, epidemiology class, HPO phenotype table with frequencies, gene table). This is likely the **highest-yield structured source** for the phenotype-frequency and prevalence sections of this entry, since HPO's OMIM:613690 annotations have such small denominators.
- **`NCIT:C174901`** (Mavacamten) — check for an `Accepted_Therapeutic_Use_For` (P302) edge to cite the indication.

---

## Appendix B — Verified Ontology Terms Ready for Curation

All terms below were resolved and label-verified with OAK against the repository's configured adapters during this session.

**MONDO:** `MONDO:0013369` hypertrophic cardiomyopathy 7

**Gene:** `hgnc:11947` TNNI3

**HPO:** `HP:0001639` Hypertrophic cardiomyopathy · `HP:0031992` Apical hypertrophic cardiomyopathy · `HP:0001714` Ventricular hypertrophy · `HP:0001670` Asymmetric septal hypertrophy · `HP:0005144` Ventricular septal hypertrophy · `HP:0025168` Left ventricular diastolic dysfunction · `HP:0032092` Left ventricular outflow tract obstruction · `HP:0001723` Restrictive cardiomyopathy · `HP:0031333` Myocardial sarcomeric disarray · `HP:0031318` Myofiber disarray · `HP:0001685` Myocardial fibrosis · `HP:0005110` Atrial fibrillation · `HP:0001716` Wolff-Parkinson-White syndrome · `HP:0004308` Ventricular arrhythmia · `HP:0004756` Ventricular tachycardia · `HP:0011675` Arrhythmia · `HP:0001645` Sudden cardiac death · `HP:0001695` Cardiac arrest · `HP:0001635` Congestive heart failure · `HP:0002094` Dyspnea · `HP:0001279` Syncope · `HP:0100749` Chest pain · `HP:0001962` Palpitations · `HP:0003581` Adult onset · `HP:0000006` Autosomal dominant inheritance

**GO (BP):** `GO:0060048` cardiac muscle contraction · `GO:0055117` regulation of cardiac muscle contraction · `GO:0010882` regulation of cardiac muscle contraction by calcium ion signaling · `GO:0032971` regulation of muscle filament sliding · `GO:1904114` positive regulation of muscle filament sliding · `GO:0003300` cardiac muscle hypertrophy · `GO:0014898` cardiac muscle hypertrophy in response to stress · `GO:0010613` positive regulation of cardiac muscle hypertrophy · `GO:0045214` sarcomere organization

**GO (CC):** `GO:1990584` cardiac Troponin complex · `GO:0005861` troponin complex · `GO:0030017` sarcomere

**CL:** `CL:2000046` ventricular cardiac muscle cell · `CL:0000746` cardiac muscle cell · `CL:0002548` fibroblast of cardiac tissue

**UBERON:** `UBERON:0002084` heart left ventricle · `UBERON:0002094` interventricular septum · `UBERON:0004667` interventricular septum muscular part · `UBERON:0002349` myocardium · `UBERON:0001083` myocardium of ventricle

**NCIT:** `NCIT:C15986` Pharmacotherapy · `NCIT:C174901` Mavacamten · `NCIT:C61845` Metoprolol · `NCIT:C928` Verapamil · `NCIT:C61730` Disopyramide · `NCIT:C80435` Implantable Cardioverter-Defibrillator Placement · `NCIT:C15289` Organ Transplantation · `NCIT:C15240` Genetic Counseling · `NCIT:C15315` Rehabilitation · `NCIT:C15747` Supportive Care · `NCIT:C15329` Surgical Procedure

**Not resolved in this session — verify before use:** NCIT terms for septal myectomy, alcohol septal ablation, catheter ablation, echocardiography, cardiac MRI; UBERON terms for heart (`UBERON:0000948`) and left atrium (`UBERON:0002079`); GO terms for myofibril, striated muscle thin filament, mitochondrion, sarcoplasmic reticulum; CL terms for endothelial cell and macrophage; LOINC codes for hs-cTnI and NT-proBNP; the Orphanet code for familial isolated HCM; NCT identifiers for MAVERICK-HCM, ODYSSEY-HCM, SEQUOIA-HCM, VALOR-HCM, and VANISH.

---

## Appendix C — Curation Notes and Cautions

1. **Do not blindly propagate the HPO frequency denominators for OMIM:613690.** "Adult onset 6/6" derives from an elderly-onset-ascertained cohort (PMID:11815426) and directly contradicts the documented pediatric presentations. Per the dismech frequency-evidence SOP, **omit `frequency:` rather than fabricate justification** for most CMH7 phenotypes; the Orphanet HPO table (`ORPHA:` structured source) is a better-denominated alternative for the parent HCM entity.

2. **Scope decision: keep CMH7 separate from `TNNI3`-RCM and `TNNI3`-DCM, but cross-reference.** They have distinct MONDO/OMIM identities and distinct clinical management, yet share a gene, a mechanism (Ca²⁺ sensitization), and even individual variants (R145, D190). A `Grouping` over the `TNNI3` allelic series (`grouping_basis: [SHARED_GENE_FAMILY, SHARED_MECHANISM]`, `criteria_semantics: NECESSARY` with a `HAS_GENE` leaf on TNNI3) would capture this cleanly and is the natural home for the lump-vs-split reasoning.

3. **Module conformance opportunities.** CMH7 is a strong candidate conformer for **`cardiomyopathy_maladaptive_remodeling`** (`#Ventricular Remodeling`) and plausibly for **`fibrotic_response`** (the interstitial fibrosis arm). It is **not** a good fit for `cardiac_ion_channel_repolarization`, despite the arrhythmic phenotype — that module is scoped to structurally normal hearts with primary channel/Ca²⁺-handling variants, whereas CMH7's arrhythmia arises from a sarcomeric lesion with disarray. If the arrhythmia-without-hypertrophy finding in p.Arg21Cys carriers is curated, it should be a CMH7-local node, not a channelopathy-module conformance claim. There is a real gap here: no dismech module currently captures the **sarcomeric myofilament Ca²⁺-sensitization → impaired relaxation → energetic mismatch** chain, which recurs across thin-filament HCM (`TNNI3`, `TNNT2`, `TPM1`, `ACTC1`) and thin-filament RCM. **That is a well-justified new-module candidate** — consider the `create-module` skill.

4. **The most distinctive, entry-justifying claims** (rank these first in the pathophysiology narrative): (i) Ca²⁺ sensitization with *reduced* maximal force — mechanistically opposite to the `MYH7` hypercontractility paradigm, and a direct challenge to the assumption that myosin inhibitors are the right drug class here; (ii) SCD without hypertrophy in p.Arg21Cys carriers, with disarray only at autopsy — genotype may outperform imaging for risk stratification; (iii) the R21C loss of the PKA lusitropic switch as a clean gene–environment (adrenergic stress) interaction; (iv) `TNNI3` as the principal RCM gene and the resulting one-gene-three-cardiomyopathies allelic series; (v) `TNNI3` over-representation in both apical and elderly-onset HCM.

5. **Verbatim-quote status.** Five abstracts were retrieved with full verbatim text (Kimura 1997, Mogensen 2003, Niimura 2002, Wen 2008, Pua 2020, Olivotto 2020 — six, in fact). The remainder were summarized by an intermediary. **Every snippet must pass `just fetch-reference` + `just validate-references` before commit**; the paraphrased items in particular will fail substring matching as written here.

6. **Publisher access.** ahajournals.org, jacc.org, and omim.org all returned HTTP 403 during this session. PubMed (`pubmed.ncbi.nlm.nih.gov`), PMC, NCBI eutils, HPO's `ontology.jax.org` API, GTR, and `rest.uniprot.org` were all accessible. Route reference fetching through those.

---

**Sources:**
[OMIM #613690 CMH7](https://omim.org/entry/613690) · [OMIM *191044 TNNI3](https://omim.org/entry/191044) · [Kimura 1997, PMID:9241277](https://pubmed.ncbi.nlm.nih.gov/9241277/) · [Mogensen 2003, PMID:12531876](https://pubmed.ncbi.nlm.nih.gov/12531876/) · [Niimura 2002, PMID:11815426](https://pubmed.ncbi.nlm.nih.gov/11815426/) · [Wen 2008, PMID:18430738](https://pubmed.ncbi.nlm.nih.gov/18430738/) · [Wang 2012, PMID:22086914](https://pubmed.ncbi.nlm.nih.gov/22086914/) · [Coppini 2014, PMID:25524337](https://pubmed.ncbi.nlm.nih.gov/25524337/) · [Fahed 2020, PMC7676616](https://pmc.ncbi.nlm.nih.gov/articles/PMC7676616/) · [Pua 2020, PMID:32815737](https://pubmed.ncbi.nlm.nih.gov/?term=Genetic+Studies+of+Hypertrophic+Cardiomyopathy+in+Singaporeans) · [Olivotto 2020 EXPLORER-HCM, PMID:32871100](https://pubmed.ncbi.nlm.nih.gov/32871100/) · [Hespe 2025 ClinGen reappraisal, PMC11312670](https://pmc.ncbi.nlm.nih.gov/articles/PMC11312670/) · [ClinGen HCM gene validity](https://clinicalgenome.org/docs/genes-associated-with-hypertrophic-cardiomyopathy-a-reappraisal-by-the-clingen-hereditary-cardiovascular-disease-gene-curation/) · [ClinGen TNNI3 CSpec GN098](https://cspec.genome.network/cspec/ui/svi/doc/GN098) · [2024 AHA/ACC HCM Guideline, PMID:38718139](https://pubmed.ncbi.nlm.nih.gov/38718139/) · [UniProt P19429](https://rest.uniprot.org/uniprotkb/P19429.txt) · [HPO annotations OMIM:613690](https://ontology.jax.org/api/network/annotation/OMIM:613690) · [GTR Hypertrophic cardiomyopathy 7](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1860752/) · [Pediatric TNNI3 p.Ile195Phe, PMC10978967](https://pmc.ncbi.nlm.nih.gov/articles/PMC10978967/) · [Hasegawa 2024 EHT, PMC11457505](https://pmc.ncbi.nlm.nih.gov/articles/PMC11457505/) · [Norrish 2024, PMID:38296631](https://pubmed.ncbi.nlm.nih.gov/38296631/) · [Semsarian 2015, PMID:25814232](https://pubmed.ncbi.nlm.nih.gov/25814232/) · [OMIA:002951-9685 feline MYBPC3 HCM](https://omia.org/OMIA002951/9685/) · [OMIA:002212-9685 feline MYH7 HCM](https://omia.org/OMIA002212/9685/) · [Genetic Basis of HCM in Cats, PMC11352635](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11352635/) · [TNNI1/2/3 evolution & structure-function, PMC5798203](https://pmc.ncbi.nlm.nih.gov/articles/PMC5798203/) · [cTnI R145W human sarcomeres, PMC5076848](https://pmc.ncbi.nlm.nih.gov/articles/PMC5076848/) · [Infantile RCM cTnI-R170G/W, PMC7077804](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7077804/) · [Troponin RCM animal models review, PMC5165243](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5165243/) · [R21C knock-in LV/RV differences, PMC4415466](https://pmc.ncbi.nlm.nih.gov/articles/PMC4415466/) · [ClinVar TNNI3 pathogenic variants (ClinVar Miner)](https://clinvarminer.genetics.utah.edu/variants-by-condition/Hypertrophic%20cardiomyopathy/gene/TNNI3/pathogenic) · [Hypertrophic cardiomyopathy, Nat Rev Dis Primers 2025](https://www.nature.com/articles/s41572-025-00643-0)