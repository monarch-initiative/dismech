# Boutonneuse fever deep-research fallback

Date: 2026-05-09

## Provider attempts

- `timeout 240s just research-disorder falcon Boutonneuse_Fever` timed out with exit code 124.
- `timeout 240s just research-disorder openai Boutonneuse_Fever` timed out with exit code 124.

No provider output artifact was produced. Curation proceeded from locally cached
Orphanet structured records and PubMed abstracts/full text fetched with
`just fetch-reference`.

## Scope used

- `ORPHA:83313` was used as the disease-specific Boutonneuse fever /
  Mediterranean spotted fever structured record. It supplies the definition,
  epidemiology, all-ages onset, exact MONDO mapping, and all 26 HPO phenotype
  rows used in the YAML.
- `ORPHA:101334` was checked because MONDO cross-references it, but it is the
  African tick typhus record caused by `Rickettsia africae`; its phenotypes were
  not transferred to the R. conorii Boutonneuse fever entry.
- `PMID:34698275` was used for the modern review summary of R. conorii subsp.
  conorii, brown dog tick vector, endothelial dissemination, diagnostic methods,
  and doxycycline treatment.
- `PMID:26090319` was used as a 250-patient case series for fever, rash, palm
  and sole involvement, inoculation eschar, blood-test abnormalities, acute renal
  injury, treatment use, ICU admission, and mortality.
- `PMID:15109588` and `PMID:16881414` were used for clinical diagnosis,
  serology-supported confirmation, disseminated vasculitis, tick-bite prevention
  context, and antimicrobial treatment.
- `PMID:7691249`, `PMID:8675654`, and `PMID:16926398` were used for the
  endothelial-injury, cytokine, COX-2/prostaglandin, vasculitis, and vascular
  permeability mechanism chain.

## Local audit summary

- Schema and term validation passed for `kb/disorders/Boutonneuse_Fever.yaml`.
- Local snippet audit found all quoted snippets/findings in cached references.
- Graph-target audit found all downstream and treatment mechanism targets.
- ORPHA phenotype coverage audit found 26/26 `ORPHA:83313` HPO rows represented.
