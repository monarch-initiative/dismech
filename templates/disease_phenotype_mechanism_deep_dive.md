# Phenotype Mechanism Deep-Dive Research Template

## Target Disease
- **Disease Name:** {disease_name}
- **MONDO ID:** {mondo_id} (if available)

## Scope

This is a narrow, per-phenotype deep dive — not a disease survey. The disease's
core pathophysiology is already curated and is not in question here. The
subject is a small set of clinical manifestations whose **mechanistic link to
the disease is unsettled, contested, or obscure**, and which a broad
mechanism survey would gloss over:

{phenotype_focus}

## Research Objective

For **each** phenotype listed above, report:

1. **Every mechanistic hypothesis in the literature** for how the disease
   produces this phenotype — including minority and historical hypotheses.
   For each hypothesis: the proposed causal chain, step by step, and who has
   proposed or tested it.
2. **The human evidence for and against each hypothesis**: PMIDs with exact
   quotes from the abstracts. Interventional evidence (improvement or
   resolution on disease-specific treatment, e.g. dietary withdrawal) counts
   for causation; note where it is absent.
3. **Non-causal explanations**, treated as first-class competitors: shared
   genetic susceptibility (e.g. HLA haplotypes), coincident autoimmune
   disease, nutritional confounding, medication effects, surveillance or
   ascertainment bias. Say which of these the literature has actually tested
   and what was found.
4. **A verdict per phenotype**, one of:
   - SETTLED — one mechanism is established in humans and generally accepted
   - CONTESTED — two or more live hypotheses with meaningful support each
   - UNKNOWN — association documented, mechanism not established
   Plus: which single study design or observation would most efficiently
   resolve a CONTESTED or UNKNOWN verdict.
5. **Timing and reversibility facts** that constrain mechanism: does the
   phenotype precede diagnosis, does it remit with treatment, is it
   irreversible once formed (for example, defects fixed during tissue
   development), does it track disease activity or persist independently?

**Honesty requirement:** UNKNOWN is a correct and valuable answer. Do not
promote a plausible hypothesis to SETTLED to make the report tidier. Where the
best available evidence is old, small, or indirect, say so.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as
  listed above, containing: the competing hypotheses each with its causal
  chain and evidence, the non-causal alternatives and their status, the
  verdict, the resolving experiment, and the timing/reversibility facts.
- Suggested ontology terms where applicable: HP for the phenotype, GO for
  biological processes, CL for cell types.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make
