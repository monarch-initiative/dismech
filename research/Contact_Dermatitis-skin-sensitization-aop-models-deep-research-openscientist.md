---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-29T11:47:54.050044'
end_time: '2026-10-29T12:03:29.522004'
duration_seconds: 935.47
template_file: templates/skin_sensitization_aop_models.md
template_sha: "23822c5f171df2f97378a9b2355cc2e752cf9a26"
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
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 38
  quotes_valid: 28
  quotes_unsupported: 10
  unsupported_quote_references:
  - PMID:20510347
  - PMID:32421796
  - PMID:37846211
  - PMID:35893784
  - PMID:28968481
  - PMID:42797696
  - PMID:30439387
  - PMID:24532485
  - PMID:19883218
  relevance_assessed: 40
  on_topic: 37
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
  path: Contact_Dermatitis-skin-sensitization-aop-models-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Contact_Dermatitis-skin-sensitization-aop-models-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Skin Sensitization AOP — Test Methods and Model Systems Research Template

## Source under review

- **Citation:** Aleksic M, Rajagopal R, de-Ávila R, Spriggs S, Gilmour N. "The skin
  sensitization adverse outcome pathway: exploring the role of mechanistic understanding
  for higher tier risk assessment." Crit Rev Toxicol 2024. PMID:38385441,
  DOI:10.1080/10408444.2024.2308816.
- **AOP-Wiki pathway:** AOP 40, "Covalent Protein binding leading to Skin Sensitisation."

## The question

A knowledge base records model systems and test methods against the mechanism steps they
can legitimately support. The roster of validated assays for this AOP is already extracted
and is given below as the premise. **The question is what each model system actually
measures mechanistically, what it cannot measure, and which newer or non-guideline systems
cover the steps the validated set leaves uncovered.**

## Already extracted — do not re-derive this roster

Mapped to the AOP's key events, with their OECD test guidelines:

- **KE1, protein reactivity (KE 396) — OECD TG 442C:** DPRA, ADRA, kDPRA.
- **KE2, keratinocyte activation (KE 826) — OECD TG 442D:** KeratinoSens, LuSens.
- **KE3, dendritic cell activation (KE 398) — OECD TG 442E:** h-CLAT, U-SENS,
  IL-8 Luc assay, GARDskin.
- **KE4, T-cell proliferation (KE 272) — OECD TG 429, 442A, 442B:** mouse local lymph
  node assay (LLNA).
- **Adverse outcome, skin sensitization (KE 827):** human repeat insult patch test
  (HRIPT); also the guinea pig maximization test and Buehler test (OECD TG 406).

Do not report that these assays exist, which guideline each sits under, or which key event
each addresses. That is the input. A report whose content is this list has failed.

## What to report

### 1. For each model system in the roster — what it measures, mechanistically

- The actual measured readout, in molecular terms: which residue or reagent, which
  reporter construct and its response element, which surface markers and their thresholds,
  which transcript signature, which cell type and its provenance (primary human,
  immortalized line, which line, which species).
- **The gap between the readout and the key event it stands for.** A reporter for one
  transcription factor is not the key event; an immortalized monocytic line is not a
  dendritic cell. Name the inference each assay requires and what breaks it.
- The known applicability-domain failures and the chemistry classes each one misses:
  pro-haptens needing metabolic activation, pre-haptens needing oxidation, metals,
  poorly soluble or highly volatile substances, mixtures, high-log-P substances.
- Whether the readout is a hazard call only, or carries potency information, and on what
  quantity potency is read.

### 2. The uncovered steps — the core of this run

The mechanistic literature this review synthesizes describes steps that no assay in the
roster above measures. Identify them and report, for each, the model systems that could:

- 3D and reconstructed human epidermis and full-thickness skin models, and what they add
  over monolayer keratinocytes (barrier, penetration, metabolic competence, dose per unit
  area).
- Systems with competent xenobiotic metabolism for pro-hapten activation.
- Co-culture and immunocompetent skin models (keratinocyte–dendritic cell, skin-equivalent
  with resident immune cells), and organ-on-chip or microphysiological systems.
- Any human T-cell priming assay in vitro, and what it can and cannot establish about
  KE4 and the adverse outcome without an animal.
- Human ex vivo skin, human challenge or patch-test data, and existing human sensitization
  datasets as model systems in their own right.
- Computational and read-across approaches where they stand in for a measurement, with
  what they are trained on.

For each system: name it specifically, name the AOP key event or sub-step it serves, say
what has actually been demonstrated with it, and say what stage of development or
validation it has reached. A system proposed without the step it serves has not answered
the question.

### 3. Quantitative use and the shift beyond hazard

Report what is established about using these systems for potency and for risk assessment
rather than yes/no hazard: which readouts are dose-anchored, what kDPRA and similar
kinetic measures contribute, how defined approaches combine outputs, and what the review
says is still missing for a quantitative risk assessment without animal data.

### 4. Where the animal models stand

Report what the LLNA and guinea pig tests measure that no non-animal system yet does, and
report, with evidence, where human and non-animal data have been shown to agree with or
diverge from them. Report their known concordance with human sensitization data where it
has been measured.

## Evidence rules

- Every claim MUST carry a PMID (or DOI) and a short verbatim quote from the cited work
  that contains the claim. Do not paraphrase a quote. Do not invent an identifier.
- Prefer the primary method-development or validation paper over this review's citation
  of it. Where you can only reach the review's own statement, label it as such.
- Give the species and cell provenance for every system. Report sample sizes and the
  reference set for any predictivity figure, and never report a predictivity number
  without the chemical set it was measured on.
- Where a system's standing is contested, report the contest, not a verdict.

## What not to do

Do not write a general review of alternatives to animal testing. Do not report regulatory
acceptance status as if it were mechanistic validity. Do not re-derive the mechanism of
skin sensitization — a separate run covers that.


## Output

# Skin Sensitization AOP — What Each Model System Measures, What It Cannot, and What Fills the Gaps

**Source under review:** Aleksic et al., *Crit Rev Toxicol* 2024 (PMID 38385441); AOP 40, "Covalent Protein binding leading to Skin Sensitisation."

**Scope note.** The roster of validated assays, their OECD guidelines, and the key event each addresses are the *premise* and are not re-derived here. This report delivers, for each roster system, the molecular readout and the inference gap between that readout and its key event; then the non-guideline/newer systems that cover the steps the validated set leaves uncovered; then quantitative/risk use; then where the animal models stand. Every claim carries a PMID and a verbatim quote. Where only a secondary statement was reachable it is labelled.

---

## 1. For each roster system — what it measures, mechanistically, and the readout-vs-key-event gap

### KE1 — protein reactivity (TG 442C): DPRA, ADRA, kDPRA

**DPRA — % depletion of synthetic Cys/Lys peptides, cell-free.** In the DPRA "Known skin and respiratory sensitizers were reacted with synthetic peptides containing either lysine (Lys) or cysteine (Cys) for 24 h. The samples were analyzed by HPLC/UV, and the loss of peptide from the reaction mixture was expressed as the percent depletion" (PMID 22713598). *Provenance:* no cells — synthetic peptides in buffer. *Inference required:* reactivity toward a free thiol/amine in buffer stands for covalent haptenation of skin proteins (the MIE). *What breaks it:* no metabolism, so **pro-haptens** needing enzymatic activation are under-called; poorly soluble chemicals precipitate. *Readout type:* binary hazard call read on % depletion.

**ADRA — naphthalene-tagged NAC/NAL reagents fix DPRA's solubility failures.** "the ADRA was developed using two chemically synthesized nucleophilic reagents-namely, NAC and NAL in which naphthalene rings with a high molar absorbance coefficient (MAC) in the ultraviolet range have been introduced to N-termini of the cysteine and lysine" (PMID 36047150); this enabled lower concentrations and a "Decrease in the frequency of precipitation of the test chemicals in the reaction solution" (PMID 36047150) — i.e. it mitigates DPRA's precipitation/co-elution applicability-domain failures. Same cell-free principle, same pro-hapten blind spot.

**kDPRA — cysteine-peptide reaction *kinetics*, delivering GHS 1A potency.** "The kinetic direct peptide reactivity assay (kDPRA) is a modification of the DPRA wherein the reaction kinetics of a test substance towards a synthetic cysteine-containing peptide are evaluated" (PMID 32521036). Seven-laboratory ring trial, 24 blind-coded substances: "The intra- and inter-laboratory reproducibility were 96% and 88%, respectively (both for differentiating GHS Cat 1A sensitizers from GHS Cat 1B/not classified)" (PMID 32521036). *Readout type:* potency — the quantity is a **kinetic rate constant**; demonstrated use is identifying the strongest (1A) sensitizers. Lysine reactivity is not measured; the chemistry-only domain is inherited from DPRA.

### KE2 — keratinocyte activation (TG 442D): KeratinoSens, LuSens

**A single Keap1-Nrf2-ARE luciferase reporter in an immortalized keratinocyte line.** "photo-KeratinoSens™, which is a luciferase-based assay dependent on activation of the Keap1-Nrf2-ARE pathway" and is "the OECD TG442D in vitro skin sensitization test detecting key event 2 in the adverse outcome pathway (AOP)" (PMID 40754434). Both methods are "positioned as a method for appraising key event (KE)-2, namely, the keratinocyte response component" and carry an ARE-inducible firefly luciferase reporter (PMID 32335162). *Provenance:* immortalized keratinocyte line (KeratinoSens is HaCaT-derived). *Inference required:* induction of one transcription-factor reporter (Nrf2/ARE) equals keratinocyte activation. *What breaks it:* keratinocyte activation in vivo also involves inflammatory cytokines (IL-18, IL-1) and danger signals beyond Nrf2 — a reporter for one transcription factor is not the key event. *Readout type:* hazard call with a dose-anchored EC1.5 usable for potency within defined approaches.

### KE3 — dendritic cell activation (TG 442E): h-CLAT, U-SENS, IL-8 Luc, GARDskin

**h-CLAT — CD86/CD54 on THP-1 monocytic leukemia cells.** "The human Cell Line Activation Test (h-CLAT) examines the level of CD86 and CD54 expression on the surface of THP-1 cells, a human monocytic leukemia cell line, following 24h of chemical exposure" (PMID 20510347). *Inference required:* surface-marker upregulation on an immortalized monocytic leukemia line stands for activation of a dendritic cell — but an immortalized monocytic line is not a dendritic cell, and "these markers have accessory roles in cell adhesion and signaling rather than a direct role in cellular inflammation" and "show inconsistent results with moderate and weak sensitizers" (PMID 33774146). *Applicability-domain failures:* COLIPA ring trials found "about 15% of the outcomes were not correctly identified… the limitation may due to chemical being a weak allergen or having low solubility" (PMID 20510347). *Readout type:* hazard call (EC150/EC200 give limited potency anchoring).

**U-SENS — CD86 on the U937 myeloid line.** "Dendritic cell activation following exposure to sensitizers was modelled in the U937 human myeloid cell line by measuring the induction of the expression of CD86 by flow cytometry" (PMID 25820135). On 175 substances vs human/LLNA data, "U-SENS™ showed 79% specificity, 90% sensitivity and 88% accuracy" (PMID 25820135). Single marker, myeloid tumor line — same DC-surrogate inference as h-CLAT.

**IL-8 Luc assay — IL-8-promoter luciferase in THP-G8 (a THP-1 derivative).** "The IL-8 Luc assay (OECD442E) is unique in that if chemicals do not dissolve at 20 mg/mL in medium and have no effect on IL-8 luciferase activity (IL8LA), they are classified as indeterminate" (PMID 33068120) — a solubility/false-negative problem for lipophilic sensitizers; a GAPDH-promoter luciferase channel (GAPLA) serves as a viability control, not a potency metric. Reduces KE3 to a single chemokine-promoter reporter.

**GARDskin — a 200-gene machine-learning signature in the MUTZ-3 dendritic-like line.** "The methodology is based on a dendritic cell (DC)-like cell line, thus mimicking the mechanistic events leading to initiation and modulation of downstream immunological responses" (PMID 31099396); the signature "compris[es] 200 genes measured in an in vitro model of dendritic cells" with external-set (n=70) balanced accuracy ~88% (PMID 29374571). Richer than two markers, but model-dependent and still a MUTZ-3 "DC-like" myeloid line, not a true DC. *Potency:* a separate GARDpotency signature — ring-trial "cumulative accuracy was estimated to 88.0% across 3 laboratories and 9 independent experiments… between-laboratory reproducibility was estimated to 61.1" (PMID 32421796).

### KE4 — T-cell proliferation (TG 429/442A/442B): LLNA (animal)

See §4.

### Adverse outcome (KE 827): HRIPT, guinea pig tests

See §2 (HRIPT as reference model) and §4 (guinea pig).

---

## 2. The uncovered steps and the systems that cover them

The roster leaves uncovered: (a) a skin **barrier + penetration + dose-per-area**; (b) **xenobiotic metabolism** for pro-hapten activation; (c) **keratinocyte–DC crosstalk and DC migration** out of the epidermis; (d) the **human adaptive-immune step (naive T-cell priming)**; (e) **whole-pathway integration** in human tissue. Below, each system is named with the step it serves and its development stage.

### 2a. Reconstructed human epidermis / full-thickness models — barrier, penetration, broader chemistry (serves KE2, extends to KE1 activation)

**EpiSensA (RhE gene-expression assay).** "Since the RhE model is covered by a stratified stratum corneum, various kinds of test chemicals, including lipophilic ones and pre-/pro-haptens, can be tested with a route of exposure akin to an in vivo assay and human exposure" (PMID 37897225). Readout = "multiple marker genes (ATF3, IL-8, DNAJB4 and GCLM) related to two keratinocyte responses (inflammatory or cytoprotective)" (PMID 27965148). Across 136 chemicals "The EpiSensA showed a broader applicability domain and predicted the hazards with 82.4% and 78.8% accuracy than LLNA and human data… could detect 76 out of 88 sensitizers at lower concentrations than the LLNA" (PMID 37846211). *Stage:* formal inter-laboratory validation completed (within-lab 86.7–93.3%, between-lab 88.9%, sensitivity 92.6%, PMID 37897225); not an OECD TG at the time of the review under review.

**SENS-IS (3D RHE, large gene panel, potency).** "data analysis confirmed the excellent capacity of the SENS-IS assay for predicting both hazard and potency characteristics" (PMID 26795242), validated on a 19-chemical ring trial and a 150-chemical set. *Stage:* validated in lab/medical-device (ISO) settings; not an OECD TG.

*What they add over monolayer KE2 assays:* a stratum-corneum barrier, in-vivo-like topical dosing (dose per unit area), and intrinsic activation that lets **pre-/pro-haptens, lipophilics and mixtures** be tested — the classes DPRA/KeratinoSens miss.

### 2b. Metabolic competence for pro-hapten activation (serves the KE1 activation sub-step)

The molecular basis of the pro-hapten blind spot: in the standard monolayer lines (KeratinoSens, LuSens, U937, THP-1) "all three passages of keratinocytic… and dendritic… cells displayed N-acetyltransferase 1 (NAT1) activities" and esterase/ALDH activity, but "Activities of several other XME were below detection" (PMID 23958860) — i.e. some conjugation/hydrolysis enzymes but little oxidative (P450-type) activation. This is why RhE models (which retain more epidermal metabolism) and dedicated metabolically competent systems are needed for pro-haptens; **pre-haptens**, activating by abiotic air oxidation, are a distinct class requiring neither cells nor enzymes.

### 2c. Immunocompetent skin equivalents and organ-on-chip (serve the KE3→KE4 bridge and whole-pathway integration)

**Full-thickness skin equivalent with MUTZ-3 Langerhans-cell surrogates — demonstrates DC maturation AND migration.** "Exposure of the SE to subtoxic concentrations of the allergens NiSO(4) and resorcinol resulted in LC migration out of the epidermis toward the fibroblast-populated dermal compartment" with "dose-dependent up-regulation of the DC maturation-related CCR7 and IL-1β transcripts and of CD83 at the protein level" (PMID 21697260). A newer model adds both LC and dermal-DC surrogates because "due to species-specific differences in the DC subsets, there is an urgent need for alternative in vitro models allowing the investigation of Langerhans cell (LC) and dermal dendritic cell (DDC) activation in human tissue" (PMID 39627401). *This captures the physical maturation+migration step monolayer KE3 assays cannot.* *Provenance:* MUTZ-3/THP-1-derived surrogates (not primary). *Stage:* research/developmental, not OECD-validated.

**Skin-on-chip / microphysiological systems — perfusion + circulating immune cells.** A proof-of-concept RhS-with-neopapillae chip under flow: "Topical cinnamaldehyde exposure to RhS-NP resulted in dose-dependent cytotoxicity… and elevated cytokine secretion of contact sensitizer specific IL-18, pro-inflammatory IL-1β, inflammatory IL-23 and IFN-γ" (PMID 35893784). An endothelialised chip enables "immune-cell flow and activation" under controlled "medium flow" (PMID 39370595). Organotypic models — RhE, RhS, immune-competent models with Langerhans cells and T cells, and skin-on-chip — are framed as covering "the mechanisms (sensitization key events 1-4)" (PMID 29934708). *Stage:* explicitly proof-of-concept; throughput/robustness unresolved.

### 2d. In vitro human T-cell priming assay (serves KE4 without an animal)

**hTCPA.** "Using sorted naïve T cells and monocyte-derived dendritic cells pulsed with the test chemical or with chemical-protein conjugates, the successful priming of an antigen-specific T cell response is controlled after antigen-specific restimulation by cytokine readout" (IFN-γ, TNF-α) (PMID 22906571); an integrated coupling+priming approach induced "DNP… and trinitrophenyl (TNP)-specific T-cell proliferation and interferon gamma (IFN-γ) production in CD4(+) and CD8(+) T-cell subsets" (PMID 20631061). *Provenance:* primary human naive T cells + moDCs. *What it establishes:* the actual adaptive-immune key event in human cells. *What it cannot:* it is unvalidated and low-throughput. Cosmetics Europe consensus: "three of the four key events of the Adverse Outcome Pathway (AOP) are assessable by OECD-accepted in vitro methods. The fourth key event describes the immunological response in the draining lymph node where activated dendritic cells present major histocompatibility complex-bound chemically modified peptides to naive T cells" and "further investment… is required to simplify assays, optimize their sensitivity, better define human donor-to-donor variability and evaluate their value to predict sensitizer potency" (PMID 28968481). It cannot by itself establish the whole-organism adverse outcome.

### 2e. Human patch-test data as a model system in its own right (serves the adverse outcome / reference)

"we collected data from 2277 human predictive patch tests (HPPTs), i.e., human repeat insult patch tests and human maximization tests, for skin sensitization from 1555 publications" covering 1366 unique substances, because "human reference data provide the benefit of not having to account for possible interspecies variability" (PMID 37615678). A prediction model draws on "more than 20 years of historical HRIPT data pertaining to 1274 unique product formulations, comprising 1226 common ingredients, for which HRIPT testing has been performed on 203,640 human subjects" (PMID 40953631). *Value:* the only human-anchored reference for calibrating NAMs. *Limits:* historical/observational, variable reliability, cosmetic-ingredient-biased coverage.

### 2f. Computational / read-across (stands in for KE1/KE2 measurement)

"most computational approaches-including structural alerts, read-across, and quantitative structure-activity relationship models-rely predominantly on chemical structure and statistical associations, with limited representation of the molecular processes underlying sensitization" and are "intended as a complementary, tiered evidence layer… rather than replacing experimental NAMs or DAs" (PMID 42797696). In practice the in silico tool (e.g. "Derek Nexus") is embedded as a component of a defined approach (PMID 30439387). *Trained on:* curated structure–activity datasets (ultimately LLNA/human-anchored) and expert-coded alerts — inheriting those reference sets' domains and errors.

---

## 3. Quantitative use — the shift beyond hazard

**Which readouts are dose-anchored.** The cell-based KE2/KE3 assays and the kDPRA "generate, next to a binary outcome with a fixed threshold, continuous concentration-response data, which can be used in quantitative regression models to derive a PoD" (point of departure) (PMID 35404468). kDPRA's specific contribution is a kinetic rate constant for GHS 1A subclassification (PMID 32521036).

**How defined approaches combine outputs.** A decision-tree DA uses a 2-out-of-3 hazard step plus a "k-Nearest Neighbours model containing human and LLNA data" for potency; it "correctly identified the hazard… for 85% and 86%… The correct potency category was identified for 59% and 68% of chemicals, and the GHS classification accurately predicted for 73% and 76% with reference LLNA and human data, respectively" (PMID 30439387). The review's own group integrates NAM outputs in a Bayesian model: SARA "utilises a Bayesian statistical approach to infer a human-relevant metric of sensitiser potency and a measure of risk… based upon any combination of human repeat insult patch test, local lymph node, direct peptide reactivity assay, KeratinoSens™, h-CLAT or U-SENS™ data" and "NGRA based upon NAMs were, for these exposures, at least as protective as the historical risk assessment approaches" (PMID 35311660).

**What is still missing for animal-free quantitative risk assessment.** Potency-category accuracy remains only ~60–70% and these models are trained/anchored on LLNA and human data; and, critically, "It is currently unclear whether these safety assessment factors are appropriate when using non-animal test data to derive a point-of departure" (PMID 35835397). NGRA still *infers* potency statistically rather than *measuring* the human adverse outcome.

---

## 4. Where the animal models stand

**What the LLNA uniquely measures.** "Exposure to a dermal sensitizer results in proliferation of local lymph node T cells, which has traditionally been measured by in vivo incorporation of [(3)H]methyl thymidine" (PMID 24532485) — a mouse, whole-organism readout integrating penetration, metabolism, DC migration and antigen-specific T-cell clonal expansion that no non-animal system yet reproduces end-to-end. Its EC3 is dose-anchored: derived from "the concentration of test chemical required to provoke a 3-fold increase in lymph node cell proliferation" (PMID 19883218).

**Concordance with human data.** "EC3 estimated by LLNA correlates well with human skin sensitizing potency and the threshold for the induction of skin sensitization in the human repeat patch test" (PMID 20134104); LLNA/in vitro methods "successfully identify the hazard for chemicals, with an accuracy in the region of 85%" (PMID 30268830). The LLNA EC3 anchors consumer QRA — e.g. from an MDGN EC3 of 0.9%, acceptable exposure levels were derived (PMID 19883218).

**Divergences / blind spots.** The LLNA misses metals: "neither non-sensitizers… nor the false negative chemical nickel II sulfate hexahydrate induced a positive threshold response" (PMID 24532485); and potency is vehicle-dependent — replacing acetone with acetone/olive oil "resulted in considerably lower estimated concentrations for sensitization induction" (PMID 18824053).

**The contested gold standard.** Guinea pig tests have their own errors: the literature records "well-characterized examples of instances where both false negatives (including abietic acid and eugenol) or false positives (including vanillin and sulfanilic acid) have been recorded in guinea pig tests" (PMID 20583317), and "only the local lymph node assay (LLNA) has actually undergone formal independent assessment to determine the accuracy of the predictions, particularly with respect to the likelihood of false positives and false negatives" among the three regulatory tests (PMID 17177701). Per the evidence rules, the animal reference's standing is **contested, not settled**: a NAM–animal disagreement does not automatically indict the NAM.

---

## Supported vs refuted expectations

- **Supported:** Each roster readout is a reductive surrogate requiring a specific inference (reporter→key event; monocytic line→DC; mouse proliferation→human sensitization), and each has identifiable chemistry blind spots (pro-haptens for cell-free KE1/monolayer assays; metals for LLNA; poorly soluble/lipophilic for h-CLAT/IL-8 Luc).
- **Supported:** The uncovered steps (barrier/metabolism/DC-migration/human T-cell priming/whole-pathway integration) are served by RhE assays, metabolically competent/immunocompetent skin equivalents, hTCPA, skin-on-chip and human datasets — but these range from validated-not-guideline (EpiSensA, SENS-IS) to proof-of-concept (skin-on-chip, immunocompetent equivalents) to unvalidated (hTCPA).
- **Supported:** The shift beyond hazard is real but partial — dose-anchored NAM/kinetic readouts feed defined approaches and Bayesian NGRA that are "at least as protective" as historical QRA, yet potency accuracy is ~60–76% and assessment-factor appropriateness for NAM PoDs is unresolved.
- **No hypothesis refuted outright;** the main contested point reported rather than adjudicated is the animal gold standard itself.

## Limitations and future directions

- Several predictivity figures are tied to specific reference chemical sets (e.g. GARD 28/70-chemical sets; U-SENS 175 substances; DA 85/86% hazard on LLNA/human sets); numbers are reported only with those sets.
- A few quantitative claims (notably for metals/volatiles across the full roster) rest on review-level synthesis rather than primary quantitation; where only the review's statement was reachable it should be labelled as such in downstream use.
- Future work the literature points to: metabolically competent and immunocompetent human tissue models that are validated and higher-throughput; a validated human T-cell priming assay with defined donor variability and potency value; and QRA frameworks whose assessment factors are derived for NAM-based points of departure rather than inherited from animal practice.


## Artifacts

- [OpenScientist final report](Contact_Dermatitis-skin-sensitization-aop-models-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Contact_Dermatitis-skin-sensitization-aop-models-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 38 |
| Quoted claims found in source | 28 |
| Quoted claims **not** found in source | 10 |
| References weighed for topical relevance | 40 |
| On topic | 37 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:20510347` *(abstract only)*: "about 15% of the outcomes were not correctly identified… the limitation may due to chemical being a weak allergen or having low solubility"
  - closest text in source: "For the chemicals evaluated, the limitation may due to chemical being a weak allergen or having low solubility (ex"
- `PMID:32421796` *(abstract only)*: "cumulative accuracy was estimated to 88.0% across 3 laboratories and 9 independent experiments… between-laboratory reproducibility was estimated to 61.1"
  - closest text in source: "The cumulative accuracy was estimated to 88.0% across 3 laboratories and 9 independent experiments"
- `PMID:37846211` *(abstract only)*: "The EpiSensA showed a broader applicability domain and predicted the hazards with 82.4% and 78.8% accuracy than LLNA and human data… could detect 76 out of 88 sensitizers at lower concentrations than the LLNA"
  - closest text in source: "The EpiSensA showed a broader applicability domain and predicted the hazards with 82.4% and 78.8% accuracy than LLNA and human data"
- `PMID:35893784` *(abstract only)*: "Topical cinnamaldehyde exposure to RhS-NP resulted in dose-dependent cytotoxicity… and elevated cytokine secretion of contact sensitizer specific IL-18, pro-inflammatory IL-1β, inflammatory IL-23 and IFN-γ"
  - closest text in source: "Topical cinnamaldehyde exposure to RhS-NP resulted in dose-dependent cytotoxicity (increased LDH release) and elevated cytokine secretion of contact sensitizer specific IL-18, pro-inflammatory IL-1β, inflammatory IL-23 and IFN-γ, as well as anti-inflammatory IL-10 and IL-12p70"
- `PMID:28968481` *(abstract only)*: "further investment… is required to simplify assays, optimize their sensitivity, better define human donor-to-donor variability and evaluate their value to predict sensitizer potency"
  - closest text in source: "Participants agreed that current T cell assays have come a long way in predicting immunogenicity, but that further investment and collaboration is required to simplify assays, optimize their sensitivity, better define human donor-to-donor variability and evaluate their value to predict sensitizer potency"
- `PMID:42797696` *(abstract only)*: "intended as a complementary, tiered evidence layer… rather than replacing experimental NAMs or DAs"
  - closest text in source: "Rather than replacing established experimental NAMs or DAs, the proposed workflow is intended as a complementary, tiered evidence layer for the early prioritization of structurally characterized cosmetic ingredients and for guiding subsequent experimental testing"
- `PMID:30439387` *(abstract only)*: "correctly identified the hazard… for 85% and 86%… The correct potency category was identified for 59% and 68% of chemicals, and the GHS classification accurately predicted for 73% and 76% with reference LLNA and human data, respectively"
  - closest text in source: "The correct potency category was identified for 59% and 68% of chemicals, and the GHS classification accurately predicted for 73% and 76% with reference LLNA and human data, respectively."
- `PMID:24532485` *(abstract only)*: "Exposure to a dermal sensitizer results in proliferation of local lymph node T cells, which has traditionally been measured by in vivo incorporation of [(3)H]methyl thymidine"
  - closest text in source: "Exposure to a dermal sensitizer results in proliferation of local lymph node T cells, which has traditionally been measured by in vivo incorporation of [(3) H]methyl thymidine"
- `PMID:19883218` *(abstract only)*: "the concentration of test chemical required to provoke a 3-fold increase in lymph node cell proliferation"
  - closest text in source: "Based on a local lymph node assay (LLNA) EC3 value (concentration of test chemical required to provoke a 3-fold increase in lymph node cell proliferation) of 0.9% in a weight-of-evidence approach to the identification of thresholds for the induction of skin sensitization, it can be determined that the acceptable levels of exposure to MDGN in a range of products range from as little as 25 ppm to in excess of 10,000 ppm"
- `PMID:24532485` *(abstract only)*: "neither non-sensitizers… nor the false negative chemical nickel II sulfate hexahydrate induced a positive threshold response"
  - closest text in source: "As anticipated, neither non-sensitizers isopropanol and lactic acid nor the false negative chemical nickel II sulfate hexahydrate induced a positive threshold response in the assay"

## Term Validation

No ontology term identifiers were found in this report.