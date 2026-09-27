---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T15:03:56.595387'
end_time: '2026-09-03T15:09:38.197937'
duration_seconds: 341.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MEPAN Syndrome
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
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 35
  total_cost_usd: 1.3216430000000003
  session_id: eccb37f5-d277-53f4-9bc9-b541745fd0d8
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 8
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MEPAN Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MEPAN Syndrome** covering all of the
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

I have sufficient material to compile a comprehensive report now.

Found PMID 37653044. I now have enough to write the comprehensive report.

---

# MEPAN Syndrome — Comprehensive Research Report

## 1. Disease Information

**Overview.** MEPAN syndrome (Mitochondrial Enoyl CoA Reductase Protein–Associated Neurodegeneration) is an ultra-rare, autosomal recessive, childhood-onset neurodegenerative disorder caused by biallelic pathogenic variants in *MECR*. It is defined by two core, largely non-overlapping-in-timing features: a progressive movement disorder (dystonia, often with chorea and/or ataxia) that begins in early childhood, and optic atrophy that develops during the same period or within a few years afterward, with relative sparing of cognition ([GeneReviews, NBK540959](https://www.ncbi.nlm.nih.gov/books/NBK540959/); [Orphanet ORPHA:508093](https://www.orpha.net/en/disease/detail/508093)). It was the first human disease shown to result from a defect in the mitochondrial fatty acid synthesis (mtFASII) pathway (Heimer et al., 2016, PMID: [27817865](https://pubmed.ncbi.nlm.nih.gov/27817865/)).

**Key identifiers:**
- **OMIM:** #617282 — "Dystonia, Childhood-Onset, With Optic Atrophy and Basal Ganglia Abnormalities" (DYTOABG); gene locus 608205 (*MECR*)
- **Orphanet:** ORPHA:508093
- **MONDO:** MONDO:0015003
- **Gene:** *MECR*, HGNC:19691, chromosome 1p35.3, 18 exons
- **Disease Ontology / other databases:** DOID:0081419 (ZFIN "childhood-onset dystonia with optic atrophy and basal ganglia abnormalities")
- ICD-10/11 do not have a disease-specific code; it is typically coded under dystonia (G24.-) and hereditary optic atrophy (H47.2) codes, or E-series inborn-error-of-metabolism codes when used in practice.

**Synonyms:** MEPAN syndrome; MECR-related neurologic disorder; childhood-onset dystonia with optic atrophy and basal ganglia abnormalities (DYTOABG); autosomal recessive childhood-onset dystonia, DYT29 type; childhood-onset generalized dystonia–optic atrophy syndrome ([Orphanet](https://www.orpha.net/en/disease/detail/508093); [Wikipedia](https://en.wikipedia.org/wiki/MEPAN_syndrome)).

**Data provenance.** Knowledge of MEPAN derives almost entirely from **aggregated case-series/cohort data** rather than large-scale EHR mining, reflecting its ultra-rarity: the original description (Heimer et al. 2016) reported 7 individuals from 5 families; GeneReviews (last substantively updated ~2019) documented 13 affected individuals from 8 families; by early 2023 more than 30 individuals had been diagnosed globally (per search aggregation of OMIM/patient-advocacy sources). Supplementary mechanistic evidence comes from patient-derived fibroblasts, yeast complementation assays, *Drosophila* and mouse models, and one small natural-history/longitudinal study (*Brain*, 2024, discussed below under phenotype).

---

## 2. Etiology

**Disease causal factor:** MEPAN is caused exclusively by **biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic pathogenic variants in *MECR*** — there is no known environmental, infectious, or purely mechanistic (non-genetic) etiology. It is a monogenic mitochondrial fatty-acid-synthesis disorder.

**Genetic risk factors:**
- Homozygosity/compound heterozygosity for *MECR* pathogenic variants (missense, nonsense, splice-site).
- **Ashkenazi Jewish ancestry** is a population-level risk factor due to two recurrent founder variants:
  - c.695G>A (missense) — carrier frequency ~1:311 in Ashkenazi Jews
  - c.830+2dupT (splice site) — carrier frequency ~1:136 in Ashkenazi Jews
  (GeneReviews, PMID: 27817865). Screening of >5,500 Ashkenazi Jewish exomes confirmed these elevated carrier frequencies. Five of the original 8 reported families were of Ashkenazi Jewish origin, though the disease occurs across all ethnicities (e.g., the Chinese proband below, and the Italian LHON-like family).
- No modifier genes have been formally established, but **intrafamilial phenotypic variability** (siblings with the same genotype ranging from minimal symptoms to severe wheelchair dependence) strongly suggests unidentified genetic or environmental modifiers/incomplete penetrance (GeneReviews).

**Environmental/triggering risk factors:**
- **Febrile illness/intercurrent infection** is repeatedly reported to precipitate acute worsening or stepwise, sometimes irreversible, loss of motor function ("Symptoms may fluctuate temporally with febrile illnesses"; one patient had permanent motor decline after a febrile episode without recovery — GeneReviews).
- **General anesthesia/propofol exposure** has been associated with marked, lasting motor decline in at least one reported patient.
- **Dopaminergic agents** (e.g., levodopa) have worsened chorea in at least one patient, an important negative treatment/exposure signal.

**Protective factors:** No genetic protective variants are established. The single most consequential "protective" finding to date is pharmacologic: early institution of **lipoic acid (LA)** ± **octanoic acid (C8)** supplementation is associated with attenuated or halted disease progression in at least two independently reported cases (see Treatment, §12).

**Gene–environment interaction:** The mechanistic link is that mtFASII produces the octanoate precursor for lipoic acid, an essential cofactor for pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, and the glycine cleavage system. Febrile/catabolic stress increases metabolic demand on these lipoylation-dependent enzymes at a time when residual MECR activity is already insufficient, plausibly explaining stress-triggered decompensation — this is inferred from the biochemistry rather than directly demonstrated by a controlled gene-environment study.

---

## 3. Phenotypes

MEPAN's phenotype spans two organ systems (extrapyramidal motor system and optic nerve) with a third, cognition, notably spared.

### Movement disorder (clinical sign/symptom)
- **Onset:** ~1–6.5 years of age (some sources describe "before age 7"); may begin with hypotonia and delayed motor milestones in infancy before dystonia emerges.
- **Core feature — dystonia:** progressive, may be axial and/or appendicular; facial dystonia also reported.
- **Associated movement abnormalities:** chorea, choreoathetosis, ataxia, myoclonus, dyskinesia, limb spasticity, nystagmus.
- **Dysarthria/dysphagia:** progressive speech impairment; feeding difficulty in more severe cases.
- **Severity/progression:** gradually progressive; highly variable even within families — from minimal impairment to complete wheelchair dependence and total care needs. Some patients lose independent ambulation (OMIM Clinical Synopsis #617282).
- **Suggested HPO terms:** HP:0001332 (Dystonia), HP:0002072 (Chorea), HP:0001251 (Ataxia), HP:0001260 (Dysarthria), HP:0002015 (Dysphagia), HP:0001257 (Spasticity), HP:0001338 (Myoclonus), HP:0000639 (Nystagmus), HP:0001510 (Growth delay — if relevant), HP:0001263 (Global developmental delay — variable/not universal).

### Optic atrophy (clinical sign, ophthalmologic)
- **Onset:** typically 4–12 years, developing around the same time as or within a few years after the movement disorder.
- **Course:** progressive decrease in visual acuity; can progress to functional or legal blindness in adulthood.
- Ophthalmic Genetics case study (Tandfonline, 2022) documented visual acuity of 20/150 bilaterally with moderate dyschromatopsia (pseudoisochromatic plates) and largely preserved peripheral fields (Goldmann perimetry); OCT showed bilateral optic atrophy with **predilection for the papillomacular bundle**, a pattern shared with other mitochondrial optic neuropathies (LHON, dominant optic atrophy/OPA1). A later cohort description notes "diffuse retinal nerve fiber layer thinning and severe ganglion cell thinning."
- **Suggested HPO terms:** HP:0000648 (Optic atrophy), HP:0000572 (Visual loss), HP:0000577 (Exotropia/strabismus if present), HP:0007663 (Reduced visual acuity), HP:0000501 (Glaucoma — not typical, for contrast), HP:0000505 (Visual impairment).

### Cognition
- **Relative sparing** is a defining and repeatedly emphasized feature ("intellect is often — but not always — preserved," GeneReviews), distinguishing MEPAN from many other pediatric neurodegenerative/NBIA-like disorders.

### Neuroimaging finding (not itself a symptom but a defining paraclinical phenotype)
- Bilateral hyperintense T2-weighted MRI signal in one or more basal ganglia structures (caudate, putamen, globus pallidus) at/around dystonia onset — a key diagnostic clue.
- Suggested term: HP:0002135 (Basal ganglia signal abnormality on MRI, if available) or more general HP:0002071 (Abnormality of extrapyramidal motor function) plus imaging-descriptor free text.

### Quality of life impact
No disease-specific EQ-5D/SF-36/PROMIS data were identified in the literature; QoL impact is described qualitatively — progressive loss of independent ambulation, speech intelligibility, and vision drives major functional impairment and caregiver burden, with impact concentrated in physical/mobility and communication domains rather than cognitive/social domains, per GeneReviews' description of variable disability trajectories.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MECR* (mitochondrial trans-2-enoyl-CoA reductase), HGNC:19691, OMIM *608205, chromosome 1p35.3, 18 exons, 5 reported protein isoforms via alternative splicing; canonical transcript NM_016011.5 encodes a 373-amino-acid protein.

**Pathogenic variant spectrum (as of GeneReviews 2019 update):** Six pathogenic variants identified — three missense, two nonsense, one canonical splice-site — across 8 families:
- c.695G>A (missense) — Ashkenazi Jewish founder, carrier freq. ~1:311
- c.830+2dupT (splice site) — Ashkenazi Jewish founder, carrier freq. ~1:136
- Additional missense/nonsense variants in non-Ashkenazi families
- c.772C>T, p.Arg258Trp — homozygous in an Italian family with an atypical "LHON-like" phenotype (see below); ultra-rare in gnomAD (MAF 6.368×10⁻⁵); reduces MECR protein levels by ~80% in yeast complementation, implying protein instability rather than pure catalytic loss (Bianco et al., 2024, *J Med Genet*, PMID: [37734847](https://pmc.ncbi.nlm.nih.gov/articles/PMC10804020/))
- c.910G>T, p.Asp304Tyr — homozygous, first reported Chinese patient, dystonia/basal ganglia disease **without** optic atrophy; disturbed protein stability by modeling (ScienceDirect, 2020)

**Population genetic constraint:** gnomAD v4.0 reports pLI = 0 and LOEUF = 0.96 for *MECR*, indicating the gene is not under strong constraint against loss-of-function variants in the heterozygous state (consistent with a fully recessive disease mechanism and viable, asymptomatic carriers).

**Variant classification:** Per ClinGen (search.clinicalgenome.org/kb/genes/HGNC:19691) and ClinVar, *MECR* variants associated with disease are classified via standard ACMG/AMP criteria; nonsense variants are interpreted as pathogenic via predicted loss-of-function/nonsense-mediated decay given LOF is an established disease mechanism for this gene.

**Functional consequence:** Loss-of-function or hypomorphic. Decreased MECR enzymatic activity reduces production of octanoyl-ACP (the terminal mtFASII product and lipoic acid precursor), which in turn:
- Impairs protein lipoylation of pyruvate dehydrogenase (PDH), α-ketoglutarate dehydrogenase (KGDH), branched-chain ketoacid dehydrogenase, and the glycine cleavage system H-protein (demonstrated directly in patient fibroblasts).
- Impairs mitochondrial RNA processing/translation and respiratory chain complex assembly.
- Destabilizes the mitochondrial iron-sulfur cluster (ISC) assembly complex (LYRM4/ISD11, NFS1, ISCU) via loss of acylated acyl-carrier protein (ACP), the form of ACP required for ISC-assembly-complex and OXPHOS-supercomplex stability (Murdock et al., 2025, PNAS, PMID: [41021813](https://pmc.ncbi.nlm.nih.gov/articles/PMC12519216/)).

**Modifier genes:** None formally established; intrafamilial variability (same genotype, discordant severity) is unexplained.

**Epigenetics:** No disease-specific epigenetic (DNA methylation/histone) studies were identified for MEPAN.

**Chromosomal abnormalities:** Not applicable — MEPAN is caused by point/small indel variants in *MECR*, not by large structural rearrangements or aneuploidy.

**Ontology suggestions:** Gene — hgnc:19691 (MECR); functional impact category — LOSS_OF_FUNCTION / PARTIAL_LOSS_OF_FUNCTION (per variant; the R258W allele is a destabilizing hypomorph rather than a null).

---

## 5. Environmental Information

- **No toxic, occupational, or pollutant exposures** are implicated in MEPAN causation; it is purely monogenic.
- **Infectious/febrile triggers:** intercurrent febrile illness is an environmental *modifier* of disease course (precipitating acute, sometimes permanent, motor decline), not a cause. No specific pathogen has been implicated — it is presumed to act via generic metabolic/catabolic stress rather than a specific infectious mechanism.
- **Iatrogenic exposure:** general anesthesia (propofol specifically flagged) is an environmental factor associated with acute, lasting neurological worsening in at least one case, warranting caution during surgical planning (GeneReviews "Agents/Circumstances to Avoid").
- **No infectious agents** cause or trigger MEPAN as primary etiology.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from initiating lesion to clinical manifestation)

1. **Biallelic pathogenic *MECR* variants** → reduced or absent mitochondrial trans-2-enoyl-CoA reductase enzymatic activity (demonstrated directly: yeast complementation assays, patient fibroblast studies; PMID 27817865, 37734847).
2. This **impairs the terminal step of mitochondrial fatty acid synthesis (mtFASII)**, reducing production of octanoyl-acyl carrier protein (octanoyl-ACP) (demonstrated in yeast *Δetr1* complementation and patient-derived cells; PMID 27817865).
3. Reduced octanoyl-ACP **leads to (a)** deficient lipoic acid biosynthesis and **(b)** an accumulation of unacylated (dimerized, 28 kD) ACP in place of properly acylated ACP (demonstrated in mouse brain proteomics; PNAS 2025, PMID 41021813).
4. **Branch A (lipoylation deficiency):** Loss of octanoyl-ACP/lipoic acid **results in** failure to lipoylate PDH, KGDH, branched-chain ketoacid dehydrogenase, and glycine cleavage H-protein (demonstrated in patient fibroblasts, Heimer et al. 2016) → impaired mitochondrial energy metabolism and amino-acid catabolism, contributing to neuronal energy failure. Notably, reduced lipoylation is tissue-selective — reported as reduced in brain but relatively spared in retina, implying (inferred, per Wikipedia summary of primary literature) that the optic neuropathy in MEPAN is **not** solely explained by loss of retinal lipoylation, and a separate mechanism (below) likely dominates in the optic nerve.
5. **Branch B (ISC/supercomplex deficiency):** Loss of properly acylated ACP **destabilizes the mitochondrial iron-sulfur cluster (ISC) assembly complex** (decreased LYRM4, NFS1, ISCU) and **alters OXPHOS complex/supercomplex assembly** (demonstrated in the Mecr-mutant mouse brain proteome and complexome; PNAS 2025, PMID 41021813) → reduced mitochondrial oxidative phosphorylation capacity in brain tissue (directly measured: "reduced mitochondrial oxidative phosphorylation in the brain," same source).
6. Downstream of ISC/Fe–S cluster deficiency, in the *Drosophila* Mecr-loss model, this **leads to increased free iron levels** and **elevated ceramide levels**, establishing a mechanistic loop between iron dysregulation and sphingolipid metabolism (demonstrated in fly neurons and confirmed in human MEPAN patient fibroblasts, which show the same elevated ceramide and impaired iron homeostasis; Tesch et al., *Nature Metabolism* 2023, PMID: [37653044](https://ncbi.nlm.nih.gov/pmc/articles/PMC11151872)). **Experimentally reducing either iron or ceramide levels suppresses the neurodegenerative phenotype** in the fly model — direct causal (interventional) evidence for this branch, in a model organism.
7. The combination of impaired energy metabolism (Branch A), impaired OXPHOS/supercomplex assembly (Branch B), and iron/ceramide dysregulation (Branch B continuation) **culminates in neurodegeneration selectively affecting the basal ganglia (producing dystonia/chorea/ataxia) and the optic nerve/retinal ganglion cells (producing optic atrophy)** — the tissue selectivity for these two structures over others remains incompletely explained (an open mechanistic gap; the retina appears to be affected through a mechanism at least partly independent of the brain-predominant lipoylation defect, per point 4 above).
8. Superimposed catabolic/febrile stress (an environmental modifier, §5) is inferred to acutely exacerbate the underlying bioenergetic deficit at points 4–7, producing the clinically observed episodic worsening after infections or anesthesia; this step is inferred from clinical observation rather than directly mechanistically demonstrated.

### Category detail

- **Molecular pathways:** Mitochondrial fatty acid synthesis II (mtFASII) pathway; lipoic acid biosynthesis pathway; iron-sulfur cluster (ISC) biogenesis pathway; oxidative phosphorylation (Complex I–IV and supercomplex assembly). Suggested GO terms: GO:0006633 (fatty acid biosynthetic process), GO:0009249 (protein lipoylation), GO:0016226 (iron-sulfur cluster assembly), GO:0032981 (mitochondrial respiratory chain complex I assembly), GO:0034551 (mitochondrial respiratory chain complex III assembly).
- **Cellular processes:** mitochondrial bioenergetic failure; iron dyshomeostasis; ceramide/sphingolipid accumulation; secondary neurodegeneration (not classic apoptosis-driven per available data — mechanism of cell death not fully characterized).
- **Protein dysfunction:** MECR protein — depending on variant, either reduced catalytic activity (nonsense/frameshift → truncation/NMD) or reduced protein stability with retained partial function (e.g., R258W, 80% reduced protein level; D304Y, disturbed stability by modeling).
- **Metabolic changes:** deficient lipoic-acid-dependent decarboxylation reactions (pyruvate and α-ketoglutarate dehydrogenase flux); altered acylated vs. unacylated ACP ratio; elevated ceramide.
- **Immune system involvement:** none described; MEPAN is not an immune-mediated or inflammatory disorder.
- **Tissue damage mechanisms:** oxidative stress (implicated by the LHON-like R258W study, which showed lipoic-acid partial rescue attributed to its antioxidant, not lipoylation-restoring, action); iron-catalyzed damage (ferroptosis-adjacent biology plausible given elevated iron/ceramide, though not explicitly termed ferroptosis in the cited work).
- **Biochemical abnormalities:** deficient octanoyl-ACP/lipoic acid synthesis; deficient protein lipoylation; ISC assembly complex instability (↓LYRM4, ↓NFS1, ↓ISCU); altered OXPHOS supercomplex formation.
- **Molecular/-omics profiling:** Proteomic and complexome profiling performed in the *Mecr*-mutant mouse brain (PNAS 2025) demonstrated altered levels of ACP, ISC-complex components, and OXPHOS supercomplexes — the most direct multi-omic mechanistic dataset currently available.
- **Advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR screen data specific to MEPAN were identified in this search; mechanistic insight instead comes from targeted proteomics/complexome analysis in mouse brain and yeast/fly genetic epistasis experiments (iron/ceramide suppressor rescue).

Suggested CL terms for affected cell types: CL:0000617 (GABAergic neuron, basal ganglia medium spiny neurons implicated), CL:0000740 (retinal ganglion cell — the cell type lost in optic atrophy).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** central nervous system — specifically the basal ganglia (caudate, putamen, globus pallidus), and the optic nerve/retina.
- **Secondary:** none robustly documented as a distinct organ-system complication (e.g., no consistently reported cardiac, hepatic, or renal involvement), consistent with a phenotype relatively restricted to the CNS/optic pathway; mild sensorineural hearing impairment was reported in the Italian LHON-like family (an audiologic/otologic secondary finding).
- **Body systems:** nervous system (extrapyramidal motor system), visual system.

**Tissue/cell level:**
- Basal ganglia neurons (medium spiny neurons of caudate/putamen, and pallidal neurons) — targeted by the dystonia/chorea mechanism.
- Retinal ganglion cells and their axons forming the papillomacular bundle — targeted in the optic neuropathy, with OCT showing diffuse retinal nerve fiber layer and ganglion cell layer thinning.
- Suggested UBERON terms: UBERON:0002420 (basal ganglion), UBERON:0001884 (globus pallidus), UBERON:0001873 (caudate nucleus), UBERON:0001874 (putamen), UBERON:0000966 (retina), UBERON:0000941 (optic nerve).

**Subcellular level:**
- Mitochondrial matrix (site of mtFASII and MECR enzymatic activity) — GO Cellular Component: GO:0005759 (mitochondrial matrix); MECR also reported at cytoplasm/nucleus at lower levels (GO:0005737, GO:0005634).
- Iron-sulfur cluster assembly complex within the mitochondrial matrix.

**Localization/laterality:** Bilateral, symmetric involvement in both the basal ganglia MRI findings and the optic atrophy — no lateralization reported, consistent with a systemic metabolic (rather than focal/vascular) mechanism.

---

## 8. Temporal Development

- **Onset:** Congenital/infantile prodrome possible (hypotonia, delayed motor milestones) followed by frank pediatric onset of the movement disorder at 1–6.5 years; optic atrophy onset 4–12 years, essentially always following or co-occurring with (not preceding) the movement disorder in the classic phenotype — though the atypical LHON-like *MECR* R258W family showed optic neuropathy onset as early as age 6 **without** dystonia, illustrating that these two phenotypic axes can dissociate depending on variant.
- **Onset pattern:** insidious/progressive for the baseline trajectory, punctuated by acute step-wise deteriorations associated with febrile illness or anesthesia exposure.
- **Progression:** No formal staging system exists. Course is chronic and progressive; rate is highly variable — from patients maintaining ambulation and some visual function into their 40s–50s, to others losing independent ambulation and functional vision earlier in childhood/adolescence.
- **Disease course pattern:** progressive with superimposed episodic worsenings (not a true relapsing-remitting pattern; deteriorations are typically not followed by full recovery).
- **Disease duration:** chronic, lifelong; not clearly life-limiting based on current (small) cohort — "all currently known affected individuals remain alive, with two in their fifth decade" (GeneReviews), though long-term mortality data are limited by cohort size.
- **Remission:** none reported; this is a neurodegenerative, not relapsing-remitting, disorder.
- **Critical periods:** early childhood (pre-symptomatic to first several years after motor onset) is implicitly the key window for intervention, given that the one well-documented favorable outcome with lipoic acid/C8 supplementation occurred when treatment began within three months of symptom onset (GeneReviews) and in a case where LA was started before optic involvement developed (ScienceDirect Chinese-patient report), suggesting early metabolic supplementation may blunt the phenotype — though this is based on n=1–2 anecdotal reports, not a controlled trial.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** described as affecting fewer than 1 person per 1,000,000 (Orphanet/Wikipedia aggregation); the disease is "ultra-rare."
- **Case counts:** 7 individuals/5 families at first description (2016); 13 individuals/8 families per GeneReviews (2019 update); >30 individuals diagnosed globally by early 2023 (OMIM-derived aggregation), indicating an actively growing ascertained cohort as awareness and testing access increase — not necessarily a true incidence estimate.
- **Incidence:** no formal birth-incidence figure is available; carrier-frequency data in Ashkenazi Jews (see below) allow a rough theoretical incidence estimate for that subpopulation but this was not explicitly published in the sources reviewed.

**Inheritance pattern:** Autosomal recessive. At each conception for a carrier couple: 25% affected, 50% carrier, 25% unaffected; parents are obligate asymptomatic heterozygous carriers.

**Penetrance:** Appears to be high/complete for the biallelic genotype causing *some* phenotype, but **expressivity is markedly variable** (see below) — some sources describe intrafamilial variability suggestive of possible modifiers, though no formal incomplete-penetrance cases (biallelic carriers who are entirely asymptomatic) have been reported in the literature reviewed.

**Expressivity:** Highly **variable**, even between siblings sharing the same genotype — ranging from minimal symptoms to severe disability with total dependence (GeneReviews).

**Genetic anticipation:** Not applicable/not reported; MEPAN is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically reported in the literature reviewed.

**Founder effects:** Yes — two well-characterized Ashkenazi Jewish founder variants (c.695G>A and c.830+2dupT) account for a disproportionate share of reported cases (5 of the original 8 families).

**Consanguinity:** Plausibly relevant for homozygous cases outside the Ashkenazi founder-variant context (e.g., the homozygous Chinese p.Asp304Tyr and Italian p.Arg258Trp cases), though explicit consanguinity was not confirmed as stated for these specific families in the sources reviewed.

**Carrier frequency:** c.695G>A ~1:311 and c.830+2dupT ~1:136 in Ashkenazi Jews (from screening >5,500 Ashkenazi Jewish exomes); population carrier frequency outside this group is not established but is presumably much lower given gnomAD MAFs on the order of 10⁻⁵ for other reported variants.

**Population demographics:**
- Ashkenazi Jewish populations show elevated prevalence due to founder variants; disease is reported worldwide across other ethnicities (Chinese, Italian families documented).
- No sex predilection is described — consistent with autosomal (non-X-linked) inheritance.
- Age distribution of diagnosed individuals spans childhood through the fifth decade of life in the current cohort, reflecting both the chronic non-lethal course and diagnostic delay/historical underrecognition (disease first described only in 2016).

---

## 10. Diagnostics

**Clinical/laboratory tests:** No specific diagnostic biomarker or enzyme assay is in routine clinical use; standard metabolic screening (lactate, organic acids) is used mainly to exclude mimics rather than to positively diagnose MEPAN.

**Neuroimaging:** Brain MRI showing **bilateral hyperintense T2-weighted signal in basal ganglia structures** (caudate, putamen, globus pallidus) at or near dystonia onset is a key suggestive finding; some reports note the pattern can resemble a Leigh-syndrome-like distribution, which is part of why Leigh syndrome sits high on the differential.

**Ophthalmic testing:** Fundus photography, OCT (showing bilateral optic atrophy with papillomacular bundle predilection and RNFL/ganglion cell thinning), visual evoked potentials, electroretinography, visual field testing (Goldmann), and color vision (pseudoisochromatic plates) — used to characterize and stage the optic neuropathy.

**Genetic testing (the definitive diagnostic modality):**
- **Overview:** Diagnosis is established by identifying biallelic pathogenic/likely pathogenic *MECR* variants in a proband with a compatible movement disorder ± optic atrophy phenotype.
- **Single-gene sequencing** of *MECR* — reasonable first step when clinical suspicion is high (compatible phenotype ± Ashkenazi Jewish ancestry).
- **Multigene dystonia panels** — many panels historically did not include *MECR* (a real ascertainment gap noted in GeneReviews), so panel selection must be verified.
- **Exome/genome sequencing (WES/WGS)** — appropriate when phenotype is nonspecific or panel testing is uninformative; this is how most reported cases (including the Chinese and several other families) have been diagnosed.
- **Chromosomal microarray, karyotype, FISH, mitochondrial DNA testing, repeat-expansion testing:** not indicated as primary diagnostic tools for MEPAN, since the disease is caused by small-variant defects in a single nuclear gene, not structural or mtDNA lesions.

**Omics-based diagnostics:** Not part of routine diagnostic workup; research-level fibroblast studies of protein lipoylation status and proteomics have been used to functionally validate variants of uncertain significance in individual cases (e.g., the R258W and D304Y reports).

**Clinical diagnostic criteria:** No formal consensus diagnostic-criteria document exists (this is too rare a disease for a society guideline); diagnosis rests on the combination of phenotype (childhood dystonia + optic atrophy + basal ganglia MRI signal) plus confirmatory biallelic *MECR* genotype.

**Differential diagnosis** (from GeneReviews, NBK540959):
- **Leigh syndrome** (nuclear or mtDNA) — distinguished by seizures, encephalopathy, elevated lactate, brainstem involvement.
- **Glutaric aciduria type 1** — macrocephaly, widened Sylvian fissures, acute dystonic crises, elevated urinary glutaric acid.
- **D-2-hydroxyglutaric aciduria** — seizures, cardiomyopathy, cognitive regression, elevated urinary D-2-HG.
- **Biotin-thiamine-responsive basal ganglia disease** — good response to biotin/thiamine (an important treatable mimic to exclude).
- **Huntington disease** (juvenile) — caudate atrophy, parkinsonism.
- **Neurodegeneration with brain iron accumulation (NBIA)** spectrum — MRI iron accumulation and parkinsonism; notably, MEPAN is explicitly classified by the NBIA advocacy/clinical community as an **"NBIA mimic"** because it does not show true brain iron accumulation on imaging despite phenotypic overlap and despite the iron-dysregulation mechanism demonstrated at the cellular level (nbiacure.org).
- **Wilson disease** — liver disease, Kayser-Fleischer rings.
- Also relevant per the newly described phenotype: **LHON and other mitochondrial optic neuropathies** (OPA1-related dominant optic atrophy, MCAT-related disease) should now include *MECR* in the differential for recessive LHON-like presentations lacking dystonia (Bianco et al. 2024).

**Screening:** No newborn screening or population carrier-screening program specifically targets *MECR*; given the Ashkenazi Jewish founder variants, some Ashkenazi Jewish expanded carrier-screening panels may include *MECR*, though this was not explicitly confirmed as a formal ACMG-recommended addition in the sources reviewed.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival curve or mortality rate has been published given the small cohort size; "all currently known affected individuals remain alive, with two in their fifth decade" (GeneReviews) — suggesting the disease is not acutely life-limiting, though this is based on limited long-term follow-up of a still-small, still-growing cohort, and definitive life-expectancy data are lacking ("Life expectancy: Unknown" — nbiacure.org).
- **Morbidity/function:** Substantial and progressive — motor disability (loss of independent ambulation in some), dysarthria affecting communicative function, and progressive visual impairment up to functional/legal blindness are the dominant morbidity drivers. No validated disease-specific QoL instrument or standardized functional outcome measure was identified.
- **Complications:** Secondary complications relate mainly to motor disability (mobility limitation, feeding/swallowing difficulty from dysphagia) and functional blindness; no evidence of major secondary organ failure.
- **Recovery potential:** Deteriorations associated with febrile illness or anesthesia are typically **not** followed by full recovery — a clinically important and somewhat unusual feature (persistent step-wise decline rather than reversible metabolic crisis), distinguishing it from some other treatable metabolic encephalopathies.
- **Prognostic factors:** Genotype partially correlates with phenotype (e.g., R258W → LHON-like phenotype without dystonia; hypomorphic vs. null alleles may correlate with severity), but intrafamilial variability shows genotype alone is an incomplete predictor. Early initiation of lipoic acid/C8 supplementation is an emerging, though anecdotal, favorable prognostic modifier.
- **Prognostic biomarkers:** None validated for clinical prognostication at this time.

---

## 12. Treatment

There is **no approved disease-modifying or curative therapy**. Management is currently symptomatic/supportive, with an actively developing precision-medicine research pipeline.

**Pharmacotherapy for movement disorder (symptomatic):**
- Anticholinergic agents (e.g., trihexyphenidyl-class) — NCIT:C15986 (Pharmacotherapy)
- Baclofen (GABA-B agonist) — NCIT:C15986
- Benzodiazepines (GABA-A agonists) — NCIT:C15986
- Botulinum toxin injections — reported as used (and having failed) in the DBS case series, implying it is part of the standard symptomatic ladder — NCIT:C15986 / relevant injection procedure term
- **Caution:** dopaminergic agents (e.g., carbidopa-levodopa) have worsened chorea in reported patients and were among the failed therapies in the DBS series — should be used cautiously.

**Metabolic/precision supplementation (investigational but in real-world compassionate use):**
- **Lipoic acid (LA)** and **octanoic acid/C8-rich nutritional supplementation** — mechanistically targeted at the mtFASII/lipoylation defect. One patient showed "remarkable improvement" when LA + C8-rich supplement was started within 3 months of symptom onset (GeneReviews). In the Chinese p.Asp304Tyr patient, LA supplementation was associated with controlled disease progression and **no** development of visual impairment or optic atrophy — the first report explicitly proposing LA as an effective therapeutic strategy for this disease (ScienceDirect, 2020). In the R258W yeast model, LA supplementation partially rescued the growth phenotype, attributed to its **antioxidant** action rather than direct restoration of lipoylation (Bianco et al. 2024).
- "Mito cocktail" (coenzyme Q10, riboflavin, thiamine, alpha-lipoic acid, octanoic acid, vitamin E, vitamin C) — offered empirically by some clinicians; efficacy unproven as a combination (GeneReviews).

**Surgical/interventional (advanced dystonia):**
- **Deep brain stimulation (DBS)** — first published application in MEPAN reported two pediatric siblings (ages 9–10) who had failed pharmacotherapy (benzodiazepines, carbidopa-levodopa, baclofen, botulinum toxin). GPi+PPN and GPi+VIM targeting respectively produced BFMDRS-M improvements of 34.9% and 49.6%, with zero perioperative complications (though one patient had transient tissue devitalization requiring staged lead placement). Authors concluded DBS provides **palliation, not disease modification**, and "can be considered for dystonia in patients with rare metabolic disorders" when pharmacotherapy fails (PMID: [38328756](https://pmc.ncbi.nlm.nih.gov/articles/PMC10847241/)). Note this contrasts with an earlier general caution (some sources state DBS "may be unsuitable due to basal ganglia lesions") — the 2024 case series is the more current, direct evidence and should supersede the earlier caution in curation.

**Supportive/rehabilitative care:**
- Visual aids for decreased acuity
- Occupational and physical therapy for mobility/activities of daily living
- Speech therapy and augmentative/alternative communication for dysarthria
- Feeding support as needed for dysphagia
- NCIT terms: NCIT:C15302 (Physical Therapy), NCIT:C15747 (Supportive Care), speech/OT via NCIT:C159273 / NCIT:C121351.

**Surveillance:** Yearly ophthalmologic, neurologic, speech-therapy, cognitive, and feeding evaluations recommended to track progression and trigger timely intervention (GeneReviews).

**Advanced/experimental therapeutics in development:**
- **AAV9-mediated gene therapy** — preclinical work (University of Florida, supported by the MEPAN Foundation) has shown successful MECR protein expression after AAV9-MECR transfection in HEK293T and Neuro-2a cells, aiming to deliver functional MECR to brain and retina; leverages precedent from FDA-approved AAV gene therapies (e.g., for SMA, LHON) (mepan.org/precision).
- **Drug repurposing — echinocandin antifungals (anidulafungin, micafungin):** Screened on MEPAN patient fibroblasts using Seahorse oxygen-consumption/ATP-production assays; anidulafungin ranked best, followed by micafungin. Echinocandins rescued MECR-deficient yeast growth — notable because their canonical fungal target (glucan synthase) does not exist in human cells, implying a favorable safety profile if repurposed. Rescue was effective only for **missense** MECR mutants retaining a foldable protein (not for null/truncating alleles), and newer-generation echinocandins (micafungin, anidulafungin) lack the high-dose toxicity seen with first-generation caspofungin (Perlara "Cure Odysseys" drug-repurposing program, described in search aggregation; primary peer-reviewed publication not yet identified in this search — should be treated as an early-stage/preprint-level lead pending verification).
- **Engineered bacterial lipoate ligase** — proposed strategy to bypass the defective endogenous lipoic acid synthesis step (mentioned in Wikipedia's synthesis of primary literature; specific citation not independently verified in this search).
- **MECR G165Q engineered variant studies** (Nature Communications 2023, PMC9899272) demonstrate that long-chain acyl-ACPs are indispensable for mitochondrial respiration distinct from octanoylation for lipoylation — informing structure-function rationale for future targeted therapeutics, though this is a basic-science mechanistic paper rather than a therapeutic trial.

**Clinical trials:** No MEPAN-specific interventional trial (e.g., an NCT-registered gene-therapy or drug trial) was identified as currently active in this search; the UMDF and MEPAN Foundation direct patients to general rare-disease clinical-trial finders and the mitoSHARE patient registry (umdf.org) rather than to a disease-specific active trial.

**Treatment outcomes/adverse events:** No systematic response-rate or FAERS-type adverse-event data exist given the small population; adverse treatment signals identified are anecdotal (dopaminergic worsening of chorea; anesthesia/propofol-associated decline).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause); the principal "primary prevention" avenue is **reproductive genetic counseling and carrier screening** in at-risk families/populations (especially Ashkenazi Jewish individuals, given the founder-variant carrier frequencies above).
- **Secondary prevention:** Early diagnosis via genetic testing in at-risk families (once a proband's variants are known) allows presymptomatic identification and, per anecdotal reports, earlier initiation of lipoic acid/C8 supplementation — plausibly delaying or attenuating symptom onset/severity, though this has not been tested in a controlled trial.
- **Tertiary prevention:** Surveillance program (annual ophthalmologic, neurologic, speech, cognitive, feeding evaluation) aims to catch and manage complications (visual decline, dysphagia, communication loss) before they become severe; avoidance of known precipitants (febrile decompensation management, cautious anesthesia planning, avoidance of dopaminergic agents) constitutes practical tertiary prevention.
- **Genetic counseling:** Carrier testing, prenatal testing, and preimplantation genetic diagnosis (PGD) are available once familial *MECR* variants are known (GeneReviews). Young adult carriers/at-risk relatives should receive reproductive counseling.
- **Screening:** No formal population-based newborn screening program includes MEPAN; targeted carrier screening may be offered within expanded Ashkenazi Jewish carrier panels in some laboratories, though this was not explicitly confirmed in the sources reviewed as an ACMG-endorsed standard.
- **Immunization/public health/prophylaxis:** Not applicable — MEPAN is not infectious or vaccine-preventable; there is no established prophylactic medication regimen (LA/C8 supplementation is disease-modifying-intent therapy, not formal "prophylaxis" in the public-health sense, though it functions similarly at the individual level).

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** No naturally occurring MEPAN-equivalent disease has been documented in non-human species (no veterinary case reports or OMIA entries were identified in this search) — MEPAN currently appears to be a human-specific clinical entity, with all cross-species data derived from engineered/induced models rather than natural disease.
- **Orthologous gene:** *MECR* orthologs exist across eukaryotes: *Drosophila* Mecr (single ortholog), *C. elegans* mecr-1/W09H1.5 (a longevity-associated gene), *S. cerevisiae* ETR1, and murine *Mecr*.
- **Comparative biology:** The core mtFASII pathway and MECR's terminal enoyl-reductase role are evolutionarily conserved from yeast to humans, evidenced by the fact that human MECR complements yeast *Δetr1* respiratory and lipoylation defects, and that engineered *Drosophila* lines expressing human wild-type or patient-variant *MECR* recapitulate aspects of the human disease.
- **Zoonotic potential/transmission:** Not applicable — MEPAN is a purely genetic, non-transmissible disorder.

---

## 15. Model Organisms

MEPAN modeling spans yeast, nematode, fly, and mouse — an unusually complete cross-species toolkit for an ultra-rare disease, reflecting the deep evolutionary conservation of mtFASII.

**Yeast (*Saccharomyces cerevisiae*):**
- *Δetr1* (Etr1p-null) mutant yeast fail to synthesize sufficient lipoic acid or assemble cytochrome complexes and cannot respire/grow on non-fermentable carbon sources.
- Human MECR (wild-type and patient-variant constructs, e.g., R258W) complements/fails to complement this strain, providing a rapid functional assay for variant pathogenicity, protein stability, and drug-rescue screening (including the echinocandin repurposing work).

**Nematode (*C. elegans*):** mecr-1/W09H1.5 encodes the 2-trans-enoyl-thioester reductase; ectopic expression of nematode mecr-1 in yeast Δetr1 restores reductase activity and phenotype rescue, and mecr-1 itself is described as a **longevity-associated gene**, connecting mtFAS to organismal aging biology (PMC2774161).

**Fruit fly (*Drosophila melanogaster*):**
- Whole-body loss of *Mecr* is **lethal**; **neuron-specific knockdown** produces **progressive neurodegeneration**, recapitulating the human neurological phenotype.
- Mechanistically, flies lacking *mecr* show Fe–S cluster biogenesis defects and elevated iron levels, leading to elevated ceramide; genetically or pharmacologically **lowering either iron or ceramide suppresses the neurodegenerative phenotype** — the clearest causal (interventional) evidence in the entire mechanistic literature (Tesch et al., *Nature Metabolism* 2023;5:1595–1614, PMID: [37653044](https://ncbi.nlm.nih.gov/pmc/articles/PMC11151872)). Human MEPAN patient fibroblasts independently show the same elevated-ceramide/impaired-iron-homeostasis signature, supporting translational relevance of the fly findings to human disease.
- UAS constructs carrying human wild-type and disease-variant *MECR* have been introduced into flies for structure-function and rescue studies (FlyBase Human Disease Model Report FBhh0001544).

**Mouse (*Mus musculus*):**
- A compound-heterozygous *Mecr*-mutant mouse model (Murdock et al., *PNAS* 2025;122(40):e2506761122, PMID: 41021813) recapitulates the core triad: **movement disorder, optic neuropathy, and defective protein lipoylation**, plus **reduced brain mitochondrial oxidative phosphorylation**.
- Proteomic/complexome profiling of mutant mouse brain revealed destabilization of the ISC assembly complex (↓LYRM4, ↓NFS1, ↓ISCU) and altered OXPHOS complex/supercomplex assembly, tied to loss of acylated ACP — this is currently the highest-fidelity mammalian model and the primary source of the ISC/supercomplex mechanistic branch described in Section 6.
- **Phenotype recapitulation:** high fidelity for movement disorder, optic neuropathy, and biochemical lipoylation defect.
- **Model limitations:** Explicit limitations were not detailed in the fetched abstract summary; general caution for any mouse CNS model — potential differences in basal ganglia circuitry/dystonia phenotyping between mouse and human, and uncertain translatability of the iron/ceramide suppressor findings (established in fly, "confirmed" only as elevated markers, not as an interventional rescue, in mouse/human fibroblasts per the sources reviewed) should be flagged as a human-model-fidelity open question.

**Cell-based models:** Patient-derived dermal fibroblasts (multiple case reports) are the standard human cellular model, used for lipoylation Western blots, Seahorse OCR/ATP assays (echinocandin screening), and ceramide/iron measurement.

**Resource note:** No mouse strain repository ID (JAX/MGI stock number), zebrafish (ZFIN), or dedicated cell-line repository (ATCC/Cellosaurus) accession for a MEPAN-specific model was identified in this search; the fly model is registered in FlyBase (FBhh0001544).

---

## Summary Table of Key Evidence Sources

| Topic | Primary citation | PMID/DOI |
|---|---|---|
| Original disease description, MECR mutations, 7 pts/5 families | Heimer et al., *Am J Hum Genet* 2016;99:1229–44 | PMID 27817865 |
| GeneReviews clinical/genetic summary | Heimer/Baris et al., *MECR-Related Neurologic Disorder*, GeneReviews (NCBI Bookshelf) | NBK540959 |
| OMIM entries | Gene *608205; Phenotype #617282 (DYTOABG) | omim.org/entry/608205, /617282 |
| Orphanet | MEPAN syndrome | ORPHA:508093 |
| Mouse model — ISC/supercomplex mechanism | Murdock et al., *PNAS* 2025;122(40):e2506761122 | PMID 41021813 |
| Drosophila model — iron/ceramide mechanism | Tesch et al., *Nat Metab* 2023;5:1595–1614 | PMID 37653044 |
| LHON-like phenotype (R258W) | Bianco et al., *J Med Genet* 2024 | PMID 37734847 |
| Chinese patient, no optic atrophy, LA response | ScienceDirect, *Mitochondrion* 2020 | PMID (search) 32853756* |
| Ophthalmic manifestations case study | *Ophthalmic Genetics* 2022;44(5) | DOI 10.1080/13816810.2022.2135112 |
| Deep brain stimulation case series | *J Neurosurg Pediatr* / PMC10847241 2024 | PMID 38328756 |
| Engineered MECR variant / long-chain acyl-ACP | *Nat Commun* 2023 | PMC9899272 |

*PMID for the Chinese-patient ScienceDirect paper was not independently confirmed via direct PubMed fetch in this session and should be re-verified before use in a curated evidence item.

---

## Notes on Evidence Gaps and Confidence

- Several claims here rely on **search-engine-summarized abstracts** rather than full-text primary-source verification (WebFetch was blocked by paywalls/bot-protection for OMIM, Orphanet's direct page, the Nature Metabolism full text, and PubMed's abstract page). GeneReviews (NBK540959) is the one source fully retrieved and directly quotable; it should be treated as the highest-confidence source in this report.
- The **echinocandin drug-repurposing** findings derive from a patient-advocacy/foundation-affiliated substack summary (Perlara), not a verified peer-reviewed publication in this search — flag as a preprint/lead-stage claim requiring primary-literature confirmation before curation.
- The **"engineered bacterial lipoate ligase"** bypass strategy and the exact PMID for the Chinese-patient case report should be independently verified against PubMed/the primary article before being entered as sourced KB claims, per this repository's evidence-sourcing policy (no assertion without a verified PMID/DOI and exact snippet).
- Quantitative epidemiologic figures (>30 diagnosed by 2023, carrier frequencies) come from secondary aggregations (OMIM search summaries, GeneReviews) rather directly quoted primary tables in every instance — treat the exact numbers as approximate pending direct-source confirmation.