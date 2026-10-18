---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-18T17:02:08.247307'
end_time: '2026-09-18T17:07:01.518574'
duration_seconds: 293.27
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Black Widow Spider Envenomation
  mondo_id: MONDO:0800176
  category: Injury
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
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 23
  total_cost_usd: 1.6501894000000001
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Black Widow Spider Envenomation
- **MONDO ID:** MONDO:0800176 (if available)
- **Category:** Injury

## Research Objectives

Please provide a comprehensive research report on **Black Widow Spider Envenomation** covering all of the
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

I now have sufficient material to compile a comprehensive report. Let me write it up.

I now have comprehensive material across all required sections. Compiling the full research report.

# Black Widow Spider Envenomation (Latrodectism) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Black widow spider envenomation is an acute toxin-mediated injury syndrome ("latrodectism") caused by the bite of female spiders of the genus *Latrodectus* (family Theridiidae), which inject a venom whose principal vertebrate-active component, α-latrotoxin, produces massive, irreversible presynaptic neurotransmitter release. It is not a genetic/heritable disease but an acquired toxic-exposure/injury entity, and this fact should be reflected in the KB `category: Injury` designation and in leaving genetic-risk-factor sections largely empty. The syndrome ranges from mild local reaction to a severe systemic pain/autonomic/neuromuscular crisis; case-fatality is now essentially zero in the modern medical era. "Envenomation is called Latrodectism and the symptoms include diaphoresis, hypertension, muscle cramping, weakness, and severe abdominal and/or back pain; however, cases of death are rare" (Springer Nature reference chapter on Latrodectus venom toxins) [1].

**Key identifiers:**
- **ICD-10-CM:** T63.31– (Toxic effect of venom of black widow spider), with subcodes T63.311 (accidental), T63.312 (self-harm), T63.313 (assault), T63.314 (undetermined), each carrying encounter suffixes (A/D/S) [2].
- **MONDO:** MONDO:0800176 is asserted in the task template as the target identifier; independent web confirmation of this exact MONDO term was not retrievable via general search in this session — verify directly against the MONDO release/OLS before binding `disease_term.term.id` (per dismech's Ontology Term Contract, never bind a CURIE from memory).
- **MeSH:** Spider Bites (MeSH D013057) is the general parent heading under which Latrodectus envenomation literature is indexed; a dedicated "Latrodectism" MeSH heading was not confirmed in this session's searches.
- **HPO/OMIM/Orphanet:** Not applicable — this is an acute exogenous toxic injury, not a rare inherited disease, so OMIM and Orphanet have no dedicated entries.
- **NCBITaxon (causal organism):** Genus *Latrodectus* Walckenaer, 1805 (Theridiidae). Principal North American species: *Latrodectus mactans* (southern black widow) and *Latrodectus hesperus* (western black widow); *Latrodectus variolus* (northern black widow) also occurs in the U.S. [3][4].

**Synonyms/alternative names:** Latrodectism; black widow spider bite; *Latrodectus* envenomation; widow spider envenomation (encompassing redback, katipo, button spider, and other regional common names for congeneric species).

**Data provenance:** Information is drawn from aggregated clinical case series (e.g., a 163-case review, a >23,000-case National Poison Data System analysis), pharmacology/toxinology primary literature, and point-of-care summaries (StatPearls, UpToDate) rather than individual-patient EHR data.

---

## 2. Etiology

**Disease causal factor:** Direct mechanical injection of *Latrodectus* venom via chelicerae (fangs) during a bite, almost exclusively by adult female spiders — "Latrodectism is caused exclusively by bites from female black widow spiders, which possess larger venom glands, longer fangs, and bodies up to 20 times larger than males" [5]. This is a mechanistic/toxic (not infectious, not primarily genetic) causal factor.

**Risk factors:**
- *Environmental/behavioral (dominant category, since there is no meaningful genetic susceptibility axis for a venom-injection injury):*
  - Contact with spider habitats — firewood piles, garages, sheds, outhouses, gardening equipment, undisturbed clutter, outdoor furniture [5].
  - Warm-climate/seasonal exposure — "exposures rise in spring and increase through summer/autumn"; the spiders "thrive in warmer climates" and are present on every continent except Antarctica [5].
  - Occupational/recreational exposures: gardening, handling firewood, moving stored items, outdoor labor.
  - Geographic residence in endemic ranges (southeastern U.S. for *L. mactans*, western U.S./Canada/Mexico for *L. hesperus*) [5].
- *Host factors modulating severity (not "causal" but modify clinical outcome):*
  - **Small body size / pediatric age** is a recognized severity modifier — "Children are at risk of increased morbidity due to their small size, which is a critical factor in determining the severity of black widow spider envenomation" [6]. Bite-to-body-mass ratio effectively increases relative venom dose.
  - Pre-existing cardiovascular disease (hypertension, coronary artery disease) — increases risk of clinically significant sequelae from catecholamine surge (hypertensive crisis, myocardial ischemia); ECG evaluation is specifically recommended in patients with chest pain or known coronary disease [StatPearls, NBK499987].
  - Pregnancy — envenomation can mimic or precipitate preeclampsia-like features (hypertension, abdominal pain, proteinuria) [7][8].
  - Allergy/atopy history is a contraindication-risk factor specifically for antivenom administration, not for the bite itself.
- **Genetic risk/protective factors:** None established or biologically plausible for the acute toxic injury itself — human genetic variation in latrotoxin receptor genes (neurexins, latrophilins/ADGRL1-3) affecting envenomation severity has not been reported in the human clinical literature retrieved in this session. This should be recorded as an evidence gap, not populated with a spurious binding.
- **Gene-environment interaction:** Not applicable in the conventional sense; the "interaction" here is pharmacological (venom dose vs. body mass/pre-existing organ disease) rather than genomic.

---

## 3. Phenotypes

Phenotypes are dominated by acute local injury signs and a systemic pain/autonomic/neuromuscular syndrome. Frequency data below come from a large NPDS-derived case series and from a 163-case clinical review referenced in the StatPearls synthesis and Wikipedia's Latrodectism summary [StatPearls NBK499987; 9].

### Local (bite-site) phenotypes
| Phenotype | Onset | Frequency (large series) | Suggested HP term |
|---|---|---|---|
| Local pain at bite site | Minutes | 17.9% (as leading complaint in a large multi-severity cohort); near-universal in envenomated cases | HP:0012531 (Pain) / HP:0100710 (Impaired pain sensation — not applicable, this is presence of pain) |
| Erythema/redness | Minutes–hours | 28.6% | HP:0010783 (Erythema) |
| Edema/swelling at site | Minutes–hours | 13.6% | HP:0000969 (Edema) |
| Dermal irritation (generic) | Minutes | 58.7% | HP:0000988 (Skin rash) — use judiciously; better modeled as a Pathophysiology/clinical-sign node than forced to an ill-fitting HP term |
| Fang marks / central punctum | Immediate | Variable, often subtle | (No dedicated HP term; document as a clinical finding in `description`) |
| Localized diaphoresis in a ring around the bite ("target" sweating pattern) | Minutes–hours | Characteristic/near-pathognomonic when present | HP:0000975 (Hyperhidrosis) |

### Systemic (latrodectism) phenotypes
| Phenotype | Onset | Frequency/severity note | Suggested HP term |
|---|---|---|---|
| Diffuse muscle rigidity/cramping/spasm | 30–60 min, spreading proximally then generalizing | Hallmark systemic feature | HP:0003745 (Muscle rigidity) / HP:0003394 (Cramps) |
| Abdominal pain/rigidity (can mimic acute abdomen) | Within an hour | 9.7% in large series; classic diagnostic confounder | HP:0002027 (Abdominal pain) |
| Back and chest pain | Within hours | Common | HP:0100749 (Chest pain) |
| Diaphoresis (generalized or regional/asymmetric) | Minutes–hours | Common, and its unusual regional patterns (below-knee bilateral, asymmetric) are "almost pathognomonic" [10] | HP:0000975 (Hyperhidrosis) |
| Hypertension | Within an hour | Common; catecholamine-driven | HP:0000822 (Hypertension) |
| Tachycardia | Within an hour | Common | HP:0001649 (Tachycardia) |
| Nausea/vomiting | Within an hour | Common | HP:0002018 (Nausea) / HP:0002013 (Vomiting) |
| Headache, dizziness | Hours | Common | HP:0002315 (Headache) |
| Sialorrhea/lacrimation | Hours | Reported | HP:0100751 (Excessive salivation) |
| Mydriasis | Hours | Reported | HP:0000640 (Dilated pupil) |
| "Facies latrodectismica" — periorbital edema, blepharospasm, grimacing flush | Hours | Distinctive but rarely described; a described diagnostic gestalt [11] | (No single dedicated HP term; consider HP:0000534 Periorbital edema + HP:0000582 Blepharospasm as components) |
| Priapism | Hours (uncommon) | Rare, male-specific | HP:0025400 (Priapism, if present in current HPO) |
| Restlessness/anxiety | Hours | Common | HP:0000713 (Restlessness) |
| Respiratory symptoms (dyspnea, tachypnea) | Hours | Reported, more common in severe cases | HP:0002094 (Dyspnea) |
| Fever/chills | Hours | Reported | HP:0001945 (Fever) |

### Laboratory/biochemical phenotypes (uncommon but clinically significant)
- Leukocytosis, hematuria, elevated liver enzymes (nonspecific) [StatPearls NBK499987].
- **Rhabdomyolysis**: elevated creatine kinase, myoglobinuria — reported in rare case series, including a case of coexisting rhabdomyolysis, myocarditis, and arrhythmia [12]. HP candidate: HP:0003201 (Muscle fiber necrosis) is not exact; better modeled biochemically via a `Biochemical` marker (creatine kinase) than forced into HP.
- **Myocarditis**: elevated troponin/cardiac biomarkers, echocardiographic wall-motion abnormality and reduced ejection fraction (one case: EF 42%, pulmonary edema, ST elevation) — reversible in reported cases [13][14][15][16].

### Severity/course
A 23,409-case NPDS-style series stratified outcomes as: 65% minor clinical effects, 33.5% moderate effects (longer symptom duration, treatment required), 1.4% major/life-threatening effects [StatPearls NBK499987]. Symptom onset is typically within 30–60 minutes of the bite, and the diffuse systemic pain "spreads contiguously from the bite site" proximally to the trunk and other extremities.

**Quality of life impact:** Pain can be "incapacitating" and "persist for days" in severe latrodectism [Wikipedia/Latrodectism 9], but per StatPearls, "recovery is usually complete within 24 to 48 hours" and long-term pain or muscle spasms are rare, with most patients expected to make a full recovery.

---

## 4. Genetic/Molecular Information

There is **no host causal gene** for this disease — it is a toxin-injection injury. The molecular information that is disease-relevant instead concerns (a) the venom's toxin genes/proteins and (b) the human/vertebrate receptor genes the toxin acts upon.

**Venom toxin components:**
- **α-Latrotoxin (α-LTX)**: the principal vertebrate-specific neurotoxin, ~130 kDa, that forms tetrameric cation-selective membrane pores. "Highly purified α-latrotoxin from black widow spider venom consists of two polypeptides with molecular weights of 130,000 and 8000 (LMWP)" [17]. Structural work: "Structural basis of α-latrotoxin transition to a cation-selective pore" (PMC11449929) elucidates the pore-forming conformational transition [18].
- **Latrodectins (α-LTX-associated low-molecular-weight proteins, LMWPs)**: ~70-residue, 3-disulfide peptides structurally related to crustacean hyperglycemic hormones (an ecdysozoan neuropeptide hormone family); "purified latrodectin is not toxic in insects and mammals" but "appear to augment the neurotoxicity of latrotoxins, probably by increasing their affinity for the membrane target and reducing vertebrate phyla-specificity" [19][20].
- Other latrotoxin paralogs are phylum-selective: five latroinsectotoxins (α, β, γ, δ, ε-LIT, insect-active) and α-latrocrustatoxin (crustacean-active), reflecting toxin gene family diversification [1].
- **Molecular evolution**: "Molecular Evolution of α-Latrotoxin, the Exceptionally Potent Vertebrate Neurotoxin in Black Widow Spider Venom" (Mol Biol Evol) documents gene-family diversification underlying phylum specificity [21].

**Host (vertebrate) receptor genes bound by α-LTX** — these are the molecular targets, not causal disease genes, and are the correct anchors for GO/molecular-function annotation of the pathophysiology nodes:
- **Neurexin-1α (NRXN1, HGNC gene)**: Ca²⁺-dependent α-LTX receptor. "α-Latrotoxin binds to two distinct families of neuronal cell-surface receptors: neurexins and CIRL/latrophilins... binding of α-Latrotoxin to neurexin is a Ca²⁺-dependent reaction while its binding to CIRL is Ca²⁺-independent" [22]. In α-neurexin triple-knockout mice, "α-neurexins are not required for synapse formation, but are essential for Ca²⁺-triggered neurotransmitter release... because synaptic Ca²⁺ channel function is markedly reduced" [23] — an important mouse-model mechanistic finding (Nature 2003, "α-Neurexins couple Ca²⁺ channels to synaptic vesicle exocytosis") [24].
- **Latrophilin-1 / ADGRL1 (CIRL — Calcium-Independent Receptor for α-Latrotoxin)**: an adhesion GPCR. "Latrophilin 1 (LPHN1/ADGRL1) is an adhesion G-protein-coupled receptor (GPCR) that serves as the principal receptor for α-latrotoxin (αLTX)... Upon activation, LPHN1 engages the Gαq–phospholipase C pathway to generate inositol 1,4,5-trisphosphate (IP3), triggering Ca²⁺ release from intracellular stores via IP3 receptors" [25][26]. Three paralogs (ADGRL1–3) exist in mammals.
- **Protein Tyrosine Phosphatase σ (PTPRD/PTPσ)** has also been reported in the broader literature as a third latrotoxin-interacting receptor family (not directly confirmed in this session's searches — flag for further verification before binding).

**Functional consequence at the molecular/cellular level (for `functional_impact_category`/`modifier` framing):** α-LTX pore formation is a **gain-of-function, non-genetic** perturbation of the presynaptic terminal — i.e., this is the textbook case in the dismech schema where `modifier: GAIN_OF_FUNCTION` (or `INCREASED` for the downstream calcium influx/neurotransmitter release quantity) applies to a *biological_processes*/*molecular_functions* node with **no host genetic_context**, exactly analogous to the viral-oncoprotein pattern documented in CLAUDE.md (HTLV-1 Tax/NF-κB), because the "gain of function" is imposed on host channels/exocytotic machinery by an exogenous protein rather than by a host mutation.

**Epigenetics/chromosomal abnormalities:** Not applicable — no evidence in this session's search of any epigenetic or chromosomal dimension to human latrodectism.

---

## 5. Environmental Information

**Environmental factors (primary etiological category for this entry):**
- Habitat exposure: firewood stacks, garages, sheds, outhouses, undisturbed storage areas, woodpiles, gardening equipment, outdoor furniture, dense ground cover/shrubbery [pest-control/CDC-adjacent sources, 27].
- Climate/season: warm climates; exposures peak spring through autumn [5].
- Geographic exposure zone: endemic range of North American species (*L. mactans* southeastern U.S.; *L. hesperus* western North America; *L. variolus* northern/eastern U.S.) and, worldwide, other *Latrodectus* species (redback *L. hasselti* in Australia, katipo *L. katipo* in New Zealand, European black widow *L. tredecimguttatus*, button spiders *L. indistinctus*/*L. geometricus* in Africa, etc.) — "Latrodectus is worldwide in its distribution... present on every continent except Antarctica" [1][5][28].

**Lifestyle/occupational factors:** Gardening, firewood handling, moving stored materials, outdoor manual labor, use of outhouses — behaviors that bring hands/extremities into contact with spider harborage. Personal protective behaviors (gloves, shaking out stored clothing/shoes, long sleeves/pants) are risk-**reducing** environmental/behavioral factors [27].

**Infectious agents:** Not applicable — this is a venom-injection injury, not an infectious disease (though secondary wound infection at the bite site is a theoretically possible but rarely reported complication and was not specifically documented in this session's sources).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A mature female *Latrodectus* spider bites, injecting venom containing α-latrotoxin (α-LTX) and accessory latrodectin peptides through the chelicerae into subcutaneous tissue **→ leads to** local deposition of toxin near cutaneous sensory/autonomic nerve terminals and dermal microvasculature.
2. α-LTX binds two families of presynaptic membrane receptors — neurexin-1α (Ca²⁺-dependent binding) and latrophilin-1/ADGRL1 (Ca²⁺-independent binding) — which tether the toxin to the plasma membrane **→ results in** toxin oligomerization into a tetramer at the membrane surface.
3. The membrane-tethered α-LTX tetramer undergoes a conformational transition and inserts into the presynaptic plasma membrane, forming a cation-selective pore **→ leads to** massive, non-physiological Ca²⁺ (and Na⁺) influx into the presynaptic terminal, largely independent of voltage-gated Ca²⁺ channel gating.
4. In parallel, latrophilin-1/ADGRL1 engagement (Gαq–phospholipase C–IP3 pathway) triggers **IP3-receptor-mediated Ca²⁺ release from intracellular (ER) stores** — a second, receptor-signaling-dependent route to elevated cytosolic Ca²⁺, operating even without pore formation **→** this is a documented parallel/branching mechanism, not solely sequential to the pore.
5. The resulting sustained, supraphysiological rise in cytosolic Ca²⁺ triggers **massive, uncontrolled synaptic vesicle exocytosis** at both cholinergic (neuromuscular junction, parasympathetic/sympathetic preganglionic) and adrenergic (postganglionic sympathetic) nerve terminals — this Ca²⁺-triggered release pathway is notably documented to occur "independent of the classical synaptic fusion machinery" in some experimental paradigms, i.e., partially SNARE-independent [29] **→ leads to** depletion-then-exhaustion of vesicular pools and continuous, unregulated neurotransmitter discharge.
6. Neurotransmitters released include **acetylcholine** (at neuromuscular junctions and autonomic ganglia), **norepinephrine and epinephrine** (sympathetic terminals/adrenal medulla), **dopamine**, and **glutamate** [StatPearls NBK499987] **→ leads to, downstream, in a branching fashion:**
   - 6a. **Excess acetylcholine at the neuromuscular junction → sustained motor end-plate depolarization → diffuse skeletal muscle fasciculation, rigidity, cramping and spasm**, spreading contiguously from the bite site to trunk and other extremities.
   - 6b. **Excess catecholamine release (norepinephrine/epinephrine) → adrenergic autonomic storm → hypertension, tachycardia, diaphoresis (including characteristic localized/asymmetric sweating patterns), mydriasis, piloerection, and — in a minority of cases — hypertensive crisis, acute pulmonary edema, and reversible stress-related myocarditis with regional wall-motion abnormality** (documented case: EF 42%, ST elevation, elevated troponin, full recovery) [13-16].
   - 6c. **Autonomic/parasympathetic hyperactivity (excess acetylcholine at autonomic ganglia and lacrimal/salivary glands) → nausea, vomiting, sialorrhea, lacrimation, abdominal rigidity/pain** (which can mimic an acute surgical abdomen).
   - 6d. **Sustained muscle contraction/rigidity, when severe → rhabdomyolysis** (elevated creatine kinase, myoglobinuria), reported to co-occur with myocarditis and arrhythmia in rare severe cases [12].
7. Local vascular/inflammatory effects at the bite site (direct membrane pore formation in dermal cells plus autonomic vasomotor effects) **→ leads to** localized erythema, edema, the "target"-pattern localized diaphoresis, and occasionally a distinctive facial sign — **"facies latrodectismica"**: periorbital edema, blepharospasm, lacrimation, and a pained/grimacing flush, thought to reflect a combination of local autonomic and reflex muscular effects on the face and orbit [11].
8. In the great majority of cases, the toxin is progressively cleared/inactivated, vesicular neurotransmitter stores are replenished, and receptor/channel function normalizes **→ leads to symptom resolution**, typically complete within 24–48 hours (StatPearls), though severe pain can occasionally persist for days.
9. Where antivenom (equine-derived anti-*Latrodectus* IgG) is administered, circulating unbound and cell-surface-tethered toxin is neutralized before/soon after pore formation **→ leads to** more rapid symptom resolution in responders, though a large placebo-controlled RCT (RAVE-II, redback spider) found antivenom added to standardized analgesia did **not** produce a clinically meaningful reduction in pain severity or systemic effects compared to placebo [30][31] — an important caveat for the mechanism-to-treatment-efficacy link, and a `HUMAN_MODEL_MISMATCH`/efficacy-controversy note worth capturing in `discussions`.

### Detail by category

- **Molecular pathways:** Gαq–phospholipase C–IP3–Ca²⁺ signaling (latrophilin/ADGRL1 arm); direct cation pore-mediated Ca²⁺ influx (neurexin-tethered α-LTX tetramer arm). GO candidates: GO:0007186 (G protein-coupled receptor signaling pathway), GO:0048016 (inositol phosphate-mediated signaling), GO:0070588 (calcium ion transmembrane transport), GO:0016079 (synaptic vesicle exocytosis), GO:0007268 (chemical synaptic transmission).
- **Cellular processes:** massive regulated exocytosis (GO:0045055 regulated exocytosis), disrupted Ca²⁺ homeostasis (GO:0055074 calcium ion homeostasis), and, in severe cases, myocyte injury/necrosis contributing to rhabdomyolysis.
- **Protein dysfunction:** Not a host-protein misfolding disease — rather, exogenous toxin protein (α-LTX) directly forms an aberrant membrane channel (a "gain of novel toxic function" at the protein level, structurally characterized in PMC11449929 [18]).
- **Metabolic changes:** Secondary — rhabdomyolysis produces myoglobin/CK elevation and can (in principle, per general rhabdomyolysis pathophysiology) risk downstream renal complications, though acute kidney injury from black widow envenomation is reported as rare ("only one study reported acute kidney failure and rhabdomyolysis from black widow spider bites") [StatPearls NBK499987].
- **Immune involvement:** Not part of the toxin mechanism itself; immune/hypersensitivity mechanisms become relevant only for the iatrogenic complication of equine-antivenom administration (Type I hypersensitivity/anaphylaxis; Type III serum sickness, observed for 8–12 days post-antivenom) [32].
- **Tissue damage mechanisms:** Direct membrane pore formation (local cytotoxicity at bite site); catecholamine-excess-mediated cardiac stress/microvascular effects (myocarditis); sustained-contraction myocyte injury (rhabdomyolysis).
- **Cell types involved (CL terms):** presynaptic neuron terminals generally; motor neuron (CL:0000100), sympathetic neuron (CL:0011103 or similar), cardiac myocyte (CL:0000746) in myocarditis cases, skeletal muscle myocyte (CL:0000188) in rhabdomyolysis.
- **Anatomical/systemic involvement:** peripheral nervous system (neuromuscular junction, autonomic ganglia), cardiovascular system (secondary), skeletal muscle (secondary), skin (primary local site).
- **Molecular profiling / advanced omics:** No transcriptomic, proteomic, or single-cell human-disease-state profiling literature was identified in this session specific to human latrodectism (unsurprising for an acute self-limited toxic injury); venom-side proteomic/transcriptomic characterization of *Latrodectus* toxin gene families exists (the Mol Biol Evol α-LTX molecular evolution paper) but is venom biology, not host disease-state omics.

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - Primary: skin/subcutaneous tissue at bite site (UBERON:0002097 skin of body / UBERON:0000014 zone of skin); peripheral nervous system, specifically the neuromuscular junction and autonomic (sympathetic and parasympathetic) ganglia.
  - Secondary: cardiovascular system (heart — myocarditis, hypertensive crisis; UBERON:0000948 heart); skeletal muscle system generally (UBERON:0001134 skeletal muscle tissue) in rhabdomyolysis; gastrointestinal tract (smooth muscle rigidity causing abdominal pain mimicking acute abdomen); rarely kidney (secondary to rhabdomyolysis-associated AKI).
  - Body systems: nervous system (autonomic + neuromuscular), cardiovascular system, musculoskeletal system, integumentary system.
- **Tissue/cell level:** peripheral nerve terminal presynaptic membranes (the primary toxin target); vascular smooth muscle/endothelium (autonomic vasomotor effects); cardiac myocytes (myocarditis); skeletal myocytes (rhabdomyolysis); dermal/epidermal tissue at bite site.
- **Subcellular level (GO Cellular Component):** presynaptic active zone/plasma membrane (GO:0048786 presynaptic active zone; GO:0042734 presynaptic membrane), synaptic vesicle (GO:0008021), endoplasmic reticulum (as the Ca²⁺ store mobilized by the IP3 arm, GO:0005783/GO:0032991 ER lumen relevant subcompartment).
- **Localization:** Bite site is typically the extremities (upper and lower limbs most common per StatPearls). Systemic spread is bilateral/generalized once latrodectism develops, not classically lateralized, though localized/asymmetric diaphoresis patterns near the bite are a documented diagnostic clue.

---

## 8. Temporal Development

- **Onset:** Acute, minutes to about one hour after the bite for local signs; systemic latrodectism typically develops within 30–60 minutes and can evolve over several hours. There is no congenital or age-restricted "typical onset age" in the Mendelian-disease sense — onset is tied to the moment of envenomation, at any age, though pediatric bites carry disproportionate severity risk.
- **Progression:** Symptoms classically **spread contiguously** from the bite site proximally to trunk, chest, back, and other extremities over the first hours. Peak severity is typically reached within the first several hours to a day.
- **Disease course pattern:** Self-limited and non-progressive beyond the acute phase in the overwhelming majority of cases — "most pain and systemic symptomatology are self-limited," and "recovery is usually complete within 24 to 48 hours" (StatPearls). A minority of cases (documented case reports) show a more protracted or complicated course with cardiac/muscle complications requiring days of monitoring, and severe pain can rarely persist for several days.
- **Remission:** Spontaneous resolution is the norm without treatment beyond supportive care; antivenom, where effective, accelerates resolution (typically within ~30 minutes of infusion per some case-series claims), though this is contested by the RAVE-II placebo-controlled trial for redback envenomation, which found no significant benefit of antivenom over standardized analgesia [30][31].
- **Critical period:** The first several hours post-bite are the critical window for both symptom escalation and for clinical decision-making regarding antivenom/analgesia; cardiac and rhabdomyolysis complications, when they occur, are generally detected within this early window via ECG/troponin/CK monitoring.

---

## 9. Inheritance and Population

- **Inheritance pattern:** None — this is an acquired toxic injury, not a heritable disease. No penetrance, expressivity, anticipation, mosaicism, founder effect, or carrier-frequency concepts apply.
- **Epidemiology:**
  - Incidence: "Approximately 2,600 *Latrodectus*-species exposures are reported to the National Poison Data System (NPDS) each year" in the U.S.; a commonly cited complementary figure is "approximately 2,200 people are bitten in the United States by black widows every year" per AAPCC data [33][StatPearls NBK499987].
  - Mortality: extremely low; "no deaths have been recorded due to black widow bites since 1983" in the U.S. [33].
  - Severity distribution (large series, n=23,409): 65% minor, 33.5% moderate, 1.4% major/life-threatening effects [StatPearls NBK499987].
- **Population demographics:**
  - Geographic distribution: worldwide except Antarctica, following the cosmopolitan range of the genus *Latrodectus*, with the brown widow (*L. geometricus*) having achieved a "nearly cosmopolitan range... a suspected consequence of human transport" [34].
  - U.S. species distribution: *L. mactans* in southeastern states; *L. hesperus* from Canada to Mexico in the west; *L. variolus* in the north/east.
  - Seasonal distribution: spring through autumn peak.
  - Age distribution: all ages bitten, but children and small-body-mass individuals experience disproportionately severe envenomation for a given venom dose.
  - Sex ratio of *victims*: not specifically reported in retrieved sources (note: the sex-differential of the *spider* — only females bite clinically significantly — is well established, but human victim sex ratio was not found in this session's searches).

---

## 10. Diagnostics

- **Clinical diagnosis is primary.** "The diagnosis of black widow envenomation is almost exclusively clinically established; visualizing the bite along with its associated symptoms and obtaining a detailed history will allow accurate diagnosis" [35]. Formal confirmation via spider capture/entomologist identification is described in the literature but is explicitly "not recommended practice" as a routine step (StatPearls).
- **Laboratory tests:** Generally nonspecific — CBC (leukocytosis), urinalysis (hematuria), liver enzymes; targeted testing for creatine kinase and myoglobin when rhabdomyolysis is suspected; troponin/cardiac biomarkers and ECG when chest pain or cardiac risk factors are present (StatPearls explicitly recommends this).
- **Imaging/functional tests:** Echocardiography when myocarditis is suspected (documented reduced ejection fraction and wall-motion abnormality in case reports) [13-16].
- **Electrophysiology:** ECG for suspected cardiac involvement (ST-segment changes reported in myocarditis cases).
- **Genetic testing:** Not applicable — no genetic testing role.
- **Differential diagnosis** (explicitly enumerated in StatPearls): other arthropod bites/stings (scorpion sting, tarantula bite, brown recluse spider bite), acute abdominal pathology (appendicitis, other surgical abdomen, trauma), acute coronary syndrome, primary myocarditis of other etiology, and other causes of back/chest pain and muscle spasm.
- **Screening:** No population screening applicable (acute injury, not a heritable or slowly progressive condition).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Prognosis is excellent; U.S. mortality is essentially zero in the modern era (no deaths recorded since 1983) [33]. Historical (pre-antivenom-era) mortality was higher but modern supportive care and antivenom access have effectively eliminated fatal outcomes in most reporting systems.
- **Morbidity/function:** "Most patients can, and should, expect a full recovery," with resolution "usually complete within 24 to 48 hours" and long-term pain or muscle spasms being rare (StatPearls). Severe pain can occasionally be "incapacitating" and persist for days in a minority of cases.
- **Complications:** Rare but documented — reversible myocarditis (multiple case reports, generally full recovery) [13-16]; rhabdomyolysis, occasionally co-occurring with myocarditis and arrhythmia [12]; rare acute kidney injury secondary to rhabdomyolysis; iatrogenic anaphylaxis or serum sickness from equine antivenom administration [32].
- **Prognostic factors:** Body size/age (pediatric risk), pre-existing cardiovascular disease, time to treatment, and possibly venom dose (number of bites, spider size/species).

---

## 12. Treatment

- **Supportive/first-line care (all severities):** Local wound cleaning, tetanus prophylaxis. Note an important negative finding: "Calcium gluconate and methocarbamol have been shown to be ineffective and are no longer recommended" (StatPearls) — historically standard treatments that current evidence does not support.
- **Mild envenomation (local pain only):** Oral analgesics (NCIT:C15986 Pharmacotherapy generic action; oral NSAID/acetaminophen as `therapeutic_agent`).
- **Moderate–severe envenomation (systemic latrodectism):**
  - **Opioids** for pain control (NCIT:C15986 Pharmacotherapy; therapeutic_agent e.g. CHEBI-bound opioid such as morphine).
  - **Benzodiazepines** for muscle spasm control (NCIT:C15986 Pharmacotherapy; therapeutic_agent e.g. CHEBI:3373 diazepam or similar) — caution advised when co-administering opioids and benzodiazepines; combined take-home prescribing at discharge specifically not recommended (respiratory depression risk).
- **Antivenom (Antivenin Latrodectus mactans, equine-derived; also redback antivenom in Australia):**
  - Treatment term: NCIT — an antivenom/antitoxin-specific NCIT concept should be sought (not confirmed in this session; verify via OAK before binding, e.g., candidate NCIT:C946 Antivenin or similar — do not bind from memory).
  - Indicated, per FDA labeling, for "severe envenomation (eg, seizures, hypertensive crisis, respiratory compromise, or intractable pain), with no allergic contraindications" [32].
  - Efficacy is **contested**: multiple case series describe rapid, dramatic relief ("usually within 30 minutes of infusion"), and StatPearls states antivenom is "safe and highly effective in most patients," reducing need for additional therapy and admission — but the rigorous placebo-controlled RAVE-II RCT in redback envenomation (n=224) found antivenom added to standardized analgesia "did not significantly improve pain or systemic effects" [30][31]. This divergence between observational/case-series claims and RCT evidence is an important curation point — likely warranting a `discussions` entry with `kind: KNOWLEDGE_GAP` or explicit efficacy-controversy framing, and differential evidence grading (DIRECT clinical trial evidence vs. case-series/observational evidence) per the dismech evidence discipline.
  - Adverse effects: anaphylaxis (immediate hypersensitivity — flushing, urticaria, bronchospasm, cardiovascular collapse) and serum sickness (observed 8–12 days post-administration), reflecting its equine origin [32].
- **Investigational/human-antibody approaches:** A 2024 Frontiers in Immunology paper reports "Human antibodies neutralizing the alpha-latrotoxin of the European black widow," representing an experimental next-generation, non-equine antivenom approach [36].
- **Surgical/interventional:** None routinely indicated (wound care only).
- **Rehabilitative/supportive care:** Antiemetics for nausea/vomiting; general supportive monitoring (cardiac monitoring, serial CK/troponin as indicated).
- **Clinical trials:** ClinicalTrials.gov NCT00657540, "Black Widow Spider Antivenin for Patients With Systemic Latrodectism" [37] — a relevant NCT identifier for a `clinical_trials` block.
- **Treatment algorithm:** Severity-stratified — mild (local wound care + oral analgesia) → moderate (opioids + benzodiazepines, consider observation) → severe (add antivenom after risk-benefit assessment for allergy; ICU-level monitoring for cardiac/respiratory compromise).
- **Species-specific note:** In Australia, redback spider (*L. hasselti*) antivenom is the analogous product, extensively studied in the RAVE/RAVE-II trials; cross-neutralization studies show redback antivenom can neutralize *L. mactans*/*L. hesperus* venom in vitro [38].

---

## 13. Prevention

- **Primary prevention (environmental/behavioral, the dominant applicable category for this Injury-category entry):**
  - Habitat modification: declutter basements/attics/garages, remove debris/leaf litter/rock piles/dense shrubbery, store firewood elevated and ≥20 feet from the house [27].
  - Personal protective measures: wear gloves when moving stored items, gardening, or handling firewood/rocks; wear long sleeves/pants in wooded areas; shake out shoes, gloves, and hats before use [27].
  - Structural exclusion: seal cracks/crevices around windows, doors, and pipes.
  - Pest control: "Sanitation and exclusion can effectively reduce widow spider populations... avoidance and habitat modification techniques are more effective than applying pesticides" [27].
- **Secondary prevention:** Prompt recognition/self-identification of bite and early medical evaluation to catch evolving systemic symptoms; patient education on when to seek care (StatPearls: return precautions for rash, joint/muscle pain, hematuria, adenopathy, respiratory distress post-antivenom).
- **Tertiary prevention:** Monitoring protocol for at-risk patients (cardiac evaluation/serial ECG/cardiac markers/echocardiography in patients exposed, per case-report recommendations) to catch and manage rhabdomyolysis/myocarditis before progression.
- **Immunization:** No vaccine exists or is in development for latrodectism (venom-injection injuries are not vaccine-preventable in the conventional infectious-disease sense).
- **Genetic/carrier screening:** Not applicable.
- **Public health interventions:** Pest control programs in endemic/high-exposure occupational settings (agriculture, construction); occupational safety guidance (e.g., a U.S. military public health fact sheet on widow spiders was identified in search results [39]).
- **Prophylaxis:** No pre-exposure prophylactic medication exists; prophylactic antivenom is not standard practice.

---

## 14. Other Species / Natural Disease

- **Taxonomy of the causal organism:** Genus *Latrodectus* (NCBITaxon — genus-level taxon; e.g., *Latrodectus mactans* NCBITaxon:6753 region, verify exact TaxID via NCBI Taxonomy before binding). The genus comprises "30 currently recognized species" by some counts (Garb et al. 2004), organized into two well-supported clades: the *geometricus* clade (*L. rhodesiensis* + cosmopolitan *L. geometricus*, brown widow) and the *mactans* clade (all other species, spanning Africa, Middle East, Iberian Peninsula, Australia, New Zealand, and the Americas) [34].
- **Species commonly implicated in human/animal envenomation worldwide:** *L. mactans* (southern black widow, N. America), *L. hesperus* (western black widow, N. America), *L. variolus* (northern black widow, N. America), *L. tredecimguttatus* (European/Mediterranean black widow), *L. hasselti* (redback spider, Australia — extensively studied via RAVE trials), *L. katipo* (katipo, New Zealand, endangered native species), *L. geometricus* (brown widow, now cosmopolitan), *L. indistinctus* and other button spiders (southern Africa).
- **Natural disease in animals (this is a genuinely cross-species-susceptible toxin, not a human-specific pathology, and OMIA is not applicable since it is not a heritable animal disease):**
  - **Differential species susceptibility is a key comparative-biology finding:** "Canids have some resistance to black widow spider toxin; however, guinea pigs, cats, and horses are highly susceptible" [40].
  - **Cats are exceptionally vulnerable:** one cited study found "20 of 22 feline victims died subsequent to black widow envenomation with an average survival time of 115 hours after the bite" [40] — this is a striking veterinary mortality statistic worth capturing in an `animal_models`/comparative-biology note, as it illustrates both the toxin's cross-mammalian potency and marked species-specific sensitivity differences.
  - Dogs are also affected clinically despite relative resistance; veterinary case literature includes reports specifically on the related brown widow spider (*L. geometricus*) envenomation in dogs [41].
  - "The primary treatment for black widow spider envenomation [in animals] is the administration of specific antivenin, which provides the most permanent and quickest relief of the envenomation syndrome, usually within 30 minutes of infusion" [40] — mirroring human management.
- **Comparative pathology:** The core molecular mechanism (α-LTX pore formation/receptor engagement, massive neurotransmitter release) is conserved across vertebrates, explaining why the venom is broadly mammalian-active; species differences in susceptibility likely reflect differences in receptor expression/density, body-mass-to-venom-dose ratios, and baseline autonomic tone rather than a fundamentally different mechanism.
- **Zoonotic potential:** Not applicable — this is a direct envenomation injury, not a transmissible infectious disease; there is no animal-to-human transmission pathway beyond the spider bite itself.

---

## 15. Model Organisms

Black widow venom and α-latrotoxin have been central *research tools* in neuroscience (for probing synaptic vesicle exocytosis mechanisms) more than the *disease* itself being modeled in genetically engineered organisms — this is an important framing distinction for the KB entry (the mechanism is often studied via receptor-knockout models, not via "black-widow-bite disease models" per se).

- **Mouse models (mammalian, genetic):**
  - **α-Neurexin triple-knockout mice**: demonstrate that α-neurexins are dispensable for synapse formation but essential for Ca²⁺-triggered neurotransmitter release, because "synaptic Ca²⁺ channel function is markedly reduced" in their absence — directly implicating the neurexin receptor arm of the α-LTX mechanism (Missler et al., *Nature* 2003) [24].
  - **Latrophilin-1/ADGRL1 studies at the mouse neuromuscular junction**: "Latrophilin-1-Mediated Gαq Signaling, Store-Operated Ca²⁺ Entry, and CaV2.1 Activation Control Spontaneous Exocytosis at the Mouse Neuromuscular Junction" (2026, *Cells*) — a recent mechanistic dissection of the latrophilin/IP3/store-operated-calcium-entry arm using pharmacological and (implicitly) genetic mouse NMJ preparations [42][43].
  - **Mouse LD50 toxicology studies**: intraperitoneal LD50 for *L. hesperus* venom = 0.64 mg/kg and for *L. mactans* (N. American) = 0.26 mg/kg in one study; a separate study found *L. mactans tredecimguttatus* (European) whole venom LD50 = 0.9 mg/kg, and other reports of 1.39 mg/kg for *L. mactans*; regional venom variation is also documented (*L. dahli* LD50 0.99 ± 0.01 mg/kg; *L. pallidus* LD50 0.62 ± 0.01 mg/kg) [44]. These are useful `computational_models`/toxicology-model data points, though they characterize venom potency rather than disease phenotype recapitulation per se. Acute mouse envenomation signs include "chill, huddle and trembling, hair fold, shortness of breath, flaccid paralysis, difficulty to open eyes, urinary incontinence and hypothermia" [44] (from an egg-extract toxicity study, illustrative of whole-organism venom bioassay phenotypes).
  - **Cell/tissue-level models:** cultured neurons, permeabilized chromaffin cells, and PC12 cells have been used extensively (Journal of Neuroscience, EMBO J primary literature) to dissect the Ca²⁺-dependent vs. Ca²⁺-independent (SNARE-independent) exocytotic pathways triggered by α-LTX and its recombinant/mutant forms (e.g., LTXN4C mutant) [29][45][46].
- **Invertebrate models:**
  - ***Drosophila* neurexin studies** at the neuromuscular junction (PLOS ONE, "Neurexin in Embryonic Drosophila Neuromuscular Junctions") establish invertebrate conservation of neurexin's synaptic role, though this models the *receptor biology* rather than a whole-organism "latrodectism" phenotype [47].
  - Invertebrate/crustacean-selective latrotoxin paralogs (latroinsectotoxins, latrocrustatoxin) themselves are used as pharmacological tools in invertebrate synaptic physiology, reflecting the toxin family's phylum-restricted activity spectrum.
- **Model limitations:** No model fully recapitulates the *integrated human clinical syndrome* of latrodectism (pain, autonomic storm, rare cardiac/muscle complications) — the mouse/cell models are mechanistic dissections of the receptor–exocytosis pathway (largely **CELLULAR/MOLECULAR scale**, per dismech's `biological_scale`/`model_scale` conventions) rather than organism-level recapitulations of the **ORGANISM/TISSUE-scale** clinical phenotype (myocarditis, rhabdomyolysis). Any `modeled_mechanisms` link from these models to a disease-level pathophysiology node describing myocarditis or systemic pain would need to be flagged as an **upward extrapolation** requiring `limitations`, per the model-credibility conventions in this KB.
- **Applications:** These models have been the primary tool for elucidating fundamental presynaptic exocytosis biology broadly (not limited to spider-bite research), and secondarily validate the receptor-engagement/pore-formation mechanism underlying human latrodectism pathophysiology.

---

## Curation Notes for dismech Entry Population

1. **Verify MONDO:0800176** directly (OLS/MONDO release) before binding `disease_term.term.id` — not independently confirmed via general web search in this session.
2. **No genetic causal factors exist** for this entry; the `genetic:` section, if populated at all, should describe the *venom toxin genes* (α-latrotoxin, latrodectins) and the *human receptor genes* (NRXN1, ADGRL1) as molecular-target annotations on pathophysiology nodes, not as disease-causing genes — this is analogous to how an infectious-disease entry might annotate a pathogen virulence factor, and should not populate `Genetic.frequency`/`case_fractions` or inheritance patterns.
3. **The antivenom efficacy controversy (RAVE-II RCT vs. widespread case-series claims of benefit)** is a strong candidate for a `discussions` entry — it is a genuine, citable evidence conflict (DIRECT RCT evidence: `SUPPORT` for "no meaningful benefit"; multiple case series: `SUPPORT` for "rapid relief") rather than a simple consensus fact.
4. **Cell-of-origin/pathway framing** does not apply (not neoplastic); this entry's pathograph should instead be organized around the toxin-mechanism causal chain in Section 6 above, using `environmental[].influences_mechanisms` to link the "spider bite exposure" node (bound to an ECTO exposure term if one exists for envenomation, else left as free text with a `notes:` search record) into the pathophysiology cascade — the `TRIGGERS` predicate is directly applicable here.
5. **Priapism, facies latrodectismica, and the regional diaphoresis patterns** are distinctive enough to warrant individual phenotype nodes with careful `preferred_term` phrasing, since exact HP term matches are imperfect for several of them.

---

## Sources

- [1] [Recent Insights in Latrodectus ("Black Widow" Spider) Envenomation: Toxins and Their Mechanisms of Action](https://link.springer.com/rwe/10.1007/978-94-007-6646-4_23-1)
- [2] [2026 ICD-10-CM Diagnosis Code T63.31](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T63/T63.3-/T63.31)
- [3] [Latrodectus variolus – Wikipedia](https://en.wikipedia.org/wiki/Latrodectus_variolus)
- [4] [Latrodectus – Wikipedia](https://en.wikipedia.org/wiki/Latrodectus)
- [5] [Black Widow Spider Toxicity – StatPearls (NCBI Bookshelf NBK499987)](https://www.ncbi.nlm.nih.gov/books/NBK499987/)
- [6] [Silently Suffering: A Pediatric Black Widow Spider Envenomation – PubMed](https://pubmed.ncbi.nlm.nih.gov/33994256/)
- [7] [Black widow spider (Latrodectus mactans) bite during pregnancy – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1022401/)
- [8] [Venomous bites during pregnancy: the black widow spider (Latrodectus mactans)](https://www.tandfonline.com/doi/full/10.1080/15569543.2018.1435553)
- [9] [Latrodectism – Wikipedia](https://en.wikipedia.org/wiki/Latrodectism)
- [10] [Clinical presentation and treatment of black widow spider envenomation: A review of 163 cases](https://www.sciencedirect.com/science/article/abs/pii/S0196064405810212)
- [11] [Latrodectus Facies After Latrodectus Hesperus Envenomation in a Pediatric Patient – PubMed](https://pubmed.ncbi.nlm.nih.gov/31492593/)
- [12] [Coexistence of Rhabdomyolysis, Myocarditis and Arrhythmia after Spider Bite: A Case Report](https://academic.oup.com/tropej/article/68/3/fmac027/6569880)
- [13] [Reversible Myocarditis Following Black Widow Spider (Latrodectus spp.) Bite in Egypt: A case report – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10292600/)
- [14] [Reversible myocarditis after spider bite – PubMed](https://pubmed.ncbi.nlm.nih.gov/23572268/)
- [15] [Acute Myocarditis After Black Widow Spider Bite: A Case Report – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7584717/)
- [16] [Reversible Myocarditis after Black Widow Spider Envenomation – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3272799/)
- [17] [Low molecular weight components from black widow spider venom – ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0041010194001666)
- [18] [Structural basis of α-latrotoxin transition to a cation-selective pore – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11449929/)
- [19] [The low molecular weight protein which co-purifies with alpha-latrotoxin is structurally related to crustacean hyperglycemic hormones – PubMed](https://pubmed.ncbi.nlm.nih.gov/8051061/)
- [20] [Recruitment and diversification of an ecdysozoan family of neuropeptide hormones for black widow spider venom expression – PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC4172349)
- [21] [Molecular Evolution of α-Latrotoxin, the Exceptionally Potent Vertebrate Neurotoxin in Black Widow Spider Venom – Mol Biol Evol](https://academic.oup.com/mbe/article/30/5/999/992531)
- [22] [α-Latrotoxin and its receptors CIRL (latrophilin) and neurexin 1α mediate effects on secretion through multiple mechanisms – PubMed](https://pubmed.ncbi.nlm.nih.gov/10865131/)
- [23] [Neurexin I alpha is a major alpha-latrotoxin receptor that cooperates in alpha-latrotoxin action – PubMed](https://pubmed.ncbi.nlm.nih.gov/9430716/)
- [24] [α-Neurexins couple Ca2+ channels to synaptic vesicle exocytosis – Nature](https://www.nature.com/articles/nature01755)
- [25] [Latrophilin-1-Mediated Gαq Signaling, Store-Operated Ca2+ Entry, and CaV2.1 Activation Control Spontaneous Exocytosis at the Mouse Neuromuscular Junction – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13162755/)
- [26] [ADGRL1 | Adhesion Class GPCRs | IUPHAR/BPS Guide to PHARMACOLOGY](https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?objectId=206)
- [27] [How dangerous is a black widow spider bite? – Poison Control](https://www.poison.org/articles/black-widow-spiders)
- [28] [The black widow spider genus Latrodectus (Araneae: Theridiidae): phylogeny, biogeography, and invasion history – ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1055790303003968)
- [29] [α-Latrotoxin Stimulates a Novel Pathway of Ca2+-Dependent Synaptic Exocytosis Independent of the Classical Synaptic Fusion Machinery – J Neurosci](https://www.jneurosci.org/content/29/27/8639)
- [30] [Randomized controlled trial of intravenous antivenom versus placebo for latrodectism: The second Redback Antivenom Evaluation (RAVE-II) study – PubMed](https://pubmed.ncbi.nlm.nih.gov/24999282/)
- [31] [A randomised controlled trial of intramuscular vs. intravenous antivenom for latrodectism—the RAVE study – PubMed](https://www.ncbi.nlm.nih.gov/pubmed/18400776)
- [32] [Antivenin (Latrodectus mactans) (Equine) Monograph for Professionals – Drugs.com](https://www.drugs.com/monograph/antivenin-latrodectus-mactans-equine.html)
- [33] [The treatment of black widow spider envenomation with antivenin latrodectus mactans: a case series – PubMed](https://pubmed.ncbi.nlm.nih.gov/22058673/)
- [34] [Map showing distribution of Latrodectus species – ResearchGate](https://www.researchgate.net/figure/Map-showing-distribution-of-Latrodectus-species-marked-at-approximately-the-center-of_fig1_8585779)
- [35] [The black widow spider bite: differential diagnosis, clinical manifestations, and treatment options – PubMed](https://pubmed.ncbi.nlm.nih.gov/25978056/)
- [36] [Human antibodies neutralizing the alpha-latrotoxin of the European black widow – Frontiers in Immunology](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1407398/full)
- [37] [Black Widow Spider Antivenin for Patients With Systemic Latrodectism – ClinicalTrials.gov NCT00657540](https://clinicaltrials.gov/study/NCT00657540)
- [38] [Neutralization of Latrodectus mactans and L. hesperus venom by redback spider (L. hasseltii) antivenom – PubMed](https://pubmed.ncbi.nlm.nih.gov/11407496/)
- [39] [Widow Spiders – Public Health fact sheet](https://ph.health.mil/resources/WidowSpiders_FS_18-030-0818.pdf)
- [40] [Black Widow Spider Envenomation – Michael E. Peterson, DVM, MS](https://redtox.org/sites/default/files/toxiblog/descargables/2006-black-widow-spider-envenomation-ecc_1.pdf)
- [41] [Challenges in the diagnosis and management of brown widow spider (Latrodectus geometricus) envenomation in dogs – ResearchGate](https://www.researchgate.net/publication/379796386_Challenges_in_the_diagnosis_and_management_of_brown_widow_spider_Latrodectus_geometricus_envenomation_in_dogs)
- [42] [Latrophilin-1-Mediated Gαq Signaling, Store-Operated Ca2+ Entry, and CaV2.1 Activation Control Spontaneous Exocytosis at the Mouse Neuromuscular Junction – Cells (2026)](https://doi.org/10.3390/cells15090821)
- [43] [The Essential Role of Latrophilin-1 Adhesion GPCR Nanoclusters in Inhibitory Synapses – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11154861/)
- [44] [Physiological and biochemical characterization of egg extract of black widow spiders – Biological Research](https://link.springer.com/article/10.1186/0717-6287-47-17)
- [45] [Mechanisms of alpha-latrotoxin action – PubMed](https://pubmed.ncbi.nlm.nih.gov/10382267/)
- [46] [The α-Latrotoxin Mutant LTXN4C Enhances Spontaneous and Evoked Transmitter Release in CA3 Pyramidal Neurons – J Neurosci](https://www.jneurosci.org/content/23/10/4044)
- [47] [Neurexin in Embryonic Drosophila Neuromuscular Junctions – PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0011115)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 24 |
| On topic | 13 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.3390/cells15090821` (1 mention) - Latrophilin-1-Mediated Gαq Signaling, Store-Operated Ca2+ Entry, and CaV2.1 Activation Control Spontaneous Exocytosis at the Mouse Neuromuscular Junction
  - shared terms: via, toxin
- `PMC:PMC11154861` (1 mention) - Essential Role of Latrophilin-1 Adhesion GPCR Nanoclusters in Inhibitory Synapses.
  - shared terms: none

Weighed against this report's own most characteristic terms: `bite`, `spider`, `widow`, `pain`, `latrodectism`, `black`, `envenomation`, `muscle`, `venom`, `acute`, `systemic`, `disease`, `latrodectus`, `rhabdomyolysis`, `injury`, `clinical`, `myocarditis`, `via`, `toxin`, `serie`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 22 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800176` (3 mentions) - the report calls it "if available"; MONDO calls it **black widow spider envenomation**
- `HP:0100751` (1 mention) - the report calls it "Excessive salivation"; HP calls it **Esophageal neoplasm**
- `HP:0000640` (1 mention) - the report calls it "Dilated pupil"; HP calls it **Gaze-evoked nystagmus**
- `HP:0025400` (1 mention) - the report calls it "Priapism, if present in current HPO"; HP calls it **Nodular-random pattern on pulmonary HRCT**
- `HP:0000713` (1 mention) - the report calls it "Restlessness"; HP calls it **Agitation**
- `HP:0003201` (1 mention) - the report calls it "Muscle fiber necrosis"; HP calls it **Rhabdomyolysis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0048016` (obsolete inositol phosphate-mediated signaling) (1 mention)
- `CHEBI:3373` (CHEBI_3373) (1 mention) - replaced by `CHEBI:28837`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0048016` (1 mention) - the report calls it "inositol phosphate-mediated signaling"; GO calls it **obsolete inositol phosphate-mediated signaling**, and lists "inositol phosphate-mediated signalling" among its other names
