# Streptococcus Pneumoniae Discitis Research Note

## Provider Attempts

OpenScientist was attempted with
`just research-disorder openscientist Streptococcus_Pneumoniae_Discitis` after
confirming that `OPENSCIENTIST_API_KEY` was available. The run resolved the
entry identity anchors and then remained active without writing
`research/Streptococcus_Pneumoniae_Discitis-deep-research-openscientist.md` or a
staged report; the local poller was terminated after a bounded wait.

The inline Claude Code provider was attempted with
`just research-disorder claude_code Streptococcus_Pneumoniae_Discitis`. It
resolved the same identity anchors and then exited with code 1 before writing a
staged report:

```text
Error: Claude Code exited with code 1: <no stderr>
```

The repo-supported Cyberian/Codex fallback was attempted with
`just research-disorder-cyberian-codex Streptococcus_Pneumoniae_Discitis`. It
started but exited before running because the local `deep-research-client`
installation only exposed the `openscientist` and `claude_code` providers:

```text
Error: Provider 'cyberian' not available. Available: openscientist, claude_code
```

Because no provider report was available, curation used a PubMed-backed local
literature sweep plus a cached-source follow-up pass. All evidence snippets in
`kb/disorders/Streptococcus_Pneumoniae_Discitis.yaml` were selected from cached
reference files generated with `just fetch-reference` and validated locally.

## Mechanistic Summary

Streptococcus pneumoniae discitis is a rare invasive pneumococcal infection of
the vertebral endplate and intervertebral disc. The curated page treats it as a
standalone organism-and-site infectious leaf, separate from broader infectious
discitis and from non-disc spinal pneumococcal infections.

The modeled pathograph is:

1. Pneumococci colonize the human upper airway.
2. During invasive pneumococcal disease, mucosal pneumococci enter the
   bloodstream.
3. Bacteremia seeds the lumbar disc-endplate complex.
4. Local pyogenic infection can extend into epidural or paraspinal spaces.
5. Epidural purulence can compress the thecal sac and produce lower-limb
   weakness or sensory loss.

The entry intentionally leaves pneumococcus-specific osteoblast or vertebral
bone-remodeling mechanisms unmodeled, because the available discitis-specific
literature supports the organism, bacteremic dissemination, local
spondylodiscitis, and epidural/paraspinal abscess manifestations but not a
quoted pneumococcal molecular chain at the vertebral endplate.

## Cached-source Coverage

PMID:24481748 provides the main pneumococcal spinal-and-paraspinal review: two
institutional cases plus 50 additional cases from the published literature. Its
pooled clinical review supports the rarity claim, common localized back pain,
lumbar predominance, epidural and paraspinal abscess involvement, and the
association between epidural abscess or phlegmon and neurologic deficits.

PMID:38680822 reports disseminated penicillin-resistant pneumococcal disease
with lumbar spondylodiscitis, multiple abscesses, progressive lower-limb
neurologic deficits, and decompressive surgery. This case supports the
disc-to-epidural compression chain and susceptibility-guided antimicrobial
therapy.

PMID:40429472 is a pyogenic spondylodiscitis management review, rather than a
pneumococcus-specific review. Its risk-factor, MRI, culture/biopsy, and neural
compression claims are therefore modeled as generic pyogenic-spondylodiscitis
context with indirect links to the pneumococcal discitis pathograph.

PMID:21734248 and PMID:29599457 support human pneumococcal nasopharyngeal
carriage and bloodstream invasion during invasive disease. PMID:29721239 and
PMID:40490099 add case-level examples of pneumococcal spondylodiscitis occurring
with meningitis, pneumonia, antibody deficiency, and endocarditis.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.
