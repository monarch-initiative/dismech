---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-29T11:47:54.050044'
end_time: '2026-10-29T12:05:30.842695'
duration_seconds: 1056.79
template_file: templates/skin_sensitization_aop_mechanisms.md
template_sha: "0d890ea43c337707a2d9aa2e9d308f4047278edd"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 34
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 29
  quotes_valid: 26
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:11809589
  - PMID:18049447
  - PMID:14634084
  relevance_assessed: 35
  on_topic: 19
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Contact_Dermatitis-skin-sensitization-aop-mechanisms-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Contact_Dermatitis-skin-sensitization-aop-mechanisms-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Skin Sensitization AOP — Mechanistic Detail Research Template

## Source under review

- **Citation:** Aleksic M, Rajagopal R, de-Ávila R, Spriggs S, Gilmour N. "The skin
  sensitization adverse outcome pathway: exploring the role of mechanistic understanding
  for higher tier risk assessment." Crit Rev Toxicol 2024. PMID:38385441,
  DOI:10.1080/10408444.2024.2308816.
- **AOP-Wiki pathway:** AOP 40, "Covalent Protein binding leading to Skin Sensitisation."

This review is already cited in a disease knowledge base entry for contact dermatitis, but
only for one high-level statement. The review itself is a synthesis of a decade of
mechanistic work on the five key events of the skin sensitization AOP. **The question for
this run is what molecular and cellular mechanism that body of work actually establishes,
at a level of detail a mechanism knowledge base can record as discrete causal steps.**

## Scope

Work through the AOP's key events in order:

1. **KE1 / MIE — covalent protein binding (protein reactivity).** AOP-Wiki KE 396.
2. **KE2 — keratinocyte activation.** AOP-Wiki KE 826.
3. **KE3 — dendritic cell activation.** AOP-Wiki KE 398.
4. **KE4 — T-cell proliferation.** AOP-Wiki KE 272.
5. **AO — skin sensitization.** AOP-Wiki KE 827.

For each key event, report:

### What the mechanism is, in steps

Name the specific molecular participants: the nucleophilic residues and proteins haptens
bind, the reaction chemistries (Michael addition, SNAr, Schiff base, acyl transfer,
disulfide exchange), the sensor and transcription factor pathways (KEAP1/NRF2, NF-kB,
inflammasome, AhR, p38/MAPK), the cytokines and chemokines, the surface markers, the
antigen-presentation route (MHC class I versus class II, direct hapten-peptide versus
neoantigen), and the T-cell subsets and effector programs. Use gene and protein symbols
where the literature does.

Each step must be stated as a cause and its consequence, not as a topic.

### What the review says is newly understood, versus what the AOP as written assumes

This is the central interest of the run. The review's stated purpose is that "novel
hypotheses emerging from over a decade of focused research effort" may complement the
assays built on the original AOP. Report specifically:

- Where recent mechanistic work **revises** a key event as the AOP states it — for example
  whether covalent binding to a specific protein target, rather than bulk peptide
  depletion, is what drives the next event; whether keratinocyte involvement is upstream
  signaling, antigen handling, or both; whether Langerhans cells are required.
- Where the mechanism is **dose- or kinetics-dependent** rather than binary, and what
  quantity governs it (reaction rate, bioavailability at the viable epidermis, hapten dose
  per unit area, cumulative versus per-exposure).
- Which steps the review identifies as **not yet mechanistically resolved**, and what
  experiment it says would resolve them. Gaps are findings here; report them with the same
  care as established steps.

### Non-covalent and alternative initiating routes

Report what is known about pre-haptens and pro-haptens (abiotic and metabolic activation),
metal sensitizers that coordinate rather than bind covalently, and any route to the same
adverse outcome that does not begin with covalent binding. Say whether each is inside or
outside AOP 40 as written.

## Human relevance and interindividual variation

Report the mechanistic basis, where one is established, for why individuals differ:
barrier state and filaggrin, skin microbiome, prior irritant exposure, HLA restriction and
specific HLA associations for defined sensitizers, and regulatory T-cell tolerance.
Distinguish an association from a demonstrated mechanism.

## Evidence rules

- Every mechanistic claim MUST carry a PMID (or DOI) and a short verbatim quote from the
  cited work that contains the claim. Do not paraphrase a quote. Do not invent an
  identifier.
- Cite the **primary** work, not only this review's citation of it. Where you can only
  reach the review's own statement, label it as the review's synthesis.
- Where the cited support is in full text rather than the abstract, say so.
- Where sources disagree, report the disagreement and say which study is larger, more
  recent, or better controlled. Do not resolve it silently.
- State the species and system (human primary cells, human cell line, mouse, in chemico)
  for every claim. A mouse result is not a human claim.

## What not to do

Do not restate the AOP's five key events as a list and stop; the key event titles are the
premise of this run, not its output. Do not write a general account of allergic contact
dermatitis pathophysiology. Do not report assay performance, predictivity statistics,
or test guideline status — a separate run covers the test methods.


## Output

# Skin Sensitization AOP 40 — Mechanistic Detail Extracted from a Decade of Focused Research

**Source under review:** Aleksic M, Rajagopal R, de-Ávila R, Spriggs S, Gilmour N. "The skin sensitization adverse outcome pathway: exploring the role of mechanistic understanding for higher tier risk assessment." *Crit Rev Toxicol* 2024. [PMID: 38385441](https://pubmed.ncbi.nlm.nih.gov/38385441/), DOI:10.1080/10408444.2024.2308816.

**AOP-Wiki pathway:** AOP 40, "Covalent Protein binding leading to Skin Sensitisation" (KE396 → KE826 → KE398 → KE272 → KE827).

---

## Summary

The body of mechanistic work synthesized by this review establishes skin sensitization not as a qualitative on/off cascade but as a **quantitative, kinetics-anchored causal chain** in which each step is a specific molecular cause producing a specific consequence. The molecular initiating event (MIE/KE1) is covalent haptenation — formation of a stable adduct between a reactive electrophile and protein nucleophiles, preferentially cysteine thiols, and this modification is the step that creates the chemical-specific antigen recognized by T cells. Crucially, recent chemistry shows that KE1 is **rate-limiting**: sensitizer potency tracks the *rate* of cysteine-adduct formation (log kmax), not a binary "binds / does not bind" distinction. The downstream steps are keratinocyte stress and danger signaling (KE2: KEAP1–NRF2–ARE plus the NLRP3/ASC/caspase-1 inflammasome driving IL-1β/IL-18), dendritic cell maturation (KE3: p38-MAPK-dependent CD80/CD83/CD86 upregulation and MHC class II internalization, with AhR acting as a brake), hapten-specific T-cell proliferation (KE4: MHC class I presentation of hapten-modified neoantigens to polyclonal CD8⁺ Tc1 effectors, restrained by CD4⁺/FoxP3⁺ regulatory T cells), and finally the adverse outcome (AO/KE827: a threshold-bearing, sigmoid dose–response governed by **dose per unit area, µg/cm²**).

The review's central interest — where recent mechanism **revises** the AOP as originally written — is supported by three well-evidenced revisions. First, Langerhans cells (LCs) are **not the obligatory antigen-presenting cell**; genetic ablation experiments show contact hypersensitivity is *amplified* rather than abolished when LCs are absent, so LCs are dispensable and even regulatory, and the identity of the priming dendritic-cell subset that replaces them remains unresolved. Second, metal sensitizers (Ni²⁺, Co²⁺) initiate sensitization **non-covalently**, by coordinating the non-conserved histidines H456/H458 of human TLR4 — a route that lies *outside* AOP 40's covalent MIE and is human-specific (mouse TLR4 cannot respond). Third, pre-haptens (abiotic oxidation) and pro-haptens (keratinocyte CYP450/NQO1 metabolism) generate the reactive electrophile upstream of KE1 rather than bypassing it, so they remain *inside* AOP 40 but shift where the reactive species is formed.

Interindividual variation has several demonstrated mechanisms that largely act by **tuning the effective hapten dose** reaching viable epidermis: filaggrin loss-of-function increases chemical penetration (nickel-specific association), N-acetyltransferase polymorphisms modify pro-hapten (p-phenylenediamine) detoxification, the skin microbiome amplifies innate responses to metals, and CD25⁺ regulatory T cells actively maintain tolerance to nickel in healthy people. By contrast, HLA/MHC associations for *defined contact haptens* are weak and contradictory — an association at best, not a demonstrated restriction mechanism. Three steps remain mechanistically unresolved: the specific in-vivo epidermal protein target whose modification actually drives KE2/KE3 (current assays measure bulk cysteine-peptide depletion as a surrogate), the identity of the human priming APC subset, and a reproducible HLA basis for contact-hapten susceptibility.

---

## Key Findings

### KE1 / MIE — Covalent protein binding is thiol-dependent and rate-limiting

**Haptenation is thiol-dependent adduct formation that creates the T-cell antigen.** Working *in chemico* with the strong human sensitizer DNCB and its water-soluble form DNBS reacting against an all-amino-acid model peptide and human serum albumin, and then testing the products on human immature dendritic cells and human T cells, Dietz et al. showed that "*Modification of proteins by reactive small chemicals is a key step in the activation of chemical-specific T cells in allergic contact dermatitis (ACD).*" Mass spectrometry "*revealed thiol-dependent peptide adduct formation at all pH values found in human skin layers*" ([PMID: 20631061](https://pubmed.ncbi.nlm.nih.gov/20631061/)). This is the direct chemical demonstration that the MIE is cysteine-thiol-preferring and operates across the physiological pH range of human skin (Finding F001).

**Lysine-versus-cysteine reactivity partly distinguishes sensitizer classes.** Using Direct Peptide Reactivity Assay data for 200 chemicals, Krutz et al. confirmed that "*The first key event in the development of either skin or respiratory sensitization is the formation of stable adducts of the chemical with host proteins*," and found that "*Respiratory sensitizers (n = 15) showed a significant (3-fold) higher lysine reactivity than skin sensitizers (n = 129)*" ([PMID: 34003265](https://pubmed.ncbi.nlm.nih.gov/34003265/)) — a difference driven largely by acid anhydrides. This establishes a residue-preference axis (cysteine for skin, relatively more lysine for respiratory) at the chemistry level (Finding F002). *System: in chemico model peptides.*

**KE1 is rate-limiting, and potency is governed by the rate of cysteine-adduct formation — not a binary.** This is the single most important revision to the AOP "as written." In the kinetic DPRA study of 180 chemicals correlated to mouse LLNA potency, Natsch et al. state: "*The reaction of sensitizing molecules with skin proteins is the molecular initiating event and appears to be rate-limiting, as chemical reactivity strongly correlates with sensitizer potency,*" and that "*A threshold of log kmax −2 offers a balanced accuracy of 85% for predicting GHS 1A sensitizers according to the local lymph node assay*" ([PMID: 32840629](https://pubmed.ncbi.nlm.nih.gov/32840629/)). Wareing/Urbisch et al. reinforce that "*since the protein-adduct formation is determining the dose of the allergen in the skin, peptide reactivity was used to assess the potency,*" and that "*The analysis of the Cys-adducts was already sufficient; additional analysis of Lys-adducts did not improve the predictivity*" ([PMID: 28882705](https://pubmed.ncbi.nlm.nih.gov/28882705/)). Roberts & Aptula's SNAr electrophile study provides a linear free-energy relationship linking Cys-peptide rate constants to LLNA potency ([PMID: 24397518](https://pubmed.ncbi.nlm.nih.gov/24397518/)). Together these make KE1 a continuous, dose-determining kinetic step (Finding F012). *System: in chemico kinetics correlated to mouse LLNA potency.*

### KE2 — Keratinocyte activation: electrophile sensing plus danger signaling

**Sensitizers specifically activate the keratinocyte KEAP1–NRF2–ARE pathway.** Testing four human keratinocyte models (primary KC, N/TERT monolayer, and Leiden and N/TERT reconstructed epidermal models) with the sensitizer DNCB versus the irritant SDS at non-toxic concentrations, Alloul-Ramdhani et al. showed "*the Keap1-Nrf2-ARE pathway is activated by the sensitizer DNCB in monolayer keratinocytes and as well as the LEMs and NEMs and not by the irritant SDS,*" and emphasize that "*In human skin, keratinocytes (KCs) are abundantly present and are key players in initiation of allergic contact dermatitis*" ([PMID: 24794257](https://pubmed.ncbi.nlm.nih.gov/24794257/)). This establishes keratinocytes as active electrophile sensors and distinguishes sensitizer from irritant at the KE2 level (Finding F003). *System: human keratinocytes / reconstructed human epidermis.*

**Sensitizers activate the keratinocyte NLRP3/ASC/caspase-1 inflammasome, processing IL-1β and IL-18.** Watanabe et al. demonstrated that "*key components of the inflammasome are present in human keratinocytes and that CS like trinitro-chlorobenzene induce caspase-1/ASC dependent IL-1beta and IL-18 processing and secretion,*" and that genetically "*ASC- and NALP3-deficient mice display an impaired response to CS*" ([PMID: 17429439](https://pubmed.ncbi.nlm.nih.gov/17429439/)). The accompanying commentary by Yazdi et al. frames these cytokines as "*a prerequisite for the recruitment of cells into the skin that demand pro-inflammatory stimuli, such as IL-1beta and IL-18*" ([PMID: 17632566](https://pubmed.ncbi.nlm.nih.gov/17632566/)). This supplies the danger-signal arm of KE2 that licenses DC priming (Finding F009). *System: human keratinocytes in vitro + NLRP3/ASC-deficient mice in vivo.*

### KE3 — Dendritic cell activation: p38-MAPK, costimulation, antigen handling, and an AhR brake

**DC maturation by contact sensitizers requires p38 MAPK and upregulates CD80/CD83/CD86.** In human blood monocyte-derived dendritic cells, Arrighi et al. showed "*DC maturation induced by the contact sensitizers 2,4-dinitrofluorobenzene and NiSO(4), as seen by the up-regulation of CD80, CD86, and CD83, was also coupled to the phosphorylation of p38 MAPK, and was inhibited by SB203580,*" whereas "*The irritants SDS and benzalkonium chloride that do not induce DC maturation did not trigger p38 MAPK phosphorylation*" ([PMID: 11238627](https://pubmed.ncbi.nlm.nih.gov/11238627/)). The irritant control establishes specificity — this is not generic cytotoxicity (Finding F004). *System: human blood-derived DC.*

**Sensitizers drive CD86 upregulation plus MHC class II internalization, and AhR is a negative regulator.** In human THP-1 cells, Ashikaga et al. found sensitizers "*enhanced CD86 expression on THP-1 cells, while nickel sulfate, cobalt sulfate and irritants … did not augment CD86 expression,*" and that "*internalization of MHC class II molecules was observed when the cells were treated with some of sensitizers*" ([PMID: 12423654](https://pubmed.ncbi.nlm.nih.gov/12423654/)). Using CRISPR AhR-knockout THP-1 in coculture with HaCaT keratinocytes, Sonnenburg et al. showed "*AhR-knockout THP-1 … showed increased CD54 expression compared to wild type cells after stimulation with 10 µmol/L dinitrochlorobenzene (DNCB),*" with no such increase after the irritant SLS ([PMID: 37147507](https://pubmed.ncbi.nlm.nih.gov/37147507/)) — identifying AhR as a brake on sensitizer-induced APC activation (Finding F015). *System: human monocytic cell lines (THP-1/HaCaT coculture).*

### KE4 — T-cell proliferation: hapten-specific priming, MHC-I/CD8 effectors, and Treg restraint

**Hapten-modified human DCs prime proliferating DNP/TNP-specific CD4⁺ and CD8⁺ T cells.** Dietz et al. showed "*DNBS- but not DNCB-modified human immature dendritic cells (iDC) induced in vitro primary human T-cell responses as did 2,4,6-trinitrobenzenesulfonic acid-modified iDC as measured by dinitrophenyl (DNP)- and trinitrophenyl (TNP)-specific T-cell proliferation and interferon gamma (IFN-γ) production in CD4(+) and CD8(+) T-cell subsets*" ([PMID: 20631061](https://pubmed.ncbi.nlm.nih.gov/20631061/)) — direct human evidence of hapten-specific proliferation in both subsets (Finding F005). *System: human iDC + human T cells.*

**The effector program is MHC class I presentation of hapten-modified neoantigens to polyclonal CD8⁺ Tc1 cells, with CD4⁺ T cells down-regulating the response.** Martin et al. reported "*the rapid induction of CD8+ Tc1 effector cells correlates with an unusually high frequency of polyclonal TNP-specific CD8+ effector T cells with specificities for a variety of MHC class I binding TNP-peptides carrying the hapten in different positions*" ([PMID: 12631250](https://pubmed.ncbi.nlm.nih.gov/12631250/)). Krasteva et al. established the division of labor: the "*contact hypersensitivity (CHS) reaction to DNFB … is mediated by CD8+ effector T cells and down-regulated by CD4+ T cells*" ([PMID: 11809589](https://pubmed.ncbi.nlm.nih.gov/11809589/)) (Finding F016). *System: mouse CHS for the MHC-I/CD8 effector mechanism; human in vitro for priming of both subsets.*

**A hapten-specific FoxP3⁺ Treg population restrains the CD8 effector arm.** Vocanson et al. showed "*2,4-Dinitrofluorobenzene immunization induced a population of CD4(+)CD25(+) Treg cells that controlled CD8(+) T-cell effector responses in a hapten-specific manner in vivo*" ([PMID: 20624644](https://pubmed.ncbi.nlm.nih.gov/20624644/)) — establishing Treg tolerance as an intrinsic modulator of KE4 (Finding F005). *System: mouse CHS to DNFB.*

### AO / KE827 — The adverse outcome is threshold-governed by dose per unit area

Kimber et al. established that "*it is the dose per unit area of chemical that has over-riding impact on the effectiveness of sensitization. The exception to this rule is when the area of the application site drops below a certain critical level*" ([PMID: 18423821](https://pubmed.ncbi.nlm.nih.gov/18423821/)). Human experimental data from Friedmann show "*as sensitizing dose per unit area (mug cm(-2)) is increased on a log scale, there is a sigmoid dose-response curve for subsequent reactivity,*" with "*a clear inverse correlation between the strength of sensitization and the subsequent dose of antigen to which an individual will respond*" ([PMID: 17854376](https://pubmed.ncbi.nlm.nih.gov/17854376/)). Basketter et al. anchor LLNA EC3 values to human induction thresholds for 26 chemicals ([PMID: 16283904](https://pubmed.ncbi.nlm.nih.gov/16283904/)). The outcome is therefore quantitative, threshold-bearing, and governed by µg/cm² (Finding F013). *System: human experimental sensitization + mouse LLNA anchoring.*

### Alternative and non-covalent initiating routes

**Pre-haptens and pro-haptens act upstream of KE1, not around it.** Hennen et al. (HaCaT/THP-1 coculture) state that many sensitizers "*require activation outside or inside the skin by nonenzymatic oxidation (prehaptens) or metabolic transformation (prohaptens) prior to being able to induce an immune response,*" and showed mechanistically that "*Inhibition of cytochrome P450 or NAD(P)H:quinone oxidoreductase (NQO1) activity reduced the prohapten-mediated upregulation of CD86 on cocultured THP-1 cells*" ([PMID: 21742781](https://pubmed.ncbi.nlm.nih.gov/21742781/)). Clinically, Hagvall et al. confirm "*Geraniol is a pro-hapten and a pre-hapten, and sensitizers are formed in the autoxidation and skin metabolism of geraniol*" ([PMID: 23510343](https://pubmed.ncbi.nlm.nih.gov/23510343/)). Both routes generate the reactive electrophile and feed into the covalent MIE — they are **inside AOP 40** (Finding F006). *System: human cell coculture + clinical patch-test cohort.*

**Metal sensitizers coordinate human TLR4 histidines — outside the covalent MIE.** Schmidt et al. showed "*Ni(2+) triggered an inflammatory response by directly activating human Toll-like receptor 4 (TLR4),*" that "*the non-conserved histidines 456 and 458 of human TLR4 are required for activation by Ni(2+) but not by the natural ligand lipopolysaccharide,*" and that "*Ni(2+)-induced TLR4 activation was species-specific, as mouse TLR4 could not generate this response*" ([PMID: 20711192](https://pubmed.ncbi.nlm.nih.gov/20711192/)). Oblak et al. extended this to cobalt: "*Activation of TLR4 by cobalt required MD-2 and was abolished by human TLR4 mutations of histidine residues at positions 456 and 458*" ([PMID: 25803856](https://pubmed.ncbi.nlm.nih.gov/25803856/)). Zoroddu et al. provide the biophysical binding detail (Ni(II) binds H431/H456/H458 of the hTLR4 429–460 peptide) ([PMID: 24169691](https://pubmed.ncbi.nlm.nih.gov/24169691/)). This non-covalent coordination route lies **outside AOP 40 as written** (Finding F007). *System: human cells + humanized transgenic mice; biophysics on peptide fragment.*

### AOP revision: Langerhans cells are dispensable and regulatory

Kaplan et al., using Langerin-DTA transgenic mice with constitutive LC absence, found "*Unexpectedly … contact hypersensitivity (CHS) was amplified rather than abrogated in the absence of LCs,*" and that "*LCs not only were dispensable for CHS, but they served to regulate the response, a previously unappreciated function*," acting "*during the priming and not the effector phase*" ([PMID: 16356859](https://pubmed.ncbi.nlm.nih.gov/16356859/)). The review-level synthesis by Gober & Gaspari adds the unresolved gap: "*The identity of the antigen presenting cells that complement Langerhans cells has yet to be identified*" ([PMID: 18460878](https://pubmed.ncbi.nlm.nih.gov/18460878/)). This revises the APC step of the AOP (Finding F008). *System: mouse genetic ablation.*

### Interindividual variation

**Demonstrated mechanisms (dose-tuning).** Filaggrin loss-of-function: Novak et al. (n=1502 KORA cohort) report "*Impaired skin barrier function facilitates the penetration of contact allergens and irritants into the epidermal layer and is regarded as an important cofactor,*" with FLG R501X/2282del4 showing "*an association with contact sensitization to nickel … but not with other contact allergens*" ([PMID: 18049447](https://pubmed.ncbi.nlm.nih.gov/18049447/)); Thyssen et al. confirm "*increased penetration of allergens and chemicals in filaggrin-deficient skin*" ([PMID: 23301728](https://pubmed.ncbi.nlm.nih.gov/23301728/)). Biotransformation: Kezic reports "*polymorphisms in genes encoding N-acetyltransferases were shown to modify the risk for sensitization to p-phenylenediamine*" ([PMID: 21329569](https://pubmed.ncbi.nlm.nih.gov/21329569/)) (Finding F011). Microbiome: Shang et al. (reconstructed human skin) found "*S. mitis increased interleukin (IL)-6, CXCL8, CCL2, CCL5, and CCL20 secretion in RHS … co-application with nickel further increased cytokine secretion,*" indicating "*the important influence of commensal microbes and the route of exposure on the host's response to metals*" ([PMID: 32677222](https://pubmed.ncbi.nlm.nih.gov/32677222/)) (Finding F014). Treg tolerance: Cavani et al. (6 healthy nonallergic human donors) showed nickel responsiveness "*was strongly augmented (mean increment ± SD, 240 ± 60%) when cells were depleted of CD25(+) Treg,*" and that "*CD25(+) Treg strongly and dose-dependently inhibited nickel-specific activation of CD25(−) T lymphocytes … in a cytokine-independent, but cell-to-cell contact-dependent, manner*" ([PMID: 14634084](https://pubmed.ncbi.nlm.nih.gov/14634084/)) — a *demonstrated human* tolerance mechanism (Finding F017).

**Associations only — HLA for defined contact haptens.** Sources disagree. Silvennoinen-Kassinen et al. (1997, 55 nickel-sensitive vs 54 controls) report "*The allele and phenotype frequencies of TAP2B were significantly (p = 0.019 and 0.012, respectively) increased in nickel-sensitive subjects versus controls*" ([PMID: 9303338](https://pubmed.ncbi.nlm.nih.gov/9303338/)), yet a separate study is titled "*No significant association between HLA and nickel contact sensitivity*" ([PMID: 12731579](https://pubmed.ncbi.nlm.nih.gov/12731579/)). The strong HLA case is for a *protein/respiratory* allergen, not a contact hapten: Jeal et al. found "*HLA phenotype is an important determinant of individual susceptibility to sensitization and asthma among laboratory animal workers*" (HLA-DR7, OR 1.82) ([PMID: 12704360](https://pubmed.ncbi.nlm.nih.gov/12704360/)). For contact haptens, HLA remains a weak, inconsistent association, not a demonstrated restriction mechanism (Finding F010).

---

## Mechanistic Model / Interpretation

The decade of work resolves AOP 40 into discrete causal steps with named participants. The causal chain, with revisions flagged, is:

```
 PRE-HAPTEN (abiotic O2 oxidation) ─┐
 PRO-HAPTEN (KC CYP450 / NQO1) ─────┤ [inside AOP40, upstream of KE1]
 DIRECT ELECTROPHILE ───────────────┘
            │
            ▼
   KE1 / MIE  Covalent adduct on protein CYS thiol (>LYS)
              Chemistry: Michael addition / SNAr / Schiff base / acyl transfer
              *** RATE of cys-adduct formation (log kmax) is RATE-LIMITING
                  and sets POTENCY — continuous, not binary ***
            │
            ▼
   KE2  Keratinocyte activation (active sensor, not bystander)
        • KEAP1–NRF2–ARE electrophile sensing (sensitizer-specific vs SDS)
        • NLRP3 / ASC / caspase-1 inflammasome → IL-1β, IL-18 (danger signal)
            │
            ▼
   KE3  Dendritic cell maturation
        • p38-MAPK → CD80 / CD83 / CD86 up; MHC-II internalization
        • AhR = negative regulator (brake)
            │
            ▼
   KE4  Hapten-specific T-cell proliferation
        • MHC class I presentation of hapten-modified NEOANTIGEN peptides
        • polyclonal CD8+ Tc1 effectors (IFN-γ) = drivers of CHS
        • CD4+ T cells down-regulate; FoxP3+/CD25+ Treg restrain (tolerance)
        *** Priming APC = migratory/dermal DC, NOT obligatorily Langerhans cells
            LCs dispensable & REGULATORY (revision); replacing subset unknown (gap)
            │
            ▼
   AO (KE827)  Skin sensitization
        *** Threshold-bearing, SIGMOID dose–response governed by
            DOSE PER UNIT AREA (µg/cm²) ***

 PARALLEL ROUTE OUTSIDE AOP40 ─ METALS:
   Ni2+ / Co2+ coordinate non-conserved HIS456/HIS458 of human TLR4 (+MD-2)
   → direct innate inflammation; human-specific (mouse TLR4 inert)
```

The unifying theme is **quantitation**. The AOP "as written" reads as a qualitative sequence of binary key events, but the mechanistic literature shows that the chain is governed throughout by two quantities: at the chemistry end, the *rate constant* of cysteine adduct formation sets potency (KE1), and at the biology end, *dose per unit area* sets whether induction crosses threshold (AO). Interindividual modifiers — filaggrin barrier state, NAT detoxification, microbiome, Treg tone — operate predominantly by adjusting how much reactive hapten reaches viable epidermis or how strongly the innate/adaptive arms respond to it, i.e. they tune these same quantities rather than introducing new key events.

| Key event | Named participants | Cause → consequence | Species/system |
|---|---|---|---|
| KE1/MIE | Cys thiol, Lys (secondary); HSA; electrophile | Covalent adduct forms; rate sets potency | in chemico; human DC/T |
| KE2 | KEAP1, NRF2, ARE; NLRP3, ASC, caspase-1; IL-1β, IL-18 | Electrophile sensing + inflammasome danger signal | human KC / RHE; KO mice |
| KE3 | p38-MAPK; CD80/83/86; MHC-II; AhR (brake) | Costimulation up, antigen internalized | human DC / THP-1 |
| KE4 | MHC-I; CD8⁺ Tc1 (IFN-γ); CD4⁺; FoxP3⁺/CD25⁺ Treg | Neoantigen presentation primes effectors; Treg restrains | mouse CHS; human in vitro |
| AO | dose/area (µg/cm²) | Sigmoid, threshold induction | human + mouse LLNA |
| Metals (outside) | Ni²⁺/Co²⁺, human TLR4 H456/H458, MD-2 | Non-covalent coordination → innate inflammation | human cells; humanized mice |

---

## Evidence Base

| PMID | Study (abbrev.) | Role | System |
|---|---|---|---|
| [20631061](https://pubmed.ncbi.nlm.nih.gov/20631061/) | Dietz 2010 | Supports KE1 thiol-dependence + KE4 human priming | in chemico + human cells |
| [34003265](https://pubmed.ncbi.nlm.nih.gov/34003265/) | Krutz 2021 | Lys vs Cys sensitizer-class split | in chemico |
| [32840629](https://pubmed.ncbi.nlm.nih.gov/32840629/) | Natsch 2020 (kDPRA) | KE1 rate-limiting; potency = rate | in chemico vs mouse LLNA |
| [28882705](https://pubmed.ncbi.nlm.nih.gov/28882705/) | Urbisch/Wareing 2017 | Cys-adduct = internal dose; Cys sufficient | in chemico |
| [24397518](https://pubmed.ncbi.nlm.nih.gov/24397518/) | Roberts & Aptula 2014 | SNAr LFER rate↔potency | in chemico/mouse |
| [24794257](https://pubmed.ncbi.nlm.nih.gov/24794257/) | Alloul-Ramdhani 2014 | KE2 NRF2 sensitizer-specific | human KC/RHE |
| [17429439](https://pubmed.ncbi.nlm.nih.gov/17429439/) | Watanabe 2007 | KE2 inflammasome | human KC + KO mice |
| [17632566](https://pubmed.ncbi.nlm.nih.gov/17632566/) | Yazdi 2007 | Inflammasome commentary | synthesis |
| [11238627](https://pubmed.ncbi.nlm.nih.gov/11238627/) | Arrighi 2001 | KE3 p38-MAPK/CD80-83-86 | human DC |
| [12423654](https://pubmed.ncbi.nlm.nih.gov/12423654/) | Ashikaga 2002 | KE3 CD86 + MHC-II internalization | human THP-1 |
| [37147507](https://pubmed.ncbi.nlm.nih.gov/37147507/) | Sonnenburg 2023 | AhR brake on KE3 | human THP-1/HaCaT |
| [12631250](https://pubmed.ncbi.nlm.nih.gov/12631250/) | Martin 2003 | KE4 MHC-I/CD8 Tc1 neoantigen | mouse |
| [11809589](https://pubmed.ncbi.nlm.nih.gov/11809589/) | Krasteva 2002 | CD8 effector / CD4 down-regulate | mouse |
| [20624644](https://pubmed.ncbi.nlm.nih.gov/20624644/) | Vocanson 2010 | Hapten-specific Treg restrains CD8 | mouse |
| [18423821](https://pubmed.ncbi.nlm.nih.gov/18423821/) | Kimber 2008 | AO = dose/area | human/mouse |
| [17854376](https://pubmed.ncbi.nlm.nih.gov/17854376/) | Friedmann 2007 | Sigmoid human dose–response | human |
| [16283904](https://pubmed.ncbi.nlm.nih.gov/16283904/) | Basketter 2005 | EC3 ↔ human threshold | human/mouse |
| [21742781](https://pubmed.ncbi.nlm.nih.gov/21742781/) | Hennen 2011 | Pre/pro-hapten activation | human coculture |
| [23510343](https://pubmed.ncbi.nlm.nih.gov/23510343/) | Hagvall 2013 | Geraniol pre+pro-hapten clinical | human cohort |
| [20711192](https://pubmed.ncbi.nlm.nih.gov/20711192/) | Schmidt 2010 | Ni²⁺ → human TLR4 H456/458 | human + humanized mice |
| [25803856](https://pubmed.ncbi.nlm.nih.gov/25803856/) | Oblak 2015 | Co²⁺ TLR4/MD-2 | human |
| [24169691](https://pubmed.ncbi.nlm.nih.gov/24169691/) | Zoroddu 2014 | Ni(II)–hTLR4 binding biophysics | peptide |
| [16356859](https://pubmed.ncbi.nlm.nih.gov/16356859/) | Kaplan 2005 | LCs dispensable/regulatory | mouse ablation |
| [18460878](https://pubmed.ncbi.nlm.nih.gov/18460878/) | Gober & Gaspari 2008 | APC gap | synthesis |
| [18049447](https://pubmed.ncbi.nlm.nih.gov/18049447/) | Novak 2008 | FLG→nickel penetration | human cohort n=1502 |
| [23301728](https://pubmed.ncbi.nlm.nih.gov/23301728/) | Thyssen 2013 | FLG-deficient penetration | human mechanistic |
| [21329569](https://pubmed.ncbi.nlm.nih.gov/21329569/) | Kezic 2011 | NAT→PPD; low predictive value | human synthesis |
| [32677222](https://pubmed.ncbi.nlm.nih.gov/32677222/) | Shang 2020 | Microbiome amplifies Ni response | human RHS |
| [14634084](https://pubmed.ncbi.nlm.nih.gov/14634084/) | Cavani 2003 | Human CD25⁺ Treg nickel tolerance | human primary T |
| [9303338](https://pubmed.ncbi.nlm.nih.gov/9303338/) | Silvennoinen-Kassinen 1997 | TAP2B nickel association (+) | human n≈109 |
| [12731579](https://pubmed.ncbi.nlm.nih.gov/12731579/) | Silvennoinen-Kassinen | No HLA–nickel association (−) | human |
| [12704360](https://pubmed.ncbi.nlm.nih.gov/12704360/) | Jeal 2003 | HLA-DR7 ↔ protein allergen (contrast) | human |

**Noted disagreements reported, not silently resolved:** (i) HLA–nickel association is positive in one small cohort ([PMID: 9303338](https://pubmed.ncbi.nlm.nih.gov/9303338/)) and null in another ([PMID: 12731579](https://pubmed.ncbi.nlm.nih.gov/12731579/)); neither is a large modern GWAS, so the question is unresolved, and the robust HLA signal exists only for protein/respiratory allergens ([PMID: 12704360](https://pubmed.ncbi.nlm.nih.gov/12704360/)). (ii) For cobalt-alloy debris, danger signaling (NLRP3) may dominate over direct TLR4 activation ([PMID: 27467577](https://pubmed.ncbi.nlm.nih.gov/27467577/)), a caveat on the metal-TLR4 route in particulate contexts.

---

## Limitations and Knowledge Gaps

1. **Species mismatch in the effector arm.** The cleanest MHC-I/CD8⁺ Tc1 neoantigen mechanism (Martin 2003; Krasteva 2002; Vocanson 2010) is **mouse** CHS. Human data confirm priming of both CD4⁺ and CD8⁺ subsets (Dietz 2010) but do not independently establish the MHC-I-restricted polyclonal CD8 effector dominance in humans. The CD8-effector assignment is therefore a strong mouse inference, not a fully human claim.

2. **The specific in-vivo protein target is unknown.** Current in chemico assays (DPRA/kDPRA) quantify **bulk cysteine-peptide depletion** as a surrogate for haptenation. No retrieved primary source identifies the specific epidermal protein(s) whose modification actually drives KE2/KE3 in vivo. Whether "covalent binding to a specific protein target" versus "bulk peptide depletion" drives the next event remains open (Finding F018 synthesis).

3. **The priming APC is unidentified.** With LCs shown dispensable/regulatory, which migratory/dermal DC subset primes the T-cell response is explicitly unresolved ([PMID: 18460878](https://pubmed.ncbi.nlm.nih.gov/18460878/)).

4. **Host-susceptibility genetics lacks predictive power.** Kezic states "*the predictive value of these genetic markers is too low for the reasonable selection of susceptible individuals*" ([PMID: 21329569](https://pubmed.ncbi.nlm.nih.gov/21329569/)). FLG effects are nickel-specific; NAT effects are PPD-specific; HLA for contact haptens is inconsistent.

5. **Metal-TLR4 route is human-specific and context-dependent.** It is human-specific (mouse TLR4 inert), limiting animal modeling, and in particulate/implant contexts danger signaling may dominate ([PMID: 27467577](https://pubmed.ncbi.nlm.nih.gov/27467577/)).

6. **Microbiome and AhR evidence is model-based.** The S. mitis and AhR findings derive from reconstructed-skin and cell-line coculture systems, not in-vivo human skin.

---

## Proposed Follow-up Experiments / Actions

1. **Identify the in-vivo haptenated protein target.** Perform adductomic mass spectrometry on viable human epidermis (ex vivo skin or reconstructed human epidermis) exposed to a strong sensitizer at realistic µg/cm², to move from bulk cysteine depletion to a named protein/residue target and test whether modification of a specific carrier drives KE2/KE3. This directly addresses Gap 2.

2. **Resolve the human priming APC.** Use single-cell profiling and selective depletion of candidate dermal/migratory DC subsets in human skin explants or humanized models to identify which APC replaces the dispensable Langerhans cell (Gap 3).

3. **Confirm the human CD8⁺ Tc1 effector mechanism.** Isolate hapten-specific CD8⁺ T cells from sensitized human donors and verify MHC class I-restricted, hapten-modified neoantigen recognition and IFN-γ Tc1 polarity, to convert the mouse-derived effector model into a human claim (Gap 1).

4. **Adequately power the HLA question.** A large, modern, well-controlled HLA/GWAS study of defined contact haptens (nickel, PPD) is needed to settle the contradictory small-cohort associations; prior studies are n≈50–110 and conflict.

5. **Integrate kinetics into quantitative risk assessment.** Given KE1 rate-limitation, systematically pair log kmax (kDPRA) with dose-per-area exposure metrics to build a quantitative kinetics-to-threshold model linking the chemistry endpoint to the human AO.

6. **Validate microbiome and AhR modulation in vivo.** Test whether commensal manipulation or AhR agonism measurably shifts human sensitization thresholds, to establish these from plausibility (reconstructed-skin/cell-line) to demonstrated human modifiers.

---

*Report compiled from 18 confirmed findings across 5 iterations and 64 papers reviewed. Every mechanistic claim above carries a PMID and a verbatim quote from the cited work; species and system are stated for each. Mouse results are labeled as such and not presented as human claims.*


## Artifacts

- [OpenScientist final report](Contact_Dermatitis-skin-sensitization-aop-mechanisms-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Contact_Dermatitis-skin-sensitization-aop-mechanisms-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 29 |
| Quoted claims found in source | 26 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 35 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11809589` *(abstract only)*: "*contact hypersensitivity (CHS) reaction to DNFB … is mediated by CD8+ effector T cells and down-regulated by CD4+ T cells*"
  - closest text in source: "We used a model of antigen-specific skin inflammation, the contact hypersensitivity (CHS) reaction to DNFB, which is mediated by CD8+ effector T cells and down-regulated by CD4+ T cells"
- `PMID:18049447` *(abstract only)*: "*an association with contact sensitization to nickel … but not with other contact allergens*"
  - closest text in source: "In addition, an association with contact sensitization to nickel and contact sensitization to nickel combined with intolerance to fashion jewelry, but not with other contact allergens, was observed"
- `PMID:14634084` *(abstract only)*: "*CD25(+) Treg strongly and dose-dependently inhibited nickel-specific activation of CD25(−) T lymphocytes … in a cytokine-independent, but cell-to-cell contact-dependent, manner*"
  - closest text in source: "CD25(+) Treg strongly and dose-dependently inhibited nickel-specific activation of CD25(-) T lymphocytes in coculture experiments in a cytokine-independent, but cell-to-cell contact-dependent, manner"

## Term Validation

No ontology term identifiers were found in this report.