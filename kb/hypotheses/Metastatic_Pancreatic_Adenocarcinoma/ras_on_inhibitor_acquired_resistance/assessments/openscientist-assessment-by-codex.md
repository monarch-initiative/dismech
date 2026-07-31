# Assessment of the OpenScientist daraxonrasib-resistance report

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Overall assessment

The report is a useful multi-route research map, but it is not a clinically
established resistance taxonomy. Daraxonrasib resistance is real: the phase
1-2 study shows finite response duration
([PMID:42090791](https://pubmed.ncbi.nlm.nih.gov/42090791/)), and a recent
preprint describes resistant PDAC models plus one KRAS-G12R patient who
progressed after ten months
([PMID:42465401](https://pubmed.ncbi.nlm.nih.gov/42465401/)). The specific
routes and their frequencies in patients remain unresolved.

The phase 3 median progression-free survival
([PMID:42223072](https://pubmed.ncbi.nlm.nih.gov/42223072/)) does not, by
itself, show that essentially every patient acquired resistance. A PFS event can
be progression or death, and many patients never had an objective response.
That distinction matters: primary nonresponse and escape after a response are
not the same biological claim.

## Strongest drug-matched leads

The most direct drug-and-disease-matched mechanistic source is
[PMID:42465401](https://pubmed.ncbi.nlm.nih.gov/42465401/). It reports
different routes in KRAS-G12D and KRAS-G12R PDAC: reduced cyclophilin A with
retained mutant-RAS signaling in G12D models, and EGFR/RAS-WT dependence in
G12R models and one patient. It is still a preprint, and only the G12R route has
the single-patient anchor.

Two other recent studies support deeper, RAS-independent escape candidates.
[PMID:41959066](https://pubmed.ncbi.nlm.nih.gov/41959066/) describes
RMC-6236-resistant cells whose proliferation became uncoupled from RAS and
could be constrained by CDK4/6 or CDK2 targeting.
[PMID:41572361](https://pubmed.ncbi.nlm.nih.gov/41572361/) supports JUN as a
convergent resistance node, but specifically under combined SHP2 plus RMC-6236
in cell models; its in-vivo reversal experiment used SHP2 plus ERK inhibition.

## Important corrections

The report overstates [PMID:41165456](https://pubmed.ncbi.nlm.nih.gov/41165456/)
as evidence from multiselective-RAS(ON)-resistant models. That NSCLC study
selected resistance to G12C(OFF) or G12C-selective RAS(ON) inhibitors.
The KRAS-amplified and NRAS-mutant models were vulnerable to dual RMC-4998 plus
RMC-7977 treatment, while the RTK/persistent-RAS models were sensitive to
RMC-7977 alone. Multiselective inhibition, alone or in combination, therefore
overcame these states rather than establishing them as routes of daraxonrasib
escape.

The metabolic claim also needs tighter scope.
[PMID:41545339](https://pubmed.ncbi.nlm.nih.gov/41545339/) establishes
mitochondrial remodeling and GPX4 vulnerability chiefly after dual SHP2/MEK
inhibition, with confirmation under direct RAS targeting. It does not establish
that this is a prevalent patient-level daraxonrasib resistance route.
The RTK/PI3K compensation anchor
([PMID:25736685](https://pubmed.ncbi.nlm.nih.gov/25736685/)) is likewise analog
evidence from a KRAS-driven PDAC mouse model, not a clinical daraxonrasib cohort.

## Curation implication

Retain acquired resistance as real and the allele-specific, cell-cycle, JUN,
RTK/PI3K, and metabolic routes as candidate mechanisms with explicit
model-system qualifiers. Do not promote a universal-resistance statement or
route ranking into the disease YAML until paired baseline/progression tissue or
serial ctDNA from a daraxonrasib-treated PDAC cohort establishes prevalence and
selection.
