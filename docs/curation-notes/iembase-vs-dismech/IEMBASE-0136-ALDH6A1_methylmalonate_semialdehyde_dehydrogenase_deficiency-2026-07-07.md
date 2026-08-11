# IEMbase 0136: ALDH6A1-related Methylmalonate semialdehyde dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 136 |
| Nosology | 1.2.17.01 |
| Gene | ALDH6A1 |
| External IDs | OMIM:603178; ORPHA:289307 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No valid ALDH6A1/MMSDH target found; generated SSADH candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ALDH6A1-related methylmalonate semialdehyde
dehydrogenase deficiency, abbreviated MMSDH. Treatability is marked unknown.

Characteristic biochemical rows include normal-to-increased urinary
2-aminoisobutyric acid, 3-aminoisobutyric acid, 3-hydroxyisobutyric acid, and
ethylmalonic acid. Other rows include normal-to-increased methionine,
beta-alanine, 3-hydroxypropionic acid, lactate, and decreased fibroblast
methylmalonic semialdehyde dehydrogenase activity. Clinical rows include
developmental delay, hepatomegaly, episodic vomiting, and failure to thrive.

## DisMech phenotype coverage

No local standalone ALDH6A1/MMSDH entry was found. The generated
`Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` candidate is a false
semialdehyde-dehydrogenase neighbor: SSADH deficiency is an ALDH5A1 disorder of
GABA catabolism with GABA/GHB accumulation, not ALDH6A1 methylmalonate
semialdehyde metabolism.

HIBCH deficiency and other valine-catabolism entries are pathway neighbors but
do not cover ALDH6A1 disease scope.

## Concordance and completeness

Judgement: true unmapped local disease gap.

The IEMbase record has a recognizable MMSDH biochemical pattern involving
aminoisobutyric acids, 3-hydroxyisobutyric acid, ethylmalonic acid, and reduced
MMSDH enzyme activity. Current DisMech captures adjacent valine or GABA pathway
disorders, but not the ALDH6A1 disease entity.

## Curation actions

- Keep this record unmapped.
- Reject the SSADH/ALDH5A1 candidate.
- Future curation should add ALDH6A1/MMSDH deficiency with the urinary organic
  acid and aminoisobutyric acid profile, failure to thrive, developmental
  delay, hepatomegaly, vomiting, and valine/thymine-catabolism mechanism.
