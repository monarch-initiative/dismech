---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-18T03:31:59.339974'
end_time: '2026-09-18T03:36:01.230353'
duration_seconds: 241.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ergotism
  mondo_id: MONDO:0042496
  category: Environmental
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
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 1.410423
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ergotism
- **MONDO ID:** MONDO:0042496 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Ergotism** covering all of the
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

I now have sufficient research material to compile a comprehensive report on Ergotism.

# Ergotism: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Ergotism (also called ergot poisoning, ergotoxicosis, or historically "St. Anthony's Fire" / "holy fire" / "ignis sacer") is a toxicological syndrome caused by ingestion of ergot alkaloids — indole (ergoline) alkaloids produced by fungi of the genus *Claviceps*, most classically *Claviceps purpurea*, which parasitizes rye and other cereal grains, forming dark sclerotia ("ergots") in place of normal grain kernels [Wikipedia: Ergotism](https://en.wikipedia.org/wiki/Ergotism); [Britannica: Ergotism](https://www.britannica.com/science/ergotism). The disease is not a Mendelian/genetic disorder but an environmental/toxicological entity — an acquired intoxication from either (a) contaminated food (classic/epidemic ergotism) or (b) pharmaceutical ergot-alkaloid derivatives used therapeutically (iatrogenic ergotism, the dominant modern form) [ScienceDirect: Ergotism overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/ergotism).

**Key identifiers.**
- **ICD-10-CM:** T62.2 (toxic effect of ingested mycotoxin food contaminants; ergot-specific subcodes exist in some national modifications), typically paired with an external-cause code [bionity.com: Ergotism](https://www.bionity.com/en/encyclopedia/Ergotism.html).
- **MeSH:** "Ergotism" is an indexed MeSH descriptor (used extensively across the PubMed literature retrieved above).
- **MONDO:** MONDO:0042496 was supplied as the target identifier for this curation; the general web search did not surface a public-facing MONDO term page distinct from the ontology's general documentation, so this identifier should be independently confirmed against the current MONDO release before binding (`just validate-terms`-equivalent check) rather than asserted from this report.
- **Orphanet:** no dedicated rare-disease Orphanet entry was located in this search; ergotism is a toxidrome rather than a genetically-defined rare disease, so Orphanet coverage may not exist — this should be verified directly against Orphanet rather than assumed absent.

**Synonyms:** St. Anthony's Fire, holy fire, ignis sacer, ergot poisoning, ergotoxicosis, ergotized-grain poisoning; the two principal clinical subtypes are named **gangrenous ergotism** and **convulsive ergotism** [Wikipedia: Ergotism](https://en.wikipedia.org/wiki/Ergotism); [National Geographic: St Anthony's fire](https://www.nationalgeographic.com/history/history-magazine/article/ergotism-infections-medieval-europe).

**Data derivation.** Modern knowledge is derived overwhelmingly from (1) aggregated case reports/case series of **iatrogenic ergotism** from therapeutic ergotamine/dihydroergotamine/methylergonovine use (individual-patient case reports, PMID-indexed), (2) historical and modern **epidemic outbreak investigations** of food-borne (grain-contamination) ergotism, especially in Ethiopia and India, and (3) **veterinary/agricultural toxicology** of livestock "fescue toxicosis"/"ergotism in animals," which is a well-studied natural-disease analog in cattle [Human and cattle ergotism since 1900 — PMID:22903169](https://pubmed.ncbi.nlm.nih.gov/22903169/); [Merck Veterinary Manual: Ergotism in Animals](https://www.merckvetmanual.com/toxicology/mycotoxicoses/ergotism-in-animals).

---

## 2. Etiology

**Disease causal factors.** Ergotism is **exogenous/environmental**, not intrinsic-genetic: it is caused by exposure to ergot alkaloids, either from (a) fungal contamination of food grain by *Claviceps* spp. sclerotia, or (b) pharmacological/iatrogenic overdose or drug-interaction-potentiated toxicity of ergot-derived medications (ergotamine, dihydroergotamine, methylergonovine/methylergometrine, ergonovine/ergometrine) [ASM.org: From Poisoning to Pharmacy](https://asm.org/articles/2018/november/from-poisoning-to-pharmacy-a-tale-of-two-ergots).

**Risk factors — environmental/exposure:**
- Consumption of rye or other cereal (wheat, barley, oats) contaminated with *Claviceps purpurea* sclerotia — historically the dominant cause of mass poisoning in medieval Europe, with cool, wet climates favoring fungal growth on grain [Ergotism — Wikipedia](https://en.wikipedia.org/wiki/Ergotism); a 9th-century Rhine Valley outbreak reportedly killed tens of thousands [National Geographic](https://www.nationalgeographic.com/history/history-magazine/article/ergotism-infections-medieval-europe).
- Poor food-safety/grain-cleaning infrastructure and lower socioeconomic status — modern outbreaks have occurred in Ethiopia (1977–78 and 2001, Arsi Zone, from ergotized wild-oat–contaminated barley) and India (1975) [Laboratory studies on the outbreak of Gangrenous Ergotism… Arsi, Ethiopia](https://www.ejhd.org/index.php/ejhd/article/view/798/609).
- Therapeutic ergot-alkaloid use (migraine treatment with ergotamine/dihydroergotamine; obstetric use of methylergonovine/ergometrine for postpartum hemorrhage) — the principal modern human risk exposure in industrialized settings [Severe iatrogenic ergotism: incidence and clinical importance — PMID:1908611](https://pubmed.ncbi.nlm.nih.gov/1908611/).
- **Drug-drug interaction risk factor:** co-administration of ergot alkaloids with potent CYP3A4 inhibitors — protease inhibitors (ritonavir, darunavir, atazanavir, indinavir, lopinavir, nelfinavir, saquinavir, tipranavir, amprenavir/fosamprenavir) and macrolide antibiotics (clarithromycin, telithromycin) — dramatically raises plasma ergotamine/DHE concentrations, converting a therapeutic dose into a toxic one; this is now considered a *contraindicated* combination [Drug Interaction Interaction of Ergotamine with Darunavir/Abacavir/Lamivudine — PMC6313968](https://pmc.ncbi.nlm.nih.gov/articles/PMC6313968/); case of coronary vasospasm with ergotamine + cobicistat + darunavir (PMID search, *J Int Med Res* 2022).
- HIV-positive patients on antiretroviral protease-inhibitor regimens are a specifically flagged modern at-risk population [A potentially lethal interaction: Migraine, HIV and ergotism — PMC11910312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11910312/).
- Concurrent tobacco/caffeine use has been implicated in exacerbating iatrogenic ergotism (cessation of these is part of first-line management).

**Genetic risk factors.** No Mendelian causal gene exists (this is an acquired toxidrome), but **genetic variability in hepatic CYP3A4/CYP3A5 metabolic capacity** (≈20 characterized variants, ~350 SNPs, most reducing enzyme activity) plausibly modulates individual susceptibility to ergotamine toxicity by altering systemic ergot-alkaloid clearance, though disease-specific pharmacogenomic studies for ergotism specifically were not found in this search and should be treated as inferred rather than established [CYP3A4 and CYP3A5: crucial roles in clinical drug metabolism — PMC11625447](https://pmc.ncbi.nlm.nih.gov/articles/PMC11625447/).

**Protective factors.**
- Modern grain-safety practices: fungicide use, crop rotation, planting of clean/inspected seed, and seed-flotation separation of ergot sclerotia from healthy kernels before milling [Medical News Today: Ergot poisoning](https://www.medicalnewstoday.com/articles/ergot-poisoning).
- Regulatory maximum limits on ergot sclerotia/alkaloid content in traded grain (see Prevention, §13).
- Avoidance of concomitant strong CYP3A4 inhibitors in patients prescribed ergot-derivative medications.

**Gene-environment interactions.** The principal documented interaction is pharmacogenomic/pharmacokinetic rather than germline-susceptibility: CYP3A4 inhibition (by co-administered drugs, a chemical/environmental factor) interacting with the pharmacologically active ergot-alkaloid "gene product" target profile (5-HT, dopamine, and α-adrenergic receptors) to produce toxic vasoconstriction at otherwise sub-toxic doses [Ergotamine/Caffeine — StatPearls NBK555953](https://www.ncbi.nlm.nih.gov/books/NBK555953/).

---

## 3. Phenotypes

Ergotism presents as two overlapping but classically distinguished symptom clusters, first well documented in Renaissance/medieval European epidemics and confirmed in modern case series:

### A. Gangrenous ergotism (vasospastic form)
- **Peripheral vasospasm/ischemia** of the extremities — cold, pale, painful hands/feet progressing to cyanosis, and dry gangrene with tissue necrosis, historically requiring limb amputation [Ergotism — Wikipedia](https://en.wikipedia.org/wiki/Ergotism). Suggested **HP term: HP:0034976 (Peripheral gangrene)** / general **HP:0025637 (Vasospasm)** if present in the enum; verify against the current HPO release before binding.
- **Burning pain/paresthesia** in the extremities ("St. Anthony's Fire" burning sensation) — precedes overt ischemia. Candidate **HP:0003401 (Paresthesia)**.
- **Diminished/absent peripheral pulses** (radial, ulnar, popliteal, tibial) — documented in case report of a 25-year-old with ergotamine-induced vasospasm [Reversal of ergotamine-induced vasospasm following methylprednisolone — PMID:18763151](https://pubmed.ncbi.nlm.nih.gov/18763151/).
- **Myocardial/coronary vasospasm and infarction** — reported in an obstetric case following intramuscular ergometrine for postpartum hemorrhage [Joining forces: cardio-obstetrics case of severe ergometrine-induced vasospasm — PMC11879452](https://pmc.ncbi.nlm.nih.gov/articles/PMC11879452/). Candidate **HP:0001677 (Coronary artery atherosclerosis)** is not quite right — better: free-text/CHEBI-linked vasospasm phenotype; consider **HP:0031650 (Vasospasm)** if present.
- **Cerebral ischemia/stroke** from vasospasm of cerebral arteries, in severe drug-interaction cases [Drug-Drug Interaction of Ergotamine… Fatal Vasospastic Ischemia — PMC6313968](https://pmc.ncbi.nlm.nih.gov/articles/PMC6313968/).
- **Transient monocular blindness** and **renal arterial spasm** — unusual manifestations documented in a historical review of ergot intoxication [Ergot Intoxication: Historical Review — PMC1343691](https://pmc.ncbi.nlm.nih.gov/articles/PMC1343691/).
- **Bilateral foot drop** from ischemic common peroneal nerve damage — an unusual, previously undocumented presentation in the same review.

### B. Convulsive ergotism (neuropsychiatric form)
- **Muscle spasms/twitching and painful seizures** — candidate **HP:0001250 (Seizure)**.
- **Hallucinations and psychosis/mania** — psychiatric manifestations historically mistaken for demonic possession in medieval accounts [Convulsive ergotism: epidemics of the serotonin syndrome? — PMID:12849122](https://pubmed.ncbi.nlm.nih.gov/12849122/). The paper's title itself argues convulsive ergotism may represent a historical analog of **serotonin syndrome**, given ergot alkaloids' serotonin-receptor agonism.
- **Paresthesias and itching (formication)** — a tactile hallucination of insects crawling under the skin, documented in the 2001 Ethiopian outbreak [Laboratory studies on the outbreak of Gangrenous Ergotism, Arsi, Ethiopia](https://www.ejhd.org/index.php/ejhd/article/view/798/609).
- **Diarrhea, nausea, vomiting** — gastrointestinal symptoms common to both forms.
- **Headache** — frequently reported, consistent with the serotonergic/vasoconstrictive mechanism also underlying ergotamine's therapeutic anti-migraine effect.
- **Fever and diaphoresis (sweating)**, lasting weeks in some accounts.
- **Weakness and burning sensations** — reported general prodromal symptoms in the 2001 Ethiopian outbreak.
- **Infant mortality from starvation**, attributed to maternal lactation failure during the outbreak — a distinctive, population-level secondary phenotype in the Ethiopian epidemic [same source].

**Phenotype characteristics:**
- **Onset:** acute-to-subacute after ingestion of contaminated grain (epidemic form) or after days-to-weeks of excessive/interacting ergot-medication use (iatrogenic form); in the case report above, symptoms began after ~1 week of ergotamine use for migraine and progressed over 2 days [PMID:18763151].
- **Severity:** highly variable — from mild paresthesia/headache to limb-threatening gangrene, blindness, stroke, or myocardial infarction, and (rarely) death.
- **Progression:** in gangrenous ergotism, progressive vasospasm → ischemia → dry gangrene → possible auto-amputation/surgical amputation if untreated; convulsive ergotism can show a fluctuating/relapsing course.
- **Frequency:** exact population frequencies are not established (this is an exposure-driven toxidrome rather than a fixed-penetrance disease); case-series literature is the primary quantitative source.
- **Reversibility:** iatrogenic ergotism is often reversible with prompt discontinuation of the causative agent — "recovery may occur within 4 days of stopping the ergot-containing medication" — but ischemic complications (gangrene, infarction, stroke) can be permanent if treatment is delayed [ScienceDirect: Ergotism treatment overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/ergotism); [Ergot Intoxication historical review, PMC1343691] ("no convincing evidence that any treatment other than discontinuation… is of benefit").

**Quality of life impact:** Limb amputation, chronic ischemic pain, and (in the psychotic/convulsive form) lasting neuropsychiatric sequelae are the major QoL burdens; specific validated QoL instrument data (EQ-5D/SF-36) for ergotism were not identified in this search and would need dedicated retrieval.

---

## 4. Genetic/Molecular Information

Ergotism has **no primary causal human gene** — it is a toxin-mediated disease. The "genetic/molecular" content that is relevant is almost entirely about (a) the fungal biosynthetic genes producing the toxin, and (b) the human drug-metabolizing/pharmacogenomic genes modulating host susceptibility.

- **Fungal causal genetics:** *Claviceps purpurea* ergot alkaloids are synthesized from a **14-gene biosynthetic gene cluster** in the fungal genome producing the ergoline/lysergic-acid-derived alkaloid metabolites [Bionity.com: Ergotism](https://www.bionity.com/en/encyclopedia/Ergotism.html).
- **Host pharmacogenomics:** CYP3A4 (and CYP3A5) — the human hepatic enzyme responsible for ergotamine/dihydroergotamine metabolism — carries ~20 characterized genetic variants and ~350 SNPs, most reducing enzymatic activity and thereby plausibly elevating individual susceptibility to ergotism when ergot-alkaloid drugs are used [PMC11625447]. Candidate gene: **CYP3A4 (HGNC:2637)**.
- **Not applicable:** somatic/germline variant classification (ClinVar/ACMG), chromosomal abnormalities, epigenetic disease drivers, and modifier genes in the classic Mendelian sense do not apply to this entity, since it is not a genetically caused disease. If the dismech schema requires a `genetic:` section, it should likely be limited to the CYP3A4 metabolic-susceptibility modifier framed as `relationship_type: MODIFIER` (pharmacogenomic host factor), not a causal gene.

---

## 5. Environmental Information

This is the **dominant etiological category** for ergotism and should anchor the `environmental:` section of the entry.

- **Fungal/mycotoxin contamination:** *Claviceps purpurea* (and related *Claviceps* spp.) infecting rye, wheat, barley, oats, and other cereal grasses, forming sclerotia ("ergots") that, if not removed before milling, contaminate flour and food products with ergot alkaloids [Ergot — Wikipedia](https://en.wikipedia.org/wiki/Ergot); [APS: Ergot Alkaloids](https://www.apsnet.org/edcenter/sites/Mycotoxins/Pages/ErgotAlkaloids.aspx).
- **Ergot alkaloid classes:** two principal chemical groups — **clavine alkaloids** and **lysergic acid alkaloids** (amides and peptide/ergopeptine alkaloids), sharing a **tetracyclic ergoline ring** core. Key compounds found in *Claviceps* sclerotia: **ergometrine (ergonovine)**, **ergotamine**, **ergosine**, **ergocristine**, **ergocryptine**, and **ergocornine** [Ergoline — Wikipedia](https://en.wikipedia.org/wiki/Ergoline); [Analysis of Ergot Alkaloids — PMC4488688](https://pmc.ncbi.nlm.nih.gov/articles/PMC4488688/). LSD (lysergic acid diethylamide) is chemically related but is a semi-synthetic derivative, not a natural sclerotial contaminant. Candidate CHEBI terms: ergotamine (**CHEBI:4880**-family), ergometrine, ergosine, ergocristine, ergocryptine, ergocornine (specific CHEBI IDs should be confirmed via `runoak` lookup per project convention rather than asserted here).
- **Iatrogenic/pharmaceutical exposure:** ergotamine tartrate, dihydroergotamine, methylergonovine/methylergometrine, and ergometrine used therapeutically (migraine abortive therapy; obstetric hemorrhage control) are the principal modern environmental exposure route in industrialized countries [Ergotamine/Caffeine — StatPearls NBK555953](https://www.ncbi.nlm.nih.gov/books/NBK555953/).
- **Climate factor:** cool, wet growing conditions favor *Claviceps* sporulation and sclerotia formation on grain heads, historically concentrating outbreaks in northern/central Europe and linked in the literature to periods of unusually wet weather preceding epidemic years [National Geographic: St Anthony's Fire](https://www.nationalgeographic.com/history/history-magazine/article/ergotism-infections-medieval-europe).
- **Socioeconomic/food-security factor:** contaminated-grain outbreaks recur in settings of food insecurity and inadequate grain-cleaning infrastructure — documented in Ethiopia (1977–78, 2001) and India (1975) [EJHD: Arsi Ethiopia outbreak](https://www.ejhd.org/index.php/ejhd/article/view/798/609).
- **Infectious agent:** *Claviceps purpurea* is technically a plant-pathogenic ascomycete fungus, not a human/animal infectious pathogen — ergotism is a toxicosis/mycotoxicosis, not an infection of the human host. NCBI Taxonomy: *Claviceps purpurea* (NCBITaxon — specific ID should be confirmed by lookup).
- **Drug-drug interaction as an environmental/exposure amplifier:** concomitant strong CYP3A4 inhibitors (protease inhibitors, macrolide antibiotics) are a well-documented environmental co-exposure that converts therapeutic ergot dosing into toxic exposure [PMC6313968]; [Cheng-En Wu et al., coronary vasospasm with ergotamine + cobicistat + darunavir, *J Int Med Res* 2022].

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion or therapeutic administration of ergot alkaloids** (ergotamine, dihydroergotamine, ergometrine/methylergonovine, or a mixture from contaminated grain) **leads to** systemic absorption of ergoline-ring compounds structurally similar to endogenous monoamine neurotransmitters (serotonin, dopamine, norepinephrine) [Ergot Alkaloid Pharmacology — pharmacology2000.com](https://www.pharmacology2000.com/Introduction%20to%20Medical%20Pharmacology/ERGO-Module1-Content.html).
2. **[Amplifying/optional branch]** Co-administration of a strong **CYP3A4 inhibitor** (protease inhibitor or macrolide) **inhibits hepatic ergot-alkaloid metabolism**, which **results in** markedly elevated plasma ergot-alkaloid concentrations even at otherwise-therapeutic oral doses [PMC6313968].
3. Elevated ergot-alkaloid concentration **leads to** simultaneous partial-agonist/agonist binding at multiple G-protein-coupled receptor families on vascular smooth muscle and neurons: **α1/α2-adrenergic receptors**, **serotonin 5-HT1B/5-HT1D/5-HT2A receptors**, and **dopamine D2-like receptors** [Investigation of the relationship between ergocristinine and vascular receptors — PMC10199403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10199403/); [Naunyn-Schmiedeberg's: non-peptide ergot alkaloids at 5-HT1-like and 5-HT2 receptors](https://link.springer.com/article/10.1007/BF00166953).
4. **Simultaneous activation of α-adrenergic and 5-HT2 receptors on vascular smooth muscle** **results in** sustained arterial and arteriolar vasoconstriction — this dual-receptor mechanism is specifically cited as the basis of ergot-induced vasospasm [ScienceDirect: Ergotism — Pharmacology/Toxicology topic](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/ergotism).
5. Sustained arterial vasoconstriction **leads to** regional tissue hypoperfusion/**ischemia**, particularly in the distal extremities (fingers, toes, hands, feet) where arterial supply is most vulnerable to prolonged spasm, and, in severe or drug-potentiated cases, in coronary, cerebral, renal, and ocular circulations [PMC1343691]; [PMC11879452 — coronary vasospasm/MI]; [PMC6313968 — cerebral ischemia].
6. Prolonged ischemia **results in** tissue hypoxia, oxidative/metabolic injury, and, if uncorrected, **dry gangrene and tissue necrosis** — historically the defining lesion of "gangrenous ergotism"/St. Anthony's Fire [Wikipedia: Ergotism].
7. **In parallel (branch)**, direct agonism of ergot alkaloids at central/peripheral **serotonin receptors** (5-HT) in the CNS **leads to** the neuropsychiatric/"convulsive ergotism" phenotype — muscle spasms, seizures, hallucinations, and psychosis — proposed in the literature to represent a historical epidemic analog of **serotonin syndrome** [Convulsive ergotism: epidemics of the serotonin syndrome? — PMID:12849122].
8. In the specific case of postpartum ergometrine/methylergonovine administration, ergot-receptor agonism also **acts directly on uterine smooth muscle** (the intended oxytocic/uterotonic pharmacological target) **in parallel with** unintended coronary/systemic vasospasm, explaining reports of peripartum myocardial infarction after obstetric ergot use [PMC11879452].

### Category detail

- **Molecular pathways:** GPCR signaling downstream of α-adrenergic, 5-HT (serotonergic), and dopaminergic receptor agonism on vascular and neuronal cell membranes. Candidate GO terms: **GO:0003085 (negative regulation of systemic arterial blood pressure)** is not quite right; more precise: **GO:0042311 (vasodilation)** [negatively implicated] and its antonym vasoconstriction processes — **GO:0042310 (vasoconstriction)** is a strong candidate for the primary node's biological process, and **GO:0007210 (serotonin receptor signaling pathway)** / **GO:0007212 (dopamine receptor signaling pathway)** / **GO:0071875 (adrenergic receptor signaling pathway)** for the receptor-signaling steps. (Confirm exact IDs/labels via OAK lookup before binding.)
- **Cellular processes:** vascular smooth muscle contraction (sustained, pathological — a "gain-of-function-like" qualitative overactivation rather than a quantitative INCREASED reading of a normally regulated process, given the exogenous receptor agonist driving it outside physiological regulatory constraints); ischemic cell injury/necrosis in distal tissue.
- **Protein dysfunction:** not a protein-structural disease — the mechanism is receptor *agonism* by an exogenous small molecule (ergot alkaloid) rather than any host protein misfolding or intrinsic dysfunction.
- **Tissue damage mechanisms:** ischemia-driven **dry gangrene/coagulative necrosis** of distal extremities; possible **myocardial infarction** from coronary vasospasm; possible **cerebral infarction/stroke** from intracranial arterial vasospasm; renal arterial spasm.
- **Biochemical abnormalities:** no primary enzyme deficiency; secondary biochemical consequences of ischemia (lactic acidosis in ischemic tissue) may occur but are non-specific.
- **Immune system involvement:** not a primary immune-mediated mechanism, although chronic gangrenous tissue may become secondarily infected/septic ("gangrene and sepsis of limbs" as a late-stage complication) [Wikipedia: Ergotism].
- **Cell types involved:** vascular smooth muscle cells (candidate **CL:0000359, vascular associated smooth muscle cell**, exact CL ID to confirm), and CNS neurons expressing serotonergic/dopaminergic receptor targets.

---

## 7. Anatomical Structures Affected

- **Organ level:** primary — peripheral vasculature of the extremities (hands, feet, digits); secondary — coronary arteries (myocardial ischemia/infarction), cerebral arteries (stroke), renal arteries, retinal/ophthalmic artery (transient monocular blindness), uterine vasculature (in obstetric ergot use), and peripheral nerves (ischemic mononeuropathy, e.g., common peroneal nerve → foot drop) [PMC1343691]. Body systems: cardiovascular, nervous, and (in convulsive form) central nervous/psychiatric.
- **Tissue/cell level:** vascular smooth muscle of small-to-medium arteries and arterioles is the direct pharmacological target; distal skin and subcutaneous tissue undergo ischemic/gangrenous change.
- **Subcellular level:** GPCR signal transduction at the plasma membrane of vascular smooth muscle cells and neurons (α-adrenergic, 5-HT, dopamine receptor complexes); no organelle-specific pathology is described in the literature reviewed.
- **Localization:** classically **bilateral and symmetric** in the epidemic/gangrenous form (both feet/hands), though case reports also document unilateral presentations (e.g., unilateral leg ischemia) [PMC1343691]. Candidate UBERON terms: extremities (**UBERON:0002542, appendage skeleton** — too broad; prefer digit/limb-specific terms), coronary artery (**UBERON:0001621**), cerebral artery, uterus (**UBERON:0000995**).

---

## 8. Temporal Development

- **Onset:** variable by route — epidemic/food-borne ergotism can present within days of consuming contaminated grain; iatrogenic ergotism has been reported after as little as ~1 week of therapeutic ergotamine use, and drug-interaction-potentiated cases can occur even with standard single/short-course dosing once a CYP3A4 inhibitor is added [PMID:18763151].
- **Progression:** gangrenous ergotism progresses through a recognizable sequence — burning paresthesia → coldness/pallor/cyanosis → absent pulses → dry gangrene, over a timescale of days; convulsive ergotism may show a fluctuating course with fever/sweating persisting for "several weeks" in some historical accounts.
- **Disease course pattern:** iatrogenic ergotism is generally **self-limited/reversible upon cessation of the causative agent**, with recovery reported within about 4 days in many cases; but ischemic complications that progress to gangrene or infarction before treatment become **fixed, irreversible** lesions.
- **Recurrence:** documented "recurrent ergotism" case reports exist in patients who resumed or continued using ergot-derivative medications after an initial episode [Recurrent Ergotism: A Case Report, *J Fam Pract* 1978](https://cdn.mdedge.com/files/s3fs-public/jfp-archived-issues/1978-volume_6-7/JFP_1978-04_v6_i4_recurrent-ergotism-a-case-report.pdf).
- **Critical window:** early recognition and cessation of the causative ergot exposure, plus prompt vasodilator therapy, represent the critical intervention window before irreversible ischemic tissue loss.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **not applicable** — ergotism is an acquired toxicological disease, not a Mendelian/heritable condition. No penetrance, expressivity, anticipation, mosaicism, founder-effect, or carrier-frequency concepts apply in the conventional genetic sense.
- **Epidemiology:** exact modern incidence/prevalence figures were not located in this search (expected, given the sporadic/case-report nature of modern disease); historically, epidemic outbreaks affected many thousands in medieval Europe (e.g., the 9th-century Rhine Valley outbreak reportedly killing "tens of thousands") [National Geographic]. Modern documented outbreaks: Ethiopia 1977–78 and 2001 (Arsi Zone, gangrenous ergotism from ergotized-wild-oat–contaminated barley, ~0.75% ergot content in affected grain) and India 1975 [EJHD Arsi Ethiopia study]; [Human and cattle ergotism since 1900 — PMID:22903169].
- **Population demographics:** modern iatrogenic ergotism disproportionately affects individuals prescribed ergot-alkaloid migraine therapy (historically more common in women, consistent with migraine epidemiology) and obstetric patients receiving ergometrine/methylergonovine for postpartum hemorrhage (exclusively female by indication). HIV-positive patients on protease-inhibitor regimens represent a specific modern at-risk subgroup due to the CYP3A4 drug-interaction mechanism [PMC11910312].
- **Geographic distribution:** historically concentrated in northern/central Europe (rye-dependent diet, cool wet climate favoring *Claviceps*); modern food-borne outbreaks concentrated in regions with less-regulated grain supply chains (Ethiopia, India).

---

## 10. Diagnostics

- **Clinical tests:**
  - **Angiography** — the primary diagnostic imaging modality, revealing characteristic segmental vasospastic narrowing of peripheral (and occasionally coronary/cerebral/renal) arteries, distinguishing ergotism from fixed atherosclerotic or embolic occlusion [PMC1343691]; angiographic pattern is also a key differentiator from thromboangiitis obliterans (Buerger disease), which shows distal segmental occlusive lesions with normal proximal arteries and a smooth, regular arterial wall without calcification [Thromboangiitis obliterans — PMC1523324](https://pmc.ncbi.nlm.nih.gov/articles/PMC1523324/).
  - Peripheral pulse examination (radial, ulnar, popliteal, tibial) — diminished/absent pulses support the diagnosis in the acute setting.
  - Toxicological/analytical confirmation — detection of ergotamine and ergometrine in contaminated grain samples was used to confirm etiology in the Ethiopian outbreak investigation [EJHD Arsi Ethiopia study].
- **Differential diagnosis:** thromboangiitis obliterans (Buerger disease), Raynaud phenomenon, other vasculitides (ergotism is specifically flagged as a vasculitis-mimic warranting careful differentiation in imaging reviews of medium/large-vessel disease) [AJR: Imaging of Primary and Secondary Inflammatory Diseases](https://ajronline.org/doi/full/10.2214/AJR.09.3367), scleroderma/CREST syndrome, and hypercoagulable states — recommended work-up includes CBC, liver function tests, creatinine, fasting glucose, ESR, ANA, rheumatoid factor, and hypercoagulability screening to exclude these mimics.
- **Genetic testing:** not applicable as a diagnostic modality for this condition (no causal gene); pharmacogenomic CYP3A4 genotyping is not a standard diagnostic test for ergotism itself but could theoretically inform risk stratification before prescribing ergot-derivative drugs.
- **Clinical criteria:** diagnosis is principally clinical — history of ergot-alkaloid exposure (medication or contaminated grain) plus compatible vasospastic/ischemic or convulsive/neuropsychiatric findings, supported by angiography and (in epidemic settings) toxicological confirmation of ergot alkaloids in the implicated food source.

---

## 11. Outcome/Prognosis

- **Reversibility with treatment:** the historical-review literature states plainly that "there is no convincing evidence that any treatment other than discontinuation of ergotamine is of benefit in the treatment of iatrogenic ergotism," and case reports document full recovery (e.g., complete resolution of ischemic foot drop within months) after cessation of the offending agent [PMC1343691].
- **Complications:** limb gangrene with risk of surgical amputation, myocardial infarction, cerebral infarction/stroke, transient or permanent monocular blindness, ischemic mononeuropathy, and (in untreated gangrenous cases) secondary sepsis [Wikipedia: Ergotism]; [PMC6313968 — fatal vasospastic ischemia case].
- **Mortality:** modern iatrogenic cases treated promptly generally have good outcomes; however, severe drug-interaction-potentiated cases (e.g., ergotamine + protease inhibitor) have been reported as **fatal** [PMC6313968 title: "…Causing a Fatal Vasospastic Ischemia"]. Historical epidemic ergotism carried substantial mortality, including reported infant deaths from lactation failure during the 2001 Ethiopian outbreak.
- **Prognostic factors:** speed of recognition and cessation of the causative ergot exposure; presence/absence of a potentiating CYP3A4-inhibitor interaction; severity/duration of ischemia before treatment; response to vasodilator therapy.

---

## 12. Treatment

- **First-line/supportive management:** **immediate discontinuation** of the causative ergot-alkaloid medication (and cessation of caffeine/tobacco, which may exacerbate vasospasm) [ScienceDirect: Ergotism treatment].
- **Vasodilator pharmacotherapy:**
  - **Sodium nitroprusside** (intravenous or intra-arterial infusion) — the most extensively documented treatment, described across multiple case series as effective in relieving vasospasm, often combined with forced diuresis and hydroxocobalamin administration to manage cyanide-release risk from prolonged nitroprusside use [Sodium Nitroprusside in the Treatment of Ergotism — *Radiology* 1977](https://doi.org/10.1148/124.1.73); [Intraarterial sodium nitroprusside infusion in the treatment of severe ergotism — PMID:3802106](https://pubmed.ncbi.nlm.nih.gov/3802106/). NCIT candidate: pharmacotherapy (**NCIT:C15986**) with therapeutic_agent sodium nitroprusside (CHEBI lookup required).
  - **Calcium channel blockers** and **prostaglandins** — cited as alternative direct vascular-smooth-muscle vasodilators for severe vasospasm [ScienceDirect: Ergotism treatment overview].
  - **Nitroglycerin** — studied experimentally in vitro and in migraine patients, and used to treat an overt ergotism case [Nitroglycerin for ergotism — *Eur J Clin Pharmacol*](https://link.springer.com/article/10.1007/BF00542453).
  - **Corticosteroids (methylprednisolone)** — reported as successful in a case unresponsive to sodium nitroprusside, suggested as alternative therapy especially for intractable cases [PMID:18763151].
- **Anticoagulation:** heparin, to prevent secondary thrombosis in ischemic vascular beds.
- **Interventional/surgical:** balloon angioplasty/dilatation, and surgical intervention (including amputation) for cases progressing to established gangrene despite medical therapy.
- **Treatment algorithm summary:** stop causative agent → vasodilator therapy (sodium nitroprusside first-line) ± heparin → escalate to corticosteroids or interventional/surgical management for refractory or advanced ischemic disease.
- **Experimental/investigational:** no dedicated clinical trials (NCT-registered) specifically for ergotism treatment were identified in this search; management is derived from case reports and small case series rather than randomized trial evidence.
- **Genetic-counseling/screening interventions:** not applicable (non-genetic disease).

---

## 13. Prevention

- **Primary prevention (food safety):**
  - EU **Regulation (EU) 2021/1399** (amending Regulation (EC) No 1881/2006) sets maximum levels for ergot sclerotia and for the sum of 12 toxicologically relevant ergot alkaloids in cereals and cereal products, effective 1 January 2022; unprocessed-cereal sclerotia limits were tightened (e.g., ≤0.5 g/kg for rye, with further reduction to 0.2 g/kg from 1 July 2024 for certain categories), because milling can grind sclerotia into "ergot dust" that contaminates grain even without visible sclerotia, necessitating separate alkaloid (not just sclerotia) limits [Europe sets new ergot alkaloids limits — Food Safety News](https://www.foodsafetynews.com/2021/09/europe-sets-new-ergot-alkaloids-limits/); [Commission Regulation (EU) 2021/1399 text](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32021R1399&rid=2).
  - Modern agricultural practice: fungicide application, crop rotation, use of clean/certified seed, and mechanical seed-cleaning (flotation separation of sclerotia) before milling [Medical News Today: Ergot poisoning].
- **Secondary prevention/screening:** routine grain inspection and cleaning at mills; surveillance of grain-supply chains in food-insecure regions where prior outbreaks have occurred.
- **Tertiary prevention (iatrogenic disease):** prescriber vigilance for CYP3A4-drug-interaction risk — avoiding co-prescription of ergot-alkaloid medications with protease inhibitors or macrolide antibiotics; ergotamine/DHE are now labeled **contraindicated** with strong CYP3A4 inhibitors [drug interaction sources above].
- **Counseling:** patient education regarding maximum ergot-medication dosing limits and drug-interaction avoidance for migraine patients on chronic ergotamine therapy; obstetric protocols limiting ergometrine/methylergonovine dosing.
- **Public health:** governmental grain-inspection regulation as the principal public-health lever, given the disease's near-total dependence on food-supply contamination in its epidemic form.

---

## 14. Other Species / Natural Disease

Ergotism is **naturally occurring and economically significant in livestock**, providing a well-studied comparative-pathology model:

- **Cattle ("fescue toxicosis"/"fescue lameness"):** grazing on endophyte-infected tall fescue (*Lolium arundinaceum*/*Festuca arundinacea*, infected by the endophytic fungus *Epichloë coenophiala*, which — like *Claviceps* — produces ergopeptine alkaloids, principally **ergovaline**, constituting ~90% of ergopeptide alkaloids in toxic fescue) causes a clinical syndrome closely paralleling human gangrenous ergotism: hindlimb lameness progressing to distal-limb necrosis/gangrene, tail and ear necrosis, rough coat, reduced body mass, and an arched-back posture [Merck Veterinary Manual: Fescue Poisoning in Animals](https://www.merckvetmanual.com/toxicology/mycotoxicoses/fescue-poisoning-in-animals); [It's fescue toxicosis on steroids — Hay and Forage Magazine](https://hayandforage.com/article-806-It's-fescue-toxicosis-on-steroids.html).
- **Toxic threshold:** ergovaline concentrations of 100–500 ppb are typical in infected fescue, with **>200 ppb considered toxic**; the mechanism mirrors the human disease — agonism at monoamine (adrenergic/serotonergic) receptors on vascular smooth muscle due to structural similarity between ergot alkaloids and endogenous monoamine neurotransmitters [Impact of Ergot Alkaloids on Female Reproduction in Domestic Livestock — PMC6628433](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6628433/).
- **Reproductive toxicity in livestock:** altered estrous cyclicity, suppressed hormone secretion, reduced pregnancy rates, agalactia (failure of milk production — directly paralleling the human infant-lactation-failure deaths reported in the 2001 Ethiopian outbreak), and reduced offspring birth weight [PMC6628433].
- **Economic burden:** fescue toxicosis is estimated to cause **over $2 billion in annual economic loss** to U.S. livestock industries [Fescue Toxicosis — Hay and Forage Magazine].
- **Comparative biology:** the shared receptor-agonism mechanism (adrenergic + serotonergic vasoconstriction) across cattle and humans makes livestock fescue-toxicosis studies a natural, non-experimental disease model directly informative for human ergotism pathophysiology — this is a naturally occurring analog rather than a laboratory-induced model.
- **Other species:** ergotism is also documented in horses, sheep, and other grazing livestock exposed to ergotized pasture grasses or contaminated feed grain [Merck Veterinary Manual: Ergotism in Animals](https://www.merckvetmanual.com/toxicology/mycotoxicoses/ergotism-in-animals).
- **Zoonotic potential:** none — this is a shared dietary/environmental toxin exposure across species (both grazing on/eating the same contaminated plant material), not a transmissible infectious disease between species.

---

## 15. Model Organisms

- **Livestock as natural disease models:** cattle (particularly Angus breed studies of fescue-toxicosis resistance/susceptibility) and sheep represent the best-characterized **naturally occurring, non-induced animal models** of ergot-alkaloid-induced vasoconstrictive disease, closely recapitulating the human gangrenous phenotype [Evaluation of Resistance to Fescue Toxicosis in Purebred Angus Cattle — PMC7764894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7764894/).
- **Experimental/induced models:**
  - **Sheep** — acute ergot-alkaloid dosing studies directly measuring vasoactive/vasoconstrictive responses ("Vasoactive Effects of Acute Ergot Exposure in Sheep" — PMC8072561), providing a controlled induced-exposure model complementing the natural cattle-grazing model.
  - **Isolated vascular tissue preparations** — rat aorta, rabbit aorta, bovine lateral saphenous vein, and human saphenous vein (obtained during varicose-vein saphenectomy surgery) have been used ex vivo to characterize ergot-alkaloid receptor pharmacology (5-HT1/5-HT2/α-adrenergic receptor contributions to vasoconstriction) [Actions of non-peptide ergot alkaloids at 5-HT1-like and 5-HT2 receptors — *Naunyn-Schmiedeberg's Arch Pharmacol*](https://link.springer.com/article/10.1007/BF00166953); [Alpha-adrenoceptors, 5-HT receptors and dihydroergotamine in human venous preparations](https://link.springer.com/article/10.1007/BF00506240); [Serotonin receptor-mediated vasorelaxation in bovine lateral saphenous vein — PMC11214916](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11214916/).
  - **Pithed rat model** — used to pharmacologically dissect the specific receptor subtypes (5-HT1A/1B/1D, α2-adrenoceptors, D2-like receptors) mediating ergotamine's inhibition of vasopressor sympathetic outflow [Pharmacological evidence that 5-HT1A/1B/1D, α2-adrenoceptors and D2-like receptors mediate ergotamine-induced effects — ScienceDirect].
- **Model characteristics/limitations:** the isolated-vessel ex vivo preparations recapitulate the **receptor-pharmacology** of ergot-alkaloid vasoconstriction well but cannot model the **systemic ischemic/gangrenous tissue outcome**; the cattle/sheep whole-animal models recapitulate the full phenotype (vasospasm → distal necrosis → reproductive/lactation failure) with high translational fidelity to the human disease, given the shared receptor pharmacology and grazing/dietary exposure route, though species differences in vascular receptor density and diet composition remain translational caveats.
- **Resources:** no dedicated ergotism-specific model-organism database was identified (unlike Mendelian-disease model registries such as MGI/IMPC); the relevant literature is distributed across veterinary toxicology (Merck Veterinary Manual, agricultural extension publications) and pharmacology journals rather than a centralized model-organism resource.

---

## Notes on Curation Gaps and Verification Needed

- **MONDO:0042496** should be independently verified against the current MONDO build before being bound as `disease_term`; this report could not confirm the identifier via public search.
- Specific **CHEBI IDs** for ergotamine, ergometrine, ergosine, ergocristine, ergocryptine, and ergocornine, and specific **HP/GO/CL/UBERON** term IDs suggested above, are candidates only — per the dismech ontology-term contract, each must be independently confirmed via `runoak`/cache lookup at curation time rather than written from this report.
- Orphanet/OMIM coverage was not confirmed either way in this search and should be checked directly.
- No NCT-registered clinical trials specific to ergotism treatment were located; treatment evidence is case-report/case-series level throughout.
- Precise modern incidence/prevalence rate figures (cases per 100,000) were not found and may not exist in a form suitable for the `Prevalence` schema's `rate_per_100000` slot — `CASES_IN_LITERATURE` may be the most defensible `measure_type` for this entry given the sporadic/case-report evidence base.

---

### Sources

- [Ergotism — Wikipedia](https://en.wikipedia.org/wiki/Ergotism)
- [Ergotism — Britannica](https://www.britannica.com/science/ergotism)
- [Ergotism — an overview | ScienceDirect Topics (medicine/dentistry)](https://www.sciencedirect.com/topics/medicine-and-dentistry/ergotism)
- [Ergotism — an overview | ScienceDirect Topics (pharmacology/toxicology)](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/ergotism)
- [From Poisoning to Pharmacy: A Tale of Two Ergots — ASM.org](https://asm.org/articles/2018/november/from-poisoning-to-pharmacy-a-tale-of-two-ergots)
- [What was St Anthony's fire, the medieval killer in the rye? — National Geographic](https://www.nationalgeographic.com/history/history-magazine/article/ergotism-infections-medieval-europe)
- [Ergot poisoning: History, causes, symptoms, and more — Medical News Today](https://www.medicalnewstoday.com/articles/ergot-poisoning)
- [Ergotism — bionity.com](https://www.bionity.com/en/encyclopedia/Ergotism.html)
- [Ergot Intoxication: Historical Review and Description of Unusual Clinical Manifestations — PMC1343691 (PMID:4371616)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1343691/)
- [Convulsive ergotism: epidemics of the serotonin syndrome? — PMID:12849122](https://pubmed.ncbi.nlm.nih.gov/12849122/)
- [Human and cattle ergotism since 1900: symptoms, outbreaks, and regulations — PMID:22903169](https://pubmed.ncbi.nlm.nih.gov/22903169/)
- [Laboratory studies on the outbreak of Gangrenous Ergotism… Arsi, Ethiopia — Ethiopian Journal of Health Development](https://www.ejhd.org/index.php/ejhd/article/view/798/609)
- [Reversal of ergotamine-induced vasospasm following methylprednisolone — PMID:18763151](https://pubmed.ncbi.nlm.nih.gov/18763151/)
- [Joining forces: cardio-obstetrics case of severe ergometrine-induced vasospasm — PMC11879452](https://pmc.ncbi.nlm.nih.gov/articles/PMC11879452/)
- [Drug-Drug Interaction of Ergotamine with Darunavir/Abacavir/Lamivudine Causing a Fatal Vasospastic Ischemia — PMC6313968](https://pmc.ncbi.nlm.nih.gov/articles/PMC6313968/)
- [A potentially lethal interaction: Migraine, HIV and ergotism — PMC11910312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11910312/)
- [Severe iatrogenic ergotism: incidence and clinical importance — PMID:1908611](https://pubmed.ncbi.nlm.nih.gov/1908611/)
- [Recurrent Ergotism: A Case Report — Journal of Family Practice, 1978](https://cdn.mdedge.com/files/s3fs-public/jfp-archived-issues/1978-volume_6-7/JFP_1978-04_v6_i4_recurrent-ergotism-a-case-report.pdf)
- [Ergotamine/Caffeine — StatPearls NBK555953](https://www.ncbi.nlm.nih.gov/books/NBK555953/)
- [CYP3A4 and CYP3A5: crucial roles in clinical drug metabolism and genetic polymorphisms — PMC11625447](https://pmc.ncbi.nlm.nih.gov/articles/PMC11625447/)
- [Ergoline — Wikipedia](https://en.wikipedia.org/wiki/Ergoline)
- [Analysis of Ergot Alkaloids — PMC4488688](https://pmc.ncbi.nlm.nih.gov/articles/PMC4488688/)
- [Ergot Alkaloids — American Phytopathological Society](https://www.apsnet.org/edcenter/sites/Mycotoxins/Pages/ErgotAlkaloids.aspx)
- [Investigation of the relationship between ergocristinine and vascular receptors — PMC10199403](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10199403/)
- [Actions of non-peptide ergot alkaloids at 5-HT1-like and 5-HT2 receptors — Naunyn-Schmiedeberg's Archives of Pharmacology](https://link.springer.com/article/10.1007/BF00166953)
- [Alpha-adrenoceptors, 5-HT receptors and dihydroergotamine in human venous preparations — Naunyn-Schmiedeberg's Archives of Pharmacology](https://link.springer.com/article/10.1007/BF00506240)
- [Serotonin receptor-mediated vasorelaxation in bovine lateral saphenous vein — PMC11214916](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11214916/)
- [Sodium Nitroprusside in the Treatment of Ergotism — Radiology, 1977](https://doi.org/10.1148/124.1.73)
- [Intraarterial sodium nitroprusside infusion in the treatment of severe ergotism — PMID:3802106](https://pubmed.ncbi.nlm.nih.gov/3802106/)
- [Nitroglycerin for ergotism — European Journal of Clinical Pharmacology](https://link.springer.com/article/10.1007/BF00542453)
- [Thromboangiitis obliterans (Buerger's disease) — PMC1523324](https://pmc.ncbi.nlm.nih.gov/articles/PMC1523324/)
- [Imaging of Primary and Secondary Inflammatory Diseases Involving Large and Medium-Sized Vessels — AJR](https://ajronline.org/doi/full/10.2214/AJR.09.3367)
- [Commission Regulation (EU) 2021/1399 — EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32021R1399&rid=2)
- [Europe sets new ergot alkaloids limits — Food Safety News](https://www.foodsafetynews.com/2021/09/europe-sets-new-ergot-alkaloids-limits/)
- [Merck Veterinary Manual: Ergotism in Animals](https://www.merckvetmanual.com/toxicology/mycotoxicoses/ergotism-in-animals)
- [Merck Veterinary Manual: Fescue Poisoning in Animals](https://www.merckvetmanual.com/toxicology/mycotoxicoses/fescue-poisoning-in-animals)
- [Impact of Ergot Alkaloids on Female Reproduction in Domestic Livestock Species — PMC6628433](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6628433/)
- [It's fescue toxicosis on steroids — Hay and Forage Magazine](https://hayandforage.com/article-806-It's-fescue-toxicosis-on-steroids.html)
- [Evaluation of Resistance to Fescue Toxicosis in Purebred Angus Cattle — PMC7764894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7764894/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 10 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11625447` (5 mentions) - CYP3A4 and CYP3A5: the crucial roles in clinical drug metabolism and the significant implications of genetic polymorphisms.
  - shared terms: cyp3a4, human
- `PMC:PMC11879452` (6 mentions) - Joining forces: a complex cardio-obstetrics case report of severe ergometrine-induced vasospasm.
  - shared terms: vasospasm, ergometrine
- `PMC:PMC11214916` (4 mentions) - Serotonin receptor-mediated vasorelaxation occurs primarily through 5-HT(4) activation in bovine lateral saphenous vein.
  - shared terms: receptor

Weighed against this report's own most characteristic terms: `ergotism`, `ergot`, `disease`, `ergotamine`, `alkaloid`, `gangrenous`, `epidemic`, `outbreak`, `grain`, `vasospasm`, `cyp3a4`, `ergot-alkaloid`, `iatrogenic`, `ischemic`, `human`, `modern`, `documented`, `receptor`, `gangrene`, `ergometrine`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0042496` (3 mentions) - the report calls it "if available"; MONDO calls it **ergotism**
- `HP:0034976` (1 mention) - the report calls it "Peripheral gangrene"; HP calls it **Absent pituitary stalk**
- `HP:0031650` (1 mention) - the report calls it "Vasospasm"; HP calls it **Abnormal atrioventricular valve physiology**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CHEBI:4880` (CHEBI_4880) (1 mention) - replaced by `CHEBI:16000`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007212` (1 mention) - the report calls it "dopamine receptor signaling pathway"; GO calls it **G protein-coupled dopamine receptor signaling pathway**, and lists "dopamine receptor signalling pathway" among its other names
