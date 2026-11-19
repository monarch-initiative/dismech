---
name: entry-naming
description: >
  Choose, review, or change the `name` of a dismech Disease entry. Use when
  creating an entry (including from a stub, whose `label` is the MONDO label),
  renaming one, or reviewing a PR that adds or renames one. Covers the scope
  rule (the name must not be broader than the entry), when a single-gene
  entry takes a gene-related (dyadic) name, where an established name can be
  found, umbrella names that must not be used for a single entry, casing, and
  when to report a MONDO label upstream. Not for choosing the `disease_term`
  binding itself; see dismech-terms and mapping-analysis.
---

# Naming a dismech entry

The rules are recorded in design decisions §18
(`docs/explanation/design-decisions.md`). This skill is the working procedure.

## The two rules

1. **The name has the same scope as the entry.** Ask: could a patient have the
   condition this name describes without the entry's defining cause? If yes,
   the name is too broad. An entry bound to a single-gene term but named
   after a phenotype (`Cryptorchidism`, `Trichotillomania`, `Normal Pressure
   Hydrocephalus`) fails this test, because each of those names also covers
   patients with other genes or with no genetic cause at all. Whether the fix
   is a rename or a rebind depends on what the entry is actually about (see
   the worked examples below).
2. **A single-gene Mendelian entry is named `<GENE>-Related <Phenotype>` when
   that name is established.** "Established" means at least one of:
   - the MONDO label, or a MONDO EXACT synonym, of the bound term
   - a ClinGen-preferred label (a MONDO synonym that MONDO attributes to
     ClinGen)
   - a GeneReviews chapter title for the same scope
     (`cache/bookshelf/genereviews.csv`)
   - the current OMIM title
   - recurring use in recent primary literature, cited in the entry's
     `notes` (add it to `synonyms`, too)

   This follows ClinGen's dyadic nomenclature (PMID:33417889,
   PMID:39241757). For a mechanism resource the gene is the root of the
   pathograph, so putting it in the name tells a reader where the graph
   starts.

## The MONDO label is an input, not the default

The `disease_term` binding fixes what disease the entry is. The `name` is
dismech's own. A stub's `label` is the MONDO label, and the stub filename and
claim issue title are built from it, so it is easy to carry it forward
unexamined. Treat it as one candidate among those above.

MONDO labels can be broader than their own class, out of date with OMIM, or
miscased. Some known cases are listed in monarch-initiative/mondo#10836. If
you choose a different name because of a problem with the MONDO label, say so
in the PR and either add the term to that issue or open a new MONDO issue (the
`mapping-analysis` skill covers upstream corrections).

## Procedure

1. **Is the entry single-gene?** Check the stub's `genes:` (or the bound MONDO
   term's `has_material_basis_in_germline_mutation_in`) and the entry's
   causative `genetic[]` rows. If it is not single-gene, only rule 1 applies.
2. **Apply the scope test to the current label.** If it fails, the name must
   change. Then decide which side is wrong: if the entry is really about the
   broad condition, the fix is a broader `disease_term` and a fuller
   `genetic` section, not a new name.
3. **Look for an established gene-related name**, in the order listed above.
   Prefer a candidate whose phenotype words match the entry's scope.
4. **Reject umbrella names for a single entry.** `POLG-Related Disorders`
   names a spectrum; Alpers-Huttenlocher syndrome is one point on it.
   Renaming the entry to the umbrella makes it broader, which breaks rule 1.
   An umbrella is a candidate for a `Grouping` or a parent entry with
   `has_subtypes`.
5. **Check that the phenotype half keeps the scope.** A gene-related name with
   a different phenotype word is often a different lumping. GeneReviews'
   `ATM-Related Cancer Predisposition` covers heterozygous carriers, not
   ataxia-telangiectasia.
6. **Keep the old names.** The MONDO label, eponyms and the OMIM title go into
   `synonyms`, so search and recognition still work.
7. **If nothing is established, keep a clear existing name.** Do not coin a
   gene-related name. An eponym or a numbered series name (`Spastic
   Paraplegia 81`) is specific, even if it is opaque. Prefer a dyad when one is
   established, but an opaque specific name is a smaller problem than a broad
   one.

## Form

- Title case, as for every entry: `ACTA1-Related Nemaline Myopathy`. The gene
  symbol keeps HGNC case, and `Related` is capitalised. The corpus mixes
  `-related` and `-Related`; new entries use `-Related`.
- No parenthetical qualifiers, as with subtype names. Put long forms in
  `synonyms`.
- Check casing against the source rather than copying it. MONDO has labels
  with a capitalised common word partway through.

## Worked examples

| Situation | Outcome |
|---|---|
| `Brachyphalangy-Polydactyly-Tibial Aplasia Syndrome`, bound to a term whose MONDO label is already `HMGB1-related ...` | Use the MONDO label's gene-related form |
| `Alpers-Huttenlocher Syndrome`, where the only gene-related title is `POLG-Related Disorders` | Keep the eponym; the umbrella belongs on a grouping |
| `Cystic Fibrosis` (CFTR) | Keep. The name is already specific to one gene |
| `Cryptorchidism`, bound to the INSL3 term | Scope test fails. Decide whether the entry is about INSL3 (rename) or about cryptorchidism generally (rebind) |
| `Protein S Deficiency`, covering PROS1-driven hereditary deficiency (AD and AR forms) | The name drops "hereditary", so it also covers acquired deficiency. Use `Hereditary Protein S Deficiency`; do not narrow it to the AD-only term, because the entry also covers the AR form |

## Renaming an existing entry

Changing `name` on its own is safe. Changing the file slug moves every
cross-file reference (`File:pathophysiology#...`, grouping members, comorbidity
entries) and needs a `history/` record with `superseded_by`. Until the project
decides how slugs follow renames (dismech#15894), change `name` and
`synonyms` and leave the filename alone.

## Reviewing

In a PR that adds or renames an entry, ask:
- Is the name as specific as the entry?
- If the PR mentions a more specific name used in the literature, has it been
  considered?
- Are the MONDO label and other prior names kept in `synonyms`?
