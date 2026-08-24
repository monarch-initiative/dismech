---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T13:57:36.950031'
end_time: '2026-08-01T14:20:51.065203'
duration_seconds: 1394.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SNF8-Related Neurodevelopmental Disorder
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
  web_search_requests: 5
  num_turns: 83
  total_cost_usd: 4.385810749999999
  session_id: 1630eae9-1a04-4066-8ddd-cff7da916933
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SNF8-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SNF8-Related Neurodevelopmental Disorder** covering all of the
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

All terms verified. Writing the report.

---

# Research Report: SNF8-Related Neurodevelopmental Disorder

**Prepared:** 2026-08-01 · **Target:** `SNF8-Related Neurodevelopmental Disorder` · **Category:** Mendelian

> ## ⚠️ Critical framing note for curators — read first
>
> **This is an ultra-rare, single-publication disease entity.** The entire clinical and mechanistic literature rests on **one paper**: Brugger M, Lauri A, Zhen Y, et al. *Bi-allelic variants in SNF8 cause a disease spectrum ranging from severe developmental and epileptic encephalopathy to syndromic optic atrophy.* Am J Hum Genet. 2024 Mar 7;111(3):594–613. **PMID:38423010**, DOI 10.1016/j.ajhg.2024.02.005, PMC10940020.
>
> I ran targeted PubMed date-bounded searches (2024–2026) and confirmed **no follow-up cohort expansion, case report, or replication cohort exists as of August 2026**. The other 27 PubMed records matching "SNF8" in title/abstract are yeast/fungal genetics, GWAS incidental hits (chicken carcass traits, psoriasis, fatigue, insomnia-cardiac pleiotropy), MASH biomarker panels, and a protein-disorder prediction methods paper — **none concern this human disease**. Total published cohort worldwide: **N=9 individuals from 6 families.**
>
> **Therefore, for Sections 2 (risk/protective factors), 5 (environment), 11 (survival statistics), 12 (treatment), 13 (prevention), and 14 (other species), most requested content genuinely does not exist.** I state this explicitly per-section rather than padding with plausible-sounding generalities. Please do not let a downstream curation pass "fill in" these gaps from disease-class priors.
>
> **NEC (Named Entity Confusion) preflight — PASSED.** `SNF8` is a high-risk name (it is a long-established *S. cerevisiae* gene, and the human gene sits in a GWAS-dense locus `UBE2Z-GIP-ATP5G1-SNF8`). I verified both MONDO entities resolve to the same causal gene and matching OMIM xrefs:
> - `MONDO:0968946` → OMIM:620783 (DEE115) → SNF8 ✅
> - `MONDO:0968947` → OMIM:620784 (NEDOA) → SNF8 ✅
>
> **Ontology term verification status:** every HP, GO, CL, UBERON, and MONDO ID in this report was verified live against the JAX HPO API or EBI OLS4 during this session, and labels below are the **canonical labels returned**. NCIT suggestions are drawn from the authoritative in-repo list in `CLAUDE.md` and are flagged where OAK verification is still required.

---

## 1. Disease Information

### Overview

SNF8-related neurodevelopmental disorder is an **autosomal recessive allelic spectrum** caused by bi-allelic loss-of-function variants in *SNF8*, which encodes one of three subunits of the **ESCRT-II** complex (Endosomal Sorting Complex Required for Transport II). The disorder was delineated in 2024 and spans a strikingly wide severity range that OMIM has split into **two separate phenotype entries**:

| Pole | Phenotype | OMIM | MONDO | Character |
|---|---|---|---|---|
| **Severe** | Developmental and epileptic encephalopathy 115 (DEE115) | **620783** | **MONDO:0968946** | Congenital onset, neurodevelopmental arrest, epileptic encephalopathy, massive white-matter loss, corpus callosum hypo-/aplasia, death in infancy |
| **Mild** | Neurodevelopmental disorder plus optic atrophy (NEDOA) | **620784** | **MONDO:0968947** | Mild ID (speech/language predominant), childhood-onset optic atrophy, or ataxia; survival into adulthood |

The verbatim framing from the defining paper (PMID:38423010, quotable snippet):

> "We report nine individuals from six families presenting with a spectrum of neurodevelopmental/neurodegenerative features caused by bi-allelic variants in SNF8 (GenBank: NM_007241.4), encoding the ESCRT-II subunit SNF8."

> "The phenotypic spectrum included four individuals with severe developmental and epileptic encephalopathy, massive reduction of white matter, hypo-/aplasia of the corpus callosum, neurodevelopmental arrest, and early death. A second cohort shows a milder phenotype with intellectual disability, childhood-onset optic atrophy, or ataxia."

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO (severe)** | MONDO:0968946 — *developmental and epileptic encephalopathy 115* ✅ verified OLS4 |
| **MONDO (mild)** | MONDO:0968947 — *neurodevelopmental disorder plus optic atrophy* ✅ verified OLS4 |
| **OMIM phenotype** | 620783 (DEE115); 620784 (NEDOA) |
| **OMIM gene** | 610904 (*SNF8 SUBUNIT OF ESCRT-II*) |
| **MedGen** | 1858870 (DEE115); 1859522 (NEDOA) |
| **UMLS** | C5935604 (DEE115); C5935605 (NEDOA) |
| **GARD** | 0027033 (DEE115) |
| **Orphanet** | **No ORPHA code assigned** as of Aug 2026 (verified: no `ORPHA_*` cache entry mentions SNF8; Orphanet gene query returned no disorder) |
| **ICD-10 / ICD-11** | No specific code. Map pragmatically: ICD-10 `G40.4` (other generalized epilepsy/epileptic syndromes) or `Q04.0` (congenital malformations of corpus callosum) for the severe pole; `H47.2` (optic atrophy) + `F7x` for the mild pole. **No disease-specific code exists.** |
| **MeSH** | No disease-specific descriptor. MEDLINE indexing for PMID:38423010 uses: *Optic Atrophy/genetics*, *Epilepsy, Generalized*, *Endosomal Sorting Complexes Required for Transport/genetics*, *Phenotype*, *Zebrafish/genetics* |

### Synonyms / alternative names

- SNF8-related neurodevelopmental disorder (umbrella term; **used as this entry's name**)
- Developmental and epileptic encephalopathy 115 / **DEE115** (severe pole)
- Neurodevelopmental disorder plus optic atrophy / **NEDOA** (mild pole)
- SNF8-related ESCRT-II deficiency
- *Gene-level aliases relevant to literature searching:* **EAP30**, **VPS22**, **Dot3** (searching "VPS22" and "EAP30" retrieves the cell-biology literature that does not use the symbol SNF8)

### Evidence provenance type

**Aggregated disease-level, case-series derived.** All content originates from deep-phenotyped individual case descriptions in a single multi-center research collaboration (Munich, Leipzig, Rome, Bologna, Jerusalem, Ulm, Oslo, Nürnberg), plus structured secondary curation in OMIM, ClinVar, MONDO, and Genomics England PanelApp. **No EHR-derived, registry, or population-cohort data exist.**

---

## 2. Etiology

### Disease causal factors

**Monogenic, fully genetic.** The sole established cause is **bi-allelic (homozygous or compound-heterozygous) loss-of-function variation in *SNF8***. There is no known environmental, infectious, or multifactorial contribution.

The pathogenic principle is **quantitative loss of the ESCRT-II holocomplex**, not merely loss of SNF8 alone. SNF8 is structurally obligatory for complex integrity, so its depletion co-depletes its partners:

> "SNF8 as well as the two physically interacting subunits of ESCRT-II, VPS36, and VPS25 were significantly decreased" (PMID:38423010, patient-derived fibroblasts, individual A2)

Measured fold-changes vs. controls in severe-phenotype fibroblasts: **SNF8 0.25** (p=7.8×10⁻¹⁵), **VPS36 0.39** (p=0.003), **VPS25 0.37** (p=0.005).

### Genetic risk factors

- **Causal variants:** see Section 4. Seven distinct variants across 6 families.
- **Susceptibility loci / GWAS:** **None for this disease.** ⚠️ Caution: *SNF8* appears in GWAS hits for type 2 diabetes, coronary artery disease, psoriasis, fatigue, and insomnia-cardiac pleiotropy (PMIDs 25469308, 41824857, 40055680, 40176577). These reflect the **gene-dense 17q21.32 locus** (`UBE2Z-GIP-ATP5G1-SNF8`) and linkage disequilibrium, **not** relevance to the Mendelian disorder. Do not curate these as risk factors.
- **Modifier genes:** **None identified.** See Section 4 for discussion of why a modifier is *hypothesized* but unproven.
- **Consanguinity:** The one homozygous family (Family C, Israeli/Jerusalem, c.623G>T homozygous) is consistent with — but not explicitly reported as — consanguinity. The paper describes families as unrelated to each other; **within-family consanguinity is not explicitly stated.** Do not assert it.

### Environmental risk factors

**None known or plausible.** No toxin, exposure, lifestyle, occupational, or age/sex risk factor has been reported or is mechanistically implicated. Parental age effects are not applicable (recessive inheritance, not de novo).

### Protective factors

**None identified.** No protective variant, modifier allele, dietary, or lifestyle factor is known.

**However, one genuinely important population-genetic observation exists** — and it is the single most curation-relevant nuance in this section:

> "one apparently healthy individual from the gnomAD population" carries the c.304G>A (p.Val102Ile) variant **homozygously** (PMID:38423010)

This means the hypomorphic p.Val102Ile allele in the homozygous state is **not fully penetrant**, implying an unidentified modifier, threshold effect, or ascertainment/phenotyping gap. This is a **`KNOWLEDGE_GAP` discussion candidate**, and arguably the most important open question for the entry.

### Gene–environment interactions

**None reported.** No GxE data exist. CTD/PheGenI contain no SNF8 GxE records for this phenotype.

---

## 3. Phenotypes

### Cohort structure (essential context for all frequencies below)

**N=9 total individuals, 6 families.** Frequencies are near-meaningless as percentages at this N — I report **exact counts** and give `FrequencyEnum` bands only where the count clearly supports one. Per `docs/frequency-evidence-guidelines.md`, **I recommend omitting `frequency:` on most phenotypes** and recording counts in `description`/`notes` instead.

| ID | Sex | Genotype | Pole | Outcome |
|---|---|---|---|---|
| A1 | F | p.Tyr167Ter / p.Gly191Asp | Severe | **Died 8 mo** — cardiac arrest during status epilepticus |
| A2 | F | p.Tyr167Ter / p.Gly191Asp | Severe | **Died 3 mo** — respiratory infection (dysphagia-related); **autopsy performed** |
| B1 | M | p.Pro79Leu / p.Gly191Asp | Severe | Alive at 4.5 y |
| C1 | M | (Family C, homozygous c.623G>T) | Severe | **Terminated at 25 weeks' gestation** for brain malformations |
| C2 | F | p.Arg208Leu homozygous | Severe | **Died 9 wk** — respiratory infection (dysphagia-related) |
| D1 | M | c.423−1G>C / **p.Val102Ile** | Mild (NEDOA) | Alive at 18 y |
| E1 | M | p.Asp225TrpfsTer99 / **p.Val102Ile** | Mild (NEDOA) | Alive at 27 y |
| E2 | M | p.Asp225TrpfsTer99 / **p.Val102Ile** | Mild (NEDOA) | Alive at 17 y |
| F1 | F | p.Pro79Leu / **p.Val102Ile** | Mild (ataxia variant) | Alive at 4 y |

**Sex ratio:** 5 M : 4 F — consistent with autosomal inheritance, no sex bias.

### Severe pole (DEE115) — phenotype table

| Phenotype | HPO term (✅ label verified) | Count | Onset | Severity | Course |
|---|---|---|---|---|---|
| Epileptic encephalopathy | **HP:0200134** Epileptic encephalopathy | 2/4 (A1, B1) | ~7–9 mo | Severe | Progressive |
| Hypsarrhythmia on EEG | **HP:0002521** Hypsarrhythmia | A1, B1 | Infantile | Severe | Progressive |
| Neurodevelopmental arrest / stagnation | **HP:0007281** Developmental stagnation | 4/4 | Congenital | Profound | Static-arrested |
| Global developmental delay | **HP:0001263** Global developmental delay | 4/4 | Congenital | Profound | Progressive |
| Hypotonia | **HP:0001252** Hypotonia | 4/4 | Congenital/neonatal | Severe | Later → spasticity |
| Spastic tetraplegia | **HP:0002510** Spastic tetraplegia | A1, B1 (late) | Infantile | Severe | Progressive |
| Dysphagia | **HP:0002015** Dysphagia | 4/4 | Congenital | Severe | Persistent |
| *(Gastrostomy/PEG required)* | *management, not phenotype* | 3/4 | Infantile | — | — |
| Leukoencephalopathy | **HP:0002352** Leukoencephalopathy | 4/4 | Congenital | Severe | **Progressive** |
| Cerebral atrophy | **HP:0002059** Cerebral atrophy | 4/4 | Early | Severe | **Progressive** |
| Hypoplasia of the corpus callosum | **HP:0002079** Hypoplasia of the corpus callosum | 4/4 (hypo- or aplasia) | Congenital | Severe | Static |
| Nystagmus | **HP:0000639** Nystagmus | A1, B1 | Infantile | — | — |
| Death in infancy | **HP:0001522** Death in infancy | 3/4 | 9 wk – 8 mo | — | — |

**Note on intellectual disability in the severe pole:** *not formally assessable* due to neurodevelopmental arrest and early death. Do **not** curate `HP:0001249` for the severe pole — curate `HP:0007281`/`HP:0001263` instead. This is a real curation trap.

### Mild pole (NEDOA + ataxia variant) — phenotype table

| Phenotype | HPO term (✅ verified) | Count | Onset | Severity | Course |
|---|---|---|---|---|---|
| **Optic atrophy** | **HP:0000648** Optic atrophy | **3/3** (D1, E1, E2); absent in F1 | **4–7 y** (childhood) | Moderate–severe | **Progressive/degenerative** |
| Intellectual disability | **HP:0001249** Intellectual disability | 4/4 (D1, E1, E2, F1) | Childhood | **Mild** | Static |
| — *speech/language predominant* | **HP:0000750** Delayed speech and language development ⚠️ *verify* | 4/4 | Childhood | Mild | Static |
| Nystagmus | **HP:0000639** Nystagmus | 3/3 | Childhood | — | — |
| Reduced visual acuity | **HP:0007663** Reduced visual acuity | 3/3 | Childhood | Moderate | Progressive |
| Optic nerve hypoplasia | **HP:0000609** Optic nerve hypoplasia | Family C (fetal, "bilateral hypoplastic optic nerves") | Congenital | Severe | — |
| **Ataxia** | **HP:0001251** Ataxia ⚠️ *verify* | **1/1 (F1 only)** — "congenital ataxia" | **Congenital** | Mild | Static |
| Cerebellar atrophy | **HP:0001272** Cerebellar atrophy | F1 (slight); D1/E1 by volumetry | Early childhood | Mild | — |
| Developmental regression | **HP:0002376** Developmental regression | Not reported | — | — | — |
| Seizures | **HP:0001250** Seizure ⚠️ *verify* | **0/4 — absent** | — | — | Curate as **`supports: REFUTE`** or omit |

**Important:** ataxia is **F1 only** — a single individual. The paper's abstract phrase "intellectual disability, childhood-onset optic atrophy, **or** ataxia" is a disjunction across the mild cohort, not a triad in each patient. Do not curate ataxia as a general feature of NEDOA. F1 also had **no optic atrophy** and a **normal anterior optic tract** on MRI at age 2.

### Neuroimaging phenotype detail

**Severe pole:**
- "Pronounced and progressive white matter atrophy of the cerebrum"
- "Hypo- or aplasia of the corpus callosum beginning at a very early age"
- Pachygyria (A2) → suggest **HP:0001302** Pachygyria ⚠️ *verify*
- "Rapidly progressive enlargement of the lateral ventricles due to cerebral white matter loss" → **HP:0002119** Ventriculomegaly ⚠️ *verify*
- **Cerebellum "less severely affected"; brainstem "comparatively normal"** — a useful discriminating feature vs. pontocerebellar hypoplasia (see §10 differential)

**Mild pole (quantitative volumetry — unusually rich for such a small cohort):**
- "Severe volume reduction of the intracranial anterior optic pathway including optic nerves (ON), optic chiasma (OC), and optic tracts (**2 SD below normal values**)"
- D1: cerebral white matter **−17%** bilateral; cerebellar cortex −13% L / −21% R; cerebellar mean diffusivity **+13%** bilateral
- E1: white matter **−20%** bilateral; temporal cortex −17%; cerebellar cortex −19% L / −17% R; putamen −18% L / −17% R; cerebellar MD +9% L / +8% R
- Slight parieto-occipital white-matter hyperintensity
- F1 (age 2): **normal myelination and white matter volume**, slightly dysmorphic callosal body, slight cerebellar atrophy

The increased cerebellar **mean diffusivity** alongside cortical volume loss is a microstructural signature worth capturing — it supports a *degenerative* rather than purely *dysplastic* reading of the mild pole.

### Quality-of-life impact

**No formal QoL instrument (EQ-5D, SF-36, PROMIS, PedsQL) was administered.** No published QoL data exist. Qualitative inference only:

- **Severe pole:** profound impact — no developmental milestones achieved, gastrostomy dependence, palliative trajectory, death in infancy in 3/4. Total care dependency.
- **Mild pole:** moderate impact — progressive low vision from childhood (educational and occupational consequence), mild ID predominantly affecting speech/language, independent survival into adulthood (to at least 27 y).

Curate as `notes`, **not** as evidenced QoL claims.

---

## 4. Genetic / Molecular Information

### Causal gene

| Field | Value |
|---|---|
| **Symbol** | *SNF8* |
| **HGNC** | **hgnc:17028** (note lowercase prefix per repo convention) |
| **Approved name** | SNF8 subunit of ESCRT-II |
| **Aliases** | EAP30, VPS22, Dot3 |
| **Previous symbol** | SNF8, ESCRT-II complex subunit, homolog (S. cerevisiae) |
| **Locus** | **17q21.32** |
| **NCBI Gene** | 11267 |
| **Ensembl** | ENSG00000159210 |
| **UniProt** | **Q96H20** (Vacuolar-sorting protein SNF8; 258 aa) |
| **OMIM gene** | 610904 |
| **RefSeq transcript** | **NM_007241.4** (the reference transcript used in the paper and ClinVar) |

### Pathogenic variants — complete published set (7 variants)

All ✅ confirmed in ClinVar under condition "SNF8-associated disease."

| cDNA (NM_007241.4) | Protein | Type | ClinVar germline classification | Families |
|---|---|---|---|---|
| c.501C>A | p.Tyr167Ter | **Nonsense** | **Pathogenic** (VCV002664478) | A |
| c.572G>A | p.Gly191Asp | Missense | **Pathogenic** (VCV002664479) | A, B |
| c.236C>T | p.Pro79Leu | Missense | **Pathogenic** (VCV002664480) | B, F |
| c.623G>T | p.Arg208Leu | Missense | **Pathogenic** (VCV002664481) | C (**homozygous**) |
| c.423−1G>C | p.? | **Splice acceptor** | **Pathogenic** (VCV002664482) | D |
| c.673_683delinsTGGA | p.Asp225TrpfsTer99 | **Frameshift (indel)** | **Pathogenic** (VCV002664483) | E |
| **c.304G>A** | **p.Val102Ile** | Missense — **hypomorphic** | ⚠️ **Conflicting** (VCV002664484) | **D, E, F** |

### The p.Val102Ile hypomorphic allele — the genotype–phenotype linchpin

This is the single most important genetic fact in the entry:

> "All mildly affected individuals shared the same hypomorphic variant, c.304G>A (p.Val102Ile)." (PMID:38423010)

**Every one of the four mildly affected individuals (D1, E1, E2, F1) carries p.Val102Ile in *trans* to a more damaging allele.** The severe pole comprises genotypes combining two non-p.Val102Ile alleles. This is a clean, near-deterministic allelic dosage model: **residual ESCRT-II function determines pole**.

Population and annotation data:

| Field | Value |
|---|---|
| **GRCh38 coordinate** | chr17:48937065 |
| **dbSNP** | **rs200399045** |
| **gnomAD (overall)** | **0.00015** |
| **gnomAD exomes** | 0.00018 |
| **TOPMed** | 0.00015 |
| **1000 Genomes** | 0.00020 |
| **ExAC** | 0.00012 |
| **ESP** | 0.00015 |
| **Homozygotes in gnomAD** | **1 apparently healthy individual** ⚠️ |

**ClinVar submitter disagreement (curate this honestly):**
- **Institute of Human Genetics Munich** (2023-12-07): **Pathogenic** for SNF8-associated disease
- **Ambry Genetics** (2024-01-30): **Uncertain significance** — "insufficient or conflicting evidence"
- **OMIM** (2024-04-10): **Pathogenic** for neurodevelopmental disorder plus optic atrophy

The Ambry VUS call is defensible: AF ~1.5×10⁻⁴ with a healthy homozygote is unusual for a fully pathogenic allele. Recommend curating p.Val102Ile with an explicit note on the conflicting classification and reduced penetrance — **not as unqualified "Pathogenic."**

### In silico support (from PMID:38423010)

- **CADD** for the pathogenic missense variants: **27.3 – 33.0**
- **REVEL:** **0.683 – 0.953**
- All variants "affected residues that were spotted in regions documented to be intolerant to variation"
- p.Val102Ile showed "less disruptive impact" by in silico prediction — concordant with its hypomorphic behavior

### Functional consequences — mechanism class

**Loss of function**, acting through two mechanistically *distinct* routes — an important subtlety:

1. **Protein-destabilizing LoF (severe alleles):** truncating/frameshift/splice and severe missense alleles reduce SNF8 protein, which **co-destabilizes VPS36 and VPS25**, collapsing the ESCRT-II holocomplex. Confirmed by quantitative proteomics (fold changes above).

2. **Stability-independent LoF (p.Val102Ile):** In the mild-phenotype fibroblasts (D1, E1), SNF8 reduction was **not statistically significant** (D1: 0.74; E1: 0.68) and **VPS36/VPS25 were not significantly reduced**. The authors conclude the variant:
   > "acts via a distinct mechanism independent of protein stability"

**No gain-of-function or dominant-negative mechanism is reported.** Heterozygous carriers (parents) are unaffected.

### gnomAD constraint metrics

⚠️ **Not retrieved.** The gnomAD GraphQL API was not reachable from this environment (sandbox network restriction) and the gnomAD gene page is a client-rendered JS app that WebFetch cannot resolve. **pLI, o/e LoF, mis_z, and LoF observed/expected for *SNF8* are therefore NOT reported here — do not populate these fields from memory.** Retrieve them directly from https://gnomad.broadinstitute.org/gene/ENSG00000159210 before curating any constraint claim.

### Modifier genes

**None identified.** A modifier is *implied* by the healthy gnomAD p.Val102Ile homozygote and by the intra-mild-cohort divergence (F1: ataxia, no optic atrophy; D1/E1/E2: optic atrophy, no ataxia — despite all four sharing p.Val102Ile). Curate as a `KNOWLEDGE_GAP` discussion, not as a finding.

### Epigenetic information

**None.** No methylation episignature, chromatin, or histone-modification data exist for SNF8-related disease. ⚠️ *Note a potential confusion source:* CHMP1A (a different ESCRT-III gene) has documented chromatin-regulatory function (PMID:23023333) — this does **not** transfer to SNF8.

### Chromosomal abnormalities

**None causal.** Three ClinVar records retrieved in the SNF8 gene query (VCV003242218, VCV003242217, VCV002692407) are **large multi-gene deletions** spanning the 17q21.32 region — they are not SNF8-specific and should **not** be curated as causing this disorder. No recurrent CNV, translocation, or inversion mechanism is known.

---

## 5. Environmental Information

**Not applicable — no environmental contribution is known or hypothesized.**

- **Environmental factors:** None. CTD contains no SNF8–chemical–disease association for this phenotype.
- **Lifestyle factors:** None.
- **Infectious agents:** **None causal.** ⚠️ *Important distinction for curators:* the recurrent **respiratory infections** that caused death in A2 and C2 are a **downstream complication of dysphagia and aspiration** (i.e., a consequence of the phenotype), **not** an etiologic or triggering agent. Curate them as complications in Section 11, never as an infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Causal chain (proposed pathograph, upstream → downstream)

```
[MOLECULAR] Bi-allelic SNF8 LoF variants
      ↓
[MOLECULAR] Reduced SNF8 protein → co-destabilization of VPS36 + VPS25
            = loss of the ESCRT-II holocomplex
      ↓
[MOLECULAR/CELLULAR] Impaired ESCRT-II → ESCRT-III handoff;
            defective MVB biogenesis + cargo-selective endosomal sorting
      ↓
[CELLULAR] Mis-sorting of lysosomal hydrolases to the (auto)lysosome
      ↓
[CELLULAR] Accumulation of autolysosomes + morphologically aberrant lysosomes
            (enlarged, electron-lucent lumen)
      ↓
[CELLULAR] IMPAIRED AUTOPHAGIC FLUX  ← the convergent hub node
      ↓
[CELLULAR] LC3 accumulation in cortical pyramidal neurons and reactive astrocytes
      ↓
[TISSUE] Myelin loss, reactive gliosis, microglial activation;
         retinal ganglion cell / optic nerve degeneration
      ↓
[TISSUE] Leukoencephalopathy + cerebral atrophy; optic pathway volume loss
      ↓
[ORGANISM] Severe pole: DEE, neurodevelopmental arrest, early death
           Mild pole:   mild ID + childhood-onset optic atrophy / ataxia
```

**Author's own summary of the terminal mechanism (quotable):**

> "Taken together, we conclude that loss of ESCRT-II due to bi-allelic SNF8 variants is associated with a spectrum of neurodevelopmental/neurodegenerative phenotypes mediated likely via impairment of the autophagic flux." (PMID:38423010)

Note the hedge — **"likely via"**. Autophagic-flux impairment is the authors' *preferred hypothesis*, well-supported in fibroblasts and neuropathology but **not proven to be the proximate cause of the neurological phenotype in vivo**. Curate the terminal edge with `status: EMERGING` in a `mechanistic_hypotheses` block rather than as established fact.

### Molecular pathways

**ESCRT / MVB pathway (the core).** ESCRT-II is the bridging complex between ubiquitin-cargo recognition (ESCRT-0/I) and membrane scission (ESCRT-III/VPS4).

Structural basis (yeast core, PMID:15329733, Nature 2004 — quotable):
> "Here we report the crystal structure of the core of the yeast ESCRT-II complex, which contains one molecule of the Vps protein Vps22, the carboxy-terminal domain of Vps36 and two molecules of Vps25, and has the shape of a capital letter 'Y'. The amino-terminal coiled coil of Vps22 and the flexible linker leading to the ubiquitin-binding NZF domain of Vps36 both protrude from the tip of one branch of the 'Y'."

Note: **Vps22 = SNF8**. The 1:1:2 stoichiometry (Vps22 : Vps36 : Vps25₂) explains mechanistically why losing SNF8 collapses the whole complex.

ESCRT-II→III coupling (PMID:15469844, Dev Cell 2004 — quotable):
> "We show that purified ESCRT-II binds directly to the Vps20 component of ESCRT-III. Surprisingly, this binding does not require the protruding N-terminal coiled-coil of Vps22. Vps25 is the chief subunit responsible for Vps20 recruitment. This interaction dramatically increases binding of both components to lipid vesicles in vitro."

Human ESCRT-II structures: **PDB 2ZME**, **PDB 3CUQ** (2.6 Å and 2.9 Å) — three lobes, one copy each of VPS22/VPS36, two copies of VPS25.

**Pathways NOT implicated:** no evidence for Wnt, MAPK, mTOR, or PI3K-AKT involvement in *this* disease. Do not import these from generic NDD priors.

### Cellular processes

- Macroautophagy / autophagic flux (**the central process**)
- Multivesicular body biogenesis
- Endosomal cargo sorting; late endosome → lysosome transport
- Lysosomal biogenesis / hydrolase delivery
- Neural progenitor proliferation (zebrafish: ectopic pH3+ cells in forebrain)
- Axon outgrowth/pathfinding (optic nerve extension, optic chiasm formation)
- Reactive gliosis and microglial activation

### Cargo selectivity — a mechanistically important negative result

> "EGFR degradation was not detectably impaired in patient-derived fibroblasts as compared to fibroblasts from control individuals." (PMID:38423010)

This is significant: EGFR downregulation is *the* canonical ESCRT-dependent readout, yet it was **preserved**. The authors attribute this to residual ESCRT-II function and **cargo specificity** — different cargoes have different ESCRT-II dependency thresholds. Curate this as `supports: PARTIAL` or as a REFUTE-flavored evidence item against a "global ESCRT collapse" model. It argues for a *selective*, threshold-dependent defect, which in turn helps explain the mild pole.

### Protein dysfunction

SNF8/Q96H20: 258 aa; coiled-coil at residues **27–53**; multiple winged-helix repeats (the entire ESCRT-II core is built from **eight winged-helix domains**, PMID:15469844). Two isoforms via alternative splicing. Interacts with VPS25, VPS36, TSG101, RILPL1, and 14-3-3 proteins.

Mechanism is **loss of function via complex destabilization** (severe alleles) or **stability-independent functional impairment** (p.Val102Ile). No misfolding/aggregation proteinopathy is described.

### Metabolic changes

**None established.** ⚠️ **Curation trap:** PMID:38423010 mentions "mitochondrial complex III deficiency, nuclear type 1" (MIM 124000, *BCS1L*) **only as a separate, unrelated individual** retrieved from the same in-house diagnostic database. **There is no mitochondrial or complex III defect in SNF8-related disease.** No lactate, CSF, or respiratory-chain enzyme abnormality was reported. Do not curate any metabolic/mitochondrial finding.

### Immune system involvement

**No primary immune involvement.** Neuroinflammation is **secondary**: reactive astrogliosis and microglial activation on autopsy. No autoimmunity, no immunodeficiency.

### Tissue damage mechanisms

Autophagic-lysosomal dysfunction → neuronal and oligodendroglial/myelin injury → demyelination and white-matter loss with reactive gliosis. Optic pathway: retinal ganglion cell / optic nerve degeneration (a classic autophagy-vulnerable, long-axon, high-metabolic-demand neuronal population — the same vulnerability class as OPA1/mitochondrial optic neuropathies). No ischemic, fibrotic, or oxidative-stress mechanism is documented.

### Biochemical abnormalities

No enzyme deficiency, receptor, ion-channel, or transporter defect. The defect is in **vesicular trafficking machinery**, not catalysis.

### Epigenetic changes

**None reported.**

### Molecular profiling

- **Proteomics** ✅ — quantitative proteomics on patient fibroblasts is the key functional dataset (SNF8/VPS36/VPS25 fold changes above). Modality: `IN_VITRO`.
- **Transcriptomics** — none.
- **Metabolomics / lipidomics** — none.
- **Single-cell / spatial transcriptomics** — none.
- **Multi-omics integration** — none.
- **Functional genomics (CRISPR/RNAi screens)** — ⚠️ Not retrieved. DepMap was inaccessible (bot-verification wall). **Do not assert SNF8 essentiality status without checking https://depmap.org/portal/gene/SNF8 directly.** *Contextual note only:* the IMPC mouse homozygous-null preweaning-lethal phenotype (§15) is consistent with a fitness-critical gene, but that is not the same claim as DepMap common-essentiality.

### Suggested GO terms (✅ all verified live)

**Biological process**
| GO ID | Label |
|---|---|
| **GO:0036258** | multivesicular body assembly |
| **GO:0016236** | macroautophagy |
| **GO:0061919** | process utilizing autophagic mechanism |
| **GO:0032456** | endocytic recycling |
| **GO:0043328** | protein transport to vacuole involved in ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway |

**Cellular component**
| GO ID | Label |
|---|---|
| **GO:0000814** | ESCRT II complex |
| **GO:0010008** | endosome membrane |
| **GO:0031902** | late endosome membrane |
| **GO:0044754** | autolysosome |

**Molecular function**
| GO ID | Label |
|---|---|
| **GO:0042803** | protein homodimerization activity |
| **GO:0008289** | lipid binding |

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:** central nervous system — cerebrum (white matter predominant), corpus callosum, anterior visual pathway, cerebellum (mild/variable).
**Secondary:** respiratory tract (aspiration pneumonia from dysphagia); GI (feeding failure → gastrostomy); cardiac (terminal arrest during status epilepticus in A1 — an agonal event, not primary cardiac disease).
**Body systems:** nervous (primary), visual/special sense (primary), respiratory + digestive (secondary).

**Notably spared:** brainstem ("comparatively normal"), and no reported hepatic, renal, hematologic, or skeletal involvement. This *sparing pattern* is diagnostically useful — it distinguishes SNF8 from the multisystem ESCRT disorder CIMDAG (*VPS4A*), which features cataracts, anemia, and growth impairment.

### Suggested UBERON terms (✅ verified — note label subtleties)

| UBERON ID | **Canonical label (use this in `term.label`)** | Suggested `preferred_term` |
|---|---|---|
| UBERON:0000955 | brain | brain |
| UBERON:0002316 | white matter ⚠️ *verify* | cerebral white matter |
| UBERON:0002336 | corpus callosum ⚠️ *verify* | corpus callosum |
| **UBERON:0000941** | **cranial nerve II** ✅ *verified* | **optic nerve** ← label ≠ common name; do not write "optic nerve" in `term.label` |
| **UBERON:0000959** | **optic chiasma** ✅ *verified* | optic chiasm |
| UBERON:0000966 | retina ⚠️ *verify* | retina |
| UBERON:0002037 | cerebellum ⚠️ *verify* | cerebellum |
| UBERON:0000956 | cerebral cortex ⚠️ *verify* | cerebral cortex |
| UBERON:0001890 | forebrain ⚠️ *verify* | forebrain |

`UBERON:0000941` is a genuine trap — its canonical label is **"cranial nerve II"**, so `term.label: optic nerve` would fail `just validate-terms`. Use `preferred_term: optic nerve` with `term.label: cranial nerve II`.

### Tissue and cell level

Affected tissue types: nervous tissue (neurons, glia), myelinated white-matter tracts.

### Suggested CL terms

| CL ID | Label | Evidence basis |
|---|---|---|
| **CL:0000598** ✅ | **pyramidal neuron** | LC3 accumulation in "cells of the internal pyramidal cell layer" (autopsy, A2) |
| **CL:0000127** ⚠️ *verify* | astrocyte | "reactive gliosis with increased numbers of reactive astrocytes"; LC3+ |
| **CL:0000129** ⚠️ *verify* | microglial cell | "microglia activation" |
| **CL:0000128** ⚠️ *verify* | oligodendrocyte | inferred from "marked loss of myelin" — **inferred, not directly demonstrated**; curate cautiously |
| **CL:0000740** ✅ | retinal ganglion cell | inferred from optic atrophy + optic pathway volume loss — **inferred**; the paper did not examine retina histologically |
| **CL:0000057** ⚠️ *verify* | fibroblast | the actual experimental cell type for all proteomics/EM/confocal work (`IN_VITRO`) |

Be explicit in the KB that **oligodendrocyte and retinal ganglion cell involvement is inferred**, while pyramidal neuron, astrocyte, microglia (autopsy) and fibroblast (in vitro) are directly evidenced.

### Subcellular level

| GO CC ID | Label | Finding |
|---|---|---|
| **GO:0044754** ✅ | autolysosome | **accumulate** — EM + LC3/LAMP1 confocal |
| GO:0005764 ⚠️ *verify* | lysosome | "aberrant morphology… enlarged size and a largely electron lucent lumen" |
| GO:0005776 ⚠️ *verify* | autophagosome | autophagy pathway component |
| GO:0031902 ✅ | late endosome membrane | ESCRT-II site of action |
| GO:0010008 ✅ | endosome membrane | ESCRT-II site of action |
| GO:0000814 ✅ | ESCRT II complex | **the disrupted complex** |

### Localization / lateralization

**Bilateral and symmetric** throughout. Volumetric measures were reported bilaterally (e.g., D1 white matter −17% bilaterally; E1 −20% bilaterally), with only minor L/R asymmetry in cerebellar cortex (D1: −13% L vs −21% R). Optic pathway involvement is bilateral (Family C: "bilateral hypoplastic optic nerves"). No unilateral or asymmetric presentation reported. Suggest **HP:0012832** Bilateral ⚠️ *verify* if a laterality modifier is desired.

---

## 8. Temporal Development

### Onset

| Pole | Age of onset | Pattern | HPO onset term |
|---|---|---|---|
| **Severe (DEE115)** | **Congenital / neonatal** (all 4); prenatal in C1 (brain malformations detected → TOP at 25 wk) | Congenital, immediately apparent | **HP:0003623** Neonatal onset ⚠️ *verify*; **HP:0030674** Antenatal onset ⚠️ *verify* (for C1) |
| — seizure onset | **7–9 months** | Subacute, then progressive | — |
| **Mild (NEDOA)** | **Optic atrophy 4–7 y**; ID recognized in childhood | Insidious | **HP:0011463** Childhood onset ⚠️ *verify* |
| **Mild (F1, ataxia)** | **Congenital ataxia**; developmental concern from 15 mo | Congenital, static | **HP:0003577** Congenital onset ⚠️ *verify* |

Note the **bimodal onset distribution** — congenital vs. mid-childhood — tracking directly with genotype (p.Val102Ile presence). Onset age is itself a genotype-driven variable here.

### Progression

**Severe pole — progressive and rapidly fatal:**
- Stage 1 (birth–~6 mo): profound hypotonia, feeding failure, **no milestone acquisition** (arrest, not regression)
- Stage 2 (~7–9 mo): seizure onset; EEG "multifocal and generalized epileptic discharges further progressing to **hypsarrythmia**"
- Stage 3: emergence of spasticity/hyperreflexia superseding hypotonia (A1, B1)
- Stage 4: "**pronounced and progressive** white matter atrophy," "**rapidly progressive** enlargement of the lateral ventricles"
- Terminal: death 9 wk – 8 mo in 3/4

Rate: **rapid.** Course: **progressive.** Duration: fatal in infancy for most; B1 survived to 4.5 y (upper bound of observation, not necessarily of survival).

**Mild pole — slowly progressive neurodegeneration on a static developmental baseline:**
- Static mild ID (developmental, non-progressive)
- **Superimposed progressive optic neuropathy** from age 4–7 y — degenerative, confirmed by abnormal VEPs (E1, E2: "delayed latency and reduced amplitude") and OCT
- Slowly progressive volume loss (white matter, cerebellar, temporal cortex, putamen) with increased cerebellar mean diffusivity
- Survival to at least 27 y (E1) with no reported deterioration to dependency

Rate: **slow.** Course: **static ID + progressive visual/cerebellar degeneration** — a genuine dual-component course. Duration: **chronic lifelong.**

**Terminology precision:** in the severe pole this is **neurodevelopmental arrest** ("Developmental stagnation," HP:0007281) — milestones were never acquired. Do **not** curate `HP:0002376` Developmental regression; the paper reports arrest, not loss of acquired skills.

### Patterns

- **Remission:** none, spontaneous or treatment-induced. No treatment exists.
- **Relapsing-remitting:** not applicable.
- **Critical periods:** Mechanistically, the prenatal/perinatal window governs the structural malformation component (corpus callosum hypo-/aplasia, pachygyria, optic nerve hypoplasia) — this is **already established at birth and is not modifiable postnatally**. The childhood window (4–7 y) is when the progressive optic neuropathy declares itself and is therefore the theoretical window for a disease-modifying (e.g., autophagy-directed) intervention. **This is mechanistic reasoning, not published clinical guidance — curate as `notes`/hypothesis, not as evidence.**

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value |
|---|---|
| **Prevalence** | **Not documented.** No Orphanet prevalence class assigned (no ORPHA code exists). |
| **Incidence** | **Not documented.** |
| **Cases in literature** | **9 individuals / 6 families** (single publication) |
| **Carrier frequency** | Not established for the gene overall. Only p.Val102Ile has usable population data: gnomAD AF **0.00015** (rs200399045). |

**Recommended dismech `Prevalence` record** (per the structured-prevalence guidance in `CLAUDE.md`):

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: NOT_YET_DOCUMENTED
  notes: >-
    Nine individuals from six families reported in the single defining
    publication (Brugger et al. 2024). No population prevalence or incidence
    estimate has been published; no Orphanet prevalence class assigned.
  evidence:
  - reference: PMID:38423010
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "We report nine individuals from six families presenting with a spectrum of neurodevelopmental/neurodegenerative features caused by bi-allelic variants in SNF8"
    explanation: Establishes the total reported case count.
```

Do **not** populate `rate_per_100000` — there is no basis for a number.

### Inheritance

- **Pattern:** **Autosomal recessive** — **HP:0000007** Autosomal recessive inheritance ⚠️ *verify*. Confirmed by homozygosity in Family C, compound heterozygosity in 5 families, unaffected heterozygous parents, and unanimous PanelApp classification as "BIALLELIC, autosomal or pseudoautosomal" across all 5 panels.
- **Penetrance:** **Incomplete for at least one genotype.** The healthy gnomAD p.Val102Ile homozygote is direct evidence that p.Val102Ile homozygosity is not fully penetrant. For the severe biallelic-null genotypes, penetrance appears complete (4/4 affected + 1 fetal). Curate as **incomplete/genotype-dependent**, not "complete."
- **Expressivity:** **Highly variable, but largely genotype-explained.** The severe↔mild split maps almost deterministically onto p.Val102Ile presence. Residual intra-mild variability (F1 ataxia-without-optic-atrophy vs. D1/E1/E2 optic-atrophy-without-ataxia) is unexplained.
- **Genetic anticipation:** **Not applicable** — not a repeat-expansion disorder.
- **Germline mosaicism:** Not reported.
- **Founder effects:** **None established.** Family C's homozygous c.623G>T (Israeli/Jerusalem) is a *single family* — insufficient to claim a founder allele. Do not assert one. The recurrence of p.Val102Ile across three unrelated families (D, E, F — two Italian, one German) reflects its **appreciable population frequency (a segregating polymorphic hypomorph)**, not a founder event.
- **Consanguinity:** Not explicitly reported; plausible in Family C given homozygosity. Do not assert.

### Population demographics

- **Reported ancestry:** German (Families A/Munich, B/Leipzig, F/mixed European), Italian (D/Bologna, E/Rome), Israeli (C/Jerusalem). **Entirely European + Middle Eastern** — this reflects **ascertainment through European diagnostic-genomics networks**, not true population restriction. Explicitly flag ascertainment bias; do not curate "affects Europeans."
- **Geographic distribution:** No endemic pattern; ascertainment-driven.
- **Variant geography:** p.Val102Ile in Italian and German families; c.623G>T homozygous in the Israeli family. N is far too small for geographic inference.
- **Sex ratio:** **5 M : 4 F** — no sex bias, as expected for autosomal recessive.
- **Age distribution:** bimodal by pole — severe pole ascertained in infancy (9 wk – 8 mo at death; B1 to 4.5 y); mild pole ascertained in childhood through adulthood (4–27 y).

---

## 10. Diagnostics

### Clinical tests

**Laboratory tests / biomarkers:** **No diagnostic biochemical biomarker exists.** No lactate, CSF, enzyme-assay, or metabolic marker abnormality was reported. Diagnosis is **molecular-genetic, full stop.** ⚠️ Do not curate a metabolic screen as diagnostic.

**Research-only functional assays** (not clinically validated, `IN_VITRO`):
- Quantitative proteomics on patient fibroblasts showing reduced SNF8/VPS36/VPS25 — the most useful functional confirmation for a VUS
- Electron microscopy: enlarged vesicular structures containing cytoplasmic material; lysosomes with "enlarged size and a largely electron lucent lumen"
- LC3/LAMP1 immunofluorescence: autolysosome accumulation

**Imaging — brain MRI (the key diagnostic modality; suggest NCIT:C16809 Magnetic Resonance Imaging ⚠️ verify):**
- *Severe:* progressive cerebral white-matter atrophy, corpus callosum hypo-/aplasia, ventriculomegaly, pachygyria; **cerebellum less affected, brainstem comparatively normal**
- *Mild:* quantitative volumetry of the anterior visual pathway (**ON/OC/optic tracts ≥2 SD below normal**) — the highest-yield mild-pole finding; plus regional volume loss and increased cerebellar mean diffusivity (DTI)

**Functional / electrophysiology:**
- **EEG:** multifocal and generalized epileptic discharges "further progressing to hypsarrythmia" (severe pole)
- **Visual evoked potentials (VEP):** "delayed latency and reduced amplitude" (E1, E2) — sensitive for the mild pole
- **OCT:** confirms optic (hypo)atrophy, onset 4–7 y

**Biopsy / pathology:** Not diagnostic. Autopsy neuropathology (A2) is confirmatory/research: pachygyria, enlarged sulci, reduced cerebral white matter, **corpus callosum thinned to 2 mm**, "marked loss of myelin," reactive astrogliosis, microglial activation, and strong LC3 immunostaining in internal pyramidal cell layer neurons and reactive white-matter astrocytes (vs. "only weak staining" in age-matched controls).

### Genetic testing — the definitive route

**Recommended approach:** **WES or WGS** (or a broad NDD/epilepsy/optic-neuropathy panel including *SNF8*), followed by phase/segregation confirmation in parents to establish biallelic status. *SNF8* is a small gene (258 aa) and single-gene testing is not clinically offered.

**Genomics England PanelApp — *SNF8* appears on 5 panels** (all "BIALLELIC, autosomal or pseudoautosomal"):

| Panel | ID | Rating |
|---|---|---|
| **DDG2P** | 484 | 🟢 **Green** (diagnostic-grade) |
| **Intellectual disability** | 285 | 🟢 **Green** |
| **Fetal anomalies** | 478 | 🟢 **Green** |
| Optic neuropathy | 186 | 🟡 Amber |
| Early onset or syndromic epilepsy | 402 | 🟡 Amber |

The Optic neuropathy amber rationale: *"two unrelated cases reported with optic atrophy"* — i.e., below the green threshold for that specific phenotype. This Green/Amber split is genuinely informative and worth capturing: *SNF8* is diagnostic-grade for **ID/DD and fetal anomalies**, but only moderate-evidence for **isolated optic neuropathy** and **epilepsy** presentations.

**Other modalities:**
- **CMA:** not indicated (no CNV mechanism)
- **Karyotype / FISH:** not indicated
- **mtDNA testing:** not indicated — but see differential below; it is often performed *before* the diagnosis because optic atrophy prompts mitochondrial workup
- **Repeat expansion testing:** not applicable

### Omics-based diagnostics

- **RNA-seq:** ⚠️ **Genuinely worth flagging as a curation-relevant gap.** The c.423−1G>C splice-acceptor variant (Family D) is annotated `p.?` — its actual transcript consequence was **not experimentally determined**. RNA-seq/RT-PCR would resolve it. This is a concrete `KNOWLEDGE_GAP` candidate.
- **Proteomics:** research-grade functional support (see above); not a clinical test.
- **Metabolomics / epigenomics (episignature) / liquid biopsy:** none available.

### Clinical criteria

**No consensus diagnostic criteria exist** (single publication, N=9). Practical diagnosis = compatible phenotype + biallelic *SNF8* variants + parental segregation.

### Differential diagnosis

**For the severe pole (DEE + leukoencephalopathy + CC hypo-/aplasia):**

| Differential | Gene | Distinguishing feature |
|---|---|---|
| **Pontocerebellar hypoplasia 8 (PCH8)** | *CHMP1A* (ESCRT-III), MIM 614961 | PCH8 has **prominent pontocerebellar hypoplasia**; SNF8 spares brainstem and relatively spares cerebellum. Both ESCRT. (PMID:23023333) |
| **CIMDAG syndrome** | *VPS4A*, MIM 619273 | Multisystem: **cataracts, dyserythropoietic anemia, growth retardation, dystonia** — absent in SNF8. *De novo* dominant missense, not recessive. (PMID:33186545) |
| Other DEEs / genetic leukodystrophies | many | Broad; resolved by sequencing |
| Aicardi–Goutières, peroxisomal, lysosomal storage disorders | many | Distinguished by biochemical markers, which are **normal/unremarkable** in SNF8 |

**For the mild pole (ID + childhood-onset optic atrophy):**

| Differential | Gene | Distinguishing feature |
|---|---|---|
| **Autosomal dominant optic atrophy** | *OPA1* | AD inheritance; typically isolated optic atrophy without ID |
| **Wolfram syndrome** | *WFS1* | Diabetes mellitus + diabetes insipidus + deafness |
| **Costeff / 3-methylglutaconic aciduria type III** | *OPA3* | **Abnormal urine organic acids** (3-methylglutaconic acid) — SNF8 has none |
| **Behr syndrome / *ACO2*-related** | *OPA1*, *ACO2* | Optic atrophy + ataxia + spasticity; overlaps closely with the SNF8 mild pole |
| **Leber hereditary optic neuropathy** | *MT-ND1/4/6* | Maternal inheritance, acute/subacute young-adult vision loss |
| Hereditary spastic paraplegia 53 | *VPS37A* (ESCRT-I), MIM 614898 | Spastic paraplegia predominant |

**Key practical point:** the mild pole most closely mimics *ACO2*/Behr-type **optic atrophy + ataxia + mild ID** syndromes, and mitochondrial optic neuropathies are typically excluded first. SNF8 is likely under-ascertained in exome-negative optic-atrophy-plus-ID cohorts — a plausible reason the published N remains 9.

### Screening

- **Newborn screening:** Not included in any program; no biochemical marker exists, so NBS is not technically feasible by current MS/MS methods.
- **Carrier screening:** *SNF8* is not on standard expanded carrier panels. Given AF ~1.5×10⁻⁴ for p.Val102Ile alone and unresolved penetrance, inclusion is **not currently justified**.
- **Cascade screening:** Appropriate within families — targeted testing of at-risk relatives and reproductive partners once a familial genotype is known.

---

## 11. Outcome / Prognosis

### Survival and mortality

⚠️ **No survival curve, 5-/10-year survival rate, life expectancy estimate, or mortality rate has been published.** With N=9, only individual outcomes are reportable. **Do not compute or curate a percentage survival figure** — any such number would be fabricated.

**Observed outcomes (individual-level, PMID:38423010):**

| Pole | Deaths | Ages at death | Cause |
|---|---|---|---|
| **Severe** | **3 of 4 died in infancy** | **9 weeks, 3 months, 8 months** | Respiratory infection secondary to dysphagia (A2, C2); cardiac arrest during status epilepticus (A1) |
| Severe (survivor) | B1 alive | 4.5 y at last visit | — |
| Fetal | C1 | 25 weeks' gestation | Termination of pregnancy for brain malformations |
| **Mild** | **0 of 4** | Alive at 4, 17, 18, 27 y | — |

**Disease-specific mortality mechanisms** — both are *secondary complications*, which is prognostically actionable:
1. **Aspiration/respiratory infection from dysphagia** (2 of 3 deaths) — the leading cause
2. **Status epilepticus** (1 of 3 deaths)

### Morbidity and function

- **Severe pole:** total functional dependency; no developmental milestones achieved; gastrostomy dependence (3/4); progressive spastic tetraplegia. Profound disability.
- **Mild pole:** mild ID predominantly affecting speech/language; progressive low vision from childhood; F1 with congenital ataxia. Substantially preserved function — all mild-pole individuals survived to adolescence/adulthood.
- **ICF-coded disability outcomes / DALYs:** none published.
- **Quality of life instruments:** **none administered** (see §3).

### Complications

| Complication | Pole | Note |
|---|---|---|
| Aspiration pneumonia / respiratory infection | Severe | **Leading cause of death** |
| Feeding failure requiring gastrostomy | Severe | 3/4 |
| Status epilepticus | Severe | Fatal in A1 |
| Progressive spasticity/contractures | Severe | A1, B1 |
| Low vision / functional visual impairment | Mild | Progressive from 4–7 y |

### Recovery potential

**None.** No recovery, no reversal of established structural CNS damage. The malformation component (CC hypo-/aplasia, pachygyria, optic nerve hypoplasia) is prenatally established and irreversible. No treatment exists to alter the degenerative component.

### Prognostic factors

**The dominant prognostic factor is genotype — specifically, presence of p.Val102Ile:**

> "All mildly affected individuals shared the same hypomorphic variant, c.304G>A (p.Val102Ile)." (PMID:38423010)

This is a genuinely strong, near-deterministic genotype–prognosis correlation in the published cohort — presence of one p.Val102Ile allele in *trans* predicted the mild pole in **4/4** cases; its absence predicted the severe pole in **5/5** (including the fetus). Caveat clearly: **N=9, single cohort, no independent replication.**

**Supporting functional/prognostic correlates:**
- **Degree of ESCRT-II subunit depletion in fibroblasts** tracks severity (severe: SNF8 0.25 with significant VPS36/VPS25 loss; mild: SNF8 0.68–0.74, non-significant, VPS36/VPS25 preserved) — a candidate functional prognostic assay
- **Zebrafish allele-pair severity** recapitulated the human gradient: severe pair (p.Tyr167Ter + p.Gly191Asp) ~**95%** aberrant embryos vs. mild pair (p.Pro79Leu + p.Val102Ile) ~**70%**
- Presence of dysphagia/gastrostomy dependence and early seizure onset mark the poor-prognosis group clinically

**Prognostic biomarkers:** none clinically validated.

---

## 12. Treatment

> ### ⚠️ **There is NO disease-specific or disease-modifying treatment for SNF8-related neurodevelopmental disorder.**
>
> PMID:38423010 discusses **no** therapeutic intervention. Verbatim finding from full-text review: *"No therapeutic interventions, treatments, or management strategies are discussed in this paper."* Severely affected individuals received **palliative care**; three required gastric tube feeding.
>
> **A search of ClinicalTrials.gov-indexed literature and the publication record identified NO clinical trials, NO NCT identifiers, and NO experimental therapeutics for this disorder.** Any treatment content below is **standard-of-care symptomatic management inferred from the reported clinical needs**, and must be curated as such — with `notes` rather than fabricated evidence, or with `evidence` citing only what PMID:38423010 actually states (i.e., that gastrostomy feeding was required).

### Pharmacotherapy

- **Antiseizure medications** for the epileptic encephalopathy. **No specific agent, regimen, or response rate is reported**; the epileptic encephalopathy with hypsarrhythmia was clinically severe and A1 died in status epilepticus, suggesting poor pharmacoresponsiveness — but the paper does not state this. Do not invent drug names.
  - Suggested: `treatment_term` NCIT:C15986 Pharmacotherapy; `therapeutic_modality: SMALL_MOLECULE`. **Leave `therapeutic_agent` empty** — no agent is documented.
- **Pharmacogenomics:** none. No PharmGKB/CPIC entry relates to *SNF8*.

### Advanced therapeutics

**None exist.** No gene therapy, gene editing, cell therapy, ASO/siRNA/mRNA therapy, targeted therapy, or immunotherapy has been developed, trialed, or proposed in print.

*Theoretical considerations only — flag clearly as speculative if curated at all:* recessive LoF with a hypomorphic-allele-defines-mild-pole architecture is in principle gene-replacement-tractable, and the p.Val102Ile natural experiment suggests only **partial** restoration of ESCRT-II function may suffice for the mild phenotype — a favorable therapeutic-threshold argument. **But:** the prenatally established malformation component (CC hypo-/aplasia) sets a hard limit on postnatal benefit, and CNS-wide delivery to white matter and retinal ganglion cells is unsolved. **This is my mechanistic reasoning, not published work — do not curate as evidence.**

### Surgical and interventional

- **Gastrostomy / PEG placement** — the one intervention actually documented: 3 of 4 severely affected individuals required gastric tube feeding.
  - Suggested: NCIT:C15329 Surgical Procedure (or a specific gastrostomy term, ⚠️ requires OAK verification); `therapeutic_modality: SURGERY`
  - Quotable basis: the paper states three required "gastric tube feeding"

### Supportive and rehabilitative (the actual standard of care)

| Intervention | Suggested NCIT (from in-repo authoritative list) | `therapeutic_modality` |
|---|---|---|
| Palliative / supportive care | **NCIT:C15747** Supportive Care | OTHER |
| Nutritional support (enteral feeding) | **NCIT:C15433** Nutritional Support | ⚠️ **Do NOT auto-tag BEHAVIORAL** — see `CLAUDE.md` warning; enteral feeding here is closer to a device/procedure |
| Physical therapy (spasticity, contractures) | **NCIT:C15302** Physical Therapy | BEHAVIORAL |
| Occupational therapy | **NCIT:C121351** Occupational Therapy ⚠️ verify | BEHAVIORAL |
| Speech and language therapy (mild pole — speech/language is the predominant ID domain) | **NCIT:C159273** Speech Therapy ⚠️ verify | BEHAVIORAL |
| Low-vision rehabilitation / visual aids | ⚠️ no verified NCIT term identified | DEVICE or BEHAVIORAL |
| Genetic counseling | **NCIT:C15240** Genetic Counseling | OTHER |

Per the `CLAUDE.md` mechanical-backfill table: NCIT:C15302 → `BEHAVIORAL`, NCIT:C15329 → `SURGERY`, NCIT:C15986 → agent-dependent (do not auto-assign). **NCIT:C15433 Nutritional Support must NOT be mechanically tagged `BEHAVIORAL`** — this exact mis-tagging was tried and reverted in this repo on 2026-07-08.

### Treatment outcomes, algorithms, combination/personalized approaches

**None published.** No response rates, no adverse-event data (no disease-specific drug exists), no treatment algorithm, no NCCN/society guideline, no genotype-guided treatment protocol. The only genotype-driven clinical action is **prognostic counseling** (p.Val102Ile → mild pole expectation), not treatment selection.

---

## 13. Prevention

### Primary prevention

**Not preventable** — a germline monogenic disorder. The only primary-prevention modality is **reproductive**:
- **Genetic counseling** with 25% recurrence risk per pregnancy for carrier couples (NCIT:C15240 Genetic Counseling)
- **Prenatal diagnosis** (CVS/amniocentesis) with targeted testing of the known familial variants
- **Preimplantation genetic testing for monogenic disorders (PGT-M)** — technically applicable once familial variants are known
- ⚠️ **Counseling caveat:** for couples where the fetus would be a **p.Val102Ile homozygote**, counseling is genuinely uncertain given the healthy gnomAD homozygote and the Ambry VUS classification. This must be communicated as uncertain, not as "affected." Important nuance to capture.

Family C's history — termination of pregnancy at 25 weeks for detected brain malformations, followed by an affected liveborn sibling (C2) who died at 9 weeks — illustrates the real reproductive stakes.

### Secondary prevention (early detection)

- **Cascade genetic testing** of at-risk relatives in known families
- In the mild pole, **serial ophthalmologic surveillance (VEP, OCT, visual acuity) from early childhood** is a rational early-detection strategy given documented onset at 4–7 y — enabling timely low-vision support and educational accommodation. *This is inference from the reported onset window, not a published guideline.*

### Tertiary prevention (complication prevention) — the highest-yield real intervention

Given that **2 of 3 deaths were respiratory infections secondary to dysphagia**, tertiary prevention is where meaningful clinical benefit plausibly lies:
- Early swallow assessment and aspiration-risk management
- Timely enteral feeding (gastrostomy) before nutritional/respiratory decompensation
- Respiratory hygiene, immunization against respiratory pathogens (routine schedule), prompt infection treatment
- Seizure-emergency (status epilepticus) action plans — relevant given A1's death
- Contracture prevention via physiotherapy/positioning

### Immunization

**No disease-specific vaccine.** Routine childhood immunization — with attention to respiratory pathogens (influenza, pneumococcus, RSV) — is rational given the aspiration-pneumonia mortality pattern. *Standard-of-care inference, not published guidance.*

### Screening programs, risk stratification, behavioral interventions, public health, prophylaxis

- **Population screening:** not warranted (ultra-rare, no biomarker, no intervention)
- **Newborn screening:** not feasible (no biochemical marker)
- **Risk stratification:** genotype-based only (p.Val102Ile presence → mild pole)
- **Behavioral / lifestyle interventions:** none applicable — no modifiable lifestyle risk factor exists
- **Public health / environmental interventions:** not applicable
- **Prophylaxis:** no antimicrobial or other prophylaxis protocol published; aspiration-pneumonia prevention is the rational target

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | NCBI Gene ID | Relevance |
|---|---|---|---|---|
| *Homo sapiens* | **NCBITaxon:9606** | *SNF8* | 11267 | The disease species |
| *Mus musculus* | **NCBITaxon:10090** | *Snf8* | ⚠️ verify MGI ID | IMPC KO model (§15) |
| *Danio rerio* | **NCBITaxon:7955** | *snf8* | ⚠️ verify ZFIN ID | The paper's in vivo model (§15) |
| *Drosophila melanogaster* | **NCBITaxon:7227** | *Vps22*/*snf8* | ⚠️ verify FlyBase ID | ESCRT-II biology; sleep/cardiac study (PMID:40176577) |
| *C. elegans* | **NCBITaxon:6239** | *vps-22* | ⚠️ verify WormBase ID | Longevity/DAF-16 (PMID:32829877) |
| *S. cerevisiae* | **NCBITaxon:4932** | *SNF8*/*VPS22* | ⚠️ verify SGD ID | Origin of the gene name; structural biology |

⚠️ **I attempted to confirm the mouse MGI accession and hit a wrong record** (MGI:1913677 is *Cyb5b*, not *Snf8*). **Do not curate MGI:1913677.** The MGI ID for *Snf8* must be looked up fresh before use. ZFIN quick-search returned 404 in this environment; the ZFIN ID likewise needs direct verification.

### Breed (VBO)

**Not applicable** — no breed-associated natural disease.

### Natural disease in other species

**None known.** No naturally occurring *SNF8*-related disease has been reported in companion animals, livestock, or wildlife. **A targeted OMIA search returned no SNF8 entry.** No veterinary relevance.

⚠️ **Do not curate the following as animal disease models** — they are incidental GWAS/biomarker associations in the SNF8-containing locus and are unrelated to this disorder:
- Chicken carcass-weight GWAS (PMID:40211845)
- *Drosophila* sleep/cardiac pleiotropy knockdown (PMID:40176577)
- *C. elegans* longevity/DAF-16 (PMID:32829877)
- Fathead minnow viral hemorrhagic septicemia proteomics (PMID:24931624)
- Rat MASH models (PMID:40306176)

### Comparative biology

**Evolutionary conservation is strong and mechanistically meaningful.** ESCRT-II is conserved from yeast to human: "ESCRT-II plays a pivotal role in receptor downregulation and multivesicular body biogenesis and is conserved from yeast to humans." The subunit architecture is preserved — yeast Vps22/Vps36/Vps25 ↔ human SNF8/VPS36/VPS25, with the same 1:1:2 stoichiometry and Y-shaped/trilobal fold (PMID:15329733; PMID:15469844; human structures PDB 2ZME, 3CUQ).

**Comparative pathology:** the human disease phenotype (CNS-restricted neurodevelopmental/neurodegenerative) is **not** recapitulated as a natural disease in any species. Yeast and invertebrate models display trafficking, gene-expression, and longevity phenotypes with **no neurodevelopmental correlate** — the yeast literature (glucose-dependent gene expression, Rim101/PMR1 calcium-pump regulation, PAF1-complex genetic interactions, flavor-ester biosynthesis) reflects **conserved machinery in a non-conserved physiological context**. Useful for structure–function, not for disease modeling.

### Transmission

**Not applicable** — no zoonotic potential, no cross-species susceptibility, not communicable.

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*) — the primary in vivo disease model

**Model type:** vertebrate, **morpholino (MO) antisense knockdown** — ⚠️ **transient knockdown, NOT a stable genetic mutant.** This distinction matters for evidence weighting.

**Recapitulated phenotypes** (from the abstract, quotable):
> "Snf8 loss of function in zebrafish results in global developmental delay and altered embryo morphology, impaired optic nerve development, and reduced forebrain size."

Detailed findings:
- Statistically significant **global developmental delay**, curly tail, reduced pigmentation, small head and eyes
- **Reduced brain area** on confocal morphometry, "with variable phenotypes among morphant fish"
- **Ectopic proliferative (pH3+) cells within the forebrain**, "partially rescued in fish expressing WT SNF8" → implicates dysregulated neural progenitor proliferation
- **Optic nerve:** statistically significant reduction in extension and thickness, "which was rescued in fish co-injected with snf8 MO and WT SNF8"; reduced axonal scaffold
- **Optic chiasm:** loss of the characteristic angle in morphants, restored by WT SNF8

**Variant-specific rescue — the key pathogenicity and genotype–phenotype experiment:**
- WT *SNF8* mRNA **partially rescued** the phenotype
- Disease-variant allele pairs **failed to rescue**
- Severity gradient mirrored the human poles:
> "A more severe phenotypic impact in embryos coexpressing the SNF8 alleles encoding p.Tyr167Ter and p.Gly191Asp compared to those microinjected with alleles encoding p.Pro79Leu and p.Val102Ile was observed (approximately 95% vs. 70% aberrant embryos)."

**Phenotype recapitulation quality — genuinely good for the axis that matters:** the model reproduces (a) impaired optic nerve/chiasm development ↔ human optic atrophy/optic nerve hypoplasia, and (b) reduced forebrain size ↔ human microcephaly/reduced cerebral volume. Critically, it reproduces the **allele-severity gradient**, providing independent in vivo support for the p.Val102Ile-hypomorph model.

**Limitations (curate honestly):**
1. **Morpholino, not a germline mutant** — subject to well-known off-target/toxicity artifacts; no stable `snf8` zebrafish mutant line is reported. Rescue experiments mitigate but do not eliminate this concern.
2. **Does not model epilepsy** — no seizure phenotype assessed; the DEE component is unmodeled
3. **Does not model leukoencephalopathy or corpus callosum hypo-/aplasia** — zebrafish lack a corpus callosum entirely
4. **Does not model intellectual disability** or the progressive postnatal neurodegenerative course
5. Variable penetrance among morphants ("reduced penetrance of morphological defects")

**Recommended dismech treatment:** curate zebrafish evidence with `evidence_source: MODEL_ORGANISM`, and add a **`kind: HUMAN_MODEL_MISMATCH`** discussion — not a generic `KNOWLEDGE_GAP` — since evidence *exists* in the model but its fidelity to the human phenotype is the open question (per the `CLAUDE.md` distinction: `KNOWLEDGE_GAP` = evidence absent; `HUMAN_MODEL_MISMATCH` = evidence exists but translational validity is uncertain). The specific mismatch: **the zebrafish MO model captures the optic-nerve/forebrain developmental axis but captures none of the epileptic encephalopathy, callosal agenesis, or leukoencephalopathy that define the severe human pole.**

### Mouse (*Mus musculus*) — IMPC knockout

Retrieved live from the IMPC genotype-phenotype API for *Snf8*:

| Zygosity | Phenotype | Parameter | p-value |
|---|---|---|---|
| **Homozygote** | **Preweaning lethality, complete penetrance** | Outcome | **0.0** |
| Heterozygote | Abnormal tail movements (tail elevation) | Tail elevation | 4.17×10⁻⁵ |
| Heterozygote | Increased lactate dehydrogenase level | Lactate dehydrogenase | 2.57×10⁻⁵ |

**Interpretation:** *Snf8* homozygous null is **preweaning lethal with complete penetrance** in mouse — consistent with an essential gene and concordant with the severity of the human biallelic-null phenotype (death in infancy in 3/4). This is a genuinely useful, independently-sourced cross-species datapoint.

**Limitations:**
1. **Complete null lethality precludes study of the postnatal neurological phenotype** — no viable homozygous mouse exists to phenotype for seizures, white matter, or optic nerve
2. **No hypomorphic mouse allele exists** — the human p.Val102Ile mild pole, which is the most clinically informative genotype, is **entirely unmodeled in mouse**. A knock-in *Snf8* p.Val102Ile equivalent is the obvious highest-value missing model. **Strong `proposed_experiments` candidate.**
3. Heterozygous phenotypes (tail elevation, elevated LDH) have **no clear human correlate** — human heterozygous carriers (parents) are unaffected. Do not over-interpret.
4. **No conditional, neural-specific, or humanized mouse model is reported.**

⚠️ **Verify the MGI accession for *Snf8* directly before curating** (my first lookup landed on *Cyb5b*).

### Cellular / in vitro models

**Patient-derived primary fibroblasts** — the workhorse functional system (individuals A2 [severe], D1 and E1 [mild]); `evidence_source: IN_VITRO`:
- Quantitative proteomics (ESCRT-II subunit quantification)
- Transmission electron microscopy (autolysosome and aberrant lysosome accumulation)
- LC3/LAMP1 confocal immunofluorescence
- EGFR degradation assay (**preserved** — the cargo-specificity result)

**Limitation:** fibroblasts are not neurons. The disease is CNS-restricted, so the most disease-relevant cell types — cortical pyramidal neurons, oligodendrocytes, retinal ganglion cells — were **not** studied functionally. **No iPSC, iPSC-derived neuron, organoid, or immortalized-line model is reported.** This is a significant gap: iPSC-derived neurons and retinal organoids are the obvious next models, and were used in the comparable *VPS4A* work (PMID:33186545 studied "iPSC-derived human neurons"), showing the approach is tractable for ESCRT disorders.

**MorPhiC:** *SNF8* is **not** among the MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2-1). No MorPhiC cellular phenotype data available.

### Induced (non-genetic) models

**None** — no drug-induced, surgical, or environmentally induced model exists or would be meaningful for a monogenic trafficking defect.

### Model databases to query

MGI (mouse — verify *Snf8* accession), IMPC/mousephenotype.org (✅ data retrieved above), ZFIN (zebrafish — verify accession), FlyBase (*Vps22*), WormBase (*vps-22*), SGD (yeast *SNF8*), Alliance of Genome Resources (cross-species), IMSR/KOMP/EMMA/MMRRC (strain availability — ⚠️ not checked).

---

## Appendix A — Curation notes on the existing draft entry

I found an **untracked draft** at `kb/disorders/SNF8-Related_Neurodevelopmental_Disorder.yaml` in this worktree. Five observations, most-actionable first:

1. **`updated_date` should be removed.** `CLAUDE.md` states plainly: *"Do not add `updated_date` to new entries. The field is deprecated — git history is the authoritative change log."* The draft sets `updated_date: "2026-08-01T00:00:00Z"`.

2. **Scope mismatch between the entry name and `disease_term`.** The entry is named "SNF8-Related Neurodevelopmental **Disorder**" (spanning both poles) but binds `disease_term` to `MONDO:0968947` (*neurodevelopmental disorder plus optic atrophy* = the **mild pole only**), and its `description` describes only "the milder end." The severe pole — DEE115, `MONDO:0968946` / OMIM:620783 — carries 4 of 9 individuals and all the mortality, and is currently unrepresented. Two clean options:
   - **(a)** Keep one spectrum entry, use `has_subtypes` with `Severe (DEE115)` and `Mild (NEDOA)` as subtype names (short and slug-friendly per the naming convention), and add `MONDO:0968946` under `mappings:`; or
   - **(b)** Split into two `Disease` entries and add a `Grouping` over them (`grouping_basis: SHARED_GENE_FAMILY` + `SHARED_MECHANISM`, with a `NECESSARY` `HAS_GENE` criterion on SNF8).

   I'd recommend **(a)** — the poles are a genotype-graded continuum of one mechanism, not two diseases, and the `has_subtypes` foreign-key machinery lets phenotypes/prevalence/progression be attributed per pole.

3. **No `evidence:` blocks anywhere in the draft.** Every pathophysiology node, phenotype, and genetic claim needs an `EvidenceItem`. `PMID_38423010.md` is **already in `references_cache/`** with the full abstract, so exact-quote snippets can be drawn from it immediately without a fetch. Verbatim snippets ready to use (all confirmed substrings of the cached abstract):
   - `"All mildly affected individuals shared the same hypomorphic variant, c.304G>A (p.Val102Ile)."`
   - `"In patient-derived fibroblasts, bi-allelic SNF8 variants cause loss of ESCRT-II subunits."`
   - `"Snf8 loss of function in zebrafish results in global developmental delay and altered embryo morphology, impaired optic nerve development, and reduced forebrain size."`
   - `"loss of ESCRT-II due to bi-allelic SNF8 variants is associated with a spectrum of neurodevelopmental/neurodegenerative phenotypes mediated likely via impairment of the autophagic flux"`
   - `"The phenotypic spectrum included four individuals with severe developmental and epileptic encephalopathy, massive reduction of white matter, hypo-/aplasia of the corpus callosum, neurodevelopmental arrest, and early death."`

4. **`hgnc:17028` is correct** for SNF8 (lowercase prefix, per repo convention) — ✅ verified against the HGNC REST API.

5. **The single pathophysiology node should be expanded** into the causal chain in §6. The most valuable addition is the convergent hub node **"Impaired Autophagic Flux"** with `biological_scale: CELLULAR`, since that is the mechanistic claim the paper actually makes — and it should carry `hypothesis_groups` reflecting the authors' `"likely via"` hedge (a `mechanistic_hypotheses` entry with `status: EMERGING`).

**Module conformance opportunity:** no existing `kb/modules/` module cleanly fits (ESCRT/autophagic-flux is not yet modeled; `lysosomal_substrate_accumulation` is a *hydrolase-deficiency/substrate-storage* module and is **not** the right anchor here — there is no stored substrate). Candidate future modules: an *ESCRT/autophagic-flux failure* module, or `photoreceptor_degeneration`'s sibling for optic neuropathy. Worth noting there is a real gap rather than forcing a bad `conforms_to`.

## Appendix B — Recommended `discussions` entries

| `kind` | Prompt |
|---|---|
| `KNOWLEDGE_GAP` | Why is one gnomAD individual homozygous for p.Val102Ile apparently healthy? Is an unidentified modifier, a threshold effect, or incomplete phenotyping responsible? |
| `KNOWLEDGE_GAP` | What is the actual transcript consequence of c.423−1G>C (annotated `p.?`)? RNA-seq/RT-PCR on patient RNA would resolve it. |
| `KNOWLEDGE_GAP` | Why does F1 (p.Pro79Leu/p.Val102Ile) have congenital ataxia without optic atrophy, while D1/E1/E2 (same hypomorph) have optic atrophy without ataxia? |
| `KNOWLEDGE_GAP` | Is impaired autophagic flux the proximate cause of the neurological phenotype, or a correlated cellular readout? The causal link is hypothesized ("likely via"), not demonstrated in neurons. |
| **`HUMAN_MODEL_MISMATCH`** | The zebrafish morpholino model reproduces optic nerve and forebrain developmental defects but **none** of the epileptic encephalopathy, callosal agenesis, or leukoencephalopathy defining the severe human pole; and the mouse null is preweaning-lethal, precluding postnatal CNS phenotyping. Does any model system faithfully represent severe-pole human pathophysiology? *Proposed experiments:* stable `snf8` zebrafish germline mutant; conditional/neural-specific mouse KO; **knock-in mouse or iPSC model of the p.Val102Ile hypomorph**; patient iPSC-derived cortical neurons and retinal organoids. |
| `KNOWLEDGE_GAP` | Which ESCRT-II cargoes are selectively affected? EGFR degradation was preserved, implying cargo specificity, but the affected cargo set (notably lysosomal hydrolases) has not been identified. |

---

## Sources

**Primary (disease-defining):**
- [Brugger M, et al. Bi-allelic variants in SNF8 cause a disease spectrum ranging from severe developmental and epileptic encephalopathy to syndromic optic atrophy. Am J Hum Genet. 2024;111(3):594–613. **PMID:38423010**](https://pubmed.ncbi.nlm.nih.gov/38423010/) · [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940020/) · [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002929724000375)

**Mechanism / structural biology:**
- [Teo H, et al. Structure of the ESCRT-II endosomal trafficking complex. Nature. 2004. **PMID:15329733**](https://pubmed.ncbi.nlm.nih.gov/15329733/)
- [Hierro A, et al. ESCRT-II, an endosome-associated complex required for protein sorting: crystal structure and interactions with ESCRT-III and membranes. Dev Cell. 2004. **PMID:15469844**](https://pubmed.ncbi.nlm.nih.gov/15469844/)
- [Structure and function of the ESCRT-II-III interface in multivesicular body biogenesis. Dev Cell. 2009. **PMID:19686684**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2749878/)
- [RCSB PDB 2ZME — human ESCRT-II complex](https://www.rcsb.org/structure/2ZME) · [PDB 3CUQ](https://www.rcsb.org/structure/3CUQ)
- [UniProt Q96H20 — Vacuolar-sorting protein SNF8](https://rest.uniprot.org/uniprotkb/Q96H20.txt)

**Related ESCRT disorders (differential diagnosis):**
- [Mochida GH, et al. CHMP1A encodes an essential regulator of BMI1-INK4A in cerebellar development. Nat Genet. 2012. **PMID:23023333**](https://pubmed.ncbi.nlm.nih.gov/23023333/)
- [Rodger C, et al. De Novo VPS4A Mutations Cause Multisystem Disease with Abnormal Neurodevelopment. Am J Hum Genet. 2020. **PMID:33186545**](https://www.sciencedirect.com/science/article/pii/S0002929720303700)

**Structured databases:**
- [OMIM 620783 — DEE115](https://omim.org/entry/620783) · [OMIM 620784 — NEDOA](https://omim.org/entry/620784) · [OMIM 610904 — SNF8 gene](https://omim.org/entry/610904)
- [ClinVar SNF8 variants](https://www.ncbi.nlm.nih.gov/clinvar/?term=SNF8%5Bgene%5D) (VCV002664478–VCV002664484)
- [HGNC:17028 (REST)](https://rest.genenames.org/fetch/symbol/SNF8)
- MONDO via [EBI OLS4](https://www.ebi.ac.uk/ols4/) — MONDO:0968946, MONDO:0968947
- HPO term verification via [JAX HPO API](https://ontology.jax.org/)
- [IMPC genotype-phenotype API — *Snf8*](https://www.mousephenotype.org/)
- [Genomics England PanelApp — SNF8 (Optic neuropathy, panel 186)](https://panelapp.genomicsengland.co.uk/panels/186/gene/SNF8/) · [all SNF8 panel entries](https://panelapp.genomicsengland.co.uk/panels/entities/SNF8)
- [GeneCards — SNF8](https://www.genecards.org/card/SNF8)

**Verified unavailable (searched, nothing found):** Orphanet ORPHA code · ClinicalTrials.gov trials · OMIA natural animal disease · MorPhiC data · published QoL/survival/prevalence statistics · GxE data · episignature data · any second clinical publication.

**Not retrievable in this environment (do NOT populate from memory — fetch directly):** gnomAD constraint metrics (pLI, o/e LoF) for *SNF8* · DepMap essentiality · MGI accession for mouse *Snf8* · ZFIN accession for zebrafish *snf8* · OMIM full clinical synopses (omim.org returned HTTP 403).