"""Display labels for the treatment-platform enums.

`therapeutic_modality` and the `oligonucleotide_details` slots are enum-backed, so
the raw values are upper-snake-case keys. Jinja's `| title` filter is not good
enough for them: it renders SIRNA as "Sirna", GALNAC as "Galnac" and
RNAI_KNOCKDOWN as "Rnai Knockdown". The labels here are editorial rather than
derivable (2'-MOE, GalNAc, cEt), so they are curated by hand.

This lives in Python rather than in a Jinja map because two templates need it --
`disorder.html.j2` and `module.html.j2` -- and those templates already duplicate
several macros between them. A drifting label map would be a silent
inconsistency between two pages describing the same treatment.

One map covers five enums. The handful of keys that appear in more than one
(OTHER, PEPTIDE) want the same display text in each, so the collision is
harmless; a test pins that down along with full coverage of every permissible
value.
"""

from __future__ import annotations

TREATMENT_PLATFORM_LABELS: dict[str, str] = {
    # TherapeuticModalityEnum
    "SMALL_MOLECULE": "Small molecule",
    "MONOCLONAL_ANTIBODY": "Monoclonal antibody",
    "NANOBODY": "Nanobody",
    "ANTISENSE_OLIGONUCLEOTIDE": "Antisense oligonucleotide",
    "SIRNA": "siRNA",
    "MRNA_THERAPY": "mRNA therapy",
    "GENE_THERAPY": "Gene therapy",
    "GENE_EDITING": "Gene editing",
    "CELL_THERAPY": "Cell therapy",
    "PROTEIN_REPLACEMENT": "Protein replacement",
    "PEPTIDE": "Peptide",
    "VACCINE": "Vaccine",
    "RADIOTHERAPY": "Radiotherapy",
    "SURGERY": "Surgery",
    "DEVICE": "Device",
    "BEHAVIORAL": "Behavioral / lifestyle",
    # OligonucleotideMechanismEnum
    "RNASE_H_KNOCKDOWN": "RNase H knockdown",
    "RNAI_KNOCKDOWN": "RNAi knockdown",
    "SPLICE_MODULATION_EXON_SKIPPING": "Splice modulation (exon skipping)",
    "SPLICE_MODULATION_EXON_INCLUSION": "Splice modulation (exon inclusion)",
    "STERIC_BLOCKADE": "Steric blockade",
    "MIRNA_MODULATION": "miRNA modulation",
    # OligonucleotideChemistryEnum
    "PHOSPHOROTHIOATE": "Phosphorothioate",
    "PHOSPHORODIAMIDATE_MORPHOLINO": "Morpholino (PMO)",
    "TWO_PRIME_O_METHYL": "2′-O-methyl",
    "TWO_PRIME_FLUORO": "2′-fluoro",
    "TWO_PRIME_O_METHOXYETHYL": "2′-MOE",
    "LOCKED_NUCLEIC_ACID": "Locked nucleic acid (LNA)",
    "CONSTRAINED_ETHYL": "Constrained ethyl (cEt)",
    # OligonucleotideConjugationEnum
    "UNCONJUGATED": "Unconjugated",
    "GALNAC": "GalNAc",
    "LIPID": "Lipid",
    "ANTIBODY": "Antibody conjugate",
    # OligonucleotideDeliveryPlatformEnum
    "UNFORMULATED": "Unformulated (free uptake)",
    "CONJUGATE": "Ligand conjugate",
    "LIPID_NANOPARTICLE": "Lipid nanoparticle",
    "POLYMER_NANOPARTICLE": "Polymer nanoparticle",
    "VIRAL_VECTOR": "Viral vector",
    "EXOSOME": "Exosome",
    # Shared across several of the above
    "OTHER": "Other",
}


def treatment_platform_label(value: object) -> str:
    """Return the display label for a treatment-platform enum value.

    An unmapped value degrades to a readable form rather than vanishing, so a
    newly added enum member still shows on the page while its label is being
    written. Returns an empty string for a missing value so callers can use the
    result directly in a truthiness test.
    """
    if value is None:
        return ""
    key = str(value)
    if not key:
        return ""
    return TREATMENT_PLATFORM_LABELS.get(key) or key.replace("_", " ").capitalize()
