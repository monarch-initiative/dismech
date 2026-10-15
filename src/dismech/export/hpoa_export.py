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
  ``REFUTE`` becomes a ``NOT``-qualified row; ``SUPPORT`` / missing is a normal
  positive row. ``directness`` is not consulted — an indirectly-evidenced
  phenotype association is still an association, and HPOA has no slot for the
  distinction.
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

Subtypes
--------
Every ``has_subtypes[]`` row bound to its own MONDO term (and not a
``curated_in`` pointer, whose content is exported from the entry it points at)
is emitted as a disease in its own right, so OMIM-level subtypes get their own
rows:

* A phenotype with no ``subtype:`` is asserted of the disease as a whole, and is
  propagated **down** to every such subtype. Its rows on the subtype carry the
  parent's MONDO id in ``inherited_from``, so they can be told apart from what
  the curator stated of the subtype directly.
* A phenotype scoped with ``subtype: X`` is emitted on X directly (empty
  ``inherited_from``), and on X's ``children`` subtypes as inherited from X. It
  is also kept on the parent, as before: a feature of a subtype is a feature
  of some cases of the parent.
* The nearest statement wins. When a phenotype is scoped to a subtype, the
  same HP term is not inherited from above onto that subtype or onto any of its
  ``children``, so a subtype-level ``NOT`` is never contradicted by a positive
  row inherited past it.
* Frequency does not propagate. The parent's frequency is measured across all
  of its subtypes and says nothing about any one of them, so an inherited row
  keeps only an obligate frequency (``HP:0040280`` / ``100%``), which is true
  of every subtype by definition. Absence (``NOT``) propagates unchanged,
  unless its source also carries a positive row for the same HP term: mixed
  evidence is not inherited at all, whether it sits on the parent or on a
  subtype whose ``children`` would inherit it.
* Subtypes without a MONDO term (unbound, or NCIT-only) receive nothing: there
  is no identifier to anchor the rows on.
* A subtype whose MONDO term is another entry's own ``disease_term`` is treated
  like a ``curated_in`` pointer: it inherits nothing, because that entry is its
  curation. Rows stated of it directly are still emitted.

OMIM keying
-----------
``--key omim`` rewrites every row onto the OMIM id MONDO itself declares
equivalent, read from MONDO's SSSOM mapping set (``skos:exactMatch`` rows
only), so the file can be joined against the HPO release:

* ``database_id`` becomes the OMIM id and ``disease_name`` the mapping set's
  OMIM label; the original MONDO id is kept in an extra ``mondo_id`` column.
  ``inherited_from`` stays a MONDO id, since it records dismech provenance.
* An IEA row that cites its own disease cites the OMIM id instead, the
  release's own convention for such rows. An inherited IEA row cites the
  disease it came from, so it keeps that disease's MONDO id.
* A disease with no exact OMIM match, one matching only an OMIM phenotypic
  series (``OMIMPS:``, which HPOA does not key on), or one matching more than
  one OMIM entry gets no rows. Each is listed, with the reason and the number
  of rows withheld, in ``omim_unmapped.tsv`` beside the export.
* The comorbidity sidecar stays MONDO-keyed: it is not an HPOA file.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections.abc import Iterator
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dismech.export.utils import (
    pathophysiology_node_names,
    phenotype_is_upstream_risk_state,
)
from dismech.yaml_io import safe_load_path

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

# supports value -> HPOA qualifier. Anything absent here (SUPPORT, or a missing
# value) becomes a positive row with an empty qualifier.
SUPPORTS_TO_QUALIFIER: dict[Any, str] = {
    "REFUTE": "NOT",
}

# supports values whose evidence item is dropped entirely (no HPOA row).
# NO_EVIDENCE means the cited reference does not mention the claim at all, so
# emitting it as a positive PCS/IEA row would falsely imply the paper supports
# the phenotype-disease link. REFUTE is NOT dropped — it becomes a NOT-qualified
# row via SUPPORTS_TO_QUALIFIER.
DROP_SUPPORTS: frozenset[str] = frozenset({"NO_EVIDENCE"})

# The first 12 columns are the HPOA format, in order. Extra columns go after
# them, never between, so a reader that takes the first 12 still sees HPOA.
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
    "inherited_from",
]

# Written after the HPOA columns in --key omim mode.
OMIM_EXTRA_COLUMNS = ["mondo_id"]

OMIM_UNMAPPED_COLUMNS = ["mondo_id", "disease_name", "reason", "rows_withheld", "candidates"]

# Frequencies that hold for every subtype when they hold for the parent.
OBLIGATE_FREQUENCIES: frozenset[str] = frozenset({FREQUENCY_TO_HP["OBLIGATE"], "100%"})

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
    ``FREQUENT`` / ``VERY_FREQUENT``) and Orphanet-style banded labels whose
    leading word is the canonical band (``Frequent (79-30%)`` -> ``FREQUENT``).
    Returns ``None`` for absent or genuinely ambiguous free text (``Common``,
    ``Rare``, ``Variable``), which is left unmapped rather than guessed.
    """
    if not value:
        return None
    text = re.sub(r"\s*\([^)]*\)\s*$", "", str(value).strip())
    key = re.sub(r"[\s\-]+", "_", text).upper()
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


def export_subtypes(data: dict[str, Any], parent_id: str) -> dict[str, dict[str, Any]]:
    """Subtypes that are exported as diseases, keyed by ``has_subtypes[].name``.

    Only subtypes bound to a MONDO term other than the parent's own, and not
    ``curated_in`` pointers, qualify. ``children`` keeps every listed child name
    so that a chain through an unbound grouping subtype is still followed.
    """
    out: dict[str, dict[str, Any]] = {}
    for sub in data.get("has_subtypes") or []:
        name = sub.get("name")
        if not name:
            continue
        term = ((sub.get("subtype_term") or {}).get("term") or {})
        term_id = term.get("id") or ""
        eligible = (
            term_id.startswith("MONDO:")
            and term_id != parent_id
            and not sub.get("curated_in")
        )
        out[name] = {
            "id": term_id if eligible else "",
            "label": term.get("label") or sub.get("display_name") or name,
            "children": list(sub.get("children") or []),
        }
    return out


def _descendants(name: str, subtypes: dict[str, dict[str, Any]]) -> list[str]:
    """Names reachable from ``name`` through ``children``, excluding itself."""
    seen: list[str] = []
    stack = list(subtypes.get(name, {}).get("children", []))
    while stack:
        child = stack.pop()
        if child == name or child in seen or child not in subtypes:
            continue
        seen.append(child)
        stack.extend(subtypes[child]["children"])
    return seen


def _subtype_targets(
    scope: str | None,
    subtypes: dict[str, dict[str, Any]],
    parent_id: str,
) -> list[tuple[str, str]]:
    """(subtype name, inherited_from) pairs a phenotype is emitted on.

    ``inherited_from`` is empty for the subtype a phenotype is scoped to, and
    otherwise names the disease the row was inherited from.
    """
    if scope is None:
        return [(name, parent_id) for name, sub in subtypes.items() if sub["id"]]
    if scope not in subtypes:
        return []
    source = subtypes[scope]["id"] or parent_id
    targets = [(scope, "")] if subtypes[scope]["id"] else []
    targets += [
        (child, source) for child in _descendants(scope, subtypes) if subtypes[child]["id"]
    ]
    return targets


def hpoa_rows_for_disorder(
    yaml_path: Path,
    propagate_subtypes: bool = True,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Read one disorder YAML and project to (hpoa_rows, comorbidity_rows).

    With ``propagate_subtypes`` (the default), MONDO-bound subtypes get their
    own rows; see the module docstring for the rules. A subtype that is also
    another entry's ``disease_term`` is only recognised by :func:`export`,
    which sees every entry.
    """
    data = safe_load_path(yaml_path) or {}
    return project_disorder(data, yaml_path.stem, propagate_subtypes)


def project_disorder(
    data: dict[str, Any],
    stem: str,
    propagate_subtypes: bool = True,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Project one parsed disorder to (hpoa_rows, comorbidity_rows)."""
    disease = ((data.get("disease_term") or {}).get("term") or {})
    disease_id = disease.get("id") or ""
    if not disease_id.startswith("MONDO:"):
        return [], []
    disease_name = disease.get("label") or data.get("name") or stem
    entry_slug = slugify(stem)
    creation_date = (data.get("creation_date") or "")[:10] or datetime.now(
        UTC
    ).strftime("%Y-%m-%d")
    biocuration = f"{BIOCURATOR}[{creation_date}]"

    hpoa_rows: list[dict[str, str]] = []
    comorb_rows: list[dict[str, str]] = []
    patho_names = pathophysiology_node_names(data)
    subtypes = export_subtypes(data, disease_id) if propagate_subtypes else {}
    # (subtype name, hpo_id) pairs the curator stated of a subtype directly;
    # these are never also inherited onto that subtype from above.
    stated: set[tuple[str, str]] = set()
    pending: list[tuple[dict[str, str], str | None]] = []

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

        # An upstream risk-state phenotype (one driving a pathophysiology node,
        # e.g. a nutritional deficiency) is not a manifestation of the disease.
        # Emitting a phenotype.hpoa row would assert `disease has_phenotype <term>`
        # and invert the curated causal direction, so skip it entirely. This is
        # checked after the MONDO branch above, which keeps its already
        # direction-neutral `biolink:associated_with` comorbidity row; and it is
        # deliberately unguarded by `term_id`, so an ontology-unbound risk state
        # cannot slip through onto the synthetic `DISMECH:` id below.
        if phenotype_is_upstream_risk_state(phenotype, patho_names):
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

        scope = phenotype.get("subtype")
        if scope in subtypes:
            stated.add((scope, hpo_id))

        for ev in evidence_items:
            row = {
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
                "inherited_from": "",
            }
            hpoa_rows.append(row)
            if subtypes:
                pending.append((row, scope))

    hpoa_rows.extend(_subtype_rows(pending, subtypes, stated, disease_id))
    return hpoa_rows, comorb_rows


def _shadowed(
    target: str,
    scope: str | None,
    hpo_id: str,
    subtypes: dict[str, dict[str, Any]],
    stated: set[tuple[str, str]],
) -> bool:
    """Whether a nearer statement of ``hpo_id`` sits between ``scope`` and ``target``.

    A subtype that states the term itself, or any subtype on the way down from
    the row's source to ``target``, takes precedence over the inherited row.
    ``scope`` is ``None`` for a row inherited from the parent, in which case
    every subtype is below it.
    """
    below = set(subtypes) if scope is None else set(_descendants(scope, subtypes))
    for name in below:
        if (name, hpo_id) not in stated:
            continue
        if name == target or target in _descendants(name, subtypes):
            return True
    return False


def _subtype_rows(
    pending: list[tuple[dict[str, str], str | None]],
    subtypes: dict[str, dict[str, Any]],
    stated: set[tuple[str, str]],
    parent_id: str,
) -> list[dict[str, str]]:
    """Copy parent-level rows onto the subtypes they apply to.

    Run after every phenotype has been read, so ``stated`` is complete whatever
    order the phenotypes appear in. Duplicates (two subtype names bound to one
    MONDO term) are emitted once.

    An HP term whose rows at one source (the parent's unscoped rows, or the
    rows scoped to one subtype) carry both a positive and a ``NOT`` row is not
    inherited from that source: its evidence is mixed, and copying a ``NOT``
    meant as "not every patient" onto each subtype below would assert that each
    one lacks the feature. The source's own rows are still emitted.
    """
    qualifiers: dict[tuple[str | None, str], set[str]] = {}
    for base, scope in pending:
        qualifiers.setdefault((scope, base["hpo_id"]), set()).add(base["qualifier"])
    mixed = {key for key, quals in qualifiers.items() if len(quals) > 1}

    rows: list[dict[str, str]] = []
    seen: set[tuple[str, ...]] = set()
    for base, scope in pending:
        hpo_id = base["hpo_id"]
        for name, inherited_from in _subtype_targets(scope, subtypes, parent_id):
            if inherited_from:
                if (scope, hpo_id) in mixed:
                    continue
                if _shadowed(name, scope, hpo_id, subtypes, stated):
                    continue
            sub = subtypes[name]
            row = dict(base)
            row["database_id"] = sub["id"]
            row["disease_name"] = sub["label"]
            row["inherited_from"] = inherited_from
            if inherited_from and row["frequency"] not in OBLIGATE_FREQUENCIES:
                row["frequency"] = ""
            key = tuple(row[c] for c in HPOA_COLUMNS)
            if key in seen:
                continue
            seen.add(key)
            rows.append(row)
    return rows


def load_omim_xrefs(sssom_path: Path) -> dict[str, list[tuple[str, str]]]:
    """MONDO id -> [(OMIM or OMIMPS id, label)], from SSSOM ``skos:exactMatch`` rows."""
    out: dict[str, list[tuple[str, str]]] = {}
    with sssom_path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(
            (line for line in fh if not line.startswith("#")), delimiter="\t"
        ):
            if row.get("predicate_id") != "skos:exactMatch":
                continue
            subject, obj = row.get("subject_id") or "", row.get("object_id") or ""
            if subject.startswith("MONDO:") and obj.startswith(("OMIM:", "OMIMPS:")):
                out.setdefault(subject, []).append((obj, row.get("object_label") or ""))
    return out


def rekey_to_omim(
    rows: list[dict[str, str]],
    xrefs: dict[str, list[tuple[str, str]]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Rewrite MONDO-keyed rows onto OMIM; return (rows, unmapped report).

    Only a disease with exactly one exact OMIM match is kept. See the module
    docstring for what happens to the rest.
    """
    out: list[dict[str, str]] = []
    unmapped: dict[str, dict[str, Any]] = {}
    for row in rows:
        mondo_id = row["database_id"]
        matches = xrefs.get(mondo_id, [])
        omim = [m for m in matches if m[0].startswith("OMIM:")]
        if len(omim) == 1:
            omim_id, omim_label = omim[0]
            new = dict(row)
            new["database_id"] = omim_id
            new["disease_name"] = omim_label or row["disease_name"]
            new["mondo_id"] = mondo_id
            if new["reference"] == mondo_id:
                new["reference"] = omim_id
            out.append(new)
            continue
        if omim:
            reason, candidates = "multiple_omim", [m[0] for m in omim]
        elif matches:
            reason, candidates = "phenotypic_series_only", [m[0] for m in matches]
        else:
            reason, candidates = "no_omim", []
        entry = unmapped.setdefault(
            mondo_id,
            {
                "mondo_id": mondo_id,
                "disease_name": row["disease_name"],
                "reason": reason,
                "rows_withheld": 0,
                "candidates": " ".join(sorted(candidates)),
            },
        )
        entry["rows_withheld"] += 1
    report = sorted(unmapped.values(), key=lambda e: (-e["rows_withheld"], e["mondo_id"]))
    return out, report


def export(
    kb_dir: Path,
    out_dir: Path,
    propagate_subtypes: bool = True,
    key: str = "mondo",
    sssom_path: Path | None = None,
) -> tuple[int, int]:
    """Project every disorder YAML in ``kb_dir`` to TSV files under ``out_dir``.

    ``key="omim"`` writes ``phenotype.dismech.omim.hpoa`` keyed on OMIM, plus
    ``omim_unmapped.tsv``, and needs MONDO's SSSOM mapping set at ``sssom_path``.
    """
    if key not in ("mondo", "omim"):
        raise ValueError(f"unknown key {key!r}; expected 'mondo' or 'omim'")
    if key == "omim" and sssom_path is None:
        raise ValueError("key='omim' needs sssom_path (MONDO's mondo.sssom.tsv)")
    xrefs = load_omim_xrefs(sssom_path) if key == "omim" else {}

    out_dir.mkdir(parents=True, exist_ok=True)
    hpoa_path = out_dir / (
        "phenotype.dismech.omim.hpoa" if key == "omim" else "phenotype.dismech.hpoa"
    )
    comorb_path = out_dir / "disease_comorbidity.tsv"
    today = datetime.now(UTC).strftime("%Y-%m-%d")

    total_hpoa = 0
    total_comorb = 0

    with hpoa_path.open("w", newline="") as hp_f, comorb_path.open(
        "w", newline=""
    ) as co_f:
        hp_f.write(
            "#description: dismech disease-phenotype annotations, "
            + (
                "OMIM-keyed via MONDO SSSOM exactMatch (mondo_id column keeps "
                "the source), HPOA-extended\n"
                if key == "omim"
                else "MONDO-anchored, HPOA-extended\n"
            )
        )
        hp_f.write(f"#date: {today}\n")
        hp_f.write(f"#version: {HPOA_VERSION}\n")
        hp_f.write("#tracker: https://github.com/monarch-initiative/dismech\n")
        hp_f.write(
            "#rules: human evidence only (MODEL_ORGANISM excluded); "
            "NO_EVIDENCE dropped; REFUTE/EXCLUDED-frequency -> NOT; "
            "reference column may be PMID/ORPHA/DOI/clinicaltrials/CGGV; "
            "untyped phenotypes get DISMECH:<entry-slug>#<phen-slug> CURIEs; "
            "MONDO-typed entries routed to disease_comorbidity.tsv"
            + (
                "; unscoped phenotypes propagated to MONDO-bound subtypes "
                "(inherited_from = source disease; frequency dropped unless obligate)"
                if propagate_subtypes
                else ""
            )
            + "\n"
        )
        hp_writer = csv.DictWriter(
            hp_f,
            fieldnames=HPOA_COLUMNS + (OMIM_EXTRA_COLUMNS if key == "omim" else []),
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

        all_hpoa: list[dict[str, str]] = []
        entry_ids: set[str] = set()
        for yaml_path in sorted(kb_dir.glob("*.yaml")):
            data = safe_load_path(yaml_path) or {}
            entry_ids.add(((data.get("disease_term") or {}).get("term") or {}).get("id") or "")
            hpoa_rows, comorb_rows = project_disorder(
                data, yaml_path.stem, propagate_subtypes=propagate_subtypes
            )
            all_hpoa.extend(hpoa_rows)
            for row in comorb_rows:
                co_writer.writerow(row)
                total_comorb += 1

        # A subtype whose MONDO term is another entry's own disease_term is
        # curated there, exactly as a `curated_in` pointer would say: inheriting
        # the parent's pooled phenotypes onto it would mix two curations of one
        # disease. Rows the parent states of that subtype directly are kept.
        kept = [
            row
            for row in all_hpoa
            if not (row["inherited_from"] and row["database_id"] in entry_ids)
        ]
        if key == "omim":
            kept, unmapped = rekey_to_omim(kept, xrefs)
            with (out_dir / "omim_unmapped.tsv").open("w", newline="") as un_f:
                un_writer = csv.DictWriter(
                    un_f,
                    fieldnames=OMIM_UNMAPPED_COLUMNS,
                    delimiter="\t",
                    lineterminator="\n",
                )
                un_writer.writeheader()
                un_writer.writerows(unmapped)
        for row in kept:
            hp_writer.writerow(row)
            total_hpoa += 1

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
    parser.add_argument(
        "--no-subtypes",
        dest="propagate_subtypes",
        action="store_false",
        help="Emit parent diseases only, without per-subtype rows.",
    )
    parser.add_argument(
        "--key",
        choices=("mondo", "omim"),
        default="mondo",
        help="Disease id to key rows on. 'omim' needs --sssom.",
    )
    parser.add_argument(
        "--sssom",
        type=Path,
        help="MONDO's SSSOM mapping set (mondo.sssom.tsv), for --key omim.",
    )
    args = parser.parse_args()
    if args.key == "omim" and args.sssom is None:
        parser.error("--key omim needs --sssom PATH (MONDO's mondo.sssom.tsv)")
    n_hpoa, n_comorb = export(
        args.kb_dir, args.out_dir, args.propagate_subtypes, args.key, args.sssom
    )
    name = "phenotype.dismech.omim.hpoa" if args.key == "omim" else "phenotype.dismech.hpoa"
    print(f"wrote {n_hpoa} HPOA rows -> {args.out_dir / name}")
    if args.key == "omim":
        unmapped_path = args.out_dir / "omim_unmapped.tsv"
        with unmapped_path.open() as fh:
            n_unmapped = sum(1 for _ in fh) - 1
        print(f"{n_unmapped} diseases had no single exact OMIM match -> {unmapped_path}")
    print(f"wrote {n_comorb} comorbidity rows -> {args.out_dir / 'disease_comorbidity.tsv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
