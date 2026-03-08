---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:22:14.468379'
end_time: '2026-02-23T23:46:58.083301'
duration_seconds: 1483.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: D-2-Hydroxyglutaric Aciduria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** D-2-Hydroxyglutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **D-2-Hydroxyglutaric Aciduria**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** D-2-Hydroxyglutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **D-2-Hydroxyglutaric Aciduria**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Title: Pathophysiology of D-2-Hydroxyglutaric Aciduria (D2HGA): molecular/cellular mechanisms, progression, and translational landscape

1. Disease definition and current understanding

D-2-hydroxyglutaric aciduria (D-2-HGA; MONDO:MONDO_0010924) is an inborn error of metabolism defined biochemically by excessive accumulation of the D-enantiomer of 2-hydroxyglutarate (D-2-HG) in body fluids, and clinically by early-onset neurodevelopmental impairment with variable severity. A central concept is that D-2-HG is a “supraphysiological” metabolite in this disease, detectable in urine, plasma, and CSF, and used diagnostically as a surrogate for intracellular metabolic derangement. (kranendijk2012progressinunderstanding pages 3-4)

Genetic subtypes (core definitions)

• D-2-HGA type I (D2HGA1): autosomal recessive loss-of-function in D2HGDH, encoding mitochondrial D-2-hydroxyglutarate dehydrogenase (D-2-HGDH), the enzyme that normally oxidizes D-2-HG back to α-ketoglutarate (α-KG; 2-KG). (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• D-2-HGA type II (D2HGA2): typically de novo heterozygous gain-of-function variants in IDH2 (mitochondrial NADP-dependent isocitrate dehydrogenase 2) that confer “neomorphic” activity converting α-KG to D-2-HG, increasing production rather than impairing degradation. (kranendijk2012progressinunderstanding pages 4-5)

A third related disorder, combined D,L-2-hydroxyglutaric aciduria (D,L-2-HGA), is caused by SLC25A1 deficiency (mitochondrial citrate carrier), and is relevant mechanistically because it perturbs mitochondrial citrate/α-KG homeostasis and secondarily elevates 2-HG enantiomers; it is discussed here for differential diagnosis and translational overlap. (kranendijk2012progressinunderstanding pages 1-3, liu2023detectionandanalysis pages 32-34)

2. Core biochemical pathway and dysregulated molecular mechanisms

2.1 Primary metabolic lesion: imbalance of the D-2-HG ⇄ α-KG node

At the biochemical core, D-2-HGA reflects dysregulation of the interconversion between α-KG (2-KG) and D-2-HG.

• Production routes: Hydroxyacid-oxoacid transhydrogenase (HOT) can generate D-2-HG from α-KG in mitochondria as part of coupled redox chemistry, and in D2HGA2 the mutant IDH2 enzyme directly reduces α-KG to D-2-HG using NADPH. (kranendijk2012progressinunderstanding pages 3-4, kranendijk2012progressinunderstanding media b9f822c6)

• Clearance route: D-2-HGDH (encoded by D2HGDH/D2HGDH; commonly referenced as D2HGDH in the clinical literature) catalyzes oxidation of D-2-HG back to α-KG; D2HGA1 is characterized by reduced D-2-HGDH activity in patient cells. (kranendijk2012progressinunderstanding pages 4-5)

Visual pathway evidence: Kranendijk et al. summarize this architecture in a pathway schematic that explicitly shows (i) HOT-mediated D-2-HG production from 2-KG, (ii) D-2-HGDH-mediated reconversion to 2-KG, and (iii) IDH2mut-driven “excessive” D-2-HG production in D2HGA2 (Figure 6). (kranendijk2012progressinunderstanding media b9f822c6)

2.2 Mitochondrial bioenergetic dysfunction and oxidative stress

A convergent mechanistic hypothesis across D2HGA subtypes is that high D-2-HG perturbs mitochondrial energy metabolism and redox state.

• A 2024 synthesis of epilepsy-associated organic acid disorders lists “impaired mitochondrial energy metabolism” and “increased oxidative stress” among key consequences of D-2-HG accumulation in D2HGA1, and connects these changes to neuronal dysfunction and seizures. (shi2024disordersoforganic pages 6-7)

• Earlier mechanistic summaries (still foundational for D2HGA) also report links between D-2-HG exposure and impaired mitochondrial respiratory chain function, reinforcing mitochondria as the dominant cellular compartment in which the primary biochemical disturbance is generated and sensed. (kranendijk2012progressinunderstanding pages 14-15)

2.3 Neurotransmitter/network toxicity: glutamate/GABA imbalance and NMDA receptor-mediated excitotoxicity

Neurologic involvement is central to D2HGA pathophysiology and is frequently framed through excitatory/inhibitory signaling disruption.

• Shi et al. (2024) propose that D-2-HG accumulation can “interfere with GABA metabolism,” and in turn perturb glutamatergic signaling; they also highlight “NMDA receptor activation” and increased glutamate handling as contributors to neurotoxicity and epilepsy phenotypes. (shi2024disordersoforganic pages 6-7)

2.4 Epigenetic and transcriptional dysregulation via α-KG-dependent dioxygenase inhibition (conceptual bridge to oncology)

D-2-HG is structurally similar to α-KG and can competitively inhibit α-KG/Fe(II)-dependent dioxygenases (e.g., histone and DNA demethylases). This creates a mechanistic bridge between D2HGA (a germline metabolic disorder) and IDH-mutant cancers (a somatic oncometabolite phenotype), with shared molecular consequences centered on chromatin state.

• Kranendijk et al. explicitly frame 2-HG as a competitive inhibitor of “alpha-ketoglutarate-dependent dioxygenases,” positioning altered epigenetic enzyme activity as part of the mechanistic landscape. (kranendijk2012progressinunderstanding pages 16-17)

• A 2024 glioma-focused review extends this mechanistic framing to practical biomarker/diagnostic consequences of D-2-HG accumulation and emphasizes that D-2-HG perturbs “epigenetics, metabolism, RNA transcript stability, and DNA damage repair” in the IDH-mutant setting, which is informative for D2HGA because D2HGA2 is itself an IDH2-mutant, D-2-HG-driven disease. (choate2024idhmutationsin pages 15-17)

3. Key molecular players (genes/proteins), chemical entities, affected cell types, and tissues

3.1 Genes/proteins (HGNC-level anchors)

Causal/definitive genes for D2HGA

• D2HGDH/D2HGDH (D-2-hydroxyglutarate dehydrogenase; mitochondrial): causal for D2HGA1 via loss-of-function. (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• IDH2 (isocitrate dehydrogenase 2; mitochondrial): causal for D2HGA2 via gain-of-function, neomorphic D-2-HG production. (kranendijk2012progressinunderstanding pages 4-5)

Related/differential genes

• IDH1 (cytosolic) can be involved in mosaic skeletal phenotypes with D-2-HG excretion (metaphyseal chondromatosis with D-2-HGA), relevant to differential diagnosis and the broader “D-2-HG excess” disease spectrum. (kranendijk2012progressinunderstanding pages 13-14)

• SLC25A1 (mitochondrial citrate carrier): causal for combined D,L-2-HGA; relevant to shared “2-HG” biochemistry and emerging therapeutic trials (phenylbutyrate). (kranendijk2012progressinunderstanding pages 1-3, NCT07125066 chunk 1)

3.2 Chemical entities (CHEBI-level anchors)

• D-2-hydroxyglutarate (D-2-HG): primary accumulating metabolite and pharmacodynamic biomarker. (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

• α-ketoglutarate / 2-oxoglutarate (α-KG; 2-KG): TCA-cycle intermediate and immediate precursor/product at the core reaction node. (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• NADPH: redox cofactor used by IDH2mut to reduce α-KG to D-2-HG (mechanistically explicit in pathway schematic). (kranendijk2012progressinunderstanding media b9f822c6)

3.3 Cell types and anatomical sites

The disease is best understood as a neurometabolic and (for D2HGA2) cardio-metabolic disorder.

• CNS involvement: clinical core includes developmental delay/hypotonia and diverse seizure phenotypes; mechanistically linked to neuronal toxicity/excitability pathways. (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

• Heart involvement: cardiomyopathy is particularly associated with D2HGA2, consistent with systemic exposure to high D-2-HG and high mitochondrial dependence of cardiomyocytes. (kranendijk2012progressinunderstanding pages 3-4)

4. Biological processes and cellular components (GO-oriented annotation candidates)

4.1 GO biological process candidates (mechanism-derived)

The following processes are strongly implicated and are appropriate starting points for knowledge-base GO annotation in D2HGA:

• 2-oxoglutarate metabolic process / TCA cycle-linked metabolism (α-KG is central to the D-2-HG node). (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• D-2-hydroxyglutarate metabolic process / D-2-hydroxyglutarate catabolic process (clearance by D-2-HGDH is the direct lesion in D2HGA1). (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• Mitochondrial energy metabolism / oxidative phosphorylation-linked processes (impaired mitochondrial energy metabolism is repeatedly proposed). (shi2024disordersoforganic pages 6-7)

• Response to oxidative stress / redox homeostasis (increased oxidative stress proposed in D2HGA1). (shi2024disordersoforganic pages 6-7)

• Glutamate metabolic/signaling process and GABA metabolic process (interference with GABA metabolism and glutamate signaling linked to seizures). (shi2024disordersoforganic pages 6-7)

• NMDA receptor signaling pathway / excitotoxicity-associated processes (NMDA receptor activation highlighted as neurotoxic mechanism). (shi2024disordersoforganic pages 6-7)

• Regulation of chromatin modification / DNA and histone demethylation (via inhibition of α-KG-dependent dioxygenases). (kranendijk2012progressinunderstanding pages 16-17, choate2024idhmutationsin pages 15-17)

4.2 GO cellular component candidates

• Mitochondrion / mitochondrial matrix: primary location of IDH2, D-2-HGDH, and HOT-mediated biochemistry driving D-2-HG imbalance. (kranendijk2012progressinunderstanding pages 4-5, kranendijk2012progressinunderstanding media b9f822c6)

• Extracellular biofluids (measurement compartments): urine/plasma/CSF are key compartments used as clinical surrogates for intracellular metabolic imbalance. (kranendijk2012progressinunderstanding pages 3-4, choate2024idhmutationsin pages 15-17)

5. Disease progression model (sequence of events)

A parsimonious mechanistic sequence consistent with the current literature is:

(1) Genetic trigger

• D2HGA1: D2HGDH loss-of-function reduces mitochondrial D-2-HG clearance → accumulation. (shi2024disordersoforganic pages 6-7, kranendijk2012progressinunderstanding pages 4-5)

• D2HGA2: IDH2 gain-of-function increases mitochondrial D-2-HG production from α-KG → accumulation. (kranendijk2012progressinunderstanding pages 4-5)

(2) Metabolic accumulation and mitochondrial stress

Elevated D-2-HG perturbs mitochondrial energy metabolism and oxidative stress state. (shi2024disordersoforganic pages 6-7)

(3) Neural network vulnerability and seizure phenotype

D-2-HG-associated disruption of GABA/glutamate balance and NMDA receptor activation contributes to neuronal dysfunction and epilepsy/seizure phenotypes. (shi2024disordersoforganic pages 6-7)

(4) Systemic organ manifestations (notably D2HGA2)

Cardiomyopathy emerges as a prominent systemic phenotype in D2HGA2 and is highlighted in genotype–phenotype summaries. (kranendijk2012progressinunderstanding pages 3-4)

6. Phenotypic manifestations (HP-oriented candidates) and mechanism linkage

Common clinical phenotypes (with mechanistic linkage)

• Global developmental delay / psychomotor retardation and hypotonia: likely reflect chronic neurodevelopmental vulnerability under mitochondrial/redox and neurotransmitter stress. (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

• Epilepsy/seizures (multiple seizure types): associated with proposed NMDA receptor activation and neurotransmitter dysregulation. (shi2024disordersoforganic pages 6-7)

• Visual cortical disturbance: reported as part of the neurologic phenotype spectrum. (shi2024disordersoforganic pages 6-7)

Subtype-associated phenotypes

• Cardiomyopathy (including dilated cardiomyopathy): emphasized as characteristic/overrepresented in D2HGA2 relative to type I in summarized cohorts. (kranendijk2012progressinunderstanding pages 3-4)

7. Recent developments (2023–2024 emphasis)

7.1 Diagnostics/biomarkers: enantiomer-resolved measurement becomes the key practical bottleneck

Because D- and L-2-HG are enantiomers, routine mass spectrometry without chiral resolution cannot distinguish them, making “chiral” analytical strategies central to D2HGA diagnosis and monitoring.

• A 2023 authoritative methods review states: “there are no standardized instruments and protocols for chiral measurements,” underscoring a major translational gap for deploying D-2-HG as a reproducible biomarker across laboratories. (liu2023detectionandanalysis pages 6-8)

• The same review emphasizes analytic and clinical implementation difficulty: “it remains difficult to achieve cost-effective and reliable analysis of small chiral molecules in clinical procedures, in part owing to their large variety and low concentration.” (liu2023detectionandanalysis pages 1-3)

• The review summarizes practical routes to enantiomer resolution, including chiral derivatization reagents, chiral stationary phases, and multidimensional chiral LC approaches, which have been used to detect large increases in D-2-HG in patient fluids (reported as ~150–200-fold increase in D-2-HG in aciduria samples in the context of chiral analyses). (liu2023detectionandanalysis pages 11-13)

7.2 Quantitative biomarker ranges and assay deployment concepts (cross-fertilization from IDH oncology)

Although derived from oncology, a 2024 review provides quantitative context for D-2-HG as a measurable analyte in tissues and fluids and discusses practical implementation features (stability through freeze–thaw, intraoperative/rapid testing). Such concepts are informative for D2HGA monitoring programs.

• Reported D-2-HG levels in IDH-mutant tumors: median ~1965.8 µM in tumor tissue; reported elevations in CSF (up to ~109 µM) and blood (up to ~10.9 µM) correlate with mutant IDH status, supporting D-2-HG as a surrogate biomarker strategy. (choate2024idhmutationsin pages 15-17)

7.3 Mechanism-focused care guidance for epilepsy phenotypes

A 2024 clinical synthesis of epilepsy in organic acid disorders compiles proposed mechanistic drivers (mitochondrial dysfunction/oxidative stress/NMDA receptor activation) and provides management cautions.

• It highlights a treatment/avoidance framework (supportive antiseizure therapy, carnitine and diet; avoidance of some agents such as valproate in specific mechanistic contexts). (shi2024disordersoforganic pages 6-7)

8. Current applications and real-world implementations

8.1 Diagnostic workflow (current practice patterns)

• First-line biochemical screening: urinary organic acid analysis (commonly GC–MS) to detect 2-HG elevation, followed by chiral speciation to determine D- vs L- configuration, and genetic confirmation (D2HGDH vs IDH2) to stratify D2HGA1 vs D2HGA2. (kranendijk2012progressinunderstanding pages 1-3)

• Prenatal diagnosis feasibility: stable-isotope dilution and other quantitative approaches have been applied for prenatal diagnosis of D- and L-2-hydroxyglutaric acidemias (methodological pathway summarized in the 2023 chiral biomarker review). (liu2023detectionandanalysis pages 30-31)

8.2 Pharmacodynamic monitoring

Across both metabolic and oncologic contexts, D-2-HG itself is a natural pharmacodynamic biomarker.

• In preclinical D2HGA2 models, “2HG” is used as a direct readout of mutant IDH2 activity and inhibitor efficacy (plasma and tissue measurements via LC–MS). (wang2016asmallmolecule pages 2-4)

8.3 Targeted and supportive therapeutics (state of the art)

Supportive care (common practice)

• Seizure management and cardiomyopathy treatment remain largely supportive in clinical practice; examples include antiseizure medications and standard heart-failure agents in cardiomyopathy. (shi2024disordersoforganic pages 6-7)

Targeted therapy for D2HGA2: IDH2 inhibition

• Strong preclinical evidence: In a D2HGA2 knock-in mouse model, the selective IDH2R140Q inhibitor AGI-026 suppressed 2HG production and “rescues cardiomyopathy,” with survival benefit and deterioration upon drug withdrawal. (wang2016asmallmolecule pages 1-2)

• Human repurposing signal: A 2025 case report on dermatologic manifestations in D2HGA2 summarizes that “Enasidenib selectively inhibits mutant IDH2 and has been found to reduce D-2HG levels in D2HGA2 individuals,” and cites a 2023 Nature Medicine report of enasidenib use in two germline IDH2 patients; however, the primary 2023 Nature Medicine article could not be retrieved in full text within this tool run, so the mechanistic/clinical details should be confirmed directly from that source when possible. (roux2025cutaneousmanifestationsin pages 3-3)

9. Clinical trials and research infrastructure (ClinicalTrials.gov)

Although D2HGA-specific interventional trials remain rare, related 2-HGA disorders have emerging trial structures.

• NCT07125066 (ClinicalTrials.gov; posted/active record, start date 2025-07-30; URL: https://clinicaltrials.gov/study/NCT07125066): a single-patient, open-label Phase 1 study of sodium phenylbutyrate (ACER-001/Olpruva) in Combined D,L-2HGA. Primary endpoint is treatment-related adverse events over 2 years; secondary endpoints include urine D,L-2-hydroxyglutaric acid and seizure frequency, among others. (NCT07125066 chunk 1)

• NCT04880356 (ClinicalTrials.gov; start date 2021-03-01; URL: https://clinicaltrials.gov/study/NCT04880356): a recruiting observational longitudinal study of ultra-rare metabolic/degenerative neurologic diseases that includes L-2-hydroxyglutaric aciduria, capturing long-term functional outcomes over ~10 years. (NCT04880356 chunk 1)

10. Relevant statistics and cohort data

Subtype differences in biochemical burden and clinical features

• In a foundational genotype–phenotype synthesis, plasma D-2-HG is reported as markedly elevated and higher in D2HGA2 compared with D2HGA1 (mean ≈5× higher in type II; and D-2-HG 2–8× higher in type II vs type I in reported comparisons), consistent with a production-driven mechanism in D2HGA2. (kranendijk2012progressinunderstanding pages 5-7)

• The same synthesis summarizes cohort sizes and indicates cardiomyopathy as a distinguishing feature of D2HGA2 relative to D2HGA1 in collected cases. (kranendijk2012progressinunderstanding pages 3-4)

11. Expert interpretation and analysis (integrated view)

Mechanistically, D2HGA is best conceptualized as a mitochondrial “metabolite toxicity” disorder centered on pathological D-2-HG excess at the α-KG metabolic node, with downstream effects spanning (i) mitochondrial bioenergetics/redox imbalance, (ii) neurotransmitter-network dysfunction (especially seizure susceptibility), and (iii) epigenetic dysregulation through inhibition of α-KG-dependent dioxygenases. (kranendijk2012progressinunderstanding pages 16-17, shi2024disordersoforganic pages 6-7)

A notable 2023–2024 translational trend is convergence of rare-disease metabolism and oncology: oncology has accelerated development of potent mutant-IDH inhibitors and robust D-2-HG quantification workflows, while the rare disease setting provides a germline model of chronic D-2-HG exposure. This convergence supports rational “reverse repurposing” (e.g., enasidenib for germline IDH2 D2HGA2) and places biomarker standardization (enantioselective D-2-HG assays) as the major practical gating item for clinical implementation in D2HGA. (roux2025cutaneousmanifestationsin pages 3-3, liu2023detectionandanalysis pages 1-3)

12. Knowledge-base–ready structured annotation blocks

12.1 Disease entity

• Disease: D-2-hydroxyglutaric aciduria
• MONDO: MONDO_0010924 (Open Targets disease entity) (kranendijk2012progressinunderstanding pages 4-5)

12.2 Gene/protein annotations (mechanism-linked)

• D2HGDH / D-2-HGDH
  – Role: mitochondrial D-2-HG → α-KG oxidation; deficiency causes D2HGA1 (loss-of-function) (shi2024disordersoforganic pages 6-7)
  – Cellular component: mitochondrion (kranendijk2012progressinunderstanding pages 4-5)

• IDH2
  – Role: mutant IDH2 reduces α-KG → D-2-HG (neomorphic activity) causing D2HGA2 (kranendijk2012progressinunderstanding pages 4-5)
  – Cellular component: mitochondrion; NADPH-dependent reaction (kranendijk2012progressinunderstanding media b9f822c6)

12.3 Chemical entities (biomarkers/mediators)

• D-2-hydroxyglutarate (D-2-HG): primary biomarker/toxic metabolite (kranendijk2012progressinunderstanding pages 3-4)
• α-ketoglutarate / 2-oxoglutarate: pathway node metabolite (shi2024disordersoforganic pages 6-7)

12.4 Phenotypes (HP candidates; non-exhaustive)

• Developmental delay, hypotonia, epilepsy/seizures, visual cortical disturbance; cardiomyopathy (especially D2HGA2). (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

12.5 Anatomical sites (UBERON candidates; non-exhaustive)

• Brain/CNS; heart. (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

12.6 Cell types (CL candidates; illustrative)

• Neurons (seizure/neurotoxicity framing); cardiomyocytes (cardiomyopathy framing). (kranendijk2012progressinunderstanding pages 3-4, shi2024disordersoforganic pages 6-7)

12.7 Biological processes and cellular components (GO candidates; illustrative)

• 2-oxoglutarate metabolic process; mitochondrial energy metabolism; response to oxidative stress; neurotransmitter metabolic process; NMDA receptor signaling; chromatin modification via α-KG-dependent dioxygenases. (kranendijk2012progressinunderstanding pages 16-17, shi2024disordersoforganic pages 6-7)
• Mitochondrion/mitochondrial matrix; extracellular biofluids for biomarker measurement (urine/plasma/CSF). (kranendijk2012progressinunderstanding pages 4-5, choate2024idhmutationsin pages 15-17)

13. Evidence items with PMIDs (available in this run)

This run retrieved PMIDs for D2HGA gene–disease associations via Open Targets (useful for knowledge base linking):

• D2HGDH ↔ D-2-hydroxyglutaric aciduria: PMID 20020533; PMID 33431826; PMID 15609246; PMID 27604308 (as listed in Open Targets evidence rows) (kranendijk2012progressinunderstanding pages 4-5)

• IDH2 ↔ D-2-hydroxyglutaric aciduria: PMID 20847235; PMID 24049096 (as listed in Open Targets evidence rows) (kranendijk2012progressinunderstanding pages 4-5)

Limitations

• The pivotal 2023 Nature Medicine report of enasidenib treatment in germline IDH2 D2HGA2 is referenced by a 2025 case report but was not retrievable in full text in the current tool session; therefore, details beyond the secondary summary should be validated against the primary 2023 publication when accessible. (roux2025cutaneousmanifestationsin pages 3-3)

Key cited sources (with publication dates/URLs)

• Kranendijk M et al. “Progress in understanding 2-hydroxyglutaric acidurias.” Journal of Inherited Metabolic Disease. 2012-03. https://doi.org/10.1007/s10545-012-9462-5 (kranendijk2012progressinunderstanding pages 3-4)

• Shi Y et al. “Disorders of organic acid metabolism and epilepsy.” Acta Epileptologica. 2024-08. https://doi.org/10.1186/s42494-024-00167-2 (shi2024disordersoforganic pages 6-7)

• Liu Y et al. “Detection and analysis of chiral molecules as disease biomarkers.” Nature Reviews Chemistry. 2023-03. https://doi.org/10.1038/s41570-023-00476-z (liu2023detectionandanalysis pages 1-3)

• Choate KA et al. “IDH Mutations in Glioma: Molecular, Cellular, Diagnostic, and Clinical Implications.” Biology. 2024-10. https://doi.org/10.3390/biology13110885 (choate2024idhmutationsin pages 15-17)

• Wang F et al. “A small molecule inhibitor of mutant IDH2 rescues cardiomyopathy in a D-2-hydroxyglutaric aciduria type II mouse model.” Journal of Inherited Metabolic Disease. 2016-07. https://doi.org/10.1007/s10545-016-9960-y (wang2016asmallmolecule pages 1-2)

• ClinicalTrials.gov: NCT07125066 (ACER-001 in combined D,L-2HGA). Start 2025-07-30. https://clinicaltrials.gov/study/NCT07125066 (NCT07125066 chunk 1)

• ClinicalTrials.gov: NCT04880356 (longitudinal observational ultra-rare registry including L-2HGA). Start 2021-03-01. https://clinicaltrials.gov/study/NCT04880356 (NCT04880356 chunk 1)


References

1. (kranendijk2012progressinunderstanding pages 3-4): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

2. (shi2024disordersoforganic pages 6-7): Yuqing Shi, Zihan Wei, Yan Feng, Ya-Jing Gan, Guo-Yan Li, and Yanchun Deng. Disorders of organic acid metabolism and epilepsy. Acta Epileptologica, Aug 2024. URL: https://doi.org/10.1186/s42494-024-00167-2, doi:10.1186/s42494-024-00167-2. This article has 2 citations.

3. (kranendijk2012progressinunderstanding pages 4-5): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

4. (kranendijk2012progressinunderstanding pages 1-3): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

5. (liu2023detectionandanalysis pages 32-34): Yaoran Liu, Zilong Wu, Daniel W. Armstrong, Herman Wolosker, and Yuebing Zheng. Detection and analysis of chiral molecules as disease biomarkers. Nature Reviews Chemistry, 7:355-373, Mar 2023. URL: https://doi.org/10.1038/s41570-023-00476-z, doi:10.1038/s41570-023-00476-z. This article has 200 citations.

6. (kranendijk2012progressinunderstanding media b9f822c6): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

7. (kranendijk2012progressinunderstanding pages 14-15): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

8. (kranendijk2012progressinunderstanding pages 16-17): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

9. (choate2024idhmutationsin pages 15-17): Kristian A. Choate, Evan P. S. Pratt, Matthew J. Jennings, Robert J. Winn, and Paul B. Mann. Idh mutations in glioma: molecular, cellular, diagnostic, and clinical implications. Biology, 13:885, Oct 2024. URL: https://doi.org/10.3390/biology13110885, doi:10.3390/biology13110885. This article has 25 citations.

10. (kranendijk2012progressinunderstanding pages 13-14): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

11. (NCT07125066 chunk 1): Jerry Vockley, MD, PhD. An Individual Patient, Open Label Study to Use ACER-001 to Treat Combined D,L-2 Hydroxyglutaric Aciduria (C-2HGA). Jerry Vockley, MD, PhD. 2025. ClinicalTrials.gov Identifier: NCT07125066

12. (liu2023detectionandanalysis pages 6-8): Yaoran Liu, Zilong Wu, Daniel W. Armstrong, Herman Wolosker, and Yuebing Zheng. Detection and analysis of chiral molecules as disease biomarkers. Nature Reviews Chemistry, 7:355-373, Mar 2023. URL: https://doi.org/10.1038/s41570-023-00476-z, doi:10.1038/s41570-023-00476-z. This article has 200 citations.

13. (liu2023detectionandanalysis pages 1-3): Yaoran Liu, Zilong Wu, Daniel W. Armstrong, Herman Wolosker, and Yuebing Zheng. Detection and analysis of chiral molecules as disease biomarkers. Nature Reviews Chemistry, 7:355-373, Mar 2023. URL: https://doi.org/10.1038/s41570-023-00476-z, doi:10.1038/s41570-023-00476-z. This article has 200 citations.

14. (liu2023detectionandanalysis pages 11-13): Yaoran Liu, Zilong Wu, Daniel W. Armstrong, Herman Wolosker, and Yuebing Zheng. Detection and analysis of chiral molecules as disease biomarkers. Nature Reviews Chemistry, 7:355-373, Mar 2023. URL: https://doi.org/10.1038/s41570-023-00476-z, doi:10.1038/s41570-023-00476-z. This article has 200 citations.

15. (liu2023detectionandanalysis pages 30-31): Yaoran Liu, Zilong Wu, Daniel W. Armstrong, Herman Wolosker, and Yuebing Zheng. Detection and analysis of chiral molecules as disease biomarkers. Nature Reviews Chemistry, 7:355-373, Mar 2023. URL: https://doi.org/10.1038/s41570-023-00476-z, doi:10.1038/s41570-023-00476-z. This article has 200 citations.

16. (wang2016asmallmolecule pages 2-4): Fang Wang, Jeremy Travins, Zhizhong Lin, Yaguang Si, Yue Chen, Josh Powe, Stuart Murray, Dongwei Zhu, Erin Artin, Stefan Gross, Stephanie Santiago, Mya Steadman, Andrew Kernytsky, Kimberly Straley, Chenming Lu, Ana Pop, Eduard A. Struys, Erwin E. W. Jansen, Gajja S. Salomons, Muriel D. David, Cyril Quivoron, Virginie Penard‐Lacronique, Karen S. Regan, Wei Liu, Lenny Dang, Hua Yang, Lee Silverman, Samuel Agresta, Marion Dorsch, Scott Biller, Katharine Yen, Yong Cang, Shin‐San Michael Su, and Shengfang Jin. A small molecule inhibitor of mutant idh2 rescues cardiomyopathy in a d-2-hydroxyglutaric aciduria type ii mouse model. Journal of Inherited Metabolic Disease, 39:807-820, Jul 2016. URL: https://doi.org/10.1007/s10545-016-9960-y, doi:10.1007/s10545-016-9960-y. This article has 20 citations and is from a peer-reviewed journal.

17. (wang2016asmallmolecule pages 1-2): Fang Wang, Jeremy Travins, Zhizhong Lin, Yaguang Si, Yue Chen, Josh Powe, Stuart Murray, Dongwei Zhu, Erin Artin, Stefan Gross, Stephanie Santiago, Mya Steadman, Andrew Kernytsky, Kimberly Straley, Chenming Lu, Ana Pop, Eduard A. Struys, Erwin E. W. Jansen, Gajja S. Salomons, Muriel D. David, Cyril Quivoron, Virginie Penard‐Lacronique, Karen S. Regan, Wei Liu, Lenny Dang, Hua Yang, Lee Silverman, Samuel Agresta, Marion Dorsch, Scott Biller, Katharine Yen, Yong Cang, Shin‐San Michael Su, and Shengfang Jin. A small molecule inhibitor of mutant idh2 rescues cardiomyopathy in a d-2-hydroxyglutaric aciduria type ii mouse model. Journal of Inherited Metabolic Disease, 39:807-820, Jul 2016. URL: https://doi.org/10.1007/s10545-016-9960-y, doi:10.1007/s10545-016-9960-y. This article has 20 citations and is from a peer-reviewed journal.

18. (roux2025cutaneousmanifestationsin pages 3-3): Jennifer Roux, Gabrielle Brody, Brandie Metz, Jingyun Gao, Changrui Xiao, and Richard C. Chang. Cutaneous manifestations in d-2-hydroxyglutaric aciduria type 2 and response to enasidenib therapy. Feb 2025. URL: https://doi.org/10.1016/j.jdcr.2024.10.020, doi:10.1016/j.jdcr.2024.10.020. This article has 3 citations.

19. (NCT04880356 chunk 1):  Longitudinal Study of Ultra-rare Inherited Metabolic and Degenerative Neurological Diseases.. Fondazione I.R.C.C.S. Istituto Neurologico Carlo Besta. 2021. ClinicalTrials.gov Identifier: NCT04880356

20. (kranendijk2012progressinunderstanding pages 5-7): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.
