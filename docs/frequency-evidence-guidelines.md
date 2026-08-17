# Frequency Qualifier Evidence Guidelines

Curator-facing SOP for assigning and supporting `frequency` values on phenotypes
in DisMech disorder files. These guidelines apply to the **current schema** —
no schema change is required.

Background and the broader schema design discussion live in
[`frequency-evidence-proposal.md`](frequency-evidence-proposal.md) and
[issue #112](https://github.com/monarch-initiative/dismech/issues/112). The
present document is the pragmatic SOP that curators (human or agent) should
follow today.

## The problem in one paragraph

A `Phenotype` has a single `evidence` list, but it carries two distinct claims:

1. **Disease–phenotype association (D2P):** "this phenotype occurs in this disease"
2. **Frequency claim:** "this phenotype occurs in *N%* of patients with this disease"

Most evidence snippets only support claim 1. Curators routinely assign a
`frequency` qualifier (e.g. `FREQUENT`) without any quantitative source for the
*frequency* itself. This is acceptable in many cases — but it must be
**transparent**, not implicit.

## Frequency enum reference

The schema defines `FrequencyEnum` with HPO-aligned bands:

| Enum value      | HPO term ID  | Range    |
|-----------------|--------------|----------|
| `OBLIGATE`      | HP:0040280   | 100%     |
| `VERY_FREQUENT` | HP:0040281   | 80–99%   |
| `FREQUENT`      | HP:0040282   | 30–79%   |
| `OCCASIONAL`    | HP:0040283   | 5–29%    |
| `VERY_RARE`     | HP:0040284   | <5%      |

If a paper gives an exact percentage, place it in the band above. **Bands take
precedence over verbal hedging** — "70% of patients" is `FREQUENT`, even if the
authors call it "common".

## Acceptable evidence patterns

The following four patterns are all acceptable, listed strongest to weakest.
Prefer the strongest pattern available; degrade gracefully when stronger evidence
does not exist.

### Pattern A — Direct quantitative statement (preferred)

The cited paper explicitly reports a percentage (or a fraction that converts
trivially) for this phenotype in this disease.

```yaml
- name: Congenital Heart Defects
  frequency: FREQUENT
  evidence:
  - reference: PMID:26504441
    supports: SUPPORT
    snippet: "the prevalence of congenital heart disease in infants with Down
      syndrome is 40%"
    explanation: 40% falls in the FREQUENT band (30-79%).
```

The `explanation` should make the band assignment **explicit**: state the
percentage and the band it falls into.

### Pattern B — Cohort count derived to a percentage

The paper reports raw counts (e.g. "12 of 19 patients") rather than a percentage.
Quote the counts verbatim and do the arithmetic in `explanation`.

```yaml
- name: Optic Atrophy
  frequency: FREQUENT
  evidence:
  - reference: PMID:32106311
    supports: SUPPORT
    snippet: "Optic atrophy was reported in 12 of 19 patients"
    explanation: 12/19 = 63%, which falls in the FREQUENT band (30-79%).
```

Never paraphrase the counts — the snippet must be a verbatim quote (see the
main evidence SOP in `CLAUDE.md`).

### Pattern C — Qualitative literature term mapped to a band

The paper uses a verbal frequency term ("common", "rare", "characteristic")
without numbers. Use the table below as the **default mapping** and document
the mapping in `explanation`.

| Literature wording                                       | Default enum     |
|----------------------------------------------------------|------------------|
| "in all", "universal", "invariable", "always present"    | `OBLIGATE`       |
| "almost all", "nearly universal", "highly characteristic", "hallmark", "very common", "typical" | `VERY_FREQUENT` |
| "common", "frequent", "often", "majority", "predominant" | `FREQUENT`       |
| "occasional", "uncommon", "sometimes", "in a minority"   | `OCCASIONAL`     |
| "rare", "infrequent", "isolated reports", "few cases"    | `VERY_RARE`      |

```yaml
- name: Ecchymoses
  frequency: FREQUENT
  evidence:
  - reference: PMID:37366866
    supports: SUPPORT
    snippet: "Common manifestations include... ecchymoses."
    explanation: |
      Author wording "common" maps to FREQUENT under the DisMech qualitative
      mapping (see docs/frequency-evidence-guidelines.md). No quantitative
      data was reported.
```

If you depart from the default mapping, **say so explicitly** in the
explanation and give a reason (e.g. "review describes it as 'common' but
specifies >80% in a referenced cohort, so VERY_FREQUENT is used instead").

### Pattern D — Clinical judgment with no frequency-specific evidence

Sometimes a phenotype is well established but no source — abstract, review, or
cohort — gives any frequency signal at all. This is acceptable when:

- the D2P association itself is well-supported by evidence,
- the frequency band is defensible from clinical experience or a tertiary
  reference, **and**
- you make the basis explicit.

There are two acceptable ways to handle this:

1. **Assign the frequency and document the basis** in an evidence item whose
   `supports: NO_EVIDENCE` (or in a curator note), making clear that the
   frequency is a clinical estimate, not extracted from the citation:

   ```yaml
   - name: Fatigue
     frequency: VERY_FREQUENT
     evidence:
     - reference: PMID:12345678
       supports: SUPPORT
       snippet: "Fatigue is reported by most patients with the disorder."
       explanation: |
         Snippet supports the D2P association. The VERY_FREQUENT band is a
         clinical estimate consistent with author wording "most patients";
         no quantitative cohort data found.
   ```

2. **Omit `frequency` entirely.** The schema does not require it. Leaving it
   off is *strictly better* than fabricating quantitative-looking justification.

   ```yaml
   - name: Fatigue
     # frequency intentionally omitted: no defensible source
     evidence:
     - reference: PMID:12345678
       supports: SUPPORT
       snippet: "Fatigue is reported by most patients with the disorder."
       explanation: Supports the D2P association.
   ```

When in doubt, **omit the frequency**. A missing frequency is honest; a
fabricated one is not.

## Anti-patterns

These patterns are not acceptable and should be removed when encountered.

### Anti-pattern 1 — Frequency that contradicts the evidence

```yaml
# WRONG
- name: Generalized Tonic-Clonic Seizures
  frequency: OCCASIONAL          # claims 5-29%
  evidence:
  - reference: PMID:30082241
    snippet: "70% experienced generalized tonic-clonic seizures"
```

70% is `FREQUENT`, not `OCCASIONAL`. The band must match the quoted number.

### Anti-pattern 2 — Frequency with empty `evidence: []`

```yaml
# WRONG
- name: Lymphadenopathy
  frequency: FREQUENT
  evidence: []
```

Either add an evidence item (any of patterns A–D) or omit `frequency`.

### Anti-pattern 3 — Fabricated quantitative-looking explanation

Do not invent a percentage in `explanation` that does not appear in the cited
text. If the snippet says "common", the explanation must not say "≈70%" unless
that number is itself sourced.

### Anti-pattern 4 — Frequency assigned to a non-typical population

A cohort study of 19 severe pediatric cases is not representative of the whole
disease. If a percentage is derived from a narrow population, say so:

```yaml
explanation: |
  68% in the FANCB severe-pediatric subcohort (PMID:32106311).
  Whole-disease frequency is likely lower; this is the subcohort estimate.
```

Consider whether the qualifier belongs on the parent phenotype at all, or
whether it should be modeled with a `subtype:` foreign key.

### Anti-pattern 5 — Frequency band inherited across a scope boundary

Anti-pattern 4 is about a band derived from a population *narrower* than the
entry. This is the mirror image, and it is the more common one: a band quoted
from a source scoped *more broadly* than the entry it lands on.

```yaml
# WRONG — in Osteogenesis_Imperfecta_Type_I.yaml
- name: Bone Pain
  frequency: FREQUENT            # claims 30-79% of OI type I
  evidence:
  - reference: ORPHA:666         # ORPHA:666 is "Osteogenesis imperfecta" — all types
    supports: SUPPORT
    snippet: "HP:0002653 | Bone pain | Frequent (79-30%)"
```

`ORPHA:666` bands describe the whole OI spectrum, in which the severe types
contribute most of the burden; type I is the mildest form. The band is real and
the quote is verbatim, so **every check in this repo passes** — snippet
verification, term validation, and schema validation all see a well-formed
record. Only a curator reading the source's scope can catch it. The same applies
to a `kb/groupings/` union, an umbrella `Disease` entry, a MONDO grouping term,
or a `has_subtypes` parent: a band measured over the union is not a band for any
one member.

**The rule.** Before adopting a `frequency:` from a source, ask what population
the source measured. If it is broader than the entry (or than the `subtype:` the
record is scoped to), you may not adopt the band unchanged. Choose one of:

1. **Scope the record instead** — if the entry defines `has_subtypes` and the
   band genuinely belongs to one of them, set the `subtype:` foreign key rather
   than restricting the scope in prose. `subtype:` is checked by
   `tests/test_data.py`; a `notes:` string is not. Note `subtype:` is
   single-valued, so a restriction naming several subtypes ("primarily in RDEB",
   covering three of four) cannot be expressed this way — keep it in `notes:`.
2. **Keep the band, demote the evidence** — when a *narrower*, quantitative
   source disagrees with the broad band, keep the narrow band and cite the broad
   row as `supports: PARTIAL` with an `explanation` naming the conflict
   outright.
3. **Drop the band** — when the only source for it is the broader entity, omit
   `frequency:` and record the reason where a reader will meet it: the cited
   row's `explanation` (best — it sits next to the band you declined to adopt)
   or the phenotype's `notes:`. This is the default; per Pattern D, a missing
   frequency is honest.

Do **not** keep the band and merely note the mismatch in prose. That leaves a
machine-readable quantitative claim the KB cannot defend, annotated by a string
nothing reads.

**Worked precedents already in the KB:**

| Entry / phenotype | Choice | Why |
|---|---|---|
| `Marfan_Syndrome` → `Spontaneous Pneumothorax` | 2 — keep narrow band | `ORPHA:558` says "Very frequent (99-80%)"; PMID:25765122 measures 5–11%. Band stays `OCCASIONAL`, ORPHA row cited `PARTIAL` with the conflict stated. |
| `Dystrophic_Epidermolysis_Bullosa` → `Cutaneous Squamous Cell Carcinoma` | 1 — scope it | `VERY_FREQUENT` comes from National EB Registry cumulative risk in severe generalized RDEB (90.1% by 55), not DEB as a whole, so the record carries `subtype: RDEB-sev gen`. |
| `Dystrophic_Epidermolysis_Bullosa` → `Osteoporosis` | 3 — drop it | The only source is a GeneReviews management sentence that states no rate. Band omitted; `notes:` records the reason. |
| `Osteogenesis_Imperfecta_Type_I` → `Hyperhidrosis` | 3 — drop it | `ORPHA:666`'s "Frequent (79-30%)" row is cited for the association only; the evidence `explanation` states that no type-I band is asserted because the band reflects the whole OI spectrum. |

## Quick checklist

When you assign or change a `frequency:` value, verify:

- [ ] At least one evidence item is present (not `evidence: []`)
- [ ] The chosen enum band matches any quoted percentage
- [ ] If quantitative: percentage / arithmetic appears in `explanation`
- [ ] If qualitative: the literature term maps to the assigned enum (Pattern C table)
- [ ] If clinical estimate (Pattern D): `explanation` says so plainly
- [ ] If none of the above is achievable: `frequency` is **omitted**, not guessed

## Related references

- Main evidence SOP: `CLAUDE.md`, §"Standard Operating Procedure: Adding/Editing Evidence"
- Schema design discussion: [`frequency-evidence-proposal.md`](frequency-evidence-proposal.md)
- Tracking issue: [monarch-initiative/dismech#112](https://github.com/monarch-initiative/dismech/issues/112)
