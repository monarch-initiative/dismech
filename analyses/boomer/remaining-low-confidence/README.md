# Remaining low-confidence results: mapping granularity first

**Gorlin syndrome, proteasome-associated autoinflammatory syndrome (PRAAS), and
TPMT deficiency are the clearest next curation targets.** In each, the competing
DO identifiers deliberately distinguish a disease family from a gene-specific
subtype. The source definitions, sibling classes, and matching MONDO terms give
us a reason to correct the mapping, beyond simply raising Boomer's score.

After the proxy-merge migration, **1,208 completed results** have the corrected
solver revision and matching current input hashes. Eleven have confidence 0.5,
two have 0.7, 1,123 have 0.9, and 72 have 0.95. The 326 timeouts and 194 results
from older solver versions are excluded. No production input or solution was
changed by this investigation.

## Three concrete mapping corrections to review

These are proposed source corrections, not changes applied by this report.
The equivalence pairs remain explicitly annotated in the pinned MONDO source;
none has the preferred DO target required by our automatic proxy policy.

### Gorlin syndrome: an umbrella mapped to its PTCH1 subtype

`MONDO:0007187` is nevoid basal cell carcinoma syndrome. It currently claims
identity with both `DOID:2512` (the family) and `DOID:0070365` (type 1, PTCH1).
DO places the latter under the former and also has `DOID:0070366`, the SUFU
subtype. MONDO independently has the same separation: `MONDO:0958174` (type 1,
PTCH1) and `MONDO:0958189` (type 2, SUFU) are children of `MONDO:0007187`.
The current type-1 MONDO term has the matching OMIM:109400 but lacks the DO
mapping that is sitting on the umbrella.
[MONDO parent and children](current-source-context.json),
[DO source](https://github.com/DiseaseOntology/HumanDiseaseOntology/blob/ec05d8346757d228193d33e6ef7a565f430ebe39/src/ontology/doid.obo#L29346).

The distinction has biological support: SUFU-associated Gorlin syndrome was
reported in a PTCH1-negative family.
[Pastorino et al., PMID:19533801](https://pubmed.ncbi.nlm.nih.gov/19533801/).

**Proposed correction:** retain `MONDO:0007187 ≡ DOID:2512`; move the
`DOID:0070365` equivalence to `MONDO:0958174`. The relationship of that DO
subtype to the MONDO umbrella is narrower-than, not identity. Preserve the
family/subtype distinction.

The saved optimum currently accepts the PTCH1-specific equivalence and rejects
the umbrella equivalence. The equally probable second solution does the reverse.
Both whole-assignment posteriors are **0.337481211545**; neither is preferred by
the model. The source context supplies the reason to favor the umbrella mapping.
[All hypotheses and top five solutions](Gorlin_Syndrome-alternatives.md).

### PRAAS: a family mapped to PRAAS1

`MONDO:0009726` maps to both `DOID:0060913` (PRAAS family) and `DOID:0050553`
(PRAAS1, including PSMB8-associated and specified digenic forms). DO makes PRAAS1
a child of the family and includes other subtypes, such as POMP-associated
PRAAS2. MONDO already has `MONDO:0054698` for PRAAS1 as a child of
`MONDO:0009726`, with the matching OMIM:256040. It lacks the DOID:0050553 mapping
currently attached to its parent.
[MONDO/DO stanzas](current-source-context.json),
[DO family](https://github.com/DiseaseOntology/HumanDiseaseOntology/blob/ec05d8346757d228193d33e6ef7a565f430ebe39/src/ontology/doid.obo#L21946).

Primary research established PRAAS involving additional proteasome genes,
including PSMB4 and POMP, with recessive, digenic, and dominant architectures.
The dismech entry also explicitly covers this broader mechanism family.
[Brehm et al., PMID:26524591](https://pubmed.ncbi.nlm.nih.gov/26524591/),
[dismech PRAAS entry](../../../kb/disorders/Proteasome_Associated_Autoinflammatory_Syndrome.yaml).

**Proposed correction:** retain `MONDO:0009726 ≡ DOID:0060913`; move the
`DOID:0050553` equivalence to `MONDO:0054698`. Review the parent's historical
synonyms at the same time: some describe particular subtypes and could explain
how the old equivalence survived the introduction of explicit children.
[Top five solutions](Proteasome_Associated_Autoinflammatory_Syndrome-alternatives.md).

### TPMT deficiency: a specific mechanism mapped to a broader response family

`MONDO:0012503` explicitly describes disrupted TPMT activity and maps to both
`DOID:0061004` (TPMT-related poor metabolism of thiopurines 1) and `DOID:0080172`
(poor metabolism of thiopurines). The latter also contains `DOID:0060996`,
NUDT15-related poor metabolism of thiopurines 2. Thus the MONDO concept matches
the DO child, while the DO parent has a broader etiologic scope.
[MONDO/DO stanzas](current-source-context.json),
[DO NUDT15 subtype](https://github.com/DiseaseOntology/HumanDiseaseOntology/blob/ec05d8346757d228193d33e6ef7a565f430ebe39/src/ontology/doid.obo#L22686).

TPMT and NUDT15 are distinct contributors to thiopurine handling; the current
CPIC guideline treats both genotype systems explicitly.
[CPIC 2025 update](https://pmc.ncbi.nlm.nih.gov/articles/PMC12997511/).

**Proposed correction:** retain `MONDO:0012503 ≡ DOID:0061004`; replace identity
with the parent by a broader-target relationship:
`MONDO:0012503 ⊂ DOID:0080172`. Also review DO's exact TPMT-deficiency synonyms
on that broader parent; they conflict with its inclusion of the NUDT15 subtype.
[Top five solutions](Thiopurine_S-methyltransferase_Deficiency-alternatives.md).

## What the numerical ties mean

All eleven 0.5 cases have two distinct optimal complete assignments, each
rejecting a different member of an equal-prior equivalence pair. Each mapping
starts with prior 0.95. If all other contributions multiply to K:

- accept the first, reject the second: `K × 0.95 × 0.05`;
- reject the first, accept the second: `K × 0.05 × 0.95`.

The hypotheses really conflict under the saved model, and the assignments are
counted once. Independent enumeration reproduces every saved confidence,
whole-assignment posterior, satisfiable-assignment count, and mapping marginal
for all thirteen cases. The two competing mappings each have marginal posterior
0.487179487179 in every 0.5 case. This is not the old duplicate-search-path bug.

Five cases also have a strict subclass edge between the competing targets in
the saved input. Removing only namespace membership still leaves the tie:

| Case | Confidence | After namespace-only relaxation | After hypothetical full proxy relaxation |
|---|---:|---:|---:|
| Gorlin syndrome | 0.5 | 0.5 | 0.9 |
| PRAAS | 0.5 | 0.5 | 0.9 |
| TPMT deficiency | 0.5 | 0.5 | 0.95 |
| Berardinelli-Seip congenital lipodystrophy | 0.5 | 0.5 | 0.9 |
| FOXE3 anterior segment dysgenesis | 0.5 | 0.5 | 0.9 |

These strict edges were synthesized by our older generator from ordinary
source subclass edges plus the namespace non-equivalence assumption; they are
not explicit source OWL disjointness. The full hypothetical relaxation changes
them back to ordinary subclass and permits the pair to merge, without changing
priors. That raises confidence but supplies no biological justification for
merging. The family/subtype source evidence is why the first three warrant
mapping corrections instead.

## Other cases and next priorities

| Case | Score | Finding / next check |
|---|---:|---|
| [FOXE3 anterior segment dysgenesis](FOXE3_Anterior_Segment_Dysgenesis-alternatives.md) | 0.5 | ICD-11 child/parent pair. Separately, the FOXE3-specific dismech entry is grounded to a broad MONDO anterior-segment-dysgenesis family; review that scope as well. |
| [Wolman disease](Wolman_Disease-alternatives.md) | 0.5 | MeSH generic Wolman disease versus Wolman disease with hypolipoproteinemia/acanthocytosis. Check whether the supplementary concept is intentionally narrower. |
| [COL11A2 skeletal spectrum](COL11A2_Skeletal_Spectrum-alternatives.md) | 0.5 | DOID:4258's Weissenbacher-Zweymuller label coexists with Pierre Robin synonyms and MIM:261800. Review the source record's mixed scope before treating it as a straightforward duplicate of DOID:0080677. |
| [Berardinelli-Seip lipodystrophy](Berardinelli_Seip_Congenital_Lipodystrophy-alternatives.md) | 0.5 | ICD-11 places the named syndrome under congenital generalized lipodystrophy. Determine intended scope rather than inferring distinctness from the hierarchy alone. |
| [PNPO deficiency](PNPO_Deficiency-alternatives.md) | 0.5 | Gene-specific PNPO deficiency versus pyridoxal-dependent epilepsy; the latter's definition says the majority have PNPO mutations, suggesting a scope question. |
| [ADan amyloidosis](ADan_amyloidosis-alternatives.md) | 0.5 | Previously investigated likely duplicate terminology; current WHO record intent remains unresolved. |
| [Brain small-vessel disease 1](Brain_Small_Vessel_Disease_1_With_Or_Without_Ocular_Anomalies-alternatives.md) | 0.5 | Two MeSH supplementary concepts; the local source provides labels but insufficient definitions to decide equivalence. |
| [Bieganski dysplasia](Spondyloepimetaphyseal_Dysplasia_Bieganski_Type-alternatives.md) | 0.5 | Two MeSH supplementary concepts; likewise needs source scope review. |

These are triage leads, not adjudicated corrections. The ICD-11 and MeSH
observations describe the saved source extracts, not newly verified live WHO
or NLM records. Labels alone cannot establish equivalence or proper subsumption.

The two **0.7** cases are a different signal:

- [Pentanucleotide-repeat familial adult myoclonus epilepsy](Pentanucleotide_Repeat_Familial_Adult_Myoclonus_Epilepsy-alternatives.md)
- [Dominant-negative TTN structural-variant myopathy](TTN_Related_Myopathy_Dominant_Negative_TTNsv-alternatives.md)

Both curation records deliberately use `skos:closeMatch` to broader historical
MONDO terms. The generator assigns identity prior 0.7 while retaining its usual
0.07/0.03 directional priors. Their top two solutions differ only in accepting
versus rejecting the dismech/MONDO equivalence; no high-prior mapping is rejected
in the chosen solution. Their confidence equals the supplied 0.7 prior ratio.
This is a known scope/prior-modeling question, not independently discovered
contradictory disease evidence. In particular, the TTN input has only three
hypotheses and four consistent assignments; its page displays all four.

## Reproduce and inspect

The report is generated from current production results, not the historical
pre-proxy baseline. Artifacts:

- [summary.json](summary.json): verified current score distribution and exclusions;
- [triage.tsv](triage.tsv): all thirteen entries, target labels, and interventions;
- [experiments.json](experiments.json): complete top assignments, marginals,
  interventions, original input/solution hashes, and solver revision;
- [local-source-context.json](local-source-context.json): read-only OAK extracts,
  including children and source versions;
- [current-source-context.json](current-source-context.json): MONDO and DO source
  stanzas with pinned source URLs and hashes.

The current MONDO annotation source is revision `f1526eeae184f43741ca73ae0050d16f0061fd37`;
DO is `ec05d8346757d228193d33e6ef7a565f430ebe39`. The OAK graph context remains
from the saved snapshots. Only the MONDO and DO source stanzas were refreshed
for this investigation. No source or dismech mapping has yet been changed.

```bash
PYTHONPATH=src uv run --with networkx --with fastobo python \
  analyses/boomer/scripts/investigate_remaining.py \
  --boomer-src /path/to/clean/boomer-py/src \
  --mondo-obo /path/to/pinned/mondo-edit.obo \
  --doid-obo /path/to/pinned/doid.obo
```

Use Boomer `744038e30741009930f57919ca2f03c6473ed198`. Both source OBO checksums
are checked before report output is written. The script validates all thirteen
saved results against exhaustive enumeration, performs interventions only on
copies, and leaves production input and solution files untouched.
