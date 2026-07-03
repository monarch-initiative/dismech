# Enum: TherapeuticModalityEnum 




_Broad therapeutic modality / platform of a treatment, independent of the specific agent or MAXO action term. Captures the "kind of thing" a treatment is (e.g., a small molecule vs. an antisense oligonucleotide vs. a gene therapy) so treatments are queryable by platform across diseases._



URI: [dismech:enum/TherapeuticModalityEnum](https://w3id.org/monarch-initiative/dismech/enum/TherapeuticModalityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SMALL_MOLECULE | NCIT:C48809 | Small-molecule pharmacotherapy (orally or parenterally administered chemical ... ||
| MONOCLONAL_ANTIBODY | NCIT:C20401 | Monoclonal antibody or antibody-derived biologic (including bispecifics and a... ||
| ANTISENSE_OLIGONUCLEOTIDE | NCIT:C1291 | Single-stranded antisense oligonucleotide (ASO) acting on RNA via RNase H, sp... | Title: Antisense oligonucleotide<br>|
| SIRNA | NCIT:C2191 | Small interfering RNA or other double-stranded RNAi therapeutic | Title: siRNA / RNAi<br>|
| MRNA_THERAPY | None | Therapeutic messenger RNA delivering a functional transcript (excludes prophy... | Title: mRNA therapy<br>|
| GENE_THERAPY | NCIT:C15238 | Gene addition/replacement therapy (e ||
| GENE_EDITING | None | In vivo or ex vivo genome editing (e ||
| CELL_THERAPY | NCIT:C70601 | Cell-based therapy (e ||
| PROTEIN_REPLACEMENT | NCIT:C16221 | Recombinant protein or enzyme replacement therapy ||
| PEPTIDE | CHEBI:16670 | Therapeutic peptide or peptide analog ||
| VACCINE | NCIT:C923 | Prophylactic or therapeutic vaccine ||
| RADIOTHERAPY | NCIT:C15313 | Radiation-based therapy ||
| SURGERY | NCIT:C15329 | Surgical or procedural intervention ||
| DEVICE | NCIT:C16830 | Implanted or external therapeutic device ||
| BEHAVIORAL | None | Non-pharmacologic behavioral, physical, dietary, or lifestyle intervention ||
| OTHER | None | Modality not covered by the above categories ||




## Slots

| Name | Description |
| ---  | --- |
| [therapeutic_modality](../slots/therapeutic_modality.md) | Broad therapeutic platform/modality of a treatment (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: TherapeuticModalityEnum
description: Broad therapeutic modality / platform of a treatment, independent of
  the specific agent or MAXO action term. Captures the "kind of thing" a treatment
  is (e.g., a small molecule vs. an antisense oligonucleotide vs. a gene therapy)
  so treatments are queryable by platform across diseases.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  SMALL_MOLECULE:
    text: SMALL_MOLECULE
    description: Small-molecule pharmacotherapy (orally or parenterally administered
      chemical drugs)
    meaning: NCIT:C48809
    aliases:
    - Small Molecule
  MONOCLONAL_ANTIBODY:
    text: MONOCLONAL_ANTIBODY
    description: Monoclonal antibody or antibody-derived biologic (including bispecifics
      and antibody-drug conjugates)
    meaning: NCIT:C20401
    aliases:
    - Monoclonal Antibody
  ANTISENSE_OLIGONUCLEOTIDE:
    text: ANTISENSE_OLIGONUCLEOTIDE
    description: Single-stranded antisense oligonucleotide (ASO) acting on RNA via
      RNase H, splice modulation, or steric blockade
    meaning: NCIT:C1291
    title: Antisense oligonucleotide
    aliases:
    - Antisense Oligonucleotides
  SIRNA:
    text: SIRNA
    description: Small interfering RNA or other double-stranded RNAi therapeutic
    meaning: NCIT:C2191
    title: siRNA / RNAi
    aliases:
    - Small Interfering RNA
  MRNA_THERAPY:
    text: MRNA_THERAPY
    description: Therapeutic messenger RNA delivering a functional transcript (excludes
      prophylactic mRNA vaccines, see VACCINE)
    title: mRNA therapy
    comments:
    - No generic "mRNA therapy" class exists in the configured ontologies; left unmapped
  GENE_THERAPY:
    text: GENE_THERAPY
    description: Gene addition/replacement therapy (e.g., AAV- or lentivirus-delivered
      transgene)
    meaning: NCIT:C15238
    aliases:
    - Gene Therapy
  GENE_EDITING:
    text: GENE_EDITING
    description: In vivo or ex vivo genome editing (e.g., CRISPR/Cas, base or prime
      editing)
    comments:
    - No generic "gene/genome editing" class in the configured ontologies (only narrower
      CRISPR Gene Editing NCIT:C200340); left unmapped
  CELL_THERAPY:
    text: CELL_THERAPY
    description: Cell-based therapy (e.g., CAR-T, stem cell transplantation, engineered
      cells)
    meaning: NCIT:C70601
    aliases:
    - Cellular Therapy
  PROTEIN_REPLACEMENT:
    text: PROTEIN_REPLACEMENT
    description: Recombinant protein or enzyme replacement therapy
    meaning: NCIT:C16221
    aliases:
    - Protein Replacement Therapy
  PEPTIDE:
    text: PEPTIDE
    description: Therapeutic peptide or peptide analog
    meaning: CHEBI:16670
    aliases:
    - peptide
  VACCINE:
    text: VACCINE
    description: Prophylactic or therapeutic vaccine
    meaning: NCIT:C923
    aliases:
    - Vaccine
  RADIOTHERAPY:
    text: RADIOTHERAPY
    description: Radiation-based therapy
    meaning: NCIT:C15313
    aliases:
    - Radiation Therapy
  SURGERY:
    text: SURGERY
    description: Surgical or procedural intervention
    meaning: NCIT:C15329
    aliases:
    - Surgical Procedure
  DEVICE:
    text: DEVICE
    description: Implanted or external therapeutic device
    meaning: NCIT:C16830
    aliases:
    - Medical Device
  BEHAVIORAL:
    text: BEHAVIORAL
    description: Non-pharmacologic behavioral, physical, dietary, or lifestyle intervention
    comments:
    - Intentionally broad (behavioral/physical/dietary/lifestyle); no single faithful
      ontology class, left unmapped
  OTHER:
    text: OTHER
    description: Modality not covered by the above categories

```
</details>