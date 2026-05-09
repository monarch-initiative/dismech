---
title: Dental Caries deep-research fallback
date: 2026-05-05
curator: codex
---

# Dental Caries deep-research fallback

This fallback research note was added while repairing the older conflicting PR #1370.
No provider-generated deep-research artifact was present on the branch, so the review
fix was bounded to the cached references already cited by the entry and the concrete
open review comments.

## Scope checked

- Ecological-plaque-hypothesis framing: PMID:12624191 and PMID:29195050 support
  low-pH selection, oral microbiome dysbiosis, and self-reinforcing cariogenic
  biofilm ecology.
- Biofilm virulence and species breadth: PMID:40933845 supports S. mutans
  glucosyltransferase, glucan-binding, and two-component virulence genes. The YAML
  now frames this as mutans-streptococci / cariogenic-biofilm biology rather than
  implying that extracellular glucan biosynthesis is restricted to S. mutans alone.
- Enamel chemistry: PMID:28540937 and PMID:17208642 support caries as phasic
  demineralization and remineralization of dental hard tissues. The acid-mediated
  node now models reduced apatite directly instead of binding acid dissolution to
  decreased tooth-mineralization GO.
- Probiotic therapy: PMID:40995678 contains a direct clinical-trial summary for
  reduced S. mutans counts and caries incidence with probiotic lozenges, gums, and
  dairy products; the treatment evidence was updated to quote that outcome text.

## Remaining limitations

This is not a broad new literature expansion. It documents the targeted review-fix
scope needed to make the older Dental Caries branch auditable without adding
uncited claims or hand-edited reference caches.
