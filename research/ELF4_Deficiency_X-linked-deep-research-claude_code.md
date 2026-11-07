---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-01T04:37:26.129340'
end_time: '2026-11-01T04:42:13.936785'
duration_seconds: 287.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ELF4 Deficiency, X-linked
  mondo_id: MONDO:0024770
  category: Mendelian
  causal_genes: ELF4
  omim_id: OMIM:301074
  synonyms: AIFBL2; deficiency 1n ELF4, X-linked
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
  num_turns: 29
  total_cost_usd: 2.4654476
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ELF4 Deficiency, X-linked
- **MONDO ID:** MONDO:0024770 (if available)
- **Causal gene(s):** ELF4
- **OMIM:** OMIM:301074
- **Synonyms:** AIFBL2; deficiency 1n ELF4, X-linked
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ELF4 Deficiency, X-linked** covering all of the
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

Searching PubMed for the main ELF4 deficiency papers next. I'm using web fetch because curl needs approval.

I have the key sources. Before writing the report, I'm checking the ontology IDs against the repo's term caches.

I wrote the report below from PubMed and PMC sources retrieved today. Three limits on how far to trust it:

- **Quotes:** The fetch tool would only return abstract excerpts of up to 125 characters, so it may have trimmed some of them. Each quote must be confirmed with `just fetch-reference PMID:<n>` and `just count-verified-snippets` before it goes into an evidence snippet. I fetched none of them into `references_cache/`.
- **Ontology IDs:** I could not run lookups against the repo's term caches; that command needed approval. The ontology IDs in this report are leads and must be checked with `just validate-terms` before binding.
- **Existing files:** The repo has a 16-line placeholder entry, `kb/disorders/ELF4_Deficiency_X-linked.yaml`, and an open stub, `stubs/Autoinflammatory_Syndrome_Familial_X-linked_Behcet-like_2.yaml`, for the same MONDO term.

---

# Deficiency in ELF4, X-linked (DEX / AIFBL2): Research Report

## 1. Disease Information

**Overview.** Deficiency in ELF4, X-linked (DEX) is a monogenic inborn error of immunity. It looks like Behçet's syndrome and inflammatory bowel disease (IBD). **The causal gene is *ELF4*** (E74-like ETS transcription factor 4, also called MEF; Xq26.1; HGNC:3319, written `hgnc:3319` in dismech). The disease is caused by hemizygous loss-of-function variants. Affected boys typically present in early childhood with:
- recurrent oral and gastrointestinal aphthous ulcers
- fevers, weight loss, skin inflammation and joint pain
- high inflammatory markers

Tyler et al. first described it in 2021 (PMID:34326534). Olyha et al. pooled an international cohort of 14 patients in 2024 (PMID:38231408).

- Olyha et al. abstract (verify): *"a Behçet's- and inflammatory bowel disease (IBD)-like disorder termed 'Deficiency in ELF4, X-linked' (DEX)"* (PMID:38231408)
- Tyler et al. abstract (verify): *"loss-of-function variants in the X-linked ETS transcription factor gene ELF4 in multiple unrelated male patients"* (PMID:34326534)

**Identifiers**
| Resource | ID |
|---|---|
| MONDO | MONDO:0024770 (MONDO label *autoinflammatory syndrome, familial, X-linked, Behcet-like 2*; parent MONDO:0031384 *autoinflammatory syndrome, familial, Behcet-like*), from the stub file |
| OMIM | #301074 (AIFBL2) |
| Gene | ELF4, `hgnc:3319` |
| ClinGen | **Definitive**, XL, Primary Immune Regulatory Disorders GCEP, 2025-06-25. Record `CGGV:assertion_625f18f6-e14f-457b-9134-a2b1aeedc410-2025-06-25T160000.000Z` (from `cache/clingen/gene_validity.csv`) |
| GenCC / PanelApp | ELF4 is listed (GenCC submission SGC-107498.2; Genomics England PanelApp panel 398, *Primary immunodeficiency or monogenic IBD*) |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found. In ICD-10 it would be coded under other autoinflammatory syndromes (M04.8, a lead to verify) |

**Synonyms:** DEX; AIFBL2; Autoinflammatory syndrome, familial, X-linked, Behçet-like 2; ELF4 deficiency; Behçet-like disease due to ELF4 deficiency.

**Data source.** All information comes from case reports and small cohorts (individual patients). No registry or EHR data exist yet.

## 2. Etiology

- **Cause.** Germline hemizygous loss-of-function variants in *ELF4*. These include nonsense, frameshift, missense in the ETS DNA-binding domain, exon deletions and an intronic splice variant.
- **Inheritance of the variant.** Variants are mostly inherited from carrier mothers. Olyha et al. found 11/12 with known status were maternal and one was *de novo* (PMID:38231408).
- **Genetic risk factors.** *ELF4* is the only causal gene. A hypomorphic missense variant, p.T187N, causes a separate presentation: NK-cell deficiency with recurrent viral infections (Salinas 2022, PMID:36477361; see §4). One patient also carried a *de novo* Xq duplication covering STAG2 and XIAP, which may have added to his phenotype (PMID:38231408).
- **Sex.** Almost all patients are male. Heterozygous females can be affected when **skewed X-inactivation** silences the wild-type X (Zhao 2025, PMID:39976696). One carrier mother had a diagnosis of Behçet's syndrome (PMID:38231408).
- **Environmental triggers, protective factors and gene-environment interaction.** None has been established in humans. In mice carrying patient variants, lipopolysaccharide (LPS, a bacterial cell-wall product) challenge caused intestinal pathology that TREM1 blockade reversed (PMID:34326534). This suggests microbial or innate-immune triggers at mucosal surfaces, but that is model-organism evidence only. Infections can precede flares, but this has not been systematically studied.

## 3. Phenotypes

Frequencies are from the Olyha 2024 cohort (14 males; PMID:38231408) unless stated otherwise. The mean age at presentation was 4.5 years, and the latest onset was 13 years.

| Phenotype | Frequency | Type | Suggested HPO term (unverified lead) |
|---|---|---|---|
| Recurrent oral aphthous ulcers | 11/14 | sign/symptom | Oral ulcer (HP:0000155) / Recurrent aphthous stomatitis |
| GI aphthous-like ulcers on endoscopy | 7/8 scoped | sign | Intestinal ulcer |
| Weight loss / poor weight gain | 13/14 | sign | Weight loss (HP:0001824); Failure to thrive |
| Decreased appetite | 12/13 | symptom | Decreased appetite |
| Recurrent fever | 9/13 | sign | Recurrent fever (HP:0001954) |
| Skin inflammation | 8/13 | sign | Abnormality of the skin (coarse; would need a `coarse_binding_basis`) |
| Abdominal pain | 8/14 | symptom | Abdominal pain (HP:0002027) |
| Diarrhea | 7/14 | symptom | Diarrhea (HP:0002014) |
| Fatigue | 6/14 | symptom | Fatigue (HP:0012378) |
| Arthralgia; arthritis | 4/14; 2/14 | symptom/sign | Arthralgia (HP:0002829); Arthritis (HP:0001369) |
| Myalgia | 3/12 | symptom | Myalgia (HP:0003326) |
| Gastritis; esophagitis | 4/6; 4/6 | sign | Gastritis; Esophagitis |
| Nausea/emesis; constipation | 4/13; 3/13 | symptom | Nausea; Vomiting; Constipation |
| Rectal bleeding | 2/14 | sign | Hematochezia |
| Short stature | 2/14 | sign | Short stature (HP:0004322) |
| Elevated ESR | 11/12 | lab | Elevated erythrocyte sedimentation rate (HP:0003565) |
| Elevated CRP | 8/8 | lab | Elevated circulating C-reactive protein concentration |
| Anemia (mostly microcytic, iron deficiency) | 11/13 (microcytic 9/13) | lab | Microcytic anemia; Iron deficiency anemia |
| Thrombocytosis (during flares) | 5/8 | lab | Thrombocytosis (HP:0001894) |
| Neutrophilia; leukocytosis | 6/8; 6/12 | lab | Neutrophilia (HP:0011897); Leukocytosis |
| Low NK cells at some point | 7/12 | lab | Decreased natural killer cell count |
| Low class-switched memory B cells | 5/6 | lab | Decreased proportion of class-switched memory B cells |
| Raised serum cytokines | IL-6 5/10, CXCL1 3/3, IL-8 3/8, IL-1β 2/7, TNF 2/9, IL-18 2/4 | lab | Increased circulating IL-6 concentration (among others) |
| Sporadic infections; recurrent pneumonia (one patient, given IVIG) | variable | sign | Recurrent pneumonia |
| SLE with class II lupus nephritis | 1 patient (P13); SLE is also listed in the Sun 2023 Chinese cohort (PMID:36823308) | sign | Systemic lupus erythematosus |

Other reports:
- **Chinese cohort.** Sun 2023 reported 5 cases *"presenting mainly with oral ulcer"*, with IBD-like symptoms, fever of unknown origin, anemia and SLE (PMID:36823308).
- **Female carriers.** All three patients had *"recurring oral ulcers, abdominal pain and diarrhea"* and colonic ulcers (PMID:39976696).
- **One patient with a different picture.** A boy with p.W231R had recurrent viral and bacterial respiratory infections, refractory oral ulcers, constipation and arthritis (Sun 2022, PMID:35266071).
- **NK-cell deficiency.** The hypomorphic p.T187N proband had reduced and dysfunctional NK cells, persistent herpes zoster and mild hypogammaglobulinemia (PMID:36477361).
- **Immune thrombocytopenia.** One adolescent with a missense variant had chronic immune thrombocytopenia and low NK cytotoxicity (Kendirli 2026, PMID:42151449).

**Characteristics.** Onset is in childhood (infancy to 13 years). Severity is moderate to severe and variable. The course is episodic and relapsing, with flares on a background of chronic mucosal inflammation. Expressivity varies even among patients with the same variant (W251S, R234X).

**Quality of life.** Painful oral ulcers and poor appetite drive weight loss and growth failure. Patients often need long-term steroids or biologics. No formal quality-of-life (EQ-5D/PROMIS) data exist.

## 4. Genetic / Molecular Information

- **Gene.** *ELF4* (MEF), Xq26.1. It encodes an ETS-family transcription factor. **OMIM gene number:** 300775 (from memory, to verify).
- **Variants in the Olyha 2024 cohort (PMID:38231408), as reported:**
  - Frameshift: c.443delG p.(G148Vfs*113); c.465delG p.(H156Ifs*105); c.1015delG p.(A339Pfs*32)
  - Nonsense: c.115C>T p.(Q39*); c.553C>T p.(R185*); c.700C>T p.(R234*)
  - Missense in the ETS domain: c.636G>T p.(W212C); c.691T>C p.(W231R); c.743C>T p.(S248F); c.752G>C p.(W251S)
  - Deletion of exons 2–7 (~29 kb; twins)
- **Variants in other reports:**
  - c.1022del p.(Q341Rfs*30), maternal. It lowers mRNA through nonsense-mediated decay (Sun L 2024, PMID:38773005).
  - c.248-7G>A, intronic. It causes abnormal splicing and lowers mRNA and protein (Tian 2025, PMID:41005485).
  - In heterozygous females: c.320_321insA, c.329delA, c.685A>G (PMID:39976696).
  - p.L80*, truncating (Zhang 2026, PMID:42769205).
  - Further novel frameshifts (Sun M 2025, PMID:40800195; Zhuo 2025, PMID:41131646).
  - Hypomorphic p.T187N (c.560C>A). It *"does not decrease expression but disrupts ELF4 protein interactions and DNA binding"* (PMID:36477361).
- **Functional consequence.** Loss of function. Truncating variants and ETS-domain missense variants abolish DNA binding or transactivation. IFN-β luciferase reporter assays are the standard functional test used to support pathogenicity (PMID:36823308, PMID:38773005).
- **ClinVar classification, allele frequency, modifiers.** Not compiled here. Check ClinVar and gnomAD per variant (hemizygous counts should be about zero). No modifier genes, epigenetic signatures or chromosomal abnormalities are established. The only related findings are skewed X-inactivation in affected females and the STAG2/XIAP duplication in one patient.

## 5. Environmental Information

No environmental, lifestyle or infectious cause is established. In models, innate stimuli such as LPS and viral infection unmask the hyperinflammatory phenotype (PMID:34326534, PMID:35266071). Infections can occur, but they are not the disease trigger.

## 6. Mechanism / Pathophysiology

**Causal chain** (each step marked human, mouse or in vitro, and whether it was shown or inferred)

1. **Germline hemizygous *ELF4* loss-of-function variant** (truncating, ETS-domain missense or splice) **leads to** absent or non-functional ELF4 protein (shown in humans: NMD or splicing defects, PMID:38773005, PMID:41005485; loss of DNA binding, PMID:35266071).
2. **Loss of ELF4 transcriptional control in myeloid cells (macrophages, neutrophils) leads to** loss of anti-inflammatory gene expression, notably *Il1rn* (IL-1 receptor antagonist). It also removes the brake on "inflammation amplifiers": S100A8, Lcn2, Trem1 and neutrophil chemoattractants (shown in mice, PMID:34326534). Abstract quote (verify): *"Elf4 both sustained the expression of anti-inflammatory genes, such as Il1rn"*.
3. **This leads to** exaggerated cytokine responses to innate stimuli (TLR ligands, LPS, viruses). Examples are more IL-6 from patient PBMCs after LPS (shown in humans, PMID:41005485) and more pro-inflammatory cytokines from mutant cells (shown in humans and mice, PMID:35266071).
   - **Branch A, T cells.** ELF4 normally restrains CD4+ Th17 differentiation, so its loss **results in** Th17 expansion. This was seen in patients and in ELF4-deficient mice (PMID:38231408). Whether it drives the mucosal lesions is inferred.
   - **Branch B, antiviral and NK cells.** ELF4 is part of the type I IFN feed-forward loop: *"ELF4 is induced by type I interferon and upregulates interferon expression in a feed-forward loop"*, and it is recruited downstream of STING and MAVS–TBK1 (mouse, PMID:24185615). Loss **leads to** poor control of viral replication (PMID:35266071). ELF4 is needed for NK-cell terminal maturation and cytotoxicity (PMID:36477361), so loss **leads to** low NK cells. It is also needed for CD8+ T-cell quiescence and homing through KLF4/KLF2 (mouse, PMID:19412182) and for memory CD8+ T cells (mouse, PMID:24338897). Human IFN data conflict: one patient's cells made *more* type I IFN (PMID:38231408).
4. **Neutrophil recruitment and a TREM1-amplified innate response at mucosal surfaces lead to** aphthous ulceration of the mouth, esophagus, stomach and ileocolon. In mice, *"Blockade of Trem1 reversed inflammation and intestine pathology after in vivo lipopolysaccharide challenge"* (PMID:34326534). Human colonic single-cell data show Crohn's-like signatures, angiogenic chemokine responses and increased innate-cell chemotaxis (PMID:41005485).
5. **Systemic spill-over of cytokines (IL-6, IL-1β, TNF, CXCL1, IL-18) results in** fever and an acute-phase response: high ESR and CRP, neutrophilia, thrombocytosis, and anemia of inflammation compounded by GI blood loss and iron deficiency.
6. **Chronic mucosal inflammation, poor intake and catabolism result in** weight loss, failure to thrive and short stature (inferred). Immune dysregulation can also lead to autoimmunity (SLE, ITP) in a minority (association only).

**Treatment response as indirect evidence.** Blocking IL-1, TNF or IL-12p40 improved symptoms in patients (PMID:34326534). This supports the IL-1/TNF myeloid axis, with `directness: INDIRECT`.

**Suggested terms (unverified leads)**
- **GO:** negative regulation of inflammatory response (GO:0050728); DNA-binding transcription factor activity, RNA polymerase II-specific; positive regulation of type I interferon production; T-helper 17 cell differentiation; natural killer cell differentiation; neutrophil chemotaxis; response to lipopolysaccharide.
- **CL:** macrophage (CL:0000235); neutrophil (CL:0000775); natural killer cell (CL:0000623); T-helper 17 cell (CL:0000899); CD8-positive, alpha-beta T cell; class switched memory B cell.
- **Subcellular (GO CC):** nucleus.
- **Molecular profiling available:**
  - Patient PBMC RNA-seq (PMID:35266071, PMID:38773005)
  - Single-cell RNA-seq of inflamed colon (PMID:41005485) and of PBMCs (PMID:42769205)
  - ChIP-qPCR of ELF4 binding at promoters
  - Search GEO for accession numbers before using any; no accession was verified here.

## 7. Anatomical Structures Affected

- **Primary sites:** oral mucosa (UBERON lead: mouth mucosa), esophagus, stomach, ileum and colon, i.e. the GI tract, the main affected system.
- **Secondary:** skin, joints and muscle; blood and haematopoietic system (anemia, thrombocytosis); kidney, through lupus nephritis in one patient.
- **Cells and compartment:** myeloid cells (macrophages, neutrophils), Th17 cells, NK cells and intestinal mucosa. ELF4 acts in the nucleus.
- **Laterality:** not applicable.

## 8. Temporal Development

- **Onset:** infancy to early childhood (mean 4.5 y; range up to 13 y). One patient presented in adolescence (PMID:41005485).
- **Course:** chronic and relapsing-remitting, with inflammatory flares.
- **Remission:** induced by treatment (steroids, TNF inhibitors). No spontaneous remission is described.
- **Long-term data:** all reported patients were younger than 25 at last follow-up, so the adult natural history is unknown.

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive in practice (HP lead: X-linked recessive inheritance, HP:0001419). Female carriers are affected only with skewed X-inactivation (PMID:39976696).
- **De novo variants:** occur (W251S in one patient). Germline mosaicism is not reported.
- **Prevalence:** ultra-rare, with roughly 30–40 cases published worldwide by 2026. Zhou 2024 reviewed 18 patients (PMID:39563044); Olyha 2024 pooled 14 (PMID:38231408); single cases have appeared since. No population prevalence figure exists.
- **Geography:** cases come from the USA, Europe, China and Turkey. Chinese reports are numerous (PMID:36823308, PMID:38948265, PMID:39563044, PMID:41070654). No founder variant is known; R234* and W251S recur.
- **Sex ratio:** overwhelmingly male.
- **Anticipation, consanguinity:** not relevant (X-linked).

## 10. Diagnostics

- **Labs:** ESR and CRP; blood count (anemia, thrombocytosis, neutrophilia); iron studies; lymphocyte subsets (NK cells, class-switched memory B cells); immunoglobulins; serum cytokines (IL-6, IL-18, CXCL1).
- **Endoscopy with biopsy:** aphthous ulcers anywhere from the esophagus to the colon. Histology shows inflammatory cell infiltration and can resemble Crohn's disease.
- **Genetic testing:** whole exome or genome sequencing, or a monogenic IBD or autoinflammatory gene panel that includes *ELF4* (PanelApp panel 398). Single-gene testing is appropriate when the phenotype fits. CNV analysis is needed, because whole-exon deletions occur (exons 2–7).
- **Functional confirmation of variants of uncertain significance:** ELF4 expression in PBMCs, and an IFN-β luciferase reporter assay (PMID:36823308).
- **Females:** test X-inactivation.
- **Differential diagnosis:**
  - Behçet's disease (DEX usually lacks pathergy, eye disease and the HLA-B51 association; this is inferred)
  - Haploinsufficiency of A20 (*TNFAIP3*, HA20) and *RELA* haploinsufficiency (other Behçet-like monogenic diseases)
  - Very-early-onset IBD, including the IL-10/IL-10R defects
  - XIAP deficiency (also X-linked; colitis and HLH)
  - PFAPA, periodic fever syndromes, trisomy 8 myelodysplasia with Behçet-like disease
  - Lv 2024 found a monogenic cause in 7/18 tested children with Behçet-like disease and GI involvement, including DEX (PMID:39360366)
- **Clinical criteria and screening:** none established. Carrier and cascade testing of mothers and sisters is advisable.

## 11. Outcome / Prognosis

- **Mortality:** no deaths reported (PMID:38231408).
- **Morbidity:** chronic GI disease, growth failure, steroid exposure, and occasional autoimmunity (SLE nephritis, ITP).
- **Treatment response:** most patients respond to steroids and TNF inhibitors, and some reach remission. Infliximab plus azathioprine and mesalazine plus steroids have each led to remission in single patients.
- **Long-term outcome and prognostic biomarkers:** unknown.

## 12. Treatment

All data come from case series; there are no trials. Results are from Olyha 2024 unless stated otherwise.

| Treatment | Evidence | NCIT action (lead) / therapeutic agent |
|---|---|---|
| Systemic glucocorticoids | 14/14 treated, good response, especially for oral ulcers | Pharmacotherapy (NCIT:C15986) + corticosteroid (use CHEBI:50858, not NCIT:C2322; see CLAUDE.md) |
| TNF inhibitors (adalimumab, infliximab) | 6/8 good response; *"the majority of DEX patients treated with biologics targeting TNFα"*; one adalimumab success over 16 months (PMID:38773005) | Pharmacotherapy + adalimumab / infliximab; `therapeutic_modality: MONOCLONAL_ANTIBODY` |
| IL-1 blockade (anakinra, canakinumab) | Benefit in some; anakinra was poorly tolerated by one patient; IL-1 blockade improved fevers and ulcers (PMID:34326534) | anakinra / canakinumab (verify CHEBI/NCIT IDs) |
| Ustekinumab (IL-12/23 p40) | At least modest benefit | monoclonal antibody |
| Vedolizumab; exclusive enteral nutrition | Described in female patients (PMID:39976696) | Dietary Intervention (NCIT:C15447) for exclusive enteral nutrition |
| Colchicine, azathioprine, 6-mercaptopurine, calcineurin inhibitors, methotrexate, NSAIDs | Mostly ineffective or minimal benefit; apremilast gave partial response | — |
| Supportive care | IVIG for recurrent infections, iron replacement, nutritional support | Supportive Care (NCIT:C15747) |
| HSCT, JAK inhibitors, gene therapy | No reports found | — |

- **Experimental:** no clinical trials registered for DEX (ClinicalTrials.gov was not searched exhaustively).
- **Proposed target:** TREM1 blockade, mouse data only (PMID:34326534).

## 13. Prevention

- **Primary prevention:** none.
- **Secondary prevention:** cascade testing of maternal relatives; genetic counselling (50% risk for each son of a carrier mother); prenatal or preimplantation testing is possible once the familial variant is known.
- **Tertiary prevention:** steroid-sparing biologic therapy; growth and nutrition monitoring; screening for autoimmunity and infection.

## 14. Other Species

- No naturally occurring animal disease found (OMIA not searched in depth).
- Orthologs: mouse *Elf4* (MGI) and others.
- Unrelated name clash: *Arabidopsis* EARLY FLOWERING 4 (ELF4), a circadian-clock protein (PMID:21753751), shares only the name and must not be confused with this gene.

## 15. Model Organisms

| Model | Recapitulation | Limitations |
|---|---|---|
| *Elf4*⁻/⁻ mice and **knock-in mice carrying patient variants** (Tyler 2021, PMID:34326534) | Hyperinflammatory macrophages; loss of *Il1rn*, gain of Trem1/S100a8/Lcn2; LPS-induced intestinal pathology reversed by anti-TREM1 | Spontaneous oral ulceration is not described; disease needs a challenge |
| W231R point-mutant mice (Sun 2022, PMID:35266071) | Poor viral control; more pro-inflammatory cytokines | Fewer mucosal data |
| *Elf4*⁻/⁻ mice (You 2013, PMID:24185615) | Reduced type I IFN; greater susceptibility to West Nile virus encephalitis | Conflicts with human high-IFN observations |
| *Elf4*⁻/⁻ CD8 T-cell studies (PMID:19412182, PMID:24338897) | CD8+ T-cell hyperproliferation and homing defects; poor memory | Not a disease model in itself |
| Bone-marrow chimeras expressing p.T187N; NK-cell lines and in vitro NK maturation (PMID:36477361) | NK maturation and cytotoxicity defect | Specific to the hypomorphic presentation |
| Intestinal *Elf4* deletion (PMID:35563234) | Gut barrier and alcoholic liver disease context | Not a DEX model |

---

## Key References (PMIDs)

- 34326534: Tyler PM et al., *Nat Immunol* 2021. Disease discovery; mouse mechanism.
- 35266071: Sun G et al., *J Clin Immunol* 2022. p.W231R; point-mutant mice.
- 36823308: Sun G et al., *J Clin Immunol* 2023. Chinese multicenter cohort, 5 patients.
- 38231408: Olyha SJ et al., *J Clin Immunol* 2024. International cohort of 14; open access, PMC10929603.
- 36477361: Salinas SA et al., *JCI Insight* 2022. Hypomorphic variant with NK-cell deficiency.
- 39976696: Zhao R et al., *J Clin Immunol* 2025. Affected females with skewed X-inactivation.
- 38773005: Sun L et al., *J Clin Immunol* 2024. c.1022del; adalimumab response.
- 41005485: Tian C et al., *Mucosal Immunol* 2025. Intronic splice variant; colonic single-cell data.
- 38733460: Du HQ & Zhao XD, *World J Pediatr* 2024. Review.
- 39563044, 38948265, 41070654, 40800195, 41131646, 42769205, 42151449: further case reports and reviews.
- 39360366: Lv Q et al., 2024. Monogenic mimics of pediatric Behçet's disease.
- 24185615, 19412182, 24338897: ELF4 basic biology (type I IFN, CD8+ T cells).

Sources:
- [Olyha et al. 2024, PMC10929603](https://pmc.ncbi.nlm.nih.gov/articles/PMC10929603)
- [Tyler et al. 2021, PubMed 34326534](https://pubmed.ncbi.nlm.nih.gov/34326534/)
- [Sun G et al. 2023, PubMed 36823308](https://pubmed.ncbi.nlm.nih.gov/36823308/)
- [Sun G et al. 2022, PubMed 35266071](https://pubmed.ncbi.nlm.nih.gov/35266071/)
- [Salinas et al. 2022, PubMed 36477361](https://pubmed.ncbi.nlm.nih.gov/36477361/)
- [Zhao et al. 2025, PubMed 39976696](https://pubmed.ncbi.nlm.nih.gov/39976696/)
- [Tian et al. 2025, PubMed 41005485](https://pubmed.ncbi.nlm.nih.gov/41005485/)
- [Sun L et al. 2024, PubMed 38773005](https://pubmed.ncbi.nlm.nih.gov/38773005/)
- [Du & Zhao 2024, PubMed 38733460](https://pubmed.ncbi.nlm.nih.gov/38733460/)
- [You et al. 2013, PubMed 24185615](https://pubmed.ncbi.nlm.nih.gov/24185615/)
- [PubMed search: ELF4 deficiency](https://pubmed.ncbi.nlm.nih.gov/?term=ELF4%5Btiab%5D+AND+%28deficiency+OR+autoinflammatory+OR+Behcet+OR+DEX%29)
- [Pure EUR: Tyler 2021 record](https://pure.eur.nl/en/publications/human-autoinflammatory-disease-reveals-elf4-as-a-transcriptional-/)
- [Yale News 2021](https://news.yale.edu/2021/07/29/rare-disorder-offers-roadmap-understanding-inflammatory-disease)
- [Springer: Zhao 2025 (female DEX)](https://link.springer.com/article/10.1007/s10875-025-01866-2)
- [GenCC submission](https://thegencc.org/submissions/SGC-107498.2)
- [PanelApp ELF4](https://panelapp.genomicsengland.co.uk/panels/398/gene/ELF4/)