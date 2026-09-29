# OpenScientist report on `nmd_escape_truncation_branch` — assessment narrative

Companion to `openscientist-assessment-by-claude-code.yaml`, which is authoritative.

## The finding

This screen found the negative result the entry had been describing as an absence of
evidence, which is the most consequential thing any of the five runs did.

The hypothesis has a premise and a question. The premise — that most pathogenic last-exon
truncating *ADNP* alleles escape nonsense-mediated decay and produce mutant transcript —
is confirmed, both by a computed allele census (150 of 165 truncating alleles predicted to
escape) and, more usefully, by direct detection of mutant *ADNP* mRNA in patient blood
(PMID:38926592). The mRNA detection was promoted; the census was not, being a live-database
snapshot from a partially auditable analysis.

The question is what the retained mutant protein does. The entry recorded that mutant
protein "has never been unambiguously demonstrated in patients" — phrasing that reads as
nobody having looked properly. The run surfaced a study that did look, systematically,
across patient-derived materials and multiple antibodies, and found no detectable mutant
ADNP protein, concluding degradation or absence. That is a materially stronger statement
than an absence of evidence, and it cuts against the branch the run was asked to explore.
Promoted as a `REFUTE` item, and the hypothesis description amended so it no longer
implies the question is merely unexamined.

The finding does not close the question. Absence of a western signal in the materials and
antibodies tested is not proof that no mutant protein exists in any relevant tissue, and
the same paper documents real difficulty obtaining specific signal even for wild-type
ADNP. The promoted evidence records that caveat.

## Where this sits across the five screens

Third of five to reach the same shape, after ASXL3 and KAT6A: the decay-escape branch is a
candidate modifier on a dosage-loss baseline, not a symmetric competitor. Here the route
is a failed protein hunt rather than cohort severity or population constraint. The
category stays `UNKNOWN` regardless, because none of this measures what the protein does
when it is present — only whether it can be found.

## Bundle quality

The provenance *reporting* is the best of the five. The environment is named to
package-version precision. A ClinGen API failure is reported rather than hidden: the gene
page returned HTTP 200 as a client-rendered shell while the JSON endpoints returned 404,
so the machine-readable dosage record was not retrieved, and the report flags this as a
curator lead. A figure that exists only in the executor sandbox is disclosed rather than
listed as delivered.

The bundle *delivery* is a different matter, and the assessment validator caught what
reading alone might not have. The README lists a `MANIFEST.yaml`, a `code/` directory and
a `logs/` directory; none was delivered. The missing logs matter: the report states its
PubMed queries are logged in the bundle, and they are not, so the four reported zero-hit
searches cannot be checked. That source is recorded `UNVERIFIABLE` rather than `ACCESSED`,
and this run's negative results carry less weight than the Arboleda-Tham run's, which
committed its logs. The report's candour about checksums — not computed because hashing
was blocked in the sandbox, with the inputs argued regenerable from pinned queries — is
undercut by ClinVar being an unpinned live database.

## Disposition

Category stays `UNKNOWN`. Two evidence items promoted from one paper, one supporting the
premise and one refuting the protein claim, each verified against the fetched record. One
hypothesis description amended. Nothing promoted from the computational work.
