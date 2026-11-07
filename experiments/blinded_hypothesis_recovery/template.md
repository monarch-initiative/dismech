# Mechanistic Hypothesis Discovery

## Target Disease
- **Disease Name:** {disease_name}
- **MONDO ID:** {mondo_id}

## What Is Already Curated

The knowledge base already records the following mechanism nodes for this disease:

{existing_mechanism}

and the following genetic risk factors:

{existing_genetics}

Do not restate or re-justify these. They are the starting point, not the answer.

## Research Objective

Identify the **mechanistic hypotheses this disease account is missing**: specific genes or
gene products whose dysfunction plausibly drives part of the disease, and the causal chain
by which it does so.

{focus}

For each hypothesis, rank-ordered from strongest to weakest, report:

1. The gene (HGNC symbol) and the gene product's molecular function.
2. The human genetic evidence: germline risk variants (with effect sizes as reported) and
   any somatic lesions in disease tissue. State the cohort.
3. The causal chain, step by step, from the molecular defect to tissue pathology to the
   clinical feature it explains. Name the cell type at each step.
4. Model-system evidence: which animal or in vitro model, what was perturbed, and which
   disease features it did and did not reproduce.
5. The therapeutic direction this implies (increase or decrease the gene product's activity,
   or act downstream), and why.
6. For every factual claim, a PMID and an exact quote from that paper's abstract.

Separate established findings from your own inference, and say which is which.
Return at least five hypotheses. Do not include any hypothesis whose central gene is already
listed in the curated genetics above.
