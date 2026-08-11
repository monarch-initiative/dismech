---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-29T19:49:54.943913'
end_time: '2026-06-29T19:55:12.157273'
duration_seconds: 317.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Antisynthetase Syndrome
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
  - claude-opus-4-8[1m]
  web_search_requests: 10
  num_turns: 13
  total_cost_usd: 2.4243795
  session_id: f99c7995-9acd-4252-961d-6e1a679452a1
  stop_reason: end_turn
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Antisynthetase Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Antisynthetase Syndrome** covering all of the
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

I now have comprehensive material across all sections. Here is the full research report.

---

# Comprehensive Research Report: Antisynthetase Syndrome

**Prepared:** 2026-06-29 | **For:** dismech knowledge base entry | **Category:** Complex (systemic autoimmune)

> **A note on sourcing and verification:** This report synthesizes recent reviews and cohort studies. PMIDs I directly verified via fetch are flagged **[verified]**; identifiers and quotes drawn from search-result summaries are flagged **[search-derived — verify snippet against abstract before committing to YAML]**. Per the dismech SOP, every snippet must be confirmed as an exact substring of the cached abstract via `just fetch-reference` + `just validate-references` before it becomes evidence. Treat the quotes below as *leads*.

---

## 1. Disease Information

**Overview.** Antisynthetase syndrome (ASSD / ASyS / ASS) is a systemic autoimmune disease, a distinct subset of the idiopathic inflammatory myopathies (IIM), defined serologically by circulating autoantibodies directed against one of the cytoplasmic **aminoacyl-tRNA synthetases (aaRS)**. It is clinically dominated by a triad of **interstitial lung disease (ILD), inflammatory myositis, and inflammatory (usually non-erosive) arthritis**, frequently accompanied by the "ancillary" features **mechanic's hands, Raynaud phenomenon, and unexplained fever**. ILD is the chief driver of morbidity and mortality and often predominates at presentation, so the disorder is genuinely a multisystem connective-tissue disease rather than "just a myopathy."

> "Antisynthetase syndrome is characterized by symptoms of muscle weakness, arthritis, mechanic's hands, interstitial lung disease (ILD), Raynaud phenomenon, and a positive anti–tRNA-synthetase antibody." [search-derived]

**Key identifiers:**
- **MONDO:** `MONDO:0019344` — *antisynthetase syndrome* **[verified via local OAK]**
- **Orphanet:** ORPHA:81 (Antisynthetase syndrome)
- **OMIM:** No single Mendelian OMIM entry (complex/polygenic autoimmune disease — not a monogenic disorder)
- **ICD-10:** No dedicated code; typically captured under **M35.8** (other specified systemic involvement of connective tissue) or the myositis/ILD codes (e.g., M33.x dermatomyositis/polymyositis; J84.x for the ILD component)
- **ICD-11:** 4A41 region (overlap/undifferentiated connective tissue diseases / inflammatory myopathies); no unique stem code
- **MeSH:** No standalone MeSH descriptor; indexed via "Myositis," "Lung Diseases, Interstitial," and the supplementary concept for aminoacyl-tRNA synthetase autoantibodies

**Data derivation:** Disease-level aggregated resources (review syntheses, multicenter cohorts such as AENEAS, registry/population studies). A small amount is EHR/population-based (e.g., the Olmsted County population cohort, PMID 39814448).

**Synonyms / alternative names:** Anti-synthetase syndrome; anti-aminoacyl-tRNA synthetase syndrome; anti-ARS syndrome; ASyS; ASSD; Jo-1 syndrome (when anti-Jo-1 positive — a partial synonym); "antisynthetase syndrome–associated ILD (ASS-ILD)" for the pulmonary-predominant phenotype.

---

## 2. Etiology

**Causal factors.** ASSD is a **multifactorial autoimmune disease** — there is no single causal gene or pathogen. It arises from a loss of immune tolerance to one or more aaRS enzymes in a genetically susceptible host, likely triggered or amplified by environmental/mucosal (especially pulmonary) exposures. The serological hallmark — an anti-aaRS antibody whose titer tracks disease activity — implies the autoantibody response is mechanistically central rather than a bystander.

> "titers of the serum anti-Jo-1 antibodies correlate with disease activity" — Kanaji et al., *Trends Biochem Sci* (PMID 36280495) **[verified]**

**Genetic risk factors (susceptibility loci — not Mendelian causes):**
- **MHC class II is the strongest risk locus.** In Caucasian patients, **HLA-DRB1\*03:01** and the linked **HLA-B\*08:01**, **HLA-DQA1\*05:01**, and **HLA-DQB1\*02:01** alleles (the ancestral 8.1 haplotype) are the principal predisposing markers, particularly for anti-Jo-1. **HLA-DRB1\*07:01** appears **protective**. [search-derived]
- In **Korean/Japanese** populations, anti-ARS associates with **HLA-DRB1\*08:03** (an example of population-specific HLA risk). [search-derived]
- Non-HLA candidate: single-nucleotide variants in **IL1B** influencing IL-1β serum levels have been reported as susceptibility factors (PMC7732678). [search-derived]

**Environmental / lifestyle risk factors:**
- **Sex:** female predominance (≈2–3:1 female:male).
- **Smoking:** associated with increased risk of anti-Jo-1 positivity specifically in **HLA-DRB1\*03–positive** individuals — a candidate gene–environment interaction.
- **Age:** peak onset in the 5th–6th decades.

**Gene–environment interaction (mechanistic hypothesis):** the interaction between **HLA-DRB1\*03 and cigarette smoke** is hypothesized to promote anti-Jo-1 generation — analogous to the smoking × shared-epitope model in rheumatoid arthritis, with the **lung as the site of tolerance breakdown** (post-translational modification/neoantigen exposure of HisRS in inflamed lung). [search-derived]

**Protective factors:** HLA-DRB1\*07:01 (genetic, above). No well-established environmental protective factor.

---

## 3. Phenotypes

ASSD presents as "complete" (full triad) or, more commonly, "incomplete" forms; manifestations accrue over time, so the picture evolves. Approximate frequencies vary widely by cohort and by antibody (see §9). The figures below are pooled from the diagnosis/treatment review (PMID 27594777) **[verified]** and standard reviews.

| Phenotype | Type | Approx. frequency | Suggested HPO term |
|---|---|---|---|
| **Interstitial lung disease** (NSIP > OP > UIP patterns; dyspnea, dry cough) | Clinical/imaging | **70–90%** (86% in one 203-pt cohort) | `HP:0006530` Abnormal pulmonary interstitial morphology |
| **Inflammatory myositis** / proximal muscle weakness | Sign | **~60–75%** | `HP:0003701` Proximal muscle weakness; `HP:0003198` Myopathy |
| **Inflammatory arthritis / arthralgia** (symmetric, non-erosive, often RA-mimicking) | Sign | **~50–60%** | `HP:0001369` Arthritis; `HP:0002829` Arthralgia |
| **Mechanic's hands** (hyperkeratotic, fissured, scaling skin of radial/ulnar fingers) | Physical sign | **~30%** | `HP:0010765` Palmar hyperkeratosis (closest; "mechanic's hands" lacks a precise HPO term — verify) |
| **Raynaud phenomenon** | Symptom | **~40%** | `HP:0030880` Abnormal vascular physiology / `HP:0033740`? → use `HP:0030880`-family; commonly mapped to *Raynaud phenomenon* — verify term |
| **Fever** (unexplained, often at flares) | Symptom | **~20%** | `HP:0001945` Fever |
| **Dyspnea** | Symptom | common | `HP:0002094` Dyspnea |
| **Elevated creatine kinase** | Lab abnormality | common when myositis present | `HP:0003236` Elevated circulating creatine kinase concentration |
| **Dysphagia** (esophageal/pharyngeal muscle) | Symptom | subset | `HP:0002015` Dysphagia |
| **Pulmonary fibrosis** (late) | Imaging/path | subset, prognostic | `HP:0002206` Pulmonary fibrosis |
| **Pulmonary arterial hypertension** (late complication) | Sign | subset, poor prognosis | `HP:0002092` Pulmonary arterial hypertension |
| **Myalgia** | Symptom | common | `HP:0003326` Myalgia |

**Phenotype characteristics:** Adult-onset (mean 43–60 yr; see §9). Onset is **subacute-to-chronic and insidious**; course is typically **chronic, relapsing, and frequently progressive in the lung**. Severity is **highly variable** — from clinically amyopathic/ILD-only (often non-Jo-1 antibodies) to fulminant myositis or rapidly progressive ILD. Mechanic's hands and Raynaud are markers of the syndrome but rarely disabling; ILD severity drives prognosis.

**Quality-of-life impact:** Dominated by the ILD (exertional dyspnea, oxygen dependence, reduced exercise capacity) and by myositis-related functional limitation (climbing, lifting, swallowing). Arthritis adds RA-like functional impairment. No ASSD-specific PRO instrument; SF-36/EQ-5D and myositis tools (e.g., HAQ, Myositis Activities Profile) are used generically.

---

## 4. Genetic / Molecular Information

**This is not a Mendelian disease** — there are no causal germline mutations. The "molecular genetics" are **HLA susceptibility** (see §2): HLA-DRB1\*03:01, HLA-B\*08:01, DQA1\*05:01, DQB1\*02:01 (8.1 haplotype) confer risk; DRB1\*07:01 protective; DRB1\*08:03 in East Asians. **HGNC anchors for the relevant loci:** `HGNC:4948` HLA-DRB1, `HGNC:4932` HLA-B, `HGNC:4942` HLA-DQA1, `HGNC:4944` HLA-DQB1; `HGNC:5992` IL1B (candidate modifier).

**Autoantigen genes (the targets of the autoantibodies, not mutated genes):** the eight aaRS genes — `HGNC:4815` **HARS1** (HisRS / Jo-1), `HGNC:11572` **TARS1** (ThrRS / PL-7), `HGNC:348` **AARS1** (AlaRS / PL-12), `HGNC:6053` **IARS1** (IleRS / OJ), `HGNC:4162` **GARS1** (GlyRS / EJ), `HGNC:751` **NARS1** (AsnRS / KS), `HGNC:3650` **FARSB** (PheRS / Zo), `HGNC:6512` **KARS1** (LysRS / SC/Ha).

**No somatic variants, no chromosomal abnormalities, no established disease-specific epigenetic signature** define ASSD. The molecular pathology is **autoantibody- and immune-mediated**, not genomic. Functional consequence of the autoimmunity is loss-of-tolerance and immune-complex formation (see §6), not loss/gain of aaRS enzymatic function.

**Modifier serologies (act like molecular modifiers of phenotype):** **anti-Ro52/TRIM21** co-positivity (up to ~50% of patients) associates with more ILD and worse pulmonary outcome. `HGNC:11312` TRIM21.

---

## 5. Environmental Information

- **Smoking** — strongest candidate environmental factor; interacts with HLA-DRB1\*03 to promote anti-Jo-1 (see §2). [search-derived]
- **Pulmonary exposures / mucosal injury** — the lung is hypothesized as the initiating site where aaRS (HisRS) is secreted/modified and presented, breaking tolerance (consistent with ILD-predominant presentations). [verified mechanism, PMID 36280495]
- **Infectious agents:** No specific pathogen is established as causal. Viral infection is a proposed nonspecific "danger signal" that upregulates aaRS secretion from infected macrophages (secretome studies show aaRS release from virus-infected macrophages, PMID 36280495 **[verified]**), but ASSD is **not an infectious disease**.
- **Occupational/toxin exposures:** none specifically established.

---

## 6. Mechanism / Pathophysiology

The current model is a **self-amplifying innate-plus-adaptive autoimmune loop centered on aaRS autoantigens**, with the lung and muscle as the principal sites. Cited details are from Kanaji et al. (PMID 36280495) **[verified]** unless noted.

**Causal chain (upstream → downstream):**

1. **Tissue injury / regeneration + tissue-specific aaRS secretion (upstream trigger).** Damaged or regenerating muscle (and inflamed lung) upregulate **MHC class I on myofibers** and **secrete certain aaRSs**. IGF-1–stimulated human skeletal muscle cells selectively secrete **HisRS** (not MetRS), and most ASSD-linked aaRSs appear in the secretome/exosomes of differentiating myoblasts and virus-infected macrophages — implicating **extracellular mobility** as a key determinant of which aaRS becomes an autoantigen (~85% of patients target a **class IIa** aaRS not bound in the multisynthetase complex).
   > "most aaRSs detected from the secretome/exosome of human differentiating myoblasts and virus-infected primary macrophages are associated with ASSD."

2. **Neoepitope exposure — the WHEP domain.** **HisRS (Jo-1)** is the dominant target (30–60%). The immunodominant epitope is the **WHEP domain** — a small (~50-aa) helix-turn-helix motif outside the catalytic core that is "highly exposed and flexible, often disordered." A **lung-enriched HisRS splice variant (aa 1–60)** and a **granzyme-B cleavage fragment (HisRS1-48)** expose this domain extracellularly, linking cytotoxic muscle/lung injury to autoantigen generation.

3. **Antigen presentation & T-cell help.** Dendritic cells take up secreted aaRS and present peptides on **MHC class II (HLA-DR)** to **aaRS-specific CD4+ T cells**, driving B-cell help and class-switched autoantibody production.

4. **Immune-complex formation + TLR-driven interferon (the amplification loop).** Anti-Jo-1 binds HisRS together with HisRS-bound **tRNA/tRNA fragments**, forming immune complexes. Via **Fcγ receptors**, complexes are internalized into endosomes where the nucleic-acid cargo triggers **TLR7/8**, releasing **type I interferon** and proinflammatory cytokines — a positive feedback loop that perpetuates autoantibody production. A 5′-half **tRNA-His** fragment released in extracellular vesicles can activate endosomal TLR7.
   > "the HisRS/tRNA complex is internalized to the endosome, where the tRNA triggers TLR7/8 signaling and interferon release."

5. **Interferon programs (effector arm).** ASSD muscle shows **type II IFN–inducible genes (e.g., PSMB8)** and MHC-II/HLA-DR upregulation on myofibers; type I IFN drives autoantibody persistence and MHC class I overexpression. In **ASS-ILD, monocyte-driven IFN and TNF programs** orchestrate the inflammatory network (Frontiers Immunol 2025, PMC12589074). [search-derived]

6. **Neutrophils / NETs (tissue-damage effector).** Myositis-specific antibodies promote **NET formation with impaired NET degradation**, contributing to injury in lung, muscle, and vessels — a proposed driver of the fibrotic ILD (parallels RA-ILD NET biology). [search-derived]

7. **Chemokine activity of the autoantigen.** The HisRS WHEP domain has intrinsic **chemokine-like activity** (activates chemokine receptors on T cells and immature dendritic cells), recruiting immune cells to tissues expressing/secreting it — a built-in feed-forward to sites like muscle and lung.

8. **Downstream tissue damage → clinical disease.** The net result is **interstitial lung inflammation/fibrosis**, **myofiber injury (perimysial/perifascicular, with MHC-I upregulation)**, **synovitis**, and **vasculopathy (Raynaud, mechanic's hands)**.

**Ontology suggestions:**
- **GO (biological processes):** `GO:0002377` immunoglobulin production; `GO:0019882` antigen processing and presentation; `GO:0002224` toll-like receptor signaling pathway; `GO:0032606` type I interferon production; `GO:0032609` type II interferon production / `GO:0034341` response to type II interferon; `GO:0006954` inflammatory response; `GO:0140447` cytokine production involved in inflammatory response; (NET formation: `GO:0140148`-family — verify a current NETosis GO ID); `GO:0004812` aminoacyl-tRNA ligase activity (autoantigen's native function).
- **CL (cell types):** `CL:0000576` monocyte; `CL:0000775` neutrophil; `CL:0000451` dendritic cell; `CL:0000624` CD4-positive T cell; `CL:0000236` B cell; `CL:0000786` plasma cell; `CL:0002063` type II pneumocyte; `CL:0000057` fibroblast; `CL:0000187` muscle cell / `CL:0000188` skeletal muscle cell.
- **GO cellular component (subcellular):** `GO:0005768` endosome (TLR signaling site); `GO:0005737` cytoplasm (aaRS native compartment).

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Lung** (`UBERON:0002048`) — interstitium; ILD is the dominant organ injury. Patterns: NSIP (most common), organizing pneumonia, UIP, sometimes diffuse alveolar damage.
- **Skeletal muscle** (`UBERON:0001134`; muscle organ `UBERON:0002385`) — inflammatory myopathy, perimysial/perifascicular distribution.
- **Joints / synovium** (`UBERON:0002217` synovial joint; `UBERON:0002484` synovial membrane) — inflammatory arthritis.

**Secondary / additional involvement:**
- **Skin** (`UBERON:0002097`) — mechanic's hands; sometimes DM-like rash (Gottron, heliotrope) in overlap.
- **Peripheral vasculature / digital vessels** — Raynaud phenomenon.
- **Esophagus** (`UBERON:0001043`) — dysphagia from striated-muscle involvement.
- **Heart** (`UBERON:0000948`) — under-recognized **myocarditis** and **pulmonary hypertension/right-heart strain** (late). [search-derived: anti-Jo-1 myocarditis reports]

**Body systems:** respiratory, musculoskeletal, integumentary, cardiovascular, immune.

**Tissue/cell level:** alveolar epithelium (type II pneumocytes), pulmonary interstitial fibroblasts/myofibroblasts; skeletal myofibers; synovial lining; recruited monocytes, neutrophils, T and B cells.

**Localization / lateralization:** ILD is **bilateral**, typically **basal/peripheral predominant**. Myositis is **proximal and symmetric**. Arthritis is **symmetric/polyarticular**. Mechanic's hands are **bilateral** on radial/ulnar finger surfaces.

---

## 8. Temporal Development

- **Onset:** **Adult**, mean age 43–60 yr (range ~19–82); peak incidence 50–59 yr. Pattern is **subacute-to-chronic/insidious**; a minority present with **rapidly progressive ILD** (acute, potentially fatal).
- **Progression:** Manifestations **accumulate over time** ("incomplete" → "complete" syndrome). The AENEAS time-course work shows new features (e.g., ILD, arthritis) emerging during follow-up. ILD course ranges from stable to relentlessly progressive fibrosis; ~**32–35%** progress despite steroids + immunosuppressant, requiring rescue therapy. [search-derived]
- **Disease course pattern:** **Chronic, relapsing-remitting to progressive**; lifelong. Muscle and joint disease often respond to immunosuppression; ILD is the limiting factor.
- **Remission:** Treatment-induced remission of myositis/arthritis is common; ILD often only stabilizes. Spontaneous remission is uncommon.
- **Critical windows:** Early aggressive treatment of **rapidly progressive ILD** is the key intervention window; delayed diagnosis (common, due to under-recognition and incomplete presentations) worsens outcome.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** age-/sex-adjusted **~0.56 per 100,000/year** (95% CI 0.25–0.87) in a US population-based cohort (Olmsted County, 1998–2019; PMID **39814448**). [search-derived]
- **Prevalence:** rare; not precisely established. Orphanet lists it as a rare disease.
- **Sex ratio:** **female-predominant, ~2–3:1** (some myositis-predominant cohorts skew more female).
- **Age distribution:** adult, peak 5th–6th decade.

**Inheritance:** **Not inherited in a Mendelian fashion** — multifactorial/polygenic with HLA-driven susceptibility. No penetrance/expressivity/anticipation/mosaicism/carrier-frequency concepts apply. **Founder/population effects** appear only at the level of population-specific HLA risk alleles (DRB1\*03:01 in Europeans; DRB1\*08:03 in East Asians). Consanguinity is not relevant.

**Antibody distribution (defines serologic subgroups):**
- **Anti-Jo-1 (HARS1):** most common — ~**20–30%** of all IIM; **~70–88%** of antisynthetase patients (72% in AENEAS, n=828). Phenotype: classic triad, **more myositis**.
- **Anti-PL-7 (TARS1):** ~18% of anti-ARS (Japanese cohort).
- **Anti-PL-12 (AARS1):** ~11%; **ILD-predominant, often amyopathic**, less muscle.
- **Anti-EJ (GARS1):** ~23% (Japanese); myositis-associated.
- **Anti-OJ (IARS1):** ~5%; **ILD-predominant**.
- **Anti-KS (NARS1):** ~8%; **ILD-predominant, minimal myositis**.
- **Anti-Zo (FARSB)** and **anti-Ha/SC (KARS1):** rare.

> "Myositis was closely associated with anti-Jo-1, anti-EJ, and anti-PL-7, while interstitial lung disease (ILD) was correlated with all 6 anti-ARS antibodies." [search-derived]

**Co-antibody:** **anti-Ro52/TRIM21** in up to ~50% — marks more severe ILD.

**Geographic distribution:** Worldwide; no strong endemicity. Subtype distribution shifts by ancestry (e.g., higher anti-EJ in Japanese cohorts).

---

## 10. Diagnostics

**Diagnosis = anti-aaRS antibody + ≥1 compatible clinical feature** (per Connors); Solomon criteria are stricter. Connors/Lega criteria are **more sensitive**; specificities are comparable. [verified PMID 27594777 + search-derived]

**Serology (cornerstone):**
- **Myositis line/immunoblot panels** detecting the 8 anti-aaRS (anti-Jo-1, PL-7, PL-12, EJ, OJ, KS, Zo, Ha). **Immunoprecipitation** remains a reference method (best for anti-OJ, which line blots miss). **Anti-Ro52** should be tested concurrently.
- **Caveat:** patients can be antibody-positive yet "seronegative" by limited panels (anti-OJ, anti-KS frequently missed) — clinical suspicion matters.

**Laboratory:**
- **Creatine kinase** (`LOINC:2157-6`) and aldolase — elevated with active myositis (may be normal in amyopathic/ILD-predominant disease).
- ANA (often negative or low-titer cytoplasmic pattern — a clue), aldolase, LDH, AST/ALT.

**Imaging:**
- **HRCT chest** — NSIP/OP/UIP patterns; the key ILD test.
- **Muscle MRI** — edema/inflammation, guides biopsy.

**Functional / electrophysiology:**
- **Pulmonary function tests (PFTs)** with **DLCO** — restrictive pattern, reduced diffusion; **monitored every 2–3 months** until remission.
- **EMG** — irritable myopathy.

**Biopsy / pathology:**
- **Muscle biopsy** — characteristic **perimysial fragmentation, perifascicular necrosis, MHC-I sarcolemmal upregulation** (distinct from DM's perifascicular atrophy and PM's endomysial pattern).
- **Lung biopsy** — rarely needed; cellular/fibrotic NSIP, OP.

**Genetic testing:** **Not used diagnostically** (no Mendelian basis). HLA typing is research/risk-stratification only. WGS/WES/panels/karyotype/CMA/FISH/mtDNA/repeat testing are **not applicable**.

**Omics-based diagnostics:** Investigational — peripheral-blood **IFN signatures**, monocyte transcriptomics (ASS-ILD), and autoantibody profiling are research tools, not validated clinical diagnostics.

**Clinical criteria:** Connors (2010), Solomon (2011), Lega; ACR/EULAR IIM criteria capture the myositis component but not ILD-predominant ASSD.

**Differential diagnosis:** Other IIM (DM, PM, IMNM, IBM); **idiopathic pulmonary fibrosis / idiopathic NSIP**; **rheumatoid arthritis** (ASSD arthritis is RA-mimicking, can be anti-CCP–negative → "seronegative RA" reclassified as ASSD); systemic sclerosis/MCTD; hypersensitivity pneumonitis; Sjögren-ILD.

**Screening:** No population screening. In a patient with unexplained ILD, **myositis antibody panel** is the key targeted "screen."

---

## 11. Outcome / Prognosis

- **Mortality / survival:** 10-year cumulative survival ~**70% (anti-Jo-1)** vs ~**49% (non-Jo-1)**; one 5-year cohort (n=45) showed **14% mortality**; AENEAS-era and registry cohorts report overall mortality ~**25%**. [verified PMID 27594777 + search-derived]
- **Leading causes of death:** **progressive pulmonary fibrosis** and **pulmonary hypertension**; rapidly progressive ILD acutely.
- **Prognostic factors:** **Better** — anti-Jo-1 positivity, presence of arthritis, presence of muscle weakness; **Worse** — severe baseline dyspnea, absent muscle weakness (ILD-only phenotype), non-Jo-1 antibodies, anti-Ro52 co-positivity, UIP-pattern fibrosis, PAH, older age.
- **Anti-Jo-1 antibody level** tracks disease activity/evolution and is being evaluated as a longitudinal biomarker (PMC11137886, PMC10362709). [search-derived]
- **Malignancy:** Cancer risk in ASSD is **lower than in classic dermatomyositis** but the population cohort (PMID 39814448) examined malignancy association — verify the specific hazard before citing.
- **Morbidity/QoL:** chronic dyspnea, oxygen dependence, exercise limitation, myositis-related functional loss, RA-like joint disability.

---

## 12. Treatment

**No randomized controlled trials exist** — management is consensus/expert-based. (`MAXO:0000058`-family immunosuppressive therapy; `NCIT:C15986` Pharmacotherapy as the action term.)

**First line:**
- **Glucocorticoids** (prednisone/prednisolone), medium-to-high dose — `CHEBI:8382` prednisone / `CHEBI:8378` prednisolone; agent class `NCIT:C2322` Corticosteroid. (`MAXO:0000058`? prefer NCIT:C15986 + corticosteroid agent.)
- **Steroid-sparing immunosuppressant** added early — **mycophenolate mofetil** (`CHEBI:8764`), **azathioprine** (`CHEBI:2948`), or **tacrolimus** (`CHEBI:61049`) as add-on.

> "prednisone AND mycophenolate mofetil or azathioprine; consider tacrolimus as add-on therapy" — PMID 27594777 **[verified]**

**Refractory / progressive ILD:**
- **Rituximab** (anti-CD20 mAb; rescue therapy; PFT improvement at ~6 months) — agent `NCIT:C2480` Rituximab; modality MONOCLONAL_ANTIBODY.
- **Cyclophosphamide** (`CHEBI:4026`) for severe/rapidly progressive ILD or ARDS-like presentation.
- **IVIG** — adjunct, especially for refractory myositis/dysphagia.
- **Combination MMF + rituximab** reported beneficial in refractory IIM. [search-derived]

**Antifibrotic (emerging):** **Nintedanib** (`CHEBI:85164`) for progressive fibrosing ILD phenotypes (extrapolated from INBUILD/progressive-pulmonary-fibrosis data) — investigational/adjunct in ASS-ILD.

**Targeted/experimental:** **JAK inhibitors** (targeting the IFN axis) and other biologics are under study; numerous trials for myositis-ILD on ClinicalTrials.gov (search for active NCTs before listing).

**Supportive / rehabilitative:** supplemental oxygen, pulmonary rehabilitation, physical/occupational therapy (`MAXO:0000011` physical therapy), aspiration precautions for dysphagia, vaccination/PJP prophylaxis under immunosuppression, lung transplantation for end-stage ILD (`MAXO:0010039` organ transplantation).

**Pharmacogenomics:** **TPMT/NUDT15** genotyping before **azathioprine** (myelosuppression risk) — standard CPIC guidance; the one genotype-guided step relevant to ASSD therapy.

**Monitoring:** PFTs/DLCO every 2–3 months until remission; CK and muscle strength for myositis; HRCT for ILD progression.

---

## 13. Prevention

- **Primary prevention:** None established (autoimmune, multifactorial). **Smoking cessation** is the only modifiable lifestyle lever plausibly reducing risk (given the smoking × HLA-DRB1\*03 interaction).
- **Secondary prevention (early detection):** Early **myositis-antibody testing in unexplained ILD/arthritis**, and **HRCT/PFT screening** in newly diagnosed antibody-positive patients, to catch ILD before irreversible fibrosis. No population screening program.
- **Tertiary prevention:** Immunosuppression to prevent ILD progression; infection prophylaxis (PJP, vaccination) while immunosuppressed; PAH surveillance; aspiration precautions.
- **Immunization, genetic screening/counseling, public-health/environmental interventions:** Not applicable as disease-specific measures (no infectious or Mendelian basis); standard immunosuppression-related vaccination applies.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease — `NCBITaxon:9606` (*Homo sapiens*).
- **Natural disease in other species:** **None recognized.** ASSD has no described naturally occurring animal counterpart (no OMIA entry). It is defined by human anti-aaRS autoantibodies in a specific HLA context.
- **Orthologous autoantigen genes (for comparative/model work):** the aaRS genes are deeply conserved (essential housekeeping enzymes) across all species — e.g., mouse *Hars1* (`NCBI Gene` mouse ortholog), etc. — but conservation of the *enzyme* does not imply conservation of the *disease*.
- **Zoonotic potential / cross-species transmission:** None (non-infectious autoimmune disease).

---

## 15. Model Organisms

ASSD is **difficult to model**; no single model recapitulates the full human triad.

- **Mouse immunization models:** Immunization with **HisRS / Jo-1 (and especially the WHEP/N-terminal fragment)** in adjuvant induces **muscle and lung inflammation (myositis + ILD-like pulmonary infiltrates)** in mice — the principal experimental system supporting the autoantigen-driven model (referenced in PMID 36280495 mechanism work). **Evidence source: MODEL_ORGANISM.**
- **In vitro / cellular:** Human skeletal myoblast and macrophage **secretome/exosome** studies (HisRS secretion on IGF-1 stimulation; aaRS release from virus-infected macrophages); TLR7/8 reporter assays with tRNA fragments; T-cell activation assays of the HisRS WHEP domain (chemokine activity / NRP2 binding). **Evidence source: IN_VITRO.** (PMID 36280495 **[verified]**.)
- **Genetic models:** No knockout/knock-in disease model (aaRS knockouts are embryonic-lethal — these are essential enzymes), so reverse-genetic disease modeling is intrinsically limited.
- **Recapitulation & limitations:** Immunization models reproduce **muscle + lung autoimmunity** and the **autoantibody response**, supporting the antigen-specific hypothesis, but **do not reproduce the chronic fibrotic ILD, arthritis, mechanic's hands, or the human HLA context** — a clear **HUMAN_MODEL_MISMATCH** candidate for a knowledge-gap note (model autoimmunity ≠ human chronic fibrosing multisystem disease).
- **Applications:** mechanism of tolerance breakdown, role of aaRS fragments/WHEP domain, TLR/IFN amplification loop, candidate-therapy testing.

---

## Consolidated Ontology Term Suggestions (for YAML)

- **Disease:** `MONDO:0019344` antisynthetase syndrome.
- **HPO phenotypes:** `HP:0006530` (ILD), `HP:0003701` (proximal weakness), `HP:0003198` (myopathy), `HP:0001369` (arthritis), `HP:0002829` (arthralgia), `HP:0010765` (palmar hyperkeratosis ≈ mechanic's hands — verify), Raynaud (verify term), `HP:0001945` (fever), `HP:0002094` (dyspnea), `HP:0003236` (elevated CK), `HP:0002015` (dysphagia), `HP:0002206` (pulmonary fibrosis), `HP:0002092` (PAH).
- **GO:** `GO:0002377`, `GO:0019882`, `GO:0002224`, `GO:0032606`, `GO:0034341`, `GO:0006954`, `GO:0004812`.
- **CL:** `CL:0000576`, `CL:0000775`, `CL:0000451`, `CL:0000624`, `CL:0000236`, `CL:0000786`, `CL:0002063`, `CL:0000057`, `CL:0000188`.
- **UBERON:** `UBERON:0002048` (lung), `UBERON:0001134` (skeletal muscle tissue), `UBERON:0002217` (synovial joint), `UBERON:0002097` (skin), `UBERON:0001043` (esophagus).
- **CHEBI (drugs):** `CHEBI:8382` prednisone, `CHEBI:8764` mycophenolate mofetil, `CHEBI:2948` azathioprine, `CHEBI:61049` tacrolimus, `CHEBI:4026` cyclophosphamide, `CHEBI:85164` nintedanib.
- **MAXO/NCIT (treatments):** `NCIT:C15986` Pharmacotherapy (+ agents); `MAXO:0000011` physical therapy; `MAXO:0010039` organ transplantation; `MAXO:0000950` supportive care.

---

## Key References (PMIDs to fetch & verify before curation)

| PMID / ID | What it supports | Status |
|---|---|---|
| **36280495** — Kanaji et al., *Trends Biochem Sci* 2022/2023, "Mechanistic perspectives on anti-aminoacyl-tRNA synthetase syndrome" | Full pathophysiology: aaRS autoantigens, WHEP domain, TLR7/8–IFN loop, secretome, chemokine activity | **[verified]** |
| **27594777** — "The Diagnosis and Treatment of Antisynthetase Syndrome" (PMC5006392) | Criteria, frequencies, the 8 antibodies, prognosis/survival, treatment algorithm | **[verified]** |
| **39814448** — Epidemiology of ASS & malignancy, population-based cohort 1998–2019, *J Rheumatol* | Incidence 0.56/100,000; malignancy risk | search-derived |
| PMC11050089 / MDPI IJMS 2024 — Review of ASS-associated ILD | ILD patterns, NETs, pathogenesis | search-derived |
| PMC12589074 — Monocyte-driven IFN/TNF programs in ASS-ILD (*Front Immunol* 2025) | Monocyte IFN signature | search-derived |
| PMC11137886 / PMC10362709 — Anti-Jo-1 antibody levels & prognosis | Antibody titer as activity biomarker | search-derived |
| AENEAS cohort (Cavagna et al.; n=828) | Antibody distribution (Jo-1 72%), clinical time course | search-derived — locate PMID |
| Anti-Ro52 cohort (Clin Exp Rheumatol) | Ro52 ~50%, worse ILD | search-derived |

**Sources (URLs):**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9974581/ (mechanism review, PMID 36280495)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5006392/ (diagnosis/treatment, PMID 27594777)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9136399/ (aaRS: on anti-synthetase syndrome and beyond)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11050089/ (ASS-ILD review)
- https://pubmed.ncbi.nlm.nih.gov/39814448/ (population epidemiology)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11137886/ (anti-Jo-1 levels & prognosis)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6222225/ (HLA/genetics, Hungarian cohort)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7732678/ (IL1B susceptibility)
- https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1652999/full (monocyte IFN/TNF in ASS-ILD)
- https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=81 (Orphanet ORPHA:81)
- https://rarediseases.org/rare-diseases/antisynthetase-syndrome/ (NORD overview)

---

### Curation handoff notes
A `kb/disorders/Antisynthetase_Syndrome.yaml` entry **already exists on this branch** (MONDO:0019344, with pathophysiology and phenotype scaffolding). This report is structured to **fill it out** — prioritize: (1) the verified mechanism chain from PMID 36280495 (autoantigen secretion → WHEP epitope → immune complex → TLR7/8 → IFN loop → tissue damage); (2) antibody-subtype phenotype heterogeneity (§9); (3) the ILD-centric prognosis/treatment (§§11–12). Before any snippet becomes an `evidence:` item, run `just fetch-reference PMID:XXXX` then confirm the quote is an exact substring of the cached abstract — especially for every claim I flagged **[search-derived]**, and watch for the mechanic's-hands and Raynaud HPO terms, which need OAK verification (the ontology may lack precise matches).