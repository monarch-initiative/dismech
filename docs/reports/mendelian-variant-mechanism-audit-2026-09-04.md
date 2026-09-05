# Mendelian entries without a structured variant mechanism (2026-09-04)

Audit of every `kb/disorders/` entry that is Mendelian (a disease-level `inheritance`
block bound to a single-locus HPO mode plus a `genetic` record with
`relationship_type: CAUSATIVE`, and no `SOMATIC_DRIVER`) but records no
`GeneticContext.functional_impact_category` anywhere in the file. The category is the
one queryable statement of *what the variant does to the gene product* (loss of function,
gain of function, dominant negative, hypomorphic); without it the mechanism survives only
as prose in a node description.

The census is regenerable:

```bash
just variant-mechanism-audit                                   # summary
just variant-mechanism-audit --format list --single-gene --with-cached-hits
just variant-mechanism-audit --format tsv --out /tmp/gap.tsv
```

## Census

| Population | Entries |
|---|---:|
| Disorder entries scanned | 2,612 |
| Mendelian (inheritance + CAUSATIVE gene, no somatic driver) | 871 |
| … already carrying `functional_impact_category` | 225 |
| … **without one (the gap)** | **646** |
| gap with exactly one causal gene | 511 |
| gap whose own prose already names a mechanism term | 558 |
| gap with a quotable mechanism sentence already in a cited cached reference | 516 |

By mode: AR 327, AD 206, AD/AR 46, X-linked (all forms) 40, mitochondrial 5, mixed the
rest. Categories in use across the KB after this tranche: `LOSS_OF_FUNCTION` 167,
`PARTIAL_LOSS_OF_FUNCTION` 42, `GAIN_OF_FUNCTION` 37, `DOMINANT_NEGATIVE` 27, `UNKNOWN` 11,
`HYPERMORPHIC` 5, `NEOMORPHIC` 2.

The gap is large but cheap to work: for four entries in five the mechanism is already
stated in the entry's own text, and for four in five a sentence that will verify as an
exact-quote snippet is already in `references_cache/`. The work is judgement, not
research — deciding which category the literature actually supports and quoting the
sentence that says so.

## Tranche curated in this pass (26 entries, 27 contexts)

Each entry gained a `genetic_context` block on its variant-level pathophysiology node
(gene, allele origin, zygosity, category, and a description saying why that category and
not its neighbour), plus one or two evidence items quoting the classifying sentence.
References newly fetched for this tranche: PMID:10441323, PMID:23585475, PMID:24318194,
PMID:32234571.

| Entry | Gene | Mode | Category | Key evidence |
|---|---|---|---|---|
| Bachmann-Bupp Syndrome | ODC1 | AD, de novo | GAIN_OF_FUNCTION | PMID:30475435 |
| Bosch-Boonstra-Schaaf Optic Atrophy Syndrome | NR2F1 | AD | LOSS_OF_FUNCTION (DN component described) | PMID:35455940 |
| Brachydactyly Type B1 | ROR2 | AD | GAIN_OF_FUNCTION | PMID:10700182, PMID:10986040 |
| Brachydactyly Type C | GDF5 | AD | LOSS_OF_FUNCTION | PMID:12357473 |
| BRPF1-Related Intellectual Disability | BRPF1 | AD | LOSS_OF_FUNCTION | PMID:31020800 |
| CAPN5-Related Vitreoretinopathy | CAPN5 | AD | GAIN_OF_FUNCTION | PMID:23055945 |
| CHD8-Related NDD with Overgrowth | CHD8 | AD, de novo | LOSS_OF_FUNCTION | PMID:25257502 |
| Chung-Jansen Syndrome | PHIP | AD | LOSS_OF_FUNCTION | PMID:29209020 |
| CLCN2-Related Leukoencephalopathy | CLCN2 | AR | LOSS_OF_FUNCTION | PMID:23707145 |
| Congenital Heart Defects and Skeletal Malformations Syndrome | ABL1 | AD | GAIN_OF_FUNCTION | PMID:33075386, PMID:33223528 |
| CTNNB1 Neurodevelopmental Disorder | CTNNB1 | AD, de novo | LOSS_OF_FUNCTION | PMID:24614104 |
| Darier Disease | ATP2A2 | AD | LOSS_OF_FUNCTION | PMID:10441323 |
| Aneurysm-Osteoarthritis Syndrome | SMAD3 | AD | LOSS_OF_FUNCTION | PMID:23585475 |
| GNAO1-Related DEE | GNAO1 | AD, de novo | LOSS_OF_FUNCTION (epilepsy alleles) | PMID:29758257, PMID:28747448 |
| GNE Myopathy | GNE | AR | PARTIAL_LOSS_OF_FUNCTION | PMID:41082181 |
| GRIN2A-Related EE/ID — TMD/linker missense node | GRIN2A | AD | GAIN_OF_FUNCTION | PMID:30544257 |
| GRIN2A-Related EE/ID — null/ATD/LBD node | GRIN2A | AD | LOSS_OF_FUNCTION | PMID:30544257 |
| Holoprosencephaly 9 | GLI2 | AD | LOSS_OF_FUNCTION | PMID:14581620 |
| Hypertrophic Cardiomyopathy 4 | MYBPC3 | AD/AR | LOSS_OF_FUNCTION (not DN) | PMID:19574547 |
| Immunodeficiency 14B | PIK3CD | AR | LOSS_OF_FUNCTION | PMID:41026257 |
| Immunodeficiency 63 | IL2RB | AR | PARTIAL_LOSS_OF_FUNCTION | PMID:31040184 |
| IPEX Syndrome | FOXP3 | XLR | LOSS_OF_FUNCTION | PMID:32234571 |
| KCNQ2 DEE | KCNQ2 | AD, de novo | DOMINANT_NEGATIVE | PMID:24318194 |
| Luscan-Lumish Syndrome | SETD2 | AD | LOSS_OF_FUNCTION | PMID:37025455 |
| Rienhoff Syndrome | TGFB3 | AD | PARTIAL_LOSS_OF_FUNCTION | PMID:23824657 |
| SOCS1 Haploinsufficiency | SOCS1 | AD | LOSS_OF_FUNCTION | PMID:33087723 |
| White-Sutton Syndrome | POGZ | AD, de novo | LOSS_OF_FUNCTION | PMID:31782611 |

Conventions used, which later tranches should keep:

- **The category goes on the variant-level node**, the one whose `genes:` names the
  causal gene, not on every downstream node. `GRIN2A` shows the pattern when one entry
  has two allele classes with opposite effects: two nodes, two contexts.
- **The category is a claim and takes its own evidence item**, quoting the sentence that
  classifies the mechanism, not the sentence that names the gene. A gene-discovery
  abstract that only says "mutations in X cause Y" does not support a category.
- **Say why not the neighbour.** `LOSS_OF_FUNCTION` vs `DOMINANT_NEGATIVE` (MYBPC3,
  KCNQ2), `LOSS_OF_FUNCTION` vs `PARTIAL_LOSS_OF_FUNCTION` (IL2RB, TGFB3, GNE),
  `GAIN_OF_FUNCTION` vs haploinsufficiency (CAPN5, ROR2). The `description` on the
  context records the discrimination so a reviewer does not have to rederive it.
- **A disease with allele classes of opposite sign gets the category of the presentation
  the entry covers**, with the other class named in the description (GNAO1: LOF for the
  epileptic encephalopathy, GOF alleles noted as the movement-disorder class).
- **Evidence grade follows the cited paper, not the claim.** Where a sentence was already
  quoted elsewhere in the same file, the new item keeps that grade
  (`check-snippet-grading` is keyed on the sentence).

## Contested mechanisms: recorded, not skipped

Five entries had a mechanism sentence in cache but the literature disagrees on which
category it supports. Leaving the slot empty would make them indistinguishable from the
hundreds of entries nobody has looked at yet, so each is now recorded structurally in
three linked places:

1. **`functional_impact_category: UNKNOWN`** on the variant-level node, with a
   `description` naming both readings and pointing at the discussion. `UNKNOWN` here
   means *assessed and contested*, not *unassessed* — the description carries that
   distinction, and the audit's category breakdown makes it countable.
2. **Competing `mechanistic_hypotheses` entries**, one per position, each with its own
   `status` and its own evidence quoting the sentence that states that position.
3. **A `CONTROVERSY` (or, where the entry already framed it that way, `KNOWLEDGE_GAP`)
   discussion** attached to the node *and* to both hypotheses, carrying a
   `proposed_experiments` entry with the discriminating experiment, its
   `decision_criterion`, and `would_support` / `would_refute` pointing back at the
   hypotheses.

| Entry | Gene | Competing hypotheses | Discussion |
|---|---|---|---|
| Weaver Syndrome | EZH2 | `loss_of_function_prc2` (CANONICAL) vs `dominant_negative_prc2` (EMERGING) | `weaver_ezh2_variant_mechanism_controversy` (CONTROVERSY, new) |
| Bainbridge-Ropers Syndrome | ASXL3 | `asxl3_nmd_haploinsufficiency` (CANONICAL) vs `asxl3_nmd_escaping_truncated_protein` (ALTERNATIVE), both new | `brps_truncated_protein_mechanism_controversy` (CONTROVERSY, new) |
| Bohring-Opitz Syndrome | ASXL1 | `asxl1_loss_of_full_length_function` (CANONICAL) vs `asxl1_truncated_protein_dominant_or_gain` (ALTERNATIVE), both new | existing `bos_truncation_molecular_consequence`, extended with the hypothesis links and an experiment |
| Arboleda-Tham Syndrome | KAT6A | existing `early_truncating_nmd_haploinsufficiency` (CANONICAL) vs `late_truncating_nmd_escape` (ALTERNATIVE) | `kat6a_truncation_position_mechanism_controversy` (CONTROVERSY, new) |
| ADNP-Related Syndrome | ADNP | existing `allele_specific_haploinsufficiency_branch` (CANONICAL) vs `nmd_escape_truncation_branch` (ALTERNATIVE) | existing `gap_adnp_allele_specific_molecular_mechanism`, extended to attach the node and both hypotheses |

Two of the five (ADNP, Arboleda-Tham) already had the competing hypotheses curated and
needed only the category and the links; Bainbridge-Ropers and Bohring-Opitz needed the
hypotheses written. In every case the discriminating experiment is the same shape,
because the disagreement is the same one: **an isogenic comparison of the disease allele
against a heterozygous null in one genetic background**, which no published study has
run for any of these genes. Where the allele class is truncating, the experiment is
preceded by a protein-detection step, since "does the truncated protein exist in patient
cells" is unanswered for ASXL1, ASXL3 and KAT6A alike.

`KCNQ2` is worth keeping in view as a trap rather than a controversy: the *same gene* is
haploinsufficient in benign familial neonatal seizures and dominant-negative in the
developmental and epileptic encephalopathy, so a category must never be copied from one
entry to the other. The DEE entry is curated as `DOMINANT_NEGATIVE` in this branch; no
BFNS entry exists yet.

## Can a deep-research provider resolve these?

Partly, and the limit is worth stating precisely. The repository already has the
plumbing: `just research-hypothesis <provider> <disorder> <hypothesis_group_id>` runs a
focused hypothesis search whose template asks, among other things, for competing
mechanistic hypotheses, explicit knowledge gaps, and the experiments that would
distinguish them, and writes to
`kb/hypotheses/<Disorder>/<hypothesis_group_id>/<provider>.md`.

```bash
just research-hypothesis openscientist Weaver_Syndrome dominant_negative_prc2
just research-hypothesis openscientist Bainbridge-Ropers_Syndrome asxl3_nmd_escaping_truncated_protein
just research-hypothesis openscientist Bohring-Opitz_syndrome asxl1_truncated_protein_dominant_or_gain
just research-hypothesis openscientist Arboleda-Tham_Syndrome late_truncating_nmd_escape
just research-hypothesis openscientist ADNP-Related_Syndrome nmd_escape_truncation_branch
```

The hypothesis blocks added above are what make these runnable: the runner seeds the
provider with the hypothesis YAML, so a controversy that exists only as prose in a node
description cannot be searched, while one curated as two competing hypotheses can.

What a provider run can realistically deliver here is **completeness of the evidence
matrix** — a functional study this audit's cache-first method missed, a preprint, a
cohort that stratified by allele class — and a sharper statement of the discriminating
experiment. What it cannot deliver is the experiment itself. Every one of these five
controversies is open because a specific comparison has not been performed, not because
the literature is hard to find; a search that returns the same two positions more
thoroughly does not move the category off `UNKNOWN`.

So the runs are worth doing as evidence sweeps, and their output is a lead, not curated
content: a report lands under `kb/hypotheses/`, is assessed with the
`review-hypothesis-exploration` skill into an assessment sidecar, and only claims that
survive that review reach the disease YAML. See
[Hypothesis Report Assessments](../hypothesis-report-assessments.md).

## Worklist for the next tranches

Ranked by how many of the entry's cited cached references already contain a mechanism
sentence (`just variant-mechanism-audit --format list --single-gene --with-cached-hits`).
Top of the list at the time of writing:

| Entry | Gene | Mode | Prose signals | Cached refs with a mechanism sentence |
|---|---|---|---|---:|
| MED13L Syndrome | MED13L | AD | lof, dn, hi | 19 |
| SETD5 Haploinsufficiency Syndrome | SETD5 | AD | lof, hi | 15 |
| USP9X Female-Restricted Syndromic ID | USP9X | XL | lof, gof, dn, hi, hypo | 15 |
| Acromesomelic Dysplasia Maroteaux Type | NPR2 | AR | lof, gof, dn, hi | 13 |
| FOXP1 Syndrome | FOXP1 | AD | lof, hi | 13 |
| Raine Syndrome | FAM20C | AR | lof, hypo | 12 |
| MICPCH Syndrome | CASK | XL | lof, hypo | 11 |
| CSF1R-related Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis | CSF1R | AR | lof, hi, hypo | 10 |
| Loeys-Dietz Syndrome 4 | TGFB2 | AD | lof, dn, hi | 10 |
| Chuvash Polycythemia | VHL p.Arg200Trp | AR | hypo | 9 |
| Giant Axonal Neuropathy 1 | GAN | AR | lof | 9 |
| Lymphatic Malformation 6 | PIEZO1 | AR | lof, gof, hypo | 9 |
| NGLY1-Congenital Disorder of Deglycosylation | NGLY1 | AR | lof | 9 |
| SHORT Syndrome | PIK3R1 | AD | dn, hi, hypo | 9 |
| KCNH1-Associated Disorder | KCNH1 | AD | gof, hi | 8 |
| MBD5 Haploinsufficiency Syndrome | MBD5 | AD | lof, hi, hypo | 8 |
| SCN2A-Related DEE | SCN2A | AD | lof, gof | 8 |
| Primary Erythermalgia | SCN9A | AD | gof | 7 |
| Snyder-Robinson Syndrome | SMS | XLR | lof, hypo | 8 |

Entries whose prose lists several signals (`lof, gof, dn, hi`) are usually reviews of
the whole gene's allelic series rather than a confused entry; read the node before
assigning. Entries with a single signal and a single gene (Giant Axonal Neuropathy,
NGLY1, Primary Erythermalgia, SETD5, FOXP1) are the fastest wins.

## Method notes

- The mechanism sentence was taken from the entry's own cited references where one
  existed, so the new evidence item verifies against a cache file already committed. Four
  entries (Darier, KCNQ2 DEE, IPEX, Aneurysm-Osteoarthritis) had no such sentence and
  received one newly fetched reference each; each was chosen for stating the human
  mechanism in its abstract, not for being the gene-discovery paper.
- `variant_origin: DE_NOVO` was recorded only where the entry's own inheritance block says
  the disorder is typically de novo; otherwise `GERMLINE`. `zygosity` was omitted for the
  two recessive entries whose allelic series mixes homozygous and compound-heterozygous
  genotypes (GNE, CLCN2) rather than picking one.
- Validation per entry: `linkml-validate`, the reference snippet audit (2,193 of 2,205
  snippets across the 26 files verified, the remainder skipped by non-PMID prefix), term
  validation, and the snippet-grading, snippet-length, title-snippet, folded-hyphen,
  enum, duplicate-key, entity-ref, causal-target and qualifier-term gates.
