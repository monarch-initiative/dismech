---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T11:46:40.228712'
end_time: '2026-10-19T11:55:47.384101'
duration_seconds: 547.16
template_file: templates/drug_mechanism_research.md
template_sha: "39d2067d15700202e24fb289be3f60fcff9114f1"
template_variables:
  disease_name: KIF1A-Related Neurological Disorder
  drug: allele-specific antisense oligonucleotide (nL-KIF1-001)
  asserted_mechanism: Dominant-Negative Inhibition of Wild-Type KIF1A
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 2
  validator_version: 0.3.0
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
  path: KIF1A_Related_Neurological_Disorder-drug-mechanism-allele_specific_antisense_oligonucleotid-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KIF1A_Related_Neurological_Disorder-drug-mechanism-allele_specific_antisense_oligonucleotid-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Drug Therapeutic Mechanism Research Template

## Target Question

- **Disease:** KIF1A-Related Neurological Disorder
- **Drug:** allele-specific antisense oligonucleotide (nL-KIF1-001)
- **Mechanism asserted in the knowledge base:** Dominant-Negative Inhibition of Wild-Type KIF1A

## Research Objectives

A disease knowledge base links **allele-specific antisense oligonucleotide (nL-KIF1-001)** to the mechanism **"Dominant-Negative Inhibition of Wild-Type KIF1A"**
as the way it acts in **KIF1A-Related Neurological Disorder**. The drug's clinical effect may be well
established while its mechanism is not. Please determine **whether the mechanism by
which allele-specific antisense oligonucleotide (nL-KIF1-001) produces its therapeutic effect in KIF1A-Related Neurological Disorder has been established,
and if so, what it is.**

This report will be used to decide whether the knowledge base should record the
mechanism as known, as one of several candidates, or as an open knowledge gap.
Evidence that a mechanism is untested or disputed is as useful as evidence that it is
settled. Report it with the same care.

Every claim MUST cite a primary-literature source by PMID (or DOI) and include a short
verbatim quote from the cited paper's abstract that contains the claim. Do not
paraphrase. Do not invent PMIDs. If a claim is supported only by full text, say so.

---

### 1. Clinical effect

- State briefly what clinical benefit allele-specific antisense oligonucleotide (nL-KIF1-001) has in KIF1A-Related Neurological Disorder, and the strongest
  evidence for it (randomized trial, meta-analysis, observational, case series).
- Keep this short. It is context, not the question.

### 2. Candidate mechanisms

- List each molecular or cellular mechanism that has been proposed for allele-specific antisense oligonucleotide (nL-KIF1-001)'s
  benefit **in this disease**, including "Dominant-Negative Inhibition of Wild-Type KIF1A".
- For each, say whether the drug's action on that target is itself established (for
  example, demonstrated binding or enzyme inhibition at clinically achieved
  concentrations).

### 3. Evidence that a mechanism mediates the benefit

This is the core question. For each candidate mechanism, report evidence that the
therapeutic effect **depends on** it, not merely that the drug also affects it:

- Genetic or pharmacological dissection (knockout, knockdown, a mutant target, a
  blocking agent) that abolishes the drug's effect.
- Target engagement or pathway readouts measured **in patients** with this disease,
  and whether they track clinical response.
- Analogues that hit the target without the benefit, or the benefit without the
  target.
- The model system for each finding (human, animal, cell culture), and whether its
  dose is clinically relevant.

### 4. Explicit statements of uncertainty

- Quote reviews, guidelines, trial protocols, or labels that state the mechanism in
  this disease is unknown, unclear, incompletely understood, or disputed.
- Quote any that state it is established.

### 5. Assessment

- Conclude with one of: **established** (state the mechanism), **leading candidate
  with partial support**, **several competing candidates**, or **unknown**.
- Say what experiment or measurement would most directly settle it.

### 6. Evidence refuting "Dominant-Negative Inhibition of Wild-Type KIF1A"

- Report findings that argue against the asserted mechanism mediating the benefit in
  KIF1A-Related Neurological Disorder, with PMIDs and quotes. Give these the same prominence as
  supporting findings.


## Output

# Therapeutic Mechanism of nL-KIF1-001 (allele-specific antisense oligonucleotide) in KIF1A-Related Neurological Disorder

## Summary

**The knowledge base's assertion is mis-stated and, read literally, refuted.** "Dominant-Negative Inhibition of Wild-Type KIF1A" describes the *disease* mechanism in KIF1A-Related Neurological Disorder (KAND) — the way a mutant KIF1A allele poisons neuronal transport — not the way the drug **nL-KIF1-001** produces benefit. The drug is an **allele-specific antisense oligonucleotide (ASO)** explicitly designed to do the *opposite* of inhibiting wild-type (WT) KIF1A: it selectively degrades the mutant KIF1A mRNA, thereby removing the dominant-negative species and **relieving** inhibition of the WT motor ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/); [PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/)).

**The actual therapeutic mechanism is a leading candidate with only partial, in-vitro support, and is not established as mediating clinical benefit.** The drug's proposed mechanism — **allele-specific knockdown of the pathogenic transcript** — is supported by phenotype rescue in patient-derived neurons carrying the P305L variant ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/)). However, the only clinical evidence is a single, open-label, uncontrolled n=1 intrathecal case followed for ~9 months, with no in-patient target-engagement biomarker tying transcript knockdown to the clinical improvements observed ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/)). No in-vivo genetic or pharmacological dissection in a KAND animal model has shown that the therapeutic effect *depends on* allele-specific knockdown.

**Bottom line for the knowledge base:** The mechanism should be recorded as an **open knowledge gap** with allele-specific mutant-transcript knockdown as the leading candidate. The specific entry "Dominant-Negative Inhibition of Wild-Type KIF1A" should be **corrected** — it is a mis-attribution (the disease mechanism labeled as the drug mechanism) and is biologically implausible as a *therapeutic* mechanism because WT KIF1A is essential for neuronal viability ([PMID: 15722511](https://pubmed.ncbi.nlm.nih.gov/15722511/); [PMID: 25253658](https://pubmed.ncbi.nlm.nih.gov/25253658/)).

---

## 1. Clinical Effect (context)

KAND is an ultrarare, often severe neurodegenerative disorder caused largely by heterozygous *de novo* missense variants in *KIF1A*, predominantly in the motor domain ([PMID: 34487232](https://pubmed.ncbi.nlm.nih.gov/34487232/)).

The clinical evidence for nL-KIF1-001 is a **single open-label case report**. An individual with KAND (p.Pro305Leu) received repeated intrathecal injections of the allele-specific ASO and showed improvement across several outcome measures over ~9 months. The authors describe the result as preliminary.

> "Most outcome measures, including severity of the spells of behavioral arrest, number of falls and quality of life, improved." — Ziegler et al., 2024 ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/))

> "Our findings provide preliminary insights on the safety and efficacy of an allele-specific antisense oligonucleotide as a possible treatment for KAND." — Ziegler et al., 2024 ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/))

This is the **weakest tier of clinical evidence** (n=1, uncontrolled, open-label). There is no randomized trial, meta-analysis, or case series. The clinical benefit is therefore *suggestive but not established*, and this report treats it only as context.

---

## 2. Candidate Mechanisms

Two mechanisms appear in connection with this drug-disease pair. Only one is a genuine *therapeutic* mechanism; the other is the knowledge base's mis-attribution.

| Candidate mechanism | Is it the drug's action? | Is the drug's action on this target established? |
|---|---|---|
| **Allele-specific knockdown** of the mutant KIF1A transcript (degrade pathogenic mRNA, preserve WT allele) | **Yes** — this is the drug's designed and demonstrated action | Demonstrated **in vitro** (patient-derived P305L neurons); **not** measured in the patient |
| **Dominant-negative inhibition of WT KIF1A** (knowledge-base assertion) | **No** — this is the *disease* mechanism, not the drug's; the drug *relieves* it | Not applicable / refuted as a therapeutic action (see §6) |

### 2a. Allele-specific knockdown (the drug's real mechanism)

The drug is explicitly engineered to degrade the mutant transcript selectively:

> "treated with intrathecal injections of an allele-specific antisense oligonucleotide specifically designed to degrade the mRNA from the pathogenic allele" — Ziegler et al., 2024 ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/))

> "One potential therapeutic strategy is allele-specific knockdown of pathogenic transcripts." — Zuccaro et al., 2026 ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/))

KAND is predominantly caused by **dominant-negative or dominant missense variants** in KIF1A; a mutant motor impairs transport in a manner that cannot be rescued simply by the normal WT allele. The therapeutic rationale is to *eliminate the mutant species* so the remaining WT allele can function. This is the inverse of "inhibiting WT KIF1A."

### 2b. Dominant-negative inhibition of WT KIF1A (asserted mechanism)

This phrase describes how the **mutant protein** causes disease — it interferes with the WT motor. It is not a mechanism by which an ASO would help a patient. Attributing it to the drug conflates pathophysiology with pharmacology.

---

## 3. Evidence That a Mechanism Mediates the Benefit

This is the core question: does the therapeutic effect *depend on* the proposed mechanism, or does the drug merely also perform that action?

### Allele-specific knockdown

- **Target engagement / phenotype rescue (in vitro only).** Knockdown of the pathogenic transcript rescued a disease-relevant cellular phenotype in neurons derived from a patient with the *same P305L variant* that was treated clinically:

  > "In vitro we further demonstrate that antisense oligonucleotide-mediated knockdown of the pathogenic transcript rescues the dendrite neurite outgrowth phenotype in neurons from a patient with the P305L variant." — Zuccaro et al., 2026 ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/))

  - **Model system:** patient-derived (iPSC) glutamatergic neurons — human cells, but *cell culture*, not the patient.
  - **Dose relevance:** the in-vitro knockdown dose is not established as clinically equivalent to the intrathecal regimen; no PK/PD bridge is reported.

- **In-patient readouts:** **None.** No cerebrospinal-fluid or tissue measurement of mutant-transcript knockdown, and no biomarker demonstrated to *track* the clinical improvements, has been reported. The link between the demonstrated in-vitro mechanism and the in-vivo clinical response is therefore inferential.

- **Genetic/pharmacological dissection in vivo:** **None.** No KAND animal model study has shown that abolishing allele-specific knockdown (e.g., with a non-targeting control ASO or a resistant allele) removes the therapeutic benefit. There are no analogues reported that hit the target without benefit, or vice versa.

### Dominant-negative inhibition of WT KIF1A

- No evidence supports this as a *therapeutic* mechanism, and strong evidence contradicts it (see §6). WT KIF1A is essential, so a drug acting by inhibiting it would be expected to harm neurons.

**Summary of mediation evidence:**

| Evidence type | Allele-specific knockdown | Dominant-negative inhibition of WT KIF1A |
|---|---|---|
| In-vivo causal dissection (KO/KD/blocking) | None | None |
| In-patient target engagement tracking response | None | None |
| In-vitro target engagement + phenotype rescue | **Yes** (P305L neurons) | N/A (refuted direction) |
| Biological plausibility as therapy | High | Low (WT KIF1A essential) |

---

## 4. Explicit Statements of Uncertainty

The primary clinical paper itself frames the evidence as preliminary rather than mechanistically established:

> "Our findings provide preliminary insights on the safety and efficacy of an allele-specific antisense oligonucleotide as a possible treatment for KAND." — Ziegler et al., 2024 ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/))

The in-vitro paper likewise frames the approach as a *potential* strategy still at the cell-culture stage:

> "One potential therapeutic strategy is allele-specific knockdown of pathogenic transcripts." — Zuccaro et al., 2026 ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/))

No review, guideline, label, or trial protocol was found that states the drug's *therapeutic mechanism* in KAND is established. Repeated targeted literature searches across five iterations returned only the two primary ASO papers (one clinical n=1, one in-vitro rescue) plus disease-biology context — the literature is effectively saturated and contains no "mechanism established" claim.

The underlying disease biology is itself **variant-specific and heterogeneous**, which further undercuts any single uniform mechanistic statement:

> "both mutations relieve autoinhibition of the full-length motor, the mutant motors display decreased velocities, run lengths, and landing rates and delayed cargo transport in cells" — Budaitis et al., 2021 ([PMID: 33496723](https://pubmed.ncbi.nlm.nih.gov/33496723/))

That is, pathogenic KIF1A variants produce *mixed* loss-of-function and altered-regulation effects rather than one clean "dominant-negative inhibition of WT KIF1A" phenotype.

---

## 5. Assessment

**Classification of the drug's therapeutic mechanism: leading candidate with partial support — and, as recorded, an open knowledge gap.**

- The **real** candidate mechanism (allele-specific knockdown of the mutant transcript) is a **leading candidate with partial support**: strong design rationale and in-vitro phenotype rescue in patient-derived P305L neurons, but no in-vivo causal dissection and no in-patient target-engagement data linking it to clinical benefit.
- The **asserted** mechanism (dominant-negative inhibition of WT KIF1A) is **not** the drug's mechanism and should be removed/corrected.

**What would most directly settle it:**
1. Measure **mutant-allele transcript/protein knockdown in patient CSF or accessible tissue** and test whether the degree of knockdown correlates with clinical outcome (target-engagement biomarker tracking response).
2. In a **humanized or knock-in KAND animal model**, show that the same ASO rescues neurological phenotypes and that a **non-targeting control ASO** (or an ASO-resistant mutant allele) **abolishes** the benefit — a genetic/pharmacological dissection establishing dependence.
3. Expand beyond n=1 to a **controlled cohort** (e.g., aggregated n-of-1 series with blinded assessment, or a small variant-stratified basket trial), correlating allele-specific knockdown with outcomes.

---

## 6. Evidence Refuting "Dominant-Negative Inhibition of Wild-Type KIF1A"

This section is given the same prominence as the supporting evidence, per the research objective.

**(a) The drug does the opposite of inhibiting WT KIF1A.** By design it degrades the *mutant* mRNA to preserve the WT allele:

> "specifically designed to degrade the mRNA from the pathogenic allele" — Ziegler et al., 2024 ([PMID: 39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/))

> "One potential therapeutic strategy is allele-specific knockdown of pathogenic transcripts." — Zuccaro et al., 2026 ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/))

The purpose of **allele specificity** is precisely to *avoid* touching the WT allele.

**(b) Benefit tracks removal, not addition, of inhibitory motor.** Rescue occurs when the pathogenic transcript is knocked down, consistent with de-repression of normal KIF1A function rather than dominant-negative inhibition of it:

> "antisense oligonucleotide-mediated knockdown of the pathogenic transcript rescues the dendrite neurite outgrowth phenotype in neurons from a patient with the P305L variant" — Zuccaro et al., 2026 ([PMID: 41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/))

**(c) Inhibiting WT KIF1A would be neurotoxic, not therapeutic.** WT KIF1A is essential for neuronal viability and function:

> "KIF1A mediates the transport of synaptic vesicle precursors and is essential for the function and viability of neurons" — Koshizuka et al., 2005 ([PMID: 15722511](https://pubmed.ncbi.nlm.nih.gov/15722511/))

> "This transport system is essential for neuronal function and survival." — Okamoto et al., 2014 ([PMID: 25253658](https://pubmed.ncbi.nlm.nih.gov/25253658/))

A therapy acting by inhibiting WT KIF1A would be expected to *cause* neurodegeneration, contradicting the observed clinical improvement.

**(d) The asserted phrase describes disease, not drug, and the disease mechanism is not uniformly "dominant-negative."** Pathogenic variants show mixed effects, including relieved autoinhibition alongside reduced motility ([PMID: 33496723](https://pubmed.ncbi.nlm.nih.gov/33496723/)), so even as a disease descriptor the phrase is an oversimplification — and it is simply not the drug's mode of action.

---

## Mechanistic Model / Interpretation

The clearest way to see the error is to lay the disease and drug mechanisms side by side.

```
DISEASE (KAND):
   Mutant KIF1A allele ──► mutant motor protein
                              │
                              ▼
        Dominant-negative / dominant interference with transport
        (impaired SV-precursor trafficking; neuronal dysfunction)
        [This is the "Dominant-Negative Inhibition of WT KIF1A"
         phrase — a PATHOPHYSIOLOGY statement]

DRUG (nL-KIF1-001, allele-specific ASO):
   ASO ──► selectively binds + degrades MUTANT mRNA
                              │
                              ▼
        Mutant protein level falls ──► WT KIF1A is RELIEVED
        ──► transport restored (shown in vitro: P305L neuron
            neurite-outgrowth rescue)
        [This is the DRUG mechanism — the OPPOSITE direction]
```

The knowledge-base entry has taken the pathophysiology label and attached it to the drug. The drug's mechanism is **allele-specific transcript knockdown**, whose downstream *consequence* is relief of (not infliction of) dominant-negative inhibition. The evidentiary chain is complete only through the in-vitro step; the final link from molecular mechanism to clinical benefit in the patient is unproven.

### Supported vs. refuted hypotheses

| Hypothesis | Verdict |
|---|---|
| Drug acts by allele-specific knockdown of the pathogenic KIF1A transcript | **Supported** (design + in-vitro rescue; in-patient causation untested) |
| Drug acts by "Dominant-Negative Inhibition of Wild-Type KIF1A" | **Refuted / mis-stated** (describes disease, not drug; drug is designed to spare WT) |
| Knockdown mediates the clinical benefit in patients | **Unknown** (no in-patient biomarker; n=1 uncontrolled) |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [39122967](https://pubmed.ncbi.nlm.nih.gov/39122967/) | *ASO therapy in an individual with KIF1A-associated neurological disorder* | Primary clinical case (n=1, p.Pro305Leu); defines drug as mutant-mRNA degrader; labels efficacy preliminary |
| [41513671](https://pubmed.ncbi.nlm.nih.gov/41513671/) | *ASOs to KIF1A polymorphisms… rescue patient-derived neurons in vitro* | In-vitro target engagement; P305L neurite-outgrowth rescue; frames strategy as allele-specific knockdown |
| [33496723](https://pubmed.ncbi.nlm.nih.gov/33496723/) | *Pathogenic KIF1A mutations diminish force… via allosteric mechanisms* | Shows disease biology is mixed (reduced motility + relieved autoinhibition), not uniform dominant-negative |
| [15722511](https://pubmed.ncbi.nlm.nih.gov/15722511/) | *HSV-2 UL56 associates with KIF1A* | Establishes WT KIF1A essential for neuronal viability |
| [25253658](https://pubmed.ncbi.nlm.nih.gov/25253658/) | *KIF1A mutation in progressive neurodegeneration* | Independently confirms KIF1A transport essential for neuronal survival |
| [34487232](https://pubmed.ncbi.nlm.nih.gov/34487232/) | *Monoallelic KIF1A-related disorders: multicenter study* | Disease epidemiology/heterogeneity; de novo motor-domain variants |

Supporting context papers on KIF1A/UNC-104 regulation and transport ([PMID: 23770702](https://pubmed.ncbi.nlm.nih.gov/23770702/), [PMID: 38477340](https://pubmed.ncbi.nlm.nih.gov/38477340/), [PMID: 21195138](https://pubmed.ncbi.nlm.nih.gov/21195138/), [PMID: 20510931](https://pubmed.ncbi.nlm.nih.gov/20510931/), [PMID: 19880746](https://pubmed.ncbi.nlm.nih.gov/19880746/), [PMID: 41648190](https://pubmed.ncbi.nlm.nih.gov/41648190/)) reinforce that KIF1A is the principal synaptic-vesicle-precursor motor whose function must be preserved.

---

## Limitations and Knowledge Gaps

1. **n=1 clinical evidence.** The sole clinical datum is an uncontrolled, open-label single case; placebo effect, natural history, and concurrent care cannot be excluded.
2. **No in-patient target engagement.** Mutant-transcript knockdown has not been measured in the treated patient; the molecular mechanism is inferred from cell culture.
3. **No in-vivo causal dissection.** No animal-model experiment demonstrates that the benefit *depends on* allele-specific knockdown (no control-ASO or resistant-allele counterfactual).
4. **Variant specificity.** In-vitro rescue was shown for P305L; generalization to other KAND variants is unproven, and disease biology differs by variant.
5. **Drug-identity inference.** The "nL-KIF1-001" designation is matched to the published p.Pro305Leu n-Lorem allele-specific ASO case; the exact trade name is not independently confirmed in indexed abstracts.
6. **Abstract-level evidence.** Claims rest on abstracts; full-text target-engagement data were not reviewed. The literature on this bespoke ultrarare agent is only two primary papers.

---

## Proposed Follow-up Experiments / Actions

1. **Correct the knowledge base entry.** Replace "Dominant-Negative Inhibition of Wild-Type KIF1A" (a disease-mechanism label misattributed to the drug) with **"Allele-specific knockdown of the mutant KIF1A transcript (relieving the dominant-negative disease mechanism)"**, flagged as a *leading candidate / open knowledge gap*, not established.
2. **In-patient biomarker.** Develop a CSF/accessible-tissue assay for allele-specific KIF1A transcript levels and correlate knockdown with clinical outcomes across repeated dosing.
3. **Animal-model dependence test.** In a knock-in/humanized KAND model, test ASO rescue vs. a non-targeting control ASO and an ASO-resistant mutant allele to establish causal dependence of benefit on knockdown.
4. **Variant breadth.** Repeat the in-vitro rescue across additional pathogenic variants to test generality of allele-specific knockdown.
5. **Controlled clinical design.** Move beyond n=1 to blinded aggregated n-of-1 series or a variant-stratified basket trial with pre-specified target-engagement endpoints.

---

### Consensus answer

No — the therapeutic mechanism of nL-KIF1-001 in KAND is **not established**, and the knowledge base's "Dominant-Negative Inhibition of Wild-Type KIF1A" is a **mis-attribution** of the disease mechanism to the drug. The drug's actual (and only partially, in-vitro-supported) mechanism is the opposite: **allele-specific knockdown that degrades the mutant KIF1A transcript, relieving dominant-negative inhibition of wild-type KIF1A** — a leading candidate whose link to clinical benefit remains an open knowledge gap.


## Artifacts

- [OpenScientist final report](KIF1A_Related_Neurological_Disorder-drug-mechanism-allele_specific_antisense_oligonucleotid-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KIF1A_Related_Neurological_Disorder-drug-mechanism-allele_specific_antisense_oligonucleotid-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.