---
provider: codex
model: gpt-5
harness: dismech abandoned-PR consolidation and literature reconciliation
cached: false
generated: '2026-08-07T23:20:00Z'
template_variables:
  disease_name: Triple A Syndrome
  mondo_id: MONDO:0009279
  category: Mendelian
  gene: AAAS (hgnc:13666)
  inheritance: autosomal recessive
verification:
  duplicate_prs_reconciled: 5
  primary_sources_fetched: 7
  evidence_snippets_verified: true
note: >-
  This artifact records the completeness and conflict-reconciliation pass used
  to consolidate PRs #5856, #6055, #6134, #6477, and #6490. Claims imported
  into the KB entry are supported by exact snippets in generated reference
  caches. It is a focused deep-research audit of the sources already surfaced
  by those five independent curation attempts, not permission to import any
  uncached claim.
---

# Triple A Syndrome — consolidated literature audit

## Scope and ontology anchor

Triple A syndrome (Allgrove syndrome) is anchored to `MONDO:0009279` and to
biallelic loss-of-function variation in `AAAS` (`hgnc:13666`), encoding the
nuclear-pore protein ALADIN. The five duplicate PRs agreed on the disease
identity, inheritance, defining clinical triad, and proximal molecular lesion.
The final model treats it as a nucleoporin/neuroendocrine disorder rather than
an inborn error of intermediary metabolism.

## Verified source set

| Reference | Role in the final model |
|---|---|
| PMID:11062474 | AAAS discovery, defining triad, autonomic and neurological spectrum |
| PMID:12730363 | ALADIN nuclear-pore localization and mutant cytoplasmic mislocalization |
| PMID:16467144 | Selective nuclear import failure, impaired repair, oxidative-stress sensitivity |
| PMID:20687490 | Rarity, optic atrophy/amyotrophy, and organ-directed management |
| PMID:25554662 | Clinical hyperpigmentation |
| PMID:36194344 | Cohort evidence for dysautonomia and palmoplantar hyperkeratosis |
| PMID:42415167 | Contemporary case, biallelic AAAS confirmation, Schirmer testing, replacement therapy, myotomy/dilation |

The authoritative evidence inventory is the entry itself and its generated
caches.

## Reconciliation findings

### Clinical completeness

The final phenotype set includes the classic triad of achalasia, alacrima, and
ACTH-resistant primary adrenal insufficiency; dysphagia; central, peripheral,
and autonomic neurological involvement; optic atrophy; amyotrophy; cutaneous
hyperpigmentation; and palmoplantar keratoderma. Frequency is asserted only
where a numeric cohort observation supports an ontology band.

### Mechanism

The final pathograph preserves the best-supported causal sequence shared across
the drafts: pathogenic `AAAS` variation and ALADIN mistargeting at the nuclear
pore lead to selective nuclear-import failure, impaired delivery of DNA-repair
factors, oxidative-stress hypersensitivity, tissue-selective degeneration, and
adrenocortical failure. In-vitro molecular experiments remain tagged
`IN_VITRO`; patient manifestations and treatment observations remain
`HUMAN_CLINICAL`.

### Diagnosis and management

The consolidated entry structures Schirmer testing and molecular confirmation
instead of leaving diagnosis solely in prose. Management is separated into
hydrocortisone and fludrocortisone replacement, Heller myotomy, endoscopic
dilation, and artificial tears, with current NCIT procedure bindings and
therapeutic agents where supported.

### Prevalence discipline

The literature consistently calls the disorder rare but does not provide a
robust denominator-based worldwide estimate in the fetched sources. The final
entry therefore records a qualitative `RARE` class with `measure_type:
UNKNOWN`; it does not convert case counts or founder observations into an
unsupported numeric prevalence.

## Excluded or deferred claims

- Antioxidants and N-acetylcysteine remain mechanistic or in-vitro leads, not
  established clinical therapies.
- No precise phenotype frequency is inferred from words such as “common.”
- No numeric worldwide prevalence rate is fabricated.
- Additional esophageal physiology tests may be curated when an exact,
  procedure-specific source is fetched.

## Completeness conclusion

The five drafts were complementary: one had the strongest atomic mechanism,
one the broadest phenotype coverage, and others supplied diagnosis, treatment,
and review corrections. Their useful content is now represented once in the
canonical YAML. Incremental histories, stale enum snapshots, and duplicate
reference caches are not part of the consolidated change.
