# PRPH2-related retinopathy curation notes

## Bottom Line

`PRPH2-related retinopathy` is a justified umbrella entity for dismech. The shared trunk is the PRPH2/ROM1 outer-segment rim/disc structural module, while the named child conditions are mostly different phenotypic expressions of that same mechanism rather than unrelated diseases.

## Why an umbrella is defensible

- PRPH2 disease spans a broad but coherent phenotype space: pattern dystrophy / vitelliform macular dystrophy, pseudo-Stargardt pattern dystrophy, central areolar choroidal dystrophy, retinitis pigmentosa, and in some reports Leber congenital amaurosis. The 2024 multicenter cohort describes “six distinct FAF phenotypes” and emphasizes marked variability across PRPH2 disease.
- The mechanistic core is shared. PRPH2 is a photoreceptor-specific tetraspanin required for outer-segment formation and maintenance, and it forms complexes with ROM1.
- The children are therefore better treated as late phenotype branches under one mechanistic parent than as separate top-level pathographs, unless a child is clearly driven by a different primary mechanism.

## Strong subtype candidates

The best MONDO child terms to keep as explicit subtypes under the umbrella are the clinically meaningful branches that reflect distinct phenotype classes:

- `retinitis pigmentosa 7`
- `vitelliform macular dystrophy 3`
- `patterned macular dystrophy 1`
- `central areolar choroidal dystrophy 2`
- `Leber congenital amaurosis 18`
- `retinitis pigmentosa 7, digenic`

These are not just severity labels. They are different retinal patterning outcomes of the same PRPH2-centered biology, with different topography and age-of-onset distributions.

## Digenic branch

`retinitis pigmentosa 7, digenic` does add a distinct genetic mechanism, but not a separate disease biology unrelated to PRPH2. The literature supports digenic RP when ROM1 interacts with heterozygous PRPH2 variants, so the right modeling choice is to keep it under the PRPH2 umbrella and mark inheritance / genetic context explicitly as digenic rather than creating a new unrelated root.

Practical modeling note: this should be represented as a subtype or inheritance-context branch, not as a severity stage. The mechanistic distinction is “PRPH2 plus ROM1 modifier / second locus,” not “same disease but more or less severe.”

## Fundus albipunctatus / retinitis punctata albescens

These should be treated cautiously under PRPH2.

- The MONDO hierarchy currently places `fundus albipunctatus` and `retinitis punctata albescens` under PRPH2-related retinopathy, but the broader literature still treats them primarily as visual-cycle disorders.
- Fundus albipunctatus is primarily an RDH5 disorder, with RLBP1 and other visual-cycle genes as secondary causes.
- Retinitis punctata albescens is classically associated with RLBP1, though PRPH2 is also reported in the broader PRPH2 spectrum.

Recommendation: do not promote these as core PRPH2 subtypes. If they remain under the umbrella for ontology reasons, label them as cautious / low-confidence children or phenotype-overlap branches unless the source paper is explicitly PRPH2-driven.

## Working rule for dismech

- Use one PRPH2 umbrella pathograph.
- Keep phenotype branches as subtypes where they reflect distinct clinical patterns.
- Model digenic RP as a genetic-context subtype.
- Exclude or de-emphasize visual-cycle phenotypes unless the supporting paper is specifically PRPH2-driven.

## References

- PMID:38278208, PRPH2-associated IRDs span macular dystrophies, cone/cone-rod dystrophies, rod-cone dystrophies, and LCA; the review explicitly highlights IRD heterogeneity.
- PMID:38743414, 241-patient PRPH2 cohort with broad phenotype variability and multiple FAF patterns.
- PMID:29961824, PRPH2 mutations span rod-dominant RP to cone-dominant macular dystrophy and require Prph2/Rom1 oligomerization for outer-segment formation.
- PMID:8202715, classic digenic retinitis pigmentosa due to PRPH2/RDS and ROM1.
- PMID:32716032, ROM1 modifies PRPH2-associated retinal disease and affects PRPH2/ROM1 complex formation.
- PMID:20829743, fundus albipunctatus is primarily an RDH5-associated visual-cycle disorder.
- PMID:30726412, PRPH2 variants are reported across a broad retinal-dystrophy spectrum that includes retinitis punctata albescens.
- PMID:23929416, retinitis punctata albescens is most often caused by RLBP1.
- PMID:11262646, RLBP1 is involved in retinitis punctata albescens families.
