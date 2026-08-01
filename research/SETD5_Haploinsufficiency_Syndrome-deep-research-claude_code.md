---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T18:25:52.306729'
end_time: '2026-07-31T18:46:42.041437'
duration_seconds: 1249.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SETD5 Haploinsufficiency Syndrome
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
  - claude-opus-5[1m]
  web_search_requests: 2
  num_turns: 78
  total_cost_usd: 7.2830945
  session_id: e58aedaf-1c1f-44cd-a337-584f147fc865
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SETD5 Haploinsufficiency Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SETD5 Haploinsufficiency Syndrome** covering all of the
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

# SETD5 Haploinsufficiency Syndrome — Comprehensive Research Report

**Prepared:** 2026-07-31 · **Target entity:** Intellectual disability–facial dysmorphism syndrome due to SETD5 haploinsufficiency (MRD23 / IDD23 / "SETD5 Disorder") · **Intended use:** dismech knowledge-base entry population

---

## ⚠️ Verification preamble (read before curating)

Three provenance caveats apply to everything below:

1. **Quote status.** Quotes marked **[CACHE-VERIFIED]** were read character-for-character from `references_cache/PMID_*.md` files already present in this worktree and are safe to use as evidence `snippet:` values. Quotes marked **[UNVERIFIED-QUOTE]** were extracted by a summarizing web-fetch layer; they are *probably* exact but **must be re-checked** with `just fetch-reference PMID:XXXX` + `just validate-references` before being committed as snippets.
2. **Ontology IDs.** Every HP/GO/CL/UBERON/CHEBI/NCIT term below is a *suggestion*. Two GO terms curators commonly reach for here are **obsolete** and must not be used: `GO:0010452` ("obsolete histone H3-K36 methylation") and `GO:0034968` ("obsolete histone lysine methylation") — both were deprecated as mis-namespaced BP terms. Confirmed-live alternatives are given in §6. Run `just validate-terms` on everything.
3. **Named Entity Confusion (NEC) risk — HIGH for this disease.** SETD5 sits in a naming minefield. Specifically:
   - **`ORPHA:435638` "Proximal 3p25.3 microdeletion syndrome" (MONDO:0018564) is a *different disease*** — an ID/epilepsy/stereotypic-hand-movement entity from a more proximal 3p25.3 interval, **not** the SETD5 critical region. Do not merge.
   - **`OMIM:615743` is the *gene* SETD5; `OMIM:615761` is the *phenotype* MRD23.** Easy to swap.
   - **KBG syndrome (ANKRD11) and Cornelia de Lange syndrome (NIPBL) are genuine clinical mimics** with real published SETD5 cases; literature retrieved under "KBG" or "CdLS" queries may or may not be about SETD5.
   - Much of the PubMed hit list for "SETD5" is **oncology** (PDAC, NSCLC, breast, glioma, colorectal), where SETD5 is *overexpressed/hyperactive* — the mechanistic opposite of the germline haploinsufficiency disorder. Do not cross-import mechanism.

---

## 1. Disease Information

### Overview

SETD5 haploinsufficiency syndrome is an autosomal dominant, essentially always *de novo*, neurodevelopmental chromatinopathy caused by heterozygous loss-of-function of *SETD5* at 3p25.3. It is defined by global developmental delay/intellectual disability, prominent speech and language impairment, hypotonia, feeding difficulties in infancy, a recognizable but non-specific facial gestalt (brachycephaly, high forehead, synophrys/full broad eyebrows, long tubular nose, upslanting palpebral fissures, low-set fleshy ears, thin upper lip, low anterior hairline), and a high burden of behavioral/psychiatric comorbidity (autism, ADHD, obsessive-compulsive features, hand flapping, stereotypies). Variable additional features include congenital heart defects, skeletal/limb anomalies (notably leg-length discrepancy), short stature, epilepsy, and a growing list of newly reported systemic associations.

It is the principal single-gene explanation for the classic **3p25 (3p–) microdeletion syndrome** phenotype: *SETD5* lies within the 124 kb critical interval and deletion versus intragenic LoF produce a largely overlapping presentation.

> "SETD5 lies within the critical interval for 3p25 microdeletion syndrome. The individuals with SETD5 mutations showed phenotypic similarity to those previously reported with a deletion in 3p25, and thus loss of SETD5 might be sufficient to account for many of the clinical features observed in this condition." — Grozeva et al. 2014, *Am J Hum Genet* (**PMID:24680889**) [UNVERIFIED-QUOTE]

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0014336` | Label: *intellectual disability-facial dysmorphism syndrome due to SETD5 haploinsufficiency* (verified via OLS4) |
| OMIM (phenotype) | `OMIM:615761` | Intellectual developmental disorder, autosomal dominant 23 (MRD23 / IDD23) |
| OMIM (gene) | `OMIM:615743` | SETD5 |
| Orphanet | `ORPHA:404440` | ⚠️ **Marked OBSOLETE** in the Orphadata 2025-12-09 snapshot (`references_cache/ORPHA_404440.md`); MONDO still xrefs it |
| UMLS | `C3810406` | |
| MedGen | `816736` | |
| DOID | `DOID:0070053` | |
| ClinGen GDV disease | `MONDO:0800439` | ⚠️ ClinGen curates the gene–disease pair against *syndromic complex neurodevelopmental disorder*, **not** MONDO:0014336 — a real identifier discrepancy worth recording |
| Related-but-distinct | `ORPHA:435638` / `MONDO:0018564` | Proximal 3p25.3 microdeletion syndrome (ICD-10 Q93.5, ICD-11 LD44.31) — **different entity** |
| ICD-10 | F79 / Q87.8 (syndrome); **Q93.5** for the deletion form | No dedicated code for MRD23 |
| ICD-11 | No dedicated code identified; deletion form maps to **LD44.31** | Treat as unresolved |

### Synonyms

- Intellectual developmental disorder, autosomal dominant 23 (IDD23)
- Mental retardation, autosomal dominant 23 (MRD23) — *historic/discouraged*
- Intellectual disability–facial dysmorphism syndrome due to SETD5 haploinsufficiency
- SETD5-related neurodevelopmental disorder / SETD5-related disorder / **SETD5 Disorder** (the term used by the National Brain Gene Registry)
- 3p25.3 microdeletion syndrome (SETD5-containing form) / 3p– syndrome critical-region phenotype

### Data provenance type — mixed

Both individual-patient and aggregated. Notably:
- **EHR/billing-code-derived:** the National Brain Gene Registry cohort explicitly validated 10 clinical features against **ICD-10 billing codes** vs. manual chart review (**PMID:40265665**) — a rare instance of EHR-derived phenotyping in this disorder.
- **Patient-reported/registry:** a 2026 Facebook support-group survey (n=51, 12 countries) (**PMID:42468298**).
- **Clinician-ascertained case series:** the 28-patient European multicenter cohort (**PMID:39603091**), Powis et al. diagnostic-exome cohort (**PMID:28881385**).
- **Aggregated resources:** HPO/OMIM annotations (currently derived from only ~7–9 individuals — see §3), ClinGen, ClinVar, DECIPHER, SFARI Gene.

---

## 2. Etiology

### Disease causal factors

Purely **genetic and monogenic**: heterozygous loss of function of *SETD5*, arising as either (a) an intragenic sequence variant (nonsense, frameshift, canonical splice) or (b) a copy-number deletion encompassing the gene (interstitial 3p25.3 microdeletion or larger 3p terminal deletion). Haploinsufficiency is the established mechanism — nonsense-mediated decay of the mutant transcript has been directly demonstrated:

> "CRISPR/Cas9 mutation modelling of the two intragenic variants demonstrated nonsense-mediated decay of the resulting transcripts, pointing to a loss-of-function (LoF) and haploinsufficiency as the common disease-causing mechanism of intragenic SETD5 sequence variants and SETD5-containing microdeletions." — Kuechler et al. 2015, *Eur J Hum Genet* (**PMID:25138099**) [UNVERIFIED-QUOTE]

**ClinGen dosage sensitivity:** Haploinsufficiency score **3 — "Sufficient Evidence for Haploinsufficiency"** (curated 2014-11-06); Triplosensitivity score **0 — No Evidence** (source: ClinGen Dosage Map, HGNC:25566). **ClinGen Gene-Disease Validity: DEFINITIVE**, autosomal dominant, Intellectual Disability and Autism GCEP, evaluated 2023-07-27.

### Genetic risk factors

- **Causal variant class:** LoF only. No convincing missense/GoF disease mechanism has been established.
- **Constraint:** SETD5 is among the most LoF-intolerant genes in the genome. ExAC **pLI = 0.9999996** (rank **259 / 18,225** genes); Sanders TADA score 0.0025 (rank **22 / 18,665**); EAGLE score 28.05 ("Strong"); **SFARI Gene score 1S** (High Confidence, Syndromic), 181 rare variants catalogued, 0 common variants (source: SFARI Gene, gene.sfari.org/database/human-gene/SETD5).
- **Genomics England PanelApp:** GREEN (diagnostic-grade) on *Intellectual disability*, *DDG2P*, *Fetal anomalies*, *Skeletal dysplasia*, and *Early onset or syndromic epilepsy*; AMBER on *Cerebral vascular malformations* and *Monogenic short stature*. All monoallelic.
- **Genetic background / "second hits":** rare variants in the genetic background modulate expressivity in this class of disorder (Pizzo et al. 2019, *Genet Med* 21:816–825). A functional two-hit study showed **SETD5 homologs synergistically interact with MOSMO homologs** in *Drosophila* and *X. laevis*, producing axon-outgrowth defects absent with single knockdown (**PMID:33819264**) [UNVERIFIED-QUOTE].

### Environmental risk factors

None established. Paternal age effects for *de novo* variants are plausible in principle (as for all *de novo* dominant disorders) but have not been demonstrated specifically for *SETD5*. No toxin, infectious, dietary, or occupational exposure has been implicated. **Not applicable / no data.**

### Protective factors

No protective genetic or environmental factors identified. **No data.**

However, the existence of **transmitting parents with mild or no phenotype** (see §9 Penetrance) implies unmeasured genetic or stochastic buffering. Powis et al. describe "an apparently unaffected carrier mother of an affected individual and a carrier mother with normal intelligence and affected twin sons" [CACHE-VERIFIED, **PMID:28881385**]. Mechanistic basis unknown — this is a genuine **knowledge gap**.

### Gene–environment interactions

No documented GxE for *SETD5*. One review positions SETD5 among NSPC-proliferation regulators that converge with teratogenic insults (Zika, valproate, metabolic stress) on shared cell-cycle control (**PMID:41283518**) — a *hypothesis-generating* convergence claim, not a demonstrated interaction. Curate as such if at all.

---

## 3. Phenotypes

### 3.1 Authoritative HPO annotation set (OMIM:615761, via ontology.jax.org)

⚠️ **Critical caveat for KB frequency curation:** the current HPO annotation frequencies for this disease derive from a *very small* seed cohort (denominators of 7, 9, or 2). Do **not** convert these fractions to HPO FrequencyEnum bands without acknowledging the tiny n. Prefer the larger cohorts in §3.2 for frequency claims.

**Inheritance:** HP:0000006 (Autosomal dominant inheritance)

| HPO ID | Phenotype | HPO frequency (n/N) |
|---|---|---|
| HP:0001263 | Global developmental delay | 7/7 |
| HP:0001249 | Intellectual disability | 7/7 |
| HP:0000750 | Delayed speech and language development | 8/9 |
| HP:0000729 | Autistic behavior | 5/7 |
| HP:0031936 | Delayed ability to walk | 2/2 |
| HP:0000722 | Compulsive behaviors | 3/7 |
| HP:0000369 | Low-set ears | 5/7 |
| HP:0000582 | Upslanted palpebral fissure | 5/7 |
| HP:0000664 | Synophrys | 5/7 |
| HP:0000219 | Thin upper lip vermilion | 5/7 |
| HP:0011968 | Feeding difficulties | 5/7 |
| HP:0000463 | Anteverted nares | 4/9 |
| HP:0000678 | Dental crowding | 3/7 |
| HP:0005280 | Depressed nasal bridge | 3/7 |
| HP:0000347 | Micrognathia | 3/7 |
| HP:0000248 | Brachycephaly | 3/7 |
| HP:0002307 | Drooling | 3/7 |
| HP:0000343 | Long philtrum | 2/2 |
| HP:0002714 | Downturned corners of mouth | 2/2 |
| HP:0000294 | Low anterior hairline | 2/2 |
| HP:0000414 | Bulbous nose | 2/2 |
| HP:0000431 | Wide nasal bridge | 2/2 |
| HP:0100559 | Lower limb asymmetry | 2/7 |
| HP:0003307 | Hyperlordosis | 2/7 |
| HP:0000960 | Sacral dimple | 2/7 |
| HP:0000494 | Downslanted palpebral fissures | 2/9 |
| HP:0000545 | Myopia | 1/2 |
| HP:0000483 | Astigmatism | 1/2 |
| HP:0009836 | Broad distal phalanx of finger | 1/2 |
| HP:0001852 | Sandal gap | 1/2 |
| HP:0000486 | Strabismus | 1/7 |
| HP:0000508 | Ptosis | 1/7 |
| HP:0100259 | Postaxial polydactyly | 1/7 |
| HP:0000348 | High forehead | 1/7 |
| HP:0003593 | Infantile onset | 2/2 |
| HP:0000319 | Smooth philtrum | (annotated, no frequency) |
| HP:0002650 | Scoliosis | (annotated, no frequency) |
| HP:0002808 | Kyphosis | (annotated, no frequency) |
| HP:0000047 | Hypospadias | (annotated, no frequency) |

### 3.2 Frequencies from larger, better-powered cohorts (preferred for curation)

**European multicenter neurological/psychiatric cohort, n = 28 (De Falco et al. 2025, PMID:39603091)** — 26 SNV, 2 CNV:

> "In our cohort neurological symptoms include hypotonia (39.2 %), hyperkinetic movement disorders including stereotypies and chorea (21.4 %) and gait abnormalities ranging from tip-toe or unsteady walking and alterations of fine motor skills (35.7 %). Epilepsy was present in about 14 % of patients, including different types of seizures as epileptic spasms, focal motor, and non-motor seizures. Concerning the cognitive phenotype, intellectual disability or global developmental delay depending on age, ranging from mild to severe, was present in 75 % of cohort, 21.4 % exhibit borderline intellectual functioning while an individual has a normal intelligence quotient. Other psychiatric comorbidities include autism, ADHD, psychotic disorder and other internalizing and externalizing symptoms." [CACHE-VERIFIED]

| Feature | Frequency | Suggested HP term |
|---|---|---|
| ID or GDD (mild→severe) | **75%** | HP:0001249 / HP:0001263 |
| Borderline intellectual functioning | 21.4% | HP:0006889 (*verify*) |
| Hypotonia | **39.2%** | HP:0001252 |
| Gait abnormality (tip-toe/unsteady, fine-motor) | **35.7%** | HP:0001288 |
| Hyperkinetic movement disorder (stereotypies, chorea) | **21.4%** | HP:0002072 (*verify*); stereotypy HP:0000733; chorea HP:0002072 |
| Epilepsy | **~14%** (spasms, focal motor, focal non-motor) | HP:0001250; epileptic spasms HP:0011097 |
| Autism, ADHD, psychotic disorder, internalizing/externalizing | present, unquantified | HP:0000729, HP:0007018, HP:0000709 |

**Facebook support-group survey, n = 51 respondents from 12 countries (Talaba et al. 2026, Pediatr Neurol, PMID:42468298)** — patient/caregiver-reported; 80% of affected individuals <18 years; **mean age at diagnosis 9.2 years**:

> "Common features included developmental delay (96%), hypotonia (78%), intellectual disability (75%), gait abnormality (59%), vision problems (51%), constipation (47%), and anxiety (47%). Potential novel findings included high pain tolerance (43%), persistent leg pain (31%), and joint pain (27%)." [CACHE-VERIFIED]

| Feature | Frequency | Suggested HP term |
|---|---|---|
| Developmental delay | **96%** | HP:0001263 |
| Hypotonia | **78%** | HP:0001252 |
| Intellectual disability | **75%** | HP:0001249 |
| Gait abnormality | **59%** | HP:0001288 |
| Vision problems | **51%** | HP:0000505 (*broad*) |
| Constipation | **47%** | HP:0002019 |
| Anxiety | **47%** | HP:0000739 |
| **High pain tolerance (novel)** | **43%** | HP:0007021 (Pain insensitivity — *verify*) |
| **Persistent leg pain (novel)** | **31%** | HP:0030838 (Limb pain — *verify*) |
| **Joint pain (novel)** | **27%** | HP:0002829 (Arthralgia) |

Note the striking discordance between HPO's hypotonia annotation (absent) and both cohorts (39–78%) — hypotonia is under-annotated in HPO for this disease and should be curated as **FREQUENT**.

**National Brain Gene Registry, n = 13, ages 2–37 y (Callahan et al. 2025, PMID:40265665):**

> "Participants in our cohort had features not previously reported, including brain and musculoskeletal abnormalities. One participant had cerebral palsy." [CACHE-VERIFIED]

### 3.3 Phenotypes by category

**Behavioral / psychiatric** (search: HPO, DSM-5)
- Autistic behavior / ASD (HP:0000729) — the most consistently reported comorbidity; SFARI 1S gene
- Obsessive-compulsive behavior with **hand flapping and ritualized behavior** (HP:0000722, HP:0100023 stereotypical hand wringing — *verify*) — Grozeva et al. 2014 called these "prominent features"
- ADHD (HP:0007018)
- Anxiety (HP:0000739) — 47%
- Psychotic disorder (HP:0000709) — reported in the De Falco cohort; notable and under-recognized
- Internalizing/externalizing symptoms
- *SETD5* also emerged in a whole-genome de-novo-mutation study of **obsessive-compulsive disorder** (Lin et al. 2022, *Sci Adv* 8:eabi6180)

**Neurological**
- Hypotonia; motor delay; delayed ability to walk (HP:0031936)
- Gait abnormality including toe-walking (HP:0040083 — *verify*)
- Hyperkinetic movement disorder: stereotypies, chorea
- Epilepsy (~14%): epileptic spasms, focal motor and focal non-motor seizures. A dedicated case report documents evolution to focal **and** generalized seizures in a 6-year-old (**PMID:40462669**) — "epilepsy may arise after SETD5 variants, with subtle clinical manifestations" [UNVERIFIED-QUOTE]
- Severe cerebral cortical dysplasia (HP:0002539) in one nonsense case with congenital diaphragmatic hernia (**PMID:28263952**)
- Cerebral palsy in 1/13 BGR participants
- **Moyamoya angiopathy** (HP:0011834 — *verify*) — a de novo *SETD5* variant identified among 39 MMA trios (**PMID:31474762**); adult-onset cerebrovascular pleiotropy. *Interpretive caution:* the paper's replication support was for CHD4/CNOT3, not SETD5 — curate as PARTIAL/emerging, not established.
- Drooling (HP:0002307)

**Speech / language**
- Delayed speech and language development (HP:0000750) — 8/9; among the most consistent features
- Receptive–expressive language disorder, speech disorder

**Craniofacial (the gestalt)** — from Grozeva 2014, verbatim description: brachycephaly; prominent high forehead with synophrys or "striking full and broad eyebrows"; long, thin, tubular nose; long, narrow upslanting palpebral fissures; large, fleshy low-set ears. Plus: low anterior hairline, thin upper lip vermilion, long/smooth philtrum, downturned corners of mouth, micrognathia, depressed/wide nasal bridge, bulbous nose, anteverted nares, dental crowding.

**Skeletal / musculoskeletal**
- **Leg-length discrepancy / lower limb asymmetry (HP:0100559)** — distinctive and repeatedly reported ("significant leg-length discrepancy... a frequent finding")
- Scoliosis (HP:0002650), kyphosis (HP:0002808), hyperlordosis (HP:0003307)
- Variable hand and skeletal abnormalities (Powis 2018)
- Broad distal phalanges, sandal gap, postaxial polydactyly (rare)
- **Bone fragility** — novel association (Anderson et al. 2021, *Clin Genet* 100:352–354, **PMID:34169511**); HP:0002659 (Increased susceptibility to fractures — *verify*)
- Vertebral fusion in the *Setd5* het mouse (IMPC) — worth a targeted look in humans

**Growth**
- Growth retardation / short stature (HP:0004322); a severe case at **−5.22 SDS** height with delayed bone age (**PMID:40869907**)
- PanelApp lists SETD5 (Amber) on the *Monogenic short stature* panel
- Feeding difficulties in infancy (HP:0011968) — 5/7

**Cardiac**
- Congenital heart defects: ASD, VSD (including ostium primum ASD detected prenatally, **PMID:41368699**), conotruncal/outflow-tract defects. Mouse *Setd5* haploinsufficiency produces **double outlet right ventricle and perimembranous VSD** (**PMID:34050709**), giving strong mechanistic corroboration.

**Ophthalmologic**
- Myopia, astigmatism, strabismus, ptosis; "vision problems" 51% in survey
- Ptosis was the presenting feature in a 10.1-Mb 3p25 terminal deletion (**PMID:28951171**)

**Gastrointestinal / genitourinary / other**
- Constipation (47%)
- Inguinal hernia; hypospadias (HP:0000047)
- Congenital diaphragmatic hernia (HP:0000776) — rare, one case
- **CAKUT** — machine-learning analysis of 515 clinical-exome cases "implicated ADNP and SETD5 genes as associated with increased CAKUT risk" (**PMID:40913078**) [UNVERIFIED-QUOTE]; emerging, low confidence
- **Congenital hypopituitarism** — variants in *SETD5* found in a CH cohort after mouse pituitary-malformation screening (**PMID:38822427**); emerging
- Aberrant blind-ending bronchus (single case, **PMID:28905509**)
- **Neuroblastoma** — one report expanding SETD5 haploinsufficiency into neuroblastoma (**PMID:32748512**). Curate cautiously: no cohort-level cancer-risk estimate exists; **there is currently no evidence base for tumor surveillance**.

### 3.4 Phenotype characteristics

- **Onset:** congenital to infantile (HP:0003593 Infantile onset annotated 2/2). Facial dysmorphism and CHD are congenital; hypotonia/feeding difficulty neonatal–infantile; DD apparent in the first 1–2 years; behavioral/psychiatric features school-age; epilepsy variable.
- **Severity:** highly variable — from normal IQ (1 individual in the 28-patient cohort) and borderline functioning (21.4%) through mild, moderate, to severe ID. Original series emphasized "moderate to severe ID."
- **Progression:** the core cognitive phenotype is **static/non-progressive** (a developmental, not neurodegenerative, disorder). Musculoskeletal features (scoliosis, leg-length discrepancy) and epilepsy may be progressive/emergent. Late-onset cerebrovascular (moyamoya) pleiotropy has been proposed, prompting the recommendation to "assess clinical complications into adulthood" (**PMID:31474762**).
- **Quality-of-life impact:** no EQ-5D/SF-36/PROMIS study exists for this disorder — **data gap**. The Facebook survey is the closest proxy: it documents caregiver-reported burden domains (feeding, gait, vision, constipation, anxiety, pain) and found that group participation "empowered families through shared experiences and information exchange" [CACHE-VERIFIED, PMID:42468298]. The mean 9.2-year diagnostic delay is itself a QoL-relevant finding.

---

## 4. Genetic / Molecular Information

### Causal gene

| Field | Value |
|---|---|
| Symbol | **SETD5** |
| HGNC | `HGNC:25566` (dismech form: `hgnc:25566`) |
| Approved name | SET domain containing 5 |
| Location | **3p25.3** |
| Entrez Gene | 55209 |
| Ensembl | ENSG00000168137 |
| UniProt | **Q9C0A6** |
| OMIM (gene) | 615743 |
| Aliases | FLJ10707, SETD5A, KIAA1757, 2900045N06Rik / mKIAA1757 (mouse) |
| Structure | **1,442 aa; 31 exons**; SET domain (degenerate, Set3/Set4 subfamily) + a predicted PHD-like region; NLS motif |
| Reference transcript | NM_001080517.3 (used in ClinVar/published nomenclature) |
| Expression | Ubiquitous; high in brain (cerebral cortex across developmental stages), thyroid, skin, ovary, lung, endometrium |

Source for structure/expression: Li et al. 2023 review (**PMID:36875494**), read from cached full text: *"The human SETD5 gene (OMIM 615743), also known as MRD23, SETD5A, 2900045N06Rik or mKIAA1757, is located on the chromosome 3p25.3 and encodes the SETD5 protein composed of 1442 amino acids... The SETD5 gene consists of 31 exons and is ubiquitously expressed in human tissues such as the brain, thyroid, skin, ovary, lung and endometrium."* [CACHE-VERIFIED]

### Pathogenic variants

**Variant classes observed (all LoF):** nonsense > frameshift > canonical splice-site > whole-gene/partial-gene deletion. No pathogenic missense mechanism established.

**Landmark allelic series — Grozeva et al. 2014 (PMID:24680889), 7 de novo LoF variants:**

| Variant (cDNA) | Protein | Type |
|---|---|---|
| c.1195A>T | p.Lys399* | nonsense |
| c.1333C>T | p.Arg445* | nonsense |
| c.1866C>G | p.Tyr622* | nonsense |
| c.3001C>T | p.Arg1001* | nonsense (in ClinVar, RCV000114962) |
| c.2177_2178del | p.Thr726Asnfs*39 | frameshift |
| c.3771dup | p.Ser1258Glufs*65 | frameshift |
| c.3856del | p.Ser1286Leufs*84 | frameshift |

**Additional published alleles:**
- c.3848_3849insC (Chr3:9,517,294 A>AC) — mild ID in a 36-year-old male (**PMID:28549204**)
- c.890_891delTT — severe short stature + overlap syndrome, rhGH-treated (**PMID:40869907**)
- NM_001080517.3:c.3601_3605del, p.Trp1201GlufsTer2 — de novo, prenatally ascertained via ostium primum ASD (**PMID:41368699**)
- Frameshift in exon 12 — ID + aberrant blind-ending bronchus (**PMID:28905509**)
- 81 bp deletion spanning a splice-donor site + a nonsense variant, both NMD-confirmed (**PMID:25138099**)
- SETD5<sup>S1257*</sup> — a *functional* truncation used experimentally: it abolishes HDAC3/PAF1 interaction and separates SETD5's proliferation function from its anti-apoptotic function (**PMID:36349512**)

**Variant classification distribution (National Brain Gene Registry, PMID:40265665):** of 11 unique P/LP variants in 13 individuals from 11 families — **6 nonsense, 4 frameshift, 1 splice site** [CACHE-VERIFIED].

**Allele frequency:** pathogenic SETD5 LoF alleles are absent/singleton in population databases; the gene is extremely LoF-depleted (**ExAC pLI 0.9999996**). No recurrent/founder allele has been described.

**Germline vs somatic:** disease alleles are **germline**, overwhelmingly **de novo**. *SETD5* is separately somatically altered/overexpressed in multiple cancers (PDAC, NSCLC, breast, ESCC, bladder amplification ~10%, high-grade glioma, ALL, prostate, colorectal, neuroblastoma) — **do not conflate** with the germline haploinsufficiency disorder.

**Functional consequence:** loss of function via NMD → 50% dosage → haploinsufficiency. No dominant-negative or GoF mechanism demonstrated for germline disease.

### Modifier genes

- No validated Mendelian modifier. Genetic-background rare-variant burden is the leading model (Pizzo 2019).
- **MOSMO** is a demonstrated genetic interactor in invertebrate/amphibian two-hit assays (**PMID:33819264**) — model-organism evidence only.
- **ANKRD11 is an upstream regulator of SETD5** (see §6), which reframes the KBG/SETD5 overlap as a *pathway* relationship rather than coincidental phenocopy.

### Epigenetic information

- **A validated DNA-methylation episignature exists for MRD23/SETD5.** SETD5 is in the EpiSign validated-disorder panel (EpiSign V2/V3 classifiers; ~25 reference samples reported for MRD23). Foundational methodology: Aref-Eshghi et al. 2020, *Am J Hum Genet* (**PMID:32109418**), "Evaluation of DNA Methylation Episignatures for Diagnosis and Phenotype Correlations in 42 Mendelian Neurodevelopmental Disorders" — *"This study more than doubles the number of published syndromes with DNA methylation episignatures."* [UNVERIFIED-QUOTE]; chromatinopathy application: Levy et al. 2022, *Genet Med* (**PMID:34906459**).
- A 2026 study of 400 NDD individuals confirmed episignature concordance for SETD5 among chromatinopathy genes and used EpiSign to reclassify VUS (**PMID:41957673**): *"26 individuals (43%) exhibited disorder-specific episignatures consistent with the associated clinical diagnosis"* [UNVERIFIED-QUOTE].
- The primary molecular lesion is itself epigenetic — see §6.

### Chromosomal abnormalities

- **3p25.3 interstitial microdeletions** encompassing *SETD5*: e.g., a **684 kb** deletion refining a **124 kb critical region containing only THUMPD3, SETD5, and LOC440944** (Kellogg et al. 2013, **PMID:23613140**); a **116 kb** deletion partially involving *SETD5* in a KBG-suspected patient (**PMID:32793091**); four independent de novo non-recurrent microdeletions (**PMID:25138099**).
- **3p terminal deletions (3p– syndrome)**, e.g., a de novo **10.1 Mb** 3p25 terminal deletion (**PMID:28951171**). Larger deletions add features not attributable to SETD5 alone (microcephaly, seizures, more severe cardiac disease) — the 684 kb case notably **lacked** cardiac defects, seizures, and microcephaly, supporting a contiguous-gene contribution in larger deletions.
- Detection: chromosomal microarray (aCGH/SNP array); DECIPHER and dbVar hold the CNV records.

---

## 5. Environmental Information

- **Environmental factors:** none identified. **Not applicable.**
- **Lifestyle factors:** none identified. **Not applicable.**
- **Infectious agents:** none. **Not applicable.**

The only environmental-adjacent literature is a general review noting that teratogens (Zika, valproate) can phenocopy NSPC-proliferation defects also produced by SETD5 loss (**PMID:41283518**) — a mechanistic convergence claim, not an etiologic factor for this disease.

---

## 6. Mechanism / Pathophysiology

### 6.1 The central unresolved question — is SETD5 a methyltransferase?

This is the single most important mechanistic controversy for this entry and should be curated explicitly as **competing `mechanistic_hypotheses`** rather than silently resolved.

**Hypothesis A — SETD5 is a genuine H3K36 methyltransferase (canonical/"catalytic" model).**
Sessa et al. 2019, *Neuron* (**PMID:31515109**):

> "Mutations in one SETD5 allele are genetic causes of intellectual disability and autistic spectrum disorders. However, the mechanisms by which SETD5 regulates brain development and function remain largely elusive. Herein, we found that Setd5 haploinsufficiency impairs the proliferative dynamics of neural progenitors and synaptic wiring of neurons, ultimately resulting in behavioral deficits in mice. Mechanistically, Setd5 inactivation in neural stem cells, zebrafish, and mice equally affects genome-wide levels of H3K36me3 on active gene bodies. Notably, we demonstrated that SETD5 directly deposits H3K36me3, which is essential to allow on-time RNA elongation dynamics. Hence, Setd5 gene loss leads to abnormal transcription, with impaired RNA maturation causing detrimental effects on gene integrity and splicing." [CACHE-VERIFIED]

**Hypothesis B — SETD5 is catalytically dead and acts as a co-repressor scaffold ("scaffold" model).**
Wang et al. 2020, *Cancer Cell* (**PMID:32442403**):

> "SETD5 lacks histone methyltransferase activity but scaffolds a co-repressor complex, including HDAC3 and G9a." [UNVERIFIED-QUOTE]

The 2023 review (**PMID:36875494**) states both positions and adds the enzymological detail [CACHE-VERIFIED from full text]:

> "SETD5 contains a SET (Su(var)3-9, enhancer-of-zeste, trithorax) domain and is thus annotated as a candidate protein of lysine methyltransferase, which methylates H3K36 up to the tri-methyl form (H3K36me3)... However, there is evidence that SETD5 lacks the methyltransferase activity but scaffolds a co-repressor complex, including HDAC3, NCoR, G9a, and PAF1, which couples selective deacetylation of H3K9ac with methylation of this residue."

And on subfamily context: *"The yeast SET3 and SET4, Drosophila UpSET, and human MLL5 are homologous to SETD5 over their SET domains and, except for SETD5, contain a PHD finger."* [CACHE-VERIFIED]

**Curation guidance:** model as two `hypothesis_group_id`s (e.g. `setd5_h3k36me3_catalytic` [EMERGING/CONTESTED] and `setd5_corepressor_scaffold` [EMERGING/CONTESTED]), with the downstream node "impaired RNA Pol II elongation and transcriptional fidelity" as a **convergent hub** that both hypotheses feed. Add a `discussions` entry with `kind: KNOWLEDGE_GAP` attached to the catalysis node.

### 6.2 Substrate/complex map (from PMID:36875494 Table 1, CACHE-VERIFIED)

| Complex | Substrate | Site | Effect |
|---|---|---|---|
| Unknown | Histone H3 | K36 (methylation) | Preservation of global transcriptional fidelity during brain development and neuronal wiring |
| G9a, HDAC3, NCoR1 | Histone H3 | K9 (methylation) | Promotes H3K9 methylation; enhances PDAC resistance to MEKi |
| HDAC3, NCoR, PAF1 | Histone H3 | K27 (deacetylation) | Recruits HDAC3/NCoR co-repressor; suppresses adipogenesis |
| HDAC3 | Histone H4 | K16 (deacetylation) | Elevates rDNA expression by removing H4K16ac/TIP5; promotes neural cell proliferation |

Additional partners: **PAF1 complex** (Ctr9), **NCoR/HDAC3**, **G9a/EHMT2**, **HCF-1**, **TBL1XR1**, **BRD2**, **OGT** (in cancer), **RNA Pol II**.

### 6.3 Causal chain — germline haploinsufficiency (proposed pathograph)

**Trigger (MOLECULAR):** Heterozygous *SETD5* LoF variant / 3p25.3 deletion → NMD → ~50% SETD5 protein
↓
**MOLECULAR:** Loss of SETD5-dependent chromatin state — reduced genome-wide H3K36me3 on active gene bodies (Hypothesis A) **and/or** failure of SETD5–NCoR/HDAC3/G9a/PAF1 co-repressor scaffolding with enhancer/promoter hyperacetylation (Hypothesis B). Osipovich et al. showed *Setd5*-deficient cells have **increased histone acetylation at transcription start sites and downstream regions** (**PMID:27864380**).
↓
**MOLECULAR:** Dysregulated RNA Pol II dynamics — altered promoter-proximal pausing/release (with **HCF-1** and PAF1; demonstrated on E2F target genes in HSCs, **PMID:34853439**), impaired elongation kinetics, and **defective RNA maturation, splicing, and gene integrity** (Sessa 2019).
↓ (parallel branch)
**MOLECULAR:** Reduced rDNA transcription — SETD5 normally recruits HDAC3 to the rDNA promoter, removing **H4K16ac** and its reader **TIP5** (a repressor of rDNA); SETD5 loss ⇒ rDNA repression ⇒ ↓ global translation ⇒ specifically **↓ cyclin D1 translation** (**PMID:32299058**).
↓
**CELLULAR:** Neural stem/progenitor cell proliferation defect and altered cell-cycle dynamics; premature/altered differentiation; deficit of **deep-layer cortical neurons** (**PMID:30655503**).
↓ (parallel branch)
**CELLULAR:** Mitochondrial compartment failure — *"Low levels of SETD5 resulted in fragmented mitochondria, reduced mitochondrial membrane potential"* and reduced ATP production, with mitochondria depleted from neurites and synapses; *"Mitochondrial impairment is facilitated by transcriptional aberrations originated by SETD5"* (**PMID:37264456**) [UNVERIFIED-QUOTE].
↓ (parallel branch, non-cell-autonomous)
**CELLULAR:** Astrocyte dysfunction — SETD5-deficient hiPSC-derived astrocytes show increased extracellular ROS, glutamate, IL-6 and IL-8; *"Elevated astrocytic IL-6 exerts a non-cell autonomous harmful effect on healthy neurons"*, driven by **JAK/STAT** (**PMID:41993368**, bioRxiv preprint 2026 — *preprint, not peer-reviewed; curate as EMERGING*) [UNVERIFIED-QUOTE].
↓
**CELLULAR/TISSUE:** Reduced synaptic density and neuritic outgrowth; decreased network activity and synchrony on MEA; abnormal postsynaptic density protein expression; **enhanced long-term potentiation** (a paradoxical/dissociated LTP finding worth flagging) (**PMID:30655503**, **PMID:30455454**).
↓ (developmental branch)
**TISSUE:** Neural crest–derived and cardiopharyngeal-mesoderm developmental defects → craniofacial dysmorphism and outflow-tract cardiac malformation. *"Setd5 was required in cardiopharyngeal mesoderm for progression of the heart tube"* through the ballooning stage (**PMID:34050709**) [UNVERIFIED-QUOTE]; Deliu et al. report *"neural crest defect-associated phenotypes"* [CACHE-VERIFIED].
↓
**ORGANISM:** Global developmental delay, intellectual disability, autism/ADHD/OCD, hypotonia, dysmorphism, CHD, skeletal anomalies.

### 6.4 Molecular pathways (KEGG/Reactome/GO framing)

- **Chromatin/transcription:** H3K36 methylation; H3K9 methylation (via G9a); H3K27/H3K9/H4K16 deacetylation (via NCoR-HDAC3); RNA Pol II pausing and elongation (PAF1, HCF-1); enhancer priming→activation transition
- **Ribosome biogenesis / translation:** rDNA transcription (RNA Pol I), TIP5/NoRC, cyclin D1 translational control
- **Cell cycle:** E2F target genes, cyclin D1, G1/S
- **PI3K–AKT(–mTOR):** implicated chiefly in the cancer literature (**PMID:37963940**, **PMID:35063407**); its relevance to the germline NDD is **unproven** — flag as a knowledge gap
- **JAK/STAT–IL-6:** astrocytic, preprint-stage
- **Semaphorin/axon guidance:** SetD5–BRD2 co-occupancy at the *Sema3a* promoter/TSS regulates Sema3A in retinal ganglion cells, **independent of the SET domain** (**PMID:29180574**) — a clean, published SET-domain-independent function
- **Protein turnover:** APC/C-mediated ubiquitin–proteasome degradation of SETD5 acts as a **molecular switch** for enhancer activation (**PMID:34857762**)

### 6.5 Suggested GO / CL / UBERON / CHEBI terms

**Molecular function (OLS-verified live):**
- `GO:0046975` — histone H3K36 methyltransferase activity ✅ verified
- `GO:0140955` — histone H3K36 trimethyltransferase activity ✅ verified
- `GO:0140003` — histone H3K36me3 reader activity ✅ verified

**❌ DO NOT USE (confirmed obsolete):** `GO:0010452`, `GO:0034968`.

**Biological process (suggested — all require OAK verification):**
- `GO:0006357` regulation of transcription by RNA polymerase II
- `GO:0032968` positive regulation of transcription elongation by RNA polymerase II
- `GO:0006338` chromatin remodeling
- `GO:0006360` transcription by RNA polymerase I *(rDNA branch)*
- `GO:0042254` ribosome biogenesis
- `GO:0006412` translation
- `GO:0000381` regulation of alternative mRNA splicing, via spliceosome
- `GO:0008283` cell population proliferation
- `GO:0021895` cerebral cortex neuron differentiation
- `GO:0007416` synapse assembly
- `GO:0000266` mitochondrial fission
- `GO:0014032` neural crest cell development
- `GO:0016575` histone deacetylation *(verify — this namespace was affected by the same GO cleanup)*

**Cell types (CL — verify each):**
- `CL:0000047` neuronal stem cell / `CL:0011020` neural progenitor cell — primary proliferative target
- `CL:0000679` glutamatergic neuron; deep-layer cortical projection neurons
- `CL:0000127` astrocyte — non-cell-autonomous IL-6 arm
- `CL:0000333` migratory cranial neural crest cell — craniofacial/cardiac
- `CL:0000604` retinal rod cell; `CL:0000636` Mueller cell — retinal survival/proliferation (**PMID:36349512**)
- `CL:0000037` hematopoietic stem cell — quiescence (**PMID:34853439**)
- `CL:0000115` endothelial cell — miR-126-5p/SetD5/Sema3A axis
- `CL:0000136` adipocyte — adipogenic enhancer switch

**Anatomy (UBERON — verify each):** see §7.

**Chemicals (CHEBI — verify each):**
- `CHEBI:15414` S-adenosyl-L-methionine (methyl donor cofactor)
- `CHEBI:8871` risperidone (zebrafish rescue)
- `CHEBI:15361` pyruvate / glycolytic intermediates *(cancer arm only)*

### 6.6 Molecular profiling

- **Transcriptomics:** RNA-seq of fetal *Setd5*<sup>+/−</sup> cortical neurons showed a **specific subpopulation** with altered neurodevelopmental gene expression (**PMID:30655503**); Setd5-null mESCs show "substantially altered gene expression" (**PMID:27864380**); adult zebrafish *setd5* brain shows "downregulation of genes encoding proteins involved in the synaptic structure and function" (**PMID:36613611**). Datasets in GEO under these accessions (specific GSE IDs not retrieved — **look up before citing**).
- **Epigenomics:** genome-wide H3K36me3 ChIP-seq (Sessa 2019); H3/H4 acetylation ChIP (Osipovich 2016); Pol II ChIP/pausing-index (Deliu 2018, Li 2022); blood DNA-methylation EPIC arrays for episignature.
- **Proteomics:** SETD5 interactome (PAF1/Ctr9, NCoR/HDAC3, TBL1XR1, G9a, HCF-1, BRD2) — mass-spec IP studies in Osipovich 2016, Deliu 2018, Wang 2020, Li 2022.
- **Metabolomics / lipidomics:** none for the germline disorder. Bioenergetic (ATP, ΔΨm) readouts only (**PMID:37264456**). **Data gap.**
- **Single-cell / spatial:** no published scRNA-seq or spatial transcriptomics of patient tissue. **Data gap.**
- **Functional genomics screens:** a scalable high-throughput neural-development platform assayed shared ASD-gene impact on cell fate/differentiation including SETD5 (cached as `PMID_35197626`). DepMap holds SETD5 dependency data for cancer lines.

---

## 7. Anatomical Structures Affected

**Organ level — primary**
- **Brain / central nervous system** — `UBERON:0000955` brain; `UBERON:0000956` cerebral cortex (deep layers particularly); `UBERON:0002336` corpus callosum (MRI abnormalities reported); `UBERON:0002037` cerebellum (ataxia/gait). Adult *Setd5*<sup>+/−</sup> mice show MRI-detectable anatomical differences and abnormal brain-to-body weight ratio.
- **Craniofacial skeleton** — `UBERON:0001474` bone element / `UBERON:0007811` craniocervical region; neural-crest-derived facial structures.

**Organ level — secondary / systemic**
- **Heart** — `UBERON:0000948`; specifically outflow tract `UBERON:0004145`, interventricular septum `UBERON:0002094`, interatrial septum `UBERON:0002085`
- **Skeleton / limbs** — `UBERON:0002101` limb; vertebral column `UBERON:0000955`→ use `UBERON:0002240` spinal column *(verify)*; asymmetric long-bone growth
- **Eye / retina** — `UBERON:0000966` retina
- **Pituitary gland** — `UBERON:0000007` (congenital hypopituitarism, emerging)
- **Kidney / urinary tract** — `UBERON:0002113` kidney (CAKUT, emerging)
- **GI tract** — `UBERON:0001155` colon (constipation)
- **Cerebral vasculature** — `UBERON:0001621`/`UBERON:0001627` cerebral artery (moyamoya, emerging)
- **Diaphragm** — `UBERON:0001103` (CDH, rare)
- **Lung/airway** — `UBERON:0002185` bronchus (single aberrant-bronchus case)

**Body systems:** nervous (dominant), cardiovascular, musculoskeletal, visual, endocrine, digestive, genitourinary.

**Tissue and cell level:** neuroepithelium/ventricular zone (proliferating NSPCs), cortical plate neurons, astroglia, cranial neural crest, cardiopharyngeal mesoderm, retinal photoreceptors and Müller glia, bone (fragility), hematopoietic compartment (mouse only).

**Subcellular level (GO CC — verify):**
- `GO:0005634` nucleus — principal localization; NLS-dependent
- `GO:0000785` chromatin
- `GO:0005730` nucleolus / rDNA promoter *(SETD5 acts on rDNA but is not itself nucleolar-resident in all reports)*
- `GO:0005739` mitochondrion — secondary, disease-relevant compartment (fragmentation, ΔΨm loss)
- `GO:0045202` synapse — reduced mitochondrial occupancy in mutant neurites/synapses
- `GO:0000502` proteasome complex — APC/C-mediated SETD5 turnover

**Localization/lateralization:** bilateral and symmetric. **Lower-limb asymmetry (leg-length discrepancy)** is the notable exception and is an asymmetric skeletal feature.

---

## 8. Temporal Development

**Onset**
- **Congenital:** facial dysmorphism, CHD (detectable on fetal cardiac ultrasound — **PMID:41368699**), CDH, structural brain anomalies
- **Neonatal–infantile:** hypotonia, feeding difficulties, drooling
- **Infancy/toddlerhood:** global developmental delay, delayed walking, delayed speech (HP:0003593 Infantile onset)
- **Childhood:** ID becomes quantifiable; autism/ADHD/OCD/stereotypies; epilepsy when present
- **Adolescence/adulthood:** scoliosis, short stature, psychiatric decompensation; rare late cerebrovascular events (moyamoya)
- **Onset pattern:** chronic, insidious, developmental

**Progression**
- **Core cognitive phenotype: static/non-progressive.** There is no evidence of neurodegeneration.
- **Progressive elements:** scoliosis/kyphosis, leg-length discrepancy, possibly bone fragility.
- **Episodic elements:** epilepsy (~14%); psychiatric exacerbations.
- **Duration:** chronic, lifelong. Oldest reported individuals: 37 years (BGR cohort), 36 years (case report), plus mildly affected transmitting parents into middle age.
- **Progression rate:** not formally quantified — **no natural-history study exists.** This is the single largest clinical-data gap.

**Patterns**
- **Remission:** none.
- **Critical periods:** (a) embryonic — neural tube closure, somitogenesis, cardiac ballooning, neural crest migration (mouse null lethal at **E10.5–11.5**); (b) fetal/early postnatal cortical neurogenesis (deep-layer neuron generation); (c) early childhood — the window for developmental/behavioral intervention; (d) growth — the case report of rhGH initiated at age 12 with +3.16 SDS gain in year 1 argues the pubertal window is actionable for the growth phenotype.
- **Diagnostic delay:** mean age at diagnosis **9.2 years** (survey, PMID:42468298) — an actionable health-services finding.

---

## 9. Inheritance and Population

### Epidemiology

- **No population prevalence or incidence estimate exists.** Orphanet's entry (ORPHA:404440) is obsolete and carries no prevalence class. For a dismech `Prevalence` record, the defensible values are `measure_type: CASES_IN_LITERATURE` and `prevalence_class: ULTRA_RARE` / `NOT_YET_DOCUMENTED`, with a `notes` field explaining why.
- **Cumulative reported cases:** *"The disorder was first described in 2014 with fewer than 75 reported cases in the literature to date"* (Talaba et al. 2026, **PMID:42468298**) [CACHE-VERIFIED]. That count predates the 28-patient De Falco cohort and the 13-person BGR cohort being fully absorbed into the literature tally, so ~120–150 published individuals is a reasonable 2026 estimate.
- **Diagnostic yield within ID cohorts — the best available "frequency" anchor: ~0.7%.** Two independent cohorts converge:
  - Grozeva 2014: 7 LoF variants in 996 individuals screened → *"rare de novo LoF mutations in SETD5 are a relatively frequent (0.7%) cause of ID"* (**PMID:24680889**) [UNVERIFIED-QUOTE]
  - Kuechler 2015: *"The present report of two SETD5 LoF variants in 301 patients demonstrates a prevalence of 0.7% and thus SETD5 variants as a relatively frequent cause of ID"* (**PMID:25138099**) [UNVERIFIED-QUOTE]

  ⚠️ Curate this carefully: **0.7% is a diagnostic yield within an ascertained moderate-to-severe ID cohort, not a population prevalence.** Do not enter it as `rate_per_100000`.

### Genetic epidemiology

- **Inheritance pattern:** autosomal dominant (`HP:0000006`). Overwhelmingly **de novo**.
- **Penetrance: incomplete/reduced.** This is well documented and clinically important for counseling:
  - Powis et al. 2018: *"We also present an apparently unaffected carrier mother of an affected individual and a carrier mother with normal intelligence and affected twin sons."* [CACHE-VERIFIED, **PMID:28881385**]
  - De Falco et al. 2025 explicitly describe the disorder as having *"incomplete penetrance"* [CACHE-VERIFIED, **PMID:39603091**]
  - Szczałuba et al. 2016 reported the first familial case: two siblings and their father, with *"the father demonstrated only mild intellectual impairment"* (**PMID:27375234**) [UNVERIFIED-QUOTE]
  - ⚠️ Note tension: Genomics England PanelApp records "complete penetrance" on the Intellectual disability panel. The published literature contradicts this. Curate **incomplete penetrance** and flag the discrepancy.
- **Expressivity: highly variable**, both between and within families — normal IQ through severe ID in the same series.
- **Genetic anticipation:** none (not a repeat-expansion disorder). **Not applicable.**
- **Germline mosaicism:** not specifically reported for SETD5, but recurrence in siblings of unaffected parents is theoretically possible; standard counseling caveat applies. **No data.**
- **Founder effects:** none identified. **No data.**
- **Consanguinity:** not relevant (dominant LoF). **Not applicable.**
- **Carrier frequency:** not applicable in the recessive sense; population LoF frequency is essentially zero (pLI ≈ 1).

### Population demographics

- **Affected populations:** no ancestry-specific enrichment reported. Cases published from Europe, North America, South America (Brazil), Asia (Japan, China, India), the Middle East, and 12 countries in the support-group survey. The India NDD cohort study (**PMID:38114583**) confirms presence in LMIC populations.
- **Geographic distribution:** worldwide; no endemic pattern; no variant-specific geography.
- **Sex ratio:** approximately 1:1; no sex bias reported. Autosomal.
- **Age distribution of ascertained individuals:** heavily pediatric — **80% under 18 years** in the survey cohort; BGR range 2–37 years. This reflects ascertainment bias (exome sequencing of children with DD), not true age distribution. **Adults are systematically under-ascertained** — a recognized gap.

---

## 10. Diagnostics

### Primary diagnostic modality: genomic sequencing

There is **no biochemical or imaging biomarker**; diagnosis is molecular.

**Recommended approach (in practical order):**
1. **Trio exome sequencing (WES)** or **genome sequencing (WGS)** — the highest-yield first-line test for unexplained GDD/ID with dysmorphism. Essentially every published SETD5 case was ascertained this way. Trio design is essential given the *de novo* mechanism.
2. **Chromosomal microarray (CMA)** — mandatory in parallel or first, since a meaningful minority of cases are 3p25.3 microdeletions or 3p terminal deletions that WES may miss (2/28 in the De Falco cohort were CNVs). Resolution matters: the smallest reported deletion is **116 kb**.
3. **Targeted NGS ID/NDD panels** — SETD5 is on all major panels; Genomics England PanelApp lists it GREEN on *Intellectual disability*, *DDG2P*, *Fetal anomalies*, *Skeletal dysplasia*, and *Early onset or syndromic epilepsy*.
4. **Single-gene SETD5 sequencing** — GTR test 582578 (sequence analysis, all coding exons, postnatal) exists but is rarely the right first test.
5. **DNA methylation episignature (EpiSign)** — a genuinely useful adjunct for this gene. SETD5/MRD23 has a **validated episignature** in the EpiSign classifier. Use cases: (a) reclassifying a SETD5 VUS; (b) resolving the KBG/CdLS/SETD5 differential; (c) NGS-negative cases with a compelling phenotype. Supporting evidence: **PMID:32109418**, **PMID:34906459**, **PMID:41957673**.
6. **Prenatal:** fetal cardiac ultrasound detecting ASD/VSD prompted prenatal WES yielding a de novo SETD5 frameshift (**PMID:41368699**) — *"Fetal cardiac ultrasound represents a valuable tool for early screening"* [UNVERIFIED-QUOTE].

**Not indicated / not applicable:** karyotyping (resolution far too low), FISH (unless confirming a known deletion), mtDNA testing, repeat-expansion testing.

### Supportive clinical evaluations (not diagnostic, but standard-of-care workup)

| Modality | Purpose | LOINC/term note |
|---|---|---|
| Brain MRI | Structural anomalies; cortical dysplasia; corpus callosum | The De Falco cohort explicitly collected MRI data and found no *distinctive* signature |
| EEG | Epilepsy/EEG abnormalities (~14% clinical epilepsy) | No pathognomonic pattern identified |
| Echocardiogram | ASD/VSD/outflow-tract defects | Baseline at diagnosis |
| Formal cognitive/adaptive testing | Quantify ID severity | e.g., Vineland, Bayley, WISC |
| ADOS-2 / ADI-R | Autism diagnosis | |
| Ophthalmology | Myopia, astigmatism, strabismus, ptosis | |
| Audiology / ABR | Mouse model shows abnormal auditory brainstem response — human data limited | |
| Skeletal survey / scoliosis series / leg-length radiographs | LLD, scoliosis, bone fragility | |
| Growth curve, bone age, GH axis | Short stature; possible hypopituitarism | |
| Renal ultrasound | CAKUT (emerging) | |

**Biomarkers:** none validated. **Data gap.** No FDA/BEST-listed biomarker.

**Biopsy/histopathology:** not indicated. The only pathology literature is the single case of severe cerebral cortical dysplasia (**PMID:28263952**).

### Clinical criteria and differential diagnosis

No consensus clinical diagnostic criteria exist (unlike CdLS or KBG). Diagnosis = pathogenic/likely pathogenic SETD5 LoF variant or deletion + compatible phenotype.

**Differential diagnosis (all are documented real-world misdiagnoses of SETD5 cases):**

| Condition | Gene | Distinguishing features / evidence |
|---|---|---|
| **KBG syndrome** | ANKRD11 | Macrodontia of upper central incisors is the KBG discriminator. **Three patients clinically suspected of KBG had SETD5 lesions** (**PMID:32793091**); another SETD5 child had "KBG syndrome-like appearance" (**PMID:35132768**). Mechanistically linked: **ANKRD11 upregulates SETD5** (see below). |
| **Cornelia de Lange syndrome** | NIPBL, SMC1A, SMC3, RAD21, HDAC8 | SETD5 identified among chromatin regulators in CdLS-overlap patients (**PMID:28120103**, **PMID:31337854**); SETD5 also appeared as a single-proband finding in a 105-family WGS study of mutation-negative CdLS (**PMID:40677927**) |
| **3p terminal deletion (3p–) syndrome** | contiguous genes | Larger deletions add microcephaly, more severe seizures/cardiac disease |
| **Proximal 3p25.3 microdeletion syndrome** | ORPHA:435638 | ⚠️ **Different locus/entity** — do not conflate |
| Other chromatinopathies | KMT2A (Wiedemann-Steiner), EP300/CREBBP (Rubinstein-Taybi), EHMT1 (Kleefstra), CHD8, KDM5C | Overlapping ID + dysmorphism + growth issues; episignature testing discriminates |
| Non-specific syndromic ID | many | |

**Mechanistic basis of the KBG overlap (important, recently resolved):** ANKRD11 (KBG) sits *upstream* of SETD5.
> "ANKRD11-deficient neural cells exhibit reduced ribosomal RNA (rRNA) and translation"; "it indirectly promotes rRNA expression by upregulating SETD5"; "ANKRD11 interacts with the Setd5 promoter and recruits WDR5"; "Overexpression of ANKRD11 or SETD5 restores rRNA levels and translational activity." — Ito et al. 2025, *iScience* (**PMID:40520101**) [UNVERIFIED-QUOTE]

This converts KBG↔SETD5 phenocopy from a clinical curiosity into a shared **ANKRD11→SETD5→rRNA/translation** axis and is high-value content for a dismech mechanism module.

### Screening

- **Newborn screening:** not applicable — no biochemical marker, no NBS program.
- **Carrier screening:** not applicable (de novo dominant).
- **Cascade screening:** appropriate. Because of documented reduced penetrance and mildly affected transmitting parents, **parental testing is mandatory** when a SETD5 variant is found — do not assume de novo.
- **Prenatal/PGT:** available for families with a known variant; PGT-M feasible.

---

## 11. Outcome / Prognosis

⚠️ **Prognosis for this disorder is essentially uncharacterized.** No natural-history study, no survival analysis, no registry-based outcome data. Everything below is inference from case series.

**Survival and mortality**
- **Life expectancy: no data.** No published deaths attributable to the syndrome; individuals reported into the fourth decade (36 y, 37 y) and mildly affected transmitting parents into middle age.
- Mortality risk, where present, would be driven by comorbidities: congenital heart disease, epilepsy (SUDEP risk applies generically), aspiration in severe hypotonia/feeding difficulty, and — in the rare moyamoya association — stroke.
- **Homozygous/biallelic loss is presumably not viable in humans**: the mouse null is embryonic lethal at E10.5–11.5 (**PMID:27864380**) and homozygous IMPC animals show "preweaning lethality, complete penetrance."
- **Disease-specific mortality: no data.**

**Morbidity and function**
- Lifelong ID in ~75% (mild→severe) plus 21% borderline; a minority with normal IQ.
- Communication impairment is near-universal and functionally dominant.
- Motor: 78% hypotonia, 59% gait abnormality; most walk, often late.
- Independence: not systematically studied. Most published adults required support. **Data gap.**
- **Quality-of-life instruments:** none applied. No EQ-5D, SF-36, PROMIS, or disease-specific PROM exists. **Priority gap.**

**Complications**
Epilepsy; scoliosis/kyphosis requiring orthopedic management; leg-length discrepancy; bone fragility/fractures; constipation; feeding difficulty and growth failure; refractive error and strabismus; psychiatric decompensation (including psychotic disorder); rare cerebrovascular events; single reports of neuroblastoma and hypopituitarism.

**Recovery potential:** none — the developmental lesion is fixed. Interventions are supportive and habilitative; developmental gains occur with therapy but the underlying dosage defect is not correctable with any current treatment.

**Prognostic factors**
- No validated prognostic model. Candidate factors, all unvalidated:
  - **Variant class/position** — De Falco et al. 2025 "conduct a comprehensive review of the available literature, suggesting a possible genotype-phenotype correlation" [CACHE-VERIFIED]. One case-report author speculated a 3'-terminal frameshift might retain partial activity, explaining a mild phenotype (**PMID:28549204**) — plausible but unproven.
  - **Deletion size** — larger 3p terminal deletions → more severe, additional features (microcephaly, seizures, cardiac).
  - **Genetic background / second hits** (Pizzo 2019).
  - Presence of epilepsy, CHD, or severe hypotonia at baseline.
- **Prognostic biomarkers:** none. **Data gap.**

---

## 12. Treatment

**There is no disease-modifying or targeted therapy.** Management is entirely symptomatic, multidisciplinary, and habilitative.

### Standard of care (all suggested NCIT terms require OAK verification)

| Intervention | Rationale | Suggested `treatment_term` (NCIT) | `therapeutic_modality` |
|---|---|---|---|
| Early intervention / developmental therapy | GDD in 96% | `NCIT:C15315` Rehabilitation | BEHAVIORAL |
| Speech and language therapy | Speech delay 8/9; near-universal | `NCIT:C159273` Speech Therapy | BEHAVIORAL |
| Physical therapy | Hypotonia 78%, gait 59% | `NCIT:C15302` Physical Therapy | BEHAVIORAL |
| Occupational therapy | Fine motor, ADLs | `NCIT:C121351` Occupational Therapy | BEHAVIORAL |
| Applied behavior analysis / ASD behavioral intervention | Autism | `NCIT:C181743` Behavioral Counseling *(verify)* | BEHAVIORAL |
| Special education / IEP | ID | `NCIT:C15747` Supportive Care | BEHAVIORAL |
| Genetic counseling | De novo mechanism, reduced penetrance, 50% transmission risk | `NCIT:C15240` Genetic Counseling | BEHAVIORAL |
| Antiseizure medication | Epilepsy ~14% | `NCIT:C15986` Pharmacotherapy | SMALL_MOLECULE |
| Psychotropics (SSRIs for anxiety/OCD; stimulants for ADHD; atypical antipsychotics e.g. risperidone/aripiprazole for irritability) | Anxiety 47%, ADHD, OCD, psychosis | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` per drug | SMALL_MOLECULE |
| Cardiac surgical repair | ASD/VSD/outflow tract | `NCIT:C15329` Surgical Procedure | SURGERY |
| Orthopedic management (scoliosis bracing/fusion; LLD epiphysiodesis/lengthening) | Scoliosis, leg-length discrepancy | `NCIT:C16186` Orthopedic Surgical Procedure | SURGERY |
| Feeding support / gastrostomy; constipation management | Feeding difficulty; constipation 47% | `NCIT:C15433` Nutritional Support *(do not auto-tag BEHAVIORAL — see CLAUDE.md)* | varies |
| Ophthalmologic correction | Refractive error 51% | `NCIT:C15747` Supportive Care / DEVICE | DEVICE |

### Disease-specific pharmacological reports

**Recombinant human growth hormone (rhGH)** — the only pharmacologic intervention with a published SETD5-specific outcome:
> "This is the first case of a patient with overlap syndrome due to SETD5 mutation treated with rhGH"; "After both one year (+3.16 SDS) and two years (+2.9 SDS), the growth rate significantly increased" (**PMID:40869907**, *Genes* 2025) [UNVERIFIED-QUOTE]

n = 1. Presented at −5.22 SDS height, bone age 3 years delayed, variant c.890_891delTT. Suggested annotation: `treatment_term` NCIT:C15986 Pharmacotherapy, `therapeutic_agent` somatropin (NCIT:C821 — *verify*), `therapeutic_modality: PROTEIN_REPLACEMENT` or `PEPTIDE`, evidence `HUMAN_CLINICAL`, and mark clearly as a single case report.

### Preclinical / experimental leads (none in human trials)

1. **Risperidone (CHEBI:8871)** — rescued the social-interest deficit in *setd5* heterozygous zebrafish: *"Impairment in social interest is rescued by risperidone, an antipsychotic drug used to treat behavioral traits in ASD"* (**PMID:36613611**) [UNVERIFIED-QUOTE]. `evidence_source: MODEL_ORGANISM`. Note this is a repurposed symptomatic agent, not disease-modifying.
2. **JAK/STAT inhibition** — in SETD5-deficient hiPSC astrocytes, *"Pharmacological JAK-STAT inhibition restored extracellular IL-6 to basal levels and partially rescued astrocyte morphology and neuronal deficits"* (**PMID:41993368**) [UNVERIFIED-QUOTE]. ⚠️ **bioRxiv preprint (2026), not peer-reviewed.** `evidence_source: IN_VITRO`, status EMERGING.
3. **Mitochondrial targeting** — the authors of **PMID:37264456** propose "mitochondrial activity and dynamics may represent new therapeutic targets," explicitly contingent on confirmation in patient-derived systems [UNVERIFIED-QUOTE]. `evidence_source: IN_VITRO`/`MODEL_ORGANISM`; hypothesis-stage.
4. **HDAC3 / epigenetic modulation** — mechanistically motivated by the SETD5–HDAC3–NCoR axis, but **no in vivo NDD rescue has been shown**. Directionality is non-obvious (SETD5 loss already de-represses acetylation). Curate only as a hypothesis with the direction problem flagged.
5. **ANKRD11/SETD5–rRNA axis** — overexpression of either restored rRNA/translation in KBG models (**PMID:40520101**); a conceptual, not clinical, lead.

### Clinical trials

**No interventional clinical trial specific to SETD5 haploinsufficiency was identified on ClinicalTrials.gov.** The relevant registries are observational:
- **National Brain Gene Registry (BGR)** — includes SETD5 Disorder participants; multi-site US (**PMID:38632549**, **PMID:40265665**). Look up its NCT/registry identifier before citing as a `clinical_trials` entry.
- Patient community: a SETD5-related disorder Facebook support group serving as an informal registry (**PMID:42468298**).

### Pharmacogenomics

No SETD5-specific pharmacogenomic guidance. Standard CPIC guidance applies to any psychotropic/antiseizure drugs used (e.g., CYP2D6 for risperidone/aripiprazole; HLA-B*15:02 for carbamazepine). **Not disease-specific.**

### Gene/RNA/cell therapy

None in development. Conceptually, a haploinsufficiency disorder with a 1,442-aa nuclear scaffold protein and a largely prenatal developmental critical window presents severe barriers to gene replacement or ASO-mediated upregulation. **No data.**

---

## 13. Prevention

**Primary prevention:** not possible. The disorder arises from *de novo* mutation; no modifiable exposure is known.

**Secondary prevention (early detection):**
- **Early genomic diagnosis** is the actionable target. Mean age at diagnosis is **9.2 years** — a substantial, reducible delay. First-tier trio WES/WGS + CMA in unexplained GDD/ID would compress this.
- **Prenatal detection** via fetal cardiac ultrasound → prenatal WES has been demonstrated (**PMID:41368699**).
- No population screening program is applicable.

**Tertiary prevention (complication prevention in diagnosed individuals):** — this is where prevention effort actually lives. Note that **no formal surveillance guideline exists for SETD5**; the list below is a reasoned synthesis of reported complications, not a published protocol, and should be curated as such.
- Baseline echocardiogram at diagnosis
- EEG if paroxysmal events; low threshold given ~14% epilepsy with subtle presentations
- Serial scoliosis and leg-length assessment through growth
- Bone health assessment given the reported fragility association
- Growth monitoring; GH-axis evaluation for significant short stature
- Ophthalmology and audiology baseline plus periodic re-evaluation
- Nutrition/GI review (feeding, constipation)
- Proactive psychiatric screening (anxiety 47%; psychotic disorder reported)
- Renal ultrasound is *reasonable but unproven* given the emerging CAKUT signal
- **No cancer surveillance is recommended** — the neuroblastoma link rests on a single report with no risk estimate

**Immunization:** routine schedule; no contraindication or special schedule. **Not applicable as disease-specific prevention.**

**Genetic screening / counseling:**
- **Parental testing is required** in every case — reduced penetrance means an apparently unaffected parent may carry the variant (**PMID:28881385**).
- Recurrence risk: ~1% (gonadal mosaicism) if both parents test negative; **50%** if a parent is a carrier, with the crucial caveat that severity is unpredictable.
- Prenatal diagnosis and PGT-M available for known familial variants.
- Suggested term: `NCIT:C15240` Genetic Counseling.

**Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease in other species:** **none reported.** No OMIA entry for a natural SETD5-related disorder in any domestic or wild species. All animal disease is experimentally induced. **Not applicable.**
- **Zoonotic potential / cross-species transmission:** **not applicable** (non-infectious genetic disorder).
- **Veterinary relevance:** none.

### Orthologs and evolutionary conservation

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | SETD5 (Entrez 55209) | |
| *Mus musculus* | NCBITaxon:10090 | **Setd5** (MGI:1920145) | Highly conserved; null lethal E10.5–11.5 |
| *Danio rerio* | NCBITaxon:7955 | **setd5** | ASD-like social phenotypes in het CRISPR mutants (**PMID:36613611**) |
| *Drosophila melanogaster* | NCBITaxon:7227 | **UpSET** | Functional homolog; recruits HDAC complexes, restricts chromatin accessibility/acetylation at promoters (Rincon-Arano et al. 2012, *Cell* 151:1214–1228) |
| *Saccharomyces cerevisiae* | NCBITaxon:4932 | **SET3**, **SET4** | Set3/Set4 SET-domain subfamily; Set4 promotes survival in oxidative stress (**PMID:30523388**) |
| *Xenopus laevis* | NCBITaxon:8355 | setd5 | Two-hit interaction study (**PMID:33819264**) |
| *Kryptolebias marmoratus* | NCBITaxon:37003 | Setd5 | Kmt family survey; gastrula-stage expression peak (**PMID:30458291**) |
| Human paralog | — | **MLL5 / KMT2E** | Same SET-domain subfamily; MLL5 retains a PHD finger that SETD5 lacks |

**Comparative pathology:** the *Setd5*<sup>+/−</sup> mouse recapitulates the human disorder's neural-crest/craniofacial, cardiac, cognitive, and behavioral axes remarkably well (see §15). Conservation extends to the biochemical mechanism: *"SETD5 functions in a manner similar to yeast Set3p and Drosophila UpSET"* (**PMID:27864380**) [UNVERIFIED-QUOTE] — i.e., the HDAC-recruiting, acetylation-restricting function is conserved from yeast to human, which is strong support for Hypothesis B (§6.1).

---

## 15. Model Organisms

### 15.1 Mouse — the primary model

**Alleles/resources:**
- `Setd5<tm1a(EUCOMM)Wtsi>` — knockout-first conditional-ready; IMPC/KOMP/EUCOMM. MGI:1920145. Available via IMSR/EMMA/MMRRC.
- Conditional (floxed) alleles used for cardiopharyngeal mesoderm–specific deletion (**PMID:34050709**)
- Independent lab-generated *Setd5*<sup>+/−</sup> lines: Osipovich/Magnuson (Vanderbilt), Deliu/Novarino (IST Austria), Moore/Muotri-adjacent (**PMID:30655503**), Sessa/Broccoli (San Raffaele), Nakagawa (Tohoku)

**Homozygous null:** embryonic lethal **E10.5–11.5**, with *"severe defects in neural tube formation, somitogenesis and cardiac development"* and aberrant vasculogenesis in embryo, yolk sac, and placenta (**PMID:27864380**). IMPC: "Preweaning lethality, complete penetrance."

**Heterozygous — IMPC systematic phenotyping** (`Setd5<tm1a(EUCOMM)Wtsi>`, het):

| MP phenotype | p-value |
|---|---|
| Abnormal snout morphology | 8.23E-11 |
| Abnormal cranium morphology | 6.16E-10 |
| Abnormal coat/hair pigmentation | 3.22E-09 |
| Abnormal maxilla morphology | 6.47E-07 |
| Abnormal tooth morphology | 3.90E-06 |
| Abnormal incisor morphology | 6.43E-06 |
| Absent pinna reflex | 9.77E-06 |
| Abnormal auditory brainstem response | 2.89E-05 – 3.64E-05 |
| Vertebral fusion | 3.92E-05 |
| Decreased grip strength | 7.49E-05 |
| Decreased circulating glucose level | 6.99E-05 |
| Increased regulatory T cell number | ~0 |
| Increased monocyte cell number | ~0 |

*Note the strong craniofacial/dental signal* — an excellent cross-species match to the human facial gestalt and dental crowding, and a hint that **hearing (ABR) and dentition deserve more systematic human assessment**.

**Heterozygous — hypothesis-driven studies:**

*Deliu et al. 2018, Nat Neurosci (**PMID:30455454**)* [CACHE-VERIFIED]:
> "Setd5-haploinsufficient mice present developmental defects such as abnormal brain-to-body weight ratios and neural crest defect-associated phenotypes. Furthermore, Setd5-mutant mice show impairments in cognitive tasks, enhanced long-term potentiation, delayed ontogenetic profile of ultrasonic vocalization, and behavioral inflexibility. Behavioral issues are accompanied by abnormal expression of postsynaptic density proteins previously associated with cognition. Our data additionally indicate that Setd5 regulates RNA polymerase II dynamics and gene transcription via its interaction with the Hdac3 and Paf1 complexes."

*Moore et al. 2019, Transl Psychiatry (**PMID:30655503**)*: reduced synaptic density and neuritic outgrowth in cultured cortical neurons; reduced MEA network activity and synchrony; altered gene expression in a fetal cortical neuron subpopulation; hyperactivity, cognitive deficit, altered social interaction; MRI-detectable adult brain differences; **deficit of deep-layer cortical neurons** in the developing brain; described as *"consistent with a highly penetrant risk factor."*

*Sessa et al. 2019, Neuron (**PMID:31515109**)*: impaired NPC proliferative dynamics and synaptic wiring; genome-wide H3K36me3 loss; behavioral deficits.

*Cheung et al. 2021, Genesis (**PMID:34050709**)*: **double outlet right ventricle + perimembranous VSD**; conditional deletion localizes requirement to cardiopharyngeal mesoderm; **no genetic interaction with Tbx1**.

*Nakagawa et al. 2020, iScience (**PMID:32299058**)*: *Setd5*<sup>+/−</sup> mice show autism-related behaviors with disturbed ribosomal protein gene and rDNA expression in brain.

*Li et al. 2022, Leukemia (**PMID:34853439**)*: hematopoietic-specific deletion → increased immunophenotypic HSCs, impaired long-term self-renewal, loss of LT-HSC quiescence via HCF-1/PAF1-dependent Pol II pause release on E2F targets.

*Matsumura et al. 2021, Nat Commun (**PMID:34857762**)*: SETD5–NCoR-HDAC3 gates Cebpa/Pparg enhancers; APC/C-mediated SETD5 degradation is the adipogenic switch.

**Phenotype recapitulation — strong.** The mouse het reproduces: craniofacial/neural-crest dysmorphology, outflow-tract cardiac defects, cognitive deficits, social/communication deficits (USV), behavioral inflexibility (an OCD/rigidity analog), reduced grip strength (hypotonia analog), vertebral anomalies, and the core molecular lesion.

**Model limitations:** (a) no reported spontaneous seizures despite human epilepsy in ~14%; (b) **enhanced** LTP in mice is hard to map onto human cognition; (c) mouse cortex lacks human-specific outer radial glia/OSVZ biology relevant to an NSPC-proliferation disorder; (d) no leg-length-discrepancy analog; (e) the human catalytic-activity question is not resolved by the mouse.

> **Curation note:** limitation (c) — and more broadly the question of whether murine NSPC proliferation phenotypes translate to human corticogenesis — is a textbook case for `discussions` with `kind: HUMAN_MODEL_MISMATCH` rather than generic `KNOWLEDGE_GAP`, since the evidence *exists* in the model and it is the translational validity that is open.

### 15.2 Zebrafish

*setd5* CRISPR/Cas9 heterozygous mutants (**PMID:36613611**): defective aggregation and shoaling coordination, indifference to social stimuli; adult-brain downregulation of synaptic structure/function genes suggesting hypo-connectivity; **risperidone rescues social interest**. Positioned as "a promising setd5 haploinsufficiency model" for drug screening. Also used to confirm H3K36me3 loss (Sessa 2019). ZFIN is the resource database.

### 15.3 Invertebrate / amphibian

*Drosophila* **UpSET** and *X. laevis* setd5 (**PMID:33819264**): two-hit interaction platform; SETD5–MOSMO synergy producing axon-outgrowth defects. Databases: FlyBase, Xenbase.

### 15.4 Cellular / in vitro

- **Mouse ESCs** — reduced proliferation, increased apoptosis, impaired cell-cycle progression and cardiomyocyte differentiation (**PMID:27864380**); required for primordial-germ-cell specification genes via Tbl1xr1/Ctr9 (Yu et al. 2017, *Cell Biochem Funct* 35:247–253)
- **Neural stem cells** — H3K36me3 and RNA-elongation phenotypes (Sessa 2019)
- **hiPSC-derived neurons and astrocytes** — mitochondrial phenotypes (**PMID:37264456**); astrocyte IL-6/JAK-STAT (**PMID:41993368**, preprint)
- **Mouse retinal explants + shRNA** — Setd5, not Setd2, required for retinal cell survival/proliferation; SET-domain-dependent; the SETD5<sup>S1257*</sup> separation-of-function allele (**PMID:36349512**)
- **High-throughput neural-development platform** profiling shared ASD-gene impact on cell fate/differentiation (cached `PMID_35197626`)

### 15.5 Model databases

MGI (MGI:1920145), IMPC, IMSR, EuMMCR/EUCOMM, KOMP, EMMA, MMRRC, ZFIN, FlyBase, Xenbase, Alliance of Genome Resources, DepMap (cancer dependency), Cellosaurus.

---

## Summary of high-priority knowledge gaps (candidates for `discussions:` entries)

| Gap | Kind | Attaches to |
|---|---|---|
| Is SETD5 catalytically active as an H3K36 methyltransferase, or a catalytically dead co-repressor scaffold? | KNOWLEDGE_GAP + competing `mechanistic_hypotheses` | the H3K36me3 deposition node |
| Mechanism of reduced penetrance / unaffected carrier parents | KNOWLEDGE_GAP | disease-level |
| No natural-history study; no survival, functional-outcome, or QoL data | KNOWLEDGE_GAP | disease-level |
| No population prevalence estimate (Orphanet entry obsolete) | KNOWLEDGE_GAP | `prevalence` |
| Mouse NSPC-proliferation phenotypes vs. human OSVZ/oRG corticogenesis | **HUMAN_MODEL_MISMATCH** | NSPC proliferation node |
| Mouse het shows no seizures despite ~14% human epilepsy | **HUMAN_MODEL_MISMATCH** | epilepsy node |
| Mitochondrial phenotype unconfirmed in patient-derived tissue (authors' own caveat) | **HUMAN_MODEL_MISMATCH** | mitochondrial dysfunction node |
| Astrocytic IL-6/JAK-STAT arm rests on a non-peer-reviewed 2026 preprint | KNOWLEDGE_GAP | astrocyte node |
| PI3K-AKT/mTOR relevance is cancer-derived; unproven in germline NDD | KNOWLEDGE_GAP | signaling node |
| Neuroblastoma / CAKUT / hypopituitarism / moyamoya associations lack risk estimates; no surveillance evidence | KNOWLEDGE_GAP | respective phenotype nodes |
| ClinGen curates the gene–disease pair against MONDO:0800439, not MONDO:0014336 | identifier discrepancy | `mappings` |
| PanelApp states "complete penetrance"; literature says incomplete | evidence conflict | `inheritance` |

---

## Key reference list (with cache status)

| PMID | Short citation | Cached in repo? |
|---|---|---|
| 24680889 | Grozeva 2014, *Am J Hum Genet* — founding LoF series, 7 variants, 0.7% | ✅ |
| 25138099 | Kuechler 2015, *Eur J Hum Genet* — WES + NMD proof of haploinsufficiency | ✅ |
| 23613140 | Kellogg 2013, *AJMG A* — 684 kb del, 124 kb critical region | ✗ |
| 28881385 | Powis 2018, *Clin Genet* — reduced penetrance, phenotype expansion | ✅ |
| 27375234 | Szczałuba 2016, *AJMG A* — first familial case | ✗ |
| 39603091 | De Falco 2025, *Eur J Paediatr Neurol* — 28-patient neuro/psych cohort | ✅ |
| 40265665 | Callahan 2025, *Clin Genet* — Brain Gene Registry, n=13 | ✅ |
| 42468298 | Talaba 2026, *Pediatr Neurol* — Facebook survey, n=51 | ✅ |
| 36335838 | Sveden/… 2023, *Pediatr Neurol* — genotype/phenotype expansion | ✅ (abstract absent in cache) |
| 32793091 | Crippa 2020, *Front Neurol* — SETD5 in suspected KBG | ✅ |
| 34169511 | Anderson 2021, *Clin Genet* — bone fragility | ✗ |
| 31474762 | Pinard 2020, *Genet Med* — moyamoya pleiotropy | ✅ |
| 27864380 | Osipovich 2016, *Development* — null lethality, PAF1/NCoR-HDAC3 | ✗ |
| 30455454 | Deliu 2018, *Nat Neurosci* — het mouse, Pol II/Hdac3/Paf1 | ✅ |
| 31515109 | Sessa 2019, *Neuron* — H3K36me3 deposition, RNA elongation | ✅ |
| 30655503 | Moore 2019, *Transl Psychiatry* — network connectivity, ASD behaviors | ✅ |
| 32299058 | Nakagawa 2020, *iScience* — rDNA/HDAC3/H4K16ac/TIP5/cyclin D1 | ✅ |
| 32442403 | Wang 2020, *Cancer Cell* — "SETD5 lacks HMT activity" scaffold model | ✗ |
| 34857762 | Matsumura 2021, *Nat Commun* — NCoR-HDAC3, APC/C switch | ✗ |
| 34853439 | Li 2022, *Leukemia* — Pol II pausing, HCF-1, HSC | ✅ |
| 37264456 | 2023, *Mol Autism* — mitochondrial compartment | ✅ |
| 36875494 | Li 2023, *Front Endocrinol* — SETD5 structure/activity review (full text cached) | ✅ |
| 40520101 | 2025, *iScience* — ANKRD11→SETD5→rRNA axis | ✗ |
| 34050709 | Cheung 2021, *Genesis* — cardiopharyngeal mesoderm, DORV/VSD | ✗ |
| 36613611 | 2022, *IJMS* — zebrafish setd5, risperidone rescue | ✗ |
| 36349512 | 2023, *FEBS Lett* — retina, Setd5 vs Setd2, S1257* allele | ✗ |
| 33819264 | Pizzo 2021, *PLoS Genet* — two-hit, SETD5×MOSMO | ✗ |
| 29180574 | Villain 2018, *Development* — SetD5/BRD2/Sema3A | ✗ |
| 41993368 | 2026 bioRxiv — astrocyte IL-6/JAK-STAT ⚠️ preprint | ✗ |
| 32109418 | Aref-Eshghi 2020, *AJHG* — 42-disorder episignatures | ✗ |
| 34906459 | Levy 2022, *Genet Med* — chromatinopathy episignatures | ✗ |
| 41957673 | 2026, *Clin Epigenetics* — 400 NDD, EpiSign, SETD5 concordance | ✗ |
| 40869907 | 2025, *Genes* — rhGH in SETD5 overlap syndrome | ✗ |
| 41368699 | 2025, *Birth Defects Res* — prenatal ASD → de novo SETD5 | ✗ |
| 40462669 | 2025, *J Child Neurol* — novel epilepsy phenotype | ✗ |
| 28263952 | Rawlins 2017, *Clin Dysmorphol* — CDH + cortical dysplasia | ✗ |
| 28951171 | Yagasaki 2018, *Pediatr Neonatol* — 10.1 Mb 3p25 del, ptosis | ✗ |
| 28905509 | 2017, *AJMG A* — aberrant blind-ending bronchus | ✗ |
| 28549204 | 2017, *Genet Mol Res* — mild ID, 36-year-old | ✗ |
| 28120103 | Parenti 2017, *Hum Genet* — CdLS-overlap chromatin regulators | ✅ |
| 32748512 | Pires 2020, *Pediatr Blood Cancer* — neuroblastoma | ✅ (abstract absent) |
| 40913078 | 2025, *EJHG* — CAKUT+ clinical exome, SETD5 signal | ✗ |
| 38822427 | 2024, *Genome Med* — pituitary malformation screen, SETD5 in CH | ✗ |
| 35132768 | Pascolini 2022, *AJMG A* — KBG-like appearance | ✗ |

**Non-PubMed sources used:** ClinGen (search.clinicalgenome.org, gene HGNC:25566 — GDV Definitive 2023-07-27; dosage HI=3/TS=0, 2014-11-06); HGNC REST (rest.genenames.org); EBI OLS4 (MONDO:0014336, GO term verification); HPO/Jax annotation API (ontology.jax.org, OMIM:615761); IMPC solr (Setd5 genotype-phenotype, MGI:1920145); SFARI Gene (gene.sfari.org); Genomics England PanelApp API; Orphadata 2025-12-09 snapshot via `references_cache/ORPHA_404440.md` and `ORPHA_435638.md`.

---

**Sources:**
- [PubMed E-utilities (esearch/efetch)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)
- [ClinGen — SETD5 (HGNC:25566)](https://search.clinicalgenome.org/kb/genes/HGNC:25566)
- [HGNC REST — SETD5](https://rest.genenames.org/fetch/symbol/SETD5)
- [EBI OLS4 — MONDO:0014336](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014336)
- [HPO annotations — OMIM:615761](https://ontology.jax.org/api/network/annotation/OMIM:615761)
- [IMPC — Setd5 phenotypes](https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Setd5)
- [SFARI Gene — SETD5](https://gene.sfari.org/database/human-gene/SETD5)
- [Genomics England PanelApp — SETD5](https://panelapp.genomicsengland.co.uk/api/v1/genes/SETD5/)
- [ClinVar RCV000114962 — SETD5 c.3001C>T](https://www.ncbi.nlm.nih.gov/clinvar/RCV000114962/)
- [GTR — Intellectual disability-facial dysmorphism syndrome due to SETD5 haploinsufficiency](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3810406/)
- [Kuechler et al. 2015, Eur J Hum Genet](https://www.nature.com/articles/ejhg2014165)
- [Crippa et al. 2020, Front Neurol (PMC7393934)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7393934/)
- [GARD — Intellectual disability-facial dysmorphism syndrome due to SETD5 haploinsufficiency](https://rarediseases.info.nih.gov/diseases/17673/intellectual-disability-facial-dysmorphism-syndrome-due-to-setd5-haploinsufficiency)
- [Levy et al., DNA methylation episignature testing improves molecular diagnosis of Mendelian chromatinopathies](https://www.gimjournal.org/article/S1098-3600(21)01121-7/fulltext)
- [EpiSign v5 methylation array panel content](https://mft.nhs.uk/app/uploads/2023/08/Methylation-Array-Panel-content-for-EpiSign.pdf)