# GeneReviews baseline workflow

### Step 3b: GeneReviews Baseline (REQUIRED when applicable)

GeneReviews (https://www.ncbi.nlm.nih.gov/books/NBK1116/) is the authoritative
expert-curated clinical reference for Mendelian disorders. Before curating
phenotypes, you MUST check whether a GeneReviews article exists for the disease.
If one exists, it is the mandatory phenotype baseline — not just a convenient
source.

> **Scope:** This step applies primarily to **Mendelian (single-gene) disorders**.
> For complex, multifactorial, infectious, or cancer entries where GeneReviews
> coverage is unlikely, skip directly to Step 4 — the PubMed search below will
> confirm either way.

#### 1. Check for a GeneReviews chapter

Once the YAML carries its `name`, `synonyms` and `disease_term`, run the offline
check against the committed Bookshelf index (`--online` adds a live PubMed
title search when you have network, for chapters newer than the snapshot):

```bash
just check-genereviews --online kb/disorders/<Entry>.yaml
```

`UNTAGGED_CHAPTER` or `CITED_UNTAGGED` on the `GeneReviews` line names the
chapter (PMID and title); `CANDIDATE_CHAPTER` lists partial title matches for
you to read; `NO_CHAPTER` means none names the disease. The reviewer runs the
same check, so its verdict is what the review will see. The `StatPearls` line
is informational — a StatPearls chapter may be cited for orientation but is
never the baseline (see `docs/genereviews-baseline-check.md`).

Before the file exists, the same question can be put to PubMed directly with
the `[book]` field, which selects GeneReviews chapters exactly:

```bash
curl -sG "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" --data-urlencode "retmode=json" \
  --data-urlencode "term=<DISEASE_NAME>[TI] AND genereviews[book]"
```

#### 2. If a PMID is found, fetch and cache it

```bash
just fetch-reference PMID:XXXXXXXX
```

#### 3. Tag it in the top-level `references:` block

```yaml
references:
  - reference: PMID:XXXXXXXX
    title: "<GeneReviews article title>"
    tags:
      - GeneReviews
```

You can also run `just tag-references` after adding the PMID to inline
evidence items — the script detects GeneReviews PMIDs from the cached
abstract and writes the top-level tag automatically.

#### 4. Cross-reference Clinical Characteristics against your YAML

- Read the cached abstract at `references_cache/PMID_XXXXXXXX.md`
- Identify every phenotype, anomaly, and comorbidity listed in the
  Clinical Characteristics section of the abstract
- Compare against your YAML `phenotypes:` section
- Any GeneReviews-documented phenotype **absent** from your YAML must
  either be added (with an HPO term and evidence item quoting the
  GeneReviews abstract) or explicitly explained as out of scope

> **Note:** The cached abstract captures only the structured PubMed abstract,
> which is a condensed summary of the full GeneReviews chapter. The full
> *Clinical Characteristics* section in the chapter body often lists additional
> phenotypes not in the abstract. Cross-reference the deep-research artifact
> (from Step 3) for comprehensive coverage — treat the abstract as the minimum
> baseline, not the ceiling.

#### 5. Capture drug-safety warnings

GeneReviews often has an *Agents/Circumstances to Avoid* section.
If the abstract mentions any, add a note in the relevant treatment entry's
`description:` and include a GeneReviews evidence item quoting it exactly.

#### 6. Frequency mapping — prose → FrequencyEnum

GeneReviews uses narrative frequency language. Map to the enum as follows:

| GeneReviews phrase | FrequencyEnum | HPO range |
|---|---|---|
| "virtually all", "most individuals", ">80%" | `VERY_FREQUENT` | 80–100% |
| "many", "majority", "common", "~50%–79%", ">30%" | `FREQUENT` | 30–79% |
| "some", "occasional", "uncommon", "~5%–29%" | `OCCASIONAL` | 5–29% |
| "rare", "few", "<5%", "infrequently reported" | `VERY_RARE` | 1–4% |
| "isolated reports", "single case" | (omit frequency) | <1% |

When frequency is ambiguous, **omit `frequency:`** rather than guessing.

#### 7. No GeneReviews article? Document it

If no GeneReviews article exists for the disease, proceed to Step 4
without this baseline. No action needed — the absence itself is not a
problem. A one-line `notes:` sentence recording it is still worth writing,
and the reviewer's `just check-genereviews` run is what verifies it.

---
