---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:11.321916'
end_time: '2026-10-14T15:52:35.391343'
duration_seconds: 204.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: neurodevelopmental disorder with facial dysmorphism, absent language,
    and pseudo-pelger-huet anomaly
  mondo_id: MONDO:0859298
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
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 15
  total_cost_usd: 2.2361853999999997
  session_id: 7993bdd0-76b6-44d1-9419-f5a5fbbe7f89
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** neurodevelopmental disorder with facial dysmorphism, absent language, and pseudo-pelger-huet anomaly
- **MONDO ID:** MONDO:0859298 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **neurodevelopmental disorder with facial dysmorphism, absent language, and pseudo-pelger-huet anomaly** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'm checking the local reference cache for TMEM147 papers before I write the report.

# Research Report: Neurodevelopmental disorder with facial dysmorphism, absent language, and pseudo-Pelger-Huët anomaly (TMEM147-related disorder)

**MONDO:0859298 · OMIM #620075 · Gene: TMEM147 (hgnc:30414), 19q13.12**

**How this was researched.** The main sources are the founding cohort paper (Thomas et al., *Am J Hum Genet* 2022, PMID:36044892) and the later family report (Ghorashi et al., *Neurogenetics* 2023, PMID:37668766). I also used the two papers on TMEM147's cellular function (PMID:32694168 and PMID:32820719) and the cached abstracts and full text in `references_cache/`. I cross-checked against web searches of OMIM/MedGen, IMPC, and the nicalin–NOMO literature. Searches for 2024–2026 found no newer patient series, so the whole literature comes from 25 patients in 16 families. The claude.ai PubMed and OLS connectors need authorization (in claude.ai connector settings) before they can be used, so I did not query them.

Quotes marked **[abstract]** are exact text from the PubMed abstract. Quotes marked **[full text]** come from the cached PMC full text of PMID:36044892.

---

## 1. Disease information

**Overview.** This is an ultra-rare autosomal recessive syndromic intellectual disability caused by biallelic loss-of-function variants in *TMEM147*. Its main features are:
- global developmental delay
- moderate-to-profound intellectual disability
- absent or minimal speech
- behavioural problems, especially self-injury
- consistent coarse facial dysmorphism
- a pseudo-Pelger-Huët anomaly on blood smear

> "These affected children displayed congruent clinical features including coarse facies, developmental delay, intellectual disability, and behavioral problems." — PMID:36044892 [abstract]

> "Our findings provide clinical, genetic, and functional evidence that bi-allelic loss-of-function variants in TMEM147 cause syndromic intellectual disability due to ER-translocon and nuclear organization dysfunction." — PMID:36044892 [abstract]

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0859298 |
| OMIM | #620075 (gene *603890? — not verified; check OMIM for the TMEM147 gene MIM number*) |
| MedGen | UID 1824005 |
| LOVD | disease 07058 |
| Orphanet | No specific ORPHA code found. Probably filed under a generic syndromic ID grouping. |
| ICD-10/11, MeSH | No specific codes. Generic options: ICD-10 Q87.8 / F72–F73; ICD-11 LD90 (disorders of intellectual development). |

**Synonyms.** TMEM147-related neurodevelopmental disorder; TMEM147 deficiency. OMIM's abbreviation is **NEDFLPH**. The existing KB entry uses "NEDFLPA", which should be corrected.

**Source type.** All data come from aggregated case series (individual patient tables in the publications). There are no EHR or registry data.

## 2. Etiology

- **Cause:** germline biallelic (homozygous or compound heterozygous) loss-of-function variants in *TMEM147*.
- **Risk factor:** parental consanguinity. "Twenty individuals were born to consanguineous parents (87%)." [full text, PMID:36044892]
- **Founder alleles:** p.Ile133Asn recurs in North African/Egyptian families and p.Gly7Arg recurs in two families. These counts come from the KB entry's reading of the full-text table and should be re-verified against Table S1.
- **Environmental, protective, and gene–environment factors:** none known; none are expected for a fully penetrant recessive Mendelian disorder.

## 3. Phenotypes

Denominators are from the founding cohort (n = 23) unless stated otherwise. Onset is in infancy for all features. The course is static: a non-progressive developmental encephalopathy.

| Phenotype | HPO | Frequency | Source / quote |
|---|---|---|---|
| Global developmental delay | HP:0001263 | 23/23 | "All individuals had global developmental delay and intellectual disability." [full text] |
| Intellectual disability, severe/profound | HP:0001249 (HP:0010864, HP:0002187) | 21/21 evaluable | "All individuals presented ID, which was considered severe for all but one individual" [full text] |
| Motor delay | HP:0001270 | 23/23 | "most children were ambulatory by 5 years of age" [full text] |
| Delayed speech and language development | HP:0000750 | 22/22 | "eight individuals (36%) had developed no speech at all, 12 (55%) could only babble or speak a few words, and only two (9%) could make short sentences." [full text] |
| Absent speech | HP:0001344 | 8/22 (36%) | same quote |
| Behavioural problems / self-injury | HP:0000708 / HP:0100716 | 15 (65%) | "Behavioral problems were observed in 15 individuals (65%) who shared a common tendency of self-injury." [full text] |
| Hyperactivity; aggression; anger outbursts | HP:0000752; HP:0000718 | subset of the 15 | same paragraph |
| Coarse facial features | HP:0000280 | 22/22 | "coarse facies, prominent forehead, board depressed nasal root, tented mouth, long smooth philtrum, and low-set ears as major features" [full text] |
| Prominent forehead; depressed nasal bridge; long philtrum; smooth philtrum; tented upper lip vermilion; low-set ears | HP:0011220; HP:0005280; HP:0000343; HP:0000319; HP:0010804; HP:0000369 | major features (per-feature counts in Table S2) | same; confirmed by composite face analysis |
| Hyposegmentation of neutrophil nuclei (pseudo-Pelger-Huët) | HP:0011447 | in the patients tested; affects ~15–25% of neutrophils per patient | "Abnormal nuclear segmentation and chromatin compaction were also observed in approximately 20% of neutrophils" [abstract] |
| Thin corpus callosum | HP:0033725 | most of those with abnormal MRI (18 imaged) | "Corpus callosum was thin in most individuals but never dysplastic" [full text] |
| Ventriculomegaly; delayed CNS myelination (posterior/temporal, improving over time); mild cerebellar atrophy | HP:0002119; HP:0002188; HP:0001272 | some of 18 | "enlarged ventricles, thin corpus callosum, and white matter hyperintensities … mild cerebellar atrophy without dysplasia in some individuals" [full text] |
| Growth parameter below −2 SD | — | 8/23 (35%) | "eight individuals (35%) presented at least one measurement below −2 standard deviations" [full text] |
| Secondary (postnatal) microcephaly | HP:0005484 | 4/23 | "four presented isolated microcephaly that was not present at birth" [full text] |
| Hypotonia | HP:0001252 | 3 (14%) | "three individuals (14%) presented with hypotonia, two had tonic seizures (9%)" [full text] |
| Tonic seizures | HP:0032792 | 2 (9%) | same |
| Mirror movements (transient) | HP:0001335 | 1 | same |
| Spasticity | HP:0001257 | 2/2 in the 2023 family | "featured spasticity as a phenotypic expansion" — PMID:37668766 [abstract] |
| Patent foramen ovale; atrial septal defect; patent ductus arteriosus | HP:0001655; HP:0001631; HP:0001643 | 2/11, 1/11, 1/11 on echo | "two presented a patent foramen ovale, one presented an atrial septum defect, and one a large patent ductus arteriosus" [full text] |

**Quality of life.** There are no formal QoL data (EQ-5D, PedsQL). The main burdens come from profound ID, lack of functional speech, and self-injurious behaviour.

## 4. Genetic and molecular information

- **Gene:** *TMEM147*, a ~22 kDa protein with seven transmembrane helices, located at 19q13.12. The 2023 report uses transcript NM_001242597.2.
- **Variant spectrum.** The founding cohort reported 12 variants: "stop-gain (3/12), frameshift (4/12), missense (3/12), and splice-site variants (2/12)" [full text]. The 2023 report added a 13th, the frameshift NM_001242597.2:c.193_197del.
  - Examples cited in full text and in the KB: c.100_118del (p.Lys34Serfs*33); c.540_543dup (p.Val182Leufs*66); c.344+5G>A (exon 4 skipping); c.345-1G>T; p.Tyr162*; missense p.Gly7Arg, p.Ile133Asn, p.Arg166Trp.
- **Functional consequence: loss of function.**
  - Truncating alleles are predicted to undergo nonsense-mediated decay.
  - Missense proteins localise correctly but are unstable: "accelerated degradation of TMEM147 mutant proteins occurs via the autophagy-lysosomal pathway" [full text]. Bafilomycin rescues their levels.
- **Genotype–phenotype:** "No phenotypic differences between affected individuals with predicted loss-of-function versus missense variants were noted." [full text]
- **ClinVar / ClinGen:** no ClinGen gene–disease validity curation was found. Check ClinVar for current classifications. gnomAD allele frequencies were not retrieved.
- **Modifiers, epigenetics, chromosomal abnormalities:**
  - No modifier genes are known.
  - The peripheral-blood **EpiSign** profile matched none of 59 episignatures: "incompatible with all 59 episignatures assessed, including chomatinopathy conditions such as Cornelia de Lange, Rubinstein-Taybi, Coffin-Siris, and Wiedemann-Steiner syndromes" [full text].
  - No chromosomal or CNV mechanism has been reported.

## 5. Environmental information

None applicable. No environmental, lifestyle or infectious contributors are known.

## 6. Mechanism / pathophysiology

**Causal chain**

1. Biallelic *TMEM147* truncating, splice or destabilising missense variants **lead to** loss of TMEM147 protein. Truncating alleles are lost through nonsense-mediated decay (inferred); missense proteins through autophagy-lysosomal degradation (shown in COS-1 cells, PMID:36044892).
2. **Branch A (ER).** Loss of TMEM147 **disrupts** the nicalin–TMEM147–NOMO module of the ribosome-bound multipass translocon (Sec61–TMCO1–CCDC47–NCLN–TMEM147–NOMO). This translocon is needed to make multipass membrane proteins:
   > "a ~ 360 kDa ribosome-associated complex comprising the core Sec61 channel and five accessory factors: TMCO1, CCDC47 and the Nicalin-TMEM147-NOMO complex" — PMID:32820719 [abstract]

   This **results in** upregulation of CKAP4 (CLIMP-63) and RTN4 (NOGO) and reorganisation of the ER in patient fibroblasts:
   > "TMEM147-deficient cells showed CKAP4 (CLIMP-63) and RTN4 (NOGO) upregulation with a concomitant reorientation of the ER, which was also witnessed in primary fibroblast cell culture." — PMID:36044892 [abstract]

   The defect in multipass protein biogenesis in patient cells is *inferred* from the complex's known function; it has not been measured.
3. **Branch B (nuclear envelope).** Loss of TMEM147 **causes** LBR to lose its anchoring at the inner nuclear membrane. In patient fibroblasts LBR spreads through the nucleus, and nuclei show abnormal segmentation:
   > "We show that TMEM147 physically interacts with LBR, and that the C-terminus of LBR is essential for their functional interaction." — PMID:32694168 [abstract]

   > "LBR mislocalization and nuclear segmentation was observed in primary fibroblast cells." — PMID:36044892 [abstract]
4. **Branch B to blood.** Mislocalised LBR **leads to** defective nuclear lobulation and chromatin compaction in maturing granulocytes. This shows as the pseudo-Pelger-Huët anomaly in ~15–25% of neutrophils, a partial version of the phenotype seen with LBR haploinsufficiency. The link is inferred from the LBR mechanism; it has not been shown directly in TMEM147-deficient granulocytes.
5. **Branch C (sterol; speculative).** In HeLa cells, knockdown of *TMEM147* lowers LBR and DHCR7 and changes cholesterol homeostasis:
   > "TMEM147 also physically interacts with the key sterol reductase DHCR7 … lipidomic analysis upon TMEM147 silencing identified changes in cellular cholesterol levels" — PMID:32694168 [abstract]

   Whether patients have abnormal sterol levels has not been tested.
6. **Convergence (inferred).** ER translocon/ER-shape dysfunction, possibly with nuclear-envelope and chromatin dysfunction, **impairs** neuronal development. This **results in** a non-progressive developmental encephalopathy: thin corpus callosum, ventriculomegaly, delayed myelination, intellectual disability, absent speech and behavioural disturbance. The supporting evidence is computational (brain-specific co-expression of TMEM147 with NDD genes) plus clinical correlation.
   > "TMEM147-related disorders cannot be considered as primary white matter disorders but rather as encephalopathies." [full text]
7. **Facial dysmorphism.** The mechanism is unknown. A possible link to nicalin–NOMO, which modulates Nodal signalling in zebrafish mesendoderm patterning (Dettmer et al. 2010, PMID:20538592), is hypothetical.

**Open question.** In HeLa cells, knocking down *TMEM147* lowers LBR protein. In patient fibroblasts LBR is mislocalised but its level is normal:
> "the diffusional mobility of LBR is not accompanied by decreased protein levels in primary fibroblast cells from affected individuals" [full text]

The KB already records this as a HUMAN_MODEL_MISMATCH discussion.

**Suggested terms**

| Category | Terms |
|---|---|
| GO biological process | GO:0160063 multi-pass transmembrane protein insertion into ER membrane *(verify)*; GO:0007029 endoplasmic reticulum organization; GO:0006998 nuclear envelope organization; GO:0070828 heterochromatin organization; GO:0030851 granulocyte differentiation; GO:0007420 brain development; GO:0022010 CNS myelination; GO:0000184 NMD; GO:1905146 lysosomal protein catabolic process |
| GO cellular component | GO:0005789 ER membrane; GO:0005637 nuclear inner membrane; GO:0005635 nuclear envelope |
| GO molecular function | GO:0043022 ribosome binding *(verify)* |
| Cell Ontology | CL:0000775 neutrophil; CL:0000771 eosinophil; CL:0000057 fibroblast; CL:0000540 neuron |
| Other genes | LBR hgnc:6518; DHCR7; TMCO1; CCDC47; NCLN; NOMO1 |

Terms marked *verify* came from memory and must be looked up before binding.

No transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen datasets specific to this disease were found.

## 7. Anatomical structures affected

- **Primary:** brain (UBERON:0000955): corpus callosum (UBERON:0002336), cerebral white matter (UBERON:0002316), lateral ventricles (UBERON:0002285), cerebellum (UBERON:0002037).
- **Craniofacial:** face (UBERON:0001456), forehead, philtrum, external ear.
- **Blood:** blood (UBERON:0000178), with granulocytes as the affected cells.
- **Heart (occasional):** interatrial septum (UBERON:0002085) and ductus arteriosus.
- **Subcellular:** ER membrane, inner nuclear membrane, heterochromatin.
- **Lateralisation:** findings are bilateral and symmetric.

## 8. Temporal development

- **Onset:** congenital or infantile. Some patients had intrauterine growth restriction or neonatal problems; delay is evident in infancy.
- **Course:** a static developmental encephalopathy.
  - Walking is achieved late, between about 1.5 and 5 years, with an unsteady gait.
  - Speech remains absent or minimal into adolescence.
  - Myelination delay improves on follow-up imaging: "visible improvement upon follow-up (i5 – F4-IV-9, available MRIs at 2 and 5 years of age)" [full text].
- **Regression and remission:** neither has been reported.
- **Critical period:** early childhood, the window for communication and behaviour intervention.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). Penetrance appears complete. Heterozygous carriers are healthy: "Heterozygous carriers were healthy." [full text]
- **Consanguinity:** 87% of the founding cohort.
- **Expressivity:** fairly consistent. ID ranges from moderate to profound.
- **Anticipation, mosaicism:** none reported.
- **Population:** cases come mostly from consanguineous families, including North African/Egyptian and Iranian families (PMID:37668766).
- **Prevalence:** unknown (`prevalence_class: NOT_YET_DOCUMENTED`; `measure_type: CASES_IN_LITERATURE`). The literature totals 25 patients in 16 families.
- **Sex ratio:** no sex bias is expected; detailed counts are in Table S2.
- **Carrier frequency:** not established.

## 10. Diagnostics

- **Genetic testing**
  - Exome or genome sequencing is the diagnostic route: "Whole exome sequencing and validating Sanger sequencing were utilized to confirm the identified causal variant." (PMID:37668766 [abstract])
  - *TMEM147* is on intellectual-disability panels, including the Genomics England PanelApp entity.
  - Chromosomal microarray, karyotype, FISH, mtDNA and repeat-expansion testing are not informative except to exclude other diagnoses.
- **Blood smear (cheap supportive biomarker):** look for hyposegmented or bilobed "sack-shaped" neutrophil nuclei, chromatin clumping, and drumstick-like appendages in ~15–25% of neutrophils.
  - It is called **pseudo**-Pelger-Huët because "the majority of mature granulocytes were not bilobed" [full text].
  - It can be used to support the pathogenicity of a variant of uncertain significance.
- **Brain MRI:** thin corpus callosum, ventriculomegaly, posterior delayed myelination.
- **Echocardiography:** screen for septal defects and PDA.
- **EpiSign:** a negative chromatinopathy episignature helps steer away from look-alike disorders.
- **Differential diagnosis:**
  - Cornelia de Lange, Rubinstein–Taybi, Coffin–Siris and Wiedemann–Steiner syndromes (all excluded by EpiSign and sequencing).
  - LBR-related Pelger-Huët anomaly or HEM/Greenberg dysplasia.
  - Disorders of the same translocon complex: *TMCO1* (cerebrofaciothoracic dysplasia) and *CCDC47* (trichohepatoneurodevelopmental syndrome).
  - Acquired pseudo-Pelger-Huët (myelodysplasia, drugs).
- **Screening:** no newborn screening. Carrier and cascade testing is possible in families with a known variant.

## 11. Outcome and prognosis

- No deaths attributed to the disorder have been reported, but follow-up is limited to childhood and adolescence. Life expectancy is unknown.
- Morbidity is lifelong dependence because of profound ID, absent speech and behavioural problems.
- Complications include occasional seizures and congenital heart defects.
- No prognostic biomarkers are known, and there is no genotype–phenotype correlation.

## 12. Treatment

There is no disease-modifying therapy and no registered clinical trials (no NCT or ICTRP entries found). Care is supportive:

| Intervention | NCIT |
|---|---|
| Supportive care | NCIT:C15747 |
| Speech-language therapy and augmentative and alternative communication (AAC) | NCIT:C159273 |
| Physical therapy | NCIT:C15302 |
| Occupational therapy | NCIT:C121351 |
| Behavioural intervention for self-injury and aggression | NCIT:C15184 |
| Antiseizure medication when needed | NCIT:C15986 Pharmacotherapy, with the agent recorded in `therapeutic_agent` |
| Cardiac follow-up or repair of septal defects/PDA | surgical procedure NCIT:C15329 only if repair is done |
| Genetic counselling | NCIT:C15240 |

Pharmacogenomic, gene, RNA and cell therapies are not available. A sterol-directed approach is speculative only, because no sterol abnormality has been shown in patients.

## 13. Prevention

- **Primary:** genetic counselling. The recurrence risk is 25% per pregnancy for carrier couples. Carrier testing within consanguineous kindreds, and prenatal or preimplantation testing once familial variants are known.
- **Tertiary:** early developmental and behavioural intervention, echocardiography, and seizure surveillance.
- **Not applicable:** vaccination and environmental measures.

## 14. Other species and natural disease

- No naturally occurring animal disease is known; no OMIA entry was found.
- TMEM147 is highly conserved in vertebrates, with orthologues in mouse (*Tmem147*, MGI:1915011) and zebrafish (ZFIN ZDB-GENE-040718-187).
- The protein is "a novel, highly conserved membrane protein with a putative topology similar to APH-1" (Dettmer et al. 2010, PMID:20538592).
- Not infectious or zoonotic.

## 15. Model organisms

- **Mouse (IMPC, *Tmem147<sup>em1(IMPC)J</sup>* exon-deletion allele).** The IMPC summary lists significant phenotypes in three systems: mortality/aging, integument and growth/body region. The search summary reported **complete preweaning lethality in homozygotes**, abnormal body wall at E18.5, and nail anomalies in heterozygotes. The IMPC data table did not render in my fetch, so this lethality call must be checked on the IMPC viability page before it is curated.
  - This is a **HUMAN_MODEL_MISMATCH** candidate: the null mouse appears to die, while humans with biallelic loss of function survive. Possible explanations include residual function of human alleles or species differences.
- **Zebrafish.** tmem147 is expressed in early embryos. nicalin/Nomo antagonise Nodal signalling in mesendodermal patterning (Dettmer et al. 2010). *nomo* mutant zebrafish show craniofacial cartilage hypoplasia (ZFIN ZDB-PUB-181213-5, PMID:30539698), which is indirect support for a role of the complex in facial development. No *tmem147*-specific zebrafish mutant phenotype was found.
- **Cell models.**
  - HeLa RNAi knockdown: LBR and DHCR7 loss, cholesterol changes (PMID:32694168).
  - HEK293 translocon biochemistry and cryo-EM (PMID:32820719).
  - COS-1 overexpression of mutant proteins, and patient primary dermal fibroblasts (PMID:36044892).
  - No iPSC-derived neurons or organoids have been reported. This is a clear gap for testing which branch (ER or nuclear envelope) drives the neurodevelopmental phenotype.

---

## Things to fix in the existing KB entry

- **Abbreviation:** OMIM uses **NEDFLPH**; the entry's description says "NEDFLPA".
- **Self-injury frequency:** the entry says 15/22 (68%); the paper says "15 individuals (65%)". Align with the source.
- **Deprecated fields:** the entry still carries `updated_date` and the deprecated free-text `prevalence.percentage`. Convert to `measure_type: CASES_IN_LITERATURE` plus a `prevalence_class`.
- **Possible additions:**
  - the IMPC mouse as an `animal_models` record, once lethality is verified;
  - the Dettmer 2010 nicalin–NOMO paper (PMID:20538592) as a reference;
  - the DHCR7/cholesterol branch, either as an emerging hypothesis or as a knowledge gap.

## Sources
- Thomas Q et al. 2022, *AJHG*, PMID:36044892 — [PMC9606387](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9606387/)
- Ghorashi T et al. 2023, *Neurogenetics*, PMID:37668766 — [scholarhub](https://scholarhub.vn/publication/:slug/2944755b-6e85-452a-bbc6-267b68c976ae)
- Christodoulou A et al. 2020, *J Cell Sci*, PMID:32694168
- McGilvray PT et al. 2020, *eLife*, PMID:32820719
- Dettmer U et al. 2010, *J Biol Chem*, PMID:20538592 — [CIPSM](https://www.cipsm.de/publications/research-area-f/transmembrane-protein-147-tmem147-is-a-novel-component-of-the-nicalin-nomo-protein-complex), [TUM](https://portal.fis.tum.de/en/publications/transmembrane-protein-147-tmem147-is-a-novel-component-of-the-nic/)
- [MedGen 1824005](https://ncbi.nlm.nih.gov/medgen/1824005) · [LOVD disease 07058](https://databases.lovd.nl/shared/diseases/07058) · [PanelApp TMEM147](https://nhsgms-panelapp.genomicsengland.co.uk/entities/TMEM147) · [GeneCards TMEM147](https://www.genecards.org/card/TMEM147)
- [IMPC Tmem147 (MGI:1915011)](https://mousephenotype.org/data/genes/MGI:1915011) · [ZFIN tmem147](https://www.zfin.org/ZDB-GENE-040718-187) · [ZFIN nomo paper](https://www.zfin.org/ZDB-PUB-181213-5)
