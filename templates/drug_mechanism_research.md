# Drug Therapeutic Mechanism Research Template

## Target Question

- **Disease:** {disease_name}
- **Drug:** {drug}
- **Mechanism asserted in the knowledge base:** {asserted_mechanism}

## Research Objectives

A disease knowledge base links **{drug}** to the mechanism **"{asserted_mechanism}"**
as the way it acts in **{disease_name}**. The drug's clinical effect may be well
established while its mechanism is not. Please determine **whether the mechanism by
which {drug} produces its therapeutic effect in {disease_name} has been established,
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

- State briefly what clinical benefit {drug} has in {disease_name}, and the strongest
  evidence for it (randomized trial, meta-analysis, observational, case series).
- Keep this short. It is context, not the question.

### 2. Candidate mechanisms

- List each molecular or cellular mechanism that has been proposed for {drug}'s
  benefit **in this disease**, including "{asserted_mechanism}".
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

### 6. Evidence refuting "{asserted_mechanism}"

- Report findings that argue against the asserted mechanism mediating the benefit in
  {disease_name}, with PMIDs and quotes. Give these the same prominence as
  supporting findings.
