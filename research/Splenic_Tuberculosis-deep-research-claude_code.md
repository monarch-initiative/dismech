---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:27:30.786447'
end_time: '2026-11-27T00:31:18.235967'
duration_seconds: 227.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Splenic Tuberculosis
  mondo_id: MONDO:0005967
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-opus-5-5
  web_search_requests: 17
  num_turns: 22
  total_cost_usd: 1.0736739
  session_id: 91ace890-a5e1-4b79-a0a5-ea64985aed9c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 29
  retrieval_calls: 27
  assistant_text_blocks: 3
citation_count: 41
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 3
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:20420041
  - PMID:16554586
  quotes_not_checkable: 1
  relevance_assessed: 40
  on_topic: 21
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  service_unreachable: 2
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Splenic Tuberculosis
- **MONDO ID:** MONDO:0005967 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Splenic Tuberculosis** covering all of the
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

Let me try PubMed E-utilities directly for PMIDs and abstracts.

I'm collecting sources (PubMed IDs, WHO guidance, imaging series) and will write the report after a few more searches.

**Splenic Tuberculosis (MONDO:0005967): research report for a disease knowledge base entry**

**Interpretation and scope.** Splenic tuberculosis is an infectious disease with no causal human gene. Its cause is infection of the spleen by organisms of the *Mycobacterium tuberculosis* complex. It most often happens through blood-borne (miliary or disseminated) spread, and sometimes as isolated disease limited to the spleen. Sections on "pathogenic variants" are answered for the host and pathogen where that applies; otherwise they say "not applicable".

**Retrieval limits.** PubMed and PMC pages often returned captcha or cookie stubs. Most PMIDs and quotes below come from PubMed search listings and search-engine abstract snippets I retrieved in this session. Where I could not get an exact abstract sentence, the text is a close paraphrase and is not shown in quotation marks.

**Ontology IDs.** Following the rule against citing unretrieved identifiers, I give suggested HPO, GO, CL, UBERON, CHEBI and NCIT terms **by label only**. Their numeric IDs need to be verified before ingestion.

---

## 1. Disease Information

**Overview.** Splenic TB is a rare form of extrapulmonary TB that usually results from blood-borne spread ([Liu P et al., Front Med 2025, PMID 41098981](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12519452/)).
- Splenic involvement is usually part of miliary TB. Among organs involved in miliary disease, the spleen ranks third after lung and liver.
- Isolated (solitary) splenic TB is uncommon. It is seen mostly in immunosuppressed people, especially those with HIV, but it is also reported in immunocompetent people ([Lin SF et al., World J Surg Oncol 2016, PMID 27250119](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4888408/); [Ranjan R et al., Cureus 2024, PMID 38919240](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11196969/)).
- Most of the evidence comes from case reports. A 2018 review notes that "a consensus statement based on the available case reports is lacking" ([Pol Przegl Chir 2018;90(5):49-51, PMID 30426945](https://pesquisa.bvsalud.org/ses/resource/pt/mdl-30426945)).

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0005967 ("infection of the spleen with mycobacteria") | [MedGen UID 11949](https://ncbi.nlm.nih.gov/medgen/11949) |
| Disease Ontology | DOID:9305 (cross-reference to ICD10CM A18.85) | [MGI/DO](https://www.informatics.jax.org/disease/DOID:9305) |
| ICD-10-CM | A18.85 "Tuberculosis of spleen" (billable; in the code set since Oct 2015) | [icdlist](https://icdlist.com/icd-10/A1885); [unboundmedicine](https://www.unboundmedicine.com/icd/view/ICD-10-CM/891844/all/A18_85___Tuberculosis_of_spleen) |
| WHO ICD-10 | A18.8 "Tuberculosis of other specified organs" (broader category) | [gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/a18-8) |
| SNOMED CT | 28399005 "Tuberculosis of spleen" (maps to A18.8) | [ART-DECOR](https://art-decor.org/terminology/snomed/viewConcept/28399005) |
| MeSH | "Tuberculosis, Splenic", record D014400 (returned for this query; confirm in MeSH) | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014400) |
| OMIM / Orphanet | Not applicable or not found (not a Mendelian disorder) | — |
| ICD-11 | Not retrieved | — |

**Synonyms:** tuberculosis of spleen; splenic TB; tuberculous splenitis; solitary or isolated splenic tuberculosis (isolated form); tuberculous splenic abscess (abscess form); hepatosplenic tuberculosis (combined form, [Radiopaedia](https://radiopaedia.org/articles/27652)).

**Type of evidence:** Aggregated disease-level resources (ontologies) plus individual-patient case reports and small case series.

## 2. Etiology

**Causal factor (infectious):** *Mycobacterium tuberculosis* complex. The spleen is seeded mostly by blood-borne spread from a primary focus, usually in the lung (PMID 41098981). *M. bovis* also causes spleen lesions in animals (Section 14).

**Risk factors (human clinical evidence)**

- **HIV and advanced immunosuppression** (strongest risk factor).
  - Splenic involvement "is more common in patients with HIV and in disseminated disease" (paraphrase of the Dixit R et al. abstract, Indian J Tuberc 2010;57:25-30, PMID 20420041; [IMSEAR](https://search.bvsalud.org/gim/resource/en/sea-146832)).
  - "Up to 70% of the patients with tuberculosis and HIV infection develop extrapulmonary disease" (Salazar A, Enferm Infecc Microbiol Clin 1994, PMID 8011721).
  - Multifocal splenic TB abscesses are described in HIV-infected drug users (Soriano V, AIDS 1991, PMID 1892601) and in AIDS (Reichel C, Z Gastroenterol 1996, PMID 8794544).
  - Splenic TB has been reported with newly diagnosed advanced HIV (Tiri B, IDCases 2016, PMID 27635384).
- **TNF-α blockade.**
  - Keane et al. reported 70 TB cases after infliximab, after a median of 12 weeks of treatment. Forty had extrapulmonary disease, 17 of them disseminated ([NEJM 2001;345:1098, PMID 11596589](https://searchworks.jioinstitute.edu.in/articles/cmedm__11596589); PMID taken from the MEDLINE accession).
  - Hepatic and splenic TB after infliximab for ulcerative colitis has been reported (Chen S, BMC Gastroenterol 2026, PMID 42464147).
- **Other immunosuppression.** Immunodeficiency is described as "an important risk factor for splenic tuberculosis" in case literature ([PMC5806411](https://pmc.ncbi.nlm.nih.gov/articles/PMC5806411)). Diabetes and other comorbidities are mentioned in case series but were not quantified in what I retrieved.
- **Geography:** Living in or coming from a high-burden TB setting. Most series come from India and sub-Saharan Africa.
- **Age:** Childhood. Splenic TB is described in children, including immunocompetent children ([PMC6758994](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6758994/); [PMC11788734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11788734/)). Abdominal TB in children is reviewed in Raj V, Pediatr Surg Int 2025 (PMID 40533676).

**Genetic risk factors (host; inferred to apply to disseminated mycobacterial disease generally, not shown specifically for the spleen)**
- Mendelian susceptibility to mycobacterial disease (MSMD) involves inborn errors of IFN-γ immunity.
  - Genes include IFNGR1, IFNGR2, IL12B, IL12RB1, IL12RB2, IL23R, STAT1, JAK1, IRF8, SPPL2A, ISG15, TYK2, RORC, CYBB and NEMO (IKBKG).
  - Homozygosity for **TYK2 P1104A** is a common-variant cause of TB with "incomplete, and probably low" penetrance ([Bustamante J, PMID 32025907, PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)).
  - Further overviews: [Errami & Bousfiha 2023, PMC10676692](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10676692/); PMID 40656276.
- No splenic-TB-specific GWAS hits, ClinVar entries or ClinGen curations were found.

**Protective factors**
- **BCG vaccination** protects strongly against disseminated (miliary) childhood TB, the form that usually involves the spleen.
  - Mangtani et al. (Clin Infect Dis 2014): RR 0.1 (95% CI 0.01–0.77) for meningeal or miliary TB in infants.
  - Trunz et al. (Lancet 2006): one miliary case prevented per 9,314 vaccinations ([UCL/LSHTM summaries](https://researchonline.lshtm.ac.uk/1440348)). PMIDs for both were not retrieved.
- **Antiretroviral therapy and immune restoration:** inferred to be protective; no splenic-specific data retrieved.
- **TB preventive treatment** before anti-TNF therapy: Keane 2001 recommends screening (PMID 11596589).
- Genetic protective alleles: none identified.

**Gene–environment interaction:** Host IFN-γ/IL-12 pathway defects (genetic) or HIV/TNF blockade (acquired) combine with exposure to *M. tuberculosis* (environmental) to allow blood-borne spread. This is inferred from the MSMD and anti-TNF literature, not demonstrated for the spleen.

## 3. Phenotypes

| Phenotype | Type | Suggested HPO label (ID to verify) | Frequency / notes | Source |
|---|---|---|---|---|
| Fever | Symptom | Fever | 82.3% in a pooled review of isolated splenic TB | Lin 2016, PMID 27250119 ([PMC4888408](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4888408/)) |
| Fatigue / malaise | Symptom | Fatigue | 44.1% (grouped with weight loss) | PMID 27250119 |
| Weight loss | Symptom | Weight loss | 44.1% | PMID 27250119 |
| Splenomegaly | Sign | Splenomegaly | 13.2–100% depending on series. All 23 patients in Sharma's series had splenomegaly (an entry criterion). TB lesions "most often occur with splenomegaly" | PMID 27250119; PMID 17642503; PMID 16554586 |
| Left upper quadrant / abdominal pain | Symptom | Abdominal pain | Common in case reports; not quantified | PMID 41098981 |
| Focal hypoechoic or hypodense splenic lesions (micro- or macronodular) | Imaging finding | Abnormality of the spleen (finer splenic-lesion term to verify) | Most common ultrasound/CT pattern | PMID 17642503 |
| Splenic abscess | Sign / imaging | Splenic abscess (verify term) | Second most common pattern | PMID 17642503 |
| Splenic calcification | Imaging (late or healed lesions) | Splenic calcification | On CT | PMID 17642503 |
| Lymphadenopathy (abdominal or other) | Sign | Lymphadenopathy | Frequent; mimics lymphoma | PMID 41098981 |
| Hepatomegaly / hepatic lesions | Sign | Hepatomegaly | In the hepatosplenic form | [Radiopaedia](https://radiopaedia.org/articles/27652) |
| Night sweats, anorexia | Symptom | Night sweats; Anorexia | Constitutional symptoms; not quantified | general literature (not quantified) |
| Anemia, raised ESR or CRP, cytopenias | Laboratory | Anemia; Elevated erythrocyte sedimentation rate | Reported in cases; not quantified | — |
| Splenic rupture / haemoperitoneum | Complication | Splenic rupture | Rare; led to emergency splenectomy | PMID 38919240 |

- **Onset:** Mostly young and middle-aged adults; also children.
- **Course:** Subacute to chronic (weeks to months), progressive without treatment.
- **Severity:** Variable.
- **Quality of life:** No EQ-5D or SF-36 data specific to splenic TB were found.

## 4. Genetic/Molecular Information

- **Causal human genes:** None (infectious disease). Not applicable: pathogenic variants, ACMG classification, allele frequency, somatic vs germline origin, chromosomal abnormalities, and disease-specific epigenetic data.
- **Host susceptibility genes (modifiers):** The MSMD genes listed in Section 2.
  - Loss of function in the IL-12/IL-23–IFN-γ axis, mostly autosomal recessive (PMID 32025907).
  - TYK2 P1104A is a missense, partial loss-of-function variant with impaired IL-23 signalling (PMID 32025907).
  - IL12RB1 (~44%) and IFNGR1 (~17%) are the most frequently reported MSMD defects ([PMC10676692](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10676692/)).
- **Pathogen genetics:** Drug-resistance mutations (for example, the rpoB rifampicin-resistance region detected by Xpert MTB/RIF) are relevant to treatment. An Xpert-positive splenic aspirate has been reported ([PMC7920217](https://pmc.ncbi.nlm.nih.gov/articles/PMC7920217)). No splenic-specific pathogen lineage data were retrieved.

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (NCBI Taxon to verify). *M. bovis* also causes spleen lesions (zoonotic).
  - Co-infection with *M. fortuitum* in splenic abscesses has been reported in HIV (Soto-Arquíñigo L 2017, PMID 29177396).
- **Lifestyle and environment:** Injecting drug use with HIV (PMID 1892601), crowding, and living in an endemic area. Smoking, alcohol and malnutrition are general TB risk factors not specifically quantified for splenic TB in retrieved sources.
- **Iatrogenic:** Anti-TNF biologics (PMIDs 11596589, 42464147).

## 6. Mechanism / Pathophysiology

**Ordered causal chain**

1. Inhaling *M. tuberculosis* droplet nuclei **leads to** infection of alveolar macrophages (CL: alveolar macrophage) and a primary focus in the lung.
2. Bacilli spreading through lymph and blood (early primary infection, or reactivation) **results in** bacteraemic seeding of reticuloendothelial organs. The spleen is commonly seeded in miliary TB because of its blood-filtering red pulp and resident macrophages. This anatomical rationale is inferred from the spleen's role; that the spleen ranks after lung and liver is shown in case literature (PMID 41098981).
   - In mice, spread from lung to spleen and liver generally occurs 11–14 days after aerosol infection. Its rate depends on host genetics (C57BL/6 vs C3H) ([PMC128141](https://pmc.ncbi.nlm.nih.gov/articles/PMC128141); model-organism evidence).
3. Splenic macrophages taking up bacilli **lead to** innate inflammatory signalling, then recruitment of T cells. IFN-γ (Th1) activation of macrophages, together with TNF-α, **drives** granuloma formation. "TNF-α and IFN-γ are particularly important in promoting the formation and function of the granuloma" ([Frontiers Immunol 2016](https://www.frontiersin.org/articles/10.3389/fimmu.2016.00434)).
4. **Branch A, effective immunity:** Contained epithelioid granulomas **result in** small micronodules that may heal with **calcification** (calcified splenic foci, PMID 17642503).
5. **Branch B, defective immunity** (HIV CD4 depletion, TNF blockade, MSMD gene defects): weak granulomas **lead to** uncontrolled bacillary growth, many microabscesses and miliary lesions. In HIV, 88.3% of splenic microabscesses seen on ultrasound were TB (PMID 31456550).
6. **Branch C, dysregulated hyperinflammation:** Excess TNF and strong T-cell immunity **lead to** macrophage necrosis and release of bacilli outside the cells (Pagán & Ramakrishnan, PMID 25377142). This **results in** caseous necrosis, which merges into **macronodules or a tuberculous ("cold") abscess** (PMID 17642503; [PMC5566777](https://pmc.ncbi.nlm.nih.gov/articles/PMC5566777)).
7. Tissue destruction and splenic enlargement **lead to** splenomegaly and LUQ pain. Rarely, the capsule gives way and the spleen **ruptures**, causing haemoperitoneum (PMID 38919240). Systemic cytokines (TNF, IL-6; inferred) **cause** fever, weight loss and fatigue.

**Checklist detail**

- **Pathways:** IL-12/IL-23–IFN-γ–STAT1 axis (PMID 32025907); TNF signalling; IL-10 as a negative regulator ([Frontiers Immunol 2016](https://www.frontiersin.org/articles/10.3389/fimmu.2016.00434)).
- **Cellular processes:** macrophage phagocytosis, failure of phagosome maturation, necrosis, granuloma formation. Caseous granulomas are "formed by epithelioid macrophages surrounding a cellular necrotic region with a rim of lymphocytes".
- **Immune system:** cell-mediated immunity is central; its failure (HIV) is linked to disseminated and splenic disease.
- **Suggested GO terms (labels, IDs to verify):** granuloma formation; defense response to Gram-positive bacterium / response to bacterium; type II interferon (IFN-γ)-mediated signaling pathway; tumor necrosis factor-mediated signaling pathway; phagocytosis; necrotic cell death; macrophage activation.
- **Suggested CL terms (labels):** macrophage; splenic macrophage / red pulp macrophage; epithelioid cell; multinucleate giant cell (Langhans); CD4-positive alpha-beta T cell; B cell.
- **Molecular profiling:** No splenic-TB-specific transcriptomic, proteomic, metabolomic, single-cell or spatial datasets were identified in this search. General TB blood signatures exist but were not retrieved here.

## 7. Anatomical Structures Affected

- **Primary organ:** spleen (UBERON label: spleen), including red pulp and white pulp.
- **Secondary organs:**
  - liver (hepatosplenic TB), abdominal lymph nodes, lung, peritoneum;
  - bone marrow in disseminated disease (inferred).
- **Body systems:** hematopoietic/lymphoid (immune) system, digestive and abdominal cavity, respiratory.
- **Tissue and cells:** lymphoid tissue; granulomatous inflammation with caseous necrosis; macrophages, epithelioid cells, Langhans giant cells, T and B lymphocytes.
- **Subcellular (GO Cellular Component labels):** phagosome; phagolysosome / lysosome (bacilli persist in the phagosome); cytoplasm of macrophages.
- **Lateralization:** Left upper quadrant (the spleen is a single left-sided organ). Lesions within the spleen are solitary or multiple and diffuse.

## 8. Temporal Development

- **Onset:** Subacute or insidious, with weeks to months of fever and weight loss. Occasionally acute, from abscess rupture (PMID 38919240). Occurs in children and adults.
- **Morphological stages (imaging and pathology):**
  - miliary micronodules (<2 cm) → macronodules or confluent lesions → abscess → healing with calcification (PMID 17642503; [Radiopaedia](https://radiopaedia.org/articles/27652));
  - on MRI, lesions tend to be "small and multiple" and "most often occur with splenomegaly" (De Backer AI et al., AJR 2006, PMID 16554586).
- **Course:** Progressive and potentially fatal without treatment. Treatment usually leads to remission; lesions shrink on ultrasound follow-up, which Sharma et al. propose for monitoring response (PMID 17642503).
- **Critical windows:**
  - early in anti-TNF therapy (median 12 weeks; PMID 11596589);
  - advanced HIV (low CD4).

## 9. Inheritance and Population

- **Inheritance:** Not applicable (acquired infection). MSMD predisposition is mostly autosomal recessive (Section 4).
- **Epidemiology:**
  - Population-level splenic TB incidence or prevalence is **not available**.
  - WHO 2025 report: 16% of TB notifications in 2024 were extrapulmonary ([WHO GTB 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-diagnosis-and-treatment/2-1-case-notifications)).
  - Splenic TB was found in 4–12% of patients who underwent diagnostic splenectomy in one cited series (secondary citation in [PMC4888408](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4888408/)).
  - In HIV-positive patients, ultrasound showed splenic lesions in 21.0% (95% CI 10.6–33.8) across 5 studies with 774 patients (Schafer JM et al., S Afr Med J 2019;109:570-6, PMID 31456550).
- **Geography:** High TB-burden regions (South Asia, sub-Saharan Africa). Major series come from India (PMIDs 17642503, 20420041).
- **Sex ratio and age distribution:** No robust data retrieved. A 2026 systematic review (Chaudhary P, J Glob Infect Dis, PMID 41958487) covers epidemiology, but its full text or abstract could not be retrieved.

## 10. Diagnostics

**Imaging**

- **Ultrasound:** In the Sharma series of 23 patients, the findings in descending order were "single or multiple hypoechoic focal lesions, splenic abscess, calcifications (on CT) and isolated splenomegaly". In 5 of 6 patients whose only ultrasound finding was splenomegaly, CT showed lesions. The authors call ultrasound affordable, non-invasive and useful for following treatment response (PMID 17642503; [IJMR](https://ijmr.org.in/radiological-manifestations-of-splenic-tuberculosis-a-23-patient-case-series-from-india/)).
- **CT:** Multiple well-defined, hypodense round lesions ([Zapata Naranjo, Cureus 2025, PMID 40291232](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12033969/)). Imaging features of splenic infections are largely non-specific ([Abdom Radiol 2021, PMC8160561](https://pmc.ncbi.nlm.nih.gov/articles/PMC8160561)).
- **MRI:** Small, multiple lesions, usually with splenomegaly (PMID 16554586).
- **FDG-PET/CT:** Isolated splenic TB has been detected only on FDG-PET ([PMC6159193](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6159193/)). PET does not distinguish TB from lymphoma.
- **FASH protocol:** Focused Assessment with Sonography for HIV-associated TB looks for splenic microabscesses ([ACEP](https://www.acep.org/sonoguide/advanced/fash)). In HIV, 88.3% (95% CI 72.3–97.9) of splenic microabscesses on ultrasound were TB, and the authors suggest this is "probably sufficient indication to initiate TB treatment prior to obtaining culture data" (PMID 31456550).

**Microbiology and pathology**

- **Sampling:** Image-guided fine-needle aspiration (FNA), core biopsy, or splenectomy specimen. FNA is safer, while core biopsy is more accurate ([PMC5566777](https://pmc.ncbi.nlm.nih.gov/articles/PMC5566777); [PMC3948145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3948145)).
- **Tests on the sample:** AFB smear (Ziehl–Neelsen), mycobacterial culture, Xpert MTB/RIF. AFB smear and Xpert were positive on a splenic aspirate in one series ([PMC7920217](https://pmc.ncbi.nlm.nih.gov/articles/PMC7920217)).
- **Histology:** caseating epithelioid granulomas with Langhans giant cells.
- **Post-splenectomy diagnosis:** "the definitive diagnosis is essentially formulated on the post-splenectomy specimen" in many reports (PMID 30426945).

**Ancillary tests:** HIV testing; IGRA or tuberculin skin test (supportive only); chest imaging; sputum testing for a concurrent pulmonary focus; urine LF-LAM in advanced HIV (general TB practice; not retrieved specifically for splenic TB).

**Genetic testing:** Not used for diagnosis. Consider an MSMD gene panel or exome sequencing (IL12RB1, IFNGR1 and others) only in children with disseminated or recurrent mycobacterial disease without an acquired cause (inferred from PMID 32025907).

**Omics-based diagnostics:** None validated for splenic TB.

**Differential diagnosis:**
- **Lymphoma:** the most important mimic, with nodules plus lymphadenopathy (PMID 41098981).
- **Pyogenic splenic abscess:** shorter illness, bacterial cultures.
- **Splenic infarct:** wedge-shaped.
- **Fungal microabscesses** (candidiasis) in neutropenia.
- **Others:** sarcoidosis, metastases, histoplasmosis (calcifications), brucellosis, melioidosis, and splenic involvement by Bartonella or nontuberculous mycobacteria (NTM) in HIV ([PMC5566777](https://pmc.ncbi.nlm.nih.gov/articles/PMC5566777)).

**Screening:** No population screening. In people with HIV, point-of-care ultrasound (FASH) is used as targeted case-finding.

## 11. Outcome/Prognosis

- **Mortality:** No splenic-TB-specific survival statistics were retrieved. Prognosis with appropriate anti-TB therapy is generally good in case reports. Mortality is driven mostly by co-existing disseminated or HIV-associated disease.
- **Complications:** abscess formation, splenic rupture with haemoperitoneum (PMID 38919240), and spread of disseminated disease. After splenectomy there is a lifelong risk of overwhelming post-splenectomy infection (general surgical knowledge; not retrieved here).
- **Prognostic factors (inferred from the case literature):** HIV status, CD4 count, disseminated vs isolated disease, drug resistance, and how fast diagnosis is made.
- **Quality of life and disability:** No data.

## 12. Treatment

**Pharmacotherapy (NCIT labels to verify: Isoniazid, Rifampin, Pyrazinamide, Ethambutol)**

- **Regimen:** Standard 6-month 2HRZ(E)/4HR, that is, 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol, then 4 months of isoniazid and rifampicin. WHO applies it to extrapulmonary TB except CNS and bone/joint TB, which get longer regimens ([WHO TB KSP node 1933](https://tbksp.who.int/en/node/1933); [WHO Module 4](https://www.who.int/publications/i/item/9789240048126); [NBK613096](https://www.ncbi.nlm.nih.gov/books/NBK613096/)).
- **Duration in practice:** Many case reports used 6–12 months; no trials specific to splenic TB exist.
- **Drug-resistant TB:** follow WHO drug-resistant TB regimens.
- **HIV co-infection:** ART coordinated with TB therapy; watch rifampicin drug interactions.
- **Mechanisms of action:**
  - isoniazid: inhibits mycolic acid synthesis via InhA after KatG activation;
  - rifampicin: inhibits RNA polymerase (rpoB);
  - pyrazinamide: acts against semi-dormant bacilli;
  - ethambutol: inhibits arabinosyltransferase.
- **Pharmacogenomics:** NAT2 acetylator status affects isoniazid exposure and hepatotoxicity (not retrieved in this session; verify in PharmGKB/CPIC).

**Surgical and interventional (NCIT labels: Splenectomy; Percutaneous Drainage)**
- Splenectomy plus anti-TB therapy is curative and was historically common. Current opinion reserves it for rupture, failed medical therapy or diagnostic uncertainty ([PMC4888408](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4888408/); PMID 38919240).
- Percutaneous (pigtail) drainage of tuberculous abscesses works as an adjunct; reported success rates for splenic abscess drainage in general are 67–100% ([PMC7920217](https://pmc.ncbi.nlm.nih.gov/articles/PMC7920217)).

**Supportive care:** nutrition, analgesia. After splenectomy: vaccination against encapsulated organisms (general practice).

**Advanced therapeutics** (gene, cell, RNA, targeted, immunotherapy): **not applicable**. No splenic-TB clinical trials (NCT IDs) were found.

**Adverse events:** hepatotoxicity (H, R, Z), peripheral neuropathy (H), optic neuritis (E), drug interactions (R). These are general knowledge; FAERS was not queried.

## 13. Prevention

- **Primary prevention:**
  - BCG in infancy, which strongly protects against miliary and disseminated childhood TB (Mangtani 2014 RR 0.1; Trunz 2006; [UCL](https://discovery-pp.ucl.ac.uk/id/eprint/1437602/1/bmj.g4643.full.pdf), [LSHTM](https://researchonline.lshtm.ac.uk/1440348));
  - infection control and contact tracing;
  - ART for people with HIV.
- **Prophylaxis:** screen for latent TB infection and give TB preventive treatment before anti-TNF therapy (PMID 11596589), and for people with HIV (WHO guidance; not separately retrieved).
- **Secondary prevention:** FASH ultrasound in HIV-positive patients with suspected TB (PMID 31456550); early tissue diagnosis.
- **Tertiary prevention:**
  - complete the full anti-TB course;
  - follow-up imaging;
  - after splenectomy, vaccines (pneumococcal, meningococcal, Hib) and antibiotic awareness (general practice).
- **Genetic counseling:** only for families with MSMD.
- **Public health:** WHO End TB strategy; in animals, control of *M. bovis* in livestock and pasteurisation of milk.

## 14. Other Species / Natural Disease

- **Species affected:**
  - Cattle and wildlife with *M. bovis*. In white-tailed deer (*Odocoileus virginianus*) in Michigan, gross TB lesions were found in liver, **spleen**, rumen and mammary gland, sites "apparently not previously reported in this species" ([J Wildl Dis 2001;37:608](https://bioone.org/journals/journal-of-wildlife-diseases/volume-37/issue-3/0090-3558-37.3.608/Tuberculous-Lesions-in-Free-Ranging-White-Tailed-Deer-in-Michigan/10.7589/0090-3558-37.3.608.full)).
  - Spleen-specific frequency data for cattle were not retrieved.
- **Zoonotic potential:** *M. bovis* is transmissible to hunters, processors and others ([Cornell CWHL](https://cwhl.vet.cornell.edu/disease/bovine-tuberculosis)). Lesions caused by *M. avium* subsp. *hominissuis* can mimic *M. bovis* in deer ([CDC EID 2020](https://WWW.CDC.GOV/eid/article/26/7/20-0187_article)).
- **Breeds (VBO), orthologous genes, OMIA:** Not applicable (non-Mendelian).
- **Comparative biology:** Caseous granulomas are conserved across mammals. Mice (except C3HeB/FeJ) usually do not form caseous necrosis.

## 15. Model Organisms

- **Mouse aerosol infection model** (*M. tuberculosis* H37Rv/Erdman):
  - Spread to the spleen at roughly 11–14 days, with spleen CFU as a standard readout of dissemination ([PMC128141](https://pmc.ncbi.nlm.nih.gov/articles/PMC128141)).
  - C57BL/6 (relatively resistant) vs C3H/DBA/2 (susceptible); host genetics affect the rate of dissemination.
  - **C3HeB/FeJ ("Kramnik") mice** form hypoxic, caseous granulomas that resemble human necrotic lesions, but lung CFU varies widely ([PMC4457037](https://pmc.ncbi.nlm.nih.gov/articles/PMC4457037); [Frontiers 2024](https://frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1427846/pdf)).
  - BCG protection measured in the spleen varies by strain ([PMC7160682](https://pmc.ncbi.nlm.nih.gov/articles/PMC7160682)).
- **Genetic models:** Knockouts of Ifng, Ifngr1, Tnf and Il12b in mice model susceptibility to disseminated mycobacterial disease (general knowledge; not retrieved in this session, verify in MGI).
- **Zebrafish–*M. marinum*:** Reveals the mechanism of granuloma formation and TNF-driven necrosis (Pagán & Ramakrishnan, PMID 25377142).
- **Limitations:** No model specifically reproduces *isolated* splenic TB or splenic abscess. Mouse spleen involvement is part of systemic spread, not a model of the focal human disease.
- **Resources:** MGI, ZFIN, IMSR (not queried directly).

---

### Key PMIDs (all retrieved in this session)
| Topic | PMIDs |
|---|---|
| Splenic TB reviews and series | 30426945, 27250119, 41098981, 41958487, 17642503, 16554586, 20420041, 38919240 |
| HIV-associated splenic TB | 31456550, 27635384, 8011721, 1892601, 8794544, 29177396 |
| Iatrogenic (anti-TNF) | 11596589, 42464147 |
| Imaging review; paediatric abdominal TB | 40291232, 40533676 |
| Mechanism and host genetics | 25377142, 32025907, 40656276 |

**Gaps:**
- incidence and prevalence, sex ratio, and mortality specific to splenic TB;
- ICD-11 code;
- ontology numeric IDs (HPO/GO/CL/UBERON/NCIT);
- PMIDs for the BCG meta-analyses (Mangtani 2014, Trunz 2006) and Ramakrishnan 2012;
- full abstract of the 2026 systematic review (PMID 41958487).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 40 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:20420041` *(abstract only)*: "is more common in patients with HIV and in disseminated disease"
  - closest text in source: "CONCLUSION: The splenic involvement in tuberculosis seems to be more frequent in patients with HIV infection and in disseminated form of disease"
- `PMID:16554586` *(abstract only)*: "most often occur with splenomegaly"
  - closest text in source: "CONCLUSION: Tuberculous focal splenic lesions are small, multiple, and most often associated with splenomegaly"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.3389/fimmu.2016.00434`: "TNF-α and IFN-γ are particularly important in promoting the formation and function of the granuloma"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Terms the ontology service could not be reached for

2 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0005967` (2 mentions)
- `DOID:9305` (3 mentions)

No term could be looked up either way, so nothing here was confirmed or contradicted.