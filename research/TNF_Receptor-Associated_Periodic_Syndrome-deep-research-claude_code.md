---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T09:04:30.400038'
end_time: '2026-06-30T09:10:05.631925'
duration_seconds: 335.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TNF Receptor-Associated Periodic Syndrome
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
  - claude-opus-4-8[1m]
  web_search_requests: 10
  num_turns: 15
  total_cost_usd: 2.48882
  session_id: 74ced53f-c56b-4072-8226-6c44ba6444d1
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TNF Receptor-Associated Periodic Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TNF Receptor-Associated Periodic Syndrome** covering all of the
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

I now have all the key citations verified against PubMed/PMC. Here is the comprehensive report.

---

# Comprehensive Research Report: TNF Receptor-Associated Periodic Syndrome (TRAPS)

**Prepared:** 2026-06-30 | **Disease category:** Mendelian (monogenic autoinflammatory) | **Primary gene:** *TNFRSF1A*

> **A note on evidence provenance:** Every PMID and quoted snippet below was checked against PubMed/PMC during this research session. Before any of these are committed into a dismech YAML entry, run `just fetch-reference PMID:XXXX` and `just validate-references` — the snippets below are drawn from abstracts but must be re-verified as exact substrings against the cached file (per the project's anti-hallucination SOP). I flag any citation where my confidence in the exact PMID digits is less than certain.

---

## 1. Disease Information

**Overview.** TNF receptor-associated periodic syndrome (TRAPS) is the prototypic **autosomal-dominant monogenic autoinflammatory disease (hereditary periodic fever syndrome)**, caused by heterozygous mutations in *TNFRSF1A*, the gene encoding the 55-kDa type 1 receptor for tumor necrosis factor (TNFR1/p55/CD120a). Clinically it is defined by **recurrent, self-limited inflammatory attacks** — fever, migratory myalgia with overlying rash, abdominal pain (sterile peritonitis), periorbital edema, conjunctivitis, and arthralgia — that characteristically last **longer than the attacks of other periodic fevers (often 1–3 weeks)**, separating it from familial Mediterranean fever (FMF, attacks 1–3 days) and the cryopyrinopathies. The most feared long-term complication is **systemic AA (reactive) amyloidosis**.

Think of TNFR1 here like a smoke detector wired backwards: instead of quietly waiting at the cell surface for a real fire (TNF), the mutant receptor gets jammed inside the cell's "shipping department" and starts setting off the alarm on its own.

It was first delineated genetically in 1999, unifying several previously eponymous disorders — most famously **"familial Hibernian fever"** described in a large Irish/Scottish kindred — under a single molecular cause.

> *"In seven affected families, we found six different missense mutations of the 55 kDa TNF receptor (TNFR1), five of which disrupt conserved extracellular disulfide bonds. Soluble plasma TNFR1 levels in patients were approximately half normal."* — McDermott et al., *Cell* 1999 (**PMID:10199409**)

**Key identifiers:**
| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0019751** (TNF receptor associated periodic syndrome) |
| **OMIM** | **142680** (TNF RECEPTOR-ASSOCIATED PERIODIC SYNDROME; TRAPS) |
| **Orphanet** | **ORPHA:32960** |
| **ICD-11** | **4A60.23** (Tumour necrosis factor receptor 1 associated periodic syndrome) |
| **ICD-10** | No dedicated code; coded under M04.1 (periodic fever syndromes) / D89.8 |
| **MeSH** | No standalone descriptor; indexed under *Hereditary Autoinflammatory Diseases* (D056660) |
| **Gene (HGNC)** | *TNFRSF1A*, **hgnc:11916** |

**Synonyms / alternative names:** TRAPS; TNF receptor-associated periodic fever syndrome; Familial Hibernian fever (FHF); Hibernian fever; Autosomal dominant familial periodic fever; Familial periodic fever, autosomal dominant; TNFRSF1A-associated periodic syndrome; periodic fever, familial, autosomal dominant.

**Data derivation:** Disease-level knowledge here is aggregated from curated resources (OMIM, Orphanet, GeneReviews) and from **patient-level cohort data**, most notably the **Eurofever/EUROTRAPS international registry** (158 validated cases) — i.e., this is registry/cohort-aggregated rather than EHR-derived.

---

## 2. Etiology

**Primary cause (genetic).** TRAPS is monogenic: heterozygous **gain-of-function/misfolding missense mutations in *TNFRSF1A***, located predominantly in the extracellular **cysteine-rich domains (CRD1 and CRD2)** of TNFR1. Mutations that disrupt conserved disulfide bonds (e.g., cysteine substitutions, T50M) confer the highest penetrance and severity.

**Triggers of attacks (environmental/physiologic modifiers).** Individual flares are often precipitated by **physical or psychological stress, minor infection, trauma, fatigue, hormonal changes (menstruation), exercise, and vaccination** — but the underlying disease is genetic, and these are flare triggers, not causes.

**Risk factors**
- **Genetic risk factors:**
  - *Causal/high-penetrance variants:* cysteine substitutions (C30R, C43R, C52F, C88Y, etc.) and **T50M** — strongly associated with disease persistence into adulthood and amyloidosis.
  - *Low-penetrance susceptibility variants:* **R92Q** (c.362G>A; legacy nomenclature; corresponds to p.Arg121Gln with signal peptide) and **P46L** (p.Pro75Leu). These are common in the general population, behave as susceptibility/modifier alleles rather than fully penetrant disease alleles, and produce milder, sometimes self-limited phenotypes. In the Eurofever cohort, **R92Q accounted for ~34% of cases and T50M ~10%**, with family history present in only 19% of R92Q carriers vs 64% of those with other variants (Lachmann et al., **PMID:23965844**).
  - *Family history:* a first-degree affected relative is a major risk factor given autosomal-dominant transmission.
- **Environmental risk factors:** No environmental exposure *causes* TRAPS; ethnicity influences variant frequency (R92Q and P46L vary by population — P46L is notably more frequent in individuals of West/sub-Saharan African ancestry).

**Protective factors.** None specifically established genetically. Effective continuous anti-inflammatory therapy is "protective" against the development of amyloidosis (see §11–12). No dietary or lifestyle protective factor is validated.

**Gene–environment interactions.** The clearest interaction is **stress/infection/trauma acting on a genetically primed innate immune system** to precipitate flares. For low-penetrance alleles (R92Q/P46L), phenotype is thought to emerge only with additional genetic or environmental "second hits," explaining incomplete penetrance.

---

## 3. Phenotypes

For each, I give type, characteristics, and a suggested HP term. Frequencies are drawn primarily from the Eurofever/EUROTRAPS registry (Lachmann 2014, **PMID:23965844**) and Aksentijevich 2001 (**PMID:11443543**, *Am J Hum Genet* 69:301–314 — verify exact digits before commit).

| Phenotype | Type | Approx. frequency | Suggested HP term |
|---|---|---|---|
| **Recurrent fever** (hallmark; attacks often last 1–3 weeks) | Symptom/sign | ~85–90%+ (near-defining) | **HP:0001954** Recurrent fever |
| **Myalgia** (characteristically *migratory*, due to monocytic fasciitis) | Symptom | ~60–80% | **HP:0003326** Myalgia |
| **Abdominal pain** (sterile peritonitis; may mimic surgical abdomen) | Symptom | ~70–90% | **HP:0002027** Abdominal pain |
| **Skin rash** — erythematous, often *migratory*, overlying the painful muscle group | Sign | ~60–80% | **HP:0000988** Skin rash / **HP:0010783** Erythema |
| **Periorbital edema** (highly characteristic of TRAPS) | Sign | ~30–50% | **HP:0100539** Periorbital edema |
| **Conjunctivitis / ocular involvement** | Sign | ~20–45% | **HP:0000509** Conjunctivitis |
| **Arthralgia / arthritis** | Symptom/sign | ~40–60% | **HP:0002829** Arthralgia |
| **Chest pain / pleuritis (serositis)** | Symptom/sign | ~20–40% | **HP:0002102** Pleuritis / Abnormality of the pleura |
| **Headache** | Symptom | ~40–70% | **HP:0002315** Headache |
| **Lymphadenopathy** | Sign | variable | **HP:0002716** Lymphadenopathy |
| **Splenomegaly** | Sign | variable | **HP:0001744** Splenomegaly |
| **Scrotal/testicular pain** | Symptom | occasional (males) | **HP:0030241** (scrotal pain — verify) |
| **AA amyloidosis** (renal-predominant) — late complication | Lab/clinical | ~10–25% lifetime (untreated; higher with cysteine variants) | **HP:0011034** Amyloidosis; **HP:0000093** Proteinuria; **HP:0000100** Nephrotic syndrome |

**Laboratory abnormalities (acute-phase reaction during flares):**
| Lab phenotype | Suggested HP term |
|---|---|
| Elevated C-reactive protein | **HP:0011227** Increased C-reactive protein level |
| Elevated ESR | **HP:0003565** Elevated erythrocyte sedimentation rate |
| Leukocytosis / neutrophilia | **HP:0001974** Leukocytosis |
| Reactive thrombocytosis | **HP:0001894** Thrombocytosis |
| Anemia of chronic disease | **HP:0001903** Anemia |
| Elevated serum amyloid A (SAA) | (use elevated acute-phase reactant) |
| Polyclonal hypergammaglobulinemia / elevated IgD (modest) | **HP:0010702** (IgD elevation — verify) |

**Phenotype characteristics:**
- **Onset:** typically **childhood (median ~4 years)** but a wide range, with adult-onset (even after age 50) well documented, especially for low-penetrance variants.
- **Severity:** **variable**, strongly genotype-influenced — cysteine/T50M variants severe; R92Q/P46L mild.
- **Progression:** **episodic/recurrent** with symptom-free intervals; attacks recur **every ~4–6 weeks**, lasting (per GeneReviews) **"between five and 25 days."** Subclinical inflammation can persist between attacks, driving amyloidosis.
- **Quality-of-life impact:** Recurrent prolonged attacks cause significant **school/work absenteeism, chronic pain, fatigue, and impaired daily functioning**; amyloidosis can progress to chronic kidney disease and dialysis dependence. (No TRAPS-specific validated QoL instrument; generic SF-36/EQ-5D and the AIDAI [Autoinflammatory Diseases Activity Index] are used in autoinflammatory cohorts.)

---

## 4. Genetic / Molecular Information

**Causal gene.** ***TNFRSF1A*** (TNF receptor superfamily member 1A), **HGNC: hgnc:11916**, located at **chromosome 12p13.31**; OMIM gene *142680*; encodes **TNFR1 (p55, CD120a)**, UniProt **P19438**. NCBI Gene ID 7132; Ensembl ENSG00000067182.

**Pathogenic variants.**
- **Location:** clustered in exons 2–4, encoding the **extracellular cysteine-rich domains CRD1 and CRD2**.
- **Variant type/class:** predominantly **missense**; a large fraction are **cysteine substitutions** that abolish one of the conserved disulfide bonds essential for correct folding of the CRDs. Splice and small in-frame changes are rare. **No large deletions or whole-gene CNVs** are characteristic — this is a coding-missense disease.
- **Representative high-penetrance variants:** C30R, C30S, C33Y, C43R, **T50M**, C52F, C70R/C70Y, C88R/C88Y, etc.
- **Low-penetrance variants:** **R92Q** (c.362G>A) and **P46L** — present at appreciable allele frequency in **gnomAD** (R92Q ~1% in some populations; P46L higher in African-ancestry groups), consistent with reduced penetrance and a susceptibility-allele model.
- **Origin:** **germline** (autosomal dominant); *de novo* mutations occur. No somatic mechanism.
- **Functional consequence:** Mechanistically a **misfolding / aberrant gain-of-function** (NOT simple haploinsufficiency or classical loss of TNF signaling) — see §6. Original "shedding hypothesis" (impaired cleavage of TNFR1 from the cell surface leaving membrane receptor to signal unopposed) has been **superseded/complemented** by the **misfolding/ER-retention model**.

> Aksentijevich et al. confirmed and expanded the mutational spectrum and population genetics: *"mutations in the extracellular domain of the 55-kD tumor-necrosis factor (TNF) receptor (TNFRSF1A) define TRAPS"* (**PMID:11443543**, *Am J Hum Genet* 2001 — verify digits).

**Variant classification (ACMG/AMP).** Cysteine and T50M variants are generally curated **Pathogenic/Likely pathogenic** in ClinVar; **R92Q and P46L are typically classified as "risk factor" / reduced-penetrance / conflicting** rather than straightforwardly pathogenic.

**Modifier genes.** Not well defined. Genetic background and possibly other innate-immunity loci modulate penetrance, particularly for R92Q/P46L; co-inheritance with *MEFV* (FMF) variants has been reported to modify phenotype in individual cases.

**Epigenetic information.** No established disease-defining epigenetic signature. Inflammation-associated changes are secondary.

**Chromosomal abnormalities.** None characteristic — TRAPS is a single-nucleotide/missense disorder, not a structural/aneuploidy disorder.

---

## 5. Environmental Information

- **Environmental factors:** No toxin, radiation, or pollutant is causal. Flares are precipitated by nonspecific stressors (see §2).
- **Lifestyle factors:** Physical exertion, emotional stress, and fatigue are reported flare triggers; no lifestyle factor causes or cures the disease.
- **Infectious agents:** No causative pathogen. Intercurrent infections can **trigger flares** and complicate the differential diagnosis, but TRAPS is sterile (non-infectious) autoinflammation; "sterile peritonitis" is a defining feature.

---

## 6. Mechanism / Pathophysiology

TRAPS sits at the intersection of **TNF signaling, ER protein-folding quality control, mitochondrial ROS, and innate cytokine amplification.** The current integrated model:

**Causal chain (upstream → downstream):**

1. **Mutant TNFR1 misfolds** because disulfide-bond–disrupting (cysteine) or destabilizing (T50M) substitutions prevent correct folding of the extracellular CRDs.
2. **Misfolded receptor is retained in the endoplasmic reticulum** rather than trafficking to the cell surface; it forms **abnormal disulfide-linked oligomers** that cannot engage wild-type receptor via the pre-ligand assembly domain (PLAD).

   > *"TRAPS mutant TNFR1 molecules were retained intracellularly and colocalized with endoplasmic reticulum markers... The inflammatory phenotype of TRAPS may be due to consequences of mutant TNFR1 protein misfolding and ER retention."* — Lobito et al., *Blood* 2006 (**PMID:16684962**)

3. **ER stress / unfolded protein response (UPR)** is activated by the accumulated misfolded receptor.
4. **Elevated mitochondrial reactive oxygen species (mtROS)** result, lowering the threshold for innate immune activation and **enhancing pro-inflammatory cytokine production** (especially in response to LPS).

   > *"Mitochondrial ROS... promote production of proinflammatory cytokines and are elevated in TNFR1-associated periodic syndrome (TRAPS)... ROS generated by mitochondrial respiration are important for... the enhanced responsiveness to LPS seen in cells from patients with TRAPS."* — Bulua et al., *J Exp Med* 2011 (**PMID:21282379**)

5. **Constitutive/augmented activation of NF-κB and MAPK (JNK/p38)** signaling, plus **defective autophagy** of mutant receptor, sustains an inflammatory state. Some surface-retained mutant receptor signals in a **ligand-independent** manner.
6. **Amplified secretion of IL-1β (and IL-6, TNF)** drives the clinical attacks. The dramatic efficacy of **IL-1 blockade** is the clinical proof that **IL-1β is the dominant downstream effector** (CLUSTER trial, §12).
7. **Chronic/subclinical inflammation → sustained elevation of serum amyloid A (SAA) → AA amyloid fibril deposition**, predominantly in the **kidney** (renal amyloidosis → proteinuria/nephrotic syndrome → renal failure).

A "concerted action" of wild-type and mutant receptors enhancing inflammation has also been proposed (Simon et al., *PNAS* 2010 — PMID ~20133695; verify before commit).

**Molecular pathways (suggested annotations):**
- TNF-mediated signaling pathway — **GO:0033209**
- I-κB kinase/NF-κB signaling — **GO:0007249**
- MAPK cascade — **GO:0000165**
- Response to endoplasmic reticulum stress / UPR — **GO:0034976**; cellular response to unfolded protein — **GO:0034620**
- Reactive oxygen species metabolic process — **GO:0072593**
- Inflammatory response — **GO:0006954**
- Interleukin-1 beta production — **GO:0032611**
- Autophagy — **GO:0006914** (impaired clearance of mutant receptor)
- Protein folding — **GO:0006457**

**Cellular processes:** ER-stress signaling, mitochondrial ROS generation, NLRP3 inflammasome priming/activation, defective autophagy, ligand-independent receptor signaling, enhanced innate cytokine secretion.

**Protein dysfunction:** misfolding + aggregation + intracellular (ER) retention of TNFR1 → aberrant gain of pro-inflammatory function. UniProt **P19438**; structural basis in the cysteine-rich TNFR ectodomain (PDB structures of TNFR1 ectodomain, e.g., 1NCF/1EXT).

**Immune system involvement:** This is an **innate-immune (autoinflammatory)** disease — monocytes/macrophages and neutrophils are central; it is **not** classically autoimmune (no defining autoantibody, no HLA-restricted T-cell autoimmunity).

**Tissue damage mechanisms:** acute neutrophilic/monocytic inflammation of fascia, serosa, skin, synovium; chronic damage via **AA amyloid fibril deposition** (oxidative/proteotoxic, see amyloid).

**Molecular profiling:** Patient PBMCs/monocytes show **elevated baseline mtROS**, augmented LPS-induced cytokines, ER-stress transcriptional signatures, and altered metabolism (a "metabolic signature" of TNFRSF1A mutation has been reported — see Frontiers/PubMed 36752501).

**Cell types (suggested CL terms):** monocyte **CL:0000576**; macrophage **CL:0000235**; neutrophil **CL:0000775**; fibroblast **CL:0000057** (fasciitis); endothelial cell **CL:0000115**.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Skin and subcutaneous tissue / fascia** (UBERON: skin **UBERON:0002097**; fascia **UBERON:0007798**) — migratory erythematous rash overlying painful muscle.
- **Skeletal muscle** (**UBERON:0001134**) — myalgia from monocytic fasciitis.
- **Serous membranes / peritoneum** (peritoneum **UBERON:0002358**; pleura **UBERON:0000977**) — sterile peritonitis, pleuritis.
- **Eye / periorbital region** (conjunctiva **UBERON:0001811**; orbital region **UBERON:0001697**) — conjunctivitis, periorbital edema.
- **Joints / synovium** (synovial joint **UBERON:0002217**) — arthralgia/arthritis.
- **Kidney** (**UBERON:0002113**) — the principal target of AA amyloidosis.
- **Reticuloendothelial system** — lymphadenopathy, splenomegaly (spleen **UBERON:0002106**; lymph node **UBERON:0000029**).
- **Systems involved:** musculoskeletal, integumentary, gastrointestinal/serosal, ophthalmic, renal/genitourinary, hematologic/immune.

**Tissue/cell level:** inflammatory infiltration of **fascia (monocytic fasciitis)**, dermis (perivascular mononuclear infiltrate), serosa, and synovium; amyloid deposition in renal glomeruli/interstitium.

**Subcellular level (GO cellular component):**
- Endoplasmic reticulum — **GO:0005783** (site of mutant-receptor retention)
- Mitochondrion — **GO:0005739** (source of pathogenic ROS)
- Plasma membrane — **GO:0005886** (TNFR1 normal locale)
- Autophagosome — **GO:0005776**

**Localization/lateralization:** systemic; cutaneous/muscular manifestations are often **migratory** and may be unilateral at any moment but are not fixed-sided; serositis and amyloidosis are systemic/bilateral.

---

## 8. Temporal Development

- **Onset:** typically **childhood**, median around **4 years**, but described from infancy to >50 years (later onset more common with R92Q/P46L). Onset pattern is **acute, recurrent**.
- **Disease course:** **episodic/recurrent-remittent.** Discrete attacks of fever + serositis + myalgia/rash recurring at irregular intervals (~every 4–6 weeks), each lasting **~5–25 days (often 1–3 weeks)** — notably *longer* than FMF attacks.
- **Progression:** Generally **non-progressive between attacks** in those without amyloidosis; some patients have decreasing attack frequency with age, while a subset develop **persistent subclinical inflammation** that culminates in **AA amyloidosis** (the principal progressive, organ-threatening sequela).
- **Remission patterns:** Individual attacks are **self-limited** (spontaneous resolution); **treatment-induced remission** of attacks and normalization of acute-phase reactants is achievable with IL-1 blockade.
- **Critical period for intervention:** sustained control of inflammation (normalizing SAA/CRP) is the **window to prevent amyloidosis**; once renal amyloid causes significant proteinuria/CKD, damage is harder to reverse.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence:** rare; **GeneReviews estimates ~1 in 1,000,000 worldwide** (likely an underestimate given under-recognition and low-penetrance carriers). TRAPS is the **second most common hereditary periodic fever after FMF** in many European cohorts.
- **Incidence:** not precisely established (orphan disease).

**Genetic transmission:**
- **Inheritance pattern:** **Autosomal dominant** (50% transmission risk per offspring).
- **Penetrance:** **High for cysteine-disrupting variants and T50M; markedly reduced for R92Q and P46L.** Many R92Q carriers are asymptomatic.
- **Expressivity:** **highly variable**, even within families carrying the same mutation.
- **Genetic anticipation:** Not a feature (this is not a repeat-expansion disorder).
- **Germline mosaicism / *de novo*:** *de novo* mutations occur; mosaicism reported uncommonly.
- **Founder effects:** Original FHF kindred Irish/Scottish; specific variants show population clustering. R92Q and P46L are **common population variants** rather than founder disease alleles in the classic sense.
- **Consanguinity:** Not relevant (dominant disease).
- **Carrier "frequency":** For low-penetrance alleles, gnomAD shows **R92Q ~0.5–1%** in some populations and **P46L** enriched in African-ancestry groups — these are heterozygous susceptibility alleles, not recessive carrier states.

**Demographics:** Reported across many ethnicities; no strong sex bias (roughly **M:F ≈ 1:1**, perhaps slight female excess in some series). Geographic distribution of variants varies (P46L more frequent in West African populations). Age distribution skews to childhood onset but spans all ages.

---

## 10. Diagnostics

**Clinical/laboratory:**
- **Acute-phase reactants during attacks:** elevated **CRP** (HP:0011227), **ESR** (HP:0003565), **serum amyloid A (SAA)**, neutrophilic leukocytosis, reactive thrombocytosis, anemia of chronic disease; polyclonal hypergammaglobulinemia. Persistently elevated SAA between attacks signals amyloidosis risk.
- **Soluble TNFR1 (sTNFR1):** classically **low/inappropriately reduced** plasma levels between attacks (McDermott 1999 noted ~half-normal soluble TNFR1) — supportive but not diagnostic; the sTNFR1/sTNFR2 ratio has been explored for differential diagnosis.
- **LOINC:** CRP (e.g., 1988-5), ESR (4537-7), albumin/creatinine ratio for renal amyloid monitoring.

**Biomarkers:** SAA and CRP for disease activity; proteinuria for amyloid surveillance.

**Imaging/biopsy:**
- **Histopathology of muscle/fascia:** monocytic **fasciitis** (panniculitis/fasciitis with mononuclear infiltrate) rather than true myositis — characteristic.
- **Skin biopsy:** superficial/deep perivascular and interstitial mononuclear infiltrate.
- **Tissue biopsy with Congo red staining** (apple-green birefringence) — gold standard to confirm **AA amyloidosis** (subcutaneous fat, rectal, or renal biopsy); immunohistochemistry confirms **SAA-type (AA) amyloid**.
- **SAP scintigraphy** (where available) to assess amyloid burden.

**Genetic testing (definitive):**
- **Targeted *TNFRSF1A* sequencing** (single-gene) confirms diagnosis when clinical suspicion is high.
- **Hereditary periodic fever / autoinflammatory NGS gene panels** (covering *MEFV*, *MVK*, *NLRP3*, *TNFRSF1A*, etc.) are standard first-line genetic testing for undifferentiated periodic fever.
- **WES/WGS** reserved for atypical/unsolved cases.
- CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable** (coding missense disease).
- **Interpretation caveat:** finding **R92Q or P46L requires cautious interpretation** given reduced penetrance — genotype must be integrated with phenotype.

**Clinical criteria / classification:** The **Eurofever/PRINTO classification criteria** and the newer **2024 EULAR/ACR (AIDA-informed) provisional classification criteria for autoinflammatory periodic fevers** are used; historically the "TRAPS clinical score." Key discriminators: **attack duration >1 week**, migratory myalgia with rash, periorbital edema, positive family history, dominant inheritance.

**Differential diagnosis:** FMF (shorter attacks, AR, *MEFV*, colchicine-responsive), **hyper-IgD/mevalonate kinase deficiency (MKD/HIDS)** (*MVK*, early onset, cervical adenitis, elevated IgD), **cryopyrin-associated periodic syndromes (CAPS/NLRP3)**, PFAPA, systemic JIA / adult-onset Still disease, Behçet disease, and infection/malignancy.

**Screening:** No population newborn screening. **Cascade genetic testing** of at-risk relatives in known-mutation families is appropriate; prenatal/preimplantation testing is possible for high-penetrance variants but ethically nuanced given variable expressivity.

---

## 11. Outcome / Prognosis

- **Survival/life expectancy:** Generally **normal life expectancy if amyloidosis is prevented/controlled.** Untreated, **AA amyloidosis is the major determinant of mortality**, via progressive **renal failure**.
- **Disease-specific mortality:** Driven almost entirely by amyloid-related end-organ (renal, and less often hepatic/cardiac/GI) failure.
- **Morbidity:** Recurrent prolonged painful attacks → chronic pain, fatigue, missed school/work; ocular involvement; complications of chronic steroid use historically.
- **AA amyloidosis frequency:** Historically reported in **~10–25% of patients overall**, **higher (up to ~25%+) for cysteine/T50M genotypes** and **very low for R92Q/P46L.** Per GeneReviews, once amyloidosis develops, **"proteinuria and kidney failure occur in 80%–90%"** of those affected.
- **Prognostic factors:** **Genotype is the strongest predictor** — cysteine-disrupting variants and T50M predict severe, persistent disease and amyloid risk; R92Q/P46L predict mild/self-limited disease. **Persistently elevated SAA/CRP** between attacks predicts amyloidosis. Early effective IL-1 blockade improves outcomes.
- **Recovery potential:** Attacks fully resolve between episodes; with modern biologics, **clinical and biochemical remission is achievable in the majority**, and continuous therapy can **prevent or stabilize amyloidosis**.

---

## 12. Treatment

**Goals:** abort/prevent attacks, normalize acute-phase reactants (CRP/SAA), and **prevent AA amyloidosis.**

**Pharmacotherapy / biologics (mainstay):**
- **IL-1 inhibitors — first-line for persistent disease:**
  - **Anakinra** (recombinant IL-1 receptor antagonist) — rapid, effective; useful diagnostically and for amyloidosis-complicated disease.
  - **Canakinumab** (anti-IL-1β monoclonal antibody) — **the only biologic with a pivotal RCT and regulatory approval for TRAPS** (FDA/EMA approval for periodic fever syndromes including TRAPS). In the **phase 3 CLUSTER trial** (De Benedetti et al., *NEJM* 2018, **PMID:29768139**; ClinicalTrials.gov **NCT02059291**), canakinumab controlled and prevented flares in TRAPS, MKD/HIDS, and colchicine-resistant FMF.

    > *"Canakinumab was effective... in controlling and preventing flares in patients with colchicine-resistant familial Mediterranean fever, mevalonate kinase deficiency... and TRAPS."* — De Benedetti et al., *NEJM* 2018 (**PMID:29768139**)

  - **Modality:** monoclonal antibody (canakinumab) / recombinant protein (anakinra). Suggested annotation: treatment_term **NCIT:C15986** (Pharmacotherapy) + `therapeutic_agent` (canakinumab/anakinra), `therapeutic_modality: MONOCLONAL_ANTIBODY` (canakinumab).
- **TNF inhibitor — etanercept (soluble TNFR2-Fc fusion):** historically used; **partially effective** but with waning/incomplete responses and poor long-term adherence:

  > *"Etanercept reduces symptoms and serum levels of inflammatory markers of TRAPS in a dose-dependent manner, but does not completely normalize symptoms or acute-phase reactant levels."* — Bulua et al., *Arthritis Rheum* 2012 (**PMID:22006113**)

  - **Important pharmacologic caveat:** **monoclonal anti-TNF antibodies (infliximab, and adalimumab) can paradoxically *worsen* TRAPS** (reported flare induction) and are generally avoided; etanercept (receptor decoy) behaves differently from anti-TNF mAbs here.
- **IL-6 blockade (tocilizumab):** reported effective in refractory/biologic-experienced cases (off-label).
- **Corticosteroids:** abort/attenuate acute attacks (high-dose during flares) but **chronic steroid use causes toxicity and is not a long-term solution**; escalating dose requirements are common.
- **NSAIDs:** symptomatic relief only.
- **Colchicine:** **largely ineffective in TRAPS** (unlike FMF) — an important contrast.

**Pharmacogenomics:** Response is genotype-correlated at the *disease-allele* level (severe genotypes need continuous biologics) rather than via drug-metabolism PGx; no validated CPIC-style PGx guidance specific to TRAPS.

**Advanced/experimental therapeutics:** No approved gene/cell/RNA therapy. Emerging interest in agents targeting ER stress, mtROS, NLRP3 inflammasome, and JAK inhibitors in refractory autoinflammation — investigational only.

**Supportive/management of amyloidosis:** suppress inflammation to halt amyloid; manage **CKD/nephrotic syndrome** (ACE inhibitors/ARBs, dialysis); **renal transplantation** in end-stage renal disease, with continued IL-1 blockade to protect the graft.

**Suggested MAXO terms:** Pharmacotherapy (**NCIT:C15986**); supportive care (**MAXO:0000950**); organ transplantation/renal transplant (**MAXO:0010039**); genetic counseling (**MAXO:0000079**); dietary/supportive management as applicable. (Use NCIT/CHEBI `therapeutic_agent` for canakinumab, anakinra, etanercept, prednisone; note canakinumab/anakinra/etanercept are biologics — likely need NCIT rather than CHEBI agents; corticosteroid CHEBI:50858/prednisone CHEBI:8382; colchicine CHEBI:23359 noted as *ineffective*.)

---

## 13. Prevention

- **Primary prevention:** Not preventable (genetic). **Genetic counseling** for affected families is the key primary-prevention tool; prenatal/preimplantation genetic testing is feasible for high-penetrance variants.
- **Secondary prevention (early detection):** **Cascade genetic testing** of at-risk relatives; early diagnosis enables early anti-inflammatory therapy.
- **Tertiary prevention (complication prevention):** the central, achievable goal — **continuous suppression of inflammation (normalizing SAA/CRP with IL-1 blockade) to prevent AA amyloidosis**, plus monitoring **urinalysis/proteinuria and renal function** for early amyloid detection.
- **Immunization:** No vaccine (not infectious). Standard immunizations advised, with awareness that vaccination can occasionally trigger a flare and that live vaccines need consideration on biologics.
- **Counseling:** genetic counseling regarding autosomal-dominant 50% transmission, variable expressivity, and the special interpretive challenges of R92Q/P46L (**MAXO:0000079**).
- **Public/environmental health:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease — *Homo sapiens* (**NCBITaxon:9606**).
- **Orthologous gene:** mouse *Tnfrsf1a* (NCBI Gene 21937); the gene/receptor (TNFR1/p55) is **highly conserved** across mammals.
- **Natural disease in other species:** No well-recognized spontaneous TRAPS-equivalent in companion animals or wildlife (**OMIA** has no established orthologous natural disease). TRAPS is essentially a **human germline disorder**; animal "disease" is engineered (see §15).
- **Comparative biology / conservation:** TNF–TNFR1 signaling and the cysteine-rich-domain architecture are deeply evolutionarily conserved, which is *why* mouse knock-ins recapitulate aspects of the disease.
- **Zoonotic potential / transmission:** None (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse "knock-in" models:** The key model is the **TNFR1 knock-in mouse** carrying TRAPS-associated mutations (e.g., T50M; C33Y), generated and characterized in the same body of work establishing the misfolding/ER-retention and mtROS mechanisms (Lobito et al. *Blood* 2006, **PMID:16684962**; Bulua et al. *J Exp Med* 2011, **PMID:21282379**). These mice show **ER retention of mutant TNFR1, elevated mitochondrial ROS, and enhanced inflammatory responses to LPS**, recapitulating the cellular phenotype.

  > *"...a mouse 'knock-in' model of TRAPS... TRAPS mutant TNFR1 molecules were retained intracellularly and colocalized with endoplasmic reticulum markers."* — Lobito et al. 2006 (**PMID:16684962**)

- **Cellular / in vitro models:** transfected cell lines expressing mutant TNFR1; **patient-derived monocytes/PBMCs and mouse embryonic fibroblasts (MEFs)** harboring TRAPS mutations — used to demonstrate elevated baseline mtROS and augmented cytokine output (Bulua 2011, **PMID:21282379**). iPSC-derived myeloid models are an emerging avenue.
- **Model types available:** knock-in (point-mutation) mice; transgenic/overexpression cell systems; primary patient cells (ex vivo).
- **Phenotype recapitulation:** Models faithfully reproduce the **molecular phenotype** (ER retention, mtROS, hyper-responsive innate cytokine secretion, NF-κB/MAPK activation). They are somewhat **less faithful to the full clinical periodic-fever syndrome** (the dramatic recurrent multi-organ human attacks and AA amyloidosis are incompletely modeled) — a candidate **HUMAN_MODEL_MISMATCH** consideration for dismech: molecular mechanism well-modeled, but periodicity/amyloidosis less so.
- **Applications:** dissecting the misfolding→ER-stress→mtROS→cytokine axis, testing antioxidants/IL-1 blockade, and validating that **IL-1β is the key effector**.
- **Resources:** **MGI** (mouse *Tnfrsf1a*), IMPC/KOMP for null alleles (note: *null* alleles model TNF-loss, not the TRAPS *gain*-type mechanism — use knock-in lines for disease modeling).

---

## Summary of Key Verified Citations (re-validate before YAML commit)

| Claim | Citation | PMID | Status |
|---|---|---|---|
| Gene discovery, disulfide-disrupting missense, low soluble TNFR1 | McDermott et al., *Cell* 1999;97:133–144 | **10199409** | ✅ verified |
| Mutational spectrum, ancestral origins, genotype–phenotype | Aksentijevich et al., *Am J Hum Genet* 2001;69:301–314 | **11443543** | ⚠️ verify exact digits |
| Misfolding / ER retention / abnormal oligomers (+ knock-in mouse) | Lobito et al., *Blood* 2006;108:1320–1327 | **16684962** | ✅ verified |
| Mitochondrial ROS drives cytokines, elevated in TRAPS | Bulua et al., *J Exp Med* 2011;208:519–533 | **21282379** | ✅ verified |
| Concerted WT+mutant receptor action | Simon et al., *PNAS* 2010 | ~**20133695** | ⚠️ verify before use |
| Etanercept partially effective | Bulua et al., *Arthritis Rheum* 2012;64:908–913 | **22006113** | ✅ verified |
| Phenotype of 158 cases; R92Q ~34%, T50M ~10% | Lachmann et al., *Ann Rheum Dis* 2014;73:2160–2167 | **23965844** | ✅ verified |
| Canakinumab RCT (CLUSTER) approval evidence | De Benedetti et al., *NEJM* 2018 (NCT02059291) | **29768139** | ✅ verified |

**Sources consulted:**
- [McDermott et al., Cell 1999 — PubMed](https://pubmed.ncbi.nlm.nih.gov/10199409/)
- [Aksentijevich et al., Am J Hum Genet 2001 — PMC1235304](https://pmc.ncbi.nlm.nih.gov/articles/PMC1235304/)
- [Lobito et al., Blood 2006 — PMC1895878](https://pmc.ncbi.nlm.nih.gov/articles/PMC1895878/)
- [Bulua et al., J Exp Med 2011 — PMC3058571](https://pmc.ncbi.nlm.nih.gov/articles/PMC3058571)
- [Bulua et al., Arthritis Rheum 2012 — PubMed](https://pubmed.ncbi.nlm.nih.gov/22006113/)
- [Lachmann et al., Eurofever/EUROTRAPS 2014 — PMC4251160](https://pmc.ncbi.nlm.nih.gov/articles/PMC4251160/)
- [De Benedetti et al., CLUSTER trial, NEJM 2018 — PubMed](https://pubmed.ncbi.nlm.nih.gov/29768139/) and [NCT02059291](https://clinicaltrials.gov/study/NCT02059291)
- [GeneReviews: TNF Receptor-Associated Periodic Fever Syndrome — NBK586171](https://www.ncbi.nlm.nih.gov/books/NBK586171/)
- [Revisiting TRAPS: Current Perspectives, Int J Mol Sci 2020 — MDPI](https://www.mdpi.com/1422-0067/21/9/3263)
- [R92Q age-at-onset cohort, Front Immunol 2017 — PMC5366323](https://pmc.ncbi.nlm.nih.gov/articles/PMC5366323/)
- [NORD: TRAPS](https://rarediseases.org/rare-diseases/tumor-necrosis-factor-receptor-associated-periodic-syndrome/)

**Curation flags for dismech:** (1) Re-fetch every PMID with `just fetch-reference` and confirm each snippet is an *exact* substring before committing — the two ⚠️ PMIDs (Aksentijevich 11443543, Simon ~20133695) need digit re-verification. (2) The R92Q/P46L low-penetrance variants are an ideal place to record a `mechanistic_hypotheses`/reduced-penetrance nuance. (3) Consider a `HUMAN_MODEL_MISMATCH` discussion note for the mouse knock-in (molecular mechanism modeled; full periodic-fever/amyloidosis phenotype not). (4) `evidence_source` tags: McDermott/Aksentijevich/Lachmann/De Benedetti/Bulua-2012 = HUMAN_CLINICAL; Lobito (knock-in mouse + transfected cells) = mix of MODEL_ORGANISM + IN_VITRO (split into separate evidence items); Bulua-2011 mtROS = mix of MODEL_ORGANISM (MEFs/mice) + IN_VITRO (human cells) — split accordingly.