"""Ask MONDO whether a stub's term is still a term.

The stub queue's obsolescence signal used to be a string heuristic: MONDO
prefixes a retired concept's label with the word "obsolete", so a stub whose
`label` starts that way names a dead term (`OBSOLETE_LABEL_PATTERN` in
`model.py`). That only fires when the nominating export captured the label
*after* MONDO retired it. When the nomination came first — the normal case,
since a stub is seeded from a list that predates the merge — the stub keeps the
clean label forever and the heuristic stays silent. Zero of the 1,333 committed
stubs match it, while three name terms MONDO has ruled on (dismech#10785).

This module asks the ontology instead, and reads two different facts:

- **Obsolete.** `owl:deprecated true`. When MONDO merged the term into a
  survivor it also carries `IAO:0100001` (`term_replaced_by`) naming it. Exact,
  no false positives, nothing to tune.
- **Scheduled for obsoletion.** `oio:inSubset obo:mondo#obsoletion_candidate`,
  with MONDO's own `rdfs:comment` saying what it will merge into and
  `IAO:0000233` linking the tracker issue. Also exact, and it is the signal that
  actually catches things: the deprecation flag only appears in a MONDO release
  built *after* the merge lands, which can be months later. `MONDO:0859244` from
  dismech#10785 has been a candidate since 2026-04 and is still not deprecated
  in the release the repository pins.

Reading either needs the MONDO semantic-SQL build, a ~1.2 GB download, so
neither may become a hard dependency of `just check-stubs`. Two paths:

- **Live** — `load_obsolescence()` opens the database when it is present and
  returns `None` when it is not, so callers skip with a message rather than
  fail. `dismech-stubs obsolescence` is the census over the whole queue.
- **Offline** — `scripts/enrich_curation_stubs.py` writes the answer into each
  stub as `mondo_obsolete` / `mondo_replaced_by` /
  `mondo_obsoletion_candidate`, so `check_stubs` reports it from the committed
  file with no ontology at hand. That is the path CI takes.
"""

from __future__ import annotations

import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

#: `owl:deprecated true` is the OWL-standard retirement marker.
DEPRECATED_PREDICATE = "owl:deprecated"
#: `IAO:0100001` is `term_replaced_by`: which live term absorbed this one. Only
#: present for a merge; a term retired without a successor has none.
REPLACED_BY_PREDICATE = "IAO:0100001"
#: `IAO:0000233` is `term tracker item`: the MONDO issue the decision was made in.
TRACKER_PREDICATE = "IAO:0000233"
#: The subset MONDO puts a term in once it has decided to retire it, ahead of
#: actually doing so. Both spellings of the OBO-in-OWL prefix appear across
#: semsql builds.
SUBSET_PREDICATES = ("oio:inSubset", "oboInOwl:inSubset")
OBSOLETION_CANDIDATE_SUBSET = "obsoletion_candidate"

_MONDO_PREFIX = "MONDO:"
_OBO_IRI = "http://purl.obolibrary.org/obo/"
_VERSION_RE = re.compile(r"/releases/([0-9]{4}-[0-9]{2}-[0-9]{2})/")
#: MONDO's scheduled-merge comments name the survivor in a fixed phrasing:
#: "...will therefore be obsoleted and replaced with MONDO:0859003".
_PROPOSED_REPLACEMENT_RE = re.compile(r"replaced with (MONDO:[0-9]{7})")


def default_mondo_db() -> Path:
    """Where OAK keeps `mondo.db`.

    OAK resolves `sqlite:obo:mondo` through pystow, which reads `PYSTOW_HOME`
    and nothing else — not `OAK_DB_DIR`. Mirrors the resolution in
    `scripts/fetch_ontology_dbs.sh` so both look in the same place.
    """
    home = os.environ.get("PYSTOW_HOME")
    base = Path(home) if home else Path.home() / ".data"
    return base / "oaklib" / "mondo.db"


def normalize_term(value: object) -> str:
    """Turn whatever the ontology stored into a CURIE.

    `term_replaced_by` is written as a CURIE in some releases and as a full OBO
    IRI in others, and the value lands in `statements.object` or
    `statements.value` depending on whether the axiom was serialized as an
    object property or an annotation. Callers should not have to care.
    """
    text = str(value or "").strip()
    if not text:
        return ""
    if text.startswith(_OBO_IRI):
        text = text[len(_OBO_IRI) :]
    return text.replace("MONDO_", _MONDO_PREFIX, 1) if "MONDO_" in text else text


@dataclass(frozen=True)
class TermStatus:
    """What MONDO says about one term's retirement, live or scheduled."""

    curie: str
    obsolete: bool = False
    #: `term_replaced_by`, once the term is actually obsolete.
    replaced_by: str | None = None
    #: True when MONDO has decided to retire the term but has not yet done so.
    obsoletion_candidate: bool = False
    #: MONDO's own note about the scheduled retirement, plus its tracker issue.
    #: Free text on purpose: it states the decision in MONDO's words, including
    #: whether a replacement is proposed, so nothing here has to parse it right.
    obsoletion_note: str | None = None

    @property
    def proposed_replacement(self) -> str | None:
        """The survivor named in a scheduled-merge note, when there is one.

        Advisory. A note saying the term will be obsoleted with no replacement
        yields `None`, and so does any phrasing this does not recognize — the
        full note is always kept in `obsoletion_note`.
        """
        match = _PROPOSED_REPLACEMENT_RE.search(self.obsoletion_note or "")
        return match.group(1) if match else None

    def describe(self) -> str:
        if self.obsolete and self.replaced_by:
            return f"{self.curie} is obsolete; replaced by {self.replaced_by}"
        if self.obsolete:
            return f"{self.curie} is obsolete with no replacement term"
        proposed = self.proposed_replacement
        if proposed:
            return (
                f"{self.curie} is scheduled for obsoletion; "
                f"MONDO will replace it with {proposed}"
            )
        return f"{self.curie} is scheduled for obsoletion with no replacement proposed"


@dataclass(frozen=True)
class ObsolescenceIndex:
    """Retirement status for a set of MONDO IDs, read from the ontology."""

    terms: dict[str, TermStatus]
    #: MONDO release the answer came from, for attribution in reports.
    version: str | None = None
    #: The database it was read from.
    source: Path | None = None

    def get(self, mondo_id: str) -> TermStatus | None:
        return self.terms.get(mondo_id)

    @property
    def obsolete(self) -> list[TermStatus]:
        return [t for t in self.terms.values() if t.obsolete]

    @property
    def candidates(self) -> list[TermStatus]:
        return [t for t in self.terms.values() if t.obsoletion_candidate]

    def __len__(self) -> int:
        return len(self.terms)


def _mondo_version(conn: sqlite3.Connection) -> str | None:
    try:
        row = conn.execute(
            "select object from statements where subject=? and predicate=?",
            ("obo:mondo.owl", "owl:versionIRI"),
        ).fetchone()
    except sqlite3.DatabaseError:
        return None
    if not row or not row[0]:
        return None
    match = _VERSION_RE.search(str(row[0]))
    return match.group(1) if match else str(row[0])


def read_statuses(
    conn: sqlite3.Connection, mondo_ids: list[str] | None = None
) -> dict[str, TermStatus]:
    """Retirement status for `mondo_ids` (or every MONDO term when omitted).

    Only terms MONDO has ruled on are returned; a live term with no retirement
    decision is absent from the mapping rather than present and empty.
    """
    ids = sorted({i for i in (mondo_ids or []) if i})
    if mondo_ids is not None and not ids:
        return {}

    def query(*predicates: str, subjects: list[str] | None = None):
        # `owl:deprecated` is a literal (`value`), `IAO:0100001` an object
        # reference (`object`), and `inSubset` either depending on the build.
        sql = (
            "select subject, coalesce(nullif(value, ''), object) from statements "
            f"where predicate in ({','.join('?' * len(predicates))})"
        )
        params: list[str] = list(predicates)
        # Narrow to the caller's IDs, or — for the annotations only a handful of
        # terms need — to those terms. Without the second narrowing, asking about
        # the whole ontology would pull every MONDO `rdfs:comment` to annotate a
        # dozen candidates.
        scope = ids if subjects is None else subjects
        if scope:
            sql += f" and subject in ({','.join('?' * len(scope))})"
            params += scope
        return [
            (str(s), str(v or ""))
            for s, v in conn.execute(sql, params)
            if str(s).startswith(_MONDO_PREFIX)
        ]

    deprecated = {
        subject
        # `owl:deprecated false` exists in the wild and is not a retirement.
        for subject, value in query(DEPRECATED_PREDICATE)
        if value.strip().lower() == "true"
    }
    replacements = {
        subject: normalize_term(value)
        for subject, value in query(REPLACED_BY_PREDICATE)
        if normalize_term(value)
    }
    candidates = {
        subject
        for subject, value in query(*SUBSET_PREDICATES)
        if OBSOLETION_CANDIDATE_SUBSET in value
    }
    scheduled = sorted(candidates - deprecated)
    comments = dict(query("rdfs:comment", subjects=scheduled)) if scheduled else {}
    trackers = dict(query(TRACKER_PREDICATE, subjects=scheduled)) if scheduled else {}

    statuses: dict[str, TermStatus] = {}
    for curie in sorted(deprecated | candidates):
        is_candidate = curie in candidates and curie not in deprecated
        note = None
        if is_candidate:
            note = " ".join(
                part for part in (comments.get(curie), trackers.get(curie)) if part
            ).strip()
        statuses[curie] = TermStatus(
            curie=curie,
            obsolete=curie in deprecated,
            replaced_by=replacements.get(curie) if curie in deprecated else None,
            obsoletion_candidate=is_candidate,
            obsoletion_note=note or None,
        )
    return statuses


def load_obsolescence(
    mondo_db: Path | None = None, mondo_ids: list[str] | None = None
) -> ObsolescenceIndex | None:
    """Read retirement status from the MONDO build, or `None` if it is absent.

    Returning `None` rather than raising is the whole point: `check-stubs` runs
    in CI and on every contributor's machine, and neither should be made to
    carry a 1.2 GB ontology to find out whether a YAML file is well formed.
    """
    path = mondo_db or default_mondo_db()
    if not path.exists():
        return None
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        return ObsolescenceIndex(
            terms=read_statuses(conn, mondo_ids),
            version=_mondo_version(conn),
            source=path,
        )
    finally:
        conn.close()
