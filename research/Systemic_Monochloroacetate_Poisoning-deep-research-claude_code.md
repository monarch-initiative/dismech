---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8
cached: false
start_time: '2026-10-22T10:14:42.618916'
end_time: '2026-10-22T10:20:01.761759'
duration_seconds: 319.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Systemic Monochloroacetate Poisoning
  mondo_id: MONDO:0019545
  category: Environmental
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: monochloroacetic acid poisoning; chloroacetic acid poisoning; MCA poisoning;
    MCAA poisoning
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
  - claude-haiku-5-5
  - claude-opus-4-8
  web_search_requests: 6
  num_turns: 16
  total_cost_usd: 2.6815124999999997
  session_id: 41bb791e-529b-4f1d-b0a6-e3c7daed605c
  stop_reason: end_turn
  assistant_text_blocks: 6
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Systemic Monochloroacetate Poisoning
- **MONDO ID:** MONDO:0019545 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** monochloroacetic acid poisoning; chloroacetic acid poisoning; MCA poisoning; MCAA poisoning
- **Category:** Environmental

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Systemic Monochloroacetate Poisoning** covering all of the
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

ok so this one's a toxicology deep-dive, not a gene thing. first paragraph note up front: **there is no causal gene** — "monochloroacetate poisoning" is environmental/chemical toxicity from monochloroacetic acid (MCAA / chloroacetic acid, CHEBI:28862), so the "causal gene(s): not recorded" line is correct and MONDO:0019545 is a poisoning concept, not a Mendelian one. let me go actually search this instead of trusting memory. loading the web tools first.

ok tools loaded. running a batch of searches in parallel — mechanism, clinical case reports, treatment/antidote, toxicokinetics.

solid hits. now pulling the primary sources for exact quotes — the human case reports, the mechanism papers, and the big ECETOC human-intoxication review.

pubmed blocks the fetcher (cookie wall) but the PMC case came through rich. switching to NCBI eutils for the clean abstracts, and grabbing the ECETOC human-intoxication review pdf.

enough primary sourcing to write it well. one last pair — the experimental dermal-exposure animal study and the chemical identifiers (CAS/ChEBI/ICD/MeSH) — then i'll write the full report.

ok so i've got the sourcing i need. here's the full report, Claude. one thing up top: don't make stuff up — i've marked every place where the mechanism is animal/in-vitro rather than human, and where sources disagree (the BSA threshold and the exact enzyme target both do). couldn't pull the PubMed abstracts raw (cookie wall) so a couple of PMIDs i'm citing from eutils/secondary and have flagged as needing a verbatim snippet pull before they go into the KB.

---

# Systemic Monochloroacetate Poisoning — Research Report

## 0. Orientation (read this first)

**There is no causal gene.** "Systemic Monochloroacetate Poisoning" (MONDO:0019545) is an acute **chemical toxidrome**, not a Mendelian disease — the "causal gene(s): not recorded" and "OMIM: not recorded" lines in the template are correct and should stay empty. The etiologic agent is **monochloroacetic acid** (MCAA; chloroacetic acid; the conjugate base is monochloroacetate / chloroacetate), a small corrosive haloacetic acid used industrially. The entry belongs in the **Environmental** category, and its pathophysiology is driven by chemical absorption → metabolic-enzyme inactivation, not by any host variant. Everything below is organized around that.

---

## 1. Disease Information

**Overview.** Systemic monochloroacetate poisoning is acute, often fatal, multi-organ intoxication following absorption of monochloroacetic acid — most characteristically through the **skin** after an industrial splash, but also by ingestion or inhalation. The agent is doubly dangerous: it is **corrosive** (a chemical burn at the contact site) *and* a **systemic metabolic poison** (it shuts down cellular energy production). The hallmark is that a seemingly survivable skin burn is followed, 1–3.5 hours later, by lethal systemic collapse — severe metabolic (lactic) acidosis, hypoglycemia, cardiac failure, coma, and death within hours to a few days.

**Chemical identifiers (the agent):**
- **CAS:** 79-11-8
- **ChEBI:** chloroacetic acid = **CHEBI:27869** (the conjugate base chloroacetate is a separate CHEBI id; *verify both with OAK before binding — these came from a web source, not a lookup*)
- **PubChem CID:** 300; **KEGG:** C06755 / D07677; **EC (EINECS):** 201-178-4; **InChIKey:** FOCAUTSVDIKZOP-UHFFFAOYSA-N
- **Sodium salt:** sodium monochloroacetate (IPCS ICSC 1449)

**Disease/condition identifiers:**
- **MONDO:** MONDO:0019545 (as given)
- **ICD-10:** no chemical-specific code; maps to **T54.2** (toxic effect of corrosive acids and acid-like substances) for the corrosive injury, plus the systemic poisoning code. ICD-11 would use the corrosive-substance toxicity category. *(No source gave a chemical-specific code; flag as approximate.)*
- **MeSH:** indexed under chloroacetates / "chloroacetic acid" (no dedicated poisoning descriptor found).
- **Orphanet:** not a rare-disease entity; no ORPHA code expected.

**Synonyms:** monochloroacetic acid poisoning, monochloroacetic acid (MCA/MCAA) intoxication, chloroacetic acid poisoning, chloroethanoic acid poisoning, sodium monochloroacetate (SMCA) poisoning.

**Data provenance:** aggregated from **disease-level** toxicology reviews (ECETOC, WHO, EU CSTEE, IPCS) and a small set of **individual human case reports** — there is no registry or EHR cohort; the human evidence base is ~40 cases total.

---

## 2. Etiology

**Primary cause (environmental/chemical).** Exposure to monochloroacetic acid or its sodium salt. Not genetic, not infectious. The ECETOC human-intoxication review tallies **41 systemic poisonings from dermal exposure, 26 of them fatal**, and notes that in 5 of the 6 best-documented fatalities **≥10% of body surface area** was contaminated.

**Risk factors — environmental/occupational (the only ones that apply):**
- **Occupational handling** is the dominant setting. The EU CSTEE opinion states exposure is "mainly occupational, during production, synthesis, and paint-remover formulation or use." Industrial uses: synthesis of carboxymethylcellulose, glycine, thioglycolic acid, herbicides (e.g., 2,4-D), dyes, and pharmaceuticals; also wart/callus removers and tissue fixatives.
- **Large contaminated skin area.** The single most important determinant of a fatal outcome. Thresholds reported vary by source — a supplier TDS says fatal when **>10% BSA**; LOINC chemical info says **>6%**; the Tao 2020 case discussion says **"Contamination of more than 5% of the skin can cause poisoning and even death."** (These numbers are secondary/consensus statements, not derived from a controlled study — carry them with that caveat.)
- **High concentration** of the solution and **delayed/inadequate decontamination**.
- **Route:** dermal ≫ oral/inhalation for reported systemic cases, though a fatal **oral** case is documented (Rogers 1995).

**Genetic risk/protective factors:** none established. **No susceptibility loci, modifier genes, or protective alleles** are known — appropriate to leave blank.

**Protective factors (environmental):** prompt copious decontamination (water, then dilute sodium bicarbonate), limiting contaminated BSA, PPE. **Gene-environment interactions:** none described.

---

## 3. Phenotypes

Human phenotype data come from case reports (Kulling 1992, PMID **1433433**; Rogers 1995, PMID **7572862**; Tao 2020, PMID **32975103**). Onset of **systemic** features is characteristically **delayed 1–3.5 h** after exposure; the local burn is immediate.

| Phenotype | Type | Onset / course | Suggested HP term |
|---|---|---|---|
| Chemical/corrosive skin burn (1st–3rd degree) at contact site | Physical manifestation | Immediate; local | HP:0100699 (Chemical burn) — *verify* |
| Metabolic (lactic) acidosis | Lab abnormality | Hours; progressive, often refractory | HP:0001942 (Metabolic acidosis); HP:0003141 (Increased lactate / lactic acidosis) |
| Hypoglycemia | Lab abnormality | Hours | HP:0001943 (Hypoglycemia) |
| Depressed consciousness → coma | Neuro sign | 1–3.5 h; progressive | HP:0001259 (Coma); HP:0001252/lethargy |
| Seizures / convulsions | Neuro sign | Variable | HP:0001250 (Seizure) |
| Cerebral edema (→ herniation) | Clinical/imaging | Days; terminal in fatal cases | HP:0002181 (Cerebral edema) |
| Cardiac failure / arrhythmia / cardiac arrest | Clinical sign | Hours | HP:0001635 (Congestive heart failure); HP:0011675 (Arrhythmia) |
| Dyspnea / hypoxemia / acute lung injury / pulmonary edema | Respiratory | ~2.5 h (Tao case) | HP:0002094 (Dyspnea); HP:0100598 (Pulmonary edema) |
| Rhabdomyolysis | Lab/clinical | Hours–days | HP:0003201 (Rhabdomyolysis) |
| Acute kidney injury / renal failure | Clinical | Hours–days | HP:0001919 (Acute kidney injury) |
| Hyperthermia | Sign | Variable | HP:0001945 (Fever/hyperthermia) |
| Hepatic injury (↑AST/ALT, fatty change) | Lab/path | Hours–days | HP:0002910 (Elevated transaminases) |
| Shock | Clinical | Late | HP:0031273 (Shock) — *verify* |

**Severity/frequency:** when systemic poisoning develops after a large exposure it is **severe and frequently fatal** (26/41 dermal systemic cases fatal per ECETOC). **Progression:** rapid and often relentless once acidosis/coma set in. **QoL:** for survivors (e.g., Tao 2020), morbidity is dominated by the burn wound (debridement, grafting) rather than lasting systemic sequelae; that single survivor's follow-up labs normalized.

*(All HP ids above are suggestions — run them through OAK/`just validate-terms` before binding; several may need remapping to the closest existing HPO term.)*

---

## 4. Genetic / Molecular Information

**Not applicable.** No causal genes, pathogenic variants, modifier genes, epigenetic signatures, or chromosomal abnormalities — this is a chemical exposure. The relevant "molecular targets" are **host metabolic enzymes that MCA inactivates** (covered in §6), not mutated genes. Leave all genetic slots empty; do **not** manufacture a gene binding.

---

## 5. Environmental Information

- **Environmental/toxic agent:** monochloroacetic acid / sodium monochloroacetate (CAS 79-11-8). Corrosive, water-soluble, dermally absorbed. Suggested exposure anchoring: an **ECTO** "exposure to chloroacetic acid / haloacetic acid" term if one exists — *search ECTO with OAK (`l~chloroacet`, `l~haloacet`); do not assume one exists, and record the search in `notes` if none does.* CHEBI for the agent: **CHEBI:27869**.
- **Lifestyle factors:** none relevant (acute occupational/accidental toxicity).
- **Infectious agents:** none.
- **Environmental (low-dose) note:** MCAA is also a **chlorination disinfection by-product** in drinking water, which is why a WHO drinking-water background document exists — but that concerns chronic low-level exposure and is **not** the acute poisoning this entry describes. Keep them distinct.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical death)

1. **Concentrated MCAA contacts skin (or is ingested)** → **local corrosive injury**: first-to-second, sometimes third-degree chemical burn. *(Human; demonstrated.)*
2. **Once a large area (~≥5–10% BSA) is contaminated, MCA is rapidly absorbed through intact skin and distributed systemically**, with systemic signs appearing **1–3.5 h** later. *(Human case/review inference; plasma level at 4 h in Kulling 1992 confirms transdermal uptake.)*
3. **Intracellularly, MCA — a reactive, sulfhydryl-alkylating haloacetate — inactivates thiol-dependent metabolic enzymes.** The specific target is **disputed**:
   - **GAPDH** (glyceraldehyde-3-phosphate dehydrogenase): Sakai et al. 2005 (PMID **15720133**), isolated perfused rat liver, found MCA **inactivates GAPDH (to ~19% of control)** and that **aconitase was *not* inhibited**, overturning the earlier assumption. *(In vitro/ex vivo, animal.)*
   - **Pyruvate dehydrogenase (PDH) and α-ketoglutarate dehydrogenase (α-KGDH):** rat heart mitochondria studies report inhibition, via oxalate and/or direct SH-alkylation. *(Animal/in vitro.)*
   - **Aconitase:** historically proposed ("MCA enters the TCA cycle and inhibits aconitase") but **refuted** by Sakai 2005 — note the disagreement explicitly in the entry rather than asserting aconitase.
4. **Enzyme blockade throttles glycolysis, the TCA cycle, and gluconeogenesis** →
   - **branch A:** impaired aerobic ATP production in **high-energy-demand tissues (heart, CNS, skeletal muscle)** → cell injury;
   - **branch B:** GAPDH/gluconeogenesis block → **severe hypoglycemia**;
   - **branch C:** pyruvate cannot enter the TCA cycle → **lactate accumulation → profound lactic/metabolic acidosis** (Dartsch et al. 2000 show ↑lactate + ↑pyruvate and ultrastructural/cytoskeletal damage in cultured kidney and liver epithelial cells — *in vitro, animal/cell*).
5. **Multi-organ failure:** cardiac failure/arrhythmia, CNS depression → coma/seizures → **cerebral edema**, rhabdomyolysis, **acute kidney injury**, **acute lung injury/pulmonary edema** (Kato & Dote 2006, subcutaneous rat model: lethal acute lung injury + hypoglycemia — *animal*), hepatic injury, hyperthermia.
6. **Death** within **hours to ~8 days** — in Kulling 1992 the patient died on **day 8 of brain herniation** after refractory acidosis, rhabdomyolysis, renal failure, and cerebral edema; other cases die within hours of cardiac arrest or refractory shock/acidosis. The ECETOC review and Toshina/Dote 2004 both note the **exact cause of death remains poorly understood**.

### Checklist coverage
- **Molecular pathways:** glycolysis (GO:0006096), TCA/citric acid cycle (GO:0006099), gluconeogenesis (GO:0006094), ATP biosynthesis (GO:0006754). Enzyme activities: GAPDH NAD+ activity (GO:0004365), pyruvate dehydrogenase activity, α-ketoglutarate dehydrogenase activity. *(verify GO ids in OAK.)*
- **Protein dysfunction:** covalent **alkylation of catalytic/structural cysteine thiols** → loss of function of GAPDH/PDH/α-KGDH. Mechanism is **enzyme inactivation**, not misfolding/aggregation.
- **Metabolic changes:** blocked carbohydrate energy metabolism; lactate↑, pyruvate↑, glucose↓.
- **Cellular processes:** energy-failure cell injury/necrosis; cytoskeletal disruption (Dartsch 2000).
- **Immune involvement:** none primary (burn-wound infection/aspiration pneumonia are secondary complications, as in Tao 2020).
- **Tissue damage mechanism:** metabolic (ATP depletion) + corrosive (local) + oxidative/energy-deprivation necrosis.

### Suggested CL / UBERON for pathograph nodes
- **Cell types (CL):** cardiomyocyte (CL:0000746), hepatocyte (CL:0000182), skeletal muscle cell, neuron, kidney epithelial cell. *(verify.)*
- **Anatomy (UBERON):** skin (UBERON:0002097), heart, brain, kidney, liver, lung, skeletal muscle.

---

## 7. Anatomical Structures Affected

- **Primary (contact):** skin (UBERON:0002097) — corrosive burn, local.
- **Primary systemic targets (high energy demand):** heart (UBERON:0000948), brain/CNS (UBERON:0000955), skeletal muscle (UBERON:0001134).
- **Secondary involvement:** kidney (UBERON:0002113; AKI, rhabdomyolysis-related), liver (UBERON:0002107; fatty change, transaminitis), lung (UBERON:0002048; acute lung injury/edema, aspiration pneumonia), GI (diffuse gastric erosions at autopsy).
- **Body systems:** integumentary, cardiovascular, nervous, renal, respiratory, musculoskeletal, hepatic/metabolic.
- **Subcellular (GO cellular component):** **mitochondrion** (GO:0005739) and **cytosol** (GO:0005829) — where the blocked enzymes act; cytoskeleton (Dartsch).
- **Localization/laterality:** burn is at the splash site (asymmetric/focal); systemic effects are, by definition, systemic/bilateral.

---

## 8. Temporal Development

- **Onset:** acute. Local burn **immediate**; **systemic signs 1–3.5 h** post-exposure (occasionally later even when the burn looked mild).
- **Progression:** rapid, often relentless once acidosis/coma begin.
- **Stages (functional):** (i) corrosive injury → (ii) latent/pre-systemic interval (~1–3.5 h) → (iii) systemic metabolic crisis (acidosis, hypoglycemia, cardiac/CNS failure) → (iv) multi-organ failure/death, **or** (rarely) recovery with supportive care.
- **Duration/outcome window:** death **within hours to ~8 days**; survivors' systemic derangements resolve over days–weeks, leaving burn-wound morbidity.
- **Critical intervention window:** the **pre-systemic interval** — immediate decontamination and early supportive/antidotal care before acidosis is entrenched. This is the single actionable window.

---

## 9. Inheritance and Population

- **Inheritance:** **none** — not heritable. No penetrance/expressivity/anticipation/mosaicism/founder/consanguinity/carrier-frequency concepts apply. Leave blank.
- **Epidemiology:** no true prevalence/incidence — this is a sporadic accidental/occupational event. The entire well-documented human literature is **~41 dermal systemic cases (26 fatal)** plus scattered oral/other reports. For a `Prevalence` record, the honest encoding is **`measure_type: CASES_IN_LITERATURE`** with `prevalence_class` qualitative (e.g., ULTRA_RARE as a reported clinical event) and the ECETOC tally in `notes` — do **not** invent a rate_per_100000.
- **Demographics:** predominantly **working-age adults** in chemical manufacturing/handling; **male-predominant** by occupational exposure pattern (no formal sex ratio reported). **Geography:** wherever MCAA is produced/used (industrial settings worldwide; documented cases from Europe, Japan, China).

---

## 10. Diagnostics

Diagnosis is **clinical/circumstantial** (known exposure + characteristic delayed systemic crisis), supported by labs. There are **no validated diagnostic criteria or biomarkers**.

- **Laboratory:** arterial blood gas (**metabolic/lactic acidosis** — the key finding), **lactate** (↑), **glucose** (↓, often markedly), electrolytes/anion gap, **creatine kinase** (rhabdomyolysis), **renal function** (AKI), **transaminases** (hepatic injury), troponin (cardiac). Suggested LOINC anchors: lactate (LOINC 2524-7), glucose, blood pH — *verify/seed per the LOINC workflow if any are bound*.
- **Toxicological confirmation:** **plasma/serum monochloroacetate** measurement (GC/LC-MS); Kulling 1992 measured a plasma level 4 h post-exposure confirming absorption; one review cites post-mortem serum up to **~100 µg/mL**. Specialized assay, not routinely available.
- **Imaging:** CT head (cerebral edema), CXR/CT chest (pulmonary edema, aspiration pneumonia).
- **Electrophysiology:** ECG (arrhythmia); EEG if encephalopathic.
- **Histopathology (autopsy):** diffuse gastric erosions, fatty infiltration of the liver, pulmonary and cerebral edema.
- **Genetic/omics testing:** **not applicable.**
- **Differential diagnosis:** other causes of acute high-anion-gap lactic acidosis with coma (other corrosive-acid burns with systemic toxicity, cyanide, salicylates, metformin-associated lactic acidosis, sepsis, toxic alcohols). The **distinguishing feature** is the exposure history + the corrosive burn + delayed metabolic collapse with hypoglycemia.
- **Screening:** not applicable (acute accidental exposure); relevant "screening" is occupational-hygiene monitoring, not clinical.

---

## 11. Outcome / Prognosis

- **Mortality:** high once systemic poisoning develops — **26/41 (≈63%)** of documented dermal systemic cases were fatal (ECETOC). Survival is the exception and is tied to small contaminated area + rapid aggressive care (Tao 2020 survived a 10% third-degree burn with CVVH, bicarbonate, steroids, grafting).
- **Prognostic factors:** **% BSA contaminated** (dominant), concentration, speed of decontamination, depth/refractoriness of **acidosis** and **hypoglycemia**, onset of coma/cerebral edema, and access to extracorporeal support/antidote.
- **Complications:** refractory lactic acidosis, cerebral edema/herniation, cardiac arrest, AKI (rhabdomyolysis), acute lung injury, aspiration pneumonia, extensive burn wounds.
- **Recovery:** survivors can normalize systemic labs (Tao 2020 follow-up normal) with residual burn-wound morbidity. No validated QoL instrument data exist for this entity.

---

## 12. Treatment

**No proven specific antidote is licensed in most countries; management is decontamination + aggressive supportive care, with dichloroacetate as the candidate antidote.**

- **Immediate decontamination (primary):** remove clothing, copious water irrigation, then **dilute sodium bicarbonate** lavage of skin/eyes (Tao 2020 used 4% NaHCO₃; the Chinese chloroacetyl-chloride case used 5%). NCIT: *Decontamination* / supportive-care terms.
- **Correct acidosis:** IV **sodium bicarbonate**; NCIT treatment = Pharmacotherapy (`NCIT:C15986`) + therapeutic_agent sodium bicarbonate (CHEBI). **Correct hypoglycemia:** IV glucose — and animal data suggest glucose is partly protective (10% glucose infusion gave ~79% 10-h survival in a rat lethal-dose model; octreotide + oral glucose improved 14-day survival).
- **Candidate antidote — dichloroacetate (DCA):** the most consistently effective agent in rodents ("dichloroacetate, and to a lesser degree phenobarbitone… reduced mortality and decreased lactate accumulation in blood and CSF of rats and mice"). **Approved in Sweden** as an antidote for life-threatening MCAA poisoning; **not FDA-approved** in the US. An informal regimen (50 mg/kg IV over 10 min, repeat at 2 h, dose doubled if hemodialyzed) circulates but is **not a validated clinical guideline — do not treat it as one.** *(Evidence: animal + reference documents; human efficacy not established.)*
- **Ineffective antidotes:** glycerol monoacetate and ethanol were tested and **did not work** — worth recording as a negative to prevent re-nomination.
- **Extracorporeal support:** **CVVH / hemodialysis** (Tao 2020) — both organ support and possible enhanced elimination. NCIT: hemofiltration/hemodialysis procedure terms.
- **Organ/supportive:** mechanical ventilation, vasopressors, seizure control, cerebral-edema management; **burn care** — debridement, negative-pressure wound therapy, **skin grafting** (NCIT: Surgical Procedure `NCIT:C15329`; skin graft term); corticosteroids were used in Tao 2020 (methylprednisolone pulse) though not evidence-based for the systemic toxin itself.
- **Experimental/trials:** no registered clinical trials (sporadic poisoning); evidence is bench/animal + case reports.
- **Pharmacogenomics / targeted / cell / gene / RNA therapy:** **not applicable.**

---

## 13. Prevention

- **Primary (the real lever):** occupational controls — engineering containment, closed handling, chemical-resistant PPE, splash protection, immediate-access emergency showers/eyewash, worker training on the **delayed systemic risk** (a "minor" burn can kill). EU/IPCS hazard communication; ICSC 1449 stresses that specific antidotal treatment should be **available on site**.
- **Secondary:** rapid on-site decontamination protocols; low threshold for hospital observation of any sizeable MCAA skin contact through the pre-systemic window.
- **Tertiary:** aggressive ICU support to prevent progression to multi-organ failure.
- **Environmental (separate issue):** drinking-water disinfection-by-product limits (WHO) — chronic, not acute.
- **Not applicable:** immunization, genetic/carrier screening, PGD, genetic counseling.

---

## 14. Other Species / Natural Disease

- **No natural disease.** This is a toxic exposure, not a spontaneous animal disease — **OMIA has no entry**, and there is no breed predisposition. MCAA is acutely toxic to mammals generally (it is also used as a herbicide intermediate).
- **Taxonomy of experimental species:** rat (*Rattus norvegicus*, NCBITaxon:10116), mouse (*Mus musculus*, NCBITaxon:10090), guinea pig — all as **induced toxicity models**, below.
- **Zoonotic/cross-species transmission:** not applicable (chemical).

---

## 15. Model Organisms

All models are **induced (chemical-dosing)**, not genetic — appropriate for an `animal_models:` block with `modeled_mechanisms` linking to the metabolic-acidosis / energy-failure pathograph nodes.

- **Rat, subcutaneous MCA (Dote/Kato/Toshina group):**
  - Toshina & Dote 2004 (*Environ Health Prev Med* 9(2):58): fasting rats, subcutaneous MCA → hepatic injury, AST/ALT ~1.5× control; "little is known about the cause of death." *(MODEL_ORGANISM.)*
  - **Kato & Dote 2006** (*Toxicol Ind Health*; DOI 10.1191/0748233706th261oa): subcutaneous MCA → **lethal acute lung injury and hypoglycemia**. *(MODEL_ORGANISM — pull a verbatim abstract snippet before citing in the KB; PubMed was behind a cookie wall for me.)*
  - Glucose/octreotide antidote studies (rat lethal-dose): **10% glucose infusion → ~79% survival at 10 h**; octreotide + oral glucose improved 14-day survival (0.90 vs 0.35 control). *(MODEL_ORGANISM — antidote proof-of-concept.)*
- **Rat heart mitochondria (ex vivo):** PDH and α-KGDH inhibition. *(IN_VITRO.)*
- **Isolated perfused rat liver — Sakai 2005 (PMID 15720133):** GAPDH inactivation (~19% control), aconitase *not* inhibited; the key mechanistic model. *(IN_VITRO/ex vivo.)*
- **Cultured kidney + liver epithelial cells — Dartsch 2000 (*Toxicol Ind Health*):** sodium monochloroacetate → ↑lactate, ↑pyruvate, ultrastructural + cytoskeletal alterations. *(IN_VITRO — PMID needs confirming via a clean lookup.)*
- **Guinea pig experimental dermal exposure:** reproduced skin injury + systemic effects, with systemic signs developing ~1–3.5 h post-exposure (matches the human latent interval). *(MODEL_ORGANISM.)*

**Recapitulation / limitations:** the rodent models reproduce the **hypoglycemia + lactic acidosis + energy-failure** core and the **delayed-onset** pattern well, and are the basis for the DCA/glucose antidote rationale. They **under-represent** the human corrosive-burn-plus-BSA-threshold dynamics (route differs: subcutaneous/IP dosing bypasses the transdermal absorption step), so a `modeled_mechanisms` link to the **systemic metabolic** nodes is well-supported while a link to the **cutaneous corrosive** node is not. Record that as a `fidelity`/`limitations` caveat.

---

## Evidence anchor list (for the KB, with the snippet-verification status)

| PMID / id | Claim it supports | evidence_source | status |
|---|---|---|---|
| **1433433** (Kulling 1992, *J Toxicol Clin Toxicol*) | Human fatal dermal case; TCA-block + SH-reaction hypothesis; died day 8, cerebral herniation | HUMAN_CLINICAL | need verbatim snippet (PubMed cookie-walled) |
| **7572862** (Rogers 1995, *Am J Forensic Med Pathol*) | Accidental fatal poisoning; first documented fatal *oral* case | HUMAN_CLINICAL | need verbatim snippet |
| **15720133** (Sakai 2005, *Chem Res Toxicol*) | MCA inactivates **GAPDH**, **not aconitase**; hypoglycemia + lactic acidosis | IN_VITRO | abstract summarized via eutils; pull exact quote |
| **32975103 / PMC7968492** (Tao 2020, *Arh Hig Rada Toksikol*) | 10% 3°-burn survivor; systemic sx at 2.5 h; CVVH/bicarb/graft; DCA approved in Sweden | HUMAN_CLINICAL | **verbatim quotes captured** (see §6, §12) |
| Kato & Dote 2006 (*Toxicol Ind Health*, DOI 10.1191/0748233706th261oa) | Subcut rat: lethal acute lung injury + hypoglycemia | MODEL_ORGANISM | need snippet (DOI/abstract) |
| Dartsch 2000 (*Toxicol Ind Health*) | ↑lactate/pyruvate + cytoskeletal damage, kidney/liver cells | IN_VITRO | need PMID + snippet |
| ECETOC TR-081 | 41 dermal systemic cases, 26 fatal; ≥10% BSA in 5/6 fatalities | OTHER (review) | numbers from secondary; verify against the PDF |

**Three things to do before this goes into `kb/disorders/Systemic_Monochloroacetate_Poisoning.yaml`:** (1) pull **verbatim** snippets for every PMID above except Tao 2020 — the PubMed cookie wall stopped me getting raw abstract text, so i only have eutils/secondary summaries for most, and the project rule is exact-quote-or-nothing; (2) **OAK-verify every CURIE** I suggested (CHEBI/HP/GO/CL/UBERON/NCIT ids are leads, written from web sources or memory, not lookups — exactly the thing CLAUDE.md says never to trust); (3) decide the lump/split and granularity — this is a single pathogen-free chemical toxidrome, so one `Disease` entry is right, and the shared energy-failure mechanism could later `conforms_to` a metabolic-poisoning module if one exists.

---

## Sources

- [ECETOC TR-081 — Human Acute Intoxication from Monochloroacetic Acid](https://www.ecetoc.org/wp-content/uploads/2021/10/ECETOC-TR-081.pdf)
- [Kulling et al. 1992 — Fatal systemic poisoning after skin exposure to MCA (PMID 1433433)](https://pubmed.ncbi.nlm.nih.gov/1433433/)
- [Rogers 1995 — Accidental fatal monochloroacetic acid poisoning (PMID 7572862)](https://pubmed.ncbi.nlm.nih.gov/7572862/)
- [Sakai et al. 2005 — MCA inhibits gluconeogenesis via GAPDH inactivation (PMID 15720133)](https://pubmed.ncbi.nlm.nih.gov/15720133/)
- [Tao, Liu, Jian 2020 — Skin burns from an MCA leak in a chemical plant (PMC7968492 / PMID 32975103)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7968492/)
- [Kato & Dote 2006 — Lethal acute lung injury and hypoglycemia after subcutaneous MCA (DOI)](https://doi.org/10.1191/0748233706th261oa)
- [Dartsch et al. 2000 — Sodium monochloroacetate cytotoxicity in kidney/liver cells (DOI)](https://doi.org/10.1191/096032700678815693)
- [Toshina/Dote group 2004 — Hepatic injury and gluconeogenesis after subcutaneous MCA (Environ Health Prev Med)](https://www.jstage.jst.go.jp/article/ehpm/9/2/9_2_58/_article/-char/ja/)
- [WHO — Monochloroacetic Acid in Drinking-water background document](https://cdn.who.int/media/docs/default-source/wash-documents/wash-chemicals/monochloroaceticacid.pdf?sfvrsn=90baad6a_4)
- [EU CSTEE opinion on monochloroacetic acid](https://ec.europa.eu/health/archive/ph_risk/committees/sct/documents/out190_en.pdf)
- [Umweltbundesamt — MCAA assessment/reference list](https://www.umweltbundesamt.de/system/files/medien/515/dokumente/mcaa.pdf)
- [IPCS ICSC 1449 — Sodium chloroacetate (antidote/first-aid guidance)](https://www.inchem.org/documents/icsc/icsc/eics1449.htm)
- [Occupational poisoning from a chloroacetyl chloride leak, Jinan 2023 (PMC10427855)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10427855/)
- [Wikipedia — Chloroacetic acid (identifiers: CAS 79-11-8, ChEBI, KEGG, PubChem)](https://en.wikipedia.org/wiki/Chloroacetic_acid)
- [EPA IRIS/NAS review — Monochloroacetic acid (2009)](https://19january2021snapshot.epa.gov/sites/static/files/2014-09/documents/monochloroacetic_acid_final_volume7_2009.pdf)

---

ok that's the report, Claude. it's complete as a research synthesis but i have **not** committed anything or touched the untracked `kb/disorders/Systemic_Monochloroacetate_Poisoning.yaml` sitting in your worktree — writing/validating the actual entry is a separate step and i'd want your y/n before i start editing KB files. haven't actually run any `just` validation this turn either, so treat the ontology ids as leads, not verified bindings. want me to go build the entry from this next?

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
