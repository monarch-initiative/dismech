# MMACHC-related methylmalonic aciduria and homocystinuria, cblC type

## Framing

This disease should be curated as a distinct `MMACHC`-anchored intracellular cobalamin-processing disorder rather than folded into isolated methylmalonic acidemia or generic homocystinuria.

- The key split is mechanistic, not cosmetic: MMACHC loss simultaneously limits methylcobalamin supply to methionine synthase and adenosylcobalamin supply to methylmalonyl-CoA mutase.
- That produces the defining combined biochemical pattern: hyperhomocysteinemia, hypomethioninemia, and methylmalonic acid accumulation.
- Early-onset and late-onset presentations belong under the same disease umbrella, but the curation should recognize them as clinically distinct strata rather than separate diseases.

Primary anchors:

- PMID:39225018: primary human cohort explicitly states that cblC is caused by biallelic `MMACHC` variants and that impaired conversion of vitamin B12 into methylcobalamin and adenosylcobalamin leads to the characteristic biochemical pattern.
- PMID:40441036: primary molecular study showing that a recurrent MMACHC missense variant destabilizes the protein and impairs cobalamin handling.
- PMID:32186706: viable zebrafish cblC model supporting the dual-enzyme downstream consequence of failed cobalamin processing.

## Disease Architecture

### Proximal defect

MMACHC is the proximal lesion. The curation should start with a node for intracellular cobalamin processing deficiency, not with methylmalonic acid accumulation or homocysteine elevation. That keeps the graph causal and disease-specific.

Useful exact quote:

- PMID:39225018: “Cobalamin C is the most common inborn error of intracellular cobalamin metabolism caused by biallelic pathogenic variants in the MMACHC gene, leading to impaired conversion of dietary vitamin B12 into its two metabolically active forms, methylcobalamin and adenosylcobalamin.”

### Remethylation branch

The methionine synthase side should be separated from the MUT side. The best compact disease-level representation is:

1. `MMACHC intracellular cobalamin processing deficiency`
2. `Reduced methylcobalamin supply`
3. `Impaired methionine synthase-dependent remethylation`
4. `Hyperhomocysteinemia and hypomethioninemia`

Useful exact quotes:

- PMID:40544542: “co-immunoprecipitation provided evidence for impaired interaction between the variant MMACHC and methionine synthase (MTR).”
- PMID:39225018: “Biochemical hallmarks are elevated plasma total homocysteine (HCYs) and low methionine accompanied by methylmalonic aciduria.”

### MUT branch

The methylmalonic acid side should be represented as a parallel branch:

1. `Reduced adenosylcobalamin supply`
2. `Impaired methylmalonyl-CoA mutase-dependent metabolism`
3. `Methylmalonic acid accumulation`

Useful exact quote:

- PMID:32186706: “This recessive disorder is characterized by a failure to metabolize cobalamin into adenosyl- and methylcobalamin, which results in the biochemical perturbations of methylmalonic acidemia, hyperhomocysteinemia and hypomethioninemia caused by the impaired activity of the downstream enzymes, methylmalonyl-CoA mutase and methionine synthase.”

## Clinical Stratification

### Early onset

Early-onset disease remains the dominant severe form, even in screened cohorts. The curation should avoid implying that newborn screening abolishes morbidity.

Useful exact quotes:

- PMID:39152755: “We assessed OH-Cbl therapy impact on biochemical, neurocognitive and visual outcomes in early-onset Cbl-C patients treated with different OH-Cbl doses over 3 years.”
- PMID:41728752: “Despite early intervention, a substantial proportion of individuals exhibited developmental impairments or ocular manifestations, and neonatal onset appears to be associated with disease severity.”

### Late onset

Late-onset cblC belongs inside the same disease entry, not in a separate disease file, but deserves explicit mention in subtype framing and notes because diagnostic delay is a recurrent theme.

Useful exact quotes:

- PMID:37770946: “Patients with late-onset form (>1 year) are often misdiagnosed due to heterogeneous symptoms.”
- PMID:41341912: “Common symptoms included spastic paralysis (41.0%), mental and behavioral abnormalities (36.5%), and renal damage (28.8%).”

## Phenotypes Best Supported by Primary Studies

### Neurodevelopmental / neurologic

- Intellectual disability: PMID:39152755 directly names it.
- Seizure and hypotonia: PMID:39225018 gives cohort counts.
- Cognitive decline / neuropsychiatric disease: late-onset cohorts PMID:37770946 and PMID:41341912 support this, though ontology mapping is easier if the YAML stays with broader supported neurologic terms unless a precise term lookup is validated.

Key quote:

- PMID:39225018: “The most common clinical features were cognitive impairment (n = 29), seizures (n = 23), motor developmental delay (n = 20), hypotonia (n = 17), and sparse/hypopigmented scalp hair (n = 16).”

### Ocular

Ocular disease is central, not incidental. The curation should not reduce it to a vague visual phenotype in notes only.

Key quotes:

- PMID:40565527: “In cblC, retinal degeneration occurs in the first months of life despite timely treatment and adequate biochemical control, and it may manifest before any signs of visual deprivation appear.”
- PMID:18454408: “Despite early treatment and regular metabolic controls, all our patients exhibited both retinal and ERG abnormalities.”

Interpretation:

- In YAML, `Visual impairment` is a safe ontology-grounded phenotype term.
- The description should preserve the clinically important specificity: infantile maculopathy / retinal degeneration.

### Renal / vascular

Renal thrombotic microangiopathy is sufficiently distinctive and well-supported to justify explicit curation, and kidney biopsy findings can be represented in `histopathology`.

Key quotes:

- PMID:39390411: “They were diagnosed with renal involvement due to cblC deficiency after laboratory tests revealing elevated serum and urine homocysteine, renal biopsy showing TMA and tubular injury, along with genetic testing showing heterogeneous compound mutations in MMACHC.”
- PMID:39390411: “Here we described three teenage patients who presented with hematuria, proteinuria, and hypertension in clinical presentation.”

### Pulmonary / cardiovascular

Pulmonary hypertension is an important complication and should be explicitly included as a phenotype if only one cardiovascular manifestation is chosen.

Key quotes:

- PMID:40468431: “Pulmonary Hypertension (PH) in patients with cblC deficiency is one of the rare but lethal complications.”
- PMID:40830795: “Cardiovascular complications were found between the ages of 2 months and 12 years, with 9 patients having pulmonary hypertension, 7 having hypertension, and 5 having non-compaction of ventricular myocardium.”

## Treatments

### Hydroxocobalamin

Hydroxocobalamin should be the lead treatment entry. The newer evidence argues for dose intensity mattering, especially in early-onset disease.

Key quotes:

- PMID:39152755: “This study showed that "high-dose" OH-Cbl treatment in NBS-diagnosed children with severe early-onset Cbl-C defect led to a significant improvement in the metabolic profile and in neurocognitive outcome, compared to age-matched patients treated with a "low-dose" regimen.”
- PMID:32071835: “A regimen of high-dose hydroxocobalamin (25 mg/day) together with betaine and folic acid resulted in rapid and sustainable biochemical correction, resolution of psychosis, improvement of neurological functions, and amelioration of brain and spinal cord lesions.”

### Betaine

Betaine is best represented as an adjunctive pharmacotherapy rather than the lead therapy.

Useful supporting quote:

- PMID:32071835: same combination-therapy sentence above.

### Newborn screening

Screening materially changes outcome and is worth including as `disease screening` or under diagnosis.

Key quote:

- PMID:40981307: “This approach allows for early diagnosis and immediate treatment with hydroxocobalamin in patients with mild CblC deficiency, resulting in early intervention, effective metabolic control, and, based on current follow-up, normal neurodevelopmental outcomes.”

### What I did not elevate

- Protein-restricted or medical-food-heavy dietary therapy was not promoted as a lead disease-level treatment because the strongest cblC-specific abstracts I found were more robust for hydroxocobalamin-centered regimens and newborn screening than for diet-first management.
- Folinic acid and carnitine are common adjuncts, but the most direct abstract-level support in this literature set is combination-regimen support rather than clean single-agent evidence.

## Variant-level Heterogeneity

The disease is genetically heterogeneous, but one or two variants are enough for the disease file.

Best-supported variant to include:

- PMID:38070096: `MMACHC c.482G>A (p.Arg161Gln)` is associated with later onset and milder phenotypes in a large cohort.
- PMID:40441036: the matching protein-level `R161Q` study shows reduced AdoCbl binding and impaired dimerization.

Potentially useful severe/mild contrast:

- PMID:38387306 contrasts milder `c.[158T>C];[271dupA]` compound heterozygotes with more severe `c.271dupA` homozygotes, and emphasizes strong hydroxocobalamin responsiveness in the milder genotype.

## Curation Choices to Preserve

- Keep the disease split away from isolated MMA.
- Keep the disease split away from generic homocystinuria.
- Use exact PMID-backed snippets only.
- Prefer human cohort evidence for phenotypes and treatments.
- Use model-organism evidence only where it adds mechanistic clarity, not to stand in for human phenotype prevalence.
- Keep the pathophysiology nodes atomic and branch-structured rather than collapsing everything into “combined methylmalonic acidemia and homocystinuria.”
