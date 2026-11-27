---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T18:23:03.938774'
end_time: '2026-11-26T18:25:37.474472'
duration_seconds: 153.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tuberculous Peritonitis
  mondo_id: MONDO:0006000
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Mycobacterium tuberculosis peritonitis; Mycobacterium tuberculosis caused
    peritonitis
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
  web_search_requests: 9
  num_turns: 14
  total_cost_usd: 0.7541013
  session_id: 3eae3dfa-50b7-4a0c-a73b-36801b87cca7
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 13
  retrieval_calls: 11
  assistant_text_blocks: 2
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 2
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMC:PMC6307147
  - PMID:40656276
  - PMID:12145724
  - PMC:PMC4929092
  - PMC:PMC7446809
  relevance_assessed: 28
  on_topic: 17
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  service_unreachable: 1
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberculous Peritonitis
- **MONDO ID:** MONDO:0006000 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Mycobacterium tuberculosis peritonitis; Mycobacterium tuberculosis caused peritonitis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tuberculous Peritonitis** covering all of the
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

I'm still gathering sources. Next I'm searching for epidemiology, genetic susceptibility and animal models.

# Tuberculous Peritonitis (MONDO:0006000): Research Report

**Scope.** I researched tuberculous peritonitis (TBP) as the infectious disease named by MONDO:0006000: peritonitis caused by *Mycobacterium tuberculosis*. **No causal gene is recorded, and none applies.** The disease is caused by infection, not by a Mendelian variant. Inborn errors of IFN-γ immunity, chiefly *IL12RB1*, are susceptibility factors only (Section 4).

**Method and limits.**
- Sources came from web searches only. Direct PubMed queries were not allowed in this session, so I could not read most full texts or abstracts.
- Quotations are taken from the abstract or summary text the searches returned. They should be checked against the full abstracts.
- I give a PMID only where the search returned one.
- Ontology terms are given as **labels only**. I did not retrieve or verify any HPO, GO, CL, UBERON, CHEBI or NCIT identifiers, so they still need to be mapped.
- A search on animal and intraperitoneal infection models failed with a tool error. Sections 14–15 therefore rely on general knowledge and are flagged as unsourced.

---

## 1. Disease Information

**Overview.** TBP is tuberculosis of the peritoneum. It is the most common form of abdominal TB in many series ("Peritoneal TB is the most common presentation of abdominal TB" — [PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)). Tertiary-centre reports, however, often find intestinal TB more common ([PMC4929092](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929092)).

A *Microbiology Spectrum* review says diagnosis needs a high index of suspicion. It should be considered when ascites is lymphocyte-predominant with a serum–ascites albumin gradient (SAAG) below 1.1 g/dL (PMID 28185616, [pubmed](https://pubmed.ncbi.nlm.nih.gov/28185616/)).

**Identifiers**

| Identifier | Value |
|---|---|
| MONDO | MONDO:0006000 (supplied in the request) |
| ICD-10 | K67.3, tuberculous peritonitis. Not verified in this session. |
| OMIM | Not applicable. This is not a Mendelian disease. |
| Orphanet | None retrieved. |
| MeSH | "Peritonitis, Tuberculous" heading exists. Its ID was not retrieved. |

**Synonyms:** peritoneal tuberculosis; *Mycobacterium tuberculosis* peritonitis; tuberculous peritonitis (TBP/TP).

**Source type:** the evidence is aggregated, disease-level literature: case series, cohorts, meta-analyses and a Cochrane review.

---

## 2. Etiology

**Cause.** Infection of the peritoneum by *M. tuberculosis* complex. Zoonotic *M. bovis* is also classically implicated in abdominal TB (unsourced here).

**Risk factors (human clinical evidence)**
- **Immunosuppression, kidney failure on dialysis, cirrhosis and malnutrition.** "Risk factors for developing peritoneal TB include states of immunosuppression (most prominently HIV/AIDS), kidney failure requiring dialysis, cirrhosis, and malnutrition" ([PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)).
- **End-stage kidney or liver disease** often accompanies TBP and complicates diagnosis (Sanai & Bzeizi, *Aliment Pharmacol Ther* 2005;22:685–700, doi:10.1111/j.1365-2036.2005.02645.x; PMID not retrieved).
- **Peritoneal dialysis (PD).** Listed risk factors in PD patients are malnutrition, diabetes, partially treated TB, chest X-ray scarring and immunosuppression ([PMC7320463](https://pmc.ncbi.nlm.nih.gov/articles/PMC7320463)).
- **Comorbidity in a hospital series.** In a Hong Kong series of 60 cases, most patients had severe underlying conditions: cirrhosis, renal failure, diabetes or malignancy (Chow et al., *Clin Infect Dis* 2002; PMID 12145724, [record](https://pesquisa.bvsalud.org/paraguay/resource/es/mdl-12145724)).

**Genetic risk.** There are no GWAS loci specific to TBP. Mendelian susceptibility to mycobacterial disease (MSMD), most often *IL12RB1* deficiency, predisposes to disseminated mycobacterial disease, including *M. tuberculosis* (Section 4).

**Protective factors.**
- No data specific to TBP were retrieved.
- In general TB terms, control of HIV and treatment of latent TB lower the risk of reactivation (general knowledge, not sourced here).
- BCG mainly protects children against disseminated and meningeal TB. I retrieved no TBP-specific data.

**Gene–environment interaction.** Only inferred: inborn IFN-γ pathway defects need mycobacterial exposure before disease appears ([PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)).

---

## 3. Phenotypes

Frequencies below are pooled from a table of 17 studies ([PMC6609850](https://pmc.ncbi.nlm.nih.gov/articles/PMC6609850)) unless another source is given.

| Phenotype | Type | Frequency | Suggested HPO label (ID not verified) |
|---|---|---|---|
| Abdominal pain | Symptom | ~75% | Abdominal pain |
| Fever | Sign | ~69% | Fever |
| Ascites | Sign | ~62% (most common presentation in other reviews) | Ascites |
| Weight loss | Symptom | ~53% | Weight loss |
| Lymphocyte-predominant exudative ascites (low SAAG) | Laboratory | Characteristic finding (PMID 28185616) | — |
| Raised ascitic ADA / IFN-γ | Laboratory | Sensitivity ~93% (Section 10) | — |
| Abdominal distension, night sweats, anorexia, abdominal mass, "doughy" abdomen | Symptoms and signs | Variable; not quantified in the retrieved sources | Abdominal distention; Night sweats; Anorexia |

**Characteristics:**
- Onset is subacute to chronic, over weeks to months.
- Most patients are adults; the peak is age 35–45 ([PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)).
- Without treatment the disease progresses. It can be fatal when diagnosis is delayed (Section 11).

**Quality of life:** I found no EQ-5D or SF-36 data specific to TBP.

---

## 4. Genetic/Molecular Information

**Causal genes:** none. This is an infectious disease.

**Host susceptibility (MSMD).** MSMD is "a rare group of inborn errors of immunity characterized by selective susceptibility to clinical disease caused by attenuated Mycobacterium strains". The source adds that "the more virulent M. tuberculosis has also caused disease in some MSMD patients" ([PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902); overview PMID 40656276).

The *IL12RB1* findings from these sources:
- *IL12RB1* is the gene most often affected.
- The deficiency is autosomal recessive.
- Loss of IL-12Rβ1 "abolishes both IL-12 and IL-23 signaling".
- A 2023 case describes a 7-year-old with an *IL12RB1* mutation and disseminated TB involving the mesenteric lymph nodes ([Frontiers Immunol 2023](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1135824/full)).

**Not applicable:** ClinVar variants for TBP itself, epigenetics and chromosomal abnormalities. Nothing was retrieved for these.

---

## 5. Environmental Information

- **Infectious agent:** *M. tuberculosis* complex (NCBI Taxon ID not verified this session).
- **Exposures:** TB-endemic settings, malnutrition and dialysis ([PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)).
- **Lifestyle factors:** alcohol-related cirrhosis is the main route ([PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)).

---

## 6. Mechanism / Pathophysiology

This is the classic model. Most steps are drawn from reviews (PMID 28185616; PMID 31293914) and general TB immunology. Steps marked *inferred* were not demonstrated in TBP-specific primary studies that I retrieved.

**Causal chain**

1. Primary infection with *M. tuberculosis* (usually in the lung) leads to a latent focus.
2. Seeding of the peritoneum. This is the branching step:
   - **2a.** Haematogenous spread from a pulmonary focus, which may be latent. This is the main route.
   - **2b.** Contiguous spread from infected mesenteric lymph nodes, intestine or fallopian tubes.
   - **2c.** Swallowed bacilli, or ingestion of *M. bovis*, then enter via the gut and lymphatics (*inferred* for current-day TBP).
3. Reactivation follows when host immunity fails (HIV, cirrhosis, dialysis, malnutrition, IFN-γ axis defects). This results in bacilli replicating inside peritoneal macrophages (*inferred*; mechanism extrapolated from general TB).
4. A Th1 response (IL-12 → IFN-γ → macrophage activation) leads to granulomas with caseating necrosis on the peritoneum. Studding of the parietal and visceral peritoneum and omentum appears as tubercles.
5. Inflammation increases vascular permeability. This results in a protein-rich exudate dominated by lymphocytes, with a low SAAG (PMID 28185616). Activated T cells release ADA and IFN-γ into the fluid, which is the basis of the biomarkers in Section 10.
6. The disease then takes one of three patterns:
   - **6a. "Wet" ascitic type:** ascites leading to distension and pain.
   - **6b. Fibroadhesive type:** fibrosis and adhesions, omental caking and matted bowel leading to bowel obstruction.
   - **6c. Fibrotic or caseous type:** abscesses and masses.
7. Systemic cytokines (TNF and others) cause fever, weight loss and anorexia. Delayed treatment leads to sepsis and death (PMID 12145724).

**Detail**
- **Cells involved** (CL labels; IDs not verified):
  - macrophage, epithelioid cell, multinucleated giant cell;
  - CD4-positive alpha-beta T cell (Th1);
  - lymphocyte;
  - mesothelial cell.
- **GO process labels:**
  - granuloma formation;
  - interferon-gamma production;
  - response to bacterium;
  - inflammatory response;
  - phagocytosis.
- **Omics:** no TBP-specific transcriptomic, proteomic, metabolomic or single-cell studies were retrieved.

---

## 7. Anatomical Structures Affected

**Primary sites** (UBERON labels, IDs not verified): parietal peritoneum, visceral peritoneum, omentum, mesentery, peritoneal cavity (ascitic fluid).

**Secondary sites:**
- Mesenteric lymph nodes.
- Small intestine, especially the ileocaecal region.
- Female genital tract (fallopian tubes).
- Lungs. Concurrent pulmonary TB is present in a minority of patients (not quantified in the retrieved sources).

**Body systems:** digestive and peritoneal, immune and lymphatic.

**Laterality:** diffuse; not lateralized.

---

## 8. Temporal Development

- **Onset:** insidious and subacute. Symptoms usually last weeks to months before diagnosis. A longer delay between symptoms and diagnosis increases mortality (Taiwan series of 211 cases, cited in [search summary](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_916149268); PMID not retrieved).
- **Course:** progressive without therapy. Remission depends on treatment; I found no data on spontaneous remission.
- **Critical period:** the time spent waiting for culture results. Mortality was "high among patients waiting for the results of mycobacterial cultures of ascitic fluid samples" (PMID 12145724).

---

## 9. Inheritance and Population

- **Inheritance:** not applicable. TBP is acquired. MSMD susceptibility genes such as *IL12RB1* are autosomal recessive ([PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)).
- **Share of TB burden:** "Abdominal TB constitutes approximately 12% of extrapulmonary TB cases and 1 to 3% of total TB cases" (as quoted in the search results; [PMC4929092](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929092) / [PMC7446809](https://pmc.ncbi.nlm.nih.gov/articles/PMC7446809)). I retrieved no population incidence for peritoneal TB alone.
- **Rising extrapulmonary share:** the extrapulmonary share of TB has risen in recent years. France had an incidence of 8.7 per 100,000, with 27% of cases extrapulmonary ([PMC7446809](https://pmc.ncbi.nlm.nih.gov/articles/PMC7446809)).
- **Sex and age:** "affects both sexes equally, and most commonly impacts those 35–45 years old" ([PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)).
- **Geography:** TB-endemic regions (South and East Asia, sub-Saharan Africa). In low-incidence countries, cases occur in migrants. Detailed figures were not retrieved.
- **Peritoneal dialysis population:** a 35-year Taiwanese cohort of 2,084 PD patients found 18 TBP cases (PMID 36632795, [PMC9848244](https://pmc.ncbi.nlm.nih.gov/articles/PMC9848244)).

---

## 10. Diagnostics

**Ascitic fluid tests**
- **Basic profile:** exudate, lymphocyte-predominant, SAAG <1.1 g/dL (PMID 28185616).
- **ADA:**
  - 2006 pooled analysis (4 studies, 264 patients): sensitivity 100% and specificity 97% at cut-offs of 36–40 IU/L (PMID 16940883).
  - 2013 meta-analysis (16 studies): pooled sensitivity 0.93 (95% CI 0.89–0.95) and specificity 0.96 (0.94–0.97); "relatively sensitive and specific" ([PMC3776182](https://pmc.ncbi.nlm.nih.gov/articles/PMC3776182)).
  - An updated meta-analysis rated certainty of evidence as very low by GRADE ([PMC10323525](https://pmc.ncbi.nlm.nih.gov/articles/PMC10323525)).
  - ADA is a nonspecific marker of T-cell activation ([Thieme commentary](https://thieme-connect.de/products/ejournals/html/10.1055/s-0042-1757402)). False positives occur with lymphoma ([PMC7193293](https://pmc.ncbi.nlm.nih.gov/articles/PMC7193293)), malignant and pancreatic ascites ([PMC7035809](https://pmc.ncbi.nlm.nih.gov/articles/PMC7035809)).
- **Ascitic IFN-γ:** pooled sensitivity 0.93 (0.87–0.97) and specificity 0.99 (0.97–1.00) (WJG 2013, PMID 23539367, [PMC3602483](https://pmc.ncbi.nlm.nih.gov/articles/PMC3602483)). Sensitivity may be lower in HIV.
- **IGRA (T-SPOT.TB) on blood or fluid:** a supplementary test ([PMC7109547](https://pmc.ncbi.nlm.nih.gov/articles/PMC7109547)).

**Microbiology**
- Ascitic smear and culture have low yield because the disease is paucibacillary. Culture is slow (PMID 12145724; Sanai & Bzeizi 2005).
- Xpert MTB/RIF on peritoneal *tissue* had 60.7% sensitivity and 100% specificity ([PMC6713244](https://pmc.ncbi.nlm.nih.gov/articles/PMC6713244)). I retrieved no pooled data for Xpert on ascitic fluid.

**Laparoscopy and biopsy**
- Laparoscopy with peritoneal biopsy is usually required. The view shows whitish tubercles, adhesions and omental thickening. Histology shows caseating granulomas, with culture or PCR of the tissue.
- Sanai & Bzeizi recommend diagnostic laparoscopy for unexplained lymphocytic ascites ([sindex](https://sindex.sdl.edu.sa/esploro/outputs/journalArticle/Systematic-review-tuberculous-peritonitis--presenting-features-diagnostic/9921392708331)).
- Peritoneal biopsy allowed early definitive diagnosis in the Hong Kong series (PMID 12145724).

**Imaging:** ultrasound and CT show ascites (often with septations), smooth peritoneal thickening, omental caking and mesenteric lymphadenopathy, sometimes with necrotic centres. These features were not quantified in the retrieved sources.

**Differential diagnosis:**
- peritoneal carcinomatosis, which is the main mimic (also shows high CA-125 and peritoneal nodules);
- lymphoma, which can raise ADA;
- cirrhotic ascites (high SAAG);
- spontaneous bacterial peritonitis (neutrophilic);
- pancreatic ascites ([PMC10323525](https://pmc.ncbi.nlm.nih.gov/articles/PMC10323525); [PMC7193293](https://pmc.ncbi.nlm.nih.gov/articles/PMC7193293)).

**Genetic testing:** not routine. Consider an MSMD/inborn-errors panel (*IL12RB1*, *IFNGR1*, *IFNGR2*, *STAT1* and others) for children with disseminated or recurrent mycobacterial disease ([PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)).

**Screening:** no TBP-specific screening. Screening for latent TB is advised before dialysis and immunosuppression (general guidance).

---

## 11. Outcome/Prognosis

**Mortality**
- Mortality is high when diagnosis is delayed. Risk factors include older age, cirrhosis and delay in therapy (PMID 12145724; [secondary summary](https://www.medicalalgorithms.com/risk-factors-for-mortality-in-a-patient-with-tuberculous-peritonitis)).
- **PD-associated TBP:**
  - Taiwan cohort: 1-year mortality 38.9% (7/18), mostly from sepsis. Age was the only significant factor on univariate analysis. One death was from anti-TB drug-induced liver failure (PMID 36632795).
  - Systematic review with ANZDATA registry data: mortality about 33% in case studies, 26% in cohort studies and 6% in registry cases (PMID 38344729, *Kidney Int Rep* 2024).
- **Treated cohorts (Cochrane trials):** deaths were 1.3% with 6-month and 2.8% with 9-month therapy (PMID 27801499).

**Complications:** bowel obstruction from adhesions, fistula and abscess, sepsis, drug-induced hepatotoxicity, and loss of the PD catheter or technique failure.

**Recovery:** cure is likely with timely therapy. Cure rates were similar for 6- and 9-month regimens (Section 12).

**Prognostic biomarkers:** none validated.

---

## 12. Treatment

**Standard regimen**
- Six months of first-line drugs: 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol (HRZE), then 4 months of HR (Sanai & Bzeizi 2005).
- NCIT labels (IDs not verified): Isoniazid; Rifampin; Pyrazinamide; Ethambutol; Antitubercular Agent.
- CHEBI labels: isoniazid, rifampicin, pyrazinamide, ethambutol.

**Duration evidence.** The Cochrane review (Jullien et al. 2016; PMID 27801499) pooled 3 RCTs with 328 participants from India and South Korea, including NCT01124929 ([clinicaltrials.gov](https://clinicaltrials.gov/study/NCT01124929)). It found "probably no difference in the proportion of participants that achieved clinical cure between six-month and nine-month regimens (RR 1.02, 95% CI 0.97 to 1.08; 294 participants, 3 trials, moderate quality evidence)". The evidence on relapse was very low certainty, and there were no data for children or people with HIV ([Cochrane](https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012163.pub2/information)).

**Pharmacogenomics:** *NAT2* acetylator status affects isoniazid hepatotoxicity. This is general knowledge and not retrieved for TBP. It matters given the hepatotoxicity death reported in PD patients (PMID 36632795).

**Adjuncts and surgery**
- Corticosteroids to prevent adhesions are of uncertain benefit. No data were retrieved.
- Surgery (adhesiolysis, resection) is reserved for obstruction, perforation or abscess.
- In PD-associated TBP, catheter removal is sometimes performed (PMID 36632795; PMID 38344729).

**Supportive care:** nutrition, HIV care (ART) and management of liver disease.

**Advanced therapies (gene, cell, RNA, targeted):** none are relevant to TBP. Recombinant IFN-γ and haematopoietic stem cell transplantation are considered for MSMD (PMID 40656276).

---

## 13. Prevention

- **Primary prevention:** TB control, treatment of latent TB in high-risk groups (dialysis, cirrhosis, HIV, anti-TNF therapy), and BCG (protects mainly against severe childhood TB). Pasteurized milk prevents *M. bovis* infection. These points are general knowledge and not TBP-specific sources.
- **Secondary prevention:** test early with ADA, IFN-γ or laparoscopy for lymphocytic low-SAAG ascites, rather than waiting for culture (PMID 12145724; PMID 28185616).
- **Tertiary prevention:** monitor liver function during treatment and watch for obstruction.
- **Genetic counseling:** only for MSMD families.

---

## 14. Other Species / Natural Disease (limited evidence)

The search on this topic failed, so these points are not sourced in this report:
- Peritoneal and serosal TB, known as "pearl disease", is a classic lesion of bovine TB caused by *M. bovis* in cattle.
- *M. bovis* is zoonotic, spread through unpasteurized milk.
- Mycobacterial peritonitis occurs sporadically in other mammals.

No OMIA entry applies, because this is not a Mendelian condition.

---

## 15. Model Organisms (limited evidence)

No sources were retrieved because the search failed.
- Mouse models of TB (low-dose aerosol, or intravenous or intraperitoneal *M. tuberculosis*/BCG infection) and zebrafish *M. marinum* granuloma models are used for TB in general.
- No validated model that recapitulates TBP (ascites, peritoneal studding) was identified.
- Knockout mice (*Ifng*, *Il12rb1*, *Tnf*) model susceptibility to IFN-γ axis defects (unverified).

---

## Key PMIDs retrieved

| PMID | Source |
|---|---|
| 28185616 | Microbiol Spectr review |
| 31293914 | Wu et al. 2019 review |
| 12145724 | Chow et al., CID 2002 |
| 36632795 | Taiwan PD cohort |
| 38344729 | PD TBP systematic review, 2024 |
| 27801499 | Cochrane 6-month therapy |
| 16940883 | 2006 ADA meta-analysis |
| 23539367 | IFN-γ meta-analysis |
| 40656276 | MSMD overview |
| 19084940 | Pediatric series (not read) |
| 24049517 | Arch Med Sci 2013 ADA meta-analysis (identifier taken from the scite URL) |

The Sanai & Bzeizi 2005 systematic review is cited by DOI 10.1111/j.1365-2036.2005.02645.x because its PMID was not retrieved.

**Sources:**
- [PMC6609850](https://pmc.ncbi.nlm.nih.gov/articles/PMC6609850)
- [PMID 28185616](https://pubmed.ncbi.nlm.nih.gov/28185616/)
- [PMC3776182](https://pmc.ncbi.nlm.nih.gov/articles/PMC3776182)
- [PMC10323525](https://pmc.ncbi.nlm.nih.gov/articles/PMC10323525)
- [PMC7035809](https://pmc.ncbi.nlm.nih.gov/articles/PMC7035809)
- [PMC7193293](https://pmc.ncbi.nlm.nih.gov/articles/PMC7193293)
- [Thieme commentary](https://thieme-connect.de/products/ejournals/html/10.1055/s-0042-1757402)
- [Frontiers Public Health 2022](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.938544/pdf)
- [PMC9848244](https://pmc.ncbi.nlm.nih.gov/articles/PMC9848244)
- [PMC7320463](https://pmc.ncbi.nlm.nih.gov/articles/PMC7320463)
- [BVS mdl-38344729](https://pesquisa.bvsalud.org/portal/resource/en/mdl-38344729)
- [Sanai & Bzeizi (scilit)](https://www.scilit.net/publications/5bc254666b96eac771a8e730db5d7bcc)
- [Sanai & Bzeizi (sindex)](https://sindex.sdl.edu.sa/esploro/outputs/journalArticle/Systematic-review-tuberculous-peritonitis--presenting-features-diagnostic/9921392708331)
- [Cochrane CD012163](https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012163.pub2/information)
- [NCT01124929](https://clinicaltrials.gov/study/NCT01124929)
- [PMC3602483](https://pmc.ncbi.nlm.nih.gov/articles/PMC3602483)
- [PMC6713244](https://pmc.ncbi.nlm.nih.gov/articles/PMC6713244)
- [PMC7109547](https://pmc.ncbi.nlm.nih.gov/articles/PMC7109547)
- [PMC6307147](https://pmc.ncbi.nlm.nih.gov/articles/PMC6307147)
- [PMC4929092](https://pmc.ncbi.nlm.nih.gov/articles/PMC4929092)
- [PMC7446809](https://pmc.ncbi.nlm.nih.gov/articles/PMC7446809)
- [BVS mdl-12145724](https://pesquisa.bvsalud.org/paraguay/resource/es/mdl-12145724)
- [Medical Algorithms summary](https://www.medicalalgorithms.com/risk-factors-for-mortality-in-a-patient-with-tuberculous-peritonitis)
- [Taiwan 211-case series](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_916149268)
- [PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)
- [PMID 40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/)
- [Frontiers Immunol 2023 case](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1135824/full)
- [Frontiers Immunol 2022 MSMD review](https://frontiersin.org/articles/10.3389/fimmu.2022.926781/pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 28 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC6307147` *(abstract only)*: "Peritoneal TB is the most common presentation of abdominal TB"
  - closest text in source: "Diagnosis of abdominal TB was confirmed using microbiologic and/or histologic methods in 76 patients (confirmed diagnosis), while the remaining 63 patients were diagnosed based on clinical presentation and radiologic imaging (clinical diagnosis)"
- `PMC:PMC6307147` *(abstract only)*: "Risk factors for developing peritoneal TB include states of immunosuppression (most prominently HIV/AIDS), kidney failure requiring dialysis, cirrhosis, and malnutrition"
  - closest text in source: "According to diagnostic method, frequency of clinical diagnosis was highest in patients with luminal (50.7%) or peritoneal (64.3%) TB, while frequency of microscopic diagnosis was highest in patients with visceral TB (68.2%), and frequency of histologic diagnosis was highest in patients with nodal TB (85.2%)"
- `PMID:40656276` *(abstract only)*: "the more virulent M. tuberculosis has also caused disease in some MSMD patients"
  - closest text in source: "MSMD patients present with disseminated BCGosis or with symptoms of non-tuberculous Mycobacterium (NTM)"
- `PMID:12145724` *(abstract only)*: "high among patients waiting for the results of mycobacterial cultures of ascitic fluid samples"
  - closest text in source: "Thirty-one patients died, 26 of whom died < or =6 weeks after their initial presentation, often before the result of mycobacterial culture was available"
- `PMC:PMC4929092` *(abstract only)*: "Abdominal TB constitutes approximately 12% of extrapulmonary TB cases and 1 to 3% of total TB cases"
  - closest text in source: "Bacteriology was positive for ascites in only 58.1% of cases, for peritoneal biopsy in 73.3%, while granuloma was found in 95.5%"
- `PMC:PMC7446809` *(abstract only)*: "Abdominal TB constitutes approximately 12% of extrapulmonary TB cases and 1 to 3% of total TB cases"
  - closest text in source: "TB also affects other sites (extrapulmonary tuberculosis, EPTB), and accounts for a significant proportion of tuberculosis cases worldwide"
- `PMC:PMC6307147` *(abstract only)*: "affects both sexes equally, and most commonly impacts those 35–45 years old"
  - closest text in source: "In this study, we aimed to highlight the clinical features, diagnostic methods, and outcomes of abdominal TB over 12 years in Southeastern Korea"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0006000` - called "peritonitis caused by *Mycobacterium tuberculosis", "supplied in the request"

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0006000` (3 mentions)

No term could be looked up either way, so nothing here was confirmed or contradicted.