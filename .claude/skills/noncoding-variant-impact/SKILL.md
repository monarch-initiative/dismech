---
name: noncoding-variant-impact
description: >-
  Curate or review noncoding variant impact in dismech, including regulatory
  SNVs and structural variants. Separate physical alteration, sequence overlap,
  regulatory target, expression consequence, and mechanistic confidence.
---

# Curating noncoding variant impact

Use the existing fields in [the schema](../../../src/dismech/schema/dismech.yaml).
Keep classifications small and optional; preserve evidence-specific detail in
descriptions. A noncoding location alone does not establish a regulatory mechanism.
Splicing, RNA stability, translation, and noncoding-RNA defects may require
different causal steps.
An SV can also overlap coding genes while acting primarily through regulation.

## Keep the claims separate

| Claim | Where to record it |
|---|---|
| Physical alteration | `Variant.variant_type`; initiating node's `genetic_context.variant_type` |
| Sequence features overlapped | `genomic_contexts` on either of those objects |
| Gene whose expression is affected or proposed to be affected | `Variant.regulatory_target_gene`; gene annotation on the downstream expression node |
| Element and direct molecular effect | `functional_effects[].regulatory_element_type`, `regulatory_mechanism`, and `description` |
| Expression pattern | `regulatory_category` on `Variant`, `FunctionalEffect`, or `Pathophysiology`, when supported |
| Quantitative process change | Biological-process descriptor `modifier: INCREASED` or `DECREASED` |
| Downstream consequences | Separate, evidence-backed pathophysiology nodes and causal edges |

`variant_type` and `genomic_contexts` use human-readable **static enum values**,
such as `deletion`, `single nucleotide variant`, `intron`, or `"5' UTR"`.
The Sequence Ontology mappings live in the schema; do not add ID/label pairs
to these fields. Gene and process annotations still use their normal descriptors.

Contexts can overlap and depend on the transcript. Identify the relevant
genes/transcripts in `description`; an intronic host gene may differ from the
regulatory target. Prefer the appropriate UTR context when the overlap is known
to be untranslated sequence of a protein-coding transcript, including a wholly
untranslated exon such as APC exon 1B. Use `noncoding exon` for an entire exon
without codons when no more specific UTR context applies. Omit unknown contexts.
Only put contexts shared by the represented alleles on a shared initiating node.
These classifications neither identify an enhancer nor encode genomic coordinates.

`regulatory_target_gene` does not assert sequence overlap or prove causality.
When a variant overlaps the gene and affects its regulation, both `gene` and
`regulatory_target_gene` may be appropriate. For an intact target, avoid putting
that gene on the physical lesion node as though its sequence were disrupted.

Keep legacy `type` and `allele_type` valid alongside the controlled fields;
do not migrate unrelated entries or require both representations. Rendering and
exports prefer `variant_type` while retaining distinct legacy detail. For a
complex alteration outside the enum, retain free text rather than forcing a class.

## Classify expression effects conservatively

| Category | Meaning in the current schema |
|---|---|
| `LOE` | Reduced or absent expression across all normally expressing cell types |
| `mLOE` | Reduced or absent expression in a subset of cell types or developmental windows |
| `GOE` | Ectopic spatial or temporal expression |

Increased expression in normally expressing cells is not sufficient for `GOE`.
Use gene-expression `modifier: INCREASED` or `DECREASED` for measured abundance
changes. A reduction in one assayed tissue may leave `LOE` versus `mLOE` unresolved;
leave the category unset and describe that limit. The enum's coding `LOF`, `GOF`,
and `DN` values do not substitute for expression effects. Use
`genetic_context.functional_impact_category` for a supported variant functional
consequence, independently of the expression-pattern classification.

Classification and confidence are independent. For example,
`regulatory_category: GOE` with `mechanism_confidence: HYPOTHETICAL` on an
expression node represents proposed ectopic expression; omitted confidence defaults
to established. `Variant` has no mechanism-confidence slot: qualify uncertain effects in its descriptions and
evidence rather than copying a hypothetical node's category as an established fact.

## Build the causal account from the evidence

Separate the physical variant, altered regulatory interaction, expression change,
and downstream disease mechanism into atomic nodes where supported. Classify the
initiating node through `genetic_context`; separate deletion and inversion triggers
when their classes or overlaps differ. Distinguish loss of silencer DNA from loss
of silencer contact or control when the element remains present.

Record assayed tissue, cell type, developmental stage, and experimental system.
Expression measurements do not by themselves establish altered transcription;
RNA stability may also explain them. Computational contact predictions and
cross-species assays need their own evidence grading, distinct from patient
measurements. Normal expression in blood does not automatically refute a
tissue-specific mechanism. Preserve possible contributions from other genes in
a multigene SV rather than attributing every phenotype to the regulatory target.

For individual alleles, retain the reported genome build and coordinate precision
in the description: array probe bounds are not nucleotide-resolved breakpoints.
Use [dismech-references](../dismech-references/SKILL.md) for source verification and
exact snippets, and [dismech-terms](../dismech-terms/SKILL.md) for ontology bindings.
`FunctionalEffect` has no evidence slot; support its claims on the variant and
the corresponding mechanism nodes. Follow the normal curation history and
validation workflow in `CLAUDE.md`.
