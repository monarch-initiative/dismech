# Hemochromatosis: a phenotypic series crosses mechanistic boundaries

**Orphanet distinguishes two SLC40A1 disorders that MONDO currently equates.**
SLC40A1-related hemochromatosis involves hepcidin-resistant iron export;
ferroportin disease involves impaired export and macrophage iron retention.
The current MONDO type-4 definition describes the former, but its mappings and
exact synonyms also identify the latter. The proposed correction weakens the
ferroportin-disease mapping to a related mapping, while explicitly leaving the
larger concept/synonym reconciliation open.

The PS also includes **African iron overload**, described in the checked sources
as involving dietary iron intake and possible genetic factors. This is a useful
counterexample to treating every member of an OMIM phenotypic series as another
established Mendelian subtype or as another defect causing hepcidin deficiency.

## Entities and source scopes

| ID | Canonical source label | Checked scope |
|---|---|---|
| OMIMPS:235200 | Hemochromatosis | Seven numbered members in the January 2026 export |
| MONDO:0006507 | hereditary hemochromatosis | Inherited metabolic disorder with tissue iron accumulation |
| MONDO:0011631 | hemochromatosis type 4 | Text definition copied from the SLC40A1 hemochromatosis Orphanet record; also carries exact ferroportin-disease synonyms |
| ORDO:647834 | SLC40A1-related hemochromatosis | High transferrin saturation and hepatocellular iron deposition |
| ORDO:648562 | Ferroportin disease | Macrophage iron retention, mild anemia, elevated ferritin; explicitly distinguished from hemochromatosis |
| ORDO:139491 | OBSOLETE: Hemochromatosis type 4 | Obsolete legacy record; excluded from hypotheses |
| MONDO:0011012 | African iron overload | Excess dietary iron intake and possible genetic factors |
| ORDO:139507 | Dietary iron overload disease | Dietary iron overload with possible genetic contribution |
| icd11f:869212237 | African iron overload | ICD-11 Foundation category mapped to the African iron-overload class |
| ICD10CM:E83.110 | Hereditary hemochromatosis | Qualified family-level equivalent in MONDO |

Definitions, labels, hierarchy, complete selected current MONDO stanzas,
qualified xrefs and the original DisMech record projection are saved in
[projection.json](projection.json). The clinical distinction is independently
supported by [Orphanet's SLC40A1 gene record](https://www.orpha.net/en/disease/gene/SLC40A1?mode=gene&name=),
which names gain of function for 647834 and loss of function for 648562, and the
[BIOIRON classification recommendations](https://pubmed.ncbi.nlm.nih.gov/34601591/).
These sources supply biological context; Boomer does not infer gene effects.

## PS coverage and classification

| OMIM member | Snapshot label | Grounded candidate in the pinned DisMech KB |
|---|---|---|
| OMIM:235200 | hemochromatosis, type 1 | Hemochromatosis: Type 1 / HFE |
| OMIM:601195 | iron overload 1n africa | None found by primary/subtype grounding |
| OMIM:602390 | hemochromatosis, type 2a | Hemochromatosis: Type 2A / HJV |
| OMIM:604250 | hemochromatosis, type 3 | Hemochromatosis: Type 3 / TFR2 |
| OMIM:606069 | hemochromatosis, type 4 | Hemochromatosis: Type 4 / SLC40A1, with an explicit allelic-scope caveat |
| OMIM:613313 | hemochromatosis, type 2b | Hemochromatosis: Type 2B / HAMP |
| OMIM:615517 | hemochromatosis, type 5 | Hemochromatosis: Type 5 / FTH1, retaining the existing Limited gene-disease evidence caveat |

The unusual `1n` spelling above is retained from the OMIM export. Coverage
scans all primary and subtype groundings at DisMech commit
`5cefcf9230687cbe99f64c18f886bb95724425ea` through MONDO's numbered-OMIM
exact mappings. Six of seven have candidates, all within one existing entry;
this is neither six independent entries nor six independently verified exact
clinical matches. The absence of a grounded candidate is a curation lead,
not proof that no text elsewhere in the KB mentions the condition.

This pilot adds a **broad mapping from the existing Hemochromatosis entry to
OMIMPS:235200**. The series includes its six enumerated genetic subtypes plus
African iron overload; equating the scopes would obscure that boundary.
No new grouping or disease is created. The rationale for the series is shared
iron-overload phenotype with heterogeneous mechanisms and etiologies, not a
single inheritance pattern or one sufficient molecular classifier. In particular,
FTH1-related iron handling and dietary iron loading do not justify a necessary
hepcidin-deficiency criterion. A grouping over separately curated entities could
be useful later, but duplicating the current six embedded subtypes would add
no member coverage now.

## Scoped Boomer comparison

The joint model contains the **DisMech family and its Type 4 row**, with African
iron overload as additional ontology context. All seven PS members contribute
membership context. The remaining five curated subtype groundings and their
external mapping networks are deliberately outside this experiment. This is a
bounded scope investigation, not an exhaustive alignment of the whole PS.

The baseline aligns DisMech, MONDO, OMIM/OMIMPS and DO. Separate variants add
ORDO, ICD-10-CM and ICD-11 Foundation; the combined model contains **seven
resources including DisMech**, or eight identifier namespaces when OMIM and
OMIMPS are counted separately. Every named resource contributes actual mapping
hypotheses: ICD-11 enters through African iron overload, not through the
SLC40A1 pair. These are qualified MONDO-to-source mappings; direct external-to-
external mapping assertions are not imported.

All six models completed independent exhaustive enumeration. Three normal searches completed and agree with enumeration; ORDO, all-source and repair normal searches timed out and retain that status. The probabilities below come from enumeration.

| Variant | Hypotheses | Normal search | Consistent assignments | Best/next confidence |
|---|---:|---|---:|---:|
| [baseline](baseline/enumeration.json) | 8 | ALL_MAPPINGS_CONSISTENT | 256 | 0.90 |
| [ordo](ordo/enumeration.json) | 11 | TIMED_OUT | 1,536 | 0.50 |
| [icd10cm](icd10cm/enumeration.json) | 9 | ALL_MAPPINGS_CONSISTENT | 512 | 0.90 |
| [icd11f](icd11f/enumeration.json) | 9 | ALL_MAPPINGS_CONSISTENT | 512 | 0.90 |
| [all](all/enumeration.json) | 13 | TIMED_OUT | 6,144 | 0.50 |
| [repair](repair/enumeration.json) | 12 | TIMED_OUT | 4,096 | 0.90 |

The combined model has two equally weighted optimal assignments:

| Mapping from hemochromatosis type 4 | Best assignment A | Best assignment B | Input prior | Marginal posterior |
|---|---|---|---:|---:|
| SLC40A1-related hemochromatosis | Reject | Accept | 0.95 | 0.487179 |
| Ferroportin disease | Accept | Reject | 0.95 | 0.487179 |

Each best complete assignment has unnormalized prior weight 0.024248846039 and whole-solution posterior 0.248706113222. Confidence 0.50 compares these two distinct assignments; it is not their whole-solution posterior or either mapping's marginal. The repair's best assignment accepts all its hypotheses, with best/next confidence 0.90. See the complete assignments and marginal arrays in the linked enumeration files.

The two Orphanet equivalents have the same supplied prior, 0.95. The competing
best assignments reject opposite equivalents. Neither ICD vocabulary supplies
biological evidence choosing the gain-of-function branch; the source definitions
and gene-effect distinctions do. No selected pair satisfies the preferred-target
proxy-merge policy. Namespace non-equivalence is a modeling constraint, **not
OWL class disjointness**, and an absent hierarchy path is never a negative fact.

The repair replaces only the 648562 equivalence hypothesis with a non-entailing
related mapping annotation. It retains all labels, hard constraints, other
mapping hypotheses and their priors. A related mapping neither asserts
containment nor prohibits equivalence; it merely ceases to supply that equality.
This is a simulated source correction, not a before/after comparison of applied
MONDO releases or a claim that improved consistency proves clinical identity.

All variants hold the pinned pre-curation DisMech record fixed. The newly added
broad PS mapping is validated separately and is not an additional hypothesis
in these source-intervention models. A broad mapping also does not logically
negate the equivalence that MONDO currently supplies to the PS; consistency
alone cannot decide the family-versus-series scope question.

## Proposed ontology edit and remaining work

[Structured proposal](../../../ontology_changes/mondo-0011631-ferroportin-related-match.yaml):

```yaml
about_node: MONDO:0011631
mapping_target: Orphanet:648562
old_value: MONDO:equivalentTo
new_value: MONDO:relatedTo
```

This is **SELF_PROPOSED / NOT_FILED**, not an applied MONDO change. Keep the
647834 equivalence, matching the current text definition. The related qualifier
is a conservative interim correction while the legacy class scope is reviewed.
A broader SLC40A1 umbrella with separately represented allelic disorders is
another possible modeling outcome, but it would require explicit class,
definition, hierarchy and mapping decisions. The current mapping registry does
not silently turn this qualifier change into a concept split.

MONDO still carries two exact ferroportin-disease synonyms and a gene-based
logical definition, and the OMIM/DO legacy type-4 scopes remain unresolved.
Those annotations are visible in the saved stanza and are not claimed to be
fixed by this proposal. African iron overload remains a member-curation lead;
its dietary component should not be replaced with an invented Mendelian model.

## Provenance and reproduction

[Sources](sources.json) pins six SQLite files by SHA-256 and version IRI.
The MONDO hierarchy is the September 2026 release; DO is February 2026;
OMIM, ORDO and both ICD source exports are January 9, 2026. Current MONDO
xref qualifiers and text are separately pinned to commit
`ece3a53ce89e1064c482c2d389fb3812492d9922`, checked November 27, 2026.
This intentionally mixes a recorded older graph with newer explicit qualifiers;
it does not claim a simultaneous November release of every resource.

Only current, unambiguously qualified mappings with retrieved, live targets
enter the model. Unqualified E83.11/E83.119 references are preserved in the audit
and excluded from hypotheses. Current source annotations replace older
OMIM/PS exact-match opinions for selected terms. Primary/subtype grounding
priors are 0.90; qualified source mappings use 0.95. Repeated assertions are
deduplicated. Supplied model probabilities are not empirical clinical confidence.

Use a clean Boomer checkout at `744038e30741009930f57919ca2f03c6473ed198`:

```bash
export BOOMER_SRC=/path/to/clean/boomer-py/src
uv run python analyses/boomer/scripts/omimps_hemochromatosis.py build
uv run python analyses/boomer/scripts/omimps_hemochromatosis.py solve --boomer-src "$BOOMER_SRC" --timeout 60
uv run python analyses/boomer/scripts/omimps_hemochromatosis.py verify --boomer-src "$BOOMER_SRC" --timeout 120
uv run pytest -q tests/test_boomer_hemochromatosis.py tests/test_ontology_changes.py
just validate kb/disorders/Hemochromatosis.yaml
just validate-ontology-changes
```

Build, solve and verify need only the frozen projection and solver. The separate
`capture --mondo-obo <file>` operation requires the pinned source file (hash
checked), SQL snapshots and DisMech git objects. Normal searches have a 60-second
limit and a 75-second supervisor deadline. Enumeration is limited to 18
hypotheses and a 135-second supervisor deadline at the shown setting. Each
result records its input hash and solver revision. Timed-out normal searches
remain marked as such; complete enumeration, when available, supplies the
reported assignment probabilities and validates completed searches independently.
