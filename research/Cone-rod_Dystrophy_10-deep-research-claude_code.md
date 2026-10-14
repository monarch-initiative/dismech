---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T13:42:14.980519'
end_time: '2026-10-14T13:43:49.040295'
duration_seconds: 94.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cone-rod dystrophy 10
  mondo_id: MONDO:0012464
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 9
  num_turns: 15
  total_cost_usd: 0.8766765000000001
  session_id: bdbb9ed8-450b-5f29-904f-87db2bb34752
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012464
    reported_labels:
    - not obsolete
    ontology_label: cone-rod dystrophy 10
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cone-rod dystrophy 10
- **MONDO ID:** MONDO:0012464 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cone-rod dystrophy 10** covering all of the
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

I've confirmed that CORD10 is the SEMA4A form (OMIM 610283), not PITPNM3, which is CORD5. I'm now getting PMIDs and clinical details for the human reports, then I'll write the report.

# Cone-rod dystrophy 10 (CORD10; MONDO:0012464): research report

## Scope and caveats

- **Tool limits.** OMIM, PMC and the JMG full text were blocked in this environment (proxy refusal and a reCAPTCHA page). Details from those sources are therefore taken from search-result summaries, not from the papers themselves.
- **No verbatim abstract quotes.** I could not retrieve abstract text, so this report has none. Every snippet destined for the KB must be fetched with `just fetch-reference` and quoted from the cache.
- **Source labels.** "Verified" means seen in a search result or the MONDO record. "Unverified" means from my memory or not seen in a source.
- **Gene identity.** My first query tied CORD10 to PITPNM3. That was wrong. PITPNM3 causes CORD5 (OMIM 600977). CORD10 is the SEMA4A form, as shown below.

## 1. Disease information

**Overview.** CORD10 is a progressive retinal dystrophy in which cone loss comes first, followed by rod loss. Color vision and acuity decline first, then night blindness and peripheral field loss (OMIM and MalaCards summaries). It is attributed to compound heterozygous SEMA4A variants and is autosomal recessive. This rests on a single 2006 paper.

**Identifiers** (from the OLS MONDO record, plus search summaries):

| Resource | ID |
|---|---|
| MONDO | MONDO:0012464 (not obsolete) |
| OMIM | 610283 |
| Orphanet | 1872 |
| DOID | 0111017 |
| GARD | 0015477 |
| MedGen | 337598 |
| MeSH | C564597 |
| UMLS | C1846529 |

**MONDO definition:** "Any cone-rod dystrophy in which the cause of the disease is a mutation in the SEMA4A gene."

**Synonyms:** cone-rod dystrophy type 10, CORD10, SEMA4A cone-rod dystrophy, cone-rod dystrophy caused by mutation in SEMA4A.

**Allelic phenotype.** Retinitis pigmentosa 35 (RP35, OMIM 610282) is also attributed to SEMA4A. Any entry should record the CORD10/RP35 overlap.

**Data source.** The resources above are aggregated disease-level records. The primary evidence is a small patient cohort (see section 4).

## 2. Etiology

- **Cause.** Genetic, from compound heterozygous SEMA4A (semaphorin 4A) variants on 1q22 (OMIM 610283 summary).
- **Risk, protective and gene-environment factors.** None are documented. I found nothing on modifier genes, protective alleles or exposures.
- **Mouse hint.** A press summary of the earlier mouse work says Sema4A moves retinoid-binding proteins and retinoids between the cell surface and the endoplasmic reticulum under normal conditions. The same summary mentions oxidative stress. This hints at a gene-environment angle, but it is mouse data only and I did not see the primary text.

## 3. Phenotypes

Human clinical detail is thin. The 2006 paper reported two CRD patients with biallelic variants. I did not retrieve per-patient data, so frequencies, ages at onset and quality-of-life data are unavailable.

| Phenotype | Suggested HPO term (look up before binding) | Notes |
|---|---|---|
| Cone-rod dystrophy | Cone/cone-rod dystrophy | Defining feature |
| Reduced color vision | Abnormal color vision | Early (OMIM) |
| Reduced visual acuity | Reduced visual acuity | Early (OMIM) |
| Night blindness | Nyctalopia | After cone symptoms (OMIM) |
| Peripheral visual field loss | Constriction of peripheral visual field | Late (OMIM) |

- **Course:** progressive. Onset ages are not confirmed.
- **Do not copy CURIEs from this table.** Each must be read from a lookup, per the repo rules.

## 4. Genetic and molecular information

**Gene.** SEMA4A is HGNC lowercase form `hgnc:` plus the ID, which I did not look up. The OMIM gene entry is 607292. The protein is a 760-residue transmembrane semaphorin.

**Abid et al. 2006** (J Med Genet 43:378–381, PMID:16199541 per GenCC and DisGeNET):
- 190 unrelated patients were screened (search summary).
- Two missense variants, p.D345H and p.F350C, were found only in affected people. Both lie in the conserved semaphorin domain, and neither appeared in 100 controls.
- OMIM-derived summaries describe compound heterozygosity for two substitutions in two RP and two CRD patients. Three RP patients and one congenitally blind patient carried a single heterozygous change.
- p.R713Q was also reported. See the caveats below.

**Evidence strength:**
- A Genomics England panel curator noted biallelic evidence from this one paper (two RP, two CRD patients) and no newer reports.
- Australian PanelApp rates SEMA4A Amber for recessive RP and Red for dominant RP.
- R713Q is common in gnomAD (more than 10,000 heterozygotes and 299 homozygotes). It did not segregate with disease in PMID:28805479 and is tagged refuted for dominant RP.
- Treat the gene-disease link as limited. ClinGen and GenCC classifications should be checked for a tier to copy. I did not retrieve them.

**Functional consequence.** The F350C change causes abnormal localization of the Sema4A protein. In mice this impairs endosomal sorting (Nojima 2013, see section 6). Whether the human variants act as loss of function is not directly shown. Modifier genes and epigenetic changes are not documented, and no chromosomal abnormalities are described.

## 5. Environmental information

None documented. There are no known infectious agents, toxins or lifestyle factors.

## 6. Mechanism and pathophysiology

**Ordered causal chain** (steps 1–3 mouse-derived, step 4 inferred, step 5 not shown):
1. Biallelic SEMA4A variants, such as F350C, are present in the semaphorin domain (human genetics, PMID:16199541).
2. The mutant protein is mislocalized. In mouse RPE, Sema4A normally regulates endosomal sorting (Nojima 2013, Nat Commun).
3. Sorting of molecules needed for photoreceptor survival and phototransduction is impaired (Nojima 2013, mouse).
4. Photoreceptors degenerate. This is shown for F350C/F350C and Sema4A−/− mice. Its extension to humans is inferred.
5. Cones are affected first and rods later in humans. The mouse data do not establish the human order.

**Supporting details:**
- **Cell types and tissue.** The mouse work places the mechanism in retinal pigment epithelium and photoreceptors. Suggested CL terms are retinal pigment epithelial cell, retinal cone cell and retinal rod cell. Look up the CURIEs.
- **Rescue.** Sema4A gene transfer prevented photoreceptor degeneration in Sema4AF350C/F350C and Sema4A−/− mice (Nojima 2013).
- **Suggested GO terms** (bind only after lookup): endosomal transport, protein localization to membrane, and visual perception.
- **Molecular profiling.** No transcriptomic, proteomic, single-cell or other omics findings were found.

## 7. Anatomical structures affected

- **Primary:** the retina, meaning photoreceptors (cones then rods) and the RPE.
- **Systemic involvement:** none described.
- **Localization:** bilateral, as for retinal dystrophies generally. I did not confirm this for CORD10.
- **Subcellular:** endosomal and cell-surface compartments, per the mouse sorting data.

## 8. Temporal development

Progressive, with cone symptoms before rod symptoms (OMIM). Age at onset, rate and staging are not retrieved. Remission is not expected.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (compound heterozygous). Genomics England lists both monoallelic and biallelic modes for the gene, but the dominant evidence is weak.
- **Prevalence:** not reported. It is probably very rare. Orphanet 1872 should be checked for a prevalence class.
- **Founder effects, consanguinity and carrier frequency:** not documented. Note that R713Q is common in population databases.
- **Related locus.** PITPNM3 (CORD5) is a separate dominant disease and should not be confused with this one. Its Q626H variant was reported in Swedish families, with a later 163-patient screen suggesting PITPNM3 is an uncommon cause.

## 10. Diagnostics

I found no CORD10-specific guidance. Standard retinal dystrophy workup applies:
- Full-field ERG, expected to show cone responses reduced before or alongside rod responses. This is expected from the disease class, not shown for this gene.
- Visual fields, fundus imaging and optical coherence tomography.
- Genetic testing through retinal dystrophy gene panels. Genomics England and PanelApp include SEMA4A.
- Interpret SEMA4A variants cautiously because the evidence is limited. R713Q alone should not be called pathogenic.
- Check GeneReviews with `just check-genereviews`. I found no chapter for this entity.

## 11. Outcome and prognosis

Vision loss is progressive. No survival, life-expectancy or quality-of-life data were found. Prognostic factors are unknown.

## 12. Treatment

- **No approved or disease-specific therapy.** Management is supportive: low-vision aids, rehabilitation and genetic counseling. Suggested NCIT terms include Supportive Care (NCIT:C15747), Rehabilitation (NCIT:C15315) and Genetic Counseling (NCIT:C15240). These come from the CLAUDE.md list, but verify them before binding.
- **Experimental.** Sema4A gene transfer prevented degeneration in mice (Nojima 2013). No human trial was found. Search ClinicalTrials.gov before asserting this.

## 13. Prevention

- **Genetic counseling and cascade testing:** carrier risk of 25% per sibling given a recessive mode.
- **Preimplantation or prenatal testing:** possible once biallelic pathogenic variants are established.
- **No other prevention measures** are known.

## 14. Other species and natural disease

No naturally occurring disease was identified and I did not check OMIA. Mouse Sema4a is the relevant ortholog.

## 15. Model organisms

| Model | Findings | Source |
|---|---|---|
| Sema4a gene-trap mouse (insertion into intron 11) | Loss of retinal photoreceptors | Rice et al. 2004, Invest Ophthalmol Vis Sci 45:2767–77, PMID:15277503 (verified) |
| Sema4aF350C knock-in mouse | Retinal degeneration. The paper reports F350C causes the phenotype (search summary) | Nojima et al. 2013, Nat Commun |
| Sema4aD345H and R713Q knock-in mice | Made in the same study. The summaries say only F350C causes the degeneration phenotype | Nojima et al. 2013 |
| Sema4a−/− | Rescued by Sema4A gene transfer | Nojima et al. 2013 |

**Fidelity.** The knock-in directly models the human F350C allele. Whether the mouse recapitulates human cone-first progression is unknown, and the model is apparently homozygous. This fits a `HUMAN_MODEL_MISMATCH`-style discussion if curated. The Nojima PMID is unresolved: a search summary gave 23360997 but flagged it uncertain, so confirm via `just fetch-reference` before citing.

## Suggested KB handling

- **Evidence is thin.** Use `evidence_source: HUMAN_CLINICAL` for Abid 2006 and `MODEL_ORGANISM` for the mouse papers.
- **Gene-disease validity.** Run `just check-gene-validity` and look for ClinGen records. Do not assign a tier yourself.
- **Allelic overlap.** Mention RP35 (MIM 610282) in the entry notes.

## Sources

- [MONDO:0012464 via EBI OLS](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http://purl.obolibrary.org/obo/MONDO_0012464)
- [OMIM #610283](https://omim.org/entry/610283) (seen only in search results)
- [Wikidata Q32146111](https://www.wikidata.org/wiki/Q32146111)
- [MalaCards CORD10](https://www.malacards.org/card/cone_rod_dystrophy_10)
- [Abid et al. 2006, J Med Genet 43:378](https://jmg.bmj.com/content/43/4/378)
- [Genomics England PanelApp, SEMA4A](https://panelapp.genomicsengland.co.uk/panels/509/gene/SEMA4A/)
- [Australian PanelApp, SEMA4A (recessive RP)](https://panelapp-aus.org/panels/277/gene/SEMA4A)
- [Nojima et al. 2013, Nat Commun](https://www.nature.com/articles/ncomms2420)
- [Rice et al. 2004 record via RIKEN MGI RDF](https://metadb.riken.jp/metadb/db/mgi_rdf/http://rdf.ncbi.nlm.nih.gov/pubmed/15277503)
- [Köhn et al. 2007, CORD5/PITPNM3](https://www.nature.com/articles/5201817.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012464` (5 mentions) - the report calls it "not obsolete"; MONDO calls it **cone-rod dystrophy 10**