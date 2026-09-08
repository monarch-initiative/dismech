# ICD-10 mapping coverage

Exploration on 2026-09-08 of the 1,728 indexed Boomer inputs, including 1,550
grounded entries with `category: Mendelian`. The 12 ungrounded Mendelian
candidates in [the selection report](../mendelian.tsv) are outside this denominator.
This measures available assertions, not validated coding choices or solver results.

| Mapping route | All 1,728 entries | Mendelian 1,550 entries |
|---|---:|---:|
| ICD term anywhere in the saved Boomer input | 164 (9.5%) | 96 (6.2%) |
| Direct disease `icd10cm_mappings` | 21 (1.2%) | 15 (1.0%) |
| Parent MONDO ICD mapping, including unqualified xrefs | 145 (8.4%) | 94 (6.1%) |
| Parent MONDO exact → ORDO → WHO ICD-10 mapping | 1,048 (60.6%) | 950 (61.3%) |
| No mapping through any of the above routes | 625 (36.2%) | 581 (37.5%) |

Rows overlap. Boomer coverage includes subtype codes; the other routes use the
entry's parent disease only. All ICD identifiers in saved inputs are `ICD10CM:`.
Of the 1,357 newly added inputs, 63 (4.6%) contain an ICD term.

## Why Boomer coverage is low

The generator imports only MONDO's direct `skos:exactMatch` assertions to
external vocabularies. It does not import the disease's direct ICD mappings or
follow ORDO's ICD mappings. Relaxing MONDO's exact-match filter adds little:
90 Mendelian parents have exact ICD mappings, and only four additional parents
have nonexact mappings or unqualified xrefs:

| Entry | MONDO mapping |
|---|---|
| Bloom_Syndrome | `skos:closeMatch ICD10CM:Q82.2` |
| Carney_Complex | `oio:hasDbXref ICD10CM:D44.8` only |
| Northern_Epilepsy | `skos:broadMatch ICD10CM:G40.3` |
| Primary_Triglyceride_Deposit_Cardiomyovasculopathy | `skos:broadMatch ICD10CM:E75.5` |

ORDO is the larger source already available locally through OAK. Among the 950
Mendelian entries reached through exact MONDO→ORDO links, 909 have a
`skos:broadMatch`, 37 an exact match, and four a `skos:narrowMatch` (these
predicate groups happen to be disjoint in this cohort). There are 973 mapping
paths because an entry can reach several codes or ORDO terms. Of the 950
entries, 870 currently lack any ICD term in their Boomer input.

The most shared target is `ICD-10:Q87.8`, reached by 105 distinct Mendelian
entries. These broad categories should not become equivalence hypotheses:
doing so would force different diseases toward the same identity. Preserve
the source predicate and provenance when designing Boomer priors.

## Direct mappings omitted from the inputs

Eight Mendelian entries have direct curated ICD mappings but no ICD term in
their Boomer input. These are the current predicates, not an endorsement of
their direction or target vocabulary.

| Entry | ICD10CM target | Curated predicate |
|---|---|---|
| Adult-Onset_Proximal_Spinal_Muscular_Atrophy_Autosomal_Dominant | G12.1 | broadMatch |
| Alagille_syndrome | Q44.7 | narrowMatch |
| Autosomal_Recessive_Multiple_Pterygium_Syndrome | Q79.8 | broadMatch |
| Fabry_Disease | E75.2 | narrowMatch |
| Familial_Hemiplegic_Migraine | G43.4 | broadMatch |
| Junctional_Epidermolysis_Bullosa | Q81.1 | closeMatch |
| Kindler_Epidermolysis_Bullosa | Q81.8 | closeMatch |
| Patent_Ductus_Arteriosus_3 | Q25.0 | broadMatch |

Two issues need resolution before importing these assertions:

* **Vocabulary identity.** WHO ICD-10 and US ICD-10-CM are distinct
  classifications; matching code strings alone do not establish equivalent
  meanings. The existing `crosssource_audit.py` aliases `ICD10CM` to `ICD10`.
  This coverage script keeps the original prefixes. The Fabry and Alagille
  YAMLs also cite WHO ICD-10 cross-references as support for ICD10CM targets;
  that requires separate verification. See the
  [CDC description of ICD-10-CM](https://www.cdc.gov/nchs/icd/icd-10-cm/index.html).
* **Mapping direction.** ORDO records Fabry→E75.2 and Alagille→Q44.7 as
  `skos:broadMatch`; the YAMLs record `skos:narrowMatch`. Orphanet's
  “Narrower” relation describes the disease relative to its ICD target;
  translating this directly to `narrowMatch` reverses the direction.
  Orphanet documents NTBT as a narrower ORPHA term mapping to a broader ICD
  term in its [alignment specification](https://www.orphadata.com/docs/ORPHAnomenclaturexmlcontent.pdf).
  SKOS `broadMatch` points to the broader target, as specified by the
  [W3C mapping properties](https://www.w3.org/TR/skos-reference/#mapping).

## Inspect and reproduce

* [coverage.tsv](coverage.tsv): every indexed entry with separate coverage
  columns. Filter `mendelian=1` and an empty `boomer_icd10_terms` for all
  **1,454** Mendelian entries missing ICD in Boomer.
* [missing-mendelian.txt](missing-mendelian.txt): the **581** Mendelian entries
  with no mapping in any examined route. This is a source-coverage gap, not
  proof that a disease has no ICD code.
* [mappings.tsv](mappings.tsv): each parent mapping path, original predicate,
  target prefix, and source. An ORDO row is reachable through an exact
  parent MONDO link; it is not a direct dismech assertion.
* [summary.json](summary.json): counts and SHA-256 fingerprints of the OAK databases.

```bash
uv run python analyses/boomer/scripts/icd10_coverage.py
# Optional: --oak-dir /path/to/local/snapshots --out /tmp/icd10-audit
```

The snapshots identify MONDO 2026-05-05 and the MONDO source extract of ORDO
2026-01-09. ORDO stores these ICD mapping targets in semantic-sql's `value`
column, not `object`; querying only object-valued mappings would miss them.
The script opens databases read-only and does not download or refresh them.
It reads indexed disorder YAMLs through the shared KB loader and writes only
this audit's four generated data files. Repeating against unchanged sources
produces identical bytes.

This is a bounded exploration: it does not traverse MONDO ancestors, follow
nonexact MONDO→ORDO links, inspect other external mapping routes, or infer
codes from names. Source snapshots differ in date, and the ORDO snapshot is
a MONDO source extract; the routes should not be assumed to provide statistically
independent evidence. Saved Boomer inputs were also generated at different times.

## Proposed workflow

Add ORDO→ICD mappings to extraction through the existing local OAK snapshots,
retaining broad/exact/narrow predicates and source paths. Resolve WHO ICD-10
adapter support separately from the current ICD10CM adapter; the validation
OAK config is not yet a complete Boomer source registry. Review direct curated
mapping direction and provenance before importing it. Generate an inspectable
mapping table first, then translate supported predicates into directional
Boomer hypotheses with explicit priors. Restrict regeneration to affected
inputs and preserve existing solver outputs until they are explicitly rerun.

This exploration changes no disease YAMLs, Boomer inputs, or solver results.
