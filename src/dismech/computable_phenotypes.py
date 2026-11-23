"""Computable phenotypes: convert library records to ``Definition`` blocks and
check transcribed code lists against their sources.

Two jobs live here.

``definition_from_hdruk`` turns an HDR UK Phenotype Library record (see
:mod:`dismech.structured_sources.hdruk`) into a dismech ``Definition`` dict:
one criteria set whose items are the record's concepts, each carrying a
``CodeList`` copied code for code from the library's resolved export, and one
evidence item quoting the record's own definition text from the cached
``HDRUK:`` reference. The fragment is a starting point for a curator, not a
finished entry: validation status, scope wording and any criteria-set logic the
library states only in prose are left for a person to read and fill.

``check_codelists`` is the gate for any ``CodeList`` in ``kb/``: every code
must carry its code system's CURIE prefix and syntax, and when the list names
a cached ``source_reference`` every code (with its label) must appear in that
cached record. That is the code-list form of the rule that a CURIE is read
from a source in the same step it is written: a code typed from memory, or a
label tidied by hand, fails.
"""

from __future__ import annotations

import csv
import re
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from dismech.structured_sources.hdruk import PhenotypeRecord

#: Code syntax per ``CodeSystemEnum`` value (the part after the prefix).
CODE_PATTERNS: dict[str, re.Pattern] = {
    "ICD9CM": re.compile(r"^(\d{3}(\.\d{1,2})?|V\d{2}(\.\d{1,2})?|E\d{3}(\.\d)?)$"),
    "ICD10": re.compile(r"^[A-Z]\d{2}(\.?[0-9A-Z]{1,4})?$"),
    "ICD10CM": re.compile(r"^[A-Z]\d[0-9A-Z](\.[0-9A-Z]{1,4})?$"),
    "SNOMEDCT": re.compile(r"^\d{6,18}$"),
    "READ2": re.compile(r"^[0-9A-Za-z.]{5}(\d{2})?$"),
    "CTV3": re.compile(r"^[0-9A-Za-z.]{5}$"),
    "OPCS4": re.compile(r"^[A-Z]\d{2}(\.?\d{1,2})?$"),
    "LOINC": re.compile(r"^\d+-\d$"),
    "RXNORM": re.compile(r"^\d+$"),
}


def _first_sentence(text: str, limit: int = 400) -> str:
    """The first sentence of the first paragraph, for an evidence snippet.

    >>> _first_sentence("At the date, a patient is X. More text.")
    'At the date, a patient is X.'
    >>> _first_sentence("No full stop here")
    'No full stop here'
    """
    paragraph = text.split("\n\n", 1)[0].strip()
    match = re.match(r"(.+?[.:])(\s|$)", paragraph)
    sentence = match.group(1) if match else paragraph
    return sentence[:limit].rstrip()


def definition_from_hdruk(record: PhenotypeRecord) -> dict:
    """Build a dismech ``Definition`` dict from an HDR UK phenotype record.

    Codes in coding systems with no dismech code system (CPRD medcodes, dm+d,
    BNF, ...) are dropped and named in ``notes``.
    """
    reference = f"HDRUK:{record.phenotype_id}"
    items: list[dict] = []
    dropped: list[str] = []
    for (concept, system), codes in record.concepts().items():
        prefix = codes[0].prefix
        if prefix is None:
            dropped.append(f"{system} ({len(codes)} codes)")
            continue
        code_list = {
            "name": concept,
            "code_system": prefix,
            "source_reference": reference,
            "codes": [
                {"id": c.curie, "label": c.description}
                for c in sorted(codes, key=lambda c: c.code)
            ],
        }
        if "/" in concept:
            # OpenCodelists concepts are named <owner>/<list>/<version>.
            code_list["code_system_version"] = concept
        items.append({"preferred_term": concept, "code_lists": [code_list]})
    definition: dict = {
        "name": f"HDR UK Phenotype Library {record.phenotype_id}: {record.name}",
        "definition_type": "PHENOTYPE_ALGORITHM",
        "source_reference": reference,
        "description": (
            f"HDR UK Phenotype Library phenotype {record.phenotype_id} "
            f"(version {record.version_id}; {record.fields.get('Template') or 'untyped'} template). "
            "A record qualifies if it carries any code in any of the code lists below."
        ),
    }
    if record.fields.get("Data sources"):
        definition["scope"] = f"UK EHR: {record.fields['Data sources']}"
    definition["criteria_sets"] = [
        {
            "name": "Qualifying codes",
            "description": "Any one code from any concept's code list qualifies.",
            "minimum_required": 1,
            "inclusion_criteria": items,
        }
    ]
    snippet = _first_sentence(record.definition)
    if snippet:
        definition["evidence"] = [
            {
                "reference": reference,
                "supports": "SUPPORT",
                "evidence_source": "OTHER",
                "reference_title": record.name,
                "snippet": snippet,
                "explanation": (
                    "Opening of the phenotype library's own definition of this "
                    "phenotype; the code lists are checked code by code against the "
                    "same record by `just check-codelists`."
                ),
            }
        ]
    notes = [f"Transcribed from {record.url} by `just hdruk-definition`."]
    if record.ontology:
        notes.append(
            "HDR UK tags the record "
            + ", ".join(f"{curie} ({label})" for curie, label in record.ontology)
            + "."
        )
    if dropped:
        notes.append(
            "Coding systems with no dismech code system, not transcribed: "
            + ", ".join(dropped)
            + "."
        )
    if not record.validation:
        notes.append("The library record has no validation section.")
    definition["notes"] = " ".join(notes)
    return definition


# ----- code-list checking -----


@dataclass(frozen=True)
class Finding:
    path: Path
    location: str
    code: str
    problem: str

    def format(self) -> str:
        return f"{self.path}: {self.location}: {self.code}: {self.problem}"


def iter_code_lists(doc: object, path: str = "") -> Iterator[tuple[str, dict]]:
    """Yield ``(location, code_list)`` for every ``code_lists`` entry in a document.

    >>> doc = {"definitions": [{"criteria_sets": [{"inclusion_criteria": [
    ...     {"code_lists": [{"code_system": "ICD10", "codes": []}]}]}]}]}
    >>> [loc for loc, _ in iter_code_lists(doc)]
    ['definitions[0].criteria_sets[0].inclusion_criteria[0].code_lists[0]']
    """
    if isinstance(doc, dict):
        for key, value in doc.items():
            child = f"{path}.{key}" if path else key
            if key == "code_lists" and isinstance(value, list):
                for i, code_list in enumerate(value):
                    if isinstance(code_list, dict):
                        yield f"{child}[{i}]", code_list
            else:
                yield from iter_code_lists(value, child)
    elif isinstance(doc, list):
        for i, item in enumerate(doc):
            yield from iter_code_lists(item, f"{path}[{i}]")


def _normalize(text: str) -> str:
    return " ".join(text.split())


def cached_body(reference: str, cache_dir: Path) -> str | None:
    """The body of a cached reference, or ``None`` if it is not cached."""
    path = cache_dir / (reference.replace(":", "_").replace("/", "_") + ".md")
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    parts = text.split("\n---\n", 1)
    return parts[1] if len(parts) == 2 else text


def code_in_source(curie: str, label: str, body: str) -> bool:
    """True when a code and its label are transcribed from ``body``.

    An ``HDRUK:`` body has a ``| <CURIE> | <label> |`` row; any other source
    must contain ``<code> <label>`` in its text (a PDF code table).

    >>> code_in_source("ICD10:D57.0", "Sickle-cell anaemia with crisis",
    ...     "| ICD10:D57.0 | Sickle-cell anaemia with crisis | c |")
    True
    >>> code_in_source("ICD9CM:282.41", "Sickle cell thalassemia without crisis",
    ...     "282.41 Sickle cell thalassemia without crisis 282.42")
    True
    >>> code_in_source("ICD9CM:282.60", "HbSS disease", "282.61 HbSS disease")
    False
    """
    body = _normalize(body)
    if f"| {curie} | {_normalize(label)} |" in body:
        return True
    code = curie.split(":", 1)[1]
    return (
        re.search(
            rf"(?<![\w.]){re.escape(code)} {re.escape(_normalize(label))}(?![\w])", body
        )
        is not None
    )


def _icd10cm_labels(cache_root: Path) -> dict[str, str]:
    path = cache_root / "icd10cm" / "terms.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        return {
            row["curie"]: row["label"]
            for row in csv.DictReader(handle)
            if row.get("curie")
        }


def check_document(
    doc: object, path: Path, references_dir: Path, term_cache_dir: Path
) -> list[Finding]:
    """Check every code list in one parsed KB document."""
    findings: list[Finding] = []
    icd10cm = None
    for location, code_list in iter_code_lists(doc):
        system = code_list.get("code_system")
        pattern = CODE_PATTERNS.get(system)
        reference = code_list.get("source_reference")
        body = cached_body(reference, references_dir) if reference else None
        if reference and body is None:
            findings.append(
                Finding(
                    path,
                    location,
                    reference,
                    "source_reference is not cached; run `just fetch-reference`",
                )
            )
        for code in code_list.get("codes") or []:
            curie = str(code.get("id", ""))
            label = str(code.get("label", ""))
            prefix, _, local = curie.partition(":")
            if prefix != system:
                findings.append(
                    Finding(
                        path,
                        location,
                        curie,
                        f"prefix does not match code_system {system}",
                    )
                )
                continue
            if pattern is not None and not pattern.match(local):
                findings.append(
                    Finding(path, location, curie, f"not a well-formed {system} code")
                )
            if body is not None and not code_in_source(curie, label, body):
                findings.append(
                    Finding(
                        path,
                        location,
                        curie,
                        f"code and label not found in {reference}",
                    )
                )
            if system == "ICD10CM":
                if icd10cm is None:
                    icd10cm = _icd10cm_labels(term_cache_dir)
                cached = icd10cm.get(curie)
                if cached is not None and cached != label:
                    findings.append(
                        Finding(
                            path,
                            location,
                            curie,
                            f"label differs from ICD-10-CM: {cached!r}",
                        )
                    )
    return findings
