---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T14:54:05.370381'
end_time: '2026-09-03T14:57:13.514311'
duration_seconds: 188.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PAPA Syndrome
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
  web_search_requests: 11
  num_turns: 13
  total_cost_usd: 0.9084305999999999
  session_id: eccb37f5-d277-53f4-9bc9-b541745fd0d8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PAPA Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PAPA Syndrome** covering all of the
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

I have enough material to compile a comprehensive, well-cited report now.

---

# PAPA Syndrome (Pyogenic Sterile Arthritis, Pyoderma Gangrenosum, and Acne Syndrome)

## 1. Disease Information

**Overview.** PAPA syndrome is a rare, autosomal dominant monogenic autoinflammatory disorder caused by heterozygous pathogenic variants in *PSTPIP1* (proline-serine-threonine phosphatase-interacting protein 1, also historically named *CD2BP1*), located at 15q24.3. It is the prototype of a broader "PSTPIP1-associated inflammatory diseases" (PAID) spectrum. It was first delineated clinically by Lindor et al. (1997) as "a new autosomal dominant disorder of pyogenic sterile arthritis, pyoderma gangrenosum, and acne" ([ScienceDirect summary](https://www.sciencedirect.com/science/article/abs/pii/S0025619611635659)), and the causal gene was identified by Wise et al., *Human Molecular Genetics* 2002 (PMID not directly returned by search but DOI 10.1093/hmg/11.8.961), who found co-segregating *CD2BP1/PSTPIP1* mutations (p.E250Q, p.A230T) in two multiplex families and showed by yeast two-hybrid assay that both severely reduce binding to PTP-PEST ([Wise et al. 2002](https://academic.oup.com/hmg/article-abstract/11/8/961/638530)).

**Key identifiers:**
- **OMIM:** 604416 — "Pyogenic Sterile Arthritis, Pyoderma Gangrenosum, and Acne" ([OMIM:604416](https://omim.org/entry/604416))
- **Orphanet:** ORPHA:69126 ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=69126&lng=EN))
- **MONDO:** MONDO:0011462 ([Wikidata cross-reference](https://www.wikidata.org/wiki/Q7118181))
- **Gene:** PSTPIP1 (HGNC:9581), chr15q24.3, also historically CD2BP1
- Common synonyms: PAPA syndrome; Pyogenic Arthritis-Pyoderma Gangrenosum-Acne syndrome; Familial recurrent arthritis

**Evidence basis.** Almost all published data derive from aggregated case reports/case series and family pedigrees (individual-patient level, not large-cohort EHR data) — this is one of the rarest monogenic autoinflammatory diseases, with the literature dominated by single-family and small-series reports rather than registries.

---

## 2. Etiology

**Disease causal factor — genetic, single-gene, autosomal dominant.** PAPA syndrome is caused by heterozygous missense variants in *PSTPIP1*. The two "classic," functionally validated PAPA-causing variants are **p.A230T** and **p.E250Q** (originally reported as E250Q; some literature also refers to it as **E250K** in the context of the related PAMI phenotype — see below), both located in the coiled-coil domain of PSTPIP1 and both shown to abolish binding to the phosphatase PTP-PEST by yeast two-hybrid assay ([Wise 2002](https://academic.oup.com/hmg/article-abstract/11/8/961/638530)). Additional variants — **p.D246N** and **p.E257G** — are classified as "likely pathogenic" based on absence from population databases, location within the same critical PSTPIP1 domain, and de novo occurrence without family history ([Frontiers Genetics case report/review, 2026](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2026.1825761/full)).

**Genetic risk factors.** The causal variants themselves are the dominant risk factor; PAPA syndrome shows **autosomal dominant inheritance with incomplete penetrance and variable expressivity** — even within the same family and the same variant, disease severity and organ involvement vary substantially ([PMC3737487, genotype-phenotype study of 5 patients](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)). No environmental cause is established; physical trauma is a recognized **trigger** of flares (pathergy) rather than a cause.

**Gene-environment interaction.** The clearest gene-environment interplay is **pathergy** — minor trauma or injection precipitates sterile abscesses and joint flares in genetically susceptible (PSTPIP1-mutant) individuals, attributed to dysregulated neutrophil recruitment and IL-1β hyperproduction at sites of minor injury.

**Protective factors.** None are established in the literature; this is expected for an ultra-rare, highly penetrant single-gene autosomal dominant disorder.

---

## 3. Phenotypes

### Articular
- **Sterile pyogenic (destructive) arthritis** — HP:0033798 (Sterile pyogenic arthritis) or generically HP:0001369 (Arthritis). Recurrent, migratory, typically **monoarticular** flares, most often affecting elbows, knees, and ankles; occurs spontaneously or after minor trauma; leads to accumulation of sterile purulent synovial fluid and, if untreated, joint destruction ([PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487); [imaging review, Pediatric Radiology 2018](https://link.springer.com/article/10.1007/s00247-018-4246-1)). Synovial fluid shows exceedingly high (often >100,000/mm³) sterile neutrophilic white cell counts, a key differentiator from true septic arthritis ([PubMed 28251506](https://pubmed.ncbi.nlm.nih.gov/28251506/)).
  - **Onset:** typically early childhood.
  - **Course:** arthritis tends to subside by/after puberty as cutaneous disease intensifies.

### Cutaneous
- **Pyoderma gangrenosum** (HP:0031928 or general "cutaneous ulceration") — recurrent, non-healing, sterile skin ulcers, often triggered by minor trauma (pathergy). Onset generally later than arthritis — adolescence/early adulthood.
- **Severe cystic/nodulocystic acne** (HP:0001061 Acne inversa / cystic acne terms) — often severe and scarring, emerging around/after puberty.
- **Pathergy** — exaggerated inflammatory response and sterile abscess formation at injection or injury sites (a hallmark clinical sign, similar to Behçet disease pathergy).
- Suppurative/pyogenic skin abscesses; in the extended PAID spectrum, hidradenitis suppurativa (see PASH/PAPASH below).

### Laboratory abnormalities
- Elevated acute-phase reactants during flares (ESR, CRP).
- Markedly elevated **IL-1β** and circulating neutrophil granule enzymes compared to controls ([PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)).
- In the PAMI end of the spectrum: hyperzincemia, hypercalprotectinemia (very high S100A8/A9 / MRP8-14), cytopenias.

**Phenotype pattern:** temporal segregation is a defining clinical feature — arthritis dominates in **childhood**, and cutaneous disease (PG, acne) dominates from **puberty onward**, though this is variable between and within families (incomplete penetrance/variable expressivity).

**Quality of life impact.** Disfiguring/scarring skin disease (PG scars, cystic acne scarring) and destructive arthritis both carry substantial psychosocial and functional burden; specific EQ-5D/SF-36 data for PAPA syndrome were not identified in this search and are likely absent given disease rarity — flag as a gap.

---

## 4. Genetic/Molecular Information

**Causal gene:** *PSTPIP1* / HGNC:9581, chr15q24.3; OMIM gene entry 606347 (gene), disease entry 604416.

**Pathogenic variants (classic/validated):**
| Variant | Classification | Domain | Functional evidence |
|---|---|---|---|
| p.A230T | Pathogenic | Coiled-coil | Segregates in families; disrupts PTP-PEST binding, ↑pyrin binding |
| p.E250Q | Pathogenic | Coiled-coil | Segregates in families; disrupts PTP-PEST binding, ↑pyrin binding |
| p.D246N | Likely pathogenic | Coiled-coil | De novo, absent from population DBs |
| p.E257G | Likely pathogenic | Coiled-coil | De novo, absent from population DBs |

A recent systematic review of PAMI-spectrum cases found **41/43 (95%) carried the heterozygous p.E250K variant** ([PMC10454568, PAMI systematic review, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10454568/)) — note this is a distinct variant from the classic PAPA-causing E250Q, illustrating allelic heterogeneity across the PSTPIP1-associated disease spectrum (genotype–phenotype correlations discussed further under §9).

**Variant type/class:** All known causal variants are **missense**, clustered in the coiled-coil domain of PSTPIP1.

**Functional consequence — gain-of-function/dominant-negative-type effect at the protein-interaction level:** PAPA-associated PSTPIP1 mutants show **reduced binding to PTP-PEST**, leading to hyperphosphorylation of PSTPIP1 and consequent **markedly increased affinity for pyrin (MEFV)** ([PLOS ONE, PMC2702820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702820/); [WebSearch synthesis of PSTPIP1-pyrin mechanism]). This is a molecular gain-of-interaction rather than classic enzymatic gain/loss of function.

**Modifier considerations:** No formal modifier genes are established, but marked intrafamilial variable expressivity (documented in the same 5-patient genotype-phenotype series) implies unidentified genetic or stochastic modifiers ([PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)).

**Allele frequency:** These variants are private/rare, essentially absent from population databases (gnomAD) consistent with high penetrance dominant disease-causing status; specific allele-frequency figures were not returned by this search pass.

**Epigenetics/chromosomal abnormalities:** Not applicable — PAPA syndrome is a point-mutation Mendelian disorder; no epigenetic mechanism or copy-number/translocation etiology is described in the literature surveyed.

---

## 5. Environmental Information

- **Physical trauma / minor injury** is the principal recognized environmental trigger, producing the pathergy phenomenon at both joint and skin sites.
- No specific toxin, infectious agent, or occupational exposure is implicated as causal; this is consistent with a fully genetically determined disease.
- No infectious trigger is causal, although the arthritis and skin lesions can be clinically mistaken for infection (hence "pyogenic," "gangrenosum" naming) — a critical **differential-diagnosis** point rather than a true infectious etiology.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from mutation to clinical manifestation):**

1. A heterozygous missense variant (e.g., p.A230T, p.E250Q) in the coiled-coil domain of *PSTPIP1* **leads to** markedly reduced binding affinity between PSTPIP1 and the tyrosine phosphatase **PTP-PEST** (demonstrated by yeast two-hybrid; [Wise 2002](https://academic.oup.com/hmg/article-abstract/11/8/961/638530)).
2. Reduced PTP-PEST engagement **results in** loss of PTP-PEST-mediated dephosphorylation of PSTPIP1, so mutant PSTPIP1 accumulates in a **hyperphosphorylated** state ([PMC2702820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702820/)).
3. Hyperphosphorylated PSTPIP1 **leads to** markedly increased binding affinity for **pyrin (encoded by *MEFV*, the familial Mediterranean fever gene)** — mechanistically linking PAPA syndrome to the same pyrin-inflammasome pathway as FMF ([PNAS, pyrin-PSTPIP1 binding paper](https://www.pnas.org/doi/10.1073/pnas.2135380100); [WebSearch synthesis]).
4. Enhanced pyrin–PSTPIP1 binding **results in** pyrin being recruited (via PSTPIP1) into **ASC specks** with unusually high efficiency — i.e., PAPA-mutant PSTPIP1 promotes assembly of the **pyrin inflammasome** ([PMC2702820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702820/)).
5. Pyrin inflammasome assembly **activates caspase-1**, which cleaves pro-IL-1β and pro-IL-18 into their active, secreted forms ([WebSearch synthesis, pyrin-inflammasome-caspase-1-IL-1β cascade]).
6. IL-1β/IL-18 overproduction, together with dysregulated neutrophil chemotaxis (PSTPIP1's independent cytoskeletal role — see step 7), **drives** local and systemic sterile neutrophilic inflammation.
7. **Branch — cytoskeletal/adaptor arm (parallel, upstream-independent of inflammasome):** wild-type PSTPIP1 is an F-BAR–domain cytoskeleton-associated adaptor that (a) in T cells, bridges **CD2** to **WASP (Wiskott-Aldrich syndrome protein)**, coupling TCR engagement to actin polymerization required for immunological synapse formation ([PubMed 12530983](https://pubmed.ncbi.nlm.nih.gov/12530983/)); and (b) in neutrophils/macrophages, localizes to the trailing uropod edge with PIP5K1C/DNM2 to regulate migration, and controls extracellular-matrix degradation and filopodia formation via podosome regulation ([Blood, ASH publications](https://ashpublications.org/blood/article/123/17/2703/32540/The-F-BAR-protein-PSTPIP1-controls-extracellular)). PAPA-mutant PSTPIP1 perturbs this cytoskeletal-regulatory function, contributing to exaggerated neutrophil influx at sites of minor trauma — the cellular basis of **pathergy**.
8. Excess IL-1β/IL-18 signaling plus exaggerated, trauma-triggered neutrophil infiltration **culminate in** the clinical triad: sterile pyogenic (neutrophil-rich) destructive arthritis, pyoderma gangrenosum ulceration, and severe cystic acne — with a temporal pattern in which arthritis predominates in childhood (when trauma/joint use is high) and cutaneous disease predominates from puberty onward (hormonally influenced acne, ongoing pathergy-driven ulceration).

**Inferential note:** the step linking hyperphosphorylation directly to increased pyrin binding (step 3) and the step linking cytoskeletal dysregulation quantitatively to pathergy severity (step 7→8) are supported mainly by in vitro biochemical and cell-biology studies; direct demonstration that this cascade alone (absent the cytoskeletal arm) is sufficient to produce the full clinical triad in vivo is not established — the mouse model data (below) show a **dissociation** between systemic cytokine elevation and clinical skin/joint phenotype, indicating the causal chain from IL-1β elevation to organ-specific lesion formation is incompletely modeled.

**Molecular pathways:** pyrin (MEFV) inflammasome pathway; IL-1β/IL-18 (caspase-1) signaling; CD2–WASP–actin cytoskeletal signaling (immunological synapse formation); F-BAR-domain membrane remodeling/podosome regulation.

**Cell types involved (candidate CL terms):**
- Neutrophils (CL:0000775) — pathergy, sterile arthritis/PG neutrophilic infiltrate
- Macrophages (CL:0000235) — cytoskeletal/podosome dysfunction, IL-1β production
- T lymphocytes (CL:0000084) — CD2/WASP synapse dysfunction
- Synoviocytes/synovial fibroblasts — site of joint inflammation

**Suggested GO terms:**
- GO:0043123 — positive regulation of canonical NF-kappaB signal transduction (downstream inflammatory signaling)
- GO:0002534 — cytokine production involved in inflammatory response
- GO:0097169 — AIM2 inflammasome complex assembly (analogous; pyrin inflammasome-specific GO term GO:0072559 "NLRP1 inflammasome complex" is not exact — best available may be the general "inflammasome complex" GO:0061702)
- GO:0030041 — actin filament polymerization
- GO:0002376 — immune system process (broad, for CD2/WASP synapse formation)

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** joints (elbows, knees, ankles predominant), skin (site of PG ulcers and acne).
- **Secondary:** in the PAMI/PSTPIP1-spectrum extreme, reticuloendothelial system — hepatosplenomegaly, lymphadenopathy, bone marrow (cytopenias).
- **Body systems:** musculoskeletal, integumentary, immune (innate).
- **Tissue/cell level:** synovium (neutrophilic synovitis), dermis/epidermis (ulcerative pyoderma gangrenosum, pilosebaceous unit in acne).
- **Subcellular:** cytoskeleton/cell cortex (F-BAR domain membrane deformation, filopodia/podosome structures), cytoplasmic inflammasome (ASC speck) assembly.
- **Candidate UBERON terms:** UBERON:0000982 (synovial joint), UBERON:0002097 (skin of body), UBERON:0001004 (respiratory system - N/A here), UBERON:0002370 (thymus - N/A). Most relevant: UBERON:0000982 (joint), UBERON:0002097 (skin).
- **Laterality:** typically unilateral/asymmetric during individual arthritis flares (migratory monoarticular pattern), though different joints affected over time.

---

## 8. Temporal Development

- **Onset:** childhood, classically before age 10, sometimes as early as infancy for arthritis; cutaneous manifestations (PG, cystic acne) typically emerge later, around puberty/adolescence.
- **Pattern:** episodic/relapsing-remitting for both arthritis and PG flares, often trauma-triggered (pathergy).
- **Progression:** arthritis is most active in childhood/pre-puberty and tends to attenuate afterward; cutaneous disease (PG and severe acne) increases from puberty into adulthood — a documented "phenotypic switch" over the disease course ([PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)).
- **Duration:** chronic, lifelong (though joint disease activity often diminishes with age; residual joint damage from earlier destructive flares may persist).
- **Critical periods:** childhood/adolescence — periods of highest inflammatory activity, when early diagnosis and IL-1 blockade could in principle limit joint destruction and cutaneous scarring; this is inferred rather than demonstrated by controlled trial data given disease rarity.

---

## 9. Inheritance and Population

- **Epidemiology:** exceptionally rare; **prevalence <1 per 1,000,000**. As of the WebSearch source cited, only ~34 patients from 5 kindreds (2 US, 1 Italian, 1 Dutch, 1 New Zealand) had been formally reported in the classic literature ([WebSearch summary; see also Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=69126)); subsequent case reports (including a 2026 Chinese family report) have added further cases but the total remains in the low hundreds worldwide across the full PSTPIP1-spectrum literature.
- **Inheritance pattern:** autosomal dominant.
- **Penetrance:** incomplete.
- **Expressivity:** markedly variable, both between and within families (documented directly in the 5-patient genotype-phenotype study, [PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)).
- **Genetic anticipation:** not reported/expected (not a repeat-expansion disorder).
- **Founder effects/consanguinity:** not specifically reported for the classic PAPA-causing variants; several kindreds independently ascertained across different populations/geographies.
- **Genotype–phenotype spectrum note:** the E250K (as opposed to classic E250Q) and E257K variants are specifically associated with the more severe **PAMI** phenotype (myeloid-related proteinemia, hyperzincemia/hypercalprotectinemia, cytopenias, failure to thrive) rather than classic PAPA — an important within-gene genotype-phenotype correlation to track separately in curation ([PMC10454568](https://pmc.ncbi.nlm.nih.gov/articles/PMC10454568/); [Sciencedirect phenotype-genotype paper](https://www.sciencedirect.com/science/article/pii/S0022202X20321680)/[PubMed 33218716](https://pubmed.ncbi.nlm.nih.gov/33218716/)).
- **Sex ratio / geographic distribution:** no strong sex predilection or endemic geographic clustering reported in the sources surveyed.

---

## 10. Diagnostics

**Clinical/laboratory:**
- Synovial fluid analysis: exceedingly high, sterile neutrophilic cell counts (differentiates from true septic arthritis) — a key diagnostic discriminator emphasized in a dedicated case series ([PubMed 28251506](https://pubmed.ncbi.nlm.nih.gov/28251506/)).
- Elevated ESR/CRP during flares; elevated IL-1β; in PAMI-spectrum disease, markedly elevated serum zinc and calprotectin (S100A8/A9).
- Imaging (radiographs, MRI, ultrasound) used to characterize joint destruction and differentiate from infectious/other inflammatory arthritis — reviewed specifically for PAPA in a Pediatric Radiology imaging-findings paper ([Springer 2018](https://link.springer.com/article/10.1007/s00247-018-4246-1)).
- Skin biopsy of PG lesions: neutrophilic dermatosis pattern (nonspecific but supportive).

**Genetic testing:** Single-gene sequencing of *PSTPIP1* (Sanger or targeted NGS) is the diagnostic standard given the small number of known causal variants clustering in the coiled-coil domain; autoinflammatory-disease gene panels including *PSTPIP1*, *MEFV*, *NLRP3*, *TNFRSF1A*, *MVK*, etc. are commonly used given phenotypic overlap with other periodic fever/autoinflammatory syndromes.

**Clinical criteria / differential diagnosis:** No formal consensus diagnostic criteria akin to DSM/ICD were identified in this search; diagnosis remains clinical, supported by genetic confirmation. Key differentials:
- **Septic arthritis** (ruled out by sterile cultures despite very high synovial WBC).
- **Pyoderma gangrenosum from other causes** (IBD-associated, idiopathic).
- **PASH syndrome** (Pyoderma gangrenosum, Acne, Suppurative Hidradenitis) — **lacks** the sterile pyogenic arthritis of PAPA; caused variably by *PSTPIP1* variants or other/no identified gene ([PubMed 21745697](https://pubmed.ncbi.nlm.nih.gov/21745697/)).
- **PAPASH** (PAPA + hidradenitis suppurativa).
- **PsAPASH** (PASH + psoriatic arthritis).
- **PASS syndrome** (PG, acne, ankylosing spondylitis ± hidradenitis suppurativa).
- **PAC syndrome** (PG, acne, ulcerative colitis).
- **PAMI syndrome** (PSTPIP1-associated myeloid-related proteinemia inflammatory syndrome) — a more severe, often earlier-onset phenotype associated specifically with E250K/E257K, featuring failure to thrive, lymphadenopathy, splenomegaly, and cytopenias in addition to/preceding classic PAPA features.
(Spectrum summarized in [WebSearch synthesis of differential-diagnosis sources, including DermNet NZ](https://dermnetnz.org/topics/papa-syndrome).)

---

## 11. Outcome/Prognosis

- No formal survival/mortality statistics are established — PAPA syndrome is not typically fatal, but morbidity from joint destruction and disfiguring cutaneous scarring can be substantial if untreated.
- **Morbidity:** destructive arthropathy (if arthritis flares are inadequately controlled in childhood), disfiguring PG scarring, severe acne scarring.
- **Complications:** secondary infection of ulcerated PG lesions; in PAMI-spectrum disease, cytopenias and growth failure add additional morbidity.
- **Prognostic factors:** early recognition and IL-1 pathway blockade may limit long-term joint damage and scarring, though this is inferred from case-series treatment response data rather than controlled prognostic studies (disease too rare for such studies to exist).

---

## 12. Treatment

**Pharmacotherapy — biologics targeting IL-1 and TNF pathways are the mainstay:**

- **Anti-IL-1 agents (anakinra, canakinumab):** most effective for the **arthritis** component; **markedly lower efficacy against PG and acne** according to a 2025 systematic review of 10 case-report studies (19 patients total) ([Springer Nature, Archives of Dermatological Research 2025](https://link.springer.com/article/10.1007/s00403-025-04324-6)). Canakinumab (dosed every 4-8 weeks) shows better compliance and fewer injection-site reactions than daily anakinra, though head-to-head comparative data remain limited; both are used, but the review explicitly calls for RCTs given the current evidence base is limited to small case series.
- **Anti-TNF agents (etanercept, adalimumab, infliximab, golimumab):** also reported effective, with some evidence that infliximab or high-dose golimumab may outperform etanercept/adalimumab for **severe PG lesions** specifically ([WebSearch synthesis; foundational case report: PubMed 15580218, abnormal TNF-α production and etanercept efficacy](https://pubmed.ncbi.nlm.nih.gov/15580218/); [Use of TNF inhibitors in PAPA syndrome, PMC4599379](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4599379/)).
- **Combination anti-TNF + anti-IL-1 therapy:** used for cases refractory to monotherapy with either class, reported as more effective than escalating corticosteroids ([WebSearch synthesis of combination-therapy case reports](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3952270/)).
- **Corticosteroids** (systemic and intralesional/intra-articular): used historically and still commonly as adjunct/bridge therapy, though associated with significant toxicity with prolonged use.

**Suggested NCIT terms:**
- NCIT:C15986 (Pharmacotherapy) — generic action
- Anakinra: therapeutic_agent candidate (NCIT has an "Anakinra" concept; verify exact CURIE via OAK before curation — not independently confirmed in this search pass)
- Canakinumab, Infliximab, Etanercept, Adalimumab — likewise verify exact NCIT CURIEs at curation time
- NCIT:C2874 (Corticosteroid) class-level term as an alternative/adjunct

**Surgical/supportive:** avoidance of unnecessary surgical intervention/injections given pathergy risk; wound care for PG ulcers; dermatologic management of acne (isotretinoin reported in some case series, though can be associated with flares in some autoinflammatory-adjacent conditions — verify per-case before curating as a general recommendation).

**Experimental/emerging:** No PAPA-syndrome-specific registered clinical trials (NCT) were identified in this search pass; given the disease's rarity, most treatment evidence is derived from off-label biologic use documented in case reports/series rather than formal trials — this should be flagged as an evidence gap when curating `clinical_trials`.

---

## 13. Prevention

- No primary prevention exists for this monogenic dominant disorder beyond genetic counseling for at-risk family members (each child of an affected parent has ~50% inheritance risk, subject to incomplete penetrance).
- **Secondary/tertiary prevention:** the central actionable preventive strategy documented in the literature is **avoidance of unnecessary trauma/injections** to minimize pathergy-triggered flares, plus early initiation of IL-1/TNF-targeted therapy to prevent cumulative joint destruction and cutaneous scarring.
- **Genetic counseling:** appropriate given autosomal dominant inheritance with variable expressivity; prenatal/preimplantation testing is technically feasible via single-gene *PSTPIP1* testing but is not routinely reported as clinical practice for this non-lethal, treatable disorder.

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary/companion-animal PAPA-syndrome-equivalent disease was identified in this search (searches for OMIA-style veterinary correlates did not surface a distinct entry); this should be recorded as **absent/not identified** rather than assumed absent.
- Comparative biology is instead addressed through **engineered mouse models** (below) rather than naturally occurring animal disease.

---

## 15. Model Organisms

**Genetic mouse model — A230T knock-in/ectopic expression:**
- Mice **ectopically/ubiquitously expressing human PAPA-associated PSTPIP1 A230T** were not born at expected Mendelian ratios, and surviving mice showed **growth retardation and elevated circulating proinflammatory cytokines** ([PMC3576065](https://pmc.ncbi.nlm.nih.gov/articles/PMC3576065/)).
- Critically, despite elevated circulating cytokines "implicated in active pyoderma gangrenosum," these mice **failed to develop the specific skin inflammation and arthritis phenotype** seen in human PAPA syndrome ([PMC3576065](https://pmc.ncbi.nlm.nih.gov/articles/PMC3576065/)) — this is a **HUMAN_MODEL_MISMATCH**-type finding per this repository's convention: systemic cytokine dysregulation is recapitulated, but organ-specific lesion formation (joint/skin) is not, suggesting the mouse model captures the inflammasome/cytokine arm of pathogenesis but misses species-specific or context-dependent factors required for the human tissue phenotype (see mechanism §6, step 7-8 caveat).
- In vitro cellular studies (non-animal) additionally show that PAPA-mutant A230T **increases IL-1β secretion** relative to wild-type PSTPIP1 in cell-based assays, consistent with — but independently supporting — the mouse cytokine findings ([WebSearch synthesis of PMC3576065 discussion]).

**Related model systems (mechanistic, not disease-specific):**
- *PSTPIP2* (a paralog) knockout/mutant mice (e.g., the classic "cmo" chronic multifocal osteomyelitis mouse) are widely used to study PSTPIP-family adaptor biology in neutrophil-mediated autoinflammation, though PSTPIP2 is genetically and phenotypically distinct from PSTPIP1/PAPA and should not be conflated with a PAPA model per se ([PMC9807597](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9807597/)).
- A separate murine model of pyoderma gangrenosum (not PSTPIP1-based) implicating IL-1β-primed neutrophils and skin-gut crosstalk exists in the literature and may be useful as a mechanistic (not genetic) comparator for the PG component of the PAPA phenotype ([Frontiers Immunology 2023](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1148893/full)).

**Model limitations:** the existing A230T mouse model recapitulates the biochemical/cytokine axis of disease but not the defining clinical lesions (arthritis, PG), representing a significant translational gap between the demonstrated pyrin-inflammasome/IL-1β mechanism and the tissue-specific human phenotype — an important caveat for any mechanistic module curation that cites this model as supporting evidence for the joint/skin nodes specifically (as opposed to the cytokine-production node).

---

## Summary of Key Ontology Term Candidates for Curation

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0011462; OMIM:604416; ORPHA:69126 |
| Gene | hgnc:9581 (PSTPIP1) |
| Modifier gene/pathway partner | MEFV (pyrin) |
| Sterile pyogenic arthritis | HP term for arthritis (verify exact HP CURIE at curation — general HP:0001369 Arthritis, or more specific sterile/pyogenic arthritis term if one exists) |
| Pyoderma gangrenosum | HP:0031928 (verify exact match) |
| Cystic acne | HP-subtree acne term (verify exact match) |
| Pathergy | verify HP term availability |
| Inflammasome activation | GO:0061702 (inflammasome complex) or more specific pyrin-inflammasome GO term (verify) |
| Actin cytoskeleton regulation | GO:0030041 (actin filament polymerization) |
| Neutrophil | CL:0000775 |
| Synovial joint | UBERON:0000982 |
| Skin | UBERON:0002097 |
| Anakinra/Canakinumab (treatment) | NCIT — verify exact CURIEs via OAK |

**Note on evidence gaps to flag during curation:** (1) no RCT-level treatment data exist — all treatment evidence is case-report/series level; (2) the mouse model shows a human-model mismatch for the tissue-specific (joint/skin) phenotype despite recapitulating the cytokine phenotype; (3) QoL-instrument data (EQ-5D/SF-36) specific to PAPA syndrome were not located in this search pass and may not exist in the primary literature; (4) exact PMIDs for several foundational papers (Wise 2002, Shoham/PNAS pyrin-PSTPIP1 paper, Lindor 1997) should be independently verified and fetched via `just fetch-reference` before use as KB evidence, since this report's citations came from web search summaries rather than direct PMID lookup for every source.

---

**Sources:**
- [PSTPIP1-Associated Myeloid-Related Proteinemia Inflammatory (PAMI) Syndrome: A Systematic Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10454568/)
- [A de novo heterozygous PSTPIP1 variant associated with PAPA syndrome: Chinese case report and review - Frontiers Genetics](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2026.1825761/full)
- [PAPA Syndrome - ScienceDirect Topics overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/papa-syndrome)
- [A novel pathogenic variant in PSTPIP1 highlights the diversity of PSTPIP1-associated disorders - Rheumatology/Oxford Academic](https://academic.oup.com/rheumatology/article/65/1/keaf466/8246822)
- [Phenotypic Associations of PSTPIP1 Sequence Variants - PubMed 33218716](https://pubmed.ncbi.nlm.nih.gov/33218716/)
- [PAPA syndrome - Wikidata (OMIM/Orphanet/MONDO IDs)](https://www.wikidata.org/wiki/Q7118181)
- [Orphanet: PAPA syndrome (ORPHA:69126)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=69126&lng=EN)
- [Pyrin Modulates the Intracellular Distribution of PSTPIP1 - PMC2702820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702820/)
- [Inflammation in Mice Ectopically Expressing PSTPIP1 A230T - PMC3576065](https://pmc.ncbi.nlm.nih.gov/articles/PMC3576065/)
- [Pyrin binds the PSTPIP1/CD2BP1 protein - PNAS](https://www.pnas.org/doi/10.1073/pnas.2135380100)
- [The role of anti-IL-1 drugs in the treatment of PAPA syndrome: a systematic review - Arch Dermatol Res 2025](https://link.springer.com/article/10.1007/s00403-025-04324-6)
- [Anakinra in PAPASH Spectrum Disorder: Case Report - PMC11244945](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11244945/)
- [OMIM 604416 - PYOGENIC STERILE ARTHRITIS, PYODERMA GANGRENOSUM, AND ACNE](https://omim.org/entry/604416)
- [Genotype, Phenotype, and Clinical Course in Five Patients With PAPA Syndrome - PMC3737487](https://ncbi.nlm.nih.gov/pmc/articles/PMC3737487)
- [Pyogenic arthritis, pyoderma gangrenosum, and acne syndrome in a Chinese family - PMC8362586](https://pmc.ncbi.nlm.nih.gov/articles/PMC8362586/)
- [Imaging findings of PAPA syndrome: differential diagnosis - Pediatric Radiology 2018](https://link.springer.com/article/10.1007/s00247-018-4246-1)
- [PAPA syndrome: differential diagnosis by synovial cell counts - PubMed 28251506](https://pubmed.ncbi.nlm.nih.gov/28251506/)
- [Pyoderma gangrenosum, acne, and suppurative hidradenitis (PASH) - PubMed 21745697](https://pubmed.ncbi.nlm.nih.gov/21745697/)
- [PAPA syndrome - DermNet NZ](https://dermnetnz.org/topics/papa-syndrome)
- [Mutations in CD2BP1 disrupt binding to PTP PEST and are responsible for PAPA syndrome - Human Molecular Genetics (Wise et al. 2002)](https://academic.oup.com/hmg/article-abstract/11/8/961/638530)
- [Clinical, Molecular, and Genetic Characteristics of PAPA Syndrome: A Review - PMC3048314](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3048314/)
- [Abnormal TNF-α production and etanercept efficacy in PAPA syndrome - PubMed 15580218](https://pubmed.ncbi.nlm.nih.gov/15580218/)
- [Use of TNF inhibitors in the treatment of PAPA syndrome - PMC4599379](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4599379/)
- [Combination TNF and IL-1 blockade in PAPA syndrome - PMC3952270](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3952270/)
- [WASp acts downstream of CD2 and CD2AP/PSTPIP1 adaptors - PubMed 12530983](https://pubmed.ncbi.nlm.nih.gov/12530983/)
- [The F-BAR protein PSTPIP1 controls ECM degradation and filopodia formation in macrophages - Blood/ASH](https://ashpublications.org/blood/article/123/17/2703/32540/The-F-BAR-protein-PSTPIP1-controls-extracellular)
- [Molecular interactions of adaptor protein PSTPIP2 in neutrophil-mediated autoinflammation - PMC9807597](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9807597/)
- [A novel murine model of pyoderma gangrenosum - Frontiers Immunology 2023](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1148893/full)