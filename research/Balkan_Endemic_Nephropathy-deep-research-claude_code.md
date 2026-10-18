---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T13:58:30.150166'
end_time: '2026-09-01T14:14:17.198489'
duration_seconds: 947.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Balkan Endemic Nephropathy
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 20
  num_turns: 47
  total_cost_usd: 5.477729500000001
  session_id: c7d897e5-ee1b-4b72-bda4-6130eded0f87
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Balkan Endemic Nephropathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Balkan Endemic Nephropathy** covering all of the
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

sup Harry — Balkan Endemic Nephropathy turned out to be one of the tidiest detective stories in environmental nephrology, so this report got long. Everything below is sourced, and I've flagged which ontology IDs I actually resolved against OLS in this session vs. which are from memory and still need a `just validate-terms` pass.

---

# Balkan Endemic Nephropathy — Comprehensive Research Report

**Prepared:** 2026-09-01 · **Target:** `MONDO:0007416` · **Category:** Complex (environmental toxin + host susceptibility)

---

## 0. Orientation — the one-paragraph version

Balkan Endemic Nephropathy (BEN) is a slow, quiet, scarring kidney disease that ate its way through specific farming villages along the Danube tributaries for most of the 20th century. It looks like a genetic disease from a distance — it clusters in families — but it clusters in *households*, not bloodlines, which is the tell. The cause is aristolochic acid (AA), a phytotoxin from the birthwort *Aristolochia clematitis*, a weed that grew in the wheat and whose seeds went into the flour and then into home-baked bread. Think of it as a very slow, very patient poisoning administered one loaf at a time over decades. The toxin's activated metabolite sticks to DNA at adenine, sits there essentially uncleaned by repair machinery, and eventually writes a fingerprint mutation (A:T→T:A) into TP53 and the rest of the genome — which is why the same villages that got kidney failure also got a bewildering excess of urinary-tract cancer. Modern agriculture accidentally cured it: bigger mills and better sieves in the 1970s stopped separating badly, and the disease is now fading.

---

## 1. Disease Information

### 1.1 Overview

BEN is a **chronic tubulointerstitial nephropathy** with insidious onset, near-invariable progression to end-stage renal disease (ESRD), and a strong association with **upper tract urothelial carcinoma (UTUC)** of the renal pelvis and ureter.

> "Balkan endemic nephropathy is a chronic tubulointerstitial disease with insidious onset, slowly progressing to end-stage renal disease and frequently associated with urothelial carcinoma of the upper urinary tract (UTUC). It was described in South-East Europe at the Balkan peninsula in rural areas around tributaries of the Danube River."
> — Jelaković et al., *Semin Nephrol* 2019 (**PMID:31054628**)

> "Endemic (Balkan) nephropathy (EN), a devastating renal disease affecting men and women living in rural areas of Bosnia, Bulgaria, Croatia, Romania, and Serbia, is characterized by its insidious onset, invariable progression to chronic renal failure and a strong association with transitional cell (urothelial) carcinoma of the upper urinary tract."
> — Grollman et al., *PNAS* 2007 (**PMID:17620607**)

### 1.2 Key identifiers

Resolved against MONDO via OLS4 this session:

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0007416` — "Balkan nephropathy" |
| OMIM | 124100 — DANUBIAN ENDEMIC FAMILIAL NEPHROPATHY |
| ICD-10-CM | N15.0 |
| ICD-9 | 583.89 |
| ICD-11 (foundation) | 18497836 |
| MeSH | D001449 |
| UMLS | C0004698 |
| NCIT | `NCIT:C123025` |
| DOID | DOID:3052 |
| SNOMED CT | 26121002 |
| MedGen | 495 |
| EFO | EFO:0007164 |
| GARD | 0008576 |

**MONDO definition (verbatim):** "A chronic tubulointerstitial nephropathy that affects people in certain rural areas along the Danube river in the Balkans. It leads to end-stage renal disease."

**Not found:** no Orphanet cross-reference appears in the MONDO record. BEN is an environmental disease of defined geography rather than a rare Mendelian disorder, which likely explains the absence — but treat this as "not confirmed" rather than "confirmed absent."

**Watch-out on OMIM 124100.** That entry frames BEN as a familial/Mendelian condition and preserves several claims that are now **superseded**: it repeats the Pliocene-lignite/polycyclic-aromatic-hydrocarbon hypothesis and states that "the histologic end stage of the kidney lesion is thought to be a form of primary amyloidosis." Neither reflects current understanding. Cite OMIM for the identifier and the historical framing; do **not** cite it for mechanism.

### 1.3 Synonyms (from MONDO)

Balkan endemic nephropathy · endemic nephropathy · Danubian endemic familial nephropathy (DEFN) · Chinese herb endemic nephropathy · aristolochic acid nephropathy (AAN) · BEN

⚠️ **Curation decision flagged:** MONDO lists "aristolochic acid nephropathy" and "Chinese herb endemic nephropathy" as synonyms of BEN. This reflects De Broe's 2012 argument (**PMID:22373701**, *"Chinese herbs nephropathy and Balkan endemic nephropathy: toward a single entity, aristolochic acid nephropathy"*) that they are one disease. They share etiology, pathology, and cancer risk — **but not clinical course**. See §1.4. If dismech models BEN as an entry, the AAN-vs-BEN relationship is a real lump/split call, and the honest answer is probably: BEN is the *environmental, low-dose, chronic* presentation of AAN, and iatrogenic/herbal AAN is the *high-dose, rapid* presentation. A `Grouping` over both, or `has_subtypes`, would capture it better than treating them as one flat concept.

### 1.4 BEN vs. iatrogenic AAN — the contrast table

Reproduced from Table 1 of Jelaković et al. 2019 (**PMID:31054628**):

| Feature | BEN | Iatrogenic AAN |
|---|---|---|
| Prevalence in exposed population | 2–5% | 3–5% |
| Sex | No difference | More women (cohort artifact — Belgian slimming clinic) |
| Familial/household aggregation | **Yes** | No |
| Awareness of plant toxicity | Unaware | Inadvertent |
| Route of ingestion | **Home-baked bread** | Herbal remedies |
| Pathology | Identical | Identical |
| Incidence of UTUC | 30–50% | 44% |
| Clinical course | **Insidious onset, slow progression** | **Rapidly progressive to ESRD; Fanconi syndrome** |

The course difference is dose-driven: Balkan exposure was micrograms over decades; Belgian exposure was a large cumulative dose over months.

### 1.5 Information provenance

Information here is **aggregated disease-level** — epidemiologic field surveys, autopsy and nephrectomy series, molecular-epidemiologic cohorts, and consensus statements. It is **not** EHR-derived. Two data types are genuinely individual-patient-level and are the ones that carry the causal argument: (a) `32P`-postlabeling / LC-MS/MS aristolactam-DNA adduct measurements in renal cortex, and (b) TP53 / whole-exome / whole-genome sequencing of tumors.

---

## 2. Etiology

### 2.1 Primary causal factor — aristolochic acid

**Chronic, low-dose dietary ingestion of aristolochic acid** from *Aristolochia clematitis* (birthwort), a weed that grows amid wheat in the Danube floodplain. Its seeds are comparable in size to wheat grain and were carried through village milling into flour, and then into home-baked bread.

The hypothesis is old — Ivić proposed it in 1969 — and sat ignored for ~35 years until the Belgian "Chinese herb nephropathy" outbreak made the pathology look familiar:

> "In 1969, Ivic had suggested that the latter, occurring in certain villages throughout the Danube Valley, might be caused by the chronic ingestion of the seeds of the Aristolochia clematitis, a common plant growing in the wheat fields of these endemic regions." (**PMID:31054628**)

The chemistry: AA is a mixture of nitrophenanthrene carboxylic acids, dominated by **aristolochic acid I (AAI)** and **aristolochic acid II (AAII)**. Both are mutagenic and genotoxic; **AAI is considered the nephrotoxic actor** (**PMID:31054628**).

**IARC classification:** herbal remedies containing *Aristolochia* species, and aristolochic acids themselves, are **Group 1 (carcinogenic to humans)**, acting by a genotoxic mechanism (**PMID:31054628**; IARC Monographs).

### 2.2 The causal evidence chain (five independent lines)

1. **Botanical/agricultural** — *A. clematitis* seeds co-mingle with harvested wheat in endemic Croatian and Serbian villages (Hranjec et al. 2005, cited in **PMID:31054628**).
2. **Analytical chemistry** — AA is quantifiable in corn, wheat grain, and soil from the endemic Serbian village of Kutleš (Chan et al., *J Agric Food Chem* 2016, **PMID:27362729**), establishing crop uptake from contaminated soil as a second exposure pathway beyond seed co-mingling.
3. **Molecular dosimetry** — aristolactam-DNA adducts in renal cortex of BEN patients and not in other CKD (**PMID:17620607**).
4. **Mutational fingerprint** — the AA-specific A:T→T:A transversion in TP53 and genome-wide (**PMID:17620607**, **PMID:22071594**, **PMID:23926199**).
5. **Natural experiments in migration** — Ukrainians who settled Croatian endemic villages acquired local BEN risk after >20 years; those who settled non-endemic villages did not; BEN has never been reported in Ukraine (Čeović 1985, in **PMID:31054628**). This kills inheritance as the primary driver.

### 2.3 Environmental risk factors

| Factor | Evidence | Notes |
|---|---|---|
| **Residence in an endemic village >20 years** | Core diagnostic criterion (**PMID:24166461**) | Duration matters — BEN has *never* been reported in children |
| **Farming occupation** | Disease "observed only in harvesting farmers" (**PMID:31054628**) | |
| **Home bread-baking from locally milled wheat** | Confirmed risk factor for BEN and UTUC (**PMID:31054628**) | The dominant route |
| **Small-village milling with coarse sieves (pre-1970s)** | Agronomic analysis, Croatia (**PMID:31054628**) | The actual proximate determinant of dose |
| **Consumption of crops grown in AA-contaminated soil** | AA quantified in corn/wheat/soil (**PMID:27362729**) | Secondary/ongoing route |
| **Cumulative AA dose** | In iatrogenic AAN, >200 g cumulative *Aristolochia* raised UTUC risk (**PMID:10841870**) | Dose-response supports causation |

**Explicitly NOT a risk factor:** herbal teas / herbal medicine use in the Balkan setting. A cohort of >2,500 Croatian farmers rejected this (Ivković et al. 2014, cited in **PMID:31054628**). Worth curating as a **REFUTE** evidence item — it's a real negative result that distinguishes Balkan from Asian AAN.

### 2.4 Genetic risk factors

There is **no causal Mendelian gene**. What exists is candidate susceptibility, and it is thin:

| Gene / locus | Finding | Source |
|---|---|---|
| **GPX3** rs8177412 | Variant TC+CC genotype carriers at **~8-fold** increased risk of BEN-associated urothelial tumors. "Carriers of variant GPX3\*TC + CC genotype were at eight-fold increased risk of BEN-associated urothelial tumors development." | **PMID:37629712** (2023) |
| **MDR1/ABCB1** rs1045642 + GPX3 combined | Female patients carrying both variants: OR 3.34–3.79 for BEN | **PMID:37629712** |
| **CELA1, HSPG2, KCNK5** | Nominated by exome sequencing of 22 Bulgarian + Serbian patients; proteins in basement membrane/ECM and vascular tone → "abnormal process of angiogenesis plays a key role" | **PMID:24949484** (2014) |
| **3q25–3q26** | Chromosomal aberrations in BEN patients and some healthy relatives; proposed BEN marker | **PMID:8730422** (1996) — old, low-resolution, **treat as historical** |
| AA-metabolizing enzyme polymorphisms (NQO1, CYP1A1/1A2, POR, COX, CYP2D6) | Biologically compelling; empirically unresolved | **PMID:31054628** |

Be honest about the state of this literature. The 2019 review is blunt:

> "However, studies evaluating genetic polymorphisms of AA-metabolising enzymes have only resulted in controversial results ... and thus this phenomenon remains to be further investigated." (**PMID:31054628**)

There is **no published GWAS** of BEN meeting modern standards that I could locate. The candidate-gene studies are small (n ≈ 200–350) and unreplicated. Curate them as `SUSCEPTIBILITY`, never `CAUSATIVE`.

### 2.5 Protective factors

- **Modern milling and combine harvesting** (post-1970s): larger central mills and finer sieves separate the larger *Aristolochia* seeds from wheat. This is the *actual* population-level protective intervention, and it happened by accident. (**PMID:31054628**)
- **Immigrant status in the post-improvement era**: Bosnians who settled Croatian endemic villages *after* the agricultural improvements showed immigrant status as a **protective predictor** for proximal tubule damage — the exact inverse of the 1950s Ukrainian result. This is a beautiful natural experiment and the single strongest argument that agricultural practice, not soil or geology, sets the dose. (**PMID:31054628**)
- **Avoiding AA-containing herbal preparations** — regulatory bans (FDA 2001 and equivalents).
- **Genetic protective alleles:** none established. Wild-type GPX3/MDR1 by implication only.

### 2.6 Gene–environment interaction

This is the mechanistic core of the disease and belongs in the KB as an explicit GxE claim:

> "Thus, in genetically susceptible individuals, dietary exposure to aristolochic acid is causally related to endemic nephropathy and carcinomas of the upper urinary tract." — **PMID:22071594**

Only 2–5% of exposed villagers develop BEN, while ~10–15% of farmers are "suspected." The proposed interaction axes:
1. **Bioactivation vs. detoxification balance** — NQO1/POR/CYP1A1/1A2/COX (activating) vs. CYP-mediated O-demethylation to AAIa (detoxifying). "Differences in AA metabolism (activation versus detoxification) might not only contribute to an individual's susceptibility but could also be an important determinant of cancer risk." (**PMID:31054628**)
2. **Antioxidant capacity** — GPX3, Nrf2, KEAP1, GSTP1, SOD2, GPX1 (**PMID:37629712**).
3. **Efflux transport** — MDR1/ABCB1.
4. **DNA repair capacity** — dA-AAI adducts are poorly excised by nucleotide-excision repair.
5. **Clinical-course modification** — "different clinical courses do not seem to be related to differences in exposure, but more likely to differences in metabolic activation or detoxification of AA and/or DNA repair resulting from different genetic polymorphisms." (**PMID:31054628**)

---

## 3. Phenotypes

BEN is phenotypically *quiet*. That is its defining clinical feature and its public-health problem — patients present late because there is nothing to present with.

> "There is no leading typical symptom (fatigue, loss of appetite, nocturia, polyuria)." (**PMID:31054628**)

### 3.1 Phenotype table with suggested HP terms

All HP IDs below were **resolved against OLS4 (hp) in this session** unless marked otherwise.

| Phenotype | HP term | Type | Onset | Frequency | Severity / course |
|---|---|---|---|---|---|
| Low-molecular-weight (tubular) proteinuria | `HP:0003126` Low-molecular-weight proteinuria | Lab | Earliest detectable | Very frequent — the **hallmark** | Progressive; the screening marker |
| Chronic kidney disease | `HP:0012622` Chronic kidney disease | Clinical | 5th decade | Obligate (definitional) | Slowly progressive |
| Decreased glomerular filtration rate | `HP:0012213` Decreased glomerular filtration rate | Lab | 5th decade | Very frequent | Progressive |
| Stage 5 chronic kidney disease | `HP:0003774` Stage 5 chronic kidney disease | Clinical | 6th–7th decade | Frequent (near-invariable if untreated) | Terminal |
| Tubulointerstitial nephritis | `HP:0001970` Tubulointerstitial nephritis | Histopath | Subclinical | Obligate | Chronic |
| Tubulointerstitial fibrosis | `HP:0005576` Tubulointerstitial fibrosis | Histopath | Subclinical | Obligate — "extensive hypocellular interstitial fibrosis" | Progressive |
| Renal tubular atrophy | `HP:0000092` Renal tubular atrophy | Histopath | Subclinical | Obligate | Progressive, outer→inner cortical gradient |
| Renal interstitial fibrosis | `HP:0032948` Renal interstitial fibrosis | Histopath | Subclinical | Obligate | — |
| Renal cortical atrophy | `HP:0002048` Renal cortical atrophy | Imaging | Mid/late | Frequent | Kidneys 20–30 g each, smooth outlines at end-stage |
| Anemia | `HP:0001903` Anemia | Lab | Mid | Frequent, **disproportionate to CKD stage** | Progressive |
| Transitional cell carcinoma (upper tract) | `HP:0030409` Renal transitional cell carcinoma | Neoplasm | Late (6th–7th decade) | **30–50%** | Often bilateral; the leading cause of death |
| Transitional cell carcinoma of bladder | `HP:0006740` Transitional cell carcinoma of the bladder | Neoplasm | Very late, often post-nephroureterectomy | Uncommon in BEN; documented in Belgian AAN | — |
| Hematuria | `HP:0000790` Hematuria | Sign | Late | Frequent with UTUC | Episodic |
| Hyposthenuria | `HP:0003158` Hyposthenuria | Lab | Early | Frequent — "urine specific gravidity is low" | — |
| Polyuria | `HP:0000103` Polyuria | Symptom | Early–mid | Occasional | — |
| Nocturia | `HP:0000017` Nocturia | Symptom | Early–mid | Occasional | — |
| Renal salt wasting | `HP:0000127` Renal salt wasting | Lab/physiol | Mid–late | Occasional | Drives late hypertension |
| Hypertension | `HP:0000822` Hypertension | Sign | **Late only** | Frequent in advanced CKD | **Normotensive early — a discriminating feature** |
| Renal tubular dysfunction | `HP:0000124` Renal tubular dysfunction | Lab | Early | Frequent | Enzymuria, aseptic leukocyturia |
| Proteinuria (total) | `HP:0000093` Proteinuria | Lab | Early | Frequent, but **<1 g/24 h** | Sub-nephrotic — another discriminator |
| Renal cell carcinoma | `HP:0005584` Renal cell carcinoma | Neoplasm | Late | Reported in Romanian/Croatian AA-exposed; **not classically in BEN cohorts** | See §4.4 |

**Iatrogenic AAN only (not BEN):** `HP:0001994` Renal Fanconi syndrome, `HP:0003076` Glycosuria, `HP:0003355` Aminoaciduria. Do not attach these to BEN — they belong to the high-dose form.

### 3.2 The three clinical courses

Explicitly enumerated in **PMID:31054628** — a good candidate for `progression:` phases or subtype modeling:

1. Chronic tubulointerstitial nephropathy alone → ESRD.
2. Simultaneous UTUC (unilateral or bilateral) + renal impairment + typical BEN histopathology.
3. Initial deterioration of kidney function, *followed later* by UTUC (unilateral or bilateral).

### 3.3 Quality of life

**No BEN-specific EQ-5D / SF-36 / PROMIS/KDQOL data located.** This is a genuine literature gap. Reasonable inferences (mark as such, not as findings):
- The pre-ESRD phase is near-asymptomatic — QoL impact is likely minimal until CKD stage 4–5.
- Dialysis dependence, and bilateral nephroureterectomy in transplant candidates, dominate the QoL burden.
- Note a paradoxically *favorable* vascular finding: "lower arterial stiffness and slower vascular aging was reported in Croatian and Bosnian BEN patients undergoing dialysis compared to other ESRD patients" (**PMID:31054628**) — later-onset, milder hypertension.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes — none

BEN has **no germline causal gene**. This is the single most important negative statement in the entry. Household clustering without bloodline clustering, plus the Ukrainian migration experiment, ruled inheritance out:

> "Inherited pattern of the disease was ruled out by the fact that BEN often affected several members of the same household not necessarily blood related." (**PMID:31054628**)

The genetics that matter are **somatic and downstream** of the exposure.

### 4.2 Somatic mutations — the aristolochic acid signature

**TP53** (`hgnc:11998`) is the flagship:

> "Mutations at A:T pairs accounted for 89% of all p53 mutations, with 78% of these being A:T --> T:A transversions." — **PMID:17620607**

Adduct–mutation coupling in the same patients:

> "Adducts were present in 70% of the endemic cohort and in 94% of patients with specific A:T to T:A mutations in TP53. In contrast, neither aristolactam-DNA adducts nor specific mutations were detected in tissues of patients residing in nonendemic regions." — **PMID:22071594**

**Genome-wide characterization** (Poon et al., *Sci Transl Med* 2013, **PMID:23926199**):

> "Whole-genome and exome analysis of nine AA-associated UTUCs revealed a strikingly high somatic mutation rate (150 mutations/Mb), exceeding smoking-associated lung cancer (8 mutations/Mb) and ultraviolet radiation-associated melanoma (111 mutations/Mb). The AA-UTUC mutational signature was characterized by A:T to T:A transversions at the sequence motif A[C|T]AGG, located primarily on nontranscribed strands."

Same paper: AA mutations were **enriched at splice sites**, with RNA-seq confirming aberrant splicing and up-regulated nonsense-mediated decay machinery; and a high frequency of somatic mutation in chromatin modifiers, particularly **KDM6A**.

**COSMIC / SBS22** is the formal signature name. Exome sequencing of 15 BEN patients with urothelial carcinoma identified Signature 22 plus a driver-gene list (**PMID:31054628**, citing Scelo et al.):

> TP53, AHNAK, ARID1B, ATRX, BLM, CHD2, CHD5, CHD8, CHD9, CHEK2, CLTC, ERBB4, FN1, HUWE1, IARS2, KALRN, LRRK2, MLL2 (KMT2D), NEB, RXRA, SMCHD1, SPEG, STAG2, SYNE1, TRIO

Functional themes: transcriptional regulation, chromatin/histone modification, DNA damage response, DNA repair.

**Somatic vs germline:** every AA-attributable variant discussed here is **somatic**, arising in renal tubular and urothelial cells after adduct formation. Nothing is inherited. Curate `variant_origin: SOMATIC`.

**Variant class:** point substitutions, overwhelmingly **A:T→T:A transversions**, strand-biased to the non-transcribed strand (which is *why* they persist — transcription-coupled repair never sees them).

### 4.3 The newest and biggest result — Senkin et al., *Nature* 2024

This is the most important recent development and expands the exposure map substantially. 962 clear cell renal cell carcinomas sequenced across 11 countries:

> "In Romania, Serbia and Thailand, mutational signatures characteristic of aristolochic acid compounds were present in most cases, but these were rare elsewhere." — Senkin et al., *Nature* 2024;629(8013):910–918, **PMID:38693263**

Country-level SBS22 burden: **Romania 45/64 (70%)**, **Serbia 16/69 (23%)**, **Thailand 3/5 (60%)**. Implication: AA exposure is far more geographically widespread than the classical BEN foci — potentially millions of people.

### 4.4 The renal cell carcinoma question — an open issue worth curating as a knowledge gap

Classical BEN cohorts report **urothelial** carcinoma, not RCC. But:

> "We detected dA-AL-I in the 14 Romanian cases at levels ranging from 0.7 to 27 adducts per 10(8) DNA bases, in line with levels reported in Asian and Balkan populations exposed through herbal remedies or food contamination. The 15 cases from other countries were negative." — Turesky et al., *Br J Cancer* 2016, **PMID:26657656**

> "Although the source of exposure is uncertain and likely different in AAN regions than elsewhere, our results demonstrate that AA exposure in Romania exists outside localised AAN regions and provide further evidence implicating AA in RCC." — **PMID:26657656**

Also: Hoang et al., *Int J Cancer* 2015, "Renal cell carcinomas of chronic kidney disease patients harbor the mutational signature of carcinogenic aristolochic acid" (**PMID:25403517**).

But the 2019 review is careful: "RCC have not been reported in BEN patients but studies in Asia (Taiwan) have linked AA exposure to this cancer type... it is clear that these patients do not cover the Romanian population of the BEN area" (**PMID:31054628**).

**Suggested KB treatment:** a `discussions:` entry with `kind: KNOWLEDGE_GAP` — is AA-associated RCC a genuine BEN phenotype, an exposure-without-BEN phenotype, or a different exposure route in the same countries? The 2024 *Nature* result (23% of Serbian ccRCC) pushes toward "real and under-recognized."

### 4.5 Modifier genes

See §2.4. GPX3 rs8177412 is the best-supported effect modifier (8-fold for tumor risk, **PMID:37629712**). Nrf2 rs6721961, KEAP1 rs1048290, GSTP1 rs1695/rs1138272, MDR1 rs1045642 were tested in the same study; only the GPX3 tumor association and the GPX3+MDR1 female combination reached significance.

### 4.6 Epigenetics

Whole-genome methylation array analysis of BEN patients: Staneva et al., *BMC Nephrol* 2013 (**PMID:24131581**). Reported differential methylation relevant to BEN etiology. This work is small and unreplicated; I did not locate independent confirmation. Curate cautiously, or note as a gap. AAI is also reported to alter DNA methylation and histone marks in tubular cells, but I have not verified a specific primary source in this session — flag as unverified.

### 4.7 Chromosomal abnormalities

Only the historical 3q25–3q26 cytogenetic marker (**PMID:8730422**, 1996). No modern CMA/karyotype/dbVar-supported structural finding. Do not curate as established.

---

## 5. Environmental Information

### 5.1 The causal agent

- **Aristolochic acid I (AAI)** — `CHEBI:2825` (⚠️ canonical CHEBI label is **"aristolochic acid A"**, not "aristolochic acid I" — dismech's exact-label rule means `preferred_term: aristolochic acid I` with `term.label: aristolochic acid A`)
- **Aristolochic acid II (AAII)** — `CHEBI:194149` "aristolochic acid B"
- **Aristolactam I** — `CHEBI:235435` "Aristolactam I"
- **Source organism:** *Aristolochia clematitis* L. (European birthwort). NCBI Taxonomy ID **not verified this session** — look it up before binding.
- **ECTO exposure term:** `ECTO:9002244` "exposure to aristolochic acid A" *(verified via OLS4)* — this is the right binding for the `environmental[]` `exposure_term`.

### 5.2 Exposure routes (both should be `influences_mechanisms` links)

1. **Home-baked bread from wheat contaminated with *A. clematitis* seed** — the dominant historical route. Chronic, low-dose, decades-long.
2. **Crops grown in AA-contaminated soil** — AA quantified in corn and wheat grain from endemic Serbian villages (**PMID:27362729**). Chan et al. "hypothesized that AA present in edible parts of crops originating from AA-contaminated soil could be one of the pathways by which AA could enter the human food chain" (**PMID:31054628**).
3. *(Elsewhere, not BEN)* herbal remedies — TCM, Kampo, Ayurvedic; genus names *Mu Tong*, *Mokutsu*, *Fang ji*.

### 5.3 Competing / rejected etiologies

Curate these as `REFUTE` evidence or historical notes — they matter because the older BEN literature is dense with them.

| Hypothesis | Status | Reasoning |
|---|---|---|
| **Ochratoxin A** (`CHEBI:7719`) | **Rejected** as primary cause | EU Committee on Food Safety 2006: no convincing human-epidemiologic evidence. Four specific reasons in **PMID:31054628**: OTA is global; contamination overlaps between BEN and non-BEN areas; blood OTA is higher in *all* CKD (so it's a consequence of impaired clearance, not a cause); the tolerable weekly intake exceeds anything measured in BEN patients. Plus histopathology and tumor type differ from OTA animal tumors. |
| **Pliocene lignite / PAH leaching into well water** | Investigated and rejected by the nephrology consensus; **still advocated** by some geochemists (USGS-affiliated) | Original: Feder/Tatu/Orem, *Environ Geochem Health*. The 2019 review lists it among "hypotheses investigated and rejected." **Present both positions** — this is a live-but-minority dissent, not a settled fraud. |
| **Selenium deficiency** (`CHEBI:27568` selenium atom) | Contributory at most | Proposed as reducing antioxidant defence. Interesting mechanistic tie-in: selenium ions inhibit AAI oxidation by rat liver microsomes — i.e. they'd impair *detox*, raising effective AAI. Speculative. |
| **Heavy metals (Cd, Pb), microelements** | Rejected | Listed among "investigated and rejected" (**PMID:31054628**) |
| **Viruses, bacteria, immunologic and metabolic alterations, silicates** | Rejected | Same |

The pivotal external assessment: Voice et al. 2006 concluded that among suspected environmental agents, **mycotoxins and AA are the primary targets** (cited in **PMID:31054628**) — and the mycotoxin arm has since collapsed.

### 5.4 Lifestyle factors

- Subsistence farming, wheat cultivation, home bread-baking — the exposure vehicle.
- Recent CKD-risk drift: "the prevalence of hypertension in BEN villages does not differ from other rural parts of Croatia, very probably reflecting changes in lifestyle (high salt intake), obesity and more stress" (**PMID:31054628**). Modern comorbidity is diluting the historically distinctive normotensive phenotype.

### 5.5 Infectious agents

**Not applicable.** Infectious etiologies were investigated and rejected.

---

## 6. Mechanism / Pathophysiology

### 6.1 The ordered causal chain

Numbered, initiating lesion → clinical manifestation. Steps marked *(inferred)* are mechanistically reasoned rather than directly demonstrated in BEN patients.

1. ***Aristolochia clematitis* seeds co-mingle with harvested wheat and enter village flour** → chronic low-dose oral aristolochic acid (AAI/AAII) exposure over decades. (**PMID:31054628**, **PMID:27362729**)
2. **Ingested AAI is absorbed from the gut and enters the portal circulation** → systemic AAI burden. *(inferred; standard pharmacokinetics)*
3. **Hepatic nitroreduction of AAI** — cytosolic NQO1 plus microsomal POR and CYP1A1/1A2 reduce the nitro group → **leads to** aristolactam metabolites, including *N*-hydroxyaristolactam, which is sulfate-conjugated (AL-I-*N*-OSO₃). This is the *bioactivation* branch. (**PMID:31054628**; NQO1 dependence shown by dicoumarol inhibition, **PMID:21613233**)
   - **Competing branch — detoxification:** CYP-mediated *O*-demethylation of AAI yields AAIa (8-hydroxy-AAI), lowering effective AAI. The **activation:detoxification ratio is the proposed susceptibility switch.** (**PMID:31054628**)
4. **Reactive conjugate is exported from hepatocytes (MRP3/MRP4) and delivered to the kidney** → **results in** presentation of AAI/AL-I-*N*-OSO₃ at the peritubular capillary. *(partly inferred — the MRP arm is from a human liver–kidney co-culture model, PMID:29202460)*
5. **Basolateral uptake into proximal tubule epithelial cells by organic anion transporters OAT1 (SLC22A6) and OAT3 (SLC22A8)** → **causes** intracellular concentration far above plasma. This is the step that makes the disease *proximal-tubule-selective* rather than generally toxic.
   > "Aristolochic acid I (AAI), the more cytotoxic and genotoxic AA congener, exhibited high affinity for hOAT1 (K(i)=0.6 microM) as well as hOAT3 (K(i)=0.5 microM), and lower affinity for hOAT4 (K(i)=20.6 microM)." — **PMID:19643159**
   > "Uptake by slices was sensitive to known mOat1 and mOat3 substrates and the organic anion transport inhibitor probenecid, which also blocked the production of DNA adducts formed with reactive intracellular metabolites of AA-I." — **PMID:21546538**
6. **Intracellular nitroreduction (renal NQO1, COX in urothelium) generates a cyclic *N*-acylnitrenium ion** → the ultimate electrophile.
   > "a cyclic N-acylnitrenium ion with a delocalised positive charge (aristolactam-nitrenium ion) is the ultimate electrophilic species that binds preferentially to the exocycylic amino groups of purine nucleotides in DNA through the C7 position of the phenanthrene ring." — **PMID:31054628**

**From step 6 the chain branches. Both branches are needed to explain BEN.**

---

**BRANCH A — the fibrotic/renal-failure arm**

7A. **Nitrenium ion + reactive oxygen species attack proximal tubule epithelial cells** → **results in** acute tubular epithelial cell injury and necrosis. *(directly demonstrated in rodents; inferred as the initiating step in humans, whose exposure was too slow to observe an acute phase)*
8A. **Necrotic tubular cells release HMGB1 and mitochondrial DNA** → **activates** TLR signaling and sterile inflammation. (**PMID:35765703**)
9A. **Interstitial recruitment of activated monocytes/macrophages, then cytotoxic T lymphocytes** → transient AKI episode. (**PMID:35602498**)
10A. **Peritubular capillary rarefaction and interstitial hypoxia** → **worsens** tubular ischemia. *(rat model)*
11A. **Surviving tubular epithelium dedifferentiates; resident fibroblasts activate into TGF-β–expressing, αSMA/vimentin-positive myofibroblasts** → **causes** collagen deposition.
   > "The accumulation of vimentin and αSMA-positive cells expressing TGFβ in interstitial areas suggested an increase in resident fibroblasts and their activation into myofibroblasts resulting in collagen deposition and CKD." — **PMID:35602498**
12A. **Progressive hypocellular interstitial fibrosis with tubular atrophy, worst in outer cortex, decreasing inward** → **produces** the pathognomonic corticomedullary gradient.
13A. **Loss of erythropoietin-secreting peritubular interstitial cells** → **causes** anemia disproportionate to CKD stage. (**PMID:31054628**)
14A. **Loss of tubular concentrating and salt-handling capacity** → hyposthenuria, polyuria, nocturia, salt wasting → **explains** the characteristically *normal* early blood pressure.
15A. **Nephron loss → declining GFR → ESRD** in the 6th–7th decade, with symmetric, smooth, 20–30 g contracted kidneys.

---

**BRANCH B — the carcinogenic arm**

7B. **Nitrenium ion binds the exocyclic amino groups of dA and dG** → forms **7-(deoxyadenosin-*N*⁶-yl)aristolactam I (dA-AAI)** — the dominant, remarkably persistent adduct — plus dG-AAI, dA-AAII, dG-AAII. (**PMID:17620607**, **PMID:31054628**)
8B. **dA-AAI is poorly excised by nucleotide-excision repair, and sits preferentially on the non-transcribed strand where transcription-coupled repair cannot reach it** → **results in** adduct persistence for decades. Curate this as its own node — persistence, not just formation, is what makes a decades-latency cancer possible.
9B. **Replication past the persistent dA adduct mispairs** → **produces** A:T→T:A transversions at the A[C|T]AGG motif.
10B. **Transversions accumulate in TP53 and genome-wide** (KDM6A, chromatin modifiers, DNA-repair genes), plus splice-site enrichment → **causes** loss of tumor-suppressor function and aberrant splicing, at an extreme mutation burden (~150 mut/Mb). (**PMID:23926199**)
11B. **Malignant transformation of urothelium** → **upper tract urothelial carcinoma** in 30–50% of BEN patients, frequently bilateral, and (per the 2024 *Nature* data) also clear cell renal cell carcinoma in AA-exposed populations.

**Amplifier feeding both branches:** AA metabolism generates reactive oxygen species → oxidative distress → both cytotoxicity (Branch A) and additional oxidative DNA lesions (Branch B). Antioxidant-gene variants (GPX3) modulate this, which is exactly why GPX3 hits tumor risk rather than nephropathy risk (**PMID:37629712**).

### 6.2 Molecular pathways

| Pathway / process | Suggested GO term | Role |
|---|---|---|
| Xenobiotic response | `GO:0009410` response to xenobiotic stimulus; `GO:0071466` cellular response to xenobiotic stimulus | Upstream framing |
| NQO1 nitroreduction | `GO:0003955` NAD(P)H dehydrogenase (quinone) activity | Bioactivation — **the key `MolecularFunctionDescriptor`** |
| Organic anion transport | *(no exact GO match found for "organic anion transmembrane transporter activity"; search the actual GO tree before binding)* | Site-selective uptake |
| Nucleotide-excision repair | `GO:0006289` nucleotide-excision repair; `GO:0070911` global genome NER | `modifier: DECREASED` — the failure that permits mutation |
| Oxidative stress response | `GO:0034599` cellular response to oxidative stress | Amplifier |
| TGF-β signaling | `GO:0007179` transforming growth factor beta receptor signaling pathway | `modifier: INCREASED` — fibrogenic driver |
| EMT / partial EMT | `GO:0001837` epithelial to mesenchymal transition | Tubular dedifferentiation; Wnt7b/β-catenin implicated |
| Ferroptosis | `GO:0097707` ferroptosis | Emerging; lipid peroxidation / mitochondrial iron overload |
| Apoptosis | `GO:0006915` apoptotic process **(from memory — NOT verified this session, the OLS call errored)** | MAPK → p38/p53 → apoptosis |

Other signaling nodes reported (verify each before binding): **RhoA/ROCK → NLRP3 inflammasome → pyroptosis** (fasudil is protective; **PMID:41289940**, 2026); **PSTPIP2 / IL-19 / neutrophil extracellular traps**; **Nrf2–HO-1/GPX4** axis; **pregnane X receptor → p53 ubiquitination** (2026, *Ren Fail*).

### 6.3 Cell types involved (CL terms, all verified via OLS4)

| Cell type | CL term | Role |
|---|---|---|
| Kidney proximal convoluted tubule epithelial cell | `CL:1000838` | **Primary target** — OAT-mediated uptake, necrosis, dedifferentiation |
| Kidney proximal straight tubule epithelial cell | `CL:1000839` | S3 segment; classically the most vulnerable |
| Urothelial cell | `CL:0000731` | **Second target tissue** — COX-mediated activation, malignant transformation |
| Transitional epithelial cell | `CL:0000244` | Broader urothelial parent |
| Kidney interstitial fibroblast | `CL:1000692` | Activates to myofibroblast; also the EPO-producing population |
| Myofibroblast cell | `CL:0000186` | αSMA⁺/vimentin⁺ collagen producer |
| Fibroblast | `CL:0000057` | Generic parent |
| Macrophage / cytotoxic T cell | *(look up `CL:0000235`, `CL:0000910` — not verified this session)* | AKI-phase infiltrate (**PMID:35602498**) |
| Endothelial cell (peritubular capillary) | *(not verified)* | Capillary rarefaction → hypoxia |

> "we identified 4 major actors in the AKI-to-CKD transition: (1) the tubular epithelial cells, (2) the endothelial cells of the interstitial capillary network, (3) the inflammatory infiltrate, and (4) the myofibroblasts." — **PMID:35602498**

### 6.4 Molecular profiling

- **Genomics:** COSMIC/SBS22 signature; driver-gene list (§4.2); ~150 mut/Mb.
- **Transcriptomics:** RNA-seq of AA-UTUC shows up-regulated nonsense-mediated decay machinery and aberrant splicing events tied to splice-site mutations; 68–76% of AA-specific deleterious mutations propagate to transcript level — "a possible basis for neoantigen formation and immunotherapy targeting" (**PMID:34569060**). Rat DrugMatrix work identified a 30-gene cluster predicting nephrotoxic potential pre-injury (**PMID:31054628**).
- **Proteomics:** differential expression of cytoskeletal, developmental, and inflammatory kidney proteins in AA-exposed vs control mice; a proteomic signature in rat kidney (**PMID:31054628**).
- **Metabolomics:** ¹H-NMR urine profiling in rats showed increased glucose, amino acids, organic acids and decreased hippurate — "indicative of an acute proximal tubule injury." Clinically, Belgian AAN and Croatian BEN patients had **close urine metabolic profiles**, "bringing some new evidence that both diseases have a common etiology" (**PMID:31054628**). That's a nice orthogonal confirmation of the lumping argument.
- **Adductomics:** dA-AL-I quantified by ³²P-postlabeling and LC-ESI/MS/MS³, in fresh and FFPE tissue.
- **Lipidomics:** no BEN-specific dataset located.
- **Single-cell / spatial transcriptomics:** no BEN-specific dataset located. Genuine gap — a spatial study of the outer→inner cortical fibrosis gradient would be an obvious high-value experiment.
- **Functional genomics screens:** no BEN-specific CRISPR/RNAi screen located.

---

## 7. Anatomical Structures Affected

All UBERON IDs verified via OLS4 this session.

### 7.1 Organ level

- **Primary:** kidney — `UBERON:0002113`
- **Primary (second target tissue):** upper urinary tract urothelium — renal pelvis `UBERON:0001224`, kidney pelvis urothelium `UBERON:0004788`, ureter `UBERON:0000056`, urothelium `UBERON:0000365`
- **Secondary:** urinary bladder `UBERON:0001255` (late, mostly in the Belgian AAN cohort post-nephroureterectomy); hematopoietic system (EPO-deficient anemia); cardiovascular system (late CKD hypertension)
- **Body systems:** renal/urinary primarily; hematologic and cardiovascular secondarily

### 7.2 Tissue level and the corticomedullary gradient

The gradient is the signature of this disease and deserves its own node:

> "The most dominant morphologic characteristic is extensive hypocellular interstitial fibrosis associated with tubular atrophy involving medullary rays, that decrease in intensity from outer medulla and the cortical labyrinth to the inner cortex." (**PMID:31054628**)

- Cortex of kidney — `UBERON:0001225`
- **Outer cortex of kidney — `UBERON:0002189`** (worst affected)
- Renal medulla — `UBERON:0000362` (medullary rays involved)
- Proximal tubule — `UBERON:0004134`

Glomeruli are **relatively spared early** — "good preservation of glomeruli" — with periglomerular fibrosis, obsolescent (collapsing-type) glomeruli, occasional TMA-like and FSGS-like lesions appearing only as the disease advances. Vascular lesions: arteriolar hyalinosis, intimal fibrous hyperplasia, occasional mucoid arterial intimal fibrosis, and multifocal thickening/splitting of peritubular capillary basement membranes.

Inflammatory infiltrate is **sparse** — "usually less than that might be expected in other renal diseases, were found in less than one-third of cases." This is why "hypocellular" is the operative adjective.

### 7.3 Subcellular level

Suggested GO cellular-component bindings **(from memory — verify all before binding)**: nucleus (`GO:0005634`) for adduct formation; mitochondrion (`GO:0005739`) for mtDNA damage and iron overload; endoplasmic reticulum (`GO:0005783`) for Ca²⁺ release / ER stress; cytosol for NQO1; plasma membrane / basolateral plasma membrane for OAT1/OAT3.

### 7.4 Lateralization

**Bilateral and symmetric** for the nephropathy — "the kidneys are extremely small, symmetrically contracted, weighing only 20–30 grams each with smooth outlines." UTUC may be **unilateral or bilateral**, and bilaterality is common enough that the consensus recommends *bilateral* prophylactic nephroureterectomy pre-transplant (**PMID:24166461**, **PMID:31054628**).

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** insidious onset in the **fifth decade**; ESRD in the sixth or seventh. **Never reported in children** — "indicating that long period of exposure to the environmental agent is needed" (**PMID:31054628**).
- **Pattern:** chronic, insidious. No acute presenting event, no fever, no pain, no nephritic syndrome.
- **Required exposure duration:** the diagnostic criteria use **>20 years residency** in a BEN village/household as the exposure threshold (**PMID:24166461**).
- **Secular drift:** "In last decades, the age when BEN patients start to receive dialysis was shifted to older ages, raising the question whether the etiological agent is still present or active." (**PMID:31054628**) — i.e. the cohort is aging out, consistent with exposure ending in the 1970s.

### 8.2 Progression

| Stage | Features |
|---|---|
| **Exposure / latent** | Decades of low-dose AA ingestion. Adducts accumulating, no clinical signal. Detectable only by adduct assay. |
| **Early (subclinical)** | Proximal tubule damage: low-molecular-weight (α1-microglobulin, β2-microglobulin) proteinuria, enzymuria, aseptic leukocyturia, low urine specific gravity, occasional urinary casts. Normal or near-normal eGFR. **Normotensive.** This is the screening window. |
| **Intermediate** | Declining eGFR, anemia disproportionate to CKD stage, sub-nephrotic proteinuria (<1 g/24 h), renal atrophy/nephrosclerosis on ultrasound. |
| **Advanced** | CKD stage 4–5; hypertension develops (salt wasting + volume); UTUC risk peaks. |
| **End-stage** | ESRD requiring dialysis or transplant. Kidneys 20–30 g, smooth-outlined. UTUC often the terminal event. |

- **Rate:** slow, over years to decades. Contrast with iatrogenic AAN, which is "rapidly progressive to ESRD."
- **Course pattern:** **progressive, monotonic**. No relapsing-remitting phase, no plateau, no documented spontaneous remission.
- **Duration:** chronic and lifelong once established.

### 8.3 Patterns

- **Remission:** none. Removing the exposure does **not** reverse established injury — "the nephrotoxic effects of AA are irreversible" (**PMID:31054628**), and "there is no effective treatment for delaying or reversing the renal deterioration caused by AAN" (**PMID:37448287**).
- **Critical periods / windows of opportunity:**
  1. **Before exposure** — the only true prevention window (agricultural practice, grain sieving).
  2. **The subclinical tubular-proteinuria window** — the only window where screening changes anything, and what the 5-yearly mass screening exists for.
  3. **Cancer surveillance window** — because adducts persist for decades, cancer risk *outlives the exposure*. This is the reason surveillance must continue in people whose exposure ended 40 years ago, and it's the most counterintuitive clinical implication of the whole disease.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Metric | Value | Source |
|---|---|---|
| Prevalence, affected subjects in exposed population | **2–5%** | **PMID:31054628** |
| Prevalence, farmers *suspected* of BEN | **10–15%** | **PMID:31054628** |
| Historical range across endemic villages | 0.4–8.3% | Literature synthesis |
| **Croatia, 2,487 adult farmers, 6 endemic + 3 non-endemic villages** | **Overall EN prevalence 1.0% (range 0.3–2.3%); suspected 3.9%** | **PMID:22116163** |
| Estimated exposed population, Balkans | ~**100,000** exposed; ~**25,000** with kidney disease | **PMID:31054628** |
| Estimated exposed, elsewhere | ~8 million (Taiwan); >100 million (mainland China) | **PMID:31054628** |
| UTUC incidence among BEN patients | **30–50%** (also given as 40–46%) | **PMID:31054628** |
| UTUC mortality, Croatian endemic county vs rest of Croatia | **55-fold higher** | **PMID:31054628** |

For a `prevalence:` block using the structured slots: 2–5% → `rate_per_100000: 3500` (midpoint), `rate_low: 2000`, `rate_high: 5000`, `measure_type: POINT_PREVALENCE`, `prevalence_class: ABOVE_1_IN_1000`, `population: "Adult residents of endemic Balkan villages"`. Do **not** compare that to a general-population rate — it's conditioned on residence in an endemic village.

**Trend — declining, possibly toward disappearance:**

> "The prevalence of EN in the endemic Croatian areas appears to be decreasing. For the first time, we failed to detect any EN patients in a village that was previously considered endemic, which might indicate that EN is diminishing." — **PMID:22116163**

> "in Croatian field surveys conducted between 2005 and 2015, where neither new BEN nor new UTUC patients were detected in some previously established BEN villages. Similar trends were observed in Serbia." — **PMID:31054628**

The mechanism of decline is the agricultural change of the 1970s, not any medical intervention (§2.5). But the review adds an important caveat: "in next few years, due to past exposure, new BEN patients will still start dialysis and even more importantly new BEN/UTUC patients will be diagnosed."

### 9.2 Inheritance

- **Pattern:** **not inherited.** Multifactorial at most — environmental exposure with polygenic susceptibility modifying penetrance. Household aggregation, not bloodline aggregation.
- **Penetrance:** ~2–5% among exposed. Whatever susceptibility exists is very incompletely penetrant.
- **Expressivity:** variable — three distinct clinical courses (§3.2).
- **Anticipation:** not applicable.
- **Germline mosaicism:** not applicable.
- **Founder effects:** none — the geographic clustering is *ecological*, not genetic, and the Ukrainian and Bosnian migration studies prove it in both directions.
- **Consanguinity:** no established role.
- **Carrier frequency:** not applicable.

If dismech models this, the `inheritance:` block should be either absent or explicitly documented as non-Mendelian with a note explaining the household-clustering artifact. The OMIM 124100 "familial nephropathy" framing is the thing most likely to mislead a downstream consumer.

### 9.3 Population demographics

- **Affected populations:** rural farming populations of **Bosnia and Herzegovina, Bulgaria, Croatia, Romania, Serbia**, in villages along tributaries of the Danube. Ethnicity is irrelevant — settlers of any origin acquired local risk after ~20 years.
- **Geographic distribution:** highly focal, village-level. Named endemic foci in the literature include Kaniža, Slavonski Kobaš, Dubočac (Croatia) and Vreoci, Kutleš (Serbia).
- **"Sporadic BEN":** cases occur outside recognized endemic villages. Nikolić et al. 2006 first proposed this; aristolactam-DNA adducts and signature mutations were subsequently found in 10 Croatian and Bosnian farmers in **non-endemic** villages (**PMID:31054628**, unpublished at time of review). The 2024 *Nature* data (23% of Serbian ccRCC carrying SBS22) argues strongly that exposure is far broader than the classical map (**PMID:38693263**).
- **Sex ratio:** essentially **1:1** — "There were no gender differences, although slight insignificant female predominance was found (1:1.2)." (**PMID:31054628**) Note the contrast with iatrogenic AAN, which is female-skewed purely because of who attended the Belgian slimming clinic — a cohort artifact, not biology.
- **Age distribution:** onset 5th decade; ESRD 6th–7th; **zero pediatric cases**.

---

## 10. Diagnostics

### 10.1 The headline caveat

> "There are no diagnostic features which are pathognomonic of BEN." (**PMID:31054628**)

Diagnosis is a **combination** of residence history, tubular proteinuria, reduced eGFR, anemia, and imaging — with adduct/signature detection as the only truly confirmatory test.

### 10.2 Laboratory tests and biomarkers

| Test | Threshold / note | LOINC |
|---|---|---|
| **α1-Microglobulin (urine)** | **>31.5 mg/g**, and α1-microglobulin/urine albumin ratio **≥0.91** — the consensus tubular-proteinuria criterion | *not looked up* |
| **β2-Microglobulin (urine)** | "One of the most reliable diagnostic markers of BEN, typical for tubular proteinuria" | *not looked up* |
| eGFR (CKD-EPI) | Reduced; the consensus specifies CKD-EPI | |
| Total proteinuria | **<1 g/24 h** — sub-nephrotic, a real discriminator | |
| Hemoglobin | **<120 g/L** (men, and women >50 y); **<110 g/L** (women ≥50 y) | |
| Red blood cell count | Part of the screening panel | |
| Urine specific gravity | Low (hyposthenuria) | |
| Dipstick urinalysis | Screening panel | |
| Urinary enzymes (enzymuria) | Early tubular injury | |
| **Urine cytology** | Screening panel; the UTUC detection arm | `NCIT:C94473` Urine Cytology |

**Emerging / research biomarkers:** urinary metabolomic profile by ¹H-NMR (Belgian AAN ≈ Croatian BEN); urinary molecular profiles in AA-UTUC (**PMID:34569060**); KIM-1/NGAL as generic tubular-injury markers (not BEN-specific — do not overclaim).

### 10.3 The confirmatory molecular tests

These are what separate BEN/AAN from every other chronic tubulointerstitial nephropathy:

1. **Aristolactam-DNA adducts (dA-AL-I) in renal cortex** — ³²P-postlabeling, or LC-ESI/MS/MS³ (now usable on FFPE tissue as well as fresh). Detected in 70% of an endemic UTUC cohort (**PMID:22071594**). Persist for decades. Levels in Romanian RCC cases: **0.7 to 27 adducts per 10⁸ DNA bases** (**PMID:26657656**).
2. **TP53 A:T→T:A transversion signature** in tumor tissue.
3. **Whole-exome / whole-genome sequencing → COSMIC SBS22.**

The consensus asks that this be operationalized surgically: "In all UTUC patients from farming villages, renal cortex should be excised during surgery (distant from tumor) and analyzed for evidence of BEN, and if possible, should be frozen at -20°C for subsequent determination of the level of aristolactam-DNA adducts and TP53 fingerprint mutation on tumor tissue." (**PMID:31054628**)

### 10.4 Imaging and endoscopy

- **Renal ultrasound** — renal atrophy and nephrosclerosis; part of the diagnostic set
- **CT urography** — `NCIT:C17204` Computed Tomography — when UTUC is suspected
- **Ureteropyeloscopy** — `NCIT:C94308` Ureteroscopy
- **Cystoscopy** — `NCIT:C16482` Cystoscopy — mandatory for hematuria

### 10.5 Biopsy / histopathology

`NCIT:C51699` Kidney Biopsy. Findings (all from **PMID:31054628**):
- Extensive **hypocellular** interstitial fibrosis with tubular atrophy, involving medullary rays
- **Corticomedullary gradient**: severity decreasing outer→inner cortex
- Glomeruli relatively spared early; later periglomerular fibrosis, obsolescent (collapsing-type) glomeruli, occasional TMA-like and FSGS-like lesions
- Vascular: arteriolar hyalinosis, intimal fibrous hyperplasia, mucoid arterial intimal fibrosis, multifocal thickening/splitting of peritubular capillary basement membranes
- Sparse chronic inflammatory infiltrate, <1/3 of cases
- End-stage: symmetric contracted kidneys, 20–30 g each, smooth outlines
- Urothelial tumors: typically **high-grade transitional cell carcinoma**

### 10.6 Genetic testing

**Germline genetic testing has no diagnostic role in BEN.** There is no gene panel, no WES/WGS indication, no CMA, no karyotype, no FISH, no mtDNA test, no repeat-expansion test. The only sequencing that matters is **somatic tumor sequencing** for the AA signature. Say this explicitly in the entry — the OMIM framing invites the opposite assumption.

### 10.7 Diagnostic and classification criteria — the 2013/2014 consensus

Jelaković et al., *Nephrol Dial Transplant* 2014;29(11):2020–7 (**PMID:24166461**), from the 2008 Brač workshop. Table 2 as reproduced in **PMID:31054628**:

**I. Diseased/affected BEN cases** — any one of:
1. Biopsy proven / indicative of BEN, **or**
2. Residency in a BEN household >20 years **+** tubular proteinuria **+** decreased eGFR **+** anemia, **or**
3. Residency in a BEN village >20 years **+** UTUC **+** tubular proteinuria

**II. Suspected BEN** — any one of:
1. Residency in a BEN household >20 years **+** reduced eGFR **+** anemia, **or**
2. Residency in a BEN household >20 years **+** tubular proteinuria, **or**
3. Residency in a BEN village >20 years **+** UTUC

**III. High-risk group** — residency in a BEN household >20 years; or residency in a household with sporadic/suspected BEN cases >20 years

**IV. Sporadic BEN** — biopsy proven/indicative of BEN in a patient with UTUC outside the endemic region, or in a member of their household

*Footnote definitions:* tubular proteinuria = α1-microglobulin >31.5 mg/g **and** α1-microglobulin/urine albumin ratio ≥0.91. Anemia = Hb <120 g/L (men and women >50 y), <110 g/L (women ≥50 y).

### 10.8 The general AAN diagnostic criteria (Gökmen et al., **PMID:23552405**)

Diagnosis is **certain** with renal failure plus **any two of three**:
1. Renal histology showing interstitial fibrosis with a **corticomedullary gradient**
2. History of ingesting vegetal/herbal products whose **phytochemical analysis demonstrated AA**
3. Presence of **aristolactam-DNA adducts** (or the specific TP53 A:T→T:A mutation) in kidney tissue or a urothelial cancer

With **one** criterion, diagnosis is "highly probable." Either AA-in-plant or adducts-in-tissue is described as "central to a diagnosis that provides absolute certainty." (**PMID:31054628**)

### 10.9 Differential diagnosis

Everything that produces chronic tubulointerstitial fibrosis. From **PMID:31054628**, must exclude:

| Differential | Distinguishing feature |
|---|---|
| Reflux nephropathy / chronic or recurrent pyelonephritis | Scarring pattern, infection history, imaging |
| Hypertensive nephrosclerosis | Early hypertension present (BEN is **normotensive early**) |
| Cadmium nephropathy | Occupational/environmental Cd history; Cd biomonitoring |
| Lead nephropathy | Blood/bone lead |
| Cyclosporine A nephrotoxicity | Transplant/autoimmune drug history |
| Ifosfamide, pamidronate, nitrosourea nephrotoxicity | Oncology drug history |
| Lithium nephropathy | Psychiatric drug history |
| Analgesic nephropathy (heavy NSAID use) | Papillary necrosis; drug history |
| Herbal-tea nephropathy (non-BEN) | Exposure history |
| Other AAN (iatrogenic) | Rapid course, Fanconi syndrome, herbal-product history — **same molecular disease** |

The **combination of chronic tubulointerstitial nephropathy + UTUC** is the pattern that should immediately raise AAN/BEN. Two individually rare things co-occurring is the whole epidemiological argument in miniature.

### 10.10 Screening

Per **PMID:24166461** / **PMID:31054628**:

- **Whole adult population of BEN villages: mass screening every 5 years.** Panel = tubular proteinuria (α1-microglobulin) + eGFR (CKD-EPI) + RBC count + dipstick urinalysis + urine cytology.
- **"Diseased"** → refer to local nephrologist.
- **"BEN suspected"** and BEN-household members without tubular proteinuria or UTUC → **yearly** screening.
- **ESRD of unknown origin from non-endemic villages**, plus their household members → screen for **sporadic BEN/UTUC**.
- **High UTUC risk** (biopsy indicative of BEN; BEN with CKD ≥3A; BEN transplanted or on dialysis) → **every 6 months** with urine cytology, ultrasound, other imaging as needed; their household members **yearly**.
- **Previous UTUC, bladder cancer, or hematuria** → **every 3 months**; hematuria → cystoscopy; high UTUC suspicion → ureteropyeloscopy + CT.

No newborn screening, no carrier screening, no cascade genetic screening. `NCIT:C48261` Screening; `NCIT:C15406` Cancer Screening.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Untreated:** invariable progression to ESRD and death.
- **With renal replacement:** survival is that of the ESRD population, **modified upward** by BEN's unusual cardiovascular profile — "lower arterial stiffness and slower vascular aging ... compared to other ESRD patients" (**PMID:31054628**), attributable to later-onset, milder hypertension.
- **Modified downward by cancer:** UTUC mortality in the Croatian endemic county was **55× higher** than the rest of Croatia (**PMID:31054628**). UTUC is the disease's leading cause of excess death.
- **I did not locate BEN-specific 5-/10-year survival figures.** Report this as a gap rather than substituting general ESRD statistics.

### 11.2 Morbidity

- ESRD with lifelong dialysis dependence or transplantation
- Anemia disproportionate to CKD stage → fatigue, reduced exercise capacity
- **Bilateral nephroureterectomy** in transplant candidates — a large, permanent, iatrogenic morbidity imposed by the cancer risk
- Recurrent urothelial tumors, including bladder cancer years after native nephroureterectomy (**PMID:31054628**)
- No GBD-specific BEN disability estimates located

### 11.3 Complications

Renal: ESRD, renal anemia, late hypertension, salt wasting, CKD-MBD (by extension, not BEN-specific).
Oncologic: UTUC (30–50%, often bilateral), bladder carcinoma (particularly post-transplant Belgian cohort), possibly RCC (§4.4).
Transplant-specific: de-novo urothelial malignancy under immunosuppression — the reason mTOR inhibitors are preferred.

### 11.4 Recovery potential

**None.** Renal injury is irreversible; exposure cessation halts accrual but does not reverse fibrosis. Adducts persist for decades, so **cancer risk does not fall when exposure stops** — arguably the most clinically important prognostic fact in the whole disease.

### 11.5 Prognostic factors

| Factor | Direction |
|---|---|
| Cumulative AA dose / exposure duration | Worse. In iatrogenic AAN, >200 g cumulative *Aristolochia* → higher UTUC risk (**PMID:10841870**) |
| CKD stage at diagnosis | Worse |
| Presence of UTUC | Markedly worse |
| Bilateral UTUC | Worse — limits conservative surgery |
| Aristolactam-DNA adduct burden in renal cortex | Higher = greater cancer risk (mechanistically; formal prognostic modeling not established) |
| **GPX3 rs8177412 variant genotype** | **~8-fold increased UTUC risk** → "BEN patients carrying variant GPX3 genotype should be more frequently monitored" (**PMID:37629712**) |
| SBS22 mutation burden | One study reports the AA signature defines a **low-risk subtype** of UTUC (**PMID:32292497**) — plausibly because the enormous neoantigen load makes these tumors immunologically visible. **Directionally opposite to what you'd expect; curate carefully and note the tension.** |

---

## 12. Treatment

**Bottom line: there is no disease-modifying therapy.** The intervention set is exposure elimination, generic CKD/ESRD care, and aggressive cancer surveillance and surgery.

> "there is no effective treatment for delaying or reversing the renal deterioration caused by AAN." — **PMID:37448287**

### 12.1 Exposure elimination

The only genuinely causal intervention. Not pharmacological — agricultural and dietary.

### 12.2 Renal replacement therapy

> "Patients with established BEN should be treated like other CKD patients, with peritoneal dialysis, hemodialysis or renal transplantation in ESRD stage." (**PMID:24166461**, via **PMID:31054628**)

| Treatment | NCIT |
|---|---|
| Peritoneal dialysis | `NCIT:C15297` Peritoneal Dialysis |
| Hemodialysis | *(NCIT lookup errored this session — resolve before binding)* |
| Kidney transplantation | `NCIT:C15265` Kidney Transplantation |
| Supportive care | `NCIT:C15747` Supportive Care |
| Erythropoiesis-stimulating agent for renal anemia | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` `NCIT:C20429` Erythropoietin |

### 12.3 Transplant-specific protocol — this is where BEN diverges from ordinary CKD

All from **PMID:31054628** / **PMID:24166461**:

- BEN patients must be screened to **exclude urothelial cancer before waitlisting**.
- **Bilateral nephroureterectomy should be performed prior to transplantation** — in all recipients <65 years, and in those >65 if UTUC or bladder cancer is already diagnosed or there is a family history of UTUC. `NCIT:C51646` Nephroureterectomy; `NCIT:C159437` Nephroureterectomy with Cuff of Bladder.
- **Living donors** who lived in a BEN region >15–20 years should have a **donor kidney biopsy** to exclude BEN and/or AA-DNA adducts. (An unusual and rather striking recommendation — the donor may be silently affected.)
- Patients who **refuse** bilateral nephroureterectomy require close post-transplant urothelial monitoring.
- **mTOR inhibitors should be considered** for immunosuppression in BEN transplant recipients (antineoplastic properties). `therapeutic_modality: SMALL_MOLECULE`.

### 12.4 UTUC treatment

- **Standard:** total nephroureterectomy with excision of a bladder cuff around the ureteral ostium **plus regional lymphadenectomy**. `NCIT:C159437`; `NCIT:C15329` Surgical Procedure.
- **Conservative/kidney-sparing surgery:** reserved for highly selected patients with **bilateral** tumors; higher local recurrence, requires close monitoring.
- **Systemic chemotherapy:** for unresectable/metastatic disease. `NCIT:C15632` Chemotherapy.
- **Non-invasive bladder cancer** (Belgian AAN cohort experience): endoscopic resection + endovesical **mitomycin C** instillation; **BCG** (`NCIT:C298` BCG Vaccine) also used successfully, including in renal-graft recipients when combined with modulation of immunosuppression and prophylactic anti-tuberculosis chemotherapy.
- **Radical cystectomy with pyelostomy of the graft** — the ultimate measure for invasive bladder cancer in transplant recipients.

### 12.5 Immunotherapy — a live, biologically motivated hypothesis

AA-UTUC carries an extreme mutation burden with 68–76% of AA-specific deleterious mutations propagating to the transcript level — "a possible basis for neoantigen formation and immunotherapy targeting" (**PMID:34569060**). Curate as an emerging hypothesis with `status: EMERGING`, not as established practice. I found no completed BEN-specific checkpoint-inhibitor trial.

### 12.6 Experimental / preclinical (nephroprotection)

None of these has clinical evidence in BEN. All are rodent or cell-model results — curate with `evidence_source: MODEL_ORGANISM` or `IN_VITRO`, never as treatment recommendations.

| Agent / target | Effect | Source |
|---|---|---|
| **Dicoumarol** (NQO1 inhibitor) | "Inhibition of renal NQO1 activity by dicoumarol suppresses nitroreduction of aristolochic acid I and attenuates its nephrotoxicity" | **PMID:21613233** |
| **Probenecid** (OAT inhibitor) | Blocked DNA adduct production in mouse renal cortical slices | **PMID:21546538** |
| **Fasudil** (RhoA/ROCK inhibitor) | Suppressed RhoA/ROCK, inhibited NLRP3 inflammasome, improved renal function | **PMID:41289940** (2026) |
| Nitric oxide restoration | Reduced acute-to-chronic transition severity in mouse AAN | PMC5568239 |
| Pregnane X receptor activation | Mitigates AA-induced AKI via p53 ubiquitination | *Ren Fail* 2026 |
| PSTPIP2 / IL-19 / NET axis | PSTPIP2 ameliorates AAN by suppressing IL-19-mediated NET formation | PMC10906995 |
| Nrf2–HO-1/GPX4 (anti-ferroptosis) | Mitochondrial iron overload inhibition | PMC7873870 |

**Dicoumarol and probenecid are the two mechanistically pointed ones** — they attack the exact bioactivation and uptake steps identified in §6.1 steps 3 and 5. That coherence is itself a form of mechanistic validation, even though neither is a clinical option.

### 12.7 Pharmacogenomics

No CPIC guideline, no FDA PGx biomarker, no PharmGKB entry for BEN. The GPX3/MDR1/NQO1/CYP1A polymorphism story is **risk-stratification**, not drug dosing. Do not present it as pharmacogenomics.

### 12.8 Clinical trials

I found **no BEN-specific interventional trial** registered on ClinicalTrials.gov in this session. If curating `clinical_trials:`, leave the section empty rather than importing generic CKD or UTUC trials — an honest empty section beats a padded one.

---

## 13. Prevention

### 13.1 Primary prevention — the one that actually worked

**Eliminating AA from the food chain**, achieved (accidentally) through agricultural modernization:

> "important improvements occurred in the 1970s: 1) large common mills were built and used instead of small village mills; 2) combines became popular with much smaller holes in sieving machines enabling better separation of much bigger Aristolochia from the wheat seeds" (**PMID:31054628**)

And the crucial nuance, which is a genuinely good insight for public health: the plant is still there.

> "the presence of Aristolochia in farming fields is a risk factor but only if associated with particular agricultural practices and life style." (**PMID:31054628**)

You do not need to eradicate the weed. You need to sieve properly. That is a far cheaper and more tractable intervention, and it is why the disease is disappearing without anyone having deliberately set out to make it disappear.

Other primary measures:
- Regulatory bans on AA-containing herbal products (FDA 2001 and international equivalents)
- Public health education in endemic regions — `NCIT:C16664` Health Education; `NCIT:C18975` Public Health Education
- Soil/crop monitoring where AA uptake into edible crops is documented (**PMID:27362729**)
- Weed management in wheat fields

### 13.2 Secondary prevention

The 5-yearly mass screening program (§10.10). This is the textbook case for population screening: a long asymptomatic phase, a cheap urine-based marker, a defined at-risk population, and a severe outcome.

### 13.3 Tertiary prevention

- Intensive UTUC surveillance schedules stratified by risk (6-monthly / 3-monthly)
- Prophylactic bilateral nephroureterectomy in transplant candidates
- mTOR-inhibitor-based immunosuppression post-transplant
- Standard CKD progression management (BP control, RAAS blockade, anemia management) — extrapolated from general CKD care, not BEN-specific evidence

### 13.4 Not applicable

**Immunization** — no infectious etiology, no vaccine. (BCG here is intravesical immunotherapy for bladder cancer, *not* immunization — don't let the shared name confuse the curation.)
**Genetic counseling / prenatal / PGD / carrier screening** — no germline causal gene. `NCIT:C15240` Genetic Counseling should **not** be curated as a treatment or prevention for BEN. Household screening is *environmental* cascade screening, not genetic.

### 13.5 Prophylaxis

No chemoprophylaxis exists. Dicoumarol and probenecid are preclinical only (§12.6).

---

## 14. Other Species / Natural Disease

This is a small but genuinely interesting section — the veterinary observation **preceded** the human hypothesis by a decade.

### 14.1 Horses — the historical first observation

> "Already ten years before, Martinčić and Dumić had reported horse poisoning with Aristolochia clematitis and found strict similarities in epidemiology, clinic, laboratory data and renal pathology between horses and BEN." (**PMID:31054628**)

Species: *Equus caballus*. NCBI Taxonomy ID **not verified this session** — look up before binding. Naturally occurring, environmental, in the same Balkan region, from the same plant. This is a strong `animal_models:` candidate with `relationship: RECAPITULATES` and high face validity — same species-of-plant, same route, same organ, same pathology — though as a mid-20th-century veterinary report the evidence grade is limited.

### 14.2 Goats

Combined toxicity of *Aristolochia bracteata* and *Calaba rotundifolia* in goats, Sudan (El Dirdiri et al., *Vet Hum Toxicol* 1987, cited in **PMID:31054628**). A different *Aristolochia* species, a different continent, the same genus and toxin class. Species: *Capra hircus*.

### 14.3 Comparative biology

- The AA activation pathway (nitroreduction by NQO1/POR/CYP) is conserved across rodents, rabbits, and humans — which is why the rodent models are as faithful as they are.
- **A caveat worth curating as a limitation:** in **rodents**, the characteristic A:T→T:A transversion lands in **codon 61 of H-*ras***; in **humans** it lands in ***TP53***. Same mutational mechanism, different target gene, because different genes drive tumorigenesis in each species (**PMID:31054628**). A model that reproduces the *signature* is not automatically reproducing the *driver*.
- Nitroreduction is described as essential for rapid AAI clearance "in different species including humans" — the same reaction is both the clearance route and the poisoning route, which is an unusually elegant piece of toxicological irony.

### 14.4 Zoonotic potential

**None.** BEN is a toxic exposure, not transmissible. Cross-species susceptibility exists only in the sense that any mammal eating *Aristolochia* is at risk.

### 14.5 OMIA

I did not locate an OMIA entry for aristolochic acid nephropathy in the horse. Report as not found rather than absent.

---

## 15. Model Organisms

### 15.1 The flagship experimental model — rodent AAN

Model type: **mammalian, in vivo, chemically induced** (not genetic).

Species: male **Wistar rat**, and **mouse** (various strains); **rabbit** also used. "Human AAN has been reproduced in several animal models including rabbits, mice and rats."

**Biphasic course — this is what makes it valuable:**

> "an early phase of acute tubular necrosis was rapidly followed by a massive interstitial recruitment of activated monocytes/macrophages followed by cytotoxic T lymphocytes, resulting in a transient AKI episode. A later chronic phase was then observed with progressive tubular atrophy related to dedifferentiation and necrosis of tubular epithelial cells." — **PMID:35602498**

**Phenotype recapitulation:**

| Human BEN feature | Rodent AAN | Fidelity |
|---|---|---|
| Proximal tubule epithelial injury | ✅ Acute tubular necrosis | HIGH |
| Interstitial fibrosis, tubular atrophy | ✅ αSMA⁺/vimentin⁺ myofibroblasts, collagen deposition | HIGH |
| Peritubular capillary loss / hypoxia | ✅ Demonstrated in rat | MODERATE |
| Aristolactam-DNA adduct formation | ✅ | HIGH |
| A:T→T:A transversion signature | ✅ — but in **H-*ras* codon 61**, not TP53 | MODERATE |
| Urothelial proliferation / dysplasia | ✅ Cyclin D1/cdk4 and cyclin E/cdk2 activation in rat urothelium; AA sufficient to induce renal dysplasia in mice (**PMID:23926199**) | MODERATE |
| **Insidious decades-long course** | ❌ Models use high-dose short-course exposure → AKI-to-CKD in weeks | **LOW — the key limitation** |
| **Full UTUC with human driver genes** | ❌ Different driver gene (H-*ras* vs TP53) | LOW |

**Limitations to record explicitly:** the rodent models reproduce **iatrogenic AAN's** dose regimen, not BEN's. They are excellent models of AA nephrotoxicity and of AKI-to-CKD transition; they are poor models of *chronic low-dose environmental* exposure. This is exactly the situation dismech's `HUMAN_MODEL_MISMATCH` discussion kind exists for — evidence exists in the model, but translational validity to the specific human disease (the slow, low-dose form) is the open question.

**Primary applications:** AKI-to-CKD transition mechanisms; nephroprotective drug screening; immune-infiltrate characterization; metabolomic biomarker discovery.

### 15.2 The Hupki (human TP53 knock-in) mouse embryo fibroblast system

The most elegant model for the *carcinogenic* branch, because it solves the species-driver-gene mismatch by putting the human gene in:

> "studying AA-induced TP53 mutagenesis using human TP53 knock-in (Hupki) mouse embryo fibroblasts (HUFs) not only confirmed the TP53 mutation signature of AA in HUFs immortalized after AAI exposure in vitro but also that AAI-treated HUFs share so-called hotspot TP53 mutations observed in UTUC from BEN patients. These findings explain the molecular mechanism whereby AA causes urothelial cancer." (**PMID:31054628**)

Model type: **genetic (knock-in) × in vitro.** Fidelity for the mutational-signature node: **HIGH**. Fidelity for tissue-level urothelial carcinogenesis: LOW (fibroblasts, not urothelium).

### 15.3 In vitro / cellular systems

| System | Use | Source |
|---|---|---|
| **HEK293 stably expressing hOAT1 / hOAT3 / hOAT4** | Established transporter-mediated uptake and its link to adduct formation; probenecid abolished the effect | **PMID:19643159** |
| **Mouse renal cortical slices** | Slice-to-medium ratio >10; probenecid blocked adduct production | **PMID:21546538** |
| **HK-2 human proximal tubule cell line** | EMT, mitochondrial dysfunction, ROS/HMGB1/mtDNA→TLR signaling | **PMID:35765703** |
| **Human renal tubular cells (primary)** | Reproduced the AA mutational signature experimentally | **PMID:23926199** |
| **Human liver–kidney co-culture model** | Elucidated the hepatic-bioactivation → renal-delivery sequence; MRP3/4 efflux | PMID:29202460 |
| **Rat/human liver microsomes** | AAI oxidation/detoxification; inhibition by OTA, Cd, Se ions | cited in AA literature |
| **Xenopus laevis oocytes** | hOAT-mediated trans-stimulation of PAH efflux by AA | **PMID:19643159** |

For dismech, the HEK293-hOAT system is worth a dedicated `experimental_models:` entry with `modeled_mechanisms` → the OAT-uptake pathophysiology node, `relationship: PERTURBS`, `fidelity: HIGH`, and a probenecid `RESCUES` readout.

### 15.4 Genetic models

- **Hupki TP53 knock-in mice** (above)
- **Glycine N-methyltransferase (GNMT) models** — GNMT inhibits AAN by increasing CYP3A44 and decreasing NQO1 expression in female mouse hepatocytes (PMC5934382) — a nice in vivo confirmation of the activation/detoxification balance hypothesis
- **NQO1 knockout** — not verified this session; would be the obvious experiment
- No BEN-specific zebrafish, *Drosophila*, *C. elegans*, or yeast model located
- No BEN-specific iPSC, organoid, or kidney-on-chip model located — a real and rather glaring gap given how well the disease's proximal-tubule selectivity would suit a proximal-tubule-on-chip with OAT expression

### 15.5 Model databases

MGI, RGD (for chemically induced AAN protocols), Cellosaurus (HK-2), IMPC/KOMP (for *Nqo1*, *Slc22a6*, *Slc22a8* alleles). No BEN-specific model repository exists.

---

## Appendix A — Curation notes and honest caveats

Things a downstream curator should know before writing YAML:

1. **The BEN / AAN lumping question is unresolved and consequential** (§1.3–1.4). MONDO treats them as synonyms; the clinical literature treats them as dose-differentiated forms of one etiologic entity. Consider `has_subtypes` or a `Grouping`.
2. **OMIM 124100 is actively misleading on mechanism** (§1.2). Cite it for identity only.
3. **`CHEBI:2825`'s canonical label is "aristolochic acid A", not "aristolochic acid I."** dismech's exact-label rule bites here.
4. **Verified vs unverified ontology IDs.** Every HP, CL, UBERON, ECTO, and NCIT ID given above was resolved against OLS4 in this session **except** where explicitly marked *(not verified)* — notably `GO:0006915`, GO cellular-component terms, macrophage/T-cell CL terms, NCBI Taxonomy IDs, and the NCIT hemodialysis term. Run `just validate-terms` regardless.
5. **The rodent models are models of iatrogenic AAN, not of BEN** (§15.1). Any `animal_models` entry should carry that limitation explicitly, and probably a `HUMAN_MODEL_MISMATCH` discussion.
6. **Negative results worth curating as `REFUTE`:** ochratoxin A as primary cause; herbal-tea use as a BEN risk factor in the Balkans; heavy metals; infectious agents.
7. **The dissent on Pliocene lignite is live, not dead.** Present the consensus rejection, but don't erase the geochemistry literature.
8. **Genuine literature gaps** — say so rather than inventing: BEN-specific QoL instruments; BEN-specific 5-/10-year survival; GBD disability estimates; modern GWAS; single-cell/spatial transcriptomics; organoid or organ-chip models; BEN-specific clinical trials; Orphanet listing.
9. **The SBS22-as-low-risk-subtype finding (PMID:32292497) runs against intuition** and against the general "more mutations = worse" prior. Curate it, but note the tension rather than smoothing it over.

---

## Appendix B — Reference list (PMID-verified)

All titles, years, and journals below were verified against NCBI eSummary/eFetch in this session.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 8094166 | 1993 | Lancet | Rapidly progressive interstitial renal fibrosis in young women: association with slimming regimen including Chinese herbs |
| 7933816 | 1994 | Kidney Int | Chinese herbs nephropathy: a clue to Balkan endemic nephropathy? |
| 8730422 | 1996 | Nephron | Genetic predisposition to Balkan endemic nephropathy |
| 10841870 | 2000 | N Engl J Med | Urothelial carcinoma associated with the use of a Chinese herb (*Aristolochia fangchi*) |
| 12216081 | 2002 | Int J Cancer | Is aristolochic acid a risk factor for Balkan endemic nephropathy-associated urothelial cancer? |
| 17434925 | 2007 | Carcinogenesis | Aristolochic acid mutagenesis: molecular clues to the aetiology of BEN-associated urothelial cancer |
| **17620607** | 2007 | PNAS | **Aristolochic acid and the etiology of endemic (Balkan) nephropathy** |
| 18418355 | 2008 | Kidney Int | Aristolochic acid nephropathy: a worldwide problem |
| 19643159 | 2009 | Toxicology | Molecular evidence for an involvement of organic anion transporters (OATs) in AAN |
| 21546538 | 2011 | J Pharmacol Exp Ther | Physiological and molecular characterization of aristolochic acid transport by the kidney |
| 21613233 | 2011 | Toxicol Sci | Inhibition of renal NQO1 activity by dicoumarol suppresses nitroreduction of AAI |
| 22071594 | 2012 | Kidney Int | Aristolactam-DNA adducts are a biomarker of environmental exposure to aristolochic acid |
| 22116163 | 2012 | Kidney Blood Press Res | Could disappearance of endemic (Balkan) nephropathy be expected in forthcoming decades? |
| 22373701 | 2012 | Kidney Int | Chinese herbs nephropathy and BEN: toward a single entity, aristolochic acid nephropathy |
| 22987305 | 2012 | Environ Mol Mutagen | Evidence of exposure to AA in patients with urothelial cancer from a BEN region of Romania |
| 23238808 | 2013 | Environ Mol Mutagen | Aristolochic acid nephropathy: harbinger of a global iatrogenic disease |
| 23552405 | 2013 | Ann Intern Med | The epidemiology, diagnosis, and management of AAN: a narrative review |
| 23926199 | 2013 | Sci Transl Med | Genome-wide mutational signatures of aristolochic acid and its application as a screening tool |
| 24131581 | 2013 | BMC Nephrol | Whole genome methylation array analysis reveals new aspects in BEN etiology |
| **24166461** | 2014 | Nephrol Dial Transplant | **Consensus statement on screening, diagnosis, classification and treatment of endemic (Balkan) nephropathy** |
| 24949484 | 2014 | Biomed Res Int | NGS nominated CELA1, HSPG2, and KCNK5 as candidate genes for predisposition to BEN |
| 25403517 | 2015 | Int J Cancer | RCCs of CKD patients harbor the mutational signature of carcinogenic aristolochic acid |
| 26657656 | 2016 | Br J Cancer | Aristolochic acid exposure in Romania and implications for renal cell carcinoma |
| 27362729 | 2016 | J Agric Food Chem | Quantitation of aristolochic acids in corn, wheat grain, and soil samples collected in Serbia |
| 28146082 | 2017 | Int J Mol Sci | An integrated view of aristolochic acid nephropathy: update of the literature |
| 30346143 | 2018 | Chem Res Toxicol | Etiology of Balkan endemic nephropathy: an update on aristolochic acids exposure mechanisms |
| **31054628** | 2019 | Semin Nephrol | **Balkan endemic nephropathy and the causative role of aristolochic acid** |
| 32050524 | 2020 | Int J Mol Sci | Aristolochic acid-induced nephrotoxicity: molecular mechanisms and potential protective approaches |
| 32292497 | 2020 | Theranostics | Aristolochic acid mutational signature defines the low-risk subtype in UTUC |
| 34569060 | 2022 | Int J Cancer | Molecular profiles and urinary biomarkers of UTUCs associated with aristolochic acid exposure |
| 35602498 | 2022 | Front Med | Experimental aristolochic acid nephropathy: a relevant model to study AKI-to-CKD transition |
| 35765703 | 2022 | J Cell Mol Med | AAI induces proximal tubule injury through ROS/HMGB1/mtDNA mediated activation of TLRs |
| 37448287 | 2023 | Kidney Res Clin Pract | Overview of aristolochic acid nephropathy: an update |
| 37629712 | 2023 | Medicina (Kaunas) | GPX3 rs8177412 polymorphism modifies risk of upper urothelial tumors in patients with BEN |
| **38693263** | 2024 | Nature | **Geographic variation of mutagenic exposures in kidney cancer genomes** |
| 41289940 | 2026 | *(in press)* | Fasudil targets the RhoA/ROCK-NLRP3 axis to attenuate AA-induced renal pyroptosis |

Already in your local cache: `references_cache/PMID_17620607.md` (abstract) and `references_cache/PMID_31054628.md` (full text, 71 KB — this one is the workhorse; most of the §3–§13 quotes come straight out of it).

---

**Sources (web):**

- [Aristolochic acid and the etiology of endemic (Balkan) nephropathy — PNAS](https://www.pnas.org/doi/full/10.1073/pnas.0701248104)
- [Balkan Endemic Nephropathy and the Causative Role of Aristolochic Acid — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0270929519300130)
- [Consensus statement on screening, diagnosis, classification and treatment of endemic (Balkan) nephropathy — NDT](https://academic.oup.com/ndt/article/29/11/2020/1806798)
- [Geographic variation of mutagenic exposures in kidney cancer genomes — Nature](https://www.nature.com/articles/s41586-024-07368-2) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11111402/)
- [Aristolactam-DNA adducts are a biomarker of environmental exposure to aristolochic acid — Kidney International](https://www.kidney-international.org/article/S0085-2538(15)55338-6/fulltext)
- [Urothelial carcinoma associated with the use of a Chinese herb (Aristolochia fangchi) — NEJM](https://www.nejm.org/doi/full/10.1056/NEJM200006083422301)
- [GPX3 rs8177412 polymorphism modifies risk of upper urothelial tumors in patients with BEN — Medicina/PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10456338/)
- [Overview of aristolochic acid nephropathy: an update — Kidney Res Clin Pract](https://www.krcp-ksn.org/journal/view.php?doi=10.23876%2Fj.krcp.22.211)
- [Experimental aristolochic acid nephropathy: a relevant model to study AKI-to-CKD transition — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9115860/)
- [Molecular evidence for an involvement of organic anion transporters (OATs) in AAN — PubMed](https://pubmed.ncbi.nlm.nih.gov/19643159/)
- [Physiological and molecular characterization of aristolochic acid transport by the kidney — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3141898/)
- [Inhibition of renal NQO1 activity by dicoumarol — Toxicological Sciences](https://academic.oup.com/toxsci/article/122/2/288/1680920)
- [NGS nominated CELA1, HSPG2, and KCNK5 as candidate genes for predisposition to BEN — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4052113/)
- [Whole genome methylation array analysis reveals new aspects in BEN etiology — BMC Nephrology](https://link.springer.com/article/10.1186/1471-2369-14-225)
- [Aristolochic acid exposure in Romania and implications for renal cell carcinoma — Br J Cancer](https://www.nature.com/articles/bjc2015402)
- [Aristolochic acid mutational signature defines the low-risk subtype in UTUC — Theranostics](https://www.thno.org/v10p4323.htm)
- [The etiology of Balkan endemic nephropathy: still more questions than answers — EHP/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1533478/)
- [A possible link between BEN and leaching of toxic organic compounds from Pliocene lignite — USGS](https://usgs.gov/publications/possible-link-between-balkan-endemic-nephropathy-and-leaching-toxic-organic-compounds)
- [Balkan endemic nephropathy: an update on its aetiology — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5065591/)
- [Aristolochic acid–associated cancers: a public health risk in need of global action — IARC](https://www.iarc.who.int/news-events/aristolochic-acid-associated-cancers-a-public-health-risk-in-need-of-global-action/)
- [Plants containing aristolochic acid — IARC Monographs / NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK304331/)
- [OMIM Entry 124100 — Danubian endemic familial nephropathy](https://omim.org/entry/124100)
- [AAI induces proximal tubule injury through ROS/HMGB1/mtDNA mediated activation of TLRs — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9345294/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 33 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 42 |
| On topic | 28 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:31054628`: "In 1969, Ivic had suggested that the latter, occurring in certain villages throughout the Danube Valley, might be caused by the chronic ingestion of the seeds of the Aristolochia clematitis, a common plant growing in the wheat fields of these endemic regions."
  - closest text in source: "1,4 In 1969, Ivic had suggested that the latter, occurring in certain villages throughout the Danube V alley, might be caused by the chronic ingestion of the seeds of the Aristolochia clematitis, a common plant growing in the wheat fields of these endemic regions"
- `PMID:24166461` *(abstract only)*: "Patients with established BEN should be treated like other CKD patients, with peritoneal dialysis, hemodialysis or renal transplantation in ESRD stage."
  - closest text in source: "National medical providers should cover costs of screening and diagnostic procedures and treatment of EN patients with or without upper urothelial cancers."
- `PMID:31054628`: "Already ten years before, Martinčić and Dumić had reported horse poisoning with Aristolochia clematitis and found strict similarities in epidemiology, clinic, laboratory data and renal pathology between horses and BEN."
  - closest text in source: "Already ten years before, Martin čić and Dumi ć had reported horse poisoning with Aristolochia clematitis and found strict 10 similarities in epidemiology, clinic, laboratory data and renal pathology between horses and BEN"
- `PMID:31054628`: "studying AA-induced TP53 mutagenesis using human TP53 knock-in (Hupki) mouse embryo fibroblasts (HUFs) not only confirmed the TP53 mutation signature of AA in HUFs immortalized after AAI exposure in vitro but also that AAI-treated HUFs share so-called hotspot TP53 mutations observed in UTUC from BEN patients. These findings explain the molecular mechanism whereby AA causes urothelial cancer."
  - closest text in source: "56 Further, studying AA-induced TP53 mutagenesis using human TP53 knock-in (Hupki) mouse embryo fibroblasts (HUFs) not only confirmed the TP53 mutation signature of AA in HUFs immortalized after AAI exposure in vitro 58 but also that AAI-treated HUFs share so-called hotspot TP53 mutations observed in UTUC from BEN patients.59 These findings explain the molecular mechanism whereby AA causes urothelial cancer.49 (Figure 2)"
