# Biological scale and activity state

### Pathophysiology Biological Scale Tag

Each `Pathophysiology` node may carry an optional `biological_scale:` value
tagging the node with the primary biological scale of its substrate. The
enum is small and closed — one of `MOLECULAR`, `CELLULAR`, `TISSUE`, or
`ORGANISM`. Each value covers both ongoing processes and persistent states
at that scale (e.g. `MOLECULAR` includes both a kinase's activity and a
fusion protein's existence; `ORGANISM` includes both cytokine storm and
chronic hyperphenylalaninemia).

```yaml
pathophysiology:
- name: SHP2 Gain-of-Function Activation
  biological_scale: MOLECULAR
  molecular_functions:
  - preferred_term: protein tyrosine phosphatase activity
    term: {id: GO:0004725, label: protein tyrosine phosphatase activity}
- name: ERK Cascade Hyperactivation
  biological_scale: CELLULAR
- name: Pulmonary Valve Dysplasia
  biological_scale: TISSUE
- name: Coagulopathy
  biological_scale: ORGANISM
```

**When to use:** on any pathophysiology node when the primary scale is
clear. Legacy nodes without the tag validate unchanged — it is optional.

**Single-value discipline.** Pick one value. If a node would naturally take
two (e.g. a fusion protein event bundled with its cellular consequence),
that is a signal the node bundles two mechanistic claims and should be
split into atomic nodes.

**Reference.** `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md` records the
survey that fixed the enum at these four values and the bundle patterns
curators should watch for.

### Gain/Loss of Function: which slot?

`GAIN_OF_FUNCTION` and `LOSS_OF_FUNCTION` appear in **two different enums**, on two
different classes. They are not interchangeable, and the free-text `functional_impact`
string is a legacy third option retained only for older entries — prefer
`functional_impact_category` whenever a controlled value applies. Decision tree:

| The claim is about… | Slot | Enum |
|---|---|---|
| the functional consequence of a specific genetic **variant** | `GeneticContext.functional_impact_category` | `FunctionalImpactEnum` |
| the activity **state** of a pathway, process, or molecular function | `Descriptor.modifier` | `ModifierEnum` |
| that state merely running **above or below** its normal level | `Descriptor.modifier` | `ModifierEnum` → `INCREASED` / `DECREASED` |

**Variant consequence → `functional_impact_category`.** This lives on `GeneticContext`,
which also carries `allele_type`, `variant_origin`, and `zygosity` — so it is meaningless
without a variant to hang it on. It has finer distinctions than `ModifierEnum` does
(`PARTIAL_LOSS_OF_FUNCTION`, `DOMINANT_NEGATIVE`, `HYPERMORPHIC`, `NEOMORPHIC`); use them
when the literature supports them.

**Pathway activity state → `modifier`.** This lives on the `Descriptor` base class
(`BiologicalProcessDescriptor`, `MolecularFunctionDescriptor`, …) and describes the node's
state *regardless of cause* — which may be no host mutation at all. The worked example is
`Adult_T_Cell_Leukemia_Lymphoma`: HTLV-1 Tax drives NF-kB activation independently of any
host variant, so there is nothing anywhere in the pathway for
`functional_impact_category` to describe. (Note that the entry itself is careful *not* to
claim a uniformly constitutive Tax signal across every established tumor — activity
differs by clinical subtype. Guidance prose should not reintroduce a stronger claim than
the node it points at makes.)

```yaml
# Non-genetic GOF — viral oncoprotein drives the pathway
biological_processes:
- preferred_term: positive regulation of NF-kappaB transcription factor activity
  modifier: GAIN_OF_FUNCTION
  term:
    id: GO:0043123
    label: positive regulation of canonical NF-kappaB signal transduction
```

`Noonan_Syndrome` is the mutation-driven counterpart: `modifier: GAIN_OF_FUNCTION` on the
SHP2 `protein tyrosine phosphatase activity` node (`GO:0004725`), where a PTPN11 missense
variant destabilizes autoinhibition.

**The two slots may co-occur** on a mutation-driven node, since they make different claims
— the variant's consequence, and the resulting activity state. Nothing in the schema
prevents it. Note that no KB entry currently does this, so there is no worked example to
copy; if you are the first, the `genetic_context` block still needs its own
allele/origin/zygosity detail rather than being added just to carry the category.

**The `INCREASED` vs `GAIN_OF_FUNCTION` line — quantitative vs qualitative.** This is the
one curators hit most, because the KB already holds thousands of `INCREASED`/`DECREASED`
annotations and `modifier` is single-valued:

- **`INCREASED` / `DECREASED`** — the claim is *quantitative*: a normally regulated
  process running above or below its normal level. These are PATO-bound
  (`PATO:0002300` / `PATO:0002301`), so they stay queryable via OWL/semantic tooling.
  **This is the default.**
- **`GAIN_OF_FUNCTION` / `LOSS_OF_FUNCTION`** — the claim is *qualitative*: the process is
  driven outside its normal regulatory constraints (viral oncoprotein, autocrine loop,
  epigenetic silencing, protein sequestration, constitutive activation). These are
  **unbound** — no suitable ontology term exists across PATO/GENO/GO/SO — so choosing them
  trades ontology grounding for expressivity. Make that trade deliberately.

Do **not** migrate an existing `INCREASED`/`DECREASED` annotation to
`GAIN_OF_FUNCTION`/`LOSS_OF_FUNCTION` without that qualitative justification. "The pathway
is very active" is `INCREASED`; "the pathway is no longer under host regulatory control"
is `GAIN_OF_FUNCTION`.
