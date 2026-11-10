---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-09T19:47:16.972076'
end_time: '2026-11-09T19:53:36.198115'
duration_seconds: 379.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Craniosynostosis 4
  mondo_id: MONDO:0010929
  category: Mendelian
  causal_genes: ERF
  omim_id: OMIM:600775
  synonyms: craniosynostosis type 4; ERF craniosynostosis; ERF-related craniosynostosis;
    craniosynostosis caused by mutation in ERF
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
  web_search_requests: 5
  num_turns: 39
  total_cost_usd: 3.1875597
  session_id: c6e37e71-0e50-49f8-aa47-d2f719d637fd
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 10
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 32
  on_topic: 9
  validator_version: 0.5.1
term_validation:
  total_terms: 78
  verified: 75
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniosynostosis 4
- **MONDO ID:** MONDO:0010929 (if available)
- **Causal gene(s):** ERF
- **OMIM:** OMIM:600775
- **Synonyms:** craniosynostosis type 4; ERF craniosynostosis; ERF-related craniosynostosis; craniosynostosis caused by mutation in ERF
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Craniosynostosis 4** covering all of the
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

I'm reading the ERF papers already cached in the repository and will check them against PubMed sources next.

I've read the cached ERF papers. Next I'm searching PubMed for the remaining key studies: the Glass phenotype series, the mouse mechanism papers and the ClinGen classification.

I have the main abstracts. Next I'm checking the ClinGen classification, the Orphanet and OMIM identifiers, and the hgnc: CURIE for ERF.

Now I'm checking the HPO, GO, CL and UBERON term caches so that every identifier in the report comes from a lookup.

# Craniosynostosis 4 (CRS4; ERF-related craniosynostosis): Research Report

**Target:** Craniosynostosis 4 · MONDO:0010929 · OMIM #600775 · causal gene **ERF** (ETS2 repressor factor; `hgnc:3444`; OMIM *611888; chromosome 19q13.2) · autosomal dominant

**Bottom line:** CRS4 is caused by heterozygous loss-of-function variants in ERF, a transcriptional repressor that ERK1/2 switch off. The skull sutures are unusually sensitive to how much ERF a cell has. The phenotype is mostly multi-suture fusion that starts after birth, often the sagittal and lambdoid sutures, with a Crouzon-like face. It carries a high risk of Chiari I malformation and of raised intracranial pressure that nobody suspected. Speech, language and attention problems are common. ClinGen classifies ERF–CRS4 as **Definitive**. The only targeted treatments (MEK and nuclear-export inhibitors) have been tested in mice only.

### How to read the citations
- **Verbatim, from the local cache:** checked character for character against the `references_cache/` files in this repo.
- **Fetched fragment:** a short excerpt returned by an automated PubMed abstract fetch. It has not been checked byte for byte. Re-fetch with `just fetch-reference PMID:<n>` before using it as an evidence snippet.
- **Ontology CURIEs:** every one comes from the repo's `cache/*/terms.csv` label caches. A concept with no cached term is marked *"no cached term; look up before binding"* rather than given a CURIE from memory. Dynamic-enum membership has not been checked; run `just validate-terms` after binding.

**Existing KB entry:** `kb/disorders/Craniosynostosis_4.yaml` is currently an 8-line skeleton. It holds only the name, creation date, category and the MONDO:0010929 binding, so all of the content below would be new.

---

## 1. Disease Information

**Overview.** CRS4 is an autosomal dominant craniosynostosis syndrome caused by reduced dosage of ERF. Twigg et al. (2013) first described it in 12 families:

> "reduced dosage of ERF, which encodes an inhibitory ETS transcription factor directly bound by ERK1/2 … causes complex craniosynostosis (premature fusion of the cranial sutures) in humans and mice. Features of this newly recognized clinical disorder include multiple-suture synostosis, craniofacial dysmorphism, Chiari malformation and language delay." — PMID:23354439, verbatim, local cache (Nat Genet 2013)

**Identifiers**

| Resource | ID | Note |
|---|---|---|
| MONDO | MONDO:0010929 "craniosynostosis 4" | Already bound in the KB stub |
| OMIM | #600775 (phenotype); *611888 (ERF gene) | |
| Orphanet | ORDO:647681 reported by a mirror; **unconfirmed** | The cached `ORPHA:207` (**Crouzon syndrome**) lists "ERF \| ETS2 repressor factor \| hgnc:3444 \| Disease-causing germline mutation(s) (loss of function) in", so Orphanet files ERF under Crouzon. Treat this as a mapping question; see the `mapping-analysis` skill. |
| UMLS | C3806917 | |
| HGNC | hgnc:3444 ERF | Cached |
| ICD-10 / ICD-11 | No disease-specific code. Craniosynostosis is classed under Q75.0 (ICD-10) or LB70 (ICD-11) | Codes recalled from memory, not looked up |

**Synonyms:** craniosynostosis type 4; CRS4; ERF-related craniosynostosis (the name Twigg et al. coined); ERF-related craniosynostosis syndrome; craniosynostosis caused by mutation in ERF.

**Allelic ERF disorders.** These must be kept separate from CRS4 (see the lump/split note in §10):
- **Chitayat syndrome** (CHYTS; OMIM #617180; MONDO:0014956, cached). Caused by the recurrent missense p.(Tyr89Cys) in the ETS domain (PMID:27738187, PMID:30569521).
- **Noonan syndrome-like phenotype with or without craniosynostosis.** Caused by truncating variants (PMID:38824261, PMID:34184330, PMID:38741564, PMID:40307313). PanelApp Australia submits ERF–Noonan syndrome (MONDO:0018997) to GenCC as Strong.
- **MIDES syndrome** (microcephaly, developmental delay, skeletal anomalies). Caused by in-frame variants that disrupt the ERK-docking FSF motif (PMID:39668184).

**Data provenance.** Everything here is aggregated case-series and disease-level knowledge (OMIM, GenCC/ClinGen, PanelApp, published cohorts). No EHR data were used.

---

## 2. Etiology

**Cause.** CRS4 is caused by a germline heterozygous loss-of-function (LoF) variant in ERF. Twigg et al. found heterozygous LoF mutations in 11 of 411 unrelated craniosynostosis patients and in none of 288 controls:

> "Heterozygous loss-of-function mutations were present in a further 11 patient samples but in no normal controls (P = 0.004, Fisher's exact test)" — PMID:23354439, verbatim, local cache

The paper also found multiple de novo cases. It concluded:

> "These data suggest that the predominant pathophysiological mechanism is heterozygous loss-of-function (haploinsufficiency)." — PMID:23354439, verbatim, local cache

Whole-gene deletions at 19q13.2 also cause the phenotype. Larger deletions that also remove neighbouring genes, especially **CIC** (`hgnc:14214`), add intellectual disability (PMID:33993607 Calpena 2021; PMID:34117072 Singh 2021).

**Genetic risk factors and modifiers**
- No population susceptibility loci are known.
- Rare damaging ERF variants are enriched in apparently *non-syndromic single-suture* craniosynostosis. Clarke et al. (2018) found "a significant increase in damaging variants in ATR, EFNA4, ERF" (fetched fragment, PMID:29168297). Because most of those variants were inherited, the authors point to reduced penetrance and possibly oligogenic factors.
- No specific modifier gene has been proven. Variable expressivity within families is the rule (PMID:35852485, PMID:32370745).
- There is one case of ERF-related craniosynostosis co-occurring with hypochondroplasia (FGFR3) (PMID:39967053). It is a single case and no modifier claim should be drawn from it.

**Environmental risk, protective factors and gene–environment interactions:** none reported. Two caveats:
- Mouse data link Erf to retinoic acid (RA) catabolism (§6), but no human exposure link is known.
- Not applicable for curation: do not infer RA-exposure effects in humans.

---

## 3. Phenotypes

The main sources are Twigg 2013 (PMID:23354439; 26 mutation carriers), Glass 2019 (PMID:30758909; 16 probands plus 20 relatives), Chaudhry 2015 (PMID:26097063), Care 2022 (PMID:35761471), Afshari 2023 (PMID:36209295) and Moddemann 2022 (PMID:35852485).

| Phenotype | HPO (cached) | Frequency / characteristics | Key source |
|---|---|---|---|
| Craniosynostosis (any) | HP:0001363 Craniosynostosis | 13 of 14 paediatric carriers. Adult carriers often show only mild facial signs or macrocephaly | PMID:23354439 |
| Multiple-suture synostosis | HP:0011324 Multiple suture craniosynostosis | 7 of 12 probands (13-fold enrichment over other diagnostic groups). The commonest pattern | PMID:23354439, PMID:30758909 |
| Sagittal synostosis | HP:0004442 Sagittal craniosynostosis | 7 of 8 with CT. Part of the sagittal + lambdoid "Mercedes-Benz" pattern | PMID:23354439, PMID:30758909 |
| Lambdoid synostosis | *no cached term; look up before binding* | 5 of 8 with CT | PMID:23354439 |
| Coronal synostosis | HP:0004440 Coronal craniosynostosis | 3 of 8 with CT | PMID:23354439 |
| Metopic synostosis | HP:0011330 Metopic synostosis | 1 of 8 with CT | PMID:23354439 |
| Postnatal, insidious onset; delayed presentation | (onset descriptor: childhood) | Median age at presentation 42 months ("a median age at presentation of 42 months among the probands", fetched fragment). Primary delayed onset at 4 years has been reported | PMID:30758909, PMID:35313736 |
| Raised intracranial pressure | HP:0002516 Increased intracranial pressure (papilledema HP:0001085 as a sign) | Raised ICP documented in 9 of 26 carriers; may be clinically silent | PMID:23354439, PMID:32370745 |
| Chiari I / tonsillar herniation | HP:0007099 Chiari type I malformation | 4 of 26 (Twigg); 8 of 10 before surgery (Afshari: "low-lying tonsils/hind brain hernia", fetched fragment) | PMID:23354439, PMID:36209295 |
| Hypertelorism | HP:0000316 Hypertelorism | Consistent finding on 3-D facial scanning | PMID:23354439, PMID:30758909 |
| Exorbitism / proptosis | HP:0000520 Proptosis | Mild; frequent | PMID:23354439, PMID:26097063 |
| Midface hypoplasia / malar hypoplasia | HP:0011800 Midface retrusion; HP:0000272 Malar flattening | Frequent; Class I occlusion (unlike Crouzon) | PMID:30758909 |
| Short / vertically displaced nose | HP:0003196 Short nose | Consistent on 3-D scanning | PMID:23354439 |
| Prominent forehead | HP:0002007 Frontal bossing | Consistent | PMID:23354439 |
| Macrocephaly | HP:0000256 Macrocephaly | Common in carriers, including adults with no synostosis | PMID:23354439, PMID:38824261 |
| Scaphocephaly / dolichocephaly | HP:0030799 Scaphocephaly; HP:0000268 Dolichocephaly | Dolichocephalic skull without synostosis in 10 subjects of the NS-like cohort | PMID:38824261 |
| Speech / language delay | HP:0000750 Delayed speech and language development | Most frequent neurodevelopmental feature; 12 of 14 (86%) paediatric cases had behavioural or learning problems | PMID:23354439, PMID:35761471 |
| Attention / hyperactivity problems | HP:0007018 ADHD; HP:0000752 Hyperactivity | Common | PMID:30758909, PMID:35761471 |
| Poor fine motor control | HP:0007010 Poor fine motor coordination | Common | PMID:35761471, PMID:30758909 |
| Learning difficulty (IQ usually not globally reduced) | HP:0001328 Specific learning disability | Variable | PMID:35761471 |
| ENT problems / conductive hearing loss | HP:0000403 Recurrent otitis media; HP:0000405 Conductive hearing impairment | "common … to have needed input from ear, nose and throat services" (fetched fragment) | PMID:35761471 |
| Brachydactyly (mild shortening of digits) | HP:0001156 Brachydactyly | Occasional (Twigg); all 6 members of one family (Moddemann) | PMID:23354439, PMID:35852485 |
| Overweight / obesity | HP:0001513 Obesity | 5 of 6 in one family; not established across cohorts | PMID:35852485 |
| Short stature | HP:0004322 Short stature | About two-thirds in the NS-like cohort, which is a different ascertainment | PMID:38824261 |
| Ptosis, low-set ears, wide nasal bridge | HP:0000508; HP:0000369; HP:0000431 | Mainly in the NS-like cohort | PMID:38824261 |
| Nephroblastoma | HP:0002667 Nephroblastoma | 1 individual (unilateral Wilms). Not a proven association | PMID:38824261 |

**Course and severity.** Severity is variable and often mild in adults. Progression is mainly in childhood: suture fusion progresses after birth, and the main risk is raised ICP with or without Chiari I. Twigg noted:

> "no health problems of later onset were consistently found in carrier adults, in many of whom mild craniofacial signs or macrocephaly were the only features" — PMID:23354439, verbatim, local cache

**Quality of life.** No EQ-5D, SF-36 or disease-specific QoL data exist. The burden comes from repeat neurosurgery, developmental and communication needs (PMID:35761471), and ENT and hearing problems.

**Inheritance HPO terms (cached):** HP:0000006 Autosomal dominant inheritance; HP:0003828 Variable expressivity; HP:0003829 Typified by incomplete penetrance.

---

## 4. Genetic / Molecular Information

**Gene.** ERF, `hgnc:3444`, 19q13.2, 4 exons. It encodes an ETS-family repressor with three regions:
- an N-terminal ETS DNA-binding domain (core GGAA/T motif);
- a central ERK-interaction region containing an FxF-type "FSF" docking motif;
- a C-terminal repressor domain.

(PMID:23354439; the FSF motif is from PMID:39668184.)

> "Functionally characterized motifs in ERF comprize the N-terminal DNA-binding (ETS), central ERK interaction, and C-terminal repressor domains" — PMID:23354439, verbatim, local cache

**Variant spectrum in CRS4.** Variants are heterozygous and germline, de novo or inherited.
- Nonsense (e.g. c.547C>T p.Arg183*, the index family), frameshift (including a recurrent one), splice-site and start-loss variants.
- Missense at critical residues of the ETS domain. These are expressed normally but fail to repress ETS-site promoters.
- Whole-gene deletions.
- Example variant: c.1201_1202del p.(Lys401Glufs*10), a mother–son pair with differing suture patterns and raised ICP in both (PMID:32370745).

Sources: PMID:23354439, PMID:26097063, PMID:32370745, PMID:33993607.

**Functional consequence.** Loss of function, i.e. haploinsufficiency (HGVS uses transcript NM_006494). Twigg reported reduced full-length protein with truncating and start-loss variants, and loss of repressor function with ETS-domain missense variants (PMID:23354439). For curation this means `functional_impact_category: LOSS_OF_FUNCTION`, `variant_origin: GERMLINE`, `zygosity: HETEROZYGOUS`. No genotype–phenotype correlation was evident within CRS4 (PMID:23354439).

**How variant class maps to the allelic disorders.** This is important for the lump/split decision:

| Variant class | Disorder | Source |
|---|---|---|
| Truncating / null variants and some ETS-domain missense | CRS4 | PMID:23354439 |
| Truncating variants | Also the NS-like phenotype, with craniosynostosis in only 3 of 15 families (likely an ascertainment difference along one LoF spectrum) | PMID:38824261 |
| Recurrent p.(Tyr89Cys) (c.266A>G; rs886041001) in the ETS domain | Chitayat syndrome (hyperphalangism, bronchomalacia) | PMID:27738187, PMID:30569521 |
| In-frame c.911_913del / c.907T>A in the FSF ERK-docking motif | MIDES. These variants *impair ERK binding and increase nuclear ERF*, the opposite direction of effect from CRS4 | PMID:39668184 |

**Gene–disease validity (GenCC, retrieved 2026-11-09)**

| Disease (MONDO) | Submitter | Classification |
|---|---|---|
| CRS4 (MONDO:0010929) | **ClinGen** (Cranio GCEP; PMID:42059179 describes the panel) | **Definitive**, AD |
| CRS4 | G2P | Definitive |
| CRS4 | Genomics England PanelApp | Strong (gene is Green on panel 168) |
| CRS4 | Labcorp / Invitae | Strong |
| CRS4 | Ambry | Moderate |
| Chitayat syndrome (MONDO:0014956) | G2P | Definitive |

For KB use: per CLAUDE.md, record the ClinGen tier only by copying a cached `CGGV:` record. None is cached locally yet, so the `CGGV:` assertion needs to be fetched first.

**Population frequency, modifiers, epigenetics.**
- gnomAD frequencies and constraint metrics were not retrieved. Look them up before stating any.
- LoF variants are absent from controls (0 of 288 north European controls; PMID:23354439).
- No modifier genes or disease epigenetic signatures are known.

**Chromosomal abnormalities.** 19q13.2 microdeletions that include ERF cause CRS4-like skull findings. Co-deletion of CIC adds developmental delay or intellectual disability (PMID:34117072; PMID:33993607: "Three larger deletions (264-314 kb) that included at least five further centromeric genes", fetched fragment).

---

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors, and the entry should record none.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **A heterozygous ERF LoF variant (germline) leads to about 50% ERF protein dosage** (haploinsufficiency). Shown in patient cells (PMID:23354439).
2. **Lower nuclear ERF reduces repression of ETS- and RUNX-associated targets in sutural osteoprogenitors.**
   - In normal physiology, ERK1/2 phosphorylate ERF and drive it out of the nucleus. Unphosphorylated nuclear ERF represses targets by competing with activating ETS factors (e.g. ETS2) at enhancers that also carry RUNX and AP-1 motifs.
   - ChIP-seq in mouse embryonic fibroblasts showed that Erf binds distal elements enriched for RUNX and AP-1 motifs. In a reporter assay, ERF suppressed RUNX2 transactivation.
   - The step from this to sutural cells is **inferred**: it rests on mouse fibroblast ChIP-seq and HeLa reporters, not on human suture tissue (PMID:23354439).
3. **Branch A, the mouse-supported step: higher Cyp26b1 leads to more retinoic acid breakdown, which impairs osteogenic commitment and differentiation of suture mesenchymal progenitors and initially delays calvarial mineralization.**
   - Vogiatzi 2021: "increased levels of the cytochrome P450 superfamily member Cyp26b1" (fetched fragment). Exogenous RA rescues the differentiation defect (PMID:33972395; ex vivo mouse cells).
   - Consistent with this, Twigg found mildly delayed embryonic calvarial ossification in *Erf^loxP/−* mice:

     > "embryonic calvarial development appears mildly delayed" — PMID:23354439, verbatim, local cache
4. **The early ossification deficit is followed by postnatal premature fusion of several sutures.**
   - In mice the sequence is impaired frontal bone formation and then multisuture synostosis (PMID:37175668).
   - In humans fusion is postnatal and progressive (PMID:30758909).
   - How the early delay turns into later fusion (e.g. compensatory osteogenesis, or depletion of the suture stem-cell niche) is **not established**. Twigg names proliferation, differentiation and apoptosis as untested contributors.
5. **Multisuture (sagittal + lambdoid) synostosis leads to a restricted, posteriorly constrained cranial vault.** That causes **raised ICP** and **crowding of the posterior fossa, giving Chiari I / tonsillar herniation**. This is the clinical inference, supported by the frequencies of both findings (PMID:23354439, PMID:36209295).
6. **Branch B: abnormal cranial-base and facial development leads to hypertelorism, exorbitism and midface hypoplasia.** This is the Crouzon-like face. Its developmental mechanism is not directly studied, so the step is **inferred**.
7. **Neurodevelopmental features (speech/language, attention, fine motor) arise by an unresolved route.** They may come from raised ICP or Chiari, or from a direct CNS role of ERF. The fact that some *carrier parents without craniosynostosis* also show difficulties (PMID:35761471) argues for at least a partly direct effect. This step is **unresolved**.
8. **Dosage sensitivity.** In mice, *Erf^+/−* animals are normal. Only about 30% of normal Erf (*Erf^loxP/−*) gives multisuture synostosis, and Erf^−/− is embryonic-lethal at E10.5 from placental failure (PMID:23354439). Human sutures therefore have a lower tolerance threshold than mouse sutures. This is a species-mismatch point that should be recorded (see §15).

### Checklist detail
- **Pathways:** RAS–MEK–ERK1/2 (MAPK). ERF is a terminal ERK effector. It links to FGFR2 pathway disease, which explains why patients are misdiagnosed as Crouzon. RA signalling (Cyp26b1). RUNX2 osteogenic transcriptional network. Cached GO terms:
  - GO:0070371 ERK1 and ERK2 cascade
  - GO:0000122 negative regulation of transcription by RNA polymerase II (ERF's normal function)
  - GO:0001649 osteoblast differentiation / GO:0045667 regulation of osteoblast differentiation
  - GO:0001957 intramembranous ossification
  - GO:0030282 bone mineralization
  - GO:0060363 cranial suture morphogenesis
  - GO:0034653 retinoic acid catabolic process (`modifier: INCREASED` in the mouse model)
  - GO:0006611 protein export from nucleus (ERK-driven ERF export)
  - GO:0001890 placenta development (homozygous mouse null only)
- **Protein dysfunction:** loss of repressor dosage (CRS4), versus an ETS-domain missense with uncertain mechanism (Chitayat), versus loss of ERK docking that keeps ERF nuclear (MIDES). The first and last move ERF activity in opposite directions.
- **Cell types (cached CL):**
  - CL:0000134 mesenchymal stem cell (suture-derived progenitors; PMID:33972395)
  - CL:0000062 osteoblast
  - CL:0008019 mesenchymal cell
  - CL:0000057 fibroblast (patient fibroblasts, MEF ChIP-seq)
  - CL:0011012 neural crest cell (frontal bone and metopic origin; not studied specifically)
  - CL:0000351 trophoblast cell (mouse null placental defect)
  - Osteoprogenitor: *no cached term; look up before binding*
- **Genes for pathophysiology nodes (cached HGNC):** ERF hgnc:3444; MAPK3 hgnc:6877 / MAPK1 hgnc:6871 (ERK1/2); RUNX2 hgnc:10472; CYP26B1 hgnc:20581; ETS2 hgnc:3489; FGFR2 hgnc:3689.
- **Chemical entities:** CHEBI:15367 all-trans-retinoic acid (cached).
- **Immune, metabolic and tissue-damage mechanisms:** none, apart from secondary pressure effects on brain and optic nerve from raised ICP.
- **Omics:** Erf ChIP-seq in mouse embryonic fibroblasts (PMID:23354439). No human single-cell or spatial data specific to CRS4. Not checked: GEO deposits, if any, for the Vogiatzi datasets; run `just discover-datasets` before adding any.
- **Separate role in blood formation (mouse):** Erf is required for primitive and definitive haematopoiesis (PMID:28694332). This has not been reported in human carriers.

---

## 7. Anatomical Structures Affected

- **Primary:**
  - UBERON:0003685 cranial suture; UBERON:0002489 coronal suture (cached)
  - Sagittal, lambdoid and metopic sutures, plus frontal, parietal and occipital bones: *no cached terms; look up before binding*
  - UBERON:0003129 skull (cached)
- **Secondary:**
  - Hindbrain and posterior fossa (Chiari I); cerebellar tonsil *(no cached term)*
  - Brain (raised ICP; optic disc swelling)
  - UBERON:0001697 orbit of skull (exorbitism)
  - UBERON:0004089 midface (cached)
  - Middle ear (ENT problems)
  - Digits (mild brachydactyly)
- **Body systems:** musculoskeletal (craniofacial skeleton), nervous.
- **Subcellular:** GO:0005634 nucleus. ERF is active in the nucleus and exported to the cytoplasm on ERK phosphorylation.
- **Laterality:** synostosis is often bilateral (e.g. bilateral lambdoid). Unilateral coronal or lambdoid involvement also occurs (PMID:23354439).

---

## 8. Temporal Development

- **Onset:** the variant is present from conception, but suture fusion is **postnatal and insidious**. Median presentation is 42 months (PMID:30758909). Primary delayed onset at 4 years has been reported (PMID:35313736). Neonatal multisuture cases do occur (PMID:41562473; a 6-day-old infant).
- **Progression:** fusion progresses during childhood. Mother and son in one family both developed raised ICP over time ("Both developed intracranial hypertension at some point during the course", fetched fragment, PMID:32370745).
- **Stages:** none formally defined.
- **Disease duration:** lifelong carrier state; adults are largely stable.
- **Critical period:** early childhood, when suture surveillance and ICP monitoring prevent visual and neurocognitive harm. Twigg noted that despite multisuture involvement:

  > "many affected individuals presented after infancy, and primary surgery was frequently delayed" — PMID:23354439, verbatim, local cache

- **Remission:** not applicable.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006). Many cases are familial, some de novo. In Twigg's 4 de novo families the mutation arose from a parent, grandparent or great-grandparent.
- **Penetrance:** incomplete for craniosynostosis. Adult carriers may show only macrocephaly or mild facial signs. Expressivity varies markedly within families (PMID:35852485, PMID:32370745).
- **Anticipation:** none. Germline mosaicism: not reported. Founder effects: none reported. A search for a Moroccan-Jewish founder found no support.
- **Frequency among craniosynostosis patients:**
  - 1.2% (5 of 402) of patients needing surgery in the Oxford cohort (PMID:23354439, verbatim, local cache: "identified in 5/402 (1.2%) of patients requiring surgery for craniosynostosis")
  - About 2% of syndromic and 0.7% of clinically non-syndromic craniosynostosis (PMID:30758909)
  - 5% (2 of 40) of multisuture or sagittal cases (PMID:26097063; "We identified heterozygous ERF mutations in two individuals (5%).", fetched fragment)
  - ERF is the 5th most common monogenic cause, after FGFR2, FGFR3, TWIST1 and TCF12 (PMID:27884935, verbatim, local cache: "in decreasing order of frequency: FGFR2, FGFR3, TWIST1, TCF12, ERF and EFNB1")
- **Birth prevalence (derived estimate only):** craniosynostosis overall is "∼1 in 2250 births" (PMID:27884935). Multiplying by about 1% gives roughly 1 in 200,000 births. **This is my own calculation, not a published figure**, and must not be recorded as `rate_per_100000`. A defensible KB record is `measure_type: CASES_IN_LITERATURE` or UNKNOWN with `prevalence_class: RARE`.
- **Sex ratio and geography:** no bias reported. Cases are reported from the UK, Europe, the USA, Japan, China, Turkey and Thailand.

---

## 10. Diagnostics

- **Imaging:**
  - 3-D CT of the skull to map suture fusion (NCIT:C17204 Computed Tomography)
  - MRI for Chiari I, tonsillar position and hydrocephalus (NCIT:C16809 Magnetic Resonance Imaging)
  - Fundoscopy for papilledema (NCIT:C120698 Ophthalmoscopy)
  - Invasive ICP monitoring when indicated
- **Laboratory or biomarkers:** none.
- **Genetic testing:**
  - Craniosynostosis multigene panels include ERF (PanelApp panel 168, Green).
  - Exome or genome sequencing: NCIT:C101295 Whole Exome Sequencing; NCIT:C101294 Whole Genome Sequencing. ERF variants are found on genome-wide analysis of panel-negative patients (PMID:38318288, PMID:27884935).
  - MLPA or CMA for 19q13.2 deletions (NCIT:C116161 Multiplex Ligation-dependent Probe Amplification), particularly when developmental delay suggests a contiguous deletion with CIC.
  - Routine UK testing has included full-gene ERF sequencing (PMID:27884935).
- **Clinical clues:**
  - multisuture synostosis, especially sagittal + lambdoid ("Mercedes-Benz");
  - postnatal or late presentation;
  - Crouzon-like face with a Class I bite;
  - FGFR2-negative "Crouzon";
  - Chiari I;
  - mildly affected macrocephalic parent.
- **Differential diagnosis:**
  - Crouzon / Pfeiffer (FGFR2; usually Class III malocclusion and earlier presentation)
  - Saethre-Chotzen (TWIST1)
  - TCF12-related (coronal-predominant)
  - Noonan syndrome and other RASopathies (overlap with ERF NS-like presentations; consider SHOC2, PMID:25123707)
  - Chitayat syndrome (p.Tyr89Cys; hyperphalangism, respiratory problems)
  - Secondary or positional skull shape
- **Lump/split note for curation:**
  - Keep CRS4 (MONDO:0010929) and Chitayat (MONDO:0014956) as separate entries.
  - The NS-like ERF phenotype is best handled as a phenotype variant or subtype of the same LoF condition, or as a note.
  - PMID:40840652 calls a **frameshift** case (p.Lys401Glufs*10) "Chitayat syndrome". That is the same variant reported in a CRS4 family (PMID:32370745), and it conflicts with the definition of Chitayat as specific to Tyr89Cys. That paper also cites RefSeq NM_001429.3. I believe (unchecked) that this accession belongs to EP300, not ERF (ERF is NM_006494). Do not cite it as evidence for Chitayat syndrome.
  - The Chitayat abstract itself types the variant once as "c.266A>C" where it means c.266A>G. Do not "correct" this inside a snippet.
- **Screening:** there is no newborn screening. Cascade testing of relatives is appropriate because carriers may be mildly affected.

---

## 11. Outcome / Prognosis

- **Life expectancy:** no reported excess mortality. Adult carriers have no consistent later-onset health problems (PMID:23354439).
- **Morbidity:**
  - Raised ICP, sometimes unsuspected, with a risk of visual loss
  - Chiari I with or without syringomyelia
  - Repeat surgery in some patients (one series reported that its individuals "did not require repeated cranial surgeries", fetched fragment, PMID:26097063; other series needed multiple procedures)
  - Speech, language and communication difficulties
  - ENT and hearing problems
- **Cognition:** overall intelligence is usually not consistently impaired; attention, impulsivity and fine motor skills are affected (PMID:35761471).
- **Prognostic factors:**
  - Multisuture involvement predicts surgery for raised ICP or Chiari (PMID:30758909).
  - Larger 19q13.2 deletions that include CIC predict intellectual disability (PMID:33993607).
- **QoL instruments:** no published data.

---

## 12. Treatment

| Treatment | NCIT (cached) | Notes |
|---|---|---|
| Cranial vault surgery (posterior vault expansion or remodelling; fronto-orbital advancement) | NCIT:C15214 Craniotomy, or NCIT:C15656 Neurosurgical Procedure; `therapeutic_modality: SURGERY` | Individualised; mean age at surgery 21.6 months in one cohort (PMID:36209295). Early posterior decompression at 2 months has been reported (PMID:41562473) |
| Posterior fossa / Chiari decompression | NCIT:C15656 Neurosurgical Procedure | For symptomatic hindbrain herniation (PMID:36209295) |
| CSF diversion when hydrocephalus is present | NCIT:C168483 Ventriculoperitoneal Shunt Placement | Not specifically reported for ERF; general craniosynostosis guideline (PMID:33156164) |
| Surveillance for raised ICP | NCIT:C120698 Ophthalmoscopy; NCIT:C16809 MRI | Repeated fundoscopy and imaging in childhood, because presentation is late |
| Speech and language therapy, developmental assessment | NCIT:C159273 Speech Language Therapy; `BEHAVIORAL` | Formal developmental assessment after diagnosis is recommended (PMID:35761471) |
| ENT and audiology management | (no specific cached term) | PMID:35761471 |
| Genetic counselling and cascade testing | NCIT:C15240 Genetic Counseling | 50% recurrence risk for offspring of a carrier |

- **Pharmacotherapy:** no approved drug.
- **Growth hormone:** used in one ERF patient labelled Chitayat (PMID:40840652; NCIT:C164163 Therapeutic Growth Hormone) with a poor response. This applies to the allelic or NS-like presentation, not to CRS4 suture disease.
- **Experimental, preclinical only:**
  - In *Erf*-insufficient mice, the MEK1/2 inhibitor U0126 and the nuclear-export (XPO1) inhibitor KPT-330 (selinexor; NCIT:C102546) raised Erf activity and "alleviated the synostosis phenotype with minimal adverse effects" (fetched fragment, PMID:37175668).
  - The rationale is to keep ERF nuclear by reducing ERK-driven export. Twigg had already proposed ERF as a therapeutic target because suture fusion is delayed:

    > "make ERF an attractive target for therapeutic modulation" — PMID:23354439, verbatim, local cache

  - Retinoic acid rescues the ex vivo differentiation defect (PMID:33972395).
  - **There are no human trials**: no NCT or ICTRP records were identified.
- **Pharmacogenomics, gene, cell and RNA therapies:** none.

---

## 13. Prevention

- **Primary:** not applicable apart from reproductive options. Prenatal or preimplantation testing is possible once the familial variant is known.
- **Secondary:** cascade genetic testing of relatives, and surveillance of at-risk children for postnatal suture fusion, ICP and Chiari, because of the delayed presentation.
- **Tertiary:** timely cranial surgery to prevent visual and neurodevelopmental damage from raised ICP; developmental, speech and ENT follow-up.
- **Vaccination, public health and environmental measures:** none apply.

---

## 14. Other Species / Natural Disease

- No naturally occurring ERF disease was found in OMIA. This was not searched in depth; check OMIA before recording absence.
- The orthologue is mouse *Erf* (NCBITaxon:10090 *Mus musculus*, cached). The ETS family and the ERK–ERF regulatory axis are conserved across vertebrates.

---

## 15. Model Organisms

| Model | Phenotype | Fidelity notes |
|---|---|---|
| **Mouse *Erf^loxP/−*** (hypomorphic conditional allele over a null; about 29–30% transcript) | Postnatal multisuture synostosis with domed heads at 3–6 weeks; mildly delayed embryonic ossification (PMID:23354439). Initially impaired frontal bone formation then multisuture synostosis; rescued by U0126 and KPT-330 (PMID:37175668) | `PARTIALLY_RECAPITULATES` the suture node. **Dosage mismatch:** needs about 30% rather than 50%. Twigg: "the threshold level required for phenotypic manifestation is lower in mice" (verbatim, local cache). Record as a `HUMAN_MODEL_MISMATCH` discussion or a typed divergence |
| **Mouse *Erf^+/−*** | Normal | `FAILS_TO_RECAPITULATE`. A real negative result, since heterozygous loss is what causes the human disease |
| **Mouse *Erf^−/−*** | Placental failure, death by E10.5; defective haematopoiesis (PMID:28694332) | Not a model of CRS4 |
| Ex vivo mouse suture-derived mesenchymal progenitors | Reduced osteogenic differentiation, higher Cyp26b1, rescue by RA (PMID:33972395) | `IN_VITRO`; mechanistic, at the cellular scale |
| ERF-knockout human ESC lines (CRISPR) | Lines generated; no craniofacial phenotype reported yet (PMID:31743839) | Resource only |
| Zebrafish / Drosophila | None identified | — |

Model-organism evidence must be tagged `MODEL_ORGANISM` (mouse) or `IN_VITRO` (ex vivo cells and ESCs), and kept separate from the human clinical evidence.

---

## Reference summary (PMIDs)

**In the local cache (`references_cache/`):**
- 23354439 (Twigg 2013, discovery; full text)
- 27884935 (Miller 2017, exome/WGS diagnostic yield)
- 38318288 (genome-wide analysis in craniosynostosis)
- 42059179 (ClinGen Cranio GCEP)
- 38824261 (NS-like ERF phenotype)
- 39668184 (MIDES)
- 27738187 and 30569521 (Chitayat syndrome)
- 40840652 (problematic "Chitayat" frameshift case)
- 33156164 (management guideline)

**Not yet cached; run `just fetch-reference`:**
- 30758909 (Glass 2019)
- 26097063 (Chaudhry 2015)
- 35761471 (Care 2022)
- 36209295 (Afshari 2023)
- 35852485 (Moddemann 2022)
- 32370745 (Körberg 2020)
- 35313736 (Radu 2023)
- 41562473 (Chaisrisawadisuk 2026)
- 33993607 (Calpena 2021)
- 34117072 (Singh 2021)
- 29168297 (Clarke 2018)
- 34184330 (Yamada 2021)
- 40307313 (Goto 2025)
- 33972395 (Vogiatzi 2021)
- 37175668 (Vogiatzi 2023)
- 28694332 (Peraki 2017)
- 31743839 (Si 2019)
- 39967053 (hypochondroplasia co-occurrence)

**Web sources consulted:**
- [GenCC ERF gene page](https://thegencc.org/genes/HGNC:3444)
- [PanelApp panel 168: ERF](https://panelapp.genomicsengland.co.uk/panels/168/gene/ERF)
- [OMIM #600775](https://omim.org/entry/600775)
- [MGI OMIM:600775](https://www.informatics.jax.org/disease/OMIM:600775)
- [Glass 2019 (ORA Oxford)](https://ora.ox.ac.uk/objects/uuid:4b443516-0fa5-4c2c-a701-71a7acd0bfd5)
- [Vogiatzi 2021 (PMC8300784)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8300784)
- [Körberg 2020 (PMC7201657)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7201657/)
- [ClinGen Cranio GCEP (ORA Oxford)](https://ora.ox.ac.uk/objects/uuid:6c7d2d18-1c43-4706-bd2a-fc5e39ab26e7)
- [PubMed search: ERF craniosynostosis](https://pubmed.ncbi.nlm.nih.gov/?term=ERF+craniosynostosis)
- [NCBI E-utilities abstracts](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 78 |
| Resolved | 75 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0010929` (5 mentions) - the report calls it "CRS4", "Keep CRS4"; MONDO calls it **craniosynostosis 4**, and lists "CRS4" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0010929` - called "CRS4", "Keep CRS4"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

75 of 78 terms resolved to a current term; the rest could not be looked up either way.