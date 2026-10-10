---
name: somatic-mosaicism
description: >
  Encode a post-zygotic (somatic mosaic) origin in a dismech Disease entry so
  the mosaic architecture is queryable. Use when curating an obligate-mosaic
  disorder (Proteus, CLOVES, Sturge-Weber, hemimegalencephaly, VEXAS, PNH), a
  germline disorder with a recognized mosaic arm (tuberous sclerosis, the MOGHE
  arm of SLC35A2-CDG), or when deciding whether HP:0001442 is the right term for
  a mosaic observation. Covers the inheritance block, variant_origin, the tiers
  the Somatic_Mosaic_Disorders grouping admits, and the cases that must not be
  bound.
---

# Somatic Mosaicism

A disorder whose causal variant arose after fertilization is encoded through
its mode of inheritance, the way a digenic one is, so the set can be recovered
by query. Before this convention the flagship entries said the same thing four
ways (an HP term, a block bound to `Sporadic`, a free-text "Not applicable"
block, prose only) and none of them could be found.

## The convention

1. Add an `inheritance` block whose `inheritance_term` is **bound** to
   `HP:0001442` *Typified by somatic mosaicism*, with its own snippet-backed
   evidence. The usual quote is the paired lesion-versus-blood sequencing
   sentence or a tissue-restricted allele-fraction sentence.
2. Set `variant_origin: SOMATIC` on the causal `genetic:` row, or
   `GERMLINE_AND_SOMATIC` for a two-hit repressor. `DE_NOVO` is for a germline
   de novo variant present in every cell.
3. Keep `category` in the standard vocabulary (`Genetic`). Never `Mendelian`
   for an obligate-mosaic disorder, and never an ad hoc `Somatic mosaic`; the
   mosaic claim lives in the bound term.

`HP:0003745` *Sporadic* is not a substitute: it describes the pedigree, not the
mechanism.

Worked example: `VEXAS_Syndrome` (acquired clonal); `Sturge-Weber_Syndrome`
(congenital obligate mosaic); `Tuberous_Sclerosis_Complex` (mosaic arm beside
an autosomal dominant block).

## Two tiers, and what is not a tier

| Situation | Encode | Grouping member? |
|---|---|---|
| The disease **is** the mosaic (no germline form exists) | one HP:0001442 block | yes |
| A germline disease has a **recognized mosaic arm** described in the literature | a second HP:0001442 block beside the germline block; do not replace it | yes |
| One mosaic **proband** in a case report | bind HP:0001442 on that block if curated; it is a true observation | no |
| **Parental or gonadal** mosaicism explaining recurrence | bind HP:0001442 if curated; the child's disease is constitutional | no |
| **Functional** mosaicism from X inactivation | do **not** bind HP:0001442; free-text `preferred_term` and say why (`CHILD_Syndrome`) | no |
| Mosaic aneuploidy as a downstream **phenotype** of a germline gene (mosaic variegated aneuploidy) | ordinary germline inheritance | no |

The term names DNA-level post-zygotic mosaicism and is true in the first four
rows. Only the first two describe the disease's architecture, which is what
`kb/groupings/Somatic_Mosaic_Disorders.yaml` collects under a `NECESSARY`
`HAS_INHERITANCE` criterion. It is deliberately not
`NECESSARY_AND_SUFFICIENT`, unlike the digenic grouping, because rows three and
four are legitimate bindings that are not memberships; the evaluator would
otherwise report them as candidates on every run.

## Not yet modelled

There is no structured slot for variant allele fraction, affected tissue, or
clone timing. Put those values in `notes:` for now. The schema question is
tracked in `projects/COMMONFUND/SMAHT.md` and
`docs/todo/inheritance-enrichment.md`.

## Validate

```bash
just validate kb/disorders/<Entry>.yaml
just count-verified-snippets kb/disorders/<Entry>.yaml
just check-groupings --strict kb/groupings/Somatic_Mosaic_Disorders.yaml
```
