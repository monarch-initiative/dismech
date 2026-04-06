---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:22:14.264719'
end_time: '2026-02-23T23:42:13.931512'
duration_seconds: 1199.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carnitine Palmitoyltransferase II Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Carnitine Palmitoyltransferase II Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Carnitine Palmitoyltransferase II Deficiency**.
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
- **Disease Name:** Carnitine Palmitoyltransferase II Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Carnitine Palmitoyltransferase II Deficiency**.
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


Title: Pathophysiology of Carnitine Palmitoyltransferase II (CPT2) Deficiency (Genetic long-chain fatty-acid oxidation disorder)

Publication window emphasized: 2023–2024 (with selected foundational/clinical-trial registry evidence).

1. Disease definition and key concepts (current understanding)

Carnitine palmitoyltransferase II (CPT-II) deficiency is an autosomal recessive inborn error of mitochondrial long-chain fatty-acid oxidation (LC-FAO). It is caused by biallelic pathogenic variants in CPT2, which encodes CPT-II, an inner mitochondrial membrane (IMM) enzyme that reconverts long-chain acylcarnitines back to long-chain acyl-CoA for entry into β-oxidation. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9)

Core concept: the “carnitine shuttle.” Long-chain fatty acids cannot directly enter the mitochondrial matrix; they are transported via a three-component system: (i) CPT-I on the outer mitochondrial membrane (OMM) converts long-chain acyl-CoA to long-chain acylcarnitine; (ii) CACT (carnitine-acylcarnitine translocase) exchanges acylcarnitine across the IMM; (iii) CPT-II on the IMM regenerates acyl-CoA inside the mitochondrion to feed β-oxidation. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9)

Clinical phenotypes are typically classified into three forms: lethal neonatal, severe infantile hepatocardiomuscular, and adult/myopathic (exercise- or illness-triggered myalgia/rhabdomyolysis). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, croce2024cptiideficiencya pages 1-9)

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Primary biochemical lesion: impaired mitochondrial LC-FAO

Loss of CPT-II function impairs mitochondrial β-oxidation of long-chain fatty acids, resulting in accumulation of long-chain acylcarnitines (LCACs) and disruption of energy homeostasis, especially during fasting, illness, fever, or prolonged exercise—states when reliance on fatty-acid oxidation increases. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9)

2.2 Temperature sensitivity (thermolability) and crisis triggering

A major genotype-linked mechanism in the common myopathic form is thermolability of certain missense variants. The p.Ser113Leu (S113L) variant can show near-normal baseline activity in recombinant protein but becomes unstable at higher temperatures (40–45 °C) and exhibits greater sensitivity to inhibitory metabolites (including malonyl-CoA), providing a mechanistic rationale for fever/exertion-triggered decompensation. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

2.3 Skeletal muscle cell injury mechanisms: LCAC-mediated calcium dyshomeostasis and structural instability (2024 mechanistic advance)

A 2024 mechanistic study using muscle-specific Cpt2 knockout (loss of mitochondrial long-chain fatty-acid oxidation in muscle) provides a cellular mechanism for muscle weakness and susceptibility to rhabdomyolysis beyond simple ATP deficiency: LCAC accumulation (particularly palmitoyl-carnitine, C16:0) in oxidative muscle fibers directly inhibits sarcoplasmic reticulum (SR) calcium uptake, slowing cytosolic Ca2+ clearance and impairing contractile function. (pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 6-8)

Key mechanistic findings include:

• Preferential vulnerability of oxidative fibers: oxidative soleus muscle accumulates LCACs far more than glycolytic muscle; palmitoyl-carnitine (C16:0) was reported ~23-fold higher in oxidative muscle versus glycolytic muscle in this model. (pereyra2024lossofmitochondria pages 8-10)

• Direct inhibition of SR Ca2+ uptake by LCACs: excess palmitoyl-carnitine (and palmitoyl-CoA) inhibited SR Ca2+ uptake (~70% reduction) without impairing Ca2+ release, supporting SERCA functional inhibition by LCACs. (pereyra2024lossofmitochondria pages 8-10)

• Disruption of excitation–contraction coupling structures: proteomics and ultrastructure showed reductions in SR–T-tubule tethering proteins and disturbance of myofibril organization, consistent with impaired calcium handling and lateral force transmission. (pereyra2024lossofmitochondria pages 6-8, pereyra2024lossofmitochondria pages 2-4)

• Mitochondrial calcium stress and susceptibility to mPTP: CPT2-deficient muscle mitochondria exhibited altered calcium influx/transporter expression, reduced calcium retention capacity, and susceptibility to permeability transition (reversible with cyclosporin A), linking lipid-driven calcium stress to mitochondrial injury pathways. (pereyra2024lossofmitochondria pages 6-8)

Visual evidence: Figures extracted from Pereyra et al. (2024) show LCAC accumulation and impaired SR Ca2+ uptake/handling in CPT2-deficient muscle, and downregulation of SR tethering and calcium-regulating proteins. (pereyra2024lossofmitochondria media 916e81c8, pereyra2024lossofmitochondria media 75a3793d)

2.4 Energy failure and Ca2+ overload as a general rhabdomyolysis mechanism

Clinical and review literature describe ATP depletion during metabolic stress as a driver of calcium dysregulation and myofiber injury. For example, one clinical discussion states cytotoxicity may arise from “an increase in cytoplasmic and mitochondrial ionized calcium as a result of ATP depletion and/or direct damage to the plasma membrane.” (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7)

3. Key molecular players (knowledge-base oriented)

3.1 Genes/proteins (HGNC symbols)

• CPT2 (HGNC:2329): encodes CPT-II; localized to IMM; catalyzes acylcarnitine → acyl-CoA regeneration for β-oxidation. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• CPT1 (family; e.g., CPT1A, CPT1B): OMM enzyme performing acyl-CoA → acylcarnitine conversion. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• SLC25A20 (CACT): IMM transporter exchanging acylcarnitines and carnitine. (risi2025primarylipidmyopathies pages 12-14)

3.2 Chemical entities / metabolites (ChEBI names; representative)

• L-carnitine (free carnitine; C0): substrate/antiporter component of the carnitine shuttle; may be low/variable. (zhang2024clinicalcharacteristicsand pages 1-4)

• Long-chain acylcarnitines used as biomarkers and mechanistic mediators: palmitoylcarnitine (C16:0), oleoylcarnitine (C18:1), and related C12–C18 species. (zhang2024clinicalcharacteristicsand pages 1-4, pereyra2024lossofmitochondria pages 8-10)

• Malonyl-CoA: metabolic regulator that can more strongly inhibit thermolabile variants (mechanistic trigger susceptibility). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

3.3 Cell types (Cell Ontology suggestions; affected cell types)

• Skeletal muscle cells / myofibers (particularly oxidative/type I–enriched): site of exercise-triggered myopathy and rhabdomyolysis; mechanistically linked to LCAC accumulation and SR Ca2+ uptake impairment. (pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 1-2)

• Hepatocytes and cardiomyocytes: prominent in infantile hepatocardiomuscular and neonatal forms, consistent with high FAO dependence in liver/heart. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, croce2024cptiideficiencya pages 1-9)

3.4 Anatomical locations (UBERON suggestions)

• Skeletal muscle (e.g., soleus in mechanistic models): predominant site of myopathic form manifestations. (pereyra2024lossofmitochondria pages 8-10)

• Liver and heart: major organs involved in severe early-onset phenotypes (hypoketotic hypoglycemia, liver dysfunction, cardiomyopathy). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, croce2024cptiideficiencya pages 1-9)

• Kidney/brain involvement can occur in neonatal lethal presentations. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5)

4. Dysregulated pathways and cellular processes (GO-oriented)

The evidence supports disruption of:

• Mitochondrial long-chain fatty-acid β-oxidation / lipid catabolic process (impaired substrate entry and oxidation due to CPT-II dysfunction). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• Acylcarnitine metabolic process and transport across mitochondrial membranes (carnitine shuttle failure). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9)

• Calcium ion homeostasis and sarcoplasmic reticulum calcium ion transport (SR Ca2+ uptake is inhibited by LCACs in muscle-specific Cpt2 deficiency). (pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 6-8)

• Mitochondrial permeability transition / mitochondrial stress susceptibility (reduced calcium retention capacity, mPTP activation sensitivity). (pereyra2024lossofmitochondria pages 6-8)

5. Cellular components (where key processes occur)

• Outer mitochondrial membrane: CPT-I activity (acyl-CoA → acylcarnitine). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• Inner mitochondrial membrane: CACT transport and CPT-II activity (acylcarnitine → acyl-CoA regeneration). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9)

• Mitochondrial matrix: β-oxidation downstream of CPT-II function (implied by shuttle function and FAO coupling). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• Sarcoplasmic reticulum: impaired Ca2+ uptake linked to LCAC accumulation in muscle. (pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria media 916e81c8)

6. Disease progression model (sequence of events)

6.1 Trigger phase

Common triggers include fever/infection, fasting, prolonged/intense exercise, and other metabolic stressors. (lu2024recurrentrhabdomyolysiscaused pages 2-3, croce2024cptiideficiencya pages 1-9)

6.2 Biochemical decompensation

Under stress, impaired CPT-II function reduces LC-FAO flux and promotes accumulation of long-chain acylcarnitines; thermolabile variants (e.g., S113L) further lose activity at elevated temperature. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

6.3 Cellular injury

In skeletal muscle, LCAC accumulation can directly inhibit SR Ca2+ uptake, disrupt excitation–contraction coupling structures, and increase mitochondrial calcium stress/mPTP susceptibility—contributing to contractile dysfunction and myofiber injury. (pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 6-8)

6.4 Clinical manifestations

• Myopathic form: recurrent myalgia, weakness, rhabdomyolysis/myoglobinuria; complications can include acute kidney injury from myoglobinuria. (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7, lu2024recurrentrhabdomyolysiscaused pages 2-3)

• Infantile/neonatal forms: hypoketotic hypoglycemia, liver dysfunction, cardiomyopathy/arrhythmia, multi-organ failure, with high lethality in the neonatal form. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, croce2024cptiideficiencya pages 1-9)

7. Phenotypic manifestations (HP-oriented, representative)

Evidence-supported phenotype groupings:

• Rhabdomyolysis / myoglobinuria (exercise/illness-triggered). (lu2024recurrentrhabdomyolysiscaused pages 2-3, castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7)

• Cardiomyopathy and arrhythmias (especially early-onset forms; also reported complications). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7)

• Hypoketotic hypoglycemia and liver dysfunction (infantile/neonatal forms). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5, croce2024cptiideficiencya pages 1-9)

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 Mechanistic advance: LCAC → SERCA inhibition → Ca2+ dyshomeostasis

The 2024 Molecular Metabolism study provides strong mechanistic evidence linking defective mitochondrial LC-FAO to calcium-handling dysfunction via LCACs and demonstrates that muscle weakness can occur despite relatively preserved mitochondrial ATP production capacity, shifting emphasis from “energy failure alone” to “lipid-mediated excitation–contraction coupling disruption.” (pereyra2024lossofmitochondria pages 2-4, pereyra2024lossofmitochondria pages 8-10)

8.2 Diagnostic insight: normal acylcarnitine profiles between crises

A 2024 case report and literature review highlights that CPT2 deficiency can present with recurrent rhabdomyolysis yet have repeatedly normal acylcarnitine profiles outside acute episodes, with definitive diagnosis made by genome sequencing; the authors emphasize that biochemical abnormalities may only be detectable during active rhabdomyolysis. (lu2024recurrentrhabdomyolysiscaused pages 1-2, lu2024recurrentrhabdomyolysiscaused pages 2-3)

8.3 Updated case-count synthesis (2024)

A 2024 PubMed-based literature synthesis identified 245 documented CPT2 cases, distributed as 21 lethal neonatal, 32 severe infantile hepatocardiomuscular, and 192 myopathic. (lu2024recurrentrhabdomyolysiscaused pages 2-3)

9. Current applications and real-world implementations

9.1 Newborn screening and biochemical diagnosis

Tandem mass spectrometry is used in newborn screening and diagnostic workups, with typical CPT2 biochemical signatures including elevation of long-chain acylcarnitines (C12–C18), particularly C16 and C18:1, often with normal or low free carnitine (C0). (zhang2024clinicalcharacteristicsand pages 1-4)

Important implementation limitation: CPT2 deficiency may yield normal profiles when patients are not metabolically stressed; thus sampling during an acute event and/or genetic testing is critical when clinical suspicion persists. (lu2024recurrentrhabdomyolysiscaused pages 1-2, ambrose2025energymetabolismdefects pages 54-58)

Direct quote (diagnostic timing): “the abnormal acylcarnitine profile is more significant if individuals are metabolically stressed,” supporting the practice of collecting biochemical samples during/soon after crises. (ambrose2025energymetabolismdefects pages 54-58)

9.2 Patient management (expert consensus themes reflected in recent reviews/case discussions)

Common management principles described in 2023–2024 sources include avoidance of fasting and other triggers, and dietary strategies (high-carbohydrate/low-fat approaches, MCT supplementation), with carnitine supplementation used in some settings and additional carbohydrate during illness/exercise. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, croce2024cptiideficiencya pages 1-9, lu2024recurrentrhabdomyolysiscaused pages 1-2)

10. Therapeutic landscape and clinical trials (applications in practice)

10.1 Triheptanoin (UX007)

Triheptanoin is an odd-chain triglyceride intended to provide anaplerotic substrate (propionyl-CoA generation) to support energy metabolism in LC-FAOD. A Phase 2 open-label Ultragenyx study (NCT01886378) included CPT II deficiency among LC-FAOD diagnoses; dosing was titrated to ~25–35% of total calories, with a primary objective to evaluate impact on acute clinical pathophysiology after 24 weeks and exercise-tolerance-related outcomes. (NCT01886378 chunk 1)

An earlier Phase 2 randomized, double-masked trial (NCT01379625; completed; n=32; ages ~7–40) compared triheptanoin vs standard MCT oil at ~20% of caloric needs for 4 months, with outcomes including total energy expenditure and resting ejection fraction. (NCT01379625 chunk 1)

10.2 Bezafibrate

A Phase 2 randomized, quadruple-masked crossover trial (NCT00983788; completed) evaluated bezafibrate in adults with CPT II or VLCAD deficiency, using fatty-acid oxidation during moderate exercise as a primary outcome and safety monitoring including CK and liver enzymes. (NCT00983788 chunk 3)

The registry record also summarizes prior translational evidence: a pilot open study of six adult CPT II patients treated with bezafibrate 400 mg daily for 6 months reported improved muscular symptoms in 5/6 and induction of LCFA oxidation in isolated muscle mitochondria. (NCT00983788 chunk 1)

11. Epidemiology and statistics (recently cited)

• Literature-compiled case counts: 245 reported CPT2 cases (21 neonatal lethal; 32 severe infantile; 192 myopathic) in a 2024 literature review. (lu2024recurrentrhabdomyolysiscaused pages 2-3)

• Prevalence estimate: one narrative review cites ~1–9 per 100,000 (note: this is a review-derived estimate and may vary by population and ascertainment). (risi2025primarylipidmyopathies pages 12-14)

12. Knowledge-base entry elements (structured annotations)

12.1 Pathophysiology summary (narrative)

CPT2 deficiency results from loss-of-function or destabilizing variants in CPT2 encoding the IMM enzyme CPT-II, a required component of the carnitine shuttle that enables mitochondrial import and oxidation of long-chain fatty acids. Under metabolic stress (fasting, fever/infection, prolonged exercise), impaired CPT-II activity reduces LC-FAO and promotes long-chain acylcarnitine accumulation. Thermolabile variants such as p.Ser113Leu can exacerbate crisis susceptibility by losing activity at elevated temperature and showing increased sensitivity to inhibition. In skeletal muscle, recent mechanistic evidence demonstrates that LCAC accumulation—especially palmitoyl-carnitine—can directly inhibit SR calcium uptake, disrupt excitation–contraction coupling protein networks, and increase mitochondrial calcium stress and mPTP susceptibility, leading to contractile dysfunction, myofiber injury, and rhabdomyolysis. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 6-8)

12.2 Gene/protein annotations (examples)

• CPT2 (HGNC:2329): mitochondrial inner membrane CPT-II; molecular function: acyltransferase activity within carnitine shuttle enabling LC-FAO; disease mechanism includes thermolability in common myopathic variants. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• SLC25A20 (CACT): inner mitochondrial membrane acylcarnitine translocase supporting carnitine shuttle. (risi2025primarylipidmyopathies pages 12-14)

12.3 Candidate GO terms (process-focused; suggested mapping)

• Mitochondrial fatty acid β-oxidation; long-chain fatty acid metabolic process; acylcarnitine metabolic process; carnitine transmembrane transport; calcium ion homeostasis; sarcoplasmic reticulum calcium ion transport; mitochondrial permeability transition pore complex opening (stress response). Evidence basis: mechanistic and review evidence as above. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, pereyra2024lossofmitochondria pages 8-10, pereyra2024lossofmitochondria pages 6-8)

12.4 Candidate cellular components (suggested mapping)

• Mitochondrial inner membrane (CPT-II, CACT), outer mitochondrial membrane (CPT-I), mitochondrial matrix (β-oxidation enzymes downstream), sarcoplasmic reticulum (calcium uptake machinery). (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7, pereyra2024lossofmitochondria pages 8-10)

12.5 Evidence items and PMIDs

PMID availability was not consistently provided in the retrieved full-text snippets for all sources in this run. Where PMIDs are required for mechanistic claims, the most relevant primary mechanistic evidence here is the 2024 Molecular Metabolism study (Pereyra et al., 2024; DOI: 10.1016/j.molmet.2024.102015) and the mechanistic variant thermolability synthesis (Yao et al., 2023; DOI: 10.3748/wjg.v29.i12.1765). (pereyra2024lossofmitochondria pages 8-10, yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

(If strict PMID-only evidence is mandatory for downstream ingestion, additional PubMed-specific retrieval would be needed to map each cited DOI to PMID and to add classic enzymology/genotype papers.)

Key 2023–2024 sources (with URLs and dates)

• Yao M et al. “Mitochondrial carnitine palmitoyltransferase-II dysfunction…” World Journal of Gastroenterology. March 2023. https://doi.org/10.3748/wjg.v29.i12.1765 (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7)

• Castillo E et al. “Myopathic Carnitine Palmitoyltransferase II (CPT II) Deficiency…” Cureus. October 2023. https://doi.org/10.7759/cureus.46595 (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7)

• Zhang Y et al. “Clinical characteristics and genetic analysis of six children with carnitine palmitoyltransferase 2 deficiency.” April 2024. https://doi.org/10.3724/zdxbyxb-2023-0611 (zhang2024clinicalcharacteristicsand pages 1-4)

• Lu C-H et al. “Recurrent rhabdomyolysis caused by… CPT-2 deficiency but complete normal acylcarnitine profile…” December 2024. https://doi.org/10.1016/j.ymgmr.2024.101151 (lu2024recurrentrhabdomyolysiscaused pages 1-2)

• Pereyra AS et al. “Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility…” November 2024. https://doi.org/10.1016/j.molmet.2024.102015 (pereyra2024lossofmitochondria pages 8-10)

• ClinicalTrials.gov: Triheptanoin Phase 2 (NCT01886378) https://clinicaltrials.gov/study/NCT01886378 (NCT01886378 chunk 1); Triheptanoin randomized Phase 2 (NCT01379625) https://clinicaltrials.gov/study/NCT01379625 (NCT01379625 chunk 1); Bezafibrate crossover Phase 2 (NCT00983788) https://clinicaltrials.gov/study/NCT00983788 (NCT00983788 chunk 3)

MONDO ID

A MONDO identifier for CPT-II deficiency was not retrieved within the tool context used in this run; therefore it is not asserted here.


References

1. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 5-7): Min Yao, Ping Zhou, Yan-Yan Qin, Li Wang, and Dengbing Yao. Mitochondrial carnitine palmitoyltransferase-ii dysfunction: a possible novel mechanism for nonalcoholic fatty liver disease in hepatocarcinogenesis. World Journal of Gastroenterology, 29:1765-1778, Mar 2023. URL: https://doi.org/10.3748/wjg.v29.i12.1765, doi:10.3748/wjg.v29.i12.1765. This article has 13 citations.

2. (croce2024cptiideficiencya pages 1-9): MMC Croce. Cptii deficiency: a therapeutical approach. Unknown journal, 2024.

3. (yao2023mitochondrialcarnitinepalmitoyltransferaseii pages 4-5): Min Yao, Ping Zhou, Yan-Yan Qin, Li Wang, and Dengbing Yao. Mitochondrial carnitine palmitoyltransferase-ii dysfunction: a possible novel mechanism for nonalcoholic fatty liver disease in hepatocarcinogenesis. World Journal of Gastroenterology, 29:1765-1778, Mar 2023. URL: https://doi.org/10.3748/wjg.v29.i12.1765, doi:10.3748/wjg.v29.i12.1765. This article has 13 citations.

4. (pereyra2024lossofmitochondria pages 8-10): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (pereyra2024lossofmitochondria pages 6-8): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (pereyra2024lossofmitochondria pages 2-4): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (pereyra2024lossofmitochondria media 916e81c8): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (pereyra2024lossofmitochondria media 75a3793d): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (castillo2023myopathiccarnitinepalmitoyltransferase pages 5-7): Efrain Castillo, Debbie Medina, and Nick Schoenmann. Myopathic carnitine palmitoyltransferase ii (cpt ii) deficiency: a rare cause of acute kidney injury and cardiomyopathy. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.46595, doi:10.7759/cureus.46595. This article has 6 citations.

10. (risi2025primarylipidmyopathies pages 12-14): B RISI, F CARIA, L POLI, and A PADOVANI. Primary lipid myopathies: a narrative review. Unknown journal, 2025.

11. (zhang2024clinicalcharacteristicsand pages 1-4): Yan Zhang, W. Qiu, Huiwen Zhang, Ting Chen, Feng Xu, Suhong Yang, Jianmei Zhang, Xuefan Gu, and Lianshu Han. Clinical characteristics and genetic analysis of six children with carnitine palmitoyltransferase 2 deficiency. Journal of Zhejiang University (Medical Sciences), 53:207-212, Apr 2024. URL: https://doi.org/10.3724/zdxbyxb-2023-0611, doi:10.3724/zdxbyxb-2023-0611. This article has 0 citations.

12. (pereyra2024lossofmitochondria pages 1-2): Andrea S. Pereyra, Regina F. Fernandez, Adam Amorese, Jasmine N. Castro, Chien-Te Lin, Espen E. Spangenburg, and Jessica M. Ellis. Loss of mitochondria long-chain fatty acid oxidation impairs skeletal muscle contractility by disrupting myofibril structure and calcium homeostasis. Nov 2024. URL: https://doi.org/10.1016/j.molmet.2024.102015, doi:10.1016/j.molmet.2024.102015. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (lu2024recurrentrhabdomyolysiscaused pages 2-3): Chih-Hsuan Lu, Chia-Feng Yang, Yun-Ru Chen, Yann-Jang Chen, Yung-Hsiu Lu, and Dau-Ming Niu. Recurrent rhabdomyolysis caused by palmitoyltransferase ii (cpt-2) deficiency but complete normal acylcarnitine profile: a patient presentation and review of the literature. Molecular Genetics and Metabolism Reports, 41:101151, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101151, doi:10.1016/j.ymgmr.2024.101151. This article has 4 citations.

14. (lu2024recurrentrhabdomyolysiscaused pages 1-2): Chih-Hsuan Lu, Chia-Feng Yang, Yun-Ru Chen, Yann-Jang Chen, Yung-Hsiu Lu, and Dau-Ming Niu. Recurrent rhabdomyolysis caused by palmitoyltransferase ii (cpt-2) deficiency but complete normal acylcarnitine profile: a patient presentation and review of the literature. Molecular Genetics and Metabolism Reports, 41:101151, Dec 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101151, doi:10.1016/j.ymgmr.2024.101151. This article has 4 citations.

15. (ambrose2025energymetabolismdefects pages 54-58): A Ambrose. Energy metabolism defects in childhood and adulthood. Unknown journal, 2025.

16. (NCT01886378 chunk 1):  A Study of UX007 (Triheptanoin) in Participants With Long-Chain Fatty Acid Oxidation Disorders (LC-FAOD). Ultragenyx Pharmaceutical Inc. 2014. ClinicalTrials.gov Identifier: NCT01886378

17. (NCT01379625 chunk 1): Melanie B Gillingham. Study of Triheptanoin for Treatment of Long-Chain Fatty Acid Oxidation Disorder. Oregon Health and Science University. 2011. ClinicalTrials.gov Identifier: NCT01379625

18. (NCT00983788 chunk 3): Mette Cathrine Oerngreen. Effect of Bezafibrate on Muscle Metabolism in Patients With Fatty Acid Oxidation Defects. Rigshospitalet, Denmark. 2009. ClinicalTrials.gov Identifier: NCT00983788

19. (NCT00983788 chunk 1): Mette Cathrine Oerngreen. Effect of Bezafibrate on Muscle Metabolism in Patients With Fatty Acid Oxidation Defects. Rigshospitalet, Denmark. 2009. ClinicalTrials.gov Identifier: NCT00983788
