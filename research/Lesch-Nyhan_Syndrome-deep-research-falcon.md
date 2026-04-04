---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-22T10:11:02.884382'
end_time: '2026-03-22T10:20:38.079921'
duration_seconds: 575.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lesch-Nyhan Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Lesch-Nyhan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lesch-Nyhan Syndrome**.
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
- **Disease Name:** Lesch-Nyhan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lesch-Nyhan Syndrome**.
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


# Lesch–Nyhan syndrome (LNS) pathophysiology research report (molecular/cellular mechanisms)

## Disease identifiers and scope
- **Disease name:** Lesch–Nyhan syndrome / Lesch–Nyhan disease (classic severe phenotype of HPRT deficiency)
- **Category:** Mendelian (X-linked)
- **Core causal gene:** **HPRT1** (HGNC: **5157**) encoding hypoxanthine-guanine phosphoribosyltransferase (**HGPRT/HPRT**) (camici2023inbornerrorsof pages 7-8)
- **Note on MONDO ID:** Not retrievable from the provided tool evidence; report proceeds with gene/protein-grounded identifiers.

## Executive summary (current understanding)
Lesch–Nyhan syndrome is caused by severe loss of **HPRT1/HGPRT** activity, disrupting the **purine salvage pathway** and leading to (i) systemic overproduction of uric acid (hyperuricemia/hyperuricuria) and (ii) a characteristic neurobehavioral phenotype dominated by dystonia and compulsive self-injury that is **not corrected by urate-lowering therapy** (camici2023inbornerrorsof pages 8-9, bairddaniel2023singleelectrodedeepbrain pages 1-2). Contemporary work (2023–2024) increasingly emphasizes that brain vulnerability reflects a combination of **(a) developmental disruption of midbrain dopaminergic circuitry and basal ganglia network function**, and **(b) bioenergetic/metabolic stress (mitochondrial complex I effects; purine pool imbalance; PRPP limitation; folate/one-carbon constraints)** rather than uric acid toxicity per se (vinokurov2023hprt1deficiencyinduces pages 1-2, tsagkaris2023metabolicpatternsin pages 1-2, escuderoferruz2024anewphysiological pages 1-2, sekine2024significanceandamplification pages 2-4).

A 2024 mechanistic advance is that **physiologic culture conditions** reveal accumulation of **ZMP/AICAR** in patient fibroblasts (an intermediate in de novo purine synthesis), with plausible downstream signaling effects (e.g., **AMPK activation**, **ADSL inhibition**, and mitochondrial oxidative phosphorylation inhibition), and these phenotypes can be masked by supraphysiologic folate levels used in standard media (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473). A separate 2024 advance clarifies why the CNS is unusually sensitive: human brain tissue shows **high HPRT expression and essentially absent xanthine oxidoreductase (XOR)**, extremely low brain uric acid, and rapid incorporation of hypoxanthine into ATP via salvage—implying that loss of HPRT removes a dominant neuronal route for rapid purine/adenylate replenishment (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 4-7).

## 1) Core pathophysiology

### 1.1 Key concepts and definitions
- **Purine salvage pathway:** Recycling of purine bases (hypoxanthine, guanine) back to nucleotides (IMP, GMP) using **PRPP**; this reduces energy cost versus de novo synthesis and helps maintain nucleotide pools (camici2023inbornerrorsof pages 7-8, sekine2024significanceandamplification pages 4-7).
- **HGPRT/HPRT (HPRT1):** Principal PRPP-dependent salvage enzyme converting **hypoxanthine → IMP** and **guanine → GMP** (camici2023inbornerrorsof pages 7-8, sekine2024significanceandamplification pages 2-4).
- **De novo purine synthesis:** Energetically intensive pathway generating IMP and downstream adenylate/guanylate nucleotides; requires folate-derived **10-formyltetrahydrofolate** at steps catalyzed by **GART** and **ATIC** (highlighted in a 2024 pathway schematic) (escuderoferruz2024anewphysiological media f6714473).
- **ZMP/AICAR:** A de novo pathway intermediate (AICAR monophosphate; also called ZMP), which can act as an AMP mimetic and influence signaling pathways such as AMPK; its accumulation can indicate altered pathway flux/bottlenecks (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473).

### 1.2 Primary pathophysiological mechanisms
**(A) Purine salvage failure → hyperuricemia and altered purine pools**
Loss of HGPRT prevents recycling of hypoxanthine and guanine, contributing to accumulation of bases and increased catabolism to uric acid, alongside **increased PRPP** and **“grossly increased de novo purine synthesis”** reported in a 2023 review of inborn purine disorders (camici2023inbornerrorsof pages 8-9). Clinically, xanthine oxidase inhibitors lower urate but do not correct neurologic/behavioral manifestations, supporting urate-independent mechanisms for neurophenotypes (camici2023inbornerrorsof pages 8-9, bairddaniel2023singleelectrodedeepbrain pages 1-2).

**(B) De novo pathway acceleration + physiologic folate constraint → ZMP accumulation and stress signaling**
A 2024 Molecular Medicine study emphasizes that under physiologic folate (e.g., **25 nM** folic acid vs **~2200 nM** in standard media), LND fibroblasts accumulate **ZMP**, and ZMP is linked to dysregulation of multiple pathways including **AMPK activation**, **ADSL inhibition**, and **mitochondrial oxidative phosphorylation inhibition** (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473). Importantly, the study reports that use of a fully physiologic medium (Plasmax-PV) uncovers additional phenotypes including higher glycolytic capacity, increased **SLC19A1** (folate carrier) expression, decreased mitochondrial membrane potential, and reduced cell migration, which can be reversed with high folic acid (escuderoferruz2024anewphysiological pages 1-2).

**(C) Brain-specific purine economy creates neuronal vulnerability**
A 2024 JBC study provides a mechanistic rationale for brain vulnerability: human brain has **high HPRT**, **essentially no detectable XOR**, and very low uric acid (reported as **~1% of total purines**), implying that hypoxanthine is preferentially preserved and routed into salvage rather than oxidized to urate (sekine2024significanceandamplification pages 2-4). In iPSC-derived neurons, labeled hypoxanthine is incorporated into ATP **within 5 minutes**, indicating that salvage can dominate rapid ATP/purine replenishment; PRPP availability is highlighted as a critical limiter (“hypoxanthine alone has a limited ATP-enhancing effect due to PRPP depletion”), tying pentose phosphate pathway flux to salvage capacity (sekine2024significanceandamplification pages 4-7, sekine2024significanceandamplification pages 12-14).

## 2) Dysregulated molecular pathways and cellular processes

### 2.1 Pathways implicated (with mechanistic evidence)
1. **Purine salvage/de novo synthesis balance**: PRPP elevation + increased de novo synthesis in HPRT deficiency, shifting flux and creating intermediates such as ZMP (camici2023inbornerrorsof pages 8-9, escuderoferruz2024anewphysiological pages 1-2).
2. **Folate/one-carbon metabolism coupling to purine synthesis**: dependence on folate-derived 10-formyl-THF at GART/ATIC steps; physiologic folate reveals metabolic imbalance and adaptive upregulation of folate transport (SLC19A1) (escuderoferruz2024anewphysiological media f6714473, escuderoferruz2024anewphysiological pages 1-2).
3. **AMPK-linked energy stress signaling**: ZMP accumulation is linked (in the 2024 LND fibroblast work and its pathway figure) to AMPK activation and downstream mitochondrial effects (escuderoferruz2024anewphysiological media f6714473).
4. **Mitochondrial bioenergetics (Complex I)**: a 2023 murine neuronal study reports that HPRT1 deficiency inhibits **complex I-dependent respiration**, increases mitochondrial NADH, reduces mitochondrial membrane potential, and increases ROS; authors interpret this primarily as energy metabolism disruption rather than overt oxidative stress (no glutathione depletion reported in the excerpt) (vinokurov2023hprt1deficiencyinduces pages 1-2).
5. **Dopaminergic developmental programming and basal ganglia circuit function**: developmental abnormalities in dopaminergic neuron migration/proliferation and reduced dopaminergic phenotypes have been reported in Hprt-deficient models (camici2023inbornerrorsof pages 8-9, camici2023inbornerrorsof pages 36-37). Network-level alterations are supported by FDG-PET patterns and neuroimaging findings (tsagkaris2023metabolicpatternsin pages 1-2).

### 2.2 Cellular processes affected
- **Nucleotide homeostasis / adenylate maintenance:** rapid salvage of hypoxanthine into ATP in neurons implies HPRT deficiency can compromise acute/chronic maintenance of adenylate pools (sekine2024significanceandamplification pages 4-7).
- **Mitochondrial respiration and membrane potential regulation:** decreased mitochondrial potential in LND fibroblasts under physiologic medium; complex I-dependent respiration defects in murine neurons (escuderoferruz2024anewphysiological pages 1-2, vinokurov2023hprt1deficiencyinduces pages 1-2).
- **Cell migration and developmental programs:** reduced migration in LND fibroblasts and evidence for altered developmental programming of dopaminergic neurons in models (escuderoferruz2024anewphysiological pages 1-2, camici2023inbornerrorsof pages 8-9).
- **Brain glucose metabolism networks:** FDG-PET shows distinctive multi-region hypometabolism pattern for HPRT1 dystonia subgroup (tsagkaris2023metabolicpatternsin pages 1-2).

## 3) Key molecular players (entities and ontologies)

### 3.1 Genes/proteins (HGNC; selected relevant GO)
- **HPRT1** (HGNC:5157) – hypoxanthine-guanine phosphoribosyltransferase; central causal gene (camici2023inbornerrorsof pages 7-8, sekine2024significanceandamplification pages 2-4)
  - Example GO processes (conceptual mapping): **purine nucleobase salvage**; **inosine monophosphate biosynthetic process**.
- **SLC19A1** (HGNC:1104) – folate transporter (RFC1); increased expression in LND fibroblasts under physiologic medium (escuderoferruz2024anewphysiological pages 1-2)
- **PRPS1/2** (HGNC:9442/9443) – PRPP synthesis (PRPP limitation emphasized for salvage capacity) (sekine2024significanceandamplification pages 12-14)
- **GART** (HGNC:4137) and **ATIC** (HGNC:204) – folate-dependent de novo purine synthesis steps (schematic) (escuderoferruz2024anewphysiological media f6714473)
- **ADSL** (HGNC:99) – adenylosuccinate lyase; proposed inhibited by ZMP in LND context (escuderoferruz2024anewphysiological media f6714473)
- **AMPK** complex (PRKAA1/2 etc.) – activated by ZMP in the proposed LND pathway schematic (escuderoferruz2024anewphysiological media f6714473)
- **XOR/XDH** (xanthine oxidoreductase; gene XDH HGNC:12805) – essentially absent/detectable at very low level in human brain, shaping CNS purine handling (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 1-2)

### 3.2 Chemical entities (CHEBI)
- **Hypoxanthine** (CHEBI:17368) – salvage substrate; elevated/handled differently in brain; rapidly incorporated into ATP by salvage in neurons (sekine2024significanceandamplification pages 4-7).
- **Guanine** (CHEBI:16235) – salvage substrate (camici2023inbornerrorsof pages 7-8).
- **PRPP** (5-phospho-α-D-ribose 1-diphosphate; CHEBI:17111) – required cosubstrate for salvage; depletion limits ATP enhancement by hypoxanthine (sekine2024significanceandamplification pages 12-14).
- **IMP** (CHEBI:17514) and **GMP** (CHEBI:17138) – nucleotide products of salvage (camici2023inbornerrorsof pages 7-8).
- **Uric acid/urate** (CHEBI:27226) – end product of purine catabolism; low in brain relative to total purines; corrected by allopurinol but neurologic phenotype persists (sekine2024significanceandamplification pages 2-4, bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **ZMP/AICAR monophosphate** (CHEBI:57628) – accumulated in LND fibroblasts in physiologic conditions; linked to AMPK and mitochondrial effects (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473).
- **Folic acid** (CHEBI:27470) and 10-formyl-THF (CHEBI:15636) – key in de novo purine steps (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473).
- **Allopurinol** (CHEBI:46195) – xanthine oxidase inhibitor used clinically (bairddaniel2023singleelectrodedeepbrain pages 1-2, reisz2023redbloodcells pages 5-7).

### 3.3 Cell types (CL) and anatomical locations (UBERON)
- **Midbrain dopaminergic neurons** (CL:0000700) and **striatal terminals** – implicated in dopaminergic dysfunction and developmental disruption (camici2023inbornerrorsof pages 8-9, alsuwaidi2025onecarbonmetabolismand pages 3-4).
- **Fibroblasts** (CL:0000057) – used to reveal physiologic-medium phenotypes including ZMP accumulation and mitochondrial potential reduction (escuderoferruz2024anewphysiological pages 1-2).
- **Erythrocytes** (CL:0000232) – multi-omics biomarkers and systemic metabolic effects observed (reisz2023redbloodcells pages 5-7, reisz2023redbloodcells pages 11-14).
- **Basal ganglia / globus pallidus internus (GPi)** (UBERON:0002038 / UBERON:0002973) – circuit focus for dystonia and DBS targeting (bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **Thalamus, brainstem, cerebellum, cortex** – implicated by FDG-PET hypometabolism patterns (tsagkaris2023metabolicpatternsin pages 1-2).

## 4) Biological processes (GO-oriented) disrupted (knowledge-base candidates)
The following processes are supported as disrupted/implicated by the evidence base:
- **Purine nucleobase salvage / purine nucleotide salvage** (loss of HGPRT activity) (camici2023inbornerrorsof pages 7-8, sekine2024significanceandamplification pages 2-4)
- **De novo IMP biosynthetic process / purine ribonucleotide biosynthetic process** (compensatory acceleration; ZMP accumulation) (camici2023inbornerrorsof pages 8-9, escuderoferruz2024anewphysiological pages 1-2)
- **Folate-dependent one-carbon metabolic process** (dependency at GART/ATIC; physiologic folate reveals phenotypes; SLC19A1 upregulation) (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473)
- **Cellular response to energy starvation / AMPK signaling pathway** (ZMP→AMPK activation in pathway schematic) (escuderoferruz2024anewphysiological media f6714473)
- **Mitochondrial electron transport, NADH to ubiquinone (Complex I)** (complex I-dependent respiration inhibition in HPRT1-deficient neurons) (vinokurov2023hprt1deficiencyinduces pages 1-2)
- **Dopaminergic neuron differentiation/development and axon guidance/migration** (abnormal DA neuron development and migration in Hprt-deficient models) (camici2023inbornerrorsof pages 8-9)
- **Regulation of glucose metabolic process / brain network metabolism** (FDG-PET hypometabolism pattern unique to HPRT1 dystonia subgroup) (tsagkaris2023metabolicpatternsin pages 1-2)

## 5) Cellular components (where key processes occur)
- **Cytosol:** HGPRT enzyme activity; PRPP-dependent salvage reactions; de novo purine synthesis steps generating ZMP (camici2023inbornerrorsof pages 7-8, escuderoferruz2024anewphysiological media f6714473).
- **Mitochondria (inner membrane / respiratory chain):** complex I-dependent respiration and membrane potential changes implicated in HPRT1 deficiency models (vinokurov2023hprt1deficiencyinduces pages 1-2, escuderoferruz2024anewphysiological pages 1-2).
- **Plasma membrane / transport systems:** folate transporter **SLC19A1** upregulation and nutrient availability effects under physiologic medium (escuderoferruz2024anewphysiological pages 1-2).
- **Synaptic terminals/circuit nodes (systems-level):** striatal terminals and basal ganglia network nodes implicated by dopamine dysfunction and imaging patterns (alsuwaidi2025onecarbonmetabolismand pages 3-4, tsagkaris2023metabolicpatternsin pages 1-2).

## 6) Disease progression model (sequence of events)
A mechanistically consistent sequence supported by the retrieved evidence is:
1. **Genetic trigger:** hemizygous loss-of-function variants in **HPRT1** → severe HGPRT deficiency (camici2023inbornerrorsof pages 7-8).
2. **Immediate metabolic consequences:** impaired hypoxanthine/guanine salvage → accumulation of purine bases/PRPP; increased de novo synthesis; increased production of urate (systemically) (camici2023inbornerrorsof pages 8-9, escuderoferruz2024anewphysiological pages 1-2).
3. **Brain-specific vulnerability:** human brain relies on salvage (high HPRT, absent XOR, rapid salvage incorporation into ATP) → HPRT loss disrupts rapid purine/adenylate maintenance, with PRPP supply as a limiting factor (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 4-7, sekine2024significanceandamplification pages 12-14).
4. **Cellular stress responses:** in physiologic nutrient conditions, de novo pathway intermediate **ZMP** accumulates and is linked to AMPK/ADSL/mitochondrial effects; fibroblasts show decreased mitochondrial membrane potential and impaired migration (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473).
5. **Neurodevelopmental derailment:** Hprt-deficient models exhibit reduced early dopaminergic neurons and abnormal migration, suggesting a critical early developmental window (camici2023inbornerrorsof pages 8-9).
6. **Systems/circuit manifestation:** basal ganglia network dysfunction (dopamine pathway deficits) yields dystonia and self-injury; FDG-PET patterns show widespread hypometabolism unique to HPRT1 subgroup among pediatric dystonias (tsagkaris2023metabolicpatternsin pages 1-2).

**Clinical timing anchors (reported):** psychomotor delay may appear at **3–6 months** (review excerpt) and motor symptoms/cognitive delay typically present before age 1; self-mutilation onset is often in early childhood (e.g., between ages 1–6) (camici2023inbornerrorsof pages 8-9, bairddaniel2023singleelectrodedeepbrain pages 1-2).

## 7) Phenotypic manifestations (HP terms) and mechanistic links
- **Hyperuricemia** (HP:0002149) / nephrolithiasis (HP:0000787) / gouty arthritis (HP:0001997): explained by increased purine catabolism and urate production due to salvage failure; treated with allopurinol (camici2023inbornerrorsof pages 8-9, bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **Dystonia** (HP:0001332) and severe motor disability: linked to basal ganglia circuitry dysfunction and dopaminergic abnormalities; supported by DBS targeting GPi (bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **Self-injurious behavior** (HP:0100716) (including compulsive self-mutilation): thought to relate to disrupted dopaminergic circuit development/function in basal ganglia–prefrontal/limbic pathways; DBS reports suggest modifiability via circuit intervention (bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **Intellectual disability / developmental delay** (HP:0001249 / HP:0001263): likely linked to early neurodevelopmental programming defects and widespread network-level metabolic abnormalities (camici2023inbornerrorsof pages 8-9, tsagkaris2023metabolicpatternsin pages 1-2).

## 8) Recent developments (prioritizing 2023–2024)

### 8.1 Physiologic media reveals masked biochemical/cellular phenotypes (2024)
Escudero-Ferruz et al. (Molecular Medicine; published Jan 2024; https://doi.org/10.1186/s10020-023-00774-8) report that physiologic nutrient conditions uncover LND fibroblast alterations including **ZMP accumulation**, **higher glycolytic capacity**, **increased SLC19A1**, **decreased mitochondrial potential**, and **reduced cell migration**, reversible with high folic acid (escuderoferruz2024anewphysiological pages 1-2). A central mechanistic figure explicitly links ZMP to AMPK activation, ADSL inhibition and mitochondrial dysfunction, and highlights folate dependence at GART/ATIC steps (escuderoferruz2024anewphysiological media f6714473).

### 8.2 Human brain dependence on salvage clarified with tissue + iPSC neuron tracing (2024)
Sekine et al. (J Biol Chem; published Aug 2024; https://doi.org/10.1016/j.jbc.2024.107524) show human brain has high HPRT, minimal XOR, very low uric acid (~1% of total purines), and that iPSC-derived neurons rapidly incorporate hypoxanthine into ATP (detectable within 5 minutes). The work emphasizes PRPP limitation and PPP-mediated amplification of salvage (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 4-7, sekine2024significanceandamplification pages 12-14).

### 8.3 Brain mitochondrial bioenergetics in an Hprt1-deficient mouse model (2023)
Vinokurov et al. (Molecular Neurobiology; published Feb 2023; https://doi.org/10.1007/s12035-023-03266-2) report Hprt1 deficiency inhibits complex I-dependent respiration, increases mitochondrial NADH, reduces membrane potential, and increases ROS; the authors propose disrupted mitochondrial energy metabolism (rather than overt oxidative stress) as a potential trigger for brain pathology (vinokurov2023hprt1deficiencyinduces pages 1-2).

### 8.4 Imaging biomarkers of dystonia etiology include a distinctive HPRT1 signature (2023)
Tsagkaris et al. (Brain; published Nov 2023; https://doi.org/10.1093/brain/awac439) analyzed FDG-PET in a pediatric dystonia cohort and report that the **HPRT1 (Lesch–Nyhan)** subgroup “**uniquely showed glucose hypometabolism across all nine cerebral regions**,” with additional region patterns (temporal, thalamic/brainstem, cerebellar/insula) that differed from other genetic dystonias (tsagkaris2023metabolicpatternsin pages 1-2).

### 8.5 Translational gene correction by base/prime editing (2023)
Jang et al. (Molecular Therapy – Nucleic Acids; published Mar 2023; https://doi.org/10.1016/j.omtn.2023.02.009) demonstrated modeling and correction of HPRT1 mutations using CRISPR base editors and prime editors. In patient fibroblasts carrying a frameshift (c.333_334ins(A)), an optimized prime editing system achieved **~14% correction** and restored HPRT protein/activity as assessed by selection assays and enzymatic readouts (jang2023therapeuticgenecorrection pages 2-4, jang2023therapeuticgenecorrection pages 6-7).

## 9) Current applications and real-world implementations

### 9.1 Standard management
- **Urate lowering:** allopurinol lowers serum uric acid and reduces stone risk but does not improve movement disorder/neurobehavioral features (bairddaniel2023singleelectrodedeepbrain pages 1-2, reisz2023redbloodcells pages 5-7).
  - Example real-world data: in a 2023 RBC multi-omics study of three affected siblings, serum uric acid at diagnosis was reported **~5–6.5 mg/dL** (normal <2–4.5 mg/dL), and allopurinol normalized urate without improving movement disorder (reisz2023redbloodcells pages 5-7).

### 9.2 Neurosurgical circuit modulation
- **Deep brain stimulation (DBS) of GPi:** a 2023 report describes DBS targeting posterolateral GPi in two pediatric patients (ages 6 and 14) with medically resistant disease, with caregiver-reported reductions in dystonia and self-injury (bairddaniel2023singleelectrodedeepbrain pages 1-2). This is consistent with basal ganglia circuit involvement.

### 9.3 Emerging/experimental causal strategies
- **Genome editing (base/prime editing):** in vitro correction of endogenous HPRT1 mutations with functional rescue provides proof-of-principle for causal therapy, but editing efficiency in primary cells remains variable and delivery to relevant brain cell types remains a major translational barrier (jang2023therapeuticgenecorrection pages 6-7, jang2023therapeuticgenecorrection pages 7-8).

## 10) Expert opinions / analysis (from authoritative sources in the retrieved corpus)

### 10.1 Urate is not the driver of neurobehavioral disease
Across mechanistic reviews and clinical reports, the consistent observation is that urate-lowering improves gout/nephrolithiasis risk but not neurobehavioral phenotype (camici2023inbornerrorsof pages 8-9, bairddaniel2023singleelectrodedeepbrain pages 1-2). This supports a model in which neurological manifestations are downstream of brain-specific purine handling and neurodevelopmental/circuit mechanisms rather than direct urate toxicity.

### 10.2 Developmental vs maintenance hypotheses
The evidence base includes strong support for early dopaminergic developmental abnormalities (reduced early DA neurons, abnormal migration) (camici2023inbornerrorsof pages 8-9), while human neuron metabolic tracing highlights ongoing reliance on salvage for rapid ATP/purine replenishment (sekine2024significanceandamplification pages 4-7). Together, these support a hybrid view: early developmental miswiring plus chronic metabolic vulnerability.

### 10.3 Importance of physiologic model systems
The 2024 physiologic-medium fibroblast study argues that standard media can mask disease-relevant phenotypes (e.g., ZMP accumulation, mitochondrial potential changes), implying that future mechanistic and therapeutic screens should use physiologic nutrient conditions for metabolic diseases like LND (escuderoferruz2024anewphysiological pages 1-2).

## 11) Relevant statistics and quantitative data (recent studies)
- **Incidence estimate:** ~**1 in 380,000 live births** (clinical report summary) (bairddaniel2023singleelectrodedeepbrain pages 1-2).
- **FDG-PET cohort:** 267 children scanned; 240 analyzed (no gross anatomic abnormality); patterns examined in 144/240 (60%) across 10 dystonia etiologies; HPRT1 showed unique hypometabolism across all nine cerebral regions (tsagkaris2023metabolicpatternsin pages 1-2).
- **Brain biochemistry (human tissue):** total extracted purines ~**2000 pmol/mg tissue**; uric acid **~1% of total purines** (sekine2024significanceandamplification pages 2-4).
- **Neuronal salvage kinetics:** hypoxanthine incorporation into ATP detectable **within 5 min** in iPSC-derived neurons (sekine2024significanceandamplification pages 4-7).
- **Serum urate (example LNS family):** **~5–6.5 mg/dL** at diagnosis in three affected siblings; allopurinol normalized urate but not movement disorder (reisz2023redbloodcells pages 5-7).
- **RBC omics statistics (2023):** 103/257 lipids differentially abundant (p<0.05) and 147 RBC proteins significantly altered (p<0.05) in a small family cohort study (reisz2023redbloodcells pages 11-14).
- **Gene correction efficiency:** prime editing improved to **~14%** in patient fibroblasts with functional rescue (jang2023therapeuticgenecorrection pages 6-7).

## 12) Evidence items (knowledge-base ready; with source links)
**Note on PMIDs:** The retrieved tool excerpts did not contain explicit PMID strings, so this report provides **DOIs/URLs and publication dates** as primary identifiers.

1. Escudero-Ferruz P, et al. *Molecular Medicine*. **Jan 2024**. “A new physiological medium uncovers biochemical and cellular alterations in Lesch-Nyhan disease fibroblasts.” https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2)
2. Sekine M, et al. *Journal of Biological Chemistry*. **Aug 2024**. “Significance and amplification methods of the purine salvage pathway in human brain cells.” https://doi.org/10.1016/j.jbc.2024.107524 (sekine2024significanceandamplification pages 2-4)
3. Vinokurov AY, et al. *Molecular Neurobiology*. **Feb 2023**. “HPRT1 Deficiency Induces Alteration of Mitochondrial Energy Metabolism in the Brain.” https://doi.org/10.1007/s12035-023-03266-2 (vinokurov2023hprt1deficiencyinduces pages 1-2)
4. Tsagkaris S, et al. *Brain*. **Nov 2023**. “Metabolic patterns in brain 18F-fluorodeoxyglucose PET relate to aetiology in paediatric dystonia.” https://doi.org/10.1093/brain/awac439 (tsagkaris2023metabolicpatternsin pages 1-2)
5. Jang G, et al. *Molecular Therapy – Nucleic Acids*. **Mar 2023**. “Therapeutic gene correction for Lesch-Nyhan syndrome using CRISPR-mediated base and prime editing.” https://doi.org/10.1016/j.omtn.2023.02.009 (jang2023therapeuticgenecorrection pages 2-4)
6. Reisz JA, et al. *Antioxidants*. **Aug 2023**. “Red Blood Cells from Individuals with Lesch–Nyhan Syndrome: Multi-Omics Insights…” https://doi.org/10.3390/antiox12091699 (reisz2023redbloodcells pages 5-7)

## 13) Curated mechanism summary table
The following table summarizes cross-scale mechanisms and is intended for direct knowledge-base ingestion.

| Mechanistic layer | Key findings | Key molecules/metabolites | Primary cell types/tissues | Evidence (paper + year + URL) | Notes/quantitative data |
|---|---|---|---|---|---|
| Genetic | Lesch–Nyhan syndrome results from loss-of-function variants in **HPRT1**, causing near-complete deficiency of hypoxanthine-guanine phosphoribosyltransferase (HGPRT/HPRT), the key PRPP-dependent salvage enzyme converting hypoxanthine and guanine to IMP and GMP. Severe classic disease is associated with very low residual activity. | HPRT1/HGPRT, PRPP, hypoxanthine, guanine, IMP, GMP | Brain (high HPRT expression), erythrocytes, fibroblasts | Camici et al., 2023, https://doi.org/10.3390/metabo13070787 (camici2023inbornerrorsof pages 7-8); Alsuwaidi & Ernst, 2025, https://doi.org/10.1159/000549247 (alsuwaidi2025onecarbonmetabolismand pages 1-2, alsuwaidi2025onecarbonmetabolismand pages 2-3) | >95% activity loss linked to classic LND in review excerpt; >600 HPRT mutations noted in review literature (camici2023inbornerrorsof pages 7-8, alsuwaidi2025onecarbonmetabolismand pages 2-3) |
| Metabolic | Salvage failure causes accumulation of unrecycled purine bases and **PRPP**, accelerates **de novo purine synthesis**, and increases uric acid production; xanthine oxidase inhibitors lower urate but do not correct neurological disease. | PRPP, hypoxanthine, xanthine, uric acid, IMP, GMP | Liver/systemic purine metabolism; fibroblasts; brain | Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2); Camici et al., 2023, https://doi.org/10.3390/metabo13070787 (camici2023inbornerrorsof pages 8-9); Vinokurov et al., 2023, https://doi.org/10.1007/s12035-023-03266-2 (vinokurov2023hprt1deficiencyinduces pages 1-2) | Hyperuricemia may be evident from birth; neurological features persist despite urate lowering (camici2023inbornerrorsof pages 8-9, vinokurov2023hprt1deficiencyinduces pages 1-2) |
| Metabolic | Under physiological folate conditions, HPRT-deficient fibroblasts accumulate **ZMP/AICAR**, revealing a de novo purine bottleneck not seen in standard high-folate media. | ZMP/AICAR, folic acid, 10-formyl-THF | Patient fibroblasts | Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473) | Physiological folic acid 25 nM vs ~2200 nM in standard media highlighted in pathway figure summary (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473) |
| Signaling | ZMP is linked to **AMPK activation**, **ADSL inhibition**, and inhibition of mitochondrial oxidative phosphorylation, connecting purine disequilibrium to stress-response signaling and bioenergetic dysfunction. | ZMP/AICAR, AMPK, ADSL | Fibroblasts; likely broader relevance to neurons | Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473) | Supported by pathway schematic and physiological-medium experiments; high folate reversibility suggests nutrient-sensitive signaling effects (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473) |
| One-carbon / folate metabolism | Loss of salvage creates greater demand on **de novo purine synthesis**, increasing dependence on **one-carbon metabolism** and folate-derived 10-formyl-THF at the GART and ATIC steps; HPRT-deficient cells upregulate folate transport and may reroute one-carbon flux away from other pathways. | 10-formyl-THF, GART, ATIC, SLC19A1, serine/OCM intermediates | Fibroblasts; midbrain dopaminergic cells (hypothesized vulnerable cell type) | Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2); Alsuwaidi & Ernst, 2025, https://doi.org/10.1159/000549247 (alsuwaidi2025onecarbonmetabolismand pages 3-4, alsuwaidi2025onecarbonmetabolismand pages 1-2) | Increased SLC19A1 expression and reversibility with high folate reported in fibroblasts; OCM rerouting proposed as a disease mechanism for DA neurons (escuderoferruz2024anewphysiological pages 1-2, alsuwaidi2025onecarbonmetabolismand pages 3-4) |
| Cellular / bioenergetic | HPRT1 deficiency impairs **complex I-dependent mitochondrial respiration**, increases mitochondrial NADH, lowers mitochondrial membrane potential, and elevates mitochondrial/cytosolic ROS; in murine neurons this was interpreted as energy-metabolism disruption more than overt oxidative damage. | Complex I, NADH, ROS, glutathione, mitochondrial membrane potential | Murine cortical and midbrain neurons; fibroblasts | Vinokurov et al., 2023, https://doi.org/10.1007/s12035-023-03266-2 (vinokurov2023hprt1deficiencyinduces pages 1-2); Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2) | ROS increased without GSH depletion in neuronal study; fibroblasts showed decreased mitochondrial potential and higher glycolytic capacity (vinokurov2023hprt1deficiencyinduces pages 1-2, escuderoferruz2024anewphysiological pages 1-2) |
| Cellular / motility | HPRT-deficient cells show reduced migration and broader developmental-gene dysregulation, supporting a developmental component rather than solely toxic metabolite accumulation. | Homeobox genes, developmental programs, folate transporter SLC19A1 | Fibroblasts; pluripotent/neuroectodermal cells | Escudero-Ferruz et al., 2024, https://doi.org/10.1186/s10020-023-00774-8 (escuderoferruz2024anewphysiological pages 1-2); Torres et al., 2025, https://doi.org/10.3390/cells14141105 (from search result summary, not cited here) | Reduced migration in physiological medium; development and nervous-system GO categories highlighted in related stem-cell work, but table relies only on cited context IDs for mechanistic claims (escuderoferruz2024anewphysiological pages 1-2) |
| Brain purine economy | Human brain is unusually dependent on salvage: **HPRT is high, XOR is essentially absent**, brain uric acid is very low, and hypoxanthine is preferentially routed into IMP/ATP rather than xanthine/urate. This helps explain neuronal sensitivity to HPRT loss. | HPRT, XOR, hypoxanthine, PRPP, IMP, ATP, uric acid | Human brain tissue; iPSC-derived neurons | Sekine et al., 2024, https://doi.org/10.1016/j.jbc.2024.107524 (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 1-2, sekine2024significanceandamplification pages 4-7, sekine2024significanceandamplification pages 12-14) | Uric acid ~1% of total purines in brain; total purines ~2000 pmol/mg tissue; labeled hypoxanthine incorporated into ATP within 5 min in iPSC-derived neurons (sekine2024significanceandamplification pages 2-4, sekine2024significanceandamplification pages 4-7) |
| Neurodevelopmental | Evidence supports an **early developmental defect of dopaminergic neurons**: reduced early DA neurons, abnormal migration/radial-glia scaffolds, disorganized innervation, and altered expression of developmental regulators and receptors in HPRT-deficient models. | Dopamine, TH, AADC, Wnt4, Wnt11, LMX1B, DRD1, ADORA2A, ADORA2B, 5-HTR7 | Midbrain dopaminergic neurons, basal ganglia/striatum | Camici et al., 2023, https://doi.org/10.3390/metabo13070787 (camici2023inbornerrorsof pages 8-9, camici2023inbornerrorsof pages 36-37); Mileti & Baleja, 2025, https://doi.org/10.3390/molecules30040839 (mileti2025theroleof pages 15-16, mileti2025theroleof pages 13-15) | CSF hypoxanthine reported ~4-fold above controls in review excerpt; HPRT-KO embryos/mice show developmental DA abnormalities (mileti2025theroleof pages 13-15, camici2023inbornerrorsof pages 8-9) |
| Neurochemical | Basal ganglia dopamine signaling is markedly deficient, with depletion of dopamine release/synthesis markers and compensatory receptor-level changes; dopamine deficiency is focal rather than due to gross global brain malformation. | Dopamine, TH, AADC, DOPAC, HVA, dopamine transporters, BH4/GTP | Striatal terminals, substantia nigra, basal ganglia | Vinokurov et al., 2023, https://doi.org/10.1007/s12035-023-03266-2 (vinokurov2023hprt1deficiencyinduces pages 1-2); Mileti & Baleja, 2025, https://doi.org/10.3390/molecules30040839 (mileti2025theroleof pages 13-15); Alsuwaidi & Ernst, 2025, https://doi.org/10.1159/000549247 (alsuwaidi2025onecarbonmetabolismand pages 3-4) | Review excerpts cite 70–90% dopamine reduction in basal ganglia; PET evidence indicates loss of dopamine release and depletion of dopamine-synthesis enzymes without cell loss in some studies (vinokurov2023hprt1deficiencyinduces pages 1-2, alsuwaidi2025onecarbonmetabolismand pages 3-4) |
| Systems / neurocircuit | Imaging supports network-level disease: white-matter and regional brain-volume losses, especially in basal ganglia/frontotemporal-limbic regions, plus characteristic metabolic network abnormalities on FDG-PET. | Glucose metabolism network changes; white matter connectivity | Basal ganglia, thalamus, brainstem, cerebellum, cortex | Tsagkaris et al., 2023, https://doi.org/10.1093/brain/awac439 (tsagkaris2023metabolicpatternsin pages 1-2); Mileti & Baleja, 2025, https://doi.org/10.3390/molecules30040839 (mileti2025theroleof pages 15-16) | FDG-PET: HPRT1 cases uniquely showed hypometabolism across all 9 cerebral regions in the pediatric dystonia cohort; classic LND review excerpt cites white matter ↓~26% and gray matter ↓~17% vs controls (tsagkaris2023metabolicpatternsin pages 1-2, mileti2025theroleof pages 15-16) |
| Clinical progression | Sequence is consistent with: congenital salvage defect → hyperuricemia/oxypurine excess and altered purine flux → early neurodevelopmental DA-circuit abnormalities → infantile motor delay/dystonia → later self-injurious behavior. | Hypoxanthine, xanthine, uric acid, dopamine-related pathways | Kidney/systemic metabolism; basal ganglia circuits | Camici et al., 2023, https://doi.org/10.3390/metabo13070787 (camici2023inbornerrorsof pages 8-9, camici2023inbornerrorsof pages 7-8); Alsuwaidi & Ernst, 2025, https://doi.org/10.1159/000549247 (alsuwaidi2025onecarbonmetabolismand pages 3-4); Baird-Daniel et al., 2023, https://doi.org/10.7759/cureus.37070 (bairddaniel2023singleelectrodedeepbrain pages 1-2) | Psychomotor delay often appears by 3–6 months; dystonia/signs between 4–12 months; self-injury usually begins after infancy, median ~2 years, often age 1–6 years (camici2023inbornerrorsof pages 8-9, alsuwaidi2025onecarbonmetabolismand pages 3-4, bairddaniel2023singleelectrodedeepbrain pages 1-2) |
| Real-world implementation / translational | Current therapy effectively treats urate overproduction (**allopurinol**) but not core neurobehavioral disease; DBS of the **GPi** can reduce dystonia/self-injury in refractory cases; gene correction with CRISPR base/prime editing restores HPRT function in human cells, supporting future causal therapy. | Allopurinol, GPi DBS, CRISPR base editors, prime editors, HPRT protein/IMP assay | Patients with LND; patient fibroblasts; HAP1/HEK293T cells | Baird-Daniel et al., 2023, https://doi.org/10.7759/cureus.37070 (bairddaniel2023singleelectrodedeepbrain pages 1-2); Jang et al., 2023, https://doi.org/10.1016/j.omtn.2023.02.009 (jang2023therapeuticgenecorrection pages 1-2, jang2023therapeuticgenecorrection pages 2-4, jang2023therapeuticgenecorrection pages 6-7, jang2023therapeuticgenecorrection pages 4-6, jang2023therapeuticgenecorrection pages 7-8) | DBS report adds 2 pediatric cases to prior literature of 14 cases; prime editing in patient fibroblasts improved to ~14% with restored HPRT protein/function, while HEK293T correction reached ~46.7–50% in optimized settings (bairddaniel2023singleelectrodedeepbrain pages 1-2, jang2023therapeuticgenecorrection pages 6-7, jang2023therapeuticgenecorrection pages 4-6, jang2023therapeuticgenecorrection pages 7-8) |
| Peripheral omics / biomarker layer | RBC multi-omics shows systemic consequences of HPRT deficiency: sharp loss of HPRT protein/GMP, altered glycolysis, membrane lipids, trace metals, redox/coagulation proteins, and incomplete biochemical normalization with allopurinol. | HPRT protein, GMP, hypoxanthine, inosine, PEP, pyruvate, PCs, SMs, acylcarnitines, Fe/Zn/Se/K | Red blood cells | Reisz et al., 2023, https://doi.org/10.3390/antiox12091699 (reisz2023redbloodcells pages 5-7, reisz2023redbloodcells pages 7-10, reisz2023redbloodcells pages 1-2, reisz2023redbloodcells pages 11-14) | 3 affected boys with novel p.S162N variant; serum uric acid ~5–6.5 mg/dL at diagnosis; 103/257 lipids and 147 proteins significantly altered; allopurinol normalized uric acid but incompletely reversed omics phenotype (reisz2023redbloodcells pages 5-7, reisz2023redbloodcells pages 11-14) |


*Table: This table condenses the provided evidence on Lesch–Nyhan syndrome from gene defect to metabolic, signaling, cellular, and neurocircuit consequences. It also highlights quantitative findings and current translational applications supported by the cited context IDs.*

## 14) Key mechanistic schematic (figure evidence)
A pathway figure from the 2024 physiologic-medium study explicitly depicts HGPRT deficiency, ZMP accumulation, AMPK/ADSL/mitochondrial consequences, and folate dependence (escuderoferruz2024anewphysiological media f6714473).

---

## Direct quote highlights (from retrieved evidence)
- FDG-PET signature: HPRT1 (Lesch–Nyhan) “**uniquely showed glucose hypometabolism across all nine cerebral regions**” in a pediatric dystonia FDG-PET cohort study (Tsagkaris et al., 2023; https://doi.org/10.1093/brain/awac439) (tsagkaris2023metabolicpatternsin pages 1-2).
- Brain urate scarcity: human brain uric acid reported as **“1% of total purines”** with HPRT high and XOR essentially absent (Sekine et al., 2024; https://doi.org/10.1016/j.jbc.2024.107524) (sekine2024significanceandamplification pages 2-4).

---

## Practical implications for therapeutic development
1. **Modeling conditions matter:** physiologic nutrient/folate conditions can reveal disease-relevant phenotypes and potential intervention points (folate sensitivity, AMPK-linked pathways) that may be missed in standard culture (escuderoferruz2024anewphysiological pages 1-2, escuderoferruz2024anewphysiological media f6714473).
2. **CNS-focused strategies must address salvage/energy demands:** human neuronal reliance on rapid salvage suggests that interventions increasing PRPP availability or modulating salvage flux could be mechanistically relevant, but this remains preclinical (sekine2024significanceandamplification pages 4-7, sekine2024significanceandamplification pages 12-14).
3. **Circuit-level interventions can be beneficial despite metabolic etiology:** GPi DBS can reduce dystonia/self-injury in refractory cases, consistent with basal ganglia network dysfunction (bairddaniel2023singleelectrodedeepbrain pages 1-2).
4. **Causal therapies are emerging but early:** CRISPR base/prime editing can restore HPRT function in patient fibroblasts; translating to brain requires improved delivery, editing efficiency, and safety evaluation (jang2023therapeuticgenecorrection pages 6-7, jang2023therapeuticgenecorrection pages 7-8).


References

1. (camici2023inbornerrorsof pages 7-8): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 21 citations.

2. (camici2023inbornerrorsof pages 8-9): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 21 citations.

3. (bairddaniel2023singleelectrodedeepbrain pages 1-2): Eliza Baird-Daniel, Adam Glaser, Scott Boop, Sharon Durfy, and Jason S Hauptman. Single-electrode deep brain stimulation of bilateral posterolateral globus pallidus internus in patients with medically resistant lesch-nyhan syndrome. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.37070, doi:10.7759/cureus.37070. This article has 1 citations.

4. (vinokurov2023hprt1deficiencyinduces pages 1-2): Andrey Y. Vinokurov, Vladislav O. Soldatov, Evgenia S. Seregina, Angelina I. Dolgikh, Pavel A. Tagunov, Andrey V. Dunaev, Marina Y. Skorkina, Alexey V. Deykin, and Andrey Y. Abramov. Hprt1 deficiency induces alteration of mitochondrial energy metabolism in the brain. Molecular Neurobiology, 60:3147-3157, Feb 2023. URL: https://doi.org/10.1007/s12035-023-03266-2, doi:10.1007/s12035-023-03266-2. This article has 23 citations and is from a peer-reviewed journal.

5. (tsagkaris2023metabolicpatternsin pages 1-2): Stavros Tsagkaris, Eric K C Yau, Verity McClelland, Apostolos Papandreou, Ata Siddiqui, Daniel E Lumsden, Margaret Kaminska, Eric Guedj, Alexander Hammers, and Jean-Pierre Lin. Metabolic patterns in brain 18f-fluorodeoxyglucose pet relate to aetiology in paediatric dystonia. Brain, 146:2512-2523, Nov 2023. URL: https://doi.org/10.1093/brain/awac439, doi:10.1093/brain/awac439. This article has 12 citations and is from a highest quality peer-reviewed journal.

6. (escuderoferruz2024anewphysiological pages 1-2): Paula Escudero-Ferruz, Neus Ontiveros, Claudia Cano-Estrada, Diane J. Sutcliffe, H. A. Jinnah, Rosa J. Torres, and José M. López. A new physiological medium uncovers biochemical and cellular alterations in lesch-nyhan disease fibroblasts. Molecular Medicine, Jan 2024. URL: https://doi.org/10.1186/s10020-023-00774-8, doi:10.1186/s10020-023-00774-8. This article has 11 citations and is from a peer-reviewed journal.

7. (sekine2024significanceandamplification pages 2-4): Mai Sekine, Megumi Fujiwara, Ken Okamoto, Kimiyoshi Ichida, Koji Nagata, Russ Hille, and Takeshi Nishino. Significance and amplification methods of the purine salvage pathway in human brain cells. Journal of Biological Chemistry, 300:107524, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107524, doi:10.1016/j.jbc.2024.107524. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (escuderoferruz2024anewphysiological media f6714473): Paula Escudero-Ferruz, Neus Ontiveros, Claudia Cano-Estrada, Diane J. Sutcliffe, H. A. Jinnah, Rosa J. Torres, and José M. López. A new physiological medium uncovers biochemical and cellular alterations in lesch-nyhan disease fibroblasts. Molecular Medicine, Jan 2024. URL: https://doi.org/10.1186/s10020-023-00774-8, doi:10.1186/s10020-023-00774-8. This article has 11 citations and is from a peer-reviewed journal.

9. (sekine2024significanceandamplification pages 4-7): Mai Sekine, Megumi Fujiwara, Ken Okamoto, Kimiyoshi Ichida, Koji Nagata, Russ Hille, and Takeshi Nishino. Significance and amplification methods of the purine salvage pathway in human brain cells. Journal of Biological Chemistry, 300:107524, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107524, doi:10.1016/j.jbc.2024.107524. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (sekine2024significanceandamplification pages 12-14): Mai Sekine, Megumi Fujiwara, Ken Okamoto, Kimiyoshi Ichida, Koji Nagata, Russ Hille, and Takeshi Nishino. Significance and amplification methods of the purine salvage pathway in human brain cells. Journal of Biological Chemistry, 300:107524, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107524, doi:10.1016/j.jbc.2024.107524. This article has 19 citations and is from a domain leading peer-reviewed journal.

11. (camici2023inbornerrorsof pages 36-37): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 21 citations.

12. (sekine2024significanceandamplification pages 1-2): Mai Sekine, Megumi Fujiwara, Ken Okamoto, Kimiyoshi Ichida, Koji Nagata, Russ Hille, and Takeshi Nishino. Significance and amplification methods of the purine salvage pathway in human brain cells. Journal of Biological Chemistry, 300:107524, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107524, doi:10.1016/j.jbc.2024.107524. This article has 19 citations and is from a domain leading peer-reviewed journal.

13. (reisz2023redbloodcells pages 5-7): Julie A. Reisz, Monika Dzieciatkowska, Daniel Stephenson, Fabia Gamboni, D. Holmes Morton, and Angelo D’Alessandro. Red blood cells from individuals with lesch–nyhan syndrome: multi-omics insights into a novel s162n mutation causing hypoxanthine-guanine phosphoribosyltransferase deficiency. Antioxidants, 12:1699, Aug 2023. URL: https://doi.org/10.3390/antiox12091699, doi:10.3390/antiox12091699. This article has 16 citations.

14. (alsuwaidi2025onecarbonmetabolismand pages 3-4): Shaima Alsuwaidi and Carl Ernst. One-carbon metabolism and midbrain dopaminergic cells in lesch-nyhan disease. Molecular Syndromology, pages 1-14, Nov 2025. URL: https://doi.org/10.1159/000549247, doi:10.1159/000549247. This article has 0 citations and is from a peer-reviewed journal.

15. (reisz2023redbloodcells pages 11-14): Julie A. Reisz, Monika Dzieciatkowska, Daniel Stephenson, Fabia Gamboni, D. Holmes Morton, and Angelo D’Alessandro. Red blood cells from individuals with lesch–nyhan syndrome: multi-omics insights into a novel s162n mutation causing hypoxanthine-guanine phosphoribosyltransferase deficiency. Antioxidants, 12:1699, Aug 2023. URL: https://doi.org/10.3390/antiox12091699, doi:10.3390/antiox12091699. This article has 16 citations.

16. (jang2023therapeuticgenecorrection pages 2-4): Gayoung Jang, Ha Rim Shin, Hyo-Sang Do, Jiyeon Kweon, Soojin Hwang, Soyoung Kim, Sun Hee Heo, Yongsub Kim, and Beom Hee Lee. Therapeutic gene correction for lesch-nyhan syndrome using crispr-mediated base and prime editing. Molecular Therapy - Nucleic Acids, 31:586-595, Mar 2023. URL: https://doi.org/10.1016/j.omtn.2023.02.009, doi:10.1016/j.omtn.2023.02.009. This article has 19 citations.

17. (jang2023therapeuticgenecorrection pages 6-7): Gayoung Jang, Ha Rim Shin, Hyo-Sang Do, Jiyeon Kweon, Soojin Hwang, Soyoung Kim, Sun Hee Heo, Yongsub Kim, and Beom Hee Lee. Therapeutic gene correction for lesch-nyhan syndrome using crispr-mediated base and prime editing. Molecular Therapy - Nucleic Acids, 31:586-595, Mar 2023. URL: https://doi.org/10.1016/j.omtn.2023.02.009, doi:10.1016/j.omtn.2023.02.009. This article has 19 citations.

18. (jang2023therapeuticgenecorrection pages 7-8): Gayoung Jang, Ha Rim Shin, Hyo-Sang Do, Jiyeon Kweon, Soojin Hwang, Soyoung Kim, Sun Hee Heo, Yongsub Kim, and Beom Hee Lee. Therapeutic gene correction for lesch-nyhan syndrome using crispr-mediated base and prime editing. Molecular Therapy - Nucleic Acids, 31:586-595, Mar 2023. URL: https://doi.org/10.1016/j.omtn.2023.02.009, doi:10.1016/j.omtn.2023.02.009. This article has 19 citations.

19. (alsuwaidi2025onecarbonmetabolismand pages 1-2): Shaima Alsuwaidi and Carl Ernst. One-carbon metabolism and midbrain dopaminergic cells in lesch-nyhan disease. Molecular Syndromology, pages 1-14, Nov 2025. URL: https://doi.org/10.1159/000549247, doi:10.1159/000549247. This article has 0 citations and is from a peer-reviewed journal.

20. (alsuwaidi2025onecarbonmetabolismand pages 2-3): Shaima Alsuwaidi and Carl Ernst. One-carbon metabolism and midbrain dopaminergic cells in lesch-nyhan disease. Molecular Syndromology, pages 1-14, Nov 2025. URL: https://doi.org/10.1159/000549247, doi:10.1159/000549247. This article has 0 citations and is from a peer-reviewed journal.

21. (mileti2025theroleof pages 15-16): Lauren N. Mileti and James D. Baleja. The role of purine metabolism and uric acid in postnatal neurologic development. Molecules, 30:839, Feb 2025. URL: https://doi.org/10.3390/molecules30040839, doi:10.3390/molecules30040839. This article has 15 citations.

22. (mileti2025theroleof pages 13-15): Lauren N. Mileti and James D. Baleja. The role of purine metabolism and uric acid in postnatal neurologic development. Molecules, 30:839, Feb 2025. URL: https://doi.org/10.3390/molecules30040839, doi:10.3390/molecules30040839. This article has 15 citations.

23. (jang2023therapeuticgenecorrection pages 1-2): Gayoung Jang, Ha Rim Shin, Hyo-Sang Do, Jiyeon Kweon, Soojin Hwang, Soyoung Kim, Sun Hee Heo, Yongsub Kim, and Beom Hee Lee. Therapeutic gene correction for lesch-nyhan syndrome using crispr-mediated base and prime editing. Molecular Therapy - Nucleic Acids, 31:586-595, Mar 2023. URL: https://doi.org/10.1016/j.omtn.2023.02.009, doi:10.1016/j.omtn.2023.02.009. This article has 19 citations.

24. (jang2023therapeuticgenecorrection pages 4-6): Gayoung Jang, Ha Rim Shin, Hyo-Sang Do, Jiyeon Kweon, Soojin Hwang, Soyoung Kim, Sun Hee Heo, Yongsub Kim, and Beom Hee Lee. Therapeutic gene correction for lesch-nyhan syndrome using crispr-mediated base and prime editing. Molecular Therapy - Nucleic Acids, 31:586-595, Mar 2023. URL: https://doi.org/10.1016/j.omtn.2023.02.009, doi:10.1016/j.omtn.2023.02.009. This article has 19 citations.

25. (reisz2023redbloodcells pages 7-10): Julie A. Reisz, Monika Dzieciatkowska, Daniel Stephenson, Fabia Gamboni, D. Holmes Morton, and Angelo D’Alessandro. Red blood cells from individuals with lesch–nyhan syndrome: multi-omics insights into a novel s162n mutation causing hypoxanthine-guanine phosphoribosyltransferase deficiency. Antioxidants, 12:1699, Aug 2023. URL: https://doi.org/10.3390/antiox12091699, doi:10.3390/antiox12091699. This article has 16 citations.

26. (reisz2023redbloodcells pages 1-2): Julie A. Reisz, Monika Dzieciatkowska, Daniel Stephenson, Fabia Gamboni, D. Holmes Morton, and Angelo D’Alessandro. Red blood cells from individuals with lesch–nyhan syndrome: multi-omics insights into a novel s162n mutation causing hypoxanthine-guanine phosphoribosyltransferase deficiency. Antioxidants, 12:1699, Aug 2023. URL: https://doi.org/10.3390/antiox12091699, doi:10.3390/antiox12091699. This article has 16 citations.