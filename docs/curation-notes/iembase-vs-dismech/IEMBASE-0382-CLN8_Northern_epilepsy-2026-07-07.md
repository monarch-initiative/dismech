# IEMbase 0382: CLN8-related Northern epilepsy variant

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 382 |
| Nosology | 20.4.07.02 |
| Gene | CLN8 |
| External IDs | OMIM:610003; ORPHA:228354 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | Broad `Neuronal_Ceroid_Lipofuscinosis.yaml` context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive CLN8-related Northern epilepsy variant,
also listed as CLN8 disease, progressive epilepsy with mental retardation, and
CLN8-EPMR.

Clinical rows emphasize seizures, including complex partial and tonic-clonic
seizures, plus behavioral disorder, cognitive decline, movement disorder,
ataxia, EEG abnormalities, storage material on electron microscopy, cerebral
and cerebellar atrophy on MRI, myoclonus, neurodegeneration, and speech
abnormality. There are no biochemical or treatment rows.

## DisMech phenotype coverage

There is broad local neuronal ceroid lipofuscinosis context, and
`Neuronal_Ceroid_Lipofuscinosis.yaml` includes CLN8 as a causative gene for the
NCL umbrella. However, the current local file does not provide a standalone
Northern epilepsy/CLN8-EPMR disease target or a leaf entry that captures this
specific CLN8 phenotype.

This conclusion is consistent with the earlier CLN8 late-infantile comparison:
the broad NCL file is useful shared context, but it should not be treated as an
exact replacement for missing CLN8 leaf diseases. Adult neuronal ceroid
lipofuscinosis/Kufs disease entries are also not valid targets for this
Northern epilepsy variant.

## Concordance and completeness

Judgement: true subtype/leaf gap; keep unmapped at disease level.

The local NCL umbrella supports the shared CLN8/NCL biology but lacks the
CLN8-EPMR-specific seizure, cognitive, movement, EEG, storage-material, and MRI
phenotype frame represented by IEMbase.

## Curation actions

- Keep this record unmapped until a CLN8 Northern epilepsy/CLN8-EPMR target or
  explicit subtype anchor exists.
- Use `Neuronal_Ceroid_Lipofuscinosis.yaml` only as broad NCL context.
- Do not map this record to adult NCL/Kufs entries or to the separate
  late-infantile CLN8 record without an explicit subtype decision.
