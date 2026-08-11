# Assessment of the OpenScientist report

**Hypothesis:** Alternative H. pylori molecular-mimicry ("hit-and-run") origin
**Assessor:** Codex
**Verdict:** **PARTIALLY_SUPPORTED**

The report is a useful lead for an H. pylori-associated AIG subset, not a basis
for promoting the full hit-and-run mechanism as established disease knowledge.
Human gastric T-cell cross-reactivity supplies direct mechanistic plausibility,
and an uncontrolled eradication cohort supports reversibility of an early,
active, non-atrophic phenotype. Neither result demonstrates that infection
initiates AIG, that epitope spreading occurs, or that autoimmunity persists
after clearance.

## What survives review

- Gastric CD4 clones that recognize both H+/K+-ATPase and H. pylori epitopes
  provide direct cellular cross-reactivity evidence
  ([PMID:14568977](https://pubmed.ncbi.nlm.nih.gov/14568977/)).
- Resolution after eradication in 64/80 selected patients is evidence for an
  H. pylori-dependent early phenotype, with the important limitations that the
  cohort was retrospective, uncontrolled, and explicitly not yet atrophic
  ([PMID:11549834](https://pubmed.ncbi.nlm.nih.gov/11549834/)).
- Human antibody-absorption work does not support the analogous humoral
  mimicry claim; that result qualifies rather than erases the cellular finding
  ([PMID:10738313](https://pubmed.ncbi.nlm.nih.gov/10738313/),
  [PMID:11815766](https://pubmed.ncbi.nlm.nih.gov/11815766/)).
- A large retrospective cohort supports clinically different associations in
  H. pylori-naive patients, but not a proven genetically or etiologically
  distinct entity
  ([PMID:38976374](https://pubmed.ncbi.nlm.nih.gov/38976374/)).

## Material corrections

The report reverses the logic of the eradication evidence. Early resolution
while H. pylori is removed does not support a later self-perpetuating phase;
that is precisely the edge for which prospective evidence is missing. The
reported “29–79%” exposure-negative range is also not supported. In the
multiplex study, 29.3% had no antigen reactivity; 21.1% met a stringent
multi-antigen positive cutoff, and the complement of that cutoff is not the
same as no evidence of exposure
([PMID:41484031](https://pubmed.ncbi.nlm.nih.gov/41484031/)). “Pacheco et al.
2025” is not traceable from the report or its citation sidecar.

The report further converts an indirect thyroid-disease MR synthesis into proof
of shared-genetic confounding, although the cited analysis did not test the
H. pylori-to-AIG edge
([PMID:41425574](https://pubmed.ncbi.nlm.nih.gov/41425574/)). Its categorical
“No GWAS” gap overlooks the large pernicious-anemia GWAS
([PMID:34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/)).

The candidate ontology block is unsafe to curate: MONDO:0007093 and
MONDO:0008223 resolve to unrelated disorders, and CL:0002086 is a specialized
cardiac myocyte, not a regulatory T cell. The existing disease YAML uses
MONDO:0031014 for autoimmune gastritis; MONDO:0008228 is the current
pernicious-anemia term.

## Disease-YAML follow-up

This assessment intentionally does not edit
`kb/disorders/Autoimmune_Gastritis.yaml`. Its current notes nevertheless repeat
two report overclaims that require a separate evidence-curation change:

1. the 80% healing result is said to support a time-limited hit-and-run window;
2. approximately 29–79% of cases are described as H. pylori-naive.

The disease YAML should instead separate four propositions: cellular
cross-reactivity is observed; an early selected phenotype can resolve after
eradication; a sizable H. pylori-naive group exists; and the full
initiation-to-persistent-autoimmunity sequence remains unproven.
