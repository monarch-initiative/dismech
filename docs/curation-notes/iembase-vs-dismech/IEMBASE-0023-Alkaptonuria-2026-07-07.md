# IEMbase 0023: HGD-related homogentisic acid oxidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 23 |
| Nosology | 1.4.05.01 |
| Gene | HGD |
| External IDs | OMIM:203500 |
| Generated mapping | MAPPED by `alias_exact:aku` |
| Candidate DisMech targets | `Alkaptonuria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents classic alkaptonuria. The characteristic clinical triad is
adult-onset arthritis, ochronosis, and urine darkening on standing, with urine
darkening marked across all age bands. The defining biochemical signal is
markedly elevated urinary homogentisate.

Additional IEMbase clinical signals include lumbosacral disc degeneration,
scleral pigmentation, general pigmentation, intrinsic dental staining, and adult
aortic and mitral valvulitis. No specific treatment rows are present in this
JSON record despite the disease-level `treatability` value being `yes`.

## DisMech phenotype coverage

The generated mapping to `Alkaptonuria.yaml` is correct. DisMech covers HGD loss
of function, homogentisic acid accumulation and oxidation, ochronotic connective
tissue degeneration, dark urine, ochronosis, osteoarthritis/arthritis,
arthralgia, joint stiffness/swelling/dislocation, back pain, intervertebral disc
calcification, cartilage calcification/destruction, tendon rupture, Achilles
tendon thickening, aortic and mitral valve calcification/stenosis, coronary
calcification, nephrolithiasis, hearing abnormalities, visual/ocular
involvement, scleral and corneal-limbal pigmentation, skin pigmentation,
elevated urinary homogentisic acid, and reduced HGD activity. It also includes
nitisinone therapy.

## Concordance and completeness

Judgement: correct mapping and very high concordance. DisMech is substantially
richer than IEMbase for musculoskeletal, cardiovascular, renal, ocular, and
treatment coverage.

IEMbase contributes a few useful granularity checks: intrinsic dental staining,
the explicit lumbosacral-disc wording, and inflammatory `valvulitis` labels.
DisMech already covers the same major organ systems, but mostly as calcific or
structural valve disease rather than valvulitis.

## Curation actions

- Keep the generated mapping.
- Consider whether intrinsic dental staining merits a phenotype entry if
  supported by alkaptonuria evidence.
- Review whether the adult valve phenotype should stay framed as calcification
  or whether inflammatory valvulitis wording is evidence-supported.
