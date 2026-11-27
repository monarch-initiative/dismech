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

import yaml

from dismech.structured_sources.hdruk import PhenotypeRecord
from dismech.yaml_io import safe_load

#: Code syntax per ``CodeSystemEnum`` value (the part after the prefix).
CODE_PATTERNS: dict[str, re.Pattern] = {
    # ICD-9-CM and ICD-10-CM are accepted with or without the dot: EHR and
    # claims extracts commonly store them dotless (441.3 as 4413).
    "ICD9CM": re.compile(r"^(\d{3}(\.?\d{1,2})?|V\d{2}(\.?\d{1,2})?|E\d{3}(\.?\d)?)$"),
    "ICD10": re.compile(r"^[A-Z]\d{2}(\.?[0-9A-Z]{1,4})?$"),
    "ICD10CM": re.compile(r"^[A-Z]\d[0-9A-Z](\.?[0-9A-Z]{1,4})?$"),
    "SNOMEDCT": re.compile(r"^\d{6,18}$"),
    "READ2": re.compile(r"^[0-9A-Za-z.]{5}(\d{2})?$"),
    "CTV3": re.compile(r"^[0-9A-Za-z.]{5}$"),
    "OPCS4": re.compile(r"^[A-Z]\d{2}(\.?\d{1,2})?$"),
    "LOINC": re.compile(r"^\d+-\d$"),
    "RXNORM": re.compile(r"^\d+$"),
}


def _first_sentence(text: str, limit: int = 400, min_words: int = 6) -> str:
    """The first real sentence of a definition, for an evidence snippet.

    Headings ("Objectives:", "The database:") and title-only lines are
    skipped: a sentence needs ``min_words`` words, because a shorter snippet
    asserts nothing and fails ``check-snippet-length``.

    >>> _first_sentence("At the date, a patient is coded with X. More text.")
    'At the date, a patient is coded with X.'
    >>> _first_sentence("Objectives:\\n\\nWe identify people with X in primary care. More.")
    'We identify people with X in primary care.'
    >>> _first_sentence("Takayasu arteritis")
    ''

    A sentence longer than ``limit`` is cut at the last whole word, because
    a snippet must start and end on whole words to verify.

    >>> _first_sentence("one two three four five six seven", limit=12)
    'one two'
    """
    for paragraph in text.split("\n\n"):
        for sentence in re.split(r"(?<=[.:])\s+", paragraph.strip()):
            sentence = sentence.strip()
            if len(sentence.split()) < min_words:
                continue
            if len(sentence) > limit:
                cut = sentence[: limit + 1]
                sentence = cut.rsplit(None, 1)[0] if cut[-1:].strip() else cut
            return sentence.rstrip()
    return ""


def definition_from_hdruk(record: PhenotypeRecord) -> dict:
    """Build a dismech ``Definition`` dict from an HDR UK phenotype record.

    Codes in coding systems with no dismech code system (CPRD medcodes, dm+d,
    BNF, ...) are dropped and named in ``notes``.
    """
    reference = f"HDRUK:{record.phenotype_id}"
    items: list[dict] = []
    dropped: list[str] = []
    malformed: dict[str, list[str]] = {}
    excluded: list[str] = []
    for (concept, system), all_codes in record.concepts().items():
        if is_exclusion_concept(concept):
            excluded.append(concept)
            continue
        prefix = all_codes[0].prefix
        if prefix is None:
            dropped.append(f"{system} ({len(all_codes)} codes)")
            continue
        codes = [c for c in all_codes if well_formed(prefix, c.code)]
        for c in all_codes:
            if c not in codes:
                malformed.setdefault(system, []).append(c.code)
        if not codes:
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
            "The code lists below are the library's resolved code export, one per "
            "concept. How the concepts combine (any one code, a code together with "
            "a prescription, a count within a window) is set out in the library's "
            "own definition and implementation text, cached with the record; this "
            "transcription does not restate it."
        ),
    }
    if record.fields.get("Data sources"):
        definition["scope"] = f"UK EHR: {record.fields['Data sources']}"
    definition["criteria_sets"] = [
        {
            "name": "Library concept code lists",
            "description": "One item per concept in the library's resolved code export.",
            "inclusion_criteria": items,
        }
    ]
    mondo = [(c, label) for c, label in record.ontology if c.startswith("MONDO:")]
    if mondo:
        snippet = f"Ontology | {mondo[0][0]} {mondo[0][1]}".strip()
        explanation = (
            "The library record's own ontology tag names this disease; the code "
            "lists are checked code by code against the same record by "
            "`just check-codelists`."
        )
    else:
        snippet = _first_sentence(record.definition)
        explanation = (
            "Opening of the phenotype library's own definition of this "
            "phenotype; the code lists are checked code by code against the "
            "same record by `just check-codelists`."
        )
    if snippet:
        definition["evidence"] = [
            {
                "reference": reference,
                "supports": "SUPPORT",
                "evidence_source": "OTHER",
                "reference_title": record.name,
                "snippet": snippet,
                "explanation": explanation,
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
    if excluded:
        notes.append(
            "Concepts the library record names as excluded codes are not "
            "transcribed: " + "; ".join(excluded) + "."
        )
    for system, bad in sorted(malformed.items()):
        examples = ", ".join(dict.fromkeys(bad[:3]))
        notes.append(
            f"{len(bad)} {system} entries in the library record are not "
            f"well-formed codes of that system (e.g. {examples}), so they are "
            "not transcribed."
        )
    if record.omitted:
        notes.append(
            "Codes omitted from this transcription and from the cached record: "
            + ", ".join(f"{n} {system}" for system, n in sorted(record.omitted.items()))
            + ". They remain in the library record and can be added later."
        )
    if not record.validation:
        notes.append("The library record has no validation section.")
    definition["notes"] = " ".join(notes)
    return definition


_EXCLUSION_CONCEPT_RE = re.compile(
    r"^\s*(?:excluded|exclusions?)\b|\(\s*exclusion codes?\s*\)", re.IGNORECASE
)


def is_exclusion_concept(name: str) -> bool:
    """True for a concept the library record names as a list of excluded codes.

    A resolved export lists every concept's codes, including concepts the
    authors kept to document what they rejected. Those are not qualifying
    codes. A qualifier inside a name ("excluding gabapentin") is not one.

    >>> is_exclusion_concept("Excluded codes - codes not indicating epilepsy")
    True
    >>> is_exclusion_concept("Type 2 Diabetes (Exclusion Codes) - Primary Care")
    True
    >>> is_exclusion_concept("Anti-seizure medication codes (excluding gabapentin)")
    False
    """
    return bool(_EXCLUSION_CONCEPT_RE.search(name))


def well_formed(prefix: str, code: str) -> bool:
    """True when ``code`` has the syntax of code system ``prefix``.

    >>> well_formed("ICD10", "D57.0"), well_formed("ICD10", "A15-A19")
    (True, False)
    >>> well_formed("READ2", "4109NC"), well_formed("ICD9CM", "4413")
    (False, True)
    """
    pattern = CODE_PATTERNS.get(prefix)
    return pattern is None or bool(pattern.match(code))


def transcribable_codes(record: PhenotypeRecord) -> int:
    """How many of a record's codes have a dismech code system and its syntax.

    A record with none (every code a CPRD medcode, dm+d, malformed or omitted
    SNOMED CT code) yields a definition with no code lists, so it is not
    imported.
    """
    return sum(
        1
        for code in record.codes
        if code.prefix is not None
        and well_formed(code.prefix, code.code)
        and not is_exclusion_concept(code.concept)
    )


def mondo_tag_conflict(record: PhenotypeRecord, entry: dict) -> str | None:
    """Explain why a record's own MONDO tag rules out this entry, else ``None``.

    The entry's MONDO terms are its ``disease_term``, its ``has_subtypes``
    terms, and its ``skos:exactMatch`` MONDO mappings. A record with no MONDO
    tag is the curator's call and is not refused.

    >>> from dismech.structured_sources.hdruk import PhenotypeRecord
    >>> r = PhenotypeRecord("PH1", 1, "x", ontology=[("MONDO:0011382", "scd")])
    >>> mondo_tag_conflict(r, {"disease_term": {"term": {"id": "MONDO:0011382"}}}) is None
    True
    >>> mondo_tag_conflict(r, {"disease_term": {"term": {"id": "MONDO:0007915"}}})
    'HDR UK tags PH1 MONDO:0011382, not any of the entry MONDO terms (MONDO:0007915)'
    """
    tags = [curie for curie, _ in record.ontology if curie.startswith("MONDO:")]
    terms = entry_mondo_terms(entry)
    if not tags or set(tags) & terms:
        return None
    return (
        f"HDR UK tags {record.phenotype_id} {', '.join(tags)}, "
        f"not any of the entry MONDO terms ({', '.join(sorted(terms))})"
    )


def entry_mondo_terms(entry: dict) -> set[str]:
    """The MONDO terms an entry is about: its disease_term, subtypes and exact matches.

    >>> sorted(entry_mondo_terms({
    ...     "disease_term": {"term": {"id": "MONDO:1"}},
    ...     "has_subtypes": [{"subtype_term": {"term": {"id": "MONDO:2"}}}],
    ...     "mappings": {"mondo_mappings": [
    ...         {"term": {"id": "MONDO:3"}, "mapping_predicate": "skos:exactMatch"},
    ...         {"term": {"id": "MONDO:4"}, "mapping_predicate": "skos:broadMatch"}]}}))
    ['MONDO:1', 'MONDO:2', 'MONDO:3']
    """

    def term_id(descriptor: object) -> str | None:
        return ((descriptor or {}).get("term") or {}).get("id")

    terms = {term_id(entry.get("disease_term"))}
    for subtype in entry.get("has_subtypes") or []:
        terms.add(term_id(subtype.get("subtype_term")))
    for mapping in (entry.get("mappings") or {}).get("mondo_mappings") or []:
        if mapping.get("mapping_predicate") == "skos:exactMatch":
            terms.add((mapping.get("term") or {}).get("id"))
    return {t for t in terms if t}


def cited_references(entry: dict) -> set[str]:
    """The ``source_reference`` of every definition an entry already carries."""
    return {d.get("source_reference") for d in entry.get("definitions") or []}


def append_definitions(path: Path, definitions: list[dict]) -> list[str]:
    """Append definitions to a KB entry's ``definitions:`` block, in place.

    Definitions whose ``source_reference`` the entry already carries are
    skipped, so a re-run adds nothing. The rest of the file is left byte for
    byte as it was: the new items are inserted as text at the end of the
    existing block, or as a new block at the end of the file. Returns the
    names of the definitions added.
    """
    text = path.read_text(encoding="utf-8")
    doc = safe_load(text)
    before = list(doc.get("definitions") or [])
    present = {d.get("source_reference") for d in before}
    new = [d for d in definitions if d.get("source_reference") not in present]
    if not new:
        return []
    fragment = yaml.safe_dump(new, sort_keys=False, allow_unicode=True, width=100)
    lines = text.splitlines(keepends=True)
    start = next(
        (i for i, line in enumerate(lines) if line.rstrip() == "definitions:"), None
    )
    if start is None and any(line.startswith("definitions:") for line in lines):
        raise RuntimeError(
            f"{path} has a definitions: line that is not a block (e.g. "
            "`definitions: []`); edit it by hand"
        )
    if start is None:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines.append("definitions:\n" + fragment)
    else:
        end = next(
            (
                i
                for i in range(start + 1, len(lines))
                if re.match(r"[A-Za-z_]", lines[i])
            ),
            len(lines),
        )
        lines.insert(end, fragment)
    updated = "".join(lines)
    after = safe_load(updated)
    if after.get("definitions") != before + new or {
        k: v for k, v in after.items() if k != "definitions"
    } != {k: v for k, v in doc.items() if k != "definitions"}:
        raise RuntimeError(
            f"appending definitions would change other content of {path}"
        )
    path.write_text(updated, encoding="utf-8")
    return [d["name"] for d in new]


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

    A PDF that gives the label in parentheses after the code also matches.

    >>> code_in_source("ICD9CM:441.3", "Abdominal aortic aneurysm, ruptured",
    ...     "• 441.3 (Abdominal aortic aneurysm, ruptured) *Note")
    True
    """
    body = _normalize(body)
    # The cache escapes a literal "|" in a cell as "\\|".
    cell = _normalize(label).replace("|", r"\|")
    if f"| {curie} | {cell} |" in body:
        return True
    code = curie.split(":", 1)[1]
    label_re = re.escape(_normalize(label))
    return (
        re.search(
            rf"(?<![\w.]){re.escape(code)} (?:{label_re}(?![\w])|\({label_re}\))", body
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
