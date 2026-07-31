---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:45:17.034998'
end_time: '2026-07-30T23:52:30.415745'
duration_seconds: 433.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 49
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 33
  total_cost_usd: 2.4517006000000006
  session_id: a577b410-8b4f-5493-a841-f05a87c54b50
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 49
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 49** covering all of the
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

# Immunodeficiency 49 (IMD49) — Comprehensive Disease Research Report

## 1. Disease Information

**Overview:** Immunodeficiency 49 (IMD49), also known as "Severe Combined Immunodeficiency with Multisystem Anomalies" or "SCID, T Cell-Negative, B Cell-Positive, NK Cell-Positive, with Intellectual Disability, Spasticity, and Craniofacial Abnormalities," is a rare, autosomal dominant (de novo) primary immunodeficiency caused by heterozygous mutation in **BCL11B** (BCL11 Transcription Factor B), a C2H2 zinc-finger transcription factor essential for T-lymphocyte, neuronal, dental, and craniofacial development. It was first described by Punwani et al. in 2016 (PMID:27959755) in an infant identified by newborn TREC (T-cell receptor excision circle) screening who presented with "leaky" T⁻B⁺NK⁺ SCID plus corpus callosum agenesis and craniofacial/dermal anomalies.

**Key identifiers:**
- **OMIM:** #617237 (IMD49, Severe Combined)
- **Gene OMIM:** *606558 (BCL11B, BAF chromatin remodeling complex subunit BCL11B)
- **MONDO:** MONDO:0014981
- **MedGen:** C4310656 (UID 934623)
- **HGNC:** 13222 (BCL11B); gene location 14q32.2
- **Related OMIM phenotype:** #618092 — Intellectual Developmental Disorder with Speech Delay, Dysmorphic Facies, and T-Cell Abnormalities (IDDSFTA), an overlapping/allelic phenotype from the same gene
- **ClinVar:** the founding variant NM_138576.4(BCL11B):c.1323T>G (p.Asn441Lys) is recorded as RCV000412543
- No dedicated Orphanet or ICD-10/11 code was identified as a distinct entity; the condition is typically catalogued under "primary immunodeficiency" / "combined immunodeficiency" headings.

**Synonyms:** IMD49; SCID T⁻B⁺NK⁺ with intellectual disability, spasticity, and craniofacial abnormalities; BCL11B-related disease (BRD); BCL11B-related "BAFopathy."

**Evidence provenance:** Nearly all available information derives from aggregated individual case reports/case series (not large disease-level registries) — a 2025 systematic review (PMID:40033098) identified only **51 total individuals** reported in the literature across ~20 publications plus 3 novel cases, underscoring that this is an ultra-rare, recently delineated condition still being phenotypically characterized case-by-case.

**Important nosological note (recent, 2025):** A systematic literature review (Vedovato-dos-Santos et al., 2025, PMID:40033098) argues that IMD49 (SCID phenotype), IDDSFTA (neurodevelopmental phenotype), and the atopic/immune-dysregulation phenotype (Lu et al. 2021) are **not distinguishable as separate diseases** and should be regarded as **one BCL11B-related disease spectrum**: *"There is no meaningful way to distinguish between the two OMIM phenotypes associated with BCL11B."* This is directly relevant to dismech curation — IMD49 may be best modeled either as a `Disease` entry with explicit cross-reference/grouping to IDDSFTA and the atopic phenotype, or the reverse, with a `Grouping` capturing the unified spectrum (`CLINICAL_CONVENTION`/`SHARED_GENE_FAMILY` basis) per this project's `kb/groupings/` conventions.

Sources:
- [Entry - #617237 - IMMUNODEFICIENCY 49 - OMIM](https://omim.org/entry/617237)
- [Multisystem Anomalies in Severe Combined Immunodeficiency with Mutant BCL11B — NEJM (PMID:27959755)](https://www.nejm.org/doi/full/10.1056/NEJMoa1509164)
- [BCL11B-related disease: a single phenotypic entity? — PMC (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)
- [Immunodeficiency 49 — MedGen (NCBI)](https://www.ncbi.nlm.nih.gov/medgen/C4310656)
- [Entry - #618092 - IDDSFTA - OMIM](https://www.omim.org/entry/618092)

---

## 2. Etiology

**Disease causal factors (genetic, monogenic):** IMD49 is caused by **heterozygous, typically de novo, dominant-negative or loss-of-function/haploinsufficient missense, frameshift, nonsense, or translocation-disrupting variants in BCL11B** (14q32.2). Unlike most SCID genes (which act recessively or X-linked and cause a null immunologic phenotype), BCL11B mutations act **dominantly** — even a single heterozygous mutant allele arrests T-cell development because BCL11B functions as a homodimer/multimer and mutant protein can "poison" wild-type complexes (dominant-negative interference), or by simple haploinsufficiency for frameshift/nonsense alleles that escape nonsense-mediated decay.

**Genetic risk factors:**
- All reported causal variants are in **BCL11B** itself; no distinct modifier/susceptibility loci have been established.
- Variant classes reported: missense (clustering in the C2H2 zinc-finger DNA-binding domains, e.g., p.Asn441Lys/ZnF2, p.Asn807Lys/ZnF4, p.Cys826Tyr/ZnF5), frameshift and nonsense variants (mostly in exon 4, predicted to escape NMD and truncate the C-terminal zinc fingers), and two reported balanced translocations disrupting regulatory elements ~538–877 kb 3′ of BCL11B (a topologically-associating-domain/enhancer-disruption mechanism).
- **Inheritance:** predominantly **autosomal dominant, de novo** (10 of 13 patients de novo in one cohort; PMID:29985992). At least one case of vertical transmission from an affected mother to daughter has been reported, confirming true autosomal dominant transmission is possible, not obligate de novo.
- No described risk haplotypes, GWAS hits, or population susceptibility alleles — this is a rare monogenic disorder, not a complex/polygenic trait.

**Environmental risk factors:** None established; this is a purely monogenic (Mendelian) disorder, not modified by known environmental exposures, toxins, or lifestyle factors.

**Protective factors:** None reported (genetic or environmental). No protective variant, modifier allele, or environmental exposure reducing penetrance has been described in the literature located.

**Gene-environment interactions:** Not applicable/not described — no evidence of environmental triggers modulating expressivity. The atopic/allergic sub-phenotype (below) could theoretically interact with allergen exposure, but this has not been formally studied as a gene-environment interaction.

Sources:
- [Multisystem Anomalies in Severe Combined Immunodeficiency with Mutant BCL11B — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)
- [BCL11B mutations in patients affected by a neurodevelopmental disorder with reduced type 2 innate lymphoid cells — Brain, 2018 (PMID:29985992)](https://academic.oup.com/brain/article/141/8/2299/5049404)
- [BCL11B-related disease: a single phenotypic entity? (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)

---

## 3. Phenotypes

Phenotypes span **immunologic, neurodevelopmental, craniofacial, dermatologic, dental, and skeletal** domains. Based on the pooled cohort of 51 individuals (PMID:40033098), the cardinal, near-universal features are:

| Category | Feature | Frequency (pooled cohort) | Suggested HP term |
|---|---|---|---|
| Neurodevelopmental | Global developmental delay / intellectual disability | 98% | HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) |
| Craniofacial | Facial dysmorphism (myopathic facies, bitemporal narrowing, thin/short philtrum, small upslanted palpebral fissures, prominent nose, small mouth with downturned corners, micrognathia, posteriorly rotated ears) | 98% | HP:0000271 (Abnormality of the face); HP:0000280 (Coarse facial features) as needed; HP:0000347 (Micrognathia); HP:0000508 (Ptosis)/HP:0012811 (Narrow palpebral fissure) |
| Immune | Immune dysregulation (SCID, T-cell lymphopenia, hypogammaglobulinemia, or severe atopy/allergy) | 93% | HP:0002721 (Immunodeficiency); HP:0002846 (Abnormal T cell physiology); HP:0002850 (Decreased circulating total IgG) |
| Behavioral | Behavioral anomalies (autistic features in ~4/13 in one cohort) | 59% | HP:0000708 (Behavioral abnormality); HP:0000717 (Autism) |
| Dental | Dental anomalies (neonatal teeth, abnormal dentition) | 41% | HP:0000164 (Abnormality of the dentition); HP:0000695 (Natal tooth) |
| Neuroimaging | Brain MRI abnormality (agenesis of corpus callosum most severe case; usually normal) | 32% | HP:0001260 (Dysgenesis of the corpus callosum) |
| Skeletal | Craniosynostosis (coronal suture most common, 67% of CRS cases) | 24.5% (12/49) | HP:0001363 (Craniosynostosis); HP:0004440 (Coronal craniosynostosis) |
| Sleep | Sleep problems | 23% | HP:0002360 (Sleep disturbance) |
| Neurologic | Hypotonia | 23% | HP:0001252 (Hypotonia) |
| GI | Constipation/reflux | 21% | HP:0002019 (Constipation); HP:0002020 (Gastroesophageal reflux) |
| Dermatologic | Dermatitis/eczema (erosive dermatitis in severe cases) | 15% | HP:0000964 (Eczema); HP:0011342 (Erosive dermatitis) |

**Additional, disease-defining features from the index/severe (IMD49-classic) case** (PMID:27959755, PMC5215776):
- Severe T-cell lymphopenia at birth with **TREC 0/68,900** (normal >25), essentially absent naive CD4+ T cells, impaired PHA proliferation (18% vs. normal >50%)
- Corpus callosum agenesis, gyri radiating from the third ventricle, parallel lateral ventricles, prominent occipital horns, malrotated hippocampi, white-matter/lentiform-nucleus volume loss
- Increased intraorbital distance, short palpebral fissures, abnormal nasal creases, micrognathia, ear tag, loose skin folds, hirsutism, neonatal teeth, umbilical hernia, erythematous psoriasiform dermatitis
- Long-term neurologic morbidity **despite** successful immune reconstitution by HSCT: intellectual impairment, spastic quadriplegia, seizures, absent receptive/expressive language

**Atopic/immune-dysregulation sub-phenotype** (Lu et al. 2021, PMID:34887873): ~50% of BCL11B patients present with severe allergic disease — food allergy (multiple categories), atopic dermatitis, asthma, alopecia totalis, prurigo nodularis, markedly elevated IgE, persistent eosinophilia — **with relatively preserved/normal T-cell numbers and thymic output**, i.e., immune dysregulation without overt SCID. Suggested HP terms: HP:0012735 (Eczema), HP:0003212 (Increased IgE level), HP:0001880 (Eosinophilia), HP:0100804 (Sepsis-prone) not applicable — better: HP:0002205 (Recurrent respiratory infections) as needed per case.

**Onset/severity/progression:** Onset is congenital/neonatal for the immunologic phenotype (detected by newborn TREC screening in the index case) and evident from infancy for the neurodevelopmental/craniofacial features. Severity is markedly variable across the spectrum — from classic leaky SCID requiring emergency HSCT, through moderate neurodevelopmental delay with normal immune function, to isolated severe atopic disease. The neurodevelopmental phenotype is generally **stable/non-progressive** (a static encephalopathy-like course), while the immunologic phenotype, if untreated, is **life-threatening in infancy** due to opportunistic infection risk.

**Quality of life impact:** Not formally studied with EQ-5D/SF-36 instruments; qualitatively, the combination of severe intellectual disability, spastic quadriplegia, absent language, and (pre-HSCT) infection susceptibility represents very high disease burden; HSCT can correct the immune component but does **not** reverse the neurodevelopmental trajectory.

Sources:
- [Multisystem Anomalies in Severe Combined Immunodeficiency with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)
- [BCL11B mutations ... reduced type 2 innate lymphoid cells — Brain (PMID:29985992)](https://academic.oup.com/brain/article/141/8/2299/5049404)
- [A Novel Germline Heterozygous BCL11B Variant Causing Severe Atopic Disease — PMC (PMID:34887873)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8650153/)
- [BCL11B-related disease: a single phenotypic entity? (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)

---

## 4. Genetic/Molecular Information

**Causal gene:** BCL11B (HGNC:13222; NCBI Gene; OMIM *606558), chromosome 14q32.2. Encodes a Krüppel-like C2H2 zinc-finger transcription factor with **six C2H2-type zinc-finger domains (ZnF1–ZnF6)**, essential for hematopoietic (T-lineage), neuronal, dental, and skin/craniofacial development.

**Pathogenic variants reported (representative, all germline heterozygous):**

| Variant | Domain | Mechanism | Phenotype | Source |
|---|---|---|---|---|
| c.1323T>G, p.Asn441Lys (N441K) | ZnF2 (DNA-binding) | Dominant-negative — heterodimerizes with WT, blocks DNA binding at canonical sites, gains aberrant binding (e.g., novel TACC1 site) | Classic IMD49 (leaky SCID + CNS/craniofacial) | PMID:27959755 |
| p.Asn807Lys (N807K; murine model Asn797Lys) | ZnF4 (C2H2) | Dominant-negative; impairs Cd4 E4p/E4m enhancer chromatin accessibility; blocks DN2→DN3 and DN→DP thymocyte transitions; impairs iNKT development | Immunodeficiency with low TRECs | PMID:38495886 (mouse model) |
| p.Cys826Tyr (C826Y) | ZnF5 | Predicted to disrupt zinc-ion coordination / protein-protein interaction; CADD 23, pathogenic by 21/23 in silico tools | Severe atopic disease, near-normal T-cell numbers | PMID:34887873 |
| p.Asn440Lys (N440K, distinct residue from N441K) | ZnF domain | Dominant-negative — interferes with paralog **BCL11A** function via heterodimerization/TCF1 interaction; dampens BCL11B-TCF1 antagonism | T-cell deficiency + neurological disorder | PMID:39487351 |
| Frameshift/nonsense variants, mostly exon 4 | C-terminal (predicted to escape NMD) | Truncates protein, loses ≥2 C-terminal DNA-binding zinc fingers | IDDSFTA-type neurodevelopmental phenotype, craniosynostosis | PMID:29985992; various case reports |
| Balanced translocations, ~538–877 kb 3′ of BCL11B | Regulatory/enhancer region | Disrupts long-range cis-regulatory elements | Neurodevelopmental phenotype | PMID:29985992 |

**Variant classification (ACMG/AMP):** Reported pathogenic/likely pathogenic per case reports; the founding N441K variant is registered in ClinVar (RCV000412543) linked to Immunodeficiency 49.

**Population allele frequency:** All reported pathogenic variants are absent from gnomAD/population databases (consistent with de novo, embryonic-lethal-in-homozygosity, severe dominant disease) — no carrier frequency or founder variant has been described.

**Somatic vs. germline:** All disease-causing variants reported are **germline** (constitutional), arising de novo in the great majority of cases, with rare vertical (parent-to-child) transmission documented.

**Functional consequence:** Predominantly **dominant-negative** for missense zinc-finger variants (heterodimerization with wild-type BCL11B — and, per the 2024 Nat Immunol study, with paralog BCL11A — poisoning normal transcriptional complexes), with **haploinsufficiency/loss-of-function** contributing for truncating (frameshift/nonsense) and regulatory-disruption (translocation) alleles. The distinction between dominant-negative and pure loss-of-function is not fully resolved even in mouse models (PMID:38495886 notes both mechanisms may operate).

**Modifier genes:** None established; BCL11B's paralog **BCL11A** is mechanistically implicated as an interaction partner whose function is interfered with by at least one dominant-negative BCL11B variant (N440K; PMID:39487351), making BCL11A a candidate "interacting partner" rather than a classical modifier locus.

**Epigenetic information:** BCL11B itself functions partly through chromatin regulation — it is a subunit of the **BAF (SWI/SNF) chromatin remodeling complex** (per OMIM *606558 title: "BAF chromatin remodeling complex subunit BCL11B"), and the N797K mouse model shows the mutation **reduces chromatin accessibility at the Cd4 E4m/E4p enhancer**, directly linking a BCL11B mutation to altered local chromatin state at a key T-lineage gene.

**Chromosomal abnormalities:** Two reported de novo balanced translocations disrupting BCL11B's 3′ regulatory landscape (not classic aneuploidy) have been associated with the neurodevelopmental phenotype (PMID:29985992).

Suggested gene/ontology annotations: **hgnc:13222** (BCL11B); GO:0003700 (DNA-binding transcription factor activity); GO:0008270 (zinc ion binding); GO:0016514 (SWI/SNF complex — for the BAF-complex subunit role).

Sources:
- [Entry - *606558 - BCL11B - OMIM](https://omim.org/entry/606558)
- [Multisystem Anomalies... PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)
- [A Bcl11bN797K variant... (PMID:38495886)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940544/)
- [A mutant BCL11B-N440K protein interferes with BCL11A function (PMID:39487351)](https://www.nature.com/articles/s41590-024-01997-5)
- [A Novel Germline Heterozygous BCL11B Variant... (PMID:34887873)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8650153/)
- [BCL11B mutations...Brain (PMID:29985992)](https://academic.oup.com/brain/article/141/8/2299/5049404)

---

## 5. Environmental Information

Not applicable in any substantial way — IMD49 is a monogenic disorder with no established environmental, occupational, toxin, dietary, or infectious *causal* factor. The only environmental interaction of note is **secondary infectious risk conferred by the immunodeficiency** (i.e., the disease creates vulnerability to environmental pathogens, rather than an environmental factor causing the disease), and possible allergen-driven exacerbation of the atopic sub-phenotype (not formally studied). No lifestyle factors (smoking, diet, exercise, alcohol) have been implicated. No infectious agent triggers the underlying genetic lesion, although opportunistic/common pathogens (bacterial, viral, fungal — e.g., CMV, PCP, mucocutaneous candidiasis) are the clinically relevant threat in the untreated SCID phenotype, consistent with T-cell immunodeficiency generally.

---

## 6. Mechanism / Pathophysiology

**Causal chain (classic IMD49/SCID phenotype):**

1. **Molecular trigger:** De novo heterozygous BCL11B variant (missense in a C2H2 zinc finger, or truncating) → altered/dominant-negative BCL11B protein.
2. **Molecular consequence:** Mutant BCL11B heterodimerizes with wild-type BCL11B (and possibly BCL11A), forming complexes with impaired canonical DNA binding at T-lineage target genes (e.g., reduced binding at BCL11B's own locus, gain of aberrant binding at off-target sites such as TACC1) and reduced chromatin accessibility at key enhancers (e.g., the Cd4 E4m/E4p enhancer).
3. **Cellular consequence:** Arrest of thymocyte development — impaired **DN2→DN3** and **DN→DP** transitions, accumulation of aberrant immature CD8 single-positive (ISP8) thymocytes, severely reduced invariant NKT (iNKT) cell development, and (in the N440K dominant-negative mechanism) emergence of aberrant **NK/ILC1-like NKp46+ cells** in the thymus due to failure of BCL11B (via BCL11A) to antagonize TCF1-driven innate-lymphoid differentiation.
4. **Tissue/organismal consequence:** Profound T-cell lymphopenia (T⁻B⁺NK⁺ "leaky SCID" pattern), absent TRECs, no naive CD4+ T cells, impaired mitogen-driven T-cell proliferation → susceptibility to opportunistic infection in infancy.
5. **Parallel non-immune consequence (same transcription factor, different tissues):** BCL11B is independently essential for **neuronal differentiation** (cortical projection neurons — reduced TBR1+ neocortical neurons in the N440K mouse model), **craniofacial/skeletal patterning** (craniosynostosis), **dental development** (neonatal/abnormal dentition), and **epidermal homeostasis** (dermatitis/eczema) — explaining the pleiotropic multisystem phenotype from a single transcription factor lesion, analogous to other "BAFopathies."

**Key molecular pathways/processes:** T-cell receptor (TCR) locus recombination and Cd4 gene regulation (via BCL11B-dependent enhancer activation), TCF1-dependent innate lymphoid vs. T-lineage fate decisions, BAF/SWI-SNF chromatin remodeling.

**Cell types involved:** Double-negative (DN) and double-positive (DP) thymocytes, CD4+/CD8+ T cells, invariant NKT cells, type 2 innate lymphoid cells (ILC2s, markedly reduced in the neurodevelopmental cohort), aberrant NK/ILC1-like cells (in the N440K dominant-negative model), cortical projection neurons, keratinocytes/epidermal cells, cranial suture osteoblasts (craniosynostosis).

**Protein dysfunction:** Dominant-negative interference via heterodimerization (loss of normal DNA-binding specificity plus gain of aberrant binding) for missense zinc-finger variants; simple haploinsufficiency for truncating/regulatory-disrupting variants.

**Suggested GO terms:** GO:0030217 (T cell differentiation), GO:0033077 (T cell differentiation in thymus), GO:0030098 (lymphocyte differentiation), GO:0045619 (regulation of lymphocyte differentiation), GO:0000122 (negative regulation of transcription by RNA polymerase II), GO:0006357 (regulation of transcription by RNA polymerase II).

**Suggested CL terms:** CL:0000827 (pro-T cell) / CL:0002489 (double-negative thymocyte), CL:0000809 (double-positive thymocyte), CL:0000895 (naive thymus-derived CD4-positive, alpha-beta T cell), CL:0000939 (CD16-negative, CD56-bright natural killer cell) as approximate NK reference, CL:0001069 (group 2 innate lymphoid cell, human), CL:0000540 (neuron)/CL:0000679 (glutamatergic neuron) for cortical projection neurons, CL:0000312 (keratinocyte).

**Model-system caveats:** The dominant-negative vs. pure loss-of-function distinction remains genuinely unresolved even in the mouse literature (PMID:38495886 authors explicitly note this ambiguity) — a good candidate for a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` discussion node if curated in dismech.

Sources:
- [Multisystem Anomalies in SCID with Mutant BCL11B — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)
- [A Bcl11bN797K variant isolated from an immunodeficient patient inhibits early thymocyte development in mice (PMID:38495886)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940544/)
- [A mutant BCL11B-N440K protein interferes with BCL11A function during T lymphocyte and neuronal development (PMID:39487351)](https://www.nature.com/articles/s41590-024-01997-5)
- [Bcl11b is required for differentiation and survival of αβ T lymphocytes — Nature Immunology, 2003 (PMID:12717433)](https://www.nature.com/articles/ni927)
- [BCL11B mutations...reduced ILC2 — Brain (PMID:29985992)](https://academic.oup.com/brain/article/141/8/2299/5049404)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Thymus (site of T-cell developmental arrest), immune system broadly (lymph nodes, peripheral blood lymphocyte compartments), central nervous system (corpus callosum, cerebral cortex/white matter, hippocampus), craniofacial skeleton (cranial sutures, mandible, maxilla), skin, teeth.
- **Secondary/complications:** Respiratory system (recurrent infections/opportunistic pneumonia pre-HSCT), gastrointestinal system (constipation/reflux, reported in ~21%), musculoskeletal system (spastic quadriplegia as a CNS-secondary complication).
- **Body systems:** Immune system, nervous system (central), integumentary system, skeletal system (craniofacial), dental/orodental system.

**Tissue and cell level:** Thymic epithelium/thymocyte niche; T-lymphocyte lineage (DN, DP, SP thymocytes; naive/memory peripheral T cells); innate lymphoid cell compartment (ILC2s, and aberrant NK/ILC1-like cells in mouse models); cortical/cerebral neurons (particularly TBR1+ deep-layer projection neurons); epidermal keratinocytes; cranial suture mesenchyme/osteogenic cells.

**Subcellular level:** Nucleus (BCL11B is a nuclear DNA-binding transcription factor and BAF/SWI-SNF chromatin-remodeling complex subunit); chromatin/enhancer elements (e.g., the Cd4 E4m/E4p enhancer). Suggested GO Cellular Component: GO:0005634 (nucleus), GO:0016514 (SWI/SNF complex), GO:0000785 (chromatin).

**Localization (UBERON):** UBERON:0002370 (thymus), UBERON:0002316 (corpus callosum), UBERON:0000955 (brain), UBERON:0002383 (skin of body)/UBERON:0002097 (skin), UBERON:0003133 (cranial suture) or UBERON:0002516 (coronal suture) if more specific term needed, UBERON:0001091 (tooth).

**Lateralization:** No consistent lateralization pattern reported; craniofacial and craniosynostotic features are generally symmetric/midline (e.g., coronal suture involvement), consistent with a developmental patterning defect rather than an asymmetric process.

Sources: as above (PMID:27959755, PMID:29985992, PMID:40033098).

---

## 8. Temporal Development

**Onset:** Congenital — the immunologic phenotype is detectable at birth via newborn screening (absent TRECs), and craniofacial/dermal/neurodevelopmental features are apparent from infancy. Onset pattern is **insidious/present-from-birth** rather than acute, though the untreated SCID component can progress to acute, life-threatening infection in the first months of life.

**Progression:**
- The **immunologic** component, if untreated, is progressive toward severe/fatal infectious complications in infancy; once treated with HSCT, immune function stabilizes and normalizes (full T-cell reconstitution, normal TCR repertoire, protective vaccine responses reported at 2-year follow-up in the index case).
- The **neurodevelopmental** component follows a relatively **stable, non-progressive (static encephalopathy-like)** course — intellectual disability, spasticity, and seizures persisted post-HSCT in the index case despite complete immune correction, indicating the CNS phenotype is not rescued by treating the immune defect.
- **Disease course pattern:** chronic and lifelong for the neurodevelopmental/craniofacial features; the immunodeficiency component is potentially curable with early HSCT.
- No formal staging system exists (this is not a malignancy or classically staged disorder).

**Patterns:**
- **Remission:** The SCID component can achieve durable immunologic "remission"/cure via HSCT (treatment-induced); no spontaneous remission is described. The atopic sub-phenotype's natural history (whether it attenuates with age) is not well characterized in the literature reviewed.
- **Critical periods:** The neonatal/early-infancy period is critical for **immunologic** intervention (newborn screening → early HSCT before infection onset dramatically improves outcome, as in the index case, which required a second HSCT after initial graft failure but ultimately succeeded). No specific critical window has been defined for preventing the neurodevelopmental phenotype, which appears to be fixed by the underlying developmental (prenatal/perinatal) transcriptional defect.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)

---

## 9. Inheritance and Population

**Epidemiology:** IMD49/BCL11B-related disease is **ultra-rare** — a 2025 systematic review identified only **51 total reported individuals** in the literature to date (PMID:40033098). No formal prevalence or incidence rate (cases per 100,000) has been calculated or published; it is not covered by large-scale newborn-screening prevalence statistics distinct from general SCID (SCID overall occurs at roughly 1 in 58,000 births per U.S. newborn screening data, but BCL11B-specific SCID is a small subset of that).

**Inheritance pattern:** Autosomal dominant. The great majority of cases (≥75-80%) arise **de novo**; rare vertical (parent-to-affected-child) transmission has been documented, confirming true dominant transmission is possible when a mutation carrier reproduces.

**Penetrance:** Appears to be high/complete for the core phenotype (facial dysmorphism, neurodevelopmental delay) based on the reported cohort, though ascertainment bias (only symptomatic individuals are sequenced/reported) likely inflates apparent penetrance.

**Expressivity:** Markedly **variable** — the same gene produces phenotypes ranging from classic severe SCID with CNS malformation, through isolated neurodevelopmental delay with normal immunity (IDDSFTA), to primarily atopic/allergic disease with preserved T-cell counts. This is the central rationale behind the 2025 proposal to unify these as one variably-expressive disease spectrum rather than discrete OMIM entries.

**Genetic anticipation:** Not described/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported in the literature reviewed, though theoretically possible given the de novo dominant inheritance pattern (relevant for recurrence-risk counseling).

**Founder effects / consanguinity:** None reported — consistent with an autosomal dominant, mostly de novo disorder (consanguinity is not a risk factor for dominant conditions).

**Carrier frequency:** Not applicable (dominant disorder; "carriers" are affected individuals, not asymptomatic heterozygotes).

**Population demographics:** No specific ethnic or geographic predilection has been reported; cases have been described in patients of varied backgrounds (e.g., a Chinese boy, a Japanese male patient, a Canadian cohort in the craniosynostosis literature, North American index cases). No sex ratio skew has been formally established, though case reports include both male and female probands (e.g., the index NEJM case was male; the severe atopic case, PMID:34887873, was a 14-year-old female). Age distribution spans neonatal diagnosis (via TREC screening) through adolescence at time of reporting.

Sources:
- [BCL11B-related disease: a single phenotypic entity? (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)
- [BCL11B mutations...Brain (PMID:29985992)](https://academic.oup.com/brain/article/141/8/2299/5049404)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Newborn screening:** TREC assay (the actual diagnostic entry point for the index case — TREC 0/68,900, dramatically abnormal).
- **Flow cytometry lymphocyte immunophenotyping:** absolute CD3+, CD4+, CD8+ T-cell counts (severely reduced in classic IMD49: CD3+ 182 cells/µL, CD4+ 130 cells/µL, CD8+ 26 cells/µL vs. age-matched normal ranges); CD19+ B cells and CD16+/CD56+ NK cells typically preserved/near-normal; naive CD45RA+ CD4+ T cells characteristically **absent**.
- **T-cell functional testing:** mitogen (PHA) proliferation assay — markedly reduced (18% vs. normal >50% in the index case).
- **Immunoglobulin levels** (IgG/IgA/IgM/IgE) — variable; IgE markedly elevated in the atopic sub-phenotype.
- **ILC subset flow cytometry:** reduced/absent peripheral ILC2s is a described hallmark of the neurodevelopmental-predominant sub-phenotype (PMID:29985992).
- **Imaging:** Brain MRI (corpus callosum agenesis/dysgenesis, white-matter volume loss in severe cases; often normal in milder neurodevelopmental cases); craniofacial CT with 3D reconstruction for suspected craniosynostosis.
- **Dental exam:** for neonatal teeth/dental anomalies.
- **Skin biopsy/dermatologic exam:** for erosive dermatitis/eczema when present.

**Genetic testing:**
- **Gold standard:** Whole exome sequencing (WES) with trio (parent-child) analysis to confirm de novo status — this is how essentially all reported cases have been identified.
- **Single-gene BCL11B sequencing** is reasonable when the SCID/neurodevelopmental/craniosynostosis phenotype triad is clinically recognized.
- **SCID gene panels** (which typically include BCL11B alongside RAG1/2, IL2RG, JAK3, ADA, DCLRE1C, etc.) are appropriate first-line when T⁻B⁺NK⁺ SCID is identified by TREC screening.
- **Chromosomal microarray/karyotype:** relevant for the rare translocation-mediated cases disrupting BCL11B's regulatory landscape.
- No dedicated NCT clinical-trial genetic-testing protocol identified; testing occurs through standard clinical WES/panel pathways (e.g., NIH GTR lists BCL11B testing under Immunodeficiency 49, concept C4310656).

**Clinical criteria:** No formal consensus diagnostic criteria/staging system exists (this is a recently delineated, ultra-rare gene-disease association); diagnosis rests on the combination of (a) molecularly confirmed heterozygous BCL11B variant, (b) compatible T-cell/immune phenotype, and (c) compatible neurodevelopmental/craniofacial features. The 2025 review (PMID:40033098) proposes craniosynostosis as "an important diagnostic clue" that should prompt BCL11B testing in undiagnosed neurodevelopmental-delay-plus-dysmorphism cases.

**Differential diagnosis:** Other T⁻B⁺NK⁺ SCID genes (IL7R, CD3 subunit deficiencies), other BAF-complex disorders ("BAFopathies," e.g., Coffin-Siris syndrome spectrum), other craniosynostosis syndromes (FGFR-related, TWIST1/TCF12-related), and other syndromic combined immunodeficiencies with CNS involvement (e.g., DOCK8 deficiency, though that has a distinct atopic/infectious pattern).

**Screening:** Newborn TREC-based SCID screening (universal in most U.S. states and many countries) is the practical population-level screening mechanism that would detect the classic IMD49 immunologic phenotype at birth, though it would **not** detect the milder, immunologically-normal neurodevelopmental or atopic-predominant ends of the spectrum.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776); [Immunodeficiency 49 — NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4310656/); [BCL11B-related disease (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** Untreated classic SCID from BCL11B mutation carries the same fundamentally fatal-in-infancy risk (from opportunistic infection) as other SCID genotypes if not corrected by HSCT — this is the rationale for its inclusion in newborn TREC screening panels. With successful HSCT, the immunologic component is correctable; the index case achieved stable engraftment, normal TCR repertoire diversity, and protective vaccine responses by two years post-transplant (after an initial failed first transplant and a successful second transplant using busulfan/fludarabine/rabbit ATG conditioning). No formal 5-year/10-year survival statistics exist given the extremely small reported cohort (51 individuals total).

**Morbidity/function:** Even with immunologic cure, **neurodevelopmental morbidity persists and is not reversed by HSCT** — the index case retained intellectual impairment, spastic quadriplegia, seizures, and absent expressive/receptive language at follow-up despite full immune reconstitution. This is a critical prognostic point: BCL11B's CNS/developmental role is cell-autonomous to neurons and craniofacial tissue and is not corrected by hematopoietic-lineage-restricted gene/cell therapy (HSCT).

**Disease course/complications:** Pre-transplant complications relate to infection susceptibility (from SCID); post-transplant complications relate to graft failure risk (as seen in the index case, requiring a second transplant) and standard HSCT-related morbidity (conditioning toxicity, GVHD risk, though not detailed as occurring in the reported case). Long-term complications also include the fixed neurodevelopmental/craniofacial burden (spasticity, seizures, intellectual disability, and for craniosynostosis cases, risk of raised intracranial pressure requiring surgical release).

**Prognostic factors:** Timing of immunologic diagnosis/HSCT (earlier before infectious complications generally favors immunologic outcome, as with SCID broadly); the severity/domain of the BCL11B variant's phenotype (SCID-dominant vs. neurodevelopmental-dominant vs. atopic-dominant) determines which organ system drives long-term prognosis. No molecular biomarker has been shown to predict severity across the spectrum; genotype-phenotype correlation has specifically been reported as **absent/unreliable** (PMID:40033098), meaning a given BCL11B variant does not reliably predict which sub-phenotype (SCID vs. neurodevelopmental vs. atopic) will predominate.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776); [BCL11B-related disease (PMID:40033098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985952/)

---

## 12. Treatment

**Definitive/curative therapy (immunologic component):**
- **Allogeneic hematopoietic stem-cell transplantation (HSCT)** is the definitive treatment for the SCID component of IMD49, as demonstrated in the index case (matched unrelated donor, second transplant successful using busulfan/fludarabine/rabbit antithymocyte globulin conditioning after initial graft failure) — full T-cell immune reconstitution, normal TCR repertoire diversity, and protective vaccine responses were achieved. Suggested MAXO term: MAXO:0000747 (hematopoietic stem cell transplantation) or MAXO:0010039 (organ transplantation); `therapeutic_modality: CELL_THERAPY`.

**Supportive/pharmacologic care (pre-HSCT and for milder phenotypes):**
- Standard SCID supportive management pending/alongside HSCT: infection prophylaxis (antimicrobial/antifungal/anti-Pneumocystis prophylaxis), **IVIG replacement therapy** for hypogammaglobulinemia, protective isolation, avoidance of live vaccines. Suggested MAXO term: MAXO:0000950 (supportive care); treatment_term NCIT:C15986 (Pharmacotherapy) with therapeutic_agent for IVIG (immunoglobulin replacement) as applicable.
- For the **atopic/immune-dysregulation** sub-phenotype: standard allergic-disease pharmacotherapy (topical corticosteroids/emollients for dermatitis, antihistamines, dietary allergen avoidance, asthma controller therapy) — not disease-specific, but standard-of-care symptomatic management as used in the reported severe atopic case (PMID:34887873). No BCL11B-targeted or precision immunomodulatory therapy has been reported for this arm.

**Surgical/interventional:**
- Craniosynostosis correction surgery for the subset (~24.5%) with craniosynostosis, per standard craniofacial surgical protocols (suggested MAXO:0000004 surgical procedure / NCIT:C16186 Orthopedic/Craniofacial Surgical Procedure as applicable).

**Rehabilitative/supportive (neurodevelopmental component):**
- Physical therapy, occupational therapy, and speech therapy for spasticity, motor impairment, and absent language — standard supportive neurodevelopmental management, not curative (MAXO:0000011 physical therapy).
- Anti-seizure medication for those with seizures (not specifically detailed in the literature reviewed beyond noting seizures as a feature).

**Advanced/experimental therapeutics:** No gene therapy, RNA-based therapy (ASO/siRNA), targeted small-molecule, or immunotherapy specific to BCL11B mutation correction has been reported or is in clinical trials, per the literature reviewed — this is consistent with the disease being too rare and too recently characterized (first description 2016) for a bespoke precision-therapeutic pipeline. HSCT remains the only "curative" modality, and only for the hematopoietic/immunologic manifestations.

**Treatment strategy/algorithm:** In practice, management is stratified by phenotype dominance — SCID-dominant presentations proceed via the standard SCID-HSCT pathway (early recognition via newborn screening → urgent HSCT), while neurodevelopmental-dominant and atopic-dominant presentations receive symptomatic, multidisciplinary supportive care (developmental therapies, allergy/dermatology management) without a disease-modifying intervention.

**Treatment outcomes:** HSCT for the immunologic component has an excellent reported outcome (full reconstitution in the index case, second-transplant success after first-transplant graft failure); however, HSCT does **not** alter the neurodevelopmental trajectory, an important outcome-expectation point for families/clinicians.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776); [A Novel Germline Heterozygous BCL11B Variant Causing Severe Atopic Disease (PMID:34887873)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8650153/)

---

## 13. Prevention

**Primary prevention:** Not applicable — this is a de novo/dominant monogenic disorder with no known modifiable environmental or lifestyle risk factor; there is no vaccination or exposure-avoidance strategy that prevents disease occurrence.

**Secondary prevention (early detection):** **Newborn TREC-based SCID screening** functions as an effective secondary-prevention/early-detection mechanism for the classic immunologic (IMD49) phenotype — as demonstrated by the index case being identified this way, enabling pre-symptomatic diagnosis and timely HSCT before life-threatening infection developed. This screening does not, however, detect the immunologically-normal ends of the phenotypic spectrum (isolated neurodevelopmental or atopic presentations).

**Genetic counseling/screening:** Given the predominantly de novo inheritance, recurrence risk for future pregnancies in unaffected parents is low but not zero (theoretical germline mosaicism); for the minority of cases with a known affected parent, standard autosomal-dominant 50% recurrence-risk counseling applies. Prenatal or preimplantation genetic testing could be offered in families with a confirmed causal variant, though this is not specifically documented as having been performed in the literature reviewed. Suggested MAXO term: MAXO:0000079 (genetic counseling).

**Tertiary prevention:** Infection prophylaxis (antimicrobial/antifungal, IVIG) pending HSCT reduces morbidity/mortality from the immunodeficiency; standard developmental-therapy and craniofacial surveillance (for craniosynostosis, which can require timely surgical intervention to prevent raised intracranial pressure) represent tertiary prevention of complications in those already affected.

**Public health/behavioral/environmental interventions:** Not applicable — no population-level public-health, environmental, or behavioral intervention modifies risk for this monogenic disorder.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring BCL11B-related disease has been reported in non-human species (companion animals, livestock, or wildlife) in the literature reviewed — this appears to be a human-specific clinical entity described only through de novo human mutation. NCBI Taxon: Homo sapiens (NCBITaxon:9606) is the only species with documented natural disease.

**Orthologous gene:** Bcl11b is highly conserved; mouse ortholog *Bcl11b* (MGI database) and zebrafish ortholog *bcl11ba* have both been used experimentally (see Model Organisms, below) but no spontaneous/natural disease-causing mutation has been reported in these species outside laboratory-engineered models.

**Comparative biology:** The T-cell developmental role of Bcl11b is deeply conserved from zebrafish through mouse to human (loss/knockdown blocks the same DN thymocyte developmental stage across species), supporting strong evolutionary conservation of this transcriptional program; similarly, the corpus callosum/craniofacial developmental role has been cross-validated (bcl11ba knockdown zebrafish reproduce the patient's increased interorbital distance).

**Zoonotic potential/transmission:** Not applicable — this is a non-infectious, non-transmissible monogenic disorder.

Sources: [Multisystem Anomalies in SCID with Mutant BCL11B — PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)

---

## 15. Model Organisms

**Mouse models:**
1. **Bcl11b constitutive knockout** (Wakabayashi et al., 2003, Nature Immunology, PMID:12717433) — the foundational mouse model. *Bcl11b⁻/⁻* mice show developmental arrest of thymocytes at the CD4⁻CD8⁻ double-negative stage, with unsuccessful Vβ-to-Dβ TCR recombination and absent pre-TCR surface expression (no Tcrb mRNA), while B- and γδ-T-lineage cells are unaffected. Homozygous null mice die within the first day of life (open eyes, failure to feed); heterozygotes are phenotypically normal/fertile — establishing that complete Bcl11b loss is neonatal-lethal and that this is a T-lineage-specific, cell-autonomous survival/differentiation factor, but that simple heterozygous loss alone (unlike the human dominant-negative missense alleles) does not reproduce human disease.
2. **Bcl11bN797K knock-in** (murine equivalent of human N807K; Matsumoto et al. 2024, Frontiers in Immunology, PMID:38495886) — heterozygous *Bcl11b+/N797K* mice recapitulate impaired early thymocyte development (DN2→DN3 and DN→DP block), accumulation of aberrant immature CD8 single-positive thymocytes, severely impaired invariant NKT cell development, growth retardation, and ~50% mortality by 6 weeks; homozygotes die within one day of birth nearly lacking double-positive thymocytes. Competitive bone-marrow chimera and mixed-chimera experiments confirm the defect is **T-cell-intrinsic**. This model directly recapitulates the human immunodeficient phenotype associated with the corresponding human variant and mechanistically implicates impaired Cd4 enhancer chromatin accessibility.
3. **Bcl11bN440K knock-in** (Nature Immunology 2024, PMID:39487351) — heterozygous mice show emergence of aberrant thymic NK/ILC1-like NKp46+ cells and reduced TBR1+ neocortical neurons, phenocopying loss of the paralog *Bcl11a* (not simple *Bcl11b* loss) — directly demonstrating the dominant-negative-via-heterodimerization-with-BCL11A mechanism, and linking a single mutant allele to both an immune (aberrant innate lymphoid emergence) and a neurodevelopmental (reduced cortical neuron number) phenotype in one model, mirroring the human multisystem presentation.

**Zebrafish model:** *bcl11ba* morpholino knockdown in *lck:GFP* transgenic zebrafish embryos (Punwani et al. 2016, PMID:27959755) blocks development of lck:GFP-marked T-cell progenitors and reproduces the patient's increased interorbital distance (craniofacial phenotype) and revealed a previously unrecognized function of BCL11B in **hematopoietic progenitor positioning/migration** (substantial lateral and dorsoventral progenitor displacement), mediated through modulation of the chemokine receptors **CCR7 and CCR9**. Critically, wild-type human BCL11B mRNA rescued both the T-cell developmental defect and craniofacial phenotype, whereas mutant (p.N441K) human BCL11B failed to rescue — direct functional confirmation of pathogenicity and dominant-negative behavior.

**Model characteristics — phenotype recapitulation and limitations:**
- The mouse knock-in models (N797K, N440K) recapitulate the **immunodeficiency and innate-lymphoid** aspects of human disease well, and the N440K model additionally recapitulates a **neurodevelopmental** correlate (reduced cortical neurons), making it a rare model bridging both organ systems.
- The zebrafish model is particularly valuable for **rapid, low-cost variant-pathogenicity testing** (rescue vs. non-rescue assays) and for uncovering the progenitor-migration function not evident in mammalian models.
- **Limitation:** No mouse or zebrafish model has yet reproduced the **craniosynostosis** or **severe atopic/allergic** ends of the human phenotypic spectrum, and the complete Bcl11b-null mouse (Wakabayashi 2003) — as opposed to the missense knock-in models — does not reproduce the dominant human disease mechanism, since human patients are heterozygous for gain-of-interference alleles rather than simple loss-of-function nulls. This gap (established mouse/zebrafish models for the SCID/neurodevelopmental core, but no natural or engineered model yet capturing the craniosynostosis or atopic sub-phenotypes) would be a reasonable `HUMAN_MODEL_MISMATCH` note in a dismech pathophysiology entry.

**Resources:** Mouse Genome Informatics (MGI) for *Bcl11b* alleles; ZFIN for *bcl11ba* zebrafish data.

Sources:
- [Bcl11b is required for differentiation and survival of αβ T lymphocytes — Nat Immunol 2003 (PMID:12717433)](https://www.nature.com/articles/ni927)
- [A Bcl11bN797K variant isolated from an immunodeficient patient inhibits early thymocyte development in mice — Front Immunol 2024 (PMID:38495886)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940544/)
- [A mutant BCL11B-N440K protein interferes with BCL11A function during T lymphocyte and neuronal development — Nat Immunol 2024 (PMID:39487351)](https://www.nature.com/articles/s41590-024-01997-5)
- [Multisystem Anomalies in Severe Combined Immunodeficiency with Mutant BCL11B — NEJM/PMC (PMID:27959755)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5215776)

---

## Summary of Curation-Relevant Notes for dismech

1. **Nosology decision needed:** The 2025 literature explicitly argues IMD49, IDDSFTA, and the BCL11B-atopic phenotype are one spectrum, not three diseases. Recommend checking `docs/explanation/design-decisions.md` for prior guidance on lump/split calls, and consider whether this is a single `Disease` entry with `has_subtypes` (SCID-dominant, neurodevelopmental-dominant, atopic-dominant) versus a `Grouping` over separate entries.
2. **Small evidence base:** Only 51 total reported patients (PMID:40033098) — every phenotype/frequency claim should cite this pooled review or the individual underlying case series, not be treated as large-cohort-validated epidemiology.
3. **Key primary papers to cite:** PMID:27959755 (index case + zebrafish), PMID:29985992 (ILC2/neurodevelopmental cohort), PMID:34887873 (atopic phenotype), PMID:38495886 and PMID:39487351 (mouse mechanistic models), PMID:12717433 (foundational Bcl11b knockout), PMID:40033098 (2025 unifying spectrum review with pooled frequencies).
4. **Mechanism module candidate:** The dominant-negative-via-heterodimerization pattern (mutant BCL11B poisoning wild-type BCL11B/BCL11A complexes) could be a useful `mechanistic_hypotheses`/pathophysiology node given its centrality across multiple papers, with `hypothesis_groups` distinguishing the "pure haploinsufficiency" (truncating variants) vs. "dominant-negative interference" (missense zinc-finger variants) causal routes.
5. **HSCT-does-not-rescue-CNS-phenotype** is a clinically important, well-evidenced causal-chain divergence point (single upstream gene, two independently-arising downstream tissue consequences, only one of which is treatable by HSCT) worth explicit modeling as two separate downstream branches from the shared BCL11B lesion node.