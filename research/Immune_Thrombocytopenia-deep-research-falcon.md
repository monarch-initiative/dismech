---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:47:01.117243'
end_time: '2025-12-18T09:55:17.914051'
duration_seconds: 496.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immune Thrombocytopenia
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Immune Thrombocytopenia
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Immune Thrombocytopenia**.
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
- **Disease Name:** Immune Thrombocytopenia
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Immune Thrombocytopenia**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Immune Thrombocytopenia (ITP)
- MONDO ID: MONDO:0005393
- Category: Autoimmune

Pathophysiology overview (current understanding)
Primary immune thrombocytopenia is an autoimmune cytopenia caused by both increased peripheral destruction of platelets and impaired megakaryopoiesis/platelet production. Central mechanisms include IgG autoantibodies against platelet glycoproteins (predominantly GPIIb/IIIa and GPIb‑IX) that drive Fcγ receptor–dependent phagocytosis, complement deposition, Fc‑independent desialylation with hepatic clearance, and direct platelet apoptosis; dysregulated T- and B-cell responses sustain loss of tolerance; and intrinsic megakaryocyte (MK) stress and apoptosis/autophagy/mitochondrial dysfunction reduce production (Discover Medicine, 2024; IJMS, 2024) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, mititelu2024currentunderstandingof pages 1-2).

1) Core Pathophysiology
- Autoantibodies and FcγR-mediated clearance: Opsonizing IgG1/IgG3 autoantibodies to GPIIb/IIIa and GPIb‑IX mediate platelet clearance by splenic/hepatic macrophages via Fcγ receptors with downstream SYK/BTK signaling. Rapid responses to IVIG and efficacy of Syk/BTK inhibitors support this pathway (2024 review) (URL: https://doi.org/10.1007/s44337-024-00008-8; published July 2024) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Fc‑independent desialylation and hepatic Ashwell–Morell receptor (AMR) clearance: Anti‑GPIb/IX can induce neuraminidase‑dependent desialylation, exposing terminal galactose recognized by hepatic AMR (ASGR1/ASGR2), leading to Fc‑independent removal. “Anti‑GPIb antibodies induce platelet desialylation … diverting clearance to the liver through the Ashwell–Morell receptor (AMR)” (URL: https://doi.org/10.3390/hematolrep16020021; April 2024) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5); also demonstrated in contemporary reviews and mechanistic studies (URL: https://doi.org/10.1007/s44337-024-00008-8; July 2024; URL: https://doi.org/10.1007/s00277-024-05999-z; Sept 2024) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, sun2024theeffectsof pages 1-5).
- Complement deposition on platelets: A substantial subset of patients shows classical pathway activation on platelets (C3/C4/C9), enhancing opsonization and lysis; complement targeting is therefore under investigation (URL: https://doi.org/10.1007/s00277-024-05999-z; Sept 2024; URL: https://doi.org/10.3390/hematolrep16020021; April 2024) (sun2024theeffectsof pages 1-5, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Platelet apoptosis independent of complement: Patient IgG can directly induce phosphatidylserine exposure, mitochondrial depolarization, and platelet-derived particle formation in complement-depleted systems, supporting non-complement apoptosis as an additional mechanism (Ann Hematol 2024) (URL: https://doi.org/10.1007/s00277-024-05999-z; Sept 2024) (sun2024theeffectsof pages 1-5).
- B- and T-cell dysregulation: Elevated BAFF and reduced/altered Breg phenotypes support autoreactive B-cell survival; T-cell alterations include reduced Treg activity, expansion of Th17/Tfh, and cytotoxic CD8+ T cells that can lyse platelets and attack MKs (2024 reviews) (URLs: https://doi.org/10.1007/s44337-024-00008-8; https://doi.org/10.15167/bartalucci-giulia_phd2024-11-26) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, bartalucci2024biologicalandclinical pages 6-11).
- Impaired megakaryopoiesis and MK apoptosis/mitochondria/autophagy: Autoantibodies, inflammatory cytokines, and intrinsic stress disrupt MK maturation and thrombopoiesis; MK apoptosis (caspase-3 activation, Bcl-2 family shifts), mitochondrial dysfunction, and altered autophagy contribute (2024 reviews) (URLs: https://doi.org/10.3390/hematolrep16020021; https://doi.org/10.3390/ijms25042163) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, mititelu2024currentunderstandingof pages 1-2).

2) Key Molecular Players
- Genes/Proteins (HGNC): ITGA2B/ITGB3 (GPIIb/IIIa), GP1BA/GP1BB/GP9 (GPIb‑IX), FCGR2A/FCGR3A, SYK, BTK, NEU1, ASGR1/ASGR2 (AMR), C1QA/C3/C4/C5, FCGRT (FcRn), BAFF (TNFSF13B), FOXP3 (Treg), IL17A, BCL6/PDCD1 (Tfh/PD‑1), CASP3, BCL2 family (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5, mititelu2024currentunderstandingof pages 1-2, bartalucci2024biologicalandclinical pages 6-11).
- Chemical Entities (CHEBI/Drugs): IVIG; fostamatinib (SYK inhibitor); rilzabrutinib (BTK inhibitor); HMPL‑523 (Syk inhibitor); neuraminidase inhibitors (e.g., oseltamivir); FcRn antagonists (efgartigimod, rozanolixizumab, nipocalimab) (ali2023safetyandefficacy pages 1-2, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, mititelu2024currentunderstandingof pages 1-2, yan2024immunethrombocytopeniaa pages 1-3).
- Cell Types (CL): Splenic/liver macrophages; B cells (Breg); Treg (FOXP3+), Th17, Tfh; CD8+ cytotoxic T cells; megakaryocytes; platelets (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, bartalucci2024biologicalandclinical pages 6-11, mititelu2024currentunderstandingof pages 1-2).
- Anatomical Locations (UBERON): Spleen, liver (hepatocyte AMR), bone marrow (megakaryopoiesis) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).

3) Biological Processes (GO) disrupted
- Fc receptor signaling pathway; phagocytosis, engulfment (FcγR–SYK/BTK dependent) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Protein desialylation; receptor-mediated endocytosis in hepatocytes via AMR; carbohydrate recognition (lectin-mediated clearance) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Complement activation, classical pathway; opsonization (sun2024theeffectsof pages 1-5, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Negative regulation of B cell tolerance; positive regulation of B-cell survival by BAFF (mititelu2024currentunderstandingof pages 1-2).
- Regulation of T cell differentiation (Treg, Th17, Tfh); cytotoxic T cell–mediated killing (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, bartalucci2024biologicalandclinical pages 6-11).
- Megakaryocyte differentiation; regulation of thrombopoiesis; intrinsic apoptotic signaling; mitochondrial membrane potential regulation; macroautophagy (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, mititelu2024currentunderstandingof pages 1-2).
- IgG catabolic process via FcRn (yan2024immunethrombocytopeniaa pages 1-3, mititelu2024currentunderstandingof pages 1-2).

4) Cellular Components (GO)
- Platelet plasma membrane (GPIIb/IIIa; GPIb‑IX) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Phagocytic vesicle; lysosome in macrophages (FcγR-mediated clearance) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Hepatocyte plasma membrane AMR complex (ASGR1/2) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Mitochondria in platelets/MKs; autophagosome (mititelu2024currentunderstandingof pages 1-2).
- Complement components on platelet surface (C3/C4/C9) (sun2024theeffectsof pages 1-5).
- FcRn compartment (endosome/lysosome interface) (yan2024immunethrombocytopeniaa pages 1-3, mititelu2024currentunderstandingof pages 1-2).

5) Disease Progression (sequence of events)
- Trigger/loss of tolerance: Genetic/immune dysregulation and/or infectious triggers (e.g., H. pylori) initiate autoreactivity (URL: https://doi.org/10.1007/s44337-024-00008-8; July 2024) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Autoantibody generation and immune effector amplification: BAFF elevation sustains autoreactive B cells; T cell subset imbalance (low Treg; expanded Th17/Tfh) provides help; CD8+ CTLs directly injure platelets/MKs (URLs: https://doi.org/10.3390/ijms25042163; Feb 2024; https://doi.org/10.15167/bartalucci-giulia_phd2024-11-26; Nov 2024) (mititelu2024currentunderstandingof pages 1-2, bartalucci2024biologicalandclinical pages 6-11).
- Platelet destruction: FcγR‑mediated phagocytosis; complement opsonization/lysis; antibody‑induced desialylation with hepatic AMR clearance; complement‑independent apoptosis with mitochondrial depolarization/PS exposure (URLs: https://doi.org/10.1007/s44337-024-00008-8; https://doi.org/10.3390/hematolrep16020021; https://doi.org/10.1007/s00277-024-05999-z) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5).
- Impaired production: Autoantibodies and inflammatory milieu inhibit MK maturation, with apoptosis/mitochondrial/autophagy dysregulation lowering platelet output (URLs: https://doi.org/10.3390/hematolrep16020021; https://doi.org/10.3390/ijms25042163) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, mititelu2024currentunderstandingof pages 1-2).
- Clinical manifestation: Thrombocytopenia with mucocutaneous bleeding, occasionally severe hemorrhage; in many adults, chronic course with fluctuating disease activity (URLs: https://doi.org/10.3390/ijms25042163; Feb 2024) (mititelu2024currentunderstandingof pages 1-2).

6) Phenotypic Manifestations (HP terms)
- Thrombocytopenia (HP:0001873); Petechiae (HP:0000967); Purpura (HP:0000979); Epistaxis (HP:0000421); Gingival bleeding (HP:0000210); Menorrhagia (HP:0000132); Intracranial hemorrhage (rare; HP:0002170) (mititelu2024currentunderstandingof pages 1-2, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).

Key statistics and data (recent)
- Autoantibody detection: “Serum antibody assays detect antibodies in only ~60% of patients,” highlighting non-antibody mechanisms and technical limitations (Discover Medicine, 2024; URL: https://doi.org/10.1007/s44337-024-00008-8) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Complement involvement: Platelet-associated complement (e.g., C3/C4/C9) has been reported in a substantial subset—on the order of about half in compiled reports—supporting a classical pathway role (Ann Hematol, 2024; URL: https://doi.org/10.1007/s00277-024-05999-z; Hematology Reports, 2024; URL: https://doi.org/10.3390/hematolrep16020021) (sun2024theeffectsof pages 1-5, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Syk/BTK inhibitor outcomes (clinical evidence synthesis): In a 2023 systematic review of clinical trials (n=255 adults with relapsed/refractory ITP): fostamatinib achieved stable response 17.8% (18/101) and overall response 42.5% (43/101) vs placebo SR 2% (1/49), OR 14% (7/49); rilzabrutinib SR 28% (17/60); HMPL‑523 (Syk) SR 25% (5/20), OR 55% (11/20) (URL: https://doi.org/10.3390/jox13010005; Jan 2023) (ali2023safetyandefficacy pages 1-2).
- Chronicity and burden: “Up to 75% of adult patients with ITP may develop chronicity,” underscoring long-term dysregulation (IJMS, 2024; URL: https://doi.org/10.3390/ijms25042163; Feb 2024) (mititelu2024currentunderstandingof pages 1-2).
- H. pylori association (pediatrics mixed; adults stronger in certain regions): Some cohorts show platelet recovery after eradication; others show no effect, reflecting geographic/age heterogeneity (summary in 2024 review) (URL: https://doi.org/10.1007/s44337-024-00008-8; July 2024) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).

Representative quotes (verbatim)
- “Anti‑GPIIb/IIIa antibodies mediate Fc‑dependent clearance in the spleen via macrophage Fc receptors and phagocytosis.” (Discover Medicine, 2024; https://doi.org/10.1007/s44337-024-00008-8) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4)
- “Anti‑GPIb antibodies induce platelet desialylation … diverting clearance to the liver through the Ashwell–Morell receptor (AMR).” (Hematology Reports, 2024; https://doi.org/10.3390/hematolrep16020021) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5)
- “Complement‑independent, autoantibody‑induced apoptosis of platelets” contributes to ITP pathogenesis (Annals of Hematology, 2024; https://doi.org/10.1007/s00277-024-05999-z) (sun2024theeffectsof pages 1-5)

Recent developments and latest research (2023–2024 priority)
- Mechanistic consolidation: 2024 reviews integrate the dual‑mechanism paradigm of FcγR‑phagocytosis and Fc‑independent AMR clearance, with explicit therapeutic hypotheses (neuraminidase inhibition, FcRn blockade, complement inhibition) (July 2024; https://doi.org/10.1007/s44337-024-00008-8) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Platelet apoptosis without complement: 2024 Annals of Hematology provides experimental evidence that purified ITP IgG can provoke platelet apoptosis and microvesiculation even when complement is removed, refining the mechanistic map (Sept 2024; https://doi.org/10.1007/s00277-024-05999-z) (sun2024theeffectsof pages 1-5).
- Therapeutic targeting of immune pathways: Quantitative synthesis shows clinically meaningful response rates for Syk and BTK inhibition in refractory ITP; these trials mechanistically validate FcγR–SYK/BTK pathways (Jan 2023; https://doi.org/10.3390/jox13010005) (ali2023safetyandefficacy pages 1-2).
- FcRn as a pathophysiologic and therapeutic axis: 2024 reviews detail FcRn’s role in IgG homeostasis and the rationale for FcRn antagonists to rapidly reduce pathogenic IgG, with multiple agents in development for ITP (URLs: https://doi.org/10.1007/s44337-024-00040-8; https://doi.org/10.3390/ijms25042163) (yan2024immunethrombocytopeniaa pages 1-3, mititelu2024currentunderstandingof pages 1-2).

Current applications and real-world implementations
- Syk inhibition (fostamatinib) is approved for chronic adult ITP and improves platelet counts by blocking FcγR–SYK–mediated phagocytosis; pooled trial data show OR ~42.5% and SR ~17.8% in refractory populations; safety profile includes hypertension and diarrhea among serious AEs (Jan 2023; https://doi.org/10.3390/jox13010005) (ali2023safetyandefficacy pages 1-2).
- BTK inhibition (rilzabrutinib) has shown clinically meaningful activity in phase 1/2; durable responses reported with acceptable tolerability in longer-term follow-up (Blood Advances 2024; URL: https://doi.org/10.1182/bloodadvances.2023012044) (ali2023safetyandefficacy pages 1-2, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4). Note: quantitative long-term results in extension follow-up are supportive but not detailed in the evidence set cited here.
- FcRn inhibitors (efgartigimod, rozanolixizumab, nipocalimab) are being evaluated in ITP to lower pathogenic IgG rapidly; mechanistic rationale is strong and early clinical experience in IgG‑mediated diseases is favorable (2024 reviews) (URLs: https://doi.org/10.1007/s44337-024-00040-8; https://doi.org/10.3390/ijms25042163; https://doi.org/10.1007/s40268-024-00490-6) (yan2024immunethrombocytopeniaa pages 1-3, mititelu2024currentunderstandingof pages 1-2).
- H. pylori eradication is implemented in selected patients with regional enrichment of responders; heterogeneity remains, especially in pediatrics (2024 review) (URL: https://doi.org/10.1007/s44337-024-00008-8) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).

Expert opinions and analysis from authoritative sources
- Contemporary reviews emphasize ITP heterogeneity encompassing antibody-dependent clearance, complement activity, Fc-independent desialylation/AMR, and T‑/B‑cell dysregulation; they advocate mechanism-guided therapy selection, including FcRn antagonism and complement targeting for appropriate phenotypes (2024; URLs as above) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, mititelu2024currentunderstandingof pages 1-2, yan2024immunethrombocytopeniaa pages 1-3).

Embedded mechanistic summary table
| Mechanism | Key molecules (HGNC / CHEBI) | Core finding | Therapeutic implications | Key sources (Year; DOI/URL) |
|---|---|---|---|---|
| FcγR-mediated phagocytosis (Fc-dependent) | FCGR2A, FCGR3A, SYK, BTK; IgG (pathogenic IgG1/IgG3); fostamatinib (SYK inhibitor), rilzabrutinib (BTK inhibitor) | Autoantibody (IgG) opsonization of platelets promotes splenic/hepatic macrophage phagocytosis via Fcγ receptors with downstream SYK/BTK signaling driving platelet clearance. | Targeting SYK or BTK reduces FcR-driven phagocytosis and raises platelet counts in refractory ITP. | 2023–2024; https://doi.org/10.3390/jox13010005 (ali2023safetyandefficacy pages 1-2), https://doi.org/10.1007/s44337-024-00008-8 (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4) |
| Fc-independent desialylation → hepatic AMR clearance | GP1BA/GP1BB/GP9 (GPIb-IX complex), NEU1 (neuraminidase), ASGR1 / ASGR2 (Ashwell–Morell receptor); oseltamivir (CHEBI:50142) | Anti‑GPIb/IX antibodies can trigger platelet desialylation (loss of sialic acid), exposing galactose residues that are recognized by hepatic ASGR1/ASGR2 and cleared independently of FcγRs. | In selected patients neuraminidase inhibition or therapies addressing desialylation may mitigate Fc‑independent platelet loss. | 2024; https://doi.org/10.1007/s44337-024-00008-8 (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4), 2024; https://doi.org/10.1007/s00277-024-05999-z (sun2024theeffectsof pages 1-5) |
| Complement activation on platelets | C1q, C3, C4, C5; complement inhibitors (e.g., C1s inhibitors) | Autoantibodies can fix classical complement on platelets (C3/C4/C9 deposition) in a substantial subset (~~half reported), promoting opsonization, membrane damage and clearance. | Complement blockade (C1s/C3/C5 targeting) is a rational approach for complement‑driven ITP phenotypes under investigation. | 2024; https://doi.org/10.1007/s00277-024-05999-z (sun2024theeffectsof pages 1-5), 2024; https://doi.org/10.3390/hematolrep16020021 (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5) |
| T cell dysregulation (Treg/Th17/Tfh; CD8+ cytotoxicity) | FOXP3 (Treg), IL17A (Th17), BCL6 / PDCD1 (Tfh / PD‑1), CD8A | Loss of peripheral tolerance with dysfunctional/low Treg activity, expanded Th17/Tfh subsets and autoreactive CD8+ T cells provides B‑cell help and direct CTL-mediated platelet and megakaryocyte damage. | Immunomodulation of T cell subsets or checkpoint pathways may benefit patients with prominent T‑cell–driven disease. | 2024; https://doi.org/10.1007/s44337-024-00008-8 (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4), 2024; https://doi.org/10.15167/bartalucci-giulia_phd2024-11-26 (bartalucci2024biologicalandclinical pages 6-11) |
| Impaired megakaryopoiesis; apoptosis / mitochondria / autophagy | PTGS2 (COX‑2), CASP3 (caspase‑3), BCL2 family members; mitochondrial regulators | Autoantibodies, inflammatory cytokines and intrinsic MK stress promote impaired megakaryocyte maturation, increased apoptosis/mitochondrial dysfunction and altered autophagy, reducing platelet production. | TPO‑receptor agonists and approaches that protect MK survival or restore mitochondrial/autophagy balance may improve thrombopoiesis. | 2024; https://doi.org/10.3390/hematolrep16020021 (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5), 2024; https://doi.org/10.3390/ijms25042163 (mititelu2024currentunderstandingof pages 1-2) |
| FcRn / IgG homeostasis | FCGRT (FcRn), IgG; efgartigimod, rozanolixizumab, nipocalimab | FcRn rescues IgG from catabolism; FcRn blockade accelerates IgG clearance, lowering pathogenic autoantibody levels and thereby improving antibody‑mediated disease activity. | FcRn inhibitors (biologics/small proteins) are a promising strategy to rapidly reduce pathogenic IgG in ITP and are under clinical evaluation. | 2024; https://doi.org/10.1007/s44337-024-00040-8 (yan2024immunethrombocytopeniaa pages 1-3), 2024; https://doi.org/10.3390/ijms25042163 (mititelu2024currentunderstandingof pages 1-2) |
| Helicobacter pylori–associated ITP (infectious trigger) | H. pylori virulence factors (CagA, VacA); host molecular mimicry / cytokines | In some patients H. pylori infection associates with ITP and platelet recovery after eradication (variable by population and age), consistent with infection‑triggered autoimmunity or molecular mimicry. | Test for and treat H. pylori in selected ITP patients—eradication can produce durable platelet responses in responders. | 2024; https://doi.org/10.1007/s44337-024-00008-8 (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4), 2024; https://doi.org/10.15167/bartalucci-giulia_phd2024-11-26 (bartalucci2024biologicalandclinical pages 6-11) |


*Table: Compact 2023–2024 evidence summary of core ITP mechanisms linking molecular players to clinical/therapeutic implications, with DOI/URL citations for each mechanism.*

Ontology-ready annotations (examples)
- Genes/Proteins (HGNC): ITGA2B; ITGB3; GP1BA; GP1BB; GP9; FCGR2A; FCGR3A; SYK; BTK; NEU1; ASGR1; ASGR2; C1QA; C3; C4A; C5; FCGRT; TNFSF13B (BAFF); FOXP3; IL17A; BCL6; PDCD1; CASP3 (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5, mititelu2024currentunderstandingof pages 1-2, bartalucci2024biologicalandclinical pages 6-11).
- Biological Process (GO): Fc receptor signaling pathway; phagocytosis, engulfment; complement activation, classical pathway; protein desialylation; receptor-mediated endocytosis; regulation of B cell tolerance; regulation of T cell differentiation; megakaryocyte differentiation; regulation of thrombopoiesis; intrinsic apoptotic signaling pathway; mitochondrial membrane potential; macroautophagy; IgG catabolic process via FcRn (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5, mititelu2024currentunderstandingof pages 1-2).
- Cellular Component (GO): platelet membrane; phagocytic vesicle; hepatocyte plasma membrane (ASGR complex); mitochondrion; autophagosome; complement component C3 on platelet surface; endolysosomal compartment (FcRn) (sun2024theeffectsof pages 1-5, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, yan2024immunethrombocytopeniaa pages 1-3).
- Cell Types (CL): macrophage; B cell (Breg); Treg; Th17 cell; Tfh cell; CD8-positive, alpha-beta T cell; megakaryocyte; platelet (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, bartalucci2024biologicalandclinical pages 6-11).
- Anatomical Locations (UBERON): spleen; liver; hepatocyte; bone marrow (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Chemical Entities (CHEBI): immunoglobulin G; fostamatinib; rilzabrutinib; HMPL‑523; oseltamivir; efgartigimod; rozanolixizumab; nipocalimab (ali2023safetyandefficacy pages 1-2, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, mititelu2024currentunderstandingof pages 1-2, yan2024immunethrombocytopeniaa pages 1-3).
- Phenotypes (HPO): thrombocytopenia (HP:0001873); petechiae (HP:0000967); purpura (HP:0000979); epistaxis (HP:0000421); gingival bleeding (HP:0000210); menorrhagia (HP:0000132); intracranial hemorrhage (HP:0002170) (mititelu2024currentunderstandingof pages 1-2, tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).

Evidence items with PMIDs/DOIs/URLs (publication dates)
- Yan X, et al. Immune thrombocytopenia: pathogenesis and current treatment. Discover Medicine. Sept 2024. DOI: 10.1007/s44337-024-00040-8 (URL: https://doi.org/10.1007/s44337-024-00040-8) (yan2024immunethrombocytopeniaa pages 1-3).
- Tungjitviboonkun S, Bumrungratanayos N. ITP: historical perspectives, pathophysiology, and treatment advances. Discover Medicine. July 2024. DOI: 10.1007/s44337-024-00008-8 (URL: https://doi.org/10.1007/s44337-024-00008-8) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4).
- Martínez-Carballeira D, et al. Pathophysiology… Hematology Reports. April 2024. DOI: 10.3390/hematolrep16020021 (URL: https://doi.org/10.3390/hematolrep16020021) (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5).
- Sun L, et al. Complement-independent, autoantibody-induced apoptosis of platelets in ITP. Ann Hematol. Sept 2024. DOI: 10.1007/s00277-024-05999-z (URL: https://doi.org/10.1007/s00277-024-05999-z) (sun2024theeffectsof pages 1-5).
- Ali MA, et al. Safety and efficacy of Syk and BTK inhibitors in ITP: a systematic review. J Xenobiotics. Jan 2023. DOI: 10.3390/jox13010005 (URL: https://doi.org/10.3390/jox13010005) (ali2023safetyandefficacy pages 1-2).
- Mititelu A, et al. Current understanding of ITP: pathogenesis and treatment options. IJMS. Feb 2024. DOI: 10.3390/ijms25042163 (URL: https://doi.org/10.3390/ijms25042163) (mititelu2024currentunderstandingof pages 1-2).
- Bartalucci G. Biological and clinical picture in ITP: single-centre cross-sectional data. Nov 2024. DOI: 10.15167/bartalucci-giulia_phd2024-11-26 (URL: https://doi.org/10.15167/bartalucci-giulia_phd2024-11-26) (bartalucci2024biologicalandclinical pages 6-11).

Notes and limitations
- Reported frequencies (e.g., exact percentages by antibody specificity and exact complement-positive rates) vary by assay; the contemporary sources above provide qualitative-to-semiquantitative ranges but not a single definitive prevalence figure. Where explicit percentages are unavailable in the extracted evidence, ranges are described conservatively (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5).

Conclusion
Primary ITP arises from a convergence of antibody-driven platelet clearance (both Fc‑dependent and Fc‑independent), complement fixation, T‑/B‑cell dysregulation, and impaired megakaryopoiesis with intrinsic cell-stress programs (apoptosis, mitochondrial dysfunction, autophagy). These convergent mechanisms are now actionable, with SYK/BTK inhibitors, FcRn antagonists, TPO‑receptor agonists, and emerging complement-directed strategies enabling mechanism-guided therapy and rational sequencing in clinical practice (2023–2024 literature) (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4, ali2023safetyandefficacy pages 1-2, yan2024immunethrombocytopeniaa pages 1-3, martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5, sun2024theeffectsof pages 1-5).

References

1. (tungjitviboonkun2024immunethrombocytopenia(itp) pages 2-4): Songphol Tungjitviboonkun and Naharuthai Bumrungratanayos. Immune thrombocytopenia (itp): historical perspectives, pathophysiology, and treatment advances. Discover Medicine, Jul 2024. URL: https://doi.org/10.1007/s44337-024-00008-8, doi:10.1007/s44337-024-00008-8. This article has 8 citations.

2. (mititelu2024currentunderstandingof pages 1-2): Alina Mititelu, Minodora-Cezarina Onisâi, Adrian Roșca, and Ana Maria Vlădăreanu. Current understanding of immune thrombocytopenia: a review of pathogenesis and treatment options. International Journal of Molecular Sciences, 25:2163, Feb 2024. URL: https://doi.org/10.3390/ijms25042163, doi:10.3390/ijms25042163. This article has 70 citations and is from a poor quality or predatory journal.

3. (martinezcarballeira2024pathophysiologyclinicalmanifestations pages 4-5): Daniel Martínez-Carballeira, Ángel Bernardo, Alberto Caro, Inmaculada Soto, and Laura Gutiérrez. Pathophysiology, clinical manifestations and diagnosis of immune thrombocytopenia: contextualization from a historical perspective. Hematology Reports, 16:204-219, Apr 2024. URL: https://doi.org/10.3390/hematolrep16020021, doi:10.3390/hematolrep16020021. This article has 24 citations and is from a poor quality or predatory journal.

4. (sun2024theeffectsof pages 1-5): Lin Sun, Yichen Zhang, Ping Chen, Nan Jiang, Qi Feng, Shuqian Xu, Jun Peng, and Zi Sheng. The effects of complement-independent, autoantibody-induced apoptosis of platelets in immune thrombocytopenia (itp). Annals of hematology, 103:5157-5168, Sep 2024. URL: https://doi.org/10.1007/s00277-024-05999-z, doi:10.1007/s00277-024-05999-z. This article has 2 citations and is from a peer-reviewed journal.

5. (bartalucci2024biologicalandclinical pages 6-11): GIULIA BARTALUCCI. Biological and clinical picture in immune thrombocytopenia (itp) patients: prospective cross-sectional data on a single centre population. Other, Nov 2024. URL: https://doi.org/10.15167/bartalucci-giulia\_phd2024-11-26, doi:10.15167/bartalucci-giulia\_phd2024-11-26. This article has 0 citations.

6. (ali2023safetyandefficacy pages 1-2): Muhammad Ashar Ali, Muhammad Yasir Anwar, Wajeeha Aiman, Gurneel Dhanesar, Zainab Omar, Mohammad Hamza, Maha Zafar, Harish Kumar Rengarajan, and Michael Maroules. Safety and efficacy of tyrosine kinase inhibitors in immune thrombocytopenic purpura: a systematic review of clinical trials. Journal of Xenobiotics, 13:29-41, Jan 2023. URL: https://doi.org/10.3390/jox13010005, doi:10.3390/jox13010005. This article has 11 citations.

7. (yan2024immunethrombocytopeniaa pages 1-3): Xiang Yan, Zhangjun Yun, Lu Tian, Hou Li, Shaodan Tian, and Jun Wang. Immune thrombocytopenia: a review of pathogenesis and current treatment. Discover Medicine, Sep 2024. URL: https://doi.org/10.1007/s44337-024-00040-8, doi:10.1007/s44337-024-00040-8. This article has 4 citations.