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
