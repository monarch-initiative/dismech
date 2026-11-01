# bGSL Dictionary Suggestions from the dismech Glycan Biomarker Pilot

Release reviewed: bGSL 2026-10-08
(`releases/2026-10-08/bGSL_2026-10-08.tsv`, 973 rows, 909 not hidden).
Reviewed: 2026-10-27.

These suggestions come from matching bGSL against the dismech knowledge base
and its 72,519 cached publication abstracts and full texts, and from mapping
glycan biomarkers in eight disease entries (see the pilot section of
[`GLYGEN.md`](GLYGEN.md)). They are ordered by how much each would improve
bGSL as a text-mining and curation resource. Items marked *check* are
patterns that look wrong from the data alone and need a glycoscientist's
judgement.

## 1. Abbreviations and synonyms that collide with non-glycan usage

Exact-match text mining with these strings produces large numbers of false
positives in biomedical text. In the dismech publication cache, `LC3` alone
matched 392 documents, nearly all about the autophagy protein.

| bGSL term | Field | String | Collides with |
|---|---|---|---|
| Lc3 | abbreviations | LC3 | MAP1LC3 autophagy protein (LC3-I/LC3-II) |
| T antigen | abbreviations | TF | TF (transferrin) gene symbol; tissue factor |
| poly-sialic acid | abbreviations | PSA | prostate-specific antigen |
| ceramide trihexoside | exact_synonyms | CTH | CTH (cystathionine gamma-lyase) gene symbol |
| Cad antigen | exact_synonyms | CAD | CAD gene symbol; coronary artery disease |
| lipoteichoic acid | abbreviations | LTA | LTA (lymphotoxin alpha) gene symbol |
| blood group A type 1 | exact_synonyms | A type 1 | generic phrases such as "type 1" with a preceding "A" |

Suggestion: add an `ambiguous` flag (or a separate `ambiguous_abbreviations`
column) so text-mining consumers can require context, such as a co-occurring
glycan term, before accepting these matches. The existing `hidden` flag
withholds whole terms, not individual strings.

## 2. Synonym errors (*check*)

- **Lc3** lists *Glucocerebroside* and *glucoceramide* as exact synonyms.
  Glucocerebroside is glucosylceramide (GlcCer), a monohexosylceramide, not
  lactotriaosylceramide. These look misplaced; there is a separate
  `Glucosylceramide` term.
- **Gb3** lists *Globotriose* as an exact synonym. Globotriose is the free
  trisaccharide (Gal-α1,4-Gal-β1,4-Glc), not the ceramide-linked
  glycosphingolipid, so it is at most a related synonym.
- **Gb3** and **ceramide trihexoside** are separate terms. Ceramide
  trihexoside (CTH) is the older clinical name for Gb3 in Fabry disease, and
  the separate term carries no identifiers. Merging it into Gb3 as an exact
  synonym would let Fabry literature resolve to G00059MO.

## 3. GlyTouCan accessions shared across distinct structures (*check*)

83 GlyTouCan accessions are attached to more than one visible term. Many are
legitimate (a common name and its systematic name), but some join structures
that differ by a modification:

- `G00672PE` is listed for both **6'-sulfo-sialyl-Lewis x** (sulfate on Gal)
  and **6-sulfo-sialyl-Lewis x** (sulfate on GlcNAc).
- `G98544DH` and `G81928IQ` are listed for both **GD3** and
  **9-O-acetyl GD3**.

A per-term check that each accession's WURCS contains the defining
modification would catch these, building on the WURCS verification already
done for the 2026-10-08 release.

## 4. Missing ChEBI cross-references

ChEBI appears only inside the free-text `description` (83 rows), not as a
column, so it cannot be used for mapping without parsing prose. Terms where
ChEBI has a matching entry that bGSL does not record:

| bGSL term | ChEBI | ChEBI label |
|---|---|---|
| sialyl Lewis x | CHEBI:61711 | alpha-Neup5Ac-(2->3)-beta-D-Galp-(1->4)-[alpha-L-Fucp-(1->3)]-D-GlcpNAc (structure is in the description, CURIE is not) |
| Gb3 | CHEBI:18313 | alpha-D-galactosyl-(1->4)-beta-D-galactosyl-(1->4)-beta-D-glucosylceramide |
| GM3 | CHEBI:84118 | ganglioside GM3 |
| CA19-9 | CHEBI:62681 | already on the sialyl Lewis a term, not on CA19-9 |

For **Tn antigen**, bGSL's description cites CHEBI:40356
(N-acetyl-alpha-D-galactosamine), the free monosaccharide. ChEBI also has
the protein-linked form, CHEBI:53604
(O-(N-acetyl-alpha-D-galactosaminyl)-L-serine residue), which matches the
definition of the Tn antigen as GalNAc-α-O-Ser/Thr. dismech uses the
residue form for galactose-deficient IgA1.

Suggestion: add a `chebi_id` column (and, if planned, a `gno_id` column for
GNOme), multi-valued like `gtc_id`.

## 5. Missing names and spelling variants

Found by looking for the biomarkers named in dismech disease entries:

- **CA 19-9** (with a space) and **CA19.9**: only `CA19-9` is present, so the
  common clinical spelling does not match. **carbohydrate antigen 19-9** is
  present.
- **CD15s**: the cluster-of-differentiation name for sialyl Lewis x, used in
  flow-cytometry diagnosis of leukocyte adhesion deficiency type II.
- **sLeX** (capital X): the sialyl Lewis x abbreviations include `sLex` and
  `SLex` but not `sLeX`, which is common in the LAD-II literature. If matching
  is case-sensitive this misses it.
- **GL-3** (hyphenated): `GL3` is present; Fabry trial literature uses both.

## 6. Missing biomarker concepts

These are the glycan biomarkers dismech most needs to represent and could not
find in bGSL. Some are glycoconjugate measurements rather than free glycans,
so they may be outside bGSL's scope; if so, saying so in the README would
help consumers.

| Concept | Disease context |
|---|---|
| lyso-Gb3 (globotriaosylsphingosine) | Fabry disease; primary monitoring biomarker. Also absent from ChEBI |
| transferrin glycoforms (asialo-, monosialo-, disialotransferrin; carbohydrate-deficient transferrin) | first-line screen for congenital disorders of glycosylation |
| apolipoprotein C-III isoforms (apoCIII-0, -1, -2) | O-glycosylation screen in CDG |
| galactose-deficient IgA1 (Gd-IgA1) | IgA nephropathy |
| urinary free oligosaccharides | oligosaccharidoses (fucosidosis, mannosidoses, aspartylglucosaminuria) |

`Glc3Man9GlcNAc2` is present but carries no GlyTouCan, GSD or GlycoMotif
identifier, although it is the lipid-linked oligosaccharide whose truncation
defines several N-glycosylation CDGs.

## 7. GlyTouCan accessions outside GNOme

All 534 distinct GlyTouCan accessions in the release were looked up in GNOme
(V2.7.0, through the EBI Ontology Lookup Service). 508 resolve. The 26 that
do not are all polysaccharides or repeat-unit glycans, for example
acharan sulfate (G25575JK), chondroitin sulfate A, C and D, hyaluronan
(G29086KO), keratan sulfate (G82109MW), poly-N-acetylneuraminic acid
(G80631ZD), amylose (G05740LL), xyloglucan (G25326UC) and the plant
galactans, arabinans and pectins. This looks like GNOme coverage rather than
bad accessions. It does mean consumers that validate through GNOme cannot
check these terms, which a note in the README would make clear.

## 8. Release and format

- 485 of 909 visible terms carry no GlyTouCan, GSD or GlycoMotif identifier.
  A column stating why (no structure defined, a class term, not yet mapped)
  would distinguish class terms from mapping gaps.
- The README's field list is out of date: the TSV has `description` and
  `hidden` columns the README does not list, and the column order differs.
- `RELEASE_NOTES.md` names the file `bGSL_2026_10_08.tsv`; the file is
  `bGSL_2026-10-08.tsv`.
- Three rows carry character-encoding damage, including one term name:
  `Î±(2-6)sialylÂ_ lactotetraosylceramide`, plus text in the
  `chondroitin sulfate` and `Sialyllactotetraosylceramide` rows
  (for example `10‚Äî60 kDa`).
- For use as an ontology by tools such as dismech's term validator, a
  registered prefix with resolvable IRIs and an OBO or OWL export (with
  synonym scopes mapped to `oboInOwl` exact, broad, narrow and related
  synonyms) would let bGSL identifiers be validated like any other ontology
  term, and loaded into the EBI Ontology Lookup Service.

## Method

Matching was token-based and exact: each bGSL term, exact synonym (both at
least 5 characters, case-insensitive) and abbreviation (at least 3
characters, case-sensitive) was matched against tokenized text, excluding
rows with `hidden` set. Counts in this file come from that scan and from the
TSV itself; ChEBI terms and labels were read from the EBI Ontology Lookup
Service. GlyTouCan accessions were resolved as `GNO:` terms through the same
service.
