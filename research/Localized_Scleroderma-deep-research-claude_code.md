---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8
cached: false
start_time: '2026-11-26T22:04:17.255927'
end_time: '2026-11-26T22:11:18.078031'
duration_seconds: 420.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Localized Scleroderma
  mondo_id: MONDO:0019562
  category: Autoimmune
  causal_genes: ''
  omim_id: ''
  synonyms: morphea; localized morphea; circumscribed scleroderma
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
  web_search_requests: 12
  num_turns: 17
  total_cost_usd: 1.7945864650000003
  session_id: b9252105-a02c-47b5-8ff2-d49204c27db7
  stop_reason: end_turn
  tool_calls: 22
  retrieval_calls: 22
  assistant_text_blocks: 6
citation_count: 33
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:36860340
  - PMC:PMC9969991
  quotes_not_checkable: 1
  relevance_assessed: 22
  on_topic: 8
  needs_review: true
  validator_version: 0.8.0
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Localized Scleroderma
- **MONDO ID:** MONDO:0019562 (if available)
- **Causal gene(s):** 
- **OMIM:** 
- **Synonyms:** morphea; localized morphea; circumscribed scleroderma
- **Category:** Autoimmune

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Localized Scleroderma** covering all of the
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

I'll research Localized Scleroderma (morphea) comprehensively. Let me first load the search tool, then run parallel searches.

I'll run several searches in parallel to build the evidence base.

Good foundation. Let me gather treatment, diagnostics, autoantibodies, prognosis, and animal model evidence.

Let me fetch the two key open-access reviews for detail/PMIDs, and search identifiers, models, and prognosis.

The Papara review came back rich. Let me get the immunopathogenesis detail from another host, plus animal models and QoL.

I have a strong evidence base. I'll write the report inline now.

---

# Comprehensive Research Report: Localized Scleroderma (Morphea)

**MONDO:0019562 · ORPHA:90289 · DOID:8472 · ICD-10 L94.0 · ICD-11 EB61 · GARD:0007058 · UMLS C0036420 · SNOMED CT 90424004**

> **Interpretation / scope note (stated up front, as instructed):** Localized scleroderma (morphea) is a **multifactorial autoimmune/immune-mediated fibrosing disorder of the skin and underlying tissues — it is NOT a monogenic Mendelian disease, and the "Causal gene(s)" field in the template is legitimately blank.** There is no single causal gene; susceptibility is polygenic/HLA-associated and strongly environmentally triggered. Accordingly, template sections that presuppose a causal gene, ACMG variant classification, gnomAD allele frequencies, COSMIC somatic variants, carrier frequency, penetrance, repeat-expansion testing, newborn screening, and gene-replacement therapy are **Not applicable (N/A)** for this disease, and I say so explicitly in each. The disease is distinct from **systemic sclerosis (SSc)**; a recurring theme in the literature is that much morphea "mechanism" is extrapolated from SSc and that morphea is understudied in its own right ([Papara et al. 2023, *Front Med* 10:1108623, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Torok et al. 2019, *Front Immunol* 10:908, DOI 10.3389/fimmu.2019.00908](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).

**Evidence-source legend:** [H] human clinical/cohort, [IV] in vitro / tissue, [M] model organism, [C] computational/transcriptomic. Most evidence for morphea is [H] observational cohorts and [IV] tissue studies; randomized trial evidence is limited.

---

## 1. Disease Information

**Overview.** Morphea, also called localized scleroderma, is a chronic immune-mediated connective-tissue disease characterized by inflammation followed by sclerosis (fibrosis) of the skin and sometimes the subcutis, fascia, muscle, and bone. Unlike systemic sclerosis, morphea generally **spares the internal organs and lacks Raynaud phenomenon, sclerodactyly, and nailfold capillary changes**, and "morphea does not transit to SSc" ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). It evolves through an **early inflammatory phase, a fibrotic/sclerotic phase, and an atrophic phase** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Key identifiers** (all retrieved this session):
- **MONDO:** MONDO:0019562 ([rarediseases.org / Monarch](https://rarediseases.org/mondo-disease/localized-scleroderma/))
- **Orphanet:** ORPHA:90289 ([MedGen 48586](https://www.ncbi.nlm.nih.gov/medgen/48586); [MGeND DOID:8472](https://mgend.ncgm.go.jp/disease/info/DOID:8472))
- **Disease Ontology:** DOID:8472
- **ICD-10-CM:** L94.0 "Localized scleroderma [morphea]" (under L94, Other localized connective tissue disorders) ([gesund.bund.de L94.0](https://gesund.bund.de/en/icd-code-suche/l94-0))
- **ICD-11:** morphoea entry **EB61** (per CISMeF ICD-11 mapping; verify against the WHO browser) ([CISMeF ICD-11 CA_31664821](https://www.cismef.org/page/detail/en/ICD11_CA_31664821))
- **GARD:** GARD:0007058; **UMLS:** C0036420; **SNOMED CT:** 90424004 ([MGeND](https://mgend.ncgm.go.jp/disease/info/DOID:8472))
- **MeSH:** "Scleroderma, Localized" is the heading; a MeSH descriptor ID was **not confirmed** in this session and should be verified in the MeSH browser.

**Synonyms / alternative names:** morphea; localized morphea; circumscribed scleroderma; morphoea (British spelling). Subtype-level names include plaque morphea, generalized morphea, linear scleroderma, en coup de sabre, Parry-Romberg syndrome (progressive hemifacial atrophy), atrophoderma of Pasini and Pierini, disabling pansclerotic morphea, eosinophilic fasciitis (Shulman syndrome), and morphea profunda ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Data provenance:** The information here is derived from **aggregated disease-level resources** (ontologies, society guidelines, systematic reviews, and multi-patient cohorts/registries such as the Morphea in Adults and Children [MAC] cohort and the National Registry for Childhood Onset Scleroderma [NRCOS]), not from individual EHR records.

---

## 2. Etiology

**Disease causal factors.** The cause is unknown and considered multifactorial: a convergence of **genetic predisposition, environmental/infectious triggers, immune/autoimmune dysregulation (abnormal cytokine production), and vascular dysfunction** ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). It is **autoimmune**, not infectious or purely toxic, although exogenous triggers can initiate it.

**Genetic risk factors (susceptibility, not causal).**
- **HLA class I/II associations** are the strongest genetic signal. In the MAC cohort the strongest associations were with **HLA-DRB1\*04:04 and HLA-B\*37** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Torok 2019, DOI 10.3389/fimmu.2019.00908](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)). For the **generalized** subgroup, an HLA-DRA1\*15-type allele showed an odds ratio of **2.0 (95% CI 1.2–3.5, p=0.010)** ([Jacobe et al., MAC HLA study, PMC4211936](https://pmc.ncbi.nlm.nih.gov/articles/PMC4211936)).
- These morphea-associated alleles **differ from those in SSc**, so morphea and SSc are considered **immunogenetically distinct**; the class I (HLA-B) signal is interpreted as supporting a CD8/NK-cell–associated response ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).
- The same alleles overlap with those of **rheumatoid arthritis, autoimmune thyroid disease, multiple sclerosis, and type 1 diabetes**, suggesting shared autoimmune susceptibility; DRB1\*04:04 is shared with RA and adult SSc ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).
- **Family history** of connective-tissue/autoimmune disease occurs in ~**22% of children and ~11% of adults** with morphea ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)); family history of autoimmunity is reported in 10–30% ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)). *No causal variant, no ClinVar pathogenic allele, no GWAS-significant locus beyond HLA is established.*

**Environmental / exogenous risk factors.** Reported triggers include **skin trauma, surgery, radiation therapy, infections, and certain drugs/vaccines** (BCG and adjuvanted vaccines reported); suspected infectious triggers include **Epstein–Barr virus, varicella-zoster virus, and *Borrelia burgdorferi***, though causation is unproven. COVID-19 infection and vaccination appear only as case reports ("the data have to be confirmed") ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). **Demographic risk factors:** female sex (~4:1), and two age peaks (childhood, ~2–14 y; and fifth decade) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Protective factors.** No established **genetic protective variant** and no validated **dietary/lifestyle protective factor** were found in this session — **N/A / not reported**. (Routine *Borrelia* and SSc-antibody screening are not recommended, which bears on workup, not prevention.)

**Gene–environment interaction.** The leading model is that an environmental trigger (trauma, infection, radiation) initiates injury/inflammation in a **genetically (HLA-) susceptible** host, which then drives the autoimmune fibrotic cascade. The **Blaschko-line distribution** of linear morphea has prompted the hypothesis that somatic **cutaneous mosaicism** creates a susceptible clone of cells that respond abnormally to a systemic trigger — explicitly a hypothesis "not yet confirmed on a molecular basis" ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)). Formal GxE quantification is not available.

---

## 3. Phenotypes

Phenotypes are organized by subtype; frequencies are cohort-derived. Suggested HPO term **labels** are given; specific HPO IDs should be verified in the HPO browser (I did not retrieve individual HPO numeric IDs this session, so I give labels rather than fabricate IDs).

**Cutaneous (clinical signs / physical manifestations).**
- **Sclerotic/indurated skin plaques** — the defining lesion; round/oval brownish or yellow-whitish plaques, active lesions with a violaceous **"lilac ring"** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *HPO suggestion: "Hidebound skin"/"Skin plaque"/"Sclerosis of skin."*
- **Dyspigmentation** (hyper- and hypopigmentation), **skin atrophy** in late phase ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *HPO: "Hyperpigmentation of the skin," "Hypopigmented skin patches," "Cutaneous atrophy."*
- **Dermal/subcutaneous atrophy, "en coup de sabre" linear facial depression**, and **progressive hemifacial atrophy (Parry-Romberg)** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [adult ECDS/PRS series, PMC3272788](https://pmc.ncbi.nlm.nih.gov/articles/PMC3272788/)). *HPO: "Facial asymmetry," "Hemifacial atrophy."*

**Musculoskeletal (signs / functional).**
- **Flexion contractures, limb-length discrepancy, growth retardation of the affected limb, myositis, fasciitis, arthritis** — especially in **linear morphea**, which accounts for **40–65% of juvenile morphea** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *HPO: "Joint contracture," "Limb length discrepancy," "Arthritis," "Myositis."*
- **Disabling pansclerotic morphea:** contractures, chronic ulcers, poor wound healing; can be fatal (sepsis, gangrene, cardiopulmonary disease) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *HPO: "Skin ulcer," "Joint contracture."*

**Extracutaneous — neurologic/ocular (signs).** In head/face linear morphea (ECDS/PRS): **seizures (most common), headache/migraine, focal deficits, movement disorders, trigeminal neuralgia, facial palsy, neuropathy**; **uveitis** and other ocular involvement ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Neurologic involvement in ECDS, PMC3272788](https://pmc.ncbi.nlm.nih.gov/articles/PMC3272788/)). Rheumatologic/ophthalmologic/neurologic findings appear in **up to ~20%** of head-variant cases, nervous system most common; notably, **up to ~50%** of patients with head/face lesions have intracranial MRI abnormalities even without neurologic symptoms ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *HPO: "Seizure," "Migraine," "Uveitis," "Abnormality of the eye."*

**Laboratory abnormalities.** Hypergammaglobulinemia, elevated CRP, **eosinophilia** (esp. active linear morphea), elevated creatine kinase with myositis, positive autoantibodies (see §10) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). *LOINC terms apply to ANA, ESR, CRP, CK, eosinophil count.*

**Phenotype characteristics.**
- **Age of onset:** bimodal — juvenile mean ~10 y and adult mean ~45 y; congenital forms rare (skin lesions at birth in ~0.8% of juvenile cases, mean diagnostic delay 3.9 y) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Severity:** variable — from self-limited guttate/plaque lesions to disfiguring/disabling linear and pansclerotic disease.
- **Progression:** chronic, relapsing-remitting (see §8/§11); sclerosis often improves over **2–5 years** while atrophy may increase ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Frequency:** plaque is the commonest **adult** form; linear is the commonest **childhood** form; mixed ~15% of juvenile cases ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Quality-of-life impact.** Mixed evidence. Some pediatric cohorts found HRQoL near that of healthy children (median CDLQI ~5/30) ([QoL cohort summaries incl. Orzechowski 2009; Ardalan](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892867)); others (PedsQL, n=40) found **poorer QoL, especially emotional domain**, linked to relapse, diagnostic delay, and adolescent onset ([PReS JLS QoL study, PMC4043758](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4043758/)). **Symptoms and functional impairment are the key QoL determinants in both children and adults, independent of subtype** ([Duke/MAC QoL analysis](https://scholars.duke.edu/individual/pub1116494)). A 2022 psychometric analysis argued the **CDLQI likely underestimates** morphea QoL impact ([Ardalan 2022, PMC8892867](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892867)); a disease-specific instrument (**LoSQI**) is under validation ([NCT07908108](https://clinicaltrials.gov/study/NCT07908108)).

---

## 4. Genetic / Molecular Information

- **Causal genes:** **None / N/A.** Morphea is not a single-gene disorder; no gene is required to cause it ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Pathogenic variants / ACMG classification / allele frequencies (gnomAD, 1000G):** **N/A** — there is no established pathogenic Mendelian variant to classify.
- **Susceptibility loci (not "pathogenic variants"):** HLA class I/II — **HLA-DRB1\*04:04, HLA-B\*37**, and a DRA1/DRB1\*15-associated allele in generalized morphea (OR 2.0) ([Jacobe MAC HLA study, PMC4211936](https://pmc.ncbi.nlm.nih.gov/articles/PMC4211936); [Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). Candidate non-HLA genes mentioned include **TGFB (TGF-β) and CCL2/MCP-1** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). HGNC symbols for suggested annotation: *HLA-DRB1*, *HLA-B*, *HLA-DRA*, *TGFB1*, *CCL2*, *CXCL9*, *CXCL10*, *CXCL11*, *IFNG*.
- **Modifier genes:** Not formally defined; HLA type and ANA status act as severity/relapse **markers** (see §11) rather than proven modifiers.
- **Epigenetics:** No robust, morphea-specific DNA-methylation or histone study was retrieved; the Blaschko-line/mosaicism hypothesis implies a somatic/epigenetic clonal mechanism but is **unconfirmed molecularly** ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)). Treat as **not established**.
- **Chromosomal abnormalities:** **N/A / none reported.**
- **Somatic vs germline:** HLA associations are germline susceptibility; the mosaicism hypothesis (if true) would be **somatic** but is unproven ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).

---

## 5. Environmental Information

- **Physical/iatrogenic exposures:** skin trauma, surgery, **ionizing radiation** (notably radiotherapy-induced morphea, e.g., post-breast-radiation), injections ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Infectious agents (suspected triggers, unproven):** *Borrelia burgdorferi*, **Epstein–Barr virus**, **varicella-zoster virus**; routine *Borrelia* testing is **not** recommended except in highly suspicious cases, reflecting weak/inconsistent evidence ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). NCBI Taxonomy suggestions: *Borreliella burgdorferi*, *Human gammaherpesvirus 4* (EBV), *Human alphaherpesvirus 3* (VZV).
- **Drugs/vaccines (case-level):** BCG and adjuvanted vaccines; COVID-19 vaccination/infection — case reports only ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Lifestyle factors (smoking, diet, alcohol):** **No established association** retrieved — not reported as causal.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **A trigger in a genetically (HLA-) susceptible host** — skin trauma, radiation, infection, or an unknown stimulus — **leads to** endothelial/vascular and keratinocyte injury and local immune activation. *(Inferred; triggers are associative.)* ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/))
2. This **results in** a **TH1 / type-1 interferon–dominated inflammatory phase**: CD4⁺ T cells predominate, regulatory T cells are **decreased**, and an **IFN-γ/IFN-α/TNF-α gene signature** is induced ([Torok 2019, DOI 10.3389/fimmu.2019.00908](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full); [Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
3. IFN-γ **drives** production of the **CXCR3-ligand chemokines CXCL9, CXCL10, and CXCL11**, which recruit more IFN-γ–producing T cells (TH1 amplification loop); CXCL9/CXCL10 rise in blood and lesional skin and **correlate with disease activity** (mLoSSI, PGA) ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).
4. **Branch — vascular:** the inflammatory milieu **results in** endothelial activation — raised soluble **E-selectin and VCAM-1** in serum and upregulated **VCAM-1** in lesional skin, with **reduced stromal CD34** — producing microvascular injury and a "sclerodermatous" vessel pattern (thickened walls, narrowed lumens) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
5. Resident **macrophages + activated T cells** signaling to fibroblasts (via the TH1/IFN-γ network, and increasingly **TH2/TH17/TH22** cytokines) **leads to** a proposed **shift toward a TH2/profibrotic program** (IL-4, IL-5, IL-6, IL-10, IL-13) in the later "collagenous" phase — explicitly a **hypothesis** ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full); [Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
6. **TGF-β and IL-4** **result in** fibroblast activation → **increased collagen synthesis and dermal/subcutaneous collagen deposition → fibrosis/sclerosis**. (Note the apparent paradox that IFN-γ itself *inhibits* procollagen synthesis, which is why the field posits the TH1→TH2 transition.) *(Fibroblast-activation link stated as inference: "this may synergistically promote fibroblasts to increase collagen expression… eventually causing increased collagen deposition, fibrosis.")* ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full); [Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/))
7. Sustained fibrosis **leads to** the clinical sclerotic plaque, and over **2–5 years** sclerosis may regress while **tissue atrophy** of dermis, fat, muscle, and bone **results in** the final atrophic deformities (contractures, hemifacial atrophy, limb-length discrepancy) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

### Checklist detail
- **Molecular pathways:** IFN-γ/JAK-STAT (STAT1) signaling; CXCR3–CXCL9/10/11 chemokine axis; TGF-β/SMAD profibrotic signaling. Reactome/KEGG suggestions: "Interferon gamma signaling," "Chemokine receptors bind chemokines," "Signaling by TGF-beta receptor complex." JAK-STAT relevance is supported clinically by response to JAK inhibitors (§12).
- **Cellular processes:** chronic inflammation, T-cell activation/differentiation, antigen presentation, fibroblast activation, collagen fibril organization, impaired immune tolerance (reduced Tregs). GO suggestions: "collagen fibril organization" (GO:0030199 — verify), "response to interferon-gamma," "fibroblast proliferation," "extracellular matrix organization," "T-helper 1 cell differentiation."
- **Protein dysfunction:** this is a dysregulation (over-activation) rather than a misfolded-protein disease; effector output is **excess type I/III collagen** from activated fibroblasts.
- **Immune involvement:** autoimmunity with a TH1/IFN signature early, proposed TH2 skew later; decreased Tregs; plasma cells prominent on histology; autoantibodies (ANA, anti-histone, anti-ssDNA) ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full); [Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Tissue damage mechanism:** immune-mediated **fibrosis** plus microvascular injury; atrophy in late phase.
- **Molecular profiling (transcriptomics [C]):** SSc skin-transcriptome classifiers place morphea lesions in the **"inflammatory" group**, expressing primarily T-lymphocyte and IFN-γ–related genes ([Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)). A 2024 transcriptomic study of 28 juvenile patients found interferon signaling, antigen presentation, and T-helper differentiation central to active disease and proposed a type-1/3 → type-2 immune transition (hypothesis) ([Frontiers in Pediatrics RNA-seq, PMC8215272](https://pmc.ncbi.nlm.nih.gov/articles/PMC8215272); [type-2 inflammation summary](https://www.hmpgloballearningnetwork.com/site/derm-app/news/type-2-inflammation-and-fibrotic-pathways-drive-localized-scleroderma)).
- **Proteomics/metabolomics/lipidomics/single-cell/spatial:** no robust morphea-specific datasets retrieved — **largely not established** for this disease (a recognized gap).

**Suggested CL (cell) terms:** fibroblast (CL:0000057), CD4-positive T cell, CD8-positive T cell, T-helper 1 cell, regulatory T cell, plasma cell, macrophage, endothelial cell, NK cell, eosinophil (verify IDs). **Suggested CHEBI:** collagen is a protein (not CHEBI); relevant chemicals are methotrexate (CHEBI:44185 — verify), bleomycin.

---

## 7. Anatomical Structures Affected

- **Primary organ:** **skin** (UBERON:0002097 skin of body — verify) — dermis and epidermis.
- **Deeper/secondary tissues:** **subcutaneous adipose tissue, fascia, skeletal muscle, and bone** (in deep, linear, and pansclerotic subtypes); **joints** (contractures) ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Extracutaneous organ involvement (head variants):** **central nervous system/brain** (seizures, intracranial MRI lesions up to ~50% in head lesions), **eye** (uveitis, adnexal/orbital involvement), oral/dental structures ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [ECDS neurologic series, PMC3272788](https://pmc.ncbi.nlm.nih.gov/articles/PMC3272788/)).
- **Body systems:** integumentary (primary); musculoskeletal; nervous and ocular (regional, head variants). **Internal viscera (lung, heart, kidney, GI) are characteristically spared** — a key contrast with SSc ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Tissue/cell level:** connective tissue (dermal/subcutaneous), with **fibroblasts** as effector cells; perivascular and periadnexal infiltrates of **lymphocytes, plasma cells, histiocytes/macrophages, eosinophils** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)).

**Subcellular level:** nucleus (autoantibody targets — ANA, histones, ssDNA); extracellular compartment (collagen/ECM deposition). GO cellular-component suggestions: "collagen-containing extracellular matrix," "nucleosome."

**Localization & lateralization:** Linear morphea is typically **unilateral and follows Blaschko lines**; en coup de sabre is paramedian frontoparietal; Parry-Romberg is **hemifacial**. Plaque/generalized morphea favors the **trunk** (submammary, groin, lower abdomen) and may be bilateral/asymmetric ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

---

## 8. Temporal Development

- **Onset:** bimodal — juvenile (mean ~10 y) and adult (mean ~45 y); insidious/subacute; congenital onset rare (~0.8% at birth) ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Stages:** inflammatory → fibrotic/sclerotic → atrophic ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Progression rate / course:** variable; classically **relapsing-remitting over many years** rather than monophasic. In a prospective cohort with >5-year follow-up (n=50), **recurrence occurred in 44%**, most often reactivation within an existing lesion ([Florez-Pollack et al., PMC6798764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6798764/)).
- **Duration:** chronic; active disease may persist/relapse for years; sclerosis often softens over 2–5 years but atrophy/damage may persist ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Remission:** can be spontaneous (esp. guttate/plaque) or treatment-induced; median time from remission to first relapse in juvenile disease ~**26 months** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Critical window:** the **early inflammatory/active phase is the therapeutic window** — treatment aims to halt inflammation before irreversible fibrosis/atrophy and growth deformity, especially in children ([SHARE recommendations, PMC6691928](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691928)).

---

## 9. Inheritance and Population

- **Incidence:** total annual incidence **~4–27 new cases per million** people; **juvenile LS ~3.4–9 per million children/year**. The classic population-based estimate (Olmsted County, MN, 1960–1993, Rochester Epidemiology Project) gave an age/sex-adjusted incidence of **2.7 per 100,000 (95% CI 2.1–3.3)** ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Olmsted County epidemiology, PMC2938024](https://pmc.ncbi.nlm.nih.gov/articles/2938024)).
- **Prevalence:** cumulative-incidence-based estimate ~**2 per 1,000 by age 80** (Olmsted) ([Olmsted study](https://pmc.ncbi.nlm.nih.gov/articles/2938024)).
- **Inheritance pattern:** **not Mendelian — multifactorial/polygenic** with HLA-linked susceptibility; penetrance, expressivity, anticipation, mosaicism (as a Mendelian concept), founder effects, consanguinity, and carrier frequency are **N/A** ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). (Germline/somatic mosaicism appears only as an unproven Blaschko-line hypothesis — [Torok 2019](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full).)
- **Sex ratio:** female predominance, **~2.4–4:1** (≈4:1 overall; ~2:1 in congenital) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Ancestry/geography:** most affected are **Caucasian**, then Hispanic/Latin American populations; nearly two-thirds of all cases are adults ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). No endemic geographic focus is established.
- **Comorbid cancer signal:** a population-based cohort reported modestly elevated overall cancer incidence (standardized incidence ratio **1.24, 95% CI 1.14–1.35** for morphea) — cited from a secondary summary and should be verified against the primary JAMA Dermatology paper before use ([Practical Dermatology summary](https://practicaldermatology.com/news/study-morphea-linked-to-elevated-cancer-incidence/2489017/)).

---

## 10. Diagnostics

**Diagnosis is primarily clinical** ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

- **Biopsy/histopathology** (reserved for atypical cases; must be **deep**, no pathognomonic finding): active lesions show thick reticular collagen bundles with **perivascular/periadnexal lymphocytes, plasma cells, eosinophils, histiocytes**; fibrotic lesions show avascular dermis with thickened vessel walls/narrow lumens ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). SNOMED CT / pathology annotation applies.
- **Laboratory / autoantibodies:** up to ~**50%** have elevated ANA, anti-histone (AHA), and/or anti-ssDNA; **ANA positive in up to ~70%** and associated with deeper/extracutaneous involvement and relapse; **anti-ssDNA and AHA correlate with disease severity/activity** and joint-muscle involvement; other autoantibodies <10% ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [J Rheumatol cohort](https://www.jrheum.org/content/jrheum/35/12/2439.full.pdf); [PLOS One AHA/ssDNA](https://pmc.ncbi.nlm.nih.gov/articles/PMC4153681/table/T4)). Baseline labs: CBC, renal/liver function, **CK** (myositis), **RF** (if arthritis suspected), CRP; eosinophilia and hypergammaglobulinemia in active linear disease. **Routine SSc-specific antibody and *Borrelia* screening are not recommended.** A 2024 review stresses that morphea has **very few validated serological biomarkers**, far fewer than lupus/RA ([Biomarkers in LS review, PMC10988679](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10988679/)).
- **Imaging:** **MRI brain with contrast** recommended for all head/face/neck lesions; **MRI of the limb with contrast** for deep/extensive limb disease; **high-frequency ultrasound (~20 MHz)** comparable to LoSCAT but not yet validated for routine use; **thermography** (sensitivity 80.7%, specificity 86.3%); dermoscopy (whitish fibrotic beams, linear branching vessels); RCM/OCT ancillary ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Clinical activity/damage scoring (not diagnostic):** the **LoSCAT** combines a Physician Global Assessment, the **mLoSSI** (modified Localized Scleroderma Skin Severity Index — activity: new lesion/extension, erythema, skin thickness over 18 body sites) and the **LoSDI** (damage). mLoSSI shows excellent inter-rater reliability and sensitivity to change; LoSDI is less precise; an adult adaptation is validated ([LoSCAT reliability, PMC6006585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6006585/); [adult LoSCAT validation, PMC6137731](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6137731/)).
- **Genetic testing / WGS / WES / panels / karyotype / repeat-expansion / newborn screening:** **N/A** — morphea is not a monogenic disease and genetic testing has **no diagnostic role**.
- **Omics-based diagnostics:** experimental only (research transcriptomic signatures; no clinical assay) — **not established**.
- **Differential diagnosis:** systemic sclerosis (presence of Raynaud/sclerodactyly/organ disease, SSc-specific antibodies, nailfold capillary changes argue for SSc), lichen sclerosus (co-occurs in ~6%), eosinophilic fasciitis, scleredema, scleromyxedema, nephrogenic systemic fibrosis, chronic graft-versus-host disease, lipodermatosclerosis, and (for ECDS/PRS) lupus panniculitis ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** generally **not life-threatening**; normal life expectancy in typical morphea. The exception is **disabling pansclerotic morphea**, where death from sepsis, gangrene, or cardiopulmonary complications is reported ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Morbidity/disability:** major morbidity is **cosmetic and functional** — contractures, limb-length discrepancy, growth impairment, facial atrophy/disfigurement, and (head variants) neurologic/ocular disease; these drive the QoL burden (§3) ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Disease course / relapse:** relapsing-remitting; overall recurrence ~**25%** (children ~27%, adults ~17%); **44%** recurrence over >5-year follow-up in one cohort; **~15%** pediatric relapse at 2 years after methotrexate; ~**one-third** relapse on steroid monotherapy; ~**half** relapse within 3 years after UVA1 ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [Florez-Pollack, PMC6798764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6798764/)).
- **Prognostic factors:** older age at onset, **linear (limb) and generalized subtypes, delayed treatment, and ANA positivity** predict relapse/worse course. In a pediatric registry, **ANA positivity was 60% in relapsers vs 24% in non-relapsers**; a multicenter study found **extracutaneous findings increased relapse risk 5.7×** ([Kurzinski/NRCOS, PMC6462250](https://pmc.ncbi.nlm.nih.gov/articles/PMC6462250); [Turkish multicenter, PubMed 37378874](https://pubmed.ncbi.nlm.nih.gov/37378874/)).
- **Recovery:** with early systemic therapy many achieve remission; ≥1 year of methotrexate is associated with prolonged remission ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). Established atrophy/contractures are typically **irreversible**, underscoring early treatment.

---

## 12. Treatment

(Suggested **NCIT** intervention term labels given; verify numeric IDs.)

**Topical / localized (mild, superficial, limited plaque disease):**
- **Topical corticosteroids** (moderate–high potency, ≤3 months) — no controlled trials in morphea.
- **Tacrolimus 0.1% ointment** BID ×12 wk — significantly improved clinical scores/skin hardness in a placebo-controlled pilot.
- **Calcipotriene/calcipotriol 0.005%** BID ×3 mo (vitamin-D analog), alone or with phototherapy.
- **Imiquimod 5%** — reduced thickening over 9 months (plaque morphea) ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Phototherapy:** **UVA1** (3–5×/week, ≥30 sessions); **medium-dose UVA1 superior** in a 64-patient RCT; ~half relapse within 3 years; PUVA avoided in children ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).

**Systemic (deep, linear, generalized, pansclerotic, rapidly progressive, or function-threatening disease):**
- **Methotrexate — drug of choice.** Pediatric dose **0.3–0.6 mg/kg/week (15 mg/m²/week)**; adult **15–25 mg/week**, usually with a **corticosteroid bridge** (IV methylprednisolone 30 mg/kg/day ×3 days monthly, or prednisone 1–2 mg/kg/day). In an RCT of **70 children, methotrexate was superior to prednisone at 12 months**, and the prednisone-only arm had a ~3× higher recurrence risk; ~15% relapse at 2 years; SHARE advises continuing ≥1 year after remission and off steroids ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/); [long-term MTX in JLS, PubMed 22657157](https://pubmed.ncbi.nlm.nih.gov/22657157/)). NCIT: "Methotrexate," "Prednisone," "Methylprednisolone."
- **Systemic corticosteroids** (0.5–1 mg/kg/day) — bridging; ~1/3 relapse ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Mycophenolate mofetil** — second-line when MTX fails/contraindicated; retrospective cohorts show comparable relapse-free survival to MTX ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). NCIT: "Mycophenolate Mofetil."

**Targeted/biologic & advanced (refractory disease; mostly case series/off-label):**
- **Abatacept** (CTLA4-Ig) — ~80% responders at 12 months (16.7% discontinued for adverse events).
- **Tocilizumab** (anti-IL-6R) — small pediatric series.
- **JAK inhibitors:** **tofacitinib** improved skin and joint mobility in refractory generalized morphea (response from month 1); single reports of baricitinib; ruxolitinib failed in one child — mechanistically consistent with the IFN/JAK-STAT signature.
- **Imatinib** — case reports (RCT NCT00479934 noted). 
- **Not supported / ineffective:** oral calcitriol, D-penicillamine, IFN-γ. Miscellaneous case-level agents: cyclosporine, hydroxychloroquine, azathioprine, retinoids, IVIG, rituximab, infliximab ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)). NCIT: "Abatacept," "Tocilizumab," "Tofacitinib," "Imatinib," "Rituximab."

**Gene/cell/RNA-based therapy:** **N/A / none** — no gene-replacement or CRISPR approach applies to this non-monogenic disease.

**Surgical/rehabilitative:** reconstructive/plastic surgery (autologous fat grafting, flaps) for burnt-out facial/limb atrophy (performed in inactive disease); **physical and occupational therapy** for contractures/limb function; orthopedic management of limb-length discrepancy — supportive, per consensus guidelines ([SHARE, PMC6691928](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691928)).

**Treatment strategy:** consensus treatment plans exist from **North American CARRA** (methotrexate alone; MTX + oral steroids; MTX + IV steroids; endorsed by >90% of responding pediatric rheumatologists) and **European SHARE 2019** (systemic steroids in active phase + concurrent DMARD, typically methotrexate), though underlying evidence is only moderate ([CARRA consensus, PMC3403067](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403067/); [SHARE 2019, PMC6691928](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691928); [systematic review/algorithm, PubMed 21645943](https://pubmed.ncbi.nlm.nih.gov/21645943/)).

**Pharmacogenomics / personalized medicine:** no morphea-specific pharmacogenomic guidance retrieved — **not established** (general MTX pharmacogenetics exist but are not morphea-specific).

---

## 13. Prevention

- **Primary prevention:** **None established** — causes/triggers are not modifiable enough for primary prevention; no vaccine or risk-factor-modification strategy applies. **N/A** ([Papara 2023, PMID 36860340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Secondary prevention (early detection/early treatment):** the practical prevention strategy is **early recognition of active disease and prompt systemic therapy to prevent irreversible fibrosis, atrophy, contractures, and growth deformity** — especially in children, and prompt MRI/neurology/ophthalmology surveillance for head-variant (ECDS/PRS) patients ([SHARE 2019, PMC6691928](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691928)).
- **Tertiary prevention:** long-term follow-up (≥2 years after stopping treatment) to catch relapse; monitoring and management of contractures, ocular/neurologic complications, and functional/psychosocial sequelae ([Papara 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)).
- **Immunization, genetic/carrier/newborn screening, prophylactic medication:** **N/A** (non-monogenic, non-infectious, no proven prophylaxis).
- **Counseling:** no genetic counseling role (not inherited in a Mendelian way); psychosocial support is relevant given disfigurement, particularly in adolescents.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** human disease — *Homo sapiens* (NCBI:txid9606).
- **Natural disease in other species / veterinary relevance:** **No naturally occurring animal counterpart of morphea was retrieved** in this session (no OMIA entry surfaced). Localized scleroderma is essentially a **human-specific** clinical entity; "scleroderma-like"/fibrosing skin conditions in animals are not established homologues. Treat as **not reported / N/A**.
- **Orthologous genes / comparative biology / zoonosis:** **N/A** (no causal gene; non-infectious, non-zoonotic). The relevant immune genes (*IFNG*, *CXCL9/10/11*, *TGFB1*, HLA/MHC) are conserved in mammals, enabling induced models (§15), but there is no natural orthologous disease.

*(This section is genuinely sparse for morphea; the gap is a true absence of data, not an omission.)*

---

## 15. Model Organisms

There is **no faithful genetic mouse model of morphea itself**; models reproduce **skin fibrosis** and are largely shared with/derived from systemic sclerosis research.

- **Bleomycin-induced dermal sclerosis (mouse) [M]** — the standard inducible model. Repeated **local (subcutaneous/intradermal) bleomycin injections** produce dermal sclerosis, with severity varying by strain; it mimics the **early inflammatory and fibrotic** stages ([Springer protocol / bleomycin model](https://link.springer.com/content/pdf/10.1007/978-1-4939-0404-4_11.pdf)). An **acute subcutaneous bleomycin model specifically framed as morphea** was reported to depend on the **CXCL9/CXCR3 axis**, aligning with the human CXCR3-chemokine signature (medRxiv preprint — **not peer-reviewed**) ([medRxiv 19000844](https://www.medrxiv.org/content/10.1101/19000844.full.pdf)). *Applications:* dissecting inflammation→fibrosis, chemokine/IFN pathways, drug testing. *Limitations:* models fibrosis, not the full morphea phenotype (subtypes, Blaschko distribution, atrophic phase); more an SSc-type model.
- **Tight-skin (Tsk/+) mouse [M]** — a *Fbn1* (fibrillin-1) **duplication** causing tight skin; used for sclerosis genetics but **lacks the early inflammatory infiltrate**, limiting relevance to inflammatory morphea ([Tsk model discussion](https://link.springer.com/content/pdf/10.1007/978-1-0716-1382-5_25.pdf)).
- **UVA1 therapeutic models [M/IV]** — bleomycin-injected **BALB/c mice** treated with UVA1 showed reduced fibroblast proliferation and improved dermal sclerosis (high-dose UVA1 most effective), used to study the mechanism of UVA1 phototherapy ([UVA1 mouse study, PMC3597330](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3597330/)).
- **In vitro:** cultured dermal **fibroblasts** (patient-derived or bleomycin/TGF-β–stimulated) for collagen-synthesis and antifibrotic-drug studies ([UVA1 fibroblast work, PMC3597330](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3597330/)).
- **Resources:** MGI/IMSR for Tsk and relevant knockouts (*Ifng*, *Cxcr3*, *Tgfb1*). No morphea-specific registry model exists.

**Phenotype recapitulation:** partial — these models capture **inflammation-driven dermal fibrosis and some chemokine/cytokine biology**, but none reproduces morphea's subtype diversity, linear/Blaschkoid pattern, extracutaneous head-variant disease, or the late atrophic phase.

---

## Key Evidence Sources (primary + authoritative reviews)

- **Papara C, De Luca DA, Bieber K, Vorobyev A, Ludwig RJ. "Morphea: The 2023 update." *Front Med (Lausanne)* 2023;10:1108623. PMID 36860340 / PMCID PMC9969991. DOI 10.3389/fmed.2023.1108623** — the principal comprehensive source used here. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969991/)
- **Torok KS, Li SC, Jacobe HM, Taber SF, Stevens AM, Zulian F, Lu TT. "Immunopathogenesis of Pediatric Localized Scleroderma." *Front Immunol* 2019;10:908. DOI 10.3389/fimmu.2019.00908** — mechanism/immunology. [link](https://www.frontiersin.org/articles/10.3389/fimmu.2019.00908/full)
- **Jacobe H et al. HLA class I/II associations in the MAC cohort** (DRB1\*04:04, HLA-B\*37; generalized OR 2.0). [PMC4211936](https://pmc.ncbi.nlm.nih.gov/articles/PMC4211936)
- **Zulian F et al. Long-term methotrexate in juvenile localized scleroderma.** [PubMed 22657157](https://pubmed.ncbi.nlm.nih.gov/22657157/) · **Systematic review/therapeutic algorithm.** [PubMed 21645943](https://pubmed.ncbi.nlm.nih.gov/21645943/)
- **SHARE 2019 consensus** [PMC6691928](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691928) · **CARRA consensus treatment plans** [PMC3403067](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403067/)
- **Florez-Pollack et al., long-term recurrence cohort** [PMC6798764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6798764/) · **Kurzinski/NRCOS relapse predictors** [PMC6462250](https://pmc.ncbi.nlm.nih.gov/articles/PMC6462250) · **Turkish multicenter relapse study** [PubMed 37378874](https://pubmed.ncbi.nlm.nih.gov/37378874/)
- **LoSCAT reliability (pediatric)** [PMC6006585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6006585/) · **adult LoSCAT validation** [PMC6137731](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6137731/)
- **Biomarkers in localized scleroderma (2024 review)** [PMC10988679](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10988679/) · **Autoantibody (AHA/ssDNA) cohorts** [J Rheumatol](https://www.jrheum.org/content/jrheum/35/12/2439.full.pdf), [PMC4153681](https://pmc.ncbi.nlm.nih.gov/articles/PMC4153681/table/T4)
- **Neurologic involvement in ECDS** [PMC3272788](https://pmc.ncbi.nlm.nih.gov/articles/PMC3272788/) · **Olmsted County epidemiology** [PMC2938024](https://pmc.ncbi.nlm.nih.gov/articles/2938024)
- **Bleomycin/UVA1 mouse models** [PMC3597330](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3597330/), [medRxiv 19000844 (preprint)](https://www.medrxiv.org/content/10.1101/19000844.full.pdf) · **Identifiers** [MedGen 48586](https://www.ncbi.nlm.nih.gov/medgen/48586), [ICD-10 L94.0](https://gesund.bund.de/en/icd-code-suche/l94-0), [MONDO:0019562](https://rarediseases.org/mondo-disease/localized-scleroderma/)

### Caveats on reliability
- **Morphea is understudied**; much mechanism is extrapolated from SSc, and the TH1→TH2 fibrotic-transition model is an explicit **hypothesis**, not demonstrated causation.
- Several figures (cancer SIR; some QoL and relapse percentages) come from **secondary summaries or abstracts**; verify against the primary papers before entering into a knowledge base.
- **Ontology IDs:** confirmed/retrieved disease IDs are given inline (MONDO, ORPHA, DOID, ICD-10 L94.0, ICD-11 EB61, GARD, UMLS, SNOMED). For **HPO, GO, CL, UBERON, NCIT, and CHEBI** I provide term **labels** as suggestions and flagged where numeric IDs still need verification, rather than assert identifiers I did not retrieve. The **MeSH descriptor ID was not confirmed** this session.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 22 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36860340` *(abstract only)*: "morphea does not transit to SSc"
  - closest text in source: "Morphea, also known as localized scleroderma, is a chronic inflammatory connective tissue disorder with variable clinical presentations, that affects both adults and children"
- `PMC:PMC9969991` *(abstract only)*: "morphea does not transit to SSc"
  - closest text in source: "Morphea, also known as localized scleroderma, is a chronic inflammatory connective tissue disorder with variable clinical presentations, that affects both adults and children"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.3389/fimmu.2019.00908`: "not yet confirmed on a molecular basis"
  - Reference resolved but exposes no abstract or full text to search