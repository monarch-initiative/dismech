# Environmental mechanism links

### Linking Environmental Factors into the Pathograph

An `environmental:` entry only appears in the pathograph if it declares which
mechanism it acts on. Use `influences_mechanisms` — the environmental
counterpart of `treatments.target_mechanisms` and
`experimental_models.modeled_mechanisms`:

```yaml
environmental:
- name: Chronic ingestion of arsenic-contaminated drinking water
  exposure_term:
    preferred_term: exposure to arsenic in water via ingestion
    term:
      id: ECTO:0080000
      label: exposure to arsenic in water via ingestion
  influences_mechanisms:
  - target: Systemic inorganic arsenic exposure
    environmental_effect: TRIGGERS
    causal_link_type: DIRECT
    description: >-
      Sustained ingestion of contaminated groundwater is the route by which the
      systemic arsenic burden is established.
    evidence:
    - reference: PMID:21576319
      supports: SUPPORT
      evidence_source: HUMAN_CLINICAL
      snippet: "exact quote from the abstract"
      explanation: Why this supports the exposure acting on this mechanism.
```

**Key points:**
- `target` must match a `pathophysiology` (preferred) or `phenotype` name in the
  same file; a test (`check_environmental_mechanism_targets`) enforces this.
- `environmental_effect` (`EnvironmentalEffectEnum`: `TRIGGERS`, `EXACERBATES`,
  `PREDISPOSES`, `PROTECTS_AGAINST`, `MODULATES`) sets the edge predicate.
  A protective exposure is drawn green, dashed, with a tee head so it never
  reads as a causal arrow. Omitting it falls back to a neutral `influences`
  predicate rather than asserting causation — prefer an explicit value. Only
  `TRIGGERS` and `EXACERBATES` count as mechanistically explaining their target
  for compliance scoring (`qc_plugins.CAUSAL_PREDICATES`).
- The link makes its own claim, so it takes its **own** evidence, separate from
  the environmental entry's general evidence.
- Because these edges have no incoming edges, exposures land at the leftmost
  layer of the layout as initiating steps.
- **Not the same as `Pathophysiology.triggers`**, which hangs an ECTO exposure
  term directly on a mechanism node. Both may coexist: `triggers` annotates the
  node, `influences_mechanisms` pulls the disease-level environmental entry in
  as its own node.
- For a protective exposure, `environmental_effect: PROTECTS_AGAINST` is now the
  preferred signal for the KGX exporter too — it supersedes the older free-text
  `effect:` phrase matching (#2098) when every mechanism link agrees, and yields
  `biolink:associated_with_decreased_likelihood_of`.

Worked example: `Arsenic_Poisoning` (acute and chronic exposure routes both
linked to "Systemic inorganic arsenic exposure").

#### Auditing `exposure_term` coverage

Once an exposure is pathograph-linked it renders as a node on the disorder page,
so an unbound one shows as free text in an otherwise ontology-grounded graph.
`just environmental-term-audit` counts that gap:

```bash
just environmental-term-audit                        # census + recurring concepts
just environmental-term-audit --format tsv --out /tmp/env.tsv
just environmental-term-audit --linked-only --unbound-only --format list
just environmental-term-audit --strict               # exit 1 on any linked+unbound
```

It classifies each `environmental[]` entry `BOUND` / `PARTIAL` / `UNBOUND`, where
**`PARTIAL` means an `exposure_term` block carrying only a free-text
`preferred_term` with no `term:`** — an entry that looks grounded in the YAML
without being grounded in an ontology. It also reports **reuse candidates**: when
the same exposure concept is already bound elsewhere in the KB, the CURIE is
already in `cache/ecto/terms.csv` and the `exposureterm` enum cache, so binding
it needs no ontology research and validates offline.

Two things the audit deliberately does not decide:

- **A reuse suggestion is advisory.** It matches curator-written names, not
  meanings. `.claude/skills/dismech-terms`' rule still governs — *no term beats
  a bad one*. Some exposures (microgravity, emotional stress) are correctly left
  unbound with a `notes:` line recording that ECTO was searched, and the audit
  cannot tell that apart from an un-researched entry.
- **A "conflict" is not necessarily an error.** The audit reports normalized
  names bound to more than one CURIE (e.g. tobacco vs. cigarette smoking); the
  same words can name genuinely different exposures, so it surfaces them for a
  curator rather than resolving them.

Run it before proposing an exposure-binding tranche — issue #8430 was opened
against an assumed gap whose lead example turned out to be bound already.
