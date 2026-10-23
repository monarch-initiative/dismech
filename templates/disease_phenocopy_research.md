# Phenocopy Differential Research Template

## Target Disease
- **Disease Name:** {disease_name}
- **MONDO ID:** {mondo_id} (if available)

## Scope

This is a narrow differential-diagnosis report, not a disease survey. The
disease's own pathophysiology is already curated and is not in question. The
subject is the **phenocopy** of the disease: an acquired, reversible condition
that reproduces the disease's defining phenotype in a person who does not have
the disease. The specific question is:

{phenocopy_focus}

## Research Objectives

Please provide a focused research report on how the literature separates a
phenocopy of **{disease_name}** from the disease itself, with particular
attention to the question above. This report will be reconciled against a
knowledge-base entry that already records the phenocopy as a differential
diagnosis. Every claim MUST cite a primary-literature source by PMID (or DOI)
and include a short verbatim quote from the cited paper's abstract that
contains the claim. Do not paraphrase quotes. Do not invent PMIDs.

---

### 1. Definition and published classification of the phenocopy

- Who coined the term for this disease's phenocopy, when, and how has the
  definition been revised since? Cite each revision.
- List the published diagnostic criteria verbatim where possible, including
  any classification into confirmed versus probable cases, and state which
  criteria are mandatory.
- State the role of a **provocative test after the provoking condition has
  resolved**: is a negative result required, and what agent, dose and timing
  do the criteria specify?

### 2. Recognized provoking conditions and their etiologic categories

- List the etiologic categories used by the classification and by any
  registry, with the reported number or proportion of cases in each.
- For each category give one representative primary report with PMID and
  exact quote.
- Note any category that the classification authors have **explicitly
  excluded**, and quote their stated reason.

### 3. The contested category named in the question

Treat this as the core of the report.

- **Position A:** the provoking agent reveals latent disease that was already
  present, so the pattern is not a phenocopy. Who holds this position, and on
  what grounds? Quote them.
- **Position B:** a sufficient exposure produces the pattern in a person with
  no underlying disease, so it is a phenocopy. Who holds this position? Quote
  them.
- **Discriminating evidence:** report every case, case series or registry
  cohort in which a pattern provoked by this category was followed by a
  **provocative challenge after washout**, and give the result of that
  challenge. Tabulate: reference, agent, dose or exposure level, whether the
  exposure was therapeutic or supratherapeutic, time to ECG normalization,
  post-washout provocative test performed (yes/no), its result, genetic
  testing performed and its result, family history, and the label the authors
  applied.
- Report separately any cases labelled a phenocopy in which **no** post-washout
  provocative test was performed, and say so.
- State how the field's consensus documents and guidelines name a pattern
  provoked by this category (for example a distinct nomenclature for a
  drug-provoked pattern), and whether that nomenclature treats it as the
  disease, a phenocopy, or a third category. Quote the consensus text.

### 4. Dose and exposure dependence

- Is there evidence that the pattern appears in the general population at
  supratherapeutic exposure but only in susceptible individuals at therapeutic
  exposure? Report any dose-response, overdose series, or population-frequency
  data with PMIDs and quotes.
- Report the yield of genetic testing in people whose pattern was provoked by
  this category, if any study reports it.

### 5. Prognosis of the phenocopy versus the disease

- Report follow-up data on arrhythmic events in confirmed phenocopy cases, by
  etiologic category where available.
- Report whether an arrhythmia at presentation has been described in any
  phenocopy case, and how the authors reconciled it with the phenocopy label.

### 6. Verdict

- State a verdict on the question above, one of:
  - SETTLED — the field agrees on the classification of this category
  - CONTESTED — published positions disagree and the discriminating evidence
    does not settle it
  - UNKNOWN — the question has not been directly studied
- Name the single study design or registry analysis that would most
  efficiently resolve a CONTESTED or UNKNOWN verdict.
- Propose the minimal set of distinguishing features a knowledge-base
  differential-diagnosis entry should record, each tied to a citation above.

### 7. Ontology terms

- Suggest HP terms for the shared phenotype(s), and say whether any MONDO or
  HP term exists for the phenocopy itself. If none exists, say so explicitly
  rather than proposing a near match.

---

## Output requirements

- **Cite every claim by PMID** (or DOI) and include a verbatim quote from the
  cited abstract containing that claim.
- Keep Position A and Position B separate throughout; do not merge them into
  a single hedged statement.
- If a section has no published evidence, say "No published evidence
  identified" — do not invent cases or values.
- UNKNOWN and CONTESTED are correct and valuable verdicts. Do not promote a
  position to SETTLED to make the report tidier.
- Do not generate findings that cannot be tied to a real, retrievable
  reference.
