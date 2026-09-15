# GeneReviews and StatPearls Baseline Check

`just check-genereviews` answers, offline, the first question the review skill's
item 15 asks of a new Mendelian entry: **does a GeneReviews chapter exist for
this disease, and is it tagged?** It also reports the same for StatPearls, which
is a different kind of source (below), and it is deliberately only
*semi*-deterministic.

## Why it exists

The review skill used to answer "does a chapter exist" with a `curl` to PubMed.
The automated PR reviewer runs in a sandbox that permits `just` and `uv run` and
blocks every network tool, so on [PR #11592](https://github.com/monarch-initiative/dismech/pull/11592)
it recorded, in two consecutive reviews, that it could not verify the entry's
"no GeneReviews chapter exists for isolated Dandy-Walker malformation" note, and
the curator had to prove the negative by hand in a comment. The question is
answerable from data the repository can carry.

## How it works

PubMed indexes both collections as *books*, so the `[book]` search field selects
every chapter exactly:

```
genereviews[book]   ->   958 chapters
statpearls[book]    -> 9,646 chapters       (snapshot 2026-09-10)
```

`just refresh-bookshelf-index` pulls those lists plus each record's title, `NBK`
accession and date into `cache/bookshelf/genereviews.csv` and
`cache/bookshelf/statpearls.csv`, with the snapshot date in
`cache/bookshelf/MANIFEST.yaml`. Rows are sorted by PMID and carry no per-row
timestamps, so the diff after a refresh is exactly the chapters that appeared,
retired, or were renamed. The check then compares each entry against that index.

Two of its answers are deterministic and one is a judgement, and the report keeps
them apart:

| Verdict | Meaning | Gates? |
|---|---|---|
| `MISTAGGED` | a reference tagged `GeneReviews` (or `StatPearls`) is not a chapter of that collection | GeneReviews only |
| `CITED_UNTAGGED` | a chapter PMID or `NBK` URL is cited somewhere in the file but not tagged in `references:` | GeneReviews only |
| `UNTAGGED_CHAPTER` | a chapter whose title, normalised, **equals** one of the entry's names exists and is not tagged | GeneReviews only |
| `TAGGED` | at least one tagged reference is a verified chapter | no |
| `CANDIDATE_CHAPTER` | only partial title matches, or only a retired chapter | no, by design |
| `NO_CHAPTER` | nothing in the snapshot names this entry | no |

Names compared are the entry `name`, its `synonyms`, and the `disease_term`
preferred term and ontology label. Normalisation drops case, diacritics,
punctuation and hyphens, a leading `<GENE>-Related`, and a trailing `Overview`,
so `Aicardi-Goutieres Syndrome` finds *Aicardi-Goutières Syndrome* and `Marfan
Syndrome` finds *FBN1-Related Marfan Syndrome* as `EXACT`.

`CANDIDATE_CHAPTER` is the judgement half. `Alpha Thalassemia` sits inside
*Alpha-Thalassemia X-Linked Intellectual Disability Syndrome* and is not that
disease's chapter; `Autosomal Dominant Robinow Syndrome 1` sits under *Autosomal
Dominant Robinow Syndrome* and is. The check lists the title and the match kind
(`CONTAINS`, `TITLE_IN_NAME`, `NEAR`) and leaves the call to a reader. Two guards
keep this list short: a numbered title never stands in for a differently numbered
name (*Usher Syndrome Type I* is not a candidate for `Usher Syndrome Type 4`),
and two `<GENE>-Related …` forms must name the same gene.

Gating is opt-in (`--strict`) and only ever on GeneReviews. A `TAGGED` entry
that also has an untagged candidate is reported, not failed.

```bash
just check-genereviews kb/disorders/Asthma.yaml     # one or more files
just check-genereviews                               # whole KB, findings only
just check-genereviews --strict FILE                 # exit 1 on a GeneReviews gap
just check-genereviews --online FILE                 # also live PubMed title search
just check-genereviews --format tsv > census.tsv     # machine-readable census
```

`--online` adds a live `<name>[TI] AND genereviews[book]` search per name so a
chapter published after the snapshot is caught. It needs network and is not
what the reviewer runs; a tagged PMID missing from the snapshot is still
accepted when the cached record carries the Bookshelf citation form.

## What to do with a finding

- **`UNTAGGED_CHAPTER` / `CITED_UNTAGGED` (GeneReviews)**: fetch the chapter
  (`just fetch-reference PMID:<id>`), tag it in the top-level `references:`
  block (`just tag-references FILE` does this for a chapter cited by PMID; one
  cited only by its `NBK` URL is tagged by hand), then mine it as the review
  skill's item 15 describes. If the matched chapter is genuinely not this
  disease's, say so in `notes:`.
- **`MISTAGGED`**: the tag is wrong. Remove it, or replace the reference with
  the real chapter.
- **`CANDIDATE_CHAPTER`**: read the title. Either tag and mine it, or ignore it;
  the check will keep listing it, which is the intended behaviour for a
  judgement it cannot make.
- **StatPearls anything**: informational. See the next section.

## GeneReviews versus StatPearls

Both are NCBI Bookshelf collections with PubMed-indexed chapters, both are
fetched and cached by `just fetch-reference` like any PMID, and both are easy to
mistake for each other in a deep-research report's "NCBI Bookshelf" citation.
They are not the same kind of source.

| | GeneReviews | StatPearls |
|---|---|---|
| Scope | Mendelian and heritable disease | all of clinical medicine |
| Size | ~960 chapters | ~9,600 chapters |
| Authorship | invited domain experts | volunteer clinicians |
| Review | peer-reviewed; scheduled comprehensive revisions | light editorial review; continuing-education framing |
| Structure | fixed clinical sections (Clinical Characteristics, Diagnosis/Testing, Management, Genetic Counseling), each quotable from the PubMed abstract | free narrative plus a "Continuing Education Activity" summary |
| Role here | **mandatory phenotype baseline** for a Mendelian entry (review skill item 15) | citable orientation source; **never a baseline**, and its absence is never a gap |

So for Dandy-Walker malformation the check reports `GeneReviews NO_CHAPTER` and
`StatPearls UNTAGGED_CHAPTER` (PMID:30855785, *Dandy-Walker Malformation*). The
first closes the reviewer's open item; the second says a StatPearls chapter
exists that the entry could cite for orientation, and nothing more. The
`StatPearls` value of `ReferenceTagEnum` exists so that a cited chapter can be
tagged and the KB queried for it, not to make it a requirement.

## Tagging is now index-driven

`just tag-references` decides whether a cited PMID is a chapter by looking it up
in the index, falling back to the Bookshelf citation form in the cached record
(`In: GeneReviews(®) [Internet]`, `In: StatPearls [Internet]`) for a chapter newer
than the snapshot. It used to grep the cached abstract for the bare word
"GeneReviews", which also matches a journal article that cites GeneReviews in its
reference list. It tags both collections.

## Staleness

The index is a snapshot and is refreshed by hand, like `cache/<prefix>/hierarchy.csv`.
A chapter published after the snapshot is missed until the next refresh; the
snapshot date is printed in every summary line so a reader can see how old the
answer is. Nothing gates on the index being current.
