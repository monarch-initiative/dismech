# Design: ModifierEnum PATO Bindings + GOF/LOF Enum Values (Proposal A — PhenoCAM v2.5)

**Date:** 2026-06-26
**Author:** Vibhor Gupta
**Status:** Approved for implementation
**Related:** PhenoCAM v2.5 proposal, Issue #743

---

## Background

PhenoCAM v2.5 is an incremental improvement strategy for the dismech pathograph model, proposed
as an alternative to the full V2 schema redesign. Proposal A (this spec) is the smallest and most
self-contained change: ground `ModifierEnum` in PATO ontology terms and add two new enum values
(`GAIN_OF_FUNCTION`, `LOSS_OF_FUNCTION`) to allow structured expression of variant functional
effects, which are currently buried in free-text node names.

---

## Problem

`ModifierEnum` has 5 values (INCREASED, DECREASED, ABNORMAL, DYSREGULATED, ABSENT) with **no
`meaning:` bindings**. This means:
- The enum is not OBO-grounded — no OWL semantics, no semantic similarity reasoning
- GOF/LOF must be encoded in free-text node names (e.g. "SHP2 Gain-of-Function Activation"),
  making them unqueryable as structured data
- Curators have no enum value to reach for when a variant or activity is gain- or loss-of-function

---

## Ontology Term Verification

All candidate PATO terms were verified via OAK (`runoak -i sqlite:obo:pato`) on 2026-06-26.
The proposal's original PATO IDs were found to be largely hallucinated:

| Enum Value | Proposed ID | Actual PATO term at that ID | Decision |
|---|---|---|---|
| INCREASED | PATO:0001998 | "conspicuousness" ❌ | Use `PATO:0002300` "increased quality" (most general active PATO term; `title:` stays "Increased") |
| DECREASED | PATO:0001997 | "decreased amount" ⚠️ | Use `PATO:0002301` "decreased quality" (more general than "decreased amount"; `title:` stays "Decreased") |
| ABSENT | PATO:0000462 | "absent" ✓ | Use as-is |
| ABNORMAL | PATO:0000460 | "abnormal" ✓ | Use as-is |
| DYSREGULATED | PATO:0001789 | "domed" ❌ | No PATO term exists — skip binding |
| GAIN_OF_FUNCTION | PATO:0001396 | "cellular quality" ❌ | No suitable term — see below |
| LOSS_OF_FUNCTION | PATO:0001561 | "having extra processual parts" ❌ | No suitable term — see below |

**GOF/LOF ontology search summary** (all searched 2026-06-26):

| Ontology | Result |
|---|---|
| PATO | All function-related terms are obsolete. No active GOF/LOF term. |
| GENO | No GOF/LOF terms found. |
| GO | No GOF/LOF terms found. |
| SO | `SO:0002053` / `SO:0002054` exist but are **variant-consequence terms**, not activity modifiers. Semantic mismatch — not used. |

**Conclusion:** `GAIN_OF_FUNCTION` and `LOSS_OF_FUNCTION` ship without `meaning:` bindings.
This reflects a genuine gap in the biomedical ontology community — no standard activity-modifier
vocabulary exists for GOF/LOF outside the variant-consequence frame.

---

## Scope

**Approach C** — schema + OAK config + one exemplar KB update.

### In scope
1. Add `PATO:` prefix to `src/dismech/schema/dismech.yaml`
2. Add `meaning:` bindings to 4 of the 5 existing enum values
3. Add `GAIN_OF_FUNCTION` and `LOSS_OF_FUNCTION` as new unbound enum values
4. Add `PATO: sqlite:obo:pato` to `conf/oak_config.yaml`
5. Add `modifier: GAIN_OF_FUNCTION` to the SHP2 molecular function descriptor in
   `kb/disorders/Noonan_Syndrome.yaml` as the exemplar
6. Run full QC (`just qc`) to confirm no regressions

### Out of scope
- Retroactive KB migration of existing free-text GOF/LOF node names — deferred to follow-up PR
- Renaming pathophysiology nodes (node name is a foreign key)
- Proposal B (kind: slot) or Proposal C (etiology block)

---

## Changes

### 1. `src/dismech/schema/dismech.yaml`

**1a. Add PATO prefix** (in the `prefixes:` block):
```yaml
PATO: http://purl.obolibrary.org/obo/PATO_
```

**1b. Update `ModifierEnum`:**
```yaml
ModifierEnum:
  description: Qualifiers for direction, intensity, or pathological state of a descriptor
  permissible_values:
    INCREASED:
      title: Increased
      meaning: PATO:0002300  # increased quality
      description: Upregulated, hyperactive, elevated, or excessive
    DECREASED:
      title: Decreased
      meaning: PATO:0002301  # decreased quality
      description: Downregulated, hypoactive, reduced, or deficient
    ABNORMAL:
      title: Abnormal
      meaning: PATO:0000460  # abnormal
      description: Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
    DYSREGULATED:
      title: Dysregulated
      # No PATO term exists — verified via OAK 2026-06-26
      description: Regulation is impaired (may be increased or decreased)
    ABSENT:
      title: Absent
      meaning: PATO:0000462  # absent
      description: Not occurring or not present
    GAIN_OF_FUNCTION:
      title: Gain of Function
      # No suitable ontology term found across PATO/GENO/GO/SO (verified 2026-06-26)
      # SO:0002053 exists but is a variant-consequence term, not an activity modifier
      description: Variant or activity that confers an abnormal or enhanced function
    LOSS_OF_FUNCTION:
      title: Loss of Function
      # No suitable ontology term found across PATO/GENO/GO/SO (verified 2026-06-26)
      # SO:0002054 exists but is a variant-consequence term, not an activity modifier
      description: Variant or activity that reduces or abolishes normal function
```

### 2. `conf/oak_config.yaml`

Add entry for PATO:
```yaml
# Quality/modifier ontology
PATO: sqlite:obo:pato
```

### 3. `kb/disorders/Noonan_Syndrome.yaml`

In the "SHP2 Gain-of-Function Activation" node, add `modifier: GAIN_OF_FUNCTION` to the
molecular function descriptor (one line addition):

```yaml
molecular_functions:
- preferred_term: protein tyrosine phosphatase activity
  term:
    id: GO:0004725
    label: protein tyrosine phosphatase activity
  modifier: GAIN_OF_FUNCTION   # structured; previously only expressed in free-text node name
```

---

## Validation

After implementation, run:
```bash
just validate kb/disorders/Noonan_Syndrome.yaml
just validate-terms-file kb/disorders/Noonan_Syndrome.yaml
just validate-references kb/disorders/Noonan_Syndrome.yaml
just qc
```

No existing KB files should require changes — the new enum values are additive and the
`meaning:` bindings on existing values are non-breaking.

---

## Branch

```
feat/proposal-a-modifier-enum-pato
```
Worktree at `../dismech-proposal-a`.

---

## Follow-up Issues to Open

1. **Retroactive GOF/LOF migration** — bulk-update free-text GOF/LOF node names across KB
2. **DYSREGULATED binding** — revisit when a suitable ontology term is standardized
3. **GOF/LOF ontology binding** — track SO:0002053/SO:0002054 fit if dismech `modifier:` semantics evolve
