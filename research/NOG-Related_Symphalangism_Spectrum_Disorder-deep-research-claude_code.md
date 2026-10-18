---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T13:13:10.461755'
end_time: '2026-10-14T13:16:41.816015'
duration_seconds: 211.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: NOG-Related Symphalangism Spectrum Disorder
  mondo_id: MONDO:0100521
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 41
  total_cost_usd: 2.4304922
  session_id: 66c91e47-4cbb-420b-838d-068659d6743d
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 18
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 31
  quotes_valid: 29
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:17668388
  - PMID:33308208
  relevance_assessed: 26
  on_topic: 20
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 55
  verified: 54
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NOG-Related Symphalangism Spectrum Disorder
- **MONDO ID:** MONDO:0100521 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **NOG-Related Symphalangism Spectrum Disorder** covering all of the
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

Let me read the abstracts of the key ones for exact quotes.

I've read the cached abstracts; now checking a few identifiers and HPO terms against local caches before writing the report.

# Research Report: NOG-Related Symphalangism Spectrum Disorder (NOG-SSD), MONDO:0100521

**How this was built.** Most claims below come from 24 abstracts or full texts already cached in `references_cache/` in this worktree, and quotes from those are exact. Two web searches added a little recent literature. Those web-only items are marked **[uncached]**: their PMIDs or snippets need `just fetch-reference` before anyone cites them as evidence. Ontology IDs marked ✓ were checked against the local `cache/*/terms.csv`. IDs not marked ✓ were not checked and should not be bound until they are looked up.

---

## 1. Disease Information

**Overview.** NOG-SSD is an umbrella term proposed in 2011. It covers five autosomal dominant joint-development syndromes, all caused by heterozygous variants in *NOG*, the gene for the BMP antagonist noggin.

> "The hallmark of NOG-related syndromes is proximal symphalangism, defined by abnormal fusion of the proximal interphalangeal joints of the hands and feet. Many additional features secondary to NOG mutations are commonly but inconsistently observed, including a characteristic facies with a hemicylindrical nose, congenital conductive hearing loss due to stapes fixation, and hyperopia." — PMID:21538686 (Potti et al., *Hum Mutat* 2011, review)

> "Due to the variable phenotypic spectrum within families and among families with the same mutation, we propose a unifying term, NOG-related symphalangism spectrum disorder (NOG-SSD)" — PMID:21538686

**The five syndromes it covers, with OMIM numbers** (as listed in PMID:34049328):

| Syndrome | Abbrev. | OMIM |
|---|---|---|
| Proximal symphalangism 1 | SYM1 | 185800 |
| Multiple synostoses syndrome 1 | SYNS1 | 186500 |
| Stapes ankylosis with broad thumbs and toes (includes Teunissen-Cremers syndrome) | SABTT | 184460 |
| Tarsal-carpal coalition syndrome | TCC | 186570 |
| Brachydactyly type B2 | BDB2 | 611377 |

The gene is *NOG*, OMIM 602991 (PMID:33308208), HGNC `hgnc:7866` ✓ (NOG). Facio-audio-symphalangism syndrome is a historical synonym (PMID:26994744, PMID:29605356).

**Identifiers.** MONDO:0100521 is the entry's disease term. I could not confirm an Orphanet code for the NOG-SSD umbrella. Orphanet lists the component syndromes separately, and the web search did not find an umbrella ORPHA entry. I did not verify ICD-10/ICD-11 or MeSH codes. The relevant MeSH headings are *Synostosis*, *Stapes/abnormalities* and *Hand Deformities, Congenital* (taken from the MeSH indexing of PMID:21538686).

**Data provenance.** All of the evidence is aggregated from case reports, family studies and reviews. There are no EHR-derived or registry data. A locus-specific variant database exists (https://NOG.lovd.nl, PMID:21538686).

**Suggested subtype modelling:** five `has_subtypes` rows (SYM1, SYNS1, SABTT, TCC, BDB2). BDB2 has a different molecular mechanism (section 6), so it is the only one that is more than a clinical label.

---

## 2. Etiology

- **Cause.** Heterozygous germline *NOG* variants (missense, nonsense, frameshift, start-loss, in-frame indel), or 17q22 microdeletions that include *NOG*.
- **Genetic heterogeneity of the clinical phenotype.** Similar SYNS and SYM phenotypes are also caused by *GDF5* (`hgnc:4220` ✓) and *FGF9* (`hgnc:3687` ✓): "Currently, three genes, NOG, GDF5, and FGF9, have been identified as causative of SYNS" (PMID:25241334). Those cases are outside NOG-SSD by definition, but they matter for the differential diagnosis.
- **Environmental, protective or gene-environment factors.** None reported. Write "not applicable"; do not leave the field empty.
- **Modifier effects.** Strong intra- and inter-familial variability with the same variant: "the phenotype was expressed differently both within and between the families" (PMID:25241334). In mice, genetic background changes the phenotype: "The Noggin null mouse phenotype is strain dependent" (PMID:16598734), and hearing loss in *Nog*+/− mice appears "Depending on the genetic background" (PMID:18096605). No human modifier gene has been identified.

---

## 3. Phenotypes

The HPO terms below were checked against `cache/hp/terms.csv` ✓. Frequencies are qualitative because no cohort-level frequency study exists. Onset is congenital unless noted.

| Phenotype | HPO ✓ | Notes / evidence |
|---|---|---|
| Proximal symphalangism | HP:0100264 Proximal symphalangism; HP:0006152 Proximal finger symphalangism; HP:0010179 Toe symphalangism | The hallmark (PMID:21538686). It can be absent in SABTT, which was described as "lacked symphalangism" (PMID:12089654). |
| Conductive hearing loss from stapes ankylosis | HP:0000405 Conductive hearing impairment | "The most common sign in NOG-SSD is conductive hearing loss related to congenital stapes fixation" (PMID:34049328). It may be **progressive in early childhood**: normal ABR at 9 months and 1–2 years, then progressive CHL (PMID:33588412). It is absent in some families, for example C230Y (PMID:26994744). Severity is mild to moderate-severe. |
| Hyperopia | HP:0000540 Hypermetropia; HP:0008499 High hypermetropia | Present in all 8 affected members across the two families of PMID:34049328, including +8 D in one proband. |
| Strabismus / amblyopia | HP:0000486 Strabismus; HP:0000646 Amblyopia | Reported in PMID:34049328 and PMID:25815513. |
| Hemicylindrical or bulbous nose | HP:0000414 Bulbous nose (no "hemicylindrical nose" term was found in the cache) | PMID:21538686, PMID:26994744. Coarse binding; record the descriptor in `preferred_term`. |
| Other facial features | HP:0000233 Thin vermilion border; HP:0000322 Short philtrum | From Table 1 of PMID:34049328 (thin upper lip, short philtrum, maxillary hypoplasia, micrognathia). |
| Broad thumbs / halluces | HP:0011304 Broad thumb; HP:0010055 Broad hallux | Characteristic of SABTT (PMID:12089654). |
| Carpal and tarsal synostosis | HP:0009702 Carpal synostosis; HP:0008368 Tarsal synostosis; HP:0100266 Synostosis of carpals/tarsals | Defines TCC (PMID:29159868) and occurs in BDB2 (PMID:17668388). |
| Elbow / humeroradial synostosis | HP:0003041 Humeroradial synostosis; HP:0003070 Elbow ankylosis | Seen in SYNS1. The review literature supports it, but none of the cached abstracts quotes it. **Needs a source.** |
| Cervical vertebral fusion | HP:0002948 Vertebral fusion | C2–C3 fusion in the L14P proband (PMID:34049328). |
| Brachydactyly (terminal digit deficiency) | HP:0001156 Brachydactyly | BDB2 (PMID:17668388). |
| Syndactyly | HP:0012725 Cutaneous syndactyly; HP:0001770 Toe syndactyly | "All the affected members had syndactyly and symphalangism" (PMID:29605356). |
| Transverse toe reduction defects | — | PMID:15736221 (one sibship). |
| Tall stature in childhood | HP:0000098 Tall stature | "Heterozygous gene mutations in NOGGIN are associated with tall stature in children but not necessarily in adults" (PMID:18204269). Two families only. |
| Esophageal atresia / TEF (rare, single case) | HP:0002032; HP:0002575 | "suggests that the clinical spectrum of NOG-related symphalangism spectrum disorders may include EA/TEF" (PMID:34472207). Model it as a candidate feature, not a core one. |
| Malleus/incus fixation (rare) | — | "has not previously been reported in individuals with NOG-SSD" before PMID:34049328. Also reported with a start-codon variant **[uncached; PMC6679842]**. |
| Joint pain, reduced range of motion | — | "recurrent pain from affected joints" (PMID:26994744). |

**Inheritance and expressivity terms:** HP:0000006 Autosomal dominant inheritance ✓ and HP:0003828 Variable expressivity ✓.

**Quality of life.** No validated QoL instrument data exist. The main functional burdens are hearing loss during school age and reduced hand dexterity. The authors of PMID:33588412 give that as the reason for early surgery. This is expert opinion, not measured data.

---

## 4. Genetic and Molecular Information

- **Gene:** *NOG* at 17q22 (PMID:25815513). It is a single-exon gene: "Since Noggin is a single exon gene, this data strongly suggest that the autosomal dominant disorders associated with NOG mutations are due to haploinsufficiency of NOGGIN" (PMID:18096605; mouse study). Because the gene has one exon, nonsense variants are not expected to trigger nonsense-mediated decay. That is my inference, not a quoted finding.
- **Spectrum:** "More than 60 mutations of NOG, including both missense and nonsense mutations" (PMID:34049328).

**Representative variants:**

| Variant | Phenotype | Functional data | Source |
|---|---|---|---|
| c.41T>C p.L14P (signal peptide) | SYNS1 | Protein completely absent; partly rescued by proteasome inhibition but still not secreted | PMID:34049328 |
| p.P170L | Congenital CHL / stapes ankylosis | Impaired secretion | PMID:31628072, PMID:34049328 |
| c.328C>T p.Q110*; c.252_253insC | SABTT | Disrupts the cysteine-rich C-terminal domain | PMID:12089654 |
| c.645C>A p.C215* | SABTT, progressive CHL | — | PMID:33588412 |
| c.406C>T p.R136C (heparin-binding site) | SYM1 + CHL | In silico loss of a heparin salt bridge | PMID:24735539 |
| p.P35A/S, A36P, E48K, R167G, P187S | BDB2 | Not a major loss of function; altered BMP/GDF binding | PMID:17668388 |
| p.C178R | SABTT-like, mild | ACMG likely pathogenic | PMID:33308208 |
| p.C230Y | SYNS1 without hearing loss | — | PMID:26994744 |
| c.688_699del p.Cys230_Cys232delins11 | Stapes fixation, syndactyly | ACMG likely pathogenic | PMID:29605356 |
| c.611G>A | TCC | — | PMID:29159868 |
| p.P42A + p.P50R (in cis, de novo) | Carpal/tarsal synostosis, toe reduction | Parental gonadal mosaicism | PMID:15736221 |
| p.M190V; p.P42R | Symphalangism, tall stature | — | PMID:18204269 |
| c.222C>A p.Y74* | Stapes ankylosis, hyperopia | — | Sonoyama 2023 **[uncached; PMC10097708]** |
| c.2T>C (start loss) | Incus and stapes malformation | — | 2019 **[uncached; PMC6679842]** |

- **Functional class.** Most variants are hypomorphic or loss of function: "the human disease-causing mutations are hypomorphic alleles that reduce secretion of functional dimeric noggin" (PMID:11562478). That study also found no dominant-negative effect: "Coexpression of mutant noggin with wild-type noggin … did not interfere with wild-type noggin secretion". BDB2 variants are an exception. They "do not indicate a major loss of function … Rather, they presumably alter NOG's ability to bind to BMPs and growth-differentiation factors (GDFs) in a subtle way" (PMID:17668388).
- **Structural variants.** A 555-kb deletion covering only *NOG* and *ANKFN1* gave a mild, typical NOG-SSD phenotype (PMID:34049328). A 1.6-Mb deletion covering 13 genes gave NOG-SSD without intellectual disability (PMID:25815513). Larger 17q22 deletions cause more severe syndromes, which "are likely due to deletion of genes other than NOG" (PMID:34049328). Recommendation from PMID:25815513: when sequencing finds no variant, screen for 17q22 deletions.
- **Mosaicism.** Gonadal or low-level somatic mosaicism has been inferred in an unaffected parent (PMID:15736221). That is parental mosaicism, so per the `somatic-mosaicism` skill it must **not** be bound to HP:0001442. A de novo variant in an affected mother has also been inferred (PMID:34049328).
- **ClinGen, ClinVar, gnomAD.** Not checked. Run `just check-gene-validity` and the ClinGen cache before recording any validity tier; do not assign one.
- **Epigenetics:** none reported.

---

## 5. Environmental Information

No environmental, lifestyle or infectious contributors are known. Treat this as not applicable.

---

## 6. Mechanism and Pathophysiology

### Causal chain

1. A heterozygous *NOG* loss-of-function or hypomorphic variant, or a *NOG*-containing deletion, **leads to** reduced secretion of functional noggin dimers (PMID:11562478, PMID:34049328, PMID:31628072). For R136C, the defect is reduced HSPG binding rather than reduced secretion (PMID:24735539; in silico only).
2. Reduced extracellular noggin **results in** unopposed BMP signalling in developing skeletal elements, including BMP4 and GDF5 (PMID:18096605; PMID:24735539, "leads to an excess of BMP signaling" — inferred from docking).
3. Excess BMP activity **causes** chondrocyte hyperplasia and over-recruitment of cells into cartilage condensations: "Excess BMP activity in the absence of Noggin antagonism may enhance the recruitment of cells into cartilage, resulting in oversized growth plates" (PMID:9603738; mouse null).
4. **Leads to** failed joint initiation and interzone formation: "initiation of joint development failed as measured by the expression of growth and differentiation factor-5"; "chondrocytes are also refractory to joint-inducing positional cues" (PMID:9603738).
5. Failure of joint cavitation **results in** bony or cartilaginous fusion:
   - **Branch A, digits, carpals, tarsals and elbow:** symphalangism and synostoses (PMID:10080184, "NOG is essential for joint formation").
   - **Branch B, middle ear:** in *Nog*+/− mice the stapes and styloid process do not separate (PMID:18096605). In humans, "circumferentially calcified cartilage bridging the stapedovestibular joint space" (PMID:26474326). Both lead to stapes fixation and then conductive hearing loss. Human ankylosis may be incomplete at birth and progressive afterwards (PMID:33588412).
6. **BDB2 branch (separate mechanism):** subtle changes to NOG–BMP/GDF binding alter the balance of BMP signalling and **lead to** terminal digit deficiency plus symphalangism. The authors propose BMP–ROR2 crosstalk, but that is a hypothesis (PMID:17668388).
7. **Not explained:** I found no mechanistic study for hyperopia, the facial features or tall stature. Leave these phenotypes without upstream edges, or attach a KNOWLEDGE_GAP discussion, instead of inventing a link.

**Dosage and species caveat.** *Nog*−/− mice die at birth. Heterozygous mice were first reported as normal (PMID:11562478), but later work found carpal/tarsal fusions in some strains (PMID:16598734) and conductive hearing loss (PMID:18096605). In other words, the human dominant phenotype only partly reproduces in mice. That fits a `HUMAN_MODEL_MISMATCH` discussion.

### Suggested terms

All checked against the cache ✓.

- **GO:** GO:0030514 negative regulation of BMP signaling pathway (activity lost, modifier DECREASED); GO:0030509 BMP signaling pathway (INCREASED); GO:0060272 embryonic skeletal joint morphogenesis; GO:0072498 embryonic skeletal joint development; GO:0001502 cartilage condensation; GO:0035988 chondrocyte proliferation; GO:0002062 chondrocyte differentiation; GO:0042474 middle ear morphogenesis; GO:0001958 endochondral ossification; GO:0009306 protein secretion; GO:0042803 protein homodimerization activity; GO:0008201 heparin binding; GO:0005615 extracellular space.
- **CL:** CL:0000138 chondrocyte; CL:0008019 mesenchymal cell; CL:0000062 osteoblast.
- **Genes on nodes:** NOG `hgnc:7866`; BMP4 `hgnc:1071` ✓; GDF5 `hgnc:4220` ✓.

**Omics, single-cell, spatial and CRISPR data:** none found for this disease.

---

## 7. Anatomical Structures Affected

- **Primary sites:** proximal interphalangeal joints of the hands and feet; carpal and tarsal bones; elbow; middle ear (stapes and stapedovestibular joint); cervical spine.
- **UBERON** ✓: UBERON:0002496 stapes base; UBERON:0001756 middle ear; UBERON:0001490 elbow joint; UBERON:0002413 cervical vertebra. Proximal interphalangeal joint, carpal bone and tarsal bone were **not** in the cache and need a lookup.
- **Tissue:** cartilage and bone (connective tissue).
- **Subcellular:** secretory pathway and extracellular space. The signal-peptide variant L14P causes degradation of the protein inside the cell (PMID:34049328).
- **Laterality:** usually bilateral and roughly symmetric. Unilateral CHL has been reported (PMID:34049328, II-4).
- **Otic capsule:** "fixation of the stapes footplate to the otic capsule because of a circumferential bridge of calcified cartilage" (PMID:26474326). There is also an unusually long incus–footplate distance: 4.62 mm, against 3.72 ± 0.38 mm in 40 otosclerosis temporal bones (PMID:34049328).

---

## 8. Temporal Development

- **Onset:** congenital for the skeletal features.
- **Hearing:** traditionally described as congenital. However, "the stapes ankylosis in our SABTT patient seemed to be incomplete at birth and progressive in early childhood" (PMID:33588412).
- **Joints:** SYNS is described as "progressive fusion of multiple joints" (PMID:25241334).
- **Growth:** children are tall and appendicular bone mineral content is low; both normalise by adulthood (PMID:18204269).
- **Course:** lifelong, with no remission. The critical window for intervention is early childhood, to limit hearing loss during school age (PMID:33588412).
- **Suggested `progression:` phases:** prenatal joint-formation failure; congenital or early-childhood stapes fixation; childhood progression of CHL and joint fusion; stable adult phenotype.

---

## 9. Inheritance and Population

- **Mode:** autosomal dominant, HP:0000006 (PMID:21538686).
- **Penetrance:** appears high, but expressivity varies widely. Non-penetrant carriers have not been documented in the cached sources. Do not claim incomplete penetrance without a source.
- **De novo variants and mosaicism:** both occur (PMID:10080184; PMID:15736221; PMID:34472207).
- **Prevalence:** no numeric estimate. Orphanet-derived data for SYNS1 say "No data available" (Phenodis). Use `prevalence_class: NOT_YET_DOCUMENTED` with `measure_type: UNKNOWN`.
- **Populations:** reported in European, North American, Israeli, Japanese, Korean, Chinese and Indian families. No founder variant is known.
- **Sex ratio:** no bias reported.
- **Anticipation and consanguinity:** not relevant.

---

## 10. Diagnostics

- **Clinical diagnosis:** proximal symphalangism or other synostoses, plus CHL with normal tympanic membranes and absent stapedial reflexes, hyperopia and the characteristic nose (PMID:26474326, PMID:21538686).
- **Imaging:** hand and foot radiographs (symphalangism, carpal/tarsal coalition) and temporal bone CT. CT can look normal: "No obvious abnormalities were found … on ear computed tomography" (PMID:33308208).
- **Audiology:** pure-tone audiometry and tympanometry (type A). Newborn ABR may be normal: "newborn hearing screening may not detect conductive hearing loss in patients with NOG-SSD" (PMID:33588412).
- **Genetic testing:**
  - Single-gene *NOG* sequencing, which is straightforward because the gene has one exon.
  - A hearing-loss or skeletal dysplasia panel, or exome sequencing. CNV calling from exome data detected the 555-kb deletion (PMID:34049328).
  - Chromosomal microarray or aCGH when sequencing is negative (PMID:25815513).
  - *GDF5* and *FGF9* should be on the panel for SYNS-like phenotypes.
- **Differential diagnosis:**
  - Otosclerosis. The key distinction: "Mutations in the NOG gene are commonly found in congenital stapes ankylosis with symphalangism, but not in otosclerosis" (PMID:22288654 **[uncached]**).
  - *GDF5*- and *FGF9*-related synostoses.
  - ROR2-related brachydactyly type B1 (PMID:17668388).
  - Larger 17q22 deletion syndromes, which include intellectual disability.
  - Osteogenesis imperfecta with stapes fixation (PMID:33308208).
- **GeneReviews:** I am not aware of a NOG-SSD chapter. Confirm with `just check-genereviews` before writing a "no chapter exists" note.
- **Screening:** periodic hearing tests for at-risk children (PMID:33588412). Prenatal and preimplantation testing are possible once the familial variant is known; this is standard practice and no source is cited.

---

## 11. Outcome and Prognosis

- Life expectancy is normal; no disease-specific mortality has been reported.
- Morbidity comes from hearing loss, restricted joint motion and joint pain.
- **Surgical outcomes:**
  - "stapedectomy had lasting effect without renewed fixation of the stapes in a follow up period of 18 months-38 years" (PMID:29605356).
  - Hearing improved by about 20 dB at 6 months, though "Some reports describe progressive hearing loss due to bone regrowth 2–5 years after surgery" (PMID:33308208).
  - Postoperative thresholds returned to normal in a SABTT child (PMID:33588412).
  - Histology suggests the CHL "should be improved after stapedectomy" (PMID:26474326).
- **Prognostic factors:** none validated. The literature disagrees on whether genotype predicts phenotype: "disease expression can be independent of the location and type of NOG mutation" (PMID:33308208), but C-terminal truncations are associated with SABTT (PMID:12089654).

---

## 12. Treatment

There is no disease-modifying therapy. NCIT IDs below are **not verified** in this session; check them with `runoak` or `cache/ncit/terms.csv` before binding.

| Treatment | Modality | Evidence | NCIT suggestion |
|---|---|---|---|
| Stapedectomy / laser stapedotomy | SURGERY | PMID:29605356, PMID:34049328, PMID:33588412, PMID:26474326 | Surgical Procedure (NCIT:C15329 per CLAUDE.md) |
| Surgical note: long or custom prosthesis (4.5–5.5 mm; a modified malleus-attachment piston) | — | "we recommend that surgeons obtain longer stapes prostheses before stapes surgery in individuals with NOG-SSD stapes ankylosis" (PMID:34049328) | Record in the description; NCIT device terms do not belong in `TreatmentTerm` |
| Assess malleus/incus mobility during surgery; consider atticotomy | SURGERY | PMID:34049328 | — |
| Hearing aids | DEVICE | Used before surgery (PMID:34049328) | No NCIT action term; use the device qualifier pattern |
| Spectacles for hyperopia and strabismus | DEVICE | PMID:34049328 | — |
| Physical / occupational therapy | BEHAVIORAL | Expert practice; no specific citation found | NCIT:C15302 / NCIT:C121351 |
| Genetic counseling | OTHER | — | NCIT:C15240 |

**Pharmacotherapy, gene therapy, RNA therapies and clinical trials:** none. I found no NCT or ICTRP registrations; this was a web search, and ClinicalTrials.gov itself was not queried.

---

## 13. Prevention

- **Primary prevention:** not applicable beyond reproductive genetic counselling (50% recurrence risk for an affected parent). Prenatal or preimplantation diagnosis is possible.
- **Recurrence after unaffected parents:** consider parental germline mosaicism when counselling (PMID:15736221).
- **Secondary prevention:** serial audiometry in at-risk children, because newborn screening can miss later-onset CHL (PMID:33588412). Ophthalmology screening for hyperopia and strabismus.
- **Tertiary prevention:** early stapes surgery; long-term audiological follow-up for refixation (PMID:33308208).

---

## 14. Other Species and Natural Disease

No naturally occurring animal disease was found; OMIA was not searched in this session. Noggin is highly conserved across vertebrates. The causal variants "alter evolutionarily conserved amino acid residues" (PMID:10080184), and L14 is conserved in more than 100 species (PMID:34049328). Joint requirements differ between species: "NOG requirements during skeletogenesis differ between species and between specific skeletal elements within species" (PMID:10080184).

---

## 15. Model Organisms

| Model | Phenotype | Fidelity / limitation | Source |
|---|---|---|---|
| *Nog*−/− mouse (129X1/SvJ and other strains) | Lethal at birth or about E18.5; cartilage hyperplasia; joint fusions; failed GDF5 joint induction | Recessive lethal, so a supraphysiological dose reduction compared with human heterozygotes. Use PARTIALLY_RECAPITULATES for joint failure. | PMID:9603738, PMID:16598734 |
| *Nog*+/− mouse | Strain-dependent carpal/tarsal fusions; mild conductive hearing loss from an ectopic stapes–tympanum bone bridge | The best model for CHL ("the first animal model for the study of conductive rather than neurosensory hearing loss"). Background-dependent. The human pathology is a stapedovestibular cartilage bridge, not a stapes–tympanum bridge. | PMID:18096605, PMID:16598734 |
| COS-7 / HEK293T secretion assays | Variant-specific loss of secretion and dimerization | IN_VITRO; no skeletal context | PMID:11562478, PMID:34049328 |
| *Xenopus* oocytes | SYNS1 mutant can still dimerize | Species-specific processing | PMID:11562478 |
| Chick limb micromass culture | BDB2 variants retain function | IN_VITRO | PMID:17668388 |
| In silico docking (noggin–heparin; NOG–GDF5) | R136C loses a salt bridge; free-energy calculations for BDB2 | COMPUTATIONAL | PMID:24735539, PMID:17668388 |

---

## Gaps to Record as Knowledge Gaps

1. The mechanism of hyperopia, the facial features and childhood tall stature.
2. A genotype–phenotype rule, especially why some families have no hearing loss (C230Y).
3. Prevalence.
4. Whether stapes fixation is congenital or progressive across the spectrum.
5. How often ossicles other than the stapes are fixed.
6. Whether EA/TEF is truly part of the spectrum (a single case so far).

## References Needing `just fetch-reference` Before Use

- PMID:22288654 (Ishino et al., *Clin Genet* 2012)
- Sonoyama 2023 (PMC10097708)
- Start-codon variant 2019 (PMC6679842)
- Ma 2019 (*BMC Med Genet*)
- Takano 2016 (*Hum Genome Var*)

## Sources

- Cached references in `references_cache/`: PMID:21538686, 10080184, 11562478, 12089654, 15736221, 16598734, 17668388, 18096605, 18204269, 24735539, 25241334, 25815513, 26474326, 26994744, 29159868, 29605356, 31628072, 33308208, 33588412, 34049328, 34472207, 9603738 (36004948 and 9634411 are cached with no abstract content)
- [PubMed 21538686](https://pubmed.ncbi.nlm.nih.gov/21538686/)
- [Phenodis: Multiple synostoses syndrome 1](https://iegext02.helmholtz-munich.de/phenodis/disease/show/9598)
- [MedlinePlus: Tarsal-carpal coalition syndrome](https://medlineplus.gov/genetics/condition/tarsal-carpal-coalition-syndrome)
- [DisGeNET: TCC](https://www.disgenet.org/browser/1/1/1/9241/diseaseid__C1861305-source__ALL/_b./)
- [NORD overview](https://rarediseases.org/?p=254208)
- [SAIL concept library: MONDO:0008521](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0008521/)
- [Sonoyama 2023, PMC10097708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10097708/)
- [Start-codon variant, PMC6679842](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6679842/)
- [Ma 2019, BMC Med Genet](https://bmcmedgenet.biomedcentral.com/track/pdf/10.1186/s12881-019-0917-5)
- [Takano 2016, PMC4972895](https://pmc.ncbi.nlm.nih.gov/articles/PMC4972895)
- [PubMed 22288654](https://pubmed.ncbi.nlm.nih.gov/22288654/)
- [Stapes ankylosis family](https://bohrium.dp.tech/paper/arxiv/12621334)
- [Springer s41439-023-00236-x](https://link.springer.com/10.1038/s41439-023-00236-x)
- [DOAJ, Case Reports in Genetics 2019](https://doaj.org/article/c6bd20ce8e624abaa3450bca26103da5)
- [DisGeNET C0039075](https://www.disgenet.org/browser/1/1/1/9241/diseaseid__C0039075-source__ALL/_b./)
- [encyclopedia.pub entry](https://encyclopedia.pub/entry/history/show/12060)
- [SAIL concept library: MONDO:0000151](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0000151/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 31 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 26 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17668388` *(abstract only)*: "do not indicate a major loss of function … Rather, they presumably alter NOG's ability to bind to BMPs and growth-differentiation factors (GDFs) in a subtle way"
  - closest text in source: "Rather, they presumably alter NOG's ability to bind to BMPs and growth-differentiation factors (GDFs) in a subtle way, thus disturbing the intricate balance of BMP signaling"
- `PMID:33308208`: "No obvious abnormalities were found … on ear computed tomography"
  - closest text in source: "No obvious abnormalities were found in acoustic conductivity tests or on ear computed tomography (Fig"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

54 of 55 terms resolved to a current term; the rest could not be looked up either way.