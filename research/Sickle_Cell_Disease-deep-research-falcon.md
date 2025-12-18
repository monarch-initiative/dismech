---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:59:05.469692'
end_time: '2025-12-18T00:11:07.717394'
duration_seconds: 722.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sickle Cell Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Sickle Cell Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sickle Cell Disease**.
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
- **Disease Name:** Sickle Cell Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sickle Cell Disease**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Sickle Cell Disease (SCD)
- MONDO ID: MONDO:0011382
- Category: Mendelian

Pathophysiology description (current understanding)
SCD arises from a single missense variant in HBB (β6 Glu→Val) that promotes deoxygenated hemoglobin S (HbS) polymerization, driving red cell sickling, membrane injury, ion dysregulation, dehydration, and premature hemolysis. Intravascular hemolysis releases cell-free hemoglobin, heme, and erythrocyte arginase-1, which together mediate nitric oxide (NO) depletion, oxidative stress, endothelial activation, sterile inflammation, and a thromboinflammatory vasculopathy characterized by multicellular adhesion and vaso-occlusion. Hemolysis-derived heme triggers endothelial TLR4 signaling that rapidly releases Weibel–Palade body cargo (P-selectin and von Willebrand factor [VWF]), enhancing leukocyte rolling/adhesion and microvascular stasis. Heme and oxidized hemoglobin promote neutrophil extracellular traps (NETs), while emerging data implicate mast cell extracellular traps (MCETs) in neural and vascular injury that can exacerbate pain. These axes—HbS polymerization/sickling, hemolysis/NO depletion, adhesion/vaso-occlusion, and thromboinflammation—interact to cause acute crises (pain, acute chest) and chronic organ damage (pulmonary hypertension, renal and cerebrovascular disease). Foundational and recent studies support these mechanisms and identify therapeutic entry points, including HbF induction, heme scavenging, selectin blockade, metabolic modulation of red cells (PK activators), and gene editing that reactivates HbF. (ilboudo2022multiomicsapproachesto pages 20-24, belcher2014hemetriggerstlr4 pages 6-9, chen2014hemeinducedneutrophilextracellular pages 1-2, guarda2017hememediatedcellactivation pages 1-5)

1) Core Pathophysiology
- Primary mechanisms
  - HbS polymerization and red-cell dehydration: Deoxygenated HbS forms long polymers that stiffen RBCs and promote membrane damage, repeated sickling, reactive oxygen species, disordered cation flux, activation of Gardos (KCNN4) and K–Cl cotransport, and RBC dehydration/density—thus increasing sickling propensity and hemolysis. (ilboudo2022multiomicsapproachesto pages 20-24)
  - Hemolysis, NO scavenging, arginase axis: Cell-free hemoglobin “reacts with and scavenges NO,” while erythrocyte arginase depletes L‑arginine, reducing NO synthesis; lower arginine:ornithine and arginine:(ornithine+citrulline) ratios correlate with pulmonary hypertension (PH) severity and mortality in adults with SCD. (morris2005dysregulatedargininemetabolism pages 7-8, kato2008evolutionofnovel pages 2-4, morris2005dysregulatedargininemetabolism pages 1-2, morris2005dysregulatedargininemetabolism pages 12-18, morris2005dysregulatedargininemetabolism pages 5-7)
  - Heme–TLR4–WPB pathway and adhesion: Free heme activates endothelial TLR4, inducing oxidative signaling and Weibel–Palade body degranulation (surface P‑selectin and VWF strings) within minutes, which promotes leukocyte rolling/adhesion and vaso‑occlusion; TLR4 inhibition (TAK‑242) and hemopexin/haptoglobin mitigate heme‑induced stasis in SCD mice. (belcher2014hemetriggerstlr4 pages 6-9)
  - Thromboinflammation: Heme/oxidized Hb and inflammatory stimuli trigger NET formation; “hemolysis releases cell free hemoglobin… [that] scavenges NO” and “oxidized hemoglobin and free heme can trigger a sterile inflammatory reaction involving TLR4 activation, and stimulates neutrophils to release NETs,” which contribute to acute lung injury and vaso‑occlusion. (chen2014hemeinducedneutrophilextracellular pages 1-2)
  - Selectin-mediated multicellular adhesion: Endothelial/platelet P‑ and E‑selectins and leukocyte PSGL‑1 drive tethering/rolling and firm adhesion of RBCs, leukocytes, and platelets, amplifying microvascular occlusion and ischemia-reperfusion injury. (escopy2024targetingthepselectinpsgl1 pages 10-12, belcher2014hemetriggerstlr4 pages 6-9)
  - MCETs and pain: In SCD murine models, PAD4‑dependent mast cell extracellular traps directly injure vasculature and nerves and promote vaso‑occlusion and hyperalgesia; PAD4 inhibition reduces vascular stasis and pain behaviors. (mahadevia2025areviewon pages 6-8)

- Dysregulated molecular pathways
  - NO signaling: Depletion by hemoglobin dioxygenation chemistry and substrate limitation via arginase; downstream sGC–cGMP vasodilatory signaling is impaired. (kato2008evolutionofnovel pages 2-4, morris2005dysregulatedargininemetabolism pages 7-8)
  - Innate immune sensing: Heme–TLR4–NF‑κB and oxidative pathways (PKC, NOX) activate endothelium and leukocytes; NETosis/MCETs propagate thromboinflammation. (belcher2014hemetriggerstlr4 pages 6-9, chen2014hemeinducedneutrophilextracellular pages 1-2, mahadevia2025areviewon pages 6-8)
  - Adhesion pathways: Selectins (P/E), PSGL‑1, VWF, integrins (ICAM/VCAM interactions) facilitate vaso‑occlusion. (escopy2024targetingthepselectinpsgl1 pages 10-12, belcher2014hemetriggerstlr4 pages 6-9)

- Affected cellular processes
  - RBC biomechanics and membrane transport (2,3‑DPG/ATP balance, Ca2+ influx, Gardos/K–Cl), endothelial activation/WPB exocytosis, leukocyte/platelet adhesion and NETosis/MCETosis, heme/iron handling and oxidative stress. (ilboudo2022multiomicsapproachesto pages 20-24, belcher2014hemetriggerstlr4 pages 6-9, chen2014hemeinducedneutrophilextracellular pages 1-2, escopy2024targetingthepselectinpsgl1 pages 10-12)

2) Key Molecular Players
- Genes/Proteins (HGNC symbol)
  - HBB (β-globin; mutant HbS) – causal. (ilboudo2022multiomicsapproachesto pages 20-24)
  - BCL11A (erythroid enhancer target for HbF reactivation by gene editing). (frangoul2024exagamglogeneautotemcelfor pages 4-6)
  - SELP (P‑selectin), SELE (E‑selectin), SELPLG (PSGL‑1) – adhesion. (escopy2024targetingthepselectinpsgl1 pages 10-12)
  - VWF; WPB cargo. (belcher2014hemetriggerstlr4 pages 6-9)
  - TLR4 – heme sensing on endothelium. (belcher2014hemetriggerstlr4 pages 6-9)
  - ARG1 – arginase‑1; NOS isoforms (NOS3/eNOS). (morris2005dysregulatedargininemetabolism pages 7-8, morris2005dysregulatedargininemetabolism pages 5-7)
  - NOX components, PKC; NF‑κB – signaling. (belcher2014hemetriggerstlr4 pages 6-9)
  - PAD4 (PADI4) – trap formation (MCET/NET). (mahadevia2025areviewon pages 6-8)

- Chemical entities (CHEBI where applicable)
  - Hemoglobin/heme (CHEBI:16136/30413), NO (CHEBI:16480), L‑arginine (CHEBI:29016), 2,3‑diphosphoglycerate (CHEBI:16001), ATP (CHEBI:15422). (chen2014hemeinducedneutrophilextracellular pages 1-2, kato2008evolutionofnovel pages 2-4, rubio2024thecurrentrole pages 9-11)

- Cell types (CL terms)
  - Erythrocyte (CL:0000232), endothelial cell (CL:0000115), neutrophil (CL:0000775), mast cell (CL:0000097), platelet (CL:0000233), monocyte (CL:0000576). (chen2014hemeinducedneutrophilextracellular pages 1-2, belcher2014hemetriggerstlr4 pages 6-9, mahadevia2025areviewon pages 6-8)

- Anatomical locations (UBERON)
  - Microvasculature (UBERON:0001981), lung (UBERON:0002048), liver (UBERON:0002107), kidney (UBERON:0002113), spleen (UBERON:0002106), urinary bladder (UBERON:0001255). (chen2014hemeinducedneutrophilextracellular pages 1-2, belcher2014hemetriggerstlr4 pages 6-9, xue2024therapeuticsforsickle pages 1-2)

3) Biological Processes (candidate GO annotations; evidence-based)
- HbS polymerization and red-cell dehydration: “hemoglobin polymerization” (GO:0030492), “regulation of cation transport” (GO:0051924), “potassium ion transmembrane transport” (GO:0071805), “erythrocyte homeostasis” (GO:0034101). (ilboudo2022multiomicsapproachesto pages 20-24)
- Endothelial activation/WPB exocytosis: “exocytosis” (GO:0006887), “endothelial cell activation” (GO:0042118), “response to heme” (GO:1903409). (belcher2014hemetriggerstlr4 pages 6-9)
- Leukocyte/platelet adhesion and rolling: “leukocyte tethering or rolling” (GO:0050901), “cell adhesion mediated by integrin” (GO:0033627), “platelet activation” (GO:0030168). (escopy2024targetingthepselectinpsgl1 pages 10-12)
- Hemolysis and NO pathway: “nitric oxide metabolic process” (GO:0046209), “arginine metabolic process” (GO:0006525), “regulation of blood pressure” (GO:0008217). (kato2008evolutionofnovel pages 2-4, morris2005dysregulatedargininemetabolism pages 7-8)
- NET/MCET formation: “neutrophil extracellular trap formation” (GO:0036342), “chromatin decondensation” (GO:0031490). (chen2014hemeinducedneutrophilextracellular pages 1-2, mahadevia2025areviewon pages 6-8)

4) Cellular Components
- Key loci of action: erythrocyte cytosol (HbS polymer), plasma (cell‑free Hb, heme), endothelial surface (P‑selectin/VWF strings), Weibel–Palade body, extracellular space (NETs/MCETs), caveolae/raft TLR4 signaling domains. (belcher2014hemetriggerstlr4 pages 6-9, chen2014hemeinducedneutrophilextracellular pages 1-2)

5) Disease Progression
- Sequence of events
  1) Deoxygenation → HbS polymerization → sickling, membrane injury, Ca2+ influx → Gardos/K–Cl activation → RBC dehydration/density. (ilboudo2022multiomicsapproachesto pages 20-24)
  2) Vaso‑occlusion axis: Endothelial activation (heme–TLR4) and selectin/VWF upregulation → leukocyte/platelet/RBC adhesion → microvascular stasis and ischemia-reperfusion injury. (belcher2014hemetriggerstlr4 pages 6-9, escopy2024targetingthepselectinpsgl1 pages 10-12)
  3) Hemolysis axis: Intravascular hemolysis releases cell‑free Hb/heme/arginase → NO scavenging + L‑arginine depletion → vasoconstriction, endothelial dysfunction, and PH risk. (kato2008evolutionofnovel pages 2-4, morris2005dysregulatedargininemetabolism pages 7-8)
  4) Thromboinflammation: Heme/oxidized Hb drive NETs (and MCETs) that scaffold thrombosis and amplify occlusion and organ injury (e.g., lung). (chen2014hemeinducedneutrophilextracellular pages 1-2, mahadevia2025areviewon pages 6-8)

- Distinct “hemolytic” vs “viscosity/vaso-occlusive” subphenotypes can dominate specific complications (e.g., PH, leg ulcers, priapism vs frequent VOC/ACS), reflecting relative contributions of hemolysis/NO depletion vs adhesion/viscosity mechanisms. (ilboudo2022multiomicsapproachesto pages 20-24, kato2008evolutionofnovel pages 2-4)

6) Phenotypic Manifestations (with mechanism links)
- Acute painful vaso-occlusive crises (VOC): adhesion/selectin–PSGL‑1 axis and thromboinflammation (NETs/MCETs). (escopy2024targetingthepselectinpsgl1 pages 10-12, chen2014hemeinducedneutrophilextracellular pages 1-2, mahadevia2025areviewon pages 6-8)
- Acute chest syndrome and acute lung injury: NETosis and heme–TLR4 endothelial activation. (chen2014hemeinducedneutrophilextracellular pages 1-2, belcher2014hemetriggerstlr4 pages 6-9)
- Pulmonary hypertension: Hemolysis-associated NO scavenging and arginase-mediated L‑arginine depletion (risk of death markedly elevated with TRV ≥2.5 m/s). (morris2005dysregulatedargininemetabolism pages 7-8, kato2008evolutionofnovel pages 2-4)
- Functional asplenia and infection susceptibility (encapsulated bacteria); infections trigger VOC/ACS and contribute substantially to morbidity/mortality, especially in LMICs. (ilboudo2022multiomicsapproachesto pages 20-24)
- Organ-specific dysfunction from systemic NO depletion/oxidative stress (e.g., bladder overactivity with decreased p‑eNOS/p‑nNOS and increased NOX/oxidative markers in hemolysis models). (xue2024therapeuticsforsickle pages 1-2)

Evidence items and quotes (selected)
- “Heme… activates endothelial TLR4 signaling leading to WPB degranulation, NF‑κB activation” and stasis; TAK‑242 reduced heme‑ or LPS‑induced stasis in SCD mice; hemopexin/haptoglobin abrogate heme effects. URL: https://doi.org/10.1182/blood-2013-04-495887 (Belcher et al., Blood, 2014). (belcher2014hemetriggerstlr4 pages 6-9)
- “Hemolysis releases cell free hemoglobin (Hb)… Free hemoglobin reacts with and scavenges NO… Oxidized hemoglobin and free heme… stimulate neutrophils to release NETs.” URL: https://doi.org/10.1182/blood-2013-10-529982 (Chen et al., Blood, 2014). (chen2014hemeinducedneutrophilextracellular pages 1-2)
- Low arginine bioavailability and PH/mortality: In adults with SCD, TRV ≥2.5 m/s conferred a risk ratio for death ≈7.4; lower arginine:ornithine and arginine:(ornithine+citrulline) ratios independently associated with mortality. URL: https://doi.org/10.1001/jama.294.1.81 (Morris et al., JAMA, 2005). (morris2005dysregulatedargininemetabolism pages 7-8, morris2005dysregulatedargininemetabolism pages 1-2, morris2005dysregulatedargininemetabolism pages 12-18)

Recent developments and latest research (2023–2024)
- HbF reactivation by CRISPR-Cas9 (exagamglogene autotemcel, exa‑cel/Casgevy). In the phase 3 SCD study, among evaluable patients, 97% were free from severe VOCs for ≥12 consecutive months, and 100% were free from VOC hospitalizations for ≥12 months; safety consistent with busulfan-conditioning autologous HSPC transplant. URL: https://doi.org/10.1056/nejmoa2309676 (NEJM, 2024). (frangoul2024exagamglogeneautotemcelfor pages 4-6)
- Selectin pathway: translational and clinical evidence establishes the biological centrality of the P‑selectin/PSGL‑1 axis; however, phase 3 results have been mixed (e.g., negative primary endpoint in STAND), prompting regulatory reassessment and regional revocation in 2023. URLs: https://doi.org/10.1016/j.bvth.2024.100015; (overview) and retrospective real‑world/center experiences. (escopy2024targetingthepselectinpsgl1 pages 10-12, rubio2024thecurrentrole pages 9-11)
- RBC metabolic modulation (pyruvate kinase activators): Class effects include increased RBC ATP and decreased 2,3‑DPG, with early trials showing hemoglobin rises and improved RBC energetics; active development continued through 2023–2024. URL: Hematology ASH Education Program 2023 review https://doi.org/10.1182/hematology.2023000467. (rubio2024thecurrentrole pages 9-11)
- Thromboinflammatory targets: NET/MCET pathways and complement/VWF/ADAMTS13 balance highlighted for future interventions; preclinical and early clinical programs include rADAMTS13 and hemopexin. (chen2014hemeinducedneutrophilextracellular pages 1-2, mahadevia2025areviewon pages 6-8)
- Safety/regulatory updates for legacy agents: Crizanlizumab—mixed efficacy (phase 3 STAND negative) leading to EMA revocation (2023) and caution in observational cohorts; voxelotor—postmarketing safety concerns and mortality signals prompted withdrawal/suspension decisions in 2024. (rubio2024thecurrentrole pages 9-11)

Current applications and implementations
- Hydroxyurea (cornerstone DMM): Increases HbF, lowers leukocytes/platelets and endothelial adhesion markers, improves NO signaling and reduces VOCs, ACS, transfusions, and mortality with long‑term use. Practical guidance emphasizes early initiation in children and use in adults with recurrent VOCs/ACS. URL: https://doi.org/10.3390/jcm13216404 (2024). (rubio2024thecurrentrole pages 9-11)
- Selectin inhibition: While mechanistically compelling, clinical utility is uncertain due to mixed trial data; centers weigh risks, cost, and alternative DMMs; retrospective series report variable VOC trajectories and serious adverse events. (escopy2024targetingthepselectinpsgl1 pages 10-12, rubio2024thecurrentrole pages 9-11)
- Gene therapy: Exa‑cel (Casgevy) has demonstrated high VOC‑free rates and pancellular HbF after myeloablative autologous HSPC gene editing; adoption considerations include myeloablative toxicity, infrastructure, and access disparities. (frangoul2024exagamglogeneautotemcelfor pages 4-6)
- PK activators: Ongoing phase 2/3 programs (mitapivat, etavopivat) exploring clinically meaningful endpoints (Hb increase, VOCs), with phase 1/2 signals of biochemical correction (↑ATP, ↓2,3‑DPG) and hemoglobin rise. (rubio2024thecurrentrole pages 9-11)

Expert opinions and analysis (authoritative sources)
- Mechanism-integrated view: Heme acts as a master DAMP; endothelial TLR4 activation is a proximal switch for WPB release and adhesion, providing rationale for heme scavenging or TLR4 pathway interventions. (belcher2014hemetriggerstlr4 pages 6-9)
- NO pathway as a determinant of the “hemolytic phenotype”: Clinical associations of arginine dysregulation with PH and mortality argue for biomarker‑guided strategies and substrate/enzyme‑targeted adjuvant therapy in selected patients. (morris2005dysregulatedargininemetabolism pages 7-8, kato2008evolutionofnovel pages 2-4)
- Thromboinflammation: Targeting NETs/MCETs and platelet–neutrophil/adhesion modules may complement HbF‑based and metabolic strategies; preclinical proof supports combined anti‑adhesive and anti‑DAMP therapies. (chen2014hemeinducedneutrophilextracellular pages 1-2, escopy2024targetingthepselectinpsgl1 pages 10-12, mahadevia2025areviewon pages 6-8)

Relevant statistics and data (recent and landmark)
- Exa‑cel phase 3 (SCD): 97% (29/30) free from severe VOCs ≥12 months; 100% (30/30) free from VOC hospitalizations ≥12 months; median follow‑up 19.3 months. URL: https://doi.org/10.1056/nejmoa2309676 (NEJM, 2024). (frangoul2024exagamglogeneautotemcelfor pages 4-6)
- Hemolysis–PH–mortality: TRV ≥2.5 m/s carried ~7.4× risk of death; low arginine:ornithine and low global arginine bioavailability independently associated with mortality (risk ratios roughly 2–3.6 depending on metric). URL: https://doi.org/10.1001/jama.294.1.81 (JAMA, 2005). (morris2005dysregulatedargininemetabolism pages 7-8, morris2005dysregulatedargininemetabolism pages 1-2, morris2005dysregulatedargininemetabolism pages 12-18)
- Heme–TLR4–WPB: In murine SCD models, heme rapidly induced WPB degranulation and vaso‑occlusion; TAK‑242 reduced stasis (e.g., vehicle+heme 26.4% vs TAK‑242 9.3%). URL: https://doi.org/10.1182/blood-2013-04-495887 (Blood, 2014). (belcher2014hemetriggerstlr4 pages 6-9)
- NETs in SCD: Heme‑driven NETosis implicated in acute lung injury and VOC in SCD models; DNase and ROS‑modulating strategies proposed. URL: https://doi.org/10.1182/blood-2013-10-529982 (Blood, 2014). (chen2014hemeinducedneutrophilextracellular pages 1-2)
- Bladder dysfunction and NO signaling (model): Intravascular hemolysis increased urinary frequency and DSM hypercontractility with decreased p‑eNOS (Ser1177), p‑nNOS (Ser1417), and p‑VASP (Ser239), and increased NOX‑2, 3‑NT, and 4‑HNE in bladder. URL: https://doi.org/10.3389/fphys.2024.1369120 (Frontiers in Physiology, 2024). (xue2024therapeuticsforsickle pages 1-2)

Structured evidence summary
| Mechanistic axis | Key molecules / cells | Mechanism (concise) | 2023–2024 highlights | Representative sources (journal, year) |
|---|---|---:|---|---|
| HbS polymerization & RBC dehydration | HbS, HbF, Gardos (KCNN4), K-Cl cotransport | Deoxygenated HbS polymerizes → filamentous polymers → RBC sickling, membrane damage, Ca2+ dysregulation → Gardos/K-Cl mediated K+ efflux → RBC dehydration and dense, rigid cells | Continued emphasis on HbF reactivation as protective; PK activators and metabolic approaches aim to alter 2,3‑DPG/ATP to reduce sickling (clinical programs active 2023–24) | (ilboudo2022multiomicsapproachesto pages 20-24, rubio2024thecurrentrole pages 9-11) |
| Adhesion / selectins & WPB release | P‑selectin, E‑selectin, PSGL‑1, Weibel–Palade bodies (VWF, P‑selectin), platelets, endothelium | Endothelial/platelet selectin expression mediates RBC/leukocyte/platelet tethering and rolling → firm adhesion → microvascular occlusion | Therapeutics targeting P‑selectin/PSGL‑1 (crizanlizumab, inclacumab, pan‑selectin agents) show mechanistic benefit; clinical outcomes mixed leading to regulatory reassessments (2023–24) | (escopy2024targetingthepselectinpsgl1 pages 10-12, belcher2014hemetriggerstlr4 pages 6-9) |
| Hemolysis → NO scavenging & arginase | Cell‑free hemoglobin, heme, arginase‑1, L‑arginine, NOS | Intravascular hemolysis releases cell‑free Hb that stoichiometrically scavenges NO; concomitant arginase release depletes L‑arginine, lowering NO production → vasoconstriction, endothelial dysfunction, PH | Strong clinical associations: low arginine:ornithine and low arginine:(ornithine+citrulline) ratios correlate with pulmonary hypertension and increased mortality in cohorts (2005 foundational data reinforced in reviews) | (morris2005dysregulatedargininemetabolism pages 8-9, kato2008evolutionofnovel pages 2-4) |
| Heme → TLR4 signaling (endothelium) | Free heme, TLR4, NADPH oxidase (NOX), PKC, NF‑κB, WPB (P‑selectin, VWF) | Free heme activates endothelial TLR4 → oxidative signaling → Weibel–Palade body degranulation (P‑selectin, VWF) → rapid leukocyte/platelet recruitment and vaso‑occlusion | Murine SCD models: TLR4 blockade (TAK‑242) reduced heme‑induced stasis; hemopexin/haptoglobin mitigate heme effects — supports heme scavenging strategies | (belcher2014hemetriggerstlr4 pages 6-9, guarda2017hememediatedcellactivation pages 1-5) |
| NETs & platelet–neutrophil aggregates | Neutrophils, NETs (citrullinated histones, DNA), platelets, HMGB1 | Heme/oxidized Hb and inflammatory signals trigger NETosis → extracellular chromatin scaffolds bind platelets and promote thrombosis and vaso‑occlusion; platelet–neutrophil crosstalk amplifies thromboinflammation | NET inhibition (DNase, ROS scavengers) and targeting platelet–neutrophil interactions are highlighted as potential interventions in recent reviews | (chen2014hemeinducedneutrophilextracellular pages 1-2, escopy2024targetingthepselectinpsgl1 pages 10-12) |
| Mast cell extracellular traps (MCETs) | Mast cells, PAD4, citrullinated histones, nerve/vascular interfaces | Sickle microenvironment (heme/inflammation) induces MCET release → direct vascular and neural injury contributing to acute/chronic pain and vaso‑occlusion in models | Emerging 2024 data implicate PAD4‑dependent MCETs in vaso‑occlusion and pain; PAD4 inhibition ameliorated stasis and hyperalgesia in mice | (guarda2017hememediatedcellactivation pages 1-5, mahadevia2025areviewon pages 6-8) |
| Complement / VWF axis & ADAMTS13 | Complement proteins, VWF, ADAMTS13, endothelium | Hemolysis/inflammation dysregulate VWF release and complement activation → microthrombotic injury; restoring ADAMTS13 or modulating complement may reduce organ injury | Preclinical and early clinical work (rADAMTS13, complement inhibitors, hemopexin) cited as promising approaches in 2023–24 reviews | (belcher2014hemetriggerstlr4 pages 6-9, mahadevia2025areviewon pages 6-8) |
| PK activators (red‑cell metabolism) | Pyruvate kinase (PKR), 2,3‑DPG, ATP (RBC) | PK activators increase RBC ATP and lower 2,3‑DPG → higher O2 affinity, reduced HbS polymerization tendency, improved RBC deformability and hydration | 2023–24: multiple PK activators (mitapivat, etavopivat, AG‑946) progressed in trials; phase‑1/2 signals show ↑Hb and biochemical shifts (↓2,3‑DPG, ↑ATP) | (rubio2024thecurrentrole pages 9-11, escopy2024targetingthepselectinpsgl1 pages 10-12) |
| Gene therapy (exa‑cel) approvals & outcomes | BCL11A editing, CD34+ HSPCs, CRISPR‑Cas9 | Ex vivo CRISPR editing of BCL11A erythroid enhancer → reactivation of γ‑globin (HbF) in erythroid lineage → reduced sickling and VOCs | Exa‑cel (Casgevy) demonstrated high rates of freedom from severe VOCs and durable HbF induction in phase‑3 data; regulatory approvals occurred in 2023 (UK, USA) with published NEJM outcomes (2024) | (frangoul2024exagamglogeneautotemcelfor pages 4-6) |
| Selectin inhibition — mixed evidence | Crizanlizumab, inclacumab, rivipansel, sevuparin | Blocking P‑selectin/PSGL‑1 reduces multicellular adhesion and theoretically prevents VOCs; clinical benefit depends on trial/context and endpoints | Crizanlizumab showed VOC reduction in earlier trials but Phase‑3 STAND failed to meet primary endpoint leading to regulatory reassessments (2023–24); other selectin agents show variable results | (escopy2024targetingthepselectinpsgl1 pages 10-12, rubio2024thecurrentrole pages 9-11) |
| Voxelotor (Hb‑oxygen affinity modifier) withdrawal signals | Voxelotor (Oxbryta), hemoglobin stabilization | Increases Hb by stabilizing oxygenated HbS (↓polymerization) improving anemia metrics | Approved earlier (2019/2022 regulatory actions), but 2024–2025 safety signal reports and registry/FAERS analyses prompted market withdrawal/reevaluation due to mortality and safety concerns in post‑approval data | (rubio2024thecurrentrole pages 9-11) |
| Infection / functional asplenia & global burden | Splenic dysfunction, encapsulated bacteria, adaptive/innate immune defects | Functional asplenia + immune defects → high risk for invasive infection; infections also trigger VOCs and acute chest syndrome | Reviews (2023–24) emphasize infection as major morbidity/mortality driver in LMICs and the persistent care gap for prophylaxis/vaccination | (ilboudo2022multiomicsapproachesto pages 20-24, rubio2024thecurrentrole pages 9-11) |
| Bladder / organ NO signaling with hemolysis | eNOS, nNOS, VASP, NOX enzymes, oxidative markers | Hemolysis reduces NO signaling (cell‑free Hb + arginase), increases oxidative stress → organ‑specific endothelial / smooth muscle dysfunction (e.g., bladder overactivity) | 2024 experimental work links intravascular hemolysis to reduced phosphorylated eNOS/nNOS and increased NOX/oxidative markers in bladder models, supporting systemic NO‑depletion effects on organs | (morris2005dysregulatedargininemetabolism pages 8-9, xue2024therapeuticsforsickle pages 1-2) |


*Table: Concise table linking core sickle cell disease mechanistic axes to key molecules, short mechanisms, 2023–2024 developments, and representative source citations (context IDs) useful for knowledge‑base curation and evidence mapping.*

Gene/protein annotations (HGNC) with ontology terms (examples)
- HBB (HGNC:4827): hemoglobin complex (GO:0005833); hemoglobin polymerization (GO:0030492). Evidence: HbS polymerization drives sickling. (ilboudo2022multiomicsapproachesto pages 20-24)
- BCL11A (HGNC:13222): regulation of hemoglobin F expression; target of exa‑cel gene editing to reactivate γ‑globin. (frangoul2024exagamglogeneautotemcelfor pages 4-6)
- TLR4 (HGNC:11848): toll-like receptor signaling pathway (GO:0002224); response to heme (GO:1903409). (belcher2014hemetriggerstlr4 pages 6-9)
- SELP/SELE/SELPLG (HGNC:10720/10719/10753): leukocyte tethering or rolling (GO:0050901), cell adhesion (GO:0007155). (escopy2024targetingthepselectinpsgl1 pages 10-12)
- ARG1 (HGNC:663): arginine metabolic process (GO:0006525); negative regulation of nitric oxide biosynthetic process (GO:0046209 context). (morris2005dysregulatedargininemetabolism pages 7-8)
- VWF (HGNC:12726): blood coagulation (GO:0007596); Weibel–Palade body (GO:0042582). (belcher2014hemetriggerstlr4 pages 6-9)
- PADI4 (HGNC:18350): protein citrullination; neutrophil extracellular trap formation (GO:0036342). (mahadevia2025areviewon pages 6-8)

Phenotype associations (HP terms; examples)
- HP:0002092 Acute chest syndrome (NET/adhesion/heme–TLR4). (chen2014hemeinducedneutrophilextracellular pages 1-2, belcher2014hemetriggerstlr4 pages 6-9)
- HP:0001945 Hemolytic anemia (HbS polymerization/hemolysis). (ilboudo2022multiomicsapproachesto pages 20-24)
- HP:0002905 Pulmonary hypertension (NO scavenging/arginase). (morris2005dysregulatedargininemetabolism pages 7-8, kato2008evolutionofnovel pages 2-4)
- HP:0002093 Recurrent infections/functional asplenia (immune dysfunction). (ilboudo2022multiomicsapproachesto pages 20-24)
- HP:0001873 Pain crisis (adhesion/thromboinflammation/MCETs). (escopy2024targetingthepselectinpsgl1 pages 10-12, mahadevia2025areviewon pages 6-8)

Cell type involvement (CL terms; examples)
- Erythrocytes (CL:0000232) – HbS polymerization/ion transport/hemolysis. (ilboudo2022multiomicsapproachesto pages 20-24)
- Endothelial cells (CL:0000115) – TLR4 activation/WPB release. (belcher2014hemetriggerstlr4 pages 6-9)
- Neutrophils (CL:0000775) – NETosis and adhesion. (chen2014hemeinducedneutrophilextracellular pages 1-2)
- Mast cells (CL:0000097) – MCETs in neural/vascular injury and pain. (mahadevia2025areviewon pages 6-8)
- Platelets (CL:0000233) – adhesion/aggregate with NETs. (escopy2024targetingthepselectinpsgl1 pages 10-12)

Anatomical locations (UBERON; examples)
- Microvasculature (UBERON:0001981), lung (UBERON:0002048), kidney (UBERON:0002113), spleen (UBERON:0002106), bladder (UBERON:0001255). (belcher2014hemetriggerstlr4 pages 6-9, chen2014hemeinducedneutrophilextracellular pages 1-2, xue2024therapeuticsforsickle pages 1-2)

Chemical entities (CHEBI; examples)
- Heme (CHEBI:30413), nitric oxide (CHEBI:16480), L‑arginine (CHEBI:29016), ATP (CHEBI:15422), 2,3‑DPG (CHEBI:16001). (chen2014hemeinducedneutrophilextracellular pages 1-2, kato2008evolutionofnovel pages 2-4, rubio2024thecurrentrole pages 9-11)

Citations (URLs and publication dates)
- Belcher et al., Blood, 2014 (Jan). Heme–TLR4–WPB/adhesion link in SCD. URL: https://doi.org/10.1182/blood-2013-04-495887 (belcher2014hemetriggerstlr4 pages 6-9)
- Chen et al., Blood, 2014 (Jun). Hemolysis → NO scavenging; heme → NETs/acute lung injury. URL: https://doi.org/10.1182/blood-2013-10-529982 (chen2014hemeinducedneutrophilextracellular pages 1-2)
- Morris et al., JAMA, 2005 (Jul). Arginase/NO pathway, PH and mortality risk. URL: https://doi.org/10.1001/jama.294.1.81 (morris2005dysregulatedargininemetabolism pages 7-8, morris2005dysregulatedargininemetabolism pages 1-2, morris2005dysregulatedargininemetabolism pages 12-18)
- Frangoul et al., NEJM, 2024 (May). Exa‑cel phase 3 outcomes. URL: https://doi.org/10.1056/nejmoa2309676 (frangoul2024exagamglogeneautotemcelfor pages 4-6)
- Escopy & Chaikof, Blood Vessels, Thrombosis & Hemostasis, 2024 (Sep). Selectin pathway therapeutics overview. URL: https://doi.org/10.1016/j.bvth.2024.100015 (escopy2024targetingthepselectinpsgl1 pages 10-12)
- Rubio & Marina, J Clin Med, 2024 (Oct). Hydroxyurea role; regulatory context for crizanlizumab/voxelotor; PK activators overview. URL: https://doi.org/10.3390/jcm13216404 (rubio2024thecurrentrole pages 9-11)
- Silveira et al., Front Physiol, 2024 (Jul). Hemolysis → bladder NO signaling and oxidative stress. URL: https://doi.org/10.3389/fphys.2024.1369120 (xue2024therapeuticsforsickle pages 1-2)

Notes on evidence strength and gaps
- Landmark mechanistic data (Belcher; Chen) and clinical associations (Morris; Kato/Gladwin) remain foundational. 2023–2024 contributions strengthen translational axes (selectin therapeutics) and show transformative efficacy with exa‑cel for severe SCD. Mixed outcomes and evolving safety signals for selectin inhibitors and Hb‑oxygen affinity modifiers highlight the need for robust, event‑driven endpoints and long‑term pharmacovigilance. (escopy2024targetingthepselectinpsgl1 pages 10-12, rubio2024thecurrentrole pages 9-11, frangoul2024exagamglogeneautotemcelfor pages 4-6)


References

1. (ilboudo2022multiomicsapproachesto pages 20-24): Y Ilboudo. Multi-omics approaches to sickle cell disease heterogeneity. Unknown journal, 2022.

2. (belcher2014hemetriggerstlr4 pages 6-9): John D. Belcher, Chunsheng Chen, Julia Nguyen, Liming Milbauer, Fuad Abdulla, Abdu I. Alayash, Ann Smith, Karl A. Nath, Robert P. Hebbel, and Gregory M. Vercellotti. Heme triggers tlr4 signaling leading to endothelial cell activation and vaso-occlusion in murine sickle cell disease. Blood, 123 3:377-90, Jan 2014. URL: https://doi.org/10.1182/blood-2013-04-495887, doi:10.1182/blood-2013-04-495887. This article has 788 citations and is from a highest quality peer-reviewed journal.

3. (chen2014hemeinducedneutrophilextracellular pages 1-2): Grace Chen, Dachuan Zhang, Tobias A. Fuchs, Deepa Manwani, Denisa D. Wagner, and Paul S. Frenette. Heme-induced neutrophil extracellular traps contribute to the pathogenesis of sickle cell disease. Blood, 123 24:3818-27, Jun 2014. URL: https://doi.org/10.1182/blood-2013-10-529982, doi:10.1182/blood-2013-10-529982. This article has 421 citations and is from a highest quality peer-reviewed journal.

4. (guarda2017hememediatedcellactivation pages 1-5): Caroline Conceição da Guarda, Rayra Pereira Santiago, Luciana Magalhães Fiuza, Milena Magalhães Aleluia, Júnia Raquel Dutra Ferreira, Camylla Vilas Boas Figueiredo, Setondji Cocou Modeste Alexandre Yahouedehou, Rodrigo Mota de Oliveira, Isa Menezes Lyra, and Marilda de Souza Gonçalves. Heme-mediated cell activation: the inflammatory puzzle of sickle cell anemia. Expert Review of Hematology, 10:533-541, May 2017. URL: https://doi.org/10.1080/17474086.2017.1327809, doi:10.1080/17474086.2017.1327809. This article has 39 citations and is from a peer-reviewed journal.

5. (morris2005dysregulatedargininemetabolism pages 7-8): C. Morris, G. Kato, M. Poljakovic, Xunde Wang, W. Blackwelder, V. Sachdev, S. Hazen, E. Vichinsky, S. Morris, and M. Gladwin. Dysregulated arginine metabolism, hemolysis-associated pulmonary hypertension, and mortality in sickle cell disease. JAMA, 294 1:81-90, Jul 2005. URL: https://doi.org/10.1001/jama.294.1.81, doi:10.1001/jama.294.1.81. This article has 905 citations.

6. (kato2008evolutionofnovel pages 2-4): GJ Kato and MT Gladwin. Evolution of novel small-molecule therapeutics targeting sickle cell vasculopathy. JAMA, 300 22:2638-46, Dec 2008. URL: https://doi.org/10.1001/jama.2008.598, doi:10.1001/jama.2008.598. This article has 85 citations.

7. (morris2005dysregulatedargininemetabolism pages 1-2): C. Morris, G. Kato, M. Poljakovic, Xunde Wang, W. Blackwelder, V. Sachdev, S. Hazen, E. Vichinsky, S. Morris, and M. Gladwin. Dysregulated arginine metabolism, hemolysis-associated pulmonary hypertension, and mortality in sickle cell disease. JAMA, 294 1:81-90, Jul 2005. URL: https://doi.org/10.1001/jama.294.1.81, doi:10.1001/jama.294.1.81. This article has 905 citations.

8. (morris2005dysregulatedargininemetabolism pages 12-18): C. Morris, G. Kato, M. Poljakovic, Xunde Wang, W. Blackwelder, V. Sachdev, S. Hazen, E. Vichinsky, S. Morris, and M. Gladwin. Dysregulated arginine metabolism, hemolysis-associated pulmonary hypertension, and mortality in sickle cell disease. JAMA, 294 1:81-90, Jul 2005. URL: https://doi.org/10.1001/jama.294.1.81, doi:10.1001/jama.294.1.81. This article has 905 citations.

9. (morris2005dysregulatedargininemetabolism pages 5-7): C. Morris, G. Kato, M. Poljakovic, Xunde Wang, W. Blackwelder, V. Sachdev, S. Hazen, E. Vichinsky, S. Morris, and M. Gladwin. Dysregulated arginine metabolism, hemolysis-associated pulmonary hypertension, and mortality in sickle cell disease. JAMA, 294 1:81-90, Jul 2005. URL: https://doi.org/10.1001/jama.294.1.81, doi:10.1001/jama.294.1.81. This article has 905 citations.

10. (escopy2024targetingthepselectinpsgl1 pages 10-12): Samira Escopy and Elliot L. Chaikof. Targeting the p-selectin/psgl-1 pathway: discovery of disease-modifying therapeutics for disorders of thromboinflammation. Blood Vessels, Thrombosis &amp; Hemostasis, 1:100015, Sep 2024. URL: https://doi.org/10.1016/j.bvth.2024.100015, doi:10.1016/j.bvth.2024.100015. This article has 21 citations.

11. (mahadevia2025areviewon pages 6-8): Himil Mahadevia, Ben Ponvilawan, Ujjwal Madan, Parth Sharma, Hana Qasim, and Anuj Shrestha. A review on disease modifying pharmacologic therapies for sickle cell disease. Annals of Hematology, 104:881-893, Jan 2025. URL: https://doi.org/10.1007/s00277-025-06216-1, doi:10.1007/s00277-025-06216-1. This article has 8 citations and is from a peer-reviewed journal.

12. (frangoul2024exagamglogeneautotemcelfor pages 4-6): Haydar Frangoul, Franco Locatelli, Akshay Sharma, Monica Bhatia, Markus Mapara, Lyndsay Molinari, Donna Wall, Robert I. Liem, Paul Telfer, Ami J. Shah, Marina Cavazzana, Selim Corbacioglu, Damiano Rondelli, Roland Meisel, Laurence Dedeken, Stephan Lobitz, Mariane de Montalembert, Martin H. Steinberg, Mark C. Walters, Michael J. Eckrich, Suzan Imren, Laura Bower, Christopher Simard, Weiyu Zhou, Fengjuan Xuan, Phuong Khanh Morrow, William E. Hobbs, and Stephan A. Grupp. Exagamglogene autotemcel for severe sickle cell disease. New England Journal of Medicine, 390:1649-1662, May 2024. URL: https://doi.org/10.1056/nejmoa2309676, doi:10.1056/nejmoa2309676. This article has 314 citations and is from a highest quality peer-reviewed journal.

13. (rubio2024thecurrentrole pages 9-11): Montserrat López Rubio and María Argüello Marina. The current role of hydroxyurea in the treatment of sickle cell anemia. Journal of Clinical Medicine, 13:6404, Oct 2024. URL: https://doi.org/10.3390/jcm13216404, doi:10.3390/jcm13216404. This article has 24 citations and is from a poor quality or predatory journal.

14. (xue2024therapeuticsforsickle pages 1-2): Jianyao Xue and Xiang-An Li. Therapeutics for sickle cell disease intravascular hemolysis. Frontiers in Physiology, Sep 2024. URL: https://doi.org/10.3389/fphys.2024.1474569, doi:10.3389/fphys.2024.1474569. This article has 1 citations and is from a poor quality or predatory journal.

15. (morris2005dysregulatedargininemetabolism pages 8-9): C. Morris, G. Kato, M. Poljakovic, Xunde Wang, W. Blackwelder, V. Sachdev, S. Hazen, E. Vichinsky, S. Morris, and M. Gladwin. Dysregulated arginine metabolism, hemolysis-associated pulmonary hypertension, and mortality in sickle cell disease. JAMA, 294 1:81-90, Jul 2005. URL: https://doi.org/10.1001/jama.294.1.81, doi:10.1001/jama.294.1.81. This article has 905 citations.