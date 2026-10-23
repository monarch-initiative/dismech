# OpenScientist report on `asxl1_truncated_protein_dominant_or_gain` — assessment narrative

Companion to `openscientist-assessment-by-claude-code.yaml`, which is authoritative.

## Why this run was commissioned

The Bohring-Opitz entry holds `functional_impact_category: UNKNOWN` because BOS alleles
are last-exon *ASXL1* truncations expected to escape nonsense-mediated decay, and whether
the resulting protein merely lacks full-length repressive function or acts dominantly is
unresolved. When I wrote the two competing hypotheses they carried a single evidence item
each, both drawn from one patient multi-omics study that does not discriminate between
them. The hypotheses were real but thinly evidenced.

## What the run supplied

**For the truncated-protein reading.** Two things the entry lacked. Truncated ASXL1 is
directly detected at protein level, by mass spectrometry and western blot, in cell lines
lacking intact ASXL1, and the authors read that as evidence the alleles are
dominant-negative or gain-of-function (PMID:26700326). Unlike the ASXL3 case, the
paralogue objection does not apply here: same gene, same terminal-exon allele class. The
context is myeloid rather than germline, which matters and which the promoted evidence
records. Separately, an expressed truncated fragment is *sufficient* to reproduce
neural-crest phenotypes in vitro and in ovo (PMID:31006630) — a developmental context
relevant to BOS, and a sufficiency claim rather than a correlation.

**For the loss-of-function reading.** The counterpart, and it is strong. Constitutive
*Asxl1* deletion in mouse produces anophthalmia, microcephaly, cleft palate and mandibular
malformation, overlapping the BOS spectrum and arising with no truncated protein present
(PMID:24218140); heterozygous animals show a haploinsufficient haematologic phenotype
(PMID:24255920). This plays the same role the whole-gene *EZH2* deletion played in the
Weaver run: it shows the null route reaches the phenotype, so detecting a truncated
protein does not by itself establish that the truncated protein causes the disease.

## What it did not do

It did not resolve the question, and it says so without being asked: no accessed source
demonstrates a stable endogenous truncated ASXL1 protein in germline BOS tissue. Its own
reading — that both mechanisms coexist and converge on the PR-DUB/Polycomb axis — is what
the entry already encodes by holding the category at `UNKNOWN` with two live hypotheses.
What changed is that both hypotheses are now evidenced rather than asserted.

The gnomAD analysis is the weakest part. ASXL1 is genuinely not loss-of-function
constrained, unlike ASXL3, KAT6A and ADNP, and the pLoF burden does concentrate in the
last-exon window. But reading that as a signature of somatic clonal fitness requires
separating germline nulls from age-related clonal haematopoiesis in a blood-derived
resource, which the report concedes it cannot do. Not promoted.

## Bundle quality and candour

The report is unusually careful about its own weaknesses: it labels a key BOS-fibroblast
source as an unrefereed preprint, and flags three snippets across two references as
normalization mismatches needing curator re-verification. That is the behaviour you want
from a lead-generating tool.

Against that, the bundle README lists a `MANIFEST.yaml`, a `code/` directory and an `env/`
directory, and none was delivered. The report's own analysis inventory anticipates this,
telling the curator to verify bundle presence and paths — good instinct, and necessary.
The data tables and both logs are present, so the analysis is `PARTIAL` rather than
`REPORTED_ONLY`.

## Disposition

Category stays `UNKNOWN`. Four references promoted across the two competing hypotheses,
each verified against its fetched record. Nothing promoted from the computational work.
