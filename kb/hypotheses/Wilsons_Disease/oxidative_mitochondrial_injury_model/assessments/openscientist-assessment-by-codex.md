# Codex assessment of the OpenScientist report

## Verdict

**Supported for the scoped hepatic core.** Pathological mitochondrial copper,
structural injury, oxidative stress, impaired respiration and ATP production,
and hepatocyte damage recur across human tissue and ATP7B models
(PMID:24517326; PMID:41480142; PMID:35603480). This is a canonical downstream
mechanism in Wilson disease.

The report's expanded formulation is more confident than the evidence.

## Material corrections

- The 13-study meta-analysis establishes recurring hepatic abnormalities across
  heterogeneous human and animal studies. It does not establish that
  oxidative-mitochondrial injury is **necessary**, **dominant**, or the **final
  common pathway** for all hepatocyte death (PMID:41480142).
- Human immunohistochemistry supports inner-membrane injury, but the study is
  observational in treated noncirrhotic patients. 8-OHdG was lower in Wilson
  samples, and 4-HNE elevation was borderline rather than significant
  (PMID:35477108). It does not directly validate the report's causal sequence.
- The proposed NRF2/GSH “shared gatekeeper” comes from acetaminophen overdose,
  not ATP7B deficiency or Wilson disease (PMID:41866691).
- The partial antioxidant experiment is in rainbow-trout hepatocytes.
  Vitamin-C effects on apoptosis but not LDH/HSP70 support multiple responses
  in that system; they do not prove ROS necessity in Wilson hepatocytes
  (PMID:12927909).
- The Wilson-specific cuproptosis study is suggestive but does not report the
  complete defining aggregation/iron-sulfur-loss sequence in its abstract
  (PMID:41230834).
- Methanobactin rescue strongly supports copper as the upstream toxic driver in
  ATP7B-deficient rats, but upstream copper removal cannot distinguish among
  downstream death mechanisms (PMID:27322060).

## Ontology and provenance

Three proposed mappings are incorrect: GO:0140623 is type I pilus assembly
(ferroptosis is GO:0097707), GO:0034383 is LDL-particle clearance, and
CL:0000049 is common myeloid progenitor rather than megakaryoblast. The stated
130-paper review is also not auditable from the 30 unique PMIDs exposed in the
committed report artifacts.

Retain the canonical oxidative-mitochondrial hypothesis, but do not promote the
NRF2 hierarchy, pathway-dominance language, regulated-cell-death branches, or
ontology leads without separate primary-evidence curation.

The authoritative structured dispositions are in
`openscientist-assessment-by-codex.yaml`.
