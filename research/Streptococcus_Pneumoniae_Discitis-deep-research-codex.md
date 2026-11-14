# Streptococcus Pneumoniae Discitis Deep Research Note

## Scope and source mode

No external deep-research provider was used for this follow-up pass. This local
Codex review re-read the cached pneumococcal discitis sources and fetched
additional PubMed/PMC records to check for missed host-context, progression,
phenotype, diagnostic, and treatment evidence.

## Sources added

- PMID:40429472 — a recent pyogenic spondylodiscitis management review with
  risk-factor, imaging, biopsy, neurologic-deficit, and operative-decompression
  synthesis.
- PMID:29721239 — a pneumococcal meningitis, spondylodiscitis, and pneumonia
  case that ultimately revealed antibody deficiency and MGUS.
- PMID:40490099 — a pneumococcal vertebral discitis case diagnosed concurrently
  with pneumococcal infectious endocarditis.

## Findings added to the entry

The follow-up pass fixes three structural omissions in the first curation:

- **Mechanism connectivity** — human pneumococcal carriage now feeds bloodstream
  invasion; bloodstream invasion feeds bacteremia and fever; local disc-endplate
  infection feeds epidural and paraspinal suppuration; epidural purulence can
  compress the thecal sac and produce lower-limb weakness or hypoesthesia.
- **Progression and severity** — the entry now records carriage-to-bacteremia,
  local epidural/paraspinal extension with higher neurologic-deficit mortality
  in the pooled pneumococcal review, and multifocal invasive pneumococcal
  disease with reported meningitis, pneumonia, and endocarditis foci.
- **Diagnosis and treatment** — MRI is added as the key imaging modality;
  culture now covers blood and CT-guided spinal biopsy; antimicrobial therapy
  carries named agents from the penicillin-resistant case report; and
  laminectomy/fenestration is targeted to epidural neural compression.

PMID:24481748 describes a pooled human review, so its evidence rows were
regraded to `HUMAN_CLINICAL` with `quote_role: REVIEW_SYNTHESIS`.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.
