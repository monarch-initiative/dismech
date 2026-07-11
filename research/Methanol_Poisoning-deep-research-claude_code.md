---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-10T14:27:57.285574'
end_time: '2026-07-10T14:33:17.324122'
duration_seconds: 320.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Methanol Poisoning
  mondo_id: ''
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 9
  num_turns: 13
  total_cost_usd: 2.3770937500000002
  session_id: 7c2c2f69-3077-440a-82ae-2b7c420aa053
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methanol Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Methanol Poisoning** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I now have enough well-sourced material to write the comprehensive report. Here it is.

---

# Comprehensive Research Report: Methanol Poisoning

**Prepared:** 2026-07-10 | **Category:** Environmental / Toxicological | **Entry type:** Acquired chemical intoxication (not a heritable disease)

> **Curation note on scope:** Methanol poisoning is an acquired toxic exposure, not a Mendelian or complex genetic disease. Sections of the template that assume a heritable etiology (causal genes, inheritance pattern, penetrance, carrier frequency, chromosomal abnormalities, model-organism knockouts) are largely **Not Applicable**; where a genetic/pharmacogenetic angle exists (ADH/ALDH/folate-enzyme variation, animal models of formate toxicity) it is reported in the relevant section. The core of the entry is a well-defined **toxicokinetic → toxicodynamic causal chain**: methanol → formaldehyde → **formate** → cytochrome c oxidase inhibition → histotoxic hypoxia + anion-gap metabolic acidosis → optic nerve and basal-ganglia (putaminal) injury.

---

## 1. Disease Information

**Overview.** Methanol (methyl alcohol, wood alcohol, CH₃OH; **CHEBI:17790**) poisoning is an acute toxic syndrome resulting from ingestion, inhalation, or dermal absorption of methanol. Methanol itself is only mildly intoxicating (similar to ethanol), but it is oxidized in the liver to **formaldehyde** and then to **formic acid/formate**, the metabolite responsible for the characteristic delayed high-anion-gap metabolic acidosis, visual toxicity (potentially irreversible blindness), basal-ganglia injury, and death ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/); [Liesivuori & Savolainen 1991, Pharmacol Toxicol](https://physoc.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0773.1991.tb01290.x)). A hallmark clinical feature is a **latent period of ~12–24 hours** between ingestion and symptom onset, corresponding to the time needed to accumulate formate.

**Key identifiers.**
- **MONDO:** MONDO:0017860 (methanol poisoning) — [MalaCards](https://www.malacards.org/card/methanol_poisoning)
- **ICD-10-CM:** T51.1 ("Toxic effect of methanol"), with subcodes for accidental (T51.1X1), intentional self-harm (T51.1X2), assault (T51.1X3), undetermined (T51.1X4) — [ICD10Data](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T51-/)
- **ICD-11:** NE61 (toxic effect of alcohol category); specific code for methanol under harmful effects of substances.
- **Orphanet:** ORPHA:31825
- **UMLS:** C0392621
- **MeSH:** "Methanol" (D000432) with subheading `/poisoning`; "Alcohols" toxicity tree.
- **Toxic agent:** methanol — **CHEBI:17790**; toxic metabolite formate — **CHEBI:15740** (formic acid CHEBI:30751).

**Synonyms:** methyl alcohol poisoning, wood alcohol poisoning, wood spirit poisoning, carbinol poisoning, methanol toxicity, methanol intoxication, methanol overdose.

**Data derivation.** Knowledge is derived primarily from **aggregated disease-level sources** — clinical toxicology practice guidelines, case series, and mass-poisoning outbreak cohorts (Estonia, Norway, Iran, Malaysia, Libya, Tunisia) — supplemented by individual case reports and controlled animal/primate studies of formate toxicity. It is not a registry/EHR-defined chronic disease.

---

## 2. Etiology

**Primary cause (environmental/chemical).** Ingestion (most common), inhalation, or transdermal absorption of methanol-containing products. There is **no genetic causation**; this is a xenobiotic intoxication. Common sources ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)):
- **Adulterated/illicit "bootleg" alcoholic beverages** — the leading cause of mass-casualty outbreaks worldwide, especially where informal spirits are consumed or during alcohol prohibition.
- **Windshield washer/wiper fluid, antifreeze (some formulations), carburetor cleaner, gas-line antifreeze, solvents, paint removers/thinners, shellac, duplicating/copy-machine fluid, canned "chafing/heating fuel" (Sterno), perfumes/colognes, hand sanitizers** (methanol-contaminated hand sanitizers caused FDA recalls and poisonings in 2020).
- Industrial/occupational and inhalational exposure (fuel, laboratory, model-airplane fuel).

**Toxic dose.** The estimated minimum lethal dose is ~**1 g/kg** (≈1–2 mL/kg of pure methanol); as little as **~10 mL** can cause permanent blindness and **~30 mL** can be fatal, though outcome depends heavily on time to treatment and co-ingested ethanol. Blood methanol **>20–25 mg/dL** generally warrants antidotal treatment ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)).

**Risk factors.**
- *Behavioral/social:* alcohol use disorder, consumption of illicitly produced/counterfeit spirits, suicidal self-poisoning, poverty and alcohol prohibition contexts, pandemic-related disruption of legal alcohol supply (large Iranian outbreaks during COVID-19) ([Hassanian-Moghaddam et al., PMC9189800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189800/)).
- *Occupational:* solvent/fuel handling.
- *Nutritional:* **folate deficiency** (malnourished, chronic alcoholics) slows formate clearance and worsens toxicity — a modifiable host factor (see §6).
- *Demographic:* adult males predominate in most outbreak cohorts (median age ~32 in the Iran cohort).

**Protective factors.**
- **Co-ingested ethanol** is strongly protective: ethanol competitively saturates alcohol dehydrogenase (ADH) — for which it has ~10–20× higher affinity than methanol — delaying/blocking formate generation. This is both the mechanistic basis for ethanol antidotal therapy and an explanation for why some heavily co-intoxicated patients present late but with lower formate burden.
- **Adequate folate status** accelerates formate → CO₂ oxidation (see §6).
- No well-established *germline protective allele*; a pharmacogenetic modifier signal exists at **ALDH2** (below).

**Gene–environment interaction (pharmacogenetic modifier).** In acutely methanol-exposed humans, the **ALDH2** minor (C, *ALDH2\*2*-associated) allele was **over-represented among poisoned patients (46%) versus healthy controls (31%)** (odds ratios ~1.9), suggesting reduced-activity ALDH2 modifies susceptibility/outcome, whereas **ADH1B** variation did **not** significantly affect susceptibility ([Zakharov et al. 2018, PMID:29968299](https://pubmed.ncbi.nlm.nih.gov/29968299/)). This is a **susceptibility/modifier** signal (SUSCEPTIBILITY relationship type), not a causal gene.

---

## 3. Phenotypes

Methanol poisoning is a **biphasic** syndrome. Suggested HPO terms and typical frequencies below (frequencies are qualitative estimates from outbreak cohorts; treat frequency bands cautiously per curation policy).

**Early (0–~12 h, "mild inebriation" phase):**
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Inebriation / CNS depression (mild) | HP:0001254 (Lethargy) / HP:0001250 relatives | Often milder than expected for ethanol |
| Nausea and vomiting | HP:0002018 (Nausea), HP:0002013 (Vomiting) | Common; GI irritation |
| Abdominal pain | HP:0002027 (Abdominal pain) | Can mimic pancreatitis |
| Headache, dizziness | HP:0002315 (Headache), HP:0002321 (Vertigo) | |

**Latent period (~12–24 h):** relatively asymptomatic while formate accumulates — a dangerous window where patients appear well.

**Late (~12–72 h, toxic phase):**
| Phenotype | HPO suggestion | Frequency (qualitative) |
|---|---|---|
| **Visual disturbance** — blurred vision, "snowfield"/halo vision, photophobia, decreased acuity, central scotoma | HP:0000504 (Abnormality of vision), HP:0000546 (Retinal degeneration), HP:0000662 (Nyctalopia relatives) | Very frequent; visual sequelae in ~30–40% of survivors ([PMC8731680](https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/)) |
| **Blindness / severe visual loss** | HP:0000618 (Blindness) | Occasional–frequent, often permanent |
| **Optic disc hyperemia / peripapillary edema → optic atrophy** | HP:0000543 (Optic disc pallor), HP:0000648 (Optic atrophy) | Fundoscopic hallmark |
| Fixed/dilated, poorly reactive pupils | HP:0000545 relatives; HP:0000577 (Abnormal pupillary function) | Poor prognostic sign |
| **High-anion-gap metabolic acidosis** | HP:0001942 (Metabolic acidosis) | Cardinal lab abnormality (late) |
| Tachypnea / Kussmaul hyperventilation | HP:0002098 (Respiratory distress), HP:0002091 (Tachypnea) | Respiratory compensation |
| Coma / depressed consciousness | HP:0001259 (Coma) | Severe cases; poor prognosis |
| Seizures | HP:0001250 (Seizure) | Severe cases |
| **Parkinsonism / dystonia (delayed)** | HP:0001300 (Parkinsonism), HP:0001332 (Dystonia) | Sequela of putaminal necrosis |
| Hypotension / circulatory failure | HP:0002615 (Hypotension) | Terminal; strongly predicts death |
| Pancreatitis / elevated amylase | HP:0001733 (Pancreatitis) | Reported complication |

**Phenotype characteristics:** onset **acute/subacute** (adult predominant); severity **variable** (from asymptomatic to fatal), dose- and time-to-treatment-dependent; course **episodic-then-progressive** in untreated disease; neuro-ophthalmic deficits may be **permanent** (progressive optic atrophy) or partially recover.

**Prognostic phenotype associations (from cohorts):** nausea and blurred vision at presentation were paradoxically associated with **better** prognosis (earlier presentation), whereas **absence** of blurred vision and **hypotension** at admission were associated with **death**; delayed admission and elevated anion gap predicted **blindness** ([Prognosis in a developing setting, PMC11097318](https://pmc.ncbi.nlm.nih.gov/articles/PMC11097318/)).

**Quality-of-life impact:** permanent visual loss and Parkinsonian motor sequelae substantially impair independent functioning; long-term follow-up documents new-onset neurologic and visual impairment developing even after apparent recovery ([Paasma et al. 2009, PMID:19327138](https://pubmed.ncbi.nlm.nih.gov/19327138/)).

---

## 4. Genetic / Molecular Information

**Not applicable as a causal genetic disease.** There are no causal genes, pathogenic variants, chromosomal abnormalities, or Mendelian inheritance.

**Relevant enzymes/genes (host metabolism, not disease-causing):**
- **ADH1B / ADH1C / ADH1A** (alcohol dehydrogenase, class I; HGNC:249, HGNC:250, HGNC:251) — catalyze methanol → formaldehyde; the **therapeutic target** of fomepizole/ethanol. **ADH1B** polymorphism does **not** significantly modify susceptibility ([PMID:29968299](https://pubmed.ncbi.nlm.nih.gov/29968299/)).
- **ALDH2** (aldehyde dehydrogenase 2, mitochondrial; HGNC:404) — formaldehyde → formate; the reduced-activity **ALDH2\*2** allele is a candidate **modifier** of outcome ([PMID:29968299](https://pubmed.ncbi.nlm.nih.gov/29968299/)).
- **ALDH1L1** (cytosolic **10-formyltetrahydrofolate dehydrogenase, FDH**; HGNC:3978) — the folate-dependent enzyme oxidizing 10-formyl-THF → THF + CO₂; the **only pathway that clears formate** in humans and the basis of folate/folinic-acid rescue. Adequate folate + functional FDH protect against toxicity ([folate-formate literature](https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854)).
- **CAT** (catalase) and peroxisomal metabolism contribute to methanol/formaldehyde handling, especially in retina (minor pathway).

**Epigenetics / molecular profiling:** No established disease-specific methylation/histone signature; transcriptomic/proteomic/metabolomic profiling is not a routine diagnostic feature. The definitive metabolomic biomarker is **elevated serum formate**.

---

## 5. Environmental Information

- **Environmental/toxic factors:** methanol (CHEBI:17790) is the sole necessary exposure. Sources as in §2 (illicit spirits, washer fluid, solvents, adulterated sanitizer). CTD indexes methanol/formaldehyde/formic acid toxicant–gene interactions.
- **Lifestyle factors:** heavy/illicit alcohol consumption is the dominant behavioral driver; poor nutrition (folate deficiency) worsens outcome.
- **Infectious agents:** none (not applicable).
- **Contextual amplifiers:** alcohol prohibition, informal alcohol economies, and supply-chain disruptions (e.g., COVID-19 pandemic misinformation that alcohol prevents infection) precipitate large outbreaks ([PMC9189800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189800/)).

---

## 6. Mechanism / Pathophysiology

**Central causal chain (toxicokinetic → toxicodynamic):**

1. **Methanol** (CHEBI:17790) is absorbed and distributed in body water; it is only weakly CNS-depressant on its own.
2. **ADH oxidizes methanol → formaldehyde** (rate-limiting; NAD⁺→NADH). *"Alcohol dehydrogenase oxidizes methanol to formaldehyde, and aldehyde dehydrogenase subsequently oxidizes formaldehyde to formic acid"* ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)). GO:0004022 (alcohol dehydrogenase activity), GO:0006069 (ethanol/alcohol oxidation).
3. **ALDH2 oxidizes formaldehyde → formic acid/formate** (very rapid; formaldehyde does not accumulate). GO:0004029 (aldehyde dehydrogenase activity).
4. **Formate accumulates** because human formate clearance (folate-dependent 10-formyl-THF pathway via **ALDH1L1/FDH**) is slow and saturable — the species difference that makes primates far more sensitive than rodents ([PNAS 1985](https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854)).
5. **Formate inhibits mitochondrial cytochrome c oxidase (Complex IV)** → blockade of the electron transport chain → **histotoxic (cytotoxic) hypoxia** and ATP depletion ([Liesivuori & Savolainen 1991](https://physoc.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0773.1991.tb01290.x)). GO:0004129 (cytochrome-c oxidase activity), GO:0006123 (mitochondrial electron transport, cytochrome c to oxygen), GO:0006119 (oxidative phosphorylation).
6. **Downstream amplifiers:**
   - Impaired aerobic respiration → **lactic acidosis** compounds the direct organic (formic) acidosis → **severe high-anion-gap metabolic acidosis** (GO:0006099 TCA/energy metabolism disruption).
   - **Acidemia increases the un-ionized (diffusible) fraction of formic acid**, enhancing cellular entry — a positive-feedback loop worsening tissue penetration and toxicity.
   - ETC blockade → **increased reactive oxygen species** → oxidative stress and **apoptosis** ([Liesivuori & Savolainen 1991](https://physoc.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0773.1991.tb01290.x)). GO:0006915 (apoptotic process), GO:0006979 (response to oxidative stress).
7. **Target-tissue injury:**
   - **Optic nerve / retina:** the **retinal ganglion cells, optic nerve head (prelaminar region), and photoreceptors** are highly vulnerable due to high energy demand; histopathology shows **axonal vacuolation and edema of the oligodendroglia**, optic disc edema → **optic atrophy** ([PMC8731680](https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/)). Suggested CL terms: **CL:0000740 (retinal ganglion cell)**, **CL:0000210 (photoreceptor cell)**, **CL:0000128 (oligodendrocyte)**, **CL:0000031 (neuroblast/neuron relatives)**; UBERON:0000941 (optic nerve), UBERON:0000966 (retina).
   - **Basal ganglia (putamen):** **bilateral putaminal necrosis ± hemorrhage** is the characteristic CNS lesion, attributed to the region's metabolic vulnerability to formate/ischemia; predilection for **putamen (not caudate)** helps distinguish it from CO poisoning ([Sefidbakht et al., MRI spectrum](https://www.sciencedirect.com/science/article/pii/S0378603X16300936); [putamen necrosis, PMID:9561519](https://pubmed.ncbi.nlm.nih.gov/9561519/)). UBERON:0001874 (putamen), UBERON:0002420 (basal ganglion). CL:0000129 (microglia) and neuron loss involved.
8. **Systemic collapse:** progressive acidosis, coma, seizures, hypotension, respiratory/circulatory failure → death.

**Upstream vs downstream:** methanol ingestion and ADH-mediated oxidation are **upstream**; formate accumulation and Complex IV inhibition are the **pivotal node**; metabolic acidosis, ROS/apoptosis, optic-nerve and putaminal injury are **downstream** effectors of clinical morbidity.

**Protein dysfunction:** the injury is not from a mutant protein but from **formate as a reversible inhibitor of cytochrome c oxidase** (heme a₃–CuB binuclear center), analogous to cyanide/azide.

**Metabolic changes:** blocked oxidative phosphorylation, elevated lactate, elevated formate; folate one-carbon pool consumption during formate detoxification.

**Immune involvement:** secondary sterile inflammation/oxidative injury; no primary autoimmune mechanism.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Eye / optic nerve** (UBERON:0000970 eye; UBERON:0000941 optic nerve; UBERON:0000966 retina) — primary and most feared target.
- **Brain, specifically basal ganglia / putamen** (UBERON:0000955 brain; UBERON:0002420 basal ganglia; UBERON:0001874 putamen) — bilateral necrosis ± hemorrhage; subcortical white matter can also be involved.

**Organ level (secondary/systemic):**
- **Metabolic/whole-body:** high-anion-gap metabolic acidosis (blood/plasma).
- **Cardiovascular** (hypotension, circulatory failure), **respiratory** (compensatory hyperventilation, later failure), **gastrointestinal/pancreas** (nausea, abdominal pain, pancreatitis), **kidney** (secondary in severe/shock states), **CNS** (coma, cerebral edema).

**Body systems:** nervous (central + special sensory/visual), cardiovascular, respiratory, digestive, and metabolic/acid–base systems.

**Tissue/cell level:** retinal ganglion cells (**CL:0000740**), photoreceptors (**CL:0000210**), optic-nerve oligodendrocytes/myelin (**CL:0000128**), basal-ganglia neurons; endothelial and glial involvement in hemorrhagic putaminal lesions.

**Subcellular level:** **mitochondria** (GO:0005739) — the primary compartment of injury (Complex IV, GO:0005751 mitochondrial respiratory chain complex IV); peroxisomes (retinal methanol metabolism, GO:0005777).

**Localization/lateralization:** CNS and optic lesions are characteristically **bilateral and symmetric**.

---

## 8. Temporal Development

- **Onset:** **acute**, typically adult. Symptom onset is **delayed 12–24 h** post-ingestion (longer if ethanol co-ingested), producing a deceptive latent period ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)).
- **Progression/stages:** (1) early mild inebriation/GI phase; (2) latent asymptomatic phase; (3) toxic phase (visual, acidotic, CNS); (4) severe/terminal phase (coma, seizures, cardiorespiratory collapse). Progression is **rapid** once acidosis develops.
- **Course pattern:** untreated disease is **progressive**; with early antidote/dialysis it is largely **self-limited** with recovery. Neuro-ophthalmic damage, once established, may be **permanent** (progressive optic atrophy; fixed Parkinsonism from putaminal necrosis).
- **Critical window:** intervention **before or during formate accumulation** (ideally within hours, before significant acidosis/visual loss) is decisive; delayed presentation is the strongest driver of blindness and death. Notably, **new** visual/neurologic deficits can emerge **after discharge** ([Paasma et al. 2009, PMID:19327138](https://pubmed.ncbi.nlm.nih.gov/19327138/)).
- **Duration:** acute illness resolves over days with treatment; sequelae are lifelong.

---

## 9. Inheritance and Population (Epidemiology)

**Epidemiology.** Occurs as **sporadic individual poisonings** and **epidemic mass-casualty outbreaks**. There is no meaningful "prevalence/incidence per 100,000" as a chronic disease; burden is episodic. In the U.S., roughly **~24 methanol-related deaths were reported in 2023** ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)). Large outbreaks include:
- **Estonia 2001:** 111 hospitalized; 86 survived (66 without, 20 with sequelae) ([Paasma et al. 2009, PMID:19327138](https://pubmed.ncbi.nlm.nih.gov/19327138/)).
- **Iran (COVID-19 era, 2020):** hundreds to thousands poisoned across provinces; one linked cohort reported **795 hospitalized, 84 deaths** ([PMC9189800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189800/)).
- **Malaysia (2018) and other outbreaks** report case-fatality up to ~55–61% in some pandemic-era series.

**Case fatality / morbidity (from cohorts):** reported mortality ranges widely (~**8% to >60%**) depending on time-to-care, availability of antidote/dialysis, and outbreak conditions; e.g., ~**23.9%** mortality in one series, with **visual sequelae in ~33.7%** and **neurologic sequelae in ~6.2%** ([prognosis studies, PMC11097318](https://pmc.ncbi.nlm.nih.gov/articles/PMC11097318/)).

**Inheritance:** **Not applicable** (acquired). No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency.

**Demographics:** adult **male predominance**; associated with alcohol use disorder, low socioeconomic status, and regions with informal/illicit alcohol production or prohibition. Median outbreak age ~30s. Geographic distribution reflects socioeconomic and regulatory context (South/Southeast Asia, Middle East, Eastern Europe, Africa hotspots), not genetics.

---

## 10. Diagnostics

**Laboratory (core):**
- **Serum methanol concentration** by gas chromatography — definitive; treat at **>20–25 mg/dL** ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)). LOINC: methanol \[Mass/volume\] in serum/plasma.
- **Elevated osmolar/osmolal gap** early (parent alcohol present; >~10–25 mOsm/kg) that **normalizes** as methanol is metabolized. LOINC: osmolality serum.
- **High anion-gap metabolic acidosis** later (formate). Arterial blood gas: low pH, low bicarbonate. Anion gap and acidosis are **late** and correlate with formate.
- **Serum/plasma formate** — best correlate of toxicity/acidosis but not widely available.
- Ancillary: elevated lactate, elevated amylase/lipase (pancreatitis), electrolytes/renal function.

**Important diagnostic pitfall:** early presenters may have an elevated osmolar gap **without** acidosis; late presenters may have severe acidosis with a **near-normal osmolar gap** (methanol already metabolized). **Serial** BMP/ABG every 2–4 h is advised, with 16–24 h observation ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)).

**Imaging (prognostic, not primary diagnostic):**
- **CT/MRI:** **bilateral putaminal necrosis ± hemorrhage**, subcortical white-matter and optic-nerve changes; putamen-predominant (vs caudate in CO poisoning) plus optic atrophy is nearly pathognomonic ([MRI spectrum, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0378603X16300936); [PMID:9561519](https://pubmed.ncbi.nlm.nih.gov/9561519/)). RadLex: putaminal necrosis/hemorrhage.

**Ophthalmologic:** funduscopy (optic disc hyperemia, peripapillary edema early; optic atrophy late), pupillary reactivity (fixed/dilated = poor prognosis); OCT and visual-evoked potentials for follow-up.

**Genetic testing:** **Not applicable** for diagnosis (no causal gene). Pharmacogenetic ALDH2 genotyping is a research modifier, not clinical.

**Clinical criteria / differential diagnosis:** high-anion-gap metabolic acidosis (MUDPILES) differentials — **ethylene glycol poisoning** (calcium-oxalate crystals, renal failure, no visual loss), diabetic/alcoholic/lactic ketoacidosis, uremia, salicylate, isopropanol (ketosis without acidosis), paraldehyde. Osmolar-gap + anion-gap pattern, visual symptoms, and putaminal imaging distinguish methanol.

**Screening:** no population screening; **public-health outbreak surveillance** of adulterated alcohol is the operative "screening" mode.

---

## 11. Outcome / Prognosis

- **Mortality:** highly variable (~8% to >60%), driven by **time to treatment, severity of acidosis (pH), coma, and antidote/dialysis availability** ([PMC11097318](https://pmc.ncbi.nlm.nih.gov/articles/PMC11097318/); [PMC9189800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189800/)).
- **Key adverse prognostic factors:** low arterial **pH (<7.0–7.2)**, coma or seizures on presentation, **hypotension** (in some cohorts, *all* hypotensive-on-admission patients died), abnormal pupillary reactivity, high formate, delayed presentation ([PMC8731680](https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/); [PMC11097318](https://pmc.ncbi.nlm.nih.gov/articles/PMC11097318/)).
- **Visual morbidity:** **persistent visual sequelae in ~30–40% of survivors**; initial severity predicts long-term visual outcome; some remyelination-related recovery over ~2 years ([PMC8731680](https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/)).
- **Neurologic morbidity:** **Parkinsonism, dystonia, cognitive deficits** from bilateral putaminal necrosis; delayed encephalopathy. New deficits can appear post-discharge ([Paasma et al. 2009, PMID:19327138](https://pubmed.ncbi.nlm.nih.gov/19327138/)).
- **Recovery potential:** excellent if treated **before** significant acidosis/visual loss; established optic atrophy and putaminal necrosis are largely irreversible.
- **Prognostic biomarkers:** admission pH/bicarbonate, formate, methanol level, GCS, and hemodynamic status; risk-prediction nomograms for in-hospital mortality have been developed ([PMC11617918](https://pmc.ncbi.nlm.nih.gov/articles/PMC11617918/)).

---

## 12. Treatment

The strategy is: **(1) block toxic-metabolite formation** (ADH inhibition), **(2) correct acidosis**, **(3) enhance formate elimination** (dialysis + folate), **(4) supportive care.**

**Antidotes — ADH inhibition (MAXO:0000001 therapeutic intervention / MAXO pharmacotherapy):**
- **Fomepizole (4-methylpyrazole)** — **first-line preferred antidote**. Binds ADH with affinity **~8,000× greater than ethanol**, halting methanol→formaldehyde. Dosing: **loading 15 mg/kg IV**, then **10 mg/kg q12h ×4 doses**, then **15 mg/kg q12h** (autoinduction), until methanol <20–25 mg/dL and acidosis resolves; **q4h or post-dialysis dosing during hemodialysis** ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)). Landmark efficacy/safety trial: **Brent et al., NEJM 2001** (Methylpyrazole for Toxic Alcohols Study Group) ([NEJM 2001](https://www.nejm.org/doi/full/10.1056/NEJM200102083440605)). CHEBI: fomepizole (CHEBI:47519). Therapeutic agent binds **ADH1B** (target enzyme).
- **Ethanol** — alternative when fomepizole unavailable; competitive ADH substrate. Target serum ethanol **100–120 mg/dL** (IV 10%: ~8 mL/kg load then 1–2 mL/kg/h; oral 50%: 2 mL/kg load then 0.2–0.4 mL/kg/h); requires frequent level monitoring, causes intoxication/hypoglycemia, harder to titrate ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/)). CHEBI:16236 (ethanol).

**Extracorporeal removal — hemodialysis (MAXO:0000059 hemodialysis / renal replacement):**
- Removes both **methanol and formate** and corrects acidosis; dramatically shortens methanol half-life (from ~**52–70 h with fomepizole alone to ~2.5 h** with dialysis).
- **EXTRIP / AACT indications:** severe metabolic acidosis, coma or seizures, visual deficits, renal impairment, or high methanol concentration (**>~50 mg/dL without fomepizole; >~70 mg/dL with fomepizole**), or evidence of end-organ injury ([EXTRIP/AJKD Core Curriculum](https://www.ajkd.org/article/S0272-6386%2821%2900796-4/fulltext); [AACT Practice Guidelines, Barceloux et al.](https://www.tandfonline.com/doi/abs/10.1081/CLT-120006745)). **Intermittent HD** is generally preferred over continuous RRT in mass-casualty settings ([PMC5519513](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5519513/)).

**Acidosis correction:**
- **IV sodium bicarbonate** for severe metabolic acidosis; raising pH also **traps formate in ionized (less diffusible) form**, reducing tissue penetration, and improves formate renal clearance (MAXO/pharmacotherapy). CHEBI:32139 (bicarbonate).

**Enhancing formate elimination (folate cofactor rescue):**
- **Folinic acid (leucovorin)** — preferred (bypasses dihydrofolate reductase), typically **1 mg/kg (up to ~50 mg) IV q4–6h**; **folic acid** if folinic unavailable. Provides the tetrahydrofolate substrate for **10-formyl-THF dehydrogenase (ALDH1L1)** to oxidize formate → CO₂. Folate deficiency potentiates and folate repletion prevents/reverses methanol toxicity in primates ([PNAS 1985](https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854); [folates & visual sequelae, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1214021X14000660)). CHEBI: folinic acid (CHEBI:15636), folic acid (CHEBI:27470). MAXO: dietary/vitamin supplementation.

**Supportive care (MAXO:0000950 supportive care):** airway/ventilation, IV fluids with **dextrose** and **thiamine** (CHEBI:26948), electrolyte management, seizure control, hemodynamic support.

**Investigational/adjunctive for optic injury:** **high-dose IV methylprednisolone** (e.g., 1 g/day ×3–4 days) reported effective in >80% of early-treated cases; **erythropoietin** neuroprotection and **near-infrared photobiomodulation (670 nm)** show promise in animal/pilot studies ([PMC8731680](https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/)). These are not standard of care.

**Pharmacogenomics:** ALDH2 genotype may modify outcome (research); no genotype-guided dosing exists.

---

## 13. Prevention

- **Primary prevention (population/public-health, the dominant lever):** regulation and quality control of alcoholic beverages; suppression of illicit/counterfeit spirit production; **denaturing/formulation** and product labeling (though methanol denaturing is itself a hazard); consumer warnings on washer fluid, solvents, and hand sanitizer; **removal of methanol-contaminated hand sanitizers** (FDA 2020 actions); rapid **outbreak response** (alerting, stockpiling fomepizole/ethanol, ensuring dialysis capacity) ([StatPearls NBK482121](https://www.ncbi.nlm.nih.gov/books/NBK482121/); WHO methanol-poisoning technical guidance).
- **Secondary prevention:** early recognition and rapid antidote/dialysis in exposed individuals; poison-control triage; screening co-exposed people during known outbreaks (shared source).
- **Tertiary prevention:** aggressive acidosis correction and extracorporeal removal to prevent blindness/CNS injury; ophthalmologic and neurologic follow-up for sequelae.
- **Behavioral interventions:** alcohol-use-disorder treatment; public education (especially countering misinformation, e.g., "drinking alcohol prevents COVID").
- **Environmental interventions:** occupational solvent-exposure controls (ventilation, PPE, exposure limits).
- **Counseling / immunization / prophylactic medication:** genetic counseling and vaccination **not applicable**; no prophylactic drug.

---

## 14. Other Species / Natural Disease

- **Taxonomy / susceptibility:** methanol toxicity is **species-dependent** and driven by **hepatic tetrahydrofolate–dependent formate-oxidation capacity**. **Primates (including humans, NCBITaxon:9606)** clear formate slowly and are highly susceptible; **rodents (mouse NCBITaxon:10090, rat NCBITaxon:10116)** oxidize formate rapidly and are relatively resistant, developing acidosis/ocular injury only under **folate deficiency** or folate-blockade ([PNAS 1985](https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854)).
- **Veterinary/natural disease:** accidental methanol exposure occurs in companion and production animals, but classic optic/putaminal syndrome is a primate phenomenon; ethylene glycol is the far more common toxic-alcohol veterinary poisoning.
- **Comparative biology / evolutionary conservation:** the ADH→ALDH oxidation and the folate one-carbon formate-clearance pathway (ALDH1L1/FDH) are **evolutionarily conserved**; the human phenotype reflects a **quantitative** (slow formate clearance), not qualitative, difference.
- **Zoonotic potential / transmission:** none (chemical toxicity, not transmissible).

---

## 15. Model Organisms

- **Non-human primates (macaque/monkey):** the **gold-standard model** reproducing human formate accumulation, metabolic acidosis, and ocular/optic toxicity; used to establish that **formate (not methanol/formaldehyde)** is the toxic agent and that **folate modulates** toxicity ([PNAS 1985](https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854)). MODEL_ORGANISM evidence.
- **Folate-deficient / folate-blocked rodents and folate-deficient young swine:** engineered to slow formate clearance so rodents recapitulate primate-like formate toxicokinetics; used for formate pharmacokinetics and antidote studies ([formate PK in folate-deficient swine, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0026049508000772)).
- **Rat / rabbit ocular-toxicity models:** for retinal/optic-nerve mitochondrial injury, photoreceptor vulnerability, and photobiomodulation/neuroprotection studies.
- **In vitro / cellular:** isolated mitochondria and cell lines to characterize **formate inhibition of cytochrome c oxidase (Complex IV)** and ROS generation (IN_VITRO evidence) ([Liesivuori & Savolainen 1991](https://physoc.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0773.1991.tb01290.x)).
- **Genetic models:** no knockout "disease model" per se; **Aldh1l1 (FDH)** and folate-pathway perturbations are the closest genetic modifiers used to sensitize animals.
- **Model limitations:** rodents require artificial folate deficiency to mimic human sensitivity; no single model fully captures the human latent period + delayed bilateral putaminal necrosis; primate models are ethically/logistically constrained.
- **Resources:** MGI/RGD (Adh, Aldh2, Aldh1l1 orthologs), Alliance of Genome Resources, Comparative Toxicogenomics Database (methanol/formaldehyde/formic acid).

---

## Consolidated Ontology Term Suggestions

- **Disease:** MONDO:0017860 (methanol poisoning)
- **Chemicals (CHEBI):** methanol 17790; formaldehyde 16842; formic acid 30751 / formate 15740; fomepizole 47519; ethanol 16236; folinic acid 15636; folic acid 27470; sodium bicarbonate 32139; thiamine 26948
- **Phenotypes (HPO):** HP:0001942 (metabolic acidosis), HP:0000504 (abnormal vision), HP:0000618 (blindness), HP:0000648 (optic atrophy), HP:0000543 (optic disc pallor), HP:0001259 (coma), HP:0001250 (seizure), HP:0001300 (parkinsonism), HP:0001332 (dystonia), HP:0002615 (hypotension), HP:0002013 (vomiting), HP:0002027 (abdominal pain), HP:0002091 (tachypnea), HP:0001733 (pancreatitis)
- **Biological processes (GO):** GO:0004022 (alcohol dehydrogenase activity), GO:0004029 (aldehyde dehydrogenase activity), GO:0004129 (cytochrome-c oxidase activity), GO:0006123 (mito electron transport cyt c→O₂), GO:0006119 (oxidative phosphorylation), GO:0006979 (response to oxidative stress), GO:0006915 (apoptotic process), GO:0035999 (tetrahydrofolate interconversion / one-carbon metabolism)
- **Cell types (CL):** CL:0000740 (retinal ganglion cell), CL:0000210 (photoreceptor cell), CL:0000128 (oligodendrocyte), CL:0000129 (microglial cell)
- **Anatomy (UBERON):** UBERON:0000941 (optic nerve), UBERON:0000966 (retina), UBERON:0001874 (putamen), UBERON:0002420 (basal ganglia), UBERON:0000955 (brain), UBERON:0000970 (eye)
- **Subcellular (GO CC):** GO:0005739 (mitochondrion), GO:0005751 (mito respiratory chain complex IV), GO:0005777 (peroxisome)
- **Treatments (MAXO):** pharmacotherapy (fomepizole/ethanol/bicarbonate/folinic acid), MAXO hemodialysis/renal replacement, MAXO:0000950 (supportive care), vitamin/dietary supplementation (folate)
- **Genes (HGNC, host metabolism/modifiers — not causal):** ADH1B (HGNC:249), ADH1C (HGNC:250), ALDH2 (HGNC:404), ALDH1L1 (HGNC:3978), CAT (HGNC:1516)

---

## Key References (PMID/DOI)

1. **StatPearls, "Methanol Toxicity"** — NBK482121 — comprehensive clinical review (dose, metabolism, dosing, prognosis). https://www.ncbi.nlm.nih.gov/books/NBK482121/
2. **Brent J, McMartin K, Phillips S, et al. Fomepizole for the Treatment of Methanol Poisoning. N Engl J Med. 2001;344(6):424–429** (Methylpyrazole for Toxic Alcohols Study Group). https://www.nejm.org/doi/full/10.1056/NEJM200102083440605
3. **Barceloux DG, et al. AACT Practice Guidelines on the Treatment of Methanol Poisoning. J Toxicol Clin Toxicol. 2002;40(4):415–446.** https://www.tandfonline.com/doi/abs/10.1081/CLT-120006745
4. **Liesivuori J, Savolainen H. Methanol and formic acid toxicity: biochemical mechanisms. Pharmacol Toxicol. 1991** — Complex IV inhibition, histotoxic hypoxia, ROS/apoptosis. https://physoc.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0773.1991.tb01290.x
5. **Paasma R, Hovda KE, Jacobsen D. Methanol poisoning and long term sequelae – a six years follow-up after a large methanol outbreak. BMC Clin Pharmacol. 2009;9:5.** PMID:19327138. https://pubmed.ncbi.nlm.nih.gov/19327138/
6. **Zakharov S, et al. ALDH2 polymorphism affects the outcome of methanol poisoning in exposed humans. 2018.** PMID:29968299. https://pubmed.ncbi.nlm.nih.gov/29968299/
7. **Methanol-induced optic neuropathy: a still-present problem. PMC8731680** (PMID:34988610) — mechanism, ~30–40% persistent visual sequelae, adjunctive therapies. https://pmc.ncbi.nlm.nih.gov/articles/PMC8731680/
8. **MRI spectrum in 58 methanol-intoxication patients (long-term visual/neurologic correlation), Eur J Radiol** — putaminal necrosis + optic-nerve enhancement. https://www.sciencedirect.com/science/article/pii/S0378603X16300936
9. **Necrosis and haemorrhage of the putamen in methanol poisoning shown on MRI.** PMID:9561519. https://pubmed.ncbi.nlm.nih.gov/9561519/
10. **Hassanian-Moghaddam H, et al. Methanol poisoning hospital admissions/mortality in Iranian adults during COVID-19. PMC9189800.** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189800/
11. **Prognosis of Methanol Poisoning in a Developing Setting. PMC11097318** — mortality/sequelae, prognostic factors. https://pmc.ncbi.nlm.nih.gov/articles/PMC11097318/
12. **Risk-prediction nomogram for in-hospital mortality in acute methanol poisoning. PMC11617918.** https://pmc.ncbi.nlm.nih.gov/articles/PMC11617918/
13. **EXTRIP / nephrologist role in poisoning (Core Curriculum 2022), Am J Kidney Dis** — hemodialysis thresholds and indications. https://www.ajkd.org/article/S0272-6386%2821%2900796-4/fulltext
14. **Species difference: role of hepatic tetrahydrofolate in methanol/formate toxicity. PNAS 1985;82:3854.** https://www.pnas.org/doi/pdf/10.1073/pnas.82.11.3854
15. **Acute methanol poisonings: folates administration and visual sequelae. Clin Toxicol/relevant.** https://www.sciencedirect.com/science/article/abs/pii/S1214021X14000660

---

**Evidence-source tagging guidance for curation:** most clinical claims are **HUMAN_CLINICAL** (outbreak cohorts, case series, guidelines); the Complex IV/ROS mechanism includes **IN_VITRO** biochemical data; primate/rodent/swine formate-toxicity and folate-modulation studies are **MODEL_ORGANISM**; risk-prediction nomograms are **HUMAN_CLINICAL** (some COMPUTATIONAL modeling on clinical data). Per the dismech DR-verification SOP, **each PMID and its snippet must be independently fetched and substring-verified** (`just fetch-reference PMID:XXXX` → `just validate-references`) before committing — the quotes and figures above are research leads, not pre-validated evidence snippets.

**Notable data gaps / not applicable:** no causal gene, inheritance, penetrance, carrier frequency, or chromosomal abnormality (acquired poisoning); no established disease-specific epigenetic or omics diagnostic signature; formate assays and pharmacogenetic (ALDH2) testing remain research/reference-lab tools rather than routine clinical diagnostics.