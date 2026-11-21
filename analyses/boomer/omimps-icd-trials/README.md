# OMIMPS trials with Orphanet and both ICD vocabularies

Adding ICD-11 Foundation exposes a family/parent mapping conflict in the FOXE3
model that the focused PS model does not contain. Orphanet and ICD-10-CM do not
resolve that conflict. Gorlin and Waldenström remain consistent for every
qualified source addition. This is a small controlled comparison, not an audit
of the complete external vocabularies.

The three frozen disease models are each run as **baseline, +ORDO, +ICD-10-CM,
+ICD-11 Foundation, and all three**. A sixteenth model tests the previously
proposed FOXE3 ICD-11 scope repair. The original pilot artifacts are untouched.
No disease, grouping, or upstream ontology mapping is edited in this analysis.

**All 16 models completed exhaustive Boolean enumeration.** Fourteen normal
searches also completed and agree with enumeration. The two normal-search
timeouts (FOXE3 all-source and repair) retain their status; their complete
enumerated results supply the reported probabilities.

## Findings

| Trial | Baseline hypotheses | Added qualified mappings: ORDO / ICD-10-CM / ICD-11 | All-source hypotheses | Finding |
|---|---:|---|---:|---|
| [Gorlin syndrome](gorlin/README.md) | 6 | 1 / 0 / 1 | 8 | Both added equivalents are accepted. The ICD-10-CM cross-reference lacks an explicit precision qualifier and contributes no hypothesis. |
| [FOXE3 spectrum](foxe3/README.md) | 6 | 2 / 1 / 3 | 12 | ORDO and ICD-10-CM alone accept all mappings. ICD-11 alone and the combined model have a 0.50 tie between two conflicting exact mappings. |
| [Waldenström macroglobulinemia](waldenstrom/README.md) | 2 | 1 / 1 / 0 | 4 | ORDO and ICD-10-CM mappings are accepted. There is no selected qualified ICD-11 mapping; that variant is identical to baseline. The disease-versus-susceptibility scope question remains. |

The all-source models actually contain **six resources for Gorlin and FOXE3,
and five for Waldenström**, counting DisMech and counting OMIM/OMIMPS as one
resource. Gorlin retains the baseline Disease Ontology mappings but adds no
ICD-10-CM hypothesis; FOXE3 has all three additions but no baseline DO mapping;
Waldenström has neither DO nor an ICD-11 addition. That is seven identifier namespaces for Gorlin and FOXE3, and six for
Waldenström, because OMIM and OMIMPS use separate namespaces. Merely listing a
resource in the trial configuration does not mean it supplied a mapping.

### FOXE3: the extra vocabulary reveals an existing source conflict

| Source entity | Canonical label | Scope in the checked source |
|---|---|---|
| MONDO:0019503 | anterior segment dysgenesis | Broad developmental disease grouping; the curated FOXE3 entry has a broad mapping to it |
| ORDO:88632 | Anterior segment developmental anomaly | Orphanet group; a qualified MONDO equivalent |
| icd11f:1182282997 | Anterior segment dysgenesis | Child of the structural-anomalies category below |
| icd11f:943599144 | Structural developmental anomalies of the anterior segment of eye | Broader parent, also containing Blue sclera and Heterochromia |
| ICD10CM:Q12.3 | Congenital aphakia | Qualified equivalent of the aphakia subtype, not of the whole FOXE3 entry |

MONDO explicitly marks both ICD-11 targets as equivalent to the same grouping.
There is no preferred-external annotation permitting a proxy merge. The two
highest-weight complete assignments reject opposite exact mappings; each
competing hypothesis has prior 0.95. Their mapping marginals and whole-assignment
posteriors are recorded in the [case report](foxe3/README.md), separately from the
0.50 best-versus-next confidence. Adding ORDO and ICD-10-CM does not select one
branch of this tie.

The local ICD-11 definition and hierarchy distinguish the broader parent from
its anterior-segment-dysgenesis child. The captured parent children include Blue
sclera and Heterochromia, providing positive scope context beyond a missing
hierarchy path. The **repair experiment** changes only the exact mapping to the
parent into `MONDO ⊆ ICD parent`, at the same 0.95 prior. All other mappings and
hard constraints remain fixed, and the repaired model accepts every hypothesis.

This reproduces the [earlier FOXE3/ICD investigation](../foxe3/README.md) in a
joint PS model whose curated broad grounding is now respected. It is not a new
upstream correction or a claim that the solver established clinical identity.
The earlier report records direct WHO source checks; this trial uses the pinned
local ICD graph and definitions, not a fresh live WHO verification.

### Coding cross-references need precision

Gorlin's `ICD10CM:Q87.8` is labelled “Other specified congenital malformation
syndromes, not elsewhere classified”. MONDO carries the cross-reference without
an explicit equivalence or directional qualifier, so it is preserved in the
source audit and excluded from logical hypotheses. The FOXE3 family link to
`Q13.8` and the cataract-34 link to `Q12.0` are likewise unqualified. Their
presence alone does not authorize treating a disease as identical to a coding
category. Curating directional mappings for those candidates would be a separate
source-and-scope review.

Waldenström has qualified equivalents to ORDO:33226 and ICD10CM:C88.0. They
introduce no conflict. No selected ICD-11 target is available, so an unchanged
ICD-11 result is an availability control, not evidence of independent ICD-11
agreement. As in the previous PS pilot, the curated related PS mapping does not
logically veto identity inferred through MONDO; adding these vocabularies does
not settle the inherited-susceptibility versus malignancy distinction.

## Constraints, source provenance, and validation

Each variant preserves the baseline facts and the order and priors of its
hypotheses. The baseline is the previous follow-up's **after** model for Gorlin
and FOXE3, and **before** model for Waldenström (retaining the source PS identity,
rather than using the previous sensitivity model). Baseline files reproduce
byte-for-byte against commit `e7a0b07711b650b69d5983e04f07f29004c854ad`.

Only explicitly qualified, non-obsolete mappings with retrieved target records
are imported. Exact mappings become equivalence hypotheses; qualified broad or
narrow mappings become correctly directed ordinary subclass hypotheses. New
mapping priors are 0.95. These trials import qualified MONDO-to-external
assertions; they do not import every direct mapping between external sources.
Excluded, missing, obsolete and conflicting-precision assertions receive explicit
audit decisions. A missing source path never becomes
a negative assertion.

External sources supply their own exported subsumption relations among mapped
targets and any explicit disjointness. Namespace non-equivalence is separate
from hierarchy and is not OWL class disjointness. The existing annotation-aware
[proxy policy](../proxy-merges/README.md) is applied; none of these selected pairs
qualifies for an exception. In these projections ORDO supplies no hierarchy
edge between its selected mapped endpoints; it cannot distinguish the competing
ICD-11 assignments. Its full captured ancestry is retained for inspection.

The [source manifest](sources.json) pins the three external SQL files by SHA-256
and version IRI. All are January 9, 2026 MONDO-source exports. They are separate
from the baseline's September MONDO graph and the newer MONDO annotation catalog
at commit `cbe6d7dba017e3fcd49374e09f4673eb1170df61`. Per-case projections retain
source definitions, ancestry, obsolete flags, complete mapping qualifiers, and
baseline hashes. Source differences are deliberate and visible; no live-source
refresh is implied. Correspondences may share OMIM/Orphanet provenance, so
additional vocabularies are not automatically independent biological evidence.

Normal searches have 60-second limits and 75-second supervisor deadlines.
Independent complete Boolean enumeration has its own 60-second per-model
limit, at most 18 hypotheses; the largest trial has 12. No mappings are pruned
to obtain a result. Normal search status, enumeration status, input hashes,
complete alternatives, marginals and certificates are retained separately.
All use the clean Boomer revision
`744038e30741009930f57919ca2f03c6473ed198`.

## Reproduction

From the repository root, with `BOOMER_SRC` pointing to that clean checkout:

```bash
cd analyses
just boomer-omimps-icd build
just boomer-omimps-icd solve 60
just boomer-omimps-icd verify 60
just boomer-omimps-icd report
```

These stages use frozen projections and need no ontology databases. To reproduce
source capture separately (requires the baseline git object and the exact
versioned SQL files):

```bash
uv run python analyses/boomer/scripts/omimps_icd_trials.py capture \
  --oak-dir /path/to/pinned/oaklib --out /tmp/recaptured-icd-trials
```

Regression checks:

```bash
BOOMER_SRC=/path/to/clean/boomer-py/src uv run pytest -q tests/test_boomer*.py
```

Tests check frozen input and audit reproduction, hash correspondence, baseline
preservation, exclusion of unqualified/obsolete/unretrieved targets, the single
changed mapping in the repair experiment, and actual-reasoner consistency with
and without the ICD-11 conflict. Historical pilot fixtures remain unchanged.
