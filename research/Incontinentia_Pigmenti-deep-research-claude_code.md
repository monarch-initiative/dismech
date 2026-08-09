---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T03:58:51.770492'
end_time: '2026-07-30T04:04:17.338597'
duration_seconds: 325.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Incontinentia Pigmenti
  mondo_id: MONDO:0010631
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
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.7640704999999999
  session_id: 5dd887df-f66e-565b-8209-dadd5bf74d40
  stop_reason: end_turn
citation_count: 62
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Incontinentia Pigmenti
- **MONDO ID:** MONDO:0010631 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Incontinentia Pigmenti** covering all of the
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

# Incontinentia Pigmenti (IP) — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview:** Incontinentia pigmenti (IP; also called Bloch-Sulzberger syndrome) is a rare, multisystem, X-linked dominant genodermatosis caused by loss-of-function variants in *IKBKG* (formerly *NEMO*), the regulatory subunit of the IκB kinase (IKK) complex required for canonical NF-κB activation. It is characterized by four sequential (though often overlapping and irregularly timed) stages of skin lesions following the lines of Blaschko, together with variable involvement of teeth, hair, nails, eyes, and the central nervous system (CNS). It is X-linked dominant and male-lethal in utero for the common null allele — the disease is seen almost exclusively in females, who survive because of functional X-chromosome mosaicism (lyonization) ([StatPearls, NBK578194](https://www.ncbi.nlm.nih.gov/books/NBK578194/); [GeneReviews, NBK1472](https://www.ncbi.nlm.nih.gov/books/NBK1472/)).

**Key identifiers:**
- **OMIM:** #308300 (Incontinentia Pigmenti) ([OMIM #308300](https://omim.org/entry/308300))
- **Related allelic disorder:** OMIM #300291 — Ectodermal Dysplasia and Immunodeficiency 1 (EDA-ID1), from hypomorphic *IKBKG* alleles in males
- **Orphanet:** ORPHA:464 ([Orphanet: Incontinentia pigmenti](https://www.orpha.net/en/disease/detail/464))
- **MONDO:** MONDO:0010631
- **ICD-10:** Q82.3; **ICD-11:** LD27 / EA90 (skin pigmentation disorders, genetic)
- **MeSH:** D007184 (Incontinentia Pigmenti)
- **Gene:** *IKBKG*/NEMO, HGNC:5961, Xq28

**Synonyms:** Bloch-Sulzberger syndrome; Bloch-Siemens syndrome; melanoblastosis cutis linearis; pigmented dermatosis, Siemens-Bloch type; NEMO deficiency syndrome (for the allelic immunodeficiency phenotype).

**Evidence basis:** Most literature is aggregated disease-level data from case series, national/regional registries, and systematic reviews (rather than large-scale EHR studies), reflecting the disease's rarity. The most recent, methodologically strongest source is a Danish **nationwide population-based cohort** (n=75, validated via the Danish National Patient Registry) that is more representative than earlier tertiary-referral case series ([Herlin et al. 2024, PMID:39623400](https://pubmed.ncbi.nlm.nih.gov/39623400/); [PMC11613904](https://pmc.ncbi.nlm.nih.gov/articles/PMC11613904/)).

---

## 2. Etiology

**Disease causal factor — genetic, monogenic:** IP is caused by heterozygous (in females) loss-of-function pathogenic variants in *IKBKG*/NEMO on Xq28. It is a purely genetic/genomic disorder; there is no known environmental, infectious, or lifestyle contribution to the primary lesion. The mutation typically arises **de novo** (~65% of cases) but can be inherited from an unaffected or mildly affected mosaic mother (~35%) ([GeneReviews NBK1472](https://www.ncbi.nlm.nih.gov/books/NBK1472/)).

**Genetic risk factor — the recurrent IKBKGdel (exon 4–10 deletion):** The overwhelming majority (≈65–80% of unrelated probands) carry an identical **11.7-kb deletion removing exons 4–10** of *IKBKG*, which abolishes protein function entirely. This deletion is generated by **non-allelic homologous recombination (NAHR)** between two 870-bp direct repeats termed **MER67B**, one in intron 3 and one downstream of exon 10 — a genomic architecture that makes this a true *recurrent* rearrangement rather than an independent mutational event in each family ([International IP Consortium / Fusco et al., PMID:19603533](https://pubmed.ncbi.nlm.nih.gov/19603533/); [Frontiers Pediatr. 2022, PMC9485571](https://pmc.ncbi.nlm.nih.gov/articles/PMC9485571/)). The remainder of cases carry small deletions/insertions, nonsense, splice-site, or (rarely) missense variants scattered across the gene; complete gene deletions (removing neighboring genes) also occur via Xq28 microdeletion/microduplication mechanisms at this same locus.

**Environmental risk factors:** None established — IP is not associated with parental age, toxin exposure, infection, or in utero exposures. Because the mutation is X-linked and typically lethal to hemizygous male conceptuses, **sex** (female) is itself the dominant "risk factor" for a liveborn, clinically recognized case.

**Protective / modifying factors:**
- **Skewed X-chromosome inactivation (XCI):** In affected females, cells expressing the mutant allele undergo NEMO-dependent apoptotic elimination (loss of NF-κB-mediated anti-apoptotic signaling upon TNF exposure), producing extremely skewed XCI in blood and skin toward the wild-type allele by birth. This skewing is itself the mechanism by which affected females survive and is a diagnostic/counseling tool (X-inactivation studies in unaffected relatives) ([GeneReviews NBK1472](https://www.ncbi.nlm.nih.gov/books/NBK1472/); [PMC7767561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7767561/)).
- **Mechanisms permitting male survival** (rare): (1) **somatic post-zygotic mosaicism** for the deletion (mixture of mutant and wild-type cells, analogous to female lyonization); (2) **47,XXY karyotype (Klinefelter syndrome)**, which supplies a second X allele and allows skewed inactivation as in females; (3) **hypomorphic (partial-function) missense/point variants** rather than the null exon 4–10 deletion, which are compatible with hemizygous male survival but typically produce a distinct, more immunodeficiency-predominant phenotype (EDA-ID) rather than classic IP ([Bruynseels et al./AJHG, PMID:11673821](https://pubmed.ncbi.nlm.nih.gov/11673821/); [Cell.com Survival of Male Patients](https://www.cell.com/fulltext/S0002-9297(07)61250-6)).
- **Gene-environment interaction:** Not a feature of this disease — pathogenesis is cell-autonomous (keratinocyte genotype × TNF-family cytokine exposure), not an external environmental modifier per se; see Mechanism section for the TNF-triggered apoptotic amplification loop, which is the closest analog to a "second hit."

---

## 3. Phenotypes

### Cutaneous phenotypes (hallmark; present in ~90–95% of patients; first sign in nearly all cases)

Skin lesions follow **Blaschko's lines** and progress through **four classic, often overlapping stages** with irregular onset/duration (Landy & Donnai major criterion) ([Actas Dermo-Sifiliográficas review, PMID:30660327](https://pubmed.ncbi.nlm.nih.gov/30660327/); [Minić et al. update, PMID:23802866](https://pubmed.ncbi.nlm.nih.gov/23802866/)):

| Stage | Clinical description | Typical timing | Histopathology | Suggested HPO |
|---|---|---|---|---|
| **I – Vesicular/bullous** | Erythematous linear vesiculobullous/pustular eruption on limbs/trunk | Birth to ~4 months (often present at birth or first 2 weeks) | Eosinophilic spongiosis, intraepidermal eosinophil-filled vesicles, dyskeratotic keratinocytes | HP:0025500 (Vesiculobullous rash) / HP:0008066 |
| **II – Verrucous** | Linear, warty, hyperkeratotic papules/plaques | Weeks–months, overlapping with stage I | Hyperkeratosis, acanthosis, papillomatosis, dyskeratosis | HP:0000988 (Skin rash) / verrucous lesion terms |
| **III – Hyperpigmented** | Swirled/marbled ("splash of paint") grey-brown hyperpigmentation along Blaschko lines, often NOT at sites of prior blistering | Infancy through childhood; may be the presenting sign in older infants | Abundant dermal melanophages with pigment incontinence (the eponymous finding) | HP:0007441 (Reticulate hyperpigmentation) / HP:0001010 (Hyperpigmentation of the skin) |
| **IV – Atrophic/hypopigmented** | Pale, hairless, atrophic, anhidrotic linear streaks/patches, often on the calves | Adolescence–adulthood; may persist lifelong | Epidermal atrophy, loss of rete ridges and adnexal structures, reduced basal melanocytes | HP:0001010 / HP:0000953 (Hyperpigmented skin patches) / hypopigmentation terms |

The vesicular stage carries a diagnostically important **triad**: characteristic Blaschko-linear vesicles + peripheral blood **eosinophilia** + histopathologic eosinophilic spongiosis — eosinophil counts of 5–79% (leukocytosis up to ~84,000/µL), peaking at 3–5 weeks of life, driven by NEMO-competent neighboring keratinocytes secreting **eotaxin** ([PMC12569988 "Diagnostic Triad"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12569988/); Medscape workup).

### Extracutaneous phenotypes (minor criteria; frequency data drawn from the largest modern cohorts, principally the 2024 Danish nationwide study, PMID:39623400, and classic case series)

| System | Phenotype | Frequency | Onset | Course | HPO suggestion |
|---|---|---|---|---|---|
| **Teeth** | Hypodontia/anodontia, delayed eruption, peg-shaped/conical teeth, microdontia, impacted teeth | 17–34% (older series); 58.7% (2024 nationwide cohort) | Deciduous and permanent dentition | Stable | HP:0000679 (Abnormal dentition), HP:0000692 (Hypodontia), HP:0000693 (Peg-shaped teeth) |
| **Hair** | Scarring vertex alopecia, wiry/coarse/lusterless hair, sparse hair in early childhood | 26–50% | Infancy onward | Often stable/permanent scarring | HP:0004291 (Cicatricial alopecia), HP:0002212 (Scalp hair loss) |
| **Nails** | Pitting, ridging, subungual hyperkeratosis, onycholysis, nail dystrophy (may mimic tumors) | 7–40% (16% in 2024 cohort) | Childhood | Stable/chronic | HP:0001817 (Toenail dystrophy) / HP:0004097 (Abnormality of the nail) |
| **Eyes** | Retinal vascular anomalies (peripheral avascularity, neovascularization), retinal detachment, strabismus, cataract, optic atrophy, microphthalmia | 22.6–35% (up to 77% in some referral cohorts) | Neonatal–infancy for the sight-threatening retinal vasculopathy | **Progressive if untreated** — the retinopathy is the leading cause of permanent disability | HP:0000556 (Retinal detachment), HP:0007843 (Attenuation of retinal blood vessels), HP:0000486 (Strabismus), HP:0000518 (Cataract) |
| **CNS** | Seizures, microcephaly, encephalopathy, motor/cognitive delay, hemiparesis, ischemic/hemorrhagic stroke | ~30% (30.7% in the 2024 cohort); seizures ~20% | Predominantly **neonatal period** (correlates with cerebrovascular injury severity) | Can be monophasic (neonatal) or evolve to fixed deficits; occasional acquired lesions later | HP:0001250 (Seizure), HP:0001300 (Encephalopathy), HP:0002119 (Ventriculomegaly), HP:0002315 (Headache) |
| **Skeletal/other** | Nipple/breast anomalies (accessory nipples, hypoplastic breast), skeletal anomalies, short stature (rare) | <10% | Variable | Stable | HP:0006190 (Rudimentary supernumerary nipple) |
| **Systemic laboratory** | Peripheral eosinophilia/leukocytosis (stage I–II) | Common in neonatal period | Neonatal, resolves | Self-limited | HP:0001880 (Eosinophilia) |

**Quality-of-life impact:** Dermatologic manifestations largely **attenuate over years** and rarely cause lasting disability once past the scarring/pigmentary stages, but **ocular disease persists lifelong** and is the dominant driver of long-term QoL burden (progressive visual impairment, need for lifelong ophthalmologic surveillance) ([Actas Dermo-Sifiliográficas](https://www.actasdermo.org/en-incontinentia-pigmenti-articulo-S1578219019301015)). Neurodevelopmental sequelae from neonatal CNS injury (motor and cognitive impairment, and documented **learning disabilities as a "fundamental hallmark"** even without gross neuroimaging abnormality, per PMC3906222) are the other major long-term QoL determinant. No validated disease-specific QoL instrument was identified in the literature searched; generic pediatric QoL and visual-function instruments have been used in small cohorts.

---

## 4. Genetic / Molecular Information

**Causal gene:** *IKBKG* (NEMO), HGNC:5961, Xq28, encoding the ~48-kDa NF-κB essential modulator, the non-enzymatic regulatory/scaffolding subunit of the IKK complex.

**Pathogenic variant spectrum:**
- **Recurrent 11.7-kb deletion of exons 4–10 ("IKBKGdel")** — accounts for ~65–80% of unrelated probands; a complete-loss-of-function null allele generated by NAHR between MER67B repeats flanking the deleted region ([PMID:19603533](https://pubmed.ncbi.nlm.nih.gov/19603533/)). Because the genomic architecture at Xq28 is inherently unstable, this exact deletion recurs independently in unrelated families rather than representing a single ancestral founder allele.
- **Small indels, nonsense, and canonical splice-site variants** distributed across the remaining coding exons — the second most common class, usually also null/loss-of-function.
- **Missense/hypomorphic variants** — rare in classic IP; these more often produce the allelic disorder **EDA-ID (Ectodermal Dysplasia and Immunodeficiency 1, OMIM #300291)** in hemizygous males, with impaired but not abolished NF-κB signaling, hypogammaglobulinemia, poor polysaccharide antibody responses, and susceptibility to pyogenic/mycobacterial infection ([PMID:26117626](https://pubmed.ncbi.nlm.nih.gov/26117626/); [PMID:28993958](https://pubmed.ncbi.nlm.nih.gov/28993958/); [PMC12221755, "Clinical relevance of loss-of-function mutations of NEMO/IKBKG"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12221755/)). Some hypomorphic alleles produce combined IP + immunodeficiency + immune thrombocytopenia phenotypes, illustrating an allelic severity continuum from null (male-lethal/classic IP in mosaic or XXY males) → hypomorphic (EDA-ID, viable males) → complete loss with somatic mosaicism (mild/atypical IP in males).
- **Larger microdeletions/microduplications at Xq28** encompassing *IKBKG* and neighboring genes can also generate the exon 4–10 deletion allele de novo through a complex rearrangement mechanism, and can produce contiguous-gene phenotypes.

**Variant classification / interpretation:** ACMG/AMP pathogenic and likely-pathogenic classifications predominate in ClinVar for the recurrent deletion and truncating variants; missense VUS interpretation is complicated by segmental duplication of *IKBKG* (a pseudogene, Δ*IKBKG*, lies distally and complicates short-read NGS/CNV calling) — **long-read sequencing** is increasingly recommended for unambiguous resolution of the exon 4–10 deletion and to distinguish it from the paralogous pseudogene sequence ([npj Genomic Medicine 2024](https://www.nature.com/articles/s41525-024-00421-z); [PMC11838753, "Long-Read Sequencing is Required for Precision Diagnosis"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11838753/)).

**Population/allele frequency:** Because the pathogenic deletion sits in a segmentally duplicated, structurally unstable region, it is essentially **absent from gnomAD/1000 Genomes/ExAC** as a "population variant" — it behaves as a recurrent de novo/rare familial lesion rather than a polymorphism, consistent with strong purifying selection against male-lethal null alleles.

**Somatic vs. germline origin:** IP is a **germline (constitutional) X-linked disorder in females**; however, the phenotype itself is a manifestation of **mosaicism** (X-inactivation mosaicism is obligatory for female survival), and rare surviving affected males owe survival to **true post-zygotic somatic mosaicism** for the mutation itself (distinct from XCI mosaicism) ([PMID:11673821](https://pubmed.ncbi.nlm.nih.gov/11673821/)).

**Functional consequence:** Loss of function — NEMO/IKKγ is required for IKK-complex-mediated phosphorylation and degradation of IκB, the step that liberates NF-κB dimers (RelA/p65–p50) to translocate to the nucleus. Loss of NEMO function abolishes canonical NF-κB activation in response to TNF-family cytokines, IL-1, and other pro-inflammatory/pro-survival stimuli, converting a normally pro-survival signal into a pro-apoptotic one in affected cells ([Smahi et al./Courtois review, PMID:12351572, "The NF-κB signalling pathway in human diseases: from incontinentia pigmenti to ectodermal dysplasias and immune-deficiency syndromes"](https://pubmed.ncbi.nlm.nih.gov/12351572/)).

**Modifier genes:** No validated disease-modifying loci are established beyond X-inactivation ratio itself, which functions as the principal "modifier" of phenotypic severity in females.

**Epigenetics:** The central epigenetic phenomenon in IP is **extreme, non-random (skewed) X-chromosome inactivation**, arising secondarily from selective apoptotic elimination of cells expressing the mutant allele rather than from a primary epigenetic lesion; this is well documented in blood leukocytes and can be used diagnostically to identify carrier relatives when the causal variant cannot itself be found ([PMC7767561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7767561/)).

**Chromosomal abnormalities:** 47,XXY (Klinefelter syndrome) is a documented mechanism enabling survival of hemizygous null-mutation males, via provision of a second X allele subject to skewed inactivation, analogous to the female mechanism.

**Suggested ontology terms:** Gene — HGNC:5961 (*IKBKG*); GO:0007249 (I-κB kinase/NF-κB signaling); GO:0051092 (positive regulation of NF-κB transcription factor activity); GO:0008384 (IκB kinase activity); GO:0006915 (apoptotic process).

---

## 5. Environmental Information

IP has **no established environmental, lifestyle, or infectious causal contribution** to disease onset — the primary lesion is a germline/mosaic *IKBKG* variant. There is no CTD/TOXNET association implicating toxins, and no infectious trigger for the disease itself. The main environmental interaction of clinical relevance is **iatrogenic/incidental**: (1) neonatal vesicular-stage lesions are frequently mistaken for and must be differentiated from **neonatal herpes simplex virus infection** ([PMC6020482, "Incontinentia Pigmenti Misdiagnosed as Neonatal HSV Infection"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020482/)) — importantly, HSV and IP can also **coexist**, so HSV must always be actively excluded rather than assumed to be the diagnosis; and (2) case reports of complications following treatment interventions (e.g., necrotizing enterocolitis following intravitreal bevacizumab in an infant with IP) reflect treatment-related, not disease-causal, environmental exposure ([PMC6792241](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6792241/)). No infectious agent, occupational exposure, or lifestyle factor is described as a disease trigger in the reviewed literature.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular trigger:** Heterozygous loss-of-function *IKBKG* variant (most commonly the exon 4–10 deletion) abolishes NEMO/IKKγ scaffolding function within the IKK complex (IKKα/IKKβ/NEMO), which is normally required for K63-linked polyubiquitin-dependent activation of the complex downstream of TNFR1, IL-1R/TLR, and CD40 signaling ([PMID:12351572](https://pubmed.ncbi.nlm.nih.gov/12351572/)).
2. **Cellular consequence — loss of NF-κB-mediated cytoprotection:** Without functional NEMO, IκB is not degraded, NF-κB (RelA/p65) cannot translocate to the nucleus, and NF-κB target anti-apoptotic genes (e.g., *BCL2*, *BCL-XL*, *cFLIP*, *cIAP1/2*) are not induced. NEMO-deficient keratinocytes therefore become **exquisitely sensitive to TNF-α-induced apoptosis/necrosis** — a signal that in normal cells is pro-survival becomes lethal in NEMO-null cells.
3. **Amplification loop (the key mechanistic feature of IP):** Neighboring **NEMO-competent** keratinocytes (the cells that retained the wild-type X as the active allele) respond normally to inflammatory stimuli by activating NF-κB and secreting chemokines/cytokines — **eotaxin, RANTES, MCP-1, IL-1, TNF-α, IFN-γ, lymphotactin** — which (a) recruit eosinophils and other inflammatory cells (explaining the pathognomonic eosinophilic spongiosis and peripheral eosinophilia of stage I/II) and (b) further amplify TNF-driven apoptosis specifically in the neighboring NEMO-deficient cells ([Frontiers Pediatr. 2022, PMC9485571](https://pmc.ncbi.nlm.nih.gov/articles/PMC9485571/); Medscape pathophysiology).
4. **Clonal resolution:** Progressive apoptotic elimination of NEMO-deficient keratinocyte clones, coupled with proliferative replacement by NEMO-expressing keratinocytes, produces the **temporal evolution of skin stages** — inflammatory/vesicular (active killing + inflammation) → verrucous (reactive hyperproliferation) → hyperpigmented (dermal macrophage/melanophage clearance of released melanin — "incontinence of pigment," the eponymous histologic finding) → atrophic/hypopigmented (end-stage tissue with reduced adnexal structures and melanocyte density after clonal loss) ([PMID:24937825](https://pubmed.ncbi.nlm.nih.gov/24937825/)).
5. **Vascular mechanism (retina/CNS):** The same NEMO-dependent apoptosis-vs-survival logic operates in vascular endothelium: mosaic loss of NF-κB protection in endothelial/vascular precursor clones is proposed to underlie the **occlusive retinal and cerebral microvasculopathy** — avascular peripheral retina, neovascularization, and in the CNS, small-vessel occlusion, ischemic/hemorrhagic infarction, and cerebral arteriopathy — that account for the sight- and life-threatening complications of IP ([Cerebral Arteriopathy report, PMID:26706482](https://pubmed.ncbi.nlm.nih.gov/26706482/); [PMC3576363, systematic review of CNS anomalies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3576363/)).
6. **A validated "reverse experiment":** A case report of IP recrudescence during **TNF/NF-κB blockade in an inflammatory malignancy context** provides a natural experiment supporting the causal centrality of NF-κB blockade to IP pathophysiology in vivo in humans ([PMC10520490](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520490/)).

**Upstream vs. downstream:** Upstream = germline/mosaic *IKBKG* genotype and X-inactivation pattern (fixed, not modifiable). Downstream = TNF-family-cytokine-triggered, cell-autonomous keratinocyte/endothelial apoptosis, a cell-non-autonomous inflammatory amplification loop, and tissue-level consequences (skin staging, retinal vaso-occlusion, cerebral small-vessel injury).

**Cell types involved:** Epidermal keratinocyte (basal and suprabasal), dermal melanophage/macrophage, eosinophil, vascular endothelial cell (retinal and cerebral), and (in the allelic EDA-ID spectrum) lymphocytes/monocytes.

**Molecular profiling:** No large-scale transcriptomic/proteomic/metabolomic datasets specific to IP skin or blood were identified in this search (reflecting the rarity of the disease and lack of GEO/PRIDE/MetaboLights-deposited disease-specific omics datasets); mechanistic insight instead derives predominantly from the *Ikbkg*-null/keratinocyte-conditional mouse model (below) and from targeted cytokine/histopathology studies in humans.

**Suggested ontology terms:**
- GO Biological Process: GO:0007249 (I-κB kinase/NF-κB signaling), GO:0006915 (apoptotic process), GO:0034612 (response to tumor necrosis factor), GO:0006954 (inflammatory response), GO:0001525 (angiogenesis, for the retinal vasculopathy).
- GO Molecular Function: GO:0008384 (IκB kinase activity).
- Cell Ontology: CL:0000312 (keratinocyte), CL:0000158 (club cell — N/A; use CL:0000148 melanocyte), CL:0000771 (eosinophil), CL:0000115 (endothelial cell).
- CHEBI: CHEBI:60485 (tumor necrosis factor) — for the causal cytokine.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin/integument (epidermis, dermis, hair follicles, nails), eye (retina primarily; also lens, optic nerve), central nervous system (brain parenchyma and cerebral vasculature).
- **Secondary/complication-driven:** Retinal detachment as a complication of untreated retinal vasculopathy; secondary infections of denuded/bullous skin; dental arch/palate anomalies as a developmental consequence of ectodermal involvement.
- **Body systems:** Integumentary, ophthalmologic, neurologic, dental/craniofacial, and (in the allelic EDA-ID spectrum) immune system.

**Tissue/cell level:**
- Epidermis (keratinocytes, CL:0000312), melanocytes (CL:0000148) and their pigment-laden dermal macrophage counterparts (melanophages), hair follicle (pilosebaceous unit), nail matrix, retinal vascular endothelium (CL:0000115) and retinal pigment epithelium, cerebral small-vessel endothelium, cerebral cortical/subcortical neurons and white matter.

**Subcellular level:** The core molecular lesion operates through cytoplasmic IKK-complex signaling (GO:0008385 IκB kinase complex) leading to nuclear translocation of NF-κB (nucleus, GO:0005634) and mitochondrial-pathway apoptosis (GO:0005739) in affected cells.

**Localization (UBERON):**
- UBERON:0002097 (skin epidermis) — Blaschko-linear distribution, classically trunk and extremities.
- UBERON:0000966 (retina) — peripheral retinal avascular zone with a sharp vascular/avascular demarcation, most often temporal.
- UBERON:0000955 (brain) — periventricular white matter, corpus callosum, basal ganglia/thalami, and small-vessel cerebral parenchyma.
- UBERON:0001091 (tooth) — dental lamina/enamel organ.

**Lateralization:** Cutaneous, and often CNS, lesions are classically **unilateral or strikingly asymmetric**, reflecting the mosaic (clonal, Blaschko-line) nature of the disorder — e.g., documented **unilateral cerebral atrophy** as a distinct, non-acute neuroimaging phenotype of IP ([PMID:30090155](https://pubmed.ncbi.nlm.nih.gov/30090155/)). Retinal vasculopathy can be unilateral or bilateral and asymmetric in severity.

---

## 8. Temporal Development

**Onset:** Congenital/neonatal for the defining cutaneous stage I lesions (present at birth or within the first 2 weeks in the majority; occasionally delayed to weeks 3–4). CNS and retinal complications, when they occur, present predominantly in the **neonatal period** as well, reflecting a shared early-life window of vulnerability tied to active mosaic apoptotic clearance and vascular development. Onset pattern for the acute complications (seizures, stroke-like injury) is typically **acute/subacute**; the skin disease itself evolves in an **insidious, staged** fashion.

**Progression / disease course:**
- **Skin:** Classic **stage-wise progression** (I→II→III→IV) though stages "may overlap" and their "sequence is irregular" and duration variable ([PMID:24937825](https://pubmed.ncbi.nlm.nih.gov/24937825/)). The dermatologic phenotype is generally **self-attenuating** over years — stage IV (atrophic/hypopigmented) lesions may persist into adulthood but are cosmetically stable rather than progressive.
- **Retina:** Vaso-occlusive disease can be **rapidly progressive** in untreated infants, evolving from peripheral avascularity to neovascularization to tractional retinal detachment within weeks to months if unmonitored — this is the principal reason for close, serial ophthalmologic screening in the first months of life.
- **CNS:** Acute neonatal encephalopathy/seizures/stroke represent a discrete early "critical period"; some neuroimaging abnormalities (e.g., diffusion restriction) have been reported as **nearly completely reversible** on follow-up imaging in some cases ([AJNR PMC report](https://www.ajnr.org/content/29/3/431)), while others (unilateral cerebral atrophy) are fixed/progressive-appearing structural sequelae.
- **Disease duration:** Chronic, lifelong condition overall, but with a bimodal severity pattern — an early (neonatal/infancy) period of highest risk for irreversible ocular and neurologic injury, followed by a **chronic stable phase** in surviving patients without early complications, in whom life expectancy and general health are normal ([StoryMD/clinical summaries](https://storymd.com/journal/qj3gxvlcaw-incontinentia-pigmenti/page/937edtzbre-what-is-the-long-term-outlook-for-people-with-incontinentia-pigmenti); Orphanet).

**Patterns:**
- **Remission:** The cutaneous eruption remits spontaneously (clonal clearance mechanism, not treatment-induced) as NEMO-deficient keratinocyte clones are eliminated.
- **Critical period:** The first weeks to months of life constitute the critical window for both (a) diagnostic recognition (vesicular stage + eosinophilia triad) and (b) prevention of irreversible retinal/CNS injury through early ophthalmologic and neurologic screening — repeatedly emphasized across the ophthalmology literature as the key modifiable determinant of long-term outcome ([Orphanet J Rare Dis, "Early management of sight threatening retinopathy in incontinentia pigmenti," PMC/Springer](https://link.springer.com/article/10.1186/s13023-020-01509-2)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Historically cited birth prevalence: **0.7 per 100,000 births** (Orphanet, 2013 estimate); more recent series report **1.2 per 100,000** ([search synthesis]); the most recent, methodologically robust nationwide Danish study (2024) found a birth prevalence of **2.37 per 100,000 live births (95% CI 1.74–3.25), or ~1 in 42,194** — roughly twice earlier estimates, likely reflecting improved case ascertainment ([PMID:39623400](https://pubmed.ncbi.nlm.nih.gov/39623400/)). Orphanet also cites a birth prevalence of approximately **1 in 143,000** in some estimates and a period prevalence in the US of **0.88 per 100,000**. Older birth-surveillance-system estimates were as low as **0.6–0.7 per 1,000,000**, reflecting substantial historical under-ascertainment.
- IP is universally described as **rare**, with wide variance across studies attributable to differing case-finding methodology (clinical vs. registry vs. genetically confirmed cohorts).

**Inheritance pattern:** X-linked dominant, **male-lethal** for the common null allele (in utero loss of hemizygous null male conceptuses). GeneReviews states the expected live-birth ratio for offspring of an affected (heterozygous) mother is approximately **1/3 unaffected female : 1/3 affected female : 1/3 unaffected male**, with affected male conceptuses largely lost to miscarriage ([GeneReviews NBK1472](https://www.ncbi.nlm.nih.gov/books/NBK1472/)). Sex ratio in liveborn, clinically recognized patients is reported as approximately **20 females : 1 male** (rare surviving males owe this to somatic mosaicism, Klinefelter 47,XXY, or hypomorphic alleles, as above).

**Penetrance/expressivity:** Effectively complete penetrance for cutaneous disease in liveborn heterozygous females, but **markedly variable expressivity** for extracutaneous (dental, ocular, hair, nail, CNS) manifestations — a direct consequence of stochastic X-inactivation ratios between individuals.

**Genetic anticipation:** Not described — IP is not a repeat-expansion disorder.

**Germline mosaicism:** Documented and clinically important — a molecularly normal (or apparently unaffected/mildly affected) mother can have **germline (gonadal) mosaicism** for the *IKBKG* variant, producing **familial recurrence despite an apparently de novo variant in the index case**, a scenario specifically studied for genetic-counseling implications ([Steffann et al. 2024, AJMG-A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63591)).

**Founder effects:** The exon 4–10 deletion is **recurrent (arising independently in multiple unrelated families via NAHR)** rather than a single ancestral founder allele — an important distinction from typical founder-mutation disorders.

**Consanguinity:** Not a relevant risk factor, given the X-linked dominant, largely de novo mutational mechanism.

**Carrier frequency:** Not meaningfully defined in the classic sense (unlike recessive carrier screening), given the predominance of de novo mutation and male lethality; population allele frequency for the pathogenic deletion is essentially unobservable in gnomAD-type reference cohorts due to strong negative selection and segmental-duplication artifacts.

**Population demographics:** No strong ethnic or geographic clustering has been reported; IP occurs worldwide across populations. Age distribution of affected individuals in registries spans neonates through adults, consistent with normal life expectancy in patients without severe neonatal complications. Sex ratio (~20:1 female:male) is the most consistent demographic feature.

---

## 10. Diagnostics

**Clinical diagnostic criteria:** **Landy and Donnai (1993)** established major criteria (any of the four Blaschko-linear skin stages) and minor criteria (dental, ocular, CNS, hair, nail, palate, breast/nipple anomalies; history of multiple male miscarriages; characteristic histopathology). **Minić et al. (2014)** revised/updated these criteria to incorporate molecular genetics, adding **positive first-degree family history** and **a pathogenic *IKBKG*/NEMO variant** as additional diagnostic criteria alongside the updated major/minor clinical criteria ([PMID:23802866](https://pubmed.ncbi.nlm.nih.gov/23802866/)).

**Laboratory tests:**
- Complete blood count with differential — **peripheral eosinophilia/leukocytosis** is a key supportive finding during stages I–II (LOINC panels for CBC/differential apply; no IP-specific biomarker assay exists).
- Skin biopsy/histopathology by stage (eosinophilic spongiosis → hyperkeratosis/dyskeratosis → dermal melanophages/pigment incontinence → epidermal atrophy) — SNOMED CT histopathology terms for spongiotic dermatitis, pigment incontinence.

**Genetic testing (primary confirmatory modality):**
- **Recommended approach (GeneReviews):** Targeted testing for the recurrent **exon 4–10 deletion** first (accounts for the majority of cases), typically by MLPA, long-range PCR, or CNV-sensitive assays, given that standard short-read NGS/exome sequencing can miss or misassign this deletion due to the *IKBKG* pseudogene (Δ*IKBKG*) segmental duplication.
- If the recurrent deletion is not found, **sequence analysis of the full *IKBKG* coding region** (single-gene sequencing or NF-κB/immunodeficiency-focused gene panels) is the next step.
- **Long-read sequencing** is increasingly advocated as the most precise, single-assay strategy to resolve the deletion breakpoints and rule out pseudogene interference, and has been proposed as an efficient molecular testing strategy specifically for IP ([npj Genomic Medicine 2024](https://www.nature.com/articles/s41525-024-00421-z); [PMC11838753](https://pmc.ncbi.nlm.nih.gov/articles/PMC11838753/)).
- **Chromosomal microarray/karyotype:** Karyotyping is relevant specifically in surviving affected males to test for 47,XXY (Klinefelter) as a survival mechanism.
- **X-inactivation studies** in peripheral blood are a useful adjunct, especially to identify carrier female relatives when the causative variant cannot be confidently identified in the proband ([PMC7767561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7767561/)).
- **Prenatal/preimplantation testing:** Both prenatal diagnosis (in known-familial pathogenic variants) and preimplantation genetic testing are available and used for reproductive planning given the high recurrence risk to offspring of affected mothers.

**Imaging:**
- **Ophthalmologic:** Fluorescein angiography (FA) is central to detecting peripheral retinal avascularity and neovascularization before clinically apparent detachment.
- **Neuroimaging:** Brain MRI/MR angiography and diffusion-weighted imaging for neonates with seizures/encephalopathy — findings include small-vessel occlusion, ischemic/hemorrhagic changes, corpus callosum hypoplasia, ventriculomegaly, periventricular white matter disease, polymicrogyria, and neuronal heterotopia ([MedLink Neurology summary](https://www.medlink.com/articles/incontinentia-pigmenti); [PMC3576363](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3576363/)).

**Differential diagnosis (stage-specific, per Medscape/EyeWiki synthesis):**
- **Stage I (vesicular):** Neonatal HSV, varicella, epidermolysis bullosa, bullous pemphigoid/impetigo, dermatitis herpetiformis, bullous SLE, linear IgA bullous dermatosis, pemphigus vulgaris, bullous mastocytosis — **neonatal HSV must always be actively excluded**, and the two conditions can coexist ([PMC6020482](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020482/)).
- **Stage II (verrucous):** Verruca vulgaris, linear epidermal nevus.
- **Stage III (hyperpigmented):** Linear and whorled nevoid hypomelanosis, dermatopathia pigmentosa reticularis, Naegeli-Franceschetti-Jadassohn syndrome, X-linked dominant chondrodysplasia punctata, other pigment mosaicism disorders.
- **Stage IV (atrophic/hypopigmented):** Hypomelanosis of Ito (key distinguishing feature: never has preceding bullous or verrucous lesions).

**Screening:** No population-based newborn or carrier screening program exists for IP (it is too rare and typically clinically apparent), but **targeted screening of at-risk relatives** (X-inactivation studies, targeted variant testing) is standard once a proband is identified, given the counseling implications of germline mosaicism.

---

## 11. Outcome / Prognosis

**Survival/mortality:** For **females without significant neonatal CNS or systemic complications, life expectancy is normal**. Mortality in IP is essentially confined to (a) in utero loss of hemizygous null male conceptuses (not counted in liveborn mortality statistics) and (b) rare severe neonatal complications (e.g., overwhelming cerebral vascular injury) in liveborn patients. No IP-specific 5-/10-year survival statistic (of the cancer-registry type) applies, as IP is not typically fatal in surviving liveborn patients.

**Morbidity/function:**
- **~20%** of patients develop neurologic sequelae ranging from mild to severe (motor deficits, epilepsy, intellectual disability); notably, **learning disabilities have been specifically flagged as a fundamental, under-recognized hallmark** of IP even in patients without overt structural brain lesions ([PMC3906222, "Learning Disabilities Are a Fundamental Hallmark of the Disease"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3906222/)).
- Ocular involvement (22.6–77% depending on cohort/referral bias) is the **principal source of persistent, lifelong QoL impact**, given that retinal vasculopathy, once established, is not reversible and dermatologic disease is not.
- Dental, nail, and hair anomalies are largely cosmetic/functional-minor and stable rather than progressive.

**Disease course/complications:** Principal complications are **tractional retinal detachment** (from untreated peripheral retinal vaso-occlusion/neovascularization), **neonatal seizures/encephalopathy**, and **ischemic/hemorrhagic cerebral injury**. Secondary skin infection during the bullous stage is a lesser but real risk.

**Prognostic factors:** The presence and severity of **neonatal CNS involvement** and **early retinal vasculopathy** are the dominant prognostic determinants for long-term disability; patients without these neonatal complications generally have normal physical and cognitive development and normal life expectancy. Early ophthalmologic screening/intervention is repeatedly identified in the literature as the single most impactful modifiable prognostic lever ([Orphanet J Rare Dis, "Early management of sight threatening retinopathy"](https://link.springer.com/article/10.1186/s13023-020-01509-2)).

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for IP — management is entirely **organ-specific, supportive, and surveillance-driven**, reflecting the mosaic/self-limited nature of the underlying cellular lesion once the vulnerable neonatal window has passed.

**Dermatologic (supportive care):**
- Gentle wound care for bullous lesions, avoidance of secondary infection; no specific pharmacotherapy alters the natural staged evolution. MAXO:0000950 (supportive care).

**Ophthalmologic (the best-defined interventional area):**
- **Serial ophthalmologic examination with fluorescein angiography** in the neonatal period/infancy to detect peripheral retinal avascularity before neovascularization/detachment develops — the standard of care recommendation across sources.
- **Laser photocoagulation** (parameters largely extrapolated from retinopathy-of-prematurity practice) of avascular retina is the primary treatment for progressive retinal neovascularization (MAXO term: laser therapy; NCIT procedure term applicable).
- **Anti-VEGF therapy (intravitreal bevacizumab)**: used as an **adjunct**, not first-line, given theoretical concern about systemic VEGF suppression in a multisystem vascular disorder (with documented case reports of adverse events, e.g., necrotizing enterocolitis post-injection) and given that IP is also associated with cerebrovascular disease/stroke risk — most authors recommend reserving anti-VEGF for severe/atypical cases with posterior neovascularization or media opacity precluding laser, as a **second-line** option rather than routine therapy; **no formal treatment consensus exists** ([PMID:30768227](https://pubmed.ncbi.nlm.nih.gov/30768227/); [PMID:30982292](https://pubmed.ncbi.nlm.nih.gov/30982292/); [Retina Today 2026](https://retinatoday.com/articles/2026-apr/incontinentia-pigmenti-associated-retinopathy); [PMC6792241](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6792241/)).
- Surgical retinal detachment repair (scleral buckle/vitrectomy) for established tractional detachment.

**Neurologic:** Standard antiepileptic pharmacotherapy for seizures; supportive/rehabilitative care (physical, occupational, speech therapy — MAXO:0000011, MAXO:0001351, MAXO:0000930) for motor/developmental delay.

**Dental:** Restorative/prosthodontic management of hypodontia/microdontia/peg-shaped teeth (implants, crowns, orthodontic planning) — a described multidisciplinary oral rehabilitation approach exists in the literature ([PMC10529459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10529459/)); NCIT:C15329 (surgical/dental procedure), MAXO:0000004 for surgical correction.

**Genetic counseling:** MAXO:0000079 (genetic counseling) is central to management — addressing the ~50% transmission risk from an affected mother (with the caveat of in utero loss of affected male conceptuses), the possibility of germline mosaicism in an apparently unaffected mother, and reproductive options (prenatal diagnosis, preimplantation genetic testing).

**Experimental/advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy directed at *IKBKG*/NF-κB restoration was identified as being in clinical development for IP in this search — the mosaic, self-clearing nature of the cutaneous disease and the segmental/organ-specific management paradigm for eye/CNS complications likely explain the absence of a systemic disease-modifying drug pipeline. No IP-specific NCT trials for a curative/disease-modifying agent were surfaced in this search; ophthalmology practice largely borrows ROP-derived treatment protocols and evidence rather than IP-dedicated trials.

**Treatment outcomes:** No large systematic response-rate data exist for anti-VEGF vs. laser specifically in IP given its rarity; case-series evidence supports revascularization following combined bevacizumab + laser in bilateral retinal vascular occlusion ([PMID:30768227](https://pubmed.ncbi.nlm.nih.gov/30768227/)).

**Treatment strategy/algorithm:** Multidisciplinary care pathway spanning neonatology, pediatric dermatology, pediatric ophthalmology, pediatric neurology, dentistry, and clinical genetics, with the **critical early-infancy period** for ophthalmologic/neurologic surveillance being the crux of the management algorithm.

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (no environmental exposure to avoid); the only "primary prevention" lever is **reproductive**, i.e., avoiding transmission through informed reproductive choices after genetic counseling (prenatal diagnosis, preimplantation genetic testing) in families with a known pathogenic variant.

**Secondary prevention (the most clinically important prevention modality for IP):** **Early detection of retinal vasculopathy** via scheduled ophthalmologic examination with fluorescein angiography in the neonatal period and infancy, enabling timely laser therapy before neovascularization progresses to tractional retinal detachment — repeatedly emphasized in the ophthalmology literature as the single highest-yield preventive intervention in this disease ([Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-020-01509-2)). Analogous early neurologic surveillance (clinical exam ± neuroimaging in symptomatic neonates) aims to identify and manage acute cerebrovascular injury promptly, though there is no specific prophylactic pharmacotherapy shown to prevent the cerebral vasculopathy itself.

**Genetic/prenatal screening:** Genetic counseling with prenatal or preimplantation genetic testing is offered to at-risk pregnancies once a familial pathogenic variant is known; X-inactivation studies can help risk-stratify apparently unaffected female relatives.

**Immunization:** Not applicable — IP is not an infectious or vaccine-preventable disease (though patients with the allelic EDA-ID phenotype from hypomorphic variants may warrant tailored immunization/infection-prophylaxis strategies given their underlying immunodeficiency — a distinct clinical entity from classic IP).

**Behavioral/public health/prophylaxis:** No behavioral, dietary, or public-health-level prevention measures apply to this monogenic disorder; the entire preventive strategy for morbidity reduction centers on **early clinical surveillance and reproductive genetic counseling** rather than exposure avoidance.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring IP-equivalent disease in non-human species (companion animals, livestock, or wildlife) was identified in this search — this is consistent with the disease being a rare, human-specific presentation of a mosaic X-linked lethal mutation, and no OMIA (Online Mendelian Inheritance in Animals) entry for a natural IP phenocopy was found. (Note: a distinct EDA-related hypohidrotic ectodermal dysplasia — caused by a different gene, *EDA*, not *IKBKG* — does occur naturally in Fleckvieh cattle as a collagen-triple-helix missense variant, but this is a different disease/gene and should not be conflated with IP; [PMC10815684](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10815684/).)

**Orthologous gene:** *Ikbkg*/NEMO is highly conserved in mammals (mouse *Ikbkg*, NCBI Gene; ortholog used extensively in the engineered mouse models below), but no spontaneous/natural disease-causing *Ikbkg* mutation has been reported in any non-human species.

**Comparative biology:** The evolutionary conservation of the NF-κB/IKK pathway across vertebrates underlies the strong construct and face validity of engineered rodent models (below) despite the absence of a naturally occurring animal disease.

---

## 15. Model Organisms

**Primary genetic model — the *Ikbkg*/NEMO-deficient mouse (the well-established IP model):**
- **Germline *Ikbkg*-null mice:** Disruption of the X-linked *Ikbkg* gene produces **male embryonic lethality**, completely abolishes NF-κB activation by pro-inflammatory cytokines, and impairs lymphocyte generation/persistence — directly recapitulating the human male-lethal pattern ([Rudolph et al., Molecular Cell 2000, PMID:10911992](https://pubmed.ncbi.nlm.nih.gov/10911992/?dopt=Abstract)).
- **Heterozygous female mice** develop **patchy skin lesions** with massive granulocyte infiltration, keratinocyte hyperproliferation, and increased keratinocyte apoptosis; affected animals show severe growth retardation and early mortality, but **surviving mice recover almost completely** as NEMO-deficient keratinocyte clones are cleared and replaced — this is a striking phenotypic and mechanistic parallel to the self-limited human cutaneous disease course ([Molecular Cell, "NEMO/IKKγ-Deficient Mice Model Incontinentia Pigmenti"](https://www.cell.com/molecular-cell/fulltext/S1097276500802634)).
- **Keratinocyte-restricted conditional *Ikbkg* deletion** (constitutive or inducible in adult skin) is sufficient to cause inflammatory skin lesions on its own, formally establishing the **NEMO-deficient keratinocyte as the initiating cell type** that triggers IP-like skin pathology, and additionally shows a strict **requirement for TNF signaling** in lesion development (crossing onto a TNF-receptor-deficient background rescues the phenotype) ([Nenci et al., PMID:16399796](https://pubmed.ncbi.nlm.nih.gov/16399796/)).
- Related mouse genetic work on **IKKα** (a downstream/interacting kinase) has additionally revealed unexpected, partially distinct roles in skin development and skin carcinogenesis, providing comparative mechanistic context for the IKK-complex/skin biology relationship ([PMC3730312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730312/)).

**Model characteristics:**
- **Phenotype recapitulation:** Excellent for the core disease logic — male lethality, mosaic-dependent female skin disease, granulocytic/eosinophilic-type inflammation, keratinocyte apoptosis, and spontaneous clonal resolution are all reproduced.
- **Model limitations:** The mouse model is a **construct-driven, engineered knockout** (not a spontaneous disease), and does not on its own model the human ocular retinal vasculopathy or CNS stroke/encephalopathy phenotypes as thoroughly characterized systems — those complications are documented primarily from human case series/imaging studies rather than from dedicated mouse retinal/cerebrovascular IP-model literature identified in this search.
- **Research applications:** The keratinocyte-specific conditional model in particular has been used to dissect the cell-autonomous vs. non-cell-autonomous (paracrine/TNF-dependent) contributions to lesion pathogenesis, directly informing the human "amplification loop" mechanistic model described in Section 6.

**Resources:** Mouse Genome Informatics (MGI) carries the *Ikbkg* knockout and conditional alleles used in these studies; no zebrafish, *Drosophila*, *C. elegans*, or iPSC/organoid IP-specific disease models were identified in this search, though iPSC-based mosaic keratinocyte modeling would be a plausible unexplored avenue given the human disease's cell-autonomous logic.

---

## Summary of Key Suggested Ontology Terms for KB Curation

- **Gene:** hgnc:5961 (*IKBKG*)
- **Disease:** MONDO:0010631; OMIM:308300; ORPHA:464; allelic disorder OMIM:300291 (EDA-ID1)
- **HPO (selected):** HP:0025500/HP:0008066 (vesiculobullous skin lesions), HP:0007441 (reticulate hyperpigmentation), HP:0000692 (hypodontia), HP:0000693 (peg-shaped teeth), HP:0004291 (cicatricial alopecia), HP:0001817 (nail dystrophy), HP:0000556 (retinal detachment), HP:0007843 (retinal vascular attenuation), HP:0001250 (seizure), HP:0001300 (encephalopathy), HP:0001880 (eosinophilia), HP:0010984 (digenic — N/A here; standard X-linked dominant term instead)
- **GO:** GO:0007249 (I-κB kinase/NF-κB signaling), GO:0008384 (IκB kinase activity), GO:0051092 (positive regulation of NF-κB transcription factor activity), GO:0006915 (apoptotic process), GO:0034612 (response to TNF), GO:0001525 (angiogenesis)
- **CL:** CL:0000312 (keratinocyte), CL:0000148 (melanocyte), CL:0000771 (eosinophil), CL:0000115 (endothelial cell)
- **UBERON:** UBERON:0002097 (epidermis), UBERON:0000966 (retina), UBERON:0000955 (brain), UBERON:0001091 (tooth)
- **CHEBI:** CHEBI:60485 (TNF, as a signaling ligand context) — treatments largely procedural (laser, anti-VEGF antibody: bevacizumab, CHEBI:64085)
- **MAXO:** MAXO:0000079 (genetic counseling), MAXO:0000014 (laser/radiation-adjacent procedure; more precisely an NCIT ophthalmic laser procedure term), MAXO:0000950 (supportive care), MAXO:0000011 (physical therapy)

---

### Sources

- [Frontiers | A case of Incontinentia Pigmenti associated with concurrent IKBKG/NEMO and MED13L mutations](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1819035/full)
- [Incontinentia Pigmenti: Learning Disabilities Are a Fundamental Hallmark of the Disease (PMC3906222)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3906222/)
- [OMIM #308300 — Incontinentia Pigmenti](https://omim.org/entry/308300)
- [OMIM #300291 — Ectodermal Dysplasia and Immunodeficiency 1](https://omim.org/entry/300291?search=300291&highlight=300291)
- [Incontinentia Pigmenti (Bloch-Sulzberger Syndrome) — StatPearls (NBK578194)](https://www.ncbi.nlm.nih.gov/books/NBK578194/)
- [Incontinentia Pigmenti — GeneReviews (NBK1472)](https://www.ncbi.nlm.nih.gov/books/NBK1472/)
- [Incontinentia Pigmenti — Actas Dermo-Sifiliográficas / PMID:30660327](https://www.actasdermo.org/en-incontinentia-pigmenti-articulo-S1578219019301015)
- [Frontiers | Uncovering incontinentia pigmenti: From DNA sequence to pathophysiology (PMC9485571)](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2022.900606/full)
- [Incontinentia pigmenti or Bloch-Sulzberger syndrome: a rare X-linked genodermatosis — PMID:24937825](https://pubmed.ncbi.nlm.nih.gov/24937825/)
- [Incontinentia Pigmenti (Bloch-Sulzberger Syndrome) — PMID:35201722](https://pubmed.ncbi.nlm.nih.gov/35201722/)
- [DermNet NZ — Incontinentia pigmenti](https://dermnetnz.org/topics/incontinentia-pigmenti)
- [Recrudescence of incontinentia pigmenti presenting as a paraneoplastic syndrome (PMC10520490)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10520490/)
- [Incontinentia Pigmenti — Medscape/eMedicine](https://emedicine.medscape.com/article/1114205-overview)
- [The NF-κB signalling pathway in human diseases — PMID:12351572](https://pubmed.ncbi.nlm.nih.gov/12351572/)
- [Systematic review of CNS anomalies in incontinentia pigmenti — Orphanet J Rare Dis (PMC3576363)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3576363/)
- [Prevalence and clinical characteristics of incontinentia pigmenti: a nationwide population-based study — PMID:39623400 / PMC11613904](https://pmc.ncbi.nlm.nih.gov/articles/PMC11613904/)
- [Orphanet: Incontinentia pigmenti (ORPHA:464)](https://www.orpha.net/en/disease/detail/464)
- [Survival of Male Patients with Incontinentia Pigmenti Carrying a Lethal Mutation — AJHG / PMID:11673821](https://pubmed.ncbi.nlm.nih.gov/11673821/)
- [A Case of a Surviving Male Infant with Incontinentia Pigmenti (PMC4903964)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4903964/)
- [Incontinentia Pigmenti: A Rare Case of Survival of a Male Infant (PMC11969057)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11969057/)
- [Microdeletion/duplication at the Xq28 IP locus causes a de novo IKBKG exon4_10 deletion — PMID:19603533](https://pubmed.ncbi.nlm.nih.gov/19603533/)
- [Clinical Utility Gene Card for incontinentia pigmenti (PMC6871521)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6871521/)
- [An efficient molecular genetic testing strategy for IP based on long fragment read sequencing — npj Genomic Medicine 2024](https://www.nature.com/articles/s41525-024-00421-z)
- [Incontinentia pigmenti inherited from a father with low-level atypical IKBKG deletion mosaicism (PMC9241235)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9241235/)
- [Revascularization After Intravitreal Bevacizumab and Laser Therapy — PMID:30768227](https://pubmed.ncbi.nlm.nih.gov/30768227/)
- [Treatment of retinopathy of incontinentia pigmenti by anti-VEGF — PMID:30982292](https://pubmed.ncbi.nlm.nih.gov/30982292/)
- [Necrotizing enterocolitis after intravitreal bevacizumab in an infant with IP (PMC6792241)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6792241/)
- [Incontinentia Pigmenti-Associated Retinopathy — Retina Today (2026)](https://retinatoday.com/articles/2026-apr/incontinentia-pigmenti-associated-retinopathy)
- [Early management of sight threatening retinopathy in incontinentia pigmenti — Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-020-01509-2)
- [Incontinentia pigmenti: presenting with neonatal seizures and diffuse MRI brain changes — PMID:22864149](https://pubmed.ncbi.nlm.nih.gov/22864149/)
- [Cerebral Arteriopathy in a Newborn With Incontinentia Pigmenti — PMID:26706482](https://pubmed.ncbi.nlm.nih.gov/26706482/)
- [Speckled brain lesions in Incontinentia Pigmenti patients with acquired brain syndromes — PMID:34133990](https://pubmed.ncbi.nlm.nih.gov/34133990/)
- [Unilateral Cerebral Atrophy in Incontinentia Pigmenti — PMID:30090155 (PMC6057194)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6057194/)
- [Incontinentia pigmenti — MedLink Neurology](https://www.medlink.com/articles/incontinentia-pigmenti)
- [Nearly Completely Reversible Brain Abnormalities in a Patient with IP — AJNR](https://www.ajnr.org/content/29/3/431)
- [Abnormal Dentition in a Boy with Incontinentia Pigmenti (PMC3484832)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3484832/)
- [Incontinentia Pigmenti — NORD](https://rarediseases.org/rare-diseases/incontinentia-pigmenti/)
- [NEMO/IKKγ-Deficient Mice Model Incontinentia Pigmenti — Molecular Cell / PMID:10911992](https://www.cell.com/molecular-cell/fulltext/S1097276500802634)
- [Skin lesion development in a mouse model of IP is triggered by NEMO deficiency in keratinocytes and requires TNF signaling — PMID:16399796](https://pubmed.ncbi.nlm.nih.gov/16399796/)
- [Mouse Genetic Models Reveal Surprising Functions of IκB Kinase Alpha in Skin (PMC3730312)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730312/)
- [A Diagnostic Triad in the Vesicular Stage of Incontinentia Pigmenti (PMC12569988)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12569988/)
- [Incontinentia Pigmenti Stages — NFED](https://nfed.org/learn/types/incontinentia-pigmenti/ip-stages/)
- [Incontinentia pigmenti diagnostic criteria update — Minić et al. / PMID:23802866](https://pubmed.ncbi.nlm.nih.gov/23802866/)
- [Incontinentia Pigmenti — EyeWiki](https://eyewiki.org/Incontinentia_Pigmenti)
- [Incontinentia Pigmenti Misdiagnosed as Neonatal Herpes Simplex Virus Infection (PMC6020482)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020482/)
- [Functional Evaluation of an IKBKG Variant Suspected to Cause Immunodeficiency Without Ectodermal Dysplasia — PMID:28993958](https://pubmed.ncbi.nlm.nih.gov/28993958/)
- [Novel hypomorphic mutation in IKBKG impairs NEMO-ubiquitylation — PMID:26117626](https://pubmed.ncbi.nlm.nih.gov/26117626/)
- [Clinical relevance of loss-of-function mutations of NEMO/IKBKG (PMC12221755)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12221755/)
- [X-linked anhidrotic ectodermal dysplasia with immunodeficiency is caused by impaired NF-κB signaling — Nature Genetics](https://www.nature.com/articles/ng0301_277)
- [A Missense Mutation in EDA Associated with X-Linked Recessive Hypohidrotic Ectodermal Dysplasia in Fleckvieh Cattle (PMC10815684)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10815684/)
- [X-Linked Ectodermal Dysplasia With Immunodeficiency Caused by NEMO Mutation — JAMA Dermatology](https://jamanetwork.com/journals/jamadermatology/fullarticle/419510)
- [Familial recurrence of incontinentia pigmenti due to de novo pathogenic variants in IKBKG — Steffann et al. 2024, AJMG-A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63591)
- [Long-Read Sequencing is Required for Precision Diagnosis of Incontinentia Pigmenti (PMC11838753)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11838753/)
- [Molecular analysis of low-level mosaicism of the IKBKG mutation using XCI pattern (PMC7767561)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7767561/)
- [Oral Rehabilitation as Part of a Multidisciplinary Treatment for IP (PMC10529459)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10529459/)
- [What Is the Long-Term Outlook for People with Incontinentia Pigmenti? — StoryMD](https://storymd.com/journal/qj3gxvlcaw-incontinentia-pigmenti/page/937edtzbre-what-is-the-long-term-outlook-for-people-with-incontinentia-pigmenti)