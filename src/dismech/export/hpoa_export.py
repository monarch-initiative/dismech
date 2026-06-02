"""
HPOA-extended exporter for dismech.

Projects disorder YAML files into a MONDO-anchored, HPOA-extended TSV that
mirrors the 12-column ``phenotype.hpoa`` format used by the HPO project, plus
one extra column (``dismech_name``) preserving dismech's clinical label when
it is more specific than the HPO term label.

A sidecar ``disease_comorbidity.tsv`` captures phenotype entries whose object
is a MONDO term — true disease-to-disease comorbidities that are not phenotypic
features. (See ``kgx_export.disease_comorbidity_to_edge`` for the same routing
applied to the KGX graph.)

Rules
-----
* Disease ID is anchored on MONDO (column 1); disorders without a MONDO term
  are skipped.
* Evidence with ``evidence_source: MODEL_ORGANISM`` is dropped (HPOA is a
  human-phenotype resource). ``IN_VITRO`` is kept and coded ``PCS`` because
  dismech's in-vitro evidence is overwhelmingly human iPSC / cell-line work.
* ``supports`` handling: ``NO_EVIDENCE`` items are dropped (the cited reference
  does not mention the claim, so a positive row would be misleading);
  ``REFUTE`` / ``WRONG_STATEMENT`` become ``NOT``-qualified rows; ``PARTIAL`` is
  kept as a normal positive row (HPOA has no partial qualifier, and partial
  support still attests the association) with no qualifier; ``SUPPORT`` /
  missing is a normal positive row.
* A phenotype whose ``frequency`` enum is ``EXCLUDED`` asserts the phenotype is
  *absent*; it is emitted as a ``NOT``-qualified row with an empty frequency
  column rather than a positive row carrying the "Excluded" frequency term.
* One row per (phenotype, surviving evidence item) pair. Phenotypes with no
  surviving evidence still emit one ``IEA`` row anchored on the MONDO disease.
  This IEA fallback applies to HPO-phenotype rows only — MONDO-typed
  comorbidity entries with no surviving evidence emit no row, because asserting
  a disease-disease comorbidity with zero evidence is not warranted.
* The ``reference`` column passes through whatever prefix the evidence item
  carries (``PMID:``, ``ORPHA:``, ``DOI:``, ``clinicaltrials:``, ``CGGV:``,
  …); HPOA consumers should not assume column 5 is always a PMID.
* Untyped phenotypes (no ``phenotype_term.term.id``) get a synthetic
  ``DISMECH:<entry-slug>#<phen-slug>`` CURIE in column 4.
* Frequency is extracted from the phenotype description when a literal ``X%``,
  ``X-Y%`` or ``X/N`` is present; otherwise the dismech frequency enum is
  mapped to an HPO Frequency term. Enum lookup tolerates case/separator
  variants (``Frequent``, ``very frequent``) and already-resolved HP frequency
  terms (``HP:0040282`` / ``HP_0040282``); genuinely ambiguous free text
  (``Common``, ``Variable``, …) is left unmapped rather than guessed.
* ``aspect`` defaults to ``P`` (phenotypic abnormality); a proper OAK-based
  classification (C / I / M / H) is a follow-up.
"""
from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

import yaml


HPOA_VERSION = "dismech-extended-v1"
BIOCURATOR = "Monarch:dismech"

FREQUENCY_TO_HP: dict[str, str] = {
    "OBLIGATE": "HP:0040280",
    "VERY_FREQUENT": "HP:0040281",
    "FREQUENT": "HP:0040282",
    "OCCASIONAL": "HP:0040283",
    "VERY_RARE": "HP:0040284",
    "EXCLUDED": "HP:0040285",
}

# evidence_source -> HPOA evidence code, or None to drop the evidence item.
EVIDENCE_CODE: dict[Any, str | None] = {
    "HUMAN_CLINICAL": "PCS",
    "IN_VITRO": "PCS",
    "COMPUTATIONAL": "IEA",
    "OTHER": "IEA",
    "MODEL_ORGANISM": None,
    None: "IEA",
}

# supports value -> HPOA qualifier. Anything absent here (SUPPORT, PARTIAL)
# becomes a positive row with an empty qualifier: PARTIAL support still attests
# the phenotype-disease association and HPOA has no dedicated partial qualifier.
SUPPORTS_TO_QUALIFIER: dict[Any, str] = {
    "REFUTE": "NOT",
    "WRONG_STATEMENT": "NOT",
}

# supports values whose evidence item is dropped entirely (no HPOA row).
# NO_EVIDENCE means the cited reference does not mention the claim at all, so
# emitting it as a positive PCS/IEA row would falsely imply the paper supports
# the phenotype-disease link. REFUTE/WRONG_STATEMENT are NOT dropped — they
# become NOT-qualified rows via SUPPORTS_TO_QUALIFIER.
DROP_SUPPORTS: frozenset[str] = frozenset({"NO_EVIDENCE"})

HPOA_COLUMNS = [
    "database_id",
    "disease_name",
    "qualifier",
    "hpo_id",
    "reference",
    "evidence",
    "onset",
    "frequency",
    "sex",
    "modifier",
    "aspect",
    "biocuration",
    "dismech_name",
]

COMORBIDITY_COLUMNS = [
    "database_id",
    "disease_name",
    "comorbid_id",
    "comorbid_name",
    "predicate",
    "reference",
    "evidence",
    "biocuration",
]

_PERCENT_RANGE = re.compile(r"\b(\d+)\s*[-–]\s*(\d+)\s*%")
_PERCENT_SINGLE = re.compile(
    r"(?:~|approximately\s+|about\s+)?\b(\d+)\s*%"
)
_RATIO = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")


def slugify(text: str) -> str:
    """Lowercase, replace runs of non-alphanumerics with single hyphens."""
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text or "").strip("-").lower()
    return s or "unnamed"


_HP_FREQ_TERM = re.compile(r"HP[:_](\d{7})$")


def normalize_frequency_enum(value: Any) -> str | None:
    """Map a raw ``frequency`` value to a canonical ``FrequencyEnum`` key.

    Tolerates case and separator variants (``Frequent``, ``very frequent`` ->
    ``FREQUENT`` / ``VERY_FREQUENT``). Returns ``None`` for absent or
    genuinely ambiguous free text (``Common``, ``Variable``), which is left
    unmapped rather than guessed.
    """
    if not value:
        return None
    key = re.sub(r"[\s\-]+", "_", str(value).strip()).upper()
    return key if key in FREQUENCY_TO_HP else None


def parse_frequency(phenotype: dict[str, Any]) -> str | None:
    """Pick a frequency value for the HPOA frequency column.

    Order: literal percent range, literal single percent, literal ratio, an
    already-resolved HP Frequency term (``HP:0040282`` / ``HP_0040282``), then
    the dismech enum mapped to an HPO Frequency term. Returns ``None`` only
    when no source is available.
    """
    desc = (phenotype.get("description") or "").strip()
    if desc:
        m = _PERCENT_RANGE.search(desc)
        if m:
            return f"{m.group(1)}-{m.group(2)}%"
        m = _PERCENT_SINGLE.search(desc)
        if m:
            return f"{m.group(1)}%"
        m = _RATIO.search(desc)
        if m:
            return f"{m.group(1)}/{m.group(2)}"

    raw = phenotype.get("frequency")
    if raw:
        m = _HP_FREQ_TERM.match(str(raw).strip())
        if m:
            return f"HP:{m.group(1)}"
        key = normalize_frequency_enum(raw)
        if key:
            return FREQUENCY_TO_HP[key]
    return None


def _human_evidence(
    items: list[dict[str, Any]] | None,
) -> Iterator[dict[str, Any]]:
    """Yield surviving evidence items with their HPOA evidence code attached."""
    for item in items or []:
        supports = item.get("supports")
        if supports in DROP_SUPPORTS:
            continue
        code = EVIDENCE_CODE.get(item.get("evidence_source"), "IEA")
        if code is None:
            continue
        ref = item.get("reference")
        if not ref:
            continue
        yield {"reference": ref, "code": code, "supports": supports}


def hpoa_rows_for_disorder(
    yaml_path: Path,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Read one disorder YAML and project to (hpoa_rows, comorbidity_rows)."""
    data = yaml.safe_load(yaml_path.read_text()) or {}
    disease = ((data.get("disease_term") or {}).get("term") or {})
    disease_id = disease.get("id") or ""
    if not disease_id.startswith("MONDO:"):
        return [], []
    disease_name = disease.get("label") or data.get("name") or yaml_path.stem
    entry_slug = slugify(yaml_path.stem)
    creation_date = (data.get("creation_date") or "")[:10] or datetime.now(
        timezone.utc
    ).strftime("%Y-%m-%d")
    biocuration = f"{BIOCURATOR}[{creation_date}]"

    hpoa_rows: list[dict[str, str]] = []
    comorb_rows: list[dict[str, str]] = []

    for phenotype in data.get("phenotypes") or []:
        term = ((phenotype.get("phenotype_term") or {}).get("term") or {})
        term_id = term.get("id") or ""
        term_label = term.get("label") or ""
        phen_name = phenotype.get("name") or term_label or "unnamed phenotype"

        if term_id.startswith("MONDO:"):
            for ev in _human_evidence(phenotype.get("evidence")):
                comorb_rows.append(
                    {
                        "database_id": disease_id,
                        "disease_name": disease_name,
                        "comorbid_id": term_id,
                        "comorbid_name": term_label or phen_name,
                        "predicate": "biolink:associated_with",
                        "reference": ev["reference"],
                        "evidence": ev["code"],
                        "biocuration": biocuration,
                    }
                )
            continue

        hpo_id = term_id or f"DISMECH:{entry_slug}#{slugify(phen_name)}"
        # An EXCLUDED frequency asserts the phenotype is absent: emit a
        # NOT-qualified row with no frequency rather than a positive row
        # carrying the "Excluded" frequency term.
        excluded = normalize_frequency_enum(phenotype.get("frequency")) == "EXCLUDED"
        default_qualifier = "NOT" if excluded else ""
        frequency = "" if excluded else (parse_frequency(phenotype) or "")
        evidence_items = list(_human_evidence(phenotype.get("evidence")))
        if not evidence_items:
            # Phenotype has no surviving human evidence — emit one IEA row
            # anchored on the disease itself so the assertion is still visible.
            evidence_items = [
                {"reference": disease_id, "code": "IEA", "supports": None}
            ]

        for ev in evidence_items:
            hpoa_rows.append(
                {
                    "database_id": disease_id,
                    "disease_name": disease_name,
                    "qualifier": SUPPORTS_TO_QUALIFIER.get(
                        ev["supports"], default_qualifier
                    ),
                    "hpo_id": hpo_id,
                    "reference": ev["reference"],
                    "evidence": ev["code"],
                    "onset": "",
                    "frequency": frequency,
                    "sex": "",
                    "modifier": "",
                    "aspect": "P",
                    "biocuration": biocuration,
                    "dismech_name": phen_name,
                }
            )

    return hpoa_rows, comorb_rows


def export(kb_dir: Path, out_dir: Path) -> tuple[int, int]:
    """Project every disorder YAML in ``kb_dir`` to TSV files under ``out_dir``."""
    out_dir.mkdir(parents=True, exist_ok=True)
    hpoa_path = out_dir / "phenotype.dismech.hpoa"
    comorb_path = out_dir / "disease_comorbidity.tsv"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    total_hpoa = 0
    total_comorb = 0

    with hpoa_path.open("w", newline="") as hp_f, comorb_path.open(
        "w", newline=""
    ) as co_f:
        hp_f.write(
            "#description: dismech disease-phenotype annotations, "
            "MONDO-anchored, HPOA-extended\n"
        )
        hp_f.write(f"#date: {today}\n")
        hp_f.write(f"#version: {HPOA_VERSION}\n")
        hp_f.write("#tracker: https://github.com/monarch-initiative/dismech\n")
        hp_f.write(
            "#rules: human evidence only (MODEL_ORGANISM excluded); "
            "NO_EVIDENCE dropped; REFUTE/WRONG_STATEMENT/EXCLUDED-frequency -> NOT; "
            "PARTIAL kept as positive; "
            "reference column may be PMID/ORPHA/DOI/clinicaltrials/CGGV; "
            "untyped phenotypes get DISMECH:<entry-slug>#<phen-slug> CURIEs; "
            "MONDO-typed entries routed to disease_comorbidity.tsv\n"
        )
        hp_writer = csv.DictWriter(
            hp_f,
            fieldnames=HPOA_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        hp_writer.writeheader()

        co_f.write(
            "#description: dismech disease-disease comorbidity annotations "
            "(phenotypes[] entries whose object is a MONDO ID)\n"
        )
        co_f.write(f"#date: {today}\n")
        co_writer = csv.DictWriter(
            co_f,
            fieldnames=COMORBIDITY_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        co_writer.writeheader()

        for yaml_path in sorted(kb_dir.glob("*.yaml")):
            hpoa_rows, comorb_rows = hpoa_rows_for_disorder(yaml_path)
            for row in hpoa_rows:
                hp_writer.writerow(row)
                total_hpoa += 1
            for row in comorb_rows:
                co_writer.writerow(row)
                total_comorb += 1

    return total_hpoa, total_comorb


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Project dismech disorder YAMLs to an HPOA-extended TSV plus a "
            "disease_comorbidity.tsv sidecar."
        )
    )
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument("--out-dir", type=Path, default=Path("output/hpoa"))
    args = parser.parse_args()
    n_hpoa, n_comorb = export(args.kb_dir, args.out_dir)
    print(f"wrote {n_hpoa} HPOA rows -> {args.out_dir / 'phenotype.dismech.hpoa'}")
    print(f"wrote {n_comorb} comorbidity rows -> {args.out_dir / 'disease_comorbidity.tsv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
