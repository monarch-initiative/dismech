# Three lowest-confidence mapping investigations

We selected **ADan amyloidosis, CANVAS, and methylcobalamin deficiency type
cblE** from the 32 completed results with confidence 0.5. These cover ICD-11
Foundation, Orphanet, and Disease Ontology conflicts. Selection was illustrative,
not random. Investigation date: 2026-09-11.

Compare the **top five distinct complete assignments**, including input priors
and marginal posteriors in separate columns:

- [CANVAS alternatives](CANVAS-alternatives.md)
- [ADan alternatives](ADan_amyloidosis-alternatives.md)
- [cblE alternatives](Methylcobalamin_Deficiency_Type_cblE-alternatives.md)

These views are generated alongside `experiments.json` by the reproduction
command below. They show ties explicitly instead of only displaying one optimum.

**All three ties are caused by two equal-prior equivalence mappings plus an
assumed prohibition on equating distinct IDs within the target vocabulary.**
Biological evidence distinguishes the cases: CANVAS follows a documented,
evidence-supported merge; cblE exposes a likely DO duplicate with an incorrect
biochemical classification; ADan is a candidate terminology duplicate.

## What the solver actually knows

The competing mappings are:

| Disease | MONDO | Target A, rejected in saved solution | Target B, accepted in saved solution |
|---|---|---|---|
| ADan amyloidosis | MONDO:0007297 | icd11f:2086401830 — Familial dementia, Danish type | icd11f:54507082 — ADan amyloidosis |
| CANVAS | MONDO:0044720 | ORDO:139564 — Hereditary sensory and autonomic neuropathy type 1B | ORDO:504476 — Cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome |
| cblE | MONDO:0009354 | DOID:0050732 — methylmalonic aciduria and homocystinuria type cblE | DOID:0112255 — homocystinuria-megaloblastic anemia cblE type |

Each mapping has prior **0.95**. The saved assignment accepts B and rejects A;
the equally probable alternative accepts A and rejects B. The probability
contribution of either choice is `0.95 × 0.05`. Accepting neither contributes
`0.05 × 0.05`, so each mapping's marginal probability of being true is
`0.0475 / (0.0475 + 0.0475 + 0.0025) = 0.487179`.

The minimal conflict contains exactly four assertions: `MONDO ≡ A`,
`MONDO ≡ B`, and membership of A and B in the same `MemberOfDisjointGroup`.
Despite its name, this Boomer construct means **non-equivalence of different
members**, not OWL class disjointness. The generator supplies it for each
namespace. None of these three saved KBs contains an explicit source
`DisjointWith` or hierarchy edge between A and B. Definitions, inheritance,
gene associations, and merge evidence are not inputs to these solves.

[Exhaustive enumeration](experiments.json) reproduces every saved marginal,
the whole-assignment posterior, and the distinct-solution count. Removing any
one assertion from the four-assertion core makes that core satisfiable.
Relaxing only the first target's namespace membership yields:

| Disease | Original confidence | Relaxed confidence | Original whole-assignment posterior | Relaxed posterior |
|---|---:|---:|---:|---:|
| ADan amyloidosis | 0.5 | 0.9 | 0.353377 | 0.654631 |
| CANVAS | 0.5 | 0.9 | 0.319719 | 0.592280 |
| cblE | 0.5 | 0.9 | 0.318039 | 0.589168 |

Each relaxed optimum accepts all high-prior hypotheses, including both competing
mappings. Removing mapping A entirely also eliminates each tie (confidence 0.9).
These are diagnostic counterfactuals, **not proposed automatic repairs**. Raising
confidence by removing a constraint is no evidence that doing so is correct.

## CANVAS: an intentional merge supported by newer genetics

The label mismatch initially looks compelling: the Orphanet snapshot classifies
HSAN1B under autosomal dominant neuropathy, whereas CANVAS is recessive. That
contrast is insufficient to reject the mapping.

Grosz and colleagues reexamined the original HSN32 and HSN35 families in 2025.
They found biallelic RFC1 expansions, including a complex repeat requiring
long-read characterization. The apparent dominant transmission was
pseudodominance; the authors concluded that the previously assigned HSN1B
chromosome 3 locus should no longer be considered valid.
[Primary study, PMID:41084404](https://pubmed.ncbi.nlm.nih.gov/41084404/).

[MONDO issue 9795](https://github.com/monarch-initiative/mondo/issues/9795)
explicitly records OMIM:608088 moving to OMIM:614575 and requests the matching
MONDO:0011961 → MONDO:0044720 merge, with Orphanet coordination. The April 2026
maintainer response says the merge follows OMIM's same-concept determination.
The May 2026 MONDO snapshot consequently carries both Orphanet exact matches;
the January 2026 Orphanet snapshot retains two concepts and still maps HSAN1B
to the retired MONDO ID. The indexed current
[Orphanet HSAN1B page](https://www.orpha.net/en/disease/detail/139564)
also retains the dominant classification and OMIM:608088.

**Assessment:** a supported merge with lagging source reconciliation, not a
reason to undo the CANVAS grounding. Coordinate the Orphanet record with the
existing MONDO issue and the primary paper. Clinical CANVAS versus the broader
RFC1 spectrum still warrants explicit granularity review; the paper does not
make every unexplained sensory neuropathy equivalent to full CANVAS.

Both ORDO→ICD-10 broad mappings remain accepted in both optima. Choosing one
MONDO equivalence does not remove the other ORDO concept or its ICD-10 mapping
from the KB. These solutions do not select a unique ICD-10 code for the disease.

## cblE: a likely DO duplicate with a biochemical classification error

Both DO entries identify **MTRR** disease. DOID:0050732 defines it as a
methylmalonic acidemia and is a subclass of DOID:14749; DOID:0112255 uses the
homocystinuria/megaloblastic-anemia concept and cross-references OMIM:236270
and ORDO:2169. Both remain active in the checked
[DO source revision](https://github.com/DiseaseOntology/HumanDiseaseOntology/blob/ec05d8346757d228193d33e6ef7a565f430ebe39/src/ontology/doid.obo),
so this is not merely an obsolete target missed by our filter.

cblE affects methionine synthase reactivation through MTRR. It belongs to the
isolated remethylation disorders, whose defining biochemical pattern is
homocystinuria without methylmalonic aciduria. The original molecular study
identifies the MTRR defect; Orphanet places cblE under the corresponding
without-methylmalonic-aciduria disorder.
[Wilson et al., PMID:10484769](https://pubmed.ncbi.nlm.nih.gov/10484769/),
[Orphanet cblE](https://www.orpha.net/en/disease/detail/2169),
[Orphanet parent](https://www.orpha.net/en/disease/detail/622).

**Assessment:** DOID:0112255 is the better-supported representation. Request
DO review of merging/obsoleting DOID:0050732 into it and correcting the
methylmalonic-acidemia classification. Follow through on MONDO's mapping after
the source decision. The evidence supports this recommendation; Boomer's tied
score itself does not prefer it. The existing dismech MONDO grounding is not
implicated by this conflict.

## ADan: likely duplicate terminology, unresolved WHO record intent

The ICD-11 Foundation snapshot has two active-looking IDs under different
parents: `2086401830` under `1502610635`, and `54507082` under `503091580`.
The former's definition describes the ITM2B duplication; the latter has no
definition in the extract. Neither has a deprecation assertion there.
Orphanet explicitly lists *Familial dementia, Danish type* as a synonym of
*ADan amyloidosis*, sharing OMIM:117300.
[Orphanet ADan record](https://www.orpha.net/en/disease/detail/97346).

**Assessment:** candidate duplicate representations of the same disease.
Different parentage alone does not prove distinct disease scope. Review both
WHO Foundation records for intended scope and duplicate/merge handling before
retracting either MONDO identity assertion. The public WHO browser returned
only its application shell during this investigation, so current WHO record
content and any pending merge proposals were not verified. The detailed term
comparison is limited to the January 2026 source snapshot.

## Implication for our workflow

Keep the probability correction. It correctly exposes a tie between different
assignments. The next improvement is to make the **reason for a conflict**
visible: inferred namespace non-equivalence versus an explicit ontology axiom,
plus source versions and merge provenance. Review known source duplicates or
supported merges before treating a rejected mapping as a curation error.

Do not blanket-remove namespace constraints: they are what detects real proxy
merge problems. Any exception should identify the particular pair and its
evidence. No generator policy, production input, saved solution, or disease KB
entry was changed in this investigation. No upstream issue was posted.

## Reproduce and inspect

```bash
PYTHONPATH=src uv run --with networkx python analyses/boomer/scripts/investigate_ties.py \
  --boomer-src /path/to/clean/boomer-py/src \
  --out analyses/boomer/low-confidence/experiments.json
```

Use Boomer `744038e30741009930f57919ca2f03c6473ed198`, as recorded in the
output. The script enumerates all Boolean assignments once, verifies the
baseline against saved results, tests minimality of each conflict, and performs
the two in-memory interventions. It asserts input bytes are unchanged.

[local-source-terms.json](local-source-terms.json) contains read-only extracts
from the existing OAK semantic-sql snapshots: MONDO 2026-05-05, DO 2026-02-02,
and MONDO's Orphanet/ICD-11 Foundation source products dated 2026-01-09.
The latter dates identify the source products, not independently verified WHO
release dates. [current-doid.json](current-doid.json) preserves the two DO
stanzas and their pinned retrieval URL.
[mondo-9795.json](mondo-9795.json) preserves the retrieved merge discussion.
