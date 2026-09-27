# An AOP Network Linking Impaired T-cell Dependent Antibody Response (TDAR) to Increased Susceptibility to Infection

## Summary

The **T-cell dependent antibody response (TDAR)** is a functional immunotoxicology endpoint that measures the coordinated cooperation of antigen-presenting cells, CD4+ T-helper cells, and B cells required to mount an antigen-specific antibody response. This investigation assembled, from the AOP-Wiki, the OECD scientific review of AOP 277, the 2026 polycyclic aromatic compound (PAC) study, and the broader immunotoxicology literature, a **coherent Adverse Outcome Pathway (AOP) network** in which multiple distinct chemical molecular initiating events (MIEs) converge onto a single shared Adverse Outcome — **impaired TDAR** — which in turn is causally linked to **increased susceptibility to infection**.

Three curated AOP-Wiki pathways terminate at impaired TDAR: **AOP 154** (Inhibition of Calcineurin Activity), **AOP 277** (Impaired IL-1R1 Signaling), and **AOP 315** (Inhibition of JAK3). All three funnel through shared downstream Key Events — suppression of the T-cell cytokines IL-2 and IL-4, suppression of T-cell activation, and reduced B-cell antibody-forming-cell output — into the same terminal node, and the final Key Event Relationship into impaired TDAR is rated **High evidence / High quantitative understanding** in every pathway. A fourth branch — **Aryl hydrocarbon receptor (AhR) activation** by PACs and dioxin-like compounds — is mechanistically supported by the literature and converges on the identical downstream events, anchoring the network to a real chemical class of regulatory concern. A fifth bridging pathway, **AOP 14** (Glucocorticoid Receptor activation leading to increased disease susceptibility), shares the NF-κB inhibition and immune-suppression hub nodes and directly connects the network to the "increased disease/infection susceptibility" outcome.

The causal linkage from impaired TDAR to increased infection susceptibility is supported by **seven independent evidence streams**: a near-linear quantitative immune-to-host-resistance relationship derived from the NTP immunotoxicology database (Luster et al. 1993); a quantified dose-response bridge in the AOP 277 review (a ~6.4% decrease in ConA-induced T-cell proliferation ≈ 10% increased risk of *Listeria* infection); mechanistic evidence that the AOP 277 MIE (IL-1R1 deficiency) directly causes susceptibility to *Mycobacterium tuberculosis*; clinical evidence that calcineurin-inhibitor immunosuppression (the AOP 154 MIE) drives a major infection burden and mortality in transplant patients; regulatory endorsement of TDAR as the first-line functional immunosuppression assay with proven inter-laboratory reproducibility; the embedding of a TDAR readout within host-resistance challenge models; and a current in vivo chemical anchor showing benzo[a]pyrene suppresses TDAR by ~75% — the most sensitive endpoint, 33× more sensitive than liver weight. Every Key Event in the network maps to a defined in vitro or in vivo assay, making the network a practical scaffold for New Approach Methodologies (NAMs) that support the 3Rs (Replacement, Reduction, Refinement of animal testing).

---

## Key Findings

### Three AOP-Wiki pathways converge on impaired TDAR (F001)

Retrieval of the full AOP structures from the AOP-Wiki JSON API confirmed that three curated pathways share a common terminal Adverse Outcome:

| AOP | Title | MIE | Intermediate Key Events | Adverse Outcome |
|-----|-------|-----|--------------------------|-----------------|
| **154** | Inhibition of Calcineurin Activity → Impaired TDAR | KE980 Calcineurin inhibition | KE979 NFAT nuclear localization interference → KE981 reduced NFAT/AP-1 complex → KE1202 suppression of IL-2/IL-4 | **AO984 Impaired TDAR** |
| **277** | Impaired IL-1R1 Signaling → Impaired TDAR | KE1700 Impaired IL-1R1 signaling | KE202 NF-κB inhibition → KE1702 suppression of T-cell activation | **AO984 Impaired TDAR** |
| **315** | Inhibition of JAK3 → Impaired TDAR | KE1715 JAK3 inhibition | KE1716 blocked STAT5 phosphorylation → KE1717 suppressed STAT5–promoter binding → KE1718 suppression of IL-4 | **AO1719 Impaired TDAR** |

AOPs 154 and 277 share the **identical** Adverse Outcome node (event 984), while AOP 315 uses a distinct but equivalent node (1719). Critically, AOPs 154 and 315 **both** include an IL-4 suppression Key Event, providing a second convergence point within the network. This establishes that chemically diverse initiating perturbations — a phosphatase inhibition, a cytokine-receptor signaling defect, and a kinase inhibition — all channel into the same functional immune outcome.

{{figure:tdar_aop_network.png|caption=Integrated AOP network showing four convergent branches (calcineurin inhibition, JAK3 inhibition, impaired IL-1R1 signaling, and AhR activation) funneling through shared Key Events into the merged terminal Adverse Outcome, impaired TDAR, and onward to increased susceptibility to infection.}}

### The AOP 277 scientific review supplies the TDAR → infection quantitative bridge (F002)

The OECD external scientific review report for AOP 277 (titled *"Impaired IL-1R1 signaling leading to increased susceptibility to infection,"* dated 22 July 2021) documents that the **original** AOP 277 terminated not at impaired TDAR but at the Adverse Outcome **"increased susceptibility to infection,"** connected via the Key Event Relationship "Suppression of T-cell activation → increased susceptibility to infection." The report cites **Luster et al. 1993**, in which quantitative models relating immune-function tests (including T-cell functions) to host-resistance tests were established, with most immune–host-resistance relationships approximating a **linear model**. A specific quantified example is preserved: *"a 6.4% decrease in ConA-induced T-cell proliferation is associated with a 10% increased risk of Listeria monocytogenes infection."* Supporting mechanistic evidence cited in the review includes IL-1R1's role in host resistance to *M. tuberculosis* and the observation that calcineurin inhibitors causing T-cell suppression produce opportunistic infections in transplant recipients. Reviewers noted the difficulty of defining "susceptibility to infection" as a *measurable* Adverse Outcome with a clear mechanism, which **motivated the revision** of the terminal AO to the measurable in vivo endpoint "Impairment of TDAR." This is the pivotal historical link between the two outcomes at the heart of the research question.

### TDAR is among the most predictive immune assays for altered host resistance (F003)

Luster et al. 1993 ([PMID: 8365588](https://pubmed.ncbi.nlm.nih.gov/8365588/)) analyzed the US National Toxicology Program immunotoxicology database of more than 50 compounds and built statistical models relating immune-function tests to host-resistance (infection) tests. Two conclusions anchor the network:

1. *"A good correlation exists between changes in the immune tests and altered host resistance in that there were no instances where host resistance was altered without affecting an immune test(s)."* — There is no observed instance of altered host resistance **without** a corresponding immune-test change.
2. *"enumeration of lymphocyte populations and quantitation of the T-dependent antibody response were particularly beneficial"* — TDAR and lymphocyte enumeration were the **most predictive** parameters, whereas apical measures (leukocyte counts, lymphoid organ weights) were relatively insensitive.

Together with the near-linear dose-response from the companion analysis cited in the AOP 277 review, this establishes TDAR as both a sensitive and quantitatively predictive surrogate for infection risk.

### Every Key Event in the network has a defined measurement assay (F004)

A core requirement of the research question was that Key Events carry associated assays or in vivo test endpoints. Extraction of the "How It Is Measured or Detected" sections from AOP-Wiki confirmed full assay coverage:

| Key Event | Assay(s) |
|-----------|----------|
| Calcineurin inhibition (KE980) | Phosphatase activity assay / Ki determination |
| NFAT nuclear localization (KE979) | Imaging flow cytometry + gel mobility shift (EMSA) |
| NFAT/AP-1 complex (KE981) | Gel-shift assay with anti-Fos/anti-Jun antibodies |
| IL-2/IL-4 suppression (KE1202) | Cytokine ELISA / ex vivo whole-blood stimulation (MSD electrochemiluminescence) |
| Impaired IL-1R1 signaling (KE1700) | IL-1α/β RT-PCR & ELISA, ¹²⁵I-IL-1α receptor binding, bioactivity neutralization |
| NF-κB inhibition (KE202) | β-lactamase/GFP reporter, IκBα phospho-Western, p65 ELISA |
| Suppression of T-cell activation (KE1702) | IL-2 ELISA, CFSE or [³H]thymidine proliferation |
| JAK3 inhibition (KE1715) | Caliper mobility-shift kinase assay (IC50) |
| STAT5 phosphorylation (KE1716) | Phospho-STAT5 flow cytometry / antibody detection |
| STAT5–promoter binding (KE1717) | EMSA |
| IL-4 suppression (KE1718) | IL-4 ELISA / RT-PCR / intracellular flow cytometry |
| **Impaired TDAR (AO984 & AO1719)** | **In vivo antigen-specific antibody quantitation by ELISA (anti-KLH IgM/IgG) or plaque-forming-cell (PFC/AFC) assay to SRBC; ex vivo KLH-specific CD4+ T-cell proliferation** |

This complete assay mapping is what makes the network actionable for NAM development: every upstream node can, in principle, be measured in vitro.

### A glucocorticoid-receptor branch bridges the network to the infection outcome (F005)

AOP-Wiki **AOP 14** (Glucocorticoid Receptor Activation Leading to Increased Disease Susceptibility) traces: MIE122 GR activation → KE145 IκB induction → **KE202 NF-κB inhibition** → KE152 suppression of inflammatory cytokines → KE168 decreased lymphocytes → KE403 suppression of immune system → **AO323 Increased Disease Susceptibility**. Because **KE202 (Inhibition of NF-κB) is shared** between AOP 14 and AOP 277, it forms a direct network bridge from the TDAR pathways to the disease/infection-susceptibility outcome. KE403 (Suppression of immune system) is a further hub shared by AOPs 14, 84, 85, and 432. Together with the three TDAR-terminal AOPs, this yields a **four-MIE immunosuppression network** (calcineurin inhibition, JAK3 inhibition, impaired IL-1R1 signaling, GR activation), all acting at the T-cell level, in which impaired TDAR and increased disease/infection susceptibility are linked convergent adverse outcomes.

### The 2026 PAC study anchors the network with an in vivo TDAR dataset (F006, F013)

Johnson, Rider, Luster, Germolec et al. 2025/2026 ([PMID: 40115130](https://pubmed.ncbi.nlm.nih.gov/40115130/)) — the paper named in the research question — treated adult female B6C3F1/N mice for 28 consecutive days by oral gavage with selected polycyclic aromatic compounds:

- **Benzo[a]pyrene** suppressed the SRBC TDAR by **~75% at 9 mg/kg/day** and ~32% at the lowest dose (2 mg/kg/day). TDAR suppression was more sensitive than splenic immune-cell loss, indicating **functional** impairment rather than mere cell depletion.
- **Phenanthrene** suppressed TDAR only at ≥50 mg/kg; **pyrene** had no immune effect — demonstrating structure-dependent potency.
- Critically: *"Suppression of the TDAR to SRBC immunization was the most sensitive immune endpoint being 33 times more sensitive than changes in liver weight, a commonly used outcome for risk assessment for PACs."*

The assay used is precisely the terminal AO node (KE984/KE1719) of the network. This quantitatively establishes that impaired TDAR detects immunotoxic hazard at exposures **33-fold below** those producing conventional organ-weight effects, underscoring its value as the network's sensitive apical endpoint.

### Convergent literature validates TDAR as a first-line assay predicting host resistance (F007)

Multiple independent regulatory and methodological sources aggregate the TDAR → infection linkage:

- **Burleson & Burleson 2008** ([PMID: 18382855](https://pubmed.ncbi.nlm.nih.gov/18382855/)): *"Host resistance assays are the best measure of a toxicant's effect on the overall ability to mount an effective immune response and protect the host from infectious disease,"* and *"Measurement of influenza-specific IgM or IgG also provides a measurement of T-dependent antibody response (TDAR) since influenza is a T-dependent antigen."* This directly couples the TDAR readout to an anti-viral host-resistance model.
- **Descotes 2006** ([PMID: 16866611](https://pubmed.ncbi.nlm.nih.gov/16866611/)): *"A T-dependent antibody response assay, either the plaque-forming cell assay or anti-keyhole limpet haemocyanin enzyme-linked immunosorbant assay, is recommended as a first-line assay."*
- **White et al. 1994** ([PMID: 20693053](https://pubmed.ncbi.nlm.nih.gov/20693053/)): In a nine-laboratory NTP validation study with cyclosporin A, the T-dependent antibody plaque-forming-cell assay showed **100% inter-laboratory concordance**, establishing assay robustness.

### Peer-reviewed 2024 mapping independently confirms the four-AOP network (F008)

A comprehensive AOP-Wiki mapping (*Front. Toxicol.* 2024, doi:10.3389/ftox.2024.1285768) independently built an immunosuppression AOP network and states verbatim: *"For immunosuppression, three complete and one less complete AOP were identified in the AOP-Wiki (AOP IDs 315, 154, 277 and 14, respectively), of which one is endorsed (AOP ID 154 …). Four different MIEs are represented (Inhibition of calcineurin activity; Inhibition of JAK3; Impaired IL-1R1 signaling; Activation of Glucocorticoid Receptor) all acting at the T-cell level."* It confirms that the three TDAR AO synonyms were **merged** into a single node and documents a key gap: *"None of the AOPs for immunosuppression include KEs related to the involvement of the innate immune system, cell-mediated immunity or direct effects on B-cell populations."* This external confirmation validates the network structure derived independently in this investigation.

### Mechanistic and clinical evidence close the infection end of the network (F009)

Two independent lines complete the causal chain to real infection outcomes:

- **Mechanistic:** Bohrer et al. 2018 ([PMID: 30068597](https://pubmed.ncbi.nlm.nih.gov/30068597/)) show that *"IL-1R1 deficiency in mice causes severe susceptibility to"* *Mycobacterium tuberculosis* — i.e., the exact molecular initiating event of AOP 277 directly compromises host resistance to infection.
- **Clinical:** Cippà et al. 2015 ([PMID: 26430088](https://pubmed.ncbi.nlm.nih.gov/26430088/)), analyzing the Symphony (n=1190) and FDCC (n=630) kidney-transplant cohorts, found severe infections in ~25.5% of patients in year 1, and *"infections were the principal cause of death (43.2% of all deaths),"* with cyclosporin A- vs tacrolimus-based immunosuppression modulating the rejection/infection balance — linking calcineurin-inhibitor immunosuppression (the AOP 154 MIE) to clinical infection burden.

### KER weight-of-evidence into TDAR is High/High across all three AOPs (F010)

Extraction of the AOP-Wiki Key Event Relationship (KER) weight-of-evidence tables shows the terminal step into impaired TDAR is uniformly the strongest link:

| AOP | Terminal KER | Evidence | Quantitative Understanding |
|-----|--------------|----------|-----------------------------|
| 154 | IL-2 & IL-4 suppression → Impaired TDAR | High | High |
| 277 | Suppression of T-cell activation → Impaired TDAR | High | High |
| 315 | IL-4 suppression → Impaired TDAR | High | High |

Upstream KERs range from Moderate to High, but the **final KER into the shared Adverse Outcome is rated High evidence AND High quantitative understanding in all three pathways**, giving the convergence node exceptional confidence.

### The network contextualizes existing test guidelines and enables NAM-based 3R refinement (F011)

The terminal AO — impaired TDAR — is the endpoint required or recommended across multiple regulatory frameworks: **ICH S8** (Immunotoxicity Studies for Human Pharmaceuticals) recommends TDAR when immunotoxic target cells are unclear; **US EPA OCSPP/OPPTS 870.7800** specifies the SRBC antibody/plaque-forming-cell response; and **OECD TG 443** (Extended One-Generation Reproductive Toxicity Study) includes an optional developmental-immunotoxicity cohort using the anti-KLH TDAR. The network maps this in vivo AO to a chain of upstream Key Events, each measurable by in vitro NAMs (calcineurin phosphatase assay, JAK3 kinase assay, NF-κB reporter genes, phospho-STAT5 flow cytometry, EMSA, cytokine ELISA, T-cell proliferation), providing the scaffold for a **defined approach** that could reduce or replace the animal-based TDAR test.

### An AhR branch integrates the PAC chemical class into the network (F012, F014)

The 2026 named paper shows oral PACs suppress the SRBC TDAR, and multiple mechanistic studies establish AhR as the **obligatory receptor** for this suppression, defining a chemical stressor branch that converges on the same downstream Key Events:

- North et al. 2009 ([PMID: 18948302](https://pubmed.ncbi.nlm.nih.gov/18948302/)): *"Suppression of humoral immune responses by 2,3,7,8-tetrachlorodibenzo-p-dioxin (TCDD) has been well established to require the aryl hydrocarbon receptor."*
- Zhang et al. 2010 ([PMID: 20359356](https://pubmed.ncbi.nlm.nih.gov/20359356/)): AhR agonists suppress B-lymphocyte terminal differentiation to antibody-secreting plasma cells; TCDD and other dioxin-like compounds *"belong to the family of aryl hydrocarbon receptor (AhR) agonists."*
- Yuan et al. 2021 ([PMID: 33032214](https://pubmed.ncbi.nlm.nih.gov/33032214/)): confirms the *"suppression of immunoglobulin M (IgM) antibody-forming cell (AFC) response which is an indicator of immunotoxicity."*
- Chen et al. 2013 ([PMID: 24051191](https://pubmed.ncbi.nlm.nih.gov/24051191/)): *"Exposure to TCDD … suppressed many ovalbumin (OVA)-stimulated cytokines, including IL-2, IFN-γ, IL-4, IL-5, and IL-10"* — the same T-cell cytokines that are terminal Key Events of AOPs 154 and 315.

This defines a **PAC/AhR-agonist → AhR activation (MIE) → suppressed B-cell differentiation and IL-4/T-cell cytokine output → impaired TDAR (AO)** branch converging on the shared downstream events.

---

## Mechanistic Model / Interpretation

The network can be summarized as a **many-to-one-to-one** funnel: multiple chemically distinct MIEs → a shared set of intermediate T-cell/B-cell Key Events → the single Adverse Outcome impaired TDAR → increased susceptibility to infection.

```
   CHEMICAL / STRESSOR         MOLECULAR INITIATING EVENT
   ------------------          --------------------------
   Cyclosporin A / FK506  -->  Calcineurin inhibition (AOP 154, KE980)
                                     |
                                     v  NFAT localization -> NFAT/AP-1 -> IL-2/IL-4 suppression
                                     |
   JAK3 inhibitors        -->  JAK3 inhibition (AOP 315, KE1715)
                                     |
                                     v  STAT5-P block -> promoter binding -> IL-4 suppression
                                     |
   IL-1R1 pathway block   -->  Impaired IL-1R1 signaling (AOP 277, KE1700)
                                     |
                                     v  NF-kB inhibition (KE202) -> suppressed T-cell activation
                                     |
   PACs / dioxin-like     -->  AhR activation (chemical branch)
                                     |
                                     v  suppressed B-cell differentiation + IL-4/IL-2 suppression
                                     |
   Glucocorticoids        -->  GR activation (AOP 14, MIE122)
                                     |
                                     v  IkB induction -> NF-kB inhibition (KE202, SHARED)
                                     |
                                     +----------------> IMPAIRED TDAR (AO984 / AO1719)
                                                              |  [KER into AO: High / High]
                                                              v
                                                   INCREASED SUSCEPTIBILITY TO INFECTION
                                                   (AOP 277 original AO; AOP 14 AO323)
```

Two **convergence nodes** give the network its coherence. First, **KE202 (NF-κB inhibition)** is shared by AOP 277 and AOP 14, physically linking the TDAR branch to the "increased disease susceptibility" branch. Second, **IL-4 suppression** is shared by AOPs 154 and 315, and IL-2/IL-4 suppression is a convergence point for the AhR branch as well. Downstream of these, the impaired antibody-forming-cell response is the common functional readout.

The biological logic of the TDAR → infection link is sound: a functional antibody response to a T-dependent antigen requires intact antigen presentation, CD4+ T-helper activation (IL-2), Th2 help (IL-4), and B-cell differentiation into antibody-secreting plasma cells. A perturbation at any of these steps reduces protective humoral immunity, and — as the Luster analysis shows — no instance of altered host resistance occurred without a corresponding immune-test change. The AOP 277 review's near-linear quantitative model (6.4% ConA proliferation decrease ≈ 10% increased *Listeria* infection risk) provides the dose-response scaffolding, while IL-1R1-deficient mice (*M. tuberculosis* susceptibility) and transplant cohorts (infection as leading cause of death) bracket the mechanistic and clinical extremes.

---

## Evidence Base

| PMID | Paper | Role in the network |
|------|-------|---------------------|
| [8365588](https://pubmed.ncbi.nlm.nih.gov/8365588/) | *Risk assessment in immunotoxicology II: relationships between immune and host resistance tests* (Luster 1993) | Quantitative/population bridge: immune-test changes correlate with altered host resistance; TDAR most predictive; near-linear model |
| [40115130](https://pubmed.ncbi.nlm.nih.gov/40115130/) | *Suppression of the TDAR following oral exposure to selected PACs in B6C3F1/N mice* (Johnson/Germolec 2025) | Current in vivo chemical anchor: benzo[a]pyrene suppresses TDAR ~75%, 33× more sensitive than liver weight |
| [18948302](https://pubmed.ncbi.nlm.nih.gov/18948302/) | *TCDD-mediated suppression of anti-SRBC IgM AFC response reversed by IFN-γ* (North 2009) | Establishes AhR as obligatory MIE for chemical suppression of TDAR |
| [20359356](https://pubmed.ncbi.nlm.nih.gov/20359356/) | *Stochastic modeling of B-cell terminal differentiation and its suppression by dioxin* (Zhang 2010) | AhR agonists suppress B-cell differentiation to plasma cells — convergent KE |
| [33032214](https://pubmed.ncbi.nlm.nih.gov/33032214/) | *Natural organic matter and TCDD bioavailability* (Yuan 2021) | IgM AFC (TDAR) as AhR-mediated immunotoxicity readout |
| [24051191](https://pubmed.ncbi.nlm.nih.gov/24051191/) | *Immunotoxic effects of dual PCP + TCDD exposure* (Chen 2013) | AhR agonist suppresses IL-2/IL-4 — shared terminal KEs of AOPs 154/315 |
| [30068597](https://pubmed.ncbi.nlm.nih.gov/30068597/) | *IL-1R1 mediates host resistance to M. tuberculosis* (Bohrer 2018) | Mechanistic: AOP 277 MIE directly causes infection susceptibility |
| [26430088](https://pubmed.ncbi.nlm.nih.gov/26430088/) | *Risk stratification for rejection and infection after kidney transplantation* (Cippà 2015) | Clinical: calcineurin-inhibitor immunosuppression → infection is leading cause of death (43.2%) |
| [16866611](https://pubmed.ncbi.nlm.nih.gov/16866611/) | *Methods of evaluating immunotoxicity* (Descotes 2006) | Regulatory: TDAR is recommended first-line functional immunosuppression assay |
| [18382855](https://pubmed.ncbi.nlm.nih.gov/18382855/) | *Testing human biologicals in animal host resistance models* (Burleson 2008) | Host-resistance assays best measure infection protection; embed a TDAR readout |
| [20693053](https://pubmed.ncbi.nlm.nih.gov/20693053/) | *International methods validation of cyclosporin A in F344 rat* (White 1994) | Assay robustness: TDAR-PFC 100% inter-laboratory concordance |
| [40711044](https://pubmed.ncbi.nlm.nih.gov/40711044/) | *Immunotoxicity studies on MPEP/pyriproxyfen* (Johnson 2025) | Chemical immunotoxicity evaluation with emphasis on host resistance to viral infection |

**Non-PubMed sources:** AOP-Wiki JSON API (AOPs 14, 84, 85, 154, 277, 315, 432 and their Key Events, KERs, and assay annotations); the OECD external scientific review report for AOP 277 ("Impaired IL-1R1 signaling leading to increased susceptibility to infection," 22 July 2021), which supplies the historical AO of "increased susceptibility to infection" and the quantitative Luster linear model; and the comprehensive AOP-Wiki immunosuppression mapping (*Front. Toxicol.* 2024, doi:10.3389/ftox.2024.1285768), which independently confirms the four-AOP network and the merged TDAR node.

{{figure:tdar_infection_aop_network.png|caption=TDAR↔infection AOP network diagram assembled from AOP-Wiki, the AOP 277 scientific review, and the supporting literature, showing MIEs, shared intermediate Key Events with their associated assays, the merged TDAR Adverse Outcome, and the terminal increased-susceptibility-to-infection outcome.}}

---

## Limitations and Knowledge Gaps

1. **Innate immunity and cell-mediated immunity are absent from the AOPs.** As both this investigation and the 2024 *Front. Toxicol.* mapping note, none of the immunosuppression AOPs include Key Events for innate immunity, cell-mediated immunity, or direct effects on B-cell populations. Infection defense in vivo depends on more than the humoral T-dependent response, so the network under-represents the full biology of host resistance.

2. **The TDAR → infection KER is quantitatively anchored largely by a single dataset.** The near-linear immune-to-host-resistance relationship derives principally from the Luster/NTP database (1993). While robust and widely cited, it is a historical rodent dataset; contemporary re-validation with modern host-resistance models and diverse pathogens would strengthen the quantitative KER.

3. **The AhR branch is not yet a curated AOP-Wiki pathway.** The AhR → impaired TDAR branch is assembled from mechanistic literature (North, Zhang, Yuan, Chen) rather than a formal AOP-Wiki entry, so it lacks the standardized KER weight-of-evidence ratings that the three curated AOPs carry.

4. **Species and quantitative extrapolation.** Most mechanistic and quantitative evidence is rodent-derived; the clinical infection evidence (Cippà 2015) reflects heavily immunosuppressed transplant patients and may not extrapolate linearly to low-dose environmental chemical exposures.

5. **AOP 14 is "less complete."** The glucocorticoid-receptor bridge to "increased disease susceptibility" relies on AOP 14, which the mapping literature explicitly flags as the least developed of the four and in need of further curation.

---

## Proposed Follow-up Experiments / Actions

1. **Formalize the AhR → impaired TDAR AOP** in AOP-Wiki, with defined MIE (AhR activation), Key Events (suppressed B-cell terminal differentiation via Bcl-6/Blimp-1/Pax5; IL-2/IL-4 suppression), and KER weight-of-evidence tables, using the North/Zhang/Yuan/Chen evidence and the Johnson/Germolec 2025 in vivo dataset.

2. **Add innate- and cell-mediated-immunity Key Events** to close the acknowledged network gap, so that "increased susceptibility to infection" is supported by more than the humoral branch — for example, NK-cell function and macrophage/phagocyte assays already used in the host-resistance literature.

3. **Re-derive the quantitative TDAR → infection KER** using modern host-resistance challenge models (influenza, *Listeria*, *M. tuberculosis*) paired with contemporaneous TDAR measurements, to update and validate the Luster near-linear relationship with current methods and effect-size confidence intervals.

4. **Prototype a NAM-based defined approach** that measures the upstream in vitro Key Events (calcineurin phosphatase, JAK3 kinase, NF-κB reporter, phospho-STAT5, IL-2/IL-4 ELISA, CFSE T-cell proliferation) as a battery predicting the in vivo TDAR outcome, then benchmark it against reference immunosuppressants (cyclosporin A, tofacitinib, dexamethasone) and PACs (benzo[a]pyrene) to support 3R replacement of the animal TDAR test.

5. **Benchmark-dose concordance analysis** relating in vitro NAM potencies to the in vivo TDAR BMDs reported for benzo[a]pyrene, phenanthrene, and pyrene (Johnson/Germolec 2025), to quantitatively demonstrate that the in vitro battery reproduces the structure-dependent potency ranking observed in vivo.

6. **Cross-AOP hub validation** for KE202 (NF-κB inhibition) and KE403 (immune-system suppression) as network-control nodes, testing whether perturbing these shared hubs predicts the infection outcome across multiple MIE branches — which would elevate them to high-value regulatory anchor points.
